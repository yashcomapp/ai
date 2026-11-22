# scripts/build_cbse9_mgm_ch8_part1.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 8: Predicting What Comes Next?: Exploring Sequences and Progressions
Part 1:
- Subtopic 8.1.1: Identifying numerical and geometric patterns
- Subtopic 8.1.2: Writing general term rules (nth term an)
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 8
CH_NAME = "Predicting What Comes Next?: Exploring Sequences and Progressions"

# ==============================================================================
# SUBTOPIC 8.1.1: Identifying numerical and geometric patterns
# ==============================================================================
def gen_8_1_1():
    tc = "CBSE-9-MGM-8-8.1.1"
    tname = "Identifying numerical and geometric patterns"

    # Arch 0: Arithmetic patterns: finding next term
    arch0 = {
        'data': [
            ("2, 5, 8, 11, ...", 14, 3, "+3"),
            ("7, 12, 17, 22, ...", 27, 5, "+5"),
            ("10, 6, 2, -2, ...", -6, -4, "-4"),
            ("1, 6, 11, 16, ...", 21, 5, "+5"),
            ("4, 11, 18, 25, ...", 32, 7, "+7"),
            ("100, 85, 70, 55, ...", 40, -15, "-15"),
            ("3, 7, 11, 15, ...", 19, 4, "+4"),
            ("50, 43, 36, 29, ...", 22, -7, "-7"),
            ("13, 20, 27, 34, ...", 41, 7, "+7"),
            ("8, 14, 20, 26, ...", 32, 6, "+6")
        ],
        'tmpls': [
            "Find the next term in the arithmetic sequence: {0}",
            "What is the next number in the pattern: {0}?",
            "Identify the missing next term in the numerical sequence: {0}",
            "Determine the next value that follows the sequence: {0}",
            "In the progression {0}, the next term is:",
            "Calculate the next term in the linear pattern: {0}",
            "What number comes next in: {0}?",
            "Evaluate the sequence continuation for: {0}",
            "Find the 5th term of the sequence: {0}",
            "Predict what comes next in the progression: {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1] + 2}", f"{item[1] - 2}", f"{item[1] + 5}"],
            f"**Step 1: Identify the common pattern/difference.**\nObserve consecutive differences: \\( {item[3]} \\).\n\n**Step 2: Add the difference to the last given term.**\nThe next term is \\( {item[1]} \\).\n\n**Step 3: State the answer.**\nThe next term is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Multiplicative / Geometric doubling or tripling patterns
    arch1 = {
        'data': [
            ("2, 4, 8, 16, ...", 32, "× 2 (doubling)"),
            ("3, 9, 27, 81, ...", 243, "× 3 (tripling)"),
            ("5, 25, 125, 625, ...", 3125, "× 5"),
            ("1, 4, 16, 64, ...", 256, "× 4"),
            ("10, 100, 1000, 10000, ...", 100000, "× 10"),
            ("80, 40, 20, 10, ...", 5, "÷ 2 (halving)"),
            ("729, 243, 81, 27, ...", 9, "÷ 3"),
            ("1/2, 1/4, 1/8, 1/16, ...", "1/32", "× 1/2"),
            ("2, 6, 18, 54, ...", 162, "× 3"),
            ("1, 5, 25, 125, ...", 625, "× 5")
        ],
        'tmpls': [
            "What is the next term in the geometric sequence: {0}?",
            "Find the next number in the multiplicative progression: {0}",
            "Identify the next term following the ratio pattern: {0}",
            "In the exponential growth sequence {0}, what is the next value?",
            "Calculate the next number in: {0}",
            "Determine the next element of the pattern: {0}",
            "Predict what comes next in the multiplicative sequence: {0}:",
            "What number completes the geometric sequence: {0}?",
            "Evaluate the continuation of the geometric pattern: {0}",
            "Find the 5th term in the sequence: {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1] * 2}" if isinstance(item[1], int) else "1/64", f"{item[1] + 10}" if isinstance(item[1], int) else "1/16", "100"],
            f"**Step 1: Identify the multiplicative ratio.**\nEach term is obtained by multiplying the previous term by {item[2]}.\n\n**Step 2: Multiply the last term by the common ratio.**\nThe next term is {item[1]}.\n\n**Step 3: State the result.**\nThe next term is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Square and cubic number sequences (1, 4, 9, 16, 25, ...) and triangular numbers
    arch2 = {
        'data': [
            ("1, 4, 9, 16, 25, ...", 36, "n² (square numbers)"),
            ("1, 8, 27, 64, 125, ...", 216, "n³ (cube numbers)"),
            ("1, 3, 6, 10, 15, ...", 21, "n(n+1)/2 (triangular numbers)"),
            ("2, 5, 10, 17, 26, ...", 37, "n² + 1"),
            ("0, 3, 8, 15, 24, ...", 35, "n² - 1"),
            ("0, 7, 26, 63, 124, ...", 215, "n³ - 1"),
            ("2, 9, 28, 65, 126, ...", 217, "n³ + 1"),
            ("1, 2, 4, 7, 11, 16, ...", 22, "differences increase by 1 (+1, +2, +3, +4, +5, +6)"),
            ("2, 6, 12, 20, 30, ...", 42, "n(n+1) (pronic numbers)"),
            ("3, 6, 11, 18, 27, ...", 38, "n² + 2")
        ],
        'tmpls': [
            "Identify the next term in the polynomial pattern: {0}",
            "What is the next number in the sequence: {0}?",
            "Find the 6th term of the sequence: {0}",
            "Calculate the next value in the square/triangular pattern: {0}",
            "In the pattern {0}, determine the next number:",
            "Evaluate what comes next in: {0}",
            "What is the mathematical pattern rule for {0} and its next term?",
            "Predict the next term in the sequence of special numbers: {0}",
            "Find the continuation of: {0}",
            "Determine the next number: {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1] + 4}", f"{item[1] - 4}", f"{item[1] + 10}"],
            f"**Step 1: Analyze the sequence structure.**\nThe sequence follows the rule of {item[2]}.\n\n**Step 2: Evaluate for the next index \\( n \\).**\nSubstituting the next value gives {item[1]}.\n\n**Step 3: State the answer.**\nThe next term is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Visual and geometric dot patterns (matchstick patterns, polygon perimeter figures)
    arch3 = {
        'data': [
            ("Square matchstick frames: 1 square needs 4 sticks, 2 squares joined need 7, 3 squares need 10", "3n + 1", 31, "10 squares need 3(10) + 1 = 31 sticks"),
            ("Triangle matchstick frames: 1 triangle needs 3 sticks, 2 joined need 5, 3 joined need 7", "2n + 1", 21, "10 triangles need 2(10) + 1 = 21 sticks"),
            ("Hexagon matchstick chain: 1 hexagon needs 6 sticks, 2 joined need 11, 3 joined need 16", "5n + 1", 51, "10 hexagons need 5(10) + 1 = 51 sticks"),
            ("House-shaped matchstick pattern: 1 house needs 6 sticks, 2 houses need 11, 3 houses need 16", "5n + 1", 31, "6 houses need 5(6) + 1 = 31 sticks"),
            ("Dots in triangular grid: 1, 3, 6, 10, ...", "n(n+1)/2", 55, "10th triangular number is 10(11)/2 = 55"),
            ("Dots in square grid: 1, 4, 9, 16, ...", "n²", 100, "10th square number is 10² = 100"),
            ("Table seating arrangement: 1 square table seats 4 people; joining tables in a row seats 2n + 2", "2n + 2", 22, "10 joined tables seat 2(10) + 2 = 22 people"),
            ("Staircase block pattern: Step 1 has 1 block, Step 2 has 3, Step 3 has 6", "n(n+1)/2", 28, "7th step has 7(8)/2 = 28 blocks"),
            ("Border tiles around n × n square: 4(n + 1)", "4n + 4", 44, "for n = 10, border tiles = 4(10) + 4 = 44"),
            ("Corner tree planting pattern around an n-sided regular polygon", "n", 8, "an 8-sided polygon has 8 corners")
        ],
        'tmpls': [
            "{0}. What is the general algebraic rule for n figures and how many are needed for 10 figures?",
            "In the matchstick/dot geometric puzzle: '{0}', find the formula in terms of n:",
            "Analyze the geometric dot pattern: '{0}'. How many elements are required for the 10th figure?",
            "What is the algebraic expression for the pattern: '{0}'?",
            "Solve the real-world pattern problem: '{0}':",
            "Evaluate the matchstick rule for: '{0}':",
            "Determine the formula and requirement: '{0}':",
            "Calculate the count for 10 units: '{0}':",
            "Which algebraic expression models: '{0}'?",
            "Find the rule for: '{0}':"
        ],
        'calc': lambda item: (
            f"\\( {item[1]} \\) (gives {item[2]} for 10 units)",
            [f"\\( {item[1]} + 2 \\)", f"\\( 2n + 5 \\)", f"\\( 3n \\)"],
            f"**Step 1: Determine the rate of change.**\nObserve how the count increases for each additional unit.\n\n**Step 2: Formulate the linear or quadratic expression.**\nThe general rule is \\( {item[1]} \\).\n\n**Step 3: State the value.**\nFor 10 units, {item[3]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Advanced pattern identification with alternating or nested sequences
    arch4 = {
        'data': [
            ("1, -2, 3, -4, 5, ...", -6, "(-1)^(n-1) × n (alternating signs)"),
            ("2, 3, 5, 7, 11, 13, ...", 17, "prime numbers sequence"),
            ("1, 1, 2, 3, 5, 8, 13, ...", 21, "Fibonacci sequence: a_n = a_(n-1) + a_(n-2)"),
            ("1/2, 2/3, 3/4, 4/5, ...", "5/6", "n / (n + 1)"),
            ("2/3, 4/9, 8/27, 16/81, ...", "32/243", "(2/3)^n"),
            ("1, 4, 2, 8, 4, 16, ...", 8, "two alternating sequences: 1, 2, 4, 8 and 4, 8, 16"),
            ("3, 5, 9, 17, 33, ...", 65, "2^n + 1"),
            ("1, 3, 7, 15, 31, ...", 63, "2^n - 1 (Mersenne numbers)"),
            ("2, 5, 11, 23, 47, ...", 95, "2a_n + 1"),
            ("1, 2, 6, 24, 120, ...", 720, "n! (factorial sequence)")
        ],
        'tmpls': [
            "Find the next term in the advanced sequence: {0}",
            "What number comes next in: {0}?",
            "Identify the pattern and compute the next term for: {0}",
            "Solve the sequence puzzle: {0}",
            "In the mathematical progression {0}, the next element is:",
            "Calculate what follows next in: {0}",
            "Determine the next term of: {0}",
            "Evaluate the continuation of the series: {0}",
            "Predict the next value in: {0}",
            "Find the next entry in: {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1] + 4}" if isinstance(item[1], int) else "6/7", f"{item[1] - 4}" if isinstance(item[1], int) else "5/7", "100"],
            f"**Step 1: Identify the underlying recurrence or functional relation.**\nThe sequence follows: {item[2]}.\n\n**Step 2: Compute the next term.**\nThe next term is {item[1]}.\n\n**Step 3: State the final answer.**\nThe next term is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical definitions: Sequence, term, pattern, progression
    arch5 = {
        'data': [
            ("An ordered arrangement of numbers according to a definite rule is called a:", "sequence", ["set", "permutation", "matrix"]),
            ("Each individual number occurring in a sequence is called a:", "term of the sequence (denoted a₁, a₂, ..., an)", ["root", "coefficient", "exponent"]),
            ("The nth term of a sequence is also called its:", "general term (an)", ["first term", "common ratio", "sum of terms"]),
            ("A sequence whose terms follow a specific mathematical law or pattern is called a:", "progression", ["random walk", "set", "variable"]),
            ("A sequence containing a finite number of terms is called a:", "finite sequence", ["infinite sequence", "divergent sequence", "null sequence"]),
            ("A sequence with endlessly many terms is called an:", "infinite sequence", ["finite sequence", "bounded sequence", "closed sequence"]),
            ("In the notation aₙ, the subscript 'n' denotes:", "the position or index of the term (n ∈ {1, 2, 3, ...})", ["the value of the term", "the common difference", "the sum of n terms"]),
            ("Can the domain of a sequence as a function be any negative real number?", "No, the domain of a sequence is strictly the set of natural numbers N = {1, 2, 3, ...}", ["Yes, any real number", "Only irrational numbers", "Only even numbers"]),
            ("A sequence can be formally defined as a function whose domain is:", "the set of natural numbers N (or positive integers)", ["the set of all real numbers R", "the set of negative integers", "the complex plane"]),
            ("The difference between a sequence and a series is that a series is:", "the sum of the terms of a sequence (a₁ + a₂ + ... + an)", ["the product of the terms", "the reciprocal of the sequence", "a sequence with negative terms"])
        ],
        'tmpls': [
            "{0}",
            "Foundational definition in sequence theory: {0}",
            "Identify the correct mathematical term: {0}",
            "NCERT terminology check: {0}",
            "Select the accurate definition: {0}",
            "Which option correctly states: {0}",
            "Theoretical characterization of sequences: {0}",
            "Choose the valid definition: {0}",
            "Concept of sequences and progressions: {0}",
            "Complete the sentence: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: State the mathematical definition.**\nA sequence is an ordered list of numbers following a specified rule, formally defined as a function from \\( \\mathbb{{N}} \\to \\mathbb{{R}} \\).\n\n**Step 2: Understand the notation.**\nEach element \\( a_n \\) is indexed by its natural position \\( n \\).\n\n**Step 3: Conclude.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: Basic MCQs & True/False statements
    arch6 = {
        'data': [
            ("True or False: A sequence is an ordered list of numbers following a rule.", "True", ["False", "It is unordered", "Cannot be determined"]),
            ("True or False: In a sequence, the position of each term is given by a natural number n.", "True", ["False", "It can be negative", "Cannot be determined"]),
            ("True or False: The sequence 2, 4, 6, 8, ... is an infinite sequence.", "True", ["False", "It stops at 10", "Cannot be determined"]),
            ("True or False: The sequence 5, 10, 15, 20 is a finite sequence of 4 terms.", "True", ["False", "It is infinite", "Cannot be determined"]),
            ("What is the 1st term of the sequence an = 3n + 1?", "4 (3(1) + 1 = 4)", ["3", "1", "7"]),
            ("What is the 2nd term of the sequence an = 3n + 1?", "7 (3(2) + 1 = 7)", ["4", "6", "10"]),
            ("What is the 3rd term of the sequence an = 3n + 1?", "10 (3(3) + 1 = 10)", ["7", "9", "12"]),
            ("What is the 1st term of the sequence an = 2^n?", "2 (2¹ = 2)", ["1", "4", "0"]),
            ("What is the 2nd term of the sequence an = 2^n?", "4 (2² = 4)", ["2", "8", "6"]),
            ("What is the 3rd term of the sequence an = 2^n?", "8 (2³ = 8)", ["6", "12", "16"])
        ],
        'tmpls': [
            "{0}",
            "Direct question: {0}",
            "Basic sequence check: {0}",
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
            f"**Step 1: Check the definition or substitute \\( n \\).**\nEvaluate the function \\( a_n \\) for the requested index.\n\n**Step 2: Compute the result.**\nVerify against standard arithmetic.\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations for simple linear rules an = pn + q
    arch7 = {
        'data': [
            (2, 1, 1, 3),      # an = 2n + 1, n=1 => 3
            (2, 1, 2, 5),      # n=2 => 5
            (2, 1, 3, 7),      # n=3 => 7
            (3, 2, 1, 5),      # an = 3n + 2, n=1 => 5
            (3, 2, 2, 8),      # n=2 => 8
            (4, -1, 1, 3),     # an = 4n - 1, n=1 => 3
            (4, -1, 2, 7),     # n=2 => 7
            (5, 0, 1, 5),      # an = 5n, n=1 => 5
            (5, 0, 2, 10),     # n=2 => 10
            (10, 5, 1, 15)     # an = 10n + 5, n=1 => 15
        ],
        'tmpls': [
            "Quick calculation: For \\( a_n = {0}n + {1} \\), find the term for \\( n = {2} \\):",
            "Evaluate \\( a_{{{2}}} \\) when \\( a_n = {0}n + {1} \\):",
            "What is the value of \\( {0}({2}) + {1} \\) in sequence generation?",
            "Calculate \\( a_{{{2}}} \\) for the rule \\( a_n = {0}n + {1} \\):",
            "Compute: \\( a_n = {0}n + {1} \\implies a_{{{2}}} = \\)",
            "Determine the term \\( a_{{{2}}} \\) for \\( a_n = {0}n + {1} \\):",
            "Find the {2}th term of the sequence \\( a_n = {0}n + {1} \\):",
            "Direct evaluation: \\( a_n = {0}n + {1} \\) at \\( n = {2} \\) is:",
            "What is \\( a_{{{2}}} \\) for the sequence \\( a_n = {0}n + {1} \\)?",
            "Find \\( a_{{{2}}} \\): \\( a_n = {0}n + {1} \\):"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            [f"{item[3] + 2}", f"{item[3] - 2}", f"{item[3] * 2}"],
            f"**Step 1: Substitute \\( n = {item[2]} \\) into the general term formula.**\n\\[ a_{{{item[2]}}} = {item[0]}({item[2]}) + {item[1]} \\]\n\n**Step 2: Multiply and add.**\n\\[ a_{{{item[2]}}} = {item[0] * item[2]} + {item[1]} = {item[3]} \\]\n\n**Step 3: State the answer.**\nThe term is {item[3]}."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 8.1.2: Writing general term rules (nth term an)
# ==============================================================================
def gen_8_1_2():
    tc = "CBSE-9-MGM-8-8.1.2"
    tname = "Writing general term rules (nth term an)"

    # Arch 0: Formulating an = dn + (a - d) for arithmetic sequences
    arch0 = {
        'data': [
            ("3, 7, 11, 15, ...", "4n - 1", "d = 4, a₁ = 3 => an = 4n + (3 - 4) = 4n - 1"),
            ("5, 8, 11, 14, ...", "3n + 2", "d = 3, a₁ = 5 => an = 3n + 2"),
            ("2, 9, 16, 23, ...", "7n - 5", "d = 7, a₁ = 2 => an = 7n - 5"),
            ("10, 16, 22, 28, ...", "6n + 4", "d = 6, a₁ = 10 => an = 6n + 4"),
            ("1, 6, 11, 16, ...", "5n - 4", "d = 5, a₁ = 1 => an = 5n - 4"),
            ("4, 10, 16, 22, ...", "6n - 2", "d = 6, a₁ = 4 => an = 6n - 2"),
            ("7, 12, 17, 22, ...", "5n + 2", "d = 5, a₁ = 7 => an = 5n + 2"),
            ("8, 15, 22, 29, ...", "7n + 1", "d = 7, a₁ = 8 => an = 7n + 1"),
            ("12, 20, 28, 36, ...", "8n + 4", "d = 8, a₁ = 12 => an = 8n + 4"),
            ("6, 11, 16, 21, ...", "5n + 1", "d = 5, a₁ = 6 => an = 5n + 1")
        ],
        'tmpls': [
            "Write the general term \\( a_n \\) for the sequence: {0}",
            "Find the nth term formula \\( a_n \\) for the progression: {0}",
            "What is the general rule \\( a_n \\) that generates: {0}?",
            "Express the nth term \\( a_n \\) in terms of n for: {0}",
            "Determine \\( a_n \\) for the linear number sequence: {0}:",
            "Calculate the nth term formula for: {0}",
            "Which algebraic expression represents \\( a_n \\) for: {0}?",
            "Evaluate the general term \\( a_n \\) of the pattern: {0}",
            "Formulate the rule for the nth term of: {0}:",
            "Find \\( a_n \\) for: {0}:"
        ],
        'calc': lambda item: (
            f"\\( a_n = {item[1]} \\)",
            [f"\\( a_n = {item[1].replace('-', '+')} \\)", f"\\( a_n = 2n + 1 \\)", f"\\( a_n = 5n \\)"],
            f"**Step 1: Identify the common difference \\( d \\) and first term \\( a_1 \\).**\n{item[2]}.\n\n**Step 2: Use the nth term formula \\( a_n = a_1 + (n - 1)d \\).**\n\\[ a_n = dn + (a_1 - d) = {item[1]} \\]\n\n**Step 3: State the final general term.**\n\\( a_n = {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Decreasing arithmetic sequences: an = -dn + c
    arch1 = {
        'data': [
            ("100, 95, 90, 85, ...", "105 - 5n", "d = -5, a₁ = 100 => an = 100 + (n-1)(-5) = 105 - 5n"),
            ("50, 46, 42, 38, ...", "54 - 4n", "d = -4, a₁ = 50 => an = 54 - 4n"),
            ("20, 17, 14, 11, ...", "23 - 3n", "d = -3, a₁ = 20 => an = 23 - 3n"),
            ("35, 28, 21, 14, ...", "42 - 7n", "d = -7, a₁ = 35 => an = 42 - 7n"),
            ("80, 72, 64, 56, ...", "88 - 8n", "d = -8, a₁ = 80 => an = 88 - 8n"),
            ("12, 8, 4, 0, ...", "16 - 4n", "d = -4, a₁ = 12 => an = 16 - 4n"),
            ("25, 20, 15, 10, ...", "30 - 5n", "d = -5, a₁ = 25 => an = 30 - 5n"),
            ("60, 54, 48, 42, ...", "66 - 6n", "d = -6, a₁ = 60 => an = 66 - 6n"),
            ("15, 13, 11, 9, ...", "17 - 2n", "d = -2, a₁ = 15 => an = 17 - 2n"),
            ("40, 31, 22, 13, ...", "49 - 9n", "d = -9, a₁ = 40 => an = 49 - 9n")
        ],
        'tmpls': [
            "Find the general term \\( a_n \\) for the decreasing sequence: {0}",
            "Write the formula for the nth term \\( a_n \\) of: {0}",
            "What is \\( a_n \\) for the descending arithmetic sequence: {0}?",
            "Express the general term of the sequence {0} in terms of n:",
            "Determine the rule \\( a_n \\) for the sequence: {0}:",
            "Calculate the nth term formula for: {0}",
            "Which algebraic formula represents the sequence: {0}?",
            "Evaluate \\( a_n \\) for the decreasing progression: {0}",
            "Find the general rule \\( a_n \\) for: {0}:",
            "Compute the nth term \\( a_n \\) of: {0}:"
        ],
        'calc': lambda item: (
            f"\\( a_n = {item[1]} \\)",
            [f"\\( a_n = {item[1].replace('-', '+')} \\)", "\\( a_n = 50 - 5n \\)", "\\( a_n = 100 - n \\)"],
            f"**Step 1: Identify the negative common difference \\( d \\).**\n{item[2]}.\n\n**Step 2: Substitute into \\( a_n = a_1 + (n - 1)d \\).**\n\\[ a_n = {item[1]} \\]\n\n**Step 3: State the final formula.**\n\\( a_n = {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Finding a specific term (e.g. 20th term, 50th term, 100th term) using an
    arch2 = {
        'data': [
            ("an = 4n - 1", 20, 79, "4(20) - 1 = 80 - 1 = 79"),
            ("an = 3n + 2", 25, 77, "3(25) + 2 = 75 + 2 = 77"),
            ("an = 5n - 4", 30, 146, "5(30) - 4 = 150 - 4 = 146"),
            ("an = 7n + 1", 15, 106, "7(15) + 1 = 105 + 1 = 106"),
            ("an = 105 - 5n", 20, 5, "105 - 5(20) = 105 - 100 = 5"),
            ("an = 6n - 2", 50, 298, "6(50) - 2 = 300 - 2 = 298"),
            ("an = 2n² + 1", 5, 51, "2(5²) + 1 = 2(25) + 1 = 51"),
            ("an = n(n + 1)", 10, 110, "10(11) = 110"),
            ("an = 2^n - 1", 8, 255, "2⁸ - 1 = 256 - 1 = 255"),
            ("an = n² - n", 10, 90, "10² - 10 = 100 - 10 = 90")
        ],
        'tmpls': [
            "Given the general term \\( {0} \\), find the {1}th term (\\( a_{{{1}}} \\)):",
            "If the nth term of a sequence is \\( {0} \\), what is \\( a_{{{1}}} \\)?",
            "Calculate \\( a_{{{1}}} \\) for the sequence with rule \\( {0} \\):",
            "What is the value of the {1}th term when \\( {0} \\)?",
            "Evaluate the {1}th term of the progression defined by \\( {0} \\):",
            "Determine \\( a_{{{1}}} \\) using the formula \\( {0} \\):",
            "Find the {1}th term: \\( {0} \\):",
            "Compute \\( a_{{{1}}} \\) for the general term \\( {0} \\):",
            "What number is at position {1} in the sequence \\( {0} \\)?",
            "Find the value of \\( a_{{{1}}} \\) given \\( {0} \\):"
        ],
        'calc': lambda item: (
            f"\\( a_{{{item[1]}}} = {item[2]} \\)",
            [f"\\( a_{{{item[1]}}} = {item[2] + 4} \\)", f"\\( a_{{{item[1]}}} = {item[2] - 4} \\)", f"\\( a_{{{item[1]}}} = {item[2] * 2} \\)"],
            f"**Step 1: Substitute \\( n = {item[1]} \\) into the general term formula.**\n\\[ {item[0]} \\implies a_{{{item[1]}}} = {item[3]} \\]\n\n**Step 2: State the final value.**\n\\( a_{{{item[1]}}} = {item[2]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Determining which term is equal to a given number (solving an = k for n)
    arch3 = {
        'data': [
            ("an = 3n + 2", 95, 31, "3n + 2 = 95 => 3n = 93 => n = 31"),
            ("an = 4n - 1", 119, 30, "4n - 1 = 119 => 4n = 120 => n = 30"),
            ("an = 5n - 4", 246, 50, "5n - 4 = 246 => 5n = 250 => n = 50"),
            ("an = 7n + 1", 148, 21, "7n + 1 = 148 => 7n = 147 => n = 21"),
            ("an = 6n + 4", 124, 20, "6n + 4 = 124 => 6n = 120 => n = 20"),
            ("an = 105 - 5n", 0, 21, "105 - 5n = 0 => 5n = 105 => n = 21"),
            ("an = 54 - 4n", -26, 20, "54 - 4n = -26 => 4n = 80 => n = 20"),
            ("an = 2n + 5", 65, 30, "2n + 5 = 65 => 2n = 60 => n = 30"),
            ("an = 8n - 3", 157, 20, "8n - 3 = 157 => 8n = 160 => n = 20"),
            ("an = 9n + 1", 181, 20, "9n + 1 = 181 => 9n = 180 => n = 20")
        ],
        'tmpls': [
            "Which term of the sequence \\( {0} \\) is equal to {1}?",
            "In the sequence with general term \\( {0} \\), find the index n such that \\( a_n = {1} \\):",
            "Find n if \\( a_n = {1} \\) for the progression \\( {0} \\):",
            "Determine the position n of the term {1} in the sequence \\( {0} \\):",
            "If \\( a_n = {1} \\) in \\( {0} \\), what is the value of n?",
            "Solve for n when the nth term \\( {0} \\) equals {1}:",
            "At which position does the number {1} appear in the sequence \\( {0} \\)?",
            "Calculate n for \\( a_n = {1} \\) given \\( {0} \\):",
            "Evaluate n such that \\( a_n = {1} \\) for \\( {0} \\):",
            "Which term is {1} in \\( {0} \\)?"
        ],
        'calc': lambda item: (
            f"\\( n = {item[2]} \\) ({item[2]}th term)",
            [f"\\( n = {item[2] + 2} \\)", f"\\( n = {item[2] - 2} \\)", f"\\( n = {item[2] + 5} \\)"],
            f"**Step 1: Set \\( a_n = {item[1]} \\).**\n\\[ {item[0]} = {item[1]} \\]\n\n**Step 2: Solve the linear equation for \\( n \\).**\n{item[3]}.\n\n**Step 3: State the position.**\nThe number {item[1]} is the {item[2]}th term (\\( n = {item[2]} \\))."
        ),
        'diff': 'medium'
    }

    # Arch 4: Non-linear general terms (quadratic, rational, exponential)
    arch4 = {
        'data': [
            ("an = n / (n + 1)", "1/2, 2/3, 3/4, 4/5", ["1/3, 2/4, 3/5", "2/3, 3/4, 4/5", "1, 2, 3"]),
            ("an = (n - 1) / n", "0, 1/2, 2/3, 3/4", ["1, 1/2, 1/3", "0, 1, 2", "1/2, 2/3, 3/4"]),
            ("an = 2^n / n", "2, 2, 8/3, 4", ["1, 2, 4", "2, 4, 8", "2, 4, 6"]),
            ("an = (-1)^n * n²", "-1, 4, -9, 16", ["1, -4, 9", "-1, -4, -9", "1, 4, 9"]),
            ("an = n² - 2n", "-1, 0, 3, 8", ["0, 1, 4", "1, 2, 3", "-1, 1, 3"]),
            ("an = 3^n - 1", "2, 8, 26, 80", ["3, 9, 27", "2, 4, 8", "1, 2, 3"]),
            ("an = (n + 1)(n + 2)", "6, 12, 20, 30", ["2, 6, 12", "1, 4, 9", "6, 8, 10"]),
            ("an = n³ - n", "0, 6, 24, 60", ["1, 7, 25", "0, 2, 6", "0, 8, 27"]),
            ("an = 1 / (2n - 1)", "1, 1/3, 1/5, 1/7", ["1/2, 1/4, 1/6", "1, 1/2, 1/3", "2, 4, 6"]),
            ("an = 2^(n-1)", "1, 2, 4, 8", ["2, 4, 8", "1, 3, 5", "0, 2, 4"])
        ],
        'tmpls': [
            "Write the first four terms of the sequence defined by: {0}:",
            "What are the first 4 terms generated by the rule: {0}?",
            "Evaluate the sequence for n = 1, 2, 3, 4 given: {0}:",
            "List the first four values of the sequence: {0}:",
            "Determine the first four entries of the sequence: {0}:",
            "Calculate \\( a_1, a_2, a_3, a_4 \\) for: {0}:",
            "Find the initial four terms corresponding to: {0}:",
            "Which sequence of four terms matches: {0}?",
            "Compute the first four terms for: {0}:",
            "Find \\( a_1, a_2, a_3, a_4 \\) given {0}:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Substitute \\( n = 1, 2, 3, 4 \\) sequentially.**\nCompute each term individually using the given rule {item[0]}.\n\n**Step 2: List the calculated values.**\n\\( a_1, a_2, a_3, a_4 \\) are {item[1]}.\n\n**Step 3: State the answer.**\nThe first four terms are {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical definitions and properties of general terms
    arch5 = {
        'data': [
            ("A formula that expresses the nth term an purely as an explicit function of n is called an:", "explicit formula (general term)", ["recursive formula", "differential equation", "integral"]),
            ("A formula that defines each term using one or more preceding terms (e.g. an = an-1 + d) is called a:", "recurrence relation (recursive formula)", ["explicit formula", "Taylor series", "logarithm"]),
            ("If the general term an of a sequence is a linear polynomial in n (an = An + B), the sequence is ALWAYS an:", "Arithmetic Progression (AP)", ["Geometric Progression (GP)", "Harmonic Progression", "Fibonacci sequence"]),
            ("In the linear general term an = An + B, the common difference d is equal to:", "the coefficient of n (A)", ["the constant term B", "A + B", "A / B"]),
            ("In the linear general term an = An + B, the first term a₁ is equal to:", "A + B", ["A", "B", "A - B"]),
            ("If an = 5n - 3, what is the common difference d of the sequence?", "5 (the coefficient of n)", ["-3", "2", "8"]),
            ("If an = 7 - 2n, what is the common difference d of the sequence?", "-2 (the coefficient of n)", ["7", "5", "2"]),
            ("Can a sequence have terms that are negative numbers?", "Yes, the values an can be any real numbers (positive, negative, or zero)", ["No, terms must be positive integers", "Only if n is negative", "Only in imaginary numbers"]),
            ("Does every sequence have a simple elementary algebraic general term?", "No, some sequences (like primes: 2, 3, 5, 7, ...) have no simple closed algebraic formula", ["Yes, every sequence has one", "Only even numbers have rules", "By definition of function"]),
            ("The nth term of the sequence of even natural numbers 2, 4, 6, 8, ... is:", "an = 2n", ["an = 2n + 1", "an = n²", "an = n + 2"])
        ],
        'tmpls': [
            "{0}",
            "Properties of the general term an: {0}",
            "Theoretical characterization of nth term formulas: {0}",
            "Select the accurate statement: {0}",
            "NCERT theoretical foundation: {0}",
            "Which option correctly states: {0}",
            "Explicit vs recursive definitions: {0}",
            "Identify the valid mathematical principle: {0}",
            "Choose the true property: {0}",
            "Complete the sentence: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: State the property of the general term.**\nAn explicit formula \\( a_n = f(n) \\) gives the value of the \\( n \\)th term directly from its position \\( n \\).\n\n**Step 2: Linear terms and common difference.**\nWhen \\( a_n = An + B \\), the difference between consecutive terms is \\( a_{{n+1}} - a_n = A(n+1) - An = A \\).\n\n**Step 3: Conclude.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: Basic MCQs & True/False statements
    arch6 = {
        'data': [
            ("True or False: If an = 4n + 3, the common difference is 4.", "True", ["False", "It is 3", "Cannot be determined"]),
            ("True or False: The general term of odd natural numbers is an = 2n - 1.", "True", ["False", "It is 2n", "Cannot be determined"]),
            ("True or False: If an = 5n, the first term is 5.", "True", ["False", "It is 1", "Cannot be determined"]),
            ("True or False: The general term of square numbers is an = n².", "True", ["False", "It is 2n", "Cannot be determined"]),
            ("What is the general term for the sequence 2, 4, 6, 8, ...?", "an = 2n", ["an = n + 2", "an = 2n + 1", "an = n²"]),
            ("What is the general term for the sequence 1, 3, 5, 7, ...?", "an = 2n - 1", ["an = 2n", "an = 2n + 1", "an = n + 1"]),
            ("What is the general term for the sequence 10, 20, 30, 40, ...?", "an = 10n", ["an = n + 10", "an = 10n - 1", "an = n²"]),
            ("What is the general term for the sequence 5, 10, 15, 20, ...?", "an = 5n", ["an = n + 5", "an = 5n + 1", "an = 5n - 1"]),
            ("What is the general term for the sequence 1, 8, 27, 64, ...?", "an = n³", ["an = 3n", "an = n²", "an = 3^n"]),
            ("What is the general term for the sequence 2, 4, 8, 16, ...?", "an = 2^n", ["an = 2n", "an = n²", "an = 2n + 2"])
        ],
        'tmpls': [
            "{0}",
            "Direct evaluation: {0}",
            "Basic general term check: {0}",
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
            f"**Step 1: Verify the general formula.**\nTest the formula for \\( n = 1, 2, 3 \\) to verify that it generates the given terms.\n\n**Step 2: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations of a₁ and a₂ from an
    arch7 = {
        'data': [
            (2, 3, 5, 7),      # an = 2n + 3 => a1=5, a2=7
            (3, 1, 4, 7),      # an = 3n + 1 => a1=4, a2=7
            (4, 2, 6, 10),     # an = 4n + 2 => a1=6, a2=10
            (5, -1, 4, 9),     # an = 5n - 1 => a1=4, a2=9
            (6, 1, 7, 13),     # an = 6n + 1 => a1=7, a2=13
            (7, 0, 7, 14),     # an = 7n => a1=7, a2=14
            (10, -2, 8, 18),   # an = 10n - 2 => a1=8, a2=18
            (3, -2, 1, 4),     # an = 3n - 2 => a1=1, a2=4
            (8, 1, 9, 17),     # an = 8n + 1 => a1=9, a2=17
            (9, 2, 11, 20)     # an = 9n + 2 => a1=11, a2=20
        ],
        'tmpls': [
            "Quick check: For \\( a_n = {0}n + {1} \\), what is the first term \\( a_1 \\)?",
            "Calculate \\( a_1 \\) when \\( a_n = {0}n + {1} \\):",
            "What is \\( a_1 = {0}(1) + {1} \\)?",
            "Evaluate \\( a_1 \\) for the rule \\( a_n = {0}n + {1} \\):",
            "Find the first term: \\( a_n = {0}n + {1} \\implies a_1 = \\)",
            "Determine \\( a_1 \\) for \\( a_n = {0}n + {1} \\):",
            "Compute \\( a_1 \\) given \\( a_n = {0}n + {1} \\):",
            "Direct calculation of first term: \\( a_1 \\) for \\( a_n = {0}n + {1} \\) is:",
            "What is the starting term \\( a_1 \\) for \\( a_n = {0}n + {1} \\)?",
            "Find \\( a_1 \\): \\( a_n = {0}n + {1} \\):"
        ],
        'calc': lambda item: (
            f"\\( a_1 = {item[2]} \\)",
            [f"\\( a_1 = {item[3]} \\)", f"\\( a_1 = {item[0]} \\)", f"\\( a_1 = {item[2] + 2} \\)"],
            f"**Step 1: Substitute \\( n = 1 \\).**\n\\[ a_1 = {item[0]}(1) + {item[1]} = {item[0]} + {item[1]} = {item[2]} \\]\n\n**Step 2: State the answer.**\nThe first term is \\( a_1 = {item[2]} \\)."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_8_1_1()
    print(f"gen_8_1_1: {len(q1)} questions")
    q2 = gen_8_1_2()
    print(f"gen_8_1_2: {len(q2)} questions")
