---
title: "Lección 53 — longitud de caminos y trabajo"
lang: es
course: "Математический анализ, 2025/26"
lecture: 53
semester: 2
date: 2026-04-23
source: "ма25_26_лекция_53_notes.pdf.txt"
pdf_pages: 20
typed_slides: 11
---

# Lección 53 — longitud de caminos y trabajo

[Índice de lecciones](index.md) · [Русский](../../ru/lectures-2025-26/lecture-53.md) · [English](../../en/lectures-2025-26/lecture-53.md) · [Anterior: 49-50](lecture-49-50.md) · [Siguiente: 54](lecture-54.md)


> **Fuente y cobertura.** `ма25_26_лекция_53_notes.pdf.txt`: 20 páginas PDF, 11 diapositivas impresas y 9 páginas manuscritas; fecha 23 de abril de 2026. Se incluyen las páginas manuscritas 6–12 y 15–16. Se utilizó solo el PDF adjunto; no se consultó la carpeta de fuentes.

> **Duplicación del semestre 2.** Esta lección coincide con [§4.7](../../ru/lectures/08-integral-applications-4-7.md); véase también el [registro](../../ru/lectures/index.md). El semestre 2 abarca las lecciones 33–64. Corrección editorial: en la página PDF 14 los límites impresos son $a,b$, aunque la curva está definida en $[\alpha,\beta]$; la parametrización y la deducción manuscrita de las páginas 15–16 indican integrar de $\alpha$ a $\beta$. En la página PDF 19 las sumas imprimen $f$ en vez de la fuerza $F$; abajo se usa $F$ y se señala la discrepancia.

## Diapositiva impresa 1 (pp. PDF 1) — Portada

«Análisis matemático», lección 53; 23 de abril de 2026.

## Diapositiva impresa 2 (pp. PDF 2) — Cita del día: juego Estudiante–Docente

Las matrices de pagos del estudiante y del docente comparan las estrategias «estudiar» y «no esforzarse» del estudiante con «aprobar» y «suspender» del docente.

## Diapositiva impresa 3 (pp. PDF 3) — Objetivo

Concluir las aplicaciones de la integral de Riemann: longitud de curvas y trabajo de una fuerza variable.

## Diapositiva impresa 4 (pp. PDF 4) — Longitud del camino y derivada

Para un camino diferenciable, las derivadas coordenadas forman el vector $\gamma'$; su norma euclídea es la velocidad instantánea.


$$
\|\gamma'(t)\|=\sqrt{\sum_{i=1}^{m}(\gamma_i'(t))^2}
$$

## Diapositiva impresa 5 (pp. PDF 5) — Teorema de la longitud de un camino suave

**Teorema 4.7.1.** Un camino suave es rectificable y su longitud es la integral de la norma de su derivada. El caso a trozos suave se deduce por aditividad. Para $\gamma=(\varphi,\psi)$ en el plano, el integrando es $\sqrt{\varphi'{}^2+\psi'{}^2}$.


$$
s_\gamma=\int_a^b\|\gamma'(t)\|\,dt
$$


$$
s_\gamma=\int_a^b\sqrt{\varphi'(t)^2+\psi'(t)^2}\,dt
$$

## Página manuscrita (pp. PDF 6) — Demostración de longitud: partición coordenada

Se divide el intervalo del parámetro en tramos pequeños. En cada uno, el incremento del camino se estima mediante valores de las derivadas coordenadas en puntos intermedios. La longitud de la cuerda da una cota inferior y la variación coordenada controla la longitud del arco.

## Página manuscrita (pp. PDF 7) — Extremos coordenados

En cada subintervalo se toman mínimos y máximos distintos para cada coordenada de la derivada. Las sumas inferiores de cuerdas y las cotas superiores por variación coordenada encierran la longitud.

## Página manuscrita (pp. PDF 8) — Control de las sumas superior e inferior

La continuidad de las derivadas en un intervalo compacto implica continuidad uniforme: la oscilación de cada derivada coordenada es pequeña en subintervalos cortos.

## Página manuscrita (pp. PDF 9) — Nota editorial sobre las sumas

La nota roja advierte que las sumas construidas con extremos coordenados no son automáticamente sumas de Darboux de la norma euclídea del vector derivada. Este paso requiere una estimación aparte; la diferencia se controla después mediante continuidad uniforme de las componentes.

## Página manuscrita (pp. PDF 10) — Convergencia a la integral

En un intervalo corto el vector derivada cambia muy poco. La continuidad de la norma euclídea permite sustituir las cotas de extremos coordenados por sumas integrales de la función velocidad.

## Página manuscrita (pp. PDF 11) — Fin de la demostración

Cuando la malla tiende a cero, las cotas de longitud coinciden con la integral de la velocidad. Por la definición como supremo de las poligonales inscritas se obtiene la fórmula.


![Deducción manuscrita (pp. PDF 11)](../../assets/lectures-2025-26/lec53-p11-length-estimate.jpg)

## Página manuscrita (pp. PDF 12) — Límite de las cotas

Para cualquier tolerancia positiva, la continuidad uniforme permite elegir una partición suficientemente fina para que la diferencia total entre las cotas superior e inferior sea menor que esa tolerancia; así concluye la demostración.

## Diapositiva impresa 6 (pp. PDF 13) — Longitud de una gráfica

**Corolario 4.7.1.** La gráfica de una función $C^1[a,b]$ es rectificable; su longitud es la integral de la velocidad de la parametrización $\Gamma_f(t)=(t,f(t))$.




$$
s_{\Gamma_f}=\int_a^b\sqrt{1+f'(t)^2}\,dt
$$

$$
\Gamma_f(t)=(t,f(t))
$$

## Diapositiva impresa 7 (pp. PDF 14) — Longitud de un camino en coordenadas polares

**Corolario 4.7.2.** Cuando $r=f(\theta)$, la longitud se obtiene integrando la raíz de la suma de los cuadrados del radio y su derivada.





$$
\gamma(\theta)=(f(\theta)\cos\theta,f(\theta)\sin\theta),\qquad \theta\in[\alpha,\beta]
$$


$$
s_\gamma=\int_\alpha^\beta\sqrt{f(\theta)^2+f'(\theta)^2}\,d\theta
$$

## Página manuscrita (pp. PDF 15) — Parametrización polar

Sea el radio polar una función f del ángulo θ en el intervalo de α a β. Las coordenadas del camino son f(θ) multiplicada respectivamente por cos θ y sin θ. Al derivar aparecen términos mixtos de signos opuestos.

![Deducción manuscrita (pp. PDF 15)](../../assets/lectures-2025-26/lec53-p15-polar-path.jpg)

## Página manuscrita (pp. PDF 16) — Simplificación de la velocidad polar

Al desarrollar los cuadrados se cancelan los términos mixtos porque seno al cuadrado más coseno al cuadrado es uno. El cuadrado de la velocidad es la suma del cuadrado de la derivada del radio y del radio; al integrar se obtiene la fórmula polar.

![Deducción manuscrita (pp. PDF 16)](../../assets/lectures-2025-26/lec53-p16-polar-path.jpg)

## Diapositiva impresa 8 (pp. PDF 17) — Trabajo de una fuerza variable

Un punto material se desplaza por una recta numérica. La fuerza $F$ es paralela al eje; el signo de $F(x)$ indica su sentido respecto del eje elegido.


$$
F:E\subset\mathbb R\to\mathbb R
$$


$$
F(x)>0
$$


$$
F(x)<0
$$

## Diapositiva impresa 9 (pp. PDF 18) — Aditividad del trabajo

El trabajo es aditivo en intervalos. Si la fuerza está entre $m$ y $M$, su trabajo queda entre los trabajos de las fuerzas constantes $m$ y $M$ en ese intervalo.


$$
m(b-a)\le A_F([a,b])\le M(b-a)
$$

## Diapositiva impresa 10 (pp. PDF 19) — Trabajo de una fuerza continua

Para una fuerza continua, las sumas inferiores y superiores de Darboux acotan el trabajo. En las sumas impresas aparece $f$ en vez de $F$; se corrige editorialmente.


> **Редакторское исправление.** В печатной строке PDF буква $f$ использована вместо уже обозначенной силы $F$; в определении сумм исправлено на $F$.


$$
m_k=\inf_{x\in[x_k,x_{k+1}]}F(x),\qquad M_k=\sup_{x\in[x_k,x_{k+1}]}F(x)
$$


$$
s_\tau=\sum_{k=0}^{n-1}m_k\Delta x_k,\qquad S_\tau=\sum_{k=0}^{n-1}M_k\Delta x_k
$$


$$
s_\tau\le A_F([a,b])\le S_\tau
$$

## Diapositiva impresa 11 (pp. PDF 20) — Fórmula del trabajo

Al pasar a la integral se obtiene el trabajo de la fuerza al desplazar el cuerpo de $a$ a $b$. Para una fuerza de dirección arbitraria solo contribuye la componente paralela al movimiento.


$$
A_F([a,b])=\int_a^bF(x)\,dx
$$


---

[Índice de lecciones](index.md) · [Русский](../../ru/lectures-2025-26/lecture-53.md) · [English](../../en/lectures-2025-26/lecture-53.md) · [Anterior: 49-50](lecture-49-50.md) · [Siguiente: 54](lecture-54.md)
