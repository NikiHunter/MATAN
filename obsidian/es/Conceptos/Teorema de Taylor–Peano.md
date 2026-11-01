---
id: taylor-peano-theorem
type: theorem
semester: 3
lang: es
aliases: ["fórmula de Taylor con resto de Peano"]
tags: [analysis/taylor, sem3, theorem]
source_pages: [p004]
translations: ["[[ru/Понятия/Теорема Тейлора–Пеано]]", "[[en/Concepts/Taylor–Peano theorem]]"]
status: draft
---

# Teorema de Taylor–Peano

> [!theorem] Teorema 6.5.1
> Sean $E\subset\mathbb{R}^n$, $a$ un punto interior de $E$, $s\in\mathbb{Z}_+$ y $f: E\to\mathbb{R}^m$ $s$ veces diferenciable en $a$. Entonces
> $$f(x)=\sum_{|\alpha|\le s}\frac{1}{\alpha!}\frac{\partial^\alpha f}{\partial x^\alpha}(a)(x-a)^\alpha+o(\|x-a\|^s)\quad \text{cuando } x\to a.$$

En otras palabras, el polinomio de Taylor de orden $s$ existe y es igual a
$$T_{a,s}f(x)=\sum_{|\alpha|\le s}\frac{1}{\alpha!}\frac{\partial^\alpha f}{\partial x^\alpha}(a)(x-a)^\alpha,$$
donde la suma recorre todos los multiíndices de orden $\le s$.

> [!proof]- Demostración tal como está en los apuntes
> Se toma $p(x)$ igual a esta suma y $F:=f-p$. Para todo multiíndice $\alpha$ de orden no mayor que $s$ se tiene $\partial^\alpha F/\partial x^\alpha(a)=0$; el lema 6.5.1 da $F(x)=o(\|x-a\|^s)$ cuando $x\to a$. $\blacksquare$

## Relaciones

- [[Lema 6.5.1]]
- [[Teorema de Taylor–Lagrange para funciones]]

> [!warning] Marcas abiertas: ⟦A021⟧, ⟦S020⟧, ⟦T018⟧, ⟦T019⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Теорема Тейлора–Пеано — `ru/Понятия/Теорема Тейлора–Пеано.md`
- en: Taylor–Peano theorem — `en/Concepts/Taylor–Peano theorem.md`
