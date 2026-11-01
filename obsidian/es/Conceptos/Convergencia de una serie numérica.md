---
id: series-convergence
type: definition
semester: 3
lang: es
aliases: ["serie convergente", "serie divergente"]
tags: [analysis/series, sem3, definition]
source_pages: [p018, p019]
translations: ["[[ru/Понятия/Сходимость числового ряда]]", "[[en/Concepts/Convergence of a numeric series]]"]
status: draft
---

# Convergencia de una serie numérica

> [!definition] Definición 7.1.2
> La serie $\sum_{n=1}^{\infty}a_n$ converge si la suma $S$ existe y es finita. En caso contrario la serie diverge.

En términos de las sumas parciales $S_n=\sum_{k=1}^{n}a_k$ y $S=\lim_{n\to\infty}S_n$:

1) $S$ existe y $S<\infty$ — la serie converge;
2) $S=\infty$ — la serie diverge;
3) $S$ no existe — la serie diverge.

> [!example] Ejemplos de los apuntes
> $\sum 0=0$ converge; $\sum_{k=1}^{\infty}1$ diverge porque $S_n=n$; $\sum_{k=0}^{\infty}(-1)^k$ diverge porque $\{S_n\}$ no tiene límite finito ni infinito; $\sum_{k=1}^{\infty}\dfrac{1}{k(k+1)}=1$ converge, pues $S_n=1-\dfrac{1}{n+1}$.

## Relaciones

- [[Serie numérica]]
- [[Propiedades de las series convergentes]]
- [[Serie armónica]]

> [!warning] Marcas abiertas: ⟦S068⟧, ⟦S069⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Сходимость числового ряда — `ru/Понятия/Сходимость числового ряда.md`
- en: Convergence of a numeric series — `en/Concepts/Convergence of a numeric series.md`
