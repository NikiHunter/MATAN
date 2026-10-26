---
title: "Lectures 57–58 — Interior, Boundary, Compactness and the Limit of a Map"
lang: en
course: "Mathematical Analysis, 2025/26"
lecture: 57-58
semester: 2
date: 2026-05-07
source: "ma25_26-lectures_57-58_notes.pdf.txt"
pdf_pages: 37
typed_slides: 18
---

# Lectures 57–58 — Interior, Boundary, Compactness and the Limit of a Map

[Lecture index](index.md) · [Русский](../../ru/lectures-2025-26/lecture-57-58.md) · [Español](../../es/lectures-2025-26/lecture-57-58.md) · [Previous: 55–56](lecture-55-56.md) · [Next: 59–60](lecture-59-60.md)


> **Source and coverage.** `ma25_26-lectures_57-58_notes.pdf.txt`: 37 PDF pages, 18 printed slides and 19 handwritten pages; dated 7 May 2026. Printed slides 1–4 occupy PDF pages 1–4; after that slide 5 is on PDF page 7, slide 6 on 10, slide 7 on 13, slide 8 on 14, slide 9 on 15, slide 10 on 17, slide 11 on 22, slide 12 on 23, slide 13 on 24, slide 14 on 25, slide 15 on 29, slide 16 on 32, slide 17 on 33 and slide 18 on 35. Handwritten PDF pages 5, 6, 8, 9, 11, 12, 16, 18, 19, 20, 21, 26, 27, 28, 30, 31, 34, 36 and 37 are included. Handwritten annotations on slides 4, 5 and 11 are attributed to their slides. Only the PDF supplied in the chat was used; the source folder was not consulted, so archive names and links are not given.

> **Semester-2 duplication.** The lecture overlaps thematically with [§5.3](../../ru/lectures/11-topology-rn-5-3.md) and [§5.4](../../ru/lectures/12-mapping-limits-5-4.md); see also the [register](../../ru/lectures/index.md). Semester 2 covers lectures 33–64.

## Printed slide 1 (PDF p. 1) — Title slide

"Mathematical Analysis", lectures 57–58; D. E. Apushkinskaya, RUDN University; 7 May 2026.

## Printed slide 2 (PDF p. 2) — Quote of the day

"Three apples changed our world: the first tempted Eve, the second woke Newton, and the third caught the eye of Steve Jobs." Beneath the quotation the slide shows the cover of the book "Three apples that changed the world" with portraits of Newton, Eve and Jobs; it is a decorative illustration, not mathematical material.

## Printed slide 3 (PDF p. 3) — Aim of the lecture

The description in $\mathbb R^n$ of reasonable analogues of open and closed intervals and of compact sets continues. The notion of the limit of a map of several variables is introduced, and analogues of some one-dimensional statements are proved for such maps.

## Printed slide 4 (PDF p. 4) — The interior of a set — Definition 5.3.3

**Definition 5.3.3.** Let $E\subset\mathbb R^n$. The set of all interior points of $E$ is called the interior of $E$ and is denoted by $\operatorname{Int}E$.

**Remarks.** 1) For every $E\subset\mathbb R^n$ the set $\operatorname{Int}E$ is open in $\mathbb R^n$. 2) If $G$ is open in $\mathbb R^n$ and $G\subset E$, then $G\subset\operatorname{Int}E$. 3) For every $E\subset\mathbb R^n$,

$$
\mathbb R^n\setminus\overline E=\operatorname{Int}\left(\mathbb R^n\setminus E\right),
$$

$$
\mathbb R^n\setminus\operatorname{Int}E=\overline{\left(\mathbb R^n\setminus E\right)}.
$$

4) If $E$ is open, then $\operatorname{Int}E=E$. 5) If $E\subset\mathbb R^n$, then $\operatorname{Int}E$ is the largest open set contained in $E$ with respect to inclusion.

![Definition 5.3.3 and remarks (PDF p. 4)](../../assets/lectures-2025-26/lec57-58-p04-interior-remarks.jpg)

> **Marks on the slide.** Remark 3 carries the mark "ex!" — the equalities are left to the reader. At the bottom, by hand: "If $E$ is open, then $\operatorname{Int}E=E$" — that is remark 4, written in the margin. In the PDF text layer the overlines in remark 3 are partly lost; here they are restored from the page image.

## Handwritten page (PDF p. 5) — Remark 1: $\operatorname{Int}E$ is open

Statement: $\forall E\subset\mathbb R^n\Rightarrow\operatorname{Int}E$ is open in $\mathbb R^n$.

Proof. Let $a\in\operatorname{Int}E$; then, by the definition of an interior point, $\exists\delta>0$: $V_\delta(a)\subset E$. The set $V_\delta(a)$ is open, so $\forall x\in V_\delta(a)$ is an interior point for $V_\delta(a)$ and hence, all the more, for $E$. Consequently $V_\delta(a)\subset\operatorname{Int}E$; thus every point of $\operatorname{Int}E$ has a neighbourhood lying in $\operatorname{Int}E$, that is, $\operatorname{Int}E$ is open.

$$
a\in\operatorname{Int}E\ \Longrightarrow\ \exists\delta>0:\ V_\delta(a)\subset E
$$

$$
V_\delta(a)\subset\operatorname{Int}E
$$

![Proof that the interior is open (PDF p. 5)](../../assets/lectures-2025-26/lec57-58-p05-interior-open-proof.jpg)

## Handwritten page (PDF p. 6) — Remark 2: $G\subset\operatorname{Int}E$

Statement: if $G$ is open in $\mathbb R^n$ and $G\subset E$, then $G\subset\operatorname{Int}E$.

Proof. Let $a\in G$; since $G$ is open, $a$ is an interior point of $G$. Because $G\subset E$, the point $a$ is also interior for $E$. Hence $a\in\operatorname{Int}E$, that is, $G\subset\operatorname{Int}E$.

$$
\left.\begin{aligned} a&\in G\\ G&\text{ — open}\end{aligned}\right\}\Longrightarrow a\ \text{is an interior point of } G
$$

$$
a\in\operatorname{Int}E
$$

## Printed slide 5 (PDF p. 7) — The boundary of a set — Definition 5.3.4

**Definition 5.3.4.** Let $E\subset\mathbb R^n$. The set $E\setminus\operatorname{Int}E$ is called the boundary of $E$ and is denoted by $\partial E$.

**Remark.** The boundary $\partial E$ of any set $E\subset\mathbb R^n$ is closed.

**Example.** Let $a\in\mathbb R^n$, $\delta>0$. Then the following statements hold. 1) $\operatorname{Int}B_\delta(a)=B_\delta(a)$. 2) $\partial\left(\overline{B_\delta(a)}\right)=\partial B_\delta(a)=S_\delta(a)$.

$$
\partial E:=E\setminus\operatorname{Int}E
$$

Handwritten notes on the slide: next to the remark, "the difference of a closed and an open set"; next to the example, "1) $B_\delta(a)$ is an open set".

## Handwritten page (PDF p. 8) — The first part of the example: $\operatorname{Int}\overline{B_\delta(a)}=B_\delta(a)$

We have to prove that $\operatorname{Int}\overline{B_\delta(a)}=B_\delta(a)$. Recall the notation:

$$
B_\delta(a)=\{x\in\mathbb R^n:\ \|x-a\|<\delta\},
$$

$$
\overline{B_\delta(a)}=\{x\in\mathbb R^n:\ \|x-a\|\le\delta\},
$$

$$
S_\delta(a)=\{x\in\mathbb R^n:\ \|x-a\|=\delta\}.
$$

The set $B_\delta(a)$ is open, therefore $B_\delta(a)\subset\operatorname{Int}\overline{B_\delta(a)}$. Let us check the reverse inclusion. Since $\overline{B_\delta(a)}\setminus B_\delta(a)=S_\delta(a)$, it is enough to show that no point of the sphere $S_\delta(a)$ is interior for $\overline{B_\delta(a)}$.

$$
B_\delta(a)\subset\operatorname{Int}\overline{B_\delta(a)}
$$

## Handwritten page (PDF p. 9) — Points of the sphere are not interior

Let $x\in S_\delta(a)$; put

$$
x^k=a+\left(1+\frac1k\right)(x-a),\qquad k\in\mathbb N.
$$

Then $\forall k\in\mathbb N$ the point $x^k\notin\overline{B_\delta(a)}$, because

$$
\|x^k-a\|=\left(1+\frac1k\right)\|x-a\|=\left(1+\frac1k\right)\delta>\delta,
$$

since $x\in S_\delta(a)\Rightarrow\|x-a\|=\delta$. Furthermore, $\lim_{k\to\infty}x^k=x$, so every neighbourhood of the point $x$ contains points of $\{x^k\}$, that is, $x\notin\operatorname{Int}\overline{B_\delta(a)}$. Consequently,

$$
\operatorname{Int}\overline{B_\delta(a)}\subset B_\delta(a).
$$

![Points of the sphere are not interior (PDF p. 9)](../../assets/lectures-2025-26/lec57-58-p09-sphere-not-interior.jpg)

## Printed slide 6 (PDF p. 10) — Open and closed subsets

**Definition 5.3.5.** Let $E\subset\mathbb R^n$, $F\subset E$. 1) A point $a\in F$ is called interior for $F$ in $E$ if it has a neighbourhood $(V_\delta(a)\cap E)\subset F$. 2) A set $F$ is called open in $E$ if every one of its points is interior for $F$ in $E$. 3) A set $F$ is called closed in $E$ if its complement $E\setminus F$ is open in $E$.

**Theorem 5.3.4.** Let $F\subset E\subset\mathbb R^n$. Then the following statements are equivalent. 1) The set $F$ is open in $E$. 2) There is a set $G$ open in $\mathbb R^n$ for which $F=E\cap G$.

$$
\left(V_\delta(a)\cap E\right)\subset F
$$

$$
F=E\cap G
$$

## Handwritten page (PDF p. 11) — Proof of Theorem 5.3.4: 1) ⇒ 2)

Let $F$ be open in $E$. Then $\forall a\in F$ the point $a$ is interior for $F$ in $E$, that is,

$$
\exists\delta_a>0:\ \left(V_{\delta_a}(a)\cap E\right)\subset F.
$$

Put

$$
G=\bigcup_{a\in F}V_{\delta_a}(a).
$$

The set $G$ is open in $\mathbb R^n$ as a union of open balls. Further,

$$
G\cap E=\bigcup_{a\in F}\left(V_{\delta_a}(a)\cap E\right)\subset F,
$$

and the inclusion $F\subset G\cap E$ is obvious, since $F\subset G$ and $F\subset E$. Consequently $F=E\cap G$ — more precisely, $F=G\cap E$.

$$
G\cap E=\bigcup_{a\in F}\left(V_{\delta_a}(a)\cap E\right)\subset F
$$

## Handwritten page (PDF p. 12) — Proof of Theorem 5.3.4: 2) ⇒ 1)

Let $F=E\cap G$, where $G$ is open in $\mathbb R^n$. We check that $F$ is open in $E$. Let $a\in F=E\cap G$; since $G$ is open, $\exists\delta>0$: $V_\delta(a)\subset G$. Then

$$
V_\delta(a)\cap E\subset G\cap E=F,
$$

that is, $a$ is an interior point for $F$ in $E$. Hence $F$ is open in $E$.

$$
V_\delta(a)\cap E\subset G\cap E=F
$$

## Printed slide 7 (PDF p. 13) — Remarks on Theorem 5.3.4

1) Let $F\subset E\subset\mathbb R^n$. If $E$ is open in $\mathbb R^n$, then by Theorems 5.3.2 and 5.3.4 the openness of $F$ in $E$ is equivalent to its openness in $\mathbb R^n$. For an arbitrary $E$ this is no longer so: for example, the set $(0,1)\cap\mathbb Q$ is open in $\mathbb Q$ but not in $\mathbb R$. 2) A statement analogous to Theorem 5.3.4 holds for sets closed in $E$ as well.

$$
(0,1)\cap\mathbb Q
$$

## Printed slide 8 (PDF p. 14) — Covers of a set and compactness

**Definition 5.3.6.** Let $E\subset\mathbb R^n$. 1) If $\Omega$ is a family of subsets of $\mathbb R^n$ such that $\bigcup_{A\in\Omega}A\supset E$, one says that $\Omega$ is a cover of $E$ (or that $\Omega$ covers $E$). 2) Let $\tilde\Omega$ be a subfamily of $\Omega$ that also covers $E$. Then $\tilde\Omega$ is called a subcover of $\Omega$.

**Definition 5.3.7.** A set $E\subset\mathbb R^n$ is called compact if from every open cover of $E$ one can select a finite subcover.

![Definitions of a cover and of compactness (PDF p. 14)](../../assets/lectures-2025-26/lec57-58-p14-compact-cover.jpg)

$$
\bigcup_{A\in\Omega}A\supset E
$$

## Printed slide 9 (PDF p. 15) — Remarks on compact sets

1) If a set $E\subset\mathbb R^n$ is compact, then every closed subset of $E$ is compact as well. 2) Every closed cube $K\subset\mathbb R^n$ is compact.

## Handwritten page (PDF p. 16) — Proof of remark 1

Let $F$ be a closed subset of a compact set $E$, and let $\Omega$ be an open cover of $F$. We show that a finite subcover can be selected from $\Omega$. The family

$$
\Omega\cup\left\{\mathbb R^n\setminus F\right\}
$$

is an open cover of the compact set $E$: the sets of $\Omega$ and the set $\mathbb R^n\setminus F$ are open, and the points of $E\setminus F$ are covered by the latter. Select from this cover a finite subfamily $\tilde\Omega$ covering $E$ — this can be done since $E$ is compact. If $\mathbb R^n\setminus F$ belongs to $\tilde\Omega$, delete it; the remaining sets cover $F$. Thus a finite subcover of $F$ has been selected from $\Omega$, that is, $F$ is compact.

$$
\Omega\cup\left\{\mathbb R^n\setminus F\right\},\qquad \tilde\Omega
$$

> **Discrepancy in the handwritten notes.** In the first line the added set is written correctly as $\mathbb R^n\setminus F$, while when the finite subfamily is selected it appears as $\Omega\cup\left\{\mathbb R^n\setminus E\right\}$. The second spelling is wrong: the complement $\mathbb R^n\setminus E$ does not cover $E$ and does not help to apply the compactness of $E$; below, $\mathbb R^n\setminus F$ is used. The discrepancy is noted but not corrected in the transcribed handwritten text.

![Proof that a closed subset of a compact set is compact (PDF p. 16)](../../assets/lectures-2025-26/lec57-58-p16-closed-subset-compact.jpg)

## Printed slide 10 (PDF p. 17) — Criterion of compactness in $\mathbb R^n$

**Theorem 5.3.5.** Let $E\subset\mathbb R^n$. Then the following statements are equivalent. 1) $E$ is compact. 2) $E$ is closed and bounded. 3) From every sequence of elements of $E$ one can select a convergent subsequence whose limit also lies in $E$.

**Remark.** The implication 2) ⇒ 1) is usually called the Heine–Borel theorem.

## Handwritten page (PDF p. 18) — Proof of Theorem 5.3.5: 1) ⇒ 3)

The scheme of the proof is 1) ⇒ 3) ⇒ 2) ⇒ 1). Let $E$ be compact, and let $\{x^k\}_{k=1}^{\infty}$ be a sequence in $E$. Then, by the Bolzano–Weierstrass selection principle, $\exists\{x^{k_\ell}\}$ such that $x^{k_\ell}\to a$ and $a\in\mathbb R^n$. We check that $a\in E$. Suppose $a\notin E$; consider the family

$$
\Omega=\left\{\mathbb R^n\setminus\overline{V_\varepsilon(a)}\right\}_{\varepsilon>0},
$$

consisting of open sets. By de Morgan's law,

$$
\bigcup_{A\in\Omega}A=\mathbb R^n\setminus\bigcap_{\varepsilon>0}\overline{V_\varepsilon(a)}=\mathbb R^n\setminus\{a\}\supset E,
$$

therefore $\Omega$ is an open cover of $E$.

$$
\bigcup_{A\in\Omega}A=\mathbb R^n\setminus\bigcap_{\varepsilon>0}\overline{V_\varepsilon(a)}=\mathbb R^n\setminus\{a\}\supset E
$$

## Handwritten page (PDF p. 19) — End of 1) ⇒ 3): contradiction with compactness

Thus $\Omega$ covers $E$. Now let $\tilde\Omega$ be an arbitrary finite subfamily of $\Omega$. Then $\exists m\in\mathbb N$ and $\varepsilon_1,\ldots,\varepsilon_m>0$ such that

$$
\tilde\Omega=\left\{\mathbb R^n\setminus\overline{V_{\varepsilon_k}(a)}\right\}_{k=1}^{m},
$$

consequently

$$
V(a):=\bigcap_{k=1}^{m}V_{\varepsilon_k}(a)
$$

is a neighbourhood of the point $a$. Note that

$$
\bigcup_{A\in\tilde\Omega}A=\mathbb R^n\setminus\bigcap_{k=1}^{m}\overline{V_{\varepsilon_k}(a)}\subset\mathbb R^n\setminus V(a).
$$

But $x^{k_\ell}\to a$, that is, for sufficiently large $\ell$ we have $x^{k_\ell}\in E\cap V(a)$. Hence $\tilde\Omega$ does not cover $E$, which contradicts the compactness of $E$. Consequently $a\in E$.

$$
\bigcup_{A\in\tilde\Omega}A=\mathbb R^n\setminus\bigcap_{k=1}^{m}\overline{V_{\varepsilon_k}(a)}\subset\mathbb R^n\setminus V(a)
$$

## Handwritten page (PDF p. 20) — Proof of Theorem 5.3.5: 3) ⇒ 2)

We check that $E$ is closed. Let $\{x^k\}$ be a sequence, $x^k\in E$, $x^k\to a\in\mathbb R^n$. By condition 3) $\exists\{x^{k_\ell}\}$ such that $x^{k_\ell}\to b$, $b\in E$. But since $\{x^{k_\ell}\}$ is a subsequence of $\{x^k\}$, we have $a=b\in E$; hence $E$ is closed.

We check that $E$ is bounded. Suppose $E$ is unbounded; then $\forall k\in\mathbb N$ $\exists x^k\in E$: $\|x^k\|\ge k$. The sequence $\{x^k\}$ is such that $x^k\to\infty$. But then for every subsequence $\{x^{k_\ell}\}$ we have $x^{k_\ell}\to\infty$, which contradicts condition 3). Consequently $E$ is bounded.

**Editorial clarification.** In the handwritten notes both arrows leading to a contradiction are marked with $\not\Rightarrow$; in the text they are rendered in words as "which contradicts".

## Handwritten page (PDF p. 21) — Proof of Theorem 5.3.5: 2) ⇒ 1)

Let $E$ be closed and bounded in $\mathbb R^n$. From boundedness it follows that $\exists c>0$:

$$
E\subset[-c,c]\times[-c,c]\times\ldots\times[-c,c]=[-c,c]^n,
$$

that is, $E$ lies in a closed cube in $\mathbb R^n$. The cube $[-c,c]^n$ is compact in $\mathbb R^n$, and $E$ is a closed subset of $[-c,c]^n$; by remark 1 the set $E$ is compact.

$$
E\subset[-c,c]\times[-c,c]\times\ldots\times[-c,c]=[-c,c]^n
$$

> **Editorial note.** In the handwritten notes the inclusion is written with an equality sign: "$E=[-c,c]^n$". For an arbitrary bounded $E$ this is false; the meaning of the line is the inclusion $E\subset[-c,c]^n$, which is what the proof uses. The handwritten equality is reported here as a discrepancy and is not reproduced in the formulas.

## Printed slide 11 (PDF p. 22) — §4. The limit of a map of several variables

Maps of the form

$$
f:E\subset\mathbb R^n\to\mathbb R^m,\qquad m,n\in\mathbb N.
$$

are considered. Such maps are called maps of several variables. If $m=1$, then $f$ is called a function of several variables. If $n=1$, then $f$ is called a vector function.

Handwritten notes: $f:E\subset\mathbb R^n\to\mathbb R$ and $f:E\subset\mathbb R^n\to\mathbb R^m$.

$$
f:E\subset\mathbb R^n\to\mathbb R^m,\qquad m,n\in\mathbb N
$$

## Printed slide 12 (PDF p. 23) — The limit of a map in the Cauchy sense

**Definition 5.4.1.** Let $E\subset\mathbb R^n$, $f:E\to\mathbb R^m$, let the point $a\in\mathbb R^n$ be a limit point of $E$, and let $A\in\mathbb R^m$. One says that $\lim_{x\to a}f(x)=A$ (or $f(x)\to A$ as $x\to a$) in the Cauchy sense if

$$
\forall\varepsilon>0\ \ \exists\delta>0\ \ \forall x\in\dot B_\delta(a)\cap E:\ \ f(x)\in B_\varepsilon(A).
$$

**Remark.** If $a\in\mathbb R^n$ and $A\in\mathbb R^m$, then the relation $\lim_{x\to a}f(x)=A$ means that

$$
\forall\varepsilon>0\ \ \exists\delta>0\ \ \forall x\in E:\ \ 0<\|x-a\|<\delta\ \Rightarrow\ \|f(x)-A\|<\varepsilon,
$$

while for $a=\infty$ and $A=\infty$ it is equivalent to

$$
\forall\varepsilon>0\ \ \exists\delta>0\ \ \forall x\in E:\ \ \|x\|>\delta\ \Rightarrow\ \|f(x)\|>\varepsilon.
$$

> **Typo in the source.** In the main definition the slide prints $f(x)\in B_\varepsilon(a)$, although the image is the point $A\in\mathbb R^m$; according to the page image and the meaning it must be $f(x)\in B_\varepsilon(A)$. The exposition uses $B_\varepsilon(A)$, and the typo is recorded here.

## Printed slide 13 (PDF p. 24) — The limit of a map in the Heine sense

**Definition 5.4.2.** Let $E\subset\mathbb R^n$, $f:E\to\mathbb R^m$, let the point $a\in\mathbb R^n$ be a limit point of $E$, and let $A\in\mathbb R^m$. One says that $\lim_{x\to a}f(x)=A$ (or $f(x)\to A$ as $x\to a$) in the Heine sense if for every sequence $\{x^k\}_{k=1}^{\infty}\subset E\setminus\{a\}$ tending to $a$ the condition

$$
\lim_{k\to\infty}f(x^k)=A.
$$

holds.

## Printed slide 14 (PDF p. 25) — Equivalence of the two definitions of the limit

**Theorem 5.4.1.** Let $E\subset\mathbb R^n$, $f:E\to\mathbb R^m$, let the point $a\in\mathbb R^n$ be a limit point of $E$, and let $A\in\mathbb R^m$. Then the following statements are equivalent. 1) $\lim_{x\to a}f(x)=A$ in the Cauchy sense. 2) $\lim_{x\to a}f(x)=A$ in the Heine sense.

## Handwritten page (PDF p. 26) — Proof of Theorem 5.4.1: 1) ⇒ 2)

Let $\lim_{x\to a}f(x)=A$ in the Cauchy sense. Take $\{x^k\}_{k=1}^{\infty}$ in $E\setminus\{a\}$ tending to $a$. We show that $f(x^k)\to A$ as $k\to\infty$.

By 1) we have statement ❋:

$$
\forall\varepsilon>0\ \ \exists\delta>0:\ \ \forall x\in\dot V_\delta(a)\cap E\ \ f(x)\in V_\varepsilon(A).
$$

Since $x^k\to a$, $\exists N\in\mathbb N$ such that $\forall k>N$

$$
x^k\in V_\delta(a).
$$

Besides, $x^k\in E\setminus\{a\}$. Thus

$$
\left.\begin{aligned} x^k&\in V_\delta(a)\\ x^k&\in E\setminus\{a\}\end{aligned}\right\}\Longrightarrow x^k\in\dot V_\delta(a)\cap E.
$$

![Proof of the equivalence of the definitions of the limit (PDF p. 26)](../../assets/lectures-2025-26/lec57-58-p26-cauchy-heine-proof.jpg)

## Handwritten page (PDF p. 27) — End of 1) ⇒ 2) and start of 2) ⇒ 1)

Therefore, by ❋,

$$
f(x^k)\in V_\varepsilon(A)\qquad\forall k>N.
$$

Thus $f(x^k)\to A$ as $k\to\infty$, that is, $\lim_{x\to a}f(x)=A$ in the Heine sense as well.

Now let $\lim_{x\to a}f(x)=A$ in the Heine sense. We prove that the Cauchy limit of $f$ also exists and equals $A$. Suppose the contrary, that is, statement ❋❋:

$$
\exists\varepsilon>0\ \ \forall\delta>0\ \ \exists x\in\dot V_\delta(a)\cap E:\ \ f(x)\notin V_\varepsilon(A).
$$

Put

$$
F:=\{x\in E\setminus\{a\}:\ f(x)\notin V_\varepsilon(A)\}.
$$

Condition ❋❋ means that $\dot V_\delta(a)\cap F\ne\varnothing$ for $\forall\delta>0$, that is, $a$ is a limit point of $F$.

$$
F:=\{x\in E\setminus\{a\}:\ f(x)\notin V_\varepsilon(A)\}
$$

## Handwritten page (PDF p. 28) — End of 2) ⇒ 1)

By Theorem 5.2.6 $\exists\{x^k\}_{k=1}^{\infty}\subset F$ (and hence in $E\setminus\{a\}$) tending to $a$. Then, by Definition 5.4.2,

$$
\lim_{k\to\infty}f(x^k)=A,
$$

which is impossible, since $f(x^k)\notin V_\varepsilon(A)$ for $\forall k\in\mathbb N$. The contradiction obtained completes the proof.

$$
\lim_{k\to\infty}f(x^k)=A,\qquad f(x^k)\notin V_\varepsilon(A)
$$

## Printed slide 15 (PDF p. 29) — Uniqueness of the limit; the limit and coordinatewise limits

**Corollary.** If $A,B\in\mathbb R^m$, $f(x)\to A$ and $f(x)\to B$ as $x\to a$, then $A=B$.

**Corollary.** Let $A\in\mathbb R^m$ under the assumptions of Theorem 5.4.1. Then the following statements are equivalent. 1) $\lim_{x\to a}f(x)=A$. 2) $\forall i\in\{1,\ldots,m\}$ the equality $\lim_{x\to a}f_i(x)=A_i$ holds.

## Handwritten page (PDF p. 30) — Proofs of the corollaries

**Corollary 1.** Let $\{x^k\}_{k=1}^{\infty}$ be a sequence in $E\setminus\{a\}$ such that $x^k\to a$ as $k\to\infty$. Then

$$
\left.\begin{aligned} \lim_{k\to\infty}f(x^k)&=A\\ \lim_{k\to\infty}f(x^k)&=B\end{aligned}\right\}\Longrightarrow A=B
$$

by the uniqueness of the limit of a sequence.

**Corollary 2.** Let $\{x^k\}_{k=1}^{\infty}$ be a sequence in $E\setminus\{a\}$ such that $x^k\to a$ as $k\to\infty$. For $f:E\subset\mathbb R^n\to\mathbb R^m$ we write the vector and its image by coordinates:

$$
x=\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix},\qquad f(x)=\begin{pmatrix}f_1(x)\\f_2(x)\\\vdots\\f_m(x)\end{pmatrix},\qquad A=\begin{pmatrix}A_1\\A_2\\\vdots\\A_m\end{pmatrix}.
$$

## Handwritten page (PDF p. 31) — End of corollary 2 and an example

Statement 1) means that $\lim_{k\to\infty}f(x^k)=A$; statement 2) means that $\lim_{k\to\infty}f_i(x^k)=A_i$. The equivalence follows from the definition and from the properties of limits of sequences in $\mathbb R^n$.

**Example.** Let

$$
f(x,y)=\frac{xy}{x^2+y^2},\qquad (x,y)\in\mathbb R^2\setminus\{(0,0)\}.
$$

The map $f$ has no limit at the point $(0,0)$. Indeed, put

$$
z^k=\left(\frac1k,0\right),\qquad \omega^k=\left(\frac1k,\frac1k\right),\qquad k\in\mathbb N.
$$

Then $z^k\to(0,0)$ and $\omega^k\to(0,0)$ as $k\to\infty$, but

$$
f(z^k)=0\to0,
$$

$$
f(\omega^k)=\frac{\frac1{k^2}}{\frac2{k^2}}=\frac12\to\frac12,
$$

that is, the limits along different sequences differ. In the figure to the right of the text two paths of approach to the origin are shown: the points $z^k$ lie on the axis $Ox$ (green), the points $\omega^k$ on the line $y=x$ (red).

![Counterexample: different limits along different paths (PDF p. 31)](../../assets/lectures-2025-26/lec57-58-p31-limit-counterexample.jpg)

## Printed slide 16 (PDF p. 32) — The limit and arithmetic operations

**Theorem 5.4.2.** Let $E\subset\mathbb R^n$, let $a\in\mathbb R^n$ be a limit point of $E$, and let $f,g:E\to\mathbb R^m$. Suppose that $f$, $g$ have limits $A$, $B\in\mathbb R^m$ at the point $a$ respectively. Then the following statements hold. 1) $\lim_{x\to a}(f(x)+g(x))=A+B$. 2) If $\lambda:E\to\mathbb R$, $\alpha\in\mathbb R$, $\lim_{x\to a}\lambda(x)=\alpha$, then $\lim_{x\to a}\lambda(x)f(x)=\alpha A$. 3) $\lim_{x\to a}f(x)\cdot g(x)=A\cdot B$. 4) If $m=1$ and $B\ne0$, then $\lim_{x\to a}\frac{f(x)}{g(x)}=\frac AB$.

$$
\lim_{x\to a}(f(x)+g(x))=A+B
$$

$$
\lim_{x\to a}\lambda(x)f(x)=\alpha A
$$

$$
\lim_{x\to a}f(x)\cdot g(x)=A\cdot B,\qquad \lim_{x\to a}\frac{f(x)}{g(x)}=\frac AB
$$

## Printed slide 17 (PDF p. 33) — The limit of a composition

**Theorem 5.4.3.** Let $E\subset\mathbb R^n$, $F\subset\mathbb R^m$, and let $a\in\mathbb R^n$ and $b\in F$ be limit points of $E$ and $F$ respectively. If $f:E\to F$, $g:F\to\mathbb R^s$, $\lim_{x\to a}f(x)=b$, $\lim_{x\to b}g(x)=g(b)$, then

$$
\lim_{x\to a}(g\circ f)(x)=g(b).
$$

## Handwritten page (PDF p. 34) — Proof of Theorem 5.4.3

Let $\varepsilon>0$. Then statement ▲ holds:

$$
\exists\delta>0\ \text{such that}\ g(y)\in V_\varepsilon(g(b))\ \ \forall y\in V_\delta(b)\cap F.
$$

Indeed, for $y\ne b$ this inclusion follows from the definition of the limit of $g$ ($\lim_{y\to b}g(y)=g(b)$), while for $y=b$ it is obvious. Let us now choose a $\delta>0$ such that

$$
f(x)\in V_\delta(b)\qquad\forall x\in\dot V_\delta(a)\cap E;
$$

this can be done since $\lim_{x\to a}f(x)=b$. Substituting $y=f(x)$ into ▲, we obtain

$$
g(f(x))\in V_\varepsilon(g(b))\qquad\forall x\in\dot V_\delta(a)\cap E.
$$

Thus

$$
\lim_{x\to a}(g\circ f)(x)=g(b).
$$

$$
g(f(x))\in V_\varepsilon(g(b))\qquad\forall x\in\dot V_\delta(a)\cap E
$$

> **Notation in the handwritten notes.** In the last display the same letter $\delta$ is used both for the neighbourhood of the argument and for the radius coming from the definition of the limit of $g$; this coincidence of letters is not commented on in the notes. The formula is given as written on the board.

## Printed slide 18 (PDF p. 35) — The Bolzano–Cauchy criterion for maps

**Theorem 5.4.4.** Let $E\subset\mathbb R^n$, let $a\in\mathbb R^n$ be a limit point of $E$, and let $f:E\to\mathbb R^m$. Then the following statements are equivalent. 1) The map $f$ has a limit in $\mathbb R^m$. 2) $\forall\varepsilon>0$ $\exists V(a)$: $\forall x,y\in\dot V(a)\cap E$ one has $\|f(x)-f(y)\|<\varepsilon$.

**Remark.** Statement 2) is called the Cauchy property of $f$ at the point $a$.

$$
\forall\varepsilon>0\ \ \exists V(a)\ \ \forall x,y\in\dot V(a)\cap E:\ \ \|f(x)-f(y)\|<\varepsilon
$$

## Handwritten page (PDF p. 36) — Proof of Theorem 5.4.4: 1) ⇒ 2) and start of 2) ⇒ 1)

Let $\lim_{x\to a}f(x)=A$. Then $\forall\varepsilon>0$ $\exists V(a)$ such that

$$
\|f(x)-A\|<\frac{\varepsilon}{2}\qquad\forall x\in\dot V(a)\cap E.
$$

Then for all $x,y\in\dot V(a)\cap E$

$$
\|f(x)-f(y)\|=\|f(x)-A+A-f(y)\|\le\|f(x)-A\|+\|f(y)-A\|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon.
$$

Conversely, let $\forall\varepsilon>0$ $\exists V(a)$ such that

$$
\forall x,y\in\dot V(a)\cap E\qquad\|f(x)-f(y)\|<\varepsilon.
$$

Let $\{x^k\}_{k=1}^{\infty}$ be a sequence in $E\setminus\{a\}$ such that $x^k\to a$ as $k\to\infty$. Then $\exists N\in\mathbb N$: $\forall k>N$ we have $x^k\in V(a)$ and $\|f(x^k)-f(x^m)\|<\varepsilon$ for all $k,m>N$.

$$
\|f(x)-f(y)\|=\|f(x)-A+A-f(y)\|\le\|f(x)-A\|+\|f(y)-A\|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon
$$

## Handwritten page (PDF p. 37) — End of the proof of Theorem 5.4.4

Hence the sequence $\{f(x^k)\}$ is a Cauchy sequence, therefore $\{f(x^k)\}$ has a limit in $\mathbb R^m$ and, consequently, the map $f$ has a limit at the point $a$.

$$
\{f(x^k)\}\ \text{is a Cauchy sequence}\ \Longrightarrow\ \{f(x^k)\}\ \text{has a limit in}\ \mathbb R^m
$$

---

[Lecture index](index.md) · [Русский](../../ru/lectures-2025-26/lecture-57-58.md) · [Español](../../es/lectures-2025-26/lecture-57-58.md) · [Previous: 55–56](lecture-55-56.md) · [Next: 59–60](lecture-59-60.md)
