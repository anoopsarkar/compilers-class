lexlib=l
yacclib=y
bindir=.
rm=/bin/rm -f
mv=/bin/mv -f
yacctargets=expr
targets=simple-expr multexpr simple-varexpr varexpr anbn coordination unambexpr expr-conflicts parens
cpptargets=usingcpp expr-interpreter

all: $(targets) $(cpptargets)

$(targets): %: %.y
	@echo "compiling yacc file:" $<
	@echo "output file:" $@
	bison -o$@.tab.c -d $<
	flex -o$@.lex.c $@.lex
	gcc -w -o $(bindir)/$@ $@.tab.c $@.lex.c -l$(yacclib) -l$(lexlib)
	$(rm) $@.tab.c $@.tab.h $@.lex.c

$(cpptargets): %: %.y
	@echo "compiling cpp yacc file:" $<
	@echo "output file:" $@
	bison -b $@ -d $<
	$(mv) $@.tab.c $@.tab.cc
	flex -o$@.lex.cc $@.lex
	g++ -w -o $(bindir)/$@ $@.tab.cc $@.lex.cc -l$(yacclib) -l$(lexlib)
	$(rm) $@.tab.h $@.tab.cc $@.lex.cc

$(yacctargets): %: %.y
	bison -o$@.tab.c $<
	gcc -w -o $(bindir)/$@ $@.tab.c -l$(yacclib)
	$(rm) $@.tab.c

clean:
	$(rm) $(targets) $(cpptargets) $(yacctargets)
	$(rm) *.tab.h *.tab.c *.lex.c
	$(rm) a.out
	$(rm) *.pyc

