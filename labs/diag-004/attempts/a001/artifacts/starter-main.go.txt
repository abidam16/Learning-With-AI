package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"syscall"
	"time"
)

func main() {
	if len(os.Args) == 4 && os.Args[1] == "--worker" {
		worker(os.Args[2], os.Args[3])
		return
	}
	if len(os.Args) != 2 || (os.Args[1] != "A" && os.Args[1] != "B") {
		fmt.Println("Usage: lab.exe A | B")
		os.Exit(64)
	}
	os.Exit(run(os.Args[1]))
}

func worker(mode, ready string) {
	fmt.Printf("Worker: mulai pid=%d\n", os.Getpid())
	if err := os.WriteFile(ready, []byte("ready"), 0600); err != nil {
		panic(err)
	}
	if mode == "A" {
		rows := []string{"record-01"}
		i := len(rows)
		fmt.Println(rows[i])
	}
	for {
		time.Sleep(100 * time.Millisecond)
	}
}

func run(mode string) int {
	exe, err := os.Executable()
	if err != nil {
		panic(err)
	}
	dir := filepath.Join(filepath.Dir(exe), "reports", mode)
	if err := os.MkdirAll(dir, 0755); err != nil {
		panic(err)
	}
	ready := filepath.Join(dir, "ready.txt")
	if err := os.Remove(ready); err != nil && !os.IsNotExist(err) {
		panic(err)
	}
	var out, stderr, supervisor bytes.Buffer
	log := func(format string, args ...any) {
		fmt.Fprintf(&supervisor, "%s ", time.Now().Format(time.RFC3339Nano))
		fmt.Fprintf(&supervisor, format+"\n", args...)
	}
	cmd := exec.Command(exe, "--worker", mode, ready)
	cmd.Stdout, cmd.Stderr = &out, &stderr
	log("launch_requested case=%s", mode)
	if err := cmd.Start(); err != nil {
		panic(err)
	}
	log("started worker_pid=%d", cmd.Process.Pid)
	finished := make(chan error, 1)
	go func() { finished <- cmd.Wait() }()
	if mode == "B" {
		deadline := time.Now().Add(5 * time.Second)
		for {
			if _, err := os.Stat(ready); err == nil {
				break
			}
			if time.Now().After(deadline) {
				_ = cmd.Process.Kill()
				<-finished
				panic("fixture setup: worker readiness timeout")
			}
			time.Sleep(10 * time.Millisecond)
		}
		log("control_request actor=supervisor operation=TerminateProcess target_pid=%d requested_exit_code=2", cmd.Process.Pid)
		h, err := syscall.OpenProcess(syscall.PROCESS_TERMINATE, false, uint32(cmd.Process.Pid))
		if err != nil {
			_ = cmd.Process.Kill()
			<-finished
			panic(err)
		}
		err = syscall.TerminateProcess(h, 2)
		_ = syscall.CloseHandle(h)
		log("control_result error=%v", err)
		if err != nil {
			_ = cmd.Process.Kill()
			<-finished
			panic(err)
		}
	}
	select {
	case err = <-finished:
	case <-time.After(5 * time.Second):
		_ = cmd.Process.Kill()
		<-finished
		panic("fixture setup: wait timeout")
	}
	status := cmd.ProcessState.ExitCode()
	log("wait_completed worker_pid=%d exit_code=%d error=%v", cmd.Process.Pid, status, err)
	write := func(name string, data []byte) {
		if err := os.WriteFile(filepath.Join(dir, name), data, 0644); err != nil {
			panic(err)
		}
	}
	write("worker.stdout.log", out.Bytes())
	write("worker.stderr.log", stderr.Bytes())
	write("supervisor.log", supervisor.Bytes())
	data, err := json.MarshalIndent(map[string]any{
		"case": mode, "worker_pid": cmd.Process.Pid, "worker_started": true,
		"worker_exit_code": status, "runner_exit_code": 2,
	}, "", "  ")
	if err != nil {
		panic(err)
	}
	write("result.json", append(data, '\n'))
	fmt.Printf("Laporan %s: worker_started=true worker_exit_code=%d\n", mode, status)
	fmt.Println("Runner: gagal")
	fmt.Printf("Berkas laporan: reports/%s\n", mode)
	return 2
}
