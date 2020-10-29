#include <iostream>
#include <vector>

using namespace std;

vector<vector<double>> rotate_vector(vector<vector<double>> &original) {
    vector<vector<double>> lines;
    for (int i = 0; i < original[0].size(); i++) {
        vector<double> vertical_line;
        for (int j = 0; j < original.size(); j++) {
            vector<double> horizontal_read = original[j];
            vertical_line.push_back(horizontal_read[i]);
        }
        lines.push_back(vertical_line);
    }
    return lines;
}

int main() {
    vector<vector<double>> original = { {1,2,3,4}, {5,6,7,8}, {9,10,11,12}};
    auto lines = rotate_vector(original);
    for (int i = 0; i < lines.size(); i++) {
        vector<double> ll = lines[i];
        for (int j = 0; j < ll.size(); j++) {
            cout << ll[j] << ", ";
        }
        cout << endl;
        cout << "----------" << endl;
    }
}
