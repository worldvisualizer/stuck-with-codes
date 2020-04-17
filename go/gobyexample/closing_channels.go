package main 

import "fmt"

// like EOF for the IO buffer
// EOF for the channel

func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	go func() {
		for {
			// this is interesting
			// channel has multiple return values
			// at least the second positional retval
			// is whether this channel is open or not
			j, more := <-jobs
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("received all jobs")
				// tis is another way to block shit
				// and wait for this goroutine to be done.
				done <- true
				return
			}
		}
	}()

	for j := 1; j <= 3; j++ {
		jobs <- j 
		fmt.Println("sent job", j)
	}
	close(jobs)
	fmt.Println("sent all jobs")

	// without this done channel,
	// this function above does not execute until the finish
	// synchronization
	<-done
}