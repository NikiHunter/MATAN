---
title: "Teoremas del valor medio, Taylor y convexidad"
lang: es
chapter: 7
part: "Cálculo de una variable"
---
# 7. Teoremas del valor medio, Taylor y convexidad

[← 6. Derivación en una variable](06-derivatives.md) · [Índice](index.md) · [Términos y teoremas](term-index.md) · [8. La integral de Riemann →](08-riemann-integration.md)

> **Objetivo.** Convertir información local de la [derivada](06-derivatives.md#sec-6-1) en estimaciones globales, aproximaciones y propiedades geométricas.

<a id="sec-7-1"></a>
## 7.1 Teoremas del valor medio

> <a id="rolle-theorem"></a>**Teorema de Rolle.** Si $`f`$ es continua en $`[a,b]`$, derivable en $`(a,b)`$ y $`f(a)=f(b)`$, existe $`c\in(a,b)`$ con $`f'(c)=0`$.

Por el [teorema de Weierstrass](05-limits-continuity.md#extreme-value-theorem), la función alcanza extremos. Si no es constante, alguno es interior.

> <a id="lagrange-mean-value-theorem"></a>**Teorema de Lagrange.** Con las mismas hipótesis de continuidad y derivabilidad, existe $`c\in(a,b)`$ tal que
> ```math
> f(b)-f(a)=f'(c)(b-a).
> ```

Consecuencias: derivada nula en un intervalo implica función constante; derivadas iguales implican diferencia constante; $`|f'|\le M`$ implica $`|f(x)-f(y)|\le M|x-y|`$.

> <a id="cauchy-mean-value-theorem"></a>**Teorema de Cauchy.** Para $`f,g`$ adecuadas con $`g'(x)\ne0`$ en $`(a,b)`$, existe $`c`$ tal que
> ```math
> \frac{f(b)-f(a)}{g(b)-g(a)}=\frac{f'(c)}{g'(c)}.
> ```

<a id="sec-7-2"></a>
## 7.2 Regla de L'Hôpital

Para formas indeterminadas $`0/0`$ o $`\infty/\infty`$, bajo las condiciones habituales de derivabilidad y denominador,

```math
\lim_{x\to a}\frac{f(x)}{g(x)}
=\lim_{x\to a}\frac{f'(x)}{g'(x)}
```

si el segundo límite existe, finito o infinito. También vale en el infinito y para [límites laterales](05-limits-continuity.md#sec-5-1). No se aplica a todo cociente; la inexistencia del límite de derivadas no refuta por sí sola el límite original.

Para $`0\cdot\infty`$, $`\infty-\infty`$, $`1^\infty`$, $`0^0`$ o $`\infty^0`$, primero se reescribe la expresión mediante álgebra o logaritmos.

<a id="sec-7-3"></a>
## 7.3 Fórmula de Taylor

Si $`f`$ tiene suficientes derivadas cerca de $`a`$, su polinomio de Taylor es

```math
P_n(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k.
```

La fórmula con resto de Lagrange afirma

```math
f(x)=P_n(x)+R_n(x),\qquad
R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}
```

para algún $`\xi`$ entre $`a`$ y $`x`$, con las hipótesis de regularidad correspondientes. La forma de Peano es $`R_n(x)=o((x-a)^n)`$ cuando $`x\to a`$.

En cero son útiles

```math
e^x=\sum_{k=0}^{n}\frac{x^k}{k!}+O(x^{n+1}),
```
```math
\sin x=\sum_{k=0}^{n}\frac{(-1)^kx^{2k+1}}{(2k+1)!}+O(x^{2n+3}),
```
```math
\log(1+x)=\sum_{k=1}^{n}\frac{(-1)^{k-1}x^k}{k}+O(x^{n+1}).
```

Las cotas del resto justifican aproximaciones numéricas; el polinomio por sí solo no prueba convergencia de una serie infinita.

<a id="sec-7-4"></a>
## 7.4 Funciones convexas

Una función $`f`$ es convexa en un intervalo $`I`$ si para todos $`x,y\in I`$ y $`t\in[0,1]`$

```math
f((1-t)x+ty)\le(1-t)f(x)+tf(y).
```

Geométricamente, cada cuerda queda por encima de la gráfica. En convexidad estricta la desigualdad es estricta para $`x\ne y`$ y $`0<t<1`$.

- Una $`f`$ derivable es convexa exactamente cuando $`f'`$ es no decreciente.
- Si $`f''\ge0`$, entonces $`f`$ es convexa; $`f''>0`$ da convexidad estricta.
- Para $`f`$ derivable, la convexidad equivale a

  $`\displaystyle f(y)\ge f(x)+f'(x)(y-x).`$

> <a id="jensen-inequality"></a>**Desigualdad de Jensen.** Para $`f`$ convexa, pesos $`\lambda_i\ge0`$ con suma $`1`$ y puntos $`x_i`$,
> ```math
> f\left(\sum_{i=1}^{n}\lambda_i x_i\right)\le\sum_{i=1}^{n}\lambda_i f(x_i).
> ```

Aplicada a $`-\log x`$ da la desigualdad entre medias aritmética y geométrica. Un punto donde cambia la concavidad es de inflexión; $`f''(a)=0`$ no basta por sí solo.

## Ejemplo resuelto

Probemos $`e^x\ge1+x`$. La función $`e^x`$ es convexa y su tangente en $`0`$ es $`1+x`$. La desigualdad de la tangente da el resultado, con igualdad solo en $`x=0`$.

## Errores frecuentes

1. El punto $`c`$ del valor medio no tiene que ser único ni explícito.
2. Un [polinomio de Taylor](#sec-7-3) finito y una [serie de Taylor](11-power-series.md#sec-11-3) infinita son afirmaciones distintas.
3. $`f''(a)=0`$ no demuestra por sí solo una inflexión.

## Ejercicios

1. Prueba $`|\sin x-\sin y|\le|x-y|`$.
2. Aproxima $`\sqrt{1+x}`$ hasta orden dos y estima el error para $`x>0`$ pequeño.
3. Demuestra $`x\log x\ge x-1`$ para $`x>0`$ mediante convexidad o una tangente.

<details>
<summary>Respuestas breves</summary>

1. Aplica Lagrange y usa $`|\cos c|\le1`$.
2. $`\sqrt{1+x}=1+x/2-x^2/8+O(x^3)`$; acota la tercera derivada en el intervalo adecuado para estimar el resto.
3. La tangente a $`x\log x`$ en $`x=1`$ es $`x-1`$, y la segunda derivada $`1/x`$ es positiva.
</details>

---

[← 6. Derivación en una variable](06-derivatives.md) · [Índice](index.md) · [Términos y teoremas](term-index.md) · [8. La integral de Riemann →](08-riemann-integration.md)
