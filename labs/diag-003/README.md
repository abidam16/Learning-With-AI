# Dua laporan kegagalan

Operator menjalankan dua pilihan, A dan B. Keduanya menampilkan `Runner: gagal` dengan `$LASTEXITCODE` bernilai 2, tanpa pesan lain.

Apakah kedua pekerjaan gagal dengan cara yang sama? Tugas Anda menyusun penjelasan berbasis observasi untuk masing-masing pilihan.

Mode: investigasi mandiri. Timebox: 15–20 menit setelah environment siap. Tidak perlu menulis perbaikan pada tahap awal.

1. Sebelum menjalankan atau mengubah source, usulkan satu hipotesis, hasil yang Anda prediksi jika benar, dan satu eksperimen untuk membedakannya dari alternatif.
2. Jalankan eksperimen, lalu bandingkan dengan prediksi. Source main.go boleh dibaca dan ditambah observasi. Pertahankan pilihan A/B dan perilaku bagian --worker; jangan membuat executable pengganti.
3. Jelaskan apa yang dapat dan belum dapat disimpulkan dari bukti, serta satu tindakan lanjutan yang sesuai.

Success criteria: setiap pilihan memiliki diagnosis yang ditopang bukti runtime; kedua status yang sama tidak dijadikan satu-satunya bukti penyebab. Hipotesis dan prediksi dibuat sebelum eksperimen. Test hijau atau patch bukan syarat tugas ini.

Commands setelah build:

```powershell
.\lab.exe A
$LASTEXITCODE
.\lab.exe B
$LASTEXITCODE
```

Build: `go build -o lab.exe .`. Hasil verifikasi environment disimpan di notes attempt sebelum tugas diberikan.
