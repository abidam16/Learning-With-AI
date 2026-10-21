"""Persist this specific pause idempotently, preserving previous observations."""
from pathlib import Path
import copy
import sys

sys.path.insert(0, r'C:/Users/abid.mahdy/AppData/Local/Temp/learning-lab-yaml-validation')
import yaml

root = Path(__file__).resolve().parents[3]
state_path = root / 'learner/competency-state.yaml'
history_path = root / 'learner/session-history.md'
session = '2026-10-21-s02'
checkpoint = session + '-cp01'
evidence_id = session + '-e01'
original = state_path.read_text(encoding='utf-8')
before = yaml.safe_load(original)
mapping = yaml.safe_load((root / 'curriculum/competency-map.yaml').read_text(encoding='utf-8'))
assert mapping['curriculum_version'] == '1.1.0'
assert set(before['competencies']) == set(mapping['competencies'])

evidence = {
    'evidence_id': evidence_id,
    'session_id': session,
    'date': '2026-10-21',
    'lab_id': 'probe-003',
    'attempt_id': 'a001',
    'competency_id': 'os.processes',
    'axis': 'concept',
    'task_variant': 'report-runner-return-windows-v1',
    'assessment_status': 'assessed',
    'artifact_or_observation': 'labs/probe-003/attempts/a001/notes.md — o01–o04; labs/probe-003/attempts/a001/artifacts/prediction-source.go.txt; labs/probe-003/attempts/a001/artifacts/instructor-run.txt',
    'result': 'Initial prediction incorrectly skipped the worker argument branch and predicted recursion. After neutral Args clarification, learner corrected the trace and predicted Worker: ditolak, Runner: hasil 9, and shell status 0. Instructor execution matched the final prediction.',
    'max_hint': 'H1',
    'prompt_context': 'Full source supplied for a reading probe. Neutral request to evaluate worker Args prompted learner correction; no Args rule or process-status answer supplied before response. Prior H4 teaching on October 20 retained. Explanatory confirmation after the final response is not additional independent evidence.',
    'reasoning_check': {
        'check_type': 'prediction',
        'prompt': 'Predict messages and LASTEXITCODE for lab.exe without arguments. Follow-ups: evaluate Args for lab.exe --worker; then state runner shell status and why.',
        'learner_response': 'Revised initial recursion prediction: worker enters if, prints Worker: ditolak and exits 6. Run returns error and execute returns 9 rather than exiting the runner. Runner prints Runner: hasil 9. LASTEXITCODE is 0 because the original lab.exe finishes normally.',
        'observation_reference': 'labs/probe-003/attempts/a001/notes.md — o01–o04; labs/probe-003/attempts/a001/artifacts/instructor-run.txt',
        'interpretation': 'Supports maintaining concept 3 for the previously assessed narrow distinction between worker exit, function return, and parent completion. Initial reading error corrected after H1 does not warrant an automatic decrease. No promotion warranted.',
        'limitations': ['Same-day familiar mechanism; not delayed retrieval or transfer.', 'Execution performed by instructor; no learner implementation or runtime diagnostic assessed.', 'PID, environment, signals, shutdown and startup/crash/kill distinctions not assessed in this probe.'],
    },
    'retest_of': None,
    'correction_of': None,
}
active = {
    'lab_id': 'diag-003',
    'task_variant': 'report-runner-two-reports-windows-v1',
    'attempt_id': 'a001',
    'session_id': session,
    'checkpoint_id': checkpoint,
    'checkpoint_reference': 'learner/sessions/2026-10-21-s02/checkpoint.md',
    'next_step': 'Read diag-003/main.go and request one hypothesis, predicted observation, and discriminating experiment before execution or edits. Learner has not answered yet; preserve blind diagnostic.',
}
candidate = original
existing = before['competencies']['os.processes']['evidence']
if not any(e['evidence_id'] == evidence_id for e in existing):
    chunk = yaml.safe_dump([evidence], allow_unicode=True, sort_keys=False, width=100)
    indented = ''.join('    ' + line if line.strip() else line for line in chunk.splitlines(keepends=True))
    candidate = candidate.replace('    assessment_history:\n', indented + '    assessment_history:\n', 1)
if before['last_session_id'] != session:
    candidate = candidate.replace('last_session_id: ' + before['last_session_id'], 'last_session_id: ' + session, 1)
if before['last_applied_checkpoint'] != checkpoint:
    candidate = candidate.replace('last_applied_checkpoint: ' + before['last_applied_checkpoint'], 'last_applied_checkpoint: ' + checkpoint, 1)
if before['active_work'] is None:
    candidate = candidate.replace('active_work: null\n', yaml.safe_dump({'active_work': active}, allow_unicode=True, sort_keys=False, width=100), 1)
else:
    assert before['active_work'] == active, 'Unexpected active work; do not overwrite'

after = yaml.safe_load(candidate)
for competency_id, old in before['competencies'].items():
    expected = copy.deepcopy(old)
    if competency_id == 'os.processes' and not any(e['evidence_id'] == evidence_id for e in old['evidence']):
        expected['evidence'].append(evidence)
    assert after['competencies'][competency_id] == expected, competency_id
assert after['active_work'] == active
all_ids = [e['evidence_id'] for c in after['competencies'].values() for e in c['evidence']]
assert len(all_ids) == len(set(all_ids))
for p in [
    active['checkpoint_reference'],
    'labs/probe-003/attempts/a001/notes.md',
    'labs/probe-003/attempts/a001/artifacts/prediction-source.go.txt',
    'labs/probe-003/attempts/a001/artifacts/instructor-run.txt',
    'labs/diag-003/attempts/a001/notes.md',
    'labs/diag-003/attempts/a001/artifacts/instructor-baseline.txt',
    'labs/diag-003/attempts/a001/artifacts/starter-main.go.txt',
]:
    assert (root / p).is_file(), p
for lab_id in ('probe-003', 'diag-003'):
    lab = yaml.safe_load((root / 'labs' / lab_id / 'lab.yaml').read_text(encoding='utf-8'))
    assert all(cid in mapping['competencies'] for cid in lab['primary_competency_ids'])
assert (root / 'labs/diag-003/main.go').read_bytes() == (root / 'labs/diag-003/attempts/a001/artifacts/starter-main.go.txt').read_bytes()
if candidate != original:
    pending = state_path.with_suffix('.yaml.pending')
    pending.write_text(candidate, encoding='utf-8')
    assert yaml.safe_load(pending.read_text(encoding='utf-8')) == after
    pending.replace(state_path)

history = history_path.read_text(encoding='utf-8')
if '### ' + checkpoint not in history:
    entry = '''

### 2026-10-21-s02-cp01

- Session 2026-10-21-s02; status paused atas permintaan learner karena perlu melakukan hal lain. Penutupan dimulai 2026-10-21T09:24:38+07:00; pemeriksaan environment 08:55:08, rentang sekitar 29 menit 30 detik termasuk setup/interaksi/jeda, bukan waktu kerja aktif.
- Probe-003 / report-runner-return-windows-v1 / a001 completed. Prediksi awal rekursi dikoreksi setelah klarifikasi Args H1. Learner menjelaskan worker exit 6, function return 9, dan runner shell status 0. Instructor build/run menghasilkan dua pesan yang diprediksi dan status 0.
- Evidence baru 2026-10-21-s02-e01, concept. Detail: labs/probe-003/attempts/a001/notes.md o01–o04; snapshot source dan output di artifacts. Full source/instrumentasi eksekusi disediakan instructor; bukan implementation/debugging evidence learner. Prior H4 tetap tercatat; maksimum bantuan baru sebelum jawaban concept H1.
- Skor tidak berubah: os.processes concept/implementation 3, debugging/judgment/transfer null; confidence low, proficiency learning. Same-day prediction mendukung lingkup lama, bukan retensi tertunda/transfer/promosi. Semua competency lain tetap. Tidak ada assessment promosi baru; reading slip yang dikoreksi belum menjadi pattern. Mistake-patterns tidak diubah.
- Diag-003 / report-runner-two-reports-windows-v1 / a001 aktif tetapi belum dijawab: soal dua pilihan dengan Runner: gagal/status 2 disampaikan setelah baseline diverifikasi. Hipotesis learner, prediksi eksperimen dan hasil diagnostik belum ada; tidak dinilai sebagai gagal karena pause. Notes dan baseline: labs/diag-003/attempts/a001/notes.md dan artifacts.
- Environment Go portable 1.26.0 pulih; arsip resmi/checksum diverifikasi, build final kedua lab berhasil. Setup sempat gagal karena ekstraksi standard library belum lengkap; bukan evidence learner. PATH sistem tidak diubah. Periksa ulang runtime TEMP saat resume.
- Feedback learner: perlu melakukan hal lain; tidak ada pernyataan frustrasi/bosan. Kalibrasi pause, difficulty tetap 1. Scope telah diperkecil menjadi satu eksperimen karena waktu setup, bukan karena kemampuan. Next check: kualitas hipotesis dan eksperimen pembeda.
- Checkpoint learner/sessions/2026-10-21-s02/checkpoint.md; active_work diag-003. Next step: learner membaca main.go dan memberikan satu hipotesis, predicted observation, serta eksperimen pembeda sebelum menjalankan atau mengubah source. Tidak ada patch yang perlu dipulihkan.
- Dua review concept/implementation tetap planned 24 Oktober 2026; belum due. Tidak ada automation atau commit/push. State dan history disimpan; validasi akhir dicatat di checkpoint setelah pemeriksaan.
'''
    with history_path.open('a', encoding='utf-8') as f:
        f.write(entry)
assert history_path.read_text(encoding='utf-8').count('### ' + checkpoint) == 1
assert yaml.safe_load(state_path.read_text(encoding='utf-8')) == after
print('PASS: YAML, IDs, references, unchanged scores/history, source snapshot, active_work and session consistency. Evidence total:', len(all_ids))
