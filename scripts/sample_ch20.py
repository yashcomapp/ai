# -*- coding: utf-8 -*-
import json

with open('backups/staging/mh9_scit_20_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

for i in range(0, len(qs), 25):
    q = qs[i]
    print(f"{i+1}. [{q['questionCode']}] ca={q.get('correctAnswer')}")
    print(f"   Q: {q.get('text')}")
    print(f"   Opts: {q.get('options')}\n")
