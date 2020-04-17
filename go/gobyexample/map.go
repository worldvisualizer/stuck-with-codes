package main 

import "fmt"

func main() {
	m := make(map[string]int) // wtf man 

	// why make() is good:
	// Things you can do with make that you can't do any other way:

	//	Create a channel
	//	Create a map with space preallocated
	//	Create a slice with space preallocated or with len != cap
	m["k1"] = 7
	m["k2"] = 13

	fmt.Println("map:", m)

	v1 := m["k1"]
	fmt.Println("v1:", v1)
	fmt.Println("len:", len(m))

	delete(m, "k2") // builtin delete
	fmt.Println("map:", m)

	_, prs := m["k2"]
	fmt.Println("prs:", prs)

	n := map[string]int{"foo": 1, "bar": 2}
	fmt.Println("map:", n)
}