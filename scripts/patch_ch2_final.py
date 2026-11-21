with open('scripts/build_clean_ch2.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. In 2.1.1 Arch 6, replace item[0]==2 with item[0]==7 (or 3, 5, etc) so smaller angle is never 60°
start_211_arch6 = content.find("        # Arch 6: One interior angle is k times the other: k*x + x = 180")
end_211_arch6 = content.find("        # Arch 7: Testing whether lines are parallel given sum of interior angles", start_211_arch6)

new_211_arch6 = '''        # Arch 6: One interior angle is k times the other: k*x + x = 180
        {
            'data': [(3, 45, 135), (4, 36, 144), (5, 30, 150), (8, 20, 160), (9, 18, 162),
                     (11, 15, 165), (14, 12, 168), (17, 10, 170), (19, 9, 171), (35, 5, 175)],
            'tmpls': [
                "One interior angle on the same side of a transversal of parallel lines is {0} times the other. Find the smaller angle.",
                "If one co-interior angle is {0} times its adjacent co-interior angle, calculate the smaller angle.",
                "An interior angle is {0} times the other on the same side of a transversal. What is the smaller angle?",
                "Determine the smaller angle if one co-interior angle is {0} times the second.",
                "Find the smaller angle: 180° / ({0} + 1) for parallel lines.",
                "Calculate smaller angle when one interior angle equals {0} times the other.",
                "Evaluate the smaller interior angle if the other is {0} times as large.",
                "Compute the smaller co-interior angle when one angle is {0} times the other.",
                "If an interior angle is {0} times its companion on the same side, find the smaller angle.",
                "For parallel lines, one interior angle is {0} times the other. Calculate the smaller angle."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{item[2]}°", f"{item[1] + 10}°", f"{item[1] - 5}°"],
                f"**Step 1: Equation**\\\\nLet smaller angle be \\\\(x\\\\), larger is \\\\({item[0]}x\\\\).\\\\n\\\\(x + {item[0]}x = 180^\\\\circ \\\\implies {item[0]+1}x = 180^\\\\circ \\\\implies x = {item[1]}^\\\\circ\\\\).\\\\n**Step 2: Conclusion**\\\\n{item[1]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"k = {item[0]}"),
            'diff': 'medium'
        },
'''

if start_211_arch6 != -1 and end_211_arch6 != -1:
    content = content[:start_211_arch6] + new_211_arch6 + content[end_211_arch6:]
    print("Replaced 2.1.1 Arch 6")

# 2. In 2.4.1 Arch 7, replace with 10 distinct proof steps & properties
start_241_arch7 = content.find("        # Arch 7: Construction proof of Angle Sum Theorem: line parallel to base through vertex")
end_241_arch7 = content.find("    ]\n    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)\n\n\n# =====", start_241_arch7)

new_241_arch7 = '''        # Arch 7: Construction and proof steps of the Triangle Angle Sum Theorem
        {
            'data': [
                ("In the textbook proof of the Angle Sum Theorem for triangle ABC, what auxiliary construction line is drawn through vertex A?", "A line parallel to base BC", ["A line perpendicular to base BC", "The angle bisector of angle A", "A median intersecting BC at its midpoint"]),
                ("In the proof that the sum of angles of a triangle is 180°, which theorem equates the alternate angles formed by the parallel line?", "Alternate Interior Angles Theorem", ["Pythagoras Theorem", "Corresponding Angles Axiom", "Midpoint Theorem"]),
                ("In the auxiliary construction through vertex A parallel to BC, the three angles formed on the straight line add up to", "180° (linear triple forming a straight line)", ["360°", "90°", "270°"]),
                ("The proof that the sum of angles of a triangle is 180° depends fundamentally on which of Euclid's postulates?", "Euclid's Fifth Postulate (Parallel Postulate)", ["First Postulate (straight line segment)", "Second Postulate (line extension)", "Third Postulate (circle construction)"]),
                ("If a quadrilateral is divided into two triangles by a single diagonal, the sum of its interior angles is deduced as", "2 × 180° = 360°", ["180°", "540°", "720°"]),
                ("In non-Euclidean spherical geometry on the surface of a sphere, the sum of angles of a triangle is always", "Strictly greater than 180°", ["Strictly equal to 180°", "Strictly less than 180°", "Exactly 90°"]),
                ("In non-Euclidean hyperbolic geometry (saddle-shaped surface), the sum of angles of a triangle is always", "Strictly less than 180°", ["Strictly equal to 180°", "Strictly greater than 180°", "Exactly 270°"]),
                ("The formula for the sum of the interior angles of any n-sided convex polygon is derived from triangles as", "(n - 2) × 180°", ["(n - 1) × 180°", "n × 180°", "(2n - 1) × 180°"]),
                ("By dividing a pentagon (5 sides) into triangles from one vertex, its interior angle sum is", "(5 - 2) × 180° = 540°", ["360°", "720°", "180°"]),
                ("In any triangle, what is the minimum number of acute interior angles it must possess?", "At least two acute angles", ["At least one acute angle", "Exactly three acute angles", "Zero acute angles"])
            ],
            'tmpls': [
                "{0}",
                "State the geometric truth: {0}",
                "Identify the correct mathematical step: {0}",
                "According to the angle sum theorem proof: {0}",
                "What is the valid mathematical result: {0}",
                "Complete the statement: {0}",
                "Select the established property: {0}",
                "Evaluate the conclusion: {0}",
                "Choose the mathematically correct answer: {0}",
                "Determine the fact: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Theorem Step**\\\\n{item[0]} {item[1]}.\\\\n**Step 2: Conclusion**\\\\n{item[1]}."
            ),
            'diff': 'medium'
        }
'''

if start_241_arch7 != -1 and end_241_arch7 != -1:
    content = content[:start_241_arch7] + new_241_arch7 + content[end_241_arch7:]
    print("Replaced 2.4.1 Arch 7")

with open('scripts/build_clean_ch2.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated build_clean_ch2.py successfully.")
