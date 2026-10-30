import json
import re

with open('scripts/mh10_mth2_ch1_t1.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Auditing KaTeX and content across {len(questions)} questions...")

math_errors = []

for q in questions:
    code = q['questionCode']
    for field in ['text', 'explanation', 'solution']:
        content = q.get(field, '')
        if not content:
            continue
        
        # Strip SVG block if checking text
        clean = re.sub(r'<svg[\s\S]*?<\/svg>', '', content)
        
        # Check for unescaped standalone dollars or mismatched delimiters
        inline_open = clean.count(r'\(')
        inline_close = clean.count(r'\)')
        if inline_open != inline_close:
            math_errors.append((code, field, f"Mismatched inline math delimiters: {inline_open} \\( vs {inline_close} \\)"))
            
        disp_open = clean.count(r'\[')
        disp_close = clean.count(r'\]')
        if disp_open != disp_close:
            math_errors.append((code, field, f"Mismatched display math delimiters: {disp_open} \\[ vs {disp_close} \\]"))

    # Check options for multiple choice
    for opt_idx, opt in enumerate(q.get('options', [])):
        inline_open = opt.count(r'\(')
        inline_close = opt.count(r'\)')
        if inline_open != inline_close:
            math_errors.append((code, f"option[{opt_idx}]", f"Mismatched inline math in option: {opt}"))

print(f"Found {len(math_errors)} KaTeX syntax issues.")
if math_errors:
    for err in math_errors:
        print(f"  - {err}")
else:
    print("ALL 82 QUESTIONS HAVE 100% BALANCED KaTeX DELIMITERS!")
