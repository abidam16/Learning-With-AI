"""Append this completed bounded review once, preserving scores and learner source."""
from pathlib import Path
from copy import deepcopy
from datetime import datetime, timezone, timedelta
import json, re, sys
sys.path.insert(0, r'C:/Users/abid.mahdy/AppData/Local/Temp/learning-lab-yaml-validation')
import yaml

root = Path(__file__).resolve().parents[3]
sid = '2026-10-26-s03'
cpid = sid+'-cp01'
ref = f'learner/sessions/{sid}/checkpoint.md'
state_path = root/'learner/competency-state.yaml'
original = state_path.read_text(encoding='utf-8')
before = yaml.safe_load(original)
curriculum = yaml.safe_load((root/'curriculum/competency-map.yaml').read_text(encoding='utf-8'))
lab = yaml.safe_load((root/'labs/review-005/lab.yaml').read_text(encoding='utf-8'))
assert before['last_applied_checkpoint'] in ['2026-10-26-s02-cp01', cpid]
assert before['active_work'] is None
assert curriculum['curriculum_version']=='1.1.0'
assert set(before['competencies'])==set(curriculum['competencies'])
assert set(lab['primary_competency_ids']) <= set(curriculum['competencies'])
snapshot=root/'labs/review-005/attempts/a001/artifacts/s03-o04/main.go.txt'
assert (root/'labs/review-005/main.go').read_bytes()==snapshot.read_bytes()
verification=json.loads((snapshot.parent/'verification.json').read_text())
assert verification['build_exit']==0 and all(c['passed'] for c in verification['cases'])
assert verification['source_unchanged'] and verification['fixtures_unchanged']
now=datetime.now(timezone(timedelta(hours=7))).isoformat(timespec='seconds')

def append_once(path,marker,text):
    old=path.read_text(encoding='utf-8') if path.exists() else ''
    if marker not in old:
        path.write_text(old.rstrip()+'\n\n'+text.rstrip()+'\n',encoding='utf-8')

notes='labs/review-005/attempts/a001/notes.md'
append_once(root/notes, '## 2026-10-26-s03-o05 ', '''## 2026-10-26-s03-o05 — final relative-path prediction and closure

- Response recorded at 2026-10-26T13:59:55+07:00. Learner predicts jobs/B/orders.txt and `Impor: 2 pesanan [B-201, B-202]` for ../../lab.exe ../B/orders.txt from jobs/A. Explains that .. moves from A to jobs, then B/orders.txt identifies the input. Correct causal answer without a new mechanism hint.
- This last scenario is source-verified hypothetical reasoning, not an executed learner run or meaningful cross-context transfer. Existing six instructor runtime checks remain separate.
- Bounded review complete. Concept/debugging assistance maximum H1 for command/contract clarification; implementation instruction H1 contract only, no target API or patch supplied. Learner selected source inspection, diagnosis, experiment and core repair; instructor supplied fixtures, formatting, verification and administrative persistence.
- Concept 3, implementation 3 and debugging 2 retained. Add independent narrow path reasoning/diagnosis evidence; do not extrapolate this wrong-content fault to permission-denied, descriptor exhaustion, safe resource ownership, judgment or transfer. No score decrease; no new misconceptions or recurring patterns. MP-001 unchanged because cleanup pattern was not tested.
- Maintain difficulty 1; next comparable probe changes one failure condition, with learner choosing and interpreting an observation. No frustration/challenge self-report. Completion before time limit reflects achieved bounded objective, not a promise to fill all 60 minutes.
''')

state=deepcopy(before)
node=state['competencies']['os.files-and-descriptors']
exposure='October 23 path exercise included H5 observation/API help and final H4 launch-path clarification. Fresh retrieval three days later. Current H1 command/output clarification; learner voluntarily inspected source before initial hypothesis. No instructor target edit or remedy supplied.'
common=dict(session_id=sid,date='2026-10-26',lab_id='review-005',attempt_id='a001',competency_id='os.files-and-descriptors',task_variant=lab['task_variant'],assessment_status='assessed',artifact_or_observation=notes,max_hint='H1',prompt_context=exposure,correction_of=None)
entries=[
    dict(common,evidence_id=sid+'-e01',axis='concept',retest_of='2026-10-23-s01-e02',result='Correct source-informed account of executable-relative lookup, absolute-input prediction confirmed by learner transcript, and correct sibling-directory relative-input prediction after learner repair.',reasoning_check=dict(check_type='prediction',prompt='From jobs/A run ../../lab.exe ../B/orders.txt. Which exact input and IDs are selected, and why?',learner_response='.. goes from A to jobs, then B/orders.txt; output is Impor: 2 pesanan [B-201, B-202].',observation_reference=notes,interpretation='Supports retained independent path/CWD reasoning on changed input ownership contract; concept 3 remains.',limitations=['Final sibling-path prediction was not executed.','Same language and near path domain; not broad transfer, permissions or descriptor evidence.'])),
    dict(common,evidence_id=sid+'-e02',axis='debugging',retest_of='2026-10-23-s01-e03',result='Learner identifies faulty path anchor from source, proposes absolute-input comparison, predicts expected IDs and supplies matching B/A output with exit 0; authors repair which passes six instructor contract checks.',reasoning_check=dict(check_type='discriminating_experiment',prompt='State a hypothesis for identical DEMO-01 results and choose an experiment with a predicted outcome.',learner_response='Relative input is joined to executable directory; supplying absolute paths for B and A should read their respective order IDs. Supplied output confirms two B orders and three A orders, each exit 0.',observation_reference='labs/review-005/attempts/a001/artifacts/s03-o03-learner-output.txt',interpretation='Independent diagnosis of this path-selection fault at H1. Retain broader debugging 2: valid new evidence is narrowly wrong-content selection, while mapped failing-operation diagnosis (file-not-found/permission/descriptor exhaustion) was not independently investigated in this review.',limitations=['Learner ran absolute cases from lab root; relative baseline from operator folders was instructor-generated, so not a fully controlled same-CWD learner experiment.','Instructor selected and executed post-repair missing-file tests; those are artifact validation, not learner diagnosis.','No permission or resource-exhaustion diagnostic, meaningful transfer, or independent test-harness implementation.']))
]
for entry in entries:
    if not any(e['evidence_id']==entry['evidence_id'] for e in node['evidence']):
        node['evidence'].append(entry)
review=next(r for r in node['review_plan'] if r['review_id']=='2026-10-23-s01-r01')
if review['status']!='completed':
    review.update(status='completed',completed_at=now,result_evidence_ids=[e['evidence_id'] for e in entries])
if not any(r['review_id']==sid+'-r01' for r in node['review_plan']):
    node['review_plan'].append(dict(review_id=sid+'-r01',anchor_evidence_ids=[e['evidence_id'] for e in entries],anchor_date='2026-10-26',target_axes=['concept','debugging'],task_type='delayed_retrieval',target_date='2026-11-02',scheduled_date='2026-11-01',scheduling_reason='Successful narrow path retrieval at H1; D7 adapted to available Sunday D6. Coordinate with existing resource-result review in one bounded session without double-counting variants; include a genuine failing-input case and learner-selected evidence.',status='planned',completed_at=None,result_evidence_ids=[],schedule_history=[]))
node['last_assessed_on']='2026-10-26'
for c in state['competencies'].values():
    c['review_due']=any(r['status']=='planned' and r.get('scheduled_date') and r['scheduled_date']<='2026-10-26' for r in c['review_plan'])
state.update(updated_on='2026-10-26',last_session_id=sid,last_applied_checkpoint=cpid,active_work=None)
for cid,old in before['competencies'].items():
    new=state['competencies'][cid]
    for key in ['scores','confidence','proficiency','weighted_score']:
        assert old[key]==new[key]
    assert new['evidence'][:len(old['evidence'])]==old['evidence']
    assert new['assessment_history']==old['assessment_history']
    if cid!='os.files-and-descriptors': assert old==new
evidence_ids=[e['evidence_id'] for c in state['competencies'].values() for e in c['evidence']]
assert len(evidence_ids)==len(set(evidence_ids))
review_ids=[r['review_id'] for c in state['competencies'].values() for r in c['review_plan']]
assert len(review_ids)==len(set(review_ids))
for c in state['competencies'].values():
    for r in c['review_plan']:
        assert set(r['anchor_evidence_ids']+r['result_evidence_ids'])<=set(evidence_ids)
    for e in c['evidence']:
        assert e['competency_id'] in curriculum['competencies']
        for relative in re.findall(r'(?:labs|learner)/[A-Za-z0-9_./-]+',e['artifact_or_observation']):
            assert (root/relative.rstrip('.')).exists(), relative
for entry in entries:
    assert entry['retest_of'] in evidence_ids
    assert (root/entry['reasoning_check']['observation_reference']).is_file()

body=f'''- Status **completed** for session {sid}, review-005 / operator-input-selection-v1 / a001; saved {now}. First captured time 13:20:44 WIB; closing began 13:59:55. User budget 60 minutes, conservative limit 14:20, reserve 14:15. Objective completed early; no additional task added to fill budget. Wall time includes setup/interactions; active learning not measured. No reported breaks.
- Learner requested missing command details (task-presentation clarification H1), selected source inspection, correctly explained the wrong input anchor, proposed absolute-input experiment and supplied predicted exact B/A outputs with exit 0. Independently authored cwd-based repair and correctly predicted sibling-folder relative lookup afterward.
- Instructor build and six runtime checks PASS: relative A/B, absolute A from B and B from A, missing relative without sample fallback, missing absolute. Learner source and fixtures unchanged during verification. Final sibling-path answer is hypothetical reasoning, not a reported run. Artifacts: labs/review-005/attempts/a001/artifacts/s03-o03-learner-output.txt and s03-o04/ (main.go.txt, build.txt, verification.json).
- Evidence {sid}-e01/e02 appended. All scores/confidence/proficiency unchanged: files C3/I3/D2/J-null/T-null, processes C2/I3/D2/J-null/T-null; both low confidence and functional. Independent narrow path reasoning and diagnosis strengthened; mapped failing-operation diagnosis, permissions, descriptors, judgment and transfer not independently assessed here. Preserve earlier implementation evidence; this path patch alone does not assess full resource-lifecycle outcome. No new numerical assessment entry because scores did not change.
- Assistance: concept/debugging H1 command/output/contract clarification; learner patch had H1 contract restatement only, no API or solution supplied. Instructor-owned setup, tests and persistence recorded separately. Source inspection was learner-selected; initial response is not a blind pre-inspection hypothesis. No new misconception or recurring pattern; MP-001 unchanged.
- File-path review 2026-10-23-s01-r01 completed, actual D3. Next related concept/debugging retrieval November 1 (D6 adapted from D7 November 2), coordinated with existing resource-result review. Process implementation review 2026-10-20-s02-r01 remains due; October 31 process reviews retained. Next direction: fresh small process implementation review, or path failing-input variant on planned retrieval date.
- Calibration maintain difficulty 1; reasoning and patch were independent with neutral clarification. Next path probe changes one failure condition and asks learner to select evidence. Learner feedback: time budget only; no emotional inference. No unfinished code or environment blocker; active_work null.
- References: {notes}; learner/sessions/{sid}/startup.md. No target edits by instructor, memory update, automation, commit or push. Source retains unused os.Executable call and unconditional Getwd; unavailable-CWD/Executable-error behavior was not injected and is outside the verified normal Windows environment.
'''
checkpoint=root/ref
if not checkpoint.exists(): checkpoint.write_text(f'# Checkpoint {cpid}\n\n'+body,encoding='utf-8')
history=root/'learner/session-history.md'
append_once(history,f'### {cpid}',f'### {cpid}\n\n'+body+'\nCheckpoint: '+ref)
header=original[:original.index('schema_version:')]
candidate=header+yaml.safe_dump(state,sort_keys=False,allow_unicode=True,width=110)
assert yaml.safe_load(candidate)==state
state_path.write_text(candidate,encoding='utf-8')
assert yaml.safe_load(state_path.read_text(encoding='utf-8'))==state
assert history.read_text(encoding='utf-8').count(f'### {cpid}')==1
assert cpid in checkpoint.read_text(encoding='utf-8')
assert (root/'labs/review-005/main.go').read_bytes()==snapshot.read_bytes()
validation='PASS: map/state/lab YAML parse; 38 competency IDs match; evidence/review IDs unique and references resolve; prior evidence and assessments preserved; numerical scores/confidence/proficiency unchanged; other competencies unchanged; source matches verified snapshot; state/history/checkpoint agree, active_work null.'
append_once(checkpoint,'## Final validation','## Final validation\n\n'+validation)
append_once(root/f'learner/sessions/{sid}/startup.md','## Completed at checkpoint',f'## Completed at checkpoint\n\n{cpid}; see {ref}. Review completed; no pending prediction or patch.')
print(validation)
print('Saved: '+ref)
