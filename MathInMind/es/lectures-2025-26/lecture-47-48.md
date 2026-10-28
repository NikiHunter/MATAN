---
title: "Lecciones 47–48 — Desigualdades integrales e integrales impropias"
lang: es
course: "Análisis matemático, 2025/26"
lecture: 47-48
semester: 2
date: 2026-04-02
source: "ma25_26-lectures_47-48_notes.pdf"
pdf_pages: 41
typed_slides: 25
archive_file: "Лекция 47-48 1.md"
---
# Lecciones 47–48 — Desigualdades integrales e integrales impropias

[← Lecciones 45–46](lecture-45-46.md) · [Índice de lecciones](index.md) · [Lecciones 49–50 →](lecture-49-50.md) · [Términos y teoremas](../term-index.md) · [Русский](../../ru/lectures-2025-26/lecture-47-48.md) · [English](../../en/lectures-2025-26/lecture-47-48.md)

> **Fuente:** `ma25_26-lectures_47-48_notes.pdf` — 41 páginas PDF, 25 diapositivas impresas; la fecha impresa es 2 de abril de 2026. Páginas impresas: 1–4, 7–13, 15, 17–18, 20–23, 25–26, 29, 31–32, 34 y 36. Páginas manuscritas: 5–6, 14, 16, 19, 24, 27–28, 30, 33, 35 y 37–41. Cada página PDF se atribuye una sola vez; la numeración de diapositivas y páginas PDF es distinta.
>
> **Duplicación del semestre 2.** El semestre 1 termina con la lección 32; el semestre 2 abarca las lecciones 33–64. El contenido completo coincide con [§4.4, «Taylor, Wallis y desigualdades integrales»](../../ru/lectures/05-taylor-wallis-inequalities-4-4.md) y [§4.5, «Integrales impropias»](../../ru/lectures/06-improper-integrals-4-5.md), y también está en el [registro del semestre 2](../../ru/lectures/index.md). Se conserva el original archivado [«Лекция 47-48 1.md»](../../../source/MathInMind/МАТАН_Л/Лекция%2047-48%201.md). Esta transcripción ilustrada completa no se sustituye por enlaces a las notas temáticas.
>
> **Condiciones importantes.** Aquí una [integral impropia](#def-4-5-2) significa un límite unilateral ordinario, no un [valor principal](../09-improper-integrals-applications.md#sec-9-1) de Cauchy. En presencia de varias singularidades, cada parte unilateral se verifica por separado. Convergencia significa límite finito. No se aplica [Newton–Leibniz](lecture-43-44.md#thm-4-3-2) a través de una singularidad sin comprobar sus hipótesis.

## Diapositiva impresa 1 (PDF p. 1). Portada

«Análisis matemático», lecciones 47–48, 2 de abril de 2026; D. E. Apushkinskaya, Universidad RUDN.

## Diapositiva impresa 2 (PDF p. 2). Cita del día

La diapositiva contrapone el símbolo [diferencial](lecture-24-25-26.md#def-3-3-1) $`\partial z/\partial x`$ y la integral $`\int f(x)\,dx`$.

**COLEGA.** «Esta monada es el diferencial. Es muy útil y calcularlo es un placer. Puedes derivar cualquier función sin esfuerzo: sus fórmulas son fáciles de recordar y te sacarán de apuros una y otra vez. ¡Sin duda, el diferencial es tu colega!»

**NO ES COLEGA.** «Esto es mal concentrado, salido de las profundidades del infierno, y te atormentará toda la vida. Los cálculos te quitarán años preciosos y kilómetros de papel. Uno de sus signos parece un instrumento de tortura, que es exactamente lo que es. ¡Huye despavorido: no es tu colega!»

## Diapositiva impresa 3 (PDF p. 3). Objetivos

Desigualdades integrales; integrales impropias; sustitución e [integración por partes](lecture-37-38.md#thm-4-1-4) para integrales impropias; criterios de convergencia de integrales impropias.

## Capítulo 4, §4. Desigualdades integrales

### Diapositiva impresa 4 (PDF p. 4). Desigualdad de Hölder

Los exponentes conjugados $`p,q\in(1,+\infty)`$ satisfacen $`1/p+1/q=1`$.

<a id="thm-4-4-5"></a>**Teorema 4.4.5.** Sean $`f,g\in C[a,b]`$ y sean $`p,q`$ exponentes conjugados. Entonces

```math
\left|\int_a^b fg\right|
\le\left(\int_a^b|f|^p\right)^{1/p}
\left(\int_a^b|g|^q\right)^{1/q}.
```

Una nota manuscrita en la diapositiva identifica el caso $`p=q=2`$ con la desigualdad de Cauchy–Bunyakovsky.

### Página manuscrita (PDF p. 5). Hölder para sumas y sumas de Riemann

La demostración usa Hölder para sumas finitas:

```math
\left|\sum_{k=0}^{n-1}a_kb_k\right|
\le\left(\sum_{k=0}^{n-1}|a_k|^p\right)^{1/p}
\left(\sum_{k=0}^{n-1}|b_k|^q\right)^{1/q}.
```

Se toma la [partición](lecture-37-38.md#def-4-2-2) uniforme $`x_k=a+k(b-a)/n`$, $`\Delta x_k=(b-a)/n`$, y se define $`a_k=f(x_k)(\Delta x_k)^{1/p}`$, $`b_k=g(x_k)(\Delta x_k)^{1/q}`$. Así, $`a_kb_k=f(x_k)g(x_k)\Delta x_k`$; las potencias de las sumas de la derecha producen $`|f(x_k)|^p\Delta x_k`$ y $`|g(x_k)|^q\Delta x_k`$.

### Página manuscrita (PDF p. 6). Límite de las sumas en la prueba de Hölder

Con estos $`a_k,b_k`$, la desigualdad de sumas queda

```math
\left|\sum f(x_k)g(x_k)\Delta x_k\right|
\le\left(\sum |f(x_k)|^p\Delta x_k\right)^{1/p}
\left(\sum |g(x_k)|^q\Delta x_k\right)^{1/q}.
```

Al hacer $`n\to\infty`$, las tres sumas tienden a sus [integrales de Riemann](lecture-39-40.md#def-4-2-6). La continuidad de los integrandos justifica el paso al límite y prueba el [teorema 4.4.5](#thm-4-4-5).

### Diapositiva impresa 5 (PDF p. 7). Desigualdad de Cauchy–Bunyakovsky

<a id="cor-4-4-1"></a>**Corolario 4.4.1.** Si $`f,g\in C[a,b]`$, entonces

```math
\left|\int_a^bfg\right|
\le\sqrt{\int_a^b f^2}\sqrt{\int_a^b g^2}.
```

### Diapositiva impresa 6 (PDF p. 8). Desigualdad de Minkowski

<a id="thm-4-4-6"></a>**Teorema 4.4.6.** Sean $`f,g\in C[a,b]`$, $`p\ge1`$. Entonces

```math
\left(\int_a^b|f+g|^p\right)^{1/p}
\le\left(\int_a^b|f|^p\right)^{1/p}
+\left(\int_a^b|g|^p\right)^{1/p}.
```

La diapositiva también escribe a mano el caso $`p=2`$:

```math
\sqrt{\int_a^b|f+g|^2}\le\sqrt{\int_a^b f^2}+\sqrt{\int_a^b g^2}.
```

## Capítulo 4, §5. Integrales impropias

### Diapositiva impresa 7 (PDF p. 9). Encabezado de sección

«§5. Integrales impropias».

### Diapositiva impresa 8 (PDF p. 10). Integrabilidad local de Riemann

Para $`f\in C([a,b])`$, la integral de Riemann está definida. ¿Qué cambia para $`f\in C([a,b))`$ o si $`b=+\infty`$?

<a id="def-4-5-1"></a>**Definición 4.5.1.** Una función $`f`$ es localmente integrable de Riemann en un intervalo $`\langle a,b\rangle`$ si es integrable de Riemann en cada segmento cerrado contenido en ese intervalo. La clase se denota $`\mathcal R_{loc}(\langle a,b\rangle)`$. Claramente, $`C(\langle a,b\rangle)\subset\mathcal R_{loc}(\langle a,b\rangle)`$.

### Diapositiva impresa 9 (PDF p. 11). Integral impropia en el extremo derecho

<a id="def-4-5-2"></a>**Definición 4.5.2.** Sean $`-\infty<a<b\le+\infty`$ y $`f\in\mathcal R_{loc}([a,b))`$. Se define

```math
\int_a^{\to b}f(x)\,dx:=\lim_{B\to b-}\int_a^Bf(x)\,dx.
```

Este límite define la integral impropia. Si existe en $`\mathbb R`$ y vale $`I`$, la integral converge y se le asigna el valor $`I`$. Si el límite es infinito o no existe, no se asigna un valor finito y la integral diverge.

### Diapositiva impresa 10 (PDF p. 12). Singularidad en el extremo izquierdo

Análogamente, para $`-\infty\le a<b<+\infty`$ y $`f\in\mathcal R_{loc}((a,b])`$:

```math
\int_{\to a}^{b}f(x)\,dx:=\lim_{A\to a+}\int_A^bf(x)\,dx.
```

La integral converge si el límite es finito. Se llama divergente si el límite es infinito o no existe.

### Diapositiva impresa 11 (PDF p. 13). Ejemplos de potencias

1. $`\displaystyle\int_{\to0}^{1}\frac{dx}{x}=\lim_{t\to0+}\int_t^1\frac{dx}{x}=\lim_{t\to0+}[\ln x]_t^1=+\infty`$.
2. $`\displaystyle\int_{\to0}^{1}x^{-p}\,dx`$ converge si $`p<1`$ y diverge si $`p\ge1`$.
3. $`\displaystyle\int_1^{\to+\infty}x^{-p}\,dx`$ converge si $`p>1`$ y diverge si $`p\le1`$.

### Página manuscrita (PDF p. 14). Cálculo de una integral de potencia

La pizarra calcula $`\int_2^B x^{-p}\,dx`$ para $`p\ne1`$:

```math
\int_2^B x^{-p}\,dx
=\left.\frac{x^{1-p}}{1-p}\right|_2^B
=\frac1{1-p}\left(B^{1-p}-2^{1-p}\right).
```

Para $`p=1`$, la [primitiva](lecture-36.md#def-4-1-1) es $`\ln x`$. El límite cuando $`B\to+\infty`$ es finito exactamente si $`p>1`$; si $`p=1`$, el logaritmo crece sin cota y, si $`p<1`$, también crece sin cota el término $`B^{1-p}`$. La fórmula análoga cerca de cero da el umbral $`p<1`$; en $`p=1`$ hay divergencia logarítmica.

### Diapositiva impresa 12 (PDF p. 15). Integral propia como caso particular

<a id="lem-4-5-1"></a>**Lema 4.5.1.** Si $`f\in C([a,b])`$, entonces

```math
\int_a^{\to b}f(x)\,dx=\int_a^bf(x)\,dx.
```

### Página manuscrita (PDF p. 16). Demostración del lema 4.5.1

Como $`f`$ es continua, existe una primitiva $`F`$, y $`\int_a^bf=F(b)-F(a)`$. Por otro lado,

```math
\int_a^{\to b}f=\lim_{t\to b-}(F(t)-F(a))=F(b)-F(a),
```

por la continuidad de $`F`$ en $`b`$.

### Diapositiva impresa 13 (PDF p. 17). Cuándo aparece una integral impropia

Hay dos casos: (a) $`b=+\infty`$; (b) $`b<+\infty`$, pero $`f\notin\mathcal R([a,b])`$. El caso (b) ocurre exactamente cuando $`f`$ no está acotada en ningún entorno izquierdo de $`b`$.

### Diapositiva impresa 14 (PDF p. 18). Aditividad en un intervalo

<a id="lem-4-5-2"></a>**Lema 4.5.2.** Sean $`f\in C([a,b))`$ y $`a<c<b`$. Entonces

```math
\int_a^{\to b}f(x)\,dx=\int_a^cf(x)\,dx+\int_c^{\to b}f(x)\,dx.\tag{4.5.1}
```

La convergencia de la integral de $`a`$ a $`b`$ equivale a la convergencia de la cola desde $`c`$ hasta $`b`$.

### Página manuscrita (PDF p. 19). Demostración del lema 4.5.2

Para cada $`B\in(c,b)`$, la aditividad de la integral propia da

```math
\int_a^Bf=\int_a^cf+\int_c^Bf.\tag{4.5.2}
```

Al tender $`B\to b-`$, el primer término es constante, así que el límite finito del lado izquierdo existe si y solo si existe el del último término. Pasar al límite en (4.5.2) da (4.5.1).

### Diapositiva impresa 15 (PDF p. 20). Resto de una integral impropia convergente

<a id="def-4-5-3"></a>**Definición 4.5.3.** La integral $`\int_A^{\to b}f(x)\,dx`$ se llama resto de la integral $`\int_a^{\to b}f(x)\,dx`$.

<a id="lem-4-5-3"></a>**Lema 4.5.3.** Si $`\int_a^{\to b}f`$ converge, entonces

```math
\int_A^{\to b}f(x)\,dx\longrightarrow0\quad(A\to b-).
```

Es decir, el resto de una integral convergente tiende a cero.

![PDF p. 20: esquema original de la cola de una integral impropia desde a hasta b](../../assets/lectures-2025-26/lec47-48-p20-improper-tail.jpg)

### Diapositiva impresa 16 (PDF p. 21). Linealidad de la integral impropia

<a id="lem-4-5-4"></a>**Lema 4.5.4.** Sean $`f,g\in C([a,b))`$ y $`\alpha,\beta\in\mathbb R`$. La diapositiva afirma

```math
\int_a^{\to b}(\alpha f+\beta g)
=\alpha\int_a^{\to b}f+\beta\int_a^{\to b}g.
```

También dice que las tres integrales convergen o divergen simultáneamente y, si convergen, sus valores satisfacen esta identidad lineal.

#### Anotación manuscrita en la misma diapositiva. Precisión sobre la linealidad

La nota manuscrita indica que se pase al límite cuando $`B\to b-`$ en la identidad de las integrales propias sobre $`[a,B]`$. Así se obtiene la linealidad cuando existen los límites de ambas integrales originales. La afirmación impresa de convergencia «simultánea» sin condiciones es falsa para $`\alpha,\beta`$ arbitrarios: los coeficientes pueden ser cero y puede haber cancelación de términos divergentes. La formulación correcta es: si convergen $`\int_a^{\to b}f`$ y $`\int_a^{\to b}g`$, converge la integral de la combinación lineal y su valor es la combinación correspondiente; si una diverge y la otra converge, la suma diverge. La convergencia del integrando $`g`$ se examina aparte, al igual que la de $`f`$. Dos términos divergentes sí pueden cancelarse.

### Diapositiva impresa 17 (PDF p. 22). Suma de una integral divergente y otra convergente

Si $`\int_a^{\to b}f`$ diverge y $`\int_a^{\to b}g`$ converge, entonces diverge $`\int_a^{\to b}(f+g)`$. La diapositiva razona que la convergencia de la suma implicaría, por linealidad, la convergencia de $`f=(f+g)-g`$, contradicción.

### Diapositiva impresa 18 (PDF p. 23). Cambio de variable

<a id="thm-4-5-1"></a>**Teorema 4.5.1.** Sean $`f\in C([a,b))`$, $`\varphi\in C^1([\alpha,\beta))`$, con $`\varphi`$ monótona, $`\varphi(\alpha)=a`$ y $`\lim_{x\to\beta-0}\varphi(x)=b`$. Entonces

```math
\int_\alpha^{\to\beta}f(\varphi(x))\varphi'(x)\,dx
=\int_a^{\to b}f(t)\,dt.\tag{4.5.3}
```

El enunciado significa que la existencia de una de las integrales implica la existencia de la otra y se cumple la igualdad.

### Página manuscrita (PDF p. 24). Demostración del cambio de variable

Para un $`y<\beta`$ finito se aplica la fórmula de sustitución para integrales propias:

```math
\int_\alpha^y f(\varphi(x))\varphi'(x)\,dx
=\int_{\varphi(\alpha)}^{\varphi(y)}f(t)\,dt.
```

Cuando $`y\to\beta-`$, $`\varphi(y)\to b`$. Pasar al límite en ambos lados demuestra (4.5.3) siempre que exista el límite finito. La monotonía garantiza que el extremo se aproxima a $`b`$ sin rebasarlo.

### Diapositiva impresa 19 (PDF p. 25). Una sustitución que convierte la integral impropia en propia

A veces la sustitución convierte una integral impropia en una propia. Ejemplo:

```math
\int_0^{+\infty}\frac{\arctan x}{1+x^2}\,dx
=\int_0^{\pi/2}t\,dt,
\qquad t=\arctan x,\quad dt=\frac{dx}{1+x^2}.
```

Para $`x=0`$, $`t=0`$; cuando $`x\to+\infty`$, $`t\to\pi/2`$. Por tanto, el valor es $`\pi^2/8`$.

### Diapositiva impresa 20 (PDF p. 26). Integración por partes

<a id="thm-4-5-2"></a>**Teorema 4.5.2.** Sean $`u,v\in C^1([a,b))`$ y supóngase que existe $`\lim_{x\to b-0}u(x)v(x)`$. Entonces

```math
\int_a^{\to b}u(x)v'(x)\,dx
=\left.uv\right|_a^{\to b}-\int_a^{\to b}v(x)u'(x)\,dx,\tag{4.5.4}
```

donde $`\left.uv\right|_a^{\to b}=\lim_{x\to b-0}u(x)v(x)-u(a)v(a)`$. Si converge el lado derecho de (4.5.4), también converge el izquierdo.

### Página manuscrita (PDF p. 27). Demostración de integración por partes

Para cada $`B<b`$, la fórmula propia da

```math
\int_a^B u(x)v'(x)\,dx=[u(x)v(x)]_a^B-\int_a^Bv(x)u'(x)\,dx.
```

Se hace $`B\to b-`$ usando el límite supuesto de $`uv`$ y la convergencia del lado derecho para obtener (4.5.4). La convergencia del lado derecho es la hipótesis que permite deducir la del izquierdo; no se desprende solo de la existencia del límite de $`uv`$ en el extremo.

### Página manuscrita (PDF p. 28). Cambio que elimina una singularidad en el extremo derecho

Para $`a<b`$, consideremos $`\int_a^b f(x)\,dx`$ con una singularidad en $`x=b`$. Tomemos

```math
x=b-\frac1t,\qquad dx=\frac{dt}{t^2}.
```

Entonces $`x=a`$ corresponde a $`t=1/(b-a)`$, y cuando $`x\to b-`$ se tiene $`t\to+\infty`$. El cambio transforma la integral en

```math
\int_{1/(b-a)}^{+\infty} f\!\left(b-\frac1t\right)\frac{dt}{t^2}.
```

### Diapositiva impresa 21 (PDF p. 29). Integrandos no negativos

<a id="lem-4-5-5"></a>**Lema 4.5.5.** Sean $`f\in\mathcal R_{loc}[a,b)`$, $`f\ge0`$. La convergencia de $`\int_a^{\to b}f`$ equivale a que esté acotada superiormente en $`[a,b)`$ la función

```math
F(A)=\int_a^A f
```

### Página manuscrita (PDF p. 30). Demostración del lema 4.5.5

Como $`f\ge0`$, la función $`F(A)=\int_a^A f`$ es no decreciente: para $`a\le A<B<b`$,

```math
F(B)-F(A)=\int_A^B f\ge0.
```

La convergencia de $`\int_a^{\to b}f`$ equivale a que exista el límite finito de $`F(A)`$ cuando $`A\to b-`$. Si ese límite es finito, $`F`$ está [acotada superiormente](lecture-05-06.md#def-1-3-7). Recíprocamente, si la función creciente $`F`$ está acotada superiormente, el teorema sobre el [límite de una función](lecture-14.md#def-2-4-4) monótona garantiza un límite finito cuando $`A\to b-`$; ese es el valor de la integral impropia.

### Diapositiva impresa 22 (PDF p. 31). Observaciones sobre el criterio

1. Para $`f\ge0`$, la integral converge o diverge a $`+\infty`$, y

```math
\int_a^{\to b}f=\sup_{A\in[a,b)}\int_a^A f.
```

2. Para acotar superiormente la función creciente $`F`$, basta acotar una sucesión $`F(A_n)`$, donde $`A_n\in[a,b)`$ crece hacia $`b`$. En efecto,

```math
\sup_nF(A_n)=\lim_{n\to\infty}F(A_n)=\lim_{A\to b-}F(A)=\sup_{A\in[a,b)}F(A).
```

### Diapositiva impresa 23 (PDF p. 32). Criterio de comparación

<a id="thm-4-5-3"></a>**Teorema 4.5.3.** Sean $`f,g\in\mathcal R_{loc}[a,b)`$, $`f,g\ge0`$, y $`f(x)=O(g(x))`$ cuando $`x\to b-`$. Entonces:

1. Si converge $`\int_a^{\to b}g`$, converge $`\int_a^{\to b}f`$.
2. Si diverge $`\int_a^{\to b}f`$, diverge $`\int_a^{\to b}g`$.

### Página manuscrita (PDF p. 33). Demostración de comparación

De $`f=O(g)`$ en el extremo derecho existen $`\Delta<b`$ y $`K>0`$ tales que $`f(x)\le Kg(x)`$ para $`x\in[\Delta,b)`$. Si converge $`\int_a^{\to b}g`$, su cola es finita; para $`B\ge\Delta`$,

```math
\int_a^Bf=\int_a^\Delta f+\int_\Delta^Bf
\le\int_a^\Delta f+K\int_\Delta^Bg.
```

Las integrales parciales $`\int_a^Bf`$ están acotadas superiormente. Por el [lema 4.5.5](#lem-4-5-5), la integral de $`f`$ converge. La segunda afirmación es la contraposición de la primera.

### Diapositiva impresa 24 (PDF p. 34). Comparación en forma límite

<a id="cor-4-5-1"></a>**Corolario 4.5.1.** Sean $`f,g\in\mathcal R_{loc}[a,b)`$, $`f,g>0`$, y supóngase que

```math
\lim_{x\to b-}\frac{f(x)}{g(x)}=\ell\in[0,+\infty].
```

1. Si $`\ell<+\infty`$ y converge $`\int g`$, converge $`\int f`$.
2. Si $`\ell>0`$ y converge $`\int f`$, converge $`\int g`$.
3. Si $`0<\ell<+\infty`$, ambas integrales convergen o divergen simultáneamente.

### Página manuscrita (PDF p. 35). Demostración de comparación límite

1. Si $`\ell=0`$ o es finito positivo, $`f/g`$ está acotado superiormente en un entorno izquierdo de $`b`$, por lo que $`f=O(g)`$ y se aplica el [teorema 4.5.3](#thm-4-5-3).
2. Si $`\ell>0`$, $`g/f`$ está acotado superiormente cerca del extremo; se aplica la comparación a $`g`$ y $`f`$.
3. Para $`0<\ell<+\infty`$, ambas razones están acotadas superiormente cerca del extremo, lo que da equivalencia del carácter de convergencia.

### Diapositiva impresa 25 (PDF p. 36). Observaciones sobre convergencia

1. Las integrales de funciones no negativas equivalentes en una singularidad convergen o divergen conjuntamente.
2. Que converja $`\int_a^{+\infty}f`$ no implica $`f(x)\to0`$ cuando $`x\to+\infty`$, ni siquiera si $`f\ge0`$ y es continua.
3. La acotación de las integrales parciales es necesaria, pero no suficiente. Por ejemplo,

```math
\int_0^{+\infty}\cos x\,dx
```

diverge porque $`\int_0^A\cos x\,dx=\sin A`$ no tiene límite cuando $`A\to+\infty`$.

### Páginas manuscritas (PDF pp. 37–41). Ejemplos y precisión de las observaciones

**PDF pp. 37–38.** Se estudia

```math
\int_2^{+\infty}\frac{dx}{x^\alpha(\ln x)^\beta},\qquad \alpha,\beta\in\mathbb R.
```

Se usa que $`\ln x=o(x^q)`$ para cada $`q>0`$. Si $`\alpha>1`$, el factor logarítmico no cambia la convergencia: para cierto $`q>0`$, el integrando está acotado en una cola por una potencia $`x^{-1-q/2}`$, y la integral converge. Si $`\alpha<1`$, una comparación inferior con una potencia divergente da divergencia. Si $`\alpha=1`$, la sustitución $`t=\ln x`$ reduce el problema a $`\int_{\ln2}^{+\infty}t^{-\beta}\,dt`$, que converge exactamente si $`\beta>1`$.

**PDF pp. 39–40.** El cálculo de $`\int_2^B x^{-p}\,dx`$ vuelve a dar el umbral $`p>1`$ en el infinito. Después se construye una función continua no negativa en $`[0,+\infty)`$, con picos triangulares estrechos cerca de los enteros positivos, altura $`k`$. Sus áreas son del orden de $`1/k^2`$, por lo que $`\sum 1/k^2`$ converge, aunque los valores en los máximos no tienden a cero. Se reproduce el dibujo original.

En la pizarra se define la unión de intervalos

```math
E=\bigcup_{k=1}^{\infty}\left(k-\frac{1}{k^2(k+1)},k+\frac{1}{k^2(k+1)}\right).
```

En cada máximo, $`f(k)=k`$; fuera de $`E`$ la función vale cero y, a cada lado de cada intervalo, la gráfica es lineal, por lo que se forman picos triangulares.

![PDF p. 40: gráfico manuscrito de picos estrechos crecientes; la integrabilidad no implica f(x)→0](../../assets/lectures-2025-26/lec47-48-p40-spike-graph.jpg)

**PDF p. 41.** Cada pico triangular de altura $`k`$ tiene semibase $`1/(k^2(k+1))`$, así que su área es

```math
\frac12\cdot\frac{2}{k^2(k+1)}\cdot k=\frac1{k(k+1)}.
```

Para $`N\in\mathbb N`$, las áreas forman una suma telescópica:

```math
\int_0^{N+1/2}f=\sum_{k=1}^{N}\frac1{k(k+1)}
=\sum_{k=1}^{N}\left(\frac1k-\frac1{k+1}\right)
=1-\frac1{N+1}\longrightarrow1.
```

Por tanto, la integral impropia vale $`1`$, aunque $`f(k)=k`$ no está acotada cuando $`x\to+\infty`$. Una nota manuscrita roja recalca: «¡Pero $`f`$ no está acotada en un entorno de $`+\infty`$!». Esto no contradice la diapositiva impresa 25, que suponía continuidad pero no afirmaba acotación.

---

**Navegación:** [Lecciones 45–46](lecture-45-46.md) · [Lecciones 49–50](lecture-49-50.md) · [Índice](index.md).
