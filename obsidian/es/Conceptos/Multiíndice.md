---
id: multiindex-definition
type: definition
semester: 3
lang: es
aliases: []
tags: [analysis/taylor, sem3, definition]
source_pages: [p001]
translations: ["[[ru/Понятия/Мультииндекс]]", "[[en/Concepts/Multi-index]]"]
status: draft
---

# Multiíndice

Un multiíndice de dimensión $n$ es un elemento $\alpha\in\mathbb{Z}_+^n$. Su orden es $|\alpha|=\alpha_1+\ldots+\alpha_n$.

> [!definition] Polinomio en $n$ variables
> Sean $M$ un conjunto finito de multiíndices de dimensión $n$ y $\{C_\alpha\}_{\alpha\in M}$ una familia de elementos de $\mathbb{R}^m$. Entonces la aplicación
> $$p(x)=\sum_{\alpha\in M}C_\alpha x^\alpha=\sum_{\alpha\in M}C_\alpha x_1^{\alpha_1}x_2^{\alpha_2}\ldots x_n^{\alpha_n}$$
> se llama polinomio en $n$ variables con valores en $\mathbb{R}^m$.

Si $p\neq0$, el grado del polinomio es $\deg p=\max\{|\alpha|:\ \alpha\in M,\ C_\alpha\neq0\}$; en caso contrario el grado se toma igual a $-\infty$.

## Relaciones

- [[Polinomio de Taylor]]

> [!warning] Marcas abiertas: ⟦S003⟧, ⟦T004⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Мультииндекс — `ru/Понятия/Мультииндекс.md`
- en: Multi-index — `en/Concepts/Multi-index.md`
