package main 

import (
	"fmt"
	"math/rand"
	"sync"
	"sync/atomic"
	"time"
)

func main() {
	var state = make(map[int]int)
	var mutex = &sync.Mutex{}

	var readOps uint64
	var writeOps uint64

	for r := 0; r < 100; r++ {
		go func() {
			total := 0
			for {
				// hmm, if it's atomic anyway,
				// why mutex?
				// hold up, didn't we talk about
				// channels and shit?
				// global scope would take precedence
				key := rand.Intn(5)
				mutex.Lock()
				// because this is data structure
				total += state[key]
				mutex.Unlock()
				atomic.AddUint64(&readOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	for w := 0; w < 10; w++ {
		go func() {
			for {
				key := rand.Intn(5)
				val := rand.Intn(100)
				mutex.Lock()
				// and this is just randomly adding shit
				state[key] = val
				mutex.Unlock()
				atomic.AddUint64(&writeOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}
	// and while sleeping for a sec...
	time.Sleep(time.Second)

	readOpsFinal := atomic.LoadUint64(&readOps)
	fmt.Println("readOps:", readOpsFinal)
	writeOpsFinal := atomic.LoadUint64(&writeOps)
	fmt.Println("writeOps:", writeOpsFinal)

	mutex.Lock()
	fmt.Println("state:", state)
	mutex.Unlock()
}
