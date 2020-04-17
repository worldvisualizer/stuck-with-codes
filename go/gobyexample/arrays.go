package main 

import "fmt"

func main() {
    // zero-initialized already for an array
    // but not really initialized per se.
    var a [5]int
    fmt.Println("emp:", a)

    a[4] = 100
    fmt.Println("set:", a)
    fmt.Println("get:", a[4])
    fmt.Println("len:", len(a))

    b := [5]int{3,4,5,6,7}
    fmt.Println("dcl:", b)

    var twoD [2][3]int
    for i := 0; i < 2; i++ {
        for j := 0; j < 3; j++ {
            twoD[i][j] = i + j
        }
    }
    // Note that arrays appear in the form [v1 v2 v3 ...]
    // when printed with fmt.Println.
    fmt.Println("2d:", twoD)
}