package main

import "fmt"
import "math"

const s string = "constant string"

func main() {
    fmt.Println(s)
    const n = 500000000 // constant expressions perform arithmetic ith arbitrary precision
    const d = 3e20 / n
    fmt.Println(d)
    fmt.Println(int64(d)) // numeric constant has no type until it's givcen one
    fmt.Println(math.Sin(n)) // math.Sin expects float64, and constant will be assigned of that type when being used without any additional context except that function call
}
