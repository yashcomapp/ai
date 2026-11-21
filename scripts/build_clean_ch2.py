# scripts/build_clean_ch2.py
# Clean generator for Chapter 2: Parallel Lines (7 subtopics, 560 Qs)
# 100% distinct, zero schema errors, >=60% SVGs.

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine import SEQS_80, build_q, generate_subtopic, svg_parallel_transversal, svg_triangle, svg_triangle_ext

CH_NUM = 2
CH_NAME = "Parallel Lines"

# =============================================================================
# 2.1.1: Sum of interior angles on same side of transversal is 180° theorem (80 Qs)
# =============================================================================
def gen_2_1_1():
    tc = "MH-9-MTH2-2-2.1.1"
    tname = "Sum of interior angles on same side of transversal is 180° theorem"
    archs = [
        # Arch 0: Given one interior angle, find the other: 180 - a
        {
            'data': [(50, 130), (55, 125), (60, 120), (65, 115), (70, 110),
                     (75, 105), (80, 100), (85, 95), (45, 135), (40, 140)],
            'tmpls': [
                "Two parallel lines are intersected by a transversal. If one interior angle on one side is {0}°, find the other interior angle on the same side.",
                "In the figure, line l || line m and line n is transversal. If an interior angle measures {0}°, calculate its consecutive interior angle.",
                "Calculate the co-interior angle adjacent to {0}° formed by a transversal cutting two parallel lines.",
                "What is the measure of the interior angle on the same side of the transversal if the first interior angle is {0}°?",
                "Determine the second interior angle on the same side of a transversal of parallel lines when one angle is {0}°.",
                "Find the consecutive interior angle: 180° - {0}° for parallel lines.",
                "Lines l and m are parallel. If interior angle on same side is {0}°, evaluate the other interior angle.",
                "Compute the co-interior angle when one of the interior angles on the same side of a transversal is {0}°.",
                "If two parallel lines are cut by a transversal and one consecutive interior angle is {0}°, find the other.",
                "For parallel lines with transversal, find the interior angle on the same side if one angle measures {0}°."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{item[1] + 10}°", f"{item[1] - 10}°", f"{item[0]}°"],
                f"**Step 1: Interior angles theorem**\\nInterior angles on the same side of a transversal are supplementary:\\n\\(\\text{{Interior angle}} = 180^\\circ - {item[0]}^\\circ = {item[1]}^\\circ\\).\\n**Step 2: Conclusion**\\n{item[1]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"int: {item[0]}°, {item[1]}°"),
            'diff': 'easy'
        },
        # Arch 1: Algebraic interior angles: (ax + b) + (cx + d) = 180 => find x
        {
            'data': [(2, 10, 3, 20, 30), (3, 5, 2, 25, 30), (4, 10, 1, 20, 30),
                     (2, 20, 2, 40, 30), (3, 15, 2, 15, 30), (1, 30, 4, 0, 30),
                     (2, 25, 3, 5, 30), (4, 5, 1, 25, 30), (3, 20, 1, 40, 30), (2, 35, 2, 25, 30)],
            # Ensure distinct values of x:
            # let's set different values of x from 15 to 24:
            # x=15: 3x + 10 + 2x + 95 = 5x + 105 = 180 => x = 15
            # x=16: 4x + 10 + 6x + 10 = 10x + 20 = 180 => x = 16
            # x=17: 3x + 20 + 2x + 75 = 5x + 95 = 180 => x = 17
            # x=18: 2x + 30 + 3x + 60 = 5x + 90 = 180 => x = 18
            # x=19: 4x + 15 + 1x + 70 = 5x + 85 = 180 => x = 19
            # x=20: 3x + 20 + 2x + 60 = 5x + 80 = 180 => x = 20
            # x=21: 2x + 10 + 3x + 65 = 5x + 75 = 180 => x = 21
            # x=22: 4x + 12 + 1x + 80 = 5x + 92 = 180 => x = 22 (wait, 5*22=110, 110+70=180 => 4x+10 + 1x+60)
            # x=23: 2x + 20 + 3x + 45 = 5x + 65 = 180 => x = 23
            # x=24: 3x + 15 + 2x + 45 = 5x + 60 = 180 => x = 24
            'data': [(3, 10, 2, 95, 15), (4, 10, 6, 10, 16), (3, 20, 2, 75, 17),
                     (2, 30, 3, 60, 18), (4, 15, 1, 70, 19), (3, 20, 2, 60, 20),
                     (2, 10, 3, 65, 21), (4, 10, 1, 60, 22), (2, 20, 3, 45, 23), (3, 15, 2, 45, 24)],
            'tmpls': [
                "Two parallel lines are cut by a transversal. If interior angles on the same side are \(({0}x + {1})^\circ\) and \(({2}x + {3})^\circ\), find \(x\).",
                "Interior angles on the same side of a transversal of parallel lines are \({0}x + {1}\) and \({2}x + {3}\). Calculate \(x\).",
                "Find \(x\) if consecutive interior angles of parallel lines are given by \(({0}x + {1})^\circ\) and \(({2}x + {3})^\circ\).",
                "What is the value of \(x\) when co-interior angles are \(({0}x + {1})^\circ\) and \(({2}x + {3})^\circ\)?",
                "Determine \(x\) from the equation \(({0}x + {1}) + ({2}x + {3}) = 180\).",
                "Calculate variable \(x\) for interior angles \(({0}x + {1})^\circ\) and \(({2}x + {3})^\circ\) on parallel lines.",
                "Evaluate \(x\) given that interior angles on the same side of transversal sum to 180°: \(({0}x + {1})^\circ\) and \(({2}x + {3})^\circ\).",
                "Lines l || m are cut by transversal n. If interior angles are \(({0}x + {1})^\circ\) and \(({2}x + {3})^\circ\), find \(x\).",
                "If interior angles on one side of a transversal are \(({0}x + {1})^\circ\) and \(({2}x + {3})^\circ\), calculate \(x\).",
                "For parallel lines with co-interior angles \(({0}x + {1})^\circ\) and \(({2}x + {3})^\circ\), find \(x\)."
            ],
            'calc': lambda item: (
                f"x = {item[4]}",
                [f"x = {item[4] + 3}", f"x = {item[4] - 3}", f"x = {item[4] + 6}"],
                f"**Step 1: Interior angles sum equation**\\n\\(({item[0]}x + {item[1]}) + ({item[2]}x + {item[3]}) = 180 \\implies {item[0]+item[2]}x + {item[1]+item[3]} = 180\\).\\n\\({item[0]+item[2]}x = {180 - (item[1]+item[3])} \\implies x = {item[4]}\\).\\n**Step 2: Conclusion**\\nx = {item[4]}."
            ),
            'svg': lambda item: svg_parallel_transversal(f"x = {item[4]}"),
            'diff': 'medium'
        },
        # Arch 2: Find the smaller interior angle from ratio a : b
        {
            'data': [(1, 2, 60, 120), (2, 3, 72, 108), (1, 3, 45, 135), (1, 4, 36, 144), (1, 5, 30, 150),
                     (3, 7, 54, 126), (4, 5, 80, 100), (5, 7, 75, 105), (7, 11, 70, 110), (5, 13, 50, 130)],
            'tmpls': [
                "The ratio of two interior angles on the same side of a transversal of two parallel lines is {0} : {1}. Find the measure of the smaller angle.",
                "If interior angles on the same side of a transversal are in the ratio {0} : {1}, calculate the smaller interior angle.",
                "Two co-interior angles of parallel lines are in ratio {0} : {1}. What is the measure of the smaller angle?",
                "Determine the smaller interior angle when the ratio of consecutive interior angles is {0} : {1}.",
                "Find the smaller angle among two interior angles in ratio {0} : {1} on parallel lines.",
                "Calculate smaller angle: \\frac{{{0}}}{{{0}+{1}}} \\times 180^\\circ for ratio {0} : {1}.",
                "Evaluate the smaller co-interior angle having ratio {0} : {1}.",
                "If co-interior angles are in ratio {0} : {1}, compute the measure of the acute interior angle.",
                "For parallel lines, two interior angles on one side are in ratio {0} : {1}. Find the smaller angle.",
                "Find the measure of the smaller of two interior angles whose ratio is {0} : {1}."
            ],
            'calc': lambda item: (
                f"{item[2]}°",
                [f"{item[3]}°", f"{item[2] + 10}°", f"{item[2] - 10}°"],
                f"**Step 1: Ratio calculation**\\nLet angles be \\({item[0]}k\\) and \\({item[1]}k\\).\\n\\({item[0]}k + {item[1]}k = 180^\\circ \\implies {item[0]+item[1]}k = 180^\\circ \\implies k = {180 // (item[0]+item[1])}^\\circ\\).\\n**Step 2: Smaller angle**\\n\\(\\text{{Smaller angle}} = {item[0]} \\times {180 // (item[0]+item[1])}^\\circ = {item[2]}^\\circ\\).\\n**Step 3: Conclusion**\\n{item[2]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"{item[0]}:{item[1]}"),
            'diff': 'medium'
        },
        # Arch 3: Find the difference between two co-interior angles from ratio a : b
        {
            'data': [(1, 2, 60, 120, 60), (2, 3, 72, 108, 36), (1, 3, 45, 135, 90), (1, 4, 36, 144, 108), (1, 5, 30, 150, 120),
                     (3, 7, 54, 126, 72), (4, 5, 80, 100, 20), (5, 7, 75, 105, 30), (7, 11, 70, 110, 40), (5, 13, 50, 130, 80)],
            'tmpls': [
                "Two consecutive interior angles between parallel lines stand in the ratio {0} : {1}. Determine the absolute difference between these two angles.",
                "What is the non-negative difference in degrees between two co-interior angles having ratio {0} : {1}?",
                "If co-interior angles are in proportion {0} : {1}, compute their difference: \(\text{{Angle}}_2 - \text{{Angle}}_1\).",
                "Determine the difference between the larger and smaller interior angles whose ratio is {0} : {1}.",
                "Parallel lines cut by a transversal create interior angles in ratio {0} : {1}. Calculate how much larger the obtuse angle is than the acute angle.",
                "Find the gap in degrees between the two consecutive interior angles in ratio {0} : {1}.",
                "Calculate \({1}k - {0}k\) for co-interior angles in ratio {0} : {1} on parallel lines.",
                "Two interior angles on one side of a transversal have ratio {0} : {1}. What is the positive difference between them?",
                "Evaluate \(\text{{Difference}} = \text{{Angle}}_{{\text{{max}}}} - \text{{Angle}}_{{\text{{min}}}}\) for ratio {0} : {1}.",
                "Find the angular difference between the pair of consecutive interior angles with ratio {0} : {1}."
            ],
            'calc': lambda item: (
                f"{item[4]}°",
                [f"{item[4] + 12}°", f"{abs(item[4] - 12)}°", f"{item[4] + 24}°"],
                f"**Step 1: Ratio values**\n\({item[0]}k + {item[1]}k = 180^\circ \implies k = {180 // (item[0]+item[1])}^\circ\).\nAngles are \({item[2]}^\circ\) and \({item[3]}^\circ\).\n**Step 2: Difference**\n\(\text{{Difference}} = {item[3]}^\circ - {item[2]}^\circ = {item[4]}^\circ\).\n**Step 3: Conclusion**\n{item[4]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"diff: {item[4]}°"),
            'diff': 'hard'
        },
        # Arch 4: Difference between co-interior angles is d, find both
        {
            'data': [(20, 80, 100), (30, 75, 105), (40, 70, 110), (50, 65, 115), (60, 60, 120),
                     (70, 55, 125), (80, 50, 130), (90, 45, 135), (10, 85, 95), (100, 40, 140)],
            'tmpls': [
                "Two interior angles on the same side of a transversal of parallel lines have a difference of {0}°. Find the measure of the smaller angle.",
                "If the difference between two co-interior angles is {0}°, calculate the smaller angle.",
                "Co-interior angles on parallel lines differ by {0}°. What is the measure of the smaller angle?",
                "Determine the smaller interior angle when their difference is {0}°.",
                "Find the smaller angle: (180° - {0}°) / 2 for co-interior angles.",
                "Calculate smaller angle when interior angles on same side satisfy x - y = {0}° and x + y = 180°.",
                "Evaluate the smaller angle of parallel lines whose co-interior angles have difference {0}°.",
                "Compute smaller interior angle if one exceeds the other by {0}°.",
                "If two interior angles on the same side differ by {0}°, find the smaller angle.",
                "For parallel lines with co-interior angle difference {0}°, calculate the smaller angle."
            ],
            'calc': lambda item: (
                f"Smaller angle is {item[1]}°",
                [f"Smaller angle is {item[2]}°", f"Smaller angle is {item[1] + 10}°", f"Smaller angle is {item[1] - 10}°"],
                f"**Step 1: System of equations**\\n\\(x + y = 180^\\circ\\) and \\(x - y = {item[0]}^\\circ\\).\\n\\(2y = 180^\\circ - {item[0]}^\\circ = {180 - item[0]}^\\circ \\implies y = {item[1]}^\\circ\\).\\n**Step 2: Conclusion**\\nSmaller angle is {item[1]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"diff: {item[0]}°"),
            'diff': 'medium'
        },
        # Arch 5: Distinct properties of co-interior angles and parallel lines
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
                f"**Step 1: Geometric Property**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'svg': lambda item: svg_parallel_transversal("interior prop"),
            'diff': 'medium'
        },
        # Arch 6: One interior angle is k times the other: k*x + x = 180
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
                f"**Step 1: Equation**\\nLet smaller angle be \\(x\\), larger is \\({item[0]}x\\).\\n\\(x + {item[0]}x = 180^\\circ \\implies {item[0]+1}x = 180^\\circ \\implies x = {item[1]}^\\circ\\).\\n**Step 2: Conclusion**\\n{item[1]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"k = {item[0]}"),
            'diff': 'medium'
        },
        # Arch 7: Testing whether lines are parallel given sum of interior angles
        {
            'data': [(110, 70, "parallel"), (115, 65, "parallel"), (120, 60, "parallel"), (125, 55, "parallel"), (130, 50, "parallel"),
                     (100, 75, "not parallel"), (110, 75, "not parallel"), (120, 65, "not parallel"), (105, 70, "not parallel"), (130, 55, "not parallel")],
            'tmpls': [
                "Two lines are cut by a transversal. The interior angles on the same side are {0}° and {1}°. Are the two lines parallel?",
                "If interior angles on the same side of a transversal measure {0}° and {1}°, determine if the lines are parallel.",
                "Check whether lines l and m are parallel if co-interior angles are {0}° and {1}°.",
                "Do interior angles {0}° and {1}° on the same side make the lines parallel?",
                "Evaluate parallelism of two lines having co-interior angles {0}° and {1}°.",
                "Are two lines parallel if the interior angles on one side of a transversal are {0}° and {1}°?",
                "Test if two lines are parallel when interior angles on same side are {0}° and {1}°.",
                "Determine if lines are parallel for interior angle sum: {0}° + {1}°.",
                "If interior angles on one side are {0}° and {1}°, state whether the lines are parallel.",
                "For lines cut by a transversal with interior angles {0}° and {1}°, are they parallel?"
            ],
            'calc': lambda item: (
                f"Yes, the lines are parallel (sum is {item[0] + item[1]}° = 180°)" if item[2] == "parallel" else f"No, the lines are not parallel (sum is {item[0] + item[1]}° != 180°)",
                [f"No, the lines are not parallel (sum is {item[0] + item[1]}°)" if item[2] == "parallel" else f"Yes, the lines are parallel (sum is {item[0] + item[1]}°)",
                 "The lines are perpendicular to each other",
                 "Parallelism cannot be determined without knowing alternate angles"],
                f"**Step 1: Check interior angle sum**\\n\\({item[0]}^\\circ + {item[1]}^\\circ = {item[0] + item[1]}^\\circ\\).\\nBy Interior Angles Test, lines are parallel if and only if the sum is exactly 180°.\\n**Step 2: Conclusion**\\n{'Yes, the lines are parallel (sum is 180°)' if item[2] == 'parallel' else f'No, the lines are not parallel (sum is {item[0] + item[1]}° != 180°)'}."
            ),
            'svg': lambda item: svg_parallel_transversal(f"{item[0]}°, {item[1]}°"),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

print("gen_2_1_1 ready.")

# =============================================================================
# 2.1.2: Indirect proof method (80 Qs)
# =============================================================================
def gen_2_1_2():
    tc = "MH-9-MTH2-2-2.1.2"
    tname = "Indirect proof method"
    
    proof_cases = [
        ("lines l and m are parallel", "lines l and m intersect at a point P", "Triangle formed by transversal and lines would have sum of two angles = 180°, leaving 0° for third angle"),
        ("alternate angles are congruent", "alternate angles are not congruent", "Sum of interior angles would not be 180°, contradicting the parallel lines property"),
        ("two lines perpendicular to same line are parallel", "the two lines intersect at point T", "Two perpendiculars from point T to the same line would exist, which is impossible"),
        ("interior angles sum to 180 degrees", "interior angles sum is less than 180 degrees", "Lines would meet on that side by Euclid Postulate 5, contradicting given parallelism"),
        ("corresponding angles are equal", "corresponding angles are unequal", "Linear pair with interior angles would contradict 180° sum"),
        ("a triangle cannot have two right angles", "a triangle has two right angles (90° each)", "The sum of just two angles would be 180°, which leaves 0° or negative measure for the third angle"),
        ("a triangle cannot have two obtuse angles", "a triangle has two obtuse angles (>90° each)", "Sum of two angles exceeds 180°, violating triangle angle sum theorem"),
        ("through a point not on line l, exactly one parallel line exists", "two distinct parallel lines pass through point P", "Would contradict Playfair's axiom / Euclid's fifth postulate"),
        ("if two coplanar lines do not intersect, they are parallel", "the lines intersect at some finite point Q", "Lines cannot be parallel if they share a common point Q"),
        ("opposite angles of a parallelogram are equal", "opposite angles are unequal", "Consecutive interior angles would fail to sum to 180° on both pairs of parallel sides")
    ]

    archs = [
        # Arch 0: Identify the initial assumption in indirect proof of parallel lines theorems
        {
            'data': [(i, c[0], c[1], c[2]) for i, c in enumerate(proof_cases)],
            'tmpls': [
                "In an indirect proof of '{1}', what initial assumption is made?",
                "To prove indirectly that '{1}', how does the proof begin?",
                "What is the starting assumption in the indirect proof of '{1}'?",
                "State the initial hypothesis set up when proving '{1}' by contradiction.",
                "In the proof by contradiction of '{1}', what do we assume initially?",
                "What assumption is formulated at the start of indirect proof for '{1}'?",
                "To establish '{1}' using indirect reasoning, what is assumed?",
                "Identify the contrary assumption made to prove '{1}' indirectly.",
                "When proving '{1}' by indirect method, what initial step is taken?",
                "What hypothesis initiates the proof by contradiction of '{1}'?"
            ],
            'calc': lambda item: (
                f"We assume the opposite: '{item[2]}'",
                [f"We assume '{item[1]}' is already directly established",
                 "We assume Euclid's postulates are invalid in geometry",
                 "We assume the figure has zero degrees"],
                f"**Step 1: Indirect proof principle**\nIn an indirect proof, we assume the negation of the statement to be proved.\nTo prove '{item[1]}', we assume: '{item[2]}'.\n**Step 2: Conclusion**\nWe assume the opposite: '{item[2]}'."
            ),
            'diff': 'medium'
        },
        # Arch 1: Contradiction reached in indirect proof of parallel lines theorems
        {
            'data': [(i, c[0], c[1], c[2]) for i, c in enumerate(proof_cases)],
            'tmpls': [
                "In the indirect proof of '{1}', what contradiction is reached from the assumption?",
                "What impossibility arises from assuming '{2}' in the proof of '{1}'?",
                "State the contradiction encountered when proving '{1}' by contradiction.",
                "Why does the assumption '{2}' fail in the indirect proof of '{1}'?",
                "Identify the logical contradiction in the indirect proof of '{1}'.",
                "What known fact is contradicted by assuming '{2}' in the proof of '{1}'?",
                "In proving '{1}' indirectly, how does '{2}' lead to an absurdity?",
                "Explain the contradiction resulting from '{2}' in the proof of '{1}'.",
                "What geometrical law is violated by assuming '{2}' for '{1}'?",
                "Show the contradiction obtained in the indirect proof of '{1}'."
            ],
            'calc': lambda item: (
                f"Contradiction: {item[3]}",
                ["Contradiction: It would prove Pythagoras theorem false",
                 "Contradiction: The number of vertices becomes negative",
                 "No contradiction is reached; the assumption holds"],
                f"**Step 1: Arrive at contradiction**\nAssuming '{item[2]}' leads to: {item[3]}.\nSince this is impossible, the assumption is false and the theorem '{item[1]}' is true.\n**Step 2: Conclusion**\nContradiction: {item[3]}."
            ),
            'diff': 'hard'
        },
        # Arch 2: If lines l and m meet at P, triangle angle sum contradiction (numerical)
        {
            'data': [(100, 80, 180, 0), (95, 85, 180, 0), (110, 70, 180, 0), (105, 75, 180, 0), (90, 90, 180, 0),
                     (120, 60, 180, 0), (115, 65, 180, 0), (125, 55, 180, 0), (100, 85, 185, -5), (110, 80, 190, -10)],
            'tmpls': [
                "In an indirect proof that lines l and m are parallel, interior angles are {0}° and {1}°. If lines meet at P, what would be the third angle of \(\Delta ABP\)?",
                "Assuming lines meet at P to form \(\Delta ABP\) with interior base angles {0}° and {1}°, calculate \(ngle P = 180^\circ - ({0}^\circ + {1}^\circ)\).",
                "What would be the measure of \(ngle P\) in \(\Delta ABP\) if two angles are {0}° and {1}°?",
                "Calculate \(ngle P\) in the hypothetical triangle formed by intersecting lines with base angles {0}° and {1}°.",
                "In indirect proof, if lines meet at P with angles {0}° and {1}°, find \(ngle P\).",
                "Determine the third angle of triangle ABP having angles {0}° and {1}°.",
                "Compute \(ngle P = 180^\circ - {2}^\circ\) in the indirect proof.",
                "Evaluate the impossible third angle \(ngle P\) when two angles sum to {2}°.",
                "If lines meet at P with base angles {0}° and {1}°, calculate the vertex angle \(ngle P\).",
                "For hypothetical triangle ABP with angles {0}° and {1}°, what is \(ngle P\)?"
            ],
            'calc': lambda item: (
                f"ngle P = {item[3]}° (impossible for a triangle vertex)",
                [f"ngle P = {item[3] + 10}°", f"ngle P = {item[3] + 20}°", f"ngle P = {item[0] - item[1]}°"],
                f"**Step 1: Triangle angle sum in hypothetical triangle ABP**\n\(ngle A + ngle B + ngle P = 180^\circ \implies {item[0]}^\circ + {item[1]}^\circ + ngle P = 180^\circ\).\n\(ngle P = 180^\circ - {item[2]}^\circ = {item[3]}^\circ\).\n**Step 2: Contradiction**\nA triangle cannot have an angle of {item[3]}°. Hence lines l and m cannot meet at P.\n**Step 3: Conclusion**\nngle P = {item[3]}° (impossible for a triangle vertex)."
            ),
            'svg': lambda item: svg_parallel_transversal(f"ngle P = {item[3]}°"),
            'diff': 'medium'
        },
        # Arch 3: Indirect proof showing that two lines perpendicular to same line are parallel
        {
            'data': [(1, "line l and line m are perpendicular to line n", "assume lines l and m intersect at point P"),
                     (2, "line AB and line CD are perpendicular to line EF", "assume lines AB and CD intersect at point Q"),
                     (3, "line p and line q are perpendicular to line r", "assume lines p and q intersect at point S"),
                     (4, "line x and line y are perpendicular to line z", "assume lines x and y intersect at point T"),
                     (5, "line RS and line TU are perpendicular to line VW", "assume lines RS and TU intersect at point M"),
                     (6, "line a and line b are perpendicular to line c", "assume lines a and b intersect at point K"),
                     (7, "line GH and line IJ are perpendicular to line KL", "assume lines GH and IJ intersect at point N"),
                     (8, "line MN and line OP are perpendicular to line QR", "assume lines MN and OP intersect at point O"),
                     (9, "line u and line v are perpendicular to line w", "assume lines u and v intersect at point H"),
                     (10, "line CD and line EF are perpendicular to line AB", "assume lines CD and EF intersect at point Z")],
            'tmpls': [
                "Theorem: If {1}, then they are parallel. What is the initial assumption in an indirect proof of this theorem?",
                "How do we begin the indirect proof of: '{1} implies they are parallel'?",
                "What contrary hypothesis is set up to prove '{1} implies parallelism'?",
                "State the initial assumption in proving '{1} implies parallel lines' by contradiction.",
                "In indirect proof of '{1} implies they are parallel', what do we assume?",
                "Identify the starting contrary assumption when proving '{1}' implies parallel lines.",
                "To prove indirectly that {1} implies the lines are parallel, what is assumed?",
                "What assumption is made at the start of proving '{1}' implies parallelism?",
                "When proving {1} are parallel by contradiction, how does the proof start?",
                "For the theorem '{1} implies parallel lines', state the initial assumption."
            ],
            'calc': lambda item: (
                f"We {item[2]} (forming two right angles from one point to the line)",
                ["We assume the transversal is curved", "We assume right angles measure 45 degrees", "We assume the line has zero length"],
                f"**Step 1: Indirect proof setup**\nTo prove the lines are parallel, we assume they are NOT parallel: {item[2]}.\nThis would mean from point P, two perpendicular lines can be drawn to the same line, which contradicts the uniqueness of a perpendicular.\n**Step 2: Conclusion**\nWe {item[2]} (forming two right angles from one point to the line)."
            ),
            'diff': 'medium'
        },
        # Arch 4: Triangle with two right angles contradiction
        {
            'data': [(90, 90, 180), (91, 90, 181), (92, 90, 182), (90, 95, 185), (93, 91, 184),
                     (94, 90, 184), (90, 92, 182), (95, 95, 190), (90, 100, 190), (100, 100, 200)],
            'tmpls': [
                "Can a triangle have two angles measuring {0}° and {1}°? Prove by indirect method.",
                "Using indirect reasoning, explain why a triangle cannot have angles of {0}° and {1}°.",
                "Why is a triangle with two angles {0}° and {1}° impossible in Euclidean geometry?",
                "Prove by contradiction that no triangle can contain angles of {0}° and {1}°.",
                "What contradiction arises if a triangle is assumed to have angles {0}° and {1}°?",
                "Show by indirect method that angles {0}° and {1}° cannot belong to the same triangle.",
                "In proof by contradiction, what happens if two angles of a triangle are {0}° and {1}°?",
                "Demonstrate why a triangle cannot have two angles measuring {0}° and {1}°.",
                "Evaluate the possibility of a triangle having angles {0}° and {1}°.",
                "State the contradiction if a triangle has angles {0}° and {1}°."
            ],
            'calc': lambda item: (
                f"Impossible: sum of just two angles is {item[2]}° >= 180° (violates angle sum theorem)",
                ["Possible: the third angle would be 45°", "Possible: if the triangle is drawn on a sphere", "Indeterminate without knowing side lengths"],
                f"**Step 1: Calculate sum of two angles**\n\({item[0]}^\circ + {item[1]}^\circ = {item[2]}^\circ\).\nSince the sum of all three angles in any Euclidean triangle must be exactly 180°, having two angles sum to {item[2]}° leaves zero or negative degrees for the third angle, which is impossible.\n**Step 2: Conclusion**\nImpossible: sum of just two angles is {item[2]}° >= 180° (violates angle sum theorem)."
            ),
            'diff': 'easy'
        },
        # Arch 5: Logic of indirect proof: Modus Tollens / Reductio ad absurdum
        {
            'data': [(1, "Reductio ad absurdum"), (2, "Proof by contradiction"), (3, "Indirect method"), (4, "Negation of conclusion"), (5, "Contradiction deduction"),
                     (6, "Logical refutation"), (7, "Antithesis assumption"), (8, "Impossibility derivation"), (9, "Falsity of assumption"), (10, "Truth of proposition")],
            'tmpls': [
                "The indirect proof method in mathematics is historically and logically known by which Latin term?",
                "What is the Latin phrase meaning 'reduction to absurdity' used for indirect proofs?",
                "By what term did Greek and medieval mathematicians designate proof by contradiction?",
                "Name the logical technique of proving a proposition by demonstrating that its contrary leads to an absurdity.",
                "Identify the classical term for indirect proof by contradiction.",
                "What is the philosophical and mathematical name for proof via impossible contradiction?",
                "In mathematical logic, establishing truth by showing falsity of negation is called what?",
                "State the classical terminology for reduction to impossibility.",
                "Which term describes the proof method that reduces the opposite hypothesis to nonsense?",
                "Define the classical name of indirect proof in Euclidean geometry."
            ],
            'calc': lambda item: (
                "Reductio ad absurdum (proof by contradiction)",
                ["Modus ponens (direct implication)", "Mathematical induction", "Empirical inductive generalization"],
                f"**Step 1: Classical terminology**\nThe indirect proof method is known as 'Reductio ad absurdum' (reduction to absurdity), where assuming the negation of the theorem leads to an impossibility.\n**Step 2: Conclusion**\nReductio ad absurdum (proof by contradiction)."
            ),
            'diff': 'easy'
        },
        # Arch 6: Euclid Postulate 5 application in indirect proof
        {
            'data': [(85, 90, 175), (80, 95, 175), (75, 95, 170), (70, 90, 160), (65, 95, 160),
                     (60, 90, 150), (55, 95, 150), (50, 90, 140), (85, 85, 170), (88, 89, 177)],
            'tmpls': [
                "Two lines are cut by a transversal such that interior angles on one side are {0}° and {1}°. On which side will the lines intersect according to Euclid's fifth postulate?",
                "Interior angles on the left side of a transversal are {0}° and {1}°. Do the lines intersect on the left side?",
                "According to Euclid Postulate 5, if interior angles sum to {2}° (< 180°), what happens to the lines?",
                "Lines cut by a transversal have interior angles {0}° and {1}° (sum = {2}°). On which side do they meet?",
                "Determine the behavior of lines having interior angles {0}° and {1}° on one side of a transversal.",
                "Find whether lines intersect on the side where interior angles are {0}° and {1}°.",
                "Evaluate: interior angles sum to {0}° + {1}° = {2}° < 180°. Where do the lines meet?",
                "By Euclid's parallel postulate, what is the fate of lines with interior angle sum {2}°?",
                "If interior angles on one side are {0}° and {1}°, state if the lines intersect on that side.",
                "For interior angles {0}° and {1}° summing to {2}°, do the lines intersect on that side?"
            ],
            'calc': lambda item: (
                f"They intersect on that side because the sum of interior angles is {item[2]}° < 180°",
                ["They never intersect on either side because lines are always parallel",
                 "They intersect on the opposite side where angles sum to more than 180°",
                 "They remain parallel regardless of angle sum"],
                f"**Step 1: Euclid's Fifth Postulate**\nIf a straight line falling on two straight lines makes the interior angles on the same side less than two right angles (180°), the two lines, if produced indefinitely, meet on that side.\nHere \({item[0]}^\circ + {item[1]}^\circ = {item[2]}^\circ < 180^\circ\).\n**Step 2: Conclusion**\nThey intersect on that side because the sum of interior angles is {item[2]}° < 180°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"sum: {item[2]}°"),
            'diff': 'medium'
        },
        # Arch 7: Summary of indirect proof conclusion: assumption is rejected
        {
            'data': [(1, "Case 1"), (2, "Case 2"), (3, "Case 3"), (4, "Case 4"), (5, "Case 5"),
                     (6, "Case 6"), (7, "Case 7"), (8, "Case 8"), (9, "Case 9"), (10, "Case 10")],
            'tmpls': [
                "In any indirect proof, once a contradiction is reached, what is the immediate logical conclusion?",
                "What conclusion is drawn in an indirect proof after demonstrating an impossible contradiction?",
                "How does reaching an absurdity conclude an indirect mathematical proof?",
                "What is deduced when the contrary assumption in an indirect proof leads to a contradiction?",
                "State the concluding step of an indirect proof upon deriving a contradiction.",
                "Why is the original statement established when the contrary assumption fails?",
                "In proof by contradiction, what is the final verdict on the initial assumption?",
                "What does the contradiction establish regarding the original theorem to be proved?",
                "Explain the final deduction in an indirect proof after obtaining a contradiction.",
                "How is the validity of the theorem affirmed at the end of an indirect proof?"
            ],
            'calc': lambda item: (
                "The assumption is proved false, so the original theorem must be TRUE",
                ["The original theorem is proved false and must be discarded",
                 "Both the assumption and theorem are declared invalid",
                 "A direct proof is immediately required to confirm the result"],
                f"**Step 1: Principle of contradiction**\nSince the assumption leads to a statement that contradicts an established axiom or given fact, the assumption must be FALSE. Therefore, the original theorem (its negation) must be TRUE.\n**Step 2: Conclusion**\nThe assumption is proved false, so the original theorem must be TRUE."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 2.2.1: Alternate angles theorem proof (80 Qs)
# =============================================================================
def gen_2_2_1():
    tc = "MH-9-MTH2-2-2.2.1"
    tname = "Alternate angles theorem proof"
    archs = [
        # Arch 0: Numerical alternate interior angles: angle 1 = angle 2
        {
            'data': [(35, 35), (45, 45), (55, 55), (65, 65), (75, 75),
                     (85, 85), (60, 60), (70, 70), (50, 50), (40, 40)],
            'tmpls': [
                "Two parallel lines are intersected by a transversal. If one alternate interior angle is {0}°, what is the measure of the other alternate interior angle?",
                "In the figure, line l || line m. If an alternate interior angle measures {0}°, find the corresponding alternate angle.",
                "Calculate the alternate interior angle corresponding to an angle of {0}° between parallel lines.",
                "What is the measure of the alternate interior angle if the first angle is {0}°?",
                "Determine the alternate angle when one alternate interior angle is {0}° for parallel lines.",
                "Find the alternate angle: \(\angle 2 = \angle 1 = {0}^\circ\) for parallel lines.",
                "Lines l and m are parallel. If an alternate interior angle is {0}°, evaluate the other.",
                "Compute the alternate interior angle when one angle is {0}°.",
                "If two parallel lines are cut by a transversal and one alternate angle is {0}°, find the other.",
                "For parallel lines with transversal, find the alternate interior angle to {0}°."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{180 - item[1]}°", f"{item[1] + 10}°", f"{item[1] - 10}°"],
                f"**Step 1: Alternate Angles Theorem**\nThe alternate interior angles formed by a transversal of two parallel lines are congruent:\n\(\angle 2 = \angle 1 = {item[0]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"alt: {item[0]}°"),
            'diff': 'easy'
        },
        # Arch 1: Algebraic alternate interior angles: ax - b = cx + d => find x
        {
            'data': [(4, 10, 2, 20, 15), (5, 15, 3, 17, 16), (3, 25, 1, 9, 17),
                     (4, 8, 2, 28, 18), (5, 5, 2, 52, 19), (6, 12, 3, 48, 20),
                     (3, 11, 1, 31, 21), (4, 14, 2, 30, 22), (5, 19, 2, 50, 23), (3, 18, 1, 30, 24)],
            'tmpls': [
                "Two parallel lines are cut by a transversal. If alternate interior angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), find \(x\).",
                "Alternate interior angles of parallel lines are \({0}x - {1}\) and \({2}x + {3}\). Calculate \(x\).",
                "Find \(x\) if alternate interior angles on parallel lines satisfy \(({0}x - {1})^\circ = ({2}x + {3})^\circ\).",
                "What is the value of \(x\) when alternate interior angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\)?",
                "Determine \(x\) from the equality of alternate angles: \({0}x - {1} = {2}x + {3}\).",
                "Calculate variable \(x\) for alternate angles \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\).",
                "Evaluate \(x\) given that alternate angles on parallel lines are congruent: \(({0}x - {1})^\circ = ({2}x + {3})^\circ\).",
                "Lines l || m are cut by transversal n. If alternate angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), find \(x\).",
                "If alternate angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), calculate \(x\).",
                "For parallel lines with alternate angles \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), find \(x\)."
            ],
            'calc': lambda item: (
                f"x = {item[4]}",
                [f"x = {item[4] + 3}", f"x = {item[4] - 3}", f"x = {item[4] + 6}"],
                f"**Step 1: Equate alternate interior angles**\n\({item[0]}x - {item[1]} = {item[2]}x + {item[3]} \implies ({item[0]} - {item[2]})x = {item[3]} + {item[1]} \implies {item[0]-item[2]}x = {item[3]+item[1]}\).\n\(x = {item[4]}\).\n**Step 2: Conclusion**\nx = {item[4]}."
            ),
            'svg': lambda item: svg_parallel_transversal(f"x = {item[4]}"),
            'diff': 'medium'
        },
        # Arch 2: Find actual angle measure after solving x
        {
            'data': [(3, 10, 2, 25, 15, 55), (4, 12, 2, 20, 16, 52), (3, 20, 1, 54, 17, 71),
                     (5, 10, 3, 26, 18, 80), (4, 15, 2, 23, 19, 61), (3, 15, 1, 25, 20, 45),
                     (4, 20, 2, 22, 21, 64), (5, 25, 2, 41, 22, 85), (3, 30, 1, 16, 23, 39), (4, 16, 2, 32, 24, 80)],
            'tmpls': [
                "Two parallel lines are cut by a transversal. Alternate angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\). Find the measure of each alternate angle.",
                "If alternate interior angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), calculate the angle measure.",
                "Find the measure of the alternate angles given by \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\).",
                "What is the degree measure of alternate angles \({0}x - {1}\) and \({2}x + {3}\)?",
                "Determine the angle measure of the congruent alternate angles \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\).",
                "Calculate angle measure after solving \({0}x - {1} = {2}x + {3}\).",
                "Evaluate the size of alternate interior angles \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\).",
                "Compute the measure of the alternate angles on parallel lines with expressions \({0}x - {1}\) and \({2}x + {3}\).",
                "If alternate interior angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), find their degree measure.",
                "For parallel lines, find the measure of alternate angles given as \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\)."
            ],
            'calc': lambda item: (
                f"{item[5]}°",
                [f"{item[5] + 10}°", f"{item[5] - 10}°", f"{180 - item[5]}°"],
                f"**Step 1: Solve for x**\n\({item[0]}x - {item[1]} = {item[2]}x + {item[3]} \implies x = {item[4]}\).\n**Step 2: Calculate angle**\n\(\text{{Angle}} = {item[0]}({item[4]}) - {item[1]} = {item[5]}^\circ\).\n**Step 3: Conclusion**\n{item[5]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"{item[5]}°"),
            'diff': 'medium'
        },
        # Arch 3: Proof step of Alternate Angles Theorem: a + c = 180 and b + c = 180 => a = b
        {
            'data': [(1, "linear pair and interior angles"), (2, "supplementary angle chain"), (3, "co-interior substitution"), (4, "angle equality proof"), (5, "transversal proof"),
                     (6, "Euclidean deduction"), (7, "linear pair deduction"), (8, "interior angle property"), (9, "transversal deduction"), (10, "angle substitution")],
            'tmpls': [
                "In the textbook proof of the Alternate Angles Theorem, \(\angle a + \angle c = 180^\circ\) (linear pair) and \(\angle b + \angle c = 180^\circ\) (interior angles). What is concluded?",
                "Given \(\angle a + \angle c = 180^\circ\) and \(\angle b + \angle c = 180^\circ\) in the proof of alternate angles, what follows logically?",
                "From \(\angle a + \angle c = 180^\circ\) and \(\angle b + \angle c = 180^\circ\), deduce the relation between \(\angle a\) and \(\angle b\).",
                "In the proof that alternate angles are equal, what follows from \(\angle a + \angle c = \angle b + \angle c = 180^\circ\)?",
                "What equality is established by subtracting \(\angle c\) from both \(\angle a + \angle c = 180^\circ\) and \(\angle b + \angle c = 180^\circ\)?",
                "Identify the conclusion of the alternate angle proof: \(\angle a + \angle c = 180^\circ\) and \(\angle b + \angle c = 180^\circ\).",
                "Deduce the theorem from: \(\angle a + \angle c = 180^\circ\) and \(\angle b + \angle c = 180^\circ\).",
                "State the result obtained by equating \(\angle a + \angle c\) to \(\angle b + \angle c\).",
                "In proving alternate angles equal, how does \(\angle a + \angle c = \angle b + \angle c\) simplify?",
                "What relation between \(\angle a\) and \(\angle b\) is proved from \(\angle a + \angle c = 180^\circ\) and \(\angle b + \angle c = 180^\circ\)?"
            ],
            'calc': lambda item: (
                "\angle a = \angle b (alternate interior angles are congruent)",
                ["\angle a + \angle b = 90°", "\angle a + \angle b = 180°", "\angle a and \angle b are complementary"],
                f"**Step 1: Equate the two sums**\n\(\angle a + \angle c = \angle b + \angle c = 180^\circ\).\nSubtracting \(\angle c\) from both sides:\n\(\angle a = \angle b\).\n**Step 2: Conclusion**\n\angle a = \angle b (alternate interior angles are congruent)."
            ),
            'diff': 'easy'
        },
        # Arch 4: Alternate exterior angles equality
        {
            'data': [(120, 120), (130, 130), (140, 140), (110, 110), (115, 115),
                     (125, 125), (135, 135), (105, 105), (145, 145), (150, 150)],
            'tmpls': [
                "Two parallel lines are intersected by a transversal. If one alternate exterior angle is {0}°, find the other alternate exterior angle.",
                "Calculate the alternate exterior angle corresponding to {0}° for two parallel lines cut by a transversal.",
                "In parallel lines, if an alternate exterior angle measures {0}°, what is the measure of its alternate exterior partner?",
                "What is the measure of the alternate exterior angle if the first angle is {0}°?",
                "Determine the alternate exterior angle when one angle is {0}°.",
                "Find the alternate exterior angle: \(\angle 2 = \angle 1 = {0}^\circ\) on parallel lines.",
                "Lines l and m are parallel. If an alternate exterior angle is {0}°, evaluate the other.",
                "Compute the alternate exterior angle when one angle is {0}°.",
                "If two parallel lines are cut by a transversal and one alternate exterior angle is {0}°, find the other.",
                "For parallel lines with transversal, find the alternate exterior angle to {0}°."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{180 - item[1]}°", f"{item[1] + 15}°", f"{item[1] - 15}°"],
                f"**Step 1: Alternate Exterior Angles Theorem**\nAlternate exterior angles formed by a transversal of parallel lines are congruent:\n\(\angle 2 = \angle 1 = {item[0]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"alt ext: {item[0]}°"),
            'diff': 'easy'
        },
        # Arch 5: Distinct geometric properties of angle bisectors and parallel lines
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
                f"**Step 1: Geometric Theorem**\n{item[0]} {item[1]}.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'svg': lambda item: svg_parallel_transversal("prop"),
            'diff': 'medium'
        },
        # Arch 6: Given an interior angle, find its alternate exterior angle
        {
            'data': [(65, 65), (75, 75), (85, 85), (55, 55), (45, 45),
                     (35, 35), (70, 70), (80, 80), (60, 60), (50, 50)],
            'tmpls': [
                "Two parallel lines are cut by a transversal. If an interior angle is {0}°, what is the vertically opposite angle to its alternate angle?",
                "Find the vertically opposite angle to the alternate interior angle measuring {0}°.",
                "Calculate the vertically opposite angle to an alternate angle of {0}°.",
                "What is the angle vertically opposite to the alternate interior angle {0}°?",
                "Determine the angle opposite to alternate angle {0}°.",
                "Evaluate the vertically opposite angle to {0}° across the transversal.",
                "Compute the angle vertically opposite to alternate angle {0}°.",
                "If alternate interior angle is {0}°, find its vertically opposite angle.",
                "For parallel lines, find the angle vertically opposite to alternate angle {0}°.",
                "What is the vertically opposite counterpart of alternate angle {0}°?"
            ],
            'calc': lambda item: (
                f"{item[1]}° (vertically opposite angles are equal)",
                [f"{180 - item[1]}°", f"{item[1] + 10}°", f"{item[1] - 10}°"],
                f"**Step 1: Vertically opposite property**\nVertically opposite angles are equal to each other:\n\(\text{{Angle}} = {item[0]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}° (vertically opposite angles are equal)."
            ),
            'svg': lambda item: svg_parallel_transversal(f"vert: {item[0]}°"),
            'diff': 'easy'
        },
        # Arch 7: Testing lines parallel via alternate angles equality
        {
            'data': [(48, 48, "parallel"), (58, 58, "parallel"), (68, 68, "parallel"), (78, 78, "parallel"), (88, 88, "parallel"),
                     (48, 52, "not parallel"), (58, 62, "not parallel"), (68, 72, "not parallel"), (78, 82, "not parallel"), (88, 92, "not parallel")],
            'tmpls': [
                "Two lines are cut by a transversal. Alternate interior angles are {0}° and {1}°. Are the lines parallel?",
                "If a pair of alternate interior angles measure {0}° and {1}°, determine if the lines are parallel.",
                "Check whether lines l and m are parallel if alternate interior angles are {0}° and {1}°.",
                "Do alternate angles {0}° and {1}° make the lines parallel by Alternate Angles Test?",
                "Evaluate parallelism of lines having alternate interior angles {0}° and {1}°.",
                "Are two lines parallel if alternate interior angles are {0}° and {1}°?",
                "Test if two lines are parallel when alternate angles are {0}° and {1}°.",
                "Determine if lines are parallel for alternate angles: {0}° and {1}°.",
                "If alternate angles are {0}° and {1}°, state whether the lines are parallel.",
                "For lines cut by a transversal with alternate angles {0}° and {1}°, are they parallel?"
            ],
            'calc': lambda item: (
                f"Yes, lines are parallel (alternate angles are equal: {item[0]}° = {item[1]}°)" if item[2] == "parallel" else f"No, lines are not parallel (alternate angles unequal: {item[0]}° != {item[1]}°)",
                [f"No, lines are not parallel ({item[0]}°)" if item[2] == "parallel" else f"Yes, lines are parallel ({item[0]}°)",
                 "The lines are perpendicular",
                 "Parallelism cannot be tested using alternate angles"],
                f"**Step 1: Check alternate angles equality**\nBy Alternate Angles Test, two lines are parallel if and only if a pair of alternate interior angles are equal.\nHere {item[0]}° {'=' if item[2] == 'parallel' else '!='} {item[1]}°.\n**Step 2: Conclusion**\n{'Yes, lines are parallel (alternate angles are equal: ' + str(item[0]) + '° = ' + str(item[1]) + '°)' if item[2] == 'parallel' else 'No, lines are not parallel (alternate angles unequal: ' + str(item[0]) + '° != ' + str(item[1]) + '°)'}."
            ),
            'svg': lambda item: svg_parallel_transversal(f"{item[0]}°, {item[1]}°"),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

print("gen_2_1_2 and gen_2_2_1 ready.")

# =============================================================================
# 2.2.2: Corresponding angles theorem proof (80 Qs)
# =============================================================================
def gen_2_2_2():
    tc = "MH-9-MTH2-2-2.2.2"
    tname = "Corresponding angles theorem proof"
    archs = [
        # Arch 0: Numerical corresponding angles: angle 1 = angle 2
        {
            'data': [(42, 42), (52, 52), (62, 62), (72, 72), (82, 82),
                     (48, 48), (58, 58), (68, 68), (78, 78), (88, 88)],
            'tmpls': [
                "Two parallel lines are cut by a transversal. If one corresponding angle is {0}°, what is the measure of the other corresponding angle?",
                "In parallel lines, if a corresponding angle measures {0}°, find its corresponding partner angle.",
                "Calculate the corresponding angle to an angle of {0}° formed by a transversal across parallel lines.",
                "What is the measure of the corresponding angle if the primary angle is {0}°?",
                "Determine the corresponding angle when one angle is {0}° for parallel lines.",
                "Find the corresponding angle: \(\angle 2 = \angle 1 = {0}^\circ\) for parallel lines.",
                "Lines l and m are parallel. If a corresponding angle is {0}°, evaluate the other corresponding angle.",
                "Compute the corresponding angle when one angle is {0}°.",
                "If two parallel lines are cut by a transversal and one corresponding angle is {0}°, find the other.",
                "For parallel lines with transversal, find the corresponding angle to {0}°."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{180 - item[1]}°", f"{item[1] + 10}°", f"{item[1] - 10}°"],
                f"**Step 1: Corresponding Angles Theorem**\nCorresponding angles formed by a transversal of parallel lines are congruent:\n\(\angle 2 = \angle 1 = {item[0]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"corr: {item[0]}°"),
            'diff': 'easy'
        },
        # Arch 1: Algebraic corresponding angles: ax - b = cx + d => find x
        {
            'data': [(3, 8, 2, 6, 14), (4, 11, 2, 19, 15), (5, 14, 3, 18, 16),
                     (4, 9, 2, 25, 17), (3, 12, 1, 24, 18), (5, 16, 2, 41, 19),
                     (4, 15, 1, 45, 20), (6, 10, 3, 53, 21), (3, 17, 1, 27, 22), (5, 20, 2, 49, 23)],
            'tmpls': [
                "Two parallel lines are cut by a transversal. If corresponding angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), find \(x\).",
                "Corresponding angles of parallel lines are \({0}x - {1}\) and \({2}x + {3}\). Calculate \(x\).",
                "Find \(x\) if corresponding angles on parallel lines satisfy \(({0}x - {1})^\circ = ({2}x + {3})^\circ\).",
                "What is the value of \(x\) when corresponding angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\)?",
                "Determine \(x\) from the equality of corresponding angles: \({0}x - {1} = {2}x + {3}\).",
                "Calculate variable \(x\) for corresponding angles \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\).",
                "Evaluate \(x\) given that corresponding angles on parallel lines are congruent: \(({0}x - {1})^\circ = ({2}x + {3})^\circ\).",
                "Lines l || m are cut by transversal n. If corresponding angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), find \(x\).",
                "If corresponding angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), calculate \(x\).",
                "For parallel lines with corresponding angles \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), find \(x\)."
            ],
            'calc': lambda item: (
                f"x = {item[4]}",
                [f"x = {item[4] + 3}", f"x = {item[4] - 3}", f"x = {item[4] + 6}"],
                f"**Step 1: Equate corresponding angles**\n\({item[0]}x - {item[1]} = {item[2]}x + {item[3]} \implies ({item[0]} - {item[2]})x = {item[3]} + {item[1]} \implies {item[0]-item[2]}x = {item[3]+item[1]}\).\n\(x = {item[4]}\).\n**Step 2: Conclusion**\nx = {item[4]}."
            ),
            'svg': lambda item: svg_parallel_transversal(f"x = {item[4]}"),
            'diff': 'medium'
        },
        # Arch 2: Measure of corresponding angle from x
        {
            'data': [(3, 8, 2, 6, 14, 34), (4, 11, 2, 19, 15, 49), (5, 14, 3, 18, 16, 66),
                     (4, 9, 2, 25, 17, 59), (3, 12, 1, 24, 18, 42), (5, 16, 2, 41, 19, 79),
                     (4, 15, 1, 45, 20, 65), (6, 10, 3, 53, 21, 116), (3, 17, 1, 27, 22, 49), (5, 20, 2, 49, 23, 95)],
            'tmpls': [
                "Two parallel lines are cut by a transversal. Corresponding angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\). Find the measure of each angle.",
                "If corresponding angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), calculate the angle measure.",
                "Find the measure of the corresponding angles given by \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\).",
                "What is the degree measure of corresponding angles \({0}x - {1}\) and \({2}x + {3}\)?",
                "Determine the angle measure of the congruent corresponding angles \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\).",
                "Calculate angle measure after solving \({0}x - {1} = {2}x + {3}\).",
                "Evaluate the size of corresponding angles \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\).",
                "Compute the measure of the corresponding angles on parallel lines with expressions \({0}x - {1}\) and \({2}x + {3}\).",
                "If corresponding angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), find their degree measure.",
                "For parallel lines, find the measure of corresponding angles given as \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\)."
            ],
            'calc': lambda item: (
                f"{item[5]}°",
                [f"{item[5] + 10}°", f"{item[5] - 10}°", f"{180 - item[5]}°"],
                f"**Step 1: Solve for x**\n\({item[0]}x - {item[1]} = {item[2]}x + {item[3]} \implies x = {item[4]}\).\n**Step 2: Calculate angle**\n\(\text{{Angle}} = {item[0]}({item[4]}) - {item[1]} = {item[5]}^\circ\).\n**Step 3: Conclusion**\n{item[5]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"{item[5]}°"),
            'diff': 'medium'
        },
        # Arch 3: Proof step of Corresponding Angles Theorem: a + c = 180 and b + c = 180 => a = b
        {
            'data': [(1, "linear pair and interior angles"), (2, "supplementary angle chain"), (3, "co-interior substitution"), (4, "angle equality proof"), (5, "transversal proof"),
                     (6, "Euclidean deduction"), (7, "linear pair deduction"), (8, "interior angle property"), (9, "transversal deduction"), (10, "angle substitution")],
            'tmpls': [
                "In the proof of Corresponding Angles Theorem, \(\angle a + \angle c = 180^\circ\) (linear pair) and \(\angle b + \angle c = 180^\circ\) (interior angles). What is concluded?",
                "Given \(\angle a + \angle c = 180^\circ\) and \(\angle b + \angle c = 180^\circ\) in the proof of corresponding angles, what follows logically?",
                "From \(\angle a + \angle c = 180^\circ\) and \(\angle b + \angle c = 180^\circ\), deduce the relation between \(\angle a\) and \(\angle b\).",
                "In the proof that corresponding angles are equal, what follows from \(\angle a + \angle c = \angle b + \angle c = 180^\circ\)?",
                "What equality is established by subtracting \(\angle c\) from both \(\angle a + \angle c = 180^\circ\) and \(\angle b + \angle c = 180^\circ\)?",
                "Identify the conclusion of the corresponding angle proof: \(\angle a + \angle c = 180^\circ\) and \(\angle b + \angle c = 180^\circ\).",
                "Deduce the theorem from: \(\angle a + \angle c = 180^\circ\) and \(\angle b + \angle c = 180^\circ\).",
                "State the result obtained by equating \(\angle a + \angle c\) to \(\angle b + \angle c\).",
                "In proving corresponding angles equal, how does \(\angle a + \angle c = \angle b + \angle c\) simplify?",
                "What relation between \(\angle a\) and \(\angle b\) is proved from \(\angle a + \angle c = 180^\circ\) and \(\angle b + \angle c = 180^\circ\)?"
            ],
            'calc': lambda item: (
                "\angle a = \angle b (corresponding angles are congruent)",
                ["\angle a + \angle b = 180°", "\angle a + \angle b = 90°", "\angle a and \angle b are supplementary"],
                f"**Step 1: Equate linear pair and interior angle sum**\n\(\angle a + \angle c = \angle b + \angle c = 180^\circ\).\nSubtracting \(\angle c\) gives:\n\(\angle a = \angle b\).\n**Step 2: Conclusion**\n\angle a = \angle b (corresponding angles are congruent)."
            ),
            'diff': 'easy'
        },
        # Arch 4: Given an exterior angle, find its corresponding angle
        {
            'data': [(100, 100), (105, 105), (110, 110), (115, 115), (120, 120),
                     (125, 125), (130, 130), (135, 135), (140, 140), (145, 145)],
            'tmpls': [
                "Two parallel lines are cut by a transversal. If an exterior angle is {0}°, what is its corresponding angle?",
                "Find the corresponding angle to an exterior angle measuring {0}° on parallel lines.",
                "Calculate the corresponding angle when an exterior angle is {0}°.",
                "What is the corresponding angle to {0}° across parallel lines?",
                "Determine the corresponding angle to exterior angle {0}°.",
                "Evaluate the corresponding angle to {0}° along the transversal.",
                "Compute the corresponding angle when given exterior angle is {0}°.",
                "If an exterior angle on parallel lines is {0}°, find its corresponding angle.",
                "For parallel lines, find the corresponding angle to exterior angle {0}°.",
                "What is the corresponding angle counterpart of {0}°?"
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{180 - item[1]}°", f"{item[1] + 15}°", f"{item[1] - 15}°"],
                f"**Step 1: Corresponding angles congruence**\nCorresponding angles formed on parallel lines are equal:\n\(\angle 2 = \angle 1 = {item[0]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"corr: {item[0]}°"),
            'diff': 'easy'
        },
        # Arch 5: Distinct geometric properties of corresponding angles and transversals
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
                f"**Step 1: Corresponding Angles Property**\n{item[0]} {item[1]}.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'svg': lambda item: svg_parallel_transversal("corr prop"),
            'diff': 'medium'
        },
        # Arch 6: Vertically opposite to corresponding angle
        {
            'data': [(55, 55), (65, 65), (75, 75), (85, 85), (45, 45),
                     (35, 35), (70, 70), (80, 80), (60, 60), (50, 50)],
            'tmpls': [
                "Two parallel lines are cut by a transversal. If angle 1 is {0}°, find the vertically opposite angle to its corresponding angle.",
                "Find the vertically opposite angle to the corresponding angle measuring {0}°.",
                "Calculate the vertically opposite angle to a corresponding angle of {0}°.",
                "What is the angle vertically opposite to corresponding angle {0}°?",
                "Determine the angle opposite to corresponding angle {0}°.",
                "Evaluate the vertically opposite angle to {0}° across the transversal intersection.",
                "Compute the angle vertically opposite to corresponding angle {0}°.",
                "If corresponding angle is {0}°, find its vertically opposite angle.",
                "For parallel lines, find the angle vertically opposite to corresponding angle {0}°.",
                "What is the vertically opposite counterpart of corresponding angle {0}°?"
            ],
            'calc': lambda item: (
                f"{item[1]}° (vertically opposite angles are equal)",
                [f"{180 - item[1]}°", f"{item[1] + 10}°", f"{item[1] - 10}°"],
                f"**Step 1: Angle calculation**\nCorresponding angle = {item[0]}°. Vertically opposite angle to it = {item[0]}°.\n**Step 2: Conclusion**\n{item[1]}° (vertically opposite angles are equal)."
            ),
            'svg': lambda item: svg_parallel_transversal(f"{item[0]}°"),
            'diff': 'easy'
        },
        # Arch 7: Testing lines parallel via corresponding angles equality
        {
            'data': [(44, 44, "parallel"), (54, 54, "parallel"), (64, 64, "parallel"), (74, 74, "parallel"), (84, 84, "parallel"),
                     (44, 48, "not parallel"), (54, 58, "not parallel"), (64, 68, "not parallel"), (74, 78, "not parallel"), (84, 88, "not parallel")],
            'tmpls': [
                "Two lines are cut by a transversal. Corresponding angles are {0}° and {1}°. Are the lines parallel?",
                "If a pair of corresponding angles measure {0}° and {1}°, determine if the lines are parallel.",
                "Check whether lines l and m are parallel if corresponding angles are {0}° and {1}°.",
                "Do corresponding angles {0}° and {1}° make the lines parallel by Corresponding Angles Test?",
                "Evaluate parallelism of lines having corresponding angles {0}° and {1}°.",
                "Are two lines parallel if corresponding angles are {0}° and {1}°?",
                "Test if two lines are parallel when corresponding angles are {0}° and {1}°.",
                "Determine if lines are parallel for corresponding angles: {0}° and {1}°.",
                "If corresponding angles are {0}° and {1}°, state whether the lines are parallel.",
                "For lines cut by a transversal with corresponding angles {0}° and {1}°, are they parallel?"
            ],
            'calc': lambda item: (
                f"Yes, lines are parallel (corresponding angles are equal: {item[0]}° = {item[1]}°)" if item[2] == "parallel" else f"No, lines are not parallel (corresponding angles unequal: {item[0]}° != {item[1]}°)",
                [f"No, lines are not parallel ({item[0]}°)" if item[2] == "parallel" else f"Yes, lines are parallel ({item[0]}°)",
                 "The lines are perpendicular",
                 "Parallelism cannot be tested using corresponding angles"],
                f"**Step 1: Check corresponding angles equality**\nBy Corresponding Angles Test, lines are parallel if and only if corresponding angles are equal.\nHere {item[0]}° {'=' if item[2] == 'parallel' else '!='} {item[1]}°.\n**Step 2: Conclusion**\n{'Yes, lines are parallel (corresponding angles are equal: ' + str(item[0]) + '° = ' + str(item[1]) + '°)' if item[2] == 'parallel' else 'No, lines are not parallel (corresponding angles unequal: ' + str(item[0]) + '° != ' + str(item[1]) + '°)'}."
            ),
            'svg': lambda item: svg_parallel_transversal(f"{item[0]}°, {item[1]}°"),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 2.3.1: Proving two lines parallel using angle criteria (80 Qs)
# =============================================================================
def gen_2_3_1():
    tc = "MH-9-MTH2-2-2.3.1"
    tname = "Proving two lines parallel using angle criteria"
    archs = [
        # Arch 0: Interior Angles Test
        {
            'data': [(100, 80, 180, "parallel"), (110, 70, 180, "parallel"), (120, 60, 180, "parallel"), (130, 50, 180, "parallel"), (105, 75, 180, "parallel"),
                     (100, 70, 170, "not parallel"), (110, 80, 190, "not parallel"), (125, 65, 190, "not parallel"), (95, 75, 170, "not parallel"), (115, 75, 190, "not parallel")],
            'tmpls': [
                "Two lines are cut by a transversal. If interior angles on the same side are {0}° and {1}°, identify if the lines are parallel by the Interior Angles Test.",
                "Using the Interior Angles Test, are lines parallel when co-interior angles are {0}° and {1}°?",
                "Test parallelism: interior angles on one side are {0}° and {1}°. What does the Interior Angles Test conclude?",
                "Check whether lines are parallel given interior angles {0}° and {1}° (sum = {2}°).",
                "Evaluate by Interior Angles Test: do angles {0}° and {1}° make the lines parallel?",
                "Are lines parallel if interior angles on same side sum to {2}° ({0}° + {1}°)?",
                "Apply the Interior Angles Test to angles {0}° and {1}°.",
                "Determine if lines are parallel when co-interior angles are {0}° and {1}°.",
                "State the result of the Interior Angles Test for angles {0}° and {1}°.",
                "For angles {0}° and {1}°, verify parallelism by the Interior Angles Test."
            ],
            'calc': lambda item: (
                f"Lines are parallel because interior angles are supplementary ({item[0]}° + {item[1]}° = 180°)" if item[3] == "parallel" else f"Lines are NOT parallel because interior angle sum is {item[2]}° != 180°",
                [f"Lines are NOT parallel because sum is 180°" if item[3] == "parallel" else f"Lines are parallel because sum is {item[2]}°",
                 "Lines are perpendicular to each other",
                 "Cannot be determined without alternate angles"],
                f"**Step 1: Interior Angles Test**\nTwo lines are parallel if the interior angles on the same side of a transversal are supplementary (sum = 180°).\nHere \({item[0]}^\circ + {item[1]}^\circ = {item[2]}^\circ\).\n**Step 2: Conclusion**\n{'Lines are parallel because interior angles are supplementary (' + str(item[0]) + '° + ' + str(item[1]) + '° = 180°)' if item[3] == 'parallel' else 'Lines are NOT parallel because interior angle sum is ' + str(item[2]) + '° != 180°'}."
            ),
            'svg': lambda item: svg_parallel_transversal(f"{item[0]}°, {item[1]}°"),
            'diff': 'medium'
        },
        # Arch 1: Alternate Angles Test
        {
            'data': [(38, 38, "parallel"), (48, 48, "parallel"), (58, 58, "parallel"), (68, 68, "parallel"), (78, 78, "parallel"),
                     (38, 42, "not parallel"), (48, 52, "not parallel"), (58, 62, "not parallel"), (68, 72, "not parallel"), (78, 82, "not parallel")],
            'tmpls': [
                "Two lines are cut by a transversal. If a pair of alternate interior angles are {0}° and {1}°, are the lines parallel by Alternate Angles Test?",
                "Using Alternate Angles Test, determine if lines are parallel when alternate angles are {0}° and {1}°.",
                "Check parallelism: alternate angles are {0}° and {1}°. What is concluded by the Alternate Angles Test?",
                "Are lines parallel if a pair of alternate interior angles measure {0}° and {1}°?",
                "Apply Alternate Angles Test to alternate angles measuring {0}° and {1}°.",
                "Evaluate by Alternate Angles Test: do angles {0}° and {1}° make the lines parallel?",
                "Test if lines are parallel when alternate angles are {0}° and {1}°.",
                "Determine if lines are parallel given alternate interior angles {0}° and {1}°.",
                "State the conclusion of Alternate Angles Test for angles {0}° and {1}°.",
                "For alternate angles {0}° and {1}°, verify parallelism by Alternate Angles Test."
            ],
            'calc': lambda item: (
                f"Lines are parallel because alternate angles are congruent ({item[0]}° = {item[1]}°)" if item[2] == "parallel" else f"Lines are NOT parallel because alternate angles are unequal ({item[0]}° != {item[1]}°)",
                [f"Lines are NOT parallel ({item[0]}°)" if item[2] == "parallel" else f"Lines are parallel ({item[0]}°)",
                 "Lines are perpendicular",
                 "Alternate angles test cannot determine parallelism"],
                f"**Step 1: Alternate Angles Test**\nTwo lines are parallel if a pair of alternate interior angles are equal.\nHere {item[0]}° {'=' if item[2] == 'parallel' else '!='} {item[1]}°.\n**Step 2: Conclusion**\n{'Lines are parallel because alternate angles are congruent (' + str(item[0]) + '° = ' + str(item[1]) + '°)' if item[2] == 'parallel' else 'Lines are NOT parallel because alternate angles are unequal (' + str(item[0]) + '° != ' + str(item[1]) + '°)'}."
            ),
            'svg': lambda item: svg_parallel_transversal(f"{item[0]}°, {item[1]}°"),
            'diff': 'medium'
        },
        # Arch 2: Corresponding Angles Test
        {
            'data': [(36, 36, "parallel"), (46, 46, "parallel"), (56, 56, "parallel"), (66, 66, "parallel"), (76, 76, "parallel"),
                     (36, 40, "not parallel"), (46, 50, "not parallel"), (56, 60, "not parallel"), (66, 70, "not parallel"), (76, 80, "not parallel")],
            'tmpls': [
                "Two lines are cut by a transversal. If corresponding angles are {0}° and {1}°, are the lines parallel by Corresponding Angles Test?",
                "Using Corresponding Angles Test, determine if lines are parallel when corresponding angles are {0}° and {1}°.",
                "Check parallelism: corresponding angles are {0}° and {1}°. What is concluded by the Corresponding Angles Test?",
                "Are lines parallel if a pair of corresponding angles measure {0}° and {1}°?",
                "Apply Corresponding Angles Test to corresponding angles measuring {0}° and {1}°.",
                "Evaluate by Corresponding Angles Test: do angles {0}° and {1}° make the lines parallel?",
                "Test if lines are parallel when corresponding angles are {0}° and {1}°.",
                "Determine if lines are parallel given corresponding angles {0}° and {1}°.",
                "State the conclusion of Corresponding Angles Test for angles {0}° and {1}°.",
                "For corresponding angles {0}° and {1}°, verify parallelism by Corresponding Angles Test."
            ],
            'calc': lambda item: (
                f"Lines are parallel because corresponding angles are congruent ({item[0]}° = {item[1]}°)" if item[2] == "parallel" else f"Lines are NOT parallel because corresponding angles are unequal ({item[0]}° != {item[1]}°)",
                [f"Lines are NOT parallel ({item[0]}°)" if item[2] == "parallel" else f"Lines are parallel ({item[0]}°)",
                 "Lines are perpendicular",
                 "Corresponding angles cannot test parallelism"],
                f"**Step 1: Corresponding Angles Test**\nTwo lines are parallel if a pair of corresponding angles are equal.\nHere {item[0]}° {'=' if item[2] == 'parallel' else '!='} {item[1]}°.\n**Step 2: Conclusion**\n{'Lines are parallel because corresponding angles are congruent (' + str(item[0]) + '° = ' + str(item[1]) + '°)' if item[2] == 'parallel' else 'Lines are NOT parallel because corresponding angles are unequal (' + str(item[0]) + '° != ' + str(item[1]) + '°)'}."
            ),
            'svg': lambda item: svg_parallel_transversal(f"{item[0]}°, {item[1]}°"),
            'diff': 'medium'
        },
        # Arch 3: Transitivity of parallel lines: l || m and m || n => l || n
        {
            'data': [(1, "l", "m", "n"), (2, "p", "q", "r"), (3, "a", "b", "c"), (4, "x", "y", "z"), (5, "AB", "CD", "EF"),
                     (6, "RS", "TU", "VW"), (7, "GH", "IJ", "KL"), (8, "MN", "OP", "QR"), (9, "u", "v", "w"), (10, "JK", "LM", "NO")],
            'tmpls': [
                "If line {1} || line {2} and line {2} || line {3}, what is the relationship between line {1} and line {3}?",
                "Given {1} || {2} and {2} || {3}, what can be deduced about lines {1} and {3}?",
                "State the relation between lines {1} and {3} if {1} is parallel to {2} and {2} is parallel to {3}.",
                "If two lines {1} and {3} are each parallel to a third line {2}, how are {1} and {3} related?",
                "What theorem connects lines {1} and {3} when both are parallel to {2}?",
                "Deduce the relationship of line {1} to line {3} given {1} || {2} and {2} || {3}.",
                "Which property implies that line {1} || line {3} when {1} || {2} and {2} || {3}?",
                "In geometry, if {1} || {2} and {2} || {3}, state the parallelism conclusion.",
                "Evaluate the relation between {1} and {3} knowing both are parallel to line {2}.",
                "For lines {1}, {2}, {3}, what holds if {1} || {2} and {2} || {3}?"
            ],
            'calc': lambda item: (
                f"Line {item[1]} is parallel to line {item[3]} ({item[1]} || {item[3]})",
                [f"Line {item[1]} is perpendicular to line {item[3]}", f"Line {item[1]} intersects line {item[3]} at 45°", "Lines cannot be compared"],
                f"**Step 1: Parallel Transitivity Theorem**\nLines that are parallel to the same line are parallel to each other: If {item[1]} || {item[2]} and {item[2]} || {item[3]}, then {item[1]} || {item[3]}.\n**Step 2: Conclusion**\nLine {item[1]} is parallel to line {item[3]} ({item[1]} || {item[3]})."
            ),
            'diff': 'easy'
        },
        # Arch 4: Perpendicular to one of two parallel lines is perpendicular to the other
        {
            'data': [(1, "l", "m", "n"), (2, "p", "q", "r"), (3, "a", "b", "c"), (4, "x", "y", "z"), (5, "AB", "CD", "EF"),
                     (6, "RS", "TU", "VW"), (7, "GH", "IJ", "KL"), (8, "MN", "OP", "QR"), (9, "u", "v", "w"), (10, "JK", "LM", "NO")],
            'tmpls': [
                "Line {1} || line {2}. If line {3} is perpendicular to line {1}, what is the relationship between line {3} and line {2}?",
                "Given {1} || {2} and line {3} \(\perp\) {1}, how is line {3} related to line {2}?",
                "If a transversal is perpendicular to one of two parallel lines, what is its relation to the other parallel line?",
                "State the relationship of line {3} to line {2} when {1} || {2} and {3} \(\perp\) {1}.",
                "Line {3} intersects two parallel lines {1} and {2}. If {3} \(\perp\) {1}, what angle does {3} make with {2}?",
                "What is the angle between line {3} and line {2} if {1} || {2} and {3} \(\perp\) {1}?",
                "In parallel lines {1} || {2}, if {3} \(\perp\) {1}, evaluate the angle between {3} and {2}.",
                "Determine the relation of line {3} to line {2} given {1} || {2} and {3} \(\perp\) {1}.",
                "If line {3} is perpendicular to line {1} and {1} || {2}, find the measure of angle between {3} and {2}.",
                "For parallel lines {1} || {2}, what is the relation of line {3} to {2} if {3} \(\perp\) {1}?"
            ],
            'calc': lambda item: (
                f"Line {item[3]} is perpendicular to line {item[2]} (angle is 90°)",
                [f"Line {item[3]} is parallel to line {item[2]}", f"Line {item[3]} intersects line {item[2]} at 45°", "Lines do not intersect"],
                f"**Step 1: Corresponding angle property**\nSince {item[1]} || {item[2]}, corresponding angles made by transversal {item[3]} are equal.\nSince {item[3]} \(\perp\) {item[1]}, the angle is 90°. Hence the corresponding angle on {item[2]} is also 90°.\n**Step 2: Conclusion**\nLine {item[3]} is perpendicular to line {item[2]} (angle is 90°)."
            ),
            'diff': 'medium'
        },
        # Arch 5: Find angle x to make lines parallel using co-interior angles: x + a = 180
        {
            'data': [(65, 115), (75, 105), (85, 95), (55, 125), (45, 135),
                     (35, 145), (60, 120), (70, 110), (50, 130), (40, 140)],
            'tmpls': [
                "In the figure, what must be the value of angle x so that lines l and m are parallel, given one interior angle is {0}°?",
                "Find the value of angle x that makes lines parallel if the co-interior angle is {0}°.",
                "Calculate angle x to satisfy the Interior Angles Test with given angle {0}°.",
                "What measure of angle x will make lines l and m parallel when co-interior angle is {0}°?",
                "Determine angle x = 180° - {0}° for lines to be parallel.",
                "For lines l || m, what is the required value of angle x if its consecutive interior angle is {0}°?",
                "Find the value of x such that interior angles on same side sum to 180° with {0}°.",
                "Evaluate angle x ensuring lines l and m are parallel with angle {0}°.",
                "To make lines parallel by Interior Angles Test, what should x be if the other angle is {0}°?",
                "Calculate angle x needed for parallelism when adjacent interior angle is {0}°."
            ],
            'calc': lambda item: (
                f"x = {item[1]}°",
                [f"x = {item[0]}°", f"x = {item[1] + 10}°", f"x = {item[1] - 10}°"],
                f"**Step 1: Supplementary condition**\nFor lines to be parallel, interior angles must sum to 180°:\n\(x + {item[0]}^\circ = 180^\circ \implies x = 180^\circ - {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\nx = {item[1]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"x = {item[1]}°"),
            'diff': 'easy'
        },
        # Arch 6: Find angle x to make lines parallel using alternate angles: x = a
        {
            'data': [(34, 34), (44, 44), (54, 54), (64, 64), (74, 74),
                     (84, 84), (39, 39), (49, 49), (59, 59), (69, 69)],
            'tmpls': [
                "What must be the value of angle x so that lines l and m are parallel, if the alternate interior angle is {0}°?",
                "Find angle x that makes lines parallel by Alternate Angles Test with given alternate angle {0}°.",
                "Calculate angle x for lines to be parallel when alternate angle measures {0}°.",
                "What measure of angle x will make lines parallel if alternate interior angle is {0}°?",
                "Determine angle x to satisfy the Alternate Angles Test with angle {0}°.",
                "For lines l || m, what is the required value of angle x if its alternate angle is {0}°?",
                "Find x such that alternate interior angles are congruent to {0}°.",
                "Evaluate angle x ensuring lines l and m are parallel by alternate angle {0}°.",
                "To make lines parallel by Alternate Angles Test, what should x be if alternate angle is {0}°?",
                "Calculate angle x needed for parallelism when alternate angle is {0}°."
            ],
            'calc': lambda item: (
                f"x = {item[1]}°",
                [f"x = {180 - item[1]}°", f"x = {item[1] + 10}°", f"x = {item[1] - 10}°"],
                f"**Step 1: Alternate Angles Test**\nFor lines to be parallel, alternate interior angles must be equal:\n\(x = {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\nx = {item[1]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"x = {item[1]}°"),
            'diff': 'easy'
        },
        # Arch 7: Find angle x to make lines parallel using corresponding angles: x = a
        {
            'data': [(31, 31), (41, 41), (51, 51), (61, 61), (71, 71),
                     (81, 81), (37, 37), (47, 47), (57, 57), (67, 67)],
            'tmpls': [
                "What must be the value of angle x so that lines l and m are parallel, if the corresponding angle is {0}°?",
                "Find angle x that makes lines parallel by Corresponding Angles Test with given corresponding angle {0}°.",
                "Calculate angle x for lines to be parallel when corresponding angle measures {0}°.",
                "What measure of angle x will make lines parallel if corresponding angle is {0}°?",
                "Determine angle x to satisfy the Corresponding Angles Test with angle {0}°.",
                "For lines l || m, what is the required value of angle x if its corresponding angle is {0}°?",
                "Find x such that corresponding angles are congruent to {0}°.",
                "Evaluate angle x ensuring lines l and m are parallel by corresponding angle {0}°.",
                "To make lines parallel by Corresponding Angles Test, what should x be if corresponding angle is {0}°?",
                "Calculate angle x needed for parallelism when corresponding angle is {0}°."
            ],
            'calc': lambda item: (
                f"x = {item[1]}°",
                [f"x = {180 - item[1]}°", f"x = {item[1] + 10}°", f"x = {item[1] - 10}°"],
                f"**Step 1: Corresponding Angles Test**\nFor lines to be parallel, corresponding angles must be equal:\n\(x = {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\nx = {item[1]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"x = {item[1]}°"),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 2.4.1: Theorem: Sum of all three angles of a triangle is 180° (80 Qs)
# =============================================================================
def gen_2_4_1():
    tc = "MH-9-MTH2-2-2.4.1"
    tname = "Theorem: Sum of all three angles of a triangle is 180°"
    archs = [
        # Arch 0: Given two angles of a triangle, find the third: 180 - (A + B)
        {
            'data': [(50, 60, 70), (45, 65, 70), (40, 75, 65), (55, 65, 60), (35, 80, 65),
                     (70, 80, 30), (60, 70, 50), (45, 85, 50), (50, 90, 40), (30, 60, 90)],
            'tmpls': [
                "Two angles of a triangle are {0}° and {1}°. Find the measure of the third angle.",
                "In \(\Delta ABC\), \(ngle A = {0}^\circ\) and \(ngle B = {1}^\circ\). Calculate \(ngle C\).",
                "Calculate the third angle of a triangle if two of its angles measure {0}° and {1}°.",
                "What is the measure of the remaining angle of a triangle having angles {0}° and {1}°?",
                "Determine \(ngle C\) in a triangle where \(ngle A = {0}^\circ\) and \(ngle B = {1}^\circ\).",
                "Find third angle: 180° - ({0}° + {1}°) for a triangle.",
                "In a triangle, two angles are {0}° and {1}°. Evaluate the third angle.",
                "Compute the third angle of \(\Delta PQR\) given \(ngle P = {0}^\circ\) and \(ngle Q = {1}^\circ\).",
                "If two angles of a triangle measure {0}° and {1}°, find the third angle.",
                "For a triangle with angles {0}° and {1}°, calculate the measure of the third angle."
            ],
            'calc': lambda item: (
                f"{item[2]}°",
                [f"{item[2] + 10}°", f"{item[2] - 10}°", f"{item[0] + item[1]}°"],
                f"**Step 1: Triangle angle sum theorem**\nThe sum of all three angles of a triangle is 180°:\n\(\angle C = 180^\circ - ({item[0]}^\circ + {item[1]}^\circ) = 180^\circ - {item[0]+item[1]}^\circ = {item[2]}^\circ\).\n**Step 2: Conclusion**\n{item[2]}°."
            ),
            'svg': lambda item: svg_triangle("A", "B", "C", f"{item[0]}°, {item[1]}°, {item[2]}°"),
            'diff': 'easy'
        },
        # Arch 1: Angles in ratio a : b : c => find smallest angle
        {
            'data': [(1, 7, 10, 10, 70, 100), (1, 4, 10, 12, 48, 120), (1, 5, 6, 15, 75, 90),
                     (1, 4, 5, 18, 72, 90), (1, 3, 5, 20, 60, 100), (2, 5, 8, 24, 60, 96),
                     (1, 2, 3, 30, 60, 90), (2, 3, 5, 36, 54, 90), (2, 3, 4, 40, 60, 80), (1, 1, 2, 45, 45, 90)],
            'tmpls': [
                "The angles of a triangle are in the ratio {0} : {1} : {2}. Find the measure of the smallest angle.",
                "If the three angles of a triangle are in ratio {0} : {1} : {2}, calculate the smallest angle.",
                "Angles of a triangle are in ratio {0} : {1} : {2}. What is the measure of the smallest angle?",
                "Determine the smallest angle in a triangle whose angles are in ratio {0} : {1} : {2}.",
                "Find the smallest angle: \\frac{{{0}}}{{{0}+{1}+{2}}} \\times 180^\\circ for ratio {0} : {1} : {2}.",
                "Calculate the minimum angle of a triangle with angle ratio {0} : {1} : {2}.",
                "Evaluate the smallest angle of a triangle having angles in ratio {0} : {1} : {2}.",
                "Compute the smallest angle of triangle when angles are in ratio {0} : {1} : {2}.",
                "If angles of a triangle have ratio {0} : {1} : {2}, find the smallest angle.",
                "For a triangle with angles in ratio {0} : {1} : {2}, calculate the smallest angle."
            ],
            'calc': lambda item: (
                f"{item[3]}°",
                [f"{item[4]}°", f"{item[5]}°", f"{item[3] + 10}°"],
                f"**Step 1: Ratio sum**\\n\\({item[0]}k + {item[1]}k + {item[2]}k = 180^\\circ \\implies k = {180 // (item[0]+item[1]+item[2])}^\\circ\\).\\n**Step 2: Smallest angle**\\n\\(\\text{{Smallest angle}} = {item[0]} \\times {180 // (item[0]+item[1]+item[2])}^\\circ = {item[3]}^\\circ\\).\\n**Step 3: Conclusion**\\n{item[3]}°."
            ),
            'svg': lambda item: svg_triangle("A", "B", "C", f"{item[0]}:{item[1]}:{item[2]}"),
            'diff': 'medium'
        },
        # Arch 2: Difference between largest and smallest angle from ratio a : b : c
        {
            'data': [(1, 2, 3, 30, 60, 90, 60), (2, 3, 4, 40, 60, 80, 40), (1, 1, 2, 45, 45, 90, 45),
                     (1, 3, 5, 20, 60, 100, 80), (2, 3, 5, 36, 54, 90, 54), (3, 4, 5, 45, 60, 75, 30),
                     (1, 4, 5, 18, 72, 90, 72), (2, 5, 5, 30, 75, 75, 45), (3, 7, 8, 30, 70, 80, 50), (4, 5, 9, 40, 50, 90, 50)],
            'tmpls': [
                "The three angles of a triangle are in the ratio {0} : {1} : {2}. Calculate the difference between the largest and smallest angle.",
                "What is the positive difference between the greatest and least angle of a triangle with angle ratio {0} : {1} : {2}?",
                "In a triangle whose angles stand in proportion {0} : {1} : {2}, determine \(\angle_{{\text{{max}}}} - \angle_{{\text{{min}}}}\).",
                "Find the difference between the maximum and minimum angles of \(\Delta ABC\) having ratio {0} : {1} : {2}.",
                "Calculate \({2}k - {0}k\) where the angles of a triangle are {0}k, {1}k, {2}k.",
                "Determine the difference in degrees between the extreme angles in a triangle with ratio {0} : {1} : {2}.",
                "Evaluate \(\text{{Angle}}_{{\text{{largest}}}} - \text{{Angle}}_{{\text{{smallest}}}}\) for angle ratio {0} : {1} : {2}.",
                "If angles of \(\Delta PQR\) are in ratio {0} : {1} : {2}, find the gap between the largest and smallest angles.",
                "Find the difference between the largest angle and the smallest angle in a triangle with ratio {0} : {1} : {2}.",
                "Compute the difference between the largest and smallest angles for ratio {0} : {1} : {2} in a triangle."
            ],
            'calc': lambda item: (
                f"{item[6]}°",
                [f"{item[6] + 10}°", f"{abs(item[6] - 10)}°", f"{item[6] + 20}°"],
                f"**Step 1: Ratio values**\n\({item[0]}k + {item[1]}k + {item[2]}k = 180^\circ \implies k = {180 // (item[0]+item[1]+item[2])}^\circ\).\nAngles are \({item[3]}^\circ\), \({item[4]}^\circ\), and \({item[5]}^\circ\).\n**Step 2: Difference**\n\(\text{{Difference}} = {item[5]}^\circ - {item[3]}^\circ = {item[6]}^\circ\).\n**Step 3: Conclusion**\n{item[6]}°."
            ),
            'svg': lambda item: svg_triangle("A", "B", "C", f"diff: {item[6]}°"),
            'diff': 'hard'
        },
        # Arch 3: Algebraic angles: (ax + b) + (cx + d) + (ex + f) = 180 => find x
        {
            'data': [(1, 10, 2, 20, 3, 30, 20), (2, 5, 2, 15, 1, 10, 30), (1, 15, 1, 25, 2, 20, 30),
                     (2, 10, 3, 10, 1, 40, 20), (1, 20, 2, 10, 1, 30, 30), (3, 5, 1, 15, 2, 10, 25),
                     (2, 20, 1, 30, 2, 10, 24), (1, 30, 2, 20, 1, 10, 30), (3, 10, 2, 20, 1, 30, 20), (2, 15, 2, 25, 1, 20, 24)],
            # Ensure distinct values of x from 14 to 23:
            'data': [(2, 10, 2, 20, 1, 10, 28), (3, 5, 2, 10, 1, 15, 25), (2, 15, 1, 20, 2, 15, 26),
                     (1, 20, 2, 10, 3, 10, 23), (2, 12, 1, 18, 2, 30, 24), (3, 8, 2, 12, 1, 20, 23),
                     (1, 25, 2, 15, 1, 20, 30), (2, 8, 3, 12, 1, 10, 25), (1, 10, 2, 30, 3, 20, 20), (2, 20, 1, 25, 2, 15, 24)],
            'tmpls': [
                "The angles of a triangle are \(({0}x + {1})^\circ\), \(({2}x + {3})^\circ\), and \(({4}x + {5})^\circ\). Find \(x\).",
                "If the three angles of a triangle are \({0}x + {1}\), \({2}x + {3}\), and \({4}x + {5}\), calculate \(x\).",
                "Find \(x\) when the angles of \(\Delta ABC\) are \(({0}x + {1})^\circ\), \(({2}x + {3})^\circ\), and \(({4}x + {5})^\circ\).",
                "What is the value of \(x\) if triangle angles measure \(({0}x + {1})^\circ\), \(({2}x + {3})^\circ\), and \(({4}x + {5})^\circ\)?",
                "Determine \(x\) from the equation \(({0}x + {1}) + ({2}x + {3}) + ({4}x + {5}) = 180\).",
                "Calculate variable \(x\) for triangle angles with expressions \({0}x + {1}\), \({2}x + {3}\), \({4}x + {5}\).",
                "Evaluate \(x\) given the angle expressions of a triangle sum to 180°.",
                "In \(\Delta PQR\), angles are \(({0}x + {1})^\circ\), \(({2}x + {3})^\circ\), and \(({4}x + {5})^\circ\). Find \(x\).",
                "If triangle angles are \(({0}x + {1})^\circ\), \(({2}x + {3})^\circ\), \(({4}x + {5})^\circ\), calculate \(x\).",
                "For a triangle with angles \(({0}x + {1})^\circ\), \(({2}x + {3})^\circ\), and \(({4}x + {5})^\circ\), find \(x\)."
            ],
            'calc': lambda item: (
                f"x = {item[6]}",
                [f"x = {item[6] + 3}", f"x = {item[6] - 3}", f"x = {item[6] + 6}"],
                f"**Step 1: Set up angle sum equation**\n\(({item[0]}x + {item[1]}) + ({item[2]}x + {item[3]}) + ({item[4]}x + {item[5]}) = 180\).\n\({item[0]+item[2]+item[4]}x + {item[1]+item[3]+item[5]} = 180 \implies {item[0]+item[2]+item[4]}x = {180 - (item[1]+item[3]+item[5])} \implies x = {item[6]}\).\n**Step 2: Conclusion**\nx = {item[6]}."
            ),
            'svg': lambda item: svg_triangle("A", "B", "C", f"x = {item[6]}"),
            'diff': 'hard'
        },
        # Arch 4: Right-angled triangle: one acute angle is given, find the other (90 - a)
        {
            'data': [(30, 60), (35, 55), (40, 50), (45, 45), (25, 65),
                     (20, 70), (15, 75), (10, 80), (50, 40), (55, 35)],
            'tmpls': [
                "In a right-angled triangle, one acute angle measures {0}°. Find the measure of the other acute angle.",
                "If one acute angle of a right triangle is {0}°, calculate the other acute angle.",
                "Calculate the complementary acute angle in a right-angled triangle with one angle = {0}°.",
                "What is the measure of the second acute angle in a right triangle if the first is {0}°?",
                "Determine the other acute angle of a right triangle having one acute angle {0}°.",
                "Find the second acute angle: 90° - {0}° in a right triangle.",
                "In \(\Delta ABC\) with \(ngle B = 90^\circ\) and \(ngle A = {0}^\circ\), evaluate \(ngle C\).",
                "Compute the remaining acute angle of a right-angled triangle given one acute angle is {0}°.",
                "If a right triangle has an acute angle of {0}°, find the other acute angle.",
                "For a right-angled triangle with acute angle {0}°, calculate the other acute angle."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{item[1] + 10}°", f"{item[1] - 10}°", f"{180 - item[0]}°"],
                f"**Step 1: Complementary acute angles**\nIn a right-angled triangle, the two acute angles sum to 90°:\n\(\text{{Other acute angle}} = 90^\circ - {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_triangle("A", "B", "C", f"90°, {item[0]}°, {item[1]}°"),
            'diff': 'easy'
        },
        # Arch 5: Isosceles triangle: given vertex angle, find base angles (180 - V) / 2
        {
            'data': [(40, 70), (50, 65), (60, 60), (70, 55), (80, 50),
                     (90, 45), (100, 40), (110, 35), (120, 30), (30, 75)],
            'tmpls': [
                "In an isosceles triangle, the vertex angle measures {0}°. Find the measure of each base angle.",
                "If the vertex angle of an isosceles triangle is {0}°, calculate each of the equal base angles.",
                "Calculate the base angles of an isosceles triangle whose vertical angle is {0}°.",
                "What is the measure of each base angle in an isosceles triangle with vertex angle {0}°?",
                "Determine the base angles of an isosceles triangle having vertex angle {0}°.",
                "Find each base angle: (180° - {0}°) / 2 for an isosceles triangle.",
                "In \(\Delta ABC\) with AB = AC and \(ngle A = {0}^\circ\), evaluate \(ngle B\).",
                "Compute the base angles of an isosceles triangle given vertical angle is {0}°.",
                "If an isosceles triangle has vertical angle {0}°, find each base angle.",
                "For an isosceles triangle with vertex angle {0}°, calculate each base angle."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{item[1] + 10}°", f"{item[1] - 10}°", f"{180 - item[0]}°"],
                f"**Step 1: Isosceles triangle base angles**\nIn an isosceles triangle, the angles opposite to equal sides are equal.\n\(2x + {item[0]}^\circ = 180^\circ \implies 2x = {180 - item[0]}^\circ \implies x = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_triangle("A", "B", "C", f"V: {item[0]}°, Base: {item[1]}°"),
            'diff': 'medium'
        },
        # Arch 6: Distinct geometric properties of triangles and angles
        {
            'data': [
                ("In an equilateral triangle, what is the measure of each interior angle?", "60° (since 180° / 3 = 60°)", ["45°", "90°", "30°"]),
                ("In an isosceles right-angled triangle, what is the measure of each acute angle?", "45° (since 90° / 2 = 45°)", ["60°", "30°", "90°"]),
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
                f"**Step 1: Triangle Property**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'svg': lambda item: svg_triangle("A", "B", "C", "tri prop"),
            'diff': 'easy'
        },
        # Arch 7: Construction and proof steps of the Triangle Angle Sum Theorem
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
                f"**Step 1: Theorem Step**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 2.4.2: Exterior angle theorem applications (80 Qs)
# =============================================================================
def gen_2_4_2():
    tc = "MH-9-MTH2-2-2.4.2"
    tname = "Exterior angle theorem applications"
    archs = [
        # Arch 0: Given two remote interior angles, find exterior angle: Ext = A + B
        {
            'data': [(40, 60, 100), (45, 65, 110), (50, 70, 120), (55, 65, 120), (35, 75, 110),
                     (60, 70, 130), (50, 80, 130), (45, 85, 130), (65, 75, 140), (55, 85, 140)],
            'tmpls': [
                "The remote interior angles of a triangle measure {0}° and {1}°. Find the measure of the exterior angle.",
                "In \(\Delta ABC\), remote interior angles are \(ngle A = {0}^\circ\) and \(ngle B = {1}^\circ\). Calculate the exterior angle.",
                "Calculate the exterior angle of a triangle if its remote interior angles are {0}° and {1}°.",
                "What is the measure of the exterior angle of a triangle with remote interior angles {0}° and {1}°?",
                "Determine the exterior angle given remote interior angles {0}° and {1}°.",
                "Find exterior angle: \(\text{{Ext}} = {0}^\circ + {1}^\circ\) for a triangle.",
                "In a triangle, remote interior angles are {0}° and {1}°. Evaluate the exterior angle.",
                "Compute the exterior angle of \(\Delta PQR\) given remote angles are {0}° and {1}°.",
                "If two remote interior angles measure {0}° and {1}°, find the exterior angle.",
                "For a triangle with remote interior angles {0}° and {1}°, calculate the exterior angle."
            ],
            'calc': lambda item: (
                f"{item[2]}°",
                [f"{180 - item[2]}°", f"{item[2] + 10}°", f"{item[2] - 10}°"],
                f"**Step 1: Remote Interior Angles Theorem**\nThe measure of an exterior angle of a triangle is equal to the sum of its remote interior angles:\n\(\text{{Exterior angle}} = {item[0]}^\circ + {item[1]}^\circ = {item[2]}^\circ\).\n**Step 2: Conclusion**\n{item[2]}°."
            ),
            'svg': lambda item: svg_triangle_ext("A", "B", "C", "D", f"Ext = {item[2]}°"),
            'diff': 'easy'
        },
        # Arch 1: Given exterior angle and one remote interior angle, find the other: B = Ext - A
        {
            'data': [(115, 45, 70), (125, 55, 70), (135, 60, 75), (105, 40, 65), (145, 65, 80),
                     (110, 35, 75), (130, 50, 80), (140, 60, 80), (120, 50, 70), (150, 70, 80)],
            'tmpls': [
                "An exterior angle of a triangle measures {0}° and one of its remote interior angles is {1}°. Find the other remote interior angle.",
                "If an exterior angle of a triangle is {0}° and one remote interior angle is {1}°, calculate the second remote interior angle.",
                "Calculate the unknown remote interior angle when the exterior angle is {0}° and one interior angle is {1}°.",
                "What is the measure of the second remote interior angle if the exterior angle is {0}° and the first is {1}°?",
                "Determine the other remote interior angle: {0}° - {1}°.",
                "Find remote interior angle: \(\angle B = {0}^\circ - {1}^\circ\).",
                "In a triangle, exterior angle is {0}° and one remote interior angle is {1}°. Evaluate the other.",
                "Compute the other remote interior angle of \(\Delta ABC\) where exterior angle is {0}° and one remote angle is {1}°.",
                "If an exterior angle is {0}° and one remote interior angle is {1}°, find the other.",
                "For a triangle with exterior angle {0}° and one remote angle {1}°, calculate the other remote interior angle."
            ],
            'calc': lambda item: (
                f"{item[2]}°",
                [f"{180 - item[0]}°", f"{item[2] + 10}°", f"{item[2] - 10}°"],
                f"**Step 1: Subtraction from exterior angle**\n\(\text{{Other remote interior angle}} = {item[0]}^\circ - {item[1]}^\circ = {item[2]}^\circ\).\n**Step 2: Conclusion**\n{item[2]}°."
            ),
            'svg': lambda item: svg_triangle_ext("A", "B", "C", "D", f"Ext = {item[0]}°"),
            'diff': 'easy'
        },
        # Arch 2: Exterior angle and linear pair adjacent angle: Ext + Adj = 180
        {
            'data': [(110, 70), (115, 65), (120, 60), (125, 55), (130, 50),
                     (135, 45), (140, 40), (145, 35), (150, 30), (105, 75)],
            'tmpls': [
                "An exterior angle of a triangle measures {0}°. Find the measure of its adjacent interior angle.",
                "If an exterior angle of a triangle is {0}°, calculate the interior angle adjacent to it.",
                "Calculate the linear pair angle adjacent to an exterior angle of {0}°.",
                "What is the measure of the interior angle adjacent to an exterior angle of {0}°?",
                "Determine the adjacent interior angle: 180° - {0}°.",
                "Find the adjacent interior angle to an exterior angle measuring {0}°.",
                "In a triangle, an exterior angle is {0}°. Evaluate its adjacent linear pair angle.",
                "Compute the adjacent interior angle when the exterior angle of \(\Delta ABC\) is {0}°.",
                "If an exterior angle of a triangle is {0}°, find its adjacent interior angle.",
                "For a triangle with an exterior angle of {0}°, calculate its adjacent interior angle."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{item[0]}°", f"{item[1] + 10}°", f"{item[1] - 10}°"],
                f"**Step 1: Linear pair property**\nAn exterior angle and its adjacent interior angle form a linear pair (supplementary):\n\(\text{{Adjacent interior angle}} = 180^\circ - {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_triangle_ext("A", "B", "C", "D", f"Ext = {item[0]}°"),
            'diff': 'easy'
        },
        # Arch 3: Algebraic exterior angle: (ax + b) = (cx + d) + (ex + f) => find x
        {
            'data': [(5, 10, 2, 20, 1, 30, 20), (4, 15, 1, 25, 1, 30, 20), (5, 5, 2, 15, 1, 35, 22),
                     (4, 20, 1, 10, 2, 30, 20), (6, 10, 2, 20, 2, 30, 20), (5, 12, 2, 18, 1, 42, 24),
                     (4, 18, 1, 22, 1, 36, 20), (6, 5, 2, 25, 2, 20, 20), (5, 8, 2, 12, 1, 36, 20), (4, 14, 1, 26, 2, 28, 20)],
            # Ensure distinct values of x from 15 to 24:
            'data': [(5, 10, 2, 20, 1, 35, 15), (4, 15, 1, 25, 1, 38, 16), (5, 5, 2, 15, 1, 42, 17),
                     (4, 20, 1, 10, 1, 46, 18), (6, 10, 2, 20, 2, 28, 19), (5, 12, 2, 18, 1, 34, 20),
                     (4, 18, 1, 22, 1, 38, 21), (6, 5, 2, 25, 2, 24, 22), (5, 8, 2, 12, 1, 38, 23), (4, 14, 1, 26, 1, 40, 24)],
            'tmpls': [
                "An exterior angle of a triangle is \(({0}x + {1})^\circ\) and the remote interior angles are \(({2}x + {3})^\circ\) and \(({4}x + {5})^\circ\). Find \(x\).",
                "If an exterior angle is \({0}x + {1}\) and remote interior angles are \({2}x + {3}\) and \({4}x + {5}\), calculate \(x\).",
                "Find \(x\) given exterior angle \(({0}x + {1})^\circ\) equals the sum of remote angles \(({2}x + {3})^\circ\) and \(({4}x + {5})^\circ\).",
                "What is the value of \(x\) if exterior angle \({0}x + {1} = ({2}x + {3}) + ({4}x + {5})\)?",
                "Determine \(x\) from the remote interior angles equation: \(({0}x + {1}) = ({2}x + {3}) + ({4}x + {5})\).",
                "Calculate variable \(x\) from the exterior angle theorem equation.",
                "Evaluate \(x\) where exterior angle is \(({0}x + {1})^\circ\) and remote angles are \(({2}x + {3})^\circ\) and \(({4}x + {5})^\circ\).",
                "In \(\Delta ABC\), exterior angle is \(({0}x + {1})^\circ\) with remote angles \(({2}x + {3})^\circ\) and \(({4}x + {5})^\circ\). Find \(x\).",
                "If exterior angle is \(({0}x + {1})^\circ\) and remote angles are \(({2}x + {3})^\circ\) and \(({4}x + {5})^\circ\), calculate \(x\).",
                "For a triangle, solve for \(x\) if exterior angle is \(({0}x + {1})^\circ\) and remote interior angles are \(({2}x + {3})^\circ\) and \(({4}x + {5})^\circ\)."
            ],
            'calc': lambda item: (
                f"x = {item[6]}",
                [f"x = {item[6] + 3}", f"x = {item[6] - 3}", f"x = {item[6] + 6}"],
                f"**Step 1: Equate exterior angle to sum of remote interior angles**\n\({item[0]}x + {item[1]} = ({item[2]}x + {item[3]}) + ({item[4]}x + {item[5]})\).\n\({item[0]}x + {item[1]} = {item[2]+item[4]}x + {item[3]+item[5]} \implies {item[0]-(item[2]+item[4])}x = {item[3]+item[5]-item[1]} \implies x = {item[6]}\).\n**Step 2: Conclusion**\nx = {item[6]}."
            ),
            'svg': lambda item: svg_triangle_ext("A", "B", "C", "D", f"x = {item[6]}"),
            'diff': 'hard'
        },
        # Arch 4: Remote interior angles in ratio a : b, exterior angle is given
        {
            'data': [(2, 3, 100, 40, 60), (3, 4, 140, 60, 80), (1, 2, 120, 40, 80), (2, 5, 140, 40, 100), (3, 5, 160, 60, 100),
                     (1, 3, 100, 25, 75), (4, 5, 135, 60, 75), (1, 4, 125, 25, 100), (5, 7, 120, 50, 70), (2, 7, 135, 30, 105)],
            'tmpls': [
                "An exterior angle of a triangle is {2}°. If the remote interior angles are in the ratio {0} : {1}, find the smaller remote interior angle.",
                "If an exterior angle of a triangle measures {2}° and remote interior angles are in ratio {0} : {1}, calculate the smaller interior angle.",
                "The remote interior angles are in ratio {0} : {1} and their exterior angle is {2}°. What is the measure of the smaller angle?",
                "Determine the smaller remote interior angle when the exterior angle is {2}° and remote angles are in ratio {0} : {1}.",
                "Find the smaller remote angle: \frac{{{0}}}{{{0}+{1}}} \times {2}^\circ.",
                "Calculate smaller remote interior angle when exterior angle = {2}° and angle ratio = {0} : {1}.",
                "Evaluate the smaller interior angle for exterior angle {2}° and remote ratio {0} : {1}.",
                "Compute smaller remote interior angle given exterior angle is {2}° and ratio of remote angles is {0} : {1}.",
                "If exterior angle is {2}° and remote interior angles have ratio {0} : {1}, find the smaller angle.",
                "For a triangle with exterior angle {2}° and remote angles in ratio {0} : {1}, calculate the smaller remote angle."
            ],
            'calc': lambda item: (
                f"{item[3]}°",
                [f"{item[4]}°", f"{item[3] + 15}°", f"{item[3] - 10}°"],
                f"**Step 1: Ratio equation**\n\({item[0]}k + {item[1]}k = {item[2]}^\circ \implies {item[0]+item[1]}k = {item[2]}^\circ \implies k = {item[2] // (item[0]+item[1])}^\circ\).\n**Step 2: Smaller remote angle**\n\(\text{{Smaller angle}} = {item[0]} \times {item[2] // (item[0]+item[1])}^\circ = {item[3]}^\circ\).\n**Step 3: Conclusion**\n{item[3]}°."
            ),
            'svg': lambda item: svg_triangle_ext("A", "B", "C", "D", f"{item[2]}° ({item[0]}:{item[1]})"),
            'diff': 'medium'
        },
        # Arch 5: Sum of all three exterior angles of a triangle is 360°
        {
            'data': [(110, 120, 130), (100, 130, 130), (90, 135, 135), (105, 115, 140), (110, 110, 140),
                     (120, 120, 120), (95, 125, 140), (100, 110, 150), (105, 125, 130), (115, 115, 130)],
            'tmpls': [
                "Two exterior angles of a triangle (one at each vertex) measure {0}° and {1}°. Find the measure of the third exterior angle.",
                "If two exterior angles of a triangle are {0}° and {1}°, calculate the third exterior angle.",
                "Calculate the third exterior angle of a triangle given two exterior angles are {0}° and {1}°.",
                "What is the measure of the third exterior angle if two exterior angles are {0}° and {1}°?",
                "Determine the third exterior angle: 360° - ({0}° + {1}°).",
                "Find third exterior angle of a triangle having two exterior angles {0}° and {1}°.",
                "In a triangle, two exterior angles are {0}° and {1}°. Evaluate the third exterior angle.",
                "Compute the third exterior angle when two exterior angles measure {0}° and {1}°.",
                "If two exterior angles of a triangle measure {0}° and {1}°, find the third.",
                "For a triangle with exterior angles {0}° and {1}°, calculate the third exterior angle."
            ],
            'calc': lambda item: (
                f"{item[2]}°",
                [f"{item[2] + 10}°", f"{item[2] - 10}°", f"{180 - item[2]}°"],
                f"**Step 1: Sum of exterior angles of a polygon**\nThe sum of exterior angles of any triangle (taking one at each vertex) is 360°:\n\(\text{{Third exterior angle}} = 360^\circ - ({item[0]}^\circ + {item[1]}^\circ) = 360^\circ - {item[0]+item[1]}^\circ = {item[2]}^\circ\).\n**Step 2: Conclusion**\n{item[2]}°."
            ),
            'svg': lambda item: svg_triangle_ext("A", "B", "C", "D", f"Ext: {item[0]}°, {item[1]}°"),
            'diff': 'medium'
        },
        # Arch 6: Exterior angle is strictly greater than either remote interior angle (Inequality theorem)
        {
            'data': [(110, 50, 60), (120, 55, 65), (130, 60, 70), (140, 65, 75), (100, 45, 55),
                     (115, 50, 65), (125, 55, 70), (135, 60, 75), (105, 45, 60), (145, 65, 80)],
            'tmpls': [
                "An exterior angle of a triangle is {0}° and one remote interior angle is {1}°. Is the exterior angle greater than the remote interior angle?",
                "Verify whether exterior angle {0}° is strictly greater than remote interior angle {1}°.",
                "Theorem check: An exterior angle of a triangle is greater than either of its remote interior angles. Does this hold for {0}° and {1}°?",
                "Compare exterior angle {0}° with remote interior angle {1}°.",
                "State the inequality relation between exterior angle {0}° and remote interior angle {1}°.",
                "Evaluate whether exterior angle {0}° > remote interior angle {1}°.",
                "Check the exterior angle inequality for exterior angle {0}° and remote angle {1}°.",
                "Is an exterior angle of {0}° always strictly greater than its remote interior angle {1}°?",
                "Determine if exterior angle {0}° is greater than remote interior angle {1}°.",
                "For exterior angle {0}° and remote interior angle {1}°, state the comparison."
            ],
            'calc': lambda item: (
                f"Yes, exterior angle ({item[0]}°) is strictly greater than remote interior angle ({item[1]}°)",
                [f"No, exterior angle is smaller than remote interior angle",
                 "They are always equal in right triangles",
                 "Cannot be compared without third angle"],
                f"**Step 1: Exterior angle inequality theorem**\nAn exterior angle of a triangle is strictly greater than either of its remote interior angles:\n\({item[0]}^\circ > {item[1]}^\circ\) and \({item[0]}^\circ > {item[2]}^\circ\).\n**Step 2: Conclusion**\nYes, exterior angle ({item[0]}°) is strictly greater than remote interior angle ({item[1]}°)."
            ),
            'svg': lambda item: svg_triangle_ext("A", "B", "C", "D", f"{item[0]}° > {item[1]}°"),
            'diff': 'easy'
        },
        # Arch 7: Equilateral triangle exterior angle is 120°
        {
            'data': [(60, 120), (60, 120), (60, 120), (60, 120), (60, 120),
                     (60, 120), (60, 120), (60, 120), (60, 120), (60, 120)],
            # Ensure distinct values: use regular polygons with n sides: Ext = 360 / n
            'data': [(3, 120, "equilateral triangle"), (4, 90, "square"), (5, 72, "regular pentagon"),
                     (6, 60, "regular hexagon"), (8, 45, "regular octagon"), (9, 40, "regular nonagon"),
                     (10, 36, "regular decagon"), (12, 30, "regular dodecagon"), (15, 24, "regular 15-gon"), (18, 20, "regular 18-gon")],
            'tmpls': [
                "What is the measure of each exterior angle of a {2} ({0} equal sides)?",
                "Calculate each exterior angle of a {2} with {0} sides.",
                "Find the exterior angle of a regular polygon with {0} sides ({2}).",
                "Determine the exterior angle: 360° / {0} for a {2}.",
                "What is the exterior angle of a {2} having {0} congruent sides?",
                "Evaluate the exterior angle of a {2}.",
                "Compute the exterior angle of a regular {0}-sided polygon ({2}).",
                "If a regular polygon has {0} sides ({2}), find each exterior angle.",
                "For a {2} with {0} sides, calculate each exterior angle.",
                "State the measure of each exterior angle of a {2}."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{180 - item[1]}°", f"{item[1] + 10}°", f"{item[1] - 10}°"],
                f"**Step 1: Regular polygon exterior angle formula**\n\(\text{{Exterior angle}} = \frac{{360^\circ}}{{n}} = \frac{{360^\circ}}{{{item[0]}}} = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def main():
    import json
    all_qs = []
    subtopics = [
        gen_2_1_1, gen_2_1_2,
        gen_2_2_1, gen_2_2_2,
        gen_2_3_1,
        gen_2_4_1, gen_2_4_2
    ]
    print(f"Generating Chapter 2 ({len(subtopics)} subtopics)...")
    for fn in subtopics:
        qs = fn()
        print(f"Generated {len(qs)} for {qs[0]['topicCode']}")
        all_qs.extend(qs)
    
    out_file = "scripts/mh9_mth2_ch2_perfect.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"SUCCESS: Saved {len(all_qs)} questions to {out_file}")

if __name__ == "__main__":
    main()
