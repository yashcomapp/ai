# scripts/gen_ch1.py
import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine import SEQS_80, build_q, generate_subtopic, svg_numberline, svg_segment_midpoint

CH_NUM = 1
CH_NAME = "Basic Concepts in Geometry"

# 1.1.1: Coordinates on number line
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
                [f"{item[1] + 1}", f"{item[1] - 1}", f"{item[0]}"],
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
                [f"{abs(item[0])}", f"{item[0] - 1}", f"{item[0] + 1}"],
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
                [f"{item[1] + 2}", f"{item[1] - 2 if item[1] > 2 else item[1] + 4}", f"{item[0]}"],
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
                [f"{item[2] + 1}", f"{item[2] - 1}", f"{item[1]}"],
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
                "For point \(A({0})\), find the coordinate of point \(C\) which is {1} units to its left."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 2}", f"{item[2] - 2}", f"{item[1]}"],
                f"**Step 1: Movement to the left**\nMoving to the left subtracts the distance: \({item[0]} - {item[1]} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(item[2], item[0], "C", "A"),
            'diff': 'easy'
        },
        # Arch 5: Midpoint coordinate on number line: x_M = (x1 + x2)/2
        {
            'data': [(2, 8, 5), (4, 12, 8), (6, 16, 11), (8, 20, 14), (10, 24, 17),
                     (-6, 2, -2), (-8, 4, -2), (-10, 2, -4), (-4, 8, 2), (-2, 10, 4)],
            # Ensure all answers are distinct:
            # Let's adjust answers so no two collide:
            # (2, 8) -> 5, (4, 12) -> 8, (6, 16) -> 11, (8, 20) -> 14, (10, 24) -> 17,
            # (-6, 0) -> -3, (-8, 2) -> -3? no: (-12, 2) -> -5, (-14, 0) -> -7, (-4, 6) -> 1, (-2, 8) -> 3
            'data': [(2, 8, 5), (4, 12, 8), (6, 16, 11), (8, 20, 14), (10, 24, 17),
                     (-12, 2, -5), (-14, 0, -7), (-18, 0, -9), (-4, 6, 1), (-2, 8, 3)],
            'tmpls': [
                "Points \(A\) and \(B\) have coordinates {0} and {1} respectively. Find the coordinate of their midpoint \(M\).",
                "Calculate the coordinate of midpoint \(M\) of segment \(AB\) with coordinates \(A({0})\) and \(B({1})\).",
                "What is the coordinate of the midpoint between points at {0} and {1} on the number line?",
                "Determine the midpoint coordinate of points \(A({0})\) and \(B({1})\).",
                "Find the coordinate of midpoint \(M\) for points with coordinates {0} and {1}.",
                "Compute midpoint coordinate \(x_M = \frac{{{0} + {1}}}{{2}}\) on the real line.",
                "Calculate the coordinate halfway between {0} and {1} on the number axis.",
                "Evaluate the coordinate of the midpoint of segment connecting {0} and {1}.",
                "If coordinates of \(A\) and \(B\) are {0} and {1}, find the midpoint coordinate.",
                "For points \(A({0})\) and \(B({1})\), calculate the coordinate of midpoint \(M\)."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 2}", f"{item[2] - 2}", f"{item[0] + item[1]}"],
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
                f"{item[2]}",
                [f"{item[0] if item[2] == item[1] else item[1]}", f"{abs(item[0])}", f"-{abs(item[2])}"],
                f"**Step 1: Number line ordering**\nOn a horizontal number line, the number that lies farther to the right is greater.\n{item[2]} lies to the right of {item[0] if item[2] == item[1] else item[1]}, so {item[2]} > {item[0] if item[2] == item[1] else item[1]}.\n**Step 2: Conclusion**\n{item[2]}."
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
                f"{item[1]}",
                [f"{item[0]}", f"{item[1] + 2}", f"{item[1] - 2}"],
                f"**Step 1: Distance formula**\n\(d(A, B) = \text{{Greater}} - \text{{Smaller}} = {item[0]} - (-{item[0]}) = {item[0]} + {item[0]} = {item[1]}\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'svg': lambda item: svg_numberline(-item[0], item[0], "A", "B"),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# 1.1.2: Distance formula: d(A, B) = Greater - Smaller
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
                [f"{item[2] + 2}", f"{item[2] - 2 if item[2] > 2 else item[2] + 4}", f"{item[0] + item[1]}"],
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
                f"{item[2]}",
                [f"{item[2] + 2}", f"{item[2] - 2 if item[2] > 2 else item[2] + 4}", f"{item[1] - abs(item[0])}"],
                f"**Step 1: Identify coordinates**\n{item[1]} > {item[0]}.\n**Step 2: Distance formula**\n\(d(P, Q) = {item[1]} - ({item[0]}) = {item[1]} + {abs(item[0])} = {item[2]}\).\n**Step 3: Conclusion**\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(item[0], item[1], "P", "Q"),
            'diff': 'easy'
        },
        # Arch 2: Both negative: d = (-smaller) - (-larger) = larger - smaller
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
                f"{item[2]}",
                [f"{item[2] + 2}", f"{item[2] - 2 if item[2] > 2 else item[2] + 4}", f"{abs(item[0]) + abs(item[1])}"],
                f"**Step 1: Identify greater coordinate**\nSince both numbers are negative, the one closer to zero is greater: {item[1]} > {item[0]}.\n**Step 2: Distance formula**\n\(d(R, S) = {item[1]} - ({item[0]}) = {item[1]} + {abs(item[0])} = {item[2]}\).\n**Step 3: Conclusion**\n{item[2]}."
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
                f"{item[2]}",
                [f"{item[2] + 2}", f"{item[2] - 2}", f"{item[1]}"],
                f"**Step 1: Formula**\nSince \(B\) lies to the right of \(A\), its coordinate is greater: \(\text{{Coord}}(B) = \text{{Coord}}(A) + d(A, B) = {item[0]} + {item[1]} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(item[0], item[2], "A", "B"),
            'diff': 'medium'
        },
        # Arch 4: Given d(A, B) and coordinate of B, find coordinate of A (to the left)
        {
            'data': [(14, 6, 8), (15, 7, 8), (16, 9, 7), (18, 10, 8), (20, 11, 9),
                     (4, 7, -3), (5, 9, -4), (6, 11, -5), (7, 13, -6), (8, 15, -7)],
            # Ensure distinct answers:
            # 8, 8 collides; let's vary item[2]:
            # (14, 5, 9), (15, 7, 8), (16, 9, 7), (18, 12, 6), (20, 15, 5), (4, 6, -2), (5, 8, -3), (6, 10, -4), (7, 12, -5), (8, 14, -6)
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
                f"{item[2]}",
                [f"{item[2] + 2}", f"{item[2] - 2}", f"{item[1]}"],
                f"**Step 1: Formula**\nSince \(A\) lies to the left of \(B\), its coordinate is smaller: \(\text{{Coord}}(A) = \text{{Coord}}(B) - d(A, B) = {item[0]} - {item[1]} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(item[2], item[0], "A", "B"),
            'diff': 'medium'
        },
        # Arch 5: Non-negativity property: distance is always non-negative
        {
            'data': [(10, 2), (12, 3), (14, 4), (16, 5), (18, 6),
                     (20, 7), (22, 8), (24, 9), (26, 10), (28, 11)],
            'tmpls': [
                "Can the geometric distance between two distinct points on a number line ever be negative?",
                "State whether the distance between two points on a number line can be negative.",
                "Is it possible for distance \(d(A, B)\) to be a negative number?",
                "What is the sign of distance between two distinct points on a number line?",
                "True or False: Distance between any two points is always non-negative.",
                "Can distance between points on a number line be less than zero?",
                "State the nature of distance \(d(A, B)\) between two points on a number axis.",
                "Is the distance between any two points on a number line always non-negative?",
                "Can distance between two real coordinates be negative?",
                "What can be said about the sign of distance \(d(A, B)\)?"
            ],
            'calc': lambda item: (
                "Always non-negative (>= 0)",
                ["Can be negative", "Sometimes negative", "Always negative"],
                f"**Step 1: Fundamental property of distance**\nDistance between any two points is defined as Greater coordinate - Smaller coordinate, which is always non-negative: \(d(A, B) \ge 0\).\n**Step 2: Conclusion**\nAlways non-negative (>= 0)."
            ),
            'diff': 'easy'
        },
        # Arch 6: Distance when coordinates are identical: d(A, A) = 0
        {
            'data': [(5, 0), (9, 0), (-4, 0), (-8, 0), (12, 0),
                     (-15, 0), (18, 0), (-20, 0), (25, 0), (30, 0)],
            'tmpls': [
                "Point \(A\) has coordinate {0}. What is the distance \(d(A, A)\) from point \(A\) to itself?",
                "Find the distance between coincident points both having coordinate {0}.",
                "What is the distance \(d(A, A)\) for a point with coordinate {0}?",
                "Calculate \(d(A, A)\) where coordinate of \(A\) is {0}.",
                "Determine \(d(A, A)\) for point \(A({0})\) on the number line.",
                "Compute distance \(d(A, A) = |{0} - {0}|\).",
                "Evaluate the distance from point \(A({0})\) to itself.",
                "What is the distance of point \(A({0})\) from itself?",
                "If point \(A\) has coordinate {0}, find \(d(A, A)\).",
                "For point \(A({0})\), calculate the distance \(d(A, A)\)."
            ],
            'calc': lambda item: (
                "0",
                [f"{item[0]}", "1", f"{abs(item[0])}"],
                f"**Step 1: Coincident points**\nThe distance of any point from itself is zero: \(d(A, A) = {item[0]} - {item[0]} = 0\).\n**Step 2: Conclusion**\n0."
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
                f"{item[3]}",
                [f"{item[3] + 2}", f"{item[3] - 2 if item[3] > 2 else item[3] + 4}", f"{item[1]}"],
                f"**Step 1: Distance formula**\nSince \(A-B-C\), \(d(A, C) = \text{{Coord}}(C) - \text{{Coord}}(A) = {item[2]} - ({item[0]}) = {item[3]}\).\n**Step 2: Conclusion**\n{item[3]}."
            ),
            'svg': lambda item: svg_numberline(item[0], item[2], "A", "C"),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

print("gen_1_1_1 and gen_1_1_2 defined.")

# 1.2.1: Condition: d(A, B) + d(B, C) = d(A, C)
def gen_1_2_1():
    tc = "MH-9-MTH2-1-1.2.1"
    tname = "Condition: d(A, B) + d(B, C) = d(A, C)"
    archs = [
        # Arch 0: Given d(A, B) and d(B, C) when A-B-C, find d(A, C) = d(A, B) + d(B, C)
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
                [f"{item[2] + 2}", f"{item[2] - 2 if item[2] > 2 else item[2] + 4}", f"{item[1] - item[0]}"],
                f"**Step 1: Betweenness condition**\nSince \(A-B-C\), \(d(A, C) = d(A, B) + d(B, C) = {item[0]} + {item[1]} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(0, item[2], "A", "C"),
            'diff': 'easy'
        },
        # Arch 1: Given d(A, C) and d(A, B), find d(B, C) = d(A, C) - d(A, B)
        {
            'data': [(14, 6, 8), (16, 7, 9), (18, 7, 11), (20, 8, 12), (23, 9, 14),
                     (25, 9, 16), (28, 10, 18), (30, 10, 20), (33, 12, 21), (35, 12, 23)],
            'tmpls': [
                "If \(A-B-C\), \(d(A, C) = {0}\) and \(d(A, B) = {1}\), find distance \(d(B, C)\).",
                "Given betweenness \(A-B-C\) with \(d(A, C) = {0}\) and \(d(A, B) = {1}\), calculate \(d(B, C)\).",
                "Calculate \(d(B, C)\) in betweenness \(A-B-C\) where \(d(A, C) = {0}\) and \(d(A, B) = {1}\).",
                "What is the distance \(d(B, C)\) if \(A-B-C\), \(d(A, C) = {0}\), and \(d(A, B) = {1}\)?",
                "Determine \(d(B, C)\) given \(A-B-C\) with \(d(A, C) = {0}\) and \(d(A, B) = {1}\).",
                "Find \(d(B, C) = d(A, C) - d(A, B)\) for \(d(A, C) = {0}\) and \(d(A, B) = {1}\).",
                "Compute \(d(B, C)\) for collinear points in order \(A-B-C\) with \(d(A, C) = {0}\) and \(d(A, B) = {1}\).",
                "Evaluate \(d(B, C)\) when \(d(A, C) = {0}\) and \(d(A, B) = {1}\) with \(A-B-C\).",
                "If \(A-B-C\), \(d(A, C) = {0}\), and \(d(A, B) = {1}\), find \(d(B, C)\).",
                "For collinear points \(A, B, C\) with \(A-B-C\), calculate \(d(B, C)\) when \(d(A, C) = {0}\) and \(d(A, B) = {1}\)."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 2}", f"{item[2] - 2 if item[2] > 2 else item[2] + 4}", f"{item[0] + item[1]}"],
                f"**Step 1: Formula**\nSince \(A-B-C\), \(d(A, B) + d(B, C) = d(A, C) \implies d(B, C) = d(A, C) - d(A, B) = {item[0]} - {item[1]} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(0, item[0], "A", "C"),
            'diff': 'easy'
        },
        # Arch 2: Identify which point lies between the other two
        {
            'data': [(5, 8, 13, "B"), (6, 9, 15, "Q"), (7, 11, 18, "Y"), (8, 12, 20, "M"), (9, 14, 23, "P"),
                     (10, 15, 25, "B"), (11, 16, 27, "Q"), (12, 17, 29, "Y"), (13, 19, 32, "M"), (14, 21, 35, "P")],
            'tmpls': [
                "If \(d(A, B) = {0}\), \(d(B, C) = {1}\), and \(d(A, C) = {2}\), which point lies between the other two?",
                "Given \(d(A, B) = {0}\), \(d(B, C) = {1}\), and \(d(A, C) = {2}\), determine which point is between the other two.",
                "For points with \(d(A, B) = {0}\), \(d(B, C) = {1}\), and \(d(A, C) = {2}\), identify the middle point.",
                "Which point lies between the other two if \(d(A, B) = {0}\), \(d(B, C) = {1}\), and \(d(A, C) = {2}\)?",
                "Determine the point between the other two given \(d(A, B) = {0}, d(B, C) = {1}, d(A, C) = {2}\).",
                "Find which point lies between the other two for distances {0}, {1}, and {2}.",
                "State which point is between the remaining two when \(d(A, B) = {0}, d(B, C) = {1}, d(A, C) = {2}\).",
                "Evaluate which point lies between the other two given \(d(A, B) = {0}, d(B, C) = {1}, d(A, C) = {2}\).",
                "If \(d(A, B) = {0}, d(B, C) = {1}\), and \(d(A, C) = {2}\), which point is in between?",
                "For three collinear points with \(d(A, B) = {0}, d(B, C) = {1}, d(A, C) = {2}\), state the middle point."
            ],
            'calc': lambda item: (
                "Point B",
                ["Point A", "Point C", "Points are not collinear"],
                f"**Step 1: Check betweenness condition**\n\(d(A, B) + d(B, C) = {item[0]} + {item[1]} = {item[2]} = d(A, C)\).\nSince the sum of two smaller distances equals the largest distance, point B lies between points A and C: \(A-B-C\).\n**Step 2: Conclusion**\nPoint B."
            ),
            'diff': 'easy'
        },
        # Arch 3: Given coordinates, verify betweenness order
        {
            'data': [(2, 7, 15, "A-B-C"), (3, 8, 14, "P-Q-R"), (1, 6, 12, "X-Y-Z"), (4, 9, 16, "D-E-F"), (5, 11, 19, "L-M-N"),
                     (-5, 0, 8, "A-B-C"), (-7, -2, 4, "P-Q-R"), (-8, -3, 5, "X-Y-Z"), (-9, -1, 6, "D-E-F"), (-10, -4, 3, "L-M-N")],
            'tmpls': [
                "Coordinates of three collinear points on a number line are {0}, {1}, and {2}. State their betweenness order.",
                "Points have coordinates {0}, {1}, and {2}. What is their order of betweenness on the number line?",
                "Determine the betweenness relation for points with coordinates {0}, {1}, and {2}.",
                "What is the betweenness order of points having coordinates {0}, {1}, and {2}?",
                "Identify the correct betweenness order for coordinates {0}, {1}, and {2}.",
                "State the order of points on the number line with coordinates {0}, {1}, and {2}.",
                "Find the betweenness sequence for points with coordinates {0}, {1}, and {2}.",
                "Evaluate the betweenness order of points plotted at {0}, {1}, and {2}.",
                "If three points on a line have coordinates {0}, {1}, and {2}, what is their order?",
                "For coordinates {0}, {1}, and {2}, write the betweenness relation."
            ],
            'calc': lambda item: (
                f"{item[0]} < {item[1]} < {item[2]}",
                [f"{item[1]} < {item[0]} < {item[2]}", f"{item[0]} < {item[2]} < {item[1]}", "Not collinear"],
                f"**Step 1: Compare coordinates**\nSince \({item[0]} < {item[1]} < {item[2]}\), the point with coordinate {item[1]} lies between the points with coordinates {item[0]} and {item[2]}.\n**Step 2: Conclusion**\n{item[0]} < {item[1]} < {item[2]}."
            ),
            'svg': lambda item: svg_numberline(item[0], item[2], "A", "C"),
            'diff': 'medium'
        },
        # Arch 4: Non-collinear case: d1 + d2 != d3
        {
            'data': [(4, 6, 12), (5, 7, 14), (6, 8, 16), (7, 9, 18), (8, 10, 20),
                     (3, 5, 10), (4, 7, 13), (5, 8, 15), (6, 9, 17), (7, 10, 19)],
            'tmpls': [
                "If \(d(P, Q) = {0}\), \(d(Q, R) = {1}\), and \(d(P, R) = {2}\), are points \(P, Q, R\) collinear?",
                "Determine whether points \(P, Q, R\) are collinear given \(d(P, Q) = {0}, d(Q, R) = {1}, d(P, R) = {2}\).",
                "Given distances {0}, {1}, and {2} between three points, state if they are collinear.",
                "Are points with mutual distances {0}, {1}, and {2} collinear?",
                "Check if points \(P, Q, R\) are collinear when \(d(P, Q) = {0}, d(Q, R) = {1}, d(P, R) = {2}\).",
                "State collinearity of points having distances \(d(P, Q) = {0}, d(Q, R) = {1}, d(P, R) = {2}\).",
                "Evaluate whether points \(P, Q, R\) lie on a single line given distances {0}, {1}, {2}.",
                "Do points \(P, Q, R\) satisfy betweenness if \(d(P, Q) = {0}, d(Q, R) = {1}, d(P, R) = {2}\)?",
                "If distances between three points are {0}, {1}, and {2}, are they collinear?",
                "For points \(P, Q, R\) with \(d(P, Q) = {0}, d(Q, R) = {1}, d(P, R) = {2}\), state whether they are collinear."
            ],
            'calc': lambda item: (
                "Non-collinear (points do not lie on a line)",
                ["Collinear with P-Q-R", "Collinear with Q-P-R", "Collinear with P-R-Q"],
                f"**Step 1: Check betweenness condition**\nSum of two smaller distances: \({item[0]} + {item[1]} = {item[0] + item[1]}\).\nLargest distance: \({item[2]}\).\nSince \({item[0] + item[1]} \\ne {item[2]}\), the betweenness condition is not satisfied.\n**Step 2: Conclusion**\nNon-collinear (points do not lie on a line)."
            ),
            'diff': 'easy'
        },
        # Arch 5: Two possibilities: if collinear, C can be between A and B or B between A and C
        {
            'data': [(10, 3, 13, 7), (12, 4, 16, 8), (14, 5, 19, 9), (16, 6, 22, 10), (18, 7, 25, 11),
                     (20, 8, 28, 12), (22, 9, 31, 13), (24, 10, 34, 14), (26, 11, 37, 15), (28, 12, 40, 16)],
            'tmpls': [
                "Points \(A, B, C\) are collinear. If \(d(A, B) = {0}\) and \(d(B, C) = {1}\), find the two possible values of \(d(A, C)\).",
                "Given collinear points \(A, B, C\) with \(d(A, B) = {0}\) and \(d(B, C) = {1}\), calculate all possible values of \(d(A, C)\).",
                "What are the two possible distances \(d(A, C)\) if \(d(A, B) = {0}\) and \(d(B, C) = {1}\) for collinear points?",
                "Determine the two possible values of \(d(A, C)\) given collinear points with \(d(A, B) = {0}\) and \(d(B, C) = {1}\).",
                "Find the possible lengths of segment \(AC\) if \(A, B, C\) are collinear and \(AB = {0}, BC = {1}\).",
                "Compute the two possible distances \(d(A, C)\) when \(d(A, B) = {0}\) and \(d(B, C) = {1}\).",
                "Evaluate the possible values of \(d(A, C)\) for collinear points with distances {0} and {1}.",
                "If \(A, B, C\) are on a line with \(d(A, B) = {0}\) and \(d(B, C) = {1}\), state both possible values of \(d(A, C)\).",
                "For collinear points \(A, B, C\), find the two values of \(d(A, C)\) given \(d(A, B) = {0}\) and \(d(B, C) = {1}\).",
                "Calculate both possible lengths of \(AC\) given collinear points with \(AB = {0}\) and \(BC = {1}\)."
            ],
            'calc': lambda item: (
                f"{item[2]} or {item[3]}",
                [f"{item[2]} only", f"{item[3]} only", f"{item[0]} or {item[1]}"],
                f"**Step 1: Case 1 - Point B lies between A and C (A-B-C)**\n\(d(A, C) = d(A, B) + d(B, C) = {item[0]} + {item[1]} = {item[2]}\).\n**Step 2: Case 2 - Point C lies between A and B (A-C-B)**\n\(d(A, C) = d(A, B) - d(B, C) = {item[0]} - {item[1]} = {item[3]}\).\n**Step 3: Conclusion**\n{item[2]} or {item[3]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Distance ratio in betweenness: d(A, B) : d(B, C)
        {
            'data': [(4, 8, "1:2"), (3, 9, "1:3"), (6, 9, "2:3"), (8, 12, "2:3"), (5, 15, "1:3"),
                     (6, 8, "3:4"), (10, 15, "2:3"), (4, 12, "1:3"), (9, 12, "3:4"), (5, 20, "1:4")],
            'tmpls': [
                "If \(A-B-C\) with \(d(A, B) = {0}\) and \(d(B, C) = {1}\), find the ratio \(d(A, B) : d(B, C)\) in simplest form.",
                "Calculate ratio \(d(A, B) : d(B, C)\) given \(d(A, B) = {0}\) and \(d(B, C) = {1}\).",
                "What is the simplified ratio of \(d(A, B)\) to \(d(B, C)\) if \(d(A, B) = {0}\) and \(d(B, C) = {1}\)?",
                "Determine the ratio \(d(A, B) : d(B, C)\) for collinear points with distances {0} and {1}.",
                "Find ratio \(AB : BC\) in simplest form when \(AB = {0}\) and \(BC = {1}\).",
                "Compute the ratio of segment \(AB\) to segment \(BC\) for \(AB = {0}\) and \(BC = {1}\).",
                "Evaluate the ratio \(d(A, B) : d(B, C)\) given \(d(A, B) = {0}\) and \(d(B, C) = {1}\).",
                "In betweenness \(A-B-C\), find the ratio \(d(A, B) : d(B, C)\) for distances {0} and {1}.",
                "If \(d(A, B) = {0}\) and \(d(B, C) = {1}\), find the ratio \(AB : BC\).",
                "For collinear points \(A-B-C\), calculate ratio \(d(A, B) : d(B, C)\) when distances are {0} and {1}."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2][::-1]}", f"{item[0]}:{item[1]}", "1:1"],
                f"**Step 1: Simplify ratio**\n\(\frac{{d(A, B)}}{{d(B, C)}} = \frac{{{item[0]}}}{{{item[1]}}} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 7: Fraction of total distance: d(A, B) / d(A, C)
        {
            'data': [(3, 9, 12, "1/4"), (4, 12, 16, "1/4"), (5, 10, 15, "1/3"), (6, 12, 18, "1/3"), (7, 14, 21, "1/3"),
                     (2, 8, 10, "1/5"), (3, 12, 15, "1/5"), (4, 16, 20, "1/5"), (6, 18, 24, "1/4"), (8, 16, 24, "1/3")],
            'tmpls': [
                "If \(A-B-C\) with \(d(A, B) = {0}\) and \(d(B, C) = {1}\), what fraction of total distance \(d(A, C)\) is \(d(A, B)\)?",
                "Calculate the fraction \(\frac{{d(A, B)}}{{d(A, C)}}\) given \(d(A, B) = {0}\) and \(d(B, C) = {1}\).",
                "What fraction of segment \(AC\) is segment \(AB\) if \(AB = {0}\) and \(BC = {1}\) with \(A-B-C\)?",
                "Determine \(\frac{{d(A, B)}}{{d(A, C)}}\) in simplest form given \(d(A, B) = {0}\) and \(d(B, C) = {1}\).",
                "Find the ratio of \(d(A, B)\) to total distance \(d(A, C)\) as a fraction for distances {0} and {1}.",
                "Compute the fraction \(\frac{{AB}}{{AC}}\) for collinear points with \(AB = {0}\) and \(BC = {1}\).",
                "Evaluate fraction \(\frac{{d(A, B)}}{{d(A, C)}}\) when \(d(A, B) = {0}\) and \(d(B, C) = {1}\).",
                "In betweenness \(A-B-C\), what part of \(d(A, C)\) is \(d(A, B)\) for distances {0} and {1}?",
                "If \(d(A, B) = {0}\) and \(d(B, C) = {1}\) with \(A-B-C\), find fraction \(\frac{{d(A, B)}}{{d(A, C)}}\).",
                "For collinear points \(A-B-C\), calculate \(\frac{{d(A, B)}}{{d(A, C)}}\) when \(AB = {0}\) and \(BC = {1}\)."
            ],
            'calc': lambda item: (
                f"{item[3]}",
                ["1/2", "2/3", "3/4"],
                f"**Step 1: Total distance**\n\(d(A, C) = d(A, B) + d(B, C) = {item[0]} + {item[1]} = {item[2]}\).\n**Step 2: Fraction calculation**\n\(\frac{{d(A, B)}}{{d(A, C)}} = \frac{{{item[0]}}}{{{item[2]}}} = {item[3]}\).\n**Step 3: Conclusion**\n{item[3]}."
            ),
            'svg': lambda item: svg_numberline(0, item[2], "A", "C"),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

print("gen_1_2_1 defined.")

# 1.2.2: Collinear vs non-collinear test
def gen_1_2_2():
    tc = "MH-9-MTH2-1-1.2.2"
    tname = "Collinear vs non-collinear test"
    archs = [
        # Arch 0: Test collinearity: sum of two smaller equals largest (Collinear)
        {
            'data': [(4, 7, 11), (5, 8, 13), (6, 9, 15), (7, 10, 17), (8, 12, 20),
                     (9, 13, 22), (10, 14, 24), (11, 15, 26), (12, 16, 28), (13, 17, 30)],
            'tmpls': [
                "Determine whether points \(A, B, C\) are collinear if \(d(A, B) = {0}\), \(d(B, C) = {1}\), and \(d(A, C) = {2}\).",
                "Given distances \(d(A, B) = {0}, d(B, C) = {1}, d(A, C) = {2}\), state if \(A, B, C\) are collinear.",
                "Calculate whether points with distances {0}, {1}, and {2} lie on a straight line.",
                "Are points \(A, B, C\) collinear when \(d(A, B) = {0}\), \(d(B, C) = {1}\), and \(d(A, C) = {2}\)?",
                "Test collinearity for points \(A, B, C\) having \(d(A, B) = {0}, d(B, C) = {1}, d(A, C) = {2}\).",
                "Check if points \(A, B, C\) are collinear for distances {0}, {1}, and {2}.",
                "State if points \(A, B, C\) are collinear given \(d(A, B) = {0}, d(B, C) = {1}, d(A, C) = {2}\).",
                "Evaluate collinearity of points \(A, B, C\) having distances {0}, {1}, and {2}.",
                "If \(d(A, B) = {0}, d(B, C) = {1}\), and \(d(A, C) = {2}\), are points \(A, B, C\) collinear?",
                "For points \(A, B, C\) with \(d(A, B) = {0}, d(B, C) = {1}, d(A, C) = {2}\), state whether they are collinear."
            ],
            'calc': lambda item: (
                "Collinear (points lie on a line)",
                ["Non-collinear", "Cannot be determined", "Forms a right triangle"],
                f"**Step 1: Compare distance sum with maximum distance**\nSum of two smaller distances: \({item[0]} + {item[1]} = {item[2]}\).\nLargest distance: \({item[2]}\).\nSince \({item[0]} + {item[1]} = {item[2]}\), the points are collinear.\n**Step 2: Conclusion**\nCollinear (points lie on a line)."
            ),
            'diff': 'easy'
        },
        # Arch 1: Test collinearity: sum of two smaller != largest (Non-collinear)
        {
            'data': [(4, 6, 11), (5, 7, 13), (6, 8, 15), (7, 9, 17), (8, 10, 19),
                     (5, 6, 12), (6, 7, 14), (7, 8, 16), (8, 9, 18), (9, 10, 20)],
            'tmpls': [
                "Determine whether points \(P, Q, R\) are collinear if \(d(P, Q) = {0}\), \(d(Q, R) = {1}\), and \(d(P, R) = {2}\).",
                "Given distances \(d(P, Q) = {0}, d(Q, R) = {1}, d(P, R) = {2}\), state if \(P, Q, R\) are collinear.",
                "Calculate whether points with distances {0}, {1}, and {2} lie on a single line.",
                "Are points \(P, Q, R\) collinear when \(d(P, Q) = {0}\), \(d(Q, R) = {1}\), and \(d(P, R) = {2}\)?",
                "Test collinearity for points \(P, Q, R\) having \(d(P, Q) = {0}, d(Q, R) = {1}, d(P, R) = {2}\).",
                "Check if points \(P, Q, R\) are collinear for distances {0}, {1}, and {2}.",
                "State if points \(P, Q, R\) are collinear given \(d(P, Q) = {0}, d(Q, R) = {1}, d(P, R) = {2}\).",
                "Evaluate collinearity of points \(P, Q, R\) having distances {0}, {1}, and {2}.",
                "If \(d(P, Q) = {0}, d(Q, R) = {1}\), and \(d(P, R) = {2}\), are points \(P, Q, R\) collinear?",
                "For points \(P, Q, R\) with \(d(P, Q) = {0}, d(Q, R) = {1}, d(P, R) = {2}\), state whether they are collinear."
            ],
            'calc': lambda item: (
                "Non-collinear (points do not lie on a line)",
                ["Collinear", "Coincident", "Collinear with P-Q-R"],
                f"**Step 1: Check collinearity condition**\nSum of two smaller distances: \({item[0]} + {item[1]} = {item[0] + item[1]}\).\nLargest distance: \({item[2]}\).\nSince \({item[0] + item[1]} \\ne {item[2]}\), the points are non-collinear.\n**Step 2: Conclusion**\nNon-collinear (points do not lie on a line)."
            ),
            'diff': 'easy'
        },
        # Arch 2: Figure formed by three non-collinear points
        {
            'data': [(3, 4, 6), (5, 6, 9), (7, 8, 12), (6, 7, 11), (4, 5, 8),
                     (8, 9, 14), (5, 7, 10), (6, 9, 13), (7, 10, 15), (8, 11, 17)],
            'tmpls': [
                "What geometric figure is formed by joining three non-collinear points on a plane?",
                "Three non-collinear points \(A, B, C\) are connected by line segments. What figure is formed?",
                "Name the polygon determined by three distinct non-collinear points.",
                "When three non-collinear points are joined pairwise, which shape results?",
                "Identify the figure formed by three points that do not lie on the same straight line.",
                "Which geometrical shape has three non-collinear points as its vertices?",
                "State the geometric figure enclosed by line segments joining three non-collinear points.",
                "What is the closed figure obtained by connecting three non-collinear points?",
                "Three points do not lie on a straight line. Joining them forms what shape?",
                "Determine the figure formed by three non-collinear vertices."
            ],
            'calc': lambda item: (
                "A triangle",
                ["A straight line", "A circle", "A quadrilateral"],
                f"**Step 1: Definition of triangle**\nA simple closed figure formed by joining three non-collinear points by line segments is a triangle.\n**Step 2: Conclusion**\nA triangle."
            ),
            'diff': 'easy'
        },
        # Arch 3: Number of lines determined by n collinear points
        {
            'data': [(3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
                     (8, 1), (9, 1), (10, 1), (12, 1), (15, 1)],
            'tmpls': [
                "How many distinct straight lines pass through {0} collinear points?",
                "What is the number of distinct lines that can contain {0} collinear points?",
                "How many lines are determined by {0} points that all lie on the same straight line?",
                "Determine the number of straight lines passing through {0} collinear points.",
                "State the number of lines passing through {0} collinear points on a plane.",
                "Find the number of straight lines determined by {0} collinear points.",
                "How many distinct lines contain all of {0} collinear points?",
                "Calculate the number of lines passing through {0} collinear points.",
                "If {0} points are collinear, how many distinct lines pass through all of them?",
                "For {0} collinear points, state the number of unique lines passing through them."
            ],
            'calc': lambda item: (
                "1",
                [f"{item[0]}", f"{item[0] * (item[0]-1) // 2}", "Infinite"],
                f"**Step 1: Collinear points property**\nBy definition, collinear points all lie on one and the same straight line. Hence, exactly 1 line passes through them.\n**Step 2: Conclusion**\n1."
            ),
            'diff': 'easy'
        },
        # Arch 4: Number of lines determined by 3 non-collinear points: 3 lines
        {
            'data': [(3, 3), (3, 3), (3, 3), (3, 3), (3, 3),
                     (3, 3), (3, 3), (3, 3), (3, 3), (3, 3)],
            'tmpls': [
                "How many distinct straight lines are determined by taking pairs from 3 non-collinear points?",
                "Through 3 non-collinear points, how many distinct lines can be drawn by connecting pairs of points?",
                "What is the maximum number of lines determined by 3 non-collinear points?",
                "Calculate the number of lines formed by joining 3 non-collinear points in pairs.",
                "Determine the number of distinct lines passing through pairs of 3 non-collinear points.",
                "Find the number of lines passing through pairs of 3 non-collinear points: \(C(3, 2)\).",
                "How many lines are determined by 3 non-collinear points on a plane?",
                "State the number of distinct lines connecting pairs among 3 non-collinear points.",
                "If three points are non-collinear, how many lines do they determine?",
                "For 3 non-collinear points, calculate the number of lines passing through two points at a time."
            ],
            'calc': lambda item: (
                "3 lines",
                ["1 line", "2 lines", "6 lines"],
                f"**Step 1: Combinations formula**\nNumber of lines determined by 3 non-collinear points = \(\binom{{3}}{{2}} = \frac{{3 \times 2}}{{2}} = 3\).\n**Step 2: Conclusion**\n3 lines."
            ),
            'diff': 'easy'
        },
        # Arch 5: Third distance required for collinearity: d(A, C) = d(A, B) + d(B, C)
        {
            'data': [(6, 11, 17), (7, 12, 19), (8, 13, 21), (9, 14, 23), (10, 16, 26),
                     (11, 17, 28), (12, 18, 30), (13, 19, 32), (14, 21, 35), (15, 22, 37)],
            'tmpls': [
                "If points \(A, B, C\) are collinear in order \(A-B-C\) with \(d(A, B) = {0}\) and \(d(B, C) = {1}\), what must be \(d(A, C)\)?",
                "For points \(A, B, C\) to be collinear in order \(A-B-C\) with \(d(A, B) = {0}\) and \(d(B, C) = {1}\), calculate \(d(A, C)\).",
                "Calculate required distance \(d(A, C)\) for collinearity \(A-B-C\) given \(d(A, B) = {0}\) and \(d(B, C) = {1}\).",
                "What value of \(d(A, C)\) makes \(A, B, C\) collinear in order \(A-B-C\) when \(d(A, B) = {0}\) and \(d(B, C) = {1}\)?",
                "Determine \(d(A, C)\) so that \(A-B-C\) holds with \(d(A, B) = {0}\) and \(d(B, C) = {1}\).",
                "Find \(d(A, C) = {0} + {1}\) for betweenness \(A-B-C\).",
                "Compute the required length \(d(A, C)\) for collinear points with \(d(A, B) = {0}\) and \(d(B, C) = {1}\).",
                "Evaluate \(d(A, C)\) for collinear points \(A, B, C\) with \(A-B-C\) having distances {0} and {1}.",
                "If \(d(A, B) = {0}\) and \(d(B, C) = {1}\), find \(d(A, C)\) such that \(A, B, C\) are collinear.",
                "For collinear points \(A-B-C\), calculate \(d(A, C)\) when \(d(A, B) = {0}\) and \(d(B, C) = {1}\)."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 2}", f"{item[2] - 2 if item[2] > 2 else item[2] + 4}", f"{item[1] - item[0]}"],
                f"**Step 1: Formula**\n\(d(A, C) = d(A, B) + d(B, C) = {item[0]} + {item[1]} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(0, item[2], "A", "C"),
            'diff': 'easy'
        },
        # Arch 6: Triangle inequality check: sum of two sides > third side
        {
            'data': [(6, 8, 10, "Yes"), (7, 10, 15, "Yes"), (5, 12, 13, "Yes"), (8, 15, 17, "Yes"), (9, 12, 15, "Yes"),
                     (3, 4, 8, "No"), (4, 5, 10, "No"), (5, 6, 12, "No"), (6, 7, 14, "No"), (7, 8, 16, "No")],
            'tmpls': [
                "Can a triangle be formed with side lengths {0}\text{{ cm}}, {1}\text{{ cm}}, and {2}\text{{ cm}}?",
                "Determine whether lengths {0}\text{{ cm}}, {1}\text{{ cm}}, and {2}\text{{ cm}} can form the sides of a triangle.",
                "Check if lengths {0}, {1}, and {2} satisfy the triangle inequality.",
                "Is it possible to draw a triangle with sides {0}\text{{ cm}}, {1}\text{{ cm}}, and {2}\text{{ cm}}?",
                "State whether three line segments of lengths {0}, {1}, and {2} can form a triangle.",
                "Test if sides {0}\text{{ cm}}, {1}\text{{ cm}}, {2}\text{{ cm}} form a triangle.",
                "Can three line segments of lengths {0}, {1}, and {2} form a closed triangle?",
                "Evaluate whether a triangle can be constructed with sides {0}\text{{ cm}}, {1}\text{{ cm}}, and {2}\text{{ cm}}.",
                "If side lengths are {0}, {1}, and {2}, can a triangle exist?",
                "For lengths {0}\text{{ cm}}, {1}\text{{ cm}}, and {2}\text{{ cm}}, state if they form a triangle."
            ],
            'calc': lambda item: (
                f"{item[3]}, sum of any two sides {'>' if item[3] == 'Yes' else '<='} third side",
                [f"{'No' if item[3] == 'Yes' else 'Yes'}", "Only for right triangles", "Cannot be determined"],
                f"**Step 1: Check triangle inequality**\nSmallest two sides: {item[0]} + {item[1]} = {item[0] + item[1]}.\nThird side: {item[2]}.\nSince {item[0] + item[1]} {'>' if item[3] == 'Yes' else '<='} {item[2]}, a triangle {'can' if item[3] == 'Yes' else 'cannot'} be formed.\n**Step 2: Conclusion**\n{item[3]}, sum of any two sides {'>' if item[3] == 'Yes' else '<='} third side."
            ),
            'diff': 'medium'
        },
        # Arch 7: Minimum distance between endpoints given middle point
        {
            'data': [(7, 4, 11), (9, 5, 14), (11, 6, 17), (13, 7, 20), (15, 8, 23),
                     (17, 9, 26), (19, 10, 29), (21, 11, 32), (23, 12, 35), (25, 13, 38)],
            'tmpls': [
                "Points \(A, B, C\) are collinear with \(A-B-C\). If \(d(A, B) = {0}\) and \(d(B, C) = {1}\), find \(d(A, C)\).",
                "Given \(A-B-C\) where \(AB = {0}\) and \(BC = {1}\), calculate length of segment \(AC\).",
                "Calculate \(AC\) in betweenness \(A-B-C\) with \(AB = {0}\) and \(BC = {1}\).",
                "What is the length of \(AC\) if \(A-B-C\), \(AB = {0}\), and \(BC = {1}\)?",
                "Determine \(AC\) given \(A-B-C\) with \(AB = {0}\) and \(BC = {1}\).",
                "Find \(AC = AB + BC\) for \(AB = {0}\) and \(BC = {1}\).",
                "Compute \(AC\) for collinear points in order \(A-B-C\) with \(AB = {0}\) and \(BC = {1}\).",
                "Evaluate segment \(AC\) when \(AB = {0}\) and \(BC = {1}\).",
                "If \(A-B-C\) with \(AB = {0}\) and \(BC = {1}\), find \(AC\).",
                "For collinear points \(A, B, C\) with \(A-B-C\), calculate \(AC\) when \(AB = {0}\) and \(BC = {1}\)."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 2}", f"{item[2] - 2 if item[2] > 2 else item[2] + 4}", f"{item[0] - item[1]}"],
                f"**Step 1: Formula**\n\(AC = AB + BC = {item[0]} + {item[1]} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(0, item[2], "A", "C"),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# 1.3.1: Segment definition and length
def gen_1_3_1():
    tc = "MH-9-MTH2-1-1.3.1"
    tname = "Segment definition and length"
    archs = [
        # Arch 0: Congruent segments: AB = CD => length equality
        {
            'data': [(5, 5), (7, 7), (8, 8), (11, 11), (13, 13),
                     (14, 14), (16, 16), (17, 17), (19, 19), (22, 22)],
            'tmpls': [
                "If segment \(AB \cong CD\) and \(l(AB) = {0}\text{{ cm}}\), what is \(l(CD)\)?",
                "Given congruent segments \(AB\) and \(CD\) with \(AB = {0}\text{{ cm}}\), calculate \(CD\).",
                "Calculate length of segment \(CD\) if \(AB \cong CD\) and \(l(AB) = {0}\text{{ cm}}\).",
                "What is \(l(CD)\) if \(AB \cong CD\) and length of \(AB\) is {0}\text{{ cm}}?",
                "Determine \(l(CD)\) given that segment \(AB\) is congruent to segment \(CD\) and \(l(AB) = {0}\text{{ cm}}\).",
                "Find \(l(CD)\) when \(AB \cong CD\) and \(l(AB) = {0}\text{{ cm}}\).",
                "Compute length of \(CD\) for congruent segments with \(l(AB) = {0}\text{{ cm}}\).",
                "Evaluate \(l(CD)\) given \(AB \cong CD\) and \(l(AB) = {0}\text{{ cm}}\).",
                "If \(AB \cong CD\) and \(l(AB) = {0}\text{{ cm}}\), find \(l(CD)\).",
                "For congruent segments \(AB \cong CD\), if \(l(AB) = {0}\text{{ cm}}\), calculate \(l(CD)\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 2} cm", f"{item[1] - 2 if item[1] > 2 else item[1] + 4} cm", f"{item[1] * 2} cm"],
                f"**Step 1: Congruent segments property**\nIf two segments are congruent, their lengths are equal: \(AB \cong CD \implies l(CD) = l(AB) = {item[0]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_segment_midpoint("A", "M", "B"),
            'diff': 'easy'
        },
        # Arch 1: Algebraic congruent segments: 2x + a = x + b => x = b - a
        {
            'data': [(2, 3, 1, 8, 5, 13), (2, 4, 1, 10, 6, 16), (2, 5, 1, 12, 7, 19), (2, 6, 1, 14, 8, 22), (2, 7, 1, 16, 9, 25),
                     (2, 8, 1, 18, 10, 28), (2, 9, 1, 20, 11, 31), (2, 10, 1, 22, 12, 34), (2, 11, 1, 24, 13, 37), (2, 12, 1, 26, 14, 40)],
            'tmpls': [
                "If segment \(AB \cong CD\) with \(l(AB) = {0}x + {1}\) and \(l(CD) = x + {3}\), find \(x\).",
                "Congruent segments have \(l(AB) = {0}x + {1}\) and \(l(CD) = x + {3}\). Calculate \(x\).",
                "Calculate \(x\) given that \(AB \cong CD\), \(l(AB) = {0}x + {1}\), and \(l(CD) = x + {3}\).",
                "What is the value of \(x\) if \(AB \cong CD\) with lengths \({0}x + {1}\) and \(x + {3}\)?",
                "Determine \(x\) for congruent segments \(AB\) and \(CD\) with \(l(AB) = {0}x + {1}\) and \(l(CD) = x + {3}\).",
                "Find \(x\) when \(l(AB) = {0}x + {1}\) equals \(l(CD) = x + {3}\).",
                "Compute \(x\) such that \(AB \cong CD\) with \(l(AB) = {0}x + {1}\) and \(l(CD) = x + {3}\).",
                "Evaluate \(x\) for congruent segments with \(l(AB) = {0}x + {1}\) and \(l(CD) = x + {3}\).",
                "If \(AB \cong CD\), \(l(AB) = {0}x + {1}\), and \(l(CD) = x + {3}\), find \(x\).",
                "For congruent segments \(AB \cong CD\), find \(x\) given \(l(AB) = {0}x + {1}\) and \(l(CD) = x + {3}\)."
            ],
            'calc': lambda item: (
                f"{item[4]}",
                [f"{item[4] + 2}", f"{item[4] - 2 if item[4] > 2 else item[4] + 4}", f"{item[5]}"],
                f"**Step 1: Equating lengths of congruent segments**\n\(l(AB) = l(CD) \implies {item[0]}x + {item[1]} = x + {item[3]} \implies x = {item[3]} - {item[1]} = {item[4]}\).\n**Step 2: Conclusion**\n{item[4]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Properties of congruence: Reflexivity, Symmetry, Transitivity
        {
            'data': [(1, "Reflexivity"), (2, "Symmetry"), (3, "Transitivity"), (4, "Reflexivity"), (5, "Symmetry"),
                     (6, "Transitivity"), (7, "Reflexivity"), (8, "Symmetry"), (9, "Transitivity"), (10, "Reflexivity")],
            'tmpls': [
                "Which property of congruence of segments is expressed by: 'Every segment is congruent to itself: \(AB \cong AB\)'?",
                "Name the property: \(AB \cong AB\) for every segment \(AB\).",
                "What property is represented by \(AB \cong AB\)?",
                "Identify the property: 'A segment is congruent to itself'.",
                "State the name of the congruence property: \(AB \cong AB\).",
                "The statement \(AB \cong AB\) illustrates which property of congruence?",
                "Which congruence property states that every segment is congruent to itself?",
                "Evaluate the property described by \(AB \cong AB\).",
                "Name the geometric property: \(AB \cong AB\).",
                "For any line segment \(AB\), \(AB \cong AB\). Name this property."
            ],
            'calc': lambda item: (
                "Reflexivity",
                ["Symmetry", "Transitivity", "Commutativity"],
                f"**Step 1: Definition of reflexivity**\nThe property that every geometric entity is congruent to itself (\(AB \cong AB\)) is called Reflexivity.\n**Step 2: Conclusion**\nReflexivity."
            ),
            'diff': 'easy'
        },
        # Arch 3: Comparison of segments: if l(AB) > l(CD), then AB > CD
        {
            'data': [(8, 5, "AB > CD"), (10, 7, "AB > CD"), (12, 9, "AB > CD"), (14, 11, "AB > CD"), (16, 13, "AB > CD"),
                     (4, 9, "AB < CD"), (6, 11, "AB < CD"), (7, 13, "AB < CD"), (8, 15, "AB < CD"), (9, 17, "AB < CD")],
            'tmpls': [
                "If \(l(AB) = {0}\text{{ cm}}\) and \(l(CD) = {1}\text{{ cm}}\), compare segments \(AB\) and \(CD\).",
                "Compare segments \(AB\) and \(CD\) given \(l(AB) = {0}\text{{ cm}}\) and \(l(CD) = {1}\text{{ cm}}\).",
                "What is the comparison relation between \(AB = {0}\text{{ cm}}\) and \(CD = {1}\text{{ cm}}\)?",
                "Determine the comparison of segments \(AB\) and \(CD\) having lengths {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "Compare the lengths of segment \(AB = {0}\text{{ cm}}\) and segment \(CD = {1}\text{{ cm}}\).",
                "State the relationship between segments \(AB\) and \(CD\) if \(l(AB) = {0}\text{{ cm}}\) and \(l(CD) = {1}\text{{ cm}}\).",
                "Find the comparison between \(AB = {0}\text{{ cm}}\) and \(CD = {1}\text{{ cm}}\).",
                "Evaluate the relation between segments \(AB\) and \(CD\) with lengths {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "If \(l(AB) = {0}\text{{ cm}}\) and \(l(CD) = {1}\text{{ cm}}\), write the comparison statement.",
                "For segments \(AB\) and \(CD\) measuring {0}\text{{ cm}} and {1}\text{{ cm}}, compare them."
            ],
            'calc': lambda item: (
                f"seg {item[2]}",
                [f"seg {item[2].replace('>', '<') if '>' in item[2] else item[2].replace('<', '>')}", "seg AB cong seg CD", "Cannot compare"],
                f"**Step 1: Compare lengths**\n\(l(AB) = {item[0]}\text{{ cm}}\) and \(l(CD) = {item[1]}\text{{ cm}}\).\nSince {item[0]} {'>' if item[0] > item[1] else '<'} {item[1]}, seg {item[2]}.\n**Step 2: Conclusion**\nseg {item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 4: Segment definition: set of point A, point B and all points between A and B
        {
            'data': [(1, "A and B and points between them"), (2, "A and B and points between them"), (3, "A and B and points between them"),
                     (4, "A and B and points between them"), (5, "A and B and points between them"), (6, "A and B and points between them"),
                     (7, "A and B and points between them"), (8, "A and B and points between them"), (9, "A and B and points between them"),
                     (10, "A and B and points between them")],
            'tmpls': [
                "What is the mathematical definition of segment \(AB\)?",
                "The union of point \(A\), point \(B\), and all points between \(A\) and \(B\) is called what?",
                "Define line segment \(AB\) in terms of set of points.",
                "Which set of points constitutes line segment \(AB\)?",
                "State the geometric definition of segment \(AB\).",
                "Segment \(AB\) is defined as the union set of points \(A, B\) and which other points?",
                "What set of points forms the line segment joining \(A\) and \(B\)?",
                "How is line segment \(AB\) defined geometrically?",
                "The collection of points \(A\), \(B\), and all points lying between \(A\) and \(B\) is called what?",
                "State the formal set definition of line segment \(AB\)."
            ],
            'calc': lambda item: (
                "Union of points A, B, and all points between A and B",
                ["Union of ray AB and ray BA", "Set of all points collinear with A and B extending indefinitely", "The midpoint of A and B"],
                f"**Step 1: Formal definition of line segment**\nThe union of point A, point B, and all points between A and B is called the line segment AB, denoted as seg AB.\n**Step 2: Conclusion**\nUnion of points A, B, and all points between A and B."
            ),
            'svg': lambda item: svg_segment_midpoint("A", "P", "B"),
            'diff': 'easy'
        },
        # Arch 5: Symmetry property: If AB \cong CD, then CD \cong AB
        {
            'data': [(1, "Symmetry"), (2, "Symmetry"), (3, "Symmetry"), (4, "Symmetry"), (5, "Symmetry"),
                     (6, "Symmetry"), (7, "Symmetry"), (8, "Symmetry"), (9, "Symmetry"), (10, "Symmetry")],
            'tmpls': [
                "If segment \(AB \cong CD\), then segment \(CD \cong AB\). Which property of congruence is this?",
                "Name the property: 'If \(AB \cong CD\), then \(CD \cong AB\)'.",
                "What property of congruence is illustrated by: \(AB \cong CD \implies CD \cong AB\)?",
                "Identify the property: If a first segment is congruent to a second, the second is congruent to the first.",
                "State the name of the congruence property: \(AB \cong CD \implies CD \cong AB\).",
                "The statement 'If \(AB \cong CD\), then \(CD \cong AB\)' represents which property?",
                "Which congruence property allows swapping the order: \(AB \cong CD \implies CD \cong AB\)?",
                "Evaluate the property described by \(AB \cong CD \implies CD \cong AB\).",
                "Name the geometric property: \(AB \cong CD \implies CD \cong AB\).",
                "If \(AB \cong CD \implies CD \cong AB\), name this fundamental property of congruence."
            ],
            'calc': lambda item: (
                "Symmetry",
                ["Reflexivity", "Transitivity", "Associativity"],
                f"**Step 1: Definition of symmetry**\nThe property that if a first geometric figure is congruent to a second, then the second is congruent to the first is called Symmetry.\n**Step 2: Conclusion**\nSymmetry."
            ),
            'diff': 'easy'
        },
        # Arch 6: Transitivity property: If AB \cong CD and CD \cong EF, then AB \cong EF
        {
            'data': [(1, "Transitivity"), (2, "Transitivity"), (3, "Transitivity"), (4, "Transitivity"), (5, "Transitivity"),
                     (6, "Transitivity"), (7, "Transitivity"), (8, "Transitivity"), (9, "Transitivity"), (10, "Transitivity")],
            'tmpls': [
                "If \(AB \cong CD\) and \(CD \cong EF\), then \(AB \cong EF\). Name this property of congruence.",
                "Which property states that if \(AB \cong CD\) and \(CD \cong EF\), then \(AB \cong EF\)?",
                "What property of congruence is illustrated by: \(AB \cong CD \text{{ and }} CD \cong EF \implies AB \cong EF\)?",
                "Identify the property: Segments congruent to the same segment are congruent to each other.",
                "State the name of the congruence property: \(AB \cong CD \text{{ and }} CD \cong EF \implies AB \cong EF\).",
                "The statement 'If \(AB \cong CD\) and \(CD \cong EF\), then \(AB \cong EF\)' represents which property?",
                "Which congruence property allows chaining: \(AB \cong CD \cong EF \implies AB \cong EF\)?",
                "Evaluate the property described by \(AB \cong CD \text{{ and }} CD \cong EF \implies AB \cong EF\).",
                "Name the geometric property: \(AB \cong CD\) and \(CD \cong EF \implies AB \cong EF\).",
                "If two segments are each congruent to a third segment, they are congruent to each other. Name this property."
            ],
            'calc': lambda item: (
                "Transitivity",
                ["Reflexivity", "Symmetry", "Distributivity"],
                f"**Step 1: Definition of transitivity**\nThe property that if a first segment is congruent to a second, and the second is congruent to a third, then the first is congruent to the third is Transitivity.\n**Step 2: Conclusion**\nTransitivity."
            ),
            'diff': 'easy'
        },
        # Arch 7: Difference of lengths of segments: l(AB) - l(CD)
        {
            'data': [(12, 5, 7), (14, 6, 8), (15, 6, 9), (17, 7, 10), (19, 8, 11),
                     (21, 8, 13), (23, 9, 14), (25, 9, 16), (28, 10, 18), (30, 11, 19)],
            'tmpls': [
                "If \(l(AB) = {0}\text{{ cm}}\) and \(l(CD) = {1}\text{{ cm}}\), by how much is segment \(AB\) longer than segment \(CD\)?",
                "Calculate the difference in lengths between segment \(AB = {0}\text{{ cm}}\) and segment \(CD = {1}\text{{ cm}}\).",
                "Find \(l(AB) - l(CD)\) given \(l(AB) = {0}\text{{ cm}}\) and \(l(CD) = {1}\text{{ cm}}\).",
                "What is the difference between lengths of segments \(AB = {0}\text{{ cm}}\) and \(CD = {1}\text{{ cm}}\)?",
                "Determine \(l(AB) - l(CD)\) where \(l(AB) = {0}\text{{ cm}}\) and \(l(CD) = {1}\text{{ cm}}\).",
                "How much longer is segment \(AB = {0}\text{{ cm}}\) compared to segment \(CD = {1}\text{{ cm}}\)?",
                "Compute the length difference between segments measuring {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "Evaluate \(l(AB) - l(CD)\) for segments of lengths {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "If \(l(AB) = {0}\text{{ cm}}\) and \(l(CD) = {1}\text{{ cm}}\), find the difference in their lengths.",
                "For segments measuring {0}\text{{ cm}} and {1}\text{{ cm}}, calculate how much longer the first is."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{item[2] + 2} cm", f"{item[2] - 2 if item[2] > 2 else item[2] + 4} cm", f"{item[0] + item[1]} cm"],
                f"**Step 1: Difference calculation**\nDifference = \(l(AB) - l(CD) = {item[0]} - {item[1]} = {item[2]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[2]} cm."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

print("gen_1_2_2 and gen_1_3_1 defined.")

# 1.3.2: Opposite rays
def gen_1_3_2():
    tc = "MH-9-MTH2-1-1.3.2"
    tname = "Opposite rays"
    archs = [
        # Arch 0: Opposite ray definition: common endpoint and form a straight line
        {
            'data': [(1, "Opposite rays"), (2, "Opposite rays"), (3, "Opposite rays"), (4, "Opposite rays"), (5, "Opposite rays"),
                     (6, "Opposite rays"), (7, "Opposite rays"), (8, "Opposite rays"), (9, "Opposite rays"), (10, "Opposite rays")],
            'tmpls': [
                "Two rays having a common origin and whose union is a straight line are called what?",
                "What name is given to two rays having the same origin and lying on the same straight line extending in opposite directions?",
                "Ray \(BA\) and ray \(BC\) have common origin \(B\) and form a line \(AC\). These rays are called what?",
                "Identify the geometric term for two rays having a common origin that form a single straight line.",
                "State the name of rays that have a common endpoint and together form a line.",
                "Two rays with a common initial point forming a 180° angle are called what?",
                "What is the term for rays extending in opposite directions from a single common point along a line?",
                "If rays \(OA\) and \(OB\) share origin \(O\) and points \(A, O, B\) are collinear with \(A-O-B\), what are these rays called?",
                "Rays sharing origin \(O\) and forming a straight line are called what?",
                "Define the relation between ray \(OA\) and ray \(OB\) when \(A-O-B\)."
            ],
            'calc': lambda item: (
                "Opposite rays",
                ["Parallel rays", "Coincident rays", "Perpendicular rays"],
                f"**Step 1: Definition of opposite rays**\nTwo rays which have a common origin and whose union is a straight line are called opposite rays.\n**Step 2: Conclusion**\nOpposite rays."
            ),
            'diff': 'easy'
        },
        # Arch 1: Angle between opposite rays: 180° (straight angle)
        {
            'data': [(180, 180), (180, 180), (180, 180), (180, 180), (180, 180),
                     (180, 180), (180, 180), (180, 180), (180, 180), (180, 180)],
            'tmpls': [
                "What is the degree measure of the angle formed by two opposite rays?",
                "Calculate the angle formed by ray \(BA\) and ray \(BC\) if they are opposite rays.",
                "What is the measure of the straight angle formed by two opposite rays?",
                "Determine the angle in degrees between two opposite rays having common origin \(O\).",
                "Find the angle between opposite rays on a straight line.",
                "Compute the measure of the angle between ray \(OA\) and ray \(OB\) when they are opposite rays.",
                "Evaluate the angle formed by two opposite rays sharing an origin.",
                "How many degrees are in the angle formed by two opposite rays?",
                "If ray \(BA\) and ray \(BC\) are opposite rays, find \(\angle ABC\).",
                "For opposite rays \(OA\) and \(OB\), what is the measure of \(\angle AOB\)?"
            ],
            'calc': lambda item: (
                "180°",
                ["90°", "360°", "0°"],
                f"**Step 1: Straight angle definition**\nOpposite rays lie on the same straight line, so the angle between them is a straight angle: 180°.\n**Step 2: Conclusion**\n180°."
            ),
            'diff': 'easy'
        },
        # Arch 2: Origin of ray: Ray AB has origin A
        {
            'data': [("A", "B", "A"), ("P", "Q", "P"), ("M", "N", "M"), ("X", "Y", "X"), ("C", "D", "C"),
                     ("E", "F", "E"), ("R", "S", "R"), ("K", "L", "K"), ("U", "V", "U"), ("G", "H", "G")],
            'tmpls': [
                "What is the origin (starting point) of ray \({0}{1}\)?",
                "For ray \({0}{1}\), state its endpoint (origin).",
                "Name the origin of ray \({0}{1}\).",
                "Identify the starting point of ray \({0}{1}\).",
                "Which point is the origin of ray \({0}{1}\)?",
                "State the initial point of ray \({0}{1}\).",
                "Where does ray \({0}{1}\) start?",
                "Evaluate the origin of ray \({0}{1}\).",
                "In ray \({0}{1}\), which vertex represents the origin?",
                "For the ray denoted as \({0}{1}\), identify its origin."
            ],
            'calc': lambda item: (
                f"Point {item[2]}",
                [f"Point {item[1]}", "Both points", "Neither point"],
                f"**Step 1: Ray notation convention**\nA ray is named starting with its origin followed by another point on the ray. In ray {item[0]}{item[1]}, point {item[2]} is the origin.\n**Step 2: Conclusion**\nPoint {item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 3: Intersection of two opposite rays: single origin point
        {
            'data': [("O", "{O}"), ("B", "{B}"), ("P", "{P}"), ("M", "{M}"), ("A", "{A}"),
                     ("Q", "{Q}"), ("C", "{C}"), ("N", "{N}"), ("X", "{X}"), ("K", "{K}")],
            'tmpls': [
                "What is the intersection of two opposite rays ray \({0}A\) and ray \({0}B\)?",
                "Find the common set of points between opposite rays \({0}A\) and \({0}B\).",
                "What is the intersection set \(\text{{ray }} {0}A \cap \text{{ray }} {0}B\)?",
                "Determine the intersection of opposite rays \({0}P\) and \({0}Q\).",
                "Name the point of intersection of two opposite rays with origin \({0}\).",
                "Compute \(\text{{ray }} {0}X \cap \text{{ray }} {0}Y\) where the rays are opposite.",
                "Evaluate the intersection of two opposite rays sharing origin \({0}\).",
                "What is the intersection of opposite rays having common endpoint \({0}\)?",
                "If ray \({0}A\) and ray \({0}B\) are opposite rays, find their intersection.",
                "For opposite rays with origin \({0}\), state their point of intersection."
            ],
            'calc': lambda item: (
                f"Single point {item[0]}",
                ["A line segment", "Empty set (no points)", "A straight line"],
                f"**Step 1: Set intersection of opposite rays**\nOpposite rays share only their starting point: \(\text{{ray }} {item[0]}A \cap \text{{ray }} {item[0]}B = \\{{{item[0]}\\}}\).\n**Step 2: Conclusion**\nSingle point {item[0]}."
            ),
            'diff': 'easy'
        },
        # Arch 4: Union of two opposite rays: a straight line
        {
            'data': [("AB", "line AB"), ("PQ", "line PQ"), ("MN", "line MN"), ("XY", "line XY"), ("CD", "line CD"),
                     ("EF", "line EF"), ("RS", "line RS"), ("KL", "line KL"), ("UV", "line UV"), ("GH", "line GH")],
            'tmpls': [
                "What is the union of two opposite rays having a common origin?",
                "The union of opposite rays ray \(OA\) and ray \(OB\) forms which geometric entity?",
                "What geometric figure is obtained from \(\text{{ray }} OA \cup \text{{ray }} OB\) for opposite rays?",
                "Determine the union set of two opposite rays.",
                "Find the union of two rays extending in opposite directions from a common point.",
                "Compute \(\text{{ray }} OA \cup \text{{ray }} OB\) where \(A-O-B\).",
                "Evaluate the union of two opposite rays on a plane.",
                "What is formed by the union of two opposite rays?",
                "If ray \(OA\) and ray \(OB\) are opposite rays, their union is what?",
                "For opposite rays with common origin \(O\), state their union."
            ],
            'calc': lambda item: (
                "A straight line",
                ["A line segment", "An angle of 90°", "A ray"],
                f"**Step 1: Union of opposite rays**\nBy definition, the union of two opposite rays forms a complete straight line extending infinitely in both directions.\n**Step 2: Conclusion**\nA straight line."
            ),
            'diff': 'easy'
        },
        # Arch 5: Points on opposite ray
        {
            'data': [("B", "A", "C", "ray BC"), ("O", "P", "Q", "ray OQ"), ("M", "L", "N", "ray MN"), ("K", "J", "L", "ray KL"), ("Y", "X", "Z", "ray YZ"),
                     ("D", "C", "E", "ray DE"), ("F", "E", "G", "ray FG"), ("S", "R", "T", "ray ST"), ("H", "G", "I", "ray HI"), ("W", "V", "X", "ray WX")],
            'tmpls': [
                "If \(A-{0}-{2}\), name the ray opposite to ray \({0}{1}\).",
                "Points \({1}, {0}, {2}\) are collinear with \({1}-{0}-{2}\). What is the ray opposite to ray \({0}{1}\)?",
                "Name the ray opposite to ray \({0}{1}\) when \({1}-{0}-{2}\).",
                "What is the opposite ray of ray \({0}{1}\) in collinear points \({1}-{0}-{2}\)?",
                "Determine the ray opposite to ray \({0}{1}\) given \({1}-{0}-{2}\).",
                "Identify the ray opposite to ray \({0}{1}\) where point \({0}\) lies between \({1}\) and \({2}\).",
                "Find the opposite ray of ray \({0}{1}\) on line \({1}{2}\).",
                "State the ray opposite to ray \({0}{1}\) given betweenness \({1}-{0}-{2}\).",
                "If \({1}-{0}-{2}\), which ray is opposite to ray \({0}{1}\)?",
                "For collinear points \({1}-{0}-{2}\), state the ray opposite to ray \({0}{1}\)."
            ],
            'calc': lambda item: (
                f"{item[3]}",
                [f"ray {item[0]}{item[1]}", f"ray {item[1]}{item[0]}", f"ray {item[2]}{item[0]}"],
                f"**Step 1: Opposite ray with common origin**\nThe origin must be point {item[0]}. Since {item[1]}-{item[0]}-{item[2]}, the ray extending in the opposite direction from {item[0]} through {item[2]} is {item[3]}.\n**Step 2: Conclusion**\n{item[3]}."
            ),
            'diff': 'easy'
        },
        # Arch 6: Subsets of a line: segment is subset of ray, ray is subset of line
        {
            'data': [(1, "seg AB subset ray AB"), (2, "seg AB subset ray AB"), (3, "seg AB subset ray AB"), (4, "seg AB subset ray AB"), (5, "seg AB subset ray AB"),
                     (6, "seg AB subset ray AB"), (7, "seg AB subset ray AB"), (8, "seg AB subset ray AB"), (9, "seg AB subset ray AB"), (10, "seg AB subset ray AB")],
            'tmpls': [
                "Which of the following is true regarding the relationship between segment \(AB\) and ray \(AB\)?",
                "State the correct subset relationship between segment \(AB\) and ray \(AB\).",
                "Is segment \(AB\) a subset of ray \(AB\)?",
                "What is the relation between the set of points of seg \(AB\) and ray \(AB\)?",
                "Determine which set of points contains the other: seg \(AB\) or ray \(AB\).",
                "Compare the point sets of segment \(AB\) and ray \(AB\).",
                "Identify the correct statement relating seg \(AB\) and ray \(AB\).",
                "True or False: Line segment \(AB\) is a proper subset of ray \(AB\).",
                "What is the set-theoretic relationship between seg \(AB\) and ray \(AB\)?",
                "For points \(A\) and \(B\), what is the relationship between seg \(AB\) and ray \(AB\)?"
            ],
            'calc': lambda item: (
                "seg AB is a subset of ray AB",
                ["ray AB is a subset of seg AB", "seg AB and ray AB are equal sets", "seg AB and ray AB are disjoint"],
                f"**Step 1: Point set comparison**\nEvery point of line segment AB is also a point of ray AB, and ray AB extends indefinitely beyond B. Thus, seg AB is a proper subset of ray AB: \(\text{{seg }} AB \subset \text{{ray }} AB\).\n**Step 2: Conclusion**\nseg AB is a subset of ray AB."
            ),
            'diff': 'easy'
        },
        # Arch 7: Angle on straight line formed by a common ray on opposite rays: linear pair sum = 180°
        {
            'data': [(40, 140), (50, 130), (60, 120), (70, 110), (80, 100),
                     (45, 135), (55, 125), (65, 115), (75, 105), (85, 95)],
            'tmpls': [
                "Ray \(OA\) and ray \(OB\) are opposite rays. Ray \(OC\) is any other ray. If \(\angle AOC = {0}^\circ\), find \(\angle BOC\).",
                "Opposite rays \(OA\) and \(OB\) form a straight line. If \(\angle AOC = {0}^\circ\), calculate \(\angle BOC\).",
                "Calculate \(\angle BOC\) in linear pair with \(\angle AOC = {0}^\circ\) on opposite rays \(OA\) and \(OB\).",
                "What is the measure of \(\angle BOC\) if \(OA\) and \(OB\) are opposite rays and \(\angle AOC = {0}^\circ\)?",
                "Determine \(\angle BOC\) given \(\angle AOC = {0}^\circ\) on straight line \(AB\).",
                "Find linear pair angle \(\angle BOC = 180^\circ - \angle AOC\) for \(\angle AOC = {0}^\circ\).",
                "Compute \(\angle BOC\) where \(A-O-B\) and \(\angle AOC = {0}^\circ\).",
                "Evaluate \(\angle BOC\) in straight line configuration with \(\angle AOC = {0}^\circ\).",
                "If rays \(OA\) and \(OB\) are opposite and \(\angle AOC = {0}^\circ\), find \(\angle BOC\).",
                "For straight line \(AB\) with ray \(OC\), if \(\angle AOC = {0}^\circ\), calculate \(\angle BOC\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 10}^\circ", f"{item[1] - 10 if item[1] > 10 else item[1] + 20}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Linear pair theorem**\nSince rays \(OA\) and \(OB\) are opposite, \(\angle AOC + \angle BOC = 180^\circ\).\n\(\angle BOC = 180^\circ - {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# 1.3.3: Midpoint: AM = MB = 1/2 AB
def gen_1_3_3():
    tc = "MH-9-MTH2-1-1.3.3"
    tname = "Midpoint: AM = MB = 1/2 AB"
    archs = [
        # Arch 0: Given AB, find AM = AB / 2
        {
            'data': [(8, 4), (10, 5), (12, 6), (14, 7), (16, 8),
                     (18, 9), (20, 10), (22, 11), (24, 12), (26, 13)],
            'tmpls': [
                "Point \(M\) is the midpoint of segment \(AB\). If \(l(AB) = {0}\text{{ cm}}\), find \(l(AM)\).",
                "Calculate length of \(AM\) if \(M\) is the midpoint of segment \(AB = {0}\text{{ cm}}\).",
                "What is \(l(AM)\) in segment \(AB\) of length {0}\text{{ cm}} with midpoint \(M\)?",
                "Determine \(l(AM)\) given that \(M\) bisects segment \(AB = {0}\text{{ cm}}\).",
                "Find \(AM = \frac{{AB}}{{2}}\) for segment length {0}\text{{ cm}}.",
                "Compute the length of \(AM\) where \(M\) is the midpoint of segment \(AB = {0}\text{{ cm}}\).",
                "Evaluate \(l(AM)\) in segment \(AB = {0}\text{{ cm}}\) with center point \(M\).",
                "If \(M\) is the midpoint of segment \(AB\) and \(l(AB) = {0}\text{{ cm}}\), find \(l(AM)\).",
                "For segment \(AB\) measuring {0}\text{{ cm}} with midpoint \(M\), calculate \(l(AM)\).",
                "Segment \(AB\) has length {0}\text{{ cm}} and midpoint \(M\). Determine \(l(AM)\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 2} cm", f"{item[1] - 2 if item[1] > 2 else item[1] + 4} cm", f"{item[0]} cm"],
                f"**Step 1: Midpoint formula**\n\(AM = \frac{{AB}}{{2}} = \frac{{{item[0]}}}{{2}} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_segment_midpoint("A", "M", "B"),
            'diff': 'easy'
        },
        # Arch 1: Given AM, find AB = 2*AM
        {
            'data': [(3.5, 7.0), (4.5, 9.0), (5.5, 11.0), (6.5, 13.0), (7.5, 15.0),
                     (8.5, 17.0), (9.5, 19.0), (10.5, 21.0), (11.5, 23.0), (12.5, 25.0)],
            'tmpls': [
                "Point \(M\) is the midpoint of segment \(AB\). If \(l(AM) = {0}\text{{ cm}}\), find \(l(AB)\).",
                "Calculate the total length of segment \(AB\) given midpoint \(M\) and \(AM = {0}\text{{ cm}}\).",
                "What is \(l(AB)\) if \(M\) is the midpoint of \(AB\) and \(l(AM) = {0}\text{{ cm}}\)?",
                "Determine total length \(AB\) when midpoint segment \(AM = {0}\text{{ cm}}\).",
                "Find \(AB = 2 \times AM\) for \(AM = {0}\text{{ cm}}\).",
                "Compute \(l(AB)\) where \(M\) bisects segment \(AB\) and \(l(AM) = {0}\text{{ cm}}\).",
                "Evaluate total length \(AB\) given midpoint \(M\) and \(AM = {0}\text{{ cm}}\).",
                "If \(M\) is the midpoint of \(AB\) and \(AM = {0}\text{{ cm}}\), find \(AB\).",
                "For midpoint \(M\) of segment \(AB\), if \(AM = {0}\text{{ cm}}\), calculate \(AB\).",
                "Segment \(AB\) has midpoint \(M\) with \(AM = {0}\text{{ cm}}\). Determine \(l(AB)\)."
            ],
            'calc': lambda item: (
                f"{int(item[1])} cm",
                [f"{int(item[1]) + 2} cm", f"{int(item[1]) - 2 if item[1] > 2 else int(item[1]) + 4} cm", f"{item[0]} cm"],
                f"**Step 1: Midpoint property**\n\(AB = 2 \times AM = 2 \times {item[0]} = {int(item[1])}\text{{ cm}}\).\n**Step 2: Conclusion**\n{int(item[1])} cm."
            ),
            'svg': lambda item: svg_segment_midpoint("A", "M", "B"),
            'diff': 'easy'
        },
        # Arch 2: Algebraic: AM = MB => 3x - a = x + b => x = (a+b)/2
        {
            'data': [(2, 8, 5, 13), (2, 10, 6, 16), (4, 12, 8, 20), (4, 14, 9, 23), (6, 16, 11, 27),
                     (6, 18, 12, 30), (8, 20, 14, 34), (8, 22, 15, 37), (10, 24, 17, 41), (10, 26, 18, 44)],
            'tmpls': [
                "Point \(M\) is the midpoint of segment \(AB\). If \(AM = 3x - {0}\) and \(MB = x + {1}\), find \(x\).",
                "Since \(M\) is the midpoint of \(AB\), \(AM = MB\). If \(AM = 3x - {0}\) and \(MB = x + {1}\), calculate \(x\).",
                "Calculate \(x\) given that \(M\) bisects segment \(AB\) with \(AM = 3x - {0}\) and \(MB = x + {1}\).",
                "What is the value of \(x\) if midpoint \(M\) gives \(AM = 3x - {0}\) and \(MB = x + {1}\)?",
                "Determine \(x\) in segment \(AB\) with midpoint \(M\) where \(AM = 3x - {0}\) and \(MB = x + {1}\).",
                "Find \(x\) when \(3x - {0} = x + {1}\) for midpoint \(M\) of \(AB\).",
                "Compute \(x\) for midpoint \(M\) of segment \(AB\) having \(AM = 3x - {0}\) and \(MB = x + {1}\).",
                "Evaluate \(x\) given that \(M\) is the midpoint of \(AB\) with \(AM = 3x - {0}\) and \(MB = x + {1}\).",
                "If \(M\) is the midpoint of \(AB\), \(AM = 3x - {0}\), and \(MB = x + {1}\), find \(x\).",
                "For midpoint \(M\) of segment \(AB\), if \(AM = 3x - {0}\) and \(MB = x + {1}\), calculate \(x\)."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 2}", f"{item[2] - 2 if item[2] > 2 else item[2] + 4}", f"{item[3]}"],
                f"**Step 1: Midpoint equality**\n\(AM = MB \implies 3x - {item[0]} = x + {item[1]} \implies 2x = {item[0] + item[1]} \implies x = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Uniqueness of midpoint: exactly one midpoint
        {
            'data': [(1, "Exactly one"), (2, "Exactly one"), (3, "Exactly one"), (4, "Exactly one"), (5, "Exactly one"),
                     (6, "Exactly one"), (7, "Exactly one"), (8, "Exactly one"), (9, "Exactly one"), (10, "Exactly one")],
            'tmpls': [
                "How many midpoints does every line segment possess?",
                "What is the number of midpoints a line segment can have?",
                "State the number of unique midpoints of a line segment.",
                "Can a line segment have more than one midpoint?",
                "Determine the number of midpoints of segment \(AB\).",
                "How many points can divide a line segment into two equal parts?",
                "State the uniqueness property of the midpoint of a line segment.",
                "Every segment has how many midpoints?",
                "How many midpoints are there for any given line segment?",
                "For any line segment \(AB\), state the number of midpoints."
            ],
            'calc': lambda item: (
                "Exactly one midpoint",
                ["Two midpoints", "Infinitely many midpoints", "No midpoints"],
                f"**Step 1: Uniqueness of midpoint property**\nEvery line segment has one and only one midpoint.\n**Step 2: Conclusion**\nExactly one midpoint."
            ),
            'diff': 'easy'
        },
        # Arch 4: Coordinates of midpoint on number line: x_M = (x1 + x2)/2
        {
            'data': [(3, 9, 6), (5, 13, 9), (7, 17, 12), (9, 21, 15), (11, 25, 18),
                     (-7, 3, -2), (-9, 1, -4), (-11, -1, -6), (-13, -3, -8), (-15, -5, -10)],
            'tmpls': [
                "Coordinates of \(A\) and \(B\) are {0} and {1} respectively. Find the coordinate of midpoint \(M\) of segment \(AB\).",
                "Calculate the coordinate of midpoint \(M\) for points \(A({0})\) and \(B({1})\).",
                "What is the coordinate of the midpoint between {0} and {1} on the number line?",
                "Determine the midpoint coordinate of segment joining points with coordinates {0} and {1}.",
                "Find coordinate of midpoint \(M = \frac{{{0} + {1}}}{{2}}\).",
                "Compute the coordinate of midpoint of segment connecting {0} and {1}.",
                "Evaluate the midpoint coordinate for points at {0} and {1}.",
                "If coordinates of \(A\) and \(B\) are {0} and {1}, find the coordinate of midpoint \(M\).",
                "For points \(A({0})\) and \(B({1})\), calculate the coordinate of their midpoint.",
                "On a number line, find the midpoint coordinate of segment with endpoints {0} and {1}."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 2}", f"{item[2] - 2}", f"{item[0] + item[1]}"],
                f"**Step 1: Midpoint formula**\n\(x_M = \frac{{{item[0]} + {item[1]}}}{{2}} = \frac{{{item[0] + item[1]}}}{{2}} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(item[0], item[1], "A", "B"),
            'diff': 'easy'
        },
        # Arch 5: Given midpoint coordinate and one endpoint, find other endpoint: x2 = 2*xM - x1
        {
            'data': [(2, 6, 10), (3, 7, 11), (4, 9, 14), (5, 11, 17), (6, 13, 20),
                     (-4, 1, 6), (-5, 2, 9), (-6, 3, 12), (-7, 4, 15), (-8, 5, 18)],
            'tmpls': [
                "Point \(M\) is the midpoint of segment \(AB\). If coordinate of \(A\) is {0} and coordinate of \(M\) is {1}, find the coordinate of \(B\).",
                "Given endpoint \(A({0})\) and midpoint \(M({1})\), calculate the coordinate of endpoint \(B\).",
                "Calculate coordinate of \(B\) if \(M({1})\) is the midpoint of segment \(AB\) with \(A({0})\).",
                "What is the coordinate of endpoint \(B\) given \(A({0})\) and midpoint \(M({1})\)?",
                "Determine coordinate of \(B\) knowing midpoint is {1} and point \(A\) is at {0}.",
                "Find coordinate of \(B = 2 \times {1} - ({0})\).",
                "Compute coordinate of endpoint \(B\) for midpoint \(M({1})\) and \(A({0})\).",
                "Evaluate coordinate of \(B\) given midpoint \(M({1})\) and \(A({0})\).",
                "If \(M({1})\) is midpoint of \(AB\) and \(A\) has coordinate {0}, find coordinate of \(B\).",
                "For segment \(AB\), midpoint is \(M({1})\) and \(A\) is {0}. Calculate coordinate of \(B\)."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 2}", f"{item[2] - 2}", f"{item[1]}"],
                f"**Step 1: Midpoint inversion formula**\n\(x_M = \frac{{x_A + x_B}}{{2}} \implies x_B = 2x_M - x_A = 2({item[1]}) - ({item[0]}) = {2*item[1]} - {item[0]} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'svg': lambda item: svg_numberline(item[0], item[2], "A", "B"),
            'diff': 'medium'
        },
        # Arch 6: Perimeter of rectangle formed by midpoints
        {
            'data': [(10, 5), (12, 6), (14, 7), (16, 8), (18, 9),
                     (20, 10), (22, 11), (24, 12), (26, 13), (28, 14)],
            'tmpls': [
                "Segment \(AB\) has length {0}\text{{ cm}} and midpoint \(M\). Find \(MB\).",
                "If \(M\) is the midpoint of \(AB = {0}\text{{ cm}}\), calculate length of segment \(MB\).",
                "Calculate \(l(MB)\) where \(M\) bisects segment \(AB = {0}\text{{ cm}}\).",
                "What is the length of \(MB\) if \(M\) is the midpoint of segment \(AB = {0}\text{{ cm}}\)?",
                "Determine \(MB\) given \(l(AB) = {0}\text{{ cm}}\) and \(M\) is the midpoint.",
                "Find \(MB = \frac{{AB}}{{2}}\) for \(AB = {0}\text{{ cm}}\).",
                "Compute \(l(MB)\) in segment \(AB = {0}\text{{ cm}}\) with midpoint \(M\).",
                "Evaluate length of segment \(MB\) when \(M\) is the midpoint of \(AB = {0}\text{{ cm}}\).",
                "If \(M\) is the midpoint of segment \(AB\) measuring {0}\text{{ cm}}, find \(MB\).",
                "For segment \(AB = {0}\text{{ cm}}\) with midpoint \(M\), calculate \(MB\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 2} cm", f"{item[1] - 2 if item[1] > 2 else item[1] + 4} cm", f"{item[0]} cm"],
                f"**Step 1: Formula**\n\(MB = \frac{{AB}}{{2}} = \frac{{{item[0]}}}{{2}} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_segment_midpoint("A", "M", "B"),
            'diff': 'easy'
        },
        # Arch 7: Sum AM + MB = AB
        {
            'data': [(7, 14), (8, 16), (9, 18), (10, 20), (11, 22),
                     (12, 24), (13, 26), (14, 28), (15, 30), (16, 32)],
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
                [f"{item[0]} cm", f"{item[1] + 2} cm", f"{item[1] - 2} cm"],
                f"**Step 1: Formula**\n\(AM + MB = AB = 2 \times AM = 2 \times {item[0]} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_segment_midpoint("A", "M", "B"),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# 1.4.1: Antecedent vs Consequent
def gen_1_4_1():
    tc = "MH-9-MTH2-1-1.4.1"
    tname = "Antecedent (If part) vs Consequent (Then part)"
    archs = [
        # Arch 0: Identifying Antecedent in conditional statement
        {
            'data': [(1, "A quadrilateral is a rhombus", "Its diagonals are perpendicular bisectors of each other"),
                     (2, "Two angles form a linear pair", "They are supplementary"),
                     (3, "A triangle is equilateral", "All its angles are congruent"),
                     (4, "Two lines are parallel", "Alternate interior angles are congruent"),
                     (5, "A quadrilateral is a rectangle", "Its diagonals are congruent"),
                     (6, "A number is divisible by 4", "It is an even number"),
                     (7, "A polygon has 3 sides", "It is a triangle"),
                     (8, "Two circles have equal radii", "They are congruent circles"),
                     (9, "A triangle has two equal sides", "It is an isosceles triangle"),
                     (10, "Opposite sides of a quadrilateral are equal", "It is a parallelogram")],
            'tmpls': [
                "In the conditional statement 'If {1}, then {2}', identify the antecedent.",
                "What is the antecedent (hypothesis) in: 'If {1}, then {2}'?",
                "Identify the antecedent of the statement: 'If {1}, then {2}'.",
                "State the antecedent in the implication: 'If {1}, then {2}'.",
                "Which part of 'If {1}, then {2}' is the antecedent?",
                "Find the antecedent in the conditional: 'If {1}, then {2}'.",
                "Name the antecedent part of the statement: 'If {1}, then {2}'.",
                "Extract the antecedent from: 'If {1}, then {2}'.",
                "In 'If {1}, then {2}', which clause is the antecedent?",
                "Determine the antecedent in: 'If {1}, then {2}'."
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", "Both parts together", "Neither part"],
                f"**Step 1: Definition of antecedent**\nIn a conditional statement 'If P, then Q', the part following 'If' (P) is called the antecedent (or hypothesis).\nHere, the antecedent is: {item[1]}.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Identifying Consequent in conditional statement
        {
            'data': [(1, "A quadrilateral is a rhombus", "Its diagonals are perpendicular bisectors of each other"),
                     (2, "Two angles form a linear pair", "They are supplementary"),
                     (3, "A triangle is equilateral", "All its angles are congruent"),
                     (4, "Two lines are parallel", "Alternate interior angles are congruent"),
                     (5, "A quadrilateral is a rectangle", "Its diagonals are congruent"),
                     (6, "A number is divisible by 4", "It is an even number"),
                     (7, "A polygon has 3 sides", "It is a triangle"),
                     (8, "Two circles have equal radii", "They are congruent circles"),
                     (9, "A triangle has two equal sides", "It is an isosceles triangle"),
                     (10, "Opposite sides of a quadrilateral are equal", "It is a parallelogram")],
            'tmpls': [
                "In the conditional statement 'If {1}, then {2}', identify the consequent.",
                "What is the consequent (conclusion) in: 'If {1}, then {2}'?",
                "Identify the consequent of the statement: 'If {1}, then {2}'.",
                "State the consequent in the implication: 'If {1}, then {2}'.",
                "Which part of 'If {1}, then {2}' is the consequent?",
                "Find the consequent in the conditional: 'If {1}, then {2}'.",
                "Name the consequent part of the statement: 'If {1}, then {2}'.",
                "Extract the consequent from: 'If {1}, then {2}'.",
                "In 'If {1}, then {2}', which clause is the consequent?",
                "Determine the consequent in: 'If {1}, then {2}'."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[1]}", "Both parts together", "The word then"],
                f"**Step 1: Definition of consequent**\nIn a conditional statement 'If P, then Q', the part following 'then' (Q) is called the consequent (or conclusion).\nHere, the consequent is: {item[2]}.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 2: Writing a statement in 'If-then' form
        {
            'data': [(1, "The diagonals of a rhombus are perpendicular bisectors", "If a quadrilateral is a rhombus, then its diagonals are perpendicular bisectors"),
                     (2, "Every square is a rectangle", "If a quadrilateral is a square, then it is a rectangle"),
                     (3, "Opposite angles of a parallelogram are congruent", "If a quadrilateral is a parallelogram, then its opposite angles are congruent"),
                     (4, "Equilateral triangles are equiangular", "If a triangle is equilateral, then it is equiangular"),
                     (5, "All right angles are congruent", "If two angles are right angles, then they are congruent"),
                     (6, "Diagonals of a rectangle are equal", "If a quadrilateral is a rectangle, then its diagonals are equal"),
                     (7, "Radii of the same circle are equal", "If two segments are radii of the same circle, then their lengths are equal"),
                     (8, "Linear pair angles are supplementary", "If two angles form a linear pair, then they are supplementary"),
                     (9, "Isosceles triangles have two equal angles", "If a triangle is isosceles, then its base angles are equal"),
                     (10, "Adjacent angles of a parallelogram are supplementary", "If a quadrilateral is a parallelogram, then its adjacent angles are supplementary")],
            'tmpls': [
                "Write the statement '{1}' in conditional 'If-then' form.",
                "Express '{1}' as an 'If-then' conditional statement.",
                "What is the 'If-then' form of: '{1}'?",
                "Convert the statement '{1}' into conditional format.",
                "How is the property '{1}' written as an If-then sentence?",
                "Identify the correct conditional 'If-then' formulation of: '{1}'.",
                "State '{1}' in 'If-then' form.",
                "Transform '{1}' into a conditional statement.",
                "Which is the correct 'If-then' version of: '{1}'?",
                "Express '{1}' in conditional form."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                ["Only if it is true, then it holds", "When a shape exists, then it has properties", "None of these"],
                f"**Step 1: Conditional statement structure**\nA statement written using 'If' and 'then' clearly separates the given condition (antecedent) and the resulting property (consequent).\nFormulation: {item[2]}.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Identifying the Given (Hypothesis) in geometric proofs
        {
            'data': [(1, "A quadrilateral is a rectangle", "In quad ABCD, all angles are 90 deg"),
                     (2, "A triangle is isosceles", "In triangle ABC, side AB = side AC"),
                     (3, "Two lines are cut by transversal", "Line l || line m and line n is transversal"),
                     (4, "A quadrilateral is a parallelogram", "In quad ABCD, AB || CD and AD || BC"),
                     (5, "A point is on perpendicular bisector", "Point P is on perpendicular bisector of seg AB"),
                     (6, "A quadrilateral is a rhombus", "In quad ABCD, all sides are equal"),
                     (7, "A triangle is right-angled", "In triangle ABC, angle B = 90 deg"),
                     (8, "A quadrilateral is a square", "In quad ABCD, all sides are equal and all angles are 90 deg"),
                     (9, "A line segment has midpoint M", "Point M is on seg AB such that AM = MB"),
                     (10, "Two angles are vertically opposite", "Lines AB and CD intersect at O forming vertically opposite angles")],
            'tmpls': [
                "In a geometric theorem proof, what does the 'Given' (Data) section correspond to?",
                "The 'Given' part in the proof of a conditional statement corresponds to which component?",
                "Which component of a conditional statement represents the 'Given' in a formal proof?",
                "In proving a theorem, what is derived directly from the antecedent?",
                "The antecedent of a conditional statement becomes which section in a geometric proof?",
                "What corresponds to the antecedent in a standard geometric proof?",
                "Identify the role of the antecedent in a theorem proof.",
                "In a formal proof, 'Given' is formulated from which part of the statement?",
                "State which part of a conditional statement constitutes the 'Given'.",
                "For any theorem, what does the antecedent represent in its proof?"
            ],
            'calc': lambda item: (
                "The Antecedent (hypothesis)",
                ["The Consequent (conclusion)", "The Construction", "The Q.E.D. statement"],
                f"**Step 1: Structure of geometric proof**\nThe 'Given' section of a proof contains the facts provided in the antecedent (hypothesis) of the conditional statement.\n**Step 2: Conclusion**\nThe Antecedent (hypothesis)."
            ),
            'diff': 'easy'
        },
        # Arch 4: Identifying 'To Prove' in geometric proofs
        {
            'data': [(1, "To Prove"), (2, "To Prove"), (3, "To Prove"), (4, "To Prove"), (5, "To Prove"),
                     (6, "To Prove"), (7, "To Prove"), (8, "To Prove"), (9, "To Prove"), (10, "To Prove")],
            'tmpls': [
                "In a geometric proof, which section corresponds to the consequent (conclusion) of the theorem?",
                "The consequent of a conditional theorem corresponds to which section of its proof?",
                "What is derived from the consequent in a formal geometric proof?",
                "Which part of a proof specifies what needs to be established using deductive reasoning?",
                "The statement following 'then' in a theorem becomes which part of the proof?",
                "What corresponds to the consequent in a standard geometric theorem proof?",
                "Identify the proof section that states the consequent.",
                "In a theorem proof, 'To Prove' is written directly from which part?",
                "State which section of a proof expresses the consequent of the theorem.",
                "For any theorem, what does the consequent represent in its proof?"
            ],
            'calc': lambda item: (
                "To Prove (conclusion)",
                ["Given (hypothesis)", "Construction", "Proof statements"],
                f"**Step 1: Structure of geometric proof**\nThe 'To Prove' section of a proof specifies the statement following 'then' (the consequent).\n**Step 2: Conclusion**\nTo Prove (conclusion)."
            ),
            'diff': 'easy'
        },
        # Arch 5: Definition of conditional statement
        {
            'data': [(1, "Conditional statement"), (2, "Conditional statement"), (3, "Conditional statement"), (4, "Conditional statement"), (5, "Conditional statement"),
                     (6, "Conditional statement"), (7, "Conditional statement"), (8, "Conditional statement"), (9, "Conditional statement"), (10, "Conditional statement")],
            'tmpls': [
                "A statement written in the form 'If ..., then ...' is called what?",
                "What is the mathematical term for a sentence expressed in 'If P, then Q' form?",
                "Name the type of mathematical statement formulated with 'If' and 'then'.",
                "Statements of the form 'If antecedent, then consequent' are known as what?",
                "Identify the term for a proposition written in 'If ... then ...' format.",
                "What name is given to an implication written with 'If' and 'then'?",
                "A proposition that asserts that if one condition holds, another must follow is called what?",
                "State the name of a statement structured as 'If P, then Q'.",
                "What is an 'If-then' statement called in geometry and mathematical logic?",
                "Define the classification of statements written using 'If' and 'then'."
            ],
            'calc': lambda item: (
                "A conditional statement",
                ["A converse statement", "A postulate", "An axiom"],
                f"**Step 1: Definition**\nA statement which can be written in the 'If-then' form is called a conditional statement.\n**Step 2: Conclusion**\nA conditional statement."
            ),
            'diff': 'easy'
        },
        # Arch 6: Meaning of Converse
        {
            'data': [(1, "Converse"), (2, "Converse"), (3, "Converse"), (4, "Converse"), (5, "Converse"),
                     (6, "Converse"), (7, "Converse"), (8, "Converse"), (9, "Converse"), (10, "Converse")],
            'tmpls': [
                "If the antecedent and consequent in a conditional statement are interchanged, the resulting statement is called what?",
                "What is the statement formed by swapping the hypothesis and conclusion of a conditional statement?",
                "When 'If P, then Q' is changed to 'If Q, then P', what is the new statement called?",
                "Name the statement obtained by interchanging the antecedent and consequent.",
                "Identify the term for the statement with swapped antecedent and consequent.",
                "State the name of the statement: 'If consequent, then antecedent'.",
                "What do we call the statement obtained by reversing the 'If' and 'then' parts?",
                "Interchanging the 'If' part and 'then' part of a conditional statement gives what?",
                "If P -> Q, then Q -> P is known as which statement?",
                "What is the resulting proposition when hypothesis and conclusion are interchanged?"
            ],
            'calc': lambda item: (
                "The converse of the statement",
                ["The inverse of the statement", "The contrapositive of the statement", "A corollary"],
                f"**Step 1: Definition of converse**\nIf the antecedent and consequent in a given conditional statement are interchanged, the resulting statement is called the converse of the given statement.\n**Step 2: Conclusion**\nThe converse of the statement."
            ),
            'diff': 'easy'
        },
        # Arch 7: Truth value of converse: converse of a true statement is not necessarily true
        {
            'data': [(1, "Not necessarily true"), (2, "Not necessarily true"), (3, "Not necessarily true"), (4, "Not necessarily true"), (5, "Not necessarily true"),
                     (6, "Not necessarily true"), (7, "Not necessarily true"), (8, "Not necessarily true"), (9, "Not necessarily true"), (10, "Not necessarily true")],
            'tmpls': [
                "If a conditional statement is true, is its converse always true?",
                "State whether the converse of a true conditional statement is always true.",
                "True or False: The converse of every true conditional statement is also true.",
                "Can the converse of a true mathematical statement be false?",
                "What can be said about the truth value of the converse of a true theorem?",
                "Is the converse of a conditional statement guaranteed to be true whenever the statement is true?",
                "Evaluate the truth nature of the converse of a true conditional statement.",
                "Does a true conditional statement imply that its converse is necessarily true?",
                "State the relationship between the truth of a statement and the truth of its converse.",
                "If a statement is true, what is the validity of its converse?"
            ],
            'calc': lambda item: (
                "It is not necessarily true (may be true or false)",
                ["It is always true", "It is always false", "It is true only for right triangles"],
                f"**Step 1: Truth value of converse**\nThe converse of a true statement is not necessarily true. For example: 'If a figure is a square, it is a rectangle' is TRUE, but its converse 'If a figure is a rectangle, it is a square' is FALSE.\n**Step 2: Conclusion**\nIt is not necessarily true (may be true or false)."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

print("gen_1_3_2, gen_1_3_3, and gen_1_4_1 defined.")

def gen_1_4_2():
    tc = "MH-9-MTH2-1-1.4.2"
    tname = "Converse formulation"
    archs = [
        # Arch 0: Converse of alternate angles theorem
        {
            'data': [(1, "lines are parallel"), (2, "lines are parallel"), (3, "lines are parallel"), (4, "lines are parallel"), (5, "lines are parallel"),
                     (6, "lines are parallel"), (7, "lines are parallel"), (8, "lines are parallel"), (9, "lines are parallel"), (10, "lines are parallel")],
            'tmpls': [
                "What is the converse of: 'If two lines are parallel, then alternate interior angles formed by a transversal are equal'?",
                "Formulate the converse statement for the alternate interior angles theorem.",
                "State the converse of: 'If two coplanar lines are parallel, their alternate interior angles are congruent'.",
                "Write the converse of the theorem: parallel lines cut by a transversal have equal alternate interior angles.",
                "Identify the correct converse: 'If two lines are parallel, alternate angles are equal'.",
                "Reverse hypothesis and conclusion: 'If lines are parallel, alternate angles are congruent'.",
                "Which statement represents the converse of the alternate angle property for parallel lines?",
                "Provide the converse formulation: 'If two lines are parallel, then the alternate angles formed are equal'.",
                "State the converse: 'If lines are parallel, alternate angles made by a transversal are equal'.",
                "What is the converse proposition of the alternate angles theorem?"
            ],
            'calc': lambda item: (
                "If alternate interior angles made by a transversal are equal, then the two lines are parallel",
                ["If alternate angles are supplementary, then the two lines are perpendicular",
                 "If two lines are parallel, then corresponding angles are equal",
                 "If two lines intersect, then alternate angles are not equal"],
                f"**Step 1: Converse definition**\nThe converse interchanges antecedent and consequent. Original: If lines are parallel (antecedent), alternate angles are equal (consequent).\n**Step 2: Conclusion**\nIf alternate interior angles made by a transversal are equal, then the two lines are parallel."
            ),
            'diff': 'medium'
        },
        # Arch 1: Converse of rectangle diagonals
        {
            'data': [(1, "rectangle"), (2, "rectangle"), (3, "rectangle"), (4, "rectangle"), (5, "rectangle"),
                     (6, "rectangle"), (7, "rectangle"), (8, "rectangle"), (9, "rectangle"), (10, "rectangle")],
            'tmpls': [
                "What is the converse of: 'If a quadrilateral is a rectangle, then its diagonals are congruent'?",
                "State the converse of the proposition: 'If a quadrilateral is a rectangle, its diagonals are equal in length'.",
                "Formulate the converse: 'If a quadrilateral is a rectangle, then the diagonals are congruent'.",
                "Write the converse of: 'A rectangle has congruent diagonals'.",
                "Which statement is the converse of: 'If a quad is a rectangle, its diagonals are congruent'?",
                "Identify the converse of the theorem that diagonals of a rectangle are congruent.",
                "State the converse statement: 'If a polygon is a rectangle, then its diagonals are congruent'.",
                "Reversing antecedent and consequent of 'If a quadrilateral is a rectangle, then its diagonals are congruent' yields what?",
                "Find the converse: 'If a quadrilateral is a rectangle, then its diagonals are congruent'.",
                "What is the converse formulation for: 'If a quadrilateral is a rectangle, then its diagonals are congruent'?"
            ],
            'calc': lambda item: (
                "If the diagonals of a quadrilateral are congruent, then it is a rectangle",
                ["If the diagonals of a quadrilateral are perpendicular, then it is a rectangle",
                 "If a quadrilateral is a square, its diagonals are congruent",
                 "If the diagonals of a quadrilateral bisect each other, it is a rhombus"],
                f"**Step 1: Interchange antecedent and consequent**\nConsequent becomes: 'If the diagonals of a quadrilateral are congruent'\nAntecedent becomes: 'then it is a rectangle'\n**Step 2: Conclusion**\nIf the diagonals of a quadrilateral are congruent, then it is a rectangle."
            ),
            'diff': 'medium'
        },
        # Arch 2: Converse of isosceles triangle theorem
        {
            'data': [(1, "isosceles"), (2, "isosceles"), (3, "isosceles"), (4, "isosceles"), (5, "isosceles"),
                     (6, "isosceles"), (7, "isosceles"), (8, "isosceles"), (9, "isosceles"), (10, "isosceles")],
            'tmpls': [
                "What is the converse of the Isosceles Triangle Theorem: 'If two sides of a triangle are congruent, the angles opposite them are congruent'?",
                "State the converse: 'If two sides of a triangle are equal, then the opposite angles are equal'.",
                "Formulate the converse of: 'If two sides of a triangle are congruent, then the angles opposite to them are congruent'.",
                "Write the converse for the theorem that equal sides imply equal opposite angles in a triangle.",
                "Identify the converse of: 'If two sides of a triangle are congruent, angles opposite them are congruent'.",
                "What is the converse statement of: 'If two sides of a triangle are congruent, then the opposite angles are congruent'?",
                "Express the converse of the isosceles triangle angle-side relationship.",
                "State the converse of: 'If in a triangle two sides are equal, the angles opposite are equal'.",
                "Which statement is the converse of: 'If two sides of a triangle are congruent, then the angles opposite them are congruent'?",
                "Formulate the converse of the theorem on congruent sides of a triangle."
            ],
            'calc': lambda item: (
                "If two angles of a triangle are congruent, then the sides opposite to them are congruent",
                ["If three angles of a triangle are congruent, then it is equilateral",
                 "If two angles of a triangle are complementary, then it is a right triangle",
                 "If two sides of a triangle are unequal, the greater side has greater angle opposite"],
                f"**Step 1: Formulation**\nInterchange hypothesis (two sides congruent) and conclusion (two opposite angles congruent).\n**Step 2: Conclusion**\nIf two angles of a triangle are congruent, then the sides opposite to them are congruent."
            ),
            'diff': 'medium'
        },
        # Arch 3: Converse of even prime number
        {
            'data': [(1, "prime"), (2, "prime"), (3, "prime"), (4, "prime"), (5, "prime"),
                     (6, "prime"), (7, "prime"), (8, "prime"), (9, "prime"), (10, "prime")],
            'tmpls': [
                "What is the converse of: 'If a number is an even prime number, then it is 2'?",
                "State the converse of: 'If a number is an even prime, then it is equal to 2'.",
                "Write the converse of: 'If a natural number is an even prime, then it is 2'.",
                "Formulate the converse of: 'If a number is an even prime number, then it is 2'.",
                "Which proposition is the converse of: 'If a number is an even prime, then it is 2'?",
                "Identify the converse statement for: 'If an integer is an even prime, then it is 2'.",
                "Interchange antecedent and consequent in: 'If a number is an even prime, then it is 2'.",
                "State the converse: 'If a number is an even prime, then it is 2'.",
                "What is the converse of the conditional statement: 'If a number is an even prime, then it is 2'?",
                "Give the converse: 'If a positive integer is an even prime, then it is 2'."
            ],
            'calc': lambda item: (
                "If a number is 2, then it is an even prime number",
                ["If a number is not 2, then it is odd",
                 "If a number is even, then it is a composite number",
                 "If a number is prime, then it is odd"],
                f"**Step 1: Converse**\nSwap 'a number is an even prime' with 'it is 2'.\n**Step 2: Conclusion**\nIf a number is 2, then it is an even prime number."
            ),
            'diff': 'easy'
        },
        # Arch 4: Truth value analysis of false converses (x=3 implies x^2=9)
        {
            'data': [(1, "x=3"), (2, "x=3"), (3, "x=3"), (4, "x=3"), (5, "x=3"),
                     (6, "x=3"), (7, "x=3"), (8, "x=3"), (9, "x=3"), (10, "x=3")],
            'tmpls': [
                "Consider the statement: 'If x = 3, then x^2 = 9'. What is its converse, and is it true for all real numbers?",
                "What is the converse of 'If x = 3, then x^2 = 9', and what is its validity?",
                "State the converse of 'If x = 3, then x^2 = 9' and evaluate its truth value.",
                "Formulate the converse of 'If x = 3, then x^2 = 9' and state whether it is always true.",
                "Which is the converse of 'If x = 3, then x^2 = 9', and why is it not necessarily true?",
                "Write the converse of 'If a real number x = 3, then x^2 = 9' and determine its truth.",
                "Is the converse of 'If x = 3, then x^2 = 9' true? State the converse and its validity.",
                "State the converse statement of 'If x = 3, then x^2 = 9'.",
                "Identify the converse of 'If x = 3, then x^2 = 9' and its truth status.",
                "Give the converse of 'If x = 3, then x^2 = 9' along with its truth classification."
            ],
            'calc': lambda item: (
                "Converse: 'If x^2 = 9, then x = 3'; it is FALSE because x could be -3",
                ["Converse: 'If x^2 = 9, then x = 3'; it is TRUE for all real numbers",
                 "Converse: 'If x != 3, then x^2 != 9'; it is TRUE",
                 "Converse: 'If x^2 != 9, then x != 3'; it is FALSE"],
                f"**Step 1: Formulate converse**\nSwapping antecedent and consequent gives: 'If x^2 = 9, then x = 3'.\n**Step 2: Evaluate truth value**\nIf x^2 = 9, x can be 3 or -3. Since (-3)^2 = 9 but -3 != 3, the converse is FALSE.\n**Step 3: Conclusion**\nConverse: 'If x^2 = 9, then x = 3'; it is FALSE because x could be -3."
            ),
            'diff': 'hard'
        },
        # Arch 5: Parallelogram diagonals converse
        {
            'data': [(1, "parallelogram"), (2, "parallelogram"), (3, "parallelogram"), (4, "parallelogram"), (5, "parallelogram"),
                     (6, "parallelogram"), (7, "parallelogram"), (8, "parallelogram"), (9, "parallelogram"), (10, "parallelogram")],
            'tmpls': [
                "What is the converse of: 'If a quadrilateral is a parallelogram, then its diagonals bisect each other'?",
                "State the converse of: 'If a quadrilateral is a parallelogram, its diagonals bisect each other'.",
                "Formulate the converse: 'If a quadrilateral is a parallelogram, then the diagonals bisect each other'.",
                "Write the converse of the theorem: 'Diagonals of a parallelogram bisect each other'.",
                "Which statement represents the converse of: 'If a quadrilateral is a parallelogram, its diagonals bisect each other'?",
                "Identify the converse: 'If ABCD is a parallelogram, then its diagonals bisect each other'.",
                "Give the converse formulation of the parallelogram diagonal bisection property.",
                "State the converse proposition: 'If a quadrilateral is a parallelogram, then its diagonals bisect each other'.",
                "What is the converse statement: 'If a four-sided figure is a parallelogram, then its diagonals bisect each other'?",
                "Write down the converse of: 'If a quadrilateral is a parallelogram, its diagonals bisect each other'."
            ],
            'calc': lambda item: (
                "If the diagonals of a quadrilateral bisect each other, then it is a parallelogram",
                ["If the diagonals of a quadrilateral are equal, then it is a parallelogram",
                 "If the diagonals of a quadrilateral are perpendicular, then it is a parallelogram",
                 "If opposite sides of a quadrilateral are parallel, then diagonals are equal"],
                f"**Step 1: Formulate converse**\nInterchange 'a quadrilateral is a parallelogram' and 'its diagonals bisect each other'.\n**Step 2: Conclusion**\nIf the diagonals of a quadrilateral bisect each other, then it is a parallelogram."
            ),
            'diff': 'medium'
        },
        # Arch 6: Interior angles theorem converse
        {
            'data': [(1, "interior"), (2, "interior"), (3, "interior"), (4, "interior"), (5, "interior"),
                     (6, "interior"), (7, "interior"), (8, "interior"), (9, "interior"), (10, "interior")],
            'tmpls': [
                "What is the converse of: 'If two parallel lines are cut by a transversal, then the interior angles on the same side are supplementary'?",
                "State the converse of the interior angles theorem for parallel lines.",
                "Formulate the converse: 'If two lines are parallel, then interior angles on the same side of a transversal are supplementary'.",
                "Write the converse of: 'If lines are parallel, interior angles sum to 180°'.",
                "Which statement is the converse of: 'If two parallel lines are intersected by a transversal, interior angles are supplementary'?",
                "State the converse proposition of the parallel line interior angles property.",
                "Identify the converse: 'If two lines are parallel, interior angles on the same side of a transversal are supplementary'.",
                "Express the converse of the interior angles theorem.",
                "What is the converse of: 'If lines are parallel, then interior angles on the same side of a transversal are supplementary'?",
                "Give the converse of: 'If two parallel lines are cut by a transversal, interior angles are supplementary'."
            ],
            'calc': lambda item: (
                "If interior angles on the same side of a transversal are supplementary, then the two lines are parallel",
                ["If interior angles on the same side of a transversal are equal, then the two lines are parallel",
                 "If two lines are parallel, then interior angles are equal",
                 "If two lines intersect, then interior angles are supplementary"],
                f"**Step 1: Formulate converse**\nInterchange hypothesis (lines are parallel) with conclusion (interior angles are supplementary).\n**Step 2: Conclusion**\nIf interior angles on the same side of a transversal are supplementary, then the two lines are parallel."
            ),
            'diff': 'medium'
        },
        # Arch 7: Cyclic quadrilateral converse
        {
            'data': [(1, "cyclic"), (2, "cyclic"), (3, "cyclic"), (4, "cyclic"), (5, "cyclic"),
                     (6, "cyclic"), (7, "cyclic"), (8, "cyclic"), (9, "cyclic"), (10, "cyclic")],
            'tmpls': [
                "What is the converse of: 'If a quadrilateral is cyclic, then its opposite angles are supplementary'?",
                "State the converse of: 'If a quadrilateral is cyclic, opposite angles are supplementary'.",
                "Formulate the converse of: 'If a quadrilateral is cyclic, then its opposite angles are supplementary'.",
                "Write the converse: 'Opposite angles of a cyclic quadrilateral are supplementary'.",
                "Which statement represents the converse of the cyclic quadrilateral theorem?",
                "Identify the converse of: 'If a quadrilateral is cyclic, its opposite angles sum to 180°'.",
                "Give the converse formulation: 'If a quadrilateral is cyclic, then its opposite angles are supplementary'.",
                "State the converse proposition: 'If a quadrilateral is cyclic, opposite angles are supplementary'.",
                "What is the converse of: 'If a quadrilateral is cyclic, then its opposite angles are supplementary'?",
                "Express the converse: 'If ABCD is a cyclic quadrilateral, then opposite angles are supplementary'."
            ],
            'calc': lambda item: (
                "If opposite angles of a quadrilateral are supplementary, then the quadrilateral is cyclic",
                ["If opposite angles of a quadrilateral are equal, then the quadrilateral is cyclic",
                 "If adjacent angles of a quadrilateral are supplementary, then it is cyclic",
                 "If diagonals of a quadrilateral are equal, then it is cyclic"],
                f"**Step 1: Formulate converse**\nInterchange 'a quadrilateral is cyclic' with 'its opposite angles are supplementary'.\n**Step 2: Conclusion**\nIf opposite angles of a quadrilateral are supplementary, then the quadrilateral is cyclic."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def gen_1_4_3():
    tc = "MH-9-MTH2-1-1.4.3"
    tname = "Direct and indirect proof methods"
    archs = [
        # Arch 0: First step of indirect proof (assume negation)
        {
            'data': [(1, "negation"), (2, "negation"), (3, "negation"), (4, "negation"), (5, "negation"),
                     (6, "negation"), (7, "negation"), (8, "negation"), (9, "negation"), (10, "negation")],
            'tmpls': [
                "In an indirect proof, what is the fundamental first step taken?",
                "How does an indirect proof (proof by contradiction) begin?",
                "What assumption is made at the start of an indirect geometric proof?",
                "State the initial assumption required when proving a theorem indirectly.",
                "In proof by contradiction, what is assumed to be true initially?",
                "What is the starting point of an indirect proof method in geometry?",
                "To prove a statement indirectly, what hypothesis must first be set up?",
                "Describe the first step in conducting an indirect proof.",
                "When constructing an indirect proof, what assumption is made at the beginning?",
                "What is assumed in an indirect proof about the statement to be proved?"
            ],
            'calc': lambda item: (
                "Assume that the statement to be proved is false (negation of the conclusion)",
                ["Assume that the given hypothesis is false",
                 "Assume that all axioms in geometry are invalid",
                 "Assume that the conclusion is already proven true directly"],
                f"**Step 1: Principle of indirect proof**\nIn an indirect proof, we assume that the statement to be proved is FALSE (we assume the negation of the conclusion).\n**Step 2: Conclusion**\nAssume that the statement to be proved is false (negation of the conclusion)."
            ),
            'diff': 'medium'
        },
        # Arch 1: Euclid Postulate 3: Circle with any center and radius
        {
            'data': [(1, "Postulate 3"), (2, "Postulate 3"), (3, "Postulate 3"), (4, "Postulate 3"), (5, "Postulate 3"),
                     (6, "Postulate 3"), (7, "Postulate 3"), (8, "Postulate 3"), (9, "Postulate 3"), (10, "Postulate 3")],
            'tmpls': [
                "Which Euclid postulate states: 'A circle can be drawn with any center and any radius'?",
                "Name the Euclid postulate that asserts a circle may be described with any center and radius.",
                "'A circle can be drawn with any center and any radius' is which of Euclid's postulates?",
                "Identify the postulate: 'To describe a circle with any center and distance'.",
                "Which postulate of Euclid guarantees that a circle can be constructed given a center and radius?",
                "State the number of Euclid's postulate: 'A circle can be drawn with any center and any radius'.",
                "According to Euclid's geometry, which postulate states that a circle can be drawn with any given center and radius?",
                "Euclid stated that a circle can be drawn with any center and radius. This is Postulate number what?",
                "Classify the statement: 'A circle can be drawn with any center and any radius' among Euclid's postulates.",
                "Which of Euclid's five postulates defines the existence of a circle with any center and radius?"
            ],
            'calc': lambda item: (
                "Euclid's Postulate 3",
                ["Euclid's Postulate 1", "Euclid's Postulate 2", "Euclid's Postulate 4"],
                f"**Step 1: Euclid's Postulates**\nPostulate 1: A straight line may be drawn from any one point to any other point.\nPostulate 2: A terminated line can be produced indefinitely.\nPostulate 3: A circle can be drawn with any center and any radius.\n**Step 2: Conclusion**\nEuclid's Postulate 3."
            ),
            'diff': 'easy'
        },
        # Arch 2: Euclid Postulate 2: Line produced indefinitely
        {
            'data': [(1, "Postulate 2"), (2, "Postulate 2"), (3, "Postulate 2"), (4, "Postulate 2"), (5, "Postulate 2"),
                     (6, "Postulate 2"), (7, "Postulate 2"), (8, "Postulate 2"), (9, "Postulate 2"), (10, "Postulate 2")],
            'tmpls': [
                "Which Euclid postulate states: 'A terminated line (line segment) can be produced indefinitely'?",
                "Name the Euclid postulate asserting that a line segment can be extended continuously in a straight line.",
                "'A terminated line can be produced indefinitely' corresponds to which of Euclid's postulates?",
                "Identify the postulate: 'A line segment can be extended indefinitely in both directions'.",
                "Which postulate of Euclid establishes that any finite straight line can be produced continuously?",
                "State the number of Euclid's postulate that allows a line segment to be extended indefinitely.",
                "According to Euclid, a line segment can be produced indefinitely. This is Postulate number what?",
                "Which Euclid postulate allows extending a line segment continuously in a straight line?",
                "Classify: 'A terminated line can be produced indefinitely' among Euclid's postulates.",
                "Euclid's statement that a straight line segment can be extended indefinitely is which postulate?"
            ],
            'calc': lambda item: (
                "Euclid's Postulate 2",
                ["Euclid's Postulate 1", "Euclid's Postulate 3", "Euclid's Postulate 5"],
                f"**Step 1: Euclid's Postulates**\nPostulate 2 states: 'A terminated line can be produced indefinitely' (a line segment can be extended indefinitely on both sides).\n**Step 2: Conclusion**\nEuclid's Postulate 2."
            ),
            'diff': 'easy'
        },
        # Arch 3: Euclid Postulate 1: Straight line between any two points
        {
            'data': [(1, "Postulate 1"), (2, "Postulate 1"), (3, "Postulate 1"), (4, "Postulate 1"), (5, "Postulate 1"),
                     (6, "Postulate 1"), (7, "Postulate 1"), (8, "Postulate 1"), (9, "Postulate 1"), (10, "Postulate 1")],
            'tmpls': [
                "Which Euclid postulate states: 'A straight line may be drawn from any one point to any other point'?",
                "Name the Euclid postulate that asserts exactly one straight line passes through two distinct points.",
                "'A straight line may be drawn from any one point to any other point' is which Euclid postulate?",
                "Identify the postulate: 'Two distinct points determine a unique straight line'.",
                "Which postulate of Euclid states that a straight line can join any two points?",
                "State the number of Euclid's postulate: 'A straight line may be drawn from any one point to another'.",
                "According to Euclid's geometry, which postulate allows drawing a straight line between two points?",
                "Euclid stated that a straight line may be drawn from any point to any other point. This is which postulate?",
                "Classify: 'A straight line may be drawn from any one point to any other point' among Euclid's postulates.",
                "Which of Euclid's five postulates states that a line segment connects two points?"
            ],
            'calc': lambda item: (
                "Euclid's Postulate 1",
                ["Euclid's Postulate 2", "Euclid's Postulate 3", "Euclid's Postulate 4"],
                f"**Step 1: Euclid's Postulates**\nPostulate 1 states: 'A straight line may be drawn from any one point to any other point.'\n**Step 2: Conclusion**\nEuclid's Postulate 1."
            ),
            'diff': 'easy'
        },
        # Arch 4: Euclid Postulate 4: All right angles are equal
        {
            'data': [(1, "Postulate 4"), (2, "Postulate 4"), (3, "Postulate 4"), (4, "Postulate 4"), (5, "Postulate 4"),
                     (6, "Postulate 4"), (7, "Postulate 4"), (8, "Postulate 4"), (9, "Postulate 4"), (10, "Postulate 4")],
            'tmpls': [
                "Which Euclid postulate states: 'All right angles are equal to one another'?",
                "Name the Euclid postulate that asserts all right angles are congruent.",
                "'All right angles are equal to one another' corresponds to which of Euclid's postulates?",
                "Identify the postulate: 'Every right angle is equal to every other right angle'.",
                "Which postulate of Euclid defines the equivalence of all right angles?",
                "State the number of Euclid's postulate establishing that all right angles are equal.",
                "According to Euclid's geometry, all right angles are equal to each other. This is which postulate?",
                "Euclid stated that all right angles are equal. This is Postulate number what?",
                "Classify: 'All right angles are equal to one another' among Euclid's postulates.",
                "Which of Euclid's five postulates states that all right angles are equal?"
            ],
            'calc': lambda item: (
                "Euclid's Postulate 4",
                ["Euclid's Postulate 1", "Euclid's Postulate 2", "Euclid's Postulate 5"],
                f"**Step 1: Euclid's Postulates**\nPostulate 4 states: 'All right angles are equal to one another.'\n**Step 2: Conclusion**\nEuclid's Postulate 4."
            ),
            'diff': 'easy'
        },
        # Arch 5: Direct proof structure and logical deduction
        {
            'data': [(1, "direct"), (2, "direct"), (3, "direct"), (4, "direct"), (5, "direct"),
                     (6, "direct"), (7, "direct"), (8, "direct"), (9, "direct"), (10, "direct")],
            'tmpls': [
                "In a direct geometric proof, how is the truth of a theorem established?",
                "What characterizes the direct method of proof in geometry?",
                "How does a direct proof progress from given facts to the conclusion?",
                "Describe the flow of reasoning in a direct mathematical proof.",
                "What is the logical structure used in a direct proof?",
                "In geometric proofs, how is a theorem proved using the direct method?",
                "State how conclusions are deduced in a direct proof.",
                "What defines the direct method of proving a mathematical proposition?",
                "In a direct proof, what are the steps connecting 'Given' to 'To Prove'?",
                "Explain the mechanism of a direct geometric proof."
            ],
            'calc': lambda item: (
                "By using axioms, definitions, and proven theorems in logical sequence to deduce the conclusion directly from the given hypothesis",
                ["By assuming the conclusion is false and reaching an impossible contradiction",
                 "By testing several numerical examples and observing the pattern",
                 "By drawing an accurate scale figure and measuring the angles with a protractor"],
                f"**Step 1: Direct proof method**\nIn a direct proof, we assume the hypothesis (Given) is true, and by applying definitions, axioms, postulates, and previously proven theorems in a chain of logical deduction, we directly arrive at the conclusion (To Prove).\n**Step 2: Conclusion**\nBy using axioms, definitions, and proven theorems in logical sequence to deduce the conclusion directly from the given hypothesis."
            ),
            'diff': 'medium'
        },
        # Arch 6: Proof by contradiction conclusion mechanism
        {
            'data': [(1, "contradiction"), (2, "contradiction"), (3, "contradiction"), (4, "contradiction"), (5, "contradiction"),
                     (6, "contradiction"), (7, "contradiction"), (8, "contradiction"), (9, "contradiction"), (10, "contradiction")],
            'tmpls': [
                "In an indirect proof, when the initial assumption leads to a contradiction with a known fact or given hypothesis, what is concluded?",
                "What conclusion is reached when an indirect proof assumption results in a logical contradiction?",
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
                "The assumption is proved false, and hence the original statement to be proved is true",
                ["The theorem is proved false and must be discarded",
                 "The given hypothesis must be modified",
                 "A direct proof is immediately required instead"],
                f"**Step 1: Indirect proof logic**\nSince the assumption leads to a contradiction with an established truth, the assumption must be FALSE. Consequently, the original statement (its opposite) must be TRUE.\n**Step 2: Conclusion**\nThe assumption is proved false, and hence the original statement to be proved is true."
            ),
            'diff': 'medium'
        },
        # Arch 7: Axiom vs Postulate vs Theorem definitions
        {
            'data': [(1, "Postulates"), (2, "Postulates"), (3, "Postulates"), (4, "Postulates"), (5, "Postulates"),
                     (6, "Postulates"), (7, "Postulates"), (8, "Postulates"), (9, "Postulates"), (10, "Postulates")],
            'tmpls': [
                "What did Euclid call self-evident assumptions that are specific to geometry?",
                "Self-evident truths assumed without proof specific to geometric space are called what?",
                "Name the geometric assumptions that are accepted as self-evident without proof.",
                "In Euclid's geometry, what term is used for assumptions that are specific to geometry?",
                "What is the distinction: general self-evident truths are axioms, while self-evident geometric truths are what?",
                "Identify the term for basic geometric assumptions accepted without proof.",
                "Euclid used the term 'axioms' for common notions; what term did he use for geometric assumptions?",
                "What are self-evident geometric assumptions called in Euclidean geometry?",
                "State the name given to fundamental geometric truths accepted without proof.",
                "In Greek mathematics, self-evident assumptions peculiar to geometry were called what?"
            ],
            'calc': lambda item: (
                "Postulates",
                ["Theorems", "Corollaries", "Conjectures"],
                f"**Step 1: Distinction between Axioms and Postulates**\nEuclid divided self-evident assumptions into two types:\n1. Axioms (Common Notions): assumptions used throughout mathematics (e.g. things equal to the same thing are equal to one another).\n2. Postulates: assumptions specific to geometry.\n**Step 2: Conclusion**\nPostulates."
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
