from pathlib import Path
from copy import deepcopy
from datetime import datetime, timezone, timedelta
import os, sys, tempfile
sys.path.insert(0, str(Path(tempfile.gettempdir()) / 'learning-lab-yaml-validation'))
import yaml

root = Path(__file__).resolve().parents[3]
sid, cp = '2026-10-26-s01', '2026-10-26-s01-cp01'
date = '2026-10-26'
stamp = datetime.now(timezone(timedelta(hours=7))).isoformat(timespec='seconds')
path = root / 'learner/competency-state.yaml'
raw = path.read_text(encoding='utf-8')
old = yaml.safe_load(raw)
state = deepcopy(old)
curriculum = yaml.safe_load((root / 'curriculum/competency-map.yaml').read_text(encoding='utf-8'))
lab = yaml.safe_load((root / 'labs/review-001/lab.yaml').read_text(encoding='utf-8'))
assert curriculum['curriculum_version'] == lab['curriculum_version'] == state['curriculum_version']
assert set(state['competencies']) == set(curriculum['competencies'])
target = state['competencies']['os.files-and-descriptors']
notes = 'labs/review-001/attempts/a001/notes.md'
art = 'labs/review-001/attempts/a001/artifacts/s01-o03/'
assert (root / 'labs/review-001/save.go').read_bytes() == (root / (art + 'save.go.txt')).read_bytes()
assert (root / (art + 'exit-code.txt')).read_text().strip() == '0'
assert (root / (art + 'tests.txt')).read_text().count('--- PASS: TestReceipt/') == 4
common = dict(session_id=sid, date=date, lab_id='review-001', attempt_id='a001', competency_id='os.files-and-descriptors', task_variant=lab['task_variant'], assessment_status='assessed', max_hint='H1', correction_of=None,
    prompt_context='Fresh D3 retrieval after October 23 H5 teaching. H0 initial prediction; H1 trace against existing cleanup contract prompted learner revision. No instructor pseudocode/patch. Later general-defer clarification H4 is outside these pre-clarification observations.')
records = [dict(common, evidence_id=sid+'-e01', axis='concept', retest_of='2026-10-23-s04-e02', artifact_or_observation=notes+' — o01-o03', result='Independently predicts deferred assignment replacing a prior error with nil; after H1 contract trace proposes unconditional cleanup and conditional result replacement; correctly predicts first-error precedence when both operations fail.', reasoning_check=dict(check_type='delayed_retrieval', prompt='Predict the original return with Write failure and successful Close, trace the learner conditional proposal, then predict both-failure return before running the repair.', learner_response='Original returns nil due to named-result assignment; guard can skip Close; call Close into a new variable first and conditionally assign its result. With both failures, destination full survives because err is non-nil.', observation_reference=notes+' — o01-o03', interpretation='Supports concept 3 for this narrow resource-result and cleanup sequence at H1 after three days, extending prior path-scoped evidence.', limitations=['Initial cleanup proposal was incomplete and corrected after H1.', 'Similar mechanism and familiar language, not transfer.', 'General defer wording required later H4 clarification; no learner uptake of that clarification yet.'])),
 dict(common, evidence_id=sid+'-e02', axis='implementation', retest_of='2026-10-23-s04-e01', artifact_or_observation=art+'save.go.txt; '+art+'tests.txt; '+notes+' — o02-o03', result='Learner implements unconditional Close into a local value and conditional named-result replacement. Instructor fresh go test -count=1 -v . exits 0; four normal/failure cases pass, all with one Close.', reasoning_check=dict(check_type='boundary_case', prompt='Before tests, predict the returned error if both writing and Close fail and explain why.', learner_response='destination full is returned because the non-nil existing err prevents replacement by destination close failed.', observation_reference=notes+' — o03; '+art+'tests.txt', interpretation='Supports implementation 3 for standard safe cleanup and error precedence with H1 only; observed patch matches reasoning and runtime checks.', limitations=['Instructor authored and ran tests; no learner test-design claim.', 'Controlled destination, no actual disk, permission or durability assessment.', 'Short record exercises underlying failure at Flush, not direct Fprintln failure.']))]
existing = {e['evidence_id'] for e in target['evidence']}
if not any(r['evidence_id'] in existing for r in records):
    assert target['scores']['implementation'] == 2
    target['evidence'].extend(records)
    target['assessment_history'].append(dict(assessment_id=sid+'-as01', session_id=sid, checkpoint_id=cp, date=date, evidence_ids=[r['evidence_id'] for r in records], before={'scores':{'implementation':2}}, after={'scores':{'implementation':3}}, rationale='Learner-authored standard cleanup/error-precedence repair and correct pre-execution reasoning verified at H1 on a fresh D3 variant. Concept 3 gains narrow retrieval support; other axes, low confidence and functional proficiency remain unchanged. Initial guarded-cleanup proposal and later defer terminology limitation retained.'))
    target['scores']['implementation'] = 3
    target['last_assessed_on'] = date
    review = next(r for r in target['review_plan'] if r['review_id']=='2026-10-23-s04-r01')
    review.update(status='completed', completed_at=stamp, result_evidence_ids=[r['evidence_id'] for r in records])
    target['review_plan'].append(dict(review_id=sid+'-r01', anchor_evidence_ids=[r['evidence_id'] for r in records], anchor_date=date, target_axes=['concept','implementation'], task_type='delayed_retrieval', target_date='2026-11-02', scheduled_date='2026-11-01', scheduling_reason='D7 target adapted to available Sunday, actual planned D6; use another resource/return shape and verify unconditional cleanup without solution cues. No external reminder.', status='planned', completed_at=None, result_evidence_ids=[], schedule_history=[]))
else:
    assert all(r['evidence_id'] in existing for r in records)
for node in state['competencies'].values():
    node['review_due'] = any(r['status']=='planned' and r.get('scheduled_date') and r['scheduled_date']<=date for r in node['review_plan'])
state.update(updated_on=date, last_session_id=sid, last_applied_checkpoint=cp, active_work=None)
for key, node in state['competencies'].items():
    if key != 'os.files-and-descriptors':
        a, b = deepcopy(node), deepcopy(old['competencies'][key])
        a.pop('review_due'); b.pop('review_due'); assert a == b
all_e = [e['evidence_id'] for n in state['competencies'].values() for e in n['evidence']]
assert len(all_e)==len(set(all_e))
for n in state['competencies'].values():
    assert all(v is None or type(v) is int and 0 <= v <= 4 for v in n['scores'].values())
    for r in n['review_plan']:
        assert all(e in all_e for e in r['anchor_evidence_ids']+r['result_evidence_ids'])
for f in [notes, art+'save.go.txt', art+'tests.txt', art+'exit-code.txt']:
    assert (root/f).is_file()
checkpoint = root / f'learner/sessions/{sid}/checkpoint.md'
body = f'''# Checkpoint {cp}

- Status **completed** for bounded review-001 / receipt-destination-result-v1 / a001. Saved at {stamp}. Session may continue with a short due review within the original conservative 06:55 WIB close; no automatic extra time.
- Learner predicts original nil result independently, revises conditional cleanup after H1 contract trace, writes repair, and predicts both-failure precedence correctly. Four instructor-controlled cases PASS, exit 0, Close once in every case. Artifacts: {art}save.go.txt and tests.txt. No instructor target edit.
- Early-return explanation correct; general claim that defer operates on return value narrowed by instructor afterward (H4 on that terminology only). Uptake not yet observed; keep separate from H0/H1 assessed o01-o03.
- Evidence {sid}-e01/e02; implementation 2 -> 3, concept 3 unchanged with added retrieval evidence. Debugging 2, judgment/transfer null, confidence low, proficiency functional unchanged. No full-domain mastery or transfer claim.
- Assistance: assessed concept/implementation H1; later general-defer clarification concept H4, not used to inflate independent evidence. Environment test fixture and runs supplied by instructor.
- Narrow conditional-cleanup recurrence across two tasks recorded MP-001 improving; learner corrected today's proposal after H1. No automatic score penalty.
- Review 2026-10-23-s04-r01 completed October 26, actual D3. Next related retrieval November 1 (D6, adjusted from D7 November 2 to Sunday availability). Older process/path reviews remain due; due flags recalculated.
- No learner frustration feedback. Difficulty stays 1 because independence improved but scope remains familiar. Next direction: short due process concept probe if budget allows, otherwise retain due reviews. No unfinished code or environment blocker.
- No commit, push or automation. Detailed notes: {notes}.
'''
checkpoint.write_text(body, encoding='utf-8')
header=raw[:raw.index('schema_version:')]
candidate=header+yaml.safe_dump(state, sort_keys=False, allow_unicode=True, width=110)
assert yaml.safe_load(candidate)==state
temp=path.with_suffix('.yaml.tmp'); temp.write_text(candidate,encoding='utf-8'); os.replace(temp,path)
history=root/'learner/session-history.md'
if f'### {cp}' not in history.read_text(encoding='utf-8'):
    with history.open('a',encoding='utf-8') as f:
        f.write('\n\n### '+cp+'\n\n'+body.split('\n\n',1)[1]+f'\nCheckpoint: learner/sessions/{sid}/checkpoint.md\n')
patterns=root/'learner/mistake-patterns.md'
if '### MP-001 ' not in patterns.read_text(encoding='utf-8'):
    with patterns.open('a',encoding='utf-8') as f:
        f.write('''\n\n### MP-001 — Kondisi penggantian error ikut membatasi cleanup

- Tanggal: 2026-10-26. Status: improving; pola terbatas pada dua task cleanup dengan mekanisme serupa.
- Observasi: conditional Close saat error kosong muncul pada patch diag-006 tanggal 23 Oktober (notes s04-o03) dan usulan awal review-001 tanggal 26 Oktober (notes s01-o01). Keduanya dapat melewatkan cleanup ketika operasi sebelumnya gagal.
- References: labs/diag-006/attempts/a001/notes.md — s04-o03/o04; labs/review-001/attempts/a001/notes.md — 2026-10-26-s01-o01/o02/o03.
- Kompetensi: os.files-and-descriptors, concept/implementation. Bukan diagnosis umum tentang kemampuan atau karakter learner.
- Evidence perbaikan: pada retrieval baru learner mengenali jalur terlewat dan menyusun repair setelah H1; sebelumnya membutuhkan bantuan H5. Patch sekarang lulus empat kasus termasuk kegagalan ganda. Kemiripan task membatasi generalisasi; belum resolved.
- Intervensi: minta trace kontrol terhadap kontrak cleanup sebelum patch; pisahkan reasoning menjalankan operasi dari memilih hasilnya. Hindari memberikan solusi sebelum attempt.
- Next check: retrieval berikut dengan bentuk resource/return berbeda, periksa apakah invariant cleanup dikenali tanpa prompt tambahan. Tidak ada penalti skor otomatis.
''')
assert yaml.safe_load(path.read_text(encoding='utf-8'))==state
assert cp in history.read_text(encoding='utf-8') and cp in checkpoint.read_text(encoding='utf-8')
validation='\n## Persistence validation\n\nPASS: map/state/lab YAML parse, competency IDs and unique evidence/review links valid; actual source matches snapshot, test exit 0 with four passes; unaffected assessment records preserved; state/history/checkpoint agree.\n'
if '## Persistence validation' not in checkpoint.read_text(encoding='utf-8'):
    with checkpoint.open('a',encoding='utf-8') as f: f.write(validation)
print('PASS: review checkpoint saved; implementation 2 -> 3; other scores unchanged; due flags refreshed.')
