# Software Engineering Learning Lab

Repository belajar untuk membangun fundamental software engineering dan penalaran engineering yang mandiri: memahami mekanisme, membuat implementasi, menyelidiki kegagalan, menimbang trade-off, dan menerapkan pemahaman pada situasi baru.

Go digunakan untuk micro-lab yang memperlihatkan mekanisme secara langsung. Pengalaman awal learner: pernah belajar sintaks Go. Kebutuhan penyegaran bahasa dan kemampuan saat ini akan diperiksa melalui latihan. Masalah pekerjaan dapat menjadi konteks transfer sesuai relevansinya dengan tujuan belajar.

## Daftar isi

- [Status awal](#status-awal)
- [Peta dokumen](#peta-dokumen)
- [Menyiapkan repository di Windows](#menyiapkan-repository-di-windows)
- [Memulai dan melanjutkan sesi](#memulai-dan-melanjutkan-sesi)
- [Alur sesi 60–120 menit](#alur-sesi-60120-menit)
- [Pemahaman, bantuan, dan tingkat kesulitan](#pemahaman-bantuan-dan-tingkat-kesulitan)
- [Menyimpan perkembangan](#menyimpan-perkembangan)
- [Jika ada kendala](#jika-ada-kendala)

## Status awal

Baseline paket dokumen pada **6 Oktober 2026**:

| Bagian | Status |
| --- | --- |
| Instruksi instructor dan prosedur belajar | Tersedia pada dokumen di bawah. |
| Curriculum | Competency map versi `1.1.0`, berisi 38 kompetensi dan lima axis penilaian. |
| Learner state | Schema versi `1`; seluruh skor awal `null`, confidence `none`, proficiency `unseen`, dan evidence kosong. |
| Riwayat sesi dan pola kesalahan | Template tersedia; belum berisi hasil belajar aktual. |
| Repository lokal, Git, dan akses instructor | Belum diverifikasi. |
| Environment Windows dan lab runnable | Belum diverifikasi; lab pertama belum dibuat. |
| Initial diagnostic | Belum dilakukan. |

Tabel ini merekam keadaan saat persiapan. Setelah sesi berjalan, gunakan learner state dan history untuk melihat perkembangan terkini; jangan menginisialisasi ulang state yang sudah memiliki evidence.

## Peta dokumen

Tempatkan file pada path berikut, relatif terhadap root repository. Tautan akan bekerja setelah file disusun sesuai struktur ini.

| File | Fungsi |
| --- | --- |
| `README.md` | Panduan masuk, setup awal, dan penggunaan sehari-hari. |
| [AGENTS.md](AGENTS.md) | Tanggung jawab dan batas bantuan instructor. |
| [curriculum/competency-map.yaml](curriculum/competency-map.yaml) | Sumber aturan competency ID, prerequisite, hint, scoring, confidence, proficiency, dan prioritas belajar. |
| [learner/profile.md](learner/profile.md) | Pengalaman, preferensi, dan kondisi environment learner. |
| [learner/goals.md](learner/goals.md) | Fokus fundamental, target kemampuan, dan kapasitas waktu. |
| [learner/competency-state.yaml](learner/competency-state.yaml) | Penilaian terkini, evidence, pekerjaan aktif, dan rencana review. |
| [learner/session-history.md](learner/session-history.md) | Riwayat sesi dan checkpoint yang ditambahkan secara berurutan. |
| [learner/mistake-patterns.md](learner/mistake-patterns.md) | Pola kesalahan berulang yang didukung beberapa observasi. |
| [docs/learning-system.md](docs/learning-system.md) | Prosedur lengkap untuk memulai, berlatih, meminta bantuan, berhenti, dan menyimpan progres. |
| [docs/evaluation-rubric.md](docs/evaluation-rubric.md) | Cara memeriksa pemahaman mekanisme dan menafsirkan evidence. |
| [docs/adaptive-learning.md](docs/adaptive-learning.md) | Cara memilih serta menyesuaikan tingkat kesulitan. |

Folder `labs/` dibuat saat latihan pertama disiapkan. Setiap lab akan memiliki metadata `labs/<lab-id>/lab.yaml`, instruksi menjalankan latihan, area kerja learner, serta tempat menyimpan observasi/artefak. Contoh diagnostic di competency map belum merupakan lab runnable.

Learner dapat mulai dari README, profile, dan goals. Instructor membaca dokumen yang relevan sebelum memilih tugas. Aturan penilaian terperinci tetap mengacu ke competency map; README tidak menetapkan skala tambahan.

## Menyiapkan repository di Windows

1. Buat satu folder project, misalnya `software-engineering-learning-lab`, lalu buka folder tersebut di VS Code. Susun dokumen mengikuti tabel di atas. Pastikan memakai competency map **`1.1.0`**, bukan attachment versi sebelumnya.
2. Buka terminal **PowerShell** di root project. Periksa lokasi dan ketersediaan tooling:

   ```powershell
   Get-Location
   git --version
   go version
   ```

   Pastikan lokasi yang tampil adalah folder project. Jika command tidak tersedia, selesaikan pemasangan atau konfigurasi PATH tool tersebut, buka terminal baru, lalu ulangi pemeriksaan. Catat versi dan hasil aktual ketika sudah diperiksa.

3. Jika folder ini benar-benar project baru dan tidak berada di dalam repository lain, inisialisasi Git:

   ```powershell
   git init
   git status
   ```

   Jika repository sudah ada, cukup periksa statusnya. Remote GitHub belum diperlukan untuk menjalankan sesi lokal. Siapkan `.gitignore` sesuai artefak lab sebelum commit pertama; file itu belum termasuk paket awal ini.

4. Gunakan sesi Codex melalui ChatGPT desktop yang benar-benar memiliki akses ke folder tersebut. Minta instructor membaca `AGENTS.md` dan menyebutkan lokasi repository yang dibaca. Akses ke aplikasi desktop saja belum memastikan akses ke file lokal atau kemampuan menjalankan command.
5. Minta instructor menyiapkan lab Go pertama beserta scaffold, fixture, instruksi PowerShell, dan pemeriksaan environment. Instructor memverifikasi program/test kecil dapat dijalankan serta membedakan kegagalan yang disengaja dari setup yang rusak. Learner mengerjakan reasoning dan implementasi inti latihan.

Jalankan command latihan dari direktori yang disebutkan pada instruksi lab. Belum ada `go.mod` atau command test untuk root repository pada tahap ini. Dukungan Docker atau service lain disiapkan ketika latihan membutuhkannya.

Setup siap ketika file dapat dibaca dan disimpan, lab pertama dapat dijalankan, dan hasil pemeriksaannya tercatat. Waktu setup dipisahkan dari waktu latihan.

## Memulai dan melanjutkan sesi

Untuk bootstrap pertama, sampaikan:

> Periksa kesiapan repository dan environment Windows saya. Baca AGENTS.md serta dokumen terkait, lalu siapkan initial diagnostic kecil berdasarkan state awal. Saya punya 90 menit. Jelaskan langkah pertama dan biarkan saya mengerjakan reasoning serta implementasi inti.

Untuk penggunaan berikutnya:

| Kebutuhan | Contoh pesan |
| --- | --- |
| Mulai sesi | “Mulai sesi hari ini, saya punya 60 menit.” |
| Melanjutkan pekerjaan | “Lanjutkan latihan terakhir dari checkpoint.” |
| Meminta petunjuk | “Beri satu hint dulu.” |
| Memerlukan fondasi | “Jelaskan konsepnya dulu, lalu beri kesempatan saya mencoba.” |
| Mengurangi scope | “Waktu saya tinggal 10 menit.” |
| Berhenti | “Berhenti dulu, simpan progres dan langkah berikutnya.” |

Instructor membaca state, history/checkpoint, dan target yang relevan sebelum memilih tugas. Initial diagnostic mengambil sampel kecil; tidak perlu menguji seluruh kompetensi sekaligus. Nyatakan mode latihan, success criteria, timebox, serta satu atau dua axis utama.

## Alur sesi 60–120 menit

Jadwal awal: **Sabtu dan Minggu**, masing-masing **60–120 menit**, dengan timezone **Asia/Jakarta**. Berikut rancangan alokasi waktu yang dapat disesuaikan:

| Kegiatan | 60 menit | 90 menit | 120 menit |
| --- | ---: | ---: | ---: |
| Retrieval atau pemulihan checkpoint | 10 | 10 | 10 |
| Scope, prediksi, dan success criteria | 5 | 5 | 5 |
| Attempt dan eksperimen learner | 30 | 50 | 70 |
| Jeda | 0 | 5 | 10 |
| Verifikasi pemahaman dan feedback | 10 | 15 | 15 |
| Menyimpan progres dan next step | 5 | 5 | 10 |

Pada sesi pertama, bagian retrieval digunakan untuk orientasi dan pemeriksaan baseline. Jika setup mengambil waktu atau konsep baru perlu dijelaskan, kurangi scope latihan sambil menyediakan waktu untuk checkpoint. Satu masalah boleh berlanjut pada beberapa sesi.

Setelah empat sesi belajar yang benar-benar dijalankan, tinjau kecocokan durasi, scope, dan bantuan. Penambahan waktu atau frekuensi mengikuti kapasitas learner. Rencana review dalam file tidak membuat reminder otomatis.

## Pemahaman, bantuan, dan tingkat kesulitan

Lima axis yang diamati adalah `concept`, `implementation`, `debugging`, `judgment`, dan `transfer`. Instructor hanya menilai axis yang memiliki evidence. `null` berarti belum dinilai; skor `0` memerlukan observasi valid atas kemampuan yang diuji.

Test hijau perlu dilengkapi pemeriksaan yang relevan, misalnya prediksi sebelum eksekusi, penjelasan sebab-akibat, eksperimen pembeda, perubahan constraint, atau penerapan pada varian baru. Retest tertunda digunakan untuk memeriksa retensi. Tidak semua pemeriksaan harus dilakukan pada setiap sesi.

Bantuan dicatat per axis yang terdampak. Meminta penjelasan atau solusi diperbolehkan; kemampuan independen pada bagian yang terbantu perlu diperiksa kembali melalui varian yang sesuai. Instructor menjaga pekerjaan learner dan tidak diam-diam menyelesaikan target latihan.

Kesulitan disesuaikan dari kualitas reasoning, bantuan, kemajuan, familiaritas tugas, kendala tooling, dan feedback learner. Sampaikan bila latihan terasa terlalu mudah, membingungkan, atau melelahkan. Instructor menangani blocker segera dan menyesuaikan satu dimensi tantangan pada satu waktu. Rasa bosan atau frustrasi tidak otomatis mengubah skor.

## Menyimpan perkembangan

Instructor mengurus pencatatan administratif berdasarkan pekerjaan dan respons aktual learner:

1. Simpan kode, observasi, dan checkpoint attempt beserta hipotesis serta langkah berikutnya.
2. Perbarui learner state untuk evidence yang valid; pertahankan axis yang belum teramati.
3. Tambahkan riwayat sesi dengan ID, bantuan, status `completed`/`paused`/`blocked`, dan reference evidence.
4. Catat mistake pattern hanya bila pengulangan telah didukung beberapa observasi, lalu periksa konsistensi state dan history.

Prosedur lengkap dan konvensi ID ada di [learning-system.md](docs/learning-system.md). Melanjutkan attempt yang sama tidak menghasilkan evidence independen baru hanya karena berpindah hari atau chat. Koreksi riwayat ditambahkan dengan reference ke catatan asal.

Laporan penutup menyebutkan hasil yang teramati, bagian yang belum diketahui, perubahan penilaian beserta alasan, status penyimpanan, dan next step. File tersimpan, commit Git, dan push remote merupakan tindakan terpisah; masing-masing hanya dilaporkan jika benar dilakukan.

## Jika ada kendala

| Kendala | Tindakan berikutnya |
| --- | --- |
| `go` atau `git` tidak dikenali | Periksa pemasangan/PATH dan ulangi pemeriksaan di terminal baru. |
| Command test gagal karena modul tidak ditemukan | Periksa working directory dan instruksi lab; lab pertama perlu disiapkan sebelum command latihan tersedia. |
| Instructor tidak dapat membaca/menulis folder | Selesaikan akses terlebih dahulu; perubahan di chat belum berarti file lokal diperbarui. |
| Instruksi command tidak cocok dengan Windows | Sesuaikan dengan shell aktual; environment yang direncanakan adalah Windows native. |
| Waktu habis atau setup terhambat | Simpan checkpoint dengan blocker dan next step; jangan mengubahnya menjadi skor rendah tanpa evidence. |
| Sesi/chat terputus | Baca checkpoint terakhir dan cocokkan dengan artefak aktual sebelum melanjutkan; cegah pencatatan evidence ganda. |

**Langkah pertama:** susun dokumen pada folder project, periksa akses dan tooling, lalu siapkan satu lab diagnostic kecil agar siklus belajar pertama dapat dijalankan dan disimpan.
