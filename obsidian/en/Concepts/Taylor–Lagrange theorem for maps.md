---
id: taylor-lagrange-map
type: theorem
semester: 3
lang: en
aliases: []
tags: [analysis/taylor, sem3, theorem]
source_pages: [p007]
translations: ["[[ru/Понятия/Теорема Тейлора–Лагранжа для отображений]]", "[[es/Conceptos/Teorema de Taylor–Lagrange para aplicaciones]]"]
status: draft
---

# Taylor–Lagrange theorem for maps

> [!theorem] Theorem 6.5.4
> Let $E$ be open in $\mathbb{R}^n$, $s\in\mathbb{Z}_+$, and let $f: E\to\mathbb{R}^m$ be $s+1$ times differentiable on $E$, $a,x\in E$ with $a\neq x$ and $\Delta_{a,x}\subset E$. Then
> $$\left\|f(x)-\sum_{k=0}^{s}\frac{d_a^kf(x-a)}{k!}\right\|\le\frac{1}{(s+1)!}\sup_{c\in\hat{\Delta}_{a,x}}\left\|d_c^{s+1}f(x-a)\right\|. \tag{6.5.2}$$

## Related

- [[Taylor–Lagrange theorem for functions]]
- [[Estimate of the Taylor remainder]]

## Other languages

- ru: Теорема Тейлора–Лагранжа для отображений — `ru/Понятия/Теорема Тейлора–Лагранжа для отображений.md`
- es: Teorema de Taylor–Lagrange para aplicaciones — `es/Conceptos/Teorema de Taylor–Lagrange para aplicaciones.md`
