"""Low-level Markdown helpers shared by the view builder and the validators.

The course is stored once, in ``MathInMind/``, in the GitHub-safe dialect:

* inline mathematics is written ``$`...`$`` and display mathematics as a
  ```` ```math ```` fence, because GitHub's Markdown pass otherwise eats
  ``\\{``, ``\\|``, ``\\,``, ``*`` and ``<b>``-like text inside ``$...$``;
  inside list items, where GitHub shows math fences as code, a display
  formula becomes a line ``$`\\displaystyle ...`$``;
* definitions and theorems carry ``<a id="..."></a>`` anchors.

``to_dollar_math`` converts back to the ``$...$`` / ``$$`` dialect that
Obsidian's MathJax renderer expects.  Everything here is dependency-free.
"""

from __future__ import annotations

import re

FENCE_RE = re.compile(r"^(?P<prefix>(?:[ \t]*>)*[ \t]*(?:(?:[-*+]|\d+[.)])[ \t]+)?)(?P<fence>`{3,}|~{3,})(?P<info>.*)$")
PREFIX_RE = re.compile(r"^(?P<quote>(?:[ \t]*>[ \t]?)*)(?P<indent>[ \t]*)(?P<marker>(?:[-*+]|\d+[.)])[ \t]+)?")
PUNCTUATION_ONLY = re.compile(r"^[\s.,;:!?)]*$")


def split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter including both --- lines, body)."""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[: end + 5], text[end + 5 :]
    return "", text


def fence_open(line: str):
    """Return (prefix, char, length, info) for a fence opener, else None."""
    match = FENCE_RE.match(line)
    if not match:
        return None
    fence = match.group("fence")
    if fence[0] == "`" and "`" in match.group("info"):
        return None
    return match.group("prefix"), fence[0], len(fence), match.group("info").strip()


def fence_closes(line: str, char: str, length: int) -> bool:
    match = FENCE_RE.match(line)
    return bool(match and match.group("fence")[0] == char
                and len(match.group("fence")) >= length and not match.group("info").strip())


# --- inline scanning -------------------------------------------------------

def inline_spans(line: str) -> list[tuple[int, int, str]]:
    """Spans of inline code, GitHub math ($`..`$) and dollar math ($..$, $$..$$).

    Kinds: 'code', 'gmath', 'math', 'dmath'.  Unclosed delimiters are ignored.
    """
    spans = []
    i, n = 0, len(line)
    while i < n:
        ch = line[i]
        if ch == "\\":
            i += 2
            continue
        if ch == "$" and line.startswith("$`", i):
            end = line.find("`$", i + 2)
            if end != -1:
                spans.append((i, end + 2, "gmath"))
                i = end + 2
                continue
        if ch == "`":
            run = len(line[i:]) - len(line[i:].lstrip("`"))
            end = line.find("`" * run, i + run)
            while end != -1 and line.startswith("`", end + run):
                end = line.find("`" * run, end + run + 1)
            if end != -1:
                spans.append((i, end + run, "code"))
                i = end + run
                continue
            i += run
            continue
        if ch == "$":
            if line.startswith("$$", i):
                end = _find_unescaped(line, "$$", i + 2)
                if end != -1:
                    spans.append((i, end + 2, "dmath"))
                    i = end + 2
                    continue
                i += 2
                continue
            end = _find_unescaped(line, "$", i + 1)
            if end != -1 and end > i + 1:
                spans.append((i, end + 1, "math"))
                i = end + 1
                continue
        i += 1
    return spans


def _find_unescaped(line: str, token: str, start: int) -> int:
    pos = line.find(token, start)
    while pos != -1 and _escaped(line, pos):
        pos = line.find(token, pos + 1)
    return pos


def _escaped(line: str, pos: int) -> bool:
    slashes = 0
    while pos - slashes - 1 >= 0 and line[pos - slashes - 1] == "\\":
        slashes += 1
    return slashes % 2 == 1


def find_display_delimiter(line: str, start: int = 0) -> int:
    """Position of an unescaped '$$' outside inline code / GitHub math, or -1."""
    protected = [(a, b) for a, b, kind in inline_spans(line) if kind in ("code", "gmath")]
    pos = _find_unescaped(line, "$$", start)
    while pos != -1 and any(a <= pos < b for a, b in protected):
        pos = _find_unescaped(line, "$$", pos + 2)
    return pos


def is_table_row(line: str) -> bool:
    stripped = re.sub(r"^(?:\s*>)*\s*", "", line)
    return stripped.startswith("|") and stripped.rstrip().endswith("|")


def table_safe_math(content: str) -> str:
    """Pipes split GFM and Obsidian table cells even inside math."""
    content = content.replace("\\|", "\\Vert ")
    return re.sub(r"(?<!\\)\|", r"\\vert ", content).replace("  ", " ")


# --- dollar math -> GitHub math --------------------------------------------

def _convert_inline_dollars(line: str) -> str:
    table = is_table_row(line)
    image_ranges = [m.span() for m in re.finditer(r"!\[[^\]\n]*\]\([^)\n]*\)", line)]
    out, last = [], 0
    for start, end, kind in inline_spans(line):
        if kind != "math" or any(a <= start < b for a, b in image_ranges):
            if kind == "gmath" and table:
                inner = line[start + 2 : end - 2]
                safe = table_safe_math(inner)
                if safe != inner:
                    out.append(line[last:start])
                    out.append("$`" + safe + "`$")
                    last = end
            continue
        inner = line[start + 1 : end - 1]
        if "`" in inner:
            continue
        if table:
            inner = table_safe_math(inner)
        out.append(line[last:start])
        out.append("$`" + inner.strip() + "`$")
        last = end
    out.append(line[last:])
    return "".join(out)


def _prefixes(line: str) -> tuple[str, str, int, int]:
    """(first-line prefix, continuation prefix, quote depth, indent width)."""
    match = PREFIX_RE.match(line)
    quote = match.group("quote") or ""
    depth = quote.count(">")
    indent = match.group("indent") or ""
    marker = match.group("marker") or ""
    first = match.group(0)
    cont = "> " * depth + indent + " " * len(marker)
    return first, cont, depth, len(indent) + len(marker)


def _strip_continuation(line: str, depth: int, width: int) -> str:
    for _ in range(depth):
        line = re.sub(r"^[ \t]*>[ \t]?", "", line, count=1)
    return re.sub(r"^ {0,%d}" % width, "", line)


def to_github_math(text: str) -> str:
    """Convert ``$..$`` and ``$$..$$`` to GitHub-safe math. Idempotent."""
    front, body = split_frontmatter(text)
    lines = body.split("\n")
    out: list[str] = []
    fence = None
    i = 0
    while i < len(lines):
        line = lines[i]
        if fence:
            out.append(line)
            if fence_closes(line, fence[0], fence[1]):
                fence = None
            i += 1
            continue
        opened = fence_open(line)
        if opened:
            fence = (opened[1], opened[2])
            out.append(line)
            i += 1
            continue
        pos = find_display_delimiter(line)
        if pos == -1:
            out.append(_convert_inline_dollars(line))
            i += 1
            continue
        first, cont, depth, width = _prefixes(line)
        if pos < len(first):  # '$$' found inside the prefix area: impossible, guard
            first, cont = line[:pos], line[:pos]
        before = line[len(first):pos]
        rest = line[pos + 2 :]
        close = find_display_delimiter(rest)
        content: list[str] = []
        after = ""
        consumed = i + 1
        if close != -1:
            content = [rest[:close]]
            after = rest[close + 2 :]
        else:
            content = [rest]
            j = i + 1
            found = False
            while j < len(lines):
                inner = _strip_continuation(lines[j], depth, width)
                c = find_display_delimiter(inner)
                if c == -1:
                    content.append(inner)
                    j += 1
                    continue
                content.append(inner[:c])
                after = inner[c + 2 :]
                found = True
                break
            if not found:  # unterminated: leave untouched for the validator
                out.append(line)
                i += 1
                continue
            consumed = j + 1
        if after.strip() and PUNCTUATION_ONLY.match(after):
            content[-1] = content[-1].rstrip() + after.strip()
            after = ""
        while content and not content[0].strip():
            content.pop(0)
        while content and not content[-1].strip():
            content.pop()
        in_list = bool(PREFIX_RE.match(line).group("marker")) or width > 0
        if in_list and not any("`" in c for c in content) and find_display_delimiter(after) == -1:
            # Inside list items GitHub shows math fences as code; keep the formula
            # inline at display size, on a line of its own.
            formula = "$`\\displaystyle " + " ".join(c.strip() for c in content if c.strip()) + "`$"
            if before.strip():
                out.append(_convert_inline_dollars(first + before.rstrip()))
                out.append(cont.rstrip())
                out.append(cont + formula + after.rstrip())
            else:
                if not PREFIX_RE.match(line).group("marker") and out and out[-1].strip(" >"):
                    out.append(cont.rstrip())
                out.append(first + formula + after.rstrip())
            i = consumed
            continue
        lead = first
        if before.strip():
            out.append(_convert_inline_dollars(first + before.rstrip()))
            lead = cont
        out.append(lead + "```math")
        out.extend((cont + c.rstrip()).rstrip() if c.strip() else cont.rstrip() for c in content)
        out.append(cont + "```")
        if after.strip():
            lines[consumed - 1 : consumed] = [cont + after.lstrip()]
            i = consumed - 1
        else:
            i = consumed
    return front + "\n".join(out)


# --- GitHub math -> dollar math --------------------------------------------

def to_dollar_math(text: str) -> str:
    """Convert GitHub math to the ``$..$`` / ``$$`` form used by Obsidian."""
    front, body = split_frontmatter(text)
    out = []
    fence = None
    math_fence = None
    for line in body.split("\n"):
        if math_fence:
            if fence_closes(line, "`", math_fence):
                out.append(FENCE_RE.match(line).group("prefix") + "$$")
                math_fence = None
            else:
                out.append(line)
            continue
        if fence:
            out.append(line)
            if fence_closes(line, fence[0], fence[1]):
                fence = None
            continue
        opened = fence_open(line)
        if opened:
            if opened[1] == "`" and opened[3] == "math":
                out.append(opened[0] + "$$")
                math_fence = opened[2]
                continue
            fence = (opened[1], opened[2])
            out.append(line)
            continue
        out.append(_gmath_to_dollars(line))
    return front + "\n".join(out)


DISPLAYSTYLE_LINE = re.compile(r"^(?P<prefix>(?:[ \t]*>)*[ \t]*(?:(?:[-*+]|\d+[.)])[ \t]+)?)"
                               r"\$`\\displaystyle (?P<math>[^`]*)`\$(?P<tail>[.,;:]?)[ \t]*$")


def _gmath_to_dollars(line: str) -> str:
    alone = DISPLAYSTYLE_LINE.match(line)
    if alone:  # a list-item display formula (see to_github_math)
        return f"{alone.group('prefix')}$${alone.group('math').strip()}{alone.group('tail')}$$"
    out, last = [], 0
    for start, end, kind in inline_spans(line):
        if kind != "gmath":
            continue
        out.append(line[last:start])
        out.append("$" + line[start + 2 : end - 2].strip() + "$")
        last = end
    out.append(line[last:])
    return "".join(out)


# --- protected regions for automatic linking -------------------------------

LINK_SPAN_RE = re.compile(r"!?\[(?:[^\[\]\n]|\[[^\[\]\n]*\])*\]\([^)\n]*\)|\[\[[^\]\n]*\]\]")
HTML_RE = re.compile(r"</?[A-Za-z][^<>\n]*>")
BOLD_RE = re.compile(r"\*\*[^*\n]+?\*\*|__[^_\n]+?__")
URL_RE = re.compile(r"https?://\S+")


def protected_mask(line: str, protect_bold: bool = True) -> list[bool]:
    """True for characters that automatic linking must not touch."""
    mask = [False] * len(line)
    masked = list(line)
    for start, end, _ in inline_spans(line):
        for k in range(start, end):
            mask[k] = True
            masked[k] = "X"
    flat = "".join(masked)
    patterns = [LINK_SPAN_RE, HTML_RE, URL_RE] + ([BOLD_RE] if protect_bold else [])
    for pattern in patterns:
        for match in pattern.finditer(flat):
            for k in range(*match.span()):
                mask[k] = True
    quote = re.match(r"^(?:\s*>)*\s*", line).end()
    for k in range(quote):
        mask[k] = True
    return mask
