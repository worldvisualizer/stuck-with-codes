// cpp templating: generic programming

// define a class or function that takes a type parameter
// template<typename T> is also applicable here,
// see: https://en.wikipedia.org/wiki/Typename
template<class T>
class Box {
public:
    void insert(const T&) { // ...
        // ...
    }
};

int main() {
    Box<int> intBox;
    intBox.insert(123);

    // from cpp11, this >> syntax is possible
    // before that it would have been a right shift operator
    Box<Box<int>> boxOfBox;
    boxOfBox.insert(intBox);
}

// template function
template<class T>
void barkThreeTimes(const T& input) {
    input.bark();
    input.bark();
    input.bark();
    // how does the compiler guarantee type 
    // of input parameter?
    // it checks invocation of barkThreeTimes()
}

Dog fluffy;
fluffy.setName("fluffy");
barkThreeTimes(fluffy);

// template parameters can also be built-in types
template<int Y>
void printMessage() {
    cout << "Learn Cpp in " << Y << " minutes" << endl;
}

// and doing this is... also possible!
template<>
void printMessage<10>() {
    cout << "Learn Cpp faster in 10 minutes" << endl;
}
printMessage<20>(); // Learn cpp in 20 minutes
printMessage<10>(); // Learn cpp faster in 10 minutes
// so this is a hardcoded function invocation,
// working around the template invocation



