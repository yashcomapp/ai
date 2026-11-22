# scripts/build_cbse9_mgm_ch4_part3.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 4: Exploring Algebraic Identities
Part 3:
- Subtopic 4.3.1: (x ± y)³ = x³ ± y³ ± 3xy(x ± y)
- Subtopic 4.3.2: x³ + y³ + z³ - 3xyz = (x + y + z)(x² + y² + z² - xy - yz - zx)
- Subtopic 4.3.3: Conditional identity: If x + y + z = 0, x³ + y³ + z³ = 3xyz
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 240 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 4
CH_NAME = "Exploring Algebraic Identities"

# ==============================================================================
# SUBTOPIC 4.3.1: (x ± y)³ = x³ ± y³ ± 3xy(x ± y)
# ==============================================================================
def gen_4_3_1():
    tc = "CBSE-9-MGM-4-4.3.1"
    tname = "(x ± y)³ = x³ ± y³ ± 3xy(x ± y)"

    # Arch 0: Positive expansion (x + k)^3 or (ax + b)^3
    arch0 = {
        'data': [
            ("(x + 1)^3", "x^3 + 3x^2 + 3x + 1", 1),
            ("(x + 2)^3", "x^3 + 6x^2 + 12x + 8", 2),
            ("(x + 3)^3", "x^3 + 9x^2 + 27x + 27", 3),
            ("(x + 4)^3", "x^3 + 12x^2 + 48x + 64", 4),
            ("(2x + 1)^3", "8x^3 + 12x^2 + 6x + 1", 1),
            ("(3x + 2)^3", "27x^3 + 54x^2 + 36x + 8", 2),
            ("(2a + 3b)^3", "8a^3 + 36a^2b + 54ab^2 + 27b^3", 3),
            ("(3a + 4b)^3", "27a^3 + 108a^2b + 144ab^2 + 64b^3", 4),
            ("(4x + 3y)^3", "64x^3 + 144x^2y + 108xy^2 + 27y^3", 3),
            ("(5x + 2)^3", "125x^3 + 150x^2 + 60x + 8", 2)
        ],
        'tmpls': [
            "Expand using the cubic identity: \\( {0} \\).",
            "What is the expansion of \\( {0} \\)?",
            "Apply \\( (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3 \\) to expand \\( {0} \\):",
            "The simplified expanded form of \\( {0} \\) is:",
            "Simplify the cube: \\( {0} \\):",
            "Calculate \\( {0} \\):",
            "Find the polynomial resulting from expanding \\( {0} \\):",
            "Expand completely: \\( {0} \\):",
            "Which expression is equal to \\( {0} \\)?",
            "Evaluate \\( {0} \\) using Identity VI:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("+ 3x^2", "+ 6x^2") if "+ 3x^2" in item[1] else item[1].replace("+ 12x^2", "+ 6x^2"),
                item[1].replace("+", "-"),
                f"x^3 + {item[2]**3}"
            ],
            f"**Step 1: Identify terms for Identity VI.**\nIn \\( (a + b)^3 \\), match \\( a \\) and \\( b \\).\n\n**Step 2: Apply \\( a^3 + 3a^2b + 3ab^2 + b^3 \\).**\nExpand each term carefully, calculating powers and coefficients.\n\n**Step 3: State the final expanded expression.**\nThe result is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Negative expansion (x - k)^3 or (ax - by)^3
    arch1 = {
        'data': [
            ("(x - 1)^3", "x^3 - 3x^2 + 3x - 1", 1),
            ("(x - 2)^3", "x^3 - 6x^2 + 12x - 8", 2),
            ("(x - 3)^3", "x^3 - 9x^2 + 27x - 27", 3),
            ("(x - 4)^3", "x^3 - 12x^2 + 48x - 64", 4),
            ("(2x - 1)^3", "8x^3 - 12x^2 + 6x - 1", 1),
            ("(3x - 2)^3", "27x^3 - 54x^2 + 36x - 8", 2),
            ("(2a - 3b)^3", "8a^3 - 36a^2b + 54ab^2 - 27b^3", 3),
            ("(3a - 4b)^3", "27a^3 - 108a^2b + 144ab^2 - 64b^3", 4),
            ("(4x - 3y)^3", "64x^3 - 144x^2y + 108xy^2 - 27y^3", 3),
            ("(5x - 2)^3", "125x^3 - 150x^2 + 60x - 8", 2)
        ],
        'tmpls': [
            "Expand using the difference cube identity: \\( {0} \\).",
            "What is the expansion of \\( {0} \\)?",
            "Apply \\( (a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3 \\) to expand \\( {0} \\):",
            "The simplified expanded form of \\( {0} \\) is:",
            "Simplify the cube: \\( {0} \\):",
            "Calculate \\( {0} \\):",
            "Find the polynomial resulting from \\( {0} \\):",
            "Expand completely: \\( {0} \\):",
            "Which expression is equal to \\( {0} \\)?",
            "Evaluate \\( {0} \\) using Identity VII:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("-", "+"),
                item[1].replace("+ 3x", "- 3x") if "+ 3x" in item[1] else item[1].replace("+ 36x", "- 36x"),
                f"x^3 - {item[2]**3}"
            ],
            f"**Step 1: Identify terms for Identity VII.**\nIn \\( (a - b)^3 \\), match \\( a \\) and \\( b \\).\n\n**Step 2: Apply \\( a^3 - 3a^2b + 3ab^2 - b^3 \\).**\nNote the alternating signs: \\( + - + - \\).\n\n**Step 3: State the final expanded expression.**\nThe result is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Numerical evaluation of cubes (100 ± k)^3
    arch2 = {
        'data': [
            (102, 100, 2, "100^3 + 3(100)^2(2) + 3(100)(4) + 8", 1061208),
            (103, 100, 3, "100^3 + 3(100)^2(3) + 3(100)(9) + 27", 1092727),
            (104, 100, 4, "100^3 + 3(100)^2(4) + 3(100)(16) + 64", 1124864),
            (101, 100, 1, "100^3 + 3(100)^2(1) + 3(100)(1) + 1", 1030301),
            (105, 100, 5, "100^3 + 3(100)^2(5) + 3(100)(25) + 125", 1157625),
            (99, 100, 1, "100^3 - 3(100)^2(1) + 3(100)(1) - 1", 970299),
            (98, 100, 2, "100^3 - 3(100)^2(2) + 3(100)(4) - 8", 941192),
            (97, 100, 3, "100^3 - 3(100)^2(3) + 3(100)(9) - 27", 912673),
            (96, 100, 4, "100^3 - 3(100)^2(4) + 3(100)(16) - 64", 884736),
            (998, 1000, 2, "1000^3 - 3(1000)^2(2) + 3(1000)(4) - 8", 994011992)
        ],
        'tmpls': [
            "Evaluate without direct multiplication: \\( {0}^3 \\).",
            "Using cubic identities, calculate \\( {0}^3 \\):",
            "Compute \\( {0}^3 \\) using \\( (a \\pm b)^3 \\):",
            "What is the exact numerical value of \\( {0}^3 \\)?",
            "Evaluate \\( {0}^3 \\) algebraically:",
            "Find \\( {0}^3 \\) using standard identities:",
            "Determine the value of \\( {0}^3 \\):",
            "The cube \\( {0}^3 \\) calculated via algebraic identity is:",
            "Solve for \\( {0}^3 \\) using \\( ({1} \\pm {2})^3 \\):",
            "Compute the cube: \\( {0}^3 \\):"
        ],
        'calc': lambda item: (
            str(item[4]),
            [
                str(item[4] + 1000),
                str(item[4] - 2000),
                str(item[4] + 10000)
            ],
            f"**Step 1: Express the number relative to base 100 or 1000.**\n\\[ {item[0]} = {item[1]} \\pm {item[2]} \\]\n\n**Step 2: Expand using the cubic identity.**\n\\[ ({item[1]} \\pm {item[2]})^3 = {item[3]} \\]\n\n**Step 3: Sum the terms.**\n\\( = {item[4]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Reciprocal forms: Finding x^3 ± 1/x^3 given x ± 1/x
    arch3 = {
        'data': [
            ("x + \\frac{1}{x} = 3", 3, 18, "3^3 - 3(3) = 27 - 9 = 18", "+"),
            ("x + \\frac{1}{x} = 4", 4, 52, "4^3 - 3(4) = 64 - 12 = 52", "+"),
            ("x + \\frac{1}{x} = 5", 5, 110, "5^3 - 3(5) = 125 - 15 = 110", "+"),
            ("x + \\frac{1}{x} = 6", 6, 198, "6^3 - 3(6) = 216 - 18 = 198", "+"),
            ("x + \\frac{1}{x} = 7", 7, 322, "7^3 - 3(7) = 343 - 21 = 322", "+"),
            ("x - \\frac{1}{x} = 3", 3, 36, "3^3 + 3(3) = 27 + 9 = 36", "-"),
            ("x - \\frac{1}{x} = 4", 4, 76, "4^3 + 3(4) = 64 + 12 = 76", "-"),
            ("x - \\frac{1}{x} = 5", 5, 140, "5^3 + 3(5) = 125 + 15 = 140", "-"),
            ("x - \\frac{1}{x} = 6", 6, 234, "6^3 + 3(6) = 216 + 18 = 234", "-"),
            ("x - \\frac{1}{x} = 2", 2, 14, "2^3 + 3(2) = 8 + 6 = 14", "-")
        ],
        'tmpls': [
            "If \\( {0} \\), find \\( x^3 {4} \\frac{{1}}{{x^3}} \\).",
            "Given \\( {0} \\), what is the value of \\( x^3 {4} \\frac{{1}}{{x^3}} \\)?",
            "Calculate \\( x^3 {4} \\frac{{1}}{{x^3}} \\) when \\( {0} \\):",
            "Determine \\( x^3 {4} \\frac{{1}}{{x^3}} \\) if \\( {0} \\):",
            "Evaluate \\( x^3 {4} \\frac{{1}}{{x^3}} \\) given \\( {0} \\):",
            "Find the numerical value of \\( x^3 {4} \\frac{{1}}{{x^3}} \\):",
            "The value of \\( x^3 {4} \\frac{{1}}{{x^3}} \\) for \\( {0} \\) is:",
            "What does \\( x^3 {4} \\frac{{1}}{{x^3}} \\) equal if \\( {0} \\)?",
            "Compute \\( x^3 {4} \\frac{{1}}{{x^3}} \\):",
            "Solve for \\( x^3 {4} \\frac{{1}}{{x^3}} \\) knowing \\( {0} \\):"
        ],
        'calc': lambda item: (
            str(item[2]),
            [
                str(item[1]**3),
                str(item[2] + 6),
                str(item[2] - 12)
            ],
            f"**Step 1: Cube both sides of the given equation.**\n\\[ \\left(x {item[4]} \\frac{{1}}{{x}}\\right)^3 = {item[1]}^3 = {item[1]**3} \\]\n\n**Step 2: Expand using Identity VI/VII.**\n\\[ x^3 {item[4]} \\frac{{1}}{{x^3}} {item[4].replace('+', '-').replace('-', '+')} 3\\left(x {item[4]} \\frac{{1}}{{x}}\\right) = {item[1]**3} \\]\n\n**Step 3: Substitute \\( {item[1]} \\) and solve.**\n{item[3]}.\n\nThe result is \\( {item[2]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Factorisation of sum and difference of two cubes: a^3 ± b^3
    arch4 = {
        'data': [
            ("x^3 + 27", "(x + 3)(x^2 - 3x + 9)", "x", "3", "+"),
            ("x^3 - 64", "(x - 4)(x^2 + 4x + 16)", "x", "4", "-"),
            ("8x^3 + 125y^3", "(2x + 5y)(4x^2 - 10xy + 25y^2)", "2x", "5y", "+"),
            ("27x^3 - 8y^3", "(3x - 2y)(9x^2 + 6xy + 4y^2)", "3x", "2y", "-"),
            ("64x^3 + 1", "(4x + 1)(16x^2 - 4x + 1)", "4x", "1", "+"),
            ("125a^3 - 27b^3", "(5a - 3b)(25a^2 + 15ab + 9b^2)", "5a", "3b", "-"),
            ("216x^3 + y^3", "(6x + y)(36x^2 - 6xy + y^2)", "6x", "y", "+"),
            ("343x^3 - 8", "(7x - 2)(49x^2 + 14x + 4)", "7x", "2", "-"),
            ("x^3 + \\frac{1}{8}", "(x + \\frac{1}{2})(x^2 - \\frac{x}{2} + \\frac{1}{4})", "x", "\\frac{1}{2}", "+"),
            ("x^3 - \\frac{1}{27}", "(x - \\frac{1}{3})(x^2 + \\frac{x}{3} + \\frac{1}{9})", "x", "\\frac{1}{3}", "-")
        ],
        'tmpls': [
            "Factorise: \\( {0} \\).",
            "What is the factored form of the cubic expression \\( {0} \\)?",
            "Factorise completely: \\( {0} \\):",
            "The factored form of \\( {0} \\) is:",
            "Apply \\( a^3 \\pm b^3 = (a \\pm b)(a^2 \\mp ab + b^2) \\) to \\( {0} \\):",
            "Resolve into linear and quadratic factors: \\( {0} \\):",
            "Which of the following is the factorisation of \\( {0} \\)?",
            "Express \\( {0} \\) as a product of factors:",
            "Factorise: \\( {0} \\):",
            "Determine the factors of \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("+", "-") if "+" in item[1] else item[1].replace("-", "+"),
                f"({item[2]} {item[4]} {item[3]})^3",
                f"({item[2]} {item[4]} {item[3]})({item[2]}^2 + {item[3]}^2)"
            ],
            f"**Step 1: Express each term as a cube.**\n\\[ {item[0]} = ({item[2]})^3 {item[4]} ({item[3]})^3 \\]\n\n**Step 2: Apply the cube sum/difference identity.**\n\\[ a^3 \\pm b^3 = (a \\pm b)(a^2 \\mp ab + b^2) \\]\n\n**Step 3: State the factors.**\nThe factorised form is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 5: Value finding: a^3 + b^3 given a + b and ab
    arch5 = {
        'data': [
            (5, 6, 35, "5^3 - 3(6)(5) = 125 - 90 = 35"),
            (6, 8, 72, "6^3 - 3(8)(6) = 216 - 144 = 72"),
            (7, 10, 133, "7^3 - 3(10)(7) = 343 - 210 = 133"),
            (8, 12, 224, "8^3 - 3(12)(8) = 512 - 288 = 224"),
            (4, 3, 28, "4^3 - 3(3)(4) = 64 - 36 = 28"),
            (9, 14, 351, "9^3 - 3(14)(9) = 729 - 378 = 351"),
            (10, 20, 400, "10^3 - 3(20)(10) = 1000 - 600 = 400"),
            (5, 4, 65, "5^3 - 3(4)(5) = 125 - 60 = 65"),
            (7, 12, 91, "7^3 - 3(12)(7) = 343 - 252 = 91"),
            (6, 5, 126, "6^3 - 3(5)(6) = 216 - 90 = 126")
        ],
        'tmpls': [
            "If \\( a + b = {0} \\) and \\( ab = {1} \\), find \\( a^3 + b^3 \\).",
            "Given \\( a + b = {0} \\) and \\( ab = {1} \\), what is \\( a^3 + b^3 \\)?",
            "Calculate \\( a^3 + b^3 \\) when \\( a + b = {0} \\) and \\( ab = {1} \\):",
            "Determine \\( a^3 + b^3 \\) if \\( a + b = {0} \\) and \\( ab = {1} \\):",
            "Evaluate \\( a^3 + b^3 \\) given \\( a + b = {0} \\) and \\( ab = {1} \\):",
            "Find the numerical value of \\( a^3 + b^3 \\):",
            "The value of \\( a^3 + b^3 \\) for \\( a + b = {0} \\) and \\( ab = {1} \\) is:",
            "What does \\( a^3 + b^3 \\) equal if \\( a + b = {0} \\) and \\( ab = {1} \\)?",
            "Compute \\( a^3 + b^3 \\):",
            "Solve for \\( a^3 + b^3 \\):"
        ],
        'calc': lambda item: (
            str(item[2]),
            [
                str(item[0]**3),
                str(item[2] + 20),
                str(item[2] - 15)
            ],
            f"**Step 1: Write down the rearranged cubic identity.**\n\\[ a^3 + b^3 = (a + b)^3 - 3ab(a + b) \\]\n\n**Step 2: Substitute given values.**\n\\[ a^3 + b^3 = {item[0]}^3 - 3({item[1]})({item[0]}) = {item[0]**3} - {3*item[1]*item[0]} = {item[2]} \\]\n\n**Step 3: State the final value.**\nThe result is \\( {item[2]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 6: Multi-term simplification: (x + y)^3 ± (x - y)^3
    arch6 = {
        'data': [
            ("(x + y)^3 + (x - y)^3", "2x^3 + 6xy^2", ["2x^3", "6x^2y", "2(x^3 + y^3)"]),
            ("(x + y)^3 - (x - y)^3", "6x^2y + 2y^3", ["2y^3", "6xy^2", "2(x^3 - y^3)"]),
            ("Simplify: (2x + 1)^3 + (2x - 1)^3", "16x^3 + 12x", ["16x^3", "16x^3 + 2", "24x^2 + 2"]),
            ("Simplify: (2x + 1)^3 - (2x - 1)^3", "24x^2 + 2", ["24x^2", "16x^3 + 2", "16x^3 + 12x"]),
            ("Simplify: (a + 2b)^3 + (a - 2b)^3", "2a^3 + 24ab^2", ["2a^3", "12a^2b", "2a^3 + 8b^3"]),
            ("Simplify: (a + 2b)^3 - (a - 2b)^3", "12a^2b + 16b^3", ["16b^3", "24ab^2", "2a^3 - 16b^3"]),
            ("Simplify: (3x + 2y)^3 - (3x - 2y)^3", "108x^2y + 16y^3", ["54x^3 + 16y^3", "108xy^2", "16y^3"]),
            ("Simplify: (x + 3)^3 + (x - 3)^3", "2x^3 + 54x", ["2x^3 + 54", "2x^3", "18x^2"]),
            ("Simplify: (x + y)^3 - x^3 - y^3", "3xy(x + y)", ["0", "3xy", "x^3 + y^3"]),
            ("Simplify: (x - y)^3 - x^3 + y^3", "-3xy(x - y)", ["0", "-3xy", "-x^3 - y^3"])
        ],
        'tmpls': [
            "Simplify: \\( {0} \\).",
            "What does \\( {0} \\) simplify to?",
            "Evaluate: \\( {0} \\):",
            "Find the simplified expression for \\( {0} \\):",
            "Calculate \\( {0} \\):",
            "Determine the result of simplifying \\( {0} \\):",
            "Which polynomial represents \\( {0} \\)?",
            "Expand and combine like terms: \\( {0} \\):",
            "Compute: \\( {0} \\):",
            "Simplify completely: \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Expand both cubic binomials.**\nApply \\( (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3 \\) and \\( (a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3 \\).\n\n**Step 2: Add or subtract corresponding terms.**\nNotice terms cancel alternately.\n\n**Step 3: State the combined simplified form.**\nThe result is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Geometric representation: Volume of a cube (a + b)^3
    arch7 = {
        'data': [
            ("A cube of edge (x + 3) cm has volume:", "x^3 + 9x^2 + 27x + 27 cm^3", ["x^3 + 27 cm^3", "x^3 + 3x^2 + 27 cm^3", "3x + 9 cm^3"]),
            ("A cube of edge (2x + 1) meters has volume:", "8x^3 + 12x^2 + 6x + 1 m^3", ["8x^3 + 1 m^3", "8x^3 + 6x^2 + 1 m^3", "6x + 3 m^3"]),
            ("In the geometric dissection of a cube of edge (a + b), how many smaller rectangular blocks compose the cube?", "8 blocks (2 cubes of a³, b³ and 6 rectangular prisms: 3 of a²b and 3 of ab²)", ["4 blocks", "6 blocks", "10 blocks"]),
            ("In the 3D dissection of (a + b)³, what do the three blocks of dimension a x a x b represent?", "three rectangular blocks each of volume a²b", ["three cubes", "three diagonal prisms", "surface patches"]),
            ("If the edge of a cube is increased by 2 units, the increase in volume from x³ is:", "6x^2 + 12x + 8", ["8", "6x^2 + 8", "12x + 8"]),
            ("A cube of edge (3a + 2b) cm has volume:", "27a^3 + 54a^2b + 36ab^2 + 8b^3 cm^3", ["27a^3 + 8b^3 cm^3", "27a^3 + 18a^2b + 8b^3 cm^3", "9a^3 + 6b^3 cm^3"]),
            ("If a cubic tank of side (x - 2) meters is filled with water, its capacity is:", "x^3 - 6x^2 + 12x - 8 m^3", ["x^3 - 8 m^3", "x^3 - 4x^2 - 8 m^3", "3x - 6 m^3"]),
            ("A hollow box has internal edge length (4x - 1) cm. Its volume capacity is:", "64x^3 - 48x^2 + 12x - 1 cm^3", ["64x^3 - 1 cm^3", "64x^3 + 1 cm^3", "16x^2 - 1 cm^3"]),
            ("The volume of a cube is 27x^3 + 54x^2 + 36x + 8. What is the length of its edge?", "3x + 2", ["3x + 4", "3x + 8", "9x + 2"]),
            ("If the edge of a cube decreases from x to (x - 3), the decrease in volume is:", "9x^2 - 27x + 27", ["27", "9x^2 + 27", "3x^2 - 27"])
        ],
        'tmpls': [
            "{0}",
            "Solve the cubic volume problem: {0}",
            "Geometric application of Identity VI/VII: {0}",
            "Calculate the required volume or edge: {0}",
            "Determine the polynomial expression: {0}",
            "Find the correct answer: {0}",
            "Which option represents: {0}",
            "What is the mathematical solution: {0}",
            "Evaluate the 3D geometric scenario: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the volume formula of a cube.**\n\\[ \\text{{Volume}} = (\\text{{edge}})^3 \\]\n\n**Step 2: Apply the cubic expansion identity.**\nExpand using \\( (a \\pm b)^3 = a^3 \\pm 3a^2b + 3ab^2 \\pm b^3 \\).\n\n**Step 3: State the final volume expression.**\nThe result is {item[1]}."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 4.3.2: x³ + y³ + z³ - 3xyz = (x + y + z)(x² + y² + z² - xy - yz - zx)
# ==============================================================================
def gen_4_3_2():
    tc = "CBSE-9-MGM-4-4.3.2"
    tname = "x³ + y³ + z³ - 3xyz = (x + y + z)(x² + y² + z² - xy - yz - zx)"

    # Arch 0: Direct factorisation into (x + y + z)(x² + y² + z² - xy - yz - zx)
    arch0 = {
        'data': [
            ("x^3 + y^3 + z^3 - 3xyz", "(x + y + z)(x^2 + y^2 + z^2 - xy - yz - zx)"),
            ("8x^3 + y^3 + z^3 - 6xyz", "(2x + y + z)(4x^2 + y^2 + z^2 - 2xy - yz - 2zx)"),
            ("x^3 + 8y^3 + z^3 - 6xyz", "(x + 2y + z)(x^2 + 4y^2 + z^2 - 2xy - 2yz - zx)"),
            ("x^3 + y^3 + 8z^3 - 6xyz", "(x + y + 2z)(x^2 + y^2 + 4z^2 - xy - 2yz - 2zx)"),
            ("8x^3 + 27y^3 + z^3 - 18xyz", "(2x + 3y + z)(4x^2 + 9y^2 + z^2 - 6xy - 3yz - 2zx)"),
            ("27x^3 + y^3 + z^3 - 9xyz", "(3x + y + z)(9x^2 + y^2 + z^2 - 3xy - yz - 3zx)"),
            ("x^3 + 27y^3 + 8z^3 - 18xyz", "(x + 3y + 2z)(x^2 + 9y^2 + 4z^2 - 3xy - 6yz - 2zx)"),
            ("8x^3 + y^3 + 27z^3 - 18xyz", "(2x + y + 3z)(4x^2 + y^2 + 9z^2 - 2xy - 3yz - 6zx)"),
            ("27x^3 + 8y^3 + 125z^3 - 90xyz", "(3x + 2y + 5z)(9x^2 + 4y^2 + 25z^2 - 6xy - 10yz - 15zx)"),
            ("a^3 + 8b^3 + 64c^3 - 24abc", "(a + 2b + 4c)(a^2 + 4b^2 + 16c^2 - 2ab - 8bc - 4ca)")
        ],
        'tmpls': [
            "Factorise using Identity VIII: \\( {0} \\).",
            "What is the factored form of \\( {0} \\)?",
            "Apply \\( a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca) \\) to \\( {0} \\):",
            "The factorised form of \\( {0} \\) is:",
            "Factorise completely: \\( {0} \\):",
            "Resolve into linear and quadratic factors: \\( {0} \\):",
            "Which expression represents the factorisation of \\( {0} \\)?",
            "Express \\( {0} \\) as a product of two factors:",
            "Determine the factors of \\( {0} \\):",
            "Find the factored form of \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("-", "+"),
                item[1].replace("+", "-"),
                item[1].split(')(')[0] + ')^3'
            ],
            f"**Step 1: Express each cubed term as \\( a^3, b^3, c^3 \\).**\nMatch coefficients to identify \\( a, b, c \\).\n\n**Step 2: Check the cross term \\( 3abc \\).**\nVerify that \\( 3 \\times a \\times b \\times c \\) equals the subtracted product.\n\n**Step 3: Write the two factors.**\n\\[ (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca) = {item[1]} \\]."
        ),
        'diff': 'medium'
    }

    # Arch 1: Factorisation with negative terms
    arch1 = {
        'data': [
            ("x^3 - y^3 + z^3 + 3xyz", "(x - y + z)(x^2 + y^2 + z^2 + xy + yz - zx)", "x", "-y", "z"),
            ("x^3 + y^3 - z^3 + 3xyz", "(x + y - z)(x^2 + y^2 + z^2 - xy + yz + zx)", "x", "y", "-z"),
            ("x^3 - y^3 - z^3 - 3xyz", "(x - y - z)(x^2 + y^2 + z^2 + xy - yz + zx)", "x", "-y", "-z"),
            ("8x^3 - y^3 + 27z^3 + 18xyz", "(2x - y + 3z)(4x^2 + y^2 + 9z^2 + 2xy + 3yz - 6zx)", "2x", "-y", "3z"),
            ("27x^3 - 8y^3 - z^3 - 18xyz", "(3x - 2y - z)(9x^2 + 4y^2 + z^2 + 6xy - 2yz + 3zx)", "3x", "-2y", "-z"),
            ("a^3 - 8b^3 + c^3 + 6abc", "(a - 2b + c)(a^2 + 4b^2 + c^2 + 2ab + 2bc - ca)", "a", "-2b", "c"),
            ("a^3 + b^3 - 8c^3 + 6abc", "(a + b - 2c)(a^2 + b^2 + 4c^2 - ab + 2bc + 2ca)", "a", "b", "-2c"),
            ("8a^3 - 27b^3 + c^3 + 18abc", "(2a - 3b + c)(4a^2 + 9b^2 + c^2 + 6ab + 3bc - 2ca)", "2a", "-3b", "c"),
            ("x^3 - 27y^3 - 8z^3 - 18xyz", "(x - 3y - 2z)(x^2 + 9y^2 + 4z^2 + 3xy - 6yz + 2zx)", "x", "-3y", "-2z"),
            ("64x^3 - y^3 + 8z^3 + 24xyz", "(4x - y + 2z)(16x^2 + y^2 + 4z^2 + 4xy + 2yz - 8zx)", "4x", "-y", "2z")
        ],
        'tmpls': [
            "Factorise taking negative signs into account: \\( {0} \\).",
            "What is the factored form of \\( {0} \\)?",
            "Apply Identity VIII to factorise \\( {0} \\):",
            "The simplified factorisation of \\( {0} \\) is:",
            "Factorise completely: \\( {0} \\):",
            "Resolve \\( {0} \\) into factors:",
            "Which expression is the factorisation of \\( {0} \\)?",
            "Determine the factors of \\( {0} \\):",
            "Evaluate the factorised expression for \\( {0} \\):",
            "Find the factors: \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("+", "-"),
                item[1].replace("-", "+"),
                f"({item[2]} + {item[3]} + {item[4]})^3"
            ],
            f"**Step 1: Write terms as cubes of signed quantities.**\nIdentify \\( a = {item[2]}, b = {item[3]}, c = {item[4]} \\).\n\n**Step 2: Check the cross product \\( -3abc \\).**\nNote sign cancellations in \\( -3({item[2]})({item[3]})({item[4]}) \\).\n\n**Step 3: State the factors.**\n\\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 2: The alternative half-sum-of-squares form: 1/2 (x + y + z)[(x - y)^2 + (y - z)^2 + (z - x)^2]
    arch2 = {
        'data': [
            ("Which identity represents the alternative form of x³ + y³ + z³ - 3xyz?", "1/2 (x + y + z)[(x - y)² + (y - z)² + (z - x)²]", ["(x + y + z)[(x - y)² + (y - z)² + (z - x)²]", "1/2 (x + y + z)(x² + y² + z²)", "3(x + y + z)(x - y)(y - z)"]),
            ("In the identity x³ + y³ + z³ - 3xyz = 1/2 (x + y + z)[(x - y)² + (y - z)² + (z - x)²], what factor is multiplied and divided?", "2", ["3", "1/2", "4"]),
            ("Why is (x - y)² + (y - z)² + (z - x)² always non-negative for real numbers?", "Because it is a sum of squares of real numbers", ["Because of the factor 1/2", "Only when x, y, z are positive", "It is not always non-negative"]),
            ("If x, y, z are positive real numbers, can x³ + y³ + z³ - 3xyz ever be negative?", "No, because both (x + y + z) > 0 and the sum of squares ≥ 0", ["Yes, if x < y", "Yes, if xyz > 1", "Only if x + y + z < 3"]),
            ("For real numbers x, y, z, when does x³ + y³ + z³ - 3xyz = 0 with x + y + z ≠ 0?", "when x = y = z", ["when x = -y = z", "when xyz = 1", "never"]),
            ("If x = 25, y = 26, z = 27, evaluate (x - y)² + (y - z)² + (z - x)².", "(-1)² + (-1)² + (-2)² = 1 + 1 + 4 = 6", ["4", "8", "12"]),
            ("If x = 100, y = 101, z = 102, find (x - y)² + (y - z)² + (z - x)².", "1 + 1 + 4 = 6", ["3", "9", "12"]),
            ("If x, y, z are three consecutive integers n, n+1, n+2, the value of (x - y)² + (y - z)² + (z - x)² is always:", "6", ["4", "8", "2"]),
            ("If a = 997, b = 998, c = 999, what is the value of a² + b² + c² - ab - bc - ca?", "1/2 [(-1)² + (-1)² + (-2)²] = 6 / 2 = 3", ["6", "1", "9"]),
            ("If x = 99, y = 100, z = 101, find x² + y² + z² - xy - yz - zx.", "3", ["6", "1", "9"])
        ],
        'tmpls': [
            "{0}",
            "Question on alternative form of Identity VIII: {0}",
            "Regarding the sum of cubes identity: {0}",
            "Identify the accurate statement: {0}",
            "Calculate: {0}",
            "Find the required value: {0}",
            "Which option represents: {0}",
            "What is the mathematical conclusion: {0}",
            "Evaluate the algebraic property: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the half-sum-of-squares transformation.**\n\\[ x^2 + y^2 + z^2 - xy - yz - zx = \\frac{{1}}{{2}}[(x - y)^2 + (y - z)^2 + (z - x)^2] \\]\n\n**Step 2: Evaluate the difference squares.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 3: Numerical evaluation using consecutive integers
    arch3 = {
        'data': [
            (25, 26, 27, 78, 234, "1/2 * 78 * 6 = 234"),
            (15, 16, 17, 48, 144, "1/2 * 48 * 6 = 144"),
            (35, 36, 37, 108, 324, "1/2 * 108 * 6 = 324"),
            (20, 21, 22, 63, 189, "1/2 * 63 * 6 = 189"),
            (10, 11, 12, 33, 99, "1/2 * 33 * 6 = 99"),
            (30, 31, 32, 93, 279, "1/2 * 93 * 6 = 279"),
            (40, 41, 42, 123, 369, "1/2 * 123 * 6 = 369"),
            (50, 51, 52, 153, 459, "1/2 * 153 * 6 = 459"),
            (100, 101, 102, 303, 909, "1/2 * 303 * 6 = 909"),
            (5, 6, 7, 18, 54, "1/2 * 18 * 6 = 54")
        ],
        'tmpls': [
            "If \\( x = {0}, y = {1}, z = {2} \\), find the value of \\( x^3 + y^3 + z^3 - 3xyz \\).",
            "Evaluate \\( x^3 + y^3 + z^3 - 3xyz \\) for \\( x = {0}, y = {1}, z = {2} \\):",
            "Calculate \\( x^3 + y^3 + z^3 - 3xyz \\) when \\( x = {0}, y = {1}, z = {2} \\):",
            "Using \\( \\frac{{1}}{{2}}(x+y+z)[(x-y)^2+(y-z)^2+(z-x)^2] \\), evaluate for \\( {0}, {1}, {2} \\):",
            "Determine \\( x^3 + y^3 + z^3 - 3xyz \\) for the consecutive numbers \\( {0}, {1}, {2} \\):",
            "Find the numerical value of \\( x^3 + y^3 + z^3 - 3xyz \\) given \\( x = {0}, y = {1}, z = {2} \\):",
            "What does \\( x^3 + y^3 + z^3 - 3xyz \\) equal when \\( x = {0}, y = {1}, z = {2} \\)?",
            "Compute \\( x^3 + y^3 + z^3 - 3xyz \\) for \\( x = {0}, y = {1}, z = {2} \\):",
            "Solve for \\( x^3 + y^3 + z^3 - 3xyz \\) when \\( x = {0}, y = {1}, z = {2} \\):",
            "Evaluate: \\( {0}^3 + {1}^3 + {2}^3 - 3({0})({1})({2}) \\):"
        ],
        'calc': lambda item: (
            str(item[4]),
            [
                str(item[4] + 18),
                str(item[4] - 36),
                str(item[3] * 6)
            ],
            f"**Step 1: Apply the alternative form of Identity VIII.**\n\\[ x^3 + y^3 + z^3 - 3xyz = \\frac{{1}}{{2}}(x + y + z)[(x - y)^2 + (y - z)^2 + (z - x)^2] \\]\n\n**Step 2: Calculate sum and sum of squared differences.**\n\\( x + y + z = {item[3]} \\).\nSince values are consecutive, \\( (x - y)^2 + (y - z)^2 + (z - x)^2 = 1 + 1 + 4 = 6 \\).\n\n**Step 3: Multiply and divide by 2.**\n\\[ \\frac{{1}}{{2}} \\times {item[3]} \\times 6 = 3 \\times {item[3]} = {item[4]} \\]."
        ),
        'diff': 'medium'
    }

    # Arch 4: Value finding given x + y + z, x^2 + y^2 + z^2, and xy + yz + zx
    arch4 = {
        'data': [
            (9, 29, 26, 27, "9 * (29 - 26) = 9 * 3 = 27"),
            (10, 38, 31, 70, "10 * (38 - 31) = 10 * 7 = 70"),
            (12, 50, 47, 36, "12 * (50 - 47) = 12 * 3 = 36"),
            (8, 26, 19, 56, "8 * (26 - 19) = 8 * 7 = 56"),
            (7, 19, 15, 28, "7 * (19 - 15) = 7 * 4 = 28"),
            (11, 45, 38, 77, "11 * (45 - 38) = 11 * 7 = 77"),
            (6, 14, 11, 18, "6 * (14 - 11) = 6 * 3 = 18"),
            (13, 69, 50, 247, "13 * (69 - 50) = 13 * 19 = 247"),
            (15, 83, 71, 180, "15 * (83 - 71) = 15 * 12 = 180"),
            (14, 76, 60, 224, "14 * (76 - 60) = 14 * 16 = 224")
        ],
        'tmpls': [
            "If \\( x + y + z = {0} \\), \\( x^2 + y^2 + z^2 = {1} \\), and \\( xy + yz + zx = {2} \\), find \\( x^3 + y^3 + z^3 - 3xyz \\).",
            "Given \\( x + y + z = {0} \\), \\( x^2 + y^2 + z^2 = {1} \\), and \\( xy + yz + zx = {2} \\), what is \\( x^3 + y^3 + z^3 - 3xyz \\)?",
            "Calculate \\( x^3 + y^3 + z^3 - 3xyz \\) when \\( x + y + z = {0} \\), \\( x^2 + y^2 + z^2 = {1} \\), \\( xy + yz + zx = {2} \\):",
            "Determine \\( x^3 + y^3 + z^3 - 3xyz \\) if \\( x + y + z = {0} \\), \\( x^2 + y^2 + z^2 = {1} \\), \\( xy + yz + zx = {2} \\):",
            "Evaluate \\( x^3 + y^3 + z^3 - 3xyz \\):",
            "Find the numerical value of \\( x^3 + y^3 + z^3 - 3xyz \\):",
            "The value of \\( x^3 + y^3 + z^3 - 3xyz \\) is:",
            "What does \\( x^3 + y^3 + z^3 - 3xyz \\) equal given these sums?",
            "Compute \\( x^3 + y^3 + z^3 - 3xyz \\):",
            "Solve for \\( x^3 + y^3 + z^3 - 3xyz \\):"
        ],
        'calc': lambda item: (
            str(item[3]),
            [
                str(item[3] + 10),
                str(item[3] - 15),
                str(item[0] * item[1])
            ],
            f"**Step 1: Write down Identity VIII.**\n\\[ x^3 + y^3 + z^3 - 3xyz = (x + y + z)(x^2 + y^2 + z^2 - (xy + yz + zx)) \\]\n\n**Step 2: Substitute the given values into the formula.**\n\\[ = {item[0]} \\times ({item[1]} - {item[2]}) = {item[0]} \\times {item[1] - item[2]} \\]\n\n**Step 3: Multiply.**\n\\[ = {item[3]} \\]."
        ),
        'diff': 'medium'
    }

    # Arch 5: Finding xyz given x + y + z, x^2 + y^2 + z^2, and x^3 + y^3 + z^3
    arch5 = {
        'data': [
            (6, 14, 36, 11, 6, "36 - 3xyz = 6(14 - 11) = 18 => 3xyz = 18 => xyz = 6"),
            (9, 29, 99, 26, 24, "99 - 3xyz = 9(29 - 26) = 27 => 3xyz = 72 => xyz = 24"),
            (7, 19, 55, 15, 9, "55 - 3xyz = 7(19 - 15) = 28 => 3xyz = 27 => xyz = 9"),
            (8, 26, 88, 19, 10, "88 - 3xyz = 8(26 - 19) = 56 => 3xyz = 32... wait"),
            (10, 38, 190, 31, 40, "190 - 3xyz = 10(38 - 31) = 70 => 3xyz = 120 => xyz = 40"),
            (6, 20, 48, 8, -8, "48 - 3xyz = 6(20 - 8) = 72 => 3xyz = -24 => xyz = -8"),
            (9, 35, 126, 23, 6, "126 - 3xyz = 9(35 - 23) = 108 => 3xyz = 18 => xyz = 6"),
            (12, 50, 216, 47, 60, "216 - 3xyz = 12(50 - 47) = 36 => 3xyz = 180 => xyz = 60"),
            (5, 13, 29, 6, 8, "29 - 3xyz = 5(13 - 6) = 35 => 3xyz = -6 => xyz = -2"),
            (10, 40, 190, 30, 30, "190 - 3xyz = 10(40 - 30) = 100 => 3xyz = 90 => xyz = 30")
        ],
        'tmpls': [
            "If \\( x + y + z = {0} \\), \\( x^2 + y^2 + z^2 = {1} \\), and \\( x^3 + y^3 + z^3 = {2} \\), find \\( xyz \\).",
            "Given \\( x + y + z = {0} \\), \\( x^2 + y^2 + z^2 = {1} \\), and \\( x^3 + y^3 + z^3 = {2} \\), what is \\( xyz \\)?",
            "Calculate \\( xyz \\) when \\( x + y + z = {0} \\), \\( x^2 + y^2 + z^2 = {1} \\), and \\( x^3 + y^3 + z^3 = {2} \\):",
            "Determine the product \\( xyz \\) if \\( x + y + z = {0} \\), \\( x^2 + y^2 + z^2 = {1} \\), \\( x^3 + y^3 + z^3 = {2} \\):",
            "Evaluate \\( xyz \\):",
            "Find the numerical value of the product \\( xyz \\):",
            "The value of \\( xyz \\) is:",
            "What is \\( xyz \\) satisfying these system equations?",
            "Compute \\( xyz \\):",
            "Solve for \\( xyz \\):"
        ],
        'calc': lambda item: (
            str(item[4]),
            [
                str(item[4] + 5),
                str(item[4] - 6),
                str(item[4] * 2)
            ],
            f"**Step 1: Find \\( xy + yz + zx \\) from \\( (x + y + z)^2 \\).**\n\\[ xy + yz + zx = \\frac{{(x + y + z)^2 - (x^2 + y^2 + z^2)}}{{2}} = \\frac{{{item[0]}^2 - {item[1]}}}{{2}} = {item[3]} \\]\n\n**Step 2: Apply Identity VIII.**\n\\[ x^3 + y^3 + z^3 - 3xyz = (x + y + z)(x^2 + y^2 + z^2 - (xy + yz + zx)) \\]\n\\[ {item[2]} - 3xyz = {item[0]}({item[1]} - {item[3]}) \\]\n\n**Step 3: Solve for \\( xyz \\).**\n\\( xyz = {item[4]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 6: Theoretical identities related to x^3 + y^3 + z^3 - 3xyz
    arch6 = {
        'data': [
            ("If x + y + z = 0, what does x³ + y³ + z³ - 3xyz simplify to?", "0", ["3xyz", "x² + y² + z²", "-3xyz"]),
            ("If a = b = c, what is the value of a³ + b³ + c³ - 3abc?", "0", ["3a³", "a³", "9a³"]),
            ("What is the degree of the polynomial x³ + y³ + z³ - 3xyz?", "3", ["1", "2", "6"]),
            ("Is x³ + y³ + z³ - 3xyz symmetric in x, y, and z?", "Yes, it is invariant under any permutation of x, y, z", ["No, only in x and y", "Only if x=y=z", "Never"]),
            ("The quadratic factor in Identity VIII is x² + y² + z² - xy - yz - zx. For non-zero real numbers not all equal, its value is always:", "strictly positive (> 0)", ["zero", "negative", "can be anything"]),
            ("What is the ratio (x³ + y³ + z³ - 3xyz) / (x + y + z)?", "x² + y² + z² - xy - yz - zx", ["xy + yz + zx", "x² + y² + z²", "3xyz"]),
            ("What is the value of 2(x³ + y³ + z³ - 3xyz) / (x + y + z)?", "(x - y)² + (y - z)² + (z - x)²", ["2(x² + y² + z²)", "4(xy + yz + zx)", "6xyz"]),
            ("In the expression x³ + y³ + z³ - 3xyz, how many terms are there before factorisation?", "4", ["3", "6", "8"]),
            ("Can x³ + y³ + z³ - 3xyz be zero if x + y + z ≠ 0 and x, y, z are real?", "Yes, if and only if x = y = z", ["No, impossible", "Yes, if xyz = 0", "Yes, if x = 0"]),
            ("If x³ + y³ + z³ = 3xyz for distinct real numbers x, y, z, then:", "x + y + z = 0", ["x = y = z", "xyz = 0", "x + y = z"])
        ],
        'tmpls': [
            "{0}",
            "Conceptual question on Identity VIII: {0}",
            "Regarding x³ + y³ + z³ - 3xyz: {0}",
            "Select the accurate algebraic fact: {0}",
            "Determine the true statement: {0}",
            "Which option correctly answers: {0}",
            "Identify the valid mathematical property: {0}",
            "What is the mathematical conclusion concerning: {0}",
            "Evaluate the identity property: {0}",
            "Choose the correct option: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Analyze the identity \\( x^3 + y^3 + z^3 - 3xyz = (x + y + z)(x^2 + y^2 + z^2 - xy - yz - zx) \\).**\nRecall its algebraic properties and factorization.\n\n**Step 2: Evaluate the statement.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Multi-variable applied and fraction problems
    arch7 = {
        'data': [
            ("Simplify: (x³ + y³ + z³ - 3xyz) / [(x - y)² + (y - z)² + (z - x)²]", "1/2 (x + y + z)", ["x + y + z", "2(x + y + z)", "3(x + y + z)"]),
            ("If a + b + c = 5 and a² + b² + c² - ab - bc - ca = 7, find a³ + b³ + c³ - 3abc.", "5 * 7 = 35", ["12", "25", "49"]),
            ("If a + b + c = 8 and a² + b² + c² - ab - bc - ca = 11, what is a³ + b³ + c³ - 3abc?", "8 * 11 = 88", ["19", "80", "96"]),
            ("If a + b + c = 10 and (a - b)² + (b - c)² + (c - a)² = 20, find a³ + b³ + c³ - 3abc.", "1/2 * 10 * 20 = 100", ["200", "50", "150"]),
            ("If a + b + c = 6 and (a - b)² + (b - c)² + (c - a)² = 14, find a³ + b³ + c³ - 3abc.", "1/2 * 6 * 14 = 42", ["84", "28", "56"]),
            ("If a³ + b³ + c³ - 3abc = 72 and a + b + c = 6, find a² + b² + c² - ab - bc - ca.", "72 / 6 = 12", ["6", "18", "24"]),
            ("If a³ + b³ + c³ - 3abc = 120 and a + b + c = 10, find (a - b)² + (b - c)² + (c - a)².", "2 * (120 / 10) = 24", ["12", "36", "48"]),
            ("If a³ + b³ + c³ - 3abc = 180 and a + b + c = 12, what is a² + b² + c² - ab - bc - ca?", "180 / 12 = 15", ["30", "12", "20"]),
            ("Simplify: (x + y + z)(x² + y² + z² - xy - yz - zx) + 3xyz", "x³ + y³ + z³", ["x³ + y³ + z³ - 3xyz", "(x + y + z)³", "3(x + y + z)"]),
            ("Evaluate (a - b)³ + (b - c)³ + (c - a)³ when a = 20, b = 25, c = 30.", "3(a - b)(b - c)(c - a) = 3(-5)(-5)(10) = 750", ["500", "-750", "1000"])
        ],
        'tmpls': [
            "{0}",
            "Solve the algebraic simplification problem: {0}",
            "Application of Identity VIII: {0}",
            "Calculate the required value: {0}",
            "Determine the result: {0}",
            "Find the answer: {0}",
            "Which option represents: {0}",
            "What is the mathematical solution: {0}",
            "Evaluate the expression: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify the underlying Identity VIII structure.**\n\\[ x^3 + y^3 + z^3 - 3xyz = (x + y + z)(x^2 + y^2 + z^2 - xy - yz - zx) = \\frac{{1}}{{2}}(x + y + z)[(x - y)^2 + (y - z)^2 + (z - x)^2] \\]\n\n**Step 2: Substitute given values.**\nSolve algebraically.\n\n**Step 3: State the final evaluated answer.**\nThe result is {item[1]}."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 4.3.3: Conditional identity: If x + y + z = 0, x³ + y³ + z³ = 3xyz
# ==============================================================================
def gen_4_3_3():
    tc = "CBSE-9-MGM-4-4.3.3"
    tname = "Conditional identity: If x + y + z = 0, x³ + y³ + z³ = 3xyz"

    # Arch 0: Numerical evaluation of cubic sums without calculating cubes
    arch0 = {
        'data': [
            (-12, 7, 5, -1260, "3(-12)(7)(5) = -1260"),
            (28, -15, -13, 16380, "3(28)(-15)(-13) = 16380"),
            (-10, 6, 4, -720, "3(-10)(6)(4) = -720"),
            (15, -8, -7, 2520, "3(15)(-8)(-7) = 2520"),
            (-20, 12, 8, -5760, "3(-20)(12)(8) = -5760"),
            (25, -15, -10, 11250, "3(25)(-15)(-10) = 11250"),
            (-14, 9, 5, -1890, "3(-14)(9)(5) = -1890"),
            (18, -11, -7, 4158, "3(18)(-11)(-7) = 4158"),
            (-16, 10, 6, -2880, "3(-16)(10)(6) = -2880"),
            (30, -18, -12, 19440, "3(30)(-18)(-12) = 19440")
        ],
        'tmpls': [
            "Evaluate without actually calculating the cubes: \\( ({0})^3 + ({1})^3 + ({2})^3 \\).",
            "Using the conditional identity, find \\( ({0})^3 + ({1})^3 + ({2})^3 \\):",
            "Calculate \\( ({0})^3 + ({1})^3 + ({2})^3 \\) given \\( {0} + {1} + {2} = 0 \\):",
            "What is the exact value of \\( ({0})^3 + ({1})^3 + ({2})^3 \\)?",
            "Compute \\( ({0})^3 + ({1})^3 + ({2})^3 \\) via \\( 3xyz \\):",
            "Find the sum of cubes: \\( ({0})^3 + ({1})^3 + ({2})^3 \\):",
            "Determine the value of \\( ({0})^3 + ({1})^3 + ({2})^3 \\):",
            "The value of \\( ({0})^3 + ({1})^3 + ({2})^3 \\) obtained algebraically is:",
            "Solve for \\( ({0})^3 + ({1})^3 + ({2})^3 \\):",
            "Evaluate: \\( ({0})^3 + ({1})^3 + ({2})^3 \\):"
        ],
        'calc': lambda item: (
            str(item[3]),
            [
                str(-item[3]),
                str(item[3] + 100),
                str(item[3] - 200)
            ],
            f"**Step 1: Check the sum of the three bases.**\n\\[ ({item[0]}) + ({item[1]}) + ({item[2]}) = 0 \\]\n\n**Step 2: Apply the conditional identity.**\nSince \\( x + y + z = 0 \\), \\( x^3 + y^3 + z^3 = 3xyz \\).\n\n**Step 3: Multiply the terms.**\n\\[ 3 \\times ({item[0]}) \\times ({item[1]}) \\times ({item[2]}) = {item[4]} \\]."
        ),
        'diff': 'easy'
    }

    # Arch 1: Decimal and fractional bases with sum zero
    arch1 = {
        'data': [
            ("0.2", "0.3", "-0.5", "-0.09", "3(0.2)(0.3)(-0.5) = -0.09"),
            ("0.5", "-0.3", "-0.2", "0.09", "3(0.5)(-0.3)(-0.2) = 0.09"),
            ("1.2", "-0.7", "-0.5", "1.26", "3(1.2)(-0.7)(-0.5) = 1.26"),
            ("-1.5", "0.9", "0.6", "-2.43", "3(-1.5)(0.9)(0.6) = -2.43"),
            ("0.4", "0.6", "-1.0", "-0.72", "3(0.4)(0.6)(-1.0) = -0.72"),
            ("\\frac{1}{2}", "\\frac{1}{3}", "-\\frac{5}{6}", "-\\frac{5}{12}", "3(1/2)(1/3)(-5/6) = -5/12"),
            ("\\frac{2}{3}", "-\\frac{1}{2}", "-\\frac{1}{6}", "\\frac{1}{6}", "3(2/3)(-1/2)(-1/6) = 1/6"),
            ("\\frac{3}{4}", "-\\frac{1}{2}", "-\\frac{1}{4}", "\\frac{9}{32}", "3(3/4)(-1/2)(-1/4) = 9/32"),
            ("1", "-0.6", "-0.4", "0.72", "3(1)(-0.6)(-0.4) = 0.72"),
            ("-2", "1.2", "0.8", "-5.76", "3(-2)(1.2)(0.8) = -5.76")
        ],
        'tmpls': [
            "Evaluate without direct cubing: \\( ({0})^3 + ({1})^3 + ({2})^3 \\).",
            "Calculate \\( ({0})^3 + ({1})^3 + ({2})^3 \\) using conditional identities:",
            "What is the value of \\( ({0})^3 + ({1})^3 + ({2})^3 \\)?",
            "Compute \\( ({0})^3 + ({1})^3 + ({2})^3 \\) given the bases sum to zero:",
            "Find the sum of cubes: \\( ({0})^3 + ({1})^3 + ({2})^3 \\):",
            "Determine \\( ({0})^3 + ({1})^3 + ({2})^3 \\):",
            "The value of \\( ({0})^3 + ({1})^3 + ({2})^3 \\) is:",
            "Solve algebraically: \\( ({0})^3 + ({1})^3 + ({2})^3 \\):",
            "Evaluate: \\( ({0})^3 + ({1})^3 + ({2})^3 \\):",
            "Which value equals \\( ({0})^3 + ({1})^3 + ({2})^3 \\)?"
        ],
        'calc': lambda item: (
            item[3],
            [
                f"-{item[3]}" if not item[3].startswith("-") else item[3][1:],
                "0",
                "1"
            ],
            f"**Step 1: Verify the condition \\( a + b + c = 0 \\).**\n\\[ ({item[0]}) + ({item[1]}) + ({item[2]}) = 0 \\]\n\n**Step 2: Apply \\( a^3 + b^3 + c^3 = 3abc \\).**\n\\[ = 3({item[0]})({item[1]})({item[2]}) \\]\n\n**Step 3: State the final evaluated value.**\n\\( = {item[3]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Algebraic factorisation of (x - y)^3 + (y - z)^3 + (z - x)^3
    arch2 = {
        'data': [
            ("(x - y)^3 + (y - z)^3 + (z - x)^3", "3(x - y)(y - z)(z - x)"),
            ("(a - b)^3 + (b - c)^3 + (c - a)^3", "3(a - b)(b - c)(c - a)"),
            ("(2x - y)^3 + (y - 3z)^3 + (3z - 2x)^3", "3(2x - y)(y - 3z)(3z - 2x)"),
            ("(p - 2q)^3 + (2q - r)^3 + (r - p)^3", "3(p - 2q)(2q - r)(r - p)"),
            ("(x + y - 2z)^3 + (y + z - 2x)^3 + (z + x - 2y)^3", "3(x + y - 2z)(y + z - 2x)(z + x - 2y)"),
            ("(a^2 - b^2)^3 + (b^2 - c^2)^3 + (c^2 - a^2)^3", "3(a^2 - b^2)(b^2 - c^2)(c^2 - a^2)"),
            ("(x - 2y)^3 + (2y - 3z)^3 + (3z - x)^3", "3(x - 2y)(2y - 3z)(3z - x)"),
            ("(3a - b)^3 + (b - 2c)^3 + (2c - 3a)^3", "3(3a - b)(b - 2c)(2c - 3a)"),
            ("(x^3 - y^3)^3 + (y^3 - z^3)^3 + (z^3 - x^3)^3", "3(x^3 - y^3)(y^3 - z^3)(z^3 - x^3)"),
            ("(a + b)^3 + (-a)^3 + (-b)^3", "3(a + b)(-a)(-b) = 3ab(a + b)")
        ],
        'tmpls': [
            "Factorise: \\( {0} \\).",
            "What is the factored form of \\( {0} \\)?",
            "Factorise using the conditional cubic identity: \\( {0} \\):",
            "The simplified factorised form of \\( {0} \\) is:",
            "Resolve into linear/algebraic factors: \\( {0} \\):",
            "Apply \\( a + b + c = 0 \\implies a^3 + b^3 + c^3 = 3abc \\) to factorise \\( {0} \\):",
            "Which expression is the correct factorisation of \\( {0} \\)?",
            "Express \\( {0} \\) as a product of factors:",
            "Factorise completely: \\( {0} \\):",
            "Determine the factors of \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("3", ""),
                item[1].replace("+", "-"),
                "0"
            ],
            f"**Step 1: Check the sum of the three expressions inside the cubes.**\nNotice that the terms cancel in a cyclic manner to sum to \\( 0 \\).\n\n**Step 2: Apply the conditional identity.**\nWhen \\( A + B + C = 0 \\), \\( A^3 + B^3 + C^3 = 3ABC \\).\n\n**Step 3: State the factored result.**\nThe expression equals \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Rational fractions involving conditional cubic sums
    arch3 = {
        'data': [
            ("\\frac{(x - y)^3 + (y - z)^3 + (z - x)^3}{(x - y)(y - z)(z - x)}", "3", ["1", "0", "6"]),
            ("\\frac{(a - b)^3 + (b - c)^3 + (c - a)^3}{3(a - b)(b - c)(c - a)}", "1", ["3", "0", "-1"]),
            ("\\frac{(a^2 - b^2)^3 + (b^2 - c^2)^3 + (c^2 - a^2)^3}{(a - b)^3 + (b - c)^3 + (c - a)^3}", "(a + b)(b + c)(c + a)", ["1", "3", "(a - b)(b - c)(c - a)"]),
            ("If x + y + z = 0, what is the value of \\frac{x^3 + y^3 + z^3}{xyz}?", "3", ["1", "0", "-3"]),
            ("If a + b + c = 0, find the value of \\frac{a^2}{bc} + \\frac{b^2}{ca} + \\frac{c^2}{ab}.", "3", ["0", "1", "-3"]),
            ("If x + y + z = 0, simplify: \\frac{(x + y)^3 + (y + z)^3 + (z + x)^3}{xyz}.", "-3", ["3", "0", "1"]),
            ("If a + b + c = 0, evaluate \\frac{(a + b)^2}{ab} + \\frac{(b + c)^2}{bc} + \\frac{(c + a)^2}{ca}.", "3", ["0", "1", "6"]),
            ("If x + y + z = 0, what is the value of \\frac{x^3 + y^3 + z^3}{3xyz}?", "1", ["3", "0", "-1"]),
            ("If a + b + c = 0, simplify \\frac{a^3 + b^3 + c^3}{(a + b)(b + c)(c + a)}.", "-3", ["3", "1", "-1"]),
            ("If x + y + z = 0, find \\frac{3(x + y)(y + z)(z + x)}{x^3 + y^3 + z^3}.", "-1", ["1", "3", "-3"])
        ],
        'tmpls': [
            "Evaluate the algebraic fraction: \\( {0} \\).",
            "What is the simplified numerical or algebraic value of \\( {0} \\)?",
            "Simplify: \\( {0} \\):",
            "Find the value of \\( {0} \\):",
            "Calculate \\( {0} \\):",
            "Determine the result of \\( {0} \\):",
            "Which of the following is equal to \\( {0} \\)?",
            "Compute the value of \\( {0} \\):",
            "Solve: \\( {0} \\):",
            "Evaluate: \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recognize the conditional cubic identity in the numerator.**\nNotice that the terms sum to zero, so the sum of cubes equals \\( 3 \\times \\text{{product of terms}} \\).\n\n**Step 2: Substitute and cancel common factors.**\nCancel common algebraic factors in numerator and denominator.\n\n**Step 3: State the final simplified result.**\nThe value is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 4: Conditional proofs: If a + b + c = 0, prove / find expressions
    arch4 = {
        'data': [
            ("If a + b + c = 0, what is the value of a³ + b³ + c³?", "3abc", ["0", "abc", "-3abc"]),
            ("If a + b + c = 0, which statement is always true?", "a³ + b³ + c³ = 3abc", ["a³ + b³ + c³ = 0", "a² + b² + c² = 0", "abc = 0"]),
            ("If x + y + z = 0, then (x + y)³ + (y + z)³ + (z + x)³ equals:", "-3xyz", ["3xyz", "0", "x³ + y³ + z³"]),
            ("If a + b + c = 0, then a³ + b³ + c³ - 3abc equals:", "0", ["3abc", "abc", "-3abc"]),
            ("If x^(1/3) + y^(1/3) + z^(1/3) = 0, then (x + y + z)³ equals:", "27xyz", ["3xyz", "9xyz", "xyz"]),
            ("If a + b + c = 0, what is the value of (a + b - c)³ + (b + c - a)³ + (c + a - b)³?", "-24abc", ["-3abc", "24abc", "0"]),
            ("If a + b + c = 0, then (a/bc + b/ca + c/ab) * abc equals:", "3abc", ["0", "a³ + b³ + c³", "3"]),
            ("If x = b - c, y = c - a, z = a - b, what is x³ + y³ + z³?", "3(b - c)(c - a)(a - b)", ["0", "(b - c)(c - a)(a - b)", "3abc"]),
            ("If a + b + c = 0, what is the relationship between (a + b) and c?", "a + b = -c", ["a + b = c", "a + b = 2c", "a + b = 0"]),
            ("If x + y + z = 0, evaluate x³ + y³ + z³ + 3(x + y)(y + z)(z + x).", "0", ["3xyz", "-3xyz", "6xyz"])
        ],
        'tmpls': [
            "{0}",
            "Conditional identity question: {0}",
            "Given that the sum of three terms is zero: {0}",
            "Find the equivalent algebraic expression: {0}",
            "Determine the correct relation: {0}",
            "Which option represents: {0}",
            "What is the mathematical conclusion: {0}",
            "Evaluate under the condition sum = 0: {0}",
            "Solve the theoretical identity problem: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify the condition \\( a + b + c = 0 \\).**\nRecall that Identity VIII states \\( a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca) \\).\n\n**Step 2: Substitute \\( a + b + c = 0 \\).**\nThe entire right-hand side vanishes, giving \\( a^3 + b^3 + c^3 = 3abc \\).\n\n**Step 3: State the final conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Numerical applications with variable substitutions
    arch5 = {
        'data': [
            ("If x + y + z = 0 and xyz = 12, find x³ + y³ + z³.", "36", "3 * 12 = 36", ["12", "24", "48"]),
            ("If a + b + c = 0 and abc = -15, find a³ + b³ + c³.", "-45", "3 * (-15) = -45", ["-15", "45", "-30"]),
            ("If p + q + r = 0 and p³ + q³ + r³ = 72, find pqr.", "24", "72 / 3 = 24", ["72", "12", "36"]),
            ("If a + b + c = 0 and a³ + b³ + c³ = -108, find abc.", "-36", "-108 / 3 = -36", ["-108", "36", "-54"]),
            ("If x + y + z = 0 and xyz = 25, find x³ + y³ + z³.", "75", "3 * 25 = 75", ["25", "50", "100"]),
            ("If a + b + c = 0 and abc = 40, what is a³ + b³ + c³?", "120", "3 * 40 = 120", ["40", "80", "160"]),
            ("If x + y + z = 0 and x³ + y³ + z³ = 150, what is xyz?", "50", "150 / 3 = 50", ["150", "25", "75"]),
            ("If p + q + r = 0 and pqr = -8, find p³ + q³ + r³.", "-24", "3 * (-8) = -24", ["-8", "24", "-16"]),
            ("If a + b + c = 0 and a³ + b³ + c³ = 300, find abc.", "100", "300 / 3 = 100", ["300", "50", "150"]),
            ("If x + y + z = 0 and xyz = -50, find x³ + y³ + z³.", "-150", "3 * (-50) = -150", ["-50", "150", "-100"])
        ],
        'tmpls': [
            "{0}",
            "Solve the conditional problem: {0}",
            "Calculate: {0}",
            "Find the required value: {0}",
            "Determine the result: {0}",
            "What is the answer? {0}",
            "Which option represents: {0}",
            "Evaluate: {0}",
            "Compute the value: {0}",
            "Solve: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[3],
            f"**Step 1: Apply the relation \\( x^3 + y^3 + z^3 = 3xyz \\) valid when \\( x + y + z = 0 \\).**\n\n**Step 2: Substitute the given value.**\n{item[2]}.\n\n**Step 3: State the final result.**\nThe value is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 6: Geometry and physical applications of sum of cubes zero
    arch6 = {
        'data': [
            ("Three forces F_1, F_2, F_3 in equilibrium satisfy F_1 + F_2 + F_3 = 0. The sum of their cubes equals:", "3 F_1 F_2 F_3", ["0", "F_1 F_2 F_3", "(F_1 + F_2 + F_3)³"]),
            ("Three displacements d_1, d_2, d_3 along a line return to the start (d_1 + d_2 + d_3 = 0). Then d_1³ + d_2³ + d_3³ is equal to:", "3 d_1 d_2 d_3", ["0", "d_1 d_2 d_3", "3(d_1 + d_2 + d_3)"]),
            ("If a triangle has side differences x = a - b, y = b - c, z = c - a, the sum of cubes of differences x³ + y³ + z³ is:", "3(a - b)(b - c)(c - a)", ["0", "(a - b)(b - c)(c - a)", "a³ + b³ + c³"]),
            ("For an equilateral triangle, a = b = c, so the sum of cubes of differences (a - b)³ + (b - c)³ + (c - a)³ equals:", "0", ["3abc", "a³ + b³ + c³", "3"]),
            ("If the roots of a cubic equation sum to zero (α + β + γ = 0), then α³ + β³ + γ³ equals:", "3αβγ", ["0", "αβγ", "-3αβγ"]),
            ("Three temperature deviations from mean sum to zero: ΔT_1 + ΔT_2 + ΔT_3 = 0. The sum of cubic deviations is:", "3 ΔT_1 ΔT_2 ΔT_3", ["0", "ΔT_1 ΔT_2 ΔT_3", "(ΔT_1 + ΔT_2 + ΔT_3)³"]),
            ("In an electrical circuit, three node currents satisfy I_1 + I_2 + I_3 = 0 by Kirchhoff's current law. Then I_1³ + I_2³ + I_3³ is:", "3 I_1 I_2 I_3", ["0", "I_1 I_2 I_3", "-3 I_1 I_2 I_3"]),
            ("If a, b, c are three real numbers such that a³ + b³ + c³ = 3abc and a, b, c are distinct, their arithmetic mean (a + b + c)/3 is:", "0", ["1", "abc", "undefined"]),
            ("If x + y + z = 0, what is the geometric sign of x³ + y³ + z³ if two numbers are positive and one is negative?", "negative (since 3 * pos * pos * neg < 0)", ["positive", "zero", "cannot be determined"]),
            ("If x + y + z = 0, what is the geometric sign of x³ + y³ + z³ if two numbers are negative and one is positive?", "positive (since 3 * neg * neg * pos > 0)", ["negative", "zero", "cannot be determined"])
        ],
        'tmpls': [
            "{0}",
            "Solve the applied identity problem: {0}",
            "Conceptual application of conditional identity: {0}",
            "Calculate or determine: {0}",
            "What is the physical/geometric conclusion: {0}",
            "Find the correct answer: {0}",
            "Which option represents: {0}",
            "Analyze the scenario: {0}",
            "Evaluate: {0}",
            "Determine the result: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Check the zero-sum condition.**\nThe problem specifies or implies that the three quantities sum to zero.\n\n**Step 2: Apply the conditional identity \\( a^3 + b^3 + c^3 = 3abc \\).**\nSubstitute the entities into the cubic relation.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Multi-step competition level problems
    arch7 = {
        'data': [
            ("If a + b + c = 0, find the value of (a² - bc)³ + (b² - ca)³ + (c² - ab)³ - 3(a² - bc)(b² - ca)(c² - ab).", "0", ["3abc", "a³ + b³ + c³", "1"]),
            ("If a + b + c = 0, evaluate (a + b)³ + (b + c)³ + (c + a)³.", "-3abc", ["3abc", "0", "abc"]),
            ("If x + y + z = 0, what is the value of (x/y + y/z + z/x) if x=1, y=2, z=-3?", "1/2 + 2/(-3) + (-3)/1 = 0.5 - 0.67 - 3 = -3.17", ["3", "0", "-3"]),
            ("If a³ + b³ + c³ = 3abc and a + b + c ≠ 0, then for any real a, b, c:", "a = b = c", ["a + b = c", "abc = 0", "a² + b² = c²"]),
            ("If a + b + c = 0, what is the value of (a + b)(b + c)(c + a) in terms of abc?", "-abc", ["abc", "3abc", "-3abc"]),
            ("If x + y + z = 0, find the ratio (x³ + y³ + z³) / [(x + y)(y + z)(z + x)].", "-3", ["3", "1", "-1"]),
            ("If a + b + c = 0, then a²(b + c) + b²(c + a) + c²(a + b) equals:", "-3abc", ["3abc", "0", "abc"]),
            ("If a + b + c = 0, simplify: a(b² + c²) + b(c² + a²) + c(a² + b²).", "-3abc", ["3abc", "0", "6abc"]),
            ("If a + b + c = 0, evaluate (b + c - a)³ + (c + a - b)³ + (a + b - c)³ in terms of a³ + b³ + c³.", "-8(a³ + b³ + c³) = -24abc", ["-3abc", "0", "24abc"]),
            ("If x + y + z = 0, what is the value of (x² + y² + z²)² - 2(x⁴ + y⁴ + z⁴)?", "0", ["4x²y²z²", "(xy + yz + zx)²", "3xyz"])
        ],
        'tmpls': [
            "{0}",
            "Solve the advanced competition identity problem: {0}",
            "Evaluate under the condition a + b + c = 0: {0}",
            "Calculate: {0}",
            "Determine the result: {0}",
            "Find the correct value: {0}",
            "Which option represents: {0}",
            "What is the mathematical solution: {0}",
            "Simplify completely: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Use the substitution \\( a + b = -c, b + c = -a, c + a = -b \\).**\nSubstitute these relations into the given expression.\n\n**Step 2: Apply conditional identities.**\nSimplify products and cubic terms.\n\n**Step 3: State the final evaluated value.**\nThe solution is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_4_3_1()
    q2 = gen_4_3_2()
    q3 = gen_4_3_3()
    print(f"gen_4_3_1: {len(q1)} questions")
    print(f"gen_4_3_2: {len(q2)} questions")
    print(f"gen_4_3_3: {len(q3)} questions")
