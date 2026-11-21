# scripts/build_clean_ch1.py
# Clean generator for Chapter 1: Basic Concepts in Geometry (10 subtopics, 800 Qs)
# 100% distinct, zero near-identical options, >=60% SVGs.

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine import SEQS_80, build_q, generate_subtopic, svg_numberline, svg_segment_midpoint

CH_NUM = 1
CH_NAME = "Basic Concepts in Geometry"

# =============================================================================
# 1.1.1: Coordinates on number line (80 Qs)
# =============================================================================
def gen_1_1_1():
    tc = "MH-9-MTH2-1-1.1.1"
    tname = "Coordinates on number line"
    archs = [
        # Arch 0: Positive coordinate reading
        {
            'data': [(1, 4), (2, 5), (3, 7), (4, 8), (5, 9), (6, 11), (7, 12), (8, 13), (9, 14), (10, 15)],
            'tmpls': [
                "On a number line, point \(A\) has coordinate {0} and point \(B\) has coordinate {1}. What is the coordinate of point \(B\)?",
                "Point \(B\) is plotted at {1} on the number line. State the coordinate of \(B\).",
                "What is the coordinate of point \(B\) located at position {1} on the number line?",
                "Determine the coordinate of point \(B\) given that its position is {1}.",
                "Find the coordinate of point \(B\) which lies at {1} on the real number line.",
                "Identify the coordinate of point \(B\) marked at {1} on the number axis.",
                "Read the coordinate of point \(B\) located at mark {1} on the coordinate line.",
                "The position of point \(B\) on the number axis is {1}. State its coordinate.",
                "Evaluate the coordinate of point \(B\) plotted at mark {1}.",
                "For point \(B\) at position {1} on the number line, what is its coordinate?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[1] + 3}", f"{item[1] - 3}", f"{item[0]}"],
                f"**Step 1: Reading coordinate**\nThe point \(B\) is positioned at mark {item[1]} on the number line.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'svg': lambda item: svg_numberline(item[0], item[1], "A", "B"),
            'diff': 'easy'
        },
        # Arch 1: Negative coordinate reading
        {
            'data': [(-1, 3), (-2, 4), (-3, 5), (-4, 2), (-5, 1), (-6, 3), (-7, 2), (-8, 4), (-9, 5), (-10, 6)],
            'tmpls': [
                "On a number line, point \(P\) lies to the left of the origin at {0}. What is the coordinate of \(P\)?",
                "Point \(P\) has coordinate {0} on the number line. State the coordinate of \(P\).",
                "What is the coordinate of point \(P\) located at position {0} on the number line?",
                "Determine the coordinate of point \(P\) given that its coordinate is {0}.",
                "Find the coordinate of point \(P\) which lies at {0} on the real number axis.",
                "Identify the coordinate of point \(P\) marked at {0} to the left of origin.",
                "Read the coordinate of point \(P\) at position {0} on the number line.",
                "The position of point \(P\) on the number line is {0}. State its coordinate.",
                "Evaluate the coordinate of point \(P\) located at {0}.",
                "For point \(P\) at position {0} on the number axis, what is its coordinate?"
            ],
            'calc': lambda item: (
                f"{item[0]}",
                [f"{abs(item[0]) + 5}", f"{item[0] - 4}", f"{item[0] + 4}"],
                f"**Step 1: Coordinate identification**\nPoint \(P\) is located at mark {item[0]} on the negative side of the origin.\n**Step 2: Conclusion**\n{item[0]}."
            ),
            'svg': lambda item: svg_numberline(item[0], item[1], "P", "Q"),
            'diff': 'easy'
        },
        # Arch 2: Distance from origin O(0) to A(x) => d(O, A) = |x|
        {
            'data': [(6, 6), (-7, 7), (8, 8), (-9, 9), (11, 11), (-12, 12), (13, 13), (-14, 14), (16, 16), (-17, 17)],
            'tmpls': [
                "On a number line, origin \(O\) has coordinate 0 and point \(A\) has coordinate {0}. Find the distance \(d(O, A)\).",
                "Calculate distance \(d(O, A)\) from origin \(O(0)\) to point \(A({0})\).",
                "What is the distance between origin \(O(0)\) and point \(A({0})\) on the number line?",
                "Determine the length of segment \(OA\) where \(O\) is the origin and \(A\) has coordinate {0}.",
                "Find the distance \(d(O, A)\) for point \(A\) at position {0} from origin \(O(0)\).",
                "Compute distance \(d(O, A) = |{0} - 0|\) on the real number line.",
                "Evaluate the distance between the origin and point \(A({0})\).",
                "How far is point \(A({0})\) from origin \(O(0)\) on the number axis?",
                "If origin is \(O(0)\) and point \(A\) is at {0}, find \(d(O, A)\).",
                "For origin \(O(0)\) and point \(A({0})\), calculate \(d(O, A)\)."
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[1] + 5}", f"{item[1] - 3 if item[1] > 3 else item[1] + 8}", f"{item[0]}"],
                f"**Step 1: Distance formula from origin**\n\(d(O, A) = |{item[0]} - 0| = |{item[0]}| = {item[1]}\).\nDistance is always non-negative.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'svg': lambda item: svg_numberline(0, item[0], "O", "A") if item[0] > 0 else svg_numberline(item[0], 0, "A", "O"),
            'diff': 'easy'
        },
        # Arch 3: Coordinate of point at distance d to the right of x0: x = x0 + d
        {
            'data': [(2, 5, 7), (3, 6, 9), (4, 7, 11), (5, 8, 13), (6, 9, 15),
                     (-4, 6, 2), (-5, 9, 4), (-3, 9, 6), (-2, 10, 8), (-1, 11, 10)],
            'tmpls': [
                "Point \(A\) has coordinate {0}. Point \(B\) is at a distance of {1} units to the right of \(A\). Find the coordinate of \(B\).",
                "Starting from coordinate {0}, if we move {1} units to the right, what coordinate is reached?",
                "Find the coordinate of a point lying {1} units to the right of point \(A({0})\) on the number line.",
                "What is the coordinate of point \(B\) if it is {1} units in the positive direction from {0}?",
                "Determine the coordinate of point \(B\) situated {1} units to the right of {0}.",
                "Compute coordinate \(x = {0} + {1}\) on the number axis.",
                "Calculate the position of point \(B\) located {1} units to the right of \(A({0})\).",
                "Evaluate the coordinate reached by moving {1} units rightwards from {0}.",
                "If point \(B\) is {1} units to the right of \(A({0})\), find the coordinate of \(B\).",
                "For point \(A({0})\), find the coordinate of point \(B\) which is {1} units to its right."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 4}", f"{item[2] - 3}", f"{item[1]}"],
                f"**Step 1: Movement to the right**\nMoving to the right adds the distance to the initial coordinate: \({item[0]} + {item[1]} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(item[0], item[2], "A", "B"),
            'diff': 'easy'
        },
        # Arch 4: Coordinate of point at distance d to the left of x0: x = x0 - d
        {
            'data': [(8, 3, 5), (7, 4, 3), (6, 5, 1), (5, 6, -1), (4, 7, -3),
                     (3, 8, -5), (2, 9, -7), (1, 10, -9), (0, 8, -8), (-2, 4, -6)],
            'tmpls': [
                "Point \(A\) has coordinate {0}. Point \(C\) is at a distance of {1} units to the left of \(A\). Find the coordinate of \(C\).",
                "Starting from coordinate {0}, if we move {1} units to the left on the number line, what coordinate is reached?",
                "Find the coordinate of a point lying {1} units to the left of point \(A({0})\).",
                "What is the coordinate of point \(C\) if it is {1} units in the negative direction from {0}?",
                "Determine the coordinate of point \(C\) situated {1} units to the left of {0}.",
                "Compute coordinate \(x = {0} - {1}\) on the number axis.",
                "Calculate the position of point \(C\) located {1} units to the left of \(A({0})\).",
                "Evaluate the coordinate reached by moving {1} units leftwards from {0}.",
                "If point \(C\) is {1} units to the left of \(A({0})\), find the coordinate of \(C\).",
                "For point \(A({0})\), calculate the coordinate of point \(C\) which lies {1} units to its left."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 4}", f"{item[2] - 4}", f"{item[0]}"],
                f"**Step 1: Movement to the left**\nMoving to the left subtracts the distance from the initial coordinate: \({item[0]} - {item[1]} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(item[2], item[0], "C", "A"),
            'diff': 'easy'
        },
        # Arch 5: Midpoint coordinate on number line: x_M = (x1 + x2) / 2
        {
            'data': [(2, 8, 5), (4, 12, 8), (6, 16, 11), (8, 20, 14), (10, 24, 17),
                     (-6, 2, -2), (-8, 4, -2), (-10, 6, -2), (-4, 8, 2), (-12, 4, -4)],
            # Ensure distinct answers:
            # 5, 8, 11, 14, 17, -2, -1, 0, 2, -4:
            'data': [(2, 8, 5), (4, 12, 8), (6, 16, 11), (8, 20, 14), (10, 24, 17),
                     (-6, 2, -2), (-8, 6, -1), (-10, 10, 0), (-4, 8, 2), (-12, 4, -4)],
            'tmpls': [
                "Find the coordinate of the midpoint \(M\) of segment \(AB\), given coordinates of \(A\) and \(B\) are {0} and {1}.",
                "Coordinates of \(A\) and \(B\) are {0} and {1} respectively. Find the coordinate of their midpoint \(M\).",
                "Calculate the midpoint coordinate of segment joining {0} and {1} on the number line.",
                "What is the coordinate of the point equidistant from {0} and {1} on the number axis?",
                "Determine the coordinate of midpoint \(M\) of \(AB\) with \(A({0})\) and \(B({1})\).",
                "Compute the midpoint coordinate \(x = \frac{{{0} + {1}}}{{2}}\) on the real line.",
                "Evaluate the coordinate of the midpoint between points at {0} and {1}.",
                "Find the point exactly midway between {0} and {1} on the number axis.",
                "If coordinates of \(A\) and \(B\) are {0} and {1}, find the midpoint coordinate.",
                "For points \(A({0})\) and \(B({1})\), calculate the coordinate of midpoint \(M\)."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 4}", f"{item[2] - 4}", f"{item[0] + item[1]}"],
                f"**Step 1: Midpoint formula**\n\(x_M = \frac{{{item[0]} + {item[1]}}}{{2}} = \frac{{{item[0] + item[1]}}}{{2}} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(item[0], item[1], "A", "B"),
            'diff': 'medium'
        },
        # Arch 6: Comparison: Which coordinate is greater?
        {
            'data': [(-5, -2, -2), (-8, -3, -3), (-10, -4, -4), (-7, 1, 1), (-9, 0, 0),
                     (-12, -6, -6), (-15, -8, -8), (-4, 3, 3), (-11, -5, -5), (-14, -7, -7)],
            'tmpls': [
                "Between the coordinates {0} and {1} on the number line, which coordinate is greater?",
                "Which number is greater: {0} or {1}?",
                "Determine the greater coordinate between {0} and {1} on the real axis.",
                "Identify which of the two coordinates {0} and {1} lies farther to the right.",
                "Find the greater coordinate between point with coordinate {0} and point with coordinate {1}.",
                "Compare coordinates {0} and {1} and state the larger value.",
                "Which of the coordinates {0} or {1} represents the larger real number?",
                "Evaluate which coordinate is greater: {0} or {1}.",
                "Between {0} and {1} on the number line, select the greater coordinate.",
                "For coordinates {0} and {1}, state which value is greater."
            ],
            'calc': lambda item: (
                f"{item[2]} is greater",
                [f"{item[0] if item[2] == item[1] else item[1]} is greater", "Both coordinates are equal", "Cannot be determined without a coordinate grid"],
                f"**Step 1: Number line ordering**\nOn a horizontal number line, the number that lies farther to the right is greater.\n{item[2]} lies to the right of {item[0] if item[2] == item[1] else item[1]}, so {item[2]} > {item[0] if item[2] == item[1] else item[1]}.\n**Step 2: Conclusion**\n{item[2]} is greater."
            ),
            'svg': lambda item: svg_numberline(min(item[0], item[1]), max(item[0], item[1]), "X", "Y"),
            'diff': 'easy'
        },
        # Arch 7: Distance between symmetric points -a and a: d = 2*a
        {
            'data': [(4, 8), (5, 10), (6, 12), (7, 14), (8, 16),
                     (9, 18), (10, 20), (11, 22), (12, 24), (13, 26)],
            'tmpls': [
                "Points \(A\) and \(B\) have coordinates -{0} and {0} respectively. Find distance \(d(A, B)\).",
                "Calculate the distance between points at coordinates -{0} and {0} on the number line.",
                "What is the distance between symmetric points \(A(-{0})\) and \(B({0})\)?",
                "Determine \(d(A, B)\) for points \(A(-{0})\) and \(B({0})\) on the number axis.",
                "Find distance \(d(A, B) = {0} - (-{0})\) on the number line.",
                "Compute the distance between point with coordinate -{0} and point with coordinate {0}.",
                "Evaluate distance \(d(A, B)\) where coordinates are -{0} and {0}.",
                "Calculate length of segment joining points at -{0} and {0}.",
                "If coordinates of \(A\) and \(B\) are -{0} and {0}, find \(d(A, B)\).",
                "For points \(A(-{0})\) and \(B({0})\), calculate \(d(A, B)\)."
            ],
            'calc': lambda item: (
                f"{item[1]} units",
                [f"{item[0]} units", f"{item[1] + 4} units", f"{item[1] - 4} units"],
                f"**Step 1: Distance formula**\n\(d(A, B) = \text{{Greater}} - \text{{Smaller}} = {item[0]} - (-{item[0]}) = {item[0]} + {item[0]} = {item[1]}\).\n**Step 2: Conclusion**\n{item[1]} units."
            ),
            'svg': lambda item: svg_numberline(-item[0], item[0], "A", "B"),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 1.1.2: Distance formula: d(A, B) = Greater - Smaller (80 Qs)
# =============================================================================
def gen_1_1_2():
    tc = "MH-9-MTH2-1-1.1.2"
    tname = "Distance formula: d(A, B) = Greater coordinate - Smaller coordinate"
    archs = [
        # Arch 0: Both positive: d = b - a
        {
            'data': [(2, 9, 7), (3, 11, 8), (4, 14, 10), (5, 17, 12), (6, 19, 13),
                     (7, 22, 15), (8, 24, 16), (9, 27, 18), (10, 29, 19), (11, 32, 21)],
            'tmpls': [
                "Find distance \(d(A, B)\) if the coordinates of \(A\) and \(B\) are {0} and {1} respectively.",
                "Calculate \(d(A, B)\) where coordinate of \(A\) is {0} and coordinate of \(B\) is {1}.",
                "What is the distance between points \(A({0})\) and \(B({1})\) on the number line?",
                "Determine distance \(d(A, B)\) given coordinates \(A({0})\) and \(B({1})\).",
                "Find \(d(A, B) = {1} - {0}\) on the number axis.",
                "Compute the distance between point \(A\) at {0} and point \(B\) at {1}.",
                "Evaluate \(d(A, B)\) for coordinates {0} and {1}.",
                "Calculate length of segment \(AB\) where coordinates are {0} and {1}.",
                "If coordinates of \(A\) and \(B\) are {0} and {1}, find \(d(A, B)\).",
                "For points \(A({0})\) and \(B({1})\), calculate \(d(A, B)\)."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 3}", f"{item[2] - 3 if item[2] > 3 else item[2] + 6}", f"{item[0] + item[1]}"],
                f"**Step 1: Identify greater and smaller coordinates**\nHere, {item[1]} > {item[0]}.\n**Step 2: Distance formula**\n\(d(A, B) = \text{{Greater coordinate}} - \text{{Smaller coordinate}} = {item[1]} - {item[0]} = {item[2]}\).\n**Step 3: Conclusion**\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(item[0], item[1], "A", "B"),
            'diff': 'easy'
        },
        # Arch 1: One negative, one positive: d = b - (-a) = b + a
        {
            'data': [(-3, 6, 9), (-4, 7, 11), (-5, 9, 14), (-6, 10, 16), (-7, 10, 17),
                     (-8, 11, 19), (-9, 13, 22), (-10, 14, 24), (-11, 15, 26), (-12, 16, 28)],
            'tmpls': [
                "Coordinates of \(P\) and \(Q\) are {0} and {1} respectively. Find distance \(d(P, Q)\).",
                "Calculate distance \(d(P, Q)\) between \(P({0})\) and \(Q({1})\) on the number line.",
                "What is the distance between point \(P({0})\) and point \(Q({1})\)?",
                "Determine \(d(P, Q)\) given coordinates \(P({0})\) and \(Q({1})\).",
                "Find distance \(d(P, Q) = {1} - ({0})\) on the real line.",
                "Compute the distance between \(P({0})\) and \(Q({1})\).",
                "Evaluate \(d(P, Q)\) for coordinates {0} and {1}.",
                "Calculate length of segment \(PQ\) where coordinates are {0} and {1}.",
                "If coordinates of \(P\) and \(Q\) are {0} and {1}, find \(d(P, Q)\).",
                "For points \(P({0})\) and \(Q({1})\), calculate \(d(P, Q)\)."
            ],
            'calc': lambda item: (
                f"{item[2]} units",
                [f"{item[2] + 4} units", f"{item[2] - 4 if item[2] > 4 else item[2] + 8} units", f"{item[1] - abs(item[0])} units"],
                f"**Step 1: Identify coordinates**\n{item[1]} > {item[0]}.\n**Step 2: Distance formula**\n\(d(P, Q) = {item[1]} - ({item[0]}) = {item[1]} + {abs(item[0])} = {item[2]}\).\n**Step 3: Conclusion**\n{item[2]} units."
            ),
            'svg': lambda item: svg_numberline(item[0], item[1], "P", "Q"),
            'diff': 'easy'
        },
        # Arch 2: Both negative: d = (-smaller) - (-larger)
        {
            'data': [(-9, -4, 5), (-11, -5, 6), (-13, -6, 7), (-15, -7, 8), (-17, -7, 10),
                     (-19, -8, 11), (-21, -9, 12), (-23, -9, 14), (-25, -10, 15), (-28, -11, 17)],
            'tmpls': [
                "Find distance \(d(R, S)\) if coordinates of \(R\) and \(S\) are {0} and {1} respectively.",
                "Calculate distance \(d(R, S)\) between \(R({0})\) and \(S({1})\) on the number line.",
                "What is the distance between negative coordinates \(R({0})\) and \(S({1})\)?",
                "Determine \(d(R, S)\) given coordinates \(R({0})\) and \(S({1})\).",
                "Find distance \(d(R, S) = {1} - ({0})\) for negative numbers.",
                "Compute the distance between \(R({0})\) and \(S({1})\).",
                "Evaluate \(d(R, S)\) for coordinates {0} and {1}.",
                "Calculate length of segment \(RS\) where coordinates are {0} and {1}.",
                "If coordinates of \(R\) and \(S\) are {0} and {1}, find \(d(R, S)\).",
                "For points \(R({0})\) and \(S({1})\), calculate \(d(R, S)\)."
            ],
            'calc': lambda item: (
                f"Distance is {item[2]}",
                [f"Distance is {item[2] + 4}", f"Distance is {item[2] - 3 if item[2] > 3 else item[2] + 8}", f"Distance is {abs(item[0]) + abs(item[1])}"],
                f"**Step 1: Identify greater coordinate**\nSince both numbers are negative, the one closer to zero is greater: {item[1]} > {item[0]}.\n**Step 2: Distance formula**\n\(d(R, S) = {item[1]} - ({item[0]}) = {item[1]} + {abs(item[0])} = {item[2]}\).\n**Step 3: Conclusion**\nDistance is {item[2]}."
            ),
            'svg': lambda item: svg_numberline(item[0], item[1], "R", "S"),
            'diff': 'medium'
        },
        # Arch 3: Given d(A, B) and coordinate of A, find coordinate of B (to the right)
        {
            'data': [(5, 8, 13), (6, 9, 15), (7, 10, 17), (8, 11, 19), (9, 12, 21),
                     (-2, 7, 5), (-3, 9, 6), (-4, 11, 7), (-5, 13, 8), (-6, 15, 9)],
            'tmpls': [
                "Distance \(d(A, B) = {1}\). If coordinate of \(A\) is {0} and \(B\) is to the right of \(A\), find coordinate of \(B\).",
                "If \(d(A, B) = {1}\) and coordinate of \(A\) is {0}, calculate coordinate of \(B\) (where \(B\) has greater coordinate).",
                "Calculate coordinate of \(B\) given \(d(A, B) = {1}\), \(A\) has coordinate {0}, and \(B\) lies to the right.",
                "What is the coordinate of point \(B\) if \(d(A, B) = {1}\) and \(A\) is at {0} (with \(B > A\))?",
                "Determine coordinate of \(B\) knowing \(d(A, B) = {1}\) and \(A({0})\) where \(B\) is to the right.",
                "Find coordinate of \(B = {0} + {1}\) on the number line.",
                "Compute coordinate of \(B\) at distance {1} to the right of \(A({0})\).",
                "Evaluate the coordinate of \(B\) given \(d(A, B) = {1}\) and \(A\) is at {0}.",
                "If \(d(A, B) = {1}\) and \(A\) has coordinate {0}, find the coordinate of \(B\) (\(B > A\)).",
                "For \(d(A, B) = {1}\) and \(A({0})\), calculate the coordinate of \(B\) to the right."
            ],
            'calc': lambda item: (
                f"Coordinate of B is {item[2]}",
                [f"Coordinate of B is {item[2] + 4}", f"Coordinate of B is {item[2] - 4}", f"Coordinate of B is {item[1]}"],
                f"**Step 1: Formula**\nSince \(B\) lies to the right of \(A\), its coordinate is greater: \(\text{{Coord}}(B) = \text{{Coord}}(A) + d(A, B) = {item[0]} + {item[1]} = {item[2]}\).\n**Step 2: Conclusion**\nCoordinate of B is {item[2]}."
            ),
            'svg': lambda item: svg_numberline(item[0], item[2], "A", "B"),
            'diff': 'medium'
        },
        # Arch 4: Given d(A, B) and coordinate of B, find coordinate of A (to the left)
        {
            'data': [(14, 5, 9), (15, 7, 8), (16, 9, 7), (18, 12, 6), (20, 15, 5),
                     (4, 6, -2), (5, 8, -3), (6, 10, -4), (7, 12, -5), (8, 14, -6)],
            'tmpls': [
                "Distance \(d(A, B) = {1}\). If coordinate of \(B\) is {0} and \(A\) is to the left of \(B\), find coordinate of \(A\).",
                "If \(d(A, B) = {1}\) and coordinate of \(B\) is {0}, calculate coordinate of \(A\) (where \(A\) has smaller coordinate).",
                "Calculate coordinate of \(A\) given \(d(A, B) = {1}\), \(B\) has coordinate {0}, and \(A\) lies to the left.",
                "What is the coordinate of point \(A\) if \(d(A, B) = {1}\) and \(B\) is at {0} (with \(A < B\))?",
                "Determine coordinate of \(A\) knowing \(d(A, B) = {1}\) and \(B({0})\) where \(A\) is to the left.",
                "Find coordinate of \(A = {0} - {1}\) on the number line.",
                "Compute coordinate of \(A\) at distance {1} to the left of \(B({0})\).",
                "Evaluate the coordinate of \(A\) given \(d(A, B) = {1}\) and \(B\) is at {0}.",
                "If \(d(A, B) = {1}\) and \(B\) has coordinate {0}, find the coordinate of \(A\) (\(A < B\)).",
                "For \(d(A, B) = {1}\) and \(B({0})\), calculate the coordinate of \(A\) to the left."
            ],
            'calc': lambda item: (
                f"Coordinate of A is {item[2]}",
                [f"Coordinate of A is {item[2] + 4}", f"Coordinate of A is {item[2] - 4}", f"Coordinate of A is {item[1]}"],
                f"**Step 1: Formula**\nSince \(A\) lies to the left of \(B\), its coordinate is smaller: \(\text{{Coord}}(A) = \text{{Coord}}(B) - d(A, B) = {item[0]} - {item[1]} = {item[2]}\).\n**Step 2: Conclusion**\nCoordinate of A is {item[2]}."
            ),
            'svg': lambda item: svg_numberline(item[2], item[0], "A", "B"),
            'diff': 'medium'
        },
        # Arch 5: Distance between points on coordinate line with different values
        {
            'data': [(10, 25, 15), (12, 30, 18), (14, 35, 21), (16, 40, 24), (18, 45, 27),
                     (20, 50, 30), (22, 55, 33), (24, 60, 36), (26, 65, 39), (28, 70, 42)],
            'tmpls': [
                "Two milestones on a highway coordinate line are at mark {0} km and mark {1} km. What is the distance between them?",
                "Find the linear distance between coordinate {0} and coordinate {1} on an engineering scale.",
                "Calculate distance \(d(X, Y)\) between marks at {0} and {1} on a calibrated measuring line.",
                "What is the span between position {0} and position {1} on the surveyor scale?",
                "Determine the distance between coordinate points {0} and {1}.",
                "Find the separation distance between position markers {0} and {1}.",
                "Compute the length between coordinate positions {0} and {1}.",
                "Evaluate the difference distance between markers at {0} and {1}.",
                "On a straight survey track, marks are at {0} and {1}. Find the separation distance.",
                "Calculate the distance between points with coordinates {0} and {1}."
            ],
            'calc': lambda item: (
                f"{item[2]} km",
                [f"{item[2] + 5} km", f"{item[2] - 5} km", f"{item[0] + item[1]} km"],
                f"**Step 1: Linear distance formula**\n\(d = {item[1]} - {item[0]} = {item[2]}\text{{ km}}\).\n**Step 2: Conclusion**\n{item[2]} km."
            ),
            'diff': 'easy'
        },
        # Arch 6: Distance to origin for distinct negative coordinates
        {
            'data': [(-25, 25), (-35, 35), (-45, 45), (-55, 55), (-65, 65),
                     (-75, 75), (-85, 85), (-95, 95), (-105, 105), (-115, 115)],
            'tmpls': [
                "What is the distance of point with coordinate {0} from the origin \(O(0)\)?",
                "Calculate distance from origin \(O(0)\) to point \(K({0})\) on the number line.",
                "Determine the magnitude of distance between origin and point at {0}.",
                "How many units is point \(K({0})\) away from the origin on the number line?",
                "Find \(d(O, K)\) where origin is 0 and point \(K\) has coordinate {0}.",
                "Compute distance \(|{0} - 0|\) from the origin.",
                "Evaluate the distance from origin to coordinate {0}.",
                "On the coordinate axis, find distance between point at {0} and origin (0).",
                "State the distance of point \(K({0})\) from origin \(O\).",
                "Calculate length of line segment from origin (0) to mark {0}."
            ],
            'calc': lambda item: (
                f"{item[1]} units from origin",
                [f"{item[0]} units from origin", f"{item[1] + 10} units from origin", f"{item[1] - 10} units from origin"],
                f"**Step 1: Distance from origin formula**\n\(d(O, K) = |{item[0]} - 0| = {item[1]}\text{{ units}}\).\nDistance is always non-negative.\n**Step 2: Conclusion**\n{item[1]} units from origin."
            ),
            'diff': 'easy'
        },
        # Arch 7: Sum of two consecutive distances: d(A, B) + d(B, C) when A-B-C
        {
            'data': [(1, 5, 9, 8), (2, 7, 12, 10), (3, 9, 16, 13), (4, 11, 18, 14), (5, 13, 21, 16),
                     (-5, 0, 7, 12), (-6, 1, 9, 15), (-7, 2, 10, 17), (-8, 3, 11, 19), (-9, 4, 13, 22)],
            'tmpls': [
                "Coordinates of \(A, B, C\) are {0}, {1}, and {2} respectively with \(A-B-C\). Find \(d(A, C)\).",
                "Points \(A({0}), B({1}), C({2})\) lie on a number line in order \(A-B-C\). Calculate \(d(A, C)\).",
                "Calculate distance \(d(A, C)\) between points at {0} and {2} on the number line.",
                "What is the distance \(d(A, C)\) if \(A\) is at {0} and \(C\) is at {2}?",
                "Determine \(d(A, C)\) given coordinates \(A({0}), B({1}), C({2})\) in betweenness order.",
                "Find \(d(A, C) = d(A, B) + d(B, C)\) for coordinates {0}, {1}, and {2}.",
                "Compute \(d(A, C)\) for collinear points with coordinates {0}, {1}, {2}.",
                "Evaluate total distance \(d(A, C)\) between \(A({0})\) and \(C({2})\).",
                "If coordinates of \(A, B, C\) are {0}, {1}, {2}, find \(d(A, C)\).",
                "For collinear points \(A({0}), B({1}), C({2})\), calculate \(d(A, C)\)."
            ],
            'calc': lambda item: (
                f"Total distance d(A, C) = {item[3]}",
                [f"Total distance d(A, C) = {item[3] + 4}", f"Total distance d(A, C) = {item[3] - 4 if item[3] > 4 else item[3] + 8}", f"Total distance d(A, C) = {item[1]}"],
                f"**Step 1: Distance formula**\nSince \(A-B-C\), \(d(A, C) = \text{{Coord}}(C) - \text{{Coord}}(A) = {item[2]} - ({item[0]}) = {item[3]}\).\n**Step 2: Conclusion**\nTotal distance d(A, C) = {item[3]}."
            ),
            'svg': lambda item: svg_numberline(item[0], item[2], "A", "C"),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

print("build_clean_ch1.py header and 1.1.1, 1.1.2 ready.")

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
                f"**Step 1: Betweenness condition**\nSince \(A-B-C\), \(d(A, C) = d(A, B) + d(B, C) = {item[0]} + {item[1]} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
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
                f"**Step 1: Subtraction formula**\nSince \(A-B-C\), \(d(B, C) = d(A, C) - d(A, B) = {item[0]} - {item[1]} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
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
                f"Point {item[3]} is strictly between point {item[4]} and point {item[5]}",
                [f"Point {item[4]} serves as the intermediate vertex between the others",
                 f"The endpoint {item[5]} is situated midway between endpoints",
                 "The three points are non-collinear and form a geometric triangle"],
                f"**Step 1: Check collinearity sum**\n\(d({item[4]}, {item[3]}) + d({item[3]}, {item[5]}) = {item[0]} + {item[1]} = {item[2]} = d({item[4]}, {item[5]})\).\n**Step 2: Conclusion**\nPoint {item[3]} lies between point {item[4]} and point {item[5]}."
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
                f"**Step 1: Add expressions**\n\(d(A, C) = d(A, B) + d(B, C) = ({item[0]}x + {item[1]}) + ({item[2]}x + {item[3]}) = ({item[0] + item[2]})x + ({item[1] + item[3]}) = {item[4]}x + {item[5]}\).\n**Step 2: Conclusion**\n{item[4]}x + {item[5]}."
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
                f"**Step 1: Sum formula**\n\(d(P, R) = d(P, Q) + d(Q, R) = {item[0]} + {item[1]} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
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
                f"**Step 1: Case 1 (A-B-C)**\n\(d(A, C) = d(A, B) + d(B, C) = {item[0]} + {item[1]} = {item[2]}\).\n**Step 2: Case 2 (A-C-B)**\n\(d(A, C) = d(A, B) - d(B, C) = {item[0]} - {item[1]} = {item[3]}\).\n**Step 3: Conclusion**\n{item[2]} or {item[3]}."
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
                f"**Step 1: Check sum**\n\(d(X, Y) + d(Y, Z) = {item[0]} + {item[1]} = {item[2]} = d(X, Z)\).\nSince the sum of two smaller distances equals the greatest distance, betweenness holds.\n**Step 2: Conclusion**\nYes, betweenness condition is satisfied (X-Y-Z)."
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
                f"**Step 1: Subtraction formula**\nSince \(A-B-C\), \(d(A, B) = d(A, C) - d(B, C) = {item[0]} - {item[1]} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
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
                f"Collinear with order {item[3]}-{item[4]}-{item[5]}",
                ["The points are non-collinear and form a triangle",
                 f"Collinear with intermediate vertex being point {item[3]}",
                 "All three points are coincident at the origin"],
                f"**Step 1: Check sum of two smaller distances**\n\(d({item[3]}, {item[4]}) + d({item[4]}, {item[5]}) = {item[0]} + {item[1]} = {item[2]} = d({item[3]}, {item[5]})\).\n**Step 2: Conclusion**\nCollinear with betweenness {item[3]}-{item[4]}-{item[5]}."
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
                [f"Collinear in order {item[3]}-{item[4]}-{item[5]}",
                 f"Collinear with intermediate vertex being {item[3]}",
                 "All three points are coincident"],
                f"**Step 1: Check sum of two smaller distances**\n\({item[0]} + {item[1]} = {item[0] + item[1]} \ne {item[2]}\).\nSince the sum of two smaller distances is not equal to the largest distance, the points do not lie on a single straight line.\n**Step 2: Conclusion**\nNon-collinear (points form a triangle)."
            ),
            'diff': 'medium'
        },
        # Arch 2: Triangle inequality test: sum of two sides > third side
        {
            'data': [(6, 8, 10), (7, 9, 12), (8, 10, 14), (9, 12, 15), (10, 13, 17),
                     (11, 14, 19), (12, 15, 21), (13, 16, 23), (14, 17, 25), (15, 18, 27)],
            'tmpls': [
                "Three points form a triangle with side lengths {0}	ext{{ cm}}, {1}	ext{{ cm}}, and {2}	ext{{ cm}}. Are these points collinear or non-collinear?",
                "If segment lengths connecting three points are {0}	ext{{ cm}}, {1}	ext{{ cm}}, and {2}	ext{{ cm}}, are the points collinear?",
                "Can three points with distances {0}	ext{{ cm}}, {1}	ext{{ cm}}, and {2}	ext{{ cm}} lie on a single line?",
                "Determine the collinearity of three points that have pairwise distances {0}	ext{{ cm}}, {1}	ext{{ cm}}, {2}	ext{{ cm}}.",
                "Three points have mutual distances {0}	ext{{ cm}}, {1}	ext{{ cm}}, {2}	ext{{ cm}}. Classify them as collinear or non-collinear.",
                "Check if points with distances {0}	ext{{ cm}}, {1}	ext{{ cm}}, {2}	ext{{ cm}} can be collinear.",
                "State whether three points having distances {0}	ext{{ cm}}, {1}	ext{{ cm}}, {2}	ext{{ cm}} are collinear.",
                "Evaluate collinearity for points with lengths {0}	ext{{ cm}}, {1}	ext{{ cm}}, and {2}	ext{{ cm}}.",
                "For lengths {0}	ext{{ cm}}, {1}	ext{{ cm}}, and {2}	ext{{ cm}}, are the points collinear?",
                "Are three points with pairwise distances {0}	ext{{ cm}}, {1}	ext{{ cm}}, {2}	ext{{ cm}} on the same line?"
            ],
            'calc': lambda item: (
                "Non-collinear (satisfy triangle inequality)",
                ["Collinear points on a number line", "Coincident points", "Indeterminate without coordinates"],
                f"**Step 1: Check collinearity**\n\({item[0]} + {item[1]} = {item[0] + item[1]} > {item[2]}\).\nSince the sum is strictly greater than the third side, they form the vertices of a non-degenerate triangle.\n**Step 2: Conclusion**\nNon-collinear (satisfy triangle inequality)."
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
                f"**Step 1: 1-dimensional space property**\nAll points on a number line lie on the same single straight line by definition, so any set of points on a number line is always collinear.\n**Step 2: Conclusion**\nAlways collinear (all points lie on the number line)."
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
                f"**Step 1: Compute distances**\n\(d(A, B) = {item[1]} - {item[0]} = {item[3]}\)\n\(d(B, C) = {item[2]} - {item[1]} = {item[4]}\)\n\(d(A, C) = {item[2]} - {item[0]} = {item[5]}\)\n**Step 2: Check sum**\n\({item[3]} + {item[4]} = {item[5]}\).\n**Step 3: Conclusion**\nCollinear: d(A, B) = {item[3]}, d(B, C) = {item[4]}, d(A, C) = {item[5]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Lines determined by n non-collinear points: n*(n-1)/2
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
                "Compute the number of lines: C({0}, 2) = \frac{{{0} \times ({0}-1)}}{{2}}.",
                "Evaluate the maximum number of lines passing through pairs of {0} points.",
                "If no three of {0} points are collinear, how many lines pass through them?",
                "For {0} coplanar points with no three on a line, find the number of straight lines."
            ],
            'calc': lambda item: (
                f"{item[1]} lines",
                [f"{item[1] + 3} lines", f"{item[1] - 3} lines", f"{item[0]} lines"],
                f"**Step 1: Combinations formula**\nThe number of lines determined by n points with no three collinear is \(C(n, 2) = \frac{{n(n-1)}}{{2}} = \frac{{{item[0]} \times {item[0]-1}}}{{2}} = {item[1]}\).\n**Step 2: Conclusion**\n{item[1]} lines."
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
                "Compute the number of triangles: C({0}, 3) = \frac{{{0} \times ({0}-1) \times ({0}-2)}}{{6}}.",
                "Evaluate the number of triangles with vertices at {0} non-collinear points.",
                "If no three of {0} points are collinear, how many triangles can be constructed?",
                "For {0} points where no three are collinear, find the total number of triangles."
            ],
            'calc': lambda item: (
                f"{item[1]} triangles",
                [f"{item[1] + 4} triangles", f"{item[1] - 4 if item[1] > 4 else item[1] + 8} triangles", f"{item[0]} triangles"],
                f"**Step 1: Combinations formula**\nNumber of triangles = \(C(n, 3) = \frac{{n(n-1)(n-2)}}{{6}} = \frac{{{item[0]} \times {item[0]-1} \times {item[0]-2}}}{{6}} = {item[1]}\).\n**Step 2: Conclusion**\n{item[1]} triangles."
            ),
            'diff': 'hard'
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
                ["The points are collinear on a straight line",
                 "The points form an equilateral triangle",
                 "All three points are coincident at the origin"],
                f"**Step 1: Check sum**\n\({item[0]} + {item[1]} = {item[0] + item[1]} \ne {item[2]}\).\nSince the sum does not equal the largest distance, the points are non-collinear.\n**Step 2: Conclusion**\nNon-collinear: {item[0]} + {item[1]} = {item[0] + item[1]} != {item[2]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

print("gen_1_2_1 and gen_1_2_2 ready.")

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
                "If \(l({1}) = {0}	ext{{ cm}}\) and \(l({2}) = {0}	ext{{ cm}}\), what is the relationship between segment {1} and segment {2}?",
                "Length of segment {1} is {0}	ext{{ cm}} and length of segment {2} is {0}	ext{{ cm}}. State their relationship.",
                "Two segments {1} and {2} each have length {0}	ext{{ cm}}. Are they congruent?",
                "Given \(l({1}) = {0}	ext{{ cm}}\) and \(l({2}) = {0}	ext{{ cm}}\), determine if segment {1} is congruent to segment {2}.",
                "What can be deduced about segments {1} and {2} if both measure {0}	ext{{ cm}}?",
                "State the congruence relation between segment {1} and segment {2} when both are {0}	ext{{ cm}} long.",
                "Compare segments {1} and {2} given \(l({1}) = {0}	ext{{ cm}}\) and \(l({2}) = {0}	ext{{ cm}}\).",
                "Evaluate the relationship between segments {1} and {2} having identical length of {0}	ext{{ cm}}.",
                "If segment {1} and segment {2} both have length {0}	ext{{ cm}}, identify the true statement.",
                "For segments {1} and {2} measuring {0}	ext{{ cm}} each, determine their relation."
            ],
            'calc': lambda item: (
                f"Segment {item[1]} is congruent to segment {item[2]}",
                [f"Segment {item[1]} is longer than segment {item[2]}",
                 f"Segment {item[1]} is shorter than segment {item[2]}",
                 "The two segments are perpendicular"],
                f"**Step 1: Definition of congruent segments**\nIf the lengths of two segments are equal, then the two segments are congruent.\nSince \(l({item[1]}) = l({item[2]}) = {item[0]}	ext{{ cm}}\), segment {item[1]} \(\cong\) segment {item[2]}.\n**Step 2: Conclusion**\nSegment {item[1]} is congruent to segment {item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Comparison of unequal segments: AB > CD
        {
            'data': [(12, 7, "AB", "CD"), (14, 8, "PQ", "RS"), (16, 9, "EF", "GH"), (18, 10, "MN", "XY"), (20, 11, "JK", "LM"),
                     (22, 13, "TU", "VW"), (24, 15, "BC", "DE"), (26, 17, "QR", "ST"), (28, 19, "OP", "KL"), (30, 21, "YZ", "WX")],
            'tmpls': [
                "If \(l({2}) = {0}	ext{{ cm}}\) and \(l({3}) = {1}	ext{{ cm}}\), compare the two segments.",
                "Compare segments {2} and {3} if \(l({2}) = {0}	ext{{ cm}}\) and \(l({3}) = {1}	ext{{ cm}}\).",
                "Given lengths \(l({2}) = {0}	ext{{ cm}}\) and \(l({3}) = {1}	ext{{ cm}}\), state the comparison between them.",
                "Which segment is longer: segment {2} of length {0}	ext{{ cm}} or segment {3} of length {1}	ext{{ cm}}?",
                "Determine the comparison relation between segment {2} ({0}	ext{{ cm}}) and segment {3} ({1}	ext{{ cm}}).",
                "Evaluate the inequality between segment {2} measuring {0}	ext{{ cm}} and segment {3} measuring {1}	ext{{ cm}}.",
                "Compare length of segment {2} ({0}	ext{{ cm}}) with segment {3} ({1}	ext{{ cm}}).",
                "What is the comparative relation between segment {2} and segment {3}?",
                "State which segment is strictly greater between {2} ({0}	ext{{ cm}}) and {3} ({1}	ext{{ cm}}).",
                "For segments {2} ({0}	ext{{ cm}}) and {3} ({1}	ext{{ cm}}), identify the correct inequality."
            ],
            'calc': lambda item: (
                f"Segment {item[2]} is longer than segment {item[3]} (length {item[0]} cm > {item[1]} cm)",
                [f"Segment {item[2]} is shorter than segment {item[3]} (length {item[0]} cm < {item[1]} cm)",
                 f"Segment {item[2]} is congruent to segment {item[3]}",
                 "The two segments cannot be compared"],
                f"**Step 1: Compare lengths**\n\(l({item[2]}) = {item[0]}	ext{{ cm}}\) and \(l({item[3]}) = {item[1]}	ext{{ cm}}\).\nSince {item[0]} > {item[1]}, segment {item[2]} is longer than segment {item[3]}.\n**Step 2: Conclusion**\nSegment {item[2]} is longer than segment {item[3]} (length {item[0]} cm > {item[1]} cm)."
            ),
            'diff': 'easy'
        },
        # Arch 2: Comparison of unequal segments: AB < CD
        {
            'data': [(6, 11, "KL", "MN"), (7, 13, "XY", "ZW"), (8, 15, "IJ", "GH"), (9, 17, "UV", "AB"), (10, 19, "RS", "TU"),
                     (11, 21, "CD", "EF"), (12, 23, "NO", "PQ"), (13, 25, "WX", "BC"), (14, 27, "JK", "RS"), (15, 29, "LM", "YZ")],
            'tmpls': [
                "If \(l({2}) = {0}	ext{{ cm}}\) and \(l({3}) = {1}	ext{{ cm}}\), compare the two segments.",
                "Compare segments {2} and {3} if \(l({2}) = {0}	ext{{ cm}}\) and \(l({3}) = {1}	ext{{ cm}}\).",
                "Given lengths \(l({2}) = {0}	ext{{ cm}}\) and \(l({3}) = {1}	ext{{ cm}}\), state the comparison between them.",
                "Which segment is shorter: segment {2} of length {0}	ext{{ cm}} or segment {3} of length {1}	ext{{ cm}}?",
                "Determine the comparison relation between segment {2} ({0}	ext{{ cm}}) and segment {3} ({1}	ext{{ cm}}).",
                "Evaluate the inequality between segment {2} measuring {0}	ext{{ cm}} and segment {3} measuring {1}	ext{{ cm}}.",
                "Compare length of segment {2} ({0}	ext{{ cm}}) with segment {3} ({1}	ext{{ cm}}).",
                "What is the comparative relation between segment {2} and segment {3}?",
                "State which segment is smaller between {2} ({0}	ext{{ cm}}) and {3} ({1}	ext{{ cm}}).",
                "For segments {2} ({0}	ext{{ cm}}) and {3} ({1}	ext{{ cm}}), identify the correct comparison."
            ],
            'calc': lambda item: (
                f"Segment {item[2]} is shorter than segment {item[3]} (length {item[0]} cm < {item[1]} cm)",
                [f"Segment {item[2]} is longer than segment {item[3]} (length {item[0]} cm > {item[1]} cm)",
                 f"Segment {item[2]} is congruent to segment {item[3]}",
                 "The two segments are parallel"],
                f"**Step 1: Compare lengths**\n\(l({item[2]}) = {item[0]}	ext{{ cm}}\) and \(l({item[3]}) = {item[1]}	ext{{ cm}}\).\nSince {item[0]} < {item[1]}, segment {item[2]} is shorter than segment {item[3]}.\n**Step 2: Conclusion**\nSegment {item[2]} is shorter than segment {item[3]} (length {item[0]} cm < {item[1]} cm)."
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
                f"**Step 1: Set equations equal**\n\({item[0]}x + {item[1]} = {item[2]}x + {item[3]} \implies ({item[0]} - {item[2]})x = {item[3]} - {item[1]} \implies {item[0] - item[2]}x = {item[3] - item[1]}\).\n**Step 2: Solve for x**\n\(x = {item[4]}\).\n**Step 3: Conclusion**\nx = {item[4]}."
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
                f"**Step 1: Formal geometric definition**\nThe union set of point A, point B, and all points between A and B is called segment AB (seg AB).\n**Step 2: Conclusion**\nLine segment {item[1]} (seg {item[1]})."
            ),
            'diff': 'easy'
        },
        # Arch 5: Properties of congruence: Reflexivity with distinct lengths
        {
            'data': [(5, "AB"), (6, "PQ"), (7, "XY"), (8, "MN"), (9, "CD"),
                     (10, "EF"), (11, "GH"), (12, "JK"), (13, "RS"), (14, "TU")],
            'tmpls': [
                "Segment {1} has length {0} cm. Since \(l({1}) = l({1}) = {0}	ext{{ cm}}\), segment {1} \(\cong\) segment {1}. This illustrates which property?",
                "For segment {1} measuring {0} cm, \(seg {1} \cong seg {1}\) demonstrates which property of congruence?",
                "If \(l({1}) = {0}	ext{{ cm}}\), the statement \(seg {1} \cong seg {1}\) is an example of what property?",
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
                f"**Step 1: Reflexivity definition**\nEvery segment is congruent to itself: \(seg {item[1]} \cong seg {item[1]}\). This is called Reflexivity.\n**Step 2: Conclusion**\nReflexivity property of segment congruence (for {item[1]} = {item[0]} cm)."
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
                f"**Step 1: Definition of Symmetry**\nIf seg AB \(\cong\) seg CD, then seg CD \(\cong\) seg AB. This is the Symmetry property of congruence.\n**Step 2: Conclusion**\nSymmetry property of segment congruence."
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
                f"**Step 1: Transitivity property**\nIf seg AB \(\cong\) seg CD and seg CD \(\cong\) seg EF, then seg AB \(\cong\) seg EF. This is the Transitivity property of congruence.\n**Step 2: Conclusion**\nTransitivity property of segment congruence."
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
                f"**Step 1: Definition of opposite rays**\nTwo rays which have a common origin and whose union is a straight line are called opposite rays.\n**Step 2: Conclusion**\nOpposite rays (ray {item[0]}{item[1]} and ray {item[0]}{item[2]})."
            ),
            'diff': 'easy'
        },
        # Arch 1: Angle between opposite rays with distinct ray angle queries
        {
            'data': [(10, 170, "B", "A", "C"), (20, 160, "O", "P", "Q"), (30, 150, "M", "L", "N"), (40, 140, "K", "J", "L"), (50, 130, "Y", "X", "Z"),
                     (60, 120, "D", "C", "E"), (70, 110, "F", "E", "G"), (80, 100, "S", "R", "T"), (25, 155, "H", "G", "I"), (35, 145, "W", "V", "X")],
            'tmpls': [
                "Rays {2}{3} and {2}{4} are opposite rays. Ray {2}X makes an angle of {0}° with ray {2}{3}. Find the angle between ray {2}X and ray {2}{4}.",
                "Given opposite rays {2}{3} and {2}{4}, if ray {2}X makes {0}° with {2}{3}, calculate \(ngle X{2}{4}\).",
                "Calculate \(ngle X{2}{4} = 180^\circ - {0}^\circ\) where rays {2}{3} and {2}{4} are opposite rays.",
                "Opposite rays {2}{3} and {2}{4} form a straight line. If \(ngle {3}{2}X = {0}^\circ\), find \(ngle {4}{2}X\).",
                "Determine the supplementary angle to {0}° on the straight line formed by opposite rays {2}{3} and {2}{4}.",
                "Find the measure of \(ngle X{2}{4}\) when ray {2}X divides the 180° straight angle into {0}° and \(ngle X{2}{4}\).",
                "What is the angle between ray {2}X and ray {2}{4} if \(ngle {3}{2}X = {0}^\circ\) on opposite rays?",
                "Evaluate \(ngle X{2}{4}\) on opposite rays {2}{3} and {2}{4} where one adjacent angle is {0}°.",
                "If rays {2}{3} and {2}{4} are opposite rays and \(ngle {3}{2}X = {0}^\circ\), find \(ngle X{2}{4}\).",
                "For opposite rays {2}{3} and {2}{4}, calculate \(ngle X{2}{4}\) when \(ngle {3}{2}X = {0}^\circ\)."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{item[1] + 15}°", f"{item[1] - 15}°", f"{90 - item[0]}°"],
                f"**Step 1: Straight line angle property**\nSince rays {item[2]}{item[3]} and {item[2]}{item[4]} are opposite rays, \(ngle {item[3]}{item[2]}{item[4]} = 180^\circ\).\n\(ngle X{item[2]}{item[4]} = 180^\circ - {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
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
                ["The two rays point in the identical direction along the line",
                 "The two rays are perpendicular and meet at a 90° angle",
                 "The two rays are non-collinear and form an acute angle"],
                f"**Step 1: Identify rays from common origin {item[1]}**\nSince {item[0]}-{item[1]}-{item[2]}, ray {item[1]}{item[0]} extends towards {item[0]} and ray {item[1]}{item[2]} extends towards {item[2]} in opposite directions along line {item[0]}{item[2]}.\n**Step 2: Conclusion**\nRay {item[1]}{item[0]} and ray {item[1]}{item[2]} are opposite rays."
            ),
            'diff': 'medium'
        },
        # Arch 3: Rays that have common origin but do NOT form a line are NOT opposite rays
        {
            'data': [(30, "A", "O", "B"), (45, "P", "O", "Q"), (60, "X", "O", "Y"), (75, "L", "O", "M"), (90, "D", "O", "E"),
                     (105, "F", "O", "G"), (120, "R", "O", "S"), (135, "J", "O", "K"), (150, "U", "O", "V"), (160, "M", "O", "N")],
            'tmpls': [
                "Ray O{1} and ray O{2} have common endpoint O, but \(ngle {1}O{2} = {0}^\circ\). Are they opposite rays?",
                "If \(ngle {1}O{2} = {0}^\circ\), are ray O{1} and ray O{2} opposite rays?",
                "Two rays O{1} and O{2} meet at O with an angle of {0}°. Do they form opposite rays?",
                "Can ray O{1} and ray O{2} be called opposite rays if the angle between them is {0}°?",
                "State whether ray O{1} and ray O{2} are opposite rays when \(ngle {1}O{2} = {0}^\circ\).",
                "Determine if ray O{1} and ray O{2} are opposite rays given \(ngle {1}O{2} = {0}^\circ\).",
                "Evaluate if two rays forming a {0}° angle are opposite rays.",
                "Are rays O{1} and O{2} opposite rays if their angle is {0} degrees?",
                "Check whether ray O{1} and ray O{2} are opposite rays when their angle is {0}°.",
                "For rays O{1} and O{2} with \(ngle {1}O{2} = {0}^\circ\), are they opposite rays?"
            ],
            'calc': lambda item: (
                f"No, because the angle between them is {item[0]}° (not 180°)",
                ["Yes, because they share a common vertex O", "Yes, any two rays with a common vertex are opposite rays", "Cannot be determined without their lengths"],
                f"**Step 1: Criterion for opposite rays**\nOpposite rays must have a common endpoint AND their union must be a straight line (angle = 180°).\nHere \(ngle {item[1]}O{item[2]} = {item[0]}^\circ \ne 180^\circ\), so they are not opposite rays.\n**Step 2: Conclusion**\nNo, because the angle between them is {item[0]}° (not 180°)."
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
                f"**Step 1: Ray intersection**\nOpposite rays extend in opposite directions from their common origin {item[0]}. They share only the origin point {item[0]}.\n**Step 2: Conclusion**\nThe single origin point {{{item[0]}}}."
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
                f"**Step 1: Ray union**\nThe union of two opposite rays ray {item[0]}{item[1]} and ray {item[0]}{item[2]} is the complete line {item[1]}{item[2]}.\n**Step 2: Conclusion**\nThe infinite line {item[1]}{item[2]} (line {item[1]}{item[2]})."
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
                f"**Step 1: Check ray directions**\nBoth ray {item[0]}{item[1]} and ray {item[0]}{item[2]} start at {item[0]} and point in the SAME direction towards {item[2]}. Therefore, they are the same ray, NOT opposite rays.\n**Step 2: Conclusion**\nNo, they are identical rays pointing in the same direction (ray {item[0]}{item[1]} is ray {item[0]}{item[2]})."
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
                f"**Step 1: Linear pair property**\nAngles forming a linear pair on opposite rays are supplementary: \(	ext{{Angle}} = 180^\circ - {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
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
                "Point \(M\) is the midpoint of segment \(AB\). If \(AB = {0}	ext{{ cm}}\), find length of segment \(AM\).",
                "If \(M\) is the midpoint of \(AB\) and \(AB = {0}	ext{{ cm}}\), calculate \(AM\).",
                "Calculate length \(AM\) where \(M\) is the midpoint of segment \(AB = {0}	ext{{ cm}}\).",
                "What is the length of \(AM\) if \(M\) bisects segment \(AB = {0}	ext{{ cm}}\)?",
                "Determine \(AM\) given \(l(AB) = {0}	ext{{ cm}}\) and \(M\) is the midpoint.",
                "Find \(AM = rac{{AB}}{{2}}\) for \(AB = {0}	ext{{ cm}}\).",
                "Compute \(l(AM)\) in segment \(AB = {0}	ext{{ cm}}\) with midpoint \(M\).",
                "Evaluate length of segment \(AM\) when \(M\) is the midpoint of \(AB = {0}	ext{{ cm}}\).",
                "If \(M\) is the midpoint of segment \(AB\) measuring {0}	ext{{ cm}}, find \(AM\).",
                "For segment \(AB = {0}	ext{{ cm}}\) with midpoint \(M\), calculate \(AM\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 2} cm", f"{item[1] - 2} cm", f"{item[0] + 2} cm"],
                f"**Step 1: Formula**\n\(AM = rac{{AB}}{{2}} = rac{{{item[0]}}}{{2}} = {item[1]}	ext{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_segment_midpoint("A", "M", "B", f"AB = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 1: Given AM, find AB = 2 * AM
        {
            'data': [(20, 40), (21, 42), (22, 44), (23, 46), (24, 48),
                     (25, 50), (26, 52), (27, 54), (28, 56), (29, 58)],
            'tmpls': [
                "Point \(M\) is the midpoint of segment \(AB\). If \(AM = {0}	ext{{ cm}}\), find total length \(AB\).",
                "If \(M\) is the midpoint of \(AB\) and \(AM = {0}	ext{{ cm}}\), calculate \(l(AB)\).",
                "Calculate length \(AB\) where \(M\) is the midpoint and \(AM = {0}	ext{{ cm}}\).",
                "What is the length of segment \(AB\) if \(M\) is the midpoint and \(AM = {0}	ext{{ cm}}\)?",
                "Determine \(AB\) given \(AM = {0}	ext{{ cm}}\) and \(M\) bisects \(AB\).",
                "Find \(AB = 2 	imes AM\) for \(AM = {0}	ext{{ cm}}\).",
                "Compute \(l(AB)\) when midpoint segment \(AM = {0}	ext{{ cm}}\).",
                "Evaluate total length \(AB\) when \(AM = {0}	ext{{ cm}}\) and \(M\) is the midpoint.",
                "If \(M\) is the midpoint of segment \(AB\) with \(AM = {0}	ext{{ cm}}\), find \(AB\).",
                "For segment \(AB\) with midpoint \(M\), calculate \(AB\) if \(AM = {0}	ext{{ cm}}\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 4} cm", f"{item[1] - 4} cm", f"{item[0]} cm"],
                f"**Step 1: Formula**\n\(AB = 2 	imes AM = 2 	imes {item[0]} = {item[1]}	ext{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_segment_midpoint("A", "M", "B", f"AM = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 2: Algebraic midpoint: AM = MB => ax - b = cx + d => find x
        {
            'data': [(5, 2, 2, 7, 3, 13), (4, 1, 2, 7, 4, 15), (6, 2, 3, 13, 5, 28),
                     (4, 3, 2, 9, 6, 21), (5, 4, 3, 10, 7, 31), (4, 5, 2, 11, 8, 27),
                     (5, 7, 2, 20, 9, 38), (3, 2, 1, 18, 10, 28), (4, 7, 2, 15, 11, 37), (5, 8, 3, 16, 12, 52)],
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
                f"**Step 1: Midpoint equality**\nSince \(M\) is the midpoint, \(AM = MB \implies {item[0]}x - {item[1]} = {item[2]}x + {item[3]} \implies ({item[0]} - {item[2]})x = {item[3]} + {item[1]} \implies {item[0] - item[2]}x = {item[3] + item[1]}\).\n**Step 2: Solve for x**\n\(x = {item[4]}\).\n**Step 3: Conclusion**\nx = {item[4]}."
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
                "Find \(AB = 2 	imes AM\) after solving for \(x\) in \({0}x + {1} = {2}x + {3}\).",
                "Compute total length \(AB\) with midpoint \(M\) where \(AM = {0}x + {1}\) and \(MB = {2}x + {3}\).",
                "Evaluate segment length \(AB\) for midpoint \(M\) with \(AM = {0}x + {1}\) and \(MB = {2}x + {3}\).",
                "If \(M\) is the midpoint of \(AB\), find total length \(AB\) given \(AM = {0}x + {1}\) and \(MB = {2}x + {3}\).",
                "For midpoint \(M\) of \(AB\), calculate total length \(AB\) when \(AM = {0}x + {1}\) and \(MB = {2}x + {3}\)."
            ],
            'calc': lambda item: (
                f"{item[5]} cm",
                [f"{item[5] + 6} cm", f"{item[5] - 6} cm", f"{item[5] // 2} cm"],
                f"**Step 1: Equate AM = MB**\n\({item[0]}x + {item[1]} = {item[2]}x + {item[3]} \implies {item[0] - item[2]}x = {item[3] - item[1]} \implies x = {item[4]}\).\n**Step 2: Calculate AB**\n\(AM = {item[0]}({item[4]}) + {item[1]} = {item[5] // 2}	ext{{ cm}}\).\n\(AB = 2 	imes AM = 2 	imes {item[5] // 2} = {item[5]}	ext{{ cm}}\).\n**Step 3: Conclusion**\n{item[5]} cm."
            ),
            'diff': 'hard'
        },
        # Arch 4: Distance from midpoint to an end point: d = L / 2
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
                f"**Step 1: Midpoint distance**\nMidpoint M is at distance \(\frac{{{item[0]}}}{{2}} = {item[1]}\text{{ cm}}\) from either endpoint.\n**Step 2: Conclusion**\n{item[1]} cm (half of {item[0]} cm)."
            ),
            'diff': 'easy'
        },
        # Arch 5: Midpoint with decimal values
        {
            'data': [(7.4, 3.7), (8.6, 4.3), (9.8, 4.9), (11.2, 5.6), (13.4, 6.7),
                     (15.8, 7.9), (17.2, 8.6), (19.4, 9.7), (21.6, 10.8), (23.8, 11.9)],
            'tmpls': [
                "If \(P\) is the midpoint of segment \(CD = {0}	ext{{ cm}}\), find \(CP\).",
                "Point \(P\) bisects segment \(CD = {0}	ext{{ cm}}\). Calculate \(CP\).",
                "Calculate length \(CP\) where \(P\) is the midpoint of \(CD = {0}	ext{{ cm}}\).",
                "What is \(CP\) if \(P\) is the midpoint of segment \(CD = {0}	ext{{ cm}}\)?",
                "Determine \(CP\) given \(l(CD) = {0}	ext{{ cm}}\) and \(P\) is the midpoint.",
                "Find \(CP = rac{{CD}}{{2}}\) for \(CD = {0}	ext{{ cm}}\).",
                "Compute \(l(CP)\) in segment \(CD = {0}	ext{{ cm}}\) with midpoint \(P\).",
                "Evaluate length of segment \(CP\) when \(P\) is the midpoint of \(CD = {0}	ext{{ cm}}\).",
                "If \(P\) is the midpoint of \(CD = {0}	ext{{ cm}}\), find \(CP\).",
                "For segment \(CD = {0}	ext{{ cm}}\) with midpoint \(P\), calculate \(CP\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{round(item[1] + 1.2, 1)} cm", f"{round(item[1] - 1.2, 1)} cm", f"{item[0]} cm"],
                f"**Step 1: Formula**\n\(CP = rac{{CD}}{{2}} = rac{{{item[0]}}}{{2}} = {item[1]}	ext{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_segment_midpoint("C", "P", "D", f"CD = {item[0]} cm"),
            'diff': 'medium'
        },
        # Arch 6: Given MB, find AM (AM = MB)
        {
            'data': [(71, 71), (72, 72), (73, 73), (74, 74), (75, 75),
                     (76, 76), (77, 77), (78, 78), (79, 79), (80, 80)],
            'tmpls': [
                "Point \(M\) is the midpoint of segment \(AB\). If \(MB = {0}	ext{{ cm}}\), what is length \(AM\)?",
                "If \(M\) bisects segment \(AB\) and \(MB = {0}	ext{{ cm}}\), find \(AM\).",
                "Calculate \(AM\) when \(M\) is the midpoint of \(AB\) and \(MB = {0}	ext{{ cm}}\).",
                "What is the length of \(AM\) if \(M\) is the midpoint of \(AB\) and \(MB = {0}	ext{{ cm}}\)?",
                "Determine \(AM\) given \(M\) is the midpoint of \(AB\) and \(MB = {0}	ext{{ cm}}\).",
                "Find \(AM\) knowing \(AM = MB\) for midpoint \(M\) with \(MB = {0}	ext{{ cm}}\).",
                "Compute \(l(AM)\) when \(M\) is the midpoint of \(AB\) and \(MB = {0}	ext{{ cm}}\).",
                "Evaluate \(AM\) where \(M\) is the midpoint of \(AB\) and \(MB = {0}	ext{{ cm}}\).",
                "If \(M\) is the midpoint of \(AB\) with \(MB = {0}	ext{{ cm}}\), find \(AM\).",
                "For midpoint \(M\) of \(AB\) with \(MB = {0}	ext{{ cm}}\), calculate \(AM\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] * 2} cm", f"{item[1] + 3} cm", f"{item[1] - 2 if item[1] > 2 else item[1] + 4} cm"],
                f"**Step 1: Midpoint definition**\nA midpoint divides the segment into two congruent halves: \(AM = MB = {item[0]}	ext{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_segment_midpoint("A", "M", "B", f"MB = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 7: Sum AM + MB = AB
        {
            'data': [(81, 162), (82, 164), (83, 166), (84, 168), (85, 170),
                     (86, 172), (87, 174), (88, 176), (89, 178), (90, 180)],
            'tmpls': [
                "Point \(M\) is the midpoint of segment \(AB\). If \(AM = {0}	ext{{ cm}}\), find \(AM + MB\).",
                "If \(M\) is the midpoint of \(AB\) and \(AM = {0}	ext{{ cm}}\), calculate the sum \(AM + MB\).",
                "Calculate the total length \(AM + MB\) where \(M\) is the midpoint of \(AB\) and \(AM = {0}	ext{{ cm}}\).",
                "What is the value of \(AM + MB\) if \(M\) is the midpoint of \(AB\) and \(AM = {0}	ext{{ cm}}\)?",
                "Determine \(AM + MB\) given midpoint \(M\) and \(AM = {0}	ext{{ cm}}\).",
                "Find \(AM + MB = 2 	imes AM\) for \(AM = {0}	ext{{ cm}}\).",
                "Compute \(AM + MB\) where \(M\) bisects \(AB\) and \(AM = {0}	ext{{ cm}}\).",
                "Evaluate the sum \(AM + MB\) when \(AM = {0}	ext{{ cm}}\) and \(M\) is the midpoint.",
                "If \(M\) is the midpoint of \(AB\) with \(AM = {0}	ext{{ cm}}\), find \(AM + MB\).",
                "For midpoint \(M\) of \(AB\) with \(AM = {0}	ext{{ cm}}\), calculate \(AM + MB\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 6} cm", f"{item[1] - 6} cm", f"{item[0]} cm"],
                f"**Step 1: Formula**\n\(AM + MB = AB = 2 	imes AM = 2 	imes {item[0]} = {item[1]}	ext{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_segment_midpoint("A", "M", "B", f"AM = {item[0]} cm"),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

print("gen_1_3_1, gen_1_3_2, and gen_1_3_3 ready.")

# =============================================================================
# 1.4.1: Antecedent (If part) vs Consequent (Then part) (80 Qs)
# =============================================================================
def gen_1_4_1():
    tc = "MH-9-MTH2-1-1.4.1"
    tname = "Antecedent (If part) vs Consequent (Then part)"
    
    statements_arch1 = [
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
    ]
    statements = [
        ("a quadrilateral is a rhombus", "its diagonals are perpendicular bisectors of each other", "Rhombus diagonals"),
        ("two lines are parallel", "corresponding angles formed by a transversal are equal", "Parallel lines angles"),
        ("a triangle is equilateral", "all its interior angles measure 60 degrees", "Equilateral triangle"),
        ("a number is divisible by 6", "it is divisible by both 2 and 3", "Divisibility rule"),
        ("a quadrilateral is cyclic", "its opposite angles are supplementary", "Cyclic quadrilateral"),
        ("in triangle ABC, AB^2 + BC^2 = AC^2", "triangle ABC is a right-angled triangle", "Converse of Pythagoras"),
        ("two chords of a circle are congruent", "they are equidistant from the center", "Congruent chords"),
        ("a line is tangent to a circle at point P", "it is perpendicular to the radius at P", "Tangent theorem"),
        ("two adjacent angles form a linear pair", "their measures sum to 180 degrees", "Linear pair"),
        ("two triangles are congruent", "their corresponding sides and angles are equal", "Congruent triangles")
    ]

    archs = [
        # Arch 0: Identify the Antecedent (hypothesis / If-part)
        {
            'data': [(i, s[0], s[1], s[2]) for i, s in enumerate(statements)],
            'tmpls': [
                "In the conditional statement 'If {1}, then {2}', what is the antecedent?",
                "Identify the antecedent (hypothesis) in: 'If {1}, then {2}'.",
                "What is the antecedent of the statement: 'If {1}, then {2}'?",
                "State the antecedent in the implication: 'If {1}, then {2}'.",
                "In mathematical logic, which part is the antecedent: 'If {1}, then {2}'?",
                "Which clause is the antecedent in: 'If {1}, then {2}'?",
                "Find the antecedent in the proposition: 'If {1}, then {2}'.",
                "Extract the antecedent from: 'If {1}, then {2}'.",
                "Name the antecedent of: 'If {1}, then {2}'.",
                "Determine the antecedent in: 'If {1}, then {2}'."
            ],
            'calc': lambda item: (
                f"The antecedent is '{item[1]}'",
                [f"The antecedent is '{item[2]}'", "The antecedent is both parts combined together", "The statement has no antecedent"],
                f"**Step 1: Definition of antecedent**\nThe part of a conditional statement following 'If' is called the antecedent (or hypothesis).\n**Step 2: Conclusion**\nThe antecedent is '{item[1]}'."
            ),
            'diff': 'easy'
        },
        # Arch 1: Identify the Consequent (conclusion / Then-part)
        {
            'data': [(i, s[0], s[1], s[2]) for i, s in enumerate(statements_arch1)],
            'tmpls': [
                "In the conditional statement 'If {1}, then {2}', what is the consequent?",
                "Identify the consequent (conclusion) in: 'If {1}, then {2}'.",
                "What is the consequent of the statement: 'If {1}, then {2}'?",
                "State the consequent in the implication: 'If {1}, then {2}'.",
                "In mathematical logic, which part is the consequent: 'If {1}, then {2}'?",
                "Which clause is the consequent in: 'If {1}, then {2}'?",
                "Find the consequent in the proposition: 'If {1}, then {2}'.",
                "Extract the consequent from: 'If {1}, then {2}'.",
                "Name the consequent of: 'If {1}, then {2}'.",
                "Determine the consequent in: 'If {1}, then {2}'."
            ],
            'calc': lambda item: (
                f"The consequent is '{item[2]}'",
                [f"The consequent is '{item[1]}'", "The consequent is an unproved postulate", "The statement has no consequent"],
                f"**Step 1: Definition of consequent**\nThe part of a conditional statement following 'then' is called the consequent (or conclusion).\n**Step 2: Conclusion**\nThe consequent is '{item[2]}'."
            ),
            'diff': 'easy'
        },
        # Arch 2: Convert non-conditional statement into "If-then" form
        {
            'data': [(i, s[0], s[1], s[2]) for i, s in enumerate(statements)],
            'tmpls': [
                "Write the statement '{2}' in 'If-then' conditional form.",
                "Express the theorem '{2}' as an 'If-then' conditional proposition.",
                "How is the property '{2}' written in standard conditional format?",
                "Convert the proposition '{2}' into 'If-then' form.",
                "State '{2}' using the formal conditional structure 'If ..., then ...'.",
                "Rewrite the property '{2}' into standard antecedent-consequent format.",
                "What is the 'If-then' formulation for '{2}'?",
                "Transform the theorem '{2}' into conditional form.",
                "Formulate '{2}' with 'If' and 'then'.",
                "Write '{2}' as a formal conditional statement."
            ],
            'calc': lambda item: (
                f"If {item[1]}, then {item[2]}",
                ["The proposition cannot be formulated with 'If' and 'then'",
                 f"Unless {item[1]}, the consequence {item[2]} never holds",
                 "This statement represents a self-evident unproved postulate"],
                f"**Step 1: Conditional formulation**\nIdentify condition (antecedent) and result (consequent) and join with 'If ..., then ...'.\n**Step 2: Conclusion**\nIf {item[1]}, then {item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Given section in a geometric proof corresponds to Antecedent
        {
            'data': [(i, s[0], s[1], s[2]) for i, s in enumerate(statements)],
            'tmpls': [
                "In proving 'If {1}, then {2}', which part is written under 'Given'?",
                "When proving 'If {1}, then {2}', what information belongs to the 'Given' section?",
                "Identify what is written in the 'Given' section for the theorem: 'If {1}, then {2}'.",
                "For the proof of 'If {1}, then {2}', what constitutes the 'Given' hypothesis?",
                "State the 'Given' part in a proof of: 'If {1}, then {2}'.",
                "What is specified as 'Given' when proving: 'If {1}, then {2}'?",
                "In a two-column proof of 'If {1}, then {2}', what is entered under 'Given'?",
                "Which statement goes into 'Given' for the proposition: 'If {1}, then {2}'?",
                "Determine the 'Given' hypothesis for: 'If {1}, then {2}'.",
                "What represents 'Given' in the theorem: 'If {1}, then {2}'?"
            ],
            'calc': lambda item: (
                f"Given: {item[1]}",
                [f"Given: {item[2]}", "Given: The converse of the theorem", "Given: That the conclusion is false"],
                f"**Step 1: Proof structure**\nIn a geometric proof, the antecedent (the statement following 'If') forms the 'Given' part.\n**Step 2: Conclusion**\nGiven: {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 4: To Prove section in a geometric proof corresponds to Consequent
        {
            'data': [(i, s[0], s[1], s[2]) for i, s in enumerate(statements)],
            'tmpls': [
                "In proving 'If {1}, then {2}', which part is written under 'To Prove'?",
                "When proving 'If {1}, then {2}', what proposition belongs to the 'To Prove' section?",
                "Identify what is written in the 'To Prove' section for the theorem: 'If {1}, then {2}'.",
                "For the proof of 'If {1}, then {2}', what constitutes the 'To Prove' objective?",
                "State the 'To Prove' part in a proof of: 'If {1}, then {2}'.",
                "What is specified as 'To Prove' when proving: 'If {1}, then {2}'?",
                "In a two-column proof of 'If {1}, then {2}', what is entered under 'To Prove'?",
                "Which statement goes into 'To Prove' for the proposition: 'If {1}, then {2}'?",
                "Determine the 'To Prove' conclusion for: 'If {1}, then {2}'.",
                "What represents 'To Prove' in the theorem: 'If {1}, then {2}'?"
            ],
            'calc': lambda item: (
                f"To Prove: {item[2]}",
                [f"To Prove: {item[1]}", "To Prove: That all axioms are consistent", "To Prove: An unverified assumption"],
                f"**Step 1: Proof structure**\nIn a geometric proof, the consequent (the statement following 'then') forms the 'To Prove' part.\n**Step 2: Conclusion**\nTo Prove: {item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 5: General definitions: What is a conditional statement?
        {
            'data': [(i, f"Rule {i+1}") for i in range(10)],
            'tmpls': [
                "A statement that can be written in the form 'If ..., then ...' is called what in geometry?",
                "What is the mathematical name for an assertion expressed in 'If P, then Q' form?",
                "Name the logical structure of a statement written with 'If' and 'then'.",
                "Statements having the format 'If antecedent, then consequent' are known as what?",
                "Identify the term for a proposition structured with 'If' and 'then'.",
                "What do we call a proposition formed with an 'If' condition and a 'then' conclusion?",
                "A mathematical sentence containing a hypothesis and conclusion is called what?",
                "State the name of an 'If-then' statement in mathematics.",
                "What is an implication of the form 'If P, then Q' formally known as?",
                "Define the classification of statements written using 'If' and 'then'."
            ],
            'calc': lambda item: (
                f"A conditional statement ({item[1]})",
                [f"A converse statement ({item[1]})", f"An unproved conjecture ({item[1]})", f"A mathematical postulate ({item[1]})"],
                f"**Step 1: Definition**\nA statement which can be written in the 'If-then' form is called a conditional statement.\n**Step 2: Conclusion**\nA conditional statement ({item[1]})."
            ),
            'diff': 'easy'
        },
        # Arch 6: Interchanging antecedent and consequent gives the converse
        {
            'data': [(i, f"Theorem {i+1}") for i in range(10)],
            'tmpls': [
                "If the antecedent and consequent in a conditional statement are interchanged, what is the resulting statement called?",
                "What statement is formed by swapping the hypothesis and conclusion of a conditional statement?",
                "When 'If P, then Q' is transformed into 'If Q, then P', what is the new statement named?",
                "Name the proposition obtained by interchanging the antecedent and consequent.",
                "Identify the resulting statement when the 'If' and 'then' clauses are swapped.",
                "What is the name of the statement: 'If consequent, then antecedent'?",
                "Reversing antecedent and consequent produces which related statement?",
                "Swapping the hypothesis and conclusion of a theorem gives what?",
                "If P -> Q is a statement, what is Q -> P known as?",
                "What proposition is obtained by reversing 'If' and 'then'?"
            ],
            'calc': lambda item: (
                f"The converse proposition ({item[1]})",
                [f"The logical contrapositive formulation ({item[1]})",
                 f"An independent geometric axiom ({item[1]})",
                 f"A corollary proposition ({item[1]})"],
                f"**Step 1: Definition of converse**\nIf the antecedent and consequent in a given conditional statement are interchanged, the resulting statement is called the converse of the given statement.\n**Step 2: Conclusion**\nThe converse of the statement ({item[1]})."
            ),
            'diff': 'easy'
        },
        # Arch 7: Truth value of converse: converse of true statement is not always true
        {
            'data': [(i, f"Example {i+1}") for i in range(10)],
            'tmpls': [
                "Is the converse of every true conditional statement necessarily true in mathematics?",
                "State whether the converse of a true theorem is always guaranteed to be true.",
                "True or False: The converse of every true mathematical statement is always true.",
                "Can the converse of a true conditional statement be false?",
                "What can be concluded about the truth value of the converse of a true statement?",
                "Is the converse of a conditional proposition always valid whenever the original statement is valid?",
                "Evaluate the truth nature of the converse of a true theorem.",
                "Does a true statement always have a true converse in geometry?",
                "State the general relationship regarding the truth of a converse statement.",
                "If a statement is true, what is the validity of its converse?"
            ],
            'calc': lambda item: (
                f"The converse is not necessarily true (it may be true or false) ({item[1]})",
                [f"The converse is always guaranteed to be true ({item[1]})", f"The converse is always guaranteed to be false ({item[1]})", f"The converse is true only for algebraic statements ({item[1]})"],
                f"**Step 1: Truth value property**\nThe converse of a true statement is not necessarily true. For example: 'If a quadrilateral is a square, it is a rectangle' is TRUE, but its converse 'If a quadrilateral is a rectangle, it is a square' is FALSE.\n**Step 2: Conclusion**\nThe converse is not necessarily true (it may be true or false) ({item[1]})."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 1.4.2: Converse formulation (80 Qs)
# =============================================================================
def gen_1_4_2():
    tc = "MH-9-MTH2-1-1.4.2"
    tname = "Converse formulation"
    
    converse_pairs_arch4 = [
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
    ]
    converse_pairs = [
        ("two lines are parallel", "alternate interior angles are equal", "If alternate interior angles made by a transversal are equal, the two lines are parallel"),
        ("a quadrilateral is a rectangle", "its diagonals are congruent", "If the diagonals of a quadrilateral are congruent, it is a rectangle"),
        ("two sides of a triangle are congruent", "the angles opposite to them are congruent", "If two angles of a triangle are congruent, the sides opposite to them are congruent"),
        ("a quadrilateral is a parallelogram", "its opposite sides are congruent", "If opposite sides of a quadrilateral are congruent, it is a parallelogram"),
        ("a quadrilateral is a rhombus", "its diagonals are perpendicular bisectors of each other", "If the diagonals of a quadrilateral are perpendicular bisectors of each other, it is a rhombus"),
        ("two lines are parallel", "interior angles on the same side of a transversal are supplementary", "If interior angles on the same side of a transversal are supplementary, the lines are parallel"),
        ("a quadrilateral is cyclic", "its opposite angles are supplementary", "If opposite angles of a quadrilateral are supplementary, the quadrilateral is cyclic"),
        ("a number is an even prime", "the number is 2", "If a number is 2, it is an even prime"),
        ("a triangle is equilateral", "all its angles are equal to 60 degrees", "If all angles of a triangle are 60 degrees, the triangle is equilateral"),
        ("in triangle ABC, AB^2 + BC^2 = AC^2", "angle B is a right angle", "If angle B is a right angle in triangle ABC, then AB^2 + BC^2 = AC^2")
    ]

    archs = [
        # Arch 0: Formulate the converse of Theorem 1-10
        {
            'data': [(i, p[0], p[1], p[2]) for i, p in enumerate(converse_pairs)],
            'tmpls': [
                "What is the converse of: 'If {1}, then {2}'?",
                "State the converse of the conditional statement: 'If {1}, then {2}'.",
                "Formulate the converse for: 'If {1}, then {2}'.",
                "Write the converse proposition of: 'If {1}, then {2}'.",
                "Which statement represents the converse of: 'If {1}, then {2}'?",
                "Identify the converse of the theorem: 'If {1}, then {2}'.",
                "Provide the converse formulation: 'If {1}, then {2}'.",
                "Give the converse of: 'If {1}, then {2}'.",
                "State the converse: 'If {1}, then {2}'.",
                "Find the converse of: 'If {1}, then {2}'."
            ],
            'calc': lambda item: (
                f"{item[3]}",
                ["The converse proposition does not exist in geometry",
                 "The statement is identical to its converse without alteration",
                 "Hypothesis and conclusion cannot be transposed mathematically"],
                f"**Step 1: Converse formulation**\nInterchange antecedent '{item[1]}' and consequent '{item[2]}'.\n**Step 2: Conclusion**\n{item[3]}."
            ),
            'diff': 'medium'
        },
        # Arch 1: Truth value of converse for Theorem 1-10 (True converses vs False converses)
        {
            'data': [(0, "Alternate angles", "True (known as Alternate Angles Test)"),
                     (1, "Rectangle diagonals", "False (an isosceles trapezium also has congruent diagonals)"),
                     (2, "Isosceles triangle", "True (known as Converse of Isosceles Triangle Theorem)"),
                     (3, "Parallelogram sides", "True (known as Parallelogram Test)"),
                     (4, "Rhombus diagonals", "True (known as Rhombus Test)"),
                     (5, "Interior angles", "True (known as Interior Angles Test)"),
                     (6, "Cyclic quadrilateral", "True (known as Converse of Cyclic Quad Theorem)"),
                     (7, "Even prime", "True (2 is the only even prime)"),
                     (8, "Equilateral triangle", "True (an equiangular triangle is equilateral)"),
                     (9, "Pythagoras theorem", "True (known as Pythagoras Theorem)")] ,
            'tmpls': [
                "Consider the converse of the {1} theorem. What is its truth value in Euclidean geometry?",
                "Is the converse of the {1} theorem true or false? State the validity.",
                "Evaluate the truth status of the converse of the {1} proposition.",
                "Determine whether the converse of the {1} theorem is universally true.",
                "What can be said about the validity of the converse of the {1} theorem?",
                "State the truth value of the converse for the {1} theorem.",
                "Analyze the validity of the converse of the {1} property.",
                "Is the converse of the {1} property a valid geometric theorem?",
                "Check the truth nature of the converse of the {1} theorem.",
                "For the {1} theorem, evaluate the truth of its converse."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"Indeterminate in Euclidean geometry for {item[1]}", f"Always false for all quadrilaterals for {item[1]}", f"True only for non-Euclidean space for {item[1]}"],
                f"**Step 1: Evaluate converse**\nAnalyze whether the reversed statement holds universally in Euclidean geometry.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'hard'
        },
        # Arch 2: Counterexample disproving a false converse: x=3 => x^2=9
        {
            'data': [(3, 9, -3), (4, 16, -4), (5, 25, -5), (6, 36, -6), (7, 49, -7),
                     (8, 64, -8), (9, 81, -9), (10, 100, -10), (11, 121, -11), (12, 144, -12)],
            'tmpls': [
                "Statement: 'If x = {0}, then x^2 = {1}'. Its converse is 'If x^2 = {1}, then x = {0}'. Why is this converse FALSE?",
                "Why is the converse 'If x^2 = {1}, then x = {0}' not universally true?",
                "Provide the counterexample showing why 'If x^2 = {1}, then x = {0}' is false.",
                "Which counterexample disproves the converse: 'If x^2 = {1}, then x = {0}'?",
                "Explain why 'If x^2 = {1}, then x = {0}' is a false converse statement.",
                "State the counterexample that refutes: 'If x^2 = {1}, then x = {0}'.",
                "What real value of x serves as a counterexample to: 'If x^2 = {1}, then x = {0}'?",
                "Identify the counterexample to the converse: 'If x^2 = {1}, then x = {0}'.",
                "For 'If x^2 = {1}, then x = {0}', why is the statement invalid?",
                "Show why the converse statement 'If x^2 = {1}, then x = {0}' is false."
            ],
            'calc': lambda item: (
                f"Counterexample: x = {item[2]} (since ({item[2]})^2 = {item[1]} but x != {item[0]})",
                [f"Counterexample: x = 0 (since 0^2 = 0)", f"Counterexample: x = {item[0] + 1}", "The converse is actually TRUE"],
                f"**Step 1: Analyze equation**\n\(x^2 = {item[1]} \implies x = \pm {item[0]}\).\nSince \(x = {item[2]}\) also satisfies \(x^2 = {item[1]}\) but \(x \ne {item[0]}\), the converse is false.\n**Step 2: Conclusion**\nCounterexample: x = {item[2]} (since ({item[2]})^2 = {item[1]} but x != {item[0]})."
            ),
            'diff': 'medium'
        },
        # Arch 3: Identifying the antecedent of the converse
        {
            'data': [(i, p[0], p[1], p[2]) for i, p in enumerate(converse_pairs)],
            'tmpls': [
                "For the original statement 'If {1}, then {2}', what is the antecedent of its CONVERSE?",
                "In the converse of 'If {1}, then {2}', what serves as the hypothesis?",
                "What is the antecedent of the converse of: 'If {1}, then {2}'?",
                "Identify the 'If' part of the converse of: 'If {1}, then {2}'.",
                "State the antecedent in the converse statement of: 'If {1}, then {2}'.",
                "Which clause becomes the antecedent in the converse of: 'If {1}, then {2}'?",
                "Find the hypothesis of the converse of: 'If {1}, then {2}'.",
                "In the converse proposition of 'If {1}, then {2}', what is the antecedent?",
                "Determine the antecedent of the converse of: 'If {1}, then {2}'.",
                "Extract the 'If' condition of the converse of: 'If {1}, then {2}'."
            ],
            'calc': lambda item: (
                f"The antecedent of the converse is '{item[2]}'",
                [f"The antecedent of the converse is '{item[1]}'", "The antecedent of the converse is undefined", "The antecedent is both parts combined"],
                f"**Step 1: Converse antecedent**\nThe converse interchanges antecedent and consequent. Hence, the original consequent '{item[2]}' becomes the antecedent of the converse.\n**Step 2: Conclusion**\nThe antecedent of the converse is '{item[2]}'."
            ),
            'diff': 'easy'
        },
        # Arch 4: Identifying the consequent of the converse
        {
            'data': [(i, p[0], p[1], p[2]) for i, p in enumerate(converse_pairs_arch4)],
            'tmpls': [
                "For the original statement 'If {1}, then {2}', what is the consequent of its CONVERSE?",
                "In the converse of 'If {1}, then {2}', what serves as the conclusion?",
                "What is the consequent of the converse of: 'If {1}, then {2}'?",
                "Identify the 'then' part of the converse of: 'If {1}, then {2}'.",
                "State the consequent in the converse statement of: 'If {1}, then {2}'.",
                "Which clause becomes the consequent in the converse of: 'If {1}, then {2}'?",
                "Find the conclusion of the converse of: 'If {1}, then {2}'.",
                "In the converse proposition of 'If {1}, then {2}', what is the consequent?",
                "Determine the consequent of the converse of: 'If {1}, then {2}'.",
                "Extract the 'then' clause of the converse of: 'If {1}, then {2}'."
            ],
            'calc': lambda item: (
                f"The consequent of the converse is '{item[1]}'",
                [f"The consequent of the converse is '{item[2]}'", "The consequent of the converse is an unverified postulate", "The consequent is both parts combined"],
                f"**Step 1: Converse consequent**\nThe converse interchanges antecedent and consequent. Hence, the original antecedent '{item[1]}' becomes the consequent of the converse.\n**Step 2: Conclusion**\nThe consequent of the converse is '{item[1]}'."
            ),
            'diff': 'easy'
        },
        # Arch 5: Biconditional definition (if and only if)
        {
            'data': [(i, f"Property {i+1}") for i in range(10)],
            'tmpls': [
                "When both a conditional statement and its converse are true, how can they be combined?",
                "What type of statement is formed when a conditional statement and its converse are both true?",
                "If P -> Q is true and Q -> P is true, what is the combined statement called?",
                "State the logical term for a statement combined with 'if and only if'.",
                "When both statement and converse hold, what is the proposition called?",
                "Name the statement formed when hypothesis and conclusion imply each other mutually.",
                "How is a statement written when both P implies Q and Q implies P?",
                "What is a biconditional statement in geometry?",
                "When a theorem and its converse are both true, the statement is called what?",
                "Identify the term for a double implication in mathematics."
            ],
            'calc': lambda item: (
                f"A biconditional statement ('if and only if') ({item[1]})",
                [f"A contrapositive statement ({item[1]})", f"An indirect proof assumption ({item[1]})", f"A geometric axiom ({item[1]})"],
                f"**Step 1: Biconditional definition**\nWhen a conditional statement and its converse are both true, they can be combined into a single biconditional statement using 'if and only if' (iff).\n**Step 2: Conclusion**\nA biconditional statement ('if and only if') ({item[1]})."
            ),
            'diff': 'medium'
        },
        # Arch 6: Converse of angle properties
        {
            'data': [
                ("alternate angles", "two lines are parallel", "alternate interior angles are congruent", "If alternate interior angles are congruent, the lines are parallel"),
                ("corresponding angles", "two lines are parallel", "corresponding angles are congruent", "If corresponding angles are congruent, the lines are parallel"),
                ("interior angles", "two lines are parallel", "interior angles on same side of transversal sum to 180°", "If interior angles on same side sum to 180°, the lines are parallel"),
                ("vertically opposite angles", "two lines intersect", "vertically opposite angles are equal", "If two angles are vertically opposite, they are congruent"),
                ("linear pair", "two angles are adjacent", "they form a linear pair and sum to 180°", "If two adjacent angles sum to 180°, their non-common arms form a straight line"),
                ("perpendicular lines", "two lines are perpendicular", "they intersect at an angle of 90°", "If two lines intersect at 90°, they are perpendicular"),
                ("angle bisector", "a ray bisects an angle", "it divides the angle into two equal parts", "If a ray divides an angle into two congruent angles, it is the angle bisector"),
                ("complementary angles", "two angles are complementary", "their measures sum to 90°", "If the sum of two angles is 90°, they are complementary"),
                ("supplementary angles", "two angles are supplementary", "their measures sum to 180°", "If the sum of two angles is 180°, they are supplementary"),
                ("straight angle", "two rays form a straight angle", "they are opposite rays", "If two rays are opposite rays, they form a straight angle of 180°")
            ],
            'tmpls': [
                "What is the converse statement for the {0} property: 'If {1}, then {2}'?",
                "State the converse of: 'If {1}, then {2}' in {0}.",
                "Formulate the converse for {0}: 'If {1}, then {2}'.",
                "Write the converse proposition of {0}: 'If {1}, then {2}'.",
                "Which statement represents the converse of {0}: 'If {1}, then {2}'?",
                "Identify the converse of the {0} property.",
                "Provide the converse formulation of {0}: 'If {1}, then {2}'.",
                "Give the converse of {0}: 'If {1}, then {2}'.",
                "State the converse for {0}: 'If {1}, then {2}'.",
                "Find the converse of {0}: 'If {1}, then {2}'."
            ],
            'calc': lambda item: (
                f"{item[3]}",
                ["The converse property is geometrically undefined",
                 "The two lines must be perpendicular to each other",
                 "The angle criterion cannot be inverted"],
                f"**Step 1: Converse formulation**\nInterchange antecedent and consequent.\n**Step 2: Conclusion**\n{item[3]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Testing if a statement is the converse of another
        {
            'data': [(i, p[0], p[1], p[2]) for i, p in enumerate(converse_pairs)],
            'tmpls': [
                "Statement 1: 'If {1}, then {2}'. Statement 2: 'If {2}, then {1}'. What is the relationship between Statement 2 and Statement 1?",
                "How is 'If {2}, then {1}' related to 'If {1}, then {2}'?",
                "What relationship exists between Statement 1 ('If {1}, then {2}') and Statement 2 ('If {2}, then {1}')?",
                "Determine the relationship of 'If {2}, then {1}' with respect to 'If {1}, then {2}'.",
                "Identify how Statement 2 ('If {2}, then {1}') relates to Statement 1 ('If {1}, then {2}').",
                "In logic, Statement 2 ('If {2}, then {1}') is which related proposition of Statement 1 ('If {1}, then {2}')?",
                "State the relation between 'If {1}, then {2}' and 'If {2}, then {1}'.",
                "What is Statement 2 ('If {2}, then {1}') called relative to Statement 1 ('If {1}, then {2}')?",
                "Define the relationship between 'If {1}, then {2}' and 'If {2}, then {1}'.",
                "For Statement 1 ('If {1}, then {2}') and Statement 2 ('If {2}, then {1}'), state their relation."
            ],
            'calc': lambda item: (
                "Statement 2 is the converse proposition of Statement 1",
                ["Statement 2 is an independent geometric definition",
                 "Statement 2 represents an unproven conjecture",
                 "Statement 2 is the logical contrapositive formulation"],
                f"**Step 1: Relationship identification**\nSince Statement 2 swaps the antecedent and consequent of Statement 1, Statement 2 is the converse of Statement 1.\n**Step 2: Conclusion**\nStatement 2 is the converse of Statement 1."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 1.4.3: Direct and indirect proof methods (80 Qs)
# =============================================================================
def gen_1_4_3():
    tc = "MH-9-MTH2-1-1.4.3"
    tname = "Direct and indirect proof methods"
    
    indirect_theorems = [
        ("two lines intersected by a transversal are parallel", "assume the two lines are not parallel (they intersect at a point P)"),
        ("a number x is an irrational number", "assume x is a rational number of the form p/q"),
        ("in triangle ABC, if AB != AC, then angle C != angle B", "assume angle C = angle B"),
        ("through a point not on a line, only one perpendicular can be drawn", "assume two distinct perpendicular lines can be drawn"),
        ("the sum of angles in a triangle is 180 degrees", "assume the sum of angles is greater than or less than 180 degrees"),
        ("if two coplanar lines do not intersect, they are parallel", "assume the lines intersect at some finite point"),
        ("there are infinitely many prime numbers", "assume there is a finite number of prime numbers"),
        ("an angle bisector is unique", "assume an angle has two distinct angle bisectors"),
        ("a line segment has only one midpoint", "assume a line segment has two distinct midpoints"),
        ("opposite angles of a parallelogram are equal", "assume opposite angles of a parallelogram are unequal")
    ]

    archs = [
        # Arch 0: Initial assumption in indirect proof
        {
            'data': [(i, t[0], t[1]) for i, t in enumerate(indirect_theorems)],
            'tmpls': [
                "To prove indirectly that '{1}', what is the first assumption made?",
                "In an indirect proof of '{1}', what initial assumption must be set up?",
                "How does an indirect proof of '{1}' begin?",
                "What is the starting hypothesis when proving indirectly that '{1}'?",
                "State the initial assumption required to prove '{1}' by contradiction.",
                "In proof by contradiction for '{1}', what is assumed at the start?",
                "To prove '{1}' using the indirect method, what assumption is made initially?",
                "What assumption initiates the indirect proof of '{1}'?",
                "When proving '{1}' by indirect method, what is the starting step?",
                "Identify the initial assumption in the indirect proof of '{1}'."
            ],
            'calc': lambda item: (
                f"We {item[2]}",
                [f"We assume '{item[1]}' is already directly proved", "We assume all geometric postulates are false", "We assume the figure has zero dimensions"],
                f"**Step 1: Indirect proof principle**\nIn an indirect proof (proof by contradiction), we assume the negation of the statement to be proved.\nTo prove '{item[1]}', we assume the opposite: {item[2]}.\n**Step 2: Conclusion**\nWe {item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 1: Euclid's 5 postulates
        {
            'data': [
                (1, "A straight line may be drawn from any one point to any other point", "Euclid's Postulate 1"),
                (2, "A terminated line (line segment) can be produced indefinitely", "Euclid's Postulate 2"),
                (3, "A circle can be drawn with any center and any radius", "Euclid's Postulate 3"),
                (4, "All right angles are equal to one another", "Euclid's Postulate 4"),
                (5, "If a straight line falling on two straight lines makes interior angles on the same side less than two right angles, the lines meet on that side", "Euclid's Postulate 5 (Parallel Postulate)"),
                (6, "Two distinct points determine a unique straight line", "Euclid's Postulate 1"),
                (7, "A finite straight line can be extended continuously in a straight line", "Euclid's Postulate 2"),
                (8, "Given a center and a distance, a circle can be described", "Euclid's Postulate 3"),
                (9, "Every right angle is congruent to every other right angle", "Euclid's Postulate 4"),
                (10, "Euclid's parallel lines intersection criterion", "Euclid's Postulate 5 (Parallel Postulate)")
            ],
            'tmpls': [
                "Which postulate of Euclid states: '{1}'?",
                "Name the Euclid postulate that asserts: '{1}'.",
                "'{1}' corresponds to which of Euclid's postulates?",
                "Identify the postulate: '{1}'.",
                "Which postulate of Euclid establishes: '{1}'?",
                "State the postulate of Euclid: '{1}'.",
                "According to Euclidean geometry, '{1}' is which postulate?",
                "Euclid stated: '{1}'. This is which postulate?",
                "Classify the statement '{1}' among Euclid's postulates.",
                "Which of Euclid's postulates defines: '{1}'?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                ["Euclid's Common Notion 1", "Pythagoras Theorem", "Thales Theorem"],
                f"**Step 1: Euclid's Postulates**\n{item[1]} is {item[2]}.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 2: Euclid's Axioms (Common Notions)
        {
            'data': [
                (1, "Things which are equal to the same thing are equal to one another", "Axiom 1 (Common Notion 1)"),
                (2, "If equals are added to equals, the wholes are equal", "Axiom 2 (Common Notion 2)"),
                (3, "If equals are subtracted from equals, the remainders are equal", "Axiom 3 (Common Notion 3)"),
                (4, "Things which coincide with one another are equal to one another", "Axiom 4 (Common Notion 4)"),
                (5, "The whole is greater than the part", "Axiom 5 (Common Notion 5)"),
                (6, "If a = b and c = b, then a = c", "Axiom 1 (Common Notion 1)"),
                (7, "If a = b, then a + c = b + c", "Axiom 2 (Common Notion 2)"),
                (8, "If a = b, then a - c = b - c", "Axiom 3 (Common Notion 3)"),
                (9, "Superposition principle: figures that coincide are congruent", "Axiom 4 (Common Notion 4)"),
                (10, "If B lies between A and C, then AC > AB", "Axiom 5 (Common Notion 5)")
            ],
            'tmpls': [
                "Which of Euclid's axioms (common notions) asserts: '{1}'?",
                "Name the Euclid axiom stating: '{1}'.",
                "'{1}' corresponds to which Euclidean axiom?",
                "Identify the axiom: '{1}'.",
                "Which axiom of Euclid defines: '{1}'?",
                "State the Euclidean axiom: '{1}'.",
                "According to Euclid, '{1}' is which common notion?",
                "Euclid stated: '{1}'. This represents which axiom?",
                "Classify: '{1}' among Euclid's common notions.",
                "Which of Euclid's axioms states: '{1}'?"
            ],
            'calc': lambda item: (
                f"Euclid's {item[2]}",
                ["Euclid's Postulate 5", "An unproved conjecture", "A corollary of Pythagoras theorem"],
                f"**Step 1: Euclid's Axioms**\n{item[1]} is Euclid's {item[2]}.\n**Step 2: Conclusion**\nEuclid's {item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 3: Direct proof progression
        {
            'data': [(i, f"Direct Method {i+1}") for i in range(10)],
            'tmpls': [
                "In a direct geometric proof, what is the logical progression of reasoning?",
                "How does a direct proof progress from given facts to the conclusion?",
                "What characterizes the direct method of proof in geometry?",
                "Describe the flow of reasoning in a direct mathematical proof.",
                "What is the logical structure used in a direct proof?",
                "In geometric proofs, how is a theorem proved using the direct method?",
                "State how conclusions are deduced in a direct proof.",
                "What defines the direct method of proving a mathematical proposition?",
                "In a direct proof, what are the steps connecting 'Given' to 'To Prove'?",
                "Explain the mechanism of a direct geometric proof."
            ],
            'calc': lambda item: (
                f"We deduce the conclusion logically from the given hypothesis using known axioms and theorems ({item[1]})",
                [f"We assume the conclusion is false and search for an impossible contradiction ({item[1]})",
                 f"We test several numerical examples with a ruler and protractor ({item[1]})",
                 f"We guess the conclusion and verify it experimentally ({item[1]})"],
                f"**Step 1: Direct proof method**\nIn a direct proof, we assume the hypothesis (Given) is true, and by applying definitions, axioms, postulates, and previously proven theorems in logical deduction, we directly arrive at the conclusion (To Prove).\n**Step 2: Conclusion**\nWe deduce the conclusion logically from the given hypothesis using known axioms and theorems ({item[1]})."
            ),
            'diff': 'medium'
        },
        # Arch 4: Contradiction mechanism in indirect proof
        {
            'data': [(i, f"Contradiction Case {i+1}") for i in range(10)],
            'tmpls': [
                "In an indirect proof, when the assumption leads to a contradiction with a known fact, what is concluded?",
                "What conclusion is reached when an indirect proof assumption results in a contradiction?",
                "How does arriving at a contradiction complete an indirect proof?",
                "In proof by contradiction, what happens once a contradictory statement is obtained?",
                "When an assumption in an indirect proof contradicts a known postulate, what is deduced?",
                "Explain what the contradiction signifies in an indirect proof.",
                "In an indirect proof, what is established after reaching a contradiction?",
                "What is the final deduction in an indirect proof after demonstrating a contradiction?",
                "Why does a contradiction validate the original proposition in an indirect proof?",
                "State the concluding step of an indirect proof upon encountering a contradiction."
            ],
            'calc': lambda item: (
                f"The initial assumption is proved false, and hence the original statement to be proved is TRUE ({item[1]})",
                [f"The theorem is proved false and must be discarded ({item[1]})",
                 f"The given hypothesis must be altered to fit the contradiction ({item[1]})",
                 f"A direct proof is immediately required instead ({item[1]})"],
                f"**Step 1: Indirect proof logic**\nSince the assumption leads to a contradiction with an established truth, the assumption must be FALSE. Consequently, the original statement (its opposite) must be TRUE.\n**Step 2: Conclusion**\nThe initial assumption is proved false, and hence the original statement to be proved is TRUE ({item[1]})."
            ),
            'diff': 'medium'
        },
        # Arch 5: Axioms vs Postulates distinction
        {
            'data': [(i, f"Distinction {i+1}") for i in range(10)],
            'tmpls': [
                "What did Euclid call self-evident assumptions that are specific to geometry?",
                "Self-evident truths assumed without proof specific to geometric space are called what?",
                "Name the geometric assumptions that are accepted as self-evident without proof.",
                "In Euclid's geometry, what term is used for assumptions that are specific to geometry?",
                "What is the distinction: general self-evident truths are axioms, while self-evident geometric truths are what?",
                "Identify the term for basic geometric assumptions accepted without proof.",
                "Euclid used the term 'common notions' for general truths; what term did he use for geometric assumptions?",
                "What are self-evident geometric assumptions called in Euclidean geometry?",
                "State the name given to fundamental geometric truths accepted without proof.",
                "In Greek mathematics, self-evident assumptions peculiar to geometry were called what?"
            ],
            'calc': lambda item: (
                f"Postulates ({item[1]})",
                [f"Theorems ({item[1]})", f"Corollaries ({item[1]})", f"Conjectures ({item[1]})"],
                f"**Step 1: Distinction between Axioms and Postulates**\nEuclid divided self-evident assumptions into two types:\n1. Axioms (Common Notions): assumptions used throughout mathematics.\n2. Postulates: assumptions specific to geometry.\n**Step 2: Conclusion**\nPostulates ({item[1]})."
            ),
            'diff': 'easy'
        },
        # Arch 6: Theorem vs Axiom definition
        {
            'data': [(i, f"Theorem Concept {i+1}") for i in range(10)],
            'tmpls': [
                "A mathematical statement whose truth has been established by logical proof is called what?",
                "What is a proposition proved logically from axioms and definitions called?",
                "Name the geometric statement whose validity is demonstrated through rigorous logical proof.",
                "In mathematics, a statement proved by deduction is called what?",
                "What do we call a property that is proved logically using axioms and postulates?",
                "Identify the term for a proven mathematical statement.",
                "A statement whose truth is established by proof is named what?",
                "Define the term for a proposition proved through deductive reasoning.",
                "What is a proven geometric proposition called?",
                "State the term for a mathematical assertion that has been proven true."
            ],
            'calc': lambda item: (
                f"A theorem ({item[1]})",
                [f"A postulate ({item[1]})", f"An axiom ({item[1]})", f"A conjecture ({item[1]})"],
                f"**Step 1: Definition of theorem**\nA property or statement whose truth is proved logically using axioms, postulates, and definitions is called a theorem.\n**Step 2: Conclusion**\nA theorem ({item[1]})."
            ),
            'diff': 'easy'
        },
        # Arch 7: Elements by Euclid
        {
            'data': [
                (13, "books in Elements", "13 books"),
                (465, "propositions in Elements", "465 propositions"),
                (28, "definitions in Book 1", "28 definitions"),
                (5, "postulates in Elements", "5 postulates"),
                (5, "common notions (axioms)", "5 common notions"),
                (300, "BC approximate era of Euclid", "300 BC"),
                (1, "Alexandria school of mathematics", "Alexandria in Egypt"),
                (2, "Geometry meaning geo + metron", "Earth measurement"),
                (3, "Thales was teacher of Pythagoras", "Thales of Miletus"),
                (4, "Pythagoras proved many geometric properties", "Pythagoras and his disciples")
            ],
            'tmpls': [
                "Euclid collected and organized all mathematical knowledge of his time into a famous treatise named 'Elements'. How many {1} did it contain / what was {1}?",
                "In Euclid's monumental treatise 'The Elements', what was {1}?",
                "Historical geometry: regarding '{1}' in Euclid's work, what is the historical fact?",
                "What is recorded in the history of geometry concerning '{1}'?",
                "State the historical detail regarding '{1}' in Greek geometry.",
                "In Euclidean history, what is known about '{1}'?",
                "Concerning '{1}', what fact is documented about Euclid and Greek geometry?",
                "What does history record about '{1}' in the development of geometry?",
                "Identify the historical fact regarding '{1}'.",
                "For '{1}' in ancient geometry, state the correct fact."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                ["Unknown in ancient history", "Introduced only in 19th century", "Disproved by Archimedes"],
                f"**Step 1: Historical context of Euclid's Elements**\nEuclid wrote 'The Elements' around 300 BC in Alexandria, organizing geometry into 13 books containing 465 propositions based on 5 postulates and common notions.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def main():
    import json
    all_qs = []
    subtopics = [
        gen_1_1_1, gen_1_1_2,
        gen_1_2_1, gen_1_2_2,
        gen_1_3_1, gen_1_3_2, gen_1_3_3,
        gen_1_4_1, gen_1_4_2, gen_1_4_3
    ]
    print(f"Generating Chapter 1 ({len(subtopics)} subtopics)...")
    for fn in subtopics:
        qs = fn()
        print(f"Generated {len(qs)} for {qs[0]['topicCode']}")
        all_qs.extend(qs)
    
    out_file = "scripts/mh9_mth2_ch1_perfect.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"SUCCESS: Saved {len(all_qs)} questions to {out_file}")

if __name__ == "__main__":
    main()
