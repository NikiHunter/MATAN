---
id: lagrange-function
type: property
semester: 3
lang: es
aliases: ["lagrangiano"]
tags: [analysis/extrema, sem3, property]
source_pages: [p017]
translations: ["[[ru/Понятия/Функция Лагранжа]]", "[[en/Concepts/Lagrange function]]"]
status: draft
---

# Función de Lagrange

> [!theorem] Teorema 6.7.4
> Sean $m,n\in\mathbb{N}$, $m<n$, $E$ abierto en $\mathbb{R}^n$, $a\in E$, $f\in C^1(E)$, $\Phi\in C^1(E,\mathbb{R}^m)$, $\operatorname{rank}\Phi'(a)=m$. Si $a$ es un punto de extremo condicional de $f$ sujeto a $\Phi=0$ y
> $$L(x,\lambda)=f(x)-\sum_{k=1}^{m}\lambda_k\varphi_k(x)\quad (x\in E,\ \lambda\in\mathbb{R}^m),$$
> entonces existe $\lambda\in\mathbb{R}^m$ tal que $\operatorname{grad}L(a,\lambda)=0$.

Es una reformulación del teorema 6.7.3 mediante la función de Lagrange: la condición (6.7.1) equivale a la estacionariedad de $L$ en $x$.

## Relaciones

- [[Multiplicadores de Lagrange]]
- [[Condición suficiente de extremo condicional]]

> [!warning] Marcas abiertas: ⟦T065⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Функция Лагранжа — `ru/Понятия/Функция Лагранжа.md`
- en: Lagrange function — `en/Concepts/Lagrange function.md`
