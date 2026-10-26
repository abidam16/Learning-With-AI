package main

import (
	"fmt"
	"os"
	"os/exec"
)

// Area implementasi learner. Kontrak lengkap ada di README.md.
func runBatch(prepare, publish *exec.Cmd) int {
	// TODO: implementasikan pengendali batch.
	if err := prepare.Run(); err != nil {
		fmt.Fprintln(os.Stderr, "prepare: gagal")
		return 1
	}

	if err := publish.Run(); err != nil {
		fmt.Fprintln(os.Stderr, "publish: gagal")
		return 1
	}

	fmt.Println("Batch: selesai")
	return 0
}
