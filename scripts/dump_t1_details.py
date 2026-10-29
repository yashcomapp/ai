import json

with open('backups/staging/mh9_scit_18_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

t1_qs = [q for q in qs if q.get('topicCode') == 'MH-9-SCIT-18-18.1.1']

with open('scripts/t1_details.txt', 'w', encoding='utf-8') as f:
    for q in t1_qs:
        f.write(f"=== {q['questionCode']} ({q['type']}) ===\n")
        f.write(f"Text: {q['text']}\n")
        if q.get('options'):
            for idx, opt in enumerate(q['options']):
                f.write(f"  ({chr(65+idx)}) {opt}\n")
        f.write(f"Ans: {q.get('correctAnswer')} {q.get('correctAnswers')}\n")
        f.write(f"Draft: {q.get('solution')}\n\n")

print("Dumped 18.1.1 details to scripts/t1_details.txt")
