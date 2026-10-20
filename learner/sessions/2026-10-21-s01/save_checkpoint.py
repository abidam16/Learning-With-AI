"""Persist this completed learning session, without editing learner source."""
import copy
import os
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(os.environ['TEMP']) / 'learning-lab-yaml-validation'))
import yaml

ROOT = Path(__file__).resolve().parents[3]
SESSION = '2026-10-21-s01'
CP = SESSION + '-cp01'
DATE = '2026-10-21'
NOTES = 'labs/diag-002/attempts/a001/notes.md'
ART = 'labs/diag-002/attempts/a001/artifacts/'
STATE = ROOT / 'learner/competency-state.yaml'
raw = STATE.read_text(encoding='utf-8')
state = yaml.safe_load(raw)
before = copy.deepcopy(state)
curriculum = yaml.safe_load((ROOT / 'curriculum/competency-map.yaml').read_text(encoding='utf-8'))
lab = yaml.safe_load((ROOT / 'labs/diag-002/lab.yaml').read_text(encoding='utf-8'))
node = state['competencies']['os.processes']
assert curriculum['curriculum_version'] == state['curriculum_version'] == lab['curriculum_version'] == '1.1.0'

def evidence(number, axis, status, result, hint, check_type, prompt, response, interpretation, refs):
    return dict(evidence_id=f'{SESSION}-e{number:02}', session_id=SESSION, date=DATE,
                lab_id='diag-002', attempt_id='a001', competency_id='os.processes', axis=axis,
                task_variant=lab['task_variant'], assessment_status=status,
                artifact_or_observation=refs, result=result, max_hint=hint,
                prompt_context='New near variant after H4 concept/API teaching on 2026-10-20. Launcher, streams, fixture, tests and business contract supplied. No new solution hint or instructor patch; neutral scope clarification H1. Not cross-stack transfer or completion of October 24 retrieval.',
                reasoning_check=dict(check_type=check_type, prompt=prompt, learner_response=response,
                                     observation_reference=refs, interpretation=interpretation,
                                     limitations=['One attempt and near variant; familiar API.',
                                                  'Worker/batch terminal comparisons learner-reported; contract rerun instructor-verified.',
                                                  'Silent worker exit-7 boundary is hypothetical, not executed.',
                                                  'PID, environment, signals, shutdown, crash/kill/startup and broad transfer untested.']),
                retest_of=None, correction_of=None)

records = [
    evidence(1, 'concept', 'assessed',
             'Correctly predicted starter messages/status 0, explained worker status 4 versus deliver completion/return 0, then predicted patched parent silent/status 2 for a silent worker exiting 7.',
             'H1', 'boundary_case',
             'If worker prints nothing then calls os.Exit(7), what output and LASTEXITCODE follow with your current code, and why?',
             'No output; LASTEXITCODE 2 because err != nil reaches os.Exit(2), preventing execution after the if block.',
             'Independent causal reasoning on this representative lifecycle/status slice supports concept 3. Earlier ambiguous referent resolved by subsequent explanation; no unsupported score reduction.',
             NOTES + ' — s01-o01, s01-o05, s01-o07'),
    evidence(2, 'implementation', 'assessed',
             'Learner added err := worker.Run() and nonzero parent exit on error. All three contract cases and three fixture cases pass on fresh instructor run, exit 0; no hardcoded scenario or text, worker runs once.',
             'H0', 'causal_explanation',
             'Complete deliver for the three business contracts, then predict the silent worker/nonzero boundary with your implementation.',
             'Learner-authored error check exits parent with 2, otherwise prints completion and returns 0. Explained why the error branch prevents later output for silent worker exit 7.',
             'Independent implementation and relevant boundary explanation support implementation 3 within result handling. Not evidence of implementing launcher, signal handling or controlled shutdown.',
             ART + 's01-patch01-main.go.txt; ' + ART + 's01-patch01-instructor-test.txt; ' + NOTES + ' — s01-o06, s01-o07'),
    evidence(3, 'debugging', 'not_observed',
             'Learner chose direct --worker kirim invocation, predicted two messages/status 4 and falsifier, reported matching result, then contrasted parent completion/status 0 and identified missing result check.',
             'H1', 'discriminating_experiment',
             'Which experiment tests your explanation of the two statuses, and what observation would refute it?',
             'Invoke lab.exe --worker kirim and inspect LASTEXITCODE. Expect only the two worker messages and 4; completion with 0 would contradict prediction. Reported matching result and later parent completion/0.',
             'Useful partial diagnostic evidence. Full debugging score remains null because mapped crash/kill/startup differentiation was not tested. Similar experiment used yesterday; not novel transfer.',
             NOTES + ' — s01-o02 through s01-o05'),
]

if state['last_applied_checkpoint'] != CP:
    assert state['last_applied_checkpoint'] == '2026-10-20-s02-cp01'
    assert node['scores'] == dict(concept=2, implementation=2, debugging=None, judgment=None, transfer=None)
    existing = {e['evidence_id'] for n in state['competencies'].values() for e in n['evidence']}
    assert not existing.intersection(e['evidence_id'] for e in records)
    node['evidence'].extend(records)
    node['scores']['concept'] = node['scores']['implementation'] = 3
    node['last_assessed_on'] = DATE
    node['assessment_history'].append(dict(
        assessment_id=SESSION + '-as01', session_id=SESSION, checkpoint_id=CP, date=DATE,
        evidence_ids=[records[0]['evidence_id'], records[1]['evidence_id']],
        before={'scores': {'concept': 2, 'implementation': 2}},
        after={'scores': {'concept': 3, 'implementation': 3}},
        rationale='Independent prediction, learner-designed comparison, learner-authored passing patch and correct boundary reasoning on a fresh near variant support 3 for the same narrow lifecycle/status slice previously assessed at 2. New assistance concept H1/implementation H0, prior H4 retained. No claim of full process outcome coverage. Debugging/judgment/transfer stay null, confidence low and proficiency learning remain; one familiar mechanism family is insufficient for broader confidence or proficiency.'))
    state.update(updated_on=DATE, last_session_id=SESSION, last_applied_checkpoint=CP, active_work=None)
    for n in state['competencies'].values():
        n['review_due'] = any(r['status'] == 'planned' and r.get('scheduled_date') and r['scheduled_date'] <= DATE for r in n['review_plan'])
    prefix = raw[:raw.index('schema_version:')]
    candidate = prefix + yaml.safe_dump(state, allow_unicode=True, sort_keys=False, width=110)
    assert yaml.safe_load(candidate) == state
    pending = STATE.with_name('competency-state.s01.pending.yaml')
    pending.write_text(candidate, encoding='utf-8')
    assert yaml.safe_load(pending.read_text(encoding='utf-8')) == state
    pending.replace(STATE)

history = ROOT / 'learner/session-history.md'
entry = f'''

### {CP}

- Session {SESSION}; status completed. Lab diag-002 / document-delivery-windows-v1 / a001 selesai; lab lama tidak dilanjutkan karena sudah completed.
- Penutupan dimulai 2026-10-21T06:40:26+07:00; timestamp pemeriksaan setup 06:12:12. Anggaran 45 menit, waktu pesan pertama dan kerja aktif tidak diukur. Tidak menambah latihan setelah target tercapai.
- Learner memprediksi perilaku program awal, memilih worker langsung sebagai pembanding, melaporkan status worker 4 versus program awal 0, dan mendiagnosis keputusan deliver. Setelah klarifikasi referen netral, penjelasan status konsisten. Learner menulis patch tanpa bantuan kode baru. Semua fixture/kontrak PASS pada instructor rerun, exit 0.
- Prediksi penutup benar: worker tanpa output/exit 7 menghasilkan program awal tanpa output/status 2 karena cabang error memanggil os.Exit(2). Hipotetis tidak dieksekusi. Catatan: {NOTES}, s01-o01 sampai s01-o07.
- Evidence {SESSION}-e01 concept, e02 implementation, e03 debugging parsial; satu attempt, bukan tiga keberhasilan independen. Snapshot {ART}s01-patch01-main.go.txt; log {ART}s01-patch01-instructor-test.txt.
- Assessment {SESSION}-as01: concept 2 -> 3 dan implementation 2 -> 3 untuk lingkup lifecycle/status dan penanganan hasil worker pada varian dekat. Alasan: prediksi, patch dan boundary reasoning mandiri setelah pengajaran kemarin. Tidak mengklaim seluruh outcome process atau mastery. Debugging/judgment/transfer tetap null; confidence low, proficiency learning tetap. 37 competency lain tidak berubah.
- Bantuan baru maksimum: concept H1, implementation H0, debugging H1. Launcher/streams/fixture/test disediakan instructor; prior H4 tanggal 20 Oktober tetap tercatat. Tidak ada patch instructor, solusi atau penjelasan API baru sebelum implementasi.
- Ketidakjelasan scope pertanyaan pada o04 teratasi pada o05/o07; tidak ditetapkan sebagai misconception berulang. Istilah API error versus variabel shell masih dapat dipastikan saat review. Mistake patterns tidak diubah.
- Feedback: learner menyediakan 45 menit; tidak ada laporan frustrasi/bosan. Kalibrasi maintain level 1 berdasarkan bantuan sebelumnya dan baru satu varian independen. Next check: fresh retrieval H0/H1, kemudian probe startup failure kecil bila waktu cukup.
- Checkpoint: learner/sessions/{SESSION}/checkpoint.md. active_work null; tidak ada blocker atau pekerjaan tertunda. Kedua review concept/implementation tetap planned 24 Oktober 2026, belum due saat sesi ini. Tidak ada automation.
- State sudah diterapkan; validasi akhir penyimpanan dicatat di checkpoint setelah pemeriksaan history/referensi. Tidak ada commit/push.
'''
if f'### {CP}' not in history.read_text(encoding='utf-8'):
    with history.open('a', encoding='utf-8') as f:
        f.write(entry)

saved = yaml.safe_load(STATE.read_text(encoding='utf-8'))
assert saved == state
assert set(saved['competencies']) == set(curriculum['competencies'])
assert saved['last_session_id'] == SESSION and saved['last_applied_checkpoint'] == CP and saved['active_work'] is None
all_evidence, all_assessments, all_reviews = [], [], []
for cid, n in saved['competencies'].items():
    if cid != 'os.processes':
        assert n == before['competencies'][cid]
    assert set(n['scores']) == set(curriculum['assessment_policy']['axes'])
    assert all(v is None or type(v) is int and 0 <= v <= 4 for v in n['scores'].values())
    all_evidence.extend(e['evidence_id'] for e in n['evidence'])
    all_assessments.extend(a['assessment_id'] for a in n['assessment_history'])
    all_reviews.extend(r['review_id'] for r in n['review_plan'])
    for e in n['evidence']:
        assert e['competency_id'] == cid and e['axis'] in n['scores']
        assert all(k in e for k in curriculum['assessment_policy']['evidence_fields'])
for ids in (all_evidence, all_assessments, all_reviews):
    assert len(ids) == len(set(ids))
for n in saved['competencies'].values():
    for a in n['assessment_history']:
        assert set(a['evidence_ids']) <= set(all_evidence)
    for r in n['review_plan']:
        assert set(r['anchor_evidence_ids']) <= set(all_evidence)
assert saved['competencies']['os.processes']['review_plan'] == before['competencies']['os.processes']['review_plan']
assert saved['competencies']['os.processes']['scores'] == dict(concept=3, implementation=3, debugging=None, judgment=None, transfer=None)
assert len(all_evidence) == 9
for ref in set(re.findall(r'(?:labs|learner|docs|curriculum)/[^\s;—]+?\.(?:md|txt|go|yaml)(?![\w.])', yaml.safe_dump(saved) + entry)):
    assert (ROOT / ref).is_file(), ref
assert (ROOT / 'labs/diag-002/main.go').read_bytes() == (ROOT / (ART + 's01-patch01-main.go.txt')).read_bytes()
assert history.read_text(encoding='utf-8').count(f'### {CP}') == 1
stamp = datetime.now(timezone(timedelta(hours=7))).isoformat(timespec='seconds')
marker = 'Verifikasi akhir checkpoint: PASS'
for rel in (NOTES, f'learner/sessions/{SESSION}/checkpoint.md'):
    p = ROOT / rel
    if marker not in p.read_text(encoding='utf-8'):
        with p.open('a', encoding='utf-8') as f:
            f.write(f'\n\n{marker}, {stamp}. YAML, IDs, evidence references, snapshot, state/history consistency validated. Sembilan evidence total; concept/implementation 3, 188 skor lain tetap null. Review 24 Oktober dipertahankan, active_work null. Tidak ada commit/push.\n')
print('PASS: completed checkpoint saved and validated; 9 evidence, concept=3, implementation=3; other scores unchanged; October 24 reviews preserved.')
