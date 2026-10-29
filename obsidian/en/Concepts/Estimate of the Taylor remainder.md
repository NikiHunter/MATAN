---
id: taylor-remainder-estimate
type: theorem
semester: 3
lang: en
aliases: []
tags: [analysis/taylor, sem3, theorem]
source_pages: [p006, p007]
translations: ["[[ru/Понятия/Оценка остатка в формуле Тейлора]]", "[[es/Conceptos/Estimación del resto de Taylor]]"]
status: draft
---

# Estimate of the Taylor remainder

The remainder in the Taylor formula is $R_{a,s}f=f-T_{a,s}f$; theorem 6.5.1 can be written as $R_{a,s}f(x)=o(\|x-a\|^s)$ as $x\to a$.

> [!theorem] Theorem 6.5.5
> Let $E$ be open in $\mathbb{R}^n$, $s\in\mathbb{Z}_+$, $f\in C^{s+1}(E,\mathbb{R}^m)$, $a,x\in E$ with $a\neq x$ and $\Delta_{a,x}\subset E$. Put
> $$M=\max_{\alpha\in M_{s+1}}\sup_{c\in\hat{\Delta}_{a,x}}\left\|\frac{\partial^\alpha f}{\partial x^\alpha}(c)\right\|.$$
> Then $M<\infty$ and
> $$\left\|R_{a,s}f(x)\right\|\le\frac{M}{(s+1)!}\left(\sqrt{n}\,\|x-a\|\right)^{s+1}.$$

For functions the notes record the corollary of theorem 6.5.2: $\left|R_{a,s}f(x)\right|\le\sup_{c\in\hat{\Delta}_{a,x}}\dfrac{\left|d_c^{s+1}f(x-a)\right|}{(s+1)!}$.

## Related

- [[Taylor–Lagrange theorem for maps]]
- [[Taylor–Peano theorem]]

> [!warning] Open markers: ⟦A030⟧, ⟦T022⟧, ⟦U029⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Оценка остатка в формуле Тейлора — `ru/Понятия/Оценка остатка в формуле Тейлора.md`
- es: Estimación del resto de Taylor — `es/Conceptos/Estimación del resto de Taylor.md`
