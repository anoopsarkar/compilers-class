%{
/* example that illustrates using C++ code and flex/bison */

/* note that this particular example does not use the C++ flex
interface as described in the bison manual */

#include "decaf_funcs_defs.h"
#include <cstring>
#include <string>
#include <iostream>

using namespace std;

%}

/* in the definition of %union you can only have scalar types like
int, double or a pointer type, e.g. you cannot have 'string tval'
as a valid type for tokens or non-terminals */

%union {
    char *sval;
    string *tval; 
}

%token FUNC_KW INT_TY BOOL_TY RET_KW
%token <sval> ID /* define return type for tokens from lexical analyzer */
%type <tval> func params has_params type body /* define return type for non-terminals in grammar */

%%

start: func
    { 
        // cout << $1; 
    }
func: FUNC_KW ID '(' params ')' type '{' body '}'
    { 
        //$$ = "Method(($2, $6, $4, $8)"; 
    }
params: has_params 
    { 
        // $$ = $1; 
    }
  |
    { 
        // $$ = "None"; 
    }
has_params: ID type ',' has_params 
    { 
        // $$ = "VarDef($1,$2),"; 
    }
  | ID type
    { 
        // $$ = "VarDef($1,$2)"; 
    }
type: INT_TY 
    { 
        // $$ = "IntType"; 
    }
  | BOOL_TY
    { 
        // $$ = "BoolType"; 
    }
body: RET_KW '(' ID ')' ';' 
    { 
        // $$ = "MethodBlock(None,ReturnStmt(VariableExpr($2)))";  
    }
  | RET_KW  ';'
    {
        // $$ = "MethodBlock(None,ReturnStmt())"; 
    }
  |
    { 
        // $$ = "MethodBlock(None,ReturnStmt())"; 
    }

%%
