import json
import sys
import os

from build_cbse9_scie_ch1 import gen_1_1_1, gen_1_1_2, gen_1_2_1, gen_1_2_2

def main():
    generators = [
        ("1.1.1", gen_1_1_1),
        ("1.1.2", gen_1_1_2),
        ("1.2.1", gen_1_2_1),
        ("1.2.2", gen_1_2_2),
    ]

    all_questions = []
    print(f"Assembling CBSE-9-SCIE Chapter 1 questions across {len(generators)} subtopics...")

    for subtopic_num, gen_func in generators:
        qs = gen_func()
        print(f"Subtopic {subtopic_num}: {len(qs)} questions")
        assert len(qs) == 80, f"Expected 80 questions for {subtopic_num}, got {len(qs)}"
        
        # Verify vault counts
        exam_count = sum(1 for q in qs if q['vault'] == 'exam')
        practice_count = sum(1 for q in qs if q['vault'] == 'practice')
        foundation_count = sum(1 for q in qs if q['vault'] == 'foundation')
        assert exam_count == 40, f"Exam vault should be 40, got {exam_count}"
        assert practice_count == 20, f"Practice vault should be 20, got {practice_count}"
        assert foundation_count == 20, f"Foundation vault should be 20, got {foundation_count}"

        all_questions.extend(qs)

    print(f"Total questions generated: {len(all_questions)}")
    assert len(all_questions) == 320, f"Expected 320, got {len(all_questions)}"

    out_path = os.path.join(os.path.dirname(__file__), "clean_cbse9_scie_ch1_questions.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(all_questions)} questions to {out_path}")

if __name__ == "__main__":
    main()
