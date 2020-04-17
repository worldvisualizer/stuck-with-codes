package main 

import "fmt"

func main() {
    // slice and array are different type
    // to create and initialize slice, use make.

    // https://blog.golang.org/go-slices-usage-and-internals

    // Slice internals
    // A slice is a descriptor of an array segment.
    // It consists of a pointer to the array,
    // the length of the segment,
    // and its capacity (the maximum length of the segment).
    s := make([]string, 3) 
    fmt.Println("empty initialized slice:", s)

    s[0] = "a"
    s[1] = "b"
    s[2] = "c"

    fmt.Println("set:", s, " get:", s[2], " len:", len(s))

    s = append(s, "d", "e", "f")
    fmt.Println("append result:", s)

    c := make([]string, len(s))
    copy(c,s)
    fmt.Println("copy result:", c)
    l := s[2:5]
    fmt.Println("slice only supported in slice:", l)

    l = s[:5]
    fmt.Println("slice upto:", l)

    l = s[2:]
    fmt.Println("slice downfrom?:", l)

    // A slice literal is declared just like an array literal,
    // except you leave out the element count:
    t := []string{"g", "h", "i"}
    fmt.Println("not just an array declaration:", t)

    twoD := make([][]int, 3)
    for i := 0; i < 3; i++ {
        innerLen := i + 1
        twoD[i] = make([]int, innerLen)
        for j := 0; j < innerLen; j++ {
            twoD[i][j] = i + j
        }
    }
    fmt.Println("2d:", twoD)
}