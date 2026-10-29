---
id: harmonic-series
type: example
semester: 3
lang: en
aliases: []
tags: [analysis/series, sem3, example]
source_pages: [p019]
translations: ["[[ru/Понятия/Гармонический ряд]]", "[[es/Conceptos/Serie armónica]]"]
status: draft
---

# Harmonic series

> [!example] Harmonic series
> $$\sum_{k=1}^{\infty}\frac{1}{k}=1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\ldots$$
> diverges, although $a_k=\dfrac{1}{k}\to0$.

Proof from the notes: grouping the terms,
$$S_{2^m}=1+\frac{1}{2}+\left(\frac{1}{3}+\frac{1}{4}\right)+\ldots+\left(\frac{1}{2^{m-1}+1}+\ldots+\frac{1}{2^m}\right)\ge1+\frac{1}{2}+\frac{1}{2}+\ldots+\frac{1}{2}=1+\frac{m}{2},$$
so $S_{2^m}\to+\infty$ and the series diverges.

> [!warning] This is a counterexample to the converse of property 1: $a_n\to0$ does not imply convergence.

## Related

- [[Properties of convergent series]]
- [[Convergence of a numeric series]]

> [!warning] Open markers: ⟦M071⟧, ⟦U072⟧ — see `ocr/ISSUES.md`

## Other languages

- ru: Гармонический ряд — `ru/Понятия/Гармонический ряд.md`
- es: Serie armónica — `es/Conceptos/Serie armónica.md`
