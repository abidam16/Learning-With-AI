"""Persist this observed session; does not modify learner source or test fixtures."""
from pathlib import Path
from copy import deepcopy
import json
import sys
sys.path.insert(0, r'C:/Users/abid.mahdy/AppData/Local/Temp/learning-lab-yaml-validation')
import yaml

root = Path(__file__).resolve().parents[3]
sid = '2026-10-23-s04'
cpid = sid + '-cp01'
day = '2026-10-23'
cid = 'os.files-and-descriptors'
session = root / 'learner/sessions' / sid
cpref = f'learner/sessions/{sid}/checkpoint.md'
notesref = 'labs/diag-006/attempts/a001/notes.md'
artref = 'labs/diag-006/attempts/a001/artifacts/s04-o04'
statepath = root / 'learner/competency-state.yaml'
text = statepath.read_text(encoding='utf-8')
before = yaml.safe_load(text)
curriculum = yaml.safe_load((root / 'curriculum/competency-map.yaml').read_text(encoding='utf-8'))
lab = yaml.safe_load((root / 'labs/diag-006/lab.yaml').read_text(encoding='utf-8'))
assert curriculum['curriculum_version'] == '1.1.0'
assert set(before['competencies']) == set(curriculum['competencies'])
assert (root / 'labs/diag-006/main.go').read_bytes() == (root / artref / 'main.go.txt').read_bytes()
checks = json.loads((root / artref / 'verification.json').read_text(encoding='utf-8-sig'))
assert checks['source_matches_snapshot']
assert all(x['exit_code'] == 0 and x['exact_ordered_rows'] for x in checks['checks'])
assert 'build_exit_code=0' in (root / artref / 'build.txt').read_text(encoding='utf-8-sig')
testlog = (root / artref / 'failure-tests.txt').read_text(encoding='utf-8-sig')
assert 'test_exit_code=0' in testlog and testlog.count('--- PASS: TestExportFailureAndCleanup/') == 7

def append_once(path, marker, content):
    old = path.read_text(encoding='utf-8')
    if marker not in old:
        with path.open('a', encoding='utf-8') as f:
            f.write('\n\n' + content.rstrip() + '\n')

closing = '''## 2026-10-23-s04-o05 — final caller-flow reasoning and completion

- Closing started 2026-10-23T16:16:54+07:00. Learner correctly explains that successful earlier work leaves resultErr nil, Close error becomes exportReport result, run enters its error branch and prints Ekspor gagal with the error, returns 1, and main passes 1 to os.Exit. Parenthetical "error == nil" understood in context as no prior result error; not treated as a new defect.
- This causal explanation is consistent with the actual learner patch and follows guided H5 work. It confirms current application, not independent retention. Core implementation is learner-authored; all failure tests are instructor-authored.
- Session and diag-006 attempt a001 completed. Implementation null -> 2 for safe cleanup/error propagation with guidance, verified normal output and controlled failures. Concept stays 3 with earlier independent path-reasoning scope explicitly preserved; buffering/error-flow concept remains guided. Debugging stays 2; judgment/transfer null. Confidence low; proficiency learning -> functional under map thresholds, not independent mastery. No weighted score.
- Misconceptions observed during this session: premise mismatch/ignored return versus assignment, and putting cleanup itself inside the error-replacement condition. Later reasoning and patch correct these in the current task; fresh retrieval needed. No independently recurring cross-task pattern established.
- Hint maxima concept H5, debugging H5, implementation H5 across this continuing attempt. No H6 solution or instructor target edit. Difficulty 1 maintained; foundation teaching narrowed the immediate work. Learner feedback about challenge/frustration not supplied; no emotion inferred.
- Next: process review October 24 unchanged; October 25 path review retained plus a fresh H0/H1 small buffering/cleanup/error-flow variant anchored to this session. No external automation. No commit/push.
'''
append_once(root / notesref, '## 2026-10-23-s04-o05 ', closing)

body = f'''- Status **completed**: diag-006 / {lab['task_variant']} / a001. Resumed s03-cp01; no fresh independent diagnostic. Closing began 2026-10-23T16:16:54+07:00, before conservative 16:35 deadline; first measured preparation time 15:52:33. Wall time includes preparation/interactions/waits, not active-work measurement. No extra lab added to fill remaining budget.
- Learner distinguished prior write error from Close result, initially guarded Close itself, then correctly traced the skipped-cleanup path and authored unconditional deferred Close with conditional result replacement. Final causal explanation correctly follows Close-only failure through exportReport -> run -> main -> exit 1.
- Build PASS; actual 3/600-order CLI runs exit 0 and exact ordered rows PASS. Seven controlled-file tests PASS for create/write/Flush/Close failures, error precedence and cleanup count. Failure harness substitutes only file creation in a copied source; it is instructor infrastructure, not actual Windows disk failure or learner-authored tests. No power-loss durability claim.
- Artifacts: {artref}/main.go.txt, build.txt, verification.json, failure-tests.txt, README.md and failure-harness/. Prior incomplete patch retained in artifacts/s04-o03/. Original learner source matches final snapshot; no instructor target edit.
- Assessment: os.files-and-descriptors implementation null -> 2, supported by guided learner-written repair, verification and reasoning. Concept 3 unchanged and scoped to prior path evidence, debugging 2 unchanged, judgment/transfer null. Buffering/cleanup concept newly demonstrated only with assistance. Confidence low; proficiency functional by map thresholds, not broad independence. Evidence {sid}-e01/e02 and assessment {sid}-as01.
- Assistance maxima: concept H5, debugging H5, implementation H5. No independent mastery or delayed-retention claim. Permission handling, real disk failures, durability, judgment and transfer remain unassessed in this lab.
- Misconceptions addressed: ignored return versus result assignment; conditional cleanup versus conditional replacement. Corrections observed within same guided task, not a recurring cross-task pattern; mistake-patterns unchanged.
- learner_feedback: time budget 45 minutes; no challenge/frustration report. calibration_decision: maintain difficulty 1, because supported progress followed targeted control-flow teaching; next check removes solution cues on a fresh H0/H1 variant.
- Active work cleared. Process reviews October 24 and path review October 25 retained. Added October 25 D2 buffering/cleanup/error-flow retrieval for concept and implementation; combine within available time without counting one variant as several independent tasks. Next executable learning step: present a small new resource-writing scenario and request prediction before running or modifying it. If next session is October 24, prioritize due process review under selection policy.
- Notes: {notesref}, observations s04-o01 through s04-o05. No automation, commit or push. Persistence validation below is required before claiming the save completed.
'''
checkpoint = root / cpref
if not checkpoint.exists():
    checkpoint.write_text(f'# Checkpoint {cpid}\n\n' + body, encoding='utf-8')

after = deepcopy(before)
if before['last_applied_checkpoint'] != cpid:
    assert before['last_applied_checkpoint'] == '2026-10-23-s03-cp01'
    assert before['active_work']['lab_id'] == 'diag-006'
    c = after['competencies'][cid]
    assert c['scores']['implementation'] is None
    oldc = deepcopy(c)
    common = dict(session_id=sid, date=day, lab_id='diag-006', attempt_id='a001', competency_id=cid,
                  task_variant=lab['task_variant'], retest_of=None, correction_of=None,
                  assessment_status='assessed', max_hint='H5')
    e1 = dict(common, evidence_id=sid+'-e01', axis='implementation',
        artifact_or_observation=f'{artref}/main.go.txt; {artref}/verification.json; {artref}/failure-tests.txt; {notesref} — s04-o03-o05',
        result='Learner implemented checked Flush and deferred unconditional Close with first-error preservation; final source builds, exact ordered 3/600 rows and seven injected-file cases pass.',
        prompt_context='Continuing guided attempt: named-result teaching and partial cleanup/error-precedence approach H5; conditional-cleanup defect identified by instructor, repaired by learner. Harness authored by instructor.',
        reasoning_check=dict(check_type='causal_explanation', prompt='Trace previous guarded Close after Fprintf failure, then trace final patch when Close fails after successful Flush.',
            learner_response='Previous resultErr receives write error and Close is skipped; final Close-only error becomes exportReport result, run prints Ekspor gagal and returns 1, main calls os.Exit(1).',
            observation_reference=notesref+' — s04-o04/o05',
            interpretation='Correct integrated implementation and causal explanation with guidance support implementation 2, not independent 3.',
            limitations=['Same guided task across sessions; no delayed retrieval.', 'Controlled fake file for failures; no real disk failure or permission configuration assessed.']))
    e2 = dict(common, evidence_id=sid+'-e02', axis='concept',
        artifact_or_observation=notesref+' — s04-o01-o05',
        result='After feedback, learner correctly distinguishes explicit result assignment, preservation of prior error, unconditional cleanup, and final error/status propagation.',
        prompt_context='H5 accumulated exposure; early incorrect premise/result reasoning preserved in notes. Correct responses followed targeted teaching.',
        reasoning_check=dict(check_type='causal_explanation', prompt='All Fprintf/Flush calls succeed, Close fails: explain exportReport -> run -> main message and exit status.',
            learner_response='No earlier result error, so Close error becomes returned result; run prints Ekspor gagal and returns 1, passed to os.Exit.',
            observation_reference=notesref+' — s04-o05',
            interpretation='Current guided error-flow understanding demonstrated. Existing concept 3 for prior path reasoning is unchanged; do not generalize independence to buffering/cleanup.',
            limitations=['Immediate guided response, not delayed independent evidence.', 'No durability, permission or cross-resource transfer assessment.']))
    c['evidence'].extend([e1, e2])
    c['scores']['implementation'] = 2
    c['proficiency'] = 'functional'
    c['last_assessed_on'] = day
    c['assessment_history'].append(dict(assessment_id=sid+'-as01', session_id=sid, checkpoint_id=cpid, date=day,
        evidence_ids=[sid+'-e01',sid+'-e02'],
        before=dict(scores={'implementation': None}, confidence='low', proficiency='learning'),
        after=dict(scores={'implementation': 2}, confidence='low', proficiency='functional'),
        rationale='Guided learner-written safe-close and error-propagation repair now verified with causal explanation. Implementation 2 supports functional threshold together with existing concept 3/path scope and debugging 2. No independence claim, other axes unchanged.'))
    c['review_plan'].append(dict(review_id=sid+'-r01', anchor_evidence_ids=[sid+'-e01',sid+'-e02'], anchor_date=day,
        target_axes=['concept','implementation'], task_type='delayed_retrieval', target_date='2026-10-25', scheduled_date='2026-10-25',
        scheduling_reason='D2 Sunday; fresh small H0/H1 buffering/cleanup/error-flow variant after H5-guided completion. Preserve existing October 24 process and October 25 path plans; fit scope to time.',
        status='planned', completed_at=None, result_evidence_ids=[], schedule_history=[]))
    after.update(last_session_id=sid, last_applied_checkpoint=cpid, updated_on=day, active_work=None)
    for key in before['competencies']:
        if key != cid: assert after['competencies'][key] == before['competencies'][key]
    assert c['evidence'][:len(oldc['evidence'])] == oldc['evidence']
    assert c['assessment_history'][:-1] == oldc['assessment_history']
    assert c['review_plan'][:-1] == oldc['review_plan']
    assert all(c['scores'][a] == oldc['scores'][a] for a in c['scores'] if a != 'implementation')
    header = text[:text.index('schema_version:')]
    candidate = header + yaml.safe_dump(after, sort_keys=False, allow_unicode=True, width=105)
    assert yaml.safe_load(candidate) == after
    temporary = session / 'competency-state.candidate.yaml'
    temporary.write_text(candidate, encoding='utf-8')
    temporary.replace(statepath)

append_once(root / 'learner/session-history.md', f'### {cpid}', f'### {cpid}\n\n{body}\nCheckpoint: {cpref}')
saved = yaml.safe_load(statepath.read_text(encoding='utf-8'))
assert saved == after and saved['active_work'] is None and saved['last_applied_checkpoint'] == cpid
assert set(saved['competencies']) == set(curriculum['competencies'])
allids = []
for key, item in saved['competencies'].items():
    assert set(item['scores']) == set(curriculum['assessment_policy']['axes'])
    assert all(v is None or type(v) is int and 0 <= v <= 4 for v in item['scores'].values())
    for e in item['evidence']:
        assert e['competency_id'] == key
        allids.append(e['evidence_id'])
assert len(allids) == len(set(allids))
for item in saved['competencies'].values():
    for assessment in item['assessment_history']:
        assert set(assessment['evidence_ids']).issubset(allids)
    for review in item['review_plan']:
        assert set(review['anchor_evidence_ids']).issubset(allids)
for ref in [cpref, notesref, artref+'/main.go.txt', artref+'/verification.json', artref+'/build.txt', artref+'/failure-tests.txt', artref+'/README.md', artref+'/failure-harness/instructor_test.go']:
    assert (root / ref).is_file(), ref
history = (root / 'learner/session-history.md').read_text(encoding='utf-8')
assert history.count(f'### {cpid}') == 1 and cpref in history
assert (root / notesref).read_text(encoding='utf-8').count('## 2026-10-23-s04-o05 ') == 1
assert (root / 'labs/diag-006/main.go').read_bytes() == (root / artref / 'main.go.txt').read_bytes()
message = 'PASS: map/state/lab YAML parse; competency IDs and unique evidence/review references valid; prior observations and other competencies preserved; checkpoint/history/state agree; source matches final learner snapshot. Implementation null->2, proficiency functional, confidence low; active work cleared.'
append_once(checkpoint, '## Final validation', '## Final validation\n\n'+message)
append_once(root / notesref, f'### {cpid} saved', f'### {cpid} saved\n\n{message}\nCheckpoint: {cpref}')
print(message)
