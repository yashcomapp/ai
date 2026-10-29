# -*- coding: utf-8 -*-
"""
Chapter 15 Builder & Quality Gate Linter: Life Processes in Living Organisms (90 Qs)
"""
import json
import re
from datetime import datetime, timezone

from ch15_topic1 import solutions_topic1
from ch15_topic2 import solutions_topic2
from ch15_topic3 import solutions_topic3

# 1. Combine solutions
all_solutions = {}
all_solutions.update(solutions_topic1)
all_solutions.update(solutions_topic2)
all_solutions.update(solutions_topic3)

print(f"Total authored solutions: {len(all_solutions)}")

# 2. Load raw questions
with open('backups/staging/mh9_scit_15_raw.json', 'r', encoding='utf-8') as f:
    raw_qs = json.load(f)

print(f"Total raw questions: {len(raw_qs)}")

# 3. Verify 1-to-1 mapping
raw_codes = set(q['questionCode'] for q in raw_qs)
authored_codes = set(all_solutions.keys())

missing = raw_codes - authored_codes
extra = authored_codes - raw_codes

if missing:
    print(f"ERROR: Missing solutions for: {missing}")
if extra:
    print(f"ERROR: Extra solutions for: {extra}")

assert len(missing) == 0 and len(extra) == 0, f"Mapping mismatch: {len(missing)} missing, {len(extra)} extra"

# 4. Quality Gate Linter
errors = []
enhanced_qs = []

for q in raw_qs:
    code = q['questionCode']
    sol = all_solutions[code]
    q_type = q.get('type')
    
    # Check 1: Mandatory headers
    if '**Key Concept:**' not in sol:
        errors.append(f"[{code}] Missing '**Key Concept:**'")
    if '### 1.' in sol or '### 2.' in sol or '### 3.' in sol:
        errors.append(f"[{code}] Contains deprecated 3-step '### ' headers")
    
    # Check 2: Type-specific section header
    if q_type in ['OSC', 'OMC']:
        if '**Option Analysis:**' not in sol:
            errors.append(f"[{code}] {q_type} missing '**Option Analysis:**'")
    elif q_type == 'OTF':
        if '**Statement Evaluation:**' not in sol:
            errors.append(f"[{code}] OTF missing '**Statement Evaluation:**'")
    elif q_type == 'OAR':
        if '**Assertion & Reason Analysis:**' not in sol:
            errors.append(f"[{code}] OAR missing '**Assertion & Reason Analysis:**'")
            
    # Check 3: KaTeX balance
    open_inline = sol.count(r'\(')
    close_inline = sol.count(r'\)')
    if open_inline != close_inline:
        errors.append(f"[{code}] Unbalanced inline KaTeX delimiters: {open_inline} '\\(' vs {close_inline} '\\)'")
        
    open_disp = sol.count(r'\[')
    close_disp = sol.count(r'\]')
    if open_disp != close_disp:
        errors.append(f"[{code}] Unbalanced display KaTeX delimiters: {open_disp} '\\[' vs {close_disp} '\\]'")
        
    # Check 4: Correct option marker
    if '(Correct)' not in sol:
        errors.append(f"[{code}] Missing '(Correct)' marker")
        
    # Check 5: Banned generic filler phrases
    banned_phrases = [
        "does not satisfy the physical conditions defined by the problem",
        "violates established optical principles",
        "accurately describes the verified physical behavior",
        "None of the above",
        "All of the above",
        "Teacher Note:",
        "Teacher note:"
    ]
    for bp in banned_phrases:
        if bp.lower() in sol.lower():
            errors.append(f"[{code}] Contains banned phrase: '{bp}'")
            
    # Build enhanced doc
    enh_doc = dict(q)
    enh_doc['solution'] = sol
    enh_doc['isEnhanced'] = True
    enh_doc['enhancedAt'] = datetime.now(timezone.utc).isoformat()
    enhanced_qs.append(enh_doc)

print(f"\n--- Quality Gate Lint Results ---")
print(f"Total checked: {len(enhanced_qs)}")
print(f"Total errors: {len(errors)}")

if errors:
    for e in errors[:20]:
        print(f"  FAILED: {e}")
    if len(errors) > 20:
        print(f"  ... and {len(errors) - 20} more errors")
    raise SystemExit(1)

# Save staging output
with open('backups/staging/mh9_scit_15_compact.json', 'w', encoding='utf-8') as f:
    json.dump(enhanced_qs, f, indent=2, ensure_ascii=False)

print(f"\nSUCCESS! 90 questions written to backups/staging/mh9_scit_15_compact.json with 0 errors.")
