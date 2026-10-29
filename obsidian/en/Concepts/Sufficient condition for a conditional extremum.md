---
id: conditional-extremum-sufficient
type: theorem
semester: 3
lang: en
aliases: []
tags: [analysis/extrema, sem3, theorem]
source_pages: [p018]
translations: ["[[ru/Понятия/Достаточное условие условного экстремума]]", "[[es/Conceptos/Condición suficiente de extremo condicional]]"]
status: draft
---

# Sufficient condition for a conditional extremum

> [!theorem] Theorem 6.7.5
> Let $m,n\in\mathbb{N}$, $m<n$, $E$ open in $\mathbb{R}^n$, $a\in E$, $f\in C^2(E)$, $\Phi\in C^2(E,\mathbb{R}^m)$, $\Phi(a)=0$, $\operatorname{rank}\Phi'(a)=m$. Put
> $$N=\{h\in\mathbb{R}^n:\ d_a\Phi(h)=0\},\qquad L(x)=f(x)-\sum_{k=1}^{m}\lambda_k\varphi_k(x),$$
> where $\lambda_1,\ldots,\lambda_m$ satisfy (6.7.1) at $a$. Then:
> 1) if $d_a^2L$ is positive (negative) definite on $N$, then $f$ has a conditional minimum (maximum) at $a$ subject to $\Phi=0$;
> 2) if $d_a^2L$ takes values of both signs on $N$, then $f$ has no conditional extremum at $a$.

## Related

- [[Lagrange multipliers]]
- [[Definiteness of a quadratic form on a subspace]]

> [!warning] Open markers: ⟦S067⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Достаточное условие условного экстремума — `ru/Понятия/Достаточное условие условного экстремума.md`
- es: Condición suficiente de extremo condicional — `es/Conceptos/Condición suficiente de extremo condicional.md`
