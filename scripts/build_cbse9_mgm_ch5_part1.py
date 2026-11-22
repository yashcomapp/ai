# scripts/build_cbse9_mgm_ch5_part1.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 5: Periodic Patterns, Rotational & Line Symmetry and Circle Geometry
Part 1:
- Subtopic 5.1.1: Rotational symmetry and order of rotation
- Subtopic 5.1.2: Symmetry axes and cyclic geometric transformations
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 5
CH_NAME = "Periodic Patterns, Rotational & Line Symmetry"

# ==============================================================================
# SUBTOPIC 5.1.1: Rotational symmetry and order of rotation
# ==============================================================================
def gen_5_1_1():
    tc = "CBSE-9-MGM-5-5.1.1"
    tname = "Rotational symmetry and order of rotation"

    # Arch 0: Order of rotational symmetry of regular polygons
    arch0 = {
        'data': [
            ("an equilateral triangle", 3, "120°", "360° / 3 = 120°"),
            ("a square", 4, "90°", "360° / 4 = 90°"),
            ("a regular pentagon", 5, "72°", "360° / 5 = 72°"),
            ("a regular hexagon", 6, "60°", "360° / 6 = 60°"),
            ("a regular octagon", 8, "45°", "360° / 8 = 45°"),
            ("a regular nonagon", 9, "40°", "360° / 9 = 40°"),
            ("a regular decagon", 10, "36°", "360° / 10 = 36°"),
            ("a regular dodecagon (12-gon)", 12, "30°", "360° / 12 = 30°"),
            ("a regular 15-gon", 15, "24°", "360° / 15 = 24°"),
            ("a regular 20-gon", 20, "18°", "360° / 20 = 18°")
        ],
        'tmpls': [
            "What is the order of rotational symmetry of {0}?",
            "Determine the order of rotational symmetry for {0}:",
            "How many times does {0} coincide with itself during a complete 360° rotation about its centre?",
            "Find the order of rotational symmetry of {0}:",
            "The order of rotational symmetry of {0} is:",
            "For {0}, what is the order of rotational symmetry about its centre?",
            "Which number represents the order of rotational symmetry of {0}?",
            "Calculate the order of rotation for {0}:",
            "In geometric symmetry, the order of rotation of {0} is:",
            "Identify the order of rotational symmetry of {0}:"
        ],
        'calc': lambda item: (
            str(item[1]),
            [
                str(item[1] + 1),
                str(item[1] - 1) if item[1] > 2 else "1",
                str(item[1] * 2)
            ],
            f"**Step 1: Identify the shape and its regularity.**\n{item[0].capitalize()} has {item[1]} equal sides and {item[1]} equal angles.\n\n**Step 2: Recall the rotational symmetry rule for regular polygons.**\nA regular \\( n \\)-gon has rotational symmetry of order \\( n \\).\n\n**Step 3: State the order of rotational symmetry.**\nThe order is {item[1]} (with angle of rotation {item[2]})."
        ),
        'diff': 'easy'
    }

    # Arch 1: Angle of rotational symmetry
    arch1 = {
        'data': [
            ("an equilateral triangle", "120°", 3, "360° / 3 = 120°"),
            ("a square", "90°", 4, "360° / 4 = 90°"),
            ("a regular pentagon", "72°", 5, "360° / 5 = 72°"),
            ("a regular hexagon", "60°", 6, "360° / 6 = 60°"),
            ("a regular octagon", "45°", 8, "360° / 8 = 45°"),
            ("a regular nonagon", "40°", 9, "360° / 9 = 40°"),
            ("a regular decagon", "36°", 10, "360° / 10 = 36°"),
            ("a rectangle", "180°", 2, "360° / 2 = 180°"),
            ("a rhombus", "180°", 2, "360° / 2 = 180°"),
            ("a parallelogram", "180°", 2, "360° / 2 = 180°")
        ],
        'tmpls': [
            "What is the minimum angle of rotational symmetry for {0}?",
            "Determine the smallest angle through which {0} must be rotated to coincide with its original position:",
            "Find the angle of rotation for {0}:",
            "The minimum angle of rotational symmetry for {0} is:",
            "Calculate the angle of rotation of {0}:",
            "At what smallest angle does {0} map onto itself under rotation about its centre?",
            "Which angle represents the angle of rotational symmetry of {0}?",
            "Compute the smallest angle of rotation for {0}:",
            "The angle of rotational symmetry for {0} is given by:",
            "Determine the angle of rotation for {0}:"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"{int(item[1].replace('°', '')) // 2}°" if int(item[1].replace('°', '')) >= 60 else "45°",
                f"{int(item[1].replace('°', '')) + 30}°",
                "360°"
            ],
            f"**Step 1: Determine the order of rotational symmetry \\( n \\).**\nFor {item[0]}, the order of rotational symmetry is \\( n = {item[2]} \\).\n\n**Step 2: Apply the formula for angle of rotation.**\n\\[ \\text{{Angle of rotation}} = \\frac{{360^\\circ}}{{n}} = \\frac{{360^\\circ}}{{{item[2]}}} \\]\n\n**Step 3: Calculate the angle.**\n{item[3]}.\nThe minimum angle is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Special quadrilaterals: order and angle of rotation
    arch2 = {
        'data': [
            ("a rectangle (non-square)", 2, "180°", ["4", "1", "infinite"]),
            ("a rhombus (non-square)", 2, "180°", ["4", "1", "infinite"]),
            ("a general parallelogram", 2, "180°", ["4", "1", "0"]),
            ("a kite (non-rhombus)", 1, "360° (no rotational symmetry > 1)", ["2", "4", "0"]),
            ("an isosceles trapezium", 1, "360° (no rotational symmetry > 1)", ["2", "4", "0"]),
            ("a scalene triangle", 1, "360° (only trivial full turn)", ["2", "3", "0"]),
            ("an isosceles triangle (non-equilateral)", 1, "360° (order 1 only)", ["2", "3", "0"]),
            ("a circle", "infinite", "any angle", ["360", "4", "2"]),
            ("a semicircle", 1, "360° (only identity rotation)", ["2", "infinite", "180°"]),
            ("an ellipse", 2, "180°", ["4", "infinite", "1"])
        ],
        'tmpls': [
            "What is the order of rotational symmetry of {0}?",
            "Does {0} possess rotational symmetry of order greater than 1, and if so, what is its order?",
            "Find the order of rotational symmetry for {0}:",
            "The order of rotational symmetry of {0} is:",
            "Determine the order of rotation for {0}:",
            "How many self-coincidences occur for {0} during a full 360° rotation?",
            "Identify the order of rotational symmetry of {0}:",
            "Which option gives the correct order of rotational symmetry for {0}?",
            "Calculate the order of rotational symmetry of {0}:",
            "State the order of rotation for {0}:"
        ],
        'calc': lambda item: (
            str(item[1]),
            item[3],
            f"**Step 1: Analyze the geometry of {item[0]}.**\nConsider rotating the figure about its intersection of diagonals / center.\n\n**Step 2: Count coincidences in \\( [0^\\circ, 360^\\circ] \\).**\nCoincidences occur at multiples of {item[2]}.\n\n**Step 3: State the order of rotational symmetry.**\nThe order is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: English capital letters and digits rotational symmetry
    arch3 = {
        'data': [
            ("the letter 'H'", 2, "180°", ["1", "4", "0"]),
            ("the letter 'I'", 2, "180°", ["1", "4", "0"]),
            ("the letter 'O'", "infinite (as circle) or 2 (as oval)", "180°", ["1", "4", "3"]),
            ("the letter 'X'", 2, "180° (or 4 if perpendicular bars)", ["1", "3", "0"]),
            ("the letter 'Z'", 2, "180°", ["1", "4", "0"]),
            ("the letter 'S'", 2, "180°", ["1", "4", "0"]),
            ("the letter 'N'", 2, "180°", ["1", "4", "0"]),
            ("the digit '0'", 2, "180°", ["1", "4", "0"]),
            ("the digit '8'", 2, "180°", ["1", "4", "0"]),
            ("the letter 'A'", 1, "360° (no rotational symmetry > 1)", ["2", "4", "0"])
        ],
        'tmpls': [
            "What is the order of rotational symmetry of {0}?",
            "Does {0} possess rotational symmetry? What is its order?",
            "Find the order of rotational symmetry of {0}:",
            "The order of rotational symmetry for {0} about its centre is:",
            "Determine the order of rotation of {0}:",
            "How many times does {0} look identical under a full 360° turn?",
            "Identify the order of rotational symmetry for {0}:",
            "Which option represents the rotational symmetry order of {0}?",
            "Evaluate the rotational symmetry of {0}:",
            "Calculate the order of rotation of {0}:"
        ],
        'calc': lambda item: (
            str(item[1]),
            item[3],
            f"**Step 1: Inspect the glyph of {item[0]}.**\nObserve whether turning it upside down (180° rotation) results in the exact same letter.\n\n**Step 2: Count the positions of coincidence.**\nIt maps onto itself after a half turn (180°) and a full turn (360°).\n\n**Step 3: State the order.**\nThe order of rotational symmetry is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 4: Comparing line symmetry and rotational symmetry
    arch4 = {
        'data': [
            ("A figure has rotational symmetry of order 2 but NO lines of symmetry. Which figure is this?", "a parallelogram (non-rhombus, non-rectangle)", ["a rectangle", "a rhombus", "an isosceles trapezium"]),
            ("A figure has 1 line of symmetry but NO rotational symmetry of order > 1. Which figure is this?", "an isosceles triangle or kite", ["a parallelogram", "a rectangle", "a square"]),
            ("A figure has rotational symmetry of order 4 and 4 lines of symmetry. This figure is:", "a square", ["a rectangle", "a rhombus", "a regular pentagon"]),
            ("A figure has rotational symmetry of order 2 and 2 lines of symmetry. Which figure could this be?", "a rectangle or rhombus", ["a square", "a parallelogram", "a kite"]),
            ("Can a figure have an angle of rotational symmetry of 45°? What would its order be?", "Yes, order 8 (since 360° / 45° = 8)", ["No, impossible", "Yes, order 4", "Yes, order 6"]),
            ("Can a figure have an angle of rotational symmetry of 17°?", "No, because 360 is not divisible by 17 (360 / 17 ≈ 21.18)", ["Yes, order 21", "Yes, order 17", "Yes, always"]),
            ("What is the condition on the angle of rotational symmetry θ for any closed figure?", "360° must be an exact integer multiple of θ (360° / θ = n is an integer)", ["θ must be less than 90°", "θ must be an even integer", "θ must be a prime number"]),
            ("A ceiling fan with 3 identical blades has rotational symmetry of order:", "3", ["1", "6", "2"]),
            ("A windmill with 4 identical perpendicular sails has rotational symmetry of order:", "4", ["2", "8", "1"]),
            ("A starfish with 5 identical arms has rotational symmetry of order:", "5", ["10", "1", "2"])
        ],
        'tmpls': [
            "{0}",
            "Question on rotational vs line symmetry: {0}",
            "Analyze the symmetry properties: {0}",
            "Identify the correct geometric figure or condition: {0}",
            "Determine the true statement: {0}",
            "Which option correctly answers: {0}",
            "Select the accurate mathematical fact: {0}",
            "What is the mathematical conclusion: {0}",
            "Evaluate the symmetry scenario: {0}",
            "Choose the correct option: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand the definitions of line and rotational symmetry.**\nLine symmetry requires reflectional invariance; rotational symmetry requires rotational invariance.\n\n**Step 2: Evaluate the criteria.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Calculations of angle of rotation given order and vice versa
    arch5 = {
        'data': [
            (2, "180°", 180),
            (3, "120°", 120),
            (4, "90°", 90),
            (5, "72°", 72),
            (6, "60°", 60),
            (8, "45°", 45),
            (9, "40°", 9),
            (10, "36°", 36),
            (12, "30°", 30),
            (18, "20°", 20)
        ],
        'tmpls': [
            "If a figure has rotational symmetry of order {0}, what is its angle of rotation?",
            "A geometric pattern has order of rotational symmetry {0}. Its smallest angle of rotation is:",
            "Calculate the angle of rotation for a figure with rotational symmetry of order {0}:",
            "What is the angle of rotation if the order of rotational symmetry is {0}?",
            "Determine the angle of rotation for order {0}:",
            "Find the angle \\( \\theta \\) such that rotation by \\( \\theta \\) maps a figure of order {0} onto itself:",
            "The angle of rotational symmetry for a design having order {0} is:",
            "Compute the angle of rotation for order {0}:",
            "Evaluate the angle of rotation corresponding to order {0}:",
            "Which angle corresponds to an order of rotational symmetry of {0}?"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"{int(item[1].replace('°', '')) // 2}°",
                f"{int(item[1].replace('°', '')) + 15}°",
                f"{360 // (item[0] + 1)}°"
            ],
            f"**Step 1: Recall the relation between order \\( n \\) and angle of rotation \\( \\theta \\).**\n\\[ \\theta = \\frac{{360^\\circ}}{{n}} \\]\n\n**Step 2: Substitute \\( n = {item[0]} \\).**\n\\[ \\theta = \\frac{{360^\\circ}}{{{item[0]}}} = {item[1]} \\]\n\n**Step 3: State the angle of rotation.**\nThe angle is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 6: Identifying whether an angle can be an angle of rotational symmetry
    arch6 = {
        'data': [
            ("45°", "Yes, because 360° / 45° = 8 (order 8)", ["No, 45 is not an even divisor", "Only for triangles", "No"]),
            ("17°", "No, because 360° is not divisible by 17°", ["Yes, order 21", "Yes, order 17", "Yes, always"]),
            ("24°", "Yes, because 360° / 24° = 15 (order 15)", ["No, 24 is too small", "Only for circles", "No"]),
            ("15°", "Yes, because 360° / 15° = 24 (order 24)", ["No, not an integer order", "Only for triangles", "No"]),
            ("25°", "No, because 360° / 25° = 14.4 (not an integer)", ["Yes, order 14", "Yes, order 25", "Yes, always"]),
            ("18°", "Yes, because 360° / 18° = 20 (order 20)", ["No", "Only for polygons with odd sides", "No"]),
            ("72°", "Yes, because 360° / 72° = 5 (order 5)", ["No", "Only for hexagons", "No"]),
            ("50°", "No, because 360° / 50° = 7.2 (not an integer)", ["Yes, order 7", "Yes, order 5", "Yes"]),
            ("36°", "Yes, because 360° / 36° = 10 (order 10)", ["No", "Only for decagons", "No"]),
            ("22°", "No, because 360° / 22° = 16.36 (not an integer)", ["Yes, order 16", "Yes, order 22", "Yes"])
        ],
        'tmpls': [
            "Can \\( {0} \\) be the angle of rotational symmetry of a figure?",
            "Is it possible for a figure to have \\( {0} \\) as its smallest angle of rotational symmetry?",
            "Determine whether \\( {0} \\) can be an angle of rotational symmetry:",
            "Check if \\( {0} \\) can be the angle of rotation for any closed figure:",
            "Which statement correctly evaluates whether \\( {0} \\) can be an angle of rotational symmetry?",
            "Can a polygon have angle of rotational symmetry equal to \\( {0} \\)?",
            "What is the verdict for \\( {0} \\) being an angle of rotational symmetry?",
            "Evaluate if \\( {0} \\) is a valid angle of rotational symmetry:",
            "Is \\( {0} \\) permissible as an angle of rotational symmetry?",
            "Assess whether \\( {0} \\) can serve as an angle of rotation:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Check if 360° is divisible by the given angle.**\nDivide 360° by {item[0]}.\n\n**Step 2: Determine if the result is an integer.**\nIf \\( \\frac{{360^\\circ}}{{\\theta}} \\) is a whole number, then \\( \\theta \\) is a valid angle of rotational symmetry.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Real-world periodic patterns, rangoli, mandalas, and friezes
    arch7 = {
        'data': [
            ("A circular rangoli pattern with 6 identical petals arranged radially has rotational symmetry of order:", "6", ["3", "12", "1"]),
            ("A Buddhist Dharmachakra (wheel of law) with 8 spokes has rotational symmetry of order:", "8", ["4", "16", "2"]),
            ("The Ashoka Chakra on the Indian National Flag has 24 spokes. What is its order of rotational symmetry?", "24", ["12", "48", "6"]),
            ("What is the angle of rotation between consecutive spokes of the Ashoka Chakra?", "360° / 24 = 15°", ["12°", "20°", "10°"]),
            ("A periodic wallpaper pattern repeats infinitely in two independent directions. It combines rotational symmetry with:", "translational symmetry", ["only line reflection", "scale dilation", "spherical curvature"]),
            ("A border pattern (frieze pattern) that repeats along a single line possesses:", "translational symmetry along a line", ["rotational symmetry of infinite order", "no symmetry", "3D helical symmetry"]),
            ("A snowflake crystal with 6-fold hexagonal dendrites has rotational symmetry of order:", "6", ["3", "12", "8"]),
            ("A steering wheel with 3 equally spaced spokes has rotational symmetry of order:", "3", ["1", "6", "2"]),
            ("A playing card (such as King or Queen of Hearts) designed to look the same upside down has rotational symmetry of order:", "2", ["1", "4", "0"]),
            ("A standard chess board has 8x8 alternating black and white squares. What is its order of rotational symmetry about its centre?", "2 (rotating by 90° swaps black and white squares, but 180° restores the colors)", ["4", "1", "8"])
        ],
        'tmpls': [
            "{0}",
            "Solve the real-world rotational symmetry question: {0}",
            "Application of symmetry in design and art: {0}",
            "Determine the order or angle of symmetry: {0}",
            "What is the mathematical answer to: {0}",
            "Find the rotational symmetry property: {0}",
            "Which option correctly answers: {0}",
            "Calculate: {0}",
            "Evaluate the pattern: {0}",
            "Identify the symmetry order: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify the periodic element and number of repetitions in a full circle.**\nObserve the radial symmetry about the central axis.\n\n**Step 2: Count the matching rotational positions in 360°.**\n'{item[0]}'.\n\n**Step 3: State the result.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 5.1.2: Symmetry axes and cyclic geometric transformations
# ==============================================================================
def gen_5_1_2():
    tc = "CBSE-9-MGM-5-5.1.2"
    tname = "Symmetry axes and cyclic geometric transformations"

    # Arch 0: Number of lines of symmetry of standard 2D plane figures
    arch0 = {
        'data': [
            ("an equilateral triangle", 3, "the 3 angle bisectors / medians", ["1", "0", "6"]),
            ("an isosceles triangle", 1, "the altitude to the base", ["2", "3", "0"]),
            ("a scalene triangle", 0, "no lines of symmetry", ["1", "2", "3"]),
            ("a square", 4, "2 axes connecting midpoints of opposite sides and 2 diagonals", ["2", "8", "1"]),
            ("a rectangle (non-square)", 2, "the 2 perpendicular bisectors of opposite sides (NOT diagonals)", ["4", "1", "0"]),
            ("a rhombus (non-square)", 2, "the 2 diagonals", ["4", "1", "0"]),
            ("a general parallelogram", 0, "parallelograms have no line of symmetry", ["1", "2", "4"]),
            ("a kite", 1, "the main diagonal bisecting the non-equal angles", ["2", "4", "0"]),
            ("an isosceles trapezium", 1, "the perpendicular bisector of the parallel bases", ["2", "4", "0"]),
            ("a regular hexagon", 6, "3 connecting opposite vertices and 3 connecting opposite side midpoints", ["3", "12", "4"])
        ],
        'tmpls': [
            "How many lines of symmetry does {0} have?",
            "What is the number of lines of symmetry for {0}?",
            "Determine the number of axes of symmetry of {0}:",
            "Find the number of lines of symmetry in {0}:",
            "The number of lines of symmetry possessed by {0} is:",
            "How many axes of reflectional symmetry exist for {0}?",
            "Which number represents the count of lines of symmetry in {0}?",
            "Calculate the number of lines of symmetry for {0}:",
            "Identify the number of lines of symmetry of {0}:",
            "State the number of axes of symmetry of {0}:"
        ],
        'calc': lambda item: (
            str(item[1]),
            item[3],
            f"**Step 1: Understand the definition of a line of symmetry.**\nA line of symmetry divides a figure into two congruent halves that coincide under reflection.\n\n**Step 2: Inspect lines of reflection for {item[0]}.**\n{item[2].capitalize()}.\n\n**Step 3: State the number of lines of symmetry.**\nThe figure has {item[1]} lines of symmetry."
        ),
        'diff': 'easy'
    }

    # Arch 1: Why diagonals of a rectangle are NOT lines of symmetry
    arch1 = {
        'data': [
            ("Why is a diagonal of a non-square rectangle NOT a line of symmetry?", "Because reflecting across a diagonal does not map the adjacent sides onto each other (vertices do not coincide)", ["Because diagonals are not equal", "Because diagonals do not bisect each other", "It IS a line of symmetry"]),
            ("Are the diagonals of a rhombus lines of symmetry?", "Yes, both diagonals are lines of symmetry because they bisect the vertex angles and opposite vertices coincide", ["No, only one is", "No, none are", "Only if it is a square"]),
            ("Are the diagonals of a square lines of symmetry?", "Yes, a square has 4 lines of symmetry: 2 diagonals and 2 side bisectors", ["No, only side bisectors are", "No, only diagonals are", "Only 2 lines exist"]),
            ("Does a circle have a finite number of lines of symmetry?", "No, a circle has infinitely many lines of symmetry (any line passing through its centre)", ["Yes, exactly 360", "Yes, exactly 4", "Yes, exactly 2"]),
            ("What is a line of symmetry of a circle?", "any diameter (straight line passing through the centre)", ["any chord", "any tangent", "any secant"]),
            ("How many lines of symmetry does a regular n-sided polygon have?", "n lines of symmetry", ["2n", "n / 2", "n - 1"]),
            ("For an odd regular polygon (like regular pentagon), where do the lines of symmetry pass?", "from each vertex perpendicular to the midpoint of the opposite side", ["connecting opposite vertices", "connecting midpoints of sides", "along diagonals"]),
            ("For an even regular polygon (like regular hexagon or octagon), how are the lines of symmetry divided?", "half connect opposite vertices, half connect midpoints of opposite sides", ["all connect vertices", "all connect midpoints", "along all diagonals"]),
            ("A line segment AB has how many lines of symmetry?", "2 lines: the line itself and its perpendicular bisector", ["1", "infinite", "0"]),
            ("An angle with unequal arms has how many lines of symmetry?", "0 (if arms are equal, its bisector is the 1 line of symmetry)", ["1", "2", "infinite"])
        ],
        'tmpls': [
            "{0}",
            "Conceptual question on axes of symmetry: {0}",
            "Reflectional symmetry reasoning: {0}",
            "Determine the accurate geometric explanation: {0}",
            "Which option correctly answers: {0}",
            "Select the valid geometric fact: {0}",
            "What is the mathematical reason: {0}",
            "Evaluate the statement: {0}",
            "Identify the correct property: {0}",
            "Analyze: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Test reflectional invariance.**\nA line \\( L \\) is an axis of symmetry if reflecting every point \\( P \\) across \\( L \\) yields a point on the same figure.\n\n**Step 2: Evaluate the property.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 2: Coordinate reflections across axes and origin
    arch2 = {
        'data': [
            ("P(3, 4)", "the X-axis", "(3, -4)", ["(-3, 4)", "(-3, -4)", "(4, 3)"]),
            ("P(3, 4)", "the Y-axis", "(-3, 4)", ["(3, -4)", "(-3, -4)", "(4, 3)"]),
            ("P(3, 4)", "the origin (0, 0)", "(-3, -4)", ["(3, -4)", "(-3, 4)", "(4, 3)"]),
            ("P(-5, 2)", "the X-axis", "(-5, -2)", ["(5, 2)", "(5, -2)", "(-2, 5)"]),
            ("P(-5, 2)", "the Y-axis", "(5, 2)", ["(-5, -2)", "(5, -2)", "(2, -5)"]),
            ("P(-5, 2)", "the origin (0, 0)", "(5, -2)", ["(-5, -2)", "(5, 2)", "(2, 5)"]),
            ("P(4, -7)", "the X-axis", "(4, 7)", ["(-4, -7)", "(-4, 7)", "(7, -4)"]),
            ("P(4, -7)", "the Y-axis", "(-4, -7)", ["(4, 7)", "(-4, 7)", "(-7, 4)"]),
            ("P(-6, -8)", "the X-axis", "(-6, 8)", ["(6, -8)", "(6, 8)", "(-8, -6)"]),
            ("P(-6, -8)", "the origin (0, 0)", "(6, 8)", ["(-6, 8)", "(6, -8)", "(8, 6)"])
        ],
        'tmpls': [
            "What are the coordinates of the image of point \\( {0} \\) after reflection in {1}?",
            "Find the reflection of \\( {0} \\) in {1}:",
            "Reflecting the point \\( {0} \\) across {1} gives the point:",
            "The image of \\( {0} \\) under reflection through {1} is:",
            "Determine the coordinates of \\( {0} \\) reflected in {1}:",
            "Calculate the image coordinates of \\( {0} \\) when reflected across {1}:",
            "Which point represents the reflection of \\( {0} \\) in {1}?",
            "Find the coordinates after reflection: \\( {0} \\) in {1}:",
            "Evaluate the reflection transformation of \\( {0} \\) in {1}:",
            "Compute the reflected point for \\( {0} \\) across {1}:"
        ],
        'calc': lambda item: (
            item[2],
            item[3],
            f"**Step 1: Recall the reflection transformation rules in coordinate geometry.**\nReflection in X-axis maps \\( (x, y) \\to (x, -y) \\).\nReflection in Y-axis maps \\( (x, y) \\to (-x, y) \\).\nReflection in origin maps \\( (x, y) \\to (-x, -y) \\).\n\n**Step 2: Apply the rule to point {item[0]} across {item[1]}.**\n\n**Step 3: State the image coordinates.**\nThe reflected point is {item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 3: Rotations in the coordinate plane (90°, 180°, 270° about origin)
    arch3 = {
        'data': [
            ("P(2, 3)", "90° counter-clockwise (anticlockwise)", "(-3, 2)", ["(3, -2)", "(-2, -3)", "(3, 2)"]),
            ("P(2, 3)", "180° about the origin", "(-2, -3)", ["(2, -3)", "(-2, 3)", "(3, 2)"]),
            ("P(2, 3)", "90° clockwise (270° counter-clockwise)", "(3, -2)", ["(-3, 2)", "(-2, -3)", "(-3, -2)"]),
            ("P(-4, 1)", "90° counter-clockwise", "(-1, -4)", ["(1, 4)", "(1, -4)", "(4, 1)"]),
            ("P(-4, 1)", "180° about the origin", "(4, -1)", ["(-4, -1)", "(4, 1)", "(1, -4)"]),
            ("P(5, -2)", "90° counter-clockwise", "(2, 5)", ["(-2, -5)", "(2, -5)", "(-5, 2)"]),
            ("P(5, -2)", "180° about the origin", "(-5, 2)", ["(5, 2)", "(-5, -2)", "(2, 5)"]),
            ("P(-3, -5)", "90° counter-clockwise", "(5, -3)", ["(-5, 3)", "(-5, -3)", "(3, 5)"]),
            ("P(-3, -5)", "180° about the origin", "(3, 5)", ["(-3, 5)", "(3, -5)", "(5, 3)"]),
            ("P(1, 4)", "270° counter-clockwise", "(4, -1)", ["(-4, 1)", "(-1, -4)", "(4, 1)"])
        ],
        'tmpls': [
            "What are the coordinates of point \\( {0} \\) after a rotation of {1} about the origin?",
            "Find the image of \\( {0} \\) under a rotation of {1} about \\( (0,0) \\):",
            "Rotating \\( {0} \\) by {1} about the origin produces the point:",
            "The coordinates of \\( {0} \\) rotated through {1} about the origin are:",
            "Determine the image of \\( {0} \\) after rotation by {1}:",
            "Calculate the rotated coordinates of \\( {0} \\) for {1}:",
            "Which point is obtained by rotating \\( {0} \\) by {1}?",
            "Apply the rotation transformation of {1} to \\( {0} \\):",
            "Evaluate the image point: \\( {0} \\) rotated by {1}:",
            "Compute the coordinates of \\( {0} \\) after rotating {1}:"
        ],
        'calc': lambda item: (
            item[2],
            item[3],
            f"**Step 1: Recall the standard coordinate rotation formulas about origin \\( (0, 0) \\).**\nRotation by 90° counter-clockwise: \\( (x, y) \\to (-y, x) \\).\nRotation by 180°: \\( (x, y) \\to (-x, -y) \\).\nRotation by 270° counter-clockwise (90° clockwise): \\( (x, y) \\to (y, -x) \\).\n\n**Step 2: Apply the transformation to {item[0]}.**\n\n**Step 3: State the image point.**\nThe image is {item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Cyclic transformations and composition of reflections
    arch4 = {
        'data': [
            ("What single transformation is equivalent to reflecting a figure across two intersecting lines at an angle θ?", "a rotation of angle 2θ about their point of intersection", ["a translation of distance 2θ", "a reflection across their angle bisector", "a dilation"]),
            ("If two reflection axes are perpendicular (θ = 90°), their composite reflection is equivalent to:", "a half-turn (rotation of 2 * 90° = 180°) about the intersection point", ["a full 360° rotation", "a translation", "no transformation"]),
            ("What single transformation is equivalent to reflecting across two parallel lines separated by distance d?", "a translation of distance 2d perpendicular to the lines", ["a rotation of 180°", "a reflection across the midline", "no change"]),
            ("Does the order of two reflections across intersecting lines matter?", "Yes, reflecting across L_1 then L_2 rotates by 2θ clockwise, while L_2 then L_1 rotates counter-clockwise", ["No, reflection is always commutative", "Only if lines are perpendicular", "Never"]),
            ("What is a glide reflection?", "a combination of a reflection across a line and a translation parallel to that line", ["a rotation followed by scaling", "two reflections across intersecting lines", "a circular translation"]),
            ("Which transformation preserves both orientation and distance (isometry)?", "translations and rotations", ["reflections and glide reflections", "dilations", "shears"]),
            ("Reflecting across a line reverses the orientation of a figure. What happens if you reflect twice?", "orientation is restored (proper isometry / direct congruence)", ["orientation remains reversed", "size doubles", "figure disappears"]),
            ("A cyclic group of order n (C_n) in plane geometry consists of:", "n pure rotations by multiples of 360°/n about a single fixed point", ["n reflections", "n translations", "combinations of dilations"]),
            ("A dihedral group of order 2n (D_n) in plane geometry represents the symmetry group of:", "a regular n-gon (n rotations and n reflections)", ["a circle", "a line", "a sphere"]),
            ("How many total symmetries (rotations + reflections) does an equilateral triangle have?", "6 symmetries (3 rotations and 3 reflections, group D_3)", ["3", "4", "12"])
        ],
        'tmpls': [
            "{0}",
            "Question on cyclic transformations and symmetry groups: {0}",
            "Advanced transformation geometry: {0}",
            "Determine the correct theorem on composite transformations: {0}",
            "Which option represents: {0}",
            "What is the mathematical conclusion: {0}",
            "Identify the valid geometric property: {0}",
            "Select the accurate statement: {0}",
            "Evaluate the composite transformation: {0}",
            "Choose the correct option: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the fundamental theorems of plane isometries.**\nComposition of two reflections across intersecting lines at angle \\( \\theta \\) equals a rotation of \\( 2\\theta \\).\n\n**Step 2: Evaluate the statement.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Lines of symmetry of geometric shapes drawn inside circles
    arch5 = {
        'data': [
            ("A regular hexagon is inscribed in a circle. How many lines of symmetry does the composite figure have?", "6", ["3", "12", "infinite"]),
            ("A non-square rectangle is inscribed in a circle. How many lines of symmetry does the composite figure have?", "2", ["4", "infinite", "0"]),
            ("An equilateral triangle is inscribed in a circle. How many lines of symmetry does the combined figure have?", "3", ["1", "6", "infinite"]),
            ("A square is inscribed in a circle. How many axes of symmetry does the combined figure possess?", "4", ["2", "8", "infinite"]),
            ("A chord is drawn in a circle. How many lines of symmetry does the circle with this single chord have?", "1 (the perpendicular bisector of the chord)", ["2", "infinite", "0"]),
            ("Two equal parallel chords are drawn in a circle. How many lines of symmetry does this figure have?", "2 (the perpendicular bisector of the chords and the line parallel to them halfway between)", ["1", "4", "infinite"]),
            ("Two perpendicular diameters are drawn in a circle. How many lines of symmetry does the resulting figure have?", "4 (the two diameters and the two angle bisectors between them)", ["2", "8", "infinite"]),
            ("A semicircle with its diameter has how many lines of symmetry?", "1 (the perpendicular bisector of the diameter)", ["2", "infinite", "0"]),
            ("A circle with two intersecting chords of equal length meeting at the circumference has how many lines of symmetry?", "1 (the angle bisector between the chords)", ["2", "0", "infinite"]),
            ("A sector of a circle subtending an angle θ < 360° at the centre has how many lines of symmetry?", "1 (the angle bisector of the central angle)", ["2", "0", "infinite"])
        ],
        'tmpls': [
            "{0}",
            "Determine the symmetry of the circle configuration: {0}",
            "Count the axes of symmetry: {0}",
            "How many lines of symmetry exist? {0}",
            "Calculate: {0}",
            "What is the number of lines of symmetry: {0}",
            "Which option gives the correct count: {0}",
            "Analyze the composite circular symmetry: {0}",
            "Find the lines of symmetry: {0}",
            "Evaluate: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify the symmetry operations common to both constituent figures.**\nThe composite figure possesses only those symmetries shared by both the circle and the inscribed feature.\n\n**Step 2: Inspect lines of reflection.**\n'{item[0]}'.\n\n**Step 3: State the number of symmetry lines.**\nThe count is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Invariant points and lines under symmetry transformations
    arch6 = {
        'data': [
            ("Under reflection in line L, which points remain invariant (unmoved)?", "all points lying on the line L itself", ["no points", "only the midpoint", "points at infinity"]),
            ("Under rotation about a point O by angle θ ≠ 0° (and < 360°), which point remains invariant?", "only the centre of rotation O", ["all points on the circle", "points on the axes", "no points"]),
            ("Under a translation by a non-zero vector, how many points remain invariant?", "0 (no point remains invariant under a non-zero translation)", ["1", "infinite", "all points on the vector"]),
            ("If a point P(x, y) satisfies P = P' under reflection across the Y-axis, what must be true about P?", "x = 0 (P lies on the Y-axis)", ["y = 0", "x = y", "x = -y"]),
            ("If a point P(x, y) is invariant under reflection across the X-axis, what is true?", "y = 0 (P lies on the X-axis)", ["x = 0", "x = y", "x + y = 0"]),
            ("If a point P(x, y) is invariant under reflection in the line y = x, what is true?", "x = y (P lies on the line y = x)", ["x = -y", "x = 0", "y = 0"]),
            ("What is the reflection of point P(a, b) across the line y = x?", "(b, a)", ["(-b, -a)", "(-a, -b)", "(a, -b)"]),
            ("What is the reflection of point P(a, b) across the line y = -x?", "(-b, -a)", ["(b, a)", "(-a, -b)", "(a, -b)"]),
            ("The line y = x is a line of symmetry for which function graph?", "y = 1/x (hyperbola)", ["y = x^2", "y = x^3", "y = |x|"]),
            ("The Y-axis (x = 0) is a line of symmetry for which function graph?", "y = x^2 (parabola)", ["y = x^3", "y = x", "y = 1/x"])
        ],
        'tmpls': [
            "{0}",
            "Question on invariant points and lines: {0}",
            "Coordinate geometry symmetry analysis: {0}",
            "Determine the invariant property: {0}",
            "Which option correctly answers: {0}",
            "What is the mathematical condition: {0}",
            "Select the accurate property: {0}",
            "Identify the invariant: {0}",
            "Evaluate the transformation condition: {0}",
            "Choose the correct option: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand invariant elements in geometric transformations.**\nA point or line is invariant if the transformation maps it onto itself.\n\n**Step 2: Apply the transformation rules.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Tessellations and tiling with regular polygons
    arch7 = {
        'data': [
            ("Which regular polygons can tile the plane by themselves (regular tessellations)?", "equilateral triangles, squares, and regular hexagons", ["only squares", "squares and pentagons", "any regular polygon"]),
            ("Why can regular pentagons NOT tile the plane by themselves?", "Because the interior angle of a regular pentagon is 108°, and 360° is not divisible by 108° (3 * 108° = 324° < 360°)", ["Because pentagons have odd sides", "Because pentagons have no symmetry", "They CAN tile the plane"]),
            ("What is the interior angle of an equilateral triangle, and how many meet at each vertex in a regular triangular tiling?", "60°, and 6 triangles meet at each vertex (6 * 60° = 360°)", ["90°, 4 meet", "120°, 3 meet", "45°, 8 meet"]),
            ("In a regular hexagonal tiling (like a honeycomb), what is the interior angle and how many hexagons meet at each vertex?", "120°, and 3 hexagons meet at each vertex (3 * 120° = 360°)", ["60°, 6 meet", "108°, 3 meet", "90°, 4 meet"]),
            ("What is the fundamental condition for regular polygons of a single type to form a regular tessellation?", "The interior angle must be an exact divisor of 360°", ["The number of sides must be even", "The perimeter must be 360", "The area must be an integer"]),
            ("In an Islamic geometric tessellation or periodic tiling, the symmetry of the repeating unit is governed by:", "the 17 crystallographic plane symmetry groups (wallpaper groups)", ["fractal dimensions", "only translation", "arbitrary choice"]),
            ("A semi-regular tessellation uses:", "two or more different regular polygons such that every vertex arrangement is identical", ["irregular polygons", "overlapping shapes", "random polygons"]),
            ("Which combination of regular octagon and another regular polygon tiles the plane?", "octagons and squares (interior angles 135° + 135° + 90° = 360°)", ["octagons and triangles", "octagons and pentagons", "octagons and hexagons"]),
            ("Can regular hexagons and equilateral triangles tile the plane together?", "Yes, 2 hexagons and 2 triangles meet at vertices (120° + 120° + 60° + 60° = 360°)", ["No, never", "Only if sides are unequal", "Only with squares"]),
            ("In a brick wall pattern (running bond), the periodic pattern is generated by:", "translations horizontally and half-brick staggered translations vertically", ["rotations only", "reflections only", "dilations"])
        ],
        'tmpls': [
            "{0}",
            "Question on geometric tiling and tessellations: {0}",
            "Application of symmetry in plane tessellations: {0}",
            "Analyze the tessellation condition: {0}",
            "Which option correctly answers: {0}",
            "Determine the mathematical reason: {0}",
            "Identify the valid tiling property: {0}",
            "What is the mathematical conclusion concerning: {0}",
            "Evaluate the geometric tiling concept: {0}",
            "Choose the correct option: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the tessellation condition at a vertex.**\nThe sum of interior angles of the polygons meeting at any vertex must equal exactly \\( 360^\\circ \\) with no gaps or overlaps.\n\n**Step 2: Evaluate the polygon angles.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_5_1_1()
    q2 = gen_5_1_2()
    print(f"gen_5_1_1: {len(q1)} questions")
    print(f"gen_5_1_2: {len(q2)} questions")
