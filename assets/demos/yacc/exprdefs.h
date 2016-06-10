
#ifndef _EXPRDEFS
#define _EXPRDEFS

extern "C"
{
  int yyerror(const char *);
  int yyparse(void);
  int yylex(void);  
  int yywrap(void);
}

#endif

