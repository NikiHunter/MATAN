---
id: implicit-function-definition
type: definition
semester: 3
lang: es
aliases: ["aplicación implícita"]
tags: [analysis/implicit, sem3, definition]
source_pages: [p007, p008, p010]
translations: ["[[ru/Понятия/Неявная функция]]", "[[en/Concepts/Implicit function]]"]
status: draft
---

# Función implícita

Sea $f: E\subset\mathbb{R}^2\to\mathbb{R}$. Se considera la ecuación en las variables $x$ e $y$:
$$f(x,y)=0,\quad (x,y)\in E. \tag{6.6.1}$$

> [!definition] Definición 6.6.1
> La aplicación $\varphi$ introducida en el teorema 6.6.1 se llama aplicación implícita generada por la ecuación $f(x,y)=0$ en un entorno de $(x^0,y^0)$.

La ecuación (6.6.1) define una dependencia entre $x$ e $y$ que se llama implícita. Si una variable puede expresarse de forma única mediante la otra, el conjunto de soluciones tiene la forma $\{(x,y)\in E:\ y=\varphi(x)\}$ y $\varphi$ se llama función implícita generada por (6.6.1). Si cerca de cada punto de $E$ la ecuación genera una función implícita, se dice que es localmente resoluble.

Los apuntes recogen una condición suficiente de solubilidad local cerca de $a=(x^0,y^0)$: $\operatorname{grad}f(a)\neq0$.

## Relaciones

- [[Teorema de la aplicación implícita]]
- [[Derivación de la aplicación implícita]]

> [!warning] Marcas abiertas: ⟦A031⟧, ⟦U032⟧, ⟦A033⟧ — véase `ocr/ISSUES.md`

## Otros idiomas

- ru: Неявная функция — `ru/Понятия/Неявная функция.md`
- en: Implicit function — `en/Concepts/Implicit function.md`
