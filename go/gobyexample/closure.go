package main 

import "fmt"

func intSeq() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}
// I am like shit, wat, 
// but function returned has variable i

func main() {
	nextInt := intSeq() // old scope.
	// but how does Go know that intSeq() is being referenced?
	// so new instance of function is being created

	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())

	newInts := intSeq() // new scope
	fmt.Println(newInts())
}