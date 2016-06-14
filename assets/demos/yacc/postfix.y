%{
#include <stdio.h>
#include <stdlib.h>
%}

%union {
  char *sval;
}

%token <sval> T_ID

%%

start: e

e: t r

r: '+' t { printf("+"); } r
 | '-' t { printf("-"); } r
 |
 ;

t: T_ID { printf("%s", $1); free($1); }

%%

