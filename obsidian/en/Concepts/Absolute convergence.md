---
id: absolute-convergence
type: definition
semester: 3
lang: en
aliases: []
tags: [analysis/series, sem3, definition]
source_pages: [p021]
translations: ["[[ru/Понятия/Абсолютная сходимость]]", "[[es/Conceptos/Convergencia absoluta]]"]
status: draft
---

# Absolute convergence

> [!definition] Definition 7.2.1
> The series $\sum_{n=1}^{\infty}a_n$ is called absolutely convergent if the series $\sum_{n=1}^{\infty}|a_n|$ converges.

> [!theorem] Property 5
> If a series converges absolutely, it converges.

> [!proof]- Proof as written in the notes
> By the Bolzano–Cauchy criterion, convergence of $\sum|a_k|$ gives $\sum_{k=n+1}^{n+p}|a_k|<\varepsilon$ for all $n>N$, $p\in\mathbb{N}$. Since $\left|\sum a_k\right|\le\sum|a_k|$, the Bolzano–Cauchy criterion yields convergence of $\sum a_k$. $\blacksquare$

## Related

- [[Bolzano–Cauchy criterion for series]]
- [[Convergence of a numeric series]]

> [!warning] Open markers: ⟦U081⟧, ⟦U082⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Абсолютная сходимость — `ru/Понятия/Абсолютная сходимость.md`
- es: Convergencia absoluta — `es/Conceptos/Convergencia absoluta.md`
