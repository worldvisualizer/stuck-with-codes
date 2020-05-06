// Section 6: Advanced Arrays and Pointers

// well known fact about array:
// address of nth element = address_of_0th_element 
//     + (n * element_size_in_bytes)
int intArray[6];
int* offset = (intArray + 3); // is a pointer
int* offset2 = &(intArray[3]); // same expression

// char* example:
// objective: implement strcpy, don't forget about copying \0
void strcpy1(char dest[], const char source[]) {
    int i = 0;
    while (1) {
        dest[i] = source[i];
        if (dest[i] == '\0') break; // we're done
        i++;
    }
}

// Move the assignment into the test
void strcpy2(char dest[], const char source[]) {
    int i = 0;
    while ((dest[i] = source[i]) != '\0') {
        i++;
    }
}

// Get rid of i and just move the pointers.
// Relies on the precedence of * and ++.
void strcpy3(char dest[], const char source[]) {
    while ((*dest++ = *source++) != '\0');
}

// Rely on the fact that '\0' is equivalent to FALSE
void strcpy4(char dest[], const char source[]) {
    while (*dest++ = *source++);
}

// pointer type effects
int *p;
p = p + 12;
// code increments p by 12 ints, not 12 bytes. so 48 bytes.
// compiler figures it out based on the type of the pointer

p = (int*) ( ((char*)p) + 12); // this just adds 12 bytes.

// what is the difference between intArray and intPtr?
// none, as far as the compiler is concerned.

int intArray[6];
int *intPtr;
int i;
intPtr = &i;
intArray[3] = 13; // ok
intPtr[0] = 12; // odd, but ok. Changes i.
intPtr[3] = 13; // BAD! There is no integer reserved here!


// array base address behaves like a const pointer.

// malloc(), and dynamic arrays
/*
    void* malloc(size_t size);
    - returns NULL if unsuccessful.
    void free(void* block);
    void* realloc(void* block, size_t size);
    - returns NULL if unsuccessful.
*/

int a[1000];
int *b;
b = (int*) malloc(sizeof(int) * 1000);
assert(b != NULL); // check that the allocation succeeded
a[123] = 13; // Just use good ol' [] to access elements
b[123] = 13; // in both arrays.
// so really no difference between array and pointer.
b = realloc(b, sizeof(int) * 2000);
// reallocation is possible
free(b);
// The array will exist until it is explicitly deallocated
// with a call to free().


/*
 Takes a c string as input, and makes a copy of that string
 in the heap. The caller takes over ownership of the new string
 and is responsible for freeing it.
*/
char* makeStringInHeap(const char* source) {
    char* newString;
    newString = (char*) malloc(strlen(source) + 1);
    // +1 for the '\0'
    assert(newString != NULL);
    strcpy(newString, source);
    return newString;
}