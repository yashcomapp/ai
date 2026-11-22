import json
from engine_algebra import generate_subtopic

CH_NUM = 3
CH_NAME = "Polynomials"

def gen_3_1_1():
    tc = "MH-9-MTH1-3-3.1.1"
    tname = "Degree in one and more variables"
    
    archs = [
        # Arch 0: Degree in single-variable polynomials
        {
            'data': [
                ("7x^5 - 3x^2 + 4", "5", ["2", "7", "0"]),
                ("9x^3 - 4x^6 + x - 8", "6", ["3", "9", "4"]),
                ("12x^8 - 5x^4 + 3", "8", ["4", "12", "0"]),
                ("4x^2 + 7x - 11", "2", ["1", "4", "3"]),
                ("15x^4 - 2x^7 + 6x", "7", ["4", "15", "1"]),
                ("25x - 13", "1", ["0", "25", "2"]),
                ("8x^9 - 3x^5 + 2x^2", "9", ["8", "5", "1"]),
                ("10x^10 - 1", "10", ["1", "10x", "0"]),
                ("6x^3 + 5x^2 - x", "3", ["2", "6", "1"]),
                ("18x^6 + 4x^3 - 7", "6", ["3", "18", "7"])
            ],
            'tmpls': [
                "Find the degree of the polynomial \\({0}\\):",
                "What is the degree of \\({0}\\)?",
                "Determine the highest power (degree) of \\({0}\\):",
                "Identify the degree of the polynomial expression \\({0}\\):",
                "Evaluate the degree of the single-variable polynomial \\({0}\\):",
                "State the degree of \\({0}\\):",
                "What is the maximum exponent of the variable in \\({0}\\)?",
                "Compute the degree of \\({0}\\):",
                "Find the degree of the given polynomial: \\({0}\\):",
                "The degree of the algebraic polynomial \\({0}\\) is:"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Identify All Powers of x**\nLook at the exponents of the variable in \\({item[0]}\\).\n**Step 2: Find the Maximum Exponent**\nThe highest power is {item[1]}.\n**Step 3: Conclusion**\nTherefore, the degree is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Multi-variable polynomials
        {
            'data': [
                ("3x^2y^3 + 5x^4y - 7", "5", ["6", "4", "3"], "2 + 3 = 5 and 4 + 1 = 5"),
                ("m^3n^7 - 5m^5n^4 + m^2n^2", "10", ["7", "9", "5"], "3 + 7 = 10, while 5 + 4 = 9"),
                ("4a^3b^2c^4 - 2a^5b^3 + c^7", "9", ["8", "7", "12"], "3 + 2 + 4 = 9, while 5 + 3 = 8"),
                ("6p^4q^5r - 2p^3q^3 + 8", "10", ["9", "8", "6"], "4 + 5 + 1 = 10"),
                ("xy + yz + zx", "2", ["1", "3", "0"], "1 + 1 = 2 for each term"),
                ("8u^2v^4 - 3u^5v^2 + uv", "7", ["6", "8", "5"], "5 + 2 = 7 and 2 + 4 = 6"),
                ("x^3y^2z^2 - 4x^4y^2 + z^5", "7", ["6", "5", "8"], "3 + 2 + 2 = 7 and 4 + 2 = 6"),
                ("5a^6b^2 - 2a^3b^4 + 9", "8", ["6", "7", "5"], "6 + 2 = 8, while 3 + 4 = 7"),
                ("2x^4y^3 + 7x^2y^6 - y^7", "8", ["7", "6", "9"], "2 + 6 = 8, while 4 + 3 = 7"),
                ("9m^2n^5p^3 - m^8 + p^9", "10", ["9", "8", "7"], "2 + 5 + 3 = 10, while single variables are 8 and 9")
            ],
            'tmpls': [
                "Find the degree of the multi-variable polynomial \\({0}\\):",
                "What is the degree of \\({0}\\)?",
                "Calculate the degree of the polynomial in more than one variable: \\({0}\\):",
                "Determine the highest sum of powers in \\({0}\\):",
                "The degree of the multi-variable expression \\({0}\\) is:",
                "Evaluate the degree of \\({0}\\):",
                "State the degree of the polynomial \\({0}\\):",
                "Find the maximum total degree among the terms in \\({0}\\):",
                "Compute the degree of the polynomial \\({0}\\):",
                "In the multi-variable polynomial \\({0}\\), the degree is:"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Sum the Exponents for Each Term**\nFor each term, add the powers of all variables involved ({item[3]}).\n**Step 2: Identify the Maximum Sum**\nThe highest sum of powers among all terms is {item[1]}.\n**Step 3: Conclusion**\nTherefore, the degree is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Classification by degree (Linear, Quadratic, Cubic)
        {
            'data': [
                ("5x - 7", "Linear polynomial (degree 1)", ["Quadratic polynomial (degree 2)", "Cubic polynomial (degree 3)", "Constant polynomial (degree 0)"]),
                ("3x^2 + 4x - 5", "Quadratic polynomial (degree 2)", ["Linear polynomial (degree 1)", "Cubic polynomial (degree 3)", "Constant polynomial (degree 0)"]),
                ("2x^3 - 8x + 1", "Cubic polynomial (degree 3)", ["Quadratic polynomial (degree 2)", "Linear polynomial (degree 1)", "Biquadratic polynomial (degree 4)"]),
                ("4y^2 - 9", "Quadratic polynomial (degree 2)", ["Linear polynomial (degree 1)", "Cubic polynomial (degree 3)", "Zero polynomial"]),
                ("7m + 12", "Linear polynomial (degree 1)", ["Quadratic polynomial (degree 2)", "Cubic polynomial (degree 3)", "Constant polynomial"]),
                ("x^3 + 3x^2 - x + 4", "Cubic polynomial (degree 3)", ["Quadratic polynomial (degree 2)", "Linear polynomial (degree 1)", "Constant polynomial"]),
                ("9p^2", "Quadratic monomial (degree 2)", ["Linear monomial (degree 1)", "Cubic monomial (degree 3)", "Constant monomial"]),
                ("8z - 3", "Linear polynomial (degree 1)", ["Quadratic polynomial (degree 2)", "Cubic polynomial (degree 3)", "Zero polynomial"]),
                ("5y^3 - 2y", "Cubic polynomial (degree 3)", ["Quadratic polynomial (degree 2)", "Linear polynomial (degree 1)", "Constant polynomial"]),
                ("11x^2 + 1", "Quadratic polynomial (degree 2)", ["Linear polynomial (degree 1)", "Cubic polynomial (degree 3)", "Biquadratic polynomial"])
            ],
            'tmpls': [
                "Classify the polynomial \\({0}\\) based on its degree:",
                "What type of polynomial is \\({0}\\) according to its degree?",
                "Classify \\({0}\\) as linear, quadratic, or cubic:",
                "Identify the classification of \\({0}\\):",
                "Based on its degree, \\({0}\\) is classified as:",
                "How is \\({0}\\) categorized by degree?",
                "Select the correct degree-based classification of \\({0}\\):",
                "Determine the classification of the polynomial \\({0}\\):",
                "According to its degree, the polynomial \\({0}\\) is a:",
                "Classify the algebraic expression \\({0}\\):"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Determine the Degree**\nIdentify the highest power of the variable in \\({item[0]}\\).\n**Step 2: Apply Degree Classification**\nDegree 1 is Linear, Degree 2 is Quadratic, Degree 3 is Cubic.\n**Step 3: Conclusion**\n\\({item[0]}\\) is a {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 3: Identifying Non-polynomials vs Polynomials
        {
            'data': [
                ("\\sqrt{x} + 5", "Not a polynomial (exponent of x is \\(\\frac{1}{2}\\), which is not a whole number)", ["Polynomial of degree 1", "Polynomial of degree \\(\\frac{1}{2}\\)", "Linear polynomial"]),
                ("x^2 + \\frac{1}{x} - 3", "Not a polynomial (exponent of x in \\(\\frac{1}{x}\\) is \\(-1\\), not a whole number)", ["Polynomial of degree 2", "Polynomial of degree 1", "Quadratic polynomial"]),
                ("3x^3 - 5x + 7", "Is a polynomial (all exponents 3, 1, 0 are non-negative integers)", ["Not a polynomial", "Polynomial of degree 1", "Rational non-polynomial"]),
                ("y^{-2} + 4y + 1", "Not a polynomial (contains negative integer power \\(-2\\))", ["Polynomial of degree 1", "Polynomial of degree \\(-2\\)", "Quadratic polynomial"]),
                ("5\\sqrt{y} + y^2", "Not a polynomial (power \\(\\frac{1}{2}\\) is not an integer)", ["Polynomial of degree 2", "Polynomial of degree 1", "Quadratic polynomial"]),
                ("4m^2 - 3m + \\sqrt{7}", "Is a polynomial (coefficients can be irrational, powers of m are whole numbers)", ["Not a polynomial because of \\(\\sqrt{7}\\)", "Polynomial of degree 1", "Rational non-polynomial"]),
                ("\\frac{2}{x^2} + 5x - 8", "Not a polynomial (contains \\(x^{-2}\\))", ["Polynomial of degree 1", "Polynomial of degree 2", "Cubic polynomial"]),
                ("7x^4 - 2x^2 + 9", "Is a polynomial (all powers are whole numbers: 4, 2, 0)", ["Not a polynomial", "Rational non-polynomial", "Polynomial of degree 2"]),
                ("p + \\frac{3}{p} + 2", "Not a polynomial (contains \\(p^{-1}\\))", ["Polynomial of degree 1", "Polynomial of degree 0", "Linear polynomial"]),
                ("\\sqrt{2}x^3 + \\frac{3}{4}x", "Is a polynomial (variable powers 3 and 1 are non-negative integers)", ["Not a polynomial", "Polynomial of degree 1", "Irrational function"])
            ],
            'tmpls': [
                "State whether \\({0}\\) is a polynomial and give the reason:",
                "Is \\({0}\\) a polynomial? Select the correct justification:",
                "Determine if \\({0}\\) represents a polynomial:",
                "Check whether the algebraic expression \\({0}\\) is a polynomial:",
                "Select the correct status of \\({0}\\):",
                "Evaluate whether \\({0}\\) satisfies the definition of a polynomial:",
                "Is the expression \\({0}\\) a polynomial?",
                "Classify the expression \\({0}\\) as a polynomial or not:",
                "Which statement correctly describes \\({0}\\)?",
                "Determine whether \\({0}\\) is a polynomial in one variable:"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Check Exponents of Variable**\nIn an algebraic expression, all powers of the variable must be non-negative integers.\n**Step 2: Examine \\(" + str(item[0]) + "\\)**\n" + str(item[1]) + ".\n**Step 3: Conclusion**\nCorrect choice is: " + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 4: Constant and Zero Polynomials
        {
            'data': [
                ("5", "0 (since \\(5 = 5x^0\\))", ["1", "5", "Not defined"]),
                ("-12", "0 (any non-zero constant has degree 0)", ["1", "-12", "Not defined"]),
                ("\\sqrt{7}", "0 (it is a non-zero constant real number)", ["\\(\\frac{1}{2}\\)", "1", "Not defined"]),
                ("0", "Not defined (conventionally, the zero polynomial has no defined degree)", ["0", "1", "-1"]),
                ("\\frac{3}{8}", "0 (non-zero constant rational number)", ["1", "3", "Not defined"]),
                ("-100", "0", ["1", "-100", "Not defined"]),
                ("\\pi", "0 (constant real number)", ["1", "3.14", "Not defined"]),
                ("0x^3", "Not defined (this simplifies to the zero polynomial 0)", ["3", "0", "1"]),
                ("25", "0", ["1", "25", "Not defined"]),
                ("0 \\text{ (the zero polynomial)}", "Not defined by convention", ["0", "1", "-Infinity"])
            ],
            'tmpls': [
                "What is the degree of the constant polynomial \\({0}\\)?",
                "Find the degree of \\({0}\\):",
                "Determine the degree of the constant \\({0}\\):",
                "State the degree of \\({0}\\):",
                "What is the degree of \\({0}\\)?",
                "The degree of the constant polynomial \\({0}\\) is:",
                "Compute the degree of the polynomial \\({0}\\):",
                "Identify the degree of \\({0}\\):",
                "Evaluate the degree of the constant expression \\({0}\\):",
                "Select the degree of \\({0}\\):"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Definition of Constant & Zero Polynomial Degree**\nFor any non-zero constant \\(c \\ne 0\\), \\(c = c x^0\\), so the degree is 0.\nFor the zero polynomial 0, the degree is not defined.\n**Step 2: Conclusion**\nThe degree of \\({item[0]}\\) is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 5: Leading coefficient and highest degree term
        {
            'data': [
                ("-5x^4 + 3x^2 - x + 7", "-5", ["4", "3", "7"], "-5x^4"),
                ("8x^3 - 12x^6 + 4x - 1", "-12", ["8", "6", "-1"], "-12x^6"),
                ("x^5 - 7x^2 + 9", "1", ["5", "-7", "9"], "x^5"),
                ("-x^7 + 4x^3 - 2", "-1", ["7", "4", "-2"], "-x^7"),
                ("14 + 3x - 6x^3", "-6", ["3", "14", "6"], "-6x^3"),
                ("9x^2 + 4x - 15", "9", ["2", "4", "-15"], "9x^2"),
                ("7x^8 - 2x^4 + 5", "7", ["8", "-2", "5"], "7x^8"),
                ("-3x^9 + 11x^5 - 8", "-3", ["9", "11", "-8"], "-3x^9"),
                ("20x - 4x^2 + 1", "-4", ["20", "2", "1"], "-4x^2"),
                ("x^4 + 10x^3 - 5", "1", ["4", "10", "-5"], "x^4")
            ],
            'tmpls': [
                "Find the leading coefficient of the polynomial \\({0}\\):",
                "What is the coefficient of the highest-degree term in \\({0}\\)?",
                "Identify the leading coefficient in \\({0}\\):",
                "Determine the leading coefficient of \\({0}\\):",
                "State the leading coefficient of \\({0}\\):",
                "What is the coefficient of the leading term in \\({0}\\)?",
                "In the polynomial \\({0}\\), the leading coefficient is:",
                "Evaluate the leading coefficient of \\({0}\\):",
                "Select the coefficient of the term with maximum degree in \\({0}\\):",
                "Find the leading coefficient of the given expression: \\({0}\\):"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Identify the Highest Degree Term**\nThe term with the maximum exponent is \\({item[3]}\\).\n**Step 2: Read Its Coefficient**\nThe numerical factor multiplying this highest power is {item[1]}.\n**Step 3: Conclusion**\nTherefore, the leading coefficient is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 6: Degree of product of polynomials
        {
            'data': [
                ("(x^3 + 2)(x^4 - 5)", "7", ["12", "4", "3"], "3 + 4 = 7"),
                ("(2x^2 - 1)(3x^5 + 4x)", "7", ["10", "5", "6"], "2 + 5 = 7"),
                ("(x^4 - 3x)(x^6 + 1)", "10", ["24", "6", "4"], "4 + 6 = 10"),
                ("(5x - 2)(4x^3 + 7x^2)", "4", ["3", "5", "1"], "1 + 3 = 4"),
                ("(x^2 + 1)(x^3 - 2)(x + 4)", "6", ["5", "8", "7"], "2 + 3 + 1 = 6"),
                ("(3x^5 - 2x^2)(2x^3 - 7)", "8", ["15", "5", "6"], "5 + 3 = 8"),
                ("(x^7 + 4)(x^2 - 3x + 1)", "9", ["14", "7", "8"], "7 + 2 = 9"),
                ("(4x^3 - 1)^2", "6", ["9", "5", "8"], "3 \\times 2 = 6"),
                ("(x^2 + 5)^3", "6", ["5", "8", "9"], "2 \\times 3 = 6"),
                ("(x^6 - 2)(x^5 + 3x)", "11", ["30", "6", "10"], "6 + 5 = 11")
            ],
            'tmpls': [
                "Find the degree of the product polynomial \\({0}\\):",
                "What is the degree of \\({0}\\)?",
                "Without fully expanding, determine the degree of \\({0}\\):",
                "Calculate the degree of the product \\({0}\\):",
                "The degree of the expression \\({0}\\) is:",
                "Evaluate the degree of the expanded polynomial \\({0}\\):",
                "Determine the highest power of x in the expansion of \\({0}\\):",
                "What is the degree of the resulting polynomial after multiplying \\({0}\\)?",
                "Compute the degree of the polynomial product \\({0}\\):",
                "Find the degree of \\({0}\\) using the product rule of polynomial degrees:"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Apply Degree of Product Rule**\nFor two non-zero polynomials \\(P(x)\\) and \\(Q(x)\\), \\(\\deg(P \\cdot Q) = \\deg(P) + \\deg(Q)\\).\n**Step 2: Add the Degrees**\nSum of degrees: {item[3]}.\n**Step 3: Conclusion**\nTherefore, the degree is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Degree of sum/difference and general properties
        {
            'data': [
                ("If \\(\\deg(P) = 4\\) and \\(\\deg(Q) = 4\\), with opposite leading coefficients, what can be said about \\(\\deg(P + Q)\\)?", "It is less than or equal to 4 (\\(\\le 4\\), terms may cancel)", ["It is strictly equal to 8", "It must be 4", "It must be 0"]),
                ("If \\(\\deg(P) = 5\\) and \\(\\deg(Q) = 2\\), what is \\(\\deg(P + Q)\\)?", "5 (the higher degree dominates)", ["7", "3", "10"]),
                ("If \\(\\deg(P) = 6\\) and \\(\\deg(Q) = 3\\), what is \\(\\deg(P - Q)\\)?", "6", ["3", "9", "2"]),
                ("If \\(\\deg(P) = m\\) and \\(\\deg(Q) = n\\) with \\(m > n\\), what is \\(\\deg(P \\pm Q)\\)?", "m (the maximum of m and n)", ["m + n", "m - n", "mn"]),
                ("If a polynomial has degree n, at most how many terms can it have in one variable?", "n + 1 terms", ["n terms", "n - 1 terms", "2n terms"]),
                ("A non-zero polynomial of degree 0 is called a:", "Constant polynomial", ["Linear polynomial", "Zero polynomial", "Quadratic polynomial"]),
                ("What is the degree of \\((x + 1)^4 - (x^4 + 1)\\)?", "3 (since the \\(x^4\\) terms cancel out leaving \\(4x^3 + \\dots\\))", ["4", "1", "0"]),
                ("If \\(\\deg(P) = 3\\), what is \\(\\deg(P^4)\\)?", "12 (since \\(3 \\times 4 = 12\\))", ["7", "81", "34"]),
                ("Can the degree of a polynomial be a negative number?", "No, all variable exponents must be whole numbers (\\(\\ge 0\\))", ["Yes, for reciprocal polynomials", "Yes, when negative powers exist", "Only for zero polynomial"]),
                ("If \\(\\deg(P) = 7\\) and \\(\\deg(Q) = 7\\), and their leading terms do NOT cancel, what is \\(\\deg(P + Q)\\)?", "7", ["14", "0", "1"])
            ],
            'tmpls': [
                "{0}",
                "Answer the following conceptual question: {0}",
                "Select the correct statement: {0}",
                "Evaluate the degree property: {0}",
                "Determine the correct result: {0}",
                "Choose the true mathematical conclusion: {0}",
                "Solve the degree property problem: {0}",
                "State the correct answer: {0}",
                "Which option correctly answers: {0}",
                "Analyze the degree condition: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Understand the Degree Rules**\nDegree of sum: \\(\\deg(P \\pm Q) \\le \\max(\\deg P, \\deg Q)\\).\nWhen degrees are unequal, the higher degree strictly determines the result.\nWhen degrees are equal, the leading terms might cancel, making the degree strictly \\(\\le n\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_3_1_2():
    tc = "MH-9-MTH1-3-3.1.2"
    tname = "Standard form, Index form, and Coefficient form"
    
    archs = [
        # Arch 0: Standard form (descending powers)
        {
            'data': [
                ("3x - 5x^3 + 7 + x^4", "x^4 - 5x^3 + 3x + 7", ["-5x^3 + x^4 + 3x + 7", "7 + 3x - 5x^3 + x^4", "x^4 + 3x - 5x^3 + 7"]),
                ("4 - x^2 + 8x^5 - 2x", "8x^5 - x^2 - 2x + 4", ["-x^2 + 8x^5 - 2x + 4", "8x^5 - 2x - x^2 + 4", "4 - 2x - x^2 + 8x^5"]),
                ("2x^2 + 5x^4 - 3 - x", "5x^4 + 2x^2 - x - 3", ["-3 - x + 2x^2 + 5x^4", "5x^4 - x + 2x^2 - 3", "2x^2 + 5x^4 - x - 3"]),
                ("7x + 9x^3 - 4", "9x^3 + 7x - 4", ["-4 + 7x + 9x^3", "7x + 9x^3 - 4", "9x^3 - 4 + 7x"]),
                ("1 - y^6 + 3y^2 - 5y^4", "-y^6 - 5y^4 + 3y^2 + 1", ["1 + 3y^2 - 5y^4 - y^6", "-y^6 + 3y^2 - 5y^4 + 1", "-5y^4 - y^6 + 3y^2 + 1"]),
                ("6m^2 - 2m^5 + m - 8", "-2m^5 + 6m^2 + m - 8", ["-8 + m + 6m^2 - 2m^5", "6m^2 - 2m^5 + m - 8", "-2m^5 + m + 6m^2 - 8"]),
                ("5p - 2 + 4p^3", "4p^3 + 5p - 2", ["-2 + 5p + 4p^3", "5p + 4p^3 - 2", "4p^3 - 2 + 5p"]),
                ("3x^3 + 8x^7 - x", "8x^7 + 3x^3 - x", ["-x + 3x^3 + 8x^7", "3x^3 - x + 8x^7", "8x^7 - x + 3x^3"]),
                ("10 - 3z^2 + z^4 - 2z", "z^4 - 3z^2 - 2z + 10", ["10 - 2z - 3z^2 + z^4", "z^4 - 2z - 3z^2 + 10", "-3z^2 + z^4 - 2z + 10"]),
                ("2x - x^3 + 5x^2 - 7", "-x^3 + 5x^2 + 2x - 7", ["-7 + 2x + 5x^2 - x^3", "5x^2 - x^3 + 2x - 7", "-x^3 + 2x + 5x^2 - 7"])
            ],
            'tmpls': [
                "Write the polynomial \\({0}\\) in standard form:",
                "Express \\({0}\\) in standard form (descending powers of variable):",
                "What is the standard form of \\({0}\\)?",
                "Rearrange \\({0}\\) into standard form:",
                "Convert \\({0}\\) to standard form:",
                "In standard form, \\({0}\\) is written as:",
                "Write \\({0}\\) by ordering terms by descending power:",
                "Select the correct standard form of \\({0}\\):",
                "Which of the following is the standard form of \\({0}\\)?",
                "Represent \\({0}\\) in its canonical standard form:"
            ],
            'calc': lambda item: (
                f"\\({item[1]}\\)",
                [f"\\({d}\\)" for d in item[2]],
                f"**Step 1: Arrange by Descending Powers of the Variable**\nSort the terms so the exponents decrease from left to right.\n**Step 2: Write the Terms**\n\\({item[1]}\\).\n**Step 3: Conclusion**\nThe standard form is \\({item[1]}\\)."
            ),
            'diff': 'easy'
        },
        # Arch 1: Index form (inserting 0 for missing terms)
        {
            'data': [
                ("x^3 - 2", "x^3 + 0x^2 + 0x - 2", ["x^3 - 2x + 0", "x^3 + 0x - 2", "x^3 + 0x^2 - 2"]),
                ("5x^4 - 3x + 1", "5x^4 + 0x^3 + 0x^2 - 3x + 1", ["5x^4 + 0x^2 - 3x + 1", "5x^4 + 0x^3 - 3x + 1", "5x^4 - 3x + 1 + 0"]),
                ("2m^5 + 7", "2m^5 + 0m^4 + 0m^3 + 0m^2 + 0m + 7", ["2m^5 + 0m + 7", "2m^5 + 0m^3 + 7", "2m^5 + 7m + 0"]),
                ("p^3 - 4p^2 + 9", "p^3 - 4p^2 + 0p + 9", ["p^3 - 4p^2 + 9", "p^3 + 0p^2 - 4p + 9", "p^3 - 4p^2 + 0"]),
                ("-2y^4 + 3y^2 - 1", "-2y^4 + 0y^3 + 3y^2 + 0y - 1", ["-2y^4 + 3y^2 + 0y - 1", "-2y^4 + 0y^3 + 3y^2 - 1", "-2y^4 + 3y^2 - 1"]),
                ("7x^2 - 5", "7x^2 + 0x - 5", ["7x^2 - 5x + 0", "7x^2 - 5", "7x^2 + 0x^2 - 5"]),
                ("4x^6 - x^2", "4x^6 + 0x^5 + 0x^4 + 0x^3 - x^2 + 0x + 0", ["4x^6 - x^2 + 0", "4x^6 + 0x^4 - x^2 + 0", "4x^6 + 0x^3 - x^2"]),
                ("8z^3 - z", "8z^3 + 0z^2 - z + 0", ["8z^3 - z + 0", "8z^3 + 0z - z", "8z^3 + 0z^2 - z"]),
                ("x^5 + 1", "x^5 + 0x^4 + 0x^3 + 0x^2 + 0x + 1", ["x^5 + 0x + 1", "x^5 + 0x^3 + 1", "x^5 + 1 + 0"]),
                ("-3x^3 + 2x^2 - 4", "-3x^3 + 2x^2 + 0x - 4", ["-3x^3 + 2x^2 - 4", "-3x^3 + 0x^2 + 2x - 4", "-3x^3 + 2x^2 - 4x + 0"])
            ],
            'tmpls': [
                "Write the polynomial \\({0}\\) in index form:",
                "Express \\({0}\\) in index form (showing all missing powers with 0 coefficient):",
                "What is the index form of \\({0}\\)?",
                "Convert \\({0}\\) into index form:",
                "In index form, \\({0}\\) is written as:",
                "State the complete index form of \\({0}\\):",
                "Represent \\({0}\\) with zero coefficients for absent powers (index form):",
                "Select the correct index form of \\({0}\\):",
                "Which expression correctly shows \\({0}\\) in index form?",
                "Transform the polynomial \\({0}\\) into its index form:"
            ],
            'calc': lambda item: (
                f"\\({item[1]}\\)",
                [f"\\({d}\\)" for d in item[2]],
                f"**Step 1: Identify Missing Powers**\nList all integer powers from the degree down to 0.\n**Step 2: Insert Zero Coefficients**\nEvery missing power gets a coefficient of 0.\n**Step 3: Conclusion**\nThe index form is \\({item[1]}\\)."
            ),
            'diff': 'easy'
        },
        # Arch 2: Converting index form to coefficient form
        {
            'data': [
                ("x^3 - 3x + 5", "x^3 + 0x^2 - 3x + 5", "(1, 0, -3, 5)", ["(1, -3, 5)", "(1, 0, 3, 5)", "(1, -3, 0, 5)"]),
                ("2x^4 - 5x^2 + 7", "2x^4 + 0x^3 - 5x^2 + 0x + 7", "(2, 0, -5, 0, 7)", ["(2, -5, 7)", "(2, 0, -5, 7)", "(2, -5, 0, 7)"]),
                ("y^5 - 1", "y^5 + 0y^4 + 0y^3 + 0y^2 + 0y - 1", "(1, 0, 0, 0, 0, -1)", ["(1, -1)", "(1, 0, 0, -1)", "(1, 0, 0, 0, -1)"]),
                ("3m^2 + 4m - 2", "3m^2 + 4m - 2", "(3, 4, -2)", ["(3, 4, 2)", "(3, 0, 4, -2)", "(3, -2)"]),
                ("-4p^3 + 7p", "-4p^3 + 0p^2 + 7p + 0", "(-4, 0, 7, 0)", ["(-4, 7)", "(-4, 7, 0)", "(-4, 0, 7)"]),
                ("5x - 8", "5x - 8", "(5, -8)", ["(5, 8)", "(5, 0, -8)", "(-8, 5)"]),
                ("x^4 + 2x^3 - x + 9", "x^4 + 2x^3 + 0x^2 - x + 9", "(1, 2, 0, -1, 9)", ["(1, 2, -1, 9)", "(1, 2, 0, 1, 9)", "(1, 0, 2, -1, 9)"]),
                ("-2x^3 + 4", "-2x^3 + 0x^2 + 0x + 4", "(-2, 0, 0, 4)", ["(-2, 4)", "(-2, 0, 4)", "(-2, 4, 0, 0)"]),
                ("7x^2 - 3x", "7x^2 - 3x + 0", "(7, -3, 0)", ["(7, -3)", "(7, 0, -3)", "(7, 3, 0)"]),
                ("6", "6", "(6,)", ["(6, 0)", "(0, 6)", "(1, 6)"])
            ],
            'tmpls': [
                "Write the polynomial \\({0}\\) in coefficient form:",
                "What is the coefficient form of \\({0}\\)?",
                "Convert \\({0}\\) into coefficient form:",
                "Express the polynomial \\({0}\\) in coefficient form:",
                "In coefficient form, \\({0}\\) is represented as:",
                "State the coefficient form of \\({0}\\):",
                "Determine the coefficient form of \\({0}\\):",
                "Select the correct coefficient form of \\({0}\\):",
                "Which tuple represents \\({0}\\) in coefficient form?",
                "Find the coefficient form for the expression \\({0}\\):"
            ],
            'calc': lambda item: (
                item[2],
                item[3],
                f"**Step 1: Write in Index Form**\n\\({item[0]} = {item[1]}\\).\n**Step 2: Extract the Coefficients in Order**\nList the coefficients from the highest power down to the constant term: {item[2]}.\n**Step 3: Conclusion**\nThe coefficient form is {item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 3: Converting coefficient form back to polynomial form
        {
            'data': [
                ("(1, 2, 3)", "x^2 + 2x + 3", ["x^3 + 2x^2 + 3x", "x + 2x^2 + 3", "x^2 + 3x + 2"], "3 terms \\implies \\deg = 2"),
                ("(2, -1, 0, 5)", "2x^3 - x^2 + 5", ["2x^4 - x^3 + 5", "2x^3 - x + 5", "2x^2 - x + 5"], "4 terms \\implies \\deg = 3"),
                ("(1, 0, 0, -8)", "x^3 - 8", ["x^4 - 8", "x^3 - 4", "x^2 - 8"], "4 terms \\implies \\deg = 3"),
                ("(3, -2, 4, -1)", "3x^3 - 2x^2 + 4x - 1", ["3x^4 - 2x^3 + 4x^2 - x", "3x^2 - 2x + 4", "3x^3 + 2x^2 - 4x - 1"], "4 terms \\implies \\deg = 3"),
                ("(5, 0, 0, 0, 2)", "5x^4 + 2", ["5x^5 + 2", "5x^3 + 2", "5x^4 - 2"], "5 terms \\implies \\deg = 4"),
                ("(-1, 4, -3)", "-x^2 + 4x - 3", ["-x^3 + 4x^2 - 3x", "-x^2 - 4x - 3", "x^2 - 4x + 3"], "3 terms \\implies \\deg = 2"),
                ("(4, 0, -7)", "4x^2 - 7", ["4x - 7", "4x^3 - 7", "4x^2 + 7"], "3 terms \\implies \\deg = 2"),
                ("(1, -5)", "x - 5", ["x^2 + 5", "x + 5", "5x - 1"], "2 terms \\implies \\deg = 1"),
                ("(2, 0, -3, 0, 1)", "2x^4 - 3x^2 + 1", ["2x^5 - 3x^3 + x", "2x^4 - 3x + 1", "2x^3 - 3x + 1"], "5 terms \\implies \\deg = 4"),
                ("(-3, 0, 0)", "-3x^2", ["-3x^3", "3x^2", "-3x + 1"], "3 terms \\implies \\deg = 2")
            ],
            'tmpls': [
                "Write the polynomial in variable x for the coefficient form {0}:",
                "Convert the coefficient form {0} into standard polynomial form in x:",
                "What polynomial corresponds to the coefficient form {0}?",
                "Express the coefficient form {0} as a polynomial in x:",
                "The polynomial in x represented by the coefficient form {0} is:",
                "State the polynomial in x corresponding to {0}:",
                "Determine the polynomial represented by {0}:",
                "Select the correct polynomial for the coefficient form {0}:",
                "Which polynomial has the coefficient form {0}?",
                "Transform the coefficient form {0} back into standard polynomial form:"
            ],
            'calc': lambda item: (
                f"\\({item[1]}\\)",
                [f"\\({d}\\)" for d in item[2]],
                f"**Step 1: Determine the Degree**\nIf there are \\(n\\) numbers in the coefficient form, the degree is \\(n - 1\\) ({item[3]}).\n**Step 2: Multiply by Descending Powers of x**\nCombine each coefficient with its respective power of \\(x\\).\n**Step 3: Conclusion**\nThe polynomial is \\({item[1]}\\)."
            ),
            'diff': 'easy'
        },
        # Arch 4: Determining degree and number of terms from forms
        {
            'data': [
                ("(4, -2, 0, 7, 1)", "4 (since there are 5 coefficients, \\(5 - 1 = 4\\))", ["5", "3", "1"]),
                ("(1, 0, 0, 0, 0, -9)", "5 (6 coefficients \\implies \\(6 - 1 = 5\\))", ["6", "4", "1"]),
                ("(7, 2, -3)", "2 (3 coefficients \\implies \\(3 - 1 = 2\\))", ["3", "1", "7"]),
                ("(5, -1)", "1 (2 coefficients \\implies \\(2 - 1 = 1\\))", ["2", "0", "5"]),
                ("(8,)", "0 (1 coefficient \\implies \\(1 - 1 = 0\\))", ["1", "8", "Not defined"]),
                ("(2, 0, 0, -4, 3, 0, 5)", "6 (7 coefficients \\implies \\(7 - 1 = 6\\))", ["7", "5", "4"]),
                ("(-3, 5, 2, 0)", "3 (4 coefficients \\implies \\(4 - 1 = 3\\))", ["4", "2", "-3"]),
                ("(1, 1, 1, 1, 1)", "4 (5 coefficients \\implies \\(5 - 1 = 4\\))", ["5", "3", "1"]),
                ("(9, 0, -2, 4)", "3 (4 coefficients \\implies \\(4 - 1 = 3\\))", ["4", "2", "9"]),
                ("(6, -7, 0, 0, 0)", "4 (5 coefficients \\implies \\(5 - 1 = 4\\))", ["5", "2", "1"])
            ],
            'tmpls': [
                "What is the degree of the polynomial whose coefficient form is {0}?",
                "Find the degree of the polynomial represented by {0}:",
                "Determine the degree of the polynomial given in coefficient form {0}:",
                "State the degree of the polynomial with coefficient form {0}:",
                "From the coefficient form {0}, identify the degree of the polynomial:",
                "Calculate the degree of the polynomial represented by {0}:",
                "Select the degree of the polynomial with coefficient form {0}:",
                "The degree of the polynomial represented by {0} is:",
                "How many is the degree of the polynomial with coefficients {0}?",
                "Evaluate the degree of the polynomial having coefficient form {0}:"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Count the Number of Coefficients**\nLet the count of coefficients be \\(n\\).\n**Step 2: Apply Degree Formula**\n\\(\Degree = n - 1\\).\n**Step 3: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 5: Missing terms count
        {
            'data': [
                ("x^5 - 1", "4 missing terms (\\(x^4, x^3, x^2, x\\))", ["3 missing terms", "5 missing terms", "1 missing term"]),
                ("3x^4 + 2x - 5", "2 missing terms (\\(x^3, x^2\\))", ["1 missing term", "3 missing terms", "0 missing terms"]),
                ("7x^6 - 2x^2 + 4", "4 missing terms (\\(x^5, x^4, x^3, x\\))", ["3 missing terms", "5 missing terms", "2 missing terms"]),
                ("x^3 + 5x^2 - 2x + 8", "0 missing terms (all powers from 3 to 0 are present)", ["1 missing term", "2 missing terms", "3 missing terms"]),
                ("4m^7 + 3", "6 missing terms (\\(m^6, m^5, m^4, m^3, m^2, m\\))", ["7 missing terms", "5 missing terms", "1 missing term"]),
                ("2y^3 - 7", "2 missing terms (\\(y^2, y\\))", ["1 missing term", "3 missing terms", "0 missing terms"]),
                ("5p^4 - 2p^3 + 1", "2 missing terms (\\(p^2, p\\))", ["1 missing term", "3 missing terms", "0 missing terms"]),
                ("8z^2 - 3z", "1 missing term (constant term \\(z^0\\))", ["0 missing terms", "2 missing terms", "3 missing terms"]),
                ("x^6 - x^3", "5 missing terms (\\(x^5, x^4, x^2, x, \\text{constant}\\))", ["4 missing terms", "3 missing terms", "2 missing terms"]),
                ("9x^5 + 4x^4 - 2", "3 missing terms (\\(x^3, x^2, x\\))", ["2 missing terms", "4 missing terms", "1 missing term"])
            ],
            'tmpls': [
                "How many missing terms need to be added with coefficient 0 to write \\({0}\\) in index form?",
                "Determine the number of missing terms in \\({0}\\):",
                "Find the count of zero-coefficient terms required for the index form of \\({0}\\):",
                "In writing \\({0}\\) in index form, how many terms have coefficient 0?",
                "Identify the missing powers of the variable in \\({0}\\):",
                "How many powers of the variable are missing between degree and 0 in \\({0}\\)?",
                "Calculate the number of missing terms in \\({0}\\):",
                "Select the number of missing terms in the polynomial \\({0}\\):",
                "The number of missing intermediate terms in \\({0}\\) is:",
                "State the missing term count for \\({0}\\):"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Identify the Degree**\nFind the degree \\(n\\) of \\({item[0]}\\).\nA complete polynomial has \\(n + 1\\) terms.\n**Step 2: Count Existing Terms**\nSubtract the number of non-zero terms present from \\(n + 1\\).\n**Step 3: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 6: Coefficient of a specific power x^k
        {
            'data': [
                ("3x^4 - 5x^3 + 7x - 2", "x^2", "0 (since the term is missing in the polynomial)", ["7", "-5", "3"]),
                ("4x^5 + 6x^3 - 8x + 1", "x^3", "6", ["-8", "4", "0"]),
                ("x^4 - x^3 + 5x^2 - 9", "x^3", "-1", ["1", "0", "-9"]),
                ("7x^3 + 2x^2 - 4x + 11", "x", "-4", ["4", "2", "7"]),
                ("2x^6 - 9x^4 + 3", "x^5", "0 (absent term)", ["2", "-9", "3"]),
                ("5x^3 - x^2 + 4x - 6", "x^2", "-1", ["1", "5", "-6"]),
                ("8x^4 + 3x - 10", "x^4", "8", ["3", "-10", "0"]),
                ("x^5 + 4x^3 - 7x^2 + 2", "x", "0", ["2", "-7", "4"]),
                ("-6x^3 + 2x^2 - x + 5", "x", "-1", ["1", "2", "-6"]),
                ("12x^2 - 5x + 3", "x^0 \\text{ (the constant term)}", "3", ["-5", "12", "0"])
            ],
            'tmpls': [
                "In the polynomial \\({0}\\), what is the coefficient of \\({1}\\)?",
                "Find the coefficient of \\({1}\\) in \\({0}\\):",
                "Determine the coefficient of \\({1}\\) in the polynomial \\({0}\\):",
                "What is the coefficient of \\({1}\\) in the expression \\({0}\\)?",
                "Identify the coefficient of \\({1}\\) in \\({0}\\):",
                "State the numerical coefficient of \\({1}\\) in \\({0}\\):",
                "Select the coefficient of \\({1}\\) in \\({0}\\):",
                "Evaluate the coefficient of \\({1}\\) in \\({0}\\):",
                "From \\({0}\\), read the coefficient of \\({1}\\):",
                "In the algebraic expression \\({0}\\), the coefficient of \\({1}\\) is:"
            ],
            'calc': lambda item: (
                item[2],
                item[3],
                f"**Step 1: Locate the Term with \\({item[1]}\\)**\nInspect \\({item[0]}\\) for \\({item[1]}\\).\nIf the term is present, read its multiplying sign and number.\nIf the term is absent, its coefficient is 0.\n**Step 2: Conclusion**\nThe coefficient of \\({item[1]}\\) is {item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 7: Coefficient form properties and comparisons
        {
            'data': [
                ("Are the polynomials with coefficient forms (1, 2, 3) and (0, 1, 2, 3) identical?", "Yes, because leading zero coefficients do not change the polynomial \\(x^2 + 2x + 3\\)", ["No, (0, 1, 2, 3) has degree 3", "No, they represent completely different functions", "Only if x = 0"]),
                ("What does the last entry in any coefficient form represent?", "The constant term \\(a_0\\) (coefficient of \\(x^0\\))", ["The leading coefficient", "The degree of the polynomial", "The coefficient of x"]),
                ("What does the first non-zero entry in a coefficient form represent?", "The leading coefficient of the polynomial", ["The constant term", "The degree", "The number of variables"]),
                ("If a polynomial has degree 4, how many numbers must be in its coefficient form?", "Exactly 5 numbers", ["4 numbers", "3 numbers", "6 numbers"]),
                ("Which coefficient form represents the polynomial \\(2x^3 - 5\\)?", "(2, 0, 0, -5)", ["(2, -5)", "(2, 0, -5)", "(2, -5, 0, 0)"]),
                ("Which polynomial is represented by the coefficient form (3, 0, 0, 0)?", "\\(3x^3\\)", ["\\(3x^4\\)", "\\(3\\)", "\\(3x\\)"]),
                ("What is the coefficient form of \\(x^2 - x\\)?", "(1, -1, 0)", ["(1, -1)", "(1, 0, -1)", "(-1, 0)"]),
                ("If the coefficient form is (-2, 0, 7), what is the degree?", "2", ["3", "1", "0"]),
                ("What is the coefficient form of the constant polynomial 0?", "(0,)", ["()", "(0, 0)", "Undefined"]),
                ("Can a coefficient in coefficient form be a fraction or negative number?", "Yes, coefficients can be any real numbers", ["No, only positive integers are allowed", "No, only whole numbers", "Only rational numbers"])
            ],
            'tmpls': [
                "{0}",
                "Answer the following question on polynomial forms: {0}",
                "Select the correct statement: {0}",
                "Evaluate the concept: {0}",
                "Determine the true mathematical fact: {0}",
                "Choose the correct response: {0}",
                "Solve the conceptual problem: {0}",
                "State the correct answer: {0}",
                "Which option correctly answers: {0}",
                "Analyze the coefficient form rule: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Understand Coefficient Form Rules**\nIn coefficient form \\((a_n, a_(n-1), \\dots, a_1, a_0)\\), there are \\(n+1\\) entries for a degree \\(n\\) polynomial.\nAll missing powers must have 0.\nThe last entry is the constant term.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_3_2():
    tc = "MH-9-MTH1-3-3.2"
    tname = "Operations on Polynomials: Addition, Subtraction, Multiplication"
    
    archs = [
        # Arch 0: Addition of polynomials
        {
            'data': [
                ("(3x^2 - 5x + 7)", "(2x^2 + 4x - 3)", "5x^2 - x + 4", ["5x^2 + x + 4", "5x^2 - 9x + 10", "6x^2 - x + 4"]),
                ("(4x^3 + 2x^2 - x)", "(x^3 - 5x^2 + 6x - 2)", "5x^3 - 3x^2 + 5x - 2", ["5x^3 + 7x^2 + 5x - 2", "4x^3 - 3x^2 + 5x - 2", "5x^3 - 3x^2 - 7x - 2"]),
                ("(7y^2 - 3y + 8)", "(2y^2 - 5)", "9y^2 - 3y + 3", ["9y^2 - 8y + 3", "9y^2 + 3y + 3", "5y^2 - 3y + 13"]),
                ("(x^3 - 4x + 1)", "(2x^2 + 3x - 5)", "x^3 + 2x^2 - x - 4", ["3x^3 - x - 4", "x^3 + 2x^2 + 7x - 4", "x^3 - 2x^2 - x - 4"]),
                ("(5m^2 - 2m + 9)", "(-3m^2 + 7m - 4)", "2m^2 + 5m + 5", ["8m^2 + 5m + 5", "2m^2 - 9m + 5", "2m^2 + 5m - 5"]),
                ("(6p^3 - p^2 + 4)", "(3p^2 - 2p - 8)", "6p^3 + 2p^2 - 2p - 4", ["6p^3 - 4p^2 - 2p - 4", "9p^3 + 2p^2 - 4", "6p^3 + 2p^2 + 2p - 4"]),
                ("(2x^4 - 3x^2 + 5)", "(x^4 + 4x^2 - 1)", "3x^4 + x^2 + 4", ["3x^4 - 7x^2 + 4", "2x^4 + x^2 + 4", "3x^4 + x^2 - 4"]),
                ("(8a^2 - 3a + 2)", "(a^2 + 5a - 7)", "9a^2 + 2a - 5", ["9a^2 - 8a - 5", "7a^2 + 2a - 5", "9a^2 + 2a + 5"]),
                ("(x^3 + 3x^2 - 2x + 6)", "(-x^3 + 2x^2 + 4x - 1)", "5x^2 + 2x + 5", ["2x^3 + 5x^2 + 2x + 5", "5x^2 - 6x + 5", "5x^2 + 2x - 5"]),
                ("(4y^2 - 6y + 1)", "(2y^2 + 6y - 9)", "6y^2 - 8", ["6y^2 - 12y - 8", "6y^2 + 12y - 8", "2y^2 - 8"])
            ],
            'tmpls': [
                "Add the polynomials \\({0}\\) and \\({1}\\):",
                "Find the sum of \\({0}\\) and \\({1}\\):",
                "Evaluate the addition: \\({0} + {1}\\):",
                "Simplify \\({0} + {1}\\):",
                "Calculate the sum of the two polynomials \\({0}\\) and \\({1}\\):",
                "What is the result when \\({0}\\) is added to \\({1}\\)?",
                "Add: \\({0} + {1}\\):",
                "Determine the sum \\({0} + {1}\\):",
                "Compute the polynomial addition: \\({0} + {1}\\):",
                "Combine like terms in \\({0} + {1}\\):"
            ],
            'calc': lambda item: (
                f"\\({item[2]}\\)",
                [f"\\({d}\\)" for d in item[3]],
                f"**Step 1: Group Like Terms Together**\nCombine terms with identical powers of the variable from \\({item[0]}\\) and \\({item[1]}\\).\n**Step 2: Add the Coefficients**\nAdd coefficients of matching powers.\n**Step 3: Conclusion**\nThe sum is \\({item[2]}\\)."
            ),
            'diff': 'easy'
        },
        # Arch 1: Subtraction of polynomials
        {
            'data': [
                ("(5x^2 - 3x + 8)", "(2x^2 + 4x - 1)", "3x^2 - 7x + 9", ["3x^2 + x + 7", "7x^2 - 7x + 9", "3x^2 - 7x - 9"]),
                ("(4x^3 + 2x^2 - 5)", "(x^3 - 3x^2 + 2x - 7)", "3x^3 + 5x^2 - 2x + 2", ["3x^3 - x^2 + 2x - 12", "5x^3 - x^2 - 2x + 2", "3x^3 + 5x^2 + 2x + 2"]),
                ("(7y^2 - 4y + 2)", "(3y^2 - 4y + 9)", "4y^2 - 7", ["4y^2 - 8y - 7", "10y^2 - 7", "4y^2 + 8y + 11"]),
                ("(6m^3 - 2m^2 + 5m)", "(4m^3 + m^2 - 3m + 8)", "2m^3 - 3m^2 + 8m - 8", ["2m^3 - m^2 + 2m - 8", "10m^3 - m^2 + 2m + 8", "2m^3 - 3m^2 + 8m + 8"]),
                ("(3x^2 + 7x - 4)", "(5x^2 - 2x + 1)", "-2x^2 + 9x - 5", ["-2x^2 + 5x - 5", "2x^2 - 9x + 5", "-2x^2 + 9x + 5"]),
                ("(8a^2 - 6a + 11)", "(2a^2 + 3a - 4)", "6a^2 - 9a + 15", ["6a^2 - 3a + 7", "10a^2 - 9a + 15", "6a^2 + 9a - 15"]),
                ("(x^4 - 2x^2 + 9)", "(3x^4 + x^2 - 5)", "-2x^4 - 3x^2 + 14", ["-2x^4 - x^2 + 4", "4x^4 - x^2 + 4", "-2x^4 - 3x^2 - 14"]),
                ("(9p^2 - 4p + 3)", "(9p^2 + 2p - 8)", "-6p + 11", ["6p + 11", "-6p - 5", "18p^2 - 2p - 5"]),
                ("(2x^3 - x + 4)", "(5x^2 - 3x + 1)", "2x^3 - 5x^2 + 2x + 3", ["-3x^3 - 4x + 3", "2x^3 - 5x^2 - 4x + 3", "2x^3 + 5x^2 + 2x + 3"]),
                ("(10y^2 - 5)", "(4y^2 - 3y + 7)", "6y^2 + 3y - 12", ["6y^2 - 3y - 12", "6y^2 + 3y + 2", "14y^2 - 3y + 2"])
            ],
            'tmpls': [
                "Subtract \\({1}\\) from \\({0}\\):",
                "Find \\({0} - {1}\\):",
                "Evaluate the subtraction: \\({0} - {1}\\):",
                "Simplify \\({0} - {1}\\):",
                "Calculate \\({0} - {1}\\):",
                "What is the result when \\({1}\\) is subtracted from \\({0}\\)?",
                "Perform the polynomial subtraction: \\({0} - {1}\\):",
                "Subtract: \\({0} - {1}\\):",
                "Determine the difference: \\({0} - {1}\\):",
                "Compute the value of \\({0} - {1}\\):"
            ],
            'calc': lambda item: (
                f"\\({item[2]}\\)",
                [f"\\({d}\\)" for d in item[3]],
                f"**Step 1: Distribute the Negative Sign**\nChange the sign of each term in the second polynomial \\({item[1]}\\).\n**Step 2: Combine with Like Terms of \\({item[0]}\\)**\nAdd the corresponding coefficients.\n**Step 3: Conclusion**\nThe difference is \\({item[2]}\\)."
            ),
            'diff': 'easy'
        },
        # Arch 2: Multiplication of monomial by polynomial
        {
            'data': [
                ("3x", "(2x^2 - 5x + 4)", "6x^3 - 15x^2 + 12x", ["6x^2 - 15x + 12", "6x^3 - 5x^2 + 12x", "5x^3 - 2x^2 + 7x"]),
                ("-2x^2", "(4x^3 - 3x + 7)", "-8x^5 + 6x^3 - 14x^2", ["-8x^6 + 6x^3 - 14x^2", "-8x^5 - 6x^3 + 14x^2", "8x^5 - 6x^3 + 14x^2"]),
                ("5y", "(3y^2 + 2y - 6)", "15y^3 + 10y^2 - 30y", ["15y^2 + 10y - 30", "15y^3 + 10y^2 - 6", "8y^3 + 7y^2 - y"]),
                ("-4m^3", "(2m^2 - m + 3)", "-8m^5 + 4m^4 - 12m^3", ["-8m^6 + 4m^4 - 12m^3", "8m^5 - 4m^4 + 12m^3", "-8m^5 - 4m^4 - 12m^3"]),
                ("2x", "(x^4 - 3x^2 + 5)", "2x^5 - 6x^3 + 10x", ["2x^4 - 6x^2 + 10x", "2x^5 - 3x^3 + 5x", "3x^5 - x^3 + 7x"]),
                ("7a^2", "(a^3 - 4a + 2)", "7a^5 - 28a^3 + 14a^2", ["7a^6 - 28a^3 + 14a^2", "7a^5 - 4a^3 + 2a^2", "8a^5 - 28a^3 + 14a^2"]),
                ("-x", "(5x^2 - 2x + 9)", "-5x^3 + 2x^2 - 9x", ["-5x^3 - 2x^2 - 9x", "5x^3 - 2x^2 + 9x", "-5x^2 + 2x - 9"]),
                ("6p", "(2p^2 + 3p - 1)", "12p^3 + 18p^2 - 6p", ["12p^2 + 18p - 6", "12p^3 + 9p^2 - 6p", "8p^3 + 9p^2 - 6p"]),
                ("-3y^2", "(2y^2 - 4y + 1)", "-6y^4 + 12y^3 - 3y^2", ["-6y^4 - 12y^3 - 3y^2", "6y^4 - 12y^3 + 3y^2", "-6y^3 + 12y^2 - 3y"]),
                ("4x^3", "(3x^2 - 5)", "12x^5 - 20x^3", ["12x^6 - 20x^3", "12x^5 - 5", "7x^5 - 20x^3"])
            ],
            'tmpls': [
                "Multiply the monomial and polynomial: \\({0} \\cdot {1}\\):",
                "Find the product \\({0} \\times {1}\\):",
                "Evaluate the product \\({0}{1}\\):",
                "Simplify \\({0} \\cdot {1}\\):",
                "Calculate the multiplication: \\({0}{1}\\):",
                "What is the product of \\({0}\\) and \\({1}\\)?",
                "Multiply: \\({0}{1}\\):",
                "Determine the expanded form of \\({0} \\cdot {1}\\):",
                "Compute \\({0}{1}\\):",
                "Expand the algebraic expression \\({0}{1}\\):"
            ],
            'calc': lambda item: (
                f"\\({item[2]}\\)",
                [f"\\({d}\\)" for d in item[3]],
                f"**Step 1: Apply the Distributive Law**\nMultiply \\({item[0]}\\) by every single term inside the parentheses \\({item[1]}\\).\n**Step 2: Add Exponents for Powers of Variable**\n\\(x^m \\cdot x^n = x^(m+n)\\).\n**Step 3: Conclusion**\nThe product is \\({item[2]}\\)."
            ),
            'diff': 'easy'
        },
        # Arch 3: Multiplication of binomials (ax + b)(cx + d)
        {
            'data': [
                ("(x + 3)", "(x + 5)", "x^2 + 8x + 15", ["x^2 + 15x + 8", "x^2 + 8x + 8", "2x^2 + 8x + 15"]),
                ("(2x - 1)", "(x + 4)", "2x^2 + 7x - 4", ["2x^2 + 8x - 4", "2x^2 - 7x - 4", "2x^2 + 7x + 4"]),
                ("(3x + 2)", "(2x - 5)", "6x^2 - 11x - 10", ["6x^2 + 11x - 10", "6x^2 - 15x - 10", "5x^2 - 11x - 10"]),
                ("(x - 4)", "(x - 7)", "x^2 - 11x + 28", ["x^2 + 11x + 28", "x^2 - 11x - 28", "x^2 - 28x + 11"]),
                ("(4x + 1)", "(3x + 2)", "12x^2 + 11x + 2", ["12x^2 + 8x + 2", "7x^2 + 11x + 2", "12x^2 + 11x + 3"]),
                ("(5x - 2)", "(2x + 3)", "10x^2 + 11x - 6", ["10x^2 - 11x - 6", "10x^2 + 15x - 6", "7x^2 + 11x - 6"]),
                ("(2x - 3)", "(3x - 4)", "6x^2 - 17x + 12", ["6x^2 + 17x + 12", "6x^2 - 12x + 12", "5x^2 - 17x + 12"]),
                ("(x + 6)", "(2x - 1)", "2x^2 + 11x - 6", ["2x^2 + 12x - 6", "2x^2 - 11x - 6", "3x^2 + 11x - 6"]),
                ("(3x - 1)", "(3x + 1)", "9x^2 - 1", ["9x^2 + 1", "9x^2 - 6x - 1", "6x^2 - 1"]),
                ("(x - 5)", "(x + 5)", "x^2 - 25", ["x^2 + 25", "x^2 - 10x - 25", "2x^2 - 25"])
            ],
            'tmpls': [
                "Multiply the binomials: \\({0}{1}\\):",
                "Find the product of \\({0}\\) and \\({1}\\):",
                "Expand the expression \\({0}{1}\\):",
                "Evaluate \\({0} \\times {1}\\):",
                "Calculate the product \\({0}{1}\\):",
                "Simplify by expanding: \\({0}{1}\\):",
                "What is the expansion of \\({0}{1}\\)?",
                "Multiply: \\({0}{1}\\):",
                "Compute \\({0}{1}\\):",
                "Perform the binomial multiplication \\({0}{1}\\):"
            ],
            'calc': lambda item: (
                f"\\({item[2]}\\)",
                [f"\\({d}\\)" for d in item[3]],
                f"**Step 1: Apply FOIL / Distributive Method**\nMultiply First, Outer, Inner, and Last terms.\n**Step 2: Combine the Middle Linear Terms**\nAdd the like terms in \\(x\\).\n**Step 3: Conclusion**\nThe product is \\({item[2]}\\)."
            ),
            'diff': 'medium'
        },
        # Arch 4: Multiplication of binomial by trinomial
        {
            'data': [
                ("(x + 2)", "(x^2 - 2x + 4)", "x^3 + 8", ["x^3 - 8", "x^3 + 4x^2 + 8", "x^3 - 4x + 8"], "Sum of cubes identity \\((a+b)(a^2-ab+b^2) = a^3+b^3\\)"),
                ("(x - 3)", "(x^2 + 3x + 9)", "x^3 - 27", ["x^3 + 27", "x^3 - 6x^2 - 27", "x^3 + 9x - 27"], "Difference of cubes identity"),
                ("(x + 1)", "(x^2 + 3x - 2)", "x^3 + 4x^2 + x - 2", ["x^3 + 3x^2 + x - 2", "x^3 + 4x^2 - 2", "x^3 + 2x^2 + x - 2"], "Direct expansion"),
                ("(x - 2)", "(2x^2 - x + 5)", "2x^3 - 5x^2 + 7x - 10", ["2x^3 - 4x^2 + 7x - 10", "2x^3 - 5x^2 - 7x - 10", "2x^3 + 5x^2 + 7x - 10"], "Direct expansion"),
                ("(2x + 1)", "(x^2 - 3x + 4)", "2x^3 - 5x^2 + 5x + 4", ["2x^3 - 6x^2 + 5x + 4", "2x^3 - 5x^2 + 8x + 4", "2x^3 + 5x^2 - 5x + 4"], "Direct expansion"),
                ("(x + 3)", "(x^2 - x + 2)", "x^3 + 2x^2 - x + 6", ["x^3 + 3x^2 - x + 6", "x^3 + 2x^2 + x + 6", "x^3 - 2x^2 - x + 6"], "Direct expansion"),
                ("(3x - 2)", "(x^2 + 2x - 1)", "3x^3 + 4x^2 - 7x + 2", ["3x^3 + 6x^2 - 7x + 2", "3x^3 + 4x^2 + 7x + 2", "3x^3 - 4x^2 - 7x + 2"], "Direct expansion"),
                ("(x - 1)", "(x^2 + x + 1)", "x^3 - 1", ["x^3 + 1", "x^3 - 2x - 1", "x^3 + x^2 - 1"], "Difference of cubes"),
                ("(2x - 3)", "(4x^2 + 6x + 9)", "8x^3 - 27", ["8x^3 + 27", "8x^3 - 18x - 27", "8x^3 - 36x^2 - 27"], "Difference of cubes identity \\((2x)^3 - 3^3\\)"),
                ("(x + 4)", "(x^2 - 4x + 16)", "x^3 + 64", ["x^3 - 64", "x^3 + 8x^2 + 64", "x^3 - 16x + 64"], "Sum of cubes identity \\(x^3 + 4^3\\)")
            ],
            'tmpls': [
                "Expand the product \\({0}{1}\\):",
                "Multiply the binomial and trinomial: \\({0}{1}\\):",
                "Find the product of \\({0}\\) and \\({1}\\):",
                "Evaluate the polynomial product: \\({0}{1}\\):",
                "Simplify \\({0}{1}\\):",
                "Calculate \\({0} \\cdot {1}\\):",
                "What is the result of multiplying \\({0}\\) by \\({1}\\)?",
                "Compute the product: \\({0}{1}\\):",
                "Determine the expanded polynomial \\({0}{1}\\):",
                "Expand and combine like terms in \\({0}{1}\\):"
            ],
            'calc': lambda item: (
                f"\\({item[2]}\\)",
                [f"\\({d}\\)" for d in item[3]],
                f"**Step 1: Distribute Each Term of the Binomial**\nMultiply the first term of \\({item[0]}\\) by every term of \\({item[1]}\\), then multiply the second term of \\({item[0]}\\) by every term of \\({item[1]}\\).\n**Step 2: Combine Like Terms**\n{item[4]}.\n**Step 3: Conclusion**\nThe product is \\({item[2]}\\)."
            ),
            'diff': 'medium'
        },
        # Arch 5: Additive inverse and P - Q vs Q - P
        {
            'data': [
                ("3x^2 - 5x + 7", "-3x^2 + 5x - 7", ["3x^2 + 5x + 7", "-3x^2 - 5x + 7", "-3x^2 - 5x - 7"]),
                ("-4x^3 + 2x - 9", "4x^3 - 2x + 9", ["-4x^3 - 2x + 9", "4x^3 + 2x - 9", "4x^3 - 2x - 9"]),
                ("x^4 - 6x^2 + 2", "-x^4 + 6x^2 - 2", ["x^4 + 6x^2 - 2", "-x^4 - 6x^2 - 2", "-x^4 + 6x^2 + 2"]),
                ("7y - 12", "-7y + 12", ["7y + 12", "-7y - 12", "12y - 7"]),
                ("-2m^2 + 8m", "2m^2 - 8m", ["2m^2 + 8m", "-2m^2 - 8m", "8m^2 - 2m"]),
                ("5x^3 - x + 4", "-5x^3 + x - 4", ["-5x^3 - x - 4", "5x^3 + x - 4", "-5x^3 + x + 4"]),
                ("9p^2 + 3p - 1", "-9p^2 - 3p + 1", ["-9p^2 + 3p + 1", "9p^2 - 3p - 1", "-9p^2 - 3p - 1"]),
                ("-x^5 - 4", "x^5 + 4", ["-x^5 + 4", "x^5 - 4", "4x^5 + 1"]),
                ("2a^2 - 7a + 3", "-2a^2 + 7a - 3", ["2a^2 + 7a + 3", "-2a^2 - 7a - 3", "-2a^2 + 7a + 3"]),
                ("6 - 5x", "5x - 6", ["-5x - 6", "5x + 6", "-6 - 5x"])
            ],
            'tmpls': [
                "Find the additive inverse of the polynomial \\({0}\\):",
                "What is the negative (additive inverse) of \\({0}\\)?",
                "Determine the additive inverse of \\({0}\\):",
                "State the additive inverse of the algebraic expression \\({0}\\):",
                "The additive inverse of \\({0}\\) is given by:",
                "Evaluate \\(-({0})\\):",
                "Write the additive inverse of \\({0}\\):",
                "Which polynomial is the additive inverse of \\({0}\\)?",
                "Select the additive inverse of \\({0}\\):",
                "Compute the additive inverse of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"\\({item[1]}\\)",
                [f"\\({d}\\)" for d in item[2]],
                f"**Step 1: Multiply Entire Polynomial by -1**\nEvery term in \\({item[0]}\\) flips its sign.\n**Step 2: Conclusion**\nThe additive inverse is \\({item[1]}\\)."
            ),
            'diff': 'easy'
        },
        # Arch 6: Polynomial applications in geometry (Perimeter / Area)
        {
            'data': [
                ("A rectangle has length \\(2x + 3\\) and breadth \\(x + 1\\). Find its perimeter:", "Perimeter = \\(2(2x + 3 + x + 1) = 2(3x + 4) = 6x + 8\\)", ["3x + 4", "2x^2 + 5x + 3", "6x + 6"]),
                ("A rectangle has length \\(2x + 3\\) and breadth \\(x + 1\\). Find its area:", "Area = \\((2x + 3)(x + 1) = 2x^2 + 5x + 3\\)", ["6x + 8", "2x^2 + 3x + 3", "2x^2 + 4x + 3"]),
                ("A square has side \\(3x - 2\\). Find its perimeter:", "Perimeter = \\(4(3x - 2) = 12x - 8\\)", ["6x - 4", "9x^2 - 12x + 4", "12x - 2"]),
                ("A square has side \\(3x - 2\\). Find its area:", "Area = \\((3x - 2)^2 = 9x^2 - 12x + 4\\)", ["12x - 8", "9x^2 - 4", "9x^2 + 12x + 4"]),
                ("A triangle has sides \\(x + 2\\), \\(2x - 1\\), and \\(3x + 4\\). Find its perimeter:", "Perimeter = \\((x + 2) + (2x - 1) + (3x + 4) = 6x + 5\\)", ["6x + 7", "6x - 5", "5x + 5"]),
                ("The length of a rectangular park is \\(4x + 5\\) and width is \\(2x - 3\\). Find the perimeter:", "Perimeter = \\(2(4x + 5 + 2x - 3) = 2(6x + 2) = 12x + 4\\)", ["6x + 2", "8x^2 - 2x - 15", "12x + 8"]),
                ("The length of a rectangular plot is \\(4x + 5\\) and width is \\(2x - 3\\). Find its area:", "Area = \\((4x + 5)(2x - 3) = 8x^2 - 2x - 15\\)", ["12x + 4", "8x^2 + 2x - 15", "8x^2 - 15"]),
                ("A cuboid has dimensions \\(x\\), \\(x + 2\\), and \\(x + 3\\). What is its volume?", "Volume = \\(x(x + 2)(x + 3) = x(x^2 + 5x + 6) = x^3 + 5x^2 + 6x\\)", ["x^3 + 6", "3x + 5", "x^3 + 6x^2 + 5x"]),
                ("The perimeter of a triangle is \\(7x^2 - 3x + 8\\). Two of its sides are \\(2x^2 + x - 1\\) and \\(3x^2 - 4x + 5\\). Find the third side:", "Third side = \\((7x^2 - 3x + 8) - (5x^2 - 3x + 4) = 2x^2 + 4\\)", ["2x^2 - 6x + 4", "5x^2 - 3x + 4", "2x^2 + 4x + 12"]),
                ("If the area of a rectangle is \\(x^2 + 7x + 12\\) and breadth is \\(x + 3\\), what is its length?", "Length = \\(\\frac{x^2 + 7x + 12}{x + 3} = x + 4\\)", ["x + 3", "x - 4", "x + 7"])
            ],
            'tmpls': [
                "{0}",
                "Solve the geometry application: {0}",
                "Calculate the polynomial expression: {0}",
                "Find the polynomial solution: {0}",
                "Determine the expression for the geometric property: {0}",
                "State the result: {0}",
                "Evaluate the polynomial word problem: {0}",
                "Find the answer: {0}",
                "Select the correct expression: {0}",
                "Compute the required value: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Write the Geometric Formula**\nApply the standard formula (Perimeter, Area, or Volume).\n**Step 2: Substitute Polynomial Dimensions**\nPerform addition or multiplication of polynomials.\n**Step 3: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Degree of results under operations
        {
            'data': [
                ("If \\(\\deg(P) = 4\\) and \\(\\deg(Q) = 3\\), what is \\(\\deg(P \\cdot Q)\\)?", "7 (sum of degrees \\(4 + 3 = 7\\))", ["12", "4", "1"]),
                ("If \\(\\deg(P) = 5\\) and \\(\\deg(Q) = 2\\), what is the degree of \\(P - Q\\)?", "5 (highest degree determines the degree of difference)", ["3", "7", "10"]),
                ("If \\(\\deg(P) = 3\\) and \\(\\deg(Q) = 3\\), what is the maximum possible degree of \\(P + Q\\)?", "3 (can be \\(\\le 3\\) if leading terms cancel)", ["6", "9", "0"]),
                ("If \\(\\deg(P) = 2\\), what is \\(\\deg(P^3)\\)?", "6 (since \\(2 \\times 3 = 6\\))", ["8", "5", "9"]),
                ("When a polynomial of degree 4 is divided by a polynomial of degree 1, what is the degree of the quotient?", "3 (since \\(4 - 1 = 3\\))", ["4", "5", "1"]),
                ("What is the degree of the zero polynomial obtained when a polynomial is subtracted from itself \\(P - P\\)?", "Not defined", ["0", "1", "-1"]),
                ("If \\(\\deg(P) = m\\) and \\(\\deg(Q) = n\\), what is \\(\\deg(P \\cdot Q)\\)?", "\\(m + n\\)", ["\\(mn\\)", "\\(\\max(m, n)\\)", "\\(m - n\\)"]),
                ("If \\(\\deg(P) = 6\\) and \\(\\deg(Q) = 2\\), what is the degree of \\(\\frac{P}{Q}\\) (assuming exact division)?", "4 (since \\(6 - 2 = 4\\))", ["3", "8", "12"]),
                ("Can the addition of two polynomials of degree 3 produce a polynomial of degree 4?", "No, degree of sum can never exceed the maximum degree of the addends", ["Yes, if coefficients are large", "Yes, in multi-variable polynomials", "Only if both have degree 3"]),
                ("If \\(P(x) = 2x^2 + 1\\) and \\(Q(x) = -2x^2 + 3x\\), what is \\(\\deg(P + Q)\\)?", "1 (the \\(x^2\\) terms cancel out leaving \\(3x + 1\\))", ["2", "0", "Not defined"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the polynomial operation rule: {0}",
                "Determine the degree: {0}",
                "Answer the following question on polynomial degrees: {0}",
                "What is the mathematical conclusion? {0}",
                "Select the correct answer: {0}",
                "Analyze the degree relationship: {0}",
                "State the result: {0}",
                "Which option correctly answers: {0}",
                "Compute the resulting degree: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Understand Operation Rules on Degrees**\n\\(\\deg(P \\cdot Q) = \\deg(P) + \\deg(Q)\\).\n\\(\\deg(P \\pm Q) \\le \\max(\\deg P, \\deg Q)\\).\n\\(\\deg(P / Q) = \\deg(P) - \\deg(Q)\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_3_3_1():
    tc = "MH-9-MTH1-3-3.3.1"
    tname = "Synthetic division algorithm using opposite coefficients"
    
    archs = [
        # Arch 0: Division by (x - a) where a > 0
        {
            'data': [
                ("(x^2 + 2x + 3) \\div (x - 1)", "Quotient = \\(x + 3\\), Remainder = \\(6\\)", ["Quotient = \\(x + 1\\), Remainder = \\(4\\)", "Quotient = \\(x + 3\\), Remainder = \\(0\\)", "Quotient = \\(x - 3\\), Remainder = \\(6\\)"], "Opposite of -1 is 1: synthetic coefficients 1, 2, 3 with multiplier 1 gives row 1, 3 and remainder 3 + 3 = 6"),
                ("(2x^2 - 3x + 4) \\div (x - 2)", "Quotient = \\(2x + 1\\), Remainder = \\(6\\)", ["Quotient = \\(2x - 1\\), Remainder = \\(6\\)", "Quotient = \\(2x + 1\\), Remainder = \\(4\\)", "Quotient = \\(2x + 3\\), Remainder = \\(2\\)"], "Opposite of -2 is 2: 2, -3, 4 with 2 gives row 2, 1 and remainder 4 + 2 = 6"),
                ("(3x^2 - 5x - 8) \\div (x - 3)", "Quotient = \\(3x + 4\\), Remainder = \\(4\\)", ["Quotient = \\(3x - 4\\), Remainder = \\(4\\)", "Quotient = \\(3x + 4\\), Remainder = \\(-4\\)", "Quotient = \\(3x + 1\\), Remainder = \\(8\\)"], "Opposite of -3 is 3: 3, -5, -8 with 3 gives row 3, 4 and remainder -8 + 12 = 4"),
                ("(x^3 - 2x^2 + 3x - 4) \\div (x - 2)", "Quotient = \\(x^2 + 3\\), Remainder = \\(2\\)", ["Quotient = \\(x^2 - 3\\), Remainder = \\(2\\)", "Quotient = \\(x^2 + 2x + 3\\), Remainder = \\(2\\)", "Quotient = \\(x^2 + 3\\), Remainder = \\(-2\\)"], "Opposite of -2 is 2: 1, -2, 3, -4 with 2 gives row 1, 0, 3 and remainder -4 + 6 = 2"),
                ("(x^3 + 4x^2 - 5x + 6) \\div (x - 1)", "Quotient = \\(x^2 + 5x\\), Remainder = \\(6\\)", ["Quotient = \\(x^2 + 5x + 6\\), Remainder = \\(0\\)", "Quotient = \\(x^2 + 3x\\), Remainder = \\(6\\)", "Quotient = \\(x^2 - 5x\\), Remainder = \\(6\\)"], "Opposite of -1 is 1: 1, 4, -5, 6 with 1 gives row 1, 5, 0 and remainder 6"),
                ("(2x^3 - 7x^2 + 5x - 3) \\div (x - 3)", "Quotient = \\(2x^2 - x + 2\\), Remainder = \\(3\\)", ["Quotient = \\(2x^2 + x + 2\\), Remainder = \\(3\\)", "Quotient = \\(2x^2 - x - 2\\), Remainder = \\(3\\)", "Quotient = \\(2x^2 - x + 2\\), Remainder = \\(-3\\)"], "Opposite of -3 is 3: 2, -7, 5, -3 with 3 gives row 2, -1, 2 and remainder -3 + 6 = 3"),
                ("(x^2 - 5x + 6) \\div (x - 2)", "Quotient = \\(x - 3\\), Remainder = \\(0\\)", ["Quotient = \\(x + 3\\), Remainder = \\(0\\)", "Quotient = \\(x - 3\\), Remainder = \\(2\\)", "Quotient = \\(x - 2\\), Remainder = \\(0\\)"], "Opposite of -2 is 2: 1, -5, 6 with 2 gives row 1, -3 and remainder 6 - 6 = 0"),
                ("(x^2 - 9) \\div (x - 3)", "Quotient = \\(x + 3\\), Remainder = \\(0\\)", ["Quotient = \\(x - 3\\), Remainder = \\(0\\)", "Quotient = \\(x + 3\\), Remainder = \\(3\\)", "Quotient = \\(x\\), Remainder = \\(0\\)"], "Opposite of -3 is 3: 1, 0, -9 with 3 gives row 1, 3 and remainder -9 + 9 = 0"),
                ("(3x^3 - 4x^2 + x - 5) \\div (x - 1)", "Quotient = \\(3x^2 - x\\), Remainder = \\(-5\\)", ["Quotient = \\(3x^2 + x\\), Remainder = \\(-5\\)", "Quotient = \\(3x^2 - x - 5\\), Remainder = \\(0\\)", "Quotient = \\(3x^2 - x\\), Remainder = \\(5\\)"], "Opposite of -1 is 1: 3, -4, 1, -5 with 1 gives row 3, -1, 0 and remainder -5"),
                ("(x^3 - 8) \\div (x - 2)", "Quotient = \\(x^2 + 2x + 4\\), Remainder = \\(0\\)", ["Quotient = \\(x^2 - 2x + 4\\), Remainder = \\(0\\)", "Quotient = \\(x^2 + 4\\), Remainder = \\(0\\)", "Quotient = \\(x^2 + 2x - 4\\), Remainder = \\(0\\)"], "Opposite of -2 is 2: 1, 0, 0, -8 with 2 gives row 1, 2, 4 and remainder -8 + 8 = 0")
            ],
            'tmpls': [
                "Divide using synthetic division: \\({0}\\):",
                "Find the quotient and remainder of \\({0}\\) by synthetic division:",
                "Using synthetic division, evaluate \\({0}\\):",
                "Perform synthetic division for \\({0}\\):",
                "Calculate the quotient and remainder for \\({0}\\) using synthetic division:",
                "What are the quotient and remainder when dividing \\({0}\\) synthetically?",
                "Apply synthetic division algorithm to solve \\({0}\\):",
                "Determine the quotient and remainder: \\({0}\\):",
                "Solve by synthetic division: \\({0}\\):",
                "Compute quotient and remainder using synthetic method: \\({0}\\):"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Identify Divisor Opposite Number**\nFor divisor \\(x - a\\), use \\(+a\\).\n**Step 2: Set Up Synthetic Division Row**\nWrite the coefficients of the dividend in descending order.\n**Step 3: Execute Algorithm**\n{item[3]}.\n**Step 4: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 1: Division by (x + a) where a > 0 (opposite is -a)
        {
            'data': [
                ("(x^2 + 5x + 6) \\div (x + 2)", "Quotient = \\(x + 3\\), Remainder = \\(0\\)", ["Quotient = \\(x - 3\\), Remainder = \\(0\\)", "Quotient = \\(x + 3\\), Remainder = \\(2\\)", "Quotient = \\(x + 2\\), Remainder = \\(0\\)"], "Opposite of +2 is -2: 1, 5, 6 with -2 gives row 1, 3 and remainder 6 - 6 = 0"),
                ("(2x^2 + 7x + 5) \\div (x + 1)", "Quotient = \\(2x + 5\\), Remainder = \\(0\\)", ["Quotient = \\(2x - 5\\), Remainder = \\(0\\)", "Quotient = \\(2x + 5\\), Remainder = \\(1\\)", "Quotient = \\(2x + 3\\), Remainder = \\(2\\)"], "Opposite of +1 is -1: 2, 7, 5 with -1 gives row 2, 5 and remainder 5 - 5 = 0"),
                ("(3x^2 + 10x + 9) \\div (x + 2)", "Quotient = \\(3x + 4\\), Remainder = \\(1\\)", ["Quotient = \\(3x - 4\\), Remainder = \\(1\\)", "Quotient = \\(3x + 4\\), Remainder = \\(-1\\)", "Quotient = \\(3x + 2\\), Remainder = \\(5\\)"], "Opposite of +2 is -2: 3, 10, 9 with -2 gives row 3, 4 and remainder 9 - 8 = 1"),
                ("(x^3 + 3x^2 + 3x + 2) \\div (x + 1)", "Quotient = \\(x^2 + 2x + 1\\), Remainder = \\(1\\)", ["Quotient = \\(x^2 + 2x - 1\\), Remainder = \\(1\\)", "Quotient = \\(x^2 - 2x + 1\\), Remainder = \\(1\\)", "Quotient = \\(x^2 + 2x + 1\\), Remainder = \\(0\\)"], "Opposite of +1 is -1: 1, 3, 3, 2 with -1 gives row 1, 2, 1 and remainder 2 - 1 = 1"),
                ("(x^3 + 2x^2 - 5x - 6) \\div (x + 3)", "Quotient = \\(x^2 - x - 2\\), Remainder = \\(0\\)", ["Quotient = \\(x^2 + x - 2\\), Remainder = \\(0\\)", "Quotient = \\(x^2 - x + 2\\), Remainder = \\(0\\)", "Quotient = \\(x^2 - x - 2\\), Remainder = \\(3\\)"], "Opposite of +3 is -3: 1, 2, -5, -6 with -3 gives row 1, -1, -2 and remainder -6 + 6 = 0"),
                ("(2x^3 + 5x^2 - 4x - 7) \\div (x + 2)", "Quotient = \\(2x^2 + x - 6\\), Remainder = \\(5\\)", ["Quotient = \\(2x^2 - x - 6\\), Remainder = \\(5\\)", "Quotient = \\(2x^2 + x + 6\\), Remainder = \\(5\\)", "Quotient = \\(2x^2 + x - 6\\), Remainder = \\(-5\\)"], "Opposite of +2 is -2: 2, 5, -4, -7 with -2 gives row 2, 1, -6 and remainder -7 + 12 = 5"),
                ("(x^2 + 4x - 12) \\div (x + 6)", "Quotient = \\(x - 2\\), Remainder = \\(0\\)", ["Quotient = \\(x + 2\\), Remainder = \\(0\\)", "Quotient = \\(x - 2\\), Remainder = \\(6\\)", "Quotient = \\(x - 6\\), Remainder = \\(0\\)"], "Opposite of +6 is -6: 1, 4, -12 with -6 gives row 1, -2 and remainder -12 + 12 = 0"),
                ("(x^3 + 27) \\div (x + 3)", "Quotient = \\(x^2 - 3x + 9\\), Remainder = \\(0\\)", ["Quotient = \\(x^2 + 3x + 9\\), Remainder = \\(0\\)", "Quotient = \\(x^2 - 9\\), Remainder = \\(0\\)", "Quotient = \\(x^2 - 3x - 9\\), Remainder = \\(0\\)"], "Opposite of +3 is -3: 1, 0, 0, 27 with -3 gives row 1, -3, 9 and remainder 27 - 27 = 0"),
                ("(4x^2 + 13x + 10) \\div (x + 2)", "Quotient = \\(4x + 5\\), Remainder = \\(0\\)", ["Quotient = \\(4x - 5\\), Remainder = \\(0\\)", "Quotient = \\(4x + 5\\), Remainder = \\(2\\)", "Quotient = \\(4x + 3\\), Remainder = \\(4\\)"], "Opposite of +2 is -2: 4, 13, 10 with -2 gives row 4, 5 and remainder 10 - 10 = 0"),
                ("(x^3 - x^2 - 4x + 5) \\div (x + 1)", "Quotient = \\(x^2 - 2x - 2\\), Remainder = \\(7\\)", ["Quotient = \\(x^2 - 2x + 2\\), Remainder = \\(7\\)", "Quotient = \\(x^2 + 2x - 2\\), Remainder = \\(7\\)", "Quotient = \\(x^2 - 2x - 2\\), Remainder = \\(-7\\)"], "Opposite of +1 is -1: 1, -1, -4, 5 with -1 gives row 1, -2, -2 and remainder 5 + 2 = 7")
            ],
            'tmpls': [
                "Perform synthetic division: \\({0}\\):",
                "Find quotient and remainder for \\({0}\\) using synthetic division with opposite coefficient:",
                "Using synthetic division with negative divisor value, evaluate \\({0}\\):",
                "Divide \\({0}\\) by synthetic division:",
                "Determine the quotient and remainder: \\({0}\\):",
                "Apply the synthetic division method to solve \\({0}\\):",
                "What is the result of synthetic division: \\({0}\\)?",
                "Evaluate by synthetic division: \\({0}\\):",
                "Solve using synthetic algorithm: \\({0}\\):",
                "Compute quotient and remainder for \\({0}\\):"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Identify Divisor Opposite Number**\nFor divisor \\(x + a\\), use \\(-a\\).\n**Step 2: Set Up Synthetic Division Row**\nWrite the coefficients of the dividend.\n**Step 3: Execute Algorithm**\n{item[3]}.\n**Step 4: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Synthetic division with missing terms in dividend
        {
            'data': [
                ("(x^3 - 3x^2 + 4) \\div (x - 2)", "Quotient = \\(x^2 - x - 2\\), Remainder = \\(0\\)", ["Quotient = \\(x^2 - x + 2\\), Remainder = \\(0\\)", "Quotient = \\(x^2 + x - 2\\), Remainder = \\(0\\)", "Quotient = \\(x^2 - x\\), Remainder = \\(4\\)"], "Dividend has missing linear term: index form is x^3 - 3x^2 + 0x + 4. Coefficients: (1, -3, 0, 4) with 2 gives row 1, -1, -2 and remainder 4 - 4 = 0"),
                ("(2x^4 - 3x^2 + 5) \\div (x - 1)", "Quotient = \\(2x^3 + 2x^2 - x - 1\\), Remainder = \\(4\\)", ["Quotient = \\(2x^3 - x^2 + 4\\), Remainder = \\(4\\)", "Quotient = \\(2x^3 + 2x^2 - x\\), Remainder = \\(4\\)", "Quotient = \\(2x^3 - 2x^2 - x - 1\\), Remainder = \\(4\\)"], "Coefficients: (2, 0, -3, 0, 5) with 1 gives row 2, 2, -1, -1 and remainder 5 - 1 = 4"),
                ("(x^4 - 16) \\div (x - 2)", "Quotient = \\(x^3 + 2x^2 + 4x + 8\\), Remainder = \\(0\\)", ["Quotient = \\(x^3 - 2x^2 + 4x - 8\\), Remainder = \\(0\\)", "Quotient = \\(x^3 + 8\\), Remainder = \\(0\\)", "Quotient = \\(x^3 + 4x + 8\\), Remainder = \\(0\\)"], "Coefficients: (1, 0, 0, 0, -16) with 2 gives row 1, 2, 4, 8 and remainder 0"),
                ("(x^3 + 1) \\div (x + 1)", "Quotient = \\(x^2 - x + 1\\), Remainder = \\(0\\)", ["Quotient = \\(x^2 + x + 1\\), Remainder = \\(0\\)", "Quotient = \\(x^2 - 1\\), Remainder = \\(0\\)", "Quotient = \\(x^2 - x - 1\\), Remainder = \\(0\\)"], "Coefficients: (1, 0, 0, 1) with -1 gives row 1, -1, 1 and remainder 1 - 1 = 0"),
                ("(3x^3 - 4x + 2) \\div (x - 1)", "Quotient = \\(3x^2 + 3x - 1\\), Remainder = \\(1\\)", ["Quotient = \\(3x^2 - 3x - 1\\), Remainder = \\(1\\)", "Quotient = \\(3x^2 + 3x + 1\\), Remainder = \\(1\\)", "Quotient = \\(3x^2 - 1\\), Remainder = \\(1\\)"], "Coefficients: (3, 0, -4, 2) with 1 gives row 3, 3, -1 and remainder 2 - 1 = 1"),
                ("(x^4 - 5x^2 + 4) \\div (x + 2)", "Quotient = \\(x^3 - 2x^2 - x + 2\\), Remainder = \\(0\\)", ["Quotient = \\(x^3 + 2x^2 - x - 2\\), Remainder = \\(0\\)", "Quotient = \\(x^3 - 2x^2 + x + 2\\), Remainder = \\(0\\)", "Quotient = \\(x^3 - x + 2\\), Remainder = \\(0\\)"], "Coefficients: (1, 0, -5, 0, 4) with -2 gives row 1, -2, -1, 2 and remainder 4 - 4 = 0"),
                ("(4x^3 - 2x + 7) \\div (x + 1)", "Quotient = \\(4x^2 - 4x + 2\\), Remainder = \\(5\\)", ["Quotient = \\(4x^2 + 4x + 2\\), Remainder = \\(5\\)", "Quotient = \\(4x^2 - 4x - 2\\), Remainder = \\(5\\)", "Quotient = \\(4x^2 + 2\\), Remainder = \\(5\\)"], "Coefficients: (4, 0, -2, 7) with -1 gives row 4, -4, 2 and remainder 7 - 2 = 5"),
                ("(x^3 - 27) \\div (x - 3)", "Quotient = \\(x^2 + 3x + 9\\), Remainder = \\(0\\)", ["Quotient = \\(x^2 - 3x + 9\\), Remainder = \\(0\\)", "Quotient = \\(x^2 + 9\\), Remainder = \\(0\\)", "Quotient = \\(x^2 + 3x - 9\\), Remainder = \\(0\\)"], "Coefficients: (1, 0, 0, -27) with 3 gives row 1, 3, 9 and remainder -27 + 27 = 0"),
                ("(2x^3 - 8x + 3) \\div (x - 2)", "Quotient = \\(2x^2 + 4x\\), Remainder = \\(3\\)", ["Quotient = \\(2x^2 - 4x\\), Remainder = \\(3\\)", "Quotient = \\(2x^2 + 4x + 3\\), Remainder = \\(0\\)", "Quotient = \\(2x^2 + 4x\\), Remainder = \\(-3\\)"], "Coefficients: (2, 0, -8, 3) with 2 gives row 2, 4, 0 and remainder 3"),
                ("(x^4 + 2x^2 - 3) \\div (x - 1)", "Quotient = \\(x^3 + x^2 + 3x + 3\\), Remainder = \\(0\\)", ["Quotient = \\(x^3 - x^2 + 3x - 3\\), Remainder = \\(0\\)", "Quotient = \\(x^3 + 3x\\), Remainder = \\(0\\)", "Quotient = \\(x^3 + x^2 - 3x + 3\\), Remainder = \\(0\\)"], "Coefficients: (1, 0, 2, 0, -3) with 1 gives row 1, 1, 3, 3 and remainder -3 + 3 = 0")
            ],
            'tmpls': [
                "Divide \\({0}\\) by synthetic division (ensure to account for missing terms):",
                "Find quotient and remainder for \\({0}\\) with missing powers:",
                "Using synthetic division, evaluate \\({0}\\) inserting zero coefficients for missing terms:",
                "Perform synthetic division on \\({0}\\):",
                "Calculate quotient and remainder of \\({0}\\) using synthetic algorithm:",
                "What is the result when \\({0}\\) is divided synthetically?",
                "Apply synthetic division to \\({0}\\):",
                "Determine the quotient and remainder: \\({0}\\):",
                "Solve \\({0}\\) by synthetic method:",
                "Compute quotient and remainder for \\({0}\\) carefully inserting 0 for absent powers:"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Write Dividend in Index Form**\n{item[3]}.\n**Step 2: Apply Synthetic Division**\nCarry down the first coefficient, multiply by divisor opposite number, and add vertically.\n**Step 3: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Conceptual synthetic division table interpretation
        {
            'data': [
                ("In synthetic division by \\(x - 4\\), what number is placed in the divisor box on the left?", "+4 (the opposite of -4)", ["-4", "0", "1"]),
                ("In synthetic division by \\(x + 5\\), what number is placed on the left?", "-5 (the opposite of +5)", ["+5", "0", "-1"]),
                ("If the bottom row of synthetic division shows 2, 3, -1 | 7, what is the quotient polynomial?", "\\(2x^2 + 3x - 1\\)", ["\\(2x^3 + 3x^2 - x\\)", "\\(2x^2 + 3x + 7\\)", "\\(2x - 1\\)"]),
                ("If the bottom row of synthetic division shows 1, 0, -4 | 0, what is the quotient?", "\\(x^2 - 4\\)", ["\\(x^3 - 4\\)", "\\(x^2 + 4\\)", "\\(x - 4\\)"]),
                ("In the bottom row of a synthetic division tableau, what does the very last number represent?", "The remainder R", ["The degree of the quotient", "The leading coefficient", "The constant term of quotient"]),
                ("If the remainder obtained in synthetic division of \\(P(x)\\) by \\(x - a\\) is 0, what does it mean?", "\\(x - a\\) is a factor of \\(P(x)\\)", ["\\(x - a\\) is not a factor", "\\(P(x) = 0\\)", "The degree of P(x) is 0"]),
                ("Can synthetic division be directly applied to a quadratic divisor like \\(x^2 + 2x + 1\\)?", "No, standard synthetic division requires a linear divisor of the form \\(x - a\\)", ["Yes, without any modification", "Yes, by adding coefficients", "Only if the dividend is cubic"]),
                ("If the dividend has degree 3, what is the degree of the quotient polynomial obtained via synthetic division by a linear divisor?", "2 (since \\(3 - 1 = 2\\))", ["3", "1", "0"]),
                ("If the synthetic row coefficients are (3, -2) and remainder is 5, write the quotient:", "\\(3x - 2\\)", ["\\(3x^2 - 2x\\)", "\\(3x + 2\\)", "\\(3x^2 - 2x + 5\\)"]),
                ("In synthetic division, what operation is performed between the column entries vertically?", "Addition (adding the numbers vertically)", ["Subtraction", "Multiplication", "Division"])
            ],
            'tmpls': [
                "{0}",
                "Answer the synthetic division concept question: {0}",
                "Select the correct statement: {0}",
                "Evaluate the synthetic division tableau property: {0}",
                "Determine the true conclusion: {0}",
                "Choose the right answer: {0}",
                "Interpret the synthetic division component: {0}",
                "State the correct rule: {0}",
                "Which option correctly answers: {0}",
                "Analyze the synthetic division step: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Understand Synthetic Division Rules**\nDivisor \\(x - a\\) uses \\(+a\\).\nNumbers in columns are added vertically.\nThe last entry is the remainder.\nThe preceding entries form the quotient polynomial of degree \\(n - 1\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 4: Division when divisor is mx - a (leading coefficient > 1)
        {
            'data': [
                ("(2x^2 + 3x + 1) \\div (2x - 1)", "Quotient = \\(x + 2\\), Remainder = \\(3\\)", ["Quotient = \\(2x + 4\\), Remainder = \\(3\\)", "Quotient = \\(x - 2\\), Remainder = \\(3\\)", "Quotient = \\(x + 2\\), Remainder = \\(0\\)"], "Divide by (x - 1/2) first: synthetic gives (2, 4) with R = 3. Dividing quotient by 2 gives x + 2"),
                ("(2x^2 - 7x - 4) \\div (2x + 1)", "Quotient = \\(x - 4\\), Remainder = \\(0\\)", ["Quotient = \\(2x - 8\\), Remainder = \\(0\\)", "Quotient = \\(x + 4\\), Remainder = \\(0\\)", "Quotient = \\(x - 4\\), Remainder = \\(1\\)"], "Divide by (x + 1/2): quotient (2, -8) / 2 = x - 4, R = 0"),
                ("(3x^2 + 5x - 2) \\div (3x - 1)", "Quotient = \\(x + 2\\), Remainder = \\(0\\)", ["Quotient = \\(3x + 6\\), Remainder = \\(0\\)", "Quotient = \\(x - 2\\), Remainder = \\(0\\)", "Quotient = \\(x + 2\\), Remainder = \\(1\\)"], "Divide by (x - 1/3): quotient (3, 6) / 3 = x + 2, R = 0"),
                ("(4x^2 - 4x + 3) \\div (2x - 1)", "Quotient = \\(2x - 1\\), Remainder = \\(2\\)", ["Quotient = \\(4x - 2\\), Remainder = \\(2\\)", "Quotient = \\(2x + 1\\), Remainder = \\(2\\)", "Quotient = \\(2x - 1\\), Remainder = \\(0\\)"], "Divide by (x - 1/2): quotient (4, -2) / 2 = 2x - 1, R = 2"),
                ("(3x^3 + x^2 - 20x + 12) \\div (3x - 2)", "Quotient = \\(x^2 + x - 6\\), Remainder = \\(0\\)", ["Quotient = \\(3x^2 + 3x - 18\\), Remainder = \\(0\\)", "Quotient = \\(x^2 - x - 6\\), Remainder = \\(0\\)", "Quotient = \\(x^2 + x + 6\\), Remainder = \\(0\\)"], "Divide by (x - 2/3): quotient (3, 3, -18) / 3 = x^2 + x - 6, R = 0"),
                ("(2x^3 - 5x^2 + 6x - 2) \\div (2x - 1)", "Quotient = \\(x^2 - 2x + 2\\), Remainder = \\(0\\)", ["Quotient = \\(2x^2 - 4x + 4\\), Remainder = \\(0\\)", "Quotient = \\(x^2 + 2x + 2\\), Remainder = \\(0\\)", "Quotient = \\(x^2 - 2x - 2\\), Remainder = \\(0\\)"], "Divide by (x - 1/2): quotient (2, -4, 4) / 2 = x^2 - 2x + 2, R = 0"),
                ("(6x^2 + 11x - 7) \\div (2x + 3)", "Quotient = \\(3x + 1\\), Remainder = \\(-10\\)", ["Quotient = \\(6x + 2\\), Remainder = \\(-10\\)", "Quotient = \\(3x - 1\\), Remainder = \\(-10\\)", "Quotient = \\(3x + 1\\), Remainder = \\(10\\)"], "Divide by (x + 3/2): quotient (6, 2) / 2 = 3x + 1, R = -10"),
                ("(4x^3 - 8x^2 + 3x + 1) \\div (2x - 1)", "Quotient = \\(2x^2 - 3x\\), Remainder = \\(1\\)", ["Quotient = \\(4x^2 - 6x\\), Remainder = \\(1\\)", "Quotient = \\(2x^2 + 3x\\), Remainder = \\(1\\)", "Quotient = \\(2x^2 - 3x + 1\\), Remainder = \\(0\\)"], "Divide by (x - 1/2): quotient (4, -6, 0) / 2 = 2x^2 - 3x, R = 1"),
                ("(3x^2 + 7x + 5) \\div (3x + 1)", "Quotient = \\(x + 2\\), Remainder = \\(3\\)", ["Quotient = \\(3x + 6\\), Remainder = \\(3\\)", "Quotient = \\(x - 2\\), Remainder = \\(3\\)", "Quotient = \\(x + 2\\), Remainder = \\(-3\\)"], "Divide by (x + 1/3): quotient (3, 6) / 3 = x + 2, R = 3"),
                ("(2x^3 + 3x^2 - 1) \\div (2x + 1)", "Quotient = \\(x^2 + x\\), Remainder = \\(-1\\)", ["Quotient = \\(2x^2 + 2x\\), Remainder = \\(-1\\)", "Quotient = \\(x^2 - x\\), Remainder = \\(-1\\)", "Quotient = \\(x^2 + x - 1\\), Remainder = \\(0\\)"], "Divide by (x + 1/2): quotient (2, 2, 0) / 2 = x^2 + x, R = -1")
            ],
            'tmpls': [
                "Find quotient and remainder for \\({0}\\) by synthetic division:",
                "Divide using synthetic division: \\({0}\\):",
                "Evaluate \\({0}\\) using synthetic division with non-monic linear divisor:",
                "Perform synthetic division for \\({0}\\) remembering to divide quotient coefficients by the leading coefficient of divisor:",
                "Calculate quotient and remainder of \\({0}\\):",
                "What are quotient and remainder when \\({0}\\) is divided synthetically?",
                "Apply synthetic method to \\({0}\\):",
                "Determine the true quotient and remainder for \\({0}\\):",
                "Solve \\({0}\\) via synthetic division:",
                "Compute the quotient and remainder: \\({0}\\):"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Divide by Equivalent Monic Linear Factor**\nFor divisor \\(mx - a = m(x - a/m)\\), divide synthetically by \\(x - a/m\\).\n**Step 2: Rescale the Quotient**\n{item[3]}.\n**Step 3: Conclusion**\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 5: Finding unknown parameter k given remainder
        {
            'data': [
                ("(x^2 + kx + 8) \\div (x - 2)", "k = -3 (since \\(R = 2^2 + 2k + 8 = 12 + 2k = 6 \\implies 2k = -6 \\implies k = -3\\))", "6", ["k = 3", "k = -2", "k = 1"]),
                ("(2x^2 - kx + 5) \\div (x - 1)", "k = 4 (since \\(R = 2(1)^2 - k(1) + 5 = 7 - k = 3 \\implies k = 4\\))", "3", ["k = -4", "k = 2", "k = -2"]),
                ("(x^3 - 3x^2 + kx - 4) \\div (x - 2)", "k = 5 (since \\(R = 8 - 12 + 2k - 4 = 2k - 8 = 2 \\implies 2k = 10 \\implies k = 5\\))", "2", ["k = -5", "k = 3", "k = 4"]),
                ("(x^2 + 4x + k) \\div (x + 1)", "k = 7 (since \\(R = (-1)^2 + 4(-1) + k = 1 - 4 + k = k - 3 = 4 \\implies k = 7\\))", "4", ["k = -7", "k = 1", "k = -1"]),
                ("(kx^2 - 5x + 6) \\div (x - 2)", "k = 3 (since \\(R = 4k - 10 + 6 = 4k - 4 = 8 \\implies 4k = 12 \\implies k = 3\\))", "8", ["k = -3", "k = 2", "k = 4"]),
                ("(x^3 + kx^2 - x + 2) \\div (x + 2)", "k = 2 (since \\(R = -8 + 4k + 2 + 2 = 4k - 4 = 4 \\implies 4k = 8 \\implies k = 2\\))", "4", ["k = -2", "k = 1", "k = 3"]),
                ("(3x^2 + kx - 10) \\div (x - 3)", "k = -5 (since \\(R = 27 + 3k - 10 = 17 + 3k = 2 \\implies 3k = -15 \\implies k = -5\\))", "2", ["k = 5", "k = -3", "k = 1"]),
                ("(x^2 - kx + 12) \\div (x - 4)", "k = 7 (if \\(x - 4\\) is a factor, \\(R = 16 - 4k + 12 = 28 - 4k = 0 \\implies k = 7\\))", "0", ["k = -7", "k = 4", "k = 6"]),
                ("(2x^2 + 5x + k) \\div (x + 3)", "k = 3 (if \\(x + 3\\) divides it with remainder 6: \\(18 - 15 + k = 3 + k = 6 \\implies k = 3\\))", "6", ["k = -3", "k = 0", "k = 6"]),
                ("(x^3 - kx + 6) \\div (x - 1)", "k = 7 (if remainder is 0: \\(1 - k + 6 = 7 - k = 0 \\implies k = 7\\))", "0", ["k = -7", "k = 1", "k = 5"])
            ],
            'tmpls': [
                "In synthetic division of \\({0}\\), the remainder is {2}. Find the value of k:",
                "If the remainder is {2} when \\({0}\\) is divided, determine k:",
                "Find k such that synthetic division of \\({0}\\) yields a remainder of {2}:",
                "Evaluate k given that dividing \\({0}\\) results in remainder {2}:",
                "What is the value of k if \\({0}\\) leaves remainder {2}?",
                "Calculate k when \\({0}\\) has remainder {2}:",
                "Determine k from the division \\({0}\\) having remainder {2}:",
                "Given that \\({0}\\) produces remainder {2}, find k:",
                "Compute the parameter k when dividing \\({0}\\) gives remainder {2}:",
                "Solve for k if the synthetic remainder of \\({0}\\) equals {2}:"
            ],
            'calc': lambda item: (
                item[1],
                item[3],
                f"**Step 1: Set Up Remainder Formula**\nBy synthetic division / remainder theorem, \\(R = P(a)\\).\n**Step 2: Solve the Linear Equation in k**\n{item[1]}.\n**Step 3: Conclusion**\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 6: Verification Dividend = Divisor * Quotient + Remainder
        {
            'data': [
                ("If \\(P(x) = (x - 2)(x^2 + 3) + 5\\), what is the dividend polynomial?", "\\(x^3 - 2x^2 + 3x - 1\\)", ["\\(x^3 - 2x^2 + 3x + 1\\)", "\\(x^3 - 2x^2 + 3x + 5\\)", "\\(x^3 + 3x + 5\\)"]),
                ("If divisor is \\(x + 1\\), quotient is \\(2x + 3\\), and remainder is 4, find the dividend:", "\\((x + 1)(2x + 3) + 4 = 2x^2 + 5x + 3 + 4 = 2x^2 + 5x + 7\\)", ["\\(2x^2 + 5x + 3\\)", "\\(2x^2 + 5x - 7\\)", "\\(2x^2 + 3x + 7\\)"]),
                ("If divisor is \\(x - 3\\), quotient is \\(x^2 - x + 2\\), and remainder is 0, find the dividend:", "\\((x - 3)(x^2 - x + 2) = x^3 - 4x^2 + 5x - 6\\)", ["\\(x^3 - 4x^2 + 5x + 6\\)", "\\(x^3 - x^2 + 2x - 6\\)", "\\(x^3 + 4x^2 - 5x - 6\\)"]),
                ("If divisor is \\(x + 2\\), quotient is \\(3x - 4\\), and remainder is -1, find the dividend:", "\\((x + 2)(3x - 4) - 1 = 3x^2 + 2x - 8 - 1 = 3x^2 + 2x - 9\\)", ["\\(3x^2 + 2x - 8\\)", "\\(3x^2 - 2x - 9\\)", "\\(3x^2 + 2x + 9\\)"]),
                ("What is the fundamental Division Algorithm identity for polynomials?", "\\(\\text{Dividend} = \\text{Divisor} \\times \\text{Quotient} + \\text{Remainder}\\)", ["\\(\\text{Dividend} = \\text{Divisor} + \\text{Quotient} \\times \\text{Remainder}\\)", "\\(\\text{Dividend} = \\text{Divisor} \\times \\text{Remainder} + \\text{Quotient}\\)", "\\(\\text{Dividend} = \\frac{\\text{Divisor}}{\\text{Quotient}} + \\text{Remainder}\\)"]),
                ("If degree of divisor is 1, what must be the degree of the remainder R?", "0 (a constant number) or R is 0", ["1", "2", "Equal to dividend degree"]),
                ("If \\(P(x) = (x - 1)(x^2 + x + 1) + 0\\), what is \\(P(x)\\)?", "\\(x^3 - 1\\)", ["\\(x^3 + 1\\)", "\\(x^2 - 1\\)", "\\(x^3 - x - 1\\)"]),
                ("If \\(P(x) = (x + 3)(x - 3) + 7\\), what is \\(P(x)\\)?", "\\(x^2 - 9 + 7 = x^2 - 2\\)", ["\\(x^2 - 9\\)", "\\(x^2 + 2\\)", "\\(x^2 - 16\\)"]),
                ("If \\(P(x) = (x - 4)(2x + 1) + 3\\), what is \\(P(x)\\)?", "\\(2x^2 - 7x - 4 + 3 = 2x^2 - 7x - 1\\)", ["\\(2x^2 - 7x - 4\\)", "\\(2x^2 - 7x + 1\\)", "\\(2x^2 + 7x - 1\\)"]),
                ("Can the remainder in polynomial division have degree greater than or equal to the divisor?", "No, \\(\\deg(\\text{Remainder}) < \\deg(\\text{Divisor})\\) strictly", ["Yes, if dividend degree is large", "Yes, when dividing by quadratic", "Only if divisor is linear"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate using the division algorithm: {0}",
                "Calculate the polynomial: {0}",
                "Determine the dividend expression: {0}",
                "State the result from the division relationship: {0}",
                "Select the correct polynomial: {0}",
                "Find the dividend: {0}",
                "Compute the dividend: {0}",
                "Identify the correct identity: {0}",
                "Which option correctly answers: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Apply Division Algorithm**\n\\(P(x) = D(x) \\cdot Q(x) + R\\).\n**Step 2: Expand and Simplify**\nMultiply divisor by quotient and add the remainder.\n**Step 3: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Advantages and Constraints of Synthetic Division
        {
            'data': [
                ("Why is synthetic division preferred over long polynomial division for linear divisors?", "It uses only numerical coefficients, eliminating repeated variable writing and reducing errors", ["It works for all non-linear divisors directly", "It does not require calculating remainders", "It can divide polynomials of two variables"]),
                ("What is the primary limitation of standard synthetic division?", "The divisor must be of linear form \\(x - a\\) (degree 1)", ["It cannot divide cubics", "It cannot find remainders", "It fails when coefficients are negative"]),
                ("What must be done to dividend coefficients before running synthetic division?", "Missing powers must be written with 0 coefficients in standard descending order", ["Only non-zero terms are written", "Coefficients are reversed", "Signs of dividend must all be changed"]),
                ("If the synthetic quotient row is (1, 2, 3), how many terms are in the quotient?", "3 terms (representing a quadratic \\(x^2 + 2x + 3\\))", ["4 terms", "2 terms", "1 term"]),
                ("In synthetic division by \\(x - a\\), how is the remainder related to \\(P(a)\\)?", "\\(R = P(a)\\) exactly", ["\\(R = -P(a)\\)", "\\(R = P(-a)\\)", "\\(R = a \\cdot P(a)\\)"]),
                ("If synthetic division produces remainder 0, what does it prove?", "The divisor is an exact factor of the dividend", ["The dividend is zero", "The quotient is zero", "The divisor has degree 0"]),
                ("If \\(P(x)\\) has degree 5, what is the degree of the quotient after synthetic division by \\(x - 2\\)?", "4", ["5", "3", "2"]),
                ("When divisor is \\(x + 7\\), what value is placed outside the division bracket?", "-7", ["+7", "0", "1"]),
                ("Can synthetic division be used when the dividend has fractional coefficients?", "Yes, fractional coefficients follow the same multiplication and addition steps", ["No, only integers are allowed", "No, fractions produce incorrect remainders", "Only if denominator is 2"]),
                ("Who invented synthetic division method for polynomial evaluation?", "Paolo Ruffini (known as Ruffini's rule in many curricula)", ["René Descartes", "Isaac Newton", "Carl Friedrich Gauss"])
            ],
            'tmpls': [
                "{0}",
                "Answer the following conceptual question: {0}",
                "Select the correct synthetic division fact: {0}",
                "Evaluate the statement: {0}",
                "Determine the true mathematical property: {0}",
                "Choose the right answer: {0}",
                "Analyze the synthetic division rule: {0}",
                "State the correct concept: {0}",
                "Which option correctly answers: {0}",
                "Identify the true reason: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Understand Synthetic Division Constraints & Concepts**\nRequires a linear divisor \\(x - a\\).\nIndex form with zero coefficients is mandatory.\nRemainder equals \\(P(a)\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_3_3_2():
    tc = "MH-9-MTH1-3-3.3.2"
    tname = "Linear division method"
    
    archs = [
        # Arch 0: Linear division of quadratic by (x - a)
        {
            'data': [
                ("(x^2 + 3x + 2) \\div (x - 1)", "Quotient = \\(x + 4\\), Remainder = \\(6\\)", ["Quotient = \\(x - 4\\), Remainder = \\(6\\)", "Quotient = \\(x + 4\\), Remainder = \\(0\\)", "Quotient = \\(x + 2\\), Remainder = \\(4\\)"], "Rewrite: x(x - 1) + x + 3x + 2 = x(x - 1) + 4x + 2 = x(x - 1) + 4(x - 1) + 4 + 2 = (x + 4)(x - 1) + 6"),
                ("(2x^2 - 5x + 3) \\div (x - 2)", "Quotient = \\(2x - 1\\), Remainder = \\(1\\)", ["Quotient = \\(2x + 1\\), Remainder = \\(1\\)", "Quotient = \\(2x - 1\\), Remainder = \\(-1\\)", "Quotient = \\(2x - 3\\), Remainder = \\(3\\)"], "2x(x - 2) + 4x - 5x + 3 = 2x(x - 2) - x + 3 = 2x(x - 2) - 1(x - 2) - 2 + 3 = (2x - 1)(x - 2) + 1"),
                ("(3x^2 + 2x - 8) \\div (x - 1)", "Quotient = \\(3x + 5\\), Remainder = \\(-3\\)", ["Quotient = \\(3x - 5\\), Remainder = \\(-3\\)", "Quotient = \\(3x + 5\\), Remainder = \\(3\\)", "Quotient = \\(3x + 2\\), Remainder = \\(-8\\)"], "3x(x - 1) + 3x + 2x - 8 = 3x(x - 1) + 5(x - 1) + 5 - 8 = (3x + 5)(x - 1) - 3"),
                ("(x^2 - 7x + 10) \\div (x - 5)", "Quotient = \\(x - 2\\), Remainder = \\(0\\)", ["Quotient = \\(x + 2\\), Remainder = \\(0\\)", "Quotient = \\(x - 2\\), Remainder = \\(5\\)", "Quotient = \\(x - 5\\), Remainder = \\(0\\)"], "x(x - 5) + 5x - 7x + 10 = x(x - 5) - 2(x - 5) - 10 + 10 = (x - 2)(x - 5) + 0"),
                ("(4x^2 - 3x + 1) \\div (x - 1)", "Quotient = \\(4x + 1\\), Remainder = \\(2\\)", ["Quotient = \\(4x - 1\\), Remainder = \\(2\\)", "Quotient = \\(4x + 1\\), Remainder = \\(0\\)", "Quotient = \\(4x + 2\\), Remainder = \\(1\\)"], "4x(x - 1) + 4x - 3x + 1 = 4x(x - 1) + (x - 1) + 1 + 1 = (4x + 1)(x - 1) + 2"),
                ("(2x^2 + x - 6) \\div (x - 2)", "Quotient = \\(2x + 5\\), Remainder = \\(4\\)", ["Quotient = \\(2x - 5\\), Remainder = \\(4\\)", "Quotient = \\(2x + 5\\), Remainder = \\(0\\)", "Quotient = \\(2x + 3\\), Remainder = \\(2\\)"], "2x(x - 2) + 4x + x - 6 = 2x(x - 2) + 5(x - 2) + 10 - 6 = (2x + 5)(x - 2) + 4"),
                ("(x^2 - 4) \\div (x - 2)", "Quotient = \\(x + 2\\), Remainder = \\(0\\)", ["Quotient = \\(x - 2\\), Remainder = \\(0\\)", "Quotient = \\(x + 2\\), Remainder = \\(2\\)", "Quotient = \\(x\\), Remainder = \\(0\\)"], "x(x - 2) + 2x - 4 = x(x - 2) + 2(x - 2) = (x + 2)(x - 2) + 0"),
                ("(3x^2 - 10x + 7) \\div (x - 3)", "Quotient = \\(3x - 1\\), Remainder = \\(4\\)", ["Quotient = \\(3x + 1\\), Remainder = \\(4\\)", "Quotient = \\(3x - 1\\), Remainder = \\(-4\\)", "Quotient = \\(3x - 3\\), Remainder = \\(1\\)"], "3x(x - 3) + 9x - 10x + 7 = 3x(x - 3) - (x - 3) - 3 + 7 = (3x - 1)(x - 3) + 4"),
                ("(x^2 + 6x + 5) \\div (x - 1)", "Quotient = \\(x + 7\\), Remainder = \\(12\\)", ["Quotient = \\(x - 7\\), Remainder = \\(12\\)", "Quotient = \\(x + 7\\), Remainder = \\(0\\)", "Quotient = \\(x + 5\\), Remainder = \\(6\\)"], "x(x - 1) + x + 6x + 5 = x(x - 1) + 7(x - 1) + 7 + 5 = (x + 7)(x - 1) + 12"),
                ("(5x^2 - 4x + 2) \\div (x - 1)", "Quotient = \\(5x + 1\\), Remainder = \\(3\\)", ["Quotient = \\(5x - 1\\), Remainder = \\(3\\)", "Quotient = \\(5x + 1\\), Remainder = \\(0\\)", "Quotient = \\(5x + 2\\), Remainder = \\(1\\)"], "5x(x - 1) + 5x - 4x + 2 = 5x(x - 1) + (x - 1) + 1 + 2 = (5x + 1)(x - 1) + 3")
            ],
            'tmpls': [
                "Divide using the linear method: \\({0}\\):",
                "Find quotient and remainder for \\({0}\\) by linear method of division:",
                "Using linear method of division, evaluate \\({0}\\):",
                "Perform linear division on \\({0}\\):",
                "Calculate quotient and remainder of \\({0}\\) via linear method:",
                "What are quotient and remainder when \\({0}\\) is divided by linear method?",
                "Apply linear division steps to solve \\({0}\\):",
                "Determine quotient and remainder using linear method: \\({0}\\):",
                "Solve by linear division: \\({0}\\):",
                "Compute quotient and remainder for \\({0}\\) through linear rearrangement:"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Express Highest Degree Term in terms of Divisor**\n{item[3]}.\n**Step 2: Collect Common Linear Factor**\nFactor out the linear divisor from grouped terms.\n**Step 3: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 1: Linear division of cubic by (x - a)
        {
            'data': [
                ("(x^3 - 2x^2 + 3x - 5) \\div (x - 2)", "Quotient = \\(x^2 + 3\\), Remainder = \\(1\\)", ["Quotient = \\(x^2 - 3\\), Remainder = \\(1\\)", "Quotient = \\(x^2 + 2x + 3\\), Remainder = \\(1\\)", "Quotient = \\(x^2 + 3\\), Remainder = \\(-1\\)"], "x^2(x - 2) + 2x^2 - 2x^2 + 3x - 5 = x^2(x - 2) + 3(x - 2) + 6 - 5 = (x^2 + 3)(x - 2) + 1"),
                ("(2x^3 - 3x^2 + 4x - 1) \\div (x - 1)", "Quotient = \\(2x^2 - x + 3\\), Remainder = \\(2\\)", ["Quotient = \\(2x^2 + x + 3\\), Remainder = \\(2\\)", "Quotient = \\(2x^2 - x - 3\\), Remainder = \\(2\\)", "Quotient = \\(2x^2 - x + 3\\), Remainder = \\(-2\\)"], "2x^2(x - 1) - x(x - 1) + 3(x - 1) + 2 = (2x^2 - x + 3)(x - 1) + 2"),
                ("(x^3 + 4x^2 - x - 4) \\div (x - 1)", "Quotient = \\(x^2 + 5x + 4\\), Remainder = \\(0\\)", ["Quotient = \\(x^2 - 5x + 4\\), Remainder = \\(0\\)", "Quotient = \\(x^2 + 5x - 4\\), Remainder = \\(0\\)", "Quotient = \\(x^2 + 4\\), Remainder = \\(0\\)"], "x^2(x - 1) + 5x(x - 1) + 4(x - 1) = (x^2 + 5x + 4)(x - 1) + 0"),
                ("(x^3 - 6x^2 + 11x - 6) \\div (x - 2)", "Quotient = \\(x^2 - 4x + 3\\), Remainder = \\(0\\)", ["Quotient = \\(x^2 + 4x + 3\\), Remainder = \\(0\\)", "Quotient = \\(x^2 - 4x - 3\\), Remainder = \\(0\\)", "Quotient = \\(x^2 - 3\\), Remainder = \\(0\\)"], "x^2(x - 2) - 4x(x - 2) + 3(x - 2) = (x^2 - 4x + 3)(x - 2) + 0"),
                ("(3x^3 - 5x^2 + 2x - 7) \\div (x - 2)", "Quotient = \\(3x^2 + x + 4\\), Remainder = \\(1\\)", ["Quotient = \\(3x^2 - x + 4\\), Remainder = \\(1\\)", "Quotient = \\(3x^2 + x - 4\\), Remainder = \\(1\\)", "Quotient = \\(3x^2 + x + 4\\), Remainder = \\(-1\\)"], "3x^2(x - 2) + x(x - 2) + 4(x - 2) + 1 = (3x^2 + x + 4)(x - 2) + 1"),
                ("(x^3 - 8) \\div (x - 2)", "Quotient = \\(x^2 + 2x + 4\\), Remainder = \\(0\\)", ["Quotient = \\(x^2 - 2x + 4\\), Remainder = \\(0\\)", "Quotient = \\(x^2 + 4\\), Remainder = \\(0\\)", "Quotient = \\(x^2 + 2x - 4\\), Remainder = \\(0\\)"], "x^2(x - 2) + 2x(x - 2) + 4(x - 2) = (x^2 + 2x + 4)(x - 2) + 0"),
                ("(2x^3 + x^2 - 5x + 2) \\div (x - 1)", "Quotient = \\(2x^2 + 3x - 2\\), Remainder = \\(0\\)", ["Quotient = \\(2x^2 - 3x - 2\\), Remainder = \\(0\\)", "Quotient = \\(2x^2 + 3x + 2\\), Remainder = \\(0\\)", "Quotient = \\(2x^2 - 2\\), Remainder = \\(0\\)"], "2x^2(x - 1) + 3x(x - 1) - 2(x - 1) = (2x^2 + 3x - 2)(x - 1) + 0"),
                ("(x^3 + 2x^2 - 3x + 4) \\div (x - 1)", "Quotient = \\(x^2 + 3x\\), Remainder = \\(4\\)", ["Quotient = \\(x^2 - 3x\\), Remainder = \\(4\\)", "Quotient = \\(x^2 + 3x + 4\\), Remainder = \\(0\\)", "Quotient = \\(x^2 + 3x\\), Remainder = \\(-4\\)"], "x^2(x - 1) + 3x(x - 1) + 4 = (x^2 + 3x)(x - 1) + 4"),
                ("(x^3 - 4x^2 + 5x - 2) \\div (x - 1)", "Quotient = \\(x^2 - 3x + 2\\), Remainder = \\(0\\)", ["Quotient = \\(x^2 + 3x + 2\\), Remainder = \\(0\\)", "Quotient = \\(x^2 - 3x - 2\\), Remainder = \\(0\\)", "Quotient = \\(x^2 + 2\\), Remainder = \\(0\\)"], "x^2(x - 1) - 3x(x - 1) + 2(x - 1) = (x^2 - 3x + 2)(x - 1) + 0"),
                ("(4x^3 - 6x^2 + 2x - 3) \\div (x - 2)", "Quotient = \\(4x^2 + 2x + 6\\), Remainder = \\(9\\)", ["Quotient = \\(4x^2 - 2x + 6\\), Remainder = \\(9\\)", "Quotient = \\(4x^2 + 2x - 6\\), Remainder = \\(9\\)", "Quotient = \\(4x^2 + 2x + 6\\), Remainder = \\(-9\\)"], "4x^2(x - 2) + 2x(x - 2) + 6(x - 2) + 9 = (4x^2 + 2x + 6)(x - 2) + 9")
            ],
            'tmpls': [
                "Divide cubic polynomial by linear method: \\({0}\\):",
                "Find quotient and remainder for \\({0}\\) using linear method:",
                "Using the linear division method, calculate \\({0}\\):",
                "Perform linear division on cubic \\({0}\\):",
                "Evaluate \\({0}\\) by linear method:",
                "What is the result of dividing \\({0}\\) by linear method?",
                "Apply successive grouping with linear divisor to solve \\({0}\\):",
                "Determine the quotient and remainder: \\({0}\\):",
                "Solve via linear division: \\({0}\\):",
                "Compute quotient and remainder for \\({0}\\) using linear division steps:"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Successive Factor Rearrangement**\n{item[3]}.\n**Step 2: Collect Quotient Polynomial**\nFactor out \\(x - a\\) from the grouped cubic terms.\n**Step 3: Conclusion**\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 2: Linear division by (x + a)
        {
            'data': [
                ("(x^2 + 5x + 8) \\div (x + 2)", "Quotient = \\(x + 3\\), Remainder = \\(2\\)", ["Quotient = \\(x - 3\\), Remainder = \\(2\\)", "Quotient = \\(x + 3\\), Remainder = \\(-2\\)", "Quotient = \\(x + 2\\), Remainder = \\(4\\)"], "x(x + 2) - 2x + 5x + 8 = x(x + 2) + 3(x + 2) - 6 + 8 = (x + 3)(x + 2) + 2"),
                ("(2x^2 + 7x + 6) \\div (x + 2)", "Quotient = \\(2x + 3\\), Remainder = \\(0\\)", ["Quotient = \\(2x - 3\\), Remainder = \\(0\\)", "Quotient = \\(2x + 3\\), Remainder = \\(2\\)", "Quotient = \\(2x + 2\\), Remainder = \\(0\\)"], "2x(x + 2) - 4x + 7x + 6 = 2x(x + 2) + 3(x + 2) - 6 + 6 = (2x + 3)(x + 2) + 0"),
                ("(3x^2 + 8x + 2) \\div (x + 1)", "Quotient = \\(3x + 5\\), Remainder = \\(-3\\)", ["Quotient = \\(3x - 5\\), Remainder = \\(-3\\)", "Quotient = \\(3x + 5\\), Remainder = \\(3\\)", "Quotient = \\(3x + 2\\), Remainder = \\(0\\)"], "3x(x + 1) - 3x + 8x + 2 = 3x(x + 1) + 5(x + 1) - 5 + 2 = (3x + 5)(x + 1) - 3"),
                ("(x^2 - 2x - 15) \\div (x + 3)", "Quotient = \\(x - 5\\), Remainder = \\(0\\)", ["Quotient = \\(x + 5\\), Remainder = \\(0\\)", "Quotient = \\(x - 5\\), Remainder = \\(3\\)", "Quotient = \\(x - 3\\), Remainder = \\(0\\)"], "x(x + 3) - 3x - 2x - 15 = x(x + 3) - 5(x + 3) + 15 - 15 = (x - 5)(x + 3) + 0"),
                ("(4x^2 + 9x + 1) \\div (x + 2)", "Quotient = \\(4x + 1\\), Remainder = \\(-1\\)", ["Quotient = \\(4x - 1\\), Remainder = \\(-1\\)", "Quotient = \\(4x + 1\\), Remainder = \\(1\\)", "Quotient = \\(4x + 2\\), Remainder = \\(-1\\)"], "4x(x + 2) - 8x + 9x + 1 = 4x(x + 2) + (x + 2) - 2 + 1 = (4x + 1)(x + 2) - 1"),
                ("(x^3 + 3x^2 + 4x + 5) \\div (x + 1)", "Quotient = \\(x^2 + 2x + 2\\), Remainder = \\(3\\)", ["Quotient = \\(x^2 - 2x + 2\\), Remainder = \\(3\\)", "Quotient = \\(x^2 + 2x - 2\\), Remainder = \\(3\\)", "Quotient = \\(x^2 + 2x + 2\\), Remainder = \\(-3\\)"], "x^2(x + 1) + 2x(x + 1) + 2(x + 1) + 3 = (x^2 + 2x + 2)(x + 1) + 3"),
                ("(2x^3 + 5x^2 - x - 6) \\div (x + 2)", "Quotient = \\(2x^2 + x - 3\\), Remainder = \\(0\\)", ["Quotient = \\(2x^2 - x - 3\\), Remainder = \\(0\\)", "Quotient = \\(2x^2 + x + 3\\), Remainder = \\(0\\)", "Quotient = \\(2x^2 - 3\\), Remainder = \\(0\\)"], "2x^2(x + 2) + x(x + 2) - 3(x + 2) = (2x^2 + x - 3)(x + 2) + 0"),
                ("(x^3 + 8) \\div (x + 2)", "Quotient = \\(x^2 - 2x + 4\\), Remainder = \\(0\\)", ["Quotient = \\(x^2 + 2x + 4\\), Remainder = \\(0\\)", "Quotient = \\(x^2 - 4\\), Remainder = \\(0\\)", "Quotient = \\(x^2 - 2x - 4\\), Remainder = \\(0\\)"], "x^2(x + 2) - 2x(x + 2) + 4(x + 2) = (x^2 - 2x + 4)(x + 2) + 0"),
                ("(3x^2 + 11x + 10) \\div (x + 2)", "Quotient = \\(3x + 5\\), Remainder = \\(0\\)", ["Quotient = \\(3x - 5\\), Remainder = \\(0\\)", "Quotient = \\(3x + 5\\), Remainder = \\(2\\)", "Quotient = \\(3x + 2\\), Remainder = \\(0\\)"], "3x(x + 2) - 6x + 11x + 10 = 3x(x + 2) + 5(x + 2) = (3x + 5)(x + 2) + 0"),
                ("(x^3 - x^2 - 5x - 3) \\div (x + 1)", "Quotient = \\(x^2 - 2x - 3\\), Remainder = \\(0\\)", ["Quotient = \\(x^2 + 2x - 3\\), Remainder = \\(0\\)", "Quotient = \\(x^2 - 2x + 3\\), Remainder = \\(0\\)", "Quotient = \\(x^2 - 3\\), Remainder = \\(0\\)"], "x^2(x + 1) - 2x(x + 1) - 3(x + 1) = (x^2 - 2x - 3)(x + 1) + 0")
            ],
            'tmpls': [
                "Perform linear division with divisor \\((x + a)\\): \\({0}\\):",
                "Divide by linear method: \\({0}\\):",
                "Find quotient and remainder for \\({0}\\) by linear method:",
                "Using the linear division method, solve \\({0}\\):",
                "Calculate quotient and remainder of \\({0}\\):",
                "What is the result when \\({0}\\) is divided using the linear method?",
                "Apply linear division with \\((x + a)\\) to \\({0}\\):",
                "Determine the quotient and remainder: \\({0}\\):",
                "Evaluate by linear division: \\({0}\\):",
                "Compute quotient and remainder for \\({0}\\) using linear algebraic restructuring:"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Write Each Term in Multiples of Divisor**\n{item[3]}.\n**Step 2: Collect Factored Terms**\nGroup the linear factor \\(x + a\\).\n**Step 3: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Identifying intermediate steps in linear division
        {
            'data': [
                ("In linear division of \\(x^2 + 4x + 5\\) by \\(x - 2\\), what is the first replacement for \\(x^2\\)?", "\\(x(x - 2) + 2x\\)", ["\\(x(x - 2) - 2x\\)", "\\(x(x + 2) - 2x\\)", "\\(x^2 - 2x\\)"]),
                ("In linear division of \\(2x^2 - 3x + 1\\) by \\(x + 1\\), what is \\(2x^2\\) rewritten as?", "\\(2x(x + 1) - 2x\\)", ["\\(2x(x + 1) + 2x\\)", "\\(2x(x - 1) + 2x\\)", "\\(2x^2 + 2x\\)"]),
                ("In linear division of \\(3x^3 + x - 4\\) by \\(x - 1\\), what is \\(3x^3\\) rewritten as?", "\\(3x^2(x - 1) + 3x^2\\)", ["\\(3x^2(x - 1) - 3x^2\\)", "\\(3x(x - 1) + 3x\\)", "\\(3x^2(x + 1) - 3x^2\\)"]),
                ("In linear division of \\(x^2 - 5x + 6\\) by \\(x - 3\\), after rewriting \\(x^2 = x(x - 3) + 3x\\), what is the remaining linear term?", "\\(-2x + 6 = -2(x - 3)\\)", ["\\(8x + 6\\)", "\\(-5x + 6\\)", "\\(2x - 6\\)"]),
                ("What is the main strategy of the linear division method?", "Expressing each higher power term progressively in terms of the linear divisor \\((x - a)\\)", ["Dividing each coefficient by a", "Multiplying polynomials", "Plotting points on graph"]),
                ("In linear division, when does the process stop?", "When the remaining term has degree strictly less than the divisor (degree 0, constant)", ["When quotient is zero", "After 2 steps always", "When dividend becomes negative"]),
                ("For \\((x^2 - 9) \\div (x - 3)\\), the linear method writes \\(x^2 - 9\\) as:", "\\(x(x - 3) + 3(x - 3) = (x + 3)(x - 3)\\)", ["\\(x(x - 3) - 9\\)", "\\(x(x + 3) - 9\\)", "\\((x - 3)^2\\)"]),
                ("In linear division of \\(4x^2 + 5\\) by \\(x - 1\\), what is the remainder?", "9 (since \\(4(1)^2 + 5 = 9\\))", ["5", "4", "1"]),
                ("In \\(P(x) = Q(x)(x - a) + R\\), what is the degree of \\(Q(x)\\) if \\(\\deg P(x) = 3\\)?", "2", ["3", "1", "0"]),
                ("How does the result of linear division compare with synthetic division?", "Both methods yield the exact same quotient and remainder", ["Synthetic gives a larger remainder", "Linear gives a higher degree quotient", "They differ by sign"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the linear division step: {0}",
                "Answer the following question about linear division: {0}",
                "Identify the correct algebraic manipulation: {0}",
                "Select the correct intermediate step: {0}",
                "Determine the true statement: {0}",
                "What is the mathematical step? {0}",
                "Choose the right answer: {0}",
                "State the correct procedure: {0}",
                "Which option correctly answers: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Understand Linear Division Substitution**\nTo divide by \\(x - a\\), replace \\(x^k\\) with \\(x^(k-1)(x - a) + a x^(k-1)\\).\nContinue until only a constant remainder remains.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Comparing linear method and synthetic division equivalence
        {
            'data': [
                ("Verify the division of \\(x^2 + 7x + 12\\) by \\(x + 3\\) via both methods:", "Quotient = \\(x + 4\\), Remainder = \\(0\\) by both methods", ["Quotient = \\(x - 4\\), Remainder = \\(0\\)", "Quotient = \\(x + 4\\), Remainder = \\(3\\)", "Quotient = \\(x + 3\\), Remainder = \\(0\\)"]),
                ("Verify \\((2x^2 - 7x + 5) \\div (x - 1)\\) via both methods:", "Quotient = \\(2x - 5\\), Remainder = \\(0\\) identically", ["Quotient = \\(2x + 5\\), Remainder = \\(0\\)", "Quotient = \\(2x - 5\\), Remainder = \\(2\\)", "Quotient = \\(2x - 1\\), Remainder = \\(5\\)"]),
                ("Verify \\((x^3 - 1) \\div (x - 1)\\) via both methods:", "Quotient = \\(x^2 + x + 1\\), Remainder = \\(0\\) in both", ["Quotient = \\(x^2 - x + 1\\), Remainder = \\(0\\)", "Quotient = \\(x^2 + 1\\), Remainder = \\(0\\)", "Quotient = \\(x^2 + x - 1\\), Remainder = \\(0\\)"]),
                ("Verify \\((3x^2 + 5x - 4) \\div (x + 2)\\) via both methods:", "Quotient = \\(3x - 1\\), Remainder = \\(-2\\)", ["Quotient = \\(3x + 1\\), Remainder = \\(-2\\)", "Quotient = \\(3x - 1\\), Remainder = \\(2\\)", "Quotient = \\(3x + 2\\), Remainder = \\(-4\\)"]),
                ("Verify \\((x^3 + 2x^2 + 5) \\div (x - 1)\\) via both methods:", "Quotient = \\(x^2 + 3x + 3\\), Remainder = \\(8\\)", ["Quotient = \\(x^2 - 3x + 3\\), Remainder = \\(8\\)", "Quotient = \\(x^2 + 3x - 3\\), Remainder = \\(8\\)", "Quotient = \\(x^2 + 3x + 3\\), Remainder = \\(-8\\)"]),
                ("Verify \\((4x^2 - 9) \\div (x - 2)\\) via both methods:", "Quotient = \\(4x + 8\\), Remainder = \\(7\\)", ["Quotient = \\(4x - 8\\), Remainder = \\(7\\)", "Quotient = \\(4x + 8\\), Remainder = \\(-7\\)", "Quotient = \\(4x + 2\\), Remainder = \\(9\\)"]),
                ("Verify \\((x^2 - 6x + 9) \\div (x - 3)\\) via both methods:", "Quotient = \\(x - 3\\), Remainder = \\(0\\)", ["Quotient = \\(x + 3\\), Remainder = \\(0\\)", "Quotient = \\(x - 3\\), Remainder = \\(3\\)", "Quotient = \\(x - 6\\), Remainder = \\(0\\)"]),
                ("Verify \\((2x^3 - x^2 + 3) \\div (x + 1)\\) via both methods:", "Quotient = \\(2x^2 - 3x + 3\\), Remainder = \\(0\\)", ["Quotient = \\(2x^2 + 3x + 3\\), Remainder = \\(0\\)", "Quotient = \\(2x^2 - 3x - 3\\), Remainder = \\(0\\)", "Quotient = \\(2x^2 + 3\\), Remainder = \\(0\\)"]),
                ("Verify \\((5x^2 - 3x + 1) \\div (x - 2)\\) via both methods:", "Quotient = \\(5x + 7\\), Remainder = \\(15\\)", ["Quotient = \\(5x - 7\\), Remainder = \\(15\\)", "Quotient = \\(5x + 7\\), Remainder = \\(-15\\)", "Quotient = \\(5x + 2\\), Remainder = \\(1\\)"]),
                ("Verify \\((x^3 + 8) \\div (x - 2)\\) via both methods:", "Quotient = \\(x^2 + 2x + 4\\), Remainder = \\(16\\)", ["Quotient = \\(x^2 - 2x + 4\\), Remainder = \\(16\\)", "Quotient = \\(x^2 + 2x + 4\\), Remainder = \\(0\\)", "Quotient = \\(x^2 + 4\\), Remainder = \\(16\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate and verify: {0}",
                "Find the unique quotient and remainder: {0}",
                "Solve and check consistency: {0}",
                "Determine quotient and remainder: {0}",
                "Calculate: {0}",
                "What are quotient and remainder? {0}",
                "Compute and verify: {0}",
                "State the result: {0}",
                "Select the correct answer: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Check Consistency Across Methods**\nBoth linear and synthetic division produce identical quotient and remainder.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Remainder calculation without full division table
        {
            'data': [
                ("(x^3 - 3x^2 + 4x - 5)", "x - 2", "-1", ["-5", "3", "1"], "P(2) = 8 - 12 + 8 - 5 = -1"),
                ("(2x^2 - 5x + 7)", "x - 1", "4", ["2", "-5", "7"], "P(1) = 2 - 5 + 7 = 4"),
                ("(x^4 - 2x^2 + 3)", "x - 2", "11", ["16", "8", "3"], "P(2) = 16 - 8 + 3 = 11"),
                ("(3x^2 + 4x - 1)", "x + 1", "-2", ["2", "6", "-1"], "P(-1) = 3 - 4 - 1 = -2"),
                ("(x^3 + 5x^2 - 2x + 6)", "x + 2", "22", ["18", "-22", "6"], "P(-2) = -8 + 20 + 4 + 6 = 22"),
                ("(4x^2 - 7x + 2)", "x - 3", "17", ["12", "15", "-7"], "P(3) = 36 - 21 + 2 = 17"),
                ("(x^3 - 8x + 1)", "x - 3", "4", ["1", "10", "-4"], "P(3) = 27 - 24 + 1 = 4"),
                ("(2x^3 - 3x + 5)", "x + 1", "6", ["4", "-6", "5"], "P(-1) = -2 + 3 + 5 = 6"),
                ("(5x^2 + 2x - 9)", "x - 1", "-2", ["-9", "2", "5"], "P(1) = 5 + 2 - 9 = -2"),
                ("(x^4 - 16)", "x - 2", "0", ["16", "-16", "2"], "P(2) = 16 - 16 = 0")
            ],
            'tmpls': [
                "Find the remainder when \\({0}\\) is divided by \\({1}\\):",
                "What is the remainder when \\({0}\\) is divided by \\({1}\\)?",
                "Determine the remainder of \\({0} \\div ({1})\\):",
                "Evaluate the remainder for \\({0}\\) divided by \\({1}\\):",
                "Calculate the remainder of \\({0}\\) divided by \\({1}\\):",
                "Compute the remainder when \\({1}\\) divides \\({0}\\):",
                "State the remainder of \\({0} \\div ({1})\\):",
                "Select the remainder of \\({0}\\) when divided by \\({1}\\):",
                "Find the remainder without full division: \\({0} \\div ({1})\\):",
                "What remainder does \\({0}\\) leave when divided by \\({1}\\)?"
            ],
            'calc': lambda item: (
                item[2],
                item[3],
                f"**Step 1: Set Divisor Equal to Zero**\n\\({item[1]} = 0 \\implies x = a\\).\n**Step 2: Evaluate \\(P(a)\\)**\n{item[4]}.\n**Step 3: Conclusion**\nThe remainder is {item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 6: Verification of Division Algorithm Identity
        {
            'data': [
                ("In \\(P(x) = (x - 3)(2x + 5) + 4\\), what is the degree of \\(P(x)\\)?", "2 (product of two degree 1 polynomials is degree 2)", ["1", "3", "4"]),
                ("If dividend is \\(x^3 + 2x - 1\\) and divisor is \\(x - 2\\), what is the maximum degree of the remainder?", "0 (remainder must be a constant when divisor is linear)", ["1", "2", "3"]),
                ("What happens if \\(P(a) = 0\\) in the division \\(P(x) \\div (x - a)\\)?", "\\(x - a\\) is an exact factor of \\(P(x)\\) with remainder 0", ["The quotient is 0", "\\(x - a\\) is not a factor", "The degree of P(x) is 0"]),
                ("If \\(P(x) = (x + 4)(x^2 - 2x + 3) + 7\\), what is the constant term of \\(P(x)\\)?", "19 (since \\(4 \\times 3 + 7 = 12 + 7 = 19\\))", ["12", "7", "3"]),
                ("If \\(P(x) = Q(x)(x - 1) + R\\) and \\(P(1) = 8\\), what is \\(R\\)?", "8 (by the Remainder Theorem)", ["0", "1", "-8"]),
                ("If \\(P(x) = Q(x)(x + 2) + 5\\), what is \\(P(-2)\\)?", "5", ["-2", "0", "-5"]),
                ("Can the linear division method be used if the divisor is \\(x^2 + 1\\)?", "Standard linear division is formulated for linear divisors \\((x - a)\\); for quadratics, polynomial long division is used", ["Yes, without modification", "Yes, with synthetic tables", "Only if dividend is linear"]),
                ("If \\(P(x) = (x - 5)(x + 2) + 0\\), what are the roots of \\(P(x) = 0\\)?", "\\(x = 5\\) and \\(x = -2\\)", ["\\(x = -5\\) and \\(x = 2\\)", "\\(x = 5\\) only", "\\(x = -2\\) only"]),
                ("If divisor is \\(x - 3\\) and quotient is \\(4\\) with remainder \\(2\\), find \\(P(x)\\):", "\\(4(x - 3) + 2 = 4x - 12 + 2 = 4x - 10\\)", ["\\(4x - 12\\)", "\\(4x + 2\\)", "\\(4x - 14\\)"]),
                ("In the division identity \\(P(x) = D(x)Q(x) + R(x)\\), the remainder \\(R(x)\\) must satisfy:", "\\(\\deg R(x) < \\deg D(x)\\) or \\(R(x) = 0\\)", ["\\(\\deg R(x) = \\deg D(x)\\)", "\\(\\deg R(x) > \\deg D(x)\\)", "\\(\\deg R(x) \\ge 1\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the division property: {0}",
                "Answer the division algorithm question: {0}",
                "Determine the true statement: {0}",
                "Select the correct conclusion: {0}",
                "What is the mathematical answer? {0}",
                "Analyze the identity: {0}",
                "State the result: {0}",
                "Choose the right answer: {0}",
                "Which option correctly answers: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Understand Division Algorithm Identity**\n\\(P(x) = D(x)Q(x) + R\\) where \\(\\deg R < \\deg D\\) or \\(R = 0\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Conceptual comparison: Linear vs Long vs Synthetic division
        {
            'data': [
                ("What distinguishes the linear method from long division?", "It avoids drawing division brackets and manipulates the polynomial algebraically along one line", ["It gives different remainders", "It cannot be used for cubics", "It works only for monic quadratics"]),
                ("What is a common error in linear division when subtracting terms?", "Sign errors when expanding and distributing negative linear factors \\(-(x - a)\\)", ["Adding fractions wrong", "Dividing by zero", "Miscounting variables"]),
                ("If \\(P(x) = (2x - 1)Q(x) + R\\), how is linear division executed?", "Factor out 2 to get \\(2(x - 1/2)Q(x) + R\\), or regroup directly using \\((2x - 1)\\)", ["Cannot be solved linearly", "By ignoring the 2", "By multiplying by 2"]),
                ("Can linear division factorize a polynomial completely if remainder is zero?", "Yes, it directly expresses the polynomial as \\((x - a) \\times Q(x)\\)", ["No, it only finds remainders", "Only for linear polynomials", "No, long division is mandatory"]),
                ("Which method is most visual in showing the algebraic identity \\(P(x) = (x - a)Q(x) + R\\)?", "The linear division method (shows the identity explicitly at every step)", ["Synthetic division", "Long division", "Graphical method"]),
                ("For \\((x^3 + 1) \\div (x + 1)\\), the linear method yields quotient:", "\\(x^2 - x + 1\\) (with remainder 0)", ["\\(x^2 + x + 1\\)", "\\(x^2 - 1\\)", "\\(x^2 + 1\\)"]),
                ("For \\((x^3 - 1) \\div (x + 1)\\), what is the remainder?", "-2 (since \\((-1)^3 - 1 = -1 - 1 = -2\\))", ["0", "2", "-1"]),
                ("In linear division of \\(5x^2 - 2\\) by \\(x - 3\\), what is the remainder?", "43 (since \\(5(3)^2 - 2 = 45 - 2 = 43\\))", ["45", "13", "2"]),
                ("If \\(x - 1\\) divides \\(x^2 + ax + 3\\) exactly, what is \\(a\\)?", "\\(a = -4\\) (since \\(1 + a + 3 = 0 \\implies a = -4\\))", ["\\(a = 4\\)", "\\(a = 2\\)", "\\(a = -3\\)"]),
                ("What is the degree of quotient when a quadratic polynomial is divided by a linear factor?", "1 (Linear polynomial \\(ax + b\\))", ["2", "0", "Constant"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the linear division comparison: {0}",
                "Select the correct answer: {0}",
                "Analyze the method property: {0}",
                "Determine the true mathematical fact: {0}",
                "Choose the right response: {0}",
                "Answer the conceptual question: {0}",
                "State the correct concept: {0}",
                "Which option correctly answers: {0}",
                "Find the correct conclusion: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Understand the Linear Division Method**\nLinear division expresses \\(P(x)\\) directly as \\((x - a)Q(x) + R\\).\nQuotient and remainder match synthetic and long division exactly.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

if __name__ == "__main__":
    print("Compiling Chapter 3 Part 1 (3.1.1, 3.1.2, 3.2, 3.3.1, 3.3.2)...")
    qs = []
    for gen in [gen_3_1_1, gen_3_1_2, gen_3_2, gen_3_3_1, gen_3_3_2]:
        sub_qs = gen()
        print(f"Generated {len(sub_qs)} questions for {sub_qs[0]['topicCode']}")
        qs.extend(sub_qs)
    
    out_path = "scripts/mh9_mth1_ch3_p1_test.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(qs)} questions to {out_path}")
