---
title: "Lecture 36 — Antiderivatives and the indefinite integral"
lang: en
course: "Mathematical Analysis, 2025/26"
lecture: 36
semester: 2
date: 2026-02-19
source: "ma25_26_lecture_36_notes.pdf"
pdf_pages: 20
typed_slides: 14
aliases: ["Lecture 36 (en)"]
tags: [mathinmind/en, mathinmind/lecture]
---
# Lecture 36 — Antiderivatives and the indefinite integral

[[en/lectures-2025-26/lecture-35|← Lecture 35]] · [[en/lectures-2025-26/index|Lecture index]] · [[en/lectures-2025-26/lecture-37-38|Lectures 37–38 →]] · [[en/term-index|Terms & theorems]] · [[ru/lectures-2025-26/lecture-36|Русский]] · [[es/lectures-2025-26/lecture-36|Español]]

> [!info] Source
> `ma25_26_lecture_36_notes.pdf` — 20 pages, 14 typed slides. Handwritten pages: 8, 10–12, 18–19; the diagram on typed PDF p. 4 is also transcribed. Date: 19 February 2026.
>
> **Semester 2: lectures 33–64; semester 1 ends with lecture 32. Starting at lecture 33, duplicate material exists** in the [[ru/lectures/index|Russian `ru/lectures/` folder]]. For this lecture, see [[ru/lectures/02-antiderivatives-4-1|§4.1 “Antiderivatives and the indefinite integral”]] and the [archived “Lecture 36”](https://github.com/NikiHunter/matan/blob/main/source/MathInMind/%D0%9C%D0%90%D0%A2%D0%90%D0%9D_%D0%9B/%D0%9B%D0%B5%D0%BA%D1%86%D0%B8%D1%8F%2036.md). This is a complete illustrated transcription of the new PDF, not a shortened reference to the older notes.
>
> **Notation.** $I=\langle A,B\rangle$ is an interval, and $\mathcal P_f(I)$ is the set of all [[#^def-4-1-1|antiderivatives]] of $f$ on it. At included endpoints, [[en/lectures-2025-26/lecture-22-23#^def-3-1-1|derivatives]] are one-sided, as in earlier lectures.

## Typed slides 1–3 (PDF pp. 1–3). Introduction

**Quote of the day:** “Tomorrow, today will become yesterday!”

**Aims:**

- Having studied differentiation, consider the inverse problem: the derivative is known and the function must be found.
- Define an antiderivative and describe all antiderivatives on an interval.
- Discuss operations on indefinite integrals.
- State necessary and sufficient conditions for the existence of antiderivatives.

## Chapter 4. Integral calculus of functions of one real variable

### Typed slide 4 (PDF p. 4). The inverse problem

Handwritten diagram: differentiation maps $f$ to $f'$, while the inverse problem is to recover $f$ from its derivative.

![PDF p. 4: differentiation and the inverse problem of recovering the function](../../assets/lectures-2025-26/lec36-p04-differentiation-integration.jpg)

## §1. Antiderivatives and the indefinite integral

### Typed slide 5 (PDF p. 5). An antiderivative on an interval

> [!definition] Definition 4.1.1
> Let $f:I\to\mathbb R$. A function $F:I\to\mathbb R$ is an **antiderivative** of $f$ on $I$ if
>
> 1. $F$ is [[en/lectures-2025-26/lecture-22-23#^def-3-2-1|differentiable]] on $I$;
> 2. $F'(x)=f(x)$ for every $x\in I$.

^def-4-1-1

Notation:

$$
\mathcal P_f(I)=\{F:I\to\mathbb R:\ F\text{ is differentiable on }I,\ F'=f\}.
$$

### Typed slide 6 (PDF p. 6). Three questions

1. For which $f$ is $\mathcal P_f(I)$ nonempty?
2. How can we describe $\mathcal P_f(I)$ when it is nonempty?
3. How can we compute antiderivatives when they exist?

Start with the second: on an interval, an antiderivative is unique up to an additive constant.

### Typed slide 7 (PDF p. 7). Describing all antiderivatives

> [!theorem] Theorem 4.1.1
> Let $f,F,G$ be defined on $I$, with $F\in\mathcal P_f(I)$. The following are equivalent:
>
> 1. $G\in\mathcal P_f(I)$.
> 2. There exists $c\in\mathbb R$ such that $G(x)=F(x)+c$ for all $x\in I$.

^thm-4-1-1

In other words,

$$
\mathcal P_f(I)=\{F+c:\ c\in\mathbb R\}.
$$

Thus it suffices to find one antiderivative.

### Handwritten page (PDF p. 8). Proof of Theorem 4.1.1

**$1\Rightarrow2$.** Put $H(x)=G(x)-F(x)$. Then

$$
H'(x)=G'(x)-F'(x)=f(x)-f(x)=0\qquad(x\in I).
$$

By the criterion for a function to be constant, $H$ is constant on the interval $I$, so $G=F+c$.

**$2\Rightarrow1$.** If $G=F+c$, both functions on the right are differentiable, so $G$ is differentiable and

$$
G'(x)=F'(x)+0=f(x)\qquad(x\in I).
$$

Hence $G\in\mathcal P_f(I)$. $\blacksquare$

### Typed slide 8 (PDF p. 9). The indefinite integral

> [!definition] Definition 4.1.2
> Let $f:I\to\mathbb R$, $F\in\mathcal P_f(I)$. The set of functions
>
> $$
> \{F(x)+c:\ c\in\mathbb R\}
> $$

^def-4-1-2

is the **indefinite integral** of $f$ on $I$, denoted by

$$
\int f(x)\,dx.
$$

It is simply $\mathcal P_f(I)$ expressed using one chosen antiderivative.

> [!note] Editorial correction
> The slide's hypothesis after $f:I\to\mathbb R$ omits $F\in$ before $\mathcal P_f(I)$. The choice of an antiderivative $F$ is restored because it is used in the next line.

### Handwritten pages (PDF pp. 10–12). Meaning of the notation

For brevity, one writes

$$
\int f(x)\,dx=F(x)+c,
$$

omitting the braces and taking $c$ to be an arbitrary real number. This is a **family of functions**, not one function with a preselected constant.

The notation is analogous to that for the [[en/lectures-2025-26/lecture-39-40#^def-4-2-6|definite integral]]. Page 10 gives the informal picture

$$
\text{definite integral}\ \sim\
\lim_{\Delta x_k\to0}\sum_k f(x_k)\Delta x_k.
$$

On p. 11, $f(x)\,dx$ is matched with $f(x_k)\Delta x_k$, and $\int$ with an elongated letter $S$ (summation).

> [!remark] Editor's note
> This is an intuitive motivation, not a definition of the limit of [[en/lectures-2025-26/lecture-37-38#^def-4-2-4|integral sums]]: [[en/lectures-2025-26/lecture-37-38#^def-4-2-2|partitions]], tags and mesh are introduced in [[en/lectures-2025-26/lecture-37-38|lectures 37–38]].

In principle, the indefinite integral could be denoted simply by $\int f$, but writing $dx$ is useful:

1. It specifies the variable of integration. In the example on p. 11:

$$
\int x^y\,dx:\quad x\mapsto x^y,\quad y\text{ is a parameter};
$$

$$
\int x^y\,dy:\quad y\mapsto x^y,\quad x\text{ is a parameter}.
$$

2. Interpreting $dx$ as a [[en/lectures-2025-26/lecture-24-25-26#^def-3-3-1|differential]] makes integration rules convenient to formulate (p. 12).

### Typed slides 9–10 (PDF pp. 13–14). Differentiating an integral

An indefinite integral is a **set of functions**, but some operations on functions extend to these sets.

Suppose $f$ has an antiderivative on $I$. Every member of the family has the same derivative, so we agree to write

$$
\left(\int f(x)\,dx\right)'=f(x),\qquad x\in I.
$$

### Typed slide 11 (PDF p. 15). Arithmetic of sets of functions

Let $D,E$ be sets of functions on $I$, let $h:I\to\mathbb R$, and fix $\lambda\in\mathbb R$. Define

$$
D+E=\{f+g:\ f\in D,\ g\in E\},
$$

$$
E+h=\{g+h:\ g\in E\},\qquad
\lambda E=\{\lambda g:\ g\in E\}.
$$

> [!remark] Editor's note
> The slide's last formula puts $\lambda\in\mathbb R$ inside the set. When multiplying by a **fixed** scalar $\lambda$, only $g\in E$ varies, not all possible multipliers $\lambda$.

### Typed slide 12 (PDF p. 16). Operations on indefinite integrals

Let $F,G$ be antiderivatives of $f,g$ on $I$, and let $H:I\to\mathbb R$. Then

$$
\int f(x)\,dx+\int g(x)\,dx
=\{F(x)+G(x)+c:\ c\in\mathbb R\},
$$

$$
\int f(x)\,dx+H(x)
=\{F(x)+H(x)+c:\ c\in\mathbb R\},
$$

$$
\lambda\int f(x)\,dx
=\{\lambda F(x)+c:\ c\in\mathbb R\},\qquad\lambda\ne0.
$$

> [!remark] Editorial explanation
> The restriction $\lambda\ne0$ matters for equality of **sets**: $0\cdot\mathcal P_f(I)=\{0\}$, whereas the antiderivatives of the zero function are all constant functions. In the second formula, $H$ is arbitrary: the assertion is equality of sets of sums, not differentiability of $H$.

### Typed slide 13 (PDF p. 17). Necessary conditions for existence

Completely describing functions that have antiderivatives is difficult; necessary and sufficient conditions are considered separately. **Continuity is not a necessary condition.**

### Handwritten page (PDF p. 18). A consequence of Darboux's theorem

If $f$ has an antiderivative $F$, then $f=F'$. Thus $f$ has the [[en/lectures-2025-26/lecture-31-32#^thm-3-7-6|Darboux property]]: the image of every interval in its domain is an interval. In particular, it cannot have jumps; [[en/lectures-2025-26/lecture-16#^def-2-5-4|discontinuities of the second kind]] may occur.

> [!remark] Editorial explanation
> The Darboux property must not be replaced merely by the absence of jumps: having no jump alone does not guarantee an antiderivative. The argument about derivatives appears in [[en/lectures-2025-26/lecture-31-32|lectures 31–32]].

### Handwritten page (PDF p. 19). A function without an antiderivative

$$
f(x)=
\begin{cases}
1,&x\ge0,\\
-1,&x<0.
\end{cases}
$$

At zero, $f$ has a jump — a discontinuity of the first kind. Hence it has **no antiderivative on an interval containing zero as an interior point**.

![PDF p. 19: the jump from −1 to 1, with a filled point at x=0 on the upper ray](../../assets/lectures-2025-26/lec36-p19-jump-no-antiderivative.jpg)

Discontinuities of the second kind are allowed for derivatives, so continuity is not necessary.

> [!example] Editorial example for the last statement
> Lectures 31–32 construct a differentiable function $u(x)=x^2(2+\sin(1/x))$ for $x\ne0$, $u(0)=0$. Its derivative is discontinuous at zero but has the antiderivative $u$. This exemplifies an allowable oscillatory discontinuity; it does not assert that every function with a discontinuity of the second kind has an antiderivative.

### Typed slide 14 (PDF p. 20). A sufficient condition for existence

> [!theorem] Theorem 4.1.2
> If $f$ is continuous on $I$, then it has an antiderivative on $I$.

^thm-4-1-2

The PDF states the theorem without proof. Its connection with an integral with variable [[en/lectures-2025-26/lecture-13#Definition 2.3.9 (upper and lower limits)|upper limit]] is treated when studying the definite integral; see also the [[en/08-riemann-integration|general chapter on Riemann integration]].

## Lecture structure

```mermaid
flowchart TD
    A["4.1.1: definition of an antiderivative"] --> B["4.1.1: all antiderivatives differ by a constant"]
    B --> C["4.1.2: the indefinite integral as a family"]
    C --> D["Differentiation and arithmetic of families"]
    A --> E["Necessary: Darboux property, no jumps"]
    A --> F["4.1.2: continuity is sufficient"]
    E --> G["Continuity is not necessary"]
```

---

Previous: [[en/lectures-2025-26/lecture-35|lecture 35]] · Next: [[en/lectures-2025-26/lecture-37-38|lectures 37–38]] · Duplicate section: [[ru/lectures/02-antiderivatives-4-1|§4.1 in `ru/lectures/`]].
