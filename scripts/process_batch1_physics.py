"""
process_batch1_physics.py
Validates and generates the compact format for all 819 Physics questions (Chapters 1, 2, 3, 11, 12).
"""

import json, sys
from convert_physics_chapters_compact import transform_solution

def main():
    with open('backups/staging/batch1_raw_dump.json', 'r', encoding='utf-8') as f:
        questions = json.load(f)

    print(f"Loaded {len(questions)} questions across Batch 1 (Physics Chapters 1, 2, 3, 11, 12).")
    assert len(questions) == 819, f"Expected 819 questions, found {len(questions)}"

    transformed = []
    errors = []

    for idx, q in enumerate(questions):
        code = q.get('questionCode') or f"Q#{idx+1}"
        q_type = q.get('type', 'OSC')
        ans = q.get('correctAnswer')
        new_q = dict(q)
        compact_sol = transform_solution(q)
        new_q['solution'] = compact_sol
        new_q['isEnhanced'] = True

        # Structure checks
        if '**Key Concept:**' not in compact_sol:
            errors.append(f"[{code}] Missing **Key Concept:**")
        if '### 1.' in compact_sol or '### 2.' in compact_sol or '### 3.' in compact_sol:
            errors.append(f"[{code}] Contains deprecated 3-part headers!")

        if q_type == 'OTF':
            if '**Statement Evaluation:**' not in compact_sol:
                errors.append(f"[{code}] OTF missing **Statement Evaluation:**")
            if '(Correct)' not in compact_sol:
                errors.append(f"[{code}] OTF missing (Correct)")
        elif q_type == 'OAR':
            if '**Assertion & Reason Analysis:**' not in compact_sol:
                errors.append(f"[{code}] OAR missing **Assertion & Reason Analysis:**")
            if '(Correct)' not in compact_sol:
                errors.append(f"[{code}] OAR missing (Correct)")
        elif q_type == 'OMC':
            if '**Option Analysis:**' not in compact_sol:
                errors.append(f"[{code}] OMC missing **Option Analysis:**")
            if '(Correct)' not in compact_sol:
                errors.append(f"[{code}] OMC missing (Correct)")
        else: # OSC
            if '**Option Analysis:**' not in compact_sol:
                errors.append(f"[{code}] OSC missing **Option Analysis:**")
            if ans not in ['A', 'B', 'C', 'D']:
                errors.append(f"[{code}] Invalid correctAnswer '{ans}'")
            elif f"({ans})" not in compact_sol or "(Correct)" not in compact_sol:
                errors.append(f"[{code}] OSC Option Analysis does not mark ({ans}) as (Correct)")

        transformed.append(new_q)

    if errors:
        print(f"Found {len(errors)} validation errors:")
        for e in errors[:20]:
            print("  ", e)
        sys.exit(1)

    print(">>> 100% OF 819 PHYSICS QUESTIONS PASSED COMPACT LINTER VALIDATION! <<<")

    with open('backups/staging/mh9_scit_batch1_physics_compact.json', 'w', encoding='utf-8') as f:
        json.dump(transformed, f, indent=2, ensure_ascii=False)

    print("Saved to backups/staging/mh9_scit_batch1_physics_compact.json")

if __name__ == '__main__':
    main()
