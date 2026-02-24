// Learning channel concept
package main

import (
	"fmt"
	"time"
)

func hello() {
	time.Sleep(time.Second * 1)
	fmt.Println("Hello, World!")
}

func main() {
	t0 := time.Now()
	greetings := make(chan bool)

	iterations := 5000
	for i := 0; i < iterations; i++ {
		go func() {
			hello()
			greetings <- true
		}()
	}

	for i := 0; i < iterations; i++ {
		fmt.Println(i, <-greetings)
	}

	t1 := time.Since(t0)
	fmt.Println(t1)
}
