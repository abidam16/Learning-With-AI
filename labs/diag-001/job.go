package main

import (
	"fmt"
	"os"
)

// Fixture instructor: kontrak job tetap selama diagnostic.
func runJob(mode string) {
	if mode != "normal" {
		fmt.Fprintln(os.Stderr, "Job: input ditolak")
		os.Exit(2)
	}
	fmt.Println("Job: laporan dibuat")
}
