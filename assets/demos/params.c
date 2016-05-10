#include <stdio.h>

void foo(int x, int y) {
  printf("foo.x:%d\nfoo.y:%d\n", x, y); 
}

int main() {
  int x;

  x = 1;
  printf("++x ++x\n");
  foo(++x, ++x);
  printf("x:%d\n\n", x);

  x = 1;
  printf("x++ x++\n");
  foo(x++, x++);
  printf("x:%d\n\n", x);

  x = 1;
  printf("x++ ++x\n");
  foo(x++, ++x);
  printf("x:%d\n\n", x);

  x = 1;
  printf("++x x++\n");
  foo(++x, x++);
  printf("x:%d\n\n", x);
}
