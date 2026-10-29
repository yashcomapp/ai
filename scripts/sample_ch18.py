import json

with open('backups/staging/mh9_scit_18_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

for i in range(0, len(qs), 30):
    q = qs[i]
    print(f"[{i+1}] {q['questionCode']} ({q.get('type')}) | Topic: {q.get('topicCode')}")
    print(f"    Text: {q['text'][:80]}...")
    print(f"    Current Sol: {q.get('solution', '')[:80]}...\n")
