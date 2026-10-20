# Adaptive Learning — Kalibrasi Tantangan V1

Tanggal: 2026-10-06. Acuan kebijakan: `curriculum/competency-map.yaml` versi `1.1.0`.

Outline: tujuan kalibrasi; konteks kesulitan task; sinyal yang diamati; keputusan dalam dan antarsesi; pencatatan; retest dan review.

## 1. Tujuan dan batas

Pilih latihan yang memberikan tantangan bermakna dengan peluang memperoleh pemahaman baru dalam kapasitas learner. Pertahankan prioritas fundamental serta jadwal awal Sabtu–Minggu, 60–120 menit, sesuai `learner/goals.md`.

Gunakan `selection_policy` map untuk urutan target dan prerequisite. Dokumen ini mengatur penyesuaian task, bukan mengganti graph, proficiency, atau target axis. Angka keberhasilan 70–85% bukan probabilitas terukur atau kuota. Tidak ada jaminan tingkat kesulitan akan selalu tepat pada percobaan pertama; kalibrasi merupakan keputusan yang dapat direvisi.

## 2. Rencanakan tantangan sebelum sesi

Periksa evidence relevan, pengalaman dengan task serupa, prerequisite, waktu yang tersedia, dan environment. Pada sesi pertama, gunakan probe kecil untuk menentukan titik awal; jangan menetapkan level dari jabatan atau lama pengalaman.

Tambahkan `difficulty_context` pada metadata lab, mencakup:

| Field | Yang dijelaskan |
| --- | --- |
| `concept_novelty` | Mekanisme apa yang baru/belum diuji atau sudah pernah didemonstrasikan. |
| `integration_scope` | Berapa komponen dan hubungan yang perlu dipikirkan bersama. |
| `failure_complexity` | Jumlah fault, ambiguitas gejala, serta informasi awal yang tersedia. |
| `scaffolding` | Bagian yang disediakan dan bagian yang harus dibuat learner. |
| `constraints` | Invariant, resource, ordering, latency, atau batas lain yang mengubah pilihan solusi. |
| `tooling_familiarity` | Kesiapan sintaks, runtime, dan tooling; unknown jika belum diperiksa. |

Gunakan deskripsi singkat dan spesifik, bukan skor psikologis. Label `difficulty` 1–5 pada lab adalah perkiraan editorial untuk keluarga task yang sebanding. Label itu bukan proficiency learner, bukan `stage` competency, dan tidak menjamin dua lab dengan angka sama memiliki tantangan identik.

Utamakan satu tantangan baru yang dominan. Misalnya, ketika mekanisme concurrency sedang diuji, sediakan fixture dan harness yang tidak menyelesaikan mekanisme itu. Jangan sekaligus memperkenalkan bahasa, framework, database, dan fault baru tanpa alasan integrasi yang didukung prerequisite.

## 3. Sinyal yang diamati

Pertimbangkan sinyal berikut bersama-sama:

- Correctness terhadap invariant dan success criteria.
- Kualitas prediksi, hipotesis, eksperimen, dan pembaruan model setelah observasi.
- Bantuan yang dibutuhkan per axis, termasuk paparan pada solusi serupa.
- Kemajuan: informasi baru yang diperoleh, alternatif yang tersisih, atau pemahaman yang makin tepat.
- Waktu pada reasoning inti dibanding waktu setup, sintaks, atau tooling.
- Feedback learner: terasa terlalu mudah, menantang tetapi produktif, membingungkan, melelahkan, atau membuat frustrasi.

Feedback learner merupakan konteks pengaturan sesi, bukan skor kemampuan. Jangan mengasumsikan perasaan dari keheningan atau lama pengerjaan. Tanyakan singkat pada pergantian tahap, saat terlihat kebuntuan, atau ketika learner menyampaikannya. Tidak perlu meminta rating setelah setiap langkah.

Pertanyaan yang dapat digunakan: “Masih ada hal yang bisa Anda uji sendiri, atau hambatannya sekarang ada pada konsep, tooling, atau energi?” Terima jawaban bebas dan permintaan berhenti tanpa harus membuktikan kemampuan terlebih dahulu.

## 4. Penyesuaian dalam sesi

Tidak perlu menunggu beberapa sesi untuk mengatasi blocker, memberi pengajaran yang dibutuhkan, atau merespons learner yang ingin berhenti. Sebelum memilih tindakan, bedakan masalah task, fondasi, tooling, strategi eksperimen, dan kapasitas saat ini.

| Sinyal | Pemeriksaan singkat | Tindakan |
| --- | --- | --- |
| Selesai cepat dengan reasoning kuat dan varian relevan juga teratasi. | Apakah task memang familiar dan masih ada waktu/energi? | Akhiri target bila evidence cukup; tawarkan satu tantangan tambahan atau siapkan varian berikutnya. Jangan memperpanjang sesi tanpa batas. |
| Selesai cepat tetapi tidak mampu menjelaskan mekanisme. | Periksa prediksi atau perubahan constraint sesuai evaluation rubric. | Pertahankan scope; kumpulkan evidence sebelum menyimpulkan terlalu mudah atau sekadar hafalan. |
| Belum selesai tetapi eksperimen menghasilkan informasi baru. | Apakah informasi membantu menguji hipotesis? | Pertahankan tantangan, beri ruang, atau simpan checkpoint bila waktu habis. |
| Tidak tahu cara mulai karena konsep belum tersedia. | Probe prerequisite yang relevan. | Jelaskan fondasi atau berikan mini-lab; catat transisi ke guided learning. |
| Percobaan berulang tanpa hipotesis atau informasi baru. | Minta satu hipotesis dan prediksi pembeda. | Persempit scope atau beri hint bertahap pada bagian yang menghambat. |
| Hambatan sintaks, instalasi, atau harness. | Verifikasi apakah target mekanisme sudah dapat diamati. | Bantu tooling, perbaiki fixture, dan catat blokir; jangan mengurangi skor mekanisme dari hambatan ini. |
| Learner bosan tetapi kemampuan belum terverifikasi. | Tanyakan apa yang repetitif; gunakan satu probe singkat jika learner bersedia. | Ubah bentuk task atau tawarkan pilihan setara; jangan menganggap bosan sebagai bukti mastery. |
| Learner frustrasi, lelah, atau meminta berhenti. | Tanyakan kebutuhan hanya bila membantu; hormati permintaan yang jelas. | Kurangi scope, beralih ke penjelasan, istirahat, atau checkpoint. Jangan otomatis menyimpulkan proficiency menurun. |
| Hasil eksperimen tidak cocok karena soal/fixture salah. | Periksa validitas task. | Perbaiki task dan catat koreksi; tinjau ulang evidence yang terdampak tanpa menyalahkan learner. |

Tidak ada batas menit universal untuk menyebut learner buntu. Gunakan kualitas kemajuan dan feedback. Instructor boleh mengambil langkah bantuan yang relevan tanpa memaksa learner menebak terus; tingkat bantuan tetap dicatat.

## 5. Penyesuaian antarsesi

Tinjau beberapa observasi yang relevan sebelum menaikkan atau menurunkan level keluarga task. Bandingkan target axis dan konteks kesulitan, bukan sekadar waktu selesai atau jumlah hint pada task yang berbeda total.

- **Naikkan:** terdapat pola reasoning dan aplikasi independen yang kuat pada variasi relevan, dengan hambatan utama yang sudah teratasi.
- **Pertahankan:** task masih menghasilkan informasi baru dan learner mampu mengambil langkah sendiri, atau evidence belum cukup untuk mengubah level.
- **Turunkan scope/remediasi:** terlihat gap fondasi atau kebutuhan bantuan besar yang berulang pada bagian target, setelah masalah tooling dan validitas task dipisahkan.
- **Ganti bentuk:** masalah utamanya repetisi, bahasa baru, atau konteks yang tidak membantu, bukan mekanisme yang terlalu sulit.
- **Tunda:** kapasitas sesi habis, review lain lebih mendesak, atau environment belum tersedia; tunda tidak berarti skor turun.

Ubah satu dimensi dominan pada satu waktu. Jika label level digunakan, ubah satu tingkat sesuai map dan jelaskan apa yang secara konkret berubah. Untuk transfer, bila konteks baru sudah menjadi tantangan utama, pertahankan constraint lain sedapat mungkin.

Contoh progression bukan lab yang sudah dibuat: dari merekonstruksi interleaving pada program kecil, ke menjaga invariant multi-step, kemudian ke konteks baru yang membutuhkan prinsip serupa. Langkah berikutnya dipilih setelah evidence siap, bukan diwajibkan selesai dalam tiga sesi.

## 6. Catatan feedback dan keputusan

Simpan `difficulty_context` di `lab.yaml`. Simpan feedback dan keputusan dalam notes/checkpoint serta ringkasan session history. Jangan menyisipkan mood atau boredom sebagai skor dalam competency state.

Gunakan struktur ringkas berikut saat ada keputusan kalibrasi yang bermakna; template kosong ini bukan data learner:

```yaml
learner_feedback:
  self_report: null
  stated_blocker: null
calibration_decision:
  action: null
  basis_references: []
  rationale: null
  changed_dimension: null
  before: null
  after: null
  next_check: null
```

`action` menggunakan `increase`, `maintain`, `reduce_scope`, `remediate`, `change_format`, atau `pause`. `basis_references` menunjuk observasi/feedback atau evidence yang nyata; keputusan pause berdasarkan permintaan learner tidak membutuhkan skor kemampuan. `next_check` menyatakan apa yang akan diamati untuk menilai apakah penyesuaian membantu. Jika tidak ada perubahan dimensi, before/after dapat null.

Self-report yang tidak ditanyakan tetap null, bukan “normal” atau tebakan instructor. Catat hanya konteks yang relevan untuk belajar. Keputusan perubahan task dipisahkan dari perubahan skor: keduanya bisa terjadi secara independen, dan perubahan skor tetap memerlukan evidence rubric/map.

Jika perlu menurunkan scope setelah sebuah attempt, pertahankan kondisi task lama dan tandai varian baru; jangan menulis ulang konteks kesulitan historis. Gunakan ID stabil sesuai learning-system agar bukti yang sama tidak dihitung dua kali.

## 7. Review dan evaluasi keputusan

Retest dan retrieval mengikuti map serta jadwal aktual. Latihan yang terasa mudah dapat tetap berguna sebagai retrieval singkat, tetapi tidak perlu dijadikan satu sesi repetitif penuh. Satu varian yang gagal tidak menghapus seluruh kemajuan; nilai axis dan kondisi kegagalannya.

Pada penutupan sesi, catat apakah penyesuaian membantu learner mengambil langkah sendiri atau menghasilkan informasi baru. Bila belum diketahui, nyatakan demikian dan gunakan next_check pada sesi berikutnya.

Evaluasi kecocokan rancangan setelah empat sesi nyata sesuai goals. Ukur kemajuan melalui evidence yang sebanding, kualitas reasoning, transfer, dan retensi; jangan menjadikan kecepatan atau mood sebagai ukuran tunggal. Ketentuan ini adalah kebijakan awal yang dapat dikalibrasi, bukan hasil pengujian efektivitas sistem terhadap learner.
