package review001

import (
	"bufio"
	"fmt"
	"io"
)

func saveReceipt(dst io.WriteCloser) (err error) {
	defer func() {
		err_close := dst.Close()

		if err == nil {
			err = err_close
		}
	}()

	w := bufio.NewWriter(dst)
	if _, err := fmt.Fprintln(w, "PAY-042,paid"); err != nil {
		return err
	}
	return w.Flush()
}
