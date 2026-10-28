---
title: "Espacios Lp y modos de convergencia"
lang: es
chapter: 21
part: "Análisis moderno"
---
# 21. Espacios $`L^p`$ y modos de convergencia

[← 20. Integración de Lebesgue y teoremas de convergencia](20-lebesgue-integration.md) · [Índice](index.md) · [Términos y teoremas](term-index.md)

> **Objetivo.** Tratar funciones como puntos de [espacios normados](14-several-variables.md#sec-14-1) y relacionar convergencia en $`L^p`$, [casi en todas partes](19-measure-theory.md#sec-19-4) y en media cuadrática.

<a id="sec-21-1"></a>
## 21.1 Definición y desigualdades básicas

Para $`1\le p<\infty`$, definimos

```math
\|f\|_p=\left(\int_X|f|^p\,d\mu\right)^{1/p},
\qquad
L^p(\mu)=\{f\text{ medible}:\|f\|_p<\infty\}.
```

Para $`p=\infty`$, $`\|f\|_\infty`$ es el supremo esencial: el menor $`M`$ tal que $`|f|\le M`$ casi en todas partes. Se identifican funciones iguales c.t.p.; así $`\|\cdot\|_p`$ es una norma y no solo una seminorma.

> <a id="holder-inequality"></a>**Desigualdad de Hölder.** Si $`1/p+1/q=1`$, entonces
> ```math
> \int_X|fg|\,d\mu\le\|f\|_p\|g\|_q.
> ```

Para $`p=q=2`$ es [Cauchy–Schwarz](#sec-21-4). La **desigualdad de Minkowski** es la triangular

```math
\|f+g\|_p\le\|f\|_p+\|g\|_p.
```

Estas desigualdades muestran que $`L^p`$ es un espacio vectorial normado y ayudan a estimar productos y perturbaciones.

<a id="sec-21-2"></a>
## 21.2 Completitud y convergencia

> <a id="riesz-fischer-theorem"></a>**Teorema de Riesz–Fischer.** Todo espacio $`L^p`$, $`1\le p\le\infty`$, es completo; por tanto es un [espacio de Banach](#sec-21-1).

La convergencia $`\|f_n-f\|_p\to0`$ se llama convergencia en media de orden $`p`$, o cuadrática media si $`p=2`$. Implica convergencia en [medida](19-measure-theory.md#sec-19-2) y la existencia de una [subsucesión](03-sequences.md#sec-3-4) que converge a $`f`$ c.t.p. No implica que toda la sucesión original converja c.t.p.

Recíprocamente, la convergencia c.t.p. no implica convergencia $`L^p`$ sin una condición adicional. La [convergencia dominada](20-lebesgue-integration.md#dominated-convergence-theorem) la proporciona cuando $`|f_n|^p\le g\in L^1`$.

En un espacio de medida finita y $`1\le r<p\le\infty`$,

```math
\|f\|_r\le\mu(X)^{1/r-1/p}\|f\|_p
```

con la interpretación natural en los extremos. Por ello $`L^p\subseteq L^r`$ y la convergencia $`L^p`$ implica convergencia $`L^r`$. Estas inclusiones suelen fallar en medida infinita.

<a id="sec-21-3"></a>
## 21.3 Densidad y aproximación

Para $`1\le p<\infty`$, las funciones simples integrables son densas en $`L^p`$. Las funciones continuas de soporte [compacto](13-metric-spaces.md#sec-13-4) son densas en $`L^p(\mathbb R^n)`$. Muchas identidades se prueban primero para funciones cómodas y luego se extienden por aproximación.

La densidad de funciones continuas falla en $`L^\infty`$: un [límite uniforme](10-function-sequences-series.md#sec-10-1) de continuas es continuo, por lo que una escalonada discontinua no puede aproximarse arbitrariamente bien.

Truncamiento, regularización y aproximación por simples son técnicas estándar que reducen problemas a estimaciones en una subclase densa.

<a id="sec-21-4"></a>
## 21.4 El espacio de Hilbert L2

El espacio $`L^2`$ tiene producto interno

```math
\langle f,g\rangle=\int_Xf\overline{g}\,d\mu,
\qquad \|f\|_2=\sqrt{\langle f,f\rangle}.
```

Por ser completo, $`L^2`$ es un espacio de Hilbert. Si $`K\subseteq L^2`$ es cerrado y convexo, cada $`f`$ tiene un único punto más próximo en $`K`$, la proyección ortogonal. Para un subespacio cerrado $`M`$,

```math
f=P_Mf+(f-P_Mf),\qquad f-P_Mf\perp M.
```

Si $`(e_n)`$ es una base ortonormal, entonces

```math
f=\sum_n\langle f,e_n\rangle e_n
\quad\text{en }L^2,
\qquad
\|f\|_2^2=\sum_n|\langle f,e_n\rangle|^2.
```

Las [series de Fourier](12-fourier-series.md#sec-12-1) son la realización trigonométrica de esta teoría. La proyección ortogonal explica por qué las [sumas parciales](04-numeric-series.md#sec-4-1) dan aproximaciones cuadráticas medias óptimas.

## Ejemplo resuelto

En $`(0,1)`$, $`f(x)=x^{-\alpha}`$ pertenece a $`L^p`$ para $`p`$ finito exactamente cuando

```math
\int_0^1x^{-\alpha p}\,dx<\infty
\iff \alpha p<1.
```

En $`(1,\infty)`$, la misma función pertenece a $`L^p`$ exactamente cuando $`\alpha p>1`$. Las singularidades locales y el decaimiento en infinito imponen condiciones opuestas.

## Errores frecuentes

1. Los elementos de $`L^p`$ son clases de equivalencia módulo conjuntos nulos, no funciones distinguidas puntualmente.
2. Ni la convergencia c.t.p. ni la $`L^p`$ implica automáticamente la otra para toda la sucesión.
3. La inclusión $`L^p\subseteq L^r`$ para $`r<p`$ exige medida finita.

## Ejercicios

1. Calcula $`\|x\|_p`$ en $`[0,1]`$ para $`1\le p<\infty`$.
2. Prueba $`\int_0^1|f|\,dx\le\|f\|_p`$ en $`[0,1]`$.
3. Para $`f_n=n^{1/p}1_{(0,1/n)}`$, halla el límite c.t.p. y $`\|f_n\|_p`$.

<details>
<summary>Respuestas breves</summary>

1. $`\|x\|_p=(1/(p+1))^{1/p}`$.
2. Aplica Hölder con $`g=1`$ y $`\|1\|_q=1`$ en un espacio de medida uno.
3. $`f_n\to0`$ c.t.p., mientras $`\|f_n\|_p=1`$ para todo $`n`$; no hay convergencia a cero en $`L^p`$.
</details>

---

[← 20. Integración de Lebesgue y teoremas de convergencia](20-lebesgue-integration.md) · [Índice](index.md) · [Términos y teoremas](term-index.md)
