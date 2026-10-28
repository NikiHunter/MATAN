#!/usr/bin/env python3
"""Build the two reading views of the course from one source.

``MathInMind/`` is both the source and the **GitHub view**.  Running this
script (idempotently) rewrites it in place:

* inline math becomes ``$`...`$`` and display math a ```` ```math ```` fence
  (GitHub's Markdown pass otherwise drops ``\\{``, ``\\|``, ``\\,`` and can turn
  ``a<b>c`` into HTML);
* every course section, labelled theorem and numbered lecture statement gets
  an ``<a id>`` anchor;
* the first mention of each registered term in a note, and every reference
  such as "Theorem 2.3.5", becomes a relative link to its definition;
* navigation bars name the previous and next note;
* ``{lang}/term-index.md`` lists every term, theorem and numbered statement.

It then generates the **Obsidian view**, ``MathInMind-Obsidian/``, a vault
with ``$...$`` MathJax, ``[[wikilinks]]`` to block ids (hover previews),
callouts for definitions and theorems, foldable answers and aliases.

    python3 scripts/build_views.py           # rebuild both views
    python3 scripts/build_views.py --check   # fail if either view is stale

Edit the Markdown in ``MathInMind/`` (plain ``$...$`` is fine: it is
converted on the next build); never edit ``MathInMind-Obsidian/`` by hand.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path, PurePosixPath
from urllib.parse import quote, unquote

sys.path.insert(0, str(Path(__file__).resolve().parent))

import mdtext  # noqa: E402
from term_registry import CHAPTER_STATEMENTS, GLOSSARY, LABELS, TERMS  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "MathInMind"
OBSIDIAN = ROOT / "MathInMind-Obsidian"
REPO_URL = "https://github.com/NikiHunter/matan"
LANGS = ("en", "ru", "es")
LECTURES = "lectures-2025-26"

KIND_PREFIX = {"definition": "def", "theorem": "thm", "lemma": "lem", "corollary": "cor",
               "remark": "rem", "proposition": "prop"}
# Nominative forms that introduce a statement (headings, bold labels).
STATEMENT_WORDS = {
    "en": {"Definition": "definition", "Theorem": "theorem", "Lemma": "lemma",
           "Corollary": "corollary", "Remark": "remark", "Proposition": "proposition"},
    "ru": {"Определение": "definition", "Теорема": "theorem", "Лемма": "lemma",
           "Следствие": "corollary", "Замечание": "remark", "Утверждение": "proposition"},
    "es": {"Definición": "definition", "Teorema": "theorem", "Lema": "lemma",
           "Corolario": "corollary", "Observación": "remark", "Proposición": "proposition"},
}
# Every inflected form that may precede a statement number in running text.
REFERENCE_WORDS = {
    "en": [(r"definitions?", "definition"), (r"theorems?", "theorem"), (r"lemmas?", "lemma"),
           (r"corollar(?:y|ies)", "corollary"), (r"remarks?", "remark"), (r"propositions?", "proposition")],
    "ru": [(r"определени(?:е|я|ю|ем|и|й|ям|ями|ях)", "definition"),
           (r"теорем(?:а|ы|е|у|ой|ою|ам|ами|ах)?", "theorem"),
           (r"лемм(?:а|ы|е|у|ой|ою|ам|ами|ах)?", "lemma"),
           (r"следстви(?:е|я|ю|ем|и|й|ям|ями|ях)", "corollary"),
           (r"замечани(?:е|я|ю|ем|и|й|ям|ями|ях)", "remark"),
           (r"утверждени(?:е|я|ю|ем|и|й|ям|ями|ях)", "proposition")],
    "es": [(r"definici(?:ón|ones)", "definition"), (r"teoremas?", "theorem"), (r"lemas?", "lemma"),
           (r"corolarios?", "corollary"), (r"observaci(?:ón|ones)", "remark"),
           (r"proposici(?:ón|ones)", "proposition")],
}
NOT_A_STATEMENT = re.compile(r"proof|доказательств|demostraci|continu|продолжени|idea|идея|sketch|набросок", re.I)
NUMBER = r"\d+\.\d+\.\d+"
PROOF_LABEL = re.compile(r"(?:proof|доказательство|demostración)\b", re.I)
ANCHOR_RE = re.compile(r'<a id="([^"]+)"></a>')
ANCHOR_LINE_RE = re.compile(r'^\s*<a id="([^"]+)"></a>\s*$')
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
NAV_LINK_RE = re.compile(r"\[(?:[^\[\]\n]|\[[^\[\]\n]*\])*\]\([^)\n]*\)")

UI = {
    "en": {"index": "Course index", "terms": "Terms & theorems", "lecture": ("Lecture", "Lectures"),
           "lecture_index": "Lecture index", "ticket": "Ticket", "section": "§"},
    "ru": {"index": "Оглавление", "terms": "Термины и теоремы", "lecture": ("Лекция", "Лекции"),
           "lecture_index": "Указатель лекций", "ticket": "Билет", "section": "§"},
    "es": {"index": "Índice", "terms": "Términos y teoremas", "lecture": ("Lección", "Lecciones"),
           "lecture_index": "Índice de lecciones", "ticket": "Billete", "section": "§"},
}
KIND_NAMES = {
    "en": {"definition": "Definition", "theorem": "Theorem", "lemma": "Lemma", "corollary": "Corollary",
           "remark": "Remark", "proposition": "Proposition"},
    "ru": {"definition": "Определение", "theorem": "Теорема", "lemma": "Лемма", "corollary": "Следствие",
           "remark": "Замечание", "proposition": "Утверждение"},
    "es": {"definition": "Definición", "theorem": "Teorema", "lemma": "Lema", "corollary": "Corolario",
           "remark": "Observación", "proposition": "Proposición"},
}


# --- file model -------------------------------------------------------------

class Note:
    def __init__(self, rel: str, text: str):
        self.rel = rel  # POSIX path relative to VAULT
        self.text = text
        parts = rel.split("/")
        self.lang = parts[0] if parts[0] in LANGS else None
        self.kind = classify(rel)
        self.chapter = chapter_of(self)

    @property
    def lines(self) -> list[str]:
        return self.text.split("\n")


def classify(rel: str) -> str:
    parts = rel.split("/")
    name = parts[-1]
    if len(parts) == 2 and parts[0] in LANGS:
        if re.fullmatch(r"(0[1-9]|1\d|2[01])-.+\.md", name):
            return "chapter"
        return {"index.md": "index", "glossary.md": "glossary", "term-index.md": "term-index"}.get(name, "support")
    if len(parts) == 3 and parts[1] == LECTURES:
        return "lecture" if name.startswith("lecture-") else "index"
    if rel.startswith("ru/lectures/"):
        return "register" if re.match(r"\d\d-", name) else ("index" if name == "index.md" else "support")
    if rel.startswith("ru/exam/tickets/"):
        return "ticket"
    if rel.startswith("ru/exam/"):
        return "index"
    if rel.startswith("ru/purgatory/"):
        return "purgatory"
    return "other"


LECTURER_TO_COURSE = {1: 2, 2: 4, 3: 7, 4: 9, 5: 14, 6: 15}


def chapter_of(note: Note) -> int | None:
    """Course chapter a note belongs to (restricts ambiguous terms)."""
    name = note.rel.split("/")[-1]
    if note.kind == "chapter" or (note.kind == "support" and name[:2].isdigit()):
        return int(name[:2])
    if note.kind == "lecture":
        first = int(re.match(r"lecture-(\d+)", name).group(1))
        for limit, chapter in ((7, 2), (13, 3), (21, 5), (35, 7), (53, 9), (60, 14)):
            if first <= limit:
                return chapter
        return 15
    if note.kind == "register":
        return LECTURER_TO_COURSE.get(int(re.search(r"-(\d)-\d+\.md$", name).group(1)))
    if note.kind == "ticket":
        section = re.search(r'(?m)^lecture_section:\s*"?\d\d-[^"]*-(\d)-\d+\.md', note.text)
        return LECTURER_TO_COURSE.get(int(section.group(1))) if section else None
    return None


def lecture_numbers(name: str) -> list[int]:
    return [int(x) for x in re.findall(r"\d+", name)]


def title_of(text: str) -> str:
    match = re.search(r'(?m)^title:\s*"?(.*?)"?\s*$', text)
    return match.group(1) if match else ""


def relpath(target: str, source: str) -> str:
    """Relative link from note `source` to vault path `target` (POSIX)."""
    if target.split("#")[0] == source:
        return "#" + target.split("#", 1)[1] if "#" in target else source.rsplit("/", 1)[-1]
    path, _, frag = target.partition("#")
    rel = os.path.relpath(path, os.path.dirname(source) or ".").replace(os.sep, "/")
    return quote(rel, safe="/-._~") + ("#" + frag if frag else "")


# --- step 1: anchors ----------------------------------------------------------

def statement_sites(line: str, lang: str):
    """Yield (kind, number) for statements introduced on this line."""
    words = STATEMENT_WORDS[lang]
    alternation = "|".join(words)
    heading = HEADING_RE.match(line)
    if heading:
        if NOT_A_STATEMENT.search(heading.group(2)):
            return
        for match in re.finditer(rf"(?<!\w)({alternation})\s+({NUMBER})(?![\d.]*\d)", heading.group(2), re.I):
            yield statement_kind(lang, match.group(1)), match.group(2)
        return
    for match in leading_labels(line, lang):
        if not NOT_A_STATEMENT.search(match.group(3)):
            yield statement_kind(lang, match.group(1)), match.group(2)


def leading_labels(line: str, lang: str):
    """Bold statement labels at the start of a line, e.g. '**Theorem 2.3.5.** **Theorem 2.3.6.**'."""
    alternation = "|".join(STATEMENT_WORDS[lang])
    label = re.compile(rf'(?:<a id="[^"]+"></a>)?\*\*({alternation})\s+({NUMBER})([^*]*)\*\*\s*', re.I)
    pos = re.match(r"^(?:\s*>)*\s*", line).end()
    while True:
        match = label.match(line, pos)
        if not match:
            return
        yield match
        pos = match.end()


def statement_kind(lang: str, word: str) -> str:
    return next(v for k, v in STATEMENT_WORDS[lang].items() if k.casefold() == word.casefold())


def anchor_id(kind: str, number: str) -> str:
    return f"{KIND_PREFIX[kind]}-{number.replace('.', '-')}"


def add_anchors(note: Note) -> None:
    lines = note.lines
    existing = set(ANCHOR_RE.findall(note.text))
    out: list[str] = []
    in_fence = None
    if note.kind == "chapter":
        chapter = int(note.rel.split("/")[-1][:2])
        statements = list(CHAPTER_STATEMENTS[chapter])
        quote_index = -1
    for i, line in enumerate(lines):
        opened = mdtext.fence_open(line)
        if in_fence:
            out.append(line)
            if mdtext.fence_closes(line, *in_fence):
                in_fence = None
            continue
        if opened:
            in_fence = (opened[1], opened[2])
            out.append(line)
            continue
        previous = out[-1] if out else ""
        if note.kind == "chapter":
            section = re.match(r"^## (\d+)\.(\d+)\s", line)
            if section:
                anchor = f"sec-{section.group(1)}-{section.group(2)}"
                if anchor not in existing:
                    out.append(f'<a id="{anchor}"></a>')
                    existing.add(anchor)
            starts_quote = line.startswith("> ") and not previous.startswith(">")
            label = re.match(r"^> (?:<a id=\"[^\"]+\"></a>)?\*\*", line)
            if starts_quote and label:
                quote_index += 1
                if quote_index >= 1:
                    anchor = statements[quote_index - 1][0]
                    if anchor not in existing:
                        line = "> " + f'<a id="{anchor}"></a>' + line[2:]
                        existing.add(anchor)
        elif note.kind in ("lecture", "register") and note.lang:
            for kind, number in statement_sites(line, note.lang):
                anchor = anchor_id(kind, number)
                if anchor in existing:
                    continue
                existing.add(anchor)
                if HEADING_RE.match(line):
                    out.append(f'<a id="{anchor}"></a>')
                else:
                    match = next(m for m in leading_labels(line, note.lang)
                                 if anchor_id(statement_kind(note.lang, m.group(1)), m.group(2)) == anchor)
                    start = match.start()
                    line = line[:start] + f'<a id="{anchor}"></a>' + line[start:]
        out.append(line)
    if note.kind == "chapter" and quote_index != len(statements):
        raise SystemExit(f"{note.rel}: expected {len(statements)} labelled statements, found {quote_index}")
    note.text = "\n".join(out)


# --- step 2: anchor catalogue ----------------------------------------------

class Anchor:
    def __init__(self, note: Note, anchor: str, line_no: int, heading: str | None, line: str):
        self.note, self.id, self.line_no, self.heading, self.line = note, anchor, line_no, heading, line

    @property
    def target(self) -> str:
        return f"{self.note.rel}#{self.id}"


def catalogue(notes: dict[str, Note]) -> dict[str, dict[str, Anchor]]:
    result: dict[str, dict[str, Anchor]] = {}
    for rel, note in notes.items():
        anchors = {}
        lines = note.lines
        for i, line in enumerate(lines):
            for anchor in ANCHOR_RE.findall(line):
                heading = None
                if ANCHOR_LINE_RE.match(line):
                    j = i + 1
                    while j < len(lines) and ANCHOR_LINE_RE.match(lines[j]):
                        j += 1
                    if j < len(lines) and HEADING_RE.match(lines[j]):
                        heading = HEADING_RE.match(lines[j]).group(2)
                        line_text = lines[j]
                    else:
                        line_text = lines[j] if j < len(lines) else ""
                else:
                    line_text = line
                anchors.setdefault(anchor, Anchor(note, anchor, i, heading, line_text))
        result[rel] = anchors
    return result


def lecture_order(rel: str) -> tuple:
    name = rel.rsplit("/", 1)[-1]
    numbers = lecture_numbers(name)
    return (numbers[0] if numbers else 999, name)


def numbered_index(notes, anchors):
    """First site of each numbered statement, per language and collection."""
    index = {}
    for lang in LANGS:
        for collection in ("lecture", "register"):
            table = {}
            rels = sorted((r for r, n in notes.items() if n.lang == lang and n.kind == collection), key=lecture_order)
            for rel in rels:
                for anchor_id_, anchor in anchors[rel].items():
                    if re.fullmatch(r"(def|thm|lem|cor|rem|prop)-\d+-\d+-\d+", anchor_id_):
                        table.setdefault(anchor_id_, anchor)
            index[(lang, collection)] = table
    return index


def chapter_files(notes) -> dict[tuple[str, int], str]:
    files = {}
    for rel, note in notes.items():
        if note.kind in ("chapter", "support") and note.lang and note.rel.count("/") == 1:
            name = rel.split("/")[-1]
            if name[:2].isdigit():
                files[(note.lang, int(name[:2]))] = rel
    return files


# --- step 3: navigation -----------------------------------------------------

def is_nav_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith("[") or "](" not in stripped:
        return False
    rest = NAV_LINK_RE.sub("", stripped)
    return not rest.replace("·", "").strip()


def nav_links(line: str) -> list[str]:
    return NAV_LINK_RE.findall(line)


def rewrite_navigation(note: Note, notes: dict[str, Note]) -> None:
    lang = note.lang
    if not lang:
        return
    ui = UI[lang]
    if note.kind == "chapter":
        number = int(note.rel.split("/")[-1][:2])
        files = chapter_files(notes)
        items = []
        prev_rel, next_rel = files.get((lang, number - 1)), files.get((lang, number + 1))
        if prev_rel and number > 1:
            items.append(f"[← {number - 1}. {title_of(notes[prev_rel].text)}]({relpath(prev_rel, note.rel)})")
        items.append(f"[{ui['index']}](index.md)")
        items.append(f"[{ui['terms']}](term-index.md)")
        if next_rel:
            items.append(f"[{number + 1}. {title_of(notes[next_rel].text)} →]({relpath(next_rel, note.rel)})")
        replace_nav(note, " · ".join(items), lambda links: any("](index.md)" in l for l in links))
    elif note.kind == "lecture":
        siblings = sorted((r for r, n in notes.items() if n.lang == lang and n.kind == "lecture"), key=lecture_order)
        pos = siblings.index(note.rel)

        def label(rel):
            nums = lecture_numbers(rel.rsplit("/", 1)[-1])
            word = ui["lecture"][0] if len(nums) == 1 else ui["lecture"][1]
            return f"{word} {nums[0]}" if len(nums) == 1 else f"{word} {nums[0]}–{nums[-1]}"

        def build(links):
            others = [l for l in links if "](index.md)" not in l and not re.search(r"\]\(lecture-[\d-]+\.md\)", l)]
            items = []
            if pos > 0:
                items.append(f"[← {label(siblings[pos - 1])}]({relpath(siblings[pos - 1], note.rel)})")
            items.append(f"[{ui['lecture_index']}](index.md)")
            if pos + 1 < len(siblings):
                items.append(f"[{label(siblings[pos + 1])} →]({relpath(siblings[pos + 1], note.rel)})")
            items.append(f"[{ui['terms']}](../term-index.md)")
            return " · ".join(items + [l for l in others if "term-index.md" not in l])
        replace_nav(note, build, lambda links: any("](index.md)" in l for l in links))
    elif note.kind in ("ticket", "register"):
        siblings = sorted(r for r, n in notes.items() if n.kind == note.kind)
        pos = siblings.index(note.rel)

        def label(rel):
            name = rel.rsplit("/", 1)[-1]
            if note.kind == "ticket":
                return f"{ui['ticket']} {int(name[:2])}"
            sec = re.search(r"-(\d+)-(\d+)\.md$", name)
            return f"§{sec.group(1)}.{sec.group(2)}"

        def build(links):
            core = [l for l in links if not l.startswith("[←") and not l.rstrip(")").split("](")[0].endswith("→")]
            items = []
            if pos > 0:
                items.append(f"[← {label(siblings[pos - 1])}]({relpath(siblings[pos - 1], note.rel)})")
            items.extend(core)
            if pos + 1 < len(siblings):
                items.append(f"[{label(siblings[pos + 1])} →]({relpath(siblings[pos + 1], note.rel)})")
            return " · ".join(items)
        index_link = "](../index.md)" if note.kind == "ticket" else "](index.md)"
        replace_nav(note, build, lambda links: any(index_link in l for l in links))


def replace_nav(note: Note, new, predicate) -> None:
    lines = note.lines
    fm_end = len(mdtext.split_frontmatter(note.text)[0].split("\n")) - 1
    for i, line in enumerate(lines):
        if i < fm_end or not is_nav_line(line):
            continue
        links = nav_links(line)
        if predicate(links):
            lines[i] = new(links) if callable(new) else new
    note.text = "\n".join(lines)


# --- step 4: automatic links ------------------------------------------------

class TermMatcher:
    """Finds registered phrases at word starts, longest phrase first.

    Phrases are bucketed by their first letter so that only a few dozen
    alternatives are tried at each word instead of the whole registry.
    """

    WORD_START = re.compile(r"(?<![\w\[-])\w")

    def __init__(self, lang: str):
        buckets, generic = defaultdict(list), []
        for term in TERMS:
            for phrase in term.phrases(lang):
                entry = (len(phrase), phrase.replace("–", "[–-]"), term)
                (buckets[phrase[0].casefold()] if phrase[0].isalpha() else generic).append(entry)
        self.lookup = {}
        self.regexes = {key: self._compile(entries + generic) for key, entries in buckets.items()}
        self.generic = self._compile(generic) if generic else None

    def _compile(self, entries):
        groups = []
        for _, pattern, term in sorted(entries, key=lambda e: -e[0]):
            name = f"t{len(self.lookup)}"
            self.lookup[name] = term
            groups.append(f"(?P<{name}>{pattern})")
        return re.compile("(?:" + "|".join(groups) + r")(?![\w-])", re.I)

    def finditer(self, flat: str):
        """Yield (match, term); characters masked as NUL are never inside a match."""
        pos = 0
        while True:
            word = self.WORD_START.search(flat, pos)
            if not word:
                return
            start = word.start()
            regex = self.regexes.get(flat[start].casefold(), self.generic)
            match = regex.match(flat, start) if regex else None
            if match and "\x00" not in match.group(0):
                yield match, self.lookup[match.lastgroup]
                pos = match.end()
            else:
                pos = start + 1


REFERENCE_RE = {
    lang: re.compile(
        r"(?<![\w\[])(?P<word>" + "|".join(f"(?:{p})" for p, _ in REFERENCE_WORDS[lang]) + r")"
        r"\s+(?P<first>" + NUMBER + r")(?P<more>(?:\s*(?:,|и|and|or|или|y|o|–|—|-)\s*" + NUMBER + r")*)",
        re.I)
    for lang in LANGS
}


def reference_kind(lang: str, word: str) -> str:
    for pattern, kind in REFERENCE_WORDS[lang]:
        if re.fullmatch(pattern, word, re.I):
            return kind
    raise ValueError(word)


class Linker:
    def __init__(self, notes, anchors):
        self.notes = notes
        self.anchors = anchors
        self.numbered = numbered_index(notes, anchors)
        self.chapters = chapter_files(notes)
        self.terms = {lang: TermMatcher(lang) for lang in LANGS}
        self.stats = defaultdict(int)

    def resolve_numbered(self, note: Note, anchor: str) -> str | None:
        lang = note.lang
        if note.kind in ("register", "ticket", "purgatory") or (note.rel.startswith("ru/lectures/")):
            order = [("ru", "register"), ("ru", "lecture")]
        else:
            order = [(lang, "lecture"), (lang, "register")]
        for key in order:
            hit = self.numbered.get(key, {}).get(anchor)
            if hit:
                return hit.target
        return None

    def resolve_term(self, note: Note, term) -> str | None:
        if note.kind in ("lecture", "register", "ticket", "purgatory") and term.lec:
            hit = self.resolve_numbered(note, term.lec)
            if hit:
                return hit
        number, _, frag = term.target.partition("#")
        rel = self.chapters.get((note.lang, int(number)))
        if rel and frag in self.anchors[rel]:
            return f"{rel}#{frag}"
        return None

    def link_note(self, note: Note) -> None:
        if not note.lang or note.kind in ("index", "glossary", "term-index", "other"):
            return
        if note.rel == "ru/lectures/terms.md":  # a hand-written link list already
            return
        lines = note.lines
        fm_lines = len(mdtext.split_frontmatter(note.text)[0].split("\n")) - 1
        linked_terms: set[str] = set()
        # Targets already linked from this note count as linked.
        for target in re.findall(r"\]\(([^)\s]+)\)", note.text):
            linked_terms.add(target)
        section = None  # latest course section anchor
        heading_anchors: set[str] = set()  # anchors attached to the current heading
        pending: set[str] = set()
        block_anchors: set[str] = set()  # anchors inside the current block
        in_fence = None
        for i, line in enumerate(lines):
            if i < fm_lines:
                continue
            opened = mdtext.fence_open(line)
            if in_fence:
                if mdtext.fence_closes(line, *in_fence):
                    in_fence = None
                continue
            if opened:
                in_fence = (opened[1], opened[2])
                continue
            anchor_line = ANCHOR_LINE_RE.match(line)
            if anchor_line:
                pending.add(anchor_line.group(1))
                if anchor_line.group(1).startswith("sec-"):
                    section = anchor_line.group(1)
                continue
            if not line.strip():
                block_anchors = set()
                continue
            if HEADING_RE.match(line):
                heading_anchors, pending, block_anchors = pending, set(), set()
                continue
            block_anchors |= set(ANCHOR_RE.findall(line))
            if (is_nav_line(line) or line.lstrip().startswith(("<", "![")) or re.match(r"^\s*\|?\s*:?-{3,}", line)):
                continue
            own = {section} | heading_anchors | block_anchors
            lines[i] = self.link_line(note, line, linked_terms, own)
        note.text = "\n".join(lines)

    def link_line(self, note, line, linked, own_block):
        lang = note.lang
        edits = []  # (start, end, replacement)
        mask = mdtext.protected_mask(line, protect_bold=False)
        # Bold text is a statement label or emphasis; only proof labels link back.
        for bold in mdtext.BOLD_RE.finditer(line):
            if not PROOF_LABEL.match(bold.group(0)[2:]):
                for k in range(*bold.span()):
                    mask[k] = True
        own = set(ANCHOR_RE.findall(line)) | own_block
        for match in REFERENCE_RE[lang].finditer(line):
            if any(mask[match.start():match.end()]):
                continue
            kind = reference_kind(lang, match.group("word"))
            numbers = [match.span("first")] + [m.span() for m in re.compile(NUMBER).finditer(
                line, match.start("more"), match.end("more"))]
            for k, (a, b) in enumerate(numbers):
                anchor = anchor_id(kind, line[a:b])
                if anchor in own:
                    continue
                target = self.resolve_numbered(note, anchor)
                if not target:
                    self.stats["unresolved-reference"] += 1
                    continue
                start = match.start() if k == 0 else a
                edits.append((start, b, f"[{line[start:b]}]({relpath(target, note.rel)})"))
                self.stats["reference"] += 1
        term_mask = mdtext.protected_mask(line, protect_bold=True)
        taken = [(a, b) for a, b, _ in edits]
        flat = "".join("\x00" if term_mask[k] else ch for k, ch in enumerate(line))
        for match, term in self.terms[lang].finditer(flat):
            if any(a < match.end() and match.start() < b for a, b in taken):
                continue
            if term.chapters and note.chapter is not None:
                low, high = term.chapters
                if not low <= note.chapter <= high:
                    continue
            target = self.resolve_term(note, term)
            if not target or term.id in linked or relpath(target, note.rel) in linked:
                continue
            rel_target, _, frag = target.partition("#")
            if rel_target == note.rel and frag in own:
                continue
            linked.add(term.id)
            linked.add(relpath(target, note.rel))
            edits.append((match.start(), match.end(),
                          f"[{line[match.start():match.end()]}]({relpath(target, note.rel)})"))
            taken.append((match.start(), match.end()))
            self.stats["term"] += 1
        for start, end, replacement in sorted(edits, reverse=True):
            line = line[:start] + replacement + line[end:]
        return line


# --- step 5: glossary and term index ---------------------------------------

def link_glossary(note: Note, linker: Linker) -> None:
    lines = note.lines
    for i, line in enumerate(lines):
        if not line.startswith("| ") or line.startswith("| English") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 3:
            continue
        plain = [re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", c) for c in cells]
        term_id = GLOSSARY.get(plain[0])
        term = next((t for t in TERMS if t.id == term_id), None)
        if not term:
            lines[i] = "| " + " | ".join(plain) + " |"
            continue
        new = []
        for lang, cell in zip(LANGS, plain):
            fake = Note(f"{lang}/glossary.md", "")
            target = linker.resolve_term(fake, term)
            new.append(f"[{cell}]({relpath(target, note.rel)})" if target else cell)
        lines[i] = "| " + " | ".join(new) + " |"
    note.text = "\n".join(lines)


INDEX_TEXT = {
    "en": {
        "title": "Index of terms and theorems",
        "intro": ("Every entry jumps straight to the place where the notion is defined or the result is stated. "
                  "The **Course** column points to the concise 21-chapter course; the **Lectures** column points to "
                  "the numbered statement in the 2025/26 lecture notes. The same links are inserted automatically at "
                  "the first mention of each term inside every note."),
        "terms": "Terms", "theorems": "Named theorems and results", "numbered": "Numbered statements of the 2025/26 lectures",
        "numbered_intro": "Numbers follow the lecturer's scheme *chapter.section.item*. The first lecture that states the item is linked.",
        "cols": ("Term", "Course", "Lectures"), "ncols": ("Statement", "Summary", "Lecture"),
        "chapter": "Chapter", "lecture": "Lecture",
    },
    "ru": {
        "title": "Указатель терминов и теорем",
        "intro": ("Каждая строка ведёт прямо к месту, где понятие определено или утверждение сформулировано. "
                  "Столбец **Курс** ведёт в краткий курс из 21 главы, столбец **Лекции** — к пронумерованному "
                  "утверждению в конспектах лекций 2025/26. Такие же ссылки автоматически расставлены при первом "
                  "упоминании термина в каждой заметке."),
        "terms": "Термины", "theorems": "Именные теоремы и результаты", "numbered": "Пронумерованные утверждения лекций 2025/26",
        "numbered_intro": "Нумерация лектора: *глава.параграф.пункт*. Ссылка ведёт на первую лекцию, где утверждение сформулировано.",
        "cols": ("Термин", "Курс", "Лекции"), "ncols": ("Утверждение", "Кратко", "Лекция"),
        "chapter": "Глава", "lecture": "Лекция", "register": "Экзаменационный реестр",
    },
    "es": {
        "title": "Índice de términos y teoremas",
        "intro": ("Cada entrada lleva directamente al lugar donde se define la noción o se enuncia el resultado. "
                  "La columna **Curso** apunta al curso conciso de 21 capítulos; la columna **Lecciones**, al enunciado "
                  "numerado de los apuntes 2025/26. Los mismos enlaces se insertan automáticamente en la primera "
                  "mención de cada término dentro de cada nota."),
        "terms": "Términos", "theorems": "Teoremas y resultados con nombre", "numbered": "Enunciados numerados de las lecciones 2025/26",
        "numbered_intro": "La numeración sigue el esquema del profesor *capítulo.sección.punto*. Se enlaza la primera lección que lo enuncia.",
        "cols": ("Término", "Curso", "Lecciones"), "ncols": ("Enunciado", "Resumen", "Lección"),
        "chapter": "Capítulo", "lecture": "Lección",
    },
}


def statement_summary(anchor: Anchor, lang: str) -> str:
    """A short, render-safe description of a numbered statement."""
    text = anchor.heading or anchor.line
    text = ANCHOR_RE.sub("", text)
    text = re.sub(r"^(?:\s*>)*\s*", "", text)
    if anchor.heading:
        text = re.sub(r"^(?:Printed slide|Typed slides?|Slide|Handwritten page|Печатный слайд|Слайд|Слайды|"
                      r"Рукописная страница|Diapositiva impresa|Diapositivas?|Página manuscrita)[^.—]*(?:\.\s*|—\s*)", "", text)
        text = re.sub(r"\(PDF[^)]*\)|\((?:стр\.|pp\.)[^)]*\)", "", text)
        text = re.sub(r"§\d+\.\s*", "", text)
        words = "|".join(STATEMENT_WORDS[lang])
        text = re.sub(rf"\s*[—.]?\s*(?:{words})\s+{NUMBER}\s*", " ", text, flags=re.I).strip(" .—-")
        if text:
            return text
        text = anchor.line
    paren = re.match(r"\*\*[^*(]*\(([^)]*)\)\.?\*\*", re.sub(r"^(?:\s*>)*\s*", "", ANCHOR_RE.sub("", anchor.line)))
    if paren:
        return paren.group(1)
    body = re.sub(r"^\*\*[^*]*\*\*\s*", "", re.sub(r"^(?:\s*>)*\s*", "", ANCHOR_RE.sub("", anchor.line)))
    bold = re.findall(r"\*\*([^*]+)\*\*", body)
    if bold:
        return ", ".join(dict.fromkeys(b.strip(" .") for b in bold))
    return safe_truncate(re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", body), 90)


def safe_truncate(text: str, limit: int) -> str:
    """Cut at a space outside math so formulas are never broken."""
    if len(text) <= limit:
        return text
    spans = [(a, b) for a, b, _ in mdtext.inline_spans(text)]
    spaces = [k for k, ch in enumerate(text[:limit]) if ch == " " and not any(a <= k < b for a, b in spans)]
    cut = spaces[-1] if spaces else limit
    return text[:cut].rstrip(" ,;:") + " …"


def build_term_index(lang: str, notes, linker: Linker) -> str:
    t = INDEX_TEXT[lang]
    rel = f"{lang}/term-index.md"
    fake = Note(rel, "")
    rows_terms, rows_theorems = [], []
    for term in TERMS:
        number, _, frag = term.target.partition("#")
        chapter_rel = linker.chapters.get((lang, int(number)))
        course = ""
        if chapter_rel and frag in linker.anchors[chapter_rel]:
            label = f"{int(number)}" + (f".{frag.split('-')[-1]}" if frag.startswith("sec-") else "")
            course = f"[§{label}]({relpath(chapter_rel + '#' + frag, rel)})"
        lecture = ""
        if term.lec:
            fake.kind = "lecture"
            hit = linker.resolve_numbered(fake, term.lec)
            if hit:
                kind = next(k for k, p in KIND_PREFIX.items() if term.lec.startswith(p + "-"))
                num = ".".join(term.lec.split("-")[1:])
                lecture = f"[{KIND_NAMES[lang][kind]} {num}]({relpath(hit, rel)})"
        name = LABELS[term.id][lang]
        row = (name, course, lecture)
        (rows_theorems if term.kind == "theorem" else rows_terms).append(row)
    out = [
        "---", f'title: "{t["title"]}"', f"lang: {lang}", "generated: true", "---",
        f"# {t['title']}", "",
        f"[{UI[lang]['index']}](index.md) · [{UI[lang]['lecture_index']}](lectures-2025-26/index.md) · "
        f"[{ {'en': 'Glossary', 'ru': 'Глоссарий', 'es': 'Glosario'}[lang] }](glossary.md)", "",
        t["intro"], "",
    ]
    collator = lambda row: row[0].casefold().lstrip("ε-(").replace("ё", "е")
    for heading, rows in ((t["theorems"], rows_theorems), (t["terms"], rows_terms)):
        out += [f"## {heading}", "", f"| {t['cols'][0]} | {t['cols'][1]} | {t['cols'][2]} |", "|---|---|---|"]
        for name, course, lecture in sorted(rows, key=collator):
            out.append(f"| {mdtext_inline_math(name)} | {course or '—'} | {lecture or '—'} |")
        out.append("")
    out += [f"## {t['numbered']}", "", t["numbered_intro"], ""]
    table = linker.numbered.get((lang, "lecture"), {})
    register = linker.numbered.get((lang, "register"), {})
    by_chapter = defaultdict(list)
    for anchor_id_, anchor in table.items():
        parts = anchor_id_.split("-")
        by_chapter[int(parts[1])].append((tuple(int(x) for x in parts[1:]), parts[0], anchor))
    order = ["def", "thm", "lem", "cor", "prop", "rem"]
    for chapter in sorted(by_chapter):
        out += [f"### {t['chapter']} {chapter}", ""]
        cols = t["ncols"] + ((t["register"],) if register else ())
        out += ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
        for key, prefix, anchor in sorted(by_chapter[chapter], key=lambda e: (e[0], order.index(e[1]))):
            kind = next(k for k, p in KIND_PREFIX.items() if p == prefix)
            num = ".".join(str(x) for x in key)
            nums = lecture_numbers(anchor.note.rel.rsplit("/", 1)[-1])
            lec = "–".join(str(n) for n in (nums[0], nums[-1])) if len(nums) > 1 else str(nums[0])
            summary = statement_summary(anchor, lang).replace("|", "\\|")
            row = [f"[{KIND_NAMES[lang][kind]} {num}]({relpath(anchor.target, rel)})", summary,
                   f"[{lec}]({relpath(anchor.note.rel, rel)})"]
            if register:
                hit = register.get(anchor.id)
                row.append(f"[§{hit.note.rel.rsplit('-', 2)[-2]}.{hit.note.rel.rsplit('-', 1)[-1][:-3]}]"
                           f"({relpath(hit.target, rel)})" if hit else "—")
            out.append("| " + " | ".join(row) + " |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def mdtext_inline_math(text: str) -> str:
    return re.sub(r"L\^p", "$`L^p`$", text)


# --- step 6: the Obsidian vault --------------------------------------------

CALLOUT_TYPES = [
    (r"definition|определение|definición", "definition"),
    (r"lemma|лемма|lema", "lemma"),
    (r"corollary|следствие|corolario", "corollary"),
    (r"axiom|аксиома|axioma", "axiom"),
    (r"warning|предупреждение|advertencia|pitfall|ошибк", "warning"),
    (r"goal|цель|objetivo", "abstract"),
    (r"example|пример|ejemplo", "example"),
    (r"proof|доказательство|demostración", "proof"),
    (r"remark|замечание|observación|note|примечание|nota|пояснение|explicación|explanation", "remark"),
    (r"source|источник|fuente|опора|duplication|дублирование|duplicación|состав|порядок", "info"),
    (r"theorem|теорема|teorema|test|признак|criterio|criterion|критерий|principle|принцип|principio|"
     r"inequality|неравенство|desigualdad|rule|правило|regla|formula|формула|fórmula|property|свойство|"
     r"propiedad|архимедовость|density|плотность|densidad|part|часть|parte|identity|равенство|identidad|"
     r"proposition|утверждение|proposición", "theorem"),
]


def callout_type(label: str) -> str:
    for pattern, kind in CALLOUT_TYPES:
        if re.search(pattern, label, re.I):
            return kind
    return "note"


def github_slug(heading: str) -> str:
    text = re.sub(r"<[^>]+>", "", heading)
    text = re.sub(r"\$`([^`]*)`\$", r"\1", text)
    text = text.lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


class ObsidianBuilder:
    def __init__(self, notes: dict[str, Note]):
        self.notes = notes
        self.blocks: dict[str, dict[str, str]] = {}  # rel -> anchor -> "^id" or "#heading"
        self.slugs: dict[str, dict[str, str]] = {}
        for rel, note in notes.items():
            self.slugs[rel] = {}
            counts = defaultdict(int)
            for line in note.lines:
                heading = HEADING_RE.match(line)
                if heading and not line.startswith("#!"):
                    slug = github_slug(heading.group(2))
                    key = slug if not counts[slug] else f"{slug}-{counts[slug]}"
                    counts[slug] += 1
                    self.slugs[rel][key] = obsidian_heading(heading.group(2))
            self.blocks[rel] = {a: "^" + a for a in ANCHOR_RE.findall(note.text)}  # or "#Heading"

    def convert_structure(self, note: Note) -> tuple[str, str]:
        """Pass 1: math, callouts and block ids (records block-id aliases)."""
        front, body = mdtext.split_frontmatter(mdtext.to_dollar_math(note.text))
        if note.kind in ("lecture", "register") and note.lang:
            body = quote_statements(body, note.lang)
        return front, self.convert_blocks(self.convert_details(body), note)

    def convert_references(self, note: Note, front: str, body: str) -> str:
        """Pass 2: links, once every note's block ids are known."""
        return self.frontmatter(front, note) + self.convert_links(body, note)

    # Frontmatter: aliases and tags make notes findable from the quick switcher.
    def frontmatter(self, front: str, note: Note) -> str:
        if not front:
            return front
        extra = []
        title = title_of(front)
        alias = None
        name = note.rel.rsplit("/", 1)[-1]
        if note.kind == "lecture":
            nums = lecture_numbers(name)
            alias = (f"{UI[note.lang]['lecture'][0]} {nums[0]}" if len(nums) == 1
                     else f"{UI[note.lang]['lecture'][1]} {nums[0]}–{nums[-1]}") + f" ({note.lang})"
        elif note.kind == "chapter":
            alias = f"{title} ({note.lang})"
        elif note.kind == "ticket":
            alias = f"Билет {int(name[:2])}"
        if alias and "aliases:" not in front:
            extra.append(f"aliases: [{json.dumps(alias, ensure_ascii=False)}]")
        if "tags:" not in front and note.lang:
            extra.append(f"tags: [mathinmind/{note.lang}, mathinmind/{note.kind}]")
        if not extra:
            return front
        return front[: -len("---\n")] + "\n".join(extra) + "\n---\n"

    def convert_details(self, body: str) -> str:
        pattern = re.compile(r"(?ms)^<details>\s*\n<summary>(.*?)</summary>\s*\n(.*?)^</details>[ \t]*$")

        def repl(match):
            summary = re.sub(r"<[^>]+>", "", match.group(1)).strip()
            inner = match.group(2).strip("\n").split("\n")
            kind = "answer" if re.search(r"answer|ответ|respuesta|solution|решени|solución", summary, re.I) else "example"
            return "\n".join([f"> [!{kind}]- {summary}"] + [("> " + l).rstrip() for l in inner])
        return pattern.sub(repl, body)

    def convert_blocks(self, body: str, note: Note) -> str:
        lines = body.split("\n")
        out: list[str] = []
        pending_heading_anchor: list[str] = []
        i = 0
        in_fence = None
        while i < len(lines):
            line = lines[i]
            if in_fence:
                out.append(line)
                if mdtext.fence_closes(line, *in_fence):
                    in_fence = None
                i += 1
                continue
            anchor_line = ANCHOR_LINE_RE.match(line)
            if anchor_line:
                pending_heading_anchor.append(anchor_line.group(1))
                i += 1
                continue
            heading = HEADING_RE.match(line)
            if heading and pending_heading_anchor and re.fullmatch(r"[^$`\[\]|#^<>]+", heading.group(2)):
                # A plain heading is a stable Obsidian link target of its own.
                for anchor in pending_heading_anchor:
                    self.blocks[note.rel][anchor] = "#" + obsidian_heading(heading.group(2))
                pending_heading_anchor = []
            if heading or not line.strip():
                out.append(line)
                i += 1
                continue
            # A block: contiguous non-blank lines (fences and $$ math kept whole).
            j = i
            block = []
            fence = None
            dollars = False
            while j < len(lines):
                current = lines[j]
                if not fence and not dollars and not current.strip():
                    break
                if not fence and not dollars and j > i and (HEADING_RE.match(current) or ANCHOR_LINE_RE.match(current)):
                    break
                opened = mdtext.fence_open(current)
                if fence:
                    if mdtext.fence_closes(current, *fence):
                        fence = None
                elif opened:
                    fence = (opened[1], opened[2])
                elif re.sub(r"^(?:\s*>)*\s*(?:[-*+]\s+|\d+[.)]\s+)?", "", current).strip() == "$$":
                    dollars = not dollars
                block.append(current)
                j += 1
            ids = pending_heading_anchor + [a for l in block[:1] for a in ANCHOR_RE.findall(l)]
            pending_heading_anchor = []
            block = [ANCHOR_RE.sub("", l) for l in block]
            block = self.callout(block)
            out.extend(block)
            if ids:
                last = block[-1]
                plain_paragraph = not last.lstrip().startswith((">", "|", "-", "*", "+", "$$", "```", "~~~")) \
                    and not re.match(r"^\s*\d+[.)]\s", last) and not last.rstrip().endswith("$$")
                if plain_paragraph and len(ids) == 1:
                    out[-1] = last.rstrip() + f" ^{ids[0]}"
                else:
                    for anchor in ids[-1:]:
                        out += ["", f"^{anchor}"]
                    for anchor in ids[:-1]:
                        # Several anchors on one block: keep the first resolvable via the last id.
                        self.blocks[note.rel][anchor] = "^" + ids[-1]
            i = j
        return "\n".join(out)

    def callout(self, block: list[str]) -> list[str]:
        first = block[0]
        match = re.match(r"^> \*\*(.+?)\*\*\s*(.*)$", first)
        if not match or not first.startswith("> "):
            return block
        label = match.group(1).rstrip()
        if label.endswith((".", ":")):
            label = label[:-1]
        kind = callout_type(label)
        rest = match.group(2)
        result = [f"> [!{kind}] {label}"]
        if rest:
            result.append("> " + rest)
        return result + block[1:]

    def convert_links(self, body: str, note: Note) -> str:
        lines = body.split("\n")
        in_fence = None
        for k, line in enumerate(lines):
            opened = mdtext.fence_open(line)
            if in_fence:
                if mdtext.fence_closes(line, *in_fence):
                    in_fence = None
                continue
            if opened:
                in_fence = (opened[1], opened[2])
                continue
            table = mdtext.is_table_row(line)
            lines[k] = mdtext.LINK_SPAN_RE.sub(lambda m: self.wikilink(m.group(0), note, table), line)
        return "\n".join(lines)

    def wikilink(self, raw: str, note: Note, table: bool) -> str:
        if raw.startswith("[["):
            return raw
        match = re.match(r"^(!?)\[(.*)\]\((.*)\)$", raw, re.S)
        bang, label, dest = match.groups()
        dest = dest.strip()
        if dest.startswith("<") and ">" in dest:
            dest = dest[1:dest.index(">")]
        else:
            dest = dest.split(" ", 1)[0]
        if re.match(r"^[a-z]+:", dest):
            return raw
        path, _, frag = unquote(dest).partition("#")
        base = PurePosixPath(note.rel).parent
        target = os.path.normpath(str(base / path)) if path else note.rel
        target = target.replace(os.sep, "/")
        if target.startswith("..") or path.endswith("/"):
            outside = os.path.normpath(str(PurePosixPath("MathInMind") / target)).replace(os.sep, "/")
            kind = "tree" if path.endswith("/") or not Path(ROOT / outside).is_file() else "blob"
            url = f"{REPO_URL}/{kind}/main/{quote(outside)}" + (f"#{frag}" if frag else "")
            return f"{bang}[{label}]({url})"
        if bang or not target.endswith(".md"):
            return raw
        if "]]" in label or "|" in label and not table:
            return raw
        link = target[:-3]
        if frag:
            block = self.blocks.get(target, {}).get(frag)
            heading = self.slugs.get(target, {}).get(frag)
            if block:
                link += block if block.startswith("#") else "#" + block
            elif heading:
                link += "#" + heading
        if target == note.rel and frag:
            link = link[len(target) - 3:]
        separator = "\\|" if table else "|"
        label = label.replace("|", "\\|") if table else label
        return f"[[{link}{separator}{label}]]"


def quote_statements(body: str, lang: str) -> str:
    """Wrap each numbered statement paragraph, with the formulas and lists that
    directly continue it, in a blockquote so that it becomes a callout."""
    lines = body.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        starts = (not out or not out[-1].strip()) and any(True for _ in leading_labels(line, lang)) \
            and not line.startswith(">") and any(True for _ in statement_sites(line, lang))
        if not starts:
            out.append(line)
            i += 1
            continue
        j = _block_end(lines, i)
        statement = lines[i:j]
        while j < len(lines):
            k = j
            while k < len(lines) and not lines[k].strip():
                k += 1
            if k >= len(lines):
                break
            head = lines[k].lstrip()
            if not (head.startswith("$$") or re.match(r"(?:[-*+]|\d+[.)])\s", head)):
                break
            end = _block_end(lines, k)
            statement += [""] * (k - j) + lines[k:end]
            j = end
        out.extend(("> " + l).rstrip() if l.strip() else ">" for l in statement)
        i = j
    return "\n".join(out)


def _block_end(lines: list[str], start: int) -> int:
    """Index after the contiguous block that starts at `start` ($$ math kept whole)."""
    j, dollars = start, False
    while j < len(lines):
        if not dollars and not lines[j].strip():
            break
        if re.sub(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)?", "", lines[j]).strip() == "$$":
            dollars = not dollars
        j += 1
    return j


def obsidian_heading(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\$`([^`]*)`\$", r"$\1$", text)
    return re.sub(r"\s+", " ", re.sub(r"[\[\]|#^]", " ", text)).strip()


OBSIDIAN_CSS = """/* MathInMind callouts: definitions, theorems and proofs at a glance. */
.callout[data-callout="definition"] { --callout-color: 46, 125, 230; --callout-icon: lucide-book-open; }
.callout[data-callout="theorem"] { --callout-color: 124, 77, 255; --callout-icon: lucide-sigma; }
.callout[data-callout="lemma"] { --callout-color: 0, 150, 136; --callout-icon: lucide-puzzle; }
.callout[data-callout="corollary"] { --callout-color: 0, 172, 193; --callout-icon: lucide-git-branch; }
.callout[data-callout="proposition"] { --callout-color: 94, 53, 177; --callout-icon: lucide-sigma; }
.callout[data-callout="axiom"] { --callout-color: 216, 67, 21; --callout-icon: lucide-anchor; }
.callout[data-callout="proof"] { --callout-color: 120, 144, 156; --callout-icon: lucide-check-square; }
.callout[data-callout="remark"] { --callout-color: 141, 110, 99; --callout-icon: lucide-message-square; }
.callout[data-callout="answer"] { --callout-color: 67, 160, 71; --callout-icon: lucide-check-circle; }
"""

OBSIDIAN_README_NOTE = ("> [!info] Generated vault\n> This Obsidian view is generated from "
                        "[`MathInMind/`]({repo}/tree/main/MathInMind) by `python3 scripts/build_views.py`. "
                        "Edit the source there; changes made here are overwritten.\n")


def build_obsidian(notes: dict[str, Note]) -> dict[str, bytes]:
    builder = ObsidianBuilder(notes)
    files: dict[str, bytes] = {}
    structured = {rel: builder.convert_structure(note) for rel, note in notes.items()}
    for rel, note in notes.items():
        text = builder.convert_references(note, *structured[rel])
        if rel == "README.md":
            text = re.sub(r"(?m)^(# .*\n)", lambda m: m.group(1) + "\n" + OBSIDIAN_README_NOTE.format(repo=REPO_URL),
                          text, count=1)
        files[rel] = text.encode("utf-8")
    files[".obsidian/snippets/mathinmind-callouts.css"] = OBSIDIAN_CSS.encode()
    files[".obsidian/appearance.json"] = (json.dumps({"enabledCssSnippets": ["mathinmind-callouts"]}, indent=2) + "\n").encode()
    files[".obsidian/app.json"] = (json.dumps({"useMarkdownLinks": False, "newLinkFormat": "absolute",
                                               "showFrontmatter": False, "alwaysUpdateLinks": True}, indent=2) + "\n").encode()
    for path in VAULT.rglob("*"):
        if path.is_file() and path.suffix != ".md":
            files[path.relative_to(VAULT).as_posix()] = path.read_bytes()
    return files


# --- driver -----------------------------------------------------------------

def build() -> tuple[dict[str, str], dict[str, bytes], Linker]:
    notes = {p.relative_to(VAULT).as_posix(): Note(p.relative_to(VAULT).as_posix(), p.read_text(encoding="utf-8"))
             for p in sorted(VAULT.rglob("*.md"))}
    for lang in LANGS:
        notes.setdefault(f"{lang}/term-index.md", Note(f"{lang}/term-index.md", ""))
    for note in notes.values():
        note.text = mdtext.to_github_math(note.text)
        add_anchors(note)
    for note in notes.values():
        rewrite_navigation(note, notes)
    anchors = catalogue(notes)
    linker = Linker(notes, anchors)
    for note in notes.values():
        linker.link_note(note)
    for lang in LANGS:
        link_glossary(notes[f"{lang}/glossary.md"], linker)
        notes[f"{lang}/term-index.md"].text = build_term_index(lang, notes, linker)
    github = {rel: note.text for rel, note in notes.items()}
    obsidian = build_obsidian(notes)
    return github, obsidian, linker


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true", help="only report whether the views are up to date")
    args = parser.parse_args()
    github, obsidian, linker = build()
    stale = []
    for rel, text in github.items():
        path = VAULT / rel
        if not path.is_file() or path.read_text(encoding="utf-8") != text:
            stale.append(f"MathInMind/{rel}")
            if not args.check:
                path.write_text(text, encoding="utf-8")
    keep = {".obsidian/workspace.json", ".obsidian/workspace-mobile.json"}
    for rel, data in obsidian.items():
        path = OBSIDIAN / rel
        if not path.is_file() or path.read_bytes() != data:
            stale.append(f"MathInMind-Obsidian/{rel}")
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
    if OBSIDIAN.is_dir():
        for path in sorted(OBSIDIAN.rglob("*")):
            rel = path.relative_to(OBSIDIAN).as_posix()
            if path.is_file() and rel not in obsidian and rel not in keep and not rel.startswith(".trash/"):
                stale.append(f"MathInMind-Obsidian/{rel} (obsolete)")
                if not args.check:
                    path.unlink()
    if args.check:
        if stale:
            print(f"{len(stale)} generated file(s) are stale; run python3 scripts/build_views.py", file=sys.stderr)
            for item in stale[:20]:
                print(f"  - {item}", file=sys.stderr)
            return 1
        print("GitHub and Obsidian views are up to date.")
        return 0
    print(f"Updated {len(stale)} file(s).")
    print("  links: " + ", ".join(f"{k}={v}" for k, v in sorted(linker.stats.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
