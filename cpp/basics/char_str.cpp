#include <iostream>

using namespace std;


void char_array() {
    char arr[6] = "Hello";
    // compilation error
    // char arr2[5] = "Hello";
    cout << arr << endl;
}

void char_pointer() {
    // str is a pointer to a const string literal.
    char* str = "Jungho";
    cout << str << endl;

    // Internally, string is represented as:
    // J|u|n|g|h|o|\0 (NULL) <- 7 bytes in total
    // https://en.cppreference.com/w/cpp/string/byte
    // For example, the character array {'\x63', '\x61', '\x74', '\0'}
    // is an NTBS holding the string "cat" in ASCII encoding.
    
    // char pointer is pointing to letter J.
    // compilation warning: type of &str[0] is coerced into char pointer 
    char* ptr = &str[0];    // = str
    cout << ptr << endl;    // Jungho
    cout << *(ptr+1) << endl;   // u
    // knows ungho because there's \0 at the end.
    cout << ptr+2 << endl;  // ungho
}

int main() {
    char_array();
    char_pointer();
}
