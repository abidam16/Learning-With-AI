package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
	if len(os.Args) == 2 && os.Args[1] == "--worker" {
		fmt.Println("Worker: ditolak")
		os.Exit(6)
	}
	executable, err := os.Executable()
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	result := execute(executable)
	fmt.Println("Runner: hasil", result)
}

func execute(executable string) int {
	cmd := exec.Command(executable, "--worker")
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	if err := cmd.Run(); err != nil {
		return 9
	}
	return 0
}
