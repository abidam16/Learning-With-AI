"""Persist the bounded session without changing assessment or learner code."""
from pathlib import Path
import hashlib
import sys
sys.path.insert(0, r'C:/Users/abid.mahdy/AppData/Local/Temp/learning-lab-yaml-validation')
import yaml

root = Path(__file__).resolve().parents[3]
sid = '2026-10-23-s03'
cpid = sid + '-cp01'
ref = f'learner/sessions/{sid}/checkpoint.md'
notes_ref = 'labs/diag-006/attempts/a001/notes.md'
state_path = root / 'learner/competency-state.yaml'
original = state_path.read_text(encoding='utf-8')
before = yaml.safe_load(original)
curriculum = yaml.safe_load((root / 'curriculum/competency-map.yaml').read_text(encoding='utf-8'))
lab = yaml.safe_load((root / 'labs/diag-006/lab.yaml').read_text(encoding='utf-8'))
assert set(before['competencies']) == set(curriculum['competencies'])
assert all(x in curriculum['competencies'] for x in lab['primary_competency_ids'])
assert (root / 'labs/diag-006/main.go').read_bytes() == (root / 'labs/diag-006/attempts/a001/artifacts/s03-o02-main.go.txt').read_bytes()

observation = '''## 2026-10-23-s03-o09 — cleanup success does not erase write failure

- Closing observation recorded 2026-10-23T14:22:20+07:00. Learner predicts nil when Fprintf fails but deferred Close succeeds, explaining that the final operation's result is returned to the caller.
- Interpretation: still conflates a deferred call's returned value with outer named result mutation, and successful cleanup with successful export. Previous o07 recognition of timing and o08 correct signature remain valid narrow observations; do not rewrite them or infer complete understanding from them.
- Feedback: caller should receive Fprintf failure; successful Close does not make writing successful. Close's returned value does not automatically modify resultErr. Only explicit assignment can do that. Unconditionally assigning a nil Close result would erase the earlier error; preserve an existing failure and use a Close failure when no earlier failure exists. No full implementation supplied or target source edited.
- No learner response to this closing explanation yet; distinguish teaching from demonstrated understanding. Guided concept/debugging/implementation maximum H5 retained. No new recurring pattern or emotional inference.
'''
notes = root / notes_ref
if '## 2026-10-23-s03-o09 ' not in notes.read_text(encoding='utf-8'):
    with notes.open('a', encoding='utf-8') as f:
        f.write('\n\n' + observation)

body = '''- Status **paused** for the 45-minute session budget. Closing began 2026-10-23T14:22:20+07:00. First measured startup 13:42:30 during preparation; conservative closing deadline 14:25. Wall time includes preparation/interactions/waits, not measured active learning time.
- Same diag-006 / order-export-completeness-windows-v1 / a001 resumed from s02-cp02. No new lab or independent delayed retest.
- Learner correctly proposed explicit Flush error propagation, implemented if err := w.Flush(); err != nil { return err }, and reported build. Instructor independently built snapshot s03-o02 successfully (exit 0). No fixture execution or failure injection this session. Snapshot/build record: labs/diag-006/attempts/a001/artifacts/s03-o02-main.go.txt and s03-o02-build.txt. Learner main.go remains byte-identical to snapshot; instructor made no target edits.
- Learner correctly predicted success despite ignored deferred Close error, with function-name wording corrected. Proposed defer-if was invalid; instructor taught anonymous function calls, named result variables, and result preparation before deferred execution and caller handoff. Learner's initial 7 prediction repeated supplied explanation; then predicted 4 despite deferred assignment to 10. After clarification recognized caller has not yet received value while defer runs. Correctly wrote named-error signature in chat; it has not been applied to source.
- Latest response predicts successful Close nil should replace an earlier Fprintf error. Closing teaching distinguishes returned Close value from explicit outer-result assignment and explains preserving earlier write failure. No learner response to this feedback yet. Notes s03-o01 through o09 retain actual observations and assistance.
- Current code: checked Flush; defer f.Close() still ignores Close error; diagnostic Printf retained; function still has unnamed error result. Close repair, exact ordered 3/600 rows, and relevant failure behavior remain pending. No environment blocker found.
- No numerical score, confidence, proficiency, assessment evidence, or review changes: partial guided learning and incomplete error-flow reasoning. os.files-and-descriptors concept 3 remains scoped to prior path reasoning, debugging 2; implementation/judgment/transfer null, confidence low, proficiency learning. Other competencies untouched. No independent buffering/cleanup mastery claim.
- Hint maxima concept H5 (named-result example/partial approach), debugging H5, implementation H5. Learner wrote actual Flush repair after prior assistance; no full Close solution or instructor patch. Correct signature and timing recognition are immediate supported observations, not retention evidence.
- Observed gaps: anonymous/deferred function syntax, return preparation versus handoff, and automatic propagation/last-operation assumptions. No cross-task recurring pattern established; mistake-patterns unchanged. Learner explicitly reported first exposure and lack of understanding; no frustration inferred.
- Calibration maintain difficulty 1; immediate teaching narrowed to language/control-flow foundation. Pause for budget, not learner failure. Next check: with resultErr already holding a write error, compare ignoring Close's returned nil against explicitly assigning it; ask which action changes resultErr and whether success would satisfy the contract. Then learner authors named-result deferred cleanup, ensuring Close runs on early returns and errors are not silently erased, followed by build/output/failure verification.
- Reviews remain October 24 (processes) and October 25 (file paths). Buffering/cleanup retrieval pending sufficient learning evidence. No automation, commit or push.
- References: labs/diag-006/attempts/a001/notes.md; learner/sessions/2026-10-23-s03/startup.md. Active work remains diag-006, now pointing to this checkpoint.
'''
checkpoint = root / ref
if not checkpoint.exists():
    checkpoint.write_text(f'# Checkpoint {cpid}\n\n' + body, encoding='utf-8')
history = root / 'learner/session-history.md'
heading = f'### {cpid}'
if heading not in history.read_text(encoding='utf-8'):
    with history.open('a', encoding='utf-8') as f:
        f.write('\n\n' + heading + '\n\n' + body + '\nCheckpoint: ' + ref + '\n')

prefix, suffix = original.split('\ncompetencies:\n', 1)
metadata = yaml.safe_load(prefix)
metadata['last_session_id'] = sid
metadata['last_applied_checkpoint'] = cpid
metadata['updated_on'] = '2026-10-23'
metadata['active_work'] = dict(lab_id='diag-006', task_variant=lab['task_variant'], attempt_id='a001', session_id=sid, checkpoint_id=cpid, checkpoint_reference=ref, next_step='Distinguish ignored Close return from assignment to named result; preserve prior write error, then learner authors deferred cleanup and verifies 3/600 rows and failures.')
comment = original[:original.index('schema_version:')]
candidate = comment + yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True).rstrip() + '\ncompetencies:\n' + suffix
after = yaml.safe_load(candidate)
assert before['competencies'] == after['competencies']
state_path.write_text(candidate, encoding='utf-8')
saved = yaml.safe_load(state_path.read_text(encoding='utf-8'))
assert saved == after
assert saved['active_work']['checkpoint_reference'] == ref
assert saved['last_applied_checkpoint'] == cpid
assert history.read_text(encoding='utf-8').count(heading) == 1
assert notes.read_text(encoding='utf-8').count('## 2026-10-23-s03-o09 ') == 1
for artifact in [ref, notes_ref, f'learner/sessions/{sid}/startup.md', 'labs/diag-006/attempts/a001/artifacts/s03-o02-main.go.txt', 'labs/diag-006/attempts/a001/artifacts/s03-o02-build.txt']:
    assert (root / artifact).is_file(), artifact
validation = '\n## Final validation\n\nPASS: map/state/lab YAML parses; 38 competency IDs match; all competency scores/evidence/assessments/reviews unchanged; checkpoint/history/state agree and entry is unique; referenced artifacts resolve; learner source equals preserved s03-o02 snapshot.\n'
if '## Final validation' not in checkpoint.read_text(encoding='utf-8'):
    with checkpoint.open('a', encoding='utf-8') as f:
        f.write(validation)
print('PASS: ' + ref + '; assessment/reviews unchanged; source SHA256=' + hashlib.sha256((root / 'labs/diag-006/main.go').read_bytes()).hexdigest())
