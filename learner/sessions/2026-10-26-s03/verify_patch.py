"""Instructor verification; learner source is never edited."""
from pathlib import Path
import subprocess, json, hashlib
from datetime import datetime, timezone, timedelta

root = Path(__file__).resolve().parents[3]
lab = root / 'labs/review-005'
out = lab / 'attempts/a001/artifacts/s03-o04'
out.mkdir(exist_ok=False)
source = (lab / 'main.go').read_bytes()
(out / 'main.go.txt').write_bytes(source)
fixtures = [lab/'orders.txt', lab/'jobs/A/orders.txt', lab/'jobs/B/orders.txt']
hashes = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in fixtures}
build = subprocess.run([str(root/'.local-tools/go/bin/go.exe'), 'build', '-o', 'lab.exe', '.'], cwd=lab, capture_output=True, text=True)
(out/'build.txt').write_text(build.stdout+build.stderr+f'\nexit={build.returncode}\n', encoding='utf-8')
assert build.returncode == 0, build.stderr
empty = out/'empty-workdir'
empty.mkdir()
cases = [
    ('relative-A', lab/'jobs/A', 'orders.txt', 'Impor: 3 pesanan [A-101, A-102, A-103]\n', 0),
    ('relative-B', lab/'jobs/B', 'orders.txt', 'Impor: 2 pesanan [B-201, B-202]\n', 0),
    ('absolute-A-from-B', lab/'jobs/B', str(lab/'jobs/A/orders.txt'), 'Impor: 3 pesanan [A-101, A-102, A-103]\n', 0),
    ('absolute-B-from-A', lab/'jobs/A', str(lab/'jobs/B/orders.txt'), 'Impor: 2 pesanan [B-201, B-202]\n', 0),
    ('missing-relative-no-fallback', empty, 'orders.txt', '', 1),
    ('missing-absolute', lab/'jobs/A', str(empty/'orders.txt'), '', 1),
]
results=[]
for name,cwd,arg,expected,exit_code in cases:
    p = subprocess.run([str(lab/'lab.exe'),arg],cwd=cwd,capture_output=True,text=True)
    passed = p.stdout==expected and p.returncode==exit_code
    passed = passed and (not p.stderr if exit_code==0 else p.stderr.startswith('Impor gagal:'))
    results.append(dict(case=name,cwd=str(cwd),argument=arg,stdout=p.stdout,stderr=p.stderr,exit=p.returncode,passed=passed))
report=dict(author='instructor',time=datetime.now(timezone(timedelta(hours=7))).isoformat(timespec='seconds'),build_exit=build.returncode,source_sha256=hashlib.sha256(source).hexdigest(),source_unchanged=(lab/'main.go').read_bytes()==source,fixtures_unchanged=all(hashlib.sha256((root/p).read_bytes()).hexdigest()==h for p,h in hashes.items()),cases=results,limitations=['No permission fault or unavailable-CWD injection','Instructor-created verification, not learner test implementation','No claim of domain mastery'])
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
assert report['source_unchanged'] and report['fixtures_unchanged']
assert all(r['passed'] for r in results), results
print('PASS: build; relative A/B; absolute A from B and B from A; missing relative without fallback; missing absolute. Source and fixtures unchanged.')
