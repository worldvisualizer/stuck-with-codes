package main 

import "os"

func main() {
	// panic is like an exception
	panic("a problem")

	_, err := os.Create("/tmp/file")
	if err != nil {
		panic(err)
	}
}
