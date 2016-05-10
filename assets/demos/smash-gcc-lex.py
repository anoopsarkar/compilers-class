import sys
if __name__ == "__main__":
  n = sys.maxint / 2
  if len(sys.argv) > 1:
    n = int(sys.argv[1])
  print >>sys.stderr, "using n =", n
  sys.stdout.write("int main() { int ")
  #for i in xrange(n): sys.stdout.write('x')
  sys.stdout.write('x' * n)
  sys.stdout.write(" = 1; }")
  print

