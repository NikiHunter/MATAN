---
id: taylor-peano-theorem
type: theorem
semester: 3
lang: en
aliases: ["Taylor formula with Peano remainder"]
tags: [analysis/taylor, sem3, theorem]
source_pages: [p004]
translations: ["[[ru/Понятия/Теорема Тейлора–Пеано]]", "[[es/Conceptos/Teorema de Taylor–Peano]]"]
status: draft
---

# Taylor–Peano theorem

> [!theorem] Theorem 6.5.1
> Let $E\subset\mathbb{R}^n$, let $a$ be an interior point of $E$, $s\in\mathbb{Z}_+$, and let $f: E\to\mathbb{R}^m$ be $s$ times differentiable at $a$. Then
> $$f(x)=\sum_{|\alpha|\le s}\frac{1}{\alpha!}\frac{\partial^\alpha f}{\partial x^\alpha}(a)(x-a)^\alpha+o(\|x-a\|^s)\quad \text{as } x\to a.$$

In other words the Taylor polynomial of order $s$ exists and equals
$$T_{a,s}f(x)=\sum_{|\alpha|\le s}\frac{1}{\alpha!}\frac{\partial^\alpha f}{\partial x^\alpha}(a)(x-a)^\alpha,$$
the sum being taken over all multi-indices of order $\le s$.

> [!proof]- Proof as written in the notes
> Take $p(x)$ equal to this sum and set $F:=f-p$. For every multi-index $\alpha$ of order at most $s$ we have $\partial^\alpha F/\partial x^\alpha(a)=0$; lemma 6.5.1 then gives $F(x)=o(\|x-a\|^s)$ as $x\to a$. $\blacksquare$

## Related

- [[Lemma 6.5.1]]
- [[Taylor–Lagrange theorem for functions]]

> [!warning] Open markers: ⟦A021⟧, ⟦S020⟧, ⟦T018⟧, ⟦T019⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Теорема Тейлора–Пеано — `ru/Понятия/Теорема Тейлора–Пеано.md`
- es: Teorema de Taylor–Peano — `es/Conceptos/Teorema de Taylor–Peano.md`
