import json

with open('scripts/cbse_9_scie_syllabus.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Chapter 0 keys:", list(data['chapters'][0].keys()))
print("Chapter 0 sample:", json.dumps(data['chapters'][0], indent=2)[:400])
