---
title: "Teoría de la medida y funciones medibles"
lang: es
chapter: 19
part: "Análisis moderno"
aliases: ["Teoría de la medida y funciones medibles (es)"]
tags: [mathinmind/es, mathinmind/chapter]
---
# 19. Teoría de la medida y funciones medibles

[[es/18-vector-calculus|← 18. Cálculo vectorial y teoremas integrales]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/20-lebesgue-integration|20. Integración de Lebesgue y teoremas de convergencia →]]

> [!abstract] Objetivo
> Construir la noción de tamaño necesaria para una integración robusta e identificar las funciones compatibles con ella.

## 19.1 Sigma-álgebras

Una **$\sigma$-álgebra** en $X$ es una colección $\Sigma$ de subconjuntos tal que

1. $X\in\Sigma$;
2. $A\in\Sigma\implies A^c\in\Sigma$;
3. $A_1,A_2,\ldots\in\Sigma\implies\bigcup_{n=1}^{\infty}A_n\in\Sigma$.

Se deduce que $\varnothing\in\Sigma$ y que $\Sigma$ es cerrada bajo intersecciones [[es/01-logic-sets-functions#1.5 Numerabilidad|numerables]]. El par $(X,\Sigma)$ es un espacio [[#19.4 Funciones medibles|medible]] y los elementos de $\Sigma$ son conjuntos medibles.

Ejemplos: $\{\varnothing,X\}$ y $\mathcal P(X)$. La **$\sigma$-álgebra de Borel** $\mathcal B(X)$ en un espacio topológico es la menor que contiene todos los abiertos. En $\mathbb R$ está generada por intervalos.

## 19.2 Medidas

Una medida en $(X,\Sigma)$ es una función $\mu:\Sigma\to[0,\infty]$ con $\mu(\varnothing)=0$ y, para $A_n$ medibles disjuntos dos a dos,

$$
\mu\left(\bigcup_{n=1}^{\infty}A_n\right)
=\sum_{n=1}^{\infty}\mu(A_n).
$$

Esta es la aditividad numerable. Consecuencias inmediatas:

- monotonía: $A\subseteq B\implies\mu(A)\le\mu(B)$;
- subaditividad numerable: $\mu(\bigcup A_n)\le\sum\mu(A_n)$;
- continuidad por debajo: $A_n\uparrow A\implies\mu(A_n)\to\mu(A)$;
- continuidad por encima: $A_n\downarrow A$ y $\mu(A_1)<\infty$ implican $\mu(A_n)\to\mu(A)$.

La condición de finitud es esencial: con medida de conteo en $\mathbb N$, las colas $\{n,n+1,\ldots\}$ tienen medida infinita pero decrecen al vacío.

Ejemplos importantes: medida de conteo, medida de Dirac $\delta_x(A)=1_A(x)$ y [[#19.3 Medida de Lebesgue|medida de Lebesgue]].

## 19.3 Medida de Lebesgue

Una [[#19.2 Medidas|medida]] exterior $\mu^*$ está definida en todos los subconjuntos, es monótona y numerablemente subaditiva y asigna cero al vacío. Carathéodory declara $A$ medible si para todo conjunto de prueba $E$

$$
\mu^*(E)=\mu^*(E\cap A)+\mu^*(E\cap A^c).
$$

Los conjuntos medibles forman una $\sigma$-álgebra donde $\mu^*$ es numerablemente aditiva. Esta construcción produce la medida de Lebesgue a partir de longitudes de intervalos.

La medida de Lebesgue $\lambda_n$ en $\mathbb R^n$ es invariante por traslaciones y cumple

$$
\lambda_n([0,1]^n)=1.
$$

Todo boreliano es medible Lebesgue. Con el axioma de elección, no todo subconjunto de $\mathbb R$ es medible Lebesgue; los conjuntos de Vitali son el contraejemplo clásico.

Un conjunto $N$ es nulo si $\mu(N)=0$. Una propiedad vale **casi en todas partes (c.t.p.)** si falla solo en un conjunto nulo. La completación incluye todos los subconjuntos de conjuntos nulos medibles.

## 19.4 Funciones medibles

Una función $f:X\to\overline{\mathbb R}$ es medible si

$$
\{x:f(x)>\alpha\}\in\Sigma\qquad\text{para todo }\alpha\in\mathbb R.
$$

Hay condiciones equivalentes con $\ge\alpha$, $<\alpha$, $\le\alpha$ o imágenes inversas de borelianos. Las funciones continuas en espacios medibles de Borel son medibles.

Sumas, productos, múltiplos escalares y composiciones con funciones continuas adecuadas conservan medibilidad. Si $f_n$ son medibles, entonces

$$
\sup_n f_n,\quad \inf_n f_n,\quad \limsup_n f_n,\quad \liminf_n f_n
$$

son medibles. En particular, un límite puntual de funciones medibles es medible.

Una **función simple** tiene la forma $\varphi=\sum_{k=1}^{m}a_k1_{A_k}$ con $A_k$ medibles. Toda función medible no negativa es límite puntual creciente de funciones simples no negativas; esta aproximación conduce a la [[es/20-lebesgue-integration#20.1 Construcción de la integral|integral de Lebesgue]].

## Ejemplo resuelto

El indicador $1_{\mathbb Q}$ en $\mathbb R$ es medible porque $\mathbb Q$ es numerable, boreliano y de medida cero. Es igual a cero casi en todas partes aunque es discontinuo en todo punto. El conjunto de Cantor es [[es/13-metric-spaces#13.4 Compacidad|compacto]], no numerable y también tiene medida cero: medida nula no significa cardinal pequeño.

## Errores frecuentes

1. Medible no es sinónimo de boreliano; tras completar, la $\sigma$-álgebra de Lebesgue es mayor.
2. «Casi en todas partes» siempre se refiere a una medida especificada.
3. La aditividad numerable es más fuerte que la finita y esencial para los teoremas de límite.

## Ejercicios

1. Prueba que una $\sigma$-álgebra es cerrada bajo intersecciones numerables.
2. Muestra que todo subconjunto numerable de $\mathbb R$ tiene medida de Lebesgue cero.
3. Si $f$ es medible, prueba que $|f|$ es medible.

> [!answer]- Respuestas breves
> 1. Usa $\bigcap A_n=(\bigcup A_n^c)^c$.
> 2. Escribe el conjunto como unión numerable de singletes de medida cero y aplica aditividad numerable.
> 3. $\{|f|>\alpha\}$ es $X$ si $\alpha<0$ y $\{f>\alpha\}\cup\{f<-\alpha\}$ si $\alpha\ge0$.

---

[[es/18-vector-calculus|← 18. Cálculo vectorial y teoremas integrales]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/20-lebesgue-integration|20. Integración de Lebesgue y teoremas de convergencia →]]
