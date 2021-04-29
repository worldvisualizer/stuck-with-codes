#include<iostream>

using namespace std;

int main() {
    for (int i = 0; i < 4; i++) {
        char ch;
        int row = i;
        int col = i + 1;
        cout << "input the letter (row : "<< row << ", column : " << col << ") : ";
        cin >> ch;
        cout << "RESULT : " << ch << endl;
    }
}
