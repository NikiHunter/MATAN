import re
import unittest
from pathlib import Path

import build_views
import mdtext


def without_inline_code(text: str) -> str:
    lines = []
    for line in text.split("\n"):
        for start, end, kind in reversed(mdtext.inline_spans(line)):
            if kind == "code":
                line = line[:start] + line[end:]
        lines.append(line)
    return "\n".join(lines)


class MathConversionTests(unittest.TestCase):
    def test_inline_math_is_protected_from_github_markdown(self):
        source = r"Let $\{x_n\}$ and $a<b>c$, but keep `$x$` and ![alt $x$](a.png)."
        expected = r"Let $`\{x_n\}`$ and $`a<b>c`$, but keep `$x$` and ![alt $x$](a.png)."
        self.assertEqual(mdtext.to_github_math(source), expected)

    def test_display_math_becomes_math_fence_in_blockquote(self):
        source = "> **Theorem.** If\n> $$\n> a\\|x\\|\n> $$\n> holds."
        expected = "> **Theorem.** If\n> ```math\n> a\\|x\\|\n> ```\n> holds."
        self.assertEqual(mdtext.to_github_math(source), expected)

    def test_display_math_in_list_items_stays_inline_at_display_size(self):
        # GitHub shows a math fence inside a list item as a code block.
        self.assertEqual(mdtext.to_github_math("2. Then\n   $$\n   x=1\n   $$\n"),
                         "2. Then\n\n   $`\\displaystyle x=1`$\n")
        self.assertEqual(mdtext.to_github_math("1. $$d(fg)=g\\,df;$$"), "1. $`\\displaystyle d(fg)=g\\,df;`$")
        self.assertEqual(mdtext.to_dollar_math("1. $`\\displaystyle d(fg)`$."), "1. $$d(fg).$$")

    def test_single_line_display_keeps_trailing_punctuation_inside(self):
        self.assertEqual(mdtext.to_github_math("$$x=1$$."), "```math\nx=1.\n```")

    def test_pipes_inside_table_math_do_not_split_cells(self):
        row = mdtext.to_github_math(r"| $f=O(g)$ | $|f|\le C\|g\|$ |")
        self.assertEqual(row.count("|") - row.count(r"\|"), 3)
        self.assertIn(r"\vert f\vert", row)
        self.assertIn(r"\Vert g\Vert", row)

    def test_conversion_is_idempotent_and_reversible(self):
        source = "Text $x_n$.\n\n$$\n\\sum a_n\n$$\n\n> $$y$$\n"
        github = mdtext.to_github_math(source)
        self.assertEqual(mdtext.to_github_math(github), github)
        self.assertEqual(mdtext.to_dollar_math(github), "Text $x_n$.\n\n$$\n\\sum a_n\n$$\n\n> $$\n> y\n> $$\n")

    def test_code_fences_are_untouched(self):
        source = "```python\nprice = '$5 and $6'\n```"
        self.assertEqual(mdtext.to_github_math(source), source)


class StatementTests(unittest.TestCase):
    def test_statement_sites_skip_proofs_and_continuations(self):
        sites = lambda line, lang="en": list(build_views.statement_sites(line, lang))
        self.assertEqual(sites("**Theorem 2.3.5.** Let"), [("theorem", "2.3.5")])
        self.assertEqual(sites("**Definition 4.6.4.** **Definition 4.6.5.**"),
                         [("definition", "4.6.4"), ("definition", "4.6.5")])
        self.assertEqual(sites("## Printed slide 6 (PDF p. 6). Derivative — Theorem 6.1.1"), [("theorem", "6.1.1")])
        self.assertEqual(sites("### Proof of Theorem 2.3.5"), [])
        self.assertEqual(sites("**Proof (Theorem 2.3.5).**"), [])
        self.assertEqual(sites("**Теорема 2.2.2 (продолжение).**", "ru"), [])

    def test_inflected_references_are_recognised(self):
        match = build_views.REFERENCE_RE["ru"].search("по теореме 2.3.5 и 2.3.6")
        self.assertEqual(build_views.reference_kind("ru", match.group("word")), "theorem")
        self.assertIn("2.3.6", match.group("more"))

    def test_summaries_never_cut_through_a_formula(self):
        text = "Let $`\\{x_n\\}`$ be real sequences and $`a, b \\in \\mathbb{R} \\cup \\{\\infty\\}`$ here."
        cut = build_views.safe_truncate(text, 70)
        self.assertEqual(cut.count("$`"), cut.count("`$"))


class GeneratedViewsTests(unittest.TestCase):
    """The committed views must match a fresh build, and every wikilink must resolve."""

    @classmethod
    def setUpClass(cls):
        cls.github, cls.obsidian, _ = build_views.build()

    def test_github_view_is_up_to_date(self):
        stale = [rel for rel, text in self.github.items()
                 if (build_views.VAULT / rel).read_text(encoding="utf-8") != text]
        self.assertEqual(stale, [], "run python3 scripts/build_views.py")

    def test_obsidian_wikilinks_resolve(self):
        notes = {rel[:-3]: data.decode("utf-8") for rel, data in self.obsidian.items() if rel.endswith(".md")}
        blocks = {k: set(re.findall(r"(?:^|\s)\^([A-Za-z0-9-]+)\s*$", t, re.M)) for k, t in notes.items()}
        headings = {k: {build_views.obsidian_heading(h) for h in re.findall(r"(?m)^#{1,6} (.*)$", t)}
                    for k, t in notes.items()}
        broken = []
        for name, text in notes.items():
            text = without_inline_code(text)
            for match in re.finditer(r"(?<!!)\[\[([^\]|\\]+?)(?:\\?\|[^\]]*)?\]\]", text):
                path, _, frag = match.group(1).partition("#")
                path = path or name
                ok = path in notes and (not frag or (frag[1:] in blocks[path] if frag.startswith("^")
                                                     else frag in headings[path]))
                if not ok:
                    broken.append(f"{name}: [[{match.group(1)}]]")
        self.assertEqual(broken, [])

    def test_obsidian_view_has_no_github_only_syntax(self):
        for rel, data in self.obsidian.items():
            if rel.endswith(".md"):
                text = without_inline_code(data.decode("utf-8"))
                self.assertNotIn("```math", text, rel)
                self.assertNotRegex(text, r'<a id="', rel)

    def test_every_registered_term_is_reachable(self):
        index = (build_views.VAULT / "en/term-index.md").read_text(encoding="utf-8").replace("$`L^p`$", "L^p")
        for term in build_views.TERMS:
            self.assertIn(build_views.LABELS[term.id]["en"], index, term.id)


if __name__ == "__main__":
    unittest.main()
