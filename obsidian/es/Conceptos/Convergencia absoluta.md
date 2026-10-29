---
id: absolute-convergence
type: definition
semester: 3
lang: es
aliases: []
tags: [analysis/series, sem3, definition]
source_pages: [p021]
translations: ["[[ru/Понятия/Абсолютная сходимость]]", "[[en/Concepts/Absolute convergence]]"]
status: draft
---

# Convergencia absoluta

> [!definition] Definición 7.2.1
> La serie $\sum_{n=1}^{\infty}a_n$ se llama absolutamente convergente si la serie $\sum_{n=1}^{\infty}|a_n|$ converge.

> [!theorem] Propiedad 5
> Si una serie converge absolutamente, entonces converge.

> [!proof]- Demostración tal como está en los apuntes
> Por el criterio de Bolzano–Cauchy, de la convergencia de $\sum|a_k|$ se sigue $\sum_{k=n+1}^{n+p}|a_k|<\varepsilon$ para todo $n>N$ y $p\in\mathbb{N}$. Como $\left|\sum a_k\right|\le\sum|a_k|$, el criterio de Bolzano–Cauchy da la convergencia de $\sum a_k$. $\blacksquare$

## Relaciones

- [[Criterio de Bolzano–Cauchy para series]]
- [[Convergencia de una serie numérica]]

> [!warning] Marcas abiertas: ⟦U081⟧, ⟦U082⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Абсолютная сходимость — `ru/Понятия/Абсолютная сходимость.md`
- en: Absolute convergence — `en/Concepts/Absolute convergence.md`
