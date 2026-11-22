# scripts/build_cbse9_mgm_ch3_part4.py
# Subtopics:
# 3.4.1: Fractional exponents a^(p/q) (80 Qs)
# 3.4.2: Laws of exponents: a^p * a^q = a^(p+q), (a^p)^q = a^(pq), a^p/a^q = a^(p-q), a^p * b^p = (ab)^p (80 Qs)

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 3
CH_NAME = "The World of Numbers"

# ==============================================================================
# SUBTOPIC 3.4.1: Fractional exponents a^(p/q)
# ==============================================================================
def gen_3_4_1():
    tc = "CBSE-9-MGM-3-3.4.1"
    tname = "Fractional exponents a^(p/q)"

    # Arch 0: Unit fractional powers a^(1/n) = n-th root
    arch0 = {
        'data': [
            ("64^{1/2}", "8", 64, 2),
            ("32^{1/5}", "2", 32, 5),
            ("125^{1/3}", "5", 125, 3),
            ("81^{1/4}", "3", 81, 4),
            ("16^{1/4}", "2", 16, 4),
            ("27^{1/3}", "3", 27, 3),
            ("49^{1/2}", "7", 49, 2),
            ("100^{1/2}", "10", 100, 2),
            ("216^{1/3}", "6", 216, 3),
            ("64^{1/3}", "4", 64, 3)
        ],
        'tmpls': [
            "Find the value of \\( {0} \\).",
            "Evaluate \\( {0} \\):",
            "What is the numerical value of \\( {0} \\)?",
            "Calculate \\( {0} \\):",
            "Determine the result of \\( {0} \\):",
            "The expression \\( {0} \\) equals:",
            "Compute \\( {0} \\):",
            "Simplify: \\( {0} \\):",
            "Find the {3}-th root of {2} expressed as \\( {0} \\):",
            "What does \\( {0} \\) simplify to?"
        ],
        'calc': lambda item: (
            item[1],
            [
                str(int(item[1]) + 2),
                str(int(item[1]) - 1),
                str(int(item[1]) * 2)
            ],
            f"**Step 1: Write the base as a prime power.**\nExpress \\( {item[2]} \\) as a base raised to the power {item[3]}.\n\\[ {item[2]} = ({item[1]})^{{{item[3]}}} \\]\n\n**Step 2: Apply the power of a power rule.**\n\\[ ({item[1]}^{{{item[3]}}})^{{1/{item[3]}}} = {item[1]}^{{{item[3]} \\times (1/{item[3]})}} = {item[1]}^1 \\]\n\n**Step 3: State the evaluated value.**\nThe value is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: General fractional powers a^(m/n)
    arch1 = {
        'data': [
            ("9^{3/2}", "27", 9, 3, 2),
            ("32^{2/5}", "4", 32, 2, 5),
            ("16^{3/4}", "8", 16, 3, 4),
            ("27^{2/3}", "9", 27, 2, 3),
            ("125^{2/3}", "25", 125, 2, 3),
            ("64^{2/3}", "16", 64, 2, 3),
            ("8^{5/3}", "32", 8, 5, 3),
            ("81^{3/4}", "27", 81, 3, 4),
            ("32^{3/5}", "8", 32, 3, 5),
            ("4^{3/2}", "8", 4, 3, 2)
        ],
        'tmpls': [
            "Find the value of \\( {0} \\).",
            "Evaluate the expression \\( {0} \\):",
            "What is the numerical value of \\( {0} \\)?",
            "Calculate \\( {0} \\):",
            "Determine the result of \\( {0} \\):",
            "The expression \\( {0} \\) evaluates to:",
            "Compute \\( {0} \\):",
            "Simplify: \\( {0} \\):",
            "Find the value of \\( {0} \\) using laws of exponents:",
            "What does \\( {0} \\) equal?"
        ],
        'calc': lambda item: (
            item[1],
            [
                str(int(item[1]) + 4),
                str(int(item[1]) - 3),
                str(int(item[1]) * 2)
            ],
            f"**Step 1: Express base as a prime power.**\nExpress \\( {item[2]} \\) in terms of its root power.\n\n**Step 2: Multiply the exponents.**\n\\[ ({item[2]})^{{{item[3]}/{item[4]}}} = ({item[1]}^{{1/{item[3]}}})^{{{item[3]}}} = {item[1]} \\]\n\n**Step 3: State the final evaluated value.**\nThe value is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Negative fractional exponents a^(-p/q)
    arch2 = {
        'data': [
            ("125^{-1/3}", "1/5", 125, 1, 3),
            ("64^{-1/6}", "1/2", 64, 1, 6),
            ("27^{-2/3}", "1/9", 27, 2, 3),
            ("16^{-3/4}", "1/8", 16, 3, 4),
            ("32^{-1/5}", "1/2", 32, 1, 5),
            ("49^{-1/2}", "1/7", 49, 1, 2),
            ("81^{-1/4}", "1/3", 81, 1, 4),
            ("64^{-2/3}", "1/16", 64, 2, 3),
            ("8^{-2/3}", "1/4", 8, 2, 3),
            ("100^{-3/2}", "1/1000", 100, 3, 2)
        ],
        'tmpls': [
            "Find the value of \\( {0} \\).",
            "Evaluate the expression with negative fractional exponent \\( {0} \\):",
            "What is the numerical fraction value of \\( {0} \\)?",
            "Calculate \\( {0} \\):",
            "Determine the result of \\( {0} \\):",
            "The expression \\( {0} \\) evaluates to:",
            "Compute \\( {0} \\):",
            "Simplify: \\( {0} \\):",
            "Express \\( {0} \\) as an irreducible rational fraction:",
            "What fraction does \\( {0} \\) equal?"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"{item[1].split('/')[1]}",
                f"1/{int(item[1].split('/')[1]) + 2}",
                f"-{item[1]}"
            ],
            f"**Step 1: Apply negative exponent rule \\( a^{{-p}} = \\frac{{1}}{{a^p}} \\).**\n\\[ {item[0]} = \\frac{{1}}{{{item[2]}^{{{item[3]}/{item[4]}}}}} \\]\n\n**Step 2: Evaluate the positive power in the denominator.**\nEvaluate \\( {item[2]}^{{{item[3]}/{item[4]}}} \\).\n\n**Step 3: State the resulting fraction.**\nThe value is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Fractions raised to negative exponents (a/b)^(-p) = (b/a)^p
    arch3 = {
        'data': [
            ("\\left(\\frac{1}{216}\\right)^{-2/3}", "36", ["6", "1/36", "216"]),
            ("\\left(\\frac{81}{16}\\right)^{-3/4}", "\\frac{8}{27}", ["\\frac{27}{8}", "\\frac{16}{81}", "\\frac{4}{9}"]),
            ("\\left(\\frac{64}{25}\\right)^{-3/2}", "\\frac{125}{512}", ["\\frac{512}{125}", "\\frac{25}{64}", "\\frac{5}{8}"]),
            ("\\left(\\frac{1}{64}\\right)^{-1/2}", "8", ["4", "1/8", "64"]),
            ("\\left(\\frac{1}{32}\\right)^{-2/5}", "4", ["2", "1/4", "32"]),
            ("\\left(\\frac{25}{9}\\right)^{-3/2}", "\\frac{27}{125}", ["\\frac{125}{27}", "\\frac{9}{25}", "\\frac{3}{5}"]),
            ("\\left(\\frac{1}{125}\\right)^{-2/3}", "25", ["5", "1/25", "125"]),
            ("\\left(\\frac{16}{81}\\right)^{-1/4}", "\\frac{3}{2}", ["\\frac{2}{3}", "\\frac{81}{16}", "\\frac{9}{4}"]),
            ("\\left(\\frac{4}{9}\\right)^{-3/2}", "\\frac{27}{8}", ["\\frac{8}{27}", "\\frac{9}{4}", "\\frac{3}{2}"]),
            ("\\left(\\frac{1}{343}\\right)^{-2/3}", "49", ["7", "1/49", "343"])
        ],
        'tmpls': [
            "Evaluate \\( {0} \\).",
            "What is the value of \\( {0} \\)?",
            "Calculate the simplified value of \\( {0} \\):",
            "Simplify: \\( {0} \\):",
            "Determine the result of \\( {0} \\):",
            "The expression \\( {0} \\) simplifies to:",
            "Find the numerical value of \\( {0} \\):",
            "Compute \\( {0} \\):",
            "What fraction or integer does \\( {0} \\) equal?",
            "Evaluate the power: \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Invert base to eliminate negative sign in exponent.**\n\\[ \\left(\\frac{{a}}{{b}}\\right)^{{-p/q}} = \\left(\\frac{{b}}{{a}}\\right)^{{p/q}} \\]\n\n**Step 2: Express numerator and denominator as powers.**\nCancel common powers.\n\n**Step 3: State the final evaluated result.**\nThe value is \\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 4: Exponential equations a^(f(x)) = a^k
    arch4 = {
        'data': [
            ("2^{x - 3} = 32", 32, "2^5", "x - 3 = 5", 8),
            ("3^{2x - 1} = 27", 27, "3^3", "2x - 1 = 3", 2),
            ("5^{x - 2} = 125", 125, "5^3", "x - 2 = 3", 5),
            ("4^{x + 1} = 64", 64, "4^3", "x + 1 = 3", 2),
            ("2^{3x - 1} = 128", 128, "2^7", "3x - 1 = 7", "8/3"),
            ("3^{x + 2} = 81", 81, "3^4", "x + 2 = 4", 2),
            ("7^{2x - 3} = 49", 49, "7^2", "2x - 3 = 2", "5/2"),
            ("2^{x + 4} = 16", 16, "2^4", "x + 4 = 4", 0),
            ("5^{2x + 1} = 1", 1, "5^0", "2x + 1 = 0", "-1/2"),
            ("6^{2x - 4} = 36", 36, "6^2", "2x - 4 = 2", 3)
        ],
        'tmpls': [
            "Solve the exponential equation for \\( x \\): \\( {0} \\).",
            "If \\( {0} \\), what is the value of \\( x \\)?",
            "Find \\( x \\) such that \\( {0} \\):",
            "Solve for \\( x \\) in \\( {0} \\):",
            "Determine \\( x \\) given \\( {0} \\):",
            "The solution to the equation \\( {0} \\) is:",
            "Calculate \\( x \\) from \\( {0} \\):",
            "What value of \\( x \\) satisfies \\( {0} \\)?",
            "Find the root \\( x \\) of the exponential equation \\( {0} \\):",
            "Evaluate \\( x \\) given \\( {0} \\):"
        ],
        'calc': lambda item: (
            str(item[4]),
            [
                str(int(item[4]) + 1) if str(item[4]).isdigit() else "1",
                str(int(item[4]) - 2) if str(item[4]).isdigit() else "3",
                "0"
            ],
            f"**Step 1: Express both sides with the same base.**\n\\[ {item[1]} = {item[2]} \\]\n\n**Step 2: Equate the exponents.**\n\\[ {item[3]} \\]\n\n**Step 3: Solve for \\( x \\).**\n\\( x = {item[4]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 5: Definitions and properties of radicals and rational exponents
    arch5 = {
        'data': [
            ("For any positive real number a and positive integer n, a^(1/n) is defined as:", "the principal n-th root of a (ⁿ√a)", ["a divided by n", "a multiplied by n", "a to the power n"]),
            ("For any non-zero real number a, what is the value of a^0?", "1", ["0", "a", "undefined"]),
            ("What is the value of 0^0 in elementary algebra?", "undefined (indeterminate form)", ["0", "1", "infinity"]),
            ("If a is a positive real number and m, n are coprime integers with n > 0, then a^(m/n) equals:", "(ⁿ√a)^m = ⁿ√(a^m)", ["n√(a/m)", "m√(a^n)", "a^(m - n)"]),
            ("What is the reciprocal of a^(-p)?", "a^p", ["a^(-p)", "-a^p", "1/a^p"]),
            ("The principal square root of any positive real number is always:", "positive", ["negative", "both positive and negative", "imaginary"]),
            ("Can a negative real number have a real square root?", "No, the square root of a negative real number is not a real number", ["Yes, always", "Only if it is an integer", "Only if odd"]),
            ("Can a negative real number have a real cube root?", "Yes, for example ³√(-8) = -2 is a real number", ["No, never", "Only if positive", "Undefined"]),
            ("If x^(1/2) = 5, what is the value of x?", "25", ["10", "√5", "2.5"]),
            ("If x^(1/3) = 4, what is the value of x?", "64", ["12", "16", "³√4"])
        ],
        'tmpls': [
            "{0}",
            "In real exponent theory: {0}",
            "Regarding rational exponents: {0}",
            "Choose the correct statement: {0}",
            "Identify the accurate fact: {0}",
            "Select the correct answer: {0}",
            "Determine the true statement: {0}",
            "Which option correctly answers: {0}",
            "State the mathematical truth: {0}",
            "What is the correct concept concerning: {0}?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the formal definition of real exponents.**\nFor \\( a > 0 \\), rational powers are defined via root extraction and integer exponentiation.\n\n**Step 2: Evaluate the statement.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 6: Combined operations with fractional powers
    arch6 = {
        'data': [
            ("25^{3/2} - 16^{3/4}", "125 - 8 = 117", 117),
            ("64^{2/3} + 27^{2/3}", "16 + 9 = 25", 25),
            ("32^{2/5} + 81^{1/4}", "4 + 3 = 7", 7),
            ("125^{1/3} \\times 16^{1/2}", "5 \\times 4 = 20", 20),
            ("4^{3/2} + 8^{2/3}", "8 + 4 = 12", 12),
            ("81^{3/4} - 32^{3/5}", "27 - 8 = 19", 19),
            ("100^{1/2} \\times 49^{1/2}", "10 \\times 7 = 70", 70),
            ("64^{1/2} + 64^{1/3}", "8 + 4 = 12", 12),
            ("216^{1/3} + 36^{1/2}", "6 + 6 = 12", 12),
            ("16^{3/4} \\times 27^{1/3}", "8 \\times 3 = 24", 24)
        ],
        'tmpls': [
            "Evaluate: \\( {0} \\).",
            "Calculate the value of \\( {0} \\):",
            "What is the result of \\( {0} \\)?",
            "Simplify the numerical expression: \\( {0} \\):",
            "Determine the value of \\( {0} \\):",
            "The expression \\( {0} \\) equals:",
            "Find the numerical value of \\( {0} \\):",
            "Compute \\( {0} \\):",
            "Evaluate and simplify: \\( {0} \\):",
            "What does \\( {0} \\) simplify to?"
        ],
        'calc': lambda item: (
            str(item[2]),
            [
                str(item[2] + 4),
                str(item[2] - 3),
                str(item[2] * 2)
            ],
            f"**Step 1: Evaluate each term with fractional exponents separately.**\n{item[1].split('=')[0]}.\n\n**Step 2: Perform the arithmetic operation.**\n{item[1]}.\n\n**Step 3: State the final evaluated value.**\nThe result is \\( {item[2]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 7: Advanced simplification of radical fractions
    arch7 = {
        'data': [
            ("\\frac{2^{n} + 2^{n-1}}{2^{n+1} - 2^n}", "3/2", "factor out 2^n: (1 + 1/2) / (2 - 1) = 3/2"),
            ("\\frac{3^{n+1} - 3^{n-1}}{3^n + 3^{n-1}}", "2", "factor out 3^{n-1}: (9 - 1) / (3 + 1) = 8/4 = 2"),
            ("\\frac{5^{n+2} - 6 \\cdot 5^{n+1}}{13 \\cdot 5^n - 2 \\cdot 5^{n+1}}", "-5/3", "factor out 5^n"),
            ("\\frac{2^{30} + 2^{29} + 2^{28}}{2^{31} + 2^{30} - 2^{29}}", "7/10", "factor out 2^{28}"),
            ("\\frac{9^n \\cdot 3^2 \\cdot (3^{-n/2})^{-2} - 27^n}{3^{3m} \\cdot 2^3} = 1", "m = n", "equate powers of 3"),
            ("(64)^{-2/3} \\times (\\frac{1}{4})^{-3}", "4", "1/16 * 64 = 4"),
            ("\\sqrt[4]{(81)^{-2}}", "1/9", "81^{-2/4} = 81^{-1/2} = 1/9"),
            ("\\sqrt[3]{(125)^{-2}}", "1/25", "125^{-2/3} = 1/25"),
            ("\\frac{16 \\times 2^{n+1} - 4 \\times 2^n}{16 \\times 2^{n+2} - 2 \\times 2^{n+2}}", "7/14 = 1/2", "factor out 2^n"),
            ("\\frac{2^{n+4} - 2(2^n)}{2(2^{n+3})}", "7/8", "factor out 2^n: (16 - 2) / 16 = 14/16 = 7/8")
        ],
        'tmpls': [
            "Simplify the algebraic exponential expression: \\( {0} \\).",
            "What is the simplified value of \\( {0} \\)?",
            "Evaluate \\( {0} \\):",
            "Calculate \\( {0} \\):",
            "Determine the result of simplifying \\( {0} \\):",
            "The expression \\( {0} \\) simplifies to:",
            "Find the value of \\( {0} \\):",
            "Compute the simplified form of \\( {0} \\):",
            "Simplify completely: \\( {0} \\):",
            "What does \\( {0} \\) evaluate to?"
        ],
        'calc': lambda item: (
            item[1],
            [
                "1" if item[1] != "1" else "2",
                "0",
                "3" if item[1] != "3" else "4"
            ],
            f"**Step 1: Factor out the common base power from numerator and denominator.**\n{item[2]}.\n\n**Step 2: Simplify the resulting numerical coefficients.**\nCancel the common exponential factor.\n\n**Step 3: State the final value.**\nThe simplified result is \\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 3.4.2: Laws of exponents: a^p * a^q = a^(p+q), (a^p)^q = a^(pq), a^p/a^q = a^(p-q), a^p * b^p = (ab)^p
# ==============================================================================
def gen_3_4_2():
    tc = "CBSE-9-MGM-3-3.4.2"
    tname = "Laws of exponents: a^p * a^q = a^(p+q), (a^p)^q = a^(pq), a^p/a^q = a^(p-q), a^p * b^p = (ab)^p"

    # Arch 0: Law 1: Product rule a^p * a^q = a^(p+q) with fractional exponents
    arch0 = {
        'data': [
            ("2^{2/3} \\cdot 2^{1/3}", "2", "2/3 + 1/3 = 1", ["2^{2/9}", "4^{1/3}", "2^{1/2}"]),
            ("2^{2/3} \\cdot 2^{1/5}", "2^{13/15}", "2/3 + 1/5 = 10/15 + 3/15 = 13/15", ["2^{3/8}", "2^{2/15}", "4^{13/15}"]),
            ("3^{1/3} \\cdot 3^{1/4}", "3^{7/12}", "1/3 + 1/4 = 4/12 + 3/12 = 7/12", ["3^{1/12}", "3^{2/7}", "9^{7/12}"]),
            ("5^{1/2} \\cdot 5^{1/3}", "5^{5/6}", "1/2 + 1/3 = 3/6 + 2/6 = 5/6", ["5^{1/6}", "5^{2/5}", "25^{5/6}"]),
            ("7^{2/5} \\cdot 7^{3/5}", "7", "2/5 + 3/5 = 5/5 = 1", ["7^{6/25}", "49", "7^{1/5}"]),
            ("3^{3/4} \\cdot 3^{1/4}", "3", "3/4 + 1/4 = 1", ["3^{3/16}", "9", "3^{1/2}"]),
            ("11^{1/2} \\cdot 11^{1/3}", "11^{5/6}", "1/2 + 1/3 = 5/6", ["11^{1/6}", "11^{2/5}", "121^{5/6}"]),
            ("2^{3/4} \\cdot 2^{1/2}", "2^{5/4}", "3/4 + 2/4 = 5/4", ["2^{3/8}", "4^{5/4}", "2^{1/4}"]),
            ("5^{2/3} \\cdot 5^{1/6}", "5^{5/6}", "4/6 + 1/6 = 5/6", ["5^{1/3}", "5^{2/9}", "25^{5/6}"]),
            ("6^{1/2} \\cdot 6^{1/2}", "6", "1/2 + 1/2 = 1", ["6^{1/4}", "36", "12"])
        ],
        'tmpls': [
            "Simplify using the product law of exponents: \\( {0} \\).",
            "What is the value of \\( {0} \\)?",
            "Calculate \\( {0} \\):",
            "Determine the result of \\( {0} \\):",
            "The product \\( {0} \\) simplifies to:",
            "Find the simplified form of \\( {0} \\):",
            "Apply the law \\( a^p \\cdot a^q = a^{{p+q}} \\) to evaluate \\( {0} \\):",
            "Compute \\( {0} \\):",
            "Simplify: \\( {0} \\):",
            "What does \\( {0} \\) equal?"
        ],
        'calc': lambda item: (
            item[1],
            item[3],
            f"**Step 1: Apply the product law of exponents.**\n\\[ a^p \\cdot a^q = a^{{p + q}} \\]\n\n**Step 2: Add the fractional exponents.**\n{item[2]}.\n\n**Step 3: State the simplified expression.**\nThe result is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Law 2: Power of a power (a^p)^q = a^(pq)
    arch1 = {
        'data': [
            ("(3^{1/5})^4", "3^{4/5}", "1/5 * 4 = 4/5", ["3^{21/5}", "3^{1/20}", "12^{1/5}"]),
            ("(2^{2/3})^3", "4", "2/3 * 3 = 2 => 2^2 = 4", ["2", "8", "2^{11/3}"]),
            ("(5^{1/3})^6", "25", "1/3 * 6 = 2 => 5^2 = 25", ["5", "125", "5^{19/3}"]),
            ("(7^{3/4})^4", "343", "3/4 * 4 = 3 => 7^3 = 343", ["49", "7", "2401"]),
            ("(11^{1/2})^4", "121", "1/2 * 4 = 2 => 11^2 = 121", ["11", "1331", "11^{9/2}"]),
            ("(3^{2/5})^5", "9", "2/5 * 5 = 2 => 3^2 = 9", ["3", "27", "3^{27/5}"]),
            ("(2^{3/2})^2", "8", "3/2 * 2 = 3 => 2^3 = 8", ["4", "16", "2^{7/2}"]),
            ("(4^{1/3})^3", "4", "1/3 * 3 = 1 => 4^1 = 4", ["16", "64", "4^{10/3}"]),
            ("(5^{1/4})^8", "25", "1/4 * 8 = 2 => 5^2 = 25", ["5", "125", "5^{33/4}"]),
            ("(10^{1/3})^6", "100", "1/3 * 6 = 2 => 10^2 = 100", ["10", "1000", "10^{19/3}"])
        ],
        'tmpls': [
            "Simplify using the power law: \\( {0} \\).",
            "What is the simplified value of \\( {0} \\)?",
            "Calculate \\( {0} \\):",
            "Determine the result of \\( {0} \\):",
            "The expression \\( {0} \\) simplifies to:",
            "Apply \\( (a^p)^q = a^{{pq}} \\) to \\( {0} \\):",
            "Find the numerical or exponential value of \\( {0} \\):",
            "Compute \\( {0} \\):",
            "Simplify: \\( {0} \\):",
            "What does \\( {0} \\) equal?"
        ],
        'calc': lambda item: (
            item[1],
            item[3],
            f"**Step 1: Apply the power of a power law.**\n\\[ (a^p)^q = a^{{p \\cdot q}} \\]\n\n**Step 2: Multiply the exponents.**\n{item[2]}.\n\n**Step 3: State the final evaluated expression.**\nThe result is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Law 3: Quotient rule a^p / a^q = a^(p-q)
    arch2 = {
        'data': [
            ("\\frac{7^{1/5}}{7^{1/3}}", "7^{-2/15}", "1/5 - 1/3 = 3/15 - 5/15 = -2/15", ["7^{8/15}", "7^{1/15}", "7^{-1/2}"]),
            ("\\frac{11^{1/2}}{11^{1/4}}", "11^{1/4}", "1/2 - 1/4 = 2/4 - 1/4 = 1/4", ["11^{3/4}", "11^{1/8}", "11^{2}"]),
            ("\\frac{2^{2/3}}{2^{1/6}}", "2^{1/2}", "2/3 - 1/6 = 4/6 - 1/6 = 3/6 = 1/2", ["2^{5/6}", "2^{1/4}", "2^{1/3}"]),
            ("\\frac{3^{3/4}}{3^{1/2}}", "3^{1/4}", "3/4 - 2/4 = 1/4", ["3^{5/4}", "3^{3/8}", "3^{1/2}"]),
            ("\\frac{5^{4/5}}{5^{1/5}}", "5^{3/5}", "4/5 - 1/5 = 3/5", ["5^{1}", "5^{4/25}", "5^{1/5}"]),
            ("\\frac{6^{1/2}}{6^{1/3}}", "6^{1/6}", "1/2 - 1/3 = 3/6 - 2/6 = 1/6", ["6^{5/6}", "6^{1/5}", "6^{2/3}"]),
            ("\\frac{7^{5/6}}{7^{1/2}}", "7^{1/3}", "5/6 - 3/6 = 2/6 = 1/3", ["7^{4/3}", "7^{5/12}", "7^{2/3}"]),
            ("\\frac{13^{2/3}}{13^{1/3}}", "13^{1/3}", "2/3 - 1/3 = 1/3", ["13^1", "13^{2/9}", "13^{1/6}"]),
            ("\\frac{8^{5/3}}{8^{2/3}}", "8", "5/3 - 2/3 = 3/3 = 1 => 8^1 = 8", ["64", "4", "8^{7/3}"]),
            ("\\frac{10^{7/4}}{10^{3/4}}", "10", "7/4 - 3/4 = 4/4 = 1 => 10^1 = 10", ["100", "1", "10^{5/2}"])
        ],
        'tmpls': [
            "Simplify using the quotient law: \\( {0} \\).",
            "What is the value of \\( {0} \\)?",
            "Calculate \\( {0} \\):",
            "Determine the result of dividing: \\( {0} \\):",
            "The quotient \\( {0} \\) simplifies to:",
            "Apply \\( a^p / a^q = a^{{p-q}} \\) to \\( {0} \\):",
            "Find the simplified form of \\( {0} \\):",
            "Compute \\( {0} \\):",
            "Simplify: \\( {0} \\):",
            "What does \\( {0} \\) simplify to?"
        ],
        'calc': lambda item: (
            item[1],
            item[3],
            f"**Step 1: Apply the quotient law of exponents.**\n\\[ \\frac{{a^p}}{{a^q}} = a^{{p - q}} \\]\n\n**Step 2: Subtract the fractional exponents.**\n{item[2]}.\n\n**Step 3: State the simplified expression.**\nThe result is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Law 4: Same power, different bases: a^p * b^p = (ab)^p
    arch3 = {
        'data': [
            ("13^{1/5} \\cdot 17^{1/5}", "221^{1/5}", "13 * 17 = 221", ["30^{1/5}", "221^{2/5}", "221^{1/25}"]),
            ("7^{1/2} \\cdot 8^{1/2}", "56^{1/2}", "7 * 8 = 56", ["15^{1/2}", "56^{1}", "56^{1/4}"]),
            ("2^{1/3} \\cdot 3^{1/3}", "6^{1/3}", "2 * 3 = 6", ["5^{1/3}", "6^{2/3}", "6^{1/9}"]),
            ("5^{1/4} \\cdot 3^{1/4}", "15^{1/4}", "5 * 3 = 15", ["8^{1/4}", "15^{1/2}", "15^{1/16}"]),
            ("6^{1/2} \\cdot 7^{1/2}", "42^{1/2}", "6 * 7 = 42", ["13^{1/2}", "42^{1}", "42^{1/4}"]),
            ("3^{1/5} \\cdot 4^{1/5}", "12^{1/5}", "3 * 4 = 12", ["7^{1/5}", "12^{2/5}", "12^{1/25}"]),
            ("11^{1/3} \\cdot 2^{1/3}", "22^{1/3}", "11 * 2 = 22", ["13^{1/3}", "22^{2/3}", "22^{1/9}"]),
            ("5^{2/3} \\cdot 2^{2/3}", "10^{2/3}", "5 * 2 = 10", ["7^{2/3}", "10^{4/3}", "10^{4/9}"]),
            ("3^{3/4} \\cdot 2^{3/4}", "6^{3/4}", "3 * 2 = 6", ["5^{3/4}", "6^{6/4}", "6^{9/16}"]),
            ("8^{1/2} \\cdot 2^{1/2}", "4", "8 * 2 = 16 => 16^{1/2} = 4", ["16", "2", "10^{1/2}"])
        ],
        'tmpls': [
            "Simplify using the power of product rule: \\( {0} \\).",
            "What is the value of \\( {0} \\)?",
            "Calculate \\( {0} \\):",
            "Determine the result of \\( {0} \\):",
            "The product \\( {0} \\) simplifies to:",
            "Apply \\( a^p \\cdot b^p = (ab)^p \\) to \\( {0} \\):",
            "Find the simplified form of \\( {0} \\):",
            "Compute \\( {0} \\):",
            "Simplify: \\( {0} \\):",
            "What does \\( {0} \\) equal?"
        ],
        'calc': lambda item: (
            item[1],
            item[3],
            f"**Step 1: Apply the power of a product rule.**\n\\[ a^p \\cdot b^p = (a \\cdot b)^p \\]\n\n**Step 2: Multiply the bases.**\n{item[2]}.\n\n**Step 3: State the simplified expression.**\nThe result is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 4: Solving exponential equations using laws of exponents
    arch4 = {
        'data': [
            ("2^x = 16^{1/2}", "16^{1/2} = 4 = 2^2", 2),
            ("3^x = 81^{3/4}", "81^{3/4} = 3^3 = 27", 3),
            ("5^x = 125^{2/3}", "125^{2/3} = 5^2 = 25", 2),
            ("2^{x+1} = 64^{1/3}", "64^{1/3} = 4 = 2^2 => x+1=2", 1),
            ("3^{2x} = 27^{4/3}", "27^{4/3} = 3^4 = 81 => 2x=4", 2),
            ("4^x = 64^{2/3}", "64^{2/3} = 16 = 4^2", 2),
            ("5^{x-1} = 25^{3/2}", "25^{3/2} = 125 = 5^3 => x-1=3", 4),
            ("2^{3x} = 32^{3/5}", "32^{3/5} = 2^3 = 8 => 3x=3", 1),
            ("10^x = 1000^{2/3}", "1000^{2/3} = 10^2 = 100", 2),
            ("7^x = 49^{3/2}", "49^{3/2} = 7^3 = 343", 3)
        ],
        'tmpls': [
            "Find \\( x \\) if \\( {0} \\).",
            "Solve for \\( x \\) in the equation \\( {0} \\):",
            "What value of \\( x \\) satisfies \\( {0} \\)?",
            "Calculate \\( x \\) given \\( {0} \\):",
            "Determine the root \\( x \\) of \\( {0} \\):",
            "The value of \\( x \\) satisfying \\( {0} \\) is:",
            "Find \\( x \\) from \\( {0} \\):",
            "Solve the exponential relation: \\( {0} \\):",
            "Evaluate \\( x \\) in \\( {0} \\):",
            "Compute \\( x \\) such that \\( {0} \\):"
        ],
        'calc': lambda item: (
            str(item[2]),
            [
                str(item[2] + 1),
                str(item[2] + 2),
                str(item[2] - 1)
            ],
            f"**Step 1: Simplify the right-hand side using fractional powers.**\n{item[1]}.\n\n**Step 2: Equate the powers on both sides.**\nEquate exponents since bases are identical.\n\n**Step 3: State the value of \\( x \\).**\n\\( x = {item[2]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 5: Theoretical laws of exponents for positive real bases
    arch5 = {
        'data': [
            ("Which of the following is the correct formulation of the Product Law of exponents for real base a > 0?", "a^p * a^q = a^(p + q)", ["a^p * a^q = a^(pq)", "a^p * a^q = a^(p - q)", "a^p * a^q = (2a)^(p+q)"]),
            ("Which law describes the power of a power for real base a > 0?", "(a^p)^q = a^(pq)", ["(a^p)^q = a^(p + q)", "(a^p)^q = a^(p^q)", "(a^p)^q = pa^q"]),
            ("Which identity represents the Quotient Law of exponents?", "a^p / a^q = a^(p - q)", ["a^p / a^q = a^(p / q)", "a^p / a^q = a^(pq)", "a^p / a^q = a^(q - p)"]),
            ("Which identity describes the power of a product for bases a, b > 0?", "a^p * b^p = (ab)^p", ["a^p * b^p = (a + b)^p", "a^p * b^p = (ab)^(2p)", "a^p * b^p = ab^p"]),
            ("What is the value of (a/b)^p according to laws of exponents?", "a^p / b^p", ["(a - b)^p", "a^p - b^p", "ab^p"]),
            ("For any positive real number a and rational number p, a^(-p) equals:", "1 / a^p", ["-a^p", "-1/a^p", "a^(1/p)"]),
            ("What is the value of a^0 for any positive real number a?", "1", ["0", "a", "undefined"]),
            ("Why is the restriction a > 0 required when dealing with rational exponents a^(p/q)?", "To prevent non-real complex numbers when taking even roots of negative numbers", ["Because negative numbers cannot be squared", "Because 0 is not a number", "It is not required"]),
            ("Is (-4)^(1/2) a real number?", "No, because no real number squared equals -4 (it is an imaginary number)", ["Yes, it is -2", "Yes, it is 2", "Yes, it is -16"]),
            ("Does (-8)^(1/3) have a real value?", "Yes, it equals -2 (since (-2)³ = -8)", ["No, it is imaginary", "Yes, it equals 2", "Undefined"])
        ],
        'tmpls': [
            "{0}",
            "In the mathematical foundation of laws of exponents: {0}",
            "Regarding exponential laws for real numbers: {0}",
            "Choose the correct option: {0}",
            "Identify the valid exponential law: {0}",
            "Select the accurate theorem: {0}",
            "Determine the true statement: {0}",
            "Which option correctly describes: {0}?",
            "State the law of exponents: {0}",
            "What is the correct mathematical identity concerning: {0}?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the fundamental laws of exponents.**\nFor positive real bases \\( a, b > 0 \\) and rational exponents \\( p, q \\), standard exponent laws hold universally.\n\n**Step 2: Evaluate the statement.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Simplifying expressions involving fractional exponents and multiple bases
    arch6 = {
        'data': [
            ("\\frac{2^{1/2} \\cdot 3^{1/3} \\cdot 4^{1/4}}{10^{-1/5} \\cdot 5^{3/5}} \\div \\frac{3^{4/3} \\cdot 5^{-7/5}}{4^{-3/5} \\cdot 6}", "10", 10),
            ("(\\sqrt{4})^{-7} \\times (\\sqrt{2})^{-5}", "2^{-19/2}", 19),
            ("(\\frac{81}{16})^{-3/4} \\times [(\\frac{25}{9})^{-3/2} \\div (\\frac{5}{2})^{-3}]", "1", 1),
            ("(\\frac{x^a}{x^b})^{a+b} \\cdot (\\frac{x^b}{x^c})^{b+c} \\cdot (\\frac{x^c}{x^a})^{c+a}", "1", 1),
            ("(\\frac{x^a}{x^b})^{1/ab} \\cdot (\\frac{x^b}{x^c})^{1/bc} \\cdot (\\frac{x^c}{x^a})^{1/ca}", "1", 1),
            ("(\\frac{x^a}{x^{-b}})^{a^2 - ab + b^2} \\cdot (\\frac{x^b}{x^{-c}})^{b^2 - bc + c^2} \\cdot (\\frac{x^c}{x^{-a}})^{c^2 - ca + a^2}", "x^{2(a^3 + b^3 + c^3)}", 2),
            ("\\frac{1}{1 + x^{b-a} + x^{c-a}} + \\frac{1}{1 + x^{a-b} + x^{c-b}} + \\frac{1}{1 + x^{a-c} + x^{b-c}}", "1", 1),
            ("\\frac{1}{1 + x^{a-b}} + \\frac{1}{1 + x^{b-a}}", "1", 1),
            ("(x^{a-b})^{a+b} \\cdot (x^{b-c})^{b+c} \\cdot (x^{c-a})^{c+a}", "1", 1),
            ("(\\frac{x^p}{x^q})^{p+q} \\cdot (\\frac{x^q}{x^r})^{q+r} \\cdot (\\frac{x^r}{x^p})^{r+p}", "1", 1)
        ],
        'tmpls': [
            "Simplify the classic exponential expression: \\( {0} \\).",
            "What is the simplified value of \\( {0} \\)?",
            "Evaluate \\( {0} \\):",
            "Calculate \\( {0} \\):",
            "Determine the result of simplifying \\( {0} \\):",
            "The expression \\( {0} \\) reduces to:",
            "Find the value of the cyclic exponential expression: \\( {0} \\):",
            "Compute the simplified form of \\( {0} \\):",
            "Simplify completely: \\( {0} \\):",
            "What does \\( {0} \\) simplify to?"
        ],
        'calc': lambda item: (
            item[1],
            [
                "0",
                "x",
                "-1"
            ],
            f"**Step 1: Apply quotient law inside each term.**\n\\( \\frac{{x^a}}{{x^b}} = x^{{a - b}} \\).\n\n**Step 2: Multiply exponents and combine terms.**\nApply difference of squares or common denominators.\n\n**Step 3: State the final simplified value.**\nThe expression simplifies to \\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 7: Real-world modeling with exponential scaling
    arch7 = {
        'data': [
            ("A culture of bacteria doubles every hour: N(t) = 100 * 2^t. How many bacteria are present after 3.5 hours?", "100 * 2^(7/2) = 800√2 ≈ 1131", ["800", "1200", "700"]),
            ("A radioactive element decays by half every year: A(t) = 64 * (1/2)^t. How much remains after 2.5 years?", "64 * (1/2)^(5/2) = 64 / (4√2) = 8√2 ≈ 11.31 g", ["16 g", "8 g", "12 g"]),
            ("Sound intensity ratio increases exponentially as 10^(L/10). What is the factor for an increase of 15 dB?", "10^(1.5) = 10√10 ≈ 31.62", ["15", "100", "25"]),
            ("An investment triples every 6 years: V(t) = P * 3^(t/6). After 9 years, the growth multiplier is:", "3^(9/6) = 3^(3/2) = 3√3 ≈ 5.196", ["4.5", "6", "9"]),
            ("The population of a species grows as P(t) = 500 * 4^(t/4). What is the population after 6 years?", "500 * 4^(3/2) = 500 * 8 = 4000", ["2000", "3000", "5000"]),
            ("A medicine concentration in blood halves every 4 hours: C(t) = 100 * (1/2)^(t/4). What is the concentration after 6 hours?", "100 * (1/2)^(3/2) = 100 / (2√2) = 25√2 ≈ 35.36 mg/L", ["50 mg/L", "25 mg/L", "40 mg/L"]),
            ("Light intensity through tinted glass decreases as I(x) = I_0 * (1/4)^x for thickness x cm. For x = 1.5 cm, the fraction remaining is:", "(1/4)^(3/2) = 1/8", ["1/4", "1/16", "3/8"]),
            ("A tree grows in height as H(t) = 2 * 8^(t/9) meters. What is its height after 6 years?", "2 * 8^(2/3) = 2 * 4 = 8 meters", ["6 meters", "10 meters", "12 meters"]),
            ("The value of an antique increases as V(t) = 1000 * (16/9)^(t/2). After 3 years, the value is:", "1000 * (16/9)^(3/2) = 1000 * (64/27) ≈ ₹2370.37", ["₹2000", "₹1800", "₹3000"]),
            ("Energy dissipated scales as E = E_0 * 27^(t/3). After 2 time units, the energy multiplication factor is:", "27^(2/3) = 9", ["6", "18", "81"])
        ],
        'tmpls': [
            "{0}",
            "Solve the following applied exponential problem: {0}",
            "In practical exponential scaling: {0}",
            "Calculate the required value using laws of exponents: {0}",
            "Applied fractional exponent problem: {0}",
            "Determine the result: {0}",
            "Compute the final quantity: {0}",
            "Find the solution to: {0}",
            "Evaluate the exponential model: {0}",
            "What is the answer to this real-world problem: {0}?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify the exponential model and fractional exponent.**\nFrom the problem description: '{item[0]}'.\n\n**Step 2: Apply fractional power evaluation.**\nExpress the base as a prime power and multiply exponents.\n\n**Step 3: State the final calculated value.**\nThe solution is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])

if __name__ == "__main__":
    q1 = gen_3_4_1()
    q2 = gen_3_4_2()
    print(f"gen_3_4_1: {len(q1)} questions generated")
    print(f"gen_3_4_2: {len(q2)} questions generated")
