---
id: taylor-polynomial-definition
type: definition
semester: 3
lang: es
aliases: []
tags: [analysis/taylor, sem3, definition]
source_pages: [p001, p002]
translations: ["[[ru/Понятия/Многочлен Тейлора]]", "[[en/Concepts/Taylor polynomial]]"]
status: draft
---

# Polinomio de Taylor

Sean $E\subset\mathbb{R}^n$, $a$ un punto interior de $E$, $f: E\to\mathbb{R}^m$, $s\in\mathbb{Z}_+$.

> [!definition] Definición 6.5.1
> Un polinomio $p:\mathbb{R}^n\to\mathbb{R}^m$ de grado no mayor que $s$ que satisface
> $$p(a)=f(a),\qquad f(x)=p(x)+o(\|x-a\|^s)\quad (x\to a) \tag{6.5.1}$$
> se llama polinomio de Taylor de $f$ de orden $s$ en $a$ y se denota $T_{a,s}f$.

Aquí $\|x-a\|=\sqrt{(x_1-a_1)^2+\ldots+(x_n-a_n)^2}$.

## Relaciones

- [[Multiíndice]]
- [[Unicidad del polinomio de Taylor]]

> [!warning] Marcas abiertas: ⟦S002⟧, ⟦U001⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Многочлен Тейлора — `ru/Понятия/Многочлен Тейлора.md`
- en: Taylor polynomial — `en/Concepts/Taylor polynomial.md`
