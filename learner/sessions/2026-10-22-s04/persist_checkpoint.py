"""Persist requested pause without adding assessment evidence."""
from pathlib import Path
import sys
sys.path.insert(0, r"C:/Users/abid.mahdy/AppData/Local/Temp/learning-lab-yaml-validation")
import yaml

root = Path(__file__).resolve().parents[3]
sid = "2026-10-22-s04"
cpid = sid + "-cp01"
ref = f"learner/sessions/{sid}/checkpoint.md"
notes_ref = "labs/diag-004/attempts/a001/notes.md"
state_path = root / "learner/competency-state.yaml"
original = state_path.read_text(encoding="utf-8")
before = yaml.safe_load(original)
curriculum = yaml.safe_load((root / "curriculum/competency-map.yaml").read_text(encoding="utf-8"))
lab = yaml.safe_load((root / "labs/diag-004/lab.yaml").read_text(encoding="utf-8"))
assert set(before["competencies"]) == set(curriculum["competencies"])
assert all(cid in curriculum["competencies"] for cid in lab["primary_competency_ids"])

body = """Status **paused**, atas permintaan eksplisit learner: "Pause sesi ini dulu". Penutupan mulai 2026-10-22T15:28:17+07:00; startup pertama bertimestamp 15:26:17. Rentang sekitar dua menit mencakup persiapan/interaksi, bukan pengukuran kerja aktif. Anggaran awal 45 menit tidak habis.

Melanjutkan diag-004 / batch-two-stops-windows-v1 / a001 dari s03-cp01. Prompt pemilik/sumber worker_exit_code dan $LASTEXITCODE setelah .\\lab.exe B sudah diberikan. Belum ada respons reasoning, hipotesis baru, eksperimen, inspeksi laporan, atau patch learner dalam sesi ini. Pertanyaan hipotetis perubahan return menjadi 7 belum diberikan. Tidak menganggap pause sebagai kegagalan.

Seluruh skor/evidence/assessment/review tetap: os.processes concept 2, implementation 3, debugging/judgment/transfer null; confidence low, proficiency learning. Tidak ada bukti baru untuk mengubah penilaian atau menetapkan misconception/pattern baru. Gap dari s03 tentang asal status belum diperiksa ulang. Tidak ada klaim kemampuan mandiri baru.

Bantuan: prompt menunjuk main.go (H3 concept untuk lokasi); maksimum bantuan historis attempt tetap concept H4/debugging H4. Tidak ada penjelasan solusi atau bantuan implementation baru. Dukungan environment: go1.26.0 windows/amd64 berhasil diperiksa, lab.exe ada, hash source sama dengan snapshot; tidak menjalankan ulang fixture. Laporan terdahulu tetap baseline instructor.

learner_feedback: permintaan pause eksplisit; alasan/emosi tidak disebutkan. calibration_decision: pause, difficulty tetap 1, tidak ada perubahan tingkat atau scope tambahan berdasarkan kemampuan. Next check tetap pemisahan pemilik/sumber status. Blocker environment tidak ditemukan pada startup.

Next step: buka labs/diag-004/main.go tanpa menjalankan atau mengubah kode. Jawab proses pemilik dan baris sumber untuk (1) worker_exit_code dalam laporan, (2) $LASTEXITCODE setelah .\\lab.exe B. Tunggu jawaban sebelum memberi prediksi hipotetis hanya return runner berubah 7 sementara TerminateProcess tetap 2. Jika sumber status jelas, lanjutkan prediksi dan inspeksi runtime A sesuai waktu sesi berikut. Ini lanjutan terbimbing dari attempt sama, bukan delayed retest.

Review concept/implementation tetap 24 Oktober 2026. Notes: labs/diag-004/attempts/a001/notes.md. Tidak ada commit/push atau automation.
"""
checkpoint = root / ref
if not checkpoint.exists():
    checkpoint.write_text(f"# Checkpoint {cpid}\n\n" + body, encoding="utf-8")
for filename, heading in ((notes_ref, f"## Checkpoint {cpid} — paused"),
                          ("learner/session-history.md", f"### {cpid}")):
    path = root / filename
    text = path.read_text(encoding="utf-8")
    if heading not in text:
        with path.open("a", encoding="utf-8") as stream:
            stream.write("\n\n" + heading + "\n\n" + body + f"\nCheckpoint pusat: {ref}\n")

prefix, suffix = original.split("\ncompetencies:\n", 1)
prefix = prefix.replace("2026-10-22-s03", sid)
candidate = prefix + "\ncompetencies:\n" + suffix
after = yaml.safe_load(candidate)
assert before["competencies"] == after["competencies"]
assert after["last_session_id"] == sid
assert after["last_applied_checkpoint"] == cpid
assert after["active_work"]["checkpoint_reference"] == ref
assert checkpoint.is_file()
state_path.write_text(candidate, encoding="utf-8")
saved = yaml.safe_load(state_path.read_text(encoding="utf-8"))
assert saved == after
for filename, heading in ((notes_ref, f"## Checkpoint {cpid} — paused"),
                          ("learner/session-history.md", f"### {cpid}")):
    assert (root / filename).read_text(encoding="utf-8").count(heading) == 1
assert (root / "labs/diag-004/main.go").read_bytes() == (root / "labs/diag-004/attempts/a001/artifacts/starter-main.go.txt").read_bytes()
validation = "\nValidasi akhir PASS: YAML map/lab/state terparse; competency IDs valid; referensi checkpoint/notes resolve; state/history/checkpoint konsisten; entri pause unik. Seluruh competencies termasuk skor, evidence, assessment history dan review identik sebelum/sesudah. Source tetap identik snapshot.\n"
if "Validasi akhir PASS" not in checkpoint.read_text(encoding="utf-8"):
    with checkpoint.open("a", encoding="utf-8") as stream:
        stream.write(validation)
print("PASS: requested pause saved; assessment and review unchanged; checkpoint " + ref)
