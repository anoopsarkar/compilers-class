
# For linux use "make libenglish.so" and "make dllinux" and run the
# programs using "LD_LIBRARY_PATH=. ./hello" and
# "LD_LIBRARY_PATH=. ./dlhello libenglish.so"
# use "make static" for statically linked version

libenglish.so: english.c
	gcc -fPIC -c english.c
	gcc -shared -o libenglish.so english.o

libkorean.so: korean.c
	gcc -fPIC -c korean.c
	gcc -shared -o libkorean.so korean.o

dllinux: dlhello.c
	gcc -c dlhello.c
	gcc -o dlhello dlhello.o -ldl

staticlinux: hello.c libenglish.so libkorean.so
	gcc -c hello.c
	gcc -o english_hello hello.o -L. -lenglish
	gcc -o korean_hello hello.o -L. -lkorean

# For macosx use "make libenglish.dylib" and "make dlmac" and run the
# programs using "./hello" and "./dlhello ./libenglish.dylib"
# use "make static" for statically linked version

libenglish.dylib: english.c
	gcc -fPIC -c english.c
	gcc -dynamiclib -o libenglish.dylib english.o

libkorean.dylib: korean.c
	gcc -fPIC -c korean.c
	gcc -dynamiclib -o libkorean.dylib korean.o

dlmac: dlhello.c
	gcc -c dlhello.c
	gcc -o dlhello dlhello.o

staticmac: hello.c libenglish.dylib libkorean.dylib
	gcc -c hello.c
	gcc -o english_hello hello.o -L. -lenglish
	gcc -o korean_hello hello.o -L. -lkorean

# common cleanup stuff

clean:
	/bin/rm -f english_hello korean_hello dlhello *.o *.so *~ *.dylib

archive:
	ar -r dylib.ar *.c makefile

