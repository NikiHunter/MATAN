#!/usr/bin/env python3
"""Dependency-free structural checks for the trilingual MathInMind vault."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ocr_issues  # noqa: E402
from course_layout import (CHAPTERS, LAST_LECTURE, LECTURE_CHAPTERS, SEMESTERS,  # noqa: E402
                           TRANSLATED_UP_TO, semester_of)
from mdtext import inline_spans, to_dollar_math  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "MathInMind"
LANGUAGES = ("en", "ru", "es")
SUPPORTING = ("index.md", "00-notation.md", "formula-sheet.md", "glossary.md", "term-index.md")
EXPECTED = set(CHAPTERS + SUPPORTING)
LECTURE_DIRECTORY = "lectures-2025-26"
LECTURE_BATCHES = {
    "31-38": tuple(f"lecture-{n}.md" for n in ("31-32", "33-34", "35", "36", "37-38")),
    "39-44": tuple(f"lecture-{n}.md" for n in ("39-40", "41-42", "43-44")),
    "45-50": tuple(f"lecture-{n}.md" for n in ("45-46", "47-48", "49-50")),
    "51-54": tuple(f"lecture-{n}.md" for n in ("51-52", "53", "54")),
    "55-60": tuple(f"lecture-{n}.md" for n in ("55-56", "57-58", "59-60")),
    "61-64": tuple(f"lecture-{n}.md" for n in ("61-62", "63-64")),
}
# Batches transcribed from notebook photos and video frames (ocr/raw/pNNN.md)
# instead of PDFs; their manifests map pages to lectures.
NOTEBOOK_BATCHES: tuple[str, ...] = ("65-84",)
PAGE_ANCHOR_ANY = re.compile(r'<a id="(p\d{3})"></a>')
PAGE_ANCHOR_LINE = re.compile(r'(?m)^<a id="(p\d{3})"></a>$')
GENERATED_FRAGMENT = re.compile(r"^(?:sec|def|thm|lem|cor|rem|prop)-[\d-]+$|^p\d{3}$")
# One level of brackets in a label is needed for interval notation in image alt text.
LINK_RE = re.compile(r"(!?)\[(?:[^\[\]\n]|\[[^\[\]\n]*\])*\]\(([^)\n]+)\)")

errors: list[str] = []


def fail(path: Path | str, message: str) -> None:
    label = str(path.relative_to(ROOT)) if isinstance(path, Path) else path
    errors.append(f"{label}: {message}")


def without_fenced_code(text: str) -> str:
    return re.sub(r"^```.*?^```\s*$", "", text, flags=re.MULTILINE | re.DOTALL)


def without_inline_code(text: str) -> str:
    lines = []
    for line in text.split("\n"):
        for start, end, kind in reversed(inline_spans(line)):
            if kind == "code":
                line = line[:start] + line[end:]
        lines.append(line)
    return "\n".join(lines)


def check_frontmatter(path: Path, lang: str, text: str) -> None:
    if not text.startswith("---\n"):
        fail(path, "missing YAML frontmatter")
        return
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(path, "unterminated YAML frontmatter")
        return
    frontmatter = text[4:end]
    if not re.search(rf"(?m)^lang:\s*{re.escape(lang)}\s*$", frontmatter):
        fail(path, f"frontmatter must declare lang: {lang}")
    if not re.search(r"(?m)^title:\s*.+$", frontmatter):
        fail(path, "frontmatter is missing a title")
    if path.name in CHAPTERS:
        expected_number = int(path.name[:2])
        if not re.search(rf"(?m)^chapter:\s*{expected_number}\s*$", frontmatter):
            fail(path, f"frontmatter must declare chapter: {expected_number}")
        if not re.search(r"(?m)^part:\s*.+$", frontmatter):
            fail(path, "chapter frontmatter is missing part")


def check_fences_and_math(path: Path, text: str) -> None:
    fence_lines = [line for line in text.splitlines() if line.lstrip().startswith("```")]
    if len(fence_lines) % 2:
        fail(path, "unbalanced fenced code blocks")

    in_mermaid = False
    mermaid_body: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```mermaid"):
            if in_mermaid:
                fail(path, "nested Mermaid fence")
            in_mermaid = True
            mermaid_body = []
            continue
        if in_mermaid and stripped == "```":
            meaningful = [item.strip() for item in mermaid_body if item.strip()]
            if not meaningful or not re.fullmatch(r"flowchart (TD|TB|BT|LR|RL)", meaningful[0]):
                fail(path, "Mermaid diagram must start with a simple flowchart declaration")
            joined = "\n".join(meaningful)
            for forbidden in ("click ", "href", "classDef", "style ", "%%{", "<script"):
                if forbidden in joined:
                    fail(path, f"non-portable Mermaid construct: {forbidden.strip()}")
            in_mermaid = False
            continue
        if in_mermaid:
            mermaid_body.append(line)
    if in_mermaid:
        fail(path, "unterminated Mermaid block")

    prose = without_fenced_code(text)
    if prose.count("$$") % 2:
        fail(path, "unbalanced display-math delimiters $$")
    unescaped_dollars = len(re.findall(r"(?<!\\)\$", prose))
    if unescaped_dollars % 2:
        fail(path, "possibly unbalanced inline-math dollar delimiters")
    html_prose = re.sub(r"`[^`\n]*`", "", prose)
    if html_prose.count("<details>") != html_prose.count("</details>"):
        fail(path, "unbalanced <details> elements")
    if html_prose.count("<summary>") != html_prose.count("</summary>"):
        fail(path, "unbalanced <summary> elements")
    # A bare ']]' also ends ordinary alt text such as ![interval [a,b]](...).
    if re.search(r"\[\[[^\n]*?\]\]", without_inline_code(prose)):
        fail(path, "wiki-style links are not portable to GitHub; use relative Markdown links")


def local_links(text: str) -> list[tuple[bool, str]]:
    """Return (is_image, decoded_local_path), excluding URLs and bare anchors."""
    result = []
    for match in LINK_RE.finditer(without_fenced_code(text)):
        raw = match.group(2).strip()
        if raw.startswith("<") and ">" in raw:
            raw = raw[1 : raw.index(">")]
        else:
            raw = raw.split(maxsplit=1)[0]
        raw = unquote(raw)
        if not raw or raw.startswith(("#", "http://", "https://", "mailto:", "obsidian:")):
            continue
        target = raw.split("#", 1)[0].split("?", 1)[0]
        if target:
            result.append((bool(match.group(1)), target))
    return result


def check_links(path: Path, text: str) -> None:
    for _, raw in local_links(text):
        target = Path(raw)
        if target.is_absolute():
            fail(path, f"absolute local link: {raw}")
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            fail(path, f"link escapes repository: {raw}")
            continue
        if not resolved.exists():
            fail(path, f"broken local link: {raw}")
    check_fragments(path, text)


def check_fragments(path: Path, text: str) -> None:
    """Links to generated anchors (sections, numbered statements, pages) must hit an <a id>."""
    cache: dict[Path, str] = {}
    for match in LINK_RE.finditer(without_fenced_code(text)):
        raw = match.group(2).strip()
        raw = raw[1:raw.index(">")] if raw.startswith("<") and ">" in raw else raw.split(maxsplit=1)[0]
        raw = unquote(raw)
        if raw.startswith(("http://", "https://", "mailto:", "obsidian:")) or "#" not in raw:
            continue
        target_part, _, fragment = raw.partition("#")
        if not GENERATED_FRAGMENT.match(fragment):
            continue
        target = (path.parent / target_part).resolve() if target_part else path.resolve()
        if target.suffix != ".md" or not target.is_file():
            continue
        if target not in cache:
            cache[target] = target.read_text(encoding="utf-8")
        if f'<a id="{fragment}"></a>' not in cache[target]:
            fail(path, f"link to a missing anchor: {raw}")


def metadata(text: str) -> dict[str, str]:
    """Read the simple scalar frontmatter used here, without a YAML dependency."""
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return {}
    header = text[4 : text.index("\n---\n", 4)]
    result = {}
    for key, value in re.findall(r"(?m)^([a-z_]+):\s*(.+)$", header):
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        result[key] = value
    return result


def number_range(value: str) -> list[int]:
    """Expand 01-02 or 24-25-26, rejecting descending or gapped enumerations."""
    if not re.fullmatch(r"\d+(?:[-–]\d+)*", value):
        raise ValueError(f"invalid number range: {value}")
    numbers = [int(n) for n in re.split(r"[-–]", value)]
    expanded = list(range(numbers[0], numbers[-1] + 1))
    if len(numbers) > 1 and numbers[0] >= numbers[-1]:
        raise ValueError(f"descending or repeated number range: {value}")
    if len(numbers) > 2 and numbers != expanded:
        raise ValueError(f"gapped enumeration: {value}")
    return expanded


def heading_coverage(text: str, kind: str) -> Counter[int]:
    """Count attributed PDF pages or typed-slide numbers in Markdown headings."""
    if kind == "pdf":
        pattern = r"\((?:стр\. PDF |PDF pp?\. |pp?\. PDF )(\d+(?:[–-]\d+)?)\)"
    else:
        pattern = (
            r"^#{2,6} (?:Печатн(?:ый слайд|ые слайды)|(?:Typed|Printed) slides?|"
            r"Diapositivas? impresas?) (\d+(?:[–-]\d+)?)"
        )
    result: Counter[int] = Counter()
    for heading in re.findall(r"(?m)^#{2,6} .+$", text):
        for value in re.findall(pattern, heading):
            result.update(number_range(value))
    return result


def math_tokens(text: str) -> tuple[list[str], Counter[str]]:
    """Ordered display formulas and an order-independent inline-math multiset.

    Translated prose can legitimately reorder inline symbols. Only translated
    \\text{...} labels and whitespace are ignored, never mathematical operators.
    """
    prose = without_fenced_code(to_dollar_math(text))
    display, inline = [], []
    pattern = r"(?<!\\)\$\$(.*?)\$\$|(?<!\\)\$([^$\n]+?)(?<!\\)\$"
    for match in re.finditer(pattern, prose, re.DOTALL):
        value = match.group(1) if match.group(1) is not None else match.group(2)
        value = re.sub(r"\\text\{[^{}]*\}", r"\\text{}", value)
        value = re.sub(r"\s+", "", value)
        (display if match.group(1) is not None else inline).append(value)
    return display, Counter(inline)


def numbered_statements(text: str) -> list[tuple[str, str]]:
    kinds = {
        "Определение": "definition", "Definition": "definition", "Definición": "definition",
        "Теорема": "theorem", "Theorem": "theorem", "Teorema": "theorem",
        "Лемма": "lemma", "Lemma": "lemma", "Lema": "lemma",
        "Следствие": "corollary", "Corollary": "corollary", "Corolario": "corollary",
        "Утверждение": "proposition", "Proposition": "proposition", "Proposición": "proposition",
        "Замечание": "remark", "Remark": "remark", "Observación": "remark",
    }
    # «Определение 8.1.4а» (a letter-suffixed item) is not a separately numbered statement.
    pattern = r"\*\*(" + "|".join(kinds) + r")\s+(\d+\.\d+\.\d+)(?![\w.]*\w)"
    lookup = {kind.casefold(): value for kind, value in kinds.items()}
    return [(lookup[kind.casefold()], number)
            for kind, number in re.findall(pattern, text, re.IGNORECASE)]


def check_lecture_tree() -> list[Path]:
    """Check the complete nested chronology, not just the 21 general chapters."""
    checked = []
    names_by_language = {}
    for lang in LANGUAGES:
        directory = VAULT / lang / LECTURE_DIRECTORY
        paths = sorted(directory.glob("*.md"))
        names_by_language[lang] = {p.name for p in paths}
        index = directory / "index.md"
        if not index.is_file():
            fail(index, "missing lecture index")
        index_text = index.read_text(encoding="utf-8") if index.is_file() else ""
        coverage: Counter[int] = Counter()
        for path in paths:
            checked.append(path)
            text = path.read_text(encoding="utf-8")
            check_frontmatter(path, lang, text)
            check_fences_and_math(path, text)
            check_links(path, text)
            if path.name == "index.md":
                continue
            match = re.fullmatch(r"lecture-([\d-]+)\.md", path.name)
            if not match:
                fail(path, "unexpected lecture filename")
                continue
            try:
                numbers = number_range(match.group(1))
                if number_range(metadata(text).get("lecture", "")) != numbers:
                    fail(path, "lecture metadata does not match the filename")
            except ValueError as exc:
                fail(path, str(exc))
                continue
            coverage.update(numbers)
            if len(text) < 2500:
                fail(path, "lecture is unexpectedly short; full notes are required")
            if index_text.count(f"]({path.name})") != 1:
                fail(index, f"must link to {path.name} exactly once")
        covered = LAST_LECTURE if lang == "ru" else TRANSLATED_UP_TO
        expected = Counter(range(covered + 1))
        if coverage != expected:
            fail(directory, f"lecture coverage must be exactly 0–{covered}; "
                 f"missing={sorted((expected - coverage).elements())}, "
                 f"duplicate/extra={sorted((coverage - expected).elements())}")
        if f"0–{covered}" not in index_text:
            fail(index, f"index must state current lecture coverage: 0–{covered}")
        for semester, first, last in SEMESTERS:
            if f"{first}–{last}" not in index_text:
                fail(index, f"index must state the range of semester {semester}: {first}–{last}")
        if not re.search(r"дублир|duplic", index_text, re.IGNORECASE):
            fail(index, "index must flag the duplicated semester-2 material")
        links = {(directory / raw).resolve() for _, raw in local_links(index_text)}
        if (VAULT / "ru/lectures/index.md").resolve() not in links:
            fail(index, "index must link to the existing semester-2 folder")
    def translated(name: str) -> bool:
        match = re.fullmatch(r"lecture-([\d-]+)\.md", name)
        return not match or int(match.group(1).split("-")[0]) <= TRANSLATED_UP_TO

    reference = {n for n in names_by_language["ru"] if translated(n)}
    for lang, names in names_by_language.items():
        if {n for n in names if translated(n)} != reference or (lang != "ru" and names != reference):
            fail(VAULT / lang / LECTURE_DIRECTORY, "lecture filenames differ between languages")
    reference = names_by_language["ru"]
    registered = Counter(name for names in LECTURE_BATCHES.values() for name in names)
    registered.update(notebook_lecture_files())
    for name in sorted(reference):
        match = re.fullmatch(r"lecture-([\d-]+)\.md", name)
        try:
            later = bool(match) and number_range(match.group(1))[0] >= 31
        except ValueError:
            continue
        if later and registered[name] != 1:
            fail(VAULT / LANGUAGES[0] / LECTURE_DIRECTORY / name,
                 "lecture must belong to exactly one provenance batch")
    return checked


def check_new_lecture_batch(batch: str = "31-38") -> int:
    """Check one registered batch: provenance, page attributions and RU/EN/ES parity.

    Visual-review flags document human review; checksums and references are
    verified independently. Source PDFs are intentionally not stored in Git.
    """
    assets = VAULT / "assets" / LECTURE_DIRECTORY
    expected_lectures = LECTURE_BATCHES[batch]
    manifest = assets / f"figures-{batch}.json"
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
        sources, figures = data["sources"], data["figures"]
        if not isinstance(sources, dict) or not isinstance(figures, list):
            raise ValueError("sources must be an object and figures must be a list")
        if not all(isinstance(s, dict) for s in sources.values()) or not all(isinstance(f, dict) for f in figures):
            raise ValueError("source and figure records must be objects")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        fail(manifest, f"invalid/missing provenance manifest: {exc}")
        return 0
    source_files = [source.get("lecture_file") for source in sources.values()]
    if (not all(isinstance(name, str) for name in source_files) or
            Counter(source_files) != Counter(expected_lectures)):
        fail(manifest, f"source records must cover each lecture file in {batch} exactly once")
    figure_by_file = {}
    for figure in figures:
        name = figure.get("file", "")
        if not isinstance(name, str) or not name or Path(name).name != name or not name.endswith(".jpg"):
            fail(manifest, f"invalid JPEG filename: {name!r}")
            continue
        image = assets / name
        if name in figure_by_file:
            fail(manifest, f"duplicate figure record: {name}")
        figure_by_file[name] = figure
        source = sources.get(figure.get("source"), {})
        page, source_pages = figure.get("pdf_page"), source.get("pages")
        if type(page) is not int or type(source_pages) is not int or not 1 <= page <= source_pages:
            fail(manifest, f"invalid source/page for {name}")
        page_match = re.search(r"-p(\d+)-", name)
        if not page_match or int(page_match.group(1)) != page:
            fail(manifest, f"filename/page mismatch for {name}")
        box, size = figure.get("crop_box", []), figure.get("page_size", [])
        if (not isinstance(box, list) or not isinstance(size, list) or len(box) != 4 or len(size) != 2 or
                not all(isinstance(n, (int, float)) for n in box + size) or
                not (0 <= box[0] < box[2] <= size[0] and 0 <= box[1] < box[3] <= size[1])):
            fail(manifest, f"invalid PDF-point crop bounds for {name}")
        if any(type(figure.get(k)) is not int or figure[k] <= 0 for k in ("width", "height")):
            fail(manifest, f"invalid output dimensions for {name}")
        if figure.get("reviewed_individually") is not True:
            fail(manifest, f"individual visual review not recorded for {name}")
        if not image.is_file():
            fail(image, "missing figure")
        else:
            content = image.read_bytes()
            if not content.startswith(b"\xff\xd8\xff") or not content.endswith(b"\xff\xd9"):
                fail(image, "not a complete JPEG")
            if hashlib.sha256(content).hexdigest() != figure.get("sha256"):
                fail(image, "JPEG checksum differs from the provenance manifest")
    referenced = set()
    for source_name, source in sources.items():
        source_hash = source.get("sha256")
        if not isinstance(source_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", source_hash):
            fail(manifest, f"invalid source SHA-256 for {source_name}")
        pages, slides = source.get("pages"), source.get("typed_slides")
        if type(pages) is not int or pages <= 0 or type(slides) is not int or slides <= 0:
            fail(manifest, f"invalid page/slide count for {source_name}")
            continue
        typed, hand = source.get("typed_pdf_pages", []), source.get("handwritten_pdf_pages", [])
        inventory_valid = (isinstance(typed, list) and isinstance(hand, list) and
                           all(type(n) is int for n in typed + hand) and
                           Counter(typed + hand) == Counter(range(1, pages + 1)) and len(typed) == slides)
        if not inventory_valid:
            fail(manifest, f"typed/handwritten page inventory is incomplete for {source_name}")
        filename = source.get("lecture_file", "")
        if filename not in expected_lectures:
            continue
        try:
            expected_semester = semester_of(max(number_range(source.get("lecture", ""))))
        except (ValueError, TypeError) as exc:
            fail(manifest, f"invalid lecture metadata: {exc}")
            continue
        if source.get("semester") != expected_semester:
            fail(manifest, f"incorrect semester for {filename}")
        # The 51–54, 55–60 and 61–64 transcriptions are based only on the
        # supplied PDFs, per the user's instruction not to consult the source
        # archive. Those batches must not claim archive files; earlier batches
        # retain their established archive checks.
        if batch in ("51-54", "55-60", "61-64"):
            if "archive_file" in source:
                fail(manifest, f"source-only batch must not claim an archive filename for {filename}")
            archive_name = None
        else:
            archive_name = source.get("archive_file", f"Лекция {source['lecture']}.md")
        if archive_name is not None and (
                not isinstance(archive_name, str) or Path(archive_name).name != archive_name or
                not archive_name.endswith(".md")):
            fail(manifest, f"invalid archive filename for {filename}")
            continue
        duplicate_sections = source.get("duplicate_sections", [])
        if (not isinstance(duplicate_sections, list) or
                not all(isinstance(name, str) and Path(name).name == name and name.endswith(".md")
                        for name in duplicate_sections)):
            fail(manifest, f"invalid duplicate sections for {filename}")
            continue
        reference_text = None
        reference_images = None
        for lang in LANGUAGES:
            path = VAULT / lang / LECTURE_DIRECTORY / filename
            if not path.is_file():
                fail(path, "missing new lecture translation")
                continue
            text = path.read_text(encoding="utf-8")
            meta = metadata(text)
            expected = {"lecture": source["lecture"], "source": source_name,
                        "semester": expected_semester, "date": source.get("date", ""),
                        "pdf_pages": pages, "typed_slides": slides}
            # The 45–50 batch records exact archive filenames (including suffixes)
            # as lecture metadata; older batches predate this field.
            if batch == "45-50":
                expected["archive_file"] = archive_name
            for key, value in expected.items():
                if meta.get(key) != str(value):
                    fail(path, f"metadata {key} must be {value!r}")
            if heading_coverage(text, "pdf") != Counter(range(1, pages + 1)):
                fail(path, "PDF-page headings must cover every source page exactly once")
            if heading_coverage(text, "slides") != Counter(range(1, slides + 1)):
                fail(path, "typed-slide headings must cover every printed slide exactly once")
            printed_pdf_pages: Counter[int] = Counter()
            for heading in re.findall(r"(?m)^#{2,6} .+$", text):
                slide_count = sum(heading_coverage(heading, "slides").values())
                # Combined headings list the printed page(s) first, then the
                # handwritten follow-up, e.g. slide 8 + PDF pages 9–10.
                pdf_numbers = sorted(heading_coverage(heading, "pdf").elements())
                printed_pdf_pages.update(pdf_numbers[:slide_count])
            if inventory_valid and printed_pdf_pages != Counter(typed):
                fail(path, "printed-slide PDF-page attributions differ from the source inventory")
            links = {(path.parent / raw).resolve() for _, raw in local_links(text)}
            images = [(path.parent / raw).resolve() for is_image, raw in local_links(text) if is_image]
            for image in images:
                figure = figure_by_file.get(image.name)
                if image.parent != assets.resolve() or not figure or figure["source"] != source_name:
                    fail(path, f"unregistered or misattributed figure: {image.name}")
                else:
                    referenced.add(image.name)
            if reference_text is None:
                reference_text, reference_images = text, images
            else:
                if math_tokens(text) != math_tokens(reference_text):
                    fail(path, "translated display formulas or inline-math inventory differ")
                if numbered_statements(text) != numbered_statements(reference_text):
                    fail(path, "numbered statement order/types differ between translations")
                if images != reference_images:
                    fail(path, "figure references/order differ between translations")
            if expected_semester == 2:
                if not re.search(r"дублир|duplic", text, re.IGNORECASE) or "33–64" not in text:
                    fail(path, "semester-2 duplication notice is missing")
                required = [VAULT / "ru/lectures/index.md"]
                required += [VAULT / "ru/lectures" / name for name in duplicate_sections]
                if archive_name is not None:
                    required += [ROOT / "source/MathInMind/МАТАН_Л" / archive_name]
                for target in required:
                    if target.resolve() not in links:
                        fail(path, f"missing duplicate-material cross-reference: {target.relative_to(ROOT)}")
    if referenced != set(figure_by_file):
        fail(manifest, f"unreferenced figures: {sorted(set(figure_by_file) - referenced)}")
    return len(figures)


def notebook_manifest(batch: str) -> dict | None:
    path = VAULT / "assets" / LECTURE_DIRECTORY / f"figures-{batch}.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return data if isinstance(data, dict) else None


def notebook_lecture_files() -> list[str]:
    names: list[str] = []
    for batch in NOTEBOOK_BATCHES:
        lectures = (notebook_manifest(batch) or {}).get("lectures", {})
        if isinstance(lectures, dict):
            names.extend(lectures)
    return names


def raw_page_metadata() -> dict[str, dict[str, str]] | None:
    raw = ROOT / "ocr" / "raw"
    if not raw.is_dir():
        return None
    return {p.stem: metadata(p.read_text(encoding="utf-8")) for p in sorted(raw.glob("p*.md"))}


def check_notebook_batch(batch: str) -> int:
    """Check a batch transcribed from notebook pages and video frames (ocr/raw/pNNN.md).

    Every original page belongs to exactly one lecture and is marked there by a
    page anchor; technical duplicates are taken from the manifest and ocr/raw.
    """
    assets = VAULT / "assets" / LECTURE_DIRECTORY
    manifest = assets / f"figures-{batch}.json"
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
        sources, pages, lectures, figures = data["sources"], data["pages"], data["lectures"], data["figures"]
        if not all(isinstance(x, dict) for x in (sources, pages, lectures)) or not isinstance(figures, list):
            raise ValueError("sources, pages and lectures must be objects and figures a list")
        if not all(isinstance(v, dict) for v in [*sources.values(), *pages.values(), *lectures.values(), *figures]):
            raise ValueError("records must be objects")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        fail(manifest, f"invalid/missing provenance manifest: {exc}")
        return 0
    for name, source in sources.items():
        if source.get("kind") not in ("notebook", "video"):
            fail(manifest, f"source {name}: kind must be notebook or video")
        digest = source.get("sha256")
        if digest is not None and not (isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest)):
            fail(manifest, f"source {name}: invalid SHA-256")
    for page, record in pages.items():
        if not re.fullmatch(r"p\d{3}", page):
            fail(manifest, f"invalid page id: {page}")
        if record.get("source") not in sources:
            fail(manifest, f"page {page}: unknown source")
        if not re.fullmatch(r"[0-9a-f]{12}", str(record.get("sha256_prefix", ""))):
            fail(manifest, f"page {page}: invalid sha256_prefix")
        twin = record.get("duplicate_of")
        if twin is not None and (twin not in pages or pages[twin].get("duplicate_of") is not None):
            fail(manifest, f"page {page}: duplicate_of must name an original page")
    raw = raw_page_metadata()
    if raw is not None:
        if set(raw) != set(pages):
            fail(manifest, f"pages differ from ocr/raw: missing={sorted(set(raw) - set(pages))}, "
                 f"extra={sorted(set(pages) - set(raw))}")
        for page, meta in raw.items():
            record = pages.get(page)
            if record is None:
                continue
            if meta.get("original") != record.get("original"):
                fail(manifest, f"page {page}: original name differs from ocr/raw")
            if meta.get("duplicate_of") != record.get("duplicate_of"):
                fail(manifest, f"page {page}: duplicate_of differs from ocr/raw")
    originals = Counter(p for p, r in pages.items() if r.get("duplicate_of") is None)
    cited = Counter(p for record in lectures.values() for p in record.get("pages", []))
    if cited != originals:
        fail(manifest, "every original page must belong to exactly one lecture; "
             f"missing={sorted((originals - cited).elements())}, extra={sorted((cited - originals).elements())}")
    figure_by_file = {}
    for figure in figures:
        name = str(figure.get("file", ""))
        match = re.fullmatch(r"lec(\d+(?:-\d+)*)-(p\d{3})-[a-z0-9-]+\.jpg", name)
        lecture_file = figure.get("lecture_file")
        if (not match or lecture_file not in lectures or f"lecture-{match.group(1)}.md" != lecture_file
                or match.group(2) != figure.get("page")
                or figure.get("page") not in lectures[lecture_file].get("pages", [])):
            fail(manifest, f"figure {name!r}: file name, page and lecture must agree")
            continue
        if name in figure_by_file:
            fail(manifest, f"duplicate figure record: {name}")
        figure_by_file[name] = figure
        if any(type(figure.get(k)) is not int or figure[k] <= 0 for k in ("width", "height")):
            fail(manifest, f"invalid output dimensions for {name}")
        if figure.get("reviewed_individually") is not True:
            fail(manifest, f"individual visual review not recorded for {name}")
        image = assets / name
        if not image.is_file():
            fail(image, "missing figure")
            continue
        content = image.read_bytes()
        if not content.startswith(b"\xff\xd8\xff") or not content.endswith(b"\xff\xd9"):
            fail(image, "not a complete JPEG")
        digest = hashlib.sha256(content).hexdigest()
        if digest != figure.get("sha256"):
            fail(image, "JPEG checksum differs from the provenance manifest")
        origin = ROOT / str(figure.get("origin", ""))
        if not figure.get("origin") or not origin.is_file():
            # Scans p022+ are not kept in Git; a crop of them must record its box.
            if figure.get("crop_box") is None:
                fail(manifest, f"origin of {name} is missing")
        elif figure.get("crop_box") is None and hashlib.sha256(origin.read_bytes()).hexdigest() != digest:
            fail(manifest, f"{name} is not a byte copy of its origin")
    referenced = set()
    labels = ("translated display formulas or inline-math inventory differ",
              "numbered statement order/types differ between translations",
              "figure references/order differ between translations",
              "page anchors differ between translations",
              "open-issue markers differ between translations")
    for filename, record in lectures.items():
        try:
            numbers = number_range(str(record.get("lecture", "")))
        except ValueError as exc:
            fail(manifest, f"{filename}: {exc}")
            continue
        if filename != f"lecture-{record['lecture']}.md":
            fail(manifest, f"{filename}: lecture number does not match the file name")
        own_pages = list(record.get("pages", []))
        expected = {"lecture": record["lecture"], "semester": str(semester_of(max(numbers))),
                    "source_pages": ", ".join(own_pages)}
        if record.get("date"):
            expected["date"] = record["date"]
        if record.get("course_chapter") is not None:
            expected["course_chapter"] = str(record["course_chapter"])
        reference = None
        pending = min(numbers) > TRANSLATED_UP_TO
        for lang in (("ru",) if pending else LANGUAGES):
            path = VAULT / lang / LECTURE_DIRECTORY / filename
            if not path.is_file():
                fail(path, "missing lecture translation")
                continue
            text = path.read_text(encoding="utf-8")
            meta = metadata(text)
            for key, value in expected.items():
                if meta.get(key) != value:
                    fail(path, f"metadata {key} must be {value!r}")
            anchors = PAGE_ANCHOR_LINE.findall(text)
            if PAGE_ANCHOR_ANY.findall(text) != anchors:
                fail(path, "page anchors must stand alone on their own line")
            if anchors != own_pages:
                fail(path, "page anchors must list the lecture's pages exactly once, in order")
            if re.search(r"(?m)^\s*>\s*\[!", text):
                fail(path, "Obsidian callouts are not allowed in the GitHub view")
            images = [(path.parent / raw).resolve() for is_image, raw in local_links(text) if is_image]
            for image in images:
                figure = figure_by_file.get(image.name)
                if image.parent != assets.resolve() or not figure or figure.get("lecture_file") != filename:
                    fail(path, f"unregistered or misattributed figure: {image.name}")
                else:
                    referenced.add(image.name)
            current = (math_tokens(text), numbered_statements(text), [i.name for i in images], anchors,
                       ocr_issues.ANY_MARKER_RE.findall(text))
            if reference is None:
                reference = current
                continue
            for got, want, message in zip(current, reference, labels):
                if got != want:
                    fail(path, message)
    if referenced != set(figure_by_file):
        fail(manifest, f"unreferenced figures: {sorted(set(figure_by_file) - referenced)}")
    return len(figure_by_file)


SECTION_HEADING = re.compile(r"(?m)^## §(\d+)\.(\d+)\b")
CLASSIC_SECTION_HEADING = re.compile(r"(?m)^## \d+\.\d+\s")
CORE_KINDS = {"definition", "theorem", "lemma", "corollary"}


def lecture_statement_inventory(lang: str) -> set[tuple[str, str]]:
    result: set[tuple[str, str]] = set()
    for path in (VAULT / lang / LECTURE_DIRECTORY).glob("lecture-*.md"):
        result.update(numbered_statements(path.read_text(encoding="utf-8")))
    return result


def check_lecture_chapters() -> None:
    """Chapters 22+ follow the lecturer's chapters: §-headings and the lectures' statement numbers."""
    for chapter in LECTURE_CHAPTERS:
        reference = None
        k = chapter.lecturer_chapter
        first, last = chapter.sections
        for lang in LANGUAGES:
            path = VAULT / lang / chapter.filename
            if not path.is_file():
                continue  # reported as a missing file
            text = path.read_text(encoding="utf-8")
            meta = metadata(text)
            for key, value in (("numbering", "lecture"), ("lecturer_chapter", str(k))):
                if meta.get(key) != value:
                    fail(path, f"metadata {key} must be {value!r}")
            sections = [(int(a), int(b)) for a, b in SECTION_HEADING.findall(text)]
            if sections != [(k, s) for s in range(first, last + 1)]:
                fail(path, f"expected headings ## §{k}.{first} … ## §{k}.{last}, once each and in order; "
                     f"found {sections}")
            if CLASSIC_SECTION_HEADING.search(text):
                fail(path, "lecture-numbered chapters use ## §K.s headings, not ## N.M")
            statements = numbered_statements(text)
            counts = Counter(statements)
            for item, n in counts.items():
                if n > 1:
                    fail(path, f"statement {item} is labelled {n} times")
            for kind, number in statements:
                c, s, _ = (int(x) for x in number.split("."))
                if c != k or not first <= s <= last:
                    fail(path, f"{kind} {number} lies outside §{k}.{first}–§{k}.{last}")
            lectures = lecture_statement_inventory(lang)
            missing = sorted((kind, n) for kind, n in lectures
                             if kind in CORE_KINDS and int(n.split(".")[0]) == k
                             and first <= int(n.split(".")[1]) <= last and (kind, n) not in counts)
            if missing:
                fail(path, f"statements of the lectures missing from the chapter: {missing}")
            unknown = sorted(set(statements) - lectures)
            if unknown:
                fail(path, f"statements not found in the lectures: {unknown}")
            current = (sections, statements, math_tokens(text))
            if reference is None:
                reference = current
            elif current != reference:
                fail(path, "sections, statements or formulas differ from the other languages")


def check_ocr_markers() -> list[Path]:
    """Open transcription issues may stay visible only in the lectures, for a manual fix."""
    open_rows = ocr_issues.open_ids(ROOT)
    for path in sorted(VAULT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if "⟦" not in text:
            continue
        lecture = path.parent.name == LECTURE_DIRECTORY and path.name.startswith("lecture-")
        scan = text if lecture else without_inline_code(without_fenced_code(text))
        for number, line in enumerate(scan.split("\n"), 1):
            for match in ocr_issues.ANY_MARKER_RE.finditer(line):
                marker = match.group(0)
                if not lecture:
                    fail(path, f"line {number}: issue marker {marker} outside the lecture notes")
                    continue
                ident = ocr_issues.MARKER_RE.fullmatch(marker)
                if not ident:
                    fail(path, f"line {number}: malformed issue marker {marker}")
                elif ident.group(1) not in open_rows:
                    fail(path, f"line {number}: {marker} is not an open row of ocr/ISSUES.md")
                elif any(a <= match.start() < b for a, b, kind in inline_spans(line) if kind != "code"):
                    fail(path, f"line {number}: issue marker inside a formula")
    others = [ROOT / "ISSUES.md", ROOT / "ocr" / "ISSUES.md", ROOT / "ocr" / "RESOLVED.md",
              ROOT / "ocr" / "MANIFEST.md", ROOT / "ocr" / "SPLIT_PROPOSAL.md"]
    return [path for path in others if path.is_file()]


def main() -> int:
    errors.clear()
    checked_paths: list[Path] = []
    if not VAULT.is_dir():
        print(f"Missing vault: {VAULT}", file=sys.stderr)
        return 2

    for lang in LANGUAGES:
        directory = VAULT / lang
        actual = {path.name for path in directory.glob("*.md")}
        missing = EXPECTED - actual
        extra = actual - EXPECTED
        if missing:
            fail(directory, f"missing files: {', '.join(sorted(missing))}")
        if extra:
            fail(directory, f"unexpected Markdown files: {', '.join(sorted(extra))}")
        for path in sorted(directory.glob("*.md")):
            checked_paths.append(path)
            text = path.read_text(encoding="utf-8")
            check_frontmatter(path, lang, text)
            check_fences_and_math(path, text)
            check_links(path, text)
            if path.name in CHAPTERS and len(text) < 2500:
                fail(path, "core chapter is unexpectedly short")
        index = directory / "index.md"
        if index.exists():
            index_text = index.read_text(encoding="utf-8")
            for chapter in CHAPTERS:
                if f"]({chapter})" not in index_text:
                    fail(index, f"index does not link to {chapter}")

    checked_paths.extend(check_lecture_tree())
    figure_count = sum(check_new_lecture_batch(batch) for batch in LECTURE_BATCHES)
    figure_count += sum(check_notebook_batch(batch) for batch in NOTEBOOK_BATCHES)
    check_lecture_chapters()
    for path in check_ocr_markers():
        checked_paths.append(path)
        check_links(path, path.read_text(encoding="utf-8"))
    # Check entry points and the provenance guide for every registered batch.
    guides = [VAULT / "assets" / LECTURE_DIRECTORY / f"provenance-{batch}.md"
              for batch in (*LECTURE_BATCHES, *NOTEBOOK_BATCHES)]
    for path in (ROOT / "README.md", VAULT / "README.md", VAULT / "ru/lectures/index.md", *guides):
        if path.is_file():
            checked_paths.append(path)
            text = path.read_text(encoding="utf-8")
            check_fences_and_math(path, text)
            check_links(path, text)
        else:
            fail(path, "missing entry point or provenance guide")

    for filename in CHAPTERS:
        texts = [p.read_text(encoding="utf-8") if p.is_file() else ""
                 for lang in LANGUAGES for p in [VAULT / lang / filename]]
        exercise_counts = [len(re.findall(r"(?m)^## (?:Exercises|Упражнения|Ejercicios)\s*$", text)) for text in texts]
        if any(count != 1 for count in exercise_counts):
            fail(filename, f"expected one exercise section per language, got {exercise_counts}")

    chapter_words = {}
    for lang in LANGUAGES:
        chapter_words[lang] = sum(
            len(p.read_text(encoding="utf-8").split())
            for name in CHAPTERS for p in [VAULT / lang / name] if p.is_file()
        )

    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    mermaid_count = sum(p.read_text(encoding="utf-8").count("```mermaid") for p in checked_paths)
    print("Course validation passed.")
    print(f"  Languages: {', '.join(LANGUAGES)}")
    print(f"  Core chapters: {len(CHAPTERS)} per language")
    print(f"  2025/26 lecture coverage: 0–{LAST_LECTURE} in Russian, 0–{TRANSLATED_UP_TO} in all languages")
    print("  Semesters: " + " / ".join(f"{first}–{last}" for _, first, last in SEMESTERS)
          + "; duplicated semester-2 cross-references checked")
    print(f"  Illustrated batches: {', '.join(LECTURE_BATCHES)}; PDF/slide headings, metadata and translation parity checked")
    if NOTEBOOK_BATCHES:
        print(f"  Notebook batches: {', '.join(NOTEBOOK_BATCHES)}; page anchors, open-issue markers and parity checked")
    if LECTURE_CHAPTERS:
        print(f"  Lecture-numbered chapters: {', '.join(str(c.number) for c in LECTURE_CHAPTERS)}")
    print(f"  Shared JPEG crops with provenance and matching checksums: {figure_count}")
    print(f"  Markdown files checked: {len(checked_paths)}")
    print(f"  Mermaid diagrams checked: {mermaid_count}")
    print("  Core word counts (whitespace estimate): " + ", ".join(f"{k}={v}" for k, v in chapter_words.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
