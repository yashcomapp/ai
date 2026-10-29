# -*- coding: utf-8 -*-
import json
import re

with open('backups/staging/mh9_scit_19_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

print("=== All Catch-All Options in Chapter 19 ===")
for q in qs:
    for i, opt in enumerate(q.get('options', [])):
        if re.search(r'all of (the |these )?above|none of (the |these )?above|both [ab] and [bc]', opt, re.I):
            letter = chr(65 + i)
            is_ca = (q.get('correctAnswer') == letter or q.get('correctAnswer') == opt)
            print(f"[{q['questionCode']}] ({letter}) '{opt}' -> is_correct={is_ca} | Q: {q.get('text')[:75]}")
