import json

with open("scripts/zero_questions_audit_result.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data if isinstance(data, list) else data.get("subjects", [])

for s in items:
    if s.get("subjectDocId") == "MH-9-SCIT" or s.get("id") == "MH-9-SCIT":
        for ch in s.get("chapters", []):
            if str(ch.get("chapterNumber")) in ["19", "20"]:
                print(f"Chapter {ch.get('chapterNumber')}: {ch.get('chapterName')}")
                for t in ch.get("topics", []):
                    print(f"  Topic: {t.get('topicCode')} {t.get('topicName')}")
                    for st in t.get("subtopics", []):
                        print(f"    Subtopic: {st.get('topicCode')} -> {st.get('subtopicName')} (count: {st.get('currentQuestionCount')})")
