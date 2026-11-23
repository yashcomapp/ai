import json
from build_cbse9_scie_ch3_part1 import gen_3_1_1, gen_3_1_2, gen_3_1_3
from build_cbse9_scie_ch3_part2 import gen_3_2_1, gen_3_2_2
from build_cbse9_scie_ch3_part3 import gen_3_3_1, gen_3_3_2, gen_3_3_3, gen_3_3_4

def assemble_chapter3():
    print("Generating Part 1 (3.1.1, 3.1.2, 3.1.3)...")
    q_3_1_1 = gen_3_1_1()
    q_3_1_2 = gen_3_1_2()
    q_3_1_3 = gen_3_1_3()

    print("Generating Part 2 (3.2.1, 3.2.2)...")
    q_3_2_1 = gen_3_2_1()
    q_3_2_2 = gen_3_2_2()

    print("Generating Part 3 (3.3.1, 3.3.2, 3.3.3, 3.3.4)...")
    q_3_3_1 = gen_3_3_1()
    q_3_3_2 = gen_3_3_2()
    q_3_3_3 = gen_3_3_3()
    q_3_3_4 = gen_3_3_4()

    all_questions = (
        q_3_1_1 + q_3_1_2 + q_3_1_3 +
        q_3_2_1 + q_3_2_2 +
        q_3_3_1 + q_3_3_2 + q_3_3_3 + q_3_3_4
    )

    print(f"Total questions assembled for Chapter 3: {len(all_questions)}")
    assert len(all_questions) == 720, f"Expected 720 questions, got {len(all_questions)}"

    # Save to clean JSON
    out_path = 'scripts/clean_cbse9_scie_ch3_questions.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(all_questions)} questions to {out_path}")

if __name__ == '__main__':
    assemble_chapter3()
