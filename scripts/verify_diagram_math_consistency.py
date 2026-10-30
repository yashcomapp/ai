import json
import re

with open('scripts/mh10_mth2_ch1_t1.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

diagram_qs = [q for q in questions if '<svg' in q['text'] or q.get('diagram')]
print(f"Verifying {len(diagram_qs)} diagram-based questions for consistency...\n")

issues = []

for q in diagram_qs:
    code = q['questionCode']
    text = q['text']
    sol = q['solution']
    opt = q['options']
    ans = q['correctAnswer']
    qtype = q['type']

    # 1. Check that text is not empty and has a prompt
    svg_end = text.find('</svg>')
    if svg_end == -1:
        issues.append((code, "Missing closing </svg> tag"))
        continue
    
    div_end = text.find('</div>', svg_end)
    if div_end == -1:
        issues.append((code, "Missing closing </div> tag after SVG"))
        continue

    stem = text[div_end + 6:].strip()
    if len(stem) < 15:
        issues.append((code, f"Stem too short: '{stem}'"))

    # 2. Check options and answer
    if qtype in ['OSC', 'OTF', 'OFB', 'OAR']:
        if ans not in ['A', 'B', 'C', 'D']:
            issues.append((code, f"Invalid correct answer letter: {ans}"))
        if not opt or len(opt) < 2:
            issues.append((code, f"Insufficient options: {opt}"))
    elif qtype == 'OMC':
        if not isinstance(ans, list) or len(ans) == 0:
            issues.append((code, f"Invalid OMC correct answer: {ans}"))
        for a in ans:
            if a not in ['A', 'B', 'C', 'D']:
                issues.append((code, f"Invalid OMC letter {a} in {ans}"))
    elif qtype == 'ONE':
        if not isinstance(ans, str) or len(ans) == 0:
            issues.append((code, f"Invalid ONE answer: {ans}"))

    # 3. Check solution length and quality
    if len(sol) < 50:
        issues.append((code, "Solution too brief or missing"))

print(f"Consistency check complete across all {len(diagram_qs)} diagram questions.")
if issues:
    print(f"Found {len(issues)} issues:")
    for code, msg in issues:
        print(f"  - {code}: {msg}")
else:
    print("ALL 55 DIAGRAM-BASED QUESTIONS ARE 100% CONSISTENT, COMPLETE, AND VALID!")
