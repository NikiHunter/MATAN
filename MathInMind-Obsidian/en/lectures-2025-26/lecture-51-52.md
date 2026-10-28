---
title: "Lectures 51–52 — area, volume, paths and integral applications"
lang: en
course: "Математический анализ, 2025/26"
lecture: 51-52
semester: 2
date: 2026-04-16
source: "ma25_26-lectures_51-52_notes.pdf.txt"
pdf_pages: 40
typed_slides: 37
aliases: ["Lectures 51–52 (en)"]
tags: [mathinmind/en, mathinmind/lecture]
---

# Lectures 51–52 — area, volume, paths and integral applications

[[en/lectures-2025-26/lecture-49-50|← Lectures 49–50]] · [[en/lectures-2025-26/index|Lecture index]] · [[en/lectures-2025-26/lecture-53|Lecture 53 →]] · [[en/term-index|Terms & theorems]] · [[ru/lectures-2025-26/lecture-51-52|Русский]] · [[es/lectures-2025-26/lecture-51-52|Español]]


> [!info] Source and coverage
> `ma25_26-lectures_51-52_notes.pdf.txt`: 40 PDF pages, 37 printed slides, dated 16 April 2026. Every page is accounted for; PDF pages 9, 17 and 27 are handwritten-only. Handwritten annotations on slides 5, 14–16, 21, 24, 28, 32 and 39 are included. This transcription uses only the attached PDF; the source-notes folder was not consulted, so no archive filenames or links are claimed.

> [!info] Semester-2 duplication
> This standalone transcription of lectures 51–52 overlaps thematically with [[ru/lectures/07-measure-paths-4-6|§4.6]] and [[ru/lectures/08-integral-applications-4-7|§4.7]] in the register; see also the [[ru/lectures/index|semester-2 register]]. Semester 2 spans lectures 33–64.

## Printed slide 1 (PDF p. 1) — Title slide

“Mathematical Analysis”, lectures 51–52; D. E. Apushkinskaya, RUDN University; 16 April 2026.

## Printed slide 2 (PDF p. 2) — Quote of the day

“In the end, everything will be all right. If it is not all right yet, then it is not the end.” Paulo Coelho.

## Printed slide 3 (PDF p. 3) — Lecture goals

Length, area and volume; paths, their properties and length; geometric applications of the [[en/lectures-2025-26/lecture-39-40#^def-4-2-6|Riemann integral]].

## Printed slide 4 (PDF p. 4) — Chapter 4, §6. Length, area and volume

Geometric characteristics are introduced only to the extent needed for the integral applications that follow.

## Printed slide 5 (PDF p. 5) — Area and rigid motions

> [!definition] Definition 4.6.1

^def-4-6-1

[[en/lectures-2025-26/lecture-54#^def-5-1-1|Euclidean distance]] in $\mathbb R^n$ is given by the formula below. A motion preserves the distance between every pair of points.


$$
\|A-B\|=\sqrt{\sum_{i=1}^{n}(A_i-B_i)^2}
$$

## Printed slide 6 (PDF p. 6) — Axioms of area

> [!definition] Definition 4.6.2

^def-4-6-2

Area is defined on a class of quadrable plane figures: finite additivity for disjoint figures, normalization on rectangles, and invariance under motions.


$$
S(P_1\cup P_2)=S(P_1)+S(P_2)
$$


$$
S([0,a]\times[0,b])=ab
$$


$$
S(U(P))=S(P)
$$

## Printed slide 7 (PDF p. 7) — Limits of the area definition

The class of quadrable figures is not formally defined; existence and uniqueness of area are accepted as geometric facts here.

## Printed slide 8 (PDF p. 8) — Further properties of area

Area is monotone; a subset of a line segment has zero area; additivity still holds when the intersection has zero area, for example a line segment.


$$
P_1\subset P\Longrightarrow S(P_1)\le S(P)
$$


$$
P\subset\text{ a line segment}\Longrightarrow S(P)=0
$$


$$
S(P_1\cup P_2)=S(P_1)+S(P_2)
$$

## Handwritten page (PDF p. 9) — Area properties: proof sketches

The handwritten page gives three short area-property proofs. Monotonicity is obtained by comparing inner and outer rectangles. If a set fits inside rectangles of arbitrarily small area, its area is zero. When the intersection has zero area, removing the shared part does not change area, which yields strengthened additivity.

## Printed slide 9 (PDF p. 10) — Volume

> [!definition] Definition 4.6.3

^def-4-6-3

Volume for cubable bodies in $\mathbb R^3$ has additivity, normalization on rectangular boxes, and invariance under motions.


$$
V(T_1\cup T_2)=V(T_1)+V(T_2)
$$


$$
V([0,a]\times[0,b]\times[0,c])=abc
$$


$$
V(U(T))=V(T)
$$

## Printed slide 10 (PDF p. 11) — Existence of volume

As with quadrability, cubability is not formally defined; existence of volume is accepted without proof.

## Printed slide 11 (PDF p. 12) — Further properties of volume

Volume is monotone, a body contained in a planar rectangle has zero volume, and intersections of zero volume do not affect additivity.


$$
T_1\subset T\Longrightarrow V(T_1)\le V(T)
$$


$$
V(T)=0
$$


$$
V(T_1\cup T_2)=V(T_1)+V(T_2)
$$

## Printed slide 12 (PDF p. 13) — Right cylinder and cross-section

> [!definition] Definition 4.6.4
> **Definition 4.6.5.**

^def-4-6-5

For $P\subset\mathbb R^2$ and $h>0$, the right cylinder $P\times[0,h]$ has volume $S(P)h$. The section of a body by the plane with first coordinate $x$ is denoted $T(x)$.


$$
Q=P\times[0,h],\qquad V(Q)=S(P)h
$$


$$
T(x)=\{(y,z)\in\mathbb R^2:(x,y,z)\in T\}
$$

## Printed slide 13 (PDF p. 14) — A path

> [!definition] Definition 4.6.6

^def-4-6-6

A path in $\mathbb R^m$ is a continuous map from $[a,b]$: $\gamma=(\gamma_1,\ldots,\gamma_m)$. The points $\gamma(a)$ and $\gamma(b)$ are its initial and terminal points.


$$
\gamma:[a,b]\to\mathbb R^m,\qquad \gamma=(\gamma_1,\ldots,\gamma_m)
$$

## Printed slide 14 (PDF p. 15) — Path properties

The image $\gamma([a,b])$ is its trace; a path is closed when its endpoints agree and simple when it has no self-intersections except possibly matching endpoints. Smoothness is coordinatewise; a piecewise-smooth path is smooth on each interval of a [[en/lectures-2025-26/lecture-37-38#^def-4-2-2|partition]].


$$
\gamma(a)=\gamma(b)
$$


$$
\gamma(t_1)=\gamma(t_2)\Longrightarrow t_1=t_2\text{ or }\{t_1,t_2\}=\{a,b\}
$$

## Printed slide 15 (PDF p. 16) — Reverse path and equivalence

> [!definition] Definition 4.6.7

^def-4-6-7

The reverse path traverses the same curve in the opposite direction. Paths are equivalent under a strictly increasing reparametrization; an equivalence class is a curve, and its members are parametrizations.


$$
\gamma^-(t)=\gamma(a+b-t)
$$


$$
\gamma=\widetilde\gamma\circ u
$$

## Handwritten page (PDF p. 17) — Different paths with one trace

Four parametrizations of the upper semicircle are listed. Their formulas and parameter intervals differ, but their geometric trace is the same. Reversing a path changes its direction, not its trace.


![Different paths with one trace (PDF p. 17)](../../assets/lectures-2025-26/lec51-52-p17-path-example.jpg)

## Printed slide 16 (PDF p. 18) — Inscribed polygonal path

> [!definition] Definition 4.6.8

^def-4-6-8

For a partition $a=t_0<\cdots<t_n=b$, the inscribed polygon joins successive points $\gamma(t_k)$; its length is the sum of the segment lengths.


$$
\ell_\tau=\sum_{k=0}^{n-1}\|\gamma(t_{k+1})-\gamma(t_k)\|
$$

## Printed slide 17 (PDF p. 19) — Length and rectifiability

> [!definition] Definition 4.6.9
> **Definition 4.6.10.**

^def-4-6-10

The [[en/lectures-2025-26/lecture-53#^thm-4-7-1|length of a path]] is the [[en/lectures-2025-26/lecture-11-12#^def-2-3-1|supremum]] of all inscribed polygonal lengths; the path is rectifiable when this supremum is finite.


$$
s_\gamma=\sup_\tau\ell_\tau
$$


$$
s_\gamma<+\infty
$$

## Printed slide 18 (PDF p. 20) — Chapter 4, §7. Applications of the Riemann integral

A geometric quantity is bounded by special lower and [[en/lectures-2025-26/lecture-39-40#^def-4-2-8|upper sums]]; their common limit is expressed as an integral.

## Printed slide 19 (PDF p. 21) — Subgraph

> [!definition] Definition 4.7.1

^def-4-7-1

For $f\ge0$, the region under the graph on $[a,b]$ is defined below. If $f$ is continuous, it is called a curvilinear trapezoid.


$$
Q_f=\{(x,y)\in\mathbb R^2:x\in[a,b],\ 0\le y\le f(x)\}
$$

## Printed slide 20 (PDF p. 22) — Area under a graph: Darboux sums

On a partition, take the [[en/lectures-2025-26/lecture-11-12#^def-2-3-2|infimum]] and supremum of $f$ on each subinterval. Multiplying by subinterval widths gives the lower and upper sums.


$$
m_k=\inf_{x\in[x_k,x_{k+1}]}f(x),\qquad M_k=\sup_{x\in[x_k,x_{k+1}]}f(x)
$$


$$
s_\tau=\sum_{k=0}^{n-1}m_k\Delta x_k,\qquad S_\tau=\sum_{k=0}^{n-1}M_k\Delta x_k
$$

## Printed slide 21 (PDF p. 23) — Geometric meaning of the sums

The lower sum is the area of rectangles contained in the subgraph; the upper sum is the area of rectangles covering it.

## Printed slide 22 (PDF p. 24) — Area under a graph

The area lies between the lower and upper sums. For Riemann-integrable $f$, both Darboux sums converge to the same number, its Riemann integral.


$$
s_\tau\le S(Q_f)\le S_\tau
$$


$$
\sup_\tau s_\tau=\inf_\tau S_\tau=\int_a^b f(x)\,dx
$$


$$
S(Q_f)=\int_a^b f(x)\,dx
$$

## Printed slide 23 (PDF p. 25) — Sign and area

For a nonnegative function, the area under its graph is the integral; for a nonpositive function it is the integral of $-f$. The area between the graph and axis is the integral of $|f|$.


$$
S(Q_f)=\int_a^b|f(x)|\,dx
$$

## Printed slide 24 (PDF p. 26) — Area between two graphs

If integrable functions satisfy $f\le g$, the area between their graphs is the integral of the difference $g-f$.


$$
S=\int_a^b(g(x)-f(x))\,dx
$$

## Handwritten page (PDF p. 27) — Area between graphs: proof

Set $c=\inf_{x\in[a,b]}f(x)$. Then $f-c\ge0$ and $g-c\ge0$. The area between the graphs is the area under $g-c$ minus the area under $f-c$; the constant $c$ cancels, leaving the integral of $g-f$.

## Printed slide 25 (PDF p. 28) — Area formula in polar coordinates

A curvilinear sector is described by $0\le r\le f(\varphi)$ and $\varphi\in[\alpha,\beta]$, with $f\ge0$; handwritten labels give $x=r\cos\varphi$, $y=r\sin\varphi$.


$$
x=r\cos\varphi,\qquad y=r\sin\varphi
$$


$$
\widetilde Q_f=\{(r\cos\varphi,r\sin\varphi):\varphi\in[\alpha,\beta],\ 0\le r\le f(\varphi)\}
$$


![Area formula in polar coordinates (PDF p. 28)](../../assets/lectures-2025-26/lec51-52-p28-polar-sector.jpg)

## Printed slide 26 (PDF p. 29) — Polar sums of sectors

On a partition of the angular interval, the minimum and maximum radii determine inscribed and circumscribed circular sectors; each sector has area equal to half the squared radius times its angle.


$$
s_\tau=\frac12\sum_{k=0}^{n-1}m_k^2\Delta\varphi_k,\qquad S_\tau=\frac12\sum_{k=0}^{n-1}M_k^2\Delta\varphi_k
$$

## Printed slide 27 (PDF p. 30) — Limit of polar sums

The sector-area sums are squeezed and are Darboux sums for $f^2/2$.

## Printed slide 28 (PDF p. 31) — Area in polar coordinates

Passing to the integral gives the area formula for a curvilinear sector.


$$
S(\widetilde Q_f)=\frac12\int_\alpha^\beta f^2(\varphi)\,d\varphi
$$

## Printed slide 29 (PDF p. 32) — Volume from cross-sectional areas

The body lies over a finite interval; its cross-sections are quadrable with area $S(x)$, and nested extreme sections bound the intermediate ones on each short interval. Continuity of $S$ is assumed.


$$
S(x)=\operatorname{area}(T(x))
$$


$$
S\in C[a,b]
$$


![Volume from cross-sectional areas (PDF p. 32)](../../assets/lectures-2025-26/lec51-52-p32-volume-slice.jpg)

## Printed slide 30 (PDF p. 33) — Lower and upper sections

For each subinterval, choose sections with the smallest and largest area; monotonicity of area yields the infimum and supremum of $S$.


$$
m_k=\inf_{x\in[x_k,x_{k+1}]}S(x),\qquad M_k=\sup_{x\in[x_k,x_{k+1}]}S(x)
$$

## Printed slide 31 (PDF p. 34) — Cylinders built on cross-sections

The sections with least and greatest area define lower and upper cylinders over each partition interval.


$$
q_k=[x_k,x_{k+1}]\times T(\xi_k^*),\qquad Q_k=[x_k,x_{k+1}]\times T(\xi_k^{**})
$$

## Printed slide 32 (PDF p. 35) — Layers of the body

Each layer is trapped between the corresponding cylinders; the union of lower cylinders lies in the body, and the body lies in the union of upper cylinders.


$$
q_k\subset T_k\subset Q_k
$$


$$
w_\tau=\sum_{k=0}^{n-1}m_k\Delta x_k,\qquad W_\tau=\sum_{k=0}^{n-1}M_k\Delta x_k
$$

## Printed slide 33 (PDF p. 36) — Cylinder-volume sums

Additivity turns the volumes of the unions into sums of base areas times interval widths.


$$
V\left(\bigcup_{k=0}^{n-1}q_k\right)=w_\tau,\qquad V\left(\bigcup_{k=0}^{n-1}Q_k\right)=W_\tau
$$

## Printed slide 34 (PDF p. 37) — Volume as an integral of cross-sectional area

The volume lies between Darboux sums of the cross-sectional area function; if $S$ is integrable, both bounds converge to the same integral.


$$
w_\tau\le V(T)\le W_\tau
$$


$$
V(T)=\int_a^b S(x)\,dx
$$

## Printed slide 35 (PDF p. 38) — Solids of revolution

Revolving the subgraph of $f\ge0$ around the $OX$ axis is described by $y^2+z^2\le f^2(x)$.


$$
T_f=\{(x,y,z)\in\mathbb R^3:x\in[a,b],\ y^2+z^2\le f^2(x)\}
$$

## Printed slide 36 (PDF p. 39) — Volume of revolution about $OX$

Each section is a disk of radius $f(x)$ and area $\pi f^2(x)$; apply the cross-sectional volume formula.


$$
S(x)=\pi f^2(x)
$$


$$
V(T_f)=\pi\int_a^b f^2(x)\,dx
$$

## Printed slide 37 (PDF p. 40) — Additional formulas for solids of revolution

For rotation about $OY$, use cylindrical shells; a polar sector gives a separate formula. For unbounded sets, the corresponding integrals are improper.


$$
V(T_f^\prime)=2\pi\int_a^b xf(x)\,dx
$$


$$
V(\widetilde T_f)=\frac{2\pi}{3}\int_\alpha^\beta f^3(\varphi)\cos\varphi\,d\varphi
$$


---

[[en/lectures-2025-26/lecture-49-50|← Lectures 49–50]] · [[en/lectures-2025-26/index|Lecture index]] · [[en/lectures-2025-26/lecture-53|Lecture 53 →]] · [[en/term-index|Terms & theorems]] · [[ru/lectures-2025-26/lecture-51-52|Русский]] · [[es/lectures-2025-26/lecture-51-52|Español]]

