# scripts/build_ch14_master.py
import json
import re
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

from ch14_topic1_questions import QUESTIONS as Q1
from ch14_topic2_questions import QUESTIONS as Q2
from ch14_topic3_questions import QUESTIONS as Q3
from ch14_topic4_questions import QUESTIONS as Q4

ALL_QUESTIONS = Q1 + Q2 + Q3 + Q4

print(f"Loaded {len(ALL_QUESTIONS)} questions across Chapter 14:")
print(f"  Topic 14.1: {len(Q1)} Qs")
print(f"  Topic 14.2: {len(Q2)} Qs")
print(f"  Topic 14.3: {len(Q3)} Qs")
print(f"  Topic 14.4: {len(Q4)} Qs")

errors = []
seen_codes = set()
seen_texts = set()

for idx, q in enumerate(ALL_QUESTIONS):
    code = q.get('questionCode')
    if not code:
        errors.append(f"[{idx}] Missing questionCode")
    elif code in seen_codes:
        errors.append(f"[{idx}] Duplicate questionCode: {code}")
    seen_codes.add(code)

    text = q.get('text', '').strip()
    if not text:
        errors.append(f"[{code}] Empty text")
    elif text in seen_texts:
        errors.append(f"[{code}] Duplicate text detected: {text[:40]}...")
    seen_texts.add(text)

    # Check options
    options = q.get('options', [])
    if q.get('type') in ['OSC', 'OMC']:
        if len(options) != 4:
            errors.append(f"[{code}] OSC/OMC must have exactly 4 options, found {len(options)}")
        for opt in options:
            if re.search(r'\b(none of the above|all of the above|all of above|none of these)\b', opt, re.IGNORECASE):
                errors.append(f"[{code}] Contains forbidden catch-all option: {opt}")
    elif q.get('type') == 'OTF':
        if len(options) != 2:
            errors.append(f"[{code}] OTF must have exactly 2 options, found {len(options)}")

    # Check solution
    sol = q.get('solution', '').strip()
    if not sol:
        errors.append(f"[{code}] Missing solution")
    else:
        if "**Key Concept:**" not in sol:
            errors.append(f"[{code}] Solution missing '**Key Concept:**'")
        qtype = q.get('type')
        if qtype in ['OSC', 'OMC'] and "**Option Analysis:**" not in sol:
            errors.append(f"[{code}] OSC/OMC solution missing '**Option Analysis:**'")
        elif qtype == 'OTF' and "**Statement Evaluation:**" not in sol:
            errors.append(f"[{code}] OTF solution missing '**Statement Evaluation:**'")
        elif qtype == 'OAR' and "**Assertion & Reason Analysis:**" not in sol:
            errors.append(f"[{code}] OAR solution missing '**Assertion & Reason Analysis:**'")

        # Forbidden boilerplate
        if "does not satisfy the physical conditions" in sol.lower():
            errors.append(f"[{code}] Found forbidden boilerplate phrase")

    # KaTeX delimiter matching
    for field_name, content in [('text', text), ('solution', sol)]:
        inline_open = content.count('\\(')
        inline_close = content.count('\\)')
        if inline_open != inline_close:
            errors.append(f"[{code}] Mismatched \\( ... \\) in {field_name}: {inline_open} open vs {inline_close} close")
        disp_open = content.count('\\[')
        disp_close = content.count('\\]')
        if disp_open != disp_close:
            errors.append(f"[{code}] Mismatched \\[ ... \\] in {field_name}: {disp_open} open vs {disp_close} close")

if errors:
    print(f"\n❌ FOUND {len(errors)} VALIDATION ERRORS:")
    for err in errors[:25]:
        print(f"  - {err}")
    sys.exit(1)
else:
    print("\n✅ ALL 160 QUESTIONS PASSED QUALITY VALIDATION WITH ZERO ERRORS!")

# Ensure staging dir exists
os.makedirs('backups/staging', exist_ok=True)
out_path = 'backups/staging/mh9_scit_14_enhanced.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(ALL_QUESTIONS, f, indent=2, ensure_ascii=False)

print(f"Successfully saved 160 questions to {out_path}")
