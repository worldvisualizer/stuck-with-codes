package main 

import "fmt"

func main() {
	nums := []int{2,3,4}
	sum := 0
	for prob_index, num := range nums {
		sum += num
		fmt.Println("index?", prob_index)
	}
	fmt.Println("sum:", sum)

	for i, num := range nums {
		if num == 3 {
			fmt.Println("index:", i)
		}
	}

	kvs := map[string]string{"a": "apple", "b": "banana"}
	// this is making things iterable
	for k,v := range kvs {
		fmt.Printf("%s -> %s\n", k, v)
	}
	// can just iterate over keys, not that k is a key-value pair.
	for k := range kvs {
		fmt.Println("key:", k)
	}
	// this is character unixcode, strangely.
	for i,c := range "go" {
		fmt.Println(i, c)
	}
}