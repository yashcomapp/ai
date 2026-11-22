# scripts/build_cbse9_mgm_ch8_part3.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 8: Predicting What Comes Next?: Exploring Sequences and Progressions
Part 3:
- Subtopic 8.3.1: Multiplicative sequences and doubling growth
- Subtopic 8.3.2: Sequences in nature: Fibonacci pattern, tree branching
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 8
CH_NAME = "Predicting What Comes Next?: Exploring Sequences and Progressions"

# ==============================================================================
# SUBTOPIC 8.3.1: Multiplicative sequences and doubling growth
# ==============================================================================
def gen_8_3_1():
    tc = "CBSE-9-MGM-8-8.3.1"
    tname = "Multiplicative sequences and doubling growth"

    # Arch 0: Doubling sequences (powers of 2)
    arch0 = {
        'data': [
            (1, 4, 16, "1 * 2^4 = 16"),
            (1, 5, 32, "1 * 2^5 = 32"),
            (1, 6, 64, "1 * 2^6 = 64"),
            (1, 7, 128, "1 * 2^7 = 128"),
            (2, 3, 16, "2 * 2^3 = 16"),
            (3, 4, 48, "3 * 2^4 = 48"),
            (5, 3, 40, "5 * 2^3 = 40"),
            (10, 4, 160, "10 * 2^4 = 160"),
            (1, 8, 256, "1 * 2^8 = 256"),
            (1, 10, 1024, "1 * 2^10 = 1024")
        ],
        'tmpls': [
            "A population of bacteria starts with {0} cell(s) and doubles every hour. How many bacteria will be present after {1} hours?",
            "If an initial quantity of {0} unit(s) doubles at each step, what will the quantity be after {1} doubling cycles?",
            "In a doubling growth pattern beginning at {0}, find the value at stage {1}:",
            "A single culture of {0} organism(s) undergoes binary fission doubling each cycle. Calculate the population after {1} cycles:",
            "Determine the amount after {1} time periods if an initial count of {0} repeatedly doubles:",
            "In a doubling sequence where the initial term is {0}, calculate the value at step {1}:",
            "What is the final quantity if {0} doubles {1} consecutive times?",
            "Evaluate the doubling growth model for {0} initial item(s) after {1} doubling intervals:",
            "A computer algorithm doubles its memory allocation from {0} MB each cycle. How much memory is allocated after {1} cycles?",
            "Find the result of doubling {0} exactly {1} times:"
        ],
        'calc': lambda item: (
            f"{item[2]}",
            [f"{item[2] * 2}", f"{item[2] // 2 if item[2] // 2 > 0 else item[2] + 4}", f"{item[2] + 10}"],
            f"**Step 1: Write down the doubling growth formula.**\nThe quantity after \\( n \\) doublings with initial count \\( A_0 \\) is \\( A_n = A_0 \\times 2^n \\).\n\n**Step 2: Substitute the given values.**\nHere, \\( A_0 = {item[0]} \\) and \\( n = {item[1]} \\):\n\\[ A_{{{item[1]}}} = {item[0]} \\times 2^{{{item[1]}}} = {item[3]} = {item[2]} \\]\n\n**Step 3: State the final result.**\nThe quantity is {item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Tripling and general multiplicative patterns
    arch1 = {
        'data': [
            (1, 3, 3, 27, "1 * 3^3 = 27"),
            (1, 3, 4, 81, "1 * 3^4 = 81"),
            (2, 3, 3, 54, "2 * 3^3 = 54"),
            (5, 3, 2, 45, "5 * 3^2 = 45"),
            (1, 4, 3, 64, "1 * 4^3 = 64"),
            (2, 5, 2, 50, "2 * 5^2 = 50"),
            (1, 5, 3, 125, "1 * 5^3 = 125"),
            (3, 3, 3, 81, "3 * 3^3 = 81"),
            (4, 3, 2, 36, "4 * 3^2 = 36"),
            (10, 3, 3, 270, "10 * 3^3 = 270")
        ],
        'tmpls': [
            "A multiplicative pattern starts with {0} and multiplies by {1} at each step. Find the value after {2} steps:",
            "If a quantity of {0} triples/multiplies by a factor of {1} every period, what is the amount after {2} periods?",
            "In a geometric growth sequence with first term {0} and multiplier {1}, compute the value at step {2}:",
            "Calculate the result when {0} is multiplied by {1} for {2} consecutive iterations:",
            "Find the term at cycle {2} if the initial term is {0} and the common factor is {1}:",
            "What is the value after {2} rounds of multiplying {0} by {1}?",
            "Determine the quantity obtained by scaling {0} by a factor of {1} across {2} cycles:",
            "In a growth model where \\( y = {0} \\times {1}^x \\), find \\( y \\) when \\( x = {2} \\):",
            "Compute the term corresponding to step {2} starting from {0} with growth ratio {1}:",
            "Evaluate the multiplicative sequence at stage {2} with base {0} and common ratio {1}:"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            [f"{item[3] + item[1]}", f"{item[3] * item[1]}", f"{item[3] - 10}"],
            f"**Step 1: Identify the multiplicative rule.**\nEach step multiplies the previous term by \\( r = {item[1]} \\). The formula is \\( T = a \\times r^n \\).\n\n**Step 2: Compute the value.**\n\\[ T = {item[0]} \\times {item[1]}^{{{item[2]}}} = {item[4]} = {item[3]} \\]\n\n**Step 3: State the answer.**\nThe value after {item[2]} steps is {item[3]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Common ratio r in geometric / multiplicative sequences
    arch2 = {
        'data': [
            ("2, 6, 18, 54, ...", 3, "6 / 2 = 3"),
            ("3, 12, 48, 192, ...", 4, "12 / 3 = 4"),
            ("5, 10, 20, 40, ...", 2, "10 / 5 = 2"),
            ("100, 50, 25, 12.5, ...", "1/2", "50 / 100 = 1/2"),
            ("7, 21, 63, 189, ...", 3, "21 / 7 = 3"),
            ("1, 5, 25, 125, ...", 5, "5 / 1 = 5"),
            ("64, 16, 4, 1, ...", "1/4", "16 / 64 = 1/4"),
            ("4, 24, 144, 864, ...", 6, "24 / 4 = 6"),
            ("10, 100, 1000, ...", 10, "100 / 10 = 10"),
            ("9, 27, 81, 243, ...", 3, "27 / 9 = 3")
        ],
        'tmpls': [
            "Find the common ratio \\( r \\) of the multiplicative sequence: {0}",
            "What is the common multiplier \\( r \\) in the sequence {0}?",
            "Identify the common ratio of the geometric progression: {0}",
            "In the multiplicative sequence {0}, determine the constant ratio \\( r \\):",
            "Calculate \\( r = \\frac{{a_2}}{{a_1}} \\) for the progression: {0}",
            "What factor multiplies each term to produce the next in {0}?",
            "Find the growth/decay factor \\( r \\) in: {0}",
            "Determine the common ratio for the geometric sequence: {0}",
            "Evaluate the constant multiplicative factor of: {0}",
            "Compute the common ratio \\( r \\) in: {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1]} + 1" if isinstance(item[1], int) else "2", f"{item[1]} * 2" if isinstance(item[1], int) else "1/3", f"{item[1]} - 1" if isinstance(item[1], int) else "3/4"],
            f"**Step 1: State the formula for the common ratio.**\nThe common ratio is \\( r = \\frac{{a_2}}{{a_1}} = \\frac{{a_3}}{{a_2}} \\).\n\n**Step 2: Calculate the ratio of consecutive terms.**\n\\[ r = {item[2]} \\]\n\n**Step 3: Conclude the common ratio.**\nThe common ratio \\( r \\) is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Repeated halving / exponential decay
    arch3 = {
        'data': [
            (80, 1, 40, "80 * (1/2)^1 = 40"),
            (80, 2, 20, "80 * (1/2)^2 = 20"),
            (80, 3, 10, "80 * (1/2)^3 = 10"),
            (80, 4, 5, "80 * (1/2)^4 = 5"),
            (64, 3, 8, "64 * (1/2)^3 = 8"),
            (128, 4, 8, "128 * (1/2)^4 = 8"),
            (100, 2, 25, "100 * (1/2)^2 = 25"),
            (256, 5, 8, "256 * (1/2)^5 = 8"),
            (200, 3, 25, "200 * (1/2)^3 = 25"),
            (512, 6, 8, "512 * (1/2)^6 = 8")
        ],
        'tmpls': [
            "A substance has an initial mass of {0} grams and undergoes radioactive decay, halving every hour. What is the remaining mass after {1} hours?",
            "If an initial quantity of {0} is halved {1} consecutive times, what is the final remaining quantity?",
            "In an exponential decay model where {0} halves each cycle, determine the amount left after {1} cycles:",
            "A sheet of paper has area {0} cm². If its area is halved {1} times by repeated cutting, what is its final area?",
            "Calculate the value after {1} halving periods starting with an initial amount of {0}:",
            "What quantity remains if {0} units undergo {1} successive halving steps?",
            "Evaluate the decaying sequence starting at {0} with common ratio 1/2 after {1} steps:",
            "Find the remaining amount of {0} after {1} half-life cycles:",
            "A medicine dose of {0} mg in the bloodstream halves every 2 hours. What amount remains after {1} halving intervals?",
            "Determine the result of dividing {0} by 2 repeatedly {1} times:"
        ],
        'calc': lambda item: (
            f"{item[2]}",
            [f"{item[2] * 2}", f"{item[2] + 4}", f"{item[2] // 2 if item[2] // 2 > 0 else 1}"],
            f"**Step 1: Use the exponential decay formula.**\nThe amount remaining after \\( n \\) halving cycles is \\( A_n = A_0 \\times \\left(\\frac{{1}}{{2}}\\right)^n \\).\n\n**Step 2: Substitute given values.**\n\\[ A_{{{item[1]}}} = {item[0]} \\times \\left(\\frac{{1}}{{2}}\\right)^{{{item[1]}}} = {item[3]} = {item[2]} \\]\n\n**Step 3: State the answer.**\nThe remaining amount is {item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Exponential vs Linear comparison
    arch4 = {
        'data': [
            ("Sequence A: 2, 4, 6, 8, ... and Sequence B: 2, 4, 8, 16, ...", "Sequence A is linear (AP with d = 2) and Sequence B is exponential (GP with r = 2)", "Linear has constant difference; Exponential has constant multiplier"),
            ("Sequence A: 5, 10, 15, 20, ... and Sequence B: 5, 10, 20, 40, ...", "Sequence A is linear (+5) while Sequence B is doubling (x2)", "Add 5 vs multiply by 2"),
            ("A plan offering ₹100 increase per day vs a plan doubling ₹1 each day", "The doubling plan grows exponentially and surpasses the linear plan quickly", "Exponential growth always eventually outpaces linear growth"),
            ("Sequence A: 3, 6, 9, 12, ... and Sequence B: 3, 9, 27, 81, ...", "Sequence A has common difference 3; Sequence B has common ratio 3", "Additive vs multiplicative rule"),
            ("Sequence: 10, 20, 30, 40, ...", "Linear arithmetic sequence with d = 10", "Consecutive terms have constant difference 10"),
            ("Sequence: 10, 20, 40, 80, ...", "Multiplicative geometric sequence with r = 2", "Consecutive terms have constant ratio 2"),
            ("Which grows faster for large n: linear an = 100n or exponential bn = 2^n?", "Exponential bn = 2^n grows vastly faster than linear an = 100n", "Exponential growth dominates polynomial/linear growth"),
            ("Sequence: 1, 3, 5, 7, ... vs Sequence: 1, 3, 9, 27, ...", "First is AP (+2), second is GP (*3)", "Constant difference 2 vs constant ratio 3"),
            ("Repeated addition of 4 vs repeated multiplication by 4", "Addition creates an AP, multiplication creates a GP", "Linear growth vs exponential growth"),
            ("If a quantity triples every year, the growth is:", "Exponential (multiplicative) growth", "Multiplication by constant factor 3 each year represents exponential growth")
        ],
        'tmpls': [
            "Compare the two patterns: {0}. Which statement is correct?",
            "Analyze the nature of growth in: {0}:",
            "Identify the correct classification for: {0}:",
            "Which of the following correctly describes: {0}?",
            "Evaluate the growth characteristics of: {0}:",
            "In mathematics, how do we distinguish: {0}?",
            "What is the key difference described in: {0}?",
            "Determine the correct statement regarding: {0}:",
            "Which description accurately characterizes: {0}?",
            "Assess the sequences: {0}. The true statement is:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [
                "Both sequences are linear arithmetic progressions",
                "Both sequences are exponential doubling sequences",
                "Linear growth always exceeds exponential growth for large n"
            ],
            f"**Step 1: Examine the transition between consecutive terms.**\nCheck whether consecutive terms differ by a constant addition \\( d \\) or a constant multiplier \\( r \\).\n\n**Step 2: Characterize the growth.**\n{item[2]}.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: nth term of geometric progression a_n = a * r^(n-1)
    arch5 = {
        'data': [
            (2, 3, 4, 54, "2 * 3^3 = 2 * 27 = 54"),
            (3, 2, 5, 48, "3 * 2^4 = 3 * 16 = 48"),
            (5, 2, 6, 160, "5 * 2^5 = 5 * 32 = 160"),
            (1, 4, 4, 64, "1 * 4^3 = 64"),
            (7, 2, 4, 56, "7 * 2^3 = 56"),
            (2, 5, 3, 50, "2 * 5^2 = 50"),
            (4, 3, 4, 108, "4 * 3^3 = 4 * 27 = 108"),
            (10, 2, 5, 160, "10 * 2^4 = 10 * 16 = 160"),
            (1, 3, 5, 81, "1 * 3^4 = 81"),
            (3, 3, 4, 81, "3 * 3^3 = 81")
        ],
        'tmpls': [
            "Find the {2}th term of the geometric sequence with first term \\( a = {0} \\) and common ratio \\( r = {1} \\):",
            "In a geometric progression where \\( a_1 = {0} \\) and \\( r = {1} \\), what is \\( a_{{{2}}} \\)?",
            "Calculate the {2}th term \\( a_{{{2}}} \\) of a GP having first term {0} and common ratio {1}:",
            "Determine the value of term {2} in the sequence defined by \\( a_n = {0} \\times {1}^{{n-1}} \\):",
            "For a multiplicative progression with initial term {0} and ratio {1}, find the {2}th term:",
            "What is \\( a_{{{2}}} \\) for the sequence with \\( a = {0} \\) and \\( r = {1} \\)?",
            "Compute the {2}th element of the geometric sequence \\( a = {0}, r = {1} \\):",
            "Evaluate \\( a_{{{2}}} \\) using the formula \\( a_n = a \\cdot r^{{n-1}} \\) with \\( a = {0}, r = {1} \\):",
            "Find the term number {2} when \\( a = {0} \\) and \\( r = {1} \\):",
            "In a GP with \\( a = {0} \\) and common ratio {1}, determine the {2}th term:"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            [f"{item[3] + 12}", f"{item[3] - 8}", f"{item[3] * 2}"],
            f"**Step 1: Write down the nth term formula of a GP.**\nThe \\( n \\)-th term of a geometric progression is given by \\( a_n = a \\cdot r^{{n-1}} \\).\n\n**Step 2: Substitute \\( a = {item[0]} \\), \\( r = {item[1]} \\), and \\( n = {item[2]} \\).**\n\\[ a_{{{item[2]}}} = {item[0]} \\times {item[1]}^{{{item[2]} - 1}} = {item[4]} \\]\n\n**Step 3: State the answer.**\nThe {item[2]}th term is {item[3]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Number of doublings to reach a threshold
    arch6 = {
        'data': [
            (1, 64, 6, "2^6 = 64"),
            (1, 128, 7, "2^7 = 128"),
            (1, 256, 8, "2^8 = 256"),
            (1, 512, 9, "2^9 = 512"),
            (1, 1024, 10, "2^10 = 1024"),
            (2, 64, 5, "2 * 2^5 = 64"),
            (3, 48, 4, "3 * 2^4 = 48"),
            (5, 80, 4, "5 * 2^4 = 80"),
            (10, 160, 4, "10 * 2^4 = 160"),
            (2, 128, 6, "2 * 2^6 = 128")
        ],
        'tmpls': [
            "If an initial colony of {0} cell(s) doubles every hour, after how many hours will the population reach {1}?",
            "How many doubling cycles are required for an initial quantity of {0} to reach {1}?",
            "A quantity starts at {0} and doubles periodically. Find the number of steps \\( n \\) needed to reach {1}:",
            "Determine the time \\( n \\) such that \\( {0} \\times 2^n = {1} \\):",
            "How many doublings must occur to increase an initial count of {0} to {1}?",
            "Solve for \\( n \\) in the doubling equation: \\( {0} \\times 2^n = {1} \\):",
            "A file size doubles every minute starting at {0} MB. After how many minutes does it reach {1} MB?",
            "Calculate the number of generations needed for {0} organism(s) to multiply into {1} by binary fission:",
            "Find the power \\( n \\) of 2 satisfying the growth from {0} to {1}:",
            "After how many doubling intervals does {0} become {1}?"
        ],
        'calc': lambda item: (
            f"{item[2]}",
            [f"{item[2] + 1}", f"{item[2] - 1}", f"{item[2] + 2}"],
            f"**Step 1: Set up the doubling equation.**\nLet \\( n \\) be the number of doublings. Then \\( {item[0]} \\times 2^n = {item[1]} \\).\n\n**Step 2: Solve for \\( 2^n \\).**\n\\[ 2^n = \\frac{{{item[1]}}}{{{item[0]}}} = {item[1] // item[0]} \\]\nSince \\( {item[3]} \\), we have \\( n = {item[2]} \\).\n\n**Step 3: State the result.**\nThe required number of doublings is {item[2]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Real-world doubling applications (paper folding, chessboard grains)
    arch7 = {
        'data': [
            ("A sheet of paper of thickness 0.1 mm is folded in half 10 times. What is its thickness?", "0.1 * 2^10 = 0.1 * 1024 = 102.4 mm", "102.4 mm", ["51.2 mm", "10.24 mm", "204.8 mm"]),
            ("On square 1 of a chessboard there is 1 grain, square 2 has 2 grains, square 3 has 4 grains. How many grains are on square 8?", "2^(8-1) = 2^7 = 128 grains", "128", ["64", "256", "512"]),
            ("On square 10 of a chessboard following doubling, how many grains are placed?", "2^(10-1) = 2^9 = 512 grains", "512", ["256", "1024", "128"]),
            ("If a rumor is told to 2 people, each of whom tells 2 new people (doubling each round), how many new people hear it in round 5?", "2^5 = 32 people", "32", ["16", "64", "10"]),
            ("An investment doubles every 7 years. In 21 years (3 doubling periods), by what factor has it multiplied?", "2^3 = 8 times", "8 times", ["6 times", "16 times", "4 times"]),
            ("If water lily leaves on a pond double every day and completely cover the pond on Day 20, on which day was the pond half covered?", "Day 19 (since one more doubling makes it full on Day 20)", "Day 19", ["Day 10", "Day 18", "Day 15"]),
            ("A bacteria sample doubles every 30 minutes. Starting from 100 cells, how many cells are present after 2 hours (4 doublings)?", "100 * 2^4 = 100 * 16 = 1600 cells", "1600", ["800", "3200", "400"]),
            ("Folding a paper doubles the number of layers. After 7 folds, how many layers are there?", "2^7 = 128 layers", "128", ["64", "256", "14"]),
            ("A chain message doubles the number of recipients every day. How many receive it on Day 6 starting with 1 person on Day 1?", "2^(6-1) = 2^5 = 32", "32", ["64", "16", "12"]),
            ("In the legend of the chessboard, the number of grains on square n is given by which formula?", "2^(n - 1)", "2^(n - 1)", ["2^n", "2n", "n^2"])
        ],
        'tmpls': [
            "{0}",
            "Solve the real-world doubling problem: {0}",
            "Calculate the outcome of the exponential scenario: {0}",
            "In this practical application of doubling growth: {0}",
            "Determine the correct answer for: {0}",
            "Evaluate the doubling model in: {0}",
            "Find the solution for: {0}",
            "Consider the classic problem: {0}",
            "Compute the result for the given growth case: {0}",
            "Analyze and solve: {0}"
        ],
        'calc': lambda item: (
            item[2],
            item[3],
            f"**Step 1: Identify the underlying doubling model.**\nIn each stage or cycle, the quantity multiplies by a factor of 2.\n\n**Step 2: Perform the calculation.**\n{item[1]}.\n\n**Step 3: State the answer.**\nThe answer is {item[2]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 8.3.2: Sequences in nature: Fibonacci pattern, tree branching
# ==============================================================================
def gen_8_3_2():
    tc = "CBSE-9-MGM-8-8.3.2"
    tname = "Sequences in nature: Fibonacci pattern, tree branching"

    # Arch 0: The Fibonacci Sequence next terms
    arch0 = {
        'data': [
            ("1, 1, 2, 3, 5, 8, ...", 13, "5 + 8 = 13", "7th term"),
            ("1, 1, 2, 3, 5, 8, 13, ...", 21, "8 + 13 = 21", "8th term"),
            ("1, 1, 2, 3, 5, 8, 13, 21, ...", 34, "13 + 21 = 34", "9th term"),
            ("1, 1, 2, 3, 5, 8, 13, 21, 34, ...", 55, "21 + 34 = 55", "10th term"),
            ("1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...", 89, "34 + 55 = 89", "11th term"),
            ("1, 1, 2, 3, 5, ...", 8, "3 + 5 = 8", "6th term"),
            ("2, 3, 5, 8, 13, ...", 21, "8 + 13 = 21", "next Fibonacci term"),
            ("1, 1, 2, 3, ...", 5, "2 + 3 = 5", "5th term"),
            ("55, 89, 144, ...", 233, "89 + 144 = 233", "next Fibonacci term"),
            ("34, 55, 89, ...", 144, "55 + 89 = 144", "12th Fibonacci term")
        ],
        'tmpls': [
            "Find the next term in the Fibonacci sequence: {0}",
            "What number comes next in the classic Fibonacci pattern: {0}?",
            "Identify the missing next term in the Fibonacci progression: {0}",
            "In the Fibonacci sequence {0}, determine the subsequent term:",
            "Calculate the next value following: {0}",
            "Predict what comes next in the biological Fibonacci sequence: {0}:",
            "What is the {3} in the Fibonacci sequence: {0}?",
            "Determine the next term of: {0}",
            "Find the value that follows in the Fibonacci pattern: {0}",
            "Evaluate the continuation of the Fibonacci numbers: {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1] + 3}", f"{item[1] - 4}", f"{item[1] + 8}"],
            f"**Step 1: Recall the definition of the Fibonacci sequence.**\nEach term after the first two is the sum of the two preceding terms: \\( F_n = F_{{n-1}} + F_{{n-2}} \\).\n\n**Step 2: Add the last two terms.**\n\\[ {item[2]} \\]\n\n**Step 3: State the answer.**\nThe next term is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Identifying Fibonacci recurrence relation
    arch1 = {
        'data': [
            ("Fn = Fn-1 + Fn-2 with F1 = 1, F2 = 1", "Fibonacci recurrence relation", "Each term is the sum of the two preceding terms"),
            ("F1 = 1, F2 = 1, F3 = 2, F4 = 3, F5 = 5. What is F6?", "8", "F6 = F5 + F4 = 5 + 3 = 8"),
            ("F6 = 8 and F7 = 13. What is F8?", "21", "F8 = F7 + F6 = 13 + 8 = 21"),
            ("F8 = 21 and F9 = 34. What is F10?", "55", "F10 = F9 + F8 = 34 + 21 = 55"),
            ("F10 = 55 and F11 = 89. What is F12?", "144", "F12 = F11 + F10 = 89 + 55 = 144"),
            ("Which formula defines the Fibonacci sequence for n >= 3?", "Fn = Fn-1 + Fn-2", "Linear recurrence of order 2"),
            ("If F(n) = 13 and F(n+1) = 21, what is F(n+2)?", "34", "F(n+2) = F(n+1) + F(n) = 21 + 13 = 34"),
            ("If F(n-1) = 34 and F(n) = 55, what is F(n-2)?", "21", "F(n-2) = F(n) - F(n-1) = 55 - 34 = 21"),
            ("What are the first two initial seeds of the standard Fibonacci sequence?", "F1 = 1 and F2 = 1", "Initial conditions of the sequence"),
            ("If a sequence has a1 = 1, a2 = 2 and an = an-1 + an-2, what is a5?", "8", "a3 = 3, a4 = 5, a5 = 8")
        ],
        'tmpls': [
            "{0}",
            "Evaluate the recurrence property: {0}",
            "Solve using the Fibonacci recurrence relation: {0}",
            "In the mathematical study of Fibonacci numbers: {0}",
            "Determine the correct value or relation for: {0}",
            "Find the answer based on Fibonacci recurrence: {0}",
            "Calculate using the rule of preceding sums: {0}",
            "What is the result for: {0}?",
            "Identify the correct option for: {0}",
            "Apply the Fibonacci formula to find: {0}"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1]} + 2" if item[1].isdigit() else "Fn = Fn-1 * Fn-2", f"{item[1]} - 3" if item[1].isdigit() else "Fn = 2Fn-1", "0"],
            f"**Step 1: State the recursive relation.**\nThe recurrence relation is \\( F_n = F_{{n-1}} + F_{{n-2}} \\).\n\n**Step 2: Compute the required term.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Tree branching and Fibonacci in nature
    arch2 = {
        'data': [
            ("A tree grows in such a way that each new branch takes one year before it can produce a new branch. The number of branches each year follows 1, 2, 3, 5, 8, ... How many branches will there be in year 6?", 13, "Year 6 = 8 + 5 = 13 branches"),
            ("In an idealised model of tree branching, branch counts year by year follow Fibonacci numbers: 1, 2, 3, 5, 8, 13. What is the branch count in the next year?", 21, "13 + 8 = 21 branches"),
            ("Why does tree branching often follow the Fibonacci pattern in botany?", "Because each new shoot needs one growth cycle to mature before producing a secondary branch", "Biological maturation cycle mirrors Fibonacci addition"),
            ("A plant stem has 1 branch in year 1, 2 in year 2, 3 in year 3, 5 in year 4. How many in year 7?", 21, "Year 5 = 8, Year 6 = 13, Year 7 = 21"),
            ("A sneeze-weed plant adds new branches following the sequence 1, 1, 2, 3, 5, 8, ... How many branch tips are present at level 7?", 13, "Level 7 = 13"),
            ("How many branches are produced at generation 5 of a Fibonacci branching tree if generation 1 has 1 branch?", 5, "Gen 1: 1, Gen 2: 2, Gen 3: 3, Gen 4: 5, Gen 5: 8, or counting 1, 1, 2, 3, 5"),
            ("In botanical phyllotaxis, the arrangement of leaves around a stem often involves fractions of Fibonacci numbers such as:", "1/2, 2/3, 3/5, 5/8", "Consecutive Fibonacci ratios in leaf spirals"),
            ("The branching pattern of blood vessels and bronchioles in human lungs exhibits fractal branching closely related to:", "Fibonacci and self-similar branching ratios", "Optimal area-preserving branching"),
            ("If a bamboo stalk branches into 3 shoots, then 5, then 8, the next branching level will likely have how many shoots?", 13, "5 + 8 = 13"),
            ("A coral structure divides following Fibonacci counts: 2, 3, 5, 8, ... What is the count at the next division tier?", 13, "5 + 8 = 13")
        ],
        'tmpls': [
            "{0}",
            "Solve the botanical branching question: {0}",
            "Consider the biological sequence model: {0}",
            "In natural growth patterns: {0}",
            "Determine the correct answer for the branching model: {0}",
            "Analyze the biological Fibonacci phenomenon: {0}",
            "Calculate the count for the natural sequence: {0}",
            "Evaluate the botanical problem: {0}",
            "Find the correct value or explanation: {0}",
            "What is the result for: {0}?"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1] + 5}" if isinstance(item[1], int) else "Because branches grow strictly in powers of 2", f"{item[1] - 3}" if isinstance(item[1], int) else "Random mutation with no mathematical pattern", "34" if isinstance(item[1], int) else "1/4, 2/4, 3/4"],
            f"**Step 1: Identify the Fibonacci branching model.**\nIn tree branching, the number of active branches at each stage follows the Fibonacci sequence where each stage adds mature branches from two generations ago.\n\n**Step 2: Compute or state the value.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Spirals in nature (sunflower seeds, pinecones, pineapples)
    arch3 = {
        'data': [
            ("A sunflower head often displays two sets of spirals turning in opposite directions. Typical spiral counts are pair of consecutive Fibonacci numbers such as:", "21 and 34, or 34 and 55", "Sunflower florets pack optimally with consecutive Fibonacci spiral numbers"),
            ("Pinecones usually have spiral counts winding clockwise and counter-clockwise that are consecutive Fibonacci numbers, commonly:", "5 and 8, or 8 and 13", "Classic pinecone spiral parastichies"),
            ("A pineapple surface features hexagonal scales organized in three distinct spiral directions with counts that are Fibonacci numbers, specifically:", "8, 13, and 21", "Pineapple spiral counts are consecutive Fibonacci numbers"),
            ("Why does nature use Fibonacci spirals in seed packing (like sunflowers)?", "To maximize packing density without leaving gaps as the flower head grows", "Optimal packing efficiency using the golden angle (approx 137.5 degrees)"),
            ("The golden angle that allows optimal packing of seeds in a spiral is approximately:", "137.5°", "360° * (1 - 1/phi) ≈ 137.5077°"),
            ("If a small daisy has 21 clockwise spirals, how many counter-clockwise spirals would it most typically possess?", "34", "Consecutive Fibonacci pair (21, 34)"),
            ("Which of the following numbers of petals is MOST commonly observed in flowers due to Fibonacci patterns?", "5 petals (e.g., buttercup, wild rose)", "Flowers commonly have 3, 5, 8, 13, 21 petals"),
            ("A daisy flower head is examined and found to have 34 spirals in one direction. The adjacent spiral family will most likely count:", "55", "Consecutive Fibonacci numbers: 34 and 55"),
            ("Which mollusk shell forms an equiangular / logarithmic spiral closely approximating the Fibonacci spiral?", "Nautilus shell", "The chambered Nautilus builds logarithmic growth chambers"),
            ("The geometric figure formed by drawing quarter-circle arcs inside adjacent squares with side lengths 1, 1, 2, 3, 5, 8, 13 is called the:", "Fibonacci Spiral (Golden Spiral)", "Constructed from nested squares of Fibonacci side lengths")
        ],
        'tmpls': [
            "{0}",
            "Solve the botanical spiral question: {0}",
            "In the context of spirals in nature: {0}",
            "Regarding natural Fibonacci patterns: {0}",
            "Identify the correct fact: {0}",
            "Analyze the natural packing model: {0}",
            "What is the mathematical reason or value for: {0}?",
            "Evaluate the spiral phenomenon in botany: {0}",
            "Which choice correctly answers: {0}?",
            "Consider Fibonacci spirals in living organisms: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "10 and 20, or 20 and 40",
                "Strictly powers of 2 (4, 8, 16)",
                "Random uneven numbers with no mathematical pattern"
            ] if not item[1].endswith("°") and not item[1].isdigit() else (
                ["90°", "180°", "45°"] if item[1].endswith("°") else ["25", "40", "15"]
            ),
            f"**Step 1: Relate the biological structure to Fibonacci numbers.**\nNatural spirals, seed heads, and flower petals exhibit Fibonacci numbers due to optimal packing algorithms governed by the golden ratio.\n\n**Step 2: Explain the specific occurrence.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Golden ratio approximation (Fn+1 / Fn)
    arch4 = {
        'data': [
            (1, 1, "1.0", "1 / 1 = 1.0"),
            (2, 1, "2.0", "2 / 1 = 2.0"),
            (3, 2, "1.5", "3 / 2 = 1.5"),
            (5, 3, "1.667", "5 / 3 ≈ 1.667"),
            (8, 5, "1.6", "8 / 5 = 1.6"),
            (13, 8, "1.625", "13 / 8 = 1.625"),
            (21, 13, "1.615", "21 / 13 ≈ 1.615"),
            (34, 21, "1.619", "34 / 21 ≈ 1.619"),
            (55, 34, "1.618", "55 / 34 ≈ 1.618"),
            (89, 55, "1.618", "89 / 55 ≈ 1.618")
        ],
        'tmpls': [
            "Calculate the ratio of consecutive Fibonacci numbers \\( \\frac{{{0}}}{{{1}}} \\) to three decimal places:",
            "What is the value of \\( \\frac{{F_{{n+1}}}}{{F_n}} = \\frac{{{0}}}{{{1}}} \\)?",
            "In approaching the Golden Ratio \\( \\phi \\), evaluate \\( \\frac{{{0}}}{{{1}}} \\):",
            "Find the decimal quotient of consecutive Fibonacci terms \\( {0} \\div {1} \\):",
            "Compute the ratio \\( \\frac{{{0}}}{{{1}}} \\) associated with the golden proportion:",
            "Evaluate the fraction \\( \\frac{{{0}}}{{{1}}} \\):",
            "What is the ratio \\( \\frac{{{0}}}{{{1}}} \\) rounded to three decimal places?",
            "Determine the quotient of the Fibonacci pair \\( \\frac{{{0}}}{{{1}}} \\):",
            "Calculate \\( {0} / {1} \\) as an approximation of the Golden Ratio:",
            "Find the numerical value of \\( \\frac{{{0}}}{{{1}}} \\):"
        ],
        'calc': lambda item: (
            f"{item[2]}",
            [f"{float(item[2]) + 0.1:.3f}", f"{float(item[2]) - 0.1:.3f}", "1.414"],
            f"**Step 1: Write down the ratio of the consecutive Fibonacci numbers.**\n\\[ \\text{{Ratio}} = \\frac{{{item[0]}}}{{{item[1]}}} \\]\n\n**Step 2: Carry out the division.**\n\\[ {item[3]} \\]\n\n**Step 3: State the answer.**\nThe ratio is {item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: The Golden Ratio phi = (1 + sqrt(5))/2 and its properties
    arch5 = {
        'data': [
            ("What is the exact algebraic value of the Golden Ratio phi?", "(1 + \\sqrt{5}) / 2", "Root of x^2 - x - 1 = 0"),
            ("To three decimal places, the Golden Ratio phi is approximately equal to:", "1.618", "phi = (1 + 2.236068) / 2 ≈ 1.618"),
            ("As n approaches infinity, the ratio of consecutive Fibonacci numbers Fn+1 / Fn converges to:", "The Golden Ratio phi = (1 + \\sqrt{5}) / 2", "Fundamental limit of Fibonacci sequence"),
            ("Which quadratic equation has the Golden Ratio phi as its positive root?", "x^2 - x - 1 = 0", "phi^2 = phi + 1"),
            ("What is the unique property of the Golden Ratio regarding its reciprocal 1/phi?", "1/phi = phi - 1 ≈ 0.618", "Its reciprocal is exactly 1 less than itself"),
            ("What is the square of the Golden Ratio phi^2?", "phi + 1 ≈ 2.618", "From x^2 - x - 1 = 0, phi^2 = phi + 1"),
            ("A rectangle whose aspect ratio length/width is equal to phi is called a:", "Golden Rectangle", "Proportions aesthetically pleasing and self-replicating"),
            ("If a square is cut off from a Golden Rectangle, the remaining rectangle is:", "Another smaller Golden Rectangle", "Self-similarity of the golden proportion"),
            ("The Golden Ratio is denoted by the Greek letter:", "phi (\\phi)", "Named after the Greek sculptor Phidias"),
            ("Which of the following is true about phi?", "phi is an irrational algebraic number", "Because \\sqrt{5} is irrational")
        ],
        'tmpls': [
            "{0}",
            "In mathematics and geometry: {0}",
            "Regarding the properties of the Golden Ratio: {0}",
            "Identify the correct mathematical fact: {0}",
            "Determine the correct statement: {0}",
            "What is the exact value or relationship for: {0}?",
            "Evaluate the golden proportion concept: {0}",
            "Which option correctly answers: {0}?",
            "Consider the golden proportion: {0}",
            "Solve the problem regarding the Golden Ratio: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "\\sqrt{2}",
                "x^2 + x - 1 = 0" if "equation" in item[0] else "1.414",
                "2.000" if "decimal" in item[0] else "(1 - \\sqrt{5}) / 2"
            ],
            f"**Step 1: Recall the definition of the Golden Ratio \\( \\phi \\).**\nTwo quantities \\( a \\) and \\( b \\) (with \\( a > b \\)) are in the golden ratio if \\( \\frac{{a+b}}{{a}} = \\frac{{a}}{{b}} = \\phi \\).\n\n**Step 2: Solve the defining equation.**\n\\( 1 + \\frac{{1}}{{\\phi}} = \\phi \\implies \\phi^2 - \\phi - 1 = 0 \\implies \\phi = \\frac{{1 + \\sqrt{{5}}}}{{2}} \\approx 1.618 \\).\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Fibonacci Rabbit Problem (Fibonacci's Original 1202 Problem in Liber Abaci)
    arch6 = {
        'data': [
            ("A pair of newborn rabbits (one male, one female) are put in a field. Rabbits take 1 month to mature and produce a new pair each month thereafter. How many pairs of rabbits are there at month 1?", "1 pair", "The original newborn pair"),
            ("In Fibonacci's rabbit model, how many pairs of rabbits are there at month 2?", "1 pair", "The pair matures but produces no offspring yet"),
            ("In Fibonacci's rabbit model, how many pairs of rabbits are there at month 3?", "2 pairs", "The mature pair produces 1 new pair (1 + 1 = 2)"),
            ("In Fibonacci's rabbit model, how many pairs of rabbits are there at month 4?", "3 pairs", "The mature pair produces another pair (2 + 1 = 3)"),
            ("In Fibonacci's rabbit model, how many pairs of rabbits are there at month 5?", "5 pairs", "Two mature pairs each produce a pair (3 + 2 = 5)"),
            ("In Fibonacci's rabbit model, how many pairs of rabbits are there at month 6?", "8 pairs", "Three mature pairs each produce a pair (5 + 3 = 8)"),
            ("In Fibonacci's rabbit model, how many pairs of rabbits are there at month 7?", "13 pairs", "Five mature pairs produce pairs (8 + 5 = 13)"),
            ("In Fibonacci's rabbit model, how many pairs of rabbits are there at month 8?", "21 pairs", "Eight mature pairs produce pairs (13 + 8 = 21)"),
            ("In which famous 1202 AD book did Leonardo of Pisa (Fibonacci) introduce this sequence to Western mathematics?", "Liber Abaci (The Book of Calculation)", "Introduced Hindu-Arabic numerals and the rabbit puzzle"),
            ("The sequence of rabbit pairs month by month: 1, 1, 2, 3, 5, 8, 13, ... is known today as:", "The Fibonacci Sequence", "Named by Edouard Lucas in the 19th century")
        ],
        'tmpls': [
            "{0}",
            "Solve the classic mathematical problem: {0}",
            "In Fibonacci's historical rabbit breeding puzzle: {0}",
            "Calculate the count according to Fibonacci's model: {0}",
            "Determine the solution to: {0}",
            "Evaluate the classic 1202 puzzle: {0}",
            "What is the answer to: {0}?",
            "Find the correct number of rabbit pairs: {0}",
            "Regarding the historical rabbit problem: {0}",
            "Analyze the growth model: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "4 pairs" if "pairs" in item[1] else "De Divina Proportione",
                "6 pairs" if "pairs" in item[1] else "Euclid's Elements",
                "10 pairs" if "pairs" in item[1] else "The Arithmetic Progression"
            ],
            f"**Step 1: Understand Fibonacci's breeding model.**\nTotal pairs at month \\( n \\) equals the pairs present in month \\( n-1 \\) plus new pairs born from mature pairs (which were present in month \\( n-2 \\)).\n\n**Step 2: Apply the recurrence.**\n\\[ P_n = P_{{n-1}} + P_{{n-2}} \\]\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Sum of Fibonacci numbers and identities
    arch7 = {
        'data': [
            ("F1 + F2 + F3 + F4 = 1 + 1 + 2 + 3", "7", "Sum = 7 (which equals F6 - 1 = 8 - 1 = 7)"),
            ("F1 + F2 + F3 + F4 + F5 = 1 + 1 + 2 + 3 + 5", "12", "Sum = 12 (which equals F7 - 1 = 13 - 1 = 12)"),
            ("F1 + F2 + ... + F6 = 1 + 1 + 2 + 3 + 5 + 8", "20", "Sum = 20 (which equals F8 - 1 = 21 - 1 = 20)"),
            ("F1 + F2 + ... + F7 = 1 + 1 + 2 + 3 + 5 + 8 + 13", "33", "Sum = 33 (which equals F9 - 1 = 34 - 1 = 33)"),
            ("What is the general identity for the sum of the first n Fibonacci numbers: F1 + F2 + ... + Fn?", "Fn+2 - 1", "Sum from i=1 to n of Fi = Fn+2 - 1"),
            ("What is F1^2 + F2^2 + F3^2 + F4^2 = 1^2 + 1^2 + 2^2 + 3^2 = 1 + 1 + 4 + 9?", "15", "Sum of squares = 15 = F4 * F5 = 3 * 5 = 15"),
            ("What is the general identity for the sum of squares: F1^2 + F2^2 + ... + Fn^2?", "Fn * Fn+1", "Proven geometrically by Fibonacci rectangles"),
            ("Evaluate F5^2 + F6^2 = 5^2 + 8^2 = 25 + 64:", "89", "89 = F11 (since Fn^2 + Fn+1^2 = F2n+1)"),
            ("Evaluate Cassini's identity for n = 5: F4 * F6 - F5^2 = 3 * 8 - 5^2 = 24 - 25:", "-1", "Cassini's identity: Fn-1 * Fn+1 - Fn^2 = (-1)^n"),
            ("Evaluate Cassini's identity for n = 6: F5 * F7 - F6^2 = 5 * 13 - 8^2 = 65 - 64:", "1", "Cassini's identity: (-1)^6 = 1")
        ],
        'tmpls': [
            "Compute the value of: {0}:",
            "Evaluate the Fibonacci sum or identity: {0}:",
            "What is the result of: {0}?",
            "Find the numerical value or formula for: {0}:",
            "Determine the result of the Fibonacci identity: {0}:",
            "Calculate: {0}:",
            "Evaluate: {0}:",
            "In Fibonacci mathematics, what is: {0}?",
            "What is the value of the expression: {0}?",
            "Find the answer for: {0}:"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"{int(item[1]) + 2}" if item[1].lstrip('-').isdigit() else "Fn+1 - 1",
                f"{int(item[1]) - 2}" if item[1].lstrip('-').isdigit() else "Fn * Fn",
                "0" if item[1].lstrip('-').isdigit() else "Fn+2 + 1"
            ],
            f"**Step 1: State the relevant Fibonacci identity or sum.**\n{item[2]}.\n\n**Step 2: Compute the result.**\nEvaluating the expression yields {item[1]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_8_3_1()
    q2 = gen_8_3_2()
    print(f"gen_8_3_1: {len(q1)} questions")
    print(f"gen_8_3_2: {len(q2)} questions")
