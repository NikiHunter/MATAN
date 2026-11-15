---
title: "Seminario NM-204. Control de series — cómo prepararse"
lang: es
---
# Control de series: cómo prepararse

[Русский](../../ru/seminar-sem3/series-test-guide.md) · [English](../../en/seminar-sem3/series-test-guide.md) · **Español**

[Todas las tareas](index.md) · [Apuntes de los seminarios](index.md#seminar-notes) · [← Control del 20 nov. (Taylor y extremos)](test1-guide.md)

> **Qué es esto.** En la consulta previa al control del 20 de noviembre de 2026 el profesor dijo que el problema de series de ese control y el del siguiente se juntarán en un control aparte a finales de noviembre o principios de diciembre; allí irá también el problema «de signo constante», al que se dedicó mucho tiempo. El formato exacto aún no se ha anunciado. Abajo está el material de series de la versión anterior de la guía del control 1 (entonces se esperaban series en los ejercicios 3 y 4) y los problemas de práctica de las variantes anteriores. La página se actualizará cuando se conozca el formato.

## Qué esperar

| Tipo de problema | Qué preguntarán probablemente | Prototipos en las tareas |
|---|---|---|
| demostraciones | Una demostración: un criterio o una propiedad de las series | [3.1–3.9](hw3-numerical-series.md), [4.4, 4.6, 4.10, 4.11](hw4-series-inequalities-bases.md) |
| estudio de series | Estudiar la convergencia de 2–3 series concretas | [3.11](hw3-numerical-series.md), [4.7–4.9, 4.12](hw4-series-inequalities-bases.md) |

Menos probable, pero posible: series con parámetro ([4.8](hw4-series-inequalities-bases.md)), ejemplos y contraejemplos ([3.8, 3.10](hw3-numerical-series.md), [4.5](hw4-series-inequalities-bases.md)). Es un pronóstico a partir de las tareas, no un formato anunciado.

## Demostraciones sobre series

**Tres hechos de los que se deduce casi todo** (con detalle al comienzo de la [tarea 3](hw3-numerical-series.md)):

1. condición necesaria: la serie converge ⟹ $`a_k\to0`$;
2. una serie de términos no negativos converge ⟺ sus sumas parciales están acotadas superiormente;
3. un número finito de términos no influye en la convergencia.

**Qué saber demostrar con el cuaderno cerrado** (por orden decreciente de probabilidad):

| Afirmación | Idea clave en una línea | Dónde |
|---|---|---|
| Una serie convergente tiene sumas parciales acotadas | toda sucesión convergente está acotada | [3.1](hw3-numerical-series.md) |
| Criterio de comparación generalizado | $`\frac{a_n}{b_n}`$ es no creciente ⟹ $`a_n\le Cb_n`$ | [3.4](hw3-numerical-series.md) |
| Criterio de Kummer | multiplicar por $`a_{n+1}`$, sumar, la suma es telescópica | [3.6](hw3-numerical-series.md) |
| Criterio de d'Alembert | Kummer con $`x_n=1`$ | [3.7](hw3-numerical-series.md) |
| Criterio de Raabe | Kummer con $`x_n=n`$ | [3.9](hw3-numerical-series.md) |
| Raabe ⟹ d'Alembert | $`1+\beta\ge1+\frac2n`$ para $`n\ge\frac2\beta`$ | [4.4](hw4-series-inequalities-bases.md) |
| Formas límite de los criterios | un límite ⟹ una desigualdad a partir de cierto índice | [4.6](hw4-series-inequalities-bases.md) |
| Criterio de Leibniz | $`S_{2m}`$ es monótona y acotada, $`S_{2m+1}=S_{2m}+a_{2m+1}`$ | [4.11](hw4-series-inequalities-bases.md) |
| Criterio integral | $`f(k+1)\le\int_k^{k+1}f\le f(k)`$ | [4.10](hw4-series-inequalities-bases.md) |
| Acotación de las sumas $`\sum\sin(kx_0)`$ | multiplicar por $`2\sin\frac{x_0}2`$, suma telescópica | [3.2](hw3-numerical-series.md) |
| $`\sum\cos(kx_0)`$ diverge | $`\cos(2kx_0)=2\cos^2(kx_0)-1`$, el término general no tiende a cero | [3.3](hw3-numerical-series.md) |
| Criterio de la raíz de Cauchy | $`\sqrt[n]{a_n}\le q`$ ⟺ $`a_n\le q^n`$; para la divergencia bastan infinitos $`n`$ | [teorema 8.2](notes-2-series-basics.md#thm-8-2) |
| $`\sum\sin(kx_0)`$ converge ⟺ $`x_0\in\pi\mathbb Z`$ | $`\cos(kx_0)`$ se expresa con $`\sin(kx_0)`$ y $`\sin((k+1)x_0)`$ | [ejemplo 8.1](notes-2-series-basics.md#ex-8-1) |
| $`\sum\frac{c_k}{k^d}`$ converge ⟺ $`d>1`$ | comparación con $`\frac{M_2}{k^d}`$ y después Raabe | [3.11](hw3-numerical-series.md#p-3-11), [teorema 12.1](notes-3-kummer-dalembert-raabe.md#thm-12-1) |

**Los criterios en la notación del seminario.** Atención: en el seminario se usa el cociente $`\dfrac{a_n}{a_{n+1}}`$ (el anterior entre el siguiente), no $`\dfrac{a_{n+1}}{a_n}`$.

| Criterio | Converge si, a partir de cierto índice, | Diverge si, a partir de cierto índice, |
|---|---|---|
| Kummer | $`x_n\frac{a_n}{a_{n+1}}-x_{n+1}\ge\alpha>0`$ | $`x_n\frac{a_n}{a_{n+1}}-x_{n+1}\le0`$ y $`\sum\frac1{x_n}`$ diverge |
| d'Alembert | $`\frac{a_n}{a_{n+1}}\ge1+\beta`$, $`\beta>0`$ | $`\frac{a_n}{a_{n+1}}\le1`$ |
| Raabe | $`\frac{a_n}{a_{n+1}}\ge1+\frac{1+\gamma}n`$, $`\gamma>0`$ | $`\frac{a_n}{a_{n+1}}\le1+\frac1n`$ |
| Cauchy | $`\sqrt[n]{a_n}\le q<1`$ | $`\sqrt[n]{a_n}\ge1`$ para infinitos $`n`$ |
| Cauchy (forma límite) | $`\sqrt[k]{a_k}\to L<1`$ | $`\sqrt[k]{a_k}\to L>1`$ |
| Leibniz | los signos alternan, $`\lvert a_k\rvert`$ es no creciente, $`a_k\to0`$ | — |

**Cómo escribir una demostración para no perder puntos.**

- Nombrar explícitamente el índice a partir del cual vale la desigualdad y remitir a «un número finito de términos no influye».
- Antes de multiplicar o dividir una desigualdad, decir que el factor es positivo.
- Al final, nombrar el criterio usado: «las sumas parciales de una serie no negativa están acotadas, luego converge».

## Estudio de la convergencia de series

**Orden de actuación.**

1. **¿Tiende a cero el término general?** Si no, diverge; fin ([4.7, 3)](hw4-series-inequalities-bases.md)).
2. **¿De signo variable?** Comprobar Leibniz. Si la serie tiene ceros o los signos alternan por grupos, quitar los ceros o agrupar ([4.12](hw4-series-inequalities-bases.md)).
3. **¿Factoriales, potencias $`q^k`$, $`k^k`$?** Calcular $`\frac{a_k}{a_{k+1}}`$. Límite mayor que $`1`$: converge; menor que $`1`$: diverge.
4. **¿El límite del cociente vale $`1`$?** D'Alembert no sirve. Calcular $`R_k=k\bigl(\frac{a_k}{a_{k+1}}-1\bigr)`$: límite mayor que $`1`$, converge; menor que $`1`$, diverge ([4.9](hw4-series-inequalities-bases.md)).
5. **¿Potencias, raíces, expresiones racionales en $`k`$?** Llevar a la forma $`\frac{C_k}{k^\alpha}`$ con $`0<M_1\le C_k\le M_2`$; converge ⟺ $`\alpha>1`$ ([3.11](hw3-numerical-series.md), [4.8](hw4-series-inequalities-bases.md)). Diferencia de raíces: multiplicar por el conjugado.
6. **¿Una potencia $`k`$-ésima completa?** Criterio de la raíz de Cauchy.
7. **¿Logaritmos de la forma $`\frac1{k\ln^pk}`$?** Criterio integral.
8. **¿Una serie irregular** (términos definidos a trozos)? Estimar directamente las sumas parciales ([4.7, 2)](hw4-series-inequalities-bases.md)).

**Series patrón.**

| Serie | Converge |
|---|---|
| $`\sum q^k`$ | para $`\lvert q\rvert<1`$ |
| $`\sum\frac1{k^\alpha}`$ | para $`\alpha>1`$ |
| $`\sum\frac{1}{k\ln^pk}`$ | para $`p>1`$ |
| $`\sum\frac1{k(k+1)}`$, $`\sum\frac1{k!}`$ | sí |
| $`\sum\frac{(-1)^k}{k^\alpha}`$ | para $`\alpha>0`$ (absolutamente para $`\alpha>1`$) |

**Límites y desigualdades útiles.** $`\bigl(1+\frac1k\bigr)^k\uparrow e`$, luego $`\bigl(1+\frac1k\bigr)^k<e`$ para todo $`k`$; $`\sqrt[k]k\to1`$; $`1+t\le e^t`$; $`(1+x)^\alpha\ge1+\alpha x`$ para $`\alpha\ge1`$, $`x\ge0`$; $`\ln(k!)\le k\ln k`$.

**Errores típicos.**

- El cociente al revés: con $`\frac{a_k}{a_{k+1}}\to L`$ la serie converge para $`L>1`$, no para $`L<1`$.
- La conclusión «el límite del cociente es $`1`$, luego diverge»: no, el criterio simplemente no se aplica.
- El criterio de Leibniz aplicado sin comprobar la monotonía de los módulos o habiendo términos nulos.
- «$`a_k\to0`$, luego converge»: la condición necesaria no es suficiente.
- Comparación $`a_k\le b_k`$ para series de signo variable: los criterios de comparación solo valen para las no negativas.
- El valor frontera de un parámetro no se trata aparte ($`\beta=e`$ en [4.8](hw4-series-inequalities-bases.md)).

## Qué repasar en los apuntes de los seminarios

Los [apuntes](index.md#seminar-notes) muestran en qué forma se dio la teoría en el seminario. En el control es sensato escribir con la misma notación: sucesiones finalmente positivas, el cociente $`\frac{a_n}{a_{n+1}}`$.

| Tema | Qué repasar | Dónde |
|---|---|---|
| demostraciones | las demostraciones de la pizarra: comparación, Cauchy, comparación generalizada, Kummer, d'Alembert, Raabe, Raabe ⟹ d'Alembert | [parte 2](notes-2-series-basics.md), [teorema 10.2 y sus corolarios](notes-3-kummer-dalembert-raabe.md#thm-10-2), [observación 14.2](notes-4-examples-tests.md#rem-14-2) |
| estudio de series | series con parámetro y ejemplos en los que los criterios fallan | [ejemplos 13.1, 13.2](notes-4-examples-tests.md#ex-13-1), [14.1](notes-4-examples-tests.md#ex-14-1), [10.4](notes-3-kummer-dalembert-raabe.md#ex-10-4), [observación 12.2](notes-3-kummer-dalembert-raabe.md#rem-12-2) |

## Plan de preparación

Un plan detallado llegará cuando se conozca el formato del control. Por ahora, un día de repaso de series:

1. Aprender la tabla de criterios y los tres hechos básicos; leer las [partes 2–4 de los apuntes](notes-2-series-basics.md).
2. Por escrito, con el cuaderno cerrado, demostrar 3.4, 3.6, 3.7, 3.9, 4.11 y el criterio de la raíz de Cauchy ([teorema 8.2](notes-2-series-basics.md#thm-8-2)). Comparar con las soluciones.
3. Rehacer 4.7–4.9 y 4.12.
4. Resolver un bloque de [problemas de práctica](#practice): 40 minutos.

## Autoevaluación

1. ¿Qué sucesión $`x_n`$ del criterio de Kummer da el criterio de Raabe?
2. ¿Qué afirma el criterio de Raabe para una serie con $`\frac{a_n}{a_{n+1}}=1+\frac1{2n+1}`$?
3. ¿Converge $`\sum\frac{e^kk!}{k^k}`$, y por qué la forma límite no ayuda aquí?
4. ¿Qué tres condiciones necesita el criterio de Leibniz?
5. Dé un ejemplo de serie divergente con sumas parciales acotadas.
6. ¿Por qué en el criterio de Cauchy bastan «infinitos $`n`$» para la divergencia y en el de d'Alembert no?

<details>
<summary>Respuestas</summary>

1. $`x_n=n`$.
2. Diverge: $`1+\frac1{2n+1}\le1+\frac1n`$.
3. Diverge. El límite del cociente es $`1`$, pero $`\frac{a_k}{a_{k+1}}=\frac1e\bigl(1+\frac1k\bigr)^k<1`$ para todo $`k`$: se aplica la forma no límite de d'Alembert.
4. Los signos alternan, los módulos son no crecientes, el término general tiende a cero.
5. $`\sum(-1)^k`$, o $`\sum\cos(kx_0)`$ para $`x_0\notin2\pi\mathbb Z`$.
6. $`\sqrt[n]{a_n}\ge1`$ significa $`a_n\ge1`$, e infinitos términos así impiden que $`a_n\to0`$. Un cociente solo describe un paso: la serie del [ejemplo 10.4](notes-3-kummer-dalembert-raabe.md#ex-10-4) crece infinitas veces y aun así converge.
</details>

<a id="practice"></a>
## Problemas de práctica

Los ejercicios 3 y 4 de las variantes de práctica anteriores del control 1. En cada bloque, el problema 1 es una demostración y el problema 2 pide estudiar la convergencia de series concretas. Referencia: 40 minutos por bloque.

### Bloque A

**1.** Sean $`a_n>0`$, $`b_n>0`$ y $`\dfrac{a_{n+1}}{a_n}\le\dfrac{b_{n+1}}{b_n}`$ para todo $`n>N_0`$. Demostrar que de la convergencia de $`\sum b_k`$ se sigue la de $`\sum a_k`$. Con esta afirmación, demostrar la convergencia de $`\sum\limits_{k=1}^\infty\dfrac1{k!}`$.

**2.** Estudiar la convergencia de las series
```math
\text{a)}\ \sum_{k=1}^\infty\frac{(k!)^2}{(2k)!};\qquad\text{b)}\ \sum_{k=1}^\infty\frac{(2k-1)!!}{(2k+2)!!};\qquad\text{c)}\ \sum_{k=1}^\infty\frac{(-1)^k}{\ln(k+1)} .
```

<details>
<summary>Soluciones del bloque A</summary>

**1.** Multiplicando la desigualdad por $`\frac{a_n}{b_{n+1}}>0`$ se obtiene $`\frac{a_{n+1}}{b_{n+1}}\le\frac{a_n}{b_n}`$ para $`n>N_0`$: la sucesión $`\frac{a_n}{b_n}`$ es no creciente, luego $`a_n\le Cb_n`$ para $`n\ge N_0+1`$, donde $`C=\frac{a_{N_0+1}}{b_{N_0+1}}`$. Sea $`B`$ la suma de $`\sum_{k>N_0}b_k`$ (converge junto con $`\sum b_k`$). Entonces $`\sum_{k=N_0+1}^na_k\le C\sum_{k=N_0+1}^nb_k\le CB`$. Las sumas parciales de la serie positiva $`\sum_{k>N_0}a_k`$ están acotadas, luego converge; añadir un número finito de términos no cambia la convergencia.

Aplicación: $`a_k=\frac1{k!}`$, $`b_k=\frac1{k(k+1)}`$ (la serie $`\sum b_k`$ converge: sus sumas parciales valen $`1-\frac1{n+1}`$). $`\frac{a_{k+1}}{a_k}=\frac1{k+1}`$, $`\frac{b_{k+1}}{b_k}=\frac k{k+2}`$; la desigualdad $`\frac1{k+1}\le\frac k{k+2}`$ equivale a $`k^2\ge2`$ y vale para $`k\ge2`$, es decir, $`N_0=1`$.

**2.** a) $`\dfrac{a_k}{a_{k+1}}=\dfrac{(2k+2)(2k+1)}{(k+1)^2}=\dfrac{2(2k+1)}{k+1}\ge3`$ para todo $`k\ge1`$ (y tiende a $`4`$). Por el criterio de d'Alembert con $`\beta=2`$ la serie **converge**.

b) $`\dfrac{a_k}{a_{k+1}}=\dfrac{2k+4}{2k+1}=1+\dfrac3{2k+1}\to1`$: d'Alembert no sirve. $`R_k=\dfrac{3k}{2k+1}\to\dfrac32>1`$: por el criterio de Raabe la serie **converge**. (Sin límite: $`\frac3{2k+1}\ge\frac{5/4}k`$ para $`k\ge3`$, $`\gamma=\frac14`$.)

c) Los signos alternan, $`\frac1{\ln(k+1)}`$ decrece y tiende a cero: por el criterio de Leibniz la serie **converge**. No hay convergencia absoluta: $`\ln(k+1)\le k`$, luego $`\frac1{\ln(k+1)}\ge\frac1k`$. La convergencia es condicional.
</details>

### Bloque B

**1.** Enunciar y demostrar el criterio de Leibniz. ¿Sigue siendo cierto si la condición $`a_ka_{k+1}<0`$ se sustituye por $`a_ka_{k+1}\le0`$?

**2.** Estudiar la convergencia de las series ($`\alpha\in\mathbb R`$ es un parámetro)
```math
\text{a)}\ \sum_{k=1}^\infty\frac{k^k}{3^k\,k!};\qquad\text{b)}\ \sum_{k=1}^\infty\frac{\sqrt{k^2+1}-k}{k^\alpha};\qquad\text{c)}\ \sum_{k=1}^\infty\frac{\sin\frac{k\pi}2}{\sqrt[3]k} .
```

<details>
<summary>Soluciones del bloque B</summary>

**1.** *Enunciado.* Si para todo $`k`$ se cumplen $`a_ka_{k+1}<0`$, $`|a_{k+1}|\le|a_k|`$ y $`a_k\to0`$, la serie $`\sum a_k`$ converge.

*Demostración.* Podemos suponer $`a_1>0`$ (si no, multiplicamos la serie por $`-1`$); entonces $`a_{2j-1}>0`$, $`a_{2j}<0`$. Los paréntesis $`a_{2j-1}+a_{2j}=|a_{2j-1}|-|a_{2j}|\ge0`$, luego $`S_{2m}=\sum_{j=1}^m(a_{2j-1}+a_{2j})`$ es no decreciente. Por otra parte, $`S_{2m}=a_1+\sum_{j=1}^{m-1}(a_{2j}+a_{2j+1})+a_{2m}\le a_1`$, pues $`a_{2j}+a_{2j+1}=-|a_{2j}|+|a_{2j+1}|\le0`$ y $`a_{2m}<0`$. La sucesión monótona y acotada $`S_{2m}`$ converge a cierto $`S`$. Entonces $`S_{2m+1}=S_{2m}+a_{2m+1}\to S`$, pues $`a_k\to0`$. Las subsucesiones de índices pares e impares convergen al mismo límite, luego $`S_n\to S`$.

*La pregunta.* Sí. Si todos los $`a_k\ne0`$, la condición $`\le0`$ coincide con $`<0`$. Si $`a_K=0`$, de $`|a_{k+1}|\le|a_k|`$ se sigue $`a_k=0`$ para $`k\ge K`$, y la serie es una suma finita.

**2.** a) $`\dfrac{a_k}{a_{k+1}}=\dfrac{k^k}{3^kk!}\cdot\dfrac{3^{k+1}(k+1)!}{(k+1)^{k+1}}=\dfrac{3}{\bigl(1+\frac1k\bigr)^k}>\dfrac3e>1`$ para todo $`k`$, ya que $`\bigl(1+\frac1k\bigr)^k<e`$. Por el criterio de d'Alembert con $`\beta=\frac3e-1`$ la serie **converge**.

b) $`\sqrt{k^2+1}-k=\dfrac{1}{\sqrt{k^2+1}+k}`$, luego $`a_k=\dfrac{C_k}{k^{\alpha+1}}`$, $`C_k=\dfrac{k}{\sqrt{k^2+1}+k}`$. Como $`k<\sqrt{k^2+1}\le\sqrt2\,k`$, se tiene $`\dfrac1{1+\sqrt2}\le C_k<\dfrac12`$. Por el problema 3.11 la serie **converge para $`\alpha>0`$ y diverge para $`\alpha\le0`$**.

c) Para $`k`$ par los términos son nulos; para $`k=2j-1`$ el numerador vale $`(-1)^{j-1}`$. Los términos no nulos $`c_j=\dfrac{(-1)^{j-1}}{\sqrt[3]{2j-1}}`$ forman una serie convergente por el criterio de Leibniz; insertar ceros no cambia las sumas parciales ($`S_{2m-1}=S_{2m}=T_m`$). La serie **converge** (condicionalmente: $`\sum\frac1{\sqrt[3]{2j-1}}`$ diverge).
</details>

### Bloque C

**1.** Sean $`x_n>0`$ y $`a_n>0`$ para todo $`n`$, y supongamos que existen $`\alpha>0`$ y $`N`$ tales que $`x_n\dfrac{a_n}{a_{n+1}}-x_{n+1}\ge\alpha`$ para todo $`n>N`$. Demostrar que la serie $`\sum a_k`$ converge. Deducir de aquí el criterio de convergencia de d'Alembert. ¿Por qué el criterio de d'Alembert no dice nada sobre la serie $`\sum\frac1{k^2}`$?

**2.** Estudiar la convergencia de las series
```math
\text{a)}\ \sum_{k=1}^\infty\Bigl(\frac{k+1}{2k+3}\Bigr)^k;\qquad\text{b)}\ \sum_{k=2}^\infty\frac{1}{k\ln^2k};\qquad\text{c)}\ \sum_{k=1}^\infty\frac{(-1)^kk}{k^2+1} .
```

<details>
<summary>Soluciones del bloque C</summary>

**1.** Multiplicamos la desigualdad por $`a_{n+1}>0`$: $`x_na_n-x_{n+1}a_{n+1}\ge\alpha a_{n+1}`$ para $`n>N`$. Sumamos para $`n=N+1,\dots,N+m`$; a la izquierda la suma es telescópica:

```math
\alpha\sum_{n=N+1}^{N+m}a_{n+1}\le x_{N+1}a_{N+1}-x_{N+m+1}a_{N+m+1}<x_{N+1}a_{N+1}.
```

Las sumas parciales de la serie positiva $`\sum_{k\ge N+2}a_k`$ están acotadas por $`\frac{x_{N+1}a_{N+1}}{\alpha}`$, luego converge, y con ella $`\sum a_k`$.

*D'Alembert.* Tomamos $`x_n=1`$: la condición se convierte en $`\frac{a_n}{a_{n+1}}-1\ge\alpha`$, es decir, $`\frac{a_n}{a_{n+1}}\ge1+\beta`$ con $`\beta=\alpha`$. Así, si $`\frac{a_n}{a_{n+1}}\ge1+\beta`$ para $`n>N`$, $`\beta>0`$, la serie converge.

*La serie $`\sum\frac1{k^2}`$.* $`\frac{a_k}{a_{k+1}}=\bigl(1+\frac1k\bigr)^2\to1`$. Este cociente es mayor que $`1`$ para todo $`k`$, así que la condición de divergencia $`\frac{a_k}{a_{k+1}}\le1`$ no se cumple; y tiende a $`1`$, así que con ningún $`\beta>0`$ constante se cumple $`\frac{a_k}{a_{k+1}}\ge1+\beta`$ para todo $`k`$ grande. El criterio de d'Alembert compara la serie con una progresión geométrica, y $`\frac1{k^2}`$ decrece más despacio que cualquier progresión. Aquí funciona el criterio de Raabe: $`\bigl(1+\frac1k\bigr)^2\ge1+\frac2k`$, $`\gamma=1`$.

**2.** a) $`\dfrac{k+1}{2k+3}<\dfrac12`$ para todo $`k`$ (pues $`2k+2<2k+3`$), luego $`0<a_k<2^{-k}`$. Por comparación con una progresión geométrica la serie **converge**. (Criterio de Cauchy: $`\sqrt[k]{a_k}\to\frac12<1`$.)

b) La función $`f(x)=\dfrac1{x\ln^2x}`$ es positiva y decreciente en $`[2;+\infty)`$ (el denominador crece). $`\displaystyle\int_2^x\frac{dy}{y\ln^2y}=\frac1{\ln2}-\frac1{\ln x}\to\frac1{\ln2}`$. La integral converge, y por el criterio integral la serie **converge**. (D'Alembert y Raabe callan aquí: $`R_k\to1`$.)

c) Los signos alternan. Los módulos $`\frac{k}{k^2+1}`$ decrecen: la desigualdad $`\frac{k}{k^2+1}\ge\frac{k+1}{(k+1)^2+1}`$ equivale a $`k^2+k\ge1`$. Los módulos tienden a cero. Por el criterio de Leibniz la serie **converge**. No hay convergencia absoluta: $`\frac{k}{k^2+1}\ge\frac1{2k}`$. La convergencia es condicional.
</details>

### Qué comprueba cada bloque

| Problema | Bloque A | Bloque B | Bloque C |
|---|---|---|---|
| 1 | comparación generalizada | Leibniz | Kummer ⟹ d'Alembert |
| 2 | d'Alembert, Raabe, Leibniz | d'Alembert con $`e`$, un parámetro, Leibniz con ceros | comparación (Cauchy), criterio integral, Leibniz |
