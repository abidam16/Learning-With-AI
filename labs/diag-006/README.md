# Diagnostic 006 — Ekspor laporan

Program menerima jumlah order sintetis dan menghasilkan CSV. Tim operasional melaporkan bahwa pesan sukses belum selalu sesuai dengan isi file yang diterima.

## Kontrak

- Untuk N order, file harus berisi tepat N baris lengkap dan berurutan, dari ORDER-0001 sampai ORDER-N.
- Pesan sukses dan exit 0 hanya boleh muncul setelah seluruh isi laporan berhasil diserahkan ke file dan file ditutup tanpa error.
- Scope: pembacaan file setelah program selesai pada OS yang tetap berjalan. Ketahanan terhadap listrik mati tidak diuji.
- Gunakan 3 dan 600 order sebagai dua kasus. Data sintetis; tidak ada layanan eksternal.
- Learner memiliki diagnosis dan perubahan main.go. Jangan mengganti hasil dengan file hardcoded atau menghapus kasus yang gagal.

## Alur

Mulai dengan membaca main.go, lalu sampaikan satu hipotesis sebelum menjalankan atau mengubah program. Pilih satu eksperimen pembeda dan prediksikan hasilnya sebelum eksekusi.

Build dari folder lab bila main.go berubah:

```powershell
& ..\..\.local-tools\go\bin\go.exe build -o lab.exe .
```

Executable awal disediakan. Jalankan dari folder lab dengan jumlah order pilihan:

```powershell
.\lab.exe 3
$LASTEXITCODE
Get-Content .\out\report-3.csv
```

Setiap eksekusi menimpa hanya report-N.csv untuk jumlah tersebut. Simpan hasil pengamatan sebelum menjalankan ulang. Ukuran file saja tidak cukup membuktikan semua baris benar.
