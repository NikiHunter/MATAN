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

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "MathInMind"
LANGUAGES = ("en", "ru", "es")
CHAPTERS = (
    "01-logic-sets-functions.md",
    "02-real-numbers.md",
    "03-sequences.md",
    "04-numeric-series.md",
    "05-limits-continuity.md",
    "06-derivatives.md",
    "07-taylor-convexity.md",
    "08-riemann-integration.md",
    "09-improper-integrals-applications.md",
    "10-function-sequences-series.md",
    "11-power-series.md",
    "12-fourier-series.md",
    "13-metric-spaces.md",
    "14-several-variables.md",
    "15-multivariable-differentiation.md",
    "16-implicit-functions-extrema.md",
    "17-multiple-integrals.md",
    "18-vector-calculus.md",
    "19-measure-theory.md",
    "20-lebesgue-integration.md",
    "21-lp-spaces.md",
)
SUPPORTING = ("index.md", "00-notation.md", "formula-sheet.md", "glossary.md")
EXPECTED = set(CHAPTERS + SUPPORTING)
LECTURE_DIRECTORY = "lectures-2025-26"
LAST_LECTURE = 64
SEMESTER_ONE_LAST = 32
LECTURE_BATCHES = {
    "31-38": tuple(f"lecture-{n}.md" for n in ("31-32", "33-34", "35", "36", "37-38")),
    "39-44": tuple(f"lecture-{n}.md" for n in ("39-40", "41-42", "43-44")),
    "45-50": tuple(f"lecture-{n}.md" for n in ("45-46", "47-48", "49-50")),
    "51-54": tuple(f"lecture-{n}.md" for n in ("51-52", "53", "54")),
    "55-60": tuple(f"lecture-{n}.md" for n in ("55-56", "57-58", "59-60")),
    "61-64": tuple(f"lecture-{n}.md" for n in ("61-62", "63-64")),
}
NEW_LECTURES = tuple(name for filenames in LECTURE_BATCHES.values() for name in filenames)
# One level of brackets in a label is needed for interval notation in image alt text.
LINK_RE = re.compile(r"(!?)\[(?:[^\[\]\n]|\[[^\[\]\n]*\])*\]\(([^)\n]+)\)")

errors: list[str] = []


def fail(path: Path | str, message: str) -> None:
    label = str(path.relative_to(ROOT)) if isinstance(path, Path) else path
    errors.append(f"{label}: {message}")


def without_fenced_code(text: str) -> str:
    return re.sub(r"^```.*?^```\s*$", "", text, flags=re.MULTILINE | re.DOTALL)


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
    if re.search(r"\[\[[^\n]*?\]\]", prose):
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
    prose = without_fenced_code(text)
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
    }
    pattern = r"\*\*(" + "|".join(kinds) + r")\s+(\d+\.\d+\.\d+)"
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
        expected = Counter(range(LAST_LECTURE + 1))
        if coverage != expected:
            fail(directory, f"lecture coverage must be exactly 0–{LAST_LECTURE}; "
                 f"missing={sorted((expected - coverage).elements())}, "
                 f"duplicate/extra={sorted((coverage - expected).elements())}")
        if f"0–{LAST_LECTURE}" not in index_text:
            fail(index, f"index must state current lecture coverage: 0–{LAST_LECTURE}")
        if "0–32" not in index_text or "33–64" not in index_text:
            fail(index, "index must state both semester ranges: 0–32 and 33–64")
        if not re.search(r"дублир|duplic", index_text, re.IGNORECASE):
            fail(index, "index must flag the duplicated semester-2 material")
        links = {(directory / raw).resolve() for _, raw in local_links(index_text)}
        if (VAULT / "ru/lectures/index.md").resolve() not in links:
            fail(index, "index must link to the existing semester-2 folder")
    reference = names_by_language[LANGUAGES[0]]
    for lang, names in names_by_language.items():
        if names != reference:
            fail(VAULT / lang / LECTURE_DIRECTORY, "lecture filenames differ between languages")
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
            expected_semester = 1 if max(number_range(source.get("lecture", ""))) <= SEMESTER_ONE_LAST else 2
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
    # Check entry points and the provenance guide for every registered batch.
    guides = [VAULT / "assets" / LECTURE_DIRECTORY / f"provenance-{batch}.md" for batch in LECTURE_BATCHES]
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
    print(f"  2025/26 lecture coverage: 0–{LAST_LECTURE} in all languages")
    print(f"  Semesters: 0–32 / 33–64; duplicated 33–{LAST_LECTURE} cross-references checked")
    print(f"  Illustrated batches: {', '.join(LECTURE_BATCHES)}; PDF/slide headings, metadata and translation parity checked")
    print(f"  Shared JPEG crops with provenance and matching checksums: {figure_count}")
    print(f"  Markdown files checked: {len(checked_paths)}")
    print(f"  Mermaid diagrams checked: {mermaid_count}")
    print("  Core word counts (whitespace estimate): " + ", ".join(f"{k}={v}" for k, v in chapter_words.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
