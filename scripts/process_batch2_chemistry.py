"""
process_batch2_chemistry.py
Transforms and validates all 388 Chemistry questions (Chapters 4, 5)
into the compact student-friendly format (**Key Concept:** + **Option Analysis:**).
"""

import json, sys
from convert_physics_chapters_compact import transform_solution

def main():
    with open('backups/staging/batch2_raw_dump.json', 'r', encoding='utf-8') as f:
        questions = json.load(f)

    print(f"Loaded {len(questions)} questions across Batch 2 (Chemistry Chapters 4, 5).")
    assert len(questions) == 388, f"Expected 388 questions, found {len(questions)}"

    transformed = []
    errors = []

    for idx, q in enumerate(questions):
        code = q.get('questionCode') or f"Q#{idx+1}"
        ans = q.get('correctAnswer')
        new_q = dict(q)
        compact_sol = transform_solution(q)
        new_q['solution'] = compact_sol
        new_q['isEnhanced'] = True

        if '**Key Concept:**' not in compact_sol:
            errors.append(f"[{code}] Missing **Key Concept:**")
        if '**Option Analysis:**' not in compact_sol:
            errors.append(f"[{code}] Missing **Option Analysis:**")
        if '### 1.' in compact_sol or '### 2.' in compact_sol or '### 3.' in compact_sol:
            errors.append(f"[{code}] Contains deprecated 3-part headers!")

        if ans not in ['A', 'B', 'C', 'D']:
            errors.append(f"[{code}] Invalid correctAnswer '{ans}'")
        elif f"({ans})" not in compact_sol or "(Correct)" not in compact_sol:
            errors.append(f"[{code}] Option Analysis does not mark ({ans}) as (Correct)")

        transformed.append(new_q)

    if errors:
        print(f"Found {len(errors)} validation errors:")
        for e in errors[:20]:
            print("  ", e)
        sys.exit(1)

    print(">>> 100% OF 388 CHEMISTRY QUESTIONS PASSED COMPACT LINTER VALIDATION! <<<")

    with open('backups/staging/mh9_scit_batch2_chemistry_compact.json', 'w', encoding='utf-8') as f:
        json.dump(transformed, f, indent=2, ensure_ascii=False)

    print("Saved to backups/staging/mh9_scit_batch2_chemistry_compact.json")

if __name__ == '__main__':
    main()
