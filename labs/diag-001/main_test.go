package main

import (
	"os/exec"
	"path/filepath"
	"strings"
	"testing"
)

func TestContract(t *testing.T) {
	binary := filepath.Join(t.TempDir(), "lab.exe")
	build := exec.Command("go", "build", "-o", binary, ".")
	if output, err := build.CombinedOutput(); err != nil {
		t.Fatalf("setup build: %v\n%s", err, output)
	}

	for _, tc := range []struct {
		name string
		mode string
		ok   bool
	}{
		{"case01", "normal", true},
		{"case02", "ditolak", false},
	} {
		t.Run(tc.name, func(t *testing.T) {
			cmd := exec.Command(binary, tc.mode)
			output, err := cmd.CombinedOutput()
			code := cmd.ProcessState.ExitCode()
			text := string(output)
			if tc.ok {
				if err != nil || code != 0 || !strings.Contains(text, "Job: laporan dibuat") || !strings.Contains(text, "Batch: selesai") {
					t.Errorf("mode=%s code=%d output=%q; kontrak jalur normal tidak terpenuhi", tc.mode, code, text)
				}
			} else if code == 0 || strings.Contains(text, "Batch: selesai") || !strings.Contains(text, "Job: input ditolak") {
				t.Errorf("mode=%s code=%d output=%q; kontrak jalur penolakan tidak terpenuhi", tc.mode, code, text)
			}
		})
	}
}
