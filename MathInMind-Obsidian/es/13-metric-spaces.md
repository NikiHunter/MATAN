---
title: "Espacios métricos, compacidad y completitud"
lang: es
chapter: 13
part: "Varias variables y topología"
aliases: ["Espacios métricos, compacidad y completitud (es)"]
tags: [mathinmind/es, mathinmind/chapter]
---
# 13. Espacios métricos, compacidad y completitud

[[es/12-fourier-series|← 12. Series de Fourier]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/14-several-variables|14. Funciones de varias variables →]]

> [!abstract] Objetivo
> Generalizar el análisis basado en distancias y comprender [[#13.4 Compacidad|compacidad]] y completitud como propiedades estructurales.

## 13.1 Métricas y ejemplos

Una métrica en $X$ es una función $d:X\times X\to[0,\infty)$ que cumple

1. $d(x,y)=0\iff x=y$;
2. $d(x,y)=d(y,x)$;
3. $d(x,z)\le d(x,y)+d(y,z)$.

El par $(X,d)$ es un espacio métrico. Ejemplos importantes:

$$
d_2(x,y)=\|x-y\|_2\quad\text{en }\mathbb R^n,
$$
$$
d_1(x,y)=\sum_{i=1}^{n}|x_i-y_i|,
\qquad
d_\infty(x,y)=\max_i|x_i-y_i|,
$$

y la métrica discreta $d(x,y)=1$ si $x\ne y$. En $C([a,b])$, $d_\infty(f,g)=\max_{x\in[a,b]}|f(x)-g(x)|$ describe [[es/10-function-sequences-series#10.1 Dos modos de convergencia|convergencia uniforme]].

## 13.2 Conjuntos abiertos y cerrados

La bola abierta es $B_r(x)=\{y\in X:d(x,y)<r\}$. Un conjunto $U$ es **abierto** si cada $x\in U$ tiene una bola $B_r(x)\subseteq U$. Un conjunto es **cerrado** si su complemento es abierto.

Uniones arbitrarias e intersecciones finitas de abiertos son abiertas. Intersecciones arbitrarias y uniones finitas de cerrados son cerradas.

El interior $A^\circ$ es el mayor abierto contenido en $A$. La clausura $\overline A$ es el menor cerrado que contiene $A$, y

$$
x\in\overline A\iff \forall r>0\;B_r(x)\cap A\ne\varnothing.
$$

La frontera es $\partial A=\overline A\setminus A^\circ$. Un conjunto $A$ es denso en $X$ si $\overline A=X$; por ejemplo, $\mathbb Q$ es denso en $\mathbb R$.

## 13.3 Convergencia y completitud

Una sucesión $x_n$ converge a $x$ si $d(x_n,x)\to0$. Es de Cauchy si para todo $\varepsilon>0$ existe $N$ tal que $d(x_m,x_n)<\varepsilon$ para $m,n\ge N$.

Un [[#13.1 Métricas y ejemplos|espacio métrico]] es **completo** si toda [[es/03-sequences#3.4 Subsucesiones y sucesiones de Cauchy|sucesión de Cauchy]] converge en él. Los espacios $\mathbb R^n$ y $(C([a,b]),d_\infty)$ son completos; $\mathbb Q$ con su métrica usual no lo es. Un subespacio cerrado de uno completo es completo.

Todo espacio métrico tiene una completación: un espacio completo que contiene una copia isométrica y densa del original. Esto abstrae la construcción de $\mathbb R$ a partir de $\mathbb Q$.

## 13.4 Compacidad

Un conjunto $K$ es **compacto** si todo recubrimiento abierto tiene un subrecubrimiento finito. En espacios métricos equivale a compacidad secuencial: toda sucesión en $K$ tiene una subsucesión convergente en $K$.

> [!theorem] Teorema de Heine–Borel
> En $\mathbb R^n$, un conjunto es compacto exactamente cuando es cerrado y acotado.

^heine-borel-theorem

En espacios métricos generales, cerrado y acotado no basta. La caracterización general es completo y totalmente acotado: para todo $\varepsilon>0$ se puede cubrir con finitas bolas de radio $\varepsilon$.

Los compactos son cerrados y acotados. La imagen continua de un compacto es compacta, lo que da el [[es/05-limits-continuity#^extreme-value-theorem|teorema de Weierstrass]]. Un compacto en un espacio de Hausdorff, y por tanto métrico, es cerrado.

```mermaid
flowchart LR
    A[Compacidad] --> B[Cerrado y acotado]
    A --> C[Compacidad secuencial]
    A --> D[Imagen continua compacta]
    E[Completo y totalmente acotado] --> A
```

## 13.5 Continuidad y conexión

Para $f:X\to Y$, continuidad en $a$ significa

$$
\forall\varepsilon>0\;\exists\delta>0:
d_X(x,a)<\delta\implies d_Y(f(x),f(a))<\varepsilon.
$$

Globalmente, $f$ es continua exactamente cuando $f^{-1}(V)$ es abierto para todo abierto $V\subseteq Y$. Las funciones continuas en compactos son [[es/05-limits-continuity#5.4 Continuidad uniforme|uniformemente continuas]].

Un espacio es **conexo** si no puede dividirse en dos abiertos no vacíos y disjuntos. Los subconjuntos conexos de $\mathbb R$ son exactamente los intervalos. Las imágenes continuas de conexos son conexas, lo que da el valor intermedio.

> [!theorem] Teorema de Baire
> En un [[#13.3 Convergencia y completitud|espacio métrico completo]], una intersección [[es/01-logic-sets-functions#1.5 Numerabilidad|numerable]] de abiertos densos es densa. Es una herramienta importante de existencia.

^baire-category-theorem

## Ejemplo resuelto

En la métrica discreta, $B_{1/2}(x)=\{x\}$, así que todo subconjunto es abierto y cerrado. Una sucesión converge exactamente cuando es finalmente constante. El espacio es completo, pero uno discreto infinito no es compacto: el recubrimiento por singletes no tiene subrecubrimiento finito.

## Errores frecuentes

1. Un conjunto puede ser abierto y cerrado a la vez.
2. La completitud depende de la métrica y del espacio ambiente.
3. Cerrado y acotado implica compacto en $\mathbb R^n$, no en todo espacio métrico.

## Ejercicios

1. Describe la convergencia en un espacio métrico discreto.
2. Halla interior, [[#13.2 Conjuntos abiertos y cerrados|clausura]] y frontera de $(0,1)$ en $\mathbb R$.
3. Prueba que un espacio métrico compacto está acotado.

> [!answer]- Respuestas breves
> 1. Convergen exactamente las sucesiones finalmente constantes.
> 2. Interior $(0,1)$, clausura $[0,1]$, frontera $\{0,1\}$.
> 3. Cubre el espacio con bolas $B_n(x_0)$ de radios enteros y extrae un subrecubrimiento finito.

---

[[es/12-fourier-series|← 12. Series de Fourier]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/14-several-variables|14. Funciones de varias variables →]]
