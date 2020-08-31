
hello: hello.c
	clang -c hello.c
	objdump -s -d hello.o

mult: mult.c
	clang -c mult.c
	objdump -s -d mult.o

quine: myquine.c
	clang -o quine myquine.c
	./quine > quine.c
	clang -o quine2 quine.c
	./quine2
	diff myquine.c quine.c

clean:
	/bin/rm -f hello hello.o
	/bin/rm -f mult mult.o
	/bin/rm -f quine quine2 quine.c
