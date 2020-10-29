#include <map>
#include <iostream>
#include <string>
#include <nlohmann/json.hpp>
#include <fstream>
#include <vector>

using namespace std;
using json = nlohmann::json;

json read_json(string filepath) {
    ifstream i(filepath);
    json j;
    i >> j;
    return j;
}

map<int, string> read_label_mapping(string filepath) {
    auto labels = read_json(filepath);
    map<int, string> label_map;
    for (auto it = labels.begin(); it != labels.end(); ++it) {
        auto index = stoi(it.key());
        auto value = it.value();
        if (label_map.find(index) != label_map.end()) {
            cout << "label exists!?" << endl;
        } else {
            label_map[index] = value;
        }
    }
    return label_map;
}

vector<string> get_values_from_map(map<int, string> &label_map) {
    vector<string> headers;
    for (auto it = label_map.begin(); it != label_map.end(); it++) {
        headers.push_back(it->second);
    }
    return headers;
}

int main() {
    cout << "hello!" << endl;
    auto label_map = read_label_mapping("label_mapping.json");
    auto vec = get_values_from_map(label_map);
    for (size_t ind = 0; ind < vec.size(); ind++) {
        cout << vec[ind] << endl;
    }
    map<int, string>::iterator it = label_map.find("3");
    cout << "Key: " << it->first << " Value: " << it->second << endl;
}
