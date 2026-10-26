# Review 001 — Penyimpanan bukti pembayaran

Pemanggil memakai hasil `saveReceipt` untuk menentukan apakah penyimpanan berhasil.
`dst` sudah dibuka sebelum fungsi dipanggil; fungsi ini bertanggung jawab menutupnya.

Kontrak:
- Simpan tepat satu baris `PAY-042,paid` diikuti newline.
- Kembalikan kegagalan penyimpanan jika terjadi; keberhasilan operasi berikutnya tidak membatalkannya.
- Jika penyimpanan berhasil tetapi penutupan gagal, kembalikan kegagalan tersebut.
- Tutup tujuan tepat sekali, termasuk pada jalur gagal.

Mulai dengan membaca `save.go`, tanpa menjalankan test atau membuka solusi lama.
Prediksi hasil fungsi ketika tujuan menolak penulisan dengan error `destination full`, tetapi `Close` berhasil. Jelaskan urutan kejadian yang mendasari prediksi.

Sesudah prediksi, pilih eksperimen lalu gunakan test dari folder ini:
```powershell
go test -v .
```

Area implementasi learner: `save.go`. Test adalah fixture instructor; pertahankan kontraknya.
Tujuan di test adalah simulasi deterministik, bukan disk Windows sungguhan.
