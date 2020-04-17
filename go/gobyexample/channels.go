package main 

import "fmt"

// channels are the pipes that connect concurrent goroutines
// I can send values into channels from one goroutine and receive those values into another goroutine

func main() {
	// create new channel with make()
	messages := make(chan string)

	// fuckkkkk 
	// this is putting value into the channel
	go func() { messages <- "ping" }()

	msg := <-messages
	fmt.Println(msg)
}