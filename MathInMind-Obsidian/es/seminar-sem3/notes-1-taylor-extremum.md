---
title: "Seminario NM-204. Apuntes, parte 1: fórmula de Taylor y extremos condicionados"
lang: es
tags: [mathinmind/es, mathinmind/other]
---
# Apuntes de los seminarios, parte 1: fórmula de Taylor y extremos condicionados

[[ru/seminar-sem3/notes-1-taylor-extremum|Русский]] · [[en/seminar-sem3/notes-1-taylor-extremum|English]] · **Español**

[[es/seminar-sem3/index|Todas las tareas y apuntes]] · [[es/seminar-sem3/notes-2-series-basics|Parte 2: fundamentos de series →]]

> [!note] Qué es esto
> Una versión reelaborada de los seminarios del 4, 9, 18 y 20 de septiembre de 2026. La base es la transcripción OCR de las pizarras manuscritas de la carpeta [`sem3_notes`](https://github.com/NikiHunter/matan/blob/main/sem3_notes/README.md) (en ruso). Los números de los enunciados se conservan como en la pizarra (2.1, 3.1, …) para que coincidan con las referencias del profesor. La redacción formal se ha sustituido por lenguaje llano, y cada enunciado lleva una nota «por qué funciona» y un enlace al problema de la tarea. Todos los cálculos se comprobaron con sympy. Los errores de reconocimiento están corregidos y se enumeran [[#Qué se corrigió respecto a la transcripción OCR|al final de la página]].

| Fecha | Qué se vio | Tareas |
|---|---|---|
| 4 sep. | [[#Observación 2.1. Un segmento es el conjunto de combinaciones convexas de sus extremos\|observación 2.1]] (segmentos), [[#^ex-2-2\|ejemplo 2.2]] (Taylor de un polinomio), [[#Definición 2.3. Extremo local condicionado\|definición 2.3]] (extremo condicionado) | [[es/seminar-sem3/hw1-taylor#Problema 1.1\|1.1]] |
| 9 sep. | [[#Teorema 3.1. Extremos condicionados y la matriz hessiana orlada\|teorema 3.1]] (hessiana orlada), [[#^ex-3-2\|ejemplo 3.2]] | el método para toda la [[es/seminar-sem3/hw2-conditional-extremum\|tarea 2]] |
| 18 sep. | [[#^ex-4-1\|ejemplo 4.1]] (Taylor con resto), [[#^ex-4-2\|ejemplo 4.2]] (extremo sobre una recta) | [[es/seminar-sem3/hw1-taylor#Problema 1.4\|1.4]], [[es/seminar-sem3/hw2-conditional-extremum#Problema 2.1\|2.1]] |
| 20 sep. | [[#^ex-5-1\|ejemplo 5.1]] (extremo en $\mathbb R^4$, dos ligaduras) | [[es/seminar-sem3/hw2-conditional-extremum#Problema 2.3\|2.3]], variante con $y^2$ |

## Seminario del 4 de septiembre: segmentos, fórmula de Taylor, extremos condicionados

### Observación 2.1. Un segmento es el conjunto de combinaciones convexas de sus extremos

**Afirmación.** Si $a<b$, entonces $[a;b]=\{\lambda a+(1-\lambda)b\mid 0\le\lambda\le1\}$.

**Demostración.** Inclusión «$\subset$»: sea $a\le x\le b$ y tomemos $\lambda=\frac{b-x}{b-a}$. De $a\le x\le b$ se sigue $0\le\lambda\le1$, y
$$
\lambda a+(1-\lambda)b=b-\lambda(b-a)=b-(b-x)=x.
$$
Inclusión «$\supset$»: si $x=\lambda a+(1-\lambda)b$ con $\lambda\in[0;1]$, entonces $x-a=(1-\lambda)(b-a)\ge0$ y $b-x=\lambda(b-a)\ge0$. $\blacksquare$

**Para qué sirve.** En la fórmula de Taylor de varias variables el punto intermedio está en el segmento $[u;u+h]=\{u+th\mid t\in[0;1]\}$. Es la misma descripción mediante combinaciones convexas de los extremos (con $\lambda=1-t$). Por eso la región donde se aplica la fórmula debe contener todo el segmento, por ejemplo siendo convexa; es justo lo que supone el [[#Teorema 3.1. Extremos condicionados y la matriz hessiana orlada|teorema 3.1]].

### Ejemplo 2.2. Fórmula de Taylor para $x^3+y^3+z^3-3xyz$ (= [[es/seminar-sem3/hw1-taylor#Problema 1.1|problema 1.1]])

**Enunciado.** $f(x;y;z)=x^3+y^3+z^3-3xyz$. Desarrollarla por la fórmula de Taylor en $(1;1;1)$ y en $(1;-1;2)$.

^ex-2-2

**La fórmula.** Para un punto $u\in\mathbb R^n$, un incremento $h$ y multiíndices $\alpha=(\alpha_1,\dots,\alpha_n)$,
$$
f(u+h)=\sum_{|\alpha|\le m}D^\alpha f(u)\,\frac{h^\alpha}{\alpha!}+R_m(h),\qquad h^\alpha=h_1^{\alpha_1}\cdots h_n^{\alpha_n},\quad \alpha!=\alpha_1!\cdots\alpha_n!,
$$
$$
R_m(h)=\sum_{|\alpha|=m+1}D^\alpha f(u+t_0h)\,\frac{h^\alpha}{\alpha!}\quad\text{para algún }t_0\in(0;1)\quad\text{(resto en forma de Lagrange)}.
$$
Por ejemplo, $D^{(1;1;0)}f=f''_{xy}$ y $(1;1;0)!=1!\cdot1!\cdot0!=1$.

**Derivadas.**
$$
f'_x=3x^2-3yz,\qquad f'_y=3y^2-3xz,\qquad f'_z=3z^2-3xy;
$$
$$
f''_{xx}=6x,\quad f''_{yy}=6y,\quad f''_{zz}=6z,\quad f''_{xy}=-3z,\quad f''_{xz}=-3y,\quad f''_{yz}=-3x;
$$
$$
f'''_{xxx}=f'''_{yyy}=f'''_{zzz}=6,\qquad f'''_{xyz}=-3.
$$
Las demás derivadas de tercer orden y todas las de orden $\ge4$ son nulas. Por eso con $m=3$ el resto $R_3\equiv0$ y el desarrollo es exacto.

**El punto $(1;-1;2)$**, $h=(x-1;\,y+1;\,z-2)$. Valores: $f=1-1+8+6=14$; $f'_x=9$, $f'_y=-3$, $f'_z=15$; $\frac{f''_{xx}}{2!}=3$, $\frac{f''_{yy}}{2!}=-3$, $\frac{f''_{zz}}{2!}=6$, $f''_{xy}=-6$, $f''_{xz}=3$, $f''_{yz}=-3$. Resultado:
$$
f=14+9h_1-3h_2+15h_3+3h_1^2-3h_2^2+6h_3^2-6h_1h_2+3h_1h_3-3h_2h_3+h_1^3+h_2^3+h_3^3-3h_1h_2h_3.
$$

**El punto $(1;1;1)$** (no se hizo en la pizarra; la respuesta es de la tarea): $f(1;1;1)=0$, todas las primeras derivadas se anulan, y
$$
f=3\bigl(h_1^2+h_2^2+h_3^2-h_1h_2-h_1h_3-h_2h_3\bigr)+h_1^3+h_2^3+h_3^3-3h_1h_2h_3.
$$

**Por qué funciona.** Un polinomio cúbico tiene todas las derivadas de cuarto orden nulas, así que el resto de Lagrange se anula para cualquier $t_0$. Aquí la fórmula de Taylor no es más que el polinomio reescrito en potencias de $h$. La parte cúbica $h_1^3+h_2^3+h_3^3-3h_1h_2h_3$ es la misma en los dos puntos: es la parte homogénea de mayor grado de la propia $f$, y una traslación no la cambia.

### Definición 2.3. Extremo local condicionado

Sean $f\colon\mathbb R^n\to\mathbb R$ y $M\subset\mathbb R^n$ no vacío. Un punto $u^{(0)}\in M$ es un punto de **mínimo local de $f$ condicionado a $M$** si existe $r_0>0$ tal que $f(u^{(0)})\le f(u)$ para todo $u\in B_{r_0}(u^{(0)})\cap M$. El **máximo local condicionado** se define igual, con $f(u^{(0)})\ge f(u)$. Aquí $B_r(u^{(0)})=\{v:\ \|v-u^{(0)}\|<r\}$ es la bola euclídea.

**Sentido.** El valor en $u^{(0)}$ se compara solo con los valores en puntos de $M$, no en todos los puntos de un entorno. Por eso un punto puede ser extremo condicionado sin ser extremo ordinario. En el [[es/seminar-sem3/hw2-conditional-extremum#Problema 2.1|problema 2.1]] el origen es un punto de silla de la función en el plano, pero un máximo sobre la recta $y=x$.

Al final del seminario quedó el ejercicio: hallar los extremos condicionados de $x^2+y^2$ sobre la recta $\frac xa+\frac yb=1$, con $a,b>0$. Pista: la ligadura es $g_1(x;y)=\frac xa+\frac yb-1=0$, y $M$ es una recta. La solución es el [[#^ex-3-2|ejemplo 3.2]].

> [!note] Al margen
> En la pizarra se mencionó el libro de E. Landau «Fundamentos del análisis» y la construcción de los enteros a partir de pares de naturales: $(k_1;m_1)\sim(k_2;m_2)\iff k_1+m_2=k_2+m_1$, donde el par $(k;m)$ representa $k-m$. No forma parte del temario del control.

## Seminario del 9 de septiembre: el teorema sobre extremos condicionados

### Teorema 3.1. Extremos condicionados y la matriz hessiana orlada

**Hipótesis.** $m<n$; $D\subset\mathbb R^n$ es una región abierta convexa; $f,g_1,\dots,g_m\in C^2(D)$; $M=\{x\in D:\ g_1(x)=\dots=g_m(x)=0\}$; el punto $u\in M$ es tal que los gradientes $\nabla g_1(u),\dots,\nabla g_m(u)$ son linealmente independientes.

**Función de Lagrange** (en el seminario, con signo «más»):
$$
\mathcal L(x;\lambda)=f(x)+\sum_{k=1}^m\lambda_kg_k(x),\qquad x\in\mathbb R^n,\ \lambda\in\mathbb R^m.
$$

**La matriz hessiana orlada** es de tamaño $(m+n)\times(m+n)$: las primeras $m$ filas y columnas corresponden a las ligaduras, las $n$ siguientes a las variables:
$$
\widetilde H(x;\lambda)=\begin{pmatrix}0_{m\times m}&J_g(x)\\ J_g(x)^{T}&H_{\mathcal L}(x;\lambda)\end{pmatrix},\qquad J_g=\Bigl(\frac{\partial g_k}{\partial x_j}\Bigr)_{m\times n},\qquad H_{\mathcal L}=\Bigl(\frac{\partial^2\mathcal L}{\partial x_i\,\partial x_j}\Bigr)_{n\times n}.
$$
Sea $\Delta_k$ su menor principal de orden $k$ (esquina superior izquierda). Solo se comprueban los últimos $n-m$ menores: $\Delta_{2m+1},\dots,\Delta_{n+m}$.

**Afirmaciones.**

1. *Condición necesaria.* Si $u$ es un punto de extremo local condicionado, existe un único $\lambda^{(0)}\in\mathbb R^m$ para el que las $n+m$ derivadas parciales de $\mathcal L$ se anulan en $(u;\lambda^{(0)})$.
2. *Mínimo.* Si $(u;\lambda)$ es un punto estacionario de $\mathcal L$ y cada menor $\Delta_k$, $k=2m+1,\dots,n+m$, tiene el signo $(-1)^m$, entonces $u$ es un punto de mínimo local condicionado.
3. *Máximo.* Si $(u;\lambda)$ es un punto estacionario de $\mathcal L$ y el menor $\Delta_k$ tiene el signo $(-1)^{k-m}$ para $k=2m+1,\dots,n+m$, entonces $u$ es un punto de máximo local condicionado. Los signos alternan empezando por $(-1)^{m+1}$; el último menor tiene el signo $(-1)^n$.
4. *No hay extremo.* Si $(u;\lambda)$ es un punto estacionario de $\mathcal L$, todos los $\Delta_k\ne0$ para $k=2m+1,\dots,n+m$, pero no se cumple ni el punto 2 ni el punto 3, entonces $u$ no es un punto de extremo condicionado.

Sobre el punto 4: si $\Delta_{2m+1}$ tiene el signo $(-1)^m$ pero un menor posterior tiene el otro signo, no es un mínimo; si $\Delta_{2m+1}$ tiene el signo $(-1)^{m+1}$ pero la alternancia se rompe después, no es un máximo.

**Chuleta de signos.**

| Tamaños | Menores | Mínimo | Máximo |
|---|---|---|---|
| $n=2$, $m=1$ | $\Delta_3=\det\widetilde H$ | $\Delta_3<0$ | $\Delta_3>0$ |
| $n=3$, $m=1$ | $\Delta_3$, $\Delta_4$ | $\Delta_3<0$, $\Delta_4<0$ | $\Delta_3>0$, $\Delta_4<0$ |
| $n=3$, $m=2$ | $\Delta_5$ | $\Delta_5>0$ | $\Delta_5<0$ |
| $n=4$, $m=2$ | $\Delta_5$, $\Delta_6$ | $\Delta_5>0$, $\Delta_6>0$ | $\Delta_5<0$, $\Delta_6>0$ |

**Por qué funciona.** La condición suficiente es el signo de la segunda diferencial $d^2\mathcal L$, pero no en todo $\mathbb R^n$, sino solo en el subespacio tangente $\{h:\ J_g(u)h=0\}$, de dimensión $n-m$. Por eso hay exactamente $n-m$ menores. De dónde sale el factor $(-1)^m$ se ve en la fórmula del complemento de Schur: si $H_{\mathcal L}$ es definida positiva, entonces
$$
\det\widetilde H=\det H_{\mathcal L}\cdot\det\bigl(-J_gH_{\mathcal L}^{-1}J_g^{T}\bigr)=(-1)^m\det H_{\mathcal L}\cdot\det\bigl(J_gH_{\mathcal L}^{-1}J_g^{T}\bigr),
$$
y los dos determinantes de la derecha son positivos. Si $\Delta_{n+m}=0$, el teorema no dice nada, y la función se estudia directamente, como en el [[es/seminar-sem3/hw2-conditional-extremum#Problema 2.3|problema 2.3]].

### Ejemplo 3.2. $x^2+y^2$ sobre la recta $\frac xa+\frac yb=1$

**Enunciado.** $a,b>0$, $f(x;y)=x^2+y^2$, $M=\bigl\{(x;y):\ \frac xa+\frac yb=1\bigr\}$. Hallar los puntos de extremo local condicionado.

^ex-3-2

**Solución.** $n=2$, $m=1$, $g_1=\frac xa+\frac yb-1$; el gradiente $\nabla g_1=\bigl(\frac1a;\frac1b\bigr)$ no se anula nunca, así que la condición de independencia se cumple.
$$
\mathcal L=x^2+y^2+\lambda\Bigl(\frac xa+\frac yb-1\Bigr),\qquad\widetilde H=\begin{pmatrix}0&\frac1a&\frac1b\\ \frac1a&2&0\\ \frac1b&0&2\end{pmatrix}.
$$
Puntos estacionarios de $\mathcal L$:
$$
2x+\frac\lambda a=0,\qquad 2y+\frac\lambda b=0,\qquad \frac xa+\frac yb=1.
$$
De las dos primeras ecuaciones, $x=-\frac{\lambda}{2a}$, $y=-\frac{\lambda}{2b}$. Al sustituir en la tercera queda $-\frac\lambda2\bigl(\frac1{a^2}+\frac1{b^2}\bigr)=1$, de donde
$$
\lambda=-\frac{2a^2b^2}{a^2+b^2},\qquad x=\frac{ab^2}{a^2+b^2},\qquad y=\frac{a^2b}{a^2+b^2}.
$$
El determinante no depende del punto:
$$
\det\widetilde H=-\frac2{a^2}-\frac2{b^2}<0.
$$
Su signo coincide con $(-1)^m=-1$, así que por el teorema 3.1 es un **mínimo local condicionado**, $f_{\min}=\frac{a^2b^2}{a^2+b^2}$.

**Por qué funciona.** $x^2+y^2$ es el cuadrado de la distancia al origen, y el problema pide el punto de la recta más cercano al origen. El valor $\frac{a^2b^2}{a^2+b^2}$ es el cuadrado de la distancia de $0$ a la recta. No hay máximo: $f$ no está acotada sobre la recta. La ecuación $\nabla\mathcal L=0$ dice que $\nabla f\parallel\nabla g_1$, es decir, en el punto más cercano el vector de posición es perpendicular a la recta.

## Seminario del 18 de septiembre: problemas 1.4 y 2.1

### Ejemplo 4.1. $x^2\sin(xy)\,e^{y+z}$ en $(-1;\pi;2)$ (= [[es/seminar-sem3/hw1-taylor#Problema 1.4|problema 1.4]])

**Enunciado.** $f(x;y;z)=x^2\sin(xy)\,e^{y+z}\in C^\infty(\mathbb R^3)$. Desarrollarla por la fórmula de Taylor hasta grado dos en $u=(-1;\pi;2)$, con el resto en forma de Lagrange.

^ex-4-1

**Derivadas.**
$$
f'_x=\bigl(2x\sin(xy)+x^2y\cos(xy)\bigr)e^{y+z},\qquad f'_y=x^2\bigl(x\cos(xy)+\sin(xy)\bigr)e^{y+z},\qquad f'_z=f,
$$
$$
f''_{xx}=\bigl(2\sin(xy)+4xy\cos(xy)-x^2y^2\sin(xy)\bigr)e^{y+z},\qquad f''_{yy}=x^2\bigl(2x\cos(xy)+(1-x^2)\sin(xy)\bigr)e^{y+z},
$$
$$
f''_{xy}=\bigl(2x\sin(xy)+3x^2\cos(xy)+x^2y\cos(xy)-x^3y\sin(xy)\bigr)e^{y+z},\qquad f''_{xz}=f'_x,\qquad f''_{yz}=f'_y,\qquad f''_{zz}=f.
$$

**Valores en el punto** (con $\sin(-\pi)=0$, $\cos(-\pi)=-1$), en unidades de $e^{\pi+2}$:

| $f$ | $f'_x$ | $f'_y$ | $f'_z$ | $f''_{xx}$ | $f''_{yy}$ | $f''_{zz}$ | $f''_{xy}$ | $f''_{xz}$ | $f''_{yz}$ |
|---|---|---|---|---|---|---|---|---|---|
| $0$ | $-\pi$ | $1$ | $0$ | $4\pi$ | $2$ | $0$ | $-(\pi+3)$ | $-\pi$ | $1$ |

**Respuesta.** Con $h=(x+1;\,y-\pi;\,z-2)$,
$$
f(x;y;z)=e^{\pi+2}\Bigl(-\pi h_1+h_2+2\pi h_1^2+h_2^2-(\pi+3)h_1h_2-\pi h_1h_3+h_2h_3\Bigr)+R_2,
$$
$$
R_2=\sum_{|\alpha|=3}D^\alpha f\bigl(-1+t_0h_1;\ \pi+t_0h_2;\ 2+t_0h_3\bigr)\,\frac{h^\alpha}{\alpha!},\qquad t_0\in(0;1).
$$

**Por qué funciona.** Los términos cuadráticos llevan el factor $\frac1{\alpha!}$. El coeficiente de $h_1^2$ es $\frac{f''_{xx}}{2!}=2\pi$, no $4\pi$. El término mixto $h_1h_2$ lleva la propia $f''_{xy}$, porque $(1;1;0)!=1$. El resto contiene derivadas de tercer orden en un punto intermedio $u+t_0h$ del segmento $[u;u+h]$ ([[#Observación 2.1. Un segmento es el conjunto de combinaciones convexas de sus extremos|observación 2.1]]). La forma explícita del resto está en el [[es/seminar-sem3/hw1-taylor#Problema 1.4|problema 1.4]].

### Ejemplo 4.2. $x^3+y^3-3xy$ sobre la recta $x=y$ (= [[es/seminar-sem3/hw2-conditional-extremum#Problema 2.1|problema 2.1]])

**Enunciado.** $f(x;y)=x^3+y^3-3xy$, $M=\{(x;y):\ x=y\}$. Hallar los puntos de extremo local condicionado.

^ex-4-2

**Solución con la hessiana orlada.** $n=2$, $m=1$, $g=x-y$, $\nabla g=(1;-1)\ne0$.
$$
\mathcal L=x^3+y^3-3xy+\lambda(x-y),\qquad \widetilde H=\begin{pmatrix}0&1&-1\\ 1&6x&-3\\ -1&-3&6y\end{pmatrix},\qquad \det\widetilde H=6(1-x-y).
$$
Puntos estacionarios: $3x^2-3y+\lambda=0$, $3y^2-3x-\lambda=0$, $x=y$. Entonces $\lambda=3x-3x^2$ y $\lambda=3x^2-3x$, es decir, $6x(x-1)=0$. Obtenemos los puntos $(0;0)$ y $(1;1)$, ambos con $\lambda=0$.

- $(0;0)$: $\det\widetilde H=6>0$, el signo $(-1)^{3-1}=+1$: **máximo local condicionado**, $f=0$.
- $(1;1)$: $\det\widetilde H=-6<0$, el signo $(-1)^m=-1$: **mínimo local condicionado**, $f=-1$.

> [!note] Consejo del seminario
> Casi siempre conviene hallar primero el determinante de $\widetilde H$ en un punto arbitrario y solo después sustituir los puntos estacionarios.

**Por qué funciona.** Sustituyendo $y=x$ se obtiene $g(x)=2x^3-3x^2$ con $g''(x)=12x-6$: $g''(0)<0$ y $g''(1)>0$, las mismas conclusiones. Así lo resuelve la tarea. La hessiana orlada hace falta cuando la ligadura no se despeja explícitamente. En relación con este método, en la pizarra se mencionaron los apuntes de Keith Conrad.

## Seminario del 20 de septiembre: un extremo condicionado en $\mathbb R^4$

### Ejemplo 5.1. $x^3+y^2+z^3+2t^2$ con $x=y$, $z=t$ (cf. [[es/seminar-sem3/hw2-conditional-extremum#Problema 2.3|problema 2.3]])

> [!note] Atención: variante del enunciado
> En el seminario se resolvió la función con $y^2$. En la tarea 2, el problema 2.3 tiene $y^3$, y allí la respuesta es otra: no hay extremos ([[es/seminar-sem3/hw2-conditional-extremum#Problema 2.3|solución]]). La variante con $y^2$ coincide con el archivo abreviado de la tarea 3.

^ex-5-1

**Enunciado.** $f(x;y;z;t)=x^3+y^2+z^3+2t^2$, $M=\{x=y,\ z=t\}$. Hallar los puntos de extremo local condicionado.

**Solución.** $n=4$, $m=2$, así que se comprueban $\Delta_5$ y $\Delta_6$. Las ligaduras son $g_1=x-y$, $g_2=z-t$; sus gradientes $(1;-1;0;0)$ y $(0;0;1;-1)$ son linealmente independientes en todas partes.
$$
\mathcal L=x^3+y^2+z^3+2t^2+\lambda_1(x-y)+\lambda_2(z-t),
$$
$$
\widetilde H=\begin{pmatrix}0&0&1&-1&0&0\\0&0&0&0&1&-1\\1&0&6x&0&0&0\\-1&0&0&2&0&0\\0&1&0&0&6z&0\\0&-1&0&0&0&4\end{pmatrix}.
$$
Puntos estacionarios:
$$
3x^2+\lambda_1=0,\quad 2y-\lambda_1=0,\quad 3z^2+\lambda_2=0,\quad 4t-\lambda_2=0,\quad x=y,\quad z=t.
$$
De aquí $3x^2+2x=0$ y $3z^2+4z=0$, es decir, $x\in\{0;-\frac23\}$, $z\in\{0;-\frac43\}$; $\lambda_1=-3x^2$, $\lambda_2=-3z^2$. Hay cuatro puntos.

Los menores se calculan desarrollando por filas y columnas con pocos elementos no nulos:
$$
\Delta_5=6x+2,\qquad\Delta_6=(6x+2)(6z+4).
$$
Para $m=2$, mínimo significa $\Delta_5>0$, $\Delta_6>0$; máximo significa $\Delta_5<0$, $\Delta_6>0$.

| Punto $(x;y;z;t)$ | $\Delta_5$ | $\Delta_6$ | Conclusión | $f$ |
|---|---|---|---|---|
| $(0;0;0;0)$ | $2$ | $8$ | mínimo | $0$ |
| $(-\frac23;-\frac23;0;0)$ | $-2$ | $-8$ | no hay extremo | $\frac4{27}$ |
| $(0;0;-\frac43;-\frac43)$ | $2$ | $-8$ | no hay extremo | $\frac{32}{27}$ |
| $(-\frac23;-\frac23;-\frac43;-\frac43)$ | $-2$ | $8$ | máximo | $\frac43$ |

**Por qué funciona.** Sobre $M$ la función se descompone en suma: $f(x;x;z;z)=\varphi(x)+\psi(z)$ con $\varphi(x)=x^3+x^2$, $\psi(z)=z^3+2z^2$. Los menores lo muestran: $\Delta_5=\varphi''(x)$ y $\Delta_6=\varphi''(x)\,\psi''(z)$. Hay mínimo cuando los dos sumandos están en un mínimo, máximo cuando los dos están en un máximo, y un mínimo de un sumando junto con un máximo del otro da un punto de silla. En la variante de la tarea 2, con $y^3$, queda $\varphi(x)=2x^3$; en los dos puntos estacionarios $\Delta_5=\Delta_6=0$, el teorema no decide, y en efecto no hay extremo.

## Qué se corrigió respecto a la transcripción OCR

| Lugar | En la transcripción | Correcto |
|---|---|---|
| [[#Teorema 3.1. Extremos condicionados y la matriz hessiana orlada\|3.1]], definición de $\widetilde H$ | filas $m+1\le k\le n$ | $m+1\le k\le n+m$ |
| [[#^ex-3-2\|3.2]] | $x=-\frac{2\lambda}{a}$, $\lambda=-\frac{a^2b^2}{2(a^2+b^2)}$ | $x=-\frac{\lambda}{2a}$, $\lambda=-\frac{2a^2b^2}{a^2+b^2}$ (el punto en sí era correcto) |
| [[#^ex-4-1\|4.1]], respuesta | $4\pi(x+1)^2+2(y-\pi)^2$ | $2\pi h_1^2+h_2^2$: faltaba el factor $\frac1{2!}$ |
| [[#^ex-4-1\|4.1]], fórmula de $f''_{xy}$ | coincidía con $f'_x$ | la fórmula de arriba; el valor $-(\pi+3)e^{\pi+2}$ era correcto |
| [[#^ex-4-2\|4.2]], enunciado | $M=\{x=y^3\}$ | $M=\{x=y\}$: la ligadura es $g=x-y$, como en el problema 2.1 |
| [[#^ex-5-1\|5.1]], enunciado | $2t^3$ | $2t^2$: así está en la función de Lagrange y en la respuesta $f=\frac43$ |

[[es/seminar-sem3/index|Todas las tareas y apuntes]] · [[es/seminar-sem3/notes-2-series-basics|Parte 2: fundamentos de series →]]
