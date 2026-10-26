"""Instructor verification infrastructure; never modifies learner source."""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
fixture_only = '--fixture' in sys.argv
build = subprocess.run(['go', 'build', '-o', 'lab.exe', '.'], cwd=ROOT, capture_output=True, text=True)
if build.returncode:
    print(build.stdout + build.stderr)
    sys.exit(build.returncode)

if fixture_only:
    cases = [
        (['--step', 'prepare', 'ok'], 0, ['prepare: started', 'prepare: done']),
        (['--step', 'publish', 'ok'], 0, ['publish: started', 'publish: done']),
        (['--step', 'prepare', 'reject'], 7, ['prepare: started']),
        (['--step', 'publish', 'publish-reject'], 9, ['publish: started']),
    ]
    assert not (ROOT / 'absent-worker' / 'worker.exe').exists()
else:
    cases = [
        (['ok'], 0, ['prepare: started', 'prepare: done', 'publish: started', 'publish: done', 'Batch: selesai']),
        (['reject'], 1, ['prepare: started']),
        (['publish-reject'], 1, ['prepare: started', 'prepare: done', 'publish: started']),
        (['unavailable'], 1, []),
    ]

records = []
for args, code, stdout_lines in cases:
    actual = subprocess.run([str(ROOT / 'lab.exe'), *args], cwd=ROOT, capture_output=True, text=True, timeout=10)
    records.append(dict(args=args, exit_code=actual.returncode, stdout=actual.stdout,
                        stderr=actual.stderr, expected_exit=code,
                        passed=actual.returncode == code and actual.stdout.splitlines() == stdout_lines))
print(json.dumps(dict(build_exit=build.returncode, fixture_only=fixture_only, results=records), indent=2))
sys.exit(0 if all(r['passed'] for r in records) else 1)
