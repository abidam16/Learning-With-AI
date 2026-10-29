package main

// Learner workspace. This starting version runs jobs sequentially.
func runJobs(jobs []func()) {
	for _, job := range jobs {
		job()
	}
}
