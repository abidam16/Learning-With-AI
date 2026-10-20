# Learning System — Prosedur Sesi V1.1

Tanggal: 2026-10-06. Selaras dengan competency map `1.1.0`.
Dokumen ini menetapkan prosedur; keberadaannya tidak berarti repository, environment, learner state, atau lab runnable sudah dibuat.

Revisi V1.1 menghubungkan pembuktian pemahaman dan kalibrasi kesulitan ke prosedur sesi, tanpa mengubah skala skor atau graph competency map.

## Outline

1. Acuan dan pembagian tanggung jawab.
2. Bootstrap dan pemeriksaan environment.
3. Memulai atau melanjutkan sesi.
4. Menyiapkan dan mengerjakan latihan.
5. Meminta bantuan dan memverifikasi pemahaman.
6. Berhenti di tengah dan memulihkan sesi.
7. Menilai evidence dan menyimpan perkembangan.
8. Retrieval, review, serta panduan penggunaan singkat.

## 1. Acuan dan tanggung jawab

Tujuan utama adalah fundamental dan penalaran engineering independen. Ikuti `AGENTS.md` untuk batas learner ownership dan perilaku instructor; `curriculum/competency-map.yaml` untuk ID, prerequisite, hint, scoring, confidence, proficiency, dan prioritas pemilihan latihan. Dokumen ini menjelaskan cara menjalankannya tanpa membuat skala penilaian baru.

`learner/profile.md` menyediakan konteks learner dan environment. `learner/goals.md` menyediakan fokus serta kapasitas waktu. Jika file pendukung opsional seperti rubric belum dibuat, gunakan map dan AGENTS.md; jangan mengarang isinya. Jika versi map berbeda atau ada aturan yang bertentangan, selesaikan konflik yang memengaruhi penilaian sebelum memberi skor terkait; pekerjaan yang tidak terdampak dapat berlanjut.

Untuk paket dokumen saat ini, gunakan [evaluation-rubric.md](evaluation-rubric.md) ketika menyusun pemeriksaan dan menilai evidence, serta [adaptive-learning.md](adaptive-learning.md) ketika memilih atau menyesuaikan tantangan. Sertakan keduanya saat memasang dokumen ke repository. Hint policy tambahan tetap opsional; kebijakan utama tersedia pada map.

| Tanggung jawab learner | Tanggung jawab instructor |
| --- | --- |
| Mengemukakan prediksi dan hipotesis. | Memilih target berdasarkan state dan tujuan. |
| Menulis implementasi inti dan menentukan eksperimen. | Menyiapkan scaffold, fixture, harness, dan environment. |
| Menjelaskan hasil serta mempertimbangkan alternatif. | Memberi bantuan sesuai kebutuhan tanpa mengambil alih reasoning. |
| Menyampaikan kendala, kebutuhan bantuan, atau keinginan berhenti. | Mengatribusikan evidence, menyimpan state, dan menyiapkan kelanjutan. |

Instructor mengurus pencatatan administratif. Learner cukup menyampaikan reasoning dan melakukan pekerjaan inti; tidak perlu menyalin seluruh percakapan ke dokumen.

## 2. Bootstrap sebelum sesi pertama

### 2.1 Pastikan repository dan aksesnya nyata

Gunakan environment pilihan learner: Windows native, VS Code, dan Codex melalui ChatGPT desktop. Pastikan sesi instructor benar-benar dapat membaca folder repository yang dimaksud. Pemilihan aplikasi desktop saja bukan bukti akses file lokal.

Jika akses belum tersedia, jelaskan keterbatasan dan bantu setup. Jangan mengaku menjalankan command, menulis file, atau menyimpan state lokal hanya karena langkahnya sudah dijelaskan di chat.

Saat bootstrap diminta, siapkan file minimum yang belum ada, tanpa mereset file yang sudah berisi pekerjaan:

- `AGENTS.md`, `README.md`, dan `curriculum/competency-map.yaml` versi yang disepakati.
- `learner/profile.md`, `learner/goals.md`, dan dokumen ini.
- `learner/competency-state.yaml`, dengan seluruh competency memakai initial state dari map.
- `learner/session-history.md` dan `learner/mistake-patterns.md`, diawali struktur kosong.

Semua skor awal `null`, confidence `none`, proficiency `unseen`, evidence kosong, dan `review_due: false`. Jangan memasukkan contoh pada dokumen ini sebagai hasil assessment. Struktur lengkap file state akan ditetapkan ketika file tersebut dibuat; pertahankan nama field dan ID yang sudah ditetapkan map.

### 2.2 Pemeriksaan environment

Kenali shell aktual dan gunakan command yang kompatibel. Untuk lab Go awal, periksa Git, Go, working directory, serta kemampuan menjalankan program dan test kecil. Catat versi serta command yang benar-benar diuji di README atau catatan setup. Pemeriksaan ini bukan assessment mastery.

Jangan mengasumsikan Bash, WSL, Docker, atau database tersedia. Siapkan dependency tambahan hanya jika lab membutuhkannya. Jika mekanisme khusus Linux menjadi target, jelaskan kebutuhan environment yang sesuai; jangan mengganti pilihan Windows secara diam-diam atau menganggap semua perilaku OS identik.

Masalah setup dicatat sebagai environment blocker. Jika akses atau runtime belum siap, dapat dilakukan probe konseptual yang relevan; kemampuan implementasi yang belum teramati tetap belum dinilai.

## 3. Memulai sesi

Learner dapat mengatakan: “Mulai sesi hari ini, saya punya 90 menit.” Jika durasi tidak disebutkan, gunakan 60 menit sebagai anggaran awal yang mudah diperpanjang; tidak perlu menanyakan ulang preferensi yang sudah tercatat. Jadwal normal adalah Sabtu dan Minggu, tetapi sesi tambahan yang dimulai learner tetap dapat dijalankan.

### 3.1 Baca konteks secara terarah

Instructor membaca:

1. AGENTS.md, profile, goals, serta kebijakan dalam map.
2. Competency state dan checkpoint pekerjaan yang belum selesai.
3. History terbaru, review yang jatuh tempo, serta mistake patterns yang relevan.
4. Evidence lama hanya ketika diperlukan untuk keputusan prerequisite, retest, atau perubahan skor.

Periksa apakah penyimpanan sesi sebelumnya lengkap sebelum menilai data sebagai state terkini. Unknown tidak boleh dianggap lemah atau kuat.

### 3.2 Pilih satu target utama

Ikuti prioritas map: pekerjaan aktif/environment blocker; prerequisite yang menghambat; retrieval due; pola berulang dan kelemahan implementation/debugging; evidence penting yang kosong; lalu transfer/integrasi yang sesuai. Tujuan fundamental memandu semua pilihan tersebut.

- Pilih satu target utama dengan satu atau dua axis utama. Node pendukung boleh ikut teramati.
- Probe prerequisite yang belum diketahui sebelum menyimpulkan perlu remediasi.
- Gunakan gate map: default concept dan implementation minimal 2 dengan evidence relevan; metadata lab boleh mempersempit axis dengan alasan yang jelas.
- Diagnostic boleh melewati gate untuk mengamati baseline. Recommended preparation tidak menjadi gate wajib.
- Jika belum ada baseline, lakukan beberapa probe kecil; jangan mencoba menilai 38 kompetensi dalam satu sesi.

### 3.3 Sampaikan pembukaan singkat

Sampaikan mode sesi, masalah/tujuan, alasan pemilihan, batas waktu, success criteria, dan tindakan pertama learner. Mode yang digunakan:

| Mode | Penggunaan |
| --- | --- |
| Diagnostic/retest independen | Mengamati baseline atau kemandirian pada varian yang sesuai; mulai H0. |
| Guided learning | Membangun konsep yang belum tersedia; penjelasan dan contoh diperbolehkan, dengan assistance tercatat. |
| Praktik | Mengimplementasikan, debugging, atau mengambil keputusan; bantuan mengikuti kebutuhan. |
| Demonstrasi | Menunjukkan solusi sesuai permintaan atau kesepakatan setelah assessment; bukan evidence implementasi mandiri. |

Pada blind diagnostic, jelaskan nilai belajarnya secara umum tanpa membocorkan mekanisme, nama fault, atau solusi. Jangan memperlihatkan metadata instructor yang mengarahkan jawaban. Repository tetap dapat diakses learner; ini bukan mekanisme pengamanan atau jaminan bahwa soal belum pernah terlihat.

## 4. Menyiapkan latihan

Instructor menyiapkan lab yang cukup kecil untuk memberi evidence bermakna dalam waktu tersedia. Metadata `lab.yaml` minimal memuat ID, task variant, jenis latihan, tingkat kesulitan, primary/secondary competency IDs, target axes, prerequisite relevan, estimasi waktu, dan success criteria. Deskripsi environment harus membedakan kebutuhan wajib dari alat bantu opsional.

Tambahkan `verification_plan` sesuai evaluation rubric dan `difficulty_context` sesuai adaptive-learning. Verification plan menyebut axis, jenis pemeriksaan, observable evidence, dan batas bantuan; difficulty context menjelaskan kebaruan konsep, lingkup integrasi, kompleksitas fault, scaffold, constraint, serta familiaritas tooling. Pilih pemeriksaan yang relevan, bukan seluruh daftar pada setiap sesi. Tetapkan success criteria sebelum attempt dan catat perubahan task sebagai varian yang dapat ditelusuri.

Struktur pendukung yang dapat digunakan ketika diperlukan:

| Lokasi | Isi |
| --- | --- |
| `labs/<lab-id>/README.md` | Gejala, constraint, command awal, dan success criteria untuk learner. |
| `labs/<lab-id>/lab.yaml` | Metadata instructor; jangan tampilkan petunjuk target saat blind diagnostic. |
| Kode, test, dan fixture dalam folder lab | Scaffold dan area kerja learner. |
| `labs/<lab-id>/attempts/<attempt-id>/notes.md` | Prediksi, eksperimen, bantuan, dan checkpoint attempt. |
| `labs/<lab-id>/attempts/<attempt-id>/artifacts/` | Output atau snapshot relevan yang mendukung evidence. |

Folder pendukung dibuat ketika dipakai, bukan sebagai syarat memiliki banyak berkas kosong. Reference solution dipisahkan dari area learner dan baru ditampilkan untuk demonstrasi yang diizinkan.

Sebelum memberikan task, verifikasi command/harness dan gejala yang memang dimaksud. Bedakan test yang sengaja gagal dari environment rusak. Jangan memberi solusi di scaffold, nama file, atau assertion message yang terlalu mengarahkan. Jika sebagian lab belum bisa diverifikasi, nyatakan bagian tersebut; jangan membuat learner menanggung ketidakpastian itu sebagai kegagalan kemampuan.

## 5. Mengerjakan latihan

Jalankan loop berikut dalam percakapan biasa; instructor merangkum evidence tanpa meminta formulir panjang setiap kali:

1. **Pahami:** learner menyebutkan perilaku yang seharusnya dan observasi saat ini.
2. **Prediksi:** learner mengajukan hipotesis dan hasil yang diharapkan jika hipotesis benar.
3. **Uji:** learner memilih eksperimen yang dapat membedakan hipotesis dari alternatif; ubah satu variabel bila praktis.
4. **Amati:** simpan command, output relevan, serta apa yang berubah.
5. **Revisi:** pertahankan atau ubah hipotesis berdasarkan evidence.
6. **Perbaiki:** learner menulis perbaikan dan menguji constraint atau failure path yang relevan.
7. **Jelaskan:** learner menerangkan mengapa perbaikan bekerja dan batasnya.

Untuk implementation task, gunakan invariant dan contoh input/output sebagai titik awal. Untuk design task, gunakan constraint, alternatif, dan alasan memilihnya. Jangan memaksakan format incident debugging pada setiap jenis latihan.

Instructor boleh membaca kode dan menjalankan pemeriksaan untuk feedback. Jangan menyisipkan perbaikan inti tanpa permintaan bantuan yang mencakupnya, mengubah expected result agar test hijau, atau menyelesaikan TODO learner. Jika diagnosis instructor menghasilkan clue yang disampaikan, catat sebagai bantuan.

Jika learner belum memiliki konsep yang dibutuhkan, beralih ke penjelasan singkat atau contoh berbeda, kemudian kembali ke attempt baru. Untuk Go, pisahkan kesulitan sintaks dari reasoning mekanisme. Fakta bahwa learner pernah belajar sintaks tidak membuktikan semua kemampuan tooling atau bahasa sudah siap.

Pada transisi yang relevan atau saat ada kebuntuan, periksa apakah learner masih memperoleh informasi baru dan bagaimana tantangan dirasakan. Ikuti tabel keputusan adaptive-learning: kemajuan reasoning dapat membenarkan mempertahankan scope meski task belum selesai; gap fondasi memerlukan pengajaran; hambatan tooling memerlukan bantuan setup. Tanggapi kebutuhan berhenti segera, tanpa menunggu pola beberapa sesi. Perubahan level task berikutnya tetap didasarkan pada beberapa observasi yang sebanding.

## 6. Meminta bantuan

Learner tidak harus mengingat nomor hint. Instructor memetakan permintaan dan isi bantuan ke ladder map:

| Permintaan learner | Respons instructor |
| --- | --- |
| “Maksud constraint ini apa?” | Klarifikasi netral; H1 hanya jika tidak mengarahkan konsep atau solusi. |
| “Beri satu hint dulu.” | Beri satu tingkat bantuan berikutnya, lalu tunggu attempt. |
| “Aku belum paham konsep ini.” | Jelaskan fondasi yang hilang; catat bantuan pada axis terdampak. |
| “Tunjukkan pseudocode.” | Beri bantuan H5 sesuai lingkup yang diminta; tidak otomatis menulis seluruh implementasi. |
| “Tunjukkan solusi lengkap.” | Beri H6, pertahankan attempt sebelumnya, dan tandai bagian independen yang berakhir. |

Default eskalasi bertahap H0–H6 mengikuti map. Permintaan eksplisit untuk bantuan lebih kuat tidak perlu dipaksa melewati semua tingkat. Ajukan satu pertanyaan reasoning pada satu waktu.

Catat isi bantuan, waktu/tahap pemberian, dan maksimum hint per axis. Bantuan dalam prompt dan scaffold ikut diperhitungkan. Bantuan setup atau sintaks dicatat terpisah, kecuali turut menyelesaikan mekanisme yang diuji. H2 atau lebih tidak membuktikan kemandirian pada bagian terbantu; evidence independen sebelum bantuan atau pada bagian lain tetap dapat dipakai sesuai cakupannya.

Setelah demonstrasi, learner boleh menjelaskan atau memodifikasi contoh untuk belajar. Jangan menganggap pengulangan solusi yang baru diberikan sebagai retest independen. Gunakan varian baru yang bermakna dan retest tertunda ketika relevan; simpan hubungan dengan attempt sebelumnya.

## 7. Mengakhiri task dan memverifikasi pemahaman

Saat success criteria tercapai, periksa pemahaman dengan satu pertanyaan atau eksperimen yang sesuai: mengapa solusi bekerja, alternatif yang masuk akal, failure mode tersisa, atau perubahan constraint.

Gunakan evaluation rubric untuk menghubungkan pemeriksaan dengan axis dan batas kesimpulannya. Prediksi dilakukan sebelum hasil diperlihatkan; variasi transfer harus mengubah reasoning yang dibutuhkan; retest tertunda harus dibedakan dari melanjutkan attempt lama. Selesai cepat dengan penjelasan lemah memicu probe terarah, bukan kenaikan level otomatis. Dokumentasi sintaks/API tidak otomatis sama dengan bantuan solusi; catat isi bantuan yang relevan.

Jika jawabannya belum jelas, probe ketidakpastian spesifik. Jangan otomatis menurunkan skor concept dari satu jawaban verbal yang tidak lengkap. Ubah skor hanya ketika evidence cukup, dengan alasan yang dapat ditelusuri. Satu task tidak harus menguji semua axis, dan satu perubahan angka/input belum tentu menguji transfer.

Task boleh dihentikan ketika timebox berakhir, learner lelah, tujuan observasi sudah tercapai, atau blocker membuat eksperimen berikutnya tidak bernilai. Tidak harus menunggu seluruh test hijau untuk mencatat evidence debugging yang valid.

## 8. Berhenti di tengah dan melanjutkan

Saat learner mengatakan “berhenti dulu” atau menyebut waktu hampir habis, hentikan penambahan tugas dan prioritaskan checkpoint. Jangan menyelesaikan latihan atas nama learner untuk menutup sesi.

Pisahkan tiga hal:

| Yang dicatat | Arti |
| --- | --- |
| Status sesi `completed` / `paused` / `blocked` | Sesi mencapai penutupan yang direncanakan, terhenti dengan pekerjaan terbuka, atau terhambat blocker. `completed` tidak berarti mastered. |
| Status assessment `assessed` / `not_observed` / `blocked` | Apakah axis mempunyai evidence cukup untuk dinilai. |
| Status penyimpanan lengkap / belum lengkap | Apakah artefak, state, dan history sudah konsisten tersimpan. |

Gunakan template checkpoint berikut di notes attempt; placeholder adalah instruksi pengisian, bukan evidence nyata:

```markdown
## Checkpoint <checkpoint-id>
- Session ID dan waktu aktual:
- Lab ID / task variant / attempt ID:
- Status sesi dan alasan:
- Tujuan dan success criteria yang sudah/belum tercapai:
- Hipotesis terakhir dan alternatif yang belum tersisih:
- Eksperimen terakhir, command, dan hasil observasi:
- File/artefak relevan beserta lokasi atau snapshot:
- Bantuan yang sudah diberikan dan axis terdampak:
- Pemeriksaan mekanisme: prompt, respons/observasi, interpretasi, dan keterbatasan:
- Feedback learner tentang tantangan/blocker, jika disampaikan:
- Keputusan kalibrasi: dasar observasi, dimensi sebelum/sesudah, dan next check:
- Evidence baru yang layak dinilai; bagian yang belum teramati:
- Perubahan state yang akan diterapkan, atau alasan tidak berubah:
- Blocker, bila ada:
- Langkah berikutnya yang dapat langsung dilakukan:
```

Langkah berikutnya harus konkret, misalnya menjalankan kembali command tertentu setelah perubahan tertentu dan membandingkan output. “Lanjut belajar concurrency” belum cukup untuk melanjutkan attempt.

Pada sesi berikutnya, baca checkpoint terakhir, periksa kondisi kode/environment aktual, dan minta learner merangkum kembali reasoning singkat. Lanjutkan hipotesis dan eksperimen terbuka. Jika file telah berubah sejak checkpoint, catat perubahan; jangan mengklaim output lama berasal dari kode baru. Jika crash terjadi sebelum checkpoint, pulihkan dari artefak yang benar-benar ada dan tanyakan observasi yang hilang tanpa mengarang hasil.

## 9. Identitas sesi, attempt, dan evidence

Gunakan konvensi ringan berikut; seluruh contoh ID hanya ilustrasi:

- `session_id`: `YYYY-MM-DD-sNN`, berdasarkan tanggal Asia/Jakarta dan nomor unik hari itu.
- `lab_id` serta `task_variant`: identitas latihan dan variasinya; jangan mengubah arti varian setelah evidence tercatat.
- `attempt_id`: unik dalam lab, misalnya `a001`; dapat berlanjut pada beberapa sesi.
- `checkpoint_id`: gabungan session ID dan nomor checkpoint, misalnya `YYYY-MM-DD-s01-cp01`.
- `evidence_id`: identitas stabil untuk satu observasi per competency/axis, misalnya `YYYY-MM-DD-s01-e01`.

Berpindah chat dalam satu sesi yang sama tidak otomatis membuat attempt baru. Pertemuan belajar baru memakai session ID baru dan merujuk checkpoint yang dilanjutkan; attempt boleh tetap sama. Melanjutkan attempt pada hari lain bukan dengan sendirinya delayed retest independen. Retest memakai task/attempt yang sesuai dan reference ke evidence asal.

Simpan evidence per axis dengan seluruh field yang diwajibkan map: `session_id`, `date`, `competency_id`, `axis`, `task_variant`, `artifact_or_observation`, `result`, `max_hint`, dan `reasoning_check`. Untuk keterlacakan, gunakan juga `evidence_id`, `attempt_id`, `assessment_status`, dan, bila relevan, `prompt_context` serta `retest_of`.

`result` berisi apa yang benar-benar diamati; `reasoning_check` mencatat pertanyaan/prediksi/eksperimen dan respons aktual. Reference artefak menggunakan path relatif repository dan bagian yang jelas. Untuk kode atau output yang dapat berubah, simpan snapshot relevan atau referensi commit yang benar-benar ada. Hindari menggandakan seluruh repository untuk setiap observasi.

Untuk record baru, `reasoning_check` memakai struktur dari evaluation rubric: `check_type`, `prompt`, `learner_response`, `observation_reference`, `interpretation`, dan `limitations`; gunakan null bila pemeriksaan tidak dilakukan dan batasi klaim sesuai observasi. Jika kelak ada evidence historis dengan bentuk teks, jangan mengarang detail untuk migrasi; pertahankan observasinya dan catat keterbatasan. Metadata ini memperjelas evidence, tidak menambah axis atau skor baru.

Simpan `learner_feedback` dan `calibration_decision` sesuai template adaptive-learning di notes/checkpoint, lalu ringkas dalam history. Jangan menjadikannya field skor competency. Keterangan perasaan berasal dari learner, sedangkan interpretasi/tindakan instructor diberi label terpisah. Field yang tidak diketahui tetap null; tidak perlu mengisi template saat tidak ada observasi/keputusan yang relevan.

Satu observasi dapat relevan bagi beberapa axis, tetapi tiap atribusi harus beralasan dan menunjuk sumber yang sama; jangan menghitungnya sebagai beberapa task independen. Simpan outcome yang blocked/not_observed tanpa perubahan skor dan tanpa menciptakan evidence mastery.

## 10. Menilai dan menyimpan perkembangan

### 10.1 Keputusan assessment

Untuk tiap axis yang relevan, bandingkan observasi dengan outcome, bantuan, dan rubric map:

- Hanya `assessed` yang dapat memperbarui skor; tidak harus selalu mengubahnya.
- `not_observed`/`blocked` mempertahankan nilai sebelumnya, termasuk `null`.
- Skor 0 memerlukan evidence valid atas kemampuan dasar yang belum dapat didemonstrasikan; bukan konsekuensi otomatis setup gagal, test merah, atau waktu habis.
- Terapkan aturan confidence/proficiency map, bukan rata-rata nilai attempt atau skor maksimum historis.
- Jangan membuat agregat ketika ada axis null, atau memakai agregat untuk melewati syarat proficiency.
- Catat nilai sebelum/sesudah, evidence pendukung, dan alasan perubahan. Bila bukti bertentangan, jelaskan keterbatasannya dan lakukan probe terarah bila diperlukan.

Contoh keputusan, bukan hasil assessment learner: learner berhasil membuat reproduksi dan eksperimen pembeda sendiri, lalu meminta pseudocode untuk perbaikan. Evidence debugging sebelum bantuan dapat dinilai sesuai kualitasnya; implementation sesudah pseudocode dicatat terbantu H5. Axis transfer yang tidak diuji tetap pada nilai sebelumnya. Tidak ada skor numerik otomatis hanya dari ringkasan contoh ini.

### 10.2 Urutan penyimpanan

Simpan checkpoint setelah eksperimen bermakna, sebelum demonstrasi solusi, serta ketika sesi berhenti atau selesai. Tidak perlu merekam setiap keystroke.

1. Simpan artefak dan checkpoint notes lebih dahulu. Cantumkan evidence baru dan rencana perubahan state, sehingga penyimpanan dapat dipulihkan jika terputus.
2. Susun kandidat perubahan `learner/competency-state.yaml`, lalu periksa parse YAML dan nilai yang berubah sebelum mengganti file aktif. Terapkan evidence tersebut pada skor yang teramati, confidence/proficiency sesuai map, evidence records, dan rencana review. Pertahankan axis dan competency lain; gunakan penggantian file yang aman ketika tersedia agar write terputus tidak merusak state lama.
3. Append entri `learner/session-history.md` dengan session/checkpoint ID, status sesi, ringkasan hasil, bantuan, evidence IDs, perubahan state, serta next step. Sertakan ringkasan feedback dan keputusan kalibrasi yang bermakna beserta reference ke notes. Jangan menimpa entri lama.
4. Perbarui `learner/mistake-patterns.md` hanya jika ada pengulangan yang didukung beberapa observasi. Catat reference dan intervensi; satu kesalahan cukup masuk history.
5. Validasi konsistensi, lalu append penanda checkpoint selesai disimpan pada notes. Laporan kepada learner harus menyebutkan bila tahap penyimpanan belum lengkap.

Penyimpanan beberapa file bukan satu transaksi atomik. Jika terputus, baca checkpoint dan bandingkan setiap evidence ID serta update yang telah diterapkan sebelum melanjutkan. Terapkan hanya bagian yang belum ada; jangan append evidence duplikat atau mengubah skor dua kali untuk observasi yang sama. Jika ada perubahan lain sejak checkpoint, rekonsiliasi dengan evidence terkini tanpa menimpa pekerjaan baru.

Commit Git dapat menjadi snapshot bila workflow repository menggunakannya. File tersimpan tidak otomatis berarti sudah di-commit atau di-push; laporkan masing-masing hanya jika benar dilakukan. Koreksi catatan historis dilakukan melalui entri koreksi dengan reference ke entri asal.

### 10.3 Pemeriksaan sebelum menyatakan progres tersimpan

- YAML yang diubah dapat diparse dan sesuai struktur state yang disepakati.
- Competency IDs dan axis tersedia di map; skor hanya null atau integer 0–4.
- Evidence/checkpoint IDs tidak duplikat dan references artefak/observasi dapat ditelusuri.
- Skor yang berubah mempunyai evidence serta alasan; axis tanpa observasi tidak berubah.
- Jenis pemeriksaan reasoning sesuai rubric; kesimpulan dibatasi oleh bantuan/exposure. Feedback dan perubahan kesulitan tidak dijadikan alasan tunggal mengubah skor.
- State dan history menunjuk checkpoint yang sama dan tidak saling bertentangan.
- Tanggal review dan waktu observasi jelas dalam Asia/Jakarta; tidak ada hasil sintetis yang dianggap nyata.

Jika penyimpanan gagal, sebutkan file/tahap yang belum tersimpan dan berikan checkpoint yang dapat dipulihkan. Jika file lokal tidak dapat ditulis, berikan ringkasan untuk disimpan learner; jangan menyatakan repository telah diperbarui.

## 11. Retrieval dan evaluasi rencana

Gunakan interval map secara adaptif bersama ketersediaan learner: Sabtu–Minggu, 60–120 menit per sesi. Simpan tanggal keberhasilan/retest asal, tanggal review yang dituju, tanggal pelaksanaan aktual, axis/task yang perlu diuji, dan alasan penyesuaian jadwal dalam state sesuai schema yang dipakai.

Review satu hari setelah belajar dicatat sebagai interval satu hari, bukan D2. Jika jadwal tidak memungkinkan D2, pilih sesi tersedia dan catat penyesuaiannya; jangan menyisipkan kewajiban weekday. Simpan retest tertunda pada akhir pekan berikutnya atau interval lebih panjang sesuai evidence.

Review menjadi due ketika tanggal rencananya tercapai dan review belum dilakukan. Review yang terlambat tidak menghapus proficiency. Jika antrean review melebihi kapasitas sesi, dahulukan yang paling relevan/rapuh dan catat penundaan sisanya. Jangan mereset semua jadwal hanya karena satu axis mendapat latihan singkat.

Setelah empat sesi belajar yang benar-benar dijalankan, tinjau scope, bantuan, kualitas evidence, dan kecocokan durasi sesuai goals. Ini checkpoint perencanaan, bukan deadline mastery. Penambahan waktu atau sesi mengikuti kapasitas yang dinyatakan learner. Rencana review dalam file tidak menciptakan reminder atau automation eksternal.

## 12. Laporan akhir dan panduan singkat learner

Laporan akhir cukup menjawab: apa diuji, evidence yang diamati, kemampuan independen vs terbantu, apa yang belum diketahui, perubahan skor dan alasannya, status sesi/penyimpanan, next review, serta tindakan berikutnya. Bila skor tidak berubah atau pattern belum terbukti, katakan demikian. Jangan memaksa ada kelemahan atau promosi di setiap sesi.

Jika ada penyesuaian tantangan, jelaskan tindakan, alasan, dan observasi yang akan diperiksa berikutnya. Tidak ada kewajiban membuat diagnosis emosional atau perubahan tingkat kesulitan di setiap sesi.

| Saat ingin… | Learner dapat mengatakan… | Instructor melakukan… |
| --- | --- | --- |
| Mulai | “Mulai sesi hari ini, saya punya 60 menit.” | Membaca state, memilih target, dan memberikan langkah pertama. |
| Melanjutkan | “Lanjutkan latihan terakhir.” | Memulihkan checkpoint dan mengecek kondisi terkini. |
| Meminta hint | “Beri satu hint dulu.” | Memberi bantuan bertahap dan mencatat axis terdampak. |
| Meminta fondasi | “Jelaskan konsepnya dulu.” | Beralih ke guided learning dan menyiapkan kesempatan mencoba. |
| Melihat solusi | “Tunjukkan solusi lengkap.” | Mendemonstrasikan tanpa menganggap hasilnya implementasi independen. |
| Berhenti | “Berhenti dulu, simpan progres saya.” | Membuat checkpoint dan menutup sesi dengan status yang tepat. |
| Membatasi waktu | “Waktu saya tinggal 10 menit.” | Memperkecil scope dan menyediakan waktu menyimpan perkembangan. |

Tidak ada keharusan memakai frasa persis di atas. Keberhasilan workflow awal adalah satu siklus belajar yang dapat ditelusuri dan dilanjutkan, bukan banyaknya file atau exercise yang selesai.
