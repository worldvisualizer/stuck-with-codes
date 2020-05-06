// Section 4: Functions

// C functions are defined in a text file and
// names of all the functions are lumped in a single namespace
// example
static int twice(int num) {
    int result = num * 3;
    result = result - num;
    return result;
}

// a pointer that does not point to any particular type
// is declared as void*

// call by reference
static void swap(int* x, int* y) {
    int temp;
    temp = *x;
    // use * to follow the pointer back to the caller's memory
    *x = *y;
    *y = temp;
}

int a = 1;
int b = 2;
swap(&a, &b);

// const
// primarily used in...
// clarify the role of a parameter in a function prototype
void foo(const struct fraction* fract);
// this prototype says that function foo() does not intend to
// change the struct fraction pointee

// example time
static void swap(int* a, int* b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

static void IncrementAndSwap(int* x, int* y) {
    (*x)++;
    (*y)++;
    swap(x, y);
}

int main() {
    int alice = 10;
    int bob = 20;
    swap(&alice, &bob);
    // at this point alice==20 and bob==10
    IncrementAndSwap(&alice, &bob);
    // at this point alice==11 and bob==21
    return 0;
}