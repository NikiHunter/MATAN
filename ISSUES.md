# Issues

Repository-wide issue log. The semester-3 transcription has its own tables: [`ocr/ISSUES.md`](ocr/ISSUES.md)
(open) and [`ocr/RESOLVED.md`](ocr/RESOLVED.md) (decided). What is left to build is in [`GOALS.md`](GOALS.md).

## Open — course chapters 01–21

Found by the audit of 2 November 2026; not fixed yet. Line numbers refer to the Russian file; the English and
Spanish files have the same defect at the same place unless noted.

| File | Line | Type | Problem | Fix |
|---|---|---|---|---|
| `MathInMind/*/01-logic-sets-functions.md` | 90 | MATH | «счётно» defined as «конечно или равномощно ℕ», contradicting lectures 1–3 (Опр 1.2.5, 1.2.6) | счётно = равномощно ℕ; add «не более чем счётно» = конечно или счётно |
| `MathInMind/*/02-real-numbers.md` | 65 | MATH | Archimedean proof: «целое $n$ с $s-1<n<s$» | «натуральное $n$ с $s-1<n\le s$», then $n+1>s$ |
| `MathInMind/*/03-sequences.md` | — | GAP | the only chapter without a worked example | add `## Разобранный пример` |
| `MathInMind/*/09-improper-integrals-applications.md` | 47 | MATH | Dirichlet test stated vaguely («с подходящей регулярностью»); Abel's test missing although the term registry links «признак Абеля» here | precise Dirichlet and Abel tests |
| `MathInMind/*/10-function-sequences-series.md` | 78 | STYLE | theorem on differentiating a limit is an unlabelled blockquote (no anchor, no callout) | label it; add `uniform-limit-differentiation` to `CHAPTER_STATEMENTS[10]` |
| `MathInMind/*/16-implicit-functions-extrema.md` | 32 | STYLE | inverse function theorem labelled just «Теорема» | «Теорема об обратной функции» |
| `MathInMind/*/21-lp-spaces.md` | 2, 66 | TYPO | plain «Lp», «L2» in the title and a heading (propagates to nav bars) | $L^p$, $L^2$ |
| `MathInMind/*/formula-sheet.md` | 126 | TYPO | plain «Lp» | $L^p$ |
| `MathInMind/ru/17-multiple-integrals.md` | 76, 78 | STYLE | `\operatorname{area}`, `\operatorname{vol}` in Russian text | $S(D)$, $V(\Omega)$ |
| `MathInMind/ru/18-vector-calculus.md` | 93 | STYLE | `\operatorname{area}` | $S(D)$ |
| `MathInMind/ru/09-improper-integrals-applications.md` | 100 | STYLE | `\mathrm{avg}` | $\bar f$ |
| `MathInMind/*/09…`, `10…`, `12…` | 68, 78, 66 | LINK | «непрерывно дифференцируем…» in one-variable chapters links to `15-multivariable-differentiation.md#sec-15-1` | unlink; restrict the term `continuously-differentiable` to chapters 13–21 |
| `MathInMind/*/06-derivatives.md`, `09-…` | 97, 30 | LINK | «внутренней точке» links to the metric-space chapter | unlink or restrict the term |

## Fixed in this pass (2 November 2026)

| File | Type | Was | Fix |
|---|---|---|---|
| `MathInMind/ru/exam/tickets/69.md` | MATH | ticket «лемма о двойном приращении» answered Lemma 6.3.1 | answers Lemma 6.4.3; listed under §6.4 in `exam/index.md` |
| `MathInMind/*/lectures-2025-26/lecture-61-62.md`, `lecture-63-64.md` | STYLE | no navigation bar | nav bars added |
| `MathInMind/ru/lectures-2025-26/lecture-61-62.md` (136, 140, 318, 326), `lecture-51-52.md` (179) | TYPO | English `\text{for all}`, `\text{and}`, `\text{or}`, `\text{otherwise}` | Russian words |
| `MathInMind/*/lectures-2025-26/*.md` | STYLE | `course:` frontmatter inconsistent (three EN and three ES files had the Russian value) | normalised per language |
| `MathInMind/{en,es}/lectures-2025-26/lecture-63-64.md` | LINK | «Continuous…» statements lost their anchors (`thm-6-3-1`) because the build skipped labels containing «continu» | build fixed; anchors restored |
| `ocr/ISSUES.md` | STYLE | 503 rows without a header (not a rendered table), unescaped pipes | real table; decided rows moved to `ocr/RESOLVED.md` |
| semester-3 transcription | OCR | 503 open issues; about 40 unflagged errors (e.g. Cauchy–Hadamard with `lim`, Lebesgue criterion «интегрируема почти всюду», swapped limits in Th 9.2.3, $R=\infty$ for $\sum x^{2n}$) | all 542 decided (503 + 39 newly found), see `ocr/RESOLVED.md`; corrections are marked «Поправка к источнику» in lectures 65–84 |
| `ocr/MANIFEST.md` | SECURITY | archive password in plain text | removed (it remains in git history) |
