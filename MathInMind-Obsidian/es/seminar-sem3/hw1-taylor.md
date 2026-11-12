---
title: "Seminario NM-204. Tarea 1 — fórmula de Taylor: soluciones"
lang: es
hw: 1
tags: [mathinmind/es, mathinmind/other]
---
# Tarea 1. Fórmula de Taylor en $\mathbb R^n$ — soluciones

[[ru/seminar-sem3/hw1-taylor|Русский]] · [[en/seminar-sem3/hw1-taylor|English]] · **Español**

[[es/seminar-sem3/index|Todas las tareas]] · [[es/seminar-sem3/hw2-conditional-extremum|Tarea 2 →]] · [[es/lectures-2025-26/lecture-65-66|Lecciones 65–66, §6.5]]

> [!note] Apoyo
> [[es/lectures-2025-26/lecture-65-66#^thm-6-5-2|Teorema 6.5.2 (fórmula de Taylor–Lagrange)]]: si $f$ es $s+1$ veces diferenciable, entonces
> $$
> f(a+h)=\sum_{k=0}^{s}\frac{d_a^kf(h)}{k!}+\frac{d_c^{s+1}f(h)}{(s+1)!},\qquad c=a+\theta h,\ \theta\in(0,1).
> $$
> En todo lo que sigue $a$ es el punto del desarrollo y $h=(h_1,h_2,h_3)=(x,y,z)-a$ es el incremento.

## La idea general: por qué todo se reduce a una variable

Fijemos $a$ y $h$ y consideremos la función de una variable $F(t)=f(a+th)$, $t\in[0,1]$. Por la regla de la cadena
$$
F^{(k)}(t)=d^k_{a+th}f(h)=\sum_{|\alpha|=k}\frac{k!}{\alpha!}\,\partial^\alpha f(a+th)\,h^\alpha .
$$
Por tanto, la fórmula de Taylor de $f$ en $a$ es la fórmula de Taylor unidimensional habitual de $F$ en cero, tomada en $t=1$:
$$
f(a+h)=F(1)=\sum_{k=0}^{s}\frac{F^{(k)}(0)}{k!}+\frac{F^{(s+1)}(\theta)}{(s+1)!}.
$$
De aquí salen dos conclusiones prácticas.

1. **La parte homogénea de grado $k$ del desarrollo es $d^k_af(h)/k!$** y está determinada de forma única: si $f(a+h)=\sum_{k\le s}P_k(h)+o(|h|^s)$ con $P_k$ un polinomio homogéneo de grado $k$, entonces $P_k(h)=d_a^kf(h)/k!$ (unicidad del polinomio de Taylor). Así que no es obligatorio calcular derivadas parciales: cualquier transformación legítima que dé un polinomio en $h$ con el resto correcto da exactamente el polinomio de Taylor.
2. **Para un polinomio de grado $N$ la suma se corta:** todas las derivadas de orden $N+1$ son nulas, de modo que el resto de Lagrange con $s=N$ es idénticamente cero. Desarrollar un polinomio es simplemente sustituir $x=a_1+h_1,\dots$ y abrir paréntesis; la «serie de Taylor» es finita y es igual a $f$ exactamente, para todo $h$ y no solo para los pequeños.

## Problema 1.1

**Enunciado.** $f(x,y,z)=x^3+y^3+z^3-3xyz$. Desarrollar por la fórmula de Taylor en los puntos $(1;1;1)$ y $(1;-1;2)$.

**Solución.** Derivadas parciales:
$$
f_x=3x^2-3yz,\quad f_y=3y^2-3xz,\quad f_z=3z^2-3xy;
$$
$$
f_{xx}=6x,\ f_{yy}=6y,\ f_{zz}=6z,\qquad f_{xy}=-3z,\ f_{xz}=-3y,\ f_{yz}=-3x;
$$
$$
f_{xxx}=f_{yyy}=f_{zzz}=6,\qquad f_{xyz}=-3,
$$
las demás derivadas de tercer orden son nulas y todas las de cuarto orden son nulas.

La diferencial tercera no depende del punto:
$$
\frac{d^3f(h)}{3!}=\frac{1}{6}\bigl(6h_1^3+6h_2^3+6h_3^3+6\cdot(-3)h_1h_2h_3\bigr)=h_1^3+h_2^3+h_3^3-3h_1h_2h_3 .
$$
(El coeficiente $6$ de $h_1h_2h_3$ es el número $3!/(1!\,1!\,1!)$ de ordenaciones de la derivada mixta $f_{xyz}$.)

*Punto $a=(1;1;1)$.* Aquí $f(a)=0$, $\nabla f(a)=(0,0,0)$, y las derivadas segundas son $f_{xx}=f_{yy}=f_{zz}=6$, $f_{xy}=f_{xz}=f_{yz}=-3$. Por tanto
$$
\frac{d_a^2f(h)}{2!}=\frac12\bigl(6h_1^2+6h_2^2+6h_3^2-6h_1h_2-6h_1h_3-6h_2h_3\bigr),
$$
$$
\boxed{f(1+h_1,1+h_2,1+h_3)=3\bigl(h_1^2+h_2^2+h_3^2-h_1h_2-h_1h_3-h_2h_3\bigr)+h_1^3+h_2^3+h_3^3-3h_1h_2h_3 .}
$$

*Punto $a=(1;-1;2)$.* Aquí $f(a)=1-1+8+6=14$, $\nabla f(a)=(3+6,\ 3-6,\ 12+3)=(9,-3,15)$; $f_{xx}=6$, $f_{yy}=-6$, $f_{zz}=12$, $f_{xy}=-6$, $f_{xz}=3$, $f_{yz}=-3$. Por tanto
$$
\boxed{\begin{aligned}f(1+h_1,-1+h_2,2+h_3)={}&14+9h_1-3h_2+15h_3\\&+3h_1^2-3h_2^2+6h_3^2-6h_1h_2+3h_1h_3-3h_2h_3\\&+h_1^3+h_2^3+h_3^3-3h_1h_2h_3 .\end{aligned}}
$$
En las variables originales $h_1=x-1$, $h_2=y+1$, $h_3=z-2$.

**Por qué funciona.** La parte superior (cúbica) del desarrollo coincide con la propia $f$ evaluada en los incrementos: al trasladar el argumento, la parte homogénea superior de un polinomio no cambia. En $(1;1;1)$ desaparecen el término constante y el lineal porque $f=(x+y+z)\cdot\frac12\bigl((x-y)^2+(y-z)^2+(z-x)^2\bigr)$ se anula sobre la recta $x=y=z$ junto con su gradiente; la parte cuadrática $\frac32\bigl((h_1-h_2)^2+(h_2-h_3)^2+(h_3-h_1)^2\bigr)$ es no negativa: sobre esa recta $f$ tiene un mínimo no estricto.

**Comprobación.** Con $h=(1,0,0)$ en el primer punto: $f(2,1,1)=8+1+1-6=4$, la fórmula da $3+1=4$. En el segundo punto: $f(2,-1,2)=8-1+8+12=27$, la fórmula da $14+9+3+1=27$.

## Problema 1.2

**Enunciado.** $f(x,y)=5x^4-4x^2y^2+3y^4-2xy+1$. Desarrollar por la fórmula de Taylor en el punto $(-3;2)$.

**Solución.** Pongamos $x=-3+h_1$, $y=2+h_2$ y hallemos las diferenciales en $a=(-3;2)$.

Valor: $f(a)=5\cdot81-4\cdot9\cdot4+3\cdot16-2\cdot(-6)+1=405-144+48+12+1=322$.

Derivadas primeras: $f_x=20x^3-8xy^2-2y$, $f_y=-8x^2y+12y^3-2x$;
$$
f_x(a)=-540+96-4=-448,\qquad f_y(a)=-144+96+6=-42 .
$$

Segundas: $f_{xx}=60x^2-8y^2$, $f_{xy}=-16xy-2$, $f_{yy}=-8x^2+36y^2$;
$$
f_{xx}(a)=540-32=508,\qquad f_{xy}(a)=96-2=94,\qquad f_{yy}(a)=-72+144=72 .
$$

Terceras: $f_{xxx}=120x$, $f_{xxy}=-16y$, $f_{xyy}=-16x$, $f_{yyy}=72y$;
$$
f_{xxx}(a)=-360,\quad f_{xxy}(a)=-32,\quad f_{xyy}(a)=48,\quad f_{yyy}(a)=144 .
$$

Cuartas (constantes): $f_{xxxx}=120$, $f_{xxyy}=-16$, $f_{yyyy}=72$, $f_{xxxy}=f_{xyyy}=0$.

Reunimos $d^k_af(h)/k!$ con los coeficientes binomiales:
$$
\frac{d^2}{2!}=\frac12\bigl(508h_1^2+2\cdot94h_1h_2+72h_2^2\bigr)=254h_1^2+94h_1h_2+36h_2^2,
$$
$$
\frac{d^3}{3!}=\frac16\bigl(-360h_1^3+3\cdot(-32)h_1^2h_2+3\cdot48h_1h_2^2+144h_2^3\bigr)=-60h_1^3-16h_1^2h_2+24h_1h_2^2+24h_2^3,
$$
$$
\frac{d^4}{4!}=\frac1{24}\bigl(120h_1^4+6\cdot(-16)h_1^2h_2^2+72h_2^4\bigr)=5h_1^4-4h_1^2h_2^2+3h_2^4 .
$$

**Respuesta.** Con $h_1=x+3$, $h_2=y-2$
$$
\boxed{\begin{aligned}f(x,y)={}&322-448h_1-42h_2+254h_1^2+94h_1h_2+36h_2^2\\&-60h_1^3-16h_1^2h_2+24h_1h_2^2+24h_2^3+5h_1^4-4h_1^2h_2^2+3h_2^4 .\end{aligned}}
$$

**Por qué funciona.** $f$ es un polinomio de grado cuatro, así que $d^5f\equiv0$ y el resto es cero: la igualdad es exacta. La parte superior $5h_1^4-4h_1^2h_2^2+3h_2^4$ repite la parte superior de $f$. Abrir paréntesis directamente en $f(-3+h_1,2+h_2)$ da la misma respuesta, por la unicidad del polinomio de Taylor.

**Comprobación.** $h=(1,0)$: $f(-2,2)=80-64+48+8+1=73$; la fórmula da $322-448+254-60+5=73$. $h=(0,1)$: $f(-3,3)=405-324+243+18+1=343$; la fórmula da $322-42+36+24+3=343$.

## Problema 1.3

**Enunciado.** $f(x,y,z)=e^{xy+z^2}$. Hallar la forma explícita del desarrollo de Taylor hasta grado tres con resto en forma de Lagrange en el punto $a=(-2;0;3)$.

**Solución.** Sustituimos $x=-2+h_1$, $y=h_2$, $z=3+h_3$ en el exponente:
$$
xy+z^2=(-2+h_1)h_2+(3+h_3)^2=9+\underbrace{(-2h_2+6h_3)}_{L}+\underbrace{(h_1h_2+h_3^2)}_{Q}.
$$
Aquí $L$ es una forma lineal y $Q$ una forma cuadrática en $h$; el exponente es un polinomio de grado dos, así que esta igualdad es exacta. A lo largo del segmento $a+th$:
$$
F(t)=f(a+th)=e^{u(t)},\qquad u(t)=9+Lt+Qt^2,\quad u'=L+2Qt,\quad u''=2Q,\quad u'''=0 .
$$
Derivamos la exponencial de una función (cada vez $(e^u)'=e^uu'$, y $u'''=0$):
$$
F'=e^uu',\qquad F''=e^u\bigl(u'^2+u''\bigr),\qquad F'''=e^u\bigl(u'^3+3u'u''\bigr),\qquad F^{(4)}=e^u\bigl(u'^4+6u'^2u''+3u''^2\bigr).
$$
En $t=0$: $u=9$, $u'=L$, $u''=2Q$, de modo que
$$
F(0)=e^9,\quad F'(0)=e^9L,\quad \frac{F''(0)}{2!}=e^9\Bigl(\frac{L^2}{2}+Q\Bigr),\quad \frac{F'''(0)}{3!}=e^9\Bigl(\frac{L^3}{6}+LQ\Bigr).
$$
Abriendo paréntesis:
$$
\frac{L^2}{2}+Q=2h_2^2-12h_2h_3+18h_3^2+h_1h_2+h_3^2=h_1h_2+2h_2^2-12h_2h_3+19h_3^2,
$$
$$
\frac{L^3}{6}+LQ=-2h_1h_2^2+6h_1h_2h_3-\frac43h_2^3+12h_2^2h_3-38h_2h_3^2+42h_3^3 .
$$

**Respuesta.** Con $h_1=x+2$, $h_2=y$, $h_3=z-3$ existe $\theta\in(0,1)$ (que depende de $h$) tal que
$$
\boxed{\begin{aligned}e^{xy+z^2}=e^9\Bigl[&1+(-2h_2+6h_3)+\bigl(h_1h_2+2h_2^2-12h_2h_3+19h_3^2\bigr)\\&+\Bigl(-2h_1h_2^2+6h_1h_2h_3-\frac43h_2^3+12h_2^2h_3-38h_2h_3^2+42h_3^3\Bigr)\Bigr]+R_3(h),\end{aligned}}
$$
$$
\boxed{R_3(h)=\frac{d^4_{a+\theta h}f(h)}{4!}=\frac{e^{\,9+L\theta+Q\theta^2}}{24}\Bigl[(L+2Q\theta)^4+12\,Q\,(L+2Q\theta)^2+12\,Q^2\Bigr],}
$$
donde $L=-2h_2+6h_3$, $Q=h_1h_2+h_3^2$.

**Por qué funciona.** El resto de Lagrange es $F^{(4)}(\theta)/4!$, y $F^{(4)}(\theta)$ es precisamente la diferencial cuarta de $f$ en el punto intermedio $c=a+\theta h$ sobre el vector $h$. En las coordenadas de $c=(\xi,\eta,\zeta)$ lo mismo se escribe así: $L+2Q\theta=\eta h_1+\xi h_2+2\zeta h_3=d_c u(h)$ para $u=xy+z^2$, y $9+L\theta+Q\theta^2=\xi\eta+\zeta^2$, es decir,
$$
R_3(h)=\frac{e^{\xi\eta+\zeta^2}}{24}\Bigl[(\eta h_1+\xi h_2+2\zeta h_3)^4+12(h_1h_2+h_3^2)(\eta h_1+\xi h_2+2\zeta h_3)^2+12(h_1h_2+h_3^2)^2\Bigr].
$$
Es la misma suma $\frac1{4!}\sum_{|\alpha|=4}\frac{4!}{\alpha!}\partial^\alpha f(c)h^\alpha$ de 15 sumandos, pero ya agrupada. El polinomio de Taylor también se obtiene sustituyendo $w=L+Q$ en $e^w=1+w+\frac{w^2}2+\frac{w^3}6+\dots$ y descartando los términos de grado mayor que tres; el resultado es el mismo por unicidad.

**Comprobación.** $h=(0,0,h_3)$: $f=e^{(3+h_3)^2}=e^9e^{6h_3+h_3^2}=e^9\bigl(1+6h_3+19h_3^2+42h_3^3+\dots\bigr)$, ya que $\frac{36}{2}+1=19$ y $\frac{216}{6}+6=42$.

## Problema 1.4

**Enunciado.** $f(x,y,z)=x^2\sin(xy)\,e^{y+z}$. Hallar la forma explícita del desarrollo de Taylor hasta grado dos con resto en forma de Lagrange en el punto $a=(-1;\pi;2)$.

**Solución.** Sean $E=e^{y+z}$, $S=\sin(xy)$, $C=\cos(xy)$. Como $f$ depende de $z$ solo a través del factor $e^{z}$, se tiene $\partial_zf=f$: cada derivación respecto de $z$ no cambia nada. Las demás derivadas:
$$
f_x=E\,(2xS+x^2yC),\qquad f_y=E\,(x^2S+x^3C),
$$
$$
f_{xx}=E\,\bigl((2-x^2y^2)S+4xyC\bigr),\quad f_{xy}=E\,\bigl((2x-x^3y)S+(3x^2+x^2y)C\bigr),\quad f_{yy}=E\,\bigl((x^2-x^4)S+2x^3C\bigr),
$$
$$
f_{xz}=f_x,\qquad f_{yz}=f_y,\qquad f_{zz}=f .
$$
En $a$: $xy=-\pi$, $S=0$, $C=-1$, $E=e^{\pi+2}$, $x=-1$, $y=\pi$. De aquí
$$
f(a)=0,\qquad f_x(a)=-\pi e^{\pi+2},\quad f_y(a)=e^{\pi+2},\quad f_z(a)=0,
$$
$$
f_{xx}(a)=4\pi e^{\pi+2},\quad f_{xy}(a)=-(3+\pi)e^{\pi+2},\quad f_{yy}(a)=2e^{\pi+2},\quad f_{xz}(a)=-\pi e^{\pi+2},\quad f_{yz}(a)=e^{\pi+2},\quad f_{zz}(a)=0 .
$$
Por tanto
$$
\frac{d_a^2f(h)}{2!}=e^{\pi+2}\bigl(2\pi h_1^2+h_2^2-(3+\pi)h_1h_2-\pi h_1h_3+h_2h_3\bigr).
$$

Para el resto hacen falta las derivadas de tercer orden:
$$
f_{xxx}=E\,\bigl(-6xy^2S+(6y-x^2y^3)C\bigr),
$$
$$
f_{xxy}=E\,\bigl((2-6x^2y-x^2y^2)S+(6x+4xy-x^3y^2)C\bigr),
$$
$$
f_{xyy}=E\,\bigl((2x-4x^3-2x^3y)S+(6x^2+x^2y-x^4y)C\bigr),
$$
$$
f_{yyy}=E\,\bigl((x^2-3x^4)S+(3x^3-x^5)C\bigr),
$$
$$
f_{xxz}=f_{xx},\quad f_{xyz}=f_{xy},\quad f_{yyz}=f_{yy},\quad f_{xzz}=f_x,\quad f_{yzz}=f_y,\quad f_{zzz}=f .
$$

**Respuesta.** Con $h_1=x+1$, $h_2=y-\pi$, $h_3=z-2$ existe $\theta\in(0,1)$ tal que
$$
\boxed{f(x,y,z)=e^{\pi+2}\Bigl[-\pi h_1+h_2+2\pi h_1^2+h_2^2-(3+\pi)h_1h_2-\pi h_1h_3+h_2h_3\Bigr]+R_2(h),}
$$
$$
\boxed{\begin{aligned}R_2(h)=\frac{d^3_cf(h)}{3!}=\frac16\Bigl[&f_{xxx}h_1^3+f_{yyy}h_2^3+f\,h_3^3+3f_{xxy}h_1^2h_2+3f_{xyy}h_1h_2^2\\&+3f_{xx}h_1^2h_3+3f_{yy}h_2^2h_3+3f_xh_1h_3^2+3f_yh_2h_3^2+6f_{xy}h_1h_2h_3\Bigr]_{c},\end{aligned}}
$$
donde todas las derivadas (escritas arriba) se toman en el punto $c=(-1+\theta h_1,\ \pi+\theta h_2,\ 2+\theta h_3)$.

**Por qué funciona.** Los coeficientes $1,3,6$ del resto son los multinomiales $3!/\alpha!$: hay una derivada «pura» de cada tipo, tres derivadas de la forma $\partial^2_i\partial_j$, y $f_{xyz}$ aparece $3!=6$ veces. El polinomio de grado dos se comprueba más fácilmente multiplicando desarrollos unidimensionales. Como $xy=-\pi+s$ con $s=\pi h_1-h_2+h_1h_2$, se tiene $\sin(xy)=-\sin s=-s+O(|h|^3)$, y
$$
x^2=1-2h_1+h_1^2,\qquad e^{y+z}=e^{\pi+2}\bigl(1+h_2+h_3+\dots\bigr).
$$
El factor $\sin(xy)$ se anula en $a$, por lo que de los otros factores solo se necesitan los términos hasta primer orden:
$$
f=-e^{\pi+2}\bigl[(\pi h_1-h_2+h_1h_2)+(\pi h_1-h_2)(-2h_1+h_2+h_3)\bigr]+o(|h|^2),
$$
lo que, tras abrir paréntesis, coincide con la respuesta. No es casualidad: el polinomio de Taylor de un producto es el producto de los polinomios de Taylor truncado por grado (unicidad).

**Comprobación.** $h=(0,h_2,0)$: $f=\sin(-\pi-h_2)\,e^{\pi+2+h_2}=\sin h_2\cdot e^{\pi+2}e^{h_2}=e^{\pi+2}(h_2+h_2^2+\dots)$: coincide.
