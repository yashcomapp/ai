import json

with open('scripts/cbse9_mgm_syllabus.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for ch in d.get('chapters', []):
    num = ch.get('chapterNumber', ch.get('number'))
    title = ch.get('title', ch.get('chapterName', ch.get('name')))
    print(f"\n=== Chapter {num}: {title} ===")
    for t in ch.get('topics', []):
        tcode = t.get('topicCode', t.get('code'))
        ttitle = t.get('title', t.get('name'))
        subtopics = t.get('subtopics', [])
        if subtopics:
            print(f"  Topic {tcode}: {ttitle} ({len(subtopics)} subtopics)")
            for st in subtopics:
                stcode = st.get('subtopicCode', st.get('topicCode', st.get('code')))
                sttitle = st.get('title', st.get('name'))
                print(f"    - {stcode}: {sttitle}")
        else:
            print(f"  Leaf Topic {tcode}: {ttitle}")
