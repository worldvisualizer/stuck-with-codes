package main 

import "fmt"
import "time"
import "sync/atomic"

func main() {
	// represents counter
	var ops uint64

	for i := 0; i < 500; i++ {
		go func() {
			for {
				// 50 goroutines that
				// increments the same counter
				// once a millisec
				atomic.AddUint64(&ops, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}
	time.Sleep(time.Second)
	// the other goroutines are still adding!
	// but this is safe because well, atomic
	opsFinal := atomic.LoadUint64(&ops)
	fmt.Println("ops:", opsFinal)
}