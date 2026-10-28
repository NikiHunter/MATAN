---
title: "Sequences and Limits"
lang: en
chapter: 3
part: "Foundations"
aliases: ["Sequences and Limits (en)"]
tags: [mathinmind/en, mathinmind/chapter]
---
# 3. Sequences and Limits

[[en/02-real-numbers|← 2. The Real Numbers and Completeness]] · [[en/index|Course index]] · [[en/term-index|Terms & theorems]] · [[en/04-numeric-series|4. Numerical Series →]]

> [!abstract] Goal
> Prove convergence, use completeness through monotone and Cauchy criteria, and control [[#3.4 Subsequences and Cauchy sequences|subsequences]].

## 3.1 The definition of a limit

A sequence is a function $a:\mathbb N\to\mathbb R$, written $(a_n)$. It converges to $L$ if

$$
\forall\varepsilon>0\;\exists N\in\mathbb N\;\forall n\ge N:
|a_n-L|<\varepsilon.
$$

We write $a_n\to L$. The chosen $N$ may depend on $\varepsilon$, but not on $n$. A sequence diverges if it has no finite limit.

To prove $1/n\to0$, choose $N>1/\varepsilon$. To prove $(2n+1)/(n+3)\to2$, estimate

$$
\left|\frac{2n+1}{n+3}-2\right|=\frac5{n+3}<\frac5n.
$$

A convergent sequence has a unique limit and is bounded. If $a_n\to L$, every subsequence also converges to $L$.

## 3.2 Limit laws

If $a_n\to a$, $b_n\to b$, then

$$
a_n\pm b_n\to a\pm b,\qquad a_nb_n\to ab,
$$

and $a_n/b_n\to a/b$ when $b\ne0$ and $b_n\ne0$ eventually. If $a_n\le c_n\le b_n$ and both outer sequences tend to $L$, then $c_n\to L$ (the squeeze theorem).

If $a_n\ge0$ eventually and $a_n\to a$, then $a\ge0$. Strict inequalities need not survive: $1/n>0$ but its limit is zero.

We write $a_n\to+\infty$ if for every $M$ there is $N$ such that $a_n>M$ for all $n\ge N$. This is a special form of divergence, not convergence in $\mathbb R$.

## 3.3 Monotone convergence

> [!theorem] Monotone convergence theorem
> Every increasing sequence [[en/02-real-numbers#2.2 Supremum and infimum|bounded above]] converges to its supremum; every decreasing sequence bounded below converges to its infimum.

^monotone-convergence-theorem

For an increasing bounded sequence, let $L=\sup\{a_n\}$. Given $\varepsilon>0$, some $a_N>L-\varepsilon$; monotonicity makes all later terms lie in $(L-\varepsilon,L]$.

For a recursive sequence, first prove boundedness and monotonicity by [[en/01-logic-sets-functions#^example-induction|induction]], then pass to the limit. For example, $a_1=1$, $a_{n+1}=\sqrt{2+a_n}$ is increasing and bounded above by $2$, so its limit $L$ satisfies $L=\sqrt{2+L}$, giving $L=2$.

## 3.4 Subsequences and Cauchy sequences

> [!theorem] Bolzano–Weierstrass theorem
> Every bounded sequence in $\mathbb R$ has a convergent subsequence.

^bolzano-weierstrass-theorem

A sequence is **Cauchy** if

$$
\forall\varepsilon>0\;\exists N\;\forall m,n\ge N:|a_n-a_m|<\varepsilon.
$$

[[#3.1 The definition of a limit|Convergent sequences]] are Cauchy. Conversely, a Cauchy sequence is bounded, hence has a convergent subsequence; the Cauchy condition then forces the whole sequence to the same limit. Thus

$$
(a_n)\text{ converges}\iff(a_n)\text{ is Cauchy}.
$$

This criterion proves convergence without knowing the limit in advance.

## 3.5 Limit superior and inferior

For a bounded sequence, define

$$
\limsup_{n\to\infty}a_n=\lim_{n\to\infty}\sup_{k\ge n}a_k,
\qquad
\liminf_{n\to\infty}a_n=\lim_{n\to\infty}\inf_{k\ge n}a_k.
$$

These limits exist because the tail suprema decrease and tail infima increase. Always $\liminf a_n\le\limsup a_n$, and equality holds exactly when the sequence converges, with the common value equal to the limit.

For $a_n=(-1)^n$, the limit superior is $1$ and the limit inferior is $-1$. The definitions extend naturally to unbounded sequences using $\pm\infty$.

## Common pitfalls

1. Boundedness alone does not imply convergence.
2. A convergent subsequence alone does not make the whole sequence converge.
3. When solving a recursive limit equation, existence of the limit must be proved first.

## Exercises

1. Prove from the definition that $(3n-2)/(2n+5)\to3/2$.
2. Show that $a_n=(1+1/n)^n$ is convergent after establishing that it is increasing and bounded above.
3. Find the limit superior and limit inferior of $a_n=(-1)^n+1/n$.

> [!answer]- Short answers
> 1. The absolute error is $19/(2(2n+5))$, which is less than $5/n$; choose $N>5/\varepsilon$.
> 2. The [[#^monotone-convergence-theorem|monotone convergence theorem]] applies; the limit is denoted $e$.
> 3. The even and odd subsequences tend to $1$ and $-1$, so the values are $1$ and $-1$.

---

[[en/02-real-numbers|← 2. The Real Numbers and Completeness]] · [[en/index|Course index]] · [[en/term-index|Terms & theorems]] · [[en/04-numeric-series|4. Numerical Series →]]
