---
title: "How to Use the Vault and Notation"
lang: en
---
# How to Use the Vault and Notation

[Course index](index.md) · [Formula sheet](formula-sheet.md) · [Glossary](glossary.md)

## Obsidian and GitHub

Open the `MathInMind` directory as an Obsidian vault. All course navigation uses ordinary relative Markdown links, which also work on GitHub. Inline formulas use `$...$`, display formulas use `$$...$$`, and diagrams use simple Mermaid `flowchart` blocks. Exercise answers are inside `<details>` elements; click or expand them only after attempting the problem.

No community plugin or custom MathJax preamble is required. If equations appear as source text in Obsidian, check that MathJax is enabled in the editor settings.

## Logical and set notation

| Notation | Meaning |
|---|---|
| $\forall$, $\exists$ | for all, there exists |
| $\neg$, $\land$, $\lor$, $\implies$, $\iff$ | not, and, or, implies, if and only if |
| $\varnothing$, $A^c$, $A\setminus B$ | empty set, complement, set difference |
| $A\subseteq B$ | subset, allowing equality |
| $\mathcal P(A)$ | power set of $A$ |
| $1_A$ | indicator: $1_A(x)=1$ if $x\in A$, otherwise $0$ |

## Number sets and intervals

We use $\mathbb N=\{1,2,3,\ldots\}$ and $\mathbb N_0=\{0,1,2,\ldots\}$. The symbols $\mathbb Z,\mathbb Q,\mathbb R,\mathbb C$ denote integers, rationals, reals, and complex numbers. The extended real line is $\overline{\mathbb R}=\mathbb R\cup\{-\infty,+\infty\}$.

Intervals are $(a,b)$ open, $[a,b]$ closed, and $[a,b)$ or $(a,b]$ half-open. Unless stated otherwise, $\log x$ is the natural logarithm.

## Analysis notation

| Notation | Meaning |
|---|---|
| $\sup A$, $\inf A$ | least upper bound, greatest lower bound |
| $\limsup a_n$, $\liminf a_n$ | limit superior, limit inferior |
| $a_n\sim b_n$ | $a_n/b_n\to1$ for eventually nonzero terms |
| $f=O(g)$ | $|f|\le C|g|$ in the stated limit regime |
| $f=o(g)$ | $f/g\to0$ in the stated limit regime |
| $f'$, $\partial_i f$, $Df$ | ordinary, partial, and total derivatives |
| $\nabla f$, $Hf$ | gradient and Hessian |
| $\|x\|_p$ | $p$-norm; $\|x\|$ usually means Euclidean norm |
| $\langle f,g\rangle$ | inner product, specified in context |
| a.e. | almost everywhere, outside a null set |
| $C^k$, $C^\infty$ | $k$ times continuously differentiable, infinitely differentiable |

For asymptotic notation, always note the regime, such as $x\to0$ or $n\to\infty$. In integrals, $dA$ and $dV$ denote area and volume elements; in measure theory, $d\mu$ identifies the underlying measure.

## Proof checklist

Before using a theorem, ask:

1. Are the domain and regularity hypotheses satisfied?
2. Is the convergence pointwise, uniform, absolute, almost everywhere, or in norm?
3. Are endpoints, orientation, compactness, and finiteness assumptions relevant?
4. Does an example actually prove the claim, or only illustrate it?
5. Can a counterexample show that an omitted hypothesis is necessary?
