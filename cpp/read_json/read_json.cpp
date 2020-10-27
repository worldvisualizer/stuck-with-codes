#include <nlohmann/json.hpp>
#include <iostream>
#include <fstream>

using namespace std;
using json = nlohmann::json;

json read_json(string filepath) {
    ifstream i(filepath);
    json j;
    i >> j;
    return j;
}

int main() {
    cout << "hello!" << endl;
    auto j = read_json("coeff.json");
    auto coef = j["coef"];
    int i = 0;
    for (auto &array : coef) {
	cout << "printing label " << i << "th's coeffs:" << endl;;
	int j = 0;
	for (auto &elem : array) {
	    if (j == 20) {
		break;
	    }
	    cout << elem << " ";
	    j++;
	}
	cout << endl;
	i++;
    }
}
