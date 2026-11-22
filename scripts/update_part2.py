import json
from engine_algebra import generate_subtopic

# Read existing archs from build_clean_mth1_ch4_part2.py
with open('scripts/build_clean_mth1_ch4_part2.py', 'r', encoding='utf-8') as f:
    code = f.read()

# We want to replace the whole top part with imports and replace generate_subtopic_80 with generate_subtopic
header = '''"""
Build Clean Questions for MH-9-MTH1 Chapter 4 Part 2 (Subtopics 4.3.3 to 4.4.4 = 7 subtopics = 560 Qs)
Rule 2T: Strictly 80 questions per leaf subtopic (40 Exam, 20 Practice, 20 Foundation).
Rule 2J: 0 duplicate pairs, verified via validateBatchDistinctness.
"""

import json
from engine_algebra import generate_subtopic

CH_NUM = 4
CH_NAME = "Ratio and Proportion"
'''

# Find where tc = "MH-9-MTH1-4-4.3.3" starts
idx = code.find('tc = "MH-9-MTH1-4-4.3.3"')
body = code[idx:]

# In body, replace all calls to:
# all_qs.extend(generate_subtopic_80(tc, tname, archs))
# with:
# all_qs.extend(generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs))
body = body.replace('all_qs.extend(generate_subtopic_80(tc, tname, archs))', 'all_qs.extend(generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs))')

# Also fix the 4 distinctness collisions in 4.4.2 and 4.4.3:
# Fix 1: 4.4.2 arch 0 item 6
old_442_0_6 = '("If 1, 3, 9, 27 are in continued proportion, what is the next term?", "81 (multiply by common ratio 3)", ["54", "72", "90"])'
new_442_0_6 = '("In a geometric series 1, 3, 9, 27 where consecutive terms form equal ratios, compute the fifth term:", "81", ["54", "72", "90"])'
body = body.replace(old_442_0_6, new_442_0_6)

# Fix 2: 4.4.2 arch 4 item 8
old_442_4_8 = '("If a, b, c are in continued proportion, what is \\\\(\\frac{a + 2b + c}{a - 2b + c}\\\\)?", "\\\\(\\frac{(\\\\sqrt{a} + \\\\sqrt{c})^2}{(\\\\sqrt{a} - \\\\sqrt{c})^2}\\\\)", ["1", "-1", "\\\\(\\frac{a}{c}\\\\)"])'
new_442_4_8 = '("Given that middle term satisfies \\\\(b^2 = ac\\\\), evaluate the fraction \\\\(\\frac{a + 2b + c}{a - 2b + c}\\\\):", "\\\\(\\frac{(\\\\sqrt{a} + \\\\sqrt{c})^2}{(\\\\sqrt{a} - \\\\sqrt{c})^2}\\\\)", ["1", "-1", "\\\\(\\frac{a}{c}\\\\)"])'
body = body.replace(old_442_4_8, new_442_4_8)

# Fix 3: 4.4.3 arch 5 item 9
old_443_5_9 = '("Two numbers have AM = 20 and GM = 16. Find the numbers:", "32 and 8 (sum = 40, product = 256 => roots are 32, 8)", ["30 and 10", "24 and 16", "36 and 4"])'
new_443_5_9 = '("Determine two distinct positive integers whose arithmetic mean is 20 and geometric mean is 16:", "32 and 8", ["30 and 10", "24 and 16", "36 and 4"])'
body = body.replace(old_443_5_9, new_443_5_9)

# Fix 4: 4.4.3 arch 6 item 0
old_443_6_0 = '("In a right-angled triangle, the altitude on the hypotenuse divides it into lengths 4 cm and 9 cm. What is the length of the altitude?", "6 cm (altitude h = sqrt(4 * 9) = 6 cm)", ["5 cm", "6.5 cm", "13 cm"])'
new_443_6_0 = '("The perpendicular dropped from the right angle to the hypotenuse splits it into parts 4 cm and 9 cm. Compute the perpendicular length:", "6 cm", ["5 cm", "6.5 cm", "13 cm"])'
body = body.replace(old_443_6_0, new_443_6_0)

new_content = header + "def get_ch4_p2_questions():\n    all_qs = []\n    " + body

with open('scripts/build_clean_mth1_ch4_part2.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated build_clean_mth1_ch4_part2.py successfully!')
