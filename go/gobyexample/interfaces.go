package main 

import "fmt"
import "math"

// To implement an interface in Go,
// we just need to implement all the methods in the interface.
// Here we implement geometry on rects.

// WTF. how does that even work man
type geometry interface {
	area() float64
	perimeter() float64
}

type rect struct {
	width, height float64
}

type circle struct {
	radius float64
}

func (r rect) area() float64 {
	return r.width * r.height
}

func (r rect) perimeter()float64 {
	return 2 * (r.width + r.height)
}

func (c circle) area() float64 {
	return c.radius * c.radius * math.Pi
}

func (c circle) perimeter()float64 {
	return c.radius * 2 * math.Pi
}

// and this is the interface type we are passing in, WTF again
// so type is just like any function, so first-class.

// this means namespacing is really important, although
// practically this shit will not be a problem.
func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perimeter())
}

func main() {
	r := rect{width: 3, height: 4}
	c := circle{radius: 5}

	measure(r)
	measure(c)
}

// need to read this:
// http://jordanorelli.com/post/32665860244/how-to-use-interfaces-in-go

