---
id: extremum-definition
type: definition
semester: 3
lang: es
aliases: ["extremo local", "punto estacionario"]
tags: [analysis/extrema, sem3, definition]
source_pages: [p011]
translations: ["[[ru/Понятия/Точки экстремума]]", "[[en/Concepts/Extremum points]]"]
status: draft
---

# Puntos de extremo

Sean $E\subset\mathbb{R}^n$, $a\in E$, $f: E\to\mathbb{R}$.

> [!definition] Definición 6.7.1
> - Si existe un entorno $V(a)$ tal que $f(x)\ge f(a)$ para todo $x\in V(a)\cap E$, entonces $a$ es un punto de mínimo de $f$.
> - Si $f(x)\le f(a)$ para todo $x\in V(a)\cap E$, entonces $a$ es un punto de máximo de $f$.
> - Si existe $V(a)$ tal que $f(x)>f(a)$ para todo $x\in\mathring{V}(a)\cap E$, entonces $a$ es un punto de mínimo estricto.
> - Si $f(x)<f(a)$ para todo $x\in\mathring{V}(a)\cap E$, entonces $a$ es un punto de máximo estricto.
> - Si $a$ es punto de mínimo o de máximo de $f$, se llama punto de extremo de $f$.

Un punto $a$ con $\operatorname{grad}f(a)=0$ se llama punto estacionario de $f$.

## Relaciones

- [[Condición necesaria de extremo]]
- [[Extremo condicional]]

> [!warning] Marcas abiertas: ⟦A042⟧, ⟦S043⟧, ⟦S044⟧, ⟦U041⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Точки экстремума — `ru/Понятия/Точки экстремума.md`
- en: Extremum points — `en/Concepts/Extremum points.md`
