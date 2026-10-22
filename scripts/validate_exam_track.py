#!/usr/bin/env python3
"""Validate the lecture-aligned Russian exam track without external dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
RU = ROOT / "MathInMind" / "ru"
LECTURES = RU / "lectures"
TICKETS = RU / "exam" / "tickets"
PURGATORY = RU / "purgatory"
SOURCE_LECTURES = ROOT / "source" / "MathInMind" / "МАТАН_Л"

SECTIONS = (
    "01-convexity-3-8.md",
    "02-antiderivatives-4-1.md",
    "03-riemann-integral-4-2.md",
    "04-riemann-properties-4-3.md",
    "05-taylor-wallis-inequalities-4-4.md",
    "06-improper-integrals-4-5.md",
    "07-measure-paths-4-6.md",
    "08-integral-applications-4-7.md",
    "09-rn-foundations-5-1.md",
    "10-vector-sequences-5-2.md",
    "11-topology-rn-5-3.md",
    "12-mapping-limits-5-4.md",
    "13-continuity-rn-5-5.md",
    "14-differentiability-6-1.md",
    "15-differentiation-rules-6-2.md",
    "16-continuous-differentiability-6-3.md",
    "17-higher-derivatives-6-4.md",
)

errors: list[str] = []


def fail(path: Path | str, message: str) -> None:
    label = str(path.relative_to(ROOT)) if isinstance(path, Path) else path
    errors.append(f"{label}: {message}")


def read(path: Path) -> str:
    if not path.is_file():
        fail(path, "required file is missing")
        return ""
    return path.read_text(encoding="utf-8")


def check_frontmatter(path: Path, text: str) -> None:
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        fail(path, "missing or unterminated YAML frontmatter")
        return
    end = text.find("\n---\n", 4)
    frontmatter = text[4:end]
    if not re.search(r"(?m)^lang:\s*ru\s*$", frontmatter):
        fail(path, "frontmatter must contain lang: ru")


def check_text_basics(path: Path, text: str) -> None:
    bad = [(i, ord(ch)) for i, ch in enumerate(text) if ord(ch) < 32 and ch not in "\n\t"]
    # Actual tab characters are also forbidden in generated mathematical prose;
    # they usually indicate a Python '\t' escape accident.
    bad.extend((i, 9) for i, ch in enumerate(text) if ch == "\t")
    if bad:
        fail(path, f"control characters detected: {bad[:5]}")
    if "\ufffd" in text:
        fail(path, "Unicode replacement character detected")
    for marker in ("TODO", "TBD", "PLACEHOLDER", "lorem ipsum"):
        if marker.lower() in text.lower():
            fail(path, f"unfinished marker: {marker}")
    if text.count("```") % 2:
        fail(path, "unbalanced fenced code blocks")
    if text.count("$$") % 2:
        fail(path, "unbalanced display-math delimiters")
    dollars = len(re.findall(r"(?<!\\)\$", text))
    if dollars % 2:
        fail(path, "possibly unbalanced inline-math delimiters")
    if text.count("<details>") != text.count("</details>"):
        fail(path, "unbalanced details blocks")


def check_links(path: Path, text: str) -> None:
    prose = re.sub(r"^```.*?^```\s*$", "", text, flags=re.MULTILINE | re.DOTALL)
    for match in re.finditer(r"!?\[[^\]]*\]\(([^)]+)\)", prose):
        raw = match.group(1).strip()
        if raw.startswith("<") and ">" in raw:
            raw = raw[1 : raw.index(">")]
        else:
            raw = raw.split(maxsplit=1)[0]
        raw = unquote(raw)
        if not raw or raw.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target_part = raw.split("#", 1)[0].split("?", 1)[0]
        if not target_part:
            continue
        target = Path(target_part)
        if target.is_absolute():
            fail(path, f"absolute link: {raw}")
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            fail(path, f"link escapes repository: {raw}")
            continue
        if not resolved.exists():
            fail(path, f"broken local link or image: {raw}")
            continue
        if "#" in raw and resolved.suffix == ".md":
            fragment = raw.split("#", 1)[1]
            if fragment.startswith(("def-", "thm-", "lem-", "cor-")):
                target_text = resolved.read_text(encoding="utf-8")
                if f'<a id="{fragment}"></a>' not in target_text:
                    fail(path, f"missing explicit anchor {fragment} in {resolved.relative_to(ROOT)}")


def validate_lecture_register() -> None:
    pattern = re.compile(r"(?i)(Определение|Теорема|Лемма|Следствие)\s+(\d+\.\d+\.\d+)")
    source_items: set[tuple[str, str]] = set()
    for path in SOURCE_LECTURES.glob("*.md"):
        for match in pattern.finditer(path.read_text(encoding="utf-8")):
            source_items.add((match.group(1).capitalize(), match.group(2)))
    curated_items: set[tuple[str, str]] = set()
    heading_pattern = re.compile(r"(?m)^##\s+(Определение|Теорема|Лемма|Следствие)\s+(\d+\.\d+\.\d+)\b")
    anchor_count = 0
    for filename in SECTIONS:
        text = read(LECTURES / filename)
        for match in heading_pattern.finditer(text):
            curated_items.add((match.group(1), match.group(2)))
        anchors = re.findall(r'(?m)^<a id="((?:def|thm|lem|cor)-[^"]+)"></a>$', text)
        if len(anchors) != len(set(anchors)):
            fail(LECTURES / filename, "duplicate explicit anchors")
        anchor_count += len(anchors)
    if anchor_count != 149:
        fail(LECTURES, f"expected 149 explicit anchors, found {anchor_count}")
    missing = sorted(source_items - curated_items)
    if missing:
        fail(LECTURES, f"numbered lecture items missing: {missing}")
    if len(source_items) != 148:
        fail(SOURCE_LECTURES, f"expected 148 source items, found {len(source_items)}")
    if ("Теорема", "6.4.1") not in curated_items:
        fail(LECTURES / "17-higher-derivatives-6-4.md", "reconstructed theorem 6.4.1 is missing")
    print(f"Lecture register: {len(source_items)} source items covered; {len(curated_items)} including reconstruction")


def validate_tickets() -> None:
    expected = {f"{n:02d}.md" for n in range(1, 73)}
    actual = {p.name for p in TICKETS.glob("*.md")}
    if actual != expected:
        fail(TICKETS, f"ticket set mismatch; missing={sorted(expected-actual)}, extra={sorted(actual-expected)}")
    for n in range(1, 73):
        path = TICKETS / f"{n:02d}.md"
        text = read(path)
        if not re.search(rf"(?m)^ticket:\s*{n}\s*$", text):
            fail(path, f"frontmatter must contain ticket: {n}")
        for heading in ("## Вопрос", "## Эталонный ответ", "## Разобранный пример", "## Проверка готовности"):
            if heading not in text:
                fail(path, f"missing section: {heading}")
        if len(text) < 1200:
            fail(path, "ticket answer is unexpectedly short")
    print(f"Exam tickets: {len(actual)} individual notes")


def validate_purgatory() -> None:
    definitions = read(PURGATORY / "definitions.md")
    headings = [int(x) for x in re.findall(r"(?m)^##\s+(\d{2})\.", definitions)]
    if headings != list(range(54)):
        fail(PURGATORY / "definitions.md", f"expected headings 00..53, got {headings}")
    expected_assets = {f"{n:02d}.png" for n in range(54) if n != 15}
    actual_assets = {p.name for p in (PURGATORY / "assets").glob("*.png")}
    if actual_assets != expected_assets:
        fail(PURGATORY / "assets", f"scan set mismatch: missing={sorted(expected_assets-actual_assets)}, extra={sorted(actual_assets-expected_assets)}")
    if "исходного скана 15" not in definitions:
        fail(PURGATORY / "definitions.md", "missing-scan note for item 15 not found")

    questions = read(PURGATORY / "questions.md")
    rows = re.findall(r"(?m)^(\d+)\.\s+(.+)$", questions)
    numbers = [int(n) for n, _ in rows]
    if numbers != list(range(1, 301)):
        fail(PURGATORY / "questions.md", f"expected sequential questions 1..300; found {len(numbers)} rows")
    # Keep case: $O$ and $o$ are deliberately different Landau symbols.
    prompts = [re.sub(r"\s+", " ", prompt.strip()) for _, prompt in rows]
    if len(set(prompts)) != len(prompts):
        fail(PURGATORY / "questions.md", "duplicate question themes detected")
    print(f"Purgatory: {len(headings)} definitions, {len(actual_assets)} scans, {len(numbers)} question themes")


def main() -> int:
    required = [LECTURES / "index.md", LECTURES / "terms.md", RU / "exam" / "index.md", PURGATORY / "definitions.md", PURGATORY / "questions.md"]
    required.extend(LECTURES / name for name in SECTIONS)
    required.extend(TICKETS / f"{n:02d}.md" for n in range(1, 73))
    for path in required:
        text = read(path)
        check_frontmatter(path, text)
        check_text_basics(path, text)
        check_links(path, text)
    validate_lecture_register()
    validate_tickets()
    validate_purgatory()
    if errors:
        print(f"Exam-track validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print("Exam-track validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
