#!/usr/bin/env python3
"""Dependency-free structural checks for the trilingual MathInMind vault."""

from __future__ import annotations

import re
import sys
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
    if "[[" in prose or "]]" in prose:
        fail(path, "wiki-style links are not portable to GitHub; use relative Markdown links")


def check_links(path: Path, text: str) -> None:
    prose = without_fenced_code(text)
    # Course links have no nested parentheses in their destinations.
    pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for match in pattern.finditer(prose):
        raw = match.group(1).strip()
        if raw.startswith("<") and ">" in raw:
            raw = raw[1 : raw.index(">")]
        else:
            raw = raw.split(maxsplit=1)[0]
        raw = unquote(raw)
        if not raw or raw.startswith(("#", "http://", "https://", "mailto:", "obsidian:")):
            continue
        target_part = raw.split("#", 1)[0].split("?", 1)[0]
        if not target_part:
            continue
        target = Path(target_part)
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


def main() -> int:
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

    for filename in CHAPTERS:
        texts = [(VAULT / lang / filename).read_text(encoding="utf-8") for lang in LANGUAGES]
        exercise_counts = [len(re.findall(r"(?m)^## (?:Exercises|Упражнения|Ejercicios)\s*$", text)) for text in texts]
        if any(count != 1 for count in exercise_counts):
            fail(filename, f"expected one exercise section per language, got {exercise_counts}")

    chapter_words = {}
    for lang in LANGUAGES:
        chapter_words[lang] = sum(
            len((VAULT / lang / name).read_text(encoding="utf-8").split()) for name in CHAPTERS
        )

    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    total_files = len(LANGUAGES) * len(EXPECTED)
    mermaid_count = sum(
        (VAULT / lang / name).read_text(encoding="utf-8").count("```mermaid")
        for lang in LANGUAGES
        for name in EXPECTED
    )
    print("Course validation passed.")
    print(f"  Languages: {', '.join(LANGUAGES)}")
    print(f"  Core chapters: {len(CHAPTERS)} per language")
    print(f"  Markdown files checked: {total_files}")
    print(f"  Mermaid diagrams checked: {mermaid_count}")
    print("  Core word counts (whitespace estimate): " + ", ".join(f"{k}={v}" for k, v in chapter_words.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
