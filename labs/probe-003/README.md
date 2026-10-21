# Runner laporan

Mode: prediksi mandiri, sebelum eksekusi. Baca main.go tanpa membuka solusi lab sebelumnya.

Anggap os.Executable berhasil dan executable dapat dijalankan. Program dipanggil tanpa argumen melalui PowerShell:

```powershell
.\lab.exe
$LASTEXITCODE
```

Apa urutan pesan dan nilai `$LASTEXITCODE` yang Anda prediksi, beserta alur yang menghasilkan keduanya?

Success criteria: prediksi disertai alasan dari kode; setelah runtime tersedia, bandingkan dengan hasil aktual dan jelaskan selisih jika ada. Tidak perlu mengubah kode sebelum prediksi.

Build setelah Go tersedia: `go build -o lab.exe .`. Pada persiapan sesi 2026-10-21-s02, runtime Go belum ditemukan di PATH maupun dua lokasi yang digunakan sebelumnya. Build/eksekusi belum diverifikasi. Ini tidak menghalangi probe membaca kode; hasil runtime belum merupakan evidence.

Pembaruan 21 Oktober 2026, 09:19 WIB: runtime portable dipulihkan; build dan eksekusi telah diverifikasi sesudah prediksi learner. Catatan dan hasil aktual berada di attempts/a001/notes.md dan artifacts/instructor-run.txt.
