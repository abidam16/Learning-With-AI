package main

// Instructor-authored verification only. main.go is the learner snapshot with
// only os.Create(path) replaced by createReportFile(path) to inject file outcomes.
// The export control flow, buffer and deferred cleanup are unchanged.
import (
	"bytes"
	"errors"
	"fmt"
	"io"
	"testing"
)

type reportFile interface {
	io.Writer
	io.Closer
}

var createReportFile func(string) (reportFile, error)

type observedFile struct {
	data bytes.Buffer
	writeErr error
	closeErr error
	writes int
	closes int
}

func (f *observedFile) Write(p []byte) (int, error) {
	f.writes++
	if f.writeErr != nil { return 0, f.writeErr }
	return f.data.Write(p)
}

func (f *observedFile) Close() error {
	f.closes++
	return f.closeErr
}

func TestExportFailureAndCleanup(t *testing.T) {
	createErr := errors.New("injected create failure")
	writeErr := errors.New("injected underlying write failure")
	closeErr := errors.New("injected close failure")
	cases := []struct {
		name string
		count int
		createErr, writeErr, closeErr, wantErr error
		wantWrites, wantCloses int
	}{
		{"create_failure", 3, createErr, nil, nil, createErr, 0, 0},
		{"normal_small", 3, nil, nil, nil, nil, 1, 1},
		{"flush_failure_cleanup", 3, nil, writeErr, nil, writeErr, 1, 1},
		{"flush_failure_preserved_over_close_failure", 3, nil, writeErr, closeErr, writeErr, 1, 1},
		{"buffer_full_write_failure_cleanup", 600, nil, writeErr, nil, writeErr, 1, 1},
		{"buffer_full_write_failure_preserved_over_close_failure", 600, nil, writeErr, closeErr, writeErr, 1, 1},
		{"close_failure_after_successful_flush", 3, nil, nil, closeErr, closeErr, 1, 1},
	}
	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			file := &observedFile{writeErr: tc.writeErr, closeErr: tc.closeErr}
			createReportFile = func(string) (reportFile, error) {
				if tc.createErr != nil { return nil, tc.createErr }
				return file, nil
			}
			got := exportReport("injected-report.csv", tc.count)
			if got != tc.wantErr { t.Errorf("returned %v, want %v", got, tc.wantErr) }
			if file.writes != tc.wantWrites { t.Errorf("write calls=%d, want %d", file.writes, tc.wantWrites) }
			if file.closes != tc.wantCloses { t.Errorf("close calls=%d, want %d", file.closes, tc.wantCloses) }
			if tc.createErr == nil && tc.writeErr == nil {
				var want bytes.Buffer
				for i := 1; i <= tc.count; i++ { fmt.Fprintf(&want, "ORDER-%04d,accepted\n", i) }
				if file.data.String() != want.String() { t.Error("underlying output incomplete or unordered") }
			}
		})
	}
}
