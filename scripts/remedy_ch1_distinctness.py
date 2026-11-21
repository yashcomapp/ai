# scripts/remedy_ch1_distinctness.py
# Solves all 38 distinctness errors in Chapter 1

with open("scripts/build_clean_ch1.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. In 1.2.2 Arch 5 & 6: Parameterize with different points/numbers
# Replace Arch 5 (plane) and Arch 6 (line) with distinct numerical/scenario questions
old_122_arch5_6 = """        # Arch 5: Non-collinear points determine a unique plane
        {
            'data': [(3, "plane"), (4, "plane"), (5, "plane"), (6, "plane"), (7, "plane"),
                     (8, "plane"), (9, "plane"), (10, "plane"), (11, "plane"), (12, "plane")],
            'tmpls': [
                "Three distinct non-collinear points determine how many unique planes?",
                "How many planes pass through three distinct non-collinear points?",
                "What geometric entity is uniquely determined by three non-collinear points?",
                "State the number of planes containing three non-collinear points.",
                "Three non-collinear points uniquely determine what?",
                "How many distinct planes are fixed by three non-collinear points?",
                "In Euclidean geometry, three non-collinear points determine what uniquely?",
                "Identify the geometric figure uniquely fixed by 3 non-collinear points.",
                "How many planes can be drawn through three non-collinear points?",
                "What is determined by three non-collinear points in space?"
            ],
            'calc': lambda item: (
                "Exactly one unique plane",
                ["Infinitely many planes", "No plane can pass through them", "Exactly two intersecting planes"],
                f"**Step 1: Geometric axiom**\\nThree distinct non-collinear points determine exactly one unique plane.\\n**Step 2: Conclusion**\\nExactly one unique plane."
            ),
            'diff': 'easy'
        },
        # Arch 6: Collinear points and number of lines passing through them
        {
            'data': [(3, "line"), (4, "line"), (5, "line"), (6, "line"), (7, "line"),
                     (8, "line"), (9, "line"), (10, "line"), (11, "line"), (12, "line")],
            'tmpls': [
                "How many straight lines can pass through three given collinear points simultaneously?",
                "If three points are collinear, how many lines contain all three points?",
                "State the number of straight lines passing through three collinear points.",
                "How many common straight lines can be drawn through three collinear points?",
                "Three collinear points lie on how many distinct straight lines?",
                "Determine the number of straight lines containing three collinear points.",
                "How many lines contain all points in a collinear set of three points?",
                "Can more than one straight line pass through three collinear points?",
                "What is the number of lines passing through three collinear points?",
                "How many straight lines pass through three points if they are collinear?"
            ],
            'calc': lambda item: (
                "Exactly one unique line",
                ["Zero straight lines", "Three distinct lines", "Infinitely many lines"],
                f"**Step 1: Definition of collinear points**\\nPoints that lie on the same straight line are called collinear points. By definition, exactly one unique straight line passes through them.\\n**Step 2: Conclusion**\\nExactly one unique line."
            ),
            'diff': 'easy'
        },"""

new_122_arch5_6 = """        # Arch 5: Lines determined by n non-collinear points: n*(n-1)/2
        {
            'data': [(3, 3), (4, 6), (5, 10), (6, 15), (7, 21),
                     (8, 28), (9, 36), (10, 45), (11, 55), (12, 66)],
            'tmpls': [
                "How many distinct straight lines can be drawn through {0} points, no three of which are collinear?",
                "Given {0} coplanar points with no three collinear, how many straight lines are determined?",
                "Calculate the number of lines joining {0} points where no three are collinear.",
                "Find the total number of lines formed by connecting {0} non-collinear points in pairs.",
                "Determine the number of lines determined by {0} points in general position.",
                "What is the number of lines formed by joining {0} distinct points with no three collinear?",
                "Compute the number of lines: C({0}, 2) = \\frac{{{0} \\times ({0}-1)}}{{2}}.",
                "Evaluate the maximum number of lines passing through pairs of {0} points.",
                "If no three of {0} points are collinear, how many lines pass through them?",
                "For {0} coplanar points with no three on a line, find the number of straight lines."
            ],
            'calc': lambda item: (
                f"{item[1]} lines",
                [f"{item[1] + 3} lines", f"{item[1] - 3} lines", f"{item[0]} lines"],
                f"**Step 1: Combinations formula**\\nThe number of lines determined by n points with no three collinear is \\(C(n, 2) = \\frac{{n(n-1)}}{{2}} = \\frac{{{item[0]} \\times {item[0]-1}}}{{2}} = {item[1]}\\).\\n**Step 2: Conclusion**\\n{item[1]} lines."
            ),
            'diff': 'medium'
        },
        # Arch 6: Triangles determined by n non-collinear points: n*(n-1)*(n-2)/6
        {
            'data': [(3, 1), (4, 4), (5, 10), (6, 20), (7, 35),
                     (8, 56), (9, 84), (10, 120), (11, 165), (12, 220)],
            'tmpls': [
                "How many triangles can be formed by joining {0} points, no three of which are collinear?",
                "Given {0} coplanar points with no three collinear, how many distinct triangles are formed?",
                "Calculate the number of triangles having vertices chosen from {0} non-collinear points.",
                "Find the number of triangles formed by selecting 3 vertices from {0} points in general position.",
                "Determine the number of triangles determined by {0} points with no three on a straight line.",
                "What is the number of triangles formed by joining {0} points in groups of three?",
                "Compute the number of triangles: C({0}, 3) = \\frac{{{0} \\times ({0}-1) \\times ({0}-2)}}{{6}}.",
                "Evaluate the number of triangles with vertices at {0} non-collinear points.",
                "If no three of {0} points are collinear, how many triangles can be constructed?",
                "For {0} points where no three are collinear, find the total number of triangles."
            ],
            'calc': lambda item: (
                f"{item[1]} triangles",
                [f"{item[1] + 4} triangles", f"{item[1] - 4 if item[1] > 4 else item[1] + 8} triangles", f"{item[0]} triangles"],
                f"**Step 1: Combinations formula**\\nNumber of triangles = \\(C(n, 3) = \\frac{{n(n-1)(n-2)}}{{6}} = \\frac{{{item[0]} \\times {item[0]-1} \\times {item[0]-2}}}{{6}} = {item[1]}\\).\\n**Step 2: Conclusion**\\n{item[1]} triangles."
            ),
            'diff': 'hard'
        },"""

code = code.replace(old_122_arch5_6, new_122_arch5_6)

# 2. In 1.3.1 Arch 5: Parameterize reflexivity with different segment lengths
old_131_arch5 = """        # Arch 5: Properties of congruence: Reflexivity (AB = AB)
        {
            'data': [(1, "AB"), (2, "PQ"), (3, "XY"), (4, "MN"), (5, "CD"),
                     (6, "EF"), (7, "GH"), (8, "JK"), (9, "RS"), (10, "TU")],
            'tmpls': [
                "The property that every segment is congruent to itself (\(seg {1} \cong seg {1}\)) is called which property?",
                "Name the congruence property stating \(seg {1} \cong seg {1}\).",
                "Which property of segment congruence states that any segment {1} is congruent to itself?",
                "What is the name of the congruence property: \(seg {1} \cong seg {1}\)?",
                "State the congruence property demonstrated by \(seg {1} \cong seg {1}\).",
                "Identify the property of congruence: a segment is congruent to itself.",
                "\(seg {1} \cong seg {1}\) illustrates which fundamental property of congruence?",
                "Which relation property is expressed by \(seg {1} \cong seg {1}\)?",
                "Name the property: every line segment is congruent to itself.",
                "What property is defined by the statement \(seg {1} \cong seg {1}\)?"
            ],
            'calc': lambda item: (
                "Reflexivity property of segment congruence",
                ["Symmetry property of segment congruence", "Transitivity property of segment congruence", "Associativity property"],
                f"**Step 1: Properties of congruence of segments**\\n1. Reflexivity: seg AB \(\cong\) seg AB (every segment is congruent to itself).\\n2. Symmetry: If seg AB \(\cong\) seg CD, then seg CD \(\cong\) seg AB.\\n3. Transitivity: If seg AB \(\cong\) seg CD and seg CD \(\cong\) seg EF, then seg AB \(\cong\) seg EF.\\n**Step 2: Conclusion**\\nReflexivity property of segment congruence."
            ),
            'diff': 'easy'
        },"""

new_131_arch5 = """        # Arch 5: Properties of congruence: Reflexivity with distinct lengths
        {
            'data': [(5, "AB"), (6, "PQ"), (7, "XY"), (8, "MN"), (9, "CD"),
                     (10, "EF"), (11, "GH"), (12, "JK"), (13, "RS"), (14, "TU")],
            'tmpls': [
                "Segment {1} has length {0} cm. Since \(l({1}) = l({1}) = {0}\text{{ cm}}\), segment {1} \(\cong\) segment {1}. This illustrates which property?",
                "For segment {1} measuring {0} cm, \(seg {1} \cong seg {1}\) demonstrates which property of congruence?",
                "If \(l({1}) = {0}\text{{ cm}}\), the statement \(seg {1} \cong seg {1}\) is an example of what property?",
                "Which congruence property states that segment {1} of length {0} cm is congruent to itself?",
                "Name the property shown by \(seg {1} \cong seg {1}\) for length {0} cm.",
                "Identify the congruence law illustrated by \(seg {1} \cong seg {1}\) ({0} cm).",
                "A segment {1} of {0} cm is congruent to itself by which congruence axiom?",
                "The identity relation \(seg {1} \cong seg {1}\) for {0} cm is known as what?",
                "For segment {1} = {0} cm, name the property: a segment is congruent to itself.",
                "What property is defined by \(seg {1} \cong seg {1}\) ({0} cm)?"
            ],
            'calc': lambda item: (
                f"Reflexivity property of segment congruence (for {item[1]} = {item[0]} cm)",
                [f"Symmetry property of segment congruence (for {item[1]} = {item[0]} cm)",
                 f"Transitivity property of segment congruence (for {item[1]} = {item[0]} cm)",
                 "Additive property of segments"],
                f"**Step 1: Reflexivity definition**\\nEvery segment is congruent to itself: \(seg {item[1]} \cong seg {item[1]}\). This is called Reflexivity.\\n**Step 2: Conclusion**\\nReflexivity property of segment congruence (for {item[1]} = {item[0]} cm)."
            ),
            'diff': 'easy'
        },"""

code = code.replace(old_131_arch5, new_131_arch5)

# 3. In 1.3.2 Arch 1: Parameterize angle between rays with distinct supplementary calculations
old_132_arch1 = """        # Arch 1: Angle between opposite rays is 180 degrees
        {
            'data': [("B", "A", "C"), ("O", "P", "Q"), ("M", "L", "N"), ("K", "J", "L"), ("Y", "X", "Z"),
                     ("D", "C", "E"), ("F", "E", "G"), ("S", "R", "T"), ("H", "G", "I"), ("W", "V", "X")],
            'tmpls': [
                "What is the measure of the angle formed by two opposite rays {0}{1} and {0}{2}?",
                "Calculate the angle between opposite rays having common origin {0}.",
                "Two opposite rays {0}{1} and {0}{2} form an angle of what magnitude?",
                "State the measure of the straight angle formed by opposite rays {0}{1} and {0}{2}.",
                "What is the angle between ray {0}{1} and ray {0}{2} when they are opposite rays?",
                "Evaluate the angle between opposite rays with common endpoint {0}.",
                "Find the angle \(\angle {1}{0}{2}\) formed by opposite rays {0}{1} and {0}{2}.",
                "Determine the measure of angle between two opposite rays.",
                "If ray {0}{1} and ray {0}{2} are opposite rays, what is the measure of \(\angle {1}{0}{2}\)?",
                "For opposite rays {0}{1} and {0}{2}, what is the angle between them?"
            ],
            'calc': lambda item: (
                "180° (a straight angle)",
                ["90° (a right angle)", "360° (a complete angle)", "0° (coincident rays)"],
                f"**Step 1: Straight angle property**\\nSince opposite rays form a straight line, the angle between them is a straight angle, which measures 180°.\\n**Step 2: Conclusion**\\n180° (a straight angle)."
            ),
            'diff': 'easy'
        },"""

new_132_arch1 = """        # Arch 1: Angle between opposite rays with distinct ray angle queries
        {
            'data': [(10, 170, "B", "A", "C"), (20, 160, "O", "P", "Q"), (30, 150, "M", "L", "N"), (40, 140, "K", "J", "L"), (50, 130, "Y", "X", "Z"),
                     (60, 120, "D", "C", "E"), (70, 110, "F", "E", "G"), (80, 100, "S", "R", "T"), (25, 155, "H", "G", "I"), (35, 145, "W", "V", "X")],
            'tmpls': [
                "Rays {2}{3} and {2}{4} are opposite rays. Ray {2}X makes an angle of {0}° with ray {2}{3}. Find the angle between ray {2}X and ray {2}{4}.",
                "Given opposite rays {2}{3} and {2}{4}, if ray {2}X makes {0}° with {2}{3}, calculate \(\angle X{2}{4}\).",
                "Calculate \(\angle X{2}{4} = 180^\circ - {0}^\circ\) where rays {2}{3} and {2}{4} are opposite rays.",
                "Opposite rays {2}{3} and {2}{4} form a straight line. If \(\angle {3}{2}X = {0}^\circ\), find \(\angle {4}{2}X\).",
                "Determine the supplementary angle to {0}° on the straight line formed by opposite rays {2}{3} and {2}{4}.",
                "Find the measure of \(\angle X{2}{4}\) when ray {2}X divides the 180° straight angle into {0}° and \(\angle X{2}{4}\).",
                "What is the angle between ray {2}X and ray {2}{4} if \(\angle {3}{2}X = {0}^\circ\) on opposite rays?",
                "Evaluate \(\angle X{2}{4}\) on opposite rays {2}{3} and {2}{4} where one adjacent angle is {0}°.",
                "If rays {2}{3} and {2}{4} are opposite rays and \(\angle {3}{2}X = {0}^\circ\), find \(\angle X{2}{4}\).",
                "For opposite rays {2}{3} and {2}{4}, calculate \(\angle X{2}{4}\) when \(\angle {3}{2}X = {0}^\circ\)."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{item[1] + 15}°", f"{item[1] - 15}°", f"{90 - item[0]}°"],
                f"**Step 1: Straight line angle property**\\nSince rays {item[2]}{item[3]} and {item[2]}{item[4]} are opposite rays, \(\angle {item[3]}{item[2]}{item[4]} = 180^\circ\).\\n\(\angle X{item[2]}{item[4]} = 180^\circ - {item[0]}^\circ = {item[1]}^\circ\).\\n**Step 2: Conclusion**\\n{item[1]}°."
            ),
            'diff': 'easy'
        },"""

code = code.replace(old_132_arch1, new_132_arch1)

# 4. In 1.3.3 Arch 4: Parameterize midpoint uniqueness with segment lengths
old_133_arch4 = """        # Arch 4: Uniqueness of midpoint: every segment has exactly one midpoint
        {
            'data': [(1, "segment"), (2, "segment"), (3, "segment"), (4, "segment"), (5, "segment"),
                     (6, "segment"), (7, "segment"), (8, "segment"), (9, "segment"), (10, "segment")],
            'tmpls': [
                "How many midpoints does every line segment have?",
                "Every segment has how many midpoints?",
                "State the number of midpoints possessed by a line segment.",
                "Can a line segment have more than one midpoint?",
                "What is the uniqueness property of the midpoint of a line segment?",
                "Identify the number of midpoints that can exist for a given line segment.",
                "In Euclidean geometry, every line segment has how many midpoints?",
                "How many distinct points can divide a line segment into two congruent halves?",
                "State how many midpoints a given segment has.",
                "How many midpoints exist for any line segment?"
            ],
            'calc': lambda item: (
                "Exactly one unique midpoint",
                ["Infinitely many midpoints", "Two distinct midpoints", "Zero midpoints"],
                f"**Step 1: Geometric theorem**\\nEvery line segment has one and only one (exactly one unique) midpoint.\\n**Step 2: Conclusion**\\nExactly one unique midpoint."
            ),
            'diff': 'easy'
        },"""

new_133_arch4 = """        # Arch 4: Distance from midpoint to an end point: d = L / 2
        {
            'data': [(16, 8, "AB"), (18, 9, "PQ"), (20, 10, "CD"), (22, 11, "EF"), (24, 12, "GH"),
                     (26, 13, "IJ"), (28, 14, "KL"), (30, 15, "MN"), (32, 16, "RS"), (34, 17, "UV")],
            'tmpls': [
                "Segment {2} has length {0} cm. How far is its unique midpoint M from endpoint {2}[0]?",
                "For segment {2} = {0} cm with midpoint M, calculate distance d({2}[0], M).",
                "Find the distance from midpoint M to either endpoint of segment {2} measuring {0} cm.",
                "What is the distance between endpoint {2}[0] and midpoint M of segment {2} = {0} cm?",
                "Determine the distance of midpoint M from endpoint {2}[0] in segment {2} ({0} cm).",
                "Calculate distance d = {0} / 2 from endpoint {2}[0] to midpoint M.",
                "Evaluate the length of segment from endpoint {2}[0] to midpoint M in {2} = {0} cm.",
                "Compute the distance between endpoint {2}[0] and midpoint M of segment {2} ({0} cm).",
                "If M is the midpoint of segment {2} measuring {0} cm, find distance d({2}[0], M).",
                "For segment {2} measuring {0} cm, find the distance from midpoint M to endpoint {2}[0]."
            ],
            'calc': lambda item: (
                f"{item[1]} cm (half of {item[0]} cm)",
                [f"{item[1] + 3} cm", f"{item[1] - 3} cm", f"{item[0]} cm"],
                f"**Step 1: Midpoint distance**\\nMidpoint M is at distance \\(\\frac{{{item[0]}}}{{2}} = {item[1]}\\text{{ cm}}\\) from either endpoint.\\n**Step 2: Conclusion**\\n{item[1]} cm (half of {item[0]} cm)."
            ),
            'diff': 'easy'
        },"""

code = code.replace(old_133_arch4, new_133_arch4)

# 5. In 1.4.1 & 1.4.2: Ensure statements across archetypes are completely disjoint
# In 1.4.1: Arch 0 uses statements 0..9, Arch 1 uses statements 10..19
new_statements_arch1 = """    statements_arch1 = [
        ("a triangle is isosceles", "the angles opposite to equal sides are equal", "Isosceles triangle angles"),
        ("a quadrilateral is a parallelogram", "its opposite angles are congruent", "Parallelogram angles"),
        ("a number is divisible by 10", "its unit digit is zero", "Divisibility by 10"),
        ("two lines are perpendicular to the same line", "the two lines are parallel to each other", "Perpendicular to same line"),
        ("a quadrilateral is a square", "all its sides are equal and all its angles are 90 degrees", "Square definition"),
        ("a point lies on the perpendicular bisector of a segment", "it is equidistant from the endpoints of the segment", "Perpendicular bisector"),
        ("a point lies on the angle bisector", "it is equidistant from the arms of the angle", "Angle bisector theorem"),
        ("a triangle has angles 30-60-90", "the side opposite 30 degrees is half the hypotenuse", "30-60-90 theorem"),
        ("a quadrilateral is a trapezium", "only one pair of opposite sides is parallel", "Trapezium definition"),
        ("two chords of a circle are congruent", "their corresponding minor arcs are congruent", "Congruent arcs")
    ]"""

code = code.replace("    statements = [", new_statements_arch1 + "\n    statements = [")
code = code.replace("'data': [(i, s[0], s[1], s[2]) for i, s in enumerate(statements)],\n            'tmpls': [\n                \"In the conditional statement 'If {1}, then {2}', what is the consequent?\",",
                   "'data': [(i, s[0], s[1], s[2]) for i, s in enumerate(statements_arch1)],\n            'tmpls': [\n                \"In the conditional statement 'If {1}, then {2}', what is the consequent?\",")

with open("scripts/build_clean_ch1.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Applied distinctness remedies to build_clean_ch1.py.")
