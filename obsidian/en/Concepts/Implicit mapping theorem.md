---
id: implicit-mapping-theorem
type: theorem
semester: 3
lang: en
aliases: []
tags: [analysis/implicit, sem3, theorem]
source_pages: [p009]
translations: ["[[ru/Понятия/Теорема о неявном отображении]]", "[[es/Conceptos/Teorema de la aplicación implícita]]"]
status: draft
---

# Implicit mapping theorem

> [!theorem] Theorem 6.6.1
> Let $E$ be open in $\mathbb{R}^{n+m}$, $(x^0,y^0)\in E$, $s\in\mathbb{N}$, $f\in C^s(E,\mathbb{R}^m)$, with $f(x^0,y^0)=0$ and $\det f'_y(x^0,y^0)\neq0$. Then there exist a neighbourhood $V(x^0,y^0)$, an open set $U$ containing $x^0$ and a map $\varphi\in C^s(U,\mathbb{R}^m)$ such that
> $$\{(x,y)\in V(x^0,y^0):\ f(x,y)=0\}=\{(x,\varphi(x)):\ x\in U\}.$$

Thus the solution set of (6.6.3) near $(x^0,y^0)$ is the graph of a map $\varphi$ of the same smoothness class as $f$.

![[p009_fig1.jpg]]

The figure in the notes is accompanied by $U\times\varphi(U)=V(x^0,y^0)$.

## Related

- [[Implicit function]]
- [[Differentiating an implicit map]]

> [!warning] Open markers: ⟦A034⟧, ⟦G038⟧, ⟦M060⟧, ⟦S035⟧, ⟦T037⟧, ⟦U036⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Теорема о неявном отображении — `ru/Понятия/Теорема о неявном отображении.md`
- es: Teorema de la aplicación implícita — `es/Conceptos/Teorema de la aplicación implícita.md`
