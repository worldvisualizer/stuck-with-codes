package main 

import "time"
import "fmt"

func main() {
	ticker := time.NewTicker(500 * time.Millisecond)
	go func() {
		// every 500 milliseoncds, tick.
		// and let you know.
		// which would have been a whole different thing
		// in python synchronous programming
		for t := range ticker.C {
			fmt.Println("Tick at", t)
		}
	}()

	time.Sleep(1600 * time.Millisecond)
	ticker.Stop()
	fmt.Println("Ticker Stopped")
}