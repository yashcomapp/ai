import json

with open("scripts/mth2_all_topics.json", "r", encoding="utf-8") as f:
    topics = json.load(f)

cl9 = [t for t in topics if t['code'].startswith('MH-9-MTH2')]
print(f"Total Class 9 MTH2 topics: {len(cl9)}")

for ch in [1, 2, 3]:
    ch_topics = [t for t in cl9 if f"-{ch}-" in t['code']]
    print(f"\n--- Chapter {ch} ({len(ch_topics)} topics) ---")
    for t in ch_topics:
        print(f"  {t['code']}: {t['name']}")
