---
id: taylor-remainder-estimate
type: theorem
semester: 3
lang: es
aliases: []
tags: [analysis/taylor, sem3, theorem]
source_pages: [p006, p007]
translations: ["[[ru/Понятия/Оценка остатка в формуле Тейлора]]", "[[en/Concepts/Estimate of the Taylor remainder]]"]
status: draft
---

# Estimación del resto de Taylor

El resto en la fórmula de Taylor es $R_{a,s}f=f-T_{a,s}f$; el teorema 6.5.1 puede escribirse como $R_{a,s}f(x)=o(\|x-a\|^s)$ cuando $x\to a$.

> [!theorem] Teorema 6.5.5
> Sean $E$ abierto en $\mathbb{R}^n$, $s\in\mathbb{Z}_+$, $f\in C^{s+1}(E,\mathbb{R}^m)$, $a,x\in E$ con $a\neq x$ y $\Delta_{a,x}\subset E$. Sea
> $$M=\max_{\alpha\in M_{s+1}}\sup_{c\in\hat{\Delta}_{a,x}}\left\|\frac{\partial^\alpha f}{\partial x^\alpha}(c)\right\|.$$
> Entonces $M<\infty$ y
> $$\left\|R_{a,s}f(x)\right\|\le\frac{M}{(s+1)!}\left(\sqrt{n}\,\|x-a\|\right)^{s+1}.$$

Para funciones los apuntes recogen el corolario del teorema 6.5.2: $\left|R_{a,s}f(x)\right|\le\sup_{c\in\hat{\Delta}_{a,x}}\dfrac{\left|d_c^{s+1}f(x-a)\right|}{(s+1)!}$.

## Relaciones

- [[Teorema de Taylor–Lagrange para aplicaciones]]
- [[Teorema de Taylor–Peano]]

> [!warning] Marcas abiertas: ⟦A030⟧, ⟦T022⟧, ⟦U029⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Оценка остатка в формуле Тейлора — `ru/Понятия/Оценка остатка в формуле Тейлора.md`
- en: Estimate of the Taylor remainder — `en/Concepts/Estimate of the Taylor remainder.md`
