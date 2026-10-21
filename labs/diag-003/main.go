package main

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
)

func main() {
	if len(os.Args) == 2 && os.Args[1] == "--worker" {
		os.Exit(6)
	}
	if len(os.Args) != 2 {
		fmt.Println("Pemakaian: lab.exe A atau lab.exe B")
		os.Exit(1)
	}
	self, err := os.Executable()
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	var target string
	switch os.Args[1] {
	case "A":
		target = self
	case "B":
		target = filepath.Join(filepath.Dir(self), "bundle", "processor.exe")
	default:
		fmt.Println("Pilihan tidak dikenal")
		os.Exit(1)
	}
	os.Exit(run(target))
}

func run(target string) int {
	cmd := exec.Command(target, "--worker")
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	err := cmd.Run()
	if err != nil {
		fmt.Println("Runner: gagal")
		return 2
	}
	fmt.Println("Runner: selesai")
	return 0
}
