import re

with open('scripts/build_clean_ch2.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace gen_2_1_1 Arch 3
new_211_arch3 = '''        # Arch 3: Find the difference between two co-interior angles from ratio a : b
        {
            'data': [(1, 2, 60, 120, 60), (2, 3, 72, 108, 36), (1, 3, 45, 135, 90), (1, 4, 36, 144, 108), (1, 5, 30, 150, 120),
                     (3, 7, 54, 126, 72), (4, 5, 80, 100, 20), (5, 7, 75, 105, 30), (7, 11, 70, 110, 40), (5, 13, 50, 130, 80)],
            'tmpls': [
                "Two consecutive interior angles between parallel lines stand in the ratio {0} : {1}. Determine the absolute difference between these two angles.",
                "What is the non-negative difference in degrees between two co-interior angles having ratio {0} : {1}?",
                "If co-interior angles are in proportion {0} : {1}, compute their difference: \\\\(\\\\text{{Angle}}_2 - \\\\text{{Angle}}_1\\\\).",
                "Determine the difference between the larger and smaller interior angles whose ratio is {0} : {1}.",
                "Parallel lines cut by a transversal create interior angles in ratio {0} : {1}. Calculate how much larger the obtuse angle is than the acute angle.",
                "Find the gap in degrees between the two consecutive interior angles in ratio {0} : {1}.",
                "Calculate \\\\({1}k - {0}k\\\\) for co-interior angles in ratio {0} : {1} on parallel lines.",
                "Two interior angles on one side of a transversal have ratio {0} : {1}. What is the positive difference between them?",
                "Evaluate \\\\(\\\\text{{Difference}} = \\\\text{{Angle}}_{{\\\\text{{max}}}} - \\\\text{{Angle}}_{{\\\\text{{min}}}}\\\\) for ratio {0} : {1}.",
                "Find the angular difference between the pair of consecutive interior angles with ratio {0} : {1}."
            ],
            'calc': lambda item: (
                f"{item[4]}°",
                [f"{item[4] + 12}°", f"{abs(item[4] - 12)}°", f"{item[4] + 24}°"],
                f"**Step 1: Ratio values**\\\\n\\\\({item[0]}k + {item[1]}k = 180^\\\\circ \\\\implies k = {180 // (item[0]+item[1])}^\\\\circ\\\\).\\\\nAngles are \\\\({item[2]}^\\\\circ\\\\) and \\\\({item[3]}^\\\\circ\\\\).\\\\n**Step 2: Difference**\\\\n\\\\(\\\\text{{Difference}} = {item[3]}^\\\\circ - {item[2]}^\\\\circ = {item[4]}^\\\\circ\\\\).\\\\n**Step 3: Conclusion**\\\\n{item[4]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"diff: {item[4]}°"),
            'diff': 'hard'
        },'''

content = re.sub(r'        # Arch 3: Find the larger interior angle from ratio a : b.*?(?=        # Arch 4: Difference between co-interior angles)', new_211_arch3 + '\n', content, flags=re.DOTALL)

# Replace gen_2_2_2 Arch 5
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
                f"**Step 1: Corresponding Angles Property**\\\\n{item[0]} {item[1]}.\\\\n**Step 2: Conclusion**\\\\n{item[1]}."
            ),
            'svg': lambda item: svg_parallel_transversal("corr prop"),
            'diff': 'medium'
        },'''

content = re.sub(r'        # Arch 5: Bisectors of corresponding angles are parallel.*?(?=        # Arch 6: Vertically opposite to corresponding angle)', new_222_arch5 + '\n', content, flags=re.DOTALL)

with open('scripts/build_clean_ch2.py', 'w', encoding='utf-8') as f:
    f.write(content)
print('Replacement finished successfully.')
