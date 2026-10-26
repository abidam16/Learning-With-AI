package main

import (
	"fmt"
	"os"
)

// Instructor-owned fixture; bukan area perbaikan learner.
func fixtureStep(step, scenario string) int {
	fmt.Printf("%s: started\n", step)
	if step == "prepare" && scenario == "reject" {
		fmt.Fprintln(os.Stderr, "prepare: input rejected")
		return 7
	}
	if step == "publish" && scenario == "publish-reject" {
		return 9
	}
	fmt.Printf("%s: done\n", step)
	return 0
}
