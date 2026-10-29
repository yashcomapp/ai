import json

with open('backups/staging/mh9_scit_17_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

codes = [
    'MH-9-SCIT-17-17.1-OSC-054',
    'MH-9-SCIT-17-17.1-OSC-059',
    'MH-9-SCIT-17-17.1-OSC-060',
    'MH-9-SCIT-17-17.1-OSC-061',
    'MH-9-SCIT-17-17.1-OSC-062',
    'MH-9-SCIT-17-17.1-OSC-063',
    'MH-9-SCIT-17-17.1-OSC-064',
    'MH-9-SCIT-17-17.1-OSC-104',
    'MH-9-SCIT-17-17.1-OSC-105'
]

for q in qs:
    if q['questionCode'] in codes:
        print(f"=== {q['questionCode']} ===")
        print(f"Text: {q['text']}")
        print(f"Options: {q['options']}")
        print(f"Correct: {q.get('correctAnswer')}\n")
