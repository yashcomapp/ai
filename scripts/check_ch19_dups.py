# -*- coding: utf-8 -*-
import json
from collections import defaultdict

with open('backups/staging/mh9_scit_19_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

texts = defaultdict(list)
for q in qs:
    clean_t = ' '.join(q['text'].lower().split())
    texts[clean_t].append(q['questionCode'])

dups = {k: v for k, v in texts.items() if len(v) > 1}
print(f"Duplicate question texts: {len(dups)}")
for k, v in list(dups.items())[:15]:
    print(f"  '{k[:60]}': {v}")
