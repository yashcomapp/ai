# -*- coding: utf-8 -*-
import json

with open('backups/staging/mh9_scit_20_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

with open('scripts/m1_sample.txt', 'w', encoding='utf-8') as out:
    for q in qs[:35]:
        out.write(f"[{q['questionCode']}] ca={q.get('correctAnswer')}\n")
        out.write(f"  Q: {q.get('text')}\n")
        for i, o in enumerate(q.get('options', [])):
            out.write(f"    ({chr(65+i)}) {o}\n")
        out.write("\n")
print("Wrote m1_sample.txt")
