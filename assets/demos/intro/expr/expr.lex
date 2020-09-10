%{
#include "expr.tab.h"
extern int yylval;
%}

%%

[ \t]     ; /* skip blanks and tabs */
[0-9]+  { yylval = atoi(yytext); return NUMBER; }
\n|.    { return yytext[0]; }

