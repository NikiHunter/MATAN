---
title: "Series de potencias y funciones analíticas"
lang: es
chapter: 11
part: "Procesos infinitos"
---
# 11. Series de potencias y funciones analíticas

[← 10. Sucesiones y series de funciones](10-function-sequences-series.md) · [Índice](index.md) · [Términos y teoremas](term-index.md) · [12. Series de Fourier →](12-fourier-series.md)

> **Objetivo.** Determinar regiones de convergencia, operar término a término y distinguir suavidad de analiticidad.

<a id="sec-11-1"></a>
## 11.1 Radio de convergencia

Una serie de potencias centrada en $`a`$ tiene la forma

```math
\sum_{n=0}^{\infty}c_n(x-a)^n.
```

Su radio de convergencia $`R\in[0,\infty]`$ viene dado por Cauchy–Hadamard:

```math
\frac1R=\limsup_{n\to\infty}\sqrt[n]{|c_n|},
```

con $`1/0=\infty`$ y $`1/\infty=0`$. La serie [converge absolutamente](04-numeric-series.md#sec-4-3) si $`|x-a|<R`$ y diverge si $`|x-a|>R`$. En $`|x-a|=R`$ cada extremo se estudia por separado.

Si existe el límite del cociente, una alternativa práctica es

```math
R=\lim_{n\to\infty}\left|\frac{c_n}{c_{n+1}}\right|.
```

También se puede aplicar el [criterio del cociente](04-numeric-series.md#sec-4-2) o de la raíz directamente a $`c_n(x-a)^n`$, incluyendo el factor con $`x`$.

<a id="sec-11-2"></a>
## 11.2 Convergencia uniforme y cálculo

En todo subintervalo cerrado de $`(a-R,a+R)`$, una [serie de potencias](#sec-11-1) [converge uniformemente](10-function-sequences-series.md#sec-10-1). Por ello su suma es continua en el intervalo abierto de convergencia. Para $`|x-a|<R`$,

```math
\frac{d}{dx}\sum_{n=0}^{\infty}c_n(x-a)^n
=\sum_{n=1}^{\infty}nc_n(x-a)^{n-1},
```
```math
\int_a^x\sum_{n=0}^{\infty}c_n(t-a)^n\,dt
=\sum_{n=0}^{\infty}\frac{c_n}{n+1}(x-a)^{n+1}.
```

Las series [derivada](06-derivatives.md#sec-6-1) e integrada tienen el mismo radio $`R`$. Derivando repetidamente, la suma es infinitamente derivable y

```math
c_n=\frac{f^{(n)}(a)}{n!}.
```

Esta unicidad permite hallar coeficientes a partir de cualquier desarrollo válido, no solo calculando derivadas.

<a id="sec-11-3"></a>
## 11.3 Desarrollos fundamentales

Son especialmente útiles las identidades

```math
e^x=\sum_{n=0}^{\infty}\frac{x^n}{n!},\qquad x\in\mathbb R,
```
```math
\sin x=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n+1}}{(2n+1)!},
\qquad
\cos x=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n}}{(2n)!},
```
```math
\log(1+x)=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}x^n}{n},
\qquad -1<x\le1,
```
```math
\arctan x=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n+1}}{2n+1},
\qquad |x|\le1.
```

Para la serie binomial,

```math
(1+x)^\alpha=\sum_{n=0}^{\infty}\binom{\alpha}{n}x^n,
\qquad |x|<1,
```

donde $`\binom{\alpha}{n}=\alpha(\alpha-1)\cdots(\alpha-n+1)/n!`$.

> <a id="abel-theorem"></a>**Teorema de Abel.** Si una serie de potencias converge en un extremo, su suma es continua desde el interior hasta ese extremo. Esto justifica tomar [límites laterales](05-limits-continuity.md#sec-5-1) en identidades válidas para $`|x-a|<R`$.

<a id="sec-11-4"></a>
## 11.4 Analítica no significa solamente suave

Una función es **analítica** cerca de $`a`$ si coincide con una serie de potencias convergente en algún entorno de $`a`$. Toda función analítica es infinitamente derivable, pero el recíproco es falso.

Sea $`f(x)=e^{-1/x^2}`$ si $`x\ne0`$ y $`f(0)=0`$. Entonces $`f\in C^\infty(\mathbb R)`$ y todas sus derivadas en cero son cero. Su [serie de Taylor](#sec-11-3) centrada en cero es idénticamente nula y no representa a $`f`$ en ningún entorno del origen.

Por tanto, para probar un desarrollo infinito hay que demostrar que la serie converge y que su suma coincide con la función, normalmente estimando el resto.

## Ejemplo resuelto

Partimos de

```math
\frac1{1+x^2}=\sum_{n=0}^{\infty}(-1)^n x^{2n},
\qquad |x|<1.
```

Al multiplicar por $`x`$, $`x/(1+x^2)=\sum(-1)^n x^{2n+1}`$. Integrando desde $`0`$ hasta $`x`$,

```math
\frac12\log(1+x^2)
=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n+2}}{2n+2}.
```

Todas las operaciones son válidas dentro del mismo intervalo abierto de convergencia.

## Errores frecuentes

1. El radio no decide en los extremos.
2. La derivación término a término es automática dentro del intervalo abierto, no necesariamente en un extremo.
3. La derivabilidad infinita no garantiza igualdad con la serie de Taylor.

## Ejercicios

1. Halla el radio y el intervalo de convergencia de $`\sum n x^n/2^n`$.
2. Halla el intervalo de convergencia de $`\sum x^n/n^2`$.
3. Calcula $`\sum_{n=1}^{\infty}n/2^n`$.

<details>
<summary>Respuestas breves</summary>

1. $`R=2`$; tanto $`x=2`$ como $`x=-2`$ divergen, así que el intervalo es $`(-2,2)`$.
2. $`R=1`$; ambos extremos convergen absolutamente, dando $`[-1,1]`$.
3. Usa $`\sum nx^n=x/(1-x)^2`$ en $`x=1/2`$; la suma es $`2`$.
</details>

---

[← 10. Sucesiones y series de funciones](10-function-sequences-series.md) · [Índice](index.md) · [Términos y teoremas](term-index.md) · [12. Series de Fourier →](12-fourier-series.md)
