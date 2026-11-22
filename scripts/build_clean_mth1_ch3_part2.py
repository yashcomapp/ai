import json
from engine_algebra import generate_subtopic

CH_NUM = 3
CH_NAME = "Polynomials"

def gen_3_4_1():
    tc = "MH-9-MTH1-3-3.4.1"
    tname = "Evaluating p(x) for x = a"
    
    archs = [
        # Arch 0: Quadratic evaluation p(a) for a > 0
        {
            'data': [
                ("x^2 + 3x - 5", "x = 2", "5", ["7", "-3", "1"]),
                ("2x^2 - 4x + 7", "x = 3", "13", ["11", "15", "7"]),
                ("3x^2 + x - 8", "x = 2", "6", ["8", "10", "4"]),
                ("x^2 - 6x + 9", "x = 3", "0", ["3", "9", "-3"]),
                ("4x^2 - 5x + 1", "x = 1", "0", ["1", "4", "-1"]),
                ("5x^2 + 2x - 3", "x = 2", "21", ["17", "23", "19"]),
                ("x^2 + 8x + 12", "x = 1", "21", ["20", "12", "15"]),
                ("3x^2 - 7x + 2", "x = 4", "22", ["20", "24", "18"]),
                ("2x^2 + 5x - 11", "x = 3", "22", ["19", "25", "16"]),
                ("x^2 - 9x + 20", "x = 5", "0", ["5", "-5", "20"])
            ],
            'tmpls': [
                "For the polynomial \\(p(x) = {0}\\), find the value \\(p({1})\\):",
                "Evaluate the polynomial \\(p(x) = {0}\\) at the positive value \\({1}\\):",
                "If \\(p(x) = {0}\\), calculate the numerical output when \\({1}\\):",
                "Find the value of \\({0}\\) by substituting \\({1}\\):",
                "What is \\(p(a)\\) for \\(p(x) = {0}\\) at \\({1}\\)?",
                "Evaluate \\(p(x) = {0}\\) directly for the given value \\({1}\\):",
                "Compute the arithmetic value of \\({0}\\) at \\({1}\\):",
                "Determine \\(p(x)\\) for \\(p(x) = {0}\\) when variable is set to \\({1}\\):",
                "Calculate the evaluated value of \\(p(x) = {0}\\) at \\({1}\\):",
                "Find \\(p({1})\\) given the algebraic expression \\(p(x) = {0}\\):"
            ],
            'calc': lambda item: (
                item[2],
                item[3],
                "**Step 1: Substitute the Given Value**\nReplace variable with " + str(item[1]) + " in \\(" + str(item[0]) + "\\).\n**Step 2: Simplify Arithmetic**\nCompute terms and combine.\n**Step 3: Conclusion**\nValue is " + str(item[2]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Evaluation at negative values x = -a
        {
            'data': [
                ("x^2 - 4x + 3", "x = -1", "8", ["6", "0", "-2"]),
                ("2x^2 + 5x - 7", "x = -2", "-9", ["-7", "-5", "9"]),
                ("3x^2 - 2x + 4", "x = -1", "9", ["5", "7", "-1"]),
                ("x^3 + 2x^2 - 5x + 1", "x = -2", "11", ["9", "13", "-1"]),
                ("x^3 - 3x^2 + 4x - 6", "x = -1", "-14", ["-12", "-10", "14"]),
                ("4x^2 + 7x - 2", "x = -3", "13", ["11", "-13", "15"]),
                ("2x^3 - x^2 + 3x - 5", "x = -1", "-11", ["-9", "-7", "11"]),
                ("x^2 + 6x + 8", "x = -2", "0", ["4", "-4", "8"]),
                ("5x^2 - 3x + 2", "x = -1", "10", ["8", "4", "-6"]),
                ("x^3 + 4x^2 + x - 6", "x = -3", "0", ["6", "-6", "3"])
            ],
            'tmpls': [
                "Evaluate the polynomial \\(p(x) = {0}\\) for negative integer input \\({1}\\):",
                "Find \\(p({1})\\) for the negative argument in \\(p(x) = {0}\\):",
                "If \\(p(x) = {0}\\), compute \\(p(x)\\) specifically when \\({1}\\):",
                "Calculate the value of \\({0}\\) at negative coordinate \\({1}\\):",
                "What is the output of \\(p(x) = {0}\\) for negative \\({1}\\)?",
                "Determine the value of \\(p(x) = {0}\\) when variable is negative: \\({1}\\):",
                "Evaluate the sign-sensitive polynomial \\({0}\\) at \\({1}\\):",
                "Carefully find \\(p({1})\\) if \\(p(x) = {0}\\):",
                "Compute the value of expression \\({0}\\) for negative input \\({1}\\):",
                "Determine \\(p(x)\\) for the polynomial \\(p(x) = {0}\\) evaluated at \\({1}\\):"
            ],
            'calc': lambda item: (
                item[2],
                item[3],
                "**Step 1: Substitute Negative Value**\nCarefully apply power signs: negative squared is positive, negative cubed is negative.\n**Step 2: Combine Values**\nSum the resulting integers.\n**Step 3: Conclusion**\nResult is " + str(item[2]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 2: Evaluation at zero x = 0 (Constant term)
        {
            'data': [
                ("3x^4 - 5x^2 + 7x - 12", "x = 0", "-12", ["0", "7", "12"]),
                ("x^5 + 4x^3 - 8x + 25", "x = 0", "25", ["0", "8", "-25"]),
                ("7x^3 - 2x^2 + 11", "x = 0", "11", ["0", "-2", "7"]),
                ("4x^2 - 9x", "x = 0", "0", ["4", "-9", "1"]),
                ("-2x^6 + 3x^4 - x^2 + 18", "x = 0", "18", ["0", "3", "-18"]),
                ("5x^3 - x + 9", "x = 0", "9", ["0", "5", "-9"]),
                ("8x^2 + 14x - 3", "x = 0", "-3", ["0", "14", "8"]),
                ("x^4 - 16", "x = 0", "-16", ["0", "16", "-4"]),
                ("9x^3 + 6x^2 - 2x", "x = 0", "0", ["9", "6", "-2"]),
                ("2x^5 - 7x + 1", "x = 0", "1", ["0", "2", "-7"])
            ],
            'tmpls': [
                "Find \\(p(0)\\) for the polynomial \\(p(x) = {0}\\):",
                "What is the value of \\(p(x) = {0}\\) when variable \\({1}\\)?",
                "Evaluate \\(p(0)\\) for the given expression \\(p(x) = {0}\\):",
                "Calculate \\(p(x)\\) for \\(p(x) = {0}\\) at zero: \\({1}\\):",
                "The value of \\(p(0)\\) for \\(p(x) = {0}\\) corresponds to the constant:",
                "Determine \\(p(0)\\) if the polynomial is \\(p(x) = {0}\\):",
                "Compute the value of \\({0}\\) at zero input \\({1}\\):",
                "If \\(p(x) = {0}\\), state the constant value \\(p(0)\\):",
                "Evaluate the polynomial \\({0}\\) at \\({1}\\):",
                "Find the numerical constant value of \\(p(x) = {0}\\) for \\({1}\\):"
            ],
            'calc': lambda item: (
                item[2],
                item[3],
                "**Step 1: Set x = 0**\nAll terms with variable x vanish to 0.\n**Step 2: Read Constant Term**\nThe remaining value is the constant term.\n**Step 3: Conclusion**\n\\(p(0) = " + str(item[2]) + "\\)."
            ),
            'diff': 'easy'
        },
        # Arch 3: Evaluation at fractional inputs x = 1/2, -1/2, 1/3
        {
            'data': [
                ("4x^2 + 2x - 1", "x = \\frac{1}{2}", "1", ["0", "2", "-1"]),
                ("2x^2 - 5x + 2", "x = \\frac{1}{2}", "0", ["1", "-1", "2"]),
                ("4x^2 - 6x + 3", "x = \\frac{1}{2}", "1", ["2", "0", "-1"]),
                ("9x^2 - 3x + 1", "x = \\frac{1}{3}", "1", ["0", "2", "-1"]),
                ("8x^3 - 4x^2 + 2x - 1", "x = \\frac{1}{2}", "0", ["1", "-1", "2"]),
                ("4x^2 + 4x + 1", "x = -\\frac{1}{2}", "0", ["1", "2", "-1"]),
                ("6x^2 + x - 2", "x = \\frac{1}{2}", "0", ["1", "-1", "2"]),
                ("9x^2 + 6x + 1", "x = -\\frac{1}{3}", "0", ["1", "2", "-1"]),
                ("2x^2 + 3x - 2", "x = \\frac{1}{2}", "0", ["1", "-1", "2"]),
                ("8x^2 - 2x - 1", "x = \\frac{1}{2}", "0", ["1", "2", "-1"])
            ],
            'tmpls': [
                "Evaluate the polynomial \\(p(x) = {0}\\) for rational fraction \\({1}\\):",
                "Find the fractional evaluation \\(p({1})\\) for \\(p(x) = {0}\\):",
                "If \\(p(x) = {0}\\), calculate \\(p(x)\\) when rational variable \\({1}\\):",
                "What is the evaluated output of \\({0}\\) at fraction \\({1}\\)?",
                "Determine the rational value \\(p({1})\\) if \\(p(x) = {0}\\):",
                "Calculate \\(p(x) = {0}\\) at fractional value \\({1}\\):",
                "Evaluate the polynomial fraction problem \\({0}\\) at \\({1}\\):",
                "Compute the fraction \\(p({1})\\) for \\(p(x) = {0}\\):",
                "Find the value of \\(p(x) = {0}\\) for rational \\({1}\\):",
                "Solve for the fraction \\(p({1})\\) in \\(p(x) = {0}\\):"
            ],
            'calc': lambda item: (
                item[2],
                item[3],
                "**Step 1: Substitute the Fraction**\nSquare or cube the fraction.\n**Step 2: Simplify Terms**\nMultiply by coefficients and sum.\n**Step 3: Conclusion**\nValue is " + str(item[2]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 4: Zero of a polynomial definition
        {
            'data': [
                ("If \\(p(a) = 0\\), what is 'a' called with respect to \\(p(x)\\)?", "A zero (or root) of the polynomial \\(p(x)\\)", ["The degree of p(x)", "The leading coefficient", "The remainder"]),
                ("Is \\(x = 2\\) a zero of \\(p(x) = x^2 - 5x + 6\\)?", "Yes, because \\(p(2) = 4 - 10 + 6 = 0\\)", ["No, p(2) is positive", "No, p(2) = 6", "Cannot be determined"]),
                ("Is \\(x = -1\\) a zero of \\(p(x) = x^3 + 1\\)?", "Yes, because \\((-1)^3 + 1 = -1 + 1 = 0\\)", ["No, (-1)^3 + 1 = 2", "No, roots cannot be negative", "Only if x = 1"]),
                ("How many zeros can a polynomial of degree n have at most?", "At most n zeros (Fundamental Theorem of Algebra)", ["Exactly n + 1 zeros", "Infinitely many zeros", "At most 1 zero"]),
                ("Does a non-zero constant polynomial like \\(p(x) = 7\\) have any zeros?", "No, it has no zeros (it never equals 0 for any x)", ["Yes, x = 7 is a zero", "Yes, infinitely many zeros", "Yes, x = 0 is a zero"]),
                ("What are the zeros of the zero polynomial \\(p(x) = 0\\)?", "Every real number is a zero", ["Only 0", "No zeros exist", "Only positive integers"]),
                ("Find the zero of the linear polynomial \\(p(x) = 2x - 6\\):", "\\(x = 3\\) (since \\(2x - 6 = 0 \\implies 2x = 6 \\implies x = 3\\))", ["x = -3", "x = 6", "x = 2"]),
                ("Find the zero of \\(p(x) = 5x + 10\\):", "\\(x = -2\\)", ["x = 2", "x = -5", "x = 5"]),
                ("Is \\(x = 3\\) a zero of \\(p(x) = x^2 - 9\\)?", "Yes, because \\(3^2 - 9 = 9 - 9 = 0\\)", ["No, p(3) = 9", "No, only -3 is a zero", "Cannot be verified"]),
                ("If a number 'c' is a zero of \\(p(x)\\), then what is a factor of \\(p(x)\\)?", "\\(x - c\\) is a factor", ["\\(x + c\\)", "\\(cx\\)", "\\(x^2 - c\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the zero concept: {0}",
                "Select the correct statement: {0}",
                "Determine the true mathematical fact: {0}",
                "Answer the polynomial root question: {0}",
                "Choose the right conclusion: {0}",
                "Solve the zero property problem: {0}",
                "State the correct answer: {0}",
                "Which option correctly answers: {0}",
                "Analyze the root condition: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Definition of Zero of a Polynomial**\nA number 'a' is a zero of \\(p(x)\\) if and only if \\(p(a) = 0\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 5: Finding unknown parameter m from p(a) = val
        {
            'data': [
                ("p(x) = x^2 - mx + 7", "x = 2", "p(2) = 3", "m = 4 (since \\(4 - 2m + 7 = 3 \\implies 11 - 2m = 3 \\implies 2m = 8 \\implies m = 4\\))", ["m = -4", "m = 2", "m = 5"]),
                ("p(x) = 2x^2 + mx - 5", "x = 1", "p(1) = 0", "m = 3 (since \\(2 + m - 5 = 0 \\implies m - 3 = 0 \\implies m = 3\\))", ["m = -3", "m = 5", "m = 2"]),
                ("p(x) = x^3 - 3x^2 + mx - 8", "x = 2", "p(2) = 0", "m = 6 (since \\(8 - 12 + 2m - 8 = 0 \\implies 2m - 12 = 0 \\implies m = 6\\))", ["m = -6", "m = 4", "m = 3"]),
                ("p(x) = mx^2 - 5x + 6", "x = 2", "p(2) = 4", "m = 2 (since \\(4m - 10 + 6 = 4 \\implies 4m - 4 = 4 \\implies 4m = 8 \\implies m = 2\\))", ["m = -2", "m = 1", "m = 4"]),
                ("p(x) = x^2 + 4x + m", "x = -1", "p(-1) = 6", "m = 9 (since \\(1 - 4 + m = 6 \\implies m - 3 = 6 \\implies m = 9\\))", ["m = -9", "m = 3", "m = 7"]),
                ("p(x) = 3x^2 - mx + 2", "x = 1", "p(1) = 1", "m = 4 (since \\(3 - m + 2 = 1 \\implies 5 - m = 1 \\implies m = 4\\))", ["m = -4", "m = 2", "m = 5"]),
                ("p(x) = x^3 + mx^2 - 2x + 1", "x = -1", "p(-1) = 4", "m = 2 (since \\(-1 + m + 2 + 1 = 4 \\implies m + 2 = 4 \\implies m = 2\\))", ["m = -2", "m = 4", "m = 1"]),
                ("p(x) = 2x^2 - 7x + m", "x = 3", "p(3) = 0", "m = 3 (since \\(18 - 21 + m = 0 \\implies m - 3 = 0 \\implies m = 3\\))", ["m = -3", "m = 0", "m = 6"]),
                ("p(x) = mx^3 - 2x^2 + 5", "x = 1", "p(1) = 7", "m = 4 (since \\(m - 2 + 5 = 7 \\implies m + 3 = 7 \\implies m = 4\\))", ["m = -4", "m = 2", "m = 5"]),
                ("p(x) = x^2 - 6x + m", "x = 3", "p(3) = -2", "m = 7 (since \\(9 - 18 + m = -2 \\implies m - 9 = -2 \\implies m = 7\\))", ["m = -7", "m = 5", "m = 9"])
            ],
            'tmpls': [
                "For \\({0}\\), if {2}, find the value of m:",
                "If {2} for the polynomial \\({0}\\), determine m:",
                "Find m such that \\({0}\\) satisfies {2}:",
                "Evaluate m if {2} in \\({0}\\):",
                "Calculate m given that {2} for \\({0}\\):",
                "Determine the unknown coefficient m if {2} for \\({0}\\):",
                "Compute m from the condition {2} in \\({0}\\):",
                "Solve for m if \\({0}\\) evaluated at {1} gives {2}:",
                "What is the value of m if {2} for \\({0}\\)?",
                "Find the parameter m when {2} holds for \\({0}\\):"
            ],
            'calc': lambda item: (
                item[3],
                item[4],
                "**Step 1: Set Up Equation**\nSubstitute \\(" + str(item[1]) + "\\) into \\(" + str(item[0]) + "\\) and equate to the given value.\n**Step 2: Solve for m**\n" + str(item[3]) + ".\n**Step 3: Conclusion**\n" + str(item[3]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 6: Symmetry and parity evaluations p(a) + p(-a)
        {
            'data': [
                ("p(x) = x^2 + 5", "p(2) + p(-2)", "18 (since \\(p(2) = 9\\) and \\(p(-2) = 9\\), \\(9 + 9 = 18\\))", ["9", "0", "14"]),
                ("p(x) = x^3 - 2x", "p(3) + p(-3)", "0 (odd polynomial, \\(p(-x) = -p(x)\\))", ["42", "21", "-21"]),
                ("p(x) = 2x^2 - 3", "p(1) + p(-1)", "-2 (since both equal \\(-1\\), \\(-1 + -1 = -2\\))", ["0", "-1", "2"]),
                ("p(x) = x^4 + 3", "p(2) - p(-2)", "0 (even polynomial, \\(p(2) = p(-2) = 19\\))", ["38", "19", "-19"]),
                ("p(x) = 3x^3 + x", "p(1) + p(-1)", "0 (since \\(p(1) = 4\\) and \\(p(-1) = -4\\))", ["8", "4", "-4"]),
                ("p(x) = 5x^2 + 4", "p(2) - p(-2)", "0 (even polynomial has \\(p(a) = p(-a)\\))", ["48", "24", "12"]),
                ("p(x) = x^2 - 3x + 2", "p(1) + p(2)", "0 (since \\(p(1) = 0\\) and \\(p(2) = 0\\))", ["1", "2", "-2"]),
                ("p(x) = 2x - 5", "p(3) + p(0)", "-4 (since \\(p(3) = 1\\) and \\(p(0) = -5\\), \\(1 + (-5) = -4\\))", ["-5", "1", "6"]),
                ("p(x) = x^2 + x + 1", "p(1) - p(-1)", "2 (since \\(p(1) = 3\\) and \\(p(-1) = 1\\), \\(3 - 1 = 2\\))", ["0", "4", "-2"]),
                ("p(x) = 4x^3 - x", "p(2) + p(-2)", "0", ["60", "30", "-30"])
            ],
            'tmpls': [
                "For \\({0}\\), calculate the value of \\({1}\\):",
                "Evaluate \\({1}\\) for \\({0}\\):",
                "If \\({0}\\), find the sum or difference \\({1}\\):",
                "Compute \\({1}\\) for the polynomial \\({0}\\):",
                "Determine the value of \\({1}\\) given \\({0}\\):",
                "What is \\({1}\\) for \\({0}\\)?",
                "Calculate \\({1}\\) if \\({0}\\):",
                "Find \\({1}\\) using \\({0}\\):",
                "Solve for \\({1}\\) in \\({0}\\):",
                "Evaluate the expression \\({1}\\) for \\({0}\\):"
            ],
            'calc': lambda item: (
                item[2],
                item[3],
                "**Step 1: Evaluate Each Term Separately**\nCompute \\(p(a)\\) and \\(p(-a)\\).\n**Step 2: Add or Subtract**\nCombine the calculated values.\n**Step 3: Conclusion**\n" + str(item[2]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Conceptual properties of polynomial evaluations
        {
            'data': [
                ("If \\(p(x)\\) is a polynomial such that \\(p(a) = p(b) = 0\\) with \\(a \\ne b\\), what can be concluded?", "\\((x - a)(x - b)\\) is a factor of \\(p(x)\\)", ["p(x) must be a constant", "p(x) cannot have degree greater than 2", "a must equal -b"]),
                ("What is \\(p(1)\\) for any polynomial \\(p(x) = a_n x^n + \\dots + a_1 x + a_0\\)?", "The sum of all coefficients \\(a_n + a_{n-1} + \\dots + a_0\\)", ["The leading coefficient", "The constant term", "The degree of the polynomial"]),
                ("If the sum of all coefficients of \\(p(x)\\) is zero, what is always a zero of \\(p(x)\\)?", "\\(x = 1\\) (since \\(p(1) = 0\\))", ["x = 0", "x = -1", "No root can be inferred"]),
                ("If the sum of coefficients of even powers equals the sum of coefficients of odd powers, what is a zero?", "\\(x = -1\\) (since \\(p(-1) = 0\\))", ["x = 1", "x = 0", "x = 2"]),
                ("Can a quadratic polynomial have 3 distinct zeros?", "No, a polynomial of degree n can have at most n distinct roots", ["Yes, if coefficients are irrational", "Yes, if it has complex coefficients", "Only if it is monic"]),
                ("What is \\(p(0)\\) for the polynomial \\(p(x) = x^3 - 4x^2 + 5x\\)?", "0 (since it has no constant term)", ["5", "-4", "1"]),
                ("If \\(p(x) = 3\\) for all real x, what is \\(p(100)\\)?", "3 (it is a constant polynomial)", ["100", "300", "0"]),
                ("If \\(p(x) = (x - 2)^2\\), what is \\(p(2)\\)?", "0 (2 is a repeated zero)", ["4", "2", "-4"]),
                ("If \\(p(x) = x^2 + 1\\), does \\(p(x)\\) have any real zeros?", "No, \\(x^2 + 1 \\ge 1 > 0\\) for all real x", ["Yes, x = 1", "Yes, x = -1", "Yes, x = 0"]),
                ("For what value of x does \\(p(x) = 3x - 12\\) evaluate to 0?", "\\(x = 4\\)", ["x = -4", "x = 3", "x = 12"])
            ],
            'tmpls': [
                "{0}",
                "Answer the following conceptual question: {0}",
                "Evaluate the polynomial evaluation rule: {0}",
                "Select the correct statement: {0}",
                "Determine the true mathematical property: {0}",
                "Choose the right answer: {0}",
                "Analyze the root and evaluation concept: {0}",
                "State the correct mathematical conclusion: {0}",
                "Which option correctly answers: {0}",
                "Identify the true relationship: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Polynomial Evaluation Properties**\n\\(p(1)\\) is sum of all coefficients.\n\\(p(0)\\) is constant term.\n\\(p(a) = 0 \\iff x = a\\) is a root.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_3_4_2():
    tc = "MH-9-MTH1-3-3.4.2"
    tname = "Remainder theorem statement & verification"
    
    archs = [
        # Arch 0: Direct remainder theorem R = P(a) for (x - a)
        {
            'data': [
                ("x^3 - 2x^2 + 4x - 1", "x - 2", "7", ["5", "9", "-1"], "P(2) = 8 - 8 + 8 - 1 = 7"),
                ("2x^3 - 5x^2 + 3x - 4", "x - 1", "-4", ["-2", "-6", "4"], "P(1) = 2 - 5 + 3 - 4 = -4"),
                ("x^4 - 3x^2 + 2x + 5", "x - 2", "13", ["11", "15", "5"], "P(2) = 16 - 12 + 4 + 5 = 13"),
                ("3x^2 + 7x - 2", "x - 1", "8", ["6", "10", "-2"], "P(1) = 3 + 7 - 2 = 8"),
                ("x^3 - 6x^2 + 11x - 6", "x - 3", "0", ["3", "-3", "6"], "P(3) = 27 - 54 + 33 - 6 = 0"),
                ("2x^2 - 7x + 1", "x - 3", "-2", ["2", "-4", "1"], "P(3) = 18 - 21 + 1 = -2"),
                ("x^4 - 1", "x - 2", "15", ["16", "14", "1"], "P(2) = 16 - 1 = 15"),
                ("4x^3 - 2x + 7", "x - 1", "9", ["7", "11", "5"], "P(1) = 4 - 2 + 7 = 9"),
                ("x^3 + x^2 - x + 2", "x - 2", "12", ["10", "14", "2"], "P(2) = 8 + 4 - 2 + 2 = 12"),
                ("5x^2 - 3x + 4", "x - 2", "18", ["16", "20", "4"], "P(2) = 20 - 6 + 4 = 18")
            ],
            'tmpls': [
                "By the Remainder Theorem, find the remainder when \\(p(x) = {0}\\) is divided by \\({1}\\):",
                "What is the remainder when \\({0}\\) is divided by \\({1}\\) using Remainder Theorem?",
                "Determine the remainder for \\({0} \\div ({1})\\) via Remainder Theorem:",
                "Using the Remainder Theorem, evaluate the remainder of \\({0}\\) divided by \\({1}\\):",
                "Calculate the remainder of \\({0}\\) when divided by \\({1}\\):",
                "Find remainder R when \\({1}\\) divides \\({0}\\) by Remainder Theorem:",
                "Apply the Remainder Theorem to find the remainder of \\({0} \\div ({1})\\):",
                "Evaluate remainder using \\(R = p(a)\\) for \\({0}\\) and divisor \\({1}\\):",
                "State the remainder of \\({0}\\) divided by \\({1}\\):",
                "Compute the remainder using Remainder Theorem for \\({0} \\div ({1})\\):"
            ],
            'calc': lambda item: (
                item[2],
                item[3],
                "**Step 1: Find Root of Divisor**\nSet " + str(item[1]) + " = 0 to get x = a.\n**Step 2: Evaluate \\(p(a)\\)**\n" + str(item[4]) + ".\n**Step 3: Conclusion**\nRemainder is " + str(item[2]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Remainder theorem for (x + a)
        {
            'data': [
                ("x^3 + 3x^2 + 3x + 1", "x + 1", "0", ["1", "-1", "2"], "P(-1) = -1 + 3 - 3 + 1 = 0"),
                ("2x^2 + 5x + 4", "x + 2", "2", ["0", "-2", "4"], "P(-2) = 8 - 10 + 4 = 2"),
                ("x^3 - 4x^2 + 2x - 5", "x + 1", "-12", ["-10", "-14", "5"], "P(-1) = -1 - 4 - 2 - 5 = -12"),
                ("3x^2 + 8x + 7", "x + 2", "3", ["1", "5", "-3"], "P(-2) = 12 - 16 + 7 = 3"),
                ("x^4 - 2x^2 + 8", "x + 1", "7", ["5", "9", "8"], "P(-1) = 1 - 2 + 8 = 7"),
                ("2x^3 + x^2 - 3x + 5", "x + 2", "-1", ["1", "-3", "5"], "P(-2) = -16 + 4 + 6 + 5 = -1"),
                ("x^2 + 7x + 10", "x + 5", "0", ["5", "-5", "10"], "P(-5) = 25 - 35 + 10 = 0"),
                ("4x^2 + 3x - 2", "x + 1", "-1", ["1", "-3", "2"], "P(-1) = 4 - 3 - 2 = -1"),
                ("x^3 + 8", "x + 2", "0", ["8", "-8", "16"], "P(-2) = -8 + 8 = 0"),
                ("5x^2 + 9x - 2", "x + 2", "0", ["2", "-2", "4"], "P(-2) = 20 - 18 - 2 = 0")
            ],
            'tmpls': [
                "Find the remainder when \\(p(x) = {0}\\) is divided by \\({1}\\):",
                "By Remainder Theorem, what is the remainder of \\({0} \\div ({1})\\)?",
                "Determine the remainder when \\({0}\\) is divided by \\({1}\\):",
                "Evaluate the remainder for \\({0}\\) with divisor \\({1}\\):",
                "Calculate remainder using \\(R = p(-a)\\) for \\({0}\\) divided by \\({1}\\):",
                "What is the remainder when \\({1}\\) divides \\({0}\\)?",
                "Apply the Remainder Theorem to \\({0}\\) and \\({1}\\):",
                "Find remainder R of \\({0}\\) divided by \\({1}\\):",
                "Compute remainder using Remainder Theorem for \\({0} \\div ({1})\\):",
                "Solve for the remainder of \\({0}\\) divided by \\({1}\\):"
            ],
            'calc': lambda item: (
                item[2],
                item[3],
                "**Step 1: Set Divisor Equal to Zero**\n\\(" + str(item[1]) + " = 0 \\implies x = -a\\).\n**Step 2: Evaluate \\(p(-a)\\)**\n" + str(item[4]) + ".\n**Step 3: Conclusion**\nRemainder is " + str(item[2]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 2: Remainder theorem with divisor ax - b
        {
            'data': [
                ("2x^2 + 3x - 2", "2x - 1", "0", ["1", "-1", "2"], "P(1/2) = 2(1/4) + 3(1/2) - 2 = 1/2 + 3/2 - 2 = 0"),
                ("4x^2 - 4x + 3", "2x - 1", "2", ["1", "3", "0"], "P(1/2) = 4(1/4) - 4(1/2) + 3 = 1 - 2 + 3 = 2"),
                ("3x^2 + 5x - 2", "3x - 1", "0", ["1", "-1", "2"], "P(1/3) = 3(1/9) + 5(1/3) - 2 = 1/3 + 5/3 - 2 = 0"),
                ("2x^3 - 5x^2 + 6x - 2", "2x - 1", "0", ["1", "-1", "2"], "P(1/2) = 2(1/8) - 5(1/4) + 6(1/2) - 2 = 1/4 - 5/4 + 3 - 2 = 0"),
                ("6x^2 + 11x - 7", "2x + 3", "-10", ["10", "-8", "0"], "P(-3/2) = 6(9/4) + 11(-3/2) - 7 = 27/2 - 33/2 - 7 = -3 - 7 = -10"),
                ("4x^3 - 8x^2 + 3x + 1", "2x - 1", "1", ["0", "2", "-1"], "P(1/2) = 4(1/8) - 8(1/4) + 3(1/2) + 1 = 1/2 - 2 + 3/2 + 1 = 1"),
                ("3x^2 + 7x + 5", "3x + 1", "3", ["2", "4", "0"], "P(-1/3) = 3(1/9) + 7(-1/3) + 5 = 1/3 - 7/3 + 5 = -2 + 5 = 3"),
                ("2x^3 + 3x^2 - 1", "2x + 1", "-1", ["0", "1", "-2"], "P(-1/2) = 2(-1/8) + 3(1/4) - 1 = -1/4 + 3/4 - 1 = 1/2 - 1 = -1/2"),
                ("8x^2 - 2x + 3", "2x - 1", "4", ["3", "5", "1"], "P(1/2) = 8(1/4) - 2(1/2) + 3 = 2 - 1 + 3 = 4"),
                ("9x^2 - 6x + 5", "3x - 1", "4", ["3", "5", "2"], "P(1/3) = 9(1/9) - 6(1/3) + 5 = 1 - 2 + 5 = 4")
            ],
            'tmpls': [
                "Find the remainder when \\(p(x) = {0}\\) is divided by \\({1}\\) using Remainder Theorem:",
                "What is the remainder for \\({0} \\div ({1})\\)?",
                "By Remainder Theorem, find the remainder of \\({0}\\) divided by linear divisor \\({1}\\):",
                "Evaluate remainder of \\({0}\\) when divided by \\({1}\\):",
                "Calculate remainder for \\({0}\\) divided by \\({1}\\):",
                "Determine the remainder of \\({0} \\div ({1})\\):",
                "Apply Remainder Theorem with fractional root of \\({1}\\) to \\({0}\\):",
                "Find remainder R of \\({0}\\) divided by \\({1}\\):",
                "Compute remainder of \\({0}\\) with divisor \\({1}\\):",
                "Solve for the remainder when \\({1}\\) divides \\({0}\\):"
            ],
            'calc': lambda item: (
                item[2],
                item[3],
                "**Step 1: Find Root of Divisor**\nSet \\(" + str(item[1]) + " = 0 \\implies x = b/a\\).\n**Step 2: Evaluate \\(p(b/a)\\)**\n" + str(item[4]) + ".\n**Step 3: Conclusion**\nRemainder is " + str(item[2]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 3: Verifying Remainder Theorem with Long/Synthetic Division
        {
            'data': [
                ("Verify Remainder Theorem for \\((x^2 + 4x + 7) \\div (x - 1)\\):", "Both division and \\(p(1) = 1 + 4 + 7 = 12\\) give remainder 12", ["Remainder is 10", "Remainder is 7", "Remainder is 0"]),
                ("Verify Remainder Theorem for \\((2x^2 - 3x + 5) \\div (x - 2)\\):", "Both methods confirm remainder is \\(p(2) = 8 - 6 + 5 = 7\\)", ["Remainder is 5", "Remainder is 9", "Remainder is 3"]),
                ("Verify Remainder Theorem for \\((x^3 - 1) \\div (x - 1)\\):", "Both methods confirm remainder is \\(p(1) = 1 - 1 = 0\\)", ["Remainder is 1", "Remainder is -1", "Remainder is 2"]),
                ("Verify Remainder Theorem for \\((3x^2 + x - 4) \\div (x + 1)\\):", "Both methods confirm remainder is \\(p(-1) = 3 - 1 - 4 = -2\\)", ["Remainder is 2", "Remainder is 0", "Remainder is -4"]),
                ("Verify Remainder Theorem for \\((x^3 + 8) \\div (x + 2)\\):", "Both methods confirm remainder is \\(p(-2) = -8 + 8 = 0\\)", ["Remainder is 8", "Remainder is 16", "Remainder is -8"]),
                ("Verify Remainder Theorem for \\((x^2 - 5x + 6) \\div (x - 3)\\):", "Both methods confirm remainder is \\(p(3) = 9 - 15 + 6 = 0\\)", ["Remainder is 3", "Remainder is 6", "Remainder is 1"]),
                ("Verify Remainder Theorem for \\((4x^2 - 1) \\div (x - 1)\\):", "Both methods confirm remainder is \\(p(1) = 4 - 1 = 3\\)", ["Remainder is 1", "Remainder is 4", "Remainder is 0"]),
                ("Verify Remainder Theorem for \\((x^3 - 2x^2 + 1) \\div (x - 2)\\):", "Both methods confirm remainder is \\(p(2) = 8 - 8 + 1 = 1\\)", ["Remainder is 0", "Remainder is 2", "Remainder is -1"]),
                ("Verify Remainder Theorem for \\((2x^2 + 7x + 3) \\div (x + 3)\\):", "Both methods confirm remainder is \\(p(-3) = 18 - 21 + 3 = 0\\)", ["Remainder is 3", "Remainder is -3", "Remainder is 1"]),
                ("Verify Remainder Theorem for \\((5x^2 - 2x + 1) \\div (x - 1)\\):", "Both methods confirm remainder is \\(p(1) = 5 - 2 + 1 = 4\\)", ["Remainder is 3", "Remainder is 5", "Remainder is 1"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate and verify: {0}",
                "Confirm the Remainder Theorem: {0}",
                "Determine remainder and verify: {0}",
                "Check the theorem result: {0}",
                "State the verified remainder: {0}",
                "What is the verified remainder? {0}",
                "Compute and verify: {0}",
                "Select the verified outcome: {0}",
                "Which option confirms: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Compute via Remainder Theorem**\nEvaluate \\(p(a)\\).\n**Step 2: Confirm via Division**\nQuotient and remainder verification matches.\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 4: Formal statement of Remainder Theorem
        {
            'data': [
                ("State the Remainder Theorem:", "If a polynomial \\(p(x)\\) of degree \\(\\ge 1\\) is divided by \\(x - a\\), then the remainder is \\(p(a)\\)", ["The remainder is always 0", "The remainder is equal to the quotient", "The remainder is \\(p(-a)\\)"]),
                ("In the division \\(p(x) = (x - a)q(x) + r\\), why must r be a constant?", "Because \\(\\deg(r) < \\deg(x - a) = 1\\), so \\(\\deg(r) = 0\\) (a constant)", ["Because q(x) is constant", "Because p(x) has no remainder", "Because r is always positive"]),
                ("What happens when \\(x = a\\) is substituted into \\(p(x) = (x - a)q(x) + r\\)?", "\\(p(a) = (a - a)q(a) + r = 0 + r = r\\), proving \\(r = p(a)\\)", ["\\(p(a) = q(a) \\text{ identically}\\)", "\\(p(a) = 0\\)", "\\(p(a) = a^2 + r\\)"]),
                ("When dividing \\(p(x)\\) by \\(x + a\\), what is the remainder according to Remainder Theorem?", "\\(p(-a)\\) (since \\(x + a = 0 \\implies x = -a\\))", ["\\(p(a)\\)", "\\(-p(a)\\)", "\\(a \\cdot p(a)\\)"]),
                ("When dividing \\(p(x)\\) by \\(ax - b\\), what is the remainder?", "\\(p\\left(\\frac{b}{a}\\right)\\)", ["\\(p\\left(-\\frac{b}{a}\\right)\\)", "\\(p\\left(\\frac{a}{b}\\right)\\)", "\\(\\frac{p(b)}{a}\\)"]),
                ("Can the Remainder Theorem be applied directly if the divisor has degree 2 (e.g., \\(x^2 - 1\\))?", "No, the remainder theorem states \\(r = p(a)\\) specifically for linear divisors \\(x - a\\)", ["Yes, without modification", "Yes, giving two remainders", "Only if dividend is cubic"]),
                ("What is the degree of the remainder when any polynomial is divided by a linear factor?", "0 (constant number) or remainder is 0", ["1", "2", "Equal to dividend degree"]),
                ("If \\(p(x)\\) is divided by \\(x - a\\) and leaves remainder 0, what does this imply?", "\\(x - a\\) is a factor of \\(p(x)\\)", ["p(x) is a constant", "a is not a root", "q(x) has degree 0"]),
                ("What is the remainder when \\(p(x)\\) is divided by \\(x\\)?", "\\(p(0)\\) (the constant term of \\(p(x)\\))", ["0 always", "\\(p(1)\\)", "Undefined"]),
                ("If \\(p(2) = 5\\), what is the remainder when \\(p(x)\\) is divided by \\(x - 2\\)?", "5", ["2", "-5", "0"])
            ],
            'tmpls': [
                "{0}",
                "Answer the theorem question: {0}",
                "Evaluate the statement: {0}",
                "Select the correct Remainder Theorem principle: {0}",
                "Determine the true mathematical property: {0}",
                "Choose the right answer: {0}",
                "State the correct concept: {0}",
                "Which option correctly answers: {0}",
                "Analyze the theorem statement: {0}",
                "Identify the correct formula: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand the Remainder Theorem Proof**\nFrom division algorithm: \\(p(x) = (x - a)q(x) + r\\).\nSetting \\(x = a\\) makes the first term 0, yielding \\(p(a) = r\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 5: Finding unknown parameter k given remainder
        {
            'data': [
                ("p(x) = x^3 - 3x^2 + kx - 5", "x - 2", "7", "k = 8 (since \\(8 - 12 + 2k - 5 = 7 \\implies 2k - 9 = 7 \\implies 2k = 16 \\implies k = 8\\))", ["k = -8", "k = 6", "k = 4"]),
                ("p(x) = 2x^2 + kx - 3", "x - 1", "5", "k = 6 (since \\(2 + k - 3 = 5 \\implies k - 1 = 5 \\implies k = 6\\))", ["k = -6", "k = 4", "k = 2"]),
                ("p(x) = x^2 + 4x + k", "x + 2", "3", "k = 7 (since \\(4 - 8 + k = 3 \\implies k - 4 = 3 \\implies k = 7\\))", ["k = -7", "k = 1", "k = 5"]),
                ("p(x) = kx^2 - 7x + 2", "x - 2", "8", "k = 5 (since \\(4k - 14 + 2 = 8 \\implies 4k - 12 = 8 \\implies 4k = 20 \\implies k = 5\\))", ["k = -5", "k = 3", "k = 4"]),
                ("p(x) = x^3 + kx^2 - 2x + 4", "x + 1", "9", "k = 4 (since \\(-1 + k + 2 + 4 = 9 \\implies k + 5 = 9 \\implies k = 4\\))", ["k = -4", "k = 2", "k = 6"]),
                ("p(x) = 3x^2 - kx + 1", "x - 3", "10", "k = 6 (since \\(27 - 3k + 1 = 10 \\implies 28 - 3k = 10 \\implies 3k = 18 \\implies k = 6\\))", ["k = -6", "k = 3", "k = 5"]),
                ("p(x) = x^2 - kx + 8", "x - 4", "0", "k = 6 (since \\(16 - 4k + 8 = 0 \\implies 24 - 4k = 0 \\implies k = 6\\))", ["k = -6", "k = 4", "k = 8"]),
                ("p(x) = 2x^2 + 5x + k", "x + 3", "0", "k = -3 (since \\(18 - 15 + k = 0 \\implies 3 + k = 0 \\implies k = -3\\))", ["k = 3", "k = 0", "k = -5"]),
                ("p(x) = x^3 - kx + 6", "x - 2", "4", "k = 5 (since \\(8 - 2k + 6 = 4 \\implies 14 - 2k = 4 \\implies 2k = 10 \\implies k = 5\\))", ["k = -5", "k = 3", "k = 7"]),
                ("p(x) = 4x^2 + kx - 5", "x - 1", "3", "k = 4 (since \\(4 + k - 5 = 3 \\implies k - 1 = 3 \\implies k = 4\\))", ["k = -4", "k = 2", "k = 5"])
            ],
            'tmpls': [
                "If the remainder when \\({0}\\) is divided by \\({1}\\) is {2}, find k:",
                "Using Remainder Theorem, find k if \\({0} \\div ({1})\\) leaves remainder {2}:",
                "Determine k such that \\({0}\\) divided by \\({1}\\) gives remainder {2}:",
                "Evaluate k given that dividing \\({0}\\) by \\({1}\\) leaves remainder {2}:",
                "Find k when the remainder of \\({0} \\div ({1})\\) is {2}:",
                "Calculate k if \\({0}\\) has remainder {2} when divided by \\({1}\\):",
                "What is k if dividing \\({0}\\) by \\({1}\\) yields remainder {2}?",
                "Compute k from Remainder Theorem: \\({0}\\) divided by \\({1}\\) leaves {2}:",
                "Solve for k when \\({0} \\div ({1})\\) leaves remainder {2}:",
                "Find the parameter k such that \\({0}\\) leaves remainder {2} upon division by \\({1}\\):"
            ],
            'calc': lambda item: (
                item[3],
                item[4],
                "**Step 1: Apply Remainder Theorem**\nSet \\(p(a) = " + str(item[2]) + "\\).\n**Step 2: Solve Linear Equation in k**\n" + str(item[3]) + ".\n**Step 3: Conclusion**\n" + str(item[3]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 6: Same remainder when dividing two different polynomials
        {
            'data': [
                ("The polynomials \\(p(x) = x^3 + 2x^2 - 5ax - 7\\) and \\(q(x) = x^3 + ax^2 - 12x + 6\\) leave the same remainder when divided by \\(x + 1\\). Find a:", "a = 2 (since \\(p(-1) = q(-1) \\implies -6 + 5a = a + 17 \\dots\\))", ["a = -2", "a = 1", "a = 3"]),
                ("If \\(p(x) = 2x^2 + ax - 3\\) and \\(q(x) = x^2 - 2x + a\\) leave the same remainder when divided by \\(x - 2\\), find a:", "a = -5 (since \\(p(2) = 8 + 2a - 3 = 2a + 5\\) and \\(q(2) = 4 - 4 + a = a\\); \\(2a + 5 = a \\implies a = -5\\))", ["a = 5", "a = 2", "a = -2"]),
                ("If \\(p(x) = x^2 + ax + 4\\) and \\(q(x) = 2x^2 - 3x + a\\) have the same remainder when divided by \\(x - 1\\), find a:", "a = 1", ["a = -1", "a = 2", "a = 0"]),
                ("Two polynomials \\(P(x)\\) and \\(Q(x)\\) both leave remainder 3 when divided by \\(x - 4\\). What is the remainder when \\(P(x) - Q(x)\\) is divided by \\(x - 4\\)?", "0 (since \\(3 - 3 = 0\\), \\(x - 4\\) divides the difference exactly)", ["3", "6", "-3"]),
                ("If \\(P(x)\\) and \\(Q(x)\\) leave remainders 4 and 5 respectively when divided by \\(x - 2\\), what is the remainder when \\(P(x) + Q(x)\\) is divided by \\(x - 2\\)?", "9 (since \\(4 + 5 = 9\\))", ["1", "20", "0"]),
                ("If \\(P(x)\\) leaves remainder 3 when divided by \\(x - 1\\), what is the remainder when \\([P(x)]^2\\) is divided by \\(x - 1\\)?", "9 (since \\(3^2 = 9\\))", ["3", "6", "1"]),
                ("If \\(P(x)\\) leaves remainder 2 when divided by \\(x - 3\\), what is the remainder when \\(4P(x) + 5\\) is divided by \\(x - 3\\)?", "13 (since \\(4(2) + 5 = 8 + 5 = 13\\))", ["8", "10", "7"]),
                ("If \\(P(x)\\) is divided by \\(x - a\\) with remainder R, what is the remainder when \\(k \\cdot P(x)\\) is divided by \\(x - a\\)?", "\\(k \\cdot R\\)", ["R", "\\(R + k\\)", "\\(R^k\\)"]),
                ("If \\(P(x)\\) and \\(Q(x)\\) leave remainders 3 and 2 when divided by \\(x - a\\), what is the remainder of \\(P(x) \\cdot Q(x)\\) divided by \\(x - a\\)?", "6 (since \\(3 \\times 2 = 6\\))", ["5", "1", "0"]),
                ("If the remainder when \\(x^2 - 3x + a\\) is divided by \\(x - 2\\) is 5, what is a?", "a = 7 (since \\(4 - 6 + a = 5 \\implies a - 2 = 5 \\implies a = 7\\))", ["a = -7", "a = 3", "a = 5"])
            ],
            'tmpls': [
                "{0}",
                "Solve the remainder problem: {0}",
                "Evaluate the remainder property: {0}",
                "Determine the result: {0}",
                "Calculate: {0}",
                "Find the answer: {0}",
                "State the remainder theorem deduction: {0}",
                "Select the correct answer: {0}",
                "Which option correctly answers: {0}",
                "Compute the value: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Use Remainder Arithmetic**\nRemainder operations mirror function operations: \\(R(P \\pm Q) = R(P) \\pm R(Q)\\), \\(R(P \\cdot Q) = R(P) \\cdot R(Q)\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 7: Conceptual boundaries: Linear vs Non-linear remainders
        {
            'data': [
                ("When dividing by a quadratic divisor \\((x - a)(x - b)\\), what form does the remainder take?", "\\(Ax + B\\) (a linear expression of degree \\(\\le 1\\))", ["A constant only", "A quadratic expression", "Zero always"]),
                ("When dividing by a cubic divisor, what is the maximum degree of the remainder?", "2 (quadratic expression \\(Ax^2 + Bx + C\\))", ["3", "1", "0"]),
                ("Can the Remainder Theorem alone find the quotient polynomial?", "No, it finds only the numerical remainder without performing division", ["Yes, it gives both quotient and remainder", "Yes, for monic polynomials", "Only if degree is 2"]),
                ("If a polynomial is divided by \\(x - 1\\) and \\(p(1) = 0\\), what is the remainder?", "0", ["1", "-1", "Cannot be determined"]),
                ("Why is Remainder Theorem faster than synthetic division for finding remainders?", "It directly calculates \\(p(a)\\) in one arithmetic step without constructing the division tableau", ["It eliminates multiplication", "It does not need the variable", "It works for all functions"]),
                ("If \\(p(x) = (x - 1)(x - 2)q(x) + 3x - 5\\), what is \\(p(1)\\)?", "-2 (since \\(0 + 3(1) - 5 = -2\\))", ["3", "-5", "1"]),
                ("If \\(p(x) = (x - 1)(x - 2)q(x) + 3x - 5\\), what is \\(p(2)\\)?", "1 (since \\(0 + 3(2) - 5 = 6 - 5 = 1\\))", ["6", "-5", "2"]),
                ("If \\(p(x)\\) leaves remainder 5 when divided by \\(x - 3\\), what point lies on the graph of \\(y = p(x)\\)?", "(3, 5)", ["(5, 3)", "(3, 0)", "(0, 5)"]),
                ("If the remainder theorem gives \\(p(a) = 0\\), what geometric feature does the graph of \\(p(x)\\) have at \\(x = a\\)?", "An x-intercept (the curve crosses or touches the x-axis at \\((a, 0)\\))", ["A y-intercept", "A vertical asymptote", "A maximum point"]),
                ("Does the Remainder Theorem hold true if coefficients of \\(p(x)\\) are real numbers?", "Yes, it holds universally for all polynomials over real (and complex) numbers", ["Only for integers", "Only for positive rational numbers", "Only for monic polynomials"])
            ],
            'tmpls': [
                "{0}",
                "Answer the following question: {0}",
                "Evaluate the concept: {0}",
                "Select the correct statement: {0}",
                "Determine the true mathematical property: {0}",
                "Choose the right answer: {0}",
                "Analyze the theorem boundary: {0}",
                "State the correct concept: {0}",
                "Which option correctly answers: {0}",
                "Identify the true reason: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Remainder Form**\nFor any divisor \\(D(x)\\), \\(\\deg(R) < \\deg(D)\\).\nFor linear divisor, \\(R\\) is constant.\nFor quadratic divisor, \\(R\\) is linear \\(Ax + B\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_3_4_3():
    tc = "MH-9-MTH1-3-3.4.3"
    tname = "Factor theorem for checking factorability"
    
    archs = [
        # Arch 0: Checking if (x - a) is a factor
        {
            'data': [
                ("x^2 - 5x + 6", "x - 2", "Is a factor (since \\(p(2) = 4 - 10 + 6 = 0\\))", ["Is not a factor", "Leaves remainder 2", "Leaves remainder -2"]),
                ("x^2 - 5x + 6", "x - 3", "Is a factor (since \\(p(3) = 9 - 15 + 6 = 0\\))", ["Is not a factor", "Leaves remainder 3", "Leaves remainder -3"]),
                ("x^2 - 5x + 6", "x - 4", "Is not a factor (since \\(p(4) = 16 - 20 + 6 = 2 \\ne 0\\))", ["Is a factor", "Leaves remainder 0", "Is an exact divisor"]),
                ("x^3 - 3x^2 + 4x - 4", "x - 2", "Is a factor (since \\(p(2) = 8 - 12 + 8 - 4 = 0\\))", ["Is not a factor", "Leaves remainder 4", "Leaves remainder -4"]),
                ("2x^3 - x^2 - 4x + 3", "x - 1", "Is a factor (since \\(p(1) = 2 - 1 - 4 + 3 = 0\\))", ["Is not a factor", "Leaves remainder 1", "Leaves remainder -1"]),
                ("x^3 + 2x^2 - 5x - 6", "x - 2", "Is a factor (since \\(p(2) = 8 + 8 - 10 - 6 = 0\\))", ["Is not a factor", "Leaves remainder 2", "Leaves remainder -2"]),
                ("3x^2 - 7x + 2", "x - 2", "Is a factor (since \\(p(2) = 12 - 14 + 2 = 0\\))", ["Is not a factor", "Leaves remainder 2", "Leaves remainder -2"]),
                ("x^4 - 16", "x - 2", "Is a factor (since \\(p(2) = 16 - 16 = 0\\))", ["Is not a factor", "Leaves remainder 16", "Leaves remainder -16"]),
                ("x^3 - 6x^2 + 11x - 6", "x - 1", "Is a factor (since \\(p(1) = 1 - 6 + 11 - 6 = 0\\))", ["Is not a factor", "Leaves remainder 1", "Leaves remainder -1"]),
                ("2x^2 + 3x - 5", "x - 1", "Is a factor (since \\(p(1) = 2 + 3 - 5 = 0\\))", ["Is not a factor", "Leaves remainder 5", "Leaves remainder -5"])
            ],
            'tmpls': [
                "Use the Factor Theorem to determine if \\({1}\\) is a factor of \\({0}\\):",
                "Is \\({1}\\) a factor of \\({0}\\)? Justify using Factor Theorem:",
                "Check whether \\({1}\\) is a factor of the polynomial \\({0}\\):",
                "Apply the Factor Theorem to check if \\({1}\\) divides \\({0}\\) completely:",
                "Determine if \\({1}\\) is an exact factor of \\({0}\\):",
                "Verify whether \\({1}\\) is a factor of \\({0}\\):",
                "State whether \\({1}\\) is a factor of \\({0}\\):",
                "Evaluate factorability of \\({0}\\) by \\({1}\\):",
                "Which conclusion is correct regarding \\({1}\\) dividing \\({0}\\)?",
                "Use Factor Theorem on \\({0}\\) with divisor \\({1}\\):"
            ],
            'calc': lambda item: (
                item[2],
                item[3],
                "**Step 1: Find Divisor Root**\nSet divisor = 0 to get x = a.\n**Step 2: Evaluate \\(p(a)\\)**\nIf \\(p(a) = 0\\), then it is a factor; otherwise it is not.\n**Step 3: Conclusion**\n" + str(item[2]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Checking if (x + a) is a factor
        {
            'data': [
                ("x^2 + 5x + 6", "x + 2", "Is a factor (since \\(p(-2) = 4 - 10 + 6 = 0\\))", ["Is not a factor", "Leaves remainder 2", "Leaves remainder -2"]),
                ("x^2 + 5x + 6", "x + 3", "Is a factor (since \\(p(-3) = 9 - 15 + 6 = 0\\))", ["Is not a factor", "Leaves remainder 3", "Leaves remainder -3"]),
                ("x^3 + 1", "x + 1", "Is a factor (since \\(p(-1) = -1 + 1 = 0\\))", ["Is not a factor", "Leaves remainder 1", "Leaves remainder -1"]),
                ("x^3 + 27", "x + 3", "Is a factor (since \\(p(-3) = -27 + 27 = 0\\))", ["Is not a factor", "Leaves remainder 27", "Leaves remainder -27"]),
                ("x^2 + 7x + 12", "x + 4", "Is a factor (since \\(p(-4) = 16 - 28 + 12 = 0\\))", ["Is not a factor", "Leaves remainder 4", "Leaves remainder -4"]),
                ("2x^2 + 7x + 3", "x + 3", "Is a factor (since \\(p(-3) = 18 - 21 + 3 = 0\\))", ["Is not a factor", "Leaves remainder 3", "Leaves remainder -3"]),
                ("x^3 + 2x^2 - x - 2", "x + 1", "Is a factor (since \\(p(-1) = -1 + 2 + 1 - 2 = 0\\))", ["Is not a factor", "Leaves remainder 1", "Leaves remainder -1"]),
                ("x^4 - 1", "x + 1", "Is a factor (since \\(p(-1) = 1 - 1 = 0\\))", ["Is not a factor", "Leaves remainder 2", "Leaves remainder -2"]),
                ("3x^2 + 10x + 3", "x + 3", "Is a factor (since \\(p(-3) = 27 - 30 + 3 = 0\\))", ["Is not a factor", "Leaves remainder 3", "Leaves remainder -3"]),
                ("x^3 + 6x^2 + 11x + 6", "x + 2", "Is a factor (since \\(p(-2) = -8 + 24 - 22 + 6 = 0\\))", ["Is not a factor", "Leaves remainder 2", "Leaves remainder -2"])
            ],
            'tmpls': [
                "Determine if \\({1}\\) is a factor of \\({0}\\) by Factor Theorem:",
                "Is \\({1}\\) a factor of \\({0}\\)?",
                "Check whether \\({1}\\) is an exact factor of \\({0}\\):",
                "Apply Factor Theorem to evaluate if \\({1}\\) divides \\({0}\\):",
                "Verify if \\({1}\\) is a factor of \\({0}\\):",
                "Use Factor Theorem to check if \\({1}\\) divides \\({0}\\):",
                "State whether \\({1}\\) is a factor of the polynomial \\({0}\\):",
                "Test if \\({1}\\) is a factor of \\({0}\\):",
                "Does \\({1}\\) divide \\({0}\\) without remainder?",
                "Evaluate factorability: is \\({1}\\) a factor of \\({0}\\)?"
            ],
            'calc': lambda item: (
                item[2],
                item[3],
                "**Step 1: Set \\(x + a = 0 \\implies x = -a\\)**\n**Step 2: Evaluate \\(p(-a)\\)**\nCheck if \\(p(-a) = 0\\).\n**Step 3: Conclusion**\n" + str(item[2]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 2: Determining unknown k such that (x - a) is a factor
        {
            'data': [
                ("x^2 - kx + 12", "x - 3", "k = 7 (since \\(p(3) = 9 - 3k + 12 = 21 - 3k = 0 \\implies 3k = 21 \\implies k = 7\\))", ["k = -7", "k = 4", "k = 3"]),
                ("2x^2 + kx - 6", "x - 2", "k = -1 (since \\(p(2) = 8 + 2k - 6 = 2k + 2 = 0 \\implies 2k = -2 \\implies k = -1\\))", ["k = 1", "k = -2", "k = 2"]),
                ("x^3 - 3x^2 + kx - 4", "x - 2", "k = 4 (since \\(p(2) = 8 - 12 + 2k - 4 = 2k - 8 = 0 \\implies 2k = 8 \\implies k = 4\\))", ["k = -4", "k = 2", "k = 6"]),
                ("x^2 + 5x + k", "x + 2", "k = 6 (since \\(p(-2) = 4 - 10 + k = k - 6 = 0 \\implies k = 6\\))", ["k = -6", "k = 5", "k = 4"]),
                ("kx^2 - 3x - 2", "x - 2", "k = 2 (since \\(p(2) = 4k - 6 - 2 = 4k - 8 = 0 \\implies 4k = 8 \\implies k = 2\\))", ["k = -2", "k = 1", "k = 4"]),
                ("x^3 + kx^2 - 4x + 4", "x + 2", "k = 3 (since \\(p(-2) = -8 + 4k + 8 + 4 = 4k + 4 = 0 \\implies 4k = -4 \\implies k = -1\\))", ["k = 1", "k = -3", "k = 2"]),
                ("3x^2 + kx - 10", "x - 2", "k = -1 (since \\(p(2) = 12 + 2k - 10 = 2k + 2 = 0 \\implies 2k = -2 \\implies k = -1\\))", ["k = 1", "k = 2", "k = -2"]),
                ("x^4 - 2x^3 + kx - 8", "x - 2", "k = 4 (since \\(p(2) = 16 - 16 + 2k - 8 = 2k - 8 = 0 \\implies 2k = 8 \\implies k = 4\\))", ["k = -4", "k = 2", "k = 8"]),
                ("2x^2 - 5x + k", "x - 1", "k = 3 (since \\(p(1) = 2 - 5 + k = k - 3 = 0 \\implies k = 3\\))", ["k = -3", "k = 1", "k = 5"]),
                ("x^3 - kx^2 + 2x - 4", "x - 2", "k = 2 (since \\(p(2) = 8 - 4k + 4 - 4 = 8 - 4k = 0 \\implies 4k = 8 \\implies k = 2\\))", ["k = -2", "k = 4", "k = 1"])
            ],
            'tmpls': [
                "Find the value of k if \\({1}\\) is a factor of \\({0}\\):",
                "If \\({1}\\) is an exact factor of \\({0}\\), determine k:",
                "Using Factor Theorem, find k such that \\({1}\\) divides \\({0}\\):",
                "Evaluate k given that \\({1}\\) is a factor of \\({0}\\):",
                "Calculate the parameter k for which \\({1}\\) is a factor of \\({0}\\):",
                "What is the value of k if \\({1}\\) is a factor of \\({0}\\)?",
                "Determine k so that \\({0}\\) is completely divisible by \\({1}\\):",
                "Apply Factor Theorem to find k when \\({1}\\) factors \\({0}\\):",
                "Compute k if \\({1}\\) is a factor of \\({0}\\):",
                "Solve for k given that \\({1}\\) divides \\({0}\\) with zero remainder:"
            ],
            'calc': lambda item: (
                item[2],
                item[3],
                "**Step 1: Apply Factor Theorem**\nSet \\(p(a) = 0\\).\n**Step 2: Solve Linear Equation in k**\n" + str(item[2]) + ".\n**Step 3: Conclusion**\n" + str(item[2]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 3: Factor theorem with quadratic expressions
        {
            'data': [
                ("x^2 - 7x + 12", "Both \\(x - 3\\) and \\(x - 4\\)", ["Only \\(x - 3\\)", "Only \\(x - 4\\)", "Neither is a factor"]),
                ("x^2 - 9x + 20", "Both \\(x - 4\\) and \\(x - 5\\)", ["Only \\(x - 4\\)", "Only \\(x - 5\\)", "Neither is a factor"]),
                ("x^2 + 8x + 15", "Both \\(x + 3\\) and \\(x + 5\\)", ["Only \\(x + 3\\)", "Only \\(x + 5\\)", "Neither is a factor"]),
                ("x^2 - x - 6", "Both \\(x - 3\\) and \\(x + 2\\)", ["Only \\(x - 3\\)", "Only \\(x + 2\\)", "Neither is a factor"]),
                ("x^2 + 2x - 8", "Both \\(x + 4\\) and \\(x - 2\\)", ["Only \\(x + 4\\)", "Only \\(x - 2\\)", "Neither is a factor"]),
                ("2x^2 + 5x + 3", "Both \\(x + 1\\) and \\(2x + 3\\)", ["Only \\(x + 1\\)", "Only \\(2x + 3\\)", "Neither is a factor"]),
                ("2x^2 - 7x + 6", "Both \\(x - 2\\) and \\(2x - 3\\)", ["Only \\(x - 2\\)", "Only \\(2x - 3\\)", "Neither is a factor"]),
                ("3x^2 - 5x - 2", "Both \\(x - 2\\) and \\(3x + 1\\)", ["Only \\(x - 2\\)", "Only \\(3x + 1\\)", "Neither is a factor"]),
                ("x^2 - 16", "Both \\(x - 4\\) and \\(x + 4\\)", ["Only \\(x - 4\\)", "Only \\(x + 4\\)", "Neither is a factor"]),
                ("x^2 - 6x + 9", "\\(x - 3\\) repeated factor \\((x - 3)^2\\)", ["\\(x + 3\\)", "\\(x - 9\\)", "No real factors"])
            ],
            'tmpls': [
                "Find the linear factors of \\({0}\\) using the Factor Theorem:",
                "Which pair of binomials are factors of \\({0}\\)?",
                "Factorize \\({0}\\) by applying the Factor Theorem:",
                "Identify all linear factors of \\({0}\\):",
                "Using Factor Theorem, select the complete set of factors of \\({0}\\):",
                "Determine the factors of \\({0}\\):",
                "Which binomial factors divide \\({0}\\) completely?",
                "Find the factors of the quadratic polynomial \\({0}\\):",
                "Evaluate the linear factors of \\({0}\\):",
                "State the factors of \\({0}\\) verified by Factor Theorem:"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Check Factorability via Roots**\nEvaluate \\(p(a)\\) for candidate integers.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 4: Factor theorem statement and logical equivalence
        {
            'data': [
                ("What does the Factor Theorem state?", "If \\(p(a) = 0\\), then \\(x - a\\) is a factor of \\(p(x)\\), and conversely if \\(x - a\\) is a factor, then \\(p(a) = 0\\)", ["\\(p(a)\\) is always non-zero", "Every polynomial has degree 1", "\\(x + a\\) is always a factor"]),
                ("The Factor Theorem is a special case of which broader theorem?", "The Remainder Theorem (where the remainder \\(R = p(a) = 0\\))", ["Pythagoras Theorem", "Binomial Theorem", "Trichotomy Law"]),
                ("If \\(x + a\\) is a factor of \\(p(x)\\), what must be true?", "\\(p(-a) = 0\\)", ["\\(p(a) = 0\\)", "\\(p(0) = -a\\)", "\\(p(-a) = 1\\)"]),
                ("If \\(ax - b\\) is a factor of \\(p(x)\\), what must be true?", "\\(p(b/a) = 0\\)", ["\\(p(-b/a) = 0\\)", "\\(p(b - a) = 0\\)", "\\(p(ab) = 0\\)"]),
                ("If \\(x - 1\\) is a factor of \\(p(x)\\), what is the sum of all coefficients of \\(p(x)\\)?", "0 (since \\(p(1) = \\text{sum of coefficients} = 0\\))", ["1", "-1", "Cannot be determined"]),
                ("If the sum of coefficients of even powers equals the sum of coefficients of odd powers, what is a factor of \\(p(x)\\)?", "\\(x + 1\\) (since \\(p(-1) = 0\\))", ["\\(x - 1\\)", "\\(x\\)", "\\(x - 2\\)"]),
                ("Can a cubic polynomial have more than 3 distinct linear factors?", "No, a polynomial of degree n can have at most n distinct linear factors", ["Yes, up to 4 factors", "Yes, infinitely many", "Only if it has integer roots"]),
                ("If \\(p(x) = (x - 2)(x + 3)q(x)\\), what are two zeros of \\(p(x)\\)?", "\\(x = 2\\) and \\(x = -3\\)", ["\\(x = -2\\) and \\(x = 3\\)", "\\(x = 0\\) and \\(x = 1\\)", "\\(x = 2\\) and \\(x = 3\\)"]),
                ("If \\(p(3) = 0\\), which of the following is guaranteed to divide \\(p(x)\\) exactly?", "\\(x - 3\\)", ["\\(x + 3\\)", "\\(3x\\)", "\\(x^2 - 3\\)"]),
                ("If \\(p(-5) = 0\\), which binomial is a factor of \\(p(x)\\)?", "\\(x + 5\\)", ["\\(x - 5\\)", "\\(5x\\)", "\\(x^2 + 5\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the Factor Theorem statement: {0}",
                "Answer the following concept question: {0}",
                "Select the correct statement: {0}",
                "Determine the true mathematical property: {0}",
                "Choose the right answer: {0}",
                "State the correct theorem property: {0}",
                "Which option correctly answers: {0}",
                "Analyze the factor property: {0}",
                "Identify the correct mathematical conclusion: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand the Factor Theorem**\n\\(x - a\\) is a factor of \\(p(x) \\iff p(a) = 0\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 5: Simultaneous equations in a and b using Factor Theorem
        {
            'data': [
                ("p(x) = x^3 + ax^2 + bx + 6 has factors (x - 1) and (x - 2). Find a and b:", "a = -6, b = 11", ["a = 6, b = -11", "a = -5, b = 6", "a = 1, b = -6"]),
                ("If (x - 2) and (x + 1) are factors of \\(x^3 + ax^2 + bx - 2\\), find a and b:", "a = 0, b = -3", ["a = 1, b = -2", "a = -1, b = 2", "a = 2, b = 3"]),
                ("If \\(x^2 - 1\\) is a factor of \\(ax^3 + x^2 - 2x + b\\), find a and b:", "a = 2, b = -1", ["a = -2, b = 1", "a = 1, b = 2", "a = 2, b = 1"]),
                ("If \\(x^2 - 4\\) is a factor of \\(x^3 + ax^2 + bx - 12\\), find a and b:", "a = 3, b = -4", ["a = -3, b = 4", "a = 4, b = -3", "a = 2, b = -6"]),
                ("If (x - 1) and (x - 3) are factors of \\(x^3 - 6x^2 + ax + b\\), and third factor is (x - 2), find a and b:", "a = 11, b = -6", ["a = -11, b = 6", "a = 6, b = -11", "a = 5, b = -6"]),
                ("If (x + 2) and (x - 1) are factors of \\(x^3 + 2x^2 + ax + b\\), find a and b:", "a = -1, b = -2", ["a = 1, b = 2", "a = -2, b = -1", "a = 2, b = -1"]),
                ("If (x - 2) is a factor of \\(x^2 + ax + b\\) and \\(a + b = 1\\), find a and b:", "a = -5, b = 6", ["a = 5, b = -6", "a = -3, b = 4", "a = 2, b = -1"]),
                ("If \\(x + 3\\) is a factor of \\(x^2 + ax + 12\\), find a:", "a = 7", ["a = -7", "a = 4", "a = 3"]),
                ("If (x - 1) divides both \\(x^2 + ax + 2\\) and \\(x^2 + bx - 3\\), find a + b:", "a = -3, b = 2 \\implies a + b = -1", ["a + b = 1", "a + b = 5", "a + b = -5"]),
                ("If (x - 2) divides \\(x^3 - 4x^2 + ax + b\\) and \\(b = 4\\), find a:", "a = 2", ["a = -2", "a = 4", "a = 1"])
            ],
            'tmpls': [
                "{0}",
                "Using Factor Theorem, solve: {0}",
                "Find the unknown parameters: {0}",
                "Evaluate the coefficients: {0}",
                "Determine the values of a and b: {0}",
                "Calculate a and b: {0}",
                "Solve the factor system: {0}",
                "What are the values of a and b? {0}",
                "Compute a and b using Factor Theorem: {0}",
                "State the solution for a and b: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set Up Simultaneous Linear Equations**\nUse \\(p(root) = 0\\) for each given factor.\n**Step 2: Solve the Linear System**\nSubstitute or eliminate variables.\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 6: Applications to Divisibility of algebraic expressions
        {
            'data': [
                ("Prove that \\(x - y\\) is always a factor of \\(x^n - y^n\\) for all positive integers n:", "Yes, substituting \\(x = y\\) yields \\(y^n - y^n = 0\\), confirming \\(x - y\\) is a factor for all n", ["Only for even n", "Only for odd n", "Never a factor"]),
                ("When is \\(x + y\\) a factor of \\(x^n + y^n\\)?", "When n is an odd positive integer (since \\((-y)^n + y^n = -y^n + y^n = 0\\))", ["When n is even", "For all positive integers n", "Never"]),
                ("When is \\(x + y\\) a factor of \\(x^n - y^n\\)?", "When n is an even positive integer (since \\((-y)^n - y^n = y^n - y^n = 0\\))", ["When n is odd", "Only when n = 1", "Never"]),
                ("Is \\(x - 2\\) a factor of \\(x^5 - 32\\)?", "Yes, since \\(2^5 - 32 = 32 - 32 = 0\\)", ["No, 32 is not divisible by 2", "Leaves remainder 2", "Leaves remainder -2"]),
                ("Is \\(x + 3\\) a factor of \\(x^3 + 27\\)?", "Yes, since \\((-3)^3 + 27 = -27 + 27 = 0\\)", ["No, leaves remainder 54", "No, leaves remainder -27", "Only if x = 3"]),
                ("Is \\(x + 2\\) a factor of \\(x^4 + 16\\)?", "No, since \\((-2)^4 + 16 = 16 + 16 = 32 \\ne 0\\)", ["Yes, it is a factor", "Leaves remainder 0", "Leaves remainder 16"]),
                ("Is \\(x - 1\\) a factor of \\(x^{100} - 1\\)?", "Yes, \\(1^{100} - 1 = 1 - 1 = 0\\)", ["No, power 100 is too large", "Leaves remainder 100", "Only for x = 0"]),
                ("Is \\(x + 1\\) a factor of \\(x^{100} - 1\\)?", "Yes, \\((-1)^{100} - 1 = 1 - 1 = 0\\) since 100 is even", ["No, (-1)^100 = -1", "Leaves remainder -2", "Only when x = 1"]),
                ("Is \\(x + 1\\) a factor of \\(x^{99} + 1\\)?", "Yes, \\((-1)^{99} + 1 = -1 + 1 = 0\\) since 99 is odd", ["No, leaves remainder 2", "No, leaves remainder -1", "Only when x = -99"]),
                ("Is \\(x - a\\) a factor of \\(p(x) - p(a)\\)?", "Yes, always, since substituting \\(x = a\\) yields \\(p(a) - p(a) = 0\\)", ["No, never", "Only if p(a) = 0", "Only if degree is 1"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the divisibility property: {0}",
                "Select the correct algebraic fact: {0}",
                "Determine the true statement: {0}",
                "Answer the generalized factor question: {0}",
                "Choose the right conclusion: {0}",
                "Analyze the algebraic identity: {0}",
                "State the correct rule: {0}",
                "Which option correctly answers: {0}",
                "Identify the true reason: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Apply Factor Theorem with Variable Replacement**\nSubstitute the root into the expression.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Summary & Contrast between Remainder and Factor Theorems
        {
            'data': [
                ("How does the Factor Theorem differ from the Remainder Theorem?", "Factor Theorem specifically focuses on the condition where remainder \\(R = p(a) = 0\\), establishing exact divisibility", ["They are completely unrelated", "Remainder Theorem requires quadratic divisor", "Factor Theorem cannot determine roots"]),
                ("If dividing \\(p(x)\\) by \\(x - a\\) yields remainder \\(R \\ne 0\\), what can be said about factorability?", "\\(x - a\\) is NOT a factor of \\(p(x)\\)", ["\\(x - a\\) is still a factor", "p(x) is not a polynomial", "The degree of p(x) must be zero"]),
                ("Can the Factor Theorem test factors of the form \\(x^2 - a^2\\)?", "Yes, by testing both linear components \\(x - a\\) and \\(x + a\\)", ["No, it only tests linear factors individually", "Only by long division", "Only if a = 0"]),
                ("If a polynomial has integer coefficients and leading coefficient 1, what must any integer zero divide?", "The constant term (Rational Root Theorem)", ["The leading coefficient", "The degree", "The sum of coefficients"]),
                ("For \\(x^3 - 6x^2 + 11x - 6\\), the candidate integer factors of the constant term \\(-6\\) are:", "\\(\\pm 1, \\pm 2, \\pm 3, \\pm 6\\)", ["\\(\\pm 2, \\pm 4\\)", "\\(\\pm 1, \\pm 5\\)", "Only positive numbers"]),
                ("If \\(p(1) = 0\\), \\(p(2) = 0\\), and \\(p(3) = 0\\) for a cubic monic polynomial, write \\(p(x)\\):", "\\((x - 1)(x - 2)(x - 3) = x^3 - 6x^2 + 11x - 6\\)", ["\\(x^3 - 6\\)", "\\((x + 1)(x + 2)(x + 3)\\)", "\\(x^3 - 5x + 6\\)"]),
                ("If \\(p(x)\\) has degree 4 and four distinct zeros 1, -1, 2, -2, what are its linear factors?", "\\((x - 1)(x + 1)(x - 2)(x + 2)\\)", ["\\((x - 1)^4\\)", "\\((x^2 + 1)(x^2 + 4)\\)", "\\((x - 2)^4\\)"]),
                ("If \\(x - a\\) is a factor of \\(p(x)\\), does \\(x = a\\) satisfy the equation \\(p(x) = 0\\)?", "Yes, \\(x = a\\) is a root of the equation \\(p(x) = 0\\)", ["No, it satisfies p(x) = a", "Only if a > 0", "Cannot be determined"]),
                ("What is the remainder when \\(x^3 - 2x^2 + 5\\) is divided by \\(x - 1\\), and is \\(x - 1\\) a factor?", "Remainder is 4, so \\(x - 1\\) is NOT a factor", ["Remainder is 0, so it is a factor", "Remainder is -4, so it is a factor", "Remainder is 5"]),
                ("If \\(p(a) = 0\\) and \\(p'(a) \\ne 0\\), what kind of root is 'a'?", "A simple (multiplicity 1) root", ["A double root", "A complex root", "An inflection point"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the summary concept: {0}",
                "Select the correct answer: {0}",
                "Determine the true mathematical fact: {0}",
                "Answer the following: {0}",
                "Choose the right response: {0}",
                "Analyze the theorem: {0}",
                "State the correct concept: {0}",
                "Which option correctly answers: {0}",
                "Identify the true conclusion: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Factor Theorem Connections**\n\\(x - a\\) is factor \\(\\iff p(a) = 0 \\iff x = a\\) is root.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_3_5_1():
    tc = "MH-9-MTH1-3-3.5.1"
    tname = "Factoring quadratic expressions (x² - x)² - 8(x² - x) + 12"
    
    archs = [
        # Arch 0: 10 distinct substitution u = x^2 - x type
        {
            'data': [
                ("(x^2 - x)^2 - 8(x^2 - x) + 12", "(x - 3)(x + 2)(x - 2)(x + 1)", ["(x - 3)(x - 2)(x + 1)^2", "(x^2 - x - 6)(x^2 - x - 2)", "(x - 6)(x - 2)"], "u = x^2 - x: (u - 6)(u - 2) = (x^2 - x - 6)(x^2 - x - 2)"),
                ("(x^2 - 3x)^2 - 2(x^2 - 3x) - 8", "(x - 4)(x + 1)(x - 2)(x - 1)", ["(x - 4)(x + 1)(x^2 - 3x + 2)", "(x^2 - 3x - 4)(x^2 - 3x + 2)", "(x - 2)(x + 1)"], "u = x^2 - 3x: (u - 4)(u + 2)"),
                ("(x^2 + 5x)^2 - 2(x^2 + 5x) - 24", "(x + 6)(x - 1)(x + 4)(x + 1)", ["(x + 6)(x - 1)(x^2 + 5x + 4)", "(x^2 + 5x - 6)(x^2 + 5x + 4)", "(x - 6)(x + 4)"], "u = x^2 + 5x: (u - 6)(u + 4)"),
                ("(x^2 - 2x)^2 - 11(x^2 - 2x) + 24", "(x - 4)(x + 2)(x - 3)(x + 1)", ["(x - 4)(x + 2)(x^2 - 2x - 3)", "(x^2 - 2x - 8)(x^2 - 2x - 3)", "(x - 3)(x + 2)"], "u = x^2 - 2x: (u - 8)(u - 3)"),
                ("(x^2 + 2x)^2 - 14(x^2 + 2x) - 15", "(x + 5)(x - 3)(x + 1)^2", ["(x + 5)(x - 3)(x^2 + 2x + 1)", "(x^2 + 2x - 15)(x^2 + 2x + 1)", "(x + 5)(x - 3)"], "u = x^2 + 2x: (u - 15)(u + 1)"),
                ("(x^2 - 4x)^2 - 8(x^2 - 4x) - 9", "(x - 5)(x - 3)(x - 1)^2", ["(x - 5)(x - 3)(x^2 - 4x - 9)", "(x^2 - 4x - 9)(x^2 - 4x + 1)", "(x - 9)(x + 1)"], "u = x^2 - 4x: (u - 9)(u + 1)"),
                ("(x^2 + x)^2 - 8(x^2 + x) + 12", "(x + 3)(x - 2)(x + 2)(x - 1)", ["(x + 3)(x - 2)(x^2 + x - 2)", "(x^2 + x - 6)(x^2 + x - 2)", "(x + 6)(x - 2)"], "u = x^2 + x: (u - 6)(u - 2)"),
                ("(x^2 - 5x)^2 + 10(x^2 - 5x) + 24", "(x - 3)(x - 2)(x - 4)(x - 1)", ["(x - 3)(x - 2)(x^2 - 5x + 4)", "(x^2 - 5x + 6)(x^2 - 5x + 4)", "(x - 6)(x - 4)"], "u = x^2 - 5x: (u + 6)(u + 4)"),
                ("(x^2 + 3x)^2 - 8(x^2 + 3x) - 20", "(x + 5)(x - 2)(x^2 + 3x + 2)", ["(x + 5)(x - 2)(x + 2)(x + 1)", "(x^2 + 3x - 10)(x^2 + 3x + 2)", "(x + 10)(x - 2)"], "u = x^2 + 3x: (u - 10)(u + 2)"),
                ("(x^2 - 6x)^2 - 2(x^2 - 6x) - 35", "(x - 7)(x + 1)(x - 5)(x - 1)", ["(x - 7)(x + 1)(x^2 - 6x + 5)", "(x^2 - 6x - 7)(x^2 - 6x + 5)", "(x - 7)(x + 5)"], "u = x^2 - 6x: (u - 7)(u + 5)")
            ],
            'tmpls': [
                "Factorize the quadratic-form polynomial completely: \\({0}\\):",
                "Find the complete linear factorization of \\({0}\\):",
                "Factorize \\({0}\\) by using a substitution \\(u = g(x)\\):",
                "Solve the factorization of \\({0}\\):",
                "Express \\({0}\\) as a product of linear factors:",
                "What is the completely factored form of \\({0}\\)?",
                "Apply substitution method to factorize \\({0}\\):",
                "Determine the factors of \\({0}\\):",
                "Evaluate the complete factorization of \\({0}\\):",
                "Decompose \\({0}\\) into irreducible real linear factors:"
            ],
            'calc': lambda item: (
                f"\\({item[1]}\\)",
                [f"\\({d}\\)" for d in item[2]],
                "**Step 1: Use Variable Substitution**\n" + str(item[3]) + ".\n**Step 2: Conclusion**\nFactored form is \\(" + str(item[1]) + "\\)."
            ),
            'diff': 'hard'
        },
        # Arch 1: 10 distinct grouping pairs
        {
            'data': [
                ("(x + 1)(x + 2)(x + 3)(x + 4) - 120", "(x + 6)(x - 1)(x^2 + 5x + 16)", ["(x^2 + 5x)(x^2 + 5x + 10) - 120", "(x^2 + 5x + 6)(x^2 + 5x + 4)", "(x + 5)(x - 2)"], "Pair (x + 1)(x + 4) and (x + 2)(x + 3)"),
                ("(x - 1)(x - 2)(x - 3)(x - 4) - 24", "x(x - 5)(x^2 - 5x + 10)", ["(x - 5)x(x^2 - 5x + 10)", "(x^2 - 5x)(x^2 - 5x + 10)", "(x - 4)(x - 1)"], "Pair (x - 1)(x - 4) and (x - 2)(x - 3)"),
                ("(x + 2)(x + 3)(x + 8)(x + 7) - 144", "(x + 9)(x + 1)(x^2 + 10x + 28)", ["(x^2 + 10x + 9)(x^2 + 10x + 28)", "(x^2 + 10x + 16)(x^2 + 10x + 21)", "(x + 8)(x + 2)"], "Pair (x + 2)(x + 8) and (x + 3)(x + 7)"),
                ("(x - 3)(x - 4)(x - 7)(x - 8) - 60", "(x - 9)(x - 2)(x^2 - 11x + 34)", ["(x^2 - 11x + 18)(x^2 - 11x + 34)", "(x^2 - 11x + 24)(x^2 - 11x + 28)", "(x - 7)(x - 4)"], "Pair (x - 3)(x - 8) and (x - 4)(x - 7)"),
                ("(x + 1)(x + 2)(x + 3)(x + 6) - 3x^2", "(x^2 + 8x + 6)(x^2 + 4x + 6)", ["(x^2 + 6x + 6)^2 - 4x^2", "(x^2 + 7x + 6)(x^2 + 5x + 6)", "(x + 6)(x + 1)"], "Pair (x + 1)(x + 6) and (x + 2)(x + 3)"),
                ("(x - 2)(x - 1)(x + 3)(x + 4) + 6", "(x^2 + 2x - 8)(x^2 + 2x - 3) + 6", ["(x^2 + 2x - 2)(x^2 + 2x - 9)", "(x + 3)(x - 1)(x^2 + 2x - 9)", "(x - 2)(x + 4)"], "Pair (x - 2)(x + 4) and (x - 1)(x + 3)"),
                ("(x + 1)(x + 3)(x + 5)(x + 7) + 15", "(x^2 + 8x + 10)(x^2 + 8x + 12)", ["(x^2 + 8x + 7)(x^2 + 8x + 15) + 15", "(x + 6)(x + 2)(x^2 + 8x + 10)", "(x + 7)(x + 1)"], "Pair (x + 1)(x + 7) and (x + 3)(x + 5)"),
                ("(x - 4)(x - 5)(x - 1)(x - 2) - 40", "(x^2 - 6x + 4)(x^2 - 6x + 10)", ["(x^2 - 6x + 5)(x^2 - 6x + 8) - 40", "(x - 6)x(x^2 - 6x + 10)", "(x - 5)(x - 1)"], "Pair (x - 1)(x - 5) and (x - 2)(x - 4)"),
                ("(x + 2)(x + 4)(x + 6)(x + 8) + 16", "(x^2 + 10x + 20)^2", ["(x^2 + 10x + 16)(x^2 + 10x + 24) + 16", "(x + 5)^4", "(x + 8)(x + 2)"], "Pair (x + 2)(x + 8) and (x + 4)(x + 6)"),
                ("(x - 1)(x - 3)(x + 2)(x + 4) + 24", "(x^2 + x - 2)(x^2 + x - 12) + 24", ["(x^2 + x - 6)(x^2 + x - 8)", "(x + 3)(x - 2)(x^2 + x - 8)", "(x - 3)(x + 4)"], "Pair (x - 1)(x + 2) and (x - 3)(x + 4)")
            ],
            'tmpls': [
                "Factorize by grouping terms with matching sums of constants: \\({0}\\):",
                "Find the factored form of the product expression: \\({0}\\):",
                "Factorize the four-binomial expression: \\({0}\\):",
                "Apply smart pairing to factorize \\({0}\\):",
                "Evaluate the factors of \\({0}\\):",
                "What is the factorization of \\({0}\\)?",
                "Factorize \\({0}\\) using quadratic substitution:",
                "Decompose \\({0}\\) into factorized form:",
                "Determine the factors of \\({0}\\):",
                "Solve for the factors of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"\\({item[1]}\\)",
                [f"\\({d}\\)" for d in item[2]],
                "**Step 1: Pair Factors with Equal Sum of Constant Terms**\n" + str(item[3]) + ".\n**Step 2: Conclusion**\nFactored form is \\(" + str(item[1]) + "\\)."
            ),
            'diff': 'hard'
        },
        # Arch 2: Biquadratic polynomials ax^4 + bx^2 + c
        {
            'data': [
                ("x^4 - 5x^2 + 4", "(x - 2)(x + 2)(x - 1)(x + 1)", ["(x^2 - 4)(x^2 - 1)", "(x - 2)^2(x + 1)^2", "(x - 4)(x + 1)"], "Let u = x^2: u^2 - 5u + 4 = (u - 4)(u - 1) = (x^2 - 4)(x^2 - 1) = (x - 2)(x + 2)(x - 1)(x + 1)"),
                ("x^4 - 13x^2 + 36", "(x - 3)(x + 3)(x - 2)(x + 2)", ["(x^2 - 9)(x^2 - 4)", "(x - 3)^2(x - 2)^2", "(x - 6)(x + 6)"], "u = x^2: u^2 - 13u + 36 = (u - 9)(u - 4) = (x - 3)(x + 3)(x - 2)(x + 2)"),
                ("x^4 - 29x^2 + 100", "(x - 5)(x + 5)(x - 2)(x + 2)", ["(x^2 - 25)(x^2 - 4)", "(x - 5)^2(x + 2)^2", "(x - 10)(x + 10)"], "u = x^2: u^2 - 29u + 100 = (u - 25)(u - 4) = (x - 5)(x + 5)(x - 2)(x + 2)"),
                ("x^4 - 10x^2 + 9", "(x - 3)(x + 3)(x - 1)(x + 1)", ["(x^2 - 9)(x^2 - 1)", "(x - 3)^2(x + 1)^2", "(x - 9)(x + 1)"], "u = x^2: u^2 - 10u + 9 = (u - 9)(u - 1) = (x - 3)(x + 3)(x - 1)(x + 1)"),
                ("x^4 - 17x^2 + 16", "(x - 4)(x + 4)(x - 1)(x + 1)", ["(x^2 - 16)(x^2 - 1)", "(x - 4)^2(x - 1)^2", "(x - 16)(x + 1)"], "u = x^2: u^2 - 17u + 16 = (u - 16)(u - 1) = (x - 4)(x + 4)(x - 1)(x + 1)"),
                ("x^4 - 25x^2 + 144", "(x - 4)(x + 4)(x - 3)(x + 3)", ["(x^2 - 16)(x^2 - 9)", "(x - 4)^2(x + 3)^2", "(x - 12)(x + 12)"], "u = x^2: u^2 - 25u + 144 = (u - 16)(u - 9) = (x - 4)(x + 4)(x - 3)(x + 3)"),
                ("x^4 - 20x^2 + 64", "(x - 4)(x + 4)(x - 2)(x + 2)", ["(x^2 - 16)(x^2 - 4)", "(x - 4)^2(x - 2)^2", "(x - 8)(x + 8)"], "u = x^2: u^2 - 20u + 64 = (u - 16)(u - 4) = (x - 4)(x + 4)(x - 2)(x + 2)"),
                ("x^4 - 26x^2 + 25", "(x - 5)(x + 5)(x - 1)(x + 1)", ["(x^2 - 25)(x^2 - 1)", "(x - 5)^2(x + 1)^2", "(x - 25)(x + 1)"], "u = x^2: u^2 - 26u + 25 = (u - 25)(u - 1) = (x - 5)(x + 5)(x - 1)(x + 1)"),
                ("4x^4 - 17x^2 + 4", "(2x - 1)(2x + 1)(x - 2)(x + 2)", ["(4x^2 - 1)(x^2 - 4)", "(2x - 1)^2(x - 2)^2", "(4x - 1)(x + 4)"], "u = x^2: 4u^2 - 17u + 4 = (4u - 1)(u - 4) = (4x^2 - 1)(x^2 - 4) = (2x - 1)(2x + 1)(x - 2)(x + 2)"),
                ("9x^4 - 10x^2 + 1", "(3x - 1)(3x + 1)(x - 1)(x + 1)", ["(9x^2 - 1)(x^2 - 1)", "(3x - 1)^2(x - 1)^2", "(9x - 1)(x + 1)"], "u = x^2: 9u^2 - 10u + 1 = (9u - 1)(u - 1) = (3x - 1)(3x + 1)(x - 1)(x + 1)")
            ],
            'tmpls': [
                "Factorize the biquadratic polynomial completely over real numbers: \\({0}\\):",
                "Find the four linear factors of \\({0}\\):",
                "Factorize \\({0}\\) by substituting \\(u = x^2\\):",
                "What is the complete factorization of \\({0}\\)?",
                "Decompose the biquadratic expression \\({0}\\) into linear factors:",
                "Factorize \\({0}\\):",
                "Determine the factors of \\({0}\\):",
                "Express \\({0}\\) as a product of four linear factors:",
                "Solve for the linear factors of \\({0}\\):",
                "Completely factorize \\({0}\\):"
            ],
            'calc': lambda item: (
                f"\\({item[1]}\\)",
                [f"\\({d}\\)" for d in item[2]],
                "**Step 1: Substitute \\(u = x^2\\)**\n" + str(item[3]) + ".\n**Step 2: Apply Difference of Two Squares**\n\\(a^2 - b^2 = (a - b)(a + b)\\).\n**Step 3: Conclusion**\nFactored form is \\(" + str(item[1]) + "\\)."
            ),
            'diff': 'medium'
        },
        # Arch 3: 10 distinct completing the square to factorize a^4 + a^2b^2 + b^4
        {
            'data': [
                ("x^4 + x^2 + 1", "(x^2 + x + 1)(x^2 - x + 1)", ["(x^2 + 1)^2", "(x^2 + x - 1)(x^2 - x - 1)", "(x^2 - 1)^2"], "(x^2 + 1)^2 - x^2 = (x^2 + x + 1)(x^2 - x + 1)"),
                ("x^4 + 4", "(x^2 + 2x + 2)(x^2 - 2x + 2)", ["(x^2 + 2)^2", "(x^2 + 4)(x^2 - 4)", "(x + 2)^4"], "(x^2 + 2)^2 - 4x^2 = (x^2 + 2x + 2)(x^2 - 2x + 2)"),
                ("x^4 + 64", "(x^2 + 4x + 8)(x^2 - 4x + 8)", ["(x^2 + 8)^2", "(x^2 + 8)(x^2 - 8)", "(x + 4)^4"], "(x^2 + 8)^2 - 16x^2 = (x^2 + 4x + 8)(x^2 - 4x + 8)"),
                ("x^4 - 7x^2 + 1", "(x^2 + 3x + 1)(x^2 - 3x + 1)", ["(x^2 - 1)^2", "(x^2 + x - 1)(x^2 - x - 1)", "(x^2 - 7)(x^2 + 1)"], "(x^2 + 1)^2 - 9x^2 = (x^2 + 3x + 1)(x^2 - 3x + 1)"),
                ("x^4 + 4y^4", "(x^2 + 2xy + 2y^2)(x^2 - 2xy + 2y^2)", ["(x^2 + 2y^2)^2", "(x^2 + 4y^2)(x^2 - 4y^2)", "(x + 2y)^4"], "Sophie Germain Identity"),
                ("x^4 + 324", "(x^2 + 6x + 18)(x^2 - 6x + 18)", ["(x^2 + 18)^2", "(x^2 + 18)(x^2 - 18)", "(x + 6)^4"], "(x^2 + 18)^2 - 36x^2"),
                ("x^4 + 2x^2 + 9", "(x^2 + 2x + 3)(x^2 - 2x + 3)", ["(x^2 + 3)^2", "(x^2 + 3)(x^2 - 3)", "(x + 3)^4"], "(x^2 + 3)^2 - 4x^2"),
                ("x^4 - 11x^2 + 1", "(x^2 + 3x - 1)(x^2 - 3x - 1)", ["(x^2 - 1)^2", "(x^2 + x - 1)(x^2 - x - 1)", "(x^2 - 11)(x^2 + 1)"], "(x^2 - 1)^2 - 9x^2"),
                ("a^4 + a^2b^2 + b^4", "(a^2 + ab + b^2)(a^2 - ab + b^2)", ["(a^2 + b^2)^2", "(a^2 + ab - b^2)(a^2 - ab - b^2)", "(a^2 - b^2)^2"], "(a^2 + b^2)^2 - a^2b^2"),
                ("x^4 + 64y^4", "(x^2 + 4xy + 8y^2)(x^2 - 4xy + 8y^2)", ["(x^2 + 8y^2)^2", "(x^2 + 8y^2)(x^2 - 8y^2)", "(x + 4y)^4"], "(x^2 + 8y^2)^2 - 16x^2y^2")
            ],
            'tmpls': [
                "Factorize by completing the square into difference of two squares: \\({0}\\):",
                "Factorize the quartic polynomial \\({0}\\):",
                "Find the irreducible quadratic factors of \\({0}\\):",
                "Decompose \\({0}\\) using \\((A^2 - B^2)\\):",
                "Factorize \\({0}\\) completely over real numbers:",
                "What are the quadratic factors of \\({0}\\)?",
                "Apply Sophie Germain / completing square technique to factorize \\({0}\\):",
                "Determine the factors of \\({0}\\):",
                "Evaluate the factorization of \\({0}\\):",
                "Express \\({0}\\) as a product of two quadratic expressions:"
            ],
            'calc': lambda item: (
                f"\\({item[1]}\\)",
                [f"\\({d}\\)" for d in item[2]],
                "**Step 1: Add and Subtract a Middle Term**\n" + str(item[3]) + ".\n**Step 2: Conclusion**\nFactored form is \\(" + str(item[1]) + "\\)."
            ),
            'diff': 'hard'
        },
        # Arch 4: 10 distinct quadratic forms with two variables
        {
            'data': [
                ("(x^2 - y^2)^2 - 8(x^2 - y^2) + 12", "((x^2 - y^2) - 6)((x^2 - y^2) - 2)", ["(x - y)^4", "(x^2 - y^2 - 12)", "(x^2 - y^2 - 8)"]),
                ("(a^2 + b^2)^2 - 10(a^2 + b^2) + 21", "((a^2 + b^2) - 7)((a^2 + b^2) - 3)", ["(a^2 + b^2 - 10)", "(a + b)^4", "(a^2 + b^2 - 21)"]),
                ("(m^2 - 3)^2 - 5(m^2 - 3) - 14", "(m^2 - 10)(m^2 - 1) = (m^2 - 10)(m - 1)(m + 1)", ["(m^2 - 7)(m^2 + 2)", "(m^2 - 3 - 14)", "(m - 1)^4"]),
                ("(p^2 + 2p)^2 - 2(p^2 + 2p) - 3", "(p^2 + 2p - 3)(p^2 + 2p + 1) = (p + 3)(p - 1)(p + 1)^2", ["(p^2 + 2p - 3)^2", "(p + 1)^4", "(p - 1)^4"]),
                ("(y^2 - 4y)^2 - (y^2 - 4y) - 20", "(y^2 - 4y - 5)(y^2 - 4y + 4) = (y - 5)(y + 1)(y - 2)^2", ["(y - 5)^2(y + 1)^2", "(y - 2)^4", "(y^2 - 4y - 20)"]),
                ("(z^2 + z)^2 - 14(z^2 + z) + 24", "(z^2 + z - 12)(z^2 + z - 2) = (z + 4)(z - 3)(z + 2)(z - 1)", ["(z^2 + z - 12)^2", "(z - 3)^4", "(z + 4)^4"]),
                ("(x^2 + 3x)^2 - 2(x^2 + 3x) - 8", "(x^2 + 3x - 4)(x^2 + 3x + 2) = (x + 4)(x - 1)(x + 2)(x + 1)", ["(x^2 + 3x - 4)^2", "(x - 1)^4", "(x + 4)^4"]),
                ("(u^2 - 5)^2 - 4(u^2 - 5) - 5", "(u^2 - 10)u^2", ["(u^2 - 10)(u^2 - 4)", "(u^2 - 5 - 5)", "(u - 5)^4"]),
                ("(w^2 - 2w)^2 - 7(w^2 - 2w) - 8", "(w^2 - 2w - 8)(w^2 - 2w + 1) = (w - 4)(w + 2)(w - 1)^2", ["(w - 4)^2(w + 2)^2", "(w - 1)^4", "(w^2 - 2w - 8)^2"]),
                ("(k^2 + 4k)^2 - 12(k^2 + 4k) - 45", "(k^2 + 4k - 15)(k^2 + 4k + 3) = (k^2 + 4k - 15)(k + 3)(k + 1)", ["(k^2 + 4k - 15)^2", "(k + 3)^4", "(k + 1)^4"])
            ],
            'tmpls': [
                "Factorize the composite quadratic expression: \\({0}\\):",
                "Find the factored form of \\({0}\\):",
                "Factorize \\({0}\\) by substituting for the repeated expression:",
                "Decompose \\({0}\\) into simpler factors:",
                "What is the factorization of \\({0}\\)?",
                "Evaluate the factors of \\({0}\\):",
                "Apply substitution to factorize \\({0}\\):",
                "Determine the complete factors of \\({0}\\):",
                "Factorize \\({0}\\):",
                "Simplify and factorize \\({0}\\):"
            ],
            'calc': lambda item: (
                f"\\({item[1]}\\)",
                [f"\\({d}\\)" for d in item[2]],
                "**Step 1: Treat Repeated Term as Single Variable u**\nFactorize quadratic in u, then replace u with original expression.\n**Step 2: Conclusion**\nFactored form is \\(" + str(item[1]) + "\\)."
            ),
            'diff': 'medium'
        },
        # Arch 5: Identifying the appropriate substitution
        {
            'data': [
                ("In factoring \\((x^2 - 2x)^2 - 7(x^2 - 2x) + 12\\), what is the most suitable substitution?", "Let \\(u = x^2 - 2x\\)", ["Let \\(u = x^2\\)", "Let \\(u = 2x\\)", "Let \\(u = x - 2\\)"]),
                ("In factoring \\((2x^2 + 5x)^2 - 4(2x^2 + 5x) - 5\\), what substitution simplifies the expression?", "Let \\(y = 2x^2 + 5x\\)", ["Let \\(y = x^2\\)", "Let \\(y = 5x\\)", "Let \\(y = 2x + 5\\)"]),
                ("In factoring \\((x + 1)(x + 2)(x + 3)(x + 4) - 8\\), which terms should be paired first?", "\\((x + 1)(x + 4)\\) and \\((x + 2)(x + 3)\\) (both produce \\(x^2 + 5x\\))", ["\\((x + 1)(x + 2)\\) and \\((x + 3)(x + 4)\\)", "\\((x + 1)(x + 3)\\) and \\((x + 2)(x + 4)\\)", "Any random pairing"]),
                ("In factoring \\((x - 1)(x - 2)(x - 4)(x - 5) + 9\\), which pairing yields a common quadratic part?", "\\((x - 1)(x - 5)\\) and \\((x - 2)(x - 4)\\) (both produce \\(x^2 - 6x\\))", ["\\((x - 1)(x - 2)\\) and \\((x - 4)(x - 5)\\)", "\\((x - 1)(x - 4)\\) and \\((x - 2)(x - 5)\\)", "Pairing first three together"]),
                ("Why is substitution used in expressions like \\((x^2 - x)^2 - 8(x^2 - x) + 12\\)?", "It reduces a degree 4 polynomial into an easily factorizable degree 2 quadratic in u", ["It eliminates the constants", "It turns multiplication into addition", "It avoids having to find roots"]),
                ("In \\(u^2 - 8u + 12 = 0\\), what are the values of u?", "\\(u = 6\\) and \\(u = 2\\)", ["\\(u = -6\\) and \\(u = -2\\)", "\\(u = 12\\) and \\(u = 1\\)", "\\(u = 4\\) and \\(u = 3\\)"]),
                ("If \\(u = x^2 - x\\) and \\(u = 6\\), what are the solutions for x?", "\\(x = 3\\) and \\(x = -2\\) (since \\(x^2 - x - 6 = 0\\))", ["\\(x = -3\\) and \\(x = 2\\)", "\\(x = 6\\) and \\(x = 1\\)", "\\(x = -6\\) and \\(x = -1\\)"]),
                ("If \\(u = x^2 - x\\) and \\(u = 2\\), what are the solutions for x?", "\\(x = 2\\) and \\(x = -1\\) (since \\(x^2 - x - 2 = 0\\))", ["\\(x = -2\\) and \\(x = 1\\)", "\\(x = 2\\) and \\(x = 1\\)", "\\(x = -2\\) and \\(x = -1\\)"]),
                ("What is the degree of \\((x^2 - x)^2 - 8(x^2 - x) + 12\\)?", "4 (since \\((x^2)^2 = x^4\\))", ["2", "8", "12"]),
                ("How many linear factors can \\((x^2 - x)^2 - 8(x^2 - x) + 12\\) have at most?", "At most 4 linear factors", ["At most 2", "At most 8", "At most 6"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the substitution strategy: {0}",
                "Select the best method: {0}",
                "Determine the true mathematical step: {0}",
                "Answer the following question: {0}",
                "Choose the right answer: {0}",
                "Identify the correct substitution: {0}",
                "State the correct procedure: {0}",
                "Which option correctly answers: {0}",
                "Analyze the factorization technique: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Identify Common Sub-Expression**\nLook for repeated quadratic blocks \\(ax^2 + bx\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 6: Number of real roots of quadratic-form quartics
        {
            'data': [
                ("How many real roots does \\((x^2 - 1)^2 + 4 = 0\\) have?", "0 real roots (sum of non-negative and positive number cannot equal 0)", ["4 real roots", "2 real roots", "1 real root"]),
                ("How many real roots does \\((x^2 - 4)^2 = 0\\) have?", "2 distinct real roots (\\(x = 2\\) and \\(x = -2\\), each with multiplicity 2)", ["4 distinct roots", "0 roots", "1 root"]),
                ("Find all real roots of \\((x^2 - 3x)^2 - 2(x^2 - 3x) - 8 = 0\\):", "\\(x = 4, -1, 2, 1\\) (all 4 roots are real and distinct)", ["x = 2 only", "x = 4 only", "No real roots"]),
                ("Find the roots of \\(x^4 - 5x^2 + 4 = 0\\):", "\\(x = \\pm 1, \\pm 2\\)", ["\\(x = \\pm 4, \\pm 1\\)", "\\(x = 1, 2\\)", "\\(x = 4, 1\\)"]),
                ("Find the roots of \\(x^4 - 13x^2 + 36 = 0\\):", "\\(x = \\pm 2, \\pm 3\\)", ["\\(x = \\pm 6, \\pm 6\\)", "\\(x = 2, 3\\)", "\\(x = \\pm 9, \\pm 4\\)"]),
                ("Find the roots of \\(x^4 - 10x^2 + 9 = 0\\):", "\\(x = \\pm 1, \\pm 3\\)", ["\\(x = \\pm 9, \\pm 1\\)", "\\(x = 1, 3\\)", "\\(x = 9, 1\\)"]),
                ("How many real roots does \\(x^4 + 5x^2 + 6 = 0\\) have?", "0 real roots (since \\(u^2 + 5u + 6 = 0 \\implies u = -2, -3\\), and \\(x^2 = \\text{negative}\\) has no real solutions)", ["4 real roots", "2 real roots", "1 real root"]),
                ("How many real roots does \\(x^4 - x^2 - 6 = 0\\) have?", "2 real roots (\\(u = 3 \\implies x = \\pm \\sqrt{3}\\), while \\(u = -2\\) yields no real roots)", ["4 real roots", "0 real roots", "1 real root"]),
                ("Find the real roots of \\(x^4 - 16 = 0\\):", "\\(x = \\pm 2\\) (2 real roots, while \\(x^2 = -4\\) yields imaginary roots)", ["\\(x = \\pm 4\\)", "4 real roots", "x = 2 only"]),
                ("Find the real roots of \\(x^4 - 81 = 0\\):", "\\(x = \\pm 3\\)", ["\\(x = \\pm 9\\)", "x = 3 only", "No real roots"])
            ],
            'tmpls': [
                "{0}",
                "Determine the roots: {0}",
                "Evaluate the root count: {0}",
                "Solve for all real values: {0}",
                "Calculate: {0}",
                "Find the real solutions: {0}",
                "What are the roots? {0}",
                "Select the correct root set: {0}",
                "Which option correctly answers: {0}",
                "Analyze the solvability: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Solve for Intermediate Variable u**\nFind roots in u.\n**Step 2: Solve \\(x^2 = u\\)**\nDiscard negative values of u when seeking real roots.\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: General factorization principles for higher degree polynomials
        {
            'data': [
                ("What is the primary advantage of the method of substitution in factoring?", "It transforms complex high-degree symmetric or repeated expressions into standard factorable quadratics", ["It eliminates the need for checking signs", "It works for prime numbers only", "It converts polynomials to fractions"]),
                ("Can every polynomial with real coefficients be factored into linear and quadratic factors with real coefficients?", "Yes, by the Fundamental Theorem of Algebra, every real polynomial factors into real linear and irreducible quadratic factors", ["No, only even-degree polynomials can", "No, only cubics can", "Only polynomials of degree 1"]),
                ("If a degree 4 polynomial factors into \\((x - 1)(x - 2)(x^2 + 1)\\), what are its irreducible factors over real numbers?", "\\(x - 1\\), \\(x - 2\\), and the irreducible quadratic \\(x^2 + 1\\)", ["Only x - 1", "Only x - 2", "All 4 are linear over reals"]),
                ("What makes a quadratic \\(ax^2 + bx + c\\) irreducible over real numbers?", "Its discriminant \\(\\Delta = b^2 - 4ac < 0\\)", ["Its discriminant \\(\\Delta > 0\\)", "Its leading coefficient is 1", "It has no constant term"]),
                ("Is \\(x^2 + 4\\) reducible over the set of real numbers?", "No, it is irreducible over \\(\\mathbb{R}\\) because \\(b^2 - 4ac = 0 - 16 = -16 < 0\\)", ["Yes, into \\((x + 2)(x - 2)\\)", "Yes, into \\((x + 2)^2\\)", "Yes, into \\((x + 4)(x + 1)\\)"]),
                ("Is \\(x^2 - 4\\) reducible over the set of real numbers?", "Yes, it factors as \\((x - 2)(x + 2)\\)", ["No, it is irreducible", "Only over integers", "Only over complex numbers"]),
                ("When factoring \\((x^2 - 4x)^2 - 2(x^2 - 4x) - 15\\), what quadratic in u is obtained?", "\\(u^2 - 2u - 15\\)", ["\\(u^2 + 2u - 15\\)", "\\(u^2 - 15\\)", "\\(u^2 - 4u - 15\\)"]),
                ("Factor \\(u^2 - 2u - 15\\):", "\\((u - 5)(u + 3)\\)", ["\\((u + 5)(u - 3)\\)", "\\((u - 15)(u + 1)\\)", "\\((u - 5)^2\\)"]),
                ("If \\(u = x^2 - 4x\\), factorize \\(u - 5\\):", "\\(x^2 - 4x - 5 = (x - 5)(x + 1)\\)", ["\\((x + 5)(x - 1)\\)", "\\((x - 5)^2\\)", "\\((x + 1)^2\\)"]),
                ("If \\(u = x^2 - 4x\\), factorize \\(u + 3\\):", "\\(x^2 - 4x + 3 = (x - 3)(x - 1)\\)", ["\\((x + 3)(x + 1)\\)", "\\((x - 3)^2\\)", "\\((x - 1)^2\\)"])
            ],
            'tmpls': [
                "{0}",
                "Answer the following question: {0}",
                "Evaluate the factorization concept: {0}",
                "Select the correct statement: {0}",
                "Determine the true mathematical fact: {0}",
                "Choose the right answer: {0}",
                "Analyze the algebraic property: {0}",
                "State the correct concept: {0}",
                "Which option correctly answers: {0}",
                "Identify the true reason: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Irreducibility and Factorization**\nA quadratic is irreducible over reals if discriminant is negative.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_3_5_2():
    tc = "MH-9-MTH1-3-3.5.2"
    tname = "Factoring cubic polynomials"
    
    archs = [
        # Arch 0: Cubics with factor (x - 1)
        {
            'data': [
                ("x^3 - 6x^2 + 11x - 6", "(x - 1)(x - 2)(x - 3)", ["(x - 1)(x + 2)(x + 3)", "(x - 1)(x - 6)", "(x + 1)(x - 2)(x - 3)"], "Sum of coefficients = 1 - 6 + 11 - 6 = 0, so (x - 1) is a factor. Division gives x^2 - 5x + 6 = (x - 2)(x - 3)"),
                ("x^3 - 2x^2 - x + 2", "(x - 1)(x + 1)(x - 2)", ["(x - 1)(x - 1)(x + 2)", "(x - 1)(x^2 + 2)", "(x + 1)(x - 2)^2"], "Sum of coefficients = 1 - 2 - 1 + 2 = 0, so (x - 1) is a factor. Division gives x^2 - x - 2 = (x - 2)(x + 1)"),
                ("x^3 - 4x^2 + x + 6", "(x - 2)(x - 3)(x + 1)", ["(x - 1)(x - 2)(x - 3)", "(x - 1)(x^2 - 3x - 6)", "(x + 1)(x + 2)(x + 3)"], "p(-1) = -1 - 4 - 1 + 6 = 0, so (x + 1) is a factor. Division gives x^2 - 5x + 6 = (x - 2)(x - 3)"),
                ("x^3 - 7x + 6", "(x - 1)(x - 2)(x + 3)", ["(x - 1)(x + 2)(x - 3)", "(x - 1)(x^2 - 6)", "(x + 1)(x - 2)(x + 3)"], "Sum of coefficients = 1 - 7 + 6 = 0, so (x - 1) is a factor. Division gives x^2 + x - 6 = (x - 2)(x + 3)"),
                ("x^3 - 3x^2 - x + 3", "(x - 1)(x + 1)(x - 3)", ["(x - 1)^2(x + 3)", "(x - 1)(x^2 + 9)", "(x + 1)^2(x - 3)"], "Sum of coefficients = 1 - 3 - 1 + 3 = 0. Division gives x^2 - 2x - 3 = (x - 3)(x + 1)"),
                ("x^3 - 2x^2 - 5x + 6", "(x - 1)(x + 2)(x - 3)", ["(x - 1)(x - 2)(x + 3)", "(x + 1)(x + 2)(x - 3)", "(x - 1)(x^2 + 6)"], "Sum of coefficients = 1 - 2 - 5 + 6 = 0. Division gives x^2 - x - 6 = (x - 3)(x + 2)"),
                ("x^3 - x^2 - 4x + 4", "(x - 1)(x - 2)(x + 2)", ["(x - 1)(x - 2)^2", "(x + 1)(x - 2)(x + 2)", "(x - 1)(x^2 + 4)"], "Sum of coefficients = 1 - 1 - 4 + 4 = 0. Division gives x^2 - 4 = (x - 2)(x + 2)"),
                ("x^3 - 3x^2 - 4x + 12", "(x - 2)(x + 2)(x - 3)", ["(x - 1)(x - 2)(x - 6)", "(x - 2)^2(x + 3)", "(x + 2)^2(x - 3)"], "p(2) = 8 - 12 - 8 + 12 = 0. Division gives x^2 - x - 6 = (x - 3)(x + 2)"),
                ("x^3 - 9x^2 + 26x - 24", "(x - 2)(x - 3)(x - 4)", ["(x - 1)(x - 4)(x - 6)", "(x - 2)(x + 3)(x - 4)", "(x + 2)(x + 3)(x + 4)"], "p(2) = 8 - 36 + 52 - 24 = 0. Division gives x^2 - 7x + 12 = (x - 3)(x - 4)"),
                ("x^3 - 10x^2 + 31x - 30", "(x - 2)(x - 3)(x - 5)", ["(x - 1)(x - 5)(x - 6)", "(x - 2)(x + 3)(x - 5)", "(x + 2)(x + 3)(x + 5)"], "p(2) = 8 - 40 + 62 - 30 = 0. Division gives x^2 - 8x + 15 = (x - 3)(x - 5)")
            ],
            'tmpls': [
                "Factorize the cubic polynomial completely: \\({0}\\):",
                "Find the three linear factors of \\({0}\\):",
                "Factorize the cubic \\({0}\\) using trial root method followed by division:",
                "Decompose \\({0}\\) into a product of linear factors:",
                "What is the complete factorization of the cubic \\({0}\\)?",
                "Factorize \\({0}\\):",
                "Determine the factors of \\({0}\\):",
                "Solve for the linear factors of the cubic expression \\({0}\\):",
                "Apply the Factor Theorem to factorize \\({0}\\):",
                "Completely factorize \\({0}\\) into linear binomials:"
            ],
            'calc': lambda item: (
                f"\\({item[1]}\\)",
                [f"\\({d}\\)" for d in item[2]],
                "**Step 1: Find First Root by Trial (Factor Theorem)**\n" + str(item[3]) + ".\n**Step 2: Factorize Resulting Quadratic Quotient**\nSplit middle term to get remaining linear factors.\n**Step 3: Conclusion**\nFactored form is \\(" + str(item[1]) + "\\)."
            ),
            'diff': 'medium'
        },
        # Arch 1: Cubics with factor (x + 1)
        {
            'data': [
                ("x^3 + 6x^2 + 11x + 6", "(x + 1)(x + 2)(x + 3)", ["(x + 1)(x - 2)(x - 3)", "(x - 1)(x + 2)(x + 3)", "(x + 1)(x^2 + 6)"], "p(-1) = -1 + 6 - 11 + 6 = 0, so (x + 1) is a factor. Division gives x^2 + 5x + 6 = (x + 2)(x + 3)"),
                ("x^3 + 2x^2 - 11x - 12", "(x + 1)(x + 4)(x - 3)", ["(x - 1)(x - 4)(x + 3)", "(x + 1)(x - 4)(x + 3)", "(x + 1)(x^2 - 12)"], "p(-1) = -1 + 2 + 11 - 12 = 0, division gives x^2 + x - 12 = (x + 4)(x - 3)"),
                ("x^3 + 4x^2 + x - 6", "(x + 2)(x + 3)(x - 1)", ["(x + 1)(x + 2)(x + 3)", "(x - 2)(x - 3)(x + 1)", "(x + 1)(x^2 - 6)"], "p(1) = 1 + 4 + 1 - 6 = 0. Division gives x^2 + 5x + 6 = (x + 2)(x + 3)"),
                ("x^3 + 7x^2 + 14x + 8", "(x + 1)(x + 2)(x + 4)", ["(x + 1)(x - 2)(x - 4)", "(x - 1)(x + 2)(x + 4)", "(x + 1)(x^2 + 8)"], "p(-1) = -1 + 7 - 14 + 8 = 0. Division gives x^2 + 6x + 8 = (x + 2)(x + 4)"),
                ("x^3 + 4x^2 - 11x - 30", "(x - 3)(x + 2)(x + 5)", ["(x + 3)(x - 2)(x - 5)", "(x - 3)(x - 2)(x + 5)", "(x - 3)(x^2 + 10)"], "p(3) = 27 + 36 - 33 - 30 = 0, division gives x^2 + 7x + 10 = (x + 2)(x + 5)"),
                ("x^3 + 5x^2 - x - 5", "(x + 1)(x - 1)(x + 5)", ["(x + 1)^2(x - 5)", "(x - 1)^2(x + 5)", "(x + 1)(x + 5)^2"], "p(1) = 1 + 5 - 1 - 5 = 0 and p(-1) = 0. Division gives x^2 + 4x - 5 = (x + 5)(x - 1)"),
                ("x^3 + 9x^2 + 26x + 24", "(x + 2)(x + 3)(x + 4)", ["(x + 1)(x + 4)(x + 6)", "(x - 2)(x - 3)(x - 4)", "(x + 2)(x - 3)(x + 4)"], "p(-2) = -8 + 36 - 52 + 24 = 0. Division gives x^2 + 7x + 12 = (x + 3)(x + 4)"),
                ("x^3 + 8x^2 + 19x + 12", "(x + 1)(x + 3)(x + 4)", ["(x + 1)(x - 3)(x - 4)", "(x - 1)(x + 3)(x + 4)", "(x + 1)(x^2 + 12)"], "p(-1) = -1 + 8 - 19 + 12 = 0. Division gives x^2 + 7x + 12 = (x + 3)(x + 4)"),
                ("x^3 + 6x^2 - x - 30", "(x - 2)(x + 3)(x + 5)", ["(x + 2)(x - 3)(x - 5)", "(x - 2)(x - 3)(x + 5)", "(x - 2)(x^2 + 15)"], "p(2) = 8 + 24 - 2 - 30 = 0, division gives x^2 + 8x + 15 = (x + 3)(x + 5)"),
                ("x^3 + 10x^2 + 31x + 30", "(x + 2)(x + 3)(x + 5)", ["(x + 1)(x + 5)(x + 6)", "(x - 2)(x - 3)(x - 5)", "(x + 2)(x - 3)(x + 5)"], "p(-2) = -8 + 40 - 62 + 30 = 0. Division gives x^2 + 8x + 15 = (x + 3)(x + 5)")
            ],
            'tmpls': [
                "Factorize the cubic polynomial having plus terms: \\({0}\\):",
                "Find all linear factors of the cubic \\({0}\\):",
                "Completely factorize the algebraic cubic \\({0}\\):",
                "Decompose \\({0}\\) into linear factors using Factor Theorem:",
                "What is the complete factorization of \\({0}\\)?",
                "Evaluate the linear factors of the cubic polynomial \\({0}\\):",
                "Factorize \\({0}\\) systematically:",
                "Determine the complete factors of \\({0}\\):",
                "Solve for the linear factors of \\({0}\\):",
                "Find the complete product of linear factors for \\({0}\\):"
            ],
            'calc': lambda item: (
                f"\\({item[1]}\\)",
                [f"\\({d}\\)" for d in item[2]],
                "**Step 1: Check Potential Roots by Factor Theorem**\n" + str(item[3]) + ".\n**Step 2: Conclusion**\nFactored form is \\(" + str(item[1]) + "\\)."
            ),
            'diff': 'medium'
        },
        # Arch 2: Cubics factorable by direct grouping
        {
            'data': [
                ("x^3 - 3x^2 - x + 3", "x^2(x - 3) - 1(x - 3) = (x - 3)(x^2 - 1) = (x - 3)(x - 1)(x + 1)", ["(x - 3)(x - 1)^2", "(x - 3)(x + 1)^2", "(x + 3)(x - 1)(x + 1)"]),
                ("x^3 + 2x^2 - 4x - 8", "x^2(x + 2) - 4(x + 2) = (x + 2)(x^2 - 4) = (x + 2)^2(x - 2)", ["(x + 2)(x - 2)^2", "(x + 2)(x^2 - 8)", "(x - 2)^3"]),
                ("x^3 - 5x^2 - x + 5", "x^2(x - 5) - 1(x - 5) = (x - 5)(x^2 - 1) = (x - 5)(x - 1)(x + 1)", ["(x - 5)(x - 1)^2", "(x + 5)(x - 1)(x + 1)", "(x - 5)(x^2 + 1)"]),
                ("x^3 + 4x^2 - 9x - 36", "x^2(x + 4) - 9(x + 4) = (x + 4)(x^2 - 9) = (x + 4)(x - 3)(x + 3)", ["(x + 4)(x - 3)^2", "(x - 4)(x - 3)(x + 3)", "(x + 4)(x^2 + 9)"]),
                ("2x^3 - 3x^2 - 8x + 12", "x^2(2x - 3) - 4(2x - 3) = (2x - 3)(x^2 - 4) = (2x - 3)(x - 2)(x + 2)", ["(2x - 3)(x - 2)^2", "(2x + 3)(x - 2)(x + 2)", "(2x - 3)(x^2 + 4)"]),
                ("3x^3 + 2x^2 - 3x - 2", "x^2(3x + 2) - 1(3x + 2) = (3x + 2)(x^2 - 1) = (3x + 2)(x - 1)(x + 1)", ["(3x + 2)(x - 1)^2", "(3x - 2)(x - 1)(x + 1)", "(3x + 2)(x^2 + 1)"]),
                ("x^3 - 2x^2 - 9x + 18", "x^2(x - 2) - 9(x - 2) = (x - 2)(x^2 - 9) = (x - 2)(x - 3)(x + 3)", ["(x - 2)(x - 3)^2", "(x + 2)(x - 3)(x + 3)", "(x - 2)(x^2 + 9)"]),
                ("4x^3 - x^2 - 4x + 1", "x^2(4x - 1) - 1(4x - 1) = (4x - 1)(x^2 - 1) = (4x - 1)(x - 1)(x + 1)", ["(4x - 1)(x - 1)^2", "(4x + 1)(x - 1)(x + 1)", "(4x - 1)(x^2 + 1)"]),
                ("x^3 + 5x^2 - 4x - 20", "x^2(x + 5) - 4(x + 5) = (x + 5)(x^2 - 4) = (x + 5)(x - 2)(x + 2)", ["(x + 5)(x - 2)^2", "(x - 5)(x - 2)(x + 2)", "(x + 5)(x^2 + 4)"]),
                ("x^3 - x^2 - 25x + 25", "x^2(x - 1) - 25(x - 1) = (x - 1)(x^2 - 25) = (x - 1)(x - 5)(x + 5)", ["(x - 1)(x - 5)^2", "(x + 1)(x - 5)(x + 5)", "(x - 1)(x^2 + 25)"])
            ],
            'tmpls': [
                "Factorize by grouping terms in pairs: \\({0}\\):",
                "Find the linear factors of \\({0}\\) by direct grouping:",
                "Factorize the four-term cubic \\({0}\\):",
                "Apply common grouping to factorize \\({0}\\):",
                "Decompose \\({0}\\) into factors:",
                "What is the factorization of \\({0}\\)?",
                "Determine the factors of \\({0}\\) using grouping:",
                "Evaluate the factored form of \\({0}\\):",
                "Completely factorize \\({0}\\):",
                "Solve for the factors of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"\\({item[1]}\\)",
                [f"\\({d}\\)" for d in item[2]],
                "**Step 1: Group First Two and Last Two Terms**\nFactor out \\(x^2\\) from the first pair and constant from second pair.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: 10 distinct rational root cubics with leading coefficient > 1
        {
            'data': [
                ("2x^3 - 3x^2 - 11x + 6", "(2x - 1)(x + 2)(x - 3)", ["(2x + 1)(x - 2)(x - 3)", "(2x - 1)(x - 2)(x + 3)", "(2x - 1)(x^2 - 6)"], "p(1/2) = 0"),
                ("2x^3 + x^2 - 13x + 6", "(2x - 1)(x - 2)(x + 3)", ["(2x + 1)(x + 2)(x - 3)", "(2x - 1)(x + 2)(x - 3)", "(2x - 1)(x^2 + 6)"], "p(2) = 0"),
                ("3x^3 - 4x^2 - 17x + 6", "(3x - 1)(x - 3)(x + 2)", ["(3x + 1)(x + 3)(x - 2)", "(3x - 1)(x + 3)(x - 2)", "(3x - 1)(x^2 - 6)"], "p(3) = 0"),
                ("2x^3 + 5x^2 - 4x - 3", "(2x + 1)(x - 1)(x + 3)", ["(2x - 1)(x + 1)(x - 3)", "(2x + 1)(x + 1)(x - 3)", "(2x + 1)(x^2 - 3)"], "p(1) = 0"),
                ("3x^3 + 10x^2 + x - 6", "(3x - 2)(x + 1)(x + 3)", ["(3x + 2)(x - 1)(x - 3)", "(3x - 2)(x - 1)(x + 3)", "(3x - 2)(x^2 - 6)"], "p(-1) = 0"),
                ("2x^3 - x^2 - 5x - 2", "(2x + 1)(x + 1)(x - 2)", ["(2x - 1)(x - 1)(x + 2)", "(2x + 1)(x - 1)(x + 2)", "(2x + 1)(x^2 - 2)"], "p(-1) = 0"),
                ("3x^3 + 2x^2 - 19x + 6", "(3x - 1)(x + 3)(x - 2)", ["(3x + 1)(x - 3)(x + 2)", "(3x - 1)(x - 3)(x + 2)", "(3x - 1)(x^2 + 6)"], "p(2) = 0"),
                ("2x^3 + 3x^2 - 8x + 3", "(2x - 1)(x - 1)(x + 3)", ["(2x + 1)(x + 1)(x - 3)", "(2x - 1)(x + 1)(x - 3)", "(2x - 1)(x^2 + 3)"], "p(1) = 0"),
                ("4x^3 - 12x^2 - x + 3", "(2x - 1)(2x + 1)(x - 3)", ["(4x - 1)(x + 1)(x - 3)", "(2x - 1)^2(x - 3)", "(4x^2 + 1)(x - 3)"], "p(3) = 0"),
                ("3x^3 - 10x^2 + 9x - 2", "(3x - 1)(x - 1)(x - 2)", ["(3x + 1)(x + 1)(x + 2)", "(3x - 1)(x + 1)(x - 2)", "(3x - 1)(x^2 - 2)"], "p(1) = 0")
            ],
            'tmpls': [
                "Factorize the cubic with leading coefficient > 1: \\({0}\\):",
                "Find the linear factors of \\({0}\\):",
                "Completely factorize the cubic polynomial \\({0}\\):",
                "Apply Rational Root Theorem to factorize \\({0}\\):",
                "Decompose \\({0}\\) into linear factors:",
                "What is the complete factorization of \\({0}\\)?",
                "Factorize \\({0}\\) using trial fractional roots:",
                "Determine the factors of \\({0}\\):",
                "Evaluate the linear factors of \\({0}\\):",
                "Solve for the factors of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"\\({item[1]}\\)",
                [f"\\({d}\\)" for d in item[2]],
                "**Step 1: Test Rational Candidates p/q**\n" + str(item[3]) + ".\n**Step 2: Conclusion**\nFactored form is \\(" + str(item[1]) + "\\)."
            ),
            'diff': 'hard'
        },
        # Arch 4: Sum and Difference of Cubes a^3 + b^3 and a^3 - b^3
        {
            'data': [
                ("x^3 + 8", "(x + 2)(x^2 - 2x + 4)", ["(x + 2)^3", "(x + 2)(x^2 + 2x + 4)", "(x - 2)(x^2 + 2x + 4)"], "\\(a^3 + b^3 = (a + b)(a^2 - ab + b^2)\\) with \\(a = x, b = 2\\)"),
                ("x^3 - 27", "(x - 3)(x^2 + 3x + 9)", ["(x - 3)^3", "(x - 3)(x^2 - 3x + 9)", "(x + 3)(x^2 - 3x + 9)"], "\\(a^3 - b^3 = (a - b)(a^2 + ab + b^2)\\) with \\(a = x, b = 3\\)"),
                ("8x^3 + 1", "(2x + 1)(4x^2 - 2x + 1)", ["(2x + 1)^3", "(2x + 1)(4x^2 + 2x + 1)", "(2x - 1)(4x^2 + 2x + 1)"], "\\(a = 2x, b = 1\\)"),
                ("27x^3 - 8", "(3x - 2)(9x^2 + 6x + 4)", ["(3x - 2)^3", "(3x - 2)(9x^2 - 6x + 4)", "(3x + 2)(9x^2 - 6x + 4)"], "\\(a = 3x, b = 2\\)"),
                ("x^3 + 64", "(x + 4)(x^2 - 4x + 16)", ["(x + 4)^3", "(x + 4)(x^2 + 4x + 16)", "(x - 4)(x^2 + 4x + 16)"], "\\(a = x, b = 4\\)"),
                ("x^3 - 125", "(x - 5)(x^2 + 5x + 25)", ["(x - 5)^3", "(x - 5)(x^2 - 5x + 25)", "(x + 5)(x^2 - 5x + 25)"], "\\(a = x, b = 5\\)"),
                ("64x^3 + 27", "(4x + 3)(16x^2 - 12x + 9)", ["(4x + 3)^3", "(4x + 3)(16x^2 + 12x + 9)", "(4x - 3)(16x^2 + 12x + 9)"], "\\(a = 4x, b = 3\\)"),
                ("125x^3 - 1", "(5x - 1)(25x^2 + 5x + 1)", ["(5x - 1)^3", "(5x - 1)(25x^2 - 5x + 1)", "(5x + 1)(25x^2 - 5x + 1)"], "\\(a = 5x, b = 1\\)"),
                ("x^3 + 1000", "(x + 10)(x^2 - 10x + 100)", ["(x + 10)^3", "(x + 10)(x^2 + 10x + 100)", "(x - 10)(x^2 + 10x + 100)"], "\\(a = x, b = 10\\)"),
                ("8x^3 - 27y^3", "(2x - 3y)(4x^2 + 6xy + 9y^2)", ["(2x - 3y)^3", "(2x - 3y)(4x^2 - 6xy + 9y^2)", "(2x + 3y)(4x^2 - 6xy + 9y^2)"], "\\(a = 2x, b = 3y\\)")
            ],
            'tmpls': [
                "Factorize using sum or difference of cubes identity: \\({0}\\):",
                "Factorize the binomial cubic \\({0}\\):",
                "What is the factored form of \\({0}\\)?",
                "Apply cubic formulas to factorize \\({0}\\):",
                "Decompose \\({0}\\) into linear and quadratic factors:",
                "Find the factors of \\({0}\\):",
                "Evaluate the factorization of \\({0}\\):",
                "Completely factorize \\({0}\\):",
                "Determine the factors of \\({0}\\):",
                "Express \\({0}\\) in factored form:"
            ],
            'calc': lambda item: (
                f"\\({item[1]}\\)",
                [f"\\({d}\\)" for d in item[2]],
                "**Step 1: Apply Identity**\n" + str(item[3]) + ".\n**Step 2: Conclusion**\nFactored form is \\(" + str(item[1]) + "\\)."
            ),
            'diff': 'easy'
        },
        # Arch 5: Cubics with repeated roots (x - a)^2(x - b)
        {
            'data': [
                ("x^3 - 3x^2 + 3x - 1", "(x - 1)^3", ["(x - 1)(x + 1)^2", "(x - 1)(x^2 + 1)", "(x + 1)^3"], "Perfect cube: (x - 1)^3"),
                ("x^3 + 3x^2 + 3x + 1", "(x + 1)^3", ["(x + 1)(x - 1)^2", "(x + 1)(x^2 + 1)", "(x - 1)^3"], "Perfect cube: (x + 1)^3"),
                ("x^3 - 6x^2 + 12x - 8", "(x - 2)^3", ["(x - 2)(x + 2)^2", "(x - 2)(x^2 + 4)", "(x + 2)^3"], "Perfect cube: (x - 2)^3"),
                ("x^3 + 6x^2 + 12x + 8", "(x + 2)^3", ["(x + 2)(x - 2)^2", "(x + 2)(x^2 + 4)", "(x - 2)^3"], "Perfect cube: (x + 2)^3"),
                ("x^3 - 5x^2 + 8x - 4", "(x - 1)(x - 2)^2", ["(x - 1)^2(x - 2)", "(x - 1)(x + 2)^2", "(x - 2)^3"], "p(1) = 0, division gives x^2 - 4x + 4 = (x - 2)^2"),
                ("x^3 - 4x^2 + 5x - 2", "(x - 2)(x - 1)^2", ["(x - 2)^2(x - 1)", "(x + 2)(x - 1)^2", "(x - 1)^3"], "p(2) = 0, division gives x^2 - 2x + 1 = (x - 1)^2"),
                ("x^3 + 5x^2 + 8x + 4", "(x + 1)(x + 2)^2", ["(x + 1)^2(x + 2)", "(x - 1)(x + 2)^2", "(x + 2)^3"], "p(-1) = 0, division gives x^2 + 4x + 4 = (x + 2)^2"),
                ("x^3 - 7x^2 + 15x - 9", "(x - 1)(x - 3)^2", ["(x - 1)^2(x - 3)", "(x + 1)(x - 3)^2", "(x - 3)^3"], "p(1) = 0, division gives x^2 - 6x + 9 = (x - 3)^2"),
                ("x^3 + 7x^2 + 15x + 9", "(x + 1)(x + 3)^2", ["(x + 1)^2(x + 3)", "(x - 1)(x + 3)^2", "(x + 3)^3"], "p(-1) = 0, division gives x^2 + 6x + 9 = (x + 3)^2"),
                ("x^3 - 8x^2 + 21x - 18", "(x - 2)(x - 3)^2", ["(x - 2)^2(x - 3)", "(x + 2)(x - 3)^2", "(x - 3)^3"], "p(2) = 0, division gives x^2 - 6x + 9 = (x - 3)^2")
            ],
            'tmpls': [
                "Factorize the cubic polynomial having repeated roots: \\({0}\\):",
                "Find the factored form of \\({0}\\):",
                "Completely factorize \\({0}\\):",
                "Decompose \\({0}\\) recognizing repeated binomial factors:",
                "What is the factorization of \\({0}\\)?",
                "Evaluate the factors of \\({0}\\):",
                "Factorize \\({0}\\):",
                "Determine the complete factors of \\({0}\\):",
                "Solve for the factors of \\({0}\\):",
                "Express \\({0}\\) in fully factored form:"
            ],
            'calc': lambda item: (
                f"\\({item[1]}\\)",
                [f"\\({d}\\)" for d in item[2]],
                "**Step 1: Check for Perfect Cube or Factor by Division**\n" + str(item[3]) + ".\n**Step 2: Conclusion**\nFactored form is \\(" + str(item[1]) + "\\)."
            ),
            'diff': 'medium'
        },
        # Arch 6: Finding roots of cubic equation P(x) = 0
        {
            'data': [
                ("x^3 - 6x^2 + 11x - 6 = 0", "x = 1, 2, 3", ["x = -1, -2, -3", "x = 1, -2, 3", "x = 2, 3, 6"]),
                ("x^3 - 2x^2 - x + 2 = 0", "x = 1, -1, 2", ["x = 1, 2, 2", "x = -1, -1, 2", "x = 1, -2, -2"]),
                ("x^3 - 7x + 6 = 0", "x = 1, 2, -3", ["x = -1, -2, 3", "x = 1, -2, 3", "x = 2, 3, -1"]),
                ("x^3 + 6x^2 + 11x + 6 = 0", "x = -1, -2, -3", ["x = 1, 2, 3", "x = -1, 2, -3", "x = -2, -3, 6"]),
                ("x^3 - 3x^2 - x + 3 = 0", "x = 1, -1, 3", ["x = -1, -1, 3", "x = 1, 1, -3", "x = 1, 2, 3"]),
                ("x^3 - 4x^2 + x + 6 = 0", "x = -1, 2, 3", ["x = 1, -2, -3", "x = 1, 2, 3", "x = -1, -2, 3"]),
                ("x^3 - 9x^2 + 26x - 24 = 0", "x = 2, 3, 4", ["x = -2, -3, -4", "x = 1, 4, 6", "x = 2, -3, 4"]),
                ("x^3 + 2x^2 - 5x - 6 = 0", "x = -1, 2, -3", ["x = 1, -2, 3", "x = -1, -2, 3", "x = 1, 2, -3"]),
                ("x^3 - x^2 - 4x + 4 = 0", "x = 1, 2, -2", ["x = -1, 2, -2", "x = 1, 2, 2", "x = -1, -2, -2"]),
                ("x^3 - 8 = 0", "x = 2 (only one real root, two complex roots)", ["x = 2, -2", "x = \\pm 2", "x = -2 only"])
            ],
            'tmpls': [
                "Solve the cubic equation for its real roots: \\({0}\\):",
                "Find all real roots of the equation \\({0}\\):",
                "What are the solutions to the cubic equation \\({0}\\)?",
                "Determine the values of x satisfying \\({0}\\):",
                "Calculate the real roots of \\({0}\\):",
                "Solve: \\({0}\\):",
                "Evaluate the roots of \\({0}\\):",
                "Which values of x satisfy \\({0}\\)?",
                "Compute all real solutions of \\({0}\\):",
                "Find the complete solution set of \\({0}\\):"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Factorize Cubic into Linear Factors**\nSet each linear factor equal to zero.\n**Step 2: Conclusion**\nRoots are " + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Geometric interpretation & Vieta's relations for cubics
        {
            'data': [
                ("For cubic \\(x^3 - 6x^2 + 11x - 6 = 0\\), what is the sum of roots \\(\\alpha + \\beta + \\gamma\\)?", "6 (since \\(-\\frac{b}{a} = -\\frac{-6}{1} = 6\\))", ["-6", "11", "-11"]),
                ("For cubic \\(x^3 - 6x^2 + 11x - 6 = 0\\), what is the product of roots \\(\\alpha \\beta \\gamma\\)?", "6 (since \\(-\\frac{d}{a} = -\\frac{-6}{1} = 6\\))", ["-6", "11", "1"]),
                ("For cubic \\(x^3 - 6x^2 + 11x - 6 = 0\\), what is the sum of pairwise products \\(\\alpha\\beta + \\beta\\gamma + \\gamma\\alpha\\)?", "11 (since \\(\\frac{c}{a} = \\frac{11}{1} = 11\\))", ["-11", "6", "-6"]),
                ("For general cubic \\(ax^3 + bx^2 + cx + d = 0\\), what is \\(\\alpha + \\beta + \\gamma\\)?", "\\(-\\frac{b}{a}\\)", ["\\(\\frac{b}{a}\\)", "\\(-\\frac{c}{a}\\)", "\\(-\\frac{d}{a}\\)"]),
                ("For general cubic \\(ax^3 + bx^2 + cx + d = 0\\), what is the product of roots \\(\\alpha \\beta \\gamma\\)?", "\\(-\\frac{d}{a}\\)", ["\\(\\frac{d}{a}\\)", "\\(-\\frac{b}{a}\\)", "\\(\\frac{c}{a}\\)"]),
                ("How many points of inflection does any cubic polynomial curve have?", "Exactly 1 point of inflection", ["2", "3", "0"]),
                ("Must every cubic polynomial with real coefficients have at least one real root?", "Yes, because complex roots always occur in conjugate pairs, leaving at least 1 real root", ["No, it can have 0 real roots", "Only if constant term is negative", "Only if it is monic"]),
                ("What is the maximum number of turning points (local extrema) a cubic polynomial graph can have?", "At most 2 turning points (one local maximum and one local minimum)", ["3 turning points", "1 turning point", "4 turning points"]),
                ("If a cubic equation has roots 1, 2, 3, what is its monic polynomial?", "\\(x^3 - 6x^2 + 11x - 6\\)", ["\\(x^3 + 6x^2 + 11x + 6\\)", "\\(x^3 - 5x + 6\\)", "\\(x^3 - 6\\)"]),
                ("If the graph of a cubic polynomial crosses the x-axis at 3 distinct points, how many real roots does it have?", "3 distinct real roots", ["1 real root", "2 real roots", "0 real roots"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the cubic property: {0}",
                "Select the correct answer: {0}",
                "Determine the true mathematical fact: {0}",
                "Answer the following Vieta / geometric question: {0}",
                "Choose the right conclusion: {0}",
                "Analyze the cubic polynomial relation: {0}",
                "State the correct theorem: {0}",
                "Which option correctly answers: {0}",
                "Identify the true relationship: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Vieta's Relations & Cubic Topology**\nSum of roots \\(= -b/a\\).\nPairwise products \\(= c/a\\).\nProduct of roots \\(= -d/a\\).\nEvery cubic has at least one real root.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

if __name__ == "__main__":
    print("Compiling Chapter 3 Part 2 (3.4.1, 3.4.2, 3.4.3, 3.5.1, 3.5.2)...")
    qs = []
    for gen in [gen_3_4_1, gen_3_4_2, gen_3_4_3, gen_3_5_1, gen_3_5_2]:
        sub_qs = gen()
        print(f"Generated {len(sub_qs)} questions for {sub_qs[0]['topicCode']}")
        qs.extend(sub_qs)
    
    out_path = "scripts/mh9_mth1_ch3_p2_test.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(qs)} questions to {out_path}")
