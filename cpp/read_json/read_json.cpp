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
    cout << j << endl;

}
