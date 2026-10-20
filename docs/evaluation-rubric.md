# Evaluation Rubric — Pembuktian Pemahaman V1

Tanggal: 2026-10-06. Acuan kebijakan: `curriculum/competency-map.yaml` versi `1.1.0`.

Outline: batas penilaian; rencana verifikasi; jenis pemeriksaan mekanisme; anchor lima axis; bantuan dan validitas; pencatatan serta contoh keputusan.

## 1. Batas dan sumber aturan

Rubric ini mengoperasionalkan outcome dan assessment policy pada map. Skala 0–4, makna null, confidence, proficiency, dan syarat mastery tetap berasal dari map. Tidak ada skor tambahan untuk kelancaran berbicara, kecepatan, motivasi, atau rasa percaya diri.

Pemahaman disimpulkan secara terbatas dari evidence; satu task tidak membuktikan penguasaan seluruh domain. Instructor menjelaskan apa yang sudah teramati, dalam kondisi apa, dan bagian yang masih belum diuji. Temuan baru dapat memperkuat atau merevisi kesimpulan sebelumnya.

## 2. Rencanakan verifikasi sebelum task diberikan

Pada metadata lab, tambahkan `verification_plan` yang mencatat target axis, jenis pemeriksaan, perilaku yang akan diamati, dan batas bantuan. Rencana ini merupakan metadata instructor; jangan tampilkan petunjuk solusi saat blind diagnostic.

- Pilih satu atau dua axis utama berdasarkan tujuan sesi.
- Tentukan observable success criteria sebelum melihat hasil learner. Jangan memindahkan kriteria hanya agar learner terlihat berhasil atau gagal.
- Pilih pemeriksaan yang cocok dari bagian 3. Tidak perlu menjalankan seluruh pemeriksaan pada setiap task.
- Pisahkan hasil eksekusi, penjelasan mekanisme, bantuan, dan transfer.
- Siapkan kemungkinan varian atau retest, tetapi jangan menambahkannya tanpa mempertimbangkan timebox dan persetujuan learner untuk melanjutkan sesi.

Jika task atau kriteria harus berubah karena fixture bermasalah, catat alasan serta versi/varian baru. Jangan menilai attempt lama dengan kriteria baru secara retroaktif.

## 3. Jenis pemeriksaan mekanisme

Nama `check_type` berikut digunakan untuk pencatatan, bukan axis baru atau daftar wajib.

| check_type | Pertanyaan atau eksperimen | Evidence yang bernilai | Batas kesimpulan |
| --- | --- | --- | --- |
| `prediction` | Sebelum eksekusi, minta prediksi perilaku dan alasan. | Prediksi memuat mekanisme/asumsi; learner membandingkannya dengan hasil. | Hasil benar tanpa alasan bisa berasal dari tebakan atau pengalaman dengan soal sama. |
| `causal_explanation` | Minta urutan kejadian, perubahan state, resource lifetime, atau interleaving. | Rantai sebab-akibat konsisten dengan observasi. | Menyebut istilah seperti race condition tanpa menjelaskan kejadian belum cukup. |
| `discriminating_experiment` | Minta eksperimen yang dapat membedakan hipotesis dari alternatif. | Learner menyatakan hasil yang akan mendukung atau membantah hipotesis. | Trial-and-error yang akhirnya berhasil belum membuktikan diagnosis terarah. |
| `constraint_change` | Ubah satu constraint yang mengubah asumsi atau keputusan. | Learner memprediksi konsekuensi dan menyesuaikan pendekatan dengan alasan. | Mengganti nama variabel atau angka tanpa perubahan reasoning bukan bukti transfer yang kuat. |
| `boundary_case` | Minta kondisi ketika solusi tidak cocok atau membutuhkan pendekatan lain. | Learner mengenali asumsi, invariant, dan failure mode tersisa. | Pertanyaan ini dapat menguji judgment; jangan otomatis memberi skor semua axis. |
| `transfer` | Berikan konteks baru tanpa menyebut mekanisme target. | Learner mengenali prinsip yang relevan, lalu memeriksa asumsi konteks baru. | Kesulitan sintaks atau pengetahuan domain baru dapat mengaburkan evidence; bedakan keduanya. |
| `delayed_retrieval` | Uji kembali setelah jeda sebelum memperlihatkan solusi sebelumnya. | Learner merekonstruksi reasoning pada task/varian yang sesuai. | Melanjutkan kode yang sama sambil membaca catatan solusi bukan dengan sendirinya retest independen. |

Prediksi dapat berupa beberapa kemungkinan ketika perilaku memang nondeterministik. Nilai apakah learner dapat menjelaskan kondisi pemicunya; jangan menuntut satu output pasti untuk sistem yang tidak menjaminnya.

Setelah task berhasil, lakukan verifikasi terarah sesuai AGENTS.md. Setelah attempt gagal atau belum selesai, gunakan pemeriksaan yang sama bila dapat mengungkap pemahaman tanpa mengambil alih pekerjaan. Berhenti ketika evidence sudah cukup untuk tujuan sesi; jangan menjadikan setiap keberhasilan awal sebagai rangkaian ujian tanpa akhir.

## 4. Anchor untuk lima axis

Tabel ini membantu mengenali evidence aplikasi independen yang dapat mendukung skor 3 sesuai map. Tidak ada promosi otomatis: pertimbangkan representativitas task, bantuan, bukti sebelumnya, dan bagian yang benar-benar teramati.

| Axis | Evidence aplikasi independen | Evidence yang belum cukup dengan sendirinya |
| --- | --- | --- |
| `concept` | Menjelaskan mekanisme, membuat prediksi yang beralasan, dan mengenali asumsi relevan. | Hafal definisi, memakai istilah yang tepat, atau mengulang penjelasan instructor. |
| `implementation` | Menulis mekanisme inti yang menjaga invariant dan memeriksa jalur relevan secara mandiri. | Test hijau setelah menerima pseudocode/solusi atau scaffold yang sudah mengerjakan mekanisme inti. |
| `debugging` | Menghubungkan gejala, hipotesis, eksperimen pembeda, serta evidence root cause. | Fix kebetulan berhasil, mengganti banyak konfigurasi sekaligus, atau mengulang diagnosis yang diberikan. |
| `judgment` | Memilih alternatif berdasarkan constraint dan menjelaskan kondisi yang dapat mengubah keputusan. | Mengutip best practice tanpa mengaitkannya dengan kebutuhan serta failure mode task. |
| `transfer` | Mengenali dan menerapkan prinsip pada situasi baru, termasuk menguji ulang asumsi yang berubah. | Mengikuti instruksi menerapkan pola yang sudah disebutkan atau mengganti angka/nama pada solusi lama. |

Nilai 4 dan label mastered tetap memerlukan variasi evidence independen, retest tertunda, transfer, serta syarat lain pada map. Jangan mengartikan tabel ini sebagai daftar yang harus dipenuhi seluruhnya oleh satu task.

## 5. Bantuan, exposure, dan ketidakpastian

- Catat bantuan per axis dan tahap attempt. Evidence sebelum bantuan dapat tetap independen; jangan menyebut keseluruhan attempt H0 jika bagian lain mendapat hint.
- Bedakan dokumentasi sintaks/API dari sumber yang menunjukkan solusi target. Penggunaan dokumentasi tidak otomatis menjadi hint konsep; nilai isi bantuan terhadap mekanisme yang diuji.
- Paparan judul task, reference solution, atau penjelasan sebelumnya dapat memberi petunjuk. Catat exposure yang diketahui tanpa menuduh learner atau mengklaim mampu mendeteksi semua bantuan yang tidak teramati.
- Jika bantuan atau artefak tidak cukup dapat ditelusuri, batasi klaim independence/confidence dan pilih pemeriksaan baru yang sesuai.
- Jawaban verbal yang pendek atau kurang lancar dapat dilengkapi dengan diagram, pseudocode, trace, prediksi, atau eksperimen. Jangan mengubah penilaian menjadi tes kefasihan berbicara.
- Jika prediksi salah tetapi learner mengidentifikasi asumsi yang keliru melalui eksperimen, catat kedua observasi. Ini dapat menunjukkan perkembangan reasoning, bukan otomatis skor 0 atau mastery.
- Jika fixture atau pertanyaan instructor ternyata salah/ambigu, koreksi assessment yang terdampak melalui catatan koreksi; jangan menurunkan kemampuan learner karena kesalahan task.

Gunakan `assessed`, `not_observed`, dan `blocked` sesuai map. Kegagalan retest menjadi evidence baru; ketidaktersediaan waktu retest tidak setara dengan kegagalan.

## 6. Mencatat hasil pemeriksaan

Pertahankan seluruh evidence fields map. Dalam `reasoning_check`, gunakan record terstruktur berikut untuk pemeriksaan yang dilakukan; contoh ini template kosong, bukan hasil learner:

```yaml
reasoning_check:
  check_type: null
  prompt: null
  learner_response: null
  observation_reference: null
  interpretation: null
  limitations: []
```

Isi `check_type` dengan salah satu jenis pada bagian 3. Simpan prompt dan respons yang cukup spesifik agar penilaian dapat ditinjau; kutipan lengkap tidak diperlukan jika ringkasan setia sudah memadai. Interpretation harus membedakan fakta observasi dari kesimpulan instructor. Assistance tetap berada pada `max_hint` dan `prompt_context` evidence terkait, bukan disembunyikan dalam kesimpulan.

Jika tidak dilakukan pemeriksaan reasoning, gunakan `reasoning_check: null` dan catat keterbatasan observasinya. Field null tidak membatalkan seluruh evidence, tetapi membatasi klaim pada perilaku yang benar-benar diamati. Untuk beberapa pemeriksaan, buat record evidence terpisah yang merujuk attempt sama; jangan menghitungnya sebagai task independen berbeda.

Pada history, rangkum: capability yang didukung, kondisi/assistance, uncertainty yang tersisa, dan probe berikutnya. Simpan perubahan skor beserta alasan; tidak setiap pemeriksaan harus mengubah skor.

## 7. Contoh keputusan — bukan assessment learner

| Situasi ilustratif | Keputusan yang dapat dipertanggungjawabkan |
| --- | --- |
| Solusi cepat dan test hijau, tetapi penjelasan hanya mengulang istilah. | Periksa prediksi atau rantai sebab-akibat. Jangan langsung menaikkan kompleksitas maupun menyimpulkan hafalan. |
| Learner mendiagnosis sendiri, kemudian meminta pseudocode perbaikan. | Simpan evidence debugging independen yang mendahului bantuan; implementation terkait dicatat terbantu. |
| Learner menjelaskan mekanisme dengan benar tetapi lupa sintaks Go. | Bantu sintaks sesuai scope; pertahankan atribusi concept berdasarkan observasi, lalu nilai implementation yang benar-benar dilakukan. |
| Learner berhasil pada kasus dekat, tetapi belum diuji pada konteks baru. | Nyatakan batas evidence; rencanakan transfer ketika siap, bukan memberi skor transfer dari dugaan. |
| Retest belum dilaksanakan karena sesi terlewat. | Pertahankan state dan status review yang sesuai; jangan menyamakan jadwal terlewat dengan lupa materi. |

Aturan ini merupakan rancangan operasional. Evaluasi kualitasnya melalui sesi nyata dan perbaiki dengan evidence, tanpa menjanjikan bahwa satu format assessment dapat memastikan pemahaman secara mutlak.
