int sqr(int x) {
  if (x > 1) {
    x = sqr(x-1)+x+x-1;
  }
  return x;
}

int main() {
  sqr(10);
}
