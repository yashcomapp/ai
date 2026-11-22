# scripts/build_cbse9_mgm_ch4_part1.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 4: Exploring Algebraic Identities
Part 1:
- Subtopic 4.1.1: Identity I: (a + b)² = a² + 2ab + b²
- Subtopic 4.1.2: Identity II: (a - b)² = a² - 2ab + b²
- Subtopic 4.1.3: Identity III: (a + b)(a - b) = a² - b²
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 240 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 4
CH_NAME = "Exploring Algebraic Identities"

# ==============================================================================
# SUBTOPIC 4.1.1: Identity I: (a + b)² = a² + 2ab + b²
# ==============================================================================
def gen_4_1_1():
    tc = "CBSE-9-MGM-4-4.1.1"
    tname = "Identity I: (a + b)² = a² + 2ab + b²"

    # Arch 0: Basic expansion (x + k)^2
    arch0 = {
        'data': [
            ("(x + 3)^2", "x^2 + 6x + 9", 3, 6, 9),
            ("(x + 4)^2", "x^2 + 8x + 16", 4, 8, 16),
            ("(x + 5)^2", "x^2 + 10x + 25", 5, 10, 25),
            ("(x + 6)^2", "x^2 + 12x + 36", 6, 12, 36),
            ("(x + 7)^2", "x^2 + 14x + 49", 7, 14, 49),
            ("(x + 8)^2", "x^2 + 16x + 64", 8, 16, 64),
            ("(x + 9)^2", "x^2 + 18x + 81", 9, 18, 81),
            ("(x + 10)^2", "x^2 + 20x + 100", 10, 20, 100),
            ("(y + 2)^2", "y^2 + 4y + 4", 2, 4, 4),
            ("(z + 11)^2", "z^2 + 22z + 121", 11, 22, 121)
        ],
        'tmpls': [
            "Expand using Identity I: \\( {0} \\).",
            "What is the expanded form of \\( {0} \\)?",
            "Apply \\( (a + b)^2 = a^2 + 2ab + b^2 \\) to expand \\( {0} \\):",
            "The expansion of \\( {0} \\) is:",
            "Simplify: \\( {0} \\):",
            "Evaluate the square: \\( {0} \\):",
            "Find the polynomial resulting from expanding \\( {0} \\):",
            "Expand and simplify the binomial square: \\( {0} \\):",
            "Which of the following is equal to \\( {0} \\)?",
            "Calculate \\( {0} \\) using the standard identity:"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"x^2 + {item[4]}",
                f"x^2 + {item[3]}x + {item[3]}",
                f"x^2 + {item[2]}x + {item[4]}"
            ],
            f"**Step 1: Identify terms for Identity I.**\nHere \\( a = x \\) and \\( b = {item[2]} \\).\n\n**Step 2: Apply the formula \\( (a + b)^2 = a^2 + 2ab + b^2 \\).**\n\\[ (x + {item[2]})^2 = x^2 + 2(x)({item[2]}) + {item[2]}^2 \\]\n\n**Step 3: Simplify coefficients.**\nThe expanded form is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Expansion with coefficients (ax + by)^2
    arch1 = {
        'data': [
            ("(2x + 3y)^2", "4x^2 + 12xy + 9y^2", "2x", "3y", "4x^2", "12xy", "9y^2"),
            ("(3x + 2y)^2", "9x^2 + 12xy + 4y^2", "3x", "2y", "9x^2", "12xy", "4y^2"),
            ("(2x + 5y)^2", "4x^2 + 20xy + 25y^2", "2x", "5y", "4x^2", "20xy", "25y^2"),
            ("(3x + 4y)^2", "9x^2 + 24xy + 16y^2", "3x", "4y", "9x^2", "24xy", "16y^2"),
            ("(4x + 3y)^2", "16x^2 + 24xy + 9y^2", "4x", "3y", "16x^2", "24xy", "9y^2"),
            ("(5x + 2y)^2", "25x^2 + 20xy + 4y^2", "5x", "2y", "25x^2", "20xy", "4y^2"),
            ("(3x + 5)^2", "9x^2 + 30x + 25", "3x", "5", "9x^2", "30x", "25"),
            ("(2a + 7b)^2", "4a^2 + 28ab + 49b^2", "2a", "7b", "4a^2", "28ab", "49b^2"),
            ("(4x + 5y)^2", "16x^2 + 40xy + 25y^2", "4x", "5y", "16x^2", "40xy", "25y^2"),
            ("(6x + y)^2", "36x^2 + 12xy + y^2", "6x", "y", "36x^2", "12xy", "y^2")
        ],
        'tmpls': [
            "Expand using algebraic identities: \\( {0} \\).",
            "What is the expansion of \\( {0} \\)?",
            "Calculate \\( {0} \\) by applying Identity I:",
            "The simplified expansion of \\( {0} \\) is:",
            "Apply \\( (a + b)^2 \\) to expand: \\( {0} \\):",
            "Expand: \\( {0} \\):",
            "Find the expanded polynomial for \\( {0} \\):",
            "Which expression is identical to \\( {0} \\)?",
            "Compute the square: \\( {0} \\):",
            "Determine the expansion of \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"{item[4]} + {item[6]}",
                f"{item[4]} + {item[5].replace('2', '1')} + {item[6]}",
                f"{item[4]} - {item[5]} + {item[6]}"
            ],
            f"**Step 1: Identify terms \\( a \\) and \\( b \\).**\n\\( a = {item[2]} \\) and \\( b = {item[3]} \\).\n\n**Step 2: Expand using \\( a^2 + 2ab + b^2 \\).**\n\\[ ({item[2]})^2 + 2({item[2]})({item[3]}) + ({item[3]})^2 \\]\n\n**Step 3: Simplify each term.**\n\\( {item[4]} + {item[5]} + {item[6]} = {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Numerical evaluation of squares using (100 + k)^2
    arch2 = {
        'data': [
            (103, 100, 3, "100^2 + 2(100)(3) + 3^2", 10609),
            (105, 100, 5, "100^2 + 2(100)(5) + 5^2", 11025),
            (104, 100, 4, "100^2 + 2(100)(4) + 4^2", 10816),
            (106, 100, 6, "100^2 + 2(100)(6) + 6^2", 11236),
            (107, 100, 7, "100^2 + 2(100)(7) + 7^2", 11449),
            (108, 100, 8, "100^2 + 2(100)(8) + 8^2", 11664),
            (102, 100, 2, "100^2 + 2(100)(2) + 2^2", 10404),
            (101, 100, 1, "100^2 + 2(100)(1) + 1^2", 10201),
            (109, 100, 9, "100^2 + 2(100)(9) + 9^2", 11881),
            (502, 500, 2, "500^2 + 2(500)(2) + 2^2", 252004)
        ],
        'tmpls': [
            "Evaluate without direct multiplication: \\( {0}^2 \\).",
            "Using Identity I, calculate the value of \\( {0}^2 \\):",
            "Compute \\( {0}^2 \\) using \\( (a + b)^2 = a^2 + 2ab + b^2 \\):",
            "What is the numerical value of \\( {0}^2 \\)?",
            "Evaluate \\( {0}^2 \\) by expressing it as \\( ({1} + {2})^2 \\):",
            "Calculate \\( {0}^2 \\) algebraically:",
            "Find the square \\( {0}^2 \\) using the identity method:",
            "Determine the exact value of \\( {0}^2 \\):",
            "The value of \\( {0}^2 \\) obtained via algebraic identity is:",
            "Solve for \\( {0}^2 \\) using standard identities:"
        ],
        'calc': lambda item: (
            str(item[4]),
            [
                str(item[4] + 10),
                str(item[4] - 20),
                str(item[4] + 100)
            ],
            f"**Step 1: Express the number as a sum of convenient bases.**\n\\[ {item[0]} = {item[1]} + {item[2]} \\]\n\n**Step 2: Apply the identity \\( (a + b)^2 = a^2 + 2ab + b^2 \\).**\n\\[ ({item[1]} + {item[2]})^2 = {item[3]} \\]\n\\[ = {item[1]**2} + {2*item[1]*item[2]} + {item[2]**2} \\]\n\n**Step 3: Sum the terms.**\n\\( = {item[4]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 3: Fractional / reciprocal form: (x + 1/x)^2
    arch3 = {
        'data': [
            ("(x + \\frac{1}{x})^2", "x^2 + 2 + \\frac{1}{x^2}", 2),
            ("(2x + \\frac{1}{2x})^2", "4x^2 + 2 + \\frac{1}{4x^2}", 2),
            ("(3x + \\frac{1}{3x})^2", "9x^2 + 2 + \\frac{1}{9x^2}", 2),
            ("(x + \\frac{2}{x})^2", "x^2 + 4 + \\frac{4}{x^2}", 4),
            ("(2x + \\frac{1}{x})^2", "4x^2 + 4 + \\frac{1}{x^2}", 4),
            ("(x + \\frac{3}{x})^2", "x^2 + 6 + \\frac{9}{x^2}", 6),
            ("(3x + \\frac{1}{x})^2", "9x^2 + 6 + \\frac{1}{x^2}", 6),
            ("(4x + \\frac{1}{2x})^2", "16x^2 + 4 + \\frac{1}{4x^2}", 4),
            ("(x + \\frac{1}{2x})^2", "x^2 + 1 + \\frac{1}{4x^2}", 1),
            ("(5x + \\frac{1}{5x})^2", "25x^2 + 2 + \\frac{1}{25x^2}", 2)
        ],
        'tmpls': [
            "Expand: \\( {0} \\).",
            "What is the expansion of the reciprocal expression \\( {0} \\)?",
            "Calculate \\( {0} \\) using Identity I:",
            "The simplified form of \\( {0} \\) is:",
            "Find the result of expanding \\( {0} \\):",
            "Apply \\( (a + b)^2 \\) to expand: \\( {0} \\):",
            "Simplify completely: \\( {0} \\):",
            "Evaluate \\( {0} \\):",
            "Which expression represents \\( {0} \\)?",
            "Determine the expanded polynomial for \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("+ 2 +", "+"),
                item[1].replace("+ 2 +", "- 2 +") if "+ 2 +" in item[1] else item[1].replace("+ 4 +", "+ 2 +"),
                item[1] + " + 1"
            ],
            f"**Step 1: Identify \\( a \\) and \\( b \\).**\nLet the first term be \\( a \\) and second term be \\( b \\).\n\n**Step 2: Apply \\( (a + b)^2 = a^2 + 2ab + b^2 \\).**\nNotice the cross term \\( 2ab = {item[2]} \\) because \\( x \\) cancels.\n\n**Step 3: State the final simplified form.**\nThe expanded expression is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Value finding: Given x + 1/x = k, find x^2 + 1/x^2
    arch4 = {
        'data': [
            (3, 7, "3^2 - 2 = 9 - 2 = 7"),
            (4, 14, "4^2 - 2 = 16 - 2 = 14"),
            (5, 23, "5^2 - 2 = 25 - 2 = 23"),
            (6, 34, "6^2 - 2 = 36 - 2 = 34"),
            (7, 47, "7^2 - 2 = 49 - 2 = 47"),
            (8, 62, "8^2 - 2 = 64 - 2 = 62"),
            (9, 79, "9^2 - 2 = 81 - 2 = 79"),
            (10, 98, "10^2 - 2 = 100 - 2 = 98"),
            (11, 119, "11^2 - 2 = 121 - 2 = 119"),
            (12, 142, "12^2 - 2 = 144 - 2 = 142")
        ],
        'tmpls': [
            "If \\( x + \\frac{{1}}{{x}} = {0} \\), find the value of \\( x^2 + \\frac{{1}}{{x^2}} \\).",
            "Given that \\( x + \\frac{{1}}{{x}} = {0} \\), what is \\( x^2 + \\frac{{1}}{{x^2}} \\)?",
            "Calculate \\( x^2 + \\frac{{1}}{{x^2}} \\) when \\( x + \\frac{{1}}{{x}} = {0} \\):",
            "Determine the value of \\( x^2 + \\frac{{1}}{{x^2}} \\) if \\( x + \\frac{{1}}{{x}} = {0} \\):",
            "If \\( x + \\frac{{1}}{{x}} = {0} \\), evaluate \\( x^2 + \\frac{{1}}{{x^2}} \\):",
            "Find \\( x^2 + \\frac{{1}}{{x^2}} \\) given \\( x + \\frac{{1}}{{x}} = {0} \\):",
            "The value of \\( x^2 + \\frac{{1}}{{x^2}} \\) for \\( x + \\frac{{1}}{{x}} = {0} \\) is:",
            "What does \\( x^2 + \\frac{{1}}{{x^2}} \\) equal if \\( x + \\frac{{1}}{{x}} = {0} \\)?",
            "Solve for \\( x^2 + \\frac{{1}}{{x^2}} \\) knowing \\( x + \\frac{{1}}{{x}} = {0} \\):",
            "Compute \\( x^2 + \\frac{{1}}{{x^2}} \\) when \\( x + \\frac{{1}}{{x}} = {0} \\):"
        ],
        'calc': lambda item: (
            str(item[1]),
            [
                str(item[0]**2),
                str(item[1] + 4),
                str(item[1] - 2)
            ],
            f"**Step 1: Square both sides of the given equation.**\n\\[ \\left(x + \\frac{{1}}{{x}}\\right)^2 = {item[0]}^2 = {item[0]**2} \\]\n\n**Step 2: Expand the left-hand side using Identity I.**\n\\[ x^2 + 2(x)\\left(\\frac{{1}}{{x}}\\right) + \\frac{{1}}{{x^2}} = x^2 + 2 + \\frac{{1}}{{x^2}} = {item[0]**2} \\]\n\n**Step 3: Subtract 2 to isolate \\( x^2 + \\frac{{1}}{{x^2}} \\).**\n\\[ x^2 + \\frac{{1}}{{x^2}} = {item[0]**2} - 2 = {item[1]} \\]."
        ),
        'diff': 'medium'
    }

    # Arch 5: Symmetric value finding: Given a + b and ab, find a^2 + b^2
    arch5 = {
        'data': [
            (5, 6, 13, "5^2 - 2(6) = 25 - 12 = 13"),
            (7, 12, 25, "7^2 - 2(12) = 49 - 24 = 25"),
            (8, 15, 34, "8^2 - 2(15) = 64 - 30 = 34"),
            (9, 20, 41, "9^2 - 2(20) = 81 - 40 = 41"),
            (6, 8, 20, "6^2 - 2(8) = 36 - 16 = 20"),
            (10, 21, 58, "10^2 - 2(21) = 100 - 42 = 58"),
            (11, 28, 65, "11^2 - 2(28) = 121 - 56 = 65"),
            (12, 35, 74, "12^2 - 2(35) = 144 - 70 = 74"),
            (4, 3, 10, "4^2 - 2(3) = 16 - 6 = 10"),
            (10, 24, 52, "10^2 - 2(24) = 100 - 48 = 52")
        ],
        'tmpls': [
            "If \\( a + b = {0} \\) and \\( ab = {1} \\), find \\( a^2 + b^2 \\).",
            "Given \\( a + b = {0} \\) and \\( ab = {1} \\), what is the value of \\( a^2 + b^2 \\)?",
            "Calculate \\( a^2 + b^2 \\) when \\( a + b = {0} \\) and \\( ab = {1} \\):",
            "Determine \\( a^2 + b^2 \\) if \\( a + b = {0} \\) and \\( ab = {1} \\):",
            "Evaluate \\( a^2 + b^2 \\) given \\( a + b = {0} \\) and \\( ab = {1} \\):",
            "Find the numerical value of \\( a^2 + b^2 \\) for \\( a + b = {0} \\) and \\( ab = {1} \\):",
            "The value of \\( a^2 + b^2 \\) given \\( a + b = {0} \\) and \\( ab = {1} \\) is:",
            "What is \\( a^2 + b^2 \\) if \\( a + b = {0} \\) and \\( ab = {1} \\)?",
            "Compute \\( a^2 + b^2 \\) when \\( a + b = {0} \\) and \\( ab = {1} \\):",
            "Solve for \\( a^2 + b^2 \\) given \\( a + b = {0} \\) and \\( ab = {1} \\):"
        ],
        'calc': lambda item: (
            str(item[2]),
            [
                str(item[0]**2),
                str(item[2] + 2*item[1]),
                str(item[2] - 4)
            ],
            f"**Step 1: Write down Identity I relating the quantities.**\n\\[ (a + b)^2 = a^2 + 2ab + b^2 \\]\n\n**Step 2: Rearrange to express \\( a^2 + b^2 \\).**\n\\[ a^2 + b^2 = (a + b)^2 - 2ab \\]\n\n**Step 3: Substitute the given values.**\n\\[ a^2 + b^2 = ({item[0]})^2 - 2({item[1]}) = {item[0]**2} - {2*item[1]} = {item[2]} \\]."
        ),
        'diff': 'medium'
    }

    # Arch 6: Missing term / coefficient identification
    arch6 = {
        'data': [
            ("If 4x^2 + kx + 9 is a perfect square trinomial (2x + 3)^2, what is k?", "12", "k = 2(2)(3) = 12", ["6", "18", "24"]),
            ("If 9x^2 + 24x + c is a perfect square (3x + 4)^2, what is c?", "16", "c = 4^2 = 16", ["8", "12", "20"]),
            ("If ax^2 + 20x + 25 is a perfect square (2x + 5)^2, what is a?", "4", "2a(5) = 20 => a = 2 => a^2 = 4", ["2", "5", "16"]),
            ("If 16x^2 + kxy + 25y^2 is a perfect square trinomial, what is k?", "40", "k = 2(4)(5) = 40", ["20", "80", "10"]),
            ("If x^2 + 14x + c is a perfect square, what must c be?", "49", "c = (14/2)^2 = 7^2 = 49", ["14", "28", "7"]),
            ("If x^2 + kx + 81 is a perfect square of a binomial, what is the positive value of k?", "18", "k = 2 * 9 = 18", ["9", "36", "81"]),
            ("If 25x^2 + 30x + c is a perfect square, what is the value of c?", "9", "25x^2 = (5x)^2; 2(5)(b) = 30 => b = 3 => c = 9", ["6", "15", "3"]),
            ("If 4x^2 + 28x + k is a perfect square, what is k?", "49", "2(2)(b) = 28 => b = 7 => k = 49", ["14", "28", "21"]),
            ("If 9x^2 + kxy + 16y^2 is of the form (3x + 4y)^2, what is k?", "24", "k = 2(3)(4) = 24", ["12", "48", "7"]),
            ("If 36a^2 + 60ab + c b^2 is a perfect square (6a + 5b)^2, what is c?", "25", "c = 5^2 = 25", ["10", "30", "50"])
        ],
        'tmpls': [
            "{0}",
            "Determine the missing coefficient: {0}",
            "Find the unknown value: {0}",
            "Solve the perfect square problem: {0}",
            "Calculate the required constant: {0}",
            "What is the missing value? {0}",
            "Identity I application: {0}",
            "Identify the value: {0}",
            "Evaluate: {0}",
            "Compute the coefficient: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[3],
            f"**Step 1: Compare with standard form \\( (px + q)^2 = p^2 x^2 + 2pq x + q^2 \\).**\nMatch known coefficients to identify \\( p \\) and \\( q \\).\n\n**Step 2: Equate the target coefficient.**\n{item[2]}.\n\n**Step 3: State the final value.**\nThe missing value is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Geometric interpretation: Area of square of side (a + b)
    arch7 = {
        'data': [
            ("A square park of side length (x + 5) meters has an area given by:", "x^2 + 10x + 25 m^2", ["x^2 + 25 m^2", "x^2 + 5x + 25 m^2", "4x + 20 m^2"]),
            ("A square plot has side (2x + 3) meters. What is its total area?", "4x^2 + 12x + 9 m^2", ["4x^2 + 9 m^2", "4x^2 + 6x + 9 m^2", "2x^2 + 12x + 9 m^2"]),
            ("Geometric dissection shows that a square of side (a + b) decomposes into:", "two squares of areas a² and b², and two rectangles of area ab", ["four equal squares", "one square and three rectangles", "two squares and one rectangle"]),
            ("If the side of a square is increased by 3 units, its area increases from x² to:", "x^2 + 6x + 9", ["x^2 + 9", "x^2 + 3x + 9", "6x + 9"]),
            ("A square tile has side (3a + 2b) cm. Its surface area is:", "9a^2 + 12ab + 4b^2 cm^2", ["9a^2 + 4b^2 cm^2", "9a^2 + 6ab + 4b^2 cm^2", "6a^2 + 12ab + 4b^2 cm^2"]),
            ("A square garden of side (x + 8) meters is expanded. The expression for its area is:", "x^2 + 16x + 64 m^2", ["x^2 + 64 m^2", "x^2 + 8x + 64 m^2", "4x + 32 m^2"]),
            ("The area of a square sheet of metal with side (4x + 1) cm is:", "16x^2 + 8x + 1 cm^2", ["16x^2 + 1 cm^2", "16x^2 + 4x + 1 cm^2", "8x + 2 cm^2"]),
            ("In the geometric proof of (a + b)², what do the two rectangles represent?", "two cross-product regions each of area ab", ["two diagonal regions", "two squares of side a", "two triangles"]),
            ("A square hall of side (5x + 4) meters has floor area:", "25x^2 + 40x + 16 m^2", ["25x^2 + 16 m^2", "25x^2 + 20x + 16 m^2", "10x + 8 m^2"]),
            ("If a square of side x has both dimensions increased by 6, the new area is:", "x^2 + 12x + 36", ["x^2 + 36", "x^2 + 6x + 36", "12x + 36"])
        ],
        'tmpls': [
            "{0}",
            "Solve the geometric identity problem: {0}",
            "Application of Identity I in geometry: {0}",
            "Calculate the area: {0}",
            "Determine the correct expression: {0}",
            "Find the geometric area: {0}",
            "Which option correctly represents: {0}",
            "What is the mathematical answer to: {0}",
            "Evaluate the geometric scenario: {0}",
            "Compute the polynomial area: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the formula for the area of a square.**\n\\[ \\text{{Area}} = (\\text{{side}})^2 \\]\n\n**Step 2: Expand using Identity I \\( (a + b)^2 = a^2 + 2ab + b^2 \\).**\nSubstitute the given side length and expand each term.\n\n**Step 3: State the final resulting area.**\nThe area is {item[1]}."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 4.1.2: Identity II: (a - b)² = a² - 2ab + b²
# ==============================================================================
def gen_4_1_2():
    tc = "CBSE-9-MGM-4-4.1.2"
    tname = "Identity II: (a - b)² = a² - 2ab + b²"

    # Arch 0: Basic expansion (x - k)^2
    arch0 = {
        'data': [
            ("(x - 3)^2", "x^2 - 6x + 9", 3, 6, 9),
            ("(x - 4)^2", "x^2 - 8x + 16", 4, 8, 16),
            ("(x - 5)^2", "x^2 - 10x + 25", 5, 10, 25),
            ("(x - 6)^2", "x^2 - 12x + 36", 6, 12, 36),
            ("(x - 7)^2", "x^2 - 14x + 49", 7, 14, 49),
            ("(x - 8)^2", "x^2 - 16x + 64", 8, 16, 64),
            ("(x - 9)^2", "x^2 - 18x + 81", 9, 18, 81),
            ("(x - 10)^2", "x^2 - 20x + 100", 10, 20, 100),
            ("(y - 2)^2", "y^2 - 4y + 4", 2, 4, 4),
            ("(z - 1)^2", "z^2 - 2z + 1", 1, 2, 1)
        ],
        'tmpls': [
            "Expand using Identity II: \\( {0} \\).",
            "What is the expansion of \\( {0} \\)?",
            "Apply \\( (a - b)^2 = a^2 - 2ab + b^2 \\) to expand \\( {0} \\):",
            "The simplified expanded form of \\( {0} \\) is:",
            "Simplify: \\( {0} \\):",
            "Evaluate the square: \\( {0} \\):",
            "Find the polynomial resulting from expanding \\( {0} \\):",
            "Expand and simplify: \\( {0} \\):",
            "Which expression is equal to \\( {0} \\)?",
            "Calculate \\( {0} \\) using Identity II:"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"x^2 + {item[4]}",
                f"x^2 + {item[3]}x + {item[4]}",
                f"x^2 - {item[3]}x - {item[4]}"
            ],
            f"**Step 1: Identify terms \\( a \\) and \\( b \\).**\n\\( a = x \\) and \\( b = {item[2]} \\).\n\n**Step 2: Apply Identity II \\( (a - b)^2 = a^2 - 2ab + b^2 \\).**\n\\[ (x - {item[2]})^2 = x^2 - 2(x)({item[2]}) + {item[2]}^2 \\]\n\n**Step 3: Simplify coefficients.**\nThe expanded form is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Expansion with coefficients (ax - by)^2
    arch1 = {
        'data': [
            ("(2x - 3y)^2", "4x^2 - 12xy + 9y^2", "2x", "3y", "4x^2", "12xy", "9y^2"),
            ("(3x - 2y)^2", "9x^2 - 12xy + 4y^2", "3x", "2y", "9x^2", "12xy", "4y^2"),
            ("(2x - 5y)^2", "4x^2 - 20xy + 25y^2", "2x", "5y", "4x^2", "20xy", "25y^2"),
            ("(3x - 4y)^2", "9x^2 - 24xy + 16y^2", "3x", "4y", "9x^2", "24xy", "16y^2"),
            ("(4x - 3y)^2", "16x^2 - 24xy + 9y^2", "4x", "3y", "16x^2", "24xy", "9y^2"),
            ("(5x - 2y)^2", "25x^2 - 20xy + 4y^2", "5x", "2y", "25x^2", "20xy", "4y^2"),
            ("(3x - 5)^2", "9x^2 - 30x + 25", "3x", "5", "9x^2", "30x", "25"),
            ("(2a - 7b)^2", "4a^2 - 28ab + 49b^2", "2a", "7b", "4a^2", "28ab", "49b^2"),
            ("(4x - 5y)^2", "16x^2 - 40xy + 25y^2", "4x", "5y", "16x^2", "40xy", "25y^2"),
            ("(7x - 2y)^2", "49x^2 - 28xy + 4y^2", "7x", "2y", "49x^2", "28xy", "4y^2")
        ],
        'tmpls': [
            "Expand using algebraic identities: \\( {0} \\).",
            "What is the expansion of \\( {0} \\)?",
            "Calculate \\( {0} \\) by applying Identity II:",
            "The simplified expansion of \\( {0} \\) is:",
            "Apply \\( (a - b)^2 \\) to expand: \\( {0} \\):",
            "Expand: \\( {0} \\):",
            "Find the expanded polynomial for \\( {0} \\):",
            "Which expression is identical to \\( {0} \\)?",
            "Compute the square: \\( {0} \\):",
            "Determine the expansion of \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"{item[4]} - {item[6]}",
                f"{item[4]} + {item[5]} + {item[6]}",
                f"{item[4]} - {item[5]} - {item[6]}"
            ],
            f"**Step 1: Identify terms \\( a \\) and \\( b \\).**\n\\( a = {item[2]} \\) and \\( b = {item[3]} \\).\n\n**Step 2: Expand using \\( a^2 - 2ab + b^2 \\).**\n\\[ ({item[2]})^2 - 2({item[2]})({item[3]}) + ({item[3]})^2 \\]\n\n**Step 3: Simplify each term.**\n\\( {item[4]} - {item[5]} + {item[6]} = {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Numerical evaluation using (100 - k)^2 or (1000 - k)^2
    arch2 = {
        'data': [
            (99, 100, 1, "100^2 - 2(100)(1) + 1^2", 9801),
            (98, 100, 2, "100^2 - 2(100)(2) + 2^2", 9604),
            (97, 100, 3, "100^2 - 2(100)(3) + 3^2", 9409),
            (96, 100, 4, "100^2 - 2(100)(4) + 4^2", 9216),
            (95, 100, 5, "100^2 - 2(100)(5) + 5^2", 9025),
            (94, 100, 6, "100^2 - 2(100)(6) + 6^2", 8836),
            (93, 100, 7, "100^2 - 2(100)(7) + 7^2", 8649),
            (92, 100, 8, "100^2 - 2(100)(8) + 8^2", 8464),
            (995, 1000, 5, "1000^2 - 2(1000)(5) + 5^2", 990025),
            (498, 500, 2, "500^2 - 2(500)(2) + 2^2", 248004)
        ],
        'tmpls': [
            "Evaluate without direct multiplication: \\( {0}^2 \\).",
            "Using Identity II, calculate the value of \\( {0}^2 \\):",
            "Compute \\( {0}^2 \\) using \\( (a - b)^2 = a^2 - 2ab + b^2 \\):",
            "What is the numerical value of \\( {0}^2 \\)?",
            "Evaluate \\( {0}^2 \\) by expressing it as \\( ({1} - {2})^2 \\):",
            "Calculate \\( {0}^2 \\) algebraically:",
            "Find the square \\( {0}^2 \\) using the standard identity:",
            "Determine the exact value of \\( {0}^2 \\):",
            "The value of \\( {0}^2 \\) obtained via algebraic identity is:",
            "Solve for \\( {0}^2 \\) using Identity II:"
        ],
        'calc': lambda item: (
            str(item[4]),
            [
                str(item[4] + 20),
                str(item[4] - 100),
                str(item[4] + 200)
            ],
            f"**Step 1: Express the number as a difference of convenient bases.**\n\\[ {item[0]} = {item[1]} - {item[2]} \\]\n\n**Step 2: Apply the identity \\( (a - b)^2 = a^2 - 2ab + b^2 \\).**\n\\[ ({item[1]} - {item[2]})^2 = {item[3]} \\]\n\\[ = {item[1]**2} - {2*item[1]*item[2]} + {item[2]**2} \\]\n\n**Step 3: Calculate the final sum.**\n\\( = {item[4]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 3: Reciprocal form: (x - 1/x)^2
    arch3 = {
        'data': [
            ("(x - \\frac{1}{x})^2", "x^2 - 2 + \\frac{1}{x^2}", 2),
            ("(2x - \\frac{1}{2x})^2", "4x^2 - 2 + \\frac{1}{4x^2}", 2),
            ("(3x - \\frac{1}{3x})^2", "9x^2 - 2 + \\frac{1}{9x^2}", 2),
            ("(x - \\frac{2}{x})^2", "x^2 - 4 + \\frac{4}{x^2}", 4),
            ("(2x - \\frac{1}{x})^2", "4x^2 - 4 + \\frac{1}{x^2}", 4),
            ("(x - \\frac{3}{x})^2", "x^2 - 6 + \\frac{9}{x^2}", 6),
            ("(3x - \\frac{1}{x})^2", "9x^2 - 6 + \\frac{1}{x^2}", 6),
            ("(4x - \\frac{1}{2x})^2", "16x^2 - 4 + \\frac{1}{4x^2}", 4),
            ("(x - \\frac{1}{2x})^2", "x^2 - 1 + \\frac{1}{4x^2}", 1),
            ("(5x - \\frac{1}{5x})^2", "25x^2 - 2 + \\frac{1}{25x^2}", 2)
        ],
        'tmpls': [
            "Expand: \\( {0} \\).",
            "What is the expansion of the reciprocal expression \\( {0} \\)?",
            "Calculate \\( {0} \\) using Identity II:",
            "The simplified form of \\( {0} \\) is:",
            "Find the result of expanding \\( {0} \\):",
            "Apply \\( (a - b)^2 \\) to expand: \\( {0} \\):",
            "Simplify completely: \\( {0} \\):",
            "Evaluate \\( {0} \\):",
            "Which expression represents \\( {0} \\)?",
            "Determine the expanded polynomial for \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("- 2 +", "+ 2 +") if "- 2 +" in item[1] else item[1].replace("- 4 +", "+ 4 +"),
                item[1].replace("- 2 +", "-") if "- 2 +" in item[1] else item[1].replace("- 4 +", "-"),
                item[1] + " - 1"
            ],
            f"**Step 1: Identify \\( a \\) and \\( b \\).**\nLet the first term be \\( a \\) and second term be \\( b \\).\n\n**Step 2: Apply \\( (a - b)^2 = a^2 - 2ab + b^2 \\).**\nNotice the cross term \\( 2ab = {item[2]} \\) because \\( x \\) cancels.\n\n**Step 3: State the final simplified form.**\nThe expanded expression is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Value finding: Given x - 1/x = k, find x^2 + 1/x^2
    arch4 = {
        'data': [
            (3, 11, "3^2 + 2 = 9 + 2 = 11"),
            (4, 18, "4^2 + 2 = 16 + 2 = 18"),
            (5, 27, "5^2 + 2 = 25 + 2 = 27"),
            (6, 38, "6^2 + 2 = 36 + 2 = 38"),
            (7, 51, "7^2 + 2 = 49 + 2 = 51"),
            (8, 66, "8^2 + 2 = 64 + 2 = 66"),
            (9, 83, "9^2 + 2 = 81 + 2 = 83"),
            (10, 102, "10^2 + 2 = 100 + 2 = 102"),
            (2, 6, "2^2 + 2 = 4 + 2 = 6"),
            (1, 3, "1^2 + 2 = 1 + 2 = 3")
        ],
        'tmpls': [
            "If \\( x - \\frac{{1}}{{x}} = {0} \\), find the value of \\( x^2 + \\frac{{1}}{{x^2}} \\).",
            "Given that \\( x - \\frac{{1}}{{x}} = {0} \\), what is \\( x^2 + \\frac{{1}}{{x^2}} \\)?",
            "Calculate \\( x^2 + \\frac{{1}}{{x^2}} \\) when \\( x - \\frac{{1}}{{x}} = {0} \\):",
            "Determine the value of \\( x^2 + \\frac{{1}}{{x^2}} \\) if \\( x - \\frac{{1}}{{x}} = {0} \\):",
            "If \\( x - \\frac{{1}}{{x}} = {0} \\), evaluate \\( x^2 + \\frac{{1}}{{x^2}} \\):",
            "Find \\( x^2 + \\frac{{1}}{{x^2}} \\) given \\( x - \\frac{{1}}{{x}} = {0} \\):",
            "The value of \\( x^2 + \\frac{{1}}{{x^2}} \\) for \\( x - \\frac{{1}}{{x}} = {0} \\) is:",
            "What does \\( x^2 + \\frac{{1}}{{x^2}} \\) equal if \\( x - \\frac{{1}}{{x}} = {0} \\)?",
            "Solve for \\( x^2 + \\frac{{1}}{{x^2}} \\) knowing \\( x - \\frac{{1}}{{x}} = {0} \\):",
            "Compute \\( x^2 + \\frac{{1}}{{x^2}} \\) when \\( x - \\frac{{1}}{{x}} = {0} \\):"
        ],
        'calc': lambda item: (
            str(item[1]),
            [
                str(item[0]**2),
                str(item[1] - 4),
                str(item[1] + 2)
            ],
            f"**Step 1: Square both sides of the given equation.**\n\\[ \\left(x - \\frac{{1}}{{x}}\\right)^2 = {item[0]}^2 = {item[0]**2} \\]\n\n**Step 2: Expand using Identity II.**\n\\[ x^2 - 2 + \\frac{{1}}{{x^2}} = {item[0]**2} \\]\n\n**Step 3: Add 2 to isolate \\( x^2 + \\frac{{1}}{{x^2}} \\).**\n\\[ x^2 + \\frac{{1}}{{x^2}} = {item[0]**2} + 2 = {item[1]} \\]."
        ),
        'diff': 'medium'
    }

    # Arch 5: Connecting (a + b)^2 and (a - b)^2: (a + b)^2 - (a - b)^2 = 4ab
    arch5 = {
        'data': [
            ("(a + b)^2 - (a - b)^2", "4ab", ["2(a^2 + b^2)", "2ab", "a^2 - b^2"]),
            ("(a + b)^2 + (a - b)^2", "2(a^2 + b^2)", ["4ab", "2ab", "a^2 + b^2"]),
            ("If a + b = 9 and a - b = 5, find 4ab.", "56", "9^2 - 5^2 = 81 - 25 = 56", ["45", "40", "64"]),
            ("If a + b = 7 and a - b = 3, what is the value of ab?", "10", "4ab = 7^2 - 3^2 = 40 => ab = 10", ["21", "20", "5"]),
            ("If a + b = 8 and a - b = 2, find a^2 + b^2.", "34", "2(a^2 + b^2) = 8^2 + 2^2 = 68 => a^2 + b^2 = 34", ["32", "30", "36"]),
            ("If a - b = 4 and ab = 12, find (a + b)^2.", "64", "(a + b)^2 = (a - b)^2 + 4ab = 16 + 48 = 64", ["52", "48", "36"]),
            ("If a - b = 6 and ab = 7, find a + b (positive root).", "8", "(a + b)^2 = 36 + 28 = 64 => a + b = 8", ["6", "10", "12"]),
            ("If a + b = 10 and ab = 21, what is (a - b)^2?", "16", "(a - b)^2 = (a + b)^2 - 4ab = 100 - 84 = 16", ["4", "25", "9"]),
            ("If a + b = 6 and ab = 5, what is |a - b|?", "4", "(a - b)^2 = 36 - 20 = 16 => |a - b| = 4", ["2", "1", "6"]),
            ("What is the simplified form of (x + y)^2 - 4xy?", "(x - y)^2", ["(x + y)^2", "x^2 + y^2", "x^2 - y^2"])
        ],
        'tmpls': [
            "{0}",
            "Evaluate the algebraic relation: {0}",
            "Solve using the identity connection between (a + b)² and (a - b)²: {0}",
            "Determine the result: {0}",
            "Calculate: {0}",
            "Find the required value: {0}",
            "Which option is correct for: {0}",
            "Compute: {0}",
            "What is the value? {0}",
            "Apply algebraic identities: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2] if isinstance(item[2], list) else item[3],
            f"**Step 1: Recall the fundamental relation.**\n\\[ (a + b)^2 - (a - b)^2 = 4ab \\quad \\text{{and}} \\quad (a + b)^2 + (a - b)^2 = 2(a^2 + b^2) \\]\n\n**Step 2: Substitute known quantities.**\nSolve for the unknown.\n\n**Step 3: State the final result.**\nThe value is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Mixed expansions and simplification of (ax - b)^2
    arch6 = {
        'data': [
            ("Simplify: (2x - 1)^2 - (2x + 1)^2", "-8x", ["8x", "-4x", "4x"]),
            ("Simplify: (x - 3)^2 + (x + 3)^2", "2x^2 + 18", ["2x^2", "2x^2 - 18", "4x^2 + 18"]),
            ("Simplify: (3x - 2y)^2 + 12xy", "9x^2 + 4y^2", ["9x^2 + 24xy + 4y^2", "9x^2 - 4y^2", "9x^2 + 12xy + 4y^2"]),
            ("Simplify: (a - 2b)^2 - (a + 2b)^2", "-8ab", ["8ab", "-4ab", "4ab"]),
            ("Simplify: (5x - y)^2 + 10xy", "25x^2 + y^2", ["25x^2 - y^2", "25x^2 + 20xy + y^2", "5x^2 + y^2"]),
            ("Simplify: (x - 4)^2 - (x - 2)^2", "-4x + 12", ["4x - 12", "-4x - 12", "-2x + 12"]),
            ("If (x - k)^2 = x^2 - 16x + 64, what is k?", "8", ["-8", "16", "4"]),
            ("If 4x^2 - 28x + c is a perfect square, what is c?", "49", ["28", "14", "7"]),
            ("If 9x^2 - kx + 25 is a perfect square (3x - 5)^2, what is k?", "30", ["15", "60", "25"]),
            ("If 16x^2 - 40xy + 25y^2 is factored, the result is:", "(4x - 5y)^2", ["(4x + 5y)^2", "(4x - 5y)(4x + 5y)", "(2x - 5y)^2"])
        ],
        'tmpls': [
            "{0}",
            "Perform the algebraic operation: {0}",
            "Simplify the expression using Identity II: {0}",
            "Evaluate: {0}",
            "Find the simplified polynomial: {0}",
            "Calculate: {0}",
            "Determine the result of: {0}",
            "What does this simplify to: {0}?",
            "Solve: {0}",
            "Which option represents: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Expand each term using Identity II and Identity I.**\nExpand the squares individually.\n\n**Step 2: Combine like terms and cancel cross terms.**\nSimplify the resulting expression.\n\n**Step 3: State the final expression.**\nThe result is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Real-world / word problems involving Identity II
    arch7 = {
        'data': [
            ("A square lawn of side x meters has a border of 2 meters removed all around. The new area is:", "(x - 4)^2 = x^2 - 8x + 16 m^2", ["x^2 - 4 m^2", "x^2 - 4x + 16 m^2", "x^2 - 16 m^2"]),
            ("A square piece of paper of side 20 cm has a strip of width x removed from all 4 sides. The remaining area is:", "(20 - 2x)^2 = 400 - 80x + 4x^2 cm^2", ["400 - 4x^2 cm^2", "400 - 40x + 4x^2 cm^2", "20 - 4x cm^2"]),
            ("If the side of a square is reduced by 5 units, its new area is given by:", "x^2 - 10x + 25", ["x^2 - 25", "x^2 - 5x + 25", "x^2 + 10x + 25"]),
            ("A square tile of side (3x - 4) cm has an area of:", "9x^2 - 24x + 16 cm^2", ["9x^2 - 16 cm^2", "9x^2 - 12x + 16 cm^2", "6x^2 - 24x + 16 cm^2"]),
            ("A square water tank has base side (x - 3) meters. What is the area of its base?", "x^2 - 6x + 9 m^2", ["x^2 - 9 m^2", "x^2 - 3x + 9 m^2", "x^2 + 6x + 9 m^2"]),
            ("The side of a square park is (5a - 2b) meters. Its surface area is:", "25a^2 - 20ab + 4b^2 m^2", ["25a^2 - 4b^2 m^2", "25a^2 - 10ab + 4b^2 m^2", "20a^2 - 20ab + 4b^2 m^2"]),
            ("A square courtyard of side 50 m is surrounded by a path inside of width 3 m. The inner courtyard area is:", "(50 - 6)^2 = 44^2 = 1936 m^2", ["2500 m^2", "2209 m^2", "1849 m^2"]),
            ("A square sheet of metal of side (4x - 1) cm has area:", "16x^2 - 8x + 1 cm^2", ["16x^2 - 1 cm^2", "16x^2 + 8x + 1 cm^2", "8x - 2 cm^2"]),
            ("If the side length of a square decreases from x to (x - 7), the decrease in area is:", "14x - 49", ["49", "7x - 49", "14x + 49"]),
            ("In geometric dissection of (a - b)², the area is obtained by subtracting from a²:", "two rectangles of area ab and adding back b²", ["two squares of area b²", "one rectangle of area 2ab", "a rectangle of area ab"])
        ],
        'tmpls': [
            "{0}",
            "Solve the practical problem using Identity II: {0}",
            "Geometric application of Identity II: {0}",
            "Calculate the required area: {0}",
            "Determine the polynomial: {0}",
            "Find the correct area formula: {0}",
            "Which option represents: {0}",
            "What is the mathematical solution to: {0}",
            "Evaluate: {0}",
            "Compute the resulting area: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Determine the side length of the modified square.**\nIdentify the base side and reduction.\n\n**Step 2: Apply Identity II \\( (a - b)^2 = a^2 - 2ab + b^2 \\).**\nExpand the square of the binomial.\n\n**Step 3: State the final area expression.**\nThe area is {item[1]}."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 4.1.3: Identity III: (a + b)(a - b) = a² - b²
# ==============================================================================
def gen_4_1_3():
    tc = "CBSE-9-MGM-4-4.1.3"
    tname = "Identity III: (a + b)(a - b) = a² - b²"

    # Arch 0: Basic expansion (x + k)(x - k)
    arch0 = {
        'data': [
            ("(x + 3)(x - 3)", "x^2 - 9", 3, 9),
            ("(x + 4)(x - 4)", "x^2 - 16", 4, 16),
            ("(x + 5)(x - 5)", "x^2 - 25", 5, 25),
            ("(x + 6)(x - 6)", "x^2 - 36", 6, 36),
            ("(x + 7)(x - 7)", "x^2 - 49", 7, 49),
            ("(x + 8)(x - 8)", "x^2 - 64", 8, 64),
            ("(x + 9)(x - 9)", "x^2 - 81", 9, 81),
            ("(x + 10)(x - 10)", "x^2 - 100", 10, 100),
            ("(y + 2)(y - 2)", "y^2 - 4", 2, 4),
            ("(z + 12)(z - 12)", "z^2 - 144", 12, 144)
        ],
        'tmpls': [
            "Find the product using Identity III: \\( {0} \\).",
            "What is the expansion of \\( {0} \\)?",
            "Apply \\( (a + b)(a - b) = a^2 - b^2 \\) to \\( {0} \\):",
            "The product \\( {0} \\) simplifies to:",
            "Simplify: \\( {0} \\):",
            "Calculate \\( {0} \\):",
            "Find the polynomial resulting from \\( {0} \\):",
            "Evaluate \\( {0} \\):",
            "Which of the following is equal to \\( {0} \\)?",
            "Determine the result of multiplying: \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("-", "+"),
                f"x^2 - {item[2]}",
                f"x^2 - {item[3]}x"
            ],
            f"**Step 1: Identify terms \\( a \\) and \\( b \\).**\n\\( a = x \\) and \\( b = {item[2]} \\).\n\n**Step 2: Apply Identity III \\( (a + b)(a - b) = a^2 - b^2 \\).**\n\\[ (x + {item[2]})(x - {item[2]}) = x^2 - ({item[2]})^2 \\]\n\n**Step 3: State the final simplified form.**\nThe product is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Expansions with coefficients (ax + by)(ax - by)
    arch1 = {
        'data': [
            ("(2x + 3y)(2x - 3y)", "4x^2 - 9y^2", "2x", "3y", "4x^2", "9y^2"),
            ("(3x + 2y)(3x - 2y)", "9x^2 - 4y^2", "3x", "2y", "9x^2", "4y^2"),
            ("(2x + 5y)(2x - 5y)", "4x^2 - 25y^2", "2x", "5y", "4x^2", "25y^2"),
            ("(3x + 4y)(3x - 4y)", "9x^2 - 16y^2", "3x", "4y", "9x^2", "16y^2"),
            ("(4x + 3y)(4x - 3y)", "16x^2 - 9y^2", "4x", "3y", "16x^2", "9y^2"),
            ("(5x + 2y)(5x - 2y)", "25x^2 - 4y^2", "5x", "2y", "25x^2", "4y^2"),
            ("(3x + 5)(3x - 5)", "9x^2 - 25", "3x", "5", "9x^2", "25"),
            ("(2a + 7b)(2a - 7b)", "4a^2 - 49b^2", "2a", "7b", "4a^2", "49b^2"),
            ("(4x + 5y)(4x - 5y)", "16x^2 - 25y^2", "4x", "5y", "16x^2", "25y^2"),
            ("(7x + y)(7x - y)", "49x^2 - y^2", "7x", "y", "49x^2", "y^2")
        ],
        'tmpls': [
            "Expand using algebraic identities: \\( {0} \\).",
            "What is the expansion of \\( {0} \\)?",
            "Calculate \\( {0} \\) by applying Identity III:",
            "The simplified product of \\( {0} \\) is:",
            "Apply \\( (a + b)(a - b) \\) to find: \\( {0} \\):",
            "Expand: \\( {0} \\):",
            "Find the product: \\( {0} \\):",
            "Which expression is identical to \\( {0} \\)?",
            "Compute the product: \\( {0} \\):",
            "Determine the result of \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("-", "+"),
                f"{item[4]} - {item[3]}",
                f"{item[2]}^2 - {item[3]}^2"
            ],
            f"**Step 1: Identify terms \\( a \\) and \\( b \\).**\n\\( a = {item[2]} \\) and \\( b = {item[3]} \\).\n\n**Step 2: Apply \\( a^2 - b^2 \\).**\n\\[ ({item[2]})^2 - ({item[3]})^2 \\]\n\n**Step 3: Simplify each square.**\n\\( {item[4]} - {item[5]} = {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Numerical evaluation without direct multiplication (100 + k)(100 - k)
    arch2 = {
        'data': [
            (103, 97, 100, 3, 9991),
            (105, 95, 100, 5, 9975),
            (104, 96, 100, 4, 9984),
            (106, 94, 100, 6, 9964),
            (107, 93, 100, 7, 9951),
            (108, 92, 100, 8, 9936),
            (102, 98, 100, 2, 9996),
            (101, 99, 100, 1, 9999),
            (54, 46, 50, 4, 2484),
            (105, 95, 100, 5, 9975)
        ],
        'tmpls': [
            "Evaluate without direct multiplication: \\( {0} \\times {1} \\).",
            "Using Identity III, calculate \\( {0} \\times {1} \\):",
            "Compute \\( {0} \\times {1} \\) using \\( (a + b)(a - b) = a^2 - b^2 \\):",
            "What is the product \\( {0} \\times {1} \\)?",
            "Evaluate \\( {0} \\times {1} \\) by writing as \\( ({2} + {3})({2} - {3}) \\):",
            "Calculate \\( {0} \\times {1} \\) algebraically:",
            "Find the product \\( {0} \\times {1} \\) using the standard identity:",
            "Determine the exact value of \\( {0} \\times {1} \\):",
            "The value of \\( {0} \\times {1} \\) obtained via algebraic identity is:",
            "Solve for \\( {0} \\times {1} \\) using Identity III:"
        ],
        'calc': lambda item: (
            str(item[4]),
            [
                str(item[4] + 10),
                str(item[4] - 20),
                str(item[4] + 100)
            ],
            f"**Step 1: Express the factors symmetrically about a central round base.**\n\\[ {item[0]} = {item[2]} + {item[3]} \\quad \\text{{and}} \\quad {item[1]} = {item[2]} - {item[3]} \\]\n\n**Step 2: Apply Identity III \\( (a + b)(a - b) = a^2 - b^2 \\).**\n\\[ ({item[2]} + {item[3]})({item[2]} - {item[3]}) = {item[2]}^2 - {item[3]}^2 \\]\n\\[ = {item[2]**2} - {item[3]**2} \\]\n\n**Step 3: Subtract.**\n\\( = {item[4]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 3: Factorisation of difference of two squares
    arch3 = {
        'data': [
            ("x^2 - 16", "(x + 4)(x - 4)", "x", "4"),
            ("x^2 - 49", "(x + 7)(x - 7)", "x", "7"),
            ("4x^2 - 9y^2", "(2x + 3y)(2x - 3y)", "2x", "3y"),
            ("9x^2 - 16y^2", "(3x + 4y)(3x - 4y)", "3x", "4y"),
            ("25x^2 - 4", "(5x + 2)(5x - 2)", "5x", "2"),
            ("49x^2 - 36y^2", "(7x + 6y)(7x - 6y)", "7x", "6y"),
            ("16a^2 - 25b^2", "(4a + 5b)(4a - 5b)", "4a", "5b"),
            ("x^2 - \\frac{y^2}{100}", "(x + \\frac{y}{10})(x - \\frac{y}{10})", "x", "\\frac{y}{10}"),
            ("100 - 9x^2", "(10 + 3x)(10 - 3x)", "10", "3x"),
            ("64x^2 - 81y^2", "(8x + 9y)(8x - 9y)", "8x", "9y")
        ],
        'tmpls': [
            "Factorise using Identity III: \\( {0} \\).",
            "What are the factors of \\( {0} \\)?",
            "Factorise completely: \\( {0} \\):",
            "The factored form of \\( {0} \\) is:",
            "Apply \\( a^2 - b^2 = (a + b)(a - b) \\) to factorise: \\( {0} \\):",
            "Factorise the binomial: \\( {0} \\):",
            "Which of the following is the factorised form of \\( {0} \\)?",
            "Resolve into linear factors: \\( {0} \\):",
            "Express \\( {0} \\) as a product of two factors:",
            "Determine the factors of \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("-", "+"),
                item[1].replace("+", "-"),
                f"({item[2]} - {item[3]})^2"
            ],
            f"**Step 1: Express each term as a perfect square.**\n\\[ {item[0]} = ({item[2]})^2 - ({item[3]})^2 \\]\n\n**Step 2: Apply the difference of squares identity.**\n\\[ a^2 - b^2 = (a + b)(a - b) \\]\n\n**Step 3: State the factors.**\nThe factorised form is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 4: Continued products: (x - y)(x + y)(x^2 + y^2)...
    arch4 = {
        'data': [
            ("(x - 1)(x + 1)(x^2 + 1)", "x^4 - 1", "x^2 - 1", "x^4 - 1"),
            ("(x - 2)(x + 2)(x^2 + 4)", "x^4 - 16", "x^2 - 4", "x^4 - 16"),
            ("(x - 3)(x + 3)(x^2 + 9)", "x^4 - 81", "x^2 - 9", "x^4 - 81"),
            ("(x - y)(x + y)(x^2 + y^2)", "x^4 - y^4", "x^2 - y^2", "x^4 - y^4"),
            ("(2x - 1)(2x + 1)(4x^2 + 1)", "16x^4 - 1", "4x^2 - 1", "16x^4 - 1"),
            ("(x - y)(x + y)(x^2 + y^2)(x^4 + y^4)", "x^8 - y^8", "x^4 - y^4", "x^8 - y^8"),
            ("(x - 1)(x + 1)(x^2 + 1)(x^4 + 1)", "x^8 - 1", "x^4 - 1", "x^8 - 1"),
            ("(p - q)(p + q)(p^2 + q^2)", "p^4 - q^4", "p^2 - q^2", "p^4 - q^4"),
            ("(3x - 2)(3x + 2)(9x^2 + 4)", "81x^4 - 16", "9x^2 - 4", "81x^4 - 16"),
            ("(x - 2)(x + 2)(x^2 + 4)(x^4 + 16)", "x^8 - 256", "x^4 - 16", "x^8 - 256")
        ],
        'tmpls': [
            "Simplify the continued product: \\( {0} \\).",
            "What is the result of multiplying: \\( {0} \\)?",
            "Evaluate the repeated difference of squares product: \\( {0} \\):",
            "The simplified expression for \\( {0} \\) is:",
            "Find the product: \\( {0} \\):",
            "Simplify: \\( {0} \\):",
            "Compute \\( {0} \\) using Identity III successively:",
            "Which polynomial equals \\( {0} \\)?",
            "Determine the result of \\( {0} \\):",
            "Evaluate the expansion: \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("-", "+"),
                item[2],
                item[1] + " + 1"
            ],
            f"**Step 1: Multiply the first two factors using Identity III.**\n\\[ (a - b)(a + b) = a^2 - b^2 = {item[2]} \\]\n\n**Step 2: Multiply the result with the next factor.**\nNotice that the next factor is the sum of the same squares, allowing repeated application of Identity III.\n\n**Step 3: State the final simplified form.**\nThe product is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 5: Multi-step value finding: x^2 - 1/x^2 given x + 1/x and x - 1/x
    arch5 = {
        'data': [
            (5, 3, 15, "x + 1/x = 5, x - 1/x = 3 => (x + 1/x)(x - 1/x) = 5 * 3 = 15"),
            (6, 4, 24, "x + 1/x = 6, x - 1/x = 4 => 6 * 4 = 24"),
            (7, 5, 35, "x + 1/x = 7, x - 1/x = 5 => 7 * 5 = 35"),
            (8, 6, 48, "x + 1/x = 8, x - 1/x = 6 => 8 * 6 = 48"),
            (9, 7, 63, "x + 1/x = 9, x - 1/x = 7 => 9 * 7 = 63"),
            (10, 8, 80, "x + 1/x = 10, x - 1/x = 8 => 10 * 8 = 80"),
            (4, 2, 8, "x + 1/x = 4, x - 1/x = 2 => 4 * 2 = 8"),
            (7, 3, 21, "x + 1/x = 7, x - 1/x = 3 => 7 * 3 = 21"),
            (5, 1, 5, "x + 1/x = 5, x - 1/x = 1 => 5 * 1 = 5"),
            (8, 2, 16, "x + 1/x = 8, x - 1/x = 2 => 8 * 2 = 16")
        ],
        'tmpls': [
            "If \\( x + \\frac{{1}}{{x}} = {0} \\) and \\( x - \\frac{{1}}{{x}} = {1} \\), find \\( x^2 - \\frac{{1}}{{x^2}} \\).",
            "Given \\( x + \\frac{{1}}{{x}} = {0} \\) and \\( x - \\frac{{1}}{{x}} = {1} \\), what is \\( x^2 - \\frac{{1}}{{x^2}} \\)?",
            "Calculate \\( x^2 - \\frac{{1}}{{x^2}} \\) when \\( x + \\frac{{1}}{{x}} = {0} \\) and \\( x - \\frac{{1}}{{x}} = {1} \\):",
            "Determine the value of \\( x^2 - \\frac{{1}}{{x^2}} \\) if \\( x + \\frac{{1}}{{x}} = {0} \\) and \\( x - \\frac{{1}}{{x}} = {1} \\):",
            "Evaluate \\( x^2 - \\frac{{1}}{{x^2}} \\) given \\( x + \\frac{{1}}{{x}} = {0} \\) and \\( x - \\frac{{1}}{{x}} = {1} \\):",
            "Find the numerical value of \\( x^2 - \\frac{{1}}{{x^2}} \\):",
            "The value of \\( x^2 - \\frac{{1}}{{x^2}} \\) for \\( x + \\frac{{1}}{{x}} = {0} \\) and \\( x - \\frac{{1}}{{x}} = {1} \\) is:",
            "What is \\( x^2 - \\frac{{1}}{{x^2}} \\) if \\( x + \\frac{{1}}{{x}} = {0} \\) and \\( x - \\frac{{1}}{{x}} = {1} \\)?",
            "Compute \\( x^2 - \\frac{{1}}{{x^2}} \\):",
            "Solve for \\( x^2 - \\frac{{1}}{{x^2}} \\):"
        ],
        'calc': lambda item: (
            str(item[2]),
            [
                str(item[0]**2 - item[1]**2),
                str(item[0] + item[1]),
                str(item[2] + 4)
            ],
            f"**Step 1: Express \\( x^2 - \\frac{{1}}{{x^2}} \\) using Identity III.**\n\\[ x^2 - \\frac{{1}}{{x^2}} = \\left(x + \\frac{{1}}{{x}}\\right)\\left(x - \\frac{{1}}{{x}}\\right) \\]\n\n**Step 2: Substitute the given values.**\n\\[ = ({item[0]})({item[1]}) = {item[2]} \\]\n\n**Step 3: State the final evaluated value.**\nThe result is \\( {item[2]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 6: Numerical evaluation of a^2 - b^2 / (a - b) or a + b
    arch6 = {
        'data': [
            (153, 147, 6, 300, 1800),
            (185, 115, 70, 300, 21000),
            (65, 35, 30, 100, 3000),
            (78, 22, 56, 100, 5600),
            (175, 25, 150, 200, 30000),
            (9.7, 0.3, 9.4, 10.0, 94),
            (0.54, 0.46, 0.08, 1.0, 0.08),
            (1.05, 0.95, 0.10, 2.0, 0.20),
            (256, 144, 112, 400, 44800),
            (325, 175, 150, 500, 75000)
        ],
        'tmpls': [
            "Evaluate without direct squaring: \\( {0}^2 - {1}^2 \\).",
            "Using Identity III, calculate \\( {0}^2 - {1}^2 \\):",
            "Compute \\( {0}^2 - {1}^2 \\) by factorising: \\( ({0} + {1})({0} - {1}) \\):",
            "What is the value of \\( {0}^2 - {1}^2 \\)?",
            "Calculate \\( {0}^2 - {1}^2 \\) algebraically:",
            "Find the numerical value of \\( {0}^2 - {1}^2 \\):",
            "The exact value of \\( {0}^2 - {1}^2 \\) is:",
            "Determine \\( {0}^2 - {1}^2 \\) using the difference of squares identity:",
            "Solve for \\( {0}^2 - {1}^2 \\):",
            "Evaluate the difference of squares: \\( {0}^2 - {1}^2 \\):"
        ],
        'calc': lambda item: (
            str(item[4]),
            [
                str(item[4] + 10) if isinstance(item[4], int) else str(round(item[4] + 0.1, 2)),
                str(item[4] - 20) if isinstance(item[4], int) else str(round(item[4] - 0.02, 2)),
                str(item[3])
            ],
            f"**Step 1: Apply Identity III \\( a^2 - b^2 = (a + b)(a - b) \\).**\n\\[ {item[0]}^2 - {item[1]}^2 = ({item[0]} + {item[1]})({item[0]} - {item[1]}) \\]\n\n**Step 2: Calculate the sum and difference separately.**\n\\[ \\text{{Sum}} = {item[3]}, \\quad \\text{{Difference}} = {item[2]} \\]\n\n**Step 3: Multiply the results.**\n\\[ {item[3]} \\times {item[2]} = {item[4]} \\]."
        ),
        'diff': 'easy'
    }

    # Arch 7: Algebraic geometry / Word applications of (a + b)(a - b)
    arch7 = {
        'data': [
            ("A rectangle has length (x + 6) meters and breadth (x - 6) meters. Its area is:", "x^2 - 36 m^2", ["x^2 + 36 m^2", "x^2 - 12 m^2", "2x m^2"]),
            ("A rectangular carpet has dimensions (2x + 5) m and (2x - 5) m. What is its area?", "4x^2 - 25 m^2", ["4x^2 + 25 m^2", "4x^2 - 10 m^2", "2x^2 - 25 m^2"]),
            ("From a square sheet of metal of side a, a smaller square of side b is cut out. The remaining area is equal to:", "a^2 - b^2 = (a + b)(a - b)", ["(a - b)^2", "a^2 + b^2", "2ab"]),
            ("A circular ring (annulus) has outer radius R and inner radius r. The area between them is:", "π(R + r)(R - r)", ["π(R - r)^2", "2π(R - r)", "π(R^2 + r^2)"]),
            ("A square of side 25 cm has a square of side 15 cm cut out from its center. The remaining area is:", "(25 + 15)(25 - 15) = 40 * 10 = 400 cm^2", ["300 cm^2", "500 cm^2", "200 cm^2"]),
            ("A rectangular garden has length (3x + 4) meters and width (3x - 4) meters. Its area is:", "9x^2 - 16 m^2", ["9x^2 + 16 m^2", "9x^2 - 8 m^2", "6x^2 - 16 m^2"]),
            ("If a rectangle of area (x^2 - 49) has length (x + 7), what is its breadth?", "x - 7", ["x + 7", "x - 14", "7"]),
            ("The area of a rectangular field is (16x^2 - 9y^2). If its width is (4x - 3y), its length is:", "4x + 3y", ["4x - 3y", "8x + 6y", "16x + 9y"]),
            ("A path of width b is cut around a square plot of side a. The area reduction is represented by:", "(a + b)(a - b) = a^2 - b^2", ["(a + b)^2", "a^2 + b^2", "ab"]),
            ("In geometric dissection of a^2 - b^2, the remaining L-shaped region can be cut and rearranged into:", "a single rectangle of length (a + b) and breadth (a - b)", ["two identical triangles", "a square of side (a - b)", "a trapezoid"])
        ],
        'tmpls': [
            "{0}",
            "Solve the geometric problem using Identity III: {0}",
            "Application of the difference of squares: {0}",
            "Calculate the required area: {0}",
            "Determine the polynomial: {0}",
            "Find the correct area formula: {0}",
            "Which option represents: {0}",
            "What is the mathematical solution to: {0}",
            "Evaluate: {0}",
            "Compute the resulting area: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify dimensions and application of Identity III.**\nHere area is given by the product of conjugate dimensions \\( (a + b)(a - b) \\).\n\n**Step 2: Apply the identity \\( (a + b)(a - b) = a^2 - b^2 \\).**\nExpand or factorise as required.\n\n**Step 3: State the final result.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_4_1_1()
    q2 = gen_4_1_2()
    q3 = gen_4_1_3()
    print(f"gen_4_1_1: {len(q1)} questions")
    print(f"gen_4_1_2: {len(q2)} questions")
    print(f"gen_4_1_3: {len(q3)} questions")
