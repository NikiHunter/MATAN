---
title: "Lecciones 67–68 — condiciones suficientes de extremo, extremo condicionado, series numéricas"
lang: es
course: "Análisis matemático, 2025/26"
lecture: 67-68
semester: 3
source: "cuaderno manuscrito, págs. p012–p021"
source_pages: "p012, p013, p014, p015, p016, p017, p018, p019, p020, p021"
course_chapter: 22
aliases: ["Lecciones 67–68 (es)"]
tags: [mathinmind/es, mathinmind/lecture]
---
# Lecciones 67–68 — condiciones suficientes de extremo, extremo condicionado, series numéricas

[[es/lectures-2025-26/lecture-65-66|← Lecciones 65–66]] · [[es/lectures-2025-26/index|Índice de lecciones]] · [[es/lectures-2025-26/lecture-69-70|Lecciones 69–70 →]] · [[es/term-index|Términos y teoremas]] · [[ru/lectures-2025-26/lecture-67-68|Русский]] · [[en/lectures-2025-26/lecture-67-68|English]]

> [!info] Fuente y numeración
> Los apuntes se copiaron de un cuaderno manuscrito (págs. p012–p021; el texto bruto de las páginas está en [`ocr/raw/`](https://github.com/NikiHunter/matan/blob/main/ocr/raw/p012.md)) y se cotejaron con los escaneos de esas páginas. La pág. p012 comienza con el final de la demostración del [[es/lectures-2025-26/lecture-65-66#^thm-6-7-1|teorema 6.7.1]] de las [[es/lectures-2025-26/lecture-65-66|lecciones 65–66]]. Le siguen la fecha «17 de septiembre» en un recuadro, el título «Lecciones 67–68» y el plan de la clase: extremos; [[es/04-numeric-series#4.1 Sumas parciales|series numéricas]]; series convergentes y divergentes; criterios de [[es/04-numeric-series#4.2 Términos no negativos|Cauchy]] y de d'Alembert. Los criterios de Cauchy y de d'Alembert no se vieron en esta clase, véanse las [[es/lectures-2025-26/lecture-69-70|lecciones 69–70]]. El [[#^thm-6-7-2|teorema 6.7.2]] lleva en el cuaderno la nota «(¡hay que saberlo!)»; el cuaderno no tiene demostración y se ha restaurado. El título de §7.1 no se conservó en las diapositivas del curso 2024/25, por lo que se usa el título del cuaderno «Series numéricas». La numeración de definiciones y teoremas es la del profesor (cotejada con las diapositivas del curso 2024/25). Los lapsus de los apuntes se corrigen y se marcan con bloques «Corrección de la fuente»; los pasajes perdidos se restauran y se marcan con bloques «Restaurado»; las etiquetas corresponden a [`ocr/RESOLVED.md`](https://github.com/NikiHunter/matan/blob/main/ocr/RESOLVED.md). Los lugares que aún hay que cotejar con el cuaderno se enumeran en [`ocr/ISSUES.md`](https://github.com/NikiHunter/matan/blob/main/ocr/ISSUES.md).

## §6.7. Extremos de funciones de varias variables (conclusión)


**Demostración del [[es/lectures-2025-26/lecture-65-66#^thm-6-7-1|teorema 6.7.1]] (conclusión).** Recordemos: $a$ es un punto de mínimo de $f$, $V_\delta(a)\subset E$ y $f(x)\ge f(a)$ para $x\in V_\delta(a)$, $h\ne0$, $F(t)=f(a+th)$ para $|t|<\frac{\delta}{\|h\|}$. La función $F$ es diferenciable en cero como composición de la aplicación afín $t\mapsto a+th$ y la aplicación $f$, diferenciable en el punto $a$, y $F'(0)=d_af(h)$. Observemos que para $|t|<\frac{\delta}{\|h\|}$
$$
\|a+th-a\|=\|th\|=|t|\,\|h\|<\delta ,
$$
por tanto,
$$
F(t)=f(a+th)\ge f(a)=F(0)\qquad\forall t\in\left(-\frac{\delta}{\|h\|},\frac{\delta}{\|h\|}\right).
$$
Así, $0$ es un punto de mínimo de la función $F$, interior a su dominio, y por el [[es/lectures-2025-26/lecture-24-25-26#^thm-3-4-1|teorema de Fermat]] $F'(0)=0$, es decir, $d_af(h)=0$ para todo $h\in\mathbb R^n\setminus\{0\}$ (para $h=0$ es evidente). En consecuencia, $d_af=0$. $\square$ ^p012

### Condición suficiente de extremo de una función de varias variables

> [!theorem] Teorema 6.7.2 (condición suficiente de extremo)
> Sean $E\subset\mathbb R^n$, $a$ un punto interior de $E$ y la función $f:E\to\mathbb R$ dos veces diferenciable en el punto $a$, con $d_af=0$. Entonces se cumplen las siguientes afirmaciones.
>
> 1. Si la forma cuadrática $d_a^2f$ es definida positiva (es decir, $d_a^2f(h)>0$ para todo $h\ne0$), entonces $a$ es un punto de mínimo estricto de $f$.
> 2. Si $d_a^2f$ es definida negativa (es decir, $d_a^2f(h)<0$ para todo $h\ne0$), entonces $a$ es un punto de máximo estricto de $f$.
> 3. Si $d_a^2f$ toma valores tanto positivos como negativos, entonces $f$ no tiene extremo en el punto $a$.

^thm-6-7-2

Por ejemplo, para una función de dos variables $f=f(x_1,x_2)$
$$
\nabla f=\left(\frac{\partial f}{\partial x_1},\frac{\partial f}{\partial x_2}\right),\qquad D^2f=\begin{pmatrix}\dfrac{\partial^2f}{\partial x_1^2}&\dfrac{\partial^2f}{\partial x_1\partial x_2}\\[2mm]\dfrac{\partial^2f}{\partial x_2\partial x_1}&\dfrac{\partial^2f}{\partial x_2^2}\end{pmatrix},
$$
y $d_a^2f$ es la forma cuadrática de matriz $D^2f(a)$: $d_a^2f(h)=\sum_{i,j=1}^{2}\frac{\partial^2f}{\partial x_i\partial x_j}(a)h_ih_j$.

> [!note] Restaurado
> (según la demostración estándar, cf. Zorich, t. 1, cap. VIII; en el cuaderno el teorema figura sin demostración).
>
> **Demostración.** Como $f$ es dos veces diferenciable en el punto $a$ y $d_af=0$, por la [[es/lectures-2025-26/lecture-65-66#^def-6-5-1|fórmula de Taylor]]–Peano ([[es/lectures-2025-26/lecture-65-66#^thm-6-5-1|teorema 6.5.1]] para $s=2$, escrita mediante diferenciales)
> $$
> f(a+h)-f(a)=\frac12\,d_a^2f(h)+r(h),\qquad r(h)=o(\|h\|^2)\quad(h\to0).
> $$
> *1)* Sea $d_a^2f$ definida positiva. Una forma cuadrática es continua y la esfera unidad $S=\{h\in\mathbb R^n:\ \|h\|=1\}$ es [[es/lectures-2025-26/lecture-57-58#^def-5-3-7|compacta]], así que $\mu=\min_{h\in S}d_a^2f(h)$ se alcanza y $\mu>0$. Por homogeneidad $d_a^2f(h)=\|h\|^2\,d_a^2f\bigl(h/\|h\|\bigr)\ge\mu\|h\|^2$ para $h\ne0$. Elijamos $\delta>0$ de modo que $V_\delta(a)\subset E$ y $|r(h)|\le\frac{\mu}{4}\|h\|^2$ para $\|h\|<\delta$. Entonces, para $0<\|h\|<\delta$
> $$
> f(a+h)-f(a)\ge\frac{\mu}{2}\|h\|^2-\frac{\mu}{4}\|h\|^2=\frac{\mu}{4}\|h\|^2>0 ,
> $$
> es decir, $a$ es un punto de mínimo estricto de $f$.
>
> *2)* Basta aplicar la afirmación 1) a la función $-f$.
>
> *3)* Sean $d_a^2f(h_1)>0$ y $d_a^2f(h_2)<0$. Para $h\ne0$ fijo y $t\to0$
> $$
> f(a+th)-f(a)=\frac{t^2}{2}\,d_a^2f(h)+o(t^2)=\frac{t^2}{2}\bigl(d_a^2f(h)+o(1)\bigr),
> $$
> por lo que para todo $t\ne0$ suficientemente pequeño se cumplen $f(a+th_1)>f(a)$ y $f(a+th_2)<f(a)$. Así, todo entorno del punto $a$ contiene puntos donde $f>f(a)$ y puntos donde $f<f(a)$, y $a$ no es un punto de extremo de $f$. $\square$

**Observación.** El [[#^thm-6-7-2|teorema 6.7.2]] no abarca la situación en que $d_a^2f$ conserva el signo pero no es ni definida positiva ni definida negativa. En particular, el teorema no afirma nada en el caso $d_a^2f\equiv0$.


**Corolario.** Sean $E\subset\mathbb R^2$, $a$ un [[es/lectures-2025-26/lecture-57-58#Diapositiva impresa 4 (pp. PDF 4) — El interior de un conjunto — definición 5.3.3|punto interior]] de $E$ y $f:E\to\mathbb R$ una función dos veces diferenciable en el punto $a$, $d_af=0$. Pongamos
$$
A=\frac{\partial^2f}{\partial x^2}(a),\qquad B=\frac{\partial^2f}{\partial x\partial y}(a),\qquad C=\frac{\partial^2f}{\partial y^2}(a).
$$
Entonces se cumplen las siguientes afirmaciones. ^p013

1. Si $A>0$ y $AC>B^2$, entonces $a$ es un punto de mínimo estricto de $f$.
2. Si $A<0$ y $AC>B^2$, entonces $a$ es un punto de máximo estricto de $f$.
3. Si $AC<B^2$, entonces $f$ no tiene extremo en el punto $a$.

**Demostración.** Comprobemos primero las afirmaciones 1) y 2). Por la fórmula
$$
d_a^2f(h)=\sum_{i=1}^{2}\sum_{j=1}^{2}\frac{\partial^2f}{\partial x_i\partial x_j}(a)h_ih_j\qquad(h\in\mathbb R^2)
$$
la segunda diferencial $d_a^2f$ es la forma cuadrática con [[es/15-multivariable-differentiation#15.4 Derivadas superiores y Taylor|matriz hessiana]]
$$
H=\begin{pmatrix}A&B\\B&C\end{pmatrix}
$$
(las [[es/lectures-2025-26/lecture-63-64#Diapositiva impresa 16 (pp. PDF 30). Condiciones suficientes de igualdad — teorema 6.4.1|derivadas mixtas]] en el punto $a$ son iguales por el [[es/lectures-2025-26/lecture-63-64#Diapositiva impresa 16 (pp. PDF 30). Condiciones suficientes de igualdad — teorema 6.4.1|teorema 6.4.1]], ya que $f$ es dos veces diferenciable en $a$). Calculemos los menores principales de $H$: $\Delta_1=A$, $\Delta_2=\det H=AC-B^2$. Por el criterio de Sylvester y su corolario:

- $\Delta_1>0$, $\Delta_2>0$ $\Rightarrow$ $d_a^2f$ es definida positiva $\Rightarrow$ se cumple 1) (por el [[#^thm-6-7-2|teorema 6.7.2]]);
- $\Delta_1<0$, $\Delta_2>0$ $\Rightarrow$ $d_a^2f$ es definida negativa $\Rightarrow$ se cumple 2) (por el [[#^thm-6-7-2|teorema 6.7.2]]).

Probemos ahora 3). Por la fórmula
$$
d_a^2f(h)=\sum_{i=1}^{2}\frac{\partial^2f}{\partial x_i^2}(a)h_i^2+2\sum_{1\le i<j\le2}\frac{\partial^2f}{\partial x_i\partial x_j}(a)h_ih_j\qquad(h\in\mathbb R^2)
$$
escribiendo $h=(dx,dy)$, obtenemos
$$
d_a^2f(dx,dy)=A\,dx^2+2B\,dx\,dy+C\,dy^2 .
$$
Fijemos $dy\ne0$. Si $A\ne0$, es un trinomio cuadrático en $dx$ con discriminante
$$
(2B\,dy)^2-4A\,C\,dy^2=4dy^2(B^2-AC)>0 ,
$$
por lo que tiene dos raíces reales distintas y toma valores tanto positivos como negativos. Si $A=0$, entonces $B\ne0$ (ya que $B^2>AC=0$), y $2B\,dy\cdot dx+C\,dy^2$ es una función lineal no constante de $dx$, que también toma valores de ambos signos. Así, $d_a^2f$ toma valores tanto positivos como negativos, y por el [[#^thm-6-7-2|teorema 6.7.2]] $f$ no tiene extremo en el punto $a$. $\square$

> [!info] Corrección de la fuente
> (M051). En los apuntes: «Para $dy\ne0$ fijo tenemos: $4dy^2(B^2-AC)>0$», sin explicar que se trata del discriminante del trinomio en $dx$ y sin el caso $A=0$, en el que la expresión no es un trinomio cuadrático. Se han añadido ambos puntos.


**Observación.** La clasificación del corolario no abarca el caso $AC-B^2=0$. Es el caso en que $d_a^2f(h)$ es un cuadrado perfecto, es decir, tiene la forma
$$
d_a^2f(dx,dy)=\pm(\alpha\,dx+\beta\,dy)^2,\qquad\alpha,\beta\in\mathbb R .
$$
En particular, cuando la segunda diferencial es nula no podemos sacar conclusiones sobre la existencia de extremo de $f$ en el punto $a$. ^p014

**Ejemplo.** Sean $f(x,y)=x^4+3xy^2+y^4$, $a=(0,0)$. Tenemos
$$
\nabla f(x,y)=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y}\right)=(4x^3+3y^2,\ 4y^3+6xy),
$$
$\nabla f(0,0)=(0,0)$, es decir, $d_af=0$ y $(0,0)$ es un punto estacionario. La segunda diferencial viene dada por la matriz hessiana
$$
H_f=\begin{pmatrix}\dfrac{\partial^2f}{\partial x^2}&\dfrac{\partial^2f}{\partial x\partial y}\\[2mm]\dfrac{\partial^2f}{\partial y\partial x}&\dfrac{\partial^2f}{\partial y^2}\end{pmatrix}=\begin{pmatrix}12x^2&6y\\6y&12y^2+6x\end{pmatrix},\qquad H_f(0,0)=\begin{pmatrix}0&0\\0&0\end{pmatrix}.
$$
La matriz es nula — un caso degenerado: $d_a^2f\equiv0$, y el [[#^thm-6-7-2|teorema 6.7.2]] no da nada. Calculemos las terceras derivadas:
$$
\frac{\partial^3f}{\partial x^3}=24x,\qquad\frac{\partial^3f}{\partial x^2\partial y}=0,\qquad\frac{\partial^3f}{\partial x\partial y^2}=6,\qquad\frac{\partial^3f}{\partial y^3}=24y ;
$$
en el punto $(0,0)$ solo $\frac{\partial^3f}{\partial x\partial y^2}(0,0)=6$ es distinta de cero. Por el [[es/lectures-2025-26/lecture-63-64#Diapositiva impresa 21 (pp. PDF 41). Cálculo de diferenciales de orden superior — teorema 6.4.2|teorema 6.4.2]] el multiíndice $(1,2)$ entra en $d_a^3f$ con coeficiente $\frac{3!}{1!\,2!}=C_3^1=3$, por lo que
$$
d_a^3f(dx,dy)=C_3^1\,\frac{\partial^3f}{\partial x\,\partial y^2}(0,0)\,dx\,dy^2=3\cdot6\,dx\,dy^2=18\,dx\,dy^2 ,
$$
es decir, $d_a^3f(h)=18\,h_1h_2^2$.

> [!info] Corrección de la fuente
> (A056). En los apuntes: «$d_a^3f(dx,dy)=C_3^1\frac{\partial^2f}{\partial x\partial y^2}(0,0)\,dx\,dy^2=18\,dx\,dy^2$» (en la transcripción de la página, $\frac{\partial^3f}{\partial x^2\partial y}$). El coeficiente de $dx\,dy^2$ es la derivada de tercer orden $\frac{\partial^3f}{\partial x\partial y^2}(0,0)=6$ (y $\frac{\partial^3f}{\partial x^2\partial y}\equiv0$); con $C_3^1=3$ se obtiene $3\cdot6=18$.

Consideremos $h\in\mathbb R^2\setminus\{(0,0)\}$ con $d_a^3f(h)\ne0$ (por ejemplo, $h=(1,1)$). Pongamos $\varphi(t)=f(th)$, $t\in\mathbb R$. Por la fórmula (∗) de la demostración del [[es/lectures-2025-26/lecture-65-66#^thm-6-5-2|teorema 6.5.2]] tenemos $\varphi^{(k)}(0)=d_a^kf(h)$, por lo que
$$
\varphi'(0)=\varphi''(0)=0,\qquad\varphi'''(0)=d_a^3f(h)\ne0 .
$$
La primera derivada no nula de la función $\varphi$ en cero tiene orden impar, por lo que $\varphi$ no tiene extremo en cero. Así, tampoco $f$ tiene extremo en el punto $(0,0)$: si $(0,0)$ fuera un punto de extremo de $f$, entonces $0$ sería un punto de extremo de $\varphi$. Directamente: $\varphi(t)=f(t,t)=3t^3+2t^4$ cambia de signo al pasar por $0$.


### El problema del extremo condicionado

Sean $f:E\subset\mathbb R^n\to\mathbb R$, $a\in E$ un punto de extremo de $f$. Entonces, en cierto entorno $V(a)$, o bien $f(x)\ge f(a)$ para todo $x\in V(a)\cap E$, o bien $f(x)\le f(a)$ para todo $x\in V(a)\cap E$. Supongamos ahora que no nos interesan todos los puntos $x\in V(a)$, sino solo los que satisfacen ciertas igualdades adicionales llamadas ecuaciones de ligadura. Se habla entonces de extremo condicionado, o relativo, sujeto a esas ecuaciones de ligadura. Por ejemplo, $f:\mathbb R^n\to\mathbb R$, $a$ es un punto de extremo bajo $m$ condiciones adicionales
$$
\begin{cases}\varphi_1(x_1,\ldots,x_n)=\varphi_1(a),\\ \ldots\ldots\ldots\ldots\ldots\\ \varphi_m(x_1,\ldots,x_n)=\varphi_m(a).\end{cases}
$$

> [!info] Corrección de la fuente
> (M058). En los apuntes el número de condiciones adicionales en esta línea se denota $k$, y la última condición, $\varphi_k$; en la [[#^def-6-7-2|definición 6.7.2]] y en lo que sigue el número de condiciones es $m$, y $k$ es el índice de la condición. La notación se ha unificado.

### Extremo condicionado (relativo)

> [!definition] Definición 6.7.2
> Sean $E\subset\mathbb R^n$, $a\in E$, $m\in\mathbb N$, $m<n$, $f,\varphi_1,\ldots,\varphi_m:E\to\mathbb R$. Supongamos que $a$ es un punto de extremo de la restricción de la función $f$ al conjunto
> $$
> \{x\in E:\ \varphi_k(x)=\varphi_k(a),\ k=1,\ldots,m\}.
> $$
> Entonces $a$ se llama punto de extremo condicionado (relativo) de $f$ del tipo correspondiente (mínimo o máximo) sujeto a las ecuaciones de ligadura $\varphi_k(x)=\varphi_k(a)$, donde $k\in\{1,\ldots,m\}$, $x\in E$.

^def-6-7-2

**Observación.** Sin pérdida de generalidad supondremos que $\varphi_k(a)=0$ para todo $k\in\{1,\ldots,m\}$ (en caso contrario sustituimos $\varphi_k$ por $\varphi_k-\varphi_k(a)$).

### Condición necesaria de extremo relativo

Denotemos $\Phi=(\varphi_1,\ldots,\varphi_m)$, es decir, $\Phi:E\subset\mathbb R^n\to\mathbb R^m$; las ecuaciones de ligadura se escriben como $\Phi=0$.

> [!theorem] Teorema 6.7.3 (condición necesaria de extremo relativo)
> Sean $m,n\in\mathbb N$, $m<n$, el conjunto $E$ abierto en $\mathbb R^n$, $a\in E$, $f\in C^1(E)$, $\Phi\in C^1(E,\mathbb R^m)$, $\operatorname{rank}\Phi'(a)=m$. Supongamos además que $a$ es un punto de extremo condicionado de $f$ sujeto a las ecuaciones de ligadura $\Phi=0$ (en particular, $\Phi(a)=0$). Entonces existen $\lambda_1,\ldots,\lambda_m\in\mathbb R$ tales que
> $$
> \operatorname{grad}f(a)=\sum_{k=1}^{m}\lambda_k\operatorname{grad}\varphi_k(a).\qquad(6.7.1)
> $$

^thm-6-7-3


**Observación.** Los números $\lambda_1,\ldots,\lambda_m$ que satisfacen (6.7.1) se llaman [[es/16-implicit-functions-extrema#16.4 Multiplicadores de Lagrange|multiplicadores de Lagrange]].

^p016

**Demostración del [[#^thm-6-7-3|teorema 6.7.3]].** Como $\operatorname{rank}\Phi'(a)=m$, entre las $n$ columnas de la matriz $\Phi'(a)$ (de tamaño $m\times n$) hay $m$ linealmente independientes; renumerando las coordenadas, podemos suponer que son las $m$ últimas columnas. Escribiremos los elementos de $\mathbb R^n$ en la forma $(x,y)$, donde $x\in\mathbb R^{n-m}$, $y\in\mathbb R^m$, y sea $a=(x^0,y^0)$. Entonces $\det\Phi'_y(a)\ne0$.

> [!info] Corrección de la fuente
> (M517). Los apuntes no mencionan la elección de la numeración de las coordenadas, y sin ella no se puede aplicar el teorema de la aplicación implícita: la matriz $\Phi'_y(a)$ debe ser invertible. Lo garantiza la condición $\operatorname{rank}\Phi'(a)=m$.

Denotemos
$$
M=\{(x,y)\in E:\ \varphi_k(x,y)=0\ \ \forall k\in\{1,\ldots,m\}\}.
$$
Por el teorema de la aplicación implícita ([[es/lectures-2025-26/lecture-65-66#^thm-6-6-1|teorema 6.6.1]] para $s=1$, aplicado a la ecuación $\Phi(x,y)=0$) existen un entorno $V(a)\subset E$, un entorno $U(x^0)\subset\mathbb R^{n-m}$ y una aplicación $\psi\in C^1(U(x^0),\mathbb R^m)$ tales que
$$
M\cap V(a)=\{(x,\psi(x)):\ x\in U(x^0)\}.
$$

*Paso 1.* La restricción $f|_M$ tiene un extremo en el punto $a$. Como $\psi$ es continua y $\psi(x^0)=y^0$, los puntos $(x,\psi(x))\in M$ para $x$ cercanos a $x^0$ están arbitrariamente cerca de $a$; por tanto, la función $F(x)=f(x,\psi(x))$, $x\in U(x^0)$, tiene un extremo en el punto $x^0$. Por el [[es/lectures-2025-26/lecture-65-66#^thm-6-7-1|teorema 6.7.1]] $\nabla F(x^0)=0$, y por la fórmula de la observación al [[es/lectures-2025-26/lecture-65-66#^thm-6-6-1|teorema 6.6.1]] (el segundo sumando procede de la derivación respecto del segundo argumento)
$$
f'_x(a)+f'_y(a)\,\psi'(x^0)=0 .
$$

*Paso 2.* Además, del teorema de la aplicación implícita se deduce que $\Phi(x,\psi(x))=0$ para todo $x\in U(x^0)$, de donde (por la misma observación al [[es/lectures-2025-26/lecture-65-66#^thm-6-6-1|teorema 6.6.1]])
$$
\Phi'_x(a)+\Phi'_y(a)\,\psi'(x^0)=0 .
$$
Aquí $\Phi=\begin{pmatrix}\varphi_1\\ \vdots\\ \varphi_m\end{pmatrix}$, $\varphi_i:E\to\mathbb R$, y
$$
\Phi'_x=\begin{pmatrix}\dfrac{\partial\varphi_1}{\partial x_1}&\dfrac{\partial\varphi_1}{\partial x_2}&\cdots&\dfrac{\partial\varphi_1}{\partial x_{n-m}}\\ \vdots&\vdots&&\vdots\\ \dfrac{\partial\varphi_m}{\partial x_1}&\dfrac{\partial\varphi_m}{\partial x_2}&\cdots&\dfrac{\partial\varphi_m}{\partial x_{n-m}}\end{pmatrix}
$$
es una matriz de tamaño $m\times(n-m)$; análogamente, $\Phi'_y$ es una matriz cuadrada de orden $m$, $f'_x(a)$ y $f'_y(a)$ son filas de longitud $n-m$ y $m$, y $\psi'(x^0)$ es una matriz de tamaño $m\times(n-m)$.

*Paso 3.* Así,
$$
\begin{cases}f'_x(a)+f'_y(a)\,\psi'(x^0)=0,\\ \Phi'_x(a)+\Phi'_y(a)\,\psi'(x^0)=0.\end{cases}
$$
Sea $\lambda=(\lambda_1,\ldots,\lambda_m)$ una fila arbitraria. Multiplicando la segunda igualdad por la izquierda por $\lambda$ y restándola de la primera, obtenemos
$$
\bigl[f'_x(a)-\lambda\Phi'_x(a)\bigr]+\bigl[f'_y(a)-\lambda\Phi'_y(a)\bigr]\psi'(x^0)=0.\qquad(*)
$$
Pongamos $\lambda=f'_y(a)\,[\Phi'_y(a)]^{-1}$. Entonces el segundo sumando de (∗) se anula y, por tanto, también el primero: $f'_x(a)=\lambda\Phi'_x(a)$; además, $f'_y(a)=\lambda\Phi'_y(a)$ por la elección de $\lambda$. Así, para todos $i\in\{1,\ldots,n-m\}$ y $j\in\{1,\ldots,m\}$
$$
\frac{\partial f}{\partial x_i}(a)=\sum_{k=1}^{m}\lambda_k\frac{\partial\varphi_k}{\partial x_i}(a),\qquad\frac{\partial f}{\partial y_j}(a)=\sum_{k=1}^{m}\lambda_k\frac{\partial\varphi_k}{\partial y_j}(a).
$$


En consecuencia,
$$
\begin{aligned}
\nabla f(a)&=\left(\frac{\partial f}{\partial x_1}(a),\ldots,\frac{\partial f}{\partial x_{n-m}}(a),\frac{\partial f}{\partial y_1}(a),\ldots,\frac{\partial f}{\partial y_m}(a)\right)\\
&=\sum_{k=1}^{m}\lambda_k\left(\frac{\partial\varphi_k}{\partial x_1}(a),\ldots,\frac{\partial\varphi_k}{\partial x_{n-m}}(a),\frac{\partial\varphi_k}{\partial y_1}(a),\ldots,\frac{\partial\varphi_k}{\partial y_m}(a)\right)=\sum_{k=1}^{m}\lambda_k\nabla\varphi_k(a).
\end{aligned}
$$
Volver a la numeración original de las coordenadas permuta las componentes de todos los [[es/lectures-2025-26/lecture-61-62#Diapositiva impresa 11 (pp. PDF 14). Matriz jacobiana y gradiente — definición 6.1.6|gradientes]] de la misma manera, por lo que la igualdad (6.7.1) se conserva. $\square$ ^p017

### Condición de estacionariedad de la función de Lagrange

> [!theorem] Teorema 6.7.4
> Sean $m,n\in\mathbb N$, $m<n$, el conjunto $E$ abierto en $\mathbb R^n$, $a\in E$, $f\in C^1(E)$, $\Phi\in C^1(E,\mathbb R^m)$, $\operatorname{rank}\Phi'(a)=m$. Supongamos además que $a$ es un punto de extremo condicionado de $f$ sujeto a las ecuaciones de ligadura $\Phi=0$. Denotemos
> $$
> L(x,\lambda)=f(x)-\sum_{k=1}^{m}\lambda_k\varphi_k(x)\qquad(x\in E,\ \lambda\in\mathbb R^m).
> $$
> Entonces existe $\lambda\in\mathbb R^m$ tal que $\operatorname{grad}L(a,\lambda)=0$.

^thm-6-7-4

> [!note] Restaurado
> (según las notas a las diapositivas del curso 2024/25, FS p47; en el cuaderno no hay demostración).
>
> **Demostración.** Tomemos $\lambda=(\lambda_1,\ldots,\lambda_m)$ del [[#^thm-6-7-3|teorema 6.7.3]]. Entonces, en virtud de (6.7.1),
> $$
> \operatorname{grad}_xL(a,\lambda)=\operatorname{grad}f(a)-\sum_{k=1}^{m}\lambda_k\operatorname{grad}\varphi_k(a)=0 .
> $$
> Además, $\frac{\partial L}{\partial\lambda_k}(a,\lambda)=-\varphi_k(a)=0$, ya que $a$ satisface las ecuaciones de ligadura. Por tanto, también se anula el gradiente de $L$ respecto del conjunto de las $n+m$ variables $(x,\lambda)$. $\square$
>
> Así, los puntos de extremo condicionado deben buscarse entre las soluciones del sistema $\operatorname{grad}L(x,\lambda)=0$: son $n+m$ ecuaciones (la condición (6.7.1) y las ecuaciones de ligadura) con $n+m$ incógnitas $x_1,\ldots,x_n,\lambda_1,\ldots,\lambda_m$.

### Condición suficiente de extremo relativo

> [!definition] Definición 6.7.3
> Sean $N$ un subespacio lineal de $\mathbb R^n$ y $f$ una forma cuadrática en $\mathbb R^n$ (aquí $f$ es una forma cuadrática arbitraria, no la función objetivo). La forma $f$ se llama definida positiva en $N$ si $f(x)>0$ para todo $x\in N\setminus\{0\}$, y definida negativa en $N$ si $f(x)<0$ para todo $x\in N\setminus\{0\}$.

^def-6-7-3

**Observación.** Si $f$ es definida positiva en $\mathbb R^n$, es definida positiva en cualquier subespacio lineal $\mathbb R^n$. El recíproco es falso.


> [!theorem] Teorema 6.7.5 (condición suficiente de extremo relativo)
> Sean $m,n\in\mathbb N$, $m<n$, el conjunto $E$ abierto en $\mathbb R^n$, $a\in E$, $f\in C^2(E)$, $\Phi\in C^2(E,\mathbb R^m)$, $\Phi(a)=0$, $\operatorname{rank}\Phi'(a)=m$. Pongamos
> $$
> N=\{h\in\mathbb R^n:\ d_a\Phi(h)=0\},\qquad L(x)=f(x)-\sum_{k=1}^{m}\lambda_k\varphi_k(x)\quad(x\in E),
> $$
> donde $\lambda_1,\ldots,\lambda_m$ satisfacen la condición (6.7.1) en el punto $a$. Entonces se cumplen las siguientes afirmaciones.
>
> 1. Si $d_a^2L$ es definida positiva (negativa) en $N$, entonces $f$ tiene en el punto $a$ un mínimo (máximo) condicionado sujeto a las ecuaciones de ligadura $\Phi=0$.
> 2. Si $d_a^2L$ toma en $N$ valores tanto positivos como negativos, entonces $f$ no tiene en el punto $a$ extremo condicionado sujeto a las ecuaciones de ligadura $\Phi=0$.

^thm-6-7-5

La condición (6.7.1) significa que $a$ es un punto estacionario de la función $L$: $d_aL=0$. La demostración del [[#^thm-6-7-5|teorema 6.7.5]] no figura en los apuntes.

## §7.1. Series numéricas

> [!definition] Definición 7.1.1
> Sea dada una sucesión $(a_n)$, $a_n\in\mathbb R$, $n\in\mathbb N$. Entonces $S_n=a_1+a_2+\ldots+a_n$ se llama suma parcial de la serie, $S=\lim_{n\to\infty}S_n$, suma de la serie; para la suma se usa la notación $S:=\sum_{n=1}^{\infty}a_n$; $a_n$ se llama término general de la serie.

^def-7-1-1

> [!definition] Definición 7.1.2
> La serie $\sum_{n=1}^{\infty}a_n$ converge si la suma de la serie $S$ existe y es finita. En caso contrario la serie diverge.

^def-7-1-2

Así, si $S_n=\sum_{k=1}^{n}a_k$ y $S=\lim_{n\to\infty}S_n$, son posibles tres casos:

1. $S$ existe y es finito ($S\in\mathbb R$): la serie converge;
2. $S$ existe y es infinito ($S=+\infty$ o $S=-\infty$): la serie diverge;
3. $S$ no existe: la serie diverge.

**Ejemplo 1.** La serie $\sum_{n=1}^{\infty}0$ converge, y su suma es $0$, ya que todas las sumas parciales son $S_n=0$.


**Ejemplo 2.** La serie $\sum_{k=1}^{\infty}1$ diverge: $S_n=\sum_{k=1}^{n}1=n$, $\lim_{n\to\infty}S_n=\lim_{n\to\infty}n=+\infty$.

^p019

**Ejemplo 3.** La serie $\sum_{k=0}^{\infty}(-1)^k=1-1+1-1+1-1+\ldots$ diverge. Sus sumas parciales $S_n=\sum_{k=0}^{n}(-1)^k$ valen $1$ para $n$ par y $0$ para $n$ impar, por lo que la sucesión $(S_n)$ no tiene límite ni finito ni infinito.

**Ejemplo 4.** La serie $\sum_{k=1}^{\infty}\frac{1}{k(k+1)}$ converge, y $S=1$:
$$
S_n=\sum_{k=1}^{n}\frac{1}{k(k+1)}=\sum_{k=1}^{n}\left(\frac1k-\frac{1}{k+1}\right)=1-\frac{1}{n+1}\to1\qquad(n\to\infty).
$$

## §7.2. Propiedades de las series

*Propiedad 1.* Si la serie $\sum_{n=1}^{\infty}a_n$ converge, entonces $a_n\to0$ cuando $n\to\infty$.

**Observación.** (a) Si $a_n\not\to0$ cuando $n\to\infty$, la serie $\sum_{n=1}^{\infty}a_n$ diverge (condición necesaria de convergencia). (b) Si $a_n\to0$ cuando $n\to\infty$, la serie $\sum_{n=1}^{\infty}a_n$ no tiene por qué converger (véase más abajo el ejemplo de la serie armónica).

*Propiedad 2.* La serie $\sum_{n=1}^{\infty}a_n$ converge si y solo si para todo $k\in\mathbb N$ converge la serie $\sum_{n=k+1}^{\infty}a_n$, el resto de la serie tras el $k$-ésimo término.

**Demostración de la propiedad 1.** Sean $\sum_{k=1}^{\infty}a_k=S$, $S_N=\sum_{k=1}^{N}a_k$. La serie converge, por lo que $S$ existe y $-\infty<S<+\infty$. Entonces $a_N=S_N-S_{N-1}\to S-S=0$ cuando $N\to\infty$. $\square$

**Ejemplo.** La serie armónica
$$
\sum_{k=1}^{\infty}\frac1k=1+\frac12+\frac13+\frac14+\ldots
$$
diverge, aunque $a_k=\frac1k\to0$. En efecto, agrupemos los términos de la suma parcial $S_{2^m}$:
$$
S_{2^m}=1+\frac12+\left(\frac13+\frac14\right)+\left(\frac15+\ldots+\frac18\right)+\ldots+\left(\frac{1}{2^{m-1}+1}+\ldots+\frac{1}{2^m}\right).
$$
Tras el uno hay $m$ grupos: el $j$-ésimo grupo ($j=1,\ldots,m$) consta de $2^{j-1}$ términos, cada uno de los cuales es al menos $\frac{1}{2^j}$, por lo que la suma del $j$-ésimo grupo es al menos $\frac{2^{j-1}}{2^j}=\frac12$. Por ejemplo, $\frac13+\frac14>\frac12$, $\frac15+\ldots+\frac18>\frac12$, …, $\frac{1}{2^{m-1}+1}+\ldots+\frac{1}{2^m}\ge\frac{2^{m-1}}{2^m}=\frac12$. En consecuencia,
$$
S_{2^m}\ge1+\underbrace{\frac12+\frac12+\ldots+\frac12}_{m}=1+\frac m2\to+\infty\qquad(m\to\infty).
$$
Así, $S_{2^m}\ge1+\frac m2$ para todo $m$ y $S_{2^m}\to+\infty$. Por tanto, la sucesión de sumas parciales $(S_n)$ no está acotada y no tiene límite finito, es decir, la serie armónica diverge (y, como $S_n$ es creciente, $S_n\to+\infty$).

**Demostración de la propiedad 2.** Sea $n>m$. Entonces
$$
\sum_{k=1}^{n}a_k=\sum_{k=1}^{m}a_k+\sum_{k=m+1}^{n}a_k ,\qquad(*)
$$
y el primer sumando de la derecha es un número fijo que no depende de $n$. Hagamos $n\to\infty$ en (∗): los límites de los miembros derecho e izquierdo de (∗) existen (o no existen) simultáneamente.


Denotemos $A=\sum_{k=1}^{m}a_k$. Si $\sum_{k=m+1}^{n}a_k\to S_1=\sum_{k=m+1}^{\infty}a_k$, entonces $\sum_{k=1}^{n}a_k\to A+S_1$, es decir,
$$
\sum_{k=1}^{\infty}a_k=A+S_1=\sum_{k=1}^{m}a_k+\sum_{k=m+1}^{\infty}a_k ;
$$
recíprocamente, si $\sum_{k=1}^{n}a_k\to S$, entonces $\sum_{k=m+1}^{n}a_k\to S-A$. Por tanto, la convergencia de las series $\sum_{k=1}^{\infty}a_k$ y $\sum_{k=m+1}^{\infty}a_k$ es equivalente. $\square$ ^p020

**Corolario (de la propiedad 2).** Si la serie $\sum_{k=1}^{\infty}a_k$ converge, su resto tiende a cero: $\sum_{k=m+1}^{\infty}a_k\to0$ cuando $m\to\infty$.

**Demostración.** Sean $S=\sum_{k=1}^{\infty}a_k$, $S_m=\sum_{k=1}^{m}a_k$. Por la propiedad 2, para todo $m$ el resto converge, y el paso al límite cuando $n\to\infty$ en la igualdad
$$
\sum_{k=m+1}^{n}a_k=\sum_{k=1}^{n}a_k-\sum_{k=1}^{m}a_k
$$
da $\sum_{k=m+1}^{\infty}a_k=S-S_m$. Cuando $m\to\infty$ tenemos $S_m\to S$, por lo que $\sum_{k=m+1}^{\infty}a_k=S-S_m\to S-S=0$. $\square$

*Propiedad 3.* Sean $k\in\mathbb R$, $k\ne0$. Las series $\sum_{n=1}^{\infty}a_n=:(\mathrm{I})$ y $\sum_{n=1}^{\infty}ka_n=:(\mathrm{II})$ convergen y divergen simultáneamente. Si (I) y (II) convergen, entonces $\sum_{n=1}^{\infty}ka_n=k\sum_{n=1}^{\infty}a_n$.

> [!info] Corrección de la fuente
> (M518). En los apuntes: «$k\in\mathbb R$». Para $k=0$ la serie (II) siempre converge, mientras que la serie (I) puede diverger, por lo que la convergencia simultánea solo vale para $k\ne0$. Si la serie (I) converge, la serie (II) converge y $\sum ka_n=k\sum a_n$ para todo $k\in\mathbb R$.

*Propiedad 4.* Sean dos series convergentes $\sum_{n=1}^{\infty}a_n$ y $\sum_{n=1}^{\infty}b_n$. Entonces la serie $\sum_{n=1}^{\infty}(a_n+b_n)$ converge y
$$
\sum_{n=1}^{\infty}(a_n+b_n)=\sum_{n=1}^{\infty}a_n+\sum_{n=1}^{\infty}b_n .
$$

**Demostración de las propiedades 3 y 4.** Para todo $N$
$$
\sum_{n=1}^{N}ka_n=k\sum_{n=1}^{N}a_n,\qquad\sum_{n=1}^{N}(a_n+b_n)=\sum_{n=1}^{N}a_n+\sum_{n=1}^{N}b_n .
$$
Si la serie (I) converge (respectivamente, las series $\sum a_n$ y $\sum b_n$ convergen), los miembros derechos tienen límites finitos cuando $N\to\infty$; por las propiedades de los [[es/lectures-2025-26/lecture-08#^def-2-1-2|límites de sucesiones]] también los tienen los miembros izquierdos, y
$$
\sum_{n=1}^{\infty}ka_n=k\sum_{n=1}^{\infty}a_n,\qquad\sum_{n=1}^{\infty}(a_n+b_n)=\sum_{n=1}^{\infty}a_n+\sum_{n=1}^{\infty}b_n .
$$
Si converge la serie (II) y $k\ne0$, las sumas parciales de la serie (I) son las sumas parciales de la serie (II) multiplicadas por $\frac1k$ y también tienen límite finito. $\square$

**Observación.** Si la serie $\sum_{n=1}^{\infty}a_n$ diverge y la serie $\sum_{n=1}^{\infty}b_n$ converge, entonces la serie $\sum_{n=1}^{\infty}(a_n+b_n)$ diverge. En efecto, si convergiera, por las propiedades 3 y 4 convergería también la serie de términos $a_n=(a_n+b_n)-b_n$. Contradicción.


### Criterio de Bolzano–Cauchy

La serie $\sum_{n=1}^{\infty}a_n$ converge si y solo si
$$
\forall\varepsilon>0\ \exists N\in\mathbb N\ \forall n>N\ \forall p\in\mathbb N\qquad\left|\sum_{k=n+1}^{n+p}a_k\right|=|a_{n+1}+\ldots+a_{n+p}|<\varepsilon .
$$

> [!info] Corrección de la fuente
> (T078). En los apuntes: «$\forall p>0$». Aquí $p$ es el número de sumandos, es decir, $p\in\mathbb N$ (así también en la demostración).

**Demostración.** Por definición la serie $\sum_{n=1}^{\infty}a_n$ converge si y solo si la sucesión de sus sumas parciales $S_m:=\sum_{n=1}^{m}a_n$ tiene límite finito cuando $m\to\infty$. Por el criterio de Bolzano–Cauchy para sucesiones (probado antes) esto equivale a la condición
$$
\forall\varepsilon>0\ \exists N\in\mathbb N:\ \forall m,n>N\qquad|S_m-S_n|<\varepsilon .
$$
Sin pérdida de generalidad $m>n$ (para $m=n$ la diferencia es nula, y $|S_m-S_n|=|S_n-S_m|$). Pongamos $p:=m-n\in\mathbb N$; entonces $S_m-S_n=\sum_{k=n+1}^{n+p}a_k$, y la última condición coincide con la del criterio. $\square$

### Cómo probar que una serie diverge

Del criterio de Bolzano–Cauchy se obtiene un modo de probar la divergencia de una serie: hay que hallar una sucesión de enteros $(m_n)$, $m_n>n$, tal que
$$
\sum_{k=n}^{m_n}a_k\not\to0\qquad(n\to\infty).
$$
Si la serie convergiera, por el criterio de Bolzano–Cauchy tales sumas tenderían a cero.

**Observación.** A menudo se elige $m_n=\alpha n$, donde $\alpha>1$ (por ejemplo, $m_n=2n$).

**Ejemplo.** Para la serie armónica tomemos $m_n=2n$:
$$
\sum_{k=n}^{2n}\frac1k=\frac1n+\frac{1}{n+1}+\ldots+\frac{1}{2n}\ge\underbrace{\frac{1}{2n}+\frac{1}{2n}+\ldots+\frac{1}{2n}}_{n+1}=\frac{n+1}{2n}>\frac12 ,
$$
por lo que $\sum_{k=n}^{2n}\frac1k\not\to0$, y la serie armónica diverge (otra demostración).

> [!info] Corrección de la fuente
> (T080). En la transcripción de la página: «$\sum_{k=n}^{2n}\frac1k\to(n+1)\frac{1}{2n}\to0$»; en el cuaderno, «$\ge(n+1)\frac{1}{2n}\not\to0$» (la flecha está tachada). La estimación correcta es $\sum_{k=n}^{2n}\frac1k\ge\frac{n+1}{2n}\to\frac12$, es decir, estas sumas no tienden a cero.

### Convergencia absoluta

> [!definition] Definición 7.2.1
> La serie $\sum_{n=1}^{\infty}a_n$ se llama absolutamente convergente si la serie $\sum_{n=1}^{\infty}|a_n|$ converge.

^def-7-2-1

*Propiedad 5.* Si una serie converge absolutamente, converge.

**Demostración de la propiedad 5.** Tomemos un $\varepsilon>0$ arbitrario y apliquemos el criterio de Bolzano–Cauchy. Sabemos que la serie $\sum_{k=1}^{\infty}|a_k|$ converge; por el criterio de Bolzano–Cauchy existe $N\in\mathbb N$ tal que $\sum_{k=n+1}^{n+p}|a_k|<\varepsilon$ para todos $n>N$ y $p\in\mathbb N$. Pero entonces
$$
\left|\sum_{k=n+1}^{n+p}a_k\right|\le\sum_{k=n+1}^{n+p}|a_k|<\varepsilon\qquad(n>N,\ p\in\mathbb N),
$$
y por el criterio de Bolzano–Cauchy la serie $\sum_{k=1}^{\infty}a_k$ converge. $\square$

## Referencias cruzadas

- Tema en el curso: [[es/16-implicit-functions-extrema|capítulo 16 «Funciones inversas e implícitas; extremos»]], [[es/04-numeric-series|capítulo 4 «Series numéricas»]].
- Hechos usados: la fórmula de Taylor–Peano ([[es/lectures-2025-26/lecture-65-66#^thm-6-5-1|teorema 6.5.1]]), la afirmación (∗) de la demostración del [[es/lectures-2025-26/lecture-65-66#^thm-6-5-2|teorema 6.5.2]], el [[es/lectures-2025-26/lecture-65-66#^thm-6-6-1|teorema 6.6.1]] de la [[es/lectures-2025-26/lecture-65-66#^def-6-6-1|aplicación implícita]] y su observación — [[es/lectures-2025-26/lecture-65-66|lecciones 65–66]]; el [[es/lectures-2025-26/lecture-63-64#Diapositiva impresa 16 (pp. PDF 30). Condiciones suficientes de igualdad — teorema 6.4.1|teorema 6.4.1]] sobre la igualdad de las derivadas mixtas y el [[es/lectures-2025-26/lecture-63-64#Diapositiva impresa 21 (pp. PDF 41). Cálculo de diferenciales de orden superior — teorema 6.4.2|teorema 6.4.2]] sobre las diferenciales de orden superior — [[es/lectures-2025-26/lecture-63-64|lecciones 63–64]]; el criterio de Bolzano–Cauchy para sucesiones — [[es/lectures-2025-26/lecture-13#^thm-2-3-7|teorema 2.3.7]].
- Continuación: series positivas, criterios de comparación, criterios de d'Alembert y de Cauchy — [[es/lectures-2025-26/lecture-69-70|lecciones 69–70]].

---

[[es/lectures-2025-26/lecture-65-66|← Lecciones 65–66]] · [[es/lectures-2025-26/index|Índice de lecciones]] · [[es/lectures-2025-26/lecture-69-70|Lecciones 69–70 →]] · [[es/term-index|Términos y teoremas]] · [[ru/lectures-2025-26/lecture-67-68|Русский]] · [[en/lectures-2025-26/lecture-67-68|English]]
