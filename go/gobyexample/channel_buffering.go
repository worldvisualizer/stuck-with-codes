package main 

import "fmt"

// by default channels are unbuffered, meaning
// they will only accept sends if there's a corresponding receive.
// buffered channels accept a limited number of values without a corresponding receiver

func main() {
	// make channel of strings buffering to 2 values
	messages := make(chan string, 2)

	messages <- "buffered"
	messages <- "channel"

	fmt.Println(<-messages) // and this is receiving, one at a time
	fmt.Println(<-messages)
}