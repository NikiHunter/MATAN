---
id: lagrange-function
type: property
semester: 3
lang: en
aliases: ["Lagrangian"]
tags: [analysis/extrema, sem3, property]
source_pages: [p017]
translations: ["[[ru/Понятия/Функция Лагранжа]]", "[[es/Conceptos/Función de Lagrange]]"]
status: draft
---

# Lagrange function

> [!theorem] Theorem 6.7.4
> Let $m,n\in\mathbb{N}$, $m<n$, $E$ open in $\mathbb{R}^n$, $a\in E$, $f\in C^1(E)$, $\Phi\in C^1(E,\mathbb{R}^m)$, $\operatorname{rank}\Phi'(a)=m$. If $a$ is a conditional extremum point of $f$ subject to $\Phi=0$ and
> $$L(x,\lambda)=f(x)-\sum_{k=1}^{m}\lambda_k\varphi_k(x)\quad (x\in E,\ \lambda\in\mathbb{R}^m),$$
> then there exists $\lambda\in\mathbb{R}^m$ with $\operatorname{grad}L(a,\lambda)=0$.

This restates theorem 6.7.3 in terms of the Lagrange function: condition (6.7.1) is equivalent to stationarity of $L$ in $x$.

## Related

- [[Lagrange multipliers]]
- [[Sufficient condition for a conditional extremum]]

> [!warning] Open markers: ⟦T065⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Функция Лагранжа — `ru/Понятия/Функция Лагранжа.md`
- es: Función de Lagrange — `es/Conceptos/Función de Lagrange.md`
