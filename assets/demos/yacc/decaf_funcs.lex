%{
/* example that illustrates using C++ code and flex/bison */
#include "decaf_funcs_defs.h"
#include "decaf_funcs.tab.h"
#include <cstring>
using namespace std;
%}

%%
func                   { return FUNC_KW; }
int                    { return INT_TY; }
bool                   { return BOOL_TY; }
return                 { return RET_KW; }
[a-zA-Z_]              { yylval.sval = strdup(yytext); return ID; }
[ \t\n]                ;
.                      return yytext[0];
%%

