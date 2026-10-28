---
title: "Los números reales y la completitud"
lang: es
chapter: 2
part: "Fundamentos"
aliases: ["Los números reales y la completitud (es)"]
tags: [mathinmind/es, mathinmind/chapter]
---
# 2. Los números reales y la completitud

[[es/01-logic-sets-functions|← 1. Lógica, conjuntos y funciones]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/03-sequences|3. Sucesiones y límites →]]

> [!abstract] Objetivo
> Comprender las propiedades algebraicas, de orden y de completitud que distinguen $\mathbb R$ de $\mathbb Q$.

## 2.1 Cuerpo ordenado

Los números reales forman un cuerpo: la suma y el producto son asociativos y conmutativos, cumplen la distributividad y tienen elementos neutros e inversos (salvo la división entre cero). El orden $<$ es compatible:

$$
a<b\implies a+c<b+c,
$$
$$
a<b,\ c>0\implies ac<bc.
$$

Al multiplicar por un número negativo se invierte la desigualdad. El valor absoluto es

$$
|x|=\begin{cases}x,&x\ge0,\\-x,&x<0.\end{cases}
$$

Para todos $x,y\in\mathbb R$,

$$
|xy|=|x|\,|y|,\qquad |x+y|\le |x|+|y|,
$$

y vale la desigualdad triangular inversa $\bigl||x|-|y|\bigr|\le |x-y|$. Geométricamente, $|x-y|$ es una distancia.

## 2.2 Supremo e ínfimo

Sea $\varnothing\ne A\subseteq\mathbb R$. Un número $u$ es una **cota superior** si $a\le u$ para todo $a\in A$. El **supremo** $\sup A$ es la menor cota superior; el ínfimo es la mayor cota inferior.

> [!axiom] Axioma de completitud
> Todo subconjunto no vacío de $\mathbb R$ acotado superiormente tiene supremo en $\mathbb R$.

^completeness-axiom

Equivalentemente, todo conjunto no vacío acotado inferiormente tiene ínfimo. El supremo no tiene que pertenecer al conjunto: $\sup(0,1)=1$; un máximo sí debe pertenecer.

Una caracterización útil es

$$
u=\sup A\iff
\begin{cases}
a\le u\quad(a\in A),\\
\forall\varepsilon>0\;\exists a\in A:a>u-\varepsilon.
\end{cases}
$$

El conjunto $\{q\in\mathbb Q:q^2<2\}$ no tiene supremo racional, por lo que $\mathbb Q$ no es completo.

## 2.3 Consecuencias de la completitud

> [!theorem] Propiedad arquimediana
> Para todo $x\in\mathbb R$ existe $n\in\mathbb N$ con $n>x$. Equivalentemente, para todo $\varepsilon>0$ hay $n$ tal que $1/n<\varepsilon$.

^archimedean-property

Si $\mathbb N$ estuviera [[#2.2 Supremo e ínfimo|acotado superiormente]], su supremo $s$ cumpliría $s-1<n<s$ para algún entero $n$, lo que daría $n+1>s$, una contradicción.

> [!theorem] Densidad de los racionales
> Si $a<b$, existe $q\in\mathbb Q$ con $a<q<b$.

^density-of-rationals

Elige $n$ con $n(b-a)>1$ y un entero $m$ entre $na$ y $nb$; entonces $q=m/n$ sirve. Los irracionales también son densos: $q+\sqrt2/k$ puede situarse en cualquier intervalo.

## 2.4 Intervalos encajados

Una sucesión de intervalos cerrados y acotados $I_n=[a_n,b_n]$ está **encajada** si $I_{n+1}\subseteq I_n$.

> [!theorem] Teorema de los intervalos encajados
> Si los $I_n$ están encajados, entonces $\bigcap_{n=1}^{\infty}I_n\ne\varnothing$. Si $b_n-a_n\to0$, la intersección contiene exactamente un punto.

^nested-interval-theorem

En efecto, $a=\sup\{a_n\}$ pertenece a todos los intervalos. El cierre y la acotación son esenciales: los $(0,1/n)$ tienen intersección vacía, al igual que los $[n,\infty)$.

La recta ampliada $\overline{\mathbb R}=\mathbb R\cup\{-\infty,+\infty\}$ resulta útil para supremos de conjuntos no acotados, pero $\infty-\infty$ sigue sin estar definido.

## Ejemplo resuelto

Sea $A=\{1-1/n:n\in\mathbb N\}$. Todos sus elementos son menores que $1$. Para cada $\varepsilon>0$, la [[#^archimedean-property|propiedad arquimediana]] da $1/n<\varepsilon$, luego $1-1/n>1-\varepsilon$. Por tanto $\sup A=1$. Como $1\notin A$, no hay máximo.

## Errores frecuentes

1. «Acotado» significa acotado superior e inferiormente.
2. $\sup A$ puede estar fuera de $A$; $\max A$ no.
3. El [[#^nested-interval-theorem|teorema de intervalos encajados]] exige intervalos cerrados y acotados.

## Ejercicios

1. Demuestra $\sup(A+B)=\sup A+\sup B$ para conjuntos no vacíos y acotados, donde $A+B=\{a+b:a\in A,b\in B\}$.
2. Prueba que entre dos números reales cualesquiera hay un irracional.
3. Calcula $\sup\{x\in\mathbb R:x^2+x<2\}$ y decide si es un máximo.

> [!answer]- Respuestas breves
> 1. La suma es una cota superior; aproxima ambos supremos con error $\varepsilon/2$.
> 2. Elige un racional $q$ adecuado y $k$ suficientemente grande; considera $q+\sqrt2/k$.
> 3. El conjunto es $(-2,1)$; el supremo es $1$ y no es máximo.

---

[[es/01-logic-sets-functions|← 1. Lógica, conjuntos y funciones]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/03-sequences|3. Sucesiones y límites →]]
