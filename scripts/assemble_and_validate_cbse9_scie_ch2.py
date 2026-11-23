import json
from build_cbse9_scie_ch2_part1 import gen_2_1_1, gen_2_1_2, gen_2_1_3
from build_cbse9_scie_ch2_part2 import gen_2_2_1, gen_2_2_2, gen_2_2_3
from build_cbse9_scie_ch2_part3 import gen_2_3_1, gen_2_3_2, gen_2_3_3

def assemble_chapter2():
    print("Generating Part 1 (2.1.1, 2.1.2, 2.1.3)...")
    q_2_1_1 = gen_2_1_1()
    q_2_1_2 = gen_2_1_2()
    q_2_1_3 = gen_2_1_3()

    print("Generating Part 2 (2.2.1, 2.2.2, 2.2.3)...")
    q_2_2_1 = gen_2_2_1()
    q_2_2_2 = gen_2_2_2()
    q_2_2_3 = gen_2_2_3()

    print("Generating Part 3 (2.3.1, 2.3.2, 2.3.3)...")
    q_2_3_1 = gen_2_3_1()
    q_2_3_2 = gen_2_3_2()
    q_2_3_3 = gen_2_3_3()

    all_questions = (
        q_2_1_1 + q_2_1_2 + q_2_1_3 +
        q_2_2_1 + q_2_2_2 + q_2_2_3 +
        q_2_3_1 + q_2_3_2 + q_2_3_3
    )

    print(f"Total questions assembled for Chapter 2: {len(all_questions)}")
    assert len(all_questions) == 720, f"Expected 720 questions, got {len(all_questions)}"

    # Save to JSON
    out_path = 'scripts/clean_cbse9_scie_ch2_questions.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(all_questions)} questions to {out_path}")

if __name__ == '__main__':
    assemble_chapter2()
