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
1. Provide $$\Sigma^3$$. 
1. Describe in English the set described by $$\Sigma^\ast$$. 
1. Give a regexp for all strings in $$\Sigma^\ast$$ equal to decimal number 6. 
1. Give regexp for all strings in $$\Sigma^\ast$$ that are powers of two. 
1. Give a regexp for all strings in $$\Sigma^\ast$$ that are even numbers. 
1. Give a regexp for all strings in $$\Sigma^\ast$$ that are Binary Coded Decimal numbers (include the empty string). A BCD number is a decimal number where each decimal digit is encoded using a 4-bit representation of its binary value. For example, the BCD number of 2509 is `0010010100001001`. 

<!--
#### Answer

1. two
1. $$\{ 000, 001, 010, 011, 100, 101, 110, 111 \}$$
1. All strings that represent binary numbers (leading zeroes are allowed).
1. $$0^*110$$
1. $$0^*10^*$$
1. $${(0|1)}^*100^*$$
1. $$((0(0|1)(0|1)(0|1))|((100)(0|1)))^*$$
-->

### Simple Tokenizer

The following is a simple tokenizer written in Lex:

    %{
    #include <stdio.h>
    #define NUMBER     256
    #define IDENTIFIER 257
    %}

    /* regexp definitions */
    num [0-9]+

    %%

    {num}           { return NUMBER; }
    [a-zA-Z0-9]+    { return IDENTIFIER; }
    \n              /* do nothing */
    .       { return -1; }

    %%

    int main () {
      int token;
      while ((token = yylex())) {
        switch (token) {
          case NUMBER: printf("NUMBER: %s, LENGTH:%d\n", yytext, (int)yyleng); break;
          case IDENTIFIER: printf("IDENTIFIER: %s, LENGTH:%d\n", yytext, (int)yyleng); break;
          default: printf("Error: %s not recognized\n", yytext);
        }
      }
      exit(0);
    }

To run this tokenizer save it to a file called `simpletok.lex` and then save the following build instructions as the file `makefile`.

    lexlib=l
    bindir=.
    rm=/bin/rm -f
    targets=simpletok

    all: $(targets)

    $(targets): %: %.lex
        @echo "compiling lex file:" $<
        @echo "output file:" $@
        flex -o$@.c $<
        gcc -o $(bindir)/$@ $@.c -l$(lexlib)
        $(rm) $@.c

    clean:
        $(rm) $(targets)
        $(rm) *.pyc

To compile simpletok run `make simpletok`.

    ./simpletok
    90int  # type this in yourself upto the comment char
    Ctrl-D # this terminates the standard input stream

You should see the lexer output:

    IDENTIFIER: 90int, LENGTH:5

Modify the pattern definition of the token IDENTIFIER so that it has to start with a letter (a-z or A-Z) and followed by a (possibly empty) sequence of letters or numbers.

<!--
#### Answer

    %{
    #include <stdio.h>
    #define NUMBER     256
    #define IDENTIFIER 257
    %}

    /* regexp definitions */
    num [0-9]+

    %%

    {num}                 { return NUMBER; }
    [a-zA-Z][a-zA-Z0-9]*  { return IDENTIFIER; }
    \n                    /* silently ignore */
    .                     { return -1; }

    %%

    int main () {
      int token;
      while ((token = yylex())) {
        switch (token) {
          case NUMBER: printf("NUMBER: %s, LENGTH:%d\n", yytext, (int)yyleng); break;
          case IDENTIFIER: printf("IDENTIFIER: %s, LENGTH:%d\n", yytext, (int)yyleng); break;
          default: printf("Error: %s not recognized\n", yytext);
        }
      }
      exit(0);
    }
-->

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
1. `cdccc`
1. `ccc`
1. `cdccd`

<!--
#### Answer

1. TOKEN_A (cdaaa), TOKEN_C (b)
1. TOKEN_A (cd), TOKEN_B (ccc)
1. TOKEN_B (ccc)
1. TOKEN_A (cd), TOKEN_B (cc), ERROR (illegal token)
-->

### Lexical Analysis using `lex`

The general architecture of a lexical analyzer for a programming
language is to specify tokens in terms of patterns.  For instance,
we can define a set of tokens `T_A, T_B, T_C`
each associated with a pattern specified as regular expressions.

| `T_A` | $$a$$ |
| `T_B` | $$abb$$ |
| `T_C` | $$a^\ast b^+$$ |
{: .table}

The lexical analysis engine should always pick the longest match
possible, and in case of two patterns matching a prefix of the input
of equal length, we break the tie by picking the pattern that was
listed first in the specification (e.g. the token `T_B` is
preferred over `T_C` for the input string $$abb$$, and for the same
input string, token `T_A` followed by `T_C` would be incorrect).

Provide a lexical analyzer using lex for the tokens shown above.
Start with the Simple Tokenizer lex program you developed.

<!--
#### Answer

    %{
    #include <stdio.h>
    #include <stdlib.h>
    #define T_A 256
    #define T_B 257
    #define T_C 258
    #define ERROR 666
    %}

    %%

    a      { return T_A; }
    abb    { return T_B; }
    a*b+   { return T_C; }
    \n     /* do nothing */
    .      { return ERROR; }

    %%

    int main () {
      int token;
      while ((token = yylex())) {
        switch (token) {
          case T_A: printf("T_A %s\n", yytext); break;
          case T_B: printf("T_B %s\n", yytext); break;
          case T_C: printf("T_C %s\n", yytext); break;
          default: fprintf(stderr, "illegal token\n"); printf("ERROR %s\n", yytext);
        }
      }
      exit(0);
}
-->

### Remove Multi-line Comments

Provide a lex program to replace all single-line and multi-line comments from C or C++ programs with an equivalent amount of whitespace. 
Single-line comments begin with `//` and continue to  the end of the line, and multi-line comments begin with `/*` and end with `*/`
`*/`. Note that `/*/` is not a valid comment. The C specification does not allow nested comments.

There are some testcases to help you develop your lex program. Clone the following repository (if you haven't done so already).

    git clone https://github.com/anoopsarkar/compilers-class-hw.git

If you have cloned it then do a `git pull` to get the latest files.

In the `rmcomments` directory you will find various python programs
which you can use to test your solution to this homework

Run your solution program on the testcases using the Python program `zipout.py`. 
Your solution must be compiled in the `answer` directory and must be called `rmcomments`.
Run against all testcases as follows:

    # go to the main rmcomments directory with the file zipout.py
    python zipout.py

This creates a directory called `output` and a file `output.zip`. If you run `zipout.py` multiple times it will overwrite your output directory and zip file which should be fine most of the time (but be careful).

Check your solution accuracy using the Python program `check.py`. You must create an `output.zip` file first.

    python check.py 

