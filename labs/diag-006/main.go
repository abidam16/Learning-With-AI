package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"strconv"
)

func exportReport(path string, count int) error {
	f, err := os.Create(path)
	if err != nil {
		return err
	}
	defer f.Close()

	w := bufio.NewWriter(f)
	for i := 1; i <= count; i++ {
		fmt.Printf("ORDER-%04d,accepted\n", i)
		if _, err := fmt.Fprintf(w, "ORDER-%04d,accepted\n", i); err != nil {
			return err
		}
	}
	if err := w.Flush(); err != nil {
		return err
	}
	return nil
}

func run() int {
	if len(os.Args) != 2 {
		fmt.Fprintln(os.Stderr, "Usage: lab.exe <jumlah-order: 1..1000>")
		return 2
	}
	count, err := strconv.Atoi(os.Args[1])
	if err != nil || count < 1 || count > 1000 {
		fmt.Fprintln(os.Stderr, "Jumlah harus 1..1000")
		return 2
	}
	executable, err := os.Executable()
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		return 1
	}
	outDir := filepath.Join(filepath.Dir(executable), "out")
	if err := os.MkdirAll(outDir, 0755); err != nil {
		fmt.Fprintln(os.Stderr, err)
		return 1
	}
	path := filepath.Join(outDir, fmt.Sprintf("report-%d.csv", count))
	if err := exportReport(path, count); err != nil {
		fmt.Fprintln(os.Stderr, "Ekspor gagal:", err)
		return 1
	}
	fmt.Printf("Ekspor selesai: %d order\nFile: %s\n", count, path)
	return 0
}

func main() {
	os.Exit(run())
}
