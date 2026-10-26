# Review 005 — Impor kiriman

Mode: retrieval mandiri; mulai dengan hipotesis sebelum inspeksi atau perubahan.

Sebuah alat menerima satu argumen nama file pesanan. Operator A dan B menjalankannya dari folder kerja masing-masing. Keduanya melaporkan sukses, tetapi pesanan yang ditampilkan bukan milik mereka.

Kontrak: argumen relatif menunjuk file dari folder terminal saat perintah dijalankan; argumen absolut menunjuk file tersebut langsung. File contoh yang disertakan bersama aplikasi tidak boleh menggantikan pilihan operator. Bila file pilihan tidak ada, laporkan gagal dengan exit nonzero. Jangan ubah fixture, menyalin data untuk mengakali kasus, atau hardcode folder A/B. Area perubahan: main.go.

## Peluncuran yang dilaporkan

A:
```powershell
Set-Location D:\learning\Learning-With-AI\labs\review-005\jobs\A
..\..\lab.exe orders.txt
$LASTEXITCODE
```

B:
```powershell
Set-Location D:\learning\Learning-With-AI\labs\review-005\jobs\B
..\..\lab.exe orders.txt
$LASTEXITCODE
```

Harapan A: A-101, A-102, A-103. Harapan B: B-201, B-202.
Observasi instructor untuk keduanya: `Impor: 1 pesanan [DEMO-01]`, exit 0.

Sebelum membuka source atau menjalankan command: apa satu hipotesis yang menjelaskan mengapa kedua operator mendapatkan DEMO-01?

Sesudah prediksi awal, learner memilih satu eksperimen pembeda; source tersedia untuk inspeksi. Setelah diagnosis, learner menulis patch. Keberhasilan mencakup bukti penyebab, hasil A/B yang benar, argumen absolut, kegagalan file hilang, dan penjelasan pada satu kondisi baru.

Build dari folder lab:
```powershell
& ..\..\.local-tools\go\bin\go.exe build -o lab.exe .
```
