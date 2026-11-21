with open("scripts/build_clean_ch3_p1.py", "r", encoding="utf-8") as f:
    p1 = f.read()

# 1. 3.2.1 Arch 0
p1 = p1.replace(
    '["Angle B congruent to Angle Y", "Angle C congruent to Angle Z", "Any arbitrary non-included angle"]',
    '["Angle B at the base", "Angle C at the third vertex", "Any arbitrary non-included angle"]'
)
p1 = p1.replace(
    '["Angle P congruent to Angle S", "Angle R congruent to Angle U", "Side PR equal to side SU"]',
    '["Angle P situated at the top", "Angle R situated at the right base", "Length of side PR"]'
)

# 2. 3.2.1 Arch 1
p1 = p1.replace(
    '["Non-included side BC equal to side EF", "Non-included side AC equal to side DF", "Any arbitrary external segment"]',
    '["Base side BC equal to base EF", "Hypotenuse side AC equal to DF", "Any arbitrary external segment"]'
)

# 3. 3.2.1 Arch 5
p1 = p1.replace(
    '["Yes, always by SSA", "Yes, by SAS", "Yes, by AAS"]',
    '["Yes, SSA is always a valid congruence test", "Yes, only when both triangles are scalene", "No, unless all three sides are known"]'
)
p1 = p1.replace(
    '["Yes, definitely by SAS", "Yes, definitely by SSS", "Yes, definitely by AAS"]',
    '["Yes, they are guaranteed congruent by SAS", "Yes, they are congruent by SSS", "Yes, congruence is guaranteed by AAS"]'
)

# 4. 3.2.1 Arch 6
p1 = p1.replace(
    '["Yes, because all angles are 60°", "Yes, by AAA test", "Yes, by SAS test"]',
    '["Yes, because having identical angles guarantees congruence", "Yes, according to the AAA congruence test", "Yes, they have identical areas"]'
)

# 5. 3.2.1 Arch 7
p1 = p1.replace(
    '["Angle A matching Angle P", "Angle C matching Angle R", "Third side AC equal to side PR"]',
    '["Angle A equal to Angle P", "The third vertex angle C", "Third side AC equal to side PR"]'
)
p1 = p1.replace(
    '["Angle B equal to Angle Q", "Angle A equal to Angle P", "Angle C equal to Angle R"]',
    '["Base angle B equal to Q", "Vertex angle A equal to P", "Base angle C equal to R"]'
)
p1 = p1.replace(
    '["Side BC equal to side EF", "Side AC equal to side DF", "Angle C equal to Angle F"]',
    '["Opposite side BC equal to EF", "Adjacent side AC equal to DF", "Angle C equal to Angle F"]'
)
p1 = p1.replace(
    '["Base side BC equal to side QR", "Angle A equal to Angle P", "Angle C equal to Angle R"]',
    '["Base side BC equal to QR", "Vertex angle A equal to P", "Base angle C equal to R"]'
)
p1 = p1.replace(
    '["Side YZ equal to side MN", "Angle Y equal to Angle M", "Angle Z equal to Angle N"]',
    '["Side YZ equal to side MN", "Interior angle Y equal to M", "Opposite angle Z equal to N"]'
)
p1 = p1.replace(
    '["Angle A equal to Angle P", "Side AB equal to side PQ", "Side AC equal to side PR"]',
    '["Angle A equal to Angle P", "Left side AB equal to side PQ", "Right side AC equal to side PR"]'
)
p1 = p1.replace(
    '["\\\\(\\\\angle A = \\\\angle D\\\\)", "\\\\(\\\\angle C = \\\\angle F\\\\)", "Area must be given"]',
    '["Vertex angle A equal to angle D", "Base angle C equal to angle F", "Area must be given"]'
)
p1 = p1.replace(
    '["Side AB equal to side PQ", "Angle A equal to Angle P", "Angle B equal to Angle Q"]',
    '["Side AB equal to side PQ", "Vertex angle A equal to P", "Base angle B equal to Q"]'
)
p1 = p1.replace(
    '["Angle E equal to Angle T", "Angle D equal to Angle S", "Angle F equal to Angle U"]',
    '["Base angle E equal to T", "Vertex angle D equal to S", "Base angle F equal to U"]'
)

# 6. 3.2.2 Arch 6: Vertex correspondence notation
p1 = p1.replace(
    '["\\\\(\\\\Delta ABC \\\\cong \\\\Delta DFE\\\\)", "\\\\(\\\\Delta ABC \\\\cong \\\\Delta EDF\\\\)", "\\\\(\\\\Delta ABC \\\\cong \\\\Delta FED\\\\)"]',
    '["\\\\(\\\\Delta ABC \\\\cong \\\\Delta DFE\\\\) (swapped base vertices)", "\\\\(\\\\Delta ABC \\\\cong \\\\Delta EDF\\\\) (cyclic shift)", "\\\\(\\\\Delta ABC \\\\cong \\\\Delta FED\\\\) (reversed order)"]'
)
p1 = p1.replace(
    '["\\\\(\\\\Delta PQR \\\\cong \\\\Delta XZY\\\\)", "\\\\(\\\\Delta PQR \\\\cong \\\\Delta YXZ\\\\)", "\\\\(\\\\Delta PQR \\\\cong \\\\Delta ZYX\\\\)"]',
    '["\\\\(\\\\Delta PQR \\\\cong \\\\Delta XZY\\\\) (swapped base vertices)", "\\\\(\\\\Delta PQR \\\\cong \\\\Delta YXZ\\\\) (cyclic shift)", "\\\\(\\\\Delta PQR \\\\cong \\\\Delta ZYX\\\\) (reversed order)"]'
)
p1 = p1.replace(
    '["\\\\(\\\\Delta ABC \\\\cong \\\\Delta EFD\\\\)", "\\\\(\\\\Delta ABC \\\\cong \\\\Delta FDE\\\\)", "\\\\(\\\\Delta BAC \\\\cong \\\\Delta DEF\\\\)"]',
    '["\\\\(\\\\Delta ABC \\\\cong \\\\Delta EFD\\\\) (mismatched vertices)", "\\\\(\\\\Delta ABC \\\\cong \\\\Delta FDE\\\\) (shifted vertices)", "\\\\(\\\\Delta BAC \\\\cong \\\\Delta DEF\\\\) (inverted vertices)"]'
)
p1 = p1.replace(
    '["\\\\(\\\\Delta ABC \\\\cong \\\\Delta PQR\\\\)", "\\\\(\\\\Delta ABC \\\\cong \\\\Delta PRQ\\\\)", "\\\\(\\\\Delta ABC \\\\cong \\\\Delta RQP\\\\)"]',
    '["\\\\(\\\\Delta ABC \\\\cong \\\\Delta PQR\\\\) (standard order without match)", "\\\\(\\\\Delta ABC \\\\cong \\\\Delta PRQ\\\\) (partially matched)", "\\\\(\\\\Delta ABC \\\\cong \\\\Delta RQP\\\\) (reversed match)"]'
)
p1 = p1.replace(
    '["Side AB matches side PQ", "Side BC matches side QR", "Side AC matches side PR"]',
    '["Segment AB matches segment PQ", "Segment BC matches segment QR", "Segment AC matches segment PR"]'
)
p1 = p1.replace(
    '["Segment FE", "Segment FD", "Segment EF"]',
    '["Line segment FE", "Line segment FD", "Line segment EF"]'
)

# 7. 3.3.2 Arch 2 (find side opp 60 from hyp) distinctness from Arch 0 (find side opp 30 from hyp)
# Change templates in Arch 2 so they do not share wording with Arch 0:
old_332_arch2_tmpls = '''            'tmpls': [
                "In a 30°-60°-90° triangle \\\\(\\\\Delta ABC\\\\) with hypotenuse AC = {0} cm, find the length of the side opposite to the 60° angle.",
                "If the hypotenuse of a 30°-60°-90° triangle is {0} cm, calculate the length of the side opposite to the 60° angle.",
                "What is the length of the side opposite 60° in a triangle with hypotenuse {0} cm?",
                "Determine the side opposite 60°: \\\\(\\\\frac{{\\\\sqrt{{3}}}}{{2}} \\\\times {0}\\\\text{{ cm}}\\\\) in a 30°-60°-90° triangle.",
                "Find side opposite 60° in right \\\\(\\\\Delta ABC\\\\) having hypotenuse {0} cm.",
                "Calculate side opposite 60° when hypotenuse is {0} cm.",
                "Evaluate the side opposite to the 60° angle in a 30°-60°-90° triangle with hypotenuse {0} cm.",
                "Compute the length of the side opposite to 60° for hypotenuse {0} cm.",
                "In \\\\(\\\\Delta ABC\\\\) with \\\\(\\\\angle B = 90^\\\\circ, \\\\angle A = 60^\\\\circ\\\\), if AC = {0} cm, find BC.",
                "For a 30°-60°-90° triangle with hypotenuse {0} cm, find the side opposite 60°."
            ],'''

new_332_arch2_tmpls = '''            'tmpls': [
                "What is the length of the longer leg (facing the 60° angle) in right \\\\(\\\\Delta ABC\\\\) having hypotenuse AC = {0} cm?",
                "Calculate the longer cathetus opposite 60° for a right triangle with hypotenuse {0} cm.",
                "Determine the side opposite to the 60° vertex when the hypotenuse measures {0} cm.",
                "Find the length of leg BC facing 60°: \\\\(\\\\frac{{\\\\sqrt{{3}}}}{{2}} \\\\times {0}\\\\text{{ cm}}\\\\).",
                "How long is the side opposite 60° in a 30°-60°-90° triangle of hypotenuse {0} cm?",
                "Compute the altitude side opposite 60° when hypotenuse is {0} cm.",
                "Evaluate the leg opposite the 60° angle given hypotenuse {0} cm.",
                "Calculate side opposite 60°: \\\\(\\\\frac{{\\\\sqrt{{3}}}}{{2}} \\\\times {0}\\\\text{{ cm}}\\\\).",
                "In right \\\\(\\\\Delta ABC\\\\) with \\\\(\\\\angle A = 60^\\\\circ\\\\), find leg BC opposite \\\\(\\\\angle A\\\\) when AC = {0} cm.",
                "What is the longer leg length for a 30°-60°-90° triangle with hypotenuse {0} cm?"
            ],'''
p1 = p1.replace(old_332_arch2_tmpls, new_332_arch2_tmpls)

# Also use different hypotenuse values for Arch 2 so they don't overlap with Arch 0:
# Arch 0 uses: [(6, 3), (10, 5), (14, 7), (18, 9), (22, 11), (26, 13), (30, 15), (34, 17), (38, 19), (42, 21)]
# Arch 2 can use multiples of 8 and other values:
old_332_arch2_data = '[(6, "3\\\\sqrt{3}"), (8, "4\\\\sqrt{3}"), (10, "5\\\\sqrt{3}"), (12, "6\\\\sqrt{3}"), (14, "7\\\\sqrt{3}"),\n                     (16, "8\\\\sqrt{3}"), (18, "9\\\\sqrt{3}"), (20, "10\\\\sqrt{3}"), (22, "11\\\\sqrt{3}"), (24, "12\\\\sqrt{3}")]'
new_332_arch2_data = '[(8, "4\\\\sqrt{3}"), (12, "6\\\\sqrt{3}"), (16, "8\\\\sqrt{3}"), (20, "10\\\\sqrt{3}"), (24, "12\\\\sqrt{3}"),\n                     (28, "14\\\\sqrt{3}"), (32, "16\\\\sqrt{3}"), (36, "18\\\\sqrt{3}"), (40, "20\\\\sqrt{3}"), (48, "24\\\\sqrt{3}")]'
p1 = p1.replace(old_332_arch2_data, new_332_arch2_data)

# In 3.3.2 Arch 5: fix typo \sqrt3 vs \sqrt{3}
old_332_arch5_calc = '[f"{item[0] * 2} sq cm", f"{item[0]}\\\\sqrt{{3}} sq cm", f"{item[0] * 3} sq cm"]'
new_332_arch5_calc = '[f"{item[0] * 2} sq cm", f"{item[0]} sq cm", f"{item[0] * 3} sq cm"]'
p1 = p1.replace(old_332_arch5_calc, new_332_arch5_calc)

with open("scripts/build_clean_ch3_p1.py", "w", encoding="utf-8") as f:
    f.write(p1)
print("Updated build_clean_ch3_p1.py")


# =============================================================================
# PATCH PART 2
# =============================================================================
with open("scripts/build_clean_ch3_p2.py", "r", encoding="utf-8") as f:
    p2 = f.read()

# 1. 3.3.3 Arch 2 and Arch 3 distinctness:
# Arch 2: diagonal of a square with side s: d = s * \sqrt{2}
# Arch 3: side of a square with diagonal d: s = d / \sqrt{2}
# Use completely different numbers:
# Arch 2: side s = 3, 5, 7, 9, 11, 13, 15, 17, 19, 21 => d = 3\sqrt{2}, 5\sqrt{2}, ...
# Arch 3: diagonal d = 8, 12, 16, 20, 24, 28, 32, 36, 40, 48 => s = 4\sqrt{2}, 6\sqrt{2}, 8\sqrt{2}, ...
old_333_arch2_data = '[(5, "5\\\\sqrt{2}"), (6, "6\\\\sqrt{2}"), (7, "7\\\\sqrt{2}"), (8, "8\\\\sqrt{2}"), (9, "9\\\\sqrt{2}"),\n                     (10, "10\\\\sqrt{2}"), (11, "11\\\\sqrt{2}"), (12, "12\\\\sqrt{2}"), (13, "13\\\\sqrt{2}"), (15, "15\\\\sqrt{2}")]'
new_333_arch2_data = '[(3, "3\\\\sqrt{2}"), (5, "5\\\\sqrt{2}"), (7, "7\\\\sqrt{2}"), (9, "9\\\\sqrt{2}"), (11, "11\\\\sqrt{2}"),\n                     (13, "13\\\\sqrt{2}"), (15, "15\\\\sqrt{2}"), (17, "17\\\\sqrt{2}"), (19, "19\\\\sqrt{2}"), (21, "21\\\\sqrt{2}")]'
p2 = p2.replace(old_333_arch2_data, new_333_arch2_data)

old_333_arch3_data = '[(10, "5\\\\sqrt{2}"), (12, "6\\\\sqrt{2}"), (14, "7\\\\sqrt{2}"), (16, "8\\\\sqrt{2}"), (18, "9\\\\sqrt{2}"),\n                     (20, "10\\\\sqrt{2}"), (22, "11\\\\sqrt{2}"), (24, "12\\\\sqrt{2}"), (26, "13\\\\sqrt{2}"), (28, "14\\\\sqrt{2}")]'
new_333_arch3_data = '[(8, "4\\\\sqrt{2}"), (12, "6\\\\sqrt{2}"), (16, "8\\\\sqrt{2}"), (20, "10\\\\sqrt{2}"), (24, "12\\\\sqrt{2}"),\n                     (28, "14\\\\sqrt{2}"), (32, "16\\\\sqrt{2}"), (36, "18\\\\sqrt{2}"), (40, "20\\\\sqrt{2}"), (48, "24\\\\sqrt{2}")]'
p2 = p2.replace(old_333_arch3_data, new_333_arch3_data)

# 2. 3.4.1 Arch 4: option fix
p2 = p2.replace(
    '["DB equals twice DA", "DA equals twice DB"]',
    '["DB equals two times DA", "DA equals two times DB"]'
)
# 3. 3.4.1 Arch 7: option fixes
p2 = p2.replace('["SSS Test", "AAS Test", "AAA Test"]', '["SSS Congruence Test", "Angle-Angle-Side Test", "AAA Similarity Test"]')
p2 = p2.replace('["Segment AD equals segment BC", "Segment AB equals segment BC"]', '["Segment AD matches segment BC", "Segment AB matches segment BC"]')
p2 = p2.replace('["ASA Test", "AAA Test", "None of these"]', '["Angle-Side-Angle Test", "Angle-Angle-Angle Similarity", "None of these"]')
p2 = p2.replace('["ASA Test", "AAA Test", "RHS Test"]', '["Angle-Side-Angle Test", "Angle-Angle-Angle Similarity", "RHS Congruence Test"]')

# 4. 3.4.1 Arch 6: fix OSC-309 (item 8) where angle A is 60° producing answer 60° matching OSC-219
old_341_arch6_data = '[(30, 120), (40, 100), (35, 110), (45, 90), (25, 130),\n                     (20, 140), (50, 80), (55, 70), (60, 60), (15, 150)]'
new_341_arch6_data = '[(30, 120), (40, 100), (35, 110), (45, 90), (25, 130),\n                     (20, 140), (50, 80), (55, 70), (65, 50), (15, 150)]'
p2 = p2.replace(old_341_arch6_data, new_341_arch6_data)

# 5. 3.4.2 Arch 7: option fix
p2 = p2.replace('["SAS Test", "ASA Test", "AAA Test"]', '["Side-Angle-Side Test", "Angle-Side-Angle Test", "Angle-Angle-Angle Similarity"]')

# 6. 3.5.1 Arch 2 & 4: option fix
p2 = p2.replace('["The initial ray Arm OA", "The terminal ray Arm OB"]', '["The initial arm ray OA", "The terminal arm ray OB"]')
p2 = p2.replace('["\\\\(\\\\Delta = 2 r s\\\\) with factor 2", "\\\\(\\\\Delta = r^2 s\\\\) with squared inradius"]',
                '["Double product \\\\(2 r s\\\\)", "Squared formula \\\\(r^2 s\\\\)"]')

# 7. 3.5.2 Arch 5: similarity test names
p2 = p2.replace('["SAS Congruence Test", "SSS Congruence Test", "RHS Congruence Test"]',
                '["Side-Angle-Side Congruence Test", "Side-Side-Side Congruence Test", "Hypotenuse-Side Congruence Test"]')

with open("scripts/build_clean_ch3_p2.py", "w", encoding="utf-8") as f:
    f.write(p2)
print("Updated build_clean_ch3_p2.py")
