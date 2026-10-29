---
id: taylor-lagrange-scalar
type: theorem
semester: 3
lang: en
aliases: []
tags: [analysis/taylor, sem3, theorem]
source_pages: [p005, p006]
translations: ["[[ru/Понятия/Теорема Тейлора–Лагранжа для функций]]", "[[es/Conceptos/Teorema de Taylor–Lagrange para funciones]]"]
status: draft
---

# Taylor–Lagrange theorem for functions

Put $\Delta_{a,b}=\{a+t(b-a):t\in[0,1]\}$ and $\hat{\Delta}_{a,b}=\Delta_{a,b}\setminus\{a,b\}$.

> [!theorem] Theorem 6.5.2
> Let $E$ be open in $\mathbb{R}^n$, $s\in\mathbb{N}$, and let $f: E\to\mathbb{R}$ be $s+1$ times differentiable on $E$, with $a\in E$ and $\Delta_{a,x}\subset E$. Then there exists $c\in\hat{\Delta}_{a,x}$ such that
> $$f(x)=\sum_{k=0}^{s}\frac{d_a^kf(x-a)}{k!}+\frac{d_c^{s+1}f(x-a)}{(s+1)!}.$$

> [!proof]- Proof as written in the notes
> Put $h:=x-a$ and $F(t)=f(a+th)$, $t\in[0,1]$; then $F^{(k)}(t)=d_{a+th}^kf(h)$. The one-dimensional Taylor–Lagrange formula is applied to $F$ at the point $1$, and one sets $c=a+\theta h$. $\blacksquare$

## Related

- [[Taylor–Peano theorem]]
- [[Mean value theorem]]
- [[Estimate of the Taylor remainder]]

> [!warning] Open markers: ⟦T023⟧, ⟦T024⟧, ⟦T025⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Теорема Тейлора–Лагранжа для функций — `ru/Понятия/Теорема Тейлора–Лагранжа для функций.md`
- es: Teorema de Taylor–Lagrange para funciones — `es/Conceptos/Teorema de Taylor–Lagrange para funciones.md`
