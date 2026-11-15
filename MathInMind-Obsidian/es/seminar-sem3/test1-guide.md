---
title: "Seminario NM-204. Control del 20 nov. — cómo prepararse"
lang: es
tags: [mathinmind/es, mathinmind/other]
---
# Control del 20 de noviembre de 2026: fórmula de Taylor y extremos condicionados

[[ru/seminar-sem3/test1-guide|Русский]] · [[en/seminar-sem3/test1-guide|English]] · **Español**

[[es/seminar-sem3/index|Todas las tareas]] · [[es/seminar-sem3/index#Apuntes de los seminarios|Apuntes de los seminarios]] · [[es/seminar-sem3/test1-variants|Variantes de práctica →]] · [[es/seminar-sem3/series-test-guide|Control de series]]

> [!note] Qué es esto
> La preparación para el control del 20 de noviembre de 2026 según la consulta. El formato ya se conoce: problema 1 (a — un polinomio, b — una función no polinómica con resto de Lagrange) y problema 2 (un extremo condicionado). Fuentes: los fotogramas de la pizarra de la consulta y un resumen de su grabación de audio ([`sem3_notes`, archivos 14](https://github.com/NikiHunter/matan/blob/main/sem3_notes/README.md), en ruso), los [[es/seminar-sem3/index#Apuntes de los seminarios|apuntes de los seminarios]] y las tareas 1–2. Todos los cálculos de abajo se comprobaron en sympy. En este control no habrá series: pasaron a un control aparte, que tiene [[es/seminar-sem3/series-test-guide|su propia página]].

## Qué habrá en el control

| Problema | Qué se da | Qué hay que hacer | Modelos |
|---|---|---|---|
| 1a | un polinomio: grado 4 en dos variables **o** grado 3 en tres; un punto $P$ | desarrollarlo por la fórmula de Taylor en $P$ completo; no hay resto | [[#Ejemplo 1'.1 (consulta): un polinomio de grado cuatro\|ejemplo 1'.1]], tareas [[es/seminar-sem3/hw1-taylor#Problema 1.1\|1.1]], [[es/seminar-sem3/hw1-taylor#Problema 1.2\|1.2]] |
| 1b | una $f\colon\mathbb R^3\to\mathbb R$ no polinómica (seno, coseno, exponencial, logaritmo, potencias); un punto $P$ | el desarrollo hasta orden dos con resto en forma de Lagrange; el resto en forma general | [[#^ex-1p-2\|ejemplo 1'.2]], tarea [[es/seminar-sem3/hw1-taylor#Problema 1.4\|1.4]] |
| 2 | $f\colon\mathbb R^3\to\mathbb R$, un conjunto $M=\{\varphi=0\}$ dado por una condición polinómica | hallar todos los puntos de extremo local condicionado y decir de cada uno: máximo, mínimo o sin extremo | [[#^ex-1p-3\|ejemplo 1'.3]], tarea [[es/seminar-sem3/hw2-conditional-extremum#Problema 2.1\|2.1]] |

**Qué prometió el profesor** (según la grabación de la consulta):

- en el problema 2 todos los menores que se comprueban son no nulos: no habrá el caso «el determinante es cero, hace falta un estudio adicional»;
- el problema 2 tiene a propósito un máximo, un mínimo y un punto sin extremo: si todos tus puntos salen extremos, busca un error;
- no habrá ecuaciones cúbicas para $\lambda$, solo cuadráticas o más sencillas (el ejemplo 1'.3 tenía una cúbica, con la raíz $\lambda=1$ elegida a propósito);
- en el problema 1b **no hace falta** la forma explícita de las derivadas de tercer orden en el resto; el resto se escribe en forma general;
- los valores de senos y cosenos serán sencillos: $0$, $1$ o $\pm\frac1{\sqrt2}$ (ángulos como $\frac\pi4$, $\frac{3\pi}4$, $\frac{5\pi}4$);
- la calculadora está prohibida. Se evalúa el razonamiento: una lógica correcta con un error aritmético recibe casi la nota máxima, y una solución que su autor no sabe explicar recibe cero en todo el examen (puede haber una comprobación oral).

**Qué no habrá.** Series: el problema de series de este control y el del siguiente se juntaron en un control aparte a finales de noviembre o principios de diciembre, junto con el problema «de signo constante» al que se dedicó mucho tiempo en los seminarios ([[es/seminar-sem3/series-test-guide|cómo prepararse]]). Las integrales paramétricas y lo demás posterior a las series van a un control pequeño a finales de diciembre.

## Problema 1: fórmula de Taylor

**La fórmula con la notación de la pizarra.** Para $P=(p_1;p_2;p_3)$, $X=(x;y;z)$ y $f$ continuamente diferenciable $N+1$ veces (en la pizarra, «$f\in C^\infty(\mathbb R^3)$»), para **cada** punto $X$ existe $t_0=t_0(X)\in(0;1)$ tal que
$$
f(X)=\sum_{|\alpha|\le N}\frac{D^{\alpha}f(P)}{\alpha!}\,(X-P)^{\alpha}+\sum_{|\alpha|=N+1}\frac{D^{\alpha}f\bigl(P+t_0(X-P)\bigr)}{\alpha!}\,(X-P)^{\alpha}.
$$
Aquí $\alpha=(\alpha_1;\alpha_2;\alpha_3)$ es un multiíndice, $|\alpha|=\alpha_1+\alpha_2+\alpha_3$, $\alpha!=\alpha_1!\,\alpha_2!\,\alpha_3!$, $(X-P)^{\alpha}=(x-p_1)^{\alpha_1}(y-p_2)^{\alpha_2}(z-p_3)^{\alpha_3}$, y $D^{\alpha}f$ es la derivada tomada $\alpha_1$ veces en $x$, $\alpha_2$ veces en $y$ y $\alpha_3$ veces en $z$.

- Se divide entre $\alpha!$, no entre $|\alpha|!$: para $\alpha=(2;1;1)$ es $2$, no $24$. Las segundas derivadas puras se dividen entre $2$; las mixtas, como $D^{(1;1;0)}f$, entre $1$.
- Cada multiíndice entra en la suma una vez; no hace falta contar cuántas veces aparece una derivada mixta: eso ya está en $\alpha!$. La forma con diferenciales $\frac{d^kf}{k!}$ y coeficientes $\frac{k!}{\alpha!}$ ([[es/seminar-sem3/hw1-taylor|tarea 1]]) da lo mismo.
- Recorre los multiíndices en orden para no olvidar ninguno: con tres variables hay $6$ de orden $2$ y $10$ de orden $3$: $(3;0;0)$, $(0;3;0)$, $(0;0;3)$, $(2;1;0)$, $(2;0;1)$, $(1;2;0)$, $(0;2;1)$, $(1;0;2)$, $(0;1;2)$, $(1;1;1)$. Con dos variables hay $k+1$ de orden $k$.
- Primero las derivadas en un punto **arbitrario**, después se sustituye $P$. Si se sustituye el punto antes, ya no queda nada que derivar.

**Método para 1a (un polinomio).**

1. Hallar todas las derivadas hasta el orden igual al grado del polinomio, en forma general.
2. Escribir las no nulas y despachar las demás con una frase: «las demás derivadas de orden $k$ son cero».
3. Sustituir $P$ con los pasos intermedios: $20\cdot3^3-8\cdot3\cdot(-2)^2-2\cdot(-2)=448$, no solo $448$.
4. Dividir entre $\alpha!$ (conviene una tabla) y reunir la respuesta.
5. Decir por qué no hay resto: las derivadas de orden mayor que el grado son idénticamente nulas, así que la igualdad es exacta para todo $X$ y la serie de Taylor es una suma finita.
6. Comprobar: la parte homogénea de mayor grado de la respuesta coincide con la de $f$ (no cambia al mover el punto), y un punto sencillo, por ejemplo $X=P+(1;0;0)$, da el mismo valor a los dos lados.

**Método para 1b (una función no polinómica).**

1. Derivadas hasta orden dos en forma general: $f$, tres de primer orden y seis de segundo. Después sus valores en $P$.
2. El polinomio de Taylor de orden dos: coeficientes $\frac{D^\alpha f(P)}{\alpha!}$ para $|\alpha|\le2$.
3. El resto **en forma general**, con el punto intermedio escrito coordenada a coordenada, como en la pizarra:
$$
R_2(X)=\sum_{|\alpha|=3}\frac{D^{\alpha}f\bigl(p_1+t_0(x-p_1);\ p_2+t_0(y-p_2);\ p_3+t_0(z-p_3)\bigr)}{\alpha!}\,(x-p_1)^{\alpha_1}(y-p_2)^{\alpha_2}(z-p_3)^{\alpha_3},\qquad t_0\in(0;1).
$$
4. Citar el teorema: $f$ es infinitamente (al menos tres veces) continuamente diferenciable. Si $f$ contiene un logaritmo o una raíz, indicar que la fórmula vale para los $X$ cuyo segmento $[P;X]$ entero está en el dominio.

No hay que hallar las derivadas de tercer orden explícitas: no es un error, pero quita tiempo al problema 2.

### Ejemplo 1'.1 (consulta): un polinomio de grado cuatro

**Enunciado.** $f(x;y)=5x^4-4x^2y^2+3y^4-2xy+1$. Desarrollarlo en serie de Taylor (finita) en el punto $P=(3;-2)$. Es el polinomio del [[es/seminar-sem3/hw1-taylor#Problema 1.2|problema 1.2]] de la tarea 1, donde el punto es $(-3;2)$.

**Derivadas en un punto arbitrario.**
$$
D^{(1;0)}f=20x^3-8xy^2-2y,\qquad D^{(0;1)}f=-8x^2y+12y^3-2x;
$$
$$
D^{(2;0)}f=60x^2-8y^2,\qquad D^{(1;1)}f=-16xy-2,\qquad D^{(0;2)}f=-8x^2+36y^2;
$$
$$
D^{(3;0)}f=120x,\qquad D^{(2;1)}f=-16y,\qquad D^{(1;2)}f=-16x,\qquad D^{(0;3)}f=72y;
$$
$$
D^{(4;0)}f=120,\qquad D^{(2;2)}f=-16,\qquad D^{(0;4)}f=72,\qquad D^{(3;1)}f=D^{(1;3)}f=0;
$$
las derivadas de quinto orden son cero.

**Valores y coeficientes.** $f(P)=5\cdot3^4-4\cdot3^2\cdot(-2)^2+3\cdot(-2)^4-2\cdot3\cdot(-2)+1=405-144+48+12+1=322$.

| Orden | $D^\alpha f(P)$ | $\frac{D^\alpha f(P)}{\alpha!}$ |
|---|---|---|
| 1 | $D^{(1;0)}=540-96+4=448$, $D^{(0;1)}=144-96-6=42$ | $448$, $42$ |
| 2 | $D^{(2;0)}=508$, $D^{(1;1)}=94$, $D^{(0;2)}=72$ | $254$, $94$, $36$ |
| 3 | $D^{(3;0)}=360$, $D^{(2;1)}=32$, $D^{(1;2)}=-48$, $D^{(0;3)}=-144$ | $60$, $16$, $-24$, $-24$ |
| 4 | $D^{(4;0)}=120$, $D^{(2;2)}=-16$, $D^{(0;4)}=72$ | $5$, $-4$, $3$ |

**Respuesta.** Para todo $(x;y)\in\mathbb R^2$
$$
\begin{aligned}f(x;y)={}&322+448(x-3)+42(y+2)+254(x-3)^2+94(x-3)(y+2)+36(y+2)^2\\&+60(x-3)^3+16(x-3)^2(y+2)-24(x-3)(y+2)^2-24(y+2)^3\\&+5(x-3)^4-4(x-3)^2(y+2)^2+3(y+2)^4 .\end{aligned}
$$

**Por qué funciona.** La parte de mayor grado $5(x-3)^4-4(x-3)^2(y+2)^2+3(y+2)^4$ repite la de $f$. En una línea intermedia la pizarra tenía $\frac{42}{(0;2)!}(y+2)^2$, una errata: $D^{(0;2)}f(P)=72$ y el coeficiente es $36$, como en la respuesta final de la pizarra. Como $f(-x;-y)=f(x;y)$, la respuesta de la tarea 1.2 en $(-3;2)$ solo difiere en los signos de los términos de grado impar.

### Ejemplo 1'.2 (consulta): $x^2e^{xy}+y\sin(yz^2)$

**Enunciado.** Desarrollar $f(x;y;z)=x^2e^{xy}+y\sin(yz^2)$ en $P=(2;0;1)$ con resto en forma de Lagrange. En la consulta se hizo hasta orden tres; en el control será orden dos, así que primero va la respuesta en el formato del control.

^ex-1p-2

**Derivadas hasta orden dos** en un punto arbitrario:
$$
D^{(1;0;0)}f=(x^2y+2x)e^{xy},\qquad D^{(0;1;0)}f=x^3e^{xy}+\sin(yz^2)+yz^2\cos(yz^2),\qquad D^{(0;0;1)}f=2y^2z\cos(yz^2);
$$
$$
D^{(2;0;0)}f=(x^2y^2+4xy+2)e^{xy},\qquad D^{(1;1;0)}f=(x^3y+3x^2)e^{xy},\qquad D^{(1;0;1)}f=0;
$$
$$
D^{(0;2;0)}f=x^4e^{xy}+2z^2\cos(yz^2)-yz^4\sin(yz^2),\qquad D^{(0;1;1)}f=4yz\cos(yz^2)-2y^2z^3\sin(yz^2),\qquad D^{(0;0;2)}f=2y^2\cos(yz^2)-4y^3z^2\sin(yz^2).
$$
**En $P$** ($e^0=1$, $\sin0=0$, $\cos0=1$): $f(P)=4$; $D^{(1;0;0)}f(P)=4$, $D^{(0;1;0)}f(P)=8$, $D^{(0;0;1)}f(P)=0$; $D^{(2;0;0)}f(P)=2$, $D^{(1;1;0)}f(P)=12$, $D^{(0;2;0)}f(P)=16+2=18$, las demás de segundo orden son cero.

**Respuesta hasta orden dos (formato del control).** $f\in C^\infty(\mathbb R^3)$, así que para todo $(x;y;z)\in\mathbb R^3$ existe $t_0\in(0;1)$ tal que
$$
f(x;y;z)=4+4(x-2)+8y+(x-2)^2+12(x-2)y+9y^2+\sum_{|\alpha|=3}\frac{D^{\alpha}f\bigl(2+t_0(x-2);\ t_0y;\ 1+t_0(z-1)\bigr)}{\alpha!}\,(x-2)^{\alpha_1}y^{\alpha_2}(z-1)^{\alpha_3}.
$$
Coeficientes: $\frac{2}{(2;0;0)!}=1$, $\frac{12}{(1;1;0)!}=12$, $\frac{18}{(0;2;0)!}=9$.

**Hasta orden tres (como en la consulta).** Las derivadas de tercer orden no nulas en $P$ son $D^{(0;3;0)}f(P)=32$, $D^{(2;1;0)}f(P)=12$, $D^{(1;2;0)}f(P)=32$, $D^{(0;2;1)}f(P)=4$. El polinomio gana los términos
$$
\frac{16}{3}y^3+6(x-2)^2y+16(x-2)y^2+2y^2(z-1),
$$
y el resto pasa a ser una suma sobre $|\alpha|=4$. La línea de la pizarra para $D^{(0;1;2)}f$ es incorrecta: lo correcto es $4y(1-y^2z^4)\cos(yz^2)-14y^2z^2\sin(yz^2)$; en $P$ vale $0$ de todos modos.

**Por qué funciona.** Casi todo se anuló porque $y=0$. El profesor advirtió que en el control el punto será «más honesto»: son posibles los valores $\pm\frac1{\sqrt2}$, y entonces los coeficientes llevan $\sqrt2$ (como en la [[es/seminar-sem3/test1-variants#Variante C|variante C]]).

## Problema 2: extremo condicionado

**El esquema (como en la consulta).**

1. **La función de Lagrange:** $\mathcal L(x;y;z;\lambda)=f(x;y;z)-\lambda\,\varphi(x;y;z)$, donde $M=\{\varphi=0\}$. El signo delante de $\lambda$ no importa: el seminario del 9 de septiembre usó «más», la consulta «menos». Al cambiar el signo solo cambia el signo de $\lambda$, y la matriz $\widetilde H$ en un punto estacionario es la misma.
2. **Puntos estacionarios de $\mathcal L$:** las cuatro derivadas parciales de primer orden se anulan; la cuarta ecuación es la propia condición $\varphi=0$.
3. **Resolver el sistema.** No hay un método general; los problemas están elegidos para que se puedan resolver. El paso habitual: la ecuación en una variable se factoriza ($6x(1-\lambda x)=0$) — tratar los dos casos; las demás variables se expresan mediante $\lambda$ y se sustituyen en la condición, lo que da una ecuación para $\lambda$. Primero probar que $\lambda\ne0$ (normalmente «si no, $2=0$») y solo después dividir. Al quitar $\lambda$ quedan los puntos candidatos de $\mathbb R^3$.
4. **La hessiana orlada** en un punto arbitrario; la orla va en la primera fila y la primera columna, como en la pizarra:
$$
\widetilde H=\begin{pmatrix}0&\varphi_x&\varphi_y&\varphi_z\\ \varphi_x&\mathcal L_{xx}&\mathcal L_{xy}&\mathcal L_{xz}\\ \varphi_y&\mathcal L_{xy}&\mathcal L_{yy}&\mathcal L_{yz}\\ \varphi_z&\mathcal L_{xz}&\mathcal L_{yz}&\mathcal L_{zz}\end{pmatrix}.
$$
5. **Menores.** Con $n=3$, $m=1$ se comprueban $n-m=2$ menores principales: $\Delta_3$, el de la esquina superior izquierda $3\times3$ (orla, $x$, $y$), y $\Delta_4=\det\widetilde H$. Primero en forma general; después se sustituye cada punto junto con su $\lambda$.
6. **Conclusión** según la tabla.

| $\Delta_3$ | $\Delta_4$ | Conclusión |
|---|---|---|
| $<0$ | $<0$ | mínimo local condicionado: los dos signos son $(-1)^m=-1$ |
| $>0$ | $<0$ | máximo local condicionado: los signos alternan empezando por $(-1)^{m+1}=+1$ |
| $<0$ | $>0$ | sin extremo |
| $>0$ | $>0$ | sin extremo |

Es el [[es/seminar-sem3/notes-1-taylor-extremum#Teorema 3.1. Extremos condicionados y la matriz hessiana orlada|teorema 3.1]] con $n=3$, $m=1$. El teorema no cubre el caso $\Delta_k=0$, pero en el control no aparecerá: un cero es motivo para revisar la aritmética.

**Fórmulas rápidas.** Si $f$ y $\varphi$ son sumas de funciones de una sola variable (como en todos los ejemplos de abajo), no hay derivadas mixtas: $\mathcal L_{xy}=\mathcal L_{xz}=\mathcal L_{yz}=0$. El desarrollo por la primera fila da
$$
\Delta_3=-\bigl(\varphi_x^2\,\mathcal L_{yy}+\varphi_y^2\,\mathcal L_{xx}\bigr),\qquad
\Delta_4=-\bigl(\varphi_x^2\,\mathcal L_{yy}\mathcal L_{zz}+\varphi_y^2\,\mathcal L_{xx}\mathcal L_{zz}+\varphi_z^2\,\mathcal L_{xx}\mathcal L_{yy}\bigr).
$$
En el control conviene escribir esa línea del desarrollo, no solo su resultado.

**Cuidado: dónde va la orla.** Si el gradiente de $\varphi$ se escribe en la última fila y la última columna (así aparece en algunos apuntes), el menor de orden tres de la esquina superior izquierda es el determinante del bloque $\mathcal L_{xx},\dots$ sin la orla, y da una respuesta errónea: en el ejemplo 1'.3 vale $-216$ en el punto de máximo, y el máximo «se convierte» en mínimo. Con esa disposición, $\Delta_3$ es el menor de las filas y columnas de $x$, $y$ y la orla. Es más sencillo poner la orla primero.

**Una comprobación sin menores.** Los menores codifican el signo de $d^2\mathcal L$ sobre el plano tangente $\{\varphi_x\,dx+\varphi_y\,dy+\varphi_z\,dz=0\}$: definida positiva — mínimo, definida negativa — máximo, indefinida — sin extremo. Si $H_{\mathcal L}$ es diagonal y todos sus elementos tienen el mismo signo, el signo se ve enseguida.

### Ejemplo 1'.3 (consulta): $3x^2+2y+6z$ sobre $2x^3+y^2+9z^2=4$

**Enunciado.** Hallar todos los puntos de extremo local condicionado de $f(x;y;z)=3x^2+2y+6z$ sobre el conjunto $M=\{(x;y;z)\in\mathbb R^3:\ 2x^3+y^2+9z^2=4\}$. Aquí $n=3$, $m=1$.

^ex-1p-3

**1. La función de Lagrange.** $\mathcal L=3x^2+2y+6z-\lambda\,(2x^3+y^2+9z^2-4)$.

**2. El sistema.**
$$
\begin{cases}6x-6\lambda x^2=0,\\ 2-2\lambda y=0,\\ 6-18\lambda z=0,\\ 2x^3+y^2+9z^2=4.\end{cases}
$$
De la segunda ecuación $\lambda y=1$, luego $\lambda\ne0$ e $y=\frac1\lambda$; de la tercera $z=\frac1{3\lambda}$. La primera: $6x(1-\lambda x)=0$.

- *Caso $x=0$.* La condición da $\frac1{\lambda^2}+9\cdot\frac1{9\lambda^2}=4$, es decir, $\lambda^2=\frac12$, $\lambda=\pm\frac1{\sqrt2}$. Los puntos $v^{(1)}=\bigl(0;-\sqrt2;-\frac{\sqrt2}3\bigr)$ con $\lambda=-\frac1{\sqrt2}$ y $v^{(2)}=\bigl(0;\sqrt2;\frac{\sqrt2}3\bigr)$ con $\lambda=\frac1{\sqrt2}$.
- *Caso $x=\frac1\lambda$.* La condición da $\frac2{\lambda^3}+\frac2{\lambda^2}=4$, es decir, $2\lambda^3-\lambda-1=0$. La raíz $\lambda=1$ se adivina, y $2\lambda^3-\lambda-1=(\lambda-1)(2\lambda^2+2\lambda+1)$ con $2\lambda^2+2\lambda+1=2\bigl(\lambda+\frac12\bigr)^2+\frac12>0$. El punto $v^{(3)}=\bigl(1;1;\frac13\bigr)$ con $\lambda=1$. (En el control no habrá ecuaciones cúbicas.)

**3. La matriz y los menores.** $\varphi_x=6x^2$, $\varphi_y=2y$, $\varphi_z=18z$; $\mathcal L_{xx}=6-12\lambda x$, $\mathcal L_{yy}=-2\lambda$, $\mathcal L_{zz}=-18\lambda$; las mixtas son cero.
$$
\widetilde H=\begin{pmatrix}0&6x^2&2y&18z\\6x^2&6-12\lambda x&0&0\\2y&0&-2\lambda&0\\18z&0&0&-18\lambda\end{pmatrix},
$$
$$
\Delta_3=72\lambda x^4-4y^2(6-12\lambda x),\qquad
\Delta_4=-1296\lambda^2x^4+72\lambda(6-12\lambda x)\,y^2+648\lambda(6-12\lambda x)\,z^2 .
$$

**4. Signos.**

| Punto | $\lambda$ | $\Delta_3$ | $\Delta_4$ | Conclusión | $f$ |
|---|---|---|---|---|---|
| $v^{(1)}=\bigl(0;-\sqrt2;-\frac{\sqrt2}3\bigr)$ | $-\frac1{\sqrt2}$ | $-48$ | $-864\sqrt2$ | mínimo | $-4\sqrt2$ |
| $v^{(2)}=\bigl(0;\sqrt2;\frac{\sqrt2}3\bigr)$ | $\frac1{\sqrt2}$ | $-48$ | $864\sqrt2$ | sin extremo | $4\sqrt2$ |
| $v^{(3)}=\bigl(1;1;\frac13\bigr)$ | $1$ | $96$ | $-2160$ | máximo | $7$ |

Por ejemplo, en $v^{(1)}$: $x=0$, $6-12\lambda x=6$, $y^2=2$, $z^2=\frac29$, así que $\Delta_3=-4\cdot2\cdot6=-48$ y $\Delta_4=72\cdot\bigl(-\frac1{\sqrt2}\bigr)\cdot6\cdot2+648\cdot\bigl(-\frac1{\sqrt2}\bigr)\cdot6\cdot\frac29=-\frac{864}{\sqrt2}-\frac{864}{\sqrt2}=-864\sqrt2$.

**Respuesta.** $\bigl(0;-\sqrt2;-\frac{\sqrt2}3\bigr)$ es un punto de mínimo local condicionado, $f=-4\sqrt2$; $\bigl(1;1;\frac13\bigr)$ es un punto de máximo local condicionado, $f=7$; en $\bigl(0;\sqrt2;\frac{\sqrt2}3\bigr)$ no hay extremo. La comprobación de signos no está en los fotogramas de la consulta; se ha recalculado aquí.

**Por qué funciona.** En $v^{(1)}$ la matriz $H_{\mathcal L}=\operatorname{diag}(6;\sqrt2;9\sqrt2)$ es definida positiva en todo $\mathbb R^3$, y en $v^{(3)}$ la matriz $\operatorname{diag}(-6;-2;-18)$ es definida negativa: los menores lo confirman. En $v^{(2)}$ el plano tangente está dado por $dy=-3\,dz$, y sobre él $d^2\mathcal L=6\,dx^2-18\sqrt2\,dz^2$ toma los dos signos. El conjunto $M$ no está acotado (se permite $x\to-\infty$), así que el argumento «en un compacto se alcanza el valor máximo» no sirve aquí: hacen falta los menores.

## Errores típicos

**Problema 1.**

- Dividir entre $|\alpha|!$ en vez de $\alpha!$; olvidar dividir entre $2$ en las segundas derivadas puras o dividir de más en las mixtas.
- Sustituir el punto antes de derivar.
- El resto escrito en $P$ y no en el punto intermedio; no decir que $t_0\in(0;1)$; intercambiar los cuantificadores («$\exists\,t_0$ para todo $X$» en lugar de «para cada $X$ existe $t_0$»).
- Escribir un resto en el problema 1a, o no explicar por qué no lo hay.
- Números sin pasos intermedios: quien corrige no ve de dónde salen.

**Problema 2.**

- Perder un caso al factorizar: $x=0$ **o** $1-\lambda x=0$.
- Dividir entre $\lambda$ sin probar que $\lambda\ne0$.
- La orla en la última fila y el «menor de la esquina superior izquierda»: un $\Delta_3$ erróneo.
- La regla de signos del extremo libre («todos los menores positivos — mínimo») en lugar de la regla con $(-1)^m$.
- Declarar extremo un punto estacionario sin comprobarlo; no decir en la respuesta que en un punto no hay extremo.

## Qué repasar en los apuntes de los seminarios

Los [[es/seminar-sem3/index#Apuntes de los seminarios|apuntes]] muestran en qué forma se dio la teoría en el seminario. En el control es sensato escribir con la misma notación: $D^\alpha f$ y $\alpha!$, el punto intermedio $P+t_0(X-P)$, la hessiana orlada con la orla primero.

| Problema | Qué repasar | Dónde |
|---|---|---|
| 1a | la fórmula de Taylor con multiíndices; por qué el resto de un polinomio es cero | [[es/seminar-sem3/notes-1-taylor-extremum#^ex-2-2\|ejemplo 2.2]], [[#Ejemplo 1'.1 (consulta): un polinomio de grado cuatro\|ejemplo 1'.1]] |
| 1b | la tabla de derivadas, los factores $\frac1{\alpha!}$, el resto en $u+t_0h$ | [[es/seminar-sem3/notes-1-taylor-extremum#^ex-4-1\|ejemplo 4.1]], [[es/seminar-sem3/notes-1-taylor-extremum#Observación 2.1. Un segmento es el conjunto de combinaciones convexas de sus extremos\|observación 2.1]], [[#^ex-1p-2\|ejemplo 1'.2]] |
| 2 | el enunciado del teorema y la tabla de signos de los menores | [[es/seminar-sem3/notes-1-taylor-extremum#Teorema 3.1. Extremos condicionados y la matriz hessiana orlada\|teorema 3.1]], [[es/seminar-sem3/notes-1-taylor-extremum#^ex-3-2\|ejemplo 3.2]] |
| 2 | la hessiana orlada en ejemplos: $n=2$; $n=4$, $m=2$; $n=3$, $m=1$, como en el control | [[es/seminar-sem3/notes-1-taylor-extremum#^ex-4-2\|ejemplo 4.2]], [[es/seminar-sem3/notes-1-taylor-extremum#^ex-5-1\|ejemplo 5.1]], [[#^ex-1p-3\|ejemplo 1'.3]] |

## Plan de preparación (16–19 de noviembre)

**Día 1: Taylor.**

1. Leer la sección [[#Problema 1: fórmula de Taylor|«Problema 1»]] y «La idea general» de la [[es/seminar-sem3/hw1-taylor|tarea 1]].
2. Sin mirar las soluciones, desarrollar el ejemplo 1'.1 y la tarea 1.2 (las respuestas difieren en los signos de los términos impares: una buena comprobación).
3. El ejemplo 1'.2 y la tarea 1.4 hasta orden dos, con el resto solo en forma general.

**Día 2: extremo condicionado.**

1. Leer el [[es/seminar-sem3/notes-1-taylor-extremum#Teorema 3.1. Extremos condicionados y la matriz hessiana orlada|teorema 3.1]] y la sección [[#Problema 2: extremo condicionado|«Problema 2»]]; deducir uno mismo las fórmulas rápidas para $\Delta_3$, $\Delta_4$.
2. Resolver el ejemplo 1'.3 completo, con los menores, sin mirar la solución.
3. Como calentamiento, la tarea 2.1 con la hessiana orlada ($n=2$, un menor).

**Día 3: variantes de práctica.** La [[es/seminar-sem3/test1-variants#Variante A|variante A]] con tiempo y sin calculadora (referencia: hora y media; confirma la duración real del control) y comprobación con las soluciones; después la [[es/seminar-sem3/test1-variants#Variante B|variante B]].

**Día 4: ensayo.** La [[es/seminar-sem3/test1-variants#Variante C|variante C]] con tiempo; analizar los errores de las tres variantes; responder a las preguntas de autoevaluación de abajo.

## Autoevaluación antes del control

1. ¿Cuánto vale $(2;0;1)!$ y entre qué se divide $D^{(1;1;1)}f(P)$ en la fórmula de Taylor?
2. ¿Cuántos multiíndices $\alpha$ con $|\alpha|=3$ tiene una función de tres variables? ¿Y con $|\alpha|=2$?
3. ¿Por qué no hay resto en el problema 1a?
4. ¿Cómo se escribe el punto intermedio del resto para $P=(2;0;1)$?
5. ¿Por qué no se puede escribir «$\exists\,t_0\in(0;1)$: la igualdad vale para todo $(x;y;z)$»?
6. ¿Cuántos menores de la hessiana orlada se comprueban con $n=3$, $m=1$, y de qué órdenes?
7. Los signos de $(\Delta_3;\Delta_4)$ son $(+;-)$. ¿Conclusión? ¿Y $(-;-)$? ¿Y $(-;+)$?
8. Se escribió la matriz con la orla en la última fila y columna. ¿Qué menor de orden tres hay que tomar?
9. ¿Cambia la respuesta si se toma $\mathcal L=f+\lambda\varphi$ en vez de $f-\lambda\varphi$?
10. Los tres puntos estacionarios salieron máximos. ¿Qué hacer?
11. ¿Cuánto valen $\sin\frac{3\pi}4$ y $\cos\frac{5\pi}4$?
12. ¿Cuándo se puede invocar la compacidad de $M$ en el problema 2, y qué no sustituye?

> [!answer]- Respuestas
> 1. $(2;0;1)!=2!\cdot0!\cdot1!=2$; $D^{(1;1;1)}f(P)$ se divide entre $(1;1;1)!=1$.
> 2. $10$ y $6$.
> 3. Las derivadas de orden mayor que el grado del polinomio son idénticamente nulas, así que el resto es cero para cualquier $t_0$ y la igualdad es exacta.
> 4. $\bigl(2+t_0(x-2);\ t_0y;\ 1+t_0(z-1)\bigr)$, $t_0\in(0;1)$.
> 5. $t_0$ depende del punto: cada punto $(x;y;z)$ tiene el suyo.
> 6. Dos: $\Delta_3$ y $\Delta_4$ (órdenes $2m+1,\dots,n+m$).
> 7. $(+;-)$: máximo; $(-;-)$: mínimo; $(-;+)$: sin extremo.
> 8. El menor de las filas y columnas de $x$, $y$ y la orla, no el de la esquina superior izquierda.
> 9. No: $\lambda$ cambia de signo, y $\widetilde H$ en el punto estacionario sigue siendo la misma.
> 10. Revisar: el profesor prometió que el problema 2 tiene un máximo, un mínimo y un punto sin extremo.
> 11. $\frac1{\sqrt2}$ y $-\frac1{\sqrt2}$.
> 12. Si $M$ es compacto (una esfera, un elipsoide), $f$ alcanza en él sus valores máximo y mínimo, y están entre los puntos estacionarios. Pero eso no prueba que los demás puntos no sean extremos: para un punto sin extremo siguen haciendo falta los menores. En el ejemplo 1'.3 el conjunto $M$ no es compacto.
