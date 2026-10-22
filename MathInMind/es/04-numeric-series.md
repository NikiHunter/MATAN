---
title: "Series numéricas"
lang: es
chapter: 4
part: "Fundamentos"
---
# 4. Series numéricas

[Anterior](03-sequences.md) · [Índice](index.md) · [Siguiente](05-limits-continuity.md)

> **Objetivo.** Distinguir los tipos de convergencia y elegir un criterio adecuado.

## 4.1 Sumas parciales

Para $\sum_{n=1}^{\infty}a_n$, definimos $s_N=\sum_{n=1}^N a_n$. La serie converge a $s$ si $s_N\to s$. En ese caso $a_n=s_n-s_{n-1}\to0$. El recíproco es falso, como muestra la serie armónica.

La serie geométrica cumple

$$
\sum_{n=0}^{\infty}q^n=\frac1{1-q}\quad(|q|<1),
$$

y diverge si $|q|\ge1$. Un ejemplo telescópico es

$$
\sum_{n=1}^{\infty}\frac1{n(n+1)}
=\sum_{n=1}^{\infty}\left(\frac1n-\frac1{n+1}\right)=1.
$$

El criterio de Cauchy afirma que para todo $\varepsilon>0$ existe $N$ tal que $m\ge n\ge N$ implica $|a_n+\cdots+a_m|<\varepsilon$.

## 4.2 Términos no negativos

Si $a_n\ge0$, las sumas parciales crecen, de modo que la serie converge exactamente cuando están acotadas.

- **Comparación:** si finalmente $0\le a_n\le b_n$, la convergencia de $\sum b_n$ implica la de $\sum a_n$, y la divergencia de $\sum a_n$ implica la de $\sum b_n$.
- **Comparación asintótica:** si $a_n,b_n>0$ y $a_n/b_n\to c\in(0,\infty)$, ambas series se comportan igual.
- **Cociente:** si $\lim |a_{n+1}/a_n|=r$, entonces $r<1$ da convergencia absoluta y $r>1$ divergencia. Si $r=1$, no hay conclusión.
- **Raíz:** si $\limsup\sqrt[n]{|a_n|}=r$, valen las mismas conclusiones.
- **Integral:** para $f$ positiva y decreciente, $\sum f(n)$ e $\int_1^\infty f(x)\,dx$ convergen o divergen a la vez.

En particular,

$$
\sum_{n=1}^{\infty}\frac1{n^p}<\infty\iff p>1.
$$

Para $a_n$ positivas y decrecientes también sirve la condensación de Cauchy: $\sum a_n$ converge exactamente cuando lo hace $\sum 2^k a_{2^k}$.

## 4.3 Convergencia absoluta y condicional

Una serie **converge absolutamente** si $\sum|a_n|$ converge. La convergencia absoluta implica la ordinaria por el criterio de Cauchy. Si converge, pero no absolutamente, la convergencia es **condicional**.

> **Criterio de Leibniz.** Si $b_n\ge0$ decrece hacia cero, entonces $\sum(-1)^{n-1}b_n$ converge. La suma queda entre sumas parciales consecutivas y el resto cumple $|R_N|\le b_{N+1}$.

Por ello $\sum(-1)^{n-1}/n$ converge condicionalmente. Criterios más generales:

- **Dirichlet:** si las sumas parciales de $\sum a_n$ están acotadas y $b_n$ decrece a $0$, entonces $\sum a_nb_n$ converge;
- **Abel:** si $\sum a_n$ converge y $(b_n)$ es monótona y acotada, entonces $\sum a_nb_n$ converge.

> **Advertencia sobre reordenaciones.** Reordenar una serie absolutamente convergente conserva su suma. Una serie real condicionalmente convergente puede reordenarse para obtener cualquier suma real prescrita o para diverger (teorema de Riemann).

## Ejemplo resuelto

Estudiamos $\sum_{n=2}^{\infty}1/(n(\log n)^p)$. La condensación produce

$$
\sum_k 2^k\frac1{2^k(k\log2)^p}
=C\sum_k\frac1{k^p}.
$$

Por tanto, hay convergencia exactamente cuando $p>1$. Aquí el criterio ordinario del cociente no decide.

## Errores frecuentes

1. $a_n\to0$ es necesario, pero no suficiente.
2. Los criterios del cociente y de la raíz no deciden cuando el límite es $1$.
3. En convergencia condicional no se pueden reordenar términos arbitrariamente sin justificación.

## Ejercicios

1. Estudia la convergencia de $\sum n!/(n^n)$.
2. Prueba que $\sum(-1)^n/\sqrt n$ converge condicionalmente.
3. ¿Converge $\sum(\sqrt{n^2+1}-n)$?

<details>
<summary>Respuestas breves</summary>

1. El cociente tiende a $1/e<1$, así que la serie converge por el criterio del cociente.
2. Se aplica Leibniz, pero $\sum1/\sqrt n$ diverge.
3. Al racionalizar, el término es $1/(\sqrt{n^2+1}+n)\sim1/(2n)$; la serie diverge.
</details>

---

[Anterior](03-sequences.md) · [Índice](index.md) · [Siguiente](05-limits-continuity.md)
