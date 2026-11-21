# scripts/fix_ch1_final_12.py
with open("scripts/build_clean_ch1.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. In 1.3.3: Make all archetype answer sets disjoint
# Arch 0 answers: 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
# Arch 1: Shift inputs so answers are 40, 42, 44, 46, 48, 50, 52, 54, 56, 58
old_133_arch1 = """        # Arch 1: Given AM, find AB = 2 * AM
        {
            'data': [(7, 14), (8, 16), (9, 18), (10, 20), (11, 22),
                     (12, 24), (13, 26), (14, 28), (15, 30), (16, 32)],"""

new_133_arch1 = """        # Arch 1: Given AM, find AB = 2 * AM
        {
            'data': [(20, 40), (21, 42), (22, 44), (23, 46), (24, 48),
                     (25, 50), (26, 52), (27, 54), (28, 56), (29, 58)],"""

text = text.replace(old_133_arch1, new_133_arch1)

# In 1.3.3 Arch 6 (Given MB, find AM): Change answers to odd decimals or 70..79
old_133_arch6 = """        # Arch 6: Given MB, find AM (AM = MB)
        {
            'data': [(5, 5), (6, 6), (7, 7), (8, 8), (9, 9),
                     (10, 10), (11, 11), (12, 12), (13, 13), (14, 14)],"""

new_133_arch6 = """        # Arch 6: Given MB, find AM (AM = MB)
        {
            'data': [(71, 71), (72, 72), (73, 73), (74, 74), (75, 75),
                     (76, 76), (77, 77), (78, 78), (79, 79), (80, 80)],"""

text = text.replace(old_133_arch6, new_133_arch6)

# In 1.3.3 Arch 7 (AM + MB): Change inputs to 81..90 (answers 162..180)
old_133_arch7 = """        # Arch 7: Sum AM + MB = AB
        {
            'data': [(11, 22), (13, 26), (15, 30), (17, 34), (19, 38),
                     (21, 42), (23, 46), (25, 50), (27, 54), (29, 58)],"""

new_133_arch7 = """        # Arch 7: Sum AM + MB = AB
        {
            'data': [(81, 162), (82, 164), (83, 166), (84, 168), (85, 170),
                     (86, 172), (87, 174), (88, 176), (89, 178), (90, 180)],"""

text = text.replace(old_133_arch7, new_133_arch7)

# 2. In 1.4.2: Create distinct statement lists for Arch 3 and Arch 4
converse_arch4_list = """    converse_pairs_arch4 = [
        ("a triangle is right-angled", "the square of the hypotenuse is the sum of the squares of the other two sides", "Right triangle pythagoras"),
        ("a quadrilateral is a trapezium", "it has exactly one pair of opposite parallel sides", "Trapezium property"),
        ("a point is on the circle", "its distance from the center equals the radius", "Circle point property"),
        ("two angles are supplementary", "their measures sum to 180 degrees", "Supplementary angles"),
        ("two lines are parallel", "they never intersect in the same plane", "Parallel lines non-intersecting"),
        ("a triangle is isosceles", "the altitude to the base bisects the base", "Isosceles base bisector"),
        ("a quadrilateral is a square", "its diagonals are equal and perpendicular", "Square diagonals"),
        ("a line segment has a midpoint", "it is divided into two equal parts", "Midpoint property"),
        ("two triangles are similar", "their corresponding angles are congruent", "Similar triangles equiangular"),
        ("a polygon is regular", "all its sides and all its interior angles are equal", "Regular polygon")
    ]"""

text = text.replace("    converse_pairs = [", converse_arch4_list + "\n    converse_pairs = [")
text = text.replace("'data': [(i, p[0], p[1], p[2]) for i, p in enumerate(converse_pairs)],\n            'tmpls': [\n                \"For the original statement 'If {1}, then {2}', what is the consequent of its CONVERSE?\",",
                   "'data': [(i, p[0], p[1], p[2]) for i, p in enumerate(converse_pairs_arch4)],\n            'tmpls': [\n                \"For the original statement 'If {1}, then {2}', what is the consequent of its CONVERSE?\",")

with open("scripts/build_clean_ch1.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Applied final 12 distinctness fixes to build_clean_ch1.py.")
