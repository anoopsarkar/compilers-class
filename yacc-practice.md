---
layout: default
img: green_dragon_book
img_link: "https://en.wikipedia.org/wiki/Principles_of_Compiler_Design"
caption: "Principles of Compiler Design, by Alfred Aho and Jeffrey Ullman, published in 1977, is the classic textbook on compilers."
title: Yacc Practice
active_tab: practice
---

## Parsing with Yacc/Bison: Practice Problems 

### Simple Expression Interpreter

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

You can automate the creation of the binary using a `makefile`. `make` is very finicky about whitespace, especially the actions have to be indented using a literal tab character. To avoid headaches download the `makefile` directly by using the `view raw` link below.
<script src="https://gist.github.com/anoopsarkar/8aebb39f2ef1bb939a4b2e875172e025.js"></script>

Run `make simple-expr` assuming you used the same filenames suggested above. Then you can
test it with various inputs:

    echo "12" | ./simple-expr
    echo "a=2+3+5" | ./simple-expr

The yacc and lex code above does not yet handle assignments to
variables. In order to implement this, we need two different kinds
of values to be returned from the lexical analyzer: one for numbers,
and another for variable names. The lex code below shows you how to do
that. Save this lex code to the file `simple-varexpr.lex`.

    %{
    #include "simple-varexpr.tab.h"
    #include <math.h>
    %}

    %%
    [0-9]+    { yylval.rvalue = atoi(yytext); return NUMBER; } /* convert NUMBER token value to integer */
    [ \t\n]   ;  /* ignore whitespace */
    [a-z]     { yylval.lvalue = yytext[0] - 'a'; return NAME; } /* convert NAME token into index */
    .         return yytext[0];
    %%

For numbers it returns `yylval.rvalue` and for variable names it
returns `yylval.lvalue`. The two types of return value, `rvalue`
and `lvalue` are defined in the yacc program `simple-varexpr.y`
shown below.

    %{
    #include <stdio.h>
    #include <stdbool.h>
    int symtbl[26];
    bool issym[26];

    int yylex(void);
    int yyerror(char *);
    %}

    %union {
      int rvalue; /* value of evaluated expression */
      int lvalue; /* index into symtbl for variable name */
    }

    %token <rvalue> NUMBER
    %token <lvalue> NAME 

    %type <rvalue> expression

    %%
    statement: NAME '=' expression { symtbl[$1] = $3; issym[$1] = true; }
             | expression  { printf("%d\n", $1); }
             ;

    expression: expression '+' NUMBER { $$ = $1 + $3; }
             | expression '-' NUMBER { $$ = $1 - $3; }
             | NUMBER { $$ = $1; }
             ;
    %%

The two different return values are represented using the `%union`
declaration which is the same concept as the [union type in C and C++](https://en.wikipedia.org/wiki/Union_type). 
The `%union` declaration can include complex datatypes.
The yacc code defines a type not just for the tokens, but also for
nonterminals, which is specified in the `%type` definition.  This
allows yacc to check that the type of the non-terminal expression
is `rvalue`, an integer type.

Extend this code in two ways:

* First, add the ability to process multiple statements so that the following works:
    echo "a=10\nb=10" | ./simple-varexpr
* Second, properly handle assignments of values to variables. The
variable on the left hand side of an equation will be an $$\ell$$_-value_
and the variable used on the right hand side of an equation will
be a _r-value_.

### Adding Functions to your Expression Interpreter

Extend your expression interpreter to include constants of type `double`,
and variables that can hold either integer or double types. Finally, add 
the functions: `exp`, `sqrt`, `log` so that you can interpret
the following types of input:

    a = 2.0
    b = exp(a)
    b

To avoid issues with precedence of operators use the yacc grammar provided
below:

    %token T_DOUBLE T_NUMBER T_NAME T_EXP T_SQRT T_LOG

    %%
    statement_list : statement '\n' statement_list
       |
       ;

    statement: T_NAME '=' expression
       | expression
       ;

    expression: expression '+' T_NUMBER
       | expression '-' T_NUMBER
       | expression '+' T_DOUBLE
       | expression '-' T_DOUBLE
       | expression '+' T_NAME 
       | expression '-' T_NAME 
       | T_NUMBER
       | T_DOUBLE
       | T_NAME 
       | T_EXP '(' expression ')'
       | T_SQRT '(' expression ')'
       | T_LOG '(' expression ')'
       ;

    %%


