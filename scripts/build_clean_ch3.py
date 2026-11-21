import json
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import build_clean_ch3_p1 as p1
import build_clean_ch3_p2 as p2

def main():
    print("Building Chapter 3 (10 subtopics, 800 questions)...")
    subtopics = [
        p1.gen_3_1_1,
        p1.gen_3_2_1,
        p1.gen_3_2_2,
        p1.gen_3_3_1,
        p1.gen_3_3_2,
        p2.gen_3_3_3,
        p2.gen_3_4_1,
        p2.gen_3_4_2,
        p2.gen_3_5_1,
        p2.gen_3_5_2
    ]
    
    all_questions = []
    for fn in subtopics:
        qs = fn()
        all_questions.extend(qs)
        print(f"Generated {len(qs)} for {qs[0]['topicCode']}")
    
    out_path = "scripts/mh9_mth2_ch3_perfect.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    
    print(f"SUCCESS: Saved {len(all_questions)} questions to {out_path}")

if __name__ == '__main__':
    main()
