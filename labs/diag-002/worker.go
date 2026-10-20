package main

import (
	"fmt"
	"os"
)

// Fixture instructor. Jangan diubah selama attempt.
func runWorker(mode string) {
	switch mode {
	case "arsip":
		fmt.Fprintln(os.Stderr, "Worker: arsip cadangan digunakan")
	case "kirim":
		fmt.Println("Worker: 2 dokumen diterima")
		fmt.Println("Worker: dokumen terakhir ditolak")
		os.Exit(4)
	case "kosong":
		return
	default:
		fmt.Fprintln(os.Stderr, "Worker: mode tidak dikenal")
		os.Exit(2)
	}
}
