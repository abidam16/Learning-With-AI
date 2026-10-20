# Learner Profile — Abid

Status: profil awal berdasarkan konteks; pengalaman Go dan pilihan environment dikonfirmasi learner pada 2026-10-06. Kesiapan tooling belum diverifikasi.
Tanggal penyusunan: 2026-10-06.

Dokumen ini memuat latar belakang, pengalaman, preferensi interaksi, dan konteks environment. Pengalaman yang disebutkan bukan hasil assessment dan tidak memberikan skor mastery. Perbarui ketika informasi learner berubah atau bagian yang belum diketahui telah dikonfirmasi.

## 1. Latar belakang

- Nama panggilan: Abid.
- Peran: backend engineer di PT Jaminan Kredit Indonesia (Jamkrindo).
- Pengalaman: sekitar dua tahun, berdasarkan dokumen konteks awal; bukan angka yang diperbarui otomatis.
- Konteks pekerjaan: pengembangan dan pemeliharaan backend, integrasi sistem, pemrosesan asynchronous, serta troubleshooting.

## 2. Teknologi yang pernah digunakan

- Bahasa dan framework: Kotlin/Spring Boot dan Java.
- Akses data: JDBC dan JPA.
- Database: SQL Server.
- Messaging: Kafka dan RabbitMQ.
- Runtime/infrastructure: Docker dan OpenShift.

Daftar ini menunjukkan exposure dalam pekerjaan. Kedalaman pemahaman dan kemampuan independen pada setiap teknologi belum ditentukan oleh daftar ini.

## 3. Pengalaman yang relevan untuk konteks latihan

- Menangani Kafka consumer dengan manual acknowledgement, commit/rebalance, pemrosesan lama, dan deserialization error.
- Mengoptimalkan batch job JDBC serta menghadapi locking dan timeout database.
- Memindahkan pekerjaan PDF/Excel ke messaging.
- Menggunakan centralized logs dan lingkungan OpenShift.

Pengalaman ini dapat menjadi konteks skenario latihan. Kemiripan dengan pengalaman sebelumnya perlu diperhatikan saat menilai transfer ke masalah baru. Gunakan fixture sintetis untuk merepresentasikan kasus kerja.

## 4. Bahasa dan pendekatan belajar

- Bahasa diskusi: Bahasa Indonesia; pertahankan istilah teknis yang membantu ketepatan makna.
- Pendekatan yang diinginkan: praktik langsung dalam repository, eksperimen, reasoning, dan feedback berbasis evidence.
- Orientasi: memahami mekanisme di balik framework; tutorial CRUD dasar bukan prioritas otomatis.
- Go telah dipilih untuk sejumlah micro-lab agar mekanisme lebih mudah diamati.
- Pengalaman Go sebelum lab: pernah belajar sintaks, berdasarkan pernyataan learner pada 2026-10-06. Kemampuan menulis program mandiri, debugging, dan penggunaan tooling Go belum diuji.
- Konteks transfer yang relevan: Kotlin/Java/Spring dan sistem backend nyata.

Pilihan pendekatan di atas merupakan preferensi dan rancangan awal, bukan bukti bahwa satu metode belajar sudah terbukti paling efektif. Instructor mengikuti kebijakan interaksi dan hint di `AGENTS.md` serta competency map.

Untuk Go, mulai dengan probe singkat membaca, menjalankan, dan mengubah program kecil. Berikan penyegaran sintaks atau scaffold sesuai kebutuhan; jangan otomatis mengulang seluruh tutorial bahasa atau menganggap sintaks sudah dikuasai. Pisahkan bantuan sintaks dari bantuan yang menyelesaikan mekanisme target.

## 5. Environment Learning Lab

Pilihan learner untuk repository ini, dikonfirmasi pada 2026-10-06:

- Environment eksekusi: Windows native.
- Editor: Visual Studio Code (VS Code).
- Cara mengakses Codex: melalui ChatGPT desktop.

Belum diverifikasi:

- Shell yang digunakan dan akses sesi Codex ke folder repository lokal.
- Runtime dan tooling yang sudah tersedia, termasuk Go, Git, dan Docker bila diperlukan.
- Constraint perangkat yang relevan untuk menjalankan lab, seperti RAM atau keterbatasan instalasi.

Instructor menyiapkan latihan awal yang kompatibel dengan Windows native dan shell aktual; jangan mengasumsikan tersedianya Bash, perintah Linux, atau WSL. Untuk lab yang menguji perilaku khusus Linux, jelaskan kebutuhan environment tambahan ketika relevan dan bedakan semantik OS yang diuji. Jangan mengubah pilihan environment learner secara diam-diam.

Pilihan environment tidak membuktikan tooling sudah terpasang atau sesi Codex sudah terhubung ke repository. Detail environment yang sudah diverifikasi dapat dicatat di README atau dokumentasi setup; profil cukup menyimpan ringkasannya.

## 6. Batas tanggung jawab dokumen

- Target, prioritas, alokasi waktu, dan batas lingkup belajar: `learner/goals.md`.
- Skor, confidence, proficiency, evidence, dan review: `learner/competency-state.yaml`.
- Hasil attempt, hipotesis, serta checkpoint sesi: `learner/session-history.md` dan artefak lab.
- Pola kesalahan yang didukung observasi berulang: `learner/mistake-patterns.md`.
- Aturan instructor dan workflow: `AGENTS.md` dan `docs/learning-system.md`.

Jangan menyimpulkan kekuatan, kelemahan, atau pola kesalahan hanya dari profil ini. Gunakan assessment untuk menguji capability; jangan mengubah pengalaman kerja menjadi baseline score.
