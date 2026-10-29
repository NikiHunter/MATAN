---
id: lagrange-multipliers
type: theorem
semester: 3
lang: es
aliases: ["condición necesaria de extremo condicional"]
tags: [analysis/extrema, sem3, theorem]
source_pages: [p015, p016, p017]
translations: ["[[ru/Понятия/Множители Лагранжа]]", "[[en/Concepts/Lagrange multipliers]]"]
status: draft
---

# Multiplicadores de Lagrange

Se escribe $\Phi=(\varphi_1,\ldots,\varphi_m)$, es decir $\Phi: E\subset\mathbb{R}^n\to\mathbb{R}^m$.

> [!theorem] Teorema 6.7.3
> Sean $m,n\in\mathbb{N}$, $m<n$, $E$ abierto en $\mathbb{R}^n$, $a\in E$, $f\in C^1(E)$, $\Phi\in C^1(E,\mathbb{R}^m)$, $\operatorname{rank}\Phi'(a)=m$. Si $a$ es un punto de extremo condicional de $f$ sujeto a $\Phi=0$, entonces existen $\lambda_1,\ldots,\lambda_m\in\mathbb{R}$ tales que
> $$\operatorname{grad}f(a)=\sum_{k=1}^{m}\lambda_k\operatorname{grad}\varphi_k(a). \tag{6.7.1}$$

Los números $\lambda_1,\ldots,\lambda_m$ que satisfacen (6.7.1) se llaman multiplicadores de Lagrange.

> [!proof]- Esquema de los apuntes
> Los puntos de $\mathbb{R}^n$ se escriben como $(x,y)$ con $x\in\mathbb{R}^{n-m}$, $y\in\mathbb{R}^m$, y $a=(x^0,y^0)$; el conjunto $M=\{(x,y)\in E:\ \varphi_k(x,y)=0\}$ es localmente una gráfica: $M\cap V(a)=\{(x,\psi(x))\}$.
>
> Como $f|_M$ tiene un extremo en $a$, la función $F(x)=f(x,\psi(x))$ tiene un extremo en $x^0$, luego $\nabla F(x^0)=0$ y $f'_x(a)+f'_y(a)\psi'(x^0)=0$. De $\Phi(x,\psi(x))=0$ se sigue $\Phi'_x(a)+\Phi'_y(a)\psi'(x^0)=0$. Con $\lambda=f'_y(a)[\Phi'_y(a)]^{-1}$ se anulan ambos sumandos de $[f'_x-\lambda\Phi'_x]+[f'_y-\lambda\Phi'_y]\psi'=0$, lo que da (6.7.1). $\blacksquare$

## Relaciones

- [[Extremo condicional]]
- [[Función de Lagrange]]
- [[Condición suficiente de extremo condicional]]

> [!warning] Marcas abiertas: ⟦U059⟧, ⟦U061⟧, ⟦S062⟧, ⟦A063⟧, ⟦S064⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Множители Лагранжа — `ru/Понятия/Множители Лагранжа.md`
- en: Lagrange multipliers — `en/Concepts/Lagrange multipliers.md`
