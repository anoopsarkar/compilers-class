#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <sys/time.h>

void send2 (char *to, char *from, int count)
{  
    int n = (count+7)/8;  
    switch (count % 8) {  
    case 0: do { *to++ = *from++;  
    case 7:      *to++ = *from++;  
    case 6:      *to++ = *from++;  
    case 5:      *to++ = *from++;  
    case 4:      *to++ = *from++;  
    case 3:      *to++ = *from++;  
    case 2:      *to++ = *from++;  
    case 1:      *to++ = *from++;
          } while(--n > 0);  
    }
}

/*
void send2 (char *to, char *from, int count)
{
  int n = (count+7)/8;
  switch (count % 8) {
  case 0: while(n-- > 0) { *to++ = *from++;
  case 7:                  *to++ = *from++;
  case 6:                  *to++ = *from++;
  case 5:                  *to++ = *from++;
  case 4:                  *to++ = *from++;
  case 3:                  *to++ = *from++;
  case 2:                  *to++ = *from++;
  case 1:                  *to++ = *from++;
          }
  }
}
*/

void send (char *to, char *from, int count)
{
  while (count-- > 0)
    *to++ = *from++;
}

bool check(char *to, char *from, int count)
{
  while (count-- > 0)
    if (!(*to++ == *from++)) return false;
  return true;
}

int main (int argc, char **argv)
{
  char *from, *to, *from2, *to2;
  int i;
  struct timeval before, after;
  int count;

  if (argc < 2) {
    printf("provide count\n");
    exit(1);
  }
  count = atoi(argv[1]);
  printf("using count %d\n", count);

  from = (char *) malloc(count * sizeof(char));
  to = (char *) malloc(count * sizeof(char));
  from2 = (char *) malloc(count * sizeof(char));
  to2 = (char *) malloc(count * sizeof(char));

  memset(from, 'a', (count * sizeof(char)));
  memset(to, 'b', (count * sizeof(char)));
  memset(from2, 'a', (count * sizeof(char)));
  memset(to2, 'b', (count * sizeof(char)));

  printf("array init done\n");

  printf("calling send2\n");
  gettimeofday(&before, NULL);
  send2(to2, from2, count);
  gettimeofday(&after, NULL);
  printf("send2 secs=%d\n", (int)after.tv_sec - (int)before.tv_sec);
  printf("send2 microsecs=%d\n", abs((int)after.tv_usec - (int)before.tv_usec));

  printf("calling send\n");
  gettimeofday(&before, NULL);
  send(to, from, count);
  gettimeofday(&after, NULL);
  printf("send secs=%d\n", (int)after.tv_sec - (int)before.tv_sec);
  printf("send microsecs=%d\n", abs((int)after.tv_usec - (int)before.tv_usec));

  if (check(to, from, count)) {
    printf("check to, from passed\n");
  } else {
    printf("check to, from failed\n");
  }
  if (check(to, to2, count)) {
    printf("check to, to2 passed\n");
  } else {
    printf("check to, to2 failed\n");
  }
  if (check(from, from2, count)) {
    printf("check from, from2 passed\n");
  } else {
    printf("check from, from2 failed\n");
  }

}
