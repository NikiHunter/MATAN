---
title: "Lecciones 69–70 — series positivas, criterios de convergencia, series de términos de signo arbitrario, reordenaciones"
lang: es
course: "Análisis matemático, 2025/26"
lecture: 69-70
semester: 3
source: "cuaderno manuscrito, págs. p022–p029"
source_pages: "p022, p023, p024, p025, p026, p027, p028, p029"
course_chapter: 23
aliases: ["Lecciones 69–70 (es)"]
tags: [mathinmind/es, mathinmind/lecture]
---
# Lecciones 69–70 — series positivas, criterios de convergencia, series de términos de signo arbitrario, reordenaciones

[[es/lectures-2025-26/lecture-67-68|← Lecciones 67–68]] · [[es/lectures-2025-26/index|Índice de lecciones]] · [[es/lectures-2025-26/lecture-71-72|Lecciones 71–72 →]] · [[es/term-index|Términos y teoremas]] · [[ru/lectures-2025-26/lecture-69-70|Русский]] · [[en/lectures-2025-26/lecture-69-70|English]]

> [!info] Fuente y numeración
> Los apuntes se copiaron de un cuaderno manuscrito (págs. p022–p029; el texto bruto de las páginas está en [`ocr/raw/`](https://github.com/NikiHunter/matan/blob/main/ocr/raw/p022.md)). La pág. p022 contiene solo el título «Lecciones 69–70» y un breve plan de la clase de dos puntos, leídos solo en parte («… conv.», «Otros ej. vistos»); el resto de la página está vacío. Por eso la definición de serie positiva y los enunciados de sus propiedades, cuyas demostraciones comienzan en la pág. p023, se restauran a partir de las diapositivas del curso 2024/25. Entre las págs. p025 y p026 se perdieron el enunciado del criterio de Cauchy y el comienzo de su demostración; entre las págs. p028 y p029, la transformación de Abel, el criterio de Dirichlet y el enunciado del criterio de Abel; estos lugares también se restauran. La numeración de las definiciones es la del profesor; el profesor no numera los criterios de convergencia. Los lapsus de los apuntes se corrigen y se marcan con bloques «Corrección de la fuente»; los pasajes perdidos se restauran y se marcan con bloques «Restaurado»; las etiquetas corresponden a [`ocr/RESOLVED.md`](https://github.com/NikiHunter/matan/blob/main/ocr/RESOLVED.md). Los lugares que aún hay que cotejar con el cuaderno se enumeran en [`ocr/ISSUES.md`](https://github.com/NikiHunter/matan/blob/main/ocr/ISSUES.md).

## §7.3. Series positivas


> [!note] Restaurado
> (según las diapositivas del curso 2024/25, FS p54; cf. los apuntes de 2022, M3S p40). La pág. p022 del cuaderno está vacía tras el título y el plan; a continuación, la definición y las propiedades cuyas demostraciones están escritas en la pág. p023.
>
> **Definición 7.3.1.** Una serie $\sum_{n=1}^{\infty}a_n$ se llama positiva si $a_n\ge0$ para todo $n$.
>
> **Propiedades.**
>
> 1. Toda serie positiva tiene suma (finita o infinita).
> 2. Una serie positiva converge si y solo si la sucesión de sus [[es/04-numeric-series#4.1 Sumas parciales|sumas parciales]] $(S_N)_{N\in\mathbb N}$ está acotada.

^def-7-3-1


**Demostración de la propiedad 2.** Sea $S_N=\sum_{n=1}^{N}a_n$. La sucesión $(S_N)$ es no decreciente, ya que $S_{N+1}-S_N=a_{N+1}\ge0$. Por el teorema del límite de una [[es/lectures-2025-26/lecture-11-12#^def-2-3-5|sucesión monótona]], una sucesión no decreciente converge si y solo si está [[es/lectures-2025-26/lecture-05-06#^def-1-3-7|acotada superiormente]]; como además $S_N\ge0$, la convergencia de $(S_N)$, es decir, la convergencia de la serie, equivale a la acotación de $(S_N)$. $\square$

^p023

**Demostración de la propiedad 1.** Por el teorema del [[es/lectures-2025-26/lecture-08#^def-2-1-2|límite de una sucesión]] monótona, la sucesión no decreciente $(S_N)$ tiene límite, finito o igual a $+\infty$. Por tanto, o bien la serie $\sum_{n=1}^{\infty}a_n$ converge, o bien $S:=\lim_{N\to\infty}S_N=+\infty$. $\square$

> [!info] Corrección de la fuente
> (S090). Los apuntes tienen el título «Dem. (prop. II)». Aquí se demuestra la propiedad 1 (la existencia de la suma); así está marcado este punto también en las notas del profesor (FS p54, M3S p40).

**Observación.** Para que la sucesión $(S_N)$ esté acotada superiormente basta que lo esté alguna de sus [[es/lectures-2025-26/lecture-11-12#^def-2-3-7|subsucesiones]] $(S_{N_k})$. En efecto, sea $S_{N_k}\le M$ para todo $k$. Para todo $N$ se puede hallar $k$ tal que $N_k>N$, y entonces, como $(S_N)$ es no decreciente, $S_N\le S_{N_k}\le M$.

### Primer criterio de comparación

Sean dadas dos series positivas $\sum_{n=1}^{\infty}a_n$ y $\sum_{n=1}^{\infty}b_n$ ($a_n\ge0$, $b_n\ge0$ para todo $n$) y sea $b_n\ge a_n$ para todo $n$. Entonces:

1. si la serie $\sum_{n=1}^{\infty}b_n$ converge, la serie $\sum_{n=1}^{\infty}a_n$ converge;
2. si la serie $\sum_{n=1}^{\infty}a_n$ diverge, la serie $\sum_{n=1}^{\infty}b_n$ diverge.

**Demostración.** Pongamos $A_N=\sum_{n=1}^{N}a_n$, $B_N=\sum_{n=1}^{N}b_n$. Como $a_n\le b_n$ para todo $n$, se tiene $A_N\le B_N$ para todo $N$.

1. Supongamos que la serie $\sum b_n$ converge, es decir, $B_N\to B<+\infty$. La sucesión $(B_N)$ es no decreciente, por lo que $B_N\le B$ y $A_N\le B_N\le B$ para todo $N$. La sucesión no decreciente $(A_N)$ está acotada superiormente; en consecuencia, existe el límite finito $\lim_{N\to\infty}A_N\le B<+\infty$, es decir, la serie $\sum a_n$ converge.
2. La afirmación 2 equivale a la afirmación 1 (es su contrarrecíproca): si la serie $\sum b_n$ convergiera, por el punto 1 también convergería la serie $\sum a_n$. $\square$


### Segundo criterio de comparación

Sean dadas dos series positivas $\sum_{n=1}^{\infty}a_n$ y $\sum_{n=1}^{\infty}b_n$, con $b_n>0$ para todo $n$. Si existe el límite $\lim_{n\to\infty}\frac{a_n}{b_n}=:L$ (finito o igual a $+\infty$), entonces:

1. si $L<+\infty$, es decir, $L\in[0,+\infty)$, de la convergencia de la serie $\sum_{n=1}^{\infty}b_n$ se deduce la convergencia de la serie $\sum_{n=1}^{\infty}a_n$;
2. si $L>0$, es decir, $L\in(0,+\infty]$, de la convergencia de la serie $\sum_{n=1}^{\infty}a_n$ se deduce la convergencia de la serie $\sum_{n=1}^{\infty}b_n$.

**Observación.** Si $L\in(0,+\infty)$, las series $\sum_{n=1}^{\infty}a_n$ y $\sum_{n=1}^{\infty}b_n$ convergen y divergen simultáneamente.

**Demostración.**

1. Como $\frac{a_n}{b_n}\to L<+\infty$, la sucesión $\left(\frac{a_n}{b_n}\right)$ está acotada: existe $M$ tal que $\frac{a_n}{b_n}\le M$, es decir, $a_n\le Mb_n$, para todo $n$. Si la serie $\sum b_n$ converge, también converge la serie $\sum Mb_n$, y entonces, por el primer criterio de comparación, converge la serie $\sum a_n$.
2. Como $\frac{a_n}{b_n}\to L>0$, a partir de cierto índice $K$ se tiene $a_n\ge cb_n$ con una constante $c>0$ (puede tomarse $c=L/2$ para $L<+\infty$ y $c=1$ para $L=+\infty$). Así, para $n>K$ se tiene $a_n\ge cb_n>0$ y $b_n\le\frac1c\,a_n$. Es el punto 1 con los papeles de $a_n$ y $b_n$ intercambiados: por el primer criterio de comparación, aplicado a los términos de índices $n>K$ (suprimir un número finito de términos no afecta a la convergencia), de la convergencia de $\sum a_n$ se deduce la convergencia de $\sum b_n$. $\square$


### Criterio de d'Alembert

Criterio de convergencia de d'Alembert. Sean $\sum_{n=1}^{\infty}a_n$ una serie de términos positivos ($a_n>0$) y supongamos que existe el límite $\lim_{n\to\infty}\frac{a_{n+1}}{a_n}=:D$. Entonces:

1. si $D<1$, la serie $\sum_{n=1}^{\infty}a_n$ converge;
2. si $D>1$, la serie $\sum_{n=1}^{\infty}a_n$ diverge;
3. si $D=1$ o el límite $D$ no existe, hace falta seguir estudiando la serie con otros medios.

En el margen de los apuntes se señala que el caso «el límite no existe» es aparte: el criterio en esta forma no afirma entonces nada.

**Demostración.**

1. Sea $D<1$; pongamos $q:=\frac{1+D}{2}$. Por la definición de límite, para todo $\varepsilon>0$ a partir de cierto índice se cumple $\left|\frac{a_{n+1}}{a_n}-D\right|<\varepsilon$. Tomemos $\varepsilon:=\frac{1-D}{2}>0$; existe $N$ tal que para todo $n\ge N$
$$
\frac{a_{n+1}}{a_n}<D+\varepsilon=D+\frac{1-D}{2}=\frac{1+D}{2}=q .
$$
Como $0\le D<1$, se tiene $q\in\left[\tfrac12,1\right)$.

> [!info] Corrección de la fuente
> (S101). En los apuntes: «$q\in(1/2;1)$». Para $D=0$ se obtiene $q=\frac12$, por lo que $q\in\left[\frac12,1\right)$; en la demostración solo importa que $q<1$.

Así, $a_{n+1}<qa_n$ para todo $n\ge N$, de donde por [[es/01-logic-sets-functions#^example-induction|inducción]] $a_n\le q^{\,n-N}a_N$ para todo $n\ge N$. Comparemos las series $\sum_n a_n$ y $\sum_n q^{\,n-N}a_N=a_Nq^{-N}\sum_n q^n$: la última converge por ser una progresión geométrica de razón $q\in(0,1)$. Por el primer criterio de comparación (aplicado a los términos de índices $n\ge N$) la serie $\sum_{n=1}^{\infty}a_n$ converge.

2. Sea $D>1$. Entonces existe $M$ tal que $\frac{a_{n+1}}{a_n}>1$, es decir, $a_{n+1}>a_n$, para todo $n\ge M$. En consecuencia, $a_n\ge a_M>0$ para todo $n\ge M$, por lo que $a_n\not\to0$, y la serie $\sum_{n=1}^{\infty}a_n$ diverge por la condición necesaria de convergencia.

3. Para $D=1$ son posibles ambos casos. La serie $\sum_{k=1}^{\infty}\frac1{k^2}$ converge, y $\frac{a_{k+1}}{a_k}=\frac{k^2}{(k+1)^2}\to1$; la serie $\sum_{k=1}^{\infty}\frac1k$ diverge, y $\frac{a_{k+1}}{a_k}=\frac{k}{k+1}\to1$. $\square$

> [!info] Corrección de la fuente
> (T505). En los apuntes, de la desigualdad $a_{n+1}<qa_n$, conocida para $n>N$, se deduce «$a_n<q^{n-N}a_N$ $\forall n>N$» (para ello hace falta además el paso $n=N$); en el punto 2 se escribe de modo análogo «$a_n>a_M>0$ para $n>M$», y en la línea «$a_{n+1}<qa_n$ $\forall q\in(1/2,1)$» sobra un [[es/01-logic-sets-functions#1.1 Proposiciones y cuantificadores|cuantificador]] sobre $q$ (el número $q$ está fijo). Los índices $N$ y $M$ se eligen de modo que las desigualdades se cumplan para $n\ge N$ (respectivamente $n\ge M$); esto siempre es posible y las conclusiones no cambian.

### Criterio de Cauchy

> [!note] Restaurado
> (según las diapositivas del curso 2024/25, FS p55; los apuntes de 2022, M3S p47). El enunciado del criterio de Cauchy y el comienzo de su demostración se perdieron en el cuaderno (entre las págs. p025 y p026); se conservaron el final del punto 2 y el punto 3 de la demostración.
>
> *Criterio de convergencia de Cauchy.* Sean $\sum_{n=1}^{\infty}a_n$ una serie de términos positivos ($a_n>0$) y supongamos que existe el límite $\lim_{n\to\infty}\sqrt[n]{a_n}=:C$. Entonces:
>
> 1. si $C<1$, la serie $\sum_{n=1}^{\infty}a_n$ converge;
> 2. si $C>1$, la serie $\sum_{n=1}^{\infty}a_n$ diverge;
> 3. si $C=1$ o el límite $C$ no existe, hace falta seguir estudiando la serie con otros medios.
>
> **Demostración.**
>
> 1. Sea $C<1$. Tomemos $\varepsilon:=\frac{1-C}{2}>0$; existe $N$ tal que para todo $n>N$ se cumple $\sqrt[n]{a_n}-C<\varepsilon$, es decir, $\sqrt[n]{a_n}<C+\varepsilon=\frac{1+C}{2}=:q$, donde $q\in(0,1)$. Entonces $a_n<q^n$ para $n>N$; la serie $\sum q^n$ converge (progresión geométrica), y por el primer criterio de comparación la serie $\sum a_n$ converge.
> 2. Sea $C>1$. Entonces existe $M$ tal que $\sqrt[n]{a_n}>1$, es decir, $a_n>1$, para todo $n>M$. En consecuencia, $a_n\not\to0$ para $n\to\infty$.


Por tanto, la serie $\sum_{n=1}^{\infty}a_n$ diverge por la condición necesaria de convergencia. ^p026

3. La serie $\sum_{n=1}^{\infty}\frac1{n^2}$ converge, la serie $\sum_{n=1}^{\infty}\frac1n$ diverge, pero para ambas series $\lim_{n\to\infty}\sqrt[n]{a_n}=1$:
$$
\sqrt[n]{\frac1{n^2}}=\frac1{\left(\sqrt[n]{n}\right)^2}\to1,\qquad \sqrt[n]{\frac1n}=\frac1{\sqrt[n]{n}}\to1,
$$
ya que $\sqrt[n]{n}\to1$. Por tanto, para $C=1$ el criterio no permite concluir nada. $\square$

> [!info] Corrección de la fuente
> (T105). En la segunda línea del punto 3 los apuntes dicen «$\sum1/n$ — div., $\sum1/n^2$ — conv.», es decir, para la serie divergente no se indica el límite de la raíz. De acuerdo con el ejemplo (y con la nota del profesor, FS p55) hay que señalar que también para $\sum\frac1n$ se cumple $\lim\sqrt[n]{1/n}=1$; añadido.

### Lema de Cauchy

Sea $a_n\ge a_{n+1}\ge0$ para todo $n$. Entonces la serie $\sum_{n=1}^{\infty}a_n$ converge si y solo si converge la serie $\sum_{n=1}^{\infty}2^na_{2^n}$.

**Idea de la demostración.** Cada uno de los términos $a_1,a_2,\dots,a_{2^n}$ es al menos $a_{2^n}$, por lo que la suma de $2^n$ términos $a_{2^n}$ se estima así:
$$
2^na_{2^n}=\underbrace{a_{2^n}+a_{2^n}+\dots+a_{2^n}}_{2^n}\le a_1+a_2+\dots+a_{2^n-1}+a_{2^n}.
$$

> [!info] Corrección de la fuente
> (S108). En la transcripción del cuaderno el miembro derecho está escrito como «$a_{2^n}+a_{2^n+1}+\ldots+a_{2^{n+1}}+a_1$». En esta forma la estimación es falsa: los términos de índice mayor que $2^n$ no superan $a_{2^n}$ (por ejemplo, para $a_k=1$ con $k\le2^n$ y $a_k=0$ para $k>2^n$ el miembro derecho vale $2$, mientras que el izquierdo es $2^n>2$ para $n\ge2$). Corregido según las notas del profesor (FS p56, M3S p49).

> [!note] Restaurado
> (según la demostración estándar, cf. Zorich/Fichtenholz; en la diapositiva de 2024/25 el profesor dejó la demostración como ejercicio: «Completar la demostración»).
>
> **Demostración.** Denotemos $S_N=\sum_{n=1}^{N}a_n$ y $T_m=\sum_{k=1}^{m}2^ka_{2^k}$. Dividamos los términos de la serie en bloques. El bloque de índices $2^{k-1}+1,\dots,2^k$ ($k\ge1$) contiene exactamente $2^{k-1}$ términos, cada uno al menos $a_{2^k}$; el bloque de índices $2^k,\dots,2^{k+1}-1$ ($k\ge0$) contiene exactamente $2^k$ términos, cada uno a lo sumo $a_{2^k}$. Por tanto,
> $$
> 2^{k-1}a_{2^k}\le a_{2^{k-1}+1}+\dots+a_{2^k},\qquad a_{2^k}+\dots+a_{2^{k+1}-1}\le2^ka_{2^k}.
> $$
> Sumando la primera desigualdad sobre $k=1,\dots,m$ y la segunda sobre $k=0,\dots,m$, obtenemos
> $$
> \tfrac12\,T_m\le S_{2^m}-a_1\le S_{2^m},\qquad S_{2^{m+1}-1}\le a_1+T_m .
> $$
> Si la serie $\sum a_n$ converge a $S$, entonces $T_m\le2S_{2^m}\le2S$ para todo $m$: las sumas parciales de la serie positiva $\sum2^ka_{2^k}$ están acotadas y, por la propiedad 2 de las series positivas, converge. Recíprocamente, si la serie $\sum2^ka_{2^k}$ converge a $T$, entonces $S_{2^{m+1}-1}\le a_1+T$ para todo $m$; por la observación a las propiedades de las series positivas (basta la acotación de una subsucesión de sumas parciales) la sucesión $(S_N)$ está acotada, y la serie $\sum a_n$ converge. $\square$
>
> **Ejemplo.** Sean $p>0$ y $a_n=\frac1{n^p}$. Entonces $2^na_{2^n}=\left(2^{1-p}\right)^n$, y la serie $\sum2^na_{2^n}$ es una progresión geométrica de razón $2^{1-p}$; converge para $p>1$ y diverge para $p\le1$. Por el lema de Cauchy la serie $\sum_{n=1}^{\infty}\frac1{n^p}$ converge para $p>1$ y diverge para $0<p\le1$ (para $p\le0$ diverge, ya que $\frac1{n^p}\not\to0$). En particular, la serie $\sum\frac1{n^2}$ converge y $\sum\frac1n$ diverge; estos hechos se usan en los ejemplos de los criterios de d'Alembert y de Cauchy.

## §7.4. Series de términos de signo arbitrario

> [!definition] Definición 7.4.1
> Si la serie $\sum_{n=1}^{\infty}a_n$ converge, mientras que la serie correspondiente $\sum_{n=1}^{\infty}|a_n|$ diverge, la serie original $\sum_{n=1}^{\infty}a_n$ se llama condicionalmente convergente.

^def-7-4-1


Consideremos ahora series de la forma $\sum_{n=0}^{\infty}(-1)^nc_n$, $c_n\ge0$, cuyos términos cambian de signo alternadamente. Tales series se suelen llamar alternadas. ^p027

### Criterio de Leibniz

Sea $c_n>0$ para todo $n$ y $c_n\downarrow0$, es decir, $c_{n+1}\le c_n$ para todo $n$ y $c_n\to0$ cuando $n\to\infty$. Entonces la serie $\sum_{n=0}^{\infty}(-1)^nc_n$ converge. Además, para el resto de la serie $R_n:=\sum_{k=n+1}^{\infty}(-1)^kc_k$ se cumple la estimación $|R_n|\le c_{n+1}$.

**Ejemplo.** $1-\frac12+\frac13-\frac14+\dots+\frac{(-1)^{n+1}}{n}+\dots=\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}=\ln2$ (la suma se calcula más abajo).

**Demostración.** Denotemos $S_n=\sum_{k=0}^{n}(-1)^kc_k$ y consideremos las sumas parciales de índice impar. Son no decrecientes:
$$
S_{2m+1}-S_{2m-1}=\sum_{n=0}^{2m+1}(-1)^nc_n-\sum_{n=0}^{2m-1}(-1)^nc_n=c_{2m}-c_{2m+1}\ge0 .
$$
Están acotadas superiormente por el número $c_0$:
$$
S_{2m+1}=c_0-c_1+c_2-c_3+\dots+c_{2m}-c_{2m+1}=c_0+(c_2-c_1)+(c_4-c_3)+\dots+(c_{2m}-c_{2m-1})-c_{2m+1}\le c_0,
$$
ya que cada paréntesis es no positivo ($c_{n+1}\le c_n$) y $-c_{2m+1}\le0$.

> [!info] Corrección de la fuente
> (M504). En los apuntes: «$\ldots=c_0+(c_2-c_1)+(c_4-c_3)+\ldots+(c_{2m}-c_{2m+1})\le c_0$». Con esta agrupación el último paréntesis es $(c_{2m}-c_{2m-1})$, y el término $-c_{2m+1}$ queda aparte (así en las notas del profesor: M3S p51, FS p57); además, el paréntesis $(c_{2m}-c_{2m+1})$ es no negativo, y no $\le0$ como se indica en el margen.

> [!note] Restaurado
> (según las diapositivas del curso 2024/25, FS p57; los apuntes de 2022, M3S p52). Conclusión de la demostración. La sucesión no decreciente y acotada superiormente $(S_{2m+1})$ tiene límite finito por el teorema del límite de una sucesión monótona: $S_{2m+1}\to S$ cuando $m\to\infty$. Además, $S_{2m+2}=S_{2m+1}+c_{2m+2}\to S$, ya que $c_n\to0$. Las sumas parciales de índice par y de índice impar tienden al mismo número $S$, por lo que $S_n\to S$, es decir, la serie $\sum_{n=0}^{\infty}(-1)^nc_n$ converge. La estimación del resto se demuestra más abajo, en la observación 2. $\square$

**Observación 1.** Agrupando los términos de otro modo, obtenemos
$$
S_{2m+1}=(c_0-c_1)+(c_2-c_3)+\dots+(c_{2m}-c_{2m+1})\ge0,
$$
ya que cada paréntesis es no negativo. Junto con la estimación $S_{2m+1}\le c_0$ esto da $0\le S_{2m+1}\le c_0$. Pasando al límite en las desigualdades cuando $m\to\infty$ (el límite existe por el teorema del límite de una sucesión monótona), obtenemos $0\le S\le c_0$: la suma de una serie de Leibniz está entre cero y su primer término.

**Observación 2.** Estimemos el resto de la serie de Leibniz $R_n=\sum_{k=n+1}^{\infty}(-1)^kc_k$.


Tenemos
$$
|R_n|=|S-S_n|=\bigl|(-1)^{n+1}(S-S_n)\bigr|\le c_{n+1}.
$$

^p028

> [!note] Restaurado
> (según la demostración estándar). Justificación de la última desigualdad: $(-1)^{n+1}R_n=\sum_{j=0}^{\infty}(-1)^jc_{n+1+j}=c_{n+1}-c_{n+2}+c_{n+3}-\dots$ es una serie del mismo tipo con términos $c_{n+1}\ge c_{n+2}\ge\dots\to0$ y primer término $c_{n+1}$. Por la observación 1 su suma está en el segmento $[0,c_{n+1}]$, es decir, $0\le(-1)^{n+1}(S-S_n)\le c_{n+1}$.

**Ejemplo.** Calculemos la suma de la serie $\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{k}=1-\frac12+\frac13-\frac14+\dots$ (converge por el criterio de Leibniz). Escribamos cada término negativo en la forma $-\frac1{2k}=\frac1{2k}-2\cdot\frac1{2k}$ (por ejemplo, $-\frac12=\frac12-2\cdot\frac12$, $-\frac14=\frac14-2\cdot\frac14$); entonces, para una suma parcial de índice par,
$$
S_{2n}=1-\frac12+\dots+\frac1{2n-1}-\frac1{2n}=1+\frac12+\frac13+\dots+\frac1{2n-1}+\frac1{2n}-2\left(\frac12+\frac14+\dots+\frac1{2n}\right).
$$
Pongamos $H_n=1+\frac12+\dots+\frac1n$. Entonces $H_{2n}=1+\frac12+\dots+\frac1{2n-1}+\frac1{2n}$ y $2\left(\frac12+\frac14+\dots+\frac1{2n}\right)=H_n$, es decir,
$$
S_{2n}=H_{2n}-H_n .
$$
Por la fórmula de Euler–Maclaurin para la asintótica de sumas
$$
H_n=\ln n+C_0+\delta_n,\qquad \delta_n\to0,
$$
donde $C_0=\gamma\approx0{,}5772$ es la constante de Euler.

> [!note] Restaurado
> (en los apuntes el cálculo se interrumpe en esta fórmula; completado con el razonamiento estándar). Sustituyendo, obtenemos
> $$
> S_{2n}=H_{2n}-H_n=\bigl(\ln(2n)+C_0+\delta_{2n}\bigr)-\bigl(\ln n+C_0+\delta_n\bigr)=\ln2+\delta_{2n}-\delta_n\xrightarrow[n\to\infty]{}\ln2,
> $$
> y $S_{2n+1}=S_{2n}+\frac1{2n+1}\to\ln2$. En consecuencia, $S_n\to\ln2$, es decir,
> $$
> \sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{k}=\ln2 .
> $$
> Sin la constante de Euler puede razonarse así: $H_{2n}-H_n=\sum_{j=1}^{n}\frac1{n+j}=\frac1n\sum_{j=1}^{n}\frac1{1+j/n}$ es una [[es/lectures-2025-26/lecture-37-38#^def-4-2-4|suma integral]] de la función $\frac1{1+x}$ en $[0,1]$ para la partición en $n$ partes iguales, por lo que $H_{2n}-H_n\to\int_0^1\frac{dx}{1+x}=\ln2$.

### Transformación de Abel. Criterios de Dirichlet y de Abel

> [!note] Restaurado
> (según las diapositivas del curso 2024/25, FS p58–p59; los apuntes de 2022, M3S p53–p56). Entre las págs. p028 y p029 el cuaderno perdió la transformación de Abel, el criterio de Dirichlet con su demostración y el enunciado del criterio de Abel; en la pág. p029 se conservó la demostración del criterio de Abel. Los enunciados siguen las diapositivas del profesor; las demostraciones, las notas a ellas.
>
> *Transformación de Abel.* Sean $(a_k)$ y $(b_k)$ sucesiones numéricas, $B_k=b_1+b_2+\dots+b_k$, $B_0:=0$. Entonces, para $m>n\ge0$
> $$
> \sum_{k=n+1}^{m}a_kb_k=a_mB_m-a_{n+1}B_n+\sum_{k=n+1}^{m-1}(a_k-a_{k+1})B_k .
> $$
>
> **Demostración.** Como $b_k=B_k-B_{k-1}$,
> $$
> \begin{aligned}
> \sum_{k=n+1}^{m}a_kb_k&=a_{n+1}(B_{n+1}-B_n)+a_{n+2}(B_{n+2}-B_{n+1})+\dots+a_m(B_m-B_{m-1})\\
> &=-a_{n+1}B_n+(a_{n+1}-a_{n+2})B_{n+1}+\dots+(a_{m-1}-a_m)B_{m-1}+a_mB_m ,
> \end{aligned}
> $$
> como se quería. $\square$
>
> *Criterio de convergencia de Dirichlet.* Supongamos que se cumplen las condiciones:
>
> 1. $a_n\downarrow0$, es decir, $a_{n+1}\le a_n$ para todo $n$ y $a_n\to0$;
> 2. existe $M$ tal que $|B_n|=|b_1+\dots+b_n|\le M$ para todo $n$.
>
> Entonces la serie $\sum_{n=1}^{\infty}a_nb_n$ converge.
>
> **Demostración.** Usemos el criterio de Bolzano–Cauchy de convergencia de una serie: la serie $\sum d_k$ converge si y solo si para todo $\varepsilon>0$ existe $N$ tal que $\bigl|\sum_{k=n+1}^{n+p}d_k\bigr|<\varepsilon$ para todos $n>N$ y $p\in\mathbb N$. Pongamos $d_k=a_kb_k$, $m=n+p$. Por la transformación de Abel, la condición 2 y la condición 1 (de la que se deducen $a_k\ge0$ y $a_k-a_{k+1}\ge0$)
> $$
> \begin{aligned}
> \Bigl|\sum_{k=n+1}^{m}a_kb_k\Bigr|&\le|a_m|\,|B_m|+|a_{n+1}|\,|B_n|+\sum_{k=n+1}^{m-1}|a_k-a_{k+1}|\,|B_k|\\
> &\le M\Bigl(a_m+a_{n+1}+\sum_{k=n+1}^{m-1}(a_k-a_{k+1})\Bigr)=M\bigl(a_m+a_{n+1}+a_{n+1}-a_m\bigr)=2Ma_{n+1},
> \end{aligned}
> $$
> ya que $\sum_{k=n+1}^{m-1}(a_k-a_{k+1})=(a_{n+1}-a_{n+2})+\dots+(a_{m-1}-a_m)=a_{n+1}-a_m$. Como $a_n\to0$, para todo $\varepsilon>0$ existe $N$ tal que $2Ma_{n+1}<\varepsilon$ para todo $n>N$. Se cumple el criterio de Bolzano–Cauchy, y la serie $\sum a_nb_n$ converge. $\square$
>
> *Criterio de convergencia de Abel.* Supongamos que se cumplen las condiciones:
>
> 1. la sucesión $(a_n)$ está acotada y es monótona;
> 2. la serie $\sum_{n=1}^{\infty}b_n$ converge.
>
> Entonces la serie $\sum_{n=1}^{\infty}a_nb_n$ converge.


**Demostración del criterio de Abel.** Por hipótesis la sucesión $(a_n)$ está acotada y es monótona. Para fijar ideas, sea no creciente ($a_1\ge a_2\ge a_3\ge\dots\ge a_n\ge\dots$) y acotada inferiormente. Entonces, por el teorema del límite de una sucesión monótona, existe el límite finito $\lim_{n\to\infty}a_n=a$. Pongamos $\alpha_n:=a_n-a$; entonces $\alpha_n\downarrow0$. Las series $\sum_{n=1}^{\infty}\alpha_nb_n$ y $a\sum_{n=1}^{\infty}b_n$ convergen: la primera por el criterio de Dirichlet ($\alpha_n\downarrow0$, y las sumas parciales de la serie convergente $\sum b_n$ están acotadas), la segunda por hipótesis. Por tanto, converge también la serie
$$
\sum_{n=1}^{\infty}a_nb_n=\sum_{n=1}^{\infty}(\alpha_n+a)b_n=\sum_{n=1}^{\infty}\alpha_nb_n+a\sum_{n=1}^{\infty}b_n .
$$
Si $(a_n)$ es no decreciente y acotada superiormente, el razonamiento es el mismo con $\alpha_n:=a-a_n\downarrow0$ y $a_nb_n=ab_n-\alpha_nb_n$. $\square$ ^p029

## §7.5. Reordenaciones de series

> [!definition] Definición 7.5.1
> Sean dadas una serie $\sum_{n=1}^{\infty}a_n$ y una aplicación biyectiva $\sigma:\mathbb N\to\mathbb N$. La serie $\sum_{n=1}^{\infty}a_{\sigma(n)}$ se llama reordenación de la serie original $\sum_{n=1}^{\infty}a_n$.

^def-7-5-1

### Propiedad conmutativa de una serie

> [!definition] Definición 7.5.2
> Diremos que una serie $\sum_{n=1}^{\infty}a_n$ tiene la propiedad conmutativa si para toda biyección $\sigma:\mathbb N\to\mathbb N$ la serie $\sum_{n=1}^{\infty}a_{\sigma(n)}$ converge y diverge a la vez que la serie original y, además,
> $$
> \sum_{n=1}^{\infty}a_n=\sum_{n=1}^{\infty}a_{\sigma(n)} .
> $$

^def-7-5-2

Un ejemplo de reordenación que cambia la suma de una serie y las propiedades conmutativas de las series se ven al comienzo de la clase siguiente (lecciones 71–72).

## Referencias cruzadas

- Tema en el curso: [[es/04-numeric-series|capítulo 4 «Series numéricas»]] — [[es/04-numeric-series#4.2 Términos no negativos|§4.2 «Series de términos de signo constante»]], [[es/04-numeric-series#4.3 Convergencia absoluta y condicional|§4.3 «Convergencia absoluta y condicional»]], [[es/04-numeric-series#^alternating-series-test|criterio de Leibniz]], [[es/04-numeric-series#^rearrangement-warning|reordenaciones de los términos de una serie]].
- Comienzo del capítulo 7 (serie numérica, propiedades de las series, criterio de Bolzano–Cauchy para series, convergencia absoluta): [[es/lectures-2025-26/lecture-67-68|lecciones 67–68]].
- Hechos usados: [[es/lectures-2025-26/lecture-11-12#^thm-2-3-3|teorema 2.3.3]] sobre el límite de una sucesión monótona; [[es/lectures-2025-26/lecture-13#^thm-2-3-7|teorema 2.3.7]], el criterio de Bolzano–Cauchy para sucesiones.
- Los criterios de Dirichlet y de Abel para [[es/lectures-2025-26/lecture-47-48#^def-4-5-2|integrales impropias]]: [[es/lectures-2025-26/lecture-49-50#^thm-4-5-4|teorema 4.5.4]] (lecciones 49–50).
- Continuación: un ejemplo de reordenación de una serie y las propiedades conmutativas — [[es/lectures-2025-26/lecture-71-72|lecciones 71–72]].

---

[[es/lectures-2025-26/lecture-67-68|← Lecciones 67–68]] · [[es/lectures-2025-26/index|Índice de lecciones]] · [[es/lectures-2025-26/lecture-71-72|Lecciones 71–72 →]] · [[es/term-index|Términos y teoremas]] · [[ru/lectures-2025-26/lecture-69-70|Русский]] · [[en/lectures-2025-26/lecture-69-70|English]]
