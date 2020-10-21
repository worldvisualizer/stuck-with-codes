#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void write_header(
    const vector<string> &headers, ofstream &csvfile
) {
    for (const auto &elem : headers)
        csvfile << elem << ",";
    csvfile << "\n";
}

void write_line(
    const vector<long double> &label, 
    const string &caseId, ofstream &csvfile
) {
    csvfile << caseId << ",";
    for (const auto &elem : label)
        csvfile << elem << ",";
    csvfile << "\n";
}

void write_csv_file(
    const vector<string> &headers,
    const vector<vector<long double>> &labels,
    const vector<string> &caseIds,
    const string &relativePath,
    const string &filename
) {
    ofstream csvfile;
    csvfile.open(relativePath + "/" + filename);
    if (csvfile.is_open()) {
        write_header(headers, csvfile);
        for (int i = 0; i < caseIds.size(); i++)
            write_line(labels[i], caseIds[i], csvfile);
        csvfile.close();
    } else {
        cout << "csv file is not open" << endl;
    }
}

int main( int argc, char* argv[] ) {
    vector<string> headers = { "cat", "dog", "hooman" };
    vector<vector<long double>> labels = { { 0.1, 0.2, 0.7 }, { 0.3, 0.4, 0.2 } };
    vector<string> caseIds = { "TCGA-AD", "TCGA-FE" };
    write_csv_file(headers, labels, caseIds, "postprocess", "out.csv");
    return 0;
}