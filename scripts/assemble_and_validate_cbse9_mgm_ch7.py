# scripts/assemble_and_validate_cbse9_mgm_ch7.py
import json
import os
import sys
sys.path.insert(0, os.path.abspath("."))

from scripts.build_cbse9_mgm_ch7_part1 import gen_7_1_1, gen_7_1_2
from scripts.build_cbse9_mgm_ch7_part2 import gen_7_2_1, gen_7_2_2, gen_7_2_3
from scripts.build_cbse9_mgm_ch7_part3 import gen_7_3_1, gen_7_3_2

def main():
    print("=== ASSEMBLING CBSE-9-MGM CHAPTER 7 QUESTIONS ===")
    all_qs = []
    generators = [
        ("7.1.1", gen_7_1_1),
        ("7.1.2", gen_7_1_2),
        ("7.2.1", gen_7_2_1),
        ("7.2.2", gen_7_2_2),
        ("7.2.3", gen_7_2_3),
        ("7.3.1", gen_7_3_1),
        ("7.3.2", gen_7_3_2),
    ]

    for code, gen_fn in generators:
        qs = gen_fn()
        print(f"Subtopic {code}: generated {len(qs)} questions")
        assert len(qs) == 80, f"Expected 80 questions for {code}, got {len(qs)}"

        # Check vaults
        exam_qs = [q for q in qs if q.get('vault') == 'exam']
        practice_qs = [q for q in qs if q.get('vault') == 'practice']
        foundation_qs = [q for q in qs if q.get('vault') == 'foundation']
        print(f"   Exam: {len(exam_qs)}, Practice: {len(practice_qs)}, Foundation: {len(foundation_qs)}")
        assert len(exam_qs) == 40
        assert len(practice_qs) == 20
        assert len(foundation_qs) == 20

        all_qs.extend(qs)

    print(f"\nTotal questions generated for Chapter 7: {len(all_qs)}")
    assert len(all_qs) == 560, f"Expected 560 questions, got {len(all_qs)}"

    # Validate distinct IDs
    qcodes = [q['questionCode'] for q in all_qs]
    assert len(qcodes) == len(set(qcodes)), "Duplicate questionCodes found!"

    out_file = "scripts/clean_cbse9_mgm_ch7_questions.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved {len(all_qs)} questions to {out_file}")

if __name__ == "__main__":
    main()
