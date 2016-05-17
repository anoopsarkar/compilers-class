---
layout: default
img: green_dragon_book
img_link: "https://en.wikipedia.org/wiki/Principles_of_Compiler_Design"
caption: "Principles of Compiler Design, by Alfred Aho and Jeffrey Ullman, published in 1977, is the classic textbook on compilers."
title: Syllabus
active_tab: syllabus
---

## Lexical Analysis: Practice Problems 

### Regexps

Let $$\Sigma = \{ 0, 1 \}$$ 

1. How many elements in the set $$\Sigma$$? 
<!-- two -->
1. Provide $$\Sigma^3$$. 
<!-- $$\{ 000, 001, 010, 011, 100, 101, 110, 111 \}$$ -->
1. Describe in English the set described by $$\Sigma^\ast$$. 
<!-- All strings that represent binary numbers (leading zeroes are allowed). -->
1. Give a regexp for all strings in $$\Sigma^\ast$$ equal to decimal number 6. 
<!-- $$0^*110$$ -->
1. Give regexp for all strings in $$\Sigma^\ast$$ that are powers of two. 
<!-- $$0^*10^*$$ -->
1. Give a regexp for all strings in $$\Sigma^\ast$$ that are even numbers. 
<!-- $${(0|1)}^*100^*$$ -->
1. Give a regexp for all strings in $$\Sigma^\ast$$ that are Binary Coded Decimal numbers (include the empty string). A BCD number is a decimal number where each decimal digit is encoded using a 4-bit representation of its binary value. For example, the BCD number of 2509 is `0010010100001001`. 
<!-- $$((0(0|1)(0|1)(0|1))|((100)(0|1)))^*$$ -->

### Lexical Analysis

You are given the following token definitions as regular expressions.

| `TOKEN_A` | `cda*` |
| `TOKEN_B` | `c*a*c` |
| `TOKEN_C` | `c*b` |
{: .table}

Provide the tokenized output for the following input strings using
the greedy longest match lexical analysis method. Provide the list
of tokens and the lexeme values.

1. `cdaaab`
<!-- TOKEN_A (cdaaa), TOKEN_C (b) -->
1. `cdccc`
<!-- TOKEN_A (cd), TOKEN_B (ccc) -->
1. `ccc`
<!-- TOKEN_B (ccc) -->
1. `cdccd`
<!-- TOKEN_A (cd), TOKEN_B (cc), ERROR (illegal token) -->

