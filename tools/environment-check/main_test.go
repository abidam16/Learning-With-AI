package main

import "testing"

func TestMessage(t *testing.T) {
	if got := message(); got != "Environment OK" {
		t.Fatalf("message() = %q; want Environment OK", got)
	}
}
