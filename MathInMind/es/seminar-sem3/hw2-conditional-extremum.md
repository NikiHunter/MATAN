---
title: "Seminario NM-204. Tarea 2 — extremos condicionados: soluciones"
lang: es
hw: 2
---
# Tarea 2. Extremos condicionados — soluciones

[Русский](../../ru/seminar-sem3/hw2-conditional-extremum.md) · [English](../../en/seminar-sem3/hw2-conditional-extremum.md) · **Español**

[← Tarea 1](hw1-taylor.md) · [Todas las tareas](index.md) · [Tarea 3 →](hw3-numerical-series.md) · [Lecciones 67–68, §6.7](../lectures-2025-26/lecture-67-68.md)

Aquí se resuelven los problemas 2.1–2.3 (tarea 2) y 2'.1–2'.3 (la serie sobre extremos condicionados de la tarea 3). Los problemas 1.2 y 1.4, repetidos en la tarea 2, están resueltos en la [tarea 1](hw1-taylor.md).

> **Apoyo.** [Teorema 6.7.4](../lectures-2025-26/lecture-67-68.md#thm-6-7-4) (condición necesaria): si $`a`$ es un punto de extremo condicionado de $`f`$ bajo las ligaduras $`\varphi_1=\dots=\varphi_m=0`$ y los gradientes de las ligaduras en $`a`$ son linealmente independientes, entonces $`\nabla f(a)=\sum_j\lambda_j\nabla\varphi_j(a)`$. [Teorema 6.7.5](../lectures-2025-26/lecture-67-68.md#thm-6-7-5) (condición suficiente): el signo de $`d^2L`$ de la función de Lagrange $`L=f-\sum\lambda_j\varphi_j`$ sobre el espacio tangente $`\{h:\ d\varphi_j(h)=0\}`$.

## Por qué funciona el método de Lagrange

Sobre el conjunto $`M=\{\varphi=0\}`$ no se permiten todos los desplazamientos, solo los tangentes a $`M`$: los $`h`$ con $`d\varphi_j(h)=0`$. En un punto de extremo $`f`$ no debe cambiar en primer orden a lo largo de las direcciones permitidas, es decir, $`df(h)=0`$ para todo $`h`$ tangente. Esto significa justamente que $`\nabla f`$ es ortogonal al espacio tangente, o sea, que pertenece a la envoltura lineal de las normales $`\nabla\varphi_j`$. La independencia de los gradientes hace falta para que el espacio tangente describa de verdad a $`M`$ cerca del punto ([teorema de la aplicación implícita](../lectures-2025-26/lecture-65-66.md#thm-6-6-1)).

Tres consecuencias que usamos más abajo.

- Si la ligadura se despeja explícitamente (por ejemplo, $`y=x`$), el problema se convierte en un problema ordinario de extremos con menos variables. Es el mismo método: una parametrización de $`M`$ en lugar de multiplicadores.
- La condición de Lagrange es **necesaria**. Un punto estacionario todavía hay que estudiarlo: con la diferencial segunda, con una estimación directa o por compacidad (una función continua sobre un compacto alcanza sus valores máximo y mínimo, y esos puntos tienen que estar entre los estacionarios).
- Si $`d^2L`$ es degenerada sobre el espacio tangente, la condición suficiente calla y hay que mirar la propia función (problemas 2.3 y 2'.3).

## Problema 2.1

**Enunciado.** $`f(x,y)=x^3+y^3-3xy`$, $`M=\{x=y\}`$. Hallar todos los puntos de extremo local condicionado.

**Solución.** La recta $`M`$ se parametriza como $`(x,x)`$, $`x\in\mathbb R`$, y esto es un homeomorfismo $`\mathbb R\to M`$. Por tanto los puntos de extremo condicionado de $`f`$ sobre $`M`$ son exactamente los puntos de extremo local de
```math
g(x)=f(x,x)=2x^3-3x^2 .
```
$`g'(x)=6x^2-6x=6x(x-1)`$, ceros: $`x=0`$ y $`x=1`$. $`g''(x)=12x-6`$: $`g''(0)=-6<0`$, máximo local estricto; $`g''(1)=6>0`$, mínimo local estricto.

*Lo mismo por el método de Lagrange.* $`\varphi=x-y`$, $`\nabla\varphi=(1,-1)\ne0`$. Sistema: $`3x^2-3y=\lambda`$, $`3y^2-3x=-\lambda`$, $`x=y`$. De las dos primeras con $`x=y`$: $`3x^2-3x=\lambda=-(3x^2-3x)`$, luego $`\lambda=0`$ y $`x\in\{0,1\}`$. La diferencial segunda $`d^2L=6x\,dx^2-6\,dx\,dy+6y\,dy^2`$ sobre los vectores tangentes $`dx=dy`$ vale $`(12x-6)\,dx^2`$: el mismo signo que $`g''`$.

**Respuesta.** $`(0;0)`$ es un punto de máximo local condicionado estricto, $`f=0`$; $`(1;1)`$ es un punto de mínimo local condicionado estricto, $`f=-1`$. No hay otros.

**Por qué funciona.** Ambos extremos son locales, no globales: $`g(x)\to\pm\infty`$ cuando $`x\to\pm\infty`$. Conviene comparar con el problema sin ligaduras: $`(1;1)`$ es un mínimo libre de $`f`$, así que sigue siendo mínimo sobre cualquier curva que pase por él. En cambio $`(0;0)`$ es un punto de silla de $`f`$ en el plano (la hessiana $`\begin{pmatrix}0&-3\\-3&0\end{pmatrix}`$ es indefinida), pero a lo largo de la recta $`x=y`$ la forma $`-6\,dx\,dy`$ vale $`-6\,dx^2<0`$: la restricción a $`M`$ «elige» la dirección en la que la silla parece un máximo. Un extremo condicionado puede aparecer donde no hay extremo libre.

## Problema 2.2

**Enunciado.** $`a>0`$, $`f(x,y,z)=e^{x+2y+3z}`$, $`M=\{x^2+2y^2+3z^2=a\}`$. Hallar todos los puntos de extremo local condicionado.

**Solución.** La ligadura es $`\varphi=x^2+2y^2+3z^2-a`$, y $`\nabla\varphi=(2x,4y,6z)`$ se anula solo en el origen, que no pertenece a $`M`$ (pues $`a>0`$). Así que la condición de regularidad se cumple en todo $`M`$, y todo punto de extremo condicionado satisface el sistema de Lagrange. Sea $`u=x+2y+3z`$; $`\nabla f=e^u(1,2,3)`$:
```math
e^u=2\lambda x,\qquad 2e^u=4\lambda y,\qquad 3e^u=6\lambda z .
```
Como $`e^u\ne0`$, resulta $`\lambda\ne0`$ y $`x=y=z=\dfrac{e^u}{2\lambda}`$. Sustituyendo $`x=y=z=t`$ en la ligadura: $`6t^2=a`$, $`t=\pm\sqrt{a/6}`$. Hay dos puntos estacionarios:
```math
P_\pm=\pm\sqrt{\frac a6}\,(1;1;1),\qquad u(P_\pm)=\pm6\sqrt{\frac a6}=\pm\sqrt{6a} .
```
$`M`$ es un elipsoide; es cerrado y acotado, es decir, compacto; $`f`$ es continua, luego alcanza sobre $`M`$ sus valores máximo y mínimo. Los puntos donde se alcanzan son puntos de extremo condicionado, así que están entre $`P_\pm`$. Como $`f(P_+)>f(P_-)`$, el máximo está en $`P_+`$ y el mínimo en $`P_-`$. No hay otros puntos de extremo local condicionado: todo punto así es estacionario, y solo hay dos puntos estacionarios.

**Respuesta.** $`P_+=\bigl(\sqrt{a/6};\sqrt{a/6};\sqrt{a/6}\bigr)`$ es el punto de máximo condicionado, $`f=e^{\sqrt{6a}}`$; $`P_-=-P_+`$ es el punto de mínimo condicionado, $`f=e^{-\sqrt{6a}}`$. Ambos extremos son estrictos y globales sobre $`M`$.

**Por qué funciona.** La exponencial es estrictamente creciente, así que los extremos de $`f`$ son los de la función lineal $`u=x+2y+3z`$ sobre el elipsoide. Geométricamente: los planos $`u=\mathrm{const}`$ son paralelos y el extremo se alcanza donde un plano toca al elipsoide, es decir, donde la normal $`(2x,4y,6z)`$ al elipsoide es paralela a $`(1,2,3)`$; eso da $`x=y=z`$. Una comprobación independiente es la desigualdad de Cauchy–Schwarz:
```math
(x+2y+3z)^2=\bigl(1\cdot x+\sqrt2\cdot\sqrt2y+\sqrt3\cdot\sqrt3z\bigr)^2\le(1+2+3)(x^2+2y^2+3z^2)=6a,
```
con igualdad solo cuando $`x=y=z`$. De aquí se ve también que los extremos son estrictos.

## Problema 2.3

**Enunciado.** $`f(x,y,z,t)=x^3+y^3+z^3+2t^2`$, $`M=\{x=y,\ z=t\}`$. Hallar todos los puntos de extremo local condicionado.

**Solución.** $`M`$ es un plano bidimensional; lo parametrizamos como $`(x,x,z,z)`$, $`(x,z)\in\mathbb R^2`$. El problema equivale a buscar los extremos locales de
```math
g(x,z)=f(x,x,z,z)=2x^3+z^3+2z^2 .
```
Condición necesaria: $`g_x=6x^2=0`$, $`g_z=3z^2+4z=0`$, de donde $`x=0`$ y $`z\in\{0,-\tfrac43\}`$. Puntos estacionarios: $`(0,0)`$ y $`(0,-\tfrac43)`$.

La hessiana de $`g`$ es $`\operatorname{diag}(12x,\ 6z+4)`$; en ambos puntos el primer elemento es cero, la forma es solo semidefinida y la condición suficiente no dice nada. Miramos la propia función: con $`z=z_0`$ fijo
```math
g(x,z_0)-g(0,z_0)=2x^3,
```
expresión positiva para $`x>0`$ y negativa para $`x<0`$. Así que en todo entorno de cada uno de los dos puntos estacionarios $`g`$ toma valores mayores y menores que en el propio punto. No hay extremo.

**Respuesta.** No hay puntos de extremo local condicionado. Los puntos estacionarios de la función de Lagrange son $`(0;0;0;0)`$ y $`(0;0;-\tfrac43;-\tfrac43)`$, pero ninguno es un punto de extremo.

**Por qué funciona.** En la variable $`z`$ todo va «bien»: $`z^3+2z^2`$ tiene un mínimo en $`z=0`$ y un máximo en $`z=-\frac43`$. Lo estropea el sumando $`2x^3`$: el punto estacionario de un cubo es una inflexión. Un extremo de una función de varias variables exige un extremo en todas las direcciones a la vez; basta una dirección «mala». Es un ejemplo de que las igualdades de Lagrange no garantizan un extremo.

> **Observación sobre una variante del enunciado.** En el archivo abreviado de la tarea 3 el mismo problema aparece con $`y^2`$ en lugar de $`y^3`$: $`f=x^3+y^2+z^3+2t^2`$. Entonces $`g(x,z)=(x^3+x^2)+(z^3+2z^2)`$, los puntos estacionarios son $`x\in\{0,-\tfrac23\}`$, $`z\in\{0,-\tfrac43\}`$, la hessiana es $`\operatorname{diag}(6x+2,\ 6z+4)`$, y la respuesta es otra: $`(0;0;0;0)`$ es un mínimo local condicionado estricto ($`f=0`$), $`(-\tfrac23;-\tfrac23;-\tfrac43;-\tfrac43)`$ es un máximo local condicionado estricto ($`f=\tfrac4{27}+\tfrac{32}{27}=\tfrac43`$), y $`(0;0;-\tfrac43;-\tfrac43)`$ y $`(-\tfrac23;-\tfrac23;0;0)`$ son puntos de silla. La solución de arriba sigue la tarea 2, donde figura $`y^3`$.

## Problema 2'.1

**Enunciado.** $`f=xyz`$, $`M=\{x^2+y^2+z^2=1,\ x+y-z=0\}`$. Hallar todos los puntos de extremo condicionado y los valores extremos.

**Solución.** *Regularidad.* Los gradientes de las ligaduras $`(2x,2y,2z)`$ y $`(1,1,-1)`$ son linealmente dependientes solo si $`(x,y,z)=c\,(1,1,-1)`$; entonces $`x+y-z=3c=0`$, es decir, el punto es el origen, que no está en la esfera. Así que el rango es 2 en todo $`M`$.

*Sistema de Lagrange* con $`L=xyz-\lambda(x^2+y^2+z^2-1)-\mu(x+y-z)`$:
```math
yz=2\lambda x+\mu,\qquad xz=2\lambda y+\mu,\qquad xy=2\lambda z-\mu .
```
Restando la segunda ecuación de la primera: $`z(y-x)=2\lambda(x-y)`$, es decir, $`(x-y)(z+2\lambda)=0`$.

- Si $`x=y`$, las ligaduras dan $`z=2x`$ y $`6x^2=1`$: los puntos $`\pm\frac1{\sqrt6}(1;1;2)`$.
- Si $`z=-2\lambda`$, sumamos la primera y la tercera: $`y(x+z)=2\lambda(x+z)=-z(x+z)`$, es decir, $`(x+z)(y+z)=0`$. Para $`x=-z`$ el plano da $`y=2z`$, y $`6z^2=1`$: los puntos $`\pm\frac1{\sqrt6}(-1;2;1)`$. Para $`y=-z`$, análogamente $`x=2z`$: los puntos $`\pm\frac1{\sqrt6}(2;-1;1)`$.

En total, seis puntos estacionarios. Valores de $`f`$:
```math
f=\frac{1}{3\sqrt6}=\frac{\sqrt6}{18}\ \text{ en los puntos }\ \tfrac1{\sqrt6}(1;1;2),\ \tfrac1{\sqrt6}(1;-2;-1),\ \tfrac1{\sqrt6}(-2;1;-1);
```
```math
f=-\frac{1}{3\sqrt6}=-\frac{\sqrt6}{18}\ \text{ en los puntos }\ \tfrac1{\sqrt6}(-1;-1;-2),\ \tfrac1{\sqrt6}(-1;2;1),\ \tfrac1{\sqrt6}(2;-1;1).
```
$`M`$ es una circunferencia (sección de la esfera por un plano que pasa por el centro), un compacto. Los valores máximo y mínimo de $`f`$ sobre $`M`$ se alcanzan, y se alcanzan en puntos estacionarios, luego valen $`\pm\frac1{3\sqrt6}`$. Cada uno de los seis puntos es un punto donde $`f`$ toma su valor máximo o mínimo sobre $`M`$, es decir, un punto de extremo global (y por tanto local).

**Respuesta.** El máximo condicionado $`f_{\max}=\dfrac{1}{3\sqrt6}`$ se alcanza en los tres puntos $`\frac1{\sqrt6}(1;1;2)`$, $`\frac1{\sqrt6}(1;-2;-1)`$, $`\frac1{\sqrt6}(-2;1;-1)`$; el mínimo condicionado $`f_{\min}=-\dfrac{1}{3\sqrt6}`$, en los tres puntos opuestos. No hay otros puntos de extremo condicionado.

**Por qué funciona.** El cambio $`w=-z`$ hace simétrico el problema: las ligaduras $`x+y+w=0`$, $`x^2+y^2+w^2=1`$ y la función $`-xyw`$ no cambian al permutar $`x,y,w`$. De ahí las «ternas» de puntos. La circunferencia se puede parametrizar explícitamente:
```math
x=\sqrt{\tfrac23}\cos\varphi,\qquad y=\sqrt{\tfrac23}\cos\bigl(\varphi+\tfrac{2\pi}3\bigr),\qquad w=\sqrt{\tfrac23}\cos\bigl(\varphi-\tfrac{2\pi}3\bigr),
```
y entonces la identidad $`\cos\varphi\cos(\varphi+\frac{2\pi}3)\cos(\varphi-\frac{2\pi}3)=\frac14\cos3\varphi`$ da
```math
f=-xyw=-\frac{\cos3\varphi}{3\sqrt6}.
```
Sobre la circunferencia $`f`$ es simplemente $`\cos3\varphi`$ salvo un factor: tres máximos y tres mínimos se alternan cada $`60^\circ`$, y no puede haber otros extremos. Puntos opuestos dan valores opuestos porque $`f`$ es impar y $`M`$ es simétrico respecto del origen.

## Problema 2'.2

**Enunciado.** $`n,m\in\mathbb N`$, $`a>0`$, $`f_m(x)=\sum_{k=1}^nx_k^m`$, $`M=\{\sum_{k=1}^nx_k=a\}`$. Hallar todos los puntos de extremo condicionado y los valores extremos.

**Solución.** La ligadura es $`\varphi=\sum x_k-a`$, $`\nabla\varphi=(1,\dots,1)\ne0`$: regular en todas partes.

**Caso $`n=1`$.** $`M=\{a\}`$ consta de un solo punto; formalmente es punto de máximo y de mínimo, con valor $`a^m`$.

**Caso $`m=1`$** (el caso trivial de la indicación). Sobre $`M`$ la función es constante: $`f_1=\sum x_k=a`$. Cada punto de $`M`$ es a la vez punto de máximo y de mínimo condicionado no estricto; el valor extremo es $`a`$.

**Caso $`n\ge2`$, $`m\ge2`$.** Sistema de Lagrange: $`m\,x_k^{m-1}=\lambda`$ para todo $`k`$, es decir, **todos los números $`x_k^{m-1}`$ son iguales**.

*$`m`$ par.* Entonces $`m-1`$ es impar, la función $`t\mapsto t^{m-1}`$ es estrictamente creciente, y todos los $`x_k`$ son iguales: $`x_k=\frac an`$. El único punto estacionario es $`P=(\frac an,\dots,\frac an)`$, $`f_m(P)=n\bigl(\frac an\bigr)^m=\frac{a^m}{n^{m-1}}`$. Es un mínimo global: para $`m`$ par la función $`t\mapsto t^m`$ es convexa en toda la recta, y por la desigualdad de Jensen
```math
\frac1n\sum_{k=1}^nx_k^m\ \ge\ \Bigl(\frac1n\sum_{k=1}^nx_k\Bigr)^m=\Bigl(\frac an\Bigr)^m,
```
con igualdad solo para $`x_k`$ iguales (convexidad estricta). No hay máximo: en los puntos $`(a+T,-T,0,\dots,0)\in M`$ el valor $`(a+T)^m+T^m\to+\infty`$ cuando $`T\to+\infty`$; y no hay otros puntos de extremo, pues el punto estacionario es único.

*$`m`$ impar, $`m\ge3`$.* Entonces $`m-1`$ es par, y de $`x_k^{m-1}=\mathrm{const}`$ solo se deduce $`|x_k|=r`$ para todo $`k`$. Sean $`q`$ coordenadas iguales a $`-r`$ y las restantes $`p=n-q`$ iguales a $`+r`$. La ligadura: $`(p-q)r=a>0`$, luego $`r>0`$, $`p>q`$ y $`r=\frac{a}{n-2q}`$. Puntos estacionarios: para cada conjunto de $`q<\frac n2`$ índices, el punto cuyas coordenadas con esos índices valen $`-\frac{a}{n-2q}`$ y las demás $`+\frac{a}{n-2q}`$.

Los estudiamos con la diferencial segunda de la función de Lagrange:
```math
d^2L(h)=m(m-1)\sum_{k=1}^nx_k^{m-2}h_k^2=m(m-1)\,r^{m-2}\Bigl(\sum_{k:\,x_k>0}h_k^2-\sum_{k:\,x_k<0}h_k^2\Bigr)
```
(el exponente $`m-2`$ es impar, así que el signo de cada coeficiente es el signo de $`x_k`$), sobre el espacio tangente $`\sum h_k=0`$.

- $`q=0`$ (todas las coordenadas valen $`\frac an`$): la forma es definida positiva, mínimo local estricto, $`f_m=\frac{a^m}{n^{m-1}}`$.
- $`q\ge1`$. Entonces $`p\ge2`$, y sobre el vector $`h=e_i-e_j`$ con dos índices «positivos» la forma es positiva. Por otra parte, tomemos $`h`$ con $`-1`$ en un índice «negativo» y $`\frac1p`$ en cada uno de los $`p`$ «positivos»: la suma de coordenadas es cero y el paréntesis vale $`p\cdot\frac1{p^2}-1=\frac1p-1<0`$. La forma es indefinida: no hay extremo.

Así, para $`m\ge3`$ impar el único punto de extremo es $`P=(\frac an,\dots,\frac an)`$, un mínimo local estricto.

**Respuesta.**

| Caso | Puntos de extremo condicionado | Valor |
|---|---|---|
| $`n=1`$ | el único punto $`x_1=a`$ | $`a^m`$ |
| $`m=1`$ | todos los puntos de $`M`$ (máximo y mínimo no estrictos) | $`a`$ |
| $`n\ge2`$, $`m`$ par | $`(\frac an,\dots,\frac an)`$: mínimo global estricto; no hay máximo | $`\dfrac{a^m}{n^{m-1}}`$ |
| $`n\ge2`$, $`m\ge3`$ impar | $`(\frac an,\dots,\frac an)`$: mínimo local estricto; no hay otros | $`\dfrac{a^m}{n^{m-1}}`$ |

**Por qué funciona.** La igualdad de Lagrange $`x_k^{m-1}=\mathrm{const}`$ dice: en un extremo el «precio marginal» de cada coordenada es el mismo; si no, se podría trasvasar un poco de una coordenada a otra sin violar $`\sum x_k=a`$ y cambiar $`f_m`$ en primer orden. Para $`m`$ par esto da coordenadas iguales; para $`m`$ impar, solo módulos iguales, y aparecen puntos estacionarios adicionales con coordenadas negativas. Resultan ser puntos de silla: cerca de un $`x_k`$ negativo la función $`t^m`$ es cóncava, cerca de uno positivo es convexa, y sobre el hiperplano siempre hay una dirección de cada tipo.

¿Es global el mínimo para $`m`$ impar? Para $`n=2`$, sí: $`f_m(a-T,T)=(a-T)^m+T^m`$ es un polinomio de grado par $`m-1`$ con coeficiente principal $`ma>0`$; está acotado inferiormente y tiene el único punto estacionario $`T=\frac a2`$. Para $`n\ge3`$, no: en los puntos $`(T,T,a-2T,0,\dots,0)`$ el valor $`2T^m+(a-2T)^m`$ se comporta como $`(2-2^m)T^m\to-\infty`$ cuando $`T\to+\infty`$. Para $`m\ge3`$ impar y $`n\ge2`$, $`f_m`$ nunca está acotada superiormente.

## Problema 2'.3

**Enunciado.** $`n\in\mathbb N`$, $`m_k\in\mathbb N`$, $`m_k\ge2`$, $`a>0`$, $`f(x)=\prod_{k=1}^nx_k^{m_k}`$, $`M=\{\sum_{k=1}^nx_k=a\}`$. Hallar todos los puntos de extremo condicionado y los valores extremos.

**Solución.** Sea $`m=\sum_{k=1}^nm_k`$. Para $`n=1`$ el conjunto $`M=\{a\}`$ es un punto, con valor $`a^{m_1}`$; en adelante $`n\ge2`$. La regularidad es como en 2'.2.

*Puntos estacionarios.* Condición de Lagrange: $`\partial_kf=\lambda`$ para todo $`k`$, donde
```math
\partial_kf=m_kx_k^{m_k-1}\prod_{j\ne k}x_j^{m_j}.
```

**(A) Todos los $`x_k\ne0`$.** Entonces $`\partial_kf=\dfrac{m_kf}{x_k}=\lambda`$ y $`f\ne0`$, de donde $`\lambda\ne0`$ y $`x_k=\dfrac{f}{\lambda}m_k`$: las coordenadas son proporcionales a los exponentes. La ligadura da $`\frac f\lambda\,m=a`$, es decir,
```math
x_k^*=\frac{a\,m_k}{m},\qquad k=1,\dots,n .
```
Es el único punto estacionario sin coordenadas nulas; todas sus coordenadas son positivas.

**(B) Hay una coordenada nula, $`x_i=0`$.** Como $`m_i\ge2`$, cada derivada parcial contiene el factor $`x_i^{m_i}`$ o $`x_i^{m_i-1}`$ y se anula. Así que $`\nabla f=0`$, y **todo** punto de $`M`$ con al menos una coordenada nula es estacionario (con $`\lambda=0`$); en él $`f=0`$.

*El punto $`P^*`$.* Sobre el conjunto $`\Delta=\{x\in M:\ x_k\ge0\ \forall k\}`$ (un símplice, compacto) la función $`f`$ es continua, positiva en el interior y nula en la frontera. Su valor máximo sobre $`\Delta`$ se alcanza, y se alcanza en el interior, luego en un punto estacionario, es decir, en $`P^*`$. El interior de $`\Delta`$ es abierto en $`M`$, así que $`P^*`$ es un punto de máximo local condicionado estricto, y
```math
f(P^*)=\prod_{k=1}^n\Bigl(\frac{a\,m_k}{m}\Bigr)^{m_k}=\Bigl(\frac am\Bigr)^{m}\prod_{k=1}^nm_k^{m_k}.
```

*Puntos de tipo (B).* Sea $`x\in M`$, $`Z=\{k:\ x_k=0\}\ne\varnothing`$. No todas las coordenadas son nulas (su suma es $`a>0`$), así que el complemento de $`Z`$ no es vacío. Escribamos un punto vecino de $`M`$ como $`x+h`$:
```math
f(x+h)=\underbrace{\prod_{k\notin Z}(x_k+h_k)^{m_k}}_{A(h)}\cdot\prod_{k\in Z}h_k^{m_k}.
```
Para $`h`$ pequeño el factor $`A(h)`$ conserva el signo del número $`\sigma=\prod_{k\notin Z}(\operatorname{sign}x_k)^{m_k}=\pm1`$. Los incrementos $`h_k`$, $`k\in Z`$, pueden ser números pequeños cualesquiera: la condición $`\sum h_k=0`$ se cumple a costa de una coordenada fuera de $`Z`$.

- Si **todos los $`m_k`$, $`k\in Z`$, son pares**, entonces $`\prod_{k\in Z}h_k^{m_k}\ge0`$, y cerca de $`x`$ la función $`f`$ tiene el signo de $`\sigma`$ o es nula. Como $`f(x)=0`$: para $`\sigma=+1`$ es un mínimo local, para $`\sigma=-1`$ un máximo local.
- Si **algún $`m_i`$, $`i\in Z`$, es impar**, tomemos todos los $`h_k=\varepsilon>0`$ para $`k\in Z`$, $`k\ne i`$, y $`h_i=\pm\varepsilon`$. El producto toma ambos signos para $`\varepsilon`$ arbitrariamente pequeño. No hay extremo.

El número $`\sigma`$ vale $`(-1)^N`$, donde $`N`$ es la cantidad de índices $`k\notin Z`$ con $`x_k<0`$ y $`m_k`$ impar.

**Respuesta** (para $`n\ge2`$).

1. El punto $`P^*=\Bigl(\dfrac{a\,m_1}{m};\dots;\dfrac{a\,m_n}{m}\Bigr)`$, $`m=\sum m_k`$, es un máximo local condicionado estricto, $`f(P^*)=\Bigl(\dfrac am\Bigr)^m\prod\limits_{k=1}^nm_k^{m_k}`$.
2. Un punto $`x\in M`$ con conjunto no vacío $`Z`$ de coordenadas nulas es un punto de extremo condicionado si y solo si todos los $`m_k`$ con $`k\in Z`$ son pares. El valor extremo es $`0`$; es un mínimo si el número de coordenadas negativas con exponente impar es par, y un máximo si es impar.
3. No hay otros puntos de extremo condicionado.

**Por qué funciona.** En la región $`x_k>0`$ la respuesta la dicta la desigualdad ponderada entre las medias: $`\prod\bigl(\frac{x_k}{m_k}\bigr)^{m_k}\le\bigl(\frac{\sum x_k}{m}\bigr)^m`$ con igualdad cuando $`\frac{x_k}{m_k}=\mathrm{const}`$: la suma hay que repartirla en proporción a los exponentes. Lo mismo da tomar logaritmos: $`\ln f=\sum m_k\ln x_k`$, y la condición de Lagrange es $`\frac{m_k}{x_k}=\mathrm{const}`$.

La condición $`m_k\ge2`$ es esencial: por ella $`f`$ se anula sobre el hiperplano $`x_k=0`$ junto con su gradiente, y todo ese hiperplano consta de puntos estacionarios. Allí la diferencial segunda es degenerada, por lo que hay que mirar directamente el signo de $`f`$. Una potencia par $`h_k^{m_k}`$ no cambia de signo («toca el cero»), una impar sí («cruza el cero»); de ahí el criterio.

Los extremos del punto 2 son no estrictos para $`n\ge3`$ (cerca hay otros puntos con $`x_k=0`$, donde también $`f=0`$) y estrictos para $`n=2`$. El máximo local en $`P^*`$, en general, no es global: por ejemplo, para $`n=2`$, $`m_1=m_2=2`$ se tiene $`f(T,a-T)=T^2(a-T)^2\to+\infty`$. Es global solo para $`n=2`$ con $`m_1,m_2`$ impares (entonces $`f\le0`$ fuera del segmento entre $`(a;0)`$ y $`(0;a)`$). Si todos los $`m_k`$ son pares, $`f\ge0`$ en todas partes y todos los puntos con una coordenada nula son puntos de mínimo global.

**Ejemplo.** $`n=2`$, $`f=x^2y^3`$, $`x+y=a`$. $`P^*=(\frac{2a}5;\frac{3a}5)`$ es un máximo local, $`f=\frac{108a^5}{3125}`$. El punto $`(0;a)`$: $`Z=\{1\}`$, $`m_1=2`$ es par, $`\sigma=+1`$: mínimo local estricto, $`f=0`$. El punto $`(a;0)`$: $`Z=\{2\}`$, $`m_2=3`$ es impar: no hay extremo. Esto concuerda con la gráfica de $`g(x)=x^2(a-x)^3`$: $`g'(x)=x(a-x)^2(2a-5x)`$.
