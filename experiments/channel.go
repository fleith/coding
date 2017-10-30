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
	greetings := make(chan bool)

	go func() {
		hello()
		greetings <- true
		}()

	go func() {
		hello()
		greetings <- true
	}()

	fmt.Println(<-greetings, <-greetings)
}
