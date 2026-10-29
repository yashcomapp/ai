"""
assemble_ch12_all.py
Assembles all 114 enhanced questions for Chapter 12 (Study of Sound)
from Part 1, Part 2, and Part 3.
"""

import json
from build_ch12_part1 import get_part1_enhancements
from build_ch12_part2 import get_part2_enhancements
from build_ch12_part3 import get_part3_enhancements

with open('backups/staging/mh9_scit_12_raw.json', 'r', encoding='utf-8') as f:
    raw_questions = json.load(f)

print(f"Loaded {len(raw_questions)} raw questions.")

part1 = get_part1_enhancements()
part2 = get_part2_enhancements()
part3 = get_part3_enhancements()

all_enhancements = {}
all_enhancements.update(part1)
all_enhancements.update(part2)
all_enhancements.update(part3)

print(f"Total enhancements assembled: {len(all_enhancements)}")
assert len(all_enhancements) == 114, f"Expected 114 enhancements, got {len(all_enhancements)}"

enhanced_list = []
for idx, raw_q in enumerate(raw_questions):
    enh = all_enhancements.get(idx)
    assert enh is not None, f"Missing enhancement for index {idx} ({raw_q.get('questionCode')})"
    
    # Merge
    merged_q = dict(raw_q)
    merged_q["text"] = enh["text"]
    merged_q["options"] = enh["options"]
    merged_q["correctAnswer"] = enh["correctAnswer"]
    merged_q["solution"] = enh["solution"]
    merged_q["isEnhanced"] = True
    enhanced_list.append(merged_q)

# Write to ch12_all.js as Node module
with open('scripts/ch12_all.js', 'w', encoding='utf-8') as f:
    f.write("// Enhanced Questions for Chapter 12: Study of Sound (114 Qs)\n")
    f.write("module.exports = ")
    json.dump(enhanced_list, f, indent=2, ensure_ascii=False)
    f.write(";\n")

# Also write to staging JSON
with open('backups/staging/mh9_scit_12_enhanced.json', 'w', encoding='utf-8') as f:
    json.dump(enhanced_list, f, indent=2, ensure_ascii=False)

print("Successfully wrote 114 enhanced questions to scripts/ch12_all.js and backups/staging/mh9_scit_12_enhanced.json")
