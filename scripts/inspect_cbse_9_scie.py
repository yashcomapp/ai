import json

with open('scripts/cbse_9_scie_syllabus.json', 'r', encoding='utf-8') as f:
    s = json.load(f)

print(f"Board: {s.get('boardCode')}, Class: {s.get('class')}, Subject: {s.get('subject')}, Code: {s.get('subjectCode')}")
print(f"Total Chapters: {len(s.get('chapters', []))}\n")

total_subtopics = 0
for ch in s['chapters']:
    ch_num = ch.get('number')
    ch_name = ch.get('name')
    topics = ch.get('topics', [])
    st_count = sum(len(t.get('subtopics', [])) for t in topics)
    total_subtopics += st_count
    print(f"Chapter {ch_num}: {ch_name} ({len(topics)} topics, {st_count} subtopics, target {st_count * 80} Qs)")
    for t in topics:
        t_num = t.get('number')
        t_name = t.get('name')
        t_code = t.get('topicCode')
        subtopics = t.get('subtopics', [])
        print(f"   Topic {t_num}: {t_name} [{t_code}] ({len(subtopics)} subtopics)")
        for st in subtopics:
            print(f"      Subtopic {st.get('number')}: {st.get('name')} [{st.get('topicCode')}]")

print(f"\nTOTAL LEAF SUBTOPICS IN CBSE-9-SCIE: {total_subtopics}")
print(f"TOTAL QUESTIONS TO BE GENERATED (80 Qs per subtopic): {total_subtopics * 80}")
