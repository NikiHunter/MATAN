---
title: "Lecciones 75–76 — integración y derivación de series de potencias, serie de Taylor, integrales dependientes de un parámetro"
lang: es
course: "Análisis matemático, 2025/26"
lecture: 75-76
semester: 3
source: "cuaderno manuscrito, págs. p050–p057"
source_pages: "p050, p051, p052, p053, p054, p055, p056, p057"
course_chapter: 24
---
# Lecciones 75–76 — integración y derivación de series de potencias, serie de Taylor, integrales dependientes de un parámetro

[← Lecciones 73–74](lecture-73-74.md) · [Índice de lecciones](index.md) · [Lecciones 77–78 →](lecture-77-78.md) · [Términos y teoremas](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-75-76.md) · [English](../../en/lectures-2025-26/lecture-75-76.md)

> **Fuente y numeración.** Los apuntes se copiaron de un cuaderno manuscrito (págs. p050–p057; el texto bruto de las páginas está en [`ocr/raw/`](../../../ocr/raw/p050.md)). La pág. p050 comienza con un ejemplo de la [fórmula de Cauchy–Hadamard](../11-power-series.md#sec-11-1) que completa la clase anterior; al lado, en el margen y en rojo, figuran el título «Lecciones 75–76» y el plan de la clase, leído solo en parte (integración de series de potencias; radios, series de potencias y serie de Taylor, funciones analíticas; el tercer punto es ilegible), y en un recuadro la nota «80 (15 oct)» (al parecer, un número de página y la fecha de la clase). Los coeficientes de las series de potencias, denotados $`C_k`$ en el cuaderno, se denotan aquí $`c_k`$, como en las diapositivas del profesor. La numeración de definiciones y teoremas es la del profesor. Los lapsus de los apuntes se corrigen y se marcan con bloques «Corrección de la fuente»; los pasajes perdidos se restauran y se marcan con bloques «Restaurado»; las etiquetas corresponden a [`ocr/RESOLVED.md`](../../../ocr/RESOLVED.md). Los lugares que aún hay que cotejar con el cuaderno se enumeran en [`ocr/ISSUES.md`](../../../ocr/ISSUES.md).

## §8.4. Series de potencias (conclusión)

<a id="p050"></a>

**Ejemplo (de la fórmula de Cauchy–Hadamard).** Consideremos la serie $`\sum_{n=0}^{\infty}c_nx^n`$, donde $`c_{2n+1}=0`$, $`c_{2n}=1`$, es decir,
```math
\sum_{n=0}^{\infty}c_nx^n=1+x^2+x^4+x^6+\dots
```
La sucesión $`\sqrt[n]{|c_n|}`$ ($`n\ge1`$) vale $`0`$ para $`n`$ impar y $`1`$ para $`n`$ par:
```math
\lim_{n\to\infty}\sqrt[2n+1]{|c_{2n+1}|}=0,\qquad \lim_{n\to\infty}\sqrt[2n]{|c_{2n}|}=1 .
```
Sus [límites parciales](lecture-11-12.md#def-2-3-8) son $`0`$ y $`1`$; el límite $`\lim\sqrt[n]{|c_n|}`$ no existe, y $`\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}=1`$. Por la fórmula de Cauchy–Hadamard ([teorema 8.4.1](lecture-73-74.md#thm-8-4-1)) $`R=1`$. Esto concuerda con el cálculo directo: para $`|x|<1`$ la serie es una progresión geométrica de razón $`x^2`$, y $`1+x^2+x^4+\dots=\frac1{1-x^2}`$, mientras que para $`|x|\ge1`$ el término general $`x^{2n}`$ no tiende a cero, y la serie diverge.

> **Corrección de la fuente** (M202, U203). En los apuntes: «$`\lim_{n\to\infty}S_n=\lim_{n\to\infty}S_{n+1}=0\Rightarrow R=\infty`$», y luego «$`\lim_{n\to\infty}S_n=\lim_{n\to\infty}S_{2n}=\ldots`$» (aquí $`S_n`$ denota $`\sqrt[n]{|c_n|}`$). La [subsucesión](lecture-11-12.md#def-2-3-7) de índices impares tiende efectivamente a $`0`$, pero en la fórmula de Cauchy–Hadamard figura el [límite superior](lecture-13.md#def-2-3-9), es decir, el mayor límite parcial; vale $`1`$ (sobre los índices pares). Por eso $`\varlimsup\sqrt[n]{|c_n|}=1`$ y $`R=1`$, y no $`\infty`$: por ejemplo, para $`x=1`$ la serie $`1+1+1+\dots`$ diverge.

### Integración de series de potencias

<a id="thm-8-4-4"></a>**Teorema 8.4.4 (integración de series de potencias).** Sean dada una serie de potencias $`\sum_{k=0}^{\infty}c_k(x-a)^k`$ y $`R\in(0,+\infty]`$ su radio de convergencia. Entonces la serie de potencias puede integrarse término a término sobre cualquier segmento contenido en el intervalo de convergencia: si $`[A,B]\subset(a-R,a+R)`$, entonces
```math
\int_A^B\sum_{k=0}^{\infty}c_k(x-a)^k\,dx=\sum_{k=0}^{\infty}c_k\,\frac{(B-a)^{k+1}-(A-a)^{k+1}}{k+1}.\qquad\qquad(8.4.2)
```
Si, además, $`R<+\infty`$ y la serie de potencias converge para $`x=a+R`$ (respectivamente para $`x=a-R`$), la igualdad (8.4.2) vale también para $`B=a+R`$ (respectivamente para $`A=a-R`$); si la serie converge en ambos extremos, (8.4.2) vale también para el segmento $`[a-R,a+R]`$.

**Demostración.** Sin pérdida de generalidad $`a=0`$ ([observación 8.4.2](lecture-73-74.md#rem-8-4-2)). Denotemos $`r=\max\{|A|,|B|\}`$. Entonces $`r<R`$ y
```math
[A,B]\subset[-r,r]\subset(-R,R).
```
Por el [teorema 8.4.2](lecture-73-74.md#thm-8-4-2) la serie $`\sum c_kx^k`$ [converge uniformemente](../10-function-sequences-series.md#sec-10-1) en $`[-r,r]`$ y, por tanto, también en $`[A,B]`$. Sus términos $`c_kx^k`$ son continuos, así que por el [teorema 8.3.2](lecture-73-74.md#thm-8-3-2) (integración término a término) la serie puede integrarse término a término sobre $`[A,B]`$:
```math
\int_A^B\sum_{k=0}^{\infty}c_kx^k\,dx=\sum_{k=0}^{\infty}c_k\int_A^Bx^k\,dx=\sum_{k=0}^{\infty}c_k\,\frac{B^{k+1}-A^{k+1}}{k+1}.
```

<a id="p051"></a>

Sean ahora $`R<+\infty`$, la serie convergente para $`x=R`$, $`B=R`$ y $`A\in(-R,R)`$. Por el [teorema de Abel](../11-power-series.md#abel-theorem) ([teorema 8.4.3](lecture-73-74.md#thm-8-4-3)) la serie $`\sum c_kx^k`$ converge uniformemente en $`[0,R]`$. Si $`A<0`$, además, por el [teorema 8.4.2](lecture-73-74.md#thm-8-4-2) (con $`r=|A|<R`$) la serie converge uniformemente en $`[A,0]`$. Una serie que converge uniformemente en cada uno de dos segmentos converge uniformemente en su unión (basta tomar el mayor de los dos índices $`N`$ en la definición de convergencia uniforme); por tanto, la serie converge uniformemente en $`[A,R]`$, y por el [teorema 8.3.2](lecture-73-74.md#thm-8-3-2) puede integrarse término a término sobre $`[A,R]`$, lo que da (8.4.2) para $`B=R`$. El caso $`A=-R`$ se trata de forma análoga (con convergencia uniforme en $`[-R,0]`$ por el teorema de Abel), y si la serie converge en ambos extremos, converge uniformemente en $`[-R,0]`$ y en $`[0,R]`$, es decir, en $`[-R,R]`$. $`\square`$

> **Corrección de la fuente** (S209, S210). En los apuntes, tras «$`\sum C_kx^k`$ conv. unif. en $`[-r,r]`$ (por el t. 8.4.2)», la integración término a término también se justifica con la referencia «(por el t. 8.4.2)»; se deduce del [teorema 8.3.2](lecture-73-74.md#thm-8-3-2) de integración término a término. En el caso $`B=R`$ se escribe «por el t. (8.4.2) la serie … conv. unif. en $`[A,B]=[-r,r]`$», pero el [teorema 8.4.2](lecture-73-74.md#thm-8-4-2) da convergencia uniforme solo en un segmento $`[A,0]`$ contenido en el interior del intervalo de convergencia; en $`[0,R]`$ se deduce del teorema de Abel (así en la nota del profesor, FS p77).

### Radios de convergencia de la serie derivada y de la integrada

<a id="thm-8-4-5"></a>**Teorema 8.4.5 (sobre los radios de las series de potencias).** Los radios de convergencia de las series de potencias
```math
\sum_{k=0}^{\infty}c_k(x-a)^k,\qquad \sum_{k=1}^{\infty}kc_k(x-a)^{k-1},\qquad \sum_{k=0}^{\infty}\frac{c_k}{k+1}(x-a)^{k+1}
```
son iguales. (La segunda serie se obtiene de la primera derivando término a término; la tercera, integrando término a término de $`a`$ a $`x`$.)

**Demostración.** Probemos que coinciden los radios de convergencia de las dos primeras series. Para $`x\ne a`$ la serie $`\sum_{k=1}^{\infty}kc_k(x-a)^{k-1}`$ converge si y solo si converge la serie $`\sum_{k=1}^{\infty}kc_k(x-a)^k`$ (sus términos difieren en el factor constante $`x-a\ne0`$), por lo que los radios de convergencia de estas dos series coinciden; el coeficiente de la segunda de ellas en $`(x-a)^n`$ es $`nc_n`$. Por la fórmula de Cauchy–Hadamard basta comprobar la igualdad
```math
\varlimsup_{n\to\infty}\sqrt[n]{n|c_n|}=\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}.
```
Fijemos un $`\varepsilon>0`$ arbitrario. Como $`\sqrt[n]n\to1`$, existe $`N`$ tal que $`\sqrt[n]n\le1+\varepsilon`$ para todo $`n>N`$, es decir, $`n\le(1+\varepsilon)^n`$, y entonces
```math
\sqrt[n]{|c_n|}\le\sqrt[n]{n|c_n|}\le\sqrt[n]{(1+\varepsilon)^n|c_n|}=(1+\varepsilon)\sqrt[n]{|c_n|}\qquad(n>N).
```
Pasando a los límites superiores (una desigualdad entre los términos de sucesiones para $`n>N`$ se conserva para los límites superiores, y el factor positivo $`1+\varepsilon`$ sale del límite superior), obtenemos
```math
\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}\le\varlimsup_{n\to\infty}\sqrt[n]{n|c_n|}\le(1+\varepsilon)\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}.
```
Como $`\varepsilon>0`$ es arbitrario, los límites superiores son iguales (también cuando valen $`0`$ o $`+\infty`$), y los radios de convergencia de las dos primeras series coinciden.

La coincidencia de los radios de convergencia de la primera y la tercera series se comprueba de modo análogo: para $`x\ne a`$ la tercera serie converge a la vez que la serie $`\sum_{k=0}^{\infty}\frac{c_k}{k+1}(x-a)^k`$, y como $`\sqrt[n]{n+1}\to1`$, para todo $`n`$ suficientemente grande
```math
\frac1{1+\varepsilon}\sqrt[n]{|c_n|}\le\sqrt[n]{\frac{|c_n|}{n+1}}\le\sqrt[n]{|c_n|}.
```
$`\square`$

> **Corrección de la fuente** (T212, U213, M214). En los apuntes, como en la fórmula de Cauchy–Hadamard (lecciones 73–74), figuran límites ordinarios en lugar de superiores, y la cadena final se escribe «$`\lim\sqrt[n]{|nC_n|}\le\lim\sqrt[n]{|C_n|}\le(1+\varepsilon)\lim\sqrt[n]{|C_n|}`$», con los dos primeros miembros intercambiados. Lo correcto es $`\varlimsup\sqrt[n]{|c_n|}\le\varlimsup\sqrt[n]{n|c_n|}\le(1+\varepsilon)\varlimsup\sqrt[n]{|c_n|}`$ (FS p78). La línea «$`\forall\varepsilon>0`$, $`\exists k\in\mathbb N`$: $`k>1`$, por $`\exists N:\forall n>N`$» se lee como «fijemos $`\varepsilon>0`$; como $`\sqrt[n]n\to1`$, existe $`N`$ tal que para todo $`n>N`$…».

> **Restaurado** (aclaración del enunciado, según la exposición estándar). El [teorema 8.4.5](#thm-8-4-5) afirma solo la igualdad de los radios; el comportamiento de las tres series en los extremos del intervalo de convergencia puede ser distinto. Por ejemplo, la serie $`\sum_{k=1}^{\infty}\frac{x^k}{k^2}`$ ($`R=1`$) converge para $`x=1`$, mientras que la serie [derivada](lecture-22-23.md#def-3-1-1) $`\sum_{k=1}^{\infty}\frac{x^{k-1}}{k}`$ se convierte en la serie armónica para $`x=1`$ y diverge.

### Derivación de series de potencias

<a id="thm-8-4-6"></a>**Teorema 8.4.6 (derivación de series de potencias).** Sea $`R\in(0,+\infty]`$ el radio de convergencia de la serie
```math
f(x)=\sum_{k=0}^{\infty}c_k(x-a)^k .
```
Entonces la función $`f`$ es infinitamente [derivable](lecture-22-23.md#def-3-2-1) en el conjunto $`|x-a|<R`$, y la serie puede derivarse término a término cualquier número de veces:
```math
f^{(m)}(x)=\sum_{k=m}^{\infty}k(k-1)\dots(k-m+1)\,c_k(x-a)^{k-m},\qquad |x-a|<R,\quad m\in\mathbb N .
```

**Demostración.** Sin pérdida de generalidad $`a=0`$. Por el [teorema 8.4.5](#thm-8-4-5) la derivación término a término no cambia el radio de convergencia: la serie $`\sum_{k=1}^{\infty}kc_kx^{k-1}`$ tiene de nuevo radio de convergencia $`R`$. Por eso basta probar la afirmación para $`m=1`$: el caso general se obtiene aplicando el caso $`m=1`$ sucesivamente a las series de $`f',f'',\dots`$ ([inducción](../01-logic-sets-functions.md#example-induction) sobre $`m`$).

<a id="p052"></a>

Así pues, $`f(x)=\sum_{k=0}^{\infty}c_kx^k`$, $`|x|<R`$. Consideremos un punto $`x_1\in(-R,R)`$ y probemos que $`f`$ es derivable en $`x_1`$ y $`f'(x_1)=\sum_{k=1}^{\infty}kc_kx_1^{k-1}`$. Fijemos un número $`\rho`$ tal que $`|x_1|<\rho<R`$, y sean $`|x|\le\rho`$, $`x\ne x_1`$. Entonces
```math
\frac{f(x)-f(x_1)}{x-x_1}=\sum_{k=1}^{\infty}c_k\,\frac{x^k-x_1^k}{x-x_1}=\sum_{k=1}^{\infty}c_k\bigl(x^{k-1}+x^{k-2}x_1+\dots+xx_1^{k-2}+x_1^{k-1}\bigr).
```
Denotemos $`\psi_k(x):=c_k\bigl(x^{k-1}+x^{k-2}x_1+\dots+x_1^{k-1}\bigr)`$: son polinomios, es decir, funciones continuas. Para $`|x|\le\rho`$ cada uno de los $`k`$ sumandos del paréntesis es, en valor absoluto, a lo sumo $`\rho^{k-1}`$, por lo que
```math
|\psi_k(x)|=\bigl|c_k\bigl(x^{k-1}+x^{k-2}x_1+\dots+x_1^{k-1}\bigr)\bigr|\le k|c_k|\rho^{k-1}\qquad(|x|\le\rho).
```
Como $`\rho<R`$, y la serie $`\sum kc_kx^{k-1}`$ tiene radio de convergencia $`R`$ por el [teorema 8.4.5](#thm-8-4-5), en el punto $`x=\rho`$ [converge absolutamente](../04-numeric-series.md#sec-4-3) (una serie de potencias converge absolutamente en su intervalo de convergencia, [observación 8.4.1](lecture-73-74.md#rem-8-4-1)), es decir, la serie $`\sum_{k=1}^{\infty}k|c_k|\rho^{k-1}`$ converge. Por el [criterio de Weierstrass](../10-function-sequences-series.md#weierstrass-m-test) la serie $`\sum_{k=1}^{\infty}\psi_k(x)`$ converge uniformemente en $`[-\rho,\rho]`$ (con mayor razón en $`[-\rho,\rho]\setminus\{x_1\}`$), y por el [teorema 8.3.1](lecture-71-72.md#thm-8-3-1) su suma $`\Psi(x)`$ es continua en $`[-\rho,\rho]`$. Para $`x\ne x_1`$ se tiene $`\Psi(x)=\frac{f(x)-f(x_1)}{x-x_1}`$, y $`\psi_k(x_1)=kc_kx_1^{k-1}`$. Por tanto (paso al límite término a término),
```math
\lim_{x\to x_1}\frac{f(x)-f(x_1)}{x-x_1}=\lim_{x\to x_1}\Psi(x)=\Psi(x_1)=\sum_{k=1}^{\infty}\lim_{x\to x_1}c_k\bigl(x^{k-1}+x^{k-2}x_1+\dots+x_1^{k-1}\bigr)=\sum_{k=1}^{\infty}kc_kx_1^{k-1}.
```
Como $`x_1`$ es cualquier punto del intervalo $`(-R,R)`$, la función $`f`$ es derivable en $`(-R,R)`$, y la serie puede derivarse término a término. $`\square`$

> **Corrección de la fuente** (M218, S220). En los apuntes la estimación de un término de la serie se escribe como continuación de la igualdad («$`=\left|C_k\left(x^{k-1}+x^{k-2}x_1+\ldots+x_1^{k-1}\right)\right|\le k|C_k|\rho^{k-1}`$»), cuando es una estimación aparte de cada término. La convergencia uniforme se escribe «para $`(-\rho,\rho)`$, con mayor razón $`\forall(-S,S)\times(x_1)`$», es decir, en $`(-\rho,\rho)`$ y con mayor razón en $`(-\rho,\rho)\setminus\{x_1\}`$; aquí se obtiene en el segmento $`[-\rho,\rho]`$, lo que permite remitir al [teorema 8.3.1](lecture-71-72.md#thm-8-3-1).

### Unicidad del desarrollo de una función en serie de potencias

<a id="thm-8-4-7"></a>**Teorema 8.4.7 (unicidad del desarrollo de una función en serie de potencias).** Sean $`a\in\mathbb R`$ y $`R\in(0,+\infty]`$ el radio de convergencia de la serie
```math
f(x)=\sum_{k=0}^{\infty}c_k(x-a)^k .
```
Entonces $`f\in C^\infty(a-R,a+R)`$, y los coeficientes $`c_k`$ se determinan de manera única por la fórmula
```math
c_k=\frac{f^{(k)}(a)}{k!} .
```

**Demostración.** Por el [teorema 8.4.6](#thm-8-4-6) la función $`f`$ es infinitamente derivable en $`(a-R,a+R)`$ (cada una de sus derivadas es derivable y, por tanto, continua, es decir, $`f\in C^\infty(a-R,a+R)`$) y
```math
f^{(m)}(x)=\sum_{k=m}^{\infty}k(k-1)\dots(k-m+1)\,c_k(x-a)^{k-m}\qquad\forall m\in\mathbb N,\ |x-a|<R .
```
Sustituyamos $`x=a`$:
```math
f^{(m)}(a)=m(m-1)\dots(m-m+1)\,c_m+\sum_{k=m+1}^{\infty}k(k-1)\dots(k-m+1)\,c_k(a-a)^{k-m}=m!\,c_m ,
```
ya que todos los términos de la suma con $`k\ge m+1`$ son nulos. Por tanto, $`f^{(m)}(a)=m!\,c_m`$, es decir, $`c_m=\frac{f^{(m)}(a)}{m!}`$; para $`m=0`$ la sustitución $`x=a`$ en la propia serie da $`c_0=f(a)`$. Los coeficientes se expresan mediante la propia función $`f`$, por lo que dos series de potencias de centro $`a`$ cuyas sumas coinciden en algún entorno del punto $`a`$ tienen los mismos coeficientes. $`\square`$

> **Corrección de la fuente** (T222, M223). En los apuntes falta el factor $`c_k`$ en la suma tras la sustitución, y la conclusión se escribe «$`\Rightarrow f^{(m)}(a)+m!C_m\Rightarrow C_m=\frac{f^{(m)}(a)}{m!}`$»; debe ser $`f^{(m)}(a)=m!\,c_m`$ (FS p80).

<a id="p053"></a>

### La serie de Taylor

<a id="def-8-4-3"></a>**Definición 8.4.3.** Supongamos que $`f`$ tiene derivadas de todos los órdenes en el punto $`a`$. Los números $`c_k=\frac{f^{(k)}(a)}{k!}`$ se llaman coeficientes de Taylor, y la serie
```math
\sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k
```
se llama serie de Taylor de la función $`f`$ con centro en el punto $`a`$. La serie de Taylor con centro en cero se llama [serie de Maclaurin](../07-taylor-convexity.md#sec-7-3).

### Representación de funciones mediante series de potencias reales

De los [teoremas 8.4.6](#thm-8-4-6) y [8.4.7](#thm-8-4-7) se deduce que, si una función se desarrolla en serie de potencias en un entorno del punto $`a`$, entonces es infinitamente derivable en ese entorno y la serie es su serie de Taylor.

Sean $`a\in\mathbb R`$, $`R\in(0,+\infty]`$, $`f\in C^\infty(a-R,a+R)`$. Entonces puede construirse la serie de Taylor de la función $`f`$
```math
\sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k
```
y preguntarse por su comportamiento. Para $`x=a`$ la serie converge a $`f(a)`$. Para $`x\ne a`$ son posibles tres casos:

1. la serie converge a $`f(x)`$;
2. la serie diverge;
3. la serie converge, pero no a $`f(x)`$.

### El polinomio de Taylor

La [suma parcial](../04-numeric-series.md#sec-4-1) de la serie de Taylor
```math
T_{n,f}(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k
```
es el [polinomio de Taylor](lecture-27-28.md#thm-3-6-3). Por la definición de suma de una serie, la convergencia de la serie de Taylor a $`f(x)`$ significa que $`T_{n,f}(x)\to f(x)`$ cuando $`n\to\infty`$, es decir, que el resto $`R_{n,f}(x):=f(x)-T_{n,f}(x)`$ tiende a cero.

<a id="thm-8-4-8"></a>**Teorema 8.4.8 (criterio de desarrollabilidad de una función en serie de Taylor).** Supongamos que

1. $`f\in C^\infty(A,B)`$;
2. $`a,x\in(A,B)`$, $`a\ne x`$;
3. existe $`M\in(0,\infty)`$ tal que $`|f^{(n)}(t)|\le M`$ para todo $`n\in\mathbb N`$ y todo $`t`$ comprendido entre $`a`$ y $`x`$.

<a id="p054"></a>

Entonces
```math
\sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x-a)^k=f(x).
```

> **Corrección de la fuente** (A227). En los apuntes (y en la diapositiva FS p81) la condición 3 se escribe para «$`\forall t\in(x-a,x+a)`$». Este intervalo no tiene relación con el segmento entre $`a`$ y $`x`$ (para $`a=0`$ es incluso vacío). La demostración usa la estimación del resto de la fórmula de Taylor, en la que la derivada se toma en puntos entre $`a`$ y $`x`$, por lo que la condición hace falta precisamente para tales $`t`$ (se cumple, por ejemplo, si $`|f^{(n)}(t)|\le M`$ para todo $`n`$ y todo $`t\in(A,B)`$).

**Demostración.** Por el lema sobre la estimación del resto en la fórmula de Taylor demostrado (mucho) antes ([lema 3.6.2](lecture-29-30.md#lem-3-6-2), lecciones 29–30) tenemos
```math
|f(x)-T_{n,f}(x)|=|R_{n,f}(x)|\le\frac{M|x-a|^{n+1}}{(n+1)!},
```
lo que da la convergencia requerida: $`\frac{q^{n+1}}{(n+1)!}\to0`$ cuando $`n\to\infty`$ para todo $`q\ge0`$ (aquí $`q=|x-a|`$), ya que la serie $`\sum_{n}\frac{q^n}{n!}`$ converge por el [criterio de d'Alembert](../04-numeric-series.md#sec-4-2) ($`\frac{q^{n+1}/(n+1)!}{q^n/n!}=\frac{q}{n+1}\to0`$), y su término general tiende a cero. $`\square`$

### Ejemplo de una función cuya serie de Taylor diverge en todos los puntos salvo el centro

**Ejemplo.** Sea ($`a=0`$)
```math
f(x)=\sum_{n=0}^{\infty}e^{-\sqrt{2^n}}\cos(2^nx),\qquad x\in\mathbb R .
```
Formemos la serie de Taylor de esta función en el punto $`x=0`$. Su término independiente es $`f(0)=\sum_{n=0}^{\infty}e^{-\sqrt{2^n}}`$. Los coeficientes de Taylor $`c_n`$ crecen tan deprisa que la serie de Taylor diverge para todo $`x\ne0`$.

> **Restaurado** (según la demostración estándar; en los apuntes la estimación de los coeficientes solo se esboza: «$`C_n`$ — … $`n!`$»).
>
> *La función $`f`$ es infinitamente derivable.* La derivada de orden $`k`$ del término $`e^{-\sqrt{2^n}}\cos(2^nx)`$ es $`e^{-\sqrt{2^n}}2^{nk}\cos\left(2^nx+\frac{k\pi}{2}\right)`$ y su valor absoluto no supera $`e^{-\sqrt{2^n}}2^{nk}`$. Pongamos $`t_n=\sqrt{2^n}=2^{n/2}`$; entonces $`e^{-\sqrt{2^n}}2^{nk}=t_n^{2k}e^{-t_n}`$. Como $`t^{2k+2}e^{-t}\to0`$ cuando $`t\to+\infty`$, existe una constante $`A_k`$ tal que $`t_n^{2k}e^{-t_n}\le A_kt_n^{-2}=A_k2^{-n}`$, y la serie $`\sum_ne^{-\sqrt{2^n}}2^{nk}`$ converge para cada $`k`$. Por el criterio de Weierstrass todas las series de derivadas convergen uniformemente en $`\mathbb R`$, y por el [teorema 8.3.3](lecture-73-74.md#thm-8-3-3) (aplicado sucesivamente en cualquier segmento) $`f\in C^\infty(\mathbb R)`$, y las derivadas se calculan término a término.
>
> *Los coeficientes de Taylor.* En el punto $`0`$ todas las derivadas de orden impar son nulas, y
> ```math
> f^{(2k)}(0)=(-1)^k\sum_{n=0}^{\infty}e^{-\sqrt{2^n}}\,2^{2nk},\qquad c_{2k}=\frac{f^{(2k)}(0)}{(2k)!}.
> ```
> Todos los sumandos son positivos, por lo que para todo $`n`$ se tiene $`|c_{2k}|\ge\frac{t_n^{4k}e^{-t_n}}{(2k)!}`$. Los números $`t_n=2^{n/2}`$ forman una progresión geométrica de razón $`\sqrt2<2`$, por lo que para cada $`k\in\mathbb N`$ existe $`n`$ con $`k\le t_n\le2k`$. Para tal $`n`$, teniendo en cuenta $`(2k)!\le(2k)^{2k}`$, obtenemos
> ```math
> |c_{2k}|\ge\frac{k^{4k}e^{-2k}}{(2k)^{2k}}=\left(\frac{k}{2e}\right)^{2k},
> ```
> es decir, $`\sqrt[2k]{|c_{2k}|}\ge\frac{k}{2e}\to+\infty`$ cuando $`k\to\infty`$. En consecuencia, $`\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}=+\infty`$, y por la fórmula de Cauchy–Hadamard el radio de convergencia de la serie de Taylor es $`0`$: la serie converge solo para $`x=0`$ (donde su suma vale $`f(0)`$).

### Funciones analíticas

<a id="def-8-4-4"></a>**Definición 8.4.4.** Sean $`-\infty\le A<B\le+\infty`$, $`f:(A,B)\to\mathbb R`$, $`a\in(A,B)`$. La función $`f`$ se llama analítica en el punto $`a`$ si se desarrolla en serie de potencias en algún entorno del punto $`a`$, es decir, si existen números $`r>0`$ y $`c_k\in\mathbb R`$ tales que
```math
f(x)=\sum_{k=0}^{\infty}c_k(x-a)^k,\qquad x\in(a-r,a+r).
```
La función $`f:(A,B)\to\mathbb R`$ se llama analítica en el intervalo $`(A,B)`$ si es analítica en cada punto $`(A,B)`$.

> **Corrección de la fuente** (A233). En los apuntes: «se desarrolla en serie de potencias $`f(x)=\sum C_k(x-a)^k`$, $`x\in(a-r,a+r)`$», sin decir que existen $`r>0`$ y los coeficientes $`c_k`$ (los [cuantificadores](../01-logic-sets-functions.md#sec-1-1) se restauran según la diapositiva FS p82); además, en los apuntes $`-\infty<A<B<+\infty`$, mientras que la diapositiva admite también extremos infinitos del intervalo.

Por los [teoremas 8.4.6](#thm-8-4-6) y [8.4.7](#thm-8-4-7), una función analítica en el punto $`a`$ es infinitamente derivable en un entorno de $`a`$, y su serie de potencias es su serie de Taylor.

## §9.1. Integrales propias dependientes de un parámetro

<a id="p055"></a>

Comienza el capítulo 9 «[Integrales dependientes de un parámetro](#def-9-1-1)». Primero, un ejemplo que muestra qué preguntas surgen al trabajar con tales integrales.

**Ejemplo.** Consideremos
```math
I(y)=\int_0^{+\infty}e^{-xy}\,\frac{\sin x}{x}\,dx,\qquad x\in(0,+\infty),\quad y\in[0,+\infty).
```
Queremos calcular $`I'(y)`$ y después la propia integral. Por ahora no nos ocupamos de la justificación (convergencia uniforme) y derivamos formalmente respecto de $`y`$ bajo el signo integral (paso ❶):
```math
I'(y)=\int_0^{+\infty}\frac{\partial}{\partial y}\Bigl(e^{-xy}\,\frac{\sin x}{x}\Bigr)dx=-\int_0^{+\infty}e^{-xy}\sin x\,dx .
```
Nota en rojo en el margen: «❶ ¡¡El paso hay que justificarlo aparte!! — se hará más adelante».

> **Corrección de la fuente** (T236). En los apuntes la primera integral tiene $`dy`$ en lugar de $`dx`$: la integración es respecto de $`x`$, y la derivación, respecto del parámetro $`y`$.

Paso ❷: para $`y>0`$ calculamos la integral $`J(y):=\int_0^{+\infty}e^{-xy}\sin x\,dx`$ integrando por partes dos veces (los términos de contorno en el infinito se anulan, ya que $`e^{-xy}\to0`$ cuando $`x\to+\infty`$):
```math
\begin{aligned}
-J(y)=\int_0^{+\infty}e^{-xy}\,d\cos x&=e^{-xy}\cos x\Big|_0^{+\infty}-\int_0^{+\infty}\cos x\,de^{-xy}=-1+y\int_0^{+\infty}e^{-xy}\cos x\,dx\\
&=-1+y\Bigl(e^{-xy}\sin x\Big|_0^{+\infty}-\int_0^{+\infty}\sin x\,de^{-xy}\Bigr)=-1+y^2\int_0^{+\infty}e^{-xy}\sin x\,dx=-1+y^2J(y).
\end{aligned}
```

> **Corrección de la fuente** (T520). En los apuntes la primera [integración por partes](lecture-37-38.md#thm-4-1-4) se escribe «$`e^{-xy}\cos x\big|_0^{+\infty}+\int_0^{+\infty}\cos x\,de^{-xy}=-1+\dots`$»: delante de la integral debe ir un signo menos. La expresión final $`-1+y\int_0^{+\infty}e^{-xy}\cos x\,dx`$ de los apuntes es correcta.

Así, $`I'(y)=-J(y)=-1+y^2J(y)`$, de donde $`J(y)(1+y^2)=1`$,
```math
J(y)=\frac{1}{1+y^2},\qquad I'(y)=-\frac{1}{1+y^2}\qquad(y>0).
```
Hemos calculado, pues, $`I'(y)`$. De aquí
```math
I(y)=-\int\frac{dy}{1+y^2}=-\operatorname{arctg}y+C .
```
Hallemos la constante $`C`$. Cuando $`y\to+\infty`$ (de nuevo pasando formalmente al límite bajo el signo integral)
```math
I(y)=\int_0^{+\infty}e^{-xy}\,\frac{\sin x}{x}\,dx\xrightarrow[y\to+\infty]{}\int_0^{+\infty}0\,dx=0 ,
```
por lo que $`-\operatorname{arctg}y+C\to-\frac\pi2+C=0`$, es decir, $`C=\frac\pi2`$ y
```math
I(y)=\frac\pi2-\operatorname{arctg}y .
```
En particular,
```math
I(0)=\int_0^{+\infty}\frac{\sin x}{x}\,dx=\frac\pi2-\operatorname{arctg}0=\frac\pi2 .
```
Nota en rojo al pie de la página: «❶ Lo de arriba hay que justificarlo».

> **Corrección de la fuente** (T239, T521). En los apuntes la [primitiva](lecture-36.md#def-4-1-1) se escribe «$`I'(y)=-\int\frac{dy}{1+y^2}=-\operatorname{arctg}y+C`$»; a la izquierda debe figurar $`I(y)`$. La línea «$`\Rightarrow I(y)=-\int_0^{+\infty}e^{-xy}\frac{\sin x}{x}dx+\int_0^{+\infty}0\,dx=0`$» está deformada; en su sentido es el paso al límite cuando $`y\to+\infty`$: $`I(y)\to\int_0^{+\infty}0\,dx=0`$.

> **Restaurado** (según estimaciones estándar; en los apuntes estos pasos se marcan como pendientes de justificación). El límite cuando $`y\to+\infty`$ se justifica enseguida: como $`\left|\frac{\sin x}{x}\right|\le1`$, para $`y>0`$ se tiene $`|I(y)|\le\int_0^{+\infty}e^{-xy}\,dx=\frac1y\to0`$. Los demás pasos —la derivación bajo el signo de una [integral impropia](lecture-47-48.md#def-4-5-2) (paso ❶) y la igualdad $`I(0)=\lim_{y\to0+}I(y)`$, necesaria porque la fórmula para $`I'(y)`$ se dedujo solo para $`y>0`$ (para $`y=0`$ la integral $`J(0)=\int_0^{+\infty}\sin x\,dx`$ diverge)— requieren la [convergencia uniforme de una integral impropia](lecture-77-78.md#def-9-2-1) respecto de un parámetro y se justificarán más adelante (§9.2).

<a id="p056"></a>

<a id="def-9-1-1"></a>**Definición 9.1.1.** Una integral dependiente de un parámetro es una función de la forma
```math
I(y)=\int_{E_y}f(x,y)\,dx ,
```
donde $`y`$ hace el papel de un parámetro que recorre el conjunto $`Y`$.

**Observación.** Si para cada $`y\in Y`$ la integral $`\int_{E_y}f(x,y)\,dx`$ es propia, la función $`I(y)`$ es una integral propia dependiente de un parámetro.

> **Corrección de la fuente** (T242). En los apuntes (y en la diapositiva FS p83) la integral de la observación se escribe «$`\int f(x,y)\,dy`$»; la integración es respecto de $`x`$, por lo que $`dx`$. La abreviatura «abs.» delante de «propia» se lee como «es».

### Continuidad de una integral respecto de un parámetro

Por ahora suponemos que el conjunto $`E_y`$ no depende de $`y`$.

> **Corrección de la fuente** (T522). El título de este punto en los apuntes es «Derivación de la integral respecto del parámetro $`y`$», pero en él se demuestra la continuidad ([teorema 9.1.1](#thm-9-1-1)); el punto siguiente está dedicado a la derivación. El título se corrige según la diapositiva FS p83 («Sobre la continuidad de una integral respecto de un parámetro»).

<a id="thm-9-1-1"></a>**Teorema 9.1.1.** Sean $`P=\{(x,y)\in\mathbb R^2:\ a\le x\le b,\ c\le y\le d\}`$ y $`f=f(x,y)\in C(P)`$. Entonces la función $`I(y)=\int_a^bf(x,y)\,dx`$ es continua en cada punto $`y\in[c,d]`$, es decir, $`I\in C([c,d])`$.

> **Corrección de la fuente** (T244). En los apuntes la conclusión del teorema dice: «la función $`I(y)=\int_a^bf(x,y)\,dx`$ es integrable $`\forall y\in[c,d]`$». El teorema afirma (y demuestra) la continuidad de $`I`$ en $`[c,d]`$ (así en la diapositiva FS p83); la integrabilidad de $`I`$ respecto de $`[c,d]`$ es una afirmación aparte que se deduce de la continuidad.

*Figura en el margen (pág. p056): el rectángulo $`P`$ en el plano de las variables $`(x,y)`$, con los puntos $`a`$, $`b`$, $`c`$, $`d`$ marcados en los ejes.*

**Demostración.** Tomemos cualquier punto $`y_0\in[c,d]`$. Por la definición de continuidad hay que probar que $`I(y_0)=\lim_{y\to y_0}I(y)`$, es decir, que
```math
I(y_0)=\int_a^bf(x,y_0)\,dx=\lim_{y\to y_0}\int_a^bf(x,y)\,dx=\lim_{y\to y_0}I(y)
```
(los límites se toman sobre $`y\in[c,d]`$).

La función $`f`$ es continua en $`P`$ por hipótesis, y el rectángulo $`P`$ es un [compacto](lecture-57-58.md#def-5-3-7); por el teorema de Cantor $`f`$ es [uniformemente continua](lecture-17-18.md#def-2-5-7) en $`P`$: para todo $`\varepsilon>0`$ existe $`\delta>0`$ tal que $`|f(x',y')-f(x'',y'')|<\varepsilon`$ para cualesquiera puntos $`(x',y'),(x'',y'')\in P`$ cuya distancia sea menor que $`\delta`$. En particular, si $`y\in[c,d]`$ y $`|y-y_0|<\delta`$, entonces
```math
|f(x,y)-f(x,y_0)|<\varepsilon\qquad\forall x\in[a,b],
```
es decir, las funciones $`\varphi_y(x):=f(x,y)`$ convergen a $`\varphi_{y_0}(x)=f(x,y_0)`$ uniformemente en $`[a,b]`$ cuando $`y\to y_0`$: $`\varphi_y\rightrightarrows\varphi_{y_0}`$. Para cada $`y\in[c,d]`$ la función $`\varphi_y`$ es continua respecto de $`x`$ en $`[a,b]`$ y, por tanto, integrable en $`[a,b]`$. Así que puede aplicarse el teorema de paso al límite bajo el signo integral ([teorema 8.2.2](lecture-71-72.md#thm-8-2-2); su demostración se traslada literalmente a un parámetro continuo $`y\to y_0`$): cuando $`|y-y_0|<\delta`$
```math
|I(y)-I(y_0)|\le\int_a^b|f(x,y)-f(x,y_0)|\,dx\le\varepsilon(b-a),
```
es decir, $`I(y)\to I(y_0)`$ cuando $`y\to y_0`$. Como el punto $`y_0\in[c,d]`$ es arbitrario, $`I\in C([c,d])`$. $`\square`$

> **Corrección de la fuente** (M245). En los apuntes el último eslabón de la cadena se escribe «$`\lim\int_a^bf(x,y)\,dx-\lim I(y)`$»; debe ser la igualdad $`\lim_{y\to y_0}\int_a^bf(x,y)\,dx=\lim_{y\to y_0}I(y)`$ (FS p83).

<a id="p057"></a>

### Derivación de una integral respecto de un parámetro

<a id="thm-9-1-2"></a>**Teorema 9.1.2.** Sean $`P=\{(x,y)\in\mathbb R^2:\ a\le x\le b,\ c\le y\le d\}`$, $`f=f(x,y)\in C(P)`$ y $`\frac{\partial f}{\partial y}\in C(P)`$. Entonces la función $`I(y)=\int_a^bf(x,y)\,dx`$ pertenece a $`C^1([c,d])`$ y
```math
I'(y)=\int_a^b\frac{\partial f}{\partial y}(x,y)\,dx .
```
En la diapositiva del profesor esta fórmula se llama fórmula (regla) de Leibniz; una nota en rojo en el margen de los apuntes remite al [teorema 8.2.3](lecture-71-72.md#thm-8-2-3) (derivación de la función límite).

**Demostración.** Tomemos $`y_0\in[c,d]`$ y $`h\ne0`$ tal que $`y_0+h\in[c,d]`$ (en los extremos del segmento la derivada es lateral). Entonces
```math
\frac{I(y_0+h)-I(y_0)}{h}=\frac1h\int_a^b\bigl(f(x,y_0+h)-f(x,y_0)\bigr)\,dx .
```
Para cada $`x\in[a,b]`$ la función $`t\mapsto f(x,t)`$ es derivable en $`[c,d]`$, y por el [teorema de Lagrange](lecture-24-25-26.md#thm-3-4-3)
```math
\frac{f(x,y_0+h)-f(x,y_0)}{h}=\frac{\partial f}{\partial y}(x,y_0+\theta h),\qquad 0<\theta<1
```
(el número $`\theta`$ depende de $`x`$ y de $`h`$). Por tanto,
```math
\begin{aligned}
\left|\frac{I(y_0+h)-I(y_0)}{h}-\int_a^b\frac{\partial f}{\partial y}(x,y_0)\,dx\right|
&=\left|\int_a^b\left[\frac{f(x,y_0+h)-f(x,y_0)}{h}-\frac{\partial f}{\partial y}(x,y_0)\right]dx\right|\\
&\le(b-a)\sup_{x\in[a,b],\ 0<\theta<1}\left|\frac{\partial f}{\partial y}(x,y_0+\theta h)-\frac{\partial f}{\partial y}(x,y_0)\right|=:\varphi(y_0,h).
\end{aligned}
```
Por hipótesis $`\frac{\partial f}{\partial y}\in C(P)`$, y $`P`$ es compacto, así que $`\frac{\partial f}{\partial y}`$ es uniformemente continua en $`P`$, y $`\frac{\partial f}{\partial y}(x,y)\rightrightarrows\frac{\partial f}{\partial y}(x,y_0)`$ en $`[a,b]`$ cuando $`y\to y_0`$: para todo $`\varepsilon>0`$ existe $`\delta>0`$ tal que $`\left|\frac{\partial f}{\partial y}(x,y)-\frac{\partial f}{\partial y}(x,y_0)\right|<\varepsilon`$ para todo $`x\in[a,b]`$ si $`|y-y_0|<\delta`$. Como $`|\theta h|<|h|`$, para $`|h|<\delta`$ obtenemos $`\varphi(y_0,h)\le\varepsilon(b-a)`$. Por tanto, $`\varphi(y_0,h)\to0`$ cuando $`h\to0`$, es decir,
```math
I'(y_0)=\int_a^b\frac{\partial f}{\partial y}(x,y_0)\,dx .
```
$`\square`$

> **Corrección de la fuente** (M251, T253). En los apuntes la estimación se escribe «$`\le\int_a^b\sup\left|\frac{\partial f}{\partial y}(x,y_0+h)-\frac{\partial f}{\partial y}(x,y_0)\right|dx`$»; por el teorema de Lagrange (nota en el margen) la derivada se toma en un punto intermedio $`y_0+\theta h`$, $`0<\theta<1`$, por lo que el [supremo](lecture-11-12.md#def-2-3-1) debe tomarse sobre $`\theta`$ (aquí, a la vez sobre $`x`$ y $`\theta`$, con el factor $`b-a`$, para no discutir la integrabilidad de la función supremo). Al final de la demostración figura «$`\varphi(y_0,h)\xrightarrow[h\to\infty]{}0`$»; debe ser $`h\to0`$.

> **Restaurado** (según la demostración estándar; los apuntes no prueban que $`I'`$ sea continua). La función $`I'(y)=\int_a^b\frac{\partial f}{\partial y}(x,y)\,dx`$ es continua en $`[c,d]`$ por el [teorema 9.1.1](#thm-9-1-1) aplicado a la función $`\frac{\partial f}{\partial y}\in C(P)`$. Por tanto, $`I\in C^1([c,d])`$.

**Ejemplo (ecuación de Bessel).** Comprobemos que para $`n`$ entero la función
```math
u(x)=\int_0^{\pi}\cos(n\varphi-x\sin\varphi)\,d\varphi
```
satisface la ecuación de Bessel
```math
x^2u''+xu'+(x^2-n^2)u=0 .
```
El integrando $`\cos(n\varphi-x\sin\varphi)`$ y sus [derivadas parciales](lecture-61-62.md#def-6-1-5) respecto de $`x`$ de cualquier orden son continuos en cada rectángulo $`[0,\pi]\times[c,d]`$, por lo que, por el [teorema 9.1.2](#thm-9-1-2) (aplicado dos veces; aquí la variable de integración es $`\varphi`$ y el parámetro, $`x`$), $`u\in C^2(\mathbb R)`$, y las derivadas pueden calcularse derivando bajo el signo integral:
```math
u'(x)=\int_0^{\pi}\frac{\partial}{\partial x}\cos(n\varphi-x\sin\varphi)\,d\varphi=\int_0^{\pi}\bigl(-\sin(n\varphi-x\sin\varphi)\bigr)(-\sin\varphi)\,d\varphi=\int_0^{\pi}\sin\varphi\,\sin(n\varphi-x\sin\varphi)\,d\varphi ,
```
```math
u''(x)=-\int_0^{\pi}\sin^2\varphi\,\cos(n\varphi-x\sin\varphi)\,d\varphi .
```

> **Corrección de la fuente** (T254). En los apuntes la primera fórmula empieza por «$`u(x)=\int_0^\pi\cos x\cos(n\varphi-x\sin\varphi)\,d\varphi`$»; aquí se calcula la derivada $`u'(x)=\int_0^\pi\frac{\partial}{\partial x}\cos(n\varphi-x\sin\varphi)\,d\varphi`$; el resto, como en los apuntes.

Sustituyamos en el miembro izquierdo de la ecuación:
```math
x^2u''+xu'+(x^2-n^2)u=\int_0^{\pi}\Bigl[-x^2\sin^2\varphi\cos(n\varphi-x\sin\varphi)+x\sin\varphi\sin(n\varphi-x\sin\varphi)+(x^2-n^2)\cos(n\varphi-x\sin\varphi)\Bigr]d\varphi .
```

> **Corrección de la fuente** (M255, M523). En los apuntes falta en el integrando el sumando $`(x^2-n^2)\cos(n\varphi-x\sin\varphi)`$ correspondiente al término $`(x^2-n^2)u`$. Además, el enunciado del ejemplo no dice que $`n`$ sea entero; sin ello la afirmación es falsa (véase el cálculo de abajo: el miembro izquierdo vale $`-(n-x)\sin(n\pi)`$).

> **Restaurado** (según el cálculo estándar; en los apuntes el cálculo se interrumpe en esta fórmula). Pongamos $`\psi(\varphi)=n\varphi-x\sin\varphi`$, de modo que $`\psi'(\varphi)=n-x\cos\varphi`$. Como $`-x^2\sin^2\varphi+x^2=x^2\cos^2\varphi`$, el integrando es igual a
> ```math
> (x^2\cos^2\varphi-n^2)\cos\psi+x\sin\varphi\sin\psi=-\frac{d}{d\varphi}\Bigl[(n+x\cos\varphi)\sin\psi(\varphi)\Bigr],
> ```
> ya que
> ```math
> \frac{d}{d\varphi}\Bigl[(n+x\cos\varphi)\sin\psi\Bigr]=-x\sin\varphi\sin\psi+(n+x\cos\varphi)(n-x\cos\varphi)\cos\psi=(n^2-x^2\cos^2\varphi)\cos\psi-x\sin\varphi\sin\psi .
> ```
> Por tanto (para $`\varphi=0`$ la expresión entre corchetes vale $`(n+x)\sin0=0`$)
> ```math
> x^2u''+xu'+(x^2-n^2)u=-\Bigl[(n+x\cos\varphi)\sin(n\varphi-x\sin\varphi)\Bigr]_{\varphi=0}^{\varphi=\pi}=-(n-x)\sin(n\pi)=0 ,
> ```
> ya que $`n`$ es entero.

## Referencias cruzadas

- Tema en el curso: [capítulo 11 «Series de potencias y funciones analíticas»](../11-power-series.md) — [§11.2 «Convergencia uniforme y operaciones»](../11-power-series.md#sec-11-2), [§11.3 «Desarrollos estándar»](../11-power-series.md#sec-11-3), [§11.4 «Analiticidad no es suavidad»](../11-power-series.md#sec-11-4) (allí también la función $`e^{-1/x^2}`$, cuya serie de Taylor converge, pero no a ella: el caso 3 de la lista de arriba); [el criterio de Dirichlet para integrales](../09-improper-integrals-applications.md#dirichlet-test-for-integrals) (convergencia de la integral $`\int_0^{+\infty}\frac{\sin x}{x}\,dx`$).
- Comienzo de §8.4 ([definiciones 8.4.1](lecture-73-74.md#def-8-4-1), [8.4.2](lecture-73-74.md#def-8-4-2), la fórmula de Cauchy–Hadamard, [teoremas 8.4.2](lecture-73-74.md#thm-8-4-2) y [8.4.3](lecture-73-74.md#thm-8-4-3) de Abel): [lecciones 73–74](lecture-73-74.md); [teoremas 8.2.2](lecture-71-72.md#thm-8-2-2), [8.3.1](lecture-71-72.md#thm-8-3-1)–[8.3.3](lecture-73-74.md#thm-8-3-3) y el criterio de Weierstrass — [lecciones 71–72](lecture-71-72.md) y [lecciones 73–74](lecture-73-74.md).
- La fórmula de Taylor y el [lema 3.6.2](lecture-29-30.md#lem-3-6-2) sobre la estimación del resto: [lecciones 29–30](lecture-29-30.md).
- Continuación del capítulo 9 (integrales impropias dependientes de un parámetro): [lecciones 77–78](lecture-77-78.md).

---

[← Lecciones 73–74](lecture-73-74.md) · [Índice de lecciones](index.md) · [Lecciones 77–78 →](lecture-77-78.md) · [Términos y teoremas](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-75-76.md) · [English](../../en/lectures-2025-26/lecture-75-76.md)
