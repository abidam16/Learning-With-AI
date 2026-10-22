# Lab 005 — Impor pesanan

Mode: diagnostic mandiri, dimulai dari hipotesis sebelum eksperimen.

Program impor yang sama berhasil lewat peluncuran A, tetapi gagal lewat peluncuran B. Executable dan data tidak diubah di antara keduanya. Pemeriksaan instructor sudah mereproduksi perbedaan itu; hasil tersebut bukan hasil kerja learner.

Kontrak: kedua peluncuran harus membaca tiga pesanan dari data/orders.txt yang disertakan bersama aplikasi dan melaporkan sukses. Paket aplikasi harus tetap berfungsi ketika seluruh folder lab dipindah ke lokasi lain. Jangan menyalin data ke folder tambahan atau hardcode lokasi D:\Learning. Isi fixture data dipertahankan.

## Dua peluncuran yang dilaporkan

A:
```powershell
Set-Location D:\Learning\Learning-With-AI\labs\diag-005
.\lab.exe
```

B:
```powershell
Set-Location D:\Learning\Learning-With-AI
.\labs\diag-005\lab.exe
```

Ringkasan A: `Impor: selesai, 3 pesanan`. Ringkasan B: `Impor: gagal`.

## Mulai

Sebelum menjalankan command, membuka source, atau mengubah kode: apa satu hipotesis awal yang dapat menjelaskan perbedaan A dan B?

Setelah jawaban itu, pilih satu eksperimen dan prediksi pengamatan yang mendukung atau membantah hipotesis. Source tersedia untuk inspeksi; area perubahan learner adalah main.go. Instructor tidak mengerjakan perbaikan target.

## Build dan pemeriksaan setelah perubahan

```powershell
Set-Location D:\Learning\Learning-With-AI\labs\diag-005
go build -o lab.exe .
```

Build ulang setelah mengubah source. Simpan command, output lengkap, dan status aktual dari pemeriksaan yang dipilih. Keberhasilan: diagnosis didukung hasil eksperimen, perbaikan memenuhi kontrak A/B, dan alasan perbaikan dapat dijelaskan pada satu kondisi peluncuran baru. Pemeriksaan pemindahan folder disiapkan instructor setelah diagnosis; tidak perlu memindahkan folder kerja asli.

Anggaran sesi 60 menit termasuk persiapan dan penutupan. Probe/eksperimen sekitar 30 menit, perbaikan dan verifikasi sekitar 15 menit, sisanya setup/feedback/checkpoint. Scope dapat diperkecil jika fondasi perlu dijelaskan.
