%{
using namespace std;
#include "json-defs.h"
#include "json.tab.h"
#include <iostream>
%}

chars    [ !\"#\$%&\(\)\*\+,\-\.\/0-9:;\<=>\?\@A-Z\[\]\^\_\`a-z\{\|\}\~\t\v\r\n\a\f\b]
stresc   \\[\'\"tvrnafb\\]
notstresc \\[^\'\"tvrnafb\\]
true     true
false    false
dec      [0-9]+
float    \.[0-9]+

%%
  /*
   strings can have escape characters. json strings cannot have control chars
   so we do not allow any unescaped newline characters
  */
\"([^\n\"\\]*{stresc}?)*\"    { yylval.s_val = new string(yytext); return T_STR; }
-?{dec}{float}?                 { yylval.s_val = new string(yytext); return T_NUM; }
{true}|{false}                { yylval.s_val = new string(yytext); return T_BOOL; }
null                          { yylval.s_val = new string(yytext); return T_NULL; }
[\t\r\n\a\v\b ]+              ;
  /* 
   Error handling
   (be careful: error patterns should not match more input than a valid token)
  */
\"([^\n\"\\]*{notstresc}?)*\" { cerr << "Error: unknown escape sequence in string constant" << endl; return -1; }
\"\"\"                        { cerr << "Error: unterminated string constant" << endl; return -1; }
\"([^\n\"\\]*{notstresc}?)*\n { cerr << "Error: newline in string constant" << endl; return -1; }
\"([^\n\"\\]*{stresc}?)*$     { cerr << "Error: string constant is missing closing delimiter" << endl; return -1; }
.                             return yytext[0];
%%
