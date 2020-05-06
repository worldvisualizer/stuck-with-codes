// Section 5: Odds and Ends

// prototypes
int twice(int num);
void swap(int* a, int* b);

// in ANSI C,
// 1) static function can only be used in the same file.
//    it can be called below its point of declaration.
//    does not need prototype.

// 2) non-static function needs a prototype.
//    ("prototype before definition" rule).

// preprocessor
// 1) #define: set up symbolic replacements in the source
#define MAX 100
#define SEVEN_WORDS that_symbol_expands_to_all_these_words

// 2) #include: pastes the text from the file
#include "foo.h" // user-defined foo.h file in the origin dir
#include <foo.h> // system foo.h file somewhere in compiler dir

// .h (header file) contains prototypes for .c file. 
// .c file contains:
#include "mymodule.h" // ensures "prototype before definition" rule
// any xxx.c file which wishes to call a function defined in foo.c
// must include: (clients must see prototypes)
#include "foo.h"

// weird feature to preprocessor
#define FOO 1

#if FOO
    #define FOO1 23232
    #define FOO2 89898
#else
    #define FOO1 44444
    #define FOO2 'aaaaa'
#endif
// if FOO from #define == true, then if code block gets compiled
// if not, else section code block gets compiled.
// so in above, FOO1 == 23232.

// <inside foo.h>
// The following line prevents problems of extra imports
// in files which #include "foo.h"
#pragma once

// assert
#include <assert.h>
#define MAX_INTS 100
int[] main() {
    int ints[MAX_INTS];
    i = foo(<something complicated>); // i should be in bounds,
    // but is it really?
    assert(i >= 0); // safety assertions
    assert(i < MAX_INTS);
    ints[i] = 0;
    return ints;
}










