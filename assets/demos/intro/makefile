
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

send: send.c
	clang -o send send.c
	pygmentize -f rtf -o send.rtf send.c

send2: send2.c
	clang -o send2 send2.c
	pygmentize -f rtf -o send2.rtf send2.c

clean:
	/bin/rm -f hello hello.o
	/bin/rm -f mult mult.o
	/bin/rm -f quine quine2 quine.c
	/bin/rm -f send send2
	/bin/rm -f *.rtf
