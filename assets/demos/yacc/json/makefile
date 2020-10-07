lexlib=l
yacclib=y
bindir=.
rm=/bin/rm -f
mv=/bin/mv -f
yacctargets=
targets=
cpptargets=
cpp11targets=json

all: $(cpp11targets)

$(targets): %: %.y
	@echo "compiling yacc file:" $<
	@echo "output file:" $@
	bison -o$@.tab.c -d $<
	flex -o$@.lex.c $@.lex
	cc -w -o $(bindir)/$@ $@.tab.c $@.lex.c -l$(yacclib) -l$(lexlib)
	$(rm) $@.tab.c $@.tab.h $@.lex.c

$(cpptargets): %: %.y
	@echo "compiling cpp yacc file:" $<
	@echo "output file:" $@
	bison -b $@ -d $<
	$(mv) $@.tab.c $@.tab.cc
	flex -o$@.lex.cc $@.lex
	c++ -w -o $(bindir)/$@ $@.tab.cc $@.lex.cc -l$(yacclib) -l$(lexlib)
	$(rm) $@.tab.h $@.tab.cc $@.lex.cc

$(cpp11targets): %: %.y
	@echo "compiling cpp yacc file:" $<
	@echo "output file:" $@
	bison -b $@ -d $<
	$(mv) $@.tab.c $@.tab.cc
	flex -o$@.lex.cc $@.lex
	c++ -std=c++11 -w -o $(bindir)/$@ $@.tab.cc $@.lex.cc -l$(yacclib) -l$(lexlib)
	$(rm) $@.tab.h $@.tab.cc $@.lex.cc

$(yacctargets): %: %.y
	bison -o$@.tab.c $<
	cc -w -o $(bindir)/$@ $@.tab.c -l$(yacclib)
	$(rm) $@.tab.c

clean:
	$(rm) $(targets) $(cpptargets) $(cpp11targets) $(yacctargets)
	$(rm) *.tab.h *.tab.c *.lex.c
	$(rm) a.out
	$(rm) *.pyc

