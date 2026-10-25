---
title: "Lección 13 — Límites superior e inferior, sucesiones fundamentales, criterio de Cauchy"
lang: es
course: "Análisis Matemático, 2025/26"
lecture: 13
date: 2025-10-16
source: "ma25_26_лекция_13_notes.pdf"
---
# Lección 13 — Límites superior e inferior, criterio de Bolzano–Cauchy

[Índice de lecciones](index.md) · [Русский](../../ru/lectures-2025-26/lecture-13.md) · [English](../../en/lectures-2025-26/lecture-13.md)

> **Fuente:** `ma25_26_лекция_13_notes.pdf` — 18 páginas: diapositivas impresas con capa de texto (páginas 1–4, 7, 13–14, 16) y páginas manuscritas sin capa de texto utilizable (páginas 5, 6, 8–12, 15, 17, 18). Las páginas manuscritas se transcribieron a partir de su imagen. Los números de página del PDF aparecen en los encabezados.
>
> **Nota del editor.** La fecha de la lección se toma del pie de las diapositivas («16 de octubre de 2025»).

## Diapositivas impresas 1–4. Introducción y definición de límites superior e inferior

**Cita del día:** «Soy una bruja malvada . . . Me levanté con el pie izquierdo . . . Me subí a la escoba equivocada . . . Y volé en la dirección equivocada . . . »

**Objetivo de la lección.** Introducir las nociones de límite superior e inferior de una sucesión. Demostrar un teorema sobre las propiedades de los límites superior e inferior. Definir la sucesión fundamental (sucesión de Cauchy). Demostrar el criterio de Bolzano–Cauchy de convergencia de una sucesión.

### Definición 2.3.9 (límites superior e inferior)

Sea $\{x_n\}$ una sucesión real acotada superiormente. La cantidad

$$
\varlimsup_{n\to\infty} x_n = \lim_{n\to\infty} \sup_{k\ge n} x_k
$$

se llama **límite superior** de la sucesión $\{x_n\}$.

Sea $\{x_n\}$ una sucesión real acotada inferiormente. La cantidad

$$
\varliminf_{n\to\infty} x_n = \lim_{n\to\infty} \inf_{k\ge n} x_k
$$

se llama **límite inferior** de la sucesión $\{x_n\}$.

## Página manuscrita 5 (p. PDF 5). Observaciones sobre los límites superior e inferior

Sea $z_n = \sup_{k \ge n} x_k$. Entonces $\varlimsup x_n = \lim z_n$.

- Si $\{x_n\}$ no está acotada superiormente, entonces $\varlimsup_{n\to\infty} x_n = +\infty$.
- Si $\{x_n\}$ no está acotada inferiormente, entonces $\varliminf_{n\to\infty} x_n = -\infty$.

**Observación.** $\varlimsup x_n$ y $\varliminf x_n$ existen en $\overline{\mathbb{R}}$, y $\varliminf x_n \le \varlimsup x_n$.

Más abajo, en el manuscrito: $x_1, x_2, x_3, x_4, \dots$; $z_1 = \sup_{k \ge 1} x_k = \sup x_n$, $z_2 = \sup_{k \ge 2} x_k$, $z_3 = \sup_{k \ge 3} x_k$, de donde $z_1 \ge z_2 \ge z_3 \ge \dots$

## Página manuscrita 6 (p. PDF 6). Acotación y límites parciales

Si $\{x_n\}$ está acotada, entonces $\exists a, b \in \mathbb{R}$ con $a \le b$ y $\forall n \in \mathbb{N}$: $a \le x_n \le b$, de donde $a \le \dots \le z_2 \le z_1 \le b$.

Recordemos que un punto $a$ se llama **límite parcial** de la sucesión $\{x_n\}$ si existe una subsucesión $\{x_{n_k}\}$ con $x_{n_k} \to a$.

## Diapositiva impresa 7. Teorema sobre los límites superior e inferior

**Teorema 2.3.5.** Sea $\{x_n\}$ una sucesión real. Entonces se cumplen las siguientes afirmaciones.

1. El límite superior es el mayor, y el límite inferior es el menor, de los límites parciales de $\{x_n\}$.
2. El límite de $\{x_n\}$ en $\mathbb{R}$ existe si y solo si $\varliminf x_n = \varlimsup x_n$. En ese caso, $\lim x_n$ es igual a su valor común.

## Página manuscrita 8 (p. PDF 8). Demostración del teorema 2.3.5, parte A

**Demostración (teorema 2.3.5).**

**A)** Sea $\{x_n\}$ acotada. Denotemos $b := \varlimsup x_n$. Probemos que $b$ es un límite parcial.

$b = \varlimsup x_n = \lim_{n\to\infty} z_n$, $z_n = \sup_{k\ge n} x_k$; $z_1 \ge z_2 \ge z_3 \ge \dots$ $\Rightarrow$ $\forall n$: $z_n \ge b$.

$\forall \varepsilon > 0$ $\forall N$: $z_{N+1} = \sup\{x_{N+1}, x_{N+2}, \dots\} > b - \varepsilon$ $\Rightarrow$ $\exists n > N$: $x_n > b - \varepsilon$.

Entonces hallamos:
- $n_1$: $x_{n_1} > b - 1$;
- $n_2$: $n_2 > n_1$ y $x_{n_2} > b - \frac{1}{2}$;
- …
- $n_k$: $n_k > n_{k-1}$ y $x_{n_k} > b - \frac{1}{k}$.

## Página manuscrita 9 (p. PDF 9). Continuación de la demostración del teorema 2.3.5

En total hemos construido una subsucesión $\{x_{n_k}\}$ con $b - \frac{1}{k} < x_{n_k} \le z_{n_k}$.

$\{z_{n_k}\}$ es una subsucesión de $\{z_n\}$, y $z_n \to b$, luego $z_{n_k} \to b$. Por el teorema del emparedado, $x_{n_k} \to b$, es decir, $b$ es un límite parcial.

Si $\{x_{m_\ell}\}$ es una subsucesión de $\{x_n\}$ y $x_{m_\ell} \to \beta$, entonces $x_{m_\ell} \le z_{m_\ell} \to b$, de donde $\beta \le b$. Es decir, $b$ es el **mayor** límite parcial de $\{x_n\}$.

## Página manuscrita 10 (p. PDF 10). El límite inferior es el menor límite parcial

Análogamente se demuestra que $\varliminf x_n$ es el menor límite parcial.

Sea $a = \varliminf x_n = \lim_{n\to\infty} y_n$, donde $y_n = \inf_{k\ge n} x_k$ (encerrado en el manuscrito). Entonces $z_n = \sup_{k\ge n} x_k$ e $y_n \le x_n \le z_n$ para todo $n$.

Si $\varliminf x_n = \varlimsup x_n$, entonces, por el teorema del emparedado, $x_n \to \varliminf x_n = \varlimsup x_n$, es decir, existe $\lim x_n = \varliminf x_n = \varlimsup x_n$.

> **Nota del editor.** En la línea al inicio de la página que define $z_n$ e $y_n$, el manuscrito usa $x_{n_k}$; en la fórmula encerrada y en los cálculos posteriores aparece $x_k$. Aquí se utiliza la versión con $x_k$.

## Página manuscrita 11 (p. PDF 11). Conclusión del teorema 2.3.5

Si existe $\lim x_n$, entonces todos los límites parciales, en particular $\varliminf x_n$ y $\varlimsup x_n$, coinciden con él.

**B)** Sea $\{x_n\}$ acotada superiormente pero no inferiormente. Entonces $\varliminf x_n = -\infty$, así que se puede elegir una subsucesión que tiende a $-\infty$, y $-\infty$ es un límite parcial. Por supuesto, $-\infty$ es menor que cualquier límite parcial (si los hay).

Que $\varlimsup x_n$ es el mayor límite parcial de $\{x_n\}$ se demuestra exactamente como en la parte A.

Si $\varliminf x_n = \varlimsup x_n$, entonces $z_n = \sup_{k\ge n} x_k \to -\infty$, luego $x_n \to -\infty$, ya que $x_n \le z_n$.

## Página manuscrita 12 (p. PDF 12). El recíproco y el caso C

Recíprocamente, si $\lim x_n = -\infty$, entonces $\varlimsup x_n = -\infty$ como límite parcial.

El caso en que $\{x_n\}$ está acotada inferiormente pero no superiormente es análogo.

**C)** Si $\{x_n\}$ no está acotada ni superior ni inferiormente, entonces:

- la **afirmación 1** del teorema es obvia: $-\infty = \varliminf x_n < \varlimsup x_n = +\infty$;
- la **afirmación 2** del teorema no se realiza (en el manuscrito está escrita de forma breve).

## Diapositiva impresa 13. Sucesión fundamental

**Definición 2.3.10.** Se dice que una sucesión $\{x_n\}$ *converge en sí misma* si

$$
\forall \varepsilon > 0\ \exists N\ \forall n, l > N:\ |x_n - x_l| < \varepsilon.
$$

A una sucesión que converge en sí misma también se le llama **sucesión fundamental** o **sucesión de Cauchy**.

## Diapositiva impresa 14. Acotación de una sucesión fundamental

**Teorema 2.3.6.**

1. Una sucesión fundamental está acotada.
2. Si una sucesión fundamental tiene una subsucesión convergente, entonces la propia sucesión converge.

## Página manuscrita 15 (p. PDF 15). Demostración del teorema 2.3.6, punto ①

**Demostración (teorema 2.3.6).**

**①** $\{x_n\}$ converge en sí misma. Tomemos $\varepsilon = 1$. $\exists N$: $\forall n, l > N$: $|x_n - x_l| < 1$.

En particular, $|x_n - x_{N+1}| < 1$ para todo $n > N$. Entonces, para $n > N$:

$$
|x_n| = |x_n - x_{N+1} + x_{N+1}| \le |x_n - x_{N+1}| + |x_{N+1}| < 1 + |x_{N+1}|.
$$

Pongamos $R = \max\{|x_1|, |x_2|, \dots, |x_N|,\ 1 + |x_{N+1}|\}$. Entonces $|x_n| \le R$ para todo $n \in \mathbb{N}$.

**②** Para demostrar como ejercicio.

## Diapositiva impresa 16. Criterio de Bolzano–Cauchy

**Teorema 2.3.7.** La convergencia de una sucesión real es equivalente a su convergencia en sí misma.

## Páginas manuscritas 17–18 (p. PDF 17–18). Demostración del teorema 2.3.7

**Demostración (teorema 2.3.7).**

**(⇒)** Sea $\lim x_n = a$. Veamos que $\{x_n\}$ converge en sí misma.

$\forall \varepsilon > 0\ \exists N$: $\forall n > N$: $|x_n - a| < \frac{\varepsilon}{2}$.

$\forall n, m > N$: $|x_n - x_m| = |x_n - a + a - x_m| \le |x_n - a| + |x_m - a| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$. Así, $\{x_n\}$ converge en sí misma.

**(⇐)** Sea $\{x_n\}$ convergente en sí misma. Entonces:

1. por el punto ① del teorema 2.3.6, $\{x_n\}$ está acotada;
2. por el principio de selección de Bolzano–Weierstrass, se puede elegir de $\{x_n\}$ una subsucesión convergente $\{x_{n_k}\}$;
3. por el punto ② del teorema 2.3.6, como $\{x_{n_k}\}$ converge, también $\{x_n\}$ converge.

> **Nota del editor.** En el paso 3, el manuscrito se refiere al «punto ②»; por su sentido, es el punto ② del teorema 2.3.6 (sobre la subsucesión convergente de una sucesión fundamental).
