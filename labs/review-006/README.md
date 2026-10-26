# Review 006 — Pengiriman paket laporan

Mode: retrieval implementasi mandiri. Area kerja: `batch.go`, fungsi `runBatch`.
`main.go` dan `fixture.go` adalah infrastruktur instructor.

Sebuah batch memiliki dua program eksternal: `prepare` menyiapkan paket dan
`publish` mengirimkannya. Kedua command sudah dikonfigurasi, tetapi pengendali
batch belum diimplementasikan.

## Kontrak

- Jalankan `prepare` tepat sekali. Jalankan `publish` tepat sekali hanya jika
  `prepare` sudah selesai dengan sukses.
- Jika salah satu tahap gagal, batch berakhir dengan status 1. Ini juga berlaku
  bila program tidak dapat dijalankan.
- Hanya jika kedua tahap berhasil, tulis `Batch: selesai` dan akhiri dengan status 0.
- Jangan mengandalkan isi stdout/stderr sebagai penentu sukses. Output tahap harus
  tetap terlihat melalui konfigurasi yang sudah tersedia.
- Jangan hardcode skenario, mengubah fixture, atau memanggil `os.Exit` dari
  `runBatch`; fungsi ini mengembalikan status ke pemanggilnya.

## Mulai

Baca kontrak dan `batch.go`. Sebelum menulis kode atau menjalankan skenario,
jelaskan urutan keputusan yang akan dilakukan pengendali agar kontrak terpenuhi.
Setelah respons awal, implementasikan dan uji.

```powershell
Set-Location D:\Learning\Learning-With-AI\labs\review-006
go build -o lab.exe .
.\lab.exe ok
$LASTEXITCODE
```

Ganti argumen `ok` dengan kasus lainnya dan baca `$LASTEXITCODE` segera setelah
setiap eksekusi:

| Kasus | Perilaku fixture | Hasil batch yang diwajibkan |
| --- | --- | --- |
| `ok` | Kedua tahap sukses | prepare lalu publish, pesan selesai, status 0 |
| `reject` | prepare menolak input | publish tidak berjalan, tanpa pesan selesai, status 1 |
| `publish-reject` | publish berakhir gagal tanpa pesan error | kedua tahap berjalan, tanpa pesan selesai, status 1 |
| `unavailable` | program prepare tidak tersedia | publish tidak berjalan, tanpa pesan selesai, status 1 |

Starter sengaja belum memenuhi kontrak; status 2 dari TODO bukan kegagalan setup.
Keberhasilan mencakup kode learner, hasil empat kasus, dan satu penjelasan kausal
setelah pengujian. Ini tidak menguji signal atau shutdown service.
