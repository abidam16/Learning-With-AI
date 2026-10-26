package main

import (
	"fmt"
	"os"
	"os/exec"
)

func run() int {
	exe, err := os.Executable()
	if err != nil {
		return 8
	}
	job := exec.Command(exe, "--task")
	job.Stdout, job.Stderr = os.Stdout, os.Stderr
	if err := job.Run(); err != nil {
		return 9
	}
	return 0
}

func main() {
	if len(os.Args) == 2 && os.Args[1] == "--task" {
		defer fmt.Println("task: cleanup")
		fmt.Println("task: rejected")
		os.Exit(5)
	}
	defer fmt.Println("runner: cleanup")
	fmt.Println("runner: result", run())
}
