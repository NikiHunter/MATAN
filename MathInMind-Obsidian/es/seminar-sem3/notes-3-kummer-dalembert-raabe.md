---
title: "Seminario NM-204. Apuntes, parte 3: criterios de Kummer, d'Alembert y Raabe"
lang: es
tags: [mathinmind/es, mathinmind/other]
---
# Apuntes de los seminarios, parte 3: criterios de Kummer, d'Alembert y Raabe

[[ru/seminar-sem3/notes-3-kummer-dalembert-raabe|Русский]] · [[en/seminar-sem3/notes-3-kummer-dalembert-raabe|English]] · **Español**

[[es/seminar-sem3/notes-2-series-basics|← Parte 2: fundamentos de series]] · [[es/seminar-sem3/index|Todas las tareas y apuntes]] · [[es/seminar-sem3/notes-4-examples-tests|Parte 4: ejemplos y comparación de criterios →]]

> [!note] Qué es esto
> Una versión reelaborada de los seminarios del 16, 21 y 28 de octubre de 2026, a partir de la transcripción de [`sem3_notes`](https://github.com/NikiHunter/matan/blob/main/sem3_notes/README.md). Los números de los enunciados son los de la pizarra. El registro del 14 de octubre está vacío (dos páginas en blanco) y no se incluye. El final de la demostración del teorema 12.1, hecho el 30 de octubre, se ha trasladado aquí.

| Fecha | Qué se vio | Tareas |
|---|---|---|
| 16 oct. | [[#^ex-9-1\|$\sum\frac1{k!}$]], [[#La idea del criterio de Kummer\|la idea de Kummer]], [[#Definición 10.1. Sucesiones finalmente positivas\|sucesiones finalmente positivas]], [[#^thm-10-2\|criterio de Kummer 10.2]], [[#^cor-10-3\|d'Alembert 10.3]], [[#^ex-10-4\|ejemplo 10.4]] | [[es/seminar-sem3/hw3-numerical-series#Problema 3.5\|3.5]]–[[es/seminar-sem3/hw3-numerical-series#Problema 3.8\|3.8]] |
| 21 oct. | [[#^cor-11-1\|criterio de Raabe 11.1]], [[#^rem-11-2\|observación 11.2]], [[#^lem-11-3\|lema 11.3]] | [[es/seminar-sem3/hw3-numerical-series#Problema 3.9 (criterio de Raabe)\|3.9]], [[es/seminar-sem3/hw3-numerical-series#^p-3-10\|3.10]], [[es/seminar-sem3/hw3-numerical-series#Problema 3.1\|3.1]] |
| 28 oct. | [[#^thm-12-1\|series $\sum\frac{c_k}{k^d}$]], [[#Observación 12.2. Qué mirar en una serie finalmente positiva\|qué mirar en cada criterio]] | [[es/seminar-sem3/hw3-numerical-series#^p-3-11\|3.11]], [[es/seminar-sem3/hw4-series-inequalities-bases#Problema 4.6 (formas límite de los criterios)\|4.6]] |

**Notación del seminario.** Los criterios usan el cociente $\frac{a_n}{a_{n+1}}$ —el término anterior entre el siguiente— y no el habitual $\frac{a_{n+1}}{a_n}$. Por eso «el cociente es mayor que uno» significa que los términos decrecen.

## Seminario del 16 de octubre: criterios de Kummer y de d'Alembert

### Ejemplo 9.1. $\sum\frac1{k!}$ converge (= [[es/seminar-sem3/hw3-numerical-series#Problema 3.5|problema 3.5]], b)

Comparemos $a_k=\frac1{k!}$ con $b_k=\frac1{k(k+1)}$; la serie de los $b_k$ converge ([[es/seminar-sem3/notes-2-series-basics#^ex-7-2|ejemplo 7.2]]).
$$
\frac{a_{k+1}}{a_k}=\frac1{k+1},\qquad\frac{b_{k+1}}{b_k}=\frac{k}{k+2}.
$$
La desigualdad $\frac1{k+1}\le\frac k{k+2}$ equivale a $\frac{k^2-2}{(k+1)(k+2)}\ge0$, es decir, a $k^2\ge2$; se cumple para $k\ge2$. Por el criterio de comparación generalizado ([[es/seminar-sem3/notes-2-series-basics#^thm-8-3|teorema 8.3]]) la serie $\sum\frac1{k!}$ converge. $\blacksquare$ ^ex-9-1

**Por qué funciona.** El cociente de términos vecinos de la serie factorial, $\frac1{k+1}$, tiende a cero, mientras que el de la serie patrón, $\frac k{k+2}$, tiende a uno: en cada paso la serie factorial decrece más deprisa. Comparar cocientes es más fácil que comparar los propios términos. Que la desigualdad falle para $k=1$ no importa: el criterio solo la necesita a partir de cierto índice.

### La idea del criterio de Kummer

Sean $x_n>0$ y, para $n$ grande,
$$
x_n\frac{a_n}{a_{n+1}}-x_{n+1}\ge d>0.
$$
Multiplicamos por $a_{n+1}>0$: $x_na_n-x_{n+1}a_{n+1}\ge d\,a_{n+1}$. Sumamos estas desigualdades para $n=n_0+1,\dots,m$. A la izquierda la suma es telescópica:
$$
d\sum_{n=n_0+1}^{m}a_{n+1}\le x_{n_0+1}a_{n_0+1}-x_{m+1}a_{m+1}\le x_{n_0+1}a_{n_0+1}.
$$
Las sumas parciales están acotadas, así que la serie converge ([[es/seminar-sem3/notes-2-series-basics#Proposición 7.1. Criterio de convergencia de una serie no negativa|proposición 7.1]]).

### Definición 10.1. Sucesiones finalmente positivas

Una sucesión $(a_n)$ es **finalmente positiva a partir del índice $N_0$** si $a_n>0$ para todo $n>N_0$, y simplemente **finalmente positiva** si esto ocurre para algún $N_0$.

**Relación con las bases.** «A partir de cierto índice» es lo mismo que «en algún elemento de la base $n\to\infty$». La base en $\mathbb N$ es la familia $\{M_k\}$ con $M_k=\{m\in\mathbb N:\ m>k\}$; es la familia $\mathcal M_2$ del [[es/seminar-sem3/hw4-series-inequalities-bases#Problema 4.3 (bases de conjuntos)|problema 4.3]].

### Teorema 10.2. Criterio de Kummer (= [[es/seminar-sem3/hw3-numerical-series#Problema 3.6 (criterio de Kummer)|problema 3.6]])

Sean $x_n>0$ para todo $n$ y $(a_n)$ finalmente positiva a partir de $N_0$. ^thm-10-2

1. Si existen $d>0$ y $N_1\ge N_0$ tales que $x_n\frac{a_n}{a_{n+1}}-x_{n+1}\ge d$ para todo $n>N_1$, entonces $\sum a_n$ converge.
2. Si la serie $\sum\frac1{x_n}$ diverge y $x_n\frac{a_n}{a_{n+1}}-x_{n+1}\le0$ para todo $n>N_2$ (con $N_2\ge N_0$), entonces $\sum a_n$ diverge.

**Demostración del punto 1.** Para $n>N_1$ multiplicamos la desigualdad por $a_{n+1}>0$:
$$
x_na_n-x_{n+1}a_{n+1}\ge d\,a_{n+1}.\tag{*}
$$
Sumamos $(*)$ para $n=N_1+1,\dots,N_1+k$. El lado izquierdo es telescópico:
$$
d\sum_{l=1}^{k}a_{N_1+1+l}\le x_{N_1+1}a_{N_1+1}-x_{N_1+k+1}a_{N_1+k+1}<x_{N_1+1}a_{N_1+1},
$$
porque el sustraendo es positivo. Por tanto, para todo $k$,
$$
\sum_{l=1}^{k}a_{N_1+1+l}<\frac{x_{N_1+1}\,a_{N_1+1}}{d},
$$
y el lado derecho no depende de $k$. Las sumas parciales de la serie positiva $\sum_l a_{N_1+1+l}$ están acotadas; converge (7.1), y con ella $\sum a_n$ (6.3).

**Demostración del punto 2.** Para $n>N_2$ la hipótesis da $x_n\frac{a_n}{a_{n+1}}\le x_{n+1}$, es decir,
$$
\frac{a_{n+1}}{a_n}\ge\frac{x_n}{x_{n+1}}=\frac{1/x_{n+1}}{1/x_n}.
$$
Es la hipótesis del [[es/seminar-sem3/notes-2-series-basics#^thm-8-3|teorema 8.3]] para el par en el que $\frac1{x_n}$ hace de «$a$» y $a_n$ de «$b$». La serie $\sum\frac1{x_n}$ diverge, luego $\sum a_n$ diverge. $\blacksquare$

**Por qué funciona.** La cantidad $x_na_n$ es un término «ponderado» de la serie. En el punto 1 disminuye en cada paso al menos $d\,a_{n+1}$, pero sigue siendo positiva. Así que todas las disminuciones juntas no superan su valor inicial: la serie «paga» sus términos con un presupuesto finito. En el punto 2 el término ponderado no decrece, por lo que $a_n\ge\frac{\mathrm{const}}{x_n}$, y la serie es al menos la divergente $\sum\frac1{x_n}$. Cada sucesión $(x_n)$ da su propio criterio: $x_n=1$ da d'Alembert ([[#^cor-10-3|10.3]]), $x_n=n$ da Raabe ([[#^cor-11-1|11.1]]).

### Corolario 10.3. Criterio de d'Alembert (= [[es/seminar-sem3/hw3-numerical-series#Problema 3.7 (criterio de d'Alembert)|problema 3.7]])

Sea $(a_n)$ finalmente positiva a partir de $N_0$. ^cor-10-3

1. Si existen $\beta>0$ y $N_1\ge N_0$ tales que $\frac{a_n}{a_{n+1}}\ge1+\beta$ para todo $n>N_1$, entonces $\sum a_n$ converge.
2. Si $\frac{a_n}{a_{n+1}}\le1$ para todo $n>N_2$ (con $N_2\ge N_0$), entonces $\sum a_n$ diverge.

**Demostración.** Criterio de Kummer con $x_n=1$: entonces $x_n\frac{a_n}{a_{n+1}}-x_{n+1}=\frac{a_n}{a_{n+1}}-1$. En el punto 1 esta cantidad es al menos $\beta$; tomamos $d=\beta$. En el punto 2 es $\le0$, y la serie $\sum\frac1{x_n}=\sum1$ diverge: sus sumas parciales $S_n=n$ no están acotadas. $\blacksquare$

**Importante.** En el punto 2 la desigualdad $\frac{a_n}{a_{n+1}}\le1$ debe cumplirse para **todos** los $n$ a partir de cierto índice. No bastan infinitos índices, como muestra el [[#^ex-10-4|ejemplo 10.4]].

### Ejemplo 10.4. El criterio de Cauchy funciona y el de d'Alembert no (= [[es/seminar-sem3/hw3-numerical-series#Problema 3.8|problema 3.8]])

$$
a_k=\begin{cases}2^{-k}, & k\ \text{impar},\\ 3^{-k}, & k\ \text{par}.\end{cases}
$$

^ex-10-4

1) **La serie converge.** $\sqrt[k]{a_k}$ vale $\frac12$ para $k$ impar y $\frac13$ para $k$ par, así que $\sqrt[k]{a_k}\le\frac12$ para todo $k$. Por el criterio de Cauchy ([[es/seminar-sem3/notes-2-series-basics#Teorema 8.2. Criterio de Cauchy (de la raíz)|teorema 8.2]]) con $q=\frac12$ la serie converge.

2) **El criterio de d'Alembert no se aplica.** Para todo $m\in\mathbb N$
$$
\frac{a_{2m}}{a_{2m+1}}=\frac{2^{2m+1}}{3^{2m}}=2\Bigl(\frac23\Bigr)^{2m}\le\frac89<1,\qquad\frac{a_{2m-1}}{a_{2m}}=\frac{3^{2m}}{2^{2m-1}}=2\Bigl(\frac32\Bigr)^{2m}\ge\frac92.
$$
Así, el conjunto $\bigl\{k:\ \frac{a_k}{a_{k+1}}\le1\bigr\}$ contiene todos los pares y $\bigl\{k:\ \frac{a_k}{a_{k+1}}\ge\frac92\bigr\}$ todos los impares; los dos son infinitos. Ninguna condición de d'Alembert se cumple para todos los $n$ a partir de cierto índice. $\blacksquare$

**Por qué funciona.** La serie son dos progresiones geométricas intercaladas. Pasar de la progresión «lenta» a la «rápida» da un cociente grande, y el paso inverso hace crecer el término. D'Alembert mira un solo paso y recibe señales contradictorias. Cauchy acota el propio término y ve que todos los términos son a lo sumo $2^{-k}$.

## Seminario del 21 de octubre: el criterio de Raabe

### Corolario 11.1. Criterio de Raabe (= [[es/seminar-sem3/hw3-numerical-series#Problema 3.9 (criterio de Raabe)|problema 3.9]])

Sea $(a_n)$ finalmente positiva a partir de $N_0$. ^cor-11-1

1. Si existen $\delta>0$ y $N_1\ge N_0$ tales que $\frac{a_n}{a_{n+1}}\ge1+\frac{1+\delta}n$ para todo $n>N_1$, entonces $\sum a_n$ converge.
2. Si $\frac{a_n}{a_{n+1}}\le1+\frac1n$ para todo $n>N_2$ (con $N_2\ge N_0$), entonces $\sum a_n$ diverge.

**Demostración.** Criterio de Kummer con $x_n=n$. La serie $\sum\frac1{x_n}=\sum\frac1n$ diverge ([[es/seminar-sem3/notes-2-series-basics#^ex-6-6|ejemplo 6.6]]), y
$$
x_n\frac{a_n}{a_{n+1}}-x_{n+1}=n\frac{a_n}{a_{n+1}}-(n+1)=n\Bigl(\frac{a_n}{a_{n+1}}-1-\frac1n\Bigr).
$$
1) Para $n>N_1$ esto es al menos $n\cdot\frac\delta n=\delta$; tomamos $d=\delta$. 2) Para $n>N_2$ es $\le0$. $\blacksquare$

**Por qué funciona.** Aquí el cociente $\frac{a_n}{a_{n+1}}$ puede tender a $1$; lo que importa es con qué rapidez. Las series patrón son $\sum\frac1{n^p}$, para las que $\frac{a_n}{a_{n+1}}=\bigl(1+\frac1n\bigr)^p\approx1+\frac pn$. El criterio de Raabe lee el coeficiente de $\frac1n$: mayor que uno con margen significa convergencia, a lo sumo uno significa divergencia.

**Un ejemplo del seminario: d'Alembert no decide, Raabe sí.** Sean $a_1=1$ y $a_{n+1}=\frac{2n}{2n+1}a_n$, es decir, $\frac{a_n}{a_{n+1}}=1+\frac1{2n}$. La condición de divergencia de d'Alembert $\frac{a_n}{a_{n+1}}\le1$ no se cumple para ningún $n$, y la de convergencia con un $\beta>0$ constante falla para $n$ grande. La condición 2 de Raabe sí se cumple: $1+\frac1{2n}\le1+\frac1n$, así que la serie diverge. (De hecho $a_n\sqrt n\to\frac{\sqrt\pi}2$, de modo que $a_n$ se comporta como $\frac{\mathrm{const}}{\sqrt n}$.) Una serie parecida es $b_k$ en el [[es/seminar-sem3/hw4-series-inequalities-bases#Problema 4.9|problema 4.9]].

### Observación 11.2. «Para infinitos $n$» tampoco basta en Raabe (= [[es/seminar-sem3/hw3-numerical-series#^p-3-10|problema 3.10]])

Tomemos la serie del [[#^ex-10-4|ejemplo 10.4]]. Converge, pero el conjunto $\bigl\{k:\ \frac{a_k}{a_{k+1}}\le1\bigr\}$ es infinito. Este conjunto está contenido en $\bigl\{k:\ \frac{a_k}{a_{k+1}}\le1+\frac1k\bigr\}$, porque $1<1+\frac1k$. Por tanto el segundo conjunto también es infinito, es decir, numerable por ser un subconjunto infinito de $\mathbb N$. Así, la cota de la condición 2 del criterio de Raabe se cumple para infinitos índices y, sin embargo, la serie converge. $\blacksquare$ ^rem-11-2

**Por qué funciona.** Las condiciones de divergencia de los criterios basados en cocientes deben cumplirse para todos los $n$ suficientemente grandes: un paso hacia arriba no impide que la serie decrezca en conjunto. En el criterio de Cauchy es distinto: allí bastan infinitos índices ([[es/seminar-sem3/notes-2-series-basics#Teorema 8.2. Criterio de Cauchy (de la raíz)|teorema 8.2]], punto 2).

### Lema 11.3. Una serie convergente tiene sumas parciales acotadas (= [[es/seminar-sem3/hw3-numerical-series#Problema 3.1|problema 3.1]])

Si $\sum a_n$ converge, entonces $(S_n)$ es una sucesión convergente, y toda sucesión convergente está acotada. $\blacksquare$ ^lem-11-3

El recíproco es falso: [[es/seminar-sem3/notes-2-series-basics#^ex-7-4|ejemplo 7.4]].

## Seminario del 28 de octubre: series de la forma $\sum\frac{c_k}{k^d}$

### Teorema 12.1. Cuándo converge $\sum\frac{c_k}{k^d}$ (= [[es/seminar-sem3/hw3-numerical-series#^p-3-11|problema 3.11]])

Sean $d\in\mathbb R$ y números $c_k$ comprendidos entre dos constantes positivas: $0<M_1\le c_k\le M_2$ para todo $k$. Entonces la serie $\sum_{k\ge1}\frac{c_k}{k^d}$ converge si y solo si $d>1$.

^thm-12-1

**Demostración.** Escribamos $a_k=\frac{c_k}{k^d}$.

*Caso $d\le0$.* Entonces $k^{-d}\ge1$ y $a_k\ge c_k\ge M_1>0$. El término general no tiende a cero; la serie diverge (6.5).

*Caso $0<d\le1$.* Entonces $k^d\le k$ y $a_k\ge\frac{M_1}{k^d}\ge\frac{M_1}k$. La serie $\sum\frac{M_1}k$ diverge (la armónica multiplicada por $M_1\ne0$), así que por el criterio de comparación diverge $\sum a_k$.

*Caso $d>1$.* Comparemos con $b_k=\frac{M_2}{k^d}\ge a_k$ y probemos con el criterio de Raabe que $\sum b_k$ converge. El cociente es
$$
\frac{b_k}{b_{k+1}}=\Bigl(1+\frac1k\Bigr)^d.
$$
Por la fórmula de Taylor con resto de Peano para $\varphi(x)=(1+x)^d$ existe una sucesión $x_k\to0$ con
$$
\Bigl(1+\frac1k\Bigr)^d=1+\frac dk+\frac{d(d-1)}{2k^2}+\frac{x_k}{k^2},\qquad k\Bigl(\frac{b_k}{b_{k+1}}-1\Bigr)=d+\frac1k\Bigl(\frac{d(d-1)}2+x_k\Bigr).
$$
Como $x_k\to0$ y $\frac{d(d-1)}2>0$, para $k$ grande (cuando $|x_k|<\frac{d(d-1)}4$) el paréntesis es positivo, y
$$
\frac{b_k}{b_{k+1}}\ge1+\frac dk=1+\frac{1+(d-1)}k.
$$
Es la condición 1 del criterio de Raabe con $\delta=d-1>0$. La serie $\sum b_k$ converge y, como $0<a_k\le b_k$, también converge $\sum a_k$. $\blacksquare$

**Más corto, con la desigualdad de Bernoulli.** Para $d>1$ y $x>0$ se tiene $(1+x)^d\ge1+dx$, lo que da directamente $\frac{b_k}{b_{k+1}}\ge1+\frac dk$ para todo $k$. Así se hace en el [[es/seminar-sem3/hw3-numerical-series#^p-3-11|problema 3.11]].

**Por qué funciona.** Un factor $c_k$ encerrado entre constantes positivas no influye en la convergencia: la serie queda encerrada entre $M_1\sum\frac1{k^d}$ y $M_2\sum\frac1{k^d}$. Por eso primero se elimina $c_k$ con el criterio de comparación y solo después se aplica Raabe a una serie patrón regular. Aplicar Raabe directamente a $a_k$ no funciona: el cociente $\frac{c_k}{c_{k+1}}$ puede saltar (por ejemplo, con $c_k=2+(-1)^k$). El primer intento en el seminario fue justo ese y se abandonó en favor de la comparación con $b_k$.

### Observación 12.2. Qué mirar en una serie finalmente positiva

| Criterio | Cantidad | Converge si, a partir de cierto índice | Diverge si |
|---|---|---|---|
| Cauchy ([[es/seminar-sem3/notes-2-series-basics#Teorema 8.2. Criterio de Cauchy (de la raíz)\|8.2]]) | $\sqrt[k]{a_k}$ | $\sqrt[k]{a_k}\le q<1$ | $\sqrt[k]{a_k}\ge1$ para infinitos $k$ |
| d'Alembert ([[#^cor-10-3\|10.3]]) | $\frac{a_k}{a_{k+1}}$ | $\frac{a_k}{a_{k+1}}\ge1+\beta$, $\beta>0$ | $\frac{a_k}{a_{k+1}}\le1$ a partir de cierto índice |
| Raabe ([[#^cor-11-1\|11.1]]) | $k\bigl(\frac{a_k}{a_{k+1}}-1\bigr)$ | $k\bigl(\frac{a_k}{a_{k+1}}-1\bigr)\ge1+\delta$, $\delta>0$ | $k\bigl(\frac{a_k}{a_{k+1}}-1\bigr)\le1$ a partir de cierto índice |

Los límites de estas cantidades dan las formas límite de los criterios: [[es/seminar-sem3/notes-4-examples-tests#^prop-14-3|proposición 14.3]].

## Qué se corrigió respecto a la transcripción OCR

| Lugar | En la transcripción | Correcto |
|---|---|---|
| [[#^cor-10-3\|10.3]], nota | «en la condición 2) basta con que la cota se cumpla para infinitos términos» | no basta: la cota hace falta para todo $n$ a partir de cierto índice ([[#^ex-10-4\|ejemplo 10.4]]) |
| [[#^cor-10-3\|10.3]], demostración del punto 2 | el índice $N_1$ | $N_2$ |
| [[#^cor-11-1\|11.1]], ejemplo | $a_{k+1}=\frac{2n}{2n+1}a_k$ | $a_{n+1}=\frac{2n}{2n+1}a_n$ |
| [[#^rem-11-2\|11.2]] | referencia al «ejemplo 7.4» | [[#^ex-10-4\|ejemplo 10.4]] |
| [[#^thm-12-1\|12.1]], caso $d>1$ | un intento inacabado de acotar $k\bigl(\frac{a_k}{a_{k+1}}-1\bigr)$ directamente y la misma demostración repetida el 30 oct. | se conserva una sola demostración, mediante $b_k=\frac{M_2}{k^d}$ |

[[es/seminar-sem3/notes-2-series-basics|← Parte 2]] · [[es/seminar-sem3/index|Todas las tareas y apuntes]] · [[es/seminar-sem3/notes-4-examples-tests|Parte 4 →]]
