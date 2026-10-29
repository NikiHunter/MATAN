---
id: taylor-polynomial-definition
type: definition
semester: 3
lang: en
aliases: ["Taylor poly"]
tags: [analysis/taylor, sem3, definition]
source_pages: [p001, p002]
translations: ["[[ru/Понятия/Многочлен Тейлора]]", "[[es/Conceptos/Polinomio de Taylor]]"]
status: draft
---

# Taylor polynomial

Let $E\subset\mathbb{R}^n$, let $a$ be an interior point of $E$, $f: E\to\mathbb{R}^m$, $s\in\mathbb{Z}_+$.

> [!definition] Definition 6.5.1
> A polynomial $p:\mathbb{R}^n\to\mathbb{R}^m$ of degree at most $s$ satisfying
> $$p(a)=f(a),\qquad f(x)=p(x)+o(\|x-a\|^s)\quad (x\to a) \tag{6.5.1}$$
> is called the Taylor polynomial of $f$ of order $s$ at $a$ and is denoted by $T_{a,s}f$.

Here $\|x-a\|=\sqrt{(x_1-a_1)^2+\ldots+(x_n-a_n)^2}$.

## Related

- [[Multi-index]]
- [[Uniqueness of the Taylor polynomial]]

> [!warning] Open markers: ⟦S002⟧, ⟦U001⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Многочлен Тейлора — `ru/Понятия/Многочлен Тейлора.md`
- es: Polinomio de Taylor — `es/Conceptos/Polinomio de Taylor.md`
