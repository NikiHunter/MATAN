---
id: hessian-criterion-dim2
type: theorem
semester: 3
lang: en
aliases: ["Sylvester criterion for a 2×2 matrix"]
tags: [analysis/extrema, sem3, theorem]
source_pages: [p013]
translations: ["[[ru/Понятия/Критерий для $n=2$ через $A$, $B$, $C$]]", "[[es/Conceptos/Criterio para $n=2$ mediante $A$, $B$, $C$]]"]
status: draft
---

# Criterion for $n=2$ via $A$, $B$, $C$

Let $E\subset\mathbb{R}^2$, let $a$ be an interior point of $E$, and let $f: E\to\mathbb{R}$ be twice differentiable at $a$ with $d_af=0$. Put
$$A=\frac{\partial^2f}{\partial x^2}(a),\qquad B=\frac{\partial^2f}{\partial x\partial y}(a),\qquad C=\frac{\partial^2f}{\partial y^2}(a).$$

> [!theorem] Corollary
> 1) If $A>0$ and $AC>B^2$, then $a$ is a strict minimum point of $f$.
> 2) If $A<0$ and $AC>B^2$, then $a$ is a strict maximum point of $f$.
> 3) If $AC<B^2$, then $f$ has no extremum at $a$.

> [!proof]- Proof as written in the notes
> The quadratic form $d_a^2f(h)$ has the Hessian matrix $H=\begin{pmatrix}A & B\\ B & C\end{pmatrix}$ with principal minors $\Delta_1=A$, $\Delta_2=\det H=AC-B^2$; by the Sylvester criterion $\Delta_1>0,\Delta_2>0$ give positive definiteness and $\Delta_1<0,\Delta_2>0$ negative definiteness. If $AC<B^2$, the form $A\,dx^2+2B\,dxdy+C\,dy^2$ takes values of both signs. $\blacksquare$

> [!example] Example from the notes
> For $f(x,y)=x^4+3xy^2+y^4$ at $(0,0)$ the Hessian is zero (degenerate), but $d_a^3f\not\equiv0$, so there is no extremum at $(0,0)$.

## Related

- [[Sufficient condition for an extremum]]
- [[Definiteness of a quadratic form on a subspace]]

> [!warning] Open markers: ⟦S050⟧, ⟦M051⟧, ⟦A052⟧, ⟦A053⟧, ⟦A054⟧, ⟦G055⟧, ⟦A056⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Критерий для $n=2$ через $A$, $B$, $C$ — `ru/Понятия/Критерий для $n=2$ через $A$, $B$, $C$.md`
- es: Criterio para $n=2$ mediante $A$, $B$, $C$ — `es/Conceptos/Criterio para $n=2$ mediante $A$, $B$, $C$.md`
