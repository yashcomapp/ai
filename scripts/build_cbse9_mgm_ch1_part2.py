# scripts/build_cbse9_mgm_ch1_part2.py
# Subtopics:
# 1.2.1: Four quadrants and sign conventions (+,+, -,+, -,-, +,-) (80 Qs)
# 1.2.2: Plotting coordinates (x, y) with positive and negative numbers (80 Qs)
# 1.2.3: Points on axes (x, 0) and (0, y) (80 Qs)

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 1
CH_NAME = "Orienting Yourself: The Use of Coordinates"

# ==============================================================================
# SUBTOPIC 1.2.1: Four quadrants and sign conventions (+,+, -,+, -,-, +,-)
# ==============================================================================
def gen_1_2_1():
    tc = "CBSE-9-MGM-1-1.2.1"
    tname = "Four quadrants and sign conventions (+,+, -,+, -,-, +,-)"

    # Arch 0: Direct identification of quadrant from signs of coordinates
    arch0 = {
        'data': [
            (4, 9, 'Quadrant I'), (-5, 6, 'Quadrant II'), (-8, -3, 'Quadrant III'), (7, -11, 'Quadrant IV'),
            (12, 3, 'Quadrant I'), (-4, 15, 'Quadrant II'), (-9, -14, 'Quadrant III'), (6, -8, 'Quadrant IV'),
            (2, 8, 'Quadrant I'), (-11, 4, 'Quadrant II')
        ],
        'tmpls': [
            "In which quadrant does the point \\( P({0}, {1}) \\) lie?",
            "Identify the quadrant containing the point \\( A({0}, {1}) \\).",
            "The coordinate point \\( ({0}, {1}) \\) is situated in:",
            "To which quadrant does the point \\( M({0}, {1}) \\) belong?",
            "Determine the quadrant in which \\( Q({0}, {1}) \\) lies:",
            "In the Cartesian coordinate system, the point \\( ({0}, {1}) \\) lies in:",
            "The point \\( B({0}, {1}) \\) is located in which quadrant?",
            "Which quadrant holds the point \\( R({0}, {1}) \\)?",
            "On plotting, the point \\( ({0}, {1}) \\) will fall into:",
            "State the quadrant where the point \\( S({0}, {1}) \\) is located:"
        ],
        'calc': lambda item: (
            item[2],
            [q for q in ['Quadrant I', 'Quadrant II', 'Quadrant III', 'Quadrant IV'] if q != item[2]][:3],
            f"**Step 1: Check the signs of the abscissa and ordinate.**\nFor the point \\( ({item[0]}, {item[1]}) \\):\n- Abscissa \\( x = {item[0]} \\) is {'positive' if item[0] > 0 else 'negative'}.\n- Ordinate \\( y = {item[1]} \\) is {'positive' if item[1] > 0 else 'negative'}.\n\n**Step 2: Recall the sign conventions of the four quadrants.**\n- Quadrant I: \\( (+, +) \\)\n- Quadrant II: \\( (-, +) \\)\n- Quadrant III: \\( (-, -) \\)\n- Quadrant IV: \\( (+, -) \\)\n\n**Step 3: Conclude the quadrant.**\nThe sign pattern \\( ({'+' if item[0] > 0 else '-'}, {'+' if item[1] > 0 else '-'}) \\) places the point in {item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Quadrants under algebraic expressions or variables
    arch1 = {
        'data': [
            ("a > 0, b < 0", "(-a, b)", "Quadrant III", "(-, -)"),
            ("a < 0, b > 0", "(a, -b)", "Quadrant III", "(-, -)"),
            ("a > 0, b < 0", "(a, -b)", "Quadrant I", "(+, +)"),
            ("a < 0, b < 0", "(-a, -b)", "Quadrant I", "(+, +)"),
            ("a > 0, b > 0", "(-a, b)", "Quadrant II", "(-, +)"),
            ("a < 0, b > 0", "(-a, b)", "Quadrant I", "(+, +)"),
            ("a > 0, b < 0", "(-a, -b)", "Quadrant II", "(-, +)"),
            ("a < 0, b < 0", "(a, -b)", "Quadrant II", "(-, +)"),
            ("a < 0, b > 0", "(-a, -b)", "Quadrant IV", "(+, -)"),
            ("a > 0, b > 0", "(a, -b)", "Quadrant IV", "(+, -)")
        ],
        'tmpls': [
            "If \\( {0} \\), in which quadrant does the point \\( {1} \\) lie?",
            "Given \\( {0} \\), the point \\( P{1} \\) belongs to:",
            "When \\( {0} \\), the coordinates \\( {1} \\) place the point in:",
            "Under the conditions \\( {0} \\), identify the quadrant for \\( {1} \\):",
            "Determine the quadrant containing \\( {1} \\) if \\( {0} \\):",
            "If real numbers satisfy \\( {0} \\), the point \\( {1} \\) lies in:",
            "For variables satisfying \\( {0} \\), which quadrant contains \\( {1} \\)?",
            "In which quadrant will the point \\( {1} \\) be located if \\( {0} \\)?",
            "Suppose \\( {0} \\). Then the point \\( {1} \\) is situated in:",
            "Find the quadrant of \\( {1} \\) given the conditions \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[2],
            [q for q in ['Quadrant I', 'Quadrant II', 'Quadrant III', 'Quadrant IV'] if q != item[2]][:3],
            f"**Step 1: Determine the signs of each coordinate.**\nGiven \\( {item[0]} \\):\nAnalyze the abscissa and ordinate of the point \\( {item[1]} \\). The signs are {item[3]}.\n\n**Step 2: Match with standard quadrant sign conventions.**\n- \\( (+, +) \\) is Quadrant I\n- \\( (-, +) \\) is Quadrant II\n- \\( (-, -) \\) is Quadrant III\n- \\( (+, -) \\) is Quadrant IV\n\n**Step 3: State the final quadrant.**\nThe point lies in {item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 2: Signs of products and quotients of coordinates
    arch2 = {
        'data': [
            ("xy > 0", "Quadrant I or Quadrant III", ["Quadrant II or Quadrant IV", "Quadrant I or Quadrant II", "Quadrant III or Quadrant IV"], "Both x and y have the same sign (both positive or both negative)."),
            ("xy < 0", "Quadrant II or Quadrant IV", ["Quadrant I or Quadrant III", "Quadrant I or Quadrant IV", "Quadrant II or Quadrant III"], "x and y have opposite signs (one positive, one negative)."),
            ("x/y > 0", "Quadrant I or Quadrant III", ["Quadrant II or Quadrant IV", "Quadrant I only", "Quadrant IV only"], "The quotient is positive if and only if numerator and denominator share the same sign."),
            ("x/y < 0", "Quadrant II or Quadrant IV", ["Quadrant I or Quadrant III", "Quadrant II only", "Quadrant III only"], "The quotient is negative if and only if numerator and denominator have opposite signs."),
            ("x > 0 and y < 0", "Quadrant IV", ["Quadrant I", "Quadrant II", "Quadrant III"], "Positive abscissa and negative ordinate define Quadrant IV."),
            ("x < 0 and y > 0", "Quadrant II", ["Quadrant I", "Quadrant III", "Quadrant IV"], "Negative abscissa and positive ordinate define Quadrant II."),
            ("x < 0 and y < 0", "Quadrant III", ["Quadrant I", "Quadrant II", "Quadrant IV"], "Negative abscissa and negative ordinate define Quadrant III."),
            ("x > 0 and y > 0", "Quadrant I", ["Quadrant II", "Quadrant III", "Quadrant IV"], "Positive abscissa and positive ordinate define Quadrant I."),
            ("x²y > 0 for all non-zero x", "Quadrant I or Quadrant II", ["Quadrant III or Quadrant IV", "Quadrant I or Quadrant IV", "Quadrant II or Quadrant III"], "Since \\( x^2 > 0 \\) for any real \\( x \\neq 0 \\), \\( x^2 y > 0 \\) strictly implies \\( y > 0 \\)."),
            ("xy² < 0 for all non-zero y", "Quadrant II or Quadrant III", ["Quadrant I or Quadrant IV", "Quadrant I or Quadrant II", "Quadrant III or Quadrant IV"], "Since \\( y^2 > 0 \\) for any real \\( y \\neq 0 \\), \\( xy^2 < 0 \\) strictly implies \\( x < 0 \\).")
        ],
        'tmpls': [
            "If a point \\( P(x, y) \\) satisfies \\( {0} \\), in which quadrant(s) can it lie?",
            "The condition \\( {0} \\) is satisfied by points lying in:",
            "In which quadrant(s) do all points satisfying \\( {0} \\) exist?",
            "Points \\( (x, y) \\) for which \\( {0} \\) must lie in:",
            "Identify the quadrant(s) where \\( {0} \\) holds true:",
            "Which quadrant(s) correspond to the inequality \\( {0} \\)?",
            "If \\( {0} \\) for a point \\( (x, y) \\), then the point lies in:",
            "Determine the possible quadrant(s) for a point when \\( {0} \\):",
            "A point with coordinates \\( (x, y) \\) satisfying \\( {0} \\) is located in:",
            "Where do points in the Cartesian plane lie if \\( {0} \\)?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Analyze the algebraic sign conditions.**\n{item[3]}\n\n**Step 2: Map to Cartesian quadrants.**\nExamine the sign patterns of \\( (x, y) \\) in each of the four quadrants.\n\n**Step 3: State the conclusion.**\nThe points lie in {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Opposite quadrants and origin symmetry
    arch3 = {
        'data': [
            ("Quadrant I", "Quadrant III"), ("Quadrant II", "Quadrant IV"),
            ("Quadrant III", "Quadrant I"), ("Quadrant IV", "Quadrant II"),
            ("Quadrant I", "Quadrant III"), ("Quadrant II", "Quadrant IV"),
            ("Quadrant III", "Quadrant I"), ("Quadrant IV", "Quadrant II"),
            ("Quadrant I", "Quadrant III"), ("Quadrant II", "Quadrant IV")
        ],
        'tmpls': [
            "The diagonally opposite quadrant to {0} across the origin is:",
            "Which quadrant is symmetric to {0} with respect to the origin?",
            "If the signs of both coordinates of a point in {0} are inverted, the point moves to:",
            "A reflection through the origin transforms points from {0} into:",
            "The opposite quadrant to {0} is:",
            "Points in {0} have their reflections through origin lying in:",
            "Inverting the signs \\( (x, y) \\to (-x, -y) \\) takes points from {0} into:",
            "Which quadrant lies directly opposite to {0} across the reference origin?",
            "A half-turn (180° rotation) around the origin maps points in {0} into:",
            "Identify the diagonally opposite quadrant for {0}:"
        ],
        'calc': lambda item: (
            item[1],
            [q for q in ['Quadrant I', 'Quadrant II', 'Quadrant III', 'Quadrant IV'] if q != item[1]][:3],
            f"**Step 1: Recall origin symmetry.**\nReflecting a point \\( (x, y) \\) across the origin negates both coordinates: \\( (-x, -y) \\).\n\n**Step 2: Trace sign changes.**\n- If \\( (x, y) \\in \\text{{{item[0]}}} \\), inverting both signs yields the sign signature of \\text{{{item[1]}}}.\n\n**Step 3: State the resulting quadrant.**\nThe diagonally opposite quadrant is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 4: Non-integer / Radical coordinate points quadrant identification
    arch4 = {
        'data': [
            ("(\\sqrt{2}, -\\sqrt{5})", "Quadrant IV", "(+, -)"),
            ("(-\\frac{3}{4}, \\frac{7}{2})", "Quadrant II", "(-, +)"),
            ("(-\\sqrt{7}, -\\pi)", "Quadrant III", "(-, -)"),
            ("(\\frac{5}{3}, \\frac{11}{4})", "Quadrant I", "(+, +)"),
            ("(\\pi, -e)", "Quadrant IV", "(+, -)"),
            ("(-2.75, 4.8)", "Quadrant II", "(-, +)"),
            ("(-0.5, -9.2)", "Quadrant III", "(-, -)"),
            ("(\\sqrt{10}, \\sqrt{3})", "Quadrant I", "(+, +)"),
            ("(\\frac{1}{2}, -\\frac{5}{8})", "Quadrant IV", "(+, -)"),
            ("(-\\sqrt{13}, 1.6)", "Quadrant II", "(-, +)")
        ],
        'tmpls': [
            "In which quadrant does the point \\( P{0} \\) lie?",
            "Identify the quadrant for the point \\( {0} \\):",
            "The point \\( A{0} \\) belongs to which quadrant?",
            "Determine the quadrant where \\( {0} \\) is situated:",
            "To which quadrant does \\( M{0} \\) belong?",
            "Where is the coordinate point \\( {0} \\) plotted?",
            "Which quadrant contains the point \\( {0} \\)?",
            "Find the quadrant of the Cartesian plane containing \\( {0} \\):",
            "The ordered pair \\( {0} \\) is located in:",
            "State the quadrant for the point \\( Q{0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [q for q in ['Quadrant I', 'Quadrant II', 'Quadrant III', 'Quadrant IV'] if q != item[1]][:3],
            f"**Step 1: Determine the sign of each numerical component.**\nExamine the coordinates: {item[0]}.\nThe sign pair is {item[2]}.\n\n**Step 2: Match with quadrant conventions.**\n- \\( (+, +) \\): Quadrant I\n- \\( (-, +) \\): Quadrant II\n- \\( (-, -) \\): Quadrant III\n- \\( (+, -) \\): Quadrant IV\n\n**Step 3: State the quadrant.**\nThe point lies in {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Loci defined by inequalities (x > 0, y < 0 etc.)
    arch5 = {
        'data': [
            ("x > 2 and y > 3", "Part of Quadrant I", ["Part of Quadrant II", "Part of Quadrant IV", "Crosses all quadrants"]),
            ("x < -1 and y > 0", "Part of Quadrant II", ["Part of Quadrant I", "Part of Quadrant III", "Part of Quadrant IV"]),
            ("x < 0 and y < -4", "Part of Quadrant III", ["Part of Quadrant II", "Part of Quadrant IV", "Part of Quadrant I"]),
            ("x > 1 and y < -2", "Part of Quadrant IV", ["Part of Quadrant I", "Part of Quadrant III", "Part of Quadrant II"]),
            ("x > 0 and y = 0", "Positive x-axis", ["Quadrant I", "Quadrant IV", "Entire x-axis"]),
            ("x = 0 and y < 0", "Negative y-axis", ["Quadrant III", "Quadrant IV", "Entire y-axis"]),
            ("x < 0 and y = 0", "Negative x-axis", ["Quadrant II", "Quadrant III", "Origin only"]),
            ("x = 0 and y > 0", "Positive y-axis", ["Quadrant I", "Quadrant II", "Origin only"]),
            ("x > 0", "Quadrant I, Quadrant IV, and positive x-axis", ["Quadrant I only", "Quadrant I and II", "Entire Cartesian plane"]),
            ("y < 0", "Quadrant III, Quadrant IV, and negative y-axis", ["Quadrant III only", "Quadrant I and II", "Quadrant II and III"])
        ],
        'tmpls': [
            "The region of the Cartesian plane defined by \\( {0} \\) corresponds to:",
            "Which description characterizes the set of all points satisfying \\( {0} \\)?",
            "In the Cartesian plane, the inequality \\( {0} \\) represents:",
            "Where do points satisfying \\( {0} \\) lie?",
            "Identify the region represented by the condition \\( {0} \\):",
            "The set of points \\( (x, y) \\) where \\( {0} \\) forms:",
            "In which part of the coordinate system do points satisfying \\( {0} \\) reside?",
            "Describe the geometric region defined by \\( {0} \\):",
            "What part of the coordinate plane satisfies \\( {0} \\)?",
            "Determine the locus of points satisfying \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand the given boundary inequalities.**\nAnalyze the conditions: \\( {item[0]} \\).\n\n**Step 2: Map the conditions onto axes and quadrants.**\nDetermine which quadrant(s) or axis ray satisfy both constraints simultaneously.\n\n**Step 3: Conclude the region.**\nThe solution set is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Points equidistant from coordinate axes in specific quadrants
    arch6 = {
        'data': [
            ("Quadrant I", "y = x (where x > 0)", ["y = -x (where x > 0)", "y = 2x", "x = 0"]),
            ("Quadrant II", "y = -x (where x < 0)", ["y = x (where x < 0)", "y = -2x", "y = 0"]),
            ("Quadrant III", "y = x (where x < 0)", ["y = -x (where x < 0)", "y = x/2", "x = 0"]),
            ("Quadrant IV", "y = -x (where x > 0)", ["y = x (where x > 0)", "y = 3x", "y = 0"]),
            ("Quadrant I", "y = x (where x > 0)", ["y = -x", "x + y = 1", "xy = 1"]),
            ("Quadrant II", "y = -x (where x < 0)", ["y = x", "x - y = 0", "xy = 0"]),
            ("Quadrant III", "y = x (where x < 0)", ["y = -x", "x + y = 0", "x = y²"]),
            ("Quadrant IV", "y = -x (where x > 0)", ["y = x", "x = -y²", "xy = 1"]),
            ("Quadrant I", "y = x (where x > 0)", ["y = 2x", "y = x + 1", "y = -x + 1"]),
            ("Quadrant II", "y = -x (where x < 0)", ["y = x", "y = -x - 1", "y = 2x + 1"])
        ],
        'tmpls': [
            "What is the equation of the line comprising all points equidistant from both coordinate axes in {0}?",
            "In {0}, the locus of points whose perpendicular distance from the x-axis equals the perpendicular distance from the y-axis is given by:",
            "Find the relation between x and y for points in {0} that are equally distant from both axes:",
            "Which ray represents points equidistant from the x-axis and y-axis in {0}?",
            "In {0}, points having \\( |x| = |y| \\) satisfy the equation:",
            "The bisector of {0} is represented by which equation?",
            "Determine the equation of the angle bisector of the axes in {0}:",
            "Which equation defines the line equidistant from both axes in {0}?",
            "Points in {0} having equal distance from both coordinate axes lie on:",
            "State the equation of the line dividing {0} symmetrically into two equal halves:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Formulate the distance equality.**\nDistance from x-axis is \\( |y| \\), and distance from y-axis is \\( |x| \\).\nEquating them gives \\( |y| = |x| \\), which means \\( y = x \\) or \\( y = -x \\).\n\n**Step 2: Apply the signs of {item[0]}.**\nIn {item[0]}, examine whether coordinates have identical or opposite signs.\n\n**Step 3: State the equation.**\nThe required line ray is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Quadrant deduction from system of linear conditions
    arch7 = {
        'data': [
            ("x + y > 0 and x < 0", "Quadrant II", ["Quadrant I", "Quadrant III", "Quadrant IV"]),
            ("x - y > 0 and y > 0", "Quadrant I", ["Quadrant II", "Quadrant III", "Quadrant IV"]),
            ("x + y < 0 and x > 0", "Quadrant IV", ["Quadrant I", "Quadrant II", "Quadrant III"]),
            ("x - y < 0 and y < 0", "Quadrant III", ["Quadrant I", "Quadrant II", "Quadrant IV"]),
            ("x + y > 0 and y < 0", "Quadrant IV", ["Quadrant I", "Quadrant II", "Quadrant III"]),
            ("x - y > 0 and x < 0", "Quadrant III", ["Quadrant I", "Quadrant II", "Quadrant IV"]),
            ("x + y < 0 and y > 0", "Quadrant II", ["Quadrant I", "Quadrant III", "Quadrant IV"]),
            ("x - y < 0 and x > 0", "Quadrant I", ["Quadrant II", "Quadrant III", "Quadrant IV"]),
            ("xy > 0 and x + y < 0", "Quadrant III", ["Quadrant I", "Quadrant II", "Quadrant IV"]),
            ("xy < 0 and x - y < 0", "Quadrant II", ["Quadrant I", "Quadrant III", "Quadrant IV"])
        ],
        'tmpls': [
            "If a point \\( P(x, y) \\) satisfies \\( {0} \\), in which quadrant does it strictly lie?",
            "Under the simultaneous conditions \\( {0} \\), point \\( (x, y) \\) must belong to:",
            "Which quadrant contains all points satisfying the system \\( {0} \\)?",
            "Determine the quadrant for point \\( P(x, y) \\) when \\( {0} \\):",
            "A point whose coordinates satisfy \\( {0} \\) is located in:",
            "Find the quadrant in which points satisfy \\( {0} \\):",
            "If \\( {0} \\), then the point \\( (x, y) \\) lies in:",
            "Identify the quadrant containing points for which \\( {0} \\):",
            "Where does the point \\( (x, y) \\) lie if \\( {0} \\)?",
            "Given \\( {0} \\), the point \\( (x, y) \\) is situated in:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Analyze the first inequality.**\nConsider the constraints in \\( {item[0]} \\).\n\n**Step 2: Deduce the signs of x and y.**\nFrom the given system, deduce unambiguously whether \\( x > 0 \\) or \\( x < 0 \\), and whether \\( y > 0 \\) or \\( y < 0 \\).\n\n**Step 3: State the matching quadrant.**\nThe unique quadrant matching these sign requirements is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 1.2.2: Plotting coordinates (x, y) with positive and negative numbers
# ==============================================================================
def gen_1_2_2():
    tc = "CBSE-9-MGM-1-1.2.2"
    tname = "Plotting coordinates (x, y) with positive and negative numbers"

    # Arch 0: Reflection of a point in the x-axis
    arch0 = {
        'data': [
            (3, 5), (-4, 7), (6, -8), (-5, -9), (2, 11),
            (-7, 3), (8, -4), (-6, -6), (9, 1), (-10, 8)
        ],
        'tmpls': [
            "What are the coordinates of the reflection of the point \\( P({0}, {1}) \\) in the x-axis?",
            "When the point \\( A({0}, {1}) \\) is reflected across the x-axis, its image has coordinates:",
            "Find the image of the point \\( ({0}, {1}) \\) under reflection in the x-axis.",
            "Reflecting \\( M({0}, {1}) \\) across the horizontal x-axis yields the point:",
            "The reflection of \\( ({0}, {1}) \\) in the x-axis is given by:",
            "What point is obtained by reflecting \\( B({0}, {1}) \\) across the line \\( y = 0 \\) (x-axis)?",
            "If \\( P({0}, {1}) \\) is reflected across the x-axis, the coordinates of the reflected point \\( P' \\) are:",
            "Determine the coordinates of the image of \\( ({0}, {1}) \\) after reflection in the x-axis:",
            "The image point of \\( ({0}, {1}) \\) under reflection across the x-axis is:",
            "Find the coordinates of \\( Q' \\), the reflection of \\( Q({0}, {1}) \\) in the x-axis:"
        ],
        'calc': lambda item: (
            f"({item[0]}, {-item[1]})",
            [
                f"({-item[0]}, {item[1]})",
                f"({-item[0]}, {-item[1]})",
                f"({item[1]}, {item[0]})"
            ],
            f"**Step 1: Recall rule for reflection in the x-axis.**\nIn reflection across the x-axis, the x-coordinate (abscissa) remains unchanged, while the y-coordinate (ordinate) changes sign: \\( (x, y) \\to (x, -y) \\).\n\n**Step 2: Apply to point \\( ({item[0]}, {item[1]}) \\).**\n- New abscissa = \\( {item[0]} \\)\n- New ordinate = \\( -({item[1]}) = {-item[1]} \\)\n\n**Step 3: State the image coordinates.**\nThe reflected point is \\( ({item[0]}, {-item[1]}) \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Reflection of a point in the y-axis
    arch1 = {
        'data': [
            (4, 6), (-5, 8), (7, -3), (-6, -10), (3, 12),
            (-8, 5), (9, -2), (-4, -7), (10, 4), (-11, 9)
        ],
        'tmpls': [
            "What are the coordinates of the reflection of the point \\( P({0}, {1}) \\) in the y-axis?",
            "When the point \\( A({0}, {1}) \\) is reflected across the y-axis, its image has coordinates:",
            "Find the image of the point \\( ({0}, {1}) \\) under reflection in the y-axis.",
            "Reflecting \\( M({0}, {1}) \\) across the vertical y-axis yields the point:",
            "The reflection of \\( ({0}, {1}) \\) in the y-axis is given by:",
            "What point is obtained by reflecting \\( B({0}, {1}) \\) across the line \\( x = 0 \\) (y-axis)?",
            "If \\( P({0}, {1}) \\) is reflected across the y-axis, the coordinates of the reflected point \\( P' \\) are:",
            "Determine the coordinates of the image of \\( ({0}, {1}) \\) after reflection in the y-axis:",
            "The image point of \\( ({0}, {1}) \\) under reflection across the y-axis is:",
            "Find the coordinates of \\( Q' \\), the reflection of \\( Q({0}, {1}) \\) in the y-axis:"
        ],
        'calc': lambda item: (
            f"({-item[0]}, {item[1]})",
            [
                f"({item[0]}, {-item[1]})",
                f"({-item[0]}, {-item[1]})",
                f"({item[1]}, {item[0]})"
            ],
            f"**Step 1: Recall rule for reflection in the y-axis.**\nIn reflection across the y-axis, the y-coordinate (ordinate) remains unchanged, while the x-coordinate (abscissa) changes sign: \\( (x, y) \\to (-x, y) \\).\n\n**Step 2: Apply to point \\( ({item[0]}, {item[1]}) \\).**\n- New abscissa = \\( -({item[0]}) = {-item[0]} \\)\n- New ordinate = \\( {item[1]} \\)\n\n**Step 3: State the image coordinates.**\nThe reflected point is \\( ({-item[0]}, {item[1]}) \\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Reflection of a point in the origin
    arch2 = {
        'data': [
            (5, 7), (-3, 8), (4, -9), (-6, -5), (8, 2),
            (-7, 6), (9, -4), (-2, -11), (3, 10), (-8, 1)
        ],
        'tmpls': [
            "What are the coordinates of the image of point \\( P({0}, {1}) \\) when reflected in the origin?",
            "The reflection of the point \\( A({0}, {1}) \\) through the origin \\( (0, 0) \\) is:",
            "Find the image coordinates of \\( ({0}, {1}) \\) after a reflection in the origin.",
            "Reflecting \\( M({0}, {1}) \\) across the origin yields the point:",
            "The point obtained by rotating \\( ({0}, {1}) \\) by 180° around the origin is:",
            "Determine the coordinates of the origin reflection of \\( B({0}, {1}) \\):",
            "If \\( P({0}, {1}) \\) is reflected through the origin, the resulting point is:",
            "What are the coordinates of the point symmetric to \\( ({0}, {1}) \\) with respect to the origin?",
            "Reflection of \\( ({0}, {1}) \\) in the origin gives:",
            "Find the coordinates of \\( Q' \\), the origin-symmetric point of \\( Q({0}, {1}) \\):"
        ],
        'calc': lambda item: (
            f"({-item[0]}, {-item[1]})",
            [
                f"({item[0]}, {-item[1]})",
                f"({-item[0]}, {item[1]})",
                f"({item[1]}, {item[0]})"
            ],
            f"**Step 1: Recall rule for reflection in the origin.**\nReflection through the origin \\( (0, 0) \\) inverts the signs of both coordinates: \\( (x, y) \\to (-x, -y) \\).\n\n**Step 2: Apply to point \\( ({item[0]}, {item[1]}) \\).**\n- New abscissa = \\( -({item[0]}) = {-item[0]} \\)\n- New ordinate = \\( -({item[1]}) = {-item[1]} \\)\n\n**Step 3: State the reflected coordinates.**\nThe image point is \\( ({-item[0]}, {-item[1]}) \\)."
        ),
        'diff': 'easy'
    }

    # Arch 3: Distance between two points sharing abscissa or ordinate
    arch3 = {
        'data': [
            ((3, 4), (3, 11), 7), ((-2, 5), (-2, -4), 9), ((6, -3), (6, 5), 8), ((-5, -2), (-5, -9), 7),
            ((1, 8), (9, 8), 8), ((-4, 3), (5, 3), 9), ((7, -6), (-2, -6), 9), ((-8, -5), (3, -5), 11),
            ((4, 2), (4, -8), 10), ((-3, 7), (8, 7), 11)
        ],
        'tmpls': [
            "What is the distance between the points \\( A{0} \\) and \\( B{1} \\)?",
            "Find the length of the line segment joining the points \\( {0} \\) and \\( {1} \\).",
            "The distance between the two coordinate points \\( P{0} \\) and \\( Q{1} \\) is:",
            "Calculate the distance between \\( {0} \\) and \\( {1} \\) on the Cartesian plane.",
            "Determine the distance separating points \\( M{0} \\) and \\( N{1} \\):",
            "How many units apart are the points \\( {0} \\) and \\( {1} \\)?",
            "What is the length of segment AB with endpoints \\( A{0} \\) and \\( B{1} \\)?",
            "Find the straight-line distance between \\( {0} \\) and \\( {1} \\):",
            "The distance in units between the plotted points \\( {0} \\) and \\( {1} \\) is:",
            "Compute the distance between point \\( A{0} \\) and point \\( B{1} \\):"
        ],
        'calc': lambda item: (
            f"{item[2]} units",
            [
                f"{item[2] + 2} units",
                f"{item[2] - 2} units",
                f"{item[2] + 4} units"
            ],
            f"**Step 1: Check if points share a coordinate.**\nPoints are \\( {item[0]} \\) and \\( {item[1]} \\).\n{'Abscissae are identical (x = ' + str(item[0][0]) + '), so the segment is vertical.' if item[0][0] == item[1][0] else 'Ordinates are identical (y = ' + str(item[0][1]) + '), so the segment is horizontal.'}\n\n**Step 2: Compute absolute difference.**\nDistance = \\( |{item[1][1]} - {item[0][1]}| = {item[2]} \\) units (or \\( |{item[1][0]} - {item[0][0]}| = {item[2]} \\) units).\n\n**Step 3: State the final distance.**\nThe distance between the points is \\( {item[2]} \\) units."
        ),
        'diff': 'medium'
    }

    # Arch 4: Midpoint of segment joining two plotted points
    arch4 = {
        'data': [
            ((2, 4), (6, 8), (4, 6)), ((-4, 6), (2, -2), (-1, 2)), ((5, -3), (1, 7), (3, 2)),
            ((-6, -4), (-2, -8), (-4, -6)), ((0, 6), (8, 0), (4, 3)), ((-3, 5), (7, 1), (2, 3)),
            ((4, -1), (-2, 5), (1, 2)), ((-5, -3), (1, 9), (-2, 3)), ((6, 2), (2, -6), (4, -2)),
            ((-8, 4), (4, -4), (-2, 0))
        ],
        'tmpls': [
            "Find the midpoint of the line segment joining \\( A{0} \\) and \\( B{1} \\).",
            "What are the coordinates of the midpoint of segment connecting \\( {0} \\) and \\( {1} \\)?",
            "The midpoint of the segment with endpoints \\( P{0} \\) and \\( Q{1} \\) is:",
            "Determine the coordinates of the point equidistant from \\( {0} \\) and \\( {1} \\) along their segment:",
            "If \\( M \\) is the midpoint of segment AB with \\( A{0} \\) and \\( B{1} \\), then \\( M \\) has coordinates:",
            "Calculate the midpoint between \\( {0} \\) and \\( {1} \\):",
            "What point bisects the line segment joining \\( {0} \\) and \\( {1} \\)?",
            "Find the bisecting point of segment joining \\( {0} \\) and \\( {1} \\):",
            "The center point of the segment from \\( {0} \\) to \\( {1} \\) is:",
            "Determine the midpoint coordinates for endpoints \\( {0} \\) and \\( {1} \\):"
        ],
        'calc': lambda item: (
            f"({item[2][0]}, {item[2][1]})",
            [
                f"({item[2][1]}, {item[2][0]})",
                f"({item[2][0] + 1}, {item[2][1] - 1})",
                f"({item[0][0] + item[1][0]}, {item[0][1] + item[1][1]})"
            ],
            f"**Step 1: Recall the midpoint formula.**\nFor endpoints \\( (x_1, y_1) \\) and \\( (x_2, y_2) \\), the midpoint is:\n\\[ M = \\left(\\frac{{x_1 + x_2}}{{2}}, \\frac{{y_1 + y_2}}{{2}}\\right) \\]\n\n**Step 2: Substitute given coordinates.**\n- \\( x_M = \\frac{{{item[0][0]} + {item[1][0]}}}{{2}} = {item[2][0]} \\)\n- \\( y_M = \\frac{{{item[0][1]} + {item[1][1]}}}{{2}} = {item[2][1]} \\)\n\n**Step 3: State the midpoint.**\nThe midpoint is \\( ({item[2][0]}, {item[2][1]}) \\)."
        ),
        'diff': 'medium'
    }

    # Arch 5: Identifying fourth vertex of rectangle / parallelogram
    arch5 = {
        'data': [
            ((1, 1), (5, 1), (5, 4), (1, 4), "rectangle"),
            ((-2, 3), (4, 3), (4, -1), (-2, -1), "rectangle"),
            ((0, 0), (6, 0), (6, 5), (0, 5), "rectangle"),
            ((-3, -2), (3, -2), (3, 4), (-3, 4), "rectangle"),
            ((2, -3), (7, -3), (7, 2), (2, 2), "square"),
            ((-4, 1), (2, 1), (2, 7), (-4, 7), "square"),
            ((1, 2), (6, 2), (8, 6), (3, 6), "parallelogram"),
            ((-3, 0), (2, 0), (4, 5), (-1, 5), "parallelogram"),
            ((0, -2), (5, -2), (7, 3), (2, 3), "parallelogram"),
            ((-1, -1), (4, -1), (6, 4), (1, 4), "parallelogram")
        ],
        'tmpls': [
            "Three vertices of a {4} ABCD are \\( A{0} \\), \\( B{1} \\), and \\( C{2} \\). What are the coordinates of the fourth vertex D?",
            "If \\( A{0} \\), \\( B{1} \\), and \\( C{2} \\) are three consecutive vertices of a {4}, find the fourth vertex D.",
            "Determine the coordinates of vertex D such that ABCD forms a {4} with \\( A{0} \\), \\( B{1} \\), \\( C{2} \\):",
            "In a {4} ABCD, given \\( A{0} \\), \\( B{1} \\), and \\( C{2} \\), what are the coordinates of point D?",
            "What fourth vertex D completes the {4} with vertices \\( A{0} \\), \\( B{1} \\), and \\( C{2} \\)?",
            "Find the missing vertex D of the {4} ABCD where \\( A = {0} \\), \\( B = {1} \\), \\( C = {2} \\):",
            "Points \\( {0} \\), \\( {1} \\), and \\( {2} \\) are three vertices of a {4}. The coordinates of the fourth vertex are:",
            "To form a {4} ABCD, what must be the coordinates of D if \\( A{0} \\), \\( B{1} \\), and \\( C{2} \\)?",
            "Calculate the coordinates of the fourth corner D of {4} ABCD with \\( A{0} \\), \\( B{1} \\), \\( C{2} \\):",
            "Identify vertex D that completes the {4} given \\( A{0} \\), \\( B{1} \\), \\( C{2} \\):"
        ],
        'calc': lambda item: (
            f"({item[3][0]}, {item[3][1]})",
            [
                f"({item[3][1]}, {item[3][0]})",
                f"({item[3][0] + 1}, {item[3][1]})",
                f"({item[3][0]}, {item[3][1] - 1})"
            ],
            f"**Step 1: Use properties of parallelograms and rectangles.**\nIn any parallelogram ABCD, the diagonals bisect each other, meaning the midpoint of AC equals the midpoint of BD:\n\\[ x_A + x_C = x_B + x_D \\implies x_D = x_A + x_C - x_B \\]\n\\[ y_A + y_C = y_B + y_D \\implies y_D = y_A + y_C - y_B \\]\n\n**Step 2: Calculate coordinates of D.**\n- \\( x_D = {item[0][0]} + {item[2][0]} - {item[1][0]} = {item[3][0]} \\)\n- \\( y_D = {item[0][1]} + {item[2][1]} - {item[1][1]} = {item[3][1]} \\)\n\n**Step 3: State the fourth vertex.**\nThe fourth vertex D is \\( ({item[3][0]}, {item[3][1]}) \\)."
        ),
        'diff': 'hard'
    }

    # Arch 6: Area of simple figures formed by plotted coordinates
    arch6 = {
        'data': [
            ((0, 0), (6, 0), (6, 4), (0, 4), 24, "rectangle"),
            ((1, 2), (8, 2), (8, 7), (1, 7), 35, "rectangle"),
            ((-2, -1), (5, -1), (5, 3), (-2, 3), 28, "rectangle"),
            ((0, 0), (5, 0), (5, 5), (0, 5), 25, "square"),
            ((-3, 2), (3, 2), (3, 8), (-3, 8), 36, "square"),
            ((0, 0), (8, 0), (0, 6), None, 24, "right-angled triangle"),
            ((0, 0), (10, 0), (0, 7), None, 35, "right-angled triangle"),
            ((-4, 0), (4, 0), (0, 6), None, 24, "isosceles triangle"),
            ((2, 1), (8, 1), (5, 9), None, 24, "triangle"),
            ((0, 0), (12, 0), (0, 5), None, 30, "right-angled triangle")
        ],
        'tmpls': [
            "Find the area of the {5} with vertices {0}, {1}, and {2}{4}.",
            "What is the area in square units enclosed by the vertices {0}, {1}, and {2}{4}?",
            "Calculate the area of the polygon with vertices plotted at {0}, {1}, and {2}{4}:",
            "Determine the area of the {5} whose corners are {0}, {1}, and {2}{4}:",
            "The area of the geometric figure formed by connecting {0}, {1}, and {2}{4} is:",
            "How many square units is the area of the {5} with vertices {0}, {1}, and {2}{4}?",
            "Points {0}, {1}, and {2}{4} define a {5}. Its area is:",
            "Find the enclosed surface area of the {5} having corners at {0}, {1}, and {2}{4}:",
            "Compute the area of the shape plotted with vertices {0}, {1}, and {2}{4}:",
            "The coordinates {0}, {1}, and {2}{4} enclose an area equal to:"
        ],
        'calc': lambda item: (
            f"{item[4]} sq units",
            [
                f"{item[4] * 2} sq units",
                f"{item[4] // 2 if item[4] % 2 == 0 else item[4] / 2} sq units",
                f"{item[4] + 6} sq units"
            ],
            f"**Step 1: Determine base and height from coordinates.**\nIdentify the side lengths parallel to the coordinate axes.\nFor base along horizontal: \\( \\text{{base}} = |x_2 - x_1| \\).\nFor height along vertical: \\( \\text{{height}} = |y_2 - y_1| \\).\n\n**Step 2: Apply area formula.**\n{'Area = base × height' if 'rectangle' in item[5] or 'square' in item[5] else 'Area = (1/2) × base × height'}.\n\n**Step 3: State the final area.**\nThe area is \\( {item[4]} \\) sq units."
        ),
        'diff': 'hard'
    }

    # Arch 7: Collinearity and points lying on the same line
    arch7 = {
        'data': [
            ((1, 2), (2, 4), (3, 6), True, "lie on the straight line y = 2x"),
            ((0, 1), (2, 5), (4, 9), True, "lie on the straight line y = 2x + 1"),
            ((1, 1), (2, 3), (3, 7), False, "slopes between segments are not equal"),
            ((-2, -4), (0, 0), (3, 6), True, "lie on the straight line y = 2x"),
            ((1, 3), (2, 5), (4, 9), True, "lie on the straight line y = 2x + 1"),
            ((2, 1), (4, 2), (5, 4), False, "slopes between consecutive pairs differ"),
            ((-1, 5), (0, 3), (2, -1), True, "lie on the straight line y = -2x + 3"),
            ((1, 4), (2, 6), (3, 9), False, "rate of change is not constant"),
            ((3, 3), (5, 5), (-2, -2), True, "all lie on the line y = x"),
            ((1, 2), (3, 4), (6, 8), False, "third point does not satisfy the linear relation")
        ],
        'tmpls': [
            "Are the points \\( A{0} \\), \\( B{1} \\), and \\( C{2} \\) collinear (lie on a single straight line)?",
            "Determine whether the three points \\( {0} \\), \\( {1} \\), and \\( {2} \\) are collinear:",
            "Do the points \\( P{0} \\), \\( Q{1} \\), and \\( R{2} \\) lie on the same straight line?",
            "Check the collinearity of the points \\( {0} \\), \\( {1} \\), and \\( {2} \\):",
            "Can a single straight line pass through all three points \\( {0} \\), \\( {1} \\), and \\( {2} \\)?",
            "Regarding points \\( {0} \\), \\( {1} \\), and \\( {2} \\), are they collinear?",
            "Identify whether \\( {0} \\), \\( {1} \\), and \\( {2} \\) form a straight line:",
            "Examine if the points \\( A{0} \\), \\( B{1} \\), \\( C{2} \\) are collinear:",
            "Do the coordinates \\( {0} \\), \\( {1} \\), and \\( {2} \\) represent collinear points?",
            "State if the set of points \\( {0} \\), \\( {1} \\), and \\( {2} \\) is collinear:"
        ],
        'calc': lambda item: (
            "Yes, they are collinear" if item[3] else "No, they are not collinear",
            [
                "No, they are not collinear" if item[3] else "Yes, they are collinear",
                "Cannot be determined without a graph",
                "They form an equilateral triangle"
            ],
            f"**Step 1: Calculate slope between point 1 and point 2.**\nSlope \\( m_1 = \\frac{{y_2 - y_1}}{{x_2 - x_1}} \\).\n\n**Step 2: Calculate slope between point 2 and point 3.**\nSlope \\( m_2 = \\frac{{y_3 - y_2}}{{x_3 - x_2}} \\).\nPoints are collinear if and only if \\( m_1 = m_2 \\).\n\n**Step 3: Conclude collinearity.**\nHere, {item[4]}. Therefore, the answer is: {'Yes, they are collinear' if item[3] else 'No, they are not collinear'}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 1.2.3: Points on axes (x, 0) and (0, y)
# ==============================================================================
def gen_1_2_3():
    tc = "CBSE-9-MGM-1-1.2.3"
    tname = "Points on axes (x, 0) and (0, y)"

    # Arch 0: Identification of points lying on x-axis or y-axis
    arch0 = {
        'data': [
            (5, 0, 'x-axis'), (0, -7, 'y-axis'), (-8, 0, 'x-axis'), (0, 12, 'y-axis'),
            (14, 0, 'x-axis'), (0, -4, 'y-axis'), (-11, 0, 'x-axis'), (0, 9, 'y-axis'),
            (6, 0, 'x-axis'), (0, -15, 'y-axis')
        ],
        'tmpls': [
            "On which coordinate axis does the point \\( P({0}, {1}) \\) lie?",
            "Identify the axis on which the point \\( A({0}, {1}) \\) is situated.",
            "The coordinate point \\( ({0}, {1}) \\) lies on:",
            "To which axis does the point \\( M({0}, {1}) \\) belong?",
            "Where is the point \\( ({0}, {1}) \\) located on the Cartesian plane?",
            "Determine which axis contains the point \\( Q({0}, {1}) \\):",
            "The point \\( B({0}, {1}) \\) is positioned on:",
            "On plotting \\( ({0}, {1}) \\), it will lie on:",
            "Which coordinate axis contains the ordered pair \\( ({0}, {1}) \\)?",
            "State the axis where the point \\( S({0}, {1}) \\) is located:"
        ],
        'calc': lambda item: (
            item[2],
            [
                'y-axis' if item[2] == 'x-axis' else 'x-axis',
                'Quadrant I',
                'Quadrant II'
            ],
            f"**Step 1: Check which coordinate is zero.**\nFor the point \\( ({item[0]}, {item[1]}) \\):\n- Abscissa = \\( {item[0]} \\)\n- Ordinate = \\( {item[1]} \\)\n\n**Step 2: Apply axis conditions.**\n- If \\( y = 0 \\), the point has zero vertical displacement and lies on the x-axis.\n- If \\( x = 0 \\), the point has zero horizontal displacement and lies on the y-axis.\n\n**Step 3: State the axis.**\nSince {'ordinate is 0' if item[2] == 'x-axis' else 'abscissa is 0'}, the point lies on the {item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Solving for unknown parameter k when point lies on x-axis or y-axis
    arch1 = {
        'data': [
            ('2k - 6', 5, 'y-axis', '2k - 6 = 0', 3),
            (7, '3m - 12', 'x-axis', '3m - 12 = 0', 4),
            ('4a + 8', -9, 'y-axis', '4a + 8 = 0', -2),
            (-5, '5p + 15', 'x-axis', '5p + 15 = 0', -3),
            ('3x - 15', 8, 'y-axis', '3x - 15 = 0', 5),
            (10, '2y - 14', 'x-axis', '2y - 14 = 0', 7),
            ('5k - 20', -2, 'y-axis', '5k - 20 = 0', 4),
            (-8, '4m + 24', 'x-axis', '4m + 24 = 0', -6),
            ('6b + 18', 11, 'y-axis', '6b + 18 = 0', -3),
            (12, '7n - 21', 'x-axis', '7n - 21 = 0', 3)
        ],
        'tmpls': [
            "If the point \\( ({0}, {1}) \\) lies on the {2}, what is the value of the unknown parameter?",
            "The point \\( P({0}, {1}) \\) lies on the {2}. Find the value of the variable.",
            "Given that \\( ({0}, {1}) \\) is situated on the {2}, solve for the unknown:",
            "Find the value of the parameter such that the point \\( ({0}, {1}) \\) lies on the {2}.",
            "For what value of the variable does the point \\( ({0}, {1}) \\) lie on the {2}?",
            "Determine the value of the unknown if the point \\( ({0}, {1}) \\) belongs to the {2}:",
            "The coordinate point \\( ({0}, {1}) \\) is on the {2}. What is the value of the unknown?",
            "If \\( ({0}, {1}) \\) lies on the {2}, find the required value:",
            "Calculate the variable value when the point \\( ({0}, {1}) \\) is on the {2}:",
            "What must be the value of the parameter for \\( ({0}, {1}) \\) to lie on the {2}?"
        ],
        'calc': lambda item: (
            str(item[4]),
            [str(item[4] + 1), str(-item[4]), str(item[4] + 2)],
            f"**Step 1: Set the appropriate coordinate to zero.**\nA point lies on the {item[2]} if and only if its {'abscissa (x-coordinate)' if item[2] == 'y-axis' else 'ordinate (y-coordinate)'} is zero.\n\n**Step 2: Solve the linear equation.**\n\\[ {item[3]} \\implies \\text{{variable}} = {item[4]} \\]\n\n**Step 3: State the parameter value.**\nThe value of the unknown parameter is \\( {item[4]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Distance of axis points from the origin
    arch2 = {
        'data': [
            (7, 0, 7), (-9, 0, 9), (0, 11, 11), (0, -14, 14), (15, 0, 15),
            (-18, 0, 18), (0, 25, 25), (0, -30, 30), (13, 0, 13), (0, -17, 17)
        ],
        'tmpls': [
            "What is the distance of the point \\( P({0}, {1}) \\) from the origin?",
            "Find the distance from the origin \\( (0, 0) \\) to the point \\( A({0}, {1}) \\).",
            "The distance of the point \\( ({0}, {1}) \\) from the origin is:",
            "How far is the point \\( ({0}, {1}) \\) situated from the origin?",
            "Calculate the distance from the origin to \\( M({0}, {1}) \\):",
            "The length of the line segment connecting the origin and \\( ({0}, {1}) \\) is:",
            "Determine the distance of the point \\( ({0}, {1}) \\) from \\( (0, 0) \\):",
            "What is the straight line distance from the origin to \\( ({0}, {1}) \\)?",
            "Compute the distance between the origin and \\( P({0}, {1}) \\):",
            "The distance from origin to the axis point \\( ({0}, {1}) \\) in units is:"
        ],
        'calc': lambda item: (
            f"{item[2]} units",
            [
                f"{item[2] + 2} units",
                f"{item[2] - 1} units",
                f"{item[2] * 2} units"
            ],
            f"**Step 1: Use distance from origin formula.**\nFor any point \\( (x, y) \\), distance from origin is \\( d = \\sqrt{{x^2 + y^2}} \\).\n\n**Step 2: Evaluate for axis point.**\nHere point is \\( ({item[0]}, {item[1]}) \\).\n\\( d = \\sqrt{{{item[0]}^2 + {item[1]}^2}} = \\sqrt{{{item[2]**2}}} = {item[2]} \\) units.\n\n**Step 3: State the distance.**\nThe distance from the origin is \\( {item[2]} \\) units."
        ),
        'diff': 'easy'
    }

    # Arch 3: Points lying on positive vs negative axes
    arch3 = {
        'data': [
            (8, 0, "positive x-axis"), (-6, 0, "negative x-axis"), (0, 9, "positive y-axis"), (0, -12, "negative y-axis"),
            (15, 0, "positive x-axis"), (-20, 0, "negative x-axis"), (0, 14, "positive y-axis"), (0, -8, "negative y-axis"),
            (22, 0, "positive x-axis"), (0, -25, "negative y-axis")
        ],
        'tmpls': [
            "Specifically, on which part of the coordinate axes does the point \\( ({0}, {1}) \\) lie?",
            "The point \\( P({0}, {1}) \\) lies on the:",
            "Identify the exact semi-axis containing the point \\( A({0}, {1}) \\):",
            "In which direction along the coordinate axes is \\( ({0}, {1}) \\) located?",
            "Point \\( M({0}, {1}) \\) is situated on the:",
            "Which ray of the coordinate system contains the point \\( ({0}, {1}) \\)?",
            "Determine the specific axis section where \\( ({0}, {1}) \\) is located:",
            "The point \\( ({0}, {1}) \\) lies precisely on the:",
            "On plotting, \\( ({0}, {1}) \\) falls directly on the:",
            "State the exact axis ray where point \\( ({0}, {1}) \\) lies:"
        ],
        'calc': lambda item: (
            item[2],
            [
                "negative x-axis" if item[2] == "positive x-axis" else "positive x-axis",
                "positive y-axis" if item[2] != "positive y-axis" else "negative y-axis",
                "Quadrant I"
            ],
            f"**Step 1: Inspect the non-zero coordinate.**\nFor \\( ({item[0]}, {item[1]}) \\), the non-zero value is {'abscissa = ' + str(item[0]) if item[0] != 0 else 'ordinate = ' + str(item[1])}.\n\n**Step 2: Check sign.**\nThe non-zero value is {'positive' if item[0] > 0 or item[1] > 0 else 'negative'}.\n\n**Step 3: State the exact semi-axis.**\nThe point lies on the {item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 4: Equations of the coordinate axes themselves
    arch4 = {
        'data': [
            ("x-axis", "y = 0", ["x = 0", "x = y", "x + y = 0"], "On the x-axis, the vertical displacement (ordinate) of every point is zero."),
            ("y-axis", "x = 0", ["y = 0", "y = x", "xy = 0"], "On the y-axis, the horizontal displacement (abscissa) of every point is zero."),
            ("line parallel to x-axis at distance 5 units above it", "y = 5", ["x = 5", "y = -5", "x + y = 5"], "Every point on a horizontal line 5 units above the x-axis has ordinate y = 5."),
            ("line parallel to y-axis at distance 4 units to the left", "x = -4", ["y = -4", "x = 4", "y = 4"], "Every point on a vertical line 4 units to the left of the y-axis has abscissa x = -4."),
            ("line parallel to x-axis passing through (2, -7)", "y = -7", ["x = 2", "y = 7", "x - y = 9"], "A line parallel to the x-axis has a constant ordinate equal to that of the given point."),
            ("line parallel to y-axis passing through (-3, 8)", "x = -3", ["y = 8", "x = 3", "x + y = 5"], "A line parallel to the y-axis has a constant abscissa equal to that of the given point."),
            ("line parallel to x-axis at distance 3 units below it", "y = -3", ["y = 3", "x = -3", "x = 3"], "Below the x-axis means y is negative, so y = -3."),
            ("line parallel to y-axis at distance 6 units to the right", "x = 6", ["x = -6", "y = 6", "y = -6"], "To the right of the y-axis means x is positive, so x = 6."),
            ("axis that has equation y = 0", "x-axis", ["y-axis", "both axes", "neither axis"], "The equation y = 0 represents the x-axis."),
            ("axis that has equation x = 0", "y-axis", ["x-axis", "line y = x", "origin only"], "The equation x = 0 represents the y-axis.")
        ],
        'tmpls': [
            "What is the mathematical equation of the {0}?",
            "The equation representing the {0} is:",
            "In coordinate geometry, the {0} is given by the equation:",
            "Which equation correctly defines the {0}?",
            "Identify the equation of the {0}:",
            "State the linear equation corresponding to the {0}:",
            "The algebraic equation of the {0} is:",
            "Which of the following equations represents the {0}?",
            "Determine the equation that describes the {0}:",
            "The line corresponding to the {0} has equation:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand axis equation principles.**\n{item[3]}\n\n**Step 2: Match with algebraic representation.**\nCheck that all points on the given geometric line satisfy this equation.\n\n**Step 3: State the equation.**\nThe equation is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Midpoint of segment joining a point on x-axis and a point on y-axis
    arch5 = {
        'data': [
            ((6, 0), (0, 8), (3, 4)), ((-8, 0), (0, 6), (-4, 3)), ((10, 0), (0, -12), (5, -6)),
            ((-4, 0), (0, -10), (-2, -5)), ((12, 0), (0, 16), (6, 8)), ((-14, 0), (0, 8), (-7, 4)),
            ((16, 0), (0, -18), (8, -9)), ((-6, 0), (0, -14), (-3, -7)), ((8, 0), (0, 10), (4, 5)),
            ((-12, 0), (0, 20), (-6, 10))
        ],
        'tmpls': [
            "Point A lies on the x-axis at \\( {0} \\) and point B lies on the y-axis at \\( {1} \\). What are the coordinates of the midpoint of segment AB?",
            "Find the midpoint of the line segment joining the intercept points \\( A{0} \\) and \\( B{1} \\).",
            "What is the midpoint of segment AB where \\( A = {0} \\) and \\( B = {1} \\)?",
            "Calculate the midpoint between \\( {0} \\) on the x-axis and \\( {1} \\) on the y-axis:",
            "Determine the midpoint of the hypotenuse formed by origin intercepts \\( {0} \\) and \\( {1} \\):",
            "If \\( A{0} \\) and \\( B{1} \\) are the endpoints of a segment, its midpoint \\( M \\) is:",
            "The midpoint of the line segment between \\( {0} \\) and \\( {1} \\) has coordinates:",
            "Find the coordinates of the point halfway between \\( {0} \\) and \\( {1} \\):",
            "Segment AB connects \\( {0} \\) on the x-axis to \\( {1} \\) on the y-axis. Its midpoint is:",
            "Compute the midpoint coordinates for segment joining \\( {0} \\) and \\( {1} \\):"
        ],
        'calc': lambda item: (
            f"({item[2][0]}, {item[2][1]})",
            [
                f"({item[2][1]}, {item[2][0]})",
                f"({item[2][0] * 2}, {item[2][1] * 2})",
                f"({item[2][0] + 1}, {item[2][1] - 1})"
            ],
            f"**Step 1: Apply the midpoint formula.**\n\\[ M = \\left(\\frac{{x_1 + x_2}}{{2}}, \\frac{{y_1 + y_2}}{{2}}\\right) \\]\n\n**Step 2: Substitute the intercept coordinates.**\n- \\( x_M = \\frac{{{item[0][0]} + {item[1][0]}}}{{2}} = \\frac{{{item[0][0]} + 0}}{{2}} = {item[2][0]} \\)\n- \\( y_M = \\frac{{{item[0][1]} + {item[1][1]}}}{{2}} = \\frac{{0 + {item[1][1]}}}{{2}} = {item[2][1]} \\)\n\n**Step 3: State the midpoint.**\nThe midpoint is \\( ({item[2][0]}, {item[2][1]}) \\)."
        ),
        'diff': 'medium'
    }

    # Arch 6: Intercepts of a linear equation on coordinate axes
    arch6 = {
        'data': [
            ("2x + 3y = 12", "(6, 0)", "(0, 4)"),
            ("3x + 4y = 24", "(8, 0)", "(0, 6)"),
            ("4x - 5y = 20", "(5, 0)", "(0, -4)"),
            ("5x + 2y = 10", "(2, 0)", "(0, 5)"),
            ("x - 3y = 6", "(6, 0)", "(0, -2)"),
            ("3x - 2y = 18", "(6, 0)", "(0, -9)"),
            ("2x + 5y = 20", "(10, 0)", "(0, 4)"),
            ("4x + 3y = 12", "(3, 0)", "(0, 4)"),
            ("x + 2y = 8", "(8, 0)", "(0, 4)"),
            ("3x - 4y = 12", "(4, 0)", "(0, -3)")
        ],
        'tmpls': [
            "At which points does the line \\( {0} \\) intersect the x-axis and y-axis respectively?",
            "Find the x-intercept and y-intercept points for the line \\( {0} \\):",
            "The graph of the equation \\( {0} \\) cuts the coordinate axes at:",
            "Where does the linear equation \\( {0} \\) meet the x-axis and y-axis?",
            "Determine the points where the line \\( {0} \\) crosses the coordinate axes:",
            "The x-intercept point and y-intercept point of \\( {0} \\) are:",
            "Find the intersection coordinates of \\( {0} \\) with the x-axis and y-axis:",
            "The straight line \\( {0} \\) intersects the coordinate axes at the points:",
            "Calculate the axis intercept points for the equation \\( {0} \\):",
            "At what coordinate points does \\( {0} \\) cross the x-axis and y-axis?"
        ],
        'calc': lambda item: (
            f"{item[1]} and {item[2]}",
            [
                f"{item[2]} and {item[1]}",
                f"{item[1].replace(', 0', ', 1')} and {item[2]}",
                f"(0, 0) and {item[1]}"
            ],
            f"**Step 1: Find x-intercept (set y = 0).**\nSubstitute \\( y = 0 \\) into \\( {item[0]} \\) to find \\( x \\). The point on the x-axis is \\( {item[1]} \\).\n\n**Step 2: Find y-intercept (set x = 0).**\nSubstitute \\( x = 0 \\) into \\( {item[0]} \\) to find \\( y \\). The point on the y-axis is \\( {item[2]} \\).\n\n**Step 3: State both intercept points.**\nThe line intersects the axes at {item[1]} and {item[2]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Geometric locus of points with fixed coordinate zero or constant
    arch7 = {
        'data': [
            ("abscissa is 0", "the y-axis", ["the x-axis", "the origin only", "the line y = x"]),
            ("ordinate is 0", "the x-axis", ["the y-axis", "the origin only", "the line y = -x"]),
            ("abscissa is 0 and ordinate is 0", "the origin (0, 0)", ["both axes entirely", "the line y = x", "Quadrant I"]),
            ("abscissa is a constant non-zero value k", "a line parallel to the y-axis at distance |k|", ["a line parallel to the x-axis", "a line passing through origin", "the y-axis itself"]),
            ("ordinate is a constant non-zero value c", "a line parallel to the x-axis at distance |c|", ["a line parallel to the y-axis", "a line passing through origin", "the x-axis itself"]),
            ("distance from x-axis is 0", "the x-axis", ["the y-axis", "the origin", "the line y = 1"]),
            ("distance from y-axis is 0", "the y-axis", ["the x-axis", "the origin", "the line x = 1"]),
            ("coordinates (x, y) satisfy x² + y² = 0", "the origin (0, 0)", ["the coordinate axes", "a circle of radius 1", "the line y = -x"]),
            ("coordinates satisfy xy = 0", "the union of the x-axis and y-axis", ["the origin only", "Quadrant I and III", "empty set"]),
            ("coordinates satisfy x/y = 0", "the x-axis excluding the origin (y ≠ 0)", ["the y-axis", "the origin only", "the line x = y"])
        ],
        'tmpls': [
            "The geometric locus of all points whose {0} is:",
            "All points on the Cartesian plane for which {0} constitute:",
            "Which geometric entity represents the set of all points whose {0}?",
            "The set of points satisfying the condition that {0} is:",
            "What line, axis, or point represents all points where {0}?",
            "Identify the locus of points whose {0}:",
            "In coordinate geometry, the collection of all points where {0} is:",
            "Geometrically, points whose {0} form:",
            "Which description precisely captures all points whose {0}?",
            "The graph of the set of points where {0} is:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Translate the algebraic condition.**\nAnalyze the property: '{item[0]}'.\n\n**Step 2: Connect to Cartesian coordinates.**\nRecall the definitions of the axes, origin, and parallel lines in coordinate geometry.\n\n**Step 3: State the geometric locus.**\nThe locus is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])

if __name__ == "__main__":
    q1 = gen_1_2_1()
    q2 = gen_1_2_2()
    q3 = gen_1_2_3()
    print(f"gen_1_2_1: {len(q1)} questions generated")
    print(f"gen_1_2_2: {len(q2)} questions generated")
    print(f"gen_1_2_3: {len(q3)} questions generated")
