// LearnXinYminutes.com, Cpp

// C++ is almost a superset of C and shares its basic syntax
// for variable declarations, primitive types, functions.

int main(int argc, char** argv) {
    // command line arguments
    // argc == number of arguments
    // argv == array of c-style strings
    return 0; // exit status
}

// in C++, char literals are chars, in C, it's integers
sizeof('c') == sizeof(char) == 1
// in C
// sizeof('c') == sizeof(int) == 4

// C++ has strict prototyping
void func();

// In C
void func(); // function may accept any number of arguments