---
id: series-properties
type: theorem
semester: 3
lang: en
aliases: []
tags: [analysis/series, sem3, theorem]
source_pages: [p019, p020]
translations: ["[[ru/Понятия/Свойства сходящихся рядов]]", "[[es/Conceptos/Propiedades de las series convergentes]]"]
status: draft
---

# Properties of convergent series

> [!theorem] Properties of series
> 1) If $\sum_{n=1}^{\infty}a_n$ converges, then $a_n\to0$ as $n\to\infty$.
> 2) $\sum_{n=1}^{\infty}a_n$ converges if and only if for every $k$ the remainder $\sum_{n=k+1}^{\infty}a_n$ converges.
> 3) The series $\sum a_n$ and $\sum ka_n$, $k\in\mathbb{R}$, converge or diverge simultaneously; when they converge, $\sum ka_n=k\sum a_n$.
> 4) If $\sum a_n$ and $\sum b_n$ converge, then $\sum(a_n+b_n)$ converges and $\sum(a_n+b_n)=\sum a_n+\sum b_n$.

> [!warning] Converse statements
> $a_n\to0$ does not imply convergence. If $\sum a_n$ diverges while $\sum b_n$ converges, then $\sum(a_n+b_n)$ diverges: otherwise the series with terms $a_n=(a_n+b_n)-b_n$ would converge.

> [!proof]- Proof of property 1 as written in the notes
> If $S_N=\sum_{k=1}^{N}a_k\to S$, then $a_N=S_N-S_{N-1}\to S-S=0$. $\blacksquare$

## Related

- [[Convergence of a numeric series]]
- [[Bolzano–Cauchy criterion for series]]
- [[Harmonic series]]

> [!warning] Open markers: ⟦M071⟧, ⟦M073⟧, ⟦S070⟧, ⟦S074⟧, ⟦S075⟧, ⟦S076⟧, ⟦S077⟧, ⟦U072⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Свойства сходящихся рядов — `ru/Понятия/Свойства сходящихся рядов.md`
- es: Propiedades de las series convergentes — `es/Conceptos/Propiedades de las series convergentes.md`
