import json

with open('scripts/cbse_9_scie_syllabus.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for ch in data['chapters']:
    if ch.get('chapterNumber') == 3:
        print(f"Chapter {ch.get('chapterNumber')}: {ch.get('chapterName')}")
        for top in ch.get('topics', []):
            print(f"  Topic {top.get('topicCode')}: {top.get('topicName')}")
            for sub in top.get('subtopics', []):
                print(f"    Subtopic {sub.get('subtopicCode')}: {sub.get('subtopicName')}")
