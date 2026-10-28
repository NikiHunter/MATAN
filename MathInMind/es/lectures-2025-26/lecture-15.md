---
title: "Lección 15 — Conservación del signo, aritmética de límites de funciones, composición, límites laterales, funciones monótonas, criterio de Cauchy para funciones"
lang: es
course: "Análisis Matemático, 2025/26"
lecture: 15
date: 2025-10-23
source: "ма25_26_лекция_15_notes_pdf.pdf"
---
# Lección 15 — Propiedades de los límites de funciones, límites laterales, criterio de Cauchy

[← Lección 14](lecture-14.md) · [Índice de lecciones](index.md) · [Lección 16 →](lecture-16.md) · [Términos y teoremas](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-15.md) · [English](../../en/lectures-2025-26/lecture-15.md)

> **Fuente:** `ма25_26_лекция_15_notes_pdf.pdf` — 24 páginas: diapositivas impresas con capa de texto (páginas 1–4, 6, 9–10, 12–13, 15–16, 18–19, 22) y páginas manuscritas sin capa de texto utilizable (páginas 5, 7–8, 11, 14, 17, 20, 21, 23–24). Las páginas 12 y 18 son diapositivas impresas con anotaciones manuscritas en azul. Las páginas manuscritas se transcribieron a partir de su imagen. Los números de página del PDF aparecen en los encabezados.
>
> **Nota del editor.** La fecha de la lección se toma del pie de las diapositivas («23 de octubre de 2025»). La «cita del día» de la página 2 es una broma; sus fórmulas se reproducen tal como aparecen en la imagen.

## Diapositivas impresas 1–3. Introducción

**Cita del día (diapositiva 2).** «MÉTODOS TÍPICOS DE DEMOSTRACIÓN»:

- *Demostración por intimidación:* «Como es fácil ver, $`\left|\bigoplus_{\kappa\in S}(\Re^{F^\alpha(i)})_{i\in U_\kappa}\right| \preceq \aleph_1`$ siempre que $`[\mathfrak{H}]_W \cap F^\alpha(\mathbb{N}) \ne \varnothing`$.»
- *Demostración por enredo:* «Esta afirmación es una reformulación de la proposición 5.3.18, que se deduce del teorema 7.1.24, basado en el lema 2.4.14, que es consecuencia del teorema 7.1.24 y de la proposición 5.3.18.»
- *Demostración por autoridad:* «Obvio.»

**Objetivo de la lección.** Demostrar el teorema sobre la conservación del signo. Considerar las operaciones aritméticas con funciones que tienen límite. Demostrar resultados sobre el límite de una composición, sobre el paso al límite en una desigualdad para funciones y sobre el [teorema del emparedado](lecture-08.md#thm-2-1-4) para funciones. Definir los [límites laterales](#def-2-4-5) por la izquierda y por la derecha. Demostrar teoremas sobre el [límite de una función](lecture-14.md#def-2-4-4) monótona y estudiar el [criterio de Bolzano–Cauchy](lecture-13.md#thm-2-3-7) para funciones.

## §4. Límite de una función (continuación)

### Diapositiva impresa 4. Conservación del signo

<a id="thm-2-4-4"></a>**Teorema 2.4.4.** Sea $`g : D \subset \mathbb{R} \to \mathbb{R}`$, sea $`a`$ punto de acumulación de $`D`$, y sea $`\lim\limits_{x\to a} g(x) = B \in \mathbb{R} \setminus \{0\}`$. Entonces existe un entorno $`V(a)`$ tal que $`g(x)`$ y $`B`$ tienen el mismo signo en $`\dot V(a) \cap D`$; en particular, $`g(x) \ne 0`$ para todo $`x \in \dot V(a) \cap D`$.

La última afirmación vale también en el caso $`\lim\limits_{x\to a} g(x) = \infty`$ (la diapositiva muestra este caso con el símbolo «1» en la capa de texto, que representa $`\infty`$).

### Página manuscrita 5 (p. PDF 5). Demostración del teorema 2.4.4

**Demostración ([teorema 2.4.4](#thm-2-4-4)).** Consideremos, para fijar ideas, $`B > 0`$ (encerrado en rojo).

Supongamos que el enunciado del [teorema 2.4.4](#thm-2-4-4) es falso. Entonces, para todo $`n \in \mathbb{N}`$, existe $`x_n \in \dot V_{1/n}(a) \cap D`$ con $`g(x_n) \le 0`$.

Pero $`x_n \to a`$. Entonces $`g(x_n) \to B`$ $`\Rightarrow`$ por el teorema del paso al límite en una desigualdad para sucesiones, $`B \le 0`$ (encerrado), lo que contradice la hipótesis $`B > 0`$ (flecha roja «contradicción»).

### Diapositiva impresa 6. Operaciones aritméticas con funciones

<a id="thm-2-4-5"></a>**Teorema 2.4.5.** Sean $`f, g : D \subset \mathbb{R} \to \mathbb{R}`$, sea $`a`$ punto de acumulación de $`D`$, $`A, B \in \mathbb{R}`$, $`f(x) \xrightarrow[x\to a]{} A`$, $`g(x) \xrightarrow[x\to a]{} B`$. Entonces

1. $`f(x) \pm g(x) \to A \pm B`$;
2. $`f(x) g(x) \to AB`$;
3. $`|f(x)| \to |A|`$;
4. si, además, $`B \ne 0`$, entonces $`\dfrac{f(x)}{g(x)} \to \dfrac{A}{B}`$.

### Páginas manuscritas 7–8 (p. PDF 7–8). Demostración del punto 1 y observación

**Demostración ([teorema 2.4.5](#thm-2-4-5)).** Demostremos el punto ① para la suma.

Tomemos $`\{x_n\}`$ con $`x_n \in D`$, $`x_n \ne a`$, $`x_n \to a`$. Por la definición de Heine, $`f(x_n) \to A`$ y $`g(x_n) \to B`$. Por el teorema del límite de una suma para sucesiones, $`f(x_n) + g(x_n) \to A + B`$.

Como $`\{x_n\}`$ era arbitraria, $`f(x) + g(x) \to A + B`$ cuando $`x \to a`$.

**Observación (manuscrita).** Al demostrar el punto ④ (el límite de un cociente) hay que tener en cuenta que, por el [teorema 2.4.4](#thm-2-4-4), existe $`V(a)`$ en el que $`\dfrac{f}{g}`$ está definida, al menos en $`\dot V(a) \cap D`$.

**Observación (manuscrita, página 8).** El [teorema 2.4.5](#thm-2-4-5) vale también para límites infinitos, excepto para las indeterminaciones $`\infty - \infty`$, $`0 \cdot \infty`$, $`\dfrac{0}{0}`$ y $`\dfrac{\infty}{\infty}`$. Encerrado: $`\dfrac{\infty}{0} = \infty`$.

### Diapositiva impresa 9. Funciones infinitésimas e infinitamente grandes

La definición de infinitésimo e [infinitamente grande](lecture-09-10.md#def-2-2-4) se traslada a las funciones. Así, una función que tiende a cero en $`a`$ se llama **infinitésima** en $`a`$. Siguen valiendo las afirmaciones de que el producto de una función infinitésima por una función acotada es infinitésimo, y la relación entre infinitésimos e infinitos.

### Diapositiva impresa 10. Límite de una composición

<a id="thm-2-4-6"></a>**Teorema 2.4.6.** Sean $`f : D \subset \mathbb{R} \to \mathbb{R}`$, $`g : E \subset \mathbb{R} \to \mathbb{R}`$, $`f(D) \subset E`$, $`a, A, B \in \overline{\mathbb{R}}`$, y supongamos que:

1. $`a`$ es [punto de acumulación](lecture-14.md#def-2-4-1) de $`D`$, y $`f(x) \xrightarrow[x\to a]{} A`$;
2. $`A`$ es punto de acumulación de $`E`$, y $`g(x) \xrightarrow[x\to A]{} B`$;
3. existe un entorno $`V(a)`$ de $`a`$ tal que $`f(x) \ne A`$ para todo $`x \in \dot V(a) \cap D`$.

Entonces $`(g \circ f)(x) \xrightarrow[x\to a]{} B`$.

### Página manuscrita 11 (p. PDF 11). Demostración del teorema 2.4.6

**Demostración ([teorema 2.4.6](#thm-2-4-6)).** Tomemos $`\{x_n\}`$ con $`x_n \in D`$, $`x_n \ne a`$, $`x_n \to a`$, y denotemos $`f(x_n) = y_n`$.

Entonces $`y_n \in E`$, $`y_n \to A`$ (por la definición de Heine). Además, a partir de cierto índice, $`x_n \in V(a)`$. Entonces $`y_n \ne A`$ para tales $`n`$.

Así, $`\{y_n\}`$ tiene las propiedades $`y_n \in E`$, $`y_n \ne A`$, $`y_n \to A`$ $`\Rightarrow`$ por la definición de Heine $`g(y_n) \to B`$, es decir, $`(g \circ f)(x_n) \to B`$.

Como $`\{x_n\}`$ era arbitraria, $`(g \circ f)(x) \to B`$ cuando $`x \to a`$.

> **Nota del editor.** En el manuscrito, la línea con $`y_n \to A`$ dice «$`x_n \mapsto A`$»; por su sentido, es $`y_n \to A`$.

### Diapositiva impresa 12 con una anotación manuscrita en azul. Paso al límite en una desigualdad

<a id="thm-2-4-7"></a>**Teorema 2.4.7.** Sean $`f, g : D \subset \mathbb{R} \to \mathbb{R}`$, sea $`a`$ punto de acumulación de $`D`$, $`f(x) \le g(x)`$ para todo $`x \in D \setminus \{a\}`$, $`A, B \in \overline{\mathbb{R}}`$, $`f(x) \xrightarrow[x\to a]{} A`$, $`g(x) \xrightarrow[x\to a]{} B`$. Entonces $`A \le B`$.

Manuscrito (en azul): «Demostración: tomemos $`\{x_n\}`$ con $`x_n \in D`$, $`x_n \ne a`$, $`x_n \to a`$ $`\Rightarrow`$ $`f(x_n) \to A`$, $`g(x_n) \to B`$. Para todo $`x \in D \setminus \{a\}`$: $`f(x) \le g(x)`$ $`\Rightarrow`$ $`f(x_n) \le g(x_n)`$ $`\Rightarrow`$ por el teorema del paso al límite en una desigualdad, $`A \le B`$.»

### Diapositiva impresa 13. Sobre la función del emparedado

<a id="thm-2-4-8"></a>**Teorema 2.4.8.** Sean $`f, g, h : D \subset \mathbb{R} \to \mathbb{R}`$, sea $`a`$ punto de acumulación de $`D`$, $`f(x) \le g(x) \le h(x)`$ para todo $`x \in D \setminus \{a\}`$, $`A \in \mathbb{R}`$, $`f(x) \xrightarrow[x\to a]{} A`$ y $`h(x) \xrightarrow[x\to a]{} A`$. Entonces también $`g(x) \xrightarrow[x\to a]{} A`$.

### Página manuscrita 14 (p. PDF 14). Observación sobre la comparación de límites

Si $`f(x) \le g(x)`$ para todo $`x \in D \setminus \{a\}`$ y $`f(x) \to +\infty`$ cuando $`x \to a`$, entonces también $`g(x) \to +\infty`$ cuando $`x \to a`$.

Análogamente: si $`f(x) \le g(x)`$ para todo $`x \in D \setminus \{a\}`$ y $`g(x) \to -\infty`$ cuando $`x \to a`$, entonces también $`f(x) \to -\infty`$ cuando $`x \to a`$.

## §4. Límites laterales

### Diapositiva impresa 15. Límite a lo largo de un conjunto

<a id="def-2-4-5"></a>**Definición 2.4.5.** Sean $`f : D \subset \mathbb{R} \to \mathbb{R}`$, $`D_1 \subset D`$, y sea $`a`$ punto de acumulación de $`D_1`$. El límite $`\lim\limits_{x\to a} f\big|_{D_1}(x)`$ se llama **límite de la función $`f`$ en el punto $`a`$ a lo largo del conjunto $`D_1`$**.

### Diapositiva impresa 16. Límites laterales por la izquierda y por la derecha

<a id="def-2-4-6"></a>**Definición 2.4.6.** Sean $`f : D \subset \mathbb{R} \to \mathbb{R}`$, $`a \in \mathbb{R}`$.

1. Si $`a`$ es punto de acumulación del conjunto $`D_1 = D \cap (-\infty, a)`$, el límite de $`f`$ en $`a`$ a lo largo de $`D_1`$ se llama **límite lateral por la izquierda** de $`f`$ en $`a`$, y se denota $`\lim\limits_{x\to a^-} f(x)`$.
2. Si $`a`$ es punto de acumulación del conjunto $`D_2 = D \cap (a, +\infty)`$, el límite de $`f`$ en $`a`$ a lo largo de $`D_2`$ se llama **límite lateral por la derecha** de $`f`$ en $`a`$, y se denota $`\lim\limits_{x\to a^+} f(x)`$.

### Página manuscrita 17 (p. PDF 17). Definiciones mediante $`\varepsilon`$–$`\delta`$ y ejemplo

$`\lim\limits_{x\to a^-} f(x) = A`$ significa: $`\forall \varepsilon > 0\ \exists \delta > 0\ \forall x \in D`$: $`0 < a - x < \delta`$ $`\Rightarrow`$ $`|f(x) - A| < \varepsilon`$.

$`\lim\limits_{x\to a^+} f(x) = A`$ significa: $`\forall \varepsilon > 0\ \exists \delta > 0\ \forall x \in D`$: $`0 < x - a < \delta`$ $`\Rightarrow`$ $`|f(x) - A| < \varepsilon`$.

**Ejemplo (manuscrito).** Gráfica de $`f(x)`$ con una [discontinuidad de salto](lecture-16.md#def-2-5-4) en $`x = 2`$: $`f(2) = 100`$ (punto relleno), límite lateral por la izquierda $`50`$ (círculo vacío sobre la recta que parte de $`(0, 0)`$). Etiquetas: $`\lim\limits_{x\to 2^-} f(x) = 50`$; $`\lim\limits_{x\to 2^+} f(x) = 100`$.

### Diapositiva impresa 18 con una anotación manuscrita en azul. El límite mediante límites laterales

**Observación (impresa).** Sean $`f : D \subset \mathbb{R} \to \mathbb{R}`$, $`a \in \mathbb{R}`$, $`D_1 = D \cap (-\infty, a)`$, $`D_2 = D \cap (a, +\infty)`$, y sea $`a`$ punto de acumulación de $`D_1`$ y de $`D_2`$. Entonces, para que exista el límite de $`f`$ en $`a`$, es necesario y suficiente que existan los límites laterales de $`f`$ en $`a`$ y que sean iguales entre sí.

Manuscrito (en azul):

«Demostración.
(⇒) $`\exists \lim\limits_{x\to a} f(x) = A`$ $`\Rightarrow`$ $`\exists \lim\limits_{x\to a^-} f(x) = \lim\limits_{x\to a^+} f(x) = A`$.
(⇐) $`\exists \lim\limits_{x\to a^-} f = \lim\limits_{x\to a^+} f = A`$ $`\Rightarrow`$ $`\forall V(A)`$ $`\exists \delta_1, \delta_2 > 0`$ tales que $`f(x) \in V(A)`$ para todo $`x \in D`$ con $`0 < a - x < \delta_1`$, y para todo $`x \in D`$ con $`0 < x - a < \delta_2`$ $`\Rightarrow`$ con $`\delta = \min\{\delta_1, \delta_2\}`$: $`f(x) \in V(a)`$ para todo $`x \in D`$ con $`|x - a| < \delta`$.»

> **Nota del editor.** En la última línea del manuscrito se escribe $`V(a)`$; por su sentido, es $`V(A)`$.

## §4. Funciones monótonas

### Diapositiva impresa 19. Sobre el límite de una función monótona

<a id="thm-2-4-9"></a>**Teorema 2.4.9.** Sean $`f : D \subset \mathbb{R} \to \mathbb{R}`$, $`a \in (-\infty, +\infty]`$, $`D_1 = D \cap (-\infty, a)`$, y sea $`a`$ punto de acumulación de $`D_1`$.

1. Si $`f`$ es creciente y está [acotada superiormente](lecture-05-06.md#def-1-3-7) en $`D_1`$, entonces existe el límite finito $`\lim\limits_{x\to a^-} f(x)`$.
2. Si $`f`$ es decreciente y está acotada inferiormente en $`D_1`$, entonces existe el límite finito $`\lim\limits_{x\to a^-} f(x)`$.

### Páginas manuscritas 20–21 (p. PDF 20–21). Demostración del teorema 2.4.9

**Demostración ([teorema 2.4.9](#thm-2-4-9)).** Demostramos ①; ② se demuestra de forma análoga.

Pongamos $`A = \sup\limits_{x \in D_1} f(x)`$ $`\Rightarrow`$ $`A \in \mathbb{R}`$, ya que $`f`$ está acotada superiormente en $`D_1`$. Veamos que $`f(a^-) = A`$.

Tomemos $`\varepsilon > 0`$. Por la definición de [supremo](lecture-11-12.md#def-2-3-1), $`\exists x_0 \in D_1`$: $`f(x_0) > A - \varepsilon`$.

Recordemos que $`f`$ es creciente en $`D_1`$ $`\Rightarrow`$ $`\forall x \in D_1`$, $`x > x_0`$: $`A - \varepsilon < f(x_0) \le f(x) \le A < A + \varepsilon`$.

Pongamos $`\delta = a - x_0`$ si $`a \in \mathbb{R}`$, o $`\Delta = \max\{x_0, 1\}`$ si $`a = +\infty`$. Entonces, para todo $`x \in D_1`$ con $`0 < a - x < \delta`$ (o para todo $`x \in D_1`$ con $`x > \Delta`$ si $`a = +\infty`$), se tiene $`A - \varepsilon < f(x) < A + \varepsilon`$, es decir, $`|f(x) - A| < \varepsilon`$.

**Observación (manuscrita, página 21).** Un enunciado análogo vale para el límite por la derecha. Sean $`f : D \subset \mathbb{R} \to \mathbb{R}`$, $`a \in [-\infty, +\infty)`$, $`D_2 = D \cap (a, +\infty)`$, y sea $`a`$ punto de acumulación de $`D_2`$.

1. Si $`f`$ es creciente y está acotada inferiormente en $`D_2`$, entonces existe el límite finito $`\lim\limits_{x\to a^+} f(x)`$.
2. Si $`f`$ es decreciente y está acotada superiormente en $`D_2`$, entonces existe el límite finito $`\lim\limits_{x\to a^+} f(x)`$.
3. Si $`f`$ es creciente y no está acotada superiormente en $`D_1`$, entonces $`\lim\limits_{x\to a^-} f(x) = +\infty`$.
4. Si $`f`$ es decreciente y no está acotada inferiormente en $`D_1`$, entonces $`\lim\limits_{x\to a^-} f(x) = -\infty`$.

Para $`D_2`$ valen afirmaciones análogas a las de los puntos 3 y 4.

## §4. Criterio de Bolzano–Cauchy para funciones

### Diapositiva impresa 22. Criterio de Bolzano–Cauchy

<a id="thm-2-4-10"></a>**Teorema 2.4.10.** Sean $`f : D \subset \mathbb{R} \to \mathbb{R}`$, y $`a`$ punto de acumulación de $`D`$. Entonces la existencia de un límite finito de $`f`$ en $`a`$ es equivalente a la siguiente afirmación:

```math
\forall \varepsilon > 0\ \exists V(a)\ \forall x, \hat{x} \in \dot V(a) \cap D: \quad |f(x) - f(\hat{x})| < \varepsilon.
```

### Páginas manuscritas 23–24 (p. PDF 23–24). Demostración del teorema 2.4.10

**Demostración ([teorema 2.4.10](#thm-2-4-10)).**

**①** Sea $`\lim\limits_{x\to a} f(x) = A \in \mathbb{R}`$. Tomemos $`\varepsilon > 0`$. Por la definición de límite, $`\exists V(a)`$: $`|f(x) - A| < \frac{\varepsilon}{2}`$ para todo $`x \in \dot V(a) \cap D`$.

Entonces, para $`x, \hat x \in \dot V(a) \cap D`$:

```math
|f(x) - f(\hat x)| = |f(x) - A + A - f(\hat x)| \le |f(x) - A| + |A - f(\hat x)| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
```

Como $`\varepsilon`$ era arbitrario, obtenemos: para todo $`x, \hat x \in \dot V(a) \cap D`$, $`|f(x) - f(\hat x)| < \varepsilon`$.

**②** Supongamos que se cumple la condición $`(*)`$: $`\forall \varepsilon > 0\ \exists V(a)`$: $`\forall x, \hat x \in \dot V(a) \cap D`$: $`|f(x) - f(\hat x)| < \varepsilon`$.

Tomemos $`\{x_n\}`$ con $`x_n \in D`$, $`x_n \ne a`$, $`x_n \to a`$.

$`x_n \to a`$ $`\Rightarrow`$ por la definición de [límite de una sucesión](lecture-08.md#def-2-1-2), $`\exists N`$: $`\forall n > N`$, $`x_n \in \dot V(a) \cap D`$.

Por $`(*)`$: $`\forall n, l > N`$: $`|f(x_n) - f(x_l)| < \varepsilon`$ $`\Rightarrow`$ $`\{f(x_n)\}`$ es una [sucesión de Cauchy](lecture-13.md#def-2-3-10) $`\Rightarrow`$ $`\{f(x_n)\}`$ tiene límite finito.

(En el manuscrito no se registra la demostración de la unicidad del límite para distintas sucesiones.)
