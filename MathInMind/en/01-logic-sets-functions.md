---
title: "Logic, Sets, and Functions"
lang: en
chapter: 1
part: "Foundations"
---
# 1. Logic, Sets, and Functions

[Course index](index.md) · [Next: Real numbers](02-real-numbers.md)

> **Goal.** Read quantified statements, construct basic proofs, and use sets and functions precisely.

## 1.1 Propositions and quantifiers

A **proposition** has a definite truth value. For propositions $P,Q$, the connectives $\neg P$, $P\land Q$, $P\lor Q$, and $P\implies Q$ mean negation, conjunction, disjunction, and implication. The implication is false only when $P$ is true and $Q$ is false.

The quantifiers are

$$
\forall x\in A\;P(x),\qquad \exists x\in A\;P(x).
$$

Their negations interchange quantifiers:

$$
\neg(\forall x\in A\;P(x))\iff \exists x\in A\;\neg P(x),
$$
$$
\neg(\exists x\in A\;P(x))\iff \forall x\in A\;\neg P(x).
$$

Quantifier order matters. $\forall x\,\exists y\,P(x,y)$ allows $y$ to depend on $x$; $\exists y\,\forall x\,P(x,y)$ requires one $y$ to work for every $x$.

## 1.2 Proof patterns

- **Direct proof:** assume $P$ and derive $Q$.
- **Contrapositive:** to prove $P\implies Q$, prove $\neg Q\implies\neg P$.
- **Contradiction:** assume the negation of the desired statement and derive an impossibility.
- **Induction:** prove $P(1)$ and $P(n)\implies P(n+1)$; then $P(n)$ holds for every positive integer $n$. Strong induction assumes all earlier cases.
- **Existence and uniqueness:** construct an object, then show that any two such objects coincide.

> **Example — induction.** For $n\ge1$, $1+2+\cdots+n=n(n+1)/2$. The base case is immediate. If the formula holds for $n$, adding $n+1$ gives
> $$
> \frac{n(n+1)}2+(n+1)=\frac{(n+1)(n+2)}2.
> $$

## 1.3 Sets

A set is determined by its elements. Standard operations are union $A\cup B$, intersection $A\cap B$, difference $A\setminus B$, and complement $A^c$ relative to a fixed universe. De Morgan's laws state

$$
(A\cup B)^c=A^c\cap B^c,\qquad (A\cap B)^c=A^c\cup B^c.
$$

The Cartesian product $A\times B$ consists of ordered pairs $(a,b)$. A relation on $A$ is a subset of $A\times A$. An equivalence relation is reflexive, symmetric, and transitive; it partitions $A$ into equivalence classes.

For an indexed family,

$$
x\in\bigcup_{i\in I}A_i\iff \exists i\in I:x\in A_i,
\qquad
x\in\bigcap_{i\in I}A_i\iff \forall i\in I:x\in A_i.
$$

## 1.4 Functions

A function $f:A\to B$ assigns exactly one output $f(x)\in B$ to each $x\in A$. Here $A$ is the domain and $B$ the codomain; the range is $f(A)=\{f(x):x\in A\}$.

- $f$ is **injective** if $f(x_1)=f(x_2)\implies x_1=x_2$.
- $f$ is **surjective** if $f(A)=B$.
- $f$ is **bijective** if it is both; then $f^{-1}:B\to A$ exists.

For $X\subseteq A$ and $Y\subseteq B$,

$$
f(X)=\{f(x):x\in X\},\qquad f^{-1}(Y)=\{x\in A:f(x)\in Y\}.
$$

The inverse-image notation does not require an inverse function. Preimages preserve unions, intersections, and complements; images preserve unions but generally not intersections.

If $g\circ f$ is injective, then $f$ is injective. If $g\circ f$ is surjective, then $g$ is surjective. These short conclusions are useful in later proofs.

## 1.5 Countability

Sets $A,B$ have the same cardinality if a bijection $A\to B$ exists. A set is **countable** if it is finite or has the cardinality of $\mathbb N$. Thus $\mathbb Z$ and $\mathbb Q$ are countable. Cantor's diagonal argument shows that $\mathbb R$ and the set of infinite binary sequences are uncountable.

> **Cantor's theorem.** There is no surjection from $A$ onto its power set $\mathcal P(A)$. If $f:A\to\mathcal P(A)$, the set $D=\{x\in A:x\notin f(x)\}$ is not in the range of $f$: assuming $D=f(a)$ leads to $a\in D\iff a\notin D$.

## Worked example

Let $f:\mathbb R\to\mathbb R$, $f(x)=2x+3$. To solve $f(x)=y$, take $x=(y-3)/2$. This unique solution proves bijectivity and gives $f^{-1}(y)=(y-3)/2$. In contrast, $x^2$ is neither injective nor surjective as a map $\mathbb R\to\mathbb R$, but is bijective as a map $[0,\infty)\to[0,\infty)$.

## Common pitfalls

1. Proving $P\implies Q$ does not prove $Q\implies P$.
2. To disprove a universal statement, one counterexample is enough; to prove it, checking examples is not enough.
3. The symbol $f^{-1}(Y)$ denotes a preimage even when $f$ is not bijective.

## Exercises

1. Negate: “For every $\varepsilon>0$ there exists $N$ such that $|a_n-a|<\varepsilon$ for all $n\ge N$.”
2. Prove that $f^{-1}(Y_1\cap Y_2)=f^{-1}(Y_1)\cap f^{-1}(Y_2)$.
3. Show that a countable union of countable sets is countable, assuming the axiom of choice for countable families.

<details>
<summary>Short answers</summary>

1. There is $\varepsilon_0>0$ such that for every $N$ there is $n\ge N$ with $|a_n-a|\ge\varepsilon_0$.
2. Both sides say exactly that $f(x)\in Y_1$ and $f(x)\in Y_2$.
3. List each set, arrange the lists in a two-dimensional array, and enumerate diagonally, omitting repetitions.
</details>

---

[Course index](index.md) · [Next: Real numbers](02-real-numbers.md)
