# Mistake Patterns

Diinisialisasi: 2026-10-06.

Outline: syarat pencatatan; template pattern dan pembaruannya; catatan aktual.

## Aturan pencatatan

- Belum ada pola kesalahan yang ditetapkan. Pengalaman kerja, pertanyaan dalam chat, dan contoh dalam kurikulum tidak otomatis menjadi pattern learner.
- Catat perilaku spesifik yang berulang pada beberapa observasi berbeda dan dapat ditelusuri. Beberapa log dari satu kejadian atau satu attempt yang disimpan berulang kali bukan pengulangan independen.
- Satu kesalahan dicatat sebagai observasi di session history. Jika bukti pengulangan masih lemah, lakukan pemeriksaan berikutnya sebelum menetapkan pattern.
- Bedakan kemungkinan gap konsep, strategi reasoning, sintaks/tooling, ketidakjelasan task, dan kondisi sesi. Jangan memberi label kepribadian atau menganggap bosan/frustrasi sebagai kesalahan.
- Hubungkan pattern dengan competency/axis yang relevan jika memang ada evidence. Pattern tidak otomatis menurunkan skor; penilaian tetap mengikuti map dan evaluation rubric.
- Sertakan intervensi yang dapat dicoba dan perilaku perbaikan yang dapat diamati. Tujuannya membantu pilihan latihan, bukan mengumpulkan daftar kekurangan.
- Pertahankan catatan awal dan append pembaruan, termasuk evidence yang menyangkal pattern. Jangan menghapus kegagalan maupun perbaikan historis.
- Gunakan ID stabil seperti `MP-001` hanya ketika pattern nyata dicatat. Status terbaru diperoleh dari pembaruan terakhir, bukan dengan menulis ulang catatan awal.

## Template pattern — bukan diagnosis learner

Isi berdasarkan pengulangan yang benar-benar teramati; jangan menyalin contoh misconception dari dokumen lain menjadi temuan.

```markdown
### <pattern-id> — <deskripsi perilaku spesifik>

- Tanggal pencatatan:
- Status: active
- Perilaku berulang yang diamati:
- Konteks saat muncul dan batas generalisasinya:
- Referensi observasi yang berbeda: <session/checkpoint/evidence IDs atau notes yang nyata>
- Competency IDs/axis terkait, jika didukung:
- Interpretasi sementara dan penjelasan alternatif:
- Evidence yang berlawanan atau keterbatasan kesimpulan:
- Intervensi yang akan dicoba:
- Perilaku perbaikan yang ingin diamati:
- Kapan/kondisi pemeriksaan berikutnya:
```

Append pembaruan memakai format ringkas:

```markdown
#### <update-id> untuk <pattern-id>
- Waktu aktual (+07:00):
- Status saat pembaruan: active / improving / resolved / retracted
- Observasi baru dan references:
- Hasil intervensi serta alasan perubahan status:
- Langkah berikutnya atau batas yang masih perlu diperiksa:
```

`improving` memerlukan observasi perubahan perilaku. `resolved` memerlukan perbaikan yang berulang pada konteks relevan, bukan satu keberhasilan atau sekadar tidak ada sesi baru. `retracted` digunakan jika interpretasi awal ternyata tidak didukung, misalnya fault berasal dari fixture. Jika pattern muncul kembali, append pembaruan `active` dengan evidence baru dan konteksnya.

## Catatan aktual

<!-- Append pattern dan pembaruan yang berbasis evidence di bawah ini. Belum ada pattern tercatat. -->


### MP-001 — Kondisi penggantian error ikut membatasi cleanup

- Tanggal: 2026-10-26. Status: improving; pola terbatas pada dua task cleanup dengan mekanisme serupa.
- Observasi: conditional Close saat error kosong muncul pada patch diag-006 tanggal 23 Oktober (notes s04-o03) dan usulan awal review-001 tanggal 26 Oktober (notes s01-o01). Keduanya dapat melewatkan cleanup ketika operasi sebelumnya gagal.
- References: labs/diag-006/attempts/a001/notes.md — s04-o03/o04; labs/review-001/attempts/a001/notes.md — 2026-10-26-s01-o01/o02/o03.
- Kompetensi: os.files-and-descriptors, concept/implementation. Bukan diagnosis umum tentang kemampuan atau karakter learner.
- Evidence perbaikan: pada retrieval baru learner mengenali jalur terlewat dan menyusun repair setelah H1; sebelumnya membutuhkan bantuan H5. Patch sekarang lulus empat kasus termasuk kegagalan ganda. Kemiripan task membatasi generalisasi; belum resolved.
- Intervensi: minta trace kontrol terhadap kontrak cleanup sebelum patch; pisahkan reasoning menjalankan operasi dari memilih hasilnya. Hindari memberikan solusi sebelum attempt.
- Next check: retrieval berikut dengan bentuk resource/return berbeda, periksa apakah invariant cleanup dikenali tanpa prompt tambahan. Tidak ada penalti skor otomatis.
