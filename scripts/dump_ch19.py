# -*- coding: utf-8 -*-
import json

with open('backups/staging/mh9_scit_19_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

with open('scripts/ch19_questions_dump.txt', 'w', encoding='utf-8') as f:
    for q in qs:
        f.write(f"{q['questionCode']} | ca={q.get('correctAnswer')} | sol_len={len(q.get('solution') or '')}\n")
        f.write(f"  Q: {q.get('text')}\n")
        for i, opt in enumerate(q.get('options', [])):
            f.write(f"    ({chr(65+i)}) {opt}\n")
        f.write('\n')

print(f"Dumped {len(qs)} questions to scripts/ch19_questions_dump.txt")
