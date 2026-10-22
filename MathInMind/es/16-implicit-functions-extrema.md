---
title: "Funciones inversas e implícitas; extremos"
lang: es
chapter: 16
part: "Varias variables y topología"
---
# 16. Funciones inversas e implícitas; extremos

[Anterior](15-multivariable-differentiation.md) · [Índice](index.md) · [Siguiente](17-multiple-integrals.md)

> **Objetivo.** Aplicar condiciones de no degeneración de la derivada y hallar extremos locales o condicionados sistemáticamente.

## 16.1 Extremos locales sin restricciones

Sea $f$ derivable en un abierto. Si tiene un extremo local en un punto interior $a$, entonces $\nabla f(a)=0$. Estos puntos se llaman estacionarios o críticos. Los puntos frontera se estudian por separado.

Para $f\in C^2$, se examina la hessiana $H=Hf(a)$ en un punto crítico:

- $H$ definida positiva $\implies$ mínimo local estricto;
- $H$ definida negativa $\implies$ máximo local estricto;
- $H$ indefinida $\implies$ punto de silla;
- $H$ semidefinida o singular $\implies$ el criterio no decide.

En dos variables, con $D=f_{xx}f_{yy}-f_{xy}^2$: mínimo si $D>0$ y $f_{xx}>0$; máximo si $D>0$ y $f_{xx}<0$; silla si $D<0$.

Por ejemplo, $f(x,y)=x^2-y^2$ tiene hessiana $\operatorname{diag}(2,-2)$ en el origen, luego una silla. Las funciones $x^4+y^4$ y $-x^4-y^4$ muestran por qué $D=0$ exige más análisis.

## 16.2 Teorema de la función inversa

> **Teorema.** Sea $F:\mathbb R^n\to\mathbb R^n$ de clase $C^1$ cerca de $a$, con $DF(a)$ invertible. Entonces $F$ aplica biyectivamente un entorno de $a$ sobre un entorno de $F(a)$, la inversa es $C^1$ y
> $$DF^{-1}(F(a))=(DF(a))^{-1}.$$

En coordenadas, la condición es $\det DF(a)\ne0$. El teorema es local: un jacobiano no nulo en todas partes no implica por sí solo inyectividad global.

Explica cuándo un cambio de coordenadas es localmente reversible y fundamenta el teorema de la función implícita.

## 16.3 Teorema de la función implícita

Supongamos que $F(x,y)$ toma valores en $\mathbb R^k$, con $x\in\mathbb R^n$ e $y\in\mathbb R^k$. Si $F$ es $C^1$, $F(a,b)=0$ y la jacobiana parcial $D_yF(a,b)$ es invertible, entonces cerca de $(a,b)$ la ecuación

$$
F(x,y)=0
$$

define $y$ únicamente como función $C^1$, $y=g(x)$, con $g(a)=b$. Además,

$$
Dg(a)=-(D_yF(a,b))^{-1}D_xF(a,b).
$$

Para una ecuación $F(x,y)=0$ con $F_y\ne0$, se reduce a

$$
\frac{dy}{dx}=-\frac{F_x}{F_y}.
$$

El teorema garantiza existencia y suavidad, no necesariamente una fórmula elemental explícita.

## 16.4 Multiplicadores de Lagrange

Para una restricción suave $g(x)=c$, supongamos $\nabla g(a)\ne0$. Si $f$ tiene un extremo local en la superficie de restricción en $a$, existe $\lambda$ tal que

$$
\nabla f(a)=\lambda\nabla g(a),\qquad g(a)=c.
$$

Geométricamente, ambos gradientes son normales a la misma superficie de nivel y deben ser paralelos. Para varias restricciones independientes $g_1,\ldots,g_k$,

$$
\nabla f(a)=\sum_{i=1}^{k}\lambda_i\nabla g_i(a),
$$

siempre que los gradientes sean linealmente independientes.

La condición es necesaria, no siempre suficiente. Compara todos los puntos críticos, puntos singulares donde falla el rango y el comportamiento frontera; usa compacidad para extremos globales cuando proceda.

## Ejemplo resuelto

Optimizamos $f(x,y)=x+y$ con $x^2+y^2=1$. Las ecuaciones de Lagrange dan

$$
1=2\lambda x,\qquad 1=2\lambda y,
$$

así que $x=y$. En la circunferencia aparecen $\pm(1/\sqrt2,1/\sqrt2)$. El máximo es $\sqrt2$ y el mínimo $-\sqrt2$. Coincide con Cauchy–Schwarz: $|x+y|\le\sqrt2\sqrt{x^2+y^2}$.

## Errores frecuentes

1. Un punto crítico no es automáticamente un extremo.
2. Lagrange exige una restricción no degenerada y no sustituye la comparación de candidatos.
3. Los teoremas de funciones inversa e implícita son locales.

## Ejercicios

1. Clasifica el origen para $f(x,y)=x^2+2y^2$.
2. Para $x^2+y^2=1$ cerca de $(0,1)$, halla $dy/dx$ implícitamente.
3. Halla los extremos de $xy$ en $x^2+y^2=1$.

<details>
<summary>Respuestas breves</summary>

1. La hessiana $\operatorname{diag}(2,4)$ es definida positiva: mínimo local y global estricto.
2. $2x+2yy'=0$, luego $y'=-x/y$ e $y'(0)=0$ en $(0,1)$.
3. Máximo $1/2$ en $x=y=1/\sqrt2$ o $x=y=-1/\sqrt2$; mínimo $-1/2$ con signos opuestos.
</details>

---

[Anterior](15-multivariable-differentiation.md) · [Índice](index.md) · [Siguiente](17-multiple-integrals.md)
