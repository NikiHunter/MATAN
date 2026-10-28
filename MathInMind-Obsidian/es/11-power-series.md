---
title: "Series de potencias y funciones analíticas"
lang: es
chapter: 11
part: "Procesos infinitos"
aliases: ["Series de potencias y funciones analíticas (es)"]
tags: [mathinmind/es, mathinmind/chapter]
---
# 11. Series de potencias y funciones analíticas

[[es/10-function-sequences-series|← 10. Sucesiones y series de funciones]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/12-fourier-series|12. Series de Fourier →]]

> [!abstract] Objetivo
> Determinar regiones de convergencia, operar término a término y distinguir suavidad de analiticidad.

## 11.1 Radio de convergencia

Una serie de potencias centrada en $a$ tiene la forma

$$
\sum_{n=0}^{\infty}c_n(x-a)^n.
$$

Su radio de convergencia $R\in[0,\infty]$ viene dado por Cauchy–Hadamard:

$$
\frac1R=\limsup_{n\to\infty}\sqrt[n]{|c_n|},
$$

con $1/0=\infty$ y $1/\infty=0$. La serie [[es/04-numeric-series#4.3 Convergencia absoluta y condicional|converge absolutamente]] si $|x-a|<R$ y diverge si $|x-a|>R$. En $|x-a|=R$ cada extremo se estudia por separado.

Si existe el límite del cociente, una alternativa práctica es

$$
R=\lim_{n\to\infty}\left|\frac{c_n}{c_{n+1}}\right|.
$$

También se puede aplicar el [[es/04-numeric-series#4.2 Términos no negativos|criterio del cociente]] o de la raíz directamente a $c_n(x-a)^n$, incluyendo el factor con $x$.

## 11.2 Convergencia uniforme y cálculo

En todo subintervalo cerrado de $(a-R,a+R)$, una [[#11.1 Radio de convergencia|serie de potencias]] [[es/10-function-sequences-series#10.1 Dos modos de convergencia|converge uniformemente]]. Por ello su suma es continua en el intervalo abierto de convergencia. Para $|x-a|<R$,

$$
\frac{d}{dx}\sum_{n=0}^{\infty}c_n(x-a)^n
=\sum_{n=1}^{\infty}nc_n(x-a)^{n-1},
$$
$$
\int_a^x\sum_{n=0}^{\infty}c_n(t-a)^n\,dt
=\sum_{n=0}^{\infty}\frac{c_n}{n+1}(x-a)^{n+1}.
$$

Las series [[es/06-derivatives#6.1 Definición y aproximación lineal|derivada]] e integrada tienen el mismo radio $R$. Derivando repetidamente, la suma es infinitamente derivable y

$$
c_n=\frac{f^{(n)}(a)}{n!}.
$$

Esta unicidad permite hallar coeficientes a partir de cualquier desarrollo válido, no solo calculando derivadas.

## 11.3 Desarrollos fundamentales

Son especialmente útiles las identidades

$$
e^x=\sum_{n=0}^{\infty}\frac{x^n}{n!},\qquad x\in\mathbb R,
$$
$$
\sin x=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n+1}}{(2n+1)!},
\qquad
\cos x=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n}}{(2n)!},
$$
$$
\log(1+x)=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}x^n}{n},
\qquad -1<x\le1,
$$
$$
\arctan x=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n+1}}{2n+1},
\qquad |x|\le1.
$$

Para la serie binomial,

$$
(1+x)^\alpha=\sum_{n=0}^{\infty}\binom{\alpha}{n}x^n,
\qquad |x|<1,
$$

donde $\binom{\alpha}{n}=\alpha(\alpha-1)\cdots(\alpha-n+1)/n!$.

> [!theorem] Teorema de Abel
> Si una serie de potencias converge en un extremo, su suma es continua desde el interior hasta ese extremo. Esto justifica tomar [[es/05-limits-continuity#5.1 Límite en un punto|límites laterales]] en identidades válidas para $|x-a|<R$.

^abel-theorem

## 11.4 Analítica no significa solamente suave

Una función es **analítica** cerca de $a$ si coincide con una serie de potencias convergente en algún entorno de $a$. Toda función analítica es infinitamente derivable, pero el recíproco es falso.

Sea $f(x)=e^{-1/x^2}$ si $x\ne0$ y $f(0)=0$. Entonces $f\in C^\infty(\mathbb R)$ y todas sus derivadas en cero son cero. Su [[#11.3 Desarrollos fundamentales|serie de Taylor]] centrada en cero es idénticamente nula y no representa a $f$ en ningún entorno del origen.

Por tanto, para probar un desarrollo infinito hay que demostrar que la serie converge y que su suma coincide con la función, normalmente estimando el resto.

## Ejemplo resuelto

Partimos de

$$
\frac1{1+x^2}=\sum_{n=0}^{\infty}(-1)^n x^{2n},
\qquad |x|<1.
$$

Al multiplicar por $x$, $x/(1+x^2)=\sum(-1)^n x^{2n+1}$. Integrando desde $0$ hasta $x$,

$$
\frac12\log(1+x^2)
=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n+2}}{2n+2}.
$$

Todas las operaciones son válidas dentro del mismo intervalo abierto de convergencia.

## Errores frecuentes

1. El radio no decide en los extremos.
2. La derivación término a término es automática dentro del intervalo abierto, no necesariamente en un extremo.
3. La derivabilidad infinita no garantiza igualdad con la serie de Taylor.

## Ejercicios

1. Halla el radio y el intervalo de convergencia de $\sum n x^n/2^n$.
2. Halla el intervalo de convergencia de $\sum x^n/n^2$.
3. Calcula $\sum_{n=1}^{\infty}n/2^n$.

> [!answer]- Respuestas breves
> 1. $R=2$; tanto $x=2$ como $x=-2$ divergen, así que el intervalo es $(-2,2)$.
> 2. $R=1$; ambos extremos convergen absolutamente, dando $[-1,1]$.
> 3. Usa $\sum nx^n=x/(1-x)^2$ en $x=1/2$; la suma es $2$.

---

[[es/10-function-sequences-series|← 10. Sucesiones y series de funciones]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/12-fourier-series|12. Series de Fourier →]]
