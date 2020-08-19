// input / output

#include <iostream>
#include <string>

using namespace std;

void inputOutput() {
    int myint;

    cout << "receiving input for the favorite number";
    cin >> myint;

    cout << "favorite number is: " << myint;
    cerr << "stderr pipe";
}

void strings() {
    string str1 = "hello";
    string str2 = "world";

    cout << str1 + str2;
    str1.append(" you!"); // cpp strings are mutable
}

string tempObjectFun() {
    // ...
}

// references
void references() {
    // cpp has _references_ instead of pointers in c.
    // These are pointer types that cannot be reassigned once set
    // and cannot be null.
    // They also have the same syntax as the variable itself:
    // No * is needed for dereferencing and
    // & (address of) is not used for assignment.
    string foo = "I am foo";
    string bar = "I am bar";

    string& fooRef = foo;
    fooRef += ". Hi!";
    cout << fooRef;

    cout << &fooRef << endl; // address of foo
    fooRef = bar; // now pointer is not reassigned, and since *
    // is not needed for dereferencing, foo is reassigned to bar.
    // aha.
    cout << &fooRef << endl; // still the address of foo
    cout << fooRef; // print "i am bar"

    const string& barRef = bar; // const reference to bar
    // most values including pointers and references cannot be modified
    barRef += ". Hi!";
    
    string retVal = tempObjectFun();
    // return value -> new string(return value) -> return value destroyed 
    foo(bar(tempObjectFun()))
}

void constReferenceTempObjectFun() {
    // constRef gets the temporary object and it is valid until 
    // the end of the function
    const string& constRef = tempObjectFun();
}

// another kind of reference introduced in C++ is specifically for
// temporary objects.
// you cannot have a variable of it type, but it takes precedence
// in overload resolution
void someFun(string& s) {
    // ... regular reference
}

void someFun(string&& s) {
    // ... reference to temporary object
}

string foo;
someFun(foo); // calls the version with regular reference
someFun(tempObjectFun()); // calls the version with temporary reference

// std::basic_string:
basic_string(const basic_string& other);
basic_string(basic_string&& other);

// Idea being if we are constructing a new string from a temporary object (which
// is going to be destroyed soon anyway), we can have a more efficient
// constructor that "salvages" parts of that temporary string. You will see this
// concept referred to as "move semantics".
