"""Save the completed session once; preserve all prior assessments and observations."""
from pathlib import Path
import copy
import sys
sys.path.insert(0, 'C:/Users/abid.mahdy/AppData/Local/Temp/learning-lab-yaml-validation')
import yaml

root = Path(__file__).resolve().parents[3]
state_file = root / 'learner/competency-state.yaml'
history_file = root / 'learner/session-history.md'
session = '2026-10-22-s01'
cp = session + '-cp01'
original = state_file.read_text(encoding='utf-8')
before = yaml.safe_load(original)
mapping = yaml.safe_load((root / 'curriculum/competency-map.yaml').read_text(encoding='utf-8'))
assert mapping['curriculum_version'] == before['curriculum_version'] == '1.1.0'
assert set(before['competencies']) == set(mapping['competencies'])
notes = 'labs/diag-003/attempts/a001/notes.md'
output = 'labs/diag-003/attempts/a001/artifacts/2026-10-22-s01-learner-direct-output.txt'
baseline = 'labs/diag-003/attempts/a001/artifacts/2026-10-22-s01-instructor-baseline.txt'
common = {
    'session_id': session, 'date': '2026-10-22', 'lab_id': 'diag-003', 'attempt_id': 'a001',
    'competency_id': 'os.processes', 'task_variant': 'report-runner-two-reports-windows-v1',
    'artifact_or_observation': notes + ' — 2026-10-22-s01-o01 through o07; ' + output + '; ' + baseline,
    'max_hint': 'H1',
    'prompt_context': 'Learner independently selected direct commands and hypothesized distinct causes before new hints. Neutral H1 questions corrected initial conflation of direct and wrapper invocation output/status. Learner predicted stale LASTEXITCODE before instructor confirmation. Prior H4 teaching on October 20 remains documented. Executable and source supplied; no instructor solution patch.',
    'retest_of': None, 'correction_of': None,
}
concept = dict(common, evidence_id=session+'-e01', axis='concept', assessment_status='assessed',
    result='Learner explained intentional worker exit 6 versus missing executable, corrected direct invocation predictions after H1, independently predicted that shell lookup failure preserves previous LASTEXITCODE 6, and reported matching observations. Parent error mapping explains status 2 for both cases.')
concept['reasoning_check'] = {
    'check_type': 'prediction',
    'prompt': 'Before direct invocation of bundle/processor.exe --worker, predict messages and LASTEXITCODE and explain why.',
    'learner_response': 'Executable is absent, so main is never reached and only a system error appears. LASTEXITCODE remains 6 from the previous direct worker command. Wrapper B separately returns/exits 2 on Run error.',
    'observation_reference': output,
    'interpretation': 'Maintains concept 3 for lifecycle and exit-status scope. Correct prediction distinguishes lookup failure from a process exit and from the wrapper result. No promotion or automatic decrease from initial corrected reading/prediction error.',
    'limitations': ['Reported terminal output rather than instructor rerun of learner commands.', 'Same previously presented attempt, not delayed retrieval or transfer.', 'No PID, signals, controlled shutdown or full process-domain assessment.'],
}
debugging = dict(common, evidence_id=session+'-e02', axis='debugging', assessment_status='not_observed',
    result='Partial diagnostic evidence: learner chose direct A/B command comparisons, revised predictions with H1, reported silent exit 6 for direct worker and shell CommandNotFoundException plus stale 6 for absent target, and proposed adding err to generic failure output.')
debugging['reasoning_check'] = {
    'check_type': 'discriminating_experiment',
    'prompt': 'Choose an experiment and predict distinct results for the two possible causes; after results, choose one additional item in Runner: gagal for the operator and explain why.',
    'learner_response': 'Run lab.exe --worker and bundle/processor.exe --worker directly. After neutral clarification, predicted silent 6 for the first, lookup error and previous 6 for the second, reported both, and selected err details so the failure cause is visible.',
    'observation_reference': output,
    'interpretation': 'Valid partial debugging evidence distinguishes intentional nonzero exit from launch failure. Full-node score remains null consistently with prior assessment scope: crash and force termination discrimination remain untested. not_observed refers to insufficient coverage for that numeric score, not absence of all diagnostic skill.',
    'limitations': ['No crash/kill experiment; exit 6 is intentional and must not be labeled a crash.', 'Direct B error comes from PowerShell, not captured Go Run error; runtime instrumentation not implemented.', 'Two commands belong to one attempt, not two independent task variants.', 'Operator-information choice is not evidence for graceful versus force-termination judgment.'],
}
candidate = original
old_records = before['competencies']['os.processes']['evidence']
additions = [e for e in (concept, debugging) if not any(x['evidence_id']==e['evidence_id'] for x in old_records)]
if additions:
    block = yaml.safe_dump(additions, allow_unicode=True, sort_keys=False, width=100)
    block = ''.join('    '+line if line.strip() else line for line in block.splitlines(keepends=True))
    candidate = candidate.replace('    assessment_history:\n', block+'    assessment_history:\n', 1)
candidate = candidate.replace("updated_on: '"+before['updated_on']+"'", "updated_on: '2026-10-22'", 1)
candidate = candidate.replace('last_session_id: '+before['last_session_id'], 'last_session_id: '+session, 1)
candidate = candidate.replace('last_applied_checkpoint: '+before['last_applied_checkpoint'], 'last_applied_checkpoint: '+cp, 1)
if before['active_work'] is not None:
    assert before['active_work']['lab_id']=='diag-003'
    start = candidate.index('active_work:\n')
    end = candidate.index('competencies:\n', start)
    candidate = candidate[:start]+'active_work: null\n'+candidate[end:]
candidate = candidate.replace("    last_assessed_on: '2026-10-21'", "    last_assessed_on: '2026-10-22'", 1)
after = yaml.safe_load(candidate)
for cid, previous in before['competencies'].items():
    expected = copy.deepcopy(previous)
    if cid=='os.processes':
        expected['evidence'].extend(additions)
        expected['last_assessed_on']='2026-10-22'
    assert after['competencies'][cid]==expected, cid
    assert cid in mapping['competencies']
    assert all(s is None or (type(s) is int and 0<=s<=4) for s in expected['scores'].values())
    due = any(r['status']=='planned' and r['scheduled_date'] is not None and r['scheduled_date']<='2026-10-22' for r in expected['review_plan'])
    assert expected['review_due']==due
ids = [e['evidence_id'] for c in after['competencies'].values() for e in c['evidence']]
assert len(ids)==len(set(ids))
assert after['active_work'] is None
for ref in [notes, output, baseline, 'learner/sessions/'+session+'/checkpoint.md', 'labs/diag-003/attempts/a001/artifacts/starter-main.go.txt']:
    assert (root/ref).is_file(), ref
lab = yaml.safe_load((root/'labs/diag-003/lab.yaml').read_text(encoding='utf-8'))
assert lab['task_variant']==concept['task_variant']
assert all(cid in mapping['competencies'] for cid in lab['primary_competency_ids'])
assert (root/'labs/diag-003/main.go').read_bytes()==(root/'labs/diag-003/attempts/a001/artifacts/starter-main.go.txt').read_bytes()
if candidate != original:
    pending = state_file.with_suffix('.yaml.pending')
    pending.write_text(candidate, encoding='utf-8')
    assert yaml.safe_load(pending.read_text(encoding='utf-8'))==after
    pending.replace(state_file)
if '### '+cp not in history_file.read_text(encoding='utf-8'):
    with history_file.open('a', encoding='utf-8') as f:
        f.write('''

### 2026-10-22-s01-cp01

- Session 2026-10-22-s01; completed. Diag-003 / report-runner-two-reports-windows-v1 / a001 mencapai target diagnosis dan reasoning, melanjutkan 2026-10-21-s02-cp01. Tidak ada patch wajib atau pekerjaan aktif tersisa.
- Penutupan dimulai 2026-10-22T06:24:40+07:00; pemeriksaan awal 05:50:01 WIB. Rentang sekitar 34 menit 39 detik termasuk setup/interaksi/jeda, bukan durasi kerja aktif. Anggaran 45 menit.
- Learner menelusuri A sebagai intentional exit worker dan B sebagai kegagalan menjalankan executable. Memilih dua direct invocations sendiri. Prediksi awal mencampur wrapper dan direct output/status; dikoreksi setelah H1. Prediksi revisi dibuat sebelum eksekusi: worker silent/status 6; command B lookup error dengan LASTEXITCODE lama 6. Kedua hasil dilaporkan cocok. Memilih keterangan err untuk laporan operator.
- Evidence 2026-10-22-s01-e01 concept dan e02 debugging parsial, satu attempt. Catatan labs/diag-003/attempts/a001/notes.md o01–o07; output learner-reported pada artifacts/2026-10-22-s01-learner-direct-output.txt. Baseline A/B instructor-verified; source sama dengan snapshot. Error B yang dikirim berasal dari PowerShell, bukan log error Go Run.
- Assistance baru maksimum concept/debugging H1 untuk prediksi scope; hipotesis/pilihan eksperimen awal H0, prior H4 tetap dicatat. Tidak ada solusi patch atau implementasi baru. Source/executable supplied; tooling support terpisah.
- Seluruh skor tetap: os.processes concept/implementation 3, debugging/judgment/transfer null, confidence low, proficiency learning. Concept diperkuat pada scope sama. Evidence debugging kini mendukung intentional exit versus launch failure; crash/kill belum diuji sehingga skor node penuh tetap null, bukan dianggap gagal. Pilihan informasi err tidak menguji judgment graceful/force termination. Tidak ada assessment promosi/penurunan baru; last_assessed_on diperbarui.
- Misconception awal direct-versus-wrapper dikoreksi. Belum cukup dasar menyamakannya dengan slip Args kemarin sebagai recurring pattern; mistake-patterns tidak diubah. Kalibrasi maintain level 1, target selesai tanpa menambah lab; learner tidak melaporkan bosan/frustrasi.
- Runtime portable lama tidak ditemukan di sandbox; executable berjalan dan tidak ada rebuild yang diperlukan. Pastikan tooling sebelum lab berikut yang membutuhkan build. Jangan menganggap setup sebagai evidence kemampuan.
- Checkpoint learner/sessions/2026-10-22-s01/checkpoint.md. active_work null. Review concept/implementation tetap 24 Oktober 2026, belum due. Resume ini bukan retest. Next direction: fresh scheduled review H0/H1; bila sesi sebelum review, probe kecil crash/termination dengan fixture terverifikasi untuk cakupan debugging yang belum diketahui.
- State/history ditulis; validasi akhir di checkpoint. Tidak ada automation, commit atau push.
''')
assert history_file.read_text(encoding='utf-8').count('### '+cp)==1
assert yaml.safe_load(state_file.read_text(encoding='utf-8'))==after
print('PASS: YAML/IDs/references, prior observations and all scores preserved, review dates unchanged, source unchanged, completed session consistent; evidence total', len(ids))
