package main

import (
	"bytes"
	"os/exec"
	"path/filepath"
	"strings"
	"testing"
)

func buildLab(t *testing.T) string {
	t.Helper()
	binary := filepath.Join(t.TempDir(), "lab.exe")
	if output, err := exec.Command("go", "build", "-o", binary, ".").CombinedOutput(); err != nil {
		t.Fatalf("setup build: %v\n%s", err, output)
	}
	return binary
}

func observe(t *testing.T, binary string, args ...string) (string, string, int) {
	t.Helper()
	cmd := exec.Command(binary, args...)
	var out, diagnostic bytes.Buffer
	cmd.Stdout, cmd.Stderr = &out, &diagnostic
	err := cmd.Run()
	if cmd.ProcessState == nil {
		t.Fatalf("setup execution: %v", err)
	}
	return strings.ReplaceAll(out.String(), "\r\n", "\n"), strings.ReplaceAll(diagnostic.String(), "\r\n", "\n"), cmd.ProcessState.ExitCode()
}

func TestFixture(t *testing.T) {
	binary := buildLab(t)
	for _, tc := range []struct {
		mode, out, diagnostic string
		code                  int
	}{
		{"arsip", "", "Worker: arsip cadangan digunakan\n", 0},
		{"kirim", "Worker: 2 dokumen diterima\nWorker: dokumen terakhir ditolak\n", "", 4},
		{"kosong", "", "", 0},
	} {
		t.Run(tc.mode, func(t *testing.T) {
			out, diagnostic, code := observe(t, binary, "--worker", tc.mode)
			if out != tc.out || diagnostic != tc.diagnostic || code != tc.code {
				t.Fatalf("fixture mismatch: stdout=%q stderr=%q code=%d", out, diagnostic, code)
			}
		})
	}
}

func TestContract(t *testing.T) {
	binary := buildLab(t)
	for _, tc := range []struct {
		mode, out, diagnostic string
		ok                    bool
	}{
		{"arsip", "Pengiriman: selesai\n", "Worker: arsip cadangan digunakan\n", true},
		{"kirim", "Worker: 2 dokumen diterima\nWorker: dokumen terakhir ditolak\n", "", false},
		{"kosong", "Pengiriman: selesai\n", "", true},
	} {
		t.Run(tc.mode, func(t *testing.T) {
			out, diagnostic, code := observe(t, binary, tc.mode)
			if out != tc.out || diagnostic != tc.diagnostic || (code == 0) != tc.ok {
				t.Errorf("kontrak %s belum terpenuhi: stdout=%q stderr=%q code=%d", tc.mode, out, diagnostic, code)
			}
		})
	}
}
