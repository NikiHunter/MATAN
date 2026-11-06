---
title: "La integral múltiple de Riemann"
lang: es
chapter: 26
part: "Semestre 3: capítulos del profesor"
numbering: lecture
lecturer_chapter: 10
---
# 26. La integral múltiple de Riemann

[← 25. Integrales dependientes de un parámetro](25-parameter-integrals.md) · [Índice](index.md) · [Términos y teoremas](term-index.md)

> **Objetivo.** Exponer el capítulo 10 del profesor (§10.1–§10.4, [clases 79–80](lectures-2025-26/lecture-79-80.md), [81–82](lectures-2025-26/lecture-81-82.md) y [83–84](lectures-2025-26/lecture-83-84.md)) conservando la numeración del profesor: la [integral de Riemann](08-riemann-integration.md#sec-8-2) sobre un intervalo $`n`$-dimensional, los criterios de Lebesgue y de Darboux, la [integral sobre un conjunto admisible](#def-10-2-4) y la [medida de Jordan](#def-10-2-5), propiedades de la integral, el [teorema de Fubini](17-multiple-integrals.md#fubini-theorem-continuous) y el [principio de Cavalieri](#thm-10-4-2). Una exposición condensada está en el [capítulo 17](17-multiple-integrals.md); la medida y la [integral de Lebesgue](20-lebesgue-integration.md#sec-20-1), en los capítulos [19](19-measure-theory.md) y [20](20-lebesgue-integration.md).

<a id="sec-10-1"></a>
## §10.1. La integral de Riemann sobre un intervalo n-dimensional

> <a id="def-10-1-1"></a>**Definición 10.1.1.** El conjunto
> ```math
> I=I_{a,b}=\{x\in\mathbb R^n:\ a_i\le x_i\le b_i,\ i=1,\ldots,n\},\qquad a=(a_1,\ldots,a_n),\ b=(b_1,\ldots,b_n)\in\mathbb R^n,\ a_i\le b_i ,
> ```
> se llama intervalo (o paralelepípedo, caja) en $`\mathbb R^n`$.

> <a id="def-10-1-2"></a>**Definición 10.1.2.** Al intervalo $`I=I_{a,b}`$ se le asocia el número
> ```math
> \mu(I):=\prod_{i=1}^n(b_i-a_i),
> ```
> llamado medida del intervalo.

Dividamos cada segmento $`[a_i,b_i]`$ mediante puntos en segmentos más pequeños; los productos de estos segmentos son intervalos $`I_1,\ldots,I_k`$ cuya unión es $`I`$ y que se cortan dos a dos solo por caras, de modo que $`\mu(I)=\sum_j\mu(I_j)`$.

> <a id="def-10-1-3"></a>**Definición 10.1.3.** Una representación del intervalo $`I`$ como unión $`I=\bigcup_{j=1}^kI_j`$ de intervalos más pequeños $`I_j`$ se llama partición del intervalo $`I`$ y se denota $`P`$.

La finura (diámetro) de la [partición](#def-10-1-3) es $`\lambda(P)=\max_jd(I_j)`$, donde $`d(I_j)`$ es el diámetro (la longitud de la diagonal principal) del intervalo $`I_j`$.

> <a id="def-10-1-4"></a>**Definición 10.1.4.** Si en cada intervalo $`I_j`$ de una partición $`P`$ se fija un punto $`\xi_j\in I_j`$, se dice que se tiene una partición con puntos marcados (partición etiquetada).

> <a id="def-10-1-5"></a>**Definición 10.1.5.** La suma
> ```math
> \sigma(f,P,\xi):=\sum_{i=1}^kf(\xi_i)\,\mu(I_i)
> ```
> se llama suma integral (de Riemann) de la función $`f`$ correspondiente a la partición del intervalo $`I`$ con puntos marcados $`\xi`$.

> <a id="def-10-1-6"></a>**Definición 10.1.6.** La magnitud
> ```math
> \int_If(x)\,dx:=\lim_{\lambda(P)\to0}\sigma(f,P,\xi)=\lim_{\lambda(P)\to0}\sum_{i=1}^kf(\xi_i)\,\mu(I_i),
> ```
> si el límite existe, se llama integral (de Riemann) de la función $`f`$ sobre el intervalo $`I\subset\mathbb R^n`$.

El límite se entiende así: para todo $`\varepsilon>0`$ existe $`\delta>0`$ tal que $`|\sigma(f,P,\xi)-J|<\varepsilon`$ para todas las particiones con $`\lambda(P)<\delta`$ y cualquier elección de puntos marcados.

> <a id="def-10-1-7"></a>**Definición 10.1.7.** Si para una función $`f:I\to\mathbb R`$ existe el límite finito de la [definición 10.1.6](#def-10-1-6), entonces $`f`$ se llama integrable (en el sentido de Riemann) en el intervalo $`I`$. El conjunto de todas esas funciones se denota $`R(I)`$.

> <a id="thm-10-1-1"></a>**Teorema 10.1.1 (condición necesaria de integrabilidad).** Si $`f\in R(I)`$, entonces $`f`$ está acotada en $`I`$.

Si $`f`$ no está acotada en uno de los intervalos $`I_{i_0}`$ de la partición (con $`\mu(I_{i_0})>0`$), moviendo el punto $`\xi_{i_0}`$ la suma integral puede hacerse arbitrariamente grande.

Un conjunto $`E\subset\mathbb R^n`$ tiene medida (de Lebesgue) nula si para todo $`\varepsilon>0`$ puede cubrirse con una familia finita o [numerable](01-logic-sets-functions.md#sec-1-5) de intervalos de medida total menor que $`\varepsilon`$. Los puntos, las curvas suaves en $`\mathbb R^2`$ y las superficies suaves en $`\mathbb R^3`$ tienen medida nula; la unión numerable y los subconjuntos de conjuntos de medida nula tienen medida nula; un intervalo no degenerado no tiene medida nula.

> <a id="def-10-1-8"></a>**Definición 10.1.8.** Una propiedad se cumple [casi en todas partes](19-measure-theory.md#sec-19-4) en un conjunto $`M`$ si el subconjunto de $`M`$ donde puede fallar tiene medida nula.

> <a id="thm-10-1-2"></a>**Teorema 10.1.2 (criterio de Lebesgue).** Una función $`f:I\to\mathbb R`$ es integrable en el sentido de Riemann en el intervalo $`I`$ si y solo si $`f`$ está acotada en $`I`$ y es continua casi en todas partes en $`I`$.

Para una $`f`$ acotada y una partición $`P`$ pongamos $`m_i=\inf_{I_i}f`$, $`M_i=\sup_{I_i}f`$.

> <a id="def-10-1-9"></a>**Definición 10.1.9.** Las magnitudes
> ```math
> s(f,P)=\sum_im_i\,\mu(I_i),\qquad S(f,P)=\sum_iM_i\,\mu(I_i)
> ```
> se llaman suma inferior y suma superior (de Darboux) de la función $`f`$ en el intervalo $`I`$, correspondientes a la partición $`P`$.

> <a id="def-10-1-10"></a>**Definición 10.1.10.** La integral inferior y la superior (de Darboux) de una función $`f:I\to\mathbb R`$ en el intervalo $`I`$ son las magnitudes
> ```math
> \underline J=\sup_Ps(f,P),\qquad\overline J=\inf_PS(f,P),
> ```
> donde el [supremo](02-real-numbers.md#sec-2-2) y el ínfimo se toman sobre todas las particiones $`P`$ del intervalo $`I`$.

> <a id="thm-10-1-3"></a>**Teorema 10.1.3 (criterio de Darboux).** Una función $`f:I\to\mathbb R`$ es integrable en el intervalo $`I`$ si y solo si $`f`$ está acotada en $`I`$ y $`\underline J=\overline J`$.

Como en el caso unidimensional, $`s(f,P)\le\sigma(f,P,\xi)\le S(f,P)`$; al refinar la partición las sumas inferiores no decrecen y las superiores no crecen, y siempre $`\underline J\le\overline J`$.

<a id="sec-10-2"></a>
## §10.2. La integral sobre un conjunto

> <a id="def-10-2-1"></a>**Definición 10.2.1.** Un conjunto $`\Omega\subset\mathbb R^n`$ se llama admisible si está acotado en $`\mathbb R^n`$ y su frontera $`\partial\Omega`$ es un conjunto de medida nula.

> <a id="def-10-2-2"></a>**Definición 10.2.2.** Sea $`\Omega\subset\mathbb R^n`$ un [conjunto admisible](#def-10-2-1). La función
> ```math
> \chi_\Omega(x)=\begin{cases}1, & x\in\Omega,\\ 0, & x\notin\Omega\end{cases}
> ```
> se llama función característica del conjunto $`\Omega`$.

> <a id="def-10-2-3"></a>**Definición 10.2.3.** Sea una función $`f`$ definida en un conjunto $`\Omega`$. Entonces
> ```math
> f\chi_\Omega(x)=\begin{cases}f(x), & x\in\Omega,\\ 0, & x\notin\Omega\end{cases}
> ```
> (aunque $`f`$ no está definida fuera de $`\Omega`$).

> <a id="def-10-2-4"></a>**Definición 10.2.4.** La integral de una función $`f`$ sobre un conjunto acotado $`\Omega`$ se define mediante
> ```math
> \int_\Omega f(x)\,dx:=\int_{I\supset\Omega}f\chi_\Omega(x)\,dx,
> ```
> donde $`I`$ es un intervalo arbitrario que contiene a $`\Omega`$; la integral de la izquierda existe si existe la de la derecha. El conjunto de funciones integrables en $`\Omega`$ se denota $`R(\Omega)`$.

El valor no depende de la elección del intervalo $`I\supset\Omega`$: fuera de $`\Omega`$ el integrando es nulo.

> <a id="def-10-2-5"></a>**Definición 10.2.5.** La medida (de Jordan), o volumen, de un conjunto acotado $`\Omega\subset\mathbb R^n`$ es la magnitud
> ```math
> \mu(\Omega):=\int_\Omega1\,dx=\int_I\chi_\Omega(x)\,dx\qquad(I\supset\Omega),
> ```
> si esta integral (de Riemann) existe.

> <a id="def-10-2-6"></a>**Definición 10.2.6.** Un conjunto $`\Omega\subset\mathbb R^n`$ se llama conjunto de medida nula en el sentido de Jordan, o conjunto de volumen nulo, si para todo $`\varepsilon>0`$ puede cubrirse con un sistema finito de intervalos $`I_1,\dots,I_k`$ tal que
> ```math
> \sum_{i=1}^k\mu(I_i)<\varepsilon .
> ```

La función $`\chi_\Omega`$ es discontinua exactamente en los puntos de $`\partial\Omega`$, por lo que, por el criterio de Lebesgue, un conjunto acotado tiene medida de Jordan si y solo si es admisible. Un [compacto](13-metric-spaces.md#sec-13-4) de [medida de Lebesgue](19-measure-theory.md#sec-19-3) nula tiene también medida de Jordan nula (de un recubrimiento numerable por intervalos abiertos se extrae uno finito), pero, por ejemplo, $`\mathbb Q\cap[0,1]`$ tiene medida de Lebesgue nula y no tiene medida de Jordan: su frontera es todo el segmento $`[0,1]`$.

> <a id="thm-10-2-1"></a>**Teorema 10.2.1.** Una función $`f:\Omega\to\mathbb R`$ es integrable en un conjunto admisible $`\Omega`$ si y solo si está acotada y es continua en casi todos los puntos del conjunto $`\Omega`$.

En efecto, las discontinuidades de $`f\chi_\Omega`$ están en la unión del conjunto de discontinuidades de $`f`$ en $`\Omega`$ y de la frontera $`\partial\Omega`$, y esta última tiene medida nula.

<a id="sec-10-3"></a>
## §10.3. Propiedades generales de la integral

La integral sobre un conjunto admisible es lineal. Sean $`\Omega`$ admisible y $`f,g\in R(\Omega)`$. Entonces:

1. si $`f\ge0`$ en $`\Omega`$, entonces $`\int_\Omega f\,dx\ge0`$;
2. si $`f\le g`$ en $`\Omega`$, entonces $`\int_\Omega f\,dx\le\int_\Omega g\,dx`$;
3. si $`m\le f\le M`$ en $`\Omega`$, entonces $`m\,\mu(\Omega)\le\int_\Omega f\,dx\le M\,\mu(\Omega)`$;
4. para $`m=\inf_\Omega f`$, $`M=\sup_\Omega f`$ existe $`\theta\in[m,M]`$ tal que $`\int_\Omega f\,dx=\theta\,\mu(\Omega)`$;
5. si $`\Omega`$ es [conexo](13-metric-spaces.md#sec-13-5) y $`f`$ es continua, entonces $`\int_\Omega f\,dx=f(\xi)\,\mu(\Omega)`$ para algún punto $`\xi\in\Omega`$ (teorema del valor medio);
6. si $`m\le f\le M`$ y $`g\ge0`$ en $`\Omega`$, entonces $`m\int_\Omega g\,dx\le\int_\Omega fg\,dx\le M\int_\Omega g\,dx`$.

> <a id="thm-10-3-1"></a>**Teorema 10.3.1.** Sean $`\Omega_1`$, $`\Omega_2`$ conjuntos admisibles en $`\mathbb R^n`$, y $`f`$ una función definida en $`\Omega_1\cup\Omega_2`$. Entonces:
>
> ① la existencia de las integrales se relaciona así:
> ```math
> \exists\int_{\Omega_1\cup\Omega_2}f(x)\,dx\iff\exists\int_{\Omega_i}f(x)\,dx\ \ (i=1,2)\implies\exists\int_{\Omega_1\cap\Omega_2}f(x)\,dx;
> ```
>
> ② si $`\mu(\Omega_1\cap\Omega_2)=0`$, entonces, siempre que existan las integrales,
> ```math
> \int_{\Omega_1\cup\Omega_2}f(x)\,dx=\int_{\Omega_1}f(x)\,dx+\int_{\Omega_2}f(x)\,dx .
> ```

El punto ① se deduce del criterio de Lebesgue; el punto ②, de la identidad $`\chi_{\Omega_1\cup\Omega_2}=\chi_{\Omega_1}+\chi_{\Omega_2}-\chi_{\Omega_1\cap\Omega_2}`$ y de que la integral sobre un conjunto de medida nula es cero.

> <a id="prop-10-3-1"></a>**Proposición 10.3.1.** Si $`f\in R(\Omega)`$, entonces $`|f|\in R(\Omega)`$ y
> ```math
> \Bigl|\int_\Omega f(x)\,dx\Bigr|\le\int_\Omega|f(x)|\,dx .
> ```

La función $`|f|`$ está acotada y es continua allí donde lo es $`f`$; la desigualdad se deduce de la propiedad 2 aplicada a $`-|f|\le f\le|f|`$.

<a id="sec-10-4"></a>
## §10.4. El teorema de Fubini

> <a id="thm-10-4-1"></a>**Teorema 10.4.1 (Fubini).** Sean $`I=I_x\times I_y\subset\mathbb R^n`$, donde $`I_x`$ es un intervalo en $`\mathbb R^m`$, $`I_y`$ es un intervalo en $`\mathbb R^k`$, $`m+k=n`$. Si la función $`f`$ es integrable en $`I`$ y, además,
>
> $`(\ast)`$ para cada $`x\in I_x`$ la función $`y\mapsto f(x,y)`$ es integrable en $`I_y`$,
>
> entonces la función $`F(x)=\int_{I_y}f(x,y)\,dy`$ es integrable en $`I_x`$ y
> ```math
> \int_If(x,y)\,dx\,dy=\int_{I_x}\Bigl(\int_{I_y}f(x,y)\,dy\Bigr)dx .
> ```

*Idea de la demostración.* Para una partición $`P=P_x\times P_y`$ se cumple $`s(f,P)\le s(F,P_x)\le S(F,P_x)\le S(f,P)`$, donde en el medio están las [sumas de Darboux](08-riemann-integration.md#sec-8-1) de la función $`F`$; las sumas extremas convergen a $`\int_If`$, y el [criterio de Darboux](08-riemann-integration.md#integrability-criterion) concluye la demostración.

> <a id="cor-10-4-1"></a>**Corolario 10.4.1.** Sean $`I=I_1\times\dots\times I_n\subset\mathbb R^n`$, $`I_i=[a_i,b_i]`$, la función $`f`$ integrable en $`I`$, y supongamos que la condición $`(\ast)`$ se cumple en cada paso (por ejemplo, si $`f`$ es continua en $`I`$). Entonces
> ```math
> \int_If(x)\,dx=\int_{a_n}^{b_n}dx_n\int_{a_{n-1}}^{b_{n-1}}dx_{n-1}\dots\int_{a_1}^{b_1}f(x_1,x_2,\dots,x_n)\,dx_1 .
> ```

> <a id="cor-10-4-2"></a>**Corolario 10.4.2.** Sean $`D\subset\mathbb R^{n-1}`$ un conjunto admisible, las funciones $`\varphi_1,\varphi_2`$ continuas en $`\overline D`$ con $`\varphi_1\le\varphi_2`$ en $`\overline D`$, y
> ```math
> E=\{(x,y)\in\mathbb R^n:\ x\in D,\ \varphi_1(x)\le y\le\varphi_2(x)\}.
> ```
> Si $`f\in R(E)`$ y para cada $`x\in D`$ existe la integral $`\int_{\varphi_1(x)}^{\varphi_2(x)}f(x,y)\,dy`$, entonces
> ```math
> \int_Ef(x,y)\,dx\,dy=\int_Ddx\int_{\varphi_1(x)}^{\varphi_2(x)}f(x,y)\,dy .
> ```

> <a id="cor-10-4-3"></a>**Corolario 10.4.3.** En las condiciones del [corolario 10.4.2](#cor-10-4-2) el conjunto $`E`$ es admisible, y su volumen es
> ```math
> \mu(E)=\int_D\bigl(\varphi_2(x)-\varphi_1(x)\bigr)\,dx .
> ```

> <a id="thm-10-4-2"></a>**Teorema 10.4.2 (principio de Cavalieri).** Sean $`A`$ y $`B`$ dos cuerpos en $`\mathbb R^3`$ que tienen volumen (medibles en el sentido de Jordan), y $`A_c`$ y $`B_c`$ sus secciones por el plano $`z=c`$. Si para cada $`c\in\mathbb R`$ las secciones $`A_c`$, $`B_c`$ son medibles y tienen la misma área, entonces los cuerpos $`A`$ y $`B`$ tienen el mismo volumen.

Por el teorema de Fubini $`\mu(A)=\int\mu(A_c)\,dc`$, y lo mismo para $`B`$.

## Ejemplo resuelto

**Una integral sobre una región curvilínea.** Sea $`E=\{(x,y):\ 0\le x\le1,\ x^2\le y\le x\}`$. Por el [corolario 10.4.2](#cor-10-4-2) con $`D=[0,1]`$, $`\varphi_1=x^2`$, $`\varphi_2=x`$:
```math
\iint_Exy\,dx\,dy=\int_0^1x\,dx\int_{x^2}^{x}y\,dy=\int_0^1\frac{x^3-x^5}{2}\,dx=\frac12\Bigl(\frac14-\frac16\Bigr)=\frac1{24}.
```

**El volumen de la bola.** La sección de la bola unidad $`B\subset\mathbb R^3`$ por el plano $`z=c`$, $`|c|\le1`$, es un disco de radio $`\sqrt{1-c^2}`$ y área $`\pi(1-c^2)`$. Por el teorema de Fubini (como en el principio de Cavalieri)
```math
\mu(B)=\int_{-1}^{1}\pi(1-c^2)\,dc=\pi\Bigl(2-\frac23\Bigr)=\frac{4\pi}{3}.
```

## Errores frecuentes

1. Confundir la medida nula de Lebesgue (recubrimientos numerables) con la medida de Jordan nula (recubrimientos finitos): $`\mathbb Q\cap[0,1]`$ tiene la primera pero no la segunda.
2. Creer que todo conjunto acotado tiene volumen: un conjunto con frontera no admisible (por ejemplo, $`\mathbb Q^2\cap[0,1]^2`$) no tiene medida de Jordan.
3. Aplicar el teorema de Fubini sin comprobar la condición $`(\ast)`$: la función igual a $`1`$ para $`x=\frac12`$, $`y\in\mathbb Q`$ y a $`0`$ en los demás puntos de $`[0,1]^2`$ es integrable (sus discontinuidades están en un segmento), pero para $`x=\frac12`$ la integral interior en $`y`$ no existe.
4. Poner mal los límites al cambiar el orden de integración: hay que describir de nuevo la región como «trapecio curvilíneo» respecto de la otra variable.
5. Sumar integrales sobre conjuntos que se solapan: la igualdad ② del [teorema 10.3.1](#thm-10-3-1) exige $`\mu(\Omega_1\cap\Omega_2)=0`$.

## Ejercicios

1. Calcule $`\iint_{[0,1]\times[0,2]}(x+y^2)\,dx\,dy`$.
2. Cambie el orden de integración en $`\int_0^1dx\int_x^1f(x,y)\,dy`$.
3. Halle el volumen del tetraedro $`\{x,y,z\ge0,\ x+y+z\le1\}`$.
4. ¿Tiene medida de Jordan el conjunto $`\{(x,y)\in[0,1]^2:\ x\in\mathbb Q\}`$?

<details>
<summary>Respuestas breves</summary>

1. $`\int_0^2\bigl(\frac12+y^2\bigr)dy=1+\frac83=\frac{11}3`$.
2. $`\int_0^1dy\int_0^yf(x,y)\,dx`$.
3. Por el [corolario 10.4.3](#cor-10-4-3) con $`D=\{x,y\ge0,\ x+y\le1\}`$, $`\varphi_1=0`$, $`\varphi_2=1-x-y`$: $`\int_0^1\frac{(1-x)^2}{2}\,dx=\frac16`$.
4. No: su frontera es todo el cuadrado $`[0,1]^2`$, que no es un conjunto de medida nula, es decir, el conjunto no es admisible.
</details>

---

[← 25. Integrales dependientes de un parámetro](25-parameter-integrals.md) · [Índice](index.md) · [Términos y teoremas](term-index.md)
