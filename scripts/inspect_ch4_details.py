import json

with open('scripts/cbse_9_scie_syllabus.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for ch in data['chapters']:
    if str(ch.get('number')) == '4':
        print(f"Chapter {ch.get('number')}: {ch.get('name')}")
        for top in ch.get('topics', []):
            print(f"  Topic {top.get('topicCode')}: {top.get('name')}")
            for sub in top.get('subtopics', []):
                print(f"    Subtopic {sub.get('topicCode')}: {sub.get('name')}")
