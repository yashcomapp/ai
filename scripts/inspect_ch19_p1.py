# -*- coding: utf-8 -*-
import json

with open('backups/staging/mh9_scit_19_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

with open('scripts/ch19_p1_sample.txt', 'w', encoding='utf-8') as out:
    for q in qs[:45]:
        out.write(f"[{q['questionCode']}] ca={q.get('correctAnswer')}\n")
        out.write(f"  Q: {q.get('text')}\n")
        for i, opt in enumerate(q.get('options', [])):
            out.write(f"    ({chr(65+i)}) {opt}\n")
        out.write("\n")
print("Done writing sample.")
