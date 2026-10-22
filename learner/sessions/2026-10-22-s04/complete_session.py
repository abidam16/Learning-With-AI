"""Persist observed guided learning; preserve the earlier pause checkpoint."""
from pathlib import Path
import copy
import sys
sys.path.insert(0, r"C:/Users/abid.mahdy/AppData/Local/Temp/learning-lab-yaml-validation")
import yaml

root = Path(__file__).resolve().parents[3]
sid, cpid = "2026-10-22-s04", "2026-10-22-s04-cp02"
notes = "labs/diag-004/attempts/a001/notes.md"
checkpoint = f"learner/sessions/{sid}/checkpoint-cp02.md"
path = root / "learner/competency-state.yaml"
original = path.read_text(encoding="utf-8")
before = yaml.safe_load(original)
curriculum = yaml.safe_load((root / "curriculum/competency-map.yaml").read_text(encoding="utf-8"))
assert curriculum["curriculum_version"] == "1.1.0"
assert set(before["competencies"]) == set(curriculum["competencies"])
node = before["competencies"]["os.processes"]

common = dict(session_id=sid, date="2026-10-22", competency_id="os.processes",
    lab_id="diag-004", attempt_id="a001", task_variant="batch-two-stops-windows-v1",
    max_hint="H4", assessment_status="assessed", retest_of=None,
    prompt_context="Same guided attempt after H4 teaching of A bounds panic, B termination and status provenance. Source location prompt H3; instructor clarified ProcessState before prediction. Learner selected A files. All fixture/instrumentation provided; no independent delayed retest.")
concept = dict(common, evidence_id=sid+"-e01", axis="concept",
    artifact_or_observation=f"{notes}, {sid}-o01 and o02",
    result="Learner assigned worker status to the child and TerminateProcess(h,2), shell status to runner and os.Exit(run(...)); then correctly predicted worker 2 / runner 7 when only run's final return changes. Guided application supports concept 2, not independent promotion.",
    reasoning_check=dict(check_type="prediction",
        prompt="Only final return 2 in run becomes return 7; TerminateProcess(h,2) remains and succeeds. Predict worker_exit_code and PowerShell LASTEXITCODE after lab.exe B, with reasons.",
        learner_response="worker_exit_code tetap 2 karena TerminateProcess(h, 2) tetap. LASTEXITCODE 7 karena return berubah dari 2 menjadi 7.",
        observation_reference=notes,
        interpretation="Correct ownership and separate numeric outcomes after teaching; previous provenance gap improves in immediate guided application.",
        limitations=["Hypothetical only; no code edit or execution.", "Immediate H4-assisted follow-up in same attempt; retention and independence untested."]))
debug = dict(common, evidence_id=sid+"-e02", axis="debugging",
    artifact_or_observation=f"{notes}, {sid}-o03/o04; labs/diag-004/attempts/a001/artifacts/A/worker.stderr.log; labs/diag-004/attempts/a001/artifacts/A/supervisor.log",
    result="Learner chose supervisor.log and worker.stderr.log, predicted an index bounds error, inspected baseline output and identified stderr panic as specific causal evidence. Together with earlier guided B termination correlation and startup diagnosis, supports standard-case debugging with guidance (2).",
    reasoning_check=dict(check_type="discriminating_experiment",
        prompt="Choose runtime evidence for A and predict specific observations before inspection; after inspection identify strongest causal evidence and explain.",
        learner_response="Chose supervisor.log and worker.stderr.log; predicted index out of bound. Sent start/Wait PID 49312 status 2 plus runtime panic index out of range [1] with length 1 at main.go:34. Explained stderr shows bounds failure more clearly than supervisor log.",
        observation_reference=notes,
        interpretation="Prediction followed by matching runtime evidence and causal selection completes guided A inspection. B termination evidence is preserved under s03-e02; launch failure under s01-e02. Score reflects combined guided coverage, not treating these observations as independent new variants.",
        limitations=["Baseline instructor logs at 10:45; learner inspected, did not rerun.", "Cause A taught H4 before this session; B log selection previously guided.", "Scope Go bounds panic, controlled Windows termination and tested launch failure; not every crash or OS.", "No instrumentation or implementation by learner."]))
boundary = dict(common, evidence_id=sid+"-e03", axis="concept",
    artifact_or_observation=f"{notes}, {sid}-o05",
    result="Learner said worker has an error but cause is unknown from status alone. Correct insufficient-cause conclusion; instructor refined wording to nonzero termination, since B is externally terminated. No claim learner independently supplied that refinement.",
    reasoning_check=dict(check_type="boundary_case",
        prompt="If detailed A/B logs disappear and only worker_exit_code=2 remains, what can and cannot be established about worker, based on both cases?",
        learner_response="Yang bisa dipastikan adalah ada error pada worker tetapi penyebabnya apa tidak bisa diketahui.",
        observation_reference=notes,
        interpretation="Recognizes numeric code does not identify cause. Word error is imprecise and does not establish learner believes code necessarily contains a bug; clarified without inventing misconception.",
        limitations=["Following guided A/B diagnosis, not independent retrieval.", "No response after final terminology clarification."]))
records = [concept, debug, boundary]
assessment = dict(assessment_id=sid+"-as01", session_id=sid, checkpoint_id=cpid,
    date="2026-10-22", evidence_ids=[debug["evidence_id"], "2026-10-22-s03-e02", "2026-10-22-s01-e02"],
    before={"scores":{"debugging":None}, "proficiency":"learning"},
    after={"scores":{"debugging":2}, "proficiency":"functional"},
    rationale="Previously deferred debugging score for incomplete crash/termination/startup coverage. A runtime inspection now complements guided B termination correlation and earlier launch failure evidence. Map score 2 fits standard cases with guidance; not independent diagnosis. Concept remains 2 after immediate assisted success, implementation 3 unchanged without reassessment; judgment/transfer null, confidence low. Functional follows map thresholds C>=2/I>=2/D>=2 and does not assert full-domain independence or mastery.")
review = dict(review_id=sid+"-r01", anchor_evidence_ids=[debug["evidence_id"]], anchor_date="2026-10-22",
    target_axes=["debugging"], task_type="delayed_retrieval", target_date="2026-10-24", scheduled_date="2026-10-24",
    scheduling_reason="D2 Saturday fresh H0/H1 runtime diagnosis after guided A/B work. Coordinate a small scope with existing concept/implementation reviews; these remain unchanged. Prioritize status ownership and evidence-to-cause reasoning.",
    status="planned", completed_at=None, result_evidence_ids=[], schedule_history=[])

def append_once(ref, marker, content):
    p = root / ref
    old = p.read_text(encoding="utf-8") if p.exists() else ""
    if marker not in old:
        with p.open("a", encoding="utf-8") as f:
            f.write("\n\n" + content + "\n")

o05 = f"""## {sid}-o05 — batas kesimpulan dan penutupan

Prompt: jika detail log A/B hilang dan hanya worker_exit_code=2 tersedia, apa yang bisa dan belum bisa ditentukan?
Respons aktual: "Yang bisa dipastikan adalah ada error pada worker tetapi penyebabnya apa tidak bisa diketahui".
Kesimpulan bahwa status tidak menetapkan penyebab tepat. Istilah error diperjelas instructor menjadi worker berakhir dengan status nonzero; tidak selalu bug internal karena B dihentikan supervisor. Jangan mengatribusikan klarifikasi ini sebagai jawaban learner atau menganggap kata error membuktikan misconception tertentu. H4 concept/debugging sebelumnya tetap. Belum ada respons setelah klarifikasi.

Target latihan terpenuhi secara terbimbing; akhiri tanpa menambah latihan untuk memenuhi seluruh 45 menit. Tidak ada patch atau eksekusi baru. Penutupan dimulai 2026-10-22T16:04:07+07:00. Startup bertimestamp 15:26:17, pause 15:28:17, resume 15:47:39; rentang sesi di luar pause sekitar 18 menit 28 detik sebelum administrasi, mencakup interaksi/setup dan bukan pengukuran kerja aktif.
"""
append_once(notes, f"## {sid}-o05", o05)
summary = f"""- Session {sid}; **completed**, diag-004 / batch-two-stops-windows-v1 / a001. Melanjutkan cp01 yang paused; cp01 tetap dipertahankan. Penutupan mulai 16:04:07 WIB setelah resume 15:47:39. Tidak memakai sisa waktu untuk task baru setelah target selesai.
- Learner memisahkan pemilik worker/runner, memprediksi worker 2/runner 7 dengan benar, memilih dua log A dan memprediksi bounds error, lalu mengidentifikasi panic stderr sebagai bukti sebab. Jawaban penutup menyatakan status saja tidak menentukan penyebab. Detail o01-o05: {notes}. Tidak ada rerun atau patch; log berasal dari baseline instructor 10:45.
- Evidence {sid}-e01 concept, e02 debugging, e03 concept; satu attempt yang sama, bukan tiga task independen. A logs: labs/diag-004/attempts/a001/artifacts/A/supervisor.log dan worker.stderr.log. Evidence B terdahulu s03-e02 dan startup s01-e02 dipakai bersama tanpa menulis ulang observasi lama.
- Bantuan maksimum concept H4/debugging H4; pemilihan dua log A dibuat learner, tetapi sebab A dan mekanisme B telah diajarkan. Prediksi status berhasil setelah penjelasan ProcessState. Tidak ada bantuan implementation baru atau evidence implementasi sesi ini. Kemandirian/retensi pada varian baru belum teruji.
- Assessment {sid}-as01: debugging null -> 2 karena cakupan guided diagnosis crash/termination/startup kini cukup; concept tetap 2 (immediate guided application), implementation tetap 3, judgment/transfer null, confidence low. Proficiency learning -> functional sesuai ambang map, berarti capability standar dengan guidance, bukan mastery atau seluruh outcome process. 37 competency lain tetap.
- Terminologi error diperjelas menjadi nonzero termination; tidak otomatis bug internal. Tidak menetapkan misconception/pattern berulang baru. Bukti perbaikan provenance segera ada, tetapi perlu fresh check. Mistake-patterns tidak berubah.
- calibration_decision maintain difficulty 1: reasoning membaik dan runtime A selesai dalam scope yang sama; tidak ada dasar menaikkan kompleksitas dari hasil terbantu. Learner meminta pause/resume tanpa laporan bosan/frustrasi. Next check: fresh H0/H1 status ownership dan diagnosis dari runtime.
- Review concept/implementation tetap 24 Oktober 2026; debugging review {sid}-r01 ditambahkan pada tanggal sama (D2). Koordinasikan probe kecil sesuai waktu, bukan tiga sesi penuh wajib. Belum ada review completed atau automation.
- Checkpoint {checkpoint}; active_work null. Source sama dengan starter, tidak ada blocker atau implementasi tertunda. Next direction: review segar 24 Oktober, atau jika belajar sebelum itu pilih target kecil sesuai selection policy tanpa mengulang latihan selesai sebagai retest. Tidak ada commit/push. Validasi akhir dicatat sesudah pemeriksaan.
"""
append_once(checkpoint, f"# Checkpoint {cpid}", f"# Checkpoint {cpid}\n\n" + summary)
append_once(notes, f"## Checkpoint {cpid}", f"## Checkpoint {cpid} — completed\n\n" + summary)
append_once("learner/session-history.md", f"### {cpid}", f"### {cpid}\n\n" + summary)

if cpid != before["last_applied_checkpoint"]:
    assert before["last_applied_checkpoint"] == sid+"-cp01"
    assert node["scores"]["debugging"] is None
    expected = copy.deepcopy(node)
    expected["scores"]["debugging"] = 2
    expected["proficiency"] = "functional"
    expected["evidence"].extend(records)
    expected["assessment_history"].append(assessment)
    expected["review_plan"].append(review)
    start = original.index("  os.processes:\n")
    end = original.index("  os.threads:\n", start)
    candidate = original[:start] + yaml.safe_dump({"os.processes":expected}, sort_keys=False, allow_unicode=True)
    # Indent just the rebuilt node beneath competencies.
    candidate = original[:start] + "".join("  "+line if line.strip() else line for line in yaml.safe_dump({"os.processes":expected}, sort_keys=False, allow_unicode=True).splitlines(True)) + original[end:]
    candidate = candidate.replace("last_applied_checkpoint: "+sid+"-cp01", "last_applied_checkpoint: "+cpid, 1)
    a, b = candidate.index("\nactive_work:")+1, candidate.index("\ncompetencies:")+1
    candidate = candidate[:a] + "active_work: null\n" + candidate[b:]
    after = yaml.safe_load(candidate)
    assert after["competencies"]["os.processes"] == expected
    for cid in before["competencies"]:
        if cid != "os.processes":
            assert after["competencies"][cid] == before["competencies"][cid]
    tmp = path.with_suffix(".yaml.tmp")
    tmp.write_text(candidate, encoding="utf-8")
    tmp.replace(path)

saved = yaml.safe_load(path.read_text(encoding="utf-8"))
assert saved["active_work"] is None and saved["last_applied_checkpoint"] == cpid
assert saved["last_session_id"] == sid
assert set(saved["competencies"]) == set(curriculum["competencies"])
all_evidence = [e for n in saved["competencies"].values() for e in n["evidence"]]
ids = {e["evidence_id"] for e in all_evidence}
assert len(ids) == len(all_evidence)
for e in records:
    assert all(k in e for k in curriculum["assessment_policy"]["evidence_fields"])
    assert (root / e["reasoning_check"]["observation_reference"]).is_file()
    assert e["competency_id"] in curriculum["competencies"]
assert all(i in ids for i in assessment["evidence_ids"])
for ref in (checkpoint, notes, "labs/diag-004/attempts/a001/artifacts/A/worker.stderr.log", "labs/diag-004/attempts/a001/artifacts/A/supervisor.log"):
    assert (root / ref).is_file()
assert saved["competencies"]["os.processes"]["scores"] == dict(concept=2, implementation=3, debugging=2, judgment=None, transfer=None)
assert all(r["scheduled_date"] == "2026-10-24" and r["status"] == "planned" for r in saved["competencies"]["os.processes"]["review_plan"])
assert (root / "learner/session-history.md").read_text(encoding="utf-8").count(f"### {cpid}\n") == 1
assert (root / "labs/diag-004/main.go").read_bytes() == (root / "labs/diag-004/attempts/a001/artifacts/starter-main.go.txt").read_bytes()
validation = "Validasi akhir s04-cp02 PASS: YAML parses, competency IDs/required evidence fields valid, references resolve, evidence IDs unique, state/history/checkpoint consistent. Prior observations preserved; only debugging 2, functional proficiency, new evidence/review and administrative pointers changed. Source unchanged."
for ref in (checkpoint, notes):
    append_once(ref, "Validasi akhir s04-cp02 PASS", validation)
print("PASS: completed checkpoint saved; debugging null->2, proficiency functional; concept 2, implementation 3, confidence low unchanged.")
