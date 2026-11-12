---
title: "Seminario NM-204. Apuntes, parte 2: fundamentos de series"
lang: es
---
# Apuntes de los seminarios, parte 2: fundamentos de series

[Русский](../../ru/seminar-sem3/notes-2-series-basics.md) · [English](../../en/seminar-sem3/notes-2-series-basics.md) · **Español**

[← Parte 1: Taylor y extremos](notes-1-taylor-extremum.md) · [Todas las tareas y apuntes](index.md) · [Parte 3: Kummer, d'Alembert, Raabe →](notes-3-kummer-dalembert-raabe.md)

> **Qué es esto.** Una versión reelaborada de los seminarios del 2, 3 y 7 de octubre de 2026, a partir de la transcripción de [`sem3_notes`](../../../sem3_notes/README.md). Los números de los enunciados son los de la pizarra. Aquí está todo aquello en lo que se apoyan los criterios de convergencia: la definición, tres hechos básicos, el criterio de comparación, el criterio de la raíz de Cauchy y el criterio de comparación generalizado.

| Fecha | Qué se vio | Tareas |
|---|---|---|
| 2 oct. | [definición 6.1](#def-6-1), [proposiciones 6.2–6.4](#prop-6-2), [condición necesaria 6.5](#cor-6-5), [serie armónica 6.6](#ex-6-6) | hechos (F1), (F3) de la [tarea 3](hw3-numerical-series.md#facts) |
| 3 oct. | [series no negativas 7.1](#prop-7-1), [ejemplos 7.2–7.4](#ex-7-2), [criterio de comparación 7.5](#prop-7-5) | (F2), [3.1](hw3-numerical-series.md#p-3-1), [3.5](hw3-numerical-series.md#p-3-5) |
| 7 oct. | [la serie de senos 8.1](#ex-8-1), [criterio de Cauchy 8.2](#thm-8-2), [comparación generalizada 8.3](#thm-8-3) | [3.3](hw3-numerical-series.md#p-3-3), [3.4](hw3-numerical-series.md#p-3-4) |

<a id="sem-10-02"></a>
## Seminario del 2 de octubre: qué significa que una serie converja

<a id="def-6-1"></a>
### Definición 6.1. Serie, sumas parciales, convergencia

Para una sucesión $`(a_n)`$, las **sumas parciales** de la serie $`\sum_{n=1}^{\infty}a_n`$ son $`S_n=a_1+\dots+a_n`$. La serie **converge** si existe el límite finito $`S=\lim_{n\to\infty}S_n`$; el número $`S`$ se llama suma de la serie. Si no hay límite o es infinito, la serie **diverge**.

**Sentido.** Una serie no es una «suma infinita», sino la sucesión $`(S_n)`$. Todo lo que se sabe de límites de sucesiones pasa directamente a las series; así se demuestran las proposiciones 6.2–6.5.

<a id="prop-6-2"></a>
### Proposición 6.2. Linealidad

Si $`\sum a_n`$ y $`\sum b_n`$ convergen y $`c\in\mathbb R`$, entonces $`\sum(a_n+b_n)`$ y $`\sum ca_n`$ convergen, y
```math
\sum(a_n+b_n)=\sum a_n+\sum b_n,\qquad\sum ca_n=c\sum a_n.
```

**Demostración.** $`S_n^{(a+b)}=S_n^{(a)}+S_n^{(b)}`$ y $`S_n^{(ca)}=c\,S_n^{(a)}`$; basta pasar al límite. $`\blacksquare`$

<a id="prop-6-3"></a>
### Proposición 6.3. Un número finito de términos no influye en la convergencia

Para todo $`N`$ las series $`\sum_{n\ge1}a_n`$ y $`\sum_{n\ge N+1}a_n`$ convergen o divergen a la vez. Si convergen, $`\sum_{n\ge1}a_n=\sum_{n=1}^Na_n+\sum_{n\ge N+1}a_n`$.

**Demostración.** Sea $`\tilde S_m=a_{N+1}+\dots+a_{N+m}`$. Entonces $`S_{N+m}=S_N+\tilde S_m`$: las dos sucesiones difieren en la constante $`S_N`$. $`\blacksquare`$

<a id="prop-6-4"></a>
### Proposición 6.4. Criterio de Cauchy

La serie $`\sum a_n`$ converge si y solo si
```math
\forall\varepsilon>0\ \exists N\ \forall n>N\ \forall p\in\mathbb N:\qquad\Bigl|\sum_{k=n+1}^{n+p}a_k\Bigr|<\varepsilon.
```

**Demostración.** Es el criterio de Cauchy para la sucesión $`(S_n)`$, ya que $`S_{n+p}-S_n=\sum_{k=n+1}^{n+p}a_k`$. $`\blacksquare`$

**Sentido.** La convergencia la deciden las «colas»: cualquier trozo de la serie lejos del principio es pequeño, sea cual sea su longitud $`p`$.

<a id="cor-6-5"></a>
### Corolario 6.5. Condición necesaria de convergencia

a) Si $`\sum a_n`$ converge, entonces $`a_n\to0`$. b) Si $`a_n\not\to0`$ (no hay límite o no es cero), la serie diverge.

**Demostración.** a) $`a_n=S_n-S_{n-1}\to S-S=0`$. b) Es el contrarrecíproco de a). $`\blacksquare`$

<a id="ex-6-6"></a>
### Ejemplo 6.6. La serie armónica $`\sum\frac1n`$ diverge

**Solución.** Veamos que el criterio de Cauchy falla para $`\varepsilon=\frac12`$. Para cualquier $`N`$ tomamos $`n=N`$ y $`p=N`$:
```math
\sum_{k=N+1}^{2N}\frac1k\ge N\cdot\frac1{2N}=\frac12,
```
porque cada uno de los $`N`$ sumandos es al menos $`\frac1{2N}`$. $`\blacksquare`$

**Por qué funciona.** Aquí $`a_n=\frac1n\to0`$ y aun así la serie diverge: la condición necesaria no es suficiente. Los términos decrecen demasiado despacio: cada bloque $`\frac1{N+1}+\dots+\frac1{2N}`$ aporta al menos $`\frac12`$, y hay infinitos bloques así.

<a id="sem-10-03"></a>
## Seminario del 3 de octubre: series de términos no negativos

<a id="prop-7-1"></a>
### Proposición 7.1. Criterio de convergencia de una serie no negativa

Si $`a_n\ge0`$ para todo $`n`$, entonces $`\sum a_n`$ converge si y solo si sus sumas parciales están acotadas superiormente: existe $`K`$ con $`S_n\le K`$ para todo $`n`$.

**Demostración.** $`S_{n+1}=S_n+a_{n+1}\ge S_n`$, así que $`(S_n)`$ es no decreciente. Una sucesión monótona converge si y solo si está acotada (teorema de Weierstrass). $`\blacksquare`$

**Por qué funciona.** Las sumas parciales de una serie no negativa solo pueden crecer. Hay exactamente dos posibilidades: el crecimiento choca con un techo (convergencia) o se va a $`+\infty`$. Esta es la herramienta principal de todos los criterios siguientes: para probar la convergencia basta acotar $`S_n`$ por arriba.

<a id="ex-7-2"></a>
### Ejemplo 7.2. La serie telescópica $`\sum\frac1{n(n+1)}=1`$

Como $`\frac1{n(n+1)}=\frac1n-\frac1{n+1}`$,
```math
S_n=\Bigl(1-\frac12\Bigr)+\Bigl(\frac12-\frac13\Bigr)+\dots+\Bigl(\frac1n-\frac1{n+1}\Bigr)=1-\frac1{n+1}\ \longrightarrow\ 1.\qquad\blacksquare
```

Esta serie es la serie patrón para comparar en el [problema 3.5](hw3-numerical-series.md#p-3-5) y en el [ejemplo 9.1](notes-3-kummer-dalembert-raabe.md#ex-9-1).

<a id="prop-7-3"></a>
### Proposición 7.3. La serie geométrica

La serie $`\sum_{n\ge1}q^n`$ converge si y solo si $`|q|<1`$, y entonces su suma es $`\frac q{1-q}`$.

**Demostración.** Para $`|q|\ge1`$ el término general no tiende a cero: $`q^n=1`$ si $`q=1`$, $`(-1)^n`$ no tiene límite, y $`|q^n|\to\infty`$ si $`|q|>1`$. Por el corolario 6.5 la serie diverge. Para $`|q|<1`$ tenemos $`qS_n=S_n+q^{n+1}-q`$, de donde
```math
S_n=\frac{q(1-q^n)}{1-q}\ \longrightarrow\ \frac q{1-q},
```
porque $`q^n\to0`$. $`\blacksquare`$

**Por qué funciona.** La progresión geométrica es la serie patrón principal. Los criterios de Cauchy y de d'Alembert comparan esencialmente una serie con ella: «los términos decrecen al menos tan deprisa como $`q^n`$ para algún $`q<1`$».

<a id="ex-7-4"></a>
### Ejemplo 7.4. $`\sum(-1)^n`$: sumas parciales acotadas, pero la serie diverge

$`S_{2m}=\sum_{l=1}^m\bigl((-1)^{2l-1}+(-1)^{2l}\bigr)=0`$ y $`S_{2m-1}=S_{2m-2}+(-1)^{2m-1}=-1`$. Así que $`|S_n|\le1`$, pero $`(S_n)`$ tiene dos límites parciales, $`0`$ y $`-1`$, y la serie diverge. $`\blacksquare`$

**Por qué funciona.** La proposición 7.1 no se puede aplicar a series con términos de distinto signo: ahí las sumas parciales acotadas no dan convergencia. Las series $`\sum\sin(kx_0)`$ y $`\sum\cos(kx_0)`$ muestran el mismo efecto ([ejemplo 12.3](notes-4-examples-tests.md#ex-12-3), problemas [3.2](hw3-numerical-series.md#p-3-2) y [3.3](hw3-numerical-series.md#p-3-3)).

<a id="prop-7-5"></a>
### Proposición 7.5. El criterio de comparación

Sea $`0\le p_n\le q_n`$ para todo $`n>N_0`$. Entonces: 1) si $`\sum p_n`$ diverge, también diverge $`\sum q_n`$; 2) si $`\sum q_n`$ converge, también converge $`\sum p_n`$.

**Demostración.** 2) Por la proposición 6.3 converge la cola $`\sum_{n\ge1}q_{N_0+n}`$, y por la proposición 7.1 sus sumas parciales están acotadas por algún $`K`$. Entonces
```math
\sum_{n=1}^mp_{N_0+n}\le\sum_{n=1}^mq_{N_0+n}\le K,
```
las sumas parciales de la serie no negativa $`\sum p_{N_0+n}`$ están acotadas; converge (7.1), y con ella $`\sum p_n`$ (6.3).
1) Es el contrarrecíproco del punto 2: si $`\sum q_n`$ convergiera, también convergería $`\sum p_n`$. $`\blacksquare`$

<a id="sem-10-07"></a>
## Seminario del 7 de octubre: la serie de senos, el criterio de Cauchy, la comparación generalizada

<a id="ex-8-1"></a>
### Ejemplo 8.1. $`\sum\sin(kx_0)`$ converge si y solo si $`x_0\in\pi\mathbb Z`$

**Afirmación.** Para $`x_0\in\mathbb R`$ son equivalentes: 1) la serie $`\sum_{k\ge1}\sin(kx_0)`$ converge; 2) $`x_0=m\pi`$ para algún $`m\in\mathbb Z`$.

**Demostración.** 2) ⟹ 1). Si $`x_0=m\pi`$, entonces $`kx_0\in\pi\mathbb Z`$, todos los términos son nulos y $`S_n=0`$.

1) ⟹ 2). Por reducción al absurdo: supongamos que la serie converge pero $`\sin x_0\ne0`$. Por la condición necesaria, $`\sin(kx_0)\to0`$, y por tanto también $`y_k=\sin\bigl((k+1)x_0\bigr)\to0`$ (la misma sucesión sin su primer término). Por la fórmula del seno de la suma,
```math
y_k=\sin(kx_0)\cos x_0+\cos(kx_0)\sin x_0\quad\Longrightarrow\quad\cos(kx_0)=\frac{y_k-\cos x_0\cdot\sin(kx_0)}{\sin x_0}\ \longrightarrow\ 0.
```
Entonces $`\sin^2(kx_0)+\cos^2(kx_0)\to0`$, mientras que esa suma vale idénticamente $`1`$. Contradicción. $`\blacksquare`$

**Por qué funciona.** Si $`\sin(kx_0)`$ tendiera a cero, también tenderían a cero los senos desplazados, y los cosenos se expresan a través de ellos. El seno y el coseno de un mismo ángulo no pueden ser pequeños a la vez. El mismo truco para los cosenos está en el [problema 3.3](hw3-numerical-series.md#p-3-3).

<a id="thm-8-2"></a>
### Teorema 8.2. Criterio de Cauchy (de la raíz)

Sea $`a_n\ge0`$ para $`n\ge N_0`$.

1. Si existe $`q\in[0;1)`$ tal que $`\sqrt[n]{a_n}\le q`$ para todo $`n>N_1`$ (con $`N_1\ge N_0`$), entonces $`\sum a_n`$ converge.
2. Si $`\sqrt[n]{a_n}\ge1`$ para infinitos $`n`$, entonces $`\sum a_n`$ diverge.

**Demostración.** 1) Para $`n>N_1`$ tenemos $`a_n=\bigl(\sqrt[n]{a_n}\bigr)^n\le q^n`$, porque $`t\mapsto t^n`$ es no decreciente en $`[0;+\infty)`$. La serie $`\sum q^n`$ converge (7.3), así que por el criterio de comparación (7.5) converge $`\sum a_n`$.
2) Si $`\sqrt[n]{a_n}\ge1`$, entonces $`a_n\ge1`$. Hay infinitos índices así, de modo que $`a_n\not\to0`$ y la serie diverge por el corolario 6.5. $`\blacksquare`$

**Por qué funciona.** La desigualdad $`\sqrt[n]{a_n}\le q`$ es exactamente $`a_n\le q^n`$: el criterio de Cauchy es la comparación con una progresión geométrica escrita de forma cómoda. En el punto 2 bastan infinitos índices porque la raíz acota el propio término, no el cociente de términos vecinos. En el criterio de d'Alembert este cambio no funciona ([ejemplo 10.4](notes-3-kummer-dalembert-raabe.md#ex-10-4)).

<a id="thm-8-3"></a>
### Teorema 8.3. El criterio de comparación generalizado (= [problema 3.4](hw3-numerical-series.md#p-3-4))

Sean $`a_n`$ y $`b_n`$ positivos para $`n>N_0`$ con $`\frac{a_{n+1}}{a_n}\le\frac{b_{n+1}}{b_n}`$. Entonces: 1) si $`\sum b_n`$ converge, también converge $`\sum a_n`$; 2) si $`\sum a_n`$ diverge, también diverge $`\sum b_n`$.

**Demostración.** Multipliquemos las desigualdades para $`k=N_0+1,\dots,m`$. Los productos son telescópicos (se comprueba por inducción sobre el número de factores):
```math
\frac{a_{m+1}}{a_{N_0+1}}=\prod_{k=N_0+1}^{m}\frac{a_{k+1}}{a_k}\le\prod_{k=N_0+1}^{m}\frac{b_{k+1}}{b_k}=\frac{b_{m+1}}{b_{N_0+1}}.
```
Así, $`a_{m+1}\le C\,b_{m+1}`$ para todo $`m>N_0`$, donde $`C=\frac{a_{N_0+1}}{b_{N_0+1}}>0`$ no depende de $`m`$.

1) Si $`\sum b_n`$ converge, también converge $`\sum C\,b_{n+1}`$; por el criterio de comparación 7.5 converge $`\sum a_{n+1}`$, y con ella $`\sum a_n`$ (6.3).
2) Si $`\sum a_n`$ diverge, también diverge $`\sum\frac1C\,a_{n+1}`$, y $`\frac1C\,a_{m+1}\le b_{m+1}`$; por 7.5 diverge $`\sum b_n`$. $`\blacksquare`$

**Por qué funciona.** El cociente $`\frac{a_{n+1}}{a_n}`$ es el factor por el que se multiplica el término en un paso. Si $`a_n`$ decrece en cada paso al menos tan deprisa como $`b_n`$, entonces tras muchos pasos $`a_n\le Cb_n`$, y un factor constante $`C`$ no influye en la convergencia. Sobre este criterio se construyen los de Kummer, d'Alembert y Raabe ([parte 3](notes-3-kummer-dalembert-raabe.md)).

## Qué se corrigió respecto a la transcripción OCR

La transcripción de estos tres seminarios casi no tiene errores. Se corrigieron índices intercambiados ($`n`$ y $`k`$ en la demostración de 8.2, $`n_0`$ y $`N_0`$ en 8.3, $`l`$ y $`k`$ en 7.4) y se eliminaron repeticiones. Los registros del 2 y el 3 de octubre se hicieron a partir de capturas de la pizarra de Zoom; su contenido se cotejó con la tarea 3 y las clases.

[← Parte 1](notes-1-taylor-extremum.md) · [Todas las tareas y apuntes](index.md) · [Parte 3 →](notes-3-kummer-dalembert-raabe.md)
