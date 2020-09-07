#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>


/* pick BUFLEN to be a suitably large number to show the speed
   difference between send and send2 */
const size_t BUFLEN = 400000000;

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

  printf("calling send\n");
  gettimeofday(&before, NULL);
  send(to, from, BUFLEN);
  gettimeofday(&after, NULL);
  printf("secs=%d\n", (int)after.tv_sec - (int)before.tv_sec);
  printf("microsecs=%d\n", abs((int)after.tv_usec - (int)before.tv_usec));
}
