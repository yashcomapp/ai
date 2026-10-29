import json, re

with open('backups/staging/mh9_scit_18_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

empty_sol = 0
catch_alls = []
leaked_notes = []

for q in qs:
    sol = q.get('solution', '')
    if not sol or not sol.strip():
        empty_sol += 1
    opts = q.get('options', [])
    for idx, opt in enumerate(opts):
        if re.search(r'\b(all|none) of (the |these |above|them)?\b|both [a-d] and [a-d]', opt, re.I):
            catch_alls.append((q['questionCode'], chr(65+idx), opt))
        if 'Right :' in opt or 'Wrong:' in opt:
            leaked_notes.append((q['questionCode'], chr(65+idx), opt))

print(f"Total Chapter 18 Questions: {len(qs)}")
print(f"Empty solutions: {empty_sol}")
print(f"Catch-all options: {len(catch_alls)}")
print(f"Leaked teacher notes: {len(leaked_notes)}")
