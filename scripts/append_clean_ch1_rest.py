# scripts/append_clean_ch1_rest.py
import sys, os

code = '''
# =============================================================================
# 1.2.1: Condition: d(A, B) + d(B, C) = d(A, C) (80 Qs)
# =============================================================================
def gen_1_2_1():
    tc = "MH-9-MTH2-1-1.2.1"
    tname = "Condition: d(A, B) + d(B, C) = d(A, C)"
    archs = [
        # Arch 0: Given d(A, B) and d(B, C) when A-B-C, find d(A, C)
        {
            'data': [(5, 7, 12), (6, 9, 15), (7, 10, 17), (8, 11, 19), (9, 13, 22),
                     (10, 14, 24), (11, 15, 26), (12, 17, 29), (13, 18, 31), (14, 19, 33)],
            'tmpls': [
                "If points \(A, B, C\) are collinear such that \(A-B-C\), \(d(A, B) = {0}\) and \(d(B, C) = {1}\), find \(d(A, C)\).",
                "Given betweenness \(A-B-C\) with \(d(A, B) = {0}\) and \(d(B, C) = {1}\), calculate \(d(A, C)\).",
                "Calculate \(d(A, C)\) when \(B\) lies between \(A\) and \(C\) with \(d(A, B) = {0}\) and \(d(B, C) = {1}\).",
                "What is the distance \(d(A, C)\) if \(A-B-C\), \(d(A, B) = {0}\), and \(d(B, C) = {1}\)?",
                "Determine \(d(A, C)\) given \(A-B-C\) with \(d(A, B) = {0}\) and \(d(B, C) = {1}\).",
                "Find \(d(A, C) = d(A, B) + d(B, C)\) for \(d(A, B) = {0}\) and \(d(B, C) = {1}\).",
                "Compute distance \(d(A, C)\) for collinear points in order \(A-B-C\) with distances {0} and {1}.",
                "Evaluate \(d(A, C)\) when \(d(A, B) = {0}\) and \(d(B, C) = {1}\) with \(A-B-C\).",
                "If \(A-B-C\), \(d(A, B) = {0}\), and \(d(B, C) = {1}\), find \(d(A, C)\).",
                "For collinear points \(A, B, C\) with \(A-B-C\), calculate \(d(A, C)\) when \(d(A, B) = {0}\) and \(d(B, C) = {1}\)."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 4}", f"{item[2] - 3 if item[2] > 3 else item[2] + 8}", f"{item[1] - item[0] + 5}"],
                f"**Step 1: Betweenness condition**\\nSince \(A-B-C\), \(d(A, C) = d(A, B) + d(B, C) = {item[0]} + {item[1]} = {item[2]}\).\\n**Step 2: Conclusion**\\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(0, item[2], "A", "C"),
            'diff': 'easy'
        },
        # Arch 1: Given d(A, C) and d(A, B), find d(B, C)
        {
            'data': [(14, 6, 8), (16, 7, 9), (18, 7, 11), (20, 8, 12), (23, 9, 14),
                     (25, 9, 16), (28, 10, 18), (30, 10, 20), (33, 12, 21), (35, 12, 23)],
            'tmpls': [
                "If \(A-B-C\), \(d(A, C) = {0}\), and \(d(A, B) = {1}\), find \(d(B, C)\).",
                "Given collinear points with \(A-B-C\), \(d(A, C) = {0}\) and \(d(A, B) = {1}\), calculate \(d(B, C)\).",
                "Calculate \(d(B, C)\) when \(d(A, C) = {0}\) and \(d(A, B) = {1}\) in order \(A-B-C\).",
                "What is the distance \(d(B, C)\) if \(A-B-C\), \(d(A, C) = {0}\), and \(d(A, B) = {1}\)?",
                "Determine \(d(B, C)\) given \(A-B-C\) with total distance {0} and segment length {1}.",
                "Find \(d(B, C) = d(A, C) - d(A, B)\) for values {0} and {1}.",
                "Compute length of segment \(BC\) when \(d(A, C) = {0}\) and \(d(A, B) = {1}\) with \(B\) between \(A\) and \(C\).",
                "Evaluate \(d(B, C)\) knowing \(A-B-C\), \(d(A, C) = {0}\), and \(d(A, B) = {1}\).",
                "If \(A-B-C\) holds with \(d(A, C) = {0}\) and \(d(A, B) = {1}\), find \(d(B, C)\).",
                "For collinear points \(A, B, C\), find \(d(B, C)\) given \(d(A, C) = {0}\) and \(d(A, B) = {1}\)."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 4}", f"{item[2] - 3 if item[2] > 3 else item[2] + 7}", f"{item[0] + item[1]}"],
                f"**Step 1: Subtraction formula**\\nSince \(A-B-C\), \(d(B, C) = d(A, C) - d(A, B) = {item[0]} - {item[1]} = {item[2]}\).\\n**Step 2: Conclusion**\\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(0, item[0], "A", "C"),
            'diff': 'easy'
        },
        # Arch 2: Identify betweenness order from distances: B between A and C (distinct full phrase options)
        {
            'data': [(4, 6, 10, "B", "A", "C"), (5, 8, 13, "Q", "P", "R"), (6, 11, 17, "Y", "X", "Z"),
                     (7, 12, 19, "N", "M", "L"), (8, 13, 21, "E", "D", "F"), (9, 15, 24, "S", "R", "T"),
                     (10, 16, 26, "V", "U", "W"), (11, 18, 29, "H", "G", "I"), (12, 19, 31, "K", "J", "L"), (13, 22, 35, "B", "A", "C")],
            'tmpls': [
                "If \(d({4}, {3}) = {0}\), \(d({3}, {5}) = {1}\), and \(d({4}, {5}) = {2}\), which point lies between the other two?",
                "Given distances \(d({4}, {3}) = {0}\), \(d({3}, {5}) = {1}\), and \(d({4}, {5}) = {2}\), identify the intermediate point.",
                "Determine which point is between the other two when distances are {0}, {1}, and {2}.",
                "Points {4}, {3}, {5} have distances {0}, {1}, and {2}. State which point lies between the remaining two.",
                "Which point is situated between the other two if distances are {0}, {1}, and sum is {2}?",
                "Find the middle point among {4}, {3}, and {5} given \(d({4}, {3}) = {0}\), \(d({3}, {5}) = {1}\), \(d({4}, {5}) = {2}\).",
                "Identify the betweenness relationship: {0} + {1} = {2}. Which point lies between?",
                "From the distance values {0}, {1}, and {2}, determine which point is between the other two.",
                "If \(d({4}, {3}) = {0}\) and \(d({3}, {5}) = {1}\) and \(d({4}, {5}) = {2}\), which point is between?",
                "For points {4}, {3}, and {5} with distances {0}, {1}, {2}, state which point is in between."
            ],
            'calc': lambda item: (
                f"Point {item[3]} lies between point {item[4]} and point {item[5]}",
                [f"Point {item[4]} lies between point {item[3]} and point {item[5]}",
                 f"Point {item[5]} lies between point {item[4]} and point {item[3]}",
                 "The three points are non-collinear and form a triangle"],
                f"**Step 1: Check collinearity sum**\\n\(d({item[4]}, {item[3]}) + d({item[3]}, {item[5]}) = {item[0]} + {item[1]} = {item[2]} = d({item[4]}, {item[5]})\).\\n**Step 2: Conclusion**\\nPoint {item[3]} lies between point {item[4]} and point {item[5]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Given d(A, B) and d(B, C), find d(A, C) with algebraic parameter x
        {
            'data': [(2, 5, 3, 10, 5, 15), (3, 4, 2, 8, 5, 12), (4, 3, 3, 7, 7, 10),
                     (2, 8, 4, 12, 6, 20), (5, 2, 2, 14, 7, 16), (3, 7, 3, 9, 6, 16),
                     (4, 5, 2, 11, 6, 16), (6, 1, 2, 15, 8, 16), (3, 6, 4, 8, 7, 14), (2, 9, 5, 11, 7, 20)],
            'tmpls': [
                "If \(A-B-C\) with \(d(A, B) = {0}x + {1}\) and \(d(B, C) = {2}x + {3}\), find the expression for \(d(A, C)\).",
                "Given \(A-B-C\), express \(d(A, C)\) in terms of \(x\) if \(d(A, B) = {0}x + {1}\) and \(d(B, C) = {2}x + {3}\).",
                "Find \(d(A, C) = ({0}x + {1}) + ({2}x + {3})\) for collinear points \(A, B, C\).",
                "What is the total length \(d(A, C)\) if \(A-B-C\), \(AB = {0}x + {1}\), and \(BC = {2}x + {3}\)?",
                "Determine the algebraic sum \(d(A, C)\) when \(d(A, B) = {0}x + {1}\) and \(d(B, C) = {2}x + {3}\).",
                "Calculate \(d(A, C)\) in terms of variable \(x\) for collinear order \(A-B-C\).",
                "Simplify the expression for \(d(A, C)\) given \(AB = {0}x + {1}\) and \(BC = {2}x + {3}\).",
                "Evaluate \(d(A, C)\) algebraically when \(A-B-C\) holds.",
                "If points are arranged as \(A-B-C\) with segments {0}x + {1} and {2}x + {3}, find \(AC\).",
                "For collinear points \(A-B-C\), write the simplified expression for \(d(A, C)\)."
            ],
            'calc': lambda item: (
                f"{item[4]}x + {item[5]}",
                [f"{item[4]}x - {item[5]}", f"{item[4] + 2}x + {item[5]}", f"{item[4]}x + {item[5] + 4}"],
                f"**Step 1: Add expressions**\\n\(d(A, C) = d(A, B) + d(B, C) = ({item[0]}x + {item[1]}) + ({item[2]}x + {item[3]}) = ({item[0] + item[2]})x + ({item[1] + item[3]}) = {item[4]}x + {item[5]}\).\\n**Step 2: Conclusion**\\n{item[4]}x + {item[5]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Collinear points with fractional/decimal values
        {
            'data': [(2.5, 4.5, 7.0), (3.5, 5.5, 9.0), (1.5, 6.5, 8.0), (4.5, 6.5, 11.0), (2.5, 7.5, 10.0),
                     (3.5, 8.5, 12.0), (1.5, 9.5, 11.0), (5.5, 7.5, 13.0), (4.5, 9.5, 14.0), (6.5, 8.5, 15.0)],
            'tmpls': [
                "If \(P-Q-R\), \(d(P, Q) = {0}\), and \(d(Q, R) = {1}\), find distance \(d(P, R)\).",
                "Points \(P, Q, R\) are collinear with \(P-Q-R\). Given \(PQ = {0}\) and \(QR = {1}\), calculate \(PR\).",
                "Calculate \(d(P, R)\) when \(d(P, Q) = {0}\) and \(d(Q, R) = {1}\) in betweenness \(P-Q-R\).",
                "What is \(d(P, R)\) if \(d(P, Q) = {0}\) and \(d(Q, R) = {1}\) for collinear points?",
                "Determine \(d(P, R)\) knowing \(P-Q-R\) with decimal lengths {0} and {1}.",
                "Find \(d(P, R) = {0} + {1}\) on the number line.",
                "Compute the combined length \(d(P, R)\) for \(PQ = {0}\) and \(QR = {1}\).",
                "Evaluate distance \(d(P, R)\) given \(P-Q-R\), \(d(P, Q) = {0}\), and \(d(Q, R) = {1}\).",
                "If \(P-Q-R\) holds with lengths {0} and {1}, find total distance \(d(P, R)\).",
                "For collinear points \(P, Q, R\), calculate \(d(P, R)\) when \(PQ = {0}\) and \(QR = {1}\)."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 1.5}", f"{item[2] - 1.5}", f"{item[1] - item[0]}"],
                f"**Step 1: Sum formula**\\n\(d(P, R) = d(P, Q) + d(Q, R) = {item[0]} + {item[1]} = {item[2]}\).\\n**Step 2: Conclusion**\\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(0, int(item[2]), "P", "R"),
            'diff': 'easy'
        },
        # Arch 5: Two possible values of distance when order is not specified
        {
            'data': [(10, 4, 14, 6), (12, 5, 17, 7), (15, 6, 21, 9), (16, 7, 23, 9), (18, 8, 26, 10),
                     (20, 9, 29, 11), (22, 10, 32, 12), (25, 11, 36, 14), (28, 12, 40, 16), (30, 13, 43, 17)],
            'tmpls': [
                "On a line, points \(A, B, C\) are such that \(d(A, B) = {0}\) and \(d(B, C) = {1}\). Find all possible values of \(d(A, C)\).",
                "If \(d(A, B) = {0}\) and \(d(B, C) = {1}\) for collinear points \(A, B, C\), what are the possible lengths of \(AC\)?",
                "Calculate the two possible values of \(d(A, C)\) given \(d(A, B) = {0}\) and \(d(B, C) = {1}\).",
                "Points \(A, B, C\) lie on a straight line. If \(AB = {0}\) and \(BC = {1}\), find possible values of \(AC\).",
                "Determine the possible distances between \(A\) and \(C\) if \(d(A, B) = {0}\) and \(d(B, C) = {1}\).",
                "What can \(d(A, C)\) be if \(A, B, C\) are collinear with \(AB = {0}\) and \(BC = {1}\)?",
                "Evaluate the potential values of \(d(A, C)\) for collinear points with distances {0} and {1}.",
                "Find both cases for \(d(A, C)\) when \(d(A, B) = {0}\) and \(d(B, C) = {1}\).",
                "If collinear points have \(d(A, B) = {0}\) and \(d(B, C) = {1}\), find the set of possible values for \(d(A, C)\).",
                "For collinear points \(A, B, C\), find the two possible values of \(d(A, C)\) when \(AB = {0}\) and \(BC = {1}\)."
            ],
            'calc': lambda item: (
                f"{item[2]} or {item[3]}",
                [f"{item[2]} only", f"{item[3]} only", f"{item[0] + item[1] + 2} or {item[0] - item[1] - 2}"],
                f"**Step 1: Case 1 (A-B-C)**\\n\(d(A, C) = d(A, B) + d(B, C) = {item[0]} + {item[1]} = {item[2]}\).\\n**Step 2: Case 2 (A-C-B)**\\n\(d(A, C) = d(A, B) - d(B, C) = {item[0]} - {item[1]} = {item[3]}\).\\n**Step 3: Conclusion**\\n{item[2]} or {item[3]}."
            ),
            'diff': 'hard'
        },
        # Arch 6: Three points with given distances, test betweenness condition
        {
            'data': [(8, 12, 20), (9, 13, 22), (10, 15, 25), (11, 16, 27), (12, 17, 29),
                     (13, 19, 32), (14, 20, 34), (15, 21, 36), (16, 23, 39), (17, 24, 41)],
            'tmpls': [
                "If \(d(X, Y) = {0}\), \(d(Y, Z) = {1}\), and \(d(X, Z) = {2}\), check whether points \(X, Y, Z\) satisfy betweenness.",
                "Verify if betweenness holds for points \(X, Y, Z\) with distances {0}, {1}, and {2}.",
                "Do points \(X, Y, Z\) with \(d(X, Y) = {0}\), \(d(Y, Z) = {1}\), and \(d(X, Z) = {2}\) satisfy \(X-Y-Z\)?",
                "Check betweenness \(X-Y-Z\) given \(XY = {0}\), \(YZ = {1}\), and \(XZ = {2}\).",
                "Determine if \(d(X, Y) + d(Y, Z) = d(X, Z)\) holds for {0}, {1}, and {2}.",
                "State whether point \(Y\) lies between \(X\) and \(Z\) given lengths {0}, {1}, and {2}.",
                "Test if \(X, Y, Z\) are collinear in order \(X-Y-Z\) for distances {0}, {1}, and {2}.",
                "Evaluate whether betweenness condition is satisfied for distances {0}, {1}, {2}.",
                "For points \(X, Y, Z\) with lengths {0}, {1}, {2}, check if \(X-Y-Z\) is true.",
                "Confirm if points \(X, Y, Z\) are arranged as \(X-Y-Z\) when distances are {0}, {1}, and {2}."
            ],
            'calc': lambda item: (
                "Yes, betweenness condition is satisfied (X-Y-Z)",
                ["No, betweenness condition is violated", "Points are vertices of an isosceles triangle", "Cannot be determined without coordinates"],
                f"**Step 1: Check sum**\\n\(d(X, Y) + d(Y, Z) = {item[0]} + {item[1]} = {item[2]} = d(X, Z)\).\\nSince the sum of two smaller distances equals the greatest distance, betweenness holds.\\n**Step 2: Conclusion**\\nYes, betweenness condition is satisfied (X-Y-Z)."
            ),
            'diff': 'easy'
        },
        # Arch 7: Subtraction betweenness: find d(A, B) = d(A, C) - d(B, C)
        {
            'data': [(19, 8, 11), (21, 9, 12), (24, 10, 14), (27, 11, 16), (29, 12, 17),
                     (32, 13, 19), (35, 14, 21), (38, 15, 23), (41, 16, 25), (44, 17, 27)],
            'tmpls': [
                "If \(A-B-C\), \(d(A, C) = {0}\), and \(d(B, C) = {1}\), find distance \(d(A, B)\).",
                "Points \(A, B, C\) are collinear in order \(A-B-C\). If \(AC = {0}\) and \(BC = {1}\), calculate \(AB\).",
                "Calculate \(d(A, B)\) given \(A-B-C\) with \(d(A, C) = {0}\) and \(d(B, C) = {1}\).",
                "What is the distance \(d(A, B)\) if \(d(A, C) = {0}\) and \(d(B, C) = {1}\) with \(A-B-C\)?",
                "Determine \(d(A, B)\) knowing \(AC = {0}\) and \(BC = {1}\) for collinear points.",
                "Find \(d(A, B) = {0} - {1}\) on the line segment.",
                "Compute segment length \(AB\) when \(d(A, C) = {0}\) and \(d(B, C) = {1}\).",
                "Evaluate \(d(A, B)\) given \(A-B-C\), \(d(A, C) = {0}\), and \(d(B, C) = {1}\).",
                "If \(A-B-C\) holds with \(d(A, C) = {0}\) and \(d(B, C) = {1}\), find \(d(A, B)\).",
                "For collinear points \(A, B, C\), calculate \(d(A, B)\) when \(d(A, C) = {0}\) and \(d(B, C) = {1}\)."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 4}", f"{item[2] - 3 if item[2] > 3 else item[2] + 7}", f"{item[0] + item[1]}"],
                f"**Step 1: Subtraction formula**\\nSince \(A-B-C\), \(d(A, B) = d(A, C) - d(B, C) = {item[0]} - {item[1]} = {item[2]}\).\\n**Step 2: Conclusion**\\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(0, item[0], "A", "C"),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 1.2.2: Collinear vs non-collinear test (80 Qs)
# =============================================================================
def gen_1_2_2():
    tc = "MH-9-MTH2-1-1.2.2"
    tname = "Collinear vs non-collinear test"
    archs = [
        # Arch 0: Collinear test: a + b = c (order P-Q-R)
        {
            'data': [(7, 8, 15, "P", "Q", "R"), (6, 9, 15, "A", "B", "C"), (8, 11, 19, "X", "Y", "Z"),
                     (5, 12, 17, "L", "M", "N"), (9, 14, 23, "D", "E", "F"), (10, 15, 25, "R", "S", "T"),
                     (7, 16, 23, "U", "V", "W"), (8, 17, 25, "G", "H", "I"), (9, 19, 28, "J", "K", "L"), (11, 20, 31, "P", "Q", "R")],
            'tmpls': [
                "Determine whether points {3}, {4}, {5} are collinear if \(d({3}, {4}) = {0}\), \(d({4}, {5}) = {1}\), and \(d({3}, {5}) = {2}\).",
                "Given distances \(d({3}, {4}) = {0}\), \(d({4}, {5}) = {1}\), and \(d({3}, {5}) = {2}\), state whether the points are collinear.",
                "Check if points {3}, {4}, {5} with distances {0}, {1}, and {2} are collinear or non-collinear.",
                "Are points {3}, {4}, {5} collinear when \(d({3}, {4}) = {0}\), \(d({4}, {5}) = {1}\), and \(d({3}, {5}) = {2}\)?",
                "Classify points {3}, {4}, {5} having distances {0}, {1}, {2} as collinear or non-collinear.",
                "Find whether points {3}, {4}, and {5} lie on the same straight line with distances {0}, {1}, and {2}.",
                "Test collinearity of points {3}, {4}, {5} with segment lengths {0}, {1}, and {2}.",
                "Evaluate if points {3}, {4}, {5} are collinear given lengths {0}, {1}, and {2}.",
                "State collinearity status of points {3}, {4}, {5} having distances {0}, {1}, and {2}.",
                "For points {3}, {4}, {5} with distances {0}, {1}, and {2}, determine if they are collinear."
            ],
            'calc': lambda item: (
                f"Collinear with betweenness {item[3]}-{item[4]}-{item[5]}",
                ["Non-collinear points", f"Collinear with betweenness {item[4]}-{item[3]}-{item[5]}", "Points form vertices of a triangle"],
                f"**Step 1: Check sum of two smaller distances**\\n\(d({item[3]}, {item[4]}) + d({item[4]}, {item[5]}) = {item[0]} + {item[1]} = {item[2]} = d({item[3]}, {item[5]})\).\\n**Step 2: Conclusion**\\nCollinear with betweenness {item[3]}-{item[4]}-{item[5]}."
            ),
            'diff': 'medium'
        },
        # Arch 1: Non-collinear test: a + b != c (strictly distinct sums)
        {
            'data': [(5, 6, 13, "A", "B", "C"), (4, 7, 14, "P", "Q", "R"), (6, 8, 16, "X", "Y", "Z"),
                     (7, 9, 18, "L", "M", "N"), (8, 10, 20, "D", "E", "F"), (9, 11, 23, "R", "S", "T"),
                     (6, 12, 21, "U", "V", "W"), (7, 13, 24, "G", "H", "I"), (8, 14, 25, "J", "K", "L"), (10, 15, 28, "M", "N", "O")],
            'tmpls': [
                "Determine whether points {3}, {4}, {5} are collinear if \(d({3}, {4}) = {0}\), \(d({4}, {5}) = {1}\), and \(d({3}, {5}) = {2}\).",
                "Given distances \(d({3}, {4}) = {0}\), \(d({4}, {5}) = {1}\), and \(d({3}, {5}) = {2}\), state whether the points are collinear.",
                "Check if points {3}, {4}, {5} with distances {0}, {1}, and {2} are collinear or non-collinear.",
                "Are points {3}, {4}, {5} collinear when \(d({3}, {4}) = {0}\), \(d({4}, {5}) = {1}\), and \(d({3}, {5}) = {2}\)?",
                "Classify points {3}, {4}, {5} having distances {0}, {1}, {2} as collinear or non-collinear.",
                "Find whether points {3}, {4}, and {5} lie on the same straight line with distances {0}, {1}, and {2}.",
                "Test collinearity of points {3}, {4}, {5} with segment lengths {0}, {1}, and {2}.",
                "Evaluate if points {3}, {4}, {5} are collinear given lengths {0}, {1}, and {2}.",
                "State collinearity status of points {3}, {4}, {5} having distances {0}, {1}, and {2}.",
                "For points {3}, {4}, {5} with distances {0}, {1}, and {2}, determine if they are collinear."
            ],
            'calc': lambda item: (
                "Non-collinear (points form a triangle)",
                [f"Collinear with betweenness {item[3]}-{item[4]}-{item[5]}", f"Collinear with betweenness {item[4]}-{item[3]}-{item[5]}", "Coincident points"],
                f"**Step 1: Check sum of two smaller distances**\\n\({item[0]} + {item[1]} = {item[0] + item[1]} \\ne {item[2]}\).\\nSince the sum of two smaller distances is not equal to the largest distance, the points do not lie on a single straight line.\\n**Step 2: Conclusion**\\nNon-collinear (points form a triangle)."
            ),
            'diff': 'medium'
        },
        # Arch 2: Triangle inequality test: sum of two sides > third side
        {
            'data': [(6, 8, 10), (7, 9, 12), (8, 10, 14), (9, 12, 15), (10, 13, 17),
                     (11, 14, 19), (12, 15, 21), (13, 16, 23), (14, 17, 25), (15, 18, 27)],
            'tmpls': [
                "Three points form a triangle with side lengths {0}\text{{ cm}}, {1}\text{{ cm}}, and {2}\text{{ cm}}. Are these points collinear or non-collinear?",
                "If segment lengths connecting three points are {0}\text{{ cm}}, {1}\text{{ cm}}, and {2}\text{{ cm}}, are the points collinear?",
                "Can three points with distances {0}\text{{ cm}}, {1}\text{{ cm}}, and {2}\text{{ cm}} lie on a single line?",
                "Determine the collinearity of three points that have pairwise distances {0}\text{{ cm}}, {1}\text{{ cm}}, {2}\text{{ cm}}.",
                "Three points have mutual distances {0}\text{{ cm}}, {1}\text{{ cm}}, {2}\text{{ cm}}. Classify them as collinear or non-collinear.",
                "Check if points with distances {0}\text{{ cm}}, {1}\text{{ cm}}, {2}\text{{ cm}} can be collinear.",
                "State whether three points having distances {0}\text{{ cm}}, {1}\text{{ cm}}, {2}\text{{ cm}} are collinear.",
                "Evaluate collinearity for points with lengths {0}\text{{ cm}}, {1}\text{{ cm}}, and {2}\text{{ cm}}.",
                "For lengths {0}\text{{ cm}}, {1}\text{{ cm}}, and {2}\text{{ cm}}, are the points collinear?",
                "Are three points with pairwise distances {0}\text{{ cm}}, {1}\text{{ cm}}, {2}\text{{ cm}} on the same line?"
            ],
            'calc': lambda item: (
                "Non-collinear (satisfy triangle inequality)",
                ["Collinear points on a number line", "Coincident points", "Indeterminate without coordinates"],
                f"**Step 1: Check collinearity**\\n\({item[0]} + {item[1]} = {item[0] + item[1]} > {item[2]}\).\\nSince the sum is strictly greater than the third side, they form the vertices of a non-degenerate triangle.\\n**Step 2: Conclusion**\\nNon-collinear (satisfy triangle inequality)."
            ),
            'diff': 'easy'
        },
        # Arch 3: Three coordinates on number line: collinearity is always satisfied
        {
            'data': [(-3, 2, 7, 5, 5, 10), (-5, 1, 9, 6, 8, 14), (-7, 0, 8, 7, 8, 15),
                     (-9, -2, 6, 7, 8, 15), (-4, 3, 11, 7, 8, 15), (-6, 2, 10, 8, 8, 16),
                     (-8, 1, 11, 9, 10, 19), (-10, -1, 9, 9, 10, 19), (-5, 4, 13, 9, 9, 18), (-7, 3, 14, 10, 11, 21)],
            'tmpls': [
                "Points \(A, B, C\) on a number line have coordinates {0}, {1}, and {2} respectively. Are they collinear?",
                "Given coordinates \(A({0})\), \(B({1})\), \(C({2})\) on a 1-dimensional axis, determine if they are collinear.",
                "Are points with coordinates {0}, {1}, {2} on a coordinate line collinear?",
                "State whether three points plotted at {0}, {1}, and {2} on a number line are collinear.",
                "Check the collinearity of points \(A({0})\), \(B({1})\), and \(C({2})\).",
                "Can points with coordinates {0}, {1}, {2} on a number line ever be non-collinear?",
                "Classify points at {0}, {1}, and {2} on a number axis.",
                "Evaluate the collinearity of points on a number line with coordinates {0}, {1}, and {2}.",
                "For coordinates {0}, {1}, {2} on a number axis, are the points collinear?",
                "Determine the collinearity status of points with coordinates {0}, {1}, {2}."
            ],
            'calc': lambda item: (
                "Always collinear (all points lie on the number line)",
                ["Non-collinear points", "Collinear only if all coordinates are positive", "Collinear only if equidistant"],
                f"**Step 1: 1-dimensional space property**\\nAll points on a number line lie on the same single straight line by definition, so any set of points on a number line is always collinear.\\n**Step 2: Conclusion**\\nAlways collinear (all points lie on the number line)."
            ),
            'diff': 'easy'
        },
        # Arch 4: Collinear check with coordinate distances: d(A,B) + d(B,C) = d(A,C)
        {
            'data': [(1, 4, 9, 3, 5, 8), (2, 6, 12, 4, 6, 10), (3, 8, 15, 5, 7, 12),
                     (4, 10, 18, 6, 8, 14), (5, 12, 21, 7, 9, 16), (6, 14, 24, 8, 10, 18),
                     (7, 16, 27, 9, 11, 20), (8, 18, 30, 10, 12, 22), (9, 20, 33, 11, 13, 24), (10, 22, 36, 12, 14, 26)],
            'tmpls': [
                "Find \(d(A, B)\), \(d(B, C)\), and \(d(A, C)\) for coordinates {0}, {1}, {2} and verify collinearity.",
                "For coordinates \(A({0})\), \(B({1})\), \(C({2})\), calculate distances and verify betweenness.",
                "Calculate segment lengths for coordinates {0}, {1}, {2} and determine collinearity.",
                "Given \(A({0})\), \(B({1})\), \(C({2})\), find \(d(A, C)\) and state collinearity.",
                "Evaluate distances between coordinates {0}, {1}, {2} and state if \(A-B-C\) holds.",
                "Compute pairwise distances for points at {0}, {1}, {2} and confirm betweenness.",
                "Determine if points with coordinates {0}, {1}, {2} satisfy \(d(A, B) + d(B, C) = d(A, C)\).",
                "Verify collinearity by distance formula for points at {0}, {1}, and {2}.",
                "Check whether points \(A({0})\), \(B({1})\), \(C({2})\) satisfy \(A-B-C\).",
                "For coordinates {0}, {1}, {2}, confirm betweenness order \(A-B-C\)."
            ],
            'calc': lambda item: (
                f"Collinear: d(A, B) = {item[3]}, d(B, C) = {item[4]}, d(A, C) = {item[5]}",
                [f"Non-collinear: sum is {item[3] + item[4] + 2}", f"Collinear: d(A, C) = {item[5] + 4}", "Cannot be evaluated"],
                f"**Step 1: Compute distances**\\n\(d(A, B) = {item[1]} - {item[0]} = {item[3]}\)\\n\(d(B, C) = {item[2]} - {item[1]} = {item[4]}\)\\n\(d(A, C) = {item[2]} - {item[0]} = {item[5]}\)\\n**Step 2: Check sum**\\n\({item[3]} + {item[4]} = {item[5]}\).\\n**Step 3: Conclusion**\\nCollinear: d(A, B) = {item[3]}, d(B, C) = {item[4]}, d(A, C) = {item[5]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Non-collinear points determine a unique plane
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
        },
        # Arch 7: Testing collinearity when largest distance is not sum of others
        {
            'data': [(11, 7, 16), (12, 8, 18), (13, 9, 20), (14, 10, 22), (15, 11, 24),
                     (16, 12, 26), (17, 13, 28), (18, 14, 30), (19, 15, 32), (20, 16, 34)],
            'tmpls': [
                "Given distances \(d(L, M) = {0}\), \(d(M, N) = {1}\), and \(d(L, N) = {2}\), evaluate whether \(L, M, N\) are collinear.",
                "Check if points \(L, M, N\) with distances {0}, {1}, {2} are collinear.",
                "Determine if points \(L, M, N\) having distances {0}, {1}, {2} lie on a straight line.",
                "Are points \(L, M, N\) collinear if \(LM = {0}\), \(MN = {1}\), and \(LN = {2}\)?",
                "Evaluate collinearity for points \(L, M, N\) with lengths {0}, {1}, and {2}.",
                "State whether \(L, M, N\) are collinear given \(d(L, M) = {0}\), \(d(M, N) = {1}\), \(d(L, N) = {2}\).",
                "Verify if \(L, M, N\) with lengths {0}, {1}, {2} satisfy the betweenness condition.",
                "Test whether \(d(L, M) + d(M, N) = d(L, N)\) for {0}, {1}, and {2}.",
                "For lengths {0}, {1}, and {2}, determine if points \(L, M, N\) are collinear.",
                "Check collinearity status of \(L, M, N\) having distances {0}, {1}, and {2}."
            ],
            'calc': lambda item: (
                f"Non-collinear: {item[0]} + {item[1]} = {item[0] + item[1]} != {item[2]}",
                [f"Collinear with order L-M-N", f"Collinear with order M-L-N", "Points are coincident"],
                f"**Step 1: Check sum**\\n\({item[0]} + {item[1]} = {item[0] + item[1]} \\ne {item[2]}\).\\nSince the sum does not equal the largest distance, the points are non-collinear.\\n**Step 2: Conclusion**\\nNon-collinear: {item[0]} + {item[1]} = {item[0] + item[1]} != {item[2]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

print("gen_1_2_1 and gen_1_2_2 ready.")
'''

with open("scripts/build_clean_ch1.py", "a", encoding="utf-8") as f:
    f.write(code)

print("Appended 1.2.1 and 1.2.2.")
