package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	fmt.Println("Impor: mulai")
	exePath, err := os.Executable()
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}

	exeDir := filepath.Dir(exePath)
	absolute_path_order := filepath.Join(exeDir, "data/orders.txt")
	data, err := os.ReadFile(absolute_path_order)
	if err != nil {
		fmt.Fprintln(os.Stderr, "Detail:", err)
		fmt.Println("Impor: gagal")
		os.Exit(1)
	}
	rows := strings.Fields(string(data))
	fmt.Printf("Impor: selesai, %d pesanan\n", len(rows))
}
