package main 

import "fmt"

// multiple return values
func vals() (int, int) {
	return 3, 7
}

func main() {
	a, b := vals()
	fmt.Println(a, b)

	_, c := vals()
	fmt.Println(c)
}