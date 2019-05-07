%{
#include <stdio.h>
int yylex();
void yyerror(const char *s);
%}

%token NUMBER
%left '+'
%left '*'

%%
lines : lines expr '\n' { printf("%d\n", $2); }
      | /* empty line */
      ;

expr : expr '+' expr { $$ = $1 + $3; }
     | expr '*' expr { $$ = $1 * $3; }
     | '(' expr ')'  { $$ = $2; }
     | NUMBER        { $$ = $1; }
     ;

%%

