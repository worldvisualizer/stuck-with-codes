#include <NTL/ZZ.h>

using namespace std;
using namespace NTL;

ZZ powerModNaive(const ZZ& a, const ZZ& e, const ZZ& n) {
   if (e == 0) return ZZ(1);

   long k = NumBits(e);

   ZZ res;
   res = 1;

   for (long i = k-1; i >= 0; i--) {
      res = (res*res) % n;
      if (bit(e, i) == 1) res = (res*a) % n;
   }

   if (e < 0)
      return InvMod(res, n);
   else
      return res;
}

int main() {
    ZZ a, e, n;

    a = 100000000;
    e = 23;
    n = 2;

    cout << powerModNaive(a, e, n) << endl;
}
