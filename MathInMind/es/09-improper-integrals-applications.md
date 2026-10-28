---
title: "Integrales impropias y aplicaciones"
lang: es
chapter: 9
part: "Cálculo de una variable"
---
# 9. Integrales impropias y aplicaciones

[← 8. La integral de Riemann](08-riemann-integration.md) · [Índice](index.md) · [Términos y teoremas](term-index.md) · [10. Sucesiones y series de funciones →](10-function-sequences-series.md)

> **Objetivo.** Tratar intervalos e integrandos no acotados mediante límites y usar integrales para magnitudes geométricas y físicas.

<a id="sec-9-1"></a>
## 9.1 Definiciones

En un intervalo no acotado definimos

```math
\int_a^\infty f(x)\,dx
=\lim_{R\to\infty}\int_a^R f(x)\,dx
```

cuando el límite existe y es finito. Si el integrando no está acotado cerca de $`b`$,

```math
\int_a^b f(x)\,dx
=\lim_{t\to b^-}\int_a^t f(x)\,dx.
```

Si ambos extremos son problemáticos, se divide en un punto interior y se exige convergencia independiente de las dos partes. En $`(-\infty,\infty)`$, ambas colas deben converger por separado. El límite simétrico llamado **valor principal** puede existir aunque la integral impropia no exista.

Por ejemplo,

```math
\int_1^\infty\frac{dx}{x^p}<\infty\iff p>1,
\qquad
\int_0^1\frac{dx}{x^p}<\infty\iff p<1.
```

<a id="sec-9-2"></a>
## 9.2 Criterios de convergencia

Para integrandos no negativos, la acotación de las integrales truncadas equivale a convergencia. La comparación funciona como en series: en un intervalo infinito, $`f\sim C/x^p`$ da convergencia si $`p>1`$.

La [convergencia absoluta](04-numeric-series.md#sec-4-3) significa que $`\int|f|`$ converge e implica la ordinaria bajo integrabilidad local usual. Puede haber convergencia condicional con integrandos oscilatorios.

> <a id="dirichlet-test-for-integrals"></a>**Criterio de Dirichlet.** Si $`F(T)=\int_a^T f`$ está acotada y $`g`$ decrece a cero con regularidad adecuada, entonces $`\int_a^\infty f(x)g(x)\,dx`$ converge.

Así, $`\int_1^\infty\sin x/x\,dx`$ converge condicionalmente: partes o Dirichlet prueban convergencia, mientras que comparaciones cerca de múltiplos de $`\pi`$ muestran que $`\int|\sin x|/x`$ diverge.

El [criterio de Cauchy](03-sequences.md#sec-3-4) para $`\int_a^\infty f`$ exige que $`\int_S^T f`$ sea arbitrariamente pequeña para todos $`S<T`$ suficientemente grandes.

<a id="sec-9-3"></a>
## 9.3 Área, longitud y volumen

Para $`f\ge g`$ en $`[a,b]`$, el área entre las gráficas es

```math
A=\int_a^b(f(x)-g(x))\,dx.
```

En [coordenadas polares](17-multiple-integrals.md#sec-17-3), el área barrida por $`r=r(\theta)`$ es

```math
A=\frac12\int_\alpha^\beta r(\theta)^2\,d\theta.
```

La longitud de una curva [continuamente derivable](15-multivariable-differentiation.md#sec-15-1) $`\gamma(t)=(x(t),y(t))`$ es

```math
L=\int_a^b\sqrt{x'(t)^2+y'(t)^2}\,dt.
```

Para una gráfica, $`L=\int_a^b\sqrt{1+f'(x)^2}\,dx`$. En forma polar,

```math
L=\int_\alpha^\beta\sqrt{r^2+(dr/d\theta)^2}\,d\theta.
```

Si un sólido tiene secciones de área $`A(x)`$, su volumen es $`V=\int_a^b A(x)\,dx`$. La rotación de $`0\le y=f(x)`$ alrededor del eje $`x`$ da

```math
V=\pi\int_a^b f(x)^2\,dx,
```

y las capas cilíndricas alrededor del eje $`y`$ dan $`V=2\pi\int_a^b x f(x)\,dx`$ si $`x\ge0`$.

<a id="sec-9-4"></a>
## 9.4 Trabajo y valor medio

Una fuerza variable $`F(x)`$ a lo largo de un trayecto recto realiza el trabajo

```math
W=\int_a^b F(x)\,dx.
```

En general, el trabajo a lo largo de una curva es una [integral de línea](18-vector-calculus.md#sec-18-1), estudiada en el capítulo 18. El valor medio de una función integrable es

```math
f_{\mathrm{avg}}=\frac1{b-a}\int_a^b f(x)\,dx.
```

Estas fórmulas se obtienen dividiendo el objeto, aproximando cada pequeña contribución y pasando al límite.

## Ejemplo resuelto

La longitud de $`y=\frac23x^{3/2}`$ desde $`0`$ hasta $`3`$ cumple $`y'=\sqrt x`$, por lo que

```math
L=\int_0^3\sqrt{1+x}\,dx
=\left.\frac23(1+x)^{3/2}\right|_0^3
=\frac{14}{3}.
```

## Errores frecuentes

1. No se sustituye infinito directamente en una [primitiva](08-riemann-integration.md#sec-8-3): se toma un límite.
2. Un límite simétrico no sustituye la convergencia independiente de ambas colas.
3. La longitud usa $`\sqrt{1+(y')^2}`$, no $`1+y'`$.

## Ejercicios

1. Decide si $`\int_0^\infty dx/(1+x^2)`$ converge y calcúlala.
2. Halla el área de un pétalo de $`r=\cos(2\theta)`$.
3. Calcula el volumen de rotación de $`y=\sqrt x`$, $`0\le x\le1`$, alrededor del eje $`x`$.

<details>
<summary>Respuestas breves</summary>

1. Converge y vale $`\pi/2`$.
2. Un pétalo corresponde a $`-\pi/4\le\theta\le\pi/4`$; su área es $`\pi/8`$.
3. $`V=\pi\int_0^1x\,dx=\pi/2`$.
</details>

---

[← 8. La integral de Riemann](08-riemann-integration.md) · [Índice](index.md) · [Términos y teoremas](term-index.md) · [10. Sucesiones y series de funciones →](10-function-sequences-series.md)
