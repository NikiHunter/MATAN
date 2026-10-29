---
id: conditional-extremum-sufficient
type: theorem
semester: 3
lang: es
aliases: []
tags: [analysis/extrema, sem3, theorem]
source_pages: [p018]
translations: ["[[ru/Понятия/Достаточное условие условного экстремума]]", "[[en/Concepts/Sufficient condition for a conditional extremum]]"]
status: draft
---

# Condición suficiente de extremo condicional

> [!theorem] Teorema 6.7.5
> Sean $m,n\in\mathbb{N}$, $m<n$, $E$ abierto en $\mathbb{R}^n$, $a\in E$, $f\in C^2(E)$, $\Phi\in C^2(E,\mathbb{R}^m)$, $\Phi(a)=0$, $\operatorname{rank}\Phi'(a)=m$. Se pone
> $$N=\{h\in\mathbb{R}^n:\ d_a\Phi(h)=0\},\qquad L(x)=f(x)-\sum_{k=1}^{m}\lambda_k\varphi_k(x),$$
> donde $\lambda_1,\ldots,\lambda_m$ satisfacen (6.7.1) en $a$. Entonces:
> 1) si $d_a^2L$ es definida positiva (negativa) en $N$, entonces $f$ tiene en $a$ un mínimo (máximo) condicional sujeto a $\Phi=0$;
> 2) si $d_a^2L$ toma en $N$ valores de ambos signos, entonces $f$ no tiene en $a$ extremo condicional.

## Relaciones

- [[Multiplicadores de Lagrange]]
- [[Definición de una forma cuadrática en un subespacio]]

> [!warning] Marcas abiertas: ⟦S067⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Достаточное условие условного экстремума — `ru/Понятия/Достаточное условие условного экстремума.md`
- en: Sufficient condition for a conditional extremum — `en/Concepts/Sufficient condition for a conditional extremum.md`
