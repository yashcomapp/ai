# scripts/assemble_and_validate_cbse9_mgm_ch2.py
import json, sys, os

sys.path.insert(0, os.path.abspath("."))
from scripts.build_cbse9_mgm_ch2_part1 import gen_2_1_1, gen_2_1_2
from scripts.build_cbse9_mgm_ch2_part2 import gen_2_2_1, gen_2_2_2
from scripts.build_cbse9_mgm_ch2_part3 import gen_2_3_1, gen_2_3_2

print("=== ASSEMBLING AND VALIDATING CBSE-9-MGM CHAPTER 2 (480 QUESTIONS) ===")

subtopics = [
    ("CBSE-9-MGM-2-2.1.1", gen_2_1_1),
    ("CBSE-9-MGM-2-2.1.2", gen_2_1_2),
    ("CBSE-9-MGM-2-2.2.1", gen_2_2_1),
    ("CBSE-9-MGM-2-2.2.2", gen_2_2_2),
    ("CBSE-9-MGM-2-2.3.1", gen_2_3_1),
    ("CBSE-9-MGM-2-2.3.2", gen_2_3_2),
]

all_questions = []
seen_qcodes = set()

for tc, gen_fn in subtopics:
    qs = gen_fn()
    print(f"Subtopic {tc}: generated {len(qs)} questions")
    assert len(qs) == 80, f"Expected 80 questions for {tc}, got {len(qs)}"

    # Audit vault counts
    counts = {'exam': 0, 'practice': 0, 'foundation': 0}
    for q in qs:
        # Check uniqueness of questionCode
        qc = q['questionCode']
        assert qc not in seen_qcodes, f"Duplicate questionCode: {qc}"
        seen_qcodes.add(qc)

        # Check options
        opts = q['options']
        assert len(opts) == 4, f"{qc}: must have 4 options, got {len(opts)}"
        opt_texts = [o['text'].strip() for o in opts]
        assert len(set(opt_texts)) == 4, f"{qc}: options must be distinct, got {opt_texts}"
        
        corr_opts = [o for o in opts if o.get('isCorrect') is True]
        assert len(corr_opts) == 1, f"{qc}: exactly 1 correct option, got {len(corr_opts)}"
        assert corr_opts[0]['id'] == q['correctAnswer'], f"{qc}: correctAnswer mismatch ({corr_opts[0]['id']} vs {q['correctAnswer']})"

        # Check solution
        sol = q.get('solution', '')
        assert "Step 1:" in sol and "Step 2:" in sol and "Step 3:" in sol, f"{qc}: solution missing 3 steps: {sol}"

        # Count vault
        v = q['vault']
        counts[v] += 1

    assert counts['exam'] == 40, f"{tc}: expected 40 exam, got {counts['exam']}"
    assert counts['practice'] == 20, f"{tc}: expected 20 practice, got {counts['practice']}"
    assert counts['foundation'] == 20, f"{tc}: expected 20 foundation, got {counts['foundation']}"
    print(f"  -> Vault counts verified: 40 Exam, 20 Practice, 20 Foundation. 100% compliant.")

    all_questions.extend(qs)

print(f"\nTotal assembled questions: {len(all_questions)}")
assert len(all_questions) == 480, f"Expected 480 questions, got {len(all_questions)}"

out_path = "scripts/clean_cbse9_mgm_ch2_questions.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)
print(f"Saved to {out_path} ({os.path.getsize(out_path)} bytes)")

print("\n=== RUNNING QUESTION_VALIDATOR.JS AGAINST CH2 QUESTIONS ===")
import subprocess
res = subprocess.run(["node", "scripts/question_validator.js", out_path], capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print("STDERR:", res.stderr)
assert res.returncode == 0, f"question_validator.js failed with code {res.returncode}"
print("All 480 questions in Chapter 2 validated with 0 errors!")
