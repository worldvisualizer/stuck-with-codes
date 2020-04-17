package main 

import "fmt"

// let's read this:
// https://medium.com/@riteeksrivastava/a-complete-journey-with-goroutines-8472630c7f5c

// - if main goroutine terminates,
// - the program will terminate and other goroutines will not run
// mainly, we use channels to block the main goroutine until all other goroutines finish execution

// if goroutine is waiting for IO, then scheduler executes other goroutine

// goroutine creation: memory allocation, channel creation, creation of goroutines
// then runtime makes syscall and thread creation to the OS kernel

// hmm, about context switch - 
// https://electronics.stackexchange.com/questions/115286/what-processor-registers-are-saved-and-recovered-in-a-context-switch

func async_function(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

func main() {
	async_function("direct")
	go async_function("goroutine")
	go async_function("goroutine2")

	go func(msg string) {
		fmt.Println("and fuck you too", msg)
	}("going")
	fmt.Scanln()
	// why does async goroutines not complete when main "routine" finishes executing?
	fmt.Println("and this line not being here makes async shit just not executed")
}