---
title: "Series de Fourier"
lang: es
chapter: 12
part: "Procesos infinitos"
---
# 12. Series de Fourier

[← 11. Series de potencias y funciones analíticas](11-power-series.md) · [Índice](index.md) · [Términos y teoremas](term-index.md) · [13. Espacios métricos, compacidad y completitud →](13-metric-spaces.md)

> **Objetivo.** Representar funciones periódicas mediante modos trigonométricos ortogonales y distinguir [convergencia puntual](10-function-sequences-series.md#sec-10-1) y cuadrática media.

<a id="sec-12-1"></a>
## 12.1 Sistema trigonométrico y coeficientes

Para una función $`f`$ integrable y $`2\pi`$-periódica, definimos

```math
a_0=\frac1\pi\int_{-\pi}^{\pi}f(x)\,dx,
```
```math
a_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos(nx)\,dx,
\qquad
b_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin(nx)\,dx.
```

Su serie de Fourier es

```math
f(x)\sim \frac{a_0}{2}
+\sum_{n=1}^{\infty}\bigl(a_n\cos(nx)+b_n\sin(nx)\bigr).
```

Al principio, $`\sim`$ solo asocia estos coeficientes; la igualdad requiere un teorema de convergencia.

El sistema $`\{1,\cos nx,\sin nx\}`$ es ortogonal con el [producto interno](21-lp-spaces.md#sec-21-4)

```math
\langle f,g\rangle=\int_{-\pi}^{\pi}f(x)g(x)\,dx.
```

Por ejemplo, $`\int_{-\pi}^{\pi}\cos(nx)\sin(mx)\,dx=0`$, mientras $`\int_{-\pi}^{\pi}\cos^2(nx)\,dx=\pi`$ para $`n\ge1`$.

Para periodo $`2L`$, se sustituye $`nx`$ por $`n\pi x/L`$ y se integra en un intervalo de longitud $`2L`$ con la normalización correspondiente.

<a id="sec-12-2"></a>
## 12.2 Simetría

Si $`f`$ es par, todos los $`b_n=0`$ y

```math
a_n=\frac2\pi\int_0^\pi f(x)\cos(nx)\,dx.
```

Si $`f`$ es impar, todos los $`a_n=0`$ y

```math
b_n=\frac2\pi\int_0^\pi f(x)\sin(nx)\,dx.
```

Los desarrollos de medio rango en senos y cosenos representan, respectivamente, extensiones periódicas impar y par de una función definida en $`(0,L)`$. El comportamiento frontera se lee en la extensión.

<a id="sec-12-3"></a>
## 12.3 Convergencia

> <a id="dirichlet-pointwise-theorem"></a>**Teorema puntual de Dirichlet.** Si una $`f`$ periódica es continua a trozos y [continuamente derivable](15-multivariable-differentiation.md#sec-15-1) a trozos, su [serie de Fourier](#sec-12-1) converge en cada punto a
> ```math
> \frac{f(x^-)+f(x^+)}2.
> ```
> En puntos de continuidad, esto es simplemente $`f(x)`$.

En un salto, la serie elige el punto medio, independientemente de cómo se defina $`f(x)`$ allí.

Para funciones de cuadrado integrable, las [sumas parciales](04-numeric-series.md#sec-4-1) de Fourier dan la mejor aproximación cuadrática media por polinomios trigonométricos del mismo grado, y

```math
\int_{-\pi}^{\pi}|f(x)-s_N(x)|^2\,dx\to0.
```

Esto no implica por sí solo convergencia puntual. La convergencia uniforme exige hipótesis más fuertes; cerca de saltos aparece el sobreimpulso de Gibbs.

<a id="sec-12-4"></a>
## 12.4 Identidad de Parseval

Para $`f\in L^2([-\pi,\pi])`$,

```math
\frac1\pi\int_{-\pi}^{\pi}|f(x)|^2\,dx
=\frac{a_0^2}{2}+\sum_{n=1}^{\infty}(a_n^2+b_n^2).
```

La identidad de Parseval es el teorema de Pitágoras en dimensión infinita. También convierte coeficientes en sumas de series numéricas.

La derivación formal requiere cuidado. Si $`f`$ es continua, periódica y suave a trozos, con [derivada](06-derivatives.md#sec-6-1) suficientemente integrable, la serie de $`f'`$ se obtiene derivando término a término. La integración suele ser más flexible, pero la periodicidad exige media nula.

## Ejemplo resuelto

Para $`f(x)=x`$ en $`(-\pi,\pi)`$, extendida periódicamente, la imparidad da $`a_n=0`$. Integrando por partes,

```math
b_n=\frac2\pi\int_0^\pi x\sin(nx)\,dx
=\frac{2(-1)^{n+1}}n.
```

Por tanto

```math
x=2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}n\sin(nx),
\qquad -\pi<x<\pi.
```

En $`x=\pi`$, la serie vale cero, el punto medio del salto entre $`\pi`$ y $`-\pi`$. Con $`x=\pi/2`$ se obtiene $`\sum_{k=0}^{\infty}(-1)^k/(2k+1)=\pi/4`$. Parseval da $`\sum_{n=1}^{\infty}1/n^2=\pi^2/6`$.

## Errores frecuentes

1. No está justificado escribir igualdad antes de probar convergencia.
2. En un salto, el límite es el promedio de los valores laterales.
3. La convergencia cuadrática media no implica automáticamente convergencia puntual en todas partes.

## Ejercicios

1. Halla la serie de Fourier de $`f(x)=x^2`$ en $`(-\pi,\pi)`$.
2. Explica por qué la serie de una función par contiene solo cosenos.
3. Usa Parseval para $`f(x)=x`$ y verifica $`\sum1/n^2=\pi^2/6`$.

<details>
<summary>Respuestas breves</summary>

1. $`x^2=\pi^2/3+4\sum_{n=1}^{\infty}(-1)^n\cos(nx)/n^2`$ en $`[-\pi,\pi]`$, entendiendo la extensión periódica.
2. Los productos $`f(x)\sin(nx)`$ son impares, así que sus integrales simétricas se anulan.
3. Usa $`b_n=2(-1)^{n+1}/n`$ y $`(1/\pi)\int_{-\pi}^{\pi}x^2\,dx=2\pi^2/3`$.
</details>

---

[← 11. Series de potencias y funciones analíticas](11-power-series.md) · [Índice](index.md) · [Términos y teoremas](term-index.md) · [13. Espacios métricos, compacidad y completitud →](13-metric-spaces.md)
