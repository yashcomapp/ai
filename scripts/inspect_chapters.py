import json

with open('scripts/cbse_9_scie_syllabus.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for ch in data['chapters']:
    print(f"Ch {ch.get('chapterNumber')} ({type(ch.get('chapterNumber'))}): {ch.get('chapterName')}")
