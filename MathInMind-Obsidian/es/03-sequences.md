---
title: "Sucesiones y límites"
lang: es
chapter: 3
part: "Fundamentos"
aliases: ["Sucesiones y límites (es)"]
tags: [mathinmind/es, mathinmind/chapter]
---
# 3. Sucesiones y límites

[[es/02-real-numbers|← 2. Los números reales y la completitud]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/04-numeric-series|4. Series numéricas →]]

> [!abstract] Objetivo
> Demostrar convergencia, aplicar los criterios de monotonía y de Cauchy, y controlar [[#3.4 Subsucesiones y sucesiones de Cauchy|subsucesiones]].

## 3.1 Definición de límite

Una sucesión es una función $a:\mathbb N\to\mathbb R$, escrita $(a_n)$. Converge a $L$ si

$$
\forall\varepsilon>0\;\exists N\in\mathbb N\;\forall n\ge N:
|a_n-L|<\varepsilon.
$$

Escribimos $a_n\to L$. El número $N$ puede depender de $\varepsilon$, pero no de $n$. Si no existe límite finito, la sucesión diverge.

Para probar $1/n\to0$, elige $N>1/\varepsilon$. Para $(2n+1)/(n+3)\to2$, estima

$$
\left|\frac{2n+1}{n+3}-2\right|=\frac5{n+3}<\frac5n.
$$

Una sucesión convergente tiene límite único y está acotada. Si $a_n\to L$, toda subsucesión también converge a $L$.

## 3.2 Álgebra de límites

Si $a_n\to a$ y $b_n\to b$, entonces

$$
a_n\pm b_n\to a\pm b,\qquad a_nb_n\to ab,
$$

y $a_n/b_n\to a/b$ si $b\ne0$ y $b_n\ne0$ a partir de cierto índice. Si $a_n\le c_n\le b_n$ y ambas sucesiones exteriores tienden a $L$, entonces $c_n\to L$ (teorema del emparedado).

Si $a_n\ge0$ finalmente y $a_n\to a$, entonces $a\ge0$. Las desigualdades estrictas pueden perderse: $1/n>0$, pero su límite es cero.

Escribimos $a_n\to+\infty$ si para todo $M$ existe $N$ tal que $a_n>M$ para $n\ge N$. Es una forma especial de divergencia, no convergencia en $\mathbb R$.

## 3.3 Convergencia monótona

> [!theorem] Teorema de convergencia monótona
> Toda sucesión creciente [[es/02-real-numbers#2.2 Supremo e ínfimo|acotada superiormente]] converge a su supremo; toda decreciente acotada inferiormente converge a su ínfimo.

^monotone-convergence-theorem

Para una sucesión creciente acotada, sea $L=\sup\{a_n\}$. Dado $\varepsilon>0$, existe $a_N>L-\varepsilon$; por monotonía, todos los términos posteriores quedan en $(L-\varepsilon,L]$.

En una sucesión recurrente, demuestra primero acotación y monotonía y después pasa al límite. Por ejemplo, $a_1=1$, $a_{n+1}=\sqrt{2+a_n}$ es creciente y está acotada por $2$. Su límite $L$ cumple $L=\sqrt{2+L}$, de donde $L=2$.

## 3.4 Subsucesiones y sucesiones de Cauchy

> [!theorem] Teorema de Bolzano–Weierstrass
> Toda sucesión acotada en $\mathbb R$ tiene una subsucesión convergente.

^bolzano-weierstrass-theorem

Una sucesión es **de Cauchy** si

$$
\forall\varepsilon>0\;\exists N\;\forall m,n\ge N:|a_n-a_m|<\varepsilon.
$$

Toda [[#3.1 Definición de límite|sucesión convergente]] es de Cauchy. Recíprocamente, una sucesión de Cauchy está acotada y tiene una subsucesión convergente; la condición de Cauchy obliga a toda la sucesión a tender al mismo límite. Así,

$$
(a_n)\text{ converge}\iff(a_n)\text{ es de Cauchy}.
$$

Este criterio permite demostrar convergencia sin conocer antes el límite.

## 3.5 Límite superior e inferior

Para una sucesión acotada, definimos

$$
\limsup_{n\to\infty}a_n=\lim_{n\to\infty}\sup_{k\ge n}a_k,
\qquad
\liminf_{n\to\infty}a_n=\lim_{n\to\infty}\inf_{k\ge n}a_k.
$$

Estos límites existen porque los supremos de las colas decrecen y los ínfimos crecen. Siempre $\liminf a_n\le\limsup a_n$; hay igualdad exactamente cuando la sucesión converge, y el valor común es su límite.

Para $a_n=(-1)^n$, el límite superior es $1$ y el inferior $-1$. Las definiciones se extienden a sucesiones no acotadas mediante $\pm\infty$.

## Errores frecuentes

1. La acotación por sí sola no implica convergencia.
2. Una subsucesión convergente no obliga a converger a toda la sucesión.
3. Antes de resolver la ecuación de un límite recurrente hay que demostrar que existe.

## Ejercicios

1. Prueba por definición que $(3n-2)/(2n+5)\to3/2$.
2. Demuestra que $a_n=(1+1/n)^n$ converge estableciendo que es creciente y está acotada superiormente.
3. Halla los límites superior e inferior de $a_n=(-1)^n+1/n$.

> [!answer]- Respuestas breves
> 1. El error absoluto es $19/(2(2n+5))$, menor que $5/n$; elige $N>5/\varepsilon$.
> 2. Se aplica el [[#^monotone-convergence-theorem|teorema de convergencia monótona]]; el límite se denota $e$.
> 3. Las subsucesiones par e impar tienden a $1$ y $-1$, respectivamente.

---

[[es/02-real-numbers|← 2. Los números reales y la completitud]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/04-numeric-series|4. Series numéricas →]]
