---
id: implicit-mapping-theorem
type: theorem
semester: 3
lang: es
aliases: []
tags: [analysis/implicit, sem3, theorem]
source_pages: [p009]
translations: ["[[ru/Понятия/Теорема о неявном отображении]]", "[[en/Concepts/Implicit mapping theorem]]"]
status: draft
---

# Teorema de la aplicación implícita

> [!theorem] Teorema 6.6.1
> Sean $E$ abierto en $\mathbb{R}^{n+m}$, $(x^0,y^0)\in E$, $s\in\mathbb{N}$, $f\in C^s(E,\mathbb{R}^m)$, con $f(x^0,y^0)=0$ y $\det f'_y(x^0,y^0)\neq0$. Entonces existen un entorno $V(x^0,y^0)$, un abierto $U$ que contiene $x^0$ y una aplicación $\varphi\in C^s(U,\mathbb{R}^m)$ tales que
> $$\{(x,y)\in V(x^0,y^0):\ f(x,y)=0\}=\{(x,\varphi(x)):\ x\in U\}.$$

Así, el conjunto de soluciones de (6.6.3) cerca de $(x^0,y^0)$ es la gráfica de una aplicación $\varphi$ de la misma clase de suavidad que $f$.

![[p009_fig1.jpg]]

La figura de los apuntes va acompañada de $U\times\varphi(U)=V(x^0,y^0)$.

## Relaciones

- [[Función implícita]]
- [[Derivación de la aplicación implícita]]

> [!warning] Marcas abiertas: ⟦A034⟧, ⟦G038⟧, ⟦M060⟧, ⟦S035⟧, ⟦T037⟧, ⟦U036⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Теорема о неявном отображении — `ru/Понятия/Теорема о неявном отображении.md`
- en: Implicit mapping theorem — `en/Concepts/Implicit mapping theorem.md`
