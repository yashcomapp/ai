import json, re

with open('backups/staging/mh9_scit_12_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

print(f"Scanning {len(qs)} questions for catch-alls and notes...")
issues = []
for idx, q in enumerate(qs):
    code = q.get('questionCode')
    opts = q.get('options', [])
    ans = q.get('correctAnswer')
    bad = []
    for oi, opt in enumerate(opts):
        s = str(opt).lower()
        if 'none of' in s or 'none above' in s or 'all of above' in s or 'all of the above' in s or 'all the above' in s or 'all of these' in s or 'none of these' in s:
            bad.append((oi, chr(65+oi), opt))
        if 'wrong:' in s or 'right:' in s or 'wrong :' in s or 'right :' in s:
            bad.append((oi, chr(65+oi), opt))
        if 'option ' in s:
            bad.append((oi, chr(65+oi), opt))
    if bad:
        issues.append((idx+1, code, ans, q.get('text'), bad, opts))

print(f"Found {len(issues)} questions with issues.")
for item in issues:
    print(f"\n[#{item[0]}] {item[1]} (Ans: {item[2]})")
    print(f"  Q: {item[3]}")
    print(f"  Bad options: {item[4]}")
    print(f"  All options: {item[5]}")
