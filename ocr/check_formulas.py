#!/usr/bin/env python3
"""Проверка формул и frontmatter без внешних зависимостей.

Запуск:  python3 ocr/check_formulas.py [каталоги...]
По умолчанию проверяются lectures/ и obsidian/.

Что проверяется:
  1. YAML frontmatter есть, открыт/закрыт и разбирается как простой YAML.
  2. Чётное число неэкранированных `$` в каждой строке (парность `$`/`$$`).
  3. `\begin{...}` и `\end{...}` парны, имена окружений совпадают.
  4. Нет `\` перед не-командой (например `\1`, `\ `), кроме известных команд.
  5. Нет пробела сразу после открывающего `$`.
  6. Блоки `$$` стоят на отдельных строках.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIRS = ("lectures", "obsidian")

BEGIN = re.compile(r"\\(begin|end)\{([^}]*)\}")
KNOWN_SINGLE = set("\\{}%&_#$|~.,;:!()-+/*'\"[]<>?=@^` ")


def split_frontmatter(text: str) -> tuple[dict[str, str], str, list[str]]:
    problems: list[str] = []
    if not text.startswith("---\n"):
        return {}, text, ["нет YAML frontmatter (файл не начинается с ---)"]
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text, ["frontmatter не закрыт (нет второй строки ---)"]
    block = text[4:end]
    body = text[end + 5 :]
    meta: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t", "-")):
            continue
        if ":" not in line:
            problems.append(f"строка frontmatter без ':' -> {line!r}")
            continue
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip()
    return meta, body, problems


def find_unclosed_math(body: str) -> list[str]:
    """Ищем незакрытые $ внутри одиночной строки."""
    problems = []
    for lineno, line in enumerate(body.splitlines(), 1):
        if line.startswith(">"):
            line = line.lstrip("> ").rstrip()
        stripped = line.replace("\\$", "")
        if stripped.count("$$") % 2 == 0:
            rest = stripped.replace("$$", "")
            if rest.count("$") % 2:
                problems.append(f"строка {lineno}: нечётное число `$` -> {line[:70]!r}")
        else:
            problems.append(f"строка {lineno}: непарный `$$` -> {line[:70]!r}")
    return problems


def check_environment_pairing(body: str) -> list[str]:
    problems = []
    stack: list[tuple[str, int]] = []
    for lineno, line in enumerate(body.splitlines(), 1):
        for kind, name in BEGIN.findall(line):
            if name == "array" or name in {"pmatrix", "bmatrix", "vmatrix", "cases"}:
                pass
            if kind == "begin":
                stack.append((name, lineno))
            else:
                if not stack:
                    problems.append(f"строка {lineno}: \\end{{{name}}} без \\begin")
                    continue
                open_name, open_line = stack.pop()
                if open_name != name:
                    problems.append(
                        f"строка {lineno}: \\end{{{name}}} закрывает \\begin{{{open_name}}} из строки {open_line}"
                    )
    for name, lineno in stack:
        problems.append(f"строка {lineno}: \\begin{{{name}}} не закрыт")
    return problems


BACKSLASH = re.compile(r"\\(.)")


def check_backslashes(body: str) -> list[str]:
    problems = []
    for lineno, line in enumerate(body.splitlines(), 1):
        for m in BACKSLASH.finditer(line):
            ch = m.group(1)
            if ch.isalpha() or ch in KNOWN_SINGLE:
                continue
            problems.append(f"строка {lineno}: `\\{ch}` — обратная косая перед не-командой")
    return problems


DELIM = re.compile(r"(?<!\\)(\$\$|\$)")


def check_dollar_spacing(body: str) -> list[str]:
    """Пробел после *открывающего* разделителя недопустим (сравниваем по чётности)."""
    problems = []
    for lineno, line in enumerate(body.splitlines(), 1):
        tokens = list(DELIM.finditer(line))
        for index, m in enumerate(tokens):
            if m.group(0) != "$":
                continue
            after = line[m.end(): m.end() + 1]
            if after != " ":
                continue
            # открывающий ли это `$`: считаем непарные одиночные разделители до него
            before = sum(1 for t in tokens[:index] if t.group(0) == "$")
            if before % 2 == 0:
                problems.append(f"строка {lineno}: пробел после открывающего `$`")
    return problems


def check_display_blocks(body: str) -> list[str]:
    problems = []
    for lineno, line in enumerate(body.splitlines(), 1):
        stripped = line.strip().lstrip("> ").strip()
        if stripped.startswith("$$") and stripped != "$$" and not stripped.endswith("$$"):
            problems.append(f"строка {lineno}: блок `$$` не на отдельной строке")
        elif stripped.count("$$") == 1 and not stripped.startswith("$$"):
            problems.append(f"строка {lineno}: `$$` не в начале строки")
    return problems


def main(argv: list[str]) -> int:
    dirs = argv[1:] or list(DEFAULT_DIRS)
    files: list[Path] = []
    for d in dirs:
        base = ROOT / d
        if base.exists():
            # README.md — служебная документация каталога, а не заметка с формулами
            files.extend(sorted(p for p in base.rglob("*.md") if p.name != "README.md"))
    if not files:
        print("не найдено markdown-файлов")
        return 1

    total = Counter()
    bad_files = 0
    for path in files:
        rel = path.relative_to(ROOT)
        meta, body, problems = split_frontmatter(path.read_text(encoding="utf-8"))
        problems += find_unclosed_math(body)
        problems += check_environment_pairing(body)
        problems += check_backslashes(body)
        problems += check_dollar_spacing(body)
        problems += check_display_blocks(body)
        for key in ("lang",):
            if key in meta:
                total[key + ":" + meta[key]] += 1
        total["files"] += 1
        if "type" in meta:
            total["type:" + meta["type"]] += 1
        if problems:
            bad_files += 1
            print(f"\n{rel}:")
            for p in problems:
                print("  -", p)

    print()
    print(f"файлов проверено: {total['files']}")
    print("языки: " + ", ".join(f"{k.split(':')[1]}={v}" for k, v in sorted(total.items()) if k.startswith("lang:")))
    types = {k.split(":")[1]: v for k, v in total.items() if k.startswith("type:")}
    if types:
        print("типы заметок: " + ", ".join(f"{k}={v}" for k, v in sorted(types.items())))
    print("файлов с замечаниями:", bad_files)
    print("ИТОГ:", "замечаний нет" if bad_files == 0 else "есть замечания")
    return 0 if bad_files == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
