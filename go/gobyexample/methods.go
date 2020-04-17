package main 

import "fmt"

// so type is like a class.
// https://stackoverflow.com/questions/8263546/whats-the-difference-of-functions-and-methods-in-go

type rect struct {
	width, height int
}

// receiver type is like self. of python or this. of java.
func (r *rect) area() int {
	return r.width * r.height
}

func (r rect) perimeter() int {
	return 2 * (r.width + r.height)
}

func main() {
	r := rect{width: 10, height: 5}

	fmt.Println("area: ", r.area())
    fmt.Println("perim:", r.perimeter())

    rp := &r // again, value and pointer conversion automatic
	fmt.Println("area: ", rp.area())
    fmt.Println("perim:", rp.perimeter())

}