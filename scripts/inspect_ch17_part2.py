import json

with open('backups/staging/mh9_scit_17_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

for idx in range(50, len(qs)):
    q = qs[idx]
    print(f"[{idx+1}] {q['questionCode']} -> {q['text']}")
    print(f"    Options: {q['options']}")
    print(f"    Correct: {q['correctAnswer']}\n")
