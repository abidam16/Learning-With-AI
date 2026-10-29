# Dua pekerjaan independen

Mode: praktik setelah penjelasan konsep, bukan blind diagnostic. Timebox awal 20 menit, mengikuti sisa sesi.

Fixture mensimulasikan dua penantian independen menggunakan timer satu detik. Tidak ada request HTTP nyata. Jalankan baseline dari PowerShell:

```powershell
Set-Location D:\Learning\Learning-With-AI\labs\diag-007
go run .
```

Timestamp mulai/selesai dan `wall` diukur di dalam program; waktu kompilasi `go run` tidak termasuk. `wall` bukan CPU time. `GOMAXPROCS(1)` membatasi eksekusi kode Go yang bersamaan; tidak mengubah jumlah core mesin atau menjamin hanya ada satu OS thread.

Langkah pertama: baca runner.go, jalankan baseline, lalu jelaskan hubungan urutan event dengan durasi total. Jangan ubah kode dahulu.

Target langkah berikut setelah baseline dibahas: ubah runner.go supaya masa tunggu pekerjaan dapat tumpang tindih. Setiap job harus dijalankan tepat sekali; runJobs baru boleh kembali setelah semua job selesai. Jangan mengubah fixture, memangkas durasi, atau memakai penundaan tetap untuk menebak kapan semua job selesai. API/sintaks dapat dipelajari secara terbimbing; bantuan akan dicatat.

Keberhasilan dilihat dari kode learner, semua event selesai sebelum batch selesai, overlap waktu pekerjaan, dan penjelasan mekanismenya. Angka satu detik adalah perkiraan dengan overhead, bukan ambang kelulusan ketat. Kode awal merupakan baseline valid dan belum memenuhi target overlap.
