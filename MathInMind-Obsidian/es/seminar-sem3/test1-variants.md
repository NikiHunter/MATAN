---
title: "Seminario NM-204. Control del 20 nov. — variantes de práctica"
lang: es
tags: [mathinmind/es, mathinmind/other]
---
# Control del 20 de noviembre de 2026: variantes de práctica con soluciones

[[ru/seminar-sem3/test1-variants|Русский]] · [[en/seminar-sem3/test1-variants|English]] · **Español**

[[es/seminar-sem3/index|Todas las tareas]] · [[es/seminar-sem3/test1-guide|← Cómo prepararse]]

> [!note] Qué es esto
> Tres variantes de práctica con el formato anunciado en la consulta: problema 1a — un polinomio (grado 3 en tres variables o grado 4 en dos), 1b — una función no polinómica de tres variables hasta orden dos con el resto de Lagrange en forma general, 2 — un extremo condicionado de una función de tres variables con una condición polinómica. Los problemas siguen el modelo de los ejemplos de la consulta; no existen variantes reales. Como prometió el profesor, cada problema 2 tiene un máximo, un mínimo y un punto sin extremo, todos los menores que se comprueban son no nulos y las ecuaciones para $\lambda$ son de grado dos como mucho. Resuélvelas por escrito, sin calculadora, y solo después abre las soluciones; todos los cálculos se comprobaron en sympy. Los problemas de series de la versión anterior de esta página pasaron al [[es/seminar-sem3/series-test-guide#Problemas de práctica|control de series]].

Notación de las soluciones: $D^{\alpha}f$ es la derivada parcial de multiíndice $\alpha$, $\widetilde H$ es la hessiana orlada con la orla en la primera fila y columna, $\Delta_3$ y $\Delta_4$ son sus menores principales. Mínimo: $\Delta_3<0$, $\Delta_4<0$; máximo: $\Delta_3>0$, $\Delta_4<0$; en otro caso no hay extremo ([[es/seminar-sem3/test1-guide#Problema 2: extremo condicionado|tabla]]).

## Variante A

**1a.** Desarrollar por la fórmula de Taylor en el punto $P=(1;-1;2)$ la función $f(x;y;z)=x^3-2xyz+y^2z+3z-1$.

**1b.** Hallar el desarrollo de Taylor de $f(x;y;z)=x\,e^{y+2z}+\sin(xy)$ hasta grado dos en el punto $P=(1;0;0)$ con resto en forma de Lagrange.

**2.** Hallar todos los puntos de extremo local condicionado de $f(x;y;z)=x^2+2y+6z$ sobre el conjunto $M=\{(x;y;z)\in\mathbb R^3:\ x^2+y^2+9z^2=18\}$.

> [!example]- Soluciones de la variante A
> **1a.** Derivadas en un punto arbitrario:
> $$
> D^{(1;0;0)}f=3x^2-2yz,\qquad D^{(0;1;0)}f=-2xz+2yz,\qquad D^{(0;0;1)}f=-2xy+y^2+3;
> $$
> $$
> D^{(2;0;0)}f=6x,\quad D^{(1;1;0)}f=-2z,\quad D^{(1;0;1)}f=-2y,\quad D^{(0;2;0)}f=2z,\quad D^{(0;1;1)}f=-2x+2y,\quad D^{(0;0;2)}f=0;
> $$
> $$
> D^{(3;0;0)}f=6,\qquad D^{(1;1;1)}f=-2,\qquad D^{(0;2;1)}f=2,
> $$
> las demás derivadas de tercer orden y todas las de cuarto son cero, así que la suma es finita y no hay resto.
>
> En $P$: $f(P)=1-2\cdot1\cdot(-1)\cdot2+(-1)^2\cdot2+3\cdot2-1=12$; $D^{(1;0;0)}f(P)=3+4=7$, $D^{(0;1;0)}f(P)=-4-4=-8$, $D^{(0;0;1)}f(P)=2+1+3=6$; $D^{(2;0;0)}f(P)=6$, $D^{(1;1;0)}f(P)=-4$, $D^{(1;0;1)}f(P)=2$, $D^{(0;2;0)}f(P)=4$, $D^{(0;1;1)}f(P)=-4$. Se divide entre $\alpha!$: $\frac62=3$, $\frac42=2$, $\frac{6}{3!}=1$, $\frac{2}{(0;2;1)!}=1$.
>
> **Respuesta.** Para todo $(x;y;z)\in\mathbb R^3$
> $$
> \begin{aligned}f={}&12+7(x-1)-8(y+1)+6(z-2)+3(x-1)^2-4(x-1)(y+1)+2(x-1)(z-2)+2(y+1)^2-4(y+1)(z-2)\\&+(x-1)^3-2(x-1)(y+1)(z-2)+(y+1)^2(z-2).\end{aligned}
> $$
> Comprobación: la parte de mayor grado repite $x^3-2xyz+y^2z$; en el punto $(2;-1;2)$ el lado izquierdo es $8+8+2+6-1=23$ y el derecho $12+7+3+1=23$.
>
> **1b.** Derivadas:
> $$
> D^{(1;0;0)}f=e^{y+2z}+y\cos(xy),\qquad D^{(0;1;0)}f=x\,e^{y+2z}+x\cos(xy),\qquad D^{(0;0;1)}f=2x\,e^{y+2z};
> $$
> $$
> D^{(2;0;0)}f=-y^2\sin(xy),\qquad D^{(1;1;0)}f=e^{y+2z}+\cos(xy)-xy\sin(xy),\qquad D^{(1;0;1)}f=2e^{y+2z},
> $$
> $$
> D^{(0;2;0)}f=x\,e^{y+2z}-x^2\sin(xy),\qquad D^{(0;1;1)}f=2x\,e^{y+2z},\qquad D^{(0;0;2)}f=4x\,e^{y+2z}.
> $$
> En $P$ ($e^0=1$, $\sin0=0$, $\cos0=1$): $f=1$; primer orden: $1$, $2$, $2$; segundo orden: $0$, $2$, $2$, $1$, $2$, $4$.
>
> **Respuesta.** $f\in C^\infty(\mathbb R^3)$, así que para todo $(x;y;z)$ existe $t_0\in(0;1)$:
> $$
> \begin{aligned}x\,e^{y+2z}+\sin(xy)={}&1+(x-1)+2y+2z+2(x-1)y+2(x-1)z+\tfrac12y^2+2yz+2z^2\\&+\sum_{|\alpha|=3}\frac{D^{\alpha}f\bigl(1+t_0(x-1);\ t_0y;\ t_0z\bigr)}{\alpha!}\,(x-1)^{\alpha_1}y^{\alpha_2}z^{\alpha_3}.\end{aligned}
> $$
> Comprobación: con $y=z=0$ la función vale $x=1+(x-1)$; no hay término cuadrático en $x-1$, igual que $D^{(2;0;0)}f(P)=0$.
>
> **2.** $\mathcal L=x^2+2y+6z-\lambda(x^2+y^2+9z^2-18)$. El sistema:
> $$
> 2x-2\lambda x=0,\qquad 2-2\lambda y=0,\qquad 6-18\lambda z=0,\qquad x^2+y^2+9z^2=18 .
> $$
> De la segunda, $\lambda\ne0$ e $y=\frac1\lambda$; de la tercera, $z=\frac1{3\lambda}$; la primera: $2x(1-\lambda)=0$.
>
> - $x=0$: $\frac1{\lambda^2}+\frac1{\lambda^2}=18$, $\lambda=\pm\frac13$. Los puntos $(0;3;1)$ con $\lambda=\frac13$ y $(0;-3;-1)$ con $\lambda=-\frac13$.
> - $\lambda=1$: $y=1$, $z=\frac13$, $x^2=18-1-1=16$. Los puntos $(\pm4;1;\frac13)$.
>
> $\varphi_x=2x$, $\varphi_y=2y$, $\varphi_z=18z$; $\mathcal L_{xx}=2-2\lambda$, $\mathcal L_{yy}=-2\lambda$, $\mathcal L_{zz}=-18\lambda$, sin derivadas mixtas. Por las fórmulas rápidas
> $$
> \Delta_3=8\lambda x^2-8(1-\lambda)y^2,\qquad \Delta_4=-144\lambda^2x^2+144\lambda(1-\lambda)y^2+1296\lambda(1-\lambda)z^2 .
> $$
>
> | Punto | $\lambda$ | $\Delta_3$ | $\Delta_4$ | Conclusión | $f$ |
> |---|---|---|---|---|---|
> | $(0;3;1)$ | $\frac13$ | $-48$ | $576$ | sin extremo | $12$ |
> | $(0;-3;-1)$ | $-\frac13$ | $-96$ | $-1152$ | mínimo | $-12$ |
> | $(4;1;\frac13)$, $(-4;1;\frac13)$ | $1$ | $128$ | $-2304$ | máximo | $20$ |
>
> **Respuesta.** $(\pm4;1;\frac13)$ son puntos de máximo local condicionado, $f=20$; $(0;-3;-1)$ es un punto de mínimo local condicionado, $f=-12$; en $(0;3;1)$ no hay extremo.
>
> **Por qué funciona.** $M$ es un elipsoide, un compacto, así que $f$ alcanza en él sus valores máximo y mínimo: son $20$ y $-12$. Pero la compacidad no dice nada del punto $(0;3;1)$: allí $d^2\mathcal L=\frac43dx^2-\frac23(dy^2+9dz^2)$ es indefinida sobre el plano tangente.

## Variante B

**1a.** Desarrollar por la fórmula de Taylor en el punto $P=(-1;2)$ la función $f(x;y)=x^4-2x^2y+3xy^2-y^3+5$.

**1b.** Hallar el desarrollo de Taylor de $f(x;y;z)=\ln(x^2+yz)$ hasta grado dos en el punto $P=(1;0;2)$ con resto en forma de Lagrange.

**2.** Hallar todos los puntos de extremo local condicionado de $f(x;y;z)=x^2+8y+4z$ sobre el conjunto $M=\{(x;y;z)\in\mathbb R^3:\ y^2-x^2-z^2=3\}$.

> [!example]- Soluciones de la variante B
> **1a.** Derivadas:
> $$
> D^{(1;0)}f=4x^3-4xy+3y^2,\qquad D^{(0;1)}f=-2x^2+6xy-3y^2;
> $$
> $$
> D^{(2;0)}f=12x^2-4y,\qquad D^{(1;1)}f=-4x+6y,\qquad D^{(0;2)}f=6x-6y;
> $$
> $$
> D^{(3;0)}f=24x,\quad D^{(2;1)}f=-4,\quad D^{(1;2)}f=6,\quad D^{(0;3)}f=-6,\quad D^{(4;0)}f=24,
> $$
> las demás derivadas de cuarto orden y todas las de quinto son cero.
>
> En $P$: $f(P)=1-4-12-8+5=-18$; $D^{(1;0)}f(P)=-4+8+12=16$, $D^{(0;1)}f(P)=-2-12-12=-26$; $D^{(2;0)}f(P)=4$, $D^{(1;1)}f(P)=16$, $D^{(0;2)}f(P)=-18$; $D^{(3;0)}f(P)=-24$, $D^{(2;1)}f(P)=-4$, $D^{(1;2)}f(P)=6$, $D^{(0;3)}f(P)=-6$; $D^{(4;0)}f(P)=24$. Coeficientes: $2$, $16$, $-9$; $-4$, $-2$, $3$, $-1$; $1$.
>
> **Respuesta.** Para todo $(x;y)\in\mathbb R^2$
> $$
> \begin{aligned}f={}&-18+16(x+1)-26(y-2)+2(x+1)^2+16(x+1)(y-2)-9(y-2)^2\\&-4(x+1)^3-2(x+1)^2(y-2)+3(x+1)(y-2)^2-(y-2)^3+(x+1)^4 .\end{aligned}
> $$
> Comprobación: en el punto $(0;2)$ el lado izquierdo es $-8+5=-3$ y el derecho $-18+16+2-4+1=-3$.
>
> **1b.** Sea $u=x^2+yz$; $f$ está definida y es infinitamente diferenciable en el abierto $\{u>0\}$, y $u(P)=1$.
> $$
> D^{(1;0;0)}f=\frac{2x}u,\qquad D^{(0;1;0)}f=\frac zu,\qquad D^{(0;0;1)}f=\frac yu;
> $$
> $$
> D^{(2;0;0)}f=\frac{2(yz-x^2)}{u^2},\quad D^{(1;1;0)}f=-\frac{2xz}{u^2},\quad D^{(1;0;1)}f=-\frac{2xy}{u^2},\quad D^{(0;2;0)}f=-\frac{z^2}{u^2},\quad D^{(0;1;1)}f=\frac{x^2}{u^2},\quad D^{(0;0;2)}f=-\frac{y^2}{u^2}.
> $$
> En $P$: $f=0$; primer orden: $2$, $2$, $0$; segundo orden: $-2$, $-4$, $0$, $-4$, $1$, $0$.
>
> **Respuesta.** Para los $(x;y;z)$ cuyo segmento desde $P$ está en la región $x^2+yz>0$ (por ejemplo, para todos los puntos de una bola centrada en $P$ dentro de esa región), existe $t_0\in(0;1)$:
> $$
> \ln(x^2+yz)=2(x-1)+2y-(x-1)^2-4(x-1)y-2y^2+y(z-2)+\sum_{|\alpha|=3}\frac{D^{\alpha}f\bigl(1+t_0(x-1);\ t_0y;\ 2+t_0(z-2)\bigr)}{\alpha!}\,(x-1)^{\alpha_1}y^{\alpha_2}(z-2)^{\alpha_3}.
> $$
> Comprobación: con $y=0$ queda $\ln x^2=2\ln\bigl(1+(x-1)\bigr)=2(x-1)-(x-1)^2+\dots$; con $x=1$, $z=2$ — $\ln(1+2y)=2y-2y^2+\dots$
>
> **2.** $\mathcal L=x^2+8y+4z-\lambda(y^2-x^2-z^2-3)$. El sistema:
> $$
> 2x+2\lambda x=0,\qquad 8-2\lambda y=0,\qquad 4+2\lambda z=0,\qquad y^2-x^2-z^2=3 .
> $$
> De la segunda, $\lambda\ne0$ e $y=\frac4\lambda$; de la tercera, $z=-\frac2\lambda$; la primera: $2x(1+\lambda)=0$.
>
> - $x=0$: $\frac{16}{\lambda^2}-\frac4{\lambda^2}=3$, $\lambda^2=4$. Los puntos $(0;2;-1)$ con $\lambda=2$ y $(0;-2;1)$ con $\lambda=-2$.
> - $\lambda=-1$: $y=-4$, $z=2$, $x^2=16-4-3=9$. Los puntos $(\pm3;-4;2)$.
>
> $\varphi_x=-2x$, $\varphi_y=2y$, $\varphi_z=-2z$; $\mathcal L_{xx}=2+2\lambda$, $\mathcal L_{yy}=-2\lambda$, $\mathcal L_{zz}=2\lambda$.
> $$
> \Delta_3=8\lambda x^2-8(1+\lambda)y^2,\qquad \Delta_4=16\lambda^2x^2-16\lambda(1+\lambda)y^2+16\lambda(1+\lambda)z^2 .
> $$
>
> | Punto | $\lambda$ | $\Delta_3$ | $\Delta_4$ | Conclusión | $f$ |
> |---|---|---|---|---|---|
> | $(0;2;-1)$ | $2$ | $-96$ | $-288$ | mínimo | $12$ |
> | $(0;-2;1)$ | $-2$ | $32$ | $-96$ | máximo | $-12$ |
> | $(3;-4;2)$, $(-3;-4;2)$ | $-1$ | $-72$ | $144$ | sin extremo | $-15$ |
>
> **Respuesta.** $(0;2;-1)$ es un punto de mínimo local condicionado, $f=12$; $(0;-2;1)$ es un punto de máximo local condicionado, $f=-12$; en los puntos $(\pm3;-4;2)$ no hay extremo.
>
> **Por qué funciona.** $M$ es un hiperboloide de dos hojas ($y^2=3+x^2+z^2$, así que $\lvert y\rvert\ge\sqrt3$); no está acotado y el argumento de compacidad no está disponible: solo sirven los menores. El mínimo ($12$) es mayor que el máximo ($-12$), y no hay contradicción: los extremos son locales y los puntos están en hojas distintas del hiperboloide ($y>0$ e $y<0$).

## Variante C

**1a.** Desarrollar por la fórmula de Taylor en el punto $P=(2;1;-1)$ la función $f(x;y;z)=x^2z+xyz-y^3+2x$.

**1b.** Hallar el desarrollo de Taylor de $f(x;y;z)=e^z\sin(x+2y)$ hasta grado dos en el punto $P=\bigl(\frac\pi4;0;0\bigr)$ con resto en forma de Lagrange.

**2.** Hallar todos los puntos de extremo local condicionado de $f(x;y;z)=6x+6y-3z^2$ sobre el conjunto $M=\{(x;y;z)\in\mathbb R^3:\ x^2+y^2+z^2=18\}$.

> [!example]- Soluciones de la variante C
> **1a.** Derivadas:
> $$
> D^{(1;0;0)}f=2xz+yz+2,\qquad D^{(0;1;0)}f=xz-3y^2,\qquad D^{(0;0;1)}f=x^2+xy;
> $$
> $$
> D^{(2;0;0)}f=2z,\quad D^{(1;1;0)}f=z,\quad D^{(1;0;1)}f=2x+y,\quad D^{(0;2;0)}f=-6y,\quad D^{(0;1;1)}f=x,\quad D^{(0;0;2)}f=0;
> $$
> $$
> D^{(2;0;1)}f=2,\qquad D^{(1;1;1)}f=1,\qquad D^{(0;3;0)}f=-6,
> $$
> las demás derivadas de tercer orden y todas las de cuarto son cero.
>
> En $P$: $f(P)=-4-2-1+4=-3$; primer orden: $-4-1+2=-3$, $-2-3=-5$, $4+2=6$; segundo orden: $-2$, $-1$, $5$, $-6$, $2$, $0$. Coeficientes de segundo orden: $-1$, $-1$, $5$, $-3$, $2$; de tercero: $\frac2{(2;0;1)!}=1$, $1$, $\frac{-6}{3!}=-1$.
>
> **Respuesta.** Para todo $(x;y;z)\in\mathbb R^3$
> $$
> \begin{aligned}f={}&-3-3(x-2)-5(y-1)+6(z+1)-(x-2)^2-(x-2)(y-1)+5(x-2)(z+1)-3(y-1)^2+2(y-1)(z+1)\\&+(x-2)^2(z+1)+(x-2)(y-1)(z+1)-(y-1)^3 .\end{aligned}
> $$
> Comprobación: en el punto $(2;1;0)$ el lado izquierdo es $0+0-1+4=3$ y el derecho $-3+6=3$.
>
> **1b.** $f\in C^\infty(\mathbb R^3)$. Derivadas: de primer orden — $e^z\cos(x+2y)$, $2e^z\cos(x+2y)$, $e^z\sin(x+2y)$; de segundo orden —
> $$
> D^{(2;0;0)}f=-e^z\sin(x+2y),\quad D^{(1;1;0)}f=-2e^z\sin(x+2y),\quad D^{(1;0;1)}f=e^z\cos(x+2y),
> $$
> $$
> D^{(0;2;0)}f=-4e^z\sin(x+2y),\quad D^{(0;1;1)}f=2e^z\cos(x+2y),\quad D^{(0;0;2)}f=e^z\sin(x+2y).
> $$
> En $P$: $\sin\frac\pi4=\cos\frac\pi4=\frac1{\sqrt2}$, $e^0=1$. Valores: $f=\frac1{\sqrt2}$; primer orden $\frac1{\sqrt2}$, $\frac2{\sqrt2}$, $\frac1{\sqrt2}$; segundo orden $-\frac1{\sqrt2}$, $-\frac2{\sqrt2}$, $\frac1{\sqrt2}$, $-\frac4{\sqrt2}$, $\frac2{\sqrt2}$, $\frac1{\sqrt2}$.
>
> **Respuesta.** Para todo $(x;y;z)$ existe $t_0\in(0;1)$:
> $$
> \begin{aligned}e^z\sin(x+2y)={}&\frac1{\sqrt2}\Bigl[1+\bigl(x-\tfrac\pi4\bigr)+2y+z-\tfrac12\bigl(x-\tfrac\pi4\bigr)^2-2\bigl(x-\tfrac\pi4\bigr)y+\bigl(x-\tfrac\pi4\bigr)z-2y^2+2yz+\tfrac12z^2\Bigr]\\&+\sum_{|\alpha|=3}\frac{D^{\alpha}f\bigl(\frac\pi4+t_0(x-\frac\pi4);\ t_0y;\ t_0z\bigr)}{\alpha!}\,\bigl(x-\tfrac\pi4\bigr)^{\alpha_1}y^{\alpha_2}z^{\alpha_3}.\end{aligned}
> $$
> Comprobación: $\sin\bigl(\frac\pi4+w\bigr)=\frac1{\sqrt2}\bigl(1+w-\frac{w^2}2+\dots\bigr)$ con $w=(x-\frac\pi4)+2y$, y $e^z=1+z+\frac{z^2}2+\dots$; su producto hasta grado dos da el mismo corchete.
>
> **2.** $\mathcal L=6x+6y-3z^2-\lambda(x^2+y^2+z^2-18)$. El sistema:
> $$
> 6-2\lambda x=0,\qquad 6-2\lambda y=0,\qquad -6z-2\lambda z=0,\qquad x^2+y^2+z^2=18 .
> $$
> De las dos primeras, $\lambda\ne0$ y $x=y=\frac3\lambda$; la tercera: $-2z(3+\lambda)=0$.
>
> - $z=0$: $\frac9{\lambda^2}+\frac9{\lambda^2}=18$, $\lambda=\pm1$. Los puntos $(3;3;0)$ con $\lambda=1$ y $(-3;-3;0)$ con $\lambda=-1$.
> - $\lambda=-3$: $x=y=-1$, $z^2=18-2=16$. Los puntos $(-1;-1;\pm4)$.
>
> $\varphi_x=2x$, $\varphi_y=2y$, $\varphi_z=2z$; $\mathcal L_{xx}=\mathcal L_{yy}=-2\lambda$, $\mathcal L_{zz}=-6-2\lambda$.
> $$
> \Delta_3=8\lambda(x^2+y^2),\qquad \Delta_4=-16\lambda(\lambda+3)(x^2+y^2)-16\lambda^2z^2 .
> $$
>
> | Punto | $\lambda$ | $\Delta_3$ | $\Delta_4$ | Conclusión | $f$ |
> |---|---|---|---|---|---|
> | $(3;3;0)$ | $1$ | $144$ | $-1152$ | máximo | $36$ |
> | $(-3;-3;0)$ | $-1$ | $-144$ | $576$ | sin extremo | $-36$ |
> | $(-1;-1;4)$, $(-1;-1;-4)$ | $-3$ | $-48$ | $-2304$ | mínimo | $-60$ |
>
> **Respuesta.** $(3;3;0)$ es un punto de máximo local condicionado, $f=36$; $(-1;-1;\pm4)$ son puntos de mínimo local condicionado, $f=-60$; en $(-3;-3;0)$ no hay extremo.
>
> **Por qué funciona.** Aquí se factoriza la ecuación en $z$, no la de $x$: hay que mirar dónde conviene. En $(-3;-3;0)$ la función $6(x+y)$ es mínima a lo largo de la circunferencia $z=0$, mientras que al moverse en $z$ el término $-3z^2$ la hace disminuir; de ahí el punto de silla.

## Qué comprueba cada variante

| Problema | Variante A | Variante B | Variante C |
|---|---|---|---|
| 1a | grado 3 en tres variables, la mixta $D^{(1;1;1)}f$ | grado 4 en dos variables | grado 3 en tres variables, $D^{(2;0;1)}f$ y $D^{(1;1;1)}f$ |
| 1b | una exponencial y el seno de un producto | un logaritmo: el dominio y el segmento $[P;X]$ | el punto $\frac\pi4$, valores $\pm\frac1{\sqrt2}$ |
| 2 | un elipsoide; los casos $x=0$ y $\lambda=1$; dos máximos | un hiperboloide de dos hojas, no compacto; el mínimo es mayor que el máximo | una esfera; el factor en $z$; dos mínimos |
