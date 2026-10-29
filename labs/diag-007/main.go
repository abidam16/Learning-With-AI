// Instructor-owned fixture: simulated external waits, not real network requests.
package main

import (
	"fmt"
	"runtime"
	"time"
)

func main() {
	// Limits simultaneous Go execution; does not pin the process to one CPU core.
	runtime.GOMAXPROCS(1)
	started := time.Now()
	jobs := []func(){
		waitingJob("A", time.Second, started),
		waitingJob("B", time.Second, started),
	}
	runJobs(jobs)
	fmt.Printf("batch selesai: wall=%s\n", time.Since(started).Round(time.Millisecond))
}

func waitingJob(name string, delay time.Duration, started time.Time) func() {
	return func() {
		fmt.Printf("%s mulai: %s\n", name, time.Since(started).Round(time.Millisecond))
		time.Sleep(delay)
		fmt.Printf("%s selesai: %s\n", name, time.Since(started).Round(time.Millisecond))
	}
}
