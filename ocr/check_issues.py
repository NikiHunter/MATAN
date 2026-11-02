#!/usr/bin/env python3
"""Проверка пометок ⟦ID⟧: транскрипция ocr/raw/ ↔ ocr/ISSUES.md (открытые) ↔ ocr/RESOLVED.md (решённые).

Запуск:  python3 ocr/check_issues.py [--fix-locations]
Код возврата 0 — соответствие полное, 1 — есть расхождения.

* каждая пометка ⟦ID⟧ в ocr/raw/ встречается один раз и имеет ровно одну строку —
  либо в ISSUES.md (status open), либо в RESOLVED.md;
* буква ID совпадает со столбцом Type, страница — со столбцом Page;
* у решённой пометки заполнены Decision и Basis, а Target ведёт на существующий якорь
  конспекта; в конспектах MathInMind/ решённых пометок нет;
* открытая пометка видна в конспектах (во всех трёх языках) ровно там, где указано
  в столбце Target; ``--fix-locations`` переписывает Target по фактическим строкам.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import ocr_issues  # noqa: E402

RAW = ROOT / "ocr" / "raw"
ISSUES = ROOT / "ocr" / "ISSUES.md"
RESOLVED = ROOT / "ocr" / "RESOLVED.md"
LECTURES = ("MathInMind/ru/lectures-2025-26", "MathInMind/en/lectures-2025-26", "MathInMind/es/lectures-2025-26")


def lecture_occurrences() -> dict[str, list[str]]:
    """ID -> ["MathInMind/ru/lectures-2025-26/lecture-77-78.md:123", ...]."""
    found: dict[str, list[str]] = defaultdict(list)
    for folder in LECTURES:
        for path in sorted((ROOT / folder).glob("lecture-*.md")):
            for number, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
                for ident in ocr_issues.MARKER_RE.findall(line):
                    found[ident].append(f"{folder}/{path.name}:{number}")
    return found


def fix_locations(occurrences: dict[str, list[str]]) -> int:
    lines = ISSUES.read_text(encoding="utf-8").split("\n")
    header = ocr_issues.format_row(ocr_issues.ISSUES_HEADER)
    changed = 0
    if header not in lines:
        return 0
    for k in range(lines.index(header) + 2, len(lines)):
        if not lines[k].startswith("|"):
            break
        cells = ocr_issues.split_row(lines[k])
        if len(cells) != len(ocr_issues.ISSUES_HEADER):
            continue
        target = "; ".join(occurrences.get(cells[0], []))
        if cells[-1] != target:
            cells[-1] = target
            lines[k] = ocr_issues.format_row(cells)
            changed += 1
    ISSUES.write_text("\n".join(lines), encoding="utf-8")
    return changed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="check ⟦ID⟧ markers against the issue tables")
    parser.add_argument("--fix-locations", action="store_true",
                        help="rewrite the Target column of open issues from the lecture files")
    args = parser.parse_args(argv)
    problems: list[str] = []

    pages = sorted(RAW.glob("p*.md"))
    page_of: dict[str, str] = {}
    counts: Counter[str] = Counter()
    for page in pages:
        text = page.read_text(encoding="utf-8")
        for marker in ocr_issues.ANY_MARKER_RE.findall(text):
            if not ocr_issues.MARKER_RE.fullmatch(marker):
                problems.append(f"{page.name}: malformed marker {marker}")
        for ident in ocr_issues.MARKER_RE.findall(text):
            counts[ident] += 1
            page_of[ident] = page.stem
    problems += [f"⟦{i}⟧ occurs {n} times in ocr/raw" for i, n in counts.items() if n > 1]

    open_rows, open_problems = ocr_issues.read_table(ISSUES, ocr_issues.ISSUES_HEADER)
    done_rows, done_problems = ocr_issues.read_table(RESOLVED, ocr_issues.RESOLVED_HEADER)
    problems += open_problems + done_problems
    ids = [row["ID"] for row in open_rows] + [row["ID"] for row in done_rows]
    problems += [f"{i}: more than one row" for i, n in Counter(ids).items() if n > 1]
    markers, rows = set(counts), set(ids)
    if markers - rows:
        problems.append(f"markers without a row: {sorted(markers - rows)}")
    if rows - markers:
        problems.append(f"rows without a marker in ocr/raw: {sorted(rows - markers)}")
    numbers = sorted(int(i[1:]) for i in rows)
    if numbers and numbers != list(range(1, numbers[-1] + 1)):
        gaps = sorted(set(range(1, numbers[-1] + 1)) - set(numbers))
        problems.append(f"ID numbers must be contiguous; missing {gaps[:10]}")

    occurrences = lecture_occurrences()
    if args.fix_locations:
        print(f"Target updated in {fix_locations(occurrences)} open row(s)")
        open_rows, _ = ocr_issues.read_table(ISSUES, ocr_issues.ISSUES_HEADER)

    for row in open_rows + done_rows:
        ident = row["ID"]
        if not ocr_issues.ID_RE.fullmatch(ident):
            problems.append(f"{ident}: invalid ID")
            continue
        if row["Type"] != ident[0]:
            problems.append(f"{ident}: Type {row['Type']!r} differs from the ID letter")
        if ident in page_of and row["Page"] != page_of[ident]:
            problems.append(f"{ident}: Page {row['Page']} but the marker is on {page_of[ident]}")
        if f"⟦{ident}⟧" not in row["As transcribed"]:
            problems.append(f"{ident}: 'As transcribed' must quote the marker")
    for row in open_rows:
        ident = row["ID"]
        if row["Status"] != "open":
            problems.append(f"{ident}: ISSUES.md holds open rows only (found status {row['Status']!r})")
        listed = [t.strip() for t in row["Target"].split(";") if t.strip()]
        if listed != occurrences.get(ident, []):
            problems.append(f"{ident}: Target {listed} differs from the lecture lines {occurrences.get(ident, [])}"
                            " (run with --fix-locations)")
    for row in done_rows:
        ident = row["ID"]
        if not row["Decision"] or not row["Basis"]:
            problems.append(f"{ident}: resolved rows need Decision and Basis")
        if ident in occurrences:
            problems.append(f"{ident}: resolved, but still marked in {occurrences[ident]}")
        path, _, anchor = row["Target"].partition("#")
        target = ROOT / path
        if not path or not target.is_file():
            problems.append(f"{ident}: Target {row['Target']!r} is not a file")
        elif anchor and f'<a id="{anchor}"></a>' not in target.read_text(encoding="utf-8"):
            problems.append(f"{ident}: anchor #{anchor} is missing in {path}")

    print(f"pages: {len(pages)}; markers: {len(markers)}; open: {len(open_rows)}; resolved: {len(done_rows)}")
    for problem in problems:
        print("  -", problem)
    print("ИТОГ:", "соответствие полное" if not problems else f"ЕСТЬ РАСХОЖДЕНИЯ ({len(problems)})")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
