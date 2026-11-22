import json
import sys
import os

from build_cbse9_mgm_ch14_part1 import gen_14_1_1, gen_14_1_2, gen_14_1_3
from build_cbse9_mgm_ch14_part2 import gen_14_1_4, gen_14_2_1, gen_14_2_2
from build_cbse9_mgm_ch14_part3 import gen_14_2_3, gen_14_2_4, gen_14_2_5
from build_cbse9_mgm_ch14_part4 import gen_14_3_1, gen_14_3_2

def main():
    generators = [
        ("14.1.1", gen_14_1_1),
        ("14.1.2", gen_14_1_2),
        ("14.1.3", gen_14_1_3),
        ("14.1.4", gen_14_1_4),
        ("14.2.1", gen_14_2_1),
        ("14.2.2", gen_14_2_2),
        ("14.2.3", gen_14_2_3),
        ("14.2.4", gen_14_2_4),
        ("14.2.5", gen_14_2_5),
        ("14.3.1", gen_14_3_1),
        ("14.3.2", gen_14_3_2),
    ]

    all_questions = []
    print(f"Assembling Chapter 14 questions across {len(generators)} subtopics...")

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
    assert len(all_questions) == 880, f"Expected 880, got {len(all_questions)}"

    out_path = os.path.join(os.path.dirname(__file__), "clean_cbse9_mgm_ch14_questions.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(all_questions)} questions to {out_path}")

if __name__ == "__main__":
    main()
