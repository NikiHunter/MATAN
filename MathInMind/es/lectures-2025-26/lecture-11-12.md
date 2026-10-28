---
title: "Lecciones 11–12 — Cotas exactas, sucesiones monótonas, el número e, subsucesiones, teorema de Bolzano–Weierstrass"
lang: es
course: "Análisis Matemático, 2025/26"
lecture: "11–12"
date: 2025-10-09
source: "ma25_26-lectures_11-12_notes.pdf"
---
# Lecciones 11–12 — Cotas exactas, sucesiones monótonas, subsucesiones

[← Lecciones 9–10](lecture-09-10.md) · [Índice de lecciones](index.md) · [Lección 13 →](lecture-13.md) · [Términos y teoremas](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-11-12.md) · [English](../../en/lectures-2025-26/lecture-11-12.md)

> **Fuente:** `ma25_26-lectures_11-12_notes.pdf` — 37 páginas: diapositivas impresas con capa de texto (páginas 1–5, 8–10, 16, 18–20, 23, 26–28, 31, 34–35) y páginas manuscritas sin capa de texto utilizable (páginas 6–7, 11–15, 21–22, 24–25, 29–30, 32–33, 36–37). Las páginas manuscritas se transcribieron a partir de su imagen. Las diapositivas impresas 27 y 34 contienen anotaciones manuscritas y se presentan a continuación con dichas anotaciones. Los números de página del PDF aparecen en los encabezados.
>
> **Nota del editor.** Los números de definiciones, teoremas y lemas se conservan tal como aparecen en la fuente. La fecha de la lección se toma del pie de las diapositivas («9 de octubre de 2025»).

## Diapositivas impresas 1–5. Introducción y intervalos encajados

**Cita del día:** «¡Si tiene tiempo libre, significa que se ha olvidado de hacer algo!»

**Objetivo de la lección.** Investigar la existencia de [cotas superiores](../02-real-numbers.md#sec-2-2) e inferiores. Demostrar el [teorema de los intervalos encajados](#thm-2-3-1). Estudiar sup e inf, máx y mín. Demostrar el teorema sobre el [límite de una sucesión](lecture-08.md#def-2-1-2) monótona. Definir el número $`e`$. Introducir las [subsucesiones](#def-2-3-7), los límites de subsucesiones y los [límites parciales](#def-2-3-8) de una sucesión. Demostrar lemas sobre las propiedades de los límites de subsucesiones. Justificar el principio de selección de [Bolzano–Weierstrass](#thm-2-3-4).

### §3. Cotas exactas de conjuntos numéricos y sucesiones monótonas

**Definición (intervalos encajados).** Se dice que $`\{[a_n, b_n]\}_{n=1}^{\infty}`$ es una **sucesión de intervalos encajados** si

```math
a_n \le a_{n+1} \le b_{n+1} \le b_n \quad \text{para todo } n \quad \text{y} \quad b_n - a_n \to 0.
```

<a id="thm-2-3-1"></a>**Teorema 2.3.1 (de los intervalos encajados).** Sea $`\{[a_n, b_n]\}_{n=1}^{\infty}`$ una sucesión de intervalos encajados. Entonces

```math
\exists c \in \mathbb{R}: \quad \bigcap_{n=1}^{\infty} [a_n, b_n] = \{c\},
```

y además $`a_n \to c`$ y $`b_n \to c`$.

### Página manuscrita 6 (p. PDF 6). Demostración del teorema 2.3.1

**Demostración ([teorema 2.3.1](#thm-2-3-1)).**

**①** Que $`\bigcap_{n=1}^{\infty}[a_n, b_n] \ne \varnothing`$ lo sabemos por el axioma de los intervalos encajados.

**②** Sean $`c, d \in \bigcap_{n=1}^{\infty}[a_n, b_n]`$. Probemos que $`c = d`$.

```math
a_n \le c \le b_n,\quad a_n \le d \le b_n,\quad \forall n \in \mathbb{N} \ \Rightarrow\ a_n - b_n \le c - d \le b_n - a_n.
```

Cuando $`n \to \infty`$, ambas partes extremas tienden a $`0`$ (flechas en el manuscrito). Por el teorema del paso al límite en una desigualdad, $`0 \le c - d \le 0`$, es decir, $`c = d`$.

### Página manuscrita 7 (p. PDF 7). Continuación: $`a_n \to c`$, $`b_n \to c`$

**③** Falta probar que $`a_n \to c`$ y $`b_n \to c`$.

De $`a_n \le c \le b_n`$ se sigue que $`0 \le c - a_n \le b_n - a_n \to 0`$, luego $`c - a_n \to 0`$, es decir, $`a_n \to c`$.

Análogamente para $`b_n`$: en el manuscrito se lee «$`b_n - b_n \le b_n - c \le b_n - a_n`$» (con «$`= 0`$» subrayado); por su sentido, $`0 \le b_n - c \le b_n - a_n \to 0`$, de donde $`b_n \to c`$.

> **Nota del editor.** En el lado izquierdo de la desigualdad para $`b_n`$, el manuscrito dice «$`b_n - b_n`$»; por su sentido es $`0`$ (subrayado como «$`=0`$»). Corregido solo en esta nota; el texto manuscrito no se ha modificado.

Recordatorio: $`E \subset \mathbb{R}`$ se llama **acotado superiormente** si $`\exists M \in \mathbb{R}: x \le M\ \forall x \in E`$; el número $`M`$ se llama cota superior de $`E`$.

### Diapositivas impresas 8–9. Cotas exactas

<a id="def-2-3-1"></a>**Definición 2.3.1.** Sea $`E \subset \mathbb{R}`$, $`E \ne \varnothing`$, acotado superiormente. La menor de las cotas superiores de $`E`$ se llama **cota superior exacta** (supremo) de $`E`$ y se denota $`\sup E`$.

<a id="def-2-3-2"></a>**Definición 2.3.2.** Sea $`E \subset \mathbb{R}`$, $`E \ne \varnothing`$, acotado inferiormente. La mayor de las cotas inferiores de $`E`$ se llama **cota inferior exacta** (ínfimo) de $`E`$ y se denota $`\inf E`$.

**Definición de sup e inf mediante desigualdades.**

```math
b = \sup E \iff \begin{cases} \forall x \in E: x \le b, \\ \forall \varepsilon > 0\ \exists x \in E: x > b - \varepsilon; \end{cases}
\qquad
a = \inf E \iff \begin{cases} \forall x \in E: x \ge a, \\ \forall \varepsilon > 0\ \exists x \in E: x < a + \varepsilon. \end{cases}
```

### Diapositiva impresa 10. Existencia de cotas exactas

<a id="thm-2-3-2"></a>**Teorema 2.3.2.** Todo subconjunto no vacío de $`\mathbb{R}`$ acotado superior (inferiormente) tiene cota superior (inferior) exacta.

**Observación.** Si un conjunto no está [acotado superiormente](lecture-05-06.md#def-1-3-7) (inferiormente), se pone $`\sup E = +\infty`$ ($`\inf E = -\infty`$). Con esta convención, el [supremo](#def-2-3-1) y el [ínfimo](#def-2-3-2) existen en $`\mathbb{R}`$ para todo conjunto no vacío. La acotación superior (inferior) equivale a la desigualdad $`\sup E < +\infty`$ ($`\inf E > -\infty`$).

### Página manuscrita 11 (p. PDF 11). Demostración del teorema 2.3.2

**Demostración ([teorema 2.3.2](#thm-2-3-2)).** Para fijar ideas, probemos el teorema para un conjunto acotado superiormente. La segunda afirmación (conjunto acotado inferiormente) se prueba de forma análoga.

Sea $`E \subset \mathbb{R}`$, $`E \ne \varnothing`$, acotado superiormente: $`\exists M \in \mathbb{R}: x \le M\ \forall x \in E`$. Tomemos $`x_0 \in E`$; entonces $`x_0 \le M`$. Denotemos $`[a_1, b_1] := [x_0, M]`$. El intervalo $`[a_1, b_1]`$ cumple dos condiciones:

① $`[a_1, b_1] \cap E \ne \varnothing`$; ② $`(b_1, +\infty) \cap E = \varnothing`$.

### Página manuscrita 12 (p. PDF 12). Continuación: bisección

Consideremos el punto medio de $`[a_1, b_1]`$: $`\dfrac{a_1 + b_1}{2} = \dfrac{x_0 + M}{2}`$. Son posibles dos casos:

- **①** Si $`\left(\dfrac{a_1 + b_1}{2}, b_1\right] \cap E = \varnothing`$, ponemos $`[a_2, b_2] = \left[a_1, \dfrac{a_1 + b_1}{2}\right]`$.
- **②** Si $`\left(\dfrac{a_1 + b_1}{2}, b_1\right] \cap E \ne \varnothing`$, ponemos $`[a_2, b_2] = \left[\dfrac{a_1 + b_1}{2}, b_2\right]`$.

En cualquiera de los casos ① o ② tenemos $`[a_2, b_2] \cap E \ne \varnothing`$ y $`(b_2, +\infty) \cap E = \varnothing`$.

![Página manuscrita 12: el intervalo [x₀, M], su punto medio y las dos opciones de mitad](../../assets/lectures-2025-26/lec11-12-p12-bisection-sup.jpg)

> **Nota del editor.** En la variante ② el manuscrito dice $`[a_2, b_2] = [\ldots, b_2]`$; por su sentido, el extremo derecho coincide con $`b_1`$ (es decir, $`b_2 = b_1`$). El texto manuscrito se conserva sin cambios.

### Página manuscrita 13 (p. PDF 13). Continuación de la construcción

A continuación, consideramos el punto medio de $`[a_2, b_2]`$ y seguimos el proceso…

Como resultado hemos construido una sucesión de intervalos encajados con las propiedades

```math
\text{<1>}\ \ [a_n, b_n] \cap E \ne \varnothing, \qquad \text{<2>}\ \ (b_n, +\infty) \cap E = \varnothing.
```

Además, $`b_n - a_n = \dfrac{b_{n-1} - a_{n-1}}{2} = \dots = \dfrac{b_1 - a_1}{2^{n-1}} \to 0`$ cuando $`n \to \infty`$.

Entonces, por el teorema de los intervalos encajados ([teorema 2.3.1](#thm-2-3-1)), existe un único punto $`c \in \bigcap_{n=1}^{\infty}[a_n, b_n]`$, y $`a_n \to c`$, $`b_n \to c`$.

Comprobemos ahora que $`c = \sup E`$.

### Página manuscrita 14 (p. PDF 14). La cota superior

Tomemos $`x \in E`$. Por la propiedad <2>, $`x \le b_n`$ para todo $`n \in \mathbb{N}`$. Pasando al límite cuando $`n \to \infty`$ ($`b_n \to c`$), por el teorema del paso al límite en una desigualdad obtenemos $`x \le c`$, es decir, $`c`$ es cota superior de $`E`$.

Tomemos $`\varepsilon > 0`$ y veamos que $`c - \varepsilon`$ no es cota superior de $`E`$. Como $`a_n \to c`$, existe $`N`$ tal que $`\forall n > N`$: $`|a_n - c| < \varepsilon`$, es decir, $`c - \varepsilon < a_n < c + \varepsilon`$; en particular, $`c - \varepsilon < a_{[N]+1}`$. Entonces, por la propiedad <1>: $`[a_{[N]+1}, b_{[N]+1}] \cap E \ne \varnothing`$.

### Página manuscrita 15 (p. PDF 15). Conclusión

Es decir, existe $`\tilde{x} \in [a_{[N]+1}, b_{[N]+1}] \cap E`$, y entonces $`\tilde{x} \ge a_{[N]+1} > c - \varepsilon`$. Así, $`c`$ es la menor cota superior, es decir, $`c = \sup E`$.

**Observación (manuscrita).** Para $`\varnothing`$ cualquier número es cota superior, así que el conjunto de cotas superiores de $`\varnothing`$ no está acotado inferiormente. Por ello es natural poner $`\sup \varnothing = -\infty`$; análogamente, $`\inf \varnothing = +\infty`$. Estas convenciones dan $`\sup \varnothing < \inf \varnothing`$ (marcado en rojo). Por esta razón, las cotas de $`\varnothing`$ no se definen.

### Diapositivas impresas 16–17. Propiedades de sup e inf; funciones

<a id="lem-2-3-1"></a>**Lema 2.3.1.**

1. Si $`D \subset E \subset \mathbb{R}`$, $`D \ne \varnothing`$, entonces $`\sup D \le \sup E`$ e $`\inf D \ge \inf E`$.
2. Si $`E, F \subset \mathbb{R}`$, $`E, F \ne \varnothing`$, $`t > 0`$, entonces
```math
\sup(E + F) = \sup E + \sup F,\quad \inf(E+F) = \inf E + \inf F,\quad \sup(tE) = t\sup E,\quad \inf(tE) = t\inf E,
```
```math
\sup(-E) = -\inf E,\quad \inf(-E) = -\sup E.
```

**Máximo y mínimo de una función en un conjunto.** El máximo y el mínimo (valores mayor y menor) de una función en un conjunto se definen de forma análoga.

<a id="def-2-3-3"></a>**Definición 2.3.3.** Una función $`f`$ se llama acotada (superiormente, inferiormente) en un conjunto $`D`$ si el conjunto $`f(D)`$ es acotado (superiormente, inferiormente).

### Diapositiva impresa 18. Funciones monótonas

<a id="def-2-3-4"></a>**Definición 2.3.4.** Sea $`D \subset X \subset \mathbb{R}`$. Una función $`f : X \to \mathbb{R}`$ se llama

- **creciente** en $`D`$ si para todos $`x_1 < x_2`$ en $`D`$ se cumple $`f(x_1) \le f(x_2)`$;
- **estrictamente creciente** en $`D`$ si para todos $`x_1 < x_2`$ en $`D`$ se cumple $`f(x_1) < f(x_2)`$;
- **decreciente** en $`D`$ si para todos $`x_1 < x_2`$ en $`D`$ se cumple $`f(x_1) \ge f(x_2)`$;
- **estrictamente decreciente** en $`D`$ si para todos $`x_1 < x_2`$ en $`D`$ se cumple $`f(x_1) > f(x_2)`$.

> **Nota del editor.** En la diapositiva, las definiciones de «decreciente» y «estrictamente decreciente» aparecen escritas con «$`>`$»; por su sentido, en la definición de función decreciente debe figurar $`\ge`$ (como en el caso creciente, donde figura $`\le`$). Se registra como un detalle tipográfico; el sentido de la definición no cambia.

### Diapositiva impresa 19. Sucesiones monótonas

<a id="def-2-3-5"></a>**Definición 2.3.5.** Una sucesión real $`\{x_n\}_{n=1}^{\infty}`$ se llama

- creciente, si $`x_n \le x_{n+1}`$ para todo $`n \in \mathbb{N}`$;
- estrictamente creciente, si $`x_n < x_{n+1}`$ para todo $`n`$;
- decreciente, si $`x_n \ge x_{n+1}`$ para todo $`n`$;
- estrictamente decreciente, si $`x_n > x_{n+1}`$ para todo $`n`$.

> **Nota del editor.** La diapositiva escribe «$`x_n > x_{n+1}`$» para «decreciente»; por su sentido, en el caso no estricto debe ser $`\ge`$, como en el caso creciente.

### Diapositiva impresa 20. Límite de una sucesión monótona

<a id="thm-2-3-3"></a>**Teorema 2.3.3.**

1. Toda [sucesión creciente](#def-2-3-5) y acotada superiormente converge.
2. Toda sucesión decreciente y acotada inferiormente converge.
3. Toda sucesión monótona y acotada converge.

### Páginas manuscritas 21–22 (p. PDF 21–22). Demostración del teorema 2.3.3

**Demostración ([teorema 2.3.3](#thm-2-3-3)).**

**①** Sea $`\{x_n\}`$ creciente y acotada superiormente. Hay que probar que $`\{x_n\}`$ converge. Por el [teorema 2.3.2](#thm-2-3-2), $`\exists \sup_{n} x_n = c \in \mathbb{R}`$. Probemos que $`\lim x_n = c`$.

Tomemos $`\varepsilon > 0`$. Como $`\sup x_n = c`$, por la definición de supremo existe $`N`$ con $`x_N > c - \varepsilon`$. Como $`\{x_n\}`$ es creciente, $`\forall n > N`$: $`x_n \ge x_N`$. Por la definición de supremo, $`\forall n`$: $`x_n \le c`$. Así, $`\forall n > N`$: $`c - \varepsilon < x_N \le x_n \le c < c + \varepsilon`$, es decir, $`\lim x_n = c`$.

**②** Se demuestra de forma análoga (en lugar del supremo se toma el ínfimo).

**③** Se sigue de ① y ②.

### Diapositiva impresa 23. Observaciones al teorema 2.3.3

1. Si una sucesión es creciente y no está acotada superiormente, tiende a $`+\infty`$.
2. Si una sucesión es decreciente y no está acotada inferiormente, tiende a $`-\infty`$.
3. Toda sucesión monótona tiene límite en $`\overline{\mathbb{R}}`$, finito o infinito. Para toda sucesión creciente $`\lim x_n = \sup x_n`$, y para toda sucesión decreciente $`\lim x_n = \inf x_n`$.

### Páginas manuscritas 24–25. El número $`e`$

**Ejemplo (el número $`e`$).** Sea $`x_n = \left(1 + \dfrac{1}{n}\right)^n`$. Probemos que $`\{x_n\}`$ converge.

Pongamos $`y_n = \left(1 + \dfrac{1}{n}\right)^{n+1}`$. Para todo $`n`$: $`y_n \ge 1`$ (así está escrito en el manuscrito; aquí $`1 + \frac1n > 1`$). Además,

```math
\frac{y_{n-1}}{y_n} = \frac{\left(1 + \frac{1}{n-1}\right)^n}{\left(1 + \frac{1}{n}\right)^{n+1}} = \frac{\left(\frac{n}{n-1}\right)^n}{\left(\frac{n+1}{n}\right)^{n+1}} = \left(\frac{n^2}{n^2-1}\right)^{n+1} \cdot \frac{n-1}{n} = \left(1 + \frac{1}{n^2-1}\right)^{n+1} \cdot \frac{n-1}{n}.
```

Por la desigualdad de Bernoulli (demostrada antes: si $`n \in \mathbb{Z}_+`$ y $`x > -1`$, entonces $`(1+x)^n \ge 1 + nx`$):

```math
\left(1 + \frac{1}{n^2-1}\right)^{n+1} \cdot \frac{n-1}{n} \ge \left(1 + \frac{n+1}{n^2-1}\right) \cdot \frac{n-1}{n} = \left(1 + \frac{1}{n-1}\right)\cdot\frac{n-1}{n} = 1.
```

Así, $`y_{n-1} \ge y_n`$, es decir, $`\{y_n\}`$ es decreciente.

Página manuscrita 25 (p. PDF 25): como $`\{y_n\}`$ es decreciente y $`y_n \ge 1`$, la sucesión $`\{y_n\}`$ converge ([teorema 2.3.3](#thm-2-3-3)). Además, $`x_n = \dfrac{y_n}{1 + \frac{1}{n}}`$, y por el teorema del límite de un cociente, $`\{x_n\}`$ converge al mismo límite que $`\{y_n\}`$.

### Diapositiva impresa 26. Definición del número $`e`$

<a id="def-2-3-6"></a>**Definición 2.3.6.** El límite de la sucesión

```math
\left(1 + \frac{1}{n}\right)^n
```

se llama número de Neper, o base de los logaritmos naturales, y se denota con la letra $`e`$:

```math
e = \lim_{n\to\infty}\left(1 + \frac{1}{n}\right)^n.
```

### Diapositiva impresa 27 con la anotación manuscrita «(ejercicios)»

En rojo se ha añadido «(ejercicios)». Observaciones-ejercicios:

1. Sea $`x_n > 0`$ para todo $`n`$ y $`\lim \dfrac{x_{n+1}}{x_n} < 1`$. Entonces $`x_n \to 0`$.
2. $`\lim\limits_{n\to\infty} \dfrac{n^k}{a^n} = 0`$, $`a > 1`$, $`k \in \mathbb{N}`$.
3. $`\lim\limits_{n\to\infty} \dfrac{a^n}{n!}`$, $`a \in \mathbb{R}`$.
4. $`\lim\limits_{n\to\infty} \dfrac{n!}{n^n} = 0`$.

### Diapositiva impresa 28. Subsucesiones

<a id="def-2-3-7"></a>**Definición 2.3.7.** Sea $`\{x_n\}_{n=1}^{\infty}`$ una sucesión en un conjunto $`X`$ y $`\{n_k\}_{k=1}^{\infty}`$ una sucesión estrictamente creciente de números naturales ($`n_k < n_{k+1}`$ para todo $`k`$). La composición ($`\{x_n\}`$ es la aplicación exterior, $`\{n_k\}`$ la interior) se llama **subsucesión** de $`\{x_n\}`$ y se denota $`\{x_{n_k}\}`$.

**Observación.** Para una sucesión estrictamente creciente $`\{n_k\}`$ se cumple $`n_k \ge k`$ para todo $`k`$. En efecto, $`n_1 \ge 1`$ (base de la [inducción](../01-logic-sets-functions.md#example-induction)), y de $`n_k \ge k`$ se sigue $`n_{k+1} \ge n_k + 1 \ge k + 1`$ (paso inductivo).

### Página manuscrita 29 (p. PDF 29). Ejemplos de subsucesiones

Consideremos la sucesión $`1, 2, 3, 4, 5, \dots = \{x_1, x_2, x_3, \dots\}`$. Subsucesiones:

- $`n_k = 2k`$: $`2, 4, 6, 8, 10, \dots`$
- $`n_k = 2k - 1`$: $`1, 3, 5, 7, 9, \dots`$
- $`n_k = k^2`$: $`1, 4, 9, 16, 25, \dots`$

### Página manuscrita 30 (p. PDF 30). Aplicaciones

Sea $`f: \mathbb{N} \to \mathbb{R}`$, $`f(n) = x_n`$, y $`\varphi: \mathbb{N} \to \mathbb{N}`$, $`\varphi(k) = n_k`$. Entonces $`f(\varphi(k)) = f(n_k) = x_{n_k}`$.

Esquema: $`\mathbb{N}`$ (índice $`k`$) $`\xrightarrow{\varphi}`$ $`\mathbb{N}`$ (índice $`n_k`$) $`\xrightarrow{f}`$ $`\mathbb{R}`$ (valor $`x_{n_k}`$).

**¡Pero!** La sucesión $`\{2, 1, 3, 5, 4, \dots\}`$ **no** es una subsucesión de $`\{x_n\} = \{1, 2, 3, 4, 5, \dots\}`$, porque se rompe el orden ($`n_k`$ debe ser estrictamente creciente).

### Diapositivas impresas 31. Límites de subsucesiones

<a id="lem-2-3-2"></a>**Lema 2.3.2.** Toda subsucesión de una sucesión que tiene límite converge al mismo límite: si $`\{x_n\}`$ es una sucesión real, $`\{x_{n_k}\}`$ es una subsucesión suya, $`a \in \mathbb{R} \cup \{\infty\}`$ y $`x_n \to a`$, entonces $`x_{n_k} \to a`$.

<a id="lem-2-3-3"></a>**Lema 2.3.3.** Sea $`\{x_n\}`$ una sucesión real, y sean $`\{x_{n_k}\}`$ y $`\{x_{m_l}\}`$ sus subsucesiones cuyos conjuntos de índices, tomados en conjunto, forman $`\mathbb{N}`$; sea $`a \in \mathbb{R} \cup \{\infty\}`$. Entonces, si $`x_{n_k} \to a`$ y $`x_{m_l} \to a`$, también $`x_n \to a`$.

### Página manuscrita 32 (p. PDF 32). Demostración del lema 2.3.2

**Demostración ([lema 2.3.2](#lem-2-3-2)).** Sea $`a \in \mathbb{R}`$. Tomemos $`\varepsilon > 0`$. $`x_n \to a \Rightarrow \exists N: \forall n > N`$: $`|x_n - a| < \varepsilon`$. Entonces, si $`k > N`$, se tiene $`n_k \ge k > N`$ (por la observación) $`\Rightarrow`$ $`|x_{n_k} - a| < \varepsilon`$.

Si $`a = \pm\infty`$ o $`a = \infty`$, en el razonamiento anterior la desigualdad $`|x_n - a| < \varepsilon`$ se sustituye por $`|x_n| > E`$.

### Página manuscrita 33 (p. PDF 33). Demostración del lema 2.3.3

**Demostración ([lema 2.3.3](#lem-2-3-3)).** Para fijar ideas, consideremos el caso $`a \in \mathbb{R}`$. Tomemos $`\varepsilon > 0`$.

$`x_{n_k} \to a \Rightarrow \exists K: \forall k > K`$: $`|x_{n_k} - a| < \varepsilon`$.
$`x_{m_l} \to a \Rightarrow \exists L: \forall l > L`$: $`|x_{m_l} - a| < \varepsilon`$.

Pongamos $`N = \max\{K, L\}`$. Si $`n > N`$, entonces:
① o bien $`n = n_k`$, y entonces $`k > K`$ y $`|x_n - a| < \varepsilon`$;
② o bien $`n = m_l`$, y entonces $`l > L`$ y $`|x_n - a| < \varepsilon`$.

En cualquier caso $`|x_n - a| < \varepsilon`$, es decir, $`x_n \to a`$.

### Página manuscrita 36 (p. PDF 36). Ejemplo de sucesión divergente

**Ejemplo.** $`x_n = (-1)^n`$ diverge.

$`x_{2k} = (-1)^{2k} = 1 \to 1`$; $`x_{2k+1} = (-1)^{2k+1} = -1 \to -1`$.

> **Nota del editor.** El manuscrito no escribe la conclusión de divergencia; esta se sigue de que la sucesión tiene dos subsucesiones con límites distintos ([lema 2.3.3](#lem-2-3-3)).

### Diapositiva impresa 34 con un ejemplo manuscrito: límite parcial

<a id="def-2-3-8"></a>**Definición 2.3.8.** Un punto $`a`$ se llama **límite parcial** de una sucesión $`\{x_n\}`$ si existe una subsucesión $`\{x_{n_k}\}`$ que tiende a $`a`$.

Manuscrito, para $`x_n = (-1)^n`$:

$`x_{2k} = (-1)^{2k}`$ $`\Rightarrow`$ $`\{x_{2k}\} = \{1, 1, 1, \dots\} \to 1`$ (encerrado).
$`x_{2k-1} = (-1)^{2k-1}`$ $`\Rightarrow`$ $`\{x_{2k-1}\} = \{-1, -1, -1, \dots\} \to -1`$ (encerrado).

Una anotación roja «límites parciales», con flechas, señala los valores $`1`$ y $`-1`$.

### Diapositiva impresa 35. Teorema de Bolzano–Weierstrass

<a id="thm-2-3-4"></a>**Teorema 2.3.4 (principio de selección de Bolzano–Weierstrass).** De toda sucesión acotada se puede extraer una subsucesión convergente.

**Observación.** Si una sucesión real no está acotada superiormente (inferiormente), de ella se puede extraer una subsucesión que tiende a $`+\infty`$ ($`-\infty`$).

### Páginas manuscritas 36–37 (p. PDF 36–37). Demostración del teorema 2.3.4

**Demostración ([teorema 2.3.4](#thm-2-3-4)).** $`\{x_n\}`$ está acotada $`\iff \forall n \in \mathbb{N}\ \exists a, b \in \mathbb{R},\ a < b`$: $`a \le x_n \le b`$ $`\iff`$ $`\forall n \in \mathbb{N}`$: $`x_n \in [a, b]`$.

Consideremos el punto medio de $`[a, b]`$. Denotemos por $`[a_1, b_1]`$ la mitad de $`[a, b]`$ que contiene infinitos términos de $`\{x_n\}`$ (es decir, $`x_n \in [a_1, b_1]`$ para infinitos índices $`n`$).

**Observación (manuscrita, en rojo).** Si ambas mitades contienen infinitos términos, se toma cualquiera de ellas.

Elijamos un índice $`n_1`$ con $`x_{n_1} \in [a_1, b_1]`$. Elijamos $`n_2`$ con $`n_2 > n_1`$ y $`x_{n_2} \in [a_2, b_2]`$. En el paso $`k`$ elegimos $`n_k`$ con $`n_k > n_{k-1}`$ y $`x_{n_k} \in [a_k, b_k]`$.

Hemos construido una sucesión de intervalos encajados $`\{[a_k, b_k]\}`$ y una subsucesión $`\{x_{n_k}\}`$ de la sucesión original. Por el teorema de los intervalos encajados, $`\exists c \in \mathbb{R}`$ con $`a_k \to c`$, $`b_k \to c`$. Además, $`a_k \le x_{n_k} \le b_k`$, por lo que $`x_{n_k} \to c`$.
