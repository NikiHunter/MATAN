---
title: "Lección 14 — Puntos de acumulación y puntos aislados, límite de una función por Cauchy y por Heine, unicidad y acotación local"
lang: es
course: "Análisis Matemático, 2025/26"
lecture: 14
date: 2025-10-16
source: "ма25_26_лекция_14_notes.pdf"
---
# Lección 14 — Límite de una función: definiciones por Cauchy y por Heine

[← Lección 13](lecture-13.md) · [Índice de lecciones](index.md) · [Lección 15 →](lecture-15.md) · [Términos y teoremas](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-14.md) · [English](../../en/lectures-2025-26/lecture-14.md)

> **Fuente:** `ма25_26_лекция_14_notes.pdf` — 18 páginas: diapositivas impresas (páginas 1–5, 7–9, 11–12, 15–16) y páginas manuscritas (6, 10, 13, 14, 17, 18). Las páginas 5 y 16 son diapositivas impresas con anotaciones manuscritas. Las páginas manuscritas se transcribieron a partir de su imagen. Los números de página del PDF aparecen en los encabezados.
>
> **Nota del editor.** La fecha de la lección se toma del pie de las diapositivas («16 de octubre de 2025»).

## Diapositivas impresas 1–3. Introducción

**Cita del día:** «Soy una bruja malvada . . . Me levanté con el pie izquierdo . . . Me subí a la escoba equivocada . . . Y volé en la dirección equivocada . . . »

**Objetivo de la lección.** Definir los [puntos de acumulación](#def-2-4-1) y los puntos aislados de un conjunto. Dar las definiciones del [límite de una función](#def-2-4-4) por Cauchy y por Heine. Demostrar la unicidad del límite de una función. Demostrar resultados sobre la acotación local de las funciones que tienen límite y sobre la estabilización del signo.

## §4. Límite de una función

### Diapositiva impresa 4. Punto de acumulación

<a id="def-2-4-1"></a>**Definición 2.4.1.** Sean $`a \in \mathbb{R}`$, $`D \subset \mathbb{R}`$. El punto $`a`$ se llama **punto de acumulación** (punto límite) del conjunto $`D`$ si en todo entorno de $`a`$ hay un punto de $`D`$ distinto de $`a`$.

<a id="def-2-4-2"></a>**Definición 2.4.2.** Un **entorno reducido** del punto $`a`$ es el conjunto $`\dot V(a) = V(a) \setminus \{a\}`$.

Así pues, $`a`$ es punto de acumulación de $`D`$ si todo [entorno reducido](#def-2-4-2) de $`a`$ corta a $`D`$ en un conjunto no vacío.

### Diapositiva impresa 5 con anotaciones manuscritas. Observaciones sobre los puntos de acumulación

1. Un punto de acumulación de un conjunto puede pertenecer o no pertenecer al conjunto. Por ejemplo, cada punto del segmento $`[c, d]`$ es punto de acumulación del intervalo $`(c, d)`$.
2. Si $`a`$ es punto de acumulación de $`D`$, entonces todo entorno de $`a`$ (reducido o no, da igual) contiene infinitos puntos de $`D`$.
3. Sea $`a`$ punto de acumulación de $`D`$. Entonces, para todo $`n \in \mathbb{N}`$, el $`\frac{1}{n}`$-entorno reducido de $`a`$ contiene un punto $`x_n`$ de $`D`$. La sucesión construida $`\{x_n\}`$ tiende a $`a`$, ya que $`|x_n - a| < \frac{1}{n} \to 0`$.
4. La definición de punto de acumulación se aplica también a los casos $`a = \pm\infty`$ y $`a = \infty`$.

Anotación manuscrita (en la observación 2): en la recta numérica se marcan los puntos $`a-1`$, $`a-\frac12`$, $`a-\frac1n`$, $`a`$, $`a+\frac1n`$, $`a+\frac12`$, $`a+1`$, con entornos alrededor de ellos (ilustración).

## Página manuscrita 6 (p. PDF 6). Recordatorio

Recordemos que

```math
\dot V(+\infty) = (E, +\infty), \qquad \dot V(-\infty) = (-\infty, -E), \qquad \dot V(\infty) = (-\infty, -E) \cup (E, +\infty),
```

para un $`E > 0`$ suficientemente grande.

### Diapositiva impresa 7. Puntos aislados

<a id="def-2-4-3"></a>**Definición 2.4.3.** Si un punto $`a`$ pertenece a un conjunto $`D`$ pero no es punto de acumulación de $`D`$, entonces $`a`$ se llama **punto aislado** de $`D`$.

### Diapositivas impresas 8–9. Límite de una función por Cauchy y por Heine

<a id="def-2-4-4"></a>**Definición 2.4.4.** Sean $`f : D \subset \mathbb{R} \to \mathbb{R}`$, $`a \in \mathbb{R}`$ punto de acumulación de $`D`$, y $`A \in \mathbb{R}`$. El número $`A`$ se llama **límite de la función** $`f`$ en el punto $`a`$, y se escribe $`\lim\limits_{x\to a} f(x) = A`$ o $`f(x) \xrightarrow[x\to a]{} A`$, si se cumple una de las siguientes afirmaciones (son equivalentes, teorema 2.4.1):

1. **Definición en lenguaje $`\varepsilon`$–$`\delta`$, o por Cauchy.** $`\forall \varepsilon > 0\ \exists \delta > 0\ \forall x \in D \setminus\{a\}`$: $`|x - a| < \delta \Rightarrow |f(x) - A| < \varepsilon`$.
2. **Definición en lenguaje de entornos.** $`\forall V(A)\ \exists V(a)`$: $`f(\dot V(a) \cap D) \subset V(A)`$.
3. **Definición en lenguaje de sucesiones, o por Heine.** Para toda sucesión $`\{x_n\}`$ con $`x_n \in D \setminus \{a\}`$, $`x_n \to a`$, se tiene $`f(x_n) \to A`$.

### Diapositiva impresa 11. Observaciones sobre la definición de límite

1. La condición de que $`a`$ sea punto de acumulación de $`D`$ implica que $`V(a) \cap D \ne \varnothing`$ para todo entorno de $`a`$, y que existe una sucesión $`\{x_n\}`$ con $`x_n \in D`$, $`x_n \ne a`$, $`x_n \to a`$.
2. La existencia del límite de una función en $`a`$ es una propiedad **local**: depende del comportamiento de la función en cualquier entorno prefijado del punto.
3. El valor de $`f`$ en $`a`$ no interviene en la definición del límite en $`a`$. Por ello, para la existencia y el valor del límite en $`a`$ es irrelevante si $`f`$ está definida en $`a`$ y, en su caso, cómo lo está.

### Diapositiva impresa 12. Equivalencia de las definiciones

<a id="thm-2-4-1"></a>**Teorema 2.4.1.** Las definiciones del límite de una función por Cauchy y por Heine son equivalentes.

## Página manuscrita 10 (p. PDF 10). Figura para la definición $`\varepsilon`$–$`\delta`$

Ilustración (manuscrita): gráfica de $`f(x)`$, una recta horizontal a la altura $`A`$, el punto $`a`$ en el eje $`x`$; los intervalos $`(a-\delta, a+\delta)`$ (verde) y $`(a-\tilde\delta, a+\tilde\delta)`$ (naranja); una franja de anchura $`\varepsilon`$ alrededor de $`A`$ (flechas verde y naranja); el punto $`x`$ (rojo) en el $`\delta`$-entorno de $`a`$.

![Página manuscrita 10: gráfica de f(x), la franja ε alrededor de A y el entorno δ de a](../../assets/lectures-2025-26/lec14-p10-epsilon-delta.jpg)

## Página manuscrita 13 (p. PDF 13). Demostración del teorema 2.4.1

**Demostración ([teorema 2.4.1](#thm-2-4-1)).** Para fijar ideas, demostremos el teorema para $`a, A \in \mathbb{R}`$.

**①** Sea $`A`$ el límite de $`f`$ por Cauchy. Probemos que entonces $`A`$ también es el límite de $`f`$ por Heine.

Tomemos $`\{x_n\}`$ con $`x_n \in D`$, $`x_n \ne a`$, $`x_n \to a`$. Hay que probar que $`f(x_n) \to A`$.

Tomemos $`\forall \varepsilon > 0`$. Por la definición de Cauchy, $`\exists \delta > 0`$: $`\forall x \in D`$, $`x \ne a`$, $`|x - a| < \delta`$ $`\Rightarrow`$ $`|f(x) - A| < \varepsilon`$.

Como $`x_n \to a`$, $`\exists N`$ $`\forall n > N`$: $`|x_n - a| < \delta`$. Pero entonces $`|f(x_n) - A| < \varepsilon`$. Esto significa exactamente que $`f(x_n) \to A`$.

**②** Sea $`A`$ el límite de $`f`$ en $`a`$ por Heine. Probemos que $`A`$ también es el límite por Cauchy. (Continúa en la página siguiente.)

## Página manuscrita 14 (p. PDF 14). Demostración del teorema 2.4.1, punto ②

Demostremos por reducción al absurdo que $`A`$ es el límite de $`f`$ por Cauchy. Supongamos que $`A`$ no es límite por Cauchy, es decir,

```math
\exists \varepsilon^* > 0\ \ \forall \delta > 0\ \ \exists x \text{ (que depende de } \delta\text{)}: \quad x \in D,\ x \ne a,\ |x - a| < \delta,\ |f(x) - A| \ge \varepsilon^*.
```

Entonces, para cada $`n \in \mathbb{N}`$, tomando $`\delta = \frac{1}{n}`$, hallamos un punto $`x_n`$ tal que $`x_n \in D`$, $`x_n \ne a`$, $`|x_n - a| < \frac{1}{n}`$, $`|f(x_n) - A| \ge \varepsilon^*`$.

Entonces $`0 < |x_n - a| < \frac{1}{n}`$ $`\Rightarrow`$ por el [teorema del emparedado](lecture-08.md#thm-2-1-4) $`x_n \to a`$. Pero entonces, por la definición de Heine, $`f(x_n) \to A`$, lo que contradice la desigualdad $`|f(x_n) - A| \ge \varepsilon^*`$.

## Diapositiva impresa 15. Unicidad del límite de una función

<a id="thm-2-4-2"></a>**Teorema 2.4.2.** Una función no puede tener más de un límite en un punto dado: si $`f : D \subset \mathbb{R} \to \mathbb{R}`$, $`a`$ es punto de acumulación de $`D`$, $`A, B \in \mathbb{R}`$, $`f(x) \xrightarrow[x\to a]{} A`$ y $`f(x) \xrightarrow[x\to a]{} B`$, entonces $`A = B`$.

## Diapositiva impresa 16 con una anotación manuscrita en azul. Acotación local

<a id="thm-2-4-3"></a>**Teorema 2.4.3.** Sea $`f : D \subset \mathbb{R} \to \mathbb{R}`$, sea $`a`$ punto de acumulación de $`D`$, $`A \in \mathbb{R}`$, y $`f(x) \xrightarrow[x\to a]{} A`$. Entonces existe un entorno $`V(a)`$ de $`a`$ tal que $`f`$ está acotada en $`V(a) \cap D`$.

Manuscrito (en azul): $`f(x) \to A`$ cuando $`x \to a`$ $`\Leftrightarrow`$ $`\forall \varepsilon > 0\ \exists \delta > 0`$: $`|x - a| < \delta`$, $`|f(x) - A| < \varepsilon`$.

## Página manuscrita 17 (p. PDF 17). Ejemplo

**Ejemplo.** $`f(x) = x`$, $`\lim\limits_{x\to 3} f(x) = 3`$.

Figura manuscrita: la gráfica de $`f(x) = x`$; sobre el eje $`x`$ se marcan $`3`$ y $`3 + \varepsilon`$; se destaca la parte de la gráfica que corresponde a este intervalo. A la derecha, el entorno de $`a`$: $`(a-\delta, a+\delta)`$; $`|x - a| < \delta \iff a - \delta < x < a + \delta \iff x \in V_\delta(a)`$.

> **Nota del editor.** En el manuscrito no se escribe explícitamente la elección $`\delta = \varepsilon`$.

## Página manuscrita 18 (p. PDF 18). Demostración del teorema 2.4.3

**Demostración ([teorema 2.4.3](#thm-2-4-3)).** Por la definición de límite para $`\varepsilon = 1`$: $`\exists V(a)`$: $`\forall x \in \dot V(a) \cap D`$: $`|f(x) - A| < 1`$.

$`\big||f(x)| - |A|\big| \le |f(x) - A| < 1`$ $`\Rightarrow`$ $`|f(x)| < 1 + |A|`$.

Si $`a \notin D`$, entonces $`V(a) \cap D = \dot V(a) \cap D`$, y la demostración termina.

Si $`a \in D`$, entonces $`\forall x \in V(a) \cap D`$: $`|f(x)| \le \max\{|A| + 1,\ |f(a)|\}`$.

En la parte inferior de la página hay un esbozo (observación): la gráfica de una función con un punto $`c \notin D`$ (una vertical discontinua en $`c`$; curvas rojas a izquierda y derecha de $`c`$).
