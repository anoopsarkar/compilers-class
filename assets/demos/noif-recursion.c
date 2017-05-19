#include <stdio.h>

double (*farr[2])();

double _fact(double n) {
	if (n == 1) { return 1; }
	else { return n * _fact(n-1); }
}

double bot(double n) {
	return 1;
}

double fact(double n) {
	return n*(*farr[n>1])(n-1);
}

int main() {
	farr[0] = &bot;
	farr[1] = &fact;

	printf("%f\n", fact(9));
	printf("%f\n", _fact(9));
	return 0;
}
