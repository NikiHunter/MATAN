---
title: "Lecciones 61–62: derivadas direccionales, Jacobiano y reglas de derivación"
lang: es
course: "Análisis matemático 2025/26"
lecture: 61-62
semester: 2
date: 2026-05-21
source: "ma25_26-lectures_61-62_notes.pdf.txt"
pdf_pages: 40
typed_slides: 25
---
# Lecciones 61–62 — derivadas direccionales, Jacobiano y reglas de derivación

> **Fuente y numeración.** Transcripción elaborada exclusivamente a partir del PDF adjunto `ma25_26-lectures_61-62_notes.pdf.txt`; no se consultó la carpeta de fuentes. Las secciones siguen el orden de las páginas físicas del PDF. Los números de «diapositiva impresa» son los pies de página 1–25 y se distinguen de las páginas PDF 1–40; las páginas manuscritas no reciben número de diapositiva. El texto impreso se cotejó con la capa de texto y las imágenes; las demostraciones, cálculos y anotaciones manuscritos se leyeron en las páginas renderizadas. Véanse el [inventario de páginas, hash de la fuente y procedencia de recortes](../../assets/lectures-2025-26/provenance-61-64.md) y el [manifiesto legible por máquina](../../assets/lectures-2025-26/figures-61-64.json).
>
> **Duplicación del semestre 2.** Este material coincide temáticamente con §§6.1–6.3 del registro temático ruso y se duplica intencionadamente en esta transcripción secuencial y trilingüe del PDF. El semestre 2 abarca las lecciones **33–64**. Véanse el [índice del registro](../../ru/lectures/index.md), [§6.1](../../ru/lectures/14-differentiability-6-1.md), [§6.2](../../ru/lectures/15-differentiation-rules-6-2.md) y [§6.3](../../ru/lectures/16-continuous-differentiability-6-3.md).

## Diapositiva impresa 1 (pp. PDF 1). Portada

Análisis matemático, lecciones 61–62; 21 de mayo de 2026. La portada presenta el segundo capítulo de cálculo diferencial.

## Diapositiva impresa 2 (pp. PDF 2). Cita del día

Alicia pregunta por qué llaman locos a quienes la rodean. El Gato responde que allí todos están locos, incluida Alicia, y que ella debe de estarlo porque está allí. La diapositiva atribuye el fragmento a Lewis Carroll, *Alicia en el país de las maravillas*.

## Diapositiva impresa 3 (pp. PDF 3). Objetivos de la lección

Se presentan las [derivadas según un vector](#def-6-1-4), los diferenciales, la [matriz jacobiana](#def-6-1-6) y el gradiente; se estudia la propiedad extrema del gradiente; se establecen versiones multivariables de las reglas de derivación y se introduce la diferenciabilidad continua.

<a id="def-6-1-4"></a>
## Diapositiva impresa 4 (pp. PDF 4). Derivada según un vector — definición 6.1.4

Sean $`E\subset\mathbb R^n`$, $`a`$ un punto interior de $`E`$, $`f:E\to\mathbb R^m`$ y $`e\in\mathbb R^n\setminus\{0\}`$. Si existe el límite finito

```math
\lim_{t\to0}\frac{f(a+te)-f(a)}{t},
```

se llama derivada de $`f`$ según el vector $`e`$ en $`a`$ y se denota $`\frac{\partial f}{\partial e}(a)`$. Si además $`\|e\|=1`$, se llama derivada direccional en la dirección $`e`$. En adelante, «derivada según un vector» siempre significa una derivada finita.

## Diapositiva impresa 5 (pp. PDF 5). Interpretación y derivadas por componentes

La restricción de $`f`$ a la recta que pasa por $`a`$ en la dirección $`e`$ es $`g(t)=f(a+te)`$; su derivada en cero es $`\frac{\partial f}{\partial e}(a)`$. Como algún entorno de $`a`$ está contenido en $`E`$, esta curva está definida al menos para $`t\in(-\delta,\delta)`$ con algún $`\delta>0`$.

Para una aplicación $`f=(f_1,\ldots,f_m)`$, la derivada según un vector se calcula por componentes:

```math
\frac{\partial f}{\partial e}(a)=\left(\frac{\partial f_1}{\partial e}(a),\ldots,\frac{\partial f_m}{\partial e}(a)\right).
```

La igualdad se entiende por componentes: si uno de los miembros está definido, también lo está el otro, y ambos coinciden.

<a id="thm-6-1-1"></a>
## Diapositiva impresa 6 (pp. PDF 6). Derivada de una aplicación diferenciable — teorema 6.1.1

Sean $`E\subset\mathbb R^n`$, $`a`$ un punto interior de $`E`$ y $`f:E\to\mathbb R^m`$ diferenciable en $`a`$. Para $`e\in\mathbb R^n\setminus\{0\}`$,

```math
\frac{\partial f}{\partial e}(a)=d_af(e). \tag{6.1.4}
```

## Página manuscrita (pp. PDF 7). Demostración del teorema 6.1.1

Escribimos el desarrollo de diferenciabilidad como

```math
f(a+h)-f(a)=Th+\alpha(h)\|h\|,\qquad T=d_af,\qquad \alpha(h)\to0.
```

Sustituimos $`h=te`$ y dividimos por $`t\ne0`$. Como $`T(te)/t=T(e)`$ y la [norma](../14-several-variables.md#sec-14-1) del resto dividida por $`|t|`$ tiende a cero, es decir, $`\|\alpha(te)\|\|e\|\to0`$, el límite es $`T(e)=d_af(e)`$. Así se justifica también la identificación manuscrita $`T=d_af`$.

![Demostración manuscrita del teorema 6.1.1](../../assets/lectures-2025-26/lec61-62-p07-vector-derivative-proof.jpg)

## Diapositiva impresa 7 (pp. PDF 8). Unicidad del diferencial

**Corolario.** Si $`f`$ es diferenciable en $`a`$, su diferencial $`d_af`$ queda determinado de forma única.

La anotación manuscrita explica que, para todo vector no nulo, la derivada según $`e`$ queda fijada por su límite y el [teorema 6.1.1](#thm-6-1-1) la identifica con $`d_af(e)`$. Como una aplicación lineal también queda fijada en $`e=0`$, pues $`d_af(0)=0`$, el diferencial es único.

![Corolario de unicidad con demostración manuscrita](../../assets/lectures-2025-26/lec61-62-p08-differential-uniqueness.jpg)

<a id="def-6-1-5"></a>
## Diapositiva impresa 8 (pp. PDF 9). Derivadas parciales — definición 6.1.5

Sean $`e^1,\ldots,e^n`$ los vectores de la base canónica, con $`e^i_j=1`$ si $`i=j`$ y $`0`$ en otro caso. La derivada según $`e^k`$, para $`k\in\{1,\ldots,n\}`$, se llama derivada parcial respecto de la variable $`k`$:

```math
\frac{\partial f}{\partial x_k}(a)=\frac{\partial f}{\partial e^k}(a).
```

También se usan las notaciones $`D_kf(a)`$, $`\partial_kf(a)`$ y $`f'_{x_k}(a)`$. Para funciones de varias variables se suele escribir $`\partial`$ en lugar de $`d`$.

## Diapositiva impresa 9 (pp. PDF 10). Cálculo de derivadas parciales

Fijamos todos los argumentos salvo el $`k`$-ésimo, definiendo

```math
\varphi_k(t)=f(a_1,\ldots,a_{k-1},t,a_{k+1},\ldots,a_n).
```

Entonces $`\frac{\partial f}{\partial x_k}(a)=\varphi_k'(a_k)`$. Para una aplicación con valores en $`\mathbb R^m`$, la derivada parcial se calcula por componentes:

```math
\frac{\partial f}{\partial x_k}(a)=\left(\frac{\partial f_1}{\partial x_k}(a),\ldots,\frac{\partial f_m}{\partial x_k}(a)\right),
```
siempre que esté definido uno de los miembros.

## Página manuscrita (pp. PDF 11). Ejemplo de derivadas parciales en $`\mathbb R^3`$

Para

```math
f(x,y,z)=x^2z+xy^2(z-3)+\sin(xyz),
```
la página manuscrita deriva término a término:

```math
\frac{\partial f}{\partial x}=2xz+y^2(z-3)+yz\cos(xyz),\qquad
\frac{\partial f}{\partial y}=2xy(z-3)+xz\cos(xyz),
```

```math
\frac{\partial f}{\partial z}=x^2+xy^2+xy\cos(xyz).
```

En $`a=(1,1,1)`$ se obtiene $`f_x(a)=\cos1`$, $`f_y(a)=\cos1-4`$ y $`f_z(a)=\cos1+2`$.

![Ejemplo manuscrito de derivadas parciales](../../assets/lectures-2025-26/lec61-62-p11-partial-derivative-example.jpg)

<a id="thm-6-1-2"></a>
## Diapositiva impresa 10 (pp. PDF 12). Diferencial y derivada direccional mediante derivadas parciales — teorema 6.1.2

Si $`f:E\to\mathbb R^m`$ es diferenciable en el punto interior $`a\in E\subset\mathbb R^n`$, entonces

```math
d_af(h)=\sum_{k=1}^{n}\frac{\partial f}{\partial x_k}(a)h_k\quad\text{para todo }h\in\mathbb R^n; \tag{6.1.5}
```

```math
\frac{\partial f}{\partial e}(a)=\sum_{k=1}^{n}\frac{\partial f}{\partial x_k}(a)e_k\quad\text{para todo }e\in\mathbb R^n\setminus\{0\}. \tag{6.1.6}
```

## Página manuscrita (pp. PDF 13). Demostración del teorema 6.1.2

Escribimos $`h=(h_1,\ldots,h_n)=\sum_{k=1}^{n}h_ke^k`$. Por la linealidad del diferencial y el [teorema 6.1.1](#thm-6-1-1),

```math
d_af(h)=d_af\left(\sum_{k=1}^{n}h_ke^k\right)=\sum_{k=1}^{n}d_af(e^k)h_k=\sum_{k=1}^{n}\frac{\partial f}{\partial x_k}(a)h_k.
```

Esto demuestra (6.1.5); al tomar $`h=e`$ se obtiene (6.1.6).

![Demostración manuscrita del teorema 6.1.2](../../assets/lectures-2025-26/lec61-62-p13-differential-formula-proof.jpg)

<a id="def-6-1-6"></a>
## Diapositiva impresa 11 (pp. PDF 14). Matriz jacobiana y gradiente — definición 6.1.6

Para una aplicación $`f:E\to\mathbb R^m`$, la matriz del operador lineal $`d_af`$ se llama matriz jacobiana de $`f`$ en $`a`$ y se denota $`f'(a)`$. Si $`m=1`$, esta matriz $`1\times n`$ es un vector de $`\mathbb R^n`$, el gradiente de $`f`$, que se denota $`\operatorname{grad}f(a)`$ o $`\nabla f(a)`$.

## Página manuscrita (pp. PDF 15). Notación de matriz jacobiana y gradiente

Para $`f=(f_1,\ldots,f_m)`$ se escribe

```math
f'(a)=d_af=\left(\frac{\partial f_i}{\partial x_j}(a)\right)_{1\le i\le m,\,1\le j\le n}.
```

Para una función escalar $`g`$, el vector $`\nabla g`$ está formado por sus [derivadas parciales](#def-6-1-5) de primer orden. Estas coordenadas se usan en las fórmulas siguientes para el gradiente.

![Notación manuscrita de la matriz jacobiana y del gradiente](../../assets/lectures-2025-26/lec61-62-p15-jacobian-gradient.jpg)

## Diapositiva impresa 12 (pp. PDF 16). Convenciones para las matrices jacobianas

Si los vectores de $`\mathbb R^n`$ y $`\mathbb R^m`$ se escriben como columnas, la expansión de diferenciabilidad queda

```math
f(a+h)=f(a)+f'(a)\cdot h+o(h)\qquad(h\to0).
```

Cuando $`m=1`$, el producto $`f'(a)\cdot h`$ puede interpretarse tanto como producto de matrices como [producto escalar](../21-lp-spaces.md#sec-21-4) $`\nabla f(a)\cdot h`$; ambos dan el mismo resultado.

<a id="lem-6-1-1"></a>
## Diapositiva impresa 13 (pp. PDF 17). Diferenciabilidad de las funciones coordenadas — lema 6.1.1

Sean $`E\subset\mathbb R^n`$, $`a`$ un punto interior, $`f:E\to\mathbb R^m`$ y $`T\in L(\mathbb R^n,\mathbb R^m)`$. Son equivalentes:

1. $`f`$ es diferenciable en $`a`$ y $`d_af=T`$.
2. Todas las funciones coordenadas $`f_k`$ son diferenciables en $`a`$, y $`d_af_k=T_k`$ para cada $`k\in\{1,\ldots,m\}`$.

## Página manuscrita (pp. PDF 18). Demostración del lema 6.1.1

Si $`f`$ es diferenciable, al componerla con cada proyección coordenada se obtienen funciones coordenadas diferenciables, cuyos diferenciales son las filas correspondientes de $`T`$. Recíprocamente, si cada $`f_k`$ es diferenciable y tiene diferencial $`T_k`$, reunimos esas aplicaciones lineales como filas de $`T`$. El resto de cada componente es $`o(\|h\|)`$; como hay un número finito de componentes, el resto vectorial también es $`o(\|h\|)`$. Por tanto, $`f`$ es diferenciable y $`d_af=T`$.

![Demostración manuscrita del lema sobre funciones coordenadas](../../assets/lectures-2025-26/lec61-62-p18-coordinate-functions-lemma.jpg)

<a id="thm-6-1-3"></a>
## Diapositiva impresa 14 (pp. PDF 19). Entradas de la matriz jacobiana — teorema 6.1.3

Si $`f:E\to\mathbb R^m`$ es diferenciable en el punto interior $`a\in E\subset\mathbb R^n`$,

```math
f'(a)=\begin{pmatrix}
\frac{\partial f_1}{\partial x_1}(a)&\cdots&\frac{\partial f_1}{\partial x_n}(a)\\
\vdots&\ddots&\vdots\\
\frac{\partial f_m}{\partial x_1}(a)&\cdots&\frac{\partial f_m}{\partial x_n}(a)
\end{pmatrix}.
```

En particular, para $`m=1`$,

```math
\operatorname{grad}f(a)=\left(\frac{\partial f}{\partial x_1}(a),\ldots,\frac{\partial f}{\partial x_n}(a)\right). \tag{6.1.7}
```

Las filas de la matriz jacobiana son los gradientes de las funciones coordenadas.

## Página manuscrita (pp. PDF 20). Demostración del teorema 6.1.3

Sea $`T=d_af=f'(a)`$. Por el [teorema 6.1.2](#thm-6-1-2), para cada vector de la base $`e^j`$ se tiene $`T(e^j)=\frac{\partial f}{\partial x_j}(a)`$. Por tanto, la columna $`j`$ de la matriz de $`T`$ es ese vector y su componente $`i`$ es $`\frac{\partial f_i}{\partial x_j}(a)`$. Estos son precisamente los elementos de la matriz jacobiana indicada.

![Demostración manuscrita del teorema 6.1.3](../../assets/lectures-2025-26/lec61-62-p20-jacobian-matrix-proof.jpg)

## Diapositiva impresa 15 (pp. PDF 21). Significado geométrico del gradiente

Para una función escalar $`f`$ diferenciable en $`a\in E\subset\mathbb R^n`$, el hiperplano tangente a su gráfica es

```math
\{(x,y):x\in\mathbb R^n,\ y=f(a)+\operatorname{grad}f(a)\cdot(x-a)\}.
```

Equivalentemente,

```math
\{(x,y):x\in\mathbb R^n,\ y=f(a)+\sum_{k=1}^{n}\frac{\partial f}{\partial x_k}(a)(x_k-a_k)\}. \tag{6.1.8}
```

Para $`n=1`$ es la recta tangente; para $`n=2`$, el [plano tangente](../15-multivariable-differentiation.md#sec-15-3) en $`\mathbb R^3`$; en general, un hiperplano de $`\mathbb R^{n+1}`$.

<a id="thm-6-1-4"></a>
## Diapositiva impresa 16 (pp. PDF 22). Propiedad extrema del gradiente — teorema 6.1.4

Sea $`f:E\to\mathbb R`$ diferenciable en el punto interior $`a`$ y supongamos que $`\operatorname{grad}f(a)\ne0`$. Para cada vector unitario $`e\in\mathbb R^n`$,

```math
\left|\frac{\partial f}{\partial e}(a)\right|\le\|\operatorname{grad}f(a)\|.
```

La igualdad se alcanza solo para $`e=\pm\frac{\operatorname{grad}f(a)}{\|\operatorname{grad}f(a)\|}`$. Así, el gradiente indica la dirección de máximo crecimiento y su longitud es el valor absoluto de la derivada en esa dirección.

## Página manuscrita (pp. PDF 23). Demostración de la cota del gradiente

Por (6.1.6)–(6.1.7), $`\frac{\partial f}{\partial e}(a)=\operatorname{grad}f(a)\cdot e`$. La [desigualdad de Cauchy–Schwarz](lecture-47-48.md#thm-4-4-6) y $`\|e\|=1`$ dan la cota. Se alcanza la igualdad de Cauchy–Schwarz exactamente cuando los vectores son colineales, es decir, $`e=\pm\operatorname{grad}f(a)/\|\operatorname{grad}f(a)\|`$.

![Demostración manuscrita de la propiedad extrema del gradiente](../../assets/lectures-2025-26/lec61-62-p23-gradient-extremal-proof.jpg)

## Página manuscrita (pp. PDF 24). Función diferenciable con derivadas parciales discontinuas

El primer ejemplo es

```math
f(x,y)=\begin{cases}(x^2+y^2)\sin\!\left(\frac{1}{x^2+y^2}\right),&(x,y)\ne(0,0),\\0,&(x,y)=(0,0).\end{cases}
```

Es diferenciable en el origen con diferencial cero, ya que $`|f(x,y)|\le x^2+y^2=o(\sqrt{x^2+y^2})`$. La demostración manuscrita expresa este hecho mediante un factor de resto acotado por $`\sqrt{x^2+y^2}`$.

![Ejemplo manuscrito de diferenciabilidad](../../assets/lectures-2025-26/lec61-62-p24-differentiable-partials-example.jpg)

## Página manuscrita (pp. PDF 25). Derivadas parciales del primer ejemplo

Fuera del origen,

```math
f_x(x,y)=2x\left[\sin\!\left(\frac{1}{x^2+y^2}\right)-\frac{1}{x^2+y^2}\cos\!\left(\frac{1}{x^2+y^2}\right)\right],
```

```math
f_y(x,y)=2y\left[\sin\!\left(\frac{1}{x^2+y^2}\right)-\frac{1}{x^2+y^2}\cos\!\left(\frac{1}{x^2+y^2}\right)\right].
```

Ambas derivadas parciales en $`(0,0)`$ son cero. Sin embargo, para $`x_k=1/\sqrt{2\pi k}`$ se tiene $`f_x(x_k,0)=-2\sqrt{2\pi k}\to-\infty`$; por simetría $`f_y(0,x_k)\to-\infty`$. Por tanto, las derivadas parciales no son continuas en el origen.

## Página manuscrita (pp. PDF 26). Las derivadas parciales no garantizan diferenciabilidad

El segundo ejemplo es

```math
f(x,y)=\begin{cases}xy\exp\!\left(\frac{1}{x^2+y^2}\right),&(x,y)\ne(0,0),\\0,&(x,y)=(0,0).\end{cases}
```

Las notas manuscritas señalan que ambas derivadas parciales primeras existen en todos los puntos, pero la derivada en el origen solo existe para vectores paralelos a $`e^1=(1,0)`$ o $`e^2=(0,1)`$. Para direcciones con dos componentes no nulas, el límite no es finito; el cálculo aparece en las páginas siguientes.

![Contraejemplo manuscrito para las derivadas direccionales](../../assets/lectures-2025-26/lec61-62-p26-directional-derivative-counterexample.jpg)

## Página manuscrita (pp. PDF 27). Derivadas del segundo ejemplo

Para $`(x,y)\ne(0,0)`$,

```math
f_x(x,y)=y\exp\!\left(\frac{1}{x^2+y^2}\right)\left(1-\frac{2x^2}{(x^2+y^2)^2}\right),\qquad
f_y(x,y)=x\exp\!\left(\frac{1}{x^2+y^2}\right)\left(1-\frac{2y^2}{(x^2+y^2)^2}\right).
```

En el origen las derivadas parciales coordenadas son cero. En la diagonal, $`f(t,t)=t^2\exp(1/(2t^2))`$, por lo que la función no es continua allí.

## Página manuscrita (pp. PDF 28). Cociente direccional y tercer ejemplo

Sea $`e=(a,b)`$. Si $`ab\ne0`$,

```math
\frac{f(te)-f(0,0)}{t}=tab\exp\!\left(\frac{1}{t^2(a^2+b^2)}\right),
```

que no tiene límite finito cuando $`t\to0`$. Si $`a=0`$ o $`b=0`$, el cociente es idénticamente cero; solo en estas direcciones existe una derivada finita según un vector en el origen.

El tercer ejemplo es

```math
f(x,y)=\begin{cases}1,&x>0\text{ and }y=x^2,\\0,&\text{otherwise}.\end{cases}
```

## Página manuscrita (pp. PDF 29). Función discontinua con todas las derivadas direccionales

Para el tercer ejemplo, $`f(1/k,1/k^2)=1`$, aunque $`(1/k,1/k^2)\to(0,0)`$ y $`f(0,0)=0`$; por tanto, $`f`$ es discontinua en el origen. Para cualquier vector fijo $`e=(a,b)`$, la recta $`(ta,tb)`$ corta la curva $`y=x^2`$, $`x>0`$ como máximo en un parámetro no nulo $`t`$ cerca de cero. Así, para todo $`t`$ no nulo y suficientemente pequeño, $`f(te)=0`$ y

```math
\frac{\partial f}{\partial e}(0,0)=0\qquad\text{para todo }e\in\mathbb R^2\setminus\{0\}.
```

![Ejemplo manuscrito de discontinuidad y derivadas direccionales](../../assets/lectures-2025-26/lec61-62-p29-zero-directional-derivatives-example.jpg)

## Página manuscrita (pp. PDF 30). Conclusiones de los ejemplos

En dos variables, la existencia de derivadas parciales finitas es necesaria pero no suficiente para la diferenciabilidad. Ni siquiera basta la existencia de derivadas según todos los vectores no nulos: la tercera función es discontinua aunque todas esas derivadas existen y valen cero.

![Resumen manuscrito de los contraejemplos](../../assets/lectures-2025-26/lec61-62-p30-directional-derivative-conclusions.jpg)

## Diapositiva impresa 17 (pp. PDF 31). §2 — Reglas de derivación

La lección pasa a las reglas de derivación multivariable.

<a id="thm-6-2-1"></a>
## Diapositiva impresa 18 (pp. PDF 32). Composición y regla de la cadena — teorema 6.2.1

Sean $`E\subset\mathbb R^n`$, $`F\subset\mathbb R^m`$, $`f:E\to F`$ y $`g:F\to\mathbb R^s`$. Supongamos que $`a`$ es interior a $`E`$, que $`f(a)`$ es interior a $`F`$, y que $`f`$ y $`g`$ son diferenciables en $`a`$ y $`f(a)`$, respectivamente. Entonces $`g\circ f`$ es diferenciable en $`a`$ y

```math
d_a(g\circ f)=d_{f(a)}g\circ d_af. \tag{6.2.1}
```

En notación matricial,

```math
(g\circ f)'(a)=g'(f(a))\cdot f'(a). \tag{6.2.2}
```

El diagrama manuscrito azul señala los espacios y aplicaciones sucesivos: $`E\subset\mathbb R^n\xrightarrow{f}F\subset\mathbb R^m\xrightarrow{g}\mathbb R^s`$.

![Diapositiva de la regla de la cadena con diagrama manuscrito](../../assets/lectures-2025-26/lec61-62-p32-chain-rule-diagram.jpg)

## Diapositiva impresa 19 (pp. PDF 33). Forma coordenada de la regla de la cadena

En las condiciones del [teorema 6.2.1](#thm-6-2-1), para $`i\in\{1,\ldots,s\}`$ y $`j\in\{1,\ldots,n\}`$,

```math
\frac{\partial(g\circ f)_i}{\partial x_j}(a)=\sum_{k=1}^{m}\frac{\partial g_i}{\partial x_k}(f(a))\,\frac{\partial f_k}{\partial x_j}(a). \tag{6.2.3}
```

Se obtiene al igualar las entradas $`(i,j)`$ en ambos miembros de (6.2.2).

<a id="thm-6-2-2"></a>
## Diapositiva impresa 20 (pp. PDF 34). Reglas aritméticas — teorema 6.2.2

Sean $`f,g:E\to\mathbb R^m`$ diferenciables en un punto interior $`a`$. Para $`\lambda,\mu\in\mathbb R`$,

```math
d_a(\lambda f+\mu g)=\lambda\,d_af+\mu\,d_ag.
```

Si una función escalar $`\lambda:E\to\mathbb R`$ es diferenciable en $`a`$, entonces

```math
d_a(\lambda\cdot f)=f(a)\cdot d_a\lambda+\lambda(a)\cdot d_af.
```

## Diapositiva impresa 21 (pp. PDF 35). Producto y cociente — teorema 6.2.2 (continuación)

El producto escalar $`f\cdot g`$ es diferenciable en $`a`$ y

```math
d_a(f\cdot g)=g(a)\cdot d_af+f(a)\cdot d_ag.
```

Si $`m=1`$ y $`g(a)\ne0`$, la función $`f/g`$ es diferenciable en $`a`$ y

```math
d_a\left(\frac{f}{g}\right)=\frac{g(a)\,d_af-f(a)\,d_ag}{g^2(a)}.
```

## Diapositiva impresa 22 (pp. PDF 36). Regla del producto en forma jacobiana

Para una función escalar $`\lambda`$ y una [aplicación diferenciable](lecture-59-60.md#def-6-1-2) $`f`$,

```math
(\lambda f)'(a)=f(a)\cdot\lambda'(a)+\lambda(a)\cdot f'(a).
```

En efecto, aplicar ambos miembros a $`h\in\mathbb R^n`$ da

```math
(\lambda f)'(a)h=d_a(\lambda f)(h)=f(a)\cdot d_a\lambda(h)+\lambda(a)\cdot d_af(h)
=(f(a)\lambda'(a)+\lambda(a)f'(a))h.
```

Equivalentemente, para cada $`j\in\{1,\ldots,n\}`$,

```math
\frac{\partial(\lambda f)}{\partial x_j}(a)=f(a)\cdot\frac{\partial\lambda}{\partial x_j}(a)+\lambda(a)\cdot\frac{\partial f}{\partial x_j}(a).
```

<a id="thm-6-2-3"></a>
## Diapositiva impresa 23 (pp. PDF 37). Derivación de la aplicación inversa — teorema 6.2.3

Sea $`f:E\to\mathbb R^n`$ diferenciable en el punto interior $`a\in E`$. Supongamos que:

1. el operador $`d_af`$ es invertible;
2. la aplicación $`f`$ es [inyectiva](lecture-01-02.md#def-1-1-4);
3. $`f(a)`$ es un punto interior de $`f(E)`$;
4. $`f^{-1}`$ es continua en $`f(a)`$.

Entonces $`f^{-1}`$ es diferenciable en $`f(a)`$ y

```math
d_{f(a)}f^{-1}=(d_af)^{-1}.
```

## Página manuscrita (pp. PDF 38). Linealidad del diferencial

La demostración manuscrita toma $`T=d_af`$ y $`S=d_ag`$, y escribe los desarrollos de diferenciabilidad de $`f`$ y $`g`$ con restos $`\alpha(h)\|h\|`$ y $`\beta(h)\|h\|`$, donde $`\alpha(h),\beta(h)\to0`$. Al multiplicar por los escalares $`\lambda,\mu`$ y sumar, la parte lineal de $`\lambda f+\mu g`$ es $`(\lambda T+\mu S)h`$ y el resto combinado sigue siendo $`o(\|h\|)`$. Por tanto,

```math
d_a(\lambda f+\mu g)=\lambda\,d_af+\mu\,d_ag.
```

![Demostración manuscrita de la linealidad del diferencial](../../assets/lectures-2025-26/lec61-62-p38-linearity-proof.jpg)

## Diapositiva impresa 24 (pp. PDF 39). Aplicaciones continuamente diferenciables

Para funciones de una variable, diferenciabilidad en un punto equivale a existencia de la derivada allí, un criterio práctico. En varias variables, la existencia de derivadas parciales no caracteriza la diferenciabilidad de manera tan sencilla. En cambio, la diferenciabilidad continua se describe cómodamente mediante las derivadas parciales y suele ser más útil en la práctica.

## Diapositiva impresa 25 (pp. PDF 40). Diferenciabilidad y diferenciabilidad continua — definiciones 6.3.1–6.3.2

<a id="def-6-3-1"></a>**Definición 6.3.1.** Si $`E`$ es abierto en $`\mathbb R^n`$, una aplicación $`f:E\to\mathbb R^m`$ se llama diferenciable en $`E`$ si es diferenciable en todos los puntos de $`E`$.

<a id="def-6-3-2"></a>**Definición 6.3.2.** Sean $`E\subset\mathbb R^n`$ y $`f:E\to\mathbb R^m`$.

1. Si $`a\in E`$, todas las derivadas parciales primeras de $`f`$ están definidas en un entorno de $`a`$ y son continuas en $`a`$, entonces $`f`$ es [continuamente diferenciable](../15-multivariable-differentiation.md#sec-15-1) en $`a`$.
2. Si $`E`$ es abierto y $`f`$ es continuamente diferenciable en cada punto de $`E`$, entonces $`f`$ es continuamente diferenciable en $`E`$.

## Referencias cruzadas

Esta transcripción coincide temáticamente con las siguientes secciones del registro ruso (material del semestre 2, lecciones 33–64): [§6.1 — diferenciabilidad, Jacobiano y gradiente](../../ru/lectures/14-differentiability-6-1.md), [§6.2 — reglas de derivación](../../ru/lectures/15-differentiation-rules-6-2.md) y [§6.3 — diferenciabilidad continua](../../ru/lectures/16-continuous-differentiability-6-3.md). El [índice del registro](../../ru/lectures/index.md) ofrece la navegación general.
