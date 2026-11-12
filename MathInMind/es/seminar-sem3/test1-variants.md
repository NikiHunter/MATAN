---
title: "Seminario NM-204. Control 1 — variantes de práctica"
lang: es
---
# Control 1: variantes de práctica con soluciones

[Русский](../../ru/seminar-sem3/test1-variants.md) · [English](../../en/seminar-sem3/test1-variants.md) · **Español**

[Todas las tareas](index.md) · [← Cómo prepararse](test1-guide.md)

> **Qué es esto.** Tres variantes de práctica con el formato previsto del control: cuatro ejercicios, apartados 1.1, 1.2, 2.1, 2.2, 3, 4. Los problemas están hechos a imagen de las tareas 1–4; no hay variantes reales, es un pronóstico. Se conserva la notación del seminario: los criterios usan el cociente $`\frac{a_k}{a_{k+1}}`$. Referencia de tiempo: 80–90 minutos por variante. Resuelva por escrito y solo después abra las soluciones.

## Variante A

**1.1.** Desarrollar por la fórmula de Taylor en el punto $`(1;-2)`$ la función $`f(x,y)=x^3+2x^2y-y^3+4x`$.

**1.2.** Hallar la forma explícita del desarrollo de Taylor de $`f(x,y)=e^{x^2-y}`$ hasta grado dos con resto en forma de Lagrange en el punto $`(1;1)`$.

**2.1.** Hallar todos los puntos de extremo local condicionado de $`f(x,y)=x^3-3xy+y^2`$ sobre el conjunto $`M=\{(x,y):\ y=2x\}`$.

**2.2.** Hallar todos los puntos de extremo condicionado de $`f(x,y,z)=x-2y+2z`$ sobre el conjunto $`M=\{x^2+y^2+z^2=9\}`$ y los valores extremos.

**3.** Sean $`a_n>0`$, $`b_n>0`$ y $`\dfrac{a_{n+1}}{a_n}\le\dfrac{b_{n+1}}{b_n}`$ para todo $`n>N_0`$. Demostrar que de la convergencia de $`\sum b_k`$ se sigue la de $`\sum a_k`$. Con esta afirmación, demostrar la convergencia de $`\sum\limits_{k=1}^\infty\dfrac1{k!}`$.

**4.** Estudiar la convergencia de las series
```math
\text{a)}\ \sum_{k=1}^\infty\frac{(k!)^2}{(2k)!};\qquad\text{b)}\ \sum_{k=1}^\infty\frac{(2k-1)!!}{(2k+2)!!};\qquad\text{c)}\ \sum_{k=1}^\infty\frac{(-1)^k}{\ln(k+1)} .
```

<details>
<summary>Soluciones de la variante A</summary>

**1.1.** Sean $`h_1=x-1`$, $`h_2=y+2`$. $`f(1,-2)=1-4+8+4=9`$. $`f_x=3x^2+4xy+4=-1`$, $`f_y=2x^2-3y^2=-10`$. $`f_{xx}=6x+4y=-2`$, $`f_{xy}=4x=4`$, $`f_{yy}=-6y=12`$. $`f_{xxx}=6`$, $`f_{xxy}=4`$, $`f_{xyy}=0`$, $`f_{yyy}=-6`$; las derivadas de cuarto orden son nulas, así que la suma es finita y la igualdad es exacta:

```math
f=9-h_1-10h_2-h_1^2+4h_1h_2+6h_2^2+h_1^3+2h_1^2h_2-h_2^3 .
```

Comprobación: $`h=(1,0)`$, $`f(2,-2)=8-16+8+8=8`$; la fórmula da $`9-1-1+1=8`$.

**1.2.** Sean $`h_1=x-1`$, $`h_2=y-1`$. Derivadas: $`f_x=2xf`$, $`f_y=-f`$, $`f_{xx}=(4x^2+2)f`$, $`f_{xy}=-2xf`$, $`f_{yy}=f`$. En $`(1;1)`$: $`f=1`$, $`f_x=2`$, $`f_y=-1`$, $`f_{xx}=6`$, $`f_{xy}=-2`$, $`f_{yy}=1`$. Derivadas terceras: $`f_{xxx}=(8x^3+12x)f`$, $`f_{xxy}=-(4x^2+2)f`$, $`f_{xyy}=2xf`$, $`f_{yyy}=-f`$. Existe $`\theta\in(0,1)`$ tal que

```math
e^{x^2-y}=1+2h_1-h_2+3h_1^2-2h_1h_2+\frac{h_2^2}2+R_2,
```

```math
R_2=\frac{e^{\xi^2-\eta}}{6}\Bigl[(8\xi^3+12\xi)h_1^3-3(4\xi^2+2)h_1^2h_2+6\xi h_1h_2^2-h_2^3\Bigr],\qquad\xi=1+\theta h_1,\ \eta=1+\theta h_2 .
```

Comprobación del polinomio: $`x^2-y=(2h_1-h_2)+h_1^2`$, y $`e^w=1+w+\frac{w^2}2+\dots`$ da $`1+(2h_1-h_2)+h_1^2+\frac{(2h_1-h_2)^2}2`$: lo mismo.

**2.1.** Sobre $`M`$: $`g(x)=f(x,2x)=x^3-6x^2+4x^2=x^3-2x^2`$. $`g'(x)=3x^2-4x=x(3x-4)`$, ceros $`x=0`$ y $`x=\frac43`$. $`g''(x)=6x-4`$: $`g''(0)=-4<0`$, $`g''(\frac43)=4>0`$.

Respuesta: $`(0;0)`$ es un máximo local condicionado estricto, $`f=0`$; $`(\frac43;\frac83)`$ es un mínimo local condicionado estricto, $`f=\frac{64}{27}-\frac{32}9=-\frac{32}{27}`$. No hay extremos globales: $`g(x)\to\pm\infty`$.

**2.2.** $`\nabla\varphi=(2x,2y,2z)\ne0`$ sobre $`M`$. Sistema de Lagrange: $`1=2\lambda x`$, $`-2=2\lambda y`$, $`2=2\lambda z`$; $`\lambda\ne0`$ y $`(x,y,z)=\frac1{2\lambda}(1,-2,2)=t(1,-2,2)`$. La ligadura da $`9t^2=9`$, $`t=\pm1`$. La esfera es compacta y $`f`$ continua: los valores máximo y mínimo se alcanzan en puntos estacionarios.

Respuesta: $`(1;-2;2)`$ es el máximo, $`f=9`$; $`(-1;2;-2)`$ es el mínimo, $`f=-9`$. No hay otros puntos de extremo. Comprobación: por Cauchy–Schwarz, $`|x-2y+2z|\le\sqrt{1+4+4}\cdot\sqrt9=9`$.

**3.** Multiplicando la desigualdad por $`\frac{a_n}{b_{n+1}}>0`$ se obtiene $`\frac{a_{n+1}}{b_{n+1}}\le\frac{a_n}{b_n}`$ para $`n>N_0`$: la sucesión $`\frac{a_n}{b_n}`$ es no creciente, luego $`a_n\le Cb_n`$ para $`n\ge N_0+1`$, donde $`C=\frac{a_{N_0+1}}{b_{N_0+1}}`$. Sea $`B`$ la suma de $`\sum_{k>N_0}b_k`$ (converge junto con $`\sum b_k`$). Entonces $`\sum_{k=N_0+1}^na_k\le C\sum_{k=N_0+1}^nb_k\le CB`$. Las sumas parciales de la serie positiva $`\sum_{k>N_0}a_k`$ están acotadas, luego converge; añadir un número finito de términos no cambia la convergencia.

Aplicación: $`a_k=\frac1{k!}`$, $`b_k=\frac1{k(k+1)}`$ (la serie $`\sum b_k`$ converge: sus sumas parciales valen $`1-\frac1{n+1}`$). $`\frac{a_{k+1}}{a_k}=\frac1{k+1}`$, $`\frac{b_{k+1}}{b_k}=\frac k{k+2}`$; la desigualdad $`\frac1{k+1}\le\frac k{k+2}`$ equivale a $`k^2\ge2`$ y vale para $`k\ge2`$, es decir, $`N_0=1`$.

**4.** a) $`\dfrac{a_k}{a_{k+1}}=\dfrac{(2k+2)(2k+1)}{(k+1)^2}=\dfrac{2(2k+1)}{k+1}\ge3`$ para todo $`k\ge1`$ (y tiende a $`4`$). Por el criterio de d'Alembert con $`\beta=2`$ la serie **converge**.

b) $`\dfrac{a_k}{a_{k+1}}=\dfrac{2k+4}{2k+1}=1+\dfrac3{2k+1}\to1`$: d'Alembert no sirve. $`R_k=\dfrac{3k}{2k+1}\to\dfrac32>1`$: por el criterio de Raabe la serie **converge**. (Sin límite: $`\frac3{2k+1}\ge\frac{5/4}k`$ para $`k\ge3`$, $`\gamma=\frac14`$.)

c) Los signos alternan, $`\frac1{\ln(k+1)}`$ decrece y tiende a cero: por el criterio de Leibniz la serie **converge**. No hay convergencia absoluta: $`\ln(k+1)\le k`$, luego $`\frac1{\ln(k+1)}\ge\frac1k`$. La convergencia es condicional.
</details>

## Variante B

**1.1.** Desarrollar por la fórmula de Taylor en el punto $`(1;2;-1)`$ la función $`f(x,y,z)=xyz+x^2-z^2`$.

**1.2.** Hallar la forma explícita del desarrollo de Taylor de $`f(x,y)=\ln(x+y^2)`$ hasta grado dos con resto en forma de Lagrange en el punto $`(1;0)`$.

**2.1.** Hallar todos los puntos de extremo local condicionado de $`f(x,y,z)=xy+2z^2`$ sobre el conjunto $`M=\{x+y=2,\ z=x-1\}`$.

**2.2.** Hallar todos los puntos de extremo condicionado de $`f(x,y)=xy`$ sobre el conjunto $`M=\{x^2+4y^2=8\}`$ y los valores extremos.

**3.** Enunciar y demostrar el criterio de Leibniz. ¿Sigue siendo cierto si la condición $`a_ka_{k+1}<0`$ se sustituye por $`a_ka_{k+1}\le0`$?

**4.** Estudiar la convergencia de las series ($`\alpha\in\mathbb R`$ es un parámetro)
```math
\text{a)}\ \sum_{k=1}^\infty\frac{k^k}{3^k\,k!};\qquad\text{b)}\ \sum_{k=1}^\infty\frac{\sqrt{k^2+1}-k}{k^\alpha};\qquad\text{c)}\ \sum_{k=1}^\infty\frac{\sin\frac{k\pi}2}{\sqrt[3]k} .
```

<details>
<summary>Soluciones de la variante B</summary>

**1.1.** Sean $`h_1=x-1`$, $`h_2=y-2`$, $`h_3=z+1`$. $`f(a)=-2+1-1=-2`$. $`f_x=yz+2x=0`$, $`f_y=xz=-1`$, $`f_z=xy-2z=4`$. $`f_{xx}=2`$, $`f_{yy}=0`$, $`f_{zz}=-2`$, $`f_{xy}=z=-1`$, $`f_{xz}=y=2`$, $`f_{yz}=x=1`$. La única derivada tercera no nula es $`f_{xyz}=1`$ (entra con coeficiente $`6`$ y se divide por $`3!`$). La suma es finita:

```math
f=-2-h_2+4h_3+h_1^2-h_3^2-h_1h_2+2h_1h_3+h_2h_3+h_1h_2h_3 .
```

Comprobación: $`h=(0,0,1)`$, $`f(1,2,0)=1`$; la fórmula da $`-2+4-1=1`$.

**1.2.** Sean $`h_1=x-1`$, $`h_2=y`$, $`u=x+y^2`$. Derivadas: $`f_x=\frac1u`$, $`f_y=\frac{2y}u`$, $`f_{xx}=-\frac1{u^2}`$, $`f_{xy}=-\frac{2y}{u^2}`$, $`f_{yy}=\frac2u-\frac{4y^2}{u^2}`$. En $`(1;0)`$: $`f=0`$, $`f_x=1`$, $`f_y=0`$, $`f_{xx}=-1`$, $`f_{xy}=0`$, $`f_{yy}=2`$. Derivadas terceras:

```math
f_{xxx}=\frac2{u^3},\quad f_{xxy}=\frac{4y}{u^3},\quad f_{xyy}=\frac{8y^2-2u}{u^3},\quad f_{yyy}=\frac{16y^3-12uy}{u^3}.
```

Para los $`h`$ tales que el segmento de $`(1;0)`$ a $`(1+h_1;h_2)`$ está en el dominio $`x+y^2>0`$, existe $`\theta\in(0,1)`$ tal que

```math
\ln(x+y^2)=h_1-\frac{h_1^2}2+h_2^2+R_2,
```

```math
R_2=\frac{1}{6u_c^3}\Bigl[2h_1^3+12\eta h_1^2h_2+3(8\eta^2-2u_c)h_1h_2^2+(16\eta^3-12u_c\eta)h_2^3\Bigr],
```

donde $`\xi=1+\theta h_1`$, $`\eta=\theta h_2`$, $`u_c=\xi+\eta^2`$.

Comprobación del polinomio: $`x+y^2=1+w`$, $`w=h_1+h_2^2`$, $`\ln(1+w)=w-\frac{w^2}2+\dots=h_1+h_2^2-\frac{h_1^2}2+\dots`$

**2.1.** Las ligaduras se despejan: $`y=2-x`$, $`z=x-1`$. $`g(x)=x(2-x)+2(x-1)^2=x^2-2x+2=(x-1)^2+1`$. El único punto de extremo es $`x=1`$, un mínimo.

Respuesta: $`(1;1;0)`$ es un mínimo condicionado estricto (global sobre $`M`$), $`f=1`$. No hay máximo: $`g(x)\to+\infty`$.

**2.2.** $`\nabla\varphi=(2x,8y)\ne0`$ sobre $`M`$. Sistema: $`y=2\lambda x`$, $`x=8\lambda y`$. Sustituyendo: $`y=16\lambda^2y`$. Si $`y=0`$, entonces $`x=0`$, punto que no está en $`M`$; luego $`\lambda=\pm\frac14`$. Para $`\lambda=\frac14`$: $`x=2y`$, $`8y^2=8`$, los puntos $`(2;1)`$ y $`(-2;-1)`$, $`f=2`$. Para $`\lambda=-\frac14`$: $`x=-2y`$, los puntos $`(-2;1)`$ y $`(2;-1)`$, $`f=-2`$. La elipse es compacta.

Respuesta: máximo $`f=2`$ en $`(2;1)`$, $`(-2;-1)`$; mínimo $`f=-2`$ en $`(-2;1)`$, $`(2;-1)`$. Comprobación: $`8=x^2+4y^2\ge2\cdot|x|\cdot2|y|=4|xy|`$.

**3.** *Enunciado.* Si para todo $`k`$ se cumplen $`a_ka_{k+1}<0`$, $`|a_{k+1}|\le|a_k|`$ y $`a_k\to0`$, la serie $`\sum a_k`$ converge.

*Demostración.* Podemos suponer $`a_1>0`$ (si no, multiplicamos la serie por $`-1`$); entonces $`a_{2j-1}>0`$, $`a_{2j}<0`$. Los paréntesis $`a_{2j-1}+a_{2j}=|a_{2j-1}|-|a_{2j}|\ge0`$, luego $`S_{2m}=\sum_{j=1}^m(a_{2j-1}+a_{2j})`$ es no decreciente. Por otra parte, $`S_{2m}=a_1+\sum_{j=1}^{m-1}(a_{2j}+a_{2j+1})+a_{2m}\le a_1`$, pues $`a_{2j}+a_{2j+1}=-|a_{2j}|+|a_{2j+1}|\le0`$ y $`a_{2m}<0`$. La sucesión monótona y acotada $`S_{2m}`$ converge a cierto $`S`$. Entonces $`S_{2m+1}=S_{2m}+a_{2m+1}\to S`$, pues $`a_k\to0`$. Las subsucesiones de índices pares e impares convergen al mismo límite, luego $`S_n\to S`$.

*La pregunta.* Sí. Si todos los $`a_k\ne0`$, la condición $`\le0`$ coincide con $`<0`$. Si $`a_K=0`$, de $`|a_{k+1}|\le|a_k|`$ se sigue $`a_k=0`$ para $`k\ge K`$, y la serie es una suma finita.

**4.** a) $`\dfrac{a_k}{a_{k+1}}=\dfrac{k^k}{3^kk!}\cdot\dfrac{3^{k+1}(k+1)!}{(k+1)^{k+1}}=\dfrac{3}{\bigl(1+\frac1k\bigr)^k}>\dfrac3e>1`$ para todo $`k`$, ya que $`\bigl(1+\frac1k\bigr)^k<e`$. Por el criterio de d'Alembert con $`\beta=\frac3e-1`$ la serie **converge**.

b) $`\sqrt{k^2+1}-k=\dfrac{1}{\sqrt{k^2+1}+k}`$, luego $`a_k=\dfrac{C_k}{k^{\alpha+1}}`$, $`C_k=\dfrac{k}{\sqrt{k^2+1}+k}`$. Como $`k<\sqrt{k^2+1}\le\sqrt2\,k`$, se tiene $`\dfrac1{1+\sqrt2}\le C_k<\dfrac12`$. Por el problema 3.11 la serie **converge para $`\alpha>0`$ y diverge para $`\alpha\le0`$**.

c) Para $`k`$ par los términos son nulos; para $`k=2j-1`$ el numerador vale $`(-1)^{j-1}`$. Los términos no nulos $`c_j=\dfrac{(-1)^{j-1}}{\sqrt[3]{2j-1}}`$ forman una serie convergente por el criterio de Leibniz; insertar ceros no cambia las sumas parciales ($`S_{2m-1}=S_{2m}=T_m`$). La serie **converge** (condicionalmente: $`\sum\frac1{\sqrt[3]{2j-1}}`$ diverge).
</details>

## Variante C

**1.1.** Desarrollar por la fórmula de Taylor en el punto $`(-1;1)`$ la función $`f(x,y)=x^4-x^2y+y^3`$.

**1.2.** Hallar la forma explícita del desarrollo de Taylor de $`f(x,y)=e^y\sin x`$ hasta grado dos con resto en forma de Lagrange en el punto $`(\pi;0)`$.

**2.1.** Hallar todos los puntos de extremo local condicionado de $`f(x,y,z)=x^4+y^2-2z^2`$ sobre el conjunto $`M=\{z=x\}`$.

**2.2.** Hallar todos los puntos de extremo condicionado de $`f(x,y,z)=x+y+z`$ sobre el conjunto $`M=\{x^2+y^2=2,\ x+z=1\}`$ y los valores extremos.

**3.** Sean $`x_n>0`$ y $`a_n>0`$ para todo $`n`$, y supongamos que existen $`\alpha>0`$ y $`N`$ tales que $`x_n\dfrac{a_n}{a_{n+1}}-x_{n+1}\ge\alpha`$ para todo $`n>N`$. Demostrar que la serie $`\sum a_k`$ converge. Deducir de aquí el criterio de convergencia de d'Alembert. ¿Por qué el criterio de d'Alembert no dice nada sobre la serie $`\sum\frac1{k^2}`$?

**4.** Estudiar la convergencia de las series
```math
\text{a)}\ \sum_{k=1}^\infty\Bigl(\frac{k+1}{2k+3}\Bigr)^k;\qquad\text{b)}\ \sum_{k=2}^\infty\frac{1}{k\ln^2k};\qquad\text{c)}\ \sum_{k=1}^\infty\frac{(-1)^kk}{k^2+1} .
```

<details>
<summary>Soluciones de la variante C</summary>

**1.1.** Sean $`h_1=x+1`$, $`h_2=y-1`$. $`f(a)=1-1+1=1`$. $`f_x=4x^3-2xy=-2`$, $`f_y=-x^2+3y^2=2`$. $`f_{xx}=12x^2-2y=10`$, $`f_{xy}=-2x=2`$, $`f_{yy}=6y=6`$. $`f_{xxx}=24x=-24`$, $`f_{xxy}=-2`$, $`f_{xyy}=0`$, $`f_{yyy}=6`$. $`f_{xxxx}=24`$, las demás derivadas cuartas son nulas; las quintas son nulas, la suma es finita:

```math
f=1-2h_1+2h_2+5h_1^2+2h_1h_2+3h_2^2-4h_1^3-h_1^2h_2+h_2^3+h_1^4 .
```

Comprobación: $`h=(1,0)`$, $`f(0,1)=1`$; la fórmula da $`1-2+5-4+1=1`$.

**1.2.** Sean $`h_1=x-\pi`$, $`h_2=y`$. $`f_x=e^y\cos x`$, $`f_y=e^y\sin x`$, $`f_{xx}=-e^y\sin x`$, $`f_{xy}=e^y\cos x`$, $`f_{yy}=e^y\sin x`$. En $`(\pi;0)`$: $`f=0`$, $`f_x=-1`$, $`f_y=0`$, $`f_{xx}=0`$, $`f_{xy}=-1`$, $`f_{yy}=0`$. Derivadas terceras: $`f_{xxx}=-e^y\cos x`$, $`f_{xxy}=-e^y\sin x`$, $`f_{xyy}=e^y\cos x`$, $`f_{yyy}=e^y\sin x`$. Existe $`\theta\in(0,1)`$ tal que

```math
e^y\sin x=-h_1-h_1h_2+R_2,
```

```math
R_2=\frac{e^{\eta}}6\Bigl[-\cos\xi\cdot h_1^3-3\sin\xi\cdot h_1^2h_2+3\cos\xi\cdot h_1h_2^2+\sin\xi\cdot h_2^3\Bigr],\qquad\xi=\pi+\theta h_1,\ \eta=\theta h_2 .
```

Comprobación del polinomio: $`\sin(\pi+h_1)=-\sin h_1=-h_1+\dots`$, $`e^{h_2}=1+h_2+\dots`$; el producto hasta grado dos es $`-h_1-h_1h_2`$.

**2.1.** Sobre $`M`$: $`g(x,y)=f(x,y,x)=x^4-2x^2+y^2`$. $`g_x=4x^3-4x=4x(x^2-1)`$, $`g_y=2y`$; puntos estacionarios $`(0,0)`$, $`(1,0)`$, $`(-1,0)`$. La hessiana es $`\operatorname{diag}(12x^2-4,\ 2)`$: en $`(0,0)`$ vale $`\operatorname{diag}(-4,2)`$, indefinida, no hay extremo; en $`(\pm1,0)`$ vale $`\operatorname{diag}(8,2)`$, mínimo.

Respuesta: $`(1;0;1)`$ y $`(-1;0;-1)`$ son mínimos locales condicionados estrictos, $`f=-1`$ (también globales sobre $`M`$: $`g=(x^2-1)^2+y^2-1\ge-1`$). El punto $`(0;0;0)`$ es estacionario, pero no es de extremo. No hay máximo.

**2.2.** Los gradientes de las ligaduras $`(2x,2y,0)`$ y $`(1,0,1)`$ son linealmente dependientes solo si $`x=y=0`$, y no hay tales puntos en $`M`$. $`L=x+y+z-\lambda(x^2+y^2-2)-\mu(x+z-1)`$:

```math
1-2\lambda x-\mu=0,\qquad1-2\lambda y=0,\qquad1-\mu=0 .
```

De la tercera $`\mu=1`$, de la primera $`\lambda x=0`$, de la segunda $`\lambda\ne0`$; luego $`x=0`$, $`y=\pm\sqrt2`$, $`z=1`$. El conjunto $`M`$ es cerrado y acotado ($`|x|,|y|\le\sqrt2`$, $`z=1-x`$), es decir, compacto.

Respuesta: $`(0;\sqrt2;1)`$ es el máximo, $`f=1+\sqrt2`$; $`(0;-\sqrt2;1)`$ es el mínimo, $`f=1-\sqrt2`$. Comprobación: sobre $`M`$ se tiene $`f=x+y+(1-x)=y+1`$, y $`|y|\le\sqrt2`$.

**3.** Multiplicamos la desigualdad por $`a_{n+1}>0`$: $`x_na_n-x_{n+1}a_{n+1}\ge\alpha a_{n+1}`$ para $`n>N`$. Sumamos para $`n=N+1,\dots,N+m`$; a la izquierda la suma es telescópica:

```math
\alpha\sum_{n=N+1}^{N+m}a_{n+1}\le x_{N+1}a_{N+1}-x_{N+m+1}a_{N+m+1}<x_{N+1}a_{N+1}.
```

Las sumas parciales de la serie positiva $`\sum_{k\ge N+2}a_k`$ están acotadas por $`\frac{x_{N+1}a_{N+1}}{\alpha}`$, luego converge, y con ella $`\sum a_k`$.

*D'Alembert.* Tomamos $`x_n=1`$: la condición se convierte en $`\frac{a_n}{a_{n+1}}-1\ge\alpha`$, es decir, $`\frac{a_n}{a_{n+1}}\ge1+\beta`$ con $`\beta=\alpha`$. Así, si $`\frac{a_n}{a_{n+1}}\ge1+\beta`$ para $`n>N`$, $`\beta>0`$, la serie converge.

*La serie $`\sum\frac1{k^2}`$.* $`\frac{a_k}{a_{k+1}}=\bigl(1+\frac1k\bigr)^2\to1`$. Este cociente es mayor que $`1`$ para todo $`k`$, así que la condición de divergencia $`\frac{a_k}{a_{k+1}}\le1`$ no se cumple; y tiende a $`1`$, así que con ningún $`\beta>0`$ constante se cumple $`\frac{a_k}{a_{k+1}}\ge1+\beta`$ para todo $`k`$ grande. El criterio de d'Alembert compara la serie con una progresión geométrica, y $`\frac1{k^2}`$ decrece más despacio que cualquier progresión. Aquí funciona el criterio de Raabe: $`\bigl(1+\frac1k\bigr)^2\ge1+\frac2k`$, $`\gamma=1`$.

**4.** a) $`\dfrac{k+1}{2k+3}<\dfrac12`$ para todo $`k`$ (pues $`2k+2<2k+3`$), luego $`0<a_k<2^{-k}`$. Por comparación con una progresión geométrica la serie **converge**. (Criterio de Cauchy: $`\sqrt[k]{a_k}\to\frac12<1`$.)

b) La función $`f(x)=\dfrac1{x\ln^2x}`$ es positiva y decreciente en $`[2;+\infty)`$ (el denominador crece). $`\displaystyle\int_2^x\frac{dy}{y\ln^2y}=\frac1{\ln2}-\frac1{\ln x}\to\frac1{\ln2}`$. La integral converge, y por el criterio integral la serie **converge**. (D'Alembert y Raabe callan aquí: $`R_k\to1`$.)

c) Los signos alternan. Los módulos $`\frac{k}{k^2+1}`$ decrecen: la desigualdad $`\frac{k}{k^2+1}\ge\frac{k+1}{(k+1)^2+1}`$ equivale a $`k^2+k\ge1`$. Los módulos tienden a cero. Por el criterio de Leibniz la serie **converge**. No hay convergencia absoluta: $`\frac{k}{k^2+1}\ge\frac1{2k}`$. La convergencia es condicional.
</details>

## Qué pone a prueba cada variante

| Apartado | Variante A | Variante B | Variante C |
|---|---|---|---|
| 1.1 | polinomio cúbico, 2 variables | polinomio, 3 variables, derivada mixta $`f_{xyz}`$ | polinomio de grado 4 |
| 1.2 | exponencial de un polinomio | logaritmo (dominio) | el producto $`e^y\sin x`$ |
| 2.1 | ligadura $`y=2x`$, máximo y mínimo | dos ligaduras, un mínimo | una silla y dos mínimos |
| 2.2 | función lineal sobre una esfera | $`xy`$ sobre una elipse, cuatro puntos | dos ligaduras, dos multiplicadores |
| 3 | comparación generalizada | Leibniz | Kummer ⟹ d'Alembert |
| 4 | d'Alembert, Raabe, Leibniz | d'Alembert con $`e`$, un parámetro, Leibniz con ceros | comparación (Cauchy), criterio integral, Leibniz |
