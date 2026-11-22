import json

with open('scripts/mh9_mth1_leaf_topics.json', 'r', encoding='utf-8') as f:
    topics = json.load(f)

for ch_num in range(1, 8):
    ch_topics = [t for t in topics if str(t.get('chapterNumber')) == str(ch_num)]
    ch_name = ch_topics[0]['chapterName'] if ch_topics else 'Unknown'
    print(f"\n--- Chapter {ch_num}: {ch_name} ({len(ch_topics)} subtopics = {len(ch_topics)*80} Qs) ---")
    for t in ch_topics:
        code = t.get('subtopicCode') or t.get('topicCode')
        name = t.get('subtopicName') or t.get('name')
        print(f"  {code}: {name}")
