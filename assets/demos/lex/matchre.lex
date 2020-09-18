%{
  /* Compare Lex with Python and Perl

    Lex:
        make matchre
        time python -c 'print("b"*100000 + "d")' | ./matchre
        time python -c 'print("b"*100000)' | ./matchre

    Python:
        time python -c 'print("b"*100000 + "d")' | python matchre.py 
        time python -c 'print("b"*100000)' | python matchre.py 

    Perl:
        time perl -e 'print "b"x100000 . "d"'  | perl matchre.pl
        time perl -e 'print "b"x100000' | perl matchre.pl

  */
#include <stdio.h>
%}

%%

^((a|b)+(b|c)+)+d$    { printf("yes\n"); return 0; }
.+                    { printf("no\n"); return 0; }

%%

