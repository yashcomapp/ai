# scripts/build_cbse9_mgm_ch3_part1.py
# Subtopics:
# 3.1.1: Definition of rational numbers p/q (q != 0) (80 Qs)
# 3.1.2: Terminating vs non-terminating recurring decimal expansions (80 Qs)
# 3.1.3: Converting repeating decimals 0.p̄ and 0.pq̄ to fraction form (80 Qs)

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 3
CH_NAME = "The World of Numbers"

# ==============================================================================
# SUBTOPIC 3.1.1: Definition of rational numbers p/q (q != 0)
# ==============================================================================
def gen_3_1_1():
    tc = "CBSE-9-MGM-3-3.1.1"
    tname = "Definition of rational numbers p/q (q != 0)"

    # Arch 0: Fundamental definition and zero as a rational number
    arch0 = {
        'data': [
            ("Can zero be written in the form p/q where p and q are integers and q ≠ 0?", "Yes, because 0 can be written as 0/1, 0/2, 0/(-5), etc.", ["No, because zero has no reciprocal", "Only if q = 0", "No, because zero is not an integer"]),
            ("Which condition must be satisfied for a number to be rational (p/q)?", "p and q are integers and q ≠ 0", ["p and q are natural numbers and q ≠ 0", "p and q are real numbers and p ≠ 0", "q can be any real number including 0"]),
            ("Every integer n is a rational number because it can be expressed as:", "n/1", ["1/n", "n/0", "n/n"]),
            ("Which of the following is NOT a rational number?", "√2", ["-7/8", "0", "0.333..."]),
            ("Which statement about rational numbers is TRUE?", "Every whole number is a rational number", ["Every real number is a rational number", "Zero is not a rational number", "The denominator q can equal 0"]),
            ("Every natural number is a rational number because:", "it can be written as n/1 where n ∈ ℕ and 1 ≠ 0", ["it is always positive", "it has no decimal part", "its square root is an integer"]),
            ("What is the reciprocal of the rational number -4/7?", "-7/4", ["7/4", "4/7", "-4/7"]),
            ("Which rational number has no reciprocal (multiplicative inverse)?", "0", ["1", "-1", "undefined"]),
            ("In the rational number p/q, what are p and q?", "integers with q ≠ 0", ["positive integers only", "fractions", "real numbers with p ≠ 0"]),
            ("Which of the following numbers is rational?", "3.1415", ["π", "√5", "0.1010010001..."])
        ],
        'tmpls': [
            "{0}",
            "Regarding the foundational definition of rational numbers: {0}",
            "In real number theory: {0}",
            "Choose the mathematically correct answer: {0}",
            "Identify the correct statement: {0}",
            "According to the definition of rational numbers: {0}",
            "Select the accurate fact: {0}",
            "Solve the following question on rational numbers: {0}",
            "Which option correctly answers: {0}",
            "Determine the true statement: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the definition of a rational number.**\nA number \\( r \\) is called a rational number if it can be written in the form \\( \\frac{{p}}{{q}} \\), where \\( p \\) and \\( q \\) are integers and \\( q \\neq 0 \\).\n\n**Step 2: Evaluate the statement.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Finding a rational number strictly between two numbers
    arch1 = {
        'data': [
            (3, 4, "\\frac{7}{2} = 3.5", ["\\frac{9}{2}", "\\frac{5}{2}", "4.5"]),
            (1, 2, "\\frac{3}{2} = 1.5", ["\\frac{5}{2}", "\\frac{1}{2}", "2.5"]),
            (5, 6, "\\frac{11}{2} = 5.5", ["\\frac{13}{2}", "\\frac{9}{2}", "6.5"]),
            (-2, -1, "-\\frac{3}{2} = -1.5", ["-\\frac{5}{2}", "-\\frac{1}{2}", "0.5"]),
            (0, 1, "\\frac{1}{2} = 0.5", ["\\frac{3}{2}", "-\\frac{1}{2}", "1.5"]),
            (2, 3, "\\frac{5}{2} = 2.5", ["\\frac{7}{2}", "\\frac{3}{2}", "3.5"]),
            (-4, -3, "-\\frac{7}{2} = -3.5", ["-\\frac{9}{2}", "-\\frac{5}{2}", "-2.5"]),
            (7, 8, "\\frac{15}{2} = 7.5", ["\\frac{17}{2}", "\\frac{13}{2}", "8.5"]),
            (-1, 0, "-\\frac{1}{2} = -0.5", ["-\\frac{3}{2}", "\\frac{1}{2}", "0"]),
            (4, 5, "\\frac{9}{2} = 4.5", ["\\frac{11}{2}", "\\frac{7}{2}", "5.5"])
        ],
        'tmpls': [
            "Find a rational number lying strictly between {0} and {1}.",
            "Which rational number lies between {0} and {1}?",
            "What is the arithmetic mean (midpoint) rational number between {0} and {1}?",
            "Calculate a rational number strictly between {0} and {1}:",
            "A rational number between {0} and {1} is given by:",
            "Determine a number in the form \\( p/q \\) lying between {0} and {1}:",
            "Identify the rational number positioned between {0} and {1}:",
            "Which value represents a rational number between {0} and {1}?",
            "Compute a rational number between {0} and {1}:",
            "Find the number halfway between {0} and {1}:"
        ],
        'calc': lambda item: (
            item[2],
            item[3],
            f"**Step 1: Use the mean formula for two rational numbers.**\nA rational number between \\( a \\) and \\( b \\) is given by the average:\n\\[ r = \\frac{{a + b}}{{2}} \\]\n\n**Step 2: Substitute \\( a = {item[0]} \\) and \\( b = {item[1]} \\).**\n\\[ r = \\frac{{{item[0]} + ({item[1]})}}{{2}} = {item[2]} \\]\n\n**Step 3: State the rational number.**\nThe rational number is \\( {item[2]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Density property of rational numbers
    arch2 = {
        'data': [
            ("How many rational numbers exist between any two distinct rational numbers?", "Infinitely many rational numbers", ["Exactly 1 rational number", "A finite number depending on the gap", "0 rational numbers"]),
            ("The property that between any two rational numbers there lies another rational number is called:", "Density property of rational numbers", ["Closure property", "Commutative property", "Associative property"]),
            ("How many rational numbers lie between 3/5 and 4/5?", "Infinitely many rational numbers", ["None (0)", "Only 1", "Exactly 10"]),
            ("Between the rational numbers -1 and 1, how many rational numbers can be found?", "Infinitely many", ["Only 0", "Exactly 100", "Exactly 2"]),
            ("Can we find 100 rational numbers between 0.1 and 0.2?", "Yes, in fact infinitely many rational numbers exist between them", ["No, only 9 rational numbers exist", "No, none exist", "Only 10 exist"]),
            ("Which of the following operations between rational numbers is NOT closed?", "Division (due to division by zero)", ["Addition", "Subtraction", "Multiplication"]),
            ("The rational numbers are closed under which set of operations?", "Addition, subtraction, and multiplication", ["Addition and division only", "Multiplication and division only", "None of these"]),
            ("What is the additive identity for the set of rational numbers?", "0", ["1", "-1", "undefined"]),
            ("What is the multiplicative identity for the set of rational numbers?", "1", ["0", "-1", "any non-zero integer"]),
            ("The negative of a rational number p/q is called its:", "additive inverse (-p/q)", ["reciprocal", "multiplicative inverse", "modulus"])
        ],
        'tmpls': [
            "{0}",
            "In number theory: {0}",
            "Regarding the density and properties of numbers: {0}",
            "Choose the correct statement: {0}",
            "Which of the following is accurate: {0}?",
            "Identify the correct mathematical fact: {0}",
            "According to the axioms of rational numbers: {0}",
            "Determine the correct answer: {0}",
            "Select the accurate option: {0}",
            "State the correct property: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the density property of rational numbers.**\nBetween any two distinct rational numbers \\( a \\) and \\( b \\), there exist infinitely many rational numbers.\n\n**Step 2: Analyze the question.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Rational numbers between fractions (e.g. 5 rationals between 3/5 and 4/5)
    arch3 = {
        'data': [
            ("\\frac{3}{5}", "\\frac{4}{5}", 5, "\\frac{19}{30}", ["\\frac{25}{30}", "\\frac{17}{30}", "\\frac{26}{30}"]),
            ("\\frac{1}{3}", "\\frac{1}{2}", 3, "\\frac{5}{12}", ["\\frac{7}{12}", "\\frac{3}{12}", "\\frac{1}{12}"]),
            ("\\frac{2}{3}", "\\frac{3}{4}", 4, "\\frac{17}{24}", ["\\frac{15}{24}", "\\frac{19}{24}", "\\frac{13}{24}"]),
            ("\\frac{3}{7}", "\\frac{4}{7}", 5, "\\frac{19}{35}", ["\\frac{22}{35}", "\\frac{14}{35}", "\\frac{25}{35}"]),
            ("\\frac{1}{4}", "\\frac{1}{3}", 3, "\\frac{7}{24}", ["\\frac{5}{24}", "\\frac{9}{24}", "\\frac{11}{24}"]),
            ("-\\frac{1}{2}", "\\frac{1}{2}", 5, "0", ["1", "-1", "\\frac{3}{2}"]),
            ("\\frac{2}{5}", "\\frac{3}{5}", 4, "\\frac{11}{25}", ["\\frac{16}{25}", "\\frac{9}{25}", "\\frac{18}{25}"]),
            ("-\\frac{3}{4}", "-\\frac{1}{4}", 3, "-\\frac{1}{2}", ["-1", "0", "\\frac{1}{4}"]),
            ("\\frac{4}{5}", "\\frac{5}{6}", 5, "\\frac{49}{60}", ["\\frac{47}{60}", "\\frac{52}{60}", "\\frac{45}{60}"]),
            ("\\frac{1}{6}", "\\frac{1}{4}", 3, "\\frac{5}{24}", ["\\frac{3}{24}", "\\frac{7}{24}", "\\frac{9}{24}"])
        ],
        'tmpls': [
            "Which of the following rational numbers lies strictly between \\( {0} \\) and \\( {1} \\)?",
            "Identify a rational number located between \\( {0} \\) and \\( {1} \\):",
            "Find a rational number lying in the interval \\( ({0}, {1}) \\):",
            "Which fraction represents a rational number between \\( {0} \\) and \\( {1} \\)?",
            "A rational number between \\( {0} \\) and \\( {1} \\) is:",
            "Determine which of the given values falls between \\( {0} \\) and \\( {1} \\):",
            "Which rational value is situated between \\( {0} \\) and \\( {1} \\)?",
            "Calculate a fraction that lies between \\( {0} \\) and \\( {1} \\):",
            "Select the rational number located strictly between \\( {0} \\) and \\( {1} \\):",
            "Find a number of the form \\( p/q \\) between \\( {0} \\) and \\( {1} \\):"
        ],
        'calc': lambda item: (
            item[3],
            item[4],
            f"**Step 1: Convert both fractions to a common denominator.**\nExpress \\( {item[0]} \\) and \\( {item[1]} \\) with a sufficiently large common denominator to view the intermediate fractions.\n\n**Step 2: Compare numerators.**\nCheck which candidate fraction lies strictly between the two bounds.\n\n**Step 3: State the intermediate fraction.**\nThe rational number is \\( {item[3]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Equivalent rational numbers and reducing to simplest (standard) form
    arch4 = {
        'data': [
            ("36/48", "3/4", ["2/3", "4/5", "6/8"]),
            ("-45/60", "-3/4", ["-4/5", "-2/3", "3/4"]),
            ("84/108", "7/9", ["6/9", "8/9", "7/8"]),
            ("-72/96", "-3/4", ["-2/3", "-5/6", "3/4"]),
            ("120/150", "4/5", ["3/5", "5/6", "2/3"]),
            ("-64/80", "-4/5", ["-3/4", "-5/6", "4/5"]),
            ("105/135", "7/9", ["5/9", "8/9", "7/8"]),
            ("-98/126", "-7/9", ["-5/9", "-8/9", "7/9"]),
            ("75/100", "3/4", ["2/3", "4/5", "1/2"]),
            ("-112/144", "-7/9", ["-5/9", "-3/4", "7/9"])
        ],
        'tmpls': [
            "Reduce the rational number \\( {0} \\) to its standard form (lowest terms).",
            "What is the simplest form of the rational number \\( {0} \\)?",
            "In lowest terms, the fraction \\( {0} \\) equals:",
            "Express the rational number \\( {0} \\) in irreducible standard form \\( p/q \\):",
            "Simplify the rational number \\( {0} \\):",
            "Find the standard form of \\( {0} \\):",
            "The fraction \\( {0} \\) simplified to lowest terms is:",
            "Convert \\( {0} \\) into its irreducible rational form:",
            "What is the canonical lowest-terms representation of \\( {0} \\)?",
            "Determine the standard form of the rational fraction \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Find the greatest common divisor (GCD) of numerator and denominator.**\nCalculate \\( \\gcd(\\text{{numerator}}, \\text{{denominator}}) \\).\n\n**Step 2: Divide numerator and denominator by their GCD.**\nDivide both by the GCD to eliminate all common factors.\n\n**Step 3: State the standard form.**\nThe simplest form is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 5: Ordering and comparing rational numbers
    arch5 = {
        'data': [
            ("-5/6", "-7/8", "-5/6 > -7/8", ["-5/6 < -7/8", "-5/6 = -7/8", "cannot be compared"]),
            ("3/4", "5/7", "3/4 > 5/7", ["3/4 < 5/7", "3/4 = 5/7", "3/4 + 5/7 = 1"]),
            ("-2/3", "-3/5", "-2/3 < -3/5", ["-2/3 > -3/5", "-2/3 = -3/5", "-2/3 * -3/5 = -1"]),
            ("7/9", "4/5", "7/9 < 4/5", ["7/9 > 4/5", "7/9 = 4/5", "7/9 + 4/5 = 1"]),
            ("-4/7", "-5/9", "-4/7 < -5/9", ["-4/7 > -5/9", "-4/7 = -5/9", "both equal 0"]),
            ("5/8", "7/11", "5/8 < 7/11", ["5/8 > 7/11", "5/8 = 7/11", "5/8 * 7/11 = 1"]),
            ("-3/8", "-5/12", "-3/8 > -5/12", ["-3/8 < -5/12", "-3/8 = -5/12", "cannot be compared"]),
            ("6/7", "8/9", "6/7 < 8/9", ["6/7 > 8/9", "6/7 = 8/9", "both equal 1"]),
            ("-1/3", "-2/7", "-1/3 < -2/7", ["-1/3 > -2/7", "-1/3 = -2/7", "-1/3 + -2/7 = 0"]),
            ("9/10", "11/12", "9/10 < 11/12", ["9/10 > 11/12", "9/10 = 11/12", "9/10 - 11/12 = 1"])
        ],
        'tmpls': [
            "Compare the two rational numbers \\( {0} \\) and \\( {1} \\). Which relationship is correct?",
            "Which of the following correctly compares \\( {0} \\) and \\( {1} \\)?",
            "Determine the correct inequality between \\( {0} \\) and \\( {1} \\):",
            "Between \\( {0} \\) and \\( {1} \\), which statement is true?",
            "Compare \\( {0} \\) and \\( {1} \\):",
            "Which inequality holds for the rational numbers \\( {0} \\) and \\( {1} \\)?",
            "Is \\( {0} \\) greater than, less than, or equal to \\( {1} \\)?",
            "State the correct comparison between \\( {0} \\) and \\( {1} \\):",
            "Evaluate the relationship between \\( {0} \\) and \\( {1} \\):",
            "Identify the valid statement comparing \\( {0} \\) with \\( {1} \\):"
        ],
        'calc': lambda item: (
            item[2],
            item[3],
            f"**Step 1: Cross-multiply or find a common denominator.**\nTo compare \\( \\frac{{a}}{{b}} \\) and \\( \\frac{{c}}{{d}} \\), cross-multiply: \\( a \\cdot d \\) vs \\( b \\cdot c \\).\n\n**Step 2: Compare the resulting integers (accounting for signs).**\nNote that for negative numbers, the number with smaller magnitude is greater.\n\n**Step 3: State the inequality.**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: True/False statements about subsets of real numbers (N ⊂ W ⊂ Z ⊂ Q)
    arch6 = {
        'data': [
            ("Every natural number is a whole number", "True", ["False", "Only for even numbers", "Undefined"]),
            ("Every whole number is a natural number", "False (0 is a whole number but not a natural number)", ["True", "Always true", "Undefined"]),
            ("Every integer is a rational number", "True (any integer m can be written as m/1)", ["False", "Only for positive integers", "Only for prime numbers"]),
            ("Every rational number is an integer", "False (e.g., 3/5 is rational but not an integer)", ["True", "True for all positive numbers", "Undefined"]),
            ("Every natural number is an integer", "True", ["False", "Only if non-zero", "Undefined"]),
            ("Every rational number is a whole number", "False (e.g., 1/2 is rational but not a whole number)", ["True", "True except for 0", "Undefined"]),
            ("The collection of rational numbers is denoted by the letter", "Q (from Quotient)", ["R", "Z", "N"]),
            ("The collection of integers is denoted by the letter", "Z (from German 'Zahlen')", ["I", "Q", "N"]),
            ("Between two distinct integers, how many integers exist?", "A finite number (or none if consecutive)", ["Infinitely many", "Always 1", "Undefined"]),
            ("Between two distinct integers, how many rational numbers exist?", "Infinitely many rational numbers", ["A finite number", "Only 1", "0"])
        ],
        'tmpls': [
            "Is the statement true or false: '{0}'?",
            "State whether the following assertion is true or false: '{0}'.",
            "Determine the truth value of the statement: '{0}'.",
            "Regarding number systems: '{0}'. This is:",
            "Evaluate the correctness of the statement: '{0}'.",
            "Which option correctly assesses: '{0}'?",
            "Analyze: '{0}'. The correct answer is:",
            "Check the validity: '{0}':",
            "Is it true that {0}?",
            "Determine whether: '{0}'."
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall hierarchy of number sets.**\n\\[ \\mathbb{{N}} \\subset \\mathbb{{W}} \\subset \\mathbb{{Z}} \\subset \\mathbb{{Q}} \\subset \\mathbb{{R}} \\]\n\n**Step 2: Test the specific statement.**\nStatement: '{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 7: Real-world problems involving rational numbers (proportions, sharing)
    arch7 = {
        'data': [
            ("A recipe calls for 3/4 cup of sugar per batch. How many cups are needed for 6 batches?", "9/2 cups (4.5 cups)", ["18/4 cups", "3 cups", "5 cups"]),
            ("A rope of length 15/2 meters is cut into 5 equal pieces. What is the length of each piece?", "3/2 meters (1.5 m)", ["2 meters", "5/2 meters", "1 meter"]),
            ("A water tank of capacity 120 liters is 3/5 full. How many liters of water are in the tank?", "72 liters", ["60 liters", "80 liters", "48 liters"]),
            ("In a class of 45 students, 2/3 passed in mathematics. How many students passed?", "30 students", ["25 students", "35 students", "15 students"]),
            ("A car travels 48 km in 3/4 of an hour. What is its speed in km/h?", "64 km/h", ["36 km/h", "72 km/h", "60 km/h"]),
            ("If 2/5 of a pizza was eaten by Rohan and 1/3 by Priya, what fraction of the pizza was eaten in total?", "11/15", ["3/8", "13/15", "2/15"]),
            ("What fraction remains from a full pizza if 11/15 was eaten?", "4/15", ["5/15", "1/15", "2/15"]),
            ("A painter paints 2/7 of a wall on Monday and 3/7 on Tuesday. What fraction remains to be painted?", "2/7", ["5/7", "1/7", "3/7"]),
            ("A petrol tank of 40 liters contains 5/8 of its capacity. How many liters of petrol are in the tank?", "25 liters", ["20 liters", "30 liters", "15 liters"]),
            ("If 3/8 of a journey is 45 km, what is the total length of the journey?", "120 km", ["100 km", "135 km", "150 km"])
        ],
        'tmpls': [
            "{0}",
            "Solve the following word problem using rational numbers: {0}",
            "In practical arithmetic: {0}",
            "Calculate the required quantity: {0}",
            "Applied rational number problem: {0}",
            "Determine the correct answer to: {0}",
            "Word problem on fractions: {0}",
            "Compute the solution: {0}",
            "Solve: {0}",
            "Find the required value: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Set up the rational arithmetic expression.**\nFrom the problem description: '{item[0]}'.\n\n**Step 2: Perform fraction multiplication or division.**\nSimplify the resulting fraction to its lowest terms.\n\n**Step 3: State the final answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 3.1.2: Terminating vs non-terminating recurring decimal expansions
# ==============================================================================
def gen_3_1_2():
    tc = "CBSE-9-MGM-3-3.1.2"
    tname = "Terminating vs non-terminating recurring decimal expansions"

    # Arch 0: Fundamental theorem on terminating decimal expansions (q = 2^m * 5^n)
    arch0 = {
        'data': [
            ("A rational number p/q in simplest form has a terminating decimal expansion if and only if the prime factorization of q contains:", "only prime factors 2 and/or 5 (2^m * 5^n)", ["only odd prime factors", "only prime factor 3", "any prime factors"]),
            ("If the prime factorization of the denominator q contains a prime factor other than 2 and 5 (such as 3, 7, 11), the decimal expansion is:", "non-terminating recurring (repeating)", ["terminating", "non-terminating non-repeating", "an integer"]),
            ("The decimal expansion of every rational number is either:", "terminating or non-terminating recurring", ["terminating only", "non-terminating non-recurring", "an integer"]),
            ("A number whose decimal expansion is non-terminating and recurring is:", "a rational number", ["an irrational number", "an integer", "an imaginary number"]),
            ("Can a rational number have a non-terminating non-recurring decimal expansion?", "No, non-terminating non-recurring expansions belong exclusively to irrational numbers", ["Yes, when the denominator is prime", "Yes, when q = 0", "Only for negative fractions"]),
            ("The maximum number of digits in the repeating block of decimals of 1/q is at most:", "q - 1 digits", ["q digits", "q + 1 digits", "2q digits"]),
            ("The number of digits in the repeating period of 1/7 is:", "6 digits (0.142857...)", ["7 digits", "5 digits", "1 digit"]),
            ("In the decimal expansion of 1/3 = 0.333..., the repeating block consists of:", "1 digit (the digit 3)", ["3 digits", "2 digits", "infinitely many different digits"]),
            ("In 1/11 = 0.090909..., the length of the period (periodicity) is:", "2 digits ('09')", ["1 digit", "3 digits", "11 digits"]),
            ("Which part of the fraction p/q determines whether the decimal terminates without actual division?", "Prime factorization of the denominator q (in lowest terms)", ["Numerator p", "Sum of p and q", "Product p * q"])
        ],
        'tmpls': [
            "{0}",
            "In decimal representations of real numbers: {0}",
            "According to the fundamental theorem of arithmetic on fractions: {0}",
            "Select the correct mathematical rule: {0}",
            "Identify the accurate fact: {0}",
            "Which statement correctly describes: {0}?",
            "Regarding decimal expansions of rational numbers: {0}",
            "Determine the correct answer: {0}",
            "Choose the true property: {0}",
            "State the theorem: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the condition for terminating decimals.**\nA rational number \\( \\frac{{p}}{{q}} \\) in lowest terms has a terminating decimal expansion if and only if \\( q = 2^m 5^n \\) for non-negative integers \\( m, n \\).\n\n**Step 2: Analyze the question.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Identifying terminating decimals without division
    arch1 = {
        'data': [
            ("13/8", "Terminating (denominator 8 = 2³)", ["Non-terminating recurring", "Non-terminating non-repeating", "Irrational"]),
            ("7/25", "Terminating (denominator 25 = 5²)", ["Non-terminating recurring", "Non-terminating non-repeating", "Irrational"]),
            ("17/20", "Terminating (denominator 20 = 2² * 5)", ["Non-terminating recurring", "Non-terminating non-repeating", "Integer"]),
            ("29/50", "Terminating (denominator 50 = 2 * 5²)", ["Non-terminating recurring", "Non-terminating non-repeating", "Irrational"]),
            ("11/16", "Terminating (denominator 16 = 2⁴)", ["Non-terminating recurring", "Non-terminating non-repeating", "Undefined"]),
            ("3/40", "Terminating (denominator 40 = 2³ * 5)", ["Non-terminating recurring", "Non-terminating non-repeating", "Irrational"]),
            ("19/80", "Terminating (denominator 80 = 2⁴ * 5)", ["Non-terminating recurring", "Non-terminating non-repeating", "Integer"]),
            ("23/125", "Terminating (denominator 125 = 5³)", ["Non-terminating recurring", "Non-terminating non-repeating", "Irrational"]),
            ("31/200", "Terminating (denominator 200 = 2³ * 5²)", ["Non-terminating recurring", "Non-terminating non-repeating", "Non-terminating"]),
            ("7/160", "Terminating (denominator 160 = 2⁵ * 5)", ["Non-terminating recurring", "Non-terminating non-repeating", "Irrational"])
        ],
        'tmpls': [
            "Without actual division, determine whether the rational number \\( {0} \\) has a terminating or non-terminating decimal expansion.",
            "Does the fraction \\( {0} \\) terminate or repeat in its decimal form?",
            "Classify the decimal expansion of \\( {0} \\) without dividing:",
            "In decimal notation, \\( {0} \\) is:",
            "What type of decimal expansion does \\( {0} \\) possess?",
            "Determine the nature of the decimal representation of \\( {0} \\):",
            "Without calculating long division, the fraction \\( {0} \\) yields a:",
            "The decimal form of \\( {0} \\) is:",
            "Identify the decimal character of \\( {0} \\):",
            "State whether \\( {0} \\) is terminating or non-terminating recurring:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Check if fraction is in lowest terms.**\nVerify that numerator and denominator share no common factors.\n\n**Step 2: Prime factorize the denominator.**\nDenominator factorizes into powers of 2 and/or 5 only: \\( 2^m 5^n \\).\n\n**Step 3: State the decimal classification.**\nIt is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Identifying non-terminating recurring decimals without division
    arch2 = {
        'data': [
            ("7/12", "Non-terminating recurring (denominator 12 = 2² * 3, contains factor 3)", ["Terminating", "Non-terminating non-repeating", "Integer"]),
            ("5/6", "Non-terminating recurring (denominator 6 = 2 * 3, contains factor 3)", ["Terminating", "Non-terminating non-repeating", "Irrational"]),
            ("11/15", "Non-terminating recurring (denominator 15 = 3 * 5, contains factor 3)", ["Terminating", "Non-terminating non-repeating", "Terminating with period 2"]),
            ("8/21", "Non-terminating recurring (denominator 21 = 3 * 7, contains factors 3 and 7)", ["Terminating", "Non-terminating non-repeating", "Irrational"]),
            ("13/30", "Non-terminating recurring (denominator 30 = 2 * 3 * 5, contains factor 3)", ["Terminating", "Non-terminating non-repeating", "Terminates after 3 digits"]),
            ("4/9", "Non-terminating recurring (denominator 9 = 3²)", ["Terminating", "Non-terminating non-repeating", "Irrational"]),
            ("17/35", "Non-terminating recurring (denominator 35 = 5 * 7, contains factor 7)", ["Terminating", "Non-terminating non-repeating", "Terminating"]),
            ("2/7", "Non-terminating recurring (denominator 7 is prime ≠ 2, 5)", ["Terminating", "Non-terminating non-repeating", "Integer"]),
            ("19/45", "Non-terminating recurring (denominator 45 = 3² * 5, contains factor 3)", ["Terminating", "Non-terminating non-repeating", "Terminating"]),
            ("1/14", "Non-terminating recurring (denominator 14 = 2 * 7, contains factor 7)", ["Terminating", "Non-terminating non-repeating", "Irrational"])
        ],
        'tmpls': [
            "Without actual division, determine whether \\( {0} \\) has a terminating or non-terminating recurring decimal expansion.",
            "Classify the decimal expansion of \\( {0} \\):",
            "What type of decimal is generated by \\( {0} \\)?",
            "Determine the nature of the decimal representation of \\( {0} \\):",
            "Without performing long division, \\( {0} \\) has a decimal expansion that is:",
            "Identify the decimal character of \\( {0} \\):",
            "In decimal notation, the fraction \\( {0} \\) represents a:",
            "Does \\( {0} \\) terminate or repeat indefinitely?",
            "State whether \\( {0} \\) has a terminating or non-terminating recurring expansion:",
            "What is the decimal expansion type of \\( {0} \\)?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Check if fraction is in lowest terms.**\nThe fraction \\( {item[0]} \\) is in irreducible form.\n\n**Step 2: Prime factorize the denominator.**\nThe denominator contains prime factors other than 2 or 5.\n\n**Step 3: Conclude the decimal type.**\nIt is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 3: Number of decimal places after which terminating decimal terminates
    arch3 = {
        'data': [
            ("7/8", 8, "2³", 3),
            ("13/25", 25, "5²", 2),
            ("17/16", 16, "2⁴", 4),
            ("19/20", 20, "2² * 5", 2),
            ("33/50", 50, "2 * 5²", 2),
            ("27/40", 40, "2³ * 5", 3),
            ("9/80", 80, "2⁴ * 5", 4),
            ("21/125", 125, "5³", 3),
            ("43/200", 200, "2³ * 5²", 3),
            ("7/250", 250, "2 * 5³", 3)
        ],
        'tmpls': [
            "After how many places of decimal will the decimal expansion of \\( {0} \\) terminate?",
            "The decimal representation of \\( {0} \\) terminates after how many decimal places?",
            "Without actual division, find the number of decimal digits after which \\( {0} \\) terminates:",
            "How many digits will appear after the decimal point in the terminating expansion of \\( {0} \\)?",
            "Determine the number of decimal places of \\( {0} \\):",
            "The fraction \\( {0} \\) terminates after:",
            "Calculate the number of decimal places in \\( {0} \\):",
            "After how many decimal positions does \\( {0} \\) come to an end?",
            "Find the number of decimal digits in the terminating form of \\( {0} \\):",
            "State the number of places of decimals after which \\( {0} \\) terminates:"
        ],
        'calc': lambda item: (
            f"{item[3]} decimal places",
            [
                f"{item[3] + 1} decimal places",
                f"{item[3] - 1} decimal places",
                f"{item[3] + 2} decimal places"
            ],
            f"**Step 1: Prime factorize the denominator.**\nDenominator \\( {item[1]} = {item[2]} \\), which is of the form \\( 2^m 5^n \\).\n\n**Step 2: Find \\( \\max(m, n) \\).**\nThe number of decimal places before termination is equal to \\( \\max(m, n) = {item[3]} \\).\n\n**Step 3: State the number of decimal places.**\nIt terminates after \\( {item[3]} \\) decimal places."
        ),
        'diff': 'medium'
    }

    # Arch 4: Unsimplified fractions that appear non-terminating but terminate after cancellation
    arch4 = {
        'data': [
            ("6/15", "2/5", "Terminating (0.4)", ["Non-terminating recurring", "Irrational", "Integer"]),
            ("21/28", "3/4", "Terminating (0.75)", ["Non-terminating recurring", "Non-terminating non-repeating", "Integer"]),
            ("33/60", "11/20", "Terminating (0.55)", ["Non-terminating recurring", "Non-terminating non-repeating", "Irrational"]),
            ("15/24", "5/8", "Terminating (0.625)", ["Non-terminating recurring", "Non-terminating non-repeating", "Integer"]),
            ("27/72", "3/8", "Terminating (0.375)", ["Non-terminating recurring", "Non-terminating non-repeating", "Irrational"]),
            ("77/210", "11/30", "Non-terminating recurring (0.3666...)", ["Terminating", "Non-terminating non-repeating", "Integer"]),
            ("14/35", "2/5", "Terminating (0.4)", ["Non-terminating recurring", "Non-terminating non-repeating", "Irrational"]),
            ("42/56", "3/4", "Terminating (0.75)", ["Non-terminating recurring", "Non-terminating non-repeating", "Integer"]),
            ("18/45", "2/5", "Terminating (0.4)", ["Non-terminating recurring", "Non-terminating non-repeating", "Irrational"]),
            ("24/30", "4/5", "Terminating (0.8)", ["Non-terminating recurring", "Non-terminating non-repeating", "Integer"])
        ],
        'tmpls': [
            "Determine the nature of the decimal expansion of \\( {0} \\) after reducing to simplest form.",
            "Classify the decimal expansion of \\( {0} \\):",
            "Is the decimal expansion of \\( {0} \\) terminating or non-terminating recurring?",
            "What type of decimal is generated by the fraction \\( {0} \\)?",
            "Identify the decimal character of \\( {0} \\):",
            "Does the decimal form of \\( {0} \\) terminate?",
            "Without calculating, determine whether \\( {0} \\) has a terminating or repeating decimal expansion:",
            "The fraction \\( {0} \\) has a decimal expansion that is:",
            "Examine whether \\( {0} \\) terminates or repeats:",
            "State the nature of the decimal representation of \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[2],
            item[3],
            f"**Step 1: ALWAYS reduce to lowest terms first!**\n\\( {item[0]} = {item[1]} \\).\n\n**Step 2: Inspect denominator of the reduced fraction.**\nCheck the prime factorization of the denominator in lowest terms.\n\n**Step 3: Conclude the decimal type.**\nIt is {item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Periodicity (length of the repeating block of digits)
    arch5 = {
        'data': [
            ("1/3 = 0.333...", 1, "the digit 3"),
            ("1/7 = 0.142857142857...", 6, "the 6 digits '142857'"),
            ("1/11 = 0.090909...", 2, "the 2 digits '09'"),
            ("1/6 = 0.1666...", 1, "the single repeating digit 6"),
            ("1/9 = 0.111...", 1, "the single digit 1"),
            ("1/13 = 0.076923076923...", 6, "the 6 digits '076923'"),
            ("1/99 = 0.010101...", 2, "the 2 repeating digits '01'"),
            ("1/999 = 0.001001...", 3, "the 3 repeating digits '001'"),
            ("4/15 = 0.2666...", 1, "the single repeating digit 6"),
            ("5/11 = 0.454545...", 2, "the 2 digits '45'")
        ],
        'tmpls': [
            "What is the length of the period (periodicity) of the repeating decimal \\( {0} \\)?",
            "How many digits repeat in the periodic block of \\( {0} \\)?",
            "The periodicity of the decimal \\( {0} \\) is:",
            "Find the number of recurring digits in \\( {0} \\):",
            "What is the length of the repeating cycle in \\( {0} \\)?",
            "Determine the period length for \\( {0} \\):",
            "The repeating block of \\( {0} \\) contains how many digits?",
            "Calculate the periodicity of \\( {0} \\):",
            "In \\( {0} \\), the recurring period has length:",
            "How many digits are under the bar in \\( {0} \\)?"
        ],
        'calc': lambda item: (
            f"{item[1]} digit(s)",
            [
                f"{item[1] + 1} digit(s)",
                f"{item[1] + 2} digit(s)",
                f"{item[1] + 3} digit(s)"
            ],
            f"**Step 1: Identify the repeating sequence of digits under the bar.**\nIn the decimal \\( {item[0]} \\), the repeating group is {item[2]}.\n\n**Step 2: Count the digits in the repeating group.**\nLength of the period = {item[1]}.\n\n**Step 3: State the periodicity.**\nThe periodicity is \\( {item[1]} \\) digit(s)."
        ),
        'diff': 'easy'
    }

    # Arch 6: Value of decimal expansion by long division
    arch6 = {
        'data': [
            ("1/8", "0.125", ["0.12", "0.15", "0.1255"]),
            ("3/8", "0.375", ["0.35", "0.38", "0.3755"]),
            ("5/8", "0.625", ["0.65", "0.62", "0.6255"]),
            ("7/8", "0.875", ["0.85", "0.88", "0.8755"]),
            ("1/16", "0.0625", ["0.625", "0.065", "0.062"]),
            ("3/16", "0.1875", ["0.185", "0.188", "0.187"]),
            ("1/25", "0.04", ["0.4", "0.004", "0.044"]),
            ("7/20", "0.35", ["0.32", "0.38", "0.035"]),
            ("11/40", "0.275", ["0.25", "0.28", "0.2755"]),
            ("3/50", "0.06", ["0.6", "0.006", "0.066"])
        ],
        'tmpls': [
            "What is the exact decimal expansion of the rational number \\( {0} \\)?",
            "Express the fraction \\( {0} \\) in decimal form:",
            "The decimal representation of \\( {0} \\) is:",
            "Convert \\( {0} \\) into decimal notation:",
            "Find the decimal value of \\( {0} \\):",
            "Calculate the decimal expansion of \\( {0} \\):",
            "In decimals, the rational number \\( {0} \\) is written as:",
            "Evaluate \\( {0} \\) as a terminating decimal:",
            "Determine the decimal equivalent of \\( {0} \\):",
            "The exact decimal value of \\( {0} \\) is:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Perform division or multiply numerator and denominator to make power of 10.**\nMake the denominator a power of 10: \\( 10, 100, 1000, \\dots \\).\n\n**Step 2: Shift the decimal point.**\nWrite down the digits according to the number of zeroes in the denominator.\n\n**Step 3: State the decimal value.**\nThe decimal form is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 7: Multiple-choice classification of numbers as terminating vs recurring
    arch7 = {
        'data': [
            ("Which of the following fractions has a terminating decimal expansion?", "17/32", ["17/30", "17/21", "17/15"]),
            ("Which of the following fractions has a non-terminating recurring decimal expansion?", "5/18", ["5/16", "5/20", "5/8"]),
            ("Which fraction terminates after exactly 2 decimal places?", "19/20", ["19/8", "19/16", "19/6"]),
            ("Which fraction terminates after exactly 3 decimal places?", "7/8", ["7/10", "7/25", "7/16"]),
            ("Which fraction terminates after exactly 4 decimal places?", "3/16", ["3/8", "3/25", "3/20"]),
            ("Which of the following is an irrational number?", "0.121121112...", ["0.12", "0.121212...", "12/99"]),
            ("Which of the following numbers is a rational number?", "0.375", ["√3", "π", "0.2020020002..."]),
            ("Which of the following numbers has non-terminating recurring decimal form?", "2/3", ["1/4", "3/5", "7/10"]),
            ("The rational number 22/7 has a decimal expansion that is:", "Non-terminating recurring", ["Terminating", "Non-terminating non-repeating", "An integer"]),
            ("Why is π an irrational number while 22/7 is a rational number?", "22/7 is a ratio of two integers p/q, whereas π has non-terminating non-repeating decimal expansion", ["22/7 is an integer", "π equals 22/7 exactly", "Both are rational"])
        ],
        'tmpls': [
            "{0}",
            "Solve the following identification question: {0}",
            "In number systems classification: {0}",
            "Choose the correct option: {0}",
            "Identify the valid statement: {0}",
            "Select the correct answer: {0}",
            "Determine the correct choice: {0}",
            "Which option correctly answers: {0}",
            "From the given options, find: {0}",
            "Analyze and answer: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Check prime factorization of denominator or decimal pattern.**\nRecall that terminating fractions have denominators factoring into \\( 2^m 5^n \\) in lowest terms.\n\n**Step 2: Inspect candidate options.**\nEvaluate each option against the question criteria: '{item[0]}'.\n\n**Step 3: State the correct answer.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 3.1.3: Converting repeating decimals 0.p̄ and 0.pq̄ to fraction form
# ==============================================================================
def gen_3_1_3():
    tc = "CBSE-9-MGM-3-3.1.3"
    tname = "Converting repeating decimals 0.p̄ and 0.pq̄ to fraction form"

    # Arch 0: Pure repeating single digit 0.p̄ = p/9
    arch0 = {
        'data': [
            ("0.\\overline{3}", "1/3", "3/9", 3),
            ("0.\\overline{6}", "2/3", "6/9", 6),
            ("0.\\overline{1}", "1/9", "1/9", 1),
            ("0.\\overline{2}", "2/9", "2/9", 2),
            ("0.\\overline{4}", "4/9", "4/9", 4),
            ("0.\\overline{5}", "5/9", "5/9", 5),
            ("0.\\overline{7}", "7/9", "7/9", 7),
            ("0.\\overline{8}", "8/9", "8/9", 8),
            ("0.\\overline{9}", "1", "9/9", 9),
            ("0.\\overline{3}", "1/3", "3/9", 3)
        ],
        'tmpls': [
            "Express the repeating decimal \\( {0} \\) in the form \\( p/q \\) where \\( p \\) and \\( q \\) are coprime integers.",
            "Convert the recurring decimal \\( {0} \\) into fraction form in lowest terms.",
            "What is the fraction representation of \\( {0} \\)?",
            "In the form \\( p/q \\), the repeating decimal \\( {0} \\) equals:",
            "Find the rational number equal to \\( {0} \\):",
            "Convert \\( {0} \\) to a rational number in simplest form:",
            "The recurring decimal \\( {0} \\) expressed as a rational fraction is:",
            "Write \\( {0} \\) in the form \\( p/q \\) (in simplest form):",
            "Determine the fraction equivalent to \\( {0} \\):",
            "Express \\( {0} \\) as a ratio of two integers in lowest terms:"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"{item[3]}/10",
                f"{item[3]}/11",
                f"{item[3]}/100"
            ],
            f"**Step 1: Let \\( x = {item[0]} = 0.{item[3]}{item[3]}{item[3]}\\dots \\)**\n\n**Step 2: Multiply by 10 (since 1 digit repeats).**\n\\[ 10x = {item[3]}.{item[3]}{item[3]}{item[3]}\\dots \\]\n\n**Step 3: Subtract the first equation from the second.**\n\\[ 10x - x = {item[3]} \\implies 9x = {item[3]} \\implies x = \\frac{{{item[3]}}}{{9}} = {item[1]} \\]\n\nThe fraction is \\( {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Pure repeating two digits 0.pq̄ = pq/99
    arch1 = {
        'data': [
            ("0.\\overline{47}", "47/99", 47),
            ("0.\\overline{23}", "23/99", 23),
            ("0.\\overline{54}", "6/11", 54),
            ("0.\\overline{36}", "4/11", 36),
            ("0.\\overline{18}", "2/11", 18),
            ("0.\\overline{27}", "3/11", 27),
            ("0.\\overline{63}", "7/11", 63),
            ("0.\\overline{72}", "8/11", 72),
            ("0.\\overline{81}", "9/11", 81),
            ("0.\\overline{15}", "5/33", 15)
        ],
        'tmpls': [
            "Express the repeating decimal \\( {0} \\) in the form \\( p/q \\) in simplest terms.",
            "Convert \\( {0} \\) into fraction form \\( p/q \\):",
            "What is the fraction representation of the recurring decimal \\( {0} \\)?",
            "In rational form, \\( {0} \\) is equal to:",
            "Find the fraction equivalent to \\( {0} \\):",
            "Convert the recurring decimal \\( {0} \\) to lowest terms:",
            "The repeating decimal \\( {0} \\) in the form \\( p/q \\) is:",
            "Write \\( {0} \\) as a rational number \\( p/q \\):",
            "Determine the simplified fraction representing \\( {0} \\):",
            "Express \\( {0} \\) as an irreducible fraction:"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"{item[2]}/100",
                f"{item[2]}/90",
                f"{item[2]}/999"
            ],
            f"**Step 1: Let \\( x = {item[0]} = 0.{item[2]}{item[2]}\\dots \\)**\n\n**Step 2: Multiply by 100 (since 2 digits repeat).**\n\\[ 100x = {item[2]}.{item[2]}{item[2]}\\dots \\]\n\n**Step 3: Subtract the two equations.**\n\\[ 100x - x = {item[2]} \\implies 99x = {item[2]} \\implies x = \\frac{{{item[2]}}}{{99}} = {item[1]} \\]\n\nThe fraction is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Mixed repeating decimal with one non-repeating digit: 0.ab̄ = (ab - a)/90
    arch2 = {
        'data': [
            ("0.4\\overline{7}", "43/90", 4, 7, 43),
            ("0.1\\overline{6}", "1/6", 1, 6, 15),
            ("0.2\\overline{3}", "7/30", 2, 3, 21),
            ("0.5\\overline{8}", "53/90", 5, 8, 53),
            ("0.7\\overline{4}", "67/90", 7, 4, 67),
            ("0.8\\overline{3}", "5/6", 8, 3, 75),
            ("0.3\\overline{5}", "16/45", 3, 5, 32),
            ("0.6\\overline{1}", "11/18", 6, 1, 55),
            ("0.2\\overline{7}", "5/18", 2, 7, 25),
            ("0.4\\overline{6}", "7/15", 4, 6, 42)
        ],
        'tmpls': [
            "Convert the mixed recurring decimal \\( {0} \\) into fraction form in simplest terms.",
            "Express the repeating decimal \\( {0} \\) in the form \\( p/q \\):",
            "What is the fraction representation of \\( {0} \\)?",
            "In lowest terms, the recurring decimal \\( {0} \\) equals:",
            "Find the rational number \\( p/q \\) equal to \\( {0} \\):",
            "Convert \\( {0} \\) to an irreducible rational fraction:",
            "The mixed repeating decimal \\( {0} \\) written as \\( p/q \\) is:",
            "Write \\( {0} \\) in the form \\( p/q \\):",
            "Determine the fraction equivalent to \\( {0} \\):",
            "Express \\( {0} \\) as a ratio of integers in simplest form:"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"{item[4]}/100",
                f"{item[4]}/99",
                f"{item[2]}{item[3]}/90"
            ],
            f"**Step 1: Set \\( x = {item[0]} = 0.{item[2]}{item[3]}{item[3]}\\dots \\)**\n\n**Step 2: Multiply by 10 and 100.**\n- \\( 10x = {item[2]}.{item[3]}{item[3]}\\dots \\)\n- \\( 100x = {item[2]}{item[3]}.{item[3]}{item[3]}\\dots \\)\n\n**Step 3: Subtract the equations.**\n\\[ 100x - 10x = {item[2]}{item[3]} - {item[2]} = {item[4]} \\implies 90x = {item[4]} \\implies x = \\frac{{{item[4]}}}{{90}} = {item[1]} \\]\n\nThe fraction is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Pure repeating three digits 0.pqr̄ = pqr/999
    arch3 = {
        'data': [
            ("0.\\overline{001}", "1/999", 1),
            ("0.\\overline{123}", "41/333", 123),
            ("0.\\overline{234}", "26/111", 234),
            ("0.\\overline{135}", "5/37", 135),
            ("0.\\overline{027}", "1/37", 27),
            ("0.\\overline{037}", "1/27", 37),
            ("0.\\overline{216}", "8/37", 216),
            ("0.\\overline{297}", "11/37", 297),
            ("0.\\overline{432}", "16/37", 432),
            ("0.\\overline{999}", "1", 999)
        ],
        'tmpls': [
            "Express the repeating decimal \\( {0} \\) in the form \\( p/q \\) in lowest terms.",
            "Convert \\( {0} \\) into fraction form \\( p/q \\):",
            "What is the fraction representation of \\( {0} \\)?",
            "In rational form, the recurring decimal \\( {0} \\) equals:",
            "Find the fraction equivalent to \\( {0} \\):",
            "Convert \\( {0} \\) to a rational number in simplest form:",
            "The repeating decimal \\( {0} \\) in the form \\( p/q \\) is:",
            "Write \\( {0} \\) as a rational number in lowest terms:",
            "Determine the simplified fraction representing \\( {0} \\):",
            "Express \\( {0} \\) as an irreducible fraction:"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"{item[2]}/1000",
                f"{item[2]}/900",
                f"{item[2]}/990"
            ],
            f"**Step 1: Set \\( x = {item[0]} \\).**\nSince 3 digits repeat under the bar, multiply by \\( 10^3 = 1000 \\).\n\n**Step 2: Subtract the equations.**\n\\[ 1000x - x = {item[2]} \\implies 999x = {item[2]} \\implies x = \\frac{{{item[2]}}}{{999}} \\]\n\n**Step 3: Reduce to lowest terms.**\nThe fraction in lowest terms is \\( {item[1]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Numbers with non-zero integer parts: e.g. 1.p̄ or 2.pq̄
    arch4 = {
        'data': [
            ("1.\\overline{27}", "14/11", 1, 27),
            ("2.\\overline{3}", "7/3", 2, 3),
            ("1.\\overline{3}", "4/3", 1, 3),
            ("3.\\overline{6}", "11/3", 3, 6),
            ("2.\\overline{45}", "27/11", 2, 45),
            ("1.\\overline{18}", "13/11", 1, 18),
            ("4.\\overline{6}", "14/3", 4, 6),
            ("2.\\overline{142857}", "15/7", 2, 142857),
            ("1.\\overline{4}", "13/9", 1, 4),
            ("3.\\overline{14}", "311/99", 3, 14)
        ],
        'tmpls': [
            "Express the repeating decimal \\( {0} \\) in the form \\( p/q \\) in simplest terms.",
            "Convert \\( {0} \\) into fraction form \\( p/q \\):",
            "What is the fraction representation of \\( {0} \\)?",
            "In lowest terms, the recurring decimal \\( {0} \\) equals:",
            "Find the rational number \\( p/q \\) equal to \\( {0} \\):",
            "Convert \\( {0} \\) to an irreducible rational fraction:",
            "The repeating decimal \\( {0} \\) written as \\( p/q \\) is:",
            "Write \\( {0} \\) in the form \\( p/q \\):",
            "Determine the fraction equivalent to \\( {0} \\):",
            "Express \\( {0} \\) as an improper fraction in simplest form:"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"{item[1].split('/')[0]}/{int(item[1].split('/')[1]) + 1}",
                f"{int(item[1].split('/')[0]) + 1}/{item[1].split('/')[1]}",
                f"{item[2]}.{item[3]}/10"
            ],
            f"**Step 1: Separate integer and decimal repeating parts.**\n\\[ {item[0]} = {item[2]} + 0.\\overline{{{item[3]}}} \\]\n\n**Step 2: Convert the repeating decimal to fraction form.**\nAdd the integer part \\( {item[2]} \\) to the fractional value.\n\n**Step 3: Combine into an improper fraction in lowest terms.**\nThe fraction is \\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 5: Sum and operations on repeating decimals (e.g. 0.3̄ + 0.4̄)
    arch5 = {
        'data': [
            ("0.\\overline{3} + 0.\\overline{4}", "7/9", "0.\\overline{7}"),
            ("0.\\overline{6} + 0.\\overline{3}", "1", "0.\\overline{9} = 1"),
            ("0.\\overline{2} + 0.\\overline{5}", "7/9", "0.\\overline{7}"),
            ("0.\\overline{12} + 0.\\overline{34}", "46/99", "0.\\overline{46}"),
            ("0.\\overline{4} + 0.\\overline{5}", "1", "0.\\overline{9} = 1"),
            ("0.\\overline{7} - 0.\\overline{2}", "5/9", "0.\\overline{5}"),
            ("0.\\overline{8} - 0.\\overline{5}", "1/3", "3/9 = 1/3"),
            ("0.\\overline{23} + 0.\\overline{32}", "5/9", "55/99 = 5/9"),
            ("0.\\overline{45} + 0.\\overline{54}", "1", "99/99 = 1"),
            ("0.\\overline{6} - 0.\\overline{3}", "1/3", "3/9 = 1/3")
        ],
        'tmpls': [
            "Find the value of \\( {0} \\) in fraction form \\( p/q \\).",
            "Calculate \\( {0} \\) and express the answer in lowest terms:",
            "What is the sum/difference \\( {0} \\) in fractional form?",
            "Evaluate \\( {0} \\) as a rational number \\( p/q \\):",
            "Compute \\( {0} \\) in simplest terms:",
            "Determine the value of \\( {0} \\):",
            "The arithmetic result of \\( {0} \\) as a fraction is:",
            "Find the fraction equal to \\( {0} \\):",
            "Solve the expression \\( {0} \\) in the form \\( p/q \\):",
            "Calculate \\( {0} \\) and express as an irreducible fraction:"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"{item[1].split('/')[0] if '/' in item[1] else '1'}/10",
                f"{int(item[1].split('/')[0]) + 1 if '/' in item[1] else '2'}/{item[1].split('/')[1] if '/' in item[1] else '9'}",
                "0"
            ],
            f"**Step 1: Convert each repeating decimal to fraction form.**\nConvert each component into fractions with common denominator 9 or 99.\n\n**Step 2: Perform the addition or subtraction.**\nAdd or subtract the numerators.\n\n**Step 3: Reduce to simplest form.**\nThe result is \\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 6: The curious case of 0.999... = 1
    arch6 = {
        'data': [
            ("0.\\overline{9} = 0.999...", "1", ["0.9", "0.99", "an infinitely close number strictly less than 1"], "Let x = 0.999... Then 10x = 9.999... Subtracting gives 9x = 9 => x = 1."),
            ("Why does 0.999... exactly equal 1?", "Because the difference 1 - 0.999... = 0 and 9/9 = 1", ["It is an approximation", "It equals 0.999", "Calculators round it up"]),
            ("Express 0.999... in the form p/q in simplest form:", "1", ["9/10", "99/100", "0.999/1"]),
            ("What is the decimal expansion 1.999... equal to?", "2", ["1.9", "1.99", "undefined"]),
            ("What is the decimal expansion 3.999... equal to?", "4", ["3.9", "3.99", "3.999"]),
            ("What is the decimal expansion 0.0999... equal to?", "1/10 (0.1)", ["0.09", "0.099", "9/90"]),
            ("If x = 0.999..., then 10x - x equals:", "9", ["8.999...", "9.999...", "0.999..."]),
            ("Is there any real number strictly between 0.999... and 1?", "No, because they are two different representations of the exact same real number", ["Yes, 0.99995", "Yes, infinitely many", "Yes, 0.9999"]),
            ("The fraction 9/9 equals:", "1", ["0.9", "0.99", "9.9"]),
            ("Every terminating decimal can also be written as a recurring decimal ending in:", "infinitely repeating 9s (e.g. 1 = 0.999...)", ["infinitely repeating 1s", "infinitely repeating 5s", "it cannot be rewritten"])
        ],
        'tmpls': [
            "{0}",
            "In real analysis and coordinate mathematics: {0}",
            "Consider the repeating decimal 0.999...: {0}",
            "Choose the mathematically correct fact: {0}",
            "Identify the accurate statement: {0}",
            "Which of the following correctly describes: {0}?",
            "Regarding the equivalence of repeating decimals: {0}",
            "Determine the true statement: {0}",
            "Select the correct answer: {0}",
            "What is the mathematical truth regarding: {0}?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Algebraic proof of \\( 0.\\overline{9} = 1 \\).**\nLet \\( x = 0.9999\\dots \\).\nThen \\( 10x = 9.9999\\dots \\).\nSubtracting yields \\( 9x = 9 \\implies x = 1 \\).\n\n**Step 2: Understand non-uniqueness of decimal expansions.**\nEvery non-zero terminating decimal has an equivalent representation ending in an infinite string of 9s.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Mixed repeating decimals with multiple non-repeating and repeating digits: 0.ab̄cd
    arch7 = {
        'data': [
            ("0.12\\overline{3}", "37/300", 12, 3, 111, 900),
            ("0.23\\overline{5}", "212/900 = 53/225", 23, 5, 212, 900),
            ("0.1\\overline{23}", "61/495", 1, 23, 122, 990),
            ("0.2\\overline{35}", "233/990", 2, 35, 233, 990),
            ("0.3\\overline{15}", "52/165", 3, 15, 312, 990),
            ("0.13\\overline{6}", "61/450", 13, 6, 123, 900),
            ("0.0\\overline{12}", "4/330 = 2/165", 0, 12, 12, 990),
            ("0.4\\overline{12}", "136/330 = 68/165", 4, 12, 408, 990),
            ("0.0\\overline{45}", "1/22", 0, 45, 45, 990),
            ("0.05\\overline{6}", "17/300", 5, 6, 51, 900)
        ],
        'tmpls': [
            "Convert the mixed recurring decimal \\( {0} \\) into fraction form in simplest terms.",
            "Express \\( {0} \\) in the form \\( p/q \\) in lowest terms:",
            "What is the irreducible fraction representation of \\( {0} \\)?",
            "In simplest terms, the repeating decimal \\( {0} \\) equals:",
            "Find the rational number \\( p/q \\) equal to \\( {0} \\):",
            "Convert \\( {0} \\) to a rational fraction in simplest terms:",
            "The recurring decimal \\( {0} \\) written in the form \\( p/q \\) is:",
            "Write \\( {0} \\) as an irreducible rational fraction:",
            "Determine the fraction equivalent to \\( {0} \\):",
            "Express \\( {0} \\) as a ratio of coprime integers:"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"{item[4]}/1000",
                f"{item[4]}/999",
                f"{item[4] + 2}/{item[5]}"
            ],
            f"**Step 1: Set up the equations with powers of 10.**\nLet \\( x = {item[0]} \\).\nMultiply by powers of 10 to align the repeating decimal parts.\n\n**Step 2: Subtract the equations.**\nSubtract to eliminate the infinite recurring tail: \\( \\text{{denominator}} \\cdot x = {item[4]} \\).\n\n**Step 3: Simplify to lowest terms.**\nThe fraction in lowest terms is \\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])

if __name__ == "__main__":
    q1 = gen_3_1_1()
    q2 = gen_3_1_2()
    q3 = gen_3_1_3()
    print(f"gen_3_1_1: {len(q1)} questions generated")
    print(f"gen_3_1_2: {len(q2)} questions generated")
    print(f"gen_3_1_3: {len(q3)} questions generated")
