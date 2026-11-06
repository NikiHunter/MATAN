# Issues

Repository-wide issue log. The semester-3 transcription has its own tables: [`ocr/ISSUES.md`](ocr/ISSUES.md)
(open) and [`ocr/RESOLVED.md`](ocr/RESOLVED.md) (decided). What is left to build is in [`GOALS.md`](GOALS.md).

## Open — course chapters 01–21

None at present: the rows found by the audit of 2 November 2026 were fixed in the G5 pass below.

## Fixed in the G5 audit (6 November 2026)

All fixes are in the Russian, English and Spanish files unless the row names one language.

| File | Type | Was | Fix |
|---|---|---|---|
| `MathInMind/*/01-logic-sets-functions.md` | MATH | «счётно» defined as «конечно или равномощно ℕ» | счётно = равномощно ℕ; «не более чем счётно» = конечно или счётно (Опр 1.2.5, 1.2.6) |
| `MathInMind/*/02-real-numbers.md` | MATH | Archimedean proof used «целое $n$ с $s-1<n<s$» | natural $n$ with $s-1<n\le s$ ($s-1$ is not an upper bound), then $n+1>s$ |
| `MathInMind/*/03-sequences.md` | GAP | no worked example | `## Разобранный пример`: $\sqrt{n^2+n}-n\to\frac12$ with an $\varepsilon$–$N$ check; divergence of $(-1)^n\frac{n}{n+1}$ via subsequences |
| `MathInMind/*/09-improper-integrals-applications.md` | MATH | Dirichlet test «с подходящей регулярностью», no Abel test | precise Dirichlet and Abel tests ($f\in C$, $g\in C^1$ monotone, as Th 4.5.4) with the proof by parts and the reduction of Abel to Dirichlet |
| `MathInMind/*/10-function-sequences-series.md` | STYLE | differentiation theorem was an unlabelled blockquote | labelled «Теорема о дифференцировании»; anchor `uniform-limit-differentiation` in `CHAPTER_STATEMENTS[10]` |
| `MathInMind/*/16-implicit-functions-extrema.md` | STYLE | inverse function theorem labelled «Теорема» | «Теорема об обратной функции» |
| `MathInMind/*/21-lp-spaces.md` | TYPO | plain «Lp», «L2» in the title and §21.4 | title «Lᵖ» (plain text, it feeds the nav bars and Obsidian aliases); heading $L^2$ |
| `MathInMind/*/formula-sheet.md` | TYPO | plain «Lp» in a heading | $L^p$ |
| `MathInMind/ru/17-multiple-integrals.md`, `ru/18-vector-calculus.md`, `ru/09-improper-integrals-applications.md` | STYLE | `\operatorname{area}`, `\operatorname{vol}`, `\mathrm{avg}` in Russian text | $S(D)$, $V(\Omega)$, $\bar f$ |
| `MathInMind/*/09…`, `10…`, `12…`, `es/00-notation.md`, `*/lectures-2025-26/lecture-27-28.md`, `ru/exam-sem3/tickets/39.md`, `ru/exam-sem3/EXAM_SEM3.md` | LINK | one-variable «непрерывно дифференцируем…» linked to the multivariable notion (§15.1, Th 6.3.1) | unlinked (reworded in the exam master); term `continuously-differentiable` restricted to chapters 13–21 |
| `MathInMind/*/06-derivatives.md`, `09-…` | LINK | «внутренней точке» of an interval linked to the metric-space chapter | unlinked; term `interior` restricted to chapters 13–21 |

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
