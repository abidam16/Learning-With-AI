"""Persist the guided learning checkpoint once; preserve unrelated state."""
from copy import deepcopy
from datetime import datetime, timedelta, timezone
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(root / '.tools/python-support'))
import yaml

sid = '2026-10-29-s01'
cpid = sid + '-cp01'
checkpoint_ref = f'learner/sessions/{sid}/checkpoint.md'
notes_ref = 'labs/probe-004/attempts/a001/notes.md'
state_path = root / 'learner/competency-state.yaml'
original = state_path.read_text(encoding='utf-8')
before = yaml.safe_load(original)
curriculum = yaml.safe_load((root / 'curriculum/competency-map.yaml').read_text(encoding='utf-8'))
assert before['last_applied_checkpoint'] in ('2026-10-27-s01-cp01', cpid)
assert curriculum['curriculum_version'] == '1.1.0'
state = deepcopy(before)
node = state['competencies']['os.threads']
now = datetime.now(timezone(timedelta(hours=7))).isoformat(timespec='seconds')

def append_once(path, marker, content):
    previous = path.read_text(encoding='utf-8') if path.exists() else ''
    if marker not in previous:
        path.write_text(previous.rstrip() + '\n\n' + content.rstrip() + '\n', encoding='utf-8')

append_once(root / notes_ref, '## 2026-10-29-s01-o05', '''## 2026-10-29-s01-o05 — guided understanding check and close

- Response observed by 07:21:30 WIB: "T2 menggunakan CPU dan T1 akan menunggu sampai kondisi blocked terpenuhi. Ketika terpenuhi dia akan masuk ke ready dan akan lanjut dieksekusi ketika mendapatkan CPU."
- Correctly distinguishes CPU reuse from blocked-thread identity, and blocked -> ready -> running. Follows direct H4 explanation; immediate uptake only, not independent reconstruction or delayed retention. No code execution/patch reported by learner.
- Concept assessment os.threads null -> 1: specific fragments explained with significant assistance. Full outcome (process/OS-thread/goroutine distinctions and concurrency/parallelism) not demonstrated independently. Confidence none -> low, proficiency unseen -> learning. Other axes remain null; other competencies unchanged. Earlier correct numerical predictions were qualified by learner's explicit report of guessing and unresolved causal explanations.
- Session paused at time boundary; closing started 07:21:30, after conservative 07:16 target. First captured startup 06:21:21, earlier setup unmeasured. No reported break or time extension. Wall-clock includes interaction/reading; active learning time unknown. Do not add another task.
- Assistance: concept H0 initial answer, H1 clarification, H4 teaching and subsequent checks. Implementation/debugging/judgment/transfer not observed. Instructor-only setup and baseline run remain separate.
- Current working model from learner: blocked T1 retains identity; T2 uses CPU; T1 becomes ready then runs only when scheduled. Remaining uncertainty: independent reconstruction of context save/restore, preemption, process/thread IDs, response mapping, goroutine versus OS-thread and hardware-thread distinctions.
- Next action: a brief fresh trace with one logical processor, T1 running and T2 ready (no I/O); ask what can allow T2 to run before T1 finishes and what preserves T1's progress. Treat this as an unassisted attempt before displaying old explanation. Teach gaps if needed, then resume diag-007 baseline using its README. No requirement to complete coding before foundation is ready.
- Next concept retrieval planned October 31 (D2 after teaching); coordinate with already-planned process reviews. No other review dates reset. No new recurring pattern: observations are within one attempt and instruction ambiguity contributed. MP-001 unchanged.
- learner_feedback: earlier responses partly guesses; missing foundational model; requested explanation before implementation. Calibration remediate/reduce immediate scope to foundation, retain difficulty 1; next check is fresh causal trace. No inferred frustration.
''')

common = dict(session_id=sid, date='2026-10-29', lab_id='probe-004', attempt_id='a001', competency_id='os.threads', axis='concept', task_variant='independent-waits-one-core-v1', assessment_status='assessed', artifact_or_observation=notes_ref, retest_of=None, correction_of=None)
entries = [
    dict(common, evidence_id=sid+'-e01', max_hint='H1', prompt_context='H0 scenario followed by H1 causal clarification. Later learner explicitly reports guessing. Instructor wording mixed work/process/thread layers; treat that ambiguity as a limitation.', result='Predicts possible one-second wait but attributes it to rapid CPU alternation; follow-up assigns different PIDs to threads of the same program and does not distinguish blocked I/O from CPU execution.', reasoning_check=dict(check_type='causal_explanation', prompt='After A/B requests are sent, must their work keep taking CPU turns while waiting for responses?', learner_response='Separate threads handle A/B with different PIDs; one core rapidly alternates between PID A and PID B, allowing one second.', observation_reference=notes_ref, interpretation='Numeric answer alone is insufficient; specific identity and waiting-model gaps require teaching. No inference of general inability.', limitations=['Self-reported guessing qualifies independence of reasoning.', 'Instructor wording ambiguity contributed.', 'No runtime or implementation evidence.'])),
    dict(common, evidence_id=sid+'-e02', max_hint='H4', prompt_context='Direct foundation explanation of process/thread/core, scheduling states, context switching, socket wakeup and Go runtime; immediate check after teaching.', result='Correctly states T2 uses CPU while T1 remains blocked; T1 becomes ready when waiting condition is satisfied and runs when scheduled. Earlier guided CPU-work prediction correctly totals two seconds but assumed A must finish before B; instructor corrected that.', reasoning_check=dict(check_type='causal_explanation', prompt='T1 is blocked waiting for network response and T2 ready. Does T2 use thread T1 or CPU, and what happens to T1?', learner_response='T2 uses CPU; T1 waits until the blocked condition is fulfilled, then enters ready and resumes when it gets CPU.', observation_reference=notes_ref, interpretation='Immediate guided uptake of a limited mechanism supports concept 1, not independent application or full-outcome score 2/3.', limitations=['H4 assistance.', 'No fresh or delayed reconstruction yet.', 'OS-thread/goroutine/SMT and response routing not rechecked.', 'No implementation, debugging, judgment or transfer assessed.']))
]
for entry in entries:
    if not any(e['evidence_id'] == entry['evidence_id'] for e in node['evidence']):
        node['evidence'].append(entry)
assessment_id = sid+'-a01'
if not any(a['assessment_id'] == assessment_id for a in node['assessment_history']):
    assert node['scores']['concept'] is None
    node['assessment_history'].append(dict(assessment_id=assessment_id, session_id=sid, checkpoint_id=cpid, date='2026-10-29', evidence_ids=[e['evidence_id'] for e in entries], before=dict(scores={'concept': None}, confidence='none', proficiency='unseen'), after=dict(scores={'concept': 1}, confidence='low', proficiency='learning'), rationale='Mapped scale 1: explains specific fragments after substantial conceptual teaching. Initial causal reasoning incomplete/self-reported guesses; final blocked-ready-running answer is immediate H4 uptake, not independent representative application. No penalty for requesting foundations or deferred implementation.'))
node['scores']['concept'] = 1
node.update(confidence='low', proficiency='learning', last_assessed_on='2026-10-29')
review_id = sid+'-r01'
if not any(r['review_id'] == review_id for r in node['review_plan']):
    node['review_plan'].append(dict(review_id=review_id, anchor_evidence_ids=[sid+'-e02'], anchor_date='2026-10-29', target_axes=['concept'], task_type='delayed_retrieval', target_date='2026-10-31', scheduled_date='2026-10-31', scheduling_reason='D2 after H4 foundation teaching and narrow immediate uptake; Saturday matches availability. Fresh trace before explanation, coordinated with existing process reviews. Not a claim of independent success today.', status='planned', completed_at=None, result_evidence_ids=[], schedule_history=[]))
node['review_due'] = False
state.update(updated_on='2026-10-29', last_session_id=sid, last_applied_checkpoint=cpid, active_work=dict(lab_id='probe-004', task_variant='independent-waits-one-core-v1', attempt_id='a001', session_id=sid, checkpoint_id=cpid, checkpoint_reference=checkpoint_ref, next_step='Fresh brief scheduling/context trace before further teaching; then, if foundation permits, read labs/diag-007/runner.go and run go run . from labs/diag-007. Implementation remains unattempted.'))

assert set(state['competencies']) == set(curriculum['competencies'])
for cid, old in before['competencies'].items():
    new = state['competencies'][cid]
    if cid != 'os.threads':
        assert old == new
    else:
        assert new['evidence'][:len(old['evidence'])] == old['evidence']
        assert new['assessment_history'][:len(old['assessment_history'])] == old['assessment_history']
        for axis in curriculum['assessment_policy']['axes']:
            if axis != 'concept':
                assert new['scores'][axis] == old['scores'][axis]
ids = [e['evidence_id'] for c in state['competencies'].values() for e in c['evidence']]
reviews = [r['review_id'] for c in state['competencies'].values() for r in c['review_plan']]
assert len(ids) == len(set(ids)) and len(reviews) == len(set(reviews))
for cid, c in state['competencies'].items():
    assert all(v is None or type(v) is int and 0 <= v <= 4 for v in c['scores'].values())
    for e in c['evidence']:
        assert e['competency_id'] == cid
        for ref in re.findall(r'(?:labs|learner)/[A-Za-z0-9_./-]+', e['artifact_or_observation']):
            assert (root / ref.rstrip('.')).exists(), ref
    for r in c['review_plan']:
        assert set(r['anchor_evidence_ids'] + r['result_evidence_ids']) <= set(ids)
for lab_id in ('probe-004', 'diag-007'):
    lab = yaml.safe_load((root / f'labs/{lab_id}/lab.yaml').read_text(encoding='utf-8'))
    assert set(lab['primary_competency_ids']) <= set(curriculum['competencies'])

summary = f'''- Status **paused**, session {sid}; saved {now}. User budget 60 minutes. Closing began 07:21:30 WIB; first captured startup 06:21:21, earlier setup unmeasured. Conservative 07:16 boundary exceeded while reading/interacting; active work time unknown. No reported break or extension. No additional task added at closing.
- probe-004 / independent-waits-one-core-v1 / a001: initial correct elapsed-time prediction had incomplete causal reasoning; learner explicitly reported guessing and requested foundations. Instructor acknowledged ambiguous switching between jobs/processes/threads, then provided H4 foundation. Final learner answer correctly distinguishes T2 using CPU from T1 remaining blocked, and T1 becoming ready before it is scheduled. Immediate guided uptake, not independent mastery or retention.
- Evidence {sid}-e01/e02; os.threads concept null -> 1, confidence none -> low, proficiency unseen -> learning. Rationale: specific fragments demonstrated after significant help, per map scale. All other os.threads axes remain null; every other competency unchanged. No score penalty for help request, time or deferred implementation.
- Assistance: concept H0 initial/H1 clarification/H4 teaching and guided checks. Implementation/debugging/judgment/transfer not observed. Instructor supplied diag-007 timer scaffold and verified sequential baseline exit 0; learner has not run or edited it. No concurrent solution supplied. Baseline reference: labs/diag-007/attempts/a001/baseline.txt.
- Misconceptions/uncertainty: PID versus thread identity, CPU versus thread reuse, blocked I/O versus CPU work, exclusivity versus run-to-completion. Latest answer corrects CPU reuse and state sequence; independent retention and other distinctions remain unverified. These observations belong to one attempt; no new recurring pattern, MP-001 unchanged.
- Calibration: remediate and reduce immediate scope from implementation to foundation at learner request; difficulty remains 1. Feedback is missing foundations and earlier guessing, not inferred frustration. Foundation work remains open; no tooling blocker.
- Active work points to probe-004 and this checkpoint. Next action: fresh short trace with one logical processor, T1 running/T2 ready and no I/O; ask how T2 can run before T1 finishes and how T1's progress is preserved. Teach gaps as needed, then resume diag-007 baseline from README. Do not immediately claim a fresh check is delayed retrieval unless sufficient interval/context warrants it.
- Next thread concept retrieval October 31 (D2 after teaching), coordinated with existing process reviews. Existing October 31, November 1 and November 7 reviews retained; no completed review falsely recorded. No automation, commit or push.
- Detailed observations: {notes_ref}, o01-o05; deferred implementation: labs/diag-007/attempts/a001/notes.md.
'''
checkpoint = root / checkpoint_ref
if not checkpoint.exists():
    checkpoint.write_text(f'# Checkpoint {cpid}\n\n'+summary, encoding='utf-8')

# Replace only the assessed node and administrative pointers, preserving other YAML text.
start = original.index('  os.threads:\n')
end = original.index('  os.memory:\n', start)
block = yaml.safe_dump({'os.threads': node}, sort_keys=False, allow_unicode=True, width=110)
candidate = original[:start] + ''.join('  '+line if line.strip() else line for line in block.splitlines(keepends=True)) + original[end:]
admin_start = candidate.index('updated_on:')
admin_end = candidate.index('\ncompetencies:', admin_start)
admin = {k: state[k] for k in ('updated_on','last_session_id','last_applied_checkpoint','active_work')}
candidate = candidate[:admin_start] + yaml.safe_dump(admin, sort_keys=False, allow_unicode=True, width=110).rstrip() + candidate[admin_end:]
assert yaml.safe_load(candidate) == state
temporary = state_path.with_suffix('.yaml.pending')
temporary.write_text(candidate, encoding='utf-8')
temporary.replace(state_path)
history = root / 'learner/session-history.md'
append_once(history, f'### {cpid}', f'### {cpid}\n\n'+summary+'\nCheckpoint: '+checkpoint_ref)
append_once(root / f'learner/sessions/{sid}/startup.md', '## Paused at checkpoint', f'## Paused at checkpoint\n\n{cpid}; see {checkpoint_ref}. Guided foundation continues next time; diag-007 remains unattempted.')
assert yaml.safe_load(state_path.read_text(encoding='utf-8')) == state
assert history.read_text(encoding='utf-8').count(f'### {cpid}') == 1
assert cpid in checkpoint.read_text(encoding='utf-8')
assert (root / state['active_work']['checkpoint_reference']).is_file()
validation = 'PASS: map/state/lab YAML parse; 38 competency IDs match; evidence/review IDs unique and references resolve; prior evidence/assessment records preserved; only os.threads concept/confidence/proficiency assessed fields changed; other axes and competencies unchanged; state/history/checkpoint agree; active work and next action resolve.'
append_once(checkpoint, '## Final validation', '## Final validation\n\n'+validation)
append_once(root / notes_ref, '## Checkpoint saved', f'## Checkpoint saved\n\n{cpid}; {checkpoint_ref}. '+validation)
print(validation)
print('Saved: '+checkpoint_ref)
