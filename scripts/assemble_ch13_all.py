"""
assemble_ch13_all.py
Assembles all 79 enhanced questions for Chapter 13: Carbon (Compact Format).
"""

import json
from build_ch13_part1 import get_part1_enhancements
from build_ch13_part2 import get_part2_enhancements

with open('backups/staging/mh9_scit_13_raw.json', 'r', encoding='utf-8') as f:
    raw_questions = json.load(f)

print(f"Loaded {len(raw_questions)} raw questions.")

part1 = get_part1_enhancements()
part2 = get_part2_enhancements()

all_enh = {}
all_enh.update(part1)
all_enh.update(part2)

print(f"Total enhancements assembled: {len(all_enh)}")
assert len(all_enh) == 79, f"Expected 79 enhancements, got {len(all_enh)}"

enhanced_list = []
for idx, raw_q in enumerate(raw_questions):
    enh = all_enh.get(idx)
    assert enh is not None, f"Missing enhancement for index {idx} ({raw_q.get('questionCode')})"

    merged = dict(raw_q)
    merged["text"] = enh["text"]
    merged["options"] = enh["options"]
    merged["correctAnswer"] = enh["correctAnswer"]
    merged["solution"] = enh["solution"]
    merged["isEnhanced"] = True
    enhanced_list.append(merged)

with open('scripts/ch13_all.js', 'w', encoding='utf-8') as f:
    f.write("// Enhanced Questions for Chapter 13: Carbon (Compact Format - 79 Qs)\n")
    f.write("module.exports = ")
    json.dump(enhanced_list, f, indent=2, ensure_ascii=False)
    f.write(";\n")

with open('backups/staging/mh9_scit_13_enhanced.json', 'w', encoding='utf-8') as f:
    json.dump(enhanced_list, f, indent=2, ensure_ascii=False)

print("Successfully wrote 79 enhanced questions to scripts/ch13_all.js and backups/staging/mh9_scit_13_enhanced.json")
