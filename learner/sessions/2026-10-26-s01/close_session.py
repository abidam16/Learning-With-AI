from pathlib import Path
from copy import deepcopy
from datetime import datetime, timezone, timedelta
import os, sys, tempfile
sys.path.insert(0, str(Path(tempfile.gettempdir())/'learning-lab-yaml-validation'))
import yaml
root=Path(__file__).resolve().parents[3]
sid='2026-10-26-s01'; cp=sid+'-cp02'; date='2026-10-26'
stamp=datetime.now(timezone(timedelta(hours=7))).isoformat(timespec='seconds')
p=root/'learner/competency-state.yaml'; raw=p.read_text(encoding='utf-8'); old=yaml.safe_load(raw); state=deepcopy(old)
mapping=yaml.safe_load((root/'curriculum/competency-map.yaml').read_text(encoding='utf-8'))
lab=yaml.safe_load((root/'labs/review-002/lab.yaml').read_text(encoding='utf-8'))
assert state['curriculum_version']==mapping['curriculum_version']==lab['curriculum_version']=='1.1.0'
assert set(state['competencies'])==set(mapping['competencies'])
notes='labs/review-002/attempts/a001/notes.md'; art='labs/review-002/attempts/a001/artifacts/'
assert (root/'labs/review-002/main.go').read_bytes()==(root/(art+'starter-main.go.txt')).read_bytes()
assert (root/(art+'baseline.txt')).read_text().splitlines()==['task: rejected','runner: result 9','runner: cleanup']
assert (root/(art+'exit-code.txt')).read_text().strip()=='0'
out=root/(art+'s01-o02-learner-output.txt')
out.write_text('Learner-reported output, not a captured terminal session:\ntask: rejected\nrunner: result 9\nrunner: cleanup\n$LASTEXITCODE = 0\nLearner observation: ternyata task: cleanup tidak muncul\n',encoding='utf-8')
node=state['competencies']['os.processes']; eid=sid+'-e03'
if not any(e['evidence_id']==eid for e in node['evidence']):
    node['evidence'].append(dict(evidence_id=eid, session_id=sid, date=date, lab_id='review-002', attempt_id='a001', competency_id='os.processes', axis='concept', task_variant=lab['task_variant'], assessment_status='assessed', max_hint='H1', artifact_or_observation=notes+' — o01/o02; '+art+'s01-o02-learner-output.txt; '+art+'baseline.txt', result='Learner correctly predicts child rejection, helper return 9, parent cleanup and shell status 0, but incorrectly predicts child deferred cleanup after os.Exit(5). After neutral execution comparison, reports actual three-line output and notices missing child cleanup; does not independently explain the exit/defer distinction before teaching.', prompt_context='H0 prediction after prior process teaching and same-session ordinary-defer explanation. H1 neutral compare-to-run prompt. Closing os.Exit/defer explanation H4 follows these observations and is not evidence of learner understanding.', reasoning_check=dict(check_type='delayed_retrieval',prompt='Predict ordered output and LASTEXITCODE for lab.exe without arguments, then compare with execution.',learner_response='Predicts task: rejected, task: cleanup, runner: result 9, runner: cleanup and status 0. Explains two processes and function return correctly but says os.Exit ends the function and runs defer. Reports three actual lines/status 0 and identifies absent task cleanup.',observation_reference=notes+' — o01/o02',interpretation='Mixed narrow retention: process/return/status distinction retained, immediate-process-exit cleanup not yet understood independently. Maintain concept 2; teaching uptake needs fresh assessment.',limitations=['Reported learner execution, matched instructor baseline.','No independent explanation after discrepancy; H4 teaching followed.','No signals, external crash/kill investigation, implementation or broad transfer tested.']), retest_of='2026-10-20-s01-e03', correction_of=None))
    node['assessment_history'].append(dict(assessment_id=sid+'-as02',session_id=sid,checkpoint_id=cp,date=date,evidence_ids=[eid],before={'scores':{'concept':2}},after={'scores':{'concept':2}},rationale='Preserve concept 2: correct child/parent/function-return reasoning but incorrect os.Exit/defer prediction. One bounded gap does not justify reducing the whole axis; H4 explanation is not demonstrated independent understanding. All other fields unchanged.'))
    node['last_assessed_on']=date
    review=next(r for r in node['review_plan'] if r['review_id']=='2026-10-20-s01-r01')
    review.update(status='completed',completed_at=stamp,result_evidence_ids=[eid])
    node['review_plan'].append(dict(review_id=sid+'-r02',anchor_evidence_ids=[eid],anchor_date=date,target_axes=['concept'],task_type='delayed_retrieval',target_date='2026-10-28',scheduled_date='2026-10-31',scheduling_reason='D2 after mixed retrieval/H4 exit-defer teaching moved to next available Saturday, actual planned D5. Fresh bounded ordinary-return versus process-exit variant; no claim of successful independent cleanup retention today.',status='planned',completed_at=None,result_evidence_ids=[],schedule_history=[]))
for n in state['competencies'].values():
    n['review_due']=any(r['status']=='planned' and r.get('scheduled_date') and r['scheduled_date']<=date for r in n['review_plan'])
state.update(updated_on=date,last_session_id=sid,last_applied_checkpoint=cp,active_work=None)
for k in state['competencies']:
    if k!='os.processes': assert state['competencies'][k]==old['competencies'][k]
assert node['scores']==old['competencies']['os.processes']['scores']
assert state['competencies']['os.files-and-descriptors']['scores']['implementation']==3
es=[e['evidence_id'] for n in state['competencies'].values() for e in n['evidence']]; assert len(es)==len(set(es))
rs=[r['review_id'] for n in state['competencies'].values() for r in n['review_plan']]; assert len(rs)==len(set(rs))
for k,n in state['competencies'].items():
    assert all(v is None or type(v) is int and 0<=v<=4 for v in n['scores'].values())
    for e in n['evidence']: assert e['competency_id']==k
    for r in n['review_plan']: assert all(x in es for x in r['anchor_evidence_ids']+r['result_evidence_ids'])
for f in [notes,art+'baseline.txt',art+'s01-o02-learner-output.txt','learner/sessions/'+sid+'/checkpoint.md','labs/review-001/attempts/a001/artifacts/s01-o03/tests.txt']:
    assert (root/f).is_file()
body=f'''# Checkpoint {cp}

- Status **completed** for session {sid}, saved {stamp}. Initial budget 45 minutes; nine-minute bathroom break 06:44–06:53 reported by learner and separated from learning time. Closing began 07:03:44 WIB, near break-adjusted conservative 07:04 boundary. Active work time not measured.
- Review-001 completed at cp01: learner-produced cleanup/error-precedence patch passes four controlled cases with Close exactly once; prediction/revision/implementation at H0/H1. Implementation 2 -> 3, concept 3 unchanged. Evidence {sid}-e01/e02. General defer terminology clarified afterward at H4, uptake not assessed.
- Review-002 / runner-task-completion-v2 / a001: learner correctly distinguishes child exit, helper return 9 and original shell status 0, but predicts child cleanup after os.Exit. Reports actual missing child cleanup. Instructor then explains os.Exit skips deferred calls (H4); no later learner explanation observed. Evidence {sid}-e03. Process concept remains 2; no other process score change.
- Assessment scope: file concept 3/implementation 3/debugging 2/judgment null/transfer null; process concept 2/implementation 3/debugging 2/judgment null/transfer null. Both confidence low and proficiency functional, unchanged. No mastery, meaningful transfer or new debugging/test-design claim.
- Assistance: review-001 independent assessed portions concept/implementation H1, later general-defer clarification concept H4. Review-002 prediction H0, comparison H1, final os.Exit explanation concept H4. Infrastructure/tests supplied by instructor; no instructor learner-source edits.
- MP-001 improving records conditional-cleanup recurrence across two task variants and today's self-correction after H1; do not call resolved. New os.Exit misconception is a session observation, not an established recurring pattern.
- Next reviews: October 31 exit/defer concept (D5 adapted from D2 October 28); November 1 resource-result concept/implementation (D6 adapted from D7 November 2). Existing process implementation/debugging and file-path reviews remain due. These are file review plans, not external reminders.
- Difficulty remains 1; narrower exit/defer check next because retained process-boundary reasoning coexists with this specific gap. Learner feedback reports a break only; no inferred frustration. No unfinished code or blocker; active_work null.
- Recommended next step: a short fresh prediction contrasting ordinary return with process exit, then prioritize the remaining due reviews within the next time budget. Do not reuse today's taught answer as independent evidence.
- References: labs/review-001/attempts/a001/notes.md and artifacts/s01-o03/; {notes}; {art}starter-main.go.txt, baseline.txt, s01-o02-learner-output.txt. No commit, push or automation.
'''
checkpoint=root/f'learner/sessions/{sid}/checkpoint-cp02.md'; checkpoint.write_text(body,encoding='utf-8')
candidate=raw[:raw.index('schema_version:')]+yaml.safe_dump(state,sort_keys=False,allow_unicode=True,width=110)
assert yaml.safe_load(candidate)==state
temp=p.with_suffix('.yaml.tmp');temp.write_text(candidate,encoding='utf-8');os.replace(temp,p)
h=root/'learner/session-history.md'
if f'### {cp}' not in h.read_text(encoding='utf-8'):
    with h.open('a',encoding='utf-8') as f: f.write('\n\n### '+cp+'\n\n'+body.split('\n\n',1)[1]+f'\nCheckpoint: learner/sessions/{sid}/checkpoint-cp02.md\n')
assert yaml.safe_load(p.read_text(encoding='utf-8'))==state and cp in h.read_text(encoding='utf-8')
assert (root/'labs/review-001/save.go').read_bytes()==(root/'labs/review-001/attempts/a001/artifacts/s01-o03/save.go.txt').read_bytes()
with checkpoint.open('a',encoding='utf-8') as f:f.write('\n## Final validation\n\nPASS: map/state/both lab YAML parse; competency IDs, unique evidence/review IDs and references valid; review-001 learner source still matches verified patch; review-002 source matches baseline; unaffected assessments preserved; state/history/checkpoint agree, active_work cleared.\n')
print('PASS: completed session checkpoint cp02 saved; process scores unchanged; prior implementation increase preserved; reviews and history consistent.')
