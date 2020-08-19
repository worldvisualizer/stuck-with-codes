// LearnXinYminutes.com, Cpp

// cpp is almost a superset of C and shares its basic syntax
// for variable declarations, primitive types, functions.
int main(int argc, char** argv) {
    // in cpp, char literals are chars, in C, it's integers
    sizeof('c') == sizeof(char) == 1
    // in c
    // sizeof('c') == sizeof(int) == 4

    // cpp has strict prototyping
    void func(); // must mean that the function declaration syntax is strict

    // In c
    void func(); // function may accept any number of arguments, unlike above

    // in cpp, use null pointer instead of null itself
    int *ip = nullptr;

    // command line arguments
    // argc == number of arguments
    // argv == array of c-style strings
    return 0; // exit status
}

// enums
enum CarTypes {
    Sedan,
    Hatchback,
    SUV,
    Wagon
};

CarTypes GetPreferredCarType() {
    return CarTypes::Hatchback;
}

// as of cpp11 there's an easy way to assign a type to the enum
// which can be useful in serialization of data and converting 
// enums back-and-forth between the desired type and their respective constants
enum CarTypes : uint8_t {
    Sedan, // 0
    Hatchback, // 1
    SUV = 254,
    Hybrid // 255
};

void WriteByteToFile(uint8_t InputValue) {
    // serialize the InputValue to a file
}

void WritePreferredCarTypeToFile(CarTypes InputCarType) {
    // enum is implicitly converted to a uint8_t type due to declared enum
    WriteBtyeToFile(InputCarType);
}

enum class CarTypes : uint8_t {
    Sedan,
    Hatchback,
    SUV = 254,
    Hybrid
}; // no accidental casting to an integer types or other enums,
// and the way to do that is: "enum class"