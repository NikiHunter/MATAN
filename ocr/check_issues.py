#!/usr/bin/env python3
"""Проверка взаимного соответствия пометок ⟦ID⟧ в ocr/raw/ и строк в ocr/ISSUES.md.

Запуск:  python3 ocr/check_issues.py
Код возврата 0 — соответствие полное, 1 — есть расхождения.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "ocr" / "raw"
ISSUES = ROOT / "ocr" / "ISSUES.md"

MARKER = re.compile(r"⟦([UATMSG]\d{3})⟧")
ROW_ID = re.compile(r"^\|\s*([UATMSG]\d{3})\s*\|", re.MULTILINE)


def main() -> int:
    pages = sorted(RAW.glob("p*.md"))
    if not pages:
        print("нет файлов ocr/raw/pNNN.md")
        return 1

    by_page: dict[str, list[str]] = {}
    counts: Counter[str] = Counter()
    for page in pages:
        found = MARKER.findall(page.read_text(encoding="utf-8"))
        by_page[page.stem] = found
        counts.update(found)

    duplicated = [mid for mid, n in counts.items() if n > 1]
    markers = set(counts)
    rows = ROW_ID.findall(ISSUES.read_text(encoding="utf-8"))
    rows_set = set(rows)
    duplicated_rows = [mid for mid, n in Counter(rows).items() if n > 1]

    missing_rows = sorted(markers - rows_set)
    missing_markers = sorted(rows_set - markers)

    print(f"страниц: {len(pages)}")
    print(f"пометок в транскрипции: {len(markers)} (вхождений {sum(counts.values())})")
    print(f"строк в ISSUES.md: {len(rows_set)} (вхождений {len(rows)})")
    print("по страницам: " + ", ".join(f"{p}:{len(v)}" for p, v in by_page.items()))
    print(f"повторно использованные ID: {duplicated or 'нет'}")
    print(f"повторно использованные строки: {duplicated_rows or 'нет'}")
    print(f"⟦ID⟧ без строки в ISSUES.md: {missing_rows or 'нет'}")
    print(f"строки без ⟦ID⟧ в транскрипции: {missing_markers or 'нет'}")

    ok = not (missing_rows or missing_markers or duplicated or duplicated_rows)
    print("ИТОГ:", "соответствие полное" if ok else "ЕСТЬ РАСХОЖДЕНИЯ")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
