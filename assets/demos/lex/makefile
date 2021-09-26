
lexlib=l
bindir=.
rm=/bin/rm -f
targets=matchre smash-gcc-lex tokenizer2
cpptargets=

all: $(targets) $(cpptargets)

$(targets): %: %.lex
	@echo "compiling lex file:" $<
	@echo "output file:" $@
	flex -o$@.c $<
	cc -o $(bindir)/$@ $@.c -l$(lexlib)
	$(rm) $@.c

$(cpptargets): %: %.lex
	@echo "compiling cpp lex file:" $<
	@echo "output file:" $@
	flex -o$@.cc $<
	c++ -o $(bindir)/$@ $@.cc -l$(lexlib)
	$(rm) $@.cc

clean:
	$(rm) a.out $(targets) $(cpptargets)

