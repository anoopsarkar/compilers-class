
%token ID

%%

start: t

t: f
 | t '*' f
 ;

f: ID
 | '(' t ')'
 ;

%%

