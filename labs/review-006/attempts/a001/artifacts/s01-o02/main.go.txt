package main

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
)

func main() {
	if len(os.Args) == 4 && os.Args[1] == "--step" {
		os.Exit(fixtureStep(os.Args[2], os.Args[3]))
	}
	if len(os.Args) != 2 {
		fmt.Fprintln(os.Stderr, "usage: lab.exe ok|reject|publish-reject|unavailable")
		os.Exit(2)
	}
	scenario := os.Args[1]
	switch scenario {
	case "ok", "reject", "publish-reject", "unavailable":
	default:
		fmt.Fprintln(os.Stderr, "unknown scenario")
		os.Exit(2)
	}
	exe, err := os.Executable()
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(2)
	}
	prepare := exec.Command(exe, "--step", "prepare", scenario)
	if scenario == "unavailable" {
		prepare = exec.Command(filepath.Join(filepath.Dir(exe), "absent-worker", "worker.exe"))
	}
	publish := exec.Command(exe, "--step", "publish", scenario)
	for _, command := range []*exec.Cmd{prepare, publish} {
		command.Stdout = os.Stdout
		command.Stderr = os.Stderr
	}
	os.Exit(runBatch(prepare, publish))
}
