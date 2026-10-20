package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
	if len(os.Args) > 2 && os.Args[1] == "--job" {
		runJob(os.Args[2])
		return
	}

	mode := "normal"
	if len(os.Args) > 1 {
		mode = os.Args[1]
	}

	executable, err := os.Executable()
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}

	job := exec.Command(executable, "--job", mode)
	job.Stdout = os.Stdout
	job.Stderr = os.Stderr
	job.Run()
	fmt.Println("Batch: selesai")
}
