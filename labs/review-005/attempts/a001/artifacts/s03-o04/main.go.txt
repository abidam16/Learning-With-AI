package main

import (
    "fmt"
    "os"
    "path/filepath"
    "strings"
)

func run(args []string) int {
    if len(args) != 1 {
        fmt.Fprintln(os.Stderr, "Pemakaian: lab.exe <file-pesanan>")
        return 2
    }
    _, err := os.Executable()
    if err != nil {
        fmt.Fprintln(os.Stderr, err)
        return 1
    }
    cwd, err := os.Getwd()
    if err != nil {
        fmt.Fprintln(os.Stderr, "Gagal mendapatkan working directory:", err)
        return 1
    }
    input := args[0]
    if !filepath.IsAbs(input) {
        input = filepath.Join(cwd, input)
    }
    data, err := os.ReadFile(input)
    if err != nil {
        fmt.Fprintln(os.Stderr, "Impor gagal:", err)
        return 1
    }
    orders := strings.Fields(string(data))
    fmt.Printf("Impor: %d pesanan [%s]\n", len(orders), strings.Join(orders, ", "))
    return 0
}

func main() { os.Exit(run(os.Args[1:])) }
