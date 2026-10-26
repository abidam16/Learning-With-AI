package main

import (
	"encoding/json"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"time"
)

func main() {
	if len(os.Args) == 3 && os.Args[1] == "--task" {
		os.Exit(task(os.Args[2]))
	}
	if len(os.Args) != 2 || (os.Args[1] != "K" && os.Args[1] != "L") {
		fmt.Fprintln(os.Stderr, "usage: lab.exe K|L")
		os.Exit(64)
	}
	os.Exit(run(os.Args[1]))
}

func task(path string) int {
	fmt.Printf("task: started pid=%d\n", os.Getpid())
	data, err := os.ReadFile(path)
	if err != nil {
		fmt.Fprintf(os.Stderr, "task: input read failed: %v\n", err)
		return 4
	}
	var input struct {
		Orders []string `json:"orders"`
	}
	if err := json.Unmarshal(data, &input); err != nil {
		fmt.Fprintf(os.Stderr, "task: input rejected: invalid JSON: %v\n", err)
		return 4
	}
	fmt.Printf("task: completed orders=%d\n", len(input.Orders))
	return 0
}

func run(id string) int {
	dir := filepath.Join("reports", id)
	if err := os.MkdirAll(dir, 0755); err != nil {
		panic(err)
	}
	stdout, err := os.Create(filepath.Join(dir, "worker.stdout.log"))
	if err != nil {
		panic(err)
	}
	defer stdout.Close()
	stderr, err := os.Create(filepath.Join(dir, "worker.stderr.log"))
	if err != nil {
		panic(err)
	}
	defer stderr.Close()
	log, err := os.Create(filepath.Join(dir, "supervisor.log"))
	if err != nil {
		panic(err)
	}
	defer log.Close()
	executable, err := os.Executable()
	if err != nil {
		panic(err)
	}
	if id == "L" {
		executable = filepath.Join(filepath.Dir(executable), "release", "worker.exe")
	}
	input, err := filepath.Abs(filepath.Join("fixtures", "orders.json"))
	if err != nil {
		panic(err)
	}
	cwd, err := os.Getwd()
	if err != nil {
		panic(err)
	}
	request := map[string]any{"case": id, "executable": executable, "args": []string{"--task", input}, "working_directory": cwd}
	writeJSON(filepath.Join(dir, "request.json"), request)
	cmd := exec.Command(executable, "--task", input)
	cmd.Stdout, cmd.Stderr = stdout, stderr
	fmt.Fprintf(log, "%s case=%s launch_requested\n", time.Now().Format(time.RFC3339Nano), id)
	result := map[string]any{"case": id, "started": false, "worker_exit_code": nil, "runner_exit_code": 1}
	if err := cmd.Start(); err != nil {
		fmt.Fprintf(log, "start_failed error=%v\n", err)
		result["error"] = err.Error()
	} else {
		result["started"] = true
		result["pid"] = cmd.Process.Pid
		fmt.Fprintf(log, "started pid=%d\n", cmd.Process.Pid)
		err := cmd.Wait()
		result["worker_exit_code"] = cmd.ProcessState.ExitCode()
		fmt.Fprintf(log, "wait_returned pid=%d exit_code=%d error=%v\n", cmd.Process.Pid, cmd.ProcessState.ExitCode(), err)
		if err == nil {
			result["runner_exit_code"] = 0
		}
	}
	writeJSON(filepath.Join(dir, "result.json"), result)
	code := result["runner_exit_code"].(int)
	if code != 0 {
		fmt.Printf("case=%s status=failed runner_exit_code=%d\n", id, code)
	} else {
		fmt.Printf("case=%s status=completed runner_exit_code=0\n", id)
	}
	return code
}

func writeJSON(path string, v any) {
	data, err := json.MarshalIndent(v, "", "  ")
	if err != nil {
		panic(err)
	}
	if err := os.WriteFile(path, append(data, '\n'), 0644); err != nil {
		panic(err)
	}
}
