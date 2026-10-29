---
id: multiindex-definition
type: definition
semester: 3
lang: en
aliases: []
tags: [analysis/taylor, sem3, definition]
source_pages: [p001]
translations: ["[[ru/Понятия/Мультииндекс]]", "[[es/Conceptos/Multiíndice]]"]
status: draft
---

# Multi-index

A multi-index of dimension $n$ is an element $\alpha\in\mathbb{Z}_+^n$. Its order is $|\alpha|=\alpha_1+\ldots+\alpha_n$.

> [!definition] Polynomial in $n$ variables
> Let $M$ be a finite set of multi-indices of dimension $n$ and let $\{C_\alpha\}_{\alpha\in M}$ be a family of elements of $\mathbb{R}^m$. Then the map
> $$p(x)=\sum_{\alpha\in M}C_\alpha x^\alpha=\sum_{\alpha\in M}C_\alpha x_1^{\alpha_1}x_2^{\alpha_2}\ldots x_n^{\alpha_n}$$
> is called a polynomial in $n$ variables with values in $\mathbb{R}^m$.

If $p\neq0$, the degree of the polynomial is $\deg p=\max\{|\alpha|:\ \alpha\in M,\ C_\alpha\neq0\}$; otherwise the degree is taken to be $-\infty$.

## Related

- [[Taylor polynomial]]

> [!warning] Open markers: ⟦S003⟧, ⟦T004⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Мультииндекс — `ru/Понятия/Мультииндекс.md`
- es: Multiíndice — `es/Conceptos/Multiíndice.md`
