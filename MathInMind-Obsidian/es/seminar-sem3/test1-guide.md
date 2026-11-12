---
title: "Seminario NM-204. Control 1 — cómo prepararse"
lang: es
tags: [mathinmind/es, mathinmind/other]
---
# Control 1: cómo prepararse

[[ru/seminar-sem3/test1-guide|Русский]] · [[en/seminar-sem3/test1-guide|English]] · **Español**

[[es/seminar-sem3/index|Todas las tareas]] · [[es/seminar-sem3/test1-variants|Variantes de práctica →]]

> [!note] Qué es esto
> Un plan de preparación para el control 1 basado en las tareas 1–4. La estructura del control es la que se ha comunicado: cuatro ejercicios, apartados **1.1, 1.2, 2.1, 2.2, 3, 4**; los ejercicios 1 y 2 tratan de la fórmula de Taylor y los extremos, los ejercicios 3 y 4 de series. No existen variantes reales: los tipos de problemas de abajo son un pronóstico a partir de las tareas, no una filtración. El reparto de temas por apartados es una suposición.

## Estructura probable

| Apartado | Qué preguntarán probablemente | Prototipos en las tareas |
|---|---|---|
| 1.1 | Desarrollar un polinomio por la fórmula de Taylor en un punto dado (suma finita) | [[es/seminar-sem3/hw1-taylor\|1.1, 1.2]] |
| 1.2 | Desarrollo de una función no polinómica hasta grado 2 o 3 con resto de Lagrange | [[es/seminar-sem3/hw1-taylor\|1.3, 1.4]] |
| 2.1 | Extremo condicionado en el que la ligadura se despeja explícitamente (recta, plano) | [[es/seminar-sem3/hw2-conditional-extremum\|2.1, 2.3]] |
| 2.2 | Extremo condicionado sobre un compacto por el método de Lagrange (elipsoide, circunferencia) | [[es/seminar-sem3/hw2-conditional-extremum\|2.2, 2'.1]] |
| 3 | Una demostración: un criterio o una propiedad de las series | [[es/seminar-sem3/hw3-numerical-series\|3.1–3.9]], [[es/seminar-sem3/hw4-series-inequalities-bases\|4.4, 4.6, 4.10, 4.11]] |
| 4 | Estudiar la convergencia de 2–3 series concretas | [[es/seminar-sem3/hw3-numerical-series\|3.11]], [[es/seminar-sem3/hw4-series-inequalities-bases\|4.7–4.9, 4.12]] |

Menos probable, pero posible: problemas con parámetro ([[es/seminar-sem3/hw2-conditional-extremum|2'.2, 2'.3]], [[es/seminar-sem3/hw4-series-inequalities-bases|4.8]]), la desigualdad de Hölder ([[es/seminar-sem3/hw4-series-inequalities-bases|4.1, 4.2]]), ejemplos y contraejemplos ([[es/seminar-sem3/hw3-numerical-series|3.8, 3.10]], [[es/seminar-sem3/hw4-series-inequalities-bases|4.5]]), bases ([[es/seminar-sem3/hw4-series-inequalities-bases|4.3]]).

## Ejercicio 1: fórmula de Taylor

**Qué saber de memoria.**
$$
f(a+h)=\sum_{k=0}^{s}\frac{d_a^kf(h)}{k!}+\frac{d_c^{s+1}f(h)}{(s+1)!},\qquad c=a+\theta h,\ \theta\in(0,1),
$$
$$
d^kf(h)=\sum_{|\alpha|=k}\frac{k!}{\alpha!}\,\partial^\alpha f\cdot h^\alpha .
$$
Para dos variables: $d^2f=f_{xx}h_1^2+2f_{xy}h_1h_2+f_{yy}h_2^2$, $d^3f=f_{xxx}h_1^3+3f_{xxy}h_1^2h_2+3f_{xyy}h_1h_2^2+f_{yyy}h_2^3$. Para tres variables los coeficientes de $d^3f$ son $1$ (puras), $3$ (de la forma $\partial_i^2\partial_j$) y $6$ (para $f_{xyz}$).

**Método para un polinomio (apartado 1.1).**

1. Introducir $h_1=x-a_1$, $h_2=y-a_2$, …
2. O bien sustituir $x=a_1+h_1$, … y abrir paréntesis, o bien calcular las derivadas en el punto y reunir $d^kf/k!$.
3. Escribir que la suma se corta en el grado del polinomio: todas las derivadas de orden superior son nulas, el resto es cero, la igualdad es exacta.
4. Comprobación: la parte homogénea superior debe coincidir con la parte superior del polinomio original; sustituir un $h$ sencillo (por ejemplo $(1,0)$) en ambos miembros.

**Método para el resto de Lagrange (apartado 1.2).**

1. Calcular el valor y las derivadas hasta orden $s$ en $a$: eso da el polinomio.
2. Calcular **todas** las derivadas de orden $s+1$ en forma general (¡no en $a$!).
3. Escribir el resto: $\frac1{(s+1)!}d^{s+1}f$ con las derivadas en $c=(a_1+\theta h_1,\dots)$, y escribir obligatoriamente «$\theta\in(0,1)$».
4. Si la función es una composición $e^{u}$, $\ln u$, $\sin u$ con un polinomio $u$, es más rápido trabajar con $F(t)=f(a+th)$: $F^{(k)}(0)/k!$ son los términos del desarrollo, $F^{(s+1)}(\theta)/(s+1)!$ es el resto (así está resuelto el [[es/seminar-sem3/hw1-taylor|problema 1.3]]).

**Errores típicos.**

- Se olvida el factor $\frac1{k!}$ o el coeficiente multinomial ($2$ para $f_{xy}$, $3$ para $f_{xxy}$, $6$ para $f_{xyz}$).
- El resto se escribe en $a$ y no en el punto intermedio $c$; no se indica $\theta\in(0,1)$.
- Se confunde el resto de Lagrange con el de Peano $o(|h|^s)$: «en forma de Lagrange» pide la expresión explícita.
- La respuesta se deja en $x,y$ sin decir qué es $h$.

## Ejercicio 2: extremos

**Qué saber.**

- Condición necesaria de extremo libre: $\nabla f=0$. Suficiente: el signo de $d^2f$ (definida positiva, mínimo; definida negativa, máximo; indefinida, no hay extremo; semidefinida, el criterio calla).
- Criterio de Sylvester para $2\times2$: $\Delta_1=f_{xx}$, $\Delta_2=f_{xx}f_{yy}-f_{xy}^2$. $\Delta_2>0,\ \Delta_1>0$: mínimo; $\Delta_2>0,\ \Delta_1<0$: máximo; $\Delta_2<0$: silla; $\Delta_2=0$: estudiar a mano.
- Extremo condicionado: $L=f-\sum\lambda_j\varphi_j$, el sistema $\nabla L=0$ más las ecuaciones de ligadura; la condición suficiente es el signo de $d^2L$ **sobre el espacio tangente** $\{h:\ d\varphi_j(h)=0\}$.

**Método cuando la ligadura se despeja explícitamente (apartado 2.1).**

1. Parametrizar $M$ (por ejemplo, $y=x$) y obtener una función $g$ de menos variables.
2. Hallar los puntos estacionarios de $g$ y estudiarlos con la diferencial segunda.
3. Si la diferencial segunda es degenerada, mirar directamente el signo del incremento (como en [[es/seminar-sem3/hw2-conditional-extremum|2.3]]: el sumando $2x^3$ cambia de signo, no hay extremo).
4. Volver a las coordenadas originales; indicar el tipo (máximo o mínimo, estricto o no, local o global) y el valor.

**El método de Lagrange (apartado 2.2).**

1. Comprobar la regularidad: los gradientes de las ligaduras son linealmente independientes sobre $M$ (normalmente «se anulan solo en un punto que no está en $M$»).
2. Resolver el sistema de Lagrange. No dividir por una expresión que pueda ser cero sin tratar ese caso: escribir $(x-y)(z+2\lambda)=0$ y estudiar ambas alternativas.
3. Determinar el tipo de los puntos. La vía más rápida cuando $M$ es compacto (esfera, elipsoide, circunferencia): «$f$ es continua sobre un compacto, luego alcanza sus valores máximo y mínimo, y se alcanzan en puntos estacionarios»; después, comparar los valores.
4. Escribir la respuesta: puntos, tipo, valores extremos.

**Errores típicos.**

- Se declara extremo un punto estacionario sin comprobarlo (el sistema de Lagrange es solo una condición necesaria).
- $d^2L$ se estudia en todo el espacio y no en el tangente.
- Se pierden soluciones al dividir; se pierde el segundo punto de signo opuesto.
- El argumento de compacidad se aplica a un $M$ no compacto (recta, plano): allí puede no haber valor máximo.
- No se comprueba la regularidad de las ligaduras.

## Ejercicio 3: demostraciones sobre series

**Tres hechos de los que se deduce casi todo** (con detalle al comienzo de la [[es/seminar-sem3/hw3-numerical-series|tarea 3]]):

1. condición necesaria: la serie converge ⟹ $a_k\to0$;
2. una serie de términos no negativos converge ⟺ sus sumas parciales están acotadas superiormente;
3. un número finito de términos no influye en la convergencia.

**Qué saber demostrar con el cuaderno cerrado** (por orden decreciente de probabilidad):

| Afirmación | Idea clave en una línea | Dónde |
|---|---|---|
| Una serie convergente tiene sumas parciales acotadas | toda sucesión convergente está acotada | [[es/seminar-sem3/hw3-numerical-series\|3.1]] |
| Criterio de comparación generalizado | $\frac{a_n}{b_n}$ es no creciente ⟹ $a_n\le Cb_n$ | [[es/seminar-sem3/hw3-numerical-series\|3.4]] |
| Criterio de Kummer | multiplicar por $a_{n+1}$, sumar, la suma es telescópica | [[es/seminar-sem3/hw3-numerical-series\|3.6]] |
| Criterio de d'Alembert | Kummer con $x_n=1$ | [[es/seminar-sem3/hw3-numerical-series\|3.7]] |
| Criterio de Raabe | Kummer con $x_n=n$ | [[es/seminar-sem3/hw3-numerical-series\|3.9]] |
| Raabe ⟹ d'Alembert | $1+\beta\ge1+\frac2n$ para $n\ge\frac2\beta$ | [[es/seminar-sem3/hw4-series-inequalities-bases\|4.4]] |
| Formas límite de los criterios | un límite ⟹ una desigualdad a partir de cierto índice | [[es/seminar-sem3/hw4-series-inequalities-bases\|4.6]] |
| Criterio de Leibniz | $S_{2m}$ es monótona y acotada, $S_{2m+1}=S_{2m}+a_{2m+1}$ | [[es/seminar-sem3/hw4-series-inequalities-bases\|4.11]] |
| Criterio integral | $f(k+1)\le\int_k^{k+1}f\le f(k)$ | [[es/seminar-sem3/hw4-series-inequalities-bases\|4.10]] |
| Acotación de las sumas $\sum\sin(kx_0)$ | multiplicar por $2\sin\frac{x_0}2$, suma telescópica | [[es/seminar-sem3/hw3-numerical-series\|3.2]] |
| $\sum\cos(kx_0)$ diverge | $\cos(2kx_0)=2\cos^2(kx_0)-1$, el término general no tiende a cero | [[es/seminar-sem3/hw3-numerical-series\|3.3]] |

**Los criterios en la notación del seminario.** Atención: en el seminario se usa el cociente $\dfrac{a_n}{a_{n+1}}$ (el anterior entre el siguiente), no $\dfrac{a_{n+1}}{a_n}$.

| Criterio | Converge si, a partir de cierto índice, | Diverge si, a partir de cierto índice, |
|---|---|---|
| Kummer | $x_n\frac{a_n}{a_{n+1}}-x_{n+1}\ge\alpha>0$ | $x_n\frac{a_n}{a_{n+1}}-x_{n+1}\le0$ y $\sum\frac1{x_n}$ diverge |
| d'Alembert | $\frac{a_n}{a_{n+1}}\ge1+\beta$, $\beta>0$ | $\frac{a_n}{a_{n+1}}\le1$ |
| Raabe | $\frac{a_n}{a_{n+1}}\ge1+\frac{1+\gamma}n$, $\gamma>0$ | $\frac{a_n}{a_{n+1}}\le1+\frac1n$ |
| Cauchy (forma límite) | $\sqrt[k]{a_k}\to L<1$ | $\sqrt[k]{a_k}\to L>1$ |
| Leibniz | los signos alternan, $\lvert a_k\rvert$ es no creciente, $a_k\to0$ | — |

**Cómo escribir una demostración para no perder puntos.**

- Nombrar explícitamente el índice a partir del cual vale la desigualdad y remitir a «un número finito de términos no influye».
- Antes de multiplicar o dividir una desigualdad, decir que el factor es positivo.
- Al final, nombrar el criterio usado: «las sumas parciales de una serie no negativa están acotadas, luego converge».

## Ejercicio 4: estudio de la convergencia de series

**Orden de actuación.**

1. **¿Tiende a cero el término general?** Si no, diverge; fin ([[es/seminar-sem3/hw4-series-inequalities-bases|4.7, 3)]]).
2. **¿De signo variable?** Comprobar Leibniz. Si la serie tiene ceros o los signos alternan por grupos, quitar los ceros o agrupar ([[es/seminar-sem3/hw4-series-inequalities-bases|4.12]]).
3. **¿Factoriales, potencias $q^k$, $k^k$?** Calcular $\frac{a_k}{a_{k+1}}$. Límite mayor que $1$: converge; menor que $1$: diverge.
4. **¿El límite del cociente vale $1$?** D'Alembert no sirve. Calcular $R_k=k\bigl(\frac{a_k}{a_{k+1}}-1\bigr)$: límite mayor que $1$, converge; menor que $1$, diverge ([[es/seminar-sem3/hw4-series-inequalities-bases|4.9]]).
5. **¿Potencias, raíces, expresiones racionales en $k$?** Llevar a la forma $\frac{C_k}{k^\alpha}$ con $0<M_1\le C_k\le M_2$; converge ⟺ $\alpha>1$ ([[es/seminar-sem3/hw3-numerical-series|3.11]], [[es/seminar-sem3/hw4-series-inequalities-bases|4.8]]). Diferencia de raíces: multiplicar por el conjugado.
6. **¿Una potencia $k$-ésima completa?** Criterio de la raíz de Cauchy.
7. **¿Logaritmos de la forma $\frac1{k\ln^pk}$?** Criterio integral.
8. **¿Una serie irregular** (términos definidos a trozos)? Estimar directamente las sumas parciales ([[es/seminar-sem3/hw4-series-inequalities-bases|4.7, 2)]]).

**Series patrón.**

| Serie | Converge |
|---|---|
| $\sum q^k$ | para $\lvert q\rvert<1$ |
| $\sum\frac1{k^\alpha}$ | para $\alpha>1$ |
| $\sum\frac{1}{k\ln^pk}$ | para $p>1$ |
| $\sum\frac1{k(k+1)}$, $\sum\frac1{k!}$ | sí |
| $\sum\frac{(-1)^k}{k^\alpha}$ | para $\alpha>0$ (absolutamente para $\alpha>1$) |

**Límites y desigualdades útiles.** $\bigl(1+\frac1k\bigr)^k\uparrow e$, luego $\bigl(1+\frac1k\bigr)^k<e$ para todo $k$; $\sqrt[k]k\to1$; $1+t\le e^t$; $(1+x)^\alpha\ge1+\alpha x$ para $\alpha\ge1$, $x\ge0$; $\ln(k!)\le k\ln k$.

**Errores típicos.**

- El cociente al revés: con $\frac{a_k}{a_{k+1}}\to L$ la serie converge para $L>1$, no para $L<1$.
- La conclusión «el límite del cociente es $1$, luego diverge»: no, el criterio simplemente no se aplica.
- El criterio de Leibniz aplicado sin comprobar la monotonía de los módulos o habiendo términos nulos.
- «$a_k\to0$, luego converge»: la condición necesaria no es suficiente.
- Comparación $a_k\le b_k$ para series de signo variable: los criterios de comparación solo valen para las no negativas.
- El valor frontera de un parámetro no se trata aparte ($\beta=e$ en [[es/seminar-sem3/hw4-series-inequalities-bases|4.8]]).

## Plan de preparación

**Día 1: Taylor y extremos.**

1. Leer las secciones «La idea general» de la [[es/seminar-sem3/hw1-taylor|tarea 1]] y «Por qué funciona el método de Lagrange» de la [[es/seminar-sem3/hw2-conditional-extremum|tarea 2]].
2. Resolver de nuevo, sin mirar la solución, 1.2 y 1.4, y después 2.2 y 2'.1. Comparar.
3. Resolver los apartados 1.1, 1.2, 2.1, 2.2 de la [[es/seminar-sem3/test1-variants|variante A]] con tiempo: 40 minutos.

**Día 2: series.**

1. Aprender la tabla de criterios y los tres hechos básicos.
2. Por escrito, con el cuaderno cerrado, demostrar 3.4, 3.6, 3.7, 3.9, 4.11. Comparar con las soluciones.
3. Rehacer 4.7–4.9 y 4.12.
4. Resolver los ejercicios 3 y 4 de la [[es/seminar-sem3/test1-variants|variante A]]: 40 minutos.

**Día 3: ensayo.**

1. La [[es/seminar-sem3/test1-variants|variante B]] completa con tiempo (80–90 minutos); comprobar con las soluciones.
2. Analizar los errores y repasar los puntos correspondientes.
3. La [[es/seminar-sem3/test1-variants|variante C]] completa con tiempo.

## Autoevaluación antes del control

1. ¿Cuál es el coeficiente de $h_1h_2h_3$ en $d^3f(h)$?
2. ¿En qué punto se toman las derivadas del resto de Lagrange?
3. ¿Por qué el desarrollo de Taylor de un polinomio es una suma finita?
4. ¿Cuándo se puede decir «el punto estacionario es un máximo» sin calcular la diferencial segunda?
5. ¿Sobre qué vectores se estudia $d^2L$?
6. ¿Qué sucesión $x_n$ del criterio de Kummer da el criterio de Raabe?
7. ¿Qué afirma el criterio de Raabe para una serie con $\frac{a_n}{a_{n+1}}=1+\frac1{2n+1}$?
8. ¿Converge $\sum\frac{e^kk!}{k^k}$, y por qué la forma límite no ayuda aquí?
9. ¿Qué tres condiciones necesita el criterio de Leibniz?
10. Dé un ejemplo de serie divergente con sumas parciales acotadas.

> [!answer]- Respuestas
> 1. $6f_{xyz}$: el coeficiente multinomial $\frac{3!}{1!\,1!\,1!}$.
> 2. En el punto intermedio $c=a+\theta h$, $\theta\in(0,1)$.
> 3. Todas las derivadas de orden superior al grado del polinomio son nulas, así que el resto es cero.
> 4. Cuando el conjunto $M$ es compacto: el valor máximo se alcanza y tiene que alcanzarse en un punto estacionario; queda comparar los valores.
> 5. Sobre los tangentes: $d\varphi_j(h)=0$ para todas las ligaduras.
> 6. $x_n=n$.
> 7. Diverge: $1+\frac1{2n+1}\le1+\frac1n$.
> 8. Diverge. El límite del cociente es $1$, pero $\frac{a_k}{a_{k+1}}=\frac1e\bigl(1+\frac1k\bigr)^k<1$ para todo $k$: se aplica la forma no límite de d'Alembert.
> 9. Los signos alternan, los módulos son no crecientes, el término general tiende a cero.
> 10. $\sum(-1)^k$, o $\sum\cos(kx_0)$ para $x_0\notin2\pi\mathbb Z$.
