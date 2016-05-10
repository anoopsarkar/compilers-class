%{
#include "expr.tab.h"
extern int yylval;
%}

num [0-9]+\.?|[0-9]*\.[0-9]+

%%

[ \t]     ; /* skip blanks and tabs */
[0-9]+  { yylval = atoi(yytext); return NUMBER; }
\n|.    { return yytext[0]; }

