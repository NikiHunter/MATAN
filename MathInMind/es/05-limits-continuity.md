---
title: "Límites y continuidad de funciones"
lang: es
chapter: 5
part: "Cálculo de una variable"
---
# 5. Límites y continuidad de funciones

[← 4. Series numéricas](04-numeric-series.md) · [Índice](index.md) · [Términos y teoremas](term-index.md) · [6. Derivación en una variable →](06-derivatives.md)

> **Objetivo.** Calcular y demostrar límites funcionales y aplicar los teoremas globales sobre funciones continuas en intervalos.

<a id="sec-5-1"></a>
## 5.1 Límite en un punto

Sea $`f`$ definida en un entorno perforado de $`a`$. Decimos que $`f(x)\to L`$ cuando $`x\to a`$ si

```math
\forall\varepsilon>0\;\exists\delta>0:\quad
0<|x-a|<\delta\implies |f(x)-L|<\varepsilon.
```

El valor $`f(a)`$, aunque exista, no afecta al límite. Suele ser útil el **criterio sucesional**:

```math
f(x)\to L\iff \bigl(x_n\to a,\ x_n\ne a\implies f(x_n)\to L\bigr).
```

Los límites lateral derecho e izquierdo usan $`a<x<a+\delta`$ y $`a-\delta<x<a`$. Existe el límite bilateral exactamente cuando ambos laterales existen y coinciden.

Por ejemplo, $`|x|/x`$ tiene límites laterales $`-1`$ y $`1`$ en $`0`$, por lo que no tiene límite bilateral. En cambio,

```math
\left|x\sin\frac1x\right|\le |x|\implies x\sin\frac1x\to0
```

por el [teorema del emparedado](03-sequences.md#sec-3-2).

<a id="sec-5-2"></a>
## 5.2 Álgebra, composición y comportamiento asintótico

Si $`f(x)\to A`$ y $`g(x)\to B`$, las sumas, los productos y los múltiplos escalares tienen los límites esperados; los cocientes exigen $`B\ne0`$. Si $`f(x)\to b`$ y $`g`$ es continua en $`b`$, entonces $`g(f(x))\to g(b)`$.

Algunos límites fundamentales son

```math
\lim_{x\to0}\frac{\sin x}{x}=1,
\qquad
\lim_{x\to0}\frac{e^x-1}{x}=1,
\qquad
\lim_{x\to0}(1+x)^{1/x}=e.
```

Los límites infinitos y en el infinito usan el mismo patrón de [cuantificadores](01-logic-sets-functions.md#sec-1-1) con $`|x|`$ o $`f(x)`$ grande. En el infinito, un polinomio está gobernado por su término de mayor grado; para funciones racionales se comparan los grados.

<a id="sec-5-3"></a>
## 5.3 Continuidad

Una función $`f`$ es continua en $`a`$ si $`f(a)`$ está definido y

```math
\lim_{x\to a}f(x)=f(a).
```

Equivalentemente, para todo $`\varepsilon>0`$ existe $`\delta>0`$ tal que $`|x-a|<\delta`$ implica $`|f(x)-f(a)|<\varepsilon`$. La continuidad se conserva mediante sumas, productos, cocientes lejos de ceros y composición.

Una discontinuidad evitable se elimina redefiniendo $`f(a)`$. En un salto, los [límites laterales](#sec-5-1) son finitos pero distintos. Una discontinuidad esencial incluye [oscilación](08-riemann-integration.md#sec-8-1) o comportamiento infinito.

> <a id="intermediate-value-theorem"></a>**Teorema del valor intermedio.** Si $`f:[a,b]\to\mathbb R`$ es continua e $`y`$ está entre $`f(a)`$ y $`f(b)`$, existe $`c\in[a,b]`$ con $`f(c)=y`$.

En particular, una función continua que toma valores de signos opuestos tiene un cero. La demostración usa bisección y completitud.

> <a id="extreme-value-theorem"></a>**Teorema de Weierstrass.** Una función continua en un intervalo cerrado y acotado está acotada y alcanza su máximo y su mínimo.

La clave es la [compacidad](13-metric-spaces.md#sec-13-4), no solo la continuidad. En $`(0,1)`$, la función continua $`1/x`$ no está acotada.

<a id="sec-5-4"></a>
## 5.4 Continuidad uniforme

Una función $`f`$ es uniformemente continua en $`E`$ si

```math
\forall\varepsilon>0\;\exists\delta>0\;\forall x,y\in E:
|x-y|<\delta\implies |f(x)-f(y)|<\varepsilon.
```

Aquí un mismo $`\delta`$ sirve para todos los pares de puntos. En continuidad ordinaria, $`\delta`$ puede depender del punto base.

> <a id="heine-cantor-theorem"></a>**Teorema de Heine–Cantor.** Una función continua en un compacto es uniformemente continua. En particular, ocurre en $`[a,b]`$.

La función $`x^2`$ no es uniformemente continua en $`\mathbb R`$; una función con [derivada](06-derivatives.md#sec-6-1) acotada sí lo es por el [teorema del valor medio](07-taylor-convexity.md#lagrange-mean-value-theorem). En $`(0,1)`$, $`\sin(1/x)`$ es continua pero no uniformemente continua.

## Ejemplo resuelto

Probemos que $`f(x)=x^2`$ es continua en $`a`$:

```math
|x^2-a^2|=|x-a|\,|x+a|.
```

Si $`|x-a|<1`$, entonces $`|x+a|\le2|a|+1`$. Por tanto basta $`\delta=\min\{1,\varepsilon/(2|a|+1)\}`$. La dependencia de $`a`$ explica por qué esta prueba no es uniforme en $`\mathbb R`$.

## Errores frecuentes

1. El límite en $`a`$ no utiliza $`f(a)`$; la continuidad sí.
2. Comprobar una sucesión no demuestra un límite funcional.
3. La continuidad en cada compacto no da un único $`\delta`$ en un dominio no acotado.

## Ejercicios

1. Demuestra directamente que $`\lim_{x\to2}(3x-1)=5`$.
2. Prueba que una función continua $`f:[0,1]\to[0,1]`$ tiene un punto fijo.
3. Decide si $`f(x)=1/x`$ es uniformemente continua en $`(1,\infty)`$ y en $`(0,1)`$.

<details>
<summary>Respuestas breves</summary>

1. $`|f(x)-5|=3|x-2|`$; toma $`\delta=\varepsilon/3`$.
2. Aplica el valor intermedio a $`g(x)=f(x)-x`$; sus valores extremos tienen signos opuestos o uno es cero.
3. Sí en $`(1,\infty)`$ porque $`|f'(x)|\le1`$; no en $`(0,1)`$, usando puntos próximos a cero con separaciones cada vez menores.
</details>

---

[← 4. Series numéricas](04-numeric-series.md) · [Índice](index.md) · [Términos y teoremas](term-index.md) · [6. Derivación en una variable →](06-derivatives.md)
