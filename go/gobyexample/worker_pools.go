package main 

import "fmt"
import "time"


// remember, no return type
func worker(id int, jobs <-chan int, results chan<- int) {
	// this is the blocking operation. waiting for jobs.
	// and I am not sure how this is orchestrated, 
	// but range ensures job being dequeued once.
	for j := range jobs {
		fmt.Println("worker", id, "started job", j)
		time.Sleep(time.Second)

		fmt.Println("worker", id, "finished job", j)
		results <- j * 2
	}
}

func main() {
	jobs := make(chan int, 100)
	results := make(chan int, 100)

	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}
	for j := 1; j <= 5; j++ {
		jobs <- j
	}
	close(jobs)

	for a := 1; a <= 5; a++ {
		fmt.Println("result:", <-results)
	}
}