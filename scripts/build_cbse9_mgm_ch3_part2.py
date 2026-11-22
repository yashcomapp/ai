# scripts/build_cbse9_mgm_ch3_part2.py
# Subtopics:
# 3.2.1: Non-terminating non-repeating numbers (80 Qs)
# 3.2.2: Constructing √2, √3, √5 using Pythagoras spiral method (80 Qs)
# 3.2.3: Locating √x on number line (80 Qs)

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 3
CH_NAME = "The World of Numbers"

# ==============================================================================
# SUBTOPIC 3.2.1: Non-terminating non-repeating numbers
# ==============================================================================
def gen_3_2_1():
    tc = "CBSE-9-MGM-3-3.2.1"
    tname = "Non-terminating non-repeating numbers"

    # Arch 0: Fundamental definition of irrational numbers
    arch0 = {
        'data': [
            ("A number is called irrational if its decimal expansion is:", "non-terminating and non-recurring (non-repeating)", ["terminating", "non-terminating recurring", "an integer"]),
            ("Which of the following is an irrational number?", "√7", ["√4", "3/5", "0.333..."]),
            ("The square root of any positive integer that is not a perfect square is:", "an irrational number", ["a rational fraction", "an integer", "a terminating decimal"]),
            ("The number π (pi) is classified as:", "an irrational number", ["a rational number", "an integer", "a natural number"]),
            ("Why is π irrational while 22/7 is rational?", "22/7 is a ratio of two integers p/q, whereas π has an infinite non-terminating non-repeating decimal expansion", ["π is an integer", "22/7 is an approximation of √2", "Both are rational"]),
            ("Which of the following decimal representations is irrational?", "0.101001000100001...", ["0.10101010...", "0.10", "1/10"]),
            ("The cube root of a number that is not a perfect cube is:", "an irrational number", ["a rational number", "a natural number", "a whole number"]),
            ("Which Greek school of mathematicians first discovered irrational numbers around 400 BC?", "The Pythagoreans", ["The Euclideans", "The Archimedeans", "The Babylonians"]),
            ("Which specific number was first proved to be irrational by the Pythagoreans?", "√2", ["π", "√3", "√5"]),
            ("Can an irrational number be written in the form p/q where p and q are integers and q ≠ 0?", "No, never", ["Yes, always", "Only when p = 0", "Only for square roots"])
        ],
        'tmpls': [
            "{0}",
            "In real number theory: {0}",
            "Regarding irrational numbers: {0}",
            "Choose the correct mathematical statement: {0}",
            "Identify the accurate fact: {0}",
            "According to the properties of real numbers: {0}",
            "Select the correct answer: {0}",
            "Which option correctly answers: {0}",
            "Determine the true statement: {0}",
            "What is the mathematical truth regarding: {0}?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the definition of an irrational number.**\nA real number is called irrational if it cannot be written in the form \\( \\frac{{p}}{{q}} \\), where \\( p \\) and \\( q \\) are integers and \\( q \\neq 0 \\). Equivalently, its decimal expansion is non-terminating and non-recurring.\n\n**Step 2: Evaluate the statement.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Classifying square roots as rational vs irrational
    arch1 = {
        'data': [
            ("\\sqrt{23}", "Irrational (23 is not a perfect square)", ["Rational", "Integer", "Terminating"]),
            ("\\sqrt{225}", "Rational (\\sqrt{225} = 15)", ["Irrational", "Non-terminating non-repeating", "Surd"]),
            ("\\sqrt{49}", "Rational (\\sqrt{49} = 7)", ["Irrational", "Non-terminating recurring", "Fraction"]),
            ("\\sqrt{12}", "Irrational (\\sqrt{12} = 2\\sqrt{3})", ["Rational", "Integer", "Terminating"]),
            ("\\sqrt{100}", "Rational (\\sqrt{100} = 10)", ["Irrational", "Surd", "Non-terminating"]),
            ("\\sqrt{8}", "Irrational (\\sqrt{8} = 2\\sqrt{2})", ["Rational", "Integer", "Whole number"]),
            ("\\sqrt{169}", "Rational (\\sqrt{169} = 13)", ["Irrational", "Non-terminating non-repeating", "Surd"]),
            ("\\sqrt{50}", "Irrational (\\sqrt{50} = 5\\sqrt{2})", ["Rational", "Integer", "Terminating"]),
            ("\\sqrt{0.04}", "Rational (\\sqrt{0.04} = 0.2 = 1/5)", ["Irrational", "Non-terminating", "Surd"]),
            ("\\sqrt{0.4}", "Irrational (\\sqrt{0.4} = \\sqrt{2/5} = \\frac{\\sqrt{10}}{5})", ["Rational", "Integer", "Terminating"])
        ],
        'tmpls': [
            "Classify the number \\( {0} \\) as rational or irrational.",
            "Is the number \\( {0} \\) rational or irrational?",
            "Determine whether \\( {0} \\) is a rational or irrational number:",
            "In the real number system, \\( {0} \\) is:",
            "What type of real number is \\( {0} \\)?",
            "Identify the nature of \\( {0} \\):",
            "Evaluate whether \\( {0} \\) is rational or irrational:",
            "The numerical expression \\( {0} \\) represents a/an:",
            "Which classification correctly describes \\( {0} \\)?",
            "State whether \\( {0} \\) is rational or irrational:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Check if the number under the radical is a perfect square.**\nIf \\( n \\) is a perfect square, \\( \\sqrt{{n}} \\) is a whole number (rational).\nIf \\( n \\) is not a perfect square, \\( \\sqrt{{n}} \\) is irrational.\n\n**Step 2: Inspect \\( {item[0]} \\).**\nEvaluate the expression.\n\n**Step 3: State the classification.**\nIt is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Finding an irrational number between two rational numbers
    arch2 = {
        'data': [
            ("1/7", "2/7", "0.2010010001...", ["0.15", "0.29", "0.333..."]),
            ("1", "2", "\\sqrt{2} \\approx 1.414", ["1.5", "1.75", "2.5"]),
            ("2", "3", "\\sqrt{5} \\approx 2.236", ["2.5", "2.75", "3.2"]),
            ("3", "4", "\\sqrt{10} \\approx 3.162", ["3.5", "3.8", "4.2"]),
            ("0.1", "0.2", "0.15010010001...", ["0.15", "0.25", "0.05"]),
            ("5", "6", "\\sqrt{26} \\approx 5.099", ["5.5", "5.8", "6.2"]),
            ("4", "5", "\\sqrt{17} \\approx 4.123", ["4.5", "4.8", "5.1"]),
            ("0.2", "0.3", "0.21010010001...", ["0.25", "0.35", "0.15"]),
            ("1/2", "3/4", "\\frac{1}{\\sqrt{3}} \\approx 0.577", ["0.6", "0.7", "0.8"]),
            ("6", "7", "\\sqrt{37} \\approx 6.082", ["6.5", "6.8", "7.2"])
        ],
        'tmpls': [
            "Find an irrational number lying strictly between \\( {0} \\) and \\( {1} \\).",
            "Which of the following is an irrational number situated between \\( {0} \\) and \\( {1} \\)?",
            "Identify an irrational number in the interval \\( ({0}, {1}) \\):",
            "Determine an irrational value located between \\( {0} \\) and \\( {1} \\):",
            "A non-terminating non-repeating number between \\( {0} \\) and \\( {1} \\) is:",
            "Which value represents an irrational number between \\( {0} \\) and \\( {1} \\)?",
            "Select an irrational number lying between \\( {0} \\) and \\( {1} \\):",
            "What is an irrational number between \\( {0} \\) and \\( {1} \\)?",
            "Find a surd or non-recurring decimal between \\( {0} \\) and \\( {1} \\):",
            "Choose the irrational number positioned between \\( {0} \\) and \\( {1} \\):"
        ],
        'calc': lambda item: (
            item[2],
            item[3],
            f"**Step 1: Convert the bounds to decimal approximations.**\nInterval is \\( ({item[0]}, {item[1]}) \\).\n\n**Step 2: Construct or identify an irrational number.**\nA non-terminating non-repeating decimal or non-perfect square root whose value falls strictly within the interval.\n\n**Step 3: State the irrational number.**\nThe irrational number is \\( {item[2]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Rational + Irrational, Rational * Irrational operations
    arch3 = {
        'data': [
            ("The sum of a rational number and an irrational number is always:", "an irrational number", ["a rational number", "an integer", "zero"]),
            ("The difference of a rational number and an irrational number is always:", "an irrational number", ["a rational number", "positive", "an integer"]),
            ("The product of a non-zero rational number and an irrational number is always:", "an irrational number", ["a rational number", "an integer", "zero"]),
            ("The quotient of a non-zero rational number and an irrational number is always:", "an irrational number", ["a rational number", "an integer", "undefined"]),
            ("The sum of two irrational numbers can be:", "either rational or irrational (e.g. √2 + (-√2) = 0 is rational)", ["always irrational", "always rational", "never an integer"]),
            ("The product of two irrational numbers can be:", "either rational or irrational (e.g. √2 * √2 = 2 is rational, √2 * √3 = √6 is irrational)", ["always irrational", "always rational", "always 1"]),
            ("Is 2 + √3 rational or irrational?", "Irrational (sum of rational 2 and irrational √3)", ["Rational", "Integer", "Terminating"]),
            ("Is 5 - √7 rational or irrational?", "Irrational (difference of rational 5 and irrational √7)", ["Rational", "Integer", "Fraction"]),
            ("Is (3 + √23) - √23 rational or irrational?", "Rational (simplifies to 3)", ["Irrational", "Surd", "Undefined"]),
            ("Is (2√7)/(7√7) rational or irrational?", "Rational (simplifies to 2/7)", ["Irrational", "Integer", "Undefined"])
        ],
        'tmpls': [
            "{0}",
            "In real number operations: {0}",
            "Regarding operations between rational and irrational numbers: {0}",
            "Choose the correct statement: {0}",
            "Identify the accurate fact: {0}",
            "Which statement correctly describes: {0}?",
            "According to algebra of real numbers: {0}",
            "Determine the correct answer: {0}",
            "Select the valid property: {0}",
            "State the mathematical truth: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall algebraic rules for real numbers.**\n- Rational \\( \\pm \\) Irrational = Irrational\n- Non-zero Rational \\( \\times \\) Irrational = Irrational\n- Non-zero Rational \\( \\div \\) Irrational = Irrational\n- Operations between two irrationals can produce rational or irrational results.\n\n**Step 2: Evaluate the statement.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Algebraic simplification of surd expressions (e.g. (3 + √3)(3 - √3))
    arch4 = {
        'data': [
            ("(3 + \\sqrt{3})(3 - \\sqrt{3})", "6 (rational)", ["9", "3", "3\\sqrt{3}"]),
            ("(5 + \\sqrt{5})(5 - \\sqrt{5})", "20 (rational)", ["25", "5", "10\\sqrt{5}"]),
            ("(\\sqrt{5} + \\sqrt{2})^2", "7 + 2\\sqrt{10} (irrational)", ["7", "10", "7 + \\sqrt{10}"]),
            ("(\\sqrt{3} + \\sqrt{2})(\\sqrt{3} - \\sqrt{2})", "1 (rational)", ["5", "2", "\\sqrt{6}"]),
            ("(\\sqrt{7} - \\sqrt{2})(\\sqrt{7} + \\sqrt{2})", "5 (rational)", ["9", "14", "2\\sqrt{14}"]),
            ("(2 + \\sqrt{3})^2", "7 + 4\\sqrt{3} (irrational)", ["7", "13", "7 + 2\\sqrt{3}"]),
            ("(4 - \\sqrt{2})(4 + \\sqrt{2})", "14 (rational)", ["16", "2", "8\\sqrt{2}"]),
            ("(6 + \\sqrt{2})(6 - \\sqrt{2})", "34 (rational)", ["36", "4", "12\\sqrt{2}"]),
            ("(\\sqrt{11} - \\sqrt{7})(\\sqrt{11} + \\sqrt{7})", "4 (rational)", ["18", "77", "\\sqrt{77}"]),
            ("(\\sqrt{5} - \\sqrt{3})^2", "8 - 2\\sqrt{15} (irrational)", ["8", "2", "8 - \\sqrt{15}"])
        ],
        'tmpls': [
            "Simplify the expression \\( {0} \\) and determine whether the result is rational or irrational.",
            "What is the simplified value of \\( {0} \\)?",
            "Evaluate \\( {0} \\):",
            "Calculate the product \\( {0} \\):",
            "Simplify: \\( {0} \\):",
            "Find the numerical value of \\( {0} \\):",
            "The expansion of \\( {0} \\) simplifies to:",
            "Determine the result of \\( {0} \\):",
            "Compute \\( {0} \\):",
            "What is the simplified form of \\( {0} \\)?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Use algebraic identity.**\nApply \\( (a+b)(a-b) = a^2 - b^2 \\) or \\( (a+b)^2 = a^2 + 2ab + b^2 \\).\n\n**Step 2: Carry out numerical squaring.**\nSquare the terms and collect like terms.\n\n**Step 3: State the simplified value.**\nThe simplified result is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Density of irrationals
    arch5 = {
        'data': [
            ("How many irrational numbers exist between any two distinct rational numbers?", "Infinitely many irrational numbers", ["None", "Only 1", "A finite number"]),
            ("How many irrational numbers exist between any two distinct irrational numbers?", "Infinitely many irrational numbers", ["None", "Only 1", "Exactly 2"]),
            ("The collection of all rational numbers together with all irrational numbers forms:", "The set of real numbers (ℝ)", ["The set of integers (ℤ)", "The set of complex numbers only", "The set of whole numbers (𝕎)"]),
            ("Is every real number an irrational number?", "No, because real numbers include rational numbers as well", ["Yes, always", "Only positive real numbers", "Only negative real numbers"]),
            ("Is every irrational number a real number?", "Yes, all irrational numbers are real numbers", ["No, they are imaginary numbers", "Only if positive", "Only if rationalizable"]),
            ("On the real number line, every point corresponds to:", "a unique real number", ["only rational numbers", "only integers", "two different numbers"]),
            ("A decimal number with pattern 0.202002000200002... is:", "an irrational number (non-terminating non-repeating)", ["a rational number", "a recurring decimal", "an integer"]),
            ("If a number can be plotted on the number line, it must be:", "a real number (either rational or irrational)", ["an integer only", "a rational number only", "an imaginary number"]),
            ("Which number is irrational?", "√11", ["√9", "√25", "√64"]),
            ("Between √2 and √3, how many real numbers exist?", "Infinitely many (both rational and irrational)", ["None", "Only 1", "Exactly 5"])
        ],
        'tmpls': [
            "{0}",
            "In the foundation of number systems: {0}",
            "Regarding real numbers on the number line: {0}",
            "Choose the correct statement: {0}",
            "Identify the accurate fact: {0}",
            "Which statement correctly describes: {0}?",
            "According to the Dedekind-Cantor continuum: {0}",
            "Determine the correct answer: {0}",
            "Select the valid mathematical principle: {0}",
            "State the property: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the real number line continuum.**\nThe set of real numbers \\( \\mathbb{{R}} \\) is the union of rational numbers \\( \\mathbb{{Q}} \\) and irrational numbers \\( \\mathbb{{I}} \\). Both sets are dense on the number line.\n\n**Step 2: Evaluate the statement.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Identifying whether expressions simplify to rational or irrational
    arch6 = {
        'data': [
            ("2 - \\sqrt{5}", "Irrational", ["Rational", "Integer", "Terminating"]),
            ("(3 + \\sqrt{23}) - \\sqrt{23}", "Rational (equals 3)", ["Irrational", "Surd", "Undefined"]),
            ("\\frac{2\\sqrt{7}}{7\\sqrt{7}}", "Rational (equals 2/7)", ["Irrational", "Surd", "Integer"]),
            ("\\frac{1}{\\sqrt{2}}", "Irrational", ["Rational", "Integer", "Terminating"]),
            ("2\\pi", "Irrational", ["Rational", "Integer", "Fraction"]),
            ("\\sqrt{2} + 21", "Irrational", ["Rational", "Integer", "Terminating"]),
            ("(\\sqrt{2} + \\sqrt{3})^2", "Irrational (equals 5 + 2\\sqrt{6})", ["Rational", "Integer", "Terminating"]),
            ("(\\sqrt{5} - 2)(\\sqrt{5} + 2)", "Rational (equals 1)", ["Irrational", "Surd", "Fraction"]),
            ("\\sqrt{18}/\\sqrt{2}", "Rational (equals \\sqrt{9} = 3)", ["Irrational", "Surd", "Fraction"]),
            ("\\sqrt{27}/\\sqrt{3}", "Rational (equals \\sqrt{9} = 3)", ["Irrational", "Surd", "Fraction"])
        ],
        'tmpls': [
            "Classify the expression \\( {0} \\) as rational or irrational.",
            "Determine whether \\( {0} \\) simplifies to a rational or irrational number:",
            "Is the value of \\( {0} \\) rational or irrational?",
            "In real arithmetic, \\( {0} \\) is:",
            "What type of number does \\( {0} \\) represent?",
            "Identify the nature of \\( {0} \\):",
            "After simplification, \\( {0} \\) is:",
            "The simplified result of \\( {0} \\) is:",
            "Evaluate whether \\( {0} \\) is rational or irrational:",
            "Classify \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Simplify the expression algebraically.**\nCarry out operations, cancel common surds or apply identities.\n\n**Step 2: Check if any non-canceling irrational surd remains.**\nIf a radical of a non-perfect square remains, the expression is irrational.\n\n**Step 3: State the classification.**\nIt is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Approximations and bounds of famous irrationals
    arch7 = {
        'data': [
            ("The value of √2 correct to three decimal places is approximately:", "1.414", ["1.412", "1.416", "1.732"]),
            ("The value of √3 correct to three decimal places is approximately:", "1.732", ["1.723", "1.735", "1.414"]),
            ("The value of √5 correct to three decimal places is approximately:", "2.236", ["2.232", "2.245", "2.500"]),
            ("Between which two consecutive integers does √7 lie?", "Between 2 and 3 (since 4 < 7 < 9)", ["Between 1 and 2", "Between 3 and 4", "Between 4 and 5"]),
            ("Between which two consecutive integers does √11 lie?", "Between 3 and 4 (since 9 < 11 < 16)", ["Between 2 and 3", "Between 4 and 5", "Between 5 and 6"]),
            ("Between which two consecutive integers does √19 lie?", "Between 4 and 5 (since 16 < 19 < 25)", ["Between 3 and 4", "Between 5 and 6", "Between 2 and 3"]),
            ("Between which two consecutive integers does √30 lie?", "Between 5 and 6 (since 25 < 30 < 36)", ["Between 4 and 5", "Between 6 and 7", "Between 3 and 4"]),
            ("The integer part (floor) of √50 is:", "7 (since 7² = 49 < 50 < 8² = 64)", ["6", "8", "5"]),
            ("The integer part (floor) of √80 is:", "8 (since 8² = 64 < 80 < 9² = 81)", ["7", "9", "80"]),
            ("The value of π correct to two decimal places is approximately:", "3.14", ["3.12", "3.16", "3.41"])
        ],
        'tmpls': [
            "{0}",
            "In approximation of surds: {0}",
            "Regarding irrational bounds: {0}",
            "Choose the correct approximation or bound: {0}",
            "Identify the accurate fact: {0}",
            "Select the correct answer: {0}",
            "Determine the correct option: {0}",
            "Which option correctly answers: {0}",
            "Solve the following bounding problem: {0}",
            "Compute the required bound: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Compare with perfect squares.**\nFind consecutive perfect squares bounding the number: \\( n^2 < x < (n+1)^2 \\).\n\n**Step 2: Take square roots.**\n\\( n < \\sqrt{{x}} < n+1 \\).\n\n**Step 3: State the bound or approximation.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 3.2.2: Constructing √2, √3, √5 using Pythagoras spiral method
# ==============================================================================
def gen_3_2_2():
    tc = "CBSE-9-MGM-3-3.2.2"
    tname = "Constructing √2, √3, √5 using Pythagoras spiral method"

    # Arch 0: Geometric construction of √2 on the number line
    arch0 = {
        'data': [
            ("In constructing √2 on a number line, a right-angled triangle is drawn with base 1 unit from 0 to 1 and perpendicular height:", "1 unit", ["2 units", "√2 units", "0.5 units"]),
            ("The hypotenuse of a right triangle with legs of length 1 unit and 1 unit is:", "√2 units", ["2 units", "1 unit", "√3 units"]),
            ("To transfer √2 from the hypotenuse onto the number line, a compass is set with center at origin (0) and radius:", "√2 (length of the hypotenuse)", ["1 unit", "2 units", "0.5 units"]),
            ("The point representing √2 on the number line lies between which two consecutive integers?", "Between 1 and 2 (since 1 < 1.414 < 2)", ["Between 0 and 1", "Between 2 and 3", "Between 3 and 4"]),
            ("In the Pythagoras theorem equation for constructing √2, the formula used is:", "OB² = 1² + 1² = 2 => OB = √2", ["OB² = 1 + 2 = 3", "OB² = 2² - 1² = 3", "OB = 1 + 1 = 2"]),
            ("What is the length of the diagonal of a square with side length 1 unit?", "√2 units", ["1 unit", "2 units", "√3 units"]),
            ("If a unit square OABC is constructed on the number line with OA on the line from 0 to 1, the diagonal OB has length:", "√2 units", ["1 unit", "1.5 units", "2 units"]),
            ("When an arc with center O(0) and radius OB = √2 is drawn, it cuts the number line at point P representing:", "√2", ["1", "2", "1.5"]),
            ("What is the decimal approximation of the point marking √2 on the number line?", "1.414", ["1.732", "2.236", "1.500"]),
            ("Can √2 be represented as an exact point on the real number line?", "Yes, geometrically via compass and straightedge construction", ["No, because it is irrational", "Only approximately", "Only using computer software"])
        ],
        'tmpls': [
            "{0}",
            "Regarding geometric construction of √2 on the number line: {0}",
            "In compass and ruler constructions: {0}",
            "Choose the correct fact about constructing √2: {0}",
            "Identify the accurate geometric step: {0}",
            "According to the Pythagoras construction method: {0}",
            "Select the correct answer: {0}",
            "Which option correctly describes: {0}?",
            "Determine the true statement: {0}",
            "State the geometric truth: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand construction of \\( \\sqrt{2} \\).**\nConstruct a right-angled triangle with base = 1 and perpendicular height = 1.\nBy Pythagoras theorem: \\( c = \\sqrt{{1^2 + 1^2}} = \\sqrt{2} \\).\n\n**Step 2: Transfer with compass.**\nSwing an arc with radius \\( \\sqrt{2} \\) centered at 0 to intersect the real number line.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Geometric construction of √3 from √2
    arch1 = {
        'data': [
            ("To construct √3 on the number line, a right triangle is drawn with base equal to √2 and perpendicular height equal to:", "1 unit", ["√2 units", "2 units", "3 units"]),
            ("The hypotenuse of a right triangle with base √2 and perpendicular 1 is:", "√3 units (since (√2)² + 1² = 2 + 1 = 3)", ["2 units", "√5 units", "3 units"]),
            ("The point representing √3 on the number line lies between which two consecutive integers?", "Between 1 and 2 (since 1 < 1.732 < 2)", ["Between 2 and 3", "Between 0 and 1", "Between 3 and 4"]),
            ("What is the approximate decimal coordinate of the point marking √3 on the number line?", "1.732", ["1.414", "2.236", "1.850"]),
            ("In the Pythagoras spiral, the hypotenuse of the triangle for √2 serves as the:", "base for the triangle constructing √3", ["perpendicular for √3", "hypotenuse for √3", "radius of the unit circle"]),
            ("If a right triangle has base √3 and perpendicular 1, what is the length of its hypotenuse?", "√4 = 2 units", ["√5 units", "3 units", "4 units"]),
            ("The point √3 on the number line lies closer to:", "2 than to 1 (since 1.732 is closer to 2)", ["1 than to 2", "0 than to 1", "exactly midway"]),
            ("Which sequence of hypotenuses is generated by successive right triangles each with perpendicular 1?", "√2, √3, √4, √5, √6, ...", ["√2, √4, √6, √8, ...", "1, 2, 3, 4, ...", "√1, √3, √5, √7, ..."]),
            ("The Pythagoras spiral method for constructing square roots of integers is also known as the:", "Spiral of Theodorus (or Square Root Spiral)", ["Fibonacci spiral", "Archimedean spiral", "Golden spiral"]),
            ("Who was Theodorus of Cyrene?", "A Greek philosopher and mathematician who constructed square roots up to √17 using right triangles", ["A Roman engineer", "A Babylonian astronomer", "An Indian astronomer"])
        ],
        'tmpls': [
            "{0}",
            "Regarding construction of √3 on the number line: {0}",
            "In the Square Root Spiral: {0}",
            "Choose the correct step in constructing √3: {0}",
            "Identify the accurate mathematical fact: {0}",
            "According to the Spiral of Theodorus: {0}",
            "Select the correct answer: {0}",
            "Which option correctly describes: {0}?",
            "Determine the true statement: {0}",
            "State the geometric fact: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand construction of \\( \\sqrt{3} \\).**\nTake the hypotenuse \\( \\sqrt{2} \\) as the base and erect a perpendicular of length 1 unit.\n\n**Step 2: Apply Pythagoras theorem.**\n\\[ \\text{{Hypotenuse}} = \\sqrt{{(\\sqrt{2})^2 + 1^2}} = \\sqrt{{2 + 1}} = \\sqrt{3} \\]\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 2: Direct construction of √5 (base 2, perpendicular 1)
    arch2 = {
        'data': [
            ("To construct √5 directly in a single step on the number line, one draws a right triangle with base 2 units from 0 to 2 and perpendicular height:", "1 unit (since 2² + 1² = 5)", ["2 units", "√5 units", "0.5 units"]),
            ("The hypotenuse of a right-angled triangle with base 2 units and perpendicular 1 unit is:", "√5 units", ["3 units", "√3 units", "5 units"]),
            ("The point representing √5 on the number line lies between which two consecutive integers?", "Between 2 and 3 (since 2 < 2.236 < 3)", ["Between 1 and 2", "Between 3 and 4", "Between 4 and 5"]),
            ("What is the decimal approximation of √5 on the number line?", "2.236", ["2.414", "2.732", "2.500"]),
            ("Can √5 also be constructed using base 1 and perpendicular 2?", "Yes, because 1² + 2² = 1 + 4 = 5", ["No, base must always be longer", "No, base must be √4", "Only with base 2"]),
            ("To plot -√5 on the number line, the arc of radius √5 from origin is drawn:", "to the left of origin (negative direction)", ["to the right of origin", "above the origin", "below the origin"]),
            ("To construct √10 directly in one step, what base and perpendicular lengths can be used?", "base = 3 units, perpendicular = 1 unit (since 3² + 1² = 10)", ["base = 2, perpendicular = 2", "base = 5, perpendicular = 2", "base = 4, perpendicular = 1"]),
            ("To construct √13 directly in one step, what integer leg lengths can be used?", "legs of 3 units and 2 units (since 3² + 2² = 9 + 4 = 13)", ["legs of 4 and 1", "legs of 3 and 3", "legs of 5 and 1"]),
            ("To construct √17 directly in one step, what integer leg lengths can be used?", "base = 4 units, perpendicular = 1 unit (since 4² + 1² = 17)", ["base = 3, perpendicular = 3", "base = 5, perpendicular = 2", "base = 2, perpendicular = 2"]),
            ("Why is √5 located just to the right of 2 on the number line?", "Because √4 = 2 and 5 > 4, so √5 = 2.236 is slightly greater than 2", ["Because 5 = 2 + 3", "Because 2² = 5", "Because √5 is negative"])
        ],
        'tmpls': [
            "{0}",
            "Regarding direct geometric construction of √5: {0}",
            "In compass and straightedge construction of surds: {0}",
            "Choose the correct method to construct √5: {0}",
            "Identify the accurate geometric step: {0}",
            "According to Pythagoras theorem: {0}",
            "Select the correct answer: {0}",
            "Which option correctly describes: {0}?",
            "Determine the true statement: {0}",
            "State the geometric truth: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Express 5 as a sum of two squares.**\n\\[ 5 = 2^2 + 1^2 \\]\n\n**Step 2: Construct right triangle with legs 2 and 1.**\nBy Pythagoras theorem: \\( c = \\sqrt{{2^2 + 1^2}} = \\sqrt{5} \\).\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Theodorus Spiral (Wheel of Theodorus) properties
    arch3 = {
        'data': [
            ("In the Theodorus spiral, every right triangle has a common outer leg of length:", "1 unit", ["√2 units", "2 units", "variable length"]),
            ("The first hypotenuse in the Theodorus spiral has length:", "√2 units", ["1 unit", "√3 units", "2 units"]),
            ("The n-th hypotenuse in the Theodorus spiral has length:", "√(n + 1) units", ["√n units", "n units", "2n units"]),
            ("At which step does the Theodorus spiral first produce an integer hypotenuse length of 2?", "At the 3rd triangle (hypotenuse = √4 = 2)", ["At the 1st triangle", "At the 2nd triangle", "At the 4th triangle"]),
            ("At which step does the Theodorus spiral produce an integer hypotenuse length of 3?", "At the 8th triangle (hypotenuse = √9 = 3)", ["At the 5th triangle", "At the 7th triangle", "At the 9th triangle"]),
            ("Historically, up to which square root did Theodorus construct his spiral before it overlapped?", "√17", ["√10", "√25", "√50"]),
            ("What angle is between the base and perpendicular in each triangle of the spiral?", "90° (right angle)", ["45°", "60°", "30°"]),
            ("As more triangles are added to the Theodorus spiral, the spiral:", "winds outward continuously without closing", ["closes into a perfect circle", "collapses to origin", "forms a square"]),
            ("The hypotenuse of the 15th triangle in the spiral has length:", "√16 = 4 units", ["√15 units", "15 units", "√17 units"]),
            ("The square root spiral demonstrates that:", "all square roots of natural numbers can be constructed geometrically", ["only rational numbers exist", "irrational numbers cannot be drawn", "all square roots are integers"])
        ],
        'tmpls': [
            "{0}",
            "Regarding the Spiral of Theodorus: {0}",
            "In the geometry of the square root spiral: {0}",
            "Choose the correct fact about the Theodorus spiral: {0}",
            "Identify the accurate geometric property: {0}",
            "According to the Spiral of Theodorus: {0}",
            "Select the correct answer: {0}",
            "Which option correctly describes: {0}?",
            "Determine the true statement: {0}",
            "State the geometric truth: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand recursive construction of Theodorus spiral.**\nStart with a right isosceles triangle of legs 1 and 1 (hypotenuse \\( \\sqrt{{2}} \\)).\nEach subsequent triangle has the previous hypotenuse \\( \\sqrt{{k}} \\) as base and perpendicular = 1.\n\n**Step 2: Compute next hypotenuse.**\n\\[ \\text{{Hypotenuse}} = \\sqrt{{(\\sqrt{{k}})^2 + 1^2}} = \\sqrt{{k + 1}} \\]\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Locating negative square roots on the number line (-√2, -√3, -√5)
    arch4 = {
        'data': [
            ("-√2", "between -2 and -1 (approx -1.414)", ["between -1 and 0", "between -3 and -2", "positive side"]),
            ("-√3", "between -2 and -1 (approx -1.732)", ["between -1 and 0", "between -3 and -2", "at -2 exactly"]),
            ("-√5", "between -3 and -2 (approx -2.236)", ["between -2 and -1", "between -4 and -3", "at -2"]),
            ("-√10", "between -4 and -3 (approx -3.162)", ["between -3 and -2", "between -5 and -4", "at -3"]),
            ("-√7", "between -3 and -2 (approx -2.646)", ["between -2 and -1", "between -4 and -3", "at -7"]),
            ("-√8", "between -3 and -2 (approx -2.828)", ["between -2 and -1", "between -4 and -3", "at -3"]),
            ("-√17", "between -5 and -4 (approx -4.123)", ["between -4 and -3", "between -6 and -5", "at -4"]),
            ("-√26", "between -6 and -5 (approx -5.099)", ["between -5 and -4", "between -7 and -6", "at -5"]),
            ("-√37", "between -7 and -6 (approx -6.082)", ["between -6 and -5", "between -8 and -7", "at -6"]),
            ("-√15", "between -4 and -3 (approx -3.873)", ["between -3 and -2", "between -5 and -4", "at -4"])
        ],
        'tmpls': [
            "Where does the point representing \\( {0} \\) lie on the number line?",
            "Between which two consecutive integers is the point \\( {0} \\) located?",
            "Identify the position of \\( {0} \\) on the real number line:",
            "On the negative side of the number line, \\( {0} \\) falls:",
            "To which interval of integers does \\( {0} \\) belong?",
            "The coordinate of \\( {0} \\) on the number line lies:",
            "In what range on the real axis is \\( {0} \\) situated?",
            "Determine between which integers \\( {0} \\) is plotted:",
            "Find the integer interval containing \\( {0} \\):",
            "State the location of \\( {0} \\) on the number line:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Determine the positive square root bounds.**\nFind consecutive squares bounding the radicand.\n\n**Step 2: Negate the bounds.**\nRemember that negating reverses inequalities: \\( a < x < b \\implies -b < -x < -a \\).\n\n**Step 3: State the interval.**\n\\( {item[0]} \\) lies {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 5: Calculating distances between constructed surds on the number line
    arch5 = {
        'data': [
            ("distance between -√2 and √2 on the number line", "2√2 units", ["0 units", "2 units", "4 units"]),
            ("distance between -√5 and √5 on the number line", "2√5 units", ["0 units", "5 units", "10 units"]),
            ("distance between 0 and √2 on the number line", "√2 units", ["1 unit", "2 units", "1.5 units"]),
            ("distance between 1 and √2 on the number line", "√2 - 1 units (approx 0.414)", ["1 unit", "√2 units", "0.5 units"]),
            ("distance between √2 and 2 on the number line", "2 - √2 units (approx 0.586)", ["√2 units", "1 unit", "0.414 units"]),
            ("distance between -√3 and √3 on the number line", "2√3 units", ["0 units", "3 units", "6 units"]),
            ("midpoint between -√2 and √2 on the number line", "0 (the origin)", ["1", "-1", "√2/2"]),
            ("midpoint between 0 and 2√3 on the number line", "√3", ["2", "3", "√3/2"]),
            ("distance between √3 and √12 on the number line", "√3 units (since √12 = 2√3)", ["√9 = 3 units", "2 units", "√15 units"]),
            ("distance between √8 and √18 on the number line", "√2 units (since √18 = 3√2 and √8 = 2√2)", ["√10 units", "2 units", "√26 units"])
        ],
        'tmpls': [
            "What is the {0}?",
            "Calculate the {0}:",
            "In coordinate geometry on the number line, find the {0}:",
            "Determine the {0}:",
            "The {0} is equal to:",
            "Find the numerical value of the {0}:",
            "Compute the {0}:",
            "What value represents the {0}?",
            "Solve for the {0}:",
            "Identify the correct result for the {0}:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Simplify surds if necessary.**\nExpress surds in terms of like radicals (e.g. \\( \\sqrt{{12}} = 2\\sqrt{3} \\)).\n\n**Step 2: Apply the distance formula on the number line.**\nDistance = \\( |b - a| \\).\n\n**Step 3: State the distance.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Verification of right-angle constructions using Pythagoras theorem
    arch6 = {
        'data': [
            ("legs a = 1, b = 1", "hypotenuse c = √2", ["c = 2", "c = √3", "c = 1"]),
            ("legs a = √2, b = 1", "hypotenuse c = √3", ["c = 2", "c = √5", "c = 3"]),
            ("legs a = 2, b = 1", "hypotenuse c = √5", ["c = 3", "c = √3", "c = 5"]),
            ("legs a = √5, b = 2", "hypotenuse c = 3 (since (√5)² + 2² = 5 + 4 = 9)", ["c = √7", "c = √29", "c = 5"]),
            ("legs a = 3, b = 1", "hypotenuse c = √10", ["c = 4", "c = √8", "c = 10"]),
            ("legs a = √6, b = √3", "hypotenuse c = 3 (since (√6)² + (√3)² = 6 + 3 = 9)", ["c = √18", "c = 9", "c = √3"]),
            ("legs a = 3, b = 2", "hypotenuse c = √13", ["c = 5", "c = √5", "c = 13"]),
            ("legs a = 4, b = 1", "hypotenuse c = √17", ["c = 5", "c = √15", "c = 17"]),
            ("legs a = √7, b = 3", "hypotenuse c = 4 (since (√7)² + 3² = 7 + 9 = 16)", ["c = √10", "c = 16", "c = 5"]),
            ("legs a = 5, b = 1", "hypotenuse c = √26", ["c = 6", "c = √24", "c = 26"])
        ],
        'tmpls': [
            "In a right-angled triangle with {0}, find the hypotenuse.",
            "What is the length of the hypotenuse when a right triangle has {0}?",
            "Calculate the hypotenuse of a right triangle with {0}:",
            "Using Pythagoras theorem, find the hypotenuse for {0}:",
            "Determine the hypotenuse length for {0}:",
            "The hypotenuse of the triangle having {0} is:",
            "Find \\( c \\) by Pythagoras theorem given {0}:",
            "Compute the hypotenuse when {0}:",
            "What hypotenuse is produced by {0}?",
            "State the hypotenuse length corresponding to {0}:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: State Pythagoras theorem.**\n\\[ c^2 = a^2 + b^2 \\implies c = \\sqrt{{a^2 + b^2}} \\]\n\n**Step 2: Substitute the leg lengths.**\nSubstitute the given values into the formula.\n\n**Step 3: State the hypotenuse.**\nThe hypotenuse is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 7: Multiple-choice geometric reasoning on compass constructions
    arch7 = {
        'data': [
            ("Which instrument is used along with a straightedge to transfer hypotenuse lengths onto the number line?", "Compass", ["Protractor", "Set square", "Divider"]),
            ("Why is the Pythagoras spiral construction exact rather than approximate?", "Because the lengths are exact Euclidean distances derived from right triangles by the Pythagorean theorem", ["Because compasses are always 100% precise", "Because all square roots are integers", "It is only an approximation"]),
            ("In constructing √2, why must the line at x = 1 be perpendicular to the number line?", "Because Pythagoras theorem applies only to right-angled triangles (angle = 90°)", ["Because 1 + 1 = 2", "To make it parallel to y-axis only", "It is not strictly necessary"]),
            ("What is the radius of the circle centered at origin that passes through the point (1, 1)?", "√2 units", ["1 unit", "2 units", "0.5 units"]),
            ("What is the radius of the circle centered at origin that passes through the point (2, 1)?", "√5 units", ["3 units", "2 units", "5 units"]),
            ("What is the radius of the circle centered at origin that passes through the point (3, 2)?", "√13 units", ["5 units", "6 units", "13 units"]),
            ("Can every real number be represented by a unique point on the number line?", "Yes, according to the Cantor-Dedekind axiom", ["No, only rational numbers", "No, only integers", "Only positive numbers"]),
            ("Does the point representing √2 on the number line coincide with 1.414?", "No, 1.414 is only a rational approximation; √2 is an exact irrational point", ["Yes, they are identical", "1.414 is larger than √2", "√2 is a rational number"]),
            ("To construct √8 on the number line in one step, what leg lengths can be used?", "legs of 2 units and 2 units (since 2² + 2² = 8)", ["legs of 3 and 1", "legs of 4 and 2", "legs of 1 and 7"]),
            ("To construct √20 on the number line in one step, what leg lengths can be used?", "legs of 4 units and 2 units (since 4² + 2² = 16 + 4 = 20)", ["legs of 5 and 1", "legs of 3 and 3", "legs of 10 and 2"])
        ],
        'tmpls': [
            "{0}",
            "In geometric number theory: {0}",
            "Regarding compass and ruler construction: {0}",
            "Choose the correct option: {0}",
            "Identify the valid geometric fact: {0}",
            "Select the accurate answer: {0}",
            "Determine the correct choice: {0}",
            "Which option correctly answers: {0}",
            "Solve the following construction question: {0}",
            "What is the mathematical answer to: {0}?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand the geometric principle.**\nConsider the question: '{item[0]}'.\n\n**Step 2: Connect with geometric theorems and axioms.**\nApply the Pythagorean relation and properties of Euclidean constructions.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 3.2.3: Locating √x on number line
# ==============================================================================
def gen_3_2_3():
    tc = "CBSE-9-MGM-3-3.2.3"
    tname = "Locating √x on number line"

    # Arch 0: Semicircle geometric method formula for √x
    arch0 = {
        'data': [
            ("In the geometric construction of √x using a semicircle, if AB = x and BC = 1, the total length AC is:", "x + 1", ["x - 1", "2x + 1", "x"]),
            ("The radius of the semicircle with diameter AC = x + 1 is:", "(x + 1)/2", ["(x - 1)/2", "x/2", "x + 1"]),
            ("If O is the midpoint of AC, the distance OB from the center O to point B is:", "(x - 1)/2", ["(x + 1)/2", "x/2", "1"]),
            ("In the right triangle OBD (where D is on the semicircle above B), the length BD is proved to equal:", "√x", ["x", "(x + 1)/2", "x²"]),
            ("The proof that BD = √x uses Pythagoras theorem: BD² = OD² - OB². Substituting gives:", "((x+1)/2)² - ((x-1)/2)² = (4x)/4 = x", ["(x+1)² - (x-1)² = 4x", "(x+1)/2 - (x-1)/2 = 1", "x² - 1 = x"]),
            ("To construct √9.3 geometrically on the number line, the segment AB is chosen of length:", "9.3 units", ["10.3 units", "8.3 units", "3.05 units"]),
            ("In the construction of √9.3, what is the length of AC (where BC = 1)?", "10.3 units", ["9.3 units", "11.3 units", "8.3 units"]),
            ("In the construction of √9.3, what is the radius of the semicircle?", "5.15 units (10.3 / 2)", ["4.65 units", "9.3 units", "3.05 units"]),
            ("In the construction of √9.3, what is the distance OB from the center to point B?", "4.15 units (5.15 - 1)", ["5.15 units", "9.3 units", "3.05 units"]),
            ("With B as origin (0) and radius BD = √x, an arc is drawn to intersect the number line at E representing:", "√x", ["x", "x + 1", "(x + 1)/2"])
        ],
        'tmpls': [
            "{0}",
            "Regarding the geometric semicircle construction of √x: {0}",
            "In constructing √x on the number line for any positive real x: {0}",
            "Choose the correct step in locating √x geometrically: {0}",
            "Identify the accurate geometric formula: {0}",
            "According to the semicircle construction method for √x: {0}",
            "Select the correct answer: {0}",
            "Which option correctly specifies: {0}?",
            "Determine the true statement: {0}",
            "State the geometric truth: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand the semicircle construction.**\nMark \\( AB = x \\) and extend by 1 unit to \\( C \\) (so \\( AC = x + 1 \\)).\nCenter \\( O \\) is the midpoint of \\( AC \\), so radius \\( r = \\frac{{x + 1}}{{2}} \\).\n\n**Step 2: Apply Pythagoras theorem in \\( \\Delta OBD \\).**\n\\( BD^2 = OD^2 - OB^2 = \\left(\\frac{{x+1}}{{2}}\\right)^2 - \\left(\\frac{{x-1}}{{2}}\\right)^2 = x \\implies BD = \\sqrt{{x}} \\).\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Numerical values of diameter AC = x + 1
    arch1 = {
        'data': [
            (9.3, 10.3), (3.5, 4.5), (4.7, 5.7), (7.2, 8.2), (5.6, 6.6),
            (6.5, 7.5), (8.4, 9.4), (2.8, 3.8), (3.6, 4.6), (4.5, 5.5)
        ],
        'tmpls': [
            "In constructing \\( \\sqrt{{{0}}} \\) geometrically on the number line using the semicircle method, what is the total length of segment AC (diameter)?",
            "To locate \\( \\sqrt{{{0}}} \\), we mark \\( AB = {0} \\) and \\( BC = 1 \\). What is the length of AC?",
            "What diameter AC is needed to construct \\( \\sqrt{{{0}}} \\) geometrically?",
            "Calculate the length of the diameter AC for constructing \\( \\sqrt{{{0}}} \\):",
            "For \\( x = {0} \\), the total diameter \\( AC = x + 1 \\) equals:",
            "Find the length of AC when constructing \\( \\sqrt{{{0}}} \\):",
            "The diameter of the semicircle used to construct \\( \\sqrt{{{0}}} \\) is:",
            "Determine the length of AC for \\( \\sqrt{{{0}}} \\):",
            "In the construction of \\( \\sqrt{{{0}}} \\), the distance from A to C is:",
            "What is \\( AC = x + 1 \\) for \\( x = {0} \\)?"
        ],
        'calc': lambda item: (
            f"{item[1]} units",
            [
                f"{item[1] + 1} units",
                f"{item[1] - 1} units",
                f"{item[0]} units"
            ],
            f"**Step 1: Use diameter formula \\( AC = x + 1 \\).**\nMark \\( AB = x = {item[0]} \\) units.\nAdd \\( BC = 1 \\) unit.\n\n**Step 2: Add the lengths.**\n\\[ AC = {item[0]} + 1 = {item[1]} \\text{{ units}} \\]\n\n**Step 3: State the diameter length.**\nThe length of AC is \\( {item[1]} \\) units."
        ),
        'diff': 'easy'
    }

    # Arch 2: Numerical values of radius r = (x + 1)/2
    arch2 = {
        'data': [
            (9.3, 5.15), (3.5, 2.25), (4.7, 2.85), (7.2, 4.10), (5.6, 3.30),
            (6.5, 3.75), (8.4, 4.70), (2.8, 1.90), (3.6, 2.30), (4.5, 2.75)
        ],
        'tmpls': [
            "What is the radius of the semicircle used to construct \\( \\sqrt{{{0}}} \\) geometrically?",
            "In the construction of \\( \\sqrt{{{0}}} \\), the radius \\( r = (x + 1)/2 \\) is:",
            "Find the radius of the semicircle drawn on diameter \\( AC \\) for \\( x = {0} \\):",
            "Calculate the radius of the semicircle needed to locate \\( \\sqrt{{{0}}} \\):",
            "For \\( x = {0} \\), determine the semicircle radius \\( r \\):",
            "The radius of the arc for constructing \\( \\sqrt{{{0}}} \\) equals:",
            "Compute \\( r = \\frac{{{0} + 1}}{{2}} \\) for the construction of \\( \\sqrt{{{0}}} \\):",
            "What radius \\( r \\) is set with the compass to draw the semicircle for \\( \\sqrt{{{0}}} \\)?",
            "Find the radius of the semicircle in locating \\( \\sqrt{{{0}}} \\):",
            "State the semicircle radius for constructing \\( \\sqrt{{{0}}} \\):"
        ],
        'calc': lambda item: (
            f"{item[1]:.2f} units",
            [
                f"{(item[1] + 0.5):.2f} units",
                f"{(item[1] - 0.5):.2f} units",
                f"{(item[0] / 2):.2f} units"
            ],
            f"**Step 1: Formula for semicircle radius.**\n\\[ r = \\frac{{x + 1}}{{2}} \\]\n\n**Step 2: Substitute \\( x = {item[0]} \\).**\n\\[ r = \\frac{{{item[0]} + 1}}{{2}} = {item[1]:.2f} \\text{{ units}} \\]\n\n**Step 3: State the radius.**\nThe radius is \\( {item[1]:.2f} \\) units."
        ),
        'diff': 'medium'
    }

    # Arch 3: Numerical values of distance OB = (x - 1)/2
    arch3 = {
        'data': [
            (9.3, 4.15), (3.5, 1.25), (4.7, 1.85), (7.2, 3.10), (5.6, 2.30),
            (6.5, 2.75), (8.4, 3.70), (2.8, 0.90), (3.6, 1.30), (4.5, 1.75)
        ],
        'tmpls': [
            "In the construction of \\( \\sqrt{{{0}}} \\), what is the distance from the midpoint O to the point B?",
            "For \\( x = {0} \\), calculate the distance \\( OB = (x - 1)/2 \\):",
            "What is the base \\( OB \\) of the right triangle \\( \\Delta OBD \\) in constructing \\( \\sqrt{{{0}}} \\)?",
            "Find the length of OB when locating \\( \\sqrt{{{0}}} \\) on the number line:",
            "Determine the distance \\( OB \\) for \\( x = {0} \\):",
            "The distance from center O of the semicircle to B for \\( x = {0} \\) is:",
            "Compute \\( OB = \\frac{{{0} - 1}}{{2}} \\) for the construction of \\( \\sqrt{{{0}}} \\):",
            "In locating \\( \\sqrt{{{0}}} \\), the segment OB has length:",
            "What is the value of \\( OB \\) when \\( x = {0} \\)?",
            "Calculate \\( OB \\) in the semicircle method for \\( \\sqrt{{{0}}} \\):"
        ],
        'calc': lambda item: (
            f"{item[1]:.2f} units",
            [
                f"{(item[1] + 1):.2f} units",
                f"{(item[1] - 0.5):.2f} units",
                f"{(item[0] - 1):.2f} units"
            ],
            f"**Step 1: Formula for distance \\( OB \\).**\n\\[ OB = \\frac{{x - 1}}{{2}} \\]\n(or \\( OB = r - 1 \\))\n\n**Step 2: Substitute \\( x = {item[0]} \\).**\n\\[ OB = \\frac{{{item[0]} - 1}}{{2}} = {item[1]:.2f} \\text{{ units}} \\]\n\n**Step 3: State the distance.**\nThe distance \\( OB \\) is \\( {item[1]:.2f} \\) units."
        ),
        'diff': 'medium'
    }

    # Arch 4: Pythagoras proof verification: r² - OB² = x
    arch4 = {
        'data': [
            (9.3, 5.15, 4.15), (3.5, 2.25, 1.25), (4.7, 2.85, 1.85), (7.2, 4.10, 3.10),
            (5.6, 3.30, 2.30), (6.5, 3.75, 2.75), (8.4, 4.70, 3.70), (2.8, 1.90, 0.90),
            (3.6, 2.30, 1.30), (4.5, 2.75, 1.75)
        ],
        'tmpls': [
            "In the construction of \\( \\sqrt{{{0}}} \\), verify that \\( OD^2 - OB^2 = ({1})^2 - ({2})^2 \\) equals:",
            "Calculate \\( ({1})^2 - ({2})^2 \\) in the geometric verification of \\( \\sqrt{{{0}}} \\):",
            "What is the value of \\( r^2 - OB^2 \\) for \\( r = {1} \\) and \\( OB = {2} \\)?",
            "In \\( \\Delta OBD \\), \\( BD^2 = ({1})^2 - ({2})^2 \\). This evaluates to:",
            "Compute \\( ({1})^2 - ({2})^2 \\) to verify the construction of \\( \\sqrt{{{0}}} \\):",
            "Evaluating \\( ({1} + {2})({1} - {2}) \\) gives:",
            "The difference of squares \\( ({1})^2 - ({2})^2 \\) is equal to:",
            "Find \\( BD^2 = ({1})^2 - ({2})^2 \\):",
            "Confirm the value of \\( OD^2 - OB^2 \\) for \\( x = {0} \\):",
            "Verify that \\( ({1})^2 - ({2})^2 \\) equals \\( x = {0} \\):"
        ],
        'calc': lambda item: (
            str(item[0]),
            [str(round(item[0] + 1, 1)), str(round(item[0] - 1, 1)), str(round(item[0] * 2, 1))],
            f"**Step 1: Use the difference of squares identity.**\n\\[ a^2 - b^2 = (a + b)(a - b) \\]\n\n**Step 2: Substitute \\( a = {item[1]} \\) and \\( b = {item[2]} \\).**\n\\[ ({item[1]} + {item[2]})({item[1]} - {item[2]}) = ({item[1] + item[2]:.1f})(1.0) = {item[0]} \\]\n\n**Step 3: State the result.**\nThe value is \\( {item[0]} \\), which proves \\( BD = \\sqrt{{{item[0]}}} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 5: Integer intervals containing √x for decimal x
    arch5 = {
        'data': [
            (9.3, 3, 4, "since 9 < 9.3 < 16"),
            (3.5, 1, 2, "since 1 < 3.5 < 4"),
            (4.7, 2, 3, "since 4 < 4.7 < 9"),
            (7.2, 2, 3, "since 4 < 7.2 < 9"),
            (5.6, 2, 3, "since 4 < 5.6 < 9"),
            (6.5, 2, 3, "since 4 < 6.5 < 9"),
            (8.4, 2, 3, "since 4 < 8.4 < 9"),
            (11.5, 3, 4, "since 9 < 11.5 < 16"),
            (14.8, 3, 4, "since 9 < 14.8 < 16"),
            (17.3, 4, 5, "since 16 < 17.3 < 25")
        ],
        'tmpls': [
            "Between which two consecutive integers does the point \\( \\sqrt{{{0}}} \\) lie on the number line?",
            "When \\( \\sqrt{{{0}}} \\) is constructed on the number line, it falls between:",
            "Find the two consecutive integers bounding \\( \\sqrt{{{0}}} \\):",
            "Identify the integer interval containing \\( \\sqrt{{{0}}} \\):",
            "The point \\( \\sqrt{{{0}}} \\) on the real number line is located between:",
            "In what integer range is \\( \\sqrt{{{0}}} \\) situated?",
            "Determine the integers immediately preceding and following \\( \\sqrt{{{0}}} \\):",
            "Between which integers does \\( \\sqrt{{{0}}} \\) lie?",
            "State the consecutive integers that bracket \\( \\sqrt{{{0}}} \\):",
            "Where does \\( \\sqrt{{{0}}} \\) lie relative to integers on the number line?"
        ],
        'calc': lambda item: (
            f"Between {item[1]} and {item[2]}",
            [
                f"Between {item[1] - 1} and {item[1]}",
                f"Between {item[2]} and {item[2] + 1}",
                f"Between {item[1] + 1} and {item[2] + 2}"
            ],
            f"**Step 1: Identify bounding perfect squares.**\nFind consecutive squares bounding \\( {item[0]} \\): {item[3]}.\n\n**Step 2: Take square roots.**\n\\( \\sqrt{{{item[1]}^2}} < \\sqrt{{{item[0]}}} < \\sqrt{{{item[2]}^2}} \\implies {item[1]} < \\sqrt{{{item[0]}}} < {item[2]} \\).\n\n**Step 3: State the bounding integers.**\nIt lies Between {item[1]} and {item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Comparison and ordering of square roots of decimals
    arch6 = {
        'data': [
            (9.3, 9.5, "\\sqrt{9.3} < \\sqrt{9.5}"),
            (3.5, 3.2, "\\sqrt{3.5} > \\sqrt{3.2}"),
            (4.7, 5.1, "\\sqrt{4.7} < \\sqrt{5.1}"),
            (7.2, 7.8, "\\sqrt{7.2} < \\sqrt{7.8}"),
            (6.5, 6.2, "\\sqrt{6.5} > \\sqrt{6.2}"),
            (8.4, 8.9, "\\sqrt{8.4} < \\sqrt{8.9}"),
            (2.8, 2.5, "\\sqrt{2.8} > \\sqrt{2.5}"),
            (3.6, 3.9, "\\sqrt{3.6} < \\sqrt{3.9}"),
            (4.5, 4.1, "\\sqrt{4.5} > \\sqrt{4.1}"),
            (5.6, 5.9, "\\sqrt{5.6} < \\sqrt{5.9}")
        ],
        'tmpls': [
            "Which relationship correctly compares \\( \\sqrt{{{0}}} \\) and \\( \\sqrt{{{1}}} \\)?",
            "Compare \\( \\sqrt{{{0}}} \\) and \\( \\sqrt{{{1}}} \\):",
            "What is the correct inequality between \\( \\sqrt{{{0}}} \\) and \\( \\sqrt{{{1}}} \\)?",
            "Determine whether \\( \\sqrt{{{0}}} \\) is greater than, less than, or equal to \\( \\sqrt{{{1}}} \\):",
            "Between \\( \\sqrt{{{0}}} \\) and \\( \\sqrt{{{1}}} \\), which is correct?",
            "Identify the valid statement comparing \\( \\sqrt{{{0}}} \\) with \\( \\sqrt{{{1}}} \\):",
            "Which inequality holds for \\( \\sqrt{{{0}}} \\) and \\( \\sqrt{{{1}}} \\)?",
            "State the correct comparison between \\( \\sqrt{{{0}}} \\) and \\( \\sqrt{{{1}}} \\):",
            "Evaluate the relationship between \\( \\sqrt{{{0}}} \\) and \\( \\sqrt{{{1}}} \\):",
            "Which order is correct for \\( \\sqrt{{{0}}} \\) and \\( \\sqrt{{{1}}} \\)?"
        ],
        'calc': lambda item: (
            item[2],
            [
                item[2].replace("<", ">") if "<" in item[2] else item[2].replace(">", "<"),
                item[2].replace("<", "=").replace(">", "="),
                "cannot be compared"
            ],
            f"**Step 1: Use monotonicity of the square root function.**\nFor any positive real numbers \\( a \\) and \\( b \\), \\( a < b \\iff \\sqrt{{a}} < \\sqrt{{b}} \\).\n\n**Step 2: Compare radicands.**\nSince {item[0]} {'<' if item[0] < item[1] else '>'} {item[1]}.\n\n**Step 3: State the conclusion.**\n{item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 7: General properties and geometric theorems regarding √x
    arch7 = {
        'data': [
            ("The geometric mean theorem states that the altitude BD to the hypotenuse in a right triangle inscribed in a semicircle is:", "the geometric mean of the segments of the diameter (BD² = AB * BC)", ["the arithmetic mean", "the harmonic mean", "the sum of segments"]),
            ("In the semicircle method for √x, what is the length of BC?", "1 unit", ["x units", "2 units", "0.5 units"]),
            ("Why is BC chosen as 1 unit in the construction of √x?", "Because BD² = AB * BC = x * 1 = x, making BD = √x", ["To make the triangle isosceles", "Because 1 is the smallest natural number", "It is an arbitrary choice"]),
            ("If BC were chosen as 2 units instead of 1 unit, BD would equal:", "√(2x)", ["√x", "2√x", "x/2"]),
            ("Can this semicircle method be used to construct square roots of non-integer decimals like √3.7?", "Yes, for any positive real number x", ["No, only for integers", "No, only for fractions", "Only for perfect squares"]),
            ("The geometric construction of √x demonstrates that:", "every positive real number has a square root that corresponds to a line segment", ["irrational numbers do not exist geometrically", "only rational square roots can be constructed", "compasses cannot draw square roots"]),
            ("The point B in the construction of √x is treated as:", "the origin (0) on the final number line", ["the center of the circle", "the point x + 1", "the point 1"]),
            ("The distance from point B(0) to point E on the number line is:", "√x units", ["x units", "x + 1 units", "(x + 1)/2 units"]),
            ("What is the angle ∠ADC inscribed in the semicircle?", "90° (angle in a semicircle is a right angle)", ["60°", "45°", "180°"]),
            ("In the right triangle ADC, the altitude BD divides the hypotenuse AC into:", "two segments AB = x and BC = 1", ["two equal segments", "segments x and x", "segments 1 and 2"])
        ],
        'tmpls': [
            "{0}",
            "In geometric theorems regarding the construction of √x: {0}",
            "Regarding the geometric mean and semicircle method: {0}",
            "Choose the correct mathematical principle: {0}",
            "Identify the accurate geometric property: {0}",
            "According to the construction of √x: {0}",
            "Select the correct answer: {0}",
            "Which option correctly describes: {0}?",
            "Determine the true statement: {0}",
            "State the geometric fact: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand the geometric mean property in a circle.**\nAn angle inscribed in a semicircle is a right angle (\\( \\angle ADC = 90^\\circ \\)).\nThe altitude to the hypotenuse satisfies \\( BD^2 = AB \\times BC \\).\n\n**Step 2: Connect with \\( BC = 1 \\).**\nSince \\( AB = x \\) and \\( BC = 1 \\), \\( BD^2 = x \\times 1 = x \\implies BD = \\sqrt{{x}} \\).\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])

if __name__ == "__main__":
    q1 = gen_3_2_1()
    q2 = gen_3_2_2()
    q3 = gen_3_2_3()
    print(f"gen_3_2_1: {len(q1)} questions generated")
    print(f"gen_3_2_2: {len(q2)} questions generated")
    print(f"gen_3_2_3: {len(q3)} questions generated")
