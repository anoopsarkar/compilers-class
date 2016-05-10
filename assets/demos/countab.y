%{
#include <stdio.h>
int yylex(void);
int yyerror(char *);
%}
%union{
	int count;
}
%type <count> S
%%
start: S { printf("count:%d\n", $1); }
S: 'a' S 'b' { $$ = $2 + 1; }
 | { $$ = 0; }
 ;
