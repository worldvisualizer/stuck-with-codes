package main 

import "fmt"

type person struct {
	name string
	age int
}

func main() {
	fmt.Println(person{"Bob", 20})
	// positional arguments work!
	fmt.Println(person{name: "Alice", age: 25})
	fmt.Println(person{name: "Mark"})
	// omitted fields zero valued
	fmt.Println(&person{name: "Ann", age: 40})
	// pointer to struct

	s := person{name: "Sean", age: 50}
	fmt.Println(s.name)

	sp := &s
	fmt.Println(sp.age)
	// pointers auto-dereferenced to access pointers

	sp.age = 51
	// structs are mutable
	fmt.Println(sp.age)
	// fucking around, has no problem
	fmt.Println(person{name: "Mark",})
}