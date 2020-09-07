#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>


/* pick BUFLEN to be a suitably large number to show the speed
   difference between send and send2 */
const size_t BUFLEN = 400000000;

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

void send (char *to, char *from, int count)
{
  while (count-- > 0)
    *to++ = *from++;
}

int main (int argc, char **argv)
{
  char *from, *to;
  int i;
  struct timeval before, after;

  from = (char *) malloc(BUFLEN * sizeof(char));
  to = (char *) malloc(BUFLEN * sizeof(char));

  memset(from, 'a', (BUFLEN * sizeof(char)));
  memset(to, 'b', (BUFLEN * sizeof(char)));
  printf("array init done\n");

  printf("calling send2\n");
  gettimeofday(&before, NULL);
  send2(to, from, BUFLEN);
  gettimeofday(&after, NULL);
  printf("secs=%d\n", (int)after.tv_sec - (int)before.tv_sec);
  printf("microsecs=%d\n", abs((int)after.tv_usec - (int)before.tv_usec));
}
