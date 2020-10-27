#include <iostream>
#include <vector>

using namespace std;

const int LENGTH = 5;

int main() {
    vector<double> vec = {1.0, 2.3, 5.0, 3.0, 2.0, 3.7, 55.4};
    auto vecslice = vector<double>(vec.begin(), vec.begin() + LENGTH);
    for (int i = 0; i < vecslice.size(); i++)
        cout << vecslice[i];
}
