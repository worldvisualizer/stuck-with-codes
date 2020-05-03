// Section 3: Complex Data Types

struct fraction {
    int numerator;
    int denominator;
} // don't forget semicolons

struct fraction f1, f2;
f1.numerator = 22;
f1.denominator = 7;
f2 = f1; // this copies over the whole struct

// arrays
int scores[100];
score[0] = 13;
scores[99] = 42; 

int board[10][10];
board[0][0] = 1;
board[9][9] = 2;

struct fraction numbers[100];
numbers[0].numerator = 22;
numbers[0].denominator = 7;

// pointers
int* intPtr;
struct fraction *f1, *f2;
// multiple variables declared on one line,
// * should go on the right with the variable

// star is allowed to be anywhere between 
// the base type and the variable name
int *intPtr;
int * intPtr;
int* intPtr;

// pointer dereferencing
struct fraction* f1;

f1; // struct fraction pointer
*f1; // struct fraction
(*f1).numerator // int

// pointer to a pointer to a struct
struct fraction** fp;
// array of 20 struct fractions
struct fraction fract_array[20];
// array of 20 struct fraction pointers
struct fraction* fract_pointer_array[20];

// this circular definition problem is no problemo
struct node {
    int data;
    struct node* next;
}

// & operator computes a pointer location
// to argument in the right
void foo() {
    int* p;
    int i;
    p = &i;
    *p = 13;
}

// const NULL == 0, when assigned to pointer 
// represents nothing to point to.

/*
    in order for a pointer - pointee to work:
    1) pointer must be declared and allocated
    2) pointee must be declared and allocated
    3) pointer must be initialized to the pointee
*/

// c strings are char pointer or char array.
void code_block() {
    char string[1000]; // string is a local 1000 char array
    int len;
    strcpy(string, "binky");
    len = strlen(string);
    /*
     Reverse the chars in the string:
     i starts at the beginning and goes up
     j starts at the end and goes down
     i/j exchange their chars as they go until they meet
    */
    int i, j;
    char temp;
    for (i = 0, j = len - 1; i < j; i++, j--) {
        temp = string[i];
        string[i] = string[j];
        string[j] = temp;
    }
    // at this point the local string should be "yknib"
}

// typedef statement defines shorthand name for a type
typedef struct fraction Fraction;
Fraction fraction; // !!! macro yeah

typedef struct treenode* Tree;
struct treenode {
    int data;
    Tree smaller, larger;
} // equivalent to struct treenode *smaller, *larger;










