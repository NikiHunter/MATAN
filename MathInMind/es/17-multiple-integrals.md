---
title: "Integrales múltiples y cambio de variables"
lang: es
chapter: 17
part: "Integración en varias variables"
---
# 17. Integrales múltiples y cambio de variables

[Anterior](16-implicit-functions-extrema.md) · [Índice](index.md) · [Siguiente](18-vector-calculus.md)

> **Objetivo.** Calcular integrales en regiones multidimensionales mediante iteración, simetría y cambios geométricos de coordenadas.

## 17.1 Definición e integrales iteradas

Para una función acotada en un rectángulo $R=\prod_{i=1}^{n}[a_i,b_i]$, las particiones en rectángulos pequeños definen sumas inferior y superior de Darboux con volúmenes $\Delta V_j$. La integrabilidad vuelve a significar que ambas sumas pueden acercarse arbitrariamente. Las funciones continuas en regiones cerradas, acotadas y medibles Jordan son integrables.

> **Teorema de Fubini — caso continuo.** Si $f$ es continua en $R=[a,b]\times[c,d]$, entonces
> $$\iint_R f(x,y)\,dA
> =\int_a^b\left(\int_c^d f(x,y)\,dy\right)dx
> =\int_c^d\left(\int_a^b f(x,y)\,dx\right)dy.$$

Para funciones generales integrables Lebesgue, la integrabilidad absoluta justifica cambiar el orden; el teorema de Tonelli lo permite para funciones medibles no negativas. Véanse los capítulos 19–20.

En una región

$$
D=\{(x,y):a\le x\le b,\ \varphi_1(x)\le y\le\varphi_2(x)\},
$$

se tiene $\iint_Df\,dA=\int_a^b\int_{\varphi_1(x)}^{\varphi_2(x)}f(x,y)\,dy\,dx$. Conviene dibujar la región antes de elegir límites.

## 17.2 Cambio de variables

Sea $T:U\to V$ una transformación $C^1$, inyectiva salvo quizá en un conjunto despreciable, con $DT$ invertible. Entonces

$$
\int_V f(v)\,dv
=\int_U f(T(u))\,|\det DT(u)|\,du.
$$

El valor absoluto del jacobiano mide el cambio local de volumen. Olvidarlo altera el valor; para área y volumen no orientados no se usa el determinante con signo.

Sustituciones importantes:

$$
(x,y)=(r\cos\theta,r\sin\theta),\qquad dA=r\,dr\,d\theta;
$$
$$
(x,y,z)=(r\cos\theta,r\sin\theta,z),\qquad dV=r\,dr\,d\theta\,dz;
$$

y coordenadas esféricas

$$
(x,y,z)=(\rho\sin\varphi\cos\theta,
\rho\sin\varphi\sin\theta,\rho\cos\varphi),
$$
$$
dV=\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta,
$$

donde $\rho\ge0$, $0\le\varphi\le\pi$ y normalmente $0\le\theta<2\pi$.

## 17.3 Elección de coordenadas

Las polares o cilíndricas convienen para discos, sectores, cilindros e integrandos radiales. Las esféricas para bolas, conos y capas. La simetría suele eliminar contribuciones impares antes del cálculo.

Las integrales dobles y triples calculan

$$
\operatorname{area}(D)=\iint_D1\,dA,
\qquad
\operatorname{vol}(\Omega)=\iiint_\Omega1\,dV.
$$

Con densidad $\rho$, la masa es $M=\int_\Omega\rho\,dV$, y el centro de masa tiene coordenadas

$$
\bar x_i=\frac1M\int_\Omega x_i\rho\,dV.
$$

Los momentos de inercia tienen la forma $I=\int_\Omega r^2\rho\,dV$, donde $r$ es la distancia al eje de rotación.

## Ejemplo resuelto

El volumen de una bola $B_R$ se obtiene en esféricas:

$$
V=\int_0^{2\pi}\int_0^\pi\int_0^R
\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta.
$$

Los factores se integran independientemente:

$$
V=\left(\int_0^{2\pi}d\theta\right)
\left(\int_0^\pi\sin\varphi\,d\varphi\right)
\left(\int_0^R\rho^2\,d\rho\right)
=2\pi\cdot2\cdot\frac{R^3}{3}
=\frac{4\pi R^3}{3}.
$$

## Errores frecuentes

1. Los límites iterados describen una región; no se intercambian sin revisar dominio o integrabilidad.
2. Incluye siempre el valor absoluto del jacobiano.
3. Aquí $\varphi$ es el ángulo polar desde el eje $z$ positivo, no el acimut.

## Ejercicios

1. Calcula $\iint_T x\,dA$ en el triángulo $x,y\ge0$, $x+y\le1$.
2. Halla el área de un disco de radio $R$ con polares.
3. Plantea una integral para el volumen dentro de $x^2+y^2+z^2\le2Rz$.

<details>
<summary>Respuestas breves</summary>

1. $\int_0^1\int_0^{1-x}x\,dy\,dx=\int_0^1x(1-x)\,dx=1/6$.
2. $\int_0^{2\pi}\int_0^Rr\,dr\,d\theta=\pi R^2$.
3. La bola es $\rho\le2R\cos\varphi$ con $0\le\varphi\le\pi/2$; $V=\int_0^{2\pi}\int_0^{\pi/2}\int_0^{2R\cos\varphi}\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta$.
</details>

---

[Anterior](16-implicit-functions-extrema.md) · [Índice](index.md) · [Siguiente](18-vector-calculus.md)
