package main 

import "fmt"

func main() {
	queue := make(chan string, 2)
	queue <- "one"
	queue <- "two"
	close(queue) // two buffered shit, closes it like a cave

	for elem := range queue { // and now it's an iterator.
		fmt.Println(elem)
	}
}