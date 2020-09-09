// this is cpp standard builtin
#include <cstdio>
// this is c builtin, represented by .h
#include <stdio.h>

// function overloading: each function should 
// take different parameters
void print(char const* myString) {
    printf("String %s\n", myString);
}

void print(int myInt) {
    printf("%d\n", myInt);
}

// dunno when, but cpp provides default parameter
void dosomething(int a = 1, int b = 4) {
    // do something
}

void rightdosomething(int a, int b = 4) {
    // default parameter should come at the end
}

namespace First {
    namespace Nested {
        void foo() {
            // do something            
        }
    }
}

namespace Second {
    void foo() {
        // do something as well, 
    } // this function is limited to here
}

void foo() {
    // this is global scope!
}

int main() {
    using namespace Second;
    // now let's see namescop in action
    Second::foo();
    First::Nested::foo();
    ::foo(); // simply foo() doesn't work, apparently
}


