---
layout: default
img: green_dragon_book
img_link: "https://en.wikipedia.org/wiki/Principles_of_Compiler_Design"
caption: "Principles of Compiler Design, by Alfred Aho and Jeffrey Ullman, published in 1977, is the classic textbook on compilers."
title: Lex Practice
active_tab: practice
---

## Lexical Analysis: Practice Problems 

### Clone the repository

The files below and other example programs are available in a git repository

You must have git and python (3.x) on your system. Once you've confirmed this, run this command:

    git clone https://github.com/anoopsarkar/compilers-class-hw.git

If you have already cloned the repository earlier you can
get the new homework files by going to the directory
where you cloned the repository earlier and then doing:

    # go to the directory where you did a git clone earlier
    git pull origin master

Then go to the `lex-practice` directory

    cd /your-path-to/compilers-class-hw/lex-practice

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
    python3 zipout.py

This creates a directory called `output` and a file `output.zip`. If you run `zipout.py` multiple times it will overwrite your output directory and zip file which should be fine most of the time (but be careful).

Check your solution accuracy using the Python program `check.py`. You must create an `output.zip` file first using `python3 zipout.py`.

    python3 check.py 

### Matching a Right Context

Lex can match a _right context_ while matching a regexp by using
the notation $$r_1/r_2$$ where the regexp $$r_1$$ will match only if
the right context matches the regexp $$r_2$$. The longest match
is computed using $$r_1$$ and $$r_2$$ concatenated together. The
lexeme reported is the match for $$r_1$$.

For example, consider the following lex program.

    %%
    a+/b  { printf("T_AB:%s\n", yytext); }
    a+/c  { printf("T_AC:%s\n", yytext); }
    b     { printf("T_B:%s\n", yytext); }
    c     { printf("T_C:%s\n", yytext); }
    .|\n  ECHO;

Here is how it behaves for a few inputs:

    On input: ab
    T_AB:a
    T_B:b

    On input: ac
    T_AC:a
    T_C:c

    On input: abc
    T_AB:a
    T_B:b
    T_C:c

Read the following lex program:

    %%
    a*b+/c+  { printf("T_AB:%s\n", yytext); }
    a*b*c/a  { printf("T_ABC:%s\n", yytext); }
    a        { printf("T_A:%s\n", yytext); }
    c+       { printf("T_C:%s\n", yytext); }
    .|\n  ECHO;

Predict what it will print out for the input string `abcca`.

### Matching a Left Context

Lex can also match the _left context_ with the use of _states_. 
The lex program below matches keyword called `inputfile` as the left context
so that a string following this keyword is treated differently from one that does not.

    %{
    /* example illustrating the use of states in lex 
       declare a state called INPUT using: %s INPUT
       enter a state using: BEGIN INPUT
       match a token only if in a certain state: <INPUT>\".*\"
    */
    %}

    %s INPUT

    %%

    [ \t\n]+                ;
    inputfile       BEGIN INPUT;
    <INPUT>\".*\"   { BEGIN 0; ECHO; printf(" is the input file.\n"); }
    \".*\"          { ECHO; printf("\n"); }
    .                ;

    %%

Modify the lex program to include a new left context for the keyword 
`outputfile` so that for the input:

    inputfile "fileA"
    outputfile "fileB"

Your program produces the output:

    "fileA" is the input file.
    "fileB" is the output file.

<!--
#### Answer

    %s INPUT
    %s OUTPUT

    %%

    [ \t\n]+                ;
    inputfile       BEGIN INPUT;
    outputfile      BEGIN OUTPUT;
    <INPUT>\".*\"   { BEGIN 0; ECHO; printf(" is the input file.\n"); }
    <OUTPUT>\".*\"  { BEGIN 0; ECHO; printf(" is the output file.\n"); }

    %%
-->

### Backtracking in Lex

Lex can be forced to perform backtracking regexp matching using the REJECT command.
For instance, this lex program does a match, does the action, and then resets back to
the start of the match. 

    %{
    int numpat1, numpat2;
    %}

    %%
    a+     { numpat1++; REJECT; }
    a*b?   { numpat2++; REJECT; }
    .|\n   /* do nothing */
    %%

    int main () {
      yylex();
      printf("pattern a+: %d -- pattern a*b?: %d\n", numpat1, numpat2);
      exit(0);
    }

On input `aaa` the lex program above will produce the output:

    pattern a+: 6 -- pattern a*b?: 6

This is because there are $$\frac{n(n+1)}{2}$$ substrings for a string of length $$n$$.
Predict the number of pattern matches for the following inputs, and check by running
the lex program.

    aaa
    aa
    ab

### Counting with Lex

Provide a lex program that reports the frequency of each pair of
words in a text file. Each word is a sequence of non-whitespace
characters separated by one or more whitespace characters (space
and tab). The lex program below shows you how to use C++ in your
lex program. However it does not compute the frequency of each
pair of words correctly.

    %{

    #include <iostream>
    #include <sstream>
    #include <utility>
    #include <string>
    #include <map>
    #include <iterator>
    #include <vector>
    #include <algorithm>
    #include <cstdlib>

    using namespace std;

    typedef pair<string, string> bigram_type;
    typedef map<bigram_type, int>::iterator dict_iter;

    map<bigram_type, int> dict;

    void
    addtodict(char *yytext) {
      string s(yytext);
      istringstream sin(s);
      vector<string> tokens;
      copy(istream_iterator<string>(sin), istream_iterator<string>(), back_inserter(tokens));
      bigram_type key(tokens[0], tokens[1]);
      dict_iter find_bigram; 
      if ((find_bigram = dict.find(key)) != dict.end()) {
        dict[key] = dict[key] + 1;
      } else {
        dict[key] = 1;
      }
    }

    %}

    ws [ \t\n]*
    notws [^ \t\n]+

    %%

    ^{notws}{ws}{notws}{ws}     { addtodict(yytext); }
    {ws}{notws}{ws}{notws}{ws}  { addtodict(yytext); }
    .|\n                        /* do nothing */

    %%

    int main () {
      yylex();
      for (dict_iter i = dict.begin(); i != dict.end(); i++) {
        cout << (i->first).first << " " << (i->first).second << " " << i->second << endl;
      }
      exit(EXIT_SUCCESS);
    }

On the input string `the cat on the mat saw the cat on the cat box on the mat spit` the lex program above prints out:

    cat box 1
    mat saw 1
    mat spit 1
    on the 3
    the cat 2

The right output should be:

    box on 1
    cat box 1
    cat on 2
    mat saw 1
    mat spit 1
    on the 3
    saw the 1
    the cat 3
    the mat 2


