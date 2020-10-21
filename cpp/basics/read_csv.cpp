#include <string>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

vector<string> read_header(const string line) {
    vector<string> row;
    istringstream iss(line);
    string lineStream;
    string::size_type sz;
    while (getline(iss, lineStream, ',')) {
        row.push_back(lineStream);
     }
    return row;
}

vector<int> read_normal_line(vector<string> &caseIds, const string line) {
    vector<int> row;
    istringstream iss(line);
    string lineStream;
    string::size_type sz;
    bool firstChunk = true;

    while (getline(iss, lineStream, ',')) {
        if (firstChunk) {
            caseIds.push_back(lineStream);
            firstChunk = false;
            continue;
        }
        try {
            row.push_back(stoi(lineStream, &sz, 10)); // convert to int
        } catch (invalid_argument& e) {
            cout << e.what() << " original input " << lineStream << endl;
        }
    }
    return row;
}

void read_csv(
    vector<string> &headers, vector<vector<int>> &lines,
    vector<string> &caseIds,
    const string &relativePath, const string &filename
) {   
    ifstream csvFile;
    string strPathCSVFile = relativePath + '/' + filename;
    csvFile.open(strPathCSVFile.c_str());

    if (!csvFile.is_open()) {
        cout << "Path is wrong" << endl;
        exit(EXIT_FAILURE);
    }
    string line;
    getline(csvFile, line);
    headers = read_header(line);
    while (getline(csvFile, line)) {
        if (line.empty())
            continue;
        lines.push_back(read_normal_line(caseIds, line));
    }
}

int main(int argc, const char **argv) {
    vector<string> headers;
    vector<string> caseIds;
    vector<vector<int>> features;
    read_csv(headers, features, caseIds, argv[1], argv[2]);

    for (size_t j = 0; j < caseIds.size(); j++) {
        cout << caseIds[j] << ",";
    }
    for (size_t i = 0; i < features.size(); i++) {
        vector<int> line = features[i];
        for (size_t j = 0; j < line.size(); j++) {
            cout << line[j] << ",";
        }
        cout << endl;
    }

    cout << "--------------------------------" << endl;
    return 0;
}
