---
id: extremum-definition
type: definition
semester: 3
lang: en
aliases: ["local extremum", "stationary point"]
tags: [analysis/extrema, sem3, definition]
source_pages: [p011]
translations: ["[[ru/Понятия/Точки экстремума]]", "[[es/Conceptos/Puntos de extremo]]"]
status: draft
---

# Extremum points

Let $E\subset\mathbb{R}^n$, $a\in E$, $f: E\to\mathbb{R}$.

> [!definition] Definition 6.7.1
> - If there is a neighbourhood $V(a)$ such that $f(x)\ge f(a)$ for all $x\in V(a)\cap E$, then $a$ is a minimum point of $f$.
> - If $f(x)\le f(a)$ for all $x\in V(a)\cap E$, then $a$ is a maximum point of $f$.
> - If there is $V(a)$ such that $f(x)>f(a)$ for all $x\in\mathring{V}(a)\cap E$, then $a$ is a strict minimum point.
> - If $f(x)<f(a)$ for all $x\in\mathring{V}(a)\cap E$, then $a$ is a strict maximum point.
> - A point that is a minimum or a maximum point of $f$ is called an extremum point of $f$.

A point $a$ with $\operatorname{grad}f(a)=0$ is called a stationary point of $f$.

## Related

- [[Necessary condition for an extremum]]
- [[Conditional extremum]]

> [!warning] Open markers: ⟦A042⟧, ⟦S043⟧, ⟦S044⟧, ⟦U041⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Точки экстремума — `ru/Понятия/Точки экстремума.md`
- es: Puntos de extremo — `es/Conceptos/Puntos de extremo.md`
