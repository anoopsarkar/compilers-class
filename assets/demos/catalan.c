
#include <stdio.h>
#include <stdlib.h>

int fact(int n) { 
  return n ? (n*fact(n-1)) : 1; 
}

double choose(int a, int b) { 
  return fact(a)/(fact(b)*fact(a-b)); 
}

double catalan(int n) { 
  return choose(2*n,n)/(n+1); 
}

int main(int argc, char **argv) {
  int n;
  if (argc < 2) { 
    printf("usage: catalan <number>\n"); 
    return EXIT_FAILURE;
  }
  n = (int)strtol(argv[1], (char **)NULL, 10);
  printf("catalan: %d %f\n", n, catalan(n));
  printf("choose: %f\n", choose(2*n,n));
  printf("fact: %d\n", fact(n));
  printf("fact: %d\n", fact(2*n));
  printf("fact: %d\n", fact(14));
  return EXIT_SUCCESS;
}
