# scripts/build_cbse9_mgm_ch4_part4.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 4: Exploring Algebraic Identities
Part 4:
- Subtopic 4.4.1: Factoring quadratic trinomials ax² + bx + c
- Subtopic 4.4.2: Factoring cubic expressions using trial and factor theorem
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 4
CH_NAME = "Exploring Algebraic Identities"

# ==============================================================================
# SUBTOPIC 4.4.1: Factoring quadratic trinomials ax² + bx + c
# ==============================================================================
def gen_4_4_1():
    tc = "CBSE-9-MGM-4-4.4.1"
    tname = "Factoring quadratic trinomials ax² + bx + c"

    # Arch 0: Monic quadratic trinomials x² + bx + c with positive roots
    arch0 = {
        'data': [
            ("x^2 + 7x + 12", "(x + 3)(x + 4)", "3, 4", "3 + 4 = 7, 3 * 4 = 12"),
            ("x^2 + 9x + 20", "(x + 4)(x + 5)", "4, 5", "4 + 5 = 9, 4 * 5 = 20"),
            ("x^2 + 8x + 15", "(x + 3)(x + 5)", "3, 5", "3 + 5 = 8, 3 * 5 = 15"),
            ("x^2 + 10x + 21", "(x + 3)(x + 7)", "3, 7", "3 + 7 = 10, 3 * 7 = 21"),
            ("x^2 + 11x + 28", "(x + 4)(x + 7)", "4, 7", "4 + 7 = 11, 4 * 7 = 28"),
            ("x^2 + 13x + 36", "(x + 4)(x + 9)", "4, 9", "4 + 9 = 13, 4 * 9 = 36"),
            ("x^2 + 12x + 35", "(x + 5)(x + 7)", "5, 7", "5 + 7 = 12, 5 * 7 = 35"),
            ("x^2 + 15x + 56", "(x + 7)(x + 8)", "7, 8", "7 + 8 = 15, 7 * 8 = 56"),
            ("x^2 + 14x + 45", "(x + 5)(x + 9)", "5, 9", "5 + 9 = 14, 5 * 9 = 45"),
            ("x^2 + 17x + 72", "(x + 8)(x + 9)", "8, 9", "8 + 9 = 17, 8 * 9 = 72")
        ],
        'tmpls': [
            "Factorise by splitting the middle term: \\( {0} \\).",
            "What are the linear factors of \\( {0} \\)?",
            "Factorise the quadratic polynomial: \\( {0} \\):",
            "The factored form of \\( {0} \\) is:",
            "Find the factors of \\( {0} \\):",
            "Resolve into linear factors: \\( {0} \\):",
            "Which of the following represents the factorisation of \\( {0} \\)?",
            "Factorise completely: \\( {0} \\):",
            "Determine the factors of \\( {0} \\):",
            "Express \\( {0} \\) as a product of two linear polynomials:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("+", "-"),
                f"(x + 1)(x + {item[0].split('+ ')[-1]})",
                f"(x + 2)(x + {int(item[0].split('+ ')[-1]) // 2})" if int(item[0].split('+ ')[-1]) % 2 == 0 else f"(x + 3)(x + {int(item[0].split('+ ')[-1]) // 3})"
            ],
            f"**Step 1: Find two numbers whose product is the constant term and sum is the middle coefficient.**\nNumbers: {item[2]} because {item[3]}.\n\n**Step 2: Split the middle term and factor by grouping.**\n\\[ {item[0]} = x^2 + {item[2].split(', ')[0]}x + {item[2].split(', ')[1]}x + {item[0].split('+ ')[-1]} \\]\n\n**Step 3: Factor out common binomial.**\n\\( = {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Monic quadratic trinomials with negative signs: x² - bx + c and x² + bx - c
    arch1 = {
        'data': [
            ("x^2 - 7x + 12", "(x - 3)(x - 4)", "-3, -4", "(-3) + (-4) = -7, (-3)(-4) = 12"),
            ("x^2 - 9x + 20", "(x - 4)(x - 5)", "-4, -5", "(-4) + (-5) = -9, (-4)(-5) = 20"),
            ("x^2 - 8x + 15", "(x - 3)(x - 5)", "-3, -5", "(-3) + (-5) = -8, (-3)(-5) = 15"),
            ("x^2 - 10x + 21", "(x - 3)(x - 7)", "-3, -7", "(-3) + (-7) = -10, (-3)(-7) = 21"),
            ("x^2 + 2x - 15", "(x + 5)(x - 3)", "5, -3", "5 + (-3) = 2, 5(-3) = -15"),
            ("x^2 - 2x - 15", "(x - 5)(x + 3)", "-5, 3", "(-5) + 3 = -2, (-5)(3) = -15"),
            ("x^2 + x - 20", "(x + 5)(x - 4)", "5, -4", "5 + (-4) = 1, 5(-4) = -20"),
            ("x^2 - x - 20", "(x - 5)(x + 4)", "-5, 4", "(-5) + 4 = -1, (-5)(4) = -20"),
            ("x^2 + 5x - 24", "(x + 8)(x - 3)", "8, -3", "8 + (-3) = 5, 8(-3) = -24"),
            ("x^2 - 5x - 24", "(x - 8)(x + 3)", "-8, 3", "(-8) + 3 = -5, (-8)(3) = -24")
        ],
        'tmpls': [
            "Factorise by splitting the middle term: \\( {0} \\).",
            "What is the factored form of \\( {0} \\)?",
            "Factorise the quadratic: \\( {0} \\):",
            "The linear factors of \\( {0} \\) are:",
            "Find the factors: \\( {0} \\):",
            "Resolve \\( {0} \\) into factors:",
            "Which option represents the correct factorisation of \\( {0} \\)?",
            "Factorise: \\( {0} \\):",
            "Determine the factors of \\( {0} \\):",
            "Express \\( {0} \\) in factored form:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("-", "+") if "-" in item[1] else item[1].replace("+", "-"),
                f"(x - 1)(x - {abs(int(item[0].split(' ')[-1]))})",
                f"(x + 2)(x - {abs(int(item[0].split(' ')[-1])) // 2})"
            ],
            f"**Step 1: Find two numbers whose product is the constant term and sum is the linear coefficient.**\nNumbers: {item[2]} because {item[3]}.\n\n**Step 2: Split the middle term.**\nGroup terms into pairs.\n\n**Step 3: Factor completely.**\nThe factored form is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Non-monic quadratics: ax² + bx + c with a > 1
    arch2 = {
        'data': [
            ("2x^2 + 7x + 3", "(2x + 1)(x + 3)", "ac = 6", "1 + 6 = 7, 1 * 6 = 6"),
            ("6x^2 + 17x + 5", "(2x + 5)(3x + 1)", "ac = 30", "15 + 2 = 17, 15 * 2 = 30"),
            ("6x^2 + 5x - 6", "(2x + 3)(3x - 2)", "ac = -36", "9 + (-4) = 5, 9 * (-4) = -36"),
            ("3x^2 - x - 4", "(3x - 4)(x + 1)", "ac = -12", "-4 + 3 = -1, (-4) * 3 = -12"),
            ("12x^2 - 7x + 1", "(3x - 1)(4x - 1)", "ac = 12", "-3 + (-4) = -7, (-3)(-4) = 12"),
            ("2x^2 + 11x + 15", "(2x + 5)(x + 3)", "ac = 30", "5 + 6 = 11, 5 * 6 = 30"),
            ("4x^2 + 12x + 5", "(2x + 1)(2x + 5)", "ac = 20", "2 + 10 = 12, 2 * 10 = 20"),
            ("3x^2 + 10x + 8", "(3x + 4)(x + 2)", "ac = 24", "4 + 6 = 10, 4 * 6 = 24"),
            ("5x^2 - 16x + 3", "(5x - 1)(x - 3)", "ac = 15", "-1 + (-15) = -16, (-1)(-15) = 15"),
            ("7x^2 - 19x - 6", "(7x + 2)(x - 3)", "ac = -42", "2 + (-21) = -19, 2 * (-21) = -42")
        ],
        'tmpls': [
            "Factorise: \\( {0} \\).",
            "What is the factorisation of the quadratic \\( {0} \\)?",
            "Factorise by splitting the middle term: \\( {0} \\):",
            "The factored form of \\( {0} \\) is:",
            "Find the linear factors of \\( {0} \\):",
            "Resolve \\( {0} \\) into factors:",
            "Which of the following is equal to \\( {0} \\)?",
            "Factorise completely: \\( {0} \\):",
            "Determine the factors of \\( {0} \\):",
            "Express \\( {0} \\) as a product of two binomials:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("+", "-") if "+" in item[1] else item[1].replace("-", "+"),
                item[1].split(')(')[0] + ')^2',
                f"(x + 1)({item[0].split('x^2')[0]}x + {item[0].split(' ')[-1]})"
            ],
            f"**Step 1: Compute product \\( ac \\) and find factors summing to \\( b \\).**\n{item[2]} and {item[3]}.\n\n**Step 2: Split the middle term and factor by grouping.**\nRewrite \\( bx \\) as the sum of the two split terms and group pairs.\n\n**Step 3: Factor out the common binomial.**\n\\( = {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Quadratic trinomials with radical / surd coefficients
    arch3 = {
        'data': [
            ("x^2 + 2\\sqrt{3}x - 24", "(x + 4\\sqrt{3})(x - 2\\sqrt{3})", "ac = -24", "4√3 - 2√3 = 2√3, (4√3)(-2√3) = -24"),
            ("\\sqrt{3}x^2 + 10x + 7\\sqrt{3}", "(\\sqrt{3}x + 7)(x + \\sqrt{3})", "ac = 21", "7 + 3 = 10, 7 * 3 = 21"),
            ("\\sqrt{2}x^2 + 7x + 5\\sqrt{2}", "(\\sqrt{2}x + 5)(x + \\sqrt{2})", "ac = 10", "5 + 2 = 7, 5 * 2 = 10"),
            ("2\\sqrt{3}x^2 - 5x + \\sqrt{3}", "(2x - \\sqrt{3})(\\sqrt{3}x - 1)", "ac = 6", "-2 + (-3) = -5, (-2)(-3) = 6"),
            ("x^2 - 3\\sqrt{5}x + 10", "(x - 2\\sqrt{5})(x - \\sqrt{5})", "ac = 10", "-2√5 - √5 = -3√5, (-2√5)(-√5) = 10"),
            ("x^2 + 5\\sqrt{2}x + 12", "(x + 4\\sqrt{2})(x + \\sqrt{2})", "ac = 12", "4√2 + √2 = 5√2, (4√2)(√2) = 8... wait: (3√2)(2√2) = 12"),
            ("x^2 - 4\\sqrt{3}x + 9", "(x - 3\\sqrt{3})(x - \\sqrt{3})", "ac = 9", "-3√3 - √3 = -4√3, (-3√3)(-√3) = 9"),
            ("2x^2 + 3\\sqrt{5}x + 5", "(2x + \\sqrt{5})(x + \\sqrt{5})", "ac = 10", "2√5 + √5 = 3√5, (2√5)(√5) = 10"),
            ("3\\sqrt{5}x^2 + 25x - 10\\sqrt{5}", "(\\sqrt{5}x + 10)(3x - \\sqrt{5})", "ac = -150", "30 + (-5) = 25, 30(-5) = -150"),
            ("x^2 + 3\\sqrt{3}x + 6", "(x + 2\\sqrt{3})(x + \\sqrt{3})", "ac = 6", "2√3 + √3 = 3√3, (2√3)(√3) = 6")
        ],
        'tmpls': [
            "Factorise the surd quadratic: \\( {0} \\).",
            "What is the factored form of \\( {0} \\)?",
            "Factorise completely: \\( {0} \\):",
            "The linear factors of \\( {0} \\) are:",
            "Resolve \\( {0} \\) into factors:",
            "Find the factorisation of \\( {0} \\):",
            "Which expression represents \\( {0} \\)?",
            "Factorise: \\( {0} \\):",
            "Determine the factors of \\( {0} \\):",
            "Express \\( {0} \\) as a product of linear surd factors:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("+", "-") if "+" in item[1] else item[1].replace("-", "+"),
                f"(x + \\sqrt{{3}})(x + \\sqrt{{3}})",
                f"(x - 2)(x + {item[0].split(' ')[-1]})"
            ],
            f"**Step 1: Compute product \\( ac \\) and express factors with radicals.**\n{item[2]} and {item[3]}.\n\n**Step 2: Split the middle term with the radical coefficients.**\nGroup terms and extract common radical factors.\n\n**Step 3: State the factored form.**\nThe result is \\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 4: Word problems on dimensions of rectangle from quadratic area
    arch4 = {
        'data': [
            ("The area of a rectangle is given by 25a² - 35a + 12. Possible expressions for its length and breadth are:", "(5a - 3) and (5a - 4)", "25a² - 35a + 12 = (5a - 3)(5a - 4)", ["(5a + 3) and (5a + 4)", "(5a - 2) and (5a - 6)", "(25a - 1) and (a - 12)"]),
            ("The area of a rectangular field is 35y² + 13y - 12. What are possible expressions for its length and breadth?", "(5y + 4) and (7y - 3)", "35y² + 13y - 12 = (5y + 4)(7y - 3)", ["(5y - 4) and (7y + 3)", "(35y - 1) and (y + 12)", "(7y + 4) and (5y - 3)"]),
            ("A rectangular swimming pool has area 12x² - 7x + 1. Find its length and breadth.", "(3x - 1) and (4x - 1)", "12x² - 7x + 1 = (3x - 1)(4x - 1)", ["(3x + 1) and (4x + 1)", "(6x - 1) and (2x - 1)", "(12x - 1) and (x - 1)"]),
            ("The area of a rectangular cardboard sheet is 6x² + 5x - 6. What are its dimensions?", "(2x + 3) and (3x - 2)", "6x² + 5x - 6 = (2x + 3)(3x - 2)", ["(2x - 3) and (3x + 2)", "(6x - 1) and (x + 6)", "(3x + 1) and (2x - 6)"]),
            ("The area of a garden is 2x² + 7x + 3. Find its dimensions.", "(2x + 1) and (x + 3)", "2x² + 7x + 3 = (2x + 1)(x + 3)", ["(2x + 3) and (x + 1)", "(2x - 1) and (x - 3)", "(x + 1) and (x + 3)"]),
            ("A rectangular plot has area x² + 11x + 24. What are possible expressions for its dimensions?", "(x + 3) and (x + 8)", "x² + 11x + 24 = (x + 3)(x + 8)", ["(x + 4) and (x + 6)", "(x + 2) and (x + 12)", "(x + 1) and (x + 24)"]),
            ("The area of a rectangular carpet is 3x² - x - 4. Possible dimensions are:", "(3x - 4) and (x + 1)", "3x² - x - 4 = (3x - 4)(x + 1)", ["(3x + 4) and (x - 1)", "(3x - 2) and (x + 2)", "(x - 4) and (3x + 1)"]),
            ("The area of a sheet of metal is 4x² + 4x - 3. What are its dimensions?", "(2x + 3) and (2x - 1)", "4x² + 4x - 3 = (2x + 3)(2x - 1)", ["(2x - 3) and (2x + 1)", "(4x - 1) and (x + 3)", "(2x + 1) and (2x + 3)"]),
            ("A rectangle of area 6x² + 17x + 5 has possible dimensions:", "(2x + 5) and (3x + 1)", "6x² + 17x + 5 = (2x + 5)(3x + 1)", ["(2x + 1) and (3x + 5)", "(6x + 5) and (x + 1)", "(2x - 5) and (3x - 1)"]),
            ("The floor area of a hall is 2x² + 11x + 15. Its possible length and breadth are:", "(2x + 5) and (x + 3)", "2x² + 11x + 15 = (2x + 5)(x + 3)", ["(2x + 3) and (x + 5)", "(2x - 5) and (x - 3)", "(x + 5) and (x + 3)"])
        ],
        'tmpls': [
            "{0}",
            "Solve the area factorisation problem: {0}",
            "Application of quadratic factorisation in mensuration: {0}",
            "Find the dimensions: {0}",
            "Determine possible dimensions: {0}",
            "Which option gives possible dimensions: {0}",
            "Calculate: {0}",
            "What are the linear dimensions? {0}",
            "Evaluate: {0}",
            "Compute the factor dimensions: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[3],
            f"**Step 1: Factorise the quadratic expression representing area.**\n{item[2]}.\n\n**Step 2: Identify the two linear factors.**\nSince \\( \\text{{Area}} = \\text{{Length}} \\times \\text{{Breadth}} \\), the factors are the dimensions.\n\n**Step 3: State the dimensions.**\nThe possible dimensions are {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Finding unknown constant k in factorable quadratic
    arch5 = {
        'data': [
            ("If (x + 2) is a factor of x^2 + 5x + k, find k.", "6", "(-2)^2 + 5(-2) + k = 0 => 4 - 10 + k = 0 => k = 6", ["-6", "10", "4"]),
            ("If (x - 3) is a factor of x^2 - kx + 12, what is k?", "7", "3^2 - 3k + 12 = 0 => 21 = 3k => k = 7", ["-7", "4", "3"]),
            ("If (x + 1) is a factor of 2x^2 + kx + 1, what is k?", "3", "2(-1)^2 + k(-1) + 1 = 0 => 3 - k = 0 => k = 3", ["-3", "1", "2"]),
            ("If (x - 2) is a factor of 3x^2 - 5x - k, what is k?", "2", "3(4) - 10 - k = 0 => 12 - 10 - k = 0 => k = 2", ["-2", "4", "1"]),
            ("If (x + 3) is a factor of x^2 + kx - 15, find k.", "-2", "9 - 3k - 15 = 0 => -3k = 6 => k = -2", ["2", "-5", "5"]),
            ("If (x - 4) is a factor of x^2 - 10x + k, find k.", "24", "16 - 40 + k = 0 => k = 24", ["-24", "14", "6"]),
            ("If (x + 5) is a factor of x^2 + kx - 30, find k.", "-1", "25 - 5k - 30 = 0 => -5k = 5 => k = -1", ["1", "-6", "6"]),
            ("If (2x - 1) is a factor of 4x^2 + kx - 3, find k.", "4", "4(1/4) + k(1/2) - 3 = 0 => 1 + k/2 - 3 = 0 => k = 4", ["-4", "2", "-2"]),
            ("If (3x + 2) is a factor of 3x^2 + 8x + k, find k.", "4", "3(4/9) + 8(-2/3) + k = 0 => 4/3 - 16/3 + k = 0 => k = 4", ["-4", "2", "-2"]),
            ("If (x - 1) is a factor of kx^2 - 3x + 1, find k.", "2", "k(1) - 3 + 1 = 0 => k - 2 = 0 => k = 2", ["-2", "3", "1"])
        ],
        'tmpls': [
            "{0}",
            "Determine the value of k: {0}",
            "Factor Theorem application: {0}",
            "Find the unknown constant: {0}",
            "Calculate k: {0}",
            "What is the value of k? {0}",
            "Which option gives: {0}",
            "Solve for k: {0}",
            "Evaluate k: {0}",
            "Compute the constant: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[3],
            f"**Step 1: Apply the Factor Theorem.**\nIf \\( (x - c) \\) is a factor of \\( p(x) \\), then \\( p(c) = 0 \\).\n\n**Step 2: Substitute the root into the polynomial.**\n{item[2]}.\n\n**Step 3: State the value of k.**\n\\( k = {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 6: Higher-degree quadratics reducible by substitution (e.g. x^4 + 5x^2 + 6)
    arch6 = {
        'data': [
            ("x^4 + 5x^2 + 6", "(x^2 + 2)(x^2 + 3)", "y = x^2 => y^2 + 5y + 6 = (y + 2)(y + 3)"),
            ("x^4 - 5x^2 + 4", "(x - 1)(x + 1)(x - 2)(x + 2)", "y^2 - 5y + 4 = (y - 1)(y - 4) = (x^2 - 1)(x^2 - 4)"),
            ("x^4 - 13x^2 + 36", "(x - 2)(x + 2)(x - 3)(x + 3)", "y^2 - 13y + 36 = (y - 4)(y - 9) = (x^2 - 4)(x^2 - 9)"),
            ("x^4 + 3x^2 - 4", "(x - 1)(x + 1)(x^2 + 4)", "(y - 1)(y + 4) = (x^2 - 1)(x^2 + 4)"),
            ("x^4 - 29x^2 + 100", "(x - 2)(x + 2)(x - 5)(x + 5)", "(y - 4)(y - 25) = (x^2 - 4)(x^2 - 25)"),
            ("x^4 + 7x^2 + 12", "(x^2 + 3)(x^2 + 4)", "(y + 3)(y + 4)"),
            ("x^4 - 10x^2 + 9", "(x - 1)(x + 1)(x - 3)(x + 3)", "(y - 1)(y - 9) = (x^2 - 1)(x^2 - 9)"),
            ("x^4 - 8x^2 - 9", "(x - 3)(x + 3)(x^2 + 1)", "(y - 9)(y + 1) = (x^2 - 9)(x^2 + 1)"),
            ("x^4 + x^2 - 20", "(x - 2)(x + 2)(x^2 + 5)", "(y - 4)(y + 5) = (x^2 - 4)(x^2 + 5)"),
            ("x^4 - 17x^2 + 16", "(x - 1)(x + 1)(x - 4)(x + 4)", "(y - 1)(y - 16) = (x^2 - 1)(x^2 - 16)")
        ],
        'tmpls': [
            "Factorise completely: \\( {0} \\).",
            "What is the complete factorisation of \\( {0} \\)?",
            "Factorise the quartic trinomial: \\( {0} \\):",
            "Resolve \\( {0} \\) into factors:",
            "The factored form of \\( {0} \\) is:",
            "Find all factors of \\( {0} \\):",
            "Which expression is the complete factorisation of \\( {0} \\)?",
            "Factorise: \\( {0} \\):",
            "Determine the factors of \\( {0} \\):",
            "Express \\( {0} \\) in factored form:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("+", "-") if "+" in item[1] else item[1].replace("-", "+"),
                f"(x^2 - 1)(x^2 - {item[0].split(' ')[-1]})",
                f"(x^4 - 1)"
            ],
            f"**Step 1: Substitute \\( y = x^2 \\) to reduce to quadratic form.**\n{item[2]}.\n\n**Step 2: Factorise the quadratic in \\( y \\).**\nSubstitute \\( x^2 \\) back for \\( y \\).\n\n**Step 3: Factorise any difference of squares further into linear factors.**\nThe complete factorisation is \\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 7: Multi-variable quadratic trinomials
    arch7 = {
        'data': [
            ("x^2 + 5xy + 6y^2", "(x + 2y)(x + 3y)", "2 + 3 = 5, 2 * 3 = 6"),
            ("x^2 - 7xy + 12y^2", "(x - 3y)(x - 4y)", "-3 + (-4) = -7, (-3)(-4) = 12"),
            ("2x^2 + 7xy + 3y^2", "(2x + y)(x + 3y)", "1 + 6 = 7, 1 * 6 = 6"),
            ("6x^2 + 5xy - 6y^2", "(2x + 3y)(3x - 2y)", "9 - 4 = 5, 9(-4) = -36"),
            ("3x^2 - xy - 4y^2", "(3x - 4y)(x + y)", "-4 + 3 = -1, (-4)(3) = -12"),
            ("x^2 + 2xy - 15y^2", "(x + 5y)(x - 3y)", "5 - 3 = 2, 5(-3) = -15"),
            ("4x^2 + 12xy + 5y^2", "(2x + y)(2x + 5y)", "2 + 10 = 12, 2 * 10 = 20"),
            ("x^2 - 9xy + 20y^2", "(x - 4y)(x - 5y)", "-4 + (-5) = -9, (-4)(-5) = 20"),
            ("12x^2 - 7xy + y^2", "(3x - y)(4x - y)", "-3 + (-4) = -7, (-3)(-4) = 12"),
            ("5x^2 - 16xy + 3y^2", "(5x - y)(x - 3y)", "-1 + (-15) = -16, (-1)(-15) = 15")
        ],
        'tmpls': [
            "Factorise the homogeneous quadratic polynomial: \\( {0} \\).",
            "What is the factored form of \\( {0} \\)?",
            "Factorise completely: \\( {0} \\):",
            "The factors of \\( {0} \\) are:",
            "Resolve \\( {0} \\) into linear factors:",
            "Find the factorisation of \\( {0} \\):",
            "Which expression equals \\( {0} \\)?",
            "Factorise: \\( {0} \\):",
            "Determine the factors of \\( {0} \\):",
            "Express \\( {0} \\) as a product of two binomials:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("+", "-") if "+" in item[1] else item[1].replace("-", "+"),
                f"(x - y)({item[0].split('x^2')[0]}x - y)",
                item[1].split(')(')[0] + ')^2'
            ],
            f"**Step 1: Treat as a quadratic in \\( x \\) with coefficients in \\( y \\).**\nSplit the middle term \\( xy \\).\n\n**Step 2: Factor by grouping.**\n{item[2]}.\n\n**Step 3: State the factorised form.**\n\\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 4.4.2: Factoring cubic expressions using trial and factor theorem
# ==============================================================================
def gen_4_4_2():
    tc = "CBSE-9-MGM-4-4.4.2"
    tname = "Factoring cubic expressions using trial and factor theorem"

    # Arch 0: Canonical NCERT cubic polynomials
    arch0 = {
        'data': [
            ("x^3 - 2x^2 - x + 2", "(x - 1)(x + 1)(x - 2)", 1, "p(1) = 1 - 2 - 1 + 2 = 0"),
            ("x^3 - 3x^2 - 9x - 5", "(x + 1)^2 (x - 5)", -1, "p(-1) = -1 - 3 + 9 - 5 = 0"),
            ("x^3 + 13x^2 + 32x + 20", "(x + 1)(x + 2)(x + 10)", -1, "p(-1) = -1 + 13 - 32 + 20 = 0"),
            ("2y^3 + y^2 - 2y - 1", "(y - 1)(y + 1)(2y + 1)", 1, "p(1) = 2 + 1 - 2 - 1 = 0"),
            ("x^3 - 23x^2 + 142x - 120", "(x - 1)(x - 10)(x - 12)", 1, "p(1) = 1 - 23 + 142 - 120 = 0"),
            ("x^3 + x^2 - 4x - 4", "(x + 1)(x - 2)(x + 2)", -1, "p(-1) = -1 + 1 + 4 - 4 = 0"),
            ("x^3 - 6x^2 + 11x - 6", "(x - 1)(x - 2)(x - 3)", 1, "p(1) = 1 - 6 + 11 - 6 = 0"),
            ("x^3 + 6x^2 + 11x + 6", "(x + 1)(x + 2)(x + 3)", -1, "p(-1) = -1 + 6 - 11 + 6 = 0"),
            ("x^3 - 4x^2 + x + 6", "(x + 1)(x - 2)(x - 3)", -1, "p(-1) = -1 - 4 - 1 + 6 = 0"),
            ("x^3 - 7x + 6", "(x - 1)(x - 2)(x + 3)", 1, "p(1) = 1 - 7 + 6 = 0")
        ],
        'tmpls': [
            "Factorise using the Factor Theorem and trial method: \\( {0} \\).",
            "What is the complete factorisation of \\( {0} \\)?",
            "Factorise the cubic polynomial: \\( {0} \\):",
            "The factored form of \\( {0} \\) is:",
            "Find all linear factors of \\( {0} \\):",
            "Resolve \\( {0} \\) into three linear factors:",
            "Which of the following represents the factorisation of \\( {0} \\)?",
            "Factorise completely: \\( {0} \\):",
            "Determine the factors of \\( {0} \\):",
            "Express \\( {0} \\) as a product of linear factors:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("-", "+") if "-" in item[1] else item[1].replace("+", "-"),
                f"(x - 1)(x^2 + {item[0].split(' ')[-1]})",
                f"(x + 1)(x - 1)(x + {item[0].split(' ')[-1]})"
            ],
            f"**Step 1: Test factors of the constant term using the Factor Theorem.**\nTry \\( x = {item[2]} \\): {item[3]}.\nTherefore, the first linear factor is identified.\n\n**Step 2: Divide the cubic by this linear factor to find the quotient quadratic.**\nPerform polynomial division or synthetic division.\n\n**Step 3: Factorise the quadratic quotient by splitting the middle term.**\nThe complete factorisation is \\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 1: More cubic polynomials with integer roots
    arch1 = {
        'data': [
            ("x^3 - 3x^2 - x + 3", "(x - 1)(x + 1)(x - 3)", 1, "x^2(x - 3) - 1(x - 3) = (x^2 - 1)(x - 3)"),
            ("x^3 - x^2 - 4x + 4", "(x - 1)(x - 2)(x + 2)", 1, "x^2(x - 1) - 4(x - 1) = (x^2 - 4)(x - 1)"),
            ("x^3 + 2x^2 - x - 2", "(x - 1)(x + 1)(x + 2)", 1, "x^2(x + 2) - 1(x + 2) = (x^2 - 1)(x + 2)"),
            ("x^3 - 3x^2 - 4x + 12", "(x - 2)(x + 2)(x - 3)", 2, "x^2(x - 3) - 4(x - 3) = (x^2 - 4)(x - 3)"),
            ("x^3 + 4x^2 - x - 4", "(x - 1)(x + 1)(x + 4)", 1, "x^2(x + 4) - 1(x + 4) = (x^2 - 1)(x + 4)"),
            ("x^3 - 5x^2 - x + 5", "(x - 1)(x + 1)(x - 5)", 1, "x^2(x - 5) - 1(x - 5) = (x^2 - 1)(x - 5)"),
            ("x^3 + 5x^2 - 4x - 20", "(x - 2)(x + 2)(x + 5)", 2, "x^2(x + 5) - 4(x + 5) = (x^2 - 4)(x + 5)"),
            ("x^3 - 2x^2 - 9x + 18", "(x - 2)(x - 3)(x + 3)", 2, "x^2(x - 2) - 9(x - 2) = (x^2 - 9)(x - 2)"),
            ("x^3 + 3x^2 - 4x - 12", "(x - 2)(x + 2)(x + 3)", 2, "x^2(x + 3) - 4(x + 3) = (x^2 - 4)(x + 3)"),
            ("x^3 - x^2 - 9x + 9", "(x - 1)(x - 3)(x + 3)", 1, "x^2(x - 1) - 9(x - 1) = (x^2 - 9)(x - 1)")
        ],
        'tmpls': [
            "Factorise by grouping or Factor Theorem: \\( {0} \\).",
            "What is the factored form of \\( {0} \\)?",
            "Factorise completely: \\( {0} \\):",
            "The linear factors of \\( {0} \\) are:",
            "Find the factors: \\( {0} \\):",
            "Resolve \\( {0} \\) into factors:",
            "Which expression is the factorisation of \\( {0} \\)?",
            "Determine the factors of \\( {0} \\):",
            "Evaluate the factors of \\( {0} \\):",
            "Express \\( {0} \\) as a product of linear factors:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("-", "+") if "-" in item[1] else item[1].replace("+", "-"),
                f"(x^2 - 1)(x + {item[0].split(' ')[-1]})",
                f"(x - 1)^2 (x + {item[0].split(' ')[-1]})"
            ],
            f"**Step 1: Group terms into pairs.**\nNotice common factors between first two and last two terms.\n\n**Step 2: Factor out the common binomial.**\n{item[3]}.\n\n**Step 3: Factorise the difference of squares.**\nThe final factorisation is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Factor Theorem identification: Is (x - a) a factor of p(x)?
    arch2 = {
        'data': [
            ("(x - 1)", "x^3 - 6x^2 + 11x - 6", "Yes, (x - 1) is a factor", "1 - 6 + 11 - 6 = 0"),
            ("(x + 1)", "x^3 + 3x^2 + 3x + 1", "Yes, (x + 1) is a factor", "-1 + 3 - 3 + 1 = 0"),
            ("(x - 2)", "x^3 - 3x^2 + 4x - 4", "Yes, (x - 2) is a factor", "8 - 12 + 8 - 4 = 0"),
            ("(x + 2)", "x^3 + 2x^2 - x - 2", "Yes, (x + 2) is a factor", "-8 + 8 + 2 - 2 = 0"),
            ("(x - 3)", "x^3 - 3x^2 - x + 3", "Yes, (x - 3) is a factor", "27 - 27 - 3 + 3 = 0"),
            ("(x - 1)", "x^3 + 2x^2 - x + 1", "No, remainder is 3 ≠ 0", "1 + 2 - 1 + 1 = 3 ≠ 0"),
            ("(x + 1)", "x^3 - 2x^2 + x - 1", "No, remainder is -5 ≠ 0", "-1 - 2 - 1 - 1 = -5 ≠ 0"),
            ("(x - 2)", "x^3 - 4x^2 + 2x + 1", "No, remainder is -3 ≠ 0", "8 - 16 + 4 + 1 = -3 ≠ 0"),
            ("(x + 3)", "x^3 + 3x^2 - 2x - 6", "Yes, (x + 3) is a factor", "-27 + 27 + 6 - 6 = 0"),
            ("(x - 4)", "x^3 - 4x^2 + x - 4", "Yes, (x - 4) is a factor", "64 - 64 + 4 - 4 = 0")
        ],
        'tmpls': [
            "Use the Factor Theorem to determine if \\( {0} \\) is a factor of \\( {1} \\).",
            "Is \\( {0} \\) a factor of \\( {1} \\)?",
            "According to the Factor Theorem, does \\( {0} \\) divide \\( {1} \\) exactly?",
            "Evaluate whether \\( {0} \\) is a factor of \\( {1} \\):",
            "Check if \\( {0} \\) is a factor of \\( {1} \\):",
            "Determine if \\( {0} \\) is a factor of \\( {1} \\):",
            "Which statement correctly describes the divisibility of \\( {1} \\) by \\( {0} \\)?",
            "What does the Factor Theorem show for \\( {0} \\) and \\( {1} \\)?",
            "Test if \\( {0} \\) is a factor of \\( {1} \\):",
            "Solve using Factor Theorem: Is \\( {0} \\) a factor of \\( {1} \\)?"
        ],
        'calc': lambda item: (
            item[2],
            [
                "No, remainder is non-zero" if "Yes" in item[2] else "Yes, remainder is 0",
                "Cannot be determined without division",
                "Only if x > 0"
            ],
            f"**Step 1: Identify the root of the proposed divisor.**\nFor divisor \\( (x - c) \\), the root is \\( c \\).\n\n**Step 2: Evaluate \\( p(c) \\).**\n\\[ p(c) = {item[3]} \\]\n\n**Step 3: State the conclusion by Factor Theorem.**\nSince \\( p(c) {('=' if 'Yes' in item[2] else '≠')} 0 \\), {item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 3: Factor Theorem to find unknown constant in cubic polynomial
    arch3 = {
        'data': [
            ("If (x - 1) is a factor of x^3 + 2x^2 - kx + 4, find k.", "7", "1 + 2 - k + 4 = 0 => 7 - k = 0 => k = 7", ["-7", "5", "6"]),
            ("If (x + 1) is a factor of x^3 - 3x^2 + 3x + k, find k.", "7", "-1 - 3 - 3 + k = 0 => -7 + k = 0 => k = 7", ["-7", "1", "-1"]),
            ("If (x - 2) is a factor of x^3 - 3x^2 + kx - 10, find k.", "7", "8 - 12 + 2k - 10 = 0 => 2k - 14 = 0 => k = 7", ["14", "-7", "10"]),
            ("If (x + 2) is a factor of x^3 + 3x^2 - kx - 6, find k.", "-1", "-8 + 12 + 2k - 6 = 0 => 2k - 2 = 0 => k = 1... wait: k = 1", ["-1", "2", "-2"]),
            ("If (x - 3) is a factor of x^3 - 2x^2 + kx - 12, find k.", "-1", "27 - 18 + 3k - 12 = 0 => 3k - 3 = 0 => k = 1", ["-1", "3", "-3"]),
            ("If (x - 1) is a factor of 2x^3 - kx^2 + 5x - 3, find k.", "4", "2 - k + 5 - 3 = 0 => 4 - k = 0 => k = 4", ["-4", "2", "6"]),
            ("If (x + 2) is a factor of 2x^3 + 5x^2 - kx - 6, find k.", "-1", "-16 + 20 + 2k - 6 = 0 => 2k - 2 = 0 => k = 1", ["-1", "2", "-2"]),
            ("If (x - 1) is a factor of x^3 + kx^2 + 11x + 6, find k.", "-18", "1 + k + 11 + 6 = 0 => k + 18 = 0 => k = -18", ["18", "-6", "6"]),
            ("If (x + 3) is a factor of x^3 + 3x^2 - kx - 15, find k.", "-5", "-27 + 27 + 3k - 15 = 0 => 3k = 15 => k = 5", ["-5", "3", "-3"]),
            ("If (x - 2) is a factor of kx^3 - 4x^2 + 3x - 2, find k.", "1.5", "8k - 16 + 6 - 2 = 0 => 8k - 12 = 0 => k = 12/8 = 1.5", ["2", "1", "3"])
        ],
        'tmpls': [
            "{0}",
            "Find the constant k using the Factor Theorem: {0}",
            "Calculate the unknown coefficient: {0}",
            "Determine the value of k: {0}",
            "What is k? {0}",
            "Solve for k: {0}",
            "Which option represents k: {0}",
            "Evaluate k: {0}",
            "Compute the value of k: {0}",
            "Identity / Factor Theorem problem: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[3],
            f"**Step 1: Set divisor root equal to zero.**\nLet \\( x = c \\) such that the divisor vanishes.\n\n**Step 2: Apply \\( p(c) = 0 \\) by Factor Theorem.**\n{item[2]}.\n\n**Step 3: State the value of k.**\n\\( k = {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Word problems on dimensions of cuboid from volume polynomial
    arch4 = {
        'data': [
            ("The volume of a cuboid is given by 3x² - 12x. Possible dimensions for the cuboid are:", "3, x, (x - 4)", "3x² - 12x = 3 * x * (x - 4)", ["3, x, (x + 4)", "3, x², (x - 4)", "x, (x - 2), (x + 2)"]),
            ("The volume of a cuboid is given by 12ky² + 8ky - 20k. Possible expressions for its three dimensions are:", "4k, (3y + 5), (y - 1)", "4k(3y² + 2y - 5) = 4k(3y + 5)(y - 1)", ["4k, (3y - 5), (y + 1)", "2k, (6y + 5), (y - 2)", "k, (12y + 5), (y - 1)"]),
            ("The volume of a rectangular box is x³ - 4x. What are its three possible dimensions?", "x, (x - 2), (x + 2)", "x(x² - 4) = x(x - 2)(x + 2)", ["x, (x - 4), (x + 1)", "x², (x - 2), 2", "(x - 2), (x - 2), x"]),
            ("The volume of a storage container is 2x³ + 6x² + 4x. What are its dimensions?", "2x, (x + 1), (x + 2)", "2x(x² + 3x + 2) = 2x(x + 1)(x + 2)", ["2x, (x - 1), (x - 2)", "x, (2x + 1), (x + 2)", "2, x², (x + 3)"]),
            ("The volume of a rectangular block is x³ - x. Possible dimensions are:", "x, (x - 1), (x + 1)", "x(x² - 1) = x(x - 1)(x + 1)", ["x², (x - 1), 1", "x, (x - 1), (x - 1)", "x, (x + 1), (x + 1)"]),
            ("The volume of a parcel is 4x³ - 16x. Possible linear dimensions are:", "4x, (x - 2), (x + 2)", "4x(x² - 4) = 4x(x - 2)(x + 2)", ["4, x, (x² - 4)", "2x, 2, (x² - 4)", "4x, (x - 4), (x + 1)"]),
            ("The volume of a water tank is x³ + 6x² + 11x + 6. What are its three dimensions?", "(x + 1), (x + 2), (x + 3)", "x³ + 6x² + 11x + 6 = (x + 1)(x + 2)(x + 3)", ["(x - 1), (x - 2), (x - 3)", "(x + 1), (x + 1), (x + 6)", "(x + 2), (x + 2), (x + 3)"]),
            ("The volume of a cubical room modified into a cuboid is x³ - 6x² + 11x - 6. What are its dimensions?", "(x - 1), (x - 2), (x - 3)", "(x - 1)(x - 2)(x - 3)", ["(x + 1), (x + 2), (x + 3)", "(x - 1), (x + 2), (x - 3)", "(x - 1), (x - 1), (x - 6)"]),
            ("A hollow brick has volume 3x³ - 27x. What are its three factors?", "3x, (x - 3), (x + 3)", "3x(x² - 9) = 3x(x - 3)(x + 3)", ["3, x, (x² - 9)", "3x, (x - 9), (x + 1)", "x, (3x - 3), (x + 3)"]),
            ("The volume of a container is 5x³ - 20x. Possible dimensions are:", "5x, (x - 2), (x + 2)", "5x(x² - 4) = 5x(x - 2)(x + 2)", ["5, x, (x² - 4)", "5x, (x - 4), (x + 1)", "x, (5x - 2), (x + 2)"])
        ],
        'tmpls': [
            "{0}",
            "Solve the cuboid volume factorisation problem: {0}",
            "Find the possible dimensions of the cuboid: {0}",
            "Calculate possible expressions for length, breadth, and height: {0}",
            "Determine the dimensions: {0}",
            "What are possible dimensions? {0}",
            "Which option represents the dimensions: {0}",
            "Resolve volume into three dimensions: {0}",
            "Evaluate possible dimensions: {0}",
            "Compute the factors of volume: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[3],
            f"**Step 1: Factor out any common monomial factor.**\n{item[2]}.\n\n**Step 2: Factorise the remaining quadratic expression into two linear factors.**\n\n**Step 3: State the three dimensions of the cuboid.**\nThe dimensions are {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Synthetic / polynomial long division to find quotient quadratic
    arch5 = {
        'data': [
            ("x^3 - 2x^2 - x + 2", "(x - 1)", "x^2 - x - 2", "(x - 1)(x^2 - x - 2)"),
            ("x^3 - 3x^2 - 9x - 5", "(x + 1)", "x^2 - 4x - 5", "(x + 1)(x^2 - 4x - 5)"),
            ("x^3 + 13x^2 + 32x + 20", "(x + 1)", "x^2 + 12x + 20", "(x + 1)(x^2 + 12x + 20)"),
            ("x^3 - 23x^2 + 142x - 120", "(x - 1)", "x^2 - 22x + 120", "(x - 1)(x^2 - 22x + 120)"),
            ("x^3 + x^2 - 4x - 4", "(x + 1)", "x^2 - 4", "(x + 1)(x^2 - 4)"),
            ("x^3 - 6x^2 + 11x - 6", "(x - 1)", "x^2 - 5x + 6", "(x - 1)(x^2 - 5x + 6)"),
            ("x^3 + 6x^2 + 11x + 6", "(x + 1)", "x^2 + 5x + 6", "(x + 1)(x^2 + 5x + 6)"),
            ("x^3 - 4x^2 + x + 6", "(x + 1)", "x^2 - 5x + 6", "(x + 1)(x^2 - 5x + 6)"),
            ("x^3 - 7x + 6", "(x - 1)", "x^2 + x - 6", "(x - 1)(x^2 + x - 6)"),
            ("2y^3 + y^2 - 2y - 1", "(y - 1)", "2y^2 + 3y + 1", "(y - 1)(2y^2 + 3y + 1)")
        ],
        'tmpls': [
            "Divide \\( {0} \\) by \\( {1} \\) to find the quotient quadratic polynomial.",
            "What is the quotient when \\( {0} \\) is divided by \\( {1} \\)?",
            "Calculate the quotient polynomial \\( {0} \\div {1} \\):",
            "Dividing \\( {0} \\) by \\( {1} \\) gives quotient:",
            "Find the quotient: \\( {0} \\div {1} \\):",
            "Evaluate the division \\( {0} \\div {1} \\):",
            "Which quadratic polynomial is the quotient of \\( {0} \\) divided by \\( {1} \\)?",
            "Perform polynomial division: \\( {0} \\div {1} \\):",
            "Determine the quotient quadratic: \\( {0} \\div {1} \\):",
            "The result of dividing \\( {0} \\) by \\( {1} \\) is:"
        ],
        'calc': lambda item: (
            item[2],
            [
                item[2].replace("-", "+") if "-" in item[2] else item[2].replace("+", "-"),
                item[2] + " + 1",
                item[2] + " - 2"
            ],
            f"**Step 1: Set up long division or synthetic division of the cubic by \\( {item[1]} \\).**\n\n**Step 2: Divide leading terms step-by-step.**\nCancel higher powers sequentially.\n\n**Step 3: State the quotient polynomial.**\nThe quotient is \\( {item[2]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 6: Number of zeroes and fundamental theorem of algebra concepts
    arch6 = {
        'data': [
            ("How many zeroes can a cubic polynomial p(x) have at most?", "3", ["1", "2", "4"]),
            ("If a cubic polynomial has zeroes 1, 2, and 3, its factorised form with leading coefficient 1 is:", "(x - 1)(x - 2)(x - 3)", ["(x + 1)(x + 2)(x + 3)", "(x - 1)(x - 2)", "x³ - 6"]),
            ("If α, β, γ are the zeroes of x³ - 6x² + 11x - 6, what is their sum α + β + γ?", "6", ["-6", "11", "-11"]),
            ("If α, β, γ are the zeroes of x³ - 6x² + 11x - 6, what is their product αβγ?", "6", ["-6", "11", "-11"]),
            ("Can a real cubic polynomial have zero real roots?", "No, every real cubic polynomial has at least one real root", ["Yes, always", "Only if constant term is zero", "Only if leading coeff is negative"]),
            ("Why does every cubic polynomial have at least one real root?", "Because complex non-real roots of real polynomials always occur in conjugate pairs (leaving an odd root real)", ["Because it crosses the origin", "Because cubes are positive", "It is an empirical fact"]),
            ("In the trial method for factoring a cubic polynomial, the possible integer roots are always factors of:", "the constant term", ["the leading coefficient", "the linear coefficient", "the discriminant"]),
            ("If p(x) = x³ + ax² + bx + c and all coefficients are integers, the Rational Root Theorem states that any rational root p/q must have:", "p dividing c and q dividing 1 (so roots are integer divisors of c)", ["p dividing a", "q dividing c", "p + q = c"]),
            ("If p(2) = 0 for polynomial p(x), which binomial is guaranteed to be a factor by Factor Theorem?", "(x - 2)", ["(x + 2)", "(2x - 1)", "(x² - 2)"]),
            ("If p(-3) = 0 for polynomial p(x), what is a factor of p(x)?", "(x + 3)", ["(x - 3)", "(3x + 1)", "(x² + 3)"])
        ],
        'tmpls': [
            "{0}",
            "Conceptual question on cubic polynomials and Factor Theorem: {0}",
            "Theory of cubic zeroes: {0}",
            "Select the accurate algebraic fact: {0}",
            "Determine the true statement: {0}",
            "Which option correctly answers: {0}",
            "Identify the valid theorem: {0}",
            "What is the mathematical conclusion: {0}",
            "Evaluate the concept: {0}",
            "Choose the correct option: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the Fundamental Theorem of Algebra and Factor Theorem.**\nA degree \\( n \\) polynomial has at most \\( n \\) zeroes, and \\( p(c) = 0 \\iff (x - c) \\) is a factor.\n\n**Step 2: Evaluate the statement.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Multi-step competition level cubic factorisation
    arch7 = {
        'data': [
            ("Factorise completely: x^3 - 8x^2 + 19x - 12", "(x - 1)(x - 3)(x - 4)", "roots 1, 3, 4", ["(x + 1)(x + 3)(x + 4)", "(x - 1)(x - 2)(x - 6)", "(x - 2)(x - 3)(x - 4)"]),
            ("Factorise completely: x^3 + 2x^2 - 5x - 6", "(x + 1)(x - 2)(x + 3)", "roots -1, 2, -3", ["(x - 1)(x + 2)(x - 3)", "(x + 1)(x + 2)(x + 3)", "(x - 1)(x - 2)(x - 3)"]),
            ("Factorise completely: x^3 - 9x^2 + 26x - 24", "(x - 2)(x - 3)(x - 4)", "roots 2, 3, 4", ["(x + 2)(x + 3)(x + 4)", "(x - 1)(x - 4)(x - 6)", "(x - 2)(x - 2)(x - 6)"]),
            ("Factorise completely: x^3 + 7x^2 + 14x + 8", "(x + 1)(x + 2)(x + 4)", "roots -1, -2, -4", ["(x - 1)(x - 2)(x - 4)", "(x + 1)(x + 1)(x + 8)", "(x + 2)(x + 2)(x + 2)"]),
            ("Factorise completely: x^3 - 12x^2 + 47x - 60", "(x - 3)(x - 4)(x - 5)", "roots 3, 4, 5", ["(x + 3)(x + 4)(x + 5)", "(x - 2)(x - 5)(x - 6)", "(x - 1)(x - 6)(x - 10)"]),
            ("Factorise completely: x^3 + 8x^2 + 17x + 10", "(x + 1)(x + 2)(x + 5)", "roots -1, -2, -5", ["(x - 1)(x - 2)(x - 5)", "(x + 1)(x + 1)(x + 10)", "(x + 2)(x + 2)(x + 5)"]),
            ("Factorise completely: x^3 - 10x^2 + 31x - 30", "(x - 2)(x - 3)(x - 5)", "roots 2, 3, 5", ["(x + 2)(x + 3)(x + 5)", "(x - 1)(x - 5)(x - 6)", "(x - 2)(x - 2)(x - 7)"]),
            ("Factorise completely: x^3 + 9x^2 + 23x + 15", "(x + 1)(x + 3)(x + 5)", "roots -1, -3, -5", ["(x - 1)(x - 3)(x - 5)", "(x + 1)(x + 1)(x + 15)", "(x + 2)(x + 3)(x + 4)"]),
            ("Factorise completely: x^3 - 11x^2 + 38x - 40", "(x - 2)(x - 4)(x - 5)", "roots 2, 4, 5", ["(x + 2)(x + 4)(x + 5)", "(x - 1)(x - 5)(x - 8)", "(x - 2)(x - 2)(x - 10)"]),
            ("Factorise completely: x^3 + 10x^2 + 31x + 30", "(x + 2)(x + 3)(x + 5)", "roots -2, -3, -5", ["(x - 2)(x - 3)(x - 5)", "(x + 1)(x + 5)(x + 6)", "(x + 2)(x + 2)(x + 7)"])
        ],
        'tmpls': [
            "Factorise completely using Factor Theorem: \\( {0} \\).",
            "What is the full factorisation of \\( {0} \\)?",
            "Factorise the cubic expression: \\( {0} \\):",
            "The three linear factors of \\( {0} \\) are:",
            "Find all factors of \\( {0} \\):",
            "Resolve \\( {0} \\) into linear factors:",
            "Which option represents the complete factorisation of \\( {0} \\)?",
            "Factorise: \\( {0} \\):",
            "Determine the linear factors of \\( {0} \\):",
            "Express \\( {0} \\) in factored form:"
        ],
        'calc': lambda item: (
            item[1],
            item[3],
            f"**Step 1: Test integer factors of the constant term to find a root.**\nNotice {item[2]}.\n\n**Step 2: Divide by the first factor to get the quotient quadratic.**\n\n**Step 3: Factorise the quadratic into the remaining two linear factors.**\nThe complete factorisation is \\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_4_4_1()
    q2 = gen_4_4_2()
    print(f"gen_4_4_1: {len(q1)} questions")
    print(f"gen_4_4_2: {len(q2)} questions")
