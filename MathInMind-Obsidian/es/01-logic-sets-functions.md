---
title: "Lógica, conjuntos y funciones"
lang: es
chapter: 1
part: "Fundamentos"
aliases: ["Lógica, conjuntos y funciones (es)"]
tags: [mathinmind/es, mathinmind/chapter]
---
# 1. Lógica, conjuntos y funciones

[[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/02-real-numbers|2. Los números reales y la completitud →]]

> [!abstract] Objetivo
> Leer enunciados con [[#1.1 Proposiciones y cuantificadores|cuantificadores]], construir demostraciones básicas y usar conjuntos y funciones con precisión.

## 1.1 Proposiciones y cuantificadores

Una **proposición** tiene un valor de verdad determinado. Para $P,Q$, los símbolos $\neg P$, $P\land Q$, $P\lor Q$ y $P\implies Q$ denotan negación, conjunción, disyunción e implicación. La implicación solo es falsa cuando $P$ es verdadera y $Q$ falsa.

Los cuantificadores se escriben

$$
\forall x\in A\;P(x),\qquad \exists x\in A\;P(x).
$$

Al negar se intercambian:

$$
\neg(\forall x\in A\;P(x))\iff \exists x\in A\;\neg P(x),
$$
$$
\neg(\exists x\in A\;P(x))\iff \forall x\in A\;\neg P(x).
$$

El orden importa. En $\forall x\,\exists y\,P(x,y)$, el valor $y$ puede depender de $x$; en $\exists y\,\forall x\,P(x,y)$, un mismo $y$ debe servir para todo $x$.

## 1.2 Métodos de demostración

- **Directa:** suponer $P$ y deducir $Q$.
- **Contrarrecíproca:** para probar $P\implies Q$, probar $\neg Q\implies\neg P$.
- **Contradicción:** suponer la negación del objetivo y obtener algo imposible.
- **Inducción:** probar $P(1)$ y $P(n)\implies P(n+1)$; entonces $P(n)$ vale para todo entero positivo. En la [[#^example-induction|inducción]] fuerte se usan todos los casos anteriores.
- **Existencia y unicidad:** construir un objeto y demostrar que dos objetos con esa propiedad coinciden.

> [!example] Ejemplo — inducción
> Para $n\ge1$, $1+2+\cdots+n=n(n+1)/2$. El caso inicial es inmediato. Si la fórmula vale para $n$, al sumar $n+1$ obtenemos
> $$
> \frac{n(n+1)}2+(n+1)=\frac{(n+1)(n+2)}2.
> $$

^example-induction

## 1.3 Conjuntos

Un conjunto está determinado por sus elementos. Las operaciones básicas son unión $A\cup B$, intersección $A\cap B$, diferencia $A\setminus B$ y complemento $A^c$ respecto de un universo fijo. Las leyes de De Morgan son

$$
(A\cup B)^c=A^c\cap B^c,\qquad (A\cap B)^c=A^c\cup B^c.
$$

El producto cartesiano $A\times B$ contiene pares ordenados $(a,b)$. Una relación en $A$ es un subconjunto de $A\times A$. Una relación de equivalencia es reflexiva, simétrica y transitiva; divide $A$ en clases de equivalencia.

Para una familia indexada,

$$
x\in\bigcup_{i\in I}A_i\iff \exists i\in I:x\in A_i,
\qquad
x\in\bigcap_{i\in I}A_i\iff \forall i\in I:x\in A_i.
$$

## 1.4 Funciones

Una función $f:A\to B$ asigna exactamente un valor $f(x)\in B$ a cada $x\in A$. El conjunto $A$ es el dominio y $B$ el codominio; el recorrido es $f(A)=\{f(x):x\in A\}$.

- $f$ es **inyectiva** si $f(x_1)=f(x_2)\implies x_1=x_2$;
- $f$ es **suprayectiva** si $f(A)=B$;
- $f$ es **biyectiva** si cumple ambas; entonces existe $f^{-1}:B\to A$.

Para $X\subseteq A$ e $Y\subseteq B$,

$$
f(X)=\{f(x):x\in X\},\qquad f^{-1}(Y)=\{x\in A:f(x)\in Y\}.
$$

La imagen inversa no exige que exista una función inversa. Las imágenes inversas conservan uniones, intersecciones y complementos; las imágenes directas conservan uniones, pero en general no intersecciones.

Si $g\circ f$ es inyectiva, $f$ es inyectiva. Si $g\circ f$ es suprayectiva, $g$ es suprayectiva.

## 1.5 Numerabilidad

Los conjuntos $A,B$ tienen el mismo cardinal si existe una [[#1.4 Funciones|biyección]] $A\to B$. Un conjunto es **numerable** si es finito o tiene el cardinal de $\mathbb N$. Así, $\mathbb Z$ y $\mathbb Q$ son numerables. El argumento diagonal de Cantor demuestra que $\mathbb R$ y el conjunto de sucesiones binarias infinitas no son numerables.

> [!theorem] Teorema de Cantor
> No existe una suprayección de $A$ sobre su conjunto potencia $\mathcal P(A)$. Dada $f:A\to\mathcal P(A)$, el conjunto $D=\{x\in A:x\notin f(x)\}$ no está en el recorrido: si $D=f(a)$, se obtiene $a\in D\iff a\notin D$.

^cantor-theorem

## Ejemplo resuelto

Sea $f:\mathbb R\to\mathbb R$, $f(x)=2x+3$. La ecuación $f(x)=y$ tiene la única solución $x=(y-3)/2$. Por tanto $f$ es biyectiva y $f^{-1}(y)=(y-3)/2$. En cambio, $x^2$ no es inyectiva ni suprayectiva en $\mathbb R$, pero sí es una biyección de $[0,\infty)$ sobre $[0,\infty)$.

## Errores frecuentes

1. Probar $P\implies Q$ no prueba $Q\implies P$.
2. Un contraejemplo refuta un enunciado universal; muchos ejemplos no lo demuestran.
3. $f^{-1}(Y)$ denota una imagen inversa aunque $f$ no sea biyectiva.

## Ejercicios

1. Niega: «Para todo $\varepsilon>0$ existe $N$ tal que $|a_n-a|<\varepsilon$ para todo $n\ge N$».
2. Demuestra $f^{-1}(Y_1\cap Y_2)=f^{-1}(Y_1)\cap f^{-1}(Y_2)$.
3. Prueba que una unión numerable de conjuntos numerables es numerable, usando el axioma de elección para familias numerables.

> [!answer]- Respuestas breves
> 1. Existe $\varepsilon_0>0$ tal que para todo $N$ hay algún $n\ge N$ con $|a_n-a|\ge\varepsilon_0$.
> 2. Ambos lados afirman exactamente $f(x)\in Y_1$ y $f(x)\in Y_2$.
> 3. Enumera cada conjunto, dispón las listas en una tabla y recórrela por diagonales, omitiendo repeticiones.

---

[[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/02-real-numbers|2. Los números reales y la completitud →]]
