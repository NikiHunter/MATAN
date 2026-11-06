---
title: "Fórmula de Taylor en ℝⁿ, aplicaciones implícitas, extremos"
lang: es
chapter: 22
part: "Semestre 3: capítulos del profesor"
numbering: lecture
lecturer_chapter: 6
---
# 22. Fórmula de Taylor en ℝⁿ, aplicaciones implícitas, extremos

[← 21. Espacios Lᵖ y modos de convergencia](21-lp-spaces.md) · [Índice](index.md) · [Términos y teoremas](term-index.md) · [23. Series numéricas →](23-numerical-series.md)

> **Objetivo.** Exponer el final del capítulo 6 del profesor (§6.5–§6.7, [clases 65–66](lectures-2025-26/lecture-65-66.md) y [67–68](lectures-2025-26/lecture-67-68.md)) conservando la numeración del profesor: la [fórmula de Taylor](#def-6-5-1) en varias variables, el [teorema de la aplicación implícita](#thm-6-6-1), los extremos libres y condicionados. Una exposición más breve de los mismos temas, sin la numeración del profesor, está en los capítulos [15](15-multivariable-differentiation.md) y [16](16-implicit-functions-extrema.md).

<a id="sec-6-5"></a>
## §6.5. Fórmula de Taylor

Para un multiíndice $`\alpha=(\alpha_1,\ldots,\alpha_n)\in\mathbb Z_+^n`$ ponemos
```math
|\alpha|=\alpha_1+\ldots+\alpha_n,\qquad\alpha!=\alpha_1!\cdots\alpha_n!,\qquad h^\alpha=h_1^{\alpha_1}\cdots h_n^{\alpha_n},\qquad\partial^\alpha f=\frac{\partial^{|\alpha|}f}{\partial x_1^{\alpha_1}\cdots\partial x_n^{\alpha_n}}.
```
Un polinomio de grado a lo sumo $`s`$ en $`n`$ variables con valores en $`\mathbb R^m`$ es $`p(x)=\sum_{|\alpha|\le s}c_\alpha x^\alpha`$, $`c_\alpha\in\mathbb R^m`$. Se busca un polinomio que aproxime $`f`$ cerca de $`a`$ con precisión
```math
f(x)=p(x)+o(\|x-a\|^s)\qquad(x\to a).\qquad(6.5.1)
```

> <a id="def-6-5-1"></a>**Definición 6.5.1.** Sean $`E\subset\mathbb R^n`$, $`a`$ un punto interior de $`E`$, $`f:E\to\mathbb R^m`$, $`s\in\mathbb Z_+`$. Un polinomio de grado a lo sumo $`s`$ que cumple la condición (6.5.1) se llama polinomio de Taylor de $`f`$ de orden $`s`$ en el punto $`a`$ y se denota $`T_{a,s}f`$.

El polinomio de Taylor, si existe, es único: la diferencia de dos de tales polinomios es un polinomio de grado a lo sumo $`s`$ igual a $`o(\|h\|^s)`$, y un polinomio así es nulo (sustitución $`h=te`$, $`t\to0`$, parte homogénea por parte homogénea). Para $`s=0`$ la condición (6.5.1) es la continuidad de $`f`$ en $`a`$; para $`s=1`$, la diferenciabilidad.

> <a id="lem-6-5-1"></a>**Lema 6.5.1.** Sean $`E\subset\mathbb R^n`$, $`a`$ un punto interior de $`E`$, $`s\in\mathbb N`$, la aplicación $`f:E\to\mathbb R^m`$ diferenciable $`s`$ veces en el punto $`a`$, y supongamos que $`f`$ y todas sus [derivadas parciales](15-multivariable-differentiation.md#sec-15-2) de orden a lo sumo $`s`$ se anulan en el punto $`a`$. Entonces $`f(a+h)=o(\|h\|^s)`$ cuando $`h\to0`$.

La demostración es por [inducción](01-logic-sets-functions.md#example-induction) sobre $`s`$: la hipótesis de inducción se aplica a las derivadas parciales de primer orden, y el incremento de $`f`$ se expresa mediante derivadas parciales en puntos intermedios ([lema 6.3.1](lectures-2025-26/lecture-63-64.md#lem-6-3-1) sobre el incremento por coordenadas).

> <a id="thm-6-5-1"></a>**Teorema 6.5.1 (fórmula de Taylor–Peano).** Sean $`E\subset\mathbb R^n`$, $`a`$ un punto interior de $`E`$, $`s\in\mathbb N`$, y la aplicación $`f:E\to\mathbb R^m`$ diferenciable $`s`$ veces en el punto $`a`$. Entonces
> ```math
> f(x)=\sum_{|\alpha|\le s}\frac{\partial^\alpha f(a)}{\alpha!}(x-a)^\alpha+o(\|x-a\|^s)=\sum_{k=0}^{s}\frac{d_a^kf(x-a)}{k!}+o(\|x-a\|^s)\qquad(x\to a),
> ```
> es decir, el polinomio de Taylor $`T_{a,s}f`$ existe y viene dado por la primera suma.

*Idea de la demostración.* La diferencia $`g=f-T`$, donde $`T`$ es la suma de la derecha, es diferenciable $`s`$ veces en $`a`$, y todas sus derivadas parciales de orden a lo sumo $`s`$ en el punto $`a`$ son nulas (para una [aplicación diferenciable](15-multivariable-differentiation.md#sec-15-1) $`s`$ veces, las [derivadas mixtas](15-multivariable-differentiation.md#clairaut-schwarz-theorem) no dependen del orden); basta aplicar el [lema 6.5.1](#lem-6-5-1).

Para el segmento de extremos $`a,x`$ escribimos $`\Delta_{a,x}=\{a+t(x-a):\ t\in[0,1]\}`$, y $`\hat\Delta_{a,x}`$ es el mismo segmento sin sus extremos.

> <a id="thm-6-5-2"></a>**Teorema 6.5.2 (fórmula de Taylor–Lagrange).** Sean el conjunto $`E`$ abierto en $`\mathbb R^n`$, $`s\in\mathbb Z_+`$, la función $`f:E\to\mathbb R`$ diferenciable $`s+1`$ veces en $`E`$, $`a,x\in E`$, $`a\ne x`$, $`\Delta_{a,x}\subset E`$. Entonces existe $`c\in\hat\Delta_{a,x}`$ tal que
> ```math
> f(x)=\sum_{k=0}^{s}\frac{d_a^kf(x-a)}{k!}+\frac{d_c^{s+1}f(x-a)}{(s+1)!}.
> ```

*Idea de la demostración.* La función $`\varphi(t)=f(a+t(x-a))`$ es diferenciable $`s+1`$ veces en $`[0,1]`$, y por inducción $`\varphi^{(k)}(t)=d^k_{a+t(x-a)}f(x-a)`$; a $`\varphi`$ se le aplica la fórmula de Taylor en una variable con el resto de Lagrange.

> <a id="thm-6-5-3"></a>**Teorema 6.5.3 (del valor medio).** Sean el conjunto $`E`$ abierto en $`\mathbb R^n`$, la función $`f:E\to\mathbb R`$ diferenciable en $`E`$, $`a,b\in E`$, $`a\ne b`$, $`\Delta_{a,b}\subset E`$. Entonces existe $`c\in\hat\Delta_{a,b}`$ tal que $`f(b)-f(a)=d_cf(b-a)`$.

Es el caso $`s=0`$ del [teorema 6.5.2](#thm-6-5-2). Para aplicaciones la igualdad falla: para $`\gamma(t)=(\cos t,\sin t)`$ en $`[0,2\pi]`$ tenemos $`\gamma(2\pi)-\gamma(0)=0`$, mientras que $`\|\gamma'(t)\|=1`$ para todo $`t`$. Sigue siendo cierta una estimación.

> <a id="thm-6-5-4"></a>**Teorema 6.5.4 (fórmula de Taylor–Lagrange para aplicaciones).** Sean el conjunto $`E`$ abierto en $`\mathbb R^n`$, $`s\in\mathbb Z_+`$, la aplicación $`f:E\to\mathbb R^m`$ diferenciable $`s+1`$ veces en $`E`$, $`a,x\in E`$, $`a\ne x`$, $`\Delta_{a,x}\subset E`$. Entonces
> ```math
> \Bigl\|f(x)-\sum_{k=0}^{s}\frac{d_a^kf(x-a)}{k!}\Bigr\|\le\frac{1}{(s+1)!}\sup_{c\in\hat\Delta_{a,x}}\bigl\|d_c^{s+1}f(x-a)\bigr\|.\qquad(6.5.2)
> ```

*Idea de la demostración.* Para el vector unitario $`e`$ con la dirección del lado izquierdo (bajo el signo de la [norma](14-several-variables.md#sec-14-1)), la función $`g=\langle f,e\rangle`$ es escalar; se le aplica el [teorema 6.5.2](#thm-6-5-2) y después la [desigualdad de Cauchy–Schwarz](21-lp-spaces.md#sec-21-4) $`|\langle v,e\rangle|\le\|v\|`$.

> <a id="thm-6-5-5"></a>**Teorema 6.5.5 (estimación del resto).** Sean el conjunto $`E`$ abierto en $`\mathbb R^n`$, $`s\in\mathbb Z_+`$, $`f\in C^{s+1}(E,\mathbb R^m)`$, $`a,x\in E`$, $`a\ne x`$, $`\Delta_{a,x}\subset E`$, y
> ```math
> M=\max_{|\alpha|=s+1}\ \sup_{c\in\hat\Delta_{a,x}}\bigl\|\partial^\alpha f(c)\bigr\|.
> ```
> Entonces $`M<+\infty`$ y el resto $`R_{a,s}f(x)=f(x)-T_{a,s}f(x)`$ cumple la desigualdad
> ```math
> \|R_{a,s}f(x)\|\le\frac{M}{(s+1)!}\bigl(\sqrt n\,\|x-a\|\bigr)^{s+1}.
> ```

La finitud de $`M`$ se deduce de la continuidad de las derivadas en el segmento [compacto](13-metric-spaces.md#sec-13-4); la estimación se obtiene de (6.5.2), ya que $`\|d_c^{s+1}f(h)\|\le M\bigl(|h_1|+\ldots+|h_n|\bigr)^{s+1}\le M(\sqrt n\,\|h\|)^{s+1}`$.

<a id="sec-6-6"></a>
## §6.6. Aplicaciones implícitas

Sean $`E\subset\mathbb R^{n+m}`$ abierto, $`f:E\to\mathbb R^m`$, y escribamos los puntos como $`(x,y)`$, $`x\in\mathbb R^n`$, $`y\in\mathbb R^m`$. Un sistema de $`m`$ ecuaciones
```math
f(x,y)=0\qquad(6.6.3)
```
define $`y`$ como función de $`x`$ solo localmente y bajo una condición de no degeneración. La aproximación lineal cerca de una solución $`(x^0,y^0)`$ es el sistema $`f'_x(x^0,y^0)h+f'_y(x^0,y^0)k=0`$, que tiene solución única respecto de $`k`$ cuando $`\det f'_y(x^0,y^0)\ne0`$.

> <a id="thm-6-6-1"></a>**Teorema 6.6.1 (de la aplicación implícita).** Sean el conjunto $`E`$ abierto en $`\mathbb R^{n+m}`$, $`(x^0,y^0)\in E`$, $`s\in\mathbb N`$, $`f\in C^s(E,\mathbb R^m)`$, $`f(x^0,y^0)=0`$ y $`\det f'_y(x^0,y^0)\ne0`$. Entonces existen un entorno $`V`$ del punto $`(x^0,y^0)`$, un [conjunto abierto](13-metric-spaces.md#sec-13-2) $`U\ni x^0`$ en $`\mathbb R^n`$ y una aplicación $`\psi\in C^s(U,\mathbb R^m)`$ tales que
> ```math
> \{(x,y)\in V:\ f(x,y)=0\}=\{(x,\psi(x)):\ x\in U\}.
> ```

> <a id="def-6-6-1"></a>**Definición 6.6.1.** La aplicación $`\psi`$ del [teorema 6.6.1](#thm-6-6-1) se llama aplicación implícita definida por la ecuación $`f(x,y)=0`$ en un entorno del punto $`(x^0,y^0)`$.

La derivada de la [aplicación implícita](#def-6-6-1) se halla derivando la identidad $`f(x,\psi(x))\equiv0`$: $`f'_x+f'_y\psi'=0`$, es decir,
```math
\psi'(x)=-\bigl[f'_y(x,\psi(x))\bigr]^{-1}f'_x(x,\psi(x)).
```
Ejemplo: la ecuación $`x^2+y^2=1`$ cerca de $`(0,1)`$ define $`\psi(x)=\sqrt{1-x^2}`$, $`\psi'(x)=-x/y`$; en los puntos $`(\pm1,0)`$, donde $`f'_y=2y=0`$, el teorema no es aplicable.

<a id="sec-6-7"></a>
## §6.7. Extremos de funciones de varias variables

> <a id="def-6-7-1"></a>**Definición 6.7.1.** Sean $`E\subset\mathbb R^n`$, $`a\in E`$, $`f:E\to\mathbb R`$. El punto $`a`$ se llama punto de mínimo (máximo) de $`f`$ si para algún entorno $`V`$ del punto $`a`$ se cumple $`f(x)\ge f(a)`$ (respectivamente $`f(x)\le f(a)`$) para todo $`x\in V\cap E`$; de mínimo (máximo) estricto si la desigualdad es estricta para $`x\ne a`$. Los puntos de mínimo y de máximo se llaman puntos de extremo.

> <a id="thm-6-7-1"></a>**Teorema 6.7.1 (condición necesaria de extremo).** Sean $`E\subset\mathbb R^n`$, $`a`$ un punto interior de $`E`$, y la función $`f:E\to\mathbb R`$ diferenciable en el punto $`a`$. Si $`a`$ es un punto de extremo de $`f`$, entonces $`d_af=0`$, es decir, $`\frac{\partial f}{\partial x_i}(a)=0`$ para todo $`i`$.

La demostración se reduce al [teorema de Fermat](06-derivatives.md#fermat-theorem) para $`t\mapsto f(a+th)`$. Los puntos con $`d_af=0`$ se llaman estacionarios.

> <a id="thm-6-7-2"></a>**Teorema 6.7.2 (condición suficiente de extremo).** Sean $`E\subset\mathbb R^n`$, $`a`$ un punto interior de $`E`$, $`f:E\to\mathbb R`$ dos veces diferenciable en el punto $`a`$ y $`d_af=0`$.
> 1. Si la forma cuadrática $`d_a^2f`$ es definida positiva, entonces $`a`$ es un punto de mínimo estricto.
> 2. Si $`d_a^2f`$ es definida negativa, entonces $`a`$ es un punto de máximo estricto.
> 3. Si $`d_a^2f`$ toma valores de ambos signos, entonces no hay extremo en $`a`$.

*Idea de la demostración.* Por el [teorema 6.5.1](#thm-6-5-1) $`f(a+h)-f(a)=\frac12d_a^2f(h)+o(\|h\|^2)`$, y por la compacidad de la esfera unidad una forma definida positiva cumple $`d_a^2f(h)\ge c\|h\|^2`$, $`c>0`$.

En el caso bidimensional, con $`A=f''_{xx}(a)`$, $`B=f''_{xy}(a)`$, $`C=f''_{yy}(a)`$: si $`AC-B^2>0`$, entonces con $`A>0`$ hay mínimo y con $`A<0`$ máximo; si $`AC-B^2<0`$, no hay extremo; si $`AC-B^2=0`$, hacen falta términos de orden superior.

> <a id="def-6-7-2"></a>**Definición 6.7.2.** Sean $`E\subset\mathbb R^n`$, $`a\in E`$, $`m<n`$, $`f,\varphi_1,\ldots,\varphi_m:E\to\mathbb R`$. Si $`a`$ es un punto de extremo de la restricción de $`f`$ al conjunto $`\{x\in E:\ \varphi_k(x)=\varphi_k(a),\ k=1,\ldots,m\}`$, entonces $`a`$ se llama punto de [extremo condicionado](16-implicit-functions-extrema.md#sec-16-4) (relativo) de $`f`$ sujeto a las ecuaciones de ligadura $`\varphi_k(x)=\varphi_k(a)`$.

En lo que sigue $`\Phi=(\varphi_1,\ldots,\varphi_m)`$, y las ligaduras se escriben como $`\Phi=0`$.

> <a id="thm-6-7-3"></a>**Teorema 6.7.3 (condición necesaria de extremo relativo).** Sean $`m<n`$, el conjunto $`E`$ abierto en $`\mathbb R^n`$, $`a\in E`$, $`f\in C^1(E)`$, $`\Phi\in C^1(E,\mathbb R^m)`$, $`\operatorname{rank}\Phi'(a)=m`$, y $`a`$ un punto de extremo condicionado de $`f`$ sujeto a las ligaduras $`\Phi=0`$. Entonces existen $`\lambda_1,\ldots,\lambda_m\in\mathbb R`$ (multiplicadores de Lagrange) tales que
> ```math
> \operatorname{grad}f(a)=\sum_{k=1}^{m}\lambda_k\operatorname{grad}\varphi_k(a).\qquad(6.7.1)
> ```

*Idea de la demostración.* Por el [teorema 6.6.1](#thm-6-6-1) las ligaduras se resuelven cerca de $`a`$ respecto de $`m`$ variables, la restricción de $`f`$ pasa a ser una función de $`n-m`$ variables libres, y se le aplica el [teorema 6.7.1](#thm-6-7-1).

> <a id="thm-6-7-4"></a>**Teorema 6.7.4.** En las condiciones del [teorema 6.7.3](#thm-6-7-3), para la función de Lagrange
> ```math
> L(x,\lambda)=f(x)-\sum_{k=1}^{m}\lambda_k\varphi_k(x)\qquad(x\in E,\ \lambda\in\mathbb R^m)
> ```
> existe $`\lambda\in\mathbb R^m`$ tal que $`\operatorname{grad}L(a,\lambda)=0`$ (el gradiente respecto de todas las $`n+m`$ variables).

El extremo condicionado se busca entre las soluciones del sistema $`\operatorname{grad}L=0`$: son $`n+m`$ ecuaciones con $`n+m`$ incógnitas.

> <a id="def-6-7-3"></a>**Definición 6.7.3.** Una forma cuadrática $`Q`$ en $`\mathbb R^n`$ se llama definida positiva (negativa) en un subespacio lineal $`N`$ si $`Q(h)>0`$ (respectivamente $`Q(h)<0`$) para todo $`h\in N\setminus\{0\}`$.

> <a id="thm-6-7-5"></a>**Teorema 6.7.5 (condición suficiente de extremo relativo).** Sean $`m<n`$, el conjunto $`E`$ abierto en $`\mathbb R^n`$, $`a\in E`$, $`f\in C^2(E)`$, $`\Phi\in C^2(E,\mathbb R^m)`$, $`\Phi(a)=0`$, $`\operatorname{rank}\Phi'(a)=m`$, $`\lambda`$ que cumple (6.7.1), $`L(x)=f(x)-\sum_k\lambda_k\varphi_k(x)`$ y $`N=\{h:\ d_a\Phi(h)=0\}`$.
> 1. Si $`d_a^2L`$ es definida positiva (negativa) en $`N`$, entonces $`a`$ es un punto de mínimo (máximo) condicionado.
> 2. Si $`d_a^2L`$ toma en $`N`$ valores de ambos signos, entonces no hay extremo condicionado en $`a`$.

## Ejemplo resuelto

**Extremo libre.** Para $`f(x,y)=x^3+y^3-3xy`$ los puntos estacionarios se hallan de $`3x^2-3y=0`$, $`3y^2-3x=0`$: son $`(0,0)`$ y $`(1,1)`$. En $`(0,0)`$: $`A=C=0`$, $`B=-3`$, $`AC-B^2=-9<0`$, luego no hay extremo. En $`(1,1)`$: $`A=C=6`$, $`B=-3`$, $`AC-B^2=27>0`$, $`A>0`$, mínimo estricto $`f(1,1)=-1`$.

**Extremo condicionado.** Para $`f=xy`$ con $`\varphi=x^2+y^2-2=0`$: $`L=xy-\lambda(x^2+y^2-2)`$, la condición (6.7.1) da $`y=2\lambda x`$, $`x=2\lambda y`$, de donde $`\lambda=\pm\frac12`$. Para $`\lambda=\frac12`$ se obtienen los puntos $`\pm(1,1)`$; aquí $`N=\{h:\ h_1+h_2=0\}`$ y $`d^2L(h)=2h_1h_2-(h_1^2+h_2^2)=-4h_1^2<0`$ en $`N\setminus\{0\}`$, máximo condicionado $`1`$. Para $`\lambda=-\frac12`$ se obtienen los puntos $`\pm(1,-1)`$, $`d^2L=4h_1^2>0`$ en $`N`$, mínimo condicionado $`-1`$.

## Errores frecuentes

1. Confundir el resto de Peano $`o(\|h\|^s)`$ (basta la diferenciabilidad $`s`$ veces en el punto) con la estimación $`O(\|h\|^{s+1})`$, que exige más regularidad.
2. Escribir el teorema del valor medio para una aplicación como igualdad: para aplicaciones con valores en $`\mathbb R^m`$ solo vale la estimación (6.5.2).
3. Aplicar el [teorema 6.6.1](#thm-6-6-1) sin comprobar $`\det f'_y(x^0,y^0)\ne0`$, o tomar su conclusión como global.
4. Sacar conclusiones sobre un extremo cuando la forma $`d_a^2f`$ es solo semidefinida (compárense $`x^2+y^4`$ y $`x^2-y^4`$).
5. En un extremo condicionado, comprobar el signo de $`d_a^2L`$ en todo $`\mathbb R^n`$ en lugar de en el subespacio $`N`$ (la condición «en todo el espacio» es suficiente, pero a menudo no se cumple).

## Ejercicios

1. Escriba $`T_{0,2}f`$ para $`f(x,y)=e^x\cos y`$.
2. La ecuación $`e^y+y+x^2=1`$ define cerca de $`(0,0)`$ una función $`y(x)`$. Halle $`y'(0)`$ y $`y''(0)`$.
3. Estudie los extremos de $`f(x,y)=x^2+xy+y^2-3x`$.
4. Halle los valores máximo y mínimo de $`f=x+2y+2z`$ en la esfera $`x^2+y^2+z^2=9`$.

<details>
<summary>Respuestas breves</summary>

1. $`1+x+\frac{x^2-y^2}{2}`$.
2. $`y'=-\frac{2x}{e^y+1}`$, $`y'(0)=0`$; $`y''(0)=-1`$.
3. Punto estacionario $`(2,-1)`$: $`A=C=2`$, $`B=1`$, $`AC-B^2=3>0`$, $`A>0`$, mínimo $`f(2,-1)=-3`$.
4. $`\operatorname{grad}f=2\lambda(x,y,z)`$ da $`\pm(1,2,2)`$: máximo $`9`$, mínimo $`-9`$.
</details>

---

[← 21. Espacios Lᵖ y modos de convergencia](21-lp-spaces.md) · [Índice](index.md) · [Términos y teoremas](term-index.md) · [23. Series numéricas →](23-numerical-series.md)
