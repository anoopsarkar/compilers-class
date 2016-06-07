---
layout: default
img: green_dragon_book
img_link: "https://en.wikipedia.org/wiki/Principles_of_Compiler_Design"
caption: "Principles of Compiler Design, by Alfred Aho and Jeffrey Ullman, published in 1977, is the classic textbook on compilers."
title: Syllabus
active_tab: syllabus
---

## Parsing using Context-free Grammars and Yacc/Bison: Practice Problems 

### Simple interpreter

The yacc program below is a very simple (and incomplete) 
expression interpreter. The `{ ... }` section contains arbitrary C/C++ code and the 
`%token` definitions is a list of tokens provided by
the lexical analyzer. 

    %{ 
    #include <stdio.h> 
    %}
    %token NAME NUMBER
    %%
    statement: NAME '=' expression { printf("%c = %d\n", $1, $3); }
         | expression  { printf("%d\n", $1); }
         ;

    expression: expression '+' NUMBER { $$ = $1 + $3; }
         | expression '-' NUMBER { $$ = $1 - $3; }
         | NUMBER { $$ = $1; }
         ;
    %%

If you save the above program to a file called `simple-expr.y` then
the program `bison` can be used to convert this parser definition
into a parser implementation by using the following command:

    bison -osimple-expr.tab.c -d simple-expr.y

The `-d` option produces a header file called `simple-expr.tab.h`
to convey information about the tokens to the lexical analyzer. Examine
the contents of this file. 

The lexical analyzer is shown below as a lex program. 

    %{
    #include "simple-expr.tab.h"
    #include <stdlib.h>
    extern int yylval;
    %}
    %%
    [0-9]+   { yylval = atoi(yytext); return NUMBER; }
    [a-z]    { yylval = yytext[0]; return NAME; }
    [ \t\n]  /* ignore whitespace */
    .        return yytext[0];
    %%


Save it to a file called `simple-expr.lex`.
The lex program can be compiled to a C program using `flex`:

    flex -osimple-expr.lex.c simple-expr.lex

The final binary is created by compiling the output
from flex and bison with a C/C++ compiler as follows. 

    gcc -o ./simple-expr simple-expr.tab.c simple-expr.lex.c -ly -lfl
    echo "a=2+3+5" | ./simple-expr

Convert the above yacc and lex programs so that it can handle
multiple expressions, exactly one per line.
You will need a recursive context-free rule in the yacc definition
in order to handle multiple lines
of input. Try different ways of writing this recursive rule.
Note that we can assign a value to a variable, e.g `b=5+10-5` but
we cannot yet use `b` in a following expression, e.g. `a=b+10`
(which fails with a syntax error).


