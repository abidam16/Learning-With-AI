"""Instructor setup only: fresh retrieval fixture; never edits older attempts."""
from pathlib import Path
import subprocess, json, sys
sys.path.insert(0, r'C:/Users/abid.mahdy/AppData/Local/Temp/learning-lab-yaml-validation')
import yaml

root = Path(__file__).resolve().parents[3]
lab = root / 'labs/review-005'
lab.mkdir(exist_ok=False)
def write(name, text):
    p = lab / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding='utf-8')

source = '''package main

import (
    "fmt"
    "os"
    "path/filepath"
    "strings"
)

func run(args []string) int {
    if len(args) != 1 {
        fmt.Fprintln(os.Stderr, "Pemakaian: lab.exe <file-pesanan>")
        return 2
    }
    executable, err := os.Executable()
    if err != nil {
        fmt.Fprintln(os.Stderr, err)
        return 1
    }
    input := args[0]
    if !filepath.IsAbs(input) {
        input = filepath.Join(filepath.Dir(executable), input)
    }
    data, err := os.ReadFile(input)
    if err != nil {
        fmt.Fprintln(os.Stderr, "Impor gagal:", err)
        return 1
    }
    orders := strings.Fields(string(data))
    fmt.Printf("Impor: %d pesanan [%s]\\n", len(orders), strings.Join(orders, ", "))
    return 0
}

func main() { os.Exit(run(os.Args[1:])) }
'''
write('main.go', source)
write('go.mod', 'module learning/review005\n\ngo 1.26.0\n')
write('orders.txt', 'DEMO-01\n')
write('jobs/A/orders.txt', 'A-101\nA-102\nA-103\n')
write('jobs/B/orders.txt', 'B-201\nB-202\n')
write('README.md', '''# Review 005 — Impor kiriman

Mode: retrieval mandiri; mulai dengan hipotesis sebelum inspeksi atau perubahan.

Sebuah alat menerima satu argumen nama file pesanan. Operator A dan B menjalankannya dari folder kerja masing-masing. Keduanya melaporkan sukses, tetapi pesanan yang ditampilkan bukan milik mereka.

Kontrak: argumen relatif menunjuk file dari folder terminal saat perintah dijalankan; argumen absolut menunjuk file tersebut langsung. File contoh yang disertakan bersama aplikasi tidak boleh menggantikan pilihan operator. Bila file pilihan tidak ada, laporkan gagal dengan exit nonzero. Jangan ubah fixture, menyalin data untuk mengakali kasus, atau hardcode folder A/B. Area perubahan: main.go.

## Peluncuran yang dilaporkan

A:
```powershell
Set-Location D:\\learning\\Learning-With-AI\\labs\\review-005\\jobs\\A
..\\..\\lab.exe orders.txt
$LASTEXITCODE
```

B:
```powershell
Set-Location D:\\learning\\Learning-With-AI\\labs\\review-005\\jobs\\B
..\\..\\lab.exe orders.txt
$LASTEXITCODE
```

Harapan A: A-101, A-102, A-103. Harapan B: B-201, B-202.
Observasi instructor untuk keduanya: `Impor: 1 pesanan [DEMO-01]`, exit 0.

Sebelum membuka source atau menjalankan command: apa satu hipotesis yang menjelaskan mengapa kedua operator mendapatkan DEMO-01?

Sesudah prediksi awal, learner memilih satu eksperimen pembeda; source tersedia untuk inspeksi. Setelah diagnosis, learner menulis patch. Keberhasilan mencakup bukti penyebab, hasil A/B yang benar, argumen absolut, kegagalan file hilang, dan penjelasan pada satu kondisi baru.

Build dari folder lab:
```powershell
& ..\\..\\.local-tools\\go\\bin\\go.exe build -o lab.exe .
```
''')
metadata = {
    'lab_id':'review-005', 'task_variant':'operator-input-selection-v1',
    'task_type':'delayed_retrieval', 'mode':'independent_diagnostic',
    'curriculum_version':'1.1.0', 'session_id':'2026-10-26-s03',
    'primary_competency_ids':['os.files-and-descriptors'], 'target_axes':['concept','debugging'],
    'prerequisites':[], 'difficulty':1, 'initial_hint':'H0', 'suggested_minutes':40,
    'review_id':'2026-10-23-s01-r01', 'retest_of':['2026-10-23-s01-e02','2026-10-23-s01-e03'],
    'selection_rationale':'No unfinished work. Due path review; vary subject after two process reviews today. Process implementation review remains due.',
    'prior_exposure':'October 23 package-relative data task with concept H1, diagnostic/API H5, final launch-path explanation H4. New contract is caller-selected input, not package data. Prompt states business contract but does not name fault or API remedy.',
    'environment':{'runtime':'Go 1.26.0 Windows amd64','build':'../../.local-tools/go/bin/go.exe build -o lab.exe .','baseline':'attempts/a001/artifacts/baseline.json','limits':'Deterministic text files; permissions and descriptors not tested.'},
    'constraints':['Learner authors target repair','No fixture changes or hardcoded locations','Prediction before inspection; one-variable experiment where practical'],
    'success_criteria':['Explain evidence for wrong selected data','A/B exact IDs correct','Absolute input works','Missing selected input returns nonzero without success','Explain a changed launch condition'],
    'verification_plan':[
        {'axis':'concept','check_type':'prediction','observable_evidence':'Predict which input is selected under changed launch conditions and explain causal path','assistance_boundary':'H0 initially; record exposure and hints per axis'},
        {'axis':'debugging','check_type':'discriminating_experiment','observable_evidence':'Learner chooses one observation with predicted supporting/refuting results then reconciles runtime evidence','limitations':'Instructor infrastructure is not learner test-design evidence; API help separately recorded'}],
    'difficulty_context':{'concept_novelty':'Previously taught path anchors; changed input ownership contract','integration_scope':'One executable and two operator directories','failure_complexity':'One deterministic wrong-data fault','scaffolding':'CLI, fixtures and executable supplied; no repaired reference','constraints':'Relative and absolute input; missing input must fail','tooling_familiarity':'Familiar PowerShell/Go; API recall not assumed'}
}
write('lab.yaml', json.dumps(metadata, indent=2)+'\n')
go = root / '.local-tools/go/bin/go.exe'
build = subprocess.run([str(go),'build','-o','lab.exe','.'],cwd=lab,capture_output=True,text=True)
assert build.returncode == 0, build.stderr
results = []
for name,cwd,arg in [('A',lab/'jobs/A','orders.txt'),('B',lab/'jobs/B','orders.txt'),('absolute',root,str(lab/'jobs/A/orders.txt')),('missing',lab/'jobs/A','absent.txt')]:
    p = subprocess.run([str(lab/'lab.exe'),arg],cwd=cwd,capture_output=True,text=True)
    results.append(dict(case=name,cwd=str(cwd),argument=arg,stdout=p.stdout,stderr=p.stderr,exit=p.returncode))
assert all(r['stdout']=='Impor: 1 pesanan [DEMO-01]\n' and r['exit']==0 for r in results[:2])
assert results[2]['stdout']=='Impor: 3 pesanan [A-101, A-102, A-103]\n' and results[2]['exit']==0
assert results[3]['exit']==1 and not results[3]['stdout']
write('attempts/a001/artifacts/starter-main.go.txt', source)
write('attempts/a001/artifacts/baseline.json',json.dumps({'author':'instructor','build_exit':build.returncode,'cases':results},indent=2)+'\n')
write('attempts/a001/notes.md', '''# review-005 / a001

## 2026-10-26-s03 startup
- Resumed completed checkpoint 2026-10-26-s02-cp01; no unfinished code. New due retrieval variant.
- Initial hypothesis prompt in README; response pending. No learner evidence or assessment changes yet.
- Baseline build and four runs verified by instructor; original attempts untouched. H0 task presentation; previously taught path concepts recorded in lab.yaml.
- learner_feedback: 60-minute availability; challenge/frustration unknown.
- calibration_decision: maintain difficulty 1; changed input ownership is dominant challenge. Next check is learner hypothesis and chosen observation.
''')
state = yaml.safe_load((root/'learner/competency-state.yaml').read_text(encoding='utf-8'))
curriculum = yaml.safe_load((root/'curriculum/competency-map.yaml').read_text(encoding='utf-8'))
assert state['last_applied_checkpoint']=='2026-10-26-s02-cp01' and state['active_work'] is None
assert set(state['competencies'])==set(curriculum['competencies'])
assert set(metadata['primary_competency_ids']) <= set(curriculum['competencies'])
assert yaml.safe_load((lab/'lab.yaml').read_text())==metadata
print('PASS: new fixture build and four baselines; map/state/lab parse, 38 IDs match. Assessment state unchanged.')
