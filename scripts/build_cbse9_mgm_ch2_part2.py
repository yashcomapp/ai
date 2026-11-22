# scripts/build_cbse9_mgm_ch2_part2.py
# Subtopics:
# 2.2.1: Evaluating p(k) for given value k (80 Qs)
# 2.2.2: Finding zero of linear polynomial ax + b algebraically (80 Qs)

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 2
CH_NAME = "Introduction to Linear Polynomials"

# ==============================================================================
# SUBTOPIC 2.2.1: Evaluating p(k) for given value k
# ==============================================================================
def gen_2_2_1():
    tc = "CBSE-9-MGM-2-2.2.1"
    tname = "Evaluating p(k) for given value k"

    # Arch 0: Direct evaluation of p(x) = ax + b at integer k
    arch0 = {
        'data': [
            (3, 4, 2, 10), (5, -7, 3, 8), (-4, 9, 2, 1), (-2, -5, -3, 1),
            (6, 1, -2, -11), (7, -12, 0, -12), (-3, 8, -4, 20), (4, -15, 5, 5),
            (-5, 6, 1, 1), (8, -3, -1, -11)
        ],
        'tmpls': [
            "If \\( p(x) = {0}x + ({1}) \\), find the value of \\( p({2}) \\).",
            "Evaluate the linear polynomial \\( p(x) = {0}x + ({1}) \\) at \\( x = {2} \\).",
            "What is the value of \\( p({2}) \\) for the polynomial \\( p(x) = {0}x + ({1}) \\)?",
            "Calculate \\( p({2}) \\) when \\( p(x) = {0}x + ({1}) \\).",
            "For \\( p(x) = {0}x + ({1}) \\), determine the value of \\( p({2}) \\):",
            "Find the numerical value of \\( {0}x + ({1}) \\) when \\( x = {2} \\):",
            "Substitute \\( x = {2} \\) into \\( p(x) = {0}x + ({1}) \\) to find \\( p({2}) \\):",
            "Compute the value of the polynomial \\( p(x) = {0}x + ({1}) \\) at \\( x = {2} \\):",
            "The value of \\( p(x) = {0}x + ({1}) \\) at \\( x = {2} \\) equals:",
            "Determine \\( p({2}) \\) given \\( p(x) = {0}x + ({1}) \\):"
        ],
        'calc': lambda item: (
            str(item[3]),
            [str(item[3] + 2), str(item[3] - 3), str(-item[3])],
            f"**Step 1: Substitute the given value \\( x = {item[2]} \\) into \\( p(x) \\).**\n\\[ p({item[2]}) = {item[0]}({item[2]}) + ({item[1]}) \\]\n\n**Step 2: Carry out multiplication and addition.**\n\\[ p({item[2]}) = {item[0] * item[2]} + ({item[1]}) = {item[3]} \\]\n\n**Step 3: State the final value.**\nThe value of \\( p({item[2]}) \\) is \\( {item[3]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Evaluating at fractional or rational values
    arch1 = {
        'data': [
            (6, -5, "1/2", -2), (4, 7, "-1/2", 5), (9, -2, "2/3", 4), (8, 3, "-3/4", -3),
            (10, -7, "3/5", -1), (12, 5, "-1/3", 1), (15, -4, "1/5", -1), (6, 9, "-2/3", 5),
            (14, -8, "3/7", -2), (16, 1, "-1/4", -3)
        ],
        'tmpls': [
            "If \\( p(x) = {0}x + ({1}) \\), find the value of \\( p({2}) \\).",
            "Evaluate \\( p(x) = {0}x + ({1}) \\) at \\( x = {2} \\).",
            "Calculate the value of \\( p({2}) \\) for the polynomial \\( p(x) = {0}x + ({1}) \\):",
            "What is the result when \\( x = {2} \\) is substituted into \\( p(x) = {0}x + ({1}) \\)?",
            "Determine the value of \\( p({2}) \\) where \\( p(x) = {0}x + ({1}) \\):",
            "Compute \\( p({2}) \\) given the linear polynomial \\( p(x) = {0}x + ({1}) \\):",
            "Find the value of \\( {0}x + ({1}) \\) when \\( x = {2} \\):",
            "The evaluation of \\( p(x) = {0}x + ({1}) \\) at \\( x = {2} \\) yields:",
            "Calculate \\( p({2}) \\) for \\( p(x) = {0}x + ({1}) \\):",
            "Find \\( p({2}) \\) when \\( p(x) = {0}x + ({1}) \\):"
        ],
        'calc': lambda item: (
            str(item[3]),
            [str(item[3] + 1), str(item[3] - 2), str(-item[3])],
            f"**Step 1: Substitute the fraction \\( x = {item[2]} \\) into \\( p(x) \\).**\n\\[ p\\left({item[2]}\\right) = {item[0]}\\left({item[2]}\\right) + ({item[1]}) \\]\n\n**Step 2: Simplify the fraction arithmetic.**\nMultiply the coefficient by the fraction and add the constant term.\n\n**Step 3: State the final evaluated integer.**\n\\( p\\left({item[2]}\\right) = {item[3]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Expression combinations: p(a) + p(b) or p(a) - p(b)
    arch2 = {
        'data': [
            (2, 3, 1, -1, 6), (3, -4, 2, 0, -2), (4, 1, 1, 2, 14), (5, -2, 2, -1, 1),
            (-2, 7, 3, 1, 6), (3, 5, 2, -2, 10), (4, -3, 3, 1, 10), (-3, 4, 2, -2, 8),
            (2, -5, 4, 1, 0), (6, 2, 1, -1, 4)
        ],
        'tmpls': [
            "If \\( p(x) = {0}x + ({1}) \\), find the value of \\( p({2}) + p({3}) \\).",
            "For the polynomial \\( p(x) = {0}x + ({1}) \\), evaluate \\( p({2}) + p({3}) \\).",
            "Calculate \\( p({2}) + p({3}) \\) given \\( p(x) = {0}x + ({1}) \\):",
            "What is the sum \\( p({2}) + p({3}) \\) for \\( p(x) = {0}x + ({1}) \\)?",
            "Determine the value of \\( p({2}) + p({3}) \\) where \\( p(x) = {0}x + ({1}) \\):",
            "Find the sum of values \\( p({2}) \\) and \\( p({3}) \\) for \\( p(x) = {0}x + ({1}) \\):",
            "Compute \\( p({2}) + p({3}) \\) when \\( p(x) = {0}x + ({1}) \\):",
            "If \\( p(x) = {0}x + ({1}) \\), the expression \\( p({2}) + p({3}) \\) equals:",
            "Evaluate the sum \\( p({2}) + p({3}) \\) for the polynomial \\( p(x) = {0}x + ({1}) \\):",
            "Calculate the total \\( p({2}) + p({3}) \\) given \\( p(x) = {0}x + ({1}) \\):"
        ],
        'calc': lambda item: (
            str(item[4]),
            [str(item[4] + 2), str(item[4] - 2), str(-item[4])],
            f"**Step 1: Evaluate \\( p({item[2]}) \\).**\n\\( p({item[2]}) = {item[0]}({item[2]}) + ({item[1]}) = {item[0] * item[2] + item[1]} \\).\n\n**Step 2: Evaluate \\( p({item[3]}) \\).**\n\\( p({item[3]}) = {item[0]}({item[3]}) + ({item[1]}) = {item[0] * item[3] + item[1]} \\).\n\n**Step 3: Compute the sum.**\n\\( p({item[2]}) + p({item[3]}) = ({item[0] * item[2] + item[1]}) + ({item[0] * item[3] + item[1]}) = {item[4]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Solving for unknown constant k given p(c) = value
    arch3 = {
        'data': [
            (3, 'k', 2, 11, 5), (4, 'k', -1, 3, 7), (2, 'k', 5, 14, 4), (5, 'k', -2, -15, -5),
            (-3, 'k', 4, -7, 5), (-2, 'k', -3, 10, 4), (6, 'k', 1, 2, -4), (7, 'k', 2, 20, 6),
            (-4, 'k', -2, 11, 3), (3, 'k', -3, -13, -4)
        ],
        'tmpls': [
            "If \\( p(x) = {0}x + k \\) and \\( p({2}) = {3} \\), find the value of \\( k \\).",
            "Given \\( p(x) = {0}x + k \\), for what value of \\( k \\) is \\( p({2}) = {3} \\)?",
            "Find \\( k \\) if the polynomial \\( p(x) = {0}x + k \\) satisfies \\( p({2}) = {3} \\).",
            "Determine the value of \\( k \\) such that \\( p({2}) = {3} \\) for \\( p(x) = {0}x + k \\):",
            "The polynomial \\( p(x) = {0}x + k \\) takes the value \\( {3} \\) at \\( x = {2} \\). Find \\( k \\):",
            "Solve for \\( k \\) given that \\( p(x) = {0}x + k \\) and \\( p({2}) = {3} \\):",
            "If \\( p({2}) = {3} \\) for \\( p(x) = {0}x + k \\), then \\( k \\) equals:",
            "What must be the value of \\( k \\) if \\( p(x) = {0}x + k \\) evaluates to \\( {3} \\) at \\( x = {2} \\)?",
            "Calculate \\( k \\) from the equation \\( p({2}) = {3} \\) where \\( p(x) = {0}x + k \\):",
            "Find the constant \\( k \\) if \\( p(x) = {0}x + k \\) and \\( p({2}) = {3} \\):"
        ],
        'calc': lambda item: (
            str(item[4]),
            [str(item[4] + 1), str(-item[4]), str(item[4] - 2)],
            f"**Step 1: Set up the equation from \\( p({item[2]}) = {item[3]} \\).**\n\\[ {item[0]}({item[2]}) + k = {item[3]} \\]\n\n**Step 2: Solve for \\( k \\).**\n\\[ {item[0] * item[2]} + k = {item[3]} \\implies k = {item[3]} - ({item[0] * item[2]}) = {item[4]} \\]\n\n**Step 3: State the value of \\( k \\).**\n\\( k = {item[4]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Verifying whether x = c is a zero of p(x)
    arch4 = {
        'data': [
            (2, -6, 3, True), (3, -12, 4, True), (4, -8, 3, False), (5, 10, -2, True),
            (-3, 9, 3, True), (2, 5, -2, False), (-4, -16, -4, True), (6, -18, 2, False),
            (7, -21, 3, True), (3, 6, 2, False)
        ],
        'tmpls': [
            "Is \\( x = {2} \\) a zero of the polynomial \\( p(x) = {0}x + ({1}) \\)?",
            "Check whether \\( x = {2} \\) is a zero of \\( p(x) = {0}x + ({1}) \\).",
            "Determine if \\( {2} \\) is a root/zero of the linear polynomial \\( p(x) = {0}x + ({1}) \\):",
            "Does \\( x = {2} \\) satisfy \\( p(x) = 0 \\) for \\( p(x) = {0}x + ({1}) \\)?",
            "Verify whether \\( x = {2} \\) is a zero of \\( p(x) = {0}x + ({1}) \\):",
            "Is the number \\( {2} \\) a zero of the polynomial \\( p(x) = {0}x + ({1}) \\)?",
            "Test if \\( x = {2} \\) is a zero of \\( p(x) = {0}x + ({1}) \\):",
            "Does the polynomial \\( p(x) = {0}x + ({1}) \\) become zero when \\( x = {2} \\)?",
            "Is \\( {2} \\) a zero of \\( p(x) = {0}x + ({1}) \\)?",
            "Confirm whether \\( x = {2} \\) is a zero of \\( p(x) = {0}x + ({1}) \\):"
        ],
        'calc': lambda item: (
            "Yes, it is a zero" if item[3] else "No, it is not a zero",
            [
                "No, it is not a zero" if item[3] else "Yes, it is a zero",
                "It is a complex zero",
                "Cannot be determined"
            ],
            f"**Step 1: Evaluate \\( p({item[2]}) \\).**\n\\[ p({item[2]}) = {item[0]}({item[2]}) + ({item[1]}) = {item[0] * item[2] + item[1]} \\]\n\n**Step 2: Check if \\( p({item[2]}) = 0 \\).**\nSince \\( p({item[2]}) {'= 0' if item[3] else '\\neq 0'} \\), \\( x = {item[2]} \\) {'is' if item[3] else 'is not'} a zero.\n\n**Step 3: State the conclusion.**\n{'Yes, it is a zero' if item[3] else 'No, it is not a zero'}."
        ),
        'diff': 'easy'
    }

    # Arch 5: Difference quotient / rate of change: (p(b) - p(a)) / (b - a)
    arch5 = {
        'data': [
            (4, 7, 1, 3, 4), (5, -3, 2, 6, 5), (-3, 8, 1, 4, -3), (-2, -5, 0, 5, -2),
            (6, 11, -1, 3, 6), (7, 2, 2, 5, 7), (-5, 1, -2, 2, -5), (8, -9, 3, 7, 8),
            (-4, 6, -3, 1, -4), (9, -2, 1, 4, 9)
        ],
        'tmpls': [
            "For the linear polynomial \\( p(x) = {0}x + ({1}) \\), find the value of \\( \\frac{{p({3}) - p({2})}}{{{3} - ({2})}} \\).",
            "Calculate the rate of change \\( \\frac{{p({3}) - p({2})}}{{{3} - {2}}} \\) for \\( p(x) = {0}x + ({1}) \\).",
            "What is the value of the difference quotient \\( \\frac{{p({3}) - p({2})}}{{{3} - {2}}} \\) when \\( p(x) = {0}x + ({1}) \\)?",
            "Determine \\( \\frac{{p({3}) - p({2})}}{{{3} - ({2})}} \\) for the linear polynomial \\( p(x) = {0}x + ({1}) \\):",
            "Evaluate \\( \\frac{{p({3}) - p({2})}}{{{3} - {2}}} \\) given \\( p(x) = {0}x + ({1}) \\):",
            "For \\( p(x) = {0}x + ({1}) \\), the value of \\( \\frac{{p({3}) - p({2})}}{{{3} - {2}}} \\) is:",
            "Find the quotient \\( \\frac{{p({3}) - p({2})}}{{{3} - {2}}} \\) where \\( p(x) = {0}x + ({1}) \\):",
            "The slope or rate of change \\( \\frac{{p({3}) - p({2})}}{{{3} - {2}}} \\) of \\( p(x) = {0}x + ({1}) \\) is:",
            "Compute \\( \\frac{{p({3}) - p({2})}}{{{3} - {2}}} \\) for the polynomial \\( p(x) = {0}x + ({1}) \\):",
            "Calculate \\( \\frac{{p({3}) - p({2})}}{{{3} - ({2})}} \\) given \\( p(x) = {0}x + ({1}) \\):"
        ],
        'calc': lambda item: (
            str(item[4]),
            [str(item[4] + 1), str(-item[4]), str(item[4] + 2)],
            f"**Step 1: Understand difference quotient for linear polynomials.**\nFor any linear polynomial \\( p(x) = ax + b \\), the rate of change between any two points \\( x = a \\) and \\( x = b \\) is constant and equal to the coefficient \\( a \\).\n\n**Step 2: Verify by explicit computation.**\n- \\( p({item[3]}) = {item[0]}({item[3]}) + ({item[1]}) = {item[0] * item[3] + item[1]} \\)\n- \\( p({item[2]}) = {item[0]}({item[2]}) + ({item[1]}) = {item[0] * item[2] + item[1]} \\)\n- \\( p({item[3]}) - p({item[2]}) = {item[0] * (item[3] - item[2])} \\)\n- Dividing by \\( ({item[3]} - {item[2]}) = {item[3] - item[2]} \\) yields \\( {item[4]} \\).\n\n**Step 3: State the result.**\nThe value is \\( {item[4]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 6: Comparing values of two polynomials at a given point
    arch6 = {
        'data': [
            ("p(x) = 3x + 4", "q(x) = 2x + 7", 3, "Both are equal (p(3) = q(3) = 13)"),
            ("p(x) = 4x - 1", "q(x) = 5x - 5", 4, "p(4) = 15 is equal to q(4) = 15"),
            ("p(x) = 2x + 8", "q(x) = 3x + 2", 5, "p(5) = 18 is greater than q(5) = 17"),
            ("p(x) = 5x - 6", "q(x) = 4x + 1", 2, "p(2) = 4 is less than q(2) = 9"),
            ("p(x) = -2x + 10", "q(x) = x + 1", 3, "Both are equal (p(3) = q(3) = 4)"),
            ("p(x) = 6x - 5", "q(x) = 7x - 9", 4, "Both are equal (p(4) = q(4) = 19)"),
            ("p(x) = 3x + 2", "q(x) = 2x + 9", 2, "p(2) = 8 is less than q(2) = 13"),
            ("p(x) = 4x + 5", "q(x) = 3x + 10", 6, "p(6) = 29 is greater than q(6) = 28"),
            ("p(x) = -x + 12", "q(x) = 2x + 3", 3, "Both are equal (p(3) = q(3) = 9)"),
            ("p(x) = 5x + 3", "q(x) = 6x - 1", 4, "Both are equal (p(4) = q(4) = 23)")
        ],
        'tmpls': [
            "Compare the values of \\( {0} \\) and \\( {1} \\) at \\( x = {2} \\).",
            "At \\( x = {2} \\), which relationship holds between \\( {0} \\) and \\( {1} \\)?",
            "Evaluate both \\( {0} \\) and \\( {1} \\) at \\( x = {2} \\) and compare their values:",
            "How do \\( {0} \\) and \\( {1} \\) compare when \\( x = {2} \\)?",
            "Determine the comparison between \\( {0} \\) and \\( {1} \\) at point \\( x = {2} \\):",
            "Find whether \\( p({2}) \\) is greater, smaller, or equal to \\( q({2}) \\) for \\( {0} \\) and \\( {1} \\):",
            "At \\( x = {2} \\), the values of \\( {0} \\) and \\( {1} \\) satisfy:",
            "Which statement correctly compares \\( {0} \\) and \\( {1} \\) at \\( x = {2} \\)?",
            "Compute and compare \\( p({2}) \\) and \\( q({2}) \\) given \\( {0} \\) and \\( {1} \\):",
            "For \\( {0} \\) and \\( {1} \\), what is the relationship between \\( p({2}) \\) and \\( q({2}) \\)?"
        ],
        'calc': lambda item: (
            item[3],
            [
                "p(x) is always twice q(x)",
                "p(x) and q(x) have opposite signs",
                "Cannot be determined without coefficients"
            ],
            f"**Step 1: Evaluate p({item[2]}).**\nSubstitute \\( x = {item[2]} \\) into the first polynomial.\n\n**Step 2: Evaluate q({item[2]}).**\nSubstitute \\( x = {item[2]} \\) into the second polynomial.\n\n**Step 3: Compare the numerical values.**\n{item[3]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Linear polynomial modeling and evaluation in real-world contexts
    arch7 = {
        'data': [
            ("A taxi charges p(x) = 15x + 30 for x km. What is the fare for a trip of 12 km?", "₹210", ["₹180", "₹240", "₹195"]),
            ("The height of a growing bamboo in cm is H(d) = 8d + 15 where d is days. What is its height after 10 days?", "95 cm", ["80 cm", "105 cm", "85 cm"]),
            ("A printing company charges C(n) = 3n + 250 for printing n brochures. What is the cost for 150 brochures?", "₹700", ["₹650", "₹750", "₹450"]),
            ("Water is draining from a pool according to V(t) = -25t + 800 liters, where t is minutes. What is the volume after 20 minutes?", "300 liters", ["500 liters", "250 liters", "400 liters"]),
            ("The temperature of a heated metal rod cools as T(m) = -4m + 120 °C after m minutes. What is its temperature after 15 minutes?", "60 °C", ["80 °C", "40 °C", "50 °C"]),
            ("A mobile plan costs B(g) = 50g + 199 for g gigabytes of extra data. What is the bill for 4 extra GB?", "₹399", ["₹349", "₹449", "₹299"]),
            ("Total cost of producing x units is C(x) = 45x + 1200. What is the total cost for 40 units?", "₹3000", ["₹2800", "₹3200", "₹2600"]),
            ("A car's fuel tank has F(d) = -0.08d + 50 liters after traveling d km. How much fuel remains after 250 km?", "30 liters", ["20 liters", "25 liters", "35 liters"]),
            ("A salesperson earns S(n) = 120n + 5000 for selling n appliances. What are their earnings for selling 25 appliances?", "₹8000", ["₹7500", "₹8500", "₹7000"]),
            ("The speed of an accelerating particle is v(t) = 6t + 14 m/s. What is its speed at t = 5 seconds?", "44 m/s", ["30 m/s", "40 m/s", "54 m/s"])
        ],
        'tmpls': [
            "{0}",
            "Solve the following applied polynomial problem: {0}",
            "In practical mathematics: {0}",
            "Calculate the required value: {0}",
            "Evaluate the polynomial in this application: {0}",
            "Real-world polynomial question: {0}",
            "Determine the result: {0}",
            "Find the answer to the word problem: {0}",
            "Solve this applied linear model problem: {0}",
            "Compute the required quantity: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify the linear polynomial function and input variable.**\nFrom the problem statement: '{item[0]}'.\n\n**Step 2: Substitute the given value.**\nPerform the algebraic evaluation \\( p(k) = ak + b \\).\n\n**Step 3: State the final evaluated result.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 2.2.2: Finding zero of linear polynomial ax + b algebraically
# ==============================================================================
def gen_2_2_2():
    tc = "CBSE-9-MGM-2-2.2.2"
    tname = "Finding zero of linear polynomial ax + b algebraically"

    # Arch 0: Finding zero of ax + b with integer zero
    arch0 = {
        'data': [
            (2, -8, 4), (3, -15, 5), (4, -28, 7), (5, 35, -7), (6, -18, 3),
            (-3, 12, 4), (-4, -20, -5), (7, 42, -6), (8, -32, 4), (-5, -45, -9)
        ],
        'tmpls': [
            "Find the zero of the linear polynomial \\( p(x) = {0}x + ({1}) \\).",
            "What is the zero of the polynomial \\( p(x) = {0}x + ({1}) \\)?",
            "Calculate the zero of the polynomial \\( {0}x + ({1}) \\).",
            "Determine the zero of \\( p(x) = {0}x + ({1}) \\):",
            "For what value of \\( x \\) does the polynomial \\( p(x) = {0}x + ({1}) \\) equal zero?",
            "Find the root of the polynomial equation \\( {0}x + ({1}) = 0 \\):",
            "The zero of the linear polynomial \\( {0}x + ({1}) \\) is:",
            "Solve for the zero of \\( p(x) = {0}x + ({1}) \\):",
            "At which value of \\( x \\) is \\( p(x) = {0}x + ({1}) \\) zero?",
            "Identify the zero of the polynomial \\( p(x) = {0}x + ({1}) \\):"
        ],
        'calc': lambda item: (
            str(item[2]),
            [str(-item[2]), str(item[2] + 1), str(item[2] - 2)],
            f"**Step 1: Set \\( p(x) = 0 \\).**\n\\[ {item[0]}x + ({item[1]}) = 0 \\]\n\n**Step 2: Solve for \\( x \\).**\n\\[ {item[0]}x = -({item[1]}) \\implies x = \\frac{{-({item[1]})}}{{{item[0]}}} = {item[2]} \\]\n\n**Step 3: State the zero.**\nThe zero of the polynomial is \\( {item[2]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Finding zero of ax + b with fractional zero (-b/a)
    arch1 = {
        'data': [
            (2, 5, "-\\frac{5}{2}"), (3, -7, "\\frac{7}{3}"), (4, 9, "-\\frac{9}{4}"), (5, -3, "\\frac{3}{5}"),
            (6, 11, "-\\frac{11}{6}"), (7, -4, "\\frac{4}{7}"), (8, 5, "-\\frac{5}{8}"), (9, -2, "\\frac{2}{9}"),
            (10, 7, "-\\frac{7}{10}"), (3, 8, "-\\frac{8}{3}")
        ],
        'tmpls': [
            "Find the zero of the linear polynomial \\( p(x) = {0}x + ({1}) \\).",
            "What is the zero of the polynomial \\( p(x) = {0}x + ({1}) \\)?",
            "Calculate the zero of \\( p(x) = {0}x + ({1}) \\):",
            "Determine the zero of the linear polynomial \\( {0}x + ({1}) \\):",
            "For what value of \\( x \\) is \\( p(x) = {0}x + ({1}) \\) equal to 0?",
            "The zero of \\( p(x) = {0}x + ({1}) \\) is given by:",
            "Solve for the zero of the linear polynomial \\( {0}x + ({1}) \\):",
            "At what point \\( x \\) does \\( p(x) = {0}x + ({1}) \\) become zero?",
            "Find the root of \\( {0}x + ({1}) = 0 \\):",
            "Identify the zero of \\( p(x) = {0}x + ({1}) \\):"
        ],
        'calc': lambda item: (
            item[2],
            [
                item[2].replace("-", "") if "-" in item[2] else f"-{item[2]}",
                f"\\frac{{{item[0]}}}{{{abs(item[1])}}}",
                "0"
            ],
            f"**Step 1: Set the linear polynomial equal to zero.**\n\\[ {item[0]}x + ({item[1]}) = 0 \\]\n\n**Step 2: Transpose the constant and divide by the coefficient.**\n\\[ {item[0]}x = -({item[1]}) \\implies x = -\\frac{{{item[1]}}}{{{item[0]}}} = {item[2]} \\]\n\n**Step 3: State the fractional zero.**\nThe zero of the polynomial is \\( {item[2]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Zero of monomial linear polynomial p(x) = ax (where zero is strictly 0)
    arch2 = {
        'data': [
            ("5x", 0), ("-7x", 0), ("\\frac{3}{4}x", 0), ("-\\frac{2}{5}x", 0),
            ("\\sqrt{2}x", 0), ("12x", 0), ("-x", 0), ("\\pi x", 0),
            ("100x", 0), ("-\\sqrt{5}x", 0)
        ],
        'tmpls': [
            "What is the zero of the monomial polynomial \\( p(x) = {0} \\)?",
            "Find the zero of \\( p(x) = {0} \\).",
            "The zero of the linear monomial \\( {0} \\) is:",
            "Determine the zero of the polynomial \\( p(x) = {0} \\):",
            "For what value of \\( x \\) does \\( {0} = 0 \\)?",
            "Calculate the zero of \\( p(x) = {0} \\):",
            "At which value of \\( x \\) is the polynomial \\( {0} \\) equal to zero?",
            "Identify the root of \\( {0} = 0 \\):",
            "Solve for the zero of \\( {0} \\):",
            "State the zero of the linear polynomial \\( p(x) = {0} \\):"
        ],
        'calc': lambda item: (
            str(item[1]),
            ["1", "-1", "undefined"],
            f"**Step 1: Set the polynomial equal to zero.**\n\\[ {item[0]} = 0 \\]\n\n**Step 2: Divide both sides by the non-zero coefficient.**\nSince the coefficient is non-zero, dividing 0 by any non-zero real number yields 0:\n\\[ x = \\frac{{0}}{{\\text{{coefficient}}}} = 0 \\]\n\n**Step 3: State the zero.**\nThe zero is \\( 0 \\)."
        ),
        'diff': 'easy'
    }

    # Arch 3: Theoretical properties of zeroes of linear polynomials
    arch3 = {
        'data': [
            ("number of zeroes a linear polynomial can have", "exactly 1 real zero", ["0 zeroes", "2 zeroes", "infinitely many"]),
            ("zero of the linear polynomial ax + b (where a ≠ 0)", "-b/a", ["b/a", "-a/b", "a/b"]),
            ("number of zeroes of a non-zero constant polynomial c", "0 zeroes (no zero)", ["1 zero", "c zeroes", "infinitely many"]),
            ("number of zeroes of the zero polynomial 0", "infinitely many (every real number is a zero)", ["0 zeroes", "1 zero", "not defined"]),
            ("can a zero of a polynomial be zero itself?", "Yes, 0 can be a zero of a polynomial", ["No, a zero can never be zero", "Only for quadratic polynomials", "Only for constant polynomials"]),
            ("geometrically, the zero of a linear polynomial y = ax + b represents", "the x-intercept of the line", ["the y-intercept of the line", "the slope of the line", "the origin"]),
            ("if c is a zero of p(x), then (x - c) is", "a factor of p(x)", ["the remainder", "the quotient", "the degree"]),
            ("the zero of p(x) = x - c is", "c", ["-c", "0", "1/c"]),
            ("the zero of p(x) = x + c is", "-c", ["c", "0", "-1/c"]),
            ("a polynomial of degree n can have at most", "n zeroes", ["n + 1 zeroes", "2n zeroes", "infinitely many zeroes"])
        ],
        'tmpls': [
            "What is the {0}?",
            "In polynomial algebra, {0} is:",
            "Identify the correct mathematical fact: {0}:",
            "Which statement correctly gives the {0}?",
            "Determine the {0}:",
            "According to the fundamental theorem of algebra, {0}:",
            "What can be stated regarding the {0}?",
            "State the {0}:",
            "Select the true statement regarding {0}:",
            "Which of the following describes the {0}?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the theoretical definition of polynomial zeroes.**\nConsider the property '{item[0]}'.\n\n**Step 2: Apply the algebraic rule.**\nFor a linear polynomial \\( ax + b \\), equating to zero gives \\( ax = -b \\implies x = -b/a \\).\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Solving for parameter k when zero is given
    arch4 = {
        'data': [
            ("2x - k", 3, 6), ("3x + k", -4, 12), ("4x - k", 5, 20), ("5x + 2k", -2, 5),
            ("6x - 3k", 2, 4), ("-3x + k", 4, 12), ("-2x - k", -5, 10), ("7x - k", 3, 21),
            ("4x + 3k", -3, 4), ("8x - 2k", 2, 8)
        ],
        'tmpls': [
            "If \\( x = {1} \\) is a zero of the polynomial \\( p(x) = {0} \\), find the value of \\( k \\).",
            "The polynomial \\( p(x) = {0} \\) has \\( x = {1} \\) as its zero. What is the value of \\( k \\)?",
            "Given that \\( {1} \\) is a root of \\( p(x) = {0} \\), calculate \\( k \\):",
            "Find the value of \\( k \\) if \\( x = {1} \\) is a zero of \\( {0} \\):",
            "Determine \\( k \\) such that \\( p({1}) = 0 \\) for \\( p(x) = {0} \\):",
            "For what value of \\( k \\) does the polynomial \\( {0} \\) have zero at \\( x = {1} \\)?",
            "If \\( p({1}) = 0 \\) for the linear polynomial \\( {0} \\), then \\( k \\) equals:",
            "Calculate the unknown \\( k \\) given that \\( {1} \\) is a zero of \\( {0} \\):",
            "Find \\( k \\) when \\( x = {1} \\) makes \\( {0} \\) equal to zero:",
            "Solve for \\( k \\) given that \\( x = {1} \\) is a zero of \\( p(x) = {0} \\):"
        ],
        'calc': lambda item: (
            str(item[2]),
            [str(item[2] + 2), str(-item[2]), str(item[2] - 3)],
            f"**Step 1: Apply definition of a zero.**\nSince \\( x = {item[1]} \\) is a zero, substituting \\( x = {item[1]} \\) makes the polynomial zero.\n\n**Step 2: Set up the linear equation in \\( k \\).**\nSubstitute \\( x = {item[1]} \\) into \\( {item[0]} = 0 \\) and solve for \\( k \\).\n\n**Step 3: State the value of \\( k \\).**\n\\( k = {item[2]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 5: Common zeroes / Equating two linear polynomials p(x) = q(x)
    arch5 = {
        'data': [
            ("3x - 4", "x + 6", 5), ("4x + 1", "2x + 9", 4), ("5x - 7", "2x + 8", 5),
            ("6x + 2", "3x + 11", 3), ("7x - 5", "4x + 10", 5), ("2x + 12", "-x + 3", -3),
            ("3x - 8", "-2x + 7", 3), ("4x + 3", "x - 9", -4), ("5x - 1", "3x + 7", 4),
            ("6x - 10", "x + 15", 5)
        ],
        'tmpls': [
            "For what value of \\( x \\) are the two linear polynomials \\( p(x) = {0} \\) and \\( q(x) = {1} \\) equal?",
            "Find the value of \\( x \\) where \\( {0} = {1} \\).",
            "At which value of \\( x \\) do the polynomials \\( p(x) = {0} \\) and \\( q(x) = {1} \\) take the same value?",
            "Solve for \\( x \\) such that \\( p(x) = q(x) \\) for \\( p(x) = {0} \\) and \\( q(x) = {1} \\):",
            "The graphs of \\( y = {0} \\) and \\( y = {1} \\) intersect at an x-coordinate of:",
            "Determine the point of equality \\( x \\) for \\( {0} \\) and \\( {1} \\):",
            "Calculate \\( x \\) if \\( {0} \\) equals \\( {1} \\):",
            "Find the common value of \\( x \\) satisfying \\( {0} = {1} \\):",
            "For what \\( x \\) is \\( p(x) - q(x) = 0 \\) given \\( p(x) = {0} \\) and \\( q(x) = {1} \\)?",
            "The root of the equation \\( {0} = {1} \\) is:"
        ],
        'calc': lambda item: (
            str(item[2]),
            [str(item[2] + 1), str(-item[2]), str(item[2] - 2)],
            f"**Step 1: Set the two polynomials equal to each other.**\n\\[ {item[0]} = {item[1]} \\]\n\n**Step 2: Collect like terms.**\nMove all \\( x \\)-terms to one side and constants to the other side.\n\n**Step 3: Solve for \\( x \\).**\n\\( x = {item[2]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 6: Sum and difference of zeroes
    arch6 = {
        'data': [
            ("2x - 6", "3x - 12", 3, 4, 7),
            ("4x - 8", "5x + 15", 2, -3, -1),
            ("3x + 9", "2x - 8", -3, 4, 1),
            ("5x - 20", "4x - 24", 4, 6, 10),
            ("6x + 18", "3x - 15", -3, 5, 2),
            ("2x + 10", "7x - 28", -5, 4, -1),
            ("4x - 16", "2x + 8", 4, -4, 0),
            ("3x - 21", "5x - 10", 7, 2, 9),
            ("8x - 24", "4x + 20", 3, -5, -2),
            ("5x + 25", "6x - 18", -5, 3, -2)
        ],
        'tmpls': [
            "If \\( \\alpha \\) is the zero of \\( p(x) = {0} \\) and \\( \\beta \\) is the zero of \\( q(x) = {1} \\), what is the sum \\( \\alpha + \\beta \\)?",
            "Find the sum of the zeroes of the two polynomials \\( p(x) = {0} \\) and \\( q(x) = {1} \\).",
            "Calculate \\( \\alpha + \\beta \\) where \\( \\alpha \\) is the root of \\( {0} = 0 \\) and \\( \\beta \\) is the root of \\( {1} = 0 \\):",
            "What is the sum of the zeroes of \\( {0} \\) and \\( {1} \\)?",
            "Determine \\( \\alpha + \\beta \\) given that \\( p(\\alpha) = 0 \\) for \\( p(x) = {0} \\) and \\( q(\\beta) = 0 \\) for \\( q(x) = {1} \\):",
            "The sum of the roots of \\( {0} = 0 \\) and \\( {1} = 0 \\) is:",
            "Find \\( \\alpha + \\beta \\) for the zeroes of \\( {0} \\) and \\( {1} \\):",
            "Compute the sum of the zeroes of \\( p(x) = {0} \\) and \\( q(x) = {1} \\):",
            "If \\( \\alpha \\) and \\( \\beta \\) are the respective zeroes of \\( {0} \\) and \\( {1} \\), then \\( \\alpha + \\beta = \\):",
            "Calculate the total of the zeroes of \\( {0} \\) and \\( {1} \\):"
        ],
        'calc': lambda item: (
            str(item[4]),
            [str(item[4] + 2), str(-item[4]), str(item[4] - 2)],
            f"**Step 1: Find the zero \\( \\alpha \\) of \\( p(x) = {item[0]} \\).**\n\\[ {item[0]} = 0 \\implies \\alpha = {item[2]} \\]\n\n**Step 2: Find the zero \\( \\beta \\) of \\( q(x) = {item[1]} \\).**\n\\[ {item[1]} = 0 \\implies \\beta = {item[3]} \\]\n\n**Step 3: Sum the zeroes.**\n\\[ \\alpha + \\beta = {item[2]} + ({item[3]}) = {item[4]} \\]"
        ),
        'diff': 'hard'
    }

    # Arch 7: Real-world break-even point / Zero value problems
    arch7 = {
        'data': [
            ("A company's profit polynomial is P(x) = 25x - 500 in rupees for x items. How many items must be sold to break even (zero profit)?", "20 items", ["15 items", "25 items", "50 items"]),
            ("The temperature of a cooling liquid is T(t) = -3t + 45 °C after t minutes. After how many minutes does it reach freezing point (0 °C)?", "15 minutes", ["12 minutes", "18 minutes", "20 minutes"]),
            ("Water drains from a 600-liter tank at 40 liters/minute as V(t) = -40t + 600. When is the tank completely empty?", "15 minutes", ["12 minutes", "20 minutes", "10 minutes"]),
            ("An altitude descent of an aircraft is modeled by h(t) = -200t + 3000 meters. How many minutes until it touches down (h = 0)?", "15 minutes", ["10 minutes", "20 minutes", "30 minutes"]),
            ("A bank loan balance in thousands is B(m) = -5m + 60 after m months. In how many months will the loan be fully repaid (B = 0)?", "12 months", ["10 months", "15 months", "20 months"]),
            ("A battery drains according to charge Q(h) = -8h + 96 mAh. After how many hours is the battery completely discharged?", "12 hours", ["10 hours", "14 hours", "16 hours"]),
            ("The height of an object descending on a parachute is y(t) = -5t + 80 meters. When does it reach the ground?", "16 seconds", ["12 seconds", "15 seconds", "20 seconds"]),
            ("Profit from selling tickets is P(t) = 50t - 2500. How many tickets must be sold to reach the break-even zero profit point?", "50 tickets", ["40 tickets", "60 tickets", "25 tickets"]),
            ("A candle of height 30 cm burns down at 2 cm/hour: H(t) = -2t + 30. How long will the candle burn until completely consumed?", "15 hours", ["12 hours", "18 hours", "20 hours"]),
            ("Fuel in a generator decreases as F(h) = -4h + 48 liters. After how many hours of operation will the fuel run out?", "12 hours", ["10 hours", "14 hours", "16 hours"])
        ],
        'tmpls': [
            "{0}",
            "Solve the following applied zero-finding problem: {0}",
            "In practical linear modeling: {0}",
            "Calculate the time or quantity when the polynomial equals zero: {0}",
            "Find the break-even / zero root: {0}",
            "Applied coordinate and polynomial problem: {0}",
            "Determine the required value: {0}",
            "Solve for the root in this context: {0}",
            "Find the solution to this applied question: {0}",
            "Compute the zero of the practical linear function: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Set the linear model equal to zero.**\nFrom the problem statement: '{item[0]}'. Set the linear function equal to 0.\n\n**Step 2: Solve the linear equation for the variable.**\nTranspose the constant and divide by the rate of change.\n\n**Step 3: State the final calculated value.**\nThe solution is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])

if __name__ == "__main__":
    q1 = gen_2_2_1()
    q2 = gen_2_2_2()
    print(f"gen_2_2_1: {len(q1)} questions generated")
    print(f"gen_2_2_2: {len(q2)} questions generated")
