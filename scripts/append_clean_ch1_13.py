# scripts/append_clean_ch1_13.py
import sys, os

code = '''
# =============================================================================
# 1.3.1: Segment definition and length (80 Qs)
# =============================================================================
def gen_1_3_1():
    tc = "MH-9-MTH2-1-1.3.1"
    tname = "Segment definition and length"
    archs = [
        # Arch 0: Congruence of segments: equal lengths => congruent
        {
            'data': [(6, "AB", "CD"), (7, "PQ", "RS"), (8, "EF", "GH"), (9, "MN", "XY"), (10, "JK", "LM"),
                     (11, "TU", "VW"), (12, "BC", "DE"), (13, "QR", "ST"), (14, "OP", "KL"), (15, "YZ", "WX")],
            'tmpls': [
                "If \(l({1}) = {0}\text{{ cm}}\) and \(l({2}) = {0}\text{{ cm}}\), what is the relationship between segment {1} and segment {2}?",
                "Length of segment {1} is {0}\text{{ cm}} and length of segment {2} is {0}\text{{ cm}}. State their relationship.",
                "Two segments {1} and {2} each have length {0}\text{{ cm}}. Are they congruent?",
                "Given \(l({1}) = {0}\text{{ cm}}\) and \(l({2}) = {0}\text{{ cm}}\), determine if segment {1} is congruent to segment {2}.",
                "What can be deduced about segments {1} and {2} if both measure {0}\text{{ cm}}?",
                "State the congruence relation between segment {1} and segment {2} when both are {0}\text{{ cm}} long.",
                "Compare segments {1} and {2} given \(l({1}) = {0}\text{{ cm}}\) and \(l({2}) = {0}\text{{ cm}}\).",
                "Evaluate the relationship between segments {1} and {2} having identical length of {0}\text{{ cm}}.",
                "If segment {1} and segment {2} both have length {0}\text{{ cm}}, identify the true statement.",
                "For segments {1} and {2} measuring {0}\text{{ cm}} each, determine their relation."
            ],
            'calc': lambda item: (
                f"Segment {item[1]} is congruent to segment {item[2]}",
                [f"Segment {item[1]} is longer than segment {item[2]}",
                 f"Segment {item[1]} is shorter than segment {item[2]}",
                 "The two segments are perpendicular"],
                f"**Step 1: Definition of congruent segments**\\nIf the lengths of two segments are equal, then the two segments are congruent.\\nSince \(l({item[1]}) = l({item[2]}) = {item[0]}\text{{ cm}}\), segment {item[1]} \(\cong\) segment {item[2]}.\\n**Step 2: Conclusion**\\nSegment {item[1]} is congruent to segment {item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Comparison of unequal segments: AB > CD
        {
            'data': [(12, 7, "AB", "CD"), (14, 8, "PQ", "RS"), (16, 9, "EF", "GH"), (18, 10, "MN", "XY"), (20, 11, "JK", "LM"),
                     (22, 13, "TU", "VW"), (24, 15, "BC", "DE"), (26, 17, "QR", "ST"), (28, 19, "OP", "KL"), (30, 21, "YZ", "WX")],
            'tmpls': [
                "If \(l({2}) = {0}\text{{ cm}}\) and \(l({3}) = {1}\text{{ cm}}\), compare the two segments.",
                "Compare segments {2} and {3} if \(l({2}) = {0}\text{{ cm}}\) and \(l({3}) = {1}\text{{ cm}}\).",
                "Given lengths \(l({2}) = {0}\text{{ cm}}\) and \(l({3}) = {1}\text{{ cm}}\), state the comparison between them.",
                "Which segment is longer: segment {2} of length {0}\text{{ cm}} or segment {3} of length {1}\text{{ cm}}?",
                "Determine the comparison relation between segment {2} ({0}\text{{ cm}}) and segment {3} ({1}\text{{ cm}}).",
                "Evaluate the inequality between segment {2} measuring {0}\text{{ cm}} and segment {3} measuring {1}\text{{ cm}}.",
                "Compare length of segment {2} ({0}\text{{ cm}}) with segment {3} ({1}\text{{ cm}}).",
                "What is the comparative relation between segment {2} and segment {3}?",
                "State which segment is strictly greater between {2} ({0}\text{{ cm}}) and {3} ({1}\text{{ cm}}).",
                "For segments {2} ({0}\text{{ cm}}) and {3} ({1}\text{{ cm}}), identify the correct inequality."
            ],
            'calc': lambda item: (
                f"Segment {item[2]} is longer than segment {item[3]} (length {item[0]} cm > {item[1]} cm)",
                [f"Segment {item[2]} is shorter than segment {item[3]} (length {item[0]} cm < {item[1]} cm)",
                 f"Segment {item[2]} is congruent to segment {item[3]}",
                 "The two segments cannot be compared"],
                f"**Step 1: Compare lengths**\\n\(l({item[2]}) = {item[0]}\text{{ cm}}\) and \(l({item[3]}) = {item[1]}\text{{ cm}}\).\\nSince {item[0]} > {item[1]}, segment {item[2]} is longer than segment {item[3]}.\\n**Step 2: Conclusion**\\nSegment {item[2]} is longer than segment {item[3]} (length {item[0]} cm > {item[1]} cm)."
            ),
            'diff': 'easy'
        },
        # Arch 2: Comparison of unequal segments: AB < CD
        {
            'data': [(6, 11, "AB", "CD"), (7, 13, "PQ", "RS"), (8, 15, "EF", "GH"), (9, 17, "MN", "XY"), (10, 19, "JK", "LM"),
                     (11, 21, "TU", "VW"), (12, 23, "BC", "DE"), (13, 25, "QR", "ST"), (14, 27, "OP", "KL"), (15, 29, "YZ", "WX")],
            'tmpls': [
                "If \(l({2}) = {0}\text{{ cm}}\) and \(l({3}) = {1}\text{{ cm}}\), compare the two segments.",
                "Compare segments {2} and {3} if \(l({2}) = {0}\text{{ cm}}\) and \(l({3}) = {1}\text{{ cm}}\).",
                "Given lengths \(l({2}) = {0}\text{{ cm}}\) and \(l({3}) = {1}\text{{ cm}}\), state the comparison between them.",
                "Which segment is shorter: segment {2} of length {0}\text{{ cm}} or segment {3} of length {1}\text{{ cm}}?",
                "Determine the comparison relation between segment {2} ({0}\text{{ cm}}) and segment {3} ({1}\text{{ cm}}).",
                "Evaluate the inequality between segment {2} measuring {0}\text{{ cm}} and segment {3} measuring {1}\text{{ cm}}.",
                "Compare length of segment {2} ({0}\text{{ cm}}) with segment {3} ({1}\text{{ cm}}).",
                "What is the comparative relation between segment {2} and segment {3}?",
                "State which segment is smaller between {2} ({0}\text{{ cm}}) and {3} ({1}\text{{ cm}}).",
                "For segments {2} ({0}\text{{ cm}}) and {3} ({1}\text{{ cm}}), identify the correct comparison."
            ],
            'calc': lambda item: (
                f"Segment {item[2]} is shorter than segment {item[3]} (length {item[0]} cm < {item[1]} cm)",
                [f"Segment {item[2]} is longer than segment {item[3]} (length {item[0]} cm > {item[1]} cm)",
                 f"Segment {item[2]} is congruent to segment {item[3]}",
                 "The two segments are parallel"],
                f"**Step 1: Compare lengths**\\n\(l({item[2]}) = {item[0]}\text{{ cm}}\) and \(l({item[3]}) = {item[1]}\text{{ cm}}\).\\nSince {item[0]} < {item[1]}, segment {item[2]} is shorter than segment {item[3]}.\\n**Step 2: Conclusion**\\nSegment {item[2]} is shorter than segment {item[3]} (length {item[0]} cm < {item[1]} cm)."
            ),
            'diff': 'easy'
        },
        # Arch 3: Algebraic equation for congruent segments: ax + b = cx + d => find x
        {
            'data': [(5, 4, 3, 16, 6, 34), (4, 3, 2, 11, 4, 19), (6, 5, 4, 15, 5, 35),
                     (5, 7, 2, 19, 4, 27), (7, 2, 3, 18, 4, 30), (4, 8, 2, 20, 6, 32),
                     (6, 3, 3, 24, 7, 45), (5, 9, 2, 27, 6, 39), (7, 4, 4, 25, 7, 53), (8, 1, 3, 26, 5, 41)],
            'tmpls': [
                "Segments \(AB\) and \(CD\) are congruent. If \(AB = {0}x + {1}\) and \(CD = {2}x + {3}\), find the value of \(x\).",
                "Given \(AB \cong CD\) with \(AB = {0}x + {1}\) and \(CD = {2}x + {3}\), calculate \(x\).",
                "Find \(x\) when congruent segments satisfy \(AB = {0}x + {1}\) and \(CD = {2}x + {3}\).",
                "What is the value of \(x\) if segment \(AB ({0}x + {1})\) equals segment \(CD ({2}x + {3})\)?",
                "Determine \(x\) knowing that \(l(AB) = {0}x + {1}\) and \(l(CD) = {2}x + {3}\) are congruent segments.",
                "Calculate variable \(x\) from the equality of segments \({0}x + {1} = {2}x + {3}\).",
                "Evaluate \(x\) for congruent segments \(AB = {0}x + {1}\) and \(CD = {2}x + {3}\).",
                "Solve for \(x\) given \(AB \cong CD\), \(AB = {0}x + {1}\), and \(CD = {2}x + {3}\).",
                "If segment \(AB\) is congruent to segment \(CD\), find \(x\) where \(AB = {0}x + {1}\) and \(CD = {2}x + {3}\).",
                "For congruent segments with lengths \({0}x + {1}\) and \({2}x + {3}\), calculate \(x\)."
            ],
            'calc': lambda item: (
                f"x = {item[4]}",
                [f"x = {item[4] + 2}", f"x = {item[4] - 2 if item[4] > 2 else item[4] + 4}", f"x = {item[4] + 5}"],
                f"**Step 1: Set equations equal**\\n\({item[0]}x + {item[1]} = {item[2]}x + {item[3]} \implies ({item[0]} - {item[2]})x = {item[3]} - {item[1]} \implies {item[0] - item[2]}x = {item[3] - item[1]}\).\\n**Step 2: Solve for x**\\n\(x = {item[4]}\).\\n**Step 3: Conclusion**\\nx = {item[4]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Union of point A, point B, and all points between them defines segment AB
        {
            'data': [(1, "AB"), (2, "PQ"), (3, "XY"), (4, "MN"), (5, "CD"),
                     (6, "EF"), (7, "GH"), (8, "JK"), (9, "RS"), (10, "TU")],
            'tmpls': [
                "The union of point {1}[0], point {1}[1], and all points between {1}[0] and {1}[1] is called what?",
                "What geometric set is formed by the union set of point {1}[0], point {1}[1], and all points between them?",
                "Name the geometric figure defined as point {1}[0] \(\cup\) point {1}[1] \(\cup\) all points between them.",
                "The union of endpoints {1}[0], {1}[1] and all points between them forms which entity?",
                "Identify the geometric figure composed of {1}[0], {1}[1], and the points between them.",
                "What is the mathematical definition of segment {1}?",
                "The set consisting of points {1}[0] and {1}[1] and all points lying between them is called what?",
                "Define the geometric set: point {1}[0], point {1}[1], and all intermediate points.",
                "In geometry, the collection of point {1}[0], point {1}[1], and all points between them is named what?",
                "State the name of the figure consisting of endpoints {1}[0], {1}[1] and all points between them."
            ],
            'calc': lambda item: (
                f"Line segment {item[1]} (seg {item[1]})",
                [f"Ray {item[1]} with origin {item[1][0]}", f"Infinite line {item[1]}", "A circular arc"],
                f"**Step 1: Formal geometric definition**\\nThe union set of point A, point B, and all points between A and B is called segment AB (seg AB).\\n**Step 2: Conclusion**\\nLine segment {item[1]} (seg {item[1]})."
            ),
            'diff': 'easy'
        },
        # Arch 5: Properties of congruence: Reflexivity (AB = AB)
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
        },
        # Arch 6: Properties of congruence: Symmetry (If AB = CD, then CD = AB)
        {
            'data': [(1, "AB", "CD"), (2, "PQ", "RS"), (3, "XY", "ZW"), (4, "MN", "LK"), (5, "EF", "GH"),
                     (6, "TU", "VW"), (7, "BC", "DE"), (8, "JK", "LM"), (9, "OP", "QR"), (10, "ST", "UV")],
            'tmpls': [
                "The property 'If \(seg {1} \cong seg {2}\), then \(seg {2} \cong seg {1}\)' is known as which property?",
                "Name the congruence property: If \(seg {1} \cong seg {2}\), then \(seg {2} \cong seg {1}\).",
                "Which property of congruence asserts that if segment {1} equals segment {2}, then segment {2} equals segment {1}?",
                "State the congruence property represented by: \(seg {1} \cong seg {2} \implies seg {2} \cong seg {1}\).",
                "Identify the property: If \(seg {1} \cong seg {2}\), then \(seg {2} \cong seg {1}\).",
                "What is the property called where order of congruent segments can be reversed?",
                "The statement 'If \(seg {1} \cong seg {2}\), then \(seg {2} \cong seg {1}\)' illustrates which axiom?",
                "Which congruence relation property is: \(seg {1} \cong seg {2} \implies seg {2} \cong seg {1}\)?",
                "Name the symmetric relation of segment congruence.",
                "Identify the property of segment equality allowing interchange of sides."
            ],
            'calc': lambda item: (
                "Symmetry property of segment congruence",
                ["Reflexivity property of segment congruence", "Transitivity property of segment congruence", "Distributive property"],
                f"**Step 1: Definition of Symmetry**\\nIf seg AB \(\cong\) seg CD, then seg CD \(\cong\) seg AB. This is the Symmetry property of congruence.\\n**Step 2: Conclusion**\\nSymmetry property of segment congruence."
            ),
            'diff': 'easy'
        },
        # Arch 7: Properties of congruence: Transitivity (If AB = CD and CD = EF, then AB = EF)
        {
            'data': [(1, "AB", "CD", "EF"), (2, "PQ", "RS", "TU"), (3, "XY", "ZW", "UV"), (4, "MN", "LK", "OP"), (5, "BC", "DE", "FG"),
                     (6, "GH", "IJ", "KL"), (7, "QR", "ST", "UV"), (8, "JK", "LM", "NO"), (9, "WX", "YZ", "AB"), (10, "CD", "EF", "GH")],
            'tmpls': [
                "The property 'If \(seg {1} \cong seg {2}\) and \(seg {2} \cong seg {3}\), then \(seg {1} \cong seg {3}\)' is called what?",
                "Name the congruence property: If \(seg {1} \cong seg {2}\) and \(seg {2} \cong seg {3}\), then \(seg {1} \cong seg {3}\).",
                "Which property of congruence states that two segments congruent to a third segment are congruent to each other?",
                "State the property: \(seg {1} \cong seg {2}\) and \(seg {2} \cong seg {3} \implies seg {1} \cong seg {3}\).",
                "Identify the property: If \(seg {1} \cong seg {2}\) and \(seg {2} \cong seg {3}\), then \(seg {1} \cong seg {3}\).",
                "What is the property connecting three congruent segments in a chain called?",
                "The deduction that \(seg {1} \cong seg {3}\) from \(seg {1} \cong seg {2}\) and \(seg {2} \cong seg {3}\) is based on what?",
                "Which congruence property is illustrated by: \(seg {1} \cong seg {2}\) and \(seg {2} \cong seg {3} \implies seg {1} \cong seg {3}\)?",
                "Name the transitivity rule for geometric segment congruence.",
                "Identify the transitive law of congruent segments."
            ],
            'calc': lambda item: (
                "Transitivity property of segment congruence",
                ["Reflexivity property of segment congruence", "Symmetry property of segment congruence", "Commutative property"],
                f"**Step 1: Transitivity property**\\nIf seg AB \(\cong\) seg CD and seg CD \(\cong\) seg EF, then seg AB \(\cong\) seg EF. This is the Transitivity property of congruence.\\n**Step 2: Conclusion**\\nTransitivity property of segment congruence."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 1.3.2: Opposite rays (80 Qs)
# =============================================================================
def gen_1_3_2():
    tc = "MH-9-MTH2-1-1.3.2"
    tname = "Opposite rays"
    archs = [
        # Arch 0: Definition of opposite rays: common origin and form a line
        {
            'data': [("B", "A", "C"), ("O", "P", "Q"), ("M", "L", "N"), ("K", "J", "L"), ("Y", "X", "Z"),
                     ("D", "C", "E"), ("F", "E", "G"), ("S", "R", "T"), ("H", "G", "I"), ("W", "V", "X")],
            'tmpls': [
                "Two rays having a common endpoint {0} and forming a straight line are called what?",
                "If ray {0}{1} and ray {0}{2} have common origin {0} and points {1}-{0}-{2} are collinear, what are they called?",
                "What name is given to two rays having a common initial point and opposite directions along the same line?",
                "Rays {0}{1} and {0}{2} share endpoint {0} and lie on line {1}{2}. What type of rays are they?",
                "Identify the term for rays {0}{1} and {0}{2} when {1}-{0}-{2} holds.",
                "When two rays with common origin {0} form a 180° straight angle, they are called what?",
                "What is the mathematical classification for ray {0}{1} and ray {0}{2} having common origin {0} and collinear arms?",
                "State the relationship between ray {0}{1} and ray {0}{2} when they form a straight line.",
                "Name the pair of rays with common origin that together form a complete straight line.",
                "Rays {0}{1} and {0}{2} have common endpoint {0} and form a straight line. What are they called?"
            ],
            'calc': lambda item: (
                f"Opposite rays (ray {item[0]}{item[1]} and ray {item[0]}{item[2]})",
                [f"Intersecting rays at 90°", f"Coincident rays", f"Non-collinear rays"],
                f"**Step 1: Definition of opposite rays**\\nTwo rays which have a common origin and whose union is a straight line are called opposite rays.\\n**Step 2: Conclusion**\\nOpposite rays (ray {item[0]}{item[1]} and ray {item[0]}{item[2]})."
            ),
            'diff': 'easy'
        },
        # Arch 1: Angle between opposite rays is 180 degrees
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
        },
        # Arch 2: Identify opposite rays from collinear points A-B-C
        {
            'data': [("A", "B", "C"), ("P", "Q", "R"), ("X", "Y", "Z"), ("L", "M", "N"), ("D", "E", "F"),
                     ("G", "H", "I"), ("R", "S", "T"), ("J", "K", "L"), ("U", "V", "W"), ("M", "N", "O")],
            'tmpls': [
                "If points are arranged in betweenness order {0}-{1}-{2}, name the pair of opposite rays with common endpoint {1}.",
                "For collinear points {0}-{1}-{2}, which two rays are opposite rays?",
                "Given betweenness {0}-{1}-{2}, identify the opposite rays originating at point {1}.",
                "Name the opposite rays formed at point {1} when {0}-{1}-{2} holds.",
                "In the figure with order {0}-{1}-{2}, state the pair of opposite rays.",
                "Which pair of rays with origin {1} are opposite rays for collinear order {0}-{1}-{2}?",
                "Identify the opposite rays with initial point {1} given {0}-{1}-{2}.",
                "From betweenness {0}-{1}-{2}, write down the pair of opposite rays.",
                "If {0}-{1}-{2} are collinear points, what are the opposite rays starting at {1}?",
                "For collinear order {0}-{1}-{2}, find the opposite rays with vertex {1}."
            ],
            'calc': lambda item: (
                f"Ray {item[1]}{item[0]} and ray {item[1]}{item[2]} are opposite rays",
                [f"Ray {item[0]}{item[1]} and ray {item[2]}{item[1]} are opposite rays",
                 f"Ray {item[1]}{item[0]} and ray {item[0]}{item[2]} are opposite rays",
                 f"Ray {item[0]}{item[2]} and ray {item[2]}{item[0]} are opposite rays"],
                f"**Step 1: Identify rays from common origin {item[1]}**\\nSince {item[0]}-{item[1]}-{item[2]}, ray {item[1]}{item[0]} extends towards {item[0]} and ray {item[1]}{item[2]} extends towards {item[2]} in opposite directions along line {item[0]}{item[2]}.\\n**Step 2: Conclusion**\\nRay {item[1]}{item[0]} and ray {item[1]}{item[2]} are opposite rays."
            ),
            'diff': 'medium'
        },
        # Arch 3: Rays that have common origin but do NOT form a line are NOT opposite rays
        {
            'data': [(30, "A", "O", "B"), (45, "P", "O", "Q"), (60, "X", "O", "Y"), (75, "L", "O", "M"), (90, "D", "O", "E"),
                     (105, "F", "O", "G"), (120, "R", "O", "S"), (135, "J", "O", "K"), (150, "U", "O", "V"), (160, "M", "O", "N")],
            'tmpls': [
                "Ray O{1} and ray O{2} have common endpoint O, but \(\angle {1}O{2} = {0}^\circ\). Are they opposite rays?",
                "If \(\angle {1}O{2} = {0}^\circ\), are ray O{1} and ray O{2} opposite rays?",
                "Two rays O{1} and O{2} meet at O with an angle of {0}°. Do they form opposite rays?",
                "Can ray O{1} and ray O{2} be called opposite rays if the angle between them is {0}°?",
                "State whether ray O{1} and ray O{2} are opposite rays when \(\angle {1}O{2} = {0}^\circ\).",
                "Determine if ray O{1} and ray O{2} are opposite rays given \(\angle {1}O{2} = {0}^\circ\).",
                "Evaluate if two rays forming a {0}° angle are opposite rays.",
                "Are rays O{1} and O{2} opposite rays if \(\angle {1}O{2} = {0}^\circ \ne 180^\circ\)?",
                "Check whether ray O{1} and ray O{2} are opposite rays when their angle is {0}°.",
                "For rays O{1} and O{2} with \(\angle {1}O{2} = {0}^\circ\), are they opposite rays?"
            ],
            'calc': lambda item: (
                f"No, because the angle between them is {item[0]}° (not 180°)",
                ["Yes, because they share a common vertex O", "Yes, any two rays with a common vertex are opposite rays", "Cannot be determined without their lengths"],
                f"**Step 1: Criterion for opposite rays**\\nOpposite rays must have a common endpoint AND their union must be a straight line (angle = 180°).\\nHere \(\angle {item[1]}O{item[2]} = {item[0]}^\circ \\ne 180^\circ\), so they are not opposite rays.\\n**Step 2: Conclusion**\\nNo, because the angle between them is {item[0]}° (not 180°)."
            ),
            'diff': 'easy'
        },
        # Arch 4: Intersection of opposite rays: ray OA intersect ray OB = {O}
        {
            'data': [("O", "A", "B"), ("P", "Q", "R"), ("M", "L", "N"), ("K", "J", "L"), ("Y", "X", "Z"),
                     ("D", "C", "E"), ("F", "E", "G"), ("S", "R", "T"), ("H", "G", "I"), ("W", "V", "X")],
            'tmpls': [
                "What is the intersection of two opposite rays {0}{1} and {0}{2}?",
                "Find the intersection set of opposite rays {0}{1} and {0}{2}.",
                "If ray {0}{1} and ray {0}{2} are opposite rays, what is (ray {0}{1} \(\cap\) ray {0}{2})?",
                "What common point(s) do opposite rays {0}{1} and {0}{2} share?",
                "Determine the intersection of opposite rays {0}{1} and {0}{2}.",
                "State the intersection of ray {0}{1} and ray {0}{2} when they are opposite rays.",
                "The intersection of two opposite rays with origin {0} consists of what?",
                "Evaluate: (ray {0}{1}) \(\cap\) (ray {0}{2}) where the rays are opposite rays.",
                "What is the set-theoretic intersection of opposite rays {0}{1} and {0}{2}?",
                "For opposite rays {0}{1} and {0}{2}, identify their intersection."
            ],
            'calc': lambda item: (
                f"The single origin point {{{item[0]}}}",
                [f"The entire line {item[1]}{item[2]}", f"The line segment {item[1]}{item[2]}", "The empty set (no intersection)"],
                f"**Step 1: Ray intersection**\\nOpposite rays extend in opposite directions from their common origin {item[0]}. They share only the origin point {item[0]}.\\n**Step 2: Conclusion**\\nThe single origin point {{{item[0]}}}."
            ),
            'diff': 'easy'
        },
        # Arch 5: Union of opposite rays: ray OA union ray OB = line AB
        {
            'data': [("O", "A", "B"), ("P", "Q", "R"), ("M", "L", "N"), ("K", "J", "L"), ("Y", "X", "Z"),
                     ("D", "C", "E"), ("F", "E", "G"), ("S", "R", "T"), ("H", "G", "I"), ("W", "V", "X")],
            'tmpls': [
                "What is the union of two opposite rays {0}{1} and {0}{2}?",
                "Find the union set: (ray {0}{1}) \(\cup\) (ray {0}{2}) for opposite rays.",
                "If ray {0}{1} and ray {0}{2} are opposite rays, their union forms what geometric figure?",
                "The union of two opposite rays having common endpoint {0} is called what?",
                "Determine the union of opposite rays {0}{1} and {0}{2}.",
                "State what figure is formed by the union of opposite rays {0}{1} and {0}{2}.",
                "What geometric entity results from the union of opposite rays {0}{1} and {0}{2}?",
                "Evaluate: (ray {0}{1}) \(\cup\) (ray {0}{2}) where they are opposite rays.",
                "The set of points in ray {0}{1} together with ray {0}{2} constitutes what?",
                "For opposite rays {0}{1} and {0}{2}, identify their union."
            ],
            'calc': lambda item: (
                f"The infinite line {item[1]}{item[2]} (line {item[1]}{item[2]})",
                [f"The line segment {item[1]}{item[2]}", f"The single origin point {{{item[0]}}}", "A circular boundary"],
                f"**Step 1: Ray union**\\nThe union of two opposite rays ray {item[0]}{item[1]} and ray {item[0]}{item[2]} is the complete line {item[1]}{item[2]}.\\n**Step 2: Conclusion**\\nThe infinite line {item[1]}{item[2]} (line {item[1]}{item[2]})."
            ),
            'diff': 'easy'
        },
        # Arch 6: Non-opposite collinear rays: Ray AB and Ray AC when A-B-C (Ray AB is subset of Ray AC)
        {
            'data': [("A", "B", "C"), ("P", "Q", "R"), ("X", "Y", "Z"), ("L", "M", "N"), ("D", "E", "F"),
                     ("G", "H", "I"), ("R", "S", "T"), ("J", "K", "L"), ("U", "V", "W"), ("M", "N", "O")],
            'tmpls': [
                "If {0}-{1}-{2}, are ray {0}{1} and ray {0}{2} opposite rays?",
                "Points are arranged as {0}-{1}-{2}. Are ray {0}{1} and ray {0}{2} opposite rays?",
                "State whether ray {0}{1} and ray {0}{2} are opposite rays when {0}-{1}-{2} holds.",
                "Given collinear order {0}-{1}-{2}, determine if ray {0}{1} and ray {0}{2} are opposite.",
                "Can ray {0}{1} and ray {0}{2} be considered opposite rays if {0}-{1}-{2}?",
                "Evaluate if ray {0}{1} and ray {0}{2} are opposite rays for betweenness {0}-{1}-{2}.",
                "Check if ray {0}{1} and ray {0}{2} are opposite rays given {0}-{1}-{2}.",
                "For collinear points {0}-{1}-{2}, are ray {0}{1} and ray {0}{2} opposite rays?",
                "If {0}-{1}-{2}, state the relationship between ray {0}{1} and ray {0}{2}.",
                "Are ray {0}{1} and ray {0}{2} opposite rays when {0} is the initial point of both?"
            ],
            'calc': lambda item: (
                f"No, they are identical rays pointing in the same direction (ray {item[0]}{item[1]} is ray {item[0]}{item[2]})",
                [f"Yes, because they have a common endpoint {item[0]}", "Yes, they form a 180° angle", "Cannot be determined without coordinates"],
                f"**Step 1: Check ray directions**\\nBoth ray {item[0]}{item[1]} and ray {item[0]}{item[2]} start at {item[0]} and point in the SAME direction towards {item[2]}. Therefore, they are the same ray, NOT opposite rays.\\n**Step 2: Conclusion**\\nNo, they are identical rays pointing in the same direction (ray {item[0]}{item[1]} is ray {item[0]}{item[2]})."
            ),
            'diff': 'medium'
        },
        # Arch 7: Linear pair formed by a ray standing on opposite rays
        {
            'data': [(40, 140), (50, 130), (60, 120), (70, 110), (80, 100),
                     (45, 135), (55, 125), (65, 115), (75, 105), (85, 95)],
            'tmpls': [
                "Two opposite rays form a straight line. If a third ray stands on this line making an angle of {0}°, find the adjacent angle.",
                "A ray stands on a line formed by opposite rays. If one linear pair angle is {0}°, calculate the other angle.",
                "Find the supplementary adjacent angle if one angle on a straight line measures {0}°.",
                "What is the measure of the linear pair angle adjacent to {0}° on a straight line?",
                "Determine the adjacent angle on opposite rays when one angle is {0}°.",
                "Calculate the measure of angle \(180^\circ - {0}^\circ\) formed on opposite rays.",
                "Compute the linear pair angle formed by a ray standing on opposite rays with one angle = {0}°.",
                "Evaluate the angle adjacent to {0}° formed on a straight line.",
                "If two angles form a linear pair on opposite rays and one is {0}°, find the other.",
                "For a ray standing on opposite rays, find the remaining angle if one angle is {0}°."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{item[1] + 10}°", f"{item[1] - 10}°", f"{90 - item[0]}°"],
                f"**Step 1: Linear pair property**\\nAngles forming a linear pair on opposite rays are supplementary: \(\text{{Angle}} = 180^\circ - {item[0]}^\circ = {item[1]}^\circ\).\\n**Step 2: Conclusion**\\n{item[1]}°."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 1.3.3: Midpoint: AM = MB = 1/2 AB (80 Qs)
# =============================================================================
def gen_1_3_3():
    tc = "MH-9-MTH2-1-1.3.3"
    tname = "Midpoint: AM = MB = 1/2 AB"
    archs = [
        # Arch 0: Given AB, find AM = AB / 2
        {
            'data': [(12, 6), (14, 7), (16, 8), (18, 9), (20, 10),
                     (22, 11), (24, 12), (26, 13), (28, 14), (30, 15)],
            'tmpls': [
                "Point \(M\) is the midpoint of segment \(AB\). If \(AB = {0}\text{{ cm}}\), find length of segment \(AM\).",
                "If \(M\) is the midpoint of \(AB\) and \(AB = {0}\text{{ cm}}\), calculate \(AM\).",
                "Calculate length \(AM\) where \(M\) is the midpoint of segment \(AB = {0}\text{{ cm}}\).",
                "What is the length of \(AM\) if \(M\) bisects segment \(AB = {0}\text{{ cm}}\)?",
                "Determine \(AM\) given \(l(AB) = {0}\text{{ cm}}\) and \(M\) is the midpoint.",
                "Find \(AM = \frac{{AB}}{{2}}\) for \(AB = {0}\text{{ cm}}\).",
                "Compute \(l(AM)\) in segment \(AB = {0}\text{{ cm}}\) with midpoint \(M\).",
                "Evaluate length of segment \(AM\) when \(M\) is the midpoint of \(AB = {0}\text{{ cm}}\).",
                "If \(M\) is the midpoint of segment \(AB\) measuring {0}\text{{ cm}}, find \(AM\).",
                "For segment \(AB = {0}\text{{ cm}}\) with midpoint \(M\), calculate \(AM\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 2} cm", f"{item[1] - 2} cm", f"{item[0] + 2} cm"],
                f"**Step 1: Formula**\\n\(AM = \frac{{AB}}{{2}} = \frac{{{item[0]}}}{{2}} = {item[1]}\text{{ cm}}\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'svg': lambda item: svg_segment_midpoint("A", "M", "B", f"AB = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 1: Given AM, find AB = 2 * AM
        {
            'data': [(7, 14), (8, 16), (9, 18), (10, 20), (11, 22),
                     (12, 24), (13, 26), (14, 28), (15, 30), (16, 32)],
            'tmpls': [
                "Point \(M\) is the midpoint of segment \(AB\). If \(AM = {0}\text{{ cm}}\), find total length \(AB\).",
                "If \(M\) is the midpoint of \(AB\) and \(AM = {0}\text{{ cm}}\), calculate \(l(AB)\).",
                "Calculate length \(AB\) where \(M\) is the midpoint and \(AM = {0}\text{{ cm}}\).",
                "What is the length of segment \(AB\) if \(M\) is the midpoint and \(AM = {0}\text{{ cm}}\)?",
                "Determine \(AB\) given \(AM = {0}\text{{ cm}}\) and \(M\) bisects \(AB\).",
                "Find \(AB = 2 \times AM\) for \(AM = {0}\text{{ cm}}\).",
                "Compute \(l(AB)\) when midpoint segment \(AM = {0}\text{{ cm}}\).",
                "Evaluate total length \(AB\) when \(AM = {0}\text{{ cm}}\) and \(M\) is the midpoint.",
                "If \(M\) is the midpoint of segment \(AB\) with \(AM = {0}\text{{ cm}}\), find \(AB\).",
                "For segment \(AB\) with midpoint \(M\), calculate \(AB\) if \(AM = {0}\text{{ cm}}\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 4} cm", f"{item[1] - 4} cm", f"{item[0]} cm"],
                f"**Step 1: Formula**\\n\(AB = 2 \times AM = 2 \times {item[0]} = {item[1]}\text{{ cm}}\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'svg': lambda item: svg_segment_midpoint("A", "M", "B", f"AM = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 2: Algebraic midpoint: AM = MB => ax - b = cx + d => find x
        {
            'data': [(4, 3, 2, 9, 6, 21), (5, 4, 3, 10, 7, 31), (6, 2, 3, 13, 5, 28),
                     (4, 5, 2, 11, 8, 27), (5, 6, 2, 18, 8, 34), (6, 4, 2, 20, 6, 32),
                     (7, 3, 4, 15, 6, 39), (5, 8, 3, 16, 12, 52), (6, 5, 3, 19, 8, 43), (7, 2, 3, 22, 6, 40)],
            'tmpls': [
                "Point \(M\) is the midpoint of segment \(AB\). If \(AM = {0}x - {1}\) and \(MB = {2}x + {3}\), find \(x\).",
                "Given \(M\) is the midpoint of \(AB\) with \(AM = {0}x - {1}\) and \(MB = {2}x + {3}\), calculate \(x\).",
                "Calculate \(x\) when midpoint \(M\) divides \(AB\) into \(AM = {0}x - {1}\) and \(MB = {2}x + {3}\).",
                "What is the value of \(x\) if \(M\) is the midpoint of \(AB\), \(AM = {0}x - {1}\), and \(MB = {2}x + {3}\)?",
                "Determine \(x\) given that \(M\) bisects \(AB\) with \(AM = {0}x - {1}\) and \(MB = {2}x + {3}\).",
                "Find \(x\) by equating \(AM = MB\): \({0}x - {1} = {2}x + {3}\).",
                "Compute variable \(x\) for midpoint \(M\) of \(AB\) with \(AM = {0}x - {1}\) and \(MB = {2}x + {3}\).",
                "Evaluate \(x\) knowing \(AM = MB\) where \(AM = {0}x - {1}\) and \(MB = {2}x + {3}\).",
                "If \(M\) is the midpoint of \(AB\), find \(x\) from \(AM = {0}x - {1}\) and \(MB = {2}x + {3}\).",
                "For midpoint \(M\) of \(AB\), calculate \(x\) when \(AM = {0}x - {1}\) and \(MB = {2}x + {3}\)."
            ],
            'calc': lambda item: (
                f"x = {item[4]}",
                [f"x = {item[4] + 2}", f"x = {item[4] - 2 if item[4] > 2 else item[4] + 4}", f"x = {item[4] + 5}"],
                f"**Step 1: Midpoint equality**\\nSince \(M\) is the midpoint, \(AM = MB \implies {item[0]}x - {item[1]} = {item[2]}x + {item[3]} \implies ({item[0]} - {item[2]})x = {item[3]} + {item[1]} \implies {item[0] - item[2]}x = {item[3] + item[1]}\).\\n**Step 2: Solve for x**\\n\(x = {item[4]}\).\\n**Step 3: Conclusion**\\nx = {item[4]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Algebraic midpoint: find total length AB from x
        {
            'data': [(3, 4, 2, 9, 5, 38), (4, 3, 2, 7, 5, 34), (5, 2, 3, 8, 5, 46),
                     (4, 5, 2, 11, 8, 54), (5, 6, 2, 18, 8, 68), (6, 4, 3, 14, 6, 64),
                     (4, 7, 2, 15, 8, 50), (5, 3, 2, 15, 6, 54), (6, 2, 3, 16, 6, 68), (5, 5, 2, 20, 5, 40)],
            'tmpls': [
                "Point \(M\) is the midpoint of segment \(AB\). If \(AM = {0}x + {1}\) and \(MB = {2}x + {3}\), find the total length of segment \(AB\).",
                "Given midpoint \(M\) of \(AB\) with \(AM = {0}x + {1}\) and \(MB = {2}x + {3}\), calculate \(l(AB)\).",
                "Calculate \(AB\) when \(M\) is the midpoint of \(AB\), \(AM = {0}x + {1}\), and \(MB = {2}x + {3}\).",
                "What is the total length \(AB\) if \(M\) bisects \(AB\) with \(AM = {0}x + {1}\) and \(MB = {2}x + {3}\)?",
                "Determine the length of segment \(AB\) knowing \(M\) is the midpoint with \(AM = {0}x + {1}\) and \(MB = {2}x + {3}\).",
                "Find \(AB = 2 \times AM\) after solving for \(x\) in \({0}x + {1} = {2}x + {3}\).",
                "Compute total length \(AB\) with midpoint \(M\) where \(AM = {0}x + {1}\) and \(MB = {2}x + {3}\).",
                "Evaluate segment length \(AB\) for midpoint \(M\) with \(AM = {0}x + {1}\) and \(MB = {2}x + {3}\).",
                "If \(M\) is the midpoint of \(AB\), find total length \(AB\) given \(AM = {0}x + {1}\) and \(MB = {2}x + {3}\).",
                "For midpoint \(M\) of \(AB\), calculate total length \(AB\) when \(AM = {0}x + {1}\) and \(MB = {2}x + {3}\)."
            ],
            'calc': lambda item: (
                f"{item[5]} cm",
                [f"{item[5] + 6} cm", f"{item[5] - 6} cm", f"{item[5] // 2} cm"],
                f"**Step 1: Equate AM = MB**\\n\({item[0]}x + {item[1]} = {item[2]}x + {item[3]} \implies {item[0] - item[2]}x = {item[3] - item[1]} \implies x = {item[4]}\).\\n**Step 2: Calculate AB**\\n\(AM = {item[0]}({item[4]}) + {item[1]} = {item[5] // 2}\text{{ cm}}\).\\n\(AB = 2 \times AM = 2 \times {item[5] // 2} = {item[5]}\text{{ cm}}\).\\n**Step 3: Conclusion**\\n{item[5]} cm."
            ),
            'diff': 'hard'
        },
        # Arch 4: Uniqueness of midpoint: every segment has exactly one midpoint
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
        },
        # Arch 5: Midpoint with decimal values
        {
            'data': [(7.4, 3.7), (8.6, 4.3), (9.8, 4.9), (11.2, 5.6), (13.4, 6.7),
                     (15.8, 7.9), (17.2, 8.6), (19.4, 9.7), (21.6, 10.8), (23.8, 11.9)],
            'tmpls': [
                "If \(P\) is the midpoint of segment \(CD = {0}\text{{ cm}}\), find \(CP\).",
                "Point \(P\) bisects segment \(CD = {0}\text{{ cm}}\). Calculate \(CP\).",
                "Calculate length \(CP\) where \(P\) is the midpoint of \(CD = {0}\text{{ cm}}\).",
                "What is \(CP\) if \(P\) is the midpoint of segment \(CD = {0}\text{{ cm}}\)?",
                "Determine \(CP\) given \(l(CD) = {0}\text{{ cm}}\) and \(P\) is the midpoint.",
                "Find \(CP = \frac{{CD}}{{2}}\) for \(CD = {0}\text{{ cm}}\).",
                "Compute \(l(CP)\) in segment \(CD = {0}\text{{ cm}}\) with midpoint \(P\).",
                "Evaluate length of segment \(CP\) when \(P\) is the midpoint of \(CD = {0}\text{{ cm}}\).",
                "If \(P\) is the midpoint of \(CD = {0}\text{{ cm}}\), find \(CP\).",
                "For segment \(CD = {0}\text{{ cm}}\) with midpoint \(P\), calculate \(CP\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{round(item[1] + 1.2, 1)} cm", f"{round(item[1] - 1.2, 1)} cm", f"{item[0]} cm"],
                f"**Step 1: Formula**\\n\(CP = \frac{{CD}}{{2}} = \frac{{{item[0]}}}{{2}} = {item[1]}\text{{ cm}}\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'svg': lambda item: svg_segment_midpoint("C", "P", "D", f"CD = {item[0]} cm"),
            'diff': 'medium'
        },
        # Arch 6: Given MB, find AM (AM = MB)
        {
            'data': [(5, 5), (6, 6), (7, 7), (8, 8), (9, 9),
                     (10, 10), (11, 11), (12, 12), (13, 13), (14, 14)],
            'tmpls': [
                "Point \(M\) is the midpoint of segment \(AB\). If \(MB = {0}\text{{ cm}}\), what is length \(AM\)?",
                "If \(M\) bisects segment \(AB\) and \(MB = {0}\text{{ cm}}\), find \(AM\).",
                "Calculate \(AM\) when \(M\) is the midpoint of \(AB\) and \(MB = {0}\text{{ cm}}\).",
                "What is the length of \(AM\) if \(M\) is the midpoint of \(AB\) and \(MB = {0}\text{{ cm}}\)?",
                "Determine \(AM\) given \(M\) is the midpoint of \(AB\) and \(MB = {0}\text{{ cm}}\).",
                "Find \(AM\) knowing \(AM = MB\) for midpoint \(M\) with \(MB = {0}\text{{ cm}}\).",
                "Compute \(l(AM)\) when \(M\) is the midpoint of \(AB\) and \(MB = {0}\text{{ cm}}\).",
                "Evaluate \(AM\) where \(M\) is the midpoint of \(AB\) and \(MB = {0}\text{{ cm}}\).",
                "If \(M\) is the midpoint of \(AB\) with \(MB = {0}\text{{ cm}}\), find \(AM\).",
                "For midpoint \(M\) of \(AB\) with \(MB = {0}\text{{ cm}}\), calculate \(AM\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] * 2} cm", f"{item[1] + 3} cm", f"{item[1] - 2 if item[1] > 2 else item[1] + 4} cm"],
                f"**Step 1: Midpoint definition**\\nA midpoint divides the segment into two congruent halves: \(AM = MB = {item[0]}\text{{ cm}}\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'svg': lambda item: svg_segment_midpoint("A", "M", "B", f"MB = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 7: Sum AM + MB = AB
        {
            'data': [(11, 22), (13, 26), (15, 30), (17, 34), (19, 38),
                     (21, 42), (23, 46), (25, 50), (27, 54), (29, 58)],
            'tmpls': [
                "Point \(M\) is the midpoint of segment \(AB\). If \(AM = {0}\text{{ cm}}\), find \(AM + MB\).",
                "If \(M\) is the midpoint of \(AB\) and \(AM = {0}\text{{ cm}}\), calculate the sum \(AM + MB\).",
                "Calculate the total length \(AM + MB\) where \(M\) is the midpoint of \(AB\) and \(AM = {0}\text{{ cm}}\).",
                "What is the value of \(AM + MB\) if \(M\) is the midpoint of \(AB\) and \(AM = {0}\text{{ cm}}\)?",
                "Determine \(AM + MB\) given midpoint \(M\) and \(AM = {0}\text{{ cm}}\).",
                "Find \(AM + MB = 2 \times AM\) for \(AM = {0}\text{{ cm}}\).",
                "Compute \(AM + MB\) where \(M\) bisects \(AB\) and \(AM = {0}\text{{ cm}}\).",
                "Evaluate the sum \(AM + MB\) when \(AM = {0}\text{{ cm}}\) and \(M\) is the midpoint.",
                "If \(M\) is the midpoint of \(AB\) with \(AM = {0}\text{{ cm}}\), find \(AM + MB\).",
                "For midpoint \(M\) of \(AB\) with \(AM = {0}\text{{ cm}}\), calculate \(AM + MB\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 6} cm", f"{item[1] - 6} cm", f"{item[0]} cm"],
                f"**Step 1: Formula**\\n\(AM + MB = AB = 2 \times AM = 2 \times {item[0]} = {item[1]}\text{{ cm}}\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'svg': lambda item: svg_segment_midpoint("A", "M", "B", f"AM = {item[0]} cm"),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

print("gen_1_3_1, gen_1_3_2, and gen_1_3_3 ready.")
'''

with open("scripts/build_clean_ch1.py", "a", encoding="utf-8") as f:
    f.write(code)

print("Appended 1.3.1, 1.3.2, 1.3.3.")
