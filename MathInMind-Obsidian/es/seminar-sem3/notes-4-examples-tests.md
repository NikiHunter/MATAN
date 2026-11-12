---
title: "Seminario NM-204. Apuntes, parte 4: ejemplos y comparación de criterios"
lang: es
tags: [mathinmind/es, mathinmind/other]
---
# Apuntes de los seminarios, parte 4: ejemplos y comparación de criterios

[[ru/seminar-sem3/notes-4-examples-tests|Русский]] · [[en/seminar-sem3/notes-4-examples-tests|English]] · **Español**

[[es/seminar-sem3/notes-3-kummer-dalembert-raabe|← Parte 3: Kummer, d'Alembert, Raabe]] · [[es/seminar-sem3/index|Todas las tareas y apuntes]] · [[es/seminar-sem3/test1-guide|Cómo prepararse para el control →]]

> [!note] Qué es esto
> Una versión reelaborada de los seminarios del 28 y 30 de octubre y del 11 de noviembre de 2026, a partir de la transcripción de [`sem3_notes`](https://github.com/NikiHunter/matan/blob/main/sem3_notes/README.md). Los números de los enunciados son los de la pizarra. El ejemplo 12.3 se empezó el 28 de octubre y se terminó el 30; aquí está completo. Al final hay un resumen de qué criterio es más fuerte; sustituye una conclusión incorrecta de la transcripción.

| Fecha | Qué se vio | Tareas |
|---|---|---|
| 28 oct., 30 oct. | [[#^ex-12-3\|sumas de senos 12.3]], [[#^ex-12-4\|sumas de cosenos 12.4]] | [[es/seminar-sem3/hw3-numerical-series#Problema 3.2\|3.2]], [[es/seminar-sem3/hw3-numerical-series#Problema 3.3\|3.3]] |
| 30 oct. | [[#^ex-13-1\|$\sum\frac{\beta^kk!}{k^k}$]], [[#^ex-13-2\|$\sum\frac{\sqrt{k+1}-\sqrt{k-1}}{k^d}$]] | [[es/seminar-sem3/hw4-series-inequalities-bases#Problema 4.8\|4.8]] |
| 11 nov. | [[#^ex-14-1\|una serie con $c_k\to1$]], [[#^rem-14-2\|Raabe ⟹ d'Alembert]], [[#^prop-14-3\|formas límite]] | [[es/seminar-sem3/hw4-series-inequalities-bases#Problema 4.7\|4.7]], [[es/seminar-sem3/hw4-series-inequalities-bases#Problema 4.4\|4.4]], [[es/seminar-sem3/hw4-series-inequalities-bases#Problema 4.6 (formas límite de los criterios)\|4.6]] |

## Seminarios del 28 y el 30 de octubre: sumas trigonométricas

### Ejemplo 12.3. Las sumas parciales de $\sum\sin(kx_0)$ están acotadas (= [[es/seminar-sem3/hw3-numerical-series#Problema 3.2|problema 3.2]])

**Afirmación.** Para todo $x_0\in\mathbb R$ la sucesión $S_n=\sum_{k=1}^n\sin(kx_0)$ está acotada, aunque la serie misma solo converge para $x_0\in\pi\mathbb Z$ ([[es/seminar-sem3/notes-2-series-basics#^ex-8-1|ejemplo 8.1]]).

^ex-12-3

**Demostración.** *Caso $x_0\in2\pi\mathbb Z$.* Todos los términos son nulos, $S_n=0$.

*Caso $x_0\notin2\pi\mathbb Z$.* Entonces $\frac{x_0}2\notin\pi\mathbb Z$ y $\sin\frac{x_0}2\ne0$. Por $\sin\alpha\sin\beta=\frac12\bigl(\cos(\alpha-\beta)-\cos(\alpha+\beta)\bigr)$,
$$
\sin(kx_0)\,\sin\frac{x_0}2=\frac12\Bigl(\cos\bigl((k-\tfrac12)x_0\bigr)-\cos\bigl((k+\tfrac12)x_0\bigr)\Bigr).
$$
La suma para $k=1,\dots,n$ es telescópica. Por inducción: al pasar de $n$ a $n+1$ se añade $\cos\bigl((n+\frac12)x_0\bigr)-\cos\bigl((n+\frac32)x_0\bigr)$, y $\cos\bigl((n+\frac12)x_0\bigr)$ se cancela. El resultado es
$$
S_n\sin\frac{x_0}2=\frac12\Bigl(\cos\frac{x_0}2-\cos\bigl((n+\tfrac12)x_0\bigr)\Bigr).
$$
Dividimos por $\sin\frac{x_0}2\ne0$ y acotamos el numerador con la desigualdad triangular:
$$
|S_n|=\frac{\bigl|\cos\frac{x_0}2-\cos\bigl((n+\frac12)x_0\bigr)\bigr|}{2\bigl|\sin\frac{x_0}2\bigr|}\le\frac{1+1}{2\bigl|\sin\frac{x_0}2\bigr|}=\frac1{\bigl|\sin\frac{x_0}2\bigr|}.
$$
La cota no depende de $n$. $\blacksquare$

**Por qué funciona.** Multiplicar por $\sin\frac{x_0}2$ convierte cada término en una diferencia de valores vecinos de una misma sucesión, y la suma «se colapsa». Geométricamente, los vectores $(\cos kx_0;\sin kx_0)$ giran cada vez un ángulo $x_0$, y su suma se queda en una región acotada. Para $x_0\notin\pi\mathbb Z$ la serie diverge de todos modos: la suma no se detiene, sino que deambula sin fin por un conjunto acotado.

### Ejemplo 12.4. Las sumas parciales de $\sum\cos(kx_0)$ (cf. [[es/seminar-sem3/hw3-numerical-series#Problema 3.3|problema 3.3]])

> El enunciado del ejemplo 12.4 no se conservó en el registro; solo queda un comentario sobre él del 30 de octubre. Por su contenido es el problema 3.3.

^ex-12-4

La identidad del seminario: $2\sin\frac{x_0}2\cos(kx_0)=\sin\bigl((k+\frac12)x_0\bigr)-\sin\bigl((k-\frac12)x_0\bigr)$. Tras la suma telescópica (por inducción, como arriba)
$$
2\sin\frac{x_0}2\sum_{k=1}^n\cos(kx_0)=\sin\bigl((n+\tfrac12)x_0\bigr)-\sin\frac{x_0}2.
$$
Así, para $x_0\notin2\pi\mathbb Z$ las sumas parciales están acotadas por $\frac1{|\sin(x_0/2)|}$, mientras que para $x_0\in2\pi\mathbb Z$ todos los términos valen $1$ y $S_n=n$ no está acotada. La serie misma diverge para todo $x_0$, porque $\cos(kx_0)\not\to0$ ([[es/seminar-sem3/hw3-numerical-series#Problema 3.3|problema 3.3]]).

## Seminario del 30 de octubre: dos series con parámetro (problema 4.8)

### Ejemplo 13.1. $\sum\frac{\beta^kk!}{k^k}$ converge para $\beta<e$ y diverge para $\beta\ge e$

Sean $\beta>0$ y $b_k=\frac{\beta^kk!}{k^k}>0$. El cociente es
$$
\frac{b_k}{b_{k+1}}=\frac{\beta^kk!}{k^k}\cdot\frac{(k+1)^{k+1}}{\beta^{k+1}(k+1)!}=\frac1\beta\Bigl(1+\frac1k\Bigr)^k=:c_k\ \xrightarrow[k\to\infty]{}\ \frac e\beta.
$$

^ex-13-1

*Caso $\beta<e$.* El límite es $\frac e\beta>1$. Tomemos $\varepsilon=\frac{e-\beta}{2\beta}$; para $k$ grande
$$
c_k>\frac e\beta-\varepsilon=\frac{e+\beta}{2\beta}=1+\frac{e-\beta}{2\beta}.
$$
La condición de convergencia de d'Alembert ([[es/seminar-sem3/notes-3-kummer-dalembert-raabe#^cor-10-3|corolario 10.3]]) se cumple con la constante $\frac{e-\beta}{2\beta}>0$.

*Caso $\beta\ge e$.* La sucesión $\bigl(1+\frac1k\bigr)^k$ crece estrictamente hacia $e$ (primer semestre), así que $\bigl(1+\frac1k\bigr)^k<e$ para todo $k$ y $c_k<\frac e\beta\le1$. La condición de divergencia de d'Alembert se cumple para todo $k$. $\blacksquare$

**Por qué funciona.** Por la fórmula de Stirling, $b_k\approx\sqrt{2\pi k}\,\bigl(\frac\beta e\bigr)^k$: casi una progresión geométrica de razón $\frac\beta e$, de ahí el umbral $\beta=e$. En el propio umbral el límite del cociente es $1$ y la forma límite del criterio no sirve. La forma no límite sí: $c_k<1$ exactamente, así que los términos crecen y no tienden a cero.

### Ejemplo 13.2. $\sum\frac{\sqrt{k+1}-\sqrt{k-1}}{k^d}$ converge si y solo si $d>\frac12$

Multiplicamos por el conjugado:
$$
a_k=\frac{\sqrt{k+1}-\sqrt{k-1}}{k^d}=\frac{2}{\bigl(\sqrt{k+1}+\sqrt{k-1}\bigr)\,k^d}.
$$
*Cota superior:* $\sqrt{k+1}+\sqrt{k-1}\ge\sqrt{k+1}>\sqrt k$, así que $a_k<\frac2{k^{d+1/2}}$.
*Cota inferior:* la desigualdad $\frac{\sqrt p+\sqrt q}2\le\sqrt{\frac{p+q}2}$ (equivalente a $\bigl(\frac{\sqrt p-\sqrt q}2\bigr)^2\ge0$) da $\sqrt{k+1}+\sqrt{k-1}\le2\sqrt k$, así que $a_k\ge\frac1{k^{d+1/2}}$.

^ex-13-2

Por tanto $a_k=\frac{d_k}{k^{d+1/2}}$ con $1\le d_k<2$, y por el [[es/seminar-sem3/notes-3-kummer-dalembert-raabe#^thm-12-1|teorema 12.1]] la serie converge si y solo si $d+\frac12>1$, es decir, $d>\frac12$. $\blacksquare$

**Por qué funciona.** Cada raíz es de orden $\sqrt k$, pero su diferencia es de orden $\frac1{\sqrt k}$: es el incremento de $\sqrt x$ en un intervalo de longitud $2$, aproximadamente $2\cdot\frac1{2\sqrt k}$. Multiplicar por el conjugado hace explícito ese orden. En el seminario primero se aplicó dos veces el criterio de comparación (por abajo y por arriba), y luego se observó que el teorema 12.1 da la respuesta de inmediato.

## Seminario del 11 de noviembre: comparación de criterios

### Ejemplo 14.1. $\sum\frac{k^{k+1/k}}{(k+1/k)^k}$ diverge (= [[es/seminar-sem3/hw4-series-inequalities-bases#Problema 4.7|problema 4.7]], 3)

$$
c_k=\frac{k^{k+\frac1k}}{\bigl(k+\frac1k\bigr)^k}=\frac{k^k\cdot k^{1/k}}{k^k\bigl(1+\frac1{k^2}\bigr)^k}=\frac{k^{1/k}}{\bigl(1+\frac1{k^2}\bigr)^k}\ \longrightarrow\ \frac11=1,
$$
porque $k^{1/k}\to1$ y $1\le\bigl(1+\frac1{k^2}\bigr)^k\le e^{1/k}\to1$. El término general no tiende a cero, así que la serie diverge ([[es/seminar-sem3/notes-2-series-basics#Corolario 6.5. Condición necesaria de convergencia|corolario 6.5]]). $\blacksquare$ ^ex-14-1

> [!note] Cómo se descifró la pizarra
> La transcripción OCR leyó el exponente $\frac1k$ como $\frac72$, y la respuesta «$\lim c_k=\frac11=1$» como «$\frac77=1$». Con $\frac72$ el cálculo no cuadra (da $c_k\to+\infty$), mientras que con $\frac1k$ todo es coherente y coincide con el problema 4.7, 3) de la tarea 4.

**Por qué funciona.** El numerador y el denominador son enormes pero casi iguales: $k+\frac1k$ se diferencia de $k$ en el factor $1+\frac1{k^2}$, y al elevar a la potencia $k$ queda un factor que tiende a $1$.

### Observación 14.2. El criterio de Raabe implica el de d'Alembert (= [[es/seminar-sem3/hw4-series-inequalities-bases#Problema 4.4|problema 4.4]])

Sea $(a_n)$ finalmente positiva. ^rem-14-2

1) Supongamos $\frac{a_n}{a_{n+1}}\ge1+\beta$ para $n>N_1$. Tomemos, por ejemplo, $\delta=5$. Como $\frac6n\to0$, existe $N_2$ a partir del cual $\frac6n<\beta$. Entonces, para $n>\max(N_1,N_2)$,
$$
\frac{a_n}{a_{n+1}}\ge1+\beta>1+\frac6n=1+\frac{1+\delta}n,
$$
se cumple la condición 1 del criterio de Raabe y la serie converge.

2) Supongamos $\frac{a_n}{a_{n+1}}\le1$ para $n>N_4$. Entonces, con mayor razón, $\frac{a_n}{a_{n+1}}\le1+\frac1n$, se cumple la condición 2 del criterio de Raabe y la serie diverge. $\blacksquare$

**Por qué funciona.** D'Alembert exige una separación constante $\beta$ entre el cociente y uno; Raabe, una separación $\frac{1+\delta}n$ que a su vez tiende a cero. Una separación constante tarde o temprano supera a cualquier $\frac cn$, así que todo lo que decide d'Alembert lo decide también Raabe. El recíproco es falso: para $\sum\frac1{n^2}$ d'Alembert no decide y Raabe da convergencia.

### Proposición 14.3. Formas límite de los criterios (= [[es/seminar-sem3/hw4-series-inequalities-bases#Problema 4.6 (formas límite de los criterios)|problema 4.6]])

Sea $(a_k)$ finalmente positiva a partir de $N_0$. Pongamos $C_k=D_k=R_k=0$ para $k\le N_0$ y
$$
C_k=\sqrt[k]{a_k},\qquad D_k=\frac{a_k}{a_{k+1}},\qquad R_k=k\Bigl(\frac{a_k}{a_{k+1}}-1\Bigr)\qquad\text{para }k>N_0.
$$
Los valores para $k\le N_0$ no influyen en nada; se definen como cero para que las sucesiones estén dadas para todo $k$. ^prop-14-3

| Si | entonces $\sum a_k$ | Por qué |
|---|---|---|
| $C_k\to L<1$ | converge | a partir de cierto índice $C_k\le\frac{1+L}2<1$; criterio de Cauchy |
| $C_k\to L>1$ | diverge | a partir de cierto índice $a_k>1$; el término general no tiende a cero |
| $D_k\to L>1$ | converge | a partir de cierto índice $D_k\ge1+\frac{L-1}2$; d'Alembert |
| $D_k\to L<1$ | diverge | a partir de cierto índice $D_k<1$; d'Alembert |
| $R_k\to L>1$ | converge | a partir de cierto índice $R_k\ge1+\frac{L-1}2$; Raabe |
| $R_k\to L<1$ | diverge | a partir de cierto índice $R_k<1$; Raabe |

> [!note] Sobre el registro
> De esta proposición la transcripción OCR solo conservó las definiciones de $C_k$, $D_k$, $R_k$; a continuación, quien la transcribió añadió una conclusión propia sobre una «jerarquía Cauchy ⟹ d'Alembert ⟹ Raabe», que así enunciada es falsa. Los seis puntos se han restaurado a partir del problema 4.6 de la tarea 4, que introduce la misma notación. Las demostraciones completas están en el [[es/seminar-sem3/hw4-series-inequalities-bases#Problema 4.6 (formas límite de los criterios)|problema 4.6]].

Para $L=1$ las tres formas límite no deciden. Para $\sum\frac1k$ y $\sum\frac1{k^2}$ se tiene $C_k\to1$ y $D_k\to1$, y para $\sum\frac1{k\ln k}$ y $\sum\frac1{k\ln^2k}$ se tiene $R_k\to1$; en cada pareja una serie diverge y la otra converge.

### Cómo se comparan los criterios

Esto no es un registro de la pizarra, sino un resumen; sustituye la conclusión incorrecta de la transcripción.

- **Raabe es más fuerte que d'Alembert** ([[#^rem-14-2|observación 14.2]]): siempre que se cumple la condición de d'Alembert, se cumple la de Raabe. El recíproco es falso: para $\sum\frac1{k^2}$, $D_k\to1$ mientras que $R_k\to2$.
- **Cauchy es más fuerte que d'Alembert para la convergencia.** Si $\frac{a_n}{a_{n+1}}\ge1+\beta$ para $n>N$, entonces $a_n\le Cq^n$ con $q=\frac1{1+\beta}$, y $\sqrt[n]{a_n}\le C^{1/n}q\to q<1$. El recíproco es falso: en el [[es/seminar-sem3/notes-3-kummer-dalembert-raabe#^ex-10-4|ejemplo 10.4]] Cauchy funciona y d'Alembert no. En forma límite: si $D_k\to L>0$, entonces $C_k\to\frac1L$.
- **Cauchy y Raabe no son comparables.** En el ejemplo 10.4 Cauchy da convergencia, mientras que $R_k$ salta entre valores negativos y muy grandes y Raabe no decide. Para $\sum\frac1{k^2}$ es al revés: $C_k=k^{-2/k}\to1$, Cauchy no decide y Raabe da convergencia.
- **Ninguno de los tres es universal.** Las series con $R_k\to1$, como $\sum\frac1{k\ln k}$ y $\sum\frac1{k\ln^2k}$, se resuelven con el criterio de Kummer con $x_n=n\ln n$ (criterio de Bertrand) o con el criterio integral ([[es/seminar-sem3/hw4-series-inequalities-bases#Problema 4.10 (criterio integral de Cauchy)|problema 4.10]]).

En resumen: d'Alembert es el más débil; Cauchy y Raabe deciden todo lo que decide él y además una clase de series propia, pero ninguno sustituye al otro.

## Qué se corrigió respecto a la transcripción OCR

| Lugar | En la transcripción | Correcto |
|---|---|---|
| [[#^ex-12-3\|12.3]] | el segundo caso primero «$x_0\notin2\pi\mathbb Z$» y luego «$x_0\notin\pi\mathbb Z$, luego $\frac{x_0}2\notin\frac\pi2\mathbb Z$» | hace falta exactamente el caso $x_0\notin2\pi\mathbb Z$: entonces $\frac{x_0}2\notin\pi\mathbb Z$ y $\sin\frac{x_0}2\ne0$ |
| [[#^ex-12-3\|12.3]] | la demostración está repartida entre el 28 y el 30 de octubre y en parte repetida | reunida en una sola |
| [[#^ex-13-1\|13.1]] | referencia «criterio de d'Alembert (§3.4)» | [[es/seminar-sem3/notes-3-kummer-dalembert-raabe#^cor-10-3\|corolario 10.3]], problema 3.7 |
| [[#^ex-13-2\|13.2]] | $2(\sqrt{k+1}+\sqrt{k-1})\le2\sqrt k$ | $\sqrt{k+1}+\sqrt{k-1}\le2\sqrt k$ |
| [[#^ex-14-1\|14.1]] | $c_k=\frac{k^{k+7/2}}{(k+7/2)^k}$, «$\lim c_k=\frac77=1$» y largos intentos de recalcular | $c_k=\frac{k^{k+1/k}}{(k+1/k)^k}$, $\lim c_k=\frac11=1$ |
| [[#^prop-14-3\|14.3]] | la conclusión «Cauchy ⟹ d'Alembert ⟹ Raabe, cada uno más fino que el anterior» | véase el [[#Cómo se comparan los criterios\|resumen]]: d'Alembert es más débil que los otros dos, y Cauchy y Raabe no son comparables |

[[es/seminar-sem3/notes-3-kummer-dalembert-raabe|← Parte 3]] · [[es/seminar-sem3/index|Todas las tareas y apuntes]] · [[es/seminar-sem3/test1-guide|Cómo prepararse para el control →]]
