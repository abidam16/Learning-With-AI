# Diagnostic 001 — Laporan batch

Mode: diagnostic independen, mulai tanpa hint substantif. Fokus observasi: concept dan debugging. Timebox latihan sekitar 20–25 menit; boleh berhenti dengan checkpoint.

Sebuah batch menjalankan satu job pembuat laporan. Operator melaporkan bahwa status batch tidak selalu cocok dengan hasil pekerjaannya. Selidiki program dan buktikan penyebab sebelum mengubah implementasi.

Kontrak bisnis:

- Input `normal`: laporan dibuat, pesan `Batch: selesai` muncul, exit status batch 0.
- Input selain `normal`: pekerjaan ditolak, alasan penolakan tetap terlihat, pesan `Batch: selesai` tidak muncul, exit status batch bukan 0. Angka nonzero tertentu tidak diwajibkan.
- Pertahankan job sebagai program terpisah yang dijalankan oleh batch. Fixture `job.go` dan kontrak test tidak diubah.

Area implementasi learner: `main.go`. Baca juga `job.go` agar mengetahui perilaku program yang dipanggil. Instructor menyediakan fixture, harness, dan build. Tidak ada solusi perbaikan yang disediakan.

## Langkah pertama

Baca `main.go` dan `job.go` tanpa menjalankan program atau test dahulu. Untuk command `.\lab.exe ditolak`, prediksikan pesan yang muncul serta nilai `$LASTEXITCODE`, dan jelaskan alasannya. Jika ada sintaks/API yang belum dikenal, sebutkan bagian itu; tidak perlu menebak.

## Command untuk tahap eksperimen setelah prediksi

Gunakan terminal PowerShell:

```powershell
Set-Location D:\Learning\Learning-With-AI\labs\diag-001
go build -o lab.exe .
.\lab.exe normal
$LASTEXITCODE
.\lab.exe ditolak
$LASTEXITCODE
go test -count=1 -v ./...
```

Build ulang setelah mengubah kode. Test awal memang memuat kegagalan kontrak. Tentukan hipotesis dan eksperimen pembeda sebelum perbaikan; instructor akan meminta satu langkah pada satu waktu. Untuk pengamatan exit status gunakan executable hasil build.

Success criteria: prediksi disertai alasan, diagnosis berdasarkan eksperimen yang dipilih learner, dan bila sampai perbaikan, kedua jalur memenuhi kontrak dengan penjelasan sebab-akibat. Test hijau saja belum membuktikan pemahaman. Pembahasan yang belum selesai dapat dilanjutkan di sesi lain.

Metadata instructor berada di `lab.yaml` dan catatan `attempts/`; belum perlu dibaca saat diagnostic karena dapat mengarahkan jawaban.
