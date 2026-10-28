---
title: "Lección 7 — Máximo y mínimo de un conjunto finito, consecuencias en ℤ y ℕ, densidad de ℚ en ℝ"
lang: es
course: "Análisis Matemático, 2025/26"
lecture: 7
source: "ma25_26_лекция_7_notes.pdf"
aliases: ["Lección 7 (es)"]
tags: [mathinmind/es, mathinmind/lecture]
---
# Lección 7 — Máximo y mínimo, parte entera, densidad de $\mathbb{Q}$ en $\mathbb{R}$

[[es/lectures-2025-26/lecture-05-06|← Lecciones 5–6]] · [[es/lectures-2025-26/index|Índice de lecciones]] · [[es/lectures-2025-26/lecture-08|Lección 8 →]] · [[es/term-index|Términos y teoremas]] · [[ru/lectures-2025-26/lecture-07|Русский]] · [[en/lectures-2025-26/lecture-07|English]]

> [!info] Fuente
> `ma25_26_лекция_7_notes.pdf` — 13 páginas: diapositivas impresas con capa de texto (páginas 1–4, 9) y páginas manuscritas cuya capa de texto está deteriorada (páginas 5–8, 10–13). Las páginas manuscritas se transcribieron a partir de su imagen. Las figuras de las páginas 6, 11 y 12 se incluyen como ilustraciones.
>
> **Nota del editor sobre la numeración.** En la diapositiva 4, el teorema sobre el máximo y el mínimo de un conjunto finito tiene el número 1.3.2; en la demostración manuscrita del [[#^cor-1-3-1|corolario 1.3.1]] (página 7) se hace referencia al «teorema 1.4.2» — se conserva tal como aparece en la página manuscrita. Los números de definiciones y teoremas no se han modificado.

## Diapositiva 2. Cita del día

> Todo lo que ocurre, ocurre para bien. Solo que no siempre para el tuyo.

## Diapositiva 3. Objetivo de la lección

- Demostrar consecuencias de los resultados sobre el máximo y el mínimo de un conjunto finito.
- Hablar sobre la densidad del conjunto de los números racionales.

## §3. Números reales

### Diapositiva 4. Existencia de máximo y mínimo de un conjunto finito

> [!theorem] Teorema 1.3.2
> Todo subconjunto finito de $\mathbb{R}$ tiene un elemento mayor y un elemento menor.

^thm-1-3-2

> [!corollary] Corolario 1.3.1
> Todo subconjunto no vacío de $\mathbb{Z}$ acotado superiormente (inferiormente) tiene un elemento mayor (menor).

^cor-1-3-1

> [!corollary] Corolario 1.3.2
> Todo subconjunto no vacío de $\mathbb{N}$ tiene un elemento menor.

^cor-1-3-2

### Página manuscrita 5 (p. PDF 5). Demostración del teorema 1.3.2

**Demostración ([[#^thm-1-3-2|teorema 1.3.2]]).** Hacemos [[es/01-logic-sets-functions#^example-induction|inducción]] sobre el número $n$ de elementos del conjunto.

**Base de la inducción** $n = 1$: $A = \{a_1\}$ ⇒ $a_1$ es a la vez el elemento mayor y el menor ✓.

Por fijar ideas, continuamos el razonamiento para el máximo.

**Hipótesis de inducción.** Sea $A = \{x_1, x_2, \dots, x_n\}$ un conjunto con máximo.

Denotemos $c = \max\{x_1, x_2, \dots, x_n\}$.

**Paso inductivo**: $n \mapsto n+1$, $A = \{x_1, x_2, \dots, x_n, x_{n+1}\}$.

- Si $c \le x_{n+1}$, entonces $x_{n+1} = \max A$;
- si $c > x_{n+1}$, entonces $c = \max A$.

### Páginas manuscritas 6–7 (p. PDF 6–7). Corolario 1.3.1 (enteros)

**Demostración ([[#^cor-1-3-1|corolario 1.3.1]]).** Sea $A \subset \mathbb{Z}$, $A \ne \varnothing$, [[es/lectures-2025-26/lecture-05-06#^def-1-3-7|acotado superiormente]].

Tomemos un elemento arbitrario $n_0 \in A$ y consideremos

$$
A_1 = \{ n \in A : n \ge n_0 \}.
$$

Como $A$ está acotado superiormente, $A_1$ es un conjunto **finito**.

![Página manuscrita 6: ℤ, n₀, la cota M y el conjunto A₁](../../assets/lectures-2025-26/lec07-p06-integers-bounded-sets.jpg)

Sea $M$ un entero que sirve como [[es/02-real-numbers#2.2 Supremo e ínfimo|cota superior]] de $A$ ⇒ entonces $A_1$ contiene como máximo [la frase se corta en el borde de la página 6; su continuación no puede reconstruirse a partir del escaneo].

En la página 7: $A_1 \subset A \subset \mathbb{Z} \subset \mathbb{R}$; $A_1$ tiene un número finito de elementos ⇒ por el teorema 1.4.2, $A_1$ tiene un elemento mayor. Este elemento mayor de $A_1$ es el elemento mayor de $A$.

El caso de un conjunto acotado inferiormente se trata de manera análoga.

### Página manuscrita 7 (p. PDF 7). Corolario 1.3.2 (números naturales)

**Demostración ([[#^cor-1-3-2|corolario 1.3.2]]).** $A \subset \mathbb{N} \subset \mathbb{Z}$, $A \ne \varnothing$; $\mathbb{N}$ está acotado inferiormente por $0$ (tal como aparece en la página; conviene verificar la convención del curso para $\mathbb{N}$). ⇒ El resultado se sigue del [[#^cor-1-3-1|corolario 1.3.1]].

### Página manuscrita 8 (p. PDF 8). Definición de parte entera

**Definición.** Sea $x \in \mathbb{R}$. El mayor entero que no supera a $x$ se llama **parte entera** de $x$ y se denota $[x]$.

**Observación.** La existencia de la parte entera se garantiza por el corolario 1.4.1 ⇒ la definición de parte entera es correcta.

**Observación.**

$$
[x] \le x < [x] + 1, \qquad x - 1 < [x] \le x.
$$

Recíprocamente, si $y \in \mathbb{Z}$ y $x - 1 < y \le x$, entonces $y = [x]$.

En el margen (en verde): $x - [x] = \{x\}$ — la **parte fraccionaria** de $x$, $0 \le \{x\} < 1$.

### Diapositiva 9. Densidad del conjunto de los números racionales (diapositiva impresa con anotación manuscrita)

> [!theorem] Teorema 1.3.3
> Todo intervalo contiene un número racional.

^thm-1-3-3

> [!corollary] Corolario 1.3.3
> Todo intervalo contiene infinitos números racionales.

^cor-1-3-3

**Anotación manuscrita** (flecha hacia el [[#^thm-1-3-3|teorema 1.3.3]]): «La propiedad descrita en el [[#^thm-1-3-3|teorema 1.3.3]] se llama **densidad** del conjunto $\mathbb{Q}$ en el conjunto $\mathbb{R}$».

### Página manuscrita 10 (p. PDF 10). Demostración del teorema 1.3.3

**Demostración ([[#^thm-1-3-3|teorema 1.3.3]]).** Sean $a, b \in \mathbb{R}$, $a < b$ ⇒ $\dfrac{1}{b-a} > 0$.

En el [[es/lectures-2025-26/lecture-05-06#^def-1-3-5|axioma de Arquímedes]] tomamos $x = 1$, $y = \dfrac{1}{b-a}$ ⇒ por el axioma de Arquímedes existe $n \in \mathbb{N}$ con $n > \dfrac{1}{b-a}$ ⇒

$$
\frac{1}{n} < b - a.
$$

Sea

$$
c = \frac{[na] + 1}{n} \in \mathbb{Q}.
$$

Entonces

$$
c = \frac{[na] + 1}{n} \le \frac{na + 1}{n} = a + \frac{1}{n} < a + b - a = b,
$$

$$
c = \frac{[na] + 1}{n} > \frac{na - 1 + 1}{n} = a.
$$

Por tanto $c \in (a, b)$. ∎

### Página manuscrita 11 (p. PDF 11). Corolario 1.3.3: dos vías

**Demostración ([[#^cor-1-3-3|corolario 1.3.3]]).**

**Vía ① — recursión.** Tomemos un intervalo $(a, b)$. Por el [[#^thm-1-3-3|teorema 1.3.3]] existe $c_1 \in \mathbb{Q}$ en el intervalo $(a, c)$ [en verde en la página]; por el [[#^thm-1-3-3|teorema 1.3.3]] existe $c_2 \in \mathbb{Q}$ en el intervalo $(c, b)$ [en rojo]; el [[#^thm-1-3-3|teorema 1.3.3]] se aplica de nuevo al punto $c$ (marcado en la figura); «etc.» — la construcción continúa recursivamente, como indica la página.

![Página manuscrita 11: construcción recursiva de números racionales dentro de (a, b)](../../assets/lectures-2025-26/lec07-p11-density-corollary.jpg)

**Vía ② — por contradicción.** Supongamos que cierto intervalo $(a, b)$ contiene solo una cantidad finita de números racionales. Denotemos por $x_1$ el menor de ellos. Entonces $(a, x_1)$ no contiene números racionales ⇒ contradicción con el [[#^thm-1-3-3|teorema 1.3.3]].

### Página manuscrita 12 (p. PDF 12). «Pago de deudas»: $[0,1]$ no es numerable

**Demostremos que $[0,1]$ no es numerable.**

**Demostración.** Supongamos lo contrario: sea $[0,1]$ [[es/lectures-2025-26/lecture-01-02#^def-1-2-5|numerable]] ⇒ todos los elementos de $[0,1]$ pueden listarse como

$$
[0,1] = \{ x_1, x_2, \dots, x_{100}, \dots \}.
$$

![Página manuscrita 12: los segmentos [0, 1/3], [1/3, 2/3], [2/3, 1] y la selección de [a₁, b₁]](../../assets/lectures-2025-26/lec07-p12-uncountable-interval.jpg)

Dividamos $[0,1]$ en tres partes: $[0, \tfrac13]$, $[\tfrac13, \tfrac23]$, $[\tfrac23, 1]$. Denotemos por $[a_1, b_1]$ aquella que no contiene a $x_1$.

### Página manuscrita 13 (p. PDF 13). Continuación

Dividamos $[a_1, b_1]$ en 3 partes iguales y denotemos por $[a_2, b_2]$ aquella que no contiene a $x_2$, y así sucesivamente.

Obtenemos una sucesión de segmentos encajados $\{[a_n, b_n]\}_{n=1}^{\infty}$ tal que $x_n \notin [a_n, b_n]$ para todo $n$.

Por el **axioma de Cantor de los segmentos encajados** existe $x^* \in [0,1]$ que pertenece a todos los $[a_n, b_n]$. Entonces $x^* = x_m$ para algún $m \in \mathbb{N}$. Pero por construcción $x_m \notin [a_m, b_m]$ — contradicción. ∎

> [!remark] Nota del editor
> El encabezado manuscrito «Отдача долгов» («Pago de deudas», título en tono de broma) en la parte superior de la página 12 se conserva tal como está; el sentido de la anotación no se aprecia en el escaneo. El ejemplo en sí trata sobre la no numerabilidad de $[0,1]$.

## Páginas no relacionadas con el contenido

- La página 1 es la portada; la página 2 es la cita del día (traducida arriba).
- Las páginas 5–8 y 10–13 son manuscritas y se han transcrito arriba; la página 9 es una diapositiva impresa con una anotación manuscrita.
