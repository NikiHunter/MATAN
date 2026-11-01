---
id: hessian-criterion-dim2
type: theorem
semester: 3
lang: es
aliases: ["criterio de Sylvester para una matriz 2×2"]
tags: [analysis/extrema, sem3, theorem]
source_pages: [p013]
translations: ["[[ru/Понятия/Критерий для $n=2$ через $A$, $B$, $C$]]", "[[en/Concepts/Criterion for $n=2$ via $A$, $B$, $C$]]"]
status: draft
---

# Criterio para $n=2$ mediante $A$, $B$, $C$

Sean $E\subset\mathbb{R}^2$, $a$ un punto interior de $E$ y $f: E\to\mathbb{R}$ dos veces diferenciable en $a$ con $d_af=0$. Se pone
$$A=\frac{\partial^2f}{\partial x^2}(a),\qquad B=\frac{\partial^2f}{\partial x\partial y}(a),\qquad C=\frac{\partial^2f}{\partial y^2}(a).$$

> [!theorem] Corolario
> 1) Si $A>0$ y $AC>B^2$, entonces $a$ es un punto de mínimo estricto de $f$.
> 2) Si $A<0$ y $AC>B^2$, entonces $a$ es un punto de máximo estricto de $f$.
> 3) Si $AC<B^2$, entonces $f$ no tiene extremo en $a$.

> [!proof]- Demostración tal como está en los apuntes
> La forma cuadrática $d_a^2f(h)$ tiene matriz hessiana $H=\begin{pmatrix}A & B\\ B & C\end{pmatrix}$ con menores principales $\Delta_1=A$, $\Delta_2=\det H=AC-B^2$; por el criterio de Sylvester, $\Delta_1>0,\Delta_2>0$ dan definición positiva y $\Delta_1<0,\Delta_2>0$ definición negativa. Si $AC<B^2$, la forma $A\,dx^2+2B\,dxdy+C\,dy^2$ toma valores de ambos signos. $\blacksquare$

> [!example] Ejemplo de los apuntes
> Para $f(x,y)=x^4+3xy^2+y^4$ en $(0,0)$ la matriz hessiana es nula (degenerada), pero $d_a^3f\not\equiv0$, por lo que no hay extremo en $(0,0)$.

## Relaciones

- [[Condición suficiente de extremo]]
- [[Definición de una forma cuadrática en un subespacio]]

> [!warning] Marcas abiertas: ⟦S050⟧, ⟦M051⟧, ⟦A052⟧, ⟦A053⟧, ⟦A054⟧, ⟦G055⟧, ⟦A056⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Критерий для $n=2$ через $A$, $B$, $C$ — `ru/Понятия/Критерий для $n=2$ через $A$, $B$, $C$.md`
- en: Criterion for $n=2$ via $A$, $B$, $C$ — `en/Concepts/Criterion for $n=2$ via $A$, $B$, $C$.md`
