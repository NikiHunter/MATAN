---
title: "Seminar NM-204. HW 4 — series, inequalities and bases: solutions"
lang: en
hw: 4
---
# HW 4. Series, Hölder's inequality and bases of sets — solutions

[Русский](../../ru/seminar-sem3/hw4-series-inequalities-bases.md) · **English** · [Español](../../es/seminar-sem3/hw4-series-inequalities-bases.md)

[← HW 3](hw3-numerical-series.md) · [All assignments](index.md) · [Lectures 69–70, §7.3–§7.4](../lectures-2025-26/lecture-69-70.md)

This page solves the new problems 4.1–4.12. The "old" problems of this assignment are solved earlier: 1.2 in [HW 1](hw1-taylor.md); 2.2 and 2'.1–2'.3 in [HW 2](hw2-conditional-extremum.md); 3.1–3.3, 3.10, 3.11 in [HW 3](hw3-numerical-series.md). The references (F1)–(F3) are the three facts from the beginning of [HW 3](hw3-numerical-series.md): the necessary condition for convergence, the bounded-partial-sums criterion for non-negative series, and the independence of convergence from finitely many terms.

<a id="p-4-1"></a>
## Problem 4.1

**Statement.** $`p>1`$, $`p'=\frac p{p-1}`$, $`b_k\ge0`$, $`\sum_{k=1}^nb_k^{p'}=1`$. Find the points of constrained extremum of $`f(x)=\sum_{k=1}^nb_kx_k`$ on the set $`M=\{x:\ x_k\ge0,\ \sum_{k=1}^nx_k^p=1\}`$.

Useful identities for conjugate exponents: $`\frac1p+\frac1{p'}=1`$, $`p'-1=\frac1{p-1}`$, $`(p-1)p'=p`$.

**Finding the candidate by the Lagrange method.** In the region $`x_k>0`$ the constraint $`\varphi=\sum x_k^p-1`$ is smooth, $`\nabla\varphi=(p\,x_k^{p-1})\ne0`$. System: $`b_k=\lambda p\,x_k^{p-1}`$, whence $`x_k=\bigl(\frac{b_k}{\lambda p}\bigr)^{1/(p-1)}`$ and $`x_k^p=\bigl(\frac{b_k}{\lambda p}\bigr)^{p'}`$. Substituting into the constraint: $`(\lambda p)^{-p'}\sum b_k^{p'}=(\lambda p)^{-p'}=1`$, i.e. $`\lambda p=1`$ and
```math
x_k^*=b_k^{\,1/(p-1)}=b_k^{\,p'-1},\qquad f(x^*)=\sum b_k\cdot b_k^{\,p'-1}=\sum b_k^{\,p'}=1 .
```
The point $`x^*`$ lies on $`M`$: $`\sum(x_k^*)^p=\sum b_k^{(p'-1)p}=\sum b_k^{p'}=1`$.

**Rigorous proof that this is the maximum.** The Lagrange method only gives a candidate, and only inside the region $`x_k>0`$; $`M`$ also has a boundary, where some coordinates vanish. To avoid going through the faces, we prove the estimate directly. For $`u,v\ge0`$ Young's inequality holds:
```math
uv\le\frac{u^p}p+\frac{v^{p'}}{p'},\qquad\text{with equality only when }u^p=v^{p'}.\tag{1}
```
(For fixed $`v>0`$ the function $`\psi(u)=\frac{u^p}p+\frac{v^{p'}}{p'}-uv`$ has derivative $`\psi'(u)=u^{p-1}-v`$, which changes sign from minus to plus at the single point $`u_0=v^{1/(p-1)}`$; there $`u_0^p=v^{p'}`$ and $`\psi(u_0)=v^{p'}\bigl(\frac1p+\frac1{p'}-1\bigr)=0`$. So $`\psi\ge0`$ and $`\psi=0`$ only at $`u=u_0`$. For $`v=0`$ the inequality is obvious.)

Apply (1) with $`u=x_k`$, $`v=b_k`$ and sum over $`k`$: for every $`x\in M`$
```math
f(x)=\sum_{k=1}^nb_kx_k\le\frac1p\sum_{k=1}^nx_k^p+\frac1{p'}\sum_{k=1}^nb_k^{p'}=\frac1p+\frac1{p'}=1,
```
and equality holds only when $`x_k^p=b_k^{p'}`$ for all $`k`$, i.e. at $`x=x^*`$. So $`x^*`$ is the unique point of global maximum, $`f_{\max}=1`$.

**Minimum.** Let $`b_{\min}=\min_kb_k`$. On $`M`$ every $`x_k\in[0,1]`$, so $`x_k\ge x_k^p`$ and $`\sum x_k\ge\sum x_k^p=1`$. Hence
```math
f(x)=\sum b_kx_k\ge b_{\min}\sum x_k\ge b_{\min}.
```
If $`b_{\min}>0`$, equality is possible only when $`\sum x_k=1`$, i.e. when every $`x_k\in\{0,1\}`$: $`x=e_j`$ is a basis vector, and $`b_j=b_{\min}`$. If $`b_{\min}=0`$, the equality $`f(x)=0`$ means $`x_k=0`$ for all $`k`$ with $`b_k>0`$.

**The remaining local extrema.** The substitution $`y_k=x_k^p`$ maps $`M`$ homeomorphically onto the simplex $`\Delta=\{y_k\ge0,\ \sum y_k=1\}`$, and $`f`$ becomes $`F(y)=\sum b_ky_k^{1/p}`$. The function $`t\mapsto t^{1/p}`$ is strictly concave on $`[0;+\infty)`$, so $`F`$ is concave on the convex set $`\Delta`$.

- *There are no local maxima other than $`x^*`$.* A local maximum of a concave function is global: if $`F(y')>F(y)`$, then along the segment $`F(y+t(y'-y))\ge F(y)+t(F(y')-F(y))>F(y)`$ for arbitrarily small $`t>0`$.
- *A local minimum is possible only in two cases.* Suppose that at a point $`y`$ two coordinates $`y_i,y_l`$ are positive and $`b_i>0`$. Then $`g(t)=F(y+t(e_i-e_l))`$ is defined for small $`|t|`$ and strictly concave, so $`g(0)>\frac12(g(t)+g(-t))`$ — no minimum at $`y`$. What remains are the points where $`b_k=0`$ on all positive coordinates (there $`f=0`$, the global minimum) and the vertices $`x=e_j`$.
- *A vertex $`e_j`$ with $`b_j>0`$.* Let $`s=\sum_{k\ne j}x_k^p`$; then $`x_j=(1-s)^{1/p}\ge1-s`$ and
```math
f(x)-b_j=b_j(x_j-1)+\sum_{k\ne j}b_kx_k\ge\sum_{k\ne j}x_k\bigl(b_k-b_jx_k^{p-1}\bigr).
```
If all $`b_k>0`$, the right-hand side is positive for small $`x_k`$ (not all zero): $`e_j`$ is a strict local minimum with value $`b_j`$. If $`b_i=0`$ for some $`i\ne j`$, a shift along $`x_i`$ decreases $`f`$ (since $`x_j<1`$), and there is no minimum.

**Answer.**

1. Maximum: the single point $`x^*=\bigl(b_1^{\,p'-1};\dots;b_n^{\,p'-1}\bigr)`$, $`f(x^*)=1`$ (global; there are no other local maxima).
2. If all $`b_k>0`$: the points of local minimum are the vertices $`e_j`$, $`j=1,\dots,n`$, with values $`f(e_j)=b_j`$; the global minimum $`\min_kb_k`$ is attained at the vertices with the smallest $`b_j`$.
3. If some $`b_k`$ are zero: the points of minimum are all $`x\in M`$ with $`x_k=0`$ whenever $`b_k>0`$; the value is $`0`$ (global minimum); there are no other local minima.

**Why it works.** The function $`f`$ is linear, its level surfaces are parallel hyperplanes with normal $`b`$, and $`M`$ is a convex "piece of a sphere" in the $`\ell_p`$ norm. The maximum is attained where a hyperplane touches $`M`$, i.e. where the normal $`(p\,x_k^{p-1})`$ to the surface is proportional to $`b`$. For $`p=2`$ this means $`x^*=b`$ (a unit vector in the direction of $`b`$) — the usual Cauchy–Schwarz inequality; for $`p\ne2`$ the "same direction" is distorted by the power $`p'-1`$. The minimum of a linear function on such a set goes to the edge — to the "corners" $`e_j`$ — because between the corners the surface bulges outwards.

The condition $`\sum b_k^{p'}=1`$ is a normalisation. It is what makes the maximum equal exactly $`1`$; this is Hölder's inequality for normalised tuples (problem 4.2).

<a id="p-4-2"></a>
## Problem 4.2 (Hölder's inequality)

**Statement.** $`p>1`$, $`p'=\frac p{p-1}`$, all numbers are non-negative. Prove:

1) $`\displaystyle\sum_{k=1}^na_kb_k\le\Bigl(\sum_{k=1}^na_k^p\Bigr)^{1/p}\Bigl(\sum_{k=1}^nb_k^{p'}\Bigr)^{1/p'}`$;

2) if the series $`\sum x_k^p`$ and $`\sum y_k^{p'}`$ converge, then $`\sum x_ky_k`$ converges and $`\displaystyle\sum_{k=1}^\infty x_ky_k\le\Bigl(\sum_{k=1}^\infty x_k^p\Bigr)^{1/p}\Bigl(\sum_{k=1}^\infty y_k^{p'}\Bigr)^{1/p'}`$.

**Proof of 1).** Put $`A=\bigl(\sum a_k^p\bigr)^{1/p}`$, $`B=\bigl(\sum b_k^{p'}\bigr)^{1/p'}`$.

If $`A=0`$, all $`a_k=0`$ and both sides are zero; similarly for $`B=0`$.

Let $`A>0`$ and $`B>0`$. Put $`\tilde a_k=\frac{a_k}A`$, $`\tilde b_k=\frac{b_k}B`$. Then
```math
\sum_{k=1}^n\tilde a_k^{\,p}=\frac{1}{A^p}\sum a_k^p=1,\qquad\sum_{k=1}^n\tilde b_k^{\,p'}=1 .
```
The tuple $`\tilde b`$ satisfies the hypothesis of problem 4.1, and the point $`\tilde a`$ lies in its set $`M`$. In 4.1 it is proved that $`f\le1`$ on $`M`$:
```math
\sum_{k=1}^n\tilde a_k\tilde b_k\le1 .
```
Multiplying by $`AB>0`$ gives $`\sum a_kb_k\le AB`$. $`\blacksquare`$

**Proof of 2).** Let $`X=\sum_{k=1}^\infty x_k^p`$, $`Y=\sum_{k=1}^\infty y_k^{p'}`$. The terms of these series are non-negative, so their partial sums do not exceed $`X`$ and $`Y`$. By part 1), for every $`n`$
```math
\sum_{k=1}^nx_ky_k\le\Bigl(\sum_{k=1}^nx_k^p\Bigr)^{1/p}\Bigl(\sum_{k=1}^ny_k^{p'}\Bigr)^{1/p'}\le X^{1/p}\,Y^{1/p'} .
```
The series $`\sum x_ky_k`$ is non-negative and its partial sums are bounded above; by (F2) it converges. Passing to the limit as $`n\to\infty`$ in $`S_n\le X^{1/p}Y^{1/p'}`$ gives the estimate for the sum. $`\blacksquare`$

**Why it works.** The inequality is homogeneous: multiplying all $`a_k`$ by $`t>0`$ multiplies both sides by $`t`$. So it suffices to prove it for tuples of "unit length", and for those it is exactly the statement about the maximum in 4.1. Zero tuples have to be treated separately only because one cannot divide by zero. The passage to series is standard: an inequality for finite sums with a right-hand side independent of $`n`$, plus monotonicity of partial sums.

Meaning: if $`x\in\ell_p`$ and $`y\in\ell_{p'}`$, then $`xy\in\ell_1`$. For $`p=p'=2`$ this is the Cauchy–Schwarz inequality. Equality in 1) holds if and only if the tuples $`(a_k^p)`$ and $`(b_k^{p'})`$ are proportional — the equality condition from 4.1.

<a id="p-4-3"></a>
## Problem 4.3 (bases of sets)

> **At the seminar.** How the base $`n\to\infty`$ is used for series: [Definition 10.1](notes-3-kummer-dalembert-raabe.md#def-10-1) (16 Oct).

**Definition from the statement.** A family $`\mathcal B`$ of non-empty subsets of $`X`$ is a base on $`X`$ if (B1) $`\bigcup_{D\in\mathcal B}D=X`$ and (B2) for any $`D_1,D_2\in\mathcal B`$ there is $`D_3\in\mathcal B`$ with $`D_3\subset D_1\cap D_2`$.

All the families below are **nested**: of any two elements, one is contained in the other. Then (B2) holds automatically: the smaller of the two serves as $`D_3`$, it equals $`D_1\cap D_2`$. So in each case three things have to be checked: non-emptiness of the elements, nestedness, and (B1).

**1) $`\mathcal M_1=\{D_k\}`$, $`D_k=\{n\ge k\}`$, and $`\mathcal M_2=\{E_m\}`$, $`E_m=\{n>m\}`$, on $`\mathbb N`$.**

- $`k\in D_k`$, $`m+1\in E_m`$ — the sets are non-empty.
- $`D_k\cap D_l=D_{\max(k,l)}`$, $`E_m\cap E_l=E_{\max(m,l)}`$ — (B2).
- $`D_1=\mathbb N`$ and $`E_0=\mathbb N`$, so the unions equal $`\mathbb N`$ — (B1).

Note that $`D_k=E_{k-1}`$, so $`\mathcal M_1=\mathcal M_2`$ as families: it is one and the same base $`n\to\infty`$. $`\blacksquare`$

**2) Families on $`\mathbb R`$.**

*$`\mathcal M_4`$, $`A_{2,r}=(-\infty;r)`$.* Non-empty; $`A_{2,r_1}\cap A_{2,r_2}=A_{2,\min(r_1,r_2)}`$; every $`x\in\mathbb R`$ lies in $`A_{2,r}`$ for $`r=|x|+1`$, so the union is $`\mathbb R`$. A base on $`\mathbb R`$. $`\blacksquare`$

*$`\mathcal M_{6,x_0}`$, $`A_{4,r}=(x_0-r;x_0+r)`$.* Non-empty ($`x_0\in A_{4,r}`$); $`A_{4,r_1}\cap A_{4,r_2}=A_{4,\min(r_1,r_2)}`$; every $`x\in\mathbb R`$ lies in $`A_{4,r}`$ for $`r=|x-x_0|+1`$. A base on $`\mathbb R`$. $`\blacksquare`$

*$`\mathcal M_3`$, $`A_{1,r}=(-\infty;-r]\cup[r;+\infty)=\{x:\ |x|\ge r\}`$.* Non-empty; $`A_{1,r_1}\cap A_{1,r_2}=A_{1,\max(r_1,r_2)}`$ — (B2) holds. But
```math
\bigcup_{r>0}A_{1,r}=\{x:\ |x|>0\}=\mathbb R\setminus\{0\},
```
because $`0\notin A_{1,r}`$ for every $`r>0`$, while every $`x\ne0`$ lies in $`A_{1,|x|}`$.

*$`\mathcal M_5`$, $`A_{3,r}=(r;+\infty)`$.* Non-empty; $`A_{3,r_1}\cap A_{3,r_2}=A_{3,\max(r_1,r_2)}`$ — (B2) holds. But
```math
\bigcup_{r>0}A_{3,r}=(0;+\infty),
```
because for $`r>0`$ the set $`A_{3,r}`$ contains no numbers $`x\le0`$.

> **Remark on the statement.** Read literally, condition (B1) for $`\mathcal M_3`$ and $`\mathcal M_5`$ on $`X=\mathbb R`$ **fails**: the unions are $`\mathbb R\setminus\{0\}`$ and $`(0;+\infty)`$. What can be proved is this: $`\mathcal M_3`$ is a base on $`\mathbb R\setminus\{0\}`$, $`\mathcal M_5`$ is a base on $`(0;+\infty)`$; both families satisfy (B2) and consist of non-empty sets, i.e. they are bases on $`\mathbb R`$ in the sense of the definition without requirement (B1) (this is how a base is defined, for example, in Zorich). For (B1) to hold on all of $`\mathbb R`$ the parameter should range not over $`(0;+\infty)`$ but, say, over $`[0;+\infty)`$ for $`\mathcal M_3`$ and over all of $`\mathbb R`$ for $`\mathcal M_5`$. This is probably an inaccuracy in the statement (it has other misprints too: $`\mathcal M_{7,x_0}`$ is used twice; $`A_{2,r}=(-\infty;r)`$ instead of the set $`(-\infty;-r)`$ expected for the base $`x\to-\infty`$) — worth clarifying with the instructor. It does not affect limits: a limit along a base is determined only by the "far" elements of the family.

**3) $`\mathcal M_{7,x_0}`$, $`A_{5,r}=(x_0;x_0+r)`$, on $`(x_0;+\infty)`$ and $`\mathcal M_{8,x_0}`$, $`A_{6,r}=(x_0-r;x_0)`$, on $`(-\infty;x_0)`$.**

- Non-empty: $`x_0+\frac r2\in A_{5,r}`$, $`x_0-\frac r2\in A_{6,r}`$; all $`A_{5,r}\subset(x_0;+\infty)`$, $`A_{6,r}\subset(-\infty;x_0)`$.
- $`A_{5,r_1}\cap A_{5,r_2}=A_{5,\min(r_1,r_2)}`$, $`A_{6,r_1}\cap A_{6,r_2}=A_{6,\min(r_1,r_2)}`$ — (B2).
- Every $`x>x_0`$ lies in $`A_{5,r}`$ for $`r=x-x_0+1`$; every $`x<x_0`$ lies in $`A_{6,r}`$ for $`r=x_0-x+1`$ — (B1). $`\blacksquare`$

(In the statement the second family repeats the name $`\mathcal M_{7,x_0}`$; here it is called $`\mathcal M_{8,x_0}`$.)

**Why it works.** A base is a way of saying "far enough" or "close enough" in one language for all kinds of limits. An element of a base is a "neighbourhood" of where we are heading: $`D_k`$ is "all indices from $`k`$ on" ($`n\to\infty`$); $`A_{1,r}`$ is $`x\to\infty`$; $`A_{3,r}`$ is $`x\to+\infty`$; $`A_{4,r}`$ is $`x\to x_0`$ (with the point $`x_0`$ itself); $`A_{5,r}`$ and $`A_{6,r}`$ are $`x\to x_0+0`$ and $`x\to x_0-0`$. Condition (B2) is needed so that "$`P`$ holds on $`D_1`$" and "$`Q`$ holds on $`D_2`$" imply "$`P`$ and $`Q`$ hold on some $`D_3`$" — uniqueness of the limit and the arithmetic of limits rest on this. Non-emptiness of the elements is needed for the limit to be unique (on the empty set anything is true).

<a id="p-4-4"></a>
## Problem 4.4

> **At the seminar.** [Remark 14.2](notes-4-examples-tests.md#rem-14-2) (11 Nov).

**Statement.** Derive d'Alembert's test (problem 3.7) from Raabe's test (problem 3.9).

**Proof.** Let $`a_n>0`$ for $`n>N_0`$.

1) Let $`\frac{a_n}{a_{n+1}}\ge1+\beta`$ for $`n>N_1`$, $`\beta>0`$. Take $`\gamma=1`$ and a natural number $`N_1'\ge\max\bigl(N_1,\frac2\beta\bigr)`$. For $`n>N_1'`$ we have $`\frac2n<\beta`$, so
```math
\frac{a_n}{a_{n+1}}\ge1+\beta\ge1+\frac2n=1+\frac{1+\gamma}n .
```
Condition 1) of Raabe's test holds (and $`N_1'>N_0`$) — the series converges.

2) Let $`\frac{a_n}{a_{n+1}}\le1`$ for $`n>N_2`$. Then all the more
```math
\frac{a_n}{a_{n+1}}\le1<1+\frac1n
```
for $`n>N_2`$. Condition 2) of Raabe's test holds — the series diverges. $`\blacksquare`$

**Why it works.** Raabe's scale is finer: d'Alembert requires the ratio to be separated from one by a constant gap $`\beta`$, while Raabe is content with a gap of order $`\frac{1+\gamma}n`$, which itself tends to zero. A constant gap sooner or later exceeds any $`\frac cn`$, so everything d'Alembert sees, Raabe sees too. The converse is false: for $`a_n=\frac1{n^2}`$ the ratio is $`(1+\frac1n)^2\to1`$, d'Alembert is silent, Raabe gives convergence. Both tests are special cases of Kummer's with $`x_n=1`$ and $`x_n=n`$: the slower $`\sum\frac1{x_n}`$ diverges, the stronger the test.

<a id="p-4-5"></a>
## Problem 4.5$`^{**}`$

**Statement.** Give an example of a convergent series for which the set $`\bigl\{k:\ 1<\frac{a_k}{a_{k+1}}\le1+\frac1k\bigr\}`$ is countable.

**Solution.** Define the terms in pairs: for $`m\in\mathbb N`$
```math
a_{2m}=\frac1{m!},\qquad a_{2m-1}=\Bigl(1+\frac1{2m-1}\Bigr)\frac1{m!}.
```
All terms are positive.

*Ratios.* For odd $`k=2m-1`$:
```math
\frac{a_k}{a_{k+1}}=\frac{a_{2m-1}}{a_{2m}}=1+\frac1{2m-1}=1+\frac1k,
```
i.e. $`1<\frac{a_k}{a_{k+1}}\le1+\frac1k`$. So the set contains all odd numbers and is therefore infinite; as an infinite subset of $`\mathbb N`$ it is countable.

*Convergence.* $`a_{2m-1}\le\frac2{m!}`$ and $`a_{2m}=\frac1{m!}`$, so every partial sum is at most
```math
\sum_{m=1}^{\infty}\frac3{m!}<\infty
```
(the series $`\sum\frac1{m!}`$ converges by problem 3.5). The series is positive with bounded partial sums — it converges by (F2). $`\blacksquare`$

(For even $`k=2m`$ the ratio is $`\frac{a_{2m}}{a_{2m+1}}=\frac{(m+1)(2m+1)}{2m+2}=m+\frac12>1+\frac1k`$; such $`k`$ are not in the set, which is exactly the set of odd numbers.)

**Why it works.** The idea is the same as in 3.8: the series is assembled from pairs. Inside a pair we prescribe the ratio ourselves — exactly $`1+\frac1k`$, "as for the harmonic series". Between pairs the series drops very fast (factorial), which secures convergence. Raabe's test sees only one step and on odd steps mistakes the series for the harmonic one.

The extra requirement $`1<\frac{a_k}{a_{k+1}}`$ excludes cheap examples like 3.8, where the terms grow on the "bad" steps. Here the terms honestly decrease on the bad steps, but no faster than harmonic ones — and still divergence does not follow from the infinitude of such steps. Upshot: in part 2) of Raabe's test the condition must hold for all indices from some point on.

<a id="p-4-6"></a>
## Problem 4.6 (limit forms of the tests)

> **At the seminar.** [Proposition 14.3](notes-4-examples-tests.md#prop-14-3) (11 Nov) and the summary [how the tests compare](notes-4-examples-tests.md#tests-compared).

**Statement.** $`a_k>0`$ for $`k\ge N_0`$; $`C_k=\sqrt[k]{a_k}`$, $`D_k=\dfrac{a_k}{a_{k+1}}`$, $`R_k=k\Bigl(\dfrac{a_k}{a_{k+1}}-1\Bigr)`$. Prove six statements.

The common device: if $`u_k\to L`$ and $`L<c`$, then $`u_k<c`$ for all sufficiently large $`k`$ (the definition of a limit with $`\varepsilon=c-L`$); similarly for $`L>c`$. A limit yields an inequality "from some index on" — exactly what the tests in pre-limit form require.

**1) $`C_k\to L<1`$ ⟹ converges.** Take $`q=\frac{1+L}2`$, so $`L<q<1`$. There is $`K\ge N_0`$ such that for $`k>K`$ we have $`\sqrt[k]{a_k}<q`$, i.e. $`0<a_k<q^k`$. The geometric series $`\sum q^k`$ converges; by comparison $`\sum a_k`$ converges.

**2) $`C_k\to L>1`$ ⟹ diverges.** For $`k>K`$ we have $`\sqrt[k]{a_k}>1`$, i.e. $`a_k>1`$. The general term does not tend to zero — divergence by (F1).

**3) $`D_k\to L<1`$ ⟹ diverges.** For $`k>K`$ we have $`\frac{a_k}{a_{k+1}}<1`$; by problem 3.7, 2) the series diverges.

**4) $`D_k\to L>1`$ ⟹ converges.** Take $`\beta=\frac{L-1}2>0`$. For $`k>K`$ we have $`\frac{a_k}{a_{k+1}}>1+\beta`$; by problem 3.7, 1) the series converges.

**5) $`R_k\to L<1`$ ⟹ diverges.** For $`k>K`$ we have $`R_k<1`$, i.e. $`\frac{a_k}{a_{k+1}}<1+\frac1k`$; by problem 3.9, 2) the series diverges.

**6) $`R_k\to L>1`$ ⟹ converges.** Take $`\gamma=\frac{L-1}2>0`$. For $`k>K`$ we have $`R_k>1+\gamma`$, i.e. $`\frac{a_k}{a_{k+1}}>1+\frac{1+\gamma}k`$; by problem 3.9, 1) the series converges. $`\blacksquare`$

**Why it works.** The limit form is more convenient in computations (one limit to find) but weaker than the pre-limit one: it requires the limit to exist. In all three tests the case $`L=1`$ stays undecided, and this is not a defect of the proof: for $`L=1`$ both convergence and divergence occur. For Cauchy and d'Alembert: $`\sum\frac1k`$ and $`\sum\frac1{k^2}`$ both give the limit $`1`$. For Raabe: $`\sum\frac1{k\ln k}`$ and $`\sum\frac1{k\ln^2k}`$ both give $`R_k\to1`$.

Beware of the direction: here $`D_k=\frac{a_k}{a_{k+1}}`$ is the ratio of the previous term to the next one, the reciprocal of the usual $`\frac{a_{k+1}}{a_k}`$. So $`D_k\to L<1`$ means the terms **grow** and the series diverges, and $`L>1`$ means convergence; for $`C_k`$ it is the other way round. The restriction $`L\ge0`$ in parts 3) and 5) of the statement is immaterial: the proof only uses $`L<1`$.

<a id="p-4-7"></a>
## Problem 4.7

> **At the seminar.** Part 3) is [Example 14.1](notes-4-examples-tests.md#ex-14-1) (11 Nov).

**1) $`a_k=\dfrac{\prod_{m=1}^k(2025+m)}{\prod_{m=1}^k(2m-1)}`$ — converges.**

All $`a_k>0`$, and
```math
\frac{a_k}{a_{k+1}}=\frac{2(k+1)-1}{2025+(k+1)}=\frac{2k+1}{k+2026}\ \longrightarrow\ 2>1 .
```
By 4.6, 4) the series converges. Without a limit: $`\frac{2k+1}{k+2026}\ge\frac32`$ is equivalent to $`k\ge6076`$, so condition 3.7, 1) holds with $`\beta=\frac12`$ for $`n>6075`$.

*Why it works.* Numerator and denominator are products of $`k`$ factors; the factors of the numerator grow like $`m`$, those of the denominator like $`2m`$. From $`k=2026`$ on, each new step multiplies the term by a number less than one and tending to $`\frac12`$: in its tail the series behaves like a geometric progression. Before that, for $`k<2025`$, the terms **grow** (the ratio $`\frac{a_{k+1}}{a_k}=\frac{k+2026}{2k+1}>1`$) and reach enormous values, but the beginning of a series does not affect convergence (F3).

**2) $`b_k=\frac1k`$ if $`k`$ is a perfect square and $`b_k=\frac1{k^2}`$ otherwise — converges.**

All $`b_k>0`$. Estimate a partial sum by splitting the terms into two kinds. The squares $`k=m^2\le n`$ contribute $`\sum\frac1{m^2}`$, the rest at most $`\sum\frac1{k^2}`$:
```math
S_n\le\sum_{m:\ m^2\le n}\frac1{m^2}+\sum_{k=1}^n\frac1{k^2}\le2\sum_{k=1}^\infty\frac1{k^2}\le4 .
```
Here $`\sum_{k\ge1}\frac1{k^2}\le1+\sum_{k\ge2}\frac1{k(k-1)}=2`$. The partial sums of a positive series are bounded — it converges by (F2).

*Why it works.* The "large" terms $`\frac1k`$ are rare: there are only about $`\sqrt n`$ squares up to $`n`$, and the sum of the large terms is again $`\sum\frac1{m^2}`$. Neither d'Alembert nor Raabe works here: at the step $`k=m^2-1\to m^2`$ the term increases ($`\frac{b_k}{b_{k+1}}=\frac{m^2}{(m^2-1)^2}<1`$ for $`m\ge2`$) infinitely often, and at the step $`m^2\to m^2+1`$ it drops sharply. Ratio tests need regular behaviour of consecutive terms; the bounded-partial-sums criterion depends neither on order nor on regularity.

**3)$`^*`$ $`c_k=\dfrac{k^{k+\frac1k}}{\bigl(k+\frac1k\bigr)^k}`$ — diverges.**

Transform:
```math
c_k=k^{1/k}\cdot\frac{k^k}{\bigl(k+\frac1k\bigr)^k}=\frac{k^{1/k}}{\bigl(1+\frac1{k^2}\bigr)^k}.
```
The numerator $`k^{1/k}\ge1`$. The denominator: from $`1+t\le e^t`$ we get $`\bigl(1+\frac1{k^2}\bigr)^k\le e^{1/k}\le e`$. So $`c_k\ge\frac1e`$ for all $`k`$: the general term does not tend to zero, and the series diverges by (F1).

*Why it works.* Numerator and denominator look huge, but they are almost equal: $`k+\frac1k`$ differs from $`k`$ by the relative amount $`\frac1{k^2}`$, and raising to the power $`k`$ turns it into $`\frac1k\to0`$ (a power of order $`k^2`$ would be needed for a finite effect, as in $`(1+\frac1n)^n\to e`$). In fact $`c_k\to1`$.

**Answer.** $`\sum a_k`$ and $`\sum b_k`$ converge, $`\sum c_k`$ diverges.

<a id="p-4-8"></a>
## Problem 4.8

> **At the seminar.** Both series were worked out on 30 Oct: $`a_k`$ in [Example 13.2](notes-4-examples-tests.md#ex-13-2), $`b_k`$ in [Example 13.1](notes-4-examples-tests.md#ex-13-1).

**The series $`a_k=\dfrac{\sqrt{k+1}-\sqrt{k-1}}{k^\alpha}`$: converges for $`\alpha>\frac12`$, diverges for $`\alpha\le\frac12`$.**

Multiply and divide by the conjugate:
```math
\sqrt{k+1}-\sqrt{k-1}=\frac{2}{\sqrt{k+1}+\sqrt{k-1}},\qquad a_k=\frac{C_k}{k^{\alpha+\frac12}},\quad C_k=\frac{2\sqrt k}{\sqrt{k+1}+\sqrt{k-1}} .
```
Estimate $`C_k`$: the denominator is greater than $`\sqrt k`$ and at most $`2\sqrt{k+1}\le2\sqrt{2k}`$, so
```math
\frac1{\sqrt2}\le C_k<2\qquad\text{for all }k\in\mathbb N .
```
By problem 3.11 (with exponent $`\alpha+\frac12`$) the series converges if and only if $`\alpha+\frac12>1`$.

*Why it works.* A difference of roots is an example of "loss of order": each root is of order $`\sqrt k`$, but their difference is of order $`\frac1{\sqrt k}`$ (it is the increment of $`\sqrt x`$ over an interval of length $`2`$, about $`2\cdot\frac1{2\sqrt k}`$). So the term is of order $`k^{-\alpha-1/2}`$, not $`k^{\frac12-\alpha}`$. Multiplying by the conjugate makes this order explicit.

**The series $`b_k=\dfrac{\beta^kk!}{k^k}`$: converges for $`0<\beta<e`$, diverges for $`\beta\ge e`$.**

All $`b_k>0`$ and
```math
\frac{b_k}{b_{k+1}}=\frac{\beta^kk!}{k^k}\cdot\frac{(k+1)^{k+1}}{\beta^{k+1}(k+1)!}=\frac1\beta\Bigl(1+\frac1k\Bigr)^k\ \longrightarrow\ \frac e\beta .
```

- $`\beta<e`$: the limit exceeds $`1`$, the series converges by 4.6, 4).
- $`\beta>e`$: the limit is below $`1`$, the series diverges by 4.6, 3).
- $`\beta=e`$: the limit equals $`1`$, the limit form does not work. But the sequence $`\bigl(1+\frac1k\bigr)^k`$ increases strictly to $`e`$, so $`\bigl(1+\frac1k\bigr)^k<e`$ and
```math
\frac{b_k}{b_{k+1}}=\frac1e\Bigl(1+\frac1k\Bigr)^k<1\qquad\text{for all }k .
```
By the pre-limit form 3.7, 2) the series diverges: the terms increase, $`b_k\ge b_1=e`$, and do not tend to zero.

*Why it works.* By Stirling's formula $`k!\approx\sqrt{2\pi k}\,\bigl(\frac ke\bigr)^k`$, so $`b_k\approx\sqrt{2\pi k}\,\bigl(\frac\beta e\bigr)^k`$: essentially a geometric progression with ratio $`\frac\beta e`$, hence the threshold $`\beta=e`$. At the threshold itself the factor $`\sqrt{2\pi k}\to\infty`$ remains. The case $`\beta=e`$ shows what the pre-limit form is for: the limit equals one, but the inequality $`\frac{b_k}{b_{k+1}}\le1`$ holds exactly, and Stirling's formula was not needed.

**Answer.** $`\sum a_k`$ converges for $`\alpha>\frac12`$ (for any $`\beta`$), $`\sum b_k`$ converges for $`\beta<e`$ (for any $`\alpha`$).

<a id="p-4-9"></a>
## Problem 4.9

> **At the seminar.** A series of the same kind as $`b_k`$ is the example after [Corollary 11.1](notes-3-kummer-dalembert-raabe.md#cor-11-1) (21 Oct).

In all four series the terms are positive and $`D_k=\frac{a_k}{a_{k+1}}\to1`$, with $`D_k>1`$ for all $`k`$. Therefore **d'Alembert's test is not applicable**: the divergence condition $`D_k\le1`$ holds for no $`k`$, and the convergence condition $`D_k\ge1+\beta`$ with a constant $`\beta>0`$ fails for large $`k`$ (otherwise the limit would be at least $`1+\beta`$). Raabe's test works.

**$`a_k=\dfrac{1}{k\ln((k+1)!)}`$ — converges.** Since $`\ln((k+2)!)=\ln((k+1)!)+\ln(k+2)`$,
```math
\frac{a_k}{a_{k+1}}=\frac{(k+1)\ln((k+2)!)}{k\ln((k+1)!)}=\Bigl(1+\frac1k\Bigr)\Bigl(1+\frac{\ln(k+2)}{\ln((k+1)!)}\Bigr).
```
From $`(k+1)!\le(k+1)^{k+1}`$ it follows that $`\ln((k+1)!)\le(k+1)\ln(k+1)<(k+1)\ln(k+2)`$, i.e. the second bracket exceeds $`1+\frac1{k+1}`$:
```math
\frac{a_k}{a_{k+1}}>\frac{k+1}k\cdot\frac{k+2}{k+1}=1+\frac2k=1+\frac{1+\gamma}k,\qquad\gamma=1 .
```
By 3.9, 1) the series converges. (That $`D_k\to1`$: $`(k+1)!\ge2^k`$, so $`\frac{\ln(k+2)}{\ln((k+1)!)}\le\frac{\ln(k+2)}{k\ln2}\to0`$.)

**$`b_k=\dfrac{(2k)!}{(k!)^2\,4^k}`$ — diverges.**
```math
\frac{b_k}{b_{k+1}}=\frac{(2k)!}{(k!)^24^k}\cdot\frac{((k+1)!)^24^{k+1}}{(2k+2)!}=\frac{4(k+1)^2}{(2k+1)(2k+2)}=\frac{2k+2}{2k+1}=1+\frac1{2k+1}\le1+\frac1k .
```
By 3.9, 2) the series diverges. ($`R_k=\frac{k}{2k+1}\to\frac12<1`$.)

**$`c_k=\dfrac{4^k}{(k+1)\,C_{2k}^k}`$ — diverges.** Note that $`c_k=\dfrac{1}{(k+1)\,b_k}`$, so
```math
\frac{c_k}{c_{k+1}}=\frac{k+2}{k+1}\cdot\frac{b_{k+1}}{b_k}=\frac{(k+2)(2k+1)}{(k+1)(2k+2)}=1+\frac{k}{2(k+1)^2}\le1+\frac1{2k}\le1+\frac1k .
```
By 3.9, 2) the series diverges. ($`R_k=\frac{k^2}{2(k+1)^2}\to\frac12<1`$.)

**$`d_k=\dfrac{(2k+16)!!}{(2k+19)!!}`$ — converges.** By definition $`(2k+16)!!=\prod_{m=1}^{k+8}2m`$ and $`(2k+19)!!=\prod_{m=1}^{k+10}(2m-1)`$. Passing from $`k`$ to $`k+1`$ multiplies the numerator by $`2k+18`$ and the denominator by $`2k+21`$:
```math
\frac{d_k}{d_{k+1}}=\frac{2k+21}{2k+18}=1+\frac{3}{2k+18},\qquad R_k=\frac{3k}{2k+18}\to\frac32>1 .
```
By 4.6, 6) the series converges. Without a limit: $`\frac3{2k+18}\ge\frac{5/4}{k}`$ is equivalent to $`k\ge45`$, so condition 3.9, 1) holds with $`\gamma=\frac14`$ for $`n>44`$.

**Answer.** $`\sum a_k`$ and $`\sum d_k`$ converge, $`\sum b_k`$ and $`\sum c_k`$ diverge.

**Why it works.** Raabe's test reads off the exponent in the asymptotics $`a_k\sim\frac{\mathrm{const}}{k^p}`$: if $`\frac{a_k}{a_{k+1}}=1+\frac pk+\dots`$, then $`R_k\to p`$. Here:

- $`b_k=C_{2k}^k/4^k`$ is the probability of returning to zero after $`2k`$ steps of a symmetric random walk, $`b_k\sim\frac1{\sqrt{\pi k}}`$, $`p=\frac12`$ — divergence;
- $`c_k=\frac1{(k+1)b_k}\sim\frac{\sqrt\pi}{\sqrt k}`$, again $`p=\frac12`$ — divergence;
- $`d_k`$: the ratio of double factorials "eats up" one and a half factors, $`d_k\sim\frac{\mathrm{const}}{k^{3/2}}`$, $`p=\frac32`$ — convergence;
- $`a_k\sim\frac1{k^2\ln k}`$, $`R_k\to2`$ — convergence (this is seen more simply too: $`\ln((k+1)!)\ge k\ln2`$, so $`a_k\le\frac{1}{k^2\ln2}`$).

D'Alembert's test only distinguishes exponential behaviour ($`a_k\approx q^k`$) and always gives $`D_k\to1`$ on power-law decay.

<a id="p-4-10"></a>
## Problem 4.10 (Cauchy's integral test)

**Statement.** $`f\colon[1;+\infty)\to\mathbb R`$; on $`[N_0;+\infty)`$ the function $`f`$ is non-increasing and non-negative; $`f`$ is integrable on every $`[N_0;x]`$. Prove: the series $`\sum_{k=1}^\infty f(k)`$ converges $`\iff`$ the finite limit $`\lim_{x\to+\infty}I_f(x)`$ exists, where $`I_f(x)=\int_{N_0}^xf(y)\,dy`$.

**Proof.** *Step 1: the basic inequality.* Let $`k\ge N_0`$ be an integer. For $`y\in[k;k+1]`$ monotonicity gives $`f(k+1)\le f(y)\le f(k)`$. Integrating over an interval of length $`1`$:
```math
f(k+1)\le\int_k^{k+1}f(y)\,dy\le f(k).\tag{2}
```
Adding (2) over $`k=N_0,\dots,n-1`$ (additivity of the integral) we get, for integers $`n>N_0`$,
```math
\sum_{k=N_0+1}^{n}f(k)\ \le\ I_f(n)\ \le\ \sum_{k=N_0}^{n-1}f(k).\tag{3}
```

*Step 2: $`I_f`$ is non-decreasing.* For $`N_0\le x_1<x_2`$ we have $`I_f(x_2)-I_f(x_1)=\int_{x_1}^{x_2}f\ge0`$, since $`f\ge0`$.

*a) ⟹ b).* Let the series converge. Then its tail converges too (F3); let $`A=\sum_{k=N_0}^\infty f(k)`$. The terms of the tail are non-negative, so its partial sums do not exceed $`A`$. For any $`x\ge N_0`$ take an integer $`n>x`$; by step 2 and the right-hand side of (3)
```math
I_f(x)\le I_f(n)\le\sum_{k=N_0}^{n-1}f(k)\le A .
```
The function $`I_f`$ is non-decreasing and bounded above, so the finite limit $`\lim_{x\to+\infty}I_f(x)=\sup I_f`$ exists.

*b) ⟹ a).* Let $`I=\lim_{x\to+\infty}I_f(x)`$ be finite. Since $`I_f`$ is non-decreasing, $`I_f(n)\le I`$ for all $`n`$. By the left-hand side of (3)
```math
\sum_{k=N_0+1}^nf(k)\le I_f(n)\le I .
```
The partial sums of the non-negative series $`\sum_{k>N_0}f(k)`$ are bounded, it converges by (F2); by (F3) $`\sum_{k\ge1}f(k)`$ converges. $`\blacksquare`$

**Why it works.** Inequality (2) is a picture: under the graph of a decreasing function on $`[k;k+1]`$ there fits a rectangle of height $`f(k+1)`$, and the graph itself fits into a rectangle of height $`f(k)`$. The sum of the series is the area of a staircase figure, and it differs from the area under the graph by at most one step $`f(N_0)`$. So the area and the sum are finite or infinite together.

Where each hypothesis is used: monotonicity — in (2) (without it the values at integer points say nothing about the function in between: $`f(x)=\sin^2(\pi x)`$ gives a zero series and a divergent integral); non-negativity — in the monotonicity of $`I_f`$ and in (F2); integrability — for $`I_f`$ to be defined. The hypotheses are needed only from some $`N_0`$ on, because convergence is a property of the tail. The test turns a question about a series into a question about an integral, which can often be computed explicitly: this is how one gets $`\sum\frac1{k^\alpha}`$ (converges for $`\alpha>1`$) and $`\sum\frac{1}{k\ln^\alpha k}`$ (converges for $`\alpha>1`$).

<a id="p-4-11"></a>
## Problem 4.11 (Leibniz's test)

**Statement.** For all $`k`$: $`a_ka_{k+1}<0`$ and $`|a_{k+1}|\le|a_k|`$; $`a_k\to0`$. Prove that $`\sum a_k`$ converges. $`^*`$ Is this true under the condition $`a_ka_{k+1}\le0`$?

**Proof.** From $`a_ka_{k+1}<0`$ it follows that all $`a_k\ne0`$ and consecutive terms have opposite signs. We may assume $`a_1>0`$ (otherwise consider $`\sum(-a_k)`$: it satisfies the same hypotheses and converges together with the original series). Then by induction $`a_{2j-1}>0`$, $`a_{2j}<0`$ for all $`j`$, and
```math
a_{2j-1}+a_{2j}=|a_{2j-1}|-|a_{2j}|\ge0,\qquad a_{2j}+a_{2j+1}=-|a_{2j}|+|a_{2j+1}|\le0 .
```

*The even partial sums are non-decreasing and non-negative:*
```math
S_{2m}=\sum_{j=1}^m(a_{2j-1}+a_{2j})\ge0,\qquad S_{2m+2}-S_{2m}=a_{2m+1}+a_{2m+2}\ge0 .
```

*The even partial sums are bounded above:* regroup differently —
```math
S_{2m}=a_1+\sum_{j=1}^{m-1}(a_{2j}+a_{2j+1})+a_{2m}\le a_1,
```
since every bracket is non-positive and $`a_{2m}<0`$.

The monotone bounded sequence $`(S_{2m})`$ converges: $`S_{2m}\to S\in[0;a_1]`$.

*The odd partial sums:* $`S_{2m+1}=S_{2m}+a_{2m+1}\to S+0=S`$, since $`a_k\to0`$.

The two subsequences $`(S_{2m})`$ and $`(S_{2m+1})`$, which together exhaust all indices, converge to the same number $`S`$; hence $`S_n\to S`$. $`\blacksquare`$

**Answer to the starred question: yes, the statement remains true.** Let $`a_ka_{k+1}\le0`$ for all $`k`$.

- If all $`a_k\ne0`$, then $`a_ka_{k+1}<0`$, and this is the case already proved.
- If $`a_K=0`$ for some $`K`$, then $`|a_{k+1}|\le|a_k|`$ gives by induction $`a_k=0`$ for all $`k\ge K`$. The series has finitely many non-zero terms, $`S_n=S_K`$ for $`n\ge K`$, and it converges.

**Why it works.** The partial sums of an alternating series with decreasing absolute values "jump" around the limit: a step up, a smaller step down, an even smaller step up. The even sums form an increasing sequence, the odd ones a decreasing one, and all even sums lie below all odd ones: we get nested intervals $`[S_{2m};S_{2m+1}]`$. Their lengths $`a_{2m+1}`$ tend to zero — hence the common limit. As a by-product one gets the remainder estimate $`|S-S_n|\le|a_{n+1}|`$.

The role of the hypotheses: monotonicity of the absolute values gives the nesting, $`a_k\to0`$ gives the shrinking. Without monotonicity the statement is false: the series $`1-\frac12+\frac12-\frac14+\frac13-\frac18+\dots`$ (positive terms $`\frac1m`$, negative $`-\frac1{2^m}`$) alternates, its terms tend to zero, but it diverges, because the positive part is the harmonic series while the negative part converges.

<a id="p-4-12"></a>
## Problem 4.12

**Statement.** $`\alpha>0`$. Using problem 4.11, prove the convergence of six series.

Auxiliary remark (Z): **inserting zeros does not affect convergence.** If the series $`\sum c_j`$ converges to $`T`$ and the series $`\sum a_k`$ is obtained from it by inserting zero terms (keeping the order), then every partial sum $`S_n`$ of $`\sum a_k`$ equals a partial sum $`T_{j(n)}`$ of $`\sum c_j`$, where $`j(n)`$ is the number of non-zero places up to $`n`$; $`j(n)\to\infty`$, so $`S_n\to T`$.

**1) $`\sum\dfrac{(-1)^k}{k^\alpha}`$.** $`a_ka_{k+1}=-\frac{1}{k^\alpha(k+1)^\alpha}<0`$; $`|a_{k+1}|=\frac1{(k+1)^\alpha}\le\frac1{k^\alpha}=|a_k|`$, since $`\alpha>0`$; $`|a_k|=k^{-\alpha}\to0`$. By 4.11 the series converges. $`\blacksquare`$

**2) $`\sum\dfrac{\cos\frac{k\pi}2}{\sqrt k}`$.** For odd $`k`$, $`\cos\frac{k\pi}2=0`$; for $`k=2j`$, $`\cos(j\pi)=(-1)^j`$. The series looks like
```math
0-\frac1{\sqrt2}+0+\frac1{\sqrt4}+0-\frac1{\sqrt6}+\dots
```
4.11 is not directly applicable: $`a_ka_{k+1}=0`$, and the absolute values are not monotone ($`|a_1|=0<|a_2|`$). But the series is obtained by inserting zeros into $`\sum_{j\ge1}c_j`$, $`c_j=\dfrac{(-1)^j}{\sqrt{2j}}`$, for which $`c_jc_{j+1}<0`$, $`|c_j|`$ decreases and tends to zero. By 4.11 the series $`\sum c_j`$ converges, and by (Z) so does the original one ($`S_{2m}=S_{2m+1}=T_m`$). $`\blacksquare`$

**3) $`\sum\dfrac{\sin\frac{k\pi}2}{\ln(k+2026)}`$.** For even $`k`$, $`\sin\frac{k\pi}2=0`$; for $`k=2j-1`$, $`\sin\bigl(j\pi-\frac\pi2\bigr)=(-1)^{j-1}`$. The non-zero terms are $`c_j=\dfrac{(-1)^{j-1}}{\ln(2j+2025)}`$. They alternate, $`|c_j|`$ decreases (the logarithm increases) and tends to zero. By 4.11 and (Z) the series converges ($`S_{2m-1}=S_{2m}=T_m`$). $`\blacksquare`$

**4)$`^*`$ $`\sum\dfrac{(-1)^kk^{10}}{3^k}`$.** The signs alternate. The ratio of absolute values is
```math
\frac{|a_{k+1}|}{|a_k|}=\frac13\Bigl(1+\frac1k\Bigr)^{10}.
```
It decreases in $`k`$; for $`k=8`$ it equals $`\frac13\bigl(\frac98\bigr)^{10}\approx1.08>1`$, for $`k=9`$ it is $`q=\frac13\bigl(\frac{10}9\bigr)^{10}\approx0.956<1`$. So the absolute values are non-increasing only from $`k=9`$ on, and the first nine terms grow in absolute value. Apply 4.11 to the tail $`c_j=a_{j+8}`$, $`j\ge1`$: $`c_jc_{j+1}<0`$; $`|c_{j+1}|\le q|c_j|\le|c_j|`$; $`|c_j|\le|c_1|q^{j-1}\to0`$. By 4.11 $`\sum c_j=\sum_{k\ge9}a_k`$ converges, and by (F3) so does the original series. $`\blacksquare`$

**5)$`^{**}`$ $`\sum\ln\Bigl(1+\dfrac{(-1)^{k+1}}{k}\Bigr)`$.** Write out the terms:

- $`k`$ odd: $`a_k=\ln\bigl(1+\frac1k\bigr)>0`$;
- $`k`$ even: $`a_k=\ln\bigl(1-\frac1k\bigr)=\ln\frac{k-1}{k}=-\ln\bigl(1+\frac1{k-1}\bigr)<0`$.

The signs alternate. Absolute values: $`|a_k|=\ln\bigl(1+\frac1k\bigr)`$ for odd $`k`$ and $`|a_k|=\ln\bigl(1+\frac1{k-1}\bigr)`$ for even $`k`$. Check monotonicity:

- $`k`$ odd: $`|a_{k+1}|=\ln\bigl(1+\frac1k\bigr)=|a_k|`$;
- $`k`$ even: $`|a_{k+1}|=\ln\bigl(1+\frac1{k+1}\bigr)<\ln\bigl(1+\frac1{k-1}\bigr)=|a_k|`$.

Finally, $`|a_k|\le\ln\bigl(1+\frac1{k-1}\bigr)\to0`$. By 4.11 the series converges. $`\blacksquare`$

Moreover, $`a_{2j-1}+a_{2j}=\ln\frac{2j}{2j-1}+\ln\frac{2j-1}{2j}=0`$, so $`S_{2m}=0`$ and the sum of the series is $`0`$.

**6)$`^{**}`$ $`\sum\dfrac{\sin\bigl(\frac\pi4+\frac{k\pi}2\bigr)}{k}`$.** The numerator: for $`k=2j`$, $`\sin\bigl(\frac\pi4+j\pi\bigr)=(-1)^j\frac{\sqrt2}2`$; for $`k=2j+1`$, $`\sin\bigl(\frac\pi4+\frac\pi2+j\pi\bigr)=(-1)^j\cos\frac\pi4=(-1)^j\frac{\sqrt2}2`$. The signs of the terms:
```math
+\ -\ -\ +\ +\ -\ -\ +\ +\ \dots
```
They change not at every step but every other step: $`a_2a_3>0`$, and 4.11 is not directly applicable. Group the terms into pairs of the same sign: for $`j\ge1`$
```math
c_j=a_{2j}+a_{2j+1}=(-1)^j\frac{\sqrt2}2\Bigl(\frac1{2j}+\frac1{2j+1}\Bigr).
```
For the series $`\sum c_j`$: the signs alternate, $`|c_j|`$ decreases, $`|c_j|\to0`$. By 4.11 it converges, say to $`T`$. Return to the original series:
```math
S_{2m+1}=a_1+\sum_{j=1}^mc_j\to a_1+T,\qquad S_{2m}=S_{2m+1}-a_{2m+1}\to a_1+T,
```
since $`a_k\to0`$. Both subsequences of partial sums converge to the same limit, so the series converges. $`\blacksquare`$

**Why it works.** In all six examples the convergence is conditional or "almost" conditional and rests on cancellation of neighbouring terms, not on smallness of absolute values (in 1) for $`\alpha\le1`$, and in 2), 3), 6), the series of absolute values diverges). Leibniz's test requires three things, and each example tests one of them:

- 2), 3): zeros in the series break strict alternation formally but not in substance — they can be thrown out;
- 4): monotonicity may start not from the first term — the tail suffices (incidentally, this series also converges absolutely, by d'Alembert);
- 5): monotonicity of absolute values is non-strict, the terms come in pairs of equal absolute value — that is why the hypothesis of 4.11 has $`\le`$ and not $`<`$;
- 6): alternation with period $`4`$ reduces to the usual one by grouping. The terms of a convergent series can always be grouped, but the reverse passage (from convergence of the grouped series to convergence of the original one) is legitimate only because $`a_k\to0`$ and every group has a bounded number of terms.

In 6) one can do without grouping: $`\sin\bigl(\frac\pi4+\frac{k\pi}2\bigr)=\frac{\sqrt2}2\bigl(\sin\frac{k\pi}2+\cos\frac{k\pi}2\bigr)`$, so the series is the sum of two convergent series of types 2) and 3) with denominator $`k`$.
