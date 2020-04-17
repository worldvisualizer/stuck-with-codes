package main 

import "fmt"

// sends and receives on channels are blocking
// we can use select with a default clause
// to implement non-blocking sends,
// and even non blocking multi-way selects

// https://blog.quickmediasolutions.com/2015/09/13/non-blocking-channels-in-go.html


func main() {
	// channel
	messages := make(chan string)
	signals := make(chan bool)

	select {
	case msg := <-messages:
		fmt.Println("received message", msg)
	default:
		fmt.Println("no message received")
	}
	
	msg := "hi"
	select {
	case messages <- msg:
		fmt.Println("sent message", msg)
	default:
		fmt.Println("no message received")
	}

	select {
	case msg := <-messages:
		fmt.Println("received message", msg)
	case sig := <-signals:
		fmt.Println("received signal", sig)
	default:
		fmt.Println("no activity")
	}
}