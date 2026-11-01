---
id: extremum-necessary-condition
type: theorem
semester: 3
lang: en
aliases: []
tags: [analysis/extrema, sem3, theorem]
source_pages: [p011, p012]
translations: ["[[ru/Понятия/Необходимое условие экстремума]]", "[[es/Conceptos/Condición necesaria de extremo]]"]
status: draft
---

# Necessary condition for an extremum

> [!theorem] Theorem 6.7.1
> Let $E\subset\mathbb{R}^n$, let $a$ be an interior point of $E$, and let $f: E\to\mathbb{R}$ be differentiable at $a$. If $a$ is an extremum point of $f$, then $d_af=0$.

In coordinates this means $\dfrac{\partial f}{\partial x_k}(a)=0$ for all $k\in\{1,\ldots,n\}$, that is $\operatorname{grad}f(a)=0$: an extremum point is stationary.

> [!proof]- Proof as written in the notes
> Let $a$ be a minimum point: $f(x)\ge f(a)$ for $x\in V_\delta(a)$. For $h\neq0$ put $F(t)=f(a+th)$ with $t\in\left(-\delta/\|h\|,\delta/\|h\|\right)$. Then $F'(0)=d_af(h)$ and $F(t)\ge F(0)$, hence $F'(0)=0$ for all $h\neq0$, that is $d_af=0$. $\blacksquare$

## Related

- [[Extremum points]]
- [[Sufficient condition for an extremum]]

> [!warning] Open markers: ⟦S045⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Необходимое условие экстремума — `ru/Понятия/Необходимое условие экстремума.md`
- es: Condición necesaria de extremo — `es/Conceptos/Condición necesaria de extremo.md`
