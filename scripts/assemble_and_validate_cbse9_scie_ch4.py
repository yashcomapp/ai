import json

with open('scripts/cbse9_scie_ch4_part_a.json', 'r', encoding='utf-8') as f:
    part_a = json.load(f)

with open('scripts/cbse9_scie_ch4_part_b.json', 'r', encoding='utf-8') as f:
    part_b = json.load(f)

all_questions = part_a + part_b
print(f"Total questions assembled: {len(all_questions)}")

# Verify subtopics
counts = {}
for q in all_questions:
    tc = q['topicCode']
    counts[tc] = counts.get(tc, 0) + 1

print("Counts per subtopic:")
for tc, cnt in sorted(counts.items()):
    print(f"  {tc}: {cnt}")

out_path = 'scripts/clean_cbse9_scie_ch4_questions.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {out_path}")
