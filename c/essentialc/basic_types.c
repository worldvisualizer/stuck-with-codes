// Section 1: Basic Types and Operators

// Integer types
char c; // 8 bits = 1 byte
short sh; // 2 bytes
int i; // 4 bytes
long l;  // 4 bytes, with chance to be bigger

unsigned int ui; // disallows representing negatives

const int CONST_DEFAULT = 234;
const long CONST_LONG = 234L;
const int CONST_HEX = 0x1a;

int k = 234823784239; // very large number
long converted = (k * 1024L); // prevents overflow

float f; // 4 bytes, single precision 
double d; // 8 bytes, double precision
long double ld; // obscure

// this is possible
float x,y,z;

char ch;
int i;

i = 321;
ch = i; // ch is now 65 because of truncation
// removes most significant bit.

// common pitfalls when dividing in integer
int score;
score = (score / 20) * 100;
// score, when < 20, will be 0, so will always be 0.

// fix - casting
score = ((double)score / 20) * 100;
score = (score / 20.0) * 100;

// surprise, C does not have boolean type
i = 0;
while (i - 10) {
	// all non-zero values are true
	// 0 is false
}

// pre-, post- variations
// nesting a variable with the operator
// inside an expression.
int i = 42;
int j;

// i is incremented after expression finishes
j = (i++ + 10); // i = 43, j = 52, not 53;
// i is incremented before the expression starts
j = (++i + 10); // i = 44, j = 54










