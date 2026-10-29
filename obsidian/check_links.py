#!/usr/bin/env python3
"""Проверка wikilink-ов в obsidian/ без Obsidian и внешних зависимостей.

Запуск:  python3 obsidian/check_links.py

Проверяется:
  1. каждый [[...]] / ![[...]] указывает на существующую заметку или вложение
     (по короткому имени внутри своей языковой ветки либо по пути от корня vault);
  2. ссылки внутри тела заметки ведут только в свою языковую ветку;
  3. у каждого понятия есть входящая и исходящая ссылка (нет сирот);
  4. `translations` во frontmatter указывает на существующие файлы;
  5. имена файлов уникальны в пределах языковой ветки;
  6. YAML-frontmatter разбирается (если установлен PyYAML) и содержит обязательные
     поля: id, type, semester, lang, aliases, tags, source_pages, translations, status.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "obsidian"
LANGS = ("ru", "en", "es")
LINK = re.compile(r"!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
FM_TRANS = re.compile(r"^translations:\s*\[(.*)\]\s*$", re.MULTILINE)
FM_BLOCK = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
REQUIRED = ["id", "type", "semester", "lang", "aliases", "tags",
            "source_pages", "translations", "status"]

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None


def main() -> int:
    # служебные файлы хранилища: не заметки, поэтому не проверяются как заметки
    notes = [p for p in sorted(VAULT.rglob("*.md")) if p.name != "README.md"]
    assets = {p.name for p in (VAULT / "assets").rglob("*") if p.is_file()}
    by_path = {p.relative_to(VAULT).as_posix(): p for p in notes}
    by_stem: dict[str, list[Path]] = defaultdict(list)
    for p in notes:
        by_stem[p.stem].append(p)

    problems: list[str] = []
    orphans_out: dict[Path, int] = defaultdict(int)
    orphans_in: dict[Path, int] = defaultdict(int)

    def resolve(target: str, source: Path) -> bool:
        target = target.strip()
        if target in by_path:
            return True
        if target.endswith(".md") and target[:-3] in by_path:
            return True
        if target in assets or target.split("/")[-1] in assets:
            return True
        # короткое имя внутри своей ветки
        lang = source.relative_to(VAULT).parts[0]
        if target in {p.name for p in notes if p.parent.parent.name == lang or p.parent.name == lang}:
            return True
        if "/" in target:
            cand = VAULT / (target if target.endswith(".md") else target + ".md")
            if cand.exists():
                return True
        return any(p.stem == target for p in notes)

    for note in notes:
        text = note.read_text(encoding="utf-8")
        lang = note.relative_to(VAULT).parts[0]
        rel = note.relative_to(VAULT)
        mfm = FM_BLOCK.match(text)
        if not mfm:
            problems.append(f"{rel}: нет YAML-frontmatter")
        else:
            raw = mfm.group(1)
            if yaml is not None:
                try:
                    data = yaml.safe_load(raw)
                except Exception as exc:  # noqa: BLE001
                    problems.append(f"{rel}: YAML не разбирается: {exc}")
                    data = None
                if isinstance(data, dict):
                    missing = [k for k in REQUIRED if k not in data]
                    if missing:
                        problems.append(f"{rel}: в frontmatter нет полей {missing}")
                    if data.get("lang") != lang:
                        problems.append(f"{rel}: lang={data.get('lang')!r} не совпадает с папкой {lang!r}")
                    if data.get("semester") != 3:
                        problems.append(f"{rel}: semester={data.get('semester')!r}")
                    if data.get("status") != "draft":
                        problems.append(f"{rel}: status={data.get('status')!r}")
                    if not isinstance(data.get("source_pages"), list) or not data["source_pages"]:
                        problems.append(f"{rel}: source_pages должен быть непустым списком")
                    if raw.count("id:") == 0:
                        problems.append(f"{rel}: пустой id")
        body = text
        m = FM_TRANS.search(text)
        if m:
            for t in LINK.findall(m.group(1)):
                if not resolve(t, note):
                    problems.append(f"{note.relative_to(VAULT)}: translations -> отсутствует {t!r}")
        for target in LINK.findall(body):
            if not resolve(target, note):
                problems.append(f"{note.relative_to(VAULT)}: битая ссылка [[{target}]]")
            # языковая изоляция: путь с префиксом другого языка допустим только в translations
            if "/" in target:
                prefix = target.split("/")[0]
                if prefix in LANGS and prefix != lang:
                    if m and target in m.group(1):
                        continue
                    problems.append(
                        f"{note.relative_to(VAULT)}: ссылка в другую языковую ветку [[{target}]]"
                    )
            # счёт степеней для поиска сирот
            if target in by_stem:
                for p in by_stem[target]:
                    orphans_in[p] += 1
                orphans_out[note] += 1
            elif (VAULT / (target + ".md")) in by_path:
                orphans_in[by_path[target + ".md"]] += 1
                orphans_out[note] += 1

    # сироты: только заметки понятий/лекций/MOC/глоссария
    concept_dirs = {"Понятия", "Concepts", "Conceptos", "Лекции", "Lectures", "Clases"}
    for note in notes:
        parts = note.relative_to(VAULT).parts
        if len(parts) < 2:
            continue
        if parts[1] not in concept_dirs:
            continue
        if orphans_out[note] == 0:
            problems.append(f"{note.relative_to(VAULT)}: сирота (нет исходящих ссылок)")
        if orphans_in[note] == 0:
            problems.append(f"{note.relative_to(VAULT)}: сирота (нет входящих ссылок)")

    # дубликаты имён внутри языковой ветки
    per_lang: dict[tuple[str, str], list[Path]] = defaultdict(list)
    for p in notes:
        parts = p.relative_to(VAULT).parts
        if len(parts) >= 2:
            per_lang[(parts[0], p.stem)].append(p)
    for (lang, stem), ps in per_lang.items():
        if len(ps) > 1:
            problems.append(f"{lang}: имя заметки не уникально: {stem} ({len(ps)} файлов)")

    print(f"заметок: {len(notes)}, вложений: {len(assets)}, YAML: {'PyYAML' if yaml else 'без разбора YAML'}")
    print(f"ссылок проверено: {sum(orphans_out.values())}")
    if problems:
        print("\nпроблемы:")
        for p in problems:
            print("  -", p)
    print(f"\nвсего проблем: {len(problems)}")
    print("ИТОГ:", "битых ссылок и сирот нет" if not problems else "есть проблемы")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
