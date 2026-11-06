---
title: "Lecciones 71–72 — reordenaciones de series, convergencia uniforme, propiedades de las funciones límite, series funcionales"
lang: es
course: "Análisis matemático, 2025/26"
lecture: 71-72
semester: 3
source: "cuaderno manuscrito, págs. p030–p041"
source_pages: "p030, p031, p034, p035, p036, p037, p038, p039, p040, p041"
course_chapter: 24
---
# Lecciones 71–72 — reordenaciones de series, convergencia uniforme, propiedades de las funciones límite, series funcionales

[← Lecciones 69–70](lecture-69-70.md) · [Índice de lecciones](index.md) · [Términos y teoremas](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-71-72.md) · [English](../../en/lectures-2025-26/lecture-71-72.md)

> **Fuente y numeración.** Los apuntes se copiaron de un cuaderno manuscrito (págs. p030, p031, p034–p041; el texto bruto de las páginas está en [`ocr/raw/`](../../../ocr/raw/p030.md); las págs. p032 y p033 son duplicados técnicos de p030 y p031). La pág. p030 comienza con el final de §7.5 (un ejemplo de reordenación y las propiedades conmutativas de las series); en el margen de la misma página empieza la anotación «Lecciones 71–72» con el plan de la clase: series funcionales; convergencia uniforme de sucesiones funcionales; criterio de Bolzano–Cauchy y criterio de Weierstrass; propiedades de las series funcionales uniformemente convergentes. La transcripción de la pág. p031 se interrumpe en la palabra «Ejemplo:», aunque en la página figuran el ejemplo $`f_n(x)=x^n`$ y dos «$`\varepsilon`$-tubos» dibujados (véase [`ocr/MANIFEST.md`](../../../ocr/MANIFEST.md)); el ejemplo y las figuras se restauran a partir de las diapositivas del curso 2024/25. El final del ejemplo 4 de §8.2 está escrito en el cuaderno en la pág. p039, ya después del [teorema 8.2.3](#thm-8-2-3) y de la [definición 8.3.1](#def-8-3-1), y se deja en ese lugar. Entre las págs. p039 y p040 se perdieron la [definición 8.3.2](#def-8-3-2), el enunciado del criterio de Bolzano–Cauchy de convergencia uniforme de una serie y el comienzo de su demostración; se restauran. La numeración de definiciones y teoremas es la del profesor. Los lapsus de los apuntes se corrigen y se marcan con bloques «Corrección de la fuente»; los pasajes perdidos se restauran y se marcan con bloques «Restaurado»; las etiquetas corresponden a [`ocr/RESOLVED.md`](../../../ocr/RESOLVED.md). Los lugares que aún hay que cotejar con el cuaderno se enumeran en [`ocr/ISSUES.md`](../../../ocr/ISSUES.md).

## §7.5. Reordenaciones de series (conclusión)

<a id="p030"></a>

**Ejemplo.** La serie
```math
\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{k}=1-\frac12+\frac13-\frac14+\dots
```
converge condicionalmente (converge por el [criterio de Leibniz](../04-numeric-series.md#alternating-series-test), mientras que la serie de los valores absolutos —la serie armónica— diverge), y su suma es $`\ln2`$ (lecciones 69–70). Denotemos sus [sumas parciales](../04-numeric-series.md#sec-4-1)
```math
S_n=\sum_{k=1}^{n}\frac{(-1)^{k-1}}{k},\qquad S_n\to\ln2 .
```

> **Corrección de la fuente** (T506). En los apuntes: «$`S_n=\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{k}`$». Una suma parcial es la suma de los primeros $`n`$ términos, por lo que el [límite superior](lecture-13.md#def-2-3-9) de la suma se corrige a $`n`$.

Reordenemos los términos de la serie de modo que a cada término positivo le sigan dos negativos:
```math
1-\frac12-\frac14+\frac13-\frac16-\frac18+\frac15-\frac1{10}-\frac1{12}+\dots
```
Los términos positivos $`\frac1{2k-1}`$ y los negativos $`-\frac1{2k}`$ conservan su orden, y cada término de la serie original aparece exactamente una vez, así que es una reordenación en el sentido de la [definición 7.5.1](lecture-69-70.md#def-7-5-1). Sea $`T_n`$ una suma parcial de la nueva serie.

Agrupemos los términos de tres en tres: $`T_{3m}=\left(1-\frac12-\frac14\right)+\left(\frac13-\frac16-\frac18\right)+\dots`$; la $`k`$-ésima terna contiene el término positivo $`\frac1{2k-1}`$ y los negativos $`-\frac1{4k-2}`$, $`-\frac1{4k}`$. Como $`\frac1{2k-1}-\frac1{4k-2}=\frac2{4k-2}-\frac1{4k-2}=\frac1{4k-2}`$, obtenemos
```math
T_{3m}=\sum_{k=1}^{m}\left(\frac1{2k-1}-\frac1{4k-2}-\frac1{4k}\right)=\sum_{k=1}^{m}\left(\frac1{4k-2}-\frac1{4k}\right)=\frac12\sum_{k=1}^{m}\left(\frac1{2k-1}-\frac1{2k}\right)=\frac12\,S_{2m}.
```
Como $`S_n\to\ln2`$,
```math
T_{3m}=\frac12\,S_{2m}\to\frac12\ln2,\qquad T_{3m+1}=T_{3m}+\frac1{2m+1}\to\frac12\ln2,\qquad T_{3m+2}=T_{3m+1}-\frac1{4m+2}\to\frac12\ln2 .
```

> **Restaurado** (según las diapositivas del curso 2024/25, FS p60; los apuntes de 2022, M3S p58). Las [subsucesiones](lecture-11-12.md#def-2-3-7) $`(T_{3m})`$, $`(T_{3m+1})`$, $`(T_{3m+2})`$ agotan todos los índices y tienen un límite común, por lo que $`T_n\to\frac12\ln2`$. Pero $`S_n\to\ln2`$: reordenar los términos de una serie [condicionalmente convergente](../04-numeric-series.md#sec-4-3) ha cambiado su suma.

### Propiedades conmutativas de las series

1. Las series positivas tienen la propiedad conmutativa.
2. Las series absolutamente convergentes tienen la propiedad conmutativa.
3. Teorema de Riemann. Si una serie converge condicionalmente, no tiene la propiedad conmutativa. Más aún, para todo $`B\in\overline{\mathbb R}=\mathbb R\cup\{-\infty,+\infty\}`$ existe una [biyección](lecture-01-02.md#def-1-1-6) $`\sigma:\mathbb N\to\mathbb N`$ tal que $`\sum_{n=1}^{\infty}a_{\sigma(n)}=B`$.

> **Restaurado** (según la demostración estándar, cf. Zorich/Fichtenholz; en los apuntes y en las diapositivas de 2024/25 las propiedades se enuncian sin demostración).
>
> **Demostración de la propiedad 1.** Sean $`a_n\ge0`$, $`A=\sum_{n=1}^{\infty}a_n\in[0,+\infty]`$ y $`\sigma`$ una biyección. Para todo $`N`$ pongamos $`K=\max\{\sigma(1),\dots,\sigma(N)\}`$; entonces $`\sum_{n=1}^{N}a_{\sigma(n)}\le\sum_{k=1}^{K}a_k\le A`$. Las sumas parciales de la serie positiva $`\sum a_{\sigma(n)}`$ no superan $`A`$, por lo que $`\sum a_{\sigma(n)}\le A`$. A su vez, la serie original se obtiene de la serie $`\sum a_{\sigma(n)}`$ mediante la reordenación $`\sigma^{-1}`$, por lo que también $`A\le\sum a_{\sigma(n)}`$. Así, las sumas son iguales (ambas finitas o ambas iguales a $`+\infty`$), es decir, las series convergen y divergen simultáneamente. $`\square`$
>
> **Demostración de la propiedad 2.** Pongamos $`a_n^+=\max\{a_n,0\}`$, $`a_n^-=\max\{-a_n,0\}`$; entonces $`a_n=a_n^+-a_n^-`$ y $`0\le a_n^{\pm}\le|a_n|`$. Si la serie $`\sum|a_n|`$ converge, por el primer criterio de comparación convergen las series positivas $`\sum a_n^+`$ y $`\sum a_n^-`$, y por la propiedad 1, para toda biyección $`\sigma`$ convergen las series $`\sum a_{\sigma(n)}^{\pm}`$, con $`\sum a_{\sigma(n)}^{\pm}=\sum a_n^{\pm}`$ (y $`\sum|a_{\sigma(n)}|=\sum|a_n|`$, es decir, la reordenación también converge absolutamente). Por tanto,
> ```math
> \sum_{n=1}^{\infty}a_{\sigma(n)}=\sum_{n=1}^{\infty}a_{\sigma(n)}^+-\sum_{n=1}^{\infty}a_{\sigma(n)}^-=\sum_{n=1}^{\infty}a_n^+-\sum_{n=1}^{\infty}a_n^-=\sum_{n=1}^{\infty}a_n .
> ```
> $`\square`$
>
> **Demostración del teorema de Riemann.** Sea la serie $`\sum a_n`$ condicionalmente convergente. Entonces $`a_n\to0`$ y $`\sum a_n^+=\sum a_n^-=+\infty`$: si, por ejemplo, convergiera la serie $`\sum a_n^+`$, convergería la serie $`\sum a_n^-=\sum(a_n^+-a_n)`$ y, con ella, $`\sum|a_n|=\sum(a_n^++a_n^-)`$, lo cual es una contradicción (análogamente para $`\sum a_n^-`$). En particular, hay infinitos términos no negativos e infinitos términos negativos. Escribamos, en orden creciente de índices, los términos no negativos de la serie $`p_1,p_2,\dots`$ y los valores absolutos de los términos negativos $`q_1,q_2,\dots`$; entonces $`p_k\to0`$, $`q_k\to0`$ y $`\sum p_k=\sum q_k=+\infty`$.
>
> Sea $`B\in\mathbb R`$. Tomamos sucesivamente los términos $`p_1,p_2,\dots`$ hasta que la suma supere por primera vez $`B`$; luego los términos $`-q_1,-q_2,\dots`$ hasta que la suma sea por primera vez menor que $`B`$; luego otra vez términos positivos, y así sucesivamente. Cada etapa termina en un número finito de pasos, ya que $`\sum p_k=\sum q_k=+\infty`$, y a partir de la segunda etapa cada etapa usa al menos un término; por tanto, la nueva serie contiene todos los términos de la serie original, cada uno exactamente una vez, es decir, es una reordenación. Dentro de una etapa las sumas parciales varían monótonamente, y al final de la etapa difieren de $`B`$ a lo sumo en el último término tomado; por tanto, durante una etapa una suma parcial difiere de $`B`$ a lo sumo en el mayor de los últimos términos tomados en esta etapa y en la anterior. Como $`p_k\to0`$ y $`q_k\to0`$, las sumas parciales tienden a $`B`$.
>
> Para $`B=+\infty`$ tomamos términos positivos hasta que la suma supere $`1`$, luego un término negativo, luego positivos hasta que la suma supere $`2`$, luego un negativo, y así sucesivamente; las sumas parciales tienden a $`+\infty`$. El caso $`B=-\infty`$ es simétrico. Finalmente, tomando cualquier $`B\ne\sum a_n`$ obtenemos una reordenación con otra suma: la serie no tiene la propiedad conmutativa. $`\square`$

## §8.1. Convergencia uniforme

Comienza el capítulo 8 «Sucesiones y series funcionales». Consideremos una sucesión de funciones $`(f_n)_{n\in\mathbb N}`$, $`f_n:X\to\mathbb R`$, y una función $`f:X\to\mathbb R`$.

> **Corrección de la fuente** (S129). En los apuntes: «$`f_n:X\to\overline{\mathbb R}`$, $`\overline{\mathbb R}:=\mathbb R\cup\{\pm\infty\}`$», y lo mismo para $`f`$. Más adelante se usan en todas partes las diferencias $`|f_n(x)-f(x)|`$, no definidas para valores infinitos; en la diapositiva del curso 2024/25 (FS p62) las funciones son reales. Corregido a $`f_n,f:X\to\mathbb R`$.

<a id="p031"></a>

<a id="def-8-1-1"></a>**Definición 8.1.1.** Diremos que la sucesión $`(f_n)`$ converge en $`X`$ a $`f`$ puntualmente si para cada $`x\in X`$ la sucesión numérica $`a_n:=f_n(x)`$ converge al número $`a:=f(x)`$ cuando $`n\to\infty`$.

**Definición 8.1.1a.** $`f_n\to f`$ puntualmente en el conjunto $`E\subset X`$ si
```math
\forall x\in E\ \ \forall\varepsilon>0\ \ \exists N=N(x,\varepsilon)\ \ \forall n>N:\quad |f_n(x)-f(x)|<\varepsilon .
```

<a id="def-8-1-2"></a>**Definición 8.1.2.** $`f_n\to f`$ uniformemente en el conjunto $`E\subset X`$ si
```math
\forall\varepsilon>0\ \ \exists N=N(\varepsilon)\ \ \forall x\in E\ \ \forall n>N:\quad |f_n(x)-f(x)|<\varepsilon .
```

Notación: $`f_n\rightrightarrows f`$ para la convergencia uniforme, $`f_n\to f`$ para la convergencia puntual. Sea $`E=X`$. Si $`f_n\rightrightarrows f`$ en $`X`$, entonces $`f_n\to f`$ puntualmente en $`X`$: la convergencia uniforme implica la puntual (el índice $`N(\varepsilon)`$ de la [definición 8.1.2](#def-8-1-2) sirve en la definición de convergencia puntual para cada $`x`$).

*¡El recíproco, en general, es falso!*

> **Restaurado** (según las diapositivas del curso 2024/25, FS p62). La transcripción de la pág. p031 se interrumpe en la palabra «Ejemplo:»; según la descripción de esta página y de su duplicado p033 en [`ocr/MANIFEST.md`](../../../ocr/MANIFEST.md), en ella figuran el ejemplo $`f_n(x)=x^n`$ y dos «$`\varepsilon`$-tubos» dibujados. Se reproducen a continuación según las notas del profesor a la diapositiva.
>
> **Ejemplo.** $`X=[0,1]`$, $`f_n(x)=x^n`$. Entonces
> ```math
> f_n(x)\xrightarrow[n\to\infty]{}f(x)=\begin{cases}0,&x\in[0,1),\\1,&x=1,\end{cases}
> ```
> es decir, la sucesión converge puntualmente en $`[0,1]`$; aquí no hay convergencia uniforme en $`[0,1]`$ (véase el ejemplo 3 de §8.2).
>
> *Figuras de los apuntes (pág. p031).* En la primera figura las gráficas de $`y=f(x)-\varepsilon`$, $`y=f(x)`$, $`y=f(x)+\varepsilon`$ delimitan una franja (un «$`\varepsilon`$-tubo») alrededor de la gráfica de $`f`$ con la leyenda «$`\forall n>N`$»: en la convergencia uniforme, a partir de cierto índice $`N+1`$, las gráficas de todas las funciones $`f_n`$ están en esa franja. En la segunda figura se marcan los puntos $`x_1`$, $`x_2`$ con las leyendas «$`\forall n>N_1`$», «$`\forall n>N_2`$»: en la convergencia puntual el índice $`N_i`$ depende del punto $`x_i`$.

<a id="p034"></a>

Surgen preguntas de forma natural.

1. Sean $`X\subset\mathbb R`$ y todas las $`f_n`$ continuas (en un punto o en un conjunto). ¿Será continua $`f`$?
2. Sean $`X\subset\mathbb R`$ y todas las $`f_n`$ diferenciables (en un punto o en un conjunto). ¿Será diferenciable $`f`$? En caso afirmativo, ¿es cierto que $`f_n'\to f'`$?
3. Sean todas las $`f_n`$ integrables en $`[a,b]`$. ¿Será integrable $`f`$? En caso afirmativo, ¿es cierto que $`\int_a^bf_n\to\int_a^bf`$?

### La convergencia uniforme en términos de un ε-entorno

(En las diapositivas del curso este punto se llama «Convergencia uniforme y desviación de Chebyshov».) Consideremos funciones $`f,g:X\to\mathbb R`$.

<a id="def-8-1-3"></a>**Definición 8.1.3.** La magnitud
```math
\rho(f,g)=\sup_{x\in X}|f(x)-g(x)|
```
se llama desviación uniforme de las funciones $`f`$ y $`g`$ (en las diapositivas, desviación de Chebyshov).

> **Corrección de la fuente** (A134). En los apuntes el número figura como «Def (8.3)»; por su lugar en la exposición y por la diapositiva del curso 2024/25 (FS p62) es la [definición 8.1.3](#def-8-1-3).

<a id="def-8-1-4"></a>**Definición 8.1.4.** $`f_n\rightrightarrows f`$ si para todo $`\varepsilon>0`$ existe $`N`$ tal que $`\rho(f_n,f)<\varepsilon`$ para todo $`n>N`$.

**Definición 8.1.4a.** $`f_n\rightrightarrows f`$ si $`\alpha_n:=\rho(f_n,f)\to0`$ cuando $`n\to\infty`$.

> **Corrección de la fuente** (M507). En los apuntes: «$`f_n\to f`$ si $`\rho(f_n,f)\to0`$». Aquí se define la convergencia uniforme, por lo que debe ser $`f_n\rightrightarrows f`$ (así en la diapositiva FS p62); la convergencia puntual no se describe con la condición $`\rho(f_n,f)\to0`$.

## §8.2. Convergencia uniforme y propiedades de las funciones límite

Sean $`f_n\to f`$ en el conjunto $`X`$ y todas las $`f_n`$ con cierta propiedad. La pregunta es si la función límite $`f`$ tendrá esa misma propiedad.

### Continuidad de la función límite

<a id="thm-8-2-1"></a>**Teorema 8.2.1 (continuidad de la función límite).** Supongamos que

1. $`f_n\in C([a,b])`$ para todo $`n`$;
2. $`f_n\rightrightarrows f`$ en $`[a,b]`$.

Entonces $`f\in C([a,b])`$.

<a id="p035"></a>

**Demostración.** Tomemos un punto arbitrario $`x_0\in[a,b]`$ y probemos que $`f`$ es continua en $`x_0`$, es decir, que
```math
\forall\varepsilon>0\ \ \exists\delta>0\ \ \forall x\in[a,b]:\quad |x-x_0|<\delta\ \Rightarrow\ |f(x)-f(x_0)|<\varepsilon .
```
Tomemos cualquier $`\varepsilon>0`$. Como $`f_n\rightrightarrows f`$, existe $`N=N\left(\frac\varepsilon3\right)`$ tal que $`|f_n(x)-f(x)|<\frac\varepsilon3`$ para todo $`n>N`$ y todo $`x\in[a,b]`$.

Fijemos algún índice $`n>N`$. La función $`f_n`$ es [continua en el punto](lecture-16.md#def-2-5-1) $`x_0`$ (recordemos que por hipótesis todas las $`f_n`$ son continuas), por lo que existe $`\delta=\delta\left(\frac\varepsilon3\right)>0`$ tal que $`|f_n(x)-f_n(x_0)|<\frac\varepsilon3`$ para todo $`x\in[a,b]`$, $`|x-x_0|<\delta`$. Entonces, para todos esos $`x`$
```math
\begin{aligned}
|f(x)-f(x_0)|&=|f(x)-f_n(x)+f_n(x)-f_n(x_0)+f_n(x_0)-f(x_0)|\\
&\le|f(x)-f_n(x)|+|f_n(x)-f_n(x_0)|+|f_n(x_0)-f(x_0)|<\frac\varepsilon3+\frac\varepsilon3+\frac\varepsilon3=\varepsilon .
\end{aligned}
```
$`\square`$

**Corolario.** Sean $`f_n\in C([a,b])`$ para todo $`n`$ y $`f_n\rightrightarrows f`$ en $`[a,b]`$. Entonces, para todo punto $`x_0\in[a,b]`$
```math
\lim_{x\to x_0}\lim_{n\to\infty}f_n(x)=\lim_{n\to\infty}\lim_{x\to x_0}f_n(x).
```

> **Corrección de la fuente** (M508). En el enunciado del corolario de los apuntes el punto $`x_0`$ no se introduce; se ha añadido «para todo punto $`x_0\in[a,b]`$» (los límites en $`x\to x_0`$ se toman sobre $`x\in[a,b]`$).

**Demostración.** La convergencia uniforme implica la puntual, por lo que $`\lim_{n\to\infty}f_n(x)=f(x)`$ para cada $`x\in[a,b]`$. Por el [teorema 8.2.1](#thm-8-2-1) la función $`f`$ es continua, por lo que $`\lim_{x\to x_0}f(x)=f(x_0)`$. Así,
```math
\lim_{x\to x_0}\lim_{n\to\infty}f_n(x)=\lim_{x\to x_0}f(x)=f(x_0).
```
Por otra parte, por la continuidad de $`f_n`$ se tiene $`\lim_{x\to x_0}f_n(x)=f_n(x_0)`$, y $`\lim_{n\to\infty}f_n(x_0)=f(x_0)`$, ya que la convergencia uniforme implica la puntual. Así,
```math
\lim_{n\to\infty}\lim_{x\to x_0}f_n(x)=\lim_{n\to\infty}f_n(x_0)=f(x_0).
```
Los [límites iterados](lecture-57-58.md#def-5-4-2) coinciden. $`\square`$

<a id="p036"></a>

### Paso al límite bajo el signo integral

<a id="thm-8-2-2"></a>**Teorema 8.2.2 (paso al límite bajo el signo integral).** Supongamos que

1. $`f_n\in C([a,b])`$ para todo $`n`$;
2. $`f_n\rightrightarrows f`$ en $`[a,b]`$.

Entonces $`\int_a^bf_n(x)\,dx\to\int_a^bf(x)\,dx`$ cuando $`n\to\infty`$, o bien
```math
\lim_{n\to\infty}\int_a^bf_n(x)\,dx=\int_a^b\Bigl(\lim_{n\to\infty}f_n(x)\Bigr)dx .
```

**Demostración.** Por el [teorema 8.2.1](#thm-8-2-1) $`f\in C([a,b])`$; en particular, $`f`$ es integrable en $`[a,b]`$. Tenemos
```math
\Bigl|\int_a^bf_n-\int_a^bf\Bigr|=\Bigl|\int_a^b(f_n-f)\Bigr|\le\int_a^b|f_n-f| .
```
Si $`|f_n-f|<\varepsilon`$ en todo $`[a,b]`$, la última integral es menor que $`\varepsilon(b-a)`$; por eso conviene tomar $`\frac{\varepsilon}{b-a}`$ en lugar de $`\varepsilon`$. Por hipótesis $`f_n\rightrightarrows f`$ en $`[a,b]`$, es decir, para todo $`\varepsilon>0`$ existe $`N`$ tal que $`|f_n(x)-f(x)|<\frac{\varepsilon}{b-a}`$ para todo $`n>N`$ y todo $`x\in[a,b]`$. Entonces, para $`n>N`$
```math
\Bigl|\int_a^bf_n-\int_a^bf\Bigr|\le\int_a^b|f_n-f|<\int_a^b\frac{\varepsilon}{b-a}\,dx=\frac{\varepsilon}{b-a}\,(b-a)=\varepsilon ,
```
es decir, $`\int_a^bf_n\to\int_a^bf`$ cuando $`n\to\infty`$. $`\square`$

**Observación.** En la demostración del [teorema 8.2.2](#thm-8-2-2) fue importante no solo la convergencia puntual, sino la uniforme. Los ejemplos siguientes muestran que la convergencia puntual sola no basta.

**Ejemplo 1.** $`f_n(x)=n^2x(1-x^2)^n`$, $`x\in[0,1]`$. Para cada $`x\in[0,1]`$ se tiene $`f_n(x)\to0`$ cuando $`n\to\infty`$, es decir, la sucesión $`(f_n)`$ converge puntualmente a $`0`$ en $`[0,1]`$. Al mismo tiempo
```math
\begin{aligned}
\int_0^1f_n&=n^2\int_0^1x(1-x^2)^n\,dx=\frac{n^2}{2}\int_0^1(1-x^2)^n\,d(x^2)=-\frac{n^2}{2}\cdot\frac{(1-x^2)^{n+1}}{n+1}\bigg|_0^1\\
&=\frac{n^2}{2(n+1)}\xrightarrow[n\to\infty]{}+\infty ,
\end{aligned}
```
mientras que la integral de la función límite vale $`0`$. La contradicción con la conclusión del [teorema 8.2.2](#thm-8-2-2) muestra que la convergencia $`f_n\to0`$ en $`[0,1]`$ no es uniforme.

<a id="p037"></a>

**Ejemplo 2.** $`f_n(x)=nx(1-x^2)^n`$, $`x\in[0,1]`$. La sucesión $`(f_n)`$ converge puntualmente a $`0`$ en $`[0,1]`$, pero
```math
\int_0^1f_n=n\int_0^1x(1-x^2)^n\,dx=\frac{n}{2(n+1)}\xrightarrow[n\to\infty]{}\frac12\ne0 .
```
Aquí las integrales tienen límite finito, pero no igual a la integral de la función límite.

**Ejemplo 3.** $`f_n(x)=x^n`$ en $`[0,1]`$. La función límite es
```math
f(x)=\begin{cases}0,&x\in[0,1),\\1,&x=1.\end{cases}
```
Como $`|f_n(x)-f(x)|=x^n`$ para $`x\in[0,1)`$ y $`|f_n(1)-f(1)|=0`$,
```math
\sup_{[0,1]}|f_n-f|=\sup_{x\in[0,1)}x^n=1\not\to0 ,
```
es decir, $`\rho(f_n,f)\not\to0`$, y la convergencia en $`[0,1]`$ no es uniforme. Pero para todo $`q\in(0,1)`$
```math
\sup_{[0,q]}|f_n-f|=\sup_{[0,q]}x^n=q^n\xrightarrow[n\to\infty]{}0 ,
```
por lo que $`f_n\rightrightarrows0`$ en $`[0,q]`$.

**Ejemplo 4.** $`f_n:[0,1]\to\mathbb R`$, $`f_n(0)=0`$, $`f_n(x)=0`$ para $`x>\frac1n`$, mientras que en el intervalo $`\left(0,\frac1n\right)`$ la función es positiva: su gráfica es un «diente», un triángulo de base $`\left[0,\frac1n\right]`$ y vértice de altura $`n`$.

*Figura de los apuntes (pág. p037): ejes de coordenadas, un «diente» triangular sobre el segmento $`[0,1/n]`$; en el eje de ordenadas se marca la altura del vértice $`n`$.*

> **Restaurado** (a partir de la figura; en la transcripción no se lee el valor en $`(0,1/n)`$, el profesor escribió «$`>0`$, $`0<x<1/n`$», M3S p72). Fórmula explícita del «diente» con vértice en el punto $`\frac1{2n}`$:
> ```math
> f_n(x)=\begin{cases}2n^2x,&0\le x\le\frac1{2n},\\ 2n-2n^2x,&\frac1{2n}\le x\le\frac1n,\\ 0,&\frac1n\le x\le1;\end{cases}
> ```
> todas las $`f_n`$ son continuas en $`[0,1]`$.

El final del ejemplo 4 está escrito en el cuaderno después del [teorema 8.2.3](#thm-8-2-3) (pág. p039) y se reproduce más abajo en su lugar.

<a id="p038"></a>

### Derivación de la función límite

<a id="thm-8-2-3"></a>**Teorema 8.2.3 (derivación de la función límite).** Supongamos que

1. $`f_n\in C^1([a,b])`$ para todo $`n`$;
2. $`f_n\to f`$ (puntualmente en $`[a,b]`$) cuando $`n\to\infty`$;
3. $`f\in C^1([a,b])`$;
4. $`f_n'\rightrightarrows\varphi`$ en $`[a,b]`$.

Entonces $`\varphi\in C([a,b])`$ y $`f'=\varphi`$, o bien
```math
\frac{d}{dx}\Bigl(\lim_{n\to\infty}f_n(x)\Bigr)=\lim_{n\to\infty}\Bigl(\frac{d}{dx}f_n(x)\Bigr).
```

> **Corrección de la fuente** (A143). La condición 3 figura tanto en los apuntes como en la diapositiva del curso 2024/25 (FS p65), pero no se usa en la demostración y se deduce de las demás: la demostración muestra que $`f(x)=f(a)+\int_a^x\varphi`$ con $`\varphi`$ continua, de donde $`f\in C^1([a,b])`$. Por tanto, el teorema vale sin la condición 3, y $`f\in C^1([a,b])`$ puede incluirse en la conclusión.

**Demostración.** Por la fórmula de Newton–Leibniz $`\int_a^bf_n'=f_n(b)-f_n(a)`$; sustituyendo $`b`$ por un $`x\in[a,b]`$ arbitrario, obtenemos $`\int_a^xf_n'=f_n(x)-f_n(a)`$, es decir,
```math
f_n(x)=f_n(a)+\int_a^xf_n'(t)\,dt\qquad(x\in[a,b]).
```
Pasemos al límite cuando $`n\to\infty`$: $`f_n(x)\to f(x)`$ y $`f_n(a)\to f(a)`$ por la condición 2, y $`\int_a^xf_n'\to\int_a^x\varphi`$ por el [teorema 8.2.2](#thm-8-2-2) de paso al límite bajo el signo integral (aplicado en el segmento $`[a,x]`$: $`f_n'\in C([a,x])`$, $`f_n'\rightrightarrows\varphi`$ en $`[a,x]`$). Obtenemos
```math
f(x)=f(a)+\int_a^x\varphi(t)\,dt\qquad(x\in[a,b]).
```

> **Restaurado** (según las diapositivas del curso 2024/25, FS p65; en los apuntes la demostración se interrumpe en esta fórmula). La función $`\varphi`$ es continua en $`[a,b]`$ por el [teorema 8.2.1](#thm-8-2-1) (como [límite uniforme de funciones continuas](../10-function-sequences-series.md#uniform-limit-continuity) $`f_n'`$). Por el teorema de Barrow, la integral con límite superior variable de una función continua es derivable y $`\frac{d}{dx}\int_a^x\varphi(t)\,dt=\varphi(x)`$. Por tanto,
> ```math
> f'(x)=\frac{d}{dx}\Bigl(f(a)+\int_a^x\varphi(t)\,dt\Bigr)=\varphi(x),\qquad x\in[a,b],
> ```
> es decir, $`f'=\varphi`$ (y, en consecuencia, $`f\in C^1([a,b])`$). $`\square`$

## §8.3. Series funcionales

<a id="def-8-3-1"></a>**Definición 8.3.1.** Sea dada una sucesión de funciones $`u_n:X\to\mathbb R`$, $`n\in\mathbb N`$. La expresión $`\sum_{n=1}^{\infty}u_n(x)`$ se llama serie funcional. Pongamos
```math
S_n(x)=\sum_{k=1}^{n}u_k(x),\qquad S(x)=\lim_{n\to\infty}S_n(x),\qquad S:X\to\mathbb R .
```
Una serie funcional se llama convergente en el conjunto $`X`$ si converge en cada punto de ese conjunto.

<a id="p039"></a>

**Ejemplo 4 (conclusión).** Volvamos a los «dientes» de §8.2. Para todo $`x>0`$ y todo $`n>\frac1x`$ se tiene $`x>\frac1n`$, es decir, $`f_n(x)=0`$; además, $`f_n(0)=0`$. Por tanto, $`f_n\to0`$ puntualmente en $`[0,1]`$, es decir, $`f=\lim_{n\to\infty}f_n=0`$. Pero (el área del triángulo de base $`\frac1n`$ y altura $`n`$)
```math
\int_0^1f_n(x)\,dx=\frac12\cdot\frac1n\cdot n=\frac12\not\to0,\qquad \int_0^1f(x)\,dx=0 ,
```
es decir, $`\int_0^1f_n\not\to\int_0^1f`$. Por el [teorema 8.2.2](#thm-8-2-2) esto significa que la convergencia $`f_n\to0`$ en $`[0,1]`$ no es uniforme.

> **Restaurado** (según las diapositivas del curso 2024/25, FS p66; cf. los apuntes de 2022, M3S p76–p78). Entre las págs. p039 y p040 el cuaderno perdió la definición de serie uniformemente convergente, la afirmación sobre el resto de la serie, el enunciado del criterio de Bolzano–Cauchy y el comienzo de su demostración (la pág. p040 comienza a mitad de la demostración de la necesidad).
>
> <a id="def-8-3-2"></a>**Definición 8.3.2.** La serie $`\sum_{n=1}^{\infty}u_n(x)`$ se llama uniformemente convergente en el conjunto $`E\subset X`$ si $`S_n\rightrightarrows S`$ en $`E`$.
>
> La función $`r_n(x):=\sum_{k=n+1}^{\infty}u_k(x)=S(x)-S_n(x)`$ se llama resto de la serie funcional; la serie $`\sum_{n=1}^{\infty}u_n(x)`$ converge uniformemente en el conjunto $`E`$ si y solo si $`r_n\rightrightarrows0`$ en $`E`$.
>
> *Criterio de Bolzano–Cauchy (de convergencia uniforme de una serie funcional).* La serie $`\sum_{n=1}^{\infty}u_n(x)`$ converge uniformemente en el conjunto $`E`$ si y solo si
> ```math
> \forall\varepsilon>0\ \ \exists N\ \ \forall n>m>N\ \ \forall x\in E:\quad |S_n(x)-S_m(x)|<\varepsilon .
> ```
>
> **Demostración.** *Necesidad.* Supongamos que la serie converge uniformemente en $`E`$, es decir, $`S_n\rightrightarrows S`$ en $`E`$. Para $`\varepsilon>0`$ existe $`N`$ tal que $`|S_n(x)-S(x)|<\frac\varepsilon2`$ para todo $`x\in E`$ y todo $`n>N`$; en particular, para $`n>m>N`$ también $`|S_m(x)-S(x)|<\frac\varepsilon2`$. Entonces, para todos $`n>m>N`$ y $`x\in E`$

<a id="p040"></a>

```math
|S_n(x)-S_m(x)|=|S_n(x)-S(x)+S(x)-S_m(x)|\le|S_n(x)-S(x)|+|S(x)-S_m(x)|<\frac\varepsilon2+\frac\varepsilon2=\varepsilon .
```

*Suficiencia.* Fijemos $`x\in E`$. Entonces $`(S_n(x))_{n\in\mathbb N}`$ es una [sucesión de Cauchy](lecture-13.md#def-2-3-10) numérica, y por el criterio de Bolzano–Cauchy para sucesiones numéricas existe $`S(x)`$ tal que $`S_n(x)\to S(x)`$. Como el $`x\in E`$ fijado era arbitrario, $`S`$ es una función en $`E`$, y la serie converge a ella puntualmente. Además, por hipótesis, para todo $`\varepsilon>0`$ existe $`N`$ tal que $`|S_n(x)-S_m(x)|<\varepsilon`$ para todo $`x\in E`$ y todo $`n>m>N`$. Hagamos $`n\to\infty`$ en esta desigualdad (paso al límite en una desigualdad): $`|S(x)-S_m(x)|\le\varepsilon<2\varepsilon`$ para todo $`x\in E`$ y todo $`m>N`$. Esto significa precisamente que $`S_m\rightrightarrows S`$ en $`E`$, es decir, la serie converge uniformemente. $`\square`$

Así queda probado el criterio de Bolzano–Cauchy (en los apuntes se escribe después de la demostración): la serie $`\sum_{n=1}^{\infty}u_n(x)`$ converge uniformemente en $`E`$ si y solo si para todo $`\varepsilon>0`$ existe $`N`$ tal que $`|S_n(x)-S_m(x)|<\varepsilon`$ para todo $`n>m>N`$ y todo $`x\in E`$, donde $`S_n(x)=\sum_{k=1}^{n}u_k(x)`$, $`S_m(x)=\sum_{k=1}^{m}u_k(x)`$.

> **Corrección de la fuente** (M509). En el enunciado del criterio de los apuntes falta el [cuantificador](../01-logic-sets-functions.md#sec-1-1) «$`\forall x\in E`$»: «$`\forall\varepsilon>0\ \exists N\ \forall n>m>N\ |S_n(x)-S_m(x)|<\varepsilon`$». Sin él (o si $`N`$ depende de $`x`$) la condición expresa solo la convergencia puntual; el cuantificador se añade, como en la demostración y en la diapositiva FS p66.

Este criterio suele usarse para refutar la convergencia uniforme de una serie.

**Ejemplo.** La serie $`\sum_{k=0}^{\infty}x^k`$ converge a $`\frac1{1-x}`$ en $`[0,1)`$ de forma no uniforme, ya que $`x^k`$ no converge a cero uniformemente en $`[0,1)`$.

> **Restaurado** (según el razonamiento estándar; en los apuntes no se detalla la relación con el criterio). Si la serie $`\sum u_k(x)`$ converge uniformemente en $`E`$, tomando $`n=m+1`$ en el criterio de Bolzano–Cauchy obtenemos $`|u_{m+1}(x)|=|S_{m+1}(x)-S_m(x)|<\varepsilon`$ para todo $`m>N`$ y $`x\in E`$, es decir, $`u_k\rightrightarrows0`$ en $`E`$. Pero aquí $`\sup_{x\in[0,1)}x^k=1`$ para todo $`k`$, de modo que $`x^k`$ no converge a cero uniformemente en $`[0,1)`$, y la serie no puede converger uniformemente.

### Criterio de Weierstrass

Sean dadas una sucesión de funciones $`u_n:X\to\mathbb R`$, $`n\in\mathbb N`$, y una sucesión numérica $`(C_n)_{n\in\mathbb N}`$, $`C_n>0`$, tales que

1. $`|u_n(x)|\le C_n`$ para todo $`x\in E\subset X`$ y todo $`n\in\mathbb N`$;
2. la serie $`\sum_{n=1}^{\infty}C_n`$ converge.

Entonces la serie $`\sum_{n=1}^{\infty}u_n(x)`$ converge uniformemente en $`E`$.

**Demostración.**

<a id="p041"></a>

Para cualesquiera $`m\in\mathbb N`$, $`p\in\mathbb N`$ y $`x\in E`$, por la condición 1
```math
\Bigl|\sum_{n=m+1}^{m+p}u_n(x)\Bigr|\le\sum_{n=m+1}^{m+p}|u_n(x)|\le\sum_{n=m+1}^{m+p}C_n .
```
Por hipótesis la serie $`\sum C_n`$ converge, por lo que, por el criterio de Bolzano–Cauchy para series numéricas, para todo $`\varepsilon>0`$ existe $`N`$ tal que $`\sum_{n=m+1}^{m+p}C_n<\varepsilon`$ para todo $`m>N`$ y $`p\in\mathbb N`$. Entonces, para todos $`m>N`$, $`p\in\mathbb N`$ y $`x\in E`$
```math
|S_{m+p}(x)-S_m(x)|=\Bigl|\sum_{k=m+1}^{m+p}u_k(x)\Bigr|\le\sum_{k=m+1}^{m+p}C_k<\varepsilon .
```
Observemos que aquí, en el criterio de Bolzano–Cauchy, $`n=m+p`$ (todo $`n>m>N`$ tiene esa forma). Por el criterio de Bolzano–Cauchy para series funcionales, la serie $`\sum_{n=1}^{\infty}u_n(x)`$ converge uniformemente en $`E`$. $`\square`$

> **Corrección de la fuente** (M510). En los apuntes la última estimación figura como «$`\left|\sum_{n=m+1}^{m+p}u_n(x)\right|\le\left|\sum_{k=m+1}^{m+p}u_k(x)\right|<\varepsilon`$»: a ambos lados está la misma suma y falta el eslabón necesario (la comparación con $`\sum C_k`$); corregido según la nota del profesor (FS p67). Además, en el margen figura «$`p>1`$» en lugar de $`p\in\mathbb N`$ ($`p\ge1`$).

**Ejemplos.** Las series $`\sum_{k=1}^{\infty}\frac{\sin kx}{k^2}`$ y $`\sum_{k=1}^{\infty}\frac{\cos kx}{k^2}`$ convergen uniformemente en $`\mathbb R`$ por el criterio de Weierstrass, ya que para todo $`x\in\mathbb R`$ ($`E=\mathbb R`$)
```math
\left|\frac{\sin kx}{k^2}\right|\le\frac1{k^2},\qquad \left|\frac{\cos kx}{k^2}\right|\le\frac1{k^2},
```
y la serie $`\sum\frac1{k^2}`$ converge.

**Observación.** Bajo las hipótesis del criterio de Weierstrass la serie $`\sum_{k=1}^{\infty}u_k(x)`$ converge en $`E`$ no solo uniformemente, sino también absolutamente. Más aún, la serie $`\sum_{k=1}^{\infty}|u_k(x)|`$ también converge uniformemente en $`E`$, ya que cumple las hipótesis del criterio de Weierstrass (con los mismos $`C_k`$).

**Observación.** La convergencia uniforme y la absoluta no se implican mutuamente.

1. Hay series que convergen absolutamente pero no uniformemente. Por ejemplo, $`\sum_{k=0}^{\infty}x^k`$ en $`(-1,1)`$.
2. Hay series que convergen uniformemente pero no absolutamente. Por ejemplo, cualquier serie numérica condicionalmente convergente considerada como funcional (con términos constantes).

### Continuidad de la suma de una serie uniformemente convergente

<a id="thm-8-3-1"></a>**Teorema 8.3.1.** Sean dadas una serie de funciones $`u_n\in C([a,b])`$, $`n\in\mathbb N`$, y $`\sum_{n=1}^{\infty}u_n(x)=S(x)`$. Si la serie $`\sum_{n=1}^{\infty}u_n(x)`$ converge uniformemente en $`[a,b]`$, entonces $`S\in C([a,b])`$.

**Demostración.** Las sumas parciales $`S_n(x)=u_1(x)+u_2(x)+\dots+u_n(x)`$ son continuas en $`[a,b]`$ como sumas finitas de funciones continuas: $`S_n\in C([a,b])`$ para todo $`n\in\mathbb N`$. Además, $`S(x)=\lim_{n\to\infty}S_n(x)`$ para todo $`x\in[a,b]`$. Por hipótesis la serie $`\sum_{k=1}^{\infty}u_k(x)`$ converge uniformemente en $`[a,b]`$, es decir, $`S_n\rightrightarrows S`$ en $`[a,b]`$. Por el [teorema 8.2.1](#thm-8-2-1) (continuidad de la función límite) $`S\in C([a,b])`$. $`\square`$

## Referencias cruzadas

- Tema en el curso: [capítulo 10 «Sucesiones y series de funciones»](../10-function-sequences-series.md) — [§10.1 «Dos tipos de convergencia»](../10-function-sequences-series.md#sec-10-1), [§10.2 «Criterio uniforme de Cauchy»](../10-function-sequences-series.md#sec-10-2), [criterio de Weierstrass](../10-function-sequences-series.md#weierstrass-m-test), [§10.3 «Continuidad e integración»](../10-function-sequences-series.md#sec-10-3), [§10.4 «Derivación»](../10-function-sequences-series.md#sec-10-4).
- Reordenaciones de series: las [definiciones 7.5.1](lecture-69-70.md#def-7-5-1) y [7.5.2](lecture-69-70.md#def-7-5-2), el criterio de Leibniz y la suma de la serie $`\sum\frac{(-1)^{k-1}}{k}=\ln2`$ — [lecciones 69–70](lecture-69-70.md); [reordenaciones de los términos de una serie](../04-numeric-series.md#rearrangement-warning) en el capítulo 4.
- Hechos usados: [teorema 2.3.7](lecture-13.md#thm-2-3-7), el criterio de Bolzano–Cauchy para sucesiones; [teorema 4.3.2](lecture-43-44.md#thm-4-3-2), la fórmula de Newton–Leibniz; el teorema de Barrow — [lecciones 43–44](lecture-43-44.md).
- Continuación de §8.3 (integración y derivación término a término de series, [series de potencias](../11-power-series.md#sec-11-1)): [lecciones 73–74](../../ru/lectures-2025-26/lecture-73-74.md).

---

[← Lecciones 69–70](lecture-69-70.md) · [Índice de lecciones](index.md) · [Términos y teoremas](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-71-72.md) · [English](../../en/lectures-2025-26/lecture-71-72.md)
