# -*- coding: utf-8 -*-
import json
import re

with open('backups/staging/mh9_scit_20_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

corrupt_b_d = 0
teacher_notes = 0

for q in qs:
    opts = q.get('options', [])
    if len(opts) >= 4:
        if opts[1] == 'None of the above' and opts[3] == 'None of the above':
            corrupt_b_d += 1
    for opt in opts:
        if 'Wrong:' in opt:
            teacher_notes += 1

print(f"Total questions: {len(qs)}")
print(f"Questions with 'None of the above' in BOTH B and D: {corrupt_b_d}")
print(f"Options with leaked teacher notes ('Wrong:'): {teacher_notes}")
