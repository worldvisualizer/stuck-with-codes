package main 

import "fmt"
import "time"

func main() {
    i := 2
    fmt.Print("Write ", i, " as ")
    switch i {
    case 1:
        fmt.Println("one")
    case 2:
        fmt.Println("two")
    case 3:
        fmt.Println("three")
    }

    switch time.Now().Weekday() {
    case time.Saturday, time.Sunday:
        fmt.Println("It's the weekend")
    default:
        fmt.Println("It's a weekday")
    }

    t := time.Now()
    switch {
    case t.Hour() < 12:
        fmt.Println("It's before noon")
    default:
        fmt.Println("It's after noon")
    }

    // so apparently interface{} is some kind of
    // object type being used in go.
    whatAmI := func(i interface{}) {
        // assign t and then evaluate
        switch t := i.(type) {
        case bool:
            fmt.Println("I am a bool")
            fmt.Println(i)
        case int:
            fmt.Println("I am an int")
            fmt.Println(i)
        default:
            fmt.Println("Don't know the type %T\n", t)
            fmt.Println(i)
        }
    }
    whatAmI(true)
    whatAmI(1)
    whatAmI("hey")
}