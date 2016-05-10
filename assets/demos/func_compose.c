#include <stdio.h>

int foo(int f(int,int), int g(int,int), int x) {
  printf("foo: %d\n", x);
  int y = g(x,x);
  int r = f(y,y);
  printf("foo: %d returns %d\n", x, r);
  return r;
}

int sq(int x, int y) {
  printf("sq: %d,%d\n", x, y);
  int r;
  if (x == 1) { r = y; }
  else { r = pl(y, sq(x-1, y)); }
  printf("sq: %d,%d returns %d\n", x, y, r);
  return r;
}

int pl(int x, int y) {
  printf("pl: %d,%d\n", x, y);
  int r;
  if (x == 0) { r = y; }
  else { r = pl(x-1, y+1); }
  printf("pl: %d,%d returns %d\n", x, y, r);
  return r;
}

int main() {
  printf("main\n");
  printf("output=%d\n", foo(sq, pl, 1));
}
