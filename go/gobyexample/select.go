package main 

import "time"
import "fmt"

func main() {
	c1 := make(chan string)
	c2 := make(chan string)

	go func() {
		time.Sleep(1 * time.Second)
		c1 <- "one"
	}()
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "two"
	}()

	for i := 0; i < 2; i++ {
		select { // select to await both values simulatenously.
		case msg1 := <-c1:
			fmt.Println("from channel one, ", msg1)

		case msg2 := <-c2:
			fmt.Println("from channel two, ", msg2)
		}
	}
}