# scripts/assemble_and_validate_scit_ch10.py
import json, sys, os

sys.path.insert(0, os.path.abspath("."))
from scripts.build_clean_scit_ch10 import gen_10_1_1
from scripts.build_clean_scit_ch10_part2 import gen_10_1_2, gen_10_2_1
from scripts.build_clean_scit_ch10_part3 import gen_10_2_2, gen_10_3_1, gen_10_3_2

print("=== ASSEMBLING AND VALIDATING MH-9-SCIT CHAPTER 10 (480 QUESTIONS) ===")

subtopics = [
    ("MH-9-SCIT-10-10.1.1", gen_10_1_1),
    ("MH-9-SCIT-10-10.1.2", gen_10_1_2),
    ("MH-9-SCIT-10-10.2.1", gen_10_2_1),
    ("MH-9-SCIT-10-10.2.2", gen_10_2_2),
    ("MH-9-SCIT-10-10.3.1", gen_10_3_1),
    ("MH-9-SCIT-10-10.3.2", gen_10_3_2),
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
        if q['questionCode'] in seen_qcodes:
            raise ValueError(f"Duplicate questionCode: {q['questionCode']}")
        seen_qcodes.add(q['questionCode'])

        # Check options
        opts = q.get('options', [])
        if len(opts) != 4:
            raise ValueError(f"Question {q['questionCode']} options length != 4: {len(opts)}")
        
        opt_texts = set()
        correct_count = 0
        correct_letter = None
        for opt in opts:
            ot = opt['text'].strip()
            if not ot:
                raise ValueError(f"Empty option text in {q['questionCode']}")
            if ot in opt_texts:
                raise ValueError(f"Duplicate option text '{ot}' in {q['questionCode']}")
            opt_texts.add(ot)
            if opt['isCorrect']:
                correct_count += 1
                correct_letter = opt['id']

        if correct_count != 1:
            raise ValueError(f"Question {q['questionCode']} has {correct_count} correct options, expected 1")
        if q['correctAnswer'] != correct_letter:
            raise ValueError(f"Question {q['questionCode']} correctAnswer mismatch: {q['correctAnswer']} vs {correct_letter}")

        # Check solution
        sol = q.get('solution', '')
        if len(sol) < 20:
            raise ValueError(f"Question {q['questionCode']} has short solution: {sol}")

        # Track vault
        v = q['vault']
        counts[v] += 1
        all_questions.append(q)

    assert counts['exam'] == 40, f"{tc} exam count = {counts['exam']}"
    assert counts['practice'] == 20, f"{tc} practice count = {counts['practice']}"
    assert counts['foundation'] == 20, f"{tc} foundation count = {counts['foundation']}"
    print(f"  -> Vault Check PASSED: 40 Exam, 20 Practice, 20 Foundation.")

print(f"\nTotal Validated Questions: {len(all_questions)}")
assert len(all_questions) == 480, f"Expected exactly 480 questions, got {len(all_questions)}"

output_path = os.path.join(os.path.dirname(__file__), "mh9_scit_ch10_all_480.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Successfully saved all 480 questions to: {output_path}")
