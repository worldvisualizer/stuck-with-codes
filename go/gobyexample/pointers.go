package main 

import "fmt"

func zeroval(ival int) {
	// pass by value copied
	ival = 0
}

func zeroptr(iptr *int) {
	// pass by reference
	*iptr = 0
}

func main() {
	i := 1
	fmt.Println("initial: ", i)

	zeroval(i)
	fmt.Println("zeroval: ", i) // nothing changes

	zeroptr(&i)
	fmt.Println("zeroptr: ", i) // value changes

	fmt.Println("pointer: ", &i) // pointer address
	// so, same as C and C++
}