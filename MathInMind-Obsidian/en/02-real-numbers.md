---
title: "The Real Numbers and Completeness"
lang: en
chapter: 2
part: "Foundations"
aliases: ["The Real Numbers and Completeness (en)"]
tags: [mathinmind/en, mathinmind/chapter]
---
# 2. The Real Numbers and Completeness

[[en/01-logic-sets-functions|← 1. Logic, Sets, and Functions]] · [[en/index|Course index]] · [[en/term-index|Terms & theorems]] · [[en/03-sequences|3. Sequences and Limits →]]

> [!abstract] Goal
> Understand the algebraic, order, and completeness properties that distinguish $\mathbb R$ from $\mathbb Q$.

## 2.1 Ordered-field properties

The real numbers form a field: addition and multiplication satisfy associativity, commutativity, distributivity, and have identities and inverses (except division by zero). The order $<$ is compatible with these operations:

$$
a<b\implies a+c<b+c,
$$
$$
a<b,\ c>0\implies ac<bc.
$$

Multiplication by a negative number reverses an inequality. The absolute value is

$$
|x|=\begin{cases}x,&x\ge0,\\-x,&x<0.\end{cases}
$$

For all $x,y\in\mathbb R$,

$$
|xy|=|x|\,|y|,\qquad |x+y|\le |x|+|y|,
$$

and the reverse triangle inequality is $\bigl||x|-|y|\bigr|\le |x-y|$. Geometrically, $|x-y|$ is distance.

## 2.2 Supremum and infimum

Let $A\subseteq\mathbb R$ be nonempty. A number $u$ is an **upper bound** if $a\le u$ for every $a\in A$. The **supremum** $\sup A$ is the least upper bound. The infimum is the greatest lower bound.

> [!axiom] Completeness axiom
> Every nonempty subset of $\mathbb R$ that is bounded above has a supremum in $\mathbb R$.

^completeness-axiom

Equivalently, every nonempty set bounded below has an infimum. A supremum need not belong to the set: $\sup(0,1)=1$, while a maximum must belong to the set.

A useful characterization is

$$
u=\sup A\iff
\begin{cases}
a\le u\quad(a\in A),\\
\forall\varepsilon>0\;\exists a\in A:a>u-\varepsilon.
\end{cases}
$$

The set $\{q\in\mathbb Q:q^2<2\}$ has no rational supremum, so $\mathbb Q$ is incomplete.

## 2.3 Consequences of completeness

> [!theorem] Archimedean property
> For every $x\in\mathbb R$ there is $n\in\mathbb N$ with $n>x$. Equivalently, for every $\varepsilon>0$ there is $n$ such that $1/n<\varepsilon$.

^archimedean-property

If $\mathbb N$ were [[#2.2 Supremum and infimum|bounded above]], its supremum $s$ would satisfy $s-1<n<s$ for some integer $n$, forcing $n+1>s$, a contradiction.

> [!theorem] Density of rationals
> If $a<b$, there exists $q\in\mathbb Q$ with $a<q<b$.

^density-of-rationals

Choose $n$ with $n(b-a)>1$ and an integer $m$ between $na$ and $nb$; then $q=m/n$ works. Irrationals are dense as well: $q+\sqrt2/k$ can be placed in any interval.

## 2.4 Nested intervals and the real line

A sequence of closed bounded intervals $I_n=[a_n,b_n]$ is **nested** if $I_{n+1}\subseteq I_n$.

> [!theorem] Nested-interval theorem
> If $I_n$ are nested closed bounded intervals, then $\bigcap_{n=1}^{\infty}I_n\ne\varnothing$. If $b_n-a_n\to0$, the intersection contains exactly one point.

^nested-interval-theorem

Indeed, $a=\sup\{a_n\}$ belongs to every interval. Closedness and boundedness are essential: $(0,1/n)$ have empty intersection, as do $[n,\infty)$.

The extended real line $\overline{\mathbb R}=\mathbb R\cup\{-\infty,+\infty\}$ is convenient for suprema of unbounded sets, but expressions such as $\infty-\infty$ remain undefined.

## Worked example

Let $A=\{1-1/n:n\in\mathbb N\}$. Every element is $<1$, and for any $\varepsilon>0$ the [[#^archimedean-property|Archimedean property]] gives $n$ with $1/n<\varepsilon$, hence $1-1/n>1-\varepsilon$. Therefore $\sup A=1$. Since $1\notin A$, there is no maximum.

## Common pitfalls

1. “Bounded” means bounded above and below.
2. $\sup A$ may lie outside $A$; $\max A$ cannot.
3. The [[#^nested-interval-theorem|nested-interval theorem]] requires closed bounded intervals in $\mathbb R$.

## Exercises

1. Prove $\sup(A+B)=\sup A+\sup B$ for nonempty bounded sets, where $A+B=\{a+b:a\in A,b\in B\}$.
2. Show that between any two real numbers there is an irrational number.
3. Find $\sup\{x\in\mathbb R:x^2+x<2\}$ and decide whether it is a maximum.

> [!answer]- Short answers
> 1. The sum is an upper bound; approximate both suprema within $\varepsilon/2$.
> 2. Choose a rational $q$ near the target and a sufficiently large $k$, then use $q+\sqrt2/k$.
> 3. The set is $(-2,1)$; the supremum is $1$, not a maximum.

---

[[en/01-logic-sets-functions|← 1. Logic, Sets, and Functions]] · [[en/index|Course index]] · [[en/term-index|Terms & theorems]] · [[en/03-sequences|3. Sequences and Limits →]]
