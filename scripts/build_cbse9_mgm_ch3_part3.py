# scripts/build_cbse9_mgm_ch3_part3.py
# Subtopics:
# 3.3.1: Properties of addition, subtraction, multiplication, division of real numbers (80 Qs)
# 3.3.2: Rationalising binomial denominators with conjugate surds 1/(a + √b) (80 Qs)

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 3
CH_NAME = "The World of Numbers"

# ==============================================================================
# SUBTOPIC 3.3.1: Properties of addition, subtraction, multiplication, division of real numbers
# ==============================================================================
def gen_3_3_1():
    tc = "CBSE-9-MGM-3-3.3.1"
    tname = "Properties of addition, subtraction, multiplication, division of real numbers"

    # Arch 0: Adding and subtracting like surds
    arch0 = {
        'data': [
            ("3\\sqrt{2} + 5\\sqrt{2}", "8\\sqrt{2}", ["8", "15\\sqrt{2}", "8\\sqrt{4}"]),
            ("7\\sqrt{3} - 4\\sqrt{3}", "3\\sqrt{3}", ["3", "11\\sqrt{3}", "3\\sqrt{9}"]),
            ("6\\sqrt{5} + 2\\sqrt{5} - 3\\sqrt{5}", "5\\sqrt{5}", ["5", "11\\sqrt{5}", "5\\sqrt{15}"]),
            ("4\\sqrt{7} + 9\\sqrt{7}", "13\\sqrt{7}", ["13", "36\\sqrt{7}", "13\\sqrt{14}"]),
            ("10\\sqrt{6} - 7\\sqrt{6}", "3\\sqrt{6}", ["3", "17\\sqrt{6}", "3\\sqrt{12}"]),
            ("5\\sqrt{11} - 2\\sqrt{11} + 4\\sqrt{11}", "7\\sqrt{11}", ["7", "11\\sqrt{11}", "7\\sqrt{33}"]),
            ("8\\sqrt{3} + 3\\sqrt{3} - 5\\sqrt{3}", "6\\sqrt{3}", ["6", "16\\sqrt{3}", "6\\sqrt{6}"]),
            ("12\\sqrt{2} - 8\\sqrt{2}", "4\\sqrt{2}", ["4", "20\\sqrt{2}", "4\\sqrt{4}"]),
            ("9\\sqrt{5} - 6\\sqrt{5} + \\sqrt{5}", "4\\sqrt{5}", ["4", "16\\sqrt{5}", "3\\sqrt{5}"]),
            ("2\\sqrt{13} + 7\\sqrt{13}", "9\\sqrt{13}", ["9", "14\\sqrt{13}", "9\\sqrt{26}"])
        ],
        'tmpls': [
            "Simplify the expression \\( {0} \\).",
            "What is the simplified value of \\( {0} \\)?",
            "Evaluate \\( {0} \\):",
            "Combine the like surds in \\( {0} \\):",
            "Calculate \\( {0} \\):",
            "Determine the result of \\( {0} \\):",
            "The expression \\( {0} \\) simplifies to:",
            "Perform the indicated operations: \\( {0} \\):",
            "Find the simplified form of \\( {0} \\):",
            "Add and subtract the radical terms: \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify like radical terms.**\nAll terms share the same surd factor.\n\n**Step 2: Apply the distributive law.**\nFactor out the common radical: \\( (c_1 + c_2 - c_3)\\sqrt{{r}} \\).\n\n**Step 3: State the result.**\nThe simplified expression is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Simplifying surds before adding (e.g. √18 + √50)
    arch1 = {
        'data': [
            ("\\sqrt{18} + \\sqrt{50}", "8\\sqrt{2}", "3\\sqrt{2} + 5\\sqrt{2}"),
            ("\\sqrt{12} + \\sqrt{27}", "5\\sqrt{3}", "2\\sqrt{3} + 3\\sqrt{3}"),
            ("\\sqrt{20} + \\sqrt{45}", "5\\sqrt{5}", "2\\sqrt{5} + 3\\sqrt{5}"),
            ("\\sqrt{28} + \\sqrt{63}", "5\\sqrt{7}", "2\\sqrt{7} + 3\\sqrt{7}"),
            ("\\sqrt{24} + \\sqrt{54}", "5\\sqrt{6}", "2\\sqrt{6} + 3\\sqrt{6}"),
            ("\\sqrt{32} - \\sqrt{8}", "2\\sqrt{2}", "4\\sqrt{2} - 2\\sqrt{2}"),
            ("\\sqrt{48} - \\sqrt{12}", "2\\sqrt{3}", "4\\sqrt{3} - 2\\sqrt{3}"),
            ("\\sqrt{75} - \\sqrt{27}", "2\\sqrt{3}", "5\\sqrt{3} - 3\\sqrt{3}"),
            ("\\sqrt{80} - \\sqrt{45}", "\\sqrt{5}", "4\\sqrt{5} - 3\\sqrt{5}"),
            ("\\sqrt{72} + \\sqrt{98}", "13\\sqrt{2}", "6\\sqrt{2} + 7\\sqrt{2}")
        ],
        'tmpls': [
            "Simplify \\( {0} \\) by writing each radical in its simplest surd form.",
            "What is the simplified value of \\( {0} \\)?",
            "Evaluate \\( {0} \\):",
            "Simplify: \\( {0} \\):",
            "Calculate \\( {0} \\) in terms of simplest radicals:",
            "Determine the result of \\( {0} \\):",
            "The sum/difference \\( {0} \\) equals:",
            "Find the value of \\( {0} \\):",
            "Express \\( {0} \\) in simplest radical form:",
            "Reduce and combine: \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("\\sqrt{", "3\\sqrt{"),
                item[1].replace("\\sqrt{", "2\\sqrt{"),
                "0"
            ],
            f"**Step 1: Simplify each square root by extracting perfect squares.**\n\\( {item[0]} = {item[2]} \\).\n\n**Step 2: Add or subtract like radical terms.**\nCombine the coefficients of the common surd.\n\n**Step 3: State the final simplified form.**\nThe result is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Multiplying surds using product rule √(ab) = √a * √b
    arch2 = {
        'data': [
            ("2\\sqrt{3} \\times 4\\sqrt{6}", "24\\sqrt{2}", 24),
            ("3\\sqrt{5} \\times 2\\sqrt{10}", "30\\sqrt{2}", 30),
            ("4\\sqrt{2} \\times 3\\sqrt{8}", "48", 48),
            ("5\\sqrt{3} \\times 2\\sqrt{12}", "60", 60),
            ("2\\sqrt{7} \\times 3\\sqrt{14}", "42\\sqrt{2}", 42),
            ("3\\sqrt{6} \\times 4\\sqrt{3}", "36\\sqrt{2}", 36),
            ("5\\sqrt{2} \\times 6\\sqrt{3}", "30\\sqrt{6}", 30),
            ("4\\sqrt{5} \\times 2\\sqrt{15}", "40\\sqrt{3}", 40),
            ("6\\sqrt{3} \\times 3\\sqrt{6}", "54\\sqrt{2}", 54),
            ("2\\sqrt{11} \\times 5\\sqrt{22}", "110\\sqrt{2}", 110)
        ],
        'tmpls': [
            "Multiply and simplify: \\( {0} \\).",
            "What is the product \\( {0} \\)?",
            "Evaluate \\( {0} \\):",
            "Calculate \\( {0} \\):",
            "Determine the product of \\( {0} \\):",
            "Simplify the product \\( {0} \\):",
            "The multiplication \\( {0} \\) gives:",
            "Find the numerical value of \\( {0} \\):",
            "Compute \\( {0} \\):",
            "Perform the multiplication: \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"{item[2] * 2}",
                item[1].replace("\\sqrt{2}", "\\sqrt{3}") if "\\sqrt{2}" in item[1] else f"{item[2]}\\sqrt{2}",
                f"{item[2] // 2}"
            ],
            f"**Step 1: Multiply rational coefficients and radicands separately.**\n\\[ (a\\sqrt{{x}})(b\\sqrt{{y}}) = (a \\cdot b)\\sqrt{{x \\cdot y}} \\]\n\n**Step 2: Simplify the radical under the square root.**\nFactor out any perfect square from the resulting radicand.\n\n**Step 3: State the simplified product.**\nThe product is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Distributive law with surds: √a(√b + √c)
    arch3 = {
        'data': [
            ("\\sqrt{3}(\\sqrt{6} + \\sqrt{3})", "3\\sqrt{2} + 3", "\\sqrt{18} + 3"),
            ("\\sqrt{2}(\\sqrt{6} - \\sqrt{2})", "2\\sqrt{3} - 2", "\\sqrt{12} - 2"),
            ("\\sqrt{5}(\\sqrt{10} + \\sqrt{5})", "5\\sqrt{2} + 5", "\\sqrt{50} + 5"),
            ("\\sqrt{3}(2\\sqrt{3} + 4)", "6 + 4\\sqrt{3}", "2(3) + 4\\sqrt{3}"),
            ("\\sqrt{7}(\\sqrt{14} - \\sqrt{7})", "7\\sqrt{2} - 7", "\\sqrt{98} - 7"),
            ("2\\sqrt{2}(\\sqrt{8} + \\sqrt{2})", "12", "2(4) + 2(2) = 8 + 4"),
            ("\\sqrt{6}(\\sqrt{3} + \\sqrt{2})", "3\\sqrt{2} + 2\\sqrt{3}", "\\sqrt{18} + \\sqrt{12}"),
            ("\\sqrt{5}(3\\sqrt{5} - \\sqrt{20})", "5", "15 - 10"),
            ("3\\sqrt{3}(\\sqrt{27} - \\sqrt{3})", "18", "3(9) - 3(3) = 27 - 9"),
            ("\\sqrt{2}(5\\sqrt{2} + \\sqrt{18})", "16", "10 + 6")
        ],
        'tmpls': [
            "Expand and simplify using the distributive property: \\( {0} \\).",
            "What is the expanded form of \\( {0} \\)?",
            "Apply the distributive law to expand \\( {0} \\):",
            "Simplify: \\( {0} \\):",
            "Calculate \\( {0} \\):",
            "Determine the result of expanding \\( {0} \\):",
            "The expression \\( {0} \\) expands to:",
            "Multiply out: \\( {0} \\):",
            "Find the simplified form of \\( {0} \\):",
            "Evaluate \\( {0} \\) using the distributive property:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("+", "-") if "+" in item[1] else item[1].replace("-", "+"),
                item[1].replace("3", "5"),
                "0"
            ],
            f"**Step 1: Apply the distributive property.**\nMultiply the outer term with each term inside the parentheses: \\( a(b + c) = ab + ac \\).\n\n**Step 2: Simplify each radical product.**\n\\( {item[0]} = {item[2]} = {item[1]} \\).\n\n**Step 3: State the final expression.**\nThe result is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Squaring binomial surds (√a + √b)² = a + 2√(ab) + b
    arch4 = {
        'data': [
            ("(\\sqrt{3} + \\sqrt{2})^2", "5 + 2\\sqrt{6}", 5, 6),
            ("(\\sqrt{5} + \\sqrt{3})^2", "8 + 2\\sqrt{15}", 8, 15),
            ("(\\sqrt{7} + \\sqrt{2})^2", "9 + 2\\sqrt{14}", 9, 14),
            ("(\\sqrt{5} - \\sqrt{2})^2", "7 - 2\\sqrt{10}", 7, 10),
            ("(\\sqrt{6} - \\sqrt{3})^2", "9 - 6\\sqrt{2}", 9, 2),
            ("(2\\sqrt{3} + \\sqrt{2})^2", "14 + 4\\sqrt{6}", 14, 6),
            ("(\\sqrt{7} - \\sqrt{5})^2", "12 - 2\\sqrt{35}", 12, 35),
            ("(3 + \\sqrt{2})^2", "11 + 6\\sqrt{2}", 11, 2),
            ("(2 - \\sqrt{5})^2", "9 - 4\\sqrt{5}", 9, 5),
            ("(\\sqrt{10} + \\sqrt{3})^2", "13 + 2\\sqrt{30}", 13, 30)
        ],
        'tmpls': [
            "Expand and simplify \\( {0} \\).",
            "What is the expansion of \\( {0} \\)?",
            "Evaluate \\( {0} \\) using algebraic identities:",
            "Calculate \\( {0} \\):",
            "Determine the result of squaring \\( {0} \\):",
            "The square \\( {0} \\) simplifies to:",
            "Find the expanded form of \\( {0} \\):",
            "Compute \\( {0} \\):",
            "Expand \\( {0} \\):",
            "Simplify: \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("+", "-") if "+" in item[1] else item[1].replace("-", "+"),
                f"{item[2]} + \\sqrt{{{item[3]}}}",
                f"{item[2]}"
            ],
            f"**Step 1: Use the identity \\( (x \\pm y)^2 = x^2 \\pm 2xy + y^2 \\).**\n\\[ (\\sqrt{{a}} \\pm \\sqrt{{b}})^2 = a \\pm 2\\sqrt{{ab}} + b \\]\n\n**Step 2: Substitute and add the rational terms.**\nCombine the integers and simplify the cross-term.\n\n**Step 3: State the expanded result.**\nThe expression equals \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 5: Product of conjugate surds (√a + √b)(√a - √b) = a - b
    arch5 = {
        'data': [
            ("(\\sqrt{5} + \\sqrt{2})(\\sqrt{5} - \\sqrt{2})", "3", 5, 2),
            ("(\\sqrt{7} + \\sqrt{3})(\\sqrt{7} - \\sqrt{3})", "4", 7, 3),
            ("(\\sqrt{11} + \\sqrt{5})(\\sqrt{11} - \\sqrt{5})", "6", 11, 5),
            ("(3 + \\sqrt{5})(3 - \\sqrt{5})", "4", 9, 5),
            ("(4 + \\sqrt{7})(4 - \\sqrt{7})", "9", 16, 7),
            ("(5 - \\sqrt{3})(5 + \\sqrt{3})", "22", 25, 3),
            ("(2\\sqrt{3} + 1)(2\\sqrt{3} - 1)", "11", 12, 1),
            ("(3\\sqrt{2} + 2)(3\\sqrt{2} - 2)", "14", 18, 4),
            ("(\\sqrt{13} - \\sqrt{7})(\\sqrt{13} + \\sqrt{7})", "6", 13, 7),
            ("(2\\sqrt{5} - 3)(2\\sqrt{5} + 3)", "11", 20, 9)
        ],
        'tmpls': [
            "Evaluate the product \\( {0} \\).",
            "What is the value of \\( {0} \\)?",
            "Calculate \\( {0} \\):",
            "Determine the result of \\( {0} \\):",
            "Multiply and simplify: \\( {0} \\):",
            "The product \\( {0} \\) simplifies to:",
            "Find the numerical value of \\( {0} \\):",
            "Compute \\( {0} \\) using the difference of squares identity:",
            "Simplify: \\( {0} \\):",
            "What does \\( {0} \\) equal?"
        ],
        'calc': lambda item: (
            item[1],
            [
                str(int(item[1]) + 2),
                str(int(item[1]) - 2),
                str(int(item[1]) * 2)
            ],
            f"**Step 1: Use the difference of squares identity.**\n\\[ (x + y)(x - y) = x^2 - y^2 \\]\n\n**Step 2: Square each term.**\n\\( x^2 = {item[2]} \\) and \\( y^2 = {item[3]} \\).\n\n**Step 3: Subtract the squares.**\n\\( {item[2]} - {item[3]} = {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 6: Division of surds: √(a/b) = √a / √b
    arch6 = {
        'data': [
            ("\\frac{\\sqrt{48}}{\\sqrt{3}}", "4", 16),
            ("\\frac{\\sqrt{75}}{\\sqrt{3}}", "5", 25),
            ("\\frac{\\sqrt{98}}{\\sqrt{2}}", "7", 49),
            ("\\frac{\\sqrt{180}}{\\sqrt{5}}", "6", 36),
            ("\\frac{\\sqrt{162}}{\\sqrt{2}}", "9", 81),
            ("\\frac{\\sqrt{112}}{\\sqrt{7}}", "4", 16),
            ("\\frac{\\sqrt{125}}{\\sqrt{5}}", "5", 25),
            ("\\frac{\\sqrt{150}}{\\sqrt{6}}", "5", 25),
            ("\\frac{\\sqrt{200}}{\\sqrt{8}}", "5", 25),
            ("\\frac{\\sqrt{243}}{\\sqrt{3}}", "9", 81)
        ],
        'tmpls': [
            "Evaluate the quotient \\( {0} \\).",
            "Simplify the fraction \\( {0} \\):",
            "What is the value of \\( {0} \\)?",
            "Calculate \\( {0} \\):",
            "Determine the result of \\( {0} \\):",
            "The expression \\( {0} \\) simplifies to:",
            "Divide and simplify: \\( {0} \\):",
            "Find the numerical value of \\( {0} \\):",
            "Compute \\( {0} \\):",
            "What does \\( {0} \\) simplify to?"
        ],
        'calc': lambda item: (
            item[1],
            [
                str(int(item[1]) + 2),
                str(int(item[1]) - 1),
                f"\\sqrt{{{item[1]}}}"
            ],
            f"**Step 1: Combine under a single square root using quotient rule.**\n\\[ \\frac{{\\sqrt{{a}}}}{{\\sqrt{{b}}}} = \\sqrt{{\\frac{{a}}{{b}}}} \\]\n\n**Step 2: Simplify the fraction under the radical.**\n\\( \\sqrt{{{item[2]}}} \\).\n\n**Step 3: Evaluate the square root.**\n\\( \\sqrt{{{item[2]}}} = {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 7: Algebraic identities for positive real numbers a, b
    arch7 = {
        'data': [
            ("\\sqrt{ab} = \\sqrt{a}\\sqrt{b}", "holds for all positive real numbers a and b", ["holds only when a = b", "holds only when a and b are integers", "does not hold for irrationals"]),
            ("\\sqrt{\\frac{a}{b}} = \\frac{\\sqrt{a}}{\\sqrt{b}}", "holds for all positive real numbers a and b > 0", ["holds only when b is a perfect square", "never holds for reals", "holds only when a is rational"]),
            ("(\\sqrt{a} + \\sqrt{b})(\\sqrt{a} - \\sqrt{b}) = a - b", "is an algebraic identity for all positive reals a and b", ["is only approximately true", "holds only when a > b²", "equals a² - b²"]),
            ("(a + \\sqrt{b})(a - \\sqrt{b}) = a^2 - b", "is true for any real number a and positive real b", ["equals a - b", "equals a² - b²", "equals a² + b"]),
            ("(\\sqrt{a} + \\sqrt{b})^2 = a + 2\\sqrt{ab} + b", "is true for all positive real numbers a and b", ["equals a + b", "equals a + ab + b", "equals a² + b²"]),
            ("(\\sqrt{a} - \\sqrt{b})^2 = a - 2\\sqrt{ab} + b", "is true for all positive real numbers a and b", ["equals a - b", "equals a² - b²", "equals a - 2ab + b"]),
            ("(\\sqrt{a} + \\sqrt{b})(\\sqrt{c} + \\sqrt{d})", "equals \\sqrt{ac} + \\sqrt{ad} + \\sqrt{bc} + \\sqrt{bd}", ["equals \\sqrt{abcd}", "equals \\sqrt{ac} + \\sqrt{bd}", "cannot be expanded"]),
            ("Does \\sqrt{a + b} equal \\sqrt{a} + \\sqrt{b} in general?", "No, \\sqrt{a + b} ≠ \\sqrt{a} + \\sqrt{b} for positive real numbers a, b", ["Yes, always", "Only when a and b are odd", "Only when a = 0 and b = 0"]),
            ("If a = 9 and b = 16, \\sqrt{a + b} = \\sqrt{25} = 5, while \\sqrt{a} + \\sqrt{b} = 3 + 4 = 7. This proves:", "\\sqrt{a + b} ≠ \\sqrt{a} + \\sqrt{b}", ["\\sqrt{a + b} = \\sqrt{a} + \\sqrt{b}", "addition is distributive over radicals", "5 = 7"]),
            ("What is the conjugate of the binomial surd \\sqrt{a} + \\sqrt{b}?", "\\sqrt{a} - \\sqrt{b}", ["\\sqrt{a} + \\sqrt{b}", "-\\sqrt{a} - \\sqrt{b}", "1/(\\sqrt{a} + \\sqrt{b})"])
        ],
        'tmpls': [
            "{0}",
            "In the algebra of radicals: {0}",
            "Regarding algebraic identities with square roots: {0}",
            "Choose the correct mathematical statement: {0}",
            "Identify the accurate algebraic identity: {0}",
            "Select the correct property: {0}",
            "Determine the true statement: {0}",
            "Which option correctly answers: {0}",
            "What is the mathematical truth regarding: {0}?",
            "State the theorem: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall algebraic properties of square roots.**\nFor positive real numbers \\( a \\) and \\( b \\), radicals follow the standard laws of algebra and binomial identities.\n\n**Step 2: Evaluate the statement.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 3.3.2: Rationalising binomial denominators with conjugate surds 1/(a + √b)
# ==============================================================================
def gen_3_3_2():
    tc = "CBSE-9-MGM-3-3.3.2"
    tname = "Rationalising binomial denominators with conjugate surds 1/(a + √b)"

    # Arch 0: Rationalising 1 / (a + √b) where a² - b = 1
    arch0 = {
        'data': [
            ("1 / (2 + \\sqrt{3})", "2 - \\sqrt{3}", 2, 3, 1),
            ("1 / (3 + 2\\sqrt{2})", "3 - 2\\sqrt{2}", 3, 8, 1),
            ("1 / (\\sqrt{2} + 1)", "\\sqrt{2} - 1", 2, 1, 1),
            ("1 / (\\sqrt{5} + 2)", "\\sqrt{5} - 2", 5, 4, 1),
            ("1 / (\\sqrt{10} + 3)", "\\sqrt{10} - 3", 10, 9, 1),
            ("1 / (4 + \\sqrt{15})", "4 - \\sqrt{15}", 16, 15, 1),
            ("1 / (\\sqrt{7} + \\sqrt{6})", "\\sqrt{7} - \\sqrt{6}", 7, 6, 1),
            ("1 / (3 - \\sqrt{8})", "3 + \\sqrt{8} = 3 + 2\\sqrt{2}", 9, 8, 1),
            ("1 / (2 - \\sqrt{3})", "2 + \\sqrt{3}", 4, 3, 1),
            ("1 / (\\sqrt{6} + \\sqrt{5})", "\\sqrt{6} - \\sqrt{5}", 6, 5, 1)
        ],
        'tmpls': [
            "Rationalise the denominator of \\( {0} \\).",
            "Express \\( {0} \\) with a rational denominator.",
            "What is the value of \\( {0} \\) after rationalising the denominator?",
            "Simplify \\( {0} \\) by rationalising its denominator:",
            "Find the equivalent expression for \\( {0} \\) having a rational denominator:",
            "Rationalise: \\( {0} \\):",
            "The expression \\( {0} \\) with rationalised denominator is:",
            "Convert \\( {0} \\) into an expression with integer denominator:",
            "Determine the rationalised form of \\( {0} \\):",
            "Calculate the rationalised value of \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("-", "+") if "-" in item[1] else item[1].replace("+", "-"),
                f"\\frac{{{item[1]}}}{{2}}",
                "1"
            ],
            f"**Step 1: Multiply numerator and denominator by the conjugate of the denominator.**\nThe conjugate changes the sign between terms.\n\n**Step 2: Simplify the denominator using difference of squares.**\n\\[ (x + y)(x - y) = x^2 - y^2 = {item[2]} - {item[3]} = {item[4]} \\]\n\n**Step 3: State the rationalised expression.**\nThe result is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Rationalising 1 / (√a + √b) where a - b > 1
    arch1 = {
        'data': [
            ("1 / (\\sqrt{5} + \\sqrt{2})", "\\frac{\\sqrt{5} - \\sqrt{2}}{3}", 5, 2, 3),
            ("1 / (\\sqrt{7} + \\sqrt{3})", "\\frac{\\sqrt{7} - \\sqrt{3}}{4}", 7, 3, 4),
            ("1 / (\\sqrt{7} + \\sqrt{2})", "\\frac{\\sqrt{7} - \\sqrt{2}}{5}", 7, 2, 5),
            ("1 / (\\sqrt{11} + \\sqrt{7})", "\\frac{\\sqrt{11} - \\sqrt{7}}{4}", 11, 7, 4),
            ("1 / (3 + \\sqrt{5})", "\\frac{3 - \\sqrt{5}}{4}", 9, 5, 4),
            ("1 / (3 + \\sqrt{7})", "\\frac{3 - \\sqrt{7}}{2}", 9, 7, 2),
            ("1 / (4 + \\sqrt{11})", "\\frac{4 - \\sqrt{11}}{5}", 16, 11, 5),
            ("1 / (\\sqrt{10} + \\sqrt{7})", "\\frac{\\sqrt{10} - \\sqrt{7}}{3}", 10, 7, 3),
            ("1 / (5 + \\sqrt{17})", "\\frac{5 - \\sqrt{17}}{8}", 25, 17, 8),
            ("1 / (\\sqrt{13} + \\sqrt{5})", "\\frac{\\sqrt{13} - \\sqrt{5}}{8}", 13, 5, 8)
        ],
        'tmpls': [
            "Rationalise the denominator of \\( {0} \\).",
            "Express \\( {0} \\) with a rational denominator in simplest form.",
            "What is the rationalised form of \\( {0} \\)?",
            "Simplify \\( {0} \\) by eliminating radicals from the denominator:",
            "Find the equivalent expression for \\( {0} \\) with a rational denominator:",
            "Rationalise: \\( {0} \\):",
            "The expression \\( {0} \\) with rationalised denominator equals:",
            "Convert \\( {0} \\) into a fraction with an integer denominator:",
            "Determine the rationalised form of \\( {0} \\):",
            "Calculate \\( {0} \\) with a rational denominator:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("-", "+"),
                f"\\frac{{{item[1].split('{')[1].split('}')[0]}}}{{{item[4] + 1}}}",
                "1"
            ],
            f"**Step 1: Multiply numerator and denominator by the conjugate.**\nMultiply both by \\( (\\sqrt{{a}} - \\sqrt{{b}}) \\).\n\n**Step 2: Simplify the denominator.**\nDenominator = \\( (\\sqrt{{a}})^2 - (\\sqrt{{b}})^2 = {item[2]} - {item[3]} = {item[4]} \\).\n\n**Step 3: State the rationalised fraction.**\nThe result is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Finding unknown rational constants a and b in identities: (√3 - 1)/(√3 + 1) = a + b√3
    arch2 = {
        'data': [
            ("\\frac{\\sqrt{3} - 1}{\\sqrt{3} + 1}", "a = 2 and b = -1", "2 - \\sqrt{3}"),
            ("\\frac{\\sqrt{3} + 1}{\\sqrt{3} - 1}", "a = 2 and b = 1", "2 + \\sqrt{3}"),
            ("\\frac{\\sqrt{5} - 1}{\\sqrt{5} + 1}", "a = 3/2 and b = -1/2", "\\frac{3 - \\sqrt{5}}{2}"),
            ("\\frac{\\sqrt{5} + 1}{\\sqrt{5} - 1}", "a = 3/2 and b = 1/2", "\\frac{3 + \\sqrt{5}}{2}"),
            ("\\frac{3 - \\sqrt{5}}{3 + \\sqrt{5}}", "a = 7/2 and b = -3/2", "\\frac{7 - 3\\sqrt{5}}{2}"),
            ("\\frac{3 + \\sqrt{5}}{3 - \\sqrt{5}}", "a = 7/2 and b = 3/2", "\\frac{7 + 3\\sqrt{5}}{2}"),
            ("\\frac{\\sqrt{2} - 1}{\\sqrt{2} + 1}", "a = 3 and b = -2", "3 - 2\\sqrt{2}"),
            ("\\frac{\\sqrt{2} + 1}{\\sqrt{2} - 1}", "a = 3 and b = 2", "3 + 2\\sqrt{2}"),
            ("\\frac{5 + 2\\sqrt{3}}{7 + 4\\sqrt{3}}", "a = 11 and b = -6", "11 - 6\\sqrt{3}"),
            ("\\frac{4 + 3\\sqrt{5}}{4 - 3\\sqrt{5}}", "a = -61/29 and b = -24/29", "\\frac{-61 - 24\\sqrt{5}}{29}")
        ],
        'tmpls': [
            "If \\( {0} = a + b\\sqrt{{r}} \\) where \\( a \\) and \\( b \\) are rational numbers, find \\( a \\) and \\( b \\).",
            "Find the values of rational numbers \\( a \\) and \\( b \\) if \\( {0} = a + b\\sqrt{{r}} \\).",
            "Determine \\( a \\) and \\( b \\) such that \\( {0} = a + b\\sqrt{{r}} \\):",
            "Equating \\( {0} = a + b\\sqrt{{r}} \\), what are \\( a \\) and \\( b \\)?",
            "Calculate the rational constants \\( a \\) and \\( b \\) from \\( {0} \\):",
            "Solve for \\( a \\) and \\( b \\) given \\( {0} = a + b\\sqrt{{r}} \\):",
            "What are the rational values of \\( a \\) and \\( b \\) in \\( {0} = a + b\\sqrt{{r}} \\)?",
            "Find \\( a \\) and \\( b \\) after rationalising: \\( {0} = a + b\\sqrt{{r}} \\):",
            "Compute \\( a \\) and \\( b \\) given \\( {0} \\):",
            "Identify \\( a \\) and \\( b \\) from the rationalised form of \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("b = -", "b = ") if "b = -" in item[1] else item[1].replace("b = ", "b = -"),
                item[1].replace("a = ", "a = -"),
                "a = 0 and b = 1"
            ],
            f"**Step 1: Rationalise the left-hand side.**\nMultiply numerator and denominator by the conjugate of the denominator.\n\n**Step 2: Simplify and express in form \\( A + B\\sqrt{{r}} \\).**\n\\( {item[0]} = {item[2]} \\).\n\n**Step 3: Equate rational and irrational parts.**\nCompare with \\( a + b\\sqrt{{r}} \\) to determine \\( a \\) and \\( b \\).\n\n**Step 4: State the values.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 3: Given x = a + √b, find x + 1/x or x² + 1/x²
    arch3 = {
        'data': [
            ("x = 2 + \\sqrt{3}", "x + 1/x", "4", "1/x = 2 - \\sqrt{3}"),
            ("x = 2 + \\sqrt{3}", "x - 1/x", "2\\sqrt{3}", "1/x = 2 - \\sqrt{3}"),
            ("x = 2 + \\sqrt{3}", "x^2 + 1/x^2", "14", "(x + 1/x)² - 2 = 16 - 2"),
            ("x = 3 + 2\\sqrt{2}", "x + 1/x", "6", "1/x = 3 - 2\\sqrt{2}"),
            ("x = 3 + 2\\sqrt{2}", "x^2 + 1/x^2", "34", "6² - 2 = 36 - 2"),
            ("x = \\sqrt{2} + 1", "x + 1/x", "2\\sqrt{2}", "1/x = \\sqrt{2} - 1"),
            ("x = \\sqrt{2} + 1", "x - 1/x", "2", "(\\sqrt{2}+1) - (\\sqrt{2}-1) = 2"),
            ("x = \\sqrt{3} + \\sqrt{2}", "x + 1/x", "2\\sqrt{3}", "1/x = \\sqrt{3} - \\sqrt{2}"),
            ("x = \\sqrt{5} + 2", "x + 1/x", "2\\sqrt{5}", "1/x = \\sqrt{5} - 2"),
            ("x = 4 + \\sqrt{15}", "x + 1/x", "8", "1/x = 4 - \\sqrt{15}")
        ],
        'tmpls': [
            "If \\( {0} \\), find the value of \\( {1} \\).",
            "Given \\( {0} \\), what is the value of \\( {1} \\)?",
            "Calculate \\( {1} \\) given that \\( {0} \\):",
            "Determine \\( {1} \\) when \\( {0} \\):",
            "For \\( {0} \\), evaluate \\( {1} \\):",
            "Compute the value of \\( {1} \\) if \\( {0} \\):",
            "Find the numerical result of \\( {1} \\) for \\( {0} \\):",
            "Solve for \\( {1} \\) given \\( {0} \\):",
            "The value of \\( {1} \\) when \\( {0} \\) is:",
            "What is \\( {1} \\) if \\( {0} \\)?"
        ],
        'calc': lambda item: (
            item[2],
            [
                str(int(item[2]) + 2) if item[2].isdigit() else item[2].replace("2", "4"),
                str(int(item[2]) - 2) if item[2].isdigit() else item[2].replace("\\sqrt{", "3\\sqrt{"),
                "0"
            ],
            f"**Step 1: Rationalise \\( 1/x \\).**\n{item[3]}.\n\n**Step 2: Add, subtract, or square as requested.**\nCombine \\( x \\) and \\( 1/x \\).\n\n**Step 3: State the final calculated value.**\nThe value is \\( {item[2]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 4: Rationalising non-unit numerators: (a + b√c) / (d + e√c)
    arch4 = {
        'data': [
            ("\\frac{5}{\\sqrt{3} - \\sqrt{5}}", "-\\frac{5(\\sqrt{3} + \\sqrt{5})}{2}", 3, 5, -2),
            ("\\frac{6}{\\sqrt{5} - \\sqrt{2}}", "2(\\sqrt{5} + \\sqrt{2})", 5, 2, 3),
            ("\\frac{2}{\\sqrt{7} - \\sqrt{5}}", "\\sqrt{7} + \\sqrt{5}", 7, 5, 2),
            ("\\frac{4}{\\sqrt{6} - \\sqrt{2}}", "\\sqrt{6} + \\sqrt{2}", 6, 2, 4),
            ("\\frac{8}{\\sqrt{11} - \\sqrt{3}}", "\\sqrt{11} + \\sqrt{3}", 11, 3, 8),
            ("\\frac{3}{\\sqrt{7} - 2}", "\\sqrt{7} + 2", 7, 4, 3),
            ("\\frac{12}{3 - \\sqrt{3}}", "2(3 + \\sqrt{3})", 9, 3, 6),
            ("\\frac{10}{\\sqrt{7} - \\sqrt{2}}", "2(\\sqrt{7} + \\sqrt{2})", 7, 2, 5),
            ("\\frac{9}{\\sqrt{13} - 2}", "\\sqrt{13} + 2", 13, 4, 9),
            ("\\frac{14}{\\sqrt{11} - 2}", "2(\\sqrt{11} + 2)", 11, 4, 7)
        ],
        'tmpls': [
            "Rationalise the denominator of \\( {0} \\) and simplify completely.",
            "Simplify \\( {0} \\) by rationalising its denominator:",
            "What is the simplified form of \\( {0} \\) after rationalising?",
            "Convert \\( {0} \\) to an expression with a rational denominator:",
            "Evaluate \\( {0} \\) by rationalising the denominator:",
            "Determine the simplest form of \\( {0} \\):",
            "The expression \\( {0} \\) with rationalised denominator is:",
            "Rationalise: \\( {0} \\):",
            "Find the equivalent simplified expression for \\( {0} \\):",
            "Compute the rationalised form of \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("+", "-"),
                item[1].replace("2(", "3("),
                "1"
            ],
            f"**Step 1: Multiply numerator and denominator by the conjugate.**\nMultiply both top and bottom by the conjugate of the denominator.\n\n**Step 2: Simplify the denominator.**\nDenominator = \\( {item[2]} - {item[3]} = {item[4]} \\).\n\n**Step 3: Cancel common numerical factors.**\nDivide the numerator by the denominator.\n\nThe simplified expression is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 5: Sum of two rationalised fractions (telescoping / canceling terms)
    arch5 = {
        'data': [
            ("\\frac{1}{\\sqrt{2} + 1} + \\frac{1}{\\sqrt{3} + \\sqrt{2}}", "\\sqrt{3} - 1", "(\\sqrt{2} - 1) + (\\sqrt{3} - \\sqrt{2})"),
            ("\\frac{1}{2 + \\sqrt{3}} + \\frac{1}{2 - \\sqrt{3}}", "4", "(2 - \\sqrt{3}) + (2 + \\sqrt{3}) = 4"),
            ("\\frac{1}{3 + \\sqrt{8}} + \\frac{1}{3 - \\sqrt{8}}", "6", "(3 - \\sqrt{8}) + (3 + \\sqrt{8}) = 6"),
            ("\\frac{1}{\\sqrt{5} + \\sqrt{3}} + \\frac{1}{\\sqrt{5} - \\sqrt{3}}", "\\sqrt{5}", "\\frac{\\sqrt{5}-\\sqrt{3} + \\sqrt{5}+\\sqrt{3}}{2} = \\sqrt{5}"),
            ("\\frac{1}{\\sqrt{7} + \\sqrt{6}} + \\frac{1}{\\sqrt{8} + \\sqrt{7}}", "\\sqrt{8} - \\sqrt{6} = 2\\sqrt{2} - \\sqrt{6}", "(\\sqrt{7}-\\sqrt{6}) + (\\sqrt{8}-\\sqrt{7})"),
            ("\\frac{1}{1 + \\sqrt{2}} + \\frac{1}{\\sqrt{2} + \\sqrt{3}} + \\frac{1}{\\sqrt{3} + \\sqrt{4}}", "1", "(\\sqrt{2}-1) + (\\sqrt{3}-\\sqrt{2}) + (2-\\sqrt{3}) = 1"),
            ("\\frac{1}{\\sqrt{3} + 1} - \\frac{1}{\\sqrt{3} - 1}", "-1", "\\frac{\\sqrt{3}-1 - (\\sqrt{3}+1)}{2} = -2/2 = -1"),
            ("\\frac{1}{4 + \\sqrt{15}} + \\frac{1}{4 - \\sqrt{15}}", "8", "(4 - \\sqrt{15}) + (4 + \\sqrt{15}) = 8"),
            ("\\frac{1}{\\sqrt{5} + 2} + \\frac{1}{\\sqrt{5} - 2}", "2\\sqrt{5}", "(\\sqrt{5}-2) + (\\sqrt{5}+2) = 2\\sqrt{5}"),
            ("\\frac{1}{\\sqrt{10} + 3} + \\frac{1}{\\sqrt{10} - 3}", "2\\sqrt{10}", "(\\sqrt{10}-3) + (\\sqrt{10}+3) = 2\\sqrt{10}")
        ],
        'tmpls': [
            "Simplify the expression \\( {0} \\) by rationalising each term.",
            "Evaluate the sum \\( {0} \\):",
            "What is the simplified value of \\( {0} \\)?",
            "Calculate \\( {0} \\):",
            "Determine the result of \\( {0} \\):",
            "The sum of rationalised fractions \\( {0} \\) equals:",
            "Find the numerical value of \\( {0} \\):",
            "Simplify completely: \\( {0} \\):",
            "Compute \\( {0} \\):",
            "What does \\( {0} \\) simplify to?"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace("+", "-") if "+" in item[1] else item[1] + " + 1",
                "0",
                "2"
            ],
            f"**Step 1: Rationalise each fraction independently.**\nMultiply each fraction's numerator and denominator by its conjugate.\n\n**Step 2: Add or subtract the rationalised expressions.**\n\\( {item[2]} \\).\n\n**Step 3: State the final simplified value.**\nThe result is \\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 6: Rationalising denominators with 3 terms: 1 / (1 + √2 + √3)
    arch6 = {
        'data': [
            ("The rationalising factor (conjugate) of a + b is:", "a - b", ["a + b", "-a - b", "1/(a + b)"]),
            ("The rationalising factor of √a + √b is:", "√a - √b", ["√a + √b", "-√a - √b", "a - b"]),
            ("The rationalising factor of 3 - √5 is:", "3 + √5", ["3 - √5", "-3 - √5", "5 - √3"]),
            ("The rationalising factor of √7 + 2 is:", "√7 - 2", ["√7 + 2", "2 - √7", "7 - √2"]),
            ("Why do we rationalise the denominator of a fraction containing surds?", "To make the denominator a rational number, making arithmetic division and estimation easier", ["To make the number an integer", "To eliminate the square root completely from the number", "Because fractions cannot have surds"]),
            ("When 1 / (√a + √b) is multiplied by (√a - √b) / (√a - √b), the value of the fraction:", "remains unchanged (multiplied by 1)", ["doubles", "is squared", "becomes rational"]),
            ("The conjugate of -3 + √2 is:", "-3 - √2", ["3 + √2", "3 - √2", "√2 - 3"]),
            ("The conjugate of √5 - 3 is:", "√5 + 3", ["-√5 - 3", "3 - √5", "5 - √3"]),
            ("The product of any real binomial surd and its conjugate is always:", "a rational number", ["an irrational number", "an imaginary number", "zero"]),
            ("To rationalise 1 / (√2 + √3 + √5), the grouping used in the first step is:", "(√2 + √3) as the first term and √5 as the second term", ["all three terms multiplied together", "cannot be rationalised", "only square the entire fraction"])
        ],
        'tmpls': [
            "{0}",
            "In rationalisation theory: {0}",
            "Regarding rationalising factors and conjugate surds: {0}",
            "Choose the correct statement: {0}",
            "Identify the accurate fact: {0}",
            "Select the correct answer: {0}",
            "Determine the true statement: {0}",
            "Which option correctly describes: {0}?",
            "State the mathematical truth: {0}",
            "What is the correct concept concerning: {0}?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand the definition of a conjugate surd.**\nFor any binomial expression \\( x + y \\), its conjugate is \\( x - y \\).\nTheir product \\( (x + y)(x - y) = x^2 - y^2 \\) is free of radicals.\n\n**Step 2: Evaluate the statement.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Application of rationalisation to solve x² + 1/x² - 2
    arch7 = {
        'data': [
            ("x = 3 + 2\\sqrt{2}", "(x - 1/x)²", "32", "x - 1/x = 4\\sqrt{2} => (4\\sqrt{2})² = 32"),
            ("x = 2 + \\sqrt{3}", "(x - 1/x)²", "12", "x - 1/x = 2\\sqrt{3} => (2\\sqrt{3})² = 12"),
            ("x = \\sqrt{2} + 1", "(x + 1/x)²", "8", "x + 1/x = 2\\sqrt{2} => (2\\sqrt{2})² = 8"),
            ("x = \\sqrt{5} + 2", "(x - 1/x)²", "16", "x - 1/x = 4 => 4² = 16"),
            ("x = 4 + \\sqrt{15}", "(x - 1/x)²", "60", "x - 1/x = 2\\sqrt{15} => (2\\sqrt{15})² = 60"),
            ("x = 3 + \\sqrt{8}", "x² + 1/x²", "34", "x + 1/x = 6 => 6² - 2 = 34"),
            ("x = 5 + 2\\sqrt{6}", "x + 1/x", "10", "1/x = 5 - 2\\sqrt{6} => 5 + 5 = 10"),
            ("x = 5 + 2\\sqrt{6}", "x² + 1/x²", "98", "10² - 2 = 98"),
            ("x = 7 + 4\\sqrt{3}", "\\sqrt{x} + 1/\\sqrt{x}", "4", "x = (2+\\sqrt{3})² => \\sqrt{x} = 2+\\sqrt{3}"),
            ("x = 9 + 4\\sqrt{5}", "\\sqrt{x} + 1/\\sqrt{x}", "2\\sqrt{5}", "x = (\\sqrt{5}+2)² => \\sqrt{x} = \\sqrt{5}+2")
        ],
        'tmpls': [
            "If \\( {0} \\), find the value of \\( {1} \\).",
            "Given \\( {0} \\), evaluate \\( {1} \\):",
            "Calculate \\( {1} \\) given that \\( {0} \\):",
            "Determine \\( {1} \\) when \\( {0} \\):",
            "For \\( {0} \\), find the numerical value of \\( {1} \\):",
            "Compute \\( {1} \\) if \\( {0} \\):",
            "Solve for \\( {1} \\) from \\( {0} \\):",
            "Find the value of \\( {1} \\) given \\( {0} \\):",
            "What is \\( {1} \\) when \\( {0} \\)?",
            "Evaluate \\( {1} \\) for \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[2],
            [
                str(int(item[2]) + 2) if item[2].isdigit() else item[2].replace("2", "4"),
                str(int(item[2]) - 4) if item[2].isdigit() else "0",
                "1"
            ],
            f"**Step 1: Rationalise \\( 1/x \\).**\nFind \\( 1/x \\) using the conjugate.\n\n**Step 2: Form the base expression.**\nCalculate \\( x + 1/x \\) or \\( x - 1/x \\).\n\n**Step 3: Square or simplify as required.**\n{item[3]}.\n\nThe value is \\( {item[2]} \\)."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])

if __name__ == "__main__":
    q1 = gen_3_3_1()
    q2 = gen_3_3_2()
    print(f"gen_3_3_1: {len(q1)} questions generated")
    print(f"gen_3_3_2: {len(q2)} questions generated")
