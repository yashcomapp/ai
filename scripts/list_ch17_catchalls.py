import json, re

with open('backups/staging/mh9_scit_17_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

for q in qs:
    opts = q.get('options', [])
    for idx, opt in enumerate(opts):
        if re.search(r'\b(all|none) of (the |these |above|them)?\b|both [a-d] and [a-d]', opt, re.I):
            print(f"Code: {q['questionCode']} | CorrectAns: {q.get('correctAnswer')} | Type: {q.get('type')}")
            print(f"Text: {q.get('text')}")
            print(f"Options: {opts}")
            print("---")
            break
