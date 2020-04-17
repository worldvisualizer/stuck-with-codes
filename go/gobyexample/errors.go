package main

import "errors"
import "fmt"

// dafuq, is this acceptable error type?
func function1(arg int) (int, error) {
	if arg == 42 {
		return -1, errors.New("arg 42 value")
	}
	return arg + 3, nil
}

type argError struct {
	arg int
	prob string
}

// use custom types as errors
// by implementing the Error() method
func (e *argError) Error() string {
 	return fmt.Sprintf("%d - %s", e.arg, e.prob)
}

func function2(arg int) (int, error) {
	if arg == 42 {
		return -1, &argError{arg, "can't work with it"}
	}
	return arg + 3, nil
}

func main() {
	for _, i := range []int{7, 42} {
		if r, e := function1(i); e != nil {
			fmt.Println("f1 failed:", e)
		} else {
			fmt.Println("f1 worked:", r)
		}
	}

	for _, i := range []int{7, 42} {
		if r, e := function2(i); e != nil {
			fmt.Println("f2 failed:", e)
		} else {
			fmt.Println("f2 worked:", r)
		}
	}

	_, function2_error := function2(42)
	if argerror, okay := function2_error.(*argError); okay {
		fmt.Println(argerror.arg)
		fmt.Println(argerror.prob)
	}
}