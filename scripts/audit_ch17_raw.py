import json
import re

with open('backups/staging/mh9_scit_17_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

empty_sol = 0
catch_all_opts = 0

for q in qs:
    sol = q.get('solution', '')
    if not sol or not sol.strip():
        empty_sol += 1
    opts = q.get('options', [])
    for opt in opts:
        if re.search(r'all of (these|the above)|none of (these|the above)', opt, re.I):
            catch_all_opts += 1
            print(f"[{q['questionCode']}] {opt}")
            break

print(f"Total: {len(qs)}, Empty solutions: {empty_sol}, Catch-all options: {catch_all_opts}")
