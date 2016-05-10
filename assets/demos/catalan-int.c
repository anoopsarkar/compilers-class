
#include <stdio.h>
#include <stdlib.h>

int fact(int n) { 
  return n ? (n*fact(n-1)) : 1; 
}

int choose(int a, int b) { 
  return fact(a)/(fact(b)*fact(a-b)); 
}

int catalan(int n) { 
  return choose(2*n,n)/(n+1); 
}

int main(int argc, char **argv) {
  int n;
  if (argc < 2) { 
    printf("usage: catalan <number>\n"); 
    return EXIT_FAILURE;
  }
  n = (int)strtol(argv[1], (char **)NULL, 10);
  printf("catalan: %d %d\n", n, catalan(n));
  return EXIT_SUCCESS;
}
