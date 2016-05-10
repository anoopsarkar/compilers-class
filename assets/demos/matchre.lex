%{
  /* stress test comparing lex with Perl */

  /* test with:  perl -e 'print "a" x 100000; print "\n"' | matchre */
  /* compare with: perl -e 'print "yes\n" if (("a" x 100000) =~ /^(ab?)*$/);' */

#include <stdio.h>
%}

%%

^(ab?)*$	{ printf("yes\n"); }
^.*$		{ printf("no\n"); }

%%

