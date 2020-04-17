package main 

import "fmt"
import "time"

func worker(done_channel chan bool) {
	fmt.Print("working...")
	time.Sleep(time.Second)
	fmt.Println("done")

	done_channel <- true
}

func main() {
	done := make(chan bool, 1)
	go worker(done)

	<-done // block until we receive a notification that we are done
}