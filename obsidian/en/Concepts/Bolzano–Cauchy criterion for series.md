---
id: cauchy-criterion-series
type: theorem
semester: 3
lang: en
aliases: []
tags: [analysis/series, sem3, theorem]
source_pages: [p021]
translations: ["[[ru/Понятия/Критерий Больцано–Коши для рядов]]", "[[es/Conceptos/Criterio de Bolzano–Cauchy para series]]"]
status: draft
---

# Bolzano–Cauchy criterion for series

> [!theorem] Bolzano–Cauchy criterion
> The series $\sum_{n=1}^{\infty}a_n$ converges if and only if
> $$\forall\varepsilon>0\ \exists N\in\mathbb{N}\ \forall n>N\ \forall p>0:\ \left|\sum_{k=n+1}^{n+p}a_k\right|<\varepsilon.$$

> [!proof]- Proof as written in the notes
> By definition convergence of the series is equivalent to the existence of a finite limit of $S_m=\sum_{n=1}^{m}a_n$; the Bolzano–Cauchy criterion is applied to $\{S_m\}$. Without loss of generality $m>n$, and with $p:=m-n$ one gets $S_m-S_n=\sum_{k=n+1}^{m}a_k$. $\blacksquare$

## Related

- [[Properties of convergent series]]
- [[Absolute convergence]]

> [!warning] Open markers: ⟦T078⟧, ⟦T080⟧, ⟦U079⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Критерий Больцано–Коши для рядов — `ru/Понятия/Критерий Больцано–Коши для рядов.md`
- es: Criterio de Bolzano–Cauchy para series — `es/Conceptos/Criterio de Bolzano–Cauchy para series.md`
