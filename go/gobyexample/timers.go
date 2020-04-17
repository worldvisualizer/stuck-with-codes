package main 

import "fmt"
import "time"

func main() {
	// provides channel tht will be notified at that time
	timer1 := time.NewTimer(2 * time.Second)
	<-timer1.C // timer object has channel C
	// and things are blocking until then.
	fmt.Println("timer 1 expired")

	// and this shit will not wait because waiting for the
	// channel is in another goroutine
	timer2 := time.NewTimer(time.Second)
	go func() {
		<-timer2.C
		fmt.Println("timer 2 expired")
	}()

	stop2 := timer2.Stop()
	if stop2 {
		fmt.Println("timer 2 stopped")
	}
}