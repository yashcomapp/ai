import json

with open('backups/staging/mh9_scit_18_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

t1 = [q for q in qs if q.get('topicCode') == 'MH-9-SCIT-18-18.1.1']
for i, q in enumerate(t1):
    print(f"[{i+1}] {q['questionCode']} ({q.get('type')}) -> {q['text'][:70]}... Ans: {q.get('correctAnswer')} {q.get('correctAnswers')}")
