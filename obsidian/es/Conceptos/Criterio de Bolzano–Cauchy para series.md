---
id: cauchy-criterion-series
type: theorem
semester: 3
lang: es
aliases: []
tags: [analysis/series, sem3, theorem]
source_pages: [p021]
translations: ["[[ru/Понятия/Критерий Больцано–Коши для рядов]]", "[[en/Concepts/Bolzano–Cauchy criterion for series]]"]
status: draft
---

# Criterio de Bolzano–Cauchy para series

> [!theorem] Criterio de Bolzano–Cauchy
> La serie $\sum_{n=1}^{\infty}a_n$ converge si y solo si
> $$\forall\varepsilon>0\ \exists N\in\mathbb{N}\ \forall n>N\ \forall p>0:\ \left|\sum_{k=n+1}^{n+p}a_k\right|<\varepsilon.$$

> [!proof]- Demostración tal como está en los apuntes
> Por definición, la convergencia de la serie equivale a la existencia de límite finito de $S_m=\sum_{n=1}^{m}a_n$; se aplica el criterio de Bolzano–Cauchy a $\{S_m\}$. Sin pérdida de generalidad $m>n$, y con $p:=m-n$ se obtiene $S_m-S_n=\sum_{k=n+1}^{m}a_k$. $\blacksquare$

## Relaciones

- [[Propiedades de las series convergentes]]
- [[Convergencia absoluta]]

> [!warning] Marcas abiertas: ⟦T078⟧, ⟦T080⟧, ⟦U079⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Критерий Больцано–Коши для рядов — `ru/Понятия/Критерий Больцано–Коши для рядов.md`
- en: Bolzano–Cauchy criterion for series — `en/Concepts/Bolzano–Cauchy criterion for series.md`
