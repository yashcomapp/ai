with open('scripts/build_clean_ch2.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 2.1.1 Arch 5
start_211_arch5 = content.find("        # Arch 5: Angle bisectors of co-interior angles intersect at 90°")
end_211_arch5 = content.find("        # Arch 6: One interior angle is k times the other", start_211_arch5)

new_211_arch5 = '''        # Arch 5: Distinct properties of co-interior angles and parallel lines
        {
            'data': [
                ("The angle bisectors of two interior angles on the same side of a transversal meet at an angle of", "90° (a right angle)", ["180° (a straight angle)", "45° (an acute angle)", "60°"]),
                ("If two parallel lines are cut by a transversal, the sum of the two interior angles on the same side is always", "180° (supplementary)", ["90° (complementary)", "360° (complete angle)", "120°"]),
                ("If one interior angle on one side of a transversal of parallel lines is an acute angle, the other interior angle on that side must be", "An obtuse angle", ["An acute angle", "A right angle", "A straight angle"]),
                ("If one of the co-interior angles of parallel lines is a right angle (90°), the other co-interior angle is", "90°", ["45°", "180°", "0°"]),
                ("If the sum of interior angles on one side of a transversal is 178°, Euclid's Fifth Postulate implies that the lines will", "Intersect on that side", ["Intersect on the opposite side", "Never intersect", "Be strictly parallel"]),
                ("In a trapezium ABCD with AB parallel to CD, the consecutive interior angles A and D are", "Supplementary (sum to 180°)", ["Equal", "Complementary (sum to 90°)", "Reflex angles"]),
                ("If two co-interior angles are equal to each other in parallel lines, each angle must be", "90°", ["45°", "60°", "120°"]),
                ("If the ratio of two interior angles on the same side of a transversal is 1 : 1, the lines cut by the transversal are intersected at an angle of", "90° (perpendicularly)", ["45°", "60°", "30°"]),
                ("The number of pairs of interior angles on the same side of a transversal formed by two lines is", "2 pairs", ["1 pair", "4 pairs", "8 pairs"]),
                ("If a line is perpendicular to one of two parallel lines, the co-interior angle formed with the second parallel line is", "90°", ["45°", "180°", "0°"])
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
                f"**Step 1: Geometric Property**\\\\n{item[0]} {item[1]}.\\\\n**Step 2: Conclusion**\\\\n{item[1]}."
            ),
            'svg': lambda item: svg_parallel_transversal("interior prop"),
            'diff': 'medium'
        },
'''

if start_211_arch5 != -1 and end_211_arch5 != -1:
    content = content[:start_211_arch5] + new_211_arch5 + content[end_211_arch5:]
    print("Replaced 2.1.1 Arch 5")
else:
    print("Could not find 2.1.1 Arch 5 markers")

# 2. 2.4.1 Arch 1
start_241_arch1 = content.find("        # Arch 1: Angles in ratio a : b : c => find smallest angle")
end_241_arch1 = content.find("        # Arch 2: Difference between largest and smallest angle", start_241_arch1)

new_241_arch1 = '''        # Arch 1: Angles in ratio a : b : c => find smallest angle
        {
            'data': [(1, 7, 10, 10, 70, 100), (1, 4, 10, 12, 48, 120), (1, 5, 6, 15, 75, 90),
                     (1, 4, 5, 18, 72, 90), (1, 3, 5, 20, 60, 100), (2, 5, 8, 24, 60, 96),
                     (1, 2, 3, 30, 60, 90), (2, 3, 5, 36, 54, 90), (2, 3, 4, 40, 60, 80), (1, 1, 2, 45, 45, 90)],
            'tmpls': [
                "The angles of a triangle are in the ratio {0} : {1} : {2}. Find the measure of the smallest angle.",
                "If the three angles of a triangle are in ratio {0} : {1} : {2}, calculate the smallest angle.",
                "Angles of a triangle are in ratio {0} : {1} : {2}. What is the measure of the smallest angle?",
                "Determine the smallest angle in a triangle whose angles are in ratio {0} : {1} : {2}.",
                "Find the smallest angle: \\\\frac{{{0}}}{{{0}+{1}+{2}}} \\\\times 180^\\\\circ for ratio {0} : {1} : {2}.",
                "Calculate the minimum angle of a triangle with angle ratio {0} : {1} : {2}.",
                "Evaluate the smallest angle of a triangle having angles in ratio {0} : {1} : {2}.",
                "Compute the smallest angle of triangle when angles are in ratio {0} : {1} : {2}.",
                "If angles of a triangle have ratio {0} : {1} : {2}, find the smallest angle.",
                "For a triangle with angles in ratio {0} : {1} : {2}, calculate the smallest angle."
            ],
            'calc': lambda item: (
                f"{item[3]}°",
                [f"{item[4]}°", f"{item[5]}°", f"{item[3] + 10}°"],
                f"**Step 1: Ratio sum**\\\\n\\\\({item[0]}k + {item[1]}k + {item[2]}k = 180^\\\\circ \\\\implies k = {180 // (item[0]+item[1]+item[2])}^\\\\circ\\\\).\\\\n**Step 2: Smallest angle**\\\\n\\\\(\\\\text{{Smallest angle}} = {item[0]} \\\\times {180 // (item[0]+item[1]+item[2])}^\\\\circ = {item[3]}^\\\\circ\\\\).\\\\n**Step 3: Conclusion**\\\\n{item[3]}°."
            ),
            'svg': lambda item: svg_triangle("A", "B", "C", f"{item[0]}:{item[1]}:{item[2]}"),
            'diff': 'medium'
        },
'''

if start_241_arch1 != -1 and end_241_arch1 != -1:
    content = content[:start_241_arch1] + new_241_arch1 + content[end_241_arch1:]
    print("Replaced 2.4.1 Arch 1")
else:
    print("Could not find 2.4.1 Arch 1 markers")

# 3. 2.4.1 Arch 4
start_241_arch4 = content.find("        # Arch 4: Special triangles: Equilateral")
end_241_arch4 = content.find("        # Arch 5: Angle classification", start_241_arch4)

new_241_arch4 = '''        # Arch 4: Special triangles and angle classification theorems
        {
            'data': [
                ("In an equilateral triangle, what is the measure of each interior angle?", "60°", ["45°", "90°", "30°"]),
                ("In an isosceles right-angled triangle, what is the measure of each acute angle?", "45°", ["60°", "30°", "90°"]),
                ("The sum of the two acute angles in any right-angled triangle is always", "90° (they are complementary)", ["180°", "45°", "60°"]),
                ("A single triangle can have at most how many right angles?", "At most one right angle", ["Two right angles", "Three right angles", "Zero right angles"]),
                ("A single triangle can have at most how many obtuse angles?", "At most one obtuse angle", ["Two obtuse angles", "Three obtuse angles", "Zero obtuse angles"]),
                ("If all three angles of a triangle are strictly less than 90°, the triangle is called an", "Acute-angled triangle", ["Right-angled triangle", "Obtuse-angled triangle", "Equiangular degenerate"]),
                ("If one angle of a triangle equals the sum of the other two angles, the triangle is always a", "Right-angled triangle (since 90° = 90°)", ["Equilateral triangle", "Obtuse triangle", "Acute triangle"]),
                ("In a right-angled triangle, the longest side opposite the 90° angle is called the", "Hypotenuse", ["Base", "Altitude", "Median"]),
                ("If two angles of a triangle are 55° and 65°, the third angle is", "60°", ["50°", "70°", "80°"]),
                ("The sum of any two angles of a triangle is always strictly", "Less than 180°", ["Greater than 180°", "Equal to 180°", "Equal to 90°"])
            ],
            'tmpls': [
                "{0}",
                "Identify the correct geometric fact: {0}",
                "State the property: {0}",
                "According to triangle angle sum theorems: {0}",
                "What is the mathematical conclusion: {0}",
                "Choose the correct statement: {0}",
                "Evaluate the truth: {0}",
                "Select the valid geometric fact: {0}",
                "Fill in the blank: {0}",
                "Determine the property: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Triangle Property**\\\\n{item[0]} {item[1]}.\\\\n**Step 2: Conclusion**\\\\n{item[1]}."
            ),
            'svg': lambda item: svg_triangle("A", "B", "C", "tri prop"),
            'diff': 'easy'
        },
'''

if start_241_arch4 != -1 and end_241_arch4 != -1:
    content = content[:start_241_arch4] + new_241_arch4 + content[end_241_arch4:]
    print("Replaced 2.4.1 Arch 4")
else:
    print("Could not find 2.4.1 Arch 4 markers")

with open('scripts/build_clean_ch2.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully.")
