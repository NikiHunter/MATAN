"""Tables of the semester-3 transcription issues (``ocr/ISSUES.md`` and ``ocr/RESOLVED.md``).

Every disputed place in ``ocr/raw/pNNN.md`` carries a marker ``⟦ID⟧`` (U illegible,
A ambiguous symbol, T slip in the notes, M mathematical inconsistency,
S unclear structure, G figure) and has exactly one row: in ``ISSUES.md`` while
it is open, in ``RESOLVED.md`` once a decision has been applied to the lectures.

Cells are separated by unescaped ``|``; a literal pipe inside a cell is written
``\\|`` (GitHub tables require this even inside math and code spans).
"""

from __future__ import annotations

import re
from pathlib import Path

ISSUES_HEADER = ("ID", "Page", "Location", "Type", "As transcribed", "Candidates", "Comment",
                 "Severity", "Status", "Decision", "Target")
RESOLVED_HEADER = ("ID", "Page", "Type", "As transcribed", "Decision", "Basis", "Target")

ID_RE = re.compile(r"[UATMSG]\d{3,4}")
MARKER_RE = re.compile(r"⟦([UATMSG]\d{3,4})⟧")
ANY_MARKER_RE = re.compile(r"⟦[^⟧\n]*⟧")
CELL_SPLIT_RE = re.compile(r"(?<!\\)\|")


def split_row(line: str) -> list[str]:
    """Cells of a table row whose literal pipes are escaped as ``\\|``."""
    inner = line.strip()
    if inner.startswith("|"):
        inner = inner[1:]
    if inner.endswith("|") and not inner.endswith("\\|"):
        inner = inner[:-1]
    return [cell.strip() for cell in CELL_SPLIT_RE.split(inner)]


def split_legacy_row(line: str) -> list[str]:
    """Cells of an old row whose pipes inside ``$…$`` math and code were not escaped."""
    inner = line.strip()[1:]
    if inner.endswith("|"):
        inner = inner[:-1]
    cells, current, k = [], [], 0
    in_math = in_code = False
    while k < len(inner):
        ch = inner[k]
        if ch == "\\" and k + 1 < len(inner):
            current.append(inner[k:k + 2])
            k += 2
            continue
        if ch == "`" and not in_math:
            in_code = not in_code
        elif ch == "$" and not in_code:
            if inner.startswith("$$", k):
                current.append("$$")
                k += 2
                in_math = not in_math
                continue
            in_math = not in_math
        elif ch == "|" and not in_math and not in_code:
            cells.append("".join(current).strip())
            current = []
            k += 1
            continue
        current.append(ch)
        k += 1
    cells.append("".join(current).strip())
    return cells


def escape_cell(text: str) -> str:
    """Escape every literal pipe so that the cell survives GitHub's table parser."""
    return re.sub(r"(?<!\\)\|", r"\\|", text.replace("\n", " "))


def format_row(cells) -> str:
    return "| " + " | ".join(cells) + " |"


def header_lines(header) -> list[str]:
    return [format_row(header), "|" + "---|" * len(header)]


def read_table(path: Path, header) -> tuple[list[dict[str, str]], list[str]]:
    """Rows (as dicts keyed by the header) and problems found while parsing."""
    problems: list[str] = []
    if not path.is_file():
        return [], [f"{path.name}: file is missing"]
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        start = lines.index(format_row(header))
    except ValueError:
        return [], [f"{path.name}: table header must be exactly: {format_row(header)}"]
    if start + 1 >= len(lines) or not re.fullmatch(r"\|(?:-{3,}\|)+", lines[start + 1].strip()):
        problems.append(f"{path.name}: separator row missing after the header")
    rows = []
    for number, line in enumerate(lines[start + 2:], start + 3):
        if not line.startswith("|"):
            break
        cells = split_row(line)
        if len(cells) != len(header):
            problems.append(f"{path.name}:{number}: expected {len(header)} cells, found {len(cells)}")
            continue
        row = dict(zip(header, cells))
        row["_line"] = str(number)
        rows.append(row)
    return rows, problems


def open_ids(root: Path) -> dict[str, dict[str, str]]:
    rows, _ = read_table(root / "ocr" / "ISSUES.md", ISSUES_HEADER)
    return {row["ID"]: row for row in rows if row.get("Status") == "open"}


def resolved_ids(root: Path) -> dict[str, dict[str, str]]:
    rows, _ = read_table(root / "ocr" / "RESOLVED.md", RESOLVED_HEADER)
    return {row["ID"]: row for row in rows}
