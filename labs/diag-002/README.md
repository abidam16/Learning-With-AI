# Lab 002 — Pengiriman dokumen

Mode: attempt mandiri; mulai dari prediksi, kemudian eksperimen dan implementasi.

Sistem pengiriman memanggil worker terpisah. Pelanggan hanya boleh menerima pesan `Pengiriman: selesai` bila seluruh pekerjaan berhasil. Kode awal belum memenuhi semua kontrak.

## Kontrak

| Skenario | Hasil bisnis yang diperlukan |
| --- | --- |
| `arsip` | Berhasil menggunakan arsip cadangan; pesan worker tetap tampil; completion tampil; status program 0. |
| `kirim` | Sebagian dokumen ditolak; semua pesan worker tetap tampil; completion tidak tampil; status program nonzero. |
| `kosong` | Tidak ada dokumen untuk diproses; completion tampil; status program 0. |

Pertahankan isi pesan serta saluran stdout/stderr worker. Jalankan worker tepat sekali, sebagai proses terpisah. Perbaikan harus mengikuti hasil worker, bukan hardcode nama skenario atau teks pesannya. Jangan mengubah fixture `worker.go` atau test. Area implementasi: fungsi `deliver` dalam `main.go`.

## Mulai

Baca `main.go` dan `worker.go` sebelum menjalankan program atau test. Untuk attempt awal, coba tanpa membuka solusi lab sebelumnya; sampaikan jika membutuhkan catatan atau penjelasan API.

Pertanyaan pertama: untuk kode yang sekarang, apa urutan pesan dan nilai `$LASTEXITCODE` setelah `./lab.exe kirim`, dan mengapa?

Setelah prediksi, pilih eksperimen untuk membandingkan prediksi dengan hasil. Sebelum mengubah implementasi, nyatakan hipotesis, hasil yang diprediksi, dan pengamatan yang bisa membantahnya.

## Command (PowerShell)

```powershell
Set-Location D:\Learning\Learning-With-AI\labs\diag-002
go build -o lab.exe .
.\lab.exe kirim
$LASTEXITCODE
go test -count=1 -v ./...
```

Build ulang setelah perubahan. Periksa `$LASTEXITCODE` segera sesudah program yang ingin diamati. Test kontrak awal memang belum seluruhnya lulus; itu bagian latihan.

Selesai bila tiga kontrak lulus dan Anda dapat menjelaskan alasan implementasi bekerja. Jika waktu habis, simpan hipotesis dan langkah berikutnya tanpa harus menuntaskan kode.
