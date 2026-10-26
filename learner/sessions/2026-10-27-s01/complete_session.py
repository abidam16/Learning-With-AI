from pathlib import Path
from copy import deepcopy
from datetime import datetime, timezone, timedelta
import json
import os
import sys

sys.dont_write_bytecode = True
root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(root / '.tools/python-support'))
import yaml

sid = '2026-10-27-s01'
cp = sid + '-cp01'
day = '2026-10-27'
stamp = datetime.now(timezone(timedelta(hours=7))).isoformat(timespec='seconds')
notesref = 'labs/review-006/attempts/a001/notes.md'
artref = 'labs/review-006/attempts/a001/artifacts/s01-o02'
cpref = f'learner/sessions/{sid}/checkpoint.md'
statepath = root / 'learner/competency-state.yaml'
raw = statepath.read_text(encoding='utf-8')
before = yaml.safe_load(raw)
state = deepcopy(before)
mapping = yaml.safe_load((root / 'curriculum/competency-map.yaml').read_text(encoding='utf-8'))
lab = yaml.safe_load((root / 'labs/review-006/lab.yaml').read_text(encoding='utf-8'))
assert mapping['curriculum_version'] == state['curriculum_version'] == lab['curriculum_version'] == '1.1.0'
assert set(state['competencies']) == set(mapping['competencies'])
assert state['last_applied_checkpoint'] in ['2026-10-26-s03-cp01', cp]
verification = json.loads((root / artref / 'verification.json').read_text(encoding='utf-8'))
assert verification['build_exit'] == 0
assert len(verification['results']) == 4 and all(r['passed'] for r in verification['results'])
for name in ['batch.go', 'main.go', 'fixture.go']:
    assert (root / 'labs/review-006' / name).read_bytes() == (root / artref / (name + '.txt')).read_bytes()

def append_once(path, marker, content):
    text = path.read_text(encoding='utf-8') if path.exists() else ''
    if marker not in text:
        with path.open('a', encoding='utf-8') as f:
            f.write('\n\n' + content.rstrip() + '\n')

response = ('Walaupun prepare: done muncul, prepare masih bekerja 5 detik sampai exit 7; '
            'publish belum berjalan. Exit nonzero menghasilkan error dari prepare.Run(), '
            'cabang error mencetak prepare: gagal dan return 1. Main memakai hasil itu '
            'untuk os.Exit(1), sehingga publish tidak berjalan dan status batch 1.')
prompt = ('Prepare prints prepare: done, continues working for five seconds, then exits 7. '
          'With current code, does publish run, when does batch return, and what is its final status? Explain.')
append_once(root / notesref, '## 2026-10-27-s01-o03', f'''## 2026-10-27-s01-o03 — Final causal prediction
- Captured at 2026-10-27T06:06:14+07:00, before any instructor explanation of this scenario.
- Prompt: {prompt}
- Actual learner response (faithful summary): {response}
- Interpretation: independently distinguishes printed progress from termination, waits for child completion, follows nonzero child result through early return and parent exit mapping. Correct outcome and causal sequence; H0 concept/implementation throughout assessed work.
- Limitations: five-second/status-7 variant is hypothetical and was not executed. Four original scenarios were executed and independently verified. No signal/shutdown, PID/environment, judgment, debugging investigation or meaningful transfer assessment.
- Decision: implementation 3 maintained with successful delayed retrieval (D7 from October 20 anchor; D6 from October 21 independent patch); concept 2 maintained with strengthened narrow outcome reasoning. Broader concept independence not established by this probe. Confidence low and functional unchanged. No new misconception or recurring pattern; MP-001 not tested.
- Calibration: maintain difficulty 1; consistent independent reasoning and patch. End bounded objective early; no new task to fill unused budget. User only reported time availability; no frustration/boredom inference.
''')

e1, e2 = sid + '-e01', sid + '-e02'
node = state['competencies']['os.processes']
common = dict(session_id=sid, date=day, lab_id='review-006', attempt_id='a001',
              competency_id='os.processes', task_variant=lab['task_variant'],
              assessment_status='assessed', max_hint='H0', correction_of=None)
reasoning = dict(check_type='causal_explanation', prompt=prompt, learner_response=response,
                 observation_reference=notesref + ' — o03',
                 interpretation='Correct independent causal chain: printed progress does not complete a child; Run result gates publication and maps child failure to batch status 1.',
                 limitations=['Five-second counterfactual discussed only, not executed.',
                              'Known prior process instruction; narrow familiar Go result-handling scope.',
                              'No signal handling, controlled shutdown or meaningful transfer observed.'])
if not any(e['evidence_id'] == e1 for e in node['evidence']):
    assert not any(e['evidence_id'] == e2 for e in node['evidence'])
    node['evidence'].extend([
        dict(common, evidence_id=e1, axis='implementation', retest_of='2026-10-20-s02-e02',
             artifact_or_observation=f'{artref}/batch.go.txt; {artref}/verification.json; {notesref} — o01/o02/o03',
             result='Learner independently authors sequential Run checks with immediate failure returns and final success only after both stages. Build and four real-process contract cases PASS: success, prepare rejection, silent publish failure, absent prepare executable. Correct final causal prediction.',
             prompt_context='Directed business contract; command construction/stream wiring, fixtures and checker instructor-provided. Learner independently chose Run and wrote controller. October 20 H4 and October 21 H0 prior implementation, October 26 concept/debugging exposure. No new API/solution hint or instructor source edit.',
             reasoning_check=deepcopy(reasoning)),
        dict(common, evidence_id=e2, axis='concept', retest_of=None,
             artifact_or_observation=notesref + ' — o01/o03',
             result='Learner independently explains completion-sensitive sequencing, nonzero child failure, skipped publication and explicit child-7 to parent-1 mapping despite misleading progress text.',
             prompt_context='H0 initial approach and final counterfactual after learner patch; prior-day process instruction known. Same task as implementation record, not a second independent task.',
             reasoning_check=deepcopy(reasoning))])
    node['last_assessed_on'] = day
    review = next(r for r in node['review_plan'] if r['review_id'] == '2026-10-20-s02-r01')
    assert review['status'] == 'planned'
    review.update(status='completed', completed_at=stamp, result_evidence_ids=[e1, e2])
    node['review_plan'].append(dict(review_id=sid+'-r01', anchor_evidence_ids=[e1,e2], anchor_date=day,
        target_axes=['implementation','concept'], task_type='delayed_retrieval',
        target_date='2026-11-03', scheduled_date='2026-11-07',
        scheduling_reason='Successful independent narrow retrieval. D7 target November 3 moved to first weekend on/after target, Saturday November 7 (D11), using stated weekend availability. Existing October 31 process concept/debugging reviews retained; avoid repeating the same familiar implementation immediately.',
        status='planned', completed_at=None, result_evidence_ids=[], schedule_history=[]))

for item in state['competencies'].values():
    item['review_due'] = any(r['status'] == 'planned' and r.get('scheduled_date') and r['scheduled_date'] <= day for r in item['review_plan'])
state.update(updated_on=day, last_session_id=sid, last_applied_checkpoint=cp, active_work=None)
for key, oldnode in before['competencies'].items():
    newnode = state['competencies'][key]
    for field in ['scores','confidence','proficiency','weighted_score','assessment_history']:
        assert newnode[field] == oldnode[field]
    assert newnode['evidence'][:len(oldnode['evidence'])] == oldnode['evidence']
    if key != 'os.processes':
        assert newnode == oldnode

eids = [e['evidence_id'] for n in state['competencies'].values() for e in n['evidence']]
rids = [r['review_id'] for n in state['competencies'].values() for r in n['review_plan']]
assert len(eids) == len(set(eids)) and len(rids) == len(set(rids))
for key, item in state['competencies'].items():
    assert set(item['scores']) == set(mapping['assessment_policy']['axes'])
    assert all(v is None or type(v) is int and 0 <= v <= 4 for v in item['scores'].values())
    for e in item['evidence']:
        assert e['competency_id'] == key
    for r in item['review_plan']:
        assert all(e in eids for e in r['anchor_evidence_ids'] + r['result_evidence_ids'])
    for assessment in item['assessment_history']:
        assert all(e in eids for e in assessment['evidence_ids'])

body = f'''- Status **completed**, session {sid}; saved {stamp}. User budget 60 minutes; first measured startup 05:31:53 WIB, earlier preparation unmeasured; conservative close 06:29, reserve 06:24. Closing began 06:06:14 after objective met. Wall time includes setup and interaction, not measured active work. No reported break; no extra exercise added to fill unused budget.
- review-006 / report-two-stage-controller-v1 / a001: learner independently proposes Run-based ordered execution, implements early failure returns and success after both stages, and reports four expected outputs/statuses. Instructor independently builds and verifies all four scenarios PASS. Learner code unchanged by instructor; snapshots and verification at {artref}/. Failure diagnostics correctly go to stderr.
- Final hypothetical reasoning: {response} Correct at H0; hypothetical delay variant was not executed. See {notesref}, observations o01-o03.
- Evidence {e1}/{e2}. Scores unchanged: processes C2/I3/D2/J-null/T-null; files C3/I3/D2/J-null/T-null. Both low confidence and functional unchanged; other competencies untouched. Successful narrow independent implementation retrieval strengthens score 3; full process concept outcome is broader than observed reasoning, so concept 2 retained. No numerical assessment change entry needed.
- Assistance per assessed axis: implementation H0, concept H0. Instructor supplied commands/streams, fixtures, checker and persistence. Known earlier teaching recorded; no claim of independently constructing launcher, signal handling, controlled shutdown, debugging investigation, judgment or cross-stack transfer.
- No misconception observed in this task, no new recurring pattern. MP-001 remains improving and was not tested; mistake-patterns unchanged.
- Completed overdue review 2026-10-20-s02-r01 on October 27 (D7 from anchor, D6 from October 21 independent patch). Next result-handling implementation/concept retrieval November 7 (D11 adjusted from D7 November 3 to weekend availability). Existing October 31 exit/defer and runtime-debugging reviews, and November 1 file reviews, retained. No reviews due as of October 27 after completion; no automation.
- Calibration maintain difficulty 1; coherent independent proposal, patch, runtime outputs and causal explanation. No reported difficulty/frustration; availability is sole learner feedback. Objective complete early, not a reason for automatic promotion or another mandatory task.
- Next direction: if next session occurs before October 31, a short baseline for os.threads concept/implementation can broaden evidence; os.processes prerequisite C2/I3 has relevant evidence. Otherwise prioritize due October 31 reviews. Frame thread/goroutine introduction as new learning/probe, not already demonstrated capability. No new lab prepared this session.
- No unfinished code or environment blocker; active_work null. No commit, push or external reminder. Startup/attempt snapshots preserved. Historical evidence unchanged.
'''
checkpoint = root / cpref
if not checkpoint.exists():
    checkpoint.write_text(f'# Checkpoint {cp}\n\n' + body, encoding='utf-8')
for ref in [notesref, cpref, artref+'/batch.go.txt', artref+'/main.go.txt', artref+'/fixture.go.txt',
            artref+'/verification.json', 'labs/review-006/attempts/a001/artifacts/s01-o02-learner-output.txt']:
    assert (root/ref).is_file(), ref
candidate = raw[:raw.index('schema_version:')] + yaml.safe_dump(state, sort_keys=False, allow_unicode=True, width=110)
assert yaml.safe_load(candidate) == state
tmp = statepath.with_suffix('.yaml.tmp')
tmp.write_text(candidate, encoding='utf-8')
os.replace(tmp, statepath)
append_once(root/'learner/session-history.md', f'### {cp}', f'### {cp}\n\n{body}\nCheckpoint: {cpref}')
saved = yaml.safe_load(statepath.read_text(encoding='utf-8'))
history = (root/'learner/session-history.md').read_text(encoding='utf-8')
assert saved == state and saved['last_applied_checkpoint'] == cp and saved['active_work'] is None
assert history.count(f'### {cp}') == 1 and cpref in history
assert (root/notesref).read_text(encoding='utf-8').count('## 2026-10-27-s01-o03') == 1
message = 'PASS: map/state/lab YAML parse; 38 competency IDs match; unique evidence/review IDs and references resolve; existing evidence and assessments preserved; scores/confidence/proficiency and other competencies unchanged; source matches verified snapshot; state/history/checkpoint agree; active_work null.'
append_once(checkpoint, '## Final validation', '## Final validation\n\n'+message)
append_once(root/notesref, f'### {cp} saved', f'### {cp} saved\n\n{message}\nCheckpoint: {cpref}')
append_once(root/f'learner/sessions/{sid}/startup.md', '## Completed at checkpoint', f'## Completed at checkpoint\n\n{cp}; see {cpref}. No pending prediction or implementation.')
print(message)
