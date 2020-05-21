// +build prod, dev, test

package main

import (
	"fmt"
	"io/ioutil"
	m "math"
	"net/http"
	"os"
	"strconv"
)

func main() {
	fmt.Println("Hello World")

	// call another function in this package
	beyondHello()
}

func beyondHello() {
	var x int                        // declaration
	x = 3                            // assignment
	y := 4                           // type inference
	sum, prod := learnMultiple(x, y) // function returns two vals
	fmt.Println("sum:", sum, "prod:", prod)
	learnTypes()
}

func learnMultiple(x, y int) (sum, prod int) {
	return x + y, x * y
}

func learnTypes() {
	str := "Learn Go!"
	s2 := `Raw String can have line 
breaks`
	g := 'Σ' // rune type, an alias for int32, holds a unicode code point.
	f := 3.14195
	c := 3 + 4i

	// var syntax with initializers
	var u uint = 7
	var pi float32 = 22. / 7 // that dot is okay.

	// conversion syntax with a short declaration
	n := byte('\n')

	// arrays have size fixed at compile time
	var a4 [4]int                // initialized all to 0
	a5 := [...]int{3, 1, 5, 100} // array literal

	// arrays have value semantics
	a4_cpy := a4                    // copied, not reference
	a4_cpy[0] = 25                  // further evidence that a4_cpy is copied
	fmt.Println(a4_cpy[0] == a4[0]) // false

	// slices have dynamic size.
	// slices use case is much more common
	s3 := []int{4, 5, 9}
	s4 := make([]int, 4)    // allocates slice of 4 ints, init to 0
	var d2 [][]float64      // declaration only. nothing allocated.
	bs := []byte("a slice") // type conversion syntax.

	// slices have reference semantics
	s3_cpy := s3 // both variables point to same instance
	s3_cpy[0] = 0 // both are updated
	fmt.Println(s3_cpy[0] == s3[0]) // true

	// slices: dynamic, appended to on-demand possible.
	s := []int{1,2,3}
	s = append(s, 4, 5, 6)
	// this is arguments to variadic functions
	s = append(s, []int{7,8,9}...) // second argument is slice literal.

	// maps: dynamically growable associative array type
	m := map[string]int{"three": 3, "four": 4}
	m["one"] = 1

	// how to handle unused variables
	_, _, _ = str, s2, g
	file, _ := os.Create("output.txt") // go convention to have error as well
	fmt.Fprint(file, "how to write to a file")
	file.Close()

	p, q := learnMemory()
	fmt.Println(*p, *q) // pointer dereferencing

	zzz := learnNamedReturns(*p, *q)
	fmt.Println(zzz)

	learnFlowControl()
}

// named returns. assigning a name to the type being returned
// in the function declaration line makes it easy to return 
// from multiple points in a function as well as to 
// only use return keyword
func learnNamedReturns(x, y int) (z int) {
	z = x * y
	return // returns z, because we already mentioned it above
}

// go is fully garbage collected. It has pointers but
// no pointer arithmetic. you can make a mistake with a nil pointer
// unlike c/cpp, taking and returning an address of local variable
// is also safe.
func learnMemory() (p, q *int) {
	p = new(int) // allocates memory.
	s := make([]int, 20) // allocates 20 ints, single block memory
	s[3] = 7
	r := -2
	return &s[3], &r // & takes address of an object
	// probably reference count created
}

func expensiveComputation() float64 {
    return m.Exp(10)
}

func learnFlowControl() {
	if true { // does not need parens
		fmt.Println("told ya")
	}
	if false {
		// pass
	} else {
		// pass
	}

	x := 42.0
	switch x {
	case 0:
	case 1,2:
	case 42:
		// cases do not fall through
	case 43:
		// unreached
	default: // optional
	}

	// Type switch allows switching on the type of something instead of value
    var data interface{}
    data = ""
    switch c := data.(type) {
    case string:
        fmt.Println(c, "is a string")
    case int64:
        fmt.Printf("%d is an int64\n", c)
    default:
        // all other cases
    }

    for x := 0; x < 3; x++ {
    	fmt.Println("iteration", x)
    }

    for { // this is actually without condition, so infinite loop
    	break
    	continue // unreached
    }

    // range returns one (channel) or two values
    for key, value := range map[string]int{"one": 1, "two": 2, "three": 3} {
    	fmt.Printf("key=%s, value=%d\n", key, value) // string interpolation
    }

    // if only need the value, don't use key
    for _, name := range []string{"Bob", "Bill", "Joe"} {
    	fmt.Printf("Hello %s\n", name)
    }

    // assignment and test in if
    if y:= expensiveComputation(); y > x {
    	x = y
    }

    // function literals are closures
    xBig := func() bool {
    	return x > 10000 // this does not error, because 
    	// x is already declared above, in line 131.
    }
    x = 99999 // now, this is outer variable.
    // closure hard at work.
    fmt.Println("xBig:", xBig())
    x = 1.3e3
    fmt.Println("xBig:", xBig())

    // function literals may be defined and called inline,
    // acting as an argument to function, as long as:
    // 1) function literal is called immediately
    // 2) result type matches expected type of an argument

    fmt.Println("Add + Double two numbers: ",
    	func(a, b int) int {
    		return (a + b) * 2
    	}(10, 2))

    // goto statement:
    goto love
    love:
    learnFunctionFactory()
    learnDefer()
    learnInterfaces()
}
