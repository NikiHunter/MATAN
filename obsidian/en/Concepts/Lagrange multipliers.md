---
id: lagrange-multipliers
type: theorem
semester: 3
lang: en
aliases: ["necessary condition for a conditional extremum"]
tags: [analysis/extrema, sem3, theorem]
source_pages: [p015, p016, p017]
translations: ["[[ru/Понятия/Множители Лагранжа]]", "[[es/Conceptos/Multiplicadores de Lagrange]]"]
status: draft
---

# Lagrange multipliers

Write $\Phi=(\varphi_1,\ldots,\varphi_m)$, that is $\Phi: E\subset\mathbb{R}^n\to\mathbb{R}^m$.

> [!theorem] Theorem 6.7.3
> Let $m,n\in\mathbb{N}$, $m<n$, $E$ open in $\mathbb{R}^n$, $a\in E$, $f\in C^1(E)$, $\Phi\in C^1(E,\mathbb{R}^m)$, $\operatorname{rank}\Phi'(a)=m$. If $a$ is a conditional extremum point of $f$ subject to $\Phi=0$, then there exist $\lambda_1,\ldots,\lambda_m\in\mathbb{R}$ such that
> $$\operatorname{grad}f(a)=\sum_{k=1}^{m}\lambda_k\operatorname{grad}\varphi_k(a). \tag{6.7.1}$$

The numbers $\lambda_1,\ldots,\lambda_m$ satisfying (6.7.1) are called Lagrange multipliers.

> [!proof]- Outline from the notes
> Points of $\mathbb{R}^n$ are written as $(x,y)$ with $x\in\mathbb{R}^{n-m}$, $y\in\mathbb{R}^m$, and $a=(x^0,y^0)$; the set $M=\{(x,y)\in E:\ \varphi_k(x,y)=0\}$ is locally a graph: $M\cap V(a)=\{(x,\psi(x))\}$.
>
> Since $f|_M$ has an extremum at $a$, the function $F(x)=f(x,\psi(x))$ has an extremum at $x^0$, so $\nabla F(x^0)=0$ and $f'_x(a)+f'_y(a)\psi'(x^0)=0$. From $\Phi(x,\psi(x))=0$ it follows that $\Phi'_x(a)+\Phi'_y(a)\psi'(x^0)=0$. With $\lambda=f'_y(a)[\Phi'_y(a)]^{-1}$ both terms in $[f'_x-\lambda\Phi'_x]+[f'_y-\lambda\Phi'_y]\psi'=0$ vanish, which gives (6.7.1). $\blacksquare$

## Related

- [[Conditional extremum]]
- [[Lagrange function]]
- [[Sufficient condition for a conditional extremum]]

> [!warning] Open markers: ⟦U059⟧, ⟦U061⟧, ⟦S062⟧, ⟦A063⟧, ⟦S064⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Множители Лагранжа — `ru/Понятия/Множители Лагранжа.md`
- es: Multiplicadores de Lagrange — `es/Conceptos/Multiplicadores de Lagrange.md`
