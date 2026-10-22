---
title: "Derivación de aplicaciones de varias variables"
lang: es
chapter: 15
part: "Varias variables y topología"
---
# 15. Derivación de aplicaciones de varias variables

[Anterior](14-several-variables.md) · [Índice](index.md) · [Siguiente](16-implicit-functions-extrema.md)

> **Objetivo.** Usar la derivada total como aplicación lineal y relacionarla con derivadas parciales, gradientes y aproximaciones de orden superior.

## 15.1 Derivada total

Para $F:D\subseteq\mathbb R^n\to\mathbb R^m$ y un punto interior $a$, la derivada es una aplicación lineal $DF(a):\mathbb R^n\to\mathbb R^m$ tal que

$$
F(a+h)=F(a)+DF(a)h+o(\|h\|)\qquad(h\to0).
$$

Equivalentemente, $\|F(a+h)-F(a)-DF(a)h\|/\|h\|\to0$. La derivabilidad implica continuidad. La matriz de $DF(a)$ en coordenadas estándar es la **matriz jacobiana**.

Para una $f$ escalar, la derivada se representa mediante el gradiente $\nabla f(a)$:

$$
f(a+h)=f(a)+\nabla f(a)\cdot h+o(\|h\|).
$$

El gradiente señala la dirección de mayor crecimiento entre direcciones unitarias, con derivada direccional máxima $\|\nabla f(a)\|$.

## 15.2 Derivadas parciales y direccionales

Las derivadas parciales son

$$
\frac{\partial f}{\partial x_i}(a)
=\lim_{t\to0}\frac{f(a+te_i)-f(a)}t.
$$

Si $F$ es derivable, todas las parciales existen y

$$
DF(a)=\left(\frac{\partial F_i}{\partial x_j}(a)\right)_{i,j}.
$$

El recíproco exige cuidado: la existencia de parciales, incluso cerca de $a$, no garantiza derivabilidad. Una condición suficiente es que todas existan cerca de $a$ y sean continuas en $a$; entonces $F$ es derivable en $a$.

La derivada direccional según $v$ es

$$
D_vf(a)=\left.\frac{d}{dt}f(a+tv)\right|_{t=0}.
$$

Si $f$ es derivable, $D_vf(a)=\nabla f(a)\cdot v$. La existencia de todas las derivadas direccionales tampoco basta por sí sola.

## 15.3 Regla de la cadena y planos tangentes

Si $F$ es derivable en $a$ y $G$ en $F(a)$, entonces

$$
D(G\circ F)(a)=DG(F(a))\,DF(a),
$$

con producto matricial. Esta fórmula contiene todas las reglas de la cadena multivariables.

Para $f(x,y)$ derivable en $(a,b)$, el plano tangente a su gráfica es

$$
z=f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b).
$$

Una superficie de nivel $F(x,y,z)=c$ con $\nabla F(a)\ne0$ tiene plano tangente $\nabla F(a)\cdot(x-a)=0$. El gradiente es normal al conjunto de nivel.

## 15.4 Derivadas superiores y Taylor

Una función es $C^k$ si todas las derivadas parciales hasta orden $k$ existen y son continuas.

> **Teorema de Clairaut–Schwarz.** Si las segundas parciales mixtas son continuas cerca de un punto, se puede intercambiar el orden: $f_{xy}=f_{yx}$.

Para $f\in C^2$, la hessiana $Hf(a)$ es la matriz simétrica de segundas parciales. El desarrollo de Taylor de segundo orden es

$$
f(a+h)=f(a)+\nabla f(a)\cdot h
+\frac12h^{T}Hf(a)h+o(\|h\|^2).
$$

La forma cuadrática $h^THh$ describe la curvatura local y es central para los extremos del capítulo siguiente.

## Ejemplo resuelto

Sea $f(x,y)=x^2e^y$ y $a=(1,0)$. Entonces

$$
f(a)=1,\qquad \nabla f=(2xe^y,x^2e^y),\qquad \nabla f(a)=(2,1).
$$

La aproximación lineal es $f(1+h,k)\approx1+2h+k$. Para la dirección unitaria $v=(3/5,4/5)$,

$$
D_vf(a)=(2,1)\cdot(3/5,4/5)=2.
$$

## Errores frecuentes

1. Las derivadas parciales no prueban por sí solas derivabilidad total.
2. La jacobiana representa una aplicación lineal, no solo una tabla de números.
3. El gradiente es normal a un conjunto de nivel; para una gráfica $z=f(x,y)$, el plano tangente usa la aproximación lineal.

## Ejercicios

1. Calcula la matriz jacobiana y su determinante para $F(r,\theta)=(r\cos\theta,r\sin\theta)$.
2. Halla el plano tangente a $z=x^2+y^2$ en $(1,1,2)$.
3. Calcula la hessiana de $f(x,y)=x^2e^y$ en $(1,0)$.

<details>
<summary>Respuestas breves</summary>

1. Las filas son $(\cos\theta,-r\sin\theta)$ y $(\sin\theta,r\cos\theta)$; el determinante es $r$.
2. $z-2=2(x-1)+2(y-1)$.
3. La hessiana en $(1,0)$ es $\begin{pmatrix}2&2\\2&1\end{pmatrix}$.
</details>

---

[Anterior](14-several-variables.md) · [Índice](index.md) · [Siguiente](16-implicit-functions-extrema.md)
