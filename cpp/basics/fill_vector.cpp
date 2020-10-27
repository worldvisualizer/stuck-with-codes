#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

const int LEN = 10;

int main() {
    vector<int> thevector(LEN);
    fill(thevector.begin(), thevector.begin() + LEN, 74883);

    cout << "myvector contains:";
    for (vector<int>::iterator it = thevector.begin(); it != thevector.end(); ++it)
        cout << ' ' << *it;
    cout << '\n';
}
