---
title: "Derivación en una variable"
lang: es
chapter: 6
part: "Cálculo de una variable"
aliases: ["Derivación en una variable (es)"]
tags: [mathinmind/es, mathinmind/chapter]
---
# 6. Derivación en una variable

[[es/05-limits-continuity|← 5. Límites y continuidad de funciones]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/07-taylor-convexity|7. Teoremas del valor medio, Taylor y convexidad →]]

> [!abstract] Objetivo
> Interpretar la [[#6.1 Definición y aproximación lineal|derivada]] como aproximación lineal local y aplicar con seguridad las reglas de derivación.

## 6.1 Definición y aproximación lineal

La derivada de $f$ en $a$ es

$$
f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}h
$$

cuando este límite finito existe. Equivalentemente,

$$
f(a+h)=f(a)+f'(a)h+o(h)\qquad(h\to0).
$$

Así, $L(h)=f(a)+f'(a)h$ es la mejor aproximación lineal cerca de $a$. La recta tangente es $y=f(a)+f'(a)(x-a)$.

La derivabilidad implica continuidad porque

$$
f(a+h)-f(a)=h\frac{f(a+h)-f(a)}h\to0.
$$

El recíproco es falso: $|x|$ es continua pero no derivable en cero, pues los cocientes incrementales laterales son $-1$ y $1$.

Las derivadas laterales se definen mediante [[es/05-limits-continuity#5.1 Límite en un punto|límites laterales]]. Existe la derivada bilateral finita exactamente cuando ambas existen y coinciden.

## 6.2 Reglas de derivación

Para $f,g$ derivables y constantes $\alpha,\beta$,

$$
(\alpha f+\beta g)'=\alpha f'+\beta g',
$$
$$
(fg)'=f'g+fg',
\qquad
\left(\frac fg\right)'=\frac{f'g-fg'}{g^2}\quad(g\ne0).
$$

> [!theorem] Regla de la cadena
> Si $f$ es derivable en $a$ y $g$ en $f(a)$, entonces
> $$
> (g\circ f)'(a)=g'(f(a))f'(a).
> $$

^chain-rule

Si $f$ es derivable y estrictamente monótona cerca de $a$, con $f'(a)\ne0$, la [[es/01-logic-sets-functions#1.4 Funciones|función inversa]] cumple

$$
(f^{-1})'(f(a))=\frac1{f'(a)}.
$$

Derivadas básicas:

$$
(x^p)'=px^{p-1},\quad (e^x)'=e^x,\quad(\log x)'=\frac1x,
$$
$$
(\sin x)'=\cos x,\quad(\cos x)'=-\sin x,\quad(\arctan x)'=\frac1{1+x^2}.
$$

Para $f(x)>0$, la derivación logarítmica da
$(f^g)'=f^g(g'\log f+gf'/f)$.

## 6.3 Diferenciales y curvas paramétricas

La diferencial $df(a;h)=f'(a)h$ es la parte lineal del incremento. La notación $dy=f'(x)\,dx$ es útil para aproximaciones y sustituciones, pero $dy/dx$ se define mediante la derivada, no como cociente literal de números.

Si $x=\varphi(t)$, $y=\psi(t)$ son derivables y $\varphi'(t)\ne0$, entonces

$$
\frac{dy}{dx}=\frac{\psi'(t)}{\varphi'(t)}.
$$

Las derivadas de orden superior se definen por $f^{(n+1)}=(f^{(n)})'$. La fórmula de Leibniz es

$$
(fg)^{(n)}=\sum_{k=0}^{n}\binom nk f^{(k)}g^{(n-k)}.
$$

## 6.4 Información local

> [!theorem] Teorema de Fermat
> Si $f$ tiene un extremo local en un punto interior $a$ y es derivable allí, entonces $f'(a)=0$.

^fermat-theorem

El recíproco es falso: $x^3$ tiene derivada cero en el origen pero no extremo. Si $f'(x)>0$ en un intervalo, $f$ es estrictamente creciente, por el [[es/07-taylor-convexity#^lagrange-mean-value-theorem|teorema del valor medio]].

> [!theorem] Propiedad de Darboux
> Una derivada no tiene que ser continua, pero en un intervalo toma cada valor entre dos cualesquiera de sus valores.

^darboux-property

Por ello una derivada no puede tener una [[es/05-limits-continuity#5.3 Continuidad|discontinuidad de salto]], aunque puede oscilar. Un ejemplo clásico es $x^2\sin(1/x)$ fuera de cero, completado con valor cero en el origen.

## Ejemplo resuelto

Derivamos $f(x)=x^x$ para $x>0$. Escribimos $f(x)=e^{x\log x}$. Por la [[#^chain-rule|regla de la cadena]],

$$
f'(x)=e^{x\log x}(\log x+1)=x^x(\log x+1).
$$

La derivada es negativa en $(0,1/e)$ y positiva en $(1/e,\infty)$, así que el mínimo está en $x=1/e$.

## Errores frecuentes

1. La continuidad no implica derivabilidad.
2. La regla de la cadena exige multiplicar por la derivada interior.
3. $f'(a)=0$ define un punto estacionario, no automáticamente un extremo.

## Ejercicios

1. Usa la definición para derivar $1/x$ en $a\ne0$.
2. Deriva $\arcsin x$ mediante la regla de la función inversa.
3. Halla la tangente a $x=t^2$, $y=t^3$ en $t=1$.

> [!answer]- Respuestas breves
> 1. El cociente incremental tiende a $-1/a^2$.
> 2. $(\arcsin x)'=1/\sqrt{1-x^2}$ para $|x|<1$.
> 3. $dy/dx=3t/2$, luego la pendiente en $(1,1)$ es $3/2$; la recta es $y-1=\frac32(x-1)$.

---

[[es/05-limits-continuity|← 5. Límites y continuidad de funciones]] · [[es/index|Índice]] · [[es/term-index|Términos y teoremas]] · [[es/07-taylor-convexity|7. Teoremas del valor medio, Taylor y convexidad →]]
