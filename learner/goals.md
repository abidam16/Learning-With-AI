# Learning Goals — Software Engineering Learning Lab

Tanggal: 2026-10-06.
Status: fokus dan ketersediaan waktu dikonfirmasi learner; urutan target dan pola sesi di bawah adalah rancangan operasional awal yang akan disesuaikan berdasarkan diagnostic.

## 1. Tujuan utama

Membangun fundamental software engineering dan kemampuan penalaran engineering yang kuat, sehingga learner mampu memahami, mengimplementasikan, mendiagnosis, dan mengevaluasi sistem secara independen.

Kemampuan menerapkan fundamental pada masalah kerja merupakan hasil transfer yang diharapkan. Tetap latih transfer secara eksplisit: pemahaman konsep tidak otomatis membuktikan penguasaan perilaku framework, database engine, atau sistem tertentu.

## 2. Prioritas dan lingkup

Prioritas utama adalah pemahaman mekanisme dan penalaran sebab-akibat. Gunakan pekerjaan sehari-hari sebagai konteks atau variasi transfer ketika membantu tujuan ini. Insiden pekerjaan tidak otomatis mengganti arah kurikulum; perubahan fokus mengikuti pilihan learner.

Arah belajar awal, fleksibel terhadap prerequisite dan hasil diagnostic:

1. Execution dan resource: process/thread, memory, file/resource lifetime.
2. Concurrency dan komunikasi: shared state, invariant, synchronization, cancellation, socket/TCP/DNS/HTTP.
3. Data: relational integrity, query execution, transaction, isolation, locking.
4. Sistem terdistribusi: messaging, failure semantics, idempotency, retry, consistency, recovery.
5. Runtime/infrastructure sebagai penerapan mekanisme yang telah dipelajari.

Debugging, observasi, pengujian, dan trade-off dilatih sepanjang urutan tersebut. Ini bukan urutan wajib atau tuntutan menguasai seluruh tahap sebelum mencoba tahap berikutnya. Gunakan ID dan prerequisite dari `curriculum/competency-map.yaml`; goals tidak membuat graph atau skala penilaian baru.

Go digunakan sebagai alat untuk melihat mekanisme pada micro-lab. Lakukan penyegaran sintaks seperlunya. Kedalaman fundamental, bukan banyaknya fitur bahasa atau framework yang dipelajari, menjadi dasar pemilihan latihan.

## 3. Capability yang ingin dibuktikan

| Axis | Perilaku yang dituju | Contoh evidence |
| --- | --- | --- |
| Concept | Menjelaskan mekanisme dan memprediksi perilaku sebelum eksperimen. | Prediksi disertai alasan, lalu penjelasan ketika hasil berbeda. |
| Implementation | Mengubah invariant dan constraint menjadi implementasi yang benar. | Kode learner beserta pengujian jalur normal, batas, atau gagal yang relevan. |
| Debugging | Memecah masalah, menyusun hipotesis yang dapat dibantah, dan memilih eksperimen pembeda. | Rangkaian hipotesis, observasi, dan penentuan root cause. |
| Judgment | Membandingkan solusi berdasarkan correctness, resource, kompleksitas, dan failure mode. | Keputusan dengan alasan serta kondisi yang dapat mengubah keputusan tersebut. |
| Transfer | Menggunakan mekanisme yang sama pada kasus, constraint, atau stack yang berbeda. | Penyelesaian varian baru dengan penjelasan bagian yang berlaku dan yang perlu diuji ulang. |

Target kemandirian pada kompetensi aktif mengacu pada skor 3 per axis yang relevan menurut map. Ini adalah target, bukan baseline atau janji capaian pada tanggal tertentu. Proficiency dan mastery tetap mengikuti seluruh syarat map, termasuk variasi evidence dan retest tertunda. Tidak perlu menilai semua axis dalam satu sesi.

## 4. Ketersediaan waktu yang dikonfirmasi

- Jadwal awal: dua sesi per minggu, pada Sabtu dan Minggu.
- Durasi awal: sekitar 60–120 menit per sesi; total sekitar 2–4 jam per minggu.
- Timezone: Asia/Jakarta.
- Jam mulai: belum ditentukan; gunakan waktu aktual saat learner memulai sesi.
- Durasi dan frekuensi boleh bertambah ketika learner sudah terbiasa dan menyatakan kapasitas tambahan.
- Sesi weekday bukan kewajiban dalam rencana awal. Sesi yang terlewat tidak otomatis diganti dengan beban ganda.

Jadwal ini adalah ketersediaan belajar, bukan permintaan untuk membuat reminder atau automation.

## 5. Rancangan penggunaan sesi

Contoh pembagian sesi 60 menit, disesuaikan dengan kebutuhan aktual:

| Kegiatan | Menit |
| --- | ---: |
| Retrieval atau melanjutkan checkpoint | 10 |
| Penetapan scope, prediksi, dan success criteria | 5 |
| Attempt dan eksperimen learner | 30 |
| Feedback dan verifikasi reasoning | 10 |
| Pencatatan evidence dan langkah berikutnya | 5 |

Untuk sesi 90–120 menit, gunakan tambahan waktu untuk eksperimen, perbaikan mandiri, atau satu variasi transfer yang relevan. Sesuaikan waktu belajar konsep baru bila diperlukan. Waktu setup dicatat terpisah dan dapat mengurangi scope latihan, tanpa dianggap kegagalan kemampuan learner.

Sabtu dapat digunakan untuk eksplorasi mekanisme; Minggu untuk melanjutkan attempt atau variasi terkait. Keduanya boleh dipakai melanjutkan satu masalah bila itu paling bernilai. Pola ini tidak mewajibkan topik baru setiap sesi.

## 6. Retrieval sesuai jadwal akhir pekan

Interval D2/D7/D21/D60 dalam map adalah default adaptif. Jadwalkan review pada sesi tersedia dengan mempertimbangkan pentingnya kompetensi dan kualitas evidence; jangan menjadikan weekday sebagai kewajiban tersembunyi.

Catat tanggal dan interval aktual. Review pada Minggu setelah belajar Sabtu adalah D1, bukan D2. Tambahkan retest pada akhir pekan berikutnya atau interval lebih panjang untuk mengamati retensi tertunda. Review yang belum sempat dilakukan tetap berstatus due; keterlambatan kalender sendiri tidak menurunkan proficiency.

## 7. Milestone awal dan evaluasi rencana

Sebelum menentukan target capaian bertanggal, kumpulkan baseline melalui beberapa probe kecil. Pilih satu target aktif berdasarkan evidence dan prerequisite; kompetensi lain boleh muncul sebagai pendukung.

Milestone awal yang dapat diperiksa:

- Environment dapat menjalankan lab kecil dan menyimpan hasil kerja.
- Initial diagnostic menghasilkan evidence yang diatribusikan ke axis yang teramati; axis lain tetap belum dinilai.
- Satu siklus attempt, feedback, dan pencatatan selesai dengan pekerjaan learner yang dapat ditelusuri.
- Varian baru dan retest tertunda mulai memperlihatkan apakah pemahaman dapat diterapkan serta dipertahankan.

Usulan checkpoint perencanaan: setelah empat sesi belajar yang benar-benar dijalankan, evaluasi kecocokan scope, durasi, bantuan, dan kualitas evidence. Ini bukan deadline mastery. Pertimbangkan penambahan durasi atau frekuensi jika learner menginginkannya; ubah satu aspek jadwal terlebih dahulu agar dampaknya mudah diamati.

## 8. Ukuran kemajuan dan pemeliharaan

Nilai kemajuan dari penjelasan yang semakin tepat, eksperimen yang semakin terarah, implementasi yang menjaga invariant, berkurangnya bantuan pada task dengan kesulitan sebanding, dan keberhasilan transfer/retrieval. Jumlah lab, jam belajar, test hijau, atau baris kode bukan ukuran tunggal capability.

Skor dan evidence aktual berada di `learner/competency-state.yaml`; hasil sesi berada di `learner/session-history.md`. Dokumen ini hanya menyimpan tujuan dan constraint. Perubahan arah, kapasitas waktu, atau target dicatat beserta tanggal dan alasannya setelah ada masukan learner atau hasil evaluasi yang relevan.
