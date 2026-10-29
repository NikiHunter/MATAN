---
id: harmonic-series
type: example
semester: 3
lang: es
aliases: []
tags: [analysis/series, sem3, example]
source_pages: [p019]
translations: ["[[ru/Понятия/Гармонический ряд]]", "[[en/Concepts/Harmonic series]]"]
status: draft
---

# Serie armónica

> [!example] Serie armónica
> $$\sum_{k=1}^{\infty}\frac{1}{k}=1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\ldots$$
> diverge, aunque $a_k=\dfrac{1}{k}\to0$.

Demostración de los apuntes: agrupando los términos,
$$S_{2^m}=1+\frac{1}{2}+\left(\frac{1}{3}+\frac{1}{4}\right)+\ldots+\left(\frac{1}{2^{m-1}+1}+\ldots+\frac{1}{2^m}\right)\ge1+\frac{1}{2}+\frac{1}{2}+\ldots+\frac{1}{2}=1+\frac{m}{2},$$
por lo que $S_{2^m}\to+\infty$ y la serie diverge.

> [!warning] Es un contraejemplo al recíproco de la propiedad 1: $a_n\to0$ no implica convergencia.

## Relaciones

- [[Propiedades de las series convergentes]]
- [[Convergencia de una serie numérica]]

> [!warning] Marcas abiertas: ⟦M071⟧, ⟦U072⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Гармонический ряд — `ru/Понятия/Гармонический ряд.md`
- en: Harmonic series — `en/Concepts/Harmonic series.md`
