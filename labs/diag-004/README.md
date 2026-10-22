# Dua laporan pemrosesan

Mode: diagnosis dari bukti runtime. Timebox latihan: 20–25 menit.

Sebuah runner memproses dua laporan secara terpisah, A dan B. Keduanya menghasilkan ringkasan:

```text
worker_started=true worker_exit_code=2
Runner: gagal
```

Status runner yang dibaca PowerShell juga 2. Operator ingin mengetahui penyebab berhentinya tiap worker sebelum menentukan tindak lanjut. Pekerjaan hanya dianggap berhasil jika pemrosesan selesai; pesan mulai bukan tanda pekerjaan selesai.

Tujuan: susun hipotesis, pilih bukti atau eksperimen pembeda, prediksi hasilnya sebelum memeriksa, lalu simpulkan penyebab sejauh bukti mendukungnya. Tidak ada patch wajib.

Berkas runtime tersedia untuk setiap laporan dalam `reports/A` dan `reports/B`: `result.json`, `worker.stdout.log`, `worker.stderr.log`, dan `supervisor.log`. Pilih sendiri yang perlu diperiksa. Source fixture tersedia, tetapi mulai dari ringkasan ini agar diagnosis pertama berasal dari bukti runtime.

Untuk mengulang fixture dari PowerShell:

```powershell
Set-Location D:\learning\Learning-With-AI\labs\diag-004
.\lab.exe A
$LASTEXITCODE
.\lab.exe B
$LASTEXITCODE
```

Eksekusi ulang mengganti laporan kasus yang sama. Simpan output penting sebelum mengulang. Semua proses fixture lokal dan tidak memakai layanan atau data kerja.

Mulai dengan satu hipotesis tentang dua laporan di atas, satu pemeriksaan yang dapat membedakannya dari alternatif, dan prediksi hasil pemeriksaan itu. Jangan menjalankan atau membuka laporan rinci sebelum menyatakan prediksi.
