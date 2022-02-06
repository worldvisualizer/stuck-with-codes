#include <NTL/ZZ.h>

// way to compile
// g++ -g -O2 -std=c++11 -pthread -march=native foo.cpp -o foo -lntl -lgmp -lm

using namespace std;
using namespace NTL;

int main() {
    ZZ a, b, c;

    cin >> a;
    cin >> b;
    c = (a + 1) * (b + 1);
    cout << c << "\n";
}
