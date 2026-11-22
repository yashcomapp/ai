# scripts/build_cbse9_mgm_ch2_part3.py
# Subtopics:
# 2.3.1: Graphing linear polynomials y = ax + b (80 Qs)
# 2.3.2: Zero as x-intercept of the linear graph (80 Qs)

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 2
CH_NAME = "Introduction to Linear Polynomials"

# ==============================================================================
# SUBTOPIC 2.3.1: Graphing linear polynomials y = ax + b
# ==============================================================================
def gen_2_3_1():
    tc = "CBSE-9-MGM-2-2.3.1"
    tname = "Graphing linear polynomials y = ax + b"

    # Arch 0: Geometric shape of the graph of y = ax + b
    arch0 = {
        'data': [
            ("y = 2x + 3", "a straight line", ["a parabola", "a circle", "a hyperbola"]),
            ("y = -3x + 5", "a straight line", ["a curve", "an ellipse", "a parabola"]),
            ("y = 4x", "a straight line passing through the origin", ["a parabola", "a circle through origin", "a horizontal line"]),
            ("y = -x", "a straight line passing through origin bisecting Quadrants II and IV", ["a line through Quadrants I and III", "a parabola", "a vertical line"]),
            ("y = x", "a straight line passing through origin bisecting Quadrants I and III", ["a horizontal line", "a curve", "a circle"]),
            ("y = 7", "a straight line parallel to the x-axis", ["a straight line parallel to the y-axis", "a line passing through origin", "a parabola"]),
            ("x = -4", "a straight line parallel to the y-axis", ["a straight line parallel to the x-axis", "a curve", "a slanted line"]),
            ("y = \\frac{1}{2}x - 2", "a straight line", ["a circular arc", "a hyperbola", "an exponential curve"]),
            ("y = -5x - 8", "a straight line falling from left to right", ["a horizontal line", "a parabola", "a circle"]),
            ("y = 3x - 1", "a straight line rising from left to right", ["a line falling from left to right", "a horizontal line", "a curve"])
        ],
        'tmpls': [
            "The graph of the equation \\( {0} \\) in the Cartesian plane is:",
            "Geometrically, what is the shape of the graph of \\( {0} \\)?",
            "What does the graph of \\( {0} \\) represent?",
            "In coordinate geometry, the graphical representation of \\( {0} \\) is:",
            "Which description characterizes the graph of \\( {0} \\)?",
            "The linear equation \\( {0} \\) graphs as:",
            "When plotted on graph paper, the equation \\( {0} \\) forms:",
            "Identify the geometric graph corresponding to \\( {0} \\):",
            "What type of geometric curve or line is formed by \\( {0} \\)?",
            "The locus of all points satisfying \\( {0} \\) is:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify the degree of the equation.**\nThe equation \\( {item[0]} \\) is linear (degree 1) in one or two variables.\n\n**Step 2: Recall the geometric theorem.**\nEvery linear equation in one or two variables graphs as a straight line in the Cartesian plane.\n\n**Step 3: State the conclusion.**\nThe graph is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Finding y-intercept of the line y = ax + b
    arch1 = {
        'data': [
            ("y = 3x + 7", "(0, 7)"), ("y = -2x + 9", "(0, 9)"), ("y = 5x - 4", "(0, -4)"),
            ("y = -4x - 11", "(0, -11)"), ("y = 6x", "(0, 0)"), ("y = -x + 8", "(0, 8)"),
            ("y = \\frac{2}{3}x - 5", "(0, -5)"), ("y = 8x + 15", "(0, 15)"),
            ("y = -7x", "(0, 0)"), ("y = 4 - 3x", "(0, 4)")
        ],
        'tmpls': [
            "At which point does the graph of the line \\( {0} \\) intersect the y-axis?",
            "Find the y-intercept of the line \\( {0} \\).",
            "The line \\( {0} \\) crosses the vertical y-axis at which coordinates?",
            "What are the coordinates of the y-intercept for \\( {0} \\)?",
            "Determine the point of intersection of the line \\( {0} \\) with the y-axis:",
            "Where does the linear graph of \\( {0} \\) cut the y-axis?",
            "The point on the y-axis lying on the line \\( {0} \\) is:",
            "Calculate the coordinates of the y-intercept of \\( {0} \\):",
            "Find where the line \\( {0} \\) meets the y-axis:",
            "The graph of \\( {0} \\) intersects the y-axis at:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("0, ", "").replace("(", "").replace(")", ""),
                f"({item[1].split(', ')[1][:-1]}, 0)",
                "(1, 1)"
            ],
            f"**Step 1: Set \\( x = 0 \\) to find the y-intercept.**\nOn the y-axis, the x-coordinate is always zero.\n\n**Step 2: Substitute \\( x = 0 \\) into the equation.**\nSubstitute \\( x = 0 \\) into \\( {item[0]} \\) to obtain the y-value.\n\n**Step 3: Write as coordinate point.**\nThe point of intersection with the y-axis is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Checking whether a point lies on the line y = ax + b
    arch2 = {
        'data': [
            ("y = 2x + 1", (3, 7), True), ("y = 3x - 4", (2, 5), False), ("y = -x + 6", (4, 2), True),
            ("y = 4x + 3", (-1, -1), True), ("y = 5x - 2", (3, 11), False), ("y = -2x + 8", (5, -2), True),
            ("y = 3x + 5", (-2, -1), True), ("y = 6x - 7", (2, 8), False), ("y = -3x - 1", (-2, 5), True),
            ("y = 2x - 9", (4, -1), True)
        ],
        'tmpls': [
            "Does the point \\( P{1} \\) lie on the graph of the line \\( {0} \\)?",
            "Check whether the point \\( {1} \\) satisfies the linear equation \\( {0} \\).",
            "Determine if the line \\( {0} \\) passes through the point \\( {1} \\):",
            "Is the point \\( {1} \\) a solution to the equation \\( {0} \\)?",
            "Verify whether \\( {1} \\) lies on the straight line \\( {0} \\):",
            "Does the line \\( {0} \\) contain the coordinate point \\( {1} \\)?",
            "Test whether point \\( {1} \\) belongs to the graph of \\( {0} \\):",
            "Will the straight line \\( {0} \\) pass through the point \\( {1} \\)?",
            "Is \\( {1} \\) on the line \\( {0} \\)?",
            "Confirm if the point \\( {1} \\) lies on the graph of \\( {0} \\):"
        ],
        'calc': lambda item: (
            "Yes, it lies on the line" if item[2] else "No, it does not lie on the line",
            [
                "No, it does not lie on the line" if item[2] else "Yes, it lies on the line",
                "It is the y-intercept",
                "Cannot be determined without a graph"
            ],
            f"**Step 1: Substitute the coordinates into the equation.**\nSubstitute \\( x = {item[1][0]} \\) and \\( y = {item[1][1]} \\) into \\( {item[0]} \\).\n\n**Step 2: Check if LHS equals RHS.**\nEvaluate the right-hand side and compare with the left-hand side.\n\n**Step 3: State the conclusion.**\n{'Yes, it lies on the line' if item[2] else 'No, it does not lie on the line'}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Parallel lines having the same slope
    arch3 = {
        'data': [
            ("y = 3x + 4", "y = 3x - 7", True), ("y = -2x + 5", "y = -2x + 11", True),
            ("y = 4x - 1", "y = 2x + 5", False), ("y = 5x + 2", "y = 5x", True),
            ("y = -x + 3", "y = x - 3", False), ("y = 6x - 8", "y = 6x + 9", True),
            ("y = \\frac{1}{2}x + 4", "y = \\frac{1}{2}x - 3", True), ("y = 3x + 1", "y = -3x + 1", False),
            ("y = -4x + 6", "y = -4x - 2", True), ("y = 7x - 5", "y = 8x - 5", False)
        ],
        'tmpls': [
            "Are the graphs of the two linear equations \\( {0} \\) and \\( {1} \\) parallel lines?",
            "Determine whether the lines \\( {0} \\) and \\( {1} \\) are parallel to each other.",
            "Do the lines \\( {0} \\) and \\( {1} \\) ever intersect in the Cartesian plane?",
            "Check if the lines represented by \\( {0} \\) and \\( {1} \\) are parallel:",
            "Are \\( {0} \\) and \\( {1} \\) parallel straight lines?",
            "Regarding \\( {0} \\) and \\( {1} \\), are their graphs parallel?",
            "Identify whether the pair of lines \\( {0} \\) and \\( {1} \\) is parallel:",
            "Examine if \\( {0} \\) and \\( {1} \\) have equal slopes and are parallel:",
            "Will the lines \\( {0} \\) and \\( {1} \\) run parallel to each other?",
            "Confirm whether \\( {0} \\) is parallel to \\( {1} \\):"
        ],
        'calc': lambda item: (
            "Yes, they are parallel" if item[2] else "No, they are not parallel",
            [
                "No, they are not parallel" if item[2] else "Yes, they are parallel",
                "They are perpendicular",
                "They are coincident (identical) lines"
            ],
            f"**Step 1: Identify the slopes (coefficients of x) of both lines.**\nIn the slope-intercept form \\( y = ax + b \\), the coefficient \\( a \\) represents the slope.\n\n**Step 2: Compare the slopes.**\nTwo non-vertical lines are parallel if and only if their slopes are equal.\n\n**Step 3: State the conclusion.**\n{'Yes, they are parallel' if item[2] else 'No, they are not parallel'}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Direction / Slope orientation of the line (rising vs falling)
    arch4 = {
        'data': [
            ("y = 4x - 5", "rises from left to right (slope > 0, acute angle with +x-axis)", ["falls from left to right", "is horizontal", "is vertical"]),
            ("y = -3x + 8", "falls from left to right (slope < 0, obtuse angle with +x-axis)", ["rises from left to right", "is horizontal", "is vertical"]),
            ("y = 5", "is horizontal (slope = 0, parallel to x-axis)", ["is vertical", "rises from left to right", "falls from left to right"]),
            ("y = -2x - 3", "falls from left to right (slope < 0, obtuse angle with +x-axis)", ["rises from left to right", "is horizontal", "passes through origin"]),
            ("y = \\frac{3}{2}x + 1", "rises from left to right (slope > 0, acute angle with +x-axis)", ["falls from left to right", "is horizontal", "is vertical"]),
            ("y = -x + 4", "falls from left to right (slope < 0, obtuse angle with +x-axis)", ["rises from left to right", "is horizontal", "bisects Quad I"]),
            ("y = 7x", "rises from left to right and passes through the origin", ["falls from left to right", "is horizontal", "parallel to y-axis"]),
            ("y = -6x", "falls from left to right and passes through the origin", ["rises from left to right", "is horizontal", "parallel to x-axis"]),
            ("y = 0", "coincides with the horizontal x-axis (slope = 0)", ["is vertical", "rises at 45°", "falls at 45°"]),
            ("y = 8x + 10", "rises from left to right (slope > 0, acute angle with +x-axis)", ["falls from left to right", "is horizontal", "is vertical"])
        ],
        'tmpls': [
            "How does the straight line \\( {0} \\) orient in the Cartesian plane?",
            "Describe the direction and inclination of the line \\( {0} \\):",
            "The graph of the linear equation \\( {0} \\):",
            "Which description characterizes the behavior of the line \\( {0} \\)?",
            "What is the orientation of the line \\( {0} \\) as \\( x \\) increases?",
            "In terms of slope and angle with the positive x-axis, the line \\( {0} \\):",
            "Determine the directional behavior of the line \\( {0} \\):",
            "Regarding its graphical trajectory, the line \\( {0} \\):",
            "How does the line \\( {0} \\) behave across the quadrants?",
            "The graph of \\( {0} \\) is a straight line that:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Check the sign of the slope \\( a \\) in \\( y = ax + b \\).**\n- If \\( a > 0 \\), the line rises from left to right (makes an acute angle with the positive x-axis).\n- If \\( a < 0 \\), the line falls from left to right (makes an obtuse angle with the positive x-axis).\n- If \\( a = 0 \\), the line is horizontal (parallel to x-axis).\n\n**Step 2: Inspect \\( {item[0]} \\).**\nAnalyze the slope of the given equation.\n\n**Step 3: State the orientation.**\nThe line {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Minimum points needed to uniquely determine a straight line
    arch5 = {
        'data': [
            ("minimum number of distinct points required to uniquely determine a straight line", "2 points", ["1 point", "3 points", "infinitely many"]),
            ("number of straight lines that can pass through a single given point", "infinitely many lines", ["only 1 line", "2 lines", "0 lines"]),
            ("the graph of every linear polynomial y = ax + b (a ≠ 0) cuts the y-axis at", "exactly 1 point (0, b)", ["2 points", "no points", "infinitely many points"]),
            ("the graph of every linear polynomial y = ax + b (a ≠ 0) cuts the x-axis at", "exactly 1 point (-b/a, 0)", ["2 points", "no points", "infinitely many points"]),
            ("condition for the graph of y = ax + b to pass through the origin", "b = 0", ["a = 0", "a = b", "a + b = 0"]),
            ("a straight line parallel to the x-axis has slope equal to", "0", ["1", "undefined", "-1"]),
            ("a straight line parallel to the y-axis has slope equal to", "undefined (infinite)", ["0", "1", "-1"]),
            ("two distinct lines with equal slopes are", "parallel and never meet", ["perpendicular", "intersecting at 1 point", "coincident"]),
            ("the point of intersection of two non-parallel lines y = a₁x + b₁ and y = a₂x + b₂ is", "unique (exactly 1 point)", ["2 points", "no point", "infinitely many points"]),
            ("if a point (x₁, y₁) lies on the graph of y = ax + b, then (x₁, y₁) is", "a solution to the linear equation", ["an extraneous root", "an asymptote", "the origin"])
        ],
        'tmpls': [
            "What is the {0}?",
            "In coordinate geometry, {0} is:",
            "Identify the correct geometric fact: {0}:",
            "Which statement correctly specifies the {0}?",
            "State the {0}:",
            "According to the axioms of geometry, the {0} is:",
            "Determine the {0}:",
            "What can be stated regarding the {0}?",
            "Which of the following defines the {0}?",
            "Select the correct answer concerning the {0}:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall Euclidean axioms and Cartesian geometry theorems.**\nConsider the property '{item[0]}'.\n\n**Step 2: Apply the relevant geometric principle.**\nVerify against the standard definitions of lines and linear equations.\n\n**Step 3: State the result.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Finding value of parameter k when line passes through a given point
    arch6 = {
        'data': [
            ("y = 3x + k", (2, 11), 5), ("y = 2x + k", (4, 15), 7), ("y = -4x + k", (3, -2), 10),
            ("y = kx + 4", (3, 13), 3), ("y = kx - 5", (2, 9), 7), ("y = -2x + k", (-3, 4), -2),
            ("y = 5x + k", (-2, -6), 4), ("y = kx + 8", (4, 0), -2), ("y = 3x + k", (-1, 2), 5),
            ("y = kx - 1", (5, 14), 3)
        ],
        'tmpls': [
            "If the graph of the line \\( {0} \\) passes through the point \\( P{1} \\), find the value of \\( k \\).",
            "The line \\( {0} \\) contains the coordinate point \\( {1} \\). What is the value of \\( k \\)?",
            "Find \\( k \\) given that the point \\( {1} \\) lies on the line \\( {0} \\):",
            "Determine the value of \\( k \\) such that \\( {1} \\) satisfies \\( {0} \\):",
            "Calculate \\( k \\) if the straight line \\( {0} \\) passes through \\( {1} \\):",
            "For what value of \\( k \\) will the graph of \\( {0} \\) pass through \\( {1} \\)?",
            "The coordinate point \\( {1} \\) is on the line \\( {0} \\). Find \\( k \\):",
            "Solve for \\( k \\) given that \\( {1} \\) is on the line \\( {0} \\):",
            "Find the unknown constant \\( k \\) if \\( {0} \\) contains \\( {1} \\):",
            "What must be the value of \\( k \\) if the line \\( {0} \\) goes through \\( {1} \\)?"
        ],
        'calc': lambda item: (
            str(item[2]),
            [str(item[2] + 2), str(-item[2]), str(item[2] - 3)],
            f"**Step 1: Substitute the coordinates into the line equation.**\nSubstitute \\( x = {item[1][0]} \\) and \\( y = {item[1][1]} \\) into \\( {item[0]} \\).\n\n**Step 2: Solve the linear equation for \\( k \\).**\nRearrange to isolate \\( k \\).\n\n**Step 3: State the value of \\( k \\).**\n\\( k = {item[2]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 7: Quadrants through which the line y = ax + b passes
    arch7 = {
        'data': [
            ("y = 2x + 4", "Quadrants I, II, and III (does NOT pass through IV)", ["Quadrants I, II, and IV", "Quadrants II, III, and IV", "Quadrants I, III, and IV"]),
            ("y = 2x - 4", "Quadrants I, III, and IV (does NOT pass through II)", ["Quadrants I, II, and III", "Quadrants II, III, and IV", "Quadrants I, II, and IV"]),
            ("y = -2x + 4", "Quadrants I, II, and IV (does NOT pass through III)", ["Quadrants I, II, and III", "Quadrants II, III, and IV", "Quadrants I, III, and IV"]),
            ("y = -2x - 4", "Quadrants II, III, and IV (does NOT pass through I)", ["Quadrants I, II, and III", "Quadrants I, II, and IV", "Quadrants I, III, and IV"]),
            ("y = 3x", "Quadrants I and III and origin only", ["Quadrants II and IV", "Quadrants I, II, and III", "All four quadrants"]),
            ("y = -3x", "Quadrants II and IV and origin only", ["Quadrants I and III", "Quadrants I, II, and IV", "All four quadrants"]),
            ("y = 5", "Quadrants I and II only", ["Quadrants III and IV", "Quadrants I and IV", "Quadrants II and III"]),
            ("y = -5", "Quadrants III and IV only", ["Quadrants I and II", "Quadrants II and III", "Quadrants I and IV"]),
            ("x = 4", "Quadrants I and IV only", ["Quadrants II and III", "Quadrants I and II", "Quadrants III and IV"]),
            ("x = -4", "Quadrants II and III only", ["Quadrants I and IV", "Quadrants I and II", "Quadrants I and III"])
        ],
        'tmpls': [
            "Through which quadrants does the graph of the line \\( {0} \\) pass?",
            "Identify the quadrants traversed by the straight line \\( {0} \\):",
            "The line \\( {0} \\) passes through which sections of the Cartesian plane?",
            "Determine the quadrants containing points of the line \\( {0} \\):",
            "Which quadrants does the linear graph of \\( {0} \\) cross?",
            "In which quadrants does the line \\( {0} \\) lie?",
            "The straight line \\( {0} \\) intersects:",
            "Find all quadrants through which the line \\( {0} \\) passes:",
            "What quadrants are entered by the line \\( {0} \\)?",
            "The graph of the equation \\( {0} \\) passes through:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Find both axis intercepts.**\n- x-intercept (set \\( y = 0 \\))\n- y-intercept (set \\( x = 0 \\))\n\n**Step 2: Connect the intercepts to trace the line.**\nDetermine which three quadrants are traversed by the straight line connecting the intercepts.\n\n**Step 3: State the quadrants.**\nThe line passes through {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 2.3.2: Zero as x-intercept of the linear graph
# ==============================================================================
def gen_2_3_2():
    tc = "CBSE-9-MGM-2-2.3.2"
    tname = "Zero as x-intercept of the linear graph"

    # Arch 0: Connecting zero to x-intercept coordinate point
    arch0 = {
        'data': [
            ("y = 2x - 6", 3, "(3, 0)"), ("y = 3x - 12", 4, "(4, 0)"), ("y = 4x + 8", -2, "(-2, 0)"),
            ("y = 5x - 25", 5, "(5, 0)"), ("y = -2x + 10", 5, "(5, 0)"), ("y = -3x - 9", -3, "(-3, 0)"),
            ("y = 6x + 18", -3, "(-3, 0)"), ("y = 4x - 20", 5, "(5, 0)"), ("y = -5x + 30", 6, "(6, 0)"),
            ("y = 7x - 14", 2, "(2, 0)")
        ],
        'tmpls': [
            "What are the coordinates of the point where the graph of the linear polynomial \\( {0} \\) cuts the x-axis?",
            "The line \\( {0} \\) intersects the horizontal x-axis at which point?",
            "Find the x-intercept point of the line \\( {0} \\).",
            "At which coordinate point does \\( {0} \\) cross the x-axis?",
            "Determine the point where the graph of \\( {0} \\) meets the x-axis:",
            "The zero of the polynomial is \\( x = {1} \\). What is the corresponding x-intercept point on the graph?",
            "What is the point of intersection of \\( {0} \\) with the x-axis?",
            "The linear graph of \\( {0} \\) crosses the x-axis at:",
            "Find the coordinates of the point on the x-axis satisfying \\( {0} \\):",
            "Where does the line \\( {0} \\) touch or cross the x-axis?"
        ],
        'calc': lambda item: (
            item[2],
            [
                f"(0, {item[1]})",
                f"({-item[1]}, 0)",
                "(0, 0)"
            ],
            f"**Step 1: Set \\( y = 0 \\) to find the x-intercept.**\nOn the x-axis, the ordinate is zero: \\( y = 0 \\).\n\n**Step 2: Solve for \\( x \\).**\nSubstitute \\( y = 0 \\) into \\( {item[0]} \\) to find \\( x = {item[1]} \\).\n\n**Step 3: Write as an ordered pair.**\nThe point on the x-axis is {item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Reading zero from graph coordinates
    arch1 = {
        'data': [
            ("(5, 0)", 5), ("(-4, 0)", -4), ("(7, 0)", 7), ("(-6, 0)", -6),
            ("(2.5, 0)", 2.5), ("(-1.5, 0)", -1.5), ("(8, 0)", 8), ("(-10, 0)", -10),
            ("(3, 0)", 3), ("(-1, 0)", -1)
        ],
        'tmpls': [
            "If the graph of a linear polynomial \\( y = p(x) \\) intersects the x-axis at \\( {0} \\), what is the zero of the polynomial?",
            "The line \\( y = p(x) \\) crosses the x-axis at the point \\( {0} \\). Find the zero of \\( p(x) \\).",
            "What is the zero of \\( p(x) \\) given that its linear graph passes through the x-axis at \\( {0} \\)?",
            "From the graphical x-intercept at \\( {0} \\), determine the zero of the linear polynomial:",
            "A linear graph \\( y = p(x) \\) has x-intercept \\( {0} \\). The root of \\( p(x) = 0 \\) is:",
            "Given that \\( p(x) \\) meets the x-axis at \\( {0} \\), its zero equals:",
            "Identify the zero of the polynomial whose graph cuts the x-axis at \\( {0} \\):",
            "What zero corresponds to the graphical x-intercept \\( {0} \\)?",
            "If the line \\( y = p(x) \\) intersects the x-axis at \\( {0} \\), the zero of \\( p(x) \\) is:",
            "Find the root of \\( p(x) = 0 \\) when the line cuts the horizontal axis at \\( {0} \\):"
        ],
        'calc': lambda item: (
            str(item[1]),
            [str(-item[1]), "0", str(item[1] + 1)],
            f"**Step 1: Understand graphical meaning of zero.**\nThe zero of a polynomial \\( p(x) \\) is the x-coordinate of the point where its graph \\( y = p(x) \\) intersects the x-axis.\n\n**Step 2: Extract the x-coordinate.**\nThe given x-intercept is \\( {item[0]} \\), so the x-coordinate is \\( {item[1]} \\).\n\n**Step 3: State the zero.**\nThe zero of \\( p(x) \\) is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Area of triangle bounded by line y = ax + b and coordinate axes
    arch2 = {
        'data': [
            ("y = -2x + 6", 3, 6, 9),
            ("y = -3x + 12", 4, 12, 24),
            ("y = -4x + 8", 2, 8, 8),
            ("y = -x + 6", 6, 6, 18),
            ("y = -5x + 10", 2, 10, 10),
            ("y = 2x - 8", 4, 8, 16),
            ("y = 3x - 6", 2, 6, 6),
            ("y = 4x - 12", 3, 12, 18),
            ("y = -2x + 10", 5, 10, 25),
            ("y = -6x + 12", 2, 12, 12)
        ],
        'tmpls': [
            "Find the area of the triangle formed by the line \\( {0} \\) with the coordinate axes.",
            "What is the area of the triangle enclosed by the coordinate axes and the straight line \\( {0} \\)?",
            "Calculate the area in square units bounded by the axes and \\( {0} \\):",
            "The line \\( {0} \\) forms a right-angled triangle with the x-axis and y-axis. What is its area?",
            "Determine the area of the triangle formed by the line \\( {0} \\) and the two axes:",
            "Find the enclosed triangle area between the coordinate axes and \\( {0} \\):",
            "How many square units is the area of the triangle bounded by \\( {0} \\), the x-axis, and the y-axis?",
            "Compute the area of the region bounded by \\( {0} \\) and the coordinate axes:",
            "The area of the right triangle whose legs lie along the axes and hypotenuse along \\( {0} \\) is:",
            "What area is enclosed by \\( {0} \\) and the positive/negative coordinate axes?"
        ],
        'calc': lambda item: (
            f"{item[3]} sq units",
            [
                f"{item[3] * 2} sq units",
                f"{item[3] + 4} sq units",
                f"{item[3] - 2} sq units"
            ],
            f"**Step 1: Find the intercepts.**\n- x-intercept: set \\( y = 0 \\implies x = {item[1]} \\)\n- y-intercept: set \\( x = 0 \\implies y = {item[2]} \\)\n\n**Step 2: Apply right triangle area formula.**\n\\[ \\text{{Area}} = \\frac{{1}}{{2}} \\times |\\text{{base}}| \\times |\\text{{height}}| = \\frac{{1}}{{2}} \\times {item[1]} \\times {item[2]} = {item[3]} \\text{{ sq units}} \\]\n\n**Step 3: State the area.**\nThe area is \\( {item[3]} \\) sq units."
        ),
        'diff': 'medium'
    }

    # Arch 3: Number of zeroes vs number of x-intercepts
    arch3 = {
        'data': [
            ("a linear polynomial p(x) = ax + b with a ≠ 0", "has exactly 1 zero and cuts x-axis at exactly 1 point", ["has 2 zeroes", "has no zero", "cuts x-axis at 2 points"]),
            ("a non-zero constant polynomial p(x) = c (c ≠ 0)", "has 0 zeroes and never intersects the x-axis (parallel line y = c)", ["has 1 zero", "intersects at (c, 0)", "has infinitely many zeroes"]),
            ("the zero polynomial p(x) = 0", "has infinitely many zeroes and coincides with the entire x-axis", ["has 0 zeroes", "has exactly 1 zero", "does not intersect x-axis"]),
            ("a polynomial of degree n", "can have at most n zeroes and intersect x-axis at most n times", ["must have exactly 2n zeroes", "has n + 1 zeroes", "always has 0 zeroes"]),
            ("if the graph of y = p(x) does not intersect the x-axis at any real point", "the polynomial has no real zeroes", ["the polynomial has infinitely many zeroes", "the degree must be 1", "it is the zero polynomial"]),
            ("if the graph of y = p(x) touches the x-axis at exactly one point", "that point represents a repeated zero", ["the polynomial has no zeroes", "the degree is not defined", "it is a linear polynomial"]),
            ("the x-coordinate of the intersection point of y = p(x) with the x-axis", "is the real zero of p(x)", ["is the y-intercept", "is the slope", "is the constant term"]),
            ("geometrically, solving p(x) = 0 is equivalent to finding", "the x-intercept(s) of the graph y = p(x)", ["the y-intercept of the graph", "the slope of the tangent", "the distance from origin"]),
            ("a linear graph y = ax + b passes through the origin if and only if", "its zero is x = 0 (b = 0)", ["its zero is x = 1", "its slope is zero", "it has no zero"]),
            ("the graph of y = 4 cuts the x-axis at", "no point (0 x-intercepts)", ["(4, 0)", "(0, 4)", "infinitely many points"])
        ],
        'tmpls': [
            "In coordinate algebra, {0}:",
            "Which statement correctly describes {0}?",
            "What can be concluded regarding {0}?",
            "Identify the geometric-algebraic relationship: {0}:",
            "State the theorem concerning {0}:",
            "According to polynomial graphing principles, {0}:",
            "Regarding zeroes and x-intercepts, {0}:",
            "Determine the true statement: {0}:",
            "In graphical analysis of polynomials, {0}:",
            "Which of the following is accurate concerning {0}?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the geometric definition of polynomial zeroes.**\nConsider the concept: '{item[0]}'.\n\n**Step 2: Connect the real zeroes with x-axis intersections.**\nEvery real root of \\( p(x) = 0 \\) corresponds to a point \\( (x, 0) \\) on the graph of \\( y = p(x) \\).\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Solving for parameter k when x-intercept is given
    arch4 = {
        'data': [
            ("y = 2x - k", 5, 10), ("y = 3x + k", -4, 12), ("y = 4x - k", 3, 12),
            ("y = 5x + 2k", -2, 5), ("y = -2x + k", 4, 8), ("y = -3x - k", -3, 9),
            ("y = kx - 12", 4, 3), ("y = kx + 15", -5, 3), ("y = 6x - k", 3, 18),
            ("y = -4x + 2k", 2, 4)
        ],
        'tmpls': [
            "If the line \\( {0} \\) has an x-intercept at \\( x = {1} \\), what is the value of \\( k \\)?",
            "The graph of \\( {0} \\) crosses the x-axis at \\( ({1}, 0) \\). Find \\( k \\).",
            "Find the value of \\( k \\) given that \\( x = {1} \\) is the zero of \\( {0} \\):",
            "Determine \\( k \\) such that the line \\( {0} \\) passes through \\( ({1}, 0) \\):",
            "At \\( x = {1} \\), the line \\( {0} \\) intersects the x-axis. Calculate \\( k \\):",
            "For what value of \\( k \\) does the line \\( {0} \\) have x-intercept \\( {1} \\)?",
            "The line \\( {0} \\) cuts the horizontal axis at \\( ({1}, 0) \\). Find \\( k \\):",
            "Calculate \\( k \\) if the zero of the linear graph \\( {0} \\) is \\( {1} \\):",
            "What must \\( k \\) be if the graph of \\( {0} \\) has x-intercept at \\( {1} \\)?",
            "Solve for \\( k \\) given that \\( ({1}, 0) \\) lies on the line \\( {0} \\):"
        ],
        'calc': lambda item: (
            str(item[2]),
            [str(item[2] + 2), str(-item[2]), str(item[2] - 3)],
            f"**Step 1: Substitute the x-intercept point into the equation.**\nSince \\( x = {item[1]} \\) is the x-intercept, substitute \\( x = {item[1]} \\) and \\( y = 0 \\) into \\( {item[0]} \\).\n\n**Step 2: Solve for \\( k \\).**\nRearrange the resulting linear equation to solve for \\( k \\).\n\n**Step 3: State the value of \\( k \\).**\n\\( k = {item[2]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 5: Hypotenuse length of triangle formed by line and axes
    arch5 = {
        'data': [
            ("y = -\\frac{4}{3}x + 4", 3, 4, 5),
            ("y = -\\frac{3}{4}x + 3", 4, 3, 5),
            ("y = -\\frac{8}{6}x + 8", 6, 8, 10),
            ("y = -\\frac{12}{5}x + 12", 5, 12, 13),
            ("y = -\\frac{5}{12}x + 5", 12, 5, 13),
            ("y = -2x + 8", 4, 8, "\\sqrt{80} = 4\\sqrt{5}"),
            ("y = -x + 5", 5, 5, "5\\sqrt{2}"),
            ("y = -\\frac{15}{8}x + 15", 8, 15, 17),
            ("y = -\\frac{8}{15}x + 8", 15, 8, 17),
            ("y = -x + 7", 7, 7, "7\\sqrt{2}")
        ],
        'tmpls': [
            "What is the length of the segment of the line \\( {0} \\) intercepted between the coordinate axes?",
            "Find the length of the hypotenuse formed by the line \\( {0} \\) with the x and y axes.",
            "The portion of the line \\( {0} \\) lying between the coordinate axes has length:",
            "Calculate the distance between the x-intercept and y-intercept of the line \\( {0} \\):",
            "What is the distance between the points where \\( {0} \\) intersects the coordinate axes?",
            "Determine the length of the segment of \\( {0} \\) between the coordinate axes:",
            "Find the length of the line segment joining the intercepts of \\( {0} \\):",
            "The distance between \\( (x_0, 0) \\) and \\( (0, y_0) \\) for \\( {0} \\) is:",
            "Compute the length of the hypotenuse of the triangle formed by \\( {0} \\) and the axes:",
            "What is the length of the line intercepted between the axes by \\( {0} \\)?"
        ],
        'calc': lambda item: (
            f"{item[3]} units",
            [
                f"{item[1] + item[2]} units",
                f"{abs(item[1] - item[2])} units",
                f"{item[1] * item[2]} units"
            ],
            f"**Step 1: Find the intercept points.**\n- x-intercept: \\( ({item[1]}, 0) \\)\n- y-intercept: \\( (0, {item[2]}) \\)\n\n**Step 2: Apply the Pythagoras theorem.**\n\\[ d = \\sqrt{{{item[1]}^2 + {item[2]}^2}} = {item[3]} \\text{{ units}} \\]\n\n**Step 3: State the length.**\nThe length of the intercepted segment is \\( {item[3]} \\) units."
        ),
        'diff': 'hard'
    }

    # Arch 6: Reflection of the zero across the origin or axes
    arch6 = {
        'data': [
            ("y = 2x - 8", 4, -4), ("y = 3x + 15", -5, 5), ("y = 5x - 35", 7, -7),
            ("y = -4x + 12", 3, -3), ("y = -2x - 14", -7, 7), ("y = 6x - 18", 3, -3),
            ("y = 4x + 24", -6, 6), ("y = -5x + 40", 8, -8), ("y = 7x - 21", 3, -3),
            ("y = -3x - 18", -6, 6)
        ],
        'tmpls': [
            "If \\( c \\) is the zero of the linear polynomial \\( {0} \\), what is the value of \\( -c \\) (the reflection of the zero across the origin)?",
            "Find the opposite of the zero of \\( {0} \\).",
            "What is the additive inverse of the zero of the polynomial \\( {0} \\)?",
            "The reflection of the zero of \\( {0} \\) across the origin is:",
            "Calculate \\( -c \\) where \\( c \\) is the zero of \\( {0} \\):",
            "Determine the negative of the root of \\( {0} = 0 \\):",
            "If \\( c \\) is the x-intercept of \\( {0} \\), find \\( -c \\):",
            "The additive inverse of the root of \\( {0} \\) is:",
            "Find the reflection through origin of the zero of \\( {0} \\):",
            "Compute \\( -c \\) where \\( c \\) satisfies \\( {0} \\) with \\( y = 0 \\):"
        ],
        'calc': lambda item: (
            str(item[2]),
            [str(item[1]), str(item[2] + 1), str(item[2] - 2)],
            f"**Step 1: Find the zero \\( c \\) of \\( {item[0]} \\).**\nSet \\( y = 0 \\) to find \\( c = {item[1]} \\).\n\n**Step 2: Negate the zero to find \\( -c \\).**\n\\( -c = -({item[1]}) = {item[2]} \\).\n\n**Step 3: State the reflected value.**\nThe value is \\( {item[2]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 7: Real-world applications of x-intercepts
    arch7 = {
        'data': [
            ("A water storage tank starts with 500 liters and drains at 25 L/min: y = -25x + 500. What does the x-intercept (20, 0) represent?", "The time (20 minutes) when the tank becomes completely empty", ["The initial water volume", "The rate of water outflow", "The capacity of the pump"]),
            ("An airplane descends according to y = -150x + 3000 where y is altitude in meters and x is minutes. What does the x-intercept represent?", "The time (20 minutes) when the plane lands on the ground (altitude = 0)", ["The cruising altitude", "The descent speed", "The distance from the airport"]),
            ("A company's profit in thousands is y = 10x - 80 for x units sold. What does the x-intercept (8, 0) represent?", "The break-even sales volume (8 units) where profit is zero", ["The maximum profit achievable", "The fixed manufacturing overhead", "The sales tax rate"]),
            ("A phone battery percentage drops as y = -5x + 100 after x hours. What is the practical meaning of the x-intercept?", "The battery lifespan (20 hours) until completely discharged (0%)", ["The full battery capacity", "The charging speed", "The current screen brightness"]),
            ("A diver descends and returns to surface according to depth profile y = 2x - 16 meters where y=0 is sea surface. What does x=8 represent?", "The time (8 minutes) when the diver resurfaces", ["The maximum depth reached", "The diving speed", "The water temperature"]),
            ("A loan balance in rupees is y = -2000x + 24000 after x monthly payments. What is the physical meaning of the x-intercept?", "The number of months (12 months) to completely pay off the loan", ["The monthly installment amount", "The interest rate", "The initial loan amount"]),
            ("Distance to destination is y = -60x + 300 km after driving x hours. What does the x-intercept x = 5 represent?", "The total travel time (5 hours) to reach the destination", ["The car's fuel efficiency", "The highway toll amount", "The average car speed"]),
            ("A candle's height in cm after x hours is y = -1.5x + 18. What does the zero of this linear function represent?", "The total burn time (12 hours) until the candle is fully melted", ["The original candle height", "The rate of burning", "The candle diameter"]),
            ("A store sells winter coats with profit y = 40x - 1200. What does the zero of the profit function mean?", "Selling 30 coats breaks even with zero net profit", ["Selling 40 coats gives maximum profit", "Selling 0 coats incurs no cost", "1200 coats are in stock"]),
            ("A descending hot air balloon has altitude y = -20x + 400 meters. What does the x-intercept represent?", "The time (20 minutes) when the balloon touches the ground", ["The maximum altitude of the balloon", "The speed of the wind", "The mass of the basket"])
        ],
        'tmpls': [
            "{0}",
            "Analyze the practical significance of the x-intercept: {0}",
            "What is the real-world interpretation of the zero: {0}",
            "Applied coordinate problem: {0}",
            "In practical linear modeling, interpret the x-intercept: {0}",
            "Solve the contextual problem regarding the zero: {0}",
            "What is the physical meaning of the root: {0}",
            "Interpret the x-intercept in this real scenario: {0}",
            "Explain the practical meaning of the x-intercept: {0}",
            "What does the x-intercept signify in the following context: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify what the variable \\( x \\) and function \\( y \\) represent.**\nFrom the scenario: '{item[0]}'.\n\n**Step 2: Understand the physical meaning of \\( y = 0 \\).**\nSetting \\( y = 0 \\) corresponds to the state where the measured dependent quantity reaches zero (empty, ground level, zero profit, fully discharged).\n\n**Step 3: State the practical interpretation.**\nThe x-intercept represents {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])

if __name__ == "__main__":
    q1 = gen_2_3_1()
    q2 = gen_2_3_2()
    print(f"gen_2_3_1: {len(q1)} questions generated")
    print(f"gen_2_3_2: {len(q2)} questions generated")
