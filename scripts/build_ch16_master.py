# -*- coding: utf-8 -*-
"""
Build Chapter 16 Master Question Bank
Chapter 16: Heredity and Variation
Target: 200 Compact Gold Standard Questions across 5 Topics (16.1 to 16.5)
"""
import json
import sys
import os

# Fix Windows console encoding
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.dirname(__file__))

import ch16_topic1_questions
import ch16_topic2_questions
import ch16_topic3_questions
import ch16_topic4_questions
import ch16_topic5_questions

def get_questions(mod):
    if hasattr(mod, 'QUESTIONS'):
        return mod.QUESTIONS
    for attr in dir(mod):
        if attr.startswith('topic_') and isinstance(getattr(mod, attr), list):
            return getattr(mod, attr)
    raise ValueError(f"Could not find questions list in {mod}")

def validate_and_assemble():
    all_questions = []
    topics = [
        ("16.1", get_questions(ch16_topic1_questions)),
        ("16.2", get_questions(ch16_topic2_questions)),
        ("16.3", get_questions(ch16_topic3_questions)),
        ("16.4", get_questions(ch16_topic4_questions)),
        ("16.5", get_questions(ch16_topic5_questions))
    ]
    
    seen_codes = set()
    errors = []
    
    for t_num, q_list in topics:
        print(f"Validating Topic {t_num}: {len(q_list)} questions...")
        if len(q_list) != 40:
            errors.append(f"Topic {t_num} has {len(q_list)} questions, expected 40!")
            
        for i, q in enumerate(q_list):
            q_code = q.get("questionCode")
            if not q_code:
                errors.append(f"Topic {t_num} Q#{i+1} missing questionCode")
            elif q_code in seen_codes:
                errors.append(f"Duplicate questionCode: {q_code}")
            seen_codes.add(q_code)
            
            # Check options
            options = q.get("options", [])
            if len(options) < 2:
                errors.append(f"{q_code}: Less than 2 options")
            for opt in options:
                opt_str = str(opt).strip().lower()
                if "none of the above" in opt_str or "all of the above" in opt_str:
                    errors.append(f"{q_code}: Forbidden catch-all option '{opt}'")
                    
            # Check solution structure
            sol = q.get("solution", "")
            if "**Key Concept:**" not in sol:
                errors.append(f"{q_code}: Missing **Key Concept:** in solution")
                
            q_type = q.get("typeCode")
            if q_type in ["OSC", "OMC"] and "**Option Analysis:**" not in sol:
                errors.append(f"{q_code}: Missing **Option Analysis:** in solution")
            elif q_type == "OTF" and "**Statement Evaluation:**" not in sol:
                errors.append(f"{q_code}: Missing **Statement Evaluation:** in solution")
            elif q_type == "OAR" and "**Assertion & Reason Analysis:**" not in sol:
                errors.append(f"{q_code}: Missing **Assertion & Reason Analysis:** in solution")
                
            # KaTeX balance check
            for field in [q.get("text", ""), sol] + [str(o) for o in options]:
                if field.count(r"\(") != field.count(r"\)"):
                    errors.append(f"{q_code}: Unbalanced KaTeX inline delimiters \\( \\)")
                if field.count(r"\[") != field.count(r"\]"):
                    errors.append(f"{q_code}: Unbalanced KaTeX display delimiters \\[ \\]")
                    
            all_questions.append(q)
            
    print(f"\nTotal assembled: {len(all_questions)} questions.")
    if errors:
        print(f"Validation FAILED with {len(errors)} errors:")
        for err in errors[:20]:
            print(f"  - {err}")
        sys.exit(1)
        
    print("All 200 questions passed 100% of format and quality checks!")
    
    out_dir = os.path.join("backups", "staging")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "mh9_scit_16_enhanced.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)
        
    print(f"Saved master file to: {out_path}")

if __name__ == "__main__":
    validate_and_assemble()
