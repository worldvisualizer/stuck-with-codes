#include <iostream>
#include <math.h>

using namespace std;

double fact(int c) {
   int factorial = 1;
   for (int i = 1; i <= c; i++) {
      factorial *= i;
   }
   return factorial;
}

double taylor_expansion(double x, int n) {
    double approx;
    double sum;
    double value;
    for (int i = 1; i <= n; i++) {
        sum=((pow(x, i)) / fact(i));
        value += sum;
    }
    approx = 1 + value;
    return approx;
}

double exp_approx(double x, int n) {
    return taylor_expansion(x, n);
}

int main() {
    for (int i = 0; i < 10; i++) {
	for (int j = 0; j < 20; j++) {
	    double result = exp_approx(i, j);
	    cout << "number x: " << i << " number of power: " << j << " result: " << result << " exp(x): " << exp(i) << " diff: " << exp(i) - result << endl;
	}
    }
}
