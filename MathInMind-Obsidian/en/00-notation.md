---
title: "How to Use the Vault and Notation"
lang: en
tags: [mathinmind/en, mathinmind/support]
---
# How to Use the Vault and Notation

[[en/index|Course index]] · [[en/formula-sheet|Formula sheet]] · [[en/glossary|Glossary]]

## Obsidian and GitHub

The course exists in two views, generated from the same text by `python3 scripts/build_views.py`:

| | GitHub view — `MathInMind/` | Obsidian view — `MathInMind-Obsidian/` |
|---|---|---|
| Open it | browse the repository on GitHub | **Open folder as vault** in Obsidian |
| Links | relative Markdown links with `#anchors` | `[[wikilinks]]` with hover previews, backlinks and the graph view |
| Inline formula | `` $`...`$ `` (survives GitHub's Markdown pass) | `$...$` (MathJax) |
| Display formula | a ```` ```math ```` block | `$$...$$` |
| Definitions and theorems | blockquotes with a bold label | coloured callouts (`[!definition]`, `[!theorem]`, …) |
| Exercise answers | `<details>` blocks | folded `[!answer]-` callouts |

Every term, named theorem and numbered lecture statement can be reached in one click: the first mention of a term in each note links to its definition, references such as "[[en/lectures-2025-26/lecture-13#^thm-2-3-5|Theorem 2.3.5]]" link to the statement, and the [[en/term-index|index of terms and theorems]] lists them all. Diagrams are simple Mermaid `flowchart` blocks, which both views render. Try each exercise before opening its answer.

No community plugin or custom MathJax preamble is required. If equations appear as source text in Obsidian, check that you opened `MathInMind-Obsidian/` (not `MathInMind/`) and that MathJax is enabled in the editor settings.

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

We use $\mathbb N=\{1,2,3,\ldots\}$ and $\mathbb N_0=\{0,1,2,\ldots\}$. The symbols $\mathbb Z,\mathbb Q,\mathbb R,\mathbb C$ denote integers, rationals, reals, and complex numbers. The [[en/02-real-numbers#2.4 Nested intervals and the real line|extended real line]] is $\overline{\mathbb R}=\mathbb R\cup\{-\infty,+\infty\}$.

Intervals are $(a,b)$ open, $[a,b]$ closed, and $[a,b)$ or $(a,b]$ half-open. Unless stated otherwise, $\log x$ is the natural logarithm.

## Analysis notation

| Notation | Meaning |
|---|---|
| $\sup A$, $\inf A$ | [[en/02-real-numbers#2.2 Supremum and infimum\|least upper bound]], greatest lower bound |
| $\limsup a_n$, $\liminf a_n$ | [[en/03-sequences#3.5 Limit superior and inferior\|limit superior]], limit inferior |
| $a_n\sim b_n$ | $a_n/b_n\to1$ for eventually nonzero terms |
| $f=O(g)$ | $\vert f\vert \le C\vert g\vert$ in the stated limit regime |
| $f=o(g)$ | $f/g\to0$ in the stated limit regime |
| $f'$, $\partial_i f$, $Df$ | ordinary, partial, and [[en/15-multivariable-differentiation#15.1 The total derivative\|total derivatives]] |
| $\nabla f$, $Hf$ | [[en/15-multivariable-differentiation#15.2 Partial and directional derivatives\|gradient]] and [[en/15-multivariable-differentiation#15.4 Higher derivatives and Taylor's formula\|Hessian]] |
| $\Vert x\Vert _p$ | $p$-norm; $\Vert x\Vert$ usually means [[en/14-several-variables#14.1 Euclidean space and norms\|Euclidean norm]] |
| $\langle f,g\rangle$ | [[en/21-lp-spaces#21.4 The Hilbert space L2\|inner product]], specified in context |
| [[en/19-measure-theory#19.4 Measurable functions\|a.e.]] | almost everywhere, outside a [[en/08-riemann-integration#8.2 Riemann sums and properties\|null set]] |
| $C^k$, $C^\infty$ | $k$ times continuously differentiable, infinitely [[en/06-derivatives#6.1 Definition and linear approximation\|differentiable]] |

For asymptotic notation, always note the regime, such as $x\to0$ or $n\to\infty$. In integrals, $dA$ and $dV$ denote area and volume elements; in measure theory, $d\mu$ identifies the underlying measure.

## Proof checklist

Before using a theorem, ask:

1. Are the domain and regularity hypotheses satisfied?
2. Is the convergence pointwise, uniform, absolute, almost everywhere, or in norm?
3. Are endpoints, orientation, [[en/13-metric-spaces#13.4 Compactness|compactness]], and finiteness assumptions relevant?
4. Does an example actually prove the claim, or only illustrate it?
5. Can a counterexample show that an omitted hypothesis is necessary?
