%token PACKAGE ID LCB RCB VAR INT ASSIGN INTCONSTANT SEMICOLON FUNC LPAREN RPAREN VOID BOOL
%%
program: PACKAGE ID LCB field_decl_list method_decl_list RCB
field_decl_list: field_decl field_decl_list
|
;
method_decl_list: method_decl method_decl_list
|
;
field_decl: VAR type ID ASSIGN INTCONSTANT SEMICOLON
method_decl: FUNC ID LPAREN RPAREN return_type
return_type: type
| VOID
;
type: INT
| BOOL
;
