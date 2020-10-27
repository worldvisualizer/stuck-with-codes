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
            row.push_back(stoi(lineStream, &sz, 10)); // convert to double
        } catch (invalid_argument& e) {
            cout << e.what() << " original input " << lineStream << endl;
        }
    }
    return row;
}

int read_csv(
    vector<string> &headers,
    vector<vector<int>> &lines,
    vector<string> &caseIds,
    const string &relativePath,
    const string &filename,
    bool vertical_read
) {   
    ifstream csvFile;
    string strPathCSVFile = relativePath + '/' + filename;
    csvFile.open(strPathCSVFile.c_str());

    if (!csvFile.is_open()) {
        cout << "Path is wrong" << endl;
        exit(EXIT_FAILURE);
    }

    int linecount = 0;
    vector<vector<int>> reads;
    string line;
    getline(csvFile, line);
    headers = read_header(line);
    while (getline(csvFile, line)) {
        if (line.empty())
            continue;
	linecount++;
        reads.push_back(read_normal_line(caseIds, line));
    }

    if (vertical_read) {
       for (int i = 0; i < reads[0].size(); i++) {
	   vector<int> vertical_line;
           for (int j = 0; j < reads.size(); j++) {
	       vector<int> horizontal_read = reads[j];
	       vertical_line.push_back(horizontal_read[i]);
           }
	   lines.push_back(vertical_line);
       }
    } else {
	lines = reads;
    }
    return linecount;
}

int main(int argc, const char **argv) {
    vector<string> headers;
    vector<string> caseIds;
    vector<vector<int>> features;
    int casecount = read_csv(headers, features, caseIds, argv[1], argv[2], true);

    for (size_t j = 0; j < caseIds.size(); j++) {
        cout << caseIds[j] << ",";
    }
    for (size_t i = 0; i < features.size(); i++) {
        vector<int> line = features[i];
        for (size_t j = 0; j < line.size(); j++) {
            cout << line[j] << ",";
        }
        cout << line.size() << endl;
    }

    cout << "--------------------------------" << endl;
    cout << "number of cases: " << casecount << endl;
    return 0;
}
