#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class InputParser {
    public:
        InputParser(int &argc, char **argv) {
            for (int i = 1; i < argc; ++i)
                this->tokens.push_back(std::string(argv[i]));
        }
        
	const string& getCmdOption(const string &option) const {
            vector<string>::const_iterator itr;
            itr = find(this->tokens.begin(), this->tokens.end(), option);
            if (itr != this->tokens.end() && ++itr != this->tokens.end()) {
                return *itr;
            }
            static const string empty_string("");
            return empty_string;
        }
        
	bool cmdOptionExists(const string &option) const {
            return find(this->tokens.begin(), this->tokens.end(), option)
                   != this->tokens.end();
        }
    
    private:
        vector <string> tokens;
};

int main(int argc, char **argv) {
    InputParser input(argc, argv);
    if(input.cmdOptionExists("-h")) {
	const string &host = input.getCmdOption("-h");
	cout << "option h specified" << endl;
	cout << host << endl;
    }
    const string &filename = input.getCmdOption("-f");
    if (!filename.empty()) {
        cout << filename << endl;
    }
    return 0;
}
