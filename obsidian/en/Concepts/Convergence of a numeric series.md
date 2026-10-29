---
id: series-convergence
type: definition
semester: 3
lang: en
aliases: ["convergent series", "divergent series"]
tags: [analysis/series, sem3, definition]
source_pages: [p018, p019]
translations: ["[[ru/Понятия/Сходимость числового ряда]]", "[[es/Conceptos/Convergencia de una serie numérica]]"]
status: draft
---

# Convergence of a numeric series

> [!definition] Definition 7.1.2
> The series $\sum_{n=1}^{\infty}a_n$ converges if the sum $S$ exists and is finite. Otherwise the series diverges.

In terms of partial sums $S_n=\sum_{k=1}^{n}a_k$ and $S=\lim_{n\to\infty}S_n$:

1) $S$ exists and $S<\infty$ — the series converges;
2) $S=\infty$ — the series diverges;
3) $S$ does not exist — the series diverges.

> [!example] Examples from the notes
> $\sum 0=0$ converges; $\sum_{k=1}^{\infty}1$ diverges since $S_n=n$; $\sum_{k=0}^{\infty}(-1)^k$ diverges since $\{S_n\}$ has neither a finite nor an infinite limit; $\sum_{k=1}^{\infty}\dfrac{1}{k(k+1)}=1$ converges, as $S_n=1-\dfrac{1}{n+1}$.

## Related

- [[Numeric series]]
- [[Properties of convergent series]]
- [[Harmonic series]]

> [!warning] Open markers: ⟦S068⟧, ⟦S069⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Сходимость числового ряда — `ru/Понятия/Сходимость числового ряда.md`
- es: Convergencia de una serie numérica — `es/Conceptos/Convergencia de una serie numérica.md`
