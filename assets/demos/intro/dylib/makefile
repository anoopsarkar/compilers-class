
# For linux use "make libenglish.so" and "make dllinux" and run the
# programs using "LD_LIBRARY_PATH=. ./hello" and
# "LD_LIBRARY_PATH=. ./dlhello libenglish.so"
# use "make static" for statically linked version

libenglish.so: english.c
	cc -fPIC -c english.c
	cc -shared -o libenglish.so english.o

libkorean.so: korean.c
	cc -fPIC -c korean.c
	cc -shared -o libkorean.so korean.o

dllinux: dlhello.c
	cc -c dlhello.c
	cc -o dlhello dlhello.o -ldl

staticlinux: hello.c libenglish.so libkorean.so
	cc -c hello.c
	cc -o english_hello hello.o -L. -lenglish
	cc -o korean_hello hello.o -L. -lkorean

# For macosx use "make libenglish.dylib" and "make dlmac" and run the
# programs using "./hello" and "./dlhello ./libenglish.dylib"
# use "make static" for statically linked version

libenglish.dylib: english.c
	cc -fPIC -c english.c
	cc -dynamiclib -o libenglish.dylib english.o

libkorean.dylib: korean.c
	cc -fPIC -c korean.c
	cc -dynamiclib -o libkorean.dylib korean.o

dlmac: dlhello.c
	cc -c dlhello.c
	cc -o dlhello dlhello.o

staticmac: hello.c libenglish.dylib libkorean.dylib
	cc -c hello.c
	cc -o english_hello hello.o -L. -lenglish
	cc -o korean_hello hello.o -L. -lkorean

# common cleanup stuff

clean:
	/bin/rm -f english_hello korean_hello dlhello *.o *.so *~ *.dylib

archive:
	zip dylib.zip *.c makefile

