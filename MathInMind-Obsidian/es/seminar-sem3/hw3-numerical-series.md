---
title: "Seminario NM-204. Tarea 3 — series numéricas: soluciones"
lang: es
hw: 3
tags: [mathinmind/es, mathinmind/other]
---
# Tarea 3. Series numéricas y criterios de convergencia — soluciones

[[ru/seminar-sem3/hw3-numerical-series|Русский]] · [[en/seminar-sem3/hw3-numerical-series|English]] · **Español**

[[es/seminar-sem3/hw2-conditional-extremum|← Tarea 2]] · [[es/seminar-sem3/index|Todas las tareas]] · [[es/seminar-sem3/hw4-series-inequalities-bases|Tarea 4 →]] · [[es/lectures-2025-26/lecture-67-68|Lecciones 67–68, §7.1–§7.2]] · [[es/lectures-2025-26/lecture-69-70|Lecciones 69–70, §7.3]]

Aquí se resuelven los problemas 3.1–3.11. Los problemas 1.2 y 2.2 de la sección de «antiguos» están resueltos en la [[es/seminar-sem3/hw1-taylor|tarea 1]] y la [[es/seminar-sem3/hw2-conditional-extremum|tarea 2]]; la serie 2'.1–2'.3, en la [[es/seminar-sem3/hw2-conditional-extremum|tarea 2]].

## Tres hechos en los que se apoya todo

> [!note] En el seminario
> (F1) es el [[es/seminar-sem3/notes-2-series-basics#Corolario 6.5. Condición necesaria de convergencia|corolario 6.5]], (F2) la [[es/seminar-sem3/notes-2-series-basics#Proposición 7.1. Criterio de convergencia de una serie no negativa|proposición 7.1]], (F3) la [[es/seminar-sem3/notes-2-series-basics#Proposición 6.3. Un número finito de términos no influye en la convergencia|proposición 6.3]] y el criterio de comparación clásico la [[es/seminar-sem3/notes-2-series-basics#Proposición 7.5. El criterio de comparación|proposición 7.5]] (2–3 oct.).

Notación: $S_n=\sum_{k=1}^na_k$ es la suma parcial.

> [!note] (F1) Condición necesaria
> Si la serie $\sum a_k$ converge, entonces $a_k\to0$. En efecto, $a_k=S_k-S_{k-1}\to S-S=0$.

> [!theorem] (F2) Criterio para series no negativas
> Si $a_k\ge0$ para todo $k$, la serie converge si y solo si la sucesión $(S_n)$ está acotada superiormente. Razón: $S_{n+1}-S_n=a_{n+1}\ge0$, la sucesión $(S_n)$ es no decreciente, y una sucesión monótona converge si y solo si está acotada.

> [!note] (F3) Un número finito de términos no influye en la convergencia
> Las series $\sum_{k\ge1}a_k$ y $\sum_{k\ge N+1}a_k$ convergen o divergen a la vez: sus sumas parciales difieren en la constante $S_N$.

De (F2) y (F3) se deduce el **criterio clásico de comparación**: si $0\le a_k\le C\,b_k$ para $k>N$ y $\sum b_k$ converge, entonces $\sum a_k$ converge (las sumas parciales de la cola de $\sum a_k$ están acotadas por $C\sum_{k>N}b_k$).

Toda la cadena de problemas 3.4 → 3.6 → 3.7, 3.9 está construida igual: cada criterio siguiente es el anterior aplicado a una serie «patrón» bien elegida.

## Problema 3.1

> [!note] En el seminario
> [[es/seminar-sem3/notes-3-kummer-dalembert-raabe#^lem-11-3|Lema 11.3]] (21 oct.); la serie $\sum(-1)^n$ es el [[es/seminar-sem3/notes-2-series-basics#^ex-7-4|ejemplo 7.4]] (3 oct.).

**Enunciado.** La serie $\sum a_k$ converge. Demostrar que la sucesión de sumas parciales está acotada.

**Demostración.** Por definición de convergencia existe el límite finito $S=\lim S_n$. Tomemos $\varepsilon=1$: existe $N$ tal que $|S_n-S|<1$ para todo $n>N$, es decir, $|S_n|<|S|+1$. Pongamos
$$
C=\max\{|S_1|,\dots,|S_N|,\ |S|+1\}.
$$
Entonces $|S_n|\le C$ para todo $n\in\mathbb N$. $\blacksquare$

**Por qué funciona.** Es simplemente el teorema «toda sucesión convergente está acotada» aplicado a $(S_n)$: los términos lejanos quedan apretados cerca del límite, y de los restantes hay un número finito. El recíproco es falso: la serie $\sum(-1)^k$ tiene sumas parciales acotadas $-1,0,-1,0,\dots$ y diverge. La acotación de las sumas parciales equivale a la convergencia solo para series de signo constante (F2). Los problemas 3.2 y 3.3 dan otros dos ejemplos de sumas parciales acotadas de series divergentes.

## Problema 3.2

> [!note] En el seminario
> [[es/seminar-sem3/notes-4-examples-tests#^ex-12-3|Ejemplo 12.3]] (28–30 oct.).

**Enunciado.** $x_0\in\mathbb R$. Demostrar que las sumas parciales de $\sum_{k=1}^\infty\sin(kx_0)$ están acotadas.

**Demostración.** Sea $S_n=\sum_{k=1}^n\sin(kx_0)$.

*Caso $x_0=2\pi m$, $m\in\mathbb Z$.* Entonces $\sin(kx_0)=0$ para todo $k$, y $S_n=0$.

*Caso $x_0\notin2\pi\mathbb Z$.* Entonces $\sin\frac{x_0}2\ne0$. Demostremos por inducción la igualdad
$$
2\sin\frac{x_0}2\cdot S_n=\cos\frac{x_0}2-\cos\Bigl(\bigl(n+\tfrac12\bigr)x_0\Bigr).\tag{1}
$$
Se basa en la fórmula $2\sin\alpha\sin\beta=\cos(\beta-\alpha)-\cos(\beta+\alpha)$ con $\alpha=\frac{x_0}2$, $\beta=kx_0$:
$$
2\sin\frac{x_0}2\sin(kx_0)=\cos\Bigl(\bigl(k-\tfrac12\bigr)x_0\Bigr)-\cos\Bigl(\bigl(k+\tfrac12\bigr)x_0\Bigr).\tag{2}
$$
Base $n=1$: (1) coincide con (2) para $k=1$. Paso: si (1) vale para $n$, sumando (2) con $k=n+1$,
$$
2\sin\frac{x_0}2\,S_{n+1}=\cos\frac{x_0}2-\cos\Bigl(\bigl(n+\tfrac12\bigr)x_0\Bigr)+\cos\Bigl(\bigl(n+\tfrac12\bigr)x_0\Bigr)-\cos\Bigl(\bigl(n+\tfrac32\bigr)x_0\Bigr),
$$
que es (1) para $n+1$. De (1):
$$
|S_n|=\frac{\bigl|\cos\frac{x_0}2-\cos\bigl((n+\frac12)x_0\bigr)\bigr|}{2\bigl|\sin\frac{x_0}2\bigr|}\le\frac{1}{\bigl|\sin\frac{x_0}2\bigr|}.
$$
La cota no depende de $n$. $\blacksquare$

**Por qué funciona.** Multiplicar por $2\sin\frac{x_0}2$ convierte cada sumando en la diferencia de dos valores «vecinos» de una misma sucesión $c_k=\cos\bigl((k-\frac12)x_0\bigr)$: el sumando vale $c_k-c_{k+1}$. En la suma todo lo interior se cancela (suma telescópica) y solo quedan los extremos. Geométricamente, $\sin(kx_0)$ son las proyecciones de un vector que gira cada vez un ángulo $x_0$; la suma de tales vectores recorre una circunferencia de radio $\frac1{2|\sin(x_0/2)|}$ y no se va al infinito. Cuando $x_0\to2\pi m$ la cota empeora (el radio crece), pero en el propio $2\pi m$ todos los sumandos son nulos. La cota depende de $x_0$ pero no de $n$: eso basta.

## Problema 3.3

> [!note] En el seminario
> La serie de senos converge solo para $x_0\in\pi\mathbb Z$: [[es/seminar-sem3/notes-2-series-basics#^ex-8-1|ejemplo 8.1]] (7 oct.); la identidad para las sumas de cosenos: [[es/seminar-sem3/notes-4-examples-tests#^ex-12-4|ejemplo 12.4]] (30 oct.).

**Enunciado.** $x_0\in\mathbb R$. Demostrar que la serie $\sum_{k=1}^\infty\cos(kx_0)$ diverge. $^*$ ¿Para qué $x_0$ están acotadas sus sumas parciales?

**Divergencia.** Veamos que no se cumple la condición necesaria (F1): $\cos(kx_0)\not\to0$. Supongamos lo contrario: $\cos(kx_0)\to0$ cuando $k\to\infty$. Entonces la subsucesión de índices pares también tiende a cero: $\cos(2kx_0)\to0$. Pero
$$
\cos(2kx_0)=2\cos^2(kx_0)-1\ \longrightarrow\ 2\cdot0-1=-1 .
$$
Contradicción ($0\ne-1$). Así que el término general no tiende a cero y la serie diverge para todo $x_0$. $\blacksquare$

En los términos de la indicación: para $\cos x_0=1$ ($x_0=2\pi m$) todos los términos valen $1$; para $\cos x_0=-1$ ($x_0=\pi+2\pi m$) los términos son $(-1)^k$; en los demás casos los términos no tienen límite. El razonamiento anterior cubre los tres casos a la vez.

**Acotación de las sumas parciales.** Sea $S_n=\sum_{k=1}^n\cos(kx_0)$.

- Si $x_0=2\pi m$, entonces $S_n=n$: no acotada.
- Si $x_0\notin2\pi\mathbb Z$, entonces $\sin\frac{x_0}2\ne0$, y el factor adecuado es otra vez $2\sin\frac{x_0}2$: por la fórmula $2\sin\alpha\cos\beta=\sin(\beta+\alpha)-\sin(\beta-\alpha)$
$$
2\sin\frac{x_0}2\cos(kx_0)=\sin\Bigl(\bigl(k+\tfrac12\bigr)x_0\Bigr)-\sin\Bigl(\bigl(k-\tfrac12\bigr)x_0\Bigr),
$$
y por inducción (como en 3.2)
$$
2\sin\frac{x_0}2\cdot S_n=\sin\Bigl(\bigl(n+\tfrac12\bigr)x_0\Bigr)-\sin\frac{x_0}2,\qquad|S_n|\le\frac{1}{\bigl|\sin\frac{x_0}2\bigr|}.
$$
Aquí entra también el caso $\cos x_0=-1$: allí $S_n\in\{-1,0\}$.

**Respuesta.** La serie diverge para todo $x_0$. Las sumas parciales están acotadas si y solo si $x_0\notin\{2\pi m:\ m\in\mathbb Z\}$.

**Por qué funciona.** Los cosenos se cancelan «en promedio» igual que los senos, por eso las sumas están acotadas. Pero los sumandos no decrecen, y la suma no se detiene: recorre sin fin un conjunto acotado. La única excepción es $x_0=2\pi m$, donde todos los sumandos valen $1$ y no hay nada que cancelar. Compárese con 3.2: la serie de senos consta de ceros y converge para $x_0\in\pi\mathbb Z$, y diverge para $x_0\notin\pi\mathbb Z$ por la misma razón. Si $\sin(kx_0)\to0$, entonces $\cos(2kx_0)=1-2\sin^2(kx_0)\to1$ y $\sin(2kx_0)\to0$, de donde $\sin((2k+1)x_0)=\sin(2kx_0)\cos x_0+\cos(2kx_0)\sin x_0\to\sin x_0\ne0$, aunque es una subsucesión de una sucesión que tiende a cero.

## Problema 3.4 (criterio de comparación generalizado)

> [!note] En el seminario
> [[es/seminar-sem3/notes-2-series-basics#^thm-8-3|Teorema 8.3]] (7 oct.): la demostración multiplicando los cocientes.

**Enunciado.** Para $n>N_0$: $a_n>0$, $b_n>0$ y $\dfrac{a_{n+1}}{a_n}\le\dfrac{b_{n+1}}{b_n}$. Demostrar: a) si $\sum b_k$ converge, entonces $\sum a_k$ converge; b) si $\sum a_k$ diverge, entonces $\sum b_k$ diverge.

**Demostración.** Reescribamos la condición: para $n>N_0$
$$
\frac{a_{n+1}}{b_{n+1}}\le\frac{a_n}{b_n}
$$
(se multiplicaron ambos miembros por el número positivo $\frac{a_n}{b_{n+1}}$). Así que la sucesión $\frac{a_n}{b_n}$ es no creciente para $n>N_0$, y para todo $n\ge N_0+1$
$$
\frac{a_n}{b_n}\le\frac{a_{N_0+1}}{b_{N_0+1}}=:C,\qquad\text{es decir,}\qquad0<a_n\le C\,b_n .
$$
(Lo mismo se obtiene multiplicando las desigualdades $\frac{a_{j+1}}{a_j}\le\frac{b_{j+1}}{b_j}$ para $j=N_0+1,\dots,n-1$: los productos son telescópicos y dan $\frac{a_n}{a_{N_0+1}}\le\frac{b_n}{b_{N_0+1}}$.)

a) Sea $\sum b_k$ convergente. Por (F3) converge la cola $\sum_{k>N_0}b_k$; sea $B$ su suma. Para $n>N_0$
$$
\sum_{k=N_0+1}^na_k\le C\sum_{k=N_0+1}^nb_k\le C\,B .
$$
Las sumas parciales de la serie positiva $\sum_{k>N_0}a_k$ están acotadas, por (F2) converge, y por (F3) también $\sum_{k\ge1}a_k$.

b) Es el contrarrecíproco de a): si $\sum b_k$ convergiera, por a) convergería $\sum a_k$, contra la hipótesis. $\blacksquare$

**Por qué funciona.** El cociente $\frac{a_{n+1}}{a_n}$ es la «velocidad de decrecimiento» de la serie en un paso. La condición dice que en cada paso $a_n$ decrece no más despacio que $b_n$. Pero entonces también en muchos pasos $a_n$ decrece no más despacio, es decir, $a_n$ no supera a $b_n$ salvo un factor constante, y un factor constante no influye en la convergencia. El criterio generalizado es el clásico en el que, en vez de los términos, se comparan sus cocientes; es cómodo cuando el cociente $\frac{a_{n+1}}{a_n}$ es más sencillo que el propio $a_n$ (factoriales, productos).

## Problema 3.5

> [!note] En el seminario
> El apartado b) es el [[es/seminar-sem3/notes-3-kummer-dalembert-raabe#^ex-9-1|ejemplo 9.1]] (16 oct.); la serie patrón $\sum\frac1{k(k+1)}$ es el [[es/seminar-sem3/notes-2-series-basics#^ex-7-2|ejemplo 7.2]].

**Enunciado.** Demostrar la convergencia de $\sum_{k=1}^\infty\frac1{k!}$: a) con el criterio clásico de comparación; b) con el generalizado.

Patrón: la serie $\sum_{k=1}^\infty\frac{1}{k(k+1)}$ converge (sus sumas parciales valen $1-\frac1{n+1}$).

**a)** Para $k\ge1$ se tiene $(k+1)!=(k+1)\cdot k\cdot(k-1)!\ge k(k+1)$, de donde
$$
0<\frac1{(k+1)!}\le\frac1{k(k+1)} .
$$
Por el criterio clásico de comparación converge la serie $\sum_{k=1}^\infty\frac1{(k+1)!}=\sum_{k=2}^\infty\frac1{k!}$, y con ella, por (F3), $\sum_{k=1}^\infty\frac1{k!}$. $\blacksquare$

**b)** Sean $a_k=\frac1{k!}$, $b_k=\frac1{k(k+1)}$. Entonces
$$
\frac{a_{k+1}}{a_k}=\frac1{k+1},\qquad\frac{b_{k+1}}{b_k}=\frac{k(k+1)}{(k+1)(k+2)}=\frac{k}{k+2}.
$$
La desigualdad $\frac1{k+1}\le\frac k{k+2}$ equivale a $k+2\le k^2+k$, es decir, $k^2\ge2$; vale para todo $k\ge2$. La hipótesis del problema 3.4 se cumple con $N_0=1$, la serie $\sum b_k$ converge, luego $\sum a_k$ converge. $\blacksquare$

**Por qué funciona.** El factorial crece más rápido que cualquier polinomio, así que $\frac1{k!}$ queda con holgura por debajo de un patrón del tipo $\frac1{k^2}$. En el apartado b) se ve para qué sirve el criterio generalizado: el cociente de términos consecutivos $\frac1{k+1}$ de la serie factorial tiende a cero, el del patrón, $\frac k{k+2}$, tiende a uno, y son más fáciles de comparar que los propios términos. Para $k=1$ la desigualdad de cocientes falla ($\frac12>\frac13$), pero el criterio solo la necesita a partir de cierto índice.

## Problema 3.6 (criterio de Kummer)

> [!note] En el seminario
> [[es/seminar-sem3/notes-3-kummer-dalembert-raabe#^thm-10-2|Teorema 10.2]] (16 oct.).

**Enunciado.** $x_n>0$ para todo $n$; $a_n>0$ para $n>N_0$.

1) Si para cierto $\alpha>0$ y todo $n>N_1$ (con $N_1>N_0$) se cumple $x_n\dfrac{a_n}{a_{n+1}}-x_{n+1}\ge\alpha$, entonces $\sum a_k$ converge.

2) Si $\sum\dfrac1{x_k}$ diverge y para todo $n>N_2$ (con $N_2>N_0$) se cumple $x_n\dfrac{a_n}{a_{n+1}}-x_{n+1}\le0$, entonces $\sum a_k$ diverge.

**Demostración de 1).** Multipliquemos la desigualdad por $a_{n+1}>0$: para $n>N_1$
$$
x_na_n-x_{n+1}a_{n+1}\ge\alpha\,a_{n+1}.\tag{3}
$$
Sumemos (3) para $n=N_1+1,\dots,N_1+m$. A la izquierda la suma es telescópica:
$$
\alpha\sum_{n=N_1+1}^{N_1+m}a_{n+1}\le x_{N_1+1}a_{N_1+1}-x_{N_1+m+1}a_{N_1+m+1}<x_{N_1+1}a_{N_1+1},
$$
pues el sustraendo es positivo. Así, para todo $m$
$$
\sum_{k=1}^ma_{k+N_1+1}<x_{N_1+1}\cdot\frac{a_{N_1+1}}{\alpha}.
$$
Las sumas parciales de la serie positiva $\sum_{k\ge1}a_{k+N_1+1}$ están acotadas, por (F2) converge, y por (F3) converge $\sum a_k$. $\blacksquare$

**Demostración de 2).** Para $n>N_2$ la condición da $x_na_n\le x_{n+1}a_{n+1}$, es decir,
$$
\frac{a_{n+1}}{a_n}\ge\frac{x_n}{x_{n+1}}=\frac{1/x_{n+1}}{1/x_n}.
$$
Sea $c_n=\frac1{x_n}>0$. Entonces $\frac{c_{n+1}}{c_n}\le\frac{a_{n+1}}{a_n}$ para $n>N_2$, y la serie $\sum c_k$ diverge. Por el problema 3.4 b) (con $c$ en el papel de «$a$» y $a$ en el de «$b$») la serie $\sum a_k$ diverge. $\blacksquare$

**Por qué funciona.** La cantidad $x_na_n$ es un término «ponderado» de la serie. La desigualdad (3) dice: en cada paso el término ponderado disminuye al menos en $\alpha a_{n+1}$. Pero $x_na_n$ es positivo y no puede disminuir en total más que su valor inicial. Por eso la suma de todas las «disminuciones», es decir, $\alpha\sum a_{n+1}$, es finita. Es un argumento de conservación: la serie paga cada uno de sus términos con el presupuesto limitado $x_{N_1+1}a_{N_1+1}$.

En el segundo apartado el término ponderado $x_na_n$ no decrece, luego $a_n\ge\frac{\mathrm{const}}{x_n}$: la serie mayora a la serie divergente $\sum\frac1{x_n}$. La divergencia de $\sum\frac1{x_k}$ hace falta justo aquí, y sin ella el enunciado es falso: para $x_n=n^2$ y $a_n=\frac1{n^2}$ el primer miembro vale $n^2\cdot\frac{(n+1)^2}{n^2}-(n+1)^2=0\le0$, y sin embargo la serie converge.

El criterio de Kummer no es un criterio sino un molde: cada sucesión $(x_n)$ da su propio criterio. Cuanto más despacio diverge $\sum\frac1{x_n}$, más fino es el criterio: $x_n=1$ da d'Alembert (3.7), $x_n=n$ da Raabe (3.9), $x_n=n\ln n$ da el criterio de Bertrand.

## Problema 3.7 (criterio de d'Alembert)

> [!note] En el seminario
> [[es/seminar-sem3/notes-3-kummer-dalembert-raabe#^cor-10-3|Corolario 10.3]] (16 oct.).

**Enunciado.** $a_n>0$ para $n>N_0$. 1) Si $\dfrac{a_n}{a_{n+1}}\ge1+\beta$ para $n>N_1$, $\beta>0$, la serie converge. 2) Si $\dfrac{a_n}{a_{n+1}}\le1$ para $n>N_2$, la serie diverge.

**Demostración.** Aplicamos el criterio de Kummer con $x_n=1$ para todo $n$. Entonces
$$
x_n\frac{a_n}{a_{n+1}}-x_{n+1}=\frac{a_n}{a_{n+1}}-1 .
$$
1) Por hipótesis esta cantidad es $\ge\beta$ para $n>N_1$; por 3.6, 1) con $\alpha=\beta$ la serie converge.
2) La serie $\sum\frac1{x_k}=\sum1$ diverge, y $\frac{a_n}{a_{n+1}}-1\le0$ para $n>N_2$; por 3.6, 2) la serie diverge. $\blacksquare$

**Por qué funciona.** En el apartado 1) $a_{n+1}\le\frac{a_n}{1+\beta}$: los términos decrecen no más despacio que una progresión geométrica de razón $q=\frac1{1+\beta}<1$. En el apartado 2) $a_{n+1}\ge a_n>0$: los términos no decrecen y no tienden a cero, falla (F1). Es importante que en 1) se necesita un margen $\beta>0$ independiente de $n$: la condición $\frac{a_n}{a_{n+1}}>1$ no basta (serie armónica: $\frac{a_n}{a_{n+1}}=1+\frac1n>1$, y la serie diverge). Ese «margen que tiende a cero» es lo que trata el criterio de Raabe.

## Problema 3.8

> [!note] En el seminario
> [[es/seminar-sem3/notes-3-kummer-dalembert-raabe#^ex-10-4|Ejemplo 10.4]] (16 oct.).

**Enunciado.** $a_k=2^{-k}$ para $k$ impar, $a_k=3^{-k}$ para $k$ par. Demostrar: 1) la serie converge; 2) los conjuntos $\bigl\{k:\ \frac{a_k}{a_{k+1}}\le1\bigr\}$ y $\bigl\{k:\ \frac{a_k}{a_{k+1}}\ge\frac92\bigr\}$ son numerables.

**Demostración.** 1) Para todo $k$ se tiene $0<a_k\le2^{-k}$, y la serie geométrica $\sum2^{-k}$ converge; por el criterio clásico de comparación la serie converge.

2) *$k$ par.* Entonces $k+1$ es impar y
$$
\frac{a_k}{a_{k+1}}=\frac{3^{-k}}{2^{-(k+1)}}=2\Bigl(\frac23\Bigr)^k\le2\cdot\frac49=\frac89<1 .
$$
*$k$ impar.* Entonces $k+1$ es par y
$$
\frac{a_k}{a_{k+1}}=\frac{2^{-k}}{3^{-(k+1)}}=3\Bigl(\frac32\Bigr)^k\ge3\cdot\frac32=\frac92 .
$$
Así, el primer conjunto son todos los números pares y el segundo todos los impares. Cada uno es un subconjunto infinito de $\mathbb N$, luego numerable (biyecciones $m\mapsto2m$ y $m\mapsto2m-1$). $\blacksquare$

**Por qué funciona.** La serie está formada por dos progresiones geométricas intercaladas. Pasar de la progresión «lenta» a la «rápida» da un cociente enorme; el paso inverso da un cociente menor que uno, es decir, el término **crece**. Por eso la desigualdad $\frac{a_k}{a_{k+1}}\le1$ de la condición de divergencia de d'Alembert se cumple para infinitos $k$, y sin embargo la serie converge. Conclusión: en el criterio de d'Alembert las palabras «a partir de cierto índice» no se pueden sustituir por «para infinitos índices».

En el criterio de la raíz de Cauchy esa sustitución sí es legítima: si $\sqrt[k]{a_k}\ge1$ para infinitos $k$, entonces $a_k\ge1$ para infinitos $k$, el término general no tiende a cero y la serie diverge. La diferencia es que la raíz estima el **propio** término, mientras que el cociente solo ve su cambio en un paso: un paso hacia arriba no impide que la serie decrezca en conjunto. Para nuestra serie $\sqrt[k]{a_k}\le\frac12$, y el criterio de Cauchy da la convergencia de inmediato, mientras que d'Alembert no da nada (ninguna de sus condiciones se cumple a partir de cierto índice).

## Problema 3.9 (criterio de Raabe)

> [!note] En el seminario
> [[es/seminar-sem3/notes-3-kummer-dalembert-raabe#^cor-11-1|Corolario 11.1]] (21 oct.), con un ejemplo en el que d'Alembert no decide y Raabe da divergencia.

**Enunciado.** $a_n>0$ para $n>N_0$. 1) Si $\dfrac{a_n}{a_{n+1}}\ge1+\dfrac{1+\gamma}n$ para $n>N_1$, $\gamma>0$, la serie converge. 2) Si $\dfrac{a_n}{a_{n+1}}\le1+\dfrac1n$ para $n>N_2$, la serie diverge.

**Demostración.** Aplicamos el criterio de Kummer con $x_n=n$.

1) Para $n>N_1$
$$
x_n\frac{a_n}{a_{n+1}}-x_{n+1}\ge n\Bigl(1+\frac{1+\gamma}n\Bigr)-(n+1)=\gamma .
$$
Por 3.6, 1) con $\alpha=\gamma$ la serie converge.

2) La serie $\sum\frac1{x_k}=\sum\frac1k$ diverge (armónica), y para $n>N_2$
$$
x_n\frac{a_n}{a_{n+1}}-x_{n+1}\le n\Bigl(1+\frac1n\Bigr)-(n+1)=0 .
$$
Por 3.6, 2) la serie diverge. $\blacksquare$

**Por qué funciona.** El patrón aquí son las series $\sum\frac1{n^p}$: para ellas $\frac{a_n}{a_{n+1}}=\bigl(1+\frac1n\bigr)^p\approx1+\frac pn$. El criterio de Raabe mide el coeficiente de $\frac1n$ en el cociente de términos consecutivos: si supera a uno con margen ($1+\gamma$), la serie se comporta como $\sum\frac1{n^{1+\gamma}}$ y converge; si no supera a uno, la serie no es mejor que la armónica. La condición 2) significa exactamente $(n+1)a_{n+1}\ge na_n$, es decir, $na_n$ no decrece y $a_n\ge\frac{\mathrm{const}}n$.

El criterio de Raabe es más fuerte que el de d'Alembert (problema 4.4 de la tarea 4): funciona donde $\frac{a_n}{a_{n+1}}\to1$ y d'Alembert calla. Pero también tiene su «zona muerta»: un coeficiente de $\frac1n$ que tiende a $1$ por arriba (por ejemplo, $a_n=\frac1{n\ln^2n}$).

## Problema 3.10$^*$

> [!note] En el seminario
> [[es/seminar-sem3/notes-3-kummer-dalembert-raabe#^rem-11-2|Observación 11.2]] (21 oct.), con el mismo ejemplo.

^p-3-10

**Enunciado.** Dar un ejemplo de serie convergente para la que el conjunto $\bigl\{k:\ \frac{a_k}{a_{k+1}}\le1+\frac1k\bigr\}$ sea numerable.

**Solución.** Sirve la serie del problema 3.8: $a_k=2^{-k}$ para $k$ impar y $a_k=3^{-k}$ para $k$ par. Converge, todos sus términos son positivos y, como allí se mostró:

- para $k$ par: $\dfrac{a_k}{a_{k+1}}\le\dfrac89<1<1+\dfrac1k$; tales $k$ pertenecen al conjunto;
- para $k$ impar: $\dfrac{a_k}{a_{k+1}}\ge\dfrac92>2\ge1+\dfrac1k$; tales $k$ no pertenecen.

El conjunto es el de todos los números pares, que es numerable. $\blacksquare$

**Por qué funciona.** El problema muestra para el criterio de Raabe lo mismo que 3.8 para el de d'Alembert: la condición de divergencia $\frac{a_k}{a_{k+1}}\le1+\frac1k$ debe cumplirse **para todo** $k$ suficientemente grande; un conjunto infinito de índices no basta. El ejemplo se toma a propósito con términos positivos: si se admiten series de signo variable, el problema queda vacío (para $\sum\frac{(-1)^k}{k^2}$ todos los cocientes son negativos y el conjunto es $\mathbb N$).

Un ejemplo más fino, en el que el cociente está en el intervalo semiabierto $(1;1+\frac1k]$ para infinitos $k$ (los términos decrecen, pero despacio), se construye en el problema 4.5 de la [[es/seminar-sem3/hw4-series-inequalities-bases|tarea 4]]; también sirve aquí.

## Problema 3.11$^{**}$

> [!note] En el seminario
> [[es/seminar-sem3/notes-3-kummer-dalembert-raabe#^thm-12-1|Teorema 12.1]] (28 oct.): la demostración con la fórmula de Taylor con resto de Peano.

^p-3-11

**Enunciado.** $\alpha\in\mathbb R$, $0<M_1\le C_k\le M_2$, $a_k=\dfrac{C_k}{k^\alpha}$. ¿Para qué $\alpha$ converge $\sum a_k$?

**Respuesta.** La serie converge para $\alpha>1$ y diverge para $\alpha\le1$.

**Solución.** De la hipótesis
$$
\frac{M_1}{k^\alpha}\le a_k\le\frac{M_2}{k^\alpha}.\tag{4}
$$

*$\alpha\le0$.* Entonces $k^{-\alpha}\ge1$ y $a_k\ge M_1>0$: el término general no tiende a cero, la serie diverge por (F1).

*$0<\alpha\le1$.* Entonces $k^\alpha\le k$ y $a_k\ge\frac{M_1}{k}$. La serie armónica diverge, luego por el criterio clásico de comparación (si $\sum a_k$ convergiera, convergería $\sum\frac1k$) la serie diverge.

*$\alpha>1$.* Demostremos la convergencia del patrón $b_k=\frac1{k^\alpha}$ con el criterio de Raabe. El cociente es
$$
\frac{b_k}{b_{k+1}}=\Bigl(1+\frac1k\Bigr)^\alpha .
$$
Por la fórmula de Taylor con resto de Lagrange para $g(x)=(1+x)^\alpha$, para $x>0$ existe $\theta\in(0,1)$ con
$$
(1+x)^\alpha=1+\alpha x+\frac{\alpha(\alpha-1)}2(1+\theta x)^{\alpha-2}x^2\ \ge\ 1+\alpha x,
$$
pues para $\alpha>1$ el resto es no negativo. Con $x=\frac1k$:
$$
\frac{b_k}{b_{k+1}}\ge1+\frac\alpha k=1+\frac{1+\gamma}k,\qquad\gamma=\alpha-1>0,
$$
para todo $k\in\mathbb N$. Por el problema 3.9, 1) la serie $\sum\frac1{k^\alpha}$ converge. Del segundo miembro de (4), por el criterio clásico de comparación, converge también $\sum a_k$. $\blacksquare$

**Por qué funciona.** Un factor $C_k$ acotado y separado de cero no influye en la convergencia: la serie queda encerrada entre dos múltiplos del patrón $\sum\frac1{k^\alpha}$. La frontera $\alpha=1$ es exactamente la frontera del criterio de Raabe: el coeficiente de $\frac1k$ en el cociente $\frac{b_k}{b_{k+1}}\approx1+\frac\alpha k$ es $\alpha$.

¿Por qué no se puede aplicar Raabe directamente a $a_k$? Porque $\frac{a_k}{a_{k+1}}=\frac{C_k}{C_{k+1}}\bigl(1+\frac1k\bigr)^\alpha$, y del cociente $\frac{C_k}{C_{k+1}}$ no se sabe nada: puede saltar (por ejemplo, $C_k=2+(-1)^k$ da los cocientes $3$ y $\frac13$). Los criterios basados en cocientes son sensibles a tales oscilaciones; el de comparación, no. El orden correcto: primero eliminar $C_k$ por comparación, después estudiar el patrón suave.

El resultado se usará a menudo así: si $a_k=\frac{C_k}{k^\alpha}$ con $C_k$ entre dos constantes positivas (en particular, si $C_k$ tiene límite finito positivo), la serie converge exactamente cuando $\alpha>1$.
