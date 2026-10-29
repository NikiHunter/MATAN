---
id: series-properties
type: theorem
semester: 3
lang: es
aliases: []
tags: [analysis/series, sem3, theorem]
source_pages: [p019, p020]
translations: ["[[ru/Понятия/Свойства сходящихся рядов]]", "[[en/Concepts/Properties of convergent series]]"]
status: draft
---

# Propiedades de las series convergentes

> [!theorem] Propiedades de las series
> 1) Si $\sum_{n=1}^{\infty}a_n$ converge, entonces $a_n\to0$ cuando $n\to\infty$.
> 2) $\sum_{n=1}^{\infty}a_n$ converge si y solo si para todo $k$ converge el resto $\sum_{n=k+1}^{\infty}a_n$.
> 3) Las series $\sum a_n$ y $\sum ka_n$, $k\in\mathbb{R}$, convergen o divergen simultáneamente; si convergen, $\sum ka_n=k\sum a_n$.
> 4) Si $\sum a_n$ y $\sum b_n$ convergen, entonces $\sum(a_n+b_n)$ converge y $\sum(a_n+b_n)=\sum a_n+\sum b_n$.

> [!warning] Enunciados recíprocos
> De $a_n\to0$ no se sigue la convergencia. Si $\sum a_n$ diverge y $\sum b_n$ converge, entonces $\sum(a_n+b_n)$ diverge: de lo contrario convergería la serie de términos $a_n=(a_n+b_n)-b_n$.

> [!proof]- Demostración de la propiedad 1 tal como está en los apuntes
> Si $S_N=\sum_{k=1}^{N}a_k\to S$, entonces $a_N=S_N-S_{N-1}\to S-S=0$. $\blacksquare$

## Relaciones

- [[Convergencia de una serie numérica]]
- [[Criterio de Bolzano–Cauchy para series]]
- [[Serie armónica]]

> [!warning] Marcas abiertas: ⟦M071⟧, ⟦M073⟧, ⟦S070⟧, ⟦S074⟧, ⟦S075⟧, ⟦S076⟧, ⟦S077⟧, ⟦U072⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Свойства сходящихся рядов — `ru/Понятия/Свойства сходящихся рядов.md`
- en: Properties of convergent series — `en/Concepts/Properties of convergent series.md`
