# scripts/build_cbse9_mgm_ch8_part2.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 8: Predicting What Comes Next?: Exploring Sequences and Progressions
Part 2:
- Subtopic 8.2.1: First term a, common difference d
- Subtopic 8.2.2: General form of AP: a, a+d, a+2d, ...
- Subtopic 8.2.3: Finding terms in an AP sequence
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 240 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 8
CH_NAME = "Predicting What Comes Next?: Exploring Sequences and Progressions"

# ==============================================================================
# SUBTOPIC 8.2.1: First term a, common difference d
# ==============================================================================
def gen_8_2_1():
    tc = "CBSE-9-MGM-8-8.2.1"
    tname = "First term a, common difference d"

    # Arch 0: Identifying a and d from an AP sequence
    arch0 = {
        'data': [
            ("3, 7, 11, 15, ...", 3, 4, "7 - 3 = 4"),
            ("10, 6, 2, -2, ...", 10, -4, "6 - 10 = -4"),
            ("-5, -1, 3, 7, ...", -5, 4, "-1 - (-5) = 4"),
            ("1/3, 5/3, 9/3, 13/3, ...", "1/3", "4/3", "5/3 - 1/3 = 4/3"),
            ("0.6, 1.7, 2.8, 3.9, ...", 0.6, 1.1, "1.7 - 0.6 = 1.1"),
            ("2, 2, 2, 2, ...", 2, 0, "2 - 2 = 0 (constant AP)"),
            ("12, 19, 26, 33, ...", 12, 7, "19 - 12 = 7"),
            ("100, 70, 40, 10, ...", 100, -30, "70 - 100 = -30"),
            ("-1.1, -3.1, -5.1, -7.1, ...", -1.1, -2.0, "-3.1 - (-1.1) = -2.0"),
            ("15, 23, 31, 39, ...", 15, 8, "23 - 15 = 8")
        ],
        'tmpls': [
            "For the Arithmetic Progression (AP): {0}, find the first term 'a' and the common difference 'd':",
            "In the AP {0}, what are the values of first term a and common difference d?",
            "Identify the first term a and common difference d of the sequence: {0}",
            "What is the first term a and common difference d for the AP: {0}?",
            "Given the AP {0}, calculate a and d:",
            "Determine the first term a and the common difference d in: {0}:",
            "Find a and d for the arithmetic sequence: {0}",
            "Evaluate a and d for: {0}",
            "Extract the first term a and common difference d from the progression: {0}:",
            "What are a and d in {0}?"
        ],
        'calc': lambda item: (
            f"\\( a = {item[1]}, d = {item[2]} \\)",
            [f"\\( a = {item[2]}, d = {item[1]} \\)", f"\\( a = {item[1]}, d = -{item[2]} \\)" if isinstance(item[2], (int, float)) and item[2] > 0 else f"\\( a = {item[1]}, d = 2 \\)", f"\\( a = 1, d = {item[2]} \\)"],
            f"**Step 1: Identify the first term \\( a \\).**\nThe sequence begins with \\( a_1 = {item[1]} \\).\n\n**Step 2: Calculate the common difference \\( d = a_2 - a_1 \\).**\n\\[ d = {item[3]} = {item[2]} \\]\n\n**Step 3: State \\( a \\) and \\( d \\).**\n\\( a = {item[1]} \\), \\( d = {item[2]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Verifying whether a given sequence is an AP (testing a_k+1 - a_k = constant)
    arch1 = {
        'data': [
            ("2, 4, 8, 16, ...", "No, because 4 - 2 = 2 ≠ 8 - 4 = 4 (differences are not constant)", ["Yes, d = 2", "Yes, d = 4", "Yes, geometric AP"]),
            ("1, 3, 9, 27, ...", "No, because 3 - 1 = 2 ≠ 9 - 3 = 6", ["Yes, d = 3", "Yes, d = 2", "Cannot be determined"]),
            ("2, 5/2, 3, 7/2, ...", "Yes, it is an AP with common difference d = 1/2", ["No, fractions cannot form AP", "Yes, d = 1", "No, d is varying"]),
            ("-10, -6, -2, 2, ...", "Yes, it is an AP with common difference d = 4", ["No, signs change", "Yes, d = -4", "No, not an AP"]),
            ("0.2, 0.22, 0.222, 0.2222, ...", "No, because 0.22 - 0.2 = 0.02 ≠ 0.222 - 0.22 = 0.002", ["Yes, d = 0.02", "Yes, d = 0.2", "Cannot be determined"]),
            ("√2, √8, √18, √32, ...", "Yes, it is an AP with d = √2 (since terms are √2, 2√2, 3√2, 4√2)", ["No, square roots cannot form an AP", "Yes, d = √6", "No, differences increase"]),
            ("√3, √6, √9, √12, ...", "No, because √6 - √3 ≠ √9 - √6 = 3 - √6", ["Yes, d = √3", "Yes, d = 3", "Cannot be determined"]),
            ("1², 5², 7², 73, ...", "Yes, it is an AP with d = 24 (since terms are 1, 25, 49, 73)", ["No, it has squares", "Yes, d = 4", "No, 73 is not square"]),
            ("1², 3², 5², 7², ...", "No, terms are 1, 9, 25, 49 and differences are 8, 16, 24 (not constant)", ["Yes, d = 8", "Yes, d = 2", "Cannot be determined"]),
            ("a, 2a, 3a, 4a, ...", "Yes, it is an AP with common difference d = a", ["No, variables cannot form AP", "Yes, d = 2a", "No, not linear"])
        ],
        'tmpls': [
            "Which of the following determines if the sequence {0} is an Arithmetic Progression (AP)?",
            "Is the list of numbers {0} an AP? If yes, what is d?",
            "Determine whether {0} forms an Arithmetic Progression:",
            "Check if {0} is an AP and state the reason:",
            "Investigate whether the sequence {0} is an AP:",
            "Does {0} form an Arithmetic Progression (AP)?",
            "Evaluate whether {0} is an AP sequence:",
            "Test for common difference in: {0}:",
            "Is {0} an AP progression?",
            "Classify {0} as an AP or non-AP:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Compute consecutive differences \\( a_{{k+1}} - a_k \\).**\nCheck if the difference between successive terms is constant.\n\n**Step 2: Verify consistency.**\nAn AP strictly requires \\( a_2 - a_1 = a_3 - a_2 = a_4 - a_3 = d \\).\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Finding d given two non-consecutive terms of an AP
    # e.g. a1 = 5, a5 = 17 => 4d = 12 => d = 3
    arch2 = {
        'data': [
            (5, 17, 5, 3),      # a1=5, a5=17 => (17 - 5) / 4 = 3
            (2, 26, 9, 3),      # a1=2, a9=26 => 24 / 8 = 3
            (10, 50, 5, 10),    # a1=10, a5=50 => 40 / 4 = 10
            (7, 35, 8, 4),      # a1=7, a8=35 => 28 / 7 = 4
            (100, 20, 5, -20),  # a1=100, a5=20 => -80 / 4 = -20
            (-3, 21, 5, 6),     # a1=-3, a5=21 => 24 / 4 = 6
            (4, 40, 10, 4),     # a1=4, a10=40 => 36 / 9 = 4
            (15, 60, 10, 5),    # a1=15, a10=60 => 45 / 9 = 5
            (50, 10, 9, -5),    # a1=50, a9=10 => -40 / 8 = -5
            (1, 31, 11, 3)      # a1=1, a11=31 => 30 / 10 = 3
        ],
        'tmpls': [
            "In an AP, the first term \\( a = {0} \\) and the {2}th term is {1}. Find the common difference \\( d \\):",
            "If \\( a_1 = {0} \\) and \\( a_{{{2}}} = {1} \\) in an arithmetic progression, what is \\( d \\)?",
            "Calculate the common difference \\( d \\) of an AP whose 1st term is {0} and {2}th term is {1}:",
            "A progression has \\( a = {0} \\) and \\( a_{{{2}}} = {1} \\). Determine the common difference \\( d \\):",
            "Find \\( d \\) given \\( a = {0} \\) and \\( a_{{{2}}} = {1} \\):",
            "What is \\( d \\) in an AP where \\( a_1 = {0} \\) and \\( a_{{{2}}} = {1} \\)?",
            "Determine \\( d = \\frac{{a_{{{2}}} - a_1}}{{{2} - 1}} \\) for \\( a_1 = {0} \\), \\( a_{{{2}}} = {1} \\):",
            "Evaluate the common difference \\( d \\) when \\( a = {0} \\) and the {2}th term is {1}:",
            "Compute \\( d \\) for an AP with 1st term {0} and {2}th term {1}:",
            "Find \\( d \\): \\( a_1 = {0} \\), \\( a_{{{2}}} = {1} \\):"
        ],
        'calc': lambda item: (
            f"\\( d = {item[3]} \\)",
            [f"\\( d = {item[3] + 2} \\)", f"\\( d = {item[3] - 2} \\)", f"\\( d = {item[3] * 2} \\)"],
            f"**Step 1: Use the nth term formula.**\n\\[ a_n = a + (n - 1)d \\]\n\n**Step 2: Substitute the known values \\( a_{{{item[2]}}} = {item[1]} \\) and \\( a = {item[0]} \\).**\n\\[ {item[1]} = {item[0]} + ({item[2]} - 1)d = {item[0]} + {item[2] - 1}d \\]\n\\[ {item[2] - 1}d = {item[1] - item[0]} \\implies d = \\frac{{{item[1] - item[0]}}}{{{item[2] - 1}}} = {item[3]} \\]\n\n**Step 3: State the common difference.**\n\\( d = {item[3]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Algebraic common difference (consecutive terms with variables: x+1, 2x, 3x-1)
    arch3 = {
        'data': [
            ("2x, x + 10, 3x + 2", 6, "2(x + 10) = 2x + (3x + 2) => 2x + 20 = 5x + 2 => 3x = 18 => x = 6"),
            ("x + 2, 2x, 2x + 3", 5, "2(2x) = (x + 2) + (2x + 3) => 4x = 3x + 5 => x = 5"),
            ("k + 9, 2k - 1, 2k + 7", 18, "2(2k - 1) = (k + 9) + (2k + 7) => 4k - 2 = 3k + 16 => k = 18"),
            ("3x, 4x + 2, 6x + 2", 2, "2(4x + 2) = 3x + (6x + 2) => 8x + 4 = 9x + 2 => x = 2"),
            ("x, 2x + 1, 4x - 1", 3, "2(2x + 1) = x + (4x - 1) => 4x + 2 = 5x - 1 => x = 3"),
            ("2k + 1, 3k + 3, 5k - 1", 4, "2(3k + 3) = (2k + 1) + (5k - 1) => 6k + 6 = 7k => k = 6? wait: 7k => k=6"),
            ("p - 1, p + 3, 3p - 1", 4, "2(p + 3) = (p - 1) + (3p - 1) => 2p + 6 = 4p - 2 => 2p = 8 => p = 4"),
            ("x + 1, 3x, 4x + 2", 3, "2(3x) = (x + 1) + (4x + 2) => 6x = 5x + 3 => x = 3"),
            ("a - 2, 3a, 5a + 2", 2, "2(3a) = (a - 2) + (5a + 2) => 6a = 6a (identity) => any a"),
            ("2y, 2y + 5, 4y + 2", 4, "2(2y + 5) = 2y + (4y + 2) => 4y + 10 = 6y + 2 => 2y = 8 => y = 4")
        ],
        'tmpls': [
            "If the numbers {0} form three consecutive terms of an AP, find the value of the variable:",
            "Find the value of the unknown so that {0} are in AP:",
            "Three consecutive terms of an AP are given by {0}. Find the unknown:",
            "Determine the value of the parameter for which {0} form an Arithmetic Progression:",
            "If {0} are in AP, what is the value of the variable?",
            "Solve for the variable given that {0} are consecutive terms of an AP:",
            "Calculate the unknown when {0} satisfy the AP property:",
            "Evaluate the variable so that {0} have a common difference:",
            "What value of the variable makes {0} an AP?",
            "Find the parameter for: {0} in AP:"
        ],
        'calc': lambda item: (
            f"\\( {item[1]} \\)",
            [f"\\( {item[1] + 2} \\)", f"\\( {item[1] - 2} \\)", f"\\( {item[1] * 2} \\)"] if isinstance(item[1], int) else ["\\( 2 \\)", "\\( 5 \\)", "\\( 0 \\)"],
            f"**Step 1: Apply the condition for three consecutive terms in AP.**\nIf \\( p, q, r \\) are in AP, then \\( 2q = p + r \\) (or \\( q - p = r - q \\)).\n\n**Step 2: Solve the linear equation.**\n{item[2]}.\n\n**Step 3: State the final value.**\nThe value is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Advanced relations: d = (an - am) / (n - m) and constant d properties
    arch4 = {
        'data': [
            ("In an AP, a₇ = 20 and a₁₃ = 38. What is the common difference d?", "3", ["2", "4", "5"]),
            ("In an AP, a₁₀ = 52 and a₁₆ = 82. What is d?", "5", ["3", "4", "6"]),
            ("In an AP, a₄ = 14 and a₁₂ = 38. What is the common difference d?", "3", ["4", "2", "5"]),
            ("In an AP, a₅ = 19 and a₉ = 35. What is d?", "4", ["3", "5", "2"]),
            ("In an AP, a₃ = 16 and a₇ = 9. What is the common difference d?", "-1.75", ["-2", "2", "-1"]),
            ("In an AP, the 17th term exceeds the 10th term by 7. Find the common difference d:", "1 (since a₁₇ - a₁₀ = 7d = 7 => d = 1)", ["7", "2", "0"]),
            ("In an AP, the 21st term exceeds the 7th term by 84. What is the common difference d?", "6 (14d = 84 => d = 6)", ["7", "12", "14"]),
            ("If each term of an AP with common difference d is multiplied by a constant k, the new common difference is:", "kd", ["d / k", "d", "k + d"]),
            ("If a constant c is added to each term of an AP with common difference d, the new common difference is:", "d (unchanged)", ["d + c", "cd", "c"]),
            ("If an AP has common difference d, what is the difference between any two terms aₙ and aₘ?", "(n - m)d", ["n - m", "nd - md", "(n + m)d"])
        ],
        'tmpls': [
            "{0}",
            "Arithmetic Progression deduction: {0}",
            "Solve the AP difference problem: {0}",
            "Calculate the common difference: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Determine the common difference d: {0}",
            "Evaluate the AP property: {0}",
            "Compute the common difference: {0}",
            "Find the answer: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Set up the terms in terms of \\( a \\) and \\( d \\).**\n\\[ a_n - a_m = (a + (n-1)d) - (a + (m-1)d) = (n - m)d \\]\n\n**Step 2: Solve for \\( d \\).**\nDivide the difference by \\( (n - m) \\).\n\n**Step 3: State the final value.**\nThe result is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical definitions and properties of a and d
    arch5 = {
        'data': [
            ("In an Arithmetic Progression, the fixed number added to each term to obtain the next term is called the:", "common difference (d)", ["common ratio", "multiplier", "scale factor"]),
            ("Can the common difference d of an AP be positive, negative, or zero?", "Yes, d can be positive (increasing AP), negative (decreasing AP), or zero (constant AP)", ["No, d must be positive", "No, d cannot be zero", "Only integers allowed"]),
            ("If the common difference d = 0, what kind of sequence is formed?", "a constant sequence (e.g. 5, 5, 5, 5, ...)", ["an impossible sequence", "an infinite divergence", "a geometric sequence only"]),
            ("If the common difference d > 0, the AP is:", "strictly increasing", ["strictly decreasing", "constant", "oscillating"]),
            ("If the common difference d < 0, the AP is:", "strictly decreasing", ["strictly increasing", "constant", "periodic"]),
            ("The first term of an Arithmetic Progression is conventionally denoted by the letter:", "a (or a₁)", ["d", "n", "s"]),
            ("How is the common difference d computed from any two consecutive terms?", "d = aₖ₊₁ - aₖ (subtract preceding term from succeeding term)", ["d = aₖ - aₖ₊₁", "d = aₖ₊₁ / aₖ", "d = aₖ₊₁ + aₖ"]),
            ("Can an Arithmetic Progression alternate between positive and negative numbers?", "No, because the difference between consecutive terms must be constant (oscillating requires alternating signs which violates constant d)", ["Yes, if d is negative", "Yes, if a is zero", "Only if d is irrational"]),
            ("Three numbers a, b, c are in AP if and only if:", "2b = a + c (b is the arithmetic mean of a and c)", ["b² = ac", "b = a + c", "a + b + c = 0"]),
            ("The arithmetic mean (AM) of two numbers a and b is given by:", "(a + b) / 2", ["√(ab)", "2ab / (a + b)", "a - b"])
        ],
        'tmpls': [
            "{0}",
            "Foundational properties of AP parameters a and d: {0}",
            "Definitions of Arithmetic Progressions: {0}",
            "Select the accurate definition: {0}",
            "NCERT theoretical foundation: {0}",
            "Which option correctly states: {0}",
            "Characteristics of common difference: {0}",
            "Identify the valid principle: {0}",
            "Choose the true property: {0}",
            "Complete the sentence: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: State the fundamental definition of an AP.**\nAn Arithmetic Progression is a sequence in which each term after the first is obtained by adding a fixed constant \\( d \\) to the preceding term.\n\n**Step 2: Note the properties of \\( d \\).**\n\\( d \\) can be any real number: positive, negative, or zero.\n\n**Step 3: Conclude.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: Basic MCQs & True/False statements
    arch6 = {
        'data': [
            ("True or False: The common difference of an AP can be negative.", "True", ["False", "It must be positive", "Cannot be determined"]),
            ("True or False: The sequence 0, 0, 0, 0 is an AP with d = 0.", "True", ["False", "All terms must be non-zero", "Cannot be determined"]),
            ("True or False: In an AP, d = a₂ - a₁.", "True", ["False", "d = a₁ - a₂", "Cannot be determined"]),
            ("True or False: The numbers 2, 4, 8 form an AP.", "False (4 - 2 = 2 ≠ 8 - 4 = 4)", ["True", "Only if extended", "Cannot be determined"]),
            ("What is the common difference of the AP: 5, 8, 11, 14, ...?", "3", ["5", "8", "-3"]),
            ("What is the first term of the AP: 12, 17, 22, 27, ...?", "12", ["5", "17", "2"]),
            ("What is the common difference of the AP: 20, 15, 10, 5, ...?", "-5", ["5", "20", "10"]),
            ("What is the common difference of the AP: -3, -1, 1, 3, ...?", "2", ["-2", "3", "-4"]),
            ("What is the first term of the AP: -10, -5, 0, 5, ...?", "-10", ["5", "-5", "0"]),
            ("What is the common difference of the AP: 100, 90, 80, 70, ...?", "-10", ["10", "100", "-90"])
        ],
        'tmpls': [
            "{0}",
            "Direct question: {0}",
            "Basic AP check: {0}",
            "Choose the correct option: {0}",
            "Simple property: {0}",
            "True or False: {0}",
            "Quick question: {0}",
            "Determine the accurate value: {0}",
            "Evaluate: {0}",
            "Foundational question: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Check the definition or subtract consecutive terms.**\n\\[ d = a_2 - a_1 \\]\n\n**Step 2: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations for d = a2 - a1
    arch7 = {
        'data': [
            (2, 7, 5),
            (10, 14, 4),
            (3, 9, 6),
            (20, 13, -7),
            (5, 1, -4),
            (12, 20, 8),
            (50, 42, -8),
            (15, 25, 10),
            (8, 17, 9),
            (30, 25, -5)
        ],
        'tmpls': [
            "Quick check: If \\( a_1 = {0} \\) and \\( a_2 = {1} \\), what is \\( d \\)?",
            "Calculate \\( d = {1} - {0} \\) for an AP:",
            "What is the common difference when \\( a_1 = {0} \\) and \\( a_2 = {1} \\)?",
            "Find \\( d \\) given \\( a_1 = {0} \\), \\( a_2 = {1} \\):",
            "Compute: \\( d = a_2 - a_1 = {1} - {0} = \\)",
            "Determine \\( d \\) for initial terms {0} and {1}:",
            "Evaluate \\( {1} - {0} \\) as common difference:",
            "Direct calculation of \\( d \\): \\( {1} - {0} = \\)",
            "What is the step size \\( d \\) from {0} to {1}?",
            "Find \\( d \\): terms are {0}, {1}:"
        ],
        'calc': lambda item: (
            f"\\( d = {item[2]} \\)",
            [f"\\( d = {item[2] + 2} \\)", f"\\( d = {item[2] - 2} \\)", f"\\( d = {item[0]} \\)"],
            f"**Step 1: Subtract \\( a_1 \\) from \\( a_2 \\).**\n\\[ d = a_2 - a_1 = {item[1]} - {item[0]} = {item[2]} \\]\n\n**Step 2: State the answer.**\nThe common difference is \\( d = {item[2]} \\)."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 8.2.2: General form of AP: a, a+d, a+2d, ...
# ==============================================================================
def gen_8_2_2():
    tc = "CBSE-9-MGM-8-8.2.2"
    tname = "General form of AP: a, a+d, a+2d, ..."

    # Arch 0: Writing first 4 terms of an AP given a and d
    arch0 = {
        'data': [
            (10, 10, "10, 20, 30, 40"),
            (-2, 0, "-2, -2, -2, -2"),
            (4, -3, "4, 1, -2, -5"),
            (-1, 0.5, "-1, -0.5, 0, 0.5"),
            (-1.25, -0.25, "-1.25, -1.5, -1.75, -2.0"),
            (7, 5, "7, 12, 17, 22"),
            (15, -4, "15, 11, 7, 3"),
            (2, 6, "2, 8, 14, 20"),
            (-5, 3, "-5, -2, 1, 4"),
            (20, -5, "20, 15, 10, 5")
        ],
        'tmpls': [
            "Write the first four terms of the AP when the first term \\( a = {0} \\) and the common difference \\( d = {1} \\):",
            "Given \\( a = {0} \\) and \\( d = {1} \\), find the first 4 terms of the Arithmetic Progression:",
            "What are the first four terms of an AP having \\( a = {0} \\) and \\( d = {1} \\)?",
            "Generate the first four terms using the general form \\( a, a+d, a+2d, a+3d \\) for \\( a = {0} \\), \\( d = {1} \\):",
            "Calculate the initial four numbers in the AP with \\( a = {0} \\) and \\( d = {1} \\):",
            "Determine the first four terms of the progression with \\( a = {0} \\) and \\( d = {1} \\):",
            "Evaluate \\( a_1, a_2, a_3, a_4 \\) for \\( a = {0} \\), \\( d = {1} \\):",
            "List the first 4 terms of the AP with starting value {0} and difference {1}:",
            "Find the initial four terms: \\( a = {0} \\), \\( d = {1} \\):",
            "Compute the first four terms: \\( a = {0} \\), \\( d = {1} \\):"
        ],
        'calc': lambda item: (
            f"{item[2]}",
            ["1, 2, 3, 4", "10, 15, 20, 25", "0, 5, 10, 15"],
            f"**Step 1: State the general form of an AP.**\n\\[ a_1 = a, \\quad a_2 = a + d, \\quad a_3 = a + 2d, \\quad a_4 = a + 3d \\]\n\n**Step 2: Substitute \\( a = {item[0]} \\) and \\( d = {item[1]} \\).**\nThe first four terms are {item[2]}.\n\n**Step 3: State the answer.**\n{item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: General formula for the nth term: an = a + (n - 1)d
    arch1 = {
        'data': [
            (2, 3, 10, 29, "2 + 9(3) = 29"),
            (5, 4, 15, 61, "5 + 14(4) = 61"),
            (10, -2, 20, -28, "10 + 19(-2) = -28"),
            (7, 5, 12, 62, "7 + 11(5) = 62"),
            (3, 7, 11, 73, "3 + 10(7) = 73"),
            (100, -5, 16, 25, "100 + 15(-5) = 25"),
            (-4, 3, 21, 56, "-4 + 20(3) = 56"),
            (12, 6, 8, 54, "12 + 7(6) = 54"),
            (1, 8, 14, 105, "1 + 13(8) = 105"),
            (50, -3, 15, 8, "50 + 14(-3) = 8")
        ],
        'tmpls': [
            "In an AP with first term \\( a = {0} \\) and common difference \\( d = {1} \\), find the {2}th term (\\( a_{{{2}}} \\)):",
            "Find the {2}th term of an AP whose first term is {0} and common difference is {1}:",
            "Calculate \\( a_{{{2}}} \\) using \\( a_n = a + (n - 1)d \\) when \\( a = {0} \\) and \\( d = {1} \\):",
            "What is the {2}th term of an AP with starting term {0} and step size {1}?",
            "Evaluate \\( a_{{{2}}} \\) given \\( a = {0} \\), \\( d = {1} \\):",
            "Determine the {2}th term of the AP defined by \\( a = {0} \\) and \\( d = {1} \\):",
            "Compute \\( a_{{{2}}} \\) for \\( a = {0} \\), \\( d = {1} \\):",
            "Find \\( a_{{{2}}} \\): \\( a = {0} \\), \\( d = {1} \\):",
            "What is the value of \\( a_{{{2}}} \\) in the AP with \\( a = {0} \\) and \\( d = {1} \\)?",
            "Calculate \\( a_{{{2}}} \\) for: \\( a = {0} \\), \\( d = {1} \\):"
        ],
        'calc': lambda item: (
            f"\\( a_{{{item[2]}}} = {item[3]} \\)",
            [f"\\( a_{{{item[2]}}} = {item[3] + 4} \\)", f"\\( a_{{{item[2]}}} = {item[3] - 4} \\)", f"\\( a_{{{item[2]}}} = {item[3] * 2} \\)"],
            f"**Step 1: State the general nth term formula.**\n\\[ a_n = a + (n - 1)d \\]\n\n**Step 2: Substitute \\( a = {item[0]} \\), \\( d = {item[1]} \\), and \\( n = {item[2]} \\).**\n\\[ a_{{{item[2]}}} = {item[0]} + ({item[2]} - 1)({item[1]}) = {item[4]} \\]\n\n**Step 3: State the final term.**\n\\( a_{{{item[2]}}} = {item[3]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Finding a given an, n, and d
    arch2 = {
        'data': [
            (29, 10, 3, 2),      # a = 29 - 9*3 = 2
            (61, 15, 4, 5),      # a = 61 - 14*4 = 5
            (-28, 20, -2, 10),   # a = -28 - 19*(-2) = 10
            (62, 12, 5, 7),      # a = 62 - 11*5 = 7
            (73, 11, 7, 3),      # a = 73 - 10*7 = 3
            (25, 16, -5, 100),   # a = 25 - 15*(-5) = 100
            (56, 21, 3, -4),     # a = 56 - 20*3 = -4
            (54, 8, 6, 12),      # a = 54 - 7*6 = 12
            (105, 14, 8, 1),     # a = 105 - 13*8 = 1
            (8, 15, -3, 50)      # a = 8 - 14*(-3) = 50
        ],
        'tmpls': [
            "In an AP, the {1}th term is {0} and the common difference is {2}. Find the first term \\( a \\):",
            "Find the first term \\( a \\) of an AP whose {1}th term is {0} and \\( d = {2} \\):",
            "If \\( a_{{{1}}} = {0} \\) and \\( d = {2} \\), calculate \\( a \\):",
            "Determine the starting value \\( a \\) in an AP where \\( a_{{{1}}} = {0} \\) and common difference is {2}:",
            "Calculate \\( a \\) using \\( a = a_n - (n - 1)d \\) for \\( a_{{{1}}} = {0} \\), \\( d = {2} \\):",
            "What is the first term \\( a \\) if \\( a_{{{1}}} = {0} \\) and \\( d = {2} \\)?",
            "Evaluate \\( a \\) given \\( a_{{{1}}} = {0} \\) and \\( d = {2} \\):",
            "Compute the first term of an AP having \\( a_{{{1}}} = {0} \\) and \\( d = {2} \\):",
            "Find \\( a \\): \\( a_{{{1}}} = {0} \\), \\( d = {2} \\):",
            "What is the value of \\( a \\) when \\( a_{{{1}}} = {0} \\), \\( d = {2} \\)?"
        ],
        'calc': lambda item: (
            f"\\( a = {item[3]} \\)",
            [f"\\( a = {item[3] + 5} \\)", f"\\( a = {item[3] - 5} \\)", f"\\( a = {item[0]} \\)"],
            f"**Step 1: Set up the formula.**\n\\[ a_n = a + (n - 1)d \\implies a = a_n - (n - 1)d \\]\n\n**Step 2: Substitute \\( a_{{{item[1]}}} = {item[0]} \\), \\( n = {item[1]} \\), \\( d = {item[2]} \\).**\n\\[ a = {item[0]} - ({item[1]} - 1)({item[2]}) = {item[3]} \\]\n\n**Step 3: State the first term.**\n\\( a = {item[3]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Missing terms in boxes (NCERT canonical problem: e.g. 2, [ ], 26)
    arch3 = {
        'data': [
            ("2, [ ], 26", 14, "b = (2 + 26) / 2 = 14"),
            ("[ ], 13, [ ], 3", "18 and 8", "a + d = 13, a + 3d = 3 => 2d = -10 => d = -5 => a = 18, a3 = 8"),
            ("5, [ ], [ ], 9.5", "6.5 and 8", "a = 5, a4 = 9.5 => 3d = 4.5 => d = 1.5"),
            ("-4, [ ], [ ], [ ], [ ], 6", "-2, 0, 2, 4", "a = -4, a6 = 6 => 5d = 10 => d = 2"),
            ("[ ], 38, [ ], [ ], [ ], -22", "53, 23, 8, -7", "a + d = 38, a + 5d = -22 => 4d = -60 => d = -15 => a = 53"),
            ("3, [ ], 19", 11, "b = (3 + 19) / 2 = 11"),
            ("12, [ ], 28", 20, "b = (12 + 28) / 2 = 20"),
            ("7, [ ], 21", 14, "b = (7 + 21) / 2 = 14"),
            ("10, [ ], 30", 20, "b = (10 + 30) / 2 = 20"),
            ("15, [ ], 35", 25, "b = (15 + 35) / 2 = 25")
        ],
        'tmpls': [
            "In the AP sequence with missing terms: {0}, find the missing value(s):",
            "Fill in the missing box(es) in the AP: {0}:",
            "Find the missing term(s) in the arithmetic progression: {0}:",
            "What number(s) complete the AP: {0}?",
            "Solve the NCERT missing term box puzzle: {0}:",
            "Determine the missing entries in: {0}:",
            "Calculate the unknown term(s) in: {0}:",
            "Evaluate the missing values in the AP: {0}:",
            "Find the value(s) in the box(es) for: {0}:",
            "Complete the AP sequence: {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            ["10", "15", "12"] if isinstance(item[1], int) else ["15 and 5", "10 and 20", "0"],
            f"**Step 1: Identify the positions of known terms.**\nUse the arithmetic mean \\( b = \\frac{{a + c}}{{2}} \\) or solve the linear system for \\( a \\) and \\( d \\).\n\n**Step 2: Calculate \\( d \\) and the missing terms.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe missing term(s) is/are {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Determining whether a given number is a term of the AP
    arch4 = {
        'data': [
            ("Check whether 301 is a term of the list of numbers: 5, 11, 17, 23, ...", "No, because n = 151/3 is not a natural number", ["Yes, it is the 50th term", "Yes, it is the 51st term", "Cannot be determined"]),
            ("Check whether -150 is a term of the AP: 11, 8, 5, 2, ...", "No, because n = 164/3 is not a positive integer", ["Yes, it is the 55th term", "Yes, it is the 54th term", "Cannot be determined"]),
            ("Is 205 a term of the AP: 7, 13, 19, ...?", "Yes, it is the 34th term (n = 34)", ["No, it is not", "Yes, it is the 35th term", "Yes, it is the 30th term"]),
            ("Is 0 a term of the AP: 31, 28, 25, ...?", "No, because 31 - 3(n - 1) = 0 => 3n = 34 => n is not an integer", ["Yes, it is the 10th term", "Yes, it is the 11th term", "Cannot be determined"]),
            ("Is 184 a term of the AP: 3, 7, 11, ...?", "No, because 4n - 1 = 184 => 4n = 185 (not divisible by 4)", ["Yes, it is the 46th term", "Yes, it is the 45th term", "Cannot be determined"]),
            ("Is 78 a term of the AP: 3, 8, 13, 18, ...?", "Yes, it is the 16th term (5n - 2 = 78 => 5n = 80 => n = 16)", ["No, it is not", "Yes, it is the 15th term", "Yes, it is the 17th term"]),
            ("Is 148 a term of the AP: 4, 10, 16, 22, ...?", "Yes, it is the 25th term (6n - 2 = 148 => 6n = 150 => n = 25)", ["No, it is not", "Yes, it is the 24th term", "Cannot be determined"]),
            ("Is 100 a term of the AP: 2, 5, 8, 11, ...?", "No, because 3n - 1 = 100 => 3n = 101 (not divisible by 3)", ["Yes, it is the 33rd term", "Yes, it is the 34th term", "Cannot be determined"]),
            ("Is -100 a term of the AP: 20, 15, 10, ...?", "Yes, it is the 25th term (25 - 5n = -100 => 5n = 125 => n = 25)", ["No, it is not", "Yes, it is the 24th term", "Cannot be determined"]),
            ("Is 150 a term of the AP: 6, 12, 18, 24, ...?", "Yes, it is the 25th term (6n = 150 => n = 25)", ["No, it is not", "Yes, it is the 26th term", "Cannot be determined"])
        ],
        'tmpls': [
            "{0}",
            "NCERT textbook verification problem: {0}",
            "Determine if the specified value belongs to the AP: {0}",
            "Test whether the given integer is a member of the progression: {0}",
            "Solve the membership check: {0}",
            "Evaluate whether the number is in the sequence: {0}",
            "Check membership of the value in the AP: {0}",
            "Is the number part of the progression? {0}",
            "Determine: {0}",
            "Investigate: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Set \\( a_n = \\text{{given value}} \\).**\nUse \\( a_n = a + (n - 1)d \\) and solve for \\( n \\).\n\n**Step 2: Check if \\( n \\) is a positive integer.**\nA number is a term of the AP if and only if \\( n \\in \\mathbb{{N}} = \\{{1, 2, 3, \\dots\\}} \\).\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical principles of the general form
    arch5 = {
        'data': [
            ("The general form of an Arithmetic Progression with first term a and common difference d is:", "a, a + d, a + 2d, a + 3d, ...", ["a, ad, ad², ad³, ...", "a, a - d, a - 2d, ...", "a², a² + d, a² + 2d, ..."]),
            ("The formula for the nth term an of an Arithmetic Progression is:", "an = a + (n - 1)d", ["an = a + nd", "an = a - (n - 1)d", "an = a + (n + 1)d"]),
            ("Why is the coefficient of d in the nth term formula (n - 1) rather than n?", "Because the first term a has zero common differences added to it (a = a + 0·d)", ["Because 1 is subtracted by convention", "Because n is a variable", "By mathematical mistake"]),
            ("If a sequence has nth term an = 3 + 4n, is it an AP?", "Yes, because an is linear in n with common difference d = 4", ["No, it has a constant term", "Only if n is even", "Cannot be determined"]),
            ("In an AP, the term an is also referred to as the:", "last term (denoted by l in a finite AP)", ["first term", "common difference", "sum"]),
            ("If an AP has m terms, then its last term l is equal to:", "a + (m - 1)d", ["a + md", "a + (m + 1)d", "md"]),
            ("What is the nth term from the end of a finite AP of m terms?", "l - (n - 1)d", ["l + (n - 1)d", "l - nd", "a + (m - n)d"]),
            ("The nth term from the end of an AP is also the ___ term from the beginning:", "(m - n + 1)th term", ["(m - n)th term", "(m + n)th term", "(n - m)th term"]),
            ("In any finite AP, the sum of terms equidistant from the beginning and end is:", "always constant and equal to a + l", ["always zero", "equal to 2d", "increases linearly"]),
            ("If an = 2n² + 1, does this sequence form an AP?", "No, because an is quadratic (second-degree) in n, not linear", ["Yes, d = 2", "Yes, d = 4", "Only for n ≤ 5"])
        ],
        'tmpls': [
            "{0}",
            "Properties of the general form of an AP: {0}",
            "Theoretical characterization of nth term formulas: {0}",
            "Select the accurate definition: {0}",
            "NCERT theoretical foundation: {0}",
            "Which option correctly states: {0}",
            "General form and terminal properties: {0}",
            "Identify the valid principle: {0}",
            "Choose the true property: {0}",
            "Complete the sentence: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the general form of an AP.**\n\\[ a, a + d, a + 2d, a + 3d, \\dots, a + (n - 1)d \\]\n\n**Step 2: Examine the algebraic structure.**\nThe \\( n \\)th term is always linear in \\( n \\), with common difference equal to the coefficient of \\( n \\).\n\n**Step 3: Conclude.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: Basic MCQs & True/False statements
    arch6 = {
        'data': [
            ("True or False: The general form of an AP is a, a + d, a + 2d, ...", "True", ["False", "It is a, ar, ar²", "Cannot be determined"]),
            ("True or False: In an AP, an = a + (n - 1)d.", "True", ["False", "an = a + nd", "Cannot be determined"]),
            ("True or False: The 10th term of an AP is a + 9d.", "True", ["False", "It is a + 10d", "Cannot be determined"]),
            ("True or False: The 100th term of an AP is a + 99d.", "True", ["False", "It is a + 100d", "Cannot be determined"]),
            ("What is the 5th term of an AP in terms of a and d?", "a + 4d", ["a + 5d", "a + 3d", "5a + d"]),
            ("What is the 3rd term of an AP in terms of a and d?", "a + 2d", ["a + 3d", "a + d", "3a + d"]),
            ("What is the 2nd term of an AP in terms of a and d?", "a + d", ["a + 2d", "2a + d", "ad"]),
            ("What is the 1st term of an AP in terms of a and d?", "a (or a + 0d)", ["a + d", "0", "d"]),
            ("If a = 1 and d = 2, what is the 3rd term?", "5 (1 + 2(2) = 5)", ["3", "7", "4"]),
            ("If a = 3 and d = 4, what is the 2nd term?", "7 (3 + 4 = 7)", ["4", "11", "12"])
        ],
        'tmpls': [
            "{0}",
            "Direct evaluation: {0}",
            "Basic general form check: {0}",
            "Choose the correct option: {0}",
            "Simple property: {0}",
            "True or False: {0}",
            "Quick question: {0}",
            "Determine the accurate value: {0}",
            "Evaluate: {0}",
            "Foundational question: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Apply the formula \\( a_n = a + (n - 1)d \\).**\nSubstitute the index \\( n \\).\n\n**Step 2: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations of a + (n - 1)d
    arch7 = {
        'data': [
            (5, 2, 3, 9),      # a=5, n=3, d=2 => 5 + 2*2 = 9
            (10, 3, 4, 19),    # a=10, n=4, d=3 => 10 + 3*3 = 19
            (1, 5, 5, 21),     # a=1, n=5, d=5 => 1 + 4*5 = 21
            (7, 2, 6, 17),     # a=7, n=6, d=2 => 7 + 5*2 = 17
            (20, -2, 5, 12),   # a=20, n=5, d=-2 => 20 + 4*(-2) = 12
            (15, 4, 3, 23),    # a=15, n=3, d=4 => 15 + 2*4 = 23
            (0, 7, 5, 28),     # a=0, n=5, d=7 => 0 + 4*7 = 28
            (12, 10, 3, 32),   # a=12, n=3, d=10 => 12 + 2*10 = 32
            (50, -5, 4, 35),   # a=50, n=4, d=-5 => 50 + 3*(-5) = 35
            (8, 3, 5, 20)      # a=8, n=5, d=3 => 8 + 4*3 = 20
        ],
        'tmpls': [
            "Quick check: Calculate \\( a + ({2} - 1)d \\) for \\( a = {0} \\), \\( d = {1} \\):",
            "Find the {2}th term \\( a_{{{2}}} \\) for \\( a = {0} \\), \\( d = {1} \\):",
            "What is \\( {0} + ({2} - 1)({1}) \\)?",
            "Calculate \\( a_{{{2}}} \\) when \\( a = {0} \\) and \\( d = {1} \\):",
            "Compute: \\( a_{{{2}}} = {0} + {2 - 1}({1}) = \\)",
            "Determine the term \\( a_{{{2}}} \\) for \\( a = {0} \\), \\( d = {1} \\):",
            "Evaluate \\( a_{{{2}}} \\) for starting term {0} and step {1}:",
            "Direct evaluation: \\( a_{{{2}}} \\) for \\( a = {0} \\), \\( d = {1} \\) is:",
            "What is the {2}th term with \\( a = {0} \\) and \\( d = {1} \\)?",
            "Find \\( a_{{{2}}} \\): \\( a = {0} \\), \\( d = {1} \\):"
        ],
        'calc': lambda item: (
            f"\\( a_{{{item[2]}}} = {item[3]} \\)",
            [f"\\( a_{{{item[2]}}} = {item[3] + 3} \\)", f"\\( a_{{{item[2]}}} = {item[3] - 3} \\)", f"\\( a_{{{item[2]}}} = {item[0]} \\)"],
            f"**Step 1: Multiply \\( (n - 1) \\) by \\( d \\).**\n\\[ ({item[2]} - 1) \\times {item[1]} = {item[2] - 1} \\times {item[1]} = {(item[2] - 1) * item[1]} \\]\n\n**Step 2: Add \\( a \\).**\n\\[ a_{{{item[2]}}} = {item[0]} + {(item[2] - 1) * item[1]} = {item[3]} \\]\n\n**Step 3: State the answer.**\n\\( a_{{{item[2]}}} = {item[3]} \\)."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 8.2.3: Finding terms in an AP sequence
# ==============================================================================
def gen_8_2_3():
    tc = "CBSE-9-MGM-8-8.2.3"
    tname = "Finding terms in an AP sequence"

    # Arch 0: Finding how many terms are in a finite AP (given a, d, and last term l)
    arch0 = {
        'data': [
            (7, 13, 205, 6, 34),     # NCERT: 7, 13, 19, ..., 205 => 6n + 1 = 205 => 6n = 204 => n = 34
            (18, 15.5, -47, -2.5, 27), # NCERT: 18, 15 1/2, ..., -47 => n = 27
            (3, 7, 111, 4, 28),      # 3, 7, 11, ..., 111 => 4n - 1 = 111 => n = 28
            (5, 9, 101, 4, 25),      # 5, 9, 13, ..., 101 => 4n + 1 = 101 => n = 25
            (2, 8, 122, 6, 21),      # 2, 8, 14, ..., 122 => 6n - 4 = 122 => n = 21
            (10, 17, 143, 7, 20),    # 10, 17, 24, ..., 143 => 7n + 3 = 143 => n = 20
            (100, 92, -60, -8, 21),  # 100, 92, ..., -60 => 108 - 8n = -60 => 8n = 168 => n = 21
            (4, 9, 149, 5, 30),      # 4, 9, ..., 149 => 5n - 1 = 149 => n = 30
            (12, 19, 215, 7, 30),    # 12, 19, ..., 215 => 7n + 5 = 215 => n = 30
            (15, 23, 255, 8, 31)     # 15, 23, ..., 255 => 8n + 7 = 255 => n = 31
        ],
        'tmpls': [
            "Find the number of terms in the AP: {0}, {1}, ..., {2}:",
            "How many terms are there in the finite Arithmetic Progression: {0}, {1}, ..., {2}?",
            "In the AP {0}, {1}, ..., {2}, what is the total number of terms n?",
            "Calculate n for the finite sequence: {0}, {1}, ..., {2}:",
            "Determine the count of terms in the sequence: {0}, {1}, ..., {2}:",
            "What is the total number of terms in the progression: {0}, {1}, ..., {2}?",
            "Find the number of terms n when the last term is {2} in the AP: {0}, {1}, ...:",
            "Evaluate the number of terms in the sequence {0}, {1}, ..., {2}:",
            "Compute n for: {0}, {1}, ..., {2}:",
            "How many numbers are in the AP: {0}, {1}, ..., {2}?"
        ],
        'calc': lambda item: (
            f"\\( n = {item[4]} \\) terms",
            [f"\\( n = {item[4] + 2} \\) terms", f"\\( n = {item[4] - 2} \\) terms", f"\\( n = {item[4] + 5} \\) terms"],
            f"**Step 1: Identify \\( a \\), \\( d \\), and last term \\( l \\).**\n\\( a = {item[0]} \\), \\( d = {item[1]} - {item[0]} = {item[3]} \\), and \\( l = {item[2]} \\).\n\n**Step 2: Set \\( a_n = l \\) and solve for \\( n \\).**\n\\[ a + (n - 1)d = l \\implies {item[0]} + (n - 1)({item[3]}) = {item[2]} \\]\n\\[ (n - 1)({item[3]}) = {item[2] - item[0]} \\implies n - 1 = {item[4] - 1} \\implies n = {item[4]} \\]\n\n**Step 3: State the number of terms.**\nThe AP contains \\( {item[4]} \\) terms."
        ),
        'diff': 'easy'
    }

    # Arch 1: How many two-digit / three-digit numbers are divisible by a given number (NCERT canonical)
    arch1 = {
        'data': [
            ("How many two-digit numbers are divisible by 3?", 12, 99, 3, 30),      # 12, 15, ..., 99 => 3n + 9 = 99 => 3n = 90 => n = 30
            ("How many three-digit numbers are divisible by 7?", 105, 994, 7, 128),  # 105, 112, ..., 994 => 7n + 98 = 994 => n = 128
            ("How many multiples of 4 lie between 10 and 250?", 12, 248, 4, 60),    # 12, 16, ..., 248 => 4n + 8 = 248 => n = 60
            ("How many two-digit numbers are divisible by 7?", 14, 98, 7, 13),       # 14, 21, ..., 98 => n = 13
            ("How many two-digit numbers are divisible by 6?", 12, 96, 6, 15),       # 12, 18, ..., 96 => n = 15
            ("How many three-digit numbers are divisible by 5?", 100, 995, 5, 180),  # 100 to 995 => n = 180
            ("How many three-digit numbers are divisible by 9?", 108, 999, 9, 100),  # 108 to 999 => n = 100
            ("How many two-digit numbers are divisible by 5?", 10, 95, 5, 18),       # 10 to 95 => n = 18
            ("How many two-digit numbers are divisible by 4?", 12, 96, 4, 22),       # 12 to 96 => n = 22
            ("How many multiples of 3 lie between 10 and 100?", 12, 99, 3, 30)      # 12 to 99 => n = 30
        ],
        'tmpls': [
            "{0}",
            "Solve the NCERT divisibility AP problem: {0}",
            "Calculate using Arithmetic Progression: {0}",
            "What is the total count: {0}?",
            "Find the answer using an AP sequence: {0}",
            "Determine the number of integers: {0}",
            "Evaluate the count using AP methods: {0}",
            "Find the number of multiples: {0}",
            "Compute: {0}",
            "Solve: {0}"
        ],
        'calc': lambda item: (
            f"{item[4]}",
            [f"{item[4] + 2}", f"{item[4] - 2}", f"{item[4] + 5}"],
            f"**Step 1: Identify the first and last numbers satisfying the condition.**\nThe first term is \\( a = {item[1]} \\) and the last term is \\( l = {item[2]} \\), with step \\( d = {item[3]} \\).\n\n**Step 2: Solve \\( a + (n - 1)d = l \\) for \\( n \\).**\n\\[ {item[1]} + (n - 1)({item[3]}) = {item[2]} \\implies n = {item[4]} \\]\n\n**Step 3: State the final count.**\nThere are {item[4]} such numbers."
        ),
        'diff': 'medium'
    }

    # Arch 2: Finding a specific term from the end of an AP (NCERT canonical problem)
    # AP: 10, 7, 4, ..., -62. Find 11th term from the last term.
    # l = -62, d = -3 => nth from end = l - (n - 1)d = -62 - (11 - 1)(-3) = -62 + 30 = -32
    arch2 = {
        'data': [
            ("10, 7, 4, ..., -62", 11, -62, -3, -32),      # NCERT: 11th from end = -32
            ("3, 8, 13, ..., 253", 20, 253, 5, 158),       # NCERT: 20th from end = 253 - 19*5 = 158
            ("4, 9, 14, ..., 254", 10, 254, 5, 209),       # 254 - 9*5 = 209
            ("2, 6, 10, ..., 86", 8, 86, 4, 58),           # 86 - 7*4 = 58
            ("12, 17, 22, ..., 157", 12, 157, 5, 102),     # 157 - 11*5 = 102
            ("7, 10, 13, ..., 184", 15, 184, 3, 142),      # 184 - 14*3 = 142
            ("100, 95, 90, ..., 10", 6, 10, -5, 35),       # 10 - 5*(-5) = 35
            ("1, 4, 7, ..., 118", 10, 118, 3, 91),         # 118 - 9*3 = 91
            ("5, 11, 17, ..., 179", 10, 179, 6, 125),      # 179 - 9*6 = 125
            ("20, 23, 26, ..., 140", 11, 140, 3, 110)      # 140 - 10*3 = 110
        ],
        'tmpls': [
            "Find the {1}th term from the end of the AP: {0}:",
            "What is the {1}th term from the last term in the AP: {0}?",
            "In the AP {0}, calculate the {1}th term counted from the end:",
            "Solve the NCERT problem: Find the {1}th term from the end of {0}:",
            "Determine the {1}th term from the end of the progression {0}:",
            "Evaluate the {1}th term from the last term of {0}:",
            "Compute the term located {1} positions from the end in: {0}:",
            "Calculate the {1}th term from the end for: {0}:",
            "What is the {1}th term from the right end of: {0}?",
            "Find the {1}th term from the end of: {0}:"
        ],
        'calc': lambda item: (
            f"\\( {item[4]} \\)",
            [f"\\( {item[4] + 10} \\)", f"\\( {item[4] - 10} \\)", f"\\( {item[2]} \\)"],
            f"**Step 1: Identify the last term \\( l \\) and common difference \\( d \\).**\nLast term \\( l = {item[2]} \\), common difference \\( d = {item[3]} \\).\n\n**Step 2: Apply the formula for the nth term from the end.**\n\\[ \\text{{Term from end}} = l - (n - 1)d \\]\n\\[ = {item[2]} - ({item[1]} - 1)({item[3]}) = {item[4]} \\]\n\n**Step 3: State the final term.**\nThe {item[1]}th term from the end is {item[4]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Word problems on AP: Salary increment, ladder rungs, savings (NCERT canonical)
    # Subba Rao started work in 1995 at ₹5000 and received annual increment of ₹200. In which year did his income reach ₹7000?
    # a = 5000, d = 200, an = 7000 => 200(n - 1) = 2000 => n - 1 = 10 => n = 11 => 1995 + 10 = 2005
    arch3 = {
        'data': [
            ("Subba Rao started work in 1995 at an annual salary of ₹5000 and received an increment of ₹200 each year. In which year did his income reach ₹7000?", "2005 (in the 11th year)", ["2004", "2006", "2010"]),
            ("Ramkali saved ₹5 in the first week of a year and then increased her weekly savings by ₹1.75. If in the nth week, her weekly savings become ₹20.75, find n:", "10 (n = 10 weeks)", ["9", "11", "12"]),
            ("A ladder has rungs 25 cm apart. The rungs decrease uniformly in length from 45 cm at the bottom to 25 cm at the top. If the top and bottom rungs are 2.5 m apart, how many rungs are there?", "11 rungs (250/25 + 1 = 11)", ["10 rungs", "12 rungs", "9 rungs"]),
            ("In a flower bed, there are 23 rose plants in the first row, 21 in the second, 19 in the third, and so on. There are 5 rose plants in the last row. How many rows are there in the flower bed?", "10 rows (23 - 2(n - 1) = 5 => 2(n - 1) = 18 => n = 10)", ["9 rows", "11 rows", "12 rows"]),
            ("A manufacturer of TV sets produced 600 sets in the third year and 700 sets in the seventh year. Assuming production increases uniformly by a fixed number every year, find the production in the 1st year:", "550 sets (a = 550, d = 25)", ["500 sets", "525 sets", "575 sets"]),
            ("In the TV manufacturer problem (a = 550, d = 25), what was the production in the 10th year?", "775 sets (550 + 9 × 25 = 775)", ["750 sets", "800 sets", "825 sets"]),
            ("A spiral is made up of successive semicircles with centres alternately at A and B, starting with centre at A, of radii 0.5 cm, 1.0 cm, 1.5 cm, 2.0 cm, ... What is the radius of the 13th semicircle?", "6.5 cm (0.5 + 12 × 0.5 = 6.5)", ["6.0 cm", "7.0 cm", "13.0 cm"]),
            ("200 logs are stacked in the following manner: 20 logs in the bottom row, 19 in the next, 18 in the next, and so on. How many logs are in the 16th row?", "5 logs (20 - 15 × 1 = 5)", ["4 logs", "6 logs", "10 logs"]),
            ("A person repays a loan of ₹3250 by paying ₹20 in the first month and then increases the payment by ₹15 every month. What will be the payment in the 10th month?", "₹155 (20 + 9 × 15 = 155)", ["₹150", "₹160", "₹170"]),
            ("A contract on construction job specifies a penalty for delay of completion beyond a certain date: ₹200 for 1st day, ₹250 for 2nd day, ₹300 for 3rd day, etc. What is the penalty for the 30th day alone?", "₹1650 (200 + 29 × 50 = 1650)", ["₹1500", "₹1600", "₹1700"])
        ],
        'tmpls': [
            "{0}",
            "Solve the real-life AP application: {0}",
            "NCERT practical word problem: {0}",
            "Apply Arithmetic Progression to solve: {0}",
            "Calculate the required value using AP: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Evaluate the scenario using AP formulas: {0}",
            "Determine the answer: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify the AP parameters from the problem statement.**\nIdentify the first term \\( a \\) and the uniform increment \\( d \\).\n\n**Step 2: Apply the general term formula \\( a_n = a + (n - 1)d \\).**\nSubstitute the known values and solve for the unknown parameter.\n\n**Step 3: State the answer.**\nThe result is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 4: Advanced relations between terms (e.g. an = am => m-n relations)
    arch4 = {
        'data': [
            ("If 7 times the 7th term of an AP is equal to 11 times its 11th term, show that its 18th term is:", "0 (7(a + 6d) = 11(a + 10d) => 4a + 68d = 0 => a + 17d = 0)", ["1", "-1", "18"]),
            ("If m times the mth term of an AP is equal to n times its nth term (m ≠ n), then its (m + n)th term is always:", "0", ["1", "m + n", "mn"]),
            ("If the pth term of an AP is q and the qth term is p, what is the (p + q)th term?", "0", ["p + q", "pq", "1"]),
            ("If the pth term of an AP is q and the qth term is p, what is the nth term?", "p + q - n", ["p + q + n", "p - q + n", "0"]),
            ("If the mth term of an AP is 1/n and the nth term is 1/m, what is the (mn)th term?", "1", ["0", "1 / (mn)", "mn"]),
            ("If the mth term of an AP is 1/n and the nth term is 1/m, what is the first term a?", "1 / (mn)", ["1 / m", "1 / n", "0"]),
            ("If the mth term of an AP is 1/n and the nth term is 1/m, what is the common difference d?", "1 / (mn)", ["1", "0", "mn"]),
            ("The 4th term of an AP is 0. Prove that the 25th term is how many times the 11th term?", "3 times (a₂₅ = 3 a₁₁)", ["2 times", "4 times", "5 times"]),
            ("The 6th term of an AP is zero. What is the ratio of its 31st term to its 11th term?", "5 : 1", ["3 : 1", "4 : 1", "6 : 1"]),
            ("The sum of 4th and 8th terms of an AP is 24, and sum of 6th and 10th terms is 44. Find the first three terms:", "-13, -8, -3 (a = -13, d = 5)", ["-10, -5, 0", "-15, -10, -5", "2, 7, 12"])
        ],
        'tmpls': [
            "{0}",
            "Classical algebraic AP identity: {0}",
            "Solve the algebraic progression theorem: {0}",
            "Deduce the term property: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Evaluate the algebraic relation: {0}",
            "Calculate: {0}",
            "Find the answer: {0}",
            "Determine: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Express the given terms algebraically.**\nUse \\( a_k = a + (k - 1)d \\) for each term.\n\n**Step 2: Equate and simplify the expression.**\nSubtract equations or combine terms to eliminate \\( a \\).\n\n**Step 3: State the final conclusion.**\nThe result is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical principles and conditions for finding terms
    arch5 = {
        'data': [
            ("To find any term of an Arithmetic Progression, how many independent pieces of information are fundamentally required?", "two pieces of information (such as a and d, or any two distinct terms)", ["one piece", "three pieces", "ten pieces"]),
            ("If two terms of an AP are known (say aₚ and a_q), can all other terms of the AP be determined?", "Yes, because two terms yield a system of two linear equations in two unknowns (a and d)", ["No, a must be given separately", "Only if p = 1", "Only for integer terms"]),
            ("The difference aₙ - aₖ in an AP is always equal to:", "(n - k)d", ["(n + k)d", "nd - kd", "d"]),
            ("If aₙ is known and common difference d is known, the preceding term aₙ₋₁ is:", "aₙ - d", ["aₙ + d", "aₙ / d", "d - aₙ"]),
            ("If aₙ is known and common difference d is known, the succeeding term aₙ₊₁ is:", "aₙ + d", ["aₙ - d", "aₙ × d", "d - aₙ"]),
            ("In an AP, the average (arithmetic mean) of the first term a and the nth term aₙ is:", "(a + aₙ) / 2", ["a + aₙ", "a × aₙ", "a_n / 2"]),
            ("The middle term of an AP with an odd number of terms n is:", "the ((n + 1) / 2)th term", ["the (n / 2)th term", "the ((n - 1) / 2)th term", "there is no middle term"]),
            ("An AP with an even number of terms n has how many middle terms?", "two middle terms: (n / 2)th and (n / 2 + 1)th", ["one middle term", "no middle terms", "three middle terms"]),
            ("If an AP has 15 terms, which term is the middle term?", "8th term ((15 + 1) / 2 = 8)", ["7th term", "9th term", "10th term"]),
            ("If an AP has 20 terms, which terms are the two middle terms?", "10th and 11th terms", ["9th and 10th", "11th and 12th", "10th only"])
        ],
        'tmpls': [
            "{0}",
            "Theoretical properties of AP terms: {0}",
            "Structure and determination of AP terms: {0}",
            "Select the accurate statement: {0}",
            "NCERT theoretical foundation: {0}",
            "Which option correctly states: {0}",
            "Middle terms and algebraic relationships: {0}",
            "Identify the valid principle: {0}",
            "Choose the true property: {0}",
            "Complete the sentence: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: State the relevant property of AP terms.**\nReview the relationship between positions, indices, and the common difference.\n\n**Step 2: Analyze middle terms or indexing.**\nOdd \\( n \\) yields a unique middle term at \\( \\frac{{n+1}}{{2}} \\), while even \\( n \\) yields two middle terms.\n\n**Step 3: Conclude.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: Basic MCQs & True/False statements
    arch6 = {
        'data': [
            ("True or False: The number of terms in an AP must be a positive integer (natural number).", "True", ["False", "It can be negative", "Cannot be determined"]),
            ("True or False: In the AP 2, 4, 6, ..., the 10th term is 20.", "True", ["False", "It is 22", "Cannot be determined"]),
            ("True or False: In the AP 5, 10, 15, ..., the 20th term is 100.", "True", ["False", "It is 105", "Cannot be determined"]),
            ("True or False: An AP with 11 terms has its middle term at position 6.", "True", ["False", "At position 5", "Cannot be determined"]),
            ("What is the 10th term of the AP: 2, 7, 12, ...?", "47 (2 + 9(5) = 47)", ["50", "45", "52"]),
            ("What is the 7th term of the AP: 10, 7, 4, ...?", "-8 (10 + 6(-3) = -8)", ["-11", "-5", "8"]),
            ("What is the 11th term of the AP: -3, -1/2, 2, ...?", "22 (-3 + 10(2.5) = 22)", ["20", "25", "24.5"]),
            ("What is the 30th term of the AP: 10, 7, 4, ...?", "-77 (10 + 29(-3) = -77)", ["-87", "-74", "-80"]),
            ("What is the 21st term of the AP: -5, -5/2, 0, 5/2, ...?", "45 (-5 + 20(2.5) = 45)", ["50", "40", "47.5"]),
            ("What is the 10th term of the AP: -40, -15, 10, 35, ...?", "185 (-40 + 9(25) = 185)", ["175", "190", "200"])
        ],
        'tmpls': [
            "{0}",
            "Direct evaluation: {0}",
            "Basic term calculation check: {0}",
            "Choose the correct option: {0}",
            "Simple property: {0}",
            "True or False: {0}",
            "Quick question: {0}",
            "Determine the accurate value: {0}",
            "Evaluate: {0}",
            "Foundational question: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Compute using \\( a_n = a + (n - 1)d \\).**\nSubstitute \\( a \\), \\( d \\), and \\( n \\).\n\n**Step 2: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations for small indices
    arch7 = {
        'data': [
            (2, 3, 4, 11),     # a=2, d=3 => a4 = 2 + 3(3) = 11
            (5, 2, 4, 11),     # a=5, d=2 => a4 = 5 + 3(2) = 11
            (1, 4, 4, 13),     # a=1, d=4 => a4 = 1 + 3(4) = 13
            (10, -2, 4, 4),    # a=10, d=-2 => a4 = 10 + 3(-2) = 4
            (7, 3, 4, 16),     # a=7, d=3 => a4 = 7 + 3(3) = 16
            (0, 5, 4, 15),     # a=0, d=5 => a4 = 0 + 3(5) = 15
            (20, -5, 4, 5),    # a=20, d=-5 => a4 = 20 + 3(-5) = 5
            (3, 6, 4, 21),     # a=3, d=6 => a4 = 3 + 3(6) = 21
            (8, 2, 4, 14),     # a=8, d=2 => a4 = 8 + 3(2) = 14
            (15, -3, 4, 6)     # a=15, d=-3 => a4 = 15 + 3(-3) = 6
        ],
        'tmpls': [
            "Quick check: What is the 4th term \\( a_4 \\) for \\( a = {0} \\), \\( d = {1} \\)?",
            "Calculate \\( a_4 = {0} + 3({1}) \\):",
            "What is \\( a_4 \\) when \\( a = {0} \\) and \\( d = {1} \\)?",
            "Find the 4th term: \\( a = {0} \\), \\( d = {1} \\):",
            "Compute: \\( a_4 = {0} + 3({1}) = \\)",
            "Determine \\( a_4 \\) for \\( a = {0} \\), \\( d = {1} \\):",
            "Evaluate the 4th term: \\( a = {0} \\), \\( d = {1} \\):",
            "Direct calculation of 4th term: \\( a = {0} \\), \\( d = {1} \\) is:",
            "What is \\( a_4 \\) with starting value {0} and step {1}?",
            "Find \\( a_4 \\): \\( a = {0} \\), \\( d = {1} \\):"
        ],
        'calc': lambda item: (
            f"\\( a_4 = {item[3]} \\)",
            [f"\\( a_4 = {item[3] + 2} \\)", f"\\( a_4 = {item[3] - 2} \\)", f"\\( a_4 = {item[0]} \\)"],
            f"**Step 1: Compute \\( a_4 = a + 3d \\).**\n\\[ a_4 = {item[0]} + 3({item[1]}) = {item[0]} + {3 * item[1]} = {item[3]} \\]\n\n**Step 2: State the answer.**\n\\( a_4 = {item[3]} \\)."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_8_2_1()
    print(f"gen_8_2_1: {len(q1)} questions")
    q2 = gen_8_2_2()
    print(f"gen_8_2_2: {len(q2)} questions")
    q3 = gen_8_2_3()
    print(f"gen_8_2_3: {len(q3)} questions")
