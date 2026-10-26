package main

import (
	"fmt"
	"os"
)

func main() {
	defer fmt.Println("main: cleanup")
	fmt.Println("main: begin")
	os.Exit(run(os.Args[1]))
}

func run(mode string) int {
	defer fmt.Println("run: cleanup")
	fmt.Println("run: begin")
	if mode == "stop" {
		os.Exit(6)
	}
	return 6
}
