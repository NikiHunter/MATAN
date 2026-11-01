---
id: lemma-remainder-zero-derivatives
type: lemma
semester: 3
lang: es
aliases: ["lema del resto nulo"]
tags: [analysis/taylor, sem3, lemma]
source_pages: [p003, p004]
translations: ["[[ru/Понятия/Лемма 6.5.1]]", "[[en/Concepts/Lemma 6.5.1]]"]
status: draft
---

# Lema 6.5.1

> [!lemma] Lema 6.5.1
> Sean $E\subset\mathbb{R}^n$, $a$ un punto interior de $E$, $s\in\mathbb{N}$ y $f: E\to\mathbb{R}^m$ diferenciable en $a$, con $f$ y todas sus derivadas parciales de orden no mayor que $s$ iguales a cero en $a$. Entonces
> $$f(a+h)=o(\|h\|^s)\quad \text{cuando } h\to0.$$

> [!proof]- Esquema de los apuntes
> Basta comprobarlo para las funciones coordenadas, así que $m=1$; la demostración es por inducción en $s$.
>
> Base $s=1$: $f(a+h)=f(a)+\sum_{k=1}^{n}\dfrac{\partial f}{\partial x_k}(a)h_k+o(\|h\|)=o(\|h\|)$.
>
> Paso $s\mapsto s+1$: las derivadas parciales de primer orden son $s$ veces diferenciables, se les aplica la hipótesis de inducción y el lema 6.4.1 proporciona puntos $c^k\in V_\delta(a)$ que dan $\left|f(a+h)\right|\le\varepsilon\|h\|^{s+1}$. $\blacksquare$

## Relaciones

- [[Teorema de Taylor–Peano]]

> [!warning] Marcas abiertas: ⟦S013⟧, ⟦S015⟧, ⟦S017⟧, ⟦T014⟧, ⟦T016⟧, ⟦U012⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Лемма 6.5.1 — `ru/Понятия/Лемма 6.5.1.md`
- en: Lemma 6.5.1 — `en/Concepts/Lemma 6.5.1.md`
