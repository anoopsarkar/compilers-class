
/* The Duff device 
 *
 * An infamous example of how a compiler can accept code that appears
 * to be illegal as per the language definition. To add insult to
 * injury, the "illegal" code actually runs faster.
 *
 * The functions send and send2 accomplish the same goal (copying a
 * string from one location to another). 
 *
 * send2 looks like it has an obvious syntax error, but most C
 * compilers will actually create an executable for this code, and it
 * will actually run much faster (on most CPU architectures).
 * 
 * What looks like a syntax error in function send2 is actually valid
 * as per the C grammar. Why? Hint: think of the infamous "goto"
 * statement.
 * 
 * This strange piece of code is named after the programmer who
 * discovered this 'optimization' technique.
 *
 * -- Anoop Sarkar <anoop at cs.sfu.ca>
 **/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>

/* pick BUFLEN to be a suitably large number to show the speed
   difference between send and send2 */
const size_t BUFLEN = 400000000;

void
send (register char *to, register char *from, register int count)
{
  while (count-- > 0)
    *to++ = *from++;
}

void
send2 (register char *to, register char *from, register int count)
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

/* Reason why send2 works:

   If you examine the C language specification for the language
   syntax specification,

   selection_statement -> SWITCH '(' expression ')' statement

   iteration_statement -> WHILE '(' expression ')' statement
        | DO statement WHILE '(' expression ')' ';'

   statement -> labeled_statement

   labeled_statement -> CASE constant_expression ':' statement

*/

int
main (int argc, char **argv)
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

  if (strcmp(from,to) == 0) {
    printf("from=to\n");
  } else {
    printf("from!=to\n");
  }

  memset(to, 'b', (BUFLEN * sizeof(char)));

  printf("calling send2\n");
  gettimeofday(&before, NULL);
  send2(to, from, BUFLEN);
  gettimeofday(&after, NULL);
  printf("secs=%d\n", (int)after.tv_sec - (int)before.tv_sec);
  printf("microsecs=%d\n", abs((int)after.tv_usec - (int)before.tv_usec));

  if (strcmp(from,to) == 0) {
    printf("from=to\n");
  } else {
    printf("from!=to\n");
  }

  free(from);
  free(to);

  return(0);
}
