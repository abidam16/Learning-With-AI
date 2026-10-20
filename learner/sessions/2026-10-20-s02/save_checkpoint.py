"""Persist and validate this session checkpoint; no learner source edits."""
import copy
import sys
from pathlib import Path

sys.path.insert(0, r"C:\Users\abid.mahdy\AppData\Local\Temp\learning-lab-yaml-validation")
import yaml

ROOT = Path(__file__).resolve().parents[3]
STATE = ROOT / "learner/competency-state.yaml"
SESSION = "2026-10-20-s02"
CP = SESSION + "-cp01"
NOTES = "labs/diag-001/attempts/a001/notes.md"
ART = "labs/diag-001/attempts/a001/artifacts/"
curriculum = yaml.safe_load((ROOT / "curriculum/competency-map.yaml").read_text(encoding="utf-8"))
raw = STATE.read_text(encoding="utf-8")
state = yaml.safe_load(raw)
before = copy.deepcopy(state)
node = state["competencies"]["os.processes"]
assert curriculum["curriculum_version"] == state["curriculum_version"] == "1.1.0"

prompt = (
    "Jika hanya os.Exit(1) pada cabang error dihapus, sementara if/else tetap, "
    "apa pesan dan LASTEXITCODE untuk lab.exe ditolak? Mengapa?"
)
response = (
    "Hanya Job: input ditolak; LASTEXITCODE 0 karena program selesai normal "
    "tanpa perintah exit nonzero seperti os.Exit(1)."
)

def evidence(number, axis, status, result, hint, context, check):
    return dict(
        evidence_id=f"{SESSION}-e{number:02}",
        session_id=SESSION, date="2026-10-20",
        lab_id="diag-001", attempt_id="a001",
        competency_id="os.processes", axis=axis,
        task_variant="batch-report-windows-v1",
        assessment_status=status, artifact_or_observation=NOTES,
        result=result, max_hint=hint, prompt_context=context,
        reasoning_check=check, retest_of=None, correction_of=None,
    )

new_evidence = [
    evidence(
        1, "debugging", "not_observed",
        "Learner identified unconditional batch completion, chose direct job invocation, "
        "predicted rejection/2 and reported that result (o03-o06). Contrasts with earlier batch completion/0.",
        "H1",
        "Neutral workflow prompts before the Stdout/Run teaching. Prior process-concept exposure H4 "
        "is retained; direct invocation experiment was selected by learner. Later API assistance "
        "does not retroactively relabel this observation.",
        dict(
            check_type="discriminating_experiment",
            prompt="Pilih eksperimen, pengamatan, dan prediksi untuk menguji dugaan sebelum perbaikan.",
            learner_response="Run lab.exe --job ditolak, inspect output and LASTEXITCODE; "
            "predict only rejection and 2 because os.Exit(2); reported both as predicted.",
            observation_reference=ART + "s02-direct-job-output.txt",
            interpretation="Useful learner-selected comparison and source-based diagnosis. "
            "Insufficient coverage to score the map outcome distinguishing crash, kill and startup failure.",
            limitations=["Same resumed attempt, not a fresh or delayed retest.",
                         "Execution output reported by learner, not observed directly.",
                         "No crash, kill or startup experiment."],
        ),
    ),
    evidence(
        2, "implementation", "assessed",
        "Learner wrote all patches. Patch01 confused Stdout with outcome and failed rejection test; "
        "patch02 adopted Run error/exit handling but failed compilation; patch03 uses one error return "
        "and exits batch 1 on error. Instructor build and both contract tests passed.",
        "H4",
        "Instructor explained Stdout destination versus exit status and Run's error return, "
        "then clarified one return value. No instructor patch or pseudocode. Scaffold launching "
        "and stream wiring are instructor-provided.",
        dict(
            check_type="prediction", prompt=prompt, learner_response=response,
            observation_reference=NOTES,
            interpretation="Passing learner-authored guided repair plus correct final explanation "
            "supports implementation 2 for result handling and batch exit status in this narrow task.",
            limitations=["Assisted implementation; not independent score 3.",
                         "Launching/wiring supplied by scaffold; signals and controlled shutdown untested.",
                         "Same final reasoning response also supports e03, not an additional independent task.",
                         "Hypothetical edit was discussed only; passing tests apply to retained final source."],
        ),
    ),
    evidence(
        3, "concept", "assessed",
        "Correctly predicted rejection message with batch status 0 if only batch os.Exit(1) "
        "were removed while if/else stayed; explained normal batch termination without nonzero exit.",
        "H4",
        "After process/exit teaching in s01 and Stdout/Run explanation in s02. "
        "Final question supplies a hypothetical change but no answer before response.",
        dict(
            check_type="prediction", prompt=prompt, learner_response=response,
            observation_reference=NOTES,
            interpretation="Reinforces concept 2 for distinction between job failure and batch "
            "termination. No independent promotion from immediate post-teaching reasoning.",
            limitations=["One familiar task/date, after assistance.",
                         "No execution of hypothetical variant.",
                         "PID, environment, signals, meaningful transfer and delayed retrieval untested."],
        ),
    ),
]

if "--validate" not in sys.argv:
    if state["last_applied_checkpoint"] != CP:
        assert node["scores"]["implementation"] is None
        assert not any(e["evidence_id"].startswith(SESSION) for e in node["evidence"])
        node["evidence"].extend(new_evidence)
        node["scores"]["implementation"] = 2
        node["assessment_history"].append(dict(
            assessment_id=SESSION + "-as01", session_id=SESSION,
            checkpoint_id=CP, date="2026-10-20",
            evidence_ids=[SESSION + "-e02", SESSION + "-e03"],
            before={"scores": {"implementation": None}},
            after={"scores": {"implementation": 2}},
            rationale="Guided learner-authored standard-case result handling passed both tests and "
            "final reasoning check. Narrow implementation baseline, not signal/shutdown mastery. "
            "Concept remains 2 after immediate assisted explanation; debugging remains unassessed "
            "for crash/kill/startup despite useful partial evidence. Confidence low and proficiency "
            "learning remain appropriate; all other scores unchanged.",
        ))
        node["review_plan"].append(dict(
            review_id=SESSION + "-r01", anchor_evidence_ids=[SESSION + "-e02"],
            anchor_date="2026-10-20", target_axes=["implementation"],
            task_type="delayed_retrieval", target_date="2026-10-22",
            scheduled_date="2026-10-24",
            scheduling_reason="Fresh H0/H1 variant after H4 API help; D2 target moved to Saturday "
            "availability D4. Can accompany existing concept review without replacing it.",
            status="planned", completed_at=None, result_evidence_ids=[], schedule_history=[],
        ))
        state["last_session_id"] = SESSION
        state["last_applied_checkpoint"] = CP
        state["active_work"] = None
        state["updated_on"] = "2026-10-20"
        # Check every unrelated competency and every unchanged target field.
        for key in state["competencies"]:
            if key != "os.processes":
                assert state["competencies"][key] == before["competencies"][key]
        previous = before["competencies"]["os.processes"]
        for axis in curriculum["assessment_policy"]["axes"]:
            if axis != "implementation":
                assert node["scores"][axis] == previous["scores"][axis]
        for key in ("confidence", "proficiency", "weighted_score", "last_assessed_on", "review_due"):
            assert node[key] == previous[key]
        assert node["evidence"][:len(previous["evidence"])] == previous["evidence"]
        assert node["assessment_history"][:len(previous["assessment_history"])] == previous["assessment_history"]
        assert node["review_plan"][:len(previous["review_plan"])] == previous["review_plan"]
        prefix = raw[:raw.index("schema_version:")]
        candidate = prefix + yaml.safe_dump(state, allow_unicode=True, sort_keys=False, width=110)
        assert yaml.safe_load(candidate) == state
        temp = STATE.with_name("competency-state.s02.pending.yaml")
        temp.write_text(candidate, encoding="utf-8")
        assert yaml.safe_load(temp.read_text(encoding="utf-8")) == state
        temp.replace(STATE)

state = yaml.safe_load(STATE.read_text(encoding="utf-8"))
assert set(state["competencies"]) == set(curriculum["competencies"])
assert state["last_session_id"] == SESSION and state["last_applied_checkpoint"] == CP
assert state["active_work"] is None
node = state["competencies"]["os.processes"]
assert node["scores"] == dict(concept=2, implementation=2, debugging=None, judgment=None, transfer=None)
assert node["confidence"] == "low" and node["proficiency"] == "learning"
all_ids = []
for key, entry in state["competencies"].items():
    for axis, value in entry["scores"].items():
        assert axis in curriculum["assessment_policy"]["axes"]
        assert value is None or (type(value) is int and 0 <= value <= 4)
    for ev in entry["evidence"]:
        all_ids.append(ev["evidence_id"])
        assert ev["competency_id"] == key
        assert set(curriculum["assessment_policy"]["evidence_fields"]).issubset(ev)
        for ref in (ev["artifact_or_observation"], (ev.get("reasoning_check") or {}).get("observation_reference")):
            if ref:
                assert (ROOT / ref.split(" — ")[0]).exists(), ref
assert len(all_ids) == len(set(all_ids)) == 6
for suffix in ("s02-patch01-main.go.txt", "s02-patch02-main.go.txt", "s02-patch03-main.go.txt",
               "s02-patch01-test.txt", "s02-patch02-test.txt", "s02-patch02-test-escalated.txt",
               "s02-patch03-test.txt", "s02-direct-job-output.txt"):
    assert (ROOT / (ART + suffix)).exists(), suffix
assert (ROOT / "labs/diag-001/main.go").read_bytes() == (ROOT / (ART + "s02-patch03-main.go.txt")).read_bytes()
for name in ("main.go", "job.go"):
    if name == "job.go":
        assert (ROOT / ("labs/diag-001/" + name)).read_bytes() == (ROOT / (ART + "initial-job.go.txt")).read_bytes()
assert "PASS" in (ROOT / (ART + "s02-patch03-test.txt")).read_text(encoding="utf-8-sig")
assert CP in (ROOT / NOTES).read_text(encoding="utf-8")
assert CP in (ROOT / f"learner/sessions/{SESSION}/checkpoint.md").read_text(encoding="utf-8")
assert len(node["review_plan"]) == 2
for review in node["review_plan"]:
    assert review["scheduled_date"] == "2026-10-24" and review["status"] == "planned"
    assert all(e in all_ids for e in review["anchor_evidence_ids"])
if "--validate" in sys.argv:
    history = (ROOT / "learner/session-history.md").read_text(encoding="utf-8")
    assert history.count("### " + CP + "\n") == 1
print("PASS: state YAML, IDs, evidence/reference uniqueness, source snapshots, scores and reviews.")
print("Implementation null -> 2; concept 2; other 188 scores null; confidence low; proficiency learning.")
print("History synchronized." if "--validate" in sys.argv else "State applied; history verification pending.")
