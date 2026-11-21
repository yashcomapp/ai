import re

# =============================================================================
# PATCH PART 1
# =============================================================================
with open("scripts/build_clean_ch3_p1.py", "r", encoding="utf-8") as f:
    p1 = f.read()

# 1. Fix 3.1.1 Arch 6 options
old_311_arch6_calc = '''            'calc': lambda item: (
                "Strictly greater than either of its remote interior angles",
                ["Strictly less than either of its remote interior angles", "Always equal to the adjacent interior angle", "Strictly equal to 90°"],'''
new_311_arch6_calc = '''            'calc': lambda item: (
                "Strictly greater than either of its remote interior angles",
                ["Strictly smaller than both remote angles", "Always equal to exactly 90 degrees", "Equal to the adjacent interior angle"],'''
p1 = p1.replace(old_311_arch6_calc, new_311_arch6_calc)

# 2. Fix 3.2.1 short test names to full descriptive names so they don't differ by 1-2 characters
# Replace "SAS Congruence Test" -> "Side-Angle-Side (SAS) Test"
p1 = p1.replace('"SAS Congruence Test"', '"Side-Angle-Side (SAS) Congruence Criterion"')
p1 = p1.replace('"ASA Congruence Test"', '"Angle-Side-Angle (ASA) Congruence Criterion"')
p1 = p1.replace('"SSS Congruence Test"', '"Side-Side-Side (SSS) Congruence Criterion"')
p1 = p1.replace('"RHS Congruence Test"', '"Hypotenuse-Side (RHS) Congruence Criterion"')
p1 = p1.replace('"AAS Congruence Test"', '"Angle-Angle-Side (AAS) Congruence Criterion"')
p1 = p1.replace('"Hypotenuse-Side (RHS) Congruence Test"', '"Hypotenuse-Side (RHS) Congruence Criterion"')
p1 = p1.replace('"AAS (or SAA) Congruence Test"', '"Angle-Angle-Side (AAS / SAA) Congruence Criterion"')
p1 = p1.replace('"AAS (SAA) Congruence Test"', '"Angle-Angle-Side (AAS / SAA) Congruence Criterion"')
p1 = p1.replace('"SAS Test"', '"Side-Angle-Side (SAS) Criterion"')
p1 = p1.replace('"ASA Test"', '"Angle-Side-Angle (ASA) Criterion"')
p1 = p1.replace('"SSS Test"', '"Side-Side-Side (SSS) Criterion"')
p1 = p1.replace('"RHS Test"', '"Hypotenuse-Side (RHS) Criterion"')
p1 = p1.replace('"AAS Test"', '"Angle-Angle-Side (AAS) Criterion"')
p1 = p1.replace('"AAA Test"', '"Angle-Angle-Angle (AAA) Similarity Criterion"')
p1 = p1.replace('"SSA Test"', '"Invalid Side-Side-Angle (SSA) Condition"')

# In 3.2.1 Arch 0: fix angle options that differ by 2 chars
old_321_arch0_opt = '["\\\\(\\\\angle B = \\\\angle Y\\\\)", "\\\\(\\\\angle C = \\\\angle Z\\\\)", "Any arbitrary angle"]'
new_321_arch0_opt = '["Angle B congruent to Angle Y", "Angle C congruent to Angle Z", "Any arbitrary non-included angle"]'
p1 = p1.replace(old_321_arch0_opt, new_321_arch0_opt)

old_321_arch0_opt2 = '["\\\\(\\\\angle P = \\\\angle S\\\\)", "\\\\(\\\\angle R = \\\\angle U\\\\)", "PR = SU"]'
new_321_arch0_opt2 = '["Angle P congruent to Angle S", "Angle R congruent to Angle U", "Side PR equal to side SU"]'
p1 = p1.replace(old_321_arch0_opt2, new_321_arch0_opt2)

# In 3.2.1 Arch 1: fix sides that differ by 2 chars
old_321_arch1_opt = '["Side BC = Side EF", "Side AC = Side DF", "Any side"]'
new_321_arch1_opt = '["Non-included side BC equal to side EF", "Non-included side AC equal to side DF", "Any arbitrary external segment"]'
p1 = p1.replace(old_321_arch1_opt, new_321_arch1_opt)

# In 3.2.1 Arch 7: fix missing conditions that differ by 1-2 chars
old_321_arch7_1 = '["\\\\(\\\\angle A = \\\\angle P\\\\)", "\\\\(\\\\angle C = \\\\angle R\\\\)", "AC = PR"]'
new_321_arch7_1 = '["Angle A matching Angle P", "Angle C matching Angle R", "Third side AC equal to side PR"]'
p1 = p1.replace(old_321_arch7_1, new_321_arch7_1)

old_321_arch7_2 = '["\\\\(\\\\angle B = \\\\angle Q\\\\)", "\\\\(\\\\angle A = \\\\angle P\\\\)", "\\\\(\\\\angle C = \\\\angle R\\\\)"]'
new_321_arch7_2 = '["Angle B equal to Angle Q", "Angle A equal to Angle P", "Angle C equal to Angle R"]'
p1 = p1.replace(old_321_arch7_2, new_321_arch7_2)

old_321_arch7_3 = '["BC = EF", "AC = DF", "\\\\(\\\\angle C = \\\\angle F\\\\)"]'
new_321_arch7_3 = '["Side BC equal to side EF", "Side AC equal to side DF", "Angle C equal to Angle F"]'
p1 = p1.replace(old_321_arch7_3, new_321_arch7_3)

old_321_arch7_4 = '["BC = QR", "\\\\(\\\\angle A = \\\\angle P\\\\)", "\\\\(\\\\angle C = \\\\angle R\\\\)"]'
new_321_arch7_4 = '["Base side BC equal to side QR", "Angle A equal to Angle P", "Angle C equal to Angle R"]'
p1 = p1.replace(old_321_arch7_4, new_321_arch7_4)

old_321_arch7_5 = '["YZ = MN", "\\\\(\\\\angle Y = \\\\angle M\\\\)", "\\\\(\\\\angle Z = \\\\angle N\\\\)"]'
new_321_arch7_5 = '["Side YZ equal to side MN", "Angle Y equal to Angle M", "Angle Z equal to Angle N"]'
p1 = p1.replace(old_321_arch7_5, new_321_arch7_5)

old_321_arch7_6 = '["\\\\(\\\\angle A = \\\\angle P\\\\)", "AB = PQ", "AC = PR"]'
new_321_arch7_6 = '["Angle A equal to Angle P", "Side AB equal to side PQ", "Side AC equal to side PR"]'
p1 = p1.replace(old_321_arch7_6, new_321_arch7_6)

old_321_arch7_7 = '["AB = PQ", "\\\\(\\\\angle A = \\\\angle P\\\\)", "\\\\(\\\\angle B = \\\\angle Q\\\\)"]'
new_321_arch7_7 = '["Side AB equal to side PQ", "Angle A equal to Angle P", "Angle B equal to Angle Q"]'
p1 = p1.replace(old_321_arch7_7, new_321_arch7_7)

old_321_arch7_8 = '["\\\\(\\\\angle E = \\\\angle T\\\\)", "\\\\(\\\\angle D = \\\\angle S\\\\)", "\\\\(\\\\angle F = \\\\angle U\\\\)"]'
new_321_arch7_8 = '["Angle E equal to Angle T", "Angle D equal to Angle S", "Angle F equal to Angle U"]'
p1 = p1.replace(old_321_arch7_8, new_321_arch7_8)

# 3. In 3.2.2 Arch 6: replace short angle/side options
p1 = p1.replace('["\\\\(\\\\angle B\\\\)", "\\\\(\\\\angle A\\\\)", "\\\\(\\\\angle D\\\\)"]',
                '["Angle B of the second triangle", "Angle A of the first triangle", "Angle D of the corresponding figure"]')
p1 = p1.replace('["Side LM", "Side MN", "Side NL"]',
                '["Adjacent side LM", "Base side MN", "Opposite side NL"]')
p1 = p1.replace('["Side FE", "Side FD", "Side EF"]',
                '["Segment FE", "Segment FD", "Segment EF"]')
p1 = p1.replace('["\\\\(\\\\angle C\\\\)", "\\\\(\\\\angle A\\\\)", "\\\\(\\\\angle P\\\\)"]',
                '["Angle C at the apex", "Angle A at the origin", "Angle P of the second triangle"]')
p1 = p1.replace('["AB = PQ", "BC = QR", "AC = PR"]',
                '["Side AB matches side PQ", "Side BC matches side QR", "Side AC matches side PR"]')

# 4. In 3.2.2 Arch 0: fix OSC-108 vs OSC-103
# Make all 10 AB values in Arch 0 distinct:
# currently: [(5, 7, 9), (6, 8, 10), (7, 10, 12), (4, 9, 11), (8, 11, 13), (5, 12, 13), (6, 9, 14), (7, 8, 11), (9, 12, 15), (8, 15, 17)]
# Notice AB has duplicates (5 twice, 6 twice, 7 twice, 8 twice).
# Replace with strictly distinct AB values: 4, 5, 6, 7, 8, 9, 10, 11, 12, 13!
old_322_arch0_data = "[(5, 7, 9), (6, 8, 10), (7, 10, 12), (4, 9, 11), (8, 11, 13),\n                     (5, 12, 13), (6, 9, 14), (7, 8, 11), (9, 12, 15), (8, 15, 17)]"
new_322_arch0_data = "[(4, 9, 11), (5, 7, 9), (6, 8, 10), (7, 10, 12), (8, 11, 13),\n                     (9, 12, 15), (10, 14, 18), (11, 15, 20), (12, 16, 22), (13, 17, 24)]"
p1 = p1.replace(old_322_arch0_data, new_322_arch0_data)

# In 3.2.2 Arch 3: fix OSC-138 vs OSC-132
# Make all 10 answers in Arch 3 distinct:
# currently: [(5, 10, 3, 20, 15), (4, 15, 2, 25, 20), (6, 5, 4, 25, 15), (7, 10, 4, 35, 15), (5, 5, 2, 40, 15), (6, 20, 3, 40, 20), (4, 10, 2, 30, 20), (5, 15, 3, 25, 20), (8, 10, 5, 35, 15), (6, 12, 2, 48, 15)]
# (many 15s and 20s!).
# Replace with strictly distinct answers: 10, 12, 14, 16, 18, 20, 22, 24, 26, 28!
# Let (ax - b) = (cx + d) => (a-c)x = d+b => x = (d+b)/(a-c):
# x=10: 4x - 10 = 2x + 10 (2x = 20 => x=10) -> (4, 10, 2, 10, 10)
# x=12: 5x - 10 = 2x + 26 (3x = 36 => x=12) -> (5, 10, 2, 26, 12)
# x=14: 4x - 6 = 2x + 22 (2x = 28 => x=14) -> (4, 6, 2, 22, 14)
# x=16: 5x - 12 = 3x + 20 (2x = 32 => x=16) -> (5, 12, 3, 20, 16)
# x=18: 4x - 14 = 2x + 22 (2x = 36 => x=18) -> (4, 14, 2, 22, 18)
# x=20: 5x - 15 = 2x + 45 (3x = 60 => x=20) -> (5, 15, 2, 45, 20)
# x=22: 4x - 12 = 2x + 32 (2x = 44 => x=22) -> (4, 12, 2, 32, 22)
# x=24: 5x - 20 = 2x + 52 (3x = 72 => x=24) -> (5, 20, 2, 52, 24)
# x=26: 4x - 8 = 2x + 44 (2x = 52 => x=26) -> (4, 8, 2, 44, 26)
# x=28: 5x - 16 = 3x + 40 (2x = 56 => x=28) -> (5, 16, 3, 40, 28)
old_322_arch3_data = "[(5, 10, 3, 20, 15), (4, 15, 2, 25, 20), (6, 5, 4, 25, 15), (7, 10, 4, 35, 15), (5, 5, 2, 40, 15),\n                     (6, 20, 3, 40, 20), (4, 10, 2, 30, 20), (5, 15, 3, 25, 20), (8, 10, 5, 35, 15), (6, 12, 2, 48, 15)]"
new_322_arch3_data = "[(4, 10, 2, 10, 10), (5, 10, 2, 26, 12), (4, 6, 2, 22, 14), (5, 12, 3, 20, 16), (4, 14, 2, 22, 18),\n                     (5, 15, 2, 45, 20), (4, 12, 2, 32, 22), (5, 20, 2, 52, 24), (4, 8, 2, 44, 26), (5, 16, 3, 40, 28)]"
p1 = p1.replace(old_322_arch3_data, new_322_arch3_data)

# 5. In 3.3.1: fix OSC-203 vs OSC-123
# In 3.3.1 Arch 2: x = (item[3]-item[1])/(item[0]-item[2]):
# currently: [(5, 10, 3, 30, 10), (4, 15, 2, 35, 10), (6, 5, 3, 26, 7), (5, 8, 2, 29, 7), (7, 5, 4, 26, 7), (4, 20, 2, 40, 10), (6, 12, 3, 36, 8), (5, 15, 2, 45, 10), (7, 10, 3, 50, 10), (8, 4, 4, 36, 8)]
# Make all 10 answers strictly distinct: 4, 5, 6, 7, 8, 9, 10, 11, 12, 13!
# x=4: 5x + 6 = 2x + 18 (3x = 12 => x=4) -> (5, 6, 2, 18, 4)
# x=5: 4x + 5 = 2x + 15 (2x = 10 => x=5) -> (4, 5, 2, 15, 5)
# x=6: 5x + 4 = 2x + 22 (3x = 18 => x=6) -> (5, 4, 2, 22, 6)
# x=7: 6x + 5 = 3x + 26 (3x = 21 => x=7) -> (6, 5, 3, 26, 7)
# x=8: 5x + 8 = 2x + 32 (3x = 24 => x=8) -> (5, 8, 2, 32, 8)
# x=9: 4x + 7 = 2x + 25 (2x = 18 => x=9) -> (4, 7, 2, 25, 9)
# x=10: 5x + 10 = 3x + 30 (2x = 20 => x=10) -> (5, 10, 3, 30, 10)
# x=11: 4x + 6 = 2x + 28 (2x = 22 => x=11) -> (4, 6, 2, 28, 11)
# x=12: 5x + 12 = 2x + 48 (3x = 36 => x=12) -> (5, 12, 2, 48, 12)
# x=13: 4x + 9 = 2x + 35 (2x = 26 => x=13) -> (4, 9, 2, 35, 13)
old_331_arch2_data = "[(5, 10, 3, 30, 10), (4, 15, 2, 35, 10), (6, 5, 3, 26, 7), (5, 8, 2, 29, 7), (7, 5, 4, 26, 7),\n                     (4, 20, 2, 40, 10), (6, 12, 3, 36, 8), (5, 15, 2, 45, 10), (7, 10, 3, 50, 10), (8, 4, 4, 36, 8)]"
new_331_arch2_data = "[(5, 6, 2, 18, 4), (4, 5, 2, 15, 5), (5, 4, 2, 22, 6), (6, 5, 3, 26, 7), (5, 8, 2, 32, 8),\n                     (4, 7, 2, 25, 9), (5, 10, 3, 30, 10), (4, 6, 2, 28, 11), (5, 12, 2, 48, 12), (4, 9, 2, 35, 13)]"
p1 = p1.replace(old_331_arch2_data, new_331_arch2_data)

# 6. In 3.3.2: fix OSC-113 vs OSC-107
# In Arch 0: hyp is given, find side opp 30: side = hyp / 2
# In Arch 1: side opp 30 is given, find hyp: hyp = 2 * side
# If Arch 0 has hyp = 20, side = 10.
# If Arch 1 has side = 5, hyp = 10.
# Both had answer `10 cm`!
# Let's ensure Arch 0 answers and Arch 1 answers are disjoint sets:
# Arch 0 answers (side opp 30): odd integers: 3, 5, 7, 9, 11, 13, 15, 17, 19, 21 (from hyp = 6, 10, 14, 18, 22, 26, 30, 34, 38, 42)
# Arch 1 answers (hypotenuse): multiples of 4: 16, 20, 24, 28, 32, 36, 40, 44, 48, 52 (from side = 8, 10, 12, 14, 16, 18, 20, 22, 24, 26)
# Completely disjoint sets!
old_332_arch0_data = "[(8, 4), (10, 5), (12, 6), (14, 7), (16, 8),\n                     (18, 9), (20, 10), (22, 11), (24, 12), (26, 13)]"
new_332_arch0_data = "[(6, 3), (10, 5), (14, 7), (18, 9), (22, 11),\n                     (26, 13), (30, 15), (34, 17), (38, 19), (42, 21)]"
p1 = p1.replace(old_332_arch0_data, new_332_arch0_data)

old_332_arch1_data = "[(3, 6), (4, 8), (5, 10), (6, 12), (7, 14),\n                     (8, 16), (9, 18), (10, 20), (11, 22), (12, 24)]"
new_332_arch1_data = "[(8, 16), (10, 20), (12, 24), (14, 28), (16, 32),\n                     (18, 36), (20, 40), (22, 44), (24, 48), (26, 52)]"
p1 = p1.replace(old_332_arch1_data, new_332_arch1_data)

# In 3.3.2 Arch 5: fix typo \sqrt3 vs \sqrt{3}
p1 = p1.replace(r"{item[0]}\sqrt{3}", r"{item[0]}\\sqrt{{3}}")

with open("scripts/build_clean_ch3_p1.py", "w", encoding="utf-8") as f:
    f.write(p1)
print("Updated build_clean_ch3_p1.py successfully.")

# =============================================================================
# PATCH PART 2
# =============================================================================
with open("scripts/build_clean_ch3_p2.py", "r", encoding="utf-8") as f:
    p2 = f.read()

# 1. In 3.3.3: fix Arch 0 vs Arch 1 distinctness by making answers disjoint
# Arch 0 answers: 2\sqrt{2}, 4\sqrt{2}, 6\sqrt{2}, 8\sqrt{2}, 10\sqrt{2}, 12\sqrt{2}, 14\sqrt{2}, 16\sqrt{2}, 18\sqrt{2}, 20\sqrt{2}
# (from hyp = 4, 8, 12, 16, 20, 24, 28, 32, 36, 40)
# Arch 1 answers: 3\sqrt{2}, 5\sqrt{2}, 7\sqrt{2}, 9\sqrt{2}, 11\sqrt{2}, 13\sqrt{2}, 15\sqrt{2}, 17\sqrt{2}, 19\sqrt{2}, 21\sqrt{2}
# (from leg = 3, 5, 7, 9, 11, 13, 15, 17, 19, 21)
# Zero overlap!
old_333_arch0_data = "[(6, \"3\\\\sqrt{2}\"), (8, \"4\\\\sqrt{2}\"), (10, \"5\\\\sqrt{2}\"), (12, \"6\\\\sqrt{2}\"), (14, \"7\\\\sqrt{2}\"),\n                     (16, \"8\\\\sqrt{2}\"), (18, \"9\\\\sqrt{2}\"), (20, \"10\\\\sqrt{2}\"), (22, \"11\\\\sqrt{2}\"), (24, \"12\\\\sqrt{2}\")]"
new_333_arch0_data = "[(4, \"2\\\\sqrt{2}\"), (8, \"4\\\\sqrt{2}\"), (12, \"6\\\\sqrt{2}\"), (16, \"8\\\\sqrt{2}\"), (20, \"10\\\\sqrt{2}\"),\n                     (24, \"12\\\\sqrt{2}\"), (28, \"14\\\\sqrt{2}\"), (32, \"16\\\\sqrt{2}\"), (36, \"18\\\\sqrt{2}\"), (40, \"20\\\\sqrt{2}\")]"
p2 = p2.replace(old_333_arch0_data, new_333_arch0_data)

old_333_arch1_data = "[(3, \"3\\\\sqrt{2}\"), (4, \"4\\\\sqrt{2}\"), (5, \"5\\\\sqrt{2}\"), (6, \"6\\\\sqrt{2}\"), (7, \"7\\\\sqrt{2}\"),\n                     (8, \"8\\\\sqrt{2}\"), (9, \"9\\\\sqrt{2}\"), (10, \"10\\\\sqrt{2}\"), (11, \"11\\\\sqrt{2}\"), (12, \"12\\\\sqrt{2}\")]"
new_333_arch1_data = "[(3, \"3\\\\sqrt{2}\"), (5, \"5\\\\sqrt{2}\"), (7, \"7\\\\sqrt{2}\"), (9, \"9\\\\sqrt{2}\"), (11, \"11\\\\sqrt{2}\"),\n                     (13, \"13\\\\sqrt{2}\"), (15, \"15\\\\sqrt{2}\"), (17, \"17\\\\sqrt{2}\"), (19, \"19\\\\sqrt{2}\"), (21, \"21\\\\sqrt{2}\")]"
p2 = p2.replace(old_333_arch1_data, new_333_arch1_data)

# 2. In 3.4.1: fix OSC-309 vs OSC-219
# In Arch 7 item 8 (OSC-309): "If in any triangle ABC, median BD to AC satisfies BD = 1/2 AC, what is angle B?" -> 90°
# In Arch 6 item 8 (OSC-219): angle ADB formed when angle A is 60° -> 180 - 2(60) = 60°
# Wait, let's check what OSC-309 and OSC-219 actually are.
# Also fix short options in 3.4.1 Arch 7 and 3.4.2 Arch 2:
p2 = p2.replace('["DB = 2 DA", "DA = 2 DB"]', '["DB equals twice DA", "DA equals twice DB"]')
p2 = p2.replace('["AD = BC", "AB = BC"]', '["Segment AD equals segment BC", "Segment AB equals segment BC"]')
p2 = p2.replace('["Arm OA", "Arm OB"]', '["The initial ray Arm OA", "The terminal ray Arm OB"]')
p2 = p2.replace('["\\\\(\\\\Delta = 2 r s\\\\)", "\\\\(\\\\Delta = r^2 s\\\\)"]',
                '["\\\\(\\\\Delta = 2 r s\\\\) with factor 2", "\\\\(\\\\Delta = r^2 s\\\\) with squared inradius"]')

# In 3.5.2: fix distinctness in Arch 3 (perimeters) and Arch 4 (angles) and Arch 7:
# Make all 10 answers in Arch 3 distinct:
old_352_arch3_data = "[(2, 3, 20, 30), (3, 4, 24, 32), (1, 2, 15, 30), (3, 5, 27, 45), (2, 5, 18, 45),\n                     (4, 5, 36, 45), (5, 6, 25, 30), (3, 7, 21, 49), (2, 7, 16, 56), (4, 7, 28, 49)]"
new_352_arch3_data = "[(2, 3, 16, 24), (3, 4, 21, 28), (1, 2, 15, 30), (2, 5, 14, 35), (3, 5, 24, 40),\n                     (4, 5, 36, 45), (1, 3, 16, 48), (3, 7, 21, 49), (2, 7, 16, 56), (5, 8, 40, 64)]"
p2 = p2.replace(old_352_arch3_data, new_352_arch3_data)

# Make all 10 answers in Arch 4 distinct:
old_352_arch4_data = "[(50, 60, 70), (40, 65, 75), (45, 55, 80), (35, 65, 80), (30, 70, 80),\n                     (55, 65, 60), (40, 50, 90), (35, 75, 70), (60, 60, 60), (25, 75, 80)]"
new_352_arch4_data = "[(25, 75, 80), (30, 70, 80), (35, 65, 80), (40, 65, 75), (45, 55, 80),\n                     (50, 60, 70), (55, 65, 60), (60, 60, 60), (65, 55, 60), (70, 50, 60)]"
p2 = p2.replace(old_352_arch4_data, new_352_arch4_data)

# In 3.5.2 Arch 7: replace item 8 with area of similar triangles relation to medians
old_352_arch7_item8 = '("In similar triangles, the ratio of corresponding medians is equal to the", "Ratio of corresponding sides", ["Ratio of areas", "Square of ratio of sides", "1 : 1 always"]),'
new_352_arch7_item8 = '("In similar triangles, the ratio of the areas is equal to the", "Square of the ratio of corresponding medians", ["Direct ratio of medians", "Square root of medians", "Cube of corresponding medians"]),'
p2 = p2.replace(old_352_arch7_item8, new_352_arch7_item8)

# In 3.5.2 Arch 5: replace short similarity test names
p2 = p2.replace('"SAS Similarity Test"', '"Side-Angle-Side (SAS) Similarity Criterion"')
p2 = p2.replace('"SSS Similarity Test"', '"Side-Side-Side (SSS) Similarity Criterion"')
p2 = p2.replace('"ASA Similarity Test"', '"Angle-Side-Angle (ASA) Criterion"')
p2 = p2.replace('"AAA Similarity Test"', '"Angle-Angle-Angle (AAA) Similarity Criterion"')
p2 = p2.replace('"RHS Similarity Test"', '"Hypotenuse-Side (RHS) Criterion"')

with open("scripts/build_clean_ch3_p2.py", "w", encoding="utf-8") as f:
    f.write(p2)
print("Updated build_clean_ch3_p2.py successfully.")
EOF
