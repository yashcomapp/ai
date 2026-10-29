# -*- coding: utf-8 -*-
import json

with open('backups/staging/mh9_scit_20_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

count = 0
for q in qs:
    opts = q.get('options', [])
    if len(opts) >= 4 and opts[1] == 'None of the above' and opts[3] == 'None of the above':
        count += 1
        if count <= 10:
            print(f"[{q['questionCode']}] ca={q.get('correctAnswer')}")
            print(f"  Q: {q.get('text')}")
            print(f"  A: {opts[0]}")
            print(f"  C: {opts[2]}")
            print(f"  Sol: {q.get('solution')}\n")

print(f"Total such questions: {count}")
