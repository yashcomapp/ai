import re

with open("scripts/build_clean_ch2.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Patch gen_2_1_1 Arch 3
old_211_arch3 = '''        # Arch 3: Find the larger interior angle from ratio a : b
        {
            'data': [(1, 2, 60, 120), (2, 3, 72, 108), (1, 3, 45, 135), (1, 4, 36, 144), (1, 5, 30, 150),
                     (3, 7, 54, 126), (4, 5, 80, 100), (5, 7, 75, 105), (7, 11, 70, 110), (5, 13, 50, 130)],
            'tmpls': [
                "The ratio of two interior angles on the same side of a transversal of two parallel lines is {0} : {1}. Find the measure of the larger angle.",
                "If interior angles on the same side of a transversal are in the ratio {0} : {1}, calculate the larger interior angle.",
                "Two co-interior angles of parallel lines are in ratio {0} : {1}. What is the measure of the larger angle?",
                "Determine the larger interior angle when the ratio of consecutive interior angles is {0} : {1}.",
                "Find the larger angle among two interior angles in ratio {0} : {1} on parallel lines.",
                "Calculate larger angle: \\frac{{{1}}}{{{0}+{1}}} \\times 180^\\circ for ratio {0} : {1}.",
                "Evaluate the larger co-interior angle having ratio {0} : {1}.",
                "If co-interior angles are in ratio {0} : {1}, compute the measure of the obtuse interior angle.",
                "For parallel lines, two interior angles on one side are in ratio {0} : {1}. Find the larger angle.",
                "Find the measure of the larger of two interior angles whose ratio is {0} : {1}."
            ],
            'calc': lambda item: (
                f"{item[3]}°",
                [f"{item[2]}°", f"{item[3] + 10}°", f"{item[3] - 10}°"],
                f"**Step 1: Ratio calculation**\\n\\({item[0]}k + {item[1]}k = 180^\\circ \\implies k = {180 // (item[0]+item[1])}^\\circ\\).\\n**Step 2: Larger angle**\\n\\(\\text{{Larger angle}} = {item[1]} \\times {180 // (item[0]+item[1])}^\\circ = {item[3]}^\\circ\\).\\n**Step 3: Conclusion**\\n{item[3]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"{item[0]}:{item[1]}"),
            'diff': 'medium'
        },'''

new_211_arch3 = '''        # Arch 3: Find the difference between two co-interior angles from ratio a : b
        {
            'data': [(1, 2, 60, 120, 60), (2, 3, 72, 108, 36), (1, 3, 45, 135, 90), (1, 4, 36, 144, 108), (1, 5, 30, 150, 120),
                     (3, 7, 54, 126, 72), (4, 5, 80, 100, 20), (5, 7, 75, 105, 30), (7, 11, 70, 110, 40), (5, 13, 50, 130, 80)],
            'tmpls': [
                "Two consecutive interior angles between parallel lines stand in the ratio {0} : {1}. Determine the absolute difference between these two angles.",
                "What is the non-negative difference in degrees between two co-interior angles having ratio {0} : {1}?",
                "If co-interior angles are in proportion {0} : {1}, compute their difference: \\(\\text{{Angle}}_2 - \\text{{Angle}}_1\\).",
                "Determine the difference between the larger and smaller interior angles whose ratio is {0} : {1}.",
                "Parallel lines cut by a transversal create interior angles in ratio {0} : {1}. Calculate how much larger the obtuse angle is than the acute angle.",
                "Find the gap in degrees between the two consecutive interior angles in ratio {0} : {1}.",
                "Calculate \\({1}k - {0}k\\) for co-interior angles in ratio {0} : {1} on parallel lines.",
                "Two interior angles on one side of a transversal have ratio {0} : {1}. What is the positive difference between them?",
                "Evaluate \\(\\text{{Difference}} = \\text{{Angle}}_{{\\text{{max}}}} - \\text{{Angle}}_{{\\text{{min}}}}\\) for ratio {0} : {1}.",
                "Find the angular difference between the pair of consecutive interior angles with ratio {0} : {1}."
            ],
            'calc': lambda item: (
                f"{item[4]}°",
                [f"{item[4] + 12}°", f"{abs(item[4] - 12)}°", f"{item[4] + 24}°"],
                f"**Step 1: Ratio values**\\n\\({item[0]}k + {item[1]}k = 180^\\circ \\implies k = {180 // (item[0]+item[1])}^\\circ\\).\\nAngles are \\({item[2]}^\\circ\\) and \\({item[3]}^\\circ\\).\\n**Step 2: Difference**\\n\\(\\text{{Difference}} = {item[3]}^\\circ - {item[2]}^\\circ = {item[4]}^\\circ\\).\\n**Step 3: Conclusion**\\n{item[4]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"diff: {item[4]}°"),
            'diff': 'hard'
        },'''

if old_211_arch3 in content:
    content = content.replace(old_211_arch3, new_211_arch3)
    print("Patched gen_2_1_1 Arch 3")
else:
    print("Could not find old_211_arch3")

# 2. Patch gen_2_2_1 Arch 5
old_221_arch5 = '''        # Arch 5: Angle between bisectors of alternate angles
        {
            'data': [(40, "parallel"), (50, "parallel"), (60, "parallel"), (70, "parallel"), (80, "parallel"),
                     (90, "parallel"), (100, "parallel"), (110, "parallel"), (120, "parallel"), (130, "parallel")],
            'tmpls': [
                "The angle bisectors of a pair of alternate interior angles of parallel lines are what to each other?",
                "What is the geometric relationship between the bisectors of two alternate interior angles of parallel lines?",
                "In parallel lines, the bisectors of alternate interior angles are always what?",
                "State the relationship between bisectors of alternate interior angles.",
                "Are the bisectors of alternate interior angles parallel or perpendicular?",
                "Identify the relationship between the two rays bisecting a pair of alternate angles.",
                "The rays bisecting alternate interior angles of parallel lines are what?",
                "Evaluate the relation between bisectors of alternate interior angles.",
                "For two parallel lines, the bisectors of alternate interior angles are what?",
                "Determine the relationship between the angle bisectors of alternate angles."
            ],
            'calc': lambda item: (
                "Parallel to each other",
                ["Perpendicular to each other (at 90°)", "Intersecting at a 45° angle", "Coincident rays"],
                f"**Step 1: Alternate angle bisectors property**\\nSince the alternate angles are equal (\\(2x = 2x\\)), their halves are equal (\\(x = x\\)). By the Alternate Angles Test, the bisector lines are parallel to each other.\\n**Step 2: Conclusion**\\nParallel to each other."
            ),
            'svg': lambda item: svg_parallel_transversal("bisectors ||"),
            'diff': 'medium'
        },'''

new_221_arch5 = '''        # Arch 5: Distinct geometric properties of angle bisectors and parallel lines
        {
            'data': [
                ("The angle bisectors of a pair of alternate interior angles of parallel lines are", "Parallel to each other", ["Perpendicular to each other", "Intersecting at 45°", "Coincident lines"]),
                ("The angle bisectors of two interior angles on the same side of a transversal of parallel lines are", "Perpendicular to each other (meet at 90°)", ["Parallel to each other", "Intersecting at 60°", "Coincident lines"]),
                ("The quadrilateral formed by the angle bisectors of all four interior angles between parallel lines and a transversal is always a", "Rectangle", ["Rhombus", "Trapezium", "Kite"]),
                ("The angle bisectors of a pair of corresponding angles formed by parallel lines and a transversal are", "Parallel to each other", ["Perpendicular to each other", "Intersecting at 30°", "Skew lines"]),
                ("In a plane, if a straight line is perpendicular to one of two parallel lines, it must be", "Perpendicular to the other line as well", ["Parallel to the other line", "Inclined at 45° to the other line", "Disjoint and non-coplanar"]),
                ("If two parallel lines are intersected by a transversal, each pair of interior angles on the same side are", "Supplementary (sum to 180°)", ["Complementary (sum to 90°)", "Congruent to each other", "Reflex angles"]),
                ("If the bisectors of two interior angles on the same side of a transversal meet at point P, the measure of angle P is", "90°", ["45°", "60°", "180°"]),
                ("If two straight lines in the same plane are both parallel to a third line, they are", "Parallel to each other", ["Perpendicular to each other", "Intersecting at an acute angle", "Skew lines"]),
                ("When two parallel lines are intersected by a transversal, the alternate exterior angles are", "Equal to each other (congruent)", ["Supplementary", "Complementary", "Differing by 90°"]),
                ("If a transversal intersects two parallel lines, the sum of all four interior angles is", "360°", ["180°", "270°", "540°"])
            ],
            'tmpls': [
                "{0} what?",
                "Complete the statement: {0}...",
                "Identify the correct geometric property: {0}...",
                "State the relationship: {0}...",
                "According to geometry theorems, {0}...",
                "What is the valid geometric conclusion: {0}...",
                "Determine the truth: {0}...",
                "Choose the mathematically correct completion: {0}...",
                "Fill in the blank: {0}...",
                "Select the established property: {0}..."
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Geometric Theorem**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'svg': lambda item: svg_parallel_transversal("prop"),
            'diff': 'medium'
        },'''

if old_221_arch5 in content:
    content = content.replace(old_221_arch5, new_221_arch5)
    print("Patched gen_2_2_1 Arch 5")
else:
    print("Could not find old_221_arch5")

# 3. Patch gen_2_2_2 Arch 5
old_222_arch5 = '''        # Arch 5: Angle between bisectors of corresponding angles
        {
            'data': [(40, "parallel"), (50, "parallel"), (60, "parallel"), (70, "parallel"), (80, "parallel"),
                     (90, "parallel"), (100, "parallel"), (110, "parallel"), (120, "parallel"), (130, "parallel")],
            'tmpls': [
                "The angle bisectors of a pair of corresponding angles of parallel lines are what to each other?",
                "What is the geometric relationship between the bisectors of two corresponding angles of parallel lines?",
                "In parallel lines, the bisectors of corresponding angles are always what?",
                "State the relationship between bisectors of corresponding angles.",
                "Are the bisectors of corresponding angles parallel or perpendicular?",
                "Identify the relationship between the two rays bisecting a pair of corresponding angles.",
                "The rays bisecting corresponding angles of parallel lines are what?",
                "Evaluate the relation between bisectors of corresponding angles.",
                "For two parallel lines, the bisectors of corresponding angles are what?",
                "Determine the relationship between the angle bisectors of corresponding angles."
            ],
            'calc': lambda item: (
                "Parallel to each other",
                ["Perpendicular to each other (at 90°)", "Intersecting at a 45° angle", "Coincident rays"],
                f"**Step 1: Corresponding angle bisectors property**\\nSince the corresponding angles are equal (\\(2x = 2x\\)), their halves are equal (\\(x = x\\)). By the Corresponding Angles Test, the bisector lines are parallel to each other.\\n**Step 2: Conclusion**\\nParallel to each other."
            ),
            'svg': lambda item: svg_parallel_transversal("corr bisectors ||"),
            'diff': 'medium'
        },'''

new_222_arch5 = '''        # Arch 5: Distinct geometric properties of corresponding angles and transversals
        {
            'data': [
                ("The angle bisectors of a pair of corresponding angles of parallel lines are", "Parallel to each other", ["Perpendicular to each other", "Intersecting at 45°", "Coincident lines"]),
                ("If a transversal intersects two parallel lines, each pair of corresponding angles are", "Equal to each other (congruent)", ["Supplementary", "Complementary", "Differing by 90°"]),
                ("If a transversal cuts two lines such that a pair of corresponding angles are equal, then the lines are", "Parallel", ["Perpendicular", "Intersecting at 30°", "Skew lines"]),
                ("How many distinct pairs of corresponding angles are formed when a transversal intersects two lines?", "4 pairs", ["2 pairs", "6 pairs", "8 pairs"]),
                ("If two lines are intersected by a transversal and one corresponding angle is 70°, the lines are parallel only if the corresponding partner angle is", "70°", ["110°", "90°", "20°"]),
                ("If corresponding angles on two parallel lines are represented by 3x and 2x + 25, the value of x is", "25", ["15", "35", "50"]),
                ("When two parallel lines are cut by a transversal, the interior angles on the same side and the corresponding angles are related because corresponding angles are equal while interior angles are", "Supplementary to their adjacent linear pair", ["Complementary", "Always acute", "Always obtuse"]),
                ("If two lines perpendicular to the same line are in the same plane, they are", "Parallel to each other", ["Perpendicular to each other", "Intersecting", "Coincident"]),
                ("In proving corresponding angles equal using interior angles, the axiom used as baseline is", "Interior Angles Axiom/Theorem", ["Pythagoras Theorem", "Angle Bisector Theorem", "Exterior Angle Inequality"]),
                ("If a transversal intersects two lines making corresponding angles 89° and 91°, the lines will", "Intersect on the side where sum of interior angles is less than 180°", ["Be strictly parallel", "Be perpendicular", "Never meet in either direction"])
            ],
            'tmpls': [
                "{0} what?",
                "Complete the statement: {0}...",
                "Identify the correct geometric property: {0}...",
                "State the relationship: {0}...",
                "According to geometry theorems, {0}...",
                "What is the valid geometric conclusion: {0}...",
                "Determine the truth: {0}...",
                "Choose the mathematically correct completion: {0}...",
                "Fill in the blank: {0}...",
                "Select the established property: {0}..."
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Corresponding Angles Property**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'svg': lambda item: svg_parallel_transversal("corr prop"),
            'diff': 'medium'
        },'''

if old_222_arch5 in content:
    content = content.replace(old_222_arch5, new_222_arch5)
    print("Patched gen_2_2_2 Arch 5")
else:
    print("Could not find old_222_arch5")

# 4. Patch gen_2_4_1 Arch 2
old_241_arch2 = '''        # Arch 2: Angles in ratio a : b : c => find largest angle
        {
            'data': [(1, 2, 3, 30, 60, 90), (2, 3, 4, 40, 60, 80), (1, 1, 2, 45, 45, 90),
                     (1, 3, 5, 20, 60, 100), (2, 3, 5, 36, 54, 90), (3, 4, 5, 45, 60, 75),
                     (1, 4, 5, 18, 72, 90), (2, 5, 5, 30, 75, 75), (3, 7, 8, 30, 70, 80), (4, 5, 9, 40, 50, 90)],
            'tmpls': [
                "The angles of a triangle are in the ratio {0} : {1} : {2}. Find the measure of the largest angle.",
                "If the three angles of a triangle are in ratio {0} : {1} : {2}, calculate the largest angle.",
                "Angles of a triangle are in ratio {0} : {1} : {2}. What is the measure of the largest angle?",
                "Determine the largest angle in a triangle whose angles are in ratio {0} : {1} : {2}.",
                "Find the largest angle: \\frac{{{2}}}{{{0}+{1}+{2}}} \\times 180^\\circ for ratio {0} : {1} : {2}.",
                "Calculate the maximum angle of a triangle with angle ratio {0} : {1} : {2}.",
                "Evaluate the largest angle of a triangle having angles in ratio {0} : {1} : {2}.",
                "Compute the largest angle of \\(\\Delta ABC\\) when angles are in ratio {0} : {1} : {2}.",
                "If angles of a triangle have ratio {0} : {1} : {2}, find the largest angle.",
                "For a triangle with angles in ratio {0} : {1} : {2}, calculate the largest angle."
            ],
            'calc': lambda item: (
                f"{item[5]}°",
                [f"{item[3]}°", f"{item[4]}°", f"{item[5] - 10}°"],
                f"**Step 1: Ratio sum**\\n\\({item[0]}k + {item[1]}k + {item[2]}k = 180^\\circ \\implies k = {180 // (item[0]+item[1]+item[2])}^\\circ\\).\\n**Step 2: Largest angle**\\n\\(\\text{{Largest angle}} = {item[2]} \\times {180 // (item[0]+item[1]+item[2])}^\\circ = {item[5]}^\\circ\\).\\n**Step 3: Conclusion**\\n{item[5]}°."
            ),
            'svg': lambda item: svg_triangle("A", "B", "C", f"{item[0]}:{item[1]}:{item[2]}"),
            'diff': 'medium'
        },'''

new_241_arch2 = '''        # Arch 2: Difference between largest and smallest angle from ratio a : b : c
        {
            'data': [(1, 2, 3, 30, 60, 90, 60), (2, 3, 4, 40, 60, 80, 40), (1, 1, 2, 45, 45, 90, 45),
                     (1, 3, 5, 20, 60, 100, 80), (2, 3, 5, 36, 54, 90, 54), (3, 4, 5, 45, 60, 75, 30),
                     (1, 4, 5, 18, 72, 90, 72), (2, 5, 5, 30, 75, 75, 45), (3, 7, 8, 30, 70, 80, 50), (4, 5, 9, 40, 50, 90, 50)],
            'tmpls': [
                "The three angles of a triangle are in the ratio {0} : {1} : {2}. Calculate the difference between the largest and smallest angle.",
                "What is the positive difference between the greatest and least angle of a triangle with angle ratio {0} : {1} : {2}?",
                "In a triangle whose angles stand in proportion {0} : {1} : {2}, determine \\(\\angle_{{\\text{{max}}}} - \\angle_{{\\text{{min}}}}\\).",
                "Find the difference between the maximum and minimum angles of \\(\\Delta ABC\\) having ratio {0} : {1} : {2}.",
                "Calculate \\({2}k - {0}k\\) where the angles of a triangle are {0}k, {1}k, {2}k.",
                "Determine the difference in degrees between the extreme angles in a triangle with ratio {0} : {1} : {2}.",
                "Evaluate \\(\\text{{Angle}}_{{\\text{{largest}}}} - \\text{{Angle}}_{{\\text{{smallest}}}}\\) for angle ratio {0} : {1} : {2}.",
                "If angles of \\(\\Delta PQR\\) are in ratio {0} : {1} : {2}, find the gap between the largest and smallest angles.",
                "Find the difference between the largest angle and the smallest angle in a triangle with ratio {0} : {1} : {2}.",
                "Compute the difference between the largest and smallest angles for ratio {0} : {1} : {2} in a triangle."
            ],
            'calc': lambda item: (
                f"{item[6]}°",
                [f"{item[6] + 10}°", f"{abs(item[6] - 10)}°", f"{item[6] + 20}°"],
                f"**Step 1: Ratio values**\\n\\({item[0]}k + {item[1]}k + {item[2]}k = 180^\\circ \\implies k = {180 // (item[0]+item[1]+item[2])}^\\circ\\).\\nAngles are \\({item[3]}^\\circ\\), \\({item[4]}^\\circ\\), and \\({item[5]}^\\circ\\).\\n**Step 2: Difference**\\n\\(\\text{{Difference}} = {item[5]}^\\circ - {item[3]}^\\circ = {item[6]}^\\circ\\).\\n**Step 3: Conclusion**\\n{item[6]}°."
            ),
            'svg': lambda item: svg_triangle("A", "B", "C", f"diff: {item[6]}°"),
            'diff': 'hard'
        },'''

if old_241_arch2 in content:
    content = content.replace(old_241_arch2, new_241_arch2)
    print("Patched gen_2_4_1 Arch 2")
else:
    print("Could not find old_241_arch2")

with open("scripts/build_clean_ch2.py", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated scripts/build_clean_ch2.py successfully")
