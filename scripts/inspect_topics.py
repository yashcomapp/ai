# -*- coding: utf-8 -*-
import json

with open('backups/staging/mh9_scit_18_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

for code in ['18.1.1', '18.2.1', '18.2.2', '18.3.1', '18.4.1', '18.4.2']:
    sub = [q for q in qs if f'-{code}' in q['questionCode']]
    print(f"=== Topic {code} ({len(sub)} Qs) ===")
    types = {}
    for q in sub:
        t = q['type']
        types[t] = types.get(t, 0) + 1
    print("Types:", types)
