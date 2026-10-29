---
id: conditional-extremum-definition
type: definition
semester: 3
lang: en
aliases: ["relative extremum", "constraint equations"]
tags: [analysis/extrema, sem3, definition]
source_pages: [p015]
translations: ["[[ru/Понятия/Условный экстремум]]", "[[es/Conceptos/Extremo condicional]]"]
status: draft
---

# Conditional extremum

Let $f: E\subset\mathbb{R}^n\to\mathbb{R}$ and let $a\in E$ be an extremum point of $f$. If one is interested not in all points $x\in V(a)$ but only in those satisfying additional equalities — constraint equations — one speaks of a conditional (relative) extremum.

> [!definition] Definition 6.7.2
> Let $E\subset\mathbb{R}^n$, $a\in E$, $m\in\mathbb{N}$, $m<n$, $f,\varphi_1,\ldots,\varphi_m: E\to\mathbb{R}$. Suppose that $a$ is an extremum point of the restriction of $f$ to the set
> $$\{x\in E:\ \varphi_k(x)=\varphi_k(a)\ \forall k=1..m\}.$$
> Then $a$ is called a conditional (relative) extremum point of $f$ of the corresponding type, subject to the constraint equations $\varphi_k(x)=\varphi_k(a)$, $k\in\{1,\ldots,m\}$, $x\in E$.

Without loss of generality one may assume $\varphi_k(a)=0$ for all $k$.

## Related

- [[Lagrange multipliers]]
- [[Extremum points]]

> [!warning] Open markers: ⟦S057⟧, ⟦M058⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Условный экстремум — `ru/Понятия/Условный экстремум.md`
- es: Extremo condicional — `es/Conceptos/Extremo condicional.md`
