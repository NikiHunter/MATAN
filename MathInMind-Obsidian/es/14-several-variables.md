---
title: "Funciones de varias variables"
lang: es
chapter: 14
part: "Varias variables y topología"
aliases: ["Funciones de varias variables (es)"]
tags: [mathinmind/es, mathinmind/chapter]
---
# 14. Funciones de varias variables

[[es/13-metric-spaces|← 13. Espacios métricos, compacidad y completitud]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/15-multivariable-differentiation|15. Derivación de aplicaciones de varias variables →]]

> [!abstract] Objetivo
> Estudiar límites y continuidad en $\mathbb R^n$, distinguiendo el comportamiento conjunto del coordenado.

## 14.1 Espacio euclidiano y normas

Un punto de $\mathbb R^n$ es $x=(x_1,\ldots,x_n)$. La norma y la distancia euclidianas son

$$
\|x\|_2=\left(\sum_{i=1}^{n}x_i^2\right)^{1/2},
\qquad d(x,y)=\|x-y\|_2.
$$

La [[es/21-lp-spaces#21.4 El espacio de Hilbert L2|desigualdad de Cauchy–Schwarz]] $|x\cdot y|\le\|x\|_2\|y\|_2$ da la desigualdad triangular. Otras normas son $\|x\|_1=\sum|x_i|$ y $\|x\|_\infty=\max|x_i|$.

Todas las normas en un espacio vectorial real de dimensión finita son equivalentes: existen $c,C>0$ con $c\|x\|_a\le\|x\|_b\le C\|x\|_a$. Por ello convergencia, apertura y continuidad no dependen de la norma elegida en $\mathbb R^n$.

Una función escalar es $f:D\to\mathbb R$ con $D\subseteq\mathbb R^n$; una aplicación vectorial es $F:D\to\mathbb R^m$. Los conjuntos de nivel $\{x:f(x)=c\}$ y las gráficas dan descripciones geométricas útiles.

## 14.2 Límites

Para $f:D\to\mathbb R$ y un punto de acumulación $a$ de $D$,

$$
\lim_{x\to a}f(x)=L
$$

significa que para todo $\varepsilon>0$ existe $\delta>0$ tal que $x\in D$ y $0<\|x-a\|<\delta$ implican $|f(x)-L|<\varepsilon$.

Para $F=(F_1,\ldots,F_m)$, la convergencia equivale a la de cada componente. Siguen valiendo el criterio sucesional y las leyes algebraicas usuales.

> [!warning] Advertencia sobre límites iterados
> La existencia de
> $$
> \lim_{x\to a}\lim_{y\to b}f(x,y),\qquad
> \lim_{y\to b}\lim_{x\to a}f(x,y)
> $$
> no implica la existencia del límite conjunto cuando $(x,y)\to(a,b)$.

^iterated-limit-warning

Comprobar finitas rectas nunca demuestra un límite conjunto. Una prueba positiva suele usar una estimación en términos de $\|x-a\|$.

## 14.3 Continuidad y dominios compactos

Una función es continua en $a$ si $f(x)\to f(a)$ cuando $x\to a$. Sumas, productos, cocientes lejos de ceros y composiciones conservan continuidad. Los polinomios son continuos en todas partes; las funciones racionales donde el denominador no se anula.

En un [[es/13-metric-spaces#13.4 Compacidad|compacto]] $K\subseteq\mathbb R^n$, una función real continua está acotada y alcanza sus extremos. También es [[es/05-limits-continuity#5.4 Continuidad uniforme|uniformemente continua]]:

$$
\forall\varepsilon>0\;\exists\delta>0:\quad
\|x-y\|<\delta\implies|f(x)-f(y)|<\varepsilon.
$$

En un conjunto [[es/13-metric-spaces#13.5 Continuidad y conexión|conexo]], una función continua tiene la propiedad del valor intermedio. Las proyecciones coordenadas y las [[#14.1 Espacio euclidiano y normas|normas]] son continuas, lo que ayuda con muchos ejemplos.

## 14.4 Dos ejemplos diagnósticos

Para

$$
f(x,y)=\frac{xy}{x^2+y^2},\qquad (x,y)\ne(0,0),
$$

el valor sobre $y=kx$ es $k/(1+k^2)$ si $x\ne0$. Distintas pendientes dan límites distintos, así que no existe límite conjunto en el origen. Sin embargo, ambos [[#^iterated-limit-warning|límites iterados]] son cero.

En cambio, para

$$
g(x,y)=\frac{x^2y}{x^2+y^2},
$$

tenemos $|g(x,y)|\le|y|$ porque $x^2/(x^2+y^2)\le1$. Por tanto $g(x,y)\to0$ cuando $(x,y)\to(0,0)$, y definir $g(0,0)=0$ la hace continua.

## Ejemplo resuelto

Probemos

$$
\lim_{(x,y)\to(0,0)}\frac{x^3+y^3}{x^2+y^2}=0.
$$

Usando $|x|,|y|\le r=\sqrt{x^2+y^2}$,

$$
\frac{|x^3+y^3|}{x^2+y^2}
\le\frac{|x|r^2+|y|r^2}{r^2}\le2r\to0.
$$

Esta estimación radial prueba el límite para todas las trayectorias simultáneamente.

## Errores frecuentes

1. Los límites iterados y el conjunto son objetos distintos.
2. Una trayectoria puede refutar un límite, pero normalmente no demostrarlo.
3. La continuidad en cada variable por separado no implica continuidad conjunta.

## Ejercicios

1. Prueba que $xy/(x^2+y^2)^{1/2}$ tiende a cero en el origen.
2. Estudia el límite de $x^2y/(x^4+y^2)$ en el origen sobre $y=kx^2$.
3. Demuestra que $F(x,y)=(x+y,xy)$ es continua.

> [!answer]- Respuestas breves
> 1. Con $r=\sqrt{x^2+y^2}$, $|xy|\le r^2/2$, así que el valor absoluto es como máximo $r/2$.
> 2. Sobre esa trayectoria el valor es $k/(1+k^2)$ si $x\ne0$, por lo que no existe límite conjunto.
> 3. Sus componentes son sumas y productos de proyecciones coordenadas continuas.

---

[[es/13-metric-spaces|← 13. Espacios métricos, compacidad y completitud]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/15-multivariable-differentiation|15. Derivación de aplicaciones de varias variables →]]
