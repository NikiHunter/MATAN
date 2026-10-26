---
title: "Lecciones 45–46 — Sustitución, Taylor, Wallis y desigualdades integrales"
lang: es
course: "Análisis matemático, 2025/26"
lecture: 45-46
semester: 2
date: 2026-03-26
source: "ma25_26-lectures_45-46_notes.pdf"
pdf_pages: 29
typed_slides: 14
archive_file: "Лекция 45-46.md"
---
# Lecciones 45–46 — Sustitución, fórmulas de Taylor y Wallis, desigualdades integrales

[Índice de lecciones](index.md) · [Русский](../../ru/lectures-2025-26/lecture-45-46.md) · [English](../../en/lectures-2025-26/lecture-45-46.md) · [Anterior: 43–44](lecture-43-44.md) · [Siguiente: 47–48](lecture-47-48.md)

> **Fuente:** `ma25_26-lectures_45-46_notes.pdf` — 29 páginas PDF, 14 diapositivas impresas; la fecha impresa es 26 de marzo de 2026. Páginas impresas: 1–7, 10–12, 18, 22, 26 y 29. Páginas manuscritas: 8–9, 13–17, 19–21, 23–25 y 27–28. No falta ninguna página PDF: las 29 se contabilizan exactamente una vez. La numeración de diapositivas (1–14) no es la numeración de páginas PDF.
>
> **Duplicación del semestre 2.** El semestre 1 termina con la lección 32; el semestre 2 comprende las lecciones 33–64. Esta lección coincide íntegramente con [§4.3, «Propiedades de la integral de Riemann»](../../ru/lectures/04-riemann-properties-4-3.md) y [§4.4, «Taylor, Wallis y desigualdades integrales»](../../ru/lectures/05-taylor-wallis-inequalities-4-4.md), y también aparece en el [registro existente del semestre 2](../../ru/lectures/index.md). El original archivado, sin modificar, es [«Лекция 45-46.md»](../../../source/MathInMind/МАТАН_Л/Лекция%2045-46.md). Estas referencias complementan, pero no sustituyen, esta transcripción ilustrada completa del PDF.
>
> **Criterios editoriales.** Se conserva la numeración, incluido el salto de 4.3.3 a 4.3.5; no se inventa el teorema 4.3.4. Las fórmulas y los pasos manuscritos se transcriben de las imágenes; las aclaraciones editoriales se identifican como tales. Las integrales son propias salvo indicación expresa.

## Diapositiva impresa 1 (PDF p. 1). Portada

«Análisis matemático», lecciones 45–46, 26 de marzo de 2026; D. E. Apushkinskaya, Universidad RUDN.

## Diapositiva impresa 2 (PDF p. 2). Cita del día

«Nada ayuda tanto con las tareas de casa como desconectar Internet».

## Diapositiva impresa 3 (PDF p. 3). Objetivos

1. Observaciones sobre el teorema de cambio de variable en la integral definida.
2. Fórmulas de Taylor y Wallis y desigualdades integrales.

## Capítulo 4. Cálculo integral, §3. Propiedades de la integral de Riemann

### Diapositiva impresa 4 (PDF p. 4). Cambio de variable

**Teorema 4.3.5.** Sean $\varphi:[\alpha,\beta]\to[A,B]$, diferenciable en $[\alpha,\beta]$, con $\varphi'\in\mathcal R[\alpha,\beta]$, y $f\in C[A,B]$. Entonces

$$
\int_\alpha^\beta (f\circ\varphi)(x)\varphi'(x)\,dx
=\int_{\varphi(\alpha)}^{\varphi(\beta)} f(t)\,dt.
$$

### Diapositiva impresa 5 (PDF p. 5). Observaciones sobre la sustitución

1. Algunos valores $\varphi(t)$, con $t\in[\alpha,\beta]$, pueden quedar fuera del intervalo comprendido entre $\varphi(\alpha)$ y $\varphi(\beta)$. El recorrido de $\varphi$ puede sobrepasar los extremos, pero cada $\varphi(t)$ pertenece a $[A,B]$, donde está definida $f$.
2. El límite inferior no tiene que ser menor que el superior. Si $\varphi$ es estrictamente decreciente y $\alpha<\beta$, entonces $\varphi(\alpha)>\varphi(\beta)$; la integral orientada ya tiene en cuenta esta situación.

## §4. Fórmulas de Taylor y Wallis y desigualdades integrales

### Diapositiva impresa 6 (PDF p. 6). Título de sección

«§4. Fórmulas de Taylor y Wallis y desigualdades integrales».

### Diapositiva impresa 7 (PDF p. 7). Taylor con resto integral

**Teorema 4.4.1.** Sean $n\in\mathbb Z_+$, $f\in C^{n+1}\langle A,B\rangle$ y $a,x\in\langle A,B\rangle$. Entonces

$$
f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k+
\frac1{n!}\int_a^x f^{(n+1)}(t)(x-t)^n\,dt.
$$

### Página manuscrita (PDF p. 8). Demostración del teorema 4.4.1: base e integración por partes

La demostración en la pizarra comienza por inducción. Para $n=0$, por el teorema fundamental del cálculo,

$$
f(x)=f(a)+\int_a^x f'(t)\,dt.
$$

Suponiendo la fórmula para $n-1$, el resto es

$$
\frac1{(n-1)!}\int_a^x f^{(n)}(t)(x-t)^{n-1}\,dt
=\int_a^x f^{(n)}(t)\,d\!\left(-\frac{(x-t)^n}{n!}\right).
$$

La integración por partes produce la expresión con la que termina esta página:

$$
=-\frac1{n!}\left[f^{(n)}(t)(x-t)^n\right]_{t=a}^{x}
+\frac1{n!}\int_a^x f^{(n+1)}(t)(x-t)^n\,dt.
$$

### Página manuscrita (PDF p. 9). Final de la demostración de Taylor

El término de frontera se reduce a

$$
-\frac1{n!}\left[f^{(n)}(t)(x-t)^n\right]_{a}^{x}
=-\frac1{n!}\left(0-f^{(n)}(a)(x-a)^n\right)
=\frac{f^{(n)}(a)}{n!}(x-a)^n.
$$

Al sustituirlo en la hipótesis de inducción se añade el término de índice $n$ a la suma y queda el resto de orden $n+1$ del teorema 4.4.1. La pizarra identifica como factores de la integración por partes a $f^{(n)}(t)$ y $-(x-t)^n/n!$.

### Diapositiva impresa 8 (PDF p. 10). Observaciones sobre el resto integral

1. La forma integral del resto también se llama forma de C. Jacobi.
2. Por el primer teorema del valor medio, bajo las hipótesis del teorema 4.4.1 existe $c\in[a,x]$ (si $x<a$, se usa la integral orientada) tal que

$$
\frac1{n!}\int_a^x f^{(n+1)}(t)(x-t)^n\,dt
=\frac{f^{(n+1)}(c)}{n!}\int_a^x(x-t)^n\,dt
=\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}.
$$

3. La ventaja de la forma integral es que no contiene un punto desconocido $c$.

### Diapositiva impresa 9 (PDF p. 11). Fórmula de Wallis

El factorial doble $m!!$ es el producto de los naturales no mayores que $m$ y de la misma paridad que $m$; por convenio, $0!!=(-1)!!=1$.

**Teorema 4.4.2.**

$$
\pi=\lim_{n\to\infty}\frac1n\left(\frac{(2n)!!}{(2n-1)!!}\right)^2.
$$

### Diapositiva impresa 10 (PDF p. 12). Integrales de potencias del seno

**Lema 4.4.1.** Si $m\in\mathbb Z_+$, entonces

$$
\int_0^{\pi/2}\sin^m x\,dx
=\frac{(m-1)!!}{m!!}\begin{cases}
\dfrac\pi2,&m\text{ par},\\[2pt]
1,&m\text{ impar}.
\end{cases}
$$

### Página manuscrita (PDF p. 13). Demostración del lema 4.4.1: notación y casos base

Se define $J_m=\int_0^{\pi/2}\sin^m x\,dx$. Los casos base son

$$
J_0=\int_0^{\pi/2}dx=\frac\pi2,\qquad
J_1=\int_0^{\pi/2}\sin x\,dx=[-\cos x]_0^{\pi/2}=1.
$$

Las anotaciones rojas verifican la fórmula de factoriales dobles para $m=0$ y $m=1$; después se obtiene la recurrencia mediante integración por partes para $m\ge2$.

### Página manuscrita (PDF p. 14). Recurrencia para $J_m$

Se escribe $J_m=\int_0^{\pi/2}\sin^{m-1}x\,d(-\cos x)$. La integración por partes, $d(\sin^{m-1}x)=(m-1)\sin^{m-2}x\cos x\,dx$ y $\cos^2x=1-\sin^2x$ dan

$$
J_m=(m-1)\left(J_{m-2}-J_m\right),\qquad
mJ_m=(m-1)J_{m-2},\qquad
J_m=\frac{m-1}{m}J_{m-2}.
$$

El término de frontera $[-\sin^{m-1}x\cos x]_0^{\pi/2}$ es cero.

### Página manuscrita (PDF p. 15). Primeros valores impares y comparación

Para índices impares se escriben

$$
J_3=\frac23J_1=\frac23,\qquad
J_5=\frac45J_3=\frac45\frac23,
\qquad J_7=\frac67J_5=\frac67\frac45\frac23.
$$

Después se usa que $0<\sin x<1$ para $0<x<\pi/2$:

$$
\sin^{2n+1}x<\sin^{2n}x<\sin^{2n-1}x.
$$

### Página manuscrita (PDF p. 16). Primeros valores pares y comparación integral

Para índices pares:

$$
J_2=\frac12J_0=\frac\pi4,\qquad
J_4=\frac34J_2=\frac34\frac12\frac\pi2,
\qquad J_6=\frac56J_4=\frac56\frac34\frac12\frac\pi2.
$$

Al integrar la comparación de la p. 15 se obtiene $J_{2n+1}<J_{2n}<J_{2n-1}$.

### Página manuscrita (PDF p. 17). Demostración de la fórmula de Wallis

Al sustituir las expresiones del lema se obtiene

$$
\frac{(2n)!!}{(2n+1)!!}
<\frac{(2n-1)!!}{(2n)!!}\frac\pi2
<\frac{(2n-2)!!}{(2n-1)!!}.
$$

Multiplicando por $\frac{(2n)!!}{(2n-1)!!}$ y usando $(2n+1)!!=(2n+1)(2n-1)!!$, $(2n)!!=2n(2n-2)!!$, resulta

$$
\frac1{2n+1}\left(\frac{(2n)!!}{(2n-1)!!}\right)^2
<\frac\pi2<
\frac1{2n}\left(\frac{(2n)!!}{(2n-1)!!}\right)^2.
$$

Sea $x_n=\frac1n\left(\frac{(2n)!!}{(2n-1)!!}\right)^2$. Entonces $\frac{2n}{2n+1}x_n<\pi<x_n$, o equivalentemente $\pi<x_n<\frac{2n+1}{2n}\pi$. Ambos extremos tienden a $\pi$, y el teorema del encaje demuestra el teorema 4.4.2.

### Diapositiva impresa 11 (PDF p. 18). Segundo teorema del valor medio de Bonnet

**Teorema 4.4.3 (O. Bonnet).** Sean $f\in C[a,b]$, $g\in C^1[a,b]$ y $g$ monótona en $[a,b]$. Existe $c\in[a,b]$ tal que

$$
\int_a^b fg=g(a)\int_a^c f+g(b)\int_c^b f.
$$

### Página manuscrita (PDF p. 19). Demostración de Bonnet: integración por partes

Sea $F(x)=\int_a^x f$; entonces $F(a)=0$ y $F'=f$. Por tanto,

$$
\int_a^b fg=\int_a^b gF'
=-\int_a^b Fg'+[Fg]_a^b
=-\int_a^b Fg'+g(b)\int_a^b f.
$$

### Página manuscrita (PDF p. 20). Aplicación del primer teorema del valor medio

Como $g$ es monótona y diferenciable, $g'$ conserva el signo. El primer teorema del valor medio ponderado, aplicado a $F$ con peso $g'$, proporciona un $c\in[a,b]$ tal que

$$
\int_a^b Fg'=F(c)\int_a^b g'=F(c)(g(b)-g(a)).
$$

Como $F(c)=\int_a^c f$, al sustituir en la línea anterior se obtiene

$$
\int_a^b fg
=-\left(g(b)-g(a)\right)\int_a^c f+g(b)\int_a^b f
=g(a)\int_a^c f+g(b)\int_c^b f.
$$

### Página manuscrita (PDF p. 21). Esquema geométrico del intervalo

El dibujo manuscrito marca $[a,b]$, el punto $c$ y las dos partes $\int_a^c f$ y $\int_c^b f$. El arco rojo abarca el intervalo completo y el verde la primera parte. Es un esquema de la descomposición de la fórmula de Bonnet, no una gráfica de una función.

![PDF p. 21: esquema original de Bonnet con c y los dos intervalos de integración](../../assets/lectures-2025-26/lec45-46-p21-bonnet-interval.jpg)

### Diapositiva impresa 12 (PDF p. 22). Observaciones sobre Bonnet

1. El teorema de Bonnet sigue siendo válido bajo hipótesis más débiles: $f\in\mathcal R[a,b]$ y $g$ monótona en $[a,b]$.
2. El segundo teorema del valor medio normalmente no aporta resultados nuevos respecto de los que se obtienen por integración por partes.

### Página manuscrita (PDF p. 23). Estimación de una integral oscilatoria

La pizarra considera

$$
I=\int_{100\pi}^{200\pi}\frac{\sin x}{x}\,dx.
$$

La integral no tiene primitiva elemental, pero puede estimarse. Como $x>0$ en el intervalo,

$$
|I|\le\int_{100\pi}^{200\pi}\frac{|\sin x|}{x}\,dx
\le\int_{100\pi}^{200\pi}\frac{dx}{x}
=\log 2.
$$

La página también comienza una estimación más detallada por periodos:

$$
I=\sum_{k=100}^{199}\int_{k\pi}^{(k+1)\pi}\frac{\sin x}{x}\,dx,
\qquad
\left|\int_{k\pi}^{(k+1)\pi}\frac{\sin x}{x}\,dx\right|
\le\frac{2}{k\pi}.
$$

Esto da una cota gruesa del orden de $\sum_{k=100}^{199}2/(k\pi)$; la página también indica la cota superior $\log 2$ para la integral del valor absoluto.

### Página manuscrita (PDF p. 24). Estimación mediante la fórmula de Bonnet

Se toma $g(x)=1/x$, monótona, y $f(x)=\sin x$. El teorema de Bonnet en $[100\pi,200\pi]$ da algún $c\in[100\pi,200\pi]$ tal que

$$
I=g(100\pi)\int_{100\pi}^{c}\sin x\,dx
+g(200\pi)\int_c^{200\pi}\sin x\,dx.
$$

Al integrar $\sin x$ aparecen expresiones de extremos con $[-\cos x]$. Como $\cos(100\pi)=\cos(200\pi)=1$, los términos de frontera se simplifican y se acotan los dos sumandos.

### Página manuscrita (PDF p. 25). Final de la estimación

Usando $\cos c\in[-1,1]$ y la fórmula anterior, el cálculo escrito se reduce a $(1-\cos c)/(200\pi)$ y, por tanto, $0\le I\le1/(100\pi)$. **Nota de transcripción:** en la página manuscrita la notación de la integral del valor absoluto y la integral con signo queda muy próxima. Aquí se distinguen: una cota para la integral con signo no demuestra convergencia absoluta del integrando $f$.

### Diapositiva impresa 13 (PDF p. 26). Desigualdad integral de Jensen

**Teorema 4.4.4.** Sea $f$ convexa y continua en $\langle A,B\rangle$, sea $\varphi:[a,b]\to\langle A,B\rangle$ continua, y sea $\lambda:[a,b]\to[0,+\infty)$ continua con $\int_a^b\lambda=1$. Entonces

$$
f\left(\int_a^b\lambda\varphi\right)
\le\int_a^b\lambda\,(f\circ\varphi).
$$

### Página manuscrita (PDF p. 27). Prueba de Jensen: recta de soporte

Se definen

$$
E=\{x\in[a,b]:\lambda(x)>0\},\qquad
m=\inf_E\varphi,\qquad M=\sup_E\varphi,
$$

y $c=\int_a^b\lambda\varphi$. Por continuidad, $\varphi$ está acotada en el intervalo. Si $m=M$, $\varphi$ es constante en $E$ y hay igualdad. Si $m<M$, entonces $c\in[m,M]$; la convexidad proporciona una recta de soporte $y=\alpha x+\beta$ en $c$:

$$
f(c)=\alpha c+\beta,\qquad f(t)\ge\alpha t+\beta.
$$

### Página manuscrita (PDF p. 28). Prueba de Jensen: integrar la recta de soporte

Multiplicando la desigualdad de soporte por $\lambda\ge0$ e integrando,

$$
\int_a^b\lambda f(\varphi)
\ge\int_a^b\lambda(\alpha\varphi+\beta)
=\alpha\int_a^b\lambda\varphi+\beta\int_a^b\lambda
=\alpha c+\beta=f(c).
$$

Esto demuestra el teorema 4.4.4. El argumento manuscrito usa continuidad y convexidad en el intervalo de valores de $\varphi$.

### Diapositiva impresa 14 (PDF p. 29). Observaciones sobre Jensen

1. Si $\varphi$ no es constante en $E=\{x\in[a,b]:\lambda(x)>0\}$ y $f$ es estrictamente convexa, la desigualdad de Jensen es estricta.
2. Para una función cóncava $f$, la desigualdad se cumple con el signo contrario.

---

**Navegación:** [Lecciones 43–44](lecture-43-44.md) · [Lecciones 47–48](lecture-47-48.md) · [Índice](index.md).
