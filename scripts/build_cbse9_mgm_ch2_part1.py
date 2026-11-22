# scripts/build_cbse9_mgm_ch2_part1.py
# Subtopics:
# 2.1.1: Variables, constants, coefficients, and degree 1 polynomials (80 Qs)
# 2.1.2: Distinction between algebraic expressions and polynomials (80 Qs)

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 2
CH_NAME = "Introduction to Linear Polynomials"

# ==============================================================================
# SUBTOPIC 2.1.1: Variables, constants, coefficients, and degree 1 polynomials
# ==============================================================================
def gen_2_1_1():
    tc = "CBSE-9-MGM-2-2.1.1"
    tname = "Variables, constants, coefficients, and degree 1 polynomials"

    # Arch 0: Identifying coefficient of x in linear polynomial
    arch0 = {
        'data': [
            ("5x - 7", 5), ("-3x + 11", -3), ("\\frac{2}{3}x - 4", "\\frac{2}{3}"),
            ("-x + 8", -1), ("12 - 4x", -4), ("7x", 7), ("-\\frac{5}{2}x + 9", "-\\frac{5}{2}"),
            ("8 - x", -1), ("\\sqrt{3}x - 5", "\\sqrt{3}"), ("-9x - 14", -9)
        ],
        'tmpls': [
            "In the linear polynomial \\( p(x) = {0} \\), what is the coefficient of \\( x \\)?",
            "Identify the coefficient of \\( x \\) in the polynomial \\( {0} \\).",
            "What is the coefficient of the variable \\( x \\) in the expression \\( {0} \\)?",
            "Find the coefficient of \\( x \\) in the degree 1 polynomial \\( {0} \\).",
            "In the polynomial expression \\( {0} \\), the coefficient of \\( x \\) is:",
            "Determine the coefficient of \\( x \\) in \\( p(x) = {0} \\):",
            "The numerical coefficient of the linear term in \\( {0} \\) is:",
            "What value multiplies \\( x \\) in the linear polynomial \\( {0} \\)?",
            "In the first-degree polynomial \\( {0} \\), the coefficient of \\( x \\) equals:",
            "State the coefficient of \\( x \\) for the polynomial \\( {0} \\):"
        ],
        'calc': lambda item: (
            str(item[1]),
            [
                str(-item[1]) if isinstance(item[1], int) else f"-{item[1]}",
                "1",
                "0"
            ],
            f"**Step 1: Write polynomial in standard form.**\nA linear polynomial in one variable has the form \\( p(x) = ax + b \\), where \\( a \\) is the coefficient of \\( x \\) and \\( b \\) is the constant term.\n\n**Step 2: Identify the coefficient \\( a \\).**\nIn \\( {item[0]} \\), the term containing \\( x \\) has coefficient \\( {item[1]} \\).\n\n**Step 3: State the coefficient.**\nThe coefficient of \\( x \\) is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Constant term in a linear polynomial
    arch1 = {
        'data': [
            ("4x + 9", 9), ("-7x - 15", -15), ("8 - 3x", 8), ("-5 - 2x", -5),
            ("6x", 0), ("-x + 13", 13), ("\\frac{1}{2}x - 7", -7), ("-4x", 0),
            ("11 - x", 11), ("-3x - 1", -1)
        ],
        'tmpls': [
            "What is the constant term in the linear polynomial \\( p(x) = {0} \\)?",
            "Identify the constant term in the polynomial \\( {0} \\).",
            "In the polynomial \\( {0} \\), the constant term is:",
            "Find the constant term of the linear polynomial \\( {0} \\).",
            "Determine the term independent of \\( x \\) in \\( {0} \\):",
            "The constant term in \\( p(x) = {0} \\) is equal to:",
            "What is the value of the constant term in \\( {0} \\)?",
            "In the expression \\( {0} \\), which value represents the constant term?",
            "State the constant term of the polynomial \\( {0} \\):",
            "Identify the term independent of variable \\( x \\) in \\( {0} \\):"
        ],
        'calc': lambda item: (
            str(item[1]),
            [
                str(-item[1]) if item[1] != 0 else "1",
                str(item[1] + 2),
                str(item[1] - 3)
            ],
            f"**Step 1: Understand the constant term definition.**\nThe constant term in a polynomial \\( ax + b \\) is the term that does not contain the variable \\( x \\) (the coefficient of \\( x^0 \\)).\n\n**Step 2: Read the constant term.**\nIn \\( {item[0]} \\), the independent constant term is \\( {item[1]} \\).\n\n**Step 3: State the constant term.**\nThe constant term is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Degree of linear and constant polynomials
    arch2 = {
        'data': [
            ("3x - 5", 1, "highest power of x is 1"),
            ("7", 0, "non-zero constant polynomial has degree 0"),
            ("-4x + 9", 1, "highest exponent of the variable x is 1"),
            ("0", "not defined", "degree of the zero polynomial is conventionally not defined"),
            ("\\frac{5}{2}x", 1, "monomial linear polynomial has degree 1"),
            ("-12", 0, "constant polynomial -12 = -12 * x^0 has degree 0"),
            ("1 - x", 1, "degree of linear polynomial 1 - x is 1"),
            ("100", 0, "degree of constant polynomial 100 is 0"),
            ("-x", 1, "linear polynomial -x has degree 1"),
            ("0x + 0", "not defined", "zero polynomial has undefined degree")
        ],
        'tmpls': [
            "What is the degree of the polynomial \\( p(x) = {0} \\)?",
            "The degree of the polynomial \\( {0} \\) is:",
            "Find the degree of the polynomial \\( {0} \\).",
            "Determine the degree of \\( p(x) = {0} \\):",
            "In algebra, the degree of \\( {0} \\) is:",
            "State the degree of the polynomial \\( {0} \\):",
            "What is the degree of the expression \\( {0} \\)?",
            "The highest power of the variable in \\( {0} \\) gives a degree of:",
            "Identify the degree of the polynomial \\( {0} \\):",
            "Compute the degree of \\( p(x) = {0} \\):"
        ],
        'calc': lambda item: (
            str(item[1]),
            [
                "0" if str(item[1]) != "0" else "1",
                "2" if str(item[1]) != "2" else "3",
                "not defined" if str(item[1]) != "not defined" else "-1"
            ],
            f"**Step 1: Recall definition of polynomial degree.**\nThe degree of a polynomial in one variable is the highest power (exponent) of the variable appearing with a non-zero coefficient.\n\n**Step 2: Analyze the given polynomial \\( {item[0]} \\).**\n{item[2]}.\n\n**Step 3: State the degree.**\nThe degree of \\( {item[0]} \\) is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 3: Condition for ax + b to be a linear polynomial (a ≠ 0)
    arch3 = {
        'data': [
            ("(k - 3)x + 7", "k ≠ 3", "k = 3"),
            ("(2k - 8)x - 5", "k ≠ 4", "k = 4"),
            ("(3k + 12)x + 1", "k ≠ -4", "k = -4"),
            ("(5k - 15)x + 8", "k ≠ 3", "k = 3"),
            ("(4k + 20)x - 2", "k ≠ -5", "k = -5"),
            ("(k + 7)x - 9", "k ≠ -7", "k = -7"),
            ("(6k - 18)x + 4", "k ≠ 3", "k = 3"),
            ("(2k + 10)x - 1", "k ≠ -5", "k = -5"),
            ("(7k - 21)x + 11", "k ≠ 3", "k = 3"),
            ("(3k - 9)x + 6", "k ≠ 3", "k = 3")
        ],
        'tmpls': [
            "For what condition on \\( k \\) is the expression \\( p(x) = {0} \\) a linear polynomial in \\( x \\)?",
            "Under what condition does \\( {0} \\) represent a polynomial of degree 1?",
            "Find the condition on \\( k \\) so that \\( {0} \\) is a linear polynomial:",
            "The polynomial \\( {0} \\) is linear if and only if:",
            "Determine the requirement on \\( k \\) for \\( {0} \\) to remain a linear polynomial:",
            "For \\( {0} \\) to be a first-degree polynomial, \\( k \\) must satisfy:",
            "What is the necessary condition on \\( k \\) for \\( {0} \\) to have degree 1?",
            "Identify the condition under which \\( {0} \\) is linear in \\( x \\):",
            "The expression \\( {0} \\) is of degree 1 provided that:",
            "State the restriction on \\( k \\) such that \\( {0} \\) is a linear polynomial:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[2],
                f"k = 0",
                f"k > 0"
            ],
            f"**Step 1: Recall linear polynomial definition.**\nA polynomial \\( ax + b \\) is linear if and only if the coefficient of \\( x \\) is non-zero, i.e., \\( a \\neq 0 \\).\n\n**Step 2: Set the coefficient not equal to zero.**\nCoefficient of \\( x \\) is {item[0].split(')')[0][1:]} \\neq 0 \\implies {item[1]}.\n\n**Step 3: State the condition.**\nThe polynomial is linear if {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Number of terms in linear polynomials (monomial vs binomial)
    arch4 = {
        'data': [
            ("7x", "monomial (1 term)", ["binomial (2 terms)", "trinomial (3 terms)", "zero polynomial"]),
            ("3x - 8", "binomial (2 terms)", ["monomial (1 term)", "trinomial (3 terms)", "quadrinomial"]),
            ("-5x", "monomial (1 term)", ["binomial (2 terms)", "trinomial (3 terms)", "constant polynomial"]),
            ("9 - 2x", "binomial (2 terms)", ["monomial (1 term)", "trinomial (3 terms)", "zero polynomial"]),
            ("\\frac{3}{4}x", "monomial (1 term)", ["binomial (2 terms)", "constant polynomial", "trinomial"]),
            ("4x + 11", "binomial (2 terms)", ["monomial (1 term)", "trinomial (3 terms)", "quadrinomial"]),
            ("-x", "monomial (1 term)", ["binomial (2 terms)", "constant polynomial", "zero polynomial"]),
            ("15 - x", "binomial (2 terms)", ["monomial (1 term)", "trinomial (3 terms)", "constant"]),
            ("8x", "monomial (1 term)", ["binomial (2 terms)", "trinomial (3 terms)", "binomial"]),
            ("-6x - 7", "binomial (2 terms)", ["monomial (1 term)", "trinomial (3 terms)", "monomial"])
        ],
        'tmpls': [
            "Based on the number of terms, how is the linear polynomial \\( p(x) = {0} \\) classified?",
            "Classify the polynomial \\( {0} \\) according to its number of terms:",
            "How many terms does the linear polynomial \\( {0} \\) have and what is its classification?",
            "In terms of term count, the polynomial \\( {0} \\) is a:",
            "What type of polynomial by number of terms is \\( {0} \\)?",
            "Determine the classification of \\( {0} \\) based on its terms:",
            "Is the linear polynomial \\( {0} \\) a monomial, binomial, or trinomial?",
            "Identify the classification of \\( {0} \\) by term count:",
            "The polynomial \\( {0} \\) consists of:",
            "Classify \\( p(x) = {0} \\) by the number of non-zero terms:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Count non-zero terms separated by addition or subtraction.**\nExamine \\( {item[0]} \\).\n\n**Step 2: Recall polynomial naming conventions.**\n- 1 term: Monomial\n- 2 terms: Binomial\n- 3 terms: Trinomial\n\n**Step 3: State the classification.**\nThe polynomial is a {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 5: Maximum and minimum number of terms in a linear polynomial in one variable
    arch5 = {
        'data': [
            ("maximum number of terms in a linear polynomial in one variable", "2 terms", ["1 term", "3 terms", "infinitely many"]),
            ("minimum number of terms in a linear polynomial in one variable", "1 term", ["0 terms", "2 terms", "3 terms"]),
            ("maximum number of zeroes a linear polynomial can have", "1 zero", ["2 zeroes", "0 zeroes", "infinitely many zeroes"]),
            ("general standard form of a linear polynomial in variable x", "ax + b (where a ≠ 0)", ["ax² + bx + c", "ax + b (where a = 0)", "a/x + b"]),
            ("the shape of the graph of any linear polynomial in one variable y = ax + b", "a straight line", ["a parabola", "a circle", "a hyperbola"]),
            ("polynomial of degree 1 is called", "linear polynomial", ["quadratic polynomial", "cubic polynomial", "constant polynomial"]),
            ("the degree of the zero polynomial 0 is", "not defined", ["0", "1", "infinity"]),
            ("the degree of a non-zero constant polynomial like 7 is", "0", ["1", "not defined", "any integer"]),
            ("number of zeroes of a non-zero constant polynomial like p(x) = 5 is", "0 zeroes", ["1 zero", "5 zeroes", "infinitely many"]),
            ("number of zeroes of the zero polynomial p(x) = 0 is", "infinitely many (every real number)", ["0 zeroes", "1 zero", "not defined"])
        ],
        'tmpls': [
            "What is the {0}?",
            "In algebra, the {0} is:",
            "Identify the correct statement regarding the {0}:",
            "Which of the following gives the {0}?",
            "State the {0}:",
            "Determine the {0}:",
            "According to polynomial theory, the {0} is:",
            "What is known about the {0}?",
            "Find the {0}:",
            "Which value or description matches the {0}?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the theoretical properties of polynomials.**\nConsider the property '{item[0]}'.\n\n**Step 2: Apply fundamental definitions.**\nA linear polynomial in one variable has the general form \\( ax + b \\) with \\( a \\neq 0 \\).\n\n**Step 3: State the result.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Forming linear polynomial models from verbal descriptions
    arch6 = {
        'data': [
            ("taxi charges a fixed flag fall of ₹50 plus ₹12 per km traveled x", "p(x) = 12x + 50", ["p(x) = 50x + 12", "p(x) = 12x - 50", "p(x) = 62x"]),
            ("perimeter of a rectangle with length x and fixed width 5 cm", "P(x) = 2x + 10", ["P(x) = x + 10", "P(x) = 2x + 5", "P(x) = 10x"]),
            ("cost of purchasing x pens at ₹15 each with a ₹20 gift box", "C(x) = 15x + 20", ["C(x) = 20x + 15", "C(x) = 35x", "C(x) = 15x - 20"]),
            ("temperature in Fahrenheit given Celsius temperature x is 9/5 times x plus 32", "F(x) = \\frac{9}{5}x + 32", ["F(x) = \\frac{5}{9}x + 32", "F(x) = \\frac{9}{5}x - 32", "F(x) = 32x + \\frac{9}{5}"]),
            ("total money saved if ₹500 was initial balance and ₹150 is saved per week x", "S(x) = 150x + 500", ["S(x) = 500x + 150", "S(x) = 650x", "S(x) = 150x - 500"]),
            ("total distance traveled at constant speed 60 km/h after x hours with 20 km head start", "D(x) = 60x + 20", ["D(x) = 20x + 60", "D(x) = 80x", "D(x) = 60x - 20"]),
            ("perimeter of an equilateral triangle of side length x + 2", "P(x) = 3x + 6", ["P(x) = 3x + 2", "P(x) = x + 6", "P(x) = 6x"]),
            ("a subscription costs ₹199 monthly plus ₹20 per movie rented x", "C(x) = 20x + 199", ["C(x) = 199x + 20", "C(x) = 219x", "C(x) = 20x - 199"]),
            ("water tank with 100 liters draining at 4 liters per minute x", "V(x) = -4x + 100", ["V(x) = 4x + 100", "V(x) = -4x - 100", "V(x) = 96x"]),
            ("mass of an empty beaker 45 g plus liquid of density 2 g/mL for volume x mL", "M(x) = 2x + 45", ["M(x) = 45x + 2", "M(x) = 47x", "M(x) = 2x - 45"])
        ],
        'tmpls': [
            "Which linear polynomial represents the situation: {0}?",
            "Express the following as a linear polynomial in \\( x \\): {0}.",
            "Formulate a degree 1 polynomial for: {0}.",
            "In algebraic modeling, {0} is written as:",
            "Write the polynomial function \\( p(x) \\) corresponding to: {0}.",
            "Translate into a linear polynomial: {0}.",
            "The mathematical polynomial modeling '{0}' is:",
            "Which algebraic polynomial models: {0}?",
            "Represent the following real-world scenario as a linear polynomial: {0}.",
            "Find the linear polynomial \\( p(x) \\) for: {0}."
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify variable and rate of change.**\nThe rate of change per unit of \\( x \\) forms the coefficient of \\( x \\).\n\n**Step 2: Identify fixed initial value or constant.**\nThe initial fixed amount forms the constant term \\( b \\).\n\n**Step 3: Combine into linear form \\( ax + b \\).**\nThe resulting polynomial is \\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 7: Value of polynomial coefficients under constraint (e.g. degree 1)
    arch7 = {
        'data': [
            ("(a - 2)x^2 + (b + 3)x + 5 is a linear polynomial in x", "a = 2 and b ≠ -3", ["a ≠ 2 and b = -3", "a = 2 and b = -3", "a = 0 and b = 0"]),
            ("(p + 4)x^2 + (q - 1)x - 7 is a linear polynomial in x", "p = -4 and q ≠ 1", ["p = 4 and q = 1", "p ≠ -4 and q = 1", "p = 0 and q = 0"]),
            ("(m - 5)x^3 + (n - 2)x^2 + 4x + 1 is a linear polynomial in x", "m = 5 and n = 2", ["m ≠ 5 and n ≠ 2", "m = 5 and n ≠ 2", "m = 0 and n = 0"]),
            ("(c + 1)x^2 + 6x - 8 is a linear polynomial in x", "c = -1", ["c ≠ -1", "c = 1", "c = 0"]),
            ("(k - 7)x^2 + (k - 7)x + 3 is NOT a linear polynomial when", "k = 7", ["k ≠ 7", "k = 0", "k = -7"]),
            ("(2a - 6)x^2 + 5x - 4 has degree 1 if", "a = 3", ["a ≠ 3", "a = -3", "a = 0"]),
            ("(3p + 9)x^2 + 7x + 2 is linear in x if", "p = -3", ["p ≠ -3", "p = 3", "p = 0"]),
            ("(h - 4)x^2 + (k - 2)x + 9 is a constant polynomial if", "h = 4 and k = 2", ["h ≠ 4 and k ≠ 2", "h = 4 and k ≠ 2", "h = 0 and k = 0"]),
            ("(r - 1)x + (s + 5) is the zero polynomial if", "r = 1 and s = -5", ["r ≠ 1 and s ≠ -5", "r = 1 and s = 5", "r = 0 and s = 0"]),
            ("(u + 3)x^2 + (v - 8)x + 6 is linear if", "u = -3 and v ≠ 8", ["u = 3 and v = 8", "u ≠ -3 and v = 8", "u = 0 and v = 0"])
        ],
        'tmpls': [
            "The expression \\( p(x) = {0} \\). What must be the values of the constants?",
            "For what values of the parameters is \\( {0} \\)?",
            "Determine the conditions on the coefficients such that \\( {0} \\):",
            "In polynomial theory, \\( {0} \\) holds when:",
            "Find the required values of the variables so that \\( {0} \\):",
            "What parameter values ensure that \\( {0} \\)?",
            "The expression \\( {0} \\) satisfies the given degree requirement when:",
            "Solve for the parameters given that \\( {0} \\):",
            "Under what conditions on the constants is \\( {0} \\)?",
            "Identify the correct parameter values for which \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall degree condition.**\nFor a polynomial to have degree 1 (linear), the coefficient of any higher power (such as \\( x^2, x^3 \\)) must be strictly 0, and the coefficient of \\( x \\) must be non-zero.\n\n**Step 2: Equate higher coefficients to zero and linear coefficient not zero.**\nSet the coefficients accordingly and solve the resulting simple linear equations.\n\n**Step 3: State the parameter values.**\nThe required conditions are {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 2.1.2: Distinction between algebraic expressions and polynomials
# ==============================================================================
def gen_2_1_2():
    tc = "CBSE-9-MGM-2-2.1.2"
    tname = "Distinction between algebraic expressions and polynomials"

    # Arch 0: Identifying which expressions are polynomials
    arch0 = {
        'data': [
            ("x + \\frac{1}{x}", "Not a polynomial", "contains variable with negative exponent x^{-1}"),
            ("3x^2 + 5x - 7", "Polynomial", "all exponents of x are non-negative integers (2, 1, 0)"),
            ("\\sqrt{x} + 4", "Not a polynomial", "exponent of x is fractional (1/2)"),
            ("x^3 - 4x + 9", "Polynomial", "all powers of x are whole numbers (3, 1, 0)"),
            ("\\frac{2}{x^2} + 3x - 1", "Not a polynomial", "term contains x^{-2}"),
            ("5x - 8", "Polynomial", "degree 1 linear polynomial with non-negative integer power"),
            ("x^2 + \\sqrt{3}x + 2", "Polynomial", "the coefficient is a radical, but the exponent of x is 1 (a whole number)"),
            ("3\\sqrt{x} + x^2", "Not a polynomial", "contains x^{1/2} which is not an integer power"),
            ("x^{3/2} - x + 1", "Not a polynomial", "contains fractional exponent 3/2"),
            ("\\frac{x^2 + 5x + 6}{x + 2} \\text{ (as an unsimplified expression)}", "Algebraic rational expression, not a polynomial", "quotient of polynomials with denominator variable")
        ],
        'tmpls': [
            "Is the expression \\( {0} \\) a polynomial?",
            "Classify the expression \\( {0} \\) as a polynomial or not a polynomial:",
            "Determine whether \\( {0} \\) is a polynomial in \\( x \\):",
            "In algebra, does \\( {0} \\) qualify as a polynomial?",
            "Check if the algebraic expression \\( {0} \\) is a polynomial:",
            "Which classification correctly describes \\( {0} \\)?",
            "Is \\( p(x) = {0} \\) a valid polynomial?",
            "Examine whether \\( {0} \\) satisfies the definition of a polynomial:",
            "Does \\( {0} \\) represent a polynomial in one variable?",
            "State whether \\( {0} \\) is a polynomial:"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Polynomial" if item[1] != "Polynomial" else "Not a polynomial",
                "Trinomial of degree -1",
                "Cannot be determined"
            ],
            f"**Step 1: Check exponents of the variable \\( x \\).**\nBy definition, an algebraic expression in \\( x \\) is a polynomial if and only if all exponents of \\( x \\) are whole numbers (non-negative integers: \\( 0, 1, 2, \\dots \\)).\n\n**Step 2: Inspect the terms of \\( {item[0]} \\).**\n{item[2]}.\n\n**Step 3: State the conclusion.**\nThe expression is: {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Exponent requirements for polynomials (whole numbers / non-negative integers)
    arch1 = {
        'data': [
            ("exponents of the variable in any polynomial must be", "whole numbers (non-negative integers: 0, 1, 2, ...)", ["any real numbers", "integers including negative integers", "rational fractions"]),
            ("the coefficients of a polynomial can be", "any real numbers (rational or irrational)", ["only positive integers", "only rational numbers", "only whole numbers"]),
            ("an algebraic expression with a variable in the denominator is", "not a polynomial (has negative exponent)", ["always a polynomial", "a linear polynomial", "a constant polynomial"]),
            ("an expression with a variable under a radical (square root) is", "not a polynomial (fractional exponent 1/2)", ["always a polynomial", "a quadratic polynomial", "a monomial"]),
            ("the degree of a non-zero constant polynomial is", "0", ["1", "not defined", "-1"]),
            ("the expression √2 x + 5 is", "a linear polynomial (coefficient is √2, exponent of x is 1)", ["not a polynomial", "a quadratic polynomial", "an irrational expression"]),
            ("the expression 2√x + 5 is", "not a polynomial (exponent of x is 1/2)", ["a linear polynomial", "a polynomial of degree 1/2", "a binomial polynomial"]),
            ("the expression 5/x + 3 is", "not a polynomial (exponent of x is -1)", ["a linear polynomial", "a rational polynomial", "a monomial"]),
            ("the expression x² - 3/x² + 4 is", "not a polynomial (contains x^{-2})", ["a polynomial of degree 4", "a quadratic polynomial", "a trinomial polynomial"]),
            ("a polynomial of degree 0 has", "1 term (a non-zero constant)", ["0 terms", "2 terms", "infinitely many terms"])
        ],
        'tmpls': [
            "In coordinate geometry and algebra, {0}:",
            "Which of the following is correct regarding: {0}?",
            "State the fundamental algebraic rule: {0}:",
            "According to the definition of polynomials, {0}:",
            "Identify the correct mathematical fact: {0}:",
            "What is the condition on polynomials: {0}?",
            "Which statement accurately describes: {0}?",
            "Regarding algebraic expressions and polynomials, {0}:",
            "Determine the true rule: {0}:",
            "In algebra, it is strictly required that {0}:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand the core distinction.**\nAn algebraic expression combines variables and constants using addition, subtraction, multiplication, division, and exponents.\nA polynomial is a restricted algebraic expression where division by variables is prohibited and all exponents of variables must be whole numbers.\n\n**Step 2: Evaluate the statement.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 2: Radical coefficients vs Radical variables
    arch2 = {
        'data': [
            ("\\sqrt{5}x + 7", "Linear polynomial (degree 1)", ["Not a polynomial", "Quadratic polynomial", "Irrational polynomial of degree 1/2"]),
            ("5\\sqrt{x} + 7", "Not a polynomial", ["Linear polynomial", "Monomial", "Polynomial of degree 1/2"]),
            ("\\sqrt{2}x^2 - \\sqrt{3}x + 1", "Quadratic polynomial (degree 2)", ["Not a polynomial", "Linear polynomial", "Trinomial of degree 1"]),
            ("2x^2 - 3\\sqrt{x} + 1", "Not a polynomial", ["Quadratic polynomial", "Trinomial", "Polynomial of degree 2"]),
            ("\\frac{1}{\\sqrt{2}}x - 4", "Linear polynomial (degree 1)", ["Not a polynomial", "Rational non-polynomial", "Constant polynomial"]),
            ("\\frac{1}{x} + 4", "Not a polynomial", ["Linear polynomial", "Monomial", "Constant polynomial"]),
            ("\\pi x - 3", "Linear polynomial (degree 1)", ["Not a polynomial", "Transcendental non-polynomial", "Quadratic polynomial"]),
            ("x^\\pi - 3", "Not a polynomial", ["Linear polynomial", "Polynomial of degree 3.14", "Binomial polynomial"]),
            ("0.75x + 1.25", "Linear polynomial (degree 1)", ["Not a polynomial", "Fractional non-polynomial", "Monomial"]),
            ("x^{0.5} + 2", "Not a polynomial", ["Linear polynomial", "Binomial polynomial", "Monomial"])
        ],
        'tmpls': [
            "Which description correctly classifies \\( p(x) = {0} \\)?",
            "Classify the expression \\( {0} \\):",
            "What is the algebraic nature of \\( {0} \\)?",
            "Determine the classification of \\( {0} \\):",
            "How is \\( {0} \\) categorized in polynomial algebra?",
            "Identify the correct category for \\( {0} \\):",
            "In polynomial theory, the expression \\( {0} \\) is a:",
            "Which statement correctly classifies \\( {0} \\)?",
            "Is \\( {0} \\) a polynomial and what is its degree?",
            "The expression \\( {0} \\) represents a:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Check where the radical or real constant appears.**\nCoefficients can be any real numbers (including \\( \\sqrt{{2}}, \\pi, 0.75 \\)).\nHowever, the variable \\( x \\) itself must have a non-negative integer exponent.\n\n**Step 2: Inspect \\( {item[0]} \\).**\nCheck if the variable \\( x \\) has whole number exponents.\n\n**Step 3: State the classification.**\nIt is: {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Identifying the reason why an expression is NOT a polynomial
    arch3 = {
        'data': [
            ("x + \\frac{2}{x}", "The exponent of x in 2/x is -1, which is not a whole number", ["The coefficient 2 is an integer", "It has 2 terms", "It contains addition"]),
            ("3\\sqrt{x} + 5", "The exponent of x is 1/2, which is not a whole number", ["The coefficient 3 is not an integer", "5 is a constant", "It has degree 1"]),
            ("x^2 + \\frac{1}{x^2}", "The second term has power -2, which is a negative integer", ["The first term has degree 2", "The coefficients are equal", "It has two terms"]),
            ("x^{3/4} - 2x + 1", "The exponent 3/4 is a fraction, not a whole number", ["It has 3 terms", "The constant term is 1", "The leading term has power > 0"]),
            ("\\frac{x^2 - 4}{x - 2} \\text{ without cancellation}", "It is a rational expression with variable in denominator", ["The numerator is quadratic", "The denominator is linear", "It has two zeroes"]),
            ("4x^{-3} + 7", "The exponent -3 is negative", ["4 is a positive coefficient", "7 is a constant", "It is a binomial"]),
            ("2x^2 + 3x^{1/3} - 6", "The term 3x^{1/3} has a fractional exponent 1/3", ["2x² has exponent 2", "-6 is negative", "It has 3 terms"]),
            ("\\sqrt[3]{x} - 8", "The exponent is 1/3, which is not a non-negative integer", ["-8 is a constant", "It is a binomial", "It has degree 3"]),
            ("\\frac{3}{2x + 1}", "The variable occurs in the denominator (rational expression)", ["3 is a constant", "The denominator is linear", "It has degree 1"]),
            ("x^{-1} + x^0", "The exponent of the first term is -1", ["x^0 equals 1", "It has 2 terms", "The coefficients are 1"])
        ],
        'tmpls': [
            "Why is the expression \\( {0} \\) NOT a polynomial?",
            "State the exact mathematical reason why \\( {0} \\) fails to be a polynomial:",
            "Which factor disqualifies \\( {0} \\) from being a polynomial?",
            "What prevents \\( {0} \\) from being classified as a polynomial?",
            "The expression \\( {0} \\) is not a polynomial because:",
            "Identify the violation in the definition of a polynomial in \\( {0} \\):",
            "Why does \\( {0} \\) not qualify as a polynomial in \\( x \\)?",
            "What makes \\( {0} \\) merely an algebraic expression and not a polynomial?",
            "Explain why \\( {0} \\) is not a polynomial:",
            "The expression \\( {0} \\) cannot be a polynomial since:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the definition of a polynomial.**\nA polynomial in variable \\( x \\) is an expression of the form \\( a_n x^n + a_{{n-1}} x^{{n-1}} + \\dots + a_0 \\) where \\( n \\) is a non-negative integer and each exponent is in \\( \\{{0, 1, 2, \\dots\\}} \\).\n\n**Step 2: Pinpoint the non-compliant term.**\nIn \\( {item[0]} \\), identify the term violating this exponent rule.\n\n**Step 3: State the reason.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Value of exponent n for which expression is a polynomial
    arch4 = {
        'data': [
            ("x^{n - 3} + 5x - 2", "n must be an integer ≥ 3", ["n can be any real number", "n must be ≤ 3", "n = 0"]),
            ("x^{2n - 6} + 4", "n must be an integer ≥ 3", ["n can be any fraction", "n must be negative", "n = 2"]),
            ("x^{5 - n} + x^2", "n must be an integer ≤ 5", ["n must be ≥ 5", "n can be any fraction", "n = 6"]),
            ("3x^{n/2} + 7", "n must be a non-negative even integer (0, 2, 4, ...)", ["n can be any integer", "n must be odd", "n can be any positive fraction"]),
            ("x^{n/3} - 4x + 1", "n must be a non-negative multiple of 3 (0, 3, 6, ...)", ["n must be any integer", "n = 1", "n can be negative"]),
            ("x^{n + 1} + 3", "n must be an integer ≥ -1", ["n must be ≥ 1", "n can be any real number", "n = -2"]),
            ("x^{4 - 2n} + 9", "n must be an integer ≤ 2", ["n must be ≥ 2", "n can be any fraction", "n = 3"]),
            ("x^{n - 1} + x^{2 - n}", "n must be either 1 or 2", ["n can be any integer", "n ≥ 2", "n ≤ 1"]),
            ("x^{n - 2} + x^{3 - n}", "n must be 2 or 3", ["n can be any real number", "n = 0", "n ≥ 3"]),
            ("x^{n} + \\frac{1}{x^n}", "never a polynomial for non-zero n", ["always a polynomial", "a polynomial when n > 0", "a polynomial when n is even"])
        ],
        'tmpls': [
            "For what condition on \\( n \\) is the expression \\( {0} \\) a polynomial in \\( x \\)?",
            "Under what values of \\( n \\) does \\( {0} \\) represent a valid polynomial?",
            "Find the condition on \\( n \\) such that \\( {0} \\) is a polynomial:",
            "The expression \\( {0} \\) is a polynomial if and only if:",
            "Determine the requirement on \\( n \\) for \\( {0} \\) to be a polynomial in \\( x \\):",
            "What must \\( n \\) satisfy for \\( {0} \\) to qualify as a polynomial?",
            "Identify the restriction on \\( n \\) so that \\( {0} \\) is a polynomial:",
            "For \\( {0} \\) to be a polynomial, \\( n \\) must be:",
            "Which condition on \\( n \\) ensures that \\( {0} \\) is a polynomial in \\( x \\)?",
            "State the necessary values of \\( n \\) for \\( {0} \\) to be a polynomial:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Set each exponent to be a non-negative integer.**\nAll powers of \\( x \\) must belong to the set \\( \\{{0, 1, 2, 3, \\dots\\}} \\).\n\n**Step 2: Solve the inequalities for \\( n \\).**\nSolve the exponent constraints simultaneously.\n\n**Step 3: State the condition on \\( n \\).**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Degrees of combinations of polynomials (sum, product)
    arch5 = {
        'data': [
            ("sum of two linear polynomials p(x) and q(x)", "at most degree 1 (can be degree 0 or zero polynomial if linear terms cancel)", ["strictly degree 2", "always degree 1", "degree 0 always"]),
            ("product of two linear polynomials (ax + b)(cx + d) with a ≠ 0, c ≠ 0", "strictly degree 2 (quadratic)", ["degree 1", "degree 3", "degree 0"]),
            ("product of a linear polynomial and a quadratic polynomial", "degree 3 (cubic)", ["degree 2", "degree 1", "degree 6"]),
            ("difference of two linear polynomials 3x + 5 and 3x - 2", "degree 0 (constant polynomial 7)", ["degree 1", "degree 2", "not defined"]),
            ("sum of a quadratic polynomial and a linear polynomial", "degree 2 (quadratic)", ["degree 3", "degree 1", "degree 0"]),
            ("quotient of two polynomials p(x)/q(x)", "not necessarily a polynomial (rational function)", ["always a polynomial", "always linear", "always of degree deg(p) - deg(q)"]),
            ("degree of p(x) * q(x) in general", "deg(p) + deg(q)", ["deg(p) * deg(q)", "max(deg(p), deg(q))", "deg(p) - deg(q)"]),
            ("degree of p(x) + q(x) when deg(p) ≠ deg(q)", "max(deg(p), deg(q))", ["deg(p) + deg(q)", "deg(p) - deg(q)", "0"]),
            ("degree of (ax + b)³ where a ≠ 0", "degree 3 (cubic)", ["degree 1", "degree 2", "degree 4"]),
            ("degree of (ax + b)² where a ≠ 0", "degree 2 (quadratic)", ["degree 1", "degree 4", "degree 0"])
        ],
        'tmpls': [
            "What is the degree of the {0}?",
            "In polynomial algebra, the {0} has degree:",
            "Determine the degree resulting from the {0}:",
            "Which statement correctly gives the degree of the {0}?",
            "Find the degree of the {0}:",
            "State the degree of the polynomial formed by the {0}:",
            "According to algebra theorems, the {0} yields a polynomial of degree:",
            "What can be concluded about the degree of the {0}?",
            "Identify the correct degree for the {0}:",
            "The operation '{0}' results in a degree of:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall algebraic rules for degrees.**\n- For product: \\( \\deg(p \\cdot q) = \\deg(p) + \\deg(q) \\)\n- For sum: \\( \\deg(p + q) \\le \\max(\\deg(p), \\deg(q)) \\)\n\n**Step 2: Apply to '{item[0]}'.**\nAnalyze the specific operations and whether cancellation of leading terms can occur.\n\n**Step 3: State the resulting degree.**\nIt is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Polynomials in one variable vs several variables
    arch6 = {
        'data': [
            ("3x^2 + 5x - 7", "Polynomial in one variable (x)", ["Polynomial in two variables", "Not a polynomial", "Rational expression"]),
            ("2x + 3y - 5", "Polynomial in two variables (x, y)", ["Polynomial in one variable", "Not a polynomial", "Linear equation in one variable"]),
            ("x^2 + y^2 + z^2 - 3xyz", "Polynomial in three variables (x, y, z)", ["Polynomial in one variable", "Not a polynomial", "Quadratic polynomial in one variable"]),
            ("4x^3 - 2x^2 + x - 9", "Polynomial in one variable (x)", ["Polynomial in two variables", "Polynomial of degree 4", "Not a polynomial"]),
            ("xy + x - 2y + 4", "Polynomial in two variables (x, y)", ["Polynomial in one variable", "Linear polynomial", "Not a polynomial"]),
            ("5t^2 - 3t + 8", "Polynomial in one variable (t)", ["Polynomial in three variables", "Not a polynomial", "Rational expression"]),
            ("u^3 + v^3 + w^3", "Polynomial in three variables (u, v, w)", ["Polynomial in one variable", "Not a polynomial", "Degree 1 polynomial"]),
            ("7y - 12", "Polynomial in one variable (y)", ["Polynomial in two variables", "Not a polynomial", "Constant polynomial"]),
            ("a^2b + ab^2 + 5", "Polynomial in two variables (a, b)", ["Polynomial in one variable", "Not a polynomial", "Linear polynomial"]),
            ("m^4 - 16", "Polynomial in one variable (m)", ["Polynomial in four variables", "Not a polynomial", "Rational expression"])
        ],
        'tmpls': [
            "Classify \\( {0} \\) according to the number of variables it contains:",
            "How many variables are present in the polynomial \\( {0} \\)?",
            "The expression \\( {0} \\) is correctly identified as a:",
            "Determine the classification of \\( {0} \\) by variable count:",
            "In which category of polynomials does \\( {0} \\) fall?",
            "Identify the number of variables in the polynomial \\( {0} \\):",
            "What type of polynomial is \\( {0} \\) based on its variables?",
            "The polynomial \\( {0} \\) is a:",
            "Classify the algebraic expression \\( {0} \\):",
            "State the variable classification for \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Count distinct variable letters.**\nInspect the expression \\( {item[0]} \\) and count distinct letters representing variables.\n\n**Step 2: Verify all powers are whole numbers.**\nEnsure the expression satisfies the polynomial definition.\n\n**Step 3: State the classification.**\nIt is a {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Multiple-choice classification of mixed expressions
    arch7 = {
        'data': [
            ("Which of the following is a polynomial?", "x² + 2x + 1", ["x + 1/x", "√x + 3", "x^{1/2} - 4"]),
            ("Which of the following is NOT a polynomial?", "3√x + 7", ["3x + 7", "x² - 5", "√3 x + 7"]),
            ("Which of the following is a linear polynomial in one variable?", "5x - 4", ["5x² - 4", "5/x - 4", "5x + 3y - 4"]),
            ("Which of the following is a binomial of degree 1?", "4x - 9", ["4x", "4x² - 9", "4x + 3y - 9"]),
            ("Which of the following expressions has degree 1?", "\\frac{x}{3} + 5", ["\\frac{3}{x} + 5", "x^2 + 1", "3"]),
            ("Which of the following is a polynomial with degree 0?", "9", ["9x", "9/x", "0"]),
            ("Which of the following has an undefined degree?", "0", ["1", "x", "1/x"]),
            ("Which of the following is a monomial of degree 1?", "-7x", ["-7", "-7x²", "-7x + 1"]),
            ("Which expression is a polynomial with irrational coefficients?", "\\sqrt{2}x + \\sqrt{3}", ["\\sqrt{2x} + 3", "2\\sqrt{x} + 3", "\\frac{2}{x} + \\sqrt{3}"]),
            ("Which of the following is NOT an algebraic polynomial in x?", "x^{-2} + 3x + 1", ["x^2 + 3x + 1", "3x + 1", "x^3 - 1"])
        ],
        'tmpls': [
            "{0}",
            "Solve the following identification problem: {0}",
            "From the given options, answer: {0}",
            "Carefully analyze and answer: {0}",
            "In polynomial classification: {0}",
            "Choose the correct option: {0}",
            "Determine the correct choice: {0}",
            "Select the correct answer: {0}",
            "Identify the correct option: {0}",
            "Which option correctly answers: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Check definition of polynomial for each option.**\nExponents of variables must be whole numbers \\( \\{{0, 1, 2, \\dots\\}} \\). No variables in denominators or under radicals.\n\n**Step 2: Inspect candidate options.**\nEvaluate each option against the question criteria: '{item[0]}'.\n\n**Step 3: State the correct option.**\nThe correct choice is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])

if __name__ == "__main__":
    q1 = gen_2_1_1()
    q2 = gen_2_1_2()
    print(f"gen_2_1_1: {len(q1)} questions generated")
    print(f"gen_2_1_2: {len(q2)} questions generated")
