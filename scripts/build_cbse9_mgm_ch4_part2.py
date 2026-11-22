# scripts/build_cbse9_mgm_ch4_part2.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 4: Exploring Algebraic Identities
Part 2:
- Subtopic 4.1.4: Geometric area dissections proving identities
- Subtopic 4.2.1: Expansion: (x + y + z)² = x² + y² + z² + 2xy + 2yz + 2zx
- Subtopic 4.2.2: Applications in algebraic simplification
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 240 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 4
CH_NAME = "Exploring Algebraic Identities"

# ==============================================================================
# SUBTOPIC 4.1.4: Geometric area dissections proving identities
# ==============================================================================
def gen_4_1_4():
    tc = "CBSE-9-MGM-4-4.1.4"
    tname = "Geometric area dissections proving identities"

    # Arch 0: Identity (x + a)(x + b) geometric model
    arch0 = {
        'data': [
            ("(x + 2)(x + 3)", "x^2 + 5x + 6", 2, 3, 5, 6),
            ("(x + 4)(x + 5)", "x^2 + 9x + 20", 4, 5, 9, 20),
            ("(x + 1)(x + 6)", "x^2 + 7x + 6", 1, 6, 7, 6),
            ("(x + 3)(x + 7)", "x^2 + 10x + 21", 3, 7, 10, 21),
            ("(x + 2)(x + 8)", "x^2 + 10x + 16", 2, 8, 10, 16),
            ("(x + 5)(x + 6)", "x^2 + 11x + 30", 5, 6, 11, 30),
            ("(x + 4)(x + 7)", "x^2 + 11x + 28", 4, 7, 11, 28),
            ("(x + 3)(x + 8)", "x^2 + 11x + 24", 3, 8, 11, 24),
            ("(x + 2)(x + 9)", "x^2 + 11x + 18", 2, 9, 11, 18),
            ("(x + 5)(x + 8)", "x^2 + 13x + 40", 5, 8, 13, 40)
        ],
        'tmpls': [
            "A rectangle of length \\( (x + {2}) \\) and width \\( (x + {3}) \\) has area:",
            "Find the area of a rectangle with dimensions \\( {0} \\):",
            "Geometric area dissection of a rectangle with sides \\( (x + {2}) \\) and \\( (x + {3}) \\) yields:",
            "Apply \\( (x + a)(x + b) = x^2 + (a + b)x + ab \\) to \\( {0} \\):",
            "What is the total area formed by partitioning a rectangle of sides \\( (x + {2}) \\) and \\( (x + {3}) \\)?",
            "Calculate the expanded area of \\( {0} \\):",
            "A tiled floor has dimensions \\( (x + {2}) \\) by \\( (x + {3}) \\). Its area polynomial is:",
            "Determine the area expression for \\( {0} \\):",
            "The expansion of \\( {0} \\) representing rectangular area is:",
            "Evaluate the geometric model product \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"x^2 + {item[5]}",
                f"x^2 + {item[4]}x + {item[4]}",
                f"x^2 - {item[4]}x + {item[5]}"
            ],
            f"**Step 1: Partition the rectangle into 4 sub-regions.**\nOne square of side \\( x \\) (area \\( x^2 \\)), two rectangles of areas \\( {item[2]}x \\) and \\( {item[3]}x \\), and one small rectangle of area \\( {item[2]} \\times {item[3]} = {item[5]} \\).\n\n**Step 2: Sum the four individual areas.**\n\\[ \\text{{Total Area}} = x^2 + {item[2]}x + {item[3]}x + {item[5]} \\]\n\n**Step 3: Combine like terms.**\n\\( = {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Numerical applications of (x + a)(x + b) model
    arch1 = {
        'data': [
            (103, 104, 100, 3, 4, 10712),
            (105, 106, 100, 5, 6, 11130),
            (102, 107, 100, 2, 7, 10914),
            (104, 108, 100, 4, 8, 11232),
            (103, 107, 100, 3, 7, 11021),
            (101, 105, 100, 1, 5, 10605),
            (106, 108, 100, 6, 8, 11448),
            (102, 109, 100, 2, 9, 11118),
            (105, 107, 100, 5, 7, 11235),
            (104, 106, 100, 4, 6, 11024)
        ],
        'tmpls': [
            "Evaluate without direct multiplication: \\( {0} \\times {1} \\).",
            "Using \\( (x + a)(x + b) = x^2 + (a + b)x + ab \\), calculate \\( {0} \\times {1} \\):",
            "Compute \\( {0} \\times {1} \\) by setting \\( x = {2} \\):",
            "What is the exact product \\( {0} \\times {1} \\)?",
            "Calculate \\( ({2} + {3})({2} + {4}) \\):",
            "Find \\( {0} \\times {1} \\) using the geometric dissection identity:",
            "Determine the value of \\( {0} \\times {1} \\):",
            "The product \\( {0} \\times {1} \\) obtained via algebraic identity is:",
            "Solve for \\( {0} \\times {1} \\) algebraically:",
            "Evaluate \\( {0} \\times {1} \\):"
        ],
        'calc': lambda item: (
            str(item[5]),
            [
                str(item[5] + 20),
                str(item[5] - 100),
                str(item[5] + 100)
            ],
            f"**Step 1: Express both factors relative to base 100.**\n\\[ {item[0]} = {item[2]} + {item[3]}, \\quad {item[1]} = {item[2]} + {item[4]} \\]\n\n**Step 2: Apply the identity \\( (x + a)(x + b) = x^2 + (a + b)x + ab \\).**\n\\[ ({item[2]} + {item[3]})({item[2]} + {item[4]}) = {item[2]}^2 + ({item[3]} + {item[4]})({item[2]}) + ({item[3]})({item[4]}) \\]\n\\[ = 10000 + {item[3]+item[4]}(100) + {item[3]*item[4]} \\]\n\n**Step 3: Sum the terms.**\n\\( = {item[5]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Mixed signs: (x + a)(x - b) model
    arch2 = {
        'data': [
            ("(x + 4)(x - 2)", "x^2 + 2x - 8", 4, -2, 2, -8),
            ("(x + 5)(x - 3)", "x^2 + 2x - 15", 5, -3, 2, -15),
            ("(x + 6)(x - 2)", "x^2 + 4x - 12", 6, -2, 4, -12),
            ("(x + 7)(x - 3)", "x^2 + 4x - 21", 7, -3, 4, -21),
            ("(x + 8)(x - 5)", "x^2 + 3x - 40", 8, -5, 3, -40),
            ("(x - 4)(x + 2)", "x^2 - 2x - 8", -4, 2, -2, -8),
            ("(x - 6)(x + 1)", "x^2 - 5x - 6", -6, 1, -5, -6),
            ("(x - 7)(x + 3)", "x^2 - 4x - 21", -7, 3, -4, -21),
            ("(x - 5)(x + 2)", "x^2 - 3x - 10", -5, 2, -3, -10),
            ("(x - 8)(x + 4)", "x^2 - 4x - 32", -8, 4, -4, -32)
        ],
        'tmpls': [
            "Expand using algebraic identities: \\( {0} \\).",
            "What is the expansion of \\( {0} \\)?",
            "Apply \\( (x + a)(x + b) \\) to expand \\( {0} \\):",
            "The simplified polynomial for \\( {0} \\) is:",
            "Find the product: \\( {0} \\):",
            "Calculate \\( {0} \\):",
            "Evaluate \\( {0} \\):",
            "Which of the following is equal to \\( {0} \\)?",
            "Determine the result of \\( {0} \\):",
            "Compute the expansion of \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("-", "+"),
                f"x^2 + {abs(item[4])}x + {abs(item[5])}",
                f"x^2 - {abs(item[5])}"
            ],
            f"**Step 1: Identify \\( a \\) and \\( b \\) in \\( (x + a)(x + b) \\).**\n\\( a = {item[2]} \\) and \\( b = {item[3]} \\).\n\n**Step 2: Apply the identity.**\n\\[ x^2 + (a + b)x + ab = x^2 + ({item[2]} + {item[3]})x + ({item[2]})({item[3]}) \\]\n\n**Step 3: Simplify signs and terms.**\nThe expanded form is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Theoretical dissections of standard identities
    arch3 = {
        'data': [
            ("In the geometric proof of (a + b)², how many distinct non-overlapping pieces compose the total square?", "4 pieces (2 squares and 2 rectangles)", ["2 pieces", "3 pieces", "5 pieces"]),
            ("In the geometric model of (a + b)², what is the total area of the two rectangles combined?", "2ab", ["ab", "a² + b²", "4ab"]),
            ("When geometrically proving (a - b)², why must b² be added after subtracting 2ab from a²?", "Because the corner region of area b² is subtracted twice", ["To make the area positive", "Because b² is outside the square", "It is an arbitrary adjustment"]),
            ("The geometric representation of a² - b² is achieved by cutting out a small square of side b from a larger square of side a. The resulting shape is:", "an L-shaped region of area a² - b²", ["a triangle", "a smaller square", "a circle"]),
            ("How is the L-shaped region of area a² - b² converted into a single rectangle?", "By cutting along a line and rearranging the two trapezoids into a rectangle of (a + b) by (a - b)", ["By folding it in half", "By stretching it", "By adding another square"]),
            ("In the geometric model of (x + a)(x + b), the constant term ab geometrically represents:", "the area of the corner rectangle of dimensions a by b", ["the perimeter", "the diagonal", "the area of the central square"]),
            ("In the geometric model of (x + a)(x + b), the middle term (a + b)x represents:", "the combined area of two rectangular strips of width x and lengths a and b", ["the total perimeter", "the corner area", "a square of side x"]),
            ("A student cuts a square of side 10 cm and two strips of 10 cm by 3 cm, and one square of 3 cm by 3 cm. Assembled together, they form a square of area:", "(10 + 3)² = 13² = 169 cm²", ["130 cm²", "109 cm²", "160 cm²"]),
            ("Which ancient mathematician is famous for using geometric dissections to establish algebraic identities in his book 'Elements'?", "Euclid (Book II)", ["Pythagoras", "Archimedes", "Aryabhata"]),
            ("The identity (a + b)² = a² + 2ab + b² corresponds to which proposition in Euclid's Elements Book II?", "Proposition 4", ["Proposition 1", "Proposition 9", "Proposition 14"])
        ],
        'tmpls': [
            "{0}",
            "Question on geometric identity proofs: {0}",
            "Regarding geometric dissection of algebraic identities: {0}",
            "Identify the correct geometric fact: {0}",
            "Select the accurate statement: {0}",
            "Conceptual geometric dissection question: {0}",
            "Which option correctly answers: {0}",
            "What is the mathematical rationale: {0}",
            "Choose the true geometric property: {0}",
            "Evaluate the geometric dissection concept: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Visualize the geometric configuration.**\nRecall the geometric area dissection model for algebraic identities.\n\n**Step 2: Analyze the geometric decomposition.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Word problems on rectangular dimensions and area
    arch4 = {
        'data': [
            ("A swimming pool has length (x + 8) meters and breadth (x + 3) meters. What is its surface area?", "x^2 + 11x + 24 m^2", ["x^2 + 24 m^2", "x^2 + 11x m^2", "2x + 11 m^2"]),
            ("A rectangular classroom has length (x + 7) meters and width (x - 2) meters. What is its floor area?", "x^2 + 5x - 14 m^2", ["x^2 - 14 m^2", "x^2 + 9x - 14 m^2", "2x + 5 m^2"]),
            ("The area of a rectangular garden is given by x² + 7x + 12. Its possible dimensions are:", "(x + 3) and (x + 4)", ["(x + 2) and (x + 6)", "(x + 1) and (x + 12)", "(x - 3) and (x - 4)"]),
            ("The area of a rectangular cardboard sheet is x² + 12x + 35. What are its linear dimensions?", "(x + 5) and (x + 7)", ["(x + 1) and (x + 35)", "(x - 5) and (x - 7)", "(x + 6) and (x + 6)"]),
            ("A rectangular park of length (x + 10) m and width (x + 4) m has its perimeter given by:", "4x + 28 m", ["2x + 14 m", "x^2 + 14x + 40 m", "4x + 14 m"]),
            ("The area of a rectangular plot is x² + 3x - 28. If the length is (x + 7), what is the breadth?", "x - 4", ["x + 4", "x - 7", "x - 28"]),
            ("A rectangular photo frame has outer dimensions (x + 6) by (x + 4). The area enclosed is:", "x^2 + 10x + 24", ["x^2 + 24", "x^2 + 10x", "2x + 10"]),
            ("A farmer expands a square field of side x by 5 meters on one side and 2 meters on the other. The new area is:", "x^2 + 7x + 10", ["x^2 + 10", "x^2 + 7x", "2x + 7"]),
            ("The area of a carpet is x² - 9x + 20. What are its factors?", "(x - 4)(x - 5)", ["(x + 4)(x + 5)", "(x - 2)(x - 10)", "(x - 1)(x - 20)"]),
            ("If a rectangle has area x² - x - 12 and length (x + 3), what is its width?", "x - 4", ["x + 4", "x - 3", "x - 12"])
        ],
        'tmpls': [
            "{0}",
            "Solve the rectangular area problem: {0}",
            "Application of algebraic identities in mensuration: {0}",
            "Calculate the dimensions or area: {0}",
            "Determine the polynomial expression: {0}",
            "Find the correct algebraic expression: {0}",
            "Which option represents: {0}",
            "What is the mathematical solution: {0}",
            "Evaluate the practical geometric model: {0}",
            "Compute the area or side: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Formulate the area or factorisation relation.**\n\\[ \\text{{Area}} = \\text{{Length}} \\times \\text{{Breadth}} = (x + a)(x + b) = x^2 + (a + b)x + ab \\]\n\n**Step 2: Factorise or expand as requested.**\nMatch product and sum of coefficients.\n\n**Step 3: State the final expression.**\nThe result is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: 3D geometric interpretation of volume of cuboid (x + a)(x + b)(x + c)
    arch5 = {
        'data': [
            ("(x + 1)(x + 2)(x + 3)", "x^3 + 6x^2 + 11x + 6", 1, 2, 3),
            ("(x + 2)(x + 3)(x + 4)", "x^3 + 9x^2 + 26x + 24", 2, 3, 4),
            ("(x + 1)(x + 3)(x + 5)", "x^3 + 9x^2 + 23x + 15", 1, 3, 5),
            ("(x + 1)(x + 4)(x + 2)", "x^3 + 7x^2 + 14x + 8", 1, 4, 2),
            ("(x - 1)(x + 2)(x + 3)", "x^3 + 4x^2 + x - 6", -1, 2, 3),
            ("(x + 2)(x - 2)(x + 5)", "x^3 + 5x^2 - 4x - 20", 2, -2, 5),
            ("(x - 1)(x - 2)(x + 3)", "x^3 - 7x + 6", -1, -2, 3),
            ("(x + 1)(x - 2)(x - 3)", "x^3 - 4x^2 + x + 6", 1, -2, -3),
            ("(x - 1)(x - 2)(x - 3)", "x^3 - 6x^2 + 11x - 6", -1, -2, -3),
            ("(x + 2)(x + 2)(x + 3)", "x^3 + 7x^2 + 16x + 12", 2, 2, 3)
        ],
        'tmpls': [
            "Find the volume of a cuboid with dimensions \\( {0} \\):",
            "Expand the cubic product: \\( {0} \\):",
            "The expansion of \\( {0} \\) representing a 3D volume is:",
            "Simplify: \\( {0} \\):",
            "Calculate \\( {0} \\) using extension of Identity IV:",
            "Determine the polynomial representing \\( {0} \\):",
            "What is the result of multiplying \\( {0} \\)?",
            "Which expression is equal to \\( {0} \\)?",
            "Evaluate the continued product \\( {0} \\):",
            "Compute: \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("+", "-"),
                item[1].replace("-", "+"),
                f"x^3 + {item[2]+item[3]+item[4]}x + {item[2]*item[3]*item[4]}"
            ],
            f"**Step 1: Multiply the first two factors using \\( (x + a)(x + b) \\).**\nExpand \\( (x + {item[2]})(x + {item[3]}) = x^2 + ({item[2] + item[3]})x + {item[2]*item[3]} \\).\n\n**Step 2: Multiply the quadratic trinomial by the third linear factor.**\nDistribute each term through \\( (x + {item[4]}) \\).\n\n**Step 3: Combine like terms.**\nThe expanded polynomial is \\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 6: Perimeter and area relations from geometric dissections
    arch6 = {
        'data': [
            ("A square of side a is divided into four regions: a square of side b, two rectangles of a x b, and a remaining region. The area of the remaining region is:", "(a - b)^2", ["a^2 - b^2", "a^2 + b^2", "2ab"]),
            ("If a wire of fixed length is bent into a rectangle, which shape encloses the maximum area according to geometric identity models?", "a square (a = b)", ["a long thin rectangle", "a triangle", "a circle"]),
            ("In the expansion of (x + a)(x + b), if a + b = 0, what does the expression reduce to?", "x^2 - a^2 (Identity III)", ["x^2 + a^2", "x^2", "2ax"]),
            ("In the expansion of (x + a)(x + b), if a = b, what does the expression reduce to?", "(x + a)^2 = x^2 + 2ax + a^2 (Identity I)", ["x^2 - a^2", "x^2 + a^2", "x^2 + 2a"]),
            ("In the expansion of (x + a)(x + b), if a = -b, the middle term of the resulting quadratic trinomial is:", "0 (the linear term vanishes)", ["2ax", "-2ax", "a^2"]),
            ("Two squares have sides x and y. What is the difference between the square of their sum and the sum of their squares?", "(x + y)^2 - (x^2 + y^2) = 2xy", ["xy", "4xy", "x^2 - y^2"]),
            ("What is the difference between the sum of squares and the square of difference?", "(x^2 + y^2) - (x - y)^2 = 2xy", ["-2xy", "4xy", "xy"]),
            ("If the area of a square is 4x^2 + 12x + 9, what is its perimeter?", "4(2x + 3) = 8x + 12", ["2x + 3", "4x + 6", "16x + 24"]),
            ("If the area of a square is 9x^2 - 24x + 16, what is its perimeter?", "4(3x - 4) = 12x - 16", ["3x - 4", "6x - 8", "12x + 16"]),
            ("If the area of a square is 25x^2 + 20x + 4, what is its perimeter?", "4(5x + 2) = 20x + 8", ["5x + 2", "10x + 4", "20x + 4"])
        ],
        'tmpls': [
            "{0}",
            "Solve the geometric problem: {0}",
            "Conceptual geometry question: {0}",
            "Calculate the required value: {0}",
            "Determine the correct expression: {0}",
            "Find the answer: {0}",
            "Which option represents: {0}",
            "What is the mathematical conclusion: {0}",
            "Evaluate the geometric scenario: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand the geometric configuration.**\nRelate side length, perimeter, and area via algebraic identities.\n\n**Step 2: Formulate the mathematical equation.**\n'{item[0]}'.\n\n**Step 3: State the final result.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Higher numerical products using (x + a)(x + b) with base 1000
    arch7 = {
        'data': [
            (1003, 1005, 1000, 3, 5, 1008015),
            (1002, 1004, 1000, 2, 4, 1006008),
            (1001, 1006, 1000, 1, 6, 1007006),
            (1005, 1007, 1000, 5, 7, 1012035),
            (1004, 1006, 1000, 4, 6, 1010024),
            (1002, 1008, 1000, 2, 8, 1010016),
            (1003, 1009, 1000, 3, 9, 1012027),
            (1005, 1008, 1000, 5, 8, 1013040),
            (1006, 1009, 1000, 6, 9, 1015054),
            (1007, 1008, 1000, 7, 8, 1015056)
        ],
        'tmpls': [
            "Evaluate without long multiplication: \\( {0} \\times {1} \\).",
            "Using \\( (x + a)(x + b) = x^2 + (a + b)x + ab \\), calculate \\( {0} \\times {1} \\):",
            "Compute \\( {0} \\times {1} \\) by setting \\( x = 1000 \\):",
            "What is the exact product \\( {0} \\times {1} \\)?",
            "Find \\( ({2} + {3})({2} + {4}) \\):",
            "Calculate \\( {0} \\times {1} \\) algebraically:",
            "Determine the value of \\( {0} \\times {1} \\):",
            "The product \\( {0} \\times {1} \\) obtained via algebraic identity is:",
            "Solve for \\( {0} \\times {1} \\) using standard identities:",
            "Evaluate \\( {0} \\times {1} \\):"
        ],
        'calc': lambda item: (
            str(item[5]),
            [
                str(item[5] + 20),
                str(item[5] - 1000),
                str(item[5] + 10000)
            ],
            f"**Step 1: Express factors relative to base 1000.**\n\\[ {item[0]} = 1000 + {item[3]}, \\quad {item[1]} = 1000 + {item[4]} \\]\n\n**Step 2: Apply Identity IV \\( (x + a)(x + b) = x^2 + (a + b)x + ab \\).**\n\\[ (1000 + {item[3]})(1000 + {item[4]}) = 1000^2 + ({item[3]} + {item[4]})(1000) + ({item[3]})({item[4]}) \\]\n\\[ = 1000000 + {item[3]+item[4]}000 + {item[3]*item[4]} \\]\n\n**Step 3: Sum the terms.**\n\\( = {item[5]} \\)."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 4.2.1: Expansion: (x + y + z)² = x² + y² + z² + 2xy + 2yz + 2zx
# ==============================================================================
def gen_4_2_1():
    tc = "CBSE-9-MGM-4-4.2.1"
    tname = "Expansion: (x + y + z)² = x² + y² + z² + 2xy + 2yz + 2zx"

    # Arch 0: Positive expansions (x + y + z)^2 with basic coefficients
    arch0 = {
        'data': [
            ("(x + y + z)^2", "x^2 + y^2 + z^2 + 2xy + 2yz + 2zx"),
            ("(x + 2y + z)^2", "x^2 + 4y^2 + z^2 + 4xy + 4yz + 2zx"),
            ("(x + y + 2z)^2", "x^2 + y^2 + 4z^2 + 2xy + 4yz + 4zx"),
            ("(2x + y + z)^2", "4x^2 + y^2 + z^2 + 4xy + 2yz + 4zx"),
            ("(x + 2y + 3z)^2", "x^2 + 4y^2 + 9z^2 + 4xy + 12yz + 6zx"),
            ("(2x + 3y + z)^2", "4x^2 + 9y^2 + z^2 + 12xy + 6yz + 4zx"),
            ("(3x + y + 2z)^2", "9x^2 + y^2 + 4z^2 + 6xy + 4yz + 12zx"),
            ("(2x + y + 4z)^2", "4x^2 + y^2 + 16z^2 + 4xy + 8yz + 16zx"),
            ("(a + 2b + c)^2", "a^2 + 4b^2 + c^2 + 4ab + 4bc + 2ca"),
            ("(p + 2q + 3r)^2", "p^2 + 4q^2 + 9r^2 + 4pq + 12qr + 6rp")
        ],
        'tmpls': [
            "Expand using trinomial square identity: \\( {0} \\).",
            "What is the expanded form of \\( {0} \\)?",
            "Apply \\( (x + y + z)^2 = x^2 + y^2 + z^2 + 2xy + 2yz + 2zx \\) to expand \\( {0} \\):",
            "The expansion of \\( {0} \\) is:",
            "Simplify the trinomial square: \\( {0} \\):",
            "Calculate the expansion of \\( {0} \\):",
            "Find the polynomial resulting from \\( {0} \\):",
            "Expand completely: \\( {0} \\):",
            "Which expression is equal to \\( {0} \\)?",
            "Evaluate \\( {0} \\) using algebraic identities:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("+ 2zx", ""),
                item[1].replace("+ 4xy", "+ 2xy") if "+ 4xy" in item[1] else item[1].replace("+ 2xy", "+ xy"),
                item[1].replace("+", "-")
            ],
            f"**Step 1: Identify terms \\( a, b, c \\) for the trinomial square.**\nMatch each term to the formula \\( (a + b + c)^2 \\).\n\n**Step 2: Apply \\( a^2 + b^2 + c^2 + 2ab + 2bc + 2ca \\).**\nSquare each of the three terms and compute the three cross products doubled.\n\n**Step 3: State the expanded result.**\nThe expansion is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Expansions with one negative sign: (x - y + z)^2 or (x + y - z)^2
    arch1 = {
        'data': [
            ("(x - y + z)^2", "x^2 + y^2 + z^2 - 2xy - 2yz + 2zx"),
            ("(x + y - z)^2", "x^2 + y^2 + z^2 + 2xy - 2yz - 2zx"),
            ("(2x - y + z)^2", "4x^2 + y^2 + z^2 - 4xy - 2yz + 4zx"),
            ("(x - 2y + z)^2", "x^2 + 4y^2 + z^2 - 4xy - 4yz + 2zx"),
            ("(x + 2y - z)^2", "x^2 + 4y^2 + z^2 + 4xy - 4yz - 2zx"),
            ("(2x + 3y - z)^2", "4x^2 + 9y^2 + z^2 + 12xy - 6yz - 4zx"),
            ("(3x - y + 2z)^2", "9x^2 + y^2 + 4z^2 - 6xy - 4yz + 12zx"),
            ("(2x - 3y + 4z)^2", "4x^2 + 9y^2 + 16z^2 - 12xy - 24yz + 16zx"),
            ("(a - 2b + 3c)^2", "a^2 + 4b^2 + 9c^2 - 4ab - 12bc + 6ca"),
            ("(4a + b - 2c)^2", "16a^2 + b^2 + 4c^2 + 8ab - 4bc - 16ca")
        ],
        'tmpls': [
            "Expand using algebraic identities: \\( {0} \\).",
            "What is the expansion of \\( {0} \\)?",
            "Apply \\( (x + y + z)^2 \\) taking negative signs into account to expand \\( {0} \\):",
            "The simplified expanded form of \\( {0} \\) is:",
            "Find the expansion: \\( {0} \\):",
            "Calculate \\( {0} \\):",
            "Evaluate \\( {0} \\):",
            "Which of the following is the correct expansion of \\( {0} \\)?",
            "Determine the result of expanding \\( {0} \\):",
            "Compute the square of the trinomial: \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("-", "+"),
                item[1].replace("+ 4zx", "- 4zx") if "+ 4zx" in item[1] else item[1].replace("+ 2zx", "- 2zx"),
                item[1].replace("y^2", "- y^2")
            ],
            f"**Step 1: Write the trinomial as a sum of positive and negative terms.**\n\\[ ({item[0].split('^')[0][1:]})^2 \\]\n\n**Step 2: Square each term.**\nSquares are always non-negative: \\( a^2, b^2, c^2 \\).\n\n**Step 3: Compute the signs of the cross products.**\nA product of positive and negative is negative; two negatives yield positive.\n\nThe final expansion is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Expansions with two negative signs: (x - y - z)^2 or (-x + y - z)^2
    arch2 = {
        'data': [
            ("(x - y - z)^2", "x^2 + y^2 + z^2 - 2xy + 2yz - 2zx"),
            ("(-x + y + z)^2", "x^2 + y^2 + z^2 - 2xy + 2yz - 2zx"),
            ("(2x - y - z)^2", "4x^2 + y^2 + z^2 - 4xy + 2yz - 4zx"),
            ("(x - 2y - 3z)^2", "x^2 + 4y^2 + 9z^2 - 4xy + 12yz - 6zx"),
            ("(-2x + 3y + 2z)^2", "4x^2 + 9y^2 + 4z^2 - 12xy + 12yz - 8zx"),
            ("(3a - 7b - c)^2", "9a^2 + 49b^2 + c^2 - 42ab + 14bc - 6ca"),
            ("(-x + 2y - 3z)^2", "x^2 + 4y^2 + 9z^2 - 4xy - 12yz + 6zx"),
            ("(2a - 5b - 3c)^2", "4a^2 + 25b^2 + 9c^2 - 20ab + 30bc - 12ca"),
            ("(-2x - 3y + 5z)^2", "4x^2 + 9y^2 + 25z^2 + 12xy - 30yz - 20zx"),
            ("(p - 2q - r)^2", "p^2 + 4q^2 + r^2 - 4pq + 4qr - 2rp")
        ],
        'tmpls': [
            "Expand: \\( {0} \\).",
            "What is the expansion of \\( {0} \\)?",
            "Calculate \\( {0} \\) using Identity V:",
            "The simplified expanded expression for \\( {0} \\) is:",
            "Find the expansion: \\( {0} \\):",
            "Evaluate \\( {0} \\):",
            "Expand and simplify the trinomial: \\( {0} \\):",
            "Which polynomial represents \\( {0} \\)?",
            "Determine the result of expanding \\( {0} \\):",
            "Compute the square of the signed trinomial: \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("+ 2yz", "- 2yz") if "+ 2yz" in item[1] else item[1].replace("+ 4qr", "- 4qr"),
                item[1].replace("-", "+"),
                item[1].replace("y^2", "- y^2")
            ],
            f"**Step 1: Identify terms including their signs.**\nRecall \\( (-a)^2 = a^2 \\) and \\( 2(-y)(-z) = +2yz \\).\n\n**Step 2: Expand using \\( a^2 + b^2 + c^2 + 2ab + 2bc + 2ca \\).**\nNotice that the cross term involving the two negative terms is positive.\n\n**Step 3: State the final simplified polynomial.**\n\\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Fractional coefficient expansions
    arch3 = {
        'data': [
            ("(\\frac{1}{4}a - \\frac{1}{2}b + 1)^2", "\\frac{1}{16}a^2 + \\frac{1}{4}b^2 + 1 - \\frac{1}{4}ab - b + \\frac{1}{2}a"),
            ("(\\frac{a}{2} + \\frac{b}{3} + \\frac{c}{4})^2", "\\frac{a^2}{4} + \\frac{b^2}{9} + \\frac{c^2}{16} + \\frac{ab}{3} + \\frac{bc}{6} + \\frac{ca}{4}"),
            ("(\\frac{x}{2} - \\frac{y}{3} + 1)^2", "\\frac{x^2}{4} + \\frac{y^2}{9} + 1 - \\frac{xy}{3} - \\frac{2y}{3} + x"),
            ("(\\frac{1}{2}x + \\frac{1}{3}y + 1)^2", "\\frac{1}{4}x^2 + \\frac{1}{9}y^2 + 1 + \\frac{1}{3}xy + \\frac{2}{3}y + x"),
            ("(\\frac{a}{3} - \\frac{b}{2} - 1)^2", "\\frac{a^2}{9} + \\frac{b^2}{4} + 1 - \\frac{ab}{3} + b - \\frac{2a}{3}"),
            ("(x + \\frac{y}{2} + \\frac{z}{3})^2", "x^2 + \\frac{y^2}{4} + \\frac{z^2}{9} + xy + \\frac{yz}{3} + \\frac{2zx}{3}"),
            ("(\\frac{x}{3} + \\frac{y}{4} - \\frac{z}{2})^2", "\\frac{x^2}{9} + \\frac{y^2}{16} + \\frac{z^2}{4} + \\frac{xy}{6} - \\frac{yz}{4} - \\frac{zx}{3}"),
            ("(\\frac{1}{3}a - \\frac{1}{4}b + 2)^2", "\\frac{1}{9}a^2 + \\frac{1}{16}b^2 + 4 - \\frac{1}{6}ab - b + \\frac{4}{3}a"),
            ("(2x - \\frac{y}{2} + \\frac{z}{4})^2", "4x^2 + \\frac{y^2}{4} + \\frac{z^2}{16} - 2xy - \\frac{yz}{4} + xz"),
            ("(\\frac{a}{4} + \\frac{b}{2} - 1)^2", "\\frac{a^2}{16} + \\frac{b^2}{4} + 1 + \\frac{ab}{4} - b - \\frac{a}{2}")
        ],
        'tmpls': [
            "Expand: \\( {0} \\).",
            "What is the expansion of the rational coefficient trinomial \\( {0} \\)?",
            "Calculate \\( {0} \\) using Identity V:",
            "The simplified expansion of \\( {0} \\) is:",
            "Find the expansion: \\( {0} \\):",
            "Evaluate \\( {0} \\):",
            "Which polynomial represents \\( {0} \\)?",
            "Determine the result of expanding \\( {0} \\):",
            "Compute the square: \\( {0} \\):",
            "Simplify completely: \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("+ 1", "- 1") if "+ 1" in item[1] else item[1].replace("+ 4", "- 4"),
                item[1].replace("-", "+"),
                item[1].replace("\\frac{1}{16}", "\\frac{1}{8}") if "\\frac{1}{16}" in item[1] else item[1] + " + 1"
            ],
            f"**Step 1: Identify each fraction term as \\( a, b, c \\).**\nTake careful note of fractions and signs.\n\n**Step 2: Square each term.**\nSquare numerators and denominators.\n\n**Step 3: Compute the three cross products \\( 2ab, 2bc, 2ca \\).**\nMultiply and cancel common factors.\n\nThe expanded form is \\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 4: Reverse factorisation into (x + y + z)^2
    arch4 = {
        'data': [
            ("4x^2 + 9y^2 + 16z^2 + 12xy - 24yz - 16xz", "(2x + 3y - 4z)^2", "2x", "3y", "-4z"),
            ("x^2 + 4y^2 + 9z^2 + 4xy - 12yz - 6xz", "(x + 2y - 3z)^2", "x", "2y", "-3z"),
            ("9x^2 + 49y^2 + 25z^2 - 42xy + 70yz - 30xz", "(-3x + 7y + 5z)^2", "-3x", "7y", "5z"),
            ("4x^2 + y^2 + z^2 - 4xy - 2yz + 4xz", "(2x - y + z)^2", "2x", "-y", "z"),
            ("25x^2 + 16y^2 + 9z^2 - 40xy + 24yz - 30xz", "(5x - 4y - 3z)^2", "5x", "-4y", "-3z"),
            ("x^2 + y^2 + 4z^2 + 2xy - 4yz - 4xz", "(x + y - 2z)^2", "x", "y", "-2z"),
            ("16x^2 + 25y^2 + z^2 - 40xy - 10yz + 8xz", "(4x - 5y + z)^2", "4x", "-5y", "z"),
            ("9a^2 + 4b^2 + 16c^2 + 12ab - 16bc - 24ca", "(3a + 2b - 4c)^2", "3a", "2b", "-4c"),
            ("x^2 + 4y^2 + z^2 - 4xy - 4yz + 2xz", "(x - 2y + z)^2", "x", "-2y", "z"),
            ("4x^2 + 9y^2 + z^2 - 12xy + 6yz - 4xz", "(2x - 3y + z)^2", "2x", "-3y", "z")
        ],
        'tmpls': [
            "Factorise: \\( {0} \\).",
            "What is the factored form of \\( {0} \\)?",
            "Factorise using trinomial square identity: \\( {0} \\):",
            "The expression \\( {0} \\) can be factored as:",
            "Resolve into factors: \\( {0} \\):",
            "Identify the square of a trinomial that equals: \\( {0} \\):",
            "Which of the following is the factorization of \\( {0} \\)?",
            "Express \\( {0} \\) as a perfect square:",
            "Factorise completely: \\( {0} \\):",
            "Determine the factored trinomial for \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("-", "+"),
                f"({item[2]} - {item[3]} - {item[4].replace('-', '')})^2",
                f"({item[2]} + {item[3]} + {item[4].replace('-', '')})^2"
            ],
            f"**Step 1: Write each squared term as \\( a^2, b^2, c^2 \\).**\nIdentify magnitudes: \\( |a| = {item[2]}, |b| = {item[3]}, |c| = {item[4].replace('-', '')} \\).\n\n**Step 2: Inspect cross-term signs to deduce negative terms.**\nThe terms involving negative signs indicate which variable carries a minus sign.\n\n**Step 3: State the factorised square.**\nThe factorised expression is \\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 5: Coefficients of specific terms in expansions
    arch5 = {
        'data': [
            ("In the expansion of (2x - 3y + 4z)², what is the coefficient of xy?", "-12", "2(2)(-3) = -12", ["12", "-6", "6"]),
            ("In the expansion of (3x + 2y - z)², what is the coefficient of yz?", "-4", "2(2)(-1) = -4", ["4", "-2", "2"]),
            ("In the expansion of (x - 2y - 3z)², what is the coefficient of yz?", "12", "2(-2)(-3) = 12", ["-12", "6", "-6"]),
            ("In the expansion of (4a - b + 2c)², what is the coefficient of ca?", "16", "2(2)(4) = 16", ["8", "-16", "-8"]),
            ("In the expansion of (-2x + 5y - 3z)², what is the coefficient of xy?", "-20", "2(-2)(5) = -20", ["20", "-10", "10"]),
            ("In the expansion of (3x - 4y + 2z)², what is the coefficient of zx?", "12", "2(2)(3) = 12", ["-12", "6", "24"]),
            ("In the expansion of (5x - y - 2z)², what is the coefficient of yz?", "4", "2(-1)(-2) = 4", ["-4", "2", "-2"]),
            ("In the expansion of (x + 3y - 5z)², what is the coefficient of zx?", "-10", "2(-5)(1) = -10", ["10", "-5", "-15"]),
            ("In the expansion of (2a + 3b - c)², what is the coefficient of ab?", "12", "2(2)(3) = 12", ["6", "-12", "24"]),
            ("In the expansion of (a - b - c)², what is the coefficient of bc?", "2", "2(-1)(-1) = 2", ["-2", "1", "-1"])
        ],
        'tmpls': [
            "{0}",
            "Calculate the required coefficient: {0}",
            "Determine the numerical value: {0}",
            "Find the coefficient: {0}",
            "What is the answer? {0}",
            "Solve: {0}",
            "Which option gives: {0}",
            "Evaluate the cross-term coefficient: {0}",
            "Compute: {0}",
            "Identify the value: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[3],
            f"**Step 1: Identify the formula for the relevant cross term.**\nThe cross term is given by \\( 2 \\times (\\text{{first variable term}}) \\times (\\text{{second variable term}}) \\).\n\n**Step 2: Multiply coefficients with signs.**\n{item[2]}.\n\n**Step 3: State the coefficient.**\nThe coefficient is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Surd coefficients in (x + y + z)^2
    arch6 = {
        'data': [
            ("(2x^2 + y^2 + 8z^2 - 2\\sqrt{2}xy + 4\\sqrt{2}yz - 8xz)", "(\\sqrt{2}x - y - 2\\sqrt{2}z)^2", "\\sqrt{2}x", "-y", "-2\\sqrt{2}z"),
            ("(2x^2 + y^2 + 8z^2 + 2\\sqrt{2}xy - 4\\sqrt{2}yz - 8xz)", "(\\sqrt{2}x + y - 2\\sqrt{2}z)^2", "\\sqrt{2}x", "y", "-2\\sqrt{2}z"),
            ("(x^2 + 2y^2 + 3z^2 + 2\\sqrt{2}xy + 2\\sqrt{6}yz + 2\\sqrt{3}zx)", "(x + \\sqrt{2}y + \\sqrt{3}z)^2", "x", "\\sqrt{2}y", "\\sqrt{3}z"),
            ("(3x^2 + 2y^2 + z^2 - 2\\sqrt{6}xy - 2\\sqrt{2}yz + 2\\sqrt{3}zx)", "(\\sqrt{3}x - \\sqrt{2}y + z)^2", "\\sqrt{3}x", "-\\sqrt{2}y", "z"),
            ("(5x^2 + y^2 + z^2 + 2\\sqrt{5}xy + 2yz + 2\\sqrt{5}zx)", "(\\sqrt{5}x + y + z)^2", "\\sqrt{5}x", "y", "z"),
            ("(2a^2 + 3b^2 + c^2 + 2\\sqrt{6}ab + 2\\sqrt{3}bc + 2\\sqrt{2}ca)", "(\\sqrt{2}a + \\sqrt{3}b + c)^2", "\\sqrt{2}a", "\\sqrt{3}b", "c"),
            ("(x^2 + 3y^2 + 2z^2 - 2\\sqrt{3}xy - 2\\sqrt{6}yz + 2\\sqrt{2}zx)", "(x - \\sqrt{3}y + \\sqrt{2}z)^2", "x", "-\\sqrt{3}y", "\\sqrt{2}z"),
            ("(2x^2 + 5y^2 + z^2 - 2\\sqrt{10}xy + 2\\sqrt{5}yz - 2\\sqrt{2}zx)", "(\\sqrt{2}x - \\sqrt{5}y - z)^2", "\\sqrt{2}x", "-\\sqrt{5}y", "-z"),
            ("(x^2 + 4y^2 + 2z^2 + 4xy + 4\\sqrt{2}yz + 2\\sqrt{2}zx)", "(x + 2y + \\sqrt{2}z)^2", "x", "2y", "\\sqrt{2}z"),
            ("(3x^2 + y^2 + 2z^2 - 2\\sqrt{3}xy + 2\\sqrt{2}yz - 2\\sqrt{6}zx)", "(\\sqrt{3}x - y - \\sqrt{2}z)^2", "\\sqrt{3}x", "-y", "-\\sqrt{2}z")
        ],
        'tmpls': [
            "Factorise the surd trinomial square: \\( {0} \\).",
            "What is the factored form of \\( {0} \\)?",
            "Factorise: \\( {0} \\):",
            "The expression \\( {0} \\) is the square of which trinomial?",
            "Express as a perfect square: \\( {0} \\):",
            "Resolve into factors: \\( {0} \\):",
            "Which trinomial squared equals \\( {0} \\)?",
            "Determine the factorisation of \\( {0} \\):",
            "Evaluate the factors of \\( {0} \\):",
            "Find the perfect square trinomial: \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("-", "+"),
                item[1].replace("\\sqrt{2}", "2").replace("\\sqrt{3}", "3"),
                f"({item[2]} + {item[3]} - {item[4]})^2"
            ],
            f"**Step 1: Write each leading term as a square of a radical term.**\n\\( a = {item[2]}, b = {item[3]}, c = {item[4]} \\).\n\n**Step 2: Check cross-product signs.**\nVerify that \\( 2ab, 2bc, 2ca \\) reproduce all radical cross terms.\n\n**Step 3: State the factorised trinomial.**\nThe factored form is \\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 7: Geometric interpretation: Diagonal and surface area of cuboid
    arch7 = {
        'data': [
            ("A cuboid has length l, breadth b, and height h. Its total surface area 2(lb + bh + hl) is related to (l + b + h)² and its space diagonal d² = l² + b² + h² by:", "2(lb + bh + hl) = (l + b + h)² - d²", ["2(lb + bh + hl) = (l + b + h)² + d²", "2(lb + bh + hl) = d² - (l + b + h)", "2(lb + bh + hl) = (l + b + h)d"]),
            ("If the sum of dimensions of a box is (l + b + h) = 19 cm and its diagonal is 11 cm, find its total surface area.", "19² - 11² = 361 - 121 = 240 cm²", ["200 cm²", "220 cm²", "250 cm²"]),
            ("If the sum of three dimensions of a room is 25 m and the diagonal of the room is 15 m, what is the total area of the six faces?", "25² - 15² = 625 - 225 = 400 m²", ["350 m²", "450 m²", "500 m²"]),
            ("If the total surface area of a cuboid is 22 cm² and l² + b² + h² = 14 cm², what is the sum of its dimensions (l + b + h)?", "√(14 + 22) = √36 = 6 cm", ["8 cm", "7 cm", "5 cm"]),
            ("If l + b + h = 20 cm and total surface area is 240 cm², find the length of the space diagonal √(l² + b² + h²).", "√(20² - 240) = √(400 - 240) = √160 = 4√10 cm", ["12 cm", "14 cm", "10 cm"]),
            ("If the diagonal of a cuboid is 5√5 cm and the sum of length, breadth, and height is 19 cm, its total surface area is:", "19² - (5√5)² = 361 - 125 = 236 cm²", ["216 cm²", "250 cm²", "240 cm²"]),
            ("How many faces of a rectangular box are accounted for in the expansion (l + b + h)²?", "all 6 faces (since 2(lb + bh + hl) covers all faces) plus 3 internal squares l² + b² + h²", ["only 3 faces", "only 4 faces", "none"]),
            ("If l + b + h = 15 cm and l² + b² + h² = 83 cm², what is the total surface area?", "15² - 83 = 225 - 83 = 142 cm²", ["140 cm²", "144 cm²", "138 cm²"]),
            ("If total surface area is 180 m² and l + b + h = 18 m, what is the square of the diagonal l² + b² + h²?", "18² - 180 = 324 - 180 = 144 m²", ["120 m²", "150 m²", "136 m²"]),
            ("The space diagonal of a cube of edge a is given by d = a√3. Its total surface area 6a² is related to (3a)² by:", "(3a)² - d² = 9a² - 3a² = 6a²", ["(3a)² + d²", "3a² - d²", "(3a)² / 2"])
        ],
        'tmpls': [
            "{0}",
            "Solve the cuboid geometry problem using Identity V: {0}",
            "Application of (l + b + h)² in cuboid mensuration: {0}",
            "Calculate the required value: {0}",
            "Determine the result: {0}",
            "Find the answer: {0}",
            "Which option represents: {0}",
            "What is the mathematical solution: {0}",
            "Evaluate the geometric scenario: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the trinomial square identity applied to dimensions.**\n\\[ (l + b + h)^2 = (l^2 + b^2 + h^2) + 2(lb + bh + hl) = d^2 + \\text{{Total Surface Area}} \\]\n\n**Step 2: Substitute the given quantities.**\nSolve for the unknown.\n\n**Step 3: State the final calculated value.**\nThe solution is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 4.2.2: Applications in algebraic simplification
# ==============================================================================
def gen_4_2_2():
    tc = "CBSE-9-MGM-4-4.2.2"
    tname = "Applications in algebraic simplification"

    # Arch 0: Finding a^2 + b^2 + c^2 given a + b + c and ab + bc + ca
    arch0 = {
        'data': [
            (9, 26, 29, "9^2 - 2(26) = 81 - 52 = 29"),
            (10, 31, 38, "10^2 - 2(31) = 100 - 62 = 38"),
            (12, 47, 50, "12^2 - 2(47) = 144 - 94 = 50"),
            (8, 19, 26, "8^2 - 2(19) = 64 - 38 = 26"),
            (7, 15, 19, "7^2 - 2(15) = 49 - 30 = 19"),
            (11, 38, 45, "11^2 - 2(38) = 121 - 76 = 45"),
            (6, 11, 14, "6^2 - 2(11) = 36 - 22 = 14"),
            (15, 71, 83, "15^2 - 2(71) = 225 - 142 = 83"),
            (13, 50, 69, "13^2 - 2(50) = 169 - 100 = 69"),
            (14, 60, 76, "14^2 - 2(60) = 196 - 120 = 76")
        ],
        'tmpls': [
            "If \\( a + b + c = {0} \\) and \\( ab + bc + ca = {1} \\), find \\( a^2 + b^2 + c^2 \\).",
            "Given that \\( a + b + c = {0} \\) and \\( ab + bc + ca = {1} \\), what is \\( a^2 + b^2 + c^2 \\)?",
            "Calculate \\( a^2 + b^2 + c^2 \\) when \\( a + b + c = {0} \\) and \\( ab + bc + ca = {1} \\):",
            "Determine \\( a^2 + b^2 + c^2 \\) if \\( a + b + c = {0} \\) and \\( ab + bc + ca = {1} \\):",
            "Find the numerical value of \\( a^2 + b^2 + c^2 \\):",
            "Evaluate \\( a^2 + b^2 + c^2 \\) given \\( a + b + c = {0} \\) and \\( ab + bc + ca = {1} \\):",
            "The value of \\( a^2 + b^2 + c^2 \\) for \\( a + b + c = {0} \\) and \\( ab + bc + ca = {1} \\) is:",
            "Compute \\( a^2 + b^2 + c^2 \\):",
            "Solve for \\( a^2 + b^2 + c^2 \\) knowing \\( a + b + c = {0} \\) and \\( ab + bc + ca = {1} \\):",
            "What does \\( a^2 + b^2 + c^2 \\) equal if \\( a + b + c = {0} \\) and \\( ab + bc + ca = {1} \\)?"
        ],
        'calc': lambda item: (
            str(item[2]),
            [
                str(item[0]**2),
                str(item[2] + 10),
                str(item[2] - 4)
            ],
            f"**Step 1: Write down Identity V.**\n\\[ (a + b + c)^2 = (a^2 + b^2 + c^2) + 2(ab + bc + ca) \\]\n\n**Step 2: Rearrange to isolate \\( a^2 + b^2 + c^2 \\).**\n\\[ a^2 + b^2 + c^2 = (a + b + c)^2 - 2(ab + bc + ca) \\]\n\n**Step 3: Substitute the given values.**\n\\[ a^2 + b^2 + c^2 = ({item[0]})^2 - 2({item[1]}) = {item[0]**2} - {2*item[1]} = {item[2]} \\]."
        ),
        'diff': 'medium'
    }

    # Arch 1: Finding ab + bc + ca given a + b + c and a^2 + b^2 + c^2
    arch1 = {
        'data': [
            (9, 35, 23, "(81 - 35) / 2 = 46 / 2 = 23"),
            (10, 40, 30, "(100 - 40) / 2 = 60 / 2 = 30"),
            (12, 64, 40, "(144 - 64) / 2 = 80 / 2 = 40"),
            (8, 30, 17, "(64 - 30) / 2 = 34 / 2 = 17"),
            (7, 25, 12, "(49 - 25) / 2 = 24 / 2 = 12"),
            (11, 61, 30, "(121 - 61) / 2 = 60 / 2 = 30"),
            (6, 20, 8, "(36 - 20) / 2 = 16 / 2 = 8"),
            (13, 69, 50, "(169 - 69) / 2 = 100 / 2 = 50"),
            (15, 85, 70, "(225 - 85) / 2 = 140 / 2 = 70"),
            (14, 76, 60, "(196 - 76) / 2 = 120 / 2 = 60")
        ],
        'tmpls': [
            "If \\( a + b + c = {0} \\) and \\( a^2 + b^2 + c^2 = {1} \\), find \\( ab + bc + ca \\).",
            "Given \\( a + b + c = {0} \\) and \\( a^2 + b^2 + c^2 = {1} \\), what is \\( ab + bc + ca \\)?",
            "Calculate \\( ab + bc + ca \\) when \\( a + b + c = {0} \\) and \\( a^2 + b^2 + c^2 = {1} \\):",
            "Determine \\( ab + bc + ca \\) if \\( a + b + c = {0} \\) and \\( a^2 + b^2 + c^2 = {1} \\):",
            "Evaluate \\( ab + bc + ca \\) given \\( a + b + c = {0} \\) and \\( a^2 + b^2 + c^2 = {1} \\):",
            "Find the numerical value of \\( ab + bc + ca \\):",
            "The value of \\( ab + bc + ca \\) for \\( a + b + c = {0} \\) and \\( a^2 + b^2 + c^2 = {1} \\) is:",
            "What does \\( ab + bc + ca \\) equal if \\( a + b + c = {0} \\) and \\( a^2 + b^2 + c^2 = {1} \\)?",
            "Compute \\( ab + bc + ca \\):",
            "Solve for \\( ab + bc + ca \\):"
        ],
        'calc': lambda item: (
            str(item[2]),
            [
                str(item[2] * 2),
                str(item[2] + 5),
                str(item[2] - 3)
            ],
            f"**Step 1: Write Identity V.**\n\\[ (a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca) \\]\n\n**Step 2: Rearrange to solve for \\( ab + bc + ca \\).**\n\\[ ab + bc + ca = \\frac{{(a + b + c)^2 - (a^2 + b^2 + c^2)}}{{2}} \\]\n\n**Step 3: Substitute and evaluate.**\n\\[ = \\frac{{{item[0]}^2 - {item[1]}}}{{2}} = \\frac{{{item[0]**2} - {item[1]}}}{{2}} = {item[2]} \\]."
        ),
        'diff': 'medium'
    }

    # Arch 2: Finding a + b + c given a^2 + b^2 + c^2 and ab + bc + ca
    arch2 = {
        'data': [
            (29, 26, 9, "√(29 + 2*26) = √81 = 9"),
            (50, 47, 12, "√(50 + 2*47) = √144 = 12"),
            (38, 31, 10, "√(38 + 2*31) = √100 = 10"),
            (26, 19, 8, "√(26 + 2*19) = √64 = 8"),
            (19, 15, 7, "√(19 + 2*15) = √49 = 7"),
            (45, 38, 11, "√(45 + 2*38) = √121 = 11"),
            (14, 11, 6, "√(14 + 2*11) = √36 = 6"),
            (69, 50, 13, "√(69 + 2*50) = √169 = 13"),
            (83, 71, 15, "√(83 + 2*71) = √225 = 15"),
            (76, 60, 14, "√(76 + 2*60) = √196 = 14")
        ],
        'tmpls': [
            "If \\( a^2 + b^2 + c^2 = {0} \\) and \\( ab + bc + ca = {1} \\), find \\( a + b + c \\) (positive value).",
            "Given \\( a^2 + b^2 + c^2 = {0} \\) and \\( ab + bc + ca = {1} \\), what is \\( a + b + c \\)?",
            "Calculate \\( a + b + c \\) when \\( a^2 + b^2 + c^2 = {0} \\) and \\( ab + bc + ca = {1} \\):",
            "Determine \\( a + b + c \\) if \\( a^2 + b^2 + c^2 = {0} \\) and \\( ab + bc + ca = {1} \\):",
            "Find the positive sum \\( a + b + c \\):",
            "Evaluate \\( a + b + c \\) given \\( a^2 + b^2 + c^2 = {0} \\) and \\( ab + bc + ca = {1} \\):",
            "The value of \\( a + b + c \\) for \\( a^2 + b^2 + c^2 = {0} \\) and \\( ab + bc + ca = {1} \\) is:",
            "What does \\( a + b + c \\) equal if \\( a^2 + b^2 + c^2 = {0} \\) and \\( ab + bc + ca = {1} \\)?",
            "Compute \\( a + b + c \\):",
            "Solve for \\( a + b + c \\):"
        ],
        'calc': lambda item: (
            str(item[2]),
            [
                str(item[2] + 2),
                str(item[2] - 1),
                str(item[2]**2)
            ],
            f"**Step 1: Write Identity V.**\n\\[ (a + b + c)^2 = (a^2 + b^2 + c^2) + 2(ab + bc + ca) \\]\n\n**Step 2: Substitute given values.**\n\\[ (a + b + c)^2 = {item[0]} + 2({item[1]}) = {item[0]} + {2*item[1]} = {item[2]**2} \\]\n\n**Step 3: Take square root.**\n\\[ a + b + c = \\sqrt{{{item[2]**2}}} = {item[2]} \\]."
        ),
        'diff': 'medium'
    }

    # Arch 3: Algebraic sum/difference of two trinomial squares
    arch3 = {
        'data': [
            ("(a + b + c)^2 + (a - b - c)^2", "2(a^2 + b^2 + c^2 + 2bc)", ["2(a^2 + b^2 + c^2)", "4ab + 4ca", "2a^2"]),
            ("(a + b + c)^2 - (a - b - c)^2", "4a(b + c)", ["4(ab + bc + ca)", "2(b^2 + c^2)", "4bc"]),
            ("(x + y + z)^2 + (x - y + z)^2", "2(x^2 + y^2 + z^2 + 2zx)", ["2(x^2 + y^2 + z^2)", "4xy + 4yz", "2y^2"]),
            ("(x + y + z)^2 - (x - y + z)^2", "4y(x + z)", ["4(xy + yz)", "4(x^2 + z^2)", "2y^2"]),
            ("(a + b + c)^2 + (a + b - c)^2", "2(a^2 + b^2 + c^2 + 2ab)", ["2(a^2 + b^2 + c^2)", "4ab", "2c^2"]),
            ("(a + b + c)^2 - (a + b - c)^2", "4c(a + b)", ["4(ac + bc)", "2(a^2 + b^2)", "4ab"]),
            ("Simplify: (x + 2y + 3z)^2 - (x - 2y + 3z)^2", "8y(x + 3z) = 8xy + 24yz", ["4xy + 12yz", "16y(x + 3z)", "8y"]),
            ("Simplify: (2x - y + z)^2 - (2x + y - z)^2", "8x(-y + z) = -8xy + 8xz", ["-4xy + 4xz", "8x(y + z)", "-16xy"]),
            ("Simplify: (a + b + c)^2 + (a - b + c)^2 + (a + b - c)^2 + (-a + b + c)^2", "4(a^2 + b^2 + c^2)", ["2(a^2 + b^2 + c^2)", "8(ab + bc + ca)", "4(a + b + c)^2"]),
            ("Simplify: (x + y + z)^2 + (x + y - z)^2 + (x - y + z)^2 + (x - y - z)^2", "4(x^2 + y^2 + z^2)", ["2(x^2 + y^2 + z^2)", "4(xy + yz + zx)", "8x^2"])
        ],
        'tmpls': [
            "Simplify: \\( {0} \\).",
            "What does the algebraic expression simplify to: \\( {0} \\)?",
            "Evaluate the combined expansion: \\( {0} \\):",
            "Calculate \\( {0} \\):",
            "Find the simplified form of \\( {0} \\):",
            "Determine the result of \\( {0} \\):",
            "Which expression is equal to \\( {0} \\)?",
            "Simplify the sum/difference: \\( {0} \\):",
            "Compute: \\( {0} \\):",
            "What is the result of evaluating \\( {0} \\)?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Expand each trinomial square using Identity V.**\nApply \\( (p + q + r)^2 = p^2 + q^2 + r^2 + 2pq + 2qr + 2rp \\) to each bracket.\n\n**Step 2: Add or subtract the corresponding terms.**\nNotice that cross terms with opposite signs cancel out while terms with identical signs double.\n\n**Step 3: State the simplified expression.**\nThe result is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 4: Special case: a + b + c = 0 applications in quadratic forms
    arch4 = {
        'data': [
            ("If a + b + c = 0, what is the value of (ab + bc + ca) in terms of (a^2 + b^2 + c^2)?", "-(a^2 + b^2 + c^2) / 2", ["(a^2 + b^2 + c^2) / 2", "a^2 + b^2 + c^2", "0"]),
            ("If a + b + c = 0 and a^2 + b^2 + c^2 = 40, find ab + bc + ca.", "-20", "(0 - 40) / 2 = -20", ["20", "-40", "0"]),
            ("If a + b + c = 0 and a^2 + b^2 + c^2 = 50, find ab + bc + ca.", "-25", "(0 - 50) / 2 = -25", ["25", "-50", "0"]),
            ("If a + b + c = 0 and ab + bc + ca = -18, find a^2 + b^2 + c^2.", "36", "0 - 2(-18) = 36", ["-36", "18", "0"]),
            ("If a + b + c = 0 and ab + bc + ca = -15, find a^2 + b^2 + c^2.", "30", "0 - 2(-15) = 30", ["-30", "15", "0"]),
            ("If a + b + c = 0 and ab + bc + ca = -24, what is a^2 + b^2 + c^2?", "48", "0 - 2(-24) = 48", ["-48", "24", "0"]),
            ("Can a^2 + b^2 + c^2 ever be negative for real numbers a, b, c?", "No, sum of squares of real numbers is always non-negative (≥ 0)", ["Yes, if numbers are negative", "Yes, if sum is zero", "Only if ab < 0"]),
            ("If a + b + c = 0 and a^2 + b^2 + c^2 = 0, what are the values of a, b, c?", "a = b = c = 0", ["a = 1, b = -1, c = 0", "any numbers summing to zero", "undefined"]),
            ("If a + b + c = 0, what is the value of a^2 / (bc) + b^2 / (ca) + c^2 / (ab)?", "3", "(a^3 + b^3 + c^3)/(abc) = 3abc / abc = 3", ["0", "1", "-3"]),
            ("If a + b + c = 0, evaluate (a + b)^2 + (b + c)^2 + (c + a)^2 in terms of a^2 + b^2 + c^2.", "a^2 + b^2 + c^2", ["2(a^2 + b^2 + c^2)", "0", "4(a^2 + b^2 + c^2)"])
        ],
        'tmpls': [
            "{0}",
            "Solve the conditional identity problem: {0}",
            "Given the condition a + b + c = 0: {0}",
            "Calculate the required value: {0}",
            "Determine the result: {0}",
            "Find the answer: {0}",
            "Which option represents: {0}",
            "What is the mathematical solution: {0}",
            "Evaluate under a + b + c = 0: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[3] if len(item) > 3 else item[2],
            f"**Step 1: Set \\( a + b + c = 0 \\) in Identity V.**\n\\[ (0)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca) \\]\n\n**Step 2: Relate \\( a^2 + b^2 + c^2 \\) and \\( ab + bc + ca \\).**\n\\[ a^2 + b^2 + c^2 = -2(ab + bc + ca) \\]\n\n**Step 3: State the final evaluated value.**\nThe solution is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Numerical applications using (a + b + c)^2
    arch5 = {
        'data': [
            (102, 100, 1, 1, "100 + 1 + 1", 10404),
            (112, 100, 10, 2, "100 + 10 + 2", 12544),
            (213, 200, 10, 3, "200 + 10 + 3", 45369),
            (315, 300, 10, 5, "300 + 10 + 5", 99225),
            (123, 100, 20, 3, "100 + 20 + 3", 15129),
            (105, 100, 3, 2, "100 + 3 + 2", 11025),
            (206, 200, 4, 2, "200 + 4 + 2", 42436),
            (115, 100, 10, 5, "100 + 10 + 5", 13225),
            (124, 100, 20, 4, "100 + 20 + 4", 15376),
            (312, 300, 10, 2, "300 + 10 + 2", 97344)
        ],
        'tmpls': [
            "Evaluate \\( {0}^2 \\) by splitting as a trinomial \\( ({1} + {2} + {3})^2 \\):",
            "Calculate \\( {0}^2 \\) using the three-term expansion identity:",
            "Find the value of \\( {0}^2 \\) via \\( (a + b + c)^2 \\):",
            "What is the exact square \\( {0}^2 \\)?",
            "Compute \\( {0}^2 \\) algebraically:",
            "Determine \\( {0}^2 \\) using Identity V:",
            "The square \\( {0}^2 \\) calculated via trinomial identity is:",
            "Solve for \\( {0}^2 \\) without long multiplication:",
            "Evaluate \\( ({1} + {2} + {3})^2 \\):",
            "Compute \\( {0}^2 \\):"
        ],
        'calc': lambda item: (
            str(item[5]),
            [
                str(item[5] + 50),
                str(item[5] - 100),
                str(item[5] + 200)
            ],
            f"**Step 1: Express the number as a trinomial sum of convenient numbers.**\n\\[ {item[0]} = {item[1]} + {item[2]} + {item[3]} \\]\n\n**Step 2: Apply Identity V.**\n\\[ ({item[1]} + {item[2]} + {item[3]})^2 = {item[1]}^2 + {item[2]}^2 + {item[3]}^2 + 2({item[1]})({item[2]}) + 2({item[2]})({item[3]}) + 2({item[3]})({item[1]}) \\]\n\n**Step 3: Sum all six terms.**\n\\( = {item[5]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 6: Variable substitution and cyclic expressions
    arch6 = {
        'data': [
            ("If x + y + z = 1, then x² + y² + z² + 2(xy + yz + zx) equals:", "1", ["0", "2", "3"]),
            ("What is the value of (x - y)² + (y - z)² + (z - x)² in terms of x² + y² + z² and xy + yz + zx?", "2(x² + y² + z² - xy - yz - zx)", ["x² + y² + z² - xy - yz - zx", "2(x² + y² + z²)", "4(xy + yz + zx)"]),
            ("If x² + y² + z² = xy + yz + zx for real numbers x, y, z, what must be true?", "x = y = z", ["x + y + z = 0", "x, y, z are all zero", "no relation exists"]),
            ("If (x - y)² + (y - z)² + (z - x)² = 0 for real numbers, then:", "x = y = z", ["x + y + z = 0", "xyz = 1", "x = y = -z"]),
            ("If a + b + c = 6 and a² + b² + c² = 14, what is the value of (a - b)² + (b - c)² + (c - a)²?", "2(14 - 11) = 6", ["12", "14", "8"]),
            ("If a + b + c = 9 and a² + b² + c² = 29, what is ab + bc + ca?", "26", ["24", "28", "30"]),
            ("If a + b + c = 12 and ab + bc + ca = 47, find (a - b)² + (b - c)² + (c - a)².", "2(50 - 47) = 6", ["8", "10", "4"]),
            ("If x/y + y/z + z/x = k, is it directly quadratic?", "No, it is a rational cyclic expression", ["Yes", "Only if k = 0", "Only if x=y=z"]),
            ("In the expression x² + y² + z² - xy - yz - zx, multiplying by 2 yields:", "(x - y)² + (y - z)² + (z - x)²", ["(x + y + z)²", "2(x + y + z)", "(x - y - z)²"]),
            ("If x² + y² + z² - xy - yz - zx ≥ 0 for all real x, y, z, equality holds if and only if:", "x = y = z", ["x = 0", "x + y + z = 0", "xyz = 0"])
        ],
        'tmpls': [
            "{0}",
            "Evaluate the cyclic algebraic expression: {0}",
            "Theoretical identity question: {0}",
            "Calculate: {0}",
            "Determine the relationship: {0}",
            "Find the correct value: {0}",
            "Which option represents: {0}",
            "What is the mathematical conclusion: {0}",
            "Analyze the expression: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recognize the standard cyclic algebraic identity.**\n\\[ 2(x^2 + y^2 + z^2 - xy - yz - zx) = (x - y)^2 + (y - z)^2 + (z - x)^2 \\]\n\n**Step 2: Apply the given values or conditions.**\nSubstitute known relations into the identity.\n\n**Step 3: State the final conclusion.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Advanced word and multi-variable applications
    arch7 = {
        'data': [
            ("Three numbers a, b, c have sum 15, and sum of their squares is 83. Find the sum of their pairwise products ab + bc + ca.", "71", "(225 - 83) / 2 = 142 / 2 = 71", ["70", "72", "68"]),
            ("Three numbers have sum 10, and their pairwise products sum to 31. What is the sum of their squares?", "38", "100 - 2(31) = 38", ["36", "40", "42"]),
            ("The sum of lengths of edges of a rectangular prism is 4(l + b + h) = 60 cm. If the surface area is 134 cm², find the space diagonal d.", "d = √(15² - 134) = √(225 - 134) = √91 cm", ["9 cm", "10 cm", "√95 cm"]),
            ("Three integers have sum 12. If the sum of their squares is 50, what is the sum of their pairwise products?", "47", "(144 - 50) / 2 = 47", ["45", "48", "50"]),
            ("If the sum of squares of three numbers is 65 and pairwise products sum to 28, find their sum.", "√(65 + 56) = √121 = 11", ["10", "12", "13"]),
            ("If a + 2b + c = 10 and a² + 4b² + c² = 40, find 2ab + 2bc + ca.", "30", "(100 - 40) / 2 = 30", ["20", "25", "35"]),
            ("If 2x + y + z = 12 and 4x² + y² + z² = 50, find 2xy + yz + 2zx.", "47", "(144 - 50) / 2 = 47", ["45", "50", "42"]),
            ("Three quantities x, y, z satisfy x + y + z = 6 and xy + yz + zx = 11. Find x² + y² + z².", "14", "36 - 22 = 14", ["12", "16", "18"]),
            ("If a + b + c = 8 and a² + b² + c² = 26, what is ab + bc + ca?", "19", "(64 - 26) / 2 = 19", ["18", "20", "21"]),
            ("A parcel of dimensions x, y, z has total ribbon length 4(x + y + z) = 80 cm. If its total surface area is 300 cm², what is x² + y² + z²?", "20² - 300 = 400 - 300 = 100 cm²", ["150 cm²", "80 cm²", "120 cm²"])
        ],
        'tmpls': [
            "{0}",
            "Solve the multi-variable problem: {0}",
            "Application of trinomial identities: {0}",
            "Calculate the required value: {0}",
            "Determine the result: {0}",
            "Find the answer: {0}",
            "Which option represents: {0}",
            "What is the mathematical solution: {0}",
            "Evaluate the scenario: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[3] if len(item) > 3 else item[2],
            f"**Step 1: Set up the algebraic relation using Identity V.**\n\\[ (a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca) \\]\n\n**Step 2: Substitute the given quantities.**\nSolve for the requested variable.\n\n**Step 3: State the final evaluated value.**\nThe solution is {item[1]}."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_4_1_4()
    q2 = gen_4_2_1()
    q3 = gen_4_2_2()
    print(f"gen_4_1_4: {len(q1)} questions")
    print(f"gen_4_2_1: {len(q2)} questions")
    print(f"gen_4_2_2: {len(q3)} questions")
