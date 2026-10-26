package review001

import (
	"bytes"
	"errors"
	"testing"
)

type destination struct {
	data     bytes.Buffer
	writeErr error
	closeErr error
	closes   int
}

func (d *destination) Write(p []byte) (int, error) {
	if d.writeErr != nil {
		return 0, d.writeErr
	}
	return d.data.Write(p)
}

func (d *destination) Close() error {
	d.closes++
	return d.closeErr
}

func TestReceipt(t *testing.T) {
	writeFailure := errors.New("destination full")
	closeFailure := errors.New("destination close failed")
	cases := []struct {
		name                     string
		writeErr, closeErr, want error
	}{
		{"normal", nil, nil, nil},
		{"write_failure", writeFailure, nil, writeFailure},
		{"close_failure", nil, closeFailure, closeFailure},
		{"both_failures", writeFailure, closeFailure, writeFailure},
	}
	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			d := &destination{writeErr: tc.writeErr, closeErr: tc.closeErr}
			got := saveReceipt(d)
			t.Logf("result=%v data=%q close_calls=%d", got, d.data.String(), d.closes)
			if !errors.Is(got, tc.want) {
				t.Errorf("result=%v; expected=%v", got, tc.want)
			}
			if d.closes != 1 {
				t.Errorf("close_calls=%d; expected=1", d.closes)
			}
			if tc.writeErr == nil && d.data.String() != "PAY-042,paid\n" {
				t.Errorf("unexpected receipt %q", d.data.String())
			}
		})
	}
}
