---
id: extremum-necessary-condition
type: theorem
semester: 3
lang: es
aliases: []
tags: [analysis/extrema, sem3, theorem]
source_pages: [p011, p012]
translations: ["[[ru/Понятия/Необходимое условие экстремума]]", "[[en/Concepts/Necessary condition for an extremum]]"]
status: draft
---

# Condición necesaria de extremo

> [!theorem] Teorema 6.7.1
> Sean $E\subset\mathbb{R}^n$, $a$ un punto interior de $E$ y $f: E\to\mathbb{R}$ diferenciable en $a$. Si $a$ es un punto de extremo de $f$, entonces $d_af=0$.

En coordenadas esto significa $\dfrac{\partial f}{\partial x_k}(a)=0$ para todo $k\in\{1,\ldots,n\}$, es decir $\operatorname{grad}f(a)=0$: el punto de extremo es estacionario.

> [!proof]- Demostración tal como está en los apuntes
> Sea $a$ un punto de mínimo: $f(x)\ge f(a)$ para $x\in V_\delta(a)$. Para $h\neq0$ se pone $F(t)=f(a+th)$ con $t\in\left(-\delta/\|h\|,\delta/\|h\|\right)$. Entonces $F'(0)=d_af(h)$ y $F(t)\ge F(0)$, luego $F'(0)=0$ para todo $h\neq0$, es decir $d_af=0$. $\blacksquare$

## Relaciones

- [[Puntos de extremo]]
- [[Condición suficiente de extremo]]

> [!warning] Marcas abiertas: ⟦S045⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Необходимое условие экстремума — `ru/Понятия/Необходимое условие экстремума.md`
- en: Necessary condition for an extremum — `en/Concepts/Necessary condition for an extremum.md`
