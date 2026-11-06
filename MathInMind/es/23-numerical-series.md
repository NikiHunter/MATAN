---
title: "Series numéricas"
lang: es
chapter: 23
part: "Semestre 3: capítulos del profesor"
numbering: lecture
lecturer_chapter: 7
---
# 23. Series numéricas

[← 22. Fórmula de Taylor en ℝⁿ, aplicaciones implícitas, extremos](22-taylor-implicit-extrema.md) · [Índice](index.md) · [Términos y teoremas](term-index.md) · [24. Series funcionales y de potencias →](24-functional-power-series.md)

> **Objetivo.** Exponer el capítulo 7 del profesor (§7.1–§7.5, [clases 67–68](lectures-2025-26/lecture-67-68.md), [69–70](lectures-2025-26/lecture-69-70.md) y el comienzo de [71–72](lectures-2025-26/lecture-71-72.md)) conservando la numeración del profesor: la convergencia de una serie y sus propiedades, el [criterio de Bolzano–Cauchy](03-sequences.md#sec-3-4), los criterios de convergencia de series positivas, los criterios de Leibniz, Dirichlet y Abel, las [reordenaciones](04-numeric-series.md#rearrangement-warning) de series. El profesor no numera los criterios de convergencia, por eso aquí se citan por su nombre. Una exposición condensada de los mismos temas está en el [capítulo 4](04-numeric-series.md).

<a id="sec-7-1"></a>
## §7.1. Series numéricas

> <a id="def-7-1-1"></a>**Definición 7.1.1.** Sea dada una sucesión $`(a_n)`$, $`a_n\in\mathbb R`$, $`n\in\mathbb N`$. Entonces $`S_n=a_1+a_2+\ldots+a_n`$ se llama [suma parcial](04-numeric-series.md#sec-4-1) de la serie, $`S=\lim_{n\to\infty}S_n`$, suma de la serie; para la suma se usa la notación $`S:=\sum_{n=1}^{\infty}a_n`$; $`a_n`$ se llama término general de la serie.

> <a id="def-7-1-2"></a>**Definición 7.1.2.** La serie $`\sum_{n=1}^{\infty}a_n`$ converge si la suma de la serie $`S`$ existe y es finita. En caso contrario la serie diverge.

Así, una serie es la sucesión de sus sumas parciales, y su convergencia es la convergencia de esa sucesión. Ejemplos: la serie $`\sum_{k=1}^{\infty}1`$ diverge ($`S_n=n\to+\infty`$); la serie $`\sum_{k=0}^{\infty}(-1)^k`$ diverge (sus sumas parciales valen alternadamente $`1`$ y $`0`$); la serie de término general $`\frac{1}{k(k+1)}=\frac1k-\frac{1}{k+1}`$ converge, ya que
```math
S_n=\sum_{k=1}^{n}\Bigl(\frac1k-\frac1{k+1}\Bigr)=1-\frac{1}{n+1}\to1 .
```
La serie geométrica $`\sum_{k=0}^{\infty}q^k`$ converge para $`|q|<1`$ a $`\frac{1}{1-q}`$ y diverge para $`|q|\ge1`$.

<a id="sec-7-2"></a>
## §7.2. Propiedades de las series

*Propiedad 1 (condición necesaria de convergencia).* Si la serie $`\sum_{n=1}^{\infty}a_n`$ converge, entonces $`a_n\to0`$: en efecto, $`a_n=S_n-S_{n-1}\to S-S=0`$. El recíproco es falso: la serie armónica $`\sum_{k=1}^{\infty}\frac1k`$ diverge aunque $`\frac1k\to0`$; agrupar los términos de la suma parcial $`S_{2^m}`$ en bloques de longitud $`2^{j-1}`$ da $`S_{2^m}\ge1+\frac m2`$.

*Propiedad 2.* Una serie converge si y solo si converge cualquiera (o al menos uno) de sus restos $`\sum_{n=k+1}^{\infty}a_n`$; además, el resto de una serie convergente tiende a cero cuando $`k\to\infty`$. Suprimir o añadir un número finito de términos no afecta a la convergencia.

*Propiedades 3 y 4 (linealidad).* Para $`k\ne0`$ las series $`\sum a_n`$ y $`\sum ka_n`$ convergen o divergen a la vez, y $`\sum ka_n=k\sum a_n`$; si las series $`\sum a_n`$ y $`\sum b_n`$ convergen, entonces la serie $`\sum(a_n+b_n)`$ converge y su suma es $`\sum a_n+\sum b_n`$. La suma de una serie convergente y una divergente diverge.

> **Criterio de Bolzano–Cauchy.** La serie $`\sum_{n=1}^{\infty}a_n`$ converge si y solo si
> ```math
> \forall\varepsilon>0\ \exists N\in\mathbb N\ \forall n>N\ \forall p\in\mathbb N\qquad\Bigl|\sum_{k=n+1}^{n+p}a_k\Bigr|<\varepsilon .
> ```

Es el criterio de Cauchy para la sucesión $`(S_n)`$, ya que $`S_{n+p}-S_n=a_{n+1}+\ldots+a_{n+p}`$. De aquí un método para probar la divergencia: hallar índices $`m_n>n`$ (a menudo $`m_n=2n`$) con $`\sum_{k=n}^{m_n}a_k\not\to0`$. Para la serie armónica $`\sum_{k=n}^{2n}\frac1k\ge\frac{n+1}{2n}>\frac12`$.

> <a id="def-7-2-1"></a>**Definición 7.2.1.** La serie $`\sum_{n=1}^{\infty}a_n`$ se llama [absolutamente convergente](04-numeric-series.md#sec-4-3) si la serie $`\sum_{n=1}^{\infty}|a_n|`$ converge.

Una serie absolutamente convergente converge: por la desigualdad triangular $`|a_{n+1}+\ldots+a_{n+p}|\le|a_{n+1}|+\ldots+|a_{n+p}|`$, y la condición del criterio de Bolzano–Cauchy para $`\sum|a_n|`$ implica la misma para $`\sum a_n`$.

<a id="sec-7-3"></a>
## §7.3. Series positivas

> <a id="def-7-3-1"></a>**Definición 7.3.1.** La serie $`\sum_{n=1}^{\infty}a_n`$ se llama positiva si $`a_n\ge0`$ para todo $`n`$.

Las sumas parciales de una serie positiva no decrecen, por lo que una serie positiva siempre tiene suma (finita o $`+\infty`$), y converge si y solo si la sucesión $`(S_N)`$ está acotada (basta que lo esté alguna subsucesión $`(S_{N_k})`$).

> **Primer criterio de comparación.** Sea $`0\le a_n\le b_n`$ para todo $`n`$. Si la serie $`\sum b_n`$ converge, también converge la serie $`\sum a_n`$; si la serie $`\sum a_n`$ diverge, también diverge la serie $`\sum b_n`$.

> **Segundo criterio de comparación.** Sean $`a_n\ge0`$, $`b_n>0`$ y supongamos que existe $`\lim_{n\to\infty}\frac{a_n}{b_n}=:L\in[0,+\infty]`$. Si $`L<+\infty`$, la convergencia de $`\sum b_n`$ implica la de $`\sum a_n`$; si $`L>0`$, la convergencia de $`\sum a_n`$ implica la de $`\sum b_n`$. Para $`L\in(0,+\infty)`$ las series convergen o divergen a la vez.

> **Criterio de d'Alembert.** Sea $`a_n>0`$ y supongamos que existe $`\lim_{n\to\infty}\frac{a_{n+1}}{a_n}=:D`$. Si $`D<1`$, la serie converge; si $`D>1`$, la serie diverge; para $`D=1`$ (o si no hay límite) el criterio no decide.

> **Criterio de Cauchy.** Sea $`a_n>0`$ y supongamos que existe $`\lim_{n\to\infty}\sqrt[n]{a_n}=:C`$. Si $`C<1`$, la serie converge; si $`C>1`$, la serie diverge; para $`C=1`$ (o si no hay límite) el criterio no decide.

En ambos criterios, cuando el valor es menor que uno, la serie se compara con una progresión geométrica de razón $`q=\frac{1+D}{2}`$ (respectivamente $`q=\frac{1+C}{2}`$); cuando es mayor que uno, falla la condición necesaria $`a_n\to0`$. Las series $`\sum\frac1n`$ y $`\sum\frac1{n^2}`$ muestran que con el valor $`1`$ son posibles ambos resultados.

> **Lema de Cauchy (de condensación).** Sea $`a_n\ge a_{n+1}\ge0`$ para todo $`n`$. Entonces la serie $`\sum_{n=1}^{\infty}a_n`$ converge si y solo si converge la serie $`\sum_{n=1}^{\infty}2^na_{2^n}`$.

*Idea de la demostración.* El bloque de índices $`2^{k-1}+1,\ldots,2^k`$ contiene exactamente $`2^{k-1}`$ términos, cada uno comprendido entre $`a_{2^k}`$ y $`a_{2^{k-1}}`$; sumando por bloques se obtiene $`\frac12T_m\le S_{2^m}`$ y $`S_{2^{m+1}-1}\le a_1+T_m`$, donde $`T_m=\sum_{k=1}^{m}2^ka_{2^k}`$.

Para $`a_n=\frac1{n^p}`$, $`p>0`$, la serie condensada es una progresión geométrica de razón $`2^{1-p}`$, por lo que
```math
\sum_{n=1}^{\infty}\frac{1}{n^p}\quad\text{converge para } p>1\text{ y diverge para } p\le1 .
```

<a id="sec-7-4"></a>
## §7.4. Series de términos de signo arbitrario

> <a id="def-7-4-1"></a>**Definición 7.4.1.** Si la serie $`\sum_{n=1}^{\infty}a_n`$ converge y la serie correspondiente $`\sum_{n=1}^{\infty}|a_n|`$ diverge, la serie original $`\sum_{n=1}^{\infty}a_n`$ se llama condicionalmente convergente.

> **Criterio de Leibniz.** Sean $`c_n>0`$, $`c_{n+1}\le c_n`$ para todo $`n`$ y $`c_n\to0`$. Entonces la serie alternada $`\sum_{n=0}^{\infty}(-1)^nc_n`$ converge, y su resto $`R_n=\sum_{k=n+1}^{\infty}(-1)^kc_k`$ cumple la estimación $`|R_n|\le c_{n+1}`$.

*Idea de la demostración.* Las sumas parciales impares $`S_{2m+1}`$ no decrecen y están entre $`0`$ y $`c_0`$, luego tienen límite $`S`$; las pares difieren de ellas en $`c_{2m+2}\to0`$. Por ejemplo, $`\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{k}=\ln2`$: $`S_{2n}=H_{2n}-H_n`$, donde $`H_n=1+\frac12+\ldots+\frac1n=\ln n+\gamma+o(1)`$.

> **Transformación de Abel.** Sean $`(a_k)`$, $`(b_k)`$ sucesiones numéricas, $`B_k=b_1+\ldots+b_k`$, $`B_0:=0`$. Entonces para $`m>n\ge0`$
> ```math
> \sum_{k=n+1}^{m}a_kb_k=a_mB_m-a_{n+1}B_n+\sum_{k=n+1}^{m-1}(a_k-a_{k+1})B_k .
> ```

Es un análogo discreto de la [integración por partes](08-riemann-integration.md#sec-8-4): sustituya $`b_k=B_k-B_{k-1}`$ y reagrupe.

> **Criterio de Dirichlet.** Sea $`a_n\downarrow0`$ (es decir, $`a_{n+1}\le a_n`$ y $`a_n\to0`$) y supongamos que las sumas parciales $`B_n=b_1+\ldots+b_n`$ están acotadas: $`|B_n|\le M`$ para todo $`n`$. Entonces la serie $`\sum_{n=1}^{\infty}a_nb_n`$ converge.

Por la transformación de Abel $`\bigl|\sum_{k=n+1}^{m}a_kb_k\bigr|\le2Ma_{n+1}`$, y se cumple el criterio de Bolzano–Cauchy. El [criterio de Leibniz](04-numeric-series.md#alternating-series-test) es un caso particular: $`b_n=(-1)^n`$.

> **Criterio de Abel.** Sea la sucesión $`(a_n)`$ monótona y acotada, y sea convergente la serie $`\sum_{n=1}^{\infty}b_n`$. Entonces la serie $`\sum_{n=1}^{\infty}a_nb_n`$ converge.

Se reduce al criterio de Dirichlet: si $`a_n\to a`$ monótonamente, entonces $`a_nb_n=(a_n-a)b_n+ab_n`$, y $`|a_n-a|\downarrow0`$.

<a id="sec-7-5"></a>
## §7.5. Reordenaciones de series

> <a id="def-7-5-1"></a>**Definición 7.5.1.** Sean dadas una serie $`\sum_{n=1}^{\infty}a_n`$ y una aplicación [biyectiva](01-logic-sets-functions.md#sec-1-4) $`\sigma:\mathbb N\to\mathbb N`$. La serie $`\sum_{n=1}^{\infty}a_{\sigma(n)}`$ se llama reordenación de la serie original $`\sum_{n=1}^{\infty}a_n`$.

> <a id="def-7-5-2"></a>**Definición 7.5.2.** Diremos que la serie $`\sum_{n=1}^{\infty}a_n`$ tiene la propiedad conmutativa si para toda biyección $`\sigma:\mathbb N\to\mathbb N`$ la serie $`\sum_{n=1}^{\infty}a_{\sigma(n)}`$ converge o diverge a la vez que la serie original y, además,
> ```math
> \sum_{n=1}^{\infty}a_n=\sum_{n=1}^{\infty}a_{\sigma(n)} .
> ```

Ejemplo del profesor: si en la serie $`1-\frac12+\frac13-\frac14+\ldots=\ln2`$ cada término positivo va seguido de dos negativos,
```math
1-\frac12-\frac14+\frac13-\frac16-\frac18+\frac15-\frac1{10}-\frac1{12}+\ldots ,
```
entonces las sumas parciales $`T_{3m}`$ son iguales a $`\frac12S_{2m}`$, y la suma de la serie reordenada es $`\frac12\ln2`$.

> **Propiedades conmutativas de las series.**
> 1. Las series positivas tienen la propiedad conmutativa.
> 2. Las series absolutamente convergentes tienen la propiedad conmutativa.
> 3. (Teorema de Riemann.) Una serie condicionalmente convergente no tiene la propiedad conmutativa: para todo $`B\in\overline{\mathbb R}`$ existe una biyección $`\sigma`$ con $`\sum_{n=1}^{\infty}a_{\sigma(n)}=B`$.

Para el punto 2 la serie se descompone en sus partes positiva y negativa $`a_n=a_n^+-a_n^-`$, cada una de las cuales converge y se reordena por el punto 1. Para el punto 3 ambas partes divergen a $`+\infty`$, mientras que $`a_n\to0`$: se toman términos positivos hasta que la suma supere $`B`$, luego negativos hasta que sea menor que $`B`$, y así sucesivamente.

## Ejemplo resuelto

**La serie $`\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^p}`$.** Para $`p>1`$ la serie de valores absolutos $`\sum\frac1{n^p}`$ converge ([lema de Cauchy](#sec-7-3)), y la serie converge absolutamente. Para $`0<p\le1`$ los números $`\frac1{n^p}`$ decrecen monótonamente a cero, y la serie converge por el criterio de Leibniz, mientras que la serie de valores absolutos diverge: la convergencia es condicional y, por el teorema de Riemann, una reordenación puede dar cualquier suma. Para $`p\le0`$ el término general no tiende a cero, así que la serie diverge.

**La serie $`\sum_{n=1}^{\infty}\frac{\sin n}{n}`$.** Las sumas parciales de los senos están acotadas:
```math
\Bigl|\sum_{k=1}^{n}\sin k\Bigr|=\Bigl|\frac{\sin\frac n2\,\sin\frac{n+1}{2}}{\sin\frac12}\Bigr|\le\frac{1}{\sin\frac12},
```
y $`\frac1n\downarrow0`$, por lo que la serie converge por el [criterio de Dirichlet](#sec-7-4). La convergencia es condicional: $`\frac{|\sin n|}{n}\ge\frac{\sin^2n}{n}=\frac{1}{2n}-\frac{\cos2n}{2n}`$, donde $`\sum\frac{\cos2n}{2n}`$ converge (de nuevo el criterio de Dirichlet) y $`\sum\frac1{2n}`$ diverge.

## Errores frecuentes

1. Considerar la condición $`a_n\to0`$ suficiente para la convergencia (la serie armónica).
2. Sacar conclusiones de los criterios de d'Alembert o de Cauchy cuando el límite es $`1`$.
3. Aplicar los [criterios de comparación](04-numeric-series.md#sec-4-2) a series cuyos términos cambian de signo: solo están probados para series positivas.
4. Olvidar la monotonía en el criterio de Leibniz: la serie con términos $`\frac{1}{\sqrt n}`$ en los lugares impares y $`-\frac1n`$ en los pares es alternada y sus términos tienden a cero, pero diverge.
5. Reordenar o agrupar los términos de una serie condicionalmente convergente como si fuera una suma finita: una reordenación puede cambiar la suma.

## Ejercicios

1. Estudie la convergencia de la serie $`\sum_{n=1}^{\infty}\frac{n!}{n^n}`$.
2. Estudie la convergencia de la serie $`\sum_{n=2}^{\infty}\frac{1}{n\ln n}`$.
3. ¿Converge la serie $`\sum_{n=1}^{\infty}\frac{(-1)^n}{\sqrt n}`$ absolutamente? ¿condicionalmente?
4. Demuestre que la serie $`\sum_{n=1}^{\infty}\frac{\cos n}{n}`$ converge.

<details>
<summary>Respuestas breves</summary>

1. Converge por el criterio de d'Alembert: $`\frac{a_{n+1}}{a_n}=\bigl(1+\frac1n\bigr)^{-n}\to\frac1e<1`$.
2. Diverge: los términos decrecen monótonamente y la serie condensada $`\sum\frac{2^n}{2^nn\ln2}=\sum\frac{1}{n\ln2}`$ diverge (lema de Cauchy).
3. Converge condicionalmente: el criterio de Leibniz da la convergencia, mientras que $`\sum\frac1{\sqrt n}`$ diverge ($`p=\frac12\le1`$).
4. Criterio de Dirichlet: $`\frac1n\downarrow0`$, y $`\bigl|\sum_{k=1}^{n}\cos k\bigr|\le\frac{1}{\sin\frac12}`$.
</details>

---

[← 22. Fórmula de Taylor en ℝⁿ, aplicaciones implícitas, extremos](22-taylor-implicit-extrema.md) · [Índice](index.md) · [Términos y teoremas](term-index.md) · [24. Series funcionales y de potencias →](24-functional-power-series.md)
