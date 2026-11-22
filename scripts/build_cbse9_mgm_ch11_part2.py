# scripts/build_cbse9_mgm_ch11_part2.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 11: The World of Algorithms
Part 2:
- Subtopic 11.2.1: Division algorithm: Dividend = Divisor * Quotient + Remainder
- Subtopic 11.2.2: Euclid's subtraction method for Greatest Common Divisor (GCD/HCF)
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 11
CH_NAME = "The World of Algorithms"

# ==============================================================================
# SUBTOPIC 11.2.1: Division algorithm: Dividend = Divisor * Quotient + Remainder
# ==============================================================================
def gen_11_2_1():
    tc = "CBSE-9-MGM-11-11.2.1"
    tname = "Division algorithm: Dividend = Divisor * Quotient + Remainder"

    # Arch 0: Calculating Dividend given Divisor, Quotient, Remainder
    arch0 = {
        'data': [
            (12, 7, 5, 89, "12 * 7 + 5 = 84 + 5 = 89"),
            (15, 6, 8, 98, "15 * 6 + 8 = 90 + 8 = 98"),
            (9, 14, 4, 130, "9 * 14 + 4 = 126 + 4 = 130"),
            (8, 23, 3, 187, "8 * 23 + 3 = 184 + 3 = 187"),
            (25, 4, 11, 111, "25 * 4 + 11 = 100 + 11 = 111"),
            (16, 9, 7, 151, "16 * 9 + 7 = 144 + 7 = 151"),
            (7, 31, 2, 219, "7 * 31 + 2 = 217 + 2 = 219"),
            (11, 18, 6, 204, "11 * 18 + 6 = 198 + 6 = 204"),
            (14, 12, 9, 177, "14 * 12 + 9 = 168 + 9 = 177"),
            (20, 15, 13, 313, "20 * 15 + 13 = 300 + 13 = 313")
        ],
        'tmpls': [
            "In the division algorithm, if the divisor is {0}, quotient is {1}, and remainder is {2}, find the dividend:",
            "What is the dividend when divisor = {0}, quotient = {1}, and remainder = {2}?",
            "Using \\( \\text{{Dividend}} = \\text{{Divisor}} \\times \\text{{Quotient}} + \\text{{Remainder}} \\), compute the number for divisor {0}, quotient {1}, remainder {2}:",
            "Calculate the dividend given divisor = {0}, quotient = {1}, and remainder = {2}:",
            "Find the original number that when divided by {0} gives quotient {1} and leaves remainder {2}:",
            "Evaluate the dividend for: divisor {0}, quotient {1}, remainder {2}:",
            "Determine the dividend value: {0} * {1} + {2}:",
            "What number was divided by {0} to obtain quotient {1} and remainder {2}?",
            "Compute the dividend for divisor {0}, quotient {1}, remainder {2}:",
            "Calculate the dividend: divisor = {0}, quotient = {1}, remainder = {2}:"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            [f"{item[3] + 4}", f"{item[3] - 5}", f"{item[3] + 10}"],
            f"**Step 1: State the Division Algorithm.**\n\\[ \\text{{Dividend}} = (\\text{{Divisor}} \\times \\text{{Quotient}}) + \\text{{Remainder}} \\]\n\n**Step 2: Substitute the given values.**\n\\[ \\text{{Dividend}} = ({item[0]} \\times {item[1]}) + {item[2]} = {item[4]} \\]\n\n**Step 3: State the answer.**\nThe dividend is {item[3]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Finding Quotient and Remainder for Given a and b
    arch1 = {
        'data': [
            (85, 9, 9, 4, "85 = 9 * 9 + 4"),
            (142, 11, 12, 10, "142 = 11 * 12 + 10"),
            (73, 8, 9, 1, "73 = 8 * 9 + 1"),
            (215, 14, 15, 5, "215 = 14 * 15 + 5"),
            (99, 7, 14, 1, "99 = 7 * 14 + 1"),
            (160, 13, 12, 4, "160 = 13 * 12 + 4"),
            (185, 12, 15, 5, "185 = 12 * 15 + 5"),
            (250, 16, 15, 10, "250 = 16 * 15 + 10"),
            (310, 20, 15, 10, "310 = 20 * 15 + 10"),
            (125, 6, 20, 5, "125 = 6 * 20 + 5")
        ],
        'tmpls': [
            "When {0} is divided by {1}, find the quotient and remainder:",
            "Apply the division algorithm to {0} and {1}: determine q and r:",
            "Find the quotient and remainder when {0} is divided by {1}:",
            "What are q and r in {0} = {1}q + r (with 0 <= r < {1})?",
            "Divide {0} by {1} and express in the form a = bq + r:",
            "Calculate quotient q and remainder r for {0} ÷ {1}:",
            "Determine q and r for dividend {0} and divisor {1}:",
            "Compute the quotient and remainder when {0} is shared into groups of {1}:",
            "Find (q, r) such that {0} = {1}q + r:",
            "Evaluate the division of {0} by {1}:"
        ],
        'calc': lambda item: (
            f"Quotient = {item[2]}, Remainder = {item[3]}",
            [
                f"Quotient = {item[2] + 1}, Remainder = {item[3]}",
                f"Quotient = {item[2]}, Remainder = {item[3] + 2}",
                f"Quotient = {item[2] - 1}, Remainder = {item[3] + item[1]}"
            ],
            f"**Step 1: Divide {item[0]} by {item[1]}.**\n\\[ {item[0]} \\div {item[1]} = {item[2]} \\text{{ with remainder }} {item[3]} \\]\n\n**Step 2: Express in division algorithm form.**\n\\[ {item[4]} \\]\nVerify that \\( 0 \\le {item[3]} < {item[1]} \\).\n\n**Step 3: State the answer.**\nQuotient = {item[2]}, Remainder = {item[3]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Finding Divisor given Dividend, Quotient, and Remainder
    arch2 = {
        'data': [
            (125, 13, 8, 9, "(125 - 8) / 13 = 117 / 13 = 9"),
            (175, 14, 7, 12, "(175 - 7) / 14 = 168 / 14 = 12"),
            (218, 18, 2, 12, "(218 - 2) / 18 = 216 / 18 = 12"),
            (147, 16, 3, 9, "(147 - 3) / 16 = 144 / 16 = 9"),
            (325, 21, 10, 15, "(325 - 10) / 21 = 315 / 21 = 15"),
            (95, 11, 7, 8, "(95 - 7) / 11 = 88 / 11 = 8"),
            (188, 15, 8, 12, "(188 - 8) / 15 = 180 / 15 = 12"),
            (247, 17, 9, 14, "(247 - 9) / 17 = 238 / 17 = 14"),
            (160, 22, 6, 7, "(160 - 6) / 22 = 154 / 22 = 7"),
            (285, 25, 10, 11, "(285 - 10) / 25 = 275 / 25 = 11")
        ],
        'tmpls': [
            "On dividing {0} by a certain divisor, the quotient is {1} and remainder is {2}. Find the divisor:",
            "What is the divisor if dividend = {0}, quotient = {1}, and remainder = {2}?",
            "Using \\( \\text{{Divisor}} = \\frac{{\\text{{Dividend}} - \\text{{Remainder}}}}{{\\text{{Quotient}}}} \\), find the divisor for {0}, {1}, {2}:",
            "Calculate the divisor when {0} is divided to yield quotient {1} and remainder {2}:",
            "Determine the divisor: dividend = {0}, quotient = {1}, remainder = {2}:",
            "Find the number by which {0} was divided to get quotient {1} and remainder {2}:",
            "Evaluate the divisor for dividend {0}, quotient {1}, remainder {2}:",
            "Compute the divisor: ({0} - {2}) / {1}:",
            "What number divides {0} with quotient {1} leaving remainder {2}?",
            "Solve for the divisor in: {0} = b * {1} + {2}:"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            [f"{item[3] + 2}", f"{item[3] - 1}", f"{item[3] + 5}"],
            f"**Step 1: Rearrange the division algorithm formula to isolate the divisor.**\n\\[ \\text{{Divisor}} = \\frac{{\\text{{Dividend}} - \\text{{Remainder}}}}{{\\text{{Quotient}}}} \\]\n\n**Step 2: Substitute the given numbers.**\n\\[ \\text{{Divisor}} = {item[4]} = {item[3]} \\]\n\n**Step 3: State the answer.**\nThe divisor is {item[3]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Constraints and Range on the Remainder (0 <= r < b)
    arch3 = {
        'data': [
            (8, "0, 1, 2, 3, 4, 5, 6, 7", 8, "Remainder r must satisfy 0 <= r < 8"),
            (5, "0, 1, 2, 3, 4", 5, "Remainder r must satisfy 0 <= r < 5"),
            (6, "0, 1, 2, 3, 4, 5", 6, "Remainder r must satisfy 0 <= r < 6"),
            (4, "0, 1, 2, 3", 4, "Remainder r must satisfy 0 <= r < 4"),
            (10, "0, 1, 2, 3, 4, 5, 6, 7, 8, 9", 10, "Remainder r must satisfy 0 <= r < 10"),
            (3, "0, 1, 2", 3, "Remainder r must satisfy 0 <= r < 3"),
            (7, "0, 1, 2, 3, 4, 5, 6", 7, "Remainder r must satisfy 0 <= r < 7"),
            (12, "0, 1, 2, ..., 11", 12, "12 possible remainders: 0 to 11"),
            (2, "0, 1", 2, "Remainder is 0 for even numbers, 1 for odd numbers"),
            (15, "0, 1, 2, ..., 14", 15, "15 possible remainders: 0 to 14")
        ],
        'tmpls': [
            "In the division algorithm \\( a = bq + r \\), if divisor \\( b = {0} \\), what are all the possible values of the remainder r?",
            "How many possible remainders can be obtained when any positive integer is divided by {0}?",
            "What is the mathematical condition on remainder r when dividing by {0}?",
            "For divisor {0}, state the range of possible remainders r:",
            "What is the maximum possible remainder when dividing a number by {0}?",
            "Can the remainder r be equal to {0} when dividing by {0}?",
            "What is the minimum possible remainder in the division algorithm?",
            "Identify all possible values of r in \\( a = {0}q + r \\):",
            "When dividing by {0}, how many distinct remainders exist?",
            "State the possible remainders when b = {0}:"
        ],
        'calc': lambda item: (
            item[1],
            [
                "1, 2, 3, 4, 5, 6, 7, 8",
                "0 to infinity",
                "Any negative number"
            ],
            f"**Step 1: State the strict constraint on remainder in the Division Algorithm.**\n\\[ 0 \\le r < b \\]\n\n**Step 2: List the allowed values for \\( b = {item[0]} \\).**\n{item[3]}.\n\n**Step 3: State the answer.**\nThe possible values are {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Word problems on Division Algorithm
    arch4 = {
        'data': [
            ("A baker bakes 145 cookies and packs them in boxes of 12. How many full boxes can be packed, and how many cookies are left over?", 12, 1, "145 = 12 * 12 + 1 (12 boxes, 1 left over)"),
            ("A school has 250 students going on a trip. If each bus holds 40 students, how many full buses are filled and how many students are left for the last bus?", 6, 10, "250 = 40 * 6 + 10 (6 full buses, 10 students remaining)"),
            ("A fruit seller has 320 apples and puts them into bags of 15. How many full bags can be made and how many apples remain?", 21, 5, "320 = 15 * 21 + 5 (21 bags, 5 remaining)"),
            ("A rope of length 185 metres is cut into pieces of 8 metres each. How many 8-metre pieces are obtained and what length is left over?", 23, 1, "185 = 8 * 23 + 1 (23 pieces, 1 m left)"),
            ("A book has 450 pages. If a student reads 35 pages per day, how many full days will it take, and how many pages are left for the final day?", 12, 30, "450 = 35 * 12 + 30 (12 full days, 30 pages on final day)"),
            ("780 eggs are packed in cartons of 30 each. How many cartons are needed and how many eggs are left?", 26, 0, "780 = 30 * 26 + 0 (26 cartons, 0 left)"),
            ("A farmer packs 500 kg of wheat into 45 kg sacks. How many full sacks are packed, and how many kg remain?", 11, 5, "500 = 45 * 11 + 5 (11 sacks, 5 kg left)"),
            ("A thread of 225 cm is used to make flower garlands requiring 20 cm each. How many complete garlands can be made?", 11, 5, "225 = 20 * 11 + 5 (11 garlands, 5 cm left)"),
            ("A hall has 620 chairs arranged in rows of 25. How many complete rows are formed and how many chairs are left over?", 24, 20, "620 = 25 * 24 + 20 (24 rows, 20 chairs left)"),
            ("1000 litres of milk is bottled into 8-litre cans. How many full cans are filled?", 125, 0, "1000 = 8 * 125 + 0 (125 full cans, 0 remaining)")
        ],
        'tmpls': [
            "{0}",
            "Solve the real-world division problem: {0}",
            "Apply the division algorithm to solve: {0}",
            "Calculate quotient and remainder for the scenario: {0}",
            "Determine the result: {0}",
            "Evaluate the division application: {0}",
            "Find the full count and remainder: {0}",
            "In practical packaging and sharing: {0}",
            "Solve using division algorithm: {0}",
            "What is the mathematical answer to: {0}?"
        ],
        'calc': lambda item: (
            f"Full = {item[1]}, Remainder = {item[2]}",
            [
                f"Full = {item[1] + 1}, Remainder = {item[2]}",
                f"Full = {item[1]}, Remainder = {item[2] + 4}",
                f"Full = {item[1] - 1}, Remainder = {item[2] + 8}"
            ],
            f"**Step 1: Set up the division problem.**\nApply Dividend = Divisor * Quotient + Remainder.\n\n**Step 2: Carry out the division.**\n{item[3]}.\n\n**Step 3: State the answer.**\nFull = {item[1]}, Remainder = {item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Repeated Subtraction model of division
    arch5 = {
        'data': [
            (24, 6, 4, "24 - 6 = 18; 18 - 6 = 12; 12 - 6 = 6; 6 - 6 = 0 (4 subtractions)"),
            (35, 7, 5, "35 - 7 = 28; 28 - 7 = 21; 21 - 7 = 14; 14 - 7 = 7; 7 - 7 = 0 (5 subtractions)"),
            (28, 5, 5, 3, "28 - 5 = 23; 23 - 5 = 18; 18 - 5 = 13; 13 - 5 = 8; 8 - 5 = 3 (5 subtractions, remainder 3)"),
            (42, 8, 5, 2, "42 - 8 = 34; 34 - 8 = 26; 26 - 8 = 18; 18 - 8 = 10; 10 - 8 = 2 (5 subtractions, remainder 2)"),
            (50, 12, 4, 2, "50 - 12 = 38; 38 - 12 = 26; 26 - 12 = 14; 14 - 12 = 2 (4 subtractions, remainder 2)"),
            (19, 4, 4, 3, "19 - 4 = 15; 15 - 4 = 11; 11 - 4 = 7; 7 - 4 = 3 (4 subtractions, remainder 3)"),
            (31, 6, 5, 1, "31 - 6 = 25; 25 - 6 = 19; 19 - 6 = 13; 13 - 6 = 7; 7 - 6 = 1 (5 subtractions, remainder 1)"),
            (45, 10, 4, 5, "45 - 10 = 35; 35 - 10 = 25; 25 - 10 = 15; 15 - 10 = 5 (4 subtractions, remainder 5)"),
            (60, 15, 4, "60 - 15 = 45; 45 - 15 = 30; 30 - 15 = 15; 15 - 15 = 0 (4 subtractions)"),
            (17, 3, 5, 2, "17 - 3 = 14; 14 - 3 = 11; 11 - 3 = 8; 8 - 3 = 5; 5 - 3 = 2 (5 subtractions, remainder 2)")
        ],
        'tmpls': [
            "In the repeated subtraction model of division, how many times can {1} be subtracted from {0} before the remainder is strictly less than {1}?",
            "Calculate {0} ÷ {1} using repeated subtraction algorithm:",
            "How many subtraction steps of {1} from {0} are performed by the division algorithm?",
            "Trace the repeated subtraction loop: count = 0; while a >= {1}: a = a - {1}, count = count + 1. For a = {0}, what is count?",
            "What is the quotient obtained by repeatedly subtracting {1} from {0}?",
            "Determine the number of subtractions and the final remainder for {0} and {1}:",
            "Evaluate the repeated subtraction algorithm for input ({0}, {1}):",
            "How many times does {1} fit into {0} via sequential subtraction?",
            "Compute the quotient count for: {0} divided by {1} via subtraction:",
            "Trace the subtraction algorithm for ({0}, {1}):"
        ],
        'calc': lambda item: (
            f"{item[2]}",
            [f"{item[2] + 1}", f"{item[2] - 1}", f"{item[2] + 2}"],
            f"**Step 1: Understand division as repeated subtraction.**\nThe quotient \\( q \\) is the number of times the divisor \\( b \\) can be subtracted from dividend \\( a \\) until \\( a < b \\).\n\n**Step 2: Carry out the subtraction chain.**\n{item[3] if len(item) > 3 else item[2]}.\n\n**Step 3: State the answer.**\nThe number of subtractions (quotient) is {item[2]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Polynomial Division Algorithm basics (Introduction to Remainder Theorem)
    arch6 = {
        'data': [
            ("p(x) = g(x) * q(x) + r(x)", "deg(r) < deg(g) or r(x) = 0", "Degree of remainder is strictly less than degree of divisor"),
            ("When a polynomial p(x) is divided by a linear polynomial (x - a), what is the maximum degree of the remainder r(x)?", "Degree 0 (a constant number)", "deg(r) < deg(x - a) = 1, so deg(r) = 0"),
            ("According to the Remainder Theorem, what is the remainder when polynomial p(x) is divided by (x - a)?", "p(a)", "Remainder equals p(a)"),
            ("When p(x) = x^2 - 5x + 6 is divided by (x - 2), what is the remainder p(2)?", "2^2 - 5(2) + 6 = 4 - 10 + 6 = 0", "Remainder is 0, so (x - 2) is a factor"),
            ("When p(x) = x^3 + 1 is divided by (x + 1), what is the remainder p(-1)?", "(-1)^3 + 1 = -1 + 1 = 0", "(x + 1) is a factor"),
            ("When p(x) = 2x^2 + 3x + 1 is divided by (x - 1), what is the remainder p(1)?", "2(1)^2 + 3(1) + 1 = 2 + 3 + 1 = 6", "Remainder = 6"),
            ("If remainder r(x) = 0 in polynomial division p(x) = g(x) * q(x) + r(x), what does this tell us about g(x)?", "g(x) is a factor of p(x) and p(x) is a multiple of g(x)", "Factor theorem connection"),
            ("Can the degree of the remainder ever equal the degree of the divisor in polynomial division?", "No, division continues until the remainder's degree is strictly less than the divisor's degree", "Degree constraint on remainder"),
            ("What is the quotient when x^2 - 4 is divided by (x - 2)?", "x + 2", "(x - 2)(x + 2) / (x - 2) = x + 2"),
            ("In polynomial division, what corresponds to the 'Divisor'?", "The polynomial g(x) by which p(x) is divided", "Analogy to integer division")
        ],
        'tmpls': [
            "{0}",
            "In the polynomial division algorithm: {0}",
            "What is the mathematical condition or value in: {0}?",
            "Identify the correct polynomial property: {0}",
            "Analyze the remainder theorem connection: {0}",
            "Determine the accurate polynomial result: {0}",
            "Which description characterizes: {0}?",
            "In NCERT Class 9 polynomial algorithms: {0}",
            "Select the accurate algebraic fact: {0}",
            "Evaluate the division algorithm for polynomials: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "deg(r) > deg(g)",
                "p(-a)",
                "The remainder is always 1"
            ],
            f"**Step 1: State the Division Algorithm for polynomials.**\n\\( p(x) = g(x)q(x) + r(x) \\) where either \\( r(x) = 0 \\) or \\( \\text{{deg}}(r) < \\text{{deg}}(g) \\).\n\n**Step 2: Evaluate the property.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Foundational Invariants of the Division Algorithm
    arch7 = {
        'data': [
            ("What mathematical theorem guarantees the uniqueness of quotient q and remainder r in a = bq + r?", "The Division Algorithm (Euclidean Division Theorem)", "Uniqueness of q and r"),
            ("Can there exist two different pairs of quotients and remainders (q1, r1) and (q2, r2) for the same dividend and divisor?", "No, the quotient q and remainder r are uniquely determined", "Uniqueness property"),
            ("If a is a multiple of b, what is the remainder r?", "0 (r = 0)", "Exact divisibility"),
            ("If an integer n is divided by 2, what are the only two possible forms of n?", "2q (even) or 2q + 1 (odd)", "Parity forms of integers"),
            ("If an integer n is divided by 3, what are the three possible forms of n?", "3q, 3q + 1, or 3q + 2", "Residue classes modulo 3"),
            ("If an integer n is divided by 4, what are the possible forms of n?", "4q, 4q + 1, 4q + 2, or 4q + 3", "Residue classes modulo 4"),
            ("Why is the division algorithm fundamental to all of number theory and cryptography?", "Because it partitions all integers into disjoint residue classes based on their remainders", "Modular arithmetic foundation"),
            ("What does the notation a ≡ b (mod m) mean in modular arithmetic?", "a and b leave the exact same remainder when divided by m (m divides a - b)", "Congruence modulo m"),
            ("If remainder r is 0 when a is divided by b, we write:", "b | a (b divides a)", "Divisibility relation"),
            ("Can divisor b ever be equal to 0 in the division algorithm?", "No, division by zero is strictly undefined in mathematics", "Divisor b > 0 restriction")
        ],
        'tmpls': [
            "{0}",
            "In the mathematical foundations of the division algorithm: {0}",
            "Identify the invariant property: {0}",
            "What is the mathematical consequence: {0}?",
            "Which statement correctly characterizes: {0}?",
            "Analyze the division algorithm theorem: {0}",
            "Determine the accurate theoretical principle: {0}",
            "In number theory and Class 9 Ganita Manjari: {0}",
            "Select the accurate algebraic insight: {0}",
            "Evaluate the division property: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Yes, multiple remainders can exist for the same division",
                "Divisor can be zero",
                "Remainder can be negative"
            ],
            f"**Step 1: Review the formal statement of the Euclidean Division Algorithm.**\nFor any positive integers \\( a \\) and \\( b \\), there exist unique integers \\( q \\) and \\( r \\) such that \\( a = bq + r \\) with \\( 0 \\le r < b \\).\n\n**Step 2: Apply the property.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 11.2.2: Euclid's subtraction method for Greatest Common Divisor (GCD/HCF)
# ==============================================================================
def gen_11_2_2():
    tc = "CBSE-9-MGM-11-11.2.2"
    tname = "Euclid's subtraction method for Greatest Common Divisor (GCD/HCF)"

    # Arch 0: Euclid's Subtraction Principle: gcd(a, b) = gcd(a - b, b)
    arch0 = {
        'data': [
            ("What fundamental mathematical principle underlies Euclid's subtraction algorithm for GCD?", "gcd(a, b) = gcd(a - b, b) for a > b", "Subtracting the smaller from the larger preserves the common divisors"),
            ("Why does subtracting b from a preserve their greatest common divisor?", "Because any number that divides both a and b must also divide their difference (a - b)", "Divisor of linear combinations"),
            ("When does Euclid's subtraction algorithm terminate?", "When both numbers become equal (a = b); that common value is the GCD", "Termination at equality"),
            ("What was the Greek name for Euclid's subtraction algorithm in Book VII of the Elements?", "Antanairesis (Reciprocal Subtraction / Alternating Subtraction)", "Historical Greek name"),
            ("If a = 30 and b = 12, what is the first subtraction in Euclid's method?", "30 - 12 = 18, so gcd(30, 12) = gcd(18, 12)", "First subtraction step"),
            ("Continuing from (18, 12), what is the next subtraction?", "18 - 12 = 6, so gcd(18, 12) = gcd(12, 6)", "Second subtraction step"),
            ("Continuing from (12, 6), what is the next subtraction?", "12 - 6 = 6, so gcd(12, 6) = gcd(6, 6) = 6", "Final step: both equal 6"),
            ("What is the GCD of 30 and 12 found by this subtraction chain?", "6", "Final common value is 6"),
            ("How does Euclid's subtraction algorithm compare to the modern division algorithm for GCD?", "Division is simply an accelerated form of repeated subtraction (subtracting multiples of b all at once)", "Division as accelerated subtraction"),
            ("Can Euclid's subtraction algorithm find the GCD of ANY two positive integers?", "Yes, it is guaranteed to terminate and correctly find the GCD for any two positive integers", "Universal correctness and termination")
        ],
        'tmpls': [
            "{0}",
            "In Euclid's subtraction algorithm for GCD: {0}",
            "What is the mathematical basis of: {0}?",
            "Identify the correct step or principle in: {0}",
            "Which statement accurately explains: {0}?",
            "Analyze the subtraction method for GCD: {0}",
            "Determine the accurate step in: {0}",
            "In ancient Greek mathematics and Class 9 Ganita Manjari: {0}",
            "Select the accurate algorithmic fact: {0}",
            "Follow Euclid's subtraction logic: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "gcd(a, b) = gcd(a + b, b)",
                "gcd(a, b) = a * b",
                "It terminates when one number reaches zero only"
            ],
            f"**Step 1: Understand Euclid's subtraction principle.**\nIf \\( d \\mid a \\) and \\( d \\mid b \\), then \\( d \\mid (a - b) \\). Therefore \\( \\gcd(a, b) = \\gcd(a - b, b) \\).\n\n**Step 2: Trace the algorithm.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Tracing Euclid's Subtraction Chains
    arch1 = {
        'data': [
            (24, 18, 6, "24 - 18 = 6 -> (18, 6); 18 - 6 = 12 -> (12, 6); 12 - 6 = 6 -> (6, 6) = 6"),
            (35, 14, 7, "35 - 14 = 21 -> (21, 14); 21 - 14 = 7 -> (14, 7); 14 - 7 = 7 -> (7, 7) = 7"),
            (40, 25, 5, "40 - 25 = 15 -> (25, 15); 25 - 15 = 10 -> (15, 10); 15 - 10 = 5 -> (10, 5); 10 - 5 = 5 -> 5"),
            (48, 18, 6, "48 - 18 = 30 -> 30 - 18 = 12 -> 18 - 12 = 6 -> 12 - 6 = 6 -> 6"),
            (56, 21, 7, "56 - 21 = 35 -> 35 - 21 = 14 -> 21 - 14 = 7 -> 14 - 7 = 7 -> 7"),
            (36, 24, 12, "36 - 24 = 12 -> (24, 12); 24 - 12 = 12 -> (12, 12) = 12"),
            (45, 30, 15, "45 - 30 = 15 -> (30, 15); 30 - 15 = 15 -> (15, 15) = 15"),
            (50, 20, 10, "50 - 20 = 30 -> 30 - 20 = 10 -> 20 - 10 = 10 -> 10"),
            (64, 48, 16, "64 - 48 = 16 -> 48 - 16 = 32 -> 32 - 16 = 16 -> 16"),
            (75, 45, 15, "75 - 45 = 30 -> 45 - 30 = 15 -> 30 - 15 = 15 -> 15")
        ],
        'tmpls': [
            "Use Euclid's subtraction algorithm to find the GCD of {0} and {1}:",
            "Trace the subtraction sequence to find \\( \\gcd({0}, {1}) \\):",
            "What is the HCF of {0} and {1} determined by repeated subtraction?",
            "Calculate \\( \\gcd({0}, {1}) \\) using Euclid's method:",
            "Determine the greatest common divisor of {0} and {1} via subtraction:",
            "Find the GCD({0}, {1}) by subtracting the smaller from the larger:",
            "Evaluate \\( \\text{{HCF}}({0}, {1}) \\) using the ancient Greek algorithm:",
            "What common value is reached when Euclid's subtraction is applied to ({0}, {1})?",
            "Compute \\( \\gcd({0}, {1}) \\) step-by-step:",
            "Trace Euclid's subtraction algorithm for pair ({0}, {1}):"
        ],
        'calc': lambda item: (
            f"{item[2]}",
            [f"{item[2] * 2}", f"{item[2] + 2}", "1" if item[2] != 1 else "2"],
            f"**Step 1: Apply Euclid's subtraction rule: replace \\( (a, b) \\) with \\( (a - b, b) \\) where \\( a > b \\).**\n\n**Step 2: Trace the subtraction chain.**\n{item[3]}.\n\n**Step 3: State the answer.**\nThe GCD is {item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Number of Subtraction Steps in Euclid's Algorithm
    arch2 = {
        'data': [
            (24, 18, 3, "24-18=6 (step 1); 18-6=12 (step 2); 12-6=6 (step 3) -> 3 steps"),
            (35, 14, 3, "35-14=21 (step 1); 21-14=7 (step 2); 14-7=7 (step 3) -> 3 steps"),
            (36, 24, 2, "36-24=12 (step 1); 24-12=12 (step 2) -> 2 steps"),
            (45, 30, 2, "45-30=15 (step 1); 30-15=15 (step 2) -> 2 steps"),
            (40, 25, 4, "40-25=15 (1); 25-15=10 (2); 15-10=5 (3); 10-5=5 (4) -> 4 steps"),
            (20, 5, 3, "20-5=15 (1); 15-5=10 (2); 10-5=5 (3) -> 3 steps"),
            (16, 4, 3, "16-4=12 (1); 12-4=8 (2); 8-4=4 (3) -> 3 steps"),
            (50, 10, 4, "50-10=40 (1); 40-10=30 (2); 30-10=20 (3); 20-10=10 (4) -> 4 steps"),
            (15, 10, 1, "15-10=5; 10-5=5 -> 2 steps"),
            (100, 25, 3, "100-25=75 (1); 75-25=50 (2); 50-25=25 (3) -> 3 steps")
        ],
        'tmpls': [
            "How many subtraction steps are required by Euclid's subtraction algorithm to find \\( \\gcd({0}, {1}) \\)?",
            "Trace the number of subtractions needed to reduce ({0}, {1}) to equal numbers:",
            "Count the exact number of subtraction operations performed in Euclid's algorithm for ({0}, {1}):",
            "In finding the GCD of {0} and {1} via subtraction, how many steps are executed?",
            "Determine the step count of the subtraction loop for inputs ({0}, {1}):",
            "Calculate how many subtractions occur for pair ({0}, {1}):",
            "Evaluate the number of steps in Euclid's subtraction method for ({0}, {1}):",
            "How many times is the subtraction statement executed for ({0}, {1})?",
            "Find the iteration count of the subtraction algorithm for ({0}, {1}):",
            "Trace and count the subtraction steps for ({0}, {1}):"
        ],
        'calc': lambda item: (
            f"{item[2]}",
            [f"{item[2] + 1}", f"{item[2] - 1 if item[2] > 1 else item[2] + 2}", f"{item[2] + 3}"],
            f"**Step 1: Carry out each subtraction until the two numbers are equal.**\n\n**Step 2: List the steps.**\n{item[3]}.\n\n**Step 3: State the answer.**\nThe algorithm takes {item[2]} subtraction steps."
        ),
        'diff': 'medium'
    }

    # Arch 3: Coprime numbers and Euclid's algorithm terminating at 1
    arch3 = {
        'data': [
            (15, 8, 1, "15 - 8 = 7; 8 - 7 = 1; 7 - 1 = 6; ...; 2 - 1 = 1 -> gcd = 1 (Coprime)"),
            (21, 10, 1, "21 - 10 = 11; 11 - 10 = 1; ...; gcd = 1 (Coprime)"),
            (14, 9, 1, "14 - 9 = 5; 9 - 5 = 4; 5 - 4 = 1; ...; gcd = 1 (Coprime)"),
            (25, 12, 1, "25 - 12 = 13; 13 - 12 = 1; ...; gcd = 1 (Coprime)"),
            (35, 16, 1, "35 - 16 = 19; 19 - 16 = 3; 16 - 3 = 13; ...; gcd = 1 (Coprime)"),
            (18, 7, 1, "18 - 7 = 11; 11 - 7 = 4; 7 - 4 = 3; 4 - 3 = 1; ...; gcd = 1 (Coprime)"),
            (27, 20, 1, "27 - 20 = 7; 20 - 7 = 13; 13 - 7 = 6; 7 - 6 = 1; ...; gcd = 1 (Coprime)"),
            (16, 15, 1, "Two consecutive integers are always coprime: 16 - 15 = 1 (gcd = 1)"),
            (100, 99, 1, "Consecutive integers gcd(n, n+1) = gcd(n+1 - n, n) = gcd(1, n) = 1"),
            ("Two positive integers a and b are called 'coprime' (or mutually prime) if:", "Their greatest common divisor gcd(a, b) = 1", "Definition of coprime numbers")
        ],
        'tmpls': [
            "Use Euclid's algorithm to determine \\( \\gcd({0}, {1}) \\):",
            "Are the numbers {0} and {1} coprime? What is their GCD?",
            "Evaluate \\( \\gcd({0}, {1}) \\) using repeated subtraction:",
            "Find the highest common factor of {0} and {1}:",
            "Determine whether {0} and {1} share any common factor greater than 1:",
            "Calculate \\( \\gcd({0}, {1}) \\) and state if they are coprime:",
            "What is the result of applying Euclid's subtraction to ({0}, {1})?",
            "Compute the GCD of the coprime pair ({0}, {1}):",
            "Trace the subtraction algorithm for: {0} and {1}:",
            "What is \\( \\gcd({0}, {1}) \\)?"
        ],
        'calc': lambda item: (
            f"{item[2]}" if isinstance(item[0], int) else item[1],
            [
                "2" if isinstance(item[0], int) else "Their sum is prime",
                "3" if isinstance(item[0], int) else "Both numbers are prime",
                "5" if isinstance(item[0], int) else "They have no factors at all"
            ],
            f"**Step 1: Apply Euclid's subtraction algorithm.**\n\n**Step 2: Trace until equality.**\n{item[3] if isinstance(item[0], int) else item[2]}.\n\n**Step 3: State the answer.**\nThe GCD is {item[2] if isinstance(item[0], int) else item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Geometric Visualization of Euclid's Algorithm (Tiling a Rectangle with Squares)
    arch4 = {
        'data': [
            ("A rectangle of dimensions 30 cm by 12 cm is to be completely tiled with identical square tiles of maximum possible size. What is the side length of the largest square tile?", 6, "gcd(30, 12) = 6 cm"),
            ("A floor measuring 48 metres by 18 metres is tiled with largest possible square marble slabs. What is the side of each slab?", 6, "gcd(48, 18) = 6 m"),
            ("A rectangular room is 35 m long and 14 m wide. What is the side length of the largest square tile that can tile it with no cutting?", 7, "gcd(35, 14) = 7 m"),
            ("A sheet of paper 36 cm by 24 cm is cut into equal squares of largest possible size without any paper waste. What is the side of each square?", 12, "gcd(36, 24) = 12 cm"),
            ("A courtyard 40 m by 25 m is to be paved with largest identical square paving stones. What is the side length of each paving stone?", 5, "gcd(40, 25) = 5 m"),
            ("How does cutting out the largest possible square (b x b) from rectangle (a x b) relate to Euclid's algorithm?", "The remaining smaller rectangle has dimensions (a - b) by b, which geometrically represents gcd(a, b) = gcd(a - b, b)", "Geometric square cutting interpretation"),
            ("When does the geometric square-tiling process terminate?", "When the remaining rectangle is itself a perfect square (side = GCD), tiling the previous rectangle completely", "Tiling termination at square"),
            ("In tiling a 30 cm by 12 cm rectangle, how many 12x12 squares are first cut out?", 2, "30 = 2 * 12 + 6 (two 12x12 squares cut out, leaving a 12x6 rectangle)"),
            ("What squares tile the remaining 12 cm by 6 cm rectangle?", "Two 6x6 squares, completing the tiling with square size 6 cm", "12 = 2 * 6, perfect tiling"),
            ("Why is the geometric tiling proof considered one of the most intuitive demonstrations of Euclid's algorithm?", "Because it makes the algebraic division step visible as physical square tiles covering an area without gaps", "Visual intuition of Euclidean division")
        ],
        'tmpls': [
            "{0}",
            "Solve the geometric tiling problem: {0}",
            "Find the maximum square tile size for: {0}",
            "Apply Euclid's algorithm geometrically to solve: {0}",
            "What is the answer to the tiling question: {0}?",
            "Determine the largest square dimensions in: {0}",
            "Evaluate the geometric Euclidean scenario: {0}",
            "Calculate the required square side length for: {0}",
            "In applied Euclidean geometry: {0}",
            "Select the accurate dimension for: {0}"
        ],
        'calc': lambda item: (
            f"{item[1]} cm" if isinstance(item[1], int) and "cm" in item[0] else (f"{item[1]} m" if isinstance(item[1], int) and "m" in item[0] else str(item[1])),
            [
                "3 cm" if "cm" in item[0] else ("3 m" if "m" in item[0] else "It terminates at a circle"),
                "4 cm" if "cm" in item[0] else ("4 m" if "m" in item[0] else "Only 1 square can be cut"),
                "10 cm" if "cm" in item[0] else ("10 m" if "m" in item[0] else "Squares cannot tile rectangles")
            ],
            f"**Step 1: Relate the maximum tile problem to the Greatest Common Divisor.**\nThe largest square tile that can tile a rectangle of \\( a \\times b \\) has side length equal to \\( \\gcd(a, b) \\).\n\n**Step 2: Compute \\( \\gcd(a, b) \\).**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe side length is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Comparison of Subtraction Algorithm vs Division Algorithm for GCD
    arch5 = {
        'data': [
            ("To find gcd(1000, 2) using subtraction, how many subtraction steps are needed?", "499 subtractions (1000 - 2, 998 - 2, ..., down to 2)", "Worst case for subtraction"),
            ("To find gcd(1000, 2) using Euclid's division algorithm (remainder), how many division steps are needed?", "Exactly 1 division step (1000 = 2 * 500 + 0, remainder 0 -> gcd = 2)", "Single step via division"),
            ("Why is the Division version of Euclid's algorithm vastly faster than the Subtraction version for disparate numbers?", "Because division computes the quotient q and subtracts all q multiples in a single step (a mod b)", "Accelerated repeated subtraction"),
            ("In the division version of Euclid's algorithm, what replaces the pair (a, b)?", "(b, a mod b) where a mod b is the remainder r", "Standard modern Euclidean algorithm"),
            ("When does the Division version of Euclid's algorithm terminate?", "When the remainder r reaches 0; the last non-zero divisor is the GCD", "Termination at remainder 0"),
            ("Which pair of numbers represents the WORST-CASE input for Euclid's division algorithm (taking maximum steps for their size)?", "Consecutive Fibonacci numbers (e.g. 89 and 55)", "Lamé's Theorem (1844)"),
            ("What does Gabriel Lamé's Theorem (1844) prove about Euclid's division algorithm?", "The number of division steps never exceeds 5 times the number of decimal digits of the smaller number", "First historical proof of algorithmic complexity"),
            ("If a = 55 and b = 34 (consecutive Fibonacci numbers), every quotient in Euclid's division algorithm is:", "Always equal to 1", "Fibonacci quotients are all 1"),
            ("What is the time complexity of the modern Euclidean division algorithm?", "Logarithmic: O(log(min(a, b)))", "Logarithmic complexity"),
            ("Why did Euclid originally formulate the algorithm using subtraction rather than division in the Elements?", "Because Greek mathematics treated numbers as geometric line lengths, and subtraction corresponded to physical segment cutting", "Historical geometric context")
        ],
        'tmpls': [
            "{0}",
            "In comparing the subtraction and division versions of Euclid's algorithm: {0}",
            "Why does the division method improve upon subtraction: {0}?",
            "Identify the correct algorithmic property: {0}",
            "Which statement accurately evaluates: {0}?",
            "Analyze the computational efficiency: {0}",
            "Determine the accurate answer: {0}",
            "In Lamé's theorem and algorithmic complexity: {0}",
            "Select the accurate comparison: {0}",
            "In Class 9 algorithms and number theory: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Subtraction is faster than division",
                "Both algorithms always take the exact same number of steps",
                "The division algorithm only works for prime numbers"
            ],
            f"**Step 1: Understand the computational relationship between subtraction and division.**\nDivision groups multiple subtractions \\( a - qb \\) into a single remainder operation \\( a \\pmod b \\).\n\n**Step 2: Detail the comparison.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: The Fundamental Relation: HCF(a, b) * LCM(a, b) = a * b
    arch6 = {
        'data': [
            (12, 18, 6, 36, "HCF * LCM = 6 * 36 = 216; a * b = 12 * 18 = 216"),
            (15, 20, 5, 60, "HCF * LCM = 5 * 60 = 300; a * b = 15 * 20 = 300"),
            (8, 12, 4, 24, "HCF * LCM = 4 * 24 = 96; a * b = 8 * 12 = 96"),
            (14, 21, 7, 42, "HCF * LCM = 7 * 42 = 294; a * b = 14 * 21 = 294"),
            (16, 24, 8, 48, "HCF * LCM = 8 * 48 = 384; a * b = 16 * 24 = 384"),
            (25, 35, 5, 175, "HCF * LCM = 5 * 175 = 875; a * b = 25 * 35 = 875"),
            (10, 15, 5, 30, "HCF * LCM = 5 * 30 = 150; a * b = 10 * 15 = 150"),
            (18, 27, 9, 54, "HCF * LCM = 9 * 54 = 486; a * b = 18 * 27 = 486"),
            (20, 30, 10, 60, "HCF * LCM = 10 * 60 = 600; a * b = 20 * 30 = 600"),
            (9, 15, 3, 45, "HCF * LCM = 3 * 45 = 135; a * b = 9 * 15 = 135")
        ],
        'tmpls': [
            "If the HCF of {0} and {1} is {2}, find their LCM using the product formula \\( \\text{{HCF}} \\times \\text{{LCM}} = a \\times b \\):",
            "Given that \\( \\gcd({0}, {1}) = {2} \\), calculate \\( \\text{{LCM}}({0}, {1}) \\):",
            "What is the LCM of {0} and {1} if their HCF is {2}?",
            "Using \\( \\text{{LCM}} = \\frac{{a \\times b}}{{\\text{{HCF}}}} \\), compute LCM for numbers {0} and {1} with HCF = {2}:",
            "Calculate the LCM: ({0} * {1}) / {2}:",
            "Find the Least Common Multiple of {0} and {1} given HCF = {2}:",
            "Evaluate \\( \\text{{LCM}}({0}, {1}) \\) from the relation \\( \\text{{HCF}} \\times \\text{{LCM}} = a \\times b \\):",
            "Determine the LCM of {0} and {1}:",
            "Compute the least common multiple using HCF = {2}:",
            "Solve for LCM({0}, {1}) with known HCF = {2}:"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            [f"{item[3] + 10}", f"{item[3] * 2}", f"{item[3] // 2}"],
            f"**Step 1: Write down the fundamental HCF-LCM relation for two numbers.**\n\\[ \\text{{HCF}}(a, b) \\times \\text{{LCM}}(a, b) = a \\times b \\]\n\n**Step 2: Solve for LCM.**\n\\[ \\text{{LCM}} = \\frac{{a \\times b}}{{\\text{{HCF}}}} = \\frac{{{item[0]} \\times {item[1]}}}{{{item[2]}}} = {item[3]} \\]\n\n**Step 3: State the answer.**\nThe LCM is {item[3]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Modern Applications of Euclid's GCD Algorithm
    arch7 = {
        'data': [
            ("In simplifying a fraction p/q to its lowest terms, by what number should both numerator and denominator be divided?", "Their Greatest Common Divisor gcd(p, q)", "Dividing by GCD reduces fraction to lowest terms in one step"),
            ("To reduce the fraction 48/60 to lowest terms in a single step, what is gcd(48, 60)?", 12, "48/12 = 4, 60/12 = 5 -> 4/5"),
            ("To reduce 35/49 to lowest terms, divide by gcd(35, 49) which is:", 7, "35/7 = 5, 49/7 = 7 -> 5/7"),
            ("Which modern public-key cryptography algorithm fundamentally relies on the Extended Euclidean Algorithm to compute modular inverses?", "The RSA Cryptosystem", "RSA encryption key generation"),
            ("In computer graphics, which line-drawing algorithm uses principles of the division algorithm to decide which pixels to illuminate?", "Bresenham's Line Algorithm", "Integer rasterization without floating point"),
            ("What does Bezout's Identity state regarding gcd(a, b)?", "There exist integers x and y such that ax + by = gcd(a, b)", "Linear combination equals GCD"),
            ("Can gcd(a, b) always be expressed as an integer linear combination ax + by?", "Yes, by Bezout's Identity (computed via Extended Euclidean Algorithm)", "Bezout's Identity"),
            ("If gcd(a, b) = 1, what does Bezout's identity state?", "There exist integers x and y such that ax + by = 1", "Coprime linear combination"),
            ("Why is Euclid's algorithm considered one of the oldest and most important algorithms in human history?", "Because it was discovered over 2,300 years ago and remains the fastest, most optimal method to compute GCDs in modern supercomputers today", "Enduring algorithmic supremacy"),
            ("What is the primary conceptual takeaway from studying Euclid's subtraction algorithm in Ganita Manjari?", "That profound mathematical procedures can emerge from simple, repetitive mechanical rules (subtraction)", "Algorithmic thinking paradigm")
        ],
        'tmpls': [
            "{0}",
            "In modern applications of Euclid's algorithm: {0}",
            "Identify the application or mathematical principle: {0}",
            "Which concept explains: {0}?",
            "What is the computational role of: {0}?",
            "Analyze the significance of Euclid's GCD algorithm: {0}",
            "Determine the accurate answer: {0}",
            "In computer science, cryptography, and Class 9 mathematics: {0}",
            "Select the accurate algorithmic insight: {0}",
            "Evaluate the practical impact of: {0}"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [
                f"{item[1] + 2}" if isinstance(item[1], int) else "The DES system",
                f"{item[1] - 2}" if isinstance(item[1], int) else "ax + by = 0 always",
                "1" if isinstance(item[1], int) else "It has no modern applications"
            ],
            f"**Step 1: Understand the practical application of GCD.**\nEuclid's algorithm simplifies fractions, computes modular inverses in cryptography, and rasterizes lines in computer graphics.\n\n**Step 2: Detail the specific application.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_11_2_1()
    q2 = gen_11_2_2()
    print(f"gen_11_2_1: {len(q1)} questions")
    print(f"gen_11_2_2: {len(q2)} questions")
