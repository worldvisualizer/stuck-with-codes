package main

import "fmt"

func main() {
    var a = "initial"
    fmt.Println(a)

    var b, c int = 1,2
    fmt.Println(b,c) // can declare multiple variables of same type

    var d  = true
    fmt.Println(d) // variables can be without type identifier
    // they take initialized value's type

    var e int
    fmt.Println(e) // without corresponding initialization takes zero-value

    f := "short"
    fmt.Println(f) // := corresponds to declaring and initializing at once
}
