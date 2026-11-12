---
title: "Seminario NM-204. Tarea 4 — series, desigualdades y bases: soluciones"
lang: es
hw: 4
tags: [mathinmind/es, mathinmind/other]
---
# Tarea 4. Series, desigualdad de Hölder y bases de conjuntos — soluciones

[[ru/seminar-sem3/hw4-series-inequalities-bases|Русский]] · [[en/seminar-sem3/hw4-series-inequalities-bases|English]] · **Español**

[[es/seminar-sem3/hw3-numerical-series|← Tarea 3]] · [[es/seminar-sem3/index|Todas las tareas]] · [[es/lectures-2025-26/lecture-69-70|Lecciones 69–70, §7.3–§7.4]]

Aquí se resuelven los problemas nuevos 4.1–4.12. Los problemas «antiguos» de esta tarea están resueltos antes: 1.2 en la [[es/seminar-sem3/hw1-taylor|tarea 1]]; 2.2 y 2'.1–2'.3 en la [[es/seminar-sem3/hw2-conditional-extremum|tarea 2]]; 3.1–3.3, 3.10, 3.11 en la [[es/seminar-sem3/hw3-numerical-series|tarea 3]]. Las referencias (F1)–(F3) son los tres hechos del comienzo de la [[es/seminar-sem3/hw3-numerical-series|tarea 3]]: la condición necesaria de convergencia, el criterio de acotación de las sumas parciales para series no negativas y la independencia de la convergencia respecto de un número finito de términos.

## Problema 4.1

**Enunciado.** $p>1$, $p'=\frac p{p-1}$, $b_k\ge0$, $\sum_{k=1}^nb_k^{p'}=1$. Hallar los puntos de extremo condicionado de $f(x)=\sum_{k=1}^nb_kx_k$ sobre el conjunto $M=\{x:\ x_k\ge0,\ \sum_{k=1}^nx_k^p=1\}$.

Identidades útiles para exponentes conjugados: $\frac1p+\frac1{p'}=1$, $p'-1=\frac1{p-1}$, $(p-1)p'=p$.

**Búsqueda del candidato por el método de Lagrange.** En la región $x_k>0$ la ligadura $\varphi=\sum x_k^p-1$ es suave, $\nabla\varphi=(p\,x_k^{p-1})\ne0$. Sistema: $b_k=\lambda p\,x_k^{p-1}$, de donde $x_k=\bigl(\frac{b_k}{\lambda p}\bigr)^{1/(p-1)}$ y $x_k^p=\bigl(\frac{b_k}{\lambda p}\bigr)^{p'}$. Sustituyendo en la ligadura: $(\lambda p)^{-p'}\sum b_k^{p'}=(\lambda p)^{-p'}=1$, es decir, $\lambda p=1$ y
$$
x_k^*=b_k^{\,1/(p-1)}=b_k^{\,p'-1},\qquad f(x^*)=\sum b_k\cdot b_k^{\,p'-1}=\sum b_k^{\,p'}=1 .
$$
El punto $x^*$ está en $M$: $\sum(x_k^*)^p=\sum b_k^{(p'-1)p}=\sum b_k^{p'}=1$.

**Demostración rigurosa de que es el máximo.** El método de Lagrange solo da un candidato, y solo dentro de la región $x_k>0$; $M$ tiene además una frontera, donde parte de las coordenadas se anulan. Para no recorrer las caras, demostramos la estimación directamente. Para $u,v\ge0$ vale la desigualdad de Young
$$
uv\le\frac{u^p}p+\frac{v^{p'}}{p'},\qquad\text{con igualdad solo si }u^p=v^{p'}.\tag{1}
$$
(Con $v>0$ fijo, la función $\psi(u)=\frac{u^p}p+\frac{v^{p'}}{p'}-uv$ tiene derivada $\psi'(u)=u^{p-1}-v$, que cambia de signo de menos a más en el único punto $u_0=v^{1/(p-1)}$; allí $u_0^p=v^{p'}$ y $\psi(u_0)=v^{p'}\bigl(\frac1p+\frac1{p'}-1\bigr)=0$. Luego $\psi\ge0$ y $\psi=0$ solo en $u=u_0$. Para $v=0$ la desigualdad es evidente.)

Aplicamos (1) con $u=x_k$, $v=b_k$ y sumamos en $k$: para todo $x\in M$
$$
f(x)=\sum_{k=1}^nb_kx_k\le\frac1p\sum_{k=1}^nx_k^p+\frac1{p'}\sum_{k=1}^nb_k^{p'}=\frac1p+\frac1{p'}=1,
$$
y la igualdad se alcanza solo cuando $x_k^p=b_k^{p'}$ para todo $k$, es decir, en $x=x^*$. Así, $x^*$ es el único punto de máximo global, $f_{\max}=1$.

**Mínimo.** Sea $b_{\min}=\min_kb_k$. Sobre $M$ cada $x_k\in[0,1]$, luego $x_k\ge x_k^p$ y $\sum x_k\ge\sum x_k^p=1$. Por tanto
$$
f(x)=\sum b_kx_k\ge b_{\min}\sum x_k\ge b_{\min}.
$$
Si $b_{\min}>0$, la igualdad solo es posible cuando $\sum x_k=1$, es decir, cuando cada $x_k\in\{0,1\}$: $x=e_j$ es un vector de la base, y además $b_j=b_{\min}$. Si $b_{\min}=0$, la igualdad $f(x)=0$ significa $x_k=0$ para todo $k$ con $b_k>0$.

**Los demás extremos locales.** El cambio $y_k=x_k^p$ aplica $M$ homeomórficamente sobre el símplice $\Delta=\{y_k\ge0,\ \sum y_k=1\}$, y $f$ pasa a ser $F(y)=\sum b_ky_k^{1/p}$. La función $t\mapsto t^{1/p}$ es estrictamente cóncava en $[0;+\infty)$, así que $F$ es cóncava sobre el conjunto convexo $\Delta$.

- *No hay máximos locales distintos de $x^*$.* Un máximo local de una función cóncava es global: si $F(y')>F(y)$, a lo largo del segmento $F(y+t(y'-y))\ge F(y)+t(F(y')-F(y))>F(y)$ para $t>0$ arbitrariamente pequeño.
- *Un mínimo local solo es posible en dos casos.* Supongamos que en un punto $y$ son positivas dos coordenadas $y_i,y_l$ y además $b_i>0$. Entonces $g(t)=F(y+t(e_i-e_l))$ está definida para $|t|$ pequeño y es estrictamente cóncava, de modo que $g(0)>\frac12(g(t)+g(-t))$: no hay mínimo en $y$. Quedan los puntos donde $b_k=0$ en todas las coordenadas positivas (allí $f=0$, mínimo global) y los vértices $x=e_j$.
- *Un vértice $e_j$ con $b_j>0$.* Sea $s=\sum_{k\ne j}x_k^p$; entonces $x_j=(1-s)^{1/p}\ge1-s$ y
$$
f(x)-b_j=b_j(x_j-1)+\sum_{k\ne j}b_kx_k\ge\sum_{k\ne j}x_k\bigl(b_k-b_jx_k^{p-1}\bigr).
$$
Si todos los $b_k>0$, el segundo miembro es positivo para $x_k$ pequeños (no todos nulos): $e_j$ es un mínimo local estricto con valor $b_j$. Si $b_i=0$ para algún $i\ne j$, un desplazamiento a lo largo de $x_i$ disminuye $f$ (pues $x_j<1$), y no hay mínimo.

**Respuesta.**

1. Máximo: el único punto $x^*=\bigl(b_1^{\,p'-1};\dots;b_n^{\,p'-1}\bigr)$, $f(x^*)=1$ (global; no hay otros máximos locales).
2. Si todos los $b_k>0$: los puntos de mínimo local son los vértices $e_j$, $j=1,\dots,n$, con valores $f(e_j)=b_j$; el mínimo global $\min_kb_k$ se alcanza en los vértices con el menor $b_j$.
3. Si entre los $b_k$ hay ceros: los puntos de mínimo son todos los $x\in M$ con $x_k=0$ siempre que $b_k>0$; el valor es $0$ (mínimo global); no hay otros mínimos locales.

**Por qué funciona.** La función $f$ es lineal, sus superficies de nivel son hiperplanos paralelos de normal $b$, y $M$ es un «trozo de esfera» convexo en la norma $\ell_p$. El máximo se alcanza donde un hiperplano toca a $M$, es decir, donde la normal $(p\,x_k^{p-1})$ a la superficie es proporcional a $b$. Para $p=2$ esto significa $x^*=b$ (un vector unitario con la dirección de $b$): la desigualdad habitual de Cauchy–Schwarz; para $p\ne2$ la «misma dirección» queda deformada por la potencia $p'-1$. El mínimo de una función lineal sobre un conjunto así se va al borde, a las «esquinas» $e_j$, porque entre las esquinas la superficie está curvada hacia fuera.

La condición $\sum b_k^{p'}=1$ es una normalización. De ella sale que el máximo vale exactamente $1$; esto es la desigualdad de Hölder para colecciones normalizadas (problema 4.2).

## Problema 4.2 (desigualdad de Hölder)

**Enunciado.** $p>1$, $p'=\frac p{p-1}$, todos los números son no negativos. Demostrar:

1) $\displaystyle\sum_{k=1}^na_kb_k\le\Bigl(\sum_{k=1}^na_k^p\Bigr)^{1/p}\Bigl(\sum_{k=1}^nb_k^{p'}\Bigr)^{1/p'}$;

2) si las series $\sum x_k^p$ y $\sum y_k^{p'}$ convergen, entonces $\sum x_ky_k$ converge y $\displaystyle\sum_{k=1}^\infty x_ky_k\le\Bigl(\sum_{k=1}^\infty x_k^p\Bigr)^{1/p}\Bigl(\sum_{k=1}^\infty y_k^{p'}\Bigr)^{1/p'}$.

**Demostración de 1).** Sean $A=\bigl(\sum a_k^p\bigr)^{1/p}$, $B=\bigl(\sum b_k^{p'}\bigr)^{1/p'}$.

Si $A=0$, todos los $a_k=0$ y ambos miembros son cero; análogamente si $B=0$.

Sean $A>0$ y $B>0$. Pongamos $\tilde a_k=\frac{a_k}A$, $\tilde b_k=\frac{b_k}B$. Entonces
$$
\sum_{k=1}^n\tilde a_k^{\,p}=\frac{1}{A^p}\sum a_k^p=1,\qquad\sum_{k=1}^n\tilde b_k^{\,p'}=1 .
$$
La colección $\tilde b$ cumple la hipótesis del problema 4.1, y el punto $\tilde a$ pertenece a su conjunto $M$. En 4.1 se demostró que $f\le1$ sobre $M$:
$$
\sum_{k=1}^n\tilde a_k\tilde b_k\le1 .
$$
Multiplicando por $AB>0$ se obtiene $\sum a_kb_k\le AB$. $\blacksquare$

**Demostración de 2).** Sean $X=\sum_{k=1}^\infty x_k^p$, $Y=\sum_{k=1}^\infty y_k^{p'}$. Los términos de estas series son no negativos, así que sus sumas parciales no superan a $X$ e $Y$. Por el apartado 1), para cada $n$
$$
\sum_{k=1}^nx_ky_k\le\Bigl(\sum_{k=1}^nx_k^p\Bigr)^{1/p}\Bigl(\sum_{k=1}^ny_k^{p'}\Bigr)^{1/p'}\le X^{1/p}\,Y^{1/p'} .
$$
La serie $\sum x_ky_k$ es no negativa y sus sumas parciales están acotadas superiormente; por (F2) converge. Pasando al límite cuando $n\to\infty$ en $S_n\le X^{1/p}Y^{1/p'}$ se obtiene la estimación de la suma. $\blacksquare$

**Por qué funciona.** La desigualdad es homogénea: si se multiplican todos los $a_k$ por $t>0$, ambos miembros se multiplican por $t$. Por eso basta demostrarla para colecciones de «longitud uno», y para ellas es exactamente la afirmación sobre el máximo de 4.1. Las colecciones nulas hay que tratarlas aparte solo porque no se puede dividir por cero. El paso a series es estándar: una desigualdad para sumas finitas con segundo miembro independiente de $n$, más la monotonía de las sumas parciales.

Sentido: si $x\in\ell_p$ e $y\in\ell_{p'}$, entonces $xy\in\ell_1$. Para $p=p'=2$ es la desigualdad de Cauchy–Schwarz. La igualdad en 1) se alcanza si y solo si las colecciones $(a_k^p)$ y $(b_k^{p'})$ son proporcionales: la condición de igualdad de 4.1.

## Problema 4.3 (bases de conjuntos)

**Definición del enunciado.** Una familia $\mathcal B$ de subconjuntos no vacíos de $X$ es una base sobre $X$ si (B1) $\bigcup_{D\in\mathcal B}D=X$ y (B2) para cualesquiera $D_1,D_2\in\mathcal B$ existe $D_3\in\mathcal B$ con $D_3\subset D_1\cap D_2$.

Todas las familias siguientes son **encajadas**: de dos elementos cualesquiera, uno está contenido en el otro. Entonces (B2) se cumple automáticamente: como $D_3$ sirve el menor de los dos, que es igual a $D_1\cap D_2$. Así que en cada caso hay que comprobar tres cosas: que los elementos no son vacíos, que la familia es encajada, y (B1).

**1) $\mathcal M_1=\{D_k\}$, $D_k=\{n\ge k\}$, y $\mathcal M_2=\{E_m\}$, $E_m=\{n>m\}$, sobre $\mathbb N$.**

- $k\in D_k$, $m+1\in E_m$: los conjuntos no son vacíos.
- $D_k\cap D_l=D_{\max(k,l)}$, $E_m\cap E_l=E_{\max(m,l)}$: (B2).
- $D_1=\mathbb N$ y $E_0=\mathbb N$, así que las uniones son $\mathbb N$: (B1).

Nótese que $D_k=E_{k-1}$, de modo que $\mathcal M_1=\mathcal M_2$ como familias: es una misma base $n\to\infty$. $\blacksquare$

**2) Familias sobre $\mathbb R$.**

*$\mathcal M_4$, $A_{2,r}=(-\infty;r)$.* No vacíos; $A_{2,r_1}\cap A_{2,r_2}=A_{2,\min(r_1,r_2)}$; todo $x\in\mathbb R$ pertenece a $A_{2,r}$ con $r=|x|+1$, así que la unión es $\mathbb R$. Base sobre $\mathbb R$. $\blacksquare$

*$\mathcal M_{6,x_0}$, $A_{4,r}=(x_0-r;x_0+r)$.* No vacíos ($x_0\in A_{4,r}$); $A_{4,r_1}\cap A_{4,r_2}=A_{4,\min(r_1,r_2)}$; todo $x\in\mathbb R$ pertenece a $A_{4,r}$ con $r=|x-x_0|+1$. Base sobre $\mathbb R$. $\blacksquare$

*$\mathcal M_3$, $A_{1,r}=(-\infty;-r]\cup[r;+\infty)=\{x:\ |x|\ge r\}$.* No vacíos; $A_{1,r_1}\cap A_{1,r_2}=A_{1,\max(r_1,r_2)}$: (B2) se cumple. Pero
$$
\bigcup_{r>0}A_{1,r}=\{x:\ |x|>0\}=\mathbb R\setminus\{0\},
$$
porque $0\notin A_{1,r}$ para ningún $r>0$, mientras que todo $x\ne0$ pertenece a $A_{1,|x|}$.

*$\mathcal M_5$, $A_{3,r}=(r;+\infty)$.* No vacíos; $A_{3,r_1}\cap A_{3,r_2}=A_{3,\max(r_1,r_2)}$: (B2) se cumple. Pero
$$
\bigcup_{r>0}A_{3,r}=(0;+\infty),
$$
porque para $r>0$ en $A_{3,r}$ no hay números $x\le0$.

> [!remark] Observación sobre el enunciado
> Leída literalmente, la condición (B1) para $\mathcal M_3$ y $\mathcal M_5$ sobre $X=\mathbb R$ **no se cumple**: las uniones son $\mathbb R\setminus\{0\}$ y $(0;+\infty)$. Lo que se puede demostrar es lo siguiente: $\mathcal M_3$ es una base sobre $\mathbb R\setminus\{0\}$, $\mathcal M_5$ es una base sobre $(0;+\infty)$; ambas familias cumplen (B2) y constan de conjuntos no vacíos, es decir, son bases sobre $\mathbb R$ en el sentido de la definición sin la exigencia (B1) (así define la base, por ejemplo, Zorich). Para que (B1) se cumpla sobre todo $\mathbb R$, el parámetro debería recorrer no $(0;+\infty)$ sino, por ejemplo, $[0;+\infty)$ para $\mathcal M_3$ y todo $\mathbb R$ para $\mathcal M_5$. Probablemente es una imprecisión del enunciado (hay otras erratas: $\mathcal M_{7,x_0}$ se usa dos veces; $A_{2,r}=(-\infty;r)$ en lugar del conjunto $(-\infty;-r)$ esperado para la base $x\to-\infty$); conviene aclararlo con el profesor. No afecta a los límites: el límite según una base solo depende de los elementos «lejanos» de la familia.

**3) $\mathcal M_{7,x_0}$, $A_{5,r}=(x_0;x_0+r)$, sobre $(x_0;+\infty)$ y $\mathcal M_{8,x_0}$, $A_{6,r}=(x_0-r;x_0)$, sobre $(-\infty;x_0)$.**

- No vacíos: $x_0+\frac r2\in A_{5,r}$, $x_0-\frac r2\in A_{6,r}$; todos los $A_{5,r}\subset(x_0;+\infty)$, $A_{6,r}\subset(-\infty;x_0)$.
- $A_{5,r_1}\cap A_{5,r_2}=A_{5,\min(r_1,r_2)}$, $A_{6,r_1}\cap A_{6,r_2}=A_{6,\min(r_1,r_2)}$: (B2).
- Todo $x>x_0$ pertenece a $A_{5,r}$ con $r=x-x_0+1$; todo $x<x_0$ pertenece a $A_{6,r}$ con $r=x_0-x+1$: (B1). $\blacksquare$

(En el enunciado la segunda familia repite la notación $\mathcal M_{7,x_0}$; aquí se llama $\mathcal M_{8,x_0}$.)

**Por qué funciona.** Una base es una manera de decir «suficientemente lejos» o «suficientemente cerca» en un mismo lenguaje para todos los tipos de límite. Un elemento de la base es un «entorno» de aquello hacia lo que tendemos: $D_k$ es «todos los índices a partir de $k$» ($n\to\infty$); $A_{1,r}$ es $x\to\infty$; $A_{3,r}$ es $x\to+\infty$; $A_{4,r}$ es $x\to x_0$ (con el propio punto $x_0$); $A_{5,r}$ y $A_{6,r}$ son $x\to x_0+0$ y $x\to x_0-0$. La condición (B2) hace falta para que de «$P$ vale en $D_1$» y «$Q$ vale en $D_2$» se siga «$P$ y $Q$ valen en cierto $D_3$»: en esto descansan la unicidad del límite y la aritmética de los límites. Que los elementos no sean vacíos hace falta para que el límite sea único (sobre el conjunto vacío cualquier cosa es cierta).

## Problema 4.4

**Enunciado.** Deducir el criterio de d'Alembert (problema 3.7) del criterio de Raabe (problema 3.9).

**Demostración.** Sea $a_n>0$ para $n>N_0$.

1) Sea $\frac{a_n}{a_{n+1}}\ge1+\beta$ para $n>N_1$, $\beta>0$. Tomemos $\gamma=1$ y un natural $N_1'\ge\max\bigl(N_1,\frac2\beta\bigr)$. Para $n>N_1'$ se tiene $\frac2n<\beta$, luego
$$
\frac{a_n}{a_{n+1}}\ge1+\beta\ge1+\frac2n=1+\frac{1+\gamma}n .
$$
Se cumple la condición 1) del criterio de Raabe (y $N_1'>N_0$): la serie converge.

2) Sea $\frac{a_n}{a_{n+1}}\le1$ para $n>N_2$. Entonces con mayor razón
$$
\frac{a_n}{a_{n+1}}\le1<1+\frac1n
$$
para $n>N_2$. Se cumple la condición 2) del criterio de Raabe: la serie diverge. $\blacksquare$

**Por qué funciona.** La escala de Raabe es más fina: d'Alembert exige que el cociente esté separado de uno por un margen constante $\beta$, mientras que a Raabe le basta un margen del orden de $\frac{1+\gamma}n$, que tiende a cero. Un margen constante tarde o temprano supera a cualquier $\frac cn$, así que todo lo que ve d'Alembert lo ve también Raabe. El recíproco es falso: para $a_n=\frac1{n^2}$ el cociente es $(1+\frac1n)^2\to1$, d'Alembert calla y Raabe da la convergencia. Ambos criterios son casos particulares de Kummer con $x_n=1$ y $x_n=n$: cuanto más despacio diverge $\sum\frac1{x_n}$, más fuerte es el criterio.

## Problema 4.5$^{**}$

**Enunciado.** Dar un ejemplo de serie convergente para la que el conjunto $\bigl\{k:\ 1<\frac{a_k}{a_{k+1}}\le1+\frac1k\bigr\}$ sea numerable.

**Solución.** Definimos los términos por parejas: para $m\in\mathbb N$
$$
a_{2m}=\frac1{m!},\qquad a_{2m-1}=\Bigl(1+\frac1{2m-1}\Bigr)\frac1{m!}.
$$
Todos los términos son positivos.

*Cocientes.* Para $k=2m-1$ impar:
$$
\frac{a_k}{a_{k+1}}=\frac{a_{2m-1}}{a_{2m}}=1+\frac1{2m-1}=1+\frac1k,
$$
es decir, $1<\frac{a_k}{a_{k+1}}\le1+\frac1k$. Así que el conjunto contiene todos los impares y por tanto es infinito; como subconjunto infinito de $\mathbb N$ es numerable.

*Convergencia.* $a_{2m-1}\le\frac2{m!}$ y $a_{2m}=\frac1{m!}$, luego toda suma parcial no supera a
$$
\sum_{m=1}^{\infty}\frac3{m!}<\infty
$$
(la serie $\sum\frac1{m!}$ converge por el problema 3.5). La serie es positiva con sumas parciales acotadas: converge por (F2). $\blacksquare$

(Para $k=2m$ par el cociente es $\frac{a_{2m}}{a_{2m+1}}=\frac{(m+1)(2m+1)}{2m+2}=m+\frac12>1+\frac1k$; tales $k$ no están en el conjunto, que es exactamente el de los impares.)

**Por qué funciona.** La idea es la misma que en 3.8: la serie está armada por parejas. Dentro de cada pareja fijamos nosotros el cociente: exactamente $1+\frac1k$, «como en la serie armónica». Entre parejas la serie cae muy deprisa (factorial), y eso asegura la convergencia. El criterio de Raabe solo ve un paso y en los pasos impares confunde la serie con la armónica.

La exigencia adicional $1<\frac{a_k}{a_{k+1}}$ excluye ejemplos baratos como 3.8, donde en los pasos «malos» los términos crecen. Aquí en los pasos malos los términos decrecen honradamente, pero no más rápido que los armónicos, y aun así de que haya infinitos de esos pasos no se sigue la divergencia. Conclusión: en el apartado 2) del criterio de Raabe la condición debe cumplirse para todos los índices a partir de alguno.

## Problema 4.6 (formas límite de los criterios)

**Enunciado.** $a_k>0$ para $k\ge N_0$; $C_k=\sqrt[k]{a_k}$, $D_k=\dfrac{a_k}{a_{k+1}}$, $R_k=k\Bigl(\dfrac{a_k}{a_{k+1}}-1\Bigr)$. Demostrar seis afirmaciones.

El recurso común: si $u_k\to L$ y $L<c$, entonces $u_k<c$ para todo $k$ suficientemente grande (definición de límite con $\varepsilon=c-L$); análogamente si $L>c$. Un límite da una desigualdad «a partir de cierto índice»: justo lo que exigen los criterios en forma no límite.

**1) $C_k\to L<1$ ⟹ converge.** Tomemos $q=\frac{1+L}2$, de modo que $L<q<1$. Existe $K\ge N_0$ tal que para $k>K$ se tiene $\sqrt[k]{a_k}<q$, es decir, $0<a_k<q^k$. La serie geométrica $\sum q^k$ converge; por comparación converge $\sum a_k$.

**2) $C_k\to L>1$ ⟹ diverge.** Para $k>K$ se tiene $\sqrt[k]{a_k}>1$, es decir, $a_k>1$. El término general no tiende a cero: divergencia por (F1).

**3) $D_k\to L<1$ ⟹ diverge.** Para $k>K$ se tiene $\frac{a_k}{a_{k+1}}<1$; por el problema 3.7, 2) la serie diverge.

**4) $D_k\to L>1$ ⟹ converge.** Tomemos $\beta=\frac{L-1}2>0$. Para $k>K$ se tiene $\frac{a_k}{a_{k+1}}>1+\beta$; por el problema 3.7, 1) la serie converge.

**5) $R_k\to L<1$ ⟹ diverge.** Para $k>K$ se tiene $R_k<1$, es decir, $\frac{a_k}{a_{k+1}}<1+\frac1k$; por el problema 3.9, 2) la serie diverge.

**6) $R_k\to L>1$ ⟹ converge.** Tomemos $\gamma=\frac{L-1}2>0$. Para $k>K$ se tiene $R_k>1+\gamma$, es decir, $\frac{a_k}{a_{k+1}}>1+\frac{1+\gamma}k$; por el problema 3.9, 1) la serie converge. $\blacksquare$

**Por qué funciona.** La forma límite es más cómoda en los cálculos (hay que hallar un solo límite), pero más débil que la no límite: exige que el límite exista. En los tres criterios el caso $L=1$ queda sin decidir, y no es un defecto de la demostración: con $L=1$ hay tanto convergencia como divergencia. Para Cauchy y d'Alembert: $\sum\frac1k$ y $\sum\frac1{k^2}$ dan ambas el límite $1$. Para Raabe: $\sum\frac1{k\ln k}$ y $\sum\frac1{k\ln^2k}$ dan ambas $R_k\to1$.

Cuidado con el sentido: aquí $D_k=\frac{a_k}{a_{k+1}}$ es el cociente del término anterior entre el siguiente, el inverso del habitual $\frac{a_{k+1}}{a_k}$. Por eso $D_k\to L<1$ significa que los términos **crecen** y la serie diverge, y $L>1$ significa convergencia; para $C_k$ es al revés. La restricción $L\ge0$ en los apartados 3) y 5) del enunciado no es esencial: la demostración solo usa $L<1$.

## Problema 4.7

**1) $a_k=\dfrac{\prod_{m=1}^k(2025+m)}{\prod_{m=1}^k(2m-1)}$: converge.**

Todos los $a_k>0$, y
$$
\frac{a_k}{a_{k+1}}=\frac{2(k+1)-1}{2025+(k+1)}=\frac{2k+1}{k+2026}\ \longrightarrow\ 2>1 .
$$
Por 4.6, 4) la serie converge. Sin límite: $\frac{2k+1}{k+2026}\ge\frac32$ equivale a $k\ge6076$, así que la condición 3.7, 1) se cumple con $\beta=\frac12$ para $n>6075$.

*Por qué funciona.* Numerador y denominador son productos de $k$ factores; los factores del numerador crecen como $m$, los del denominador como $2m$. A partir de $k=2026$ cada nuevo paso multiplica el término por un número menor que uno que tiende a $\frac12$: en la cola la serie se comporta como una progresión geométrica. Antes, para $k<2025$, los términos **crecen** (el cociente $\frac{a_{k+1}}{a_k}=\frac{k+2026}{2k+1}>1$) y alcanzan valores enormes, pero el comienzo de la serie no influye en la convergencia (F3).

**2) $b_k=\frac1k$ si $k$ es un cuadrado perfecto y $b_k=\frac1{k^2}$ en otro caso: converge.**

Todos los $b_k>0$. Estimamos una suma parcial separando los sumandos en dos clases. Los cuadrados $k=m^2\le n$ aportan $\sum\frac1{m^2}$; los demás, a lo sumo $\sum\frac1{k^2}$:
$$
S_n\le\sum_{m:\ m^2\le n}\frac1{m^2}+\sum_{k=1}^n\frac1{k^2}\le2\sum_{k=1}^\infty\frac1{k^2}\le4 .
$$
Aquí $\sum_{k\ge1}\frac1{k^2}\le1+\sum_{k\ge2}\frac1{k(k-1)}=2$. Las sumas parciales de una serie positiva están acotadas: converge por (F2).

*Por qué funciona.* Los términos «grandes» $\frac1k$ son escasos: hasta $n$ hay solo unos $\sqrt n$ cuadrados, y la suma de los términos grandes es otra vez $\sum\frac1{m^2}$. Aquí no funcionan ni d'Alembert ni Raabe: en el paso $k=m^2-1\to m^2$ el término crece ($\frac{b_k}{b_{k+1}}=\frac{m^2}{(m^2-1)^2}<1$ para $m\ge2$) infinitas veces, y en el paso $m^2\to m^2+1$ cae bruscamente. Los criterios de cocientes exigen un comportamiento regular de los términos consecutivos; el criterio de acotación de las sumas parciales no depende ni del orden ni de la regularidad.

**3)$^*$ $c_k=\dfrac{k^{k+\frac1k}}{\bigl(k+\frac1k\bigr)^k}$: diverge.**

Transformamos:
$$
c_k=k^{1/k}\cdot\frac{k^k}{\bigl(k+\frac1k\bigr)^k}=\frac{k^{1/k}}{\bigl(1+\frac1{k^2}\bigr)^k}.
$$
El numerador $k^{1/k}\ge1$. El denominador: de $1+t\le e^t$ se obtiene $\bigl(1+\frac1{k^2}\bigr)^k\le e^{1/k}\le e$. Así, $c_k\ge\frac1e$ para todo $k$: el término general no tiende a cero y la serie diverge por (F1).

*Por qué funciona.* A la vista, numerador y denominador son enormes, pero son casi iguales: $k+\frac1k$ difiere de $k$ en la cantidad relativa $\frac1{k^2}$, y elevar a la potencia $k$ la convierte en $\frac1k\to0$ (haría falta una potencia del orden de $k^2$ para un efecto finito, como en $(1+\frac1n)^n\to e$). De hecho $c_k\to1$.

**Respuesta.** $\sum a_k$ y $\sum b_k$ convergen, $\sum c_k$ diverge.

## Problema 4.8

**La serie $a_k=\dfrac{\sqrt{k+1}-\sqrt{k-1}}{k^\alpha}$: converge para $\alpha>\frac12$, diverge para $\alpha\le\frac12$.**

Multiplicamos y dividimos por el conjugado:
$$
\sqrt{k+1}-\sqrt{k-1}=\frac{2}{\sqrt{k+1}+\sqrt{k-1}},\qquad a_k=\frac{C_k}{k^{\alpha+\frac12}},\quad C_k=\frac{2\sqrt k}{\sqrt{k+1}+\sqrt{k-1}} .
$$
Estimamos $C_k$: el denominador es mayor que $\sqrt k$ y no mayor que $2\sqrt{k+1}\le2\sqrt{2k}$, luego
$$
\frac1{\sqrt2}\le C_k<2\qquad\text{para todo }k\in\mathbb N .
$$
Por el problema 3.11 (con exponente $\alpha+\frac12$) la serie converge si y solo si $\alpha+\frac12>1$.

*Por qué funciona.* Una diferencia de raíces es un ejemplo de «pérdida de orden»: cada raíz es del orden de $\sqrt k$, pero su diferencia es del orden de $\frac1{\sqrt k}$ (es el incremento de $\sqrt x$ en un intervalo de longitud $2$, aproximadamente $2\cdot\frac1{2\sqrt k}$). Por eso el término es del orden de $k^{-\alpha-1/2}$, no de $k^{\frac12-\alpha}$. Multiplicar por el conjugado hace explícito ese orden.

**La serie $b_k=\dfrac{\beta^kk!}{k^k}$: converge para $0<\beta<e$, diverge para $\beta\ge e$.**

Todos los $b_k>0$ y
$$
\frac{b_k}{b_{k+1}}=\frac{\beta^kk!}{k^k}\cdot\frac{(k+1)^{k+1}}{\beta^{k+1}(k+1)!}=\frac1\beta\Bigl(1+\frac1k\Bigr)^k\ \longrightarrow\ \frac e\beta .
$$

- $\beta<e$: el límite es mayor que $1$, la serie converge por 4.6, 4).
- $\beta>e$: el límite es menor que $1$, la serie diverge por 4.6, 3).
- $\beta=e$: el límite vale $1$, la forma límite no sirve. Pero la sucesión $\bigl(1+\frac1k\bigr)^k$ crece estrictamente hacia $e$, luego $\bigl(1+\frac1k\bigr)^k<e$ y
$$
\frac{b_k}{b_{k+1}}=\frac1e\Bigl(1+\frac1k\Bigr)^k<1\qquad\text{para todo }k .
$$
Por la forma no límite 3.7, 2) la serie diverge: los términos crecen, $b_k\ge b_1=e$, y no tienden a cero.

*Por qué funciona.* Por la fórmula de Stirling $k!\approx\sqrt{2\pi k}\,\bigl(\frac ke\bigr)^k$, de modo que $b_k\approx\sqrt{2\pi k}\,\bigl(\frac\beta e\bigr)^k$: en esencia una progresión geométrica de razón $\frac\beta e$, de ahí la frontera $\beta=e$. En la propia frontera queda el factor $\sqrt{2\pi k}\to\infty$. El caso $\beta=e$ muestra para qué sirve la forma no límite: el límite vale uno, pero la desigualdad $\frac{b_k}{b_{k+1}}\le1$ se cumple exactamente, y no hizo falta la fórmula de Stirling.

**Respuesta.** $\sum a_k$ converge para $\alpha>\frac12$ (con cualquier $\beta$), $\sum b_k$ converge para $\beta<e$ (con cualquier $\alpha$).

## Problema 4.9

En las cuatro series los términos son positivos y $D_k=\frac{a_k}{a_{k+1}}\to1$, con $D_k>1$ para todo $k$. Por tanto **el criterio de d'Alembert no es aplicable**: la condición de divergencia $D_k\le1$ no se cumple para ningún $k$, y la de convergencia $D_k\ge1+\beta$ con $\beta>0$ constante falla para $k$ grande (si no, el límite sería al menos $1+\beta$). Funciona Raabe.

**$a_k=\dfrac{1}{k\ln((k+1)!)}$: converge.** Como $\ln((k+2)!)=\ln((k+1)!)+\ln(k+2)$,
$$
\frac{a_k}{a_{k+1}}=\frac{(k+1)\ln((k+2)!)}{k\ln((k+1)!)}=\Bigl(1+\frac1k\Bigr)\Bigl(1+\frac{\ln(k+2)}{\ln((k+1)!)}\Bigr).
$$
De $(k+1)!\le(k+1)^{k+1}$ se sigue $\ln((k+1)!)\le(k+1)\ln(k+1)<(k+1)\ln(k+2)$, es decir, el segundo paréntesis es mayor que $1+\frac1{k+1}$:
$$
\frac{a_k}{a_{k+1}}>\frac{k+1}k\cdot\frac{k+2}{k+1}=1+\frac2k=1+\frac{1+\gamma}k,\qquad\gamma=1 .
$$
Por 3.9, 1) la serie converge. (Que $D_k\to1$: $(k+1)!\ge2^k$, luego $\frac{\ln(k+2)}{\ln((k+1)!)}\le\frac{\ln(k+2)}{k\ln2}\to0$.)

**$b_k=\dfrac{(2k)!}{(k!)^2\,4^k}$: diverge.**
$$
\frac{b_k}{b_{k+1}}=\frac{(2k)!}{(k!)^24^k}\cdot\frac{((k+1)!)^24^{k+1}}{(2k+2)!}=\frac{4(k+1)^2}{(2k+1)(2k+2)}=\frac{2k+2}{2k+1}=1+\frac1{2k+1}\le1+\frac1k .
$$
Por 3.9, 2) la serie diverge. ($R_k=\frac{k}{2k+1}\to\frac12<1$.)

**$c_k=\dfrac{4^k}{(k+1)\,C_{2k}^k}$: diverge.** Nótese que $c_k=\dfrac{1}{(k+1)\,b_k}$, luego
$$
\frac{c_k}{c_{k+1}}=\frac{k+2}{k+1}\cdot\frac{b_{k+1}}{b_k}=\frac{(k+2)(2k+1)}{(k+1)(2k+2)}=1+\frac{k}{2(k+1)^2}\le1+\frac1{2k}\le1+\frac1k .
$$
Por 3.9, 2) la serie diverge. ($R_k=\frac{k^2}{2(k+1)^2}\to\frac12<1$.)

**$d_k=\dfrac{(2k+16)!!}{(2k+19)!!}$: converge.** Por definición $(2k+16)!!=\prod_{m=1}^{k+8}2m$ y $(2k+19)!!=\prod_{m=1}^{k+10}(2m-1)$. Al pasar de $k$ a $k+1$ el numerador se multiplica por $2k+18$ y el denominador por $2k+21$:
$$
\frac{d_k}{d_{k+1}}=\frac{2k+21}{2k+18}=1+\frac{3}{2k+18},\qquad R_k=\frac{3k}{2k+18}\to\frac32>1 .
$$
Por 4.6, 6) la serie converge. Sin límite: $\frac3{2k+18}\ge\frac{5/4}{k}$ equivale a $k\ge45$, así que la condición 3.9, 1) se cumple con $\gamma=\frac14$ para $n>44$.

**Respuesta.** $\sum a_k$ y $\sum d_k$ convergen, $\sum b_k$ y $\sum c_k$ divergen.

**Por qué funciona.** El criterio de Raabe lee el exponente en la asintótica $a_k\sim\frac{\mathrm{const}}{k^p}$: si $\frac{a_k}{a_{k+1}}=1+\frac pk+\dots$, entonces $R_k\to p$. Aquí:

- $b_k=C_{2k}^k/4^k$ es la probabilidad de volver al cero tras $2k$ pasos de un paseo aleatorio simétrico, $b_k\sim\frac1{\sqrt{\pi k}}$, $p=\frac12$: divergencia;
- $c_k=\frac1{(k+1)b_k}\sim\frac{\sqrt\pi}{\sqrt k}$, otra vez $p=\frac12$: divergencia;
- $d_k$: el cociente de dobles factoriales «se come» un factor y medio, $d_k\sim\frac{\mathrm{const}}{k^{3/2}}$, $p=\frac32$: convergencia;
- $a_k\sim\frac1{k^2\ln k}$, $R_k\to2$: convergencia (se ve también más fácil: $\ln((k+1)!)\ge k\ln2$, luego $a_k\le\frac{1}{k^2\ln2}$).

El criterio de d'Alembert solo distingue el comportamiento exponencial ($a_k\approx q^k$) y con decrecimiento potencial siempre da $D_k\to1$.

## Problema 4.10 (criterio integral de Cauchy)

**Enunciado.** $f\colon[1;+\infty)\to\mathbb R$; en $[N_0;+\infty)$ la función $f$ es no creciente y no negativa; $f$ es integrable en cada $[N_0;x]$. Demostrar: la serie $\sum_{k=1}^\infty f(k)$ converge $\iff$ existe el límite finito $\lim_{x\to+\infty}I_f(x)$, donde $I_f(x)=\int_{N_0}^xf(y)\,dy$.

**Demostración.** *Paso 1: la desigualdad básica.* Sea $k\ge N_0$ entero. Para $y\in[k;k+1]$ la monotonía da $f(k+1)\le f(y)\le f(k)$. Integrando en un intervalo de longitud $1$:
$$
f(k+1)\le\int_k^{k+1}f(y)\,dy\le f(k).\tag{2}
$$
Sumando (2) para $k=N_0,\dots,n-1$ (aditividad de la integral) se obtiene, para enteros $n>N_0$,
$$
\sum_{k=N_0+1}^{n}f(k)\ \le\ I_f(n)\ \le\ \sum_{k=N_0}^{n-1}f(k).\tag{3}
$$

*Paso 2: $I_f$ es no decreciente.* Para $N_0\le x_1<x_2$ se tiene $I_f(x_2)-I_f(x_1)=\int_{x_1}^{x_2}f\ge0$, pues $f\ge0$.

*a) ⟹ b).* Supongamos que la serie converge. Entonces converge su cola (F3); sea $A=\sum_{k=N_0}^\infty f(k)$. Los términos de la cola son no negativos, así que sus sumas parciales no superan a $A$. Para cualquier $x\ge N_0$ tomemos un entero $n>x$; por el paso 2 y el segundo miembro de (3)
$$
I_f(x)\le I_f(n)\le\sum_{k=N_0}^{n-1}f(k)\le A .
$$
La función $I_f$ es no decreciente y acotada superiormente, luego existe el límite finito $\lim_{x\to+\infty}I_f(x)=\sup I_f$.

*b) ⟹ a).* Sea $I=\lim_{x\to+\infty}I_f(x)$ finito. Como $I_f$ es no decreciente, $I_f(n)\le I$ para todo $n$. Por el primer miembro de (3)
$$
\sum_{k=N_0+1}^nf(k)\le I_f(n)\le I .
$$
Las sumas parciales de la serie no negativa $\sum_{k>N_0}f(k)$ están acotadas, converge por (F2); por (F3) converge $\sum_{k\ge1}f(k)$. $\blacksquare$

**Por qué funciona.** La desigualdad (2) es un dibujo: bajo la gráfica de una función decreciente en $[k;k+1]$ cabe un rectángulo de altura $f(k+1)$, y la propia gráfica cabe en un rectángulo de altura $f(k)$. La suma de la serie es el área de una figura escalonada, y difiere del área bajo la gráfica en a lo sumo un escalón $f(N_0)$. Por eso el área y la suma son finitas o infinitas a la vez.

Dónde se usa cada hipótesis: la monotonía, en (2) (sin ella los valores en los enteros no dicen nada de la función entre ellos: $f(x)=\sin^2(\pi x)$ da una serie nula y una integral divergente); la no negatividad, en la monotonía de $I_f$ y en (F2); la integrabilidad, para que $I_f$ esté definida. Las hipótesis solo hacen falta a partir de cierto $N_0$, porque la convergencia es una propiedad de la cola. El criterio convierte una pregunta sobre una serie en una pregunta sobre una integral, que a menudo se calcula explícitamente: así se obtienen $\sum\frac1{k^\alpha}$ (converge para $\alpha>1$) y $\sum\frac{1}{k\ln^\alpha k}$ (converge para $\alpha>1$).

## Problema 4.11 (criterio de Leibniz)

**Enunciado.** Para todo $k$: $a_ka_{k+1}<0$ y $|a_{k+1}|\le|a_k|$; $a_k\to0$. Demostrar que $\sum a_k$ converge. $^*$ ¿Sigue siendo cierto con la condición $a_ka_{k+1}\le0$?

**Demostración.** De $a_ka_{k+1}<0$ se sigue que todos los $a_k\ne0$ y que términos consecutivos tienen signos opuestos. Podemos suponer $a_1>0$ (si no, consideramos $\sum(-a_k)$: cumple las mismas hipótesis y converge a la vez que la serie original). Entonces por inducción $a_{2j-1}>0$, $a_{2j}<0$ para todo $j$, y
$$
a_{2j-1}+a_{2j}=|a_{2j-1}|-|a_{2j}|\ge0,\qquad a_{2j}+a_{2j+1}=-|a_{2j}|+|a_{2j+1}|\le0 .
$$

*Las sumas parciales pares son no decrecientes y no negativas:*
$$
S_{2m}=\sum_{j=1}^m(a_{2j-1}+a_{2j})\ge0,\qquad S_{2m+2}-S_{2m}=a_{2m+1}+a_{2m+2}\ge0 .
$$

*Las sumas parciales pares están acotadas superiormente:* reagrupando de otro modo,
$$
S_{2m}=a_1+\sum_{j=1}^{m-1}(a_{2j}+a_{2j+1})+a_{2m}\le a_1,
$$
pues cada paréntesis es no positivo y $a_{2m}<0$.

La sucesión monótona y acotada $(S_{2m})$ converge: $S_{2m}\to S\in[0;a_1]$.

*Las sumas parciales impares:* $S_{2m+1}=S_{2m}+a_{2m+1}\to S+0=S$, pues $a_k\to0$.

Las dos subsucesiones $(S_{2m})$ y $(S_{2m+1})$, que juntas agotan todos los índices, convergen al mismo número $S$; luego $S_n\to S$. $\blacksquare$

**Respuesta a la pregunta con asterisco: sí, la afirmación sigue siendo cierta.** Sea $a_ka_{k+1}\le0$ para todo $k$.

- Si todos los $a_k\ne0$, entonces $a_ka_{k+1}<0$, y es el caso ya demostrado.
- Si $a_K=0$ para algún $K$, de $|a_{k+1}|\le|a_k|$ se sigue por inducción $a_k=0$ para todo $k\ge K$. La serie tiene un número finito de términos no nulos, $S_n=S_K$ para $n\ge K$, y converge.

**Por qué funciona.** Las sumas parciales de una serie alternada con módulos decrecientes «saltan» alrededor del límite: un paso hacia arriba, un paso menor hacia abajo, un paso aún menor hacia arriba. Las sumas pares forman una sucesión creciente, las impares una decreciente, y todas las pares quedan por debajo de todas las impares: se obtienen intervalos encajados $[S_{2m};S_{2m+1}]$. Sus longitudes $a_{2m+1}$ tienden a cero; de ahí el límite común. De paso sale la estimación del resto $|S-S_n|\le|a_{n+1}|$.

Papel de las hipótesis: la monotonía de los módulos da el encaje, $a_k\to0$ da la contracción. Sin monotonía la afirmación es falsa: la serie $1-\frac12+\frac12-\frac14+\frac13-\frac18+\dots$ (términos positivos $\frac1m$, negativos $-\frac1{2^m}$) es alternada, sus términos tienden a cero, pero diverge, porque la parte positiva es la serie armónica y la negativa converge.

## Problema 4.12

**Enunciado.** $\alpha>0$. Usando el problema 4.11, demostrar la convergencia de seis series.

Observación auxiliar (Z): **insertar ceros no influye en la convergencia.** Si la serie $\sum c_j$ converge a $T$ y la serie $\sum a_k$ se obtiene de ella insertando términos nulos (conservando el orden), entonces cada suma parcial $S_n$ de $\sum a_k$ es una suma parcial $T_{j(n)}$ de $\sum c_j$, donde $j(n)$ es el número de lugares no nulos hasta $n$; $j(n)\to\infty$, luego $S_n\to T$.

**1) $\sum\dfrac{(-1)^k}{k^\alpha}$.** $a_ka_{k+1}=-\frac{1}{k^\alpha(k+1)^\alpha}<0$; $|a_{k+1}|=\frac1{(k+1)^\alpha}\le\frac1{k^\alpha}=|a_k|$, pues $\alpha>0$; $|a_k|=k^{-\alpha}\to0$. Por 4.11 la serie converge. $\blacksquare$

**2) $\sum\dfrac{\cos\frac{k\pi}2}{\sqrt k}$.** Para $k$ impar, $\cos\frac{k\pi}2=0$; para $k=2j$, $\cos(j\pi)=(-1)^j$. La serie tiene la forma
$$
0-\frac1{\sqrt2}+0+\frac1{\sqrt4}+0-\frac1{\sqrt6}+\dots
$$
4.11 no se aplica directamente: $a_ka_{k+1}=0$, y los módulos no son monótonos ($|a_1|=0<|a_2|$). Pero la serie se obtiene insertando ceros en $\sum_{j\ge1}c_j$, $c_j=\dfrac{(-1)^j}{\sqrt{2j}}$, para la cual $c_jc_{j+1}<0$, $|c_j|$ decrece y tiende a cero. Por 4.11 la serie $\sum c_j$ converge, y por (Z) también la original ($S_{2m}=S_{2m+1}=T_m$). $\blacksquare$

**3) $\sum\dfrac{\sin\frac{k\pi}2}{\ln(k+2026)}$.** Para $k$ par, $\sin\frac{k\pi}2=0$; para $k=2j-1$, $\sin\bigl(j\pi-\frac\pi2\bigr)=(-1)^{j-1}$. Los términos no nulos son $c_j=\dfrac{(-1)^{j-1}}{\ln(2j+2025)}$. Alternan de signo, $|c_j|$ decrece (el logaritmo crece) y tiende a cero. Por 4.11 y (Z) la serie converge ($S_{2m-1}=S_{2m}=T_m$). $\blacksquare$

**4)$^*$ $\sum\dfrac{(-1)^kk^{10}}{3^k}$.** Los signos alternan. El cociente de módulos es
$$
\frac{|a_{k+1}|}{|a_k|}=\frac13\Bigl(1+\frac1k\Bigr)^{10}.
$$
Decrece con $k$; para $k=8$ vale $\frac13\bigl(\frac98\bigr)^{10}\approx1{,}08>1$, para $k=9$ es $q=\frac13\bigl(\frac{10}9\bigr)^{10}\approx0{,}956<1$. Así que los módulos son no crecientes solo a partir de $k=9$, y los nueve primeros términos crecen en módulo. Aplicamos 4.11 a la cola $c_j=a_{j+8}$, $j\ge1$: $c_jc_{j+1}<0$; $|c_{j+1}|\le q|c_j|\le|c_j|$; $|c_j|\le|c_1|q^{j-1}\to0$. Por 4.11 converge $\sum c_j=\sum_{k\ge9}a_k$, y por (F3) la serie original. $\blacksquare$

**5)$^{**}$ $\sum\ln\Bigl(1+\dfrac{(-1)^{k+1}}{k}\Bigr)$.** Escribamos los términos:

- $k$ impar: $a_k=\ln\bigl(1+\frac1k\bigr)>0$;
- $k$ par: $a_k=\ln\bigl(1-\frac1k\bigr)=\ln\frac{k-1}{k}=-\ln\bigl(1+\frac1{k-1}\bigr)<0$.

Los signos alternan. Módulos: $|a_k|=\ln\bigl(1+\frac1k\bigr)$ para $k$ impar y $|a_k|=\ln\bigl(1+\frac1{k-1}\bigr)$ para $k$ par. Comprobamos la monotonía:

- $k$ impar: $|a_{k+1}|=\ln\bigl(1+\frac1k\bigr)=|a_k|$;
- $k$ par: $|a_{k+1}|=\ln\bigl(1+\frac1{k+1}\bigr)<\ln\bigl(1+\frac1{k-1}\bigr)=|a_k|$.

Por último, $|a_k|\le\ln\bigl(1+\frac1{k-1}\bigr)\to0$. Por 4.11 la serie converge. $\blacksquare$

Más aún, $a_{2j-1}+a_{2j}=\ln\frac{2j}{2j-1}+\ln\frac{2j-1}{2j}=0$, luego $S_{2m}=0$ y la suma de la serie es $0$.

**6)$^{**}$ $\sum\dfrac{\sin\bigl(\frac\pi4+\frac{k\pi}2\bigr)}{k}$.** El numerador: para $k=2j$, $\sin\bigl(\frac\pi4+j\pi\bigr)=(-1)^j\frac{\sqrt2}2$; para $k=2j+1$, $\sin\bigl(\frac\pi4+\frac\pi2+j\pi\bigr)=(-1)^j\cos\frac\pi4=(-1)^j\frac{\sqrt2}2$. Los signos de los términos:
$$
+\ -\ -\ +\ +\ -\ -\ +\ +\ \dots
$$
No cambian en cada paso sino cada dos: $a_2a_3>0$, y 4.11 no se aplica directamente. Agrupamos los términos en parejas del mismo signo: para $j\ge1$
$$
c_j=a_{2j}+a_{2j+1}=(-1)^j\frac{\sqrt2}2\Bigl(\frac1{2j}+\frac1{2j+1}\Bigr).
$$
Para la serie $\sum c_j$: los signos alternan, $|c_j|$ decrece, $|c_j|\to0$. Por 4.11 converge, digamos a $T$. Volvemos a la serie original:
$$
S_{2m+1}=a_1+\sum_{j=1}^mc_j\to a_1+T,\qquad S_{2m}=S_{2m+1}-a_{2m+1}\to a_1+T,
$$
pues $a_k\to0$. Ambas subsucesiones de sumas parciales convergen al mismo límite: la serie converge. $\blacksquare$

**Por qué funciona.** En los seis ejemplos la convergencia es condicional o «casi» condicional y descansa en la cancelación de términos vecinos, no en la pequeñez de los módulos (en 1) para $\alpha\le1$, y en 2), 3), 6), la serie de los módulos diverge). El criterio de Leibniz exige tres cosas, y cada ejemplo pone a prueba una:

- 2), 3): los ceros de la serie rompen la alternancia estricta formalmente, pero no en el fondo: se pueden quitar;
- 4): la monotonía puede empezar no desde el primer término; basta la cola (por cierto, esta serie también converge absolutamente, por d'Alembert);
- 5): la monotonía de los módulos es no estricta, los términos van en parejas de igual módulo; por eso en la hipótesis de 4.11 figura $\le$ y no $<$;
- 6): la alternancia con período $4$ se reduce a la habitual agrupando. Los términos de una serie convergente siempre se pueden agrupar, pero el paso inverso (de la convergencia de la serie agrupada a la de la original) es legítimo solo porque $a_k\to0$ y cada grupo tiene un número acotado de términos.

En 6) se puede prescindir de la agrupación: $\sin\bigl(\frac\pi4+\frac{k\pi}2\bigr)=\frac{\sqrt2}2\bigl(\sin\frac{k\pi}2+\cos\frac{k\pi}2\bigr)$, así que la serie es suma de dos series convergentes de los tipos 2) y 3) con denominador $k$.
