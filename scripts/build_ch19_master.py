# -*- coding: utf-8 -*-
"""
Chapter 19 Master Assembler & Quality Gate Linter
Class 9 Science & Technology: Class 7 Science Foundation Core (MH-9-SCIT-19)
Total Questions: 245 (165 curated in 19.1 + 40 new in 19.2 + 40 new in 19.3)
"""

import json
import re
from datetime import datetime, timezone

# Load modules
with open('backups/staging/mh9_scit_19_topic1_curated.json', 'r', encoding='utf-8') as f:
    t1_qs = json.load(f)

with open('backups/staging/mh9_scit_19_topic2_new.json', 'r', encoding='utf-8') as f:
    t2_qs = json.load(f)

with open('backups/staging/mh9_scit_19_topic3_new.json', 'r', encoding='utf-8') as f:
    t3_qs = json.load(f)

all_qs = t1_qs + t2_qs + t3_qs
print(f"Total Chapter 19 Questions: {len(all_qs)} (T1: {len(t1_qs)}, T2: {len(t2_qs)}, T3: {len(t3_qs)})")

errors = []
validated_qs = []

for q in all_qs:
    code = q['questionCode']
    sol = q.get('solution', '')
    qtype = q['type']

    # 1. Header checks
    if "**Key Concept:**" not in sol:
        errors.append(f"{code}: Missing '**Key Concept:**'")
    if "### 1." in sol or "### 2." in sol or "### 3." in sol:
        errors.append(f"{code}: Contains legacy '### ' headers")

    if qtype in ['OSC', 'OMC'] and "**Option Analysis:**" not in sol:
        errors.append(f"{code}: Missing '**Option Analysis:**'")
    elif qtype == 'OTF' and "**Statement Evaluation:**" not in sol:
        errors.append(f"{code}: Missing '**Statement Evaluation:**'")
    elif qtype == 'OAR' and "**Assertion & Reason Analysis:**" not in sol:
        errors.append(f"{code}: Missing '**Assertion & Reason Analysis:**'")

    # 2. Marker check
    if "(Correct)" not in sol:
        errors.append(f"{code}: Missing '(Correct)' marker")

    # 3. Catch-all check
    for opt in q.get('options', []):
        if re.search(r'all of (the |these )?above|none of (the |these )?above|both [ab] and [bc]', opt, re.I):
            errors.append(f"{code}: Contains catch-all option '{opt}'")

    # 4. KaTeX delimiter balance
    inline_open = sol.count(r'\(')
    inline_close = sol.count(r'\)')
    if inline_open != inline_close:
        errors.append(f"{code}: Unbalanced inline KaTeX delimiters: {inline_open} vs {inline_close}")

    disp_open = sol.count(r'\[')
    disp_close = sol.count(r'\]')
    if disp_open != disp_close:
        errors.append(f"{code}: Unbalanced display KaTeX delimiters: {disp_open} vs {disp_close}")

    # Standardize metadata
    q_copy = dict(q)
    if 'id' not in q_copy:
        q_copy['id'] = code
    q_copy['isEnhanced'] = True
    q_copy['enhancedAt'] = datetime.now(timezone.utc).isoformat()
    q_copy['updatedAt'] = datetime.now(timezone.utc).isoformat()
    validated_qs.append(q_copy)

print(f"\nQuality Gate Results:")
print(f"Total Validated Questions: {len(validated_qs)}")
print(f"Errors Found: {len(errors)}")

if errors:
    for err in errors[:20]:
        print(f"  ERROR: {err}")
    raise SystemExit("Quality Gate Failed!")
else:
    print("ALL 245 QUESTIONS PASSED STRICT COMPACT QUALITY GATE WITH ZERO ERRORS!")

# Save to staging
out_path = 'backups/staging/mh9_scit_19_full_compact.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(validated_qs, f, indent=2, ensure_ascii=False)

print(f"\nSuccessfully saved {len(validated_qs)} questions to {out_path}")
