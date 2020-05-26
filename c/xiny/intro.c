// LearnXinYminutes.com, C


// constants: all-caps out of convention.
#define DAYS_IN_YEAR 365

// enum constants are also ways to declare constants.
enum days {SUN = 1, MON, TUE, WED, THU, FRI, SAT};
// MON gets 2 automatically

// import headers with #include
// <angle brackets> -> C standard library
// "my_header.h" -> user-defined library
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// declare function signatures in .h file or at the top of .c file
// must declare function prototype before main() 
// when functions occur after main() function
int add_two_ints(int x1, int x2);

void learnTypes() {
    ///////////////////////////////////////
    // Types
    ///////////////////////////////////////

    // Compilers that are not C99-compliant require that variables MUST be
    // declared at the top of the current block scope.
    // Compilers that ARE C99-compliant allow declarations near the point where
    // the value is used.
    // For the sake of the tutorial, variables are declared dynamically under
    // C99-compliant standards.

    int x_int = 0;
    short x_short = 0;

    char x_char = 0;
    char y_char = 'y';

    long x_long = 0;
    long long x_long_long = 0; // at least 8 bytes

    float x_float = 0.0f; // 32 bit
    double x_double = 0.0 // 64 bit

    unsigned short ux_short;
    unsigned int ux_int;
    unsigned long long ux_long_long;

    // If the argument for `sizeof` is expression,
    // then its argument is not evaluated
    int a = 1;
    size_t size = sizeof(a++); // a++ not evaluated
    printf("sizeof(a++) = %zu where a = %d\n", size, a);

    // If we have characters between single quotes, that's a character literal.
    // It's of type `int`, and *not* `char` (for historical reasons).
    int cha = 'a'; // fine
    char chb = 'a'; // fine too (implicit conversion from int to char)
}

void learnArrays() {
    // Arrays
    char char_array[20]; // 20 bytes
    int int_array[20]; // 80 bytes

    // You can initialize an array to 0 thusly:
    char my_array[20] = {0};
    // where the "{0}" part is called an "array initializer".
    // NOTE that you get away without explicitly declaring the size of the array,
    // IF you initialize the array on the same line. So, the following declaration
    // is equivalent:
    char my_array[] = {0};
    // BUT, then you have to evaluate the size of the array at run-time, like this:
    size_t my_array_size = sizeof(my_array) / sizeof(my_array[0]);
    // WARNING If you adopt this approach, you should evaluate the size *before*
    // you begin passing the array to function (see later discussion), because
    // arrays get "downgraded" to raw pointers when they are passed to functions
    // (so the statement above will produce the wrong result inside the function).

    // In C99 (and as an optional feature in C11), variable-length arrays (VLAs)
    // can be declared as well. The size of such an array need not be a compile
    // time constant:
    printf("Enter the array size: "); // ask the user for an array size
    int array_size;
    fscanf(stdin, "%d", &array_size);
    int var_length_array[array_size]; // declare the VLA
    printf("sizeof array = %zu\n", sizeof var_length_array);

    // strings are arrays of chars terminated by NULL (0x00) byte
    char a_string[20] = "This is a string";
    printf("%s\n", a_string);
    printf("%d\n", a_string[16]); // 0.

    // Multi-dimensional arrays:
    int multi_array[2][5] = {
        {1, 2, 3, 4, 5},
        {6, 7, 8, 9, 0}
    };
    // access elements:
    int array_int = multi_array[0][2]; // => 3 
}

void learnLogicalOperators() {
    // there is no Boolean type in C. We use ints instead.
    // (Or _Bool or bool in C99.)
    // 0 is false, anything else is true. (The comparison
    // operators always yield 0 or 1.)
    3 == 2; // => 0 (false)
    3 != 2; // => 1 (true)
    3 > 2; // => 1
    3 < 2; // => 0
    2 <= 2; // => 1
    2 >= 2; // => 1

    // C is not Python - comparisons don't chain.
    // Warning: The line below will compile, but it means `(0 < a) < 2`.
    // This expression is always true, because (0 < a) could be either 1 or 0.
    // In this case it's 1, because (0 < 1).
    int between_0_and_2 = 0 < a < 2;
    // Instead use:
    int between_0_and_2 = 0 < a && a < 2;

    // Logic works on ints
    !3; // => 0 (Logical not)
    !0; // => 1
    1 && 1; // => 1 (Logical and)
    0 && 1; // => 0
    0 || 1; // => 1 (Logical or)
    0 || 0; // => 0
}

void learnGeneralOperators() {
    // Conditional ternary expression ( ? : )
    int e = 5;
    int f = 10;
    int z;
    z = (e > f) ? e : f; // => 10 "if e > f return e, else return f."

    // Increment and decrement operators:
    int j = 0;
    int s = j++; // Return j THEN increase j. (s = 0, j = 1)
    s = ++j; // Increase j THEN return j. (s = 2, j = 2)
    // same with j-- and --j

    // Bitwise operators!
    ~0x0F; // => 0xFFFFFFF0 (bitwise negation, "1's complement" for int)
    0x0F & 0xF0; // => 0x00 (bitwise AND)
    0x0F | 0xF0; // => 0xFF (bitwise OR)
    0x04 ^ 0x0F; // => 0x0B (bitwise XOR)
    0x01 << 1; // => 0x02 (bitwise left shift (by 1))
    0x02 >> 1; // => 0x01 (bitwise right shift (by 1))

    // Be careful when shifting signed integers
    // the following are undefined:
    // - shifting into the sign bit of a signed integer (int a = 1 << 31)
    // - left-shifting a negative number (int a = -1 << 2)
    // - shifting by an offset which is >= the width of the type of the LHS:
    //   int a = 1 << 32; // UB if int is 32 bits wide
}

void learnControls() {
    // Loops and Functions MUST have a body. If no body is needed:
    int i;
    for (i = 0; i <= 5; i++) {
    ; // use semicolon to act as the body (null statement)
    }
    // Or
    for (i = 0; i <= 5; i++);

    // goto statements in C:
    typedef enum { false, true } bool;
    // for C don't have bool as data type before C99:
    bool disaster = false;
    int i, j;
    for (i = 0; i < 100; ++i) {
        for (j = 0; j < 100; ++j) {
            if ((i + j) >= 150) {
                disaster = true;
            }
            if (disaster) {
                goto error;
            }
        }
    }
    error:
    printf("Error occurred at i = %d and j %d\n", i, j);
}

void learnTypeCasting() {
    // Typecasting
    int x_hex = 0x01;

    // casting tries to preserve numeric values
    printf("%d\n", x_hex); // 1
    printf("%d\n", (short) x_hex); // 1
    printf("%d\n", (char) x_hex); // 1

    // types will overflow without warning
    printf("%d\n", (unsigned char) 257); // 1

    // Integral types can be cast to floating-point types, and vice-versa.
    printf("%f\n", (double) 100); // %f always formats a double...
    printf("%f\n", (float)  100); // ...even with a float.
    printf("%d\n", (char)100.0);
}

void learnPointers() {
    int x = 888;
    int *px, not_a_pointer;
    px = &x;
    printf("%p\n", (void *)px); // => Prints some address in memory
    printf("%zu, %zu\n", sizeof(px), sizeof(not_a_pointer)); // 8, 4
    printf("%d\n", *px); // 888, value of x.

    // You can also change the value the pointer is pointing to.
    // We'll have to wrap the dereference in parenthesis because
    // ++ has a higher precedence than *.
    (*px)++; // Increment the value px is pointing to by 1
    printf("%d\n", *px); // 889
    printf("%d\n", x); // 889

    // TODO: continued rambling about pointers
}

void learnExtern() {
    // if referring to external variables outside function, you should use the extern keyword.
    int i = 0;
    void testFunc() {
        extern int i; //i here is now using external variable i
    }

    // make external variables private to source file with static:
    static int j = 0; //other files using testFunc2() cannot access variable j
    void testFunc2() {
        extern int j;
    }
    // static makes variable inaccessible outside of the file.
}

void learnTypeDef() {
    // user-defined types and structs

    // type alias possible
    typedef int my_type;
    my_type my_type_var = 0;

    struct rectangle {
        int width;
        int height;
    };

    // but sizeof(rectangle) != sizeof(int) + sizeof(int)
    // because of the possible padding.

    // this typedef inside a function is possible,
    // and this rect is limited to local scope
    typedef struct rectangle rect;
}

// lexical scoping is not possible in C
// because compiler cannot reach/find the memory location
// of the inner function.
void function_1() {
    struct rectangle my_rec;

    // Access struct members with .
    my_rec.width = 10;
    my_rec.height = 20;

    // You can declare pointers to structs
    struct rectangle *my_rec_ptr = &my_rec;

    // Use dereferencing to set struct pointer members...
    (*my_rec_ptr).width = 30;

    // ... or even better: prefer the -> shorthand for the sake of readability
    my_rec_ptr->height = 10;
    // Same as (*my_rec_ptr).height = 10;
}

int area(rect r) {
    return r.width * r.height;
}

int areaptr(const rect *r) {
    return r-> width * r->height;
}

// at runtime, functions are located at known memory addrs
// function pointers can be used to invoke functions
// directly, and to pass handlers or callbacks.
void str_reverse_through_pointer(char* str_in) {
    // define function pointer variable named f.
    void (*f)(char *); // signature should match target func.
    f = &str_reverse; // assign the address.
    f = str_reverse; // this works as well
    // because function wraps as pointers at runtime

    (*f)(str_in); // calling the function through the pointer
}

// function pointers are usually typedef'd for simplicity
typedef void (*my_fnp_type)(char *);
// Then used when declaring the actual pointer variable:
// ...
// my_fnp_type f;

int main(int argc, char** argv) {
    printf("%d\n", 0);
    learnBasicPrimitives();
    learnArrays();
    learnLogicalOperators();
    learnGeneralOperators();
    learnControls();
    learnTypeCasting();
    learnPointers();
    learnFuncPointers();
}