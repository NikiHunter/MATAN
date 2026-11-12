---
title: "Seminar NM-204. Test 1 — practice variants"
lang: en
---
# Test 1: practice variants with solutions

[Русский](../../ru/seminar-sem3/test1-variants.md) · **English** · [Español](../../es/seminar-sem3/test1-variants.md)

[All assignments](index.md) · [← How to prepare](test1-guide.md)

> **What this is.** Three practice variants in the expected format of the test: four tasks, items 1.1, 1.2, 2.1, 2.2, 3, 4. The problems are modelled on homework 1–4; there are no real papers, this is a forecast. The seminar's notation is kept: the tests use the ratio $`\frac{a_k}{a_{k+1}}`$. Aim for 80–90 minutes per variant. Solve in writing and only then open the solutions.

## Variant A

**1.1.** Expand $`f(x,y)=x^3+2x^2y-y^3+4x`$ by Taylor's formula at the point $`(1;-2)`$.

**1.2.** Find the explicit Taylor expansion of $`f(x,y)=e^{x^2-y}`$ up to degree two with the Lagrange remainder at the point $`(1;1)`$.

**2.1.** Find all points of constrained local extremum of $`f(x,y)=x^3-3xy+y^2`$ on the set $`M=\{(x,y):\ y=2x\}`$.

**2.2.** Find all points of constrained extremum of $`f(x,y,z)=x-2y+2z`$ on the set $`M=\{x^2+y^2+z^2=9\}`$ and the extremal values.

**3.** Let $`a_n>0`$, $`b_n>0`$ and $`\dfrac{a_{n+1}}{a_n}\le\dfrac{b_{n+1}}{b_n}`$ for all $`n>N_0`$. Prove that convergence of $`\sum b_k`$ implies convergence of $`\sum a_k`$. Using this statement, prove that $`\sum\limits_{k=1}^\infty\dfrac1{k!}`$ converges.

**4.** Test the series for convergence:
```math
\text{a)}\ \sum_{k=1}^\infty\frac{(k!)^2}{(2k)!};\qquad\text{b)}\ \sum_{k=1}^\infty\frac{(2k-1)!!}{(2k+2)!!};\qquad\text{c)}\ \sum_{k=1}^\infty\frac{(-1)^k}{\ln(k+1)} .
```

<details>
<summary>Solutions to variant A</summary>

**1.1.** Let $`h_1=x-1`$, $`h_2=y+2`$. $`f(1,-2)=1-4+8+4=9`$. $`f_x=3x^2+4xy+4=-1`$, $`f_y=2x^2-3y^2=-10`$. $`f_{xx}=6x+4y=-2`$, $`f_{xy}=4x=4`$, $`f_{yy}=-6y=12`$. $`f_{xxx}=6`$, $`f_{xxy}=4`$, $`f_{xyy}=0`$, $`f_{yyy}=-6`$; the fourth-order derivatives vanish, so the sum is finite and the equality is exact:

```math
f=9-h_1-10h_2-h_1^2+4h_1h_2+6h_2^2+h_1^3+2h_1^2h_2-h_2^3 .
```

Check: $`h=(1,0)`$, $`f(2,-2)=8-16+8+8=8`$; the formula gives $`9-1-1+1=8`$.

**1.2.** Let $`h_1=x-1`$, $`h_2=y-1`$. Derivatives: $`f_x=2xf`$, $`f_y=-f`$, $`f_{xx}=(4x^2+2)f`$, $`f_{xy}=-2xf`$, $`f_{yy}=f`$. At $`(1;1)`$: $`f=1`$, $`f_x=2`$, $`f_y=-1`$, $`f_{xx}=6`$, $`f_{xy}=-2`$, $`f_{yy}=1`$. Third derivatives: $`f_{xxx}=(8x^3+12x)f`$, $`f_{xxy}=-(4x^2+2)f`$, $`f_{xyy}=2xf`$, $`f_{yyy}=-f`$. There is $`\theta\in(0,1)`$ such that

```math
e^{x^2-y}=1+2h_1-h_2+3h_1^2-2h_1h_2+\frac{h_2^2}2+R_2,
```

```math
R_2=\frac{e^{\xi^2-\eta}}{6}\Bigl[(8\xi^3+12\xi)h_1^3-3(4\xi^2+2)h_1^2h_2+6\xi h_1h_2^2-h_2^3\Bigr],\qquad\xi=1+\theta h_1,\ \eta=1+\theta h_2 .
```

Check of the polynomial: $`x^2-y=(2h_1-h_2)+h_1^2`$, and $`e^w=1+w+\frac{w^2}2+\dots`$ gives $`1+(2h_1-h_2)+h_1^2+\frac{(2h_1-h_2)^2}2`$ — the same.

**2.1.** On $`M`$: $`g(x)=f(x,2x)=x^3-6x^2+4x^2=x^3-2x^2`$. $`g'(x)=3x^2-4x=x(3x-4)`$, zeros $`x=0`$ and $`x=\frac43`$. $`g''(x)=6x-4`$: $`g''(0)=-4<0`$, $`g''(\frac43)=4>0`$.

Answer: $`(0;0)`$ is a strict constrained local maximum, $`f=0`$; $`(\frac43;\frac83)`$ is a strict constrained local minimum, $`f=\frac{64}{27}-\frac{32}9=-\frac{32}{27}`$. There are no global extrema: $`g(x)\to\pm\infty`$.

**2.2.** $`\nabla\varphi=(2x,2y,2z)\ne0`$ on $`M`$. Lagrange system: $`1=2\lambda x`$, $`-2=2\lambda y`$, $`2=2\lambda z`$; $`\lambda\ne0`$ and $`(x,y,z)=\frac1{2\lambda}(1,-2,2)=t(1,-2,2)`$. The constraint gives $`9t^2=9`$, $`t=\pm1`$. The sphere is compact and $`f`$ is continuous, so the greatest and least values are attained at stationary points.

Answer: $`(1;-2;2)`$ is the maximum, $`f=9`$; $`(-1;2;-2)`$ is the minimum, $`f=-9`$. There are no other extremum points. Check: by Cauchy–Schwarz, $`|x-2y+2z|\le\sqrt{1+4+4}\cdot\sqrt9=9`$.

**3.** Multiplying the inequality by $`\frac{a_n}{b_{n+1}}>0`$ gives $`\frac{a_{n+1}}{b_{n+1}}\le\frac{a_n}{b_n}`$ for $`n>N_0`$: the sequence $`\frac{a_n}{b_n}`$ is non-increasing, so $`a_n\le Cb_n`$ for $`n\ge N_0+1`$, where $`C=\frac{a_{N_0+1}}{b_{N_0+1}}`$. Let $`B`$ be the sum of $`\sum_{k>N_0}b_k`$ (it converges together with $`\sum b_k`$). Then $`\sum_{k=N_0+1}^na_k\le C\sum_{k=N_0+1}^nb_k\le CB`$. The partial sums of the positive series $`\sum_{k>N_0}a_k`$ are bounded, so it converges; adding finitely many terms does not change convergence.

Application: $`a_k=\frac1{k!}`$, $`b_k=\frac1{k(k+1)}`$ (the series $`\sum b_k`$ converges: its partial sums equal $`1-\frac1{n+1}`$). $`\frac{a_{k+1}}{a_k}=\frac1{k+1}`$, $`\frac{b_{k+1}}{b_k}=\frac k{k+2}`$; the inequality $`\frac1{k+1}\le\frac k{k+2}`$ is equivalent to $`k^2\ge2`$ and holds for $`k\ge2`$, i.e. $`N_0=1`$.

**4.** a) $`\dfrac{a_k}{a_{k+1}}=\dfrac{(2k+2)(2k+1)}{(k+1)^2}=\dfrac{2(2k+1)}{k+1}\ge3`$ for all $`k\ge1`$ (and tends to $`4`$). By d'Alembert's test with $`\beta=2`$ the series **converges**.

b) $`\dfrac{a_k}{a_{k+1}}=\dfrac{2k+4}{2k+1}=1+\dfrac3{2k+1}\to1`$ — d'Alembert does not work. $`R_k=\dfrac{3k}{2k+1}\to\dfrac32>1`$: by Raabe's test the series **converges**. (Without a limit: $`\frac3{2k+1}\ge\frac{5/4}k`$ for $`k\ge3`$, $`\gamma=\frac14`$.)

c) The signs alternate, $`\frac1{\ln(k+1)}`$ decreases and tends to zero: by Leibniz's test the series **converges**. There is no absolute convergence: $`\ln(k+1)\le k`$, so $`\frac1{\ln(k+1)}\ge\frac1k`$. The convergence is conditional.
</details>

## Variant B

**1.1.** Expand $`f(x,y,z)=xyz+x^2-z^2`$ by Taylor's formula at the point $`(1;2;-1)`$.

**1.2.** Find the explicit Taylor expansion of $`f(x,y)=\ln(x+y^2)`$ up to degree two with the Lagrange remainder at the point $`(1;0)`$.

**2.1.** Find all points of constrained local extremum of $`f(x,y,z)=xy+2z^2`$ on the set $`M=\{x+y=2,\ z=x-1\}`$.

**2.2.** Find all points of constrained extremum of $`f(x,y)=xy`$ on the set $`M=\{x^2+4y^2=8\}`$ and the extremal values.

**3.** State and prove Leibniz's test. Does it remain true if the condition $`a_ka_{k+1}<0`$ is replaced by $`a_ka_{k+1}\le0`$?

**4.** Test the series for convergence ($`\alpha\in\mathbb R`$ is a parameter):
```math
\text{a)}\ \sum_{k=1}^\infty\frac{k^k}{3^k\,k!};\qquad\text{b)}\ \sum_{k=1}^\infty\frac{\sqrt{k^2+1}-k}{k^\alpha};\qquad\text{c)}\ \sum_{k=1}^\infty\frac{\sin\frac{k\pi}2}{\sqrt[3]k} .
```

<details>
<summary>Solutions to variant B</summary>

**1.1.** Let $`h_1=x-1`$, $`h_2=y-2`$, $`h_3=z+1`$. $`f(a)=-2+1-1=-2`$. $`f_x=yz+2x=0`$, $`f_y=xz=-1`$, $`f_z=xy-2z=4`$. $`f_{xx}=2`$, $`f_{yy}=0`$, $`f_{zz}=-2`$, $`f_{xy}=z=-1`$, $`f_{xz}=y=2`$, $`f_{yz}=x=1`$. The only non-zero third derivative is $`f_{xyz}=1`$ (it enters with coefficient $`6`$ and is divided by $`3!`$). The sum is finite:

```math
f=-2-h_2+4h_3+h_1^2-h_3^2-h_1h_2+2h_1h_3+h_2h_3+h_1h_2h_3 .
```

Check: $`h=(0,0,1)`$, $`f(1,2,0)=1`$; the formula gives $`-2+4-1=1`$.

**1.2.** Let $`h_1=x-1`$, $`h_2=y`$, $`u=x+y^2`$. Derivatives: $`f_x=\frac1u`$, $`f_y=\frac{2y}u`$, $`f_{xx}=-\frac1{u^2}`$, $`f_{xy}=-\frac{2y}{u^2}`$, $`f_{yy}=\frac2u-\frac{4y^2}{u^2}`$. At $`(1;0)`$: $`f=0`$, $`f_x=1`$, $`f_y=0`$, $`f_{xx}=-1`$, $`f_{xy}=0`$, $`f_{yy}=2`$. Third derivatives:

```math
f_{xxx}=\frac2{u^3},\quad f_{xxy}=\frac{4y}{u^3},\quad f_{xyy}=\frac{8y^2-2u}{u^3},\quad f_{yyy}=\frac{16y^3-12uy}{u^3}.
```

For $`h`$ such that the segment from $`(1;0)`$ to $`(1+h_1;h_2)`$ lies in the domain $`x+y^2>0`$, there is $`\theta\in(0,1)`$ such that

```math
\ln(x+y^2)=h_1-\frac{h_1^2}2+h_2^2+R_2,
```

```math
R_2=\frac{1}{6u_c^3}\Bigl[2h_1^3+12\eta h_1^2h_2+3(8\eta^2-2u_c)h_1h_2^2+(16\eta^3-12u_c\eta)h_2^3\Bigr],
```

where $`\xi=1+\theta h_1`$, $`\eta=\theta h_2`$, $`u_c=\xi+\eta^2`$.

Check of the polynomial: $`x+y^2=1+w`$, $`w=h_1+h_2^2`$, $`\ln(1+w)=w-\frac{w^2}2+\dots=h_1+h_2^2-\frac{h_1^2}2+\dots`$

**2.1.** The constraints can be solved: $`y=2-x`$, $`z=x-1`$. $`g(x)=x(2-x)+2(x-1)^2=x^2-2x+2=(x-1)^2+1`$. The only extremum point is $`x=1`$, a minimum.

Answer: $`(1;1;0)`$ is a strict constrained minimum (global on $`M`$), $`f=1`$. There is no maximum: $`g(x)\to+\infty`$.

**2.2.** $`\nabla\varphi=(2x,8y)\ne0`$ on $`M`$. System: $`y=2\lambda x`$, $`x=8\lambda y`$. Substituting: $`y=16\lambda^2y`$. If $`y=0`$, then $`x=0`$ — a point not on $`M`$; so $`\lambda=\pm\frac14`$. For $`\lambda=\frac14`$: $`x=2y`$, $`8y^2=8`$, the points $`(2;1)`$ and $`(-2;-1)`$, $`f=2`$. For $`\lambda=-\frac14`$: $`x=-2y`$, the points $`(-2;1)`$ and $`(2;-1)`$, $`f=-2`$. The ellipse is compact.

Answer: maximum $`f=2`$ at $`(2;1)`$, $`(-2;-1)`$; minimum $`f=-2`$ at $`(-2;1)`$, $`(2;-1)`$. Check: $`8=x^2+4y^2\ge2\cdot|x|\cdot2|y|=4|xy|`$.

**3.** *Statement.* If for all $`k`$ we have $`a_ka_{k+1}<0`$, $`|a_{k+1}|\le|a_k|`$ and $`a_k\to0`$, then the series $`\sum a_k`$ converges.

*Proof.* We may assume $`a_1>0`$ (otherwise multiply the series by $`-1`$); then $`a_{2j-1}>0`$, $`a_{2j}<0`$. The brackets $`a_{2j-1}+a_{2j}=|a_{2j-1}|-|a_{2j}|\ge0`$, so $`S_{2m}=\sum_{j=1}^m(a_{2j-1}+a_{2j})`$ is non-decreasing. On the other hand, $`S_{2m}=a_1+\sum_{j=1}^{m-1}(a_{2j}+a_{2j+1})+a_{2m}\le a_1`$, since $`a_{2j}+a_{2j+1}=-|a_{2j}|+|a_{2j+1}|\le0`$ and $`a_{2m}<0`$. The monotone bounded sequence $`S_{2m}`$ converges to some $`S`$. Then $`S_{2m+1}=S_{2m}+a_{2m+1}\to S`$, since $`a_k\to0`$. The subsequences with even and odd indices converge to the same limit, hence $`S_n\to S`$.

*The question.* Yes. If all $`a_k\ne0`$, the condition $`\le0`$ coincides with $`<0`$. If $`a_K=0`$, then $`|a_{k+1}|\le|a_k|`$ gives $`a_k=0`$ for $`k\ge K`$, and the series is a finite sum.

**4.** a) $`\dfrac{a_k}{a_{k+1}}=\dfrac{k^k}{3^kk!}\cdot\dfrac{3^{k+1}(k+1)!}{(k+1)^{k+1}}=\dfrac{3}{\bigl(1+\frac1k\bigr)^k}>\dfrac3e>1`$ for all $`k`$, since $`\bigl(1+\frac1k\bigr)^k<e`$. By d'Alembert's test with $`\beta=\frac3e-1`$ the series **converges**.

b) $`\sqrt{k^2+1}-k=\dfrac{1}{\sqrt{k^2+1}+k}`$, so $`a_k=\dfrac{C_k}{k^{\alpha+1}}`$, $`C_k=\dfrac{k}{\sqrt{k^2+1}+k}`$. Since $`k<\sqrt{k^2+1}\le\sqrt2\,k`$, we have $`\dfrac1{1+\sqrt2}\le C_k<\dfrac12`$. By problem 3.11 the series **converges for $`\alpha>0`$ and diverges for $`\alpha\le0`$**.

c) For even $`k`$ the terms are zero; for $`k=2j-1`$ the numerator is $`(-1)^{j-1}`$. The non-zero terms $`c_j=\dfrac{(-1)^{j-1}}{\sqrt[3]{2j-1}}`$ form a series that converges by Leibniz's test; inserting zeros does not change the partial sums ($`S_{2m-1}=S_{2m}=T_m`$). The series **converges** (conditionally: $`\sum\frac1{\sqrt[3]{2j-1}}`$ diverges).
</details>

## Variant C

**1.1.** Expand $`f(x,y)=x^4-x^2y+y^3`$ by Taylor's formula at the point $`(-1;1)`$.

**1.2.** Find the explicit Taylor expansion of $`f(x,y)=e^y\sin x`$ up to degree two with the Lagrange remainder at the point $`(\pi;0)`$.

**2.1.** Find all points of constrained local extremum of $`f(x,y,z)=x^4+y^2-2z^2`$ on the set $`M=\{z=x\}`$.

**2.2.** Find all points of constrained extremum of $`f(x,y,z)=x+y+z`$ on the set $`M=\{x^2+y^2=2,\ x+z=1\}`$ and the extremal values.

**3.** Let $`x_n>0`$ and $`a_n>0`$ for all $`n`$, and let there be $`\alpha>0`$ and $`N`$ such that $`x_n\dfrac{a_n}{a_{n+1}}-x_{n+1}\ge\alpha`$ for all $`n>N`$. Prove that the series $`\sum a_k`$ converges. Derive from this d'Alembert's convergence test. Why does d'Alembert's test say nothing about the series $`\sum\frac1{k^2}`$?

**4.** Test the series for convergence:
```math
\text{a)}\ \sum_{k=1}^\infty\Bigl(\frac{k+1}{2k+3}\Bigr)^k;\qquad\text{b)}\ \sum_{k=2}^\infty\frac{1}{k\ln^2k};\qquad\text{c)}\ \sum_{k=1}^\infty\frac{(-1)^kk}{k^2+1} .
```

<details>
<summary>Solutions to variant C</summary>

**1.1.** Let $`h_1=x+1`$, $`h_2=y-1`$. $`f(a)=1-1+1=1`$. $`f_x=4x^3-2xy=-2`$, $`f_y=-x^2+3y^2=2`$. $`f_{xx}=12x^2-2y=10`$, $`f_{xy}=-2x=2`$, $`f_{yy}=6y=6`$. $`f_{xxx}=24x=-24`$, $`f_{xxy}=-2`$, $`f_{xyy}=0`$, $`f_{yyy}=6`$. $`f_{xxxx}=24`$, the other fourth derivatives vanish; the fifth derivatives vanish, the sum is finite:

```math
f=1-2h_1+2h_2+5h_1^2+2h_1h_2+3h_2^2-4h_1^3-h_1^2h_2+h_2^3+h_1^4 .
```

Check: $`h=(1,0)`$, $`f(0,1)=1`$; the formula gives $`1-2+5-4+1=1`$.

**1.2.** Let $`h_1=x-\pi`$, $`h_2=y`$. $`f_x=e^y\cos x`$, $`f_y=e^y\sin x`$, $`f_{xx}=-e^y\sin x`$, $`f_{xy}=e^y\cos x`$, $`f_{yy}=e^y\sin x`$. At $`(\pi;0)`$: $`f=0`$, $`f_x=-1`$, $`f_y=0`$, $`f_{xx}=0`$, $`f_{xy}=-1`$, $`f_{yy}=0`$. Third derivatives: $`f_{xxx}=-e^y\cos x`$, $`f_{xxy}=-e^y\sin x`$, $`f_{xyy}=e^y\cos x`$, $`f_{yyy}=e^y\sin x`$. There is $`\theta\in(0,1)`$ such that

```math
e^y\sin x=-h_1-h_1h_2+R_2,
```

```math
R_2=\frac{e^{\eta}}6\Bigl[-\cos\xi\cdot h_1^3-3\sin\xi\cdot h_1^2h_2+3\cos\xi\cdot h_1h_2^2+\sin\xi\cdot h_2^3\Bigr],\qquad\xi=\pi+\theta h_1,\ \eta=\theta h_2 .
```

Check of the polynomial: $`\sin(\pi+h_1)=-\sin h_1=-h_1+\dots`$, $`e^{h_2}=1+h_2+\dots`$, the product up to degree two is $`-h_1-h_1h_2`$.

**2.1.** On $`M`$: $`g(x,y)=f(x,y,x)=x^4-2x^2+y^2`$. $`g_x=4x^3-4x=4x(x^2-1)`$, $`g_y=2y`$; stationary points $`(0,0)`$, $`(1,0)`$, $`(-1,0)`$. The Hessian is $`\operatorname{diag}(12x^2-4,\ 2)`$: at $`(0,0)`$ it is $`\operatorname{diag}(-4,2)`$, indefinite, no extremum; at $`(\pm1,0)`$ it is $`\operatorname{diag}(8,2)`$, a minimum.

Answer: $`(1;0;1)`$ and $`(-1;0;-1)`$ are strict constrained local minima, $`f=-1`$ (they are also global on $`M`$: $`g=(x^2-1)^2+y^2-1\ge-1`$). The point $`(0;0;0)`$ is stationary but not an extremum. There is no maximum.

**2.2.** The gradients of the constraints $`(2x,2y,0)`$ and $`(1,0,1)`$ are linearly dependent only for $`x=y=0`$, and there are no such points on $`M`$. $`L=x+y+z-\lambda(x^2+y^2-2)-\mu(x+z-1)`$:

```math
1-2\lambda x-\mu=0,\qquad1-2\lambda y=0,\qquad1-\mu=0 .
```

The third gives $`\mu=1`$, the first $`\lambda x=0`$, the second $`\lambda\ne0`$; hence $`x=0`$, $`y=\pm\sqrt2`$, $`z=1`$. The set $`M`$ is closed and bounded ($`|x|,|y|\le\sqrt2`$, $`z=1-x`$), i.e. compact.

Answer: $`(0;\sqrt2;1)`$ is the maximum, $`f=1+\sqrt2`$; $`(0;-\sqrt2;1)`$ is the minimum, $`f=1-\sqrt2`$. Check: on $`M`$ we have $`f=x+y+(1-x)=y+1`$, and $`|y|\le\sqrt2`$.

**3.** Multiply the inequality by $`a_{n+1}>0`$: $`x_na_n-x_{n+1}a_{n+1}\ge\alpha a_{n+1}`$ for $`n>N`$. Add over $`n=N+1,\dots,N+m`$; the left-hand side telescopes:

```math
\alpha\sum_{n=N+1}^{N+m}a_{n+1}\le x_{N+1}a_{N+1}-x_{N+m+1}a_{N+m+1}<x_{N+1}a_{N+1}.
```

The partial sums of the positive series $`\sum_{k\ge N+2}a_k`$ are bounded by $`\frac{x_{N+1}a_{N+1}}{\alpha}`$, so it converges, and with it $`\sum a_k`$.

*D'Alembert.* Take $`x_n=1`$: the condition becomes $`\frac{a_n}{a_{n+1}}-1\ge\alpha`$, i.e. $`\frac{a_n}{a_{n+1}}\ge1+\beta`$ with $`\beta=\alpha`$. So if $`\frac{a_n}{a_{n+1}}\ge1+\beta`$ for $`n>N`$, $`\beta>0`$, the series converges.

*The series $`\sum\frac1{k^2}`$.* $`\frac{a_k}{a_{k+1}}=\bigl(1+\frac1k\bigr)^2\to1`$. This ratio exceeds $`1`$ for all $`k`$, so the divergence condition $`\frac{a_k}{a_{k+1}}\le1`$ fails; and it tends to $`1`$, so for no constant $`\beta>0`$ does $`\frac{a_k}{a_{k+1}}\ge1+\beta`$ hold for all large $`k`$. D'Alembert's test compares the series with a geometric progression, and $`\frac1{k^2}`$ decays slower than any progression. Raabe's test works here: $`\bigl(1+\frac1k\bigr)^2\ge1+\frac2k`$, $`\gamma=1`$.

**4.** a) $`\dfrac{k+1}{2k+3}<\dfrac12`$ for all $`k`$ (since $`2k+2<2k+3`$), so $`0<a_k<2^{-k}`$. By comparison with a geometric progression the series **converges**. (Cauchy's test: $`\sqrt[k]{a_k}\to\frac12<1`$.)

b) The function $`f(x)=\dfrac1{x\ln^2x}`$ is positive and decreasing on $`[2;+\infty)`$ (the denominator increases). $`\displaystyle\int_2^x\frac{dy}{y\ln^2y}=\frac1{\ln2}-\frac1{\ln x}\to\frac1{\ln2}`$. The integral converges, so by the integral test the series **converges**. (D'Alembert and Raabe are silent here: $`R_k\to1`$.)

c) The signs alternate. The absolute values $`\frac{k}{k^2+1}`$ decrease: the inequality $`\frac{k}{k^2+1}\ge\frac{k+1}{(k+1)^2+1}`$ is equivalent to $`k^2+k\ge1`$. The absolute values tend to zero. By Leibniz's test the series **converges**. There is no absolute convergence: $`\frac{k}{k^2+1}\ge\frac1{2k}`$. The convergence is conditional.
</details>

## What each variant tests

| Item | Variant A | Variant B | Variant C |
|---|---|---|---|
| 1.1 | cubic polynomial, 2 variables | polynomial, 3 variables, mixed derivative $`f_{xyz}`$ | quartic polynomial |
| 1.2 | exponential of a polynomial | logarithm (domain) | the product $`e^y\sin x`$ |
| 2.1 | constraint $`y=2x`$, maximum and minimum | two constraints, one minimum | a saddle and two minima |
| 2.2 | linear function on a sphere | $`xy`$ on an ellipse, four points | two constraints, two multipliers |
| 3 | generalised comparison | Leibniz | Kummer ⟹ d'Alembert |
| 4 | d'Alembert, Raabe, Leibniz | d'Alembert with $`e`$, a parameter, Leibniz with zeros | comparison (Cauchy), integral test, Leibniz |
