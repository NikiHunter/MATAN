---
title: "Lecciones 73–74 — propiedades de las series uniformemente convergentes, series de potencias, teorema de Abel"
lang: es
course: "Análisis matemático, 2025/26"
lecture: 73-74
semester: 3
source: "cuaderno manuscrito, págs. p042–p049"
source_pages: "p042, p044, p045, p046, p047, p048, p049"
course_chapter: 24
---
# Lecciones 73–74 — propiedades de las series uniformemente convergentes, series de potencias, teorema de Abel

[← Lecciones 71–72](lecture-71-72.md) · [Índice de lecciones](index.md) · [Lecciones 75–76 →](lecture-75-76.md) · [Términos y teoremas](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-73-74.md) · [English](../../en/lectures-2025-26/lecture-73-74.md)

> **Fuente y numeración.** Los apuntes se copiaron de un cuaderno manuscrito (págs. p042, p044–p049; el texto bruto de las páginas está en [`ocr/raw/`](../../../ocr/raw/p042.md); la pág. p043 es un duplicado técnico de p042). La anotación «Lecciones 73–74» comienza en el margen de la pág. p042 con el plan de la clase: propiedades de las series funcionales uniformemente convergentes; fórmula de Cauchy–Hadamard; series de potencias; teorema de Abel. El [teorema 8.3.2](#thm-8-3-2) está escrito dos veces en la pág. p042 (al final de la clase anterior y otra vez —con título e hipótesis— antes de la demostración) y aquí se reproduce una sola vez. En el cuaderno los coeficientes de una serie de potencias se denotan $`C_k`$; aquí, como en las diapositivas del profesor, se denotan $`c_k`$ (la letra $`C_n`$ denota las mayorantes en el [criterio de Weierstrass](../10-function-sequences-series.md#weierstrass-m-test)). La numeración de definiciones y teoremas es la del profesor. Los lapsus de los apuntes se corrigen y se marcan con bloques «Corrección de la fuente»; los pasajes perdidos se restauran y se marcan con bloques «Restaurado»; las etiquetas corresponden a [`ocr/RESOLVED.md`](../../../ocr/RESOLVED.md). Los lugares que aún hay que cotejar con el cuaderno se enumeran en [`ocr/ISSUES.md`](../../../ocr/ISSUES.md).

## §8.3. Series funcionales (conclusión)

<a id="p042"></a>

### Integración de series uniformemente convergentes

<a id="thm-8-3-2"></a>**Teorema 8.3.2 (integración término a término).** Sean $`u_n\in C([a,b])`$ para todo $`n\in\mathbb N`$ y $`\sum_{n=1}^{\infty}u_n(x)=S(x)`$. Si la serie $`\sum_{n=1}^{\infty}u_n(x)`$ converge uniformemente en $`[a,b]`$, entonces
```math
\int_a^b S(x)\,dx=\sum_{n=1}^{\infty}\int_a^b u_n(x)\,dx .
```

**Demostración.** Pongamos $`S_n(x)=u_1(x)+u_2(x)+\dots+u_n(x)`$. Las funciones $`S_n`$ son continuas en $`[a,b]`$ como sumas finitas de funciones continuas, y por la linealidad de la integral
```math
\int_a^b S_n(x)\,dx=\int_a^b u_1(x)\,dx+\int_a^b u_2(x)\,dx+\dots+\int_a^b u_n(x)\,dx=\sum_{k=1}^{n}\int_a^b u_k(x)\,dx .
```
Por hipótesis $`S_n\rightrightarrows S`$ en $`[a,b]`$, así que por el [teorema 8.2.2](lecture-71-72.md#thm-8-2-2) (paso al límite bajo el signo integral) el miembro izquierdo tiende a $`\int_a^b S(x)\,dx`$ cuando $`n\to\infty`$. El miembro derecho es la $`n`$-ésima [suma parcial](../04-numeric-series.md#sec-4-1) de la serie numérica $`\sum_{k=1}^{\infty}\int_a^b u_k(x)\,dx`$; por tanto, tiene el mismo límite, es decir, esta serie converge y
```math
\int_a^b S(x)\,dx=\sum_{k=1}^{\infty}\int_a^b u_k(x)\,dx .
```
$`\square`$

**Observación.** La [convergencia uniforme](../10-function-sequences-series.md#sec-10-1), e incluso la convergencia en cada punto, no es condición necesaria para la integración término a término de una serie.

<a id="p044"></a>

Dicho de otro modo (nota en rojo en el margen), que una serie pueda integrarse término a término no significa que converja uniformemente: de la igualdad $`\sum_{n=1}^{\infty}\int_a^b u_n(x)\,dx=\int_a^b S(x)\,dx`$ no se deduce que la serie $`\sum_{n=1}^{\infty}u_n(x)`$ converja uniformemente en $`[a,b]`$.

> **Corrección de la fuente** (M164). En los apuntes: «$`\sum_{n=1}^{\infty}\int_a^bu_n(x)\,dx-\int_a^bS(x)\,dx\nRightarrow\sum_{n=1}^{\infty}u_n(x)`$ conv. unif. en $`[a,b]`$». Entre la suma de las integrales y la integral de la suma debe ir un signo de igualdad: se trata de la igualdad del [teorema 8.3.2](#thm-8-3-2) (así en la nota del profesor, M3S p86).

**Ejemplo.** Para cada $`x\in(-1,1)`$ la serie $`\sum_{k=0}^{\infty}(-1)^kx^k=1-x+x^2-\dots`$ (progresión geométrica de razón $`-x`$) converge a $`\frac1{1+x}`$, mientras que para $`x=1`$ la serie $`\sum_{k=0}^{\infty}(-1)^k`$ diverge. Pero
```math
\int_0^1\frac{dx}{1+x}=\ln|1+x|\Big|_0^1=\ln2 ,
```
y la integración término a término sobre el segmento $`[0,1]`$ da el mismo número:
```math
\sum_{k=0}^{\infty}(-1)^k\int_0^1x^k\,dx=\sum_{k=0}^{\infty}\left.\frac{(-1)^kx^{k+1}}{k+1}\right|_0^1=\sum_{k=0}^{\infty}\frac{(-1)^k}{k+1}=1-\frac12+\frac13-\dots=\ln2
```
(la suma de esta serie se calculó en las lecciones 69–70).

> **Corrección de la fuente** (T166). En los apuntes la última igualdad figura como «$`\sum_{k=0}^{\infty}\frac{(-1)^k}{k+1}-\ln(2)`$»; debe ser «$`=\ln2`$».

Así pues, aquí no hay convergencia uniforme: en el punto $`x=1`$ la serie incluso diverge, y en $`[0,1)`$ (y en $`(-1,1)`$) la convergencia no es uniforme, ya que $`\sup_{x\in[0,1)}|(-1)^kx^k|=1\not\to0`$, es decir, el término general no tiende a cero uniformemente. Sin embargo, esta serie puede integrarse término a término sobre el segmento $`[0,1]`$ (la suma $`\frac1{1+x}`$ está definida en $`[0,1)`$; el valor en un punto no afecta a la integral).

### Derivación de series uniformemente convergentes

<a id="thm-8-3-3"></a>**Teorema 8.3.3 (derivación término a término).** Sean $`u_n\in C^1([a,b])`$ para todo $`n\in\mathbb N`$ y $`\sum_{n=1}^{\infty}u_n(x)=S(x)`$. Si

1. la serie $`\sum_{n=1}^{\infty}u_n(x)`$ converge (en cada punto del segmento $`[a,b]`$);
2. la serie $`\sum_{n=1}^{\infty}u_n'(x)`$ converge uniformemente en $`[a,b]`$,

entonces $`S\in C^1([a,b])`$ y
```math
\Bigl(\sum_{n=1}^{\infty}u_n(x)\Bigr)'=\sum_{n=1}^{\infty}u_n'(x)=S'(x),\qquad x\in[a,b].
```

> **Corrección de la fuente** (S169). La segunda afirmación del teorema está escrita en el margen como «$`\sum u_n(x)=\sum u'_n(x)=S(x)`$», sin los signos de derivada; corregido según la diapositiva del curso 2024/25 (FS p69).

**Demostración.** Pongamos $`S_n(x)=u_1(x)+\dots+u_n(x)`$. Entonces $`S_n\in C^1([a,b])`$, y por la condición 1 $`S_n\to S`$ puntualmente en $`[a,b]`$. Además,
```math
S_n'(x)=u_1'(x)+\dots+u_n'(x),
```
es decir, $`S_n'`$ son las sumas parciales de la serie $`\sum u_n'(x)`$, y por la condición 2, cuando $`n\to\infty`$, se tiene $`S_n'\rightrightarrows\varphi`$ en $`[a,b]`$, donde $`\varphi(x):=\sum_{n=1}^{\infty}u_n'(x)`$.

Por el [teorema 8.2.3](lecture-71-72.md#thm-8-2-3) (derivación de la función límite), aplicado a la sucesión $`(S_n)`$, obtenemos
```math
S'(x)=\varphi(x)=\sum_{k=1}^{\infty}u_k'(x)\in C([a,b]).
```
La condición «$`S\in C^1([a,b])`$» del enunciado del [teorema 8.2.3](lecture-71-72.md#thm-8-2-3) no se conoce aquí de antemano, pero no hace falta comprobarla: como se señaló tras el [teorema 8.2.3](lecture-71-72.md#thm-8-2-3) (lecciones 71–72), su demostración da $`S(x)=S(a)+\int_a^x\varphi(t)\,dt`$ sin esa condición. La función $`\varphi`$ es continua por el [teorema 8.2.1](lecture-71-72.md#thm-8-2-1) como [límite uniforme de funciones continuas](../10-function-sequences-series.md#uniform-limit-continuity) $`S_n'`$. Así, $`S'=\varphi\in C([a,b])`$, es decir, $`S\in C^1([a,b])`$, y $`\bigl(\sum u_n\bigr)'=\sum u_n'`$. $`\square`$

<a id="p045"></a>

**Ejemplo.** La serie $`\sum_{k=1}^{\infty}1`$ diverge, mientras que la serie de las derivadas $`\sum_{k=1}^{\infty}(1)'=\sum_{k=1}^{\infty}0`$ converge uniformemente en cualquier intervalo.

> **Restaurado** (según los apuntes de 2022, M3S p84). Conclusión del ejemplo: las funciones $`u_k\equiv1`$ pertenecen a $`C^1`$, la serie de sus derivadas converge uniformemente, pero la propia serie $`\sum u_k`$ diverge. Por eso en el [teorema 8.3.3](#thm-8-3-3) no puede omitirse la condición 1 (convergencia de la serie $`\sum_{k=1}^{\infty}u_k(x)`$).

## §8.4. Series de potencias

<a id="def-8-4-1"></a>**Definición 8.4.1.** Una serie de la forma
```math
\sum_{k=0}^{\infty}c_k(x-a)^k,\qquad\qquad(8.4.1)
```
donde $`c_k,x,a\in\mathbb R`$, se llama serie de potencias (real); los números $`c_k`$ se llaman sus coeficientes, y $`a`$, su centro.

Una serie de potencias generaliza el polinomio $`\sum_{k=0}^{n}c_k(x-a)^k`$ y se reduce a él si $`c_k=0`$ a partir de cierto índice.

> **Corrección de la fuente** (T519). En los apuntes el polinomio figura como «$`\sum_{k=0}^{\infty}C_k(x-a)^k`$». Un polinomio es una suma finita, por lo que el límite superior de la suma es $`n`$ (así en la diapositiva FS p72).

Observemos que para $`x=a`$ la serie (8.4.1) converge a la suma $`c_0`$, ya que los términos de índices $`k\in\mathbb N`$ son nulos (aquí $`(x-a)^0=1`$).

### Radio de convergencia

<a id="def-8-4-2"></a>**Definición 8.4.2.** La magnitud $`R\in[0,+\infty]`$ se llama radio de convergencia de la serie $`\sum_{k=0}^{\infty}c_k(x-a)^k`$ si

1. la serie converge para todo $`x`$ tal que $`|x-a|<R`$;
2. la serie diverge para todo $`x`$ tal que $`|x-a|>R`$.

**Observación.** La desigualdad $`|x-a|<R`$ define en la recta real el intervalo $`(a-R,a+R)`$, el intervalo de convergencia.

- Si $`R=+\infty`$, el intervalo de convergencia coincide con $`\mathbb R`$, y la serie $`\sum c_k(x-a)^k`$ converge absolutamente para todo $`x\in\mathbb R`$.
- Si $`R=0`$, el intervalo de convergencia es vacío, y la serie converge solo para $`x=a`$.
- Si $`0<R<+\infty`$, la serie $`\sum c_k(x-a)^k`$ converge absolutamente para $`|x-a|<R`$ y diverge para $`|x-a|>R`$, es decir, converge en el intervalo de convergencia $`(a-R,a+R)`$ y diverge fuera del segmento $`[a-R,a+R]`$; en los extremos $`x=a\pm R`$ son posibles tanto la convergencia como la divergencia.

La convergencia absoluta para $`|x-a|<R`$ se justifica más abajo ([observación 8.4.1](#rem-8-4-1)).

> **Corrección de la fuente** (S176). En los apuntes el último punto termina con las palabras «es decir, el conj. de conv. $`(a-R,a+R)`$» (lectura insegura; igual en los apuntes de 2022, M3S p88). El conjunto de convergencia contiene el intervalo $`(a-R,a+R)`$ y está contenido en el segmento $`[a-R,a+R]`$, pero puede contener los extremos: por ejemplo, la serie $`\sum_{k=1}^{\infty}\frac{x^k}{k^2}`$ (ejemplo más abajo) tiene $`R=1`$ y converge en todo el segmento $`[-1,1]`$, ya que $`\left|\frac{x^k}{k^2}\right|\le\frac1{k^2}`$ para $`|x|\le1`$. El comportamiento de la serie en los puntos $`x=a\pm R`$ no lo determina el radio y se estudia por separado.

<a id="p046"></a>

### Fórmula de Cauchy–Hadamard

En el teorema siguiente se usan los convenios $`\frac1{+\infty}=0`$, $`\frac10=+\infty`$.

<a id="thm-8-4-1"></a>**Teorema 8.4.1 (fórmula de Cauchy–Hadamard).** Toda serie de potencias $`\sum_{k=0}^{\infty}c_k(x-a)^k`$ tiene radio de convergencia, y este viene dado por la fórmula
```math
R=\frac{1}{\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}} .
```

> **Corrección de la fuente** (A178). En los apuntes (y más adelante en la demostración) figura un límite ordinario en lugar del límite superior: «$`R=\frac{1}{\lim_{n\to\infty}\sqrt[n]{|C_n|}}`$». El límite $`\lim\sqrt[n]{|c_n|}`$ no siempre existe: por ejemplo, la serie $`1+x^2+x^4+\dots`$ tiene coeficientes alternadamente iguales a $`1`$ y $`0`$, y $`\sqrt[n]{|c_n|}`$ toma los valores $`1`$ y $`0`$. El límite superior ([definición 2.3.9](lecture-13.md#def-2-3-9)) siempre existe en $`[0,+\infty]`$; la fórmula de Cauchy–Hadamard se escribe con él (así en la diapositiva FS p73).

**Demostración.** Probemos que la magnitud $`R`$ dada por la fórmula de Cauchy–Hadamard satisface la definición de radio de convergencia. Pongamos $`L:=\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}\in[0,+\infty]`$, de modo que $`R=\frac1L`$. Para $`x=a`$ la serie converge; sea $`x\ne a`$. Consideremos
```math
K=\varlimsup_{n\to\infty}\sqrt[n]{|c_n(x-a)^n|}=\varlimsup_{n\to\infty}\bigl(|x-a|\sqrt[n]{|c_n|}\bigr)=|x-a|\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}=|x-a|\,L .
```
El factor positivo $`|x-a|`$ puede sacarse del límite superior, ya que $`\sup_{k\ge n}\bigl(|x-a|\,y_k\bigr)=|x-a|\sup_{k\ge n}y_k`$; si $`L=+\infty`$, también $`K=+\infty`$ (para $`\infty`$, por definición: $`|x-a|\cdot(+\infty)=+\infty`$ para $`|x-a|>0`$).

Si $`|x-a|<R`$, entonces $`K<1`$: para $`L=0`$ tenemos $`K=0`$, y para $`0<L<+\infty`$ tenemos $`K=|x-a|\,L<RL=1`$ (el caso $`L=+\infty`$ aquí es imposible, ya que entonces $`R=0`$). Por el [criterio de Cauchy](../04-numeric-series.md#sec-4-2) la serie $`\sum|c_k(x-a)^k|`$ converge y, por tanto, la serie $`\sum c_k(x-a)^k`$ converge (absolutamente).

Si $`|x-a|>R`$, entonces $`K>1`$: para $`L=+\infty`$ tenemos $`K=+\infty`$, y para $`0<L<+\infty`$ tenemos $`K=|x-a|\,L>RL=1`$ (el caso $`L=0`$ es imposible, ya que entonces $`R=+\infty`$). Por el criterio de Cauchy los términos de la serie no tienden a cero, y la serie $`\sum c_k(x-a)^k`$ diverge. $`\square`$

> **Restaurado** (según la demostración estándar, cf. Zorich/Fichtenholz). En las lecciones 69–70 el criterio de Cauchy se demostró en el caso en que existe el límite $`\lim\sqrt[n]{a_n}`$; aquí se aplica en la forma con límite superior. *Sean $`a_n\ge0`$ y $`K=\varlimsup_{n\to\infty}\sqrt[n]{a_n}`$. Si $`K<1`$, la serie $`\sum a_n`$ converge; si $`K>1`$, entonces $`a_n\not\to0`$.* Pongamos $`z_n=\sup_{k\ge n}\sqrt[k]{a_k}`$; la sucesión $`(z_n)`$ es no creciente y $`z_n\to K`$. Si $`K<1`$, tomemos $`q:=\frac{1+K}{2}\in(K,1)`$; existe $`N`$ tal que $`z_N<q`$, es decir, $`a_k<q^k`$ para todo $`k\ge N`$, y por el primer criterio de comparación con la progresión geométrica $`\sum q^k`$ la serie $`\sum a_n`$ converge. Si $`K>1`$ (incluido $`K=+\infty`$), entonces $`z_n\ge K>1`$ para todo $`n`$, es decir, para cada $`n`$ existe $`k\ge n`$ con $`\sqrt[k]{a_k}>1`$; por tanto, $`a_k>1`$ para infinitos $`k`$, y $`a_k\not\to0`$. En la demostración del [teorema 8.4.1](#thm-8-4-1) $`a_n=|c_n(x-a)^n|`$: para $`K>1`$ los términos $`c_n(x-a)^n`$ no tienden a cero, y la serie $`\sum c_n(x-a)^n`$ diverge por la condición necesaria de convergencia.

### Convergencia absoluta de una serie de potencias

<a id="rem-8-4-1"></a>**Observación 8.4.1.** Por el criterio de Cauchy, para $`|x-a|<R`$ la serie $`\sum_{k=0}^{\infty}c_k(x-a)^k`$ converge absolutamente (en la demostración del teorema 8.4.1 se estableció la convergencia de la serie $`\sum|c_k(x-a)^k|`$ para $`|x-a|<R`$).

### Intervalo de convergencia

El [teorema 8.4.1](#thm-8-4-1) permite sacar conclusiones sobre la convergencia de una serie de potencias:

- la desigualdad $`|x-a|<R`$ define en la recta real el intervalo $`(a-R,a+R)`$, llamado intervalo de convergencia de la serie de potencias;
- si $`R=+\infty`$, el intervalo de convergencia coincide con $`\mathbb R`$, y la serie converge absolutamente para todo $`x\in\mathbb R`$;
- si $`R=0`$, el intervalo de convergencia es vacío, y la serie converge solo para $`x=a`$;
- si $`R\in(0,+\infty)`$, la serie converge absolutamente para $`|x-a|<R`$ y diverge para $`|x-a|>R`$.

<a id="p047"></a>

### Radio de convergencia y criterio de d'Alembert

A menudo el radio de convergencia puede hallarse no solo por la fórmula de Cauchy–Hadamard, sino también con el criterio de d'Alembert. A saber,
```math
R=\lim_{n\to\infty}\left|\frac{c_n}{c_{n+1}}\right|,
```
si existe el límite del miembro derecho.

> **Restaurado** (según la demostración estándar; en los apuntes y en la diapositiva FS p74 la fórmula se da sin justificación). La existencia del límite presupone que $`c_n\ne0`$ para todo $`n`$ suficientemente grande; el límite puede ser infinito. Sean $`\lim_{n\to\infty}\left|\frac{c_n}{c_{n+1}}\right|=\rho\in[0,+\infty]`$ y $`x\ne a`$. Para los valores absolutos de los términos de la serie $`a_n=|c_n(x-a)^n|`$
> ```math
> \frac{a_{n+1}}{a_n}=|x-a|\left|\frac{c_{n+1}}{c_n}\right|\xrightarrow[n\to\infty]{}\frac{|x-a|}{\rho}
> ```
> (con los convenios $`\frac{|x-a|}{+\infty}=0`$, $`\frac{|x-a|}{0}=+\infty`$). Si $`|x-a|<\rho`$, este límite es menor que $`1`$, y por el criterio de d'Alembert la serie converge absolutamente; si $`|x-a|>\rho`$, el límite es mayor que $`1`$, entonces $`a_{n+1}>a_n`$ a partir de cierto índice, los términos de la serie no tienden a cero, y la serie diverge. Por la [definición 8.4.2](#def-8-4-2) el número $`\rho`$ es el radio de convergencia.

**Ejemplo.** Para la serie $`\sum_{k=1}^{\infty}\frac{x^k}{k^2}`$ tenemos $`c_k=\frac1{k^2}`$, $`c_{k+1}=\frac1{(k+1)^2}`$,
```math
R=\lim_{k\to\infty}\left|\frac{c_k}{c_{k+1}}\right|=\lim_{k\to\infty}\frac{(k+1)^2}{k^2}=1 .
```
Así, $`R=1`$: la serie converge para $`|x|<1`$ y diverge para $`|x|>1`$.

### Observación sobre el centro de una serie de potencias

<a id="rem-8-4-2"></a>**Observación 8.4.2.** El cambio $`x-a=y`$ reduce la serie (8.4.1) a una serie de potencias de $`y`$ con centro en cero:
```math
\sum_{k=0}^{\infty}c_k(x-a)^k\ \longrightarrow\ \sum_{k=0}^{\infty}c_ky^k,\qquad y=x-a .
```
Por eso, al deducir las propiedades de las series de potencias, puede suponerse sin pérdida de generalidad que $`a=0`$.

### Convergencia uniforme de una serie de potencias

<a id="thm-8-4-2"></a>**Teorema 8.4.2 (convergencia uniforme de las series de potencias).** Sean dada una serie de potencias $`\sum_{k=0}^{\infty}c_k(x-a)^k`$ y $`R\in(0,+\infty]`$ su radio de convergencia. Entonces, para todo $`r\in(0,R)`$ la serie de potencias converge uniformemente en el conjunto $`|x-a|\le r`$, es decir, en el segmento $`[a-r,a+r]\subset(a-R,a+R)`$.

**Demostración.** Si $`|x-a|\le r`$, entonces
```math
|c_k(x-a)^k|=|c_k|\,|x-a|^k\le|c_k|\,r^k .
```

*Figura de los apuntes (pág. p047): en la recta numérica se marcan los puntos $`a-R`$, $`a`$, $`a+r`$, $`a+R`$; el segmento $`|x-a|\le r`$ está estrictamente dentro del intervalo de convergencia $`(a-R,a+R)`$.*

Como $`0<r<R`$, el punto $`x=a+r`$ está en el intervalo de convergencia, y por la [observación 8.4.1](#rem-8-4-1) la serie $`\sum_{k=0}^{\infty}c_kr^k`$ converge absolutamente, es decir, la serie $`\sum_{k=0}^{\infty}|c_k|\,r^k`$ converge.

<a id="p048"></a>

Recordemos el enunciado del criterio de Weierstrass (lecciones 71–72): si $`u_n:X\to\mathbb R`$, $`|u_n(x)|\le C_n`$ para todo $`x\in E\subset X`$ y todo $`n`$, y la serie $`\sum_{n=1}^{\infty}C_n`$ converge, entonces la serie $`\sum_{n=1}^{\infty}u_n(x)`$ converge uniformemente en $`E`$. Apliquémoslo a $`u_k(x)=c_k(x-a)^k`$, $`C_k=|c_k|\,r^k`$ y $`E=\{x:|x-a|\le r\}`$: por el criterio de Weierstrass la serie $`\sum_{k=0}^{\infty}c_k(x-a)^k`$ converge uniformemente en el conjunto $`|x-a|\le r`$. $`\square`$

### Teorema de Abel

<a id="thm-8-4-3"></a>**Teorema 8.4.3 (teorema de Abel sobre series de potencias).** Sean dada una serie de potencias $`\sum_{k=0}^{\infty}c_k(x-a)^k`$ y $`R\in(0,+\infty)`$ su radio de convergencia. Si la serie de potencias converge para $`x=a+R`$ (respectivamente para $`x=a-R`$), entonces converge uniformemente en el segmento $`[a,a+R]`$ (respectivamente en $`[a-R,a]`$), y su suma es continua por la izquierda en el punto $`a+R`$ (respectivamente por la derecha en el punto $`a-R`$).

*Figura en el margen (pág. p048): en el eje se marcan los puntos $`a-R`$, $`a`$, $`a+R`$; bajo los extremos del intervalo se escriben las series numéricas $`\sum c_k(-R)^k`$ y $`\sum c_kR^k`$, en las que se convierte la serie de potencias para $`x=a-R`$ y para $`x=a+R`$.*

Para la demostración hará falta el criterio de convergencia uniforme de Abel (en los apuntes figura como «Teorema de Abel (pista)» y sin demostración; en las diapositivas, «teorema de Abel sobre la convergencia uniforme de series»).

### Criterio de Abel de convergencia uniforme

Supongamos que

1. la serie $`\sum_{k=1}^{\infty}f_k(x)`$ converge uniformemente en $`X`$;
2. para cada $`x\in X`$ la sucesión $`\{g_k(x)\}`$ es monótona, y la sucesión de funciones $`\{g_k\}`$ está uniformemente acotada en $`X`$, es decir, existe $`M`$ tal que $`|g_k(x)|\le M`$ para todo $`k\in\mathbb N`$ y todo $`x\in X`$.

Entonces la serie $`\sum_{k=1}^{\infty}f_k(x)g_k(x)`$ converge uniformemente en $`X`$.

> **Restaurado** (según la demostración estándar, cf. Zorich/Fichtenholz; en los apuntes y en las diapositivas el criterio se da sin demostración).
>
> **Demostración.** Fijemos $`n`$ y pongamos $`F_n(x):=0`$, $`F_m(x):=\sum_{j=n+1}^{m}f_j(x)`$ para $`m>n`$. Como $`f_k=F_k-F_{k-1}`$ para $`k>n`$, para $`m>n`$ (transformación de Abel, lecciones 69–70)
> ```math
> \sum_{k=n+1}^{m}f_k(x)g_k(x)=\sum_{k=n+1}^{m}\bigl(F_k(x)-F_{k-1}(x)\bigr)g_k(x)=F_m(x)g_m(x)+\sum_{k=n+1}^{m-1}F_k(x)\bigl(g_k(x)-g_{k+1}(x)\bigr).
> ```
> Por el criterio de Bolzano–Cauchy (para la serie uniformemente convergente $`\sum f_k`$), para todo $`\varepsilon>0`$ existe $`N`$ tal que $`|F_k(x)|<\varepsilon`$ para todo $`k>n>N`$ y todo $`x\in X`$. Para $`x`$ fijo todas las diferencias $`g_k(x)-g_{k+1}(x)`$ tienen el mismo signo (la sucesión es monótona), por lo que
> ```math
> \sum_{k=n+1}^{m-1}\bigl|g_k(x)-g_{k+1}(x)\bigr|=\bigl|g_{n+1}(x)-g_m(x)\bigr|\le2M .
> ```
> En consecuencia, para todo $`m>n>N`$ y todo $`x\in X`$
> ```math
> \Bigl|\sum_{k=n+1}^{m}f_k(x)g_k(x)\Bigr|\le\varepsilon M+\varepsilon\cdot2M=3M\varepsilon .
> ```
> Como $`\varepsilon>0`$ es arbitrario, por el criterio de Bolzano–Cauchy la serie $`\sum_{k=1}^{\infty}f_k(x)g_k(x)`$ converge uniformemente en $`X`$. $`\square`$

**Demostración del [teorema 8.4.3](#thm-8-4-3).** Sin pérdida de generalidad $`a=0`$ ([observación 8.4.2](#rem-8-4-2)), es decir, consideramos la serie $`\sum_{k=0}^{\infty}c_kx^k`$. Supongamos que converge en el punto $`x=R`$. Transformemos los términos de la serie:
```math
c_kx^k=c_kR^k\cdot\left(\frac{x}{R}\right)^k .
```

<a id="p049"></a>

$`\sum_{k=0}^{\infty}c_kR^k`$ es una serie numérica, y converge (por la hipótesis del teorema la serie $`\sum c_k(x-a)^k`$ converge para $`x=a+R`$). Como los términos $`f_k(x):=c_kR^k`$ de esta serie no dependen de $`x`$, su convergencia puede considerarse uniforme en $`[0,R]`$: la condición del criterio de Bolzano–Cauchy se cumple a la vez para todo $`x`$.

La sucesión $`g_k(x):=\left(\frac{x}{R}\right)^k`$: si $`0\le x\le R`$, entonces $`0\le\left(\frac{x}{R}\right)^k\le1`$. Por tanto, la sucesión $`\{g_k\}`$ está uniformemente acotada en $`[0,R]`$ y es monótona para cada $`x\in[0,R]`$ (no creciente en $`k`$, ya que $`0\le\frac xR\le1`$).

> **Corrección de la fuente** (U193, T195). En los apuntes: «$`\sum_{k=0}^{\infty}R^k`$ es una serie numérica ⇒ su conv. puede considerarse unif[orme] en $`[0,R]`$»; se trata de la serie $`\sum c_kR^k`$ de la línea anterior (falta el factor $`c_k`$); luego «$`0<x<R`$, [entonces] $`0\le(x/R)^k\le1`$ ⇒ la suc. $`(x/R)^k`$ está acot. en $`[0,R]`$». La estimación hace falta en todo el segmento $`[0,R]`$, incluidos los extremos, por lo que la condición es $`0\le x\le R`$ (así en la nota del profesor, FS p76).

Por el criterio de convergencia uniforme de Abel, la serie $`\sum_{k=0}^{\infty}c_kx^k=\sum_{k=0}^{\infty}c_kR^k\left(\frac xR\right)^k`$ converge uniformemente en $`[0,R]`$.

La continuidad de la suma se deduce de la continuidad de cada término de la serie $`\sum c_kx^k`$ y de la convergencia uniforme de la serie en $`[0,R]`$: por el [teorema 8.3.1](lecture-71-72.md#thm-8-3-1) la suma de la serie es continua en $`[0,R]`$, en particular [continua en el punto](lecture-16.md#def-2-5-1) $`R`$ por la izquierda. $`\square`$

> **Restaurado** (según el razonamiento estándar; en los apuntes y en la nota del profesor solo se trata el caso $`x=a+R`$). Supongamos que la serie converge para $`x=a-R`$, es decir (para $`a=0`$) en el punto $`x=-R`$. La serie de potencias $`\sum_{k=0}^{\infty}(-1)^kc_kt^k`$ tiene el mismo radio de convergencia $`R`$ (por la fórmula de Cauchy–Hadamard, ya que $`|(-1)^kc_k|=|c_k|`$) y converge para $`t=R`$. Por lo demostrado, converge uniformemente en $`[0,R]`$, y su suma es continua por la izquierda en el punto $`R`$. Como $`\sum(-1)^kc_kt^k=\sum c_k(-t)^k`$, tras el cambio $`x=-t`$ obtenemos: la serie $`\sum c_kx^k`$ converge uniformemente en $`[-R,0]`$, y su suma es continua por la derecha en el punto $`-R`$.

### Ejemplos de cálculo del radio de convergencia

**Ejemplo 1.** $`\sum_{n=0}^{\infty}(-2)^n(x-3)^n`$. Aquí $`c_n=(-2)^n`$ y
```math
R=\lim_{n\to\infty}\left|\frac{c_n}{c_{n+1}}\right|=\lim_{n\to\infty}\frac{2^n}{2^{n+1}}=\frac12 .
```
El intervalo de convergencia es $`\left(3-\frac12,\,3+\frac12\right)=(2{,}5;\ 3{,}5)`$.

> **Corrección de la fuente** (M197). En los apuntes: «$`R=\lim\left|\frac{C_n}{C_{n+1}}\right|=\lim\left(\frac{2^nn}{(-2)^{n+1}(n+1)}\right)=\lim\left|\frac{2}{2(n+1)}\right|=\frac12`$». Para la serie tal como está escrita, $`c_n=(-2)^n`$: no hay factores $`n`$ ni $`n+1`$, y $`\left|\frac{c_n}{c_{n+1}}\right|=\frac12`$ para todo $`n`$; además, $`\lim\frac{2}{2(n+1)}=0`$, y no $`\frac12`$. La respuesta $`R=\frac12`$ es correcta (la fórmula de Cauchy–Hadamard da lo mismo: $`\sqrt[n]{|c_n|}=2`$; y para $`c_n=(-2)^nn`$ sería $`\left|\frac{c_n}{c_{n+1}}\right|=\frac{n}{2(n+1)}\to\frac12`$).

**Ejemplo 2.** $`\sum_{n=0}^{\infty}\left(-\frac32\right)^n(x-2)^n`$. Aquí $`c_n=\left(-\frac32\right)^n`$, $`\sqrt[n]{|c_n|}=\frac32`$ para todo $`n`$ y
```math
R=\frac{1}{\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}}=\frac{1}{3/2}=\frac23 .
```
El intervalo de convergencia es $`\left(2-\frac23,\,2+\frac23\right)=\left(\frac43,\frac83\right)`$.

> **Corrección de la fuente** (T199, U200). En los apuntes: «$`R=\frac{1}{\lim\sqrt[n]{|C_n|}}=\frac{1}{\lim|3/2|^{n/n}}=\left|\frac23\right|=a`$», y luego «La serie conv. en $`x=-2`$, int[ervalo] de conv. $`\varnothing`$». El radio $`R=\frac23`$ está bien calculado («$`=a`$» es un lapsus; aquí $`\sqrt[n]{|c_n|}=\frac32`$ para todo $`n`$, así que el límite existe y coincide con el superior). La conclusión, sin embargo, contradice el radio hallado: para $`R=\frac23>0`$ el intervalo de convergencia $`\left(\frac43,\frac83\right)`$ no es vacío. La conclusión «el intervalo de convergencia es vacío, la serie converge en un único punto» es correcta para el ejemplo 3, donde $`R=0`$, y el único punto de convergencia es el centro $`x=2`$.

**Ejemplo 3.** $`\sum_{n=0}^{\infty}2^{n^2}(x-2)^n`$. Aquí $`c_n=2^{n^2}`$, $`\sqrt[n]{|c_n|}=2^n\to+\infty`$, por lo que
```math
R=\frac{1}{\varlimsup_{n\to\infty}\sqrt[n]{|c_n|}}=\frac{1}{+\infty}=0 .
```
El intervalo de convergencia es vacío: la serie converge solo para $`x=2`$ (en el centro).

> **Corrección de la fuente** (T201). En los apuntes: «$`R=\frac{1}{\lim\sqrt[n]{|C_n|}}=\frac{1}{\lim2^n}=\infty`$ — int. de conv. $`\mathbb R`$, conv. solo en $`\mathbb R`$». Como $`2^n\to+\infty`$, por el convenio $`\frac1{+\infty}=0`$ se obtiene $`R=0`$, y no $`+\infty`$. Comprobación: para $`x\ne2`$ se tiene $`|2^{n^2}(x-2)^n|=\bigl(2^n|x-2|\bigr)^n\ge1`$ en cuanto $`2^n|x-2|\ge1`$, es decir, para todo $`n`$ suficientemente grande; los términos de la serie no tienden a cero, y la serie diverge.

> **Restaurado** (estudio de los extremos de los intervalos de convergencia; no se hace en los apuntes). En el ejemplo 1, para $`x=\frac52`$ los términos de la serie valen $`(-2)^n\left(-\frac12\right)^n=1`$, y para $`x=\frac72`$ valen $`(-2)^n\left(\frac12\right)^n=(-1)^n`$; en ambos casos no tienden a cero, y la serie diverge, de modo que el conjunto de convergencia es el intervalo $`\left(\frac52,\frac72\right)`$. En el ejemplo 2, para $`x=\frac83`$ los términos valen $`\left(-\frac32\right)^n\left(\frac23\right)^n=(-1)^n`$, y para $`x=\frac43`$ valen $`\left(-\frac32\right)^n\left(-\frac23\right)^n=1`$; la serie diverge en ambos extremos, y el conjunto de convergencia es $`\left(\frac43,\frac83\right)`$.

## Referencias cruzadas

- Tema en el curso: [capítulo 10 «Sucesiones y series de funciones»](../10-function-sequences-series.md) — [§10.3 «Continuidad e integración»](../10-function-sequences-series.md#sec-10-3), [§10.4 «Derivación»](../10-function-sequences-series.md#sec-10-4); [capítulo 11 «Series de potencias y funciones analíticas»](../11-power-series.md) — [§11.1 «Radio de convergencia»](../11-power-series.md#sec-11-1), [§11.2 «Convergencia uniforme y operaciones»](../11-power-series.md#sec-11-2), [teorema de Abel](../11-power-series.md#abel-theorem).
- Hechos usados: los [teoremas 8.2.1](lecture-71-72.md#thm-8-2-1)–[8.2.3](lecture-71-72.md#thm-8-2-3) y [8.3.1](lecture-71-72.md#thm-8-3-1), el criterio de Weierstrass y el criterio de Bolzano–Cauchy de convergencia uniforme — [lecciones 71–72](lecture-71-72.md); los criterios de Cauchy y de d'Alembert, la transformación de Abel, la suma de la serie $`\sum\frac{(-1)^{k-1}}{k}=\ln2`$ — [lecciones 69–70](lecture-69-70.md); el [límite superior](lecture-13.md#def-2-3-9) ([definición 2.3.9](lecture-13.md#def-2-3-9)).
- Continuación de §8.4 (integración y derivación de series de potencias, [serie de Taylor](../11-power-series.md#sec-11-3), [funciones analíticas](../11-power-series.md#sec-11-4)): [lecciones 75–76](lecture-75-76.md).

---

[← Lecciones 71–72](lecture-71-72.md) · [Índice de lecciones](index.md) · [Lecciones 75–76 →](lecture-75-76.md) · [Términos y teoremas](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-73-74.md) · [English](../../en/lectures-2025-26/lecture-73-74.md)
