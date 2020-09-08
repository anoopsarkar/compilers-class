#include <dlfcn.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
  void (*greeting)();
  void *module;
  if( argc > 2 ) exit(0);
  module = dlopen(argv[1], RTLD_LAZY);
  if(!module) exit(0);
  greeting = dlsym(module, "greet");
  if(greeting) {
    (*greeting)();
  }
  dlclose(module);
}
