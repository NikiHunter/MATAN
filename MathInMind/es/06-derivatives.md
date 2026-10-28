---
title: "Derivación en una variable"
lang: es
chapter: 6
part: "Cálculo de una variable"
---
# 6. Derivación en una variable

[← 5. Límites y continuidad de funciones](05-limits-continuity.md) · [Índice](index.md) · [Términos y teoremas](term-index.md) · [7. Teoremas del valor medio, Taylor y convexidad →](07-taylor-convexity.md)

> **Objetivo.** Interpretar la [derivada](#sec-6-1) como aproximación lineal local y aplicar con seguridad las reglas de derivación.

<a id="sec-6-1"></a>
## 6.1 Definición y aproximación lineal

La derivada de $`f`$ en $`a`$ es

```math
f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}h
```

cuando este límite finito existe. Equivalentemente,

```math
f(a+h)=f(a)+f'(a)h+o(h)\qquad(h\to0).
```

Así, $`L(h)=f(a)+f'(a)h`$ es la mejor aproximación lineal cerca de $`a`$. La recta tangente es $`y=f(a)+f'(a)(x-a)`$.

La derivabilidad implica continuidad porque

```math
f(a+h)-f(a)=h\frac{f(a+h)-f(a)}h\to0.
```

El recíproco es falso: $`|x|`$ es continua pero no derivable en cero, pues los cocientes incrementales laterales son $`-1`$ y $`1`$.

Las derivadas laterales se definen mediante [límites laterales](05-limits-continuity.md#sec-5-1). Existe la derivada bilateral finita exactamente cuando ambas existen y coinciden.

<a id="sec-6-2"></a>
## 6.2 Reglas de derivación

Para $`f,g`$ derivables y constantes $`\alpha,\beta`$,

```math
(\alpha f+\beta g)'=\alpha f'+\beta g',
```
```math
(fg)'=f'g+fg',
\qquad
\left(\frac fg\right)'=\frac{f'g-fg'}{g^2}\quad(g\ne0).
```

> <a id="chain-rule"></a>**Regla de la cadena.** Si $`f`$ es derivable en $`a`$ y $`g`$ en $`f(a)`$, entonces
> ```math
> (g\circ f)'(a)=g'(f(a))f'(a).
> ```

Si $`f`$ es derivable y estrictamente monótona cerca de $`a`$, con $`f'(a)\ne0`$, la [función inversa](01-logic-sets-functions.md#sec-1-4) cumple

```math
(f^{-1})'(f(a))=\frac1{f'(a)}.
```

Derivadas básicas:

```math
(x^p)'=px^{p-1},\quad (e^x)'=e^x,\quad(\log x)'=\frac1x,
```
```math
(\sin x)'=\cos x,\quad(\cos x)'=-\sin x,\quad(\arctan x)'=\frac1{1+x^2}.
```

Para $`f(x)>0`$, la derivación logarítmica da
$`(f^g)'=f^g(g'\log f+gf'/f)`$.

<a id="sec-6-3"></a>
## 6.3 Diferenciales y curvas paramétricas

La diferencial $`df(a;h)=f'(a)h`$ es la parte lineal del incremento. La notación $`dy=f'(x)\,dx`$ es útil para aproximaciones y sustituciones, pero $`dy/dx`$ se define mediante la derivada, no como cociente literal de números.

Si $`x=\varphi(t)`$, $`y=\psi(t)`$ son derivables y $`\varphi'(t)\ne0`$, entonces

```math
\frac{dy}{dx}=\frac{\psi'(t)}{\varphi'(t)}.
```

Las derivadas de orden superior se definen por $`f^{(n+1)}=(f^{(n)})'`$. La fórmula de Leibniz es

```math
(fg)^{(n)}=\sum_{k=0}^{n}\binom nk f^{(k)}g^{(n-k)}.
```

<a id="sec-6-4"></a>
## 6.4 Información local

> <a id="fermat-theorem"></a>**Teorema de Fermat.** Si $`f`$ tiene un extremo local en un punto interior $`a`$ y es derivable allí, entonces $`f'(a)=0`$.

El recíproco es falso: $`x^3`$ tiene derivada cero en el origen pero no extremo. Si $`f'(x)>0`$ en un intervalo, $`f`$ es estrictamente creciente, por el [teorema del valor medio](07-taylor-convexity.md#lagrange-mean-value-theorem).

> <a id="darboux-property"></a>**Propiedad de Darboux.** Una derivada no tiene que ser continua, pero en un intervalo toma cada valor entre dos cualesquiera de sus valores.

Por ello una derivada no puede tener una [discontinuidad de salto](05-limits-continuity.md#sec-5-3), aunque puede oscilar. Un ejemplo clásico es $`x^2\sin(1/x)`$ fuera de cero, completado con valor cero en el origen.

## Ejemplo resuelto

Derivamos $`f(x)=x^x`$ para $`x>0`$. Escribimos $`f(x)=e^{x\log x}`$. Por la [regla de la cadena](#chain-rule),

```math
f'(x)=e^{x\log x}(\log x+1)=x^x(\log x+1).
```

La derivada es negativa en $`(0,1/e)`$ y positiva en $`(1/e,\infty)`$, así que el mínimo está en $`x=1/e`$.

## Errores frecuentes

1. La continuidad no implica derivabilidad.
2. La regla de la cadena exige multiplicar por la derivada interior.
3. $`f'(a)=0`$ define un punto estacionario, no automáticamente un extremo.

## Ejercicios

1. Usa la definición para derivar $`1/x`$ en $`a\ne0`$.
2. Deriva $`\arcsin x`$ mediante la regla de la función inversa.
3. Halla la tangente a $`x=t^2`$, $`y=t^3`$ en $`t=1`$.

<details>
<summary>Respuestas breves</summary>

1. El cociente incremental tiende a $`-1/a^2`$.
2. $`(\arcsin x)'=1/\sqrt{1-x^2}`$ para $`|x|<1`$.
3. $`dy/dx=3t/2`$, luego la pendiente en $`(1,1)`$ es $`3/2`$; la recta es $`y-1=\frac32(x-1)`$.
</details>

---

[← 5. Límites y continuidad de funciones](05-limits-continuity.md) · [Índice](index.md) · [Términos y teoremas](term-index.md) · [7. Teoremas del valor medio, Taylor y convexidad →](07-taylor-convexity.md)
