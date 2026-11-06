---
title: "Lecciones 81–82 — criterio de Lebesgue, sumas de Darboux, integral sobre un conjunto, medida de Jordan, propiedades generales de la integral"
lang: es
course: "Análisis matemático, 2025/26"
lecture: 81-82
semester: 3
source: "cuaderno manuscrito, págs. p074–p082"
source_pages: "p074, p075, p076, p077, p078, p079, p080, p081, p082"
course_chapter: 26
---
# Lecciones 81–82 — criterio de Lebesgue, sumas de Darboux, integral sobre un conjunto, medida de Jordan, propiedades generales de la integral

[← Lecciones 79–80](lecture-79-80.md) · [Índice de lecciones](index.md) · [Lecciones 83–84 →](lecture-83-84.md) · [Términos y teoremas](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-81-82.md) · [English](../../en/lectures-2025-26/lecture-81-82.md)

> **Fuente y numeración.** Los apuntes se copiaron de un cuaderno manuscrito (págs. p074–p082; el texto bruto de las páginas está en [`ocr/raw/`](../../../ocr/raw/p074.md)). La pág. p074 comienza con la demostración del [teorema 10.1.1](lecture-79-80.md#thm-10-1-1), enunciado al final de las lecciones 79–80; tras ella, en el margen, figura la nota en un recuadro «20 de octubre» (al parecer, la fecha de la clase; las lecciones 79–80 están fechadas el 22 de octubre en el cuaderno, así que probablemente debe leerse «29 de octubre») y, en rojo, el título «Lecciones 81–82» con el plan de la clase: [criterio de Lebesgue](lecture-41-42.md#thm-4-2-5); [sumas de Darboux](lecture-39-40.md#def-4-2-8); [integral de Riemann](lecture-39-40.md#def-4-2-6) sobre un conjunto; [medida de Jordan](#def-10-2-5); propiedades de la integral; [teorema de Fubini](../17-multiple-integrals.md#fubini-theorem-continuous) y sus corolarios; [principio de Cavalieri](lecture-83-84.md#thm-10-4-2) (los dos últimos puntos se ven en las lecciones 83–84). Las fotografías de las págs. p078–p081, a juzgar por su contenido, se tomaron por pares en orden inverso (por el sentido, la anotación sigue el orden p079, p078, p081, p080). El texto de abajo sigue la numeración de las páginas, pero la observación sobre la independencia de la integral respecto de la elección del paralelepípedo (comenzada al final de la pág. p078 y continuada al principio de la pág. p081) se reproduce completa justo después de la [definición 10.2.4](#def-10-2-4), y la demostración del [teorema 10.2.1](#thm-10-2-1) (comienzo de la pág. p080), tras su enunciado (final de la pág. p081); las sumas de Darboux (pág. p079, numeración de §10.1) se dejan en su lugar, aunque en las diapositivas de 2024/25 van antes de §10.2. Las [definiciones 10.1.9](#def-10-1-9), [10.1.10](#def-10-1-10), [10.2.3](#def-10-2-3), [10.2.4](#def-10-2-4) y el [teorema 10.2.1](#thm-10-2-1) están sin terminar en el cuaderno («// complet.») y se restauran a partir de las diapositivas del curso 2024/25 (FS p93, p95). La numeración de definiciones y teoremas es la del profesor. Los lapsus de los apuntes se corrigen y se marcan con bloques «Corrección de la fuente»; los pasajes perdidos se restauran y se marcan con bloques «Restaurado»; las etiquetas corresponden a [`ocr/RESOLVED.md`](../../../ocr/RESOLVED.md). Los lugares que aún hay que cotejar con el cuaderno se enumeran en [`ocr/ISSUES.md`](../../../ocr/ISSUES.md).

## §10.1. Integral de Riemann sobre un paralelepípedo n-dimensional (continuación)

<a id="p074"></a>

Recordemos el [teorema 10.1.1](lecture-79-80.md#thm-10-1-1) (condición necesaria de integrabilidad), enunciado al final de las lecciones 79–80: si $`f\in R(I)`$, entonces $`f`$ está acotada en el paralelepípedo $`I`$. Su demostración está escrita al comienzo de la pág. p074.

**Demostración del [teorema 10.1.1](lecture-79-80.md#thm-10-1-1).** Probemos que si $`f`$ no está acotada en $`I`$, entonces $`f\notin R(I)`$. Sea $`P`$ cierta [partición](lecture-79-80.md#def-10-1-3) de $`I`$. El paralelepípedo $`I`$ es la unión de un número finito de paralelepípedos de la partición, por lo que existe un paralelepípedo $`I_{i_0}\in P`$ en el que $`f`$ no está acotada.

*Figura de los apuntes (pág. p074): el paralelepípedo $`I`$ con la malla de la partición, en la que se destaca el paralelepípedo $`I_{i_0}`$.*

Sean $`\xi'`$ y $`\xi''`$ dos conjuntos de puntos marcados para $`P`$ que (para simplificar) solo difieren en la elección del punto en $`I_{i_0}`$: en $`I_{i_0}`$ se marcan los puntos $`\xi'_{i_0}`$ y $`\xi''_{i_0}`$ respectivamente. Entonces
```math
|\sigma(f,P,\xi')-\sigma(f,P,\xi'')|=|f(\xi'_{i_0})-f(\xi''_{i_0})|\cdot\mu(I_{i_0}).
```
Fijemos $`\xi'_{i_0}`$ y movamos el punto $`\xi''_{i_0}`$ por $`I_{i_0}`$. Como $`f`$ no está acotada en $`I_{i_0}`$, la diferencia $`|f(\xi'_{i_0})-f(\xi''_{i_0})|`$ puede hacerse arbitrariamente grande, y $`\mu(I_{i_0})>0`$; por tanto, la diferencia de las [sumas integrales](lecture-37-38.md#def-4-2-4) puede hacerse, por ejemplo, mayor que $`1`$. Esto vale para toda partición $`P`$, incluidas las arbitrariamente finas, y por el criterio de Cauchy el límite de las sumas integrales cuando $`\lambda(P)\to0`$ no existe, es decir, $`f\notin R(I)`$. $`\square`$

### Criterio de Lebesgue de integrabilidad según Riemann

> **Restaurado** (la definición no figura ni en los apuntes ni en las diapositivas de 2024/25; se da por analogía con la [definición 4.2.11](lecture-41-42.md#def-4-2-11) unidimensional de las lecciones 41–42). Un conjunto $`E\subset\mathbb R^n`$ se llama *conjunto de medida nula* (según Lebesgue) si para todo $`\varepsilon>0`$ puede cubrirse con un sistema finito o [numerable](lecture-01-02.md#def-1-2-5) de paralelepípedos $`I_1,I_2,\dots`$ con suma de medidas $`\sum_k\mu(I_k)<\varepsilon`$. Se escribe $`\mu(E)=0`$; la notación $`\mu(E)\ne0`$ significa que $`E`$ no es un conjunto de medida nula. Los paralelepípedos del recubrimiento pueden tomarse cerrados o abiertos: cada paralelepípedo $`I_k`$ está contenido en un paralelepípedo abierto de medida menor que $`\mu(I_k)+\varepsilon/2^k`$, así que la noción no cambia.

<a id="def-10-1-8"></a>**Definición 10.1.8.** Diremos que cierta propiedad se cumple en casi todo punto del conjunto $`M`$ si el subconjunto de $`M`$ donde esta propiedad puede fallar tiene medida nula.

<a id="p075"></a>

<a id="thm-10-1-2"></a>**Teorema 10.1.2 (criterio de Lebesgue).** Una función $`f:I\to\mathbb R`$ es integrable según Riemann en el paralelepípedo $`I`$, es decir, $`f\in R(I)`$, si y solo si $`f`$ está acotada en $`I`$ y es continua en casi todo punto de $`I`$.

> **Corrección de la fuente** (T374). En los apuntes: «$`f\in R(I)\Leftrightarrow f`$ integr. [en casi todo punto](../19-measure-theory.md#sec-19-4) de $`I`$». Corregido según la diapositiva FS p92: la condición del criterio es la acotación de $`f`$ en $`I`$ y la continuidad en casi todo punto de $`I`$ (cf. el criterio de Lebesgue unidimensional, [teorema 4.2.5](lecture-41-42.md#thm-4-2-5)); las palabras «integrable en casi todo punto» aquí carecen de sentido.

**Observación (sobre los conjuntos de medida nula).**

① Un punto (o un número finito de puntos) tiene medida nula. Por ejemplo, para $`n=2`$ el punto $`a=(a_1,a_2)`$ es el paralelepípedo degenerado $`I_{a,a}`$; puede cubrirse con el rectángulo $`(a_1-\delta,a_1+\delta)\times(a_2-\delta,a_2+\delta)`$ de área $`4\delta^2`$, arbitrariamente pequeña para $`\delta`$ pequeño.

② En $`\mathbb R^2`$ una curva suave (o un número finito de curvas suaves) tiene medida nula.

③ En $`\mathbb R^3`$ una superficie suave (o un número finito de superficies suaves) tiene medida nula.

> **Corrección de la fuente** (U376, U377). En los apuntes los puntos ② y ③ se escriben para curvas y superficies arbitrarias («Superf-e» en el punto ③ es «superficie»), y bajo el punto ③, en rojo en el margen, figura una aclaración ilegible «en el sentido de s…», al parecer sobre la suavidad. Se ha añadido la palabra «suave»: para curvas y superficies suaves (de clase $`C^1`$) las afirmaciones son ciertas, mientras que para curvas continuas arbitrarias no lo son: la curva de Peano aplica de forma continua un segmento sobre todo el cuadrado.

④ La unión de un número finito o numerable de conjuntos de medida nula es un conjunto de medida nula.

⑤ Todo subconjunto de un conjunto de medida nula tiene medida nula.

⑥ Un paralelepípedo no degenerado $`I_{a,b}=\{x\in\mathbb R^n:\ a_i\le x_i\le b_i\}`$, donde $`a_i<b_i`$ para todo $`i`$, no es un conjunto de medida nula: $`\mu(I_{a,b})\ne0`$.

> **Restaurado** (justificación de las propiedades ①, ④–⑥ según el esquema estándar; en los apuntes y en la diapositiva FS p92 se dan sin demostración). ① Cada uno de los $`m`$ puntos puede cubrirse con un cubo de medida menor que $`\varepsilon/m`$. ④ Si $`\mu(E_k)=0`$, $`k=1,2,\dots`$, entonces $`E_k`$ se cubre con paralelepípedos de suma de medidas menor que $`\varepsilon/2^k`$; todos estos paralelepípedos juntos forman un sistema numerable que cubre $`\bigcup_kE_k`$ con suma de medidas menor que $`\sum_k\varepsilon/2^k=\varepsilon`$. ⑤ Un recubrimiento de un conjunto cubre también cualquier subconjunto suyo. ⑥ Sean $`I=I_{a,b}\subset\bigcup_kI_k`$ y $`\varepsilon>0`$. Sustituyamos cada $`I_k`$ por un paralelepípedo abierto $`J_k\supset I_k`$ con $`\mu(J_k)<\mu(I_k)+\varepsilon/2^k`$. El [compacto](lecture-57-58.md#def-5-3-7) $`I`$ se cubre con un número finito de ellos, digamos $`J_1,\dots,J_N`$, y por la propiedad de la medida de un paralelepípedo (lecciones 79–80) $`\mu(I)\le\sum_{k=1}^N\mu(J_k)<\sum_k\mu(I_k)+\varepsilon`$. Como $`\varepsilon`$ es arbitrario, la suma de medidas de cualquier recubrimiento de $`I`$ es al menos $`\mu(I)=\prod_i(b_i-a_i)>0`$.

**Demostración del [teorema 10.1.2](#thm-10-1-2).** *Necesidad.* Sea $`f\in R(I)`$. Por el [teorema 10.1.1](lecture-79-80.md#thm-10-1-1) $`f`$ está acotada en $`I`$: $`|f|\le M`$ en $`I`$. Comprobemos que $`f`$ es continua en casi todo punto de $`I`$, es decir, que el conjunto $`E`$ de los puntos de discontinuidad de la función $`f`$ en $`I`$ tiene medida nula.

> **Corrección de la fuente** (M380). En los apuntes el objetivo se escribe «probemos que $`E=`$ el conj. de puntos de discontinuidad de la fn $`I\Rightarrow f\in R(I)`$»; por el sentido, se demuestra que $`\mu(E)=0`$ (por reducción al absurdo: de $`\mu(E)\ne0`$ se deduce $`f\notin R(I)`$).

Recordemos la noción de [oscilación](lecture-39-40.md#def-4-2-9). Para una función $`f:I\to\mathbb R`$ y un conjunto $`X\subset I`$, la magnitud
```math
\omega(f,X)=\sup_{x,y\in X}|f(x)-f(y)|
```
se llama oscilación de la función $`f`$ en el conjunto $`X`$, y la magnitud
```math
\omega(f,x)=\lim_{\delta\to0}\omega\bigl(f,V_\delta(x)\bigr),
```
donde $`V_\delta(x)=\{y\in I:\ |y-x|<\delta\}`$ es el $`\delta`$-entorno del punto $`x`$ en $`I`$, se llama oscilación de la función $`f`$ en el punto $`x`$ (el límite existe, ya que $`\omega(f,V_\delta(x))`$ no crece al disminuir $`\delta`$). La función $`f`$ es [continua en el punto](lecture-16.md#def-2-5-1) $`x`$ si y solo si $`\omega(f,x)=0`$.

Consideremos los conjuntos
```math
E_n=\Bigl\{x\in I:\ \omega(f,x)\ge\frac1n\Bigr\},\qquad n\in\mathbb N .
```
Entonces $`E=\bigcup_{n=1}^{\infty}E_n`$. Si $`\mu(E)\ne0`$, por la propiedad ④ existe $`n_0\in\mathbb N`$ tal que $`\mu(E_{n_0})\ne0`$. Probemos que esto contradice la integrabilidad de $`f`$.

Sea $`P`$ una partición arbitraria de $`I`$ en paralelepípedos $`I_i`$. Dividamos los paralelepípedos de la partición en dos grupos:
```math
A=\Bigl\{I_i\in P:\ I_i\cap E_{n_0}\ne\varnothing,\ \ \omega(f,I_i)\ge\frac1{2n_0}\Bigr\},\qquad B=P\setminus A .
```

<a id="p076"></a>

El sistema de paralelepípedos $`A`$ forma un recubrimiento de $`E_{n_0}`$. En efecto, sea $`y\in E_{n_0}`$. Si $`y`$ es un punto interior (respecto de $`I`$) de algún paralelepípedo $`I_i\in P`$, entonces $`I_i\supset V_\delta(y)`$ para $`\delta`$ pequeño, por lo que $`\omega(f,I_i)\ge\omega(f,y)\ge\frac1{n_0}`$, y $`I_i\in A`$. Si $`y`$ está en la frontera de los paralelepípedos de la partición, hace falta un razonamiento, para el cual la definición de $`A`$ tiene el umbral $`\frac1{2n_0}`$ y no $`\frac1{n_0}`$.

> **Restaurado** (según la demostración estándar; en los apuntes el caso de un [punto frontera](lecture-57-58.md#def-5-3-4) se interrumpe: «$`\to y\in`$ frontera $`I_i`$:»). Sean $`I_{i_1},\dots,I_{i_m}`$ todos los paralelepípedos de la partición que contienen $`y`$. Los demás paralelepípedos son cerrados y no contienen $`y`$, por lo que para $`\delta>0`$ pequeño el entorno $`V_\delta(y)`$ está contenido en $`I_{i_1}\cup\dots\cup I_{i_m}`$. Si fuera $`\omega(f,I_{i_s})<\frac1{2n_0}`$ para todo $`s`$, para cualesquiera puntos $`x\in I_{i_s}`$, $`x'\in I_{i_t}`$ de $`V_\delta(y)`$ se tendría
> ```math
> |f(x)-f(x')|\le|f(x)-f(y)|+|f(y)-f(x')|\le\omega(f,I_{i_s})+\omega(f,I_{i_t})\le2\max_{s}\omega(f,I_{i_s}),
> ```
> de donde $`\omega(f,y)\le\omega(f,V_\delta(y))\le2\max_s\omega(f,I_{i_s})<\frac1{n_0}`$, en contradicción con $`y\in E_{n_0}`$. Por tanto, $`\omega(f,I_{i_s})\ge\frac1{2n_0}`$ para algún $`s`$; este paralelepípedo contiene $`y\in E_{n_0}`$ y, en consecuencia, pertenece a $`A`$.

Elijamos dos conjuntos de puntos marcados $`\xi'`$ y $`\xi''`$ de modo que:

1) para $`I_i\in B`$ los puntos marcados coincidan: $`\xi'_i=\xi''_i`$;
2) para $`I_i\in A`$ se cumpla la desigualdad $`f(\xi'_i)-f(\xi''_i)\ge\frac1{3n_0}`$ (es posible, ya que $`\omega(f,I_i)\ge\frac1{2n_0}>\frac1{3n_0}`$).

Entonces
```math
|\sigma(f,P,\xi')-\sigma(f,P,\xi'')|=\sum_{I_i\in A}\bigl(f(\xi'_i)-f(\xi''_i)\bigr)\mu(I_i)\ge\frac1{3n_0}\sum_{I_i\in A}\mu(I_i).
```

> **Corrección de la fuente** (M386). En los apuntes falta en la parte central el factor $`\mu(I_i)`$: «$`=\left|\sum_{I_i\in A}\left(f(\xi'_i)-f(\xi''_i)\right)\right|>\frac1{3n_0}\sum_{I_i\in A}\mu(I_i)`$». La diferencia de las sumas integrales consta de los sumandos $`\bigl(f(\xi'_i)-f(\xi''_i)\bigr)\mu(I_i)`$ sobre los paralelepípedos del grupo $`A`$ (sobre el grupo $`B`$ los sumandos son nulos); todos son no negativos, y cada uno es al menos $`\frac1{3n_0}\mu(I_i)`$.

La suma $`\sum_{I_i\in A}\mu(I_i)`$ está [acotada inferiormente](lecture-05-06.md#def-1-3-7) por una constante positiva que no depende de $`P`$. Se deduce de la hipótesis $`\mu(E_{n_0})\ne0`$ y de que los paralelepípedos de $`A`$ cubren $`E_{n_0}`$: como $`E_{n_0}`$ no es un conjunto de medida nula, existe $`c>0`$ tal que la suma de medidas de cualquier sistema finito o numerable de paralelepípedos que cubra $`E_{n_0}`$ es al menos $`c`$. Por tanto, $`\sum_{I_i\in A}\mu(I_i)\ge c`$ y
```math
|\sigma(f,P,\xi')-\sigma(f,P,\xi'')|\ge\frac{c}{3n_0}.
```
La partición $`P`$ es arbitraria (en particular, arbitrariamente fina), por lo que, por el criterio de Cauchy, las sumas integrales $`\sigma(f,P,\xi)`$ no tienen límite cuando $`\lambda(P)\to0`$, es decir, $`f\notin R(I)`$, lo cual es una contradicción. En consecuencia, $`\mu(E)=0`$.

*Suficiencia.* Sea $`f`$ acotada en $`I`$, $`|f|\le M`$, y continua en casi todo punto de $`I`$, es decir, $`\mu(E)=0`$. Si $`M=0`$, entonces $`f\equiv0`$ y $`f\in R(I)`$; además, $`M>0`$. Fijemos $`\varepsilon>0`$ y pongamos
```math
E_\varepsilon=\{x\in I:\ \omega(f,x)\ge\varepsilon\}.
```
Como $`E_\varepsilon\subset E`$, se tiene $`\mu(E_\varepsilon)=0`$ (propiedad ⑤). El conjunto $`E_\varepsilon`$ es cerrado en $`I`$; al estar acotado, es compacto. Y para los compactos es cierto que de todo recubrimiento por [conjuntos abiertos](lecture-55-56.md#def-5-3-1) puede extraerse un subrecubrimiento finito (observación del profesor en el margen). Por tanto, existe un conjunto finito de paralelepípedos $`I_1,\dots,I_k`$ tal que
```math
E_\varepsilon\subset\bigcup_{i=1}^kI_i,\qquad\sum_{i=1}^k\mu(I_i)<\varepsilon .
```

> **Restaurado** (según la demostración estándar; en los apuntes: «Evidentemente, $`E_\varepsilon`$ es cerrado en $`I\Rightarrow E_\varepsilon`$: ¡compacto!»). *Cerradura.* Sean $`x_s\in E_\varepsilon`$ y $`x_s\to x`$; entonces $`x\in I`$. Para todo $`\delta>0`$, para $`s`$ suficientemente grande se tiene $`|x_s-x|<\delta/2`$, por lo que $`V_{\delta/2}(x_s)\subset V_\delta(x)`$ y
> ```math
> \omega\bigl(f,V_\delta(x)\bigr)\ge\omega\bigl(f,V_{\delta/2}(x_s)\bigr)\ge\omega(f,x_s)\ge\varepsilon .
> ```
> Cuando $`\delta\to0`$ obtenemos $`\omega(f,x)\ge\varepsilon`$, es decir, $`x\in E_\varepsilon`$. *Recubrimiento finito.* Como $`\mu(E_\varepsilon)=0`$, el conjunto $`E_\varepsilon`$ se cubre con un sistema numerable de paralelepípedos de suma de medidas menor que $`\varepsilon/2`$; sustituyamos el $`m`$-ésimo por un paralelepípedo abierto que lo contenga y cuya medida sea mayor en menos de $`\varepsilon/2^{m+1}`$. Obtenemos un recubrimiento del compacto $`E_\varepsilon`$ por paralelepípedos abiertos con suma de medidas menor que $`\varepsilon`$; las [clausuras](lecture-55-56.md#def-5-3-2) de los paralelepípedos de su subrecubrimiento finito son los $`I_1,\dots,I_k`$. Todos son no degenerados.

Consideremos dos particiones $`P'=\{I'_i\}`$ y $`P''=\{I''_j\}`$ del paralelepípedo $`I`$ con puntos marcados $`\xi'`$, $`\xi''`$ y finura pequeña $`\lambda(P')`$, $`\lambda(P'')`$ (recordemos que la finura es el mayor de los diámetros de los paralelepípedos de la partición; cuán pequeña debe ser se indicará más abajo). Sea $`P`$ la partición obtenida intersecando los paralelepípedos de las particiones $`P'`$ y $`P''`$: $`P=\{I_{ij}=I'_i\cap I''_j\}`$ (se toman las intersecciones no degeneradas), y sea $`\xi=\{\xi_{ij}\}`$ cierto conjunto de puntos marcados para $`P`$.

<a id="p077"></a>

Pongamos $`C_1=\bigcup_{i=1}^kI_i`$, y denotemos por $`C_2`$ y $`C_3`$ las uniones de los paralelepípedos $`2I_i`$ y, respectivamente, $`3I_i`$, obtenidos de $`I_i`$ mediante una homotecia de razón $`2`$ y $`3`$ con centro en el centro de $`I_i`$. Entonces $`E_\varepsilon\subset C_1\subset C_2\subset C_3`$, y $`E_\varepsilon`$ está estrictamente dentro de $`C_2`$, mientras que la distancia entre las fronteras de $`C_2`$ y $`C_3`$ es estrictamente positiva.

*Figura de los apuntes (pág. p077): un paralelepípedo del recubrimiento dentro de sus dilataciones; leyendas $`C_2`$, $`C_3`$.*

Observemos que $`\mu(I'_i)=\sum_j\mu(I_{ij})`$. Por tanto,
```math
|\sigma(f,P',\xi')-\sigma(f,P,\xi)|=\Bigl|\sum_{i,j}\bigl(f(\xi'_i)-f(\xi_{ij})\bigr)\mu(I_{ij})\Bigr|\le\Sigma_1+\Sigma_2,
```
donde $`\Sigma_1`$ es la suma de los sumandos $`|f(\xi'_i)-f(\xi_{ij})|\,\mu(I_{ij})`$ sobre aquellos $`i`$ para los que $`I'_i`$ corta a $`C_2`$, y $`\Sigma_2`$ es la suma de los mismos sumandos sobre los $`i`$ restantes. Los sumandos $`\Sigma_1`$ se acotan superiormente de forma burda, sin distinguir casos (nota en el margen).

> **Corrección de la fuente** (M392, U394, U395, U396). En los apuntes el miembro derecho de la estimación se escribe «$`\le\sum_1+\sum_2\left|f(\xi'_i)-f(\xi_{ij})\right|\mu(I_{ij})+\sum\left|f(\xi_i)-f(\xi_{ij})\right|\mu(I_{ij})`$»: en realidad es una sola suma $`\sum_{i,j}|f(\xi'_i)-f(\xi_{ij})|\,\mu(I_{ij})`$ dividida en dos grupos de sumandos, y en el segundo grupo debe figurar $`\xi'_i`$. Las definiciones de $`C_1`$, $`C_2`$, $`C_3`$ en los apuntes son ilegibles («unión de intervalos $`I_{ij}`$ con centros en $`\xi'`$…», «…coord. 2») y se leen según la demostración estándar (cf. V. A. Zorich, «Análisis matemático», parte II, cap. 11, §1): es el recubrimiento de $`E_\varepsilon`$ y sus dilataciones por los factores $`2`$ y $`3`$. En los apuntes se introducen tras la división de la suma; aquí, antes, ya que $`\Sigma_1`$ y $`\Sigma_2`$ se definen a partir de $`C_2`$.

> **Restaurado** (final de la demostración según el esquema estándar, cf. Zorich, ibid.; en los apuntes las estimaciones de $`\Sigma_1`$ y $`\Sigma_2`$ no se completan, y en las lecciones 83–84 el profesor demostró la suficiencia en el caso unidimensional).
>
> Sea $`d`$ la mitad de la menor de las aristas de los paralelepípedos $`I_1,\dots,I_k`$. Si un conjunto de diámetro menor que $`d`$ corta a $`2I_l`$, está contenido en $`3I_l`$: en cada coordenada $`3I_l`$ es más ancho que $`2I_l`$ por cada lado en la mitad de la arista correspondiente de $`I_l`$. Este es el sentido preciso de las palabras «la distancia entre las fronteras de $`C_2`$ y $`C_3`$ es positiva».
>
> *Estimación de $`\Sigma_1`$.* Sea $`\lambda(P')<d`$. Todo paralelepípedo $`I'_i`$ que corta a $`C_2`$ corta a algún $`2I_l`$ y, por tanto, está contenido en $`3I_l`$; asignémoslo a uno de esos $`l`$. Los paralelepípedos sin solapamiento contenidos en $`3I_l`$ tienen medida total a lo sumo $`\mu(3I_l)=3^n\mu(I_l)`$, por lo que la suma de las medidas de todos esos $`I'_i`$ es menor que $`3^n\sum_l\mu(I_l)<3^n\varepsilon`$. Como $`|f(\xi'_i)-f(\xi_{ij})|\le2M`$,
> ```math
> \Sigma_1\le2M\sum_{I'_i\cap C_2\ne\varnothing}\mu(I'_i)<2\cdot3^nM\varepsilon .
> ```
> *Estimación de $`\Sigma_2`$.* El conjunto $`K=I\setminus\operatorname{int}C_2`$ es compacto y no corta a $`E_\varepsilon`$, por lo que $`\omega(f,x)<\varepsilon`$ en cada punto de $`x\in K`$. De aquí se deduce que existe $`\delta_0>0`$ tal que $`\omega(f,V_{\delta_0}(x))<\varepsilon`$ para todo $`x\in K`$. En efecto, para cada punto $`x\in K`$ elijamos $`\delta(x)>0`$ de modo que $`\omega(f,V_{2\delta(x)}(x))<\varepsilon`$. Las bolas abiertas de radios $`\delta(x)`$ con centros $`x\in K`$ cubren el compacto $`K`$; elijamos un subrecubrimiento finito por bolas de centros $`x_1,\dots,x_m`$ y pongamos $`\delta_0=\min_s\delta(x_s)`$. Si $`x\in K`$ está en la bola de centro $`x_s`$, entonces $`V_{\delta_0}(x)\subset V_{2\delta(x_s)}(x_s)`$ y, por tanto, $`\omega(f,V_{\delta_0}(x))<\varepsilon`$.
>
> Supongamos además que $`\lambda(P')<\delta_0`$. Si $`I'_i`$ no corta a $`C_2`$, entonces $`I'_i\subset K`$ y $`I'_i\subset V_{\delta_0}(\xi'_i)`$, ya que el diámetro de $`I'_i`$ es menor que $`\delta_0`$. Como $`\xi_{ij}\in I_{ij}\subset I'_i`$, se tiene $`|f(\xi'_i)-f(\xi_{ij})|<\varepsilon`$, y
> ```math
> \Sigma_2\le\varepsilon\sum_{i,j}\mu(I_{ij})=\varepsilon\,\mu(I).
> ```
> *Conclusión.* Así, si $`\lambda(P')<\min(d,\delta_0)`$, entonces $`|\sigma(f,P',\xi')-\sigma(f,P,\xi)|<(2\cdot3^nM+\mu(I))\,\varepsilon`$. La partición $`P`$ es también más fina que la partición $`P''`$, por lo que para $`\lambda(P'')<\min(d,\delta_0)`$ lo mismo vale para $`P''`$. En consecuencia, para $`\lambda(P'),\lambda(P'')<\min(d,\delta_0)`$
> ```math
> |\sigma(f,P',\xi')-\sigma(f,P'',\xi'')|<2\bigl(2\cdot3^nM+\mu(I)\bigr)\varepsilon .
> ```
> El número $`\varepsilon>0`$ es arbitrario y el factor $`2(2\cdot3^nM+\mu(I))`$ no depende de él; por el criterio de Cauchy las sumas integrales tienen límite cuando $`\lambda(P)\to0`$, es decir, $`f\in R(I)`$. $`\square`$

**Observación (sobre la demostración de la suficiencia).** En los apuntes (pág. p077) la demostración de la suficiencia se escribe otra vez, con una normalización de las constantes tal que la estimación final resulte directamente menor que $`\varepsilon`$; aquí $`|f|\le M`$ en $`I`$ (si $`M=0`$, entonces $`f\equiv0`$ y es integrable). Para ello cubrimos el conjunto $`E_\eta`$, donde $`\eta=\frac{\varepsilon}{2\mu(I)}`$, con un conjunto finito de paralelepípedos $`I_1,\dots,I_k`$ con $`\sum\mu(I_i)<\frac{\varepsilon}{4\cdot3^nM}`$. Fuera del recubrimiento, en cada punto $`x`$, la oscilación es $`\omega(f,x)<\eta`$, por lo que tiene un entorno $`V_\delta(x)`$ en el que la oscilación de la función es $`\omega(f,V_\delta(x))<\eta`$. Entonces, en la notación de la demostración, $`\Sigma_1<2\cdot3^nM\cdot\frac{\varepsilon}{4\cdot3^nM}=\frac{\varepsilon}2`$ y $`\Sigma_2\le\eta\,\mu(I)=\frac{\varepsilon}2`$.

> **Corrección de la fuente** (M530, U400). En los apuntes: «$`\sum\mu(I_i)<\frac{\varepsilon}{4M}`$» para el recubrimiento de $`E_\varepsilon`$ y después «fuera de $`I_i`$ $`f`$ es continua en cada punto ⇒ … $`\omega(f,D(x))<\frac{\varepsilon}{2\mu(I)}`$». Fuera del recubrimiento del conjunto $`E_\varepsilon`$ la función no tiene por qué ser continua: allí solo se sabe que $`\omega(f,x)<\varepsilon`$ (pueden quedar fuera del recubrimiento [puntos de discontinuidad](lecture-16.md#def-2-5-4) con oscilación menor), y es esta estimación la que se usa. Para que la oscilación fuera del recubrimiento sea menor que $`\frac{\varepsilon}{2\mu(I)}`$, hay que cubrir $`E_\eta`$ con $`\eta=\frac{\varepsilon}{2\mu(I)}`$, y por la dilatación del recubrimiento por el factor $`3`$, la suma de medidas del recubrimiento debe ser menor que $`\frac{\varepsilon}{4\cdot3^nM}`$, y no $`\frac{\varepsilon}{4M}`$.

## §10.2. Integral sobre un conjunto

<a id="p078"></a>

### Conjuntos admisibles. Función característica de un conjunto

<a id="def-10-2-1"></a>**Definición 10.2.1.** Un conjunto $`\Omega\subset\mathbb R^n`$ se llama admisible si está acotado en $`\mathbb R^n`$ y su frontera $`\partial\Omega`$ es un conjunto de medida nula.

<a id="def-10-2-2"></a>**Definición 10.2.2.** Sea $`\Omega\subset\mathbb R^n`$ un conjunto admisible. La función
```math
\chi_\Omega(x)=\begin{cases}1, & x\in\Omega,\\ 0, & x\notin\Omega\end{cases}
```
se llama función característica del conjunto $`\Omega`$.

**Observación.** La función $`\chi_\Omega`$ solo tiene discontinuidades en $`\partial\Omega`$: en los [puntos interiores](lecture-57-58.md#def-5-3-3) de $`\Omega`$ es localmente igual a $`1`$, en los exteriores es localmente igual a $`0`$, y en cada punto frontera es discontinua (todo entorno suyo contiene puntos de $`\Omega`$ y del complementario). Si $`\Omega`$ es un [conjunto admisible](#def-10-2-1), entonces $`\mu(\partial\Omega)=0`$ y, por tanto, $`\chi_\Omega`$ es continua en casi todo punto de $`\mathbb R^n`$.

### Integral sobre un conjunto

Sean $`\Omega\subset\mathbb R^n`$ y $`f:\Omega\to\mathbb R`$.

> **Restaurado** (según las diapositivas del curso 2024/25, FS p95; en los apuntes ambas definiciones están sin terminar —«// complet.»—; de la [definición 10.2.3](#def-10-2-3) solo se escribe el comienzo «La fn $`f`$ está definida en el conj. $`\Omega`$. Entonces.», y la línea «$`\Omega=\mathbb R^n`$, $`f:\Omega\to\mathbb R`$» que las precede se lee como $`\Omega\subset\mathbb R^n`$, así en la diapositiva).
>
> <a id="def-10-2-3"></a>**Definición 10.2.3.** Sea la función $`f`$ definida en el conjunto $`\Omega`$. Entonces
> ```math
> f\chi_\Omega(x)=\begin{cases}f(x), & x\in\Omega,\\ 0, & x\notin\Omega\end{cases}
> ```
> (aunque $`f`$ no está definida fuera de $`\Omega`$).
>
> <a id="def-10-2-4"></a>**Definición 10.2.4.** La integral de la función $`f`$ sobre el conjunto (acotado) $`\Omega`$ se define mediante la relación
> ```math
> \int_\Omega f(x)\,dx:=\int_{I\supset\Omega}f\chi_\Omega(x)\,dx,
> ```
> donde $`I`$ es un paralelepípedo arbitrario que contiene el conjunto $`\Omega`$; la integral de la izquierda existe si existe la de la derecha. El conjunto de las funciones integrables en $`\Omega`$ se denota $`R(\Omega)`$.

**Observación (sobre la independencia respecto de la elección del paralelepípedo).** Sean $`\Omega\subset I_1`$ y $`\Omega\subset I_2`$, donde $`I_1`$, $`I_2`$ son paralelepípedos. Entonces las integrales
```math
\int_{I_1}f\chi_\Omega\,dx,\qquad\int_{I_2}f\chi_\Omega\,dx
```
existen o no existen simultáneamente y, si existen, sus valores coinciden. Así, la [definición 10.2.4](#def-10-2-4) es correcta.

Consideremos el paralelepípedo $`I_1\cap I_2\supset\Omega`$. ¿Qué puede decirse de los puntos de discontinuidad de la función $`f\chi_\Omega`$? Son

① los puntos de discontinuidad de $`f`$ en $`\Omega`$;

② los puntos de discontinuidad de $`\chi_\Omega`$, es decir, los puntos de $`\partial\Omega`$.

Todos están en $`\overline\Omega\subset I_1\cap I_2`$, y fuera de $`I_1\cap I_2`$ la función $`f\chi_\Omega`$ es nula. Por tanto, por el criterio de Lebesgue ([teorema 10.1.2](#thm-10-1-2)), las tres integrales
```math
\int_{I_1\cap I_2}f\chi_\Omega\,dx,\qquad\int_{I_1}f\chi_\Omega\,dx,\qquad\int_{I_2}f\chi_\Omega\,dx
```
existen o no existen simultáneamente.

*Figura de los apuntes (pág. p081): dos rectángulos superpuestos $`I_1`$ y $`I_2`$; en la intersección sombreada está el conjunto $`\Omega`$.*

Supongamos que las integrales existen. Consideraremos solo las particiones $`I_1`$ y $`I_2`$ que se obtienen completando particiones de $`I_1\cap I_2`$ (es decir, los paralelepípedos de la partición contenidos en $`I_1\cap I_2`$ forman una partición de $`I_1\cap I_2`$). Observemos que fuera de $`I_1\cap I_2`$ la función $`f\chi_\Omega`$ es nula, por lo que las sumas integrales para $`I_1`$ y $`I_2`$ son en realidad sumas integrales para $`I_1\cap I_2`$:
```math
\sum_if\chi_\Omega(\xi_i)\,\mu(I_{1i})=\sum_{I_{1i}\subset I_1\cap I_2}f\chi_\Omega(\xi_i)\,\mu(I_{1i}),\qquad
\sum_if\chi_\Omega(\eta_i)\,\mu(I_{2i})=\sum_{I_{2i}\subset I_1\cap I_2}f\chi_\Omega(\eta_i)\,\mu(I_{2i}).
```
Pasando al límite cuando la finura de las particiones tiende a cero, obtenemos
```math
\int_{I_1}f\chi_\Omega\,dx=\int_{I_1\cap I_2}f\chi_\Omega\,dx=\int_{I_2}f\chi_\Omega\,dx .
```

> **Corrección de la fuente** (S423, M424, T427). En los apuntes: «① pts de discontinuidad de $`f`$ fuera de $`\Omega`$», «Son siempre pts de discontinuidad de $`\chi_\Omega\in I_1\cap I_2`$», «Las sumas integrales para $`I_1`$ y $`I_2`$ son la misma suma integral para $`I_1\cap I_2`$». Corregido según el sentido y la anotación de la lección de 2024/25 (FS p95): los puntos de discontinuidad de $`f`$ se toman en $`\Omega`$ (fuera de $`\Omega`$ la función $`f`$ no está definida, y $`f\chi_\Omega=0`$); en $`I_1\cap I_2`$ están todos los puntos de discontinuidad de $`f\chi_\Omega`$, no solo $`\chi_\Omega`$; la suma integral para $`I_1`$ y la suma integral para $`I_2`$, cada una la suya, son sumas integrales para $`I_1\cap I_2`$.

> **Restaurado** (precisiones al razonamiento del profesor, según la demostración estándar). 1) Los puntos de la frontera del paralelepípedo $`J=I_1\cap I_2`$ pueden ser puntos de discontinuidad de la restricción de $`f\chi_\Omega`$ a $`J`$ sin serlo en $`I_1`$ (o al revés), pero la frontera de un paralelepípedo tiene medida nula, así que esto no afecta a la aplicación del criterio de Lebesgue; la acotación de $`f\chi_\Omega`$ en $`I_1`$, en $`I_2`$ y en $`J`$ equivale a la acotación de $`f`$ en $`\Omega`$. 2) La igualdad de las sumas integrales de la fórmula de arriba es cierta si en los paralelepípedos no contenidos en $`J`$ los puntos marcados se eligen fuera de $`J`$ (de lo contrario un punto marcado puede caer en una cara común con $`J`$, donde $`f\chi_\Omega`$ no tiene por qué ser nula). Como las integrales existen, pueden calcularse como límites de sumas integrales para cualquier elección así de los puntos marcados y cualesquiera particiones del tipo indicado cuya finura tienda a cero; de aquí se deduce la igualdad de las integrales.

<a id="p079"></a>

### Sumas integrales de Darboux (de §10.1)

Este punto pertenece a §10.1 (de ahí la numeración 10.1.9, 10.1.10 y el [teorema 10.1.3](#thm-10-1-3)); en el cuaderno está escrito en la pág. p079, entre las definiciones de §10.2.

Sean $`f`$ una función real en el paralelepípedo $`I`$ y $`P=\{I_i\}`$ una partición del paralelepípedo $`I`$. Pongamos
```math
m_i=\inf_{x\in I_i}f(x),\qquad M_i=\sup_{x\in I_i}f(x).
```

> **Restaurado** (según las diapositivas del curso 2024/25, FS p93; en los apuntes la definición está sin terminar —«// complet.»—: solo se escribe «La magnitud $`s(f,P)=\sum m_i\mu(I_i)`$, $`S(f,P)`$»).
>
> <a id="def-10-1-9"></a>**Definición 10.1.9.** Las magnitudes
> ```math
> s(f,P)=\sum_im_i\,\mu(I_i),\qquad S(f,P)=\sum_iM_i\,\mu(I_i)
> ```
> se llaman respectivamente suma integral inferior y superior (de Darboux) de la función $`f`$ en el paralelepípedo $`I`$, correspondientes a la partición $`P`$ de este paralelepípedo.

![Una columna sobre un paralelepípedo de la partición bajo la gráfica de la función (pág. p079)](../../assets/lectures-2025-26/lec81-82-p079-darboux-column.jpg)

### Integrales inferior y superior de Darboux

> **Restaurado** (según las diapositivas del curso 2024/25, FS p93; en los apuntes solo figura el título «Def (10.1.10) // complet.»).
>
> <a id="def-10-1-10"></a>**Definición 10.1.10.** Se llaman integral inferior y superior (de Darboux) de la función $`f:I\to\mathbb R`$ en el paralelepípedo $`I`$, respectivamente, las magnitudes
> ```math
> \underline J=\sup_Ps(f,P),\qquad\overline J=\inf_PS(f,P),
> ```
> donde el [ínfimo](lecture-11-12.md#def-2-3-2) y el [supremo](lecture-11-12.md#def-2-3-1) se toman sobre todas las particiones posibles $`P`$ del paralelepípedo $`I`$.

> **Restaurado** (el enunciado del ejercicio procede de la diapositiva FS p93; en los apuntes: «Ejercicio. Los rectángulos $`I`$ tienen la siguiente prop.: // complet.», luego solo «$`s`$» y la pista del profesor «$`\sup\inf\le\inf\sup`$»; la solución sigue el esquema estándar).
>
> **Ejercicio.** Para toda partición $`P`$ del paralelepípedo $`I`$ se cumplen las desigualdades
> ```math
> s(f,P)\le\underline J\le\overline J\le S(f,P).
> ```
> Pista del profesor: $`\sup\inf\le\inf\sup`$. Solución: al añadir nuevos puntos de división, las sumas inferiores no decrecen y las superiores no crecen (el ínfimo sobre un conjunto menor no es menor, el supremo no es mayor). Por tanto, para cualesquiera particiones $`P_1`$, $`P_2`$ y su refinamiento común $`P`$
> ```math
> s(f,P_1)\le s(f,P)\le S(f,P)\le S(f,P_2).
> ```
> Tomando el supremo sobre $`P_1`$ y el ínfimo sobre $`P_2`$, obtenemos $`\underline J\le\overline J`$; las desigualdades extremas se deducen de la definición del ínfimo y del supremo.

### Criterio de Darboux de integrabilidad de una función real

<a id="thm-10-1-3"></a>**Teorema 10.1.3 (criterio de Darboux).** Una función $`f:I\to\mathbb R`$ es integrable en el paralelepípedo $`I`$ si y solo si $`f`$ está acotada en $`I`$ y $`\underline J=\overline J`$.

El teorema se da sin demostración.

> **Corrección de la fuente** (A413, U414). En los apuntes: «Teorema (10.1.13)» y «$`f\in R(I)\Leftrightarrow\underline{J}=\overline{J}`$». El número se corrige a 10.1.3 (así en la diapositiva FS p93; en §10.1 no hay otros teoremas); la nota tras el número, leída como «fór.», es al parecer «s/d» (sin demostración). Se añade la condición de acotación omitida (así en la diapositiva): sin ella la afirmación es falsa. Por ejemplo, para $`I=[0,1]`$, $`f(x)=\frac1x`$ para $`0<x\le1`$, $`f(0)=0`$ se tiene $`S(f,P)=+\infty`$ para todo $`P`$, mientras que para la partición por los puntos $`0<2^{-N}<2^{-N+1}<\dots<\frac12<1`$ obtenemos $`s(f,P)=\frac N2`$; así, $`\underline J=\overline J=+\infty`$, aunque $`f\notin R(I)`$ por el [teorema 10.1.1](lecture-79-80.md#thm-10-1-1).

<a id="p080"></a>

### Medida (volumen) de un conjunto admisible

<a id="def-10-2-5"></a>**Definición 10.2.5.** La medida (de Jordan), o volumen, de un conjunto acotado $`\Omega\subset\mathbb R^n`$ es la magnitud
```math
\mu(\Omega):=\int_\Omega1\,dx=\int_I\chi_\Omega(x)\,dx\qquad(I\supset\Omega),
```
si existe dicha integral (de Riemann).

> **Corrección de la fuente** (S417, T532). En los apuntes: «$`\mu(\Omega):=\int_I1\,dx`$», y en la observación de abajo «$`\int_I1\,dx=\int_{I\ni\Omega}\chi_\Omega(x)\,dx`$». La integral de uno sobre el paralelepípedo $`I`$ vale $`\mu(I)`$, y no el volumen $`\Omega`$; debe ser $`\int_\Omega1\,dx`$, que por la [definición 10.2.4](#def-10-2-4) es igual a $`\int_I\chi_\Omega(x)\,dx`$ para cualquier paralelepípedo $`I\supset\Omega`$ (así en la diapositiva FS p96).

<a id="def-10-2-6"></a>**Definición 10.2.6.** Un conjunto $`\Omega\subset\mathbb R^n`$ se llama conjunto de medida nula en el sentido de Jordan, o conjunto de volumen nulo, si para todo $`\varepsilon>0`$ puede cubrirse con un sistema finito de paralelepípedos (rectángulos) $`I_1,\dots,I_k`$ tal que
```math
\sum_{i=1}^k\mu(I_i)<\varepsilon .
```

**Observación.** Por la [definición 10.2.4](#def-10-2-4)
```math
\int_\Omega1\,dx=\int_{I\supset\Omega}\chi_\Omega(x)\,dx .
```
Como los puntos de discontinuidad de $`\chi_\Omega`$ son exactamente los puntos de $`\partial\Omega`$, por el criterio de Lebesgue ([teorema 10.1.2](#thm-10-1-2)) esta integral existe si y solo si $`\mu(\partial\Omega)=0`$. Por tanto, la medida $`\mu(\Omega)`$ de un conjunto acotado $`\Omega`$ solo está definida para los conjuntos admisibles (y para todos ellos).

**Observación.** Solo los conjuntos admisibles son medibles (según Jordan).

*Figura en el margen (pág. p080): dos óvalos encajados, «conjuntos de medida nula según Jordan» dentro de «conjuntos de medida nula según Lebesgue».*

> **Restaurado** (explicación de la figura, según la anotación de la lección de 2024/25, FS p96, y un ejemplo estándar). Un conjunto de medida nula según Jordan es un conjunto de medida nula según Lebesgue: un sistema finito de paralelepípedos es un caso particular de uno a lo sumo numerable. El recíproco es falso: el conjunto de los puntos racionales del segmento $`[0,1]`$ es numerable y, por tanto, tiene medida nula según Lebesgue (propiedades ① y ④), pero un sistema finito de segmentos que cubra todos sus puntos cubre también todo el segmento $`[0,1]`$ (su unión es cerrada), así que la suma de las longitudes es al menos $`1`$. Para los compactos ambas nociones coinciden: de un recubrimiento por paralelepípedos abiertos puede extraerse un subrecubrimiento finito (así se usó en la demostración de la suficiencia en el [teorema 10.1.2](#thm-10-1-2)).

<a id="p081"></a>

### Criterio de integrabilidad sobre un conjunto

> **Restaurado** (según las diapositivas del curso 2024/25, FS p95; en los apuntes figuran el título «Teorema (10.2.1) // complet.» y un comienzo ilegible del enunciado «… $`f:\Omega\to\mathbb R`$ es integrable en un conj. admisible»).
>
> <a id="thm-10-2-1"></a>**Teorema 10.2.1.** Una función $`f:\Omega\to\mathbb R`$ es integrable en un conjunto admisible $`\Omega`$ si y solo si está acotada y es continua en casi todos los puntos del conjunto $`\Omega`$.

**Demostración.** Tomemos un paralelepípedo $`I\supset\Omega`$; por la [definición 10.2.4](#def-10-2-4) hay que averiguar cuándo $`f\chi_\Omega\in R(I)`$. Los puntos de discontinuidad de la función $`f\chi_\Omega`$ son los puntos de discontinuidad de $`f`$ en $`\Omega`$ y los puntos de discontinuidad de $`\chi_\Omega`$ situados en $`\partial\Omega`$. Más precisamente, fuera de $`\partial\Omega`$ los puntos de discontinuidad de $`f\chi_\Omega`$ son exactamente los puntos de discontinuidad de $`f`$ situados en el interior de $`\Omega`$ (en los puntos exteriores $`f\chi_\Omega`$ es localmente nula), y $`\mu(\partial\Omega)=0`$, ya que $`\Omega`$ es admisible. Por tanto, el conjunto de los puntos de discontinuidad de $`f\chi_\Omega`$ tiene medida nula si y solo si el conjunto de los puntos de discontinuidad de $`f`$ en $`\Omega`$ tiene medida nula. Además, $`f\chi_\Omega`$ está acotada en $`I`$ si y solo si $`f`$ está acotada en $`\Omega`$. Basta aplicar el criterio de Lebesgue ([teorema 10.1.2](#thm-10-1-2)). $`\square`$

## §10.3. Propiedades generales de la integral

<a id="p082"></a>

<a id="thm-10-3-1"></a>**Teorema 10.3.1.** Sean $`\Omega_1`$, $`\Omega_2`$ conjuntos admisibles en $`\mathbb R^n`$, y $`f`$ una función definida en $`\Omega_1\cup\Omega_2`$. Entonces:

① la existencia de las integrales se relaciona así:
```math
\exists\int_{\Omega_1\cup\Omega_2}f(x)\,dx\iff\exists\int_{\Omega_i}f(x)\,dx\ \ (i=1,2)\implies\exists\int_{\Omega_1\cap\Omega_2}f(x)\,dx;
```

② si $`\mu(\Omega_1\cap\Omega_2)=0`$, entonces, siempre que existan las integrales, se cumple la igualdad
```math
\int_{\Omega_1\cup\Omega_2}f(x)\,dx=\int_{\Omega_1}f(x)\,dx+\int_{\Omega_2}f(x)\,dx .
```

**Demostración del punto ②.** Sea $`\mu(\Omega_1\cap\Omega_2)=0`$ y supongamos que existen las integrales. Tomemos un paralelepípedo $`I\supset\Omega_1\cup\Omega_2`$. Por la [definición 10.2.4](#def-10-2-4)
```math
\int_{\Omega_1\cup\Omega_2}f(x)\,dx=\int_If\chi_{\Omega_1\cup\Omega_2}(x)\,dx .
```
Observemos que
```math
\chi_{\Omega_1\cup\Omega_2}(x)=\chi_{\Omega_1}(x)+\chi_{\Omega_2}(x)-\chi_{\Omega_1\cap\Omega_2}(x)
```
(en los puntos de ambos conjuntos: $`1=1+1-1`$; de exactamente uno de ellos: $`1=1+0-0`$; fuera de ambos: $`0=0`$). Por tanto, usando la linealidad de la integral sobre un paralelepípedo (se deduce de la linealidad de las sumas integrales),
```math
\int_If\chi_{\Omega_1\cup\Omega_2}\,dx=\underbrace{\int_If\chi_{\Omega_1}\,dx}_{=\int_{\Omega_1}f\,dx}+\underbrace{\int_If\chi_{\Omega_2}\,dx}_{=\int_{\Omega_2}f\,dx}-\underbrace{\int_If\chi_{\Omega_1\cap\Omega_2}\,dx}_{=0},
```
donde la última integral existe por el punto ① y es nula, ya que $`\mu(\Omega_1\cap\Omega_2)=0`$. $`\square`$

> **Corrección de la fuente** (T531, S432). En los apuntes la demostración se titula «Dem. (p. ① t. 10.3.1)», pero lo que se demuestra es el punto ② (así también en la anotación de la lección de 2024/25, FS p97: «Dem. (punto ②)»). Los signos «⇔» de la última línea («$`\int_{\Omega_1}f\,dx`$ ⇔ $`\int_{\Omega_2}f\,dx`$ − … ⇔ $`0`$») son signos de igualdad verticales bajo llaves, que relacionan los sumandos con las integrales sobre $`\Omega_1`$, $`\Omega_2`$ y con cero, y el signo dentro de un círculo al comienzo de esta línea indica la continuación de la igualdad.

> **Restaurado** (según la demostración estándar; en los apuntes y en la diapositiva FS p97 el punto ① no se demuestra, y no se justifica que la última integral sea nula). *Punto ①.* Los conjuntos $`\Omega_1\cup\Omega_2`$ y $`\Omega_1\cap\Omega_2`$ están acotados y sus fronteras están contenidas en $`\partial\Omega_1\cup\partial\Omega_2`$, por lo que son admisibles (propiedades ④, ⑤). Sea $`I\supset\Omega_1\cup\Omega_2`$ un paralelepípedo. La suma y el producto de funciones son continuos en cada punto donde son continuos todos los sumandos (factores), y $`\chi_\Omega`$ solo es discontinua en $`\partial\Omega`$. Por tanto, si $`f\chi_{\Omega_1\cup\Omega_2}\in R(I)`$, las funciones $`f\chi_{\Omega_i}=f\chi_{\Omega_1\cup\Omega_2}\cdot\chi_{\Omega_i}`$ y $`f\chi_{\Omega_1\cap\Omega_2}=f\chi_{\Omega_1\cup\Omega_2}\cdot\chi_{\Omega_1\cap\Omega_2}`$ están acotadas, y sus puntos de discontinuidad están en la unión del conjunto de puntos de discontinuidad de $`f\chi_{\Omega_1\cup\Omega_2}`$ y el conjunto $`\partial\Omega_1\cup\partial\Omega_2`$, es decir, en un conjunto de medida nula; por el criterio de Lebesgue son integrables en $`I`$. Recíprocamente, si $`f\chi_{\Omega_1},f\chi_{\Omega_2}\in R(I)`$, entonces $`f\chi_{\Omega_1\cap\Omega_2}=f\chi_{\Omega_1}\cdot\chi_{\Omega_2}\in R(I)`$ por el mismo razonamiento, y $`f\chi_{\Omega_1\cup\Omega_2}=f\chi_{\Omega_1}+f\chi_{\Omega_2}-f\chi_{\Omega_1\cap\Omega_2}\in R(I)`$. *Anulación.* La función $`f`$ está acotada en $`\Omega_1\cup\Omega_2`$, $`|f|\le M`$ (la integral sobre $`\Omega_1\cup\Omega_2`$ existe). Para toda partición $`P`$ del paralelepípedo $`I`$ con puntos marcados $`\xi`$
> ```math
> \bigl|\sigma(f\chi_{\Omega_1\cap\Omega_2},P,\xi)\bigr|\le M\,\sigma(\chi_{\Omega_1\cap\Omega_2},P,\xi)\xrightarrow[\lambda(P)\to0]{}M\int_I\chi_{\Omega_1\cap\Omega_2}\,dx=M\,\mu(\Omega_1\cap\Omega_2)=0 .
> ```

### Estimación de la integral

<a id="prop-10-3-1"></a>**Proposición 10.3.1.** Si $`f\in R(\Omega)`$, entonces $`|f|\in R(\Omega)`$ y se cumple la desigualdad
```math
\Bigl|\int_\Omega f(x)\,dx\Bigr|\le\int_\Omega|f(x)|\,dx .
```
Aquí $`R(\Omega)`$ es el conjunto de las funciones integrables según Riemann en el conjunto $`\Omega`$.

**Demostración.** 1) La integrabilidad de $`|f|`$ en $`\Omega`$ se deduce de la definición de la integral sobre el conjunto $`\Omega`$ y del criterio de Lebesgue: si $`I\supset\Omega`$ y $`f\chi_\Omega\in R(I)`$, la función $`|f|\chi_\Omega=|f\chi_\Omega|`$ está acotada en $`I`$ y es continua en cada punto donde lo es $`f\chi_\Omega`$, por lo que $`|f\chi_\Omega|\in R(I)`$.

2) La desigualdad se obtiene pasando al límite en la desigualdad para las sumas integrales: para toda partición $`P`$ del paralelepípedo $`I`$ con puntos marcados $`\xi`$
```math
|\sigma(f\chi_\Omega,P,\xi)|\le\sigma(|f|\chi_\Omega,P,\xi),
```
y cuando $`\lambda(P)\to0`$ obtenemos $`\bigl|\int_\Omega f\,dx\bigr|\le\int_\Omega|f|\,dx`$. $`\square`$

## Referencias cruzadas

- Tema en el curso: [capítulo 17 «Integrales múltiples y cambio de variables»](../17-multiple-integrals.md) — [§17.1 «Definición e integrales iteradas»](../17-multiple-integrals.md#sec-17-1); sumas de Darboux en el caso unidimensional — [§8.1 «Particiones y sumas de Darboux»](../08-riemann-integration.md#sec-8-1); [medida de Lebesgue](lecture-51-52.md#def-4-6-6) — [§19.3 «Medida de Lebesgue»](../19-measure-theory.md#sec-19-3).
- El caso unidimensional: conjunto de medida nula ([definición 4.2.11](lecture-41-42.md#def-4-2-11)) y criterio de Lebesgue ([teorema 4.2.5](lecture-41-42.md#thm-4-2-5)) — [lecciones 41–42](lecture-41-42.md).
- Comienzo de §10.1 (un paralelepípedo y su medida, particiones, sumas integrales, [definiciones 10.1.1](lecture-79-80.md#def-10-1-1)–[10.1.7](lecture-79-80.md#def-10-1-7), enunciado del [teorema 10.1.1](lecture-79-80.md#thm-10-1-1)): [lecciones 79–80](lecture-79-80.md).
- Final de §10.3 (propiedades de la integral), demostración de la suficiencia del criterio de Lebesgue en el caso unidimensional, teorema de Fubini y principio de Cavalieri (§10.4): [lecciones 83–84](lecture-83-84.md).

---

[← Lecciones 79–80](lecture-79-80.md) · [Índice de lecciones](index.md) · [Lecciones 83–84 →](lecture-83-84.md) · [Términos y teoremas](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-81-82.md) · [English](../../en/lectures-2025-26/lecture-81-82.md)
