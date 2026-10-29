# -*- coding: utf-8 -*-
"""
Chapter 18 Master Assembler & Quality Gate Linter
Class 9 Science & Technology: Observing Space: Telescopes (MH-9-SCIT-18)
Total Questions: 317
"""

import json
import re
from datetime import datetime, timezone

# Load raw questions
with open('backups/staging/mh9_scit_18_raw.json', 'r', encoding='utf-8') as f:
    raw_qs = json.load(f)

# Load module solutions
with open('scripts/ch18_t1_solutions.json', 'r', encoding='utf-8') as f:
    t1_sols = json.load(f)

with open('scripts/ch18_t2_solutions.json', 'r', encoding='utf-8') as f:
    t2_sols = json.load(f)

with open('scripts/ch18_t3_solutions.json', 'r', encoding='utf-8') as f:
    t3_sols = json.load(f)

with open('scripts/ch18_t4_solutions.json', 'r', encoding='utf-8') as f:
    t4_sols = json.load(f)

all_sols = {}
all_sols.update(t1_sols)
all_sols.update(t2_sols)
all_sols.update(t3_sols)
all_sols.update(t4_sols)

print(f"Total modular solutions loaded: {len(all_sols)} / {len(raw_qs)}")

# Merge into compact questions
enhanced_qs = []
errors = []

for q in raw_qs:
    code = q['questionCode']
    if code not in all_sols:
        errors.append(f"Missing solution for {code}")
        continue

    sol = all_sols[code]
    qtype = q['type']

    # --- Quality Gate Validations ---
    # 1. Compact header check
    if "**Key Concept:**" not in sol:
        errors.append(f"{code}: Missing '**Key Concept:**'")
    if "### 1." in sol or "### 2." in sol or "### 3." in sol:
        errors.append(f"{code}: Contains legacy '### ' boilerplate headers")

    # 2. Section check
    if qtype in ['OSC', 'OMC'] and "**Option Analysis:**" not in sol:
        errors.append(f"{code}: Missing '**Option Analysis:**'")
    elif qtype == 'OTF' and "**Statement Evaluation:**" not in sol:
        errors.append(f"{code}: Missing '**Statement Evaluation:**'")
    elif qtype == 'OAR' and "**Assertion & Reason Analysis:**" not in sol:
        errors.append(f"{code}: Missing '**Assertion & Reason Analysis:**'")

    # 3. Correct marker check
    if "(Correct)" not in sol:
        errors.append(f"{code}: Missing '(Correct)' marker in solution")

    # 4. KaTeX balance check
    inline_open = sol.count(r'\(')
    inline_close = sol.count(r'\)')
    if inline_open != inline_close:
        errors.append(f"{code}: Unbalanced inline KaTeX delimiters: {inline_open} vs {inline_close}")

    disp_open = sol.count(r'\[')
    disp_close = sol.count(r'\]')
    if disp_open != disp_close:
        errors.append(f"{code}: Unbalanced display KaTeX delimiters: {disp_open} vs {disp_close}")

    # 5. Generic boilerplate phrases check
    banned_phrases = [
        "does not satisfy the physical conditions defined by the problem",
        "violates established optical principles",
        "inapplicable ray characteristic"
    ]
    for bp in banned_phrases:
        if bp in sol:
            errors.append(f"{code}: Contains banned generic boilerplate '{bp}'")

    # Clone and update
    q_copy = dict(q)
    q_copy['solution'] = sol
    q_copy['isEnhanced'] = True
    q_copy['enhancedAt'] = datetime.now(timezone.utc).isoformat()
    q_copy['updatedAt'] = datetime.now(timezone.utc).isoformat()
    enhanced_qs.append(q_copy)

print(f"\nQuality Gate Results:")
print(f"Total Enhanced Questions: {len(enhanced_qs)} / {len(raw_qs)}")
print(f"Errors Found: {len(errors)}")

if errors:
    for err in errors[:20]:
        print(f"  ERROR: {err}")
    raise SystemExit("Quality Gate Failed!")
else:
    print("ALL 317 QUESTIONS PASSED STRICT COMPACT QUALITY GATE WITH ZERO ERRORS!")

# Save to staging
out_path = 'backups/staging/mh9_scit_18_compact.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(enhanced_qs, f, indent=2, ensure_ascii=False)

print(f"\nSuccessfully wrote {len(enhanced_qs)} questions to {out_path}")
