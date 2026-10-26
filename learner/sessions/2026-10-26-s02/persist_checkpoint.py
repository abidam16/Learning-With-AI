"""Persist this session once; preserve historical observations and learner code."""
from pathlib import Path
from copy import deepcopy
from datetime import datetime, timezone, timedelta
import json
import re
import sys
sys.path.insert(0, r'C:/Users/abid.mahdy/AppData/Local/Temp/learning-lab-yaml-validation')
import yaml

root = Path(__file__).resolve().parents[3]
sid = '2026-10-26-s02'
cpid = sid + '-cp01'
ref = f'learner/sessions/{sid}/checkpoint.md'
state_path = root / 'learner/competency-state.yaml'
original = state_path.read_text(encoding='utf-8')
before = yaml.safe_load(original)
curriculum = yaml.safe_load((root / 'curriculum/competency-map.yaml').read_text(encoding='utf-8'))
assert curriculum['curriculum_version'] == '1.1.0'
assert set(before['competencies']) == set(curriculum['competencies'])
now = datetime.now(timezone(timedelta(hours=7))).isoformat(timespec='seconds')
for lab_id in ['review-003', 'review-004']:
    lab = yaml.safe_load((root / f'labs/{lab_id}/lab.yaml').read_text(encoding='utf-8'))
    assert set(lab['primary_competency_ids']) <= set(curriculum['competencies'])
    assert (root / f'labs/{lab_id}/main.go').read_bytes() == (root / f'labs/{lab_id}/attempts/a001/artifacts/starter-main.go.txt').read_bytes()

def append_once(path, marker, text):
    existing = path.read_text(encoding='utf-8') if path.exists() else ''
    if marker not in existing:
        path.write_text(existing.rstrip() + '\n\n' + text.rstrip() + '\n', encoding='utf-8')

notes4 = root / 'labs/review-004/attempts/a001/notes.md'
append_once(notes4, '## 2026-10-26-s02-o03 ', '''## 2026-10-26-s02-o03 — final continuation check

- Closing began 2026-10-26T10:24:43+07:00, within conservative 10:25 boundary; later persistence time is administrative, not extra learner work.
- Actual learner response: runner continues and retains default runner_exit_code 1 because no remaining line replaces it; LASTEXITCODE 1. Correctly retracts initial immediate-crash claim and traces handled failure through final return. Exact terminal summary was not supplied by learner; instructor supplies it only after this response.
- Prompt H1 (neutral final trace), not an API explanation. Learner generated corrected Start/Wait and handled-error reasoning. Source and fixture inspected voluntarily; raw log output was not pasted and direct execution of log commands was not confirmed. Preserve this evidence boundary.
- Bounded review completed. Observed gap was launch-versus-completion attribution and treating a returned error as immediate crash; both revised within the task. Do not establish a recurring pattern from these observations alone.
- Assessment: retain process debugging 2 and concept 2; positive source-supported causal correction at H0/H1, but learner's selection of exact runtime causal evidence and its limitations remains insufficiently demonstrated for broader promotion. Implementation 3 unchanged; judgment/transfer unobserved. Not a penalty for initial wrong hypotheses or time.
- Calibration maintain difficulty 1; next runtime review requests one decisive log record with source/PID context and an alternative it excludes. Next session prioritizes still-due implementation/path reviews. No learner frustration feedback.
''')

body = f'''- Status **completed**, session {sid}; saved {now}. Closing began 10:24:43 WIB near conservative 10:25 limit. User authorized 60 minutes. First recorded setup time 09:28:36, earlier preparation unmeasured; wall-clock interaction is not measured active learning time. No reported breaks.
- review-003 / command-completion-v3 / a001 completed: correct finish/stop output and status predictions, learner-reported execution matching instructor baseline, and causal explanation of missing cleanup after explicit exit. No source changes. Same-day earlier H4 exposure limits this to uptake on changed call structure, not delayed retention or transfer. Current prompt/comparison maximum concept H1.
- review-004 / order-job-investigation-v2 / a001 completed as a bounded debugging review: learner independently inspected source/fixture and identified malformed JSON for K and missing executable for L. Initially confused child exit with Start failure and expected runner crash on missing executable. After H1 comparison prompt, independently revised to K Start success/Wait nonzero and L handled Start failure; final explanation correctly retains runner exit 1. Source-supported reasoning is valid; no raw learner log output or confirmed log-command execution was supplied.
- Instructor verified build and both cases and archived baseline. At closing, existing K log shows started PID 29408 then Wait exit 4 for that PID; L log shows missing-path Start failure. These are instructor-observed records, not learner-generated runtime evidence. No learner-source edits or implementation assessment.
- Evidence {sid}-e01 (concept follow-up) and {sid}-e02 (debugging retrieval) appended. All numerical scores, confidence and proficiency unchanged. Process C2/I3/D2/J-null/T-null; files C3/I3/D2/J-null/T-null; both low confidence and functional. Evidence supports correction but not broad independence or mastery; no score decrease for initial hypotheses or time.
- Assistance: review-003 concept H1 in this probe, known earlier same-day H4 teaching; review-004 debugging H1 and final concept trace H1, with learner-selected source/fixture exposure. Instructor supplied fixtures, instrumentation and baseline. Implementation/judgment/transfer not assessed this session.
- No new recurring mistake pattern established; MP-001 unchanged. Learner feedback: 60-minute availability only, no inferred emotion. Difficulty remains 1. Narrow next runtime check to concrete evidence selection and limits, without adding another difficulty dimension.
- Completed overdue debugging review 2026-10-22-s04-r01 (actual D4) with mixed initial prediction and successful source-based correction; not a claim of complete independent runtime diagnosis. Added {sid}-r01 for October 31 (D5, adapted from D2 October 28) to verify fresh runtime evidence selection. Existing October 31 exit/defer review and November 1 resource-result review remain planned; coordinate scope without double-counting one task.
- Process implementation review 2026-10-20-s02-r01 and file-path review 2026-10-23-s01-r01 remain due. Recommended next session: a fresh small process implementation or file-path diagnostic chosen from these due reviews, with hypothesis/prediction before inspecting solution-bearing artifacts; preserve learner choice to inspect source and record exposure.
- No unfinished code or environment blocker; active_work null. No automation, commit or push. References: learner/sessions/{sid}/startup.md; labs/review-003/attempts/a001/notes.md and artifacts/baseline.txt; labs/review-004/attempts/a001/notes.md and artifacts/baseline-reports/.
'''
checkpoint = root / ref
if not checkpoint.exists():
    checkpoint.write_text(f'# Checkpoint {cpid}\n\n' + body, encoding='utf-8')
history = root / 'learner/session-history.md'
append_once(history, f'### {cpid}', f'### {cpid}\n\n' + body + '\nCheckpoint: ' + ref)

state = deepcopy(before)
process = state['competencies']['os.processes']
def evidence(eid, lab, axis, variant, result, response, interpretation, hint, exposure, limitations, retest):
    return dict(evidence_id=eid, session_id=sid, date='2026-10-26', lab_id=lab, attempt_id='a001', competency_id='os.processes', axis=axis, task_variant=variant, assessment_status='assessed', artifact_or_observation=f'labs/{lab}/attempts/a001/notes.md', result=result, max_hint=hint, prompt_context=exposure, reasoning_check=dict(check_type='prediction' if lab == 'review-003' else 'discriminating_experiment', prompt='Predict finish/stop ordered output and shell status, then compare and explain.' if lab == 'review-003' else 'Choose evidence and predict distinguishing observations; compare with logs and trace whether the runner continues after Start failure.', learner_response=response, observation_reference=f'labs/{lab}/attempts/a001/notes.md', interpretation=interpretation, limitations=limitations), retest_of=retest, correction_of=None)
entries = [
evidence(sid+'-e01', 'review-003', 'concept', 'command-completion-v3',
    'Correctly predicts both outputs/status 6, reports matching execution and explains immediate exit prevents run cleanup in stop mode.',
    'finish: main begin, run begin, run cleanup, then outer os.Exit(6). stop: main begin, run begin, immediate os.Exit(6). Reports matching output; explains stop skips run cleanup.',
    'Correct uptake on changed nested-call shape; retain concept 2 because same-day H4 exposure and broader lifecycle uncertainty remain.', 'H1',
    'Initial prediction H0 and comparison H1; earlier same-day review-002 H4 exit/defer teaching. No new solution hint before response.',
    ['Same-day teaching follow-up, not delayed retention or meaningful transfer.', 'Learner-reported run; baseline independently verified.', 'No implementation or debugging design assessed.'], '2026-10-26-s01-e03'),
evidence(sid+'-e02', 'review-004', 'debugging', 'order-job-investigation-v2',
    'Independently finds source/fixture causal candidates, predicts incorrect Start/crash paths, then corrects Start/Wait attribution and handled-error continuation after neutral comparison prompts.',
    'Initially K malformed JSON causes child exit 4 then Start failure; L missing executable crashes runner. Revises K to Start success and Wait exit 4, L to handled Start failure; finally explains L continues with default runner status 1.',
    'Valid source-supported hypothesis revision at H0/H1. Retain debugging 2: specific decisive runtime records and evidence limits were not supplied by learner, so do not infer full independent runtime diagnosis.', 'H1',
    'Learner voluntarily read source and malformed fixture before log comparison. Instructor did not name causes or explain Start/Wait before revised response. Prior guided process diagnosis October 22.',
    ['No raw learner log output or confirmed log-command execution; explanation matches instructor baseline.', 'No source repair, instrumentation implementation, signals, crash/kill comparison or transfer.', 'Initial hypotheses remain preserved; no automatic penalty.'], '2026-10-22-s04-e02')
]
for entry in entries:
    if not any(e['evidence_id'] == entry['evidence_id'] for e in process['evidence']):
        process['evidence'].append(entry)
assessment_id = sid+'-as01'
if not any(a['assessment_id'] == assessment_id for a in process['assessment_history']):
    process['assessment_history'].append(dict(assessment_id=assessment_id, session_id=sid, checkpoint_id=cpid, date='2026-10-26', evidence_ids=[e['evidence_id'] for e in entries], before={'scores': {'concept': 2, 'debugging': 2}}, after={'scores': {'concept': 2, 'debugging': 2}}, rationale='Preserve scores: same-day exit/defer uptake and source-supported lifecycle corrections are positive narrow evidence. Learner-selected decisive runtime records/limitations not yet demonstrated, and implementation/judgment/transfer unobserved. No score penalty for initial hypotheses or time; maintain low confidence/functional proficiency.'))
for review in process['review_plan']:
    if review['review_id'] == '2026-10-22-s04-r01' and review['status'] != 'completed':
        review.update(status='completed', completed_at=now, result_evidence_ids=[sid+'-e02'])
if not any(r['review_id'] == sid+'-r01' for r in process['review_plan']):
    process['review_plan'].append(dict(review_id=sid+'-r01', anchor_evidence_ids=[sid+'-e02'], anchor_date='2026-10-26', target_axes=['debugging'], task_type='delayed_retrieval', target_date='2026-10-28', scheduled_date='2026-10-31', scheduling_reason='Fresh runtime evidence-selection check after mixed initial prediction and successful H1 source-supported correction. D2 adapted to Saturday availability D5. Coordinate with existing concept review without double-counting one variant.', status='planned', completed_at=None, result_evidence_ids=[], schedule_history=[]))
process['last_assessed_on'] = '2026-10-26'
for c in state['competencies'].values():
    c['review_due'] = any(r['status'] == 'planned' and r.get('scheduled_date') and r['scheduled_date'] <= '2026-10-26' for r in c['review_plan'])
state.update(last_session_id=sid, last_applied_checkpoint=cpid, updated_on='2026-10-26', active_work=None)
for cid, old in before['competencies'].items():
    new = state['competencies'][cid]
    for key in ['scores', 'confidence', 'proficiency', 'weighted_score']:
        assert old[key] == new[key], (cid, key)
    assert new['evidence'][:len(old['evidence'])] == old['evidence']
    assert new['assessment_history'][:len(old['assessment_history'])] == old['assessment_history']
    if cid != 'os.processes':
        assert old == new, cid
all_evidence = [e for c in state['competencies'].values() for e in c['evidence']]
ids = [e['evidence_id'] for e in all_evidence]
assert len(ids) == len(set(ids))
review_ids = [r['review_id'] for c in state['competencies'].values() for r in c['review_plan']]
assert len(review_ids) == len(set(review_ids))
for entry in entries:
    assert entry['competency_id'] in curriculum['competencies']
    assert (root / entry['artifact_or_observation']).is_file()
    assert (root / entry['reasoning_check']['observation_reference']).is_file()
    assert entry['retest_of'] in ids
for c in state['competencies'].values():
    for r in c['review_plan']:
        assert set(r['anchor_evidence_ids'] + r['result_evidence_ids']) <= set(ids)
    for e in c['evidence']:
        for relative in re.findall(r'(?:labs|learner)/[A-Za-z0-9_./-]+', e['artifact_or_observation']):
            assert (root / relative.rstrip('.')).exists(), relative
for lab in ['review-003', 'review-004']:
    assert (root / f'labs/{lab}/attempts/a001/notes.md').exists()
assert (root / 'labs/review-003/attempts/a001/artifacts/baseline.txt').exists()
for case in ['K', 'L']:
    p = root / f'labs/review-004/attempts/a001/artifacts/baseline-reports/{case}'
    for name in ['supervisor.log', 'worker.stdout.log', 'worker.stderr.log', 'request.json', 'result.json']:
        assert (p / name).exists()
    result = json.loads((p / 'result.json').read_text())
    assert result['runner_exit_code'] == 1
    assert result['started'] == (case == 'K')
    assert result['worker_exit_code'] == (4 if case == 'K' else None)
header = original[:original.index('schema_version:')]
candidate = header + yaml.safe_dump(state, sort_keys=False, allow_unicode=True, width=110)
assert yaml.safe_load(candidate) == state
state_path.write_text(candidate, encoding='utf-8')
assert yaml.safe_load(state_path.read_text(encoding='utf-8')) == state
assert history.read_text(encoding='utf-8').count(f'### {cpid}') == 1
assert cpid in checkpoint.read_text(encoding='utf-8')
assert state['active_work'] is None and state['last_applied_checkpoint'] == cpid
validation = 'PASS: map/state/both lab YAML parse; 38 competency IDs and unique evidence/review IDs valid; evidence artifact paths and review anchors resolve; prior evidence/assessments preserved; scores/confidence/proficiency and other competencies unchanged; source snapshots match; baseline cases correct; state/history/checkpoint agree, active_work null.'
append_once(checkpoint, '## Final validation', '## Final validation\n\n' + validation)
print(validation)
print('Saved: ' + ref)
