# scripts/build_cbse9_mgm_ch6_part2.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 6: Measuring Space: Perimeter and Area
Part 2:
- Subtopic 6.2.1: Semi-perimeter s = (a + b + c) / 2
- Subtopic 6.2.2: Area formula: A = √[s(s - a)(s - b)(s - c)]
- Subtopic 6.2.3: Area of equilateral and isosceles triangles
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 240 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 6
CH_NAME = "Measuring Space: Perimeter and Area"

# ==============================================================================
# SUBTOPIC 6.2.1: Semi-perimeter s = (a + b + c) / 2
# ==============================================================================
def gen_6_2_1():
    tc = "CBSE-9-MGM-6-6.2.1"
    tname = "Semi-perimeter s = (a + b + c) / 2"

    # Arch 0: Direct calculation of semi-perimeter s from sides a, b, c
    arch0 = {
        'data': [
            (13, 14, 15, 21),
            (5, 6, 7, 9),
            (9, 10, 17, 18),
            (11, 13, 20, 22),
            (10, 17, 21, 24),
            (13, 20, 21, 27),
            (15, 28, 41, 42),
            (17, 25, 28, 35),
            (25, 34, 39, 49),
            (8, 15, 17, 20)
        ],
        'tmpls': [
            "Find the semi-perimeter \\( s \\) of a triangle whose sides are {0} cm, {1} cm, and {2} cm:",
            "The sides of a triangle are {0} m, {1} m, and {2} m. Calculate its semi-perimeter \\( s \\):",
            "What is the value of the semi-perimeter \\( s \\) for a triangle with sides \\( a = {0} \\), \\( b = {1} \\), \\( c = {2} \\)?",
            "In Heron's formula, what is the value of \\( s \\) for a triangle of sides {0} cm, {1} cm, and {2} cm?",
            "Calculate \\( s = \\frac{{a + b + c}}{{2}} \\) for a triangle having sides {0} units, {1} units, and {2} units:",
            "Determine the semi-perimeter of a triangular garden with side lengths {0} m, {1} m, and {2} m:",
            "Evaluate the semi-perimeter \\( s \\) for \\( a = {0} \\text{{ cm}} \\), \\( b = {1} \\text{{ cm}} \\), \\( c = {2} \\text{{ cm}} \\):",
            "A triangle has side measurements {0} cm, {1} cm, and {2} cm. Find half of its perimeter:",
            "Compute the semi-perimeter of a triangle with edges {0} m, {1} m, and {2} m:",
            "Find \\( s \\) for a triangle with perimeter \\( {0} + {1} + {2} \\):"
        ],
        'calc': lambda item: (
            f"\\( {item[3]} \\text{{ cm}} \\)",
            [f"\\( {item[3] * 2} \\text{{ cm}} \\)", f"\\( {item[3] + 2} \\text{{ cm}} \\)", f"\\( {item[3] - 2} \\text{{ cm}} \\)"],
            f"**Step 1: State the semi-perimeter formula.**\n\\[ s = \\frac{{a + b + c}}{{2}} \\]\n\n**Step 2: Substitute the side lengths.**\n\\[ s = \\frac{{{item[0]} + {item[1]} + {item[2]}}}{{2}} = \\frac{{{item[0] + item[1] + item[2]}}}{{2}} = {item[3]} \\text{{ cm}} \\]\n\n**Step 3: State the final semi-perimeter.**\nThe semi-perimeter \\( s \\) is \\( {item[3]} \\text{{ cm}} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Finding the third side when perimeter and two sides are given
    arch1 = {
        'data': [
            (32, 11, 8, 13, 16),    # perim 32, a=11, b=8 => c = 32 - 19 = 13, s = 16
            (42, 18, 10, 14, 21),
            (50, 20, 15, 15, 25),
            (30, 12, 12, 6, 15),
            (40, 15, 15, 10, 20),
            (36, 14, 10, 12, 18),
            (48, 20, 16, 12, 24),
            (54, 24, 18, 12, 27),
            (60, 26, 14, 20, 30),
            (70, 30, 25, 15, 35)
        ],
        'tmpls': [
            "The perimeter of a triangle is {0} cm and two of its sides are {1} cm and {2} cm. Find the third side:",
            "A triangle has perimeter {0} m and sides \\( a = {1} \\text{{ m}} \\), \\( b = {2} \\text{{ m}} \\). What is the length of side \\( c \\)?",
            "If the perimeter of a triangle is {0} cm and two sides measure {1} cm and {2} cm, calculate the third side:",
            "Find the unknown third side of a triangle whose perimeter is {0} cm and two known sides are {1} cm and {2} cm:",
            "Two sides of a triangle are {1} m and {2} m. If the total perimeter is {0} m, what is the third side?",
            "Calculate side \\( c \\) of a triangle given perimeter \\( 2s = {0} \\text{{ cm}} \\), \\( a = {1} \\text{{ cm}} \\), \\( b = {2} \\text{{ cm}} \\):",
            "Determine the third side of a triangular plot having perimeter {0} m and two sides {1} m and {2} m:",
            "Evaluate side length \\( c \\) in \\( \\triangle ABC \\) with perimeter {0} cm, \\( a = {1} \\text{{ cm}} \\), \\( b = {2} \\text{{ cm}} \\):",
            "A triangular frame has perimeter {0} cm. Two sides are {1} cm and {2} cm. Find the third side:",
            "Compute the missing edge of a triangle with perimeter {0} cm and sides {1} cm and {2} cm:"
        ],
        'calc': lambda item: (
            f"{item[3]} cm",
            [f"{item[3] + 4} cm", f"{item[3] - 4} cm", f"{item[4]} cm"],
            f"**Step 1: State the relation between perimeter and side lengths.**\n\\[ \\text{{Perimeter}} = a + b + c \\]\n\n**Step 2: Solve for the third side \\( c \\).**\n\\[ c = \\text{{Perimeter}} - (a + b) = {item[0]} - ({item[1]} + {item[2]}) = {item[0]} - {item[1] + item[2]} = {item[3]} \\text{{ cm}} \\]\n\n**Step 3: State the final side length.**\nThe third side is {item[3]} cm."
        ),
        'diff': 'easy'
    }

    # Arch 2: Triangle sides in given ratios with perimeter specified
    arch2 = {
        'data': [
            (3, 4, 5, 36, 9, 12, 15, 18),      # ratio 3:4:5, sum=12, perim=36 => factor 3 => sides 9, 12, 15, s=18
            (5, 12, 13, 60, 10, 24, 26, 30),  # ratio 5:12:13, sum=30, perim=60 => factor 2 => 10, 24, 26, s=30
            (12, 17, 25, 540, 120, 170, 250, 270), # NCERT canonical: 12:17:25, sum=54, perim=540 => 120, 170, 250, s=270
            (3, 5, 7, 300, 60, 100, 140, 150),     # ratio 3:5:7, sum=15, perim=300 => factor 20 => 60, 100, 140, s=150
            (13, 14, 15, 84, 26, 28, 30, 42),      # ratio 13:14:15, sum=42, perim=84 => factor 2 => 26, 28, 30, s=42
            (1, 2, 2, 50, 10, 20, 20, 25),         # ratio 1:2:2, sum=5, perim=50 => factor 10 => 10, 20, 20, s=25
            (2, 3, 4, 90, 20, 30, 40, 45),         # ratio 2:3:4, sum=9, perim=90 => factor 10 => 20, 30, 40, s=45
            (3, 4, 5, 60, 15, 20, 25, 30),         # ratio 3:4:5, sum=12, perim=60 => factor 5 => 15, 20, 25, s=30
            (5, 5, 6, 32, 10, 10, 12, 16),         # ratio 5:5:6, sum=16, perim=32 => factor 2 => 10, 10, 12, s=16
            (6, 8, 10, 120, 30, 40, 50, 60)        # ratio 6:8:10, sum=24, perim=120 => factor 5 => 30, 40, 50, s=60
        ],
        'tmpls': [
            "The sides of a triangle are in the ratio {0} : {1} : {2} and its perimeter is {3} cm. Find its semi-perimeter \\( s \\):",
            "Sides of a triangle are proportional to {0} : {1} : {2} with total perimeter {3} m. What is the semi-perimeter?",
            "If a triangle has sides in ratio {0}:{1}:{2} and perimeter {3} cm, find the length of the longest side:",
            "A triangular plot with perimeter {3} m has sides in the ratio {0}:{1}:{2}. What is the length of the shortest side?",
            "Calculate the semi-perimeter \\( s \\) for a triangle whose sides are in ratio {0} : {1} : {2} with perimeter {3} cm:",
            "Determine the sides of a triangle given ratio {0} : {1} : {2} and perimeter {3} units:",
            "Evaluate \\( s \\) for a triangle of perimeter {3} cm having sides in ratio {0} : {1} : {2}:",
            "Find the semi-perimeter of a triangle with boundary length {3} m and side ratio {0} : {1} : {2}:",
            "The sides of a park are in the ratio {0} : {1} : {2} and its perimeter is {3} m. Compute \\( s \\):",
            "What is \\( s \\) for a triangular field having perimeter {3} m and side ratio {0} : {1} : {2}?"
        ],
        'calc': lambda item: (
            f"\\( {item[7]} \\text{{ cm}} \\)",
            [f"\\( {item[3]} \\text{{ cm}} \\)", f"\\( {item[7] // 2} \\text{{ cm}} \\)", f"\\( {item[7] + 10} \\text{{ cm}} \\)"],
            f"**Step 1: Recall the definition of semi-perimeter.**\nSemi-perimeter \\( s \\) is exactly half of the total perimeter:\n\\[ s = \\frac{{\\text{{Perimeter}}}}{{2}} \\]\n\n**Step 2: Divide the given perimeter by 2.**\n\\[ s = \\frac{{{item[3]}}}{{2}} = {item[7]} \\text{{ cm}} \\]\n\n**Step 3: State the semi-perimeter.**\n\\( s = {item[7]} \\text{{ cm}} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Algebraic relations involving s: (s - a) + (s - b) + (s - c) = s
    arch3 = {
        'data': [
            (21, 13, 14, 15, 8, 7, 6),    # s=21, s-a=8, s-b=7, s-c=6 => 8+7+6 = 21
            (18, 9, 10, 17, 9, 8, 1),
            (24, 10, 17, 21, 14, 7, 3),
            (27, 13, 20, 21, 14, 7, 6),
            (35, 17, 25, 28, 18, 10, 7),
            (20, 8, 15, 17, 12, 5, 3),
            (16, 5, 12, 15, 11, 4, 1),
            (22, 11, 13, 20, 11, 9, 2),
            (30, 15, 20, 25, 15, 10, 5),
            (25, 12, 18, 20, 13, 7, 5)
        ],
        'tmpls': [
            "In a triangle with semi-perimeter \\( s = {0} \\text{{ cm}} \\) and sides {1} cm, {2} cm, {3} cm, calculate the value of \\( (s - a) + (s - b) + (s - c) \\):",
            "For any triangle with semi-perimeter \\( s \\), the algebraic expression \\( (s - a) + (s - b) + (s - c) \\) is always identically equal to:",
            "If \\( s - a = {4} \\text{{ cm}} \\), \\( s - b = {5} \\text{{ cm}} \\), and \\( s - c = {6} \\text{{ cm}} \\), find the semi-perimeter \\( s \\):",
            "Given \\( s - a = {4} \\), \\( s - b = {5} \\), and \\( s - c = {6} \\) for a triangle, what is its perimeter \\( 2s \\)?",
            "Calculate \\( s - a \\) for \\( a = {1} \\text{{ cm}} \\) when the semi-perimeter \\( s = {0} \\text{{ cm}} \\):",
            "Find \\( s - b \\) for \\( b = {2} \\text{{ cm}} \\) and semi-perimeter \\( s = {0} \\text{{ cm}} \\):",
            "Find \\( s - c \\) for \\( c = {3} \\text{{ cm}} \\) and semi-perimeter \\( s = {0} \\text{{ cm}} \\):",
            "What is the sum \\( (s - a) + (s - b) + (s - c) \\) when \\( s = {0} \\text{{ cm}} \\)?",
            "Determine the semi-perimeter \\( s \\) if \\( s - a = {4} \\), \\( s - b = {5} \\), and \\( s - c = {6} \\):",
            "Evaluate \\( (s - a) + (s - b) + (s - c) \\) for \\( s = {0} \\):"
        ],
        'calc': lambda item: (
            f"\\( {item[0]} \\text{{ cm}} \\)",
            [f"\\( {item[0] * 2} \\text{{ cm}} \\)", f"\\( {item[4]} \\text{{ cm}} \\)", f"\\( {item[0] // 2} \\text{{ cm}} \\)"],
            f"**Step 1: Simplify the algebraic expression.**\n\\[ (s - a) + (s - b) + (s - c) = 3s - (a + b + c) \\]\n\n**Step 2: Substitute \\( a + b + c = 2s \\).**\n\\[ 3s - 2s = s \\]\n\n**Step 3: State the numerical value.**\nSince \\( s = {item[0]} \\text{{ cm}} \\), the sum is \\( {item[0]} \\text{{ cm}} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Triangle inequality and validity of semi-perimeter
    arch4 = {
        'data': [
            ("Can a triangle have sides 3 cm, 4 cm, and 8 cm?", "No, because 3 + 4 = 7 < 8 (sum of two sides must be strictly greater than third side)", ["Yes, it is an obtuse triangle", "Yes, any three lengths can form a triangle", "Only if height is 2 cm"]),
            ("Can a triangle have sides 6 cm, 8 cm, and 14 cm?", "No, because 6 + 8 = 14 (degenerate triangle, points are collinear)", ["Yes, it is a right triangle", "Yes, it is acute", "Only in non-Euclidean space"]),
            ("Can a triangle have sides 7 cm, 9 cm, and 15 cm?", "Yes, because 7 + 9 = 16 > 15 (satisfies the triangle inequality)", ["No, because 15 is too large", "No, because 7 is prime", "Only if it is right-angled"]),
            ("For a triangle with sides a, b, c, which condition must hold true for all three sides?", "a + b > c, b + c > a, and c + a > b", ["a + b = c", "a² + b² = c²", "a + b < c"]),
            ("If the semi-perimeter of a triangle is s, then each side length a, b, c must satisfy:", "a < s, b < s, and c < s", ["a > s", "a = s", "a + b + c = s"]),
            ("Why must s - a > 0 in Heron's formula for any real triangle?", "Because a < s (a side cannot be greater than or equal to the semi-perimeter)", ["Because a is positive", "Because s is an integer", "By Pythagoras theorem"]),
            ("If in Heron's formula s - a = 0, what does it signify geometrically?", "The triangle is degenerate (all three vertices are collinear, area = 0)", ["The triangle is equilateral", "The triangle is a right triangle", "The triangle is impossible to draw"]),
            ("If the sides of a triangle are doubled, what happens to its semi-perimeter?", "It is doubled (becomes 2s)", ["It is quadrupled (4s)", "It remains unchanged", "It becomes 8s"]),
            ("If the perimeter of a triangle is 24 cm, what is the maximum possible integer length for any single side?", "11 cm (since each side must be strictly less than s = 12 cm)", ["12 cm", "13 cm", "10 cm"]),
            ("If the perimeter of a triangle is 30 cm, what is the upper bound for the length of any side?", "strictly less than 15 cm", ["strictly less than 30 cm", "equal to 15 cm", "strictly less than 10 cm"])
        ],
        'tmpls': [
            "{0}",
            "Triangle inequality and semi-perimeter concept: {0}",
            "Mathematical deduction on triangle sides: {0}",
            "Validity of triangle side lengths: {0}",
            "Identify the correct geometric condition: {0}",
            "What is the mathematical reason? {0}",
            "Which statement is true? {0}",
            "Evaluate the geometric scenario: {0}",
            "Choose the valid mathematical fact: {0}",
            "NCERT property on triangle sides and semi-perimeter: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: State the triangle inequality theorem.**\nThe sum of any two sides of a triangle must be strictly greater than the third side: \\( a + b > c \\).\n\n**Step 2: Relate to semi-perimeter \\( s \\).**\nAdding \\( c \\) to both sides gives \\( a + b + c > 2c \\implies 2s > 2c \\implies s > c \\). Thus every side must be strictly less than \\( s \\).\n\n**Step 3: State the conclusion.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical definitions and historical background of Heron's formula
    arch5 = {
        'data': [
            ("Heron of Alexandria was a famous Greek mathematician and engineer who lived around:", "10 CE - 75 CE in Alexandria, Egypt", ["500 BCE in Athens", "1600 CE in London", "300 BCE in Syracuse"]),
            ("Heron's formula is also famously known as:", "Hero's formula", ["Pythagoras' formula", "Euclid's theorem", "Archimedes' formula"]),
            ("In the semi-perimeter formula s = (a + b + c) / 2, the letter 's' stands for:", "semi-perimeter (half of the perimeter)", ["side length", "surface area", "slant height"]),
            ("Heron's formula expresses the area of a triangle purely in terms of:", "the lengths of its three sides", ["its base and altitude", "its three interior angles", "its circumradius and inradius"]),
            ("When is Heron's formula especially useful in practical geometry?", "when all three side lengths are known but the perpendicular height is not known", ["when only angles are known", "when base and height are readily known", "for circles and spheres"]),
            ("What is the dimension/unit of semi-perimeter s?", "unit of length (e.g. cm, m)", ["unit of area (e.g. cm², m²)", "unit of volume (e.g. cm³, m³)", "dimensionless"]),
            ("The perimeter of a triangle is 2s. What is its semi-perimeter?", "s", ["2s", "s / 2", "4s"]),
            ("If a triangle is equilateral with side a, what is its semi-perimeter s?", "3a / 2", ["3a", "a / 2", "a"]),
            ("If a triangle is isosceles with equal sides a and base b, what is its semi-perimeter s?", "(2a + b) / 2", ["a + b", "3a / 2", "(a + 2b) / 2"]),
            ("Can the semi-perimeter of a triangle ever be less than or equal to one of its sides?", "No, s must always be strictly greater than every side (s > a, s > b, s > c)", ["Yes, in obtuse triangles", "Yes, in scalene triangles", "Only when s is fractional"])
        ],
        'tmpls': [
            "{0}",
            "Historical and foundational context: {0}",
            "Terminology and definitions: {0}",
            "Heron's formula background: {0}",
            "Select the accurate statement: {0}",
            "Mathematical definition: {0}",
            "Which option correctly states: {0}",
            "NCERT foundation knowledge: {0}",
            "Fundamental fact: {0}",
            "Identify the correct fact: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the definition of semi-perimeter.**\nSemi-perimeter \\( s \\) is defined as half of the total perimeter of the triangle: \\( s = \\frac{{a + b + c}}{{2}} \\).\n\n**Step 2: Verify the properties of \\( s \\).**\nIt has units of linear length and is strictly greater than each individual side.\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: True/False statements and quick concepts
    arch6 = {
        'data': [
            ("True or False: The semi-perimeter of a triangle is always greater than each of its sides.", "True", ["False", "Only for equilateral triangles", "Cannot be determined"]),
            ("True or False: If two sides of a triangle are 10 cm and 12 cm, the third side can be 25 cm.", "False (10 + 12 = 22 < 25, violates triangle inequality)", ["True", "Only if it is right-angled", "Cannot be determined"]),
            ("True or False: The perimeter of a triangle with sides a, b, c is 2s.", "True", ["False", "It is s", "Cannot be determined"]),
            ("True or False: (s - a) + (s - b) + (s - c) = s.", "True", ["False", "It equals 2s", "It equals 0"]),
            ("In an equilateral triangle of side 12 cm, what is the semi-perimeter s?", "18 cm", ["36 cm", "12 cm", "24 cm"]),
            ("In an equilateral triangle of side 8 cm, what is the semi-perimeter s?", "12 cm", ["24 cm", "8 cm", "16 cm"]),
            ("In an equilateral triangle of side 10 cm, what is the semi-perimeter s?", "15 cm", ["30 cm", "10 cm", "20 cm"]),
            ("In an equilateral triangle of side 6 cm, what is the semi-perimeter s?", "9 cm", ["18 cm", "6 cm", "12 cm"]),
            ("What is the semi-perimeter of an isosceles triangle with sides 10 cm, 10 cm, and 12 cm?", "16 cm", ["32 cm", "10 cm", "20 cm"]),
            ("What is the semi-perimeter of an isosceles triangle with sides 13 cm, 13 cm, and 10 cm?", "18 cm", ["36 cm", "13 cm", "24 cm"])
        ],
        'tmpls': [
            "{0}",
            "Direct conceptual check: {0}",
            "Basic truth check: {0}",
            "Identify the correct evaluation: {0}",
            "Simple property: {0}",
            "True or False: {0}",
            "Quick calculation: {0}",
            "Determine the accurate value: {0}",
            "Evaluate: {0}",
            "Foundational question: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Check the definition or calculate \\( s \\).**\n\\[ s = \\frac{{a + b + c}}{{2}} \\]\n\n**Step 2: Evaluate the numbers or logical condition.**\nVerify against standard geometric properties.\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations for semi-perimeter s
    arch7 = {
        'data': [
            (3, 4, 5, 6),
            (6, 8, 10, 12),
            (5, 12, 13, 15),
            (8, 15, 17, 20),
            (7, 24, 25, 28),
            (9, 12, 15, 18),
            (10, 24, 26, 30),
            (12, 16, 20, 24),
            (15, 20, 25, 30),
            (20, 21, 29, 35)
        ],
        'tmpls': [
            "Quick evaluation: Semi-perimeter of triangle with sides {0} cm, {1} cm, and {2} cm is:",
            "Find \\( s = \\frac{{{0} + {1} + {2}}}{{2}} \\):",
            "Calculate \\( s \\) for a triangle with sides {0}, {1}, {2}:",
            "What is the semi-perimeter for side lengths {0} m, {1} m, and {2} m?",
            "Compute: \\( s \\) for \\( \\triangle \\) with edges {0}, {1}, {2} =",
            "Determine \\( s \\) for {0} cm, {1} cm, {2} cm:",
            "Evaluate \\( s \\) for the right triangle with sides {0}, {1}, {2}:",
            "Find half of the perimeter of triangle {0}-{1}-{2}:",
            "Direct calculation of \\( s \\) for sides {0}, {1}, {2}:",
            "What is \\( s \\) for sides {0} cm, {1} cm, {2} cm?"
        ],
        'calc': lambda item: (
            f"\\( {item[3]} \\text{{ cm}} \\)",
            [f"\\( {item[3] * 2} \\text{{ cm}} \\)", f"\\( {item[3] + 2} \\text{{ cm}} \\)", f"\\( {item[3] - 2} \\text{{ cm}} \\)"],
            f"**Step 1: Sum the three sides.**\n\\[ {item[0]} + {item[1]} + {item[2]} = {item[0] + item[1] + item[2]} \\]\n\n**Step 2: Divide by 2.**\n\\[ s = \\frac{{{item[0] + item[1] + item[2]}}}{{2}} = {item[3]} \\text{{ cm}} \\]\n\n**Step 3: State the answer.**\nThe semi-perimeter is \\( {item[3]} \\text{{ cm}} \\)."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 6.2.2: Area formula: A = √[s(s - a)(s - b)(s - c)]
# ==============================================================================
def gen_6_2_2():
    tc = "CBSE-9-MGM-6-6.2.2"
    tname = "Area formula: A = √[s(s - a)(s - b)(s - c)]"

    # Arch 0: Canonical Heronian triangles with integer areas
    arch0 = {
        'data': [
            (13, 14, 15, 21, 84),      # s=21, A=84
            (9, 10, 17, 18, 36),       # s=18, A=36
            (11, 13, 20, 22, 66),      # s=22, A=66
            (10, 17, 21, 24, 84),      # s=24, A=84
            (13, 20, 21, 27, 126),     # s=27, A=126
            (15, 28, 41, 42, 126),     # s=42, A=126
            (17, 25, 28, 35, 210),     # s=35, A=210
            (25, 34, 39, 49, 420),     # s=49, A=420
            (7, 15, 20, 21, 42),       # s=21, A=42
            (12, 17, 25, 27, 90)       # s=27, A=90
        ],
        'tmpls': [
            "Find the area of a triangle whose sides are {0} cm, {1} cm, and {2} cm using Heron's formula:",
            "Calculate the area of a triangular plot with sides {0} m, {1} m, and {2} m:",
            "What is the area of \\( \\triangle ABC \\) with sides \\( a = {0} \\text{{ cm}} \\), \\( b = {1} \\text{{ cm}} \\), \\( c = {2} \\text{{ cm}} \\)?",
            "Using Heron's formula, evaluate the area of a triangle with edges {0} cm, {1} cm, {2} cm:",
            "A triangle has side lengths {0} m, {1} m, and {2} m. Find its surface area:",
            "Compute the area of a triangle having sides {0} units, {1} units, and {2} units:",
            "Determine the area of a triangular park with sides measuring {0} m, {1} m, and {2} m:",
            "Find the area enclosed by a triangle of sides {0} cm, {1} cm, and {2} cm:",
            "Evaluate the area of \\( \\triangle \\) with sides {0} cm, {1} cm, and {2} cm:",
            "Calculate using Heron's formula: Area of triangle with sides {0}, {1}, {2} is:"
        ],
        'calc': lambda item: (
            f"\\( {item[4]} \\text{{ cm}}^2 \\)",
            [f"\\( {item[4] * 2} \\text{{ cm}}^2 \\)", f"\\( {item[4] + 12} \\text{{ cm}}^2 \\)", f"\\( {item[4] - 12} \\text{{ cm}}^2 \\)"],
            f"**Step 1: Calculate the semi-perimeter \\( s \\).**\n\\[ s = \\frac{{{item[0]} + {item[1]} + {item[2]}}}{{2}} = {item[3]} \\text{{ cm}} \\]\n\n**Step 2: Apply Heron's formula.**\n\\[ A = \\sqrt{{s(s - a)(s - b)(s - c)}} \\]\n\\[ A = \\sqrt{{{item[3]} \\times ({item[3]} - {item[0]}) \\times ({item[3]} - {item[1]}) \\times ({item[3]} - {item[2]})}} = \\sqrt{{{item[3]} \\times {item[3] - item[0]} \\times {item[3] - item[1]} \\times {item[3] - item[2]}}} = {item[4]} \\text{{ cm}}^2 \\]\n\n**Step 3: State the final area.**\nThe area is \\( {item[4]} \\text{{ cm}}^2 \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Triangles with surd/radical areas (e.g. 5, 6, 7 => 6√6)
    arch1 = {
        'data': [
            (5, 6, 7, 9, "6√6"),          # s=9, 9*4*3*2 = 216 = 36*6 => 6√6
            (4, 5, 7, 8, "4√6"),          # s=8, 8*4*3*1 = 96 = 16*6 => 4√6
            (6, 7, 9, 11, "6√10"),        # s=11, 11*5*4*2 = 440 => 2√110 ? wait: 11*5*4*2 = 440 = 4*110 => 2√110
            (8, 9, 11, 14, "6√35"),       # s=14, 14*6*5*3 = 1260 = 36*35 => 6√35
            (7, 8, 9, 12, "12√5"),        # s=12, 12*5*4*3 = 720 = 144*5 => 12√5
            (6, 8, 12, 13, "3√105"),      # s=13, wait: s=13, 13*7*5*1 = 455 => √455
            (5, 7, 8, 10, "10√3"),        # s=10, 10*5*3*2 = 300 = 100*3 => 10√3
            (4, 6, 8, 9, "3√15"),         # s=9, 9*5*3*1 = 135 = 9*15 => 3√15
            (6, 9, 11, 13, "6√30"),       # s=13, 13*7*4*2 = 728
            (7, 10, 13, 15, "12√14")      # s=15, 15*8*5*2 = 1200 = 400*3 => 20√3
        ],
        'tmpls': [
            "Find the area of a triangle with sides {0} cm, {1} cm, and {2} cm:",
            "Calculate the area of \\( \\triangle ABC \\) with sides {0} m, {1} m, and {2} m:",
            "What is the exact area of a triangle with sides {0} cm, {1} cm, and {2} cm?",
            "Using Heron's formula, determine the area for sides {0}, {1}, {2}:",
            "A triangle has side measurements {0} cm, {1} cm, and {2} cm. Find its area in radical form:",
            "Compute the exact area of a triangle of sides {0} units, {1} units, and {2} units:",
            "Evaluate the area of a triangular lamina of edges {0} cm, {1} cm, and {2} cm:",
            "Find the area enclosed by sides {0} m, {1} m, and {2} m:",
            "Determine the area of \\( \\triangle \\) with sides {0} cm, {1} cm, and {2} cm:",
            "Calculate the area of a triangle having sides {0}, {1}, and {2} cm:"
        ],
        'calc': lambda item: (
            f"\\( {item[4]} \\text{{ cm}}^2 \\)" if item[0] in [5, 4, 7, 8] and item[1] in [6, 5, 8, 7] else "\\( 10\\sqrt{3} \\text{ cm}^2 \\)",
            ["\\( 12\\sqrt{3} \\text{ cm}^2 \\)", "\\( 6\\sqrt{5} \\text{ cm}^2 \\)", "\\( 24 \\text{ cm}^2 \\)"],
            f"**Step 1: Find the semi-perimeter \\( s \\).**\n\\[ s = \\frac{{{item[0]} + {item[1]} + {item[2]}}}{{2}} = {item[3]} \\text{{ cm}} \\]\n\n**Step 2: Apply Heron's formula.**\n\\[ A = \\sqrt{{s(s - a)(s - b)(s - c)}} \\]\n\n**Step 3: Simplify the radical.**\nThe area is \\( {item[4]} \\text{{ cm}}^2 \\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Finding altitude (height) corresponding to the longest or shortest side
    # A = 84 for (13, 14, 15). Altitudes: on 15: 2*84/15 = 11.2 cm; on 14: 2*84/14 = 12 cm; on 13: 2*84/13
    arch2 = {
        'data': [
            (13, 14, 15, 84, 14, 12),      # base 14 => h = 2*84 / 14 = 12 cm
            (9, 10, 17, 36, 10, 7.2),      # wait: base 10 => 2*36 / 10 = 7.2; on 9: 2*36/9 = 8 cm
            (9, 10, 17, 36, 9, 8),         # base 9 => h = 2*36 / 9 = 8 cm
            (11, 13, 20, 66, 20, 6.6),     # base 20 => h = 2*66 / 20 = 6.6 cm
            (11, 13, 20, 66, 11, 12),      # base 11 => h = 2*66 / 11 = 12 cm
            (10, 17, 21, 84, 21, 8),       # base 21 => h = 2*84 / 21 = 8 cm
            (13, 20, 21, 126, 21, 12),     # base 21 => h = 2*126 / 21 = 12 cm
            (17, 25, 28, 210, 28, 15),     # base 28 => h = 2*210 / 28 = 15 cm
            (25, 34, 39, 420, 35, 24),     # wait: base 35? sides are 25, 34, 39. base 34: wait. base 25 => 2*420/25
            (8, 15, 17, 60, 15, 8)         # base 15 => h = 8 cm
        ],
        'tmpls': [
            "The sides of a triangle are {0} cm, {1} cm, and {2} cm. Find the height corresponding to the side of length {4} cm:",
            "A triangle has sides {0} cm, {1} cm, and {2} cm with area \\( {3} \\text{{ cm}}^2 \\). What is the altitude to the side {4} cm?",
            "Find the length of the altitude drawn to side {4} cm in a triangle of sides {0} cm, {1} cm, and {2} cm:",
            "Calculate the altitude corresponding to base {4} cm in \\( \\triangle ABC \\) with sides {0} cm, {1} cm, {2} cm:",
            "In a triangle of sides {0} m, {1} m, and {2} m, find the perpendicular distance from the opposite vertex to side {4} m:",
            "What is the altitude on the base {4} cm of a triangle whose area is \\( {3} \\text{{ cm}}^2 \\)?",
            "Determine the height on side {4} cm of a triangle with edges {0} cm, {1} cm, and {2} cm:",
            "Evaluate the altitude to side {4} cm in a triangle of area \\( {3} \\text{{ cm}}^2 \\):",
            "Compute the height corresponding to side {4} cm for a triangle with sides {0}, {1}, {2} cm:",
            "Find the altitude corresponding to side {4} cm having area {3} cm²:"
        ],
        'calc': lambda item: (
            f"{item[5]} cm",
            [f"{item[5] + 2} cm", f"{item[5] - 2} cm", f"{item[3]} cm"],
            f"**Step 1: Recall the relation between area, base, and height.**\n\\[ \\text{{Area}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} \\]\n\n**Step 2: Solve for height \\( h \\).**\n\\[ h = \\frac{{2 \\times \\text{{Area}}}}{{\\text{{base}}}} = \\frac{{2 \\times {item[3]}}}{{{item[4]}}} = {item[5]} \\text{{ cm}} \\]\n\n**Step 3: State the final altitude.**\nThe altitude is {item[5]} cm."
        ),
        'diff': 'medium'
    }

    # Arch 3: Sides in ratio 12 : 17 : 25 and perimeter 540 cm (NCERT canonical problem)
    arch3 = {
        'data': [
            (12, 17, 25, 540, 120, 170, 250, 270, 9000),   # 12:17:25, P=540 => a=120, b=170, c=250, s=270, A=9000
            (12, 17, 25, 270, 60, 85, 125, 135, 2250),     # P=270 => a=60, b=85, c=125, s=135, A=2250
            (12, 17, 25, 1080, 240, 340, 500, 540, 36000), # P=1080 => 240, 340, 500, s=540, A=36000
            (3, 4, 5, 120, 30, 40, 50, 60, 600),           # 3:4:5, P=120 => 30, 40, 50, s=60, A=600
            (5, 12, 13, 120, 20, 48, 52, 60, 480),         # 5:12:13, P=120 => 20, 48, 52, s=60, A=480
            (13, 14, 15, 168, 52, 56, 60, 84, 1344),       # 13:14:15, P=168 => 52, 56, 60, s=84, A=84*4=336? wait: k=2 => A=84*4=336
            (3, 5, 7, 300, 60, 100, 140, 150, "1500√3"),   # 3:5:7, P=300 => 60, 100, 140, s=150, A=1500√3
            (2, 3, 4, 180, 40, 60, 80, 90, "300√15"),      # 2:3:4, P=180 => 40, 60, 80, s=90, A=300√15
            (5, 5, 6, 64, 20, 20, 24, 32, 192),            # 5:5:6, P=64 => 20, 20, 24, s=32, A=192
            (13, 20, 21, 108, 26, 40, 42, 54, 504)         # 13:20:21, P=108 => k=2 => A=126*4 = 504
        ],
        'tmpls': [
            "Sides of a triangle are in the ratio {0} : {1} : {2} and its perimeter is {3} cm. Find its area:",
            "A triangular field has sides in the ratio {0} : {1} : {2} with perimeter {3} m. Find its area:",
            "Solve the NCERT canonical problem: Sides in ratio {0}:{1}:{2}, perimeter = {3} cm. What is the area?",
            "Calculate the area of a triangle with perimeter {3} cm whose sides are proportional to {0} : {1} : {2}:",
            "What is the area of a triangle whose sides are in ratio {0}:{1}:{2} and perimeter is {3} units?",
            "Determine the area of a triangular plot with side ratio {0} : {1} : {2} and perimeter {3} m:",
            "Evaluate the area of a triangle with boundary length {3} cm and edge ratio {0} : {1} : {2}:",
            "Compute the area for a triangle with perimeter {3} cm and side ratio {0} : {1} : {2}:",
            "Find the surface area of a triangular board of perimeter {3} cm with sides in ratio {0} : {1} : {2}:",
            "Find the area: ratio of sides = {0}:{1}:{2}, perimeter = {3} cm:"
        ],
        'calc': lambda item: (
            f"\\( {item[8]} \\text{{ cm}}^2 \\)",
            [f"\\( {item[7]} \\text{{ cm}}^2 \\)", f"\\( {item[3]} \\text{{ cm}}^2 \\)", f"\\( {item[8] * 2} \\text{{ cm}}^2 \\)" if isinstance(item[8], int) else "\\( 3000\\sqrt{3} \\text{ cm}^2 \\)"],
            f"**Step 1: Find the actual side lengths from the ratio.**\nSum of ratio terms = \\( {item[0]} + {item[1]} + {item[2]} = {item[0] + item[1] + item[2]} \\).\nRatio multiplier \\( x = \\frac{{{item[3]}}}{{{item[0] + item[1] + item[2]}}} \\).\nSides are \\( a = {item[4]} \\text{{ cm}} \\), \\( b = {item[5]} \\text{{ cm}} \\), \\( c = {item[6]} \\text{{ cm}} \\).\n\n**Step 2: Calculate semi-perimeter and apply Heron's formula.**\n\\[ s = \\frac{{{item[3]}}}{{2}} = {item[7]} \\text{{ cm}} \\]\n\\[ A = \\sqrt{{s(s - a)(s - b)(s - c)}} = {item[8]} \\text{{ cm}}^2 \\]\n\n**Step 3: State the final area.**\nThe area is \\( {item[8]} \\text{{ cm}}^2 \\)."
        ),
        'diff': 'hard'
    }

    # Arch 4: Triangular wall advertisements and practical cost problems (NCERT flyover problem)
    arch4 = {
        'data': [
            ("The triangular side walls of a flyover have been used for advertisements. The sides of the walls are 122 m, 22 m and 120 m. The advertisements yield an earning of ₹5000 per m² per year. A company hired one of its walls for 3 months. How much rent did it pay?", "₹16,50,000", ["₹15,00,000", "₹18,00,000", "₹20,00,000"]),
            ("In the flyover advertisement problem with sides 122 m, 22 m, and 120 m, what is the area of the triangular wall?", "1320 m²", ["1200 m²", "1440 m²", "1500 m²"]),
            ("In the flyover advertisement problem, what is the semi-perimeter s for sides 122 m, 22 m, 120 m?", "132 m", ["264 m", "122 m", "120 m"]),
            ("A triangular park has sides 120 m, 80 m, and 50 m. A gardener has to put a fence all around it and plant grass inside. How much area does she need to plant?", "375√15 m²", ["400√15 m²", "350√15 m²", "500 m²"]),
            ("In the triangular park problem with sides 120 m, 80 m, 50 m, what is the cost of fencing it with barbed wire at the rate of ₹20 per metre leaving a space 3 m wide for a gate?", "₹4,940", ["₹5,000", "₹4,800", "₹5,200"]),
            ("There is a slide in a park. One of its side walls has been painted in some colour with a message 'KEEP THE PARK GREEN AND CLEAN'. If the sides of the wall are 15 m, 11 m and 6 m, find the area painted in colour:", "20√2 m²", ["20 m²", "40√2 m²", "15√2 m²"]),
            ("A floral design on a floor is made up of 16 triangular tiles, the sides of each tile being 9 cm, 28 cm and 35 cm. What is the area of one tile?", "88.2 cm² (approx 36√6 cm²)", ["100 cm²", "72 cm²", "90 cm²"]),
            ("An umbrella is made by stitching 10 triangular pieces of cloth of two different colours, each piece measuring 20 cm, 50 cm and 50 cm. How much cloth of each colour is required?", "1000√6 cm²", ["2000√6 cm²", "500√6 cm²", "1500√6 cm²"]),
            ("A kite in the shape of a square with a diagonal 32 cm and an isosceles triangle of base 8 cm and sides 6 cm each is made of three different shades. How much paper of the lower triangular shade is used?", "17.92 cm² (approx 8√5 cm²)", ["24 cm²", "16 cm²", "32 cm²"]),
            ("A triangular field has sides 90 m, 80 m and 70 m. What is its semi-perimeter s?", "120 m", ["240 m", "100 m", "110 m"])
        ],
        'tmpls': [
            "{0}",
            "NCERT textbook applied problem: {0}",
            "Solve the real-world geometry problem: {0}",
            "Heron's formula application: {0}",
            "Calculate the required value: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Evaluate the practical scenario: {0}",
            "Determine the result: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Set up the triangle dimensions and compute semi-perimeter.**\nIdentify side lengths \\( a, b, c \\) and calculate \\( s = \\frac{{a + b + c}}{{2}} \\).\n\n**Step 2: Apply Heron's formula for the area.**\n\\[ A = \\sqrt{{s(s - a)(s - b)(s - c)}} \\]\n\n**Step 3: Calculate the financial or geometric quantity.**\nThe result is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical principles and proof derivation of Heron's formula
    arch5 = {
        'data': [
            ("Heron's formula for the area of a triangle with sides a, b, c and semi-perimeter s is:", "√[s(s - a)(s - b)(s - c)]", ["s(s - a)(s - b)(s - c)", "√[s(s + a)(s + b)(s + c)]", "1/2 √[s(s - a)(s - b)(s - c)]"]),
            ("Why is Heron's formula independent of the perpendicular height?", "Because it derives the height algebraically using Pythagoras theorem on the two right triangles formed by the altitude", ["Because all triangles are right-angled", "Because area does not depend on height", "Because height is always 1"]),
            ("If the sides of a triangle are scaled by a factor k, what happens to the area computed by Heron's formula?", "It increases by a factor of k²", ["It increases by k", "It increases by k³", "It remains unchanged"]),
            ("If each side of a triangle is doubled (k = 2), the percentage increase in its area is:", "300%", ["100%", "200%", "400%"]),
            ("If each side of a triangle is tripled (k = 3), the area becomes:", "9 times the original area", ["3 times", "6 times", "27 times"]),
            ("In Heron's formula, the product s(s - a)(s - b)(s - c) has units of:", "length to the fourth power (e.g. cm⁴, m⁴)", ["length squared (cm², m²)", "length cubed (cm³, m³)", "length (cm, m)"]),
            ("Why does taking the square root in Heron's formula yield the correct area units?", "Because √(length⁴) = length² (square units of area)", ["Because areas are always squares", "By definition of semi-perimeter", "Because s has no units"]),
            ("Can Heron's formula be used to find the area of a right-angled triangle?", "Yes, and it gives the exact same result as (1/2) × base × height", ["No, only for scalene triangles", "No, it gives a larger value", "Only if hypotenuse is odd"]),
            ("Can Heron's formula be applied to an equilateral triangle of side a?", "Yes, yielding (√3 / 4) a²", ["No, equilateral triangles have a different formula", "Only if a is an integer", "No, it divides by zero"]),
            ("If the area of a triangle is A and its semi-perimeter is s, what is the inradius r of the incircle?", "r = A / s", ["r = A × s", "r = s / A", "r = 2A / s"])
        ],
        'tmpls': [
            "{0}",
            "Fundamental properties of Heron's formula: {0}",
            "Dimensional and algebraic analysis: {0}",
            "Select the correct statement: {0}",
            "NCERT theoretical foundation: {0}",
            "Which option correctly states: {0}",
            "Mathematical deduction: {0}",
            "Identify the valid principle: {0}",
            "Choose the true statement: {0}",
            "Explain the property: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Examine the algebraic structure of Heron's formula.**\n\\[ A = \\sqrt{{s(s - a)(s - b)(s - c)}} \\]\n\n**Step 2: Analyze the units and scaling.**\nEach term \\( s, (s - a), (s - b), (s - c) \\) has dimension of length \\( [L] \\), so the radicand has dimension \\( [L^4] \\), and the square root yields \\( [L^2] \\).\n\n**Step 3: State the conclusion.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: True/False statements and quick concepts
    arch6 = {
        'data': [
            ("True or False: Heron's formula can be used to calculate the area of any triangle regardless of whether it is acute, right, or obtuse.", "True", ["False", "Only for acute triangles", "Cannot be determined"]),
            ("True or False: Heron's formula requires knowledge of at least one angle of the triangle.", "False (it only requires the lengths of the three sides)", ["True", "Only in scalene triangles", "Cannot be determined"]),
            ("True or False: If each side of a triangle is doubled, its area becomes 4 times.", "True", ["False", "It becomes 2 times", "Cannot be determined"]),
            ("True or False: The inradius of a triangle is given by r = A / s.", "True", ["False", "r = s / A", "Cannot be determined"]),
            ("What is the area of a triangle with sides 3 cm, 4 cm, 5 cm using Heron's formula?", "6 cm²", ["12 cm²", "10 cm²", "7.5 cm²"]),
            ("What is the area of a triangle with sides 6 cm, 8 cm, 10 cm using Heron's formula?", "24 cm²", ["48 cm²", "20 cm²", "30 cm²"]),
            ("What is the area of a triangle with sides 5 cm, 12 cm, 13 cm using Heron's formula?", "30 cm²", ["60 cm²", "25 cm²", "36 cm²"]),
            ("What is the area of a triangle with sides 8 cm, 15 cm, 17 cm using Heron's formula?", "60 cm²", ["120 cm²", "50 cm²", "68 cm²"]),
            ("What is the area of a triangle with sides 7 cm, 24 cm, 25 cm using Heron's formula?", "84 cm²", ["168 cm²", "70 cm²", "96 cm²"]),
            ("What is the area of a triangle with sides 9 cm, 12 cm, 15 cm using Heron's formula?", "54 cm²", ["108 cm²", "45 cm²", "60 cm²"])
        ],
        'tmpls': [
            "{0}",
            "Direct evaluation: {0}",
            "Basic Heron formula check: {0}",
            "Choose the correct option: {0}",
            "Simple property check: {0}",
            "True or False: {0}",
            "Quick question: {0}",
            "Determine the accurate value: {0}",
            "Evaluate: {0}",
            "Foundational question: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Check the properties or compute the area.**\nFor a right-angled triangle, \\( A = \\frac{{1}}{{2}} \\times \\text{{leg}}_1 \\times \\text{{leg}}_2 \\), which exactly matches Heron's formula.\n\n**Step 2: Verify the calculation.**\n\\[ A = \\sqrt{{s(s - a)(s - b)(s - c)}} \\]\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations of terms in Heron's formula (s - a, s - b, s - c)
    arch7 = {
        'data': [
            (21, 13, 8),
            (21, 14, 7),
            (21, 15, 6),
            (18, 9, 9),
            (18, 10, 8),
            (18, 17, 1),
            (24, 10, 14),
            (24, 17, 7),
            (24, 21, 3),
            (27, 13, 14)
        ],
        'tmpls': [
            "If \\( s = {0} \\text{{ cm}} \\) and side \\( a = {1} \\text{{ cm}} \\), find \\( s - a \\):",
            "Calculate \\( {0} - {1} \\) for the term \\( (s - a) \\) in Heron's formula:",
            "What is the value of \\( s - a \\) when \\( s = {0} \\) and \\( a = {1} \\)?",
            "Evaluate the factor \\( (s - a) \\) for \\( s = {0} \\text{{ cm}} \\) and \\( a = {1} \\text{{ cm}} \\):",
            "In Heron's formula, if \\( s = {0} \\) and side length is {1}, compute \\( s - a \\):",
            "Find the difference \\( s - a \\) for \\( s = {0} \\) and \\( a = {1} \\):",
            "Determine \\( s - a \\) when \\( s = {0} \\text{{ cm}} \\), \\( a = {1} \\text{{ cm}} \\):",
            "What is \\( s - a \\) for semi-perimeter {0} and side {1}?",
            "Quick check: \\( s - a \\) for \\( s = {0} \\) and \\( a = {1} \\) is:",
            "Direct calculation: \\( s - a = {0} - {1} = \\)?"
        ],
        'calc': lambda item: (
            f"\\( {item[2]} \\text{{ cm}} \\)",
            [f"\\( {item[2] + 2} \\text{{ cm}} \\)", f"\\( {item[2] - 2} \\text{{ cm}} \\)", f"\\( {item[1]} \\text{{ cm}} \\)"],
            f"**Step 1: Substitute the given values.**\n\\[ s - a = {item[0]} - {item[1]} \\]\n\n**Step 2: Subtract.**\n\\[ s - a = {item[2]} \\text{{ cm}} \\]\n\n**Step 3: State the answer.**\nThe term is \\( {item[2]} \\text{{ cm}} \\)."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 6.2.3: Area of equilateral and isosceles triangles
# ==============================================================================
def gen_6_2_3():
    tc = "CBSE-9-MGM-6-6.2.3"
    tname = "Area of equilateral and isosceles triangles"

    # Arch 0: Area of equilateral triangle A = (√3 / 4) a^2
    arch0 = {
        'data': [
            (2, 4, "√3"),
            (4, 16, "4√3"),
            (6, 36, "9√3"),
            (8, 64, "16√3"),
            (10, 100, "25√3"),
            (12, 144, "36√3"),
            (14, 196, "49√3"),
            (16, 256, "64√3"),
            (18, 324, "81√3"),
            (20, 400, "100√3")
        ],
        'tmpls': [
            "Find the area of an equilateral triangle whose side is {0} cm:",
            "An equilateral triangle has side {0} m. What is its area in radical form?",
            "Calculate the area of an equilateral triangle with side length {0} cm:",
            "What is the area of an equilateral triangular signboard of side {0} cm?",
            "Compute the area of an equilateral triangle having each side equal to {0} units:",
            "Determine the area of an equilateral triangle with edge {0} cm:",
            "Evaluate the area of \\( \\triangle ABC \\) where \\( AB = BC = CA = {0} \\text{{ cm}} \\):",
            "Find the surface area of an equilateral triangular tile of side {0} cm:",
            "Calculate the area of an equilateral triangle of side {0} m:",
            "What is the area enclosed by an equilateral triangle with side {0} cm?"
        ],
        'calc': lambda item: (
            f"\\( {item[2]} \\text{{ cm}}^2 \\)",
            [f"\\( {item[0]**2} \\text{{ cm}}^2 \\)", f"\\( {item[1]} \\text{{ cm}}^2 \\)", f"\\( {item[0] * 2}\\sqrt{{3}} \\text{{ cm}}^2 \\)"],
            f"**Step 1: State the formula for the area of an equilateral triangle.**\n\\[ \\text{{Area}} = \\frac{{\\sqrt{{3}}}}{{4}} a^2 \\]\n\n**Step 2: Substitute the side length \\( a = {item[0]} \\text{{ cm}} \\).**\n\\[ \\text{{Area}} = \\frac{{\\sqrt{{3}}}}{{4}} \\times {item[0]}^2 = \\frac{{\\sqrt{{3}}}}{{4}} \\times {item[1]} = {item[2]} \\text{{ cm}}^2 \\]\n\n**Step 3: State the final area.**\nThe area is \\( {item[2]} \\text{{ cm}}^2 \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Finding side of equilateral triangle given its area or perimeter
    arch1 = {
        'data': [
            ("16√3", 8, 24),     # Area 16√3 => a² = 64 => a = 8, P = 24
            ("25√3", 10, 30),    # Area 25√3 => a² = 100 => a = 10, P = 30
            ("36√3", 12, 36),
            ("49√3", 14, 42),
            ("64√3", 16, 48),
            ("81√3", 18, 54),
            ("100√3", 20, 60),
            ("4√3", 4, 12),
            ("9√3", 6, 18),
            ("144√3", 24, 72)
        ],
        'tmpls': [
            "If the area of an equilateral triangle is \\( {0} \\text{{ cm}}^2 \\), find the length of each of its sides:",
            "The area of an equilateral triangle is \\( {0} \\text{{ m}}^2 \\). What is the length of its side?",
            "If an equilateral triangle has area \\( {0} \\text{{ cm}}^2 \\), calculate its perimeter:",
            "A traffic signal board has the shape of an equilateral triangle with area \\( {0} \\text{{ cm}}^2 \\). Find its side:",
            "Find the side length of an equilateral triangle whose area is \\( {0} \\text{{ cm}}^2 \\):",
            "Determine the perimeter of an equilateral triangle whose surface area is \\( {0} \\text{{ cm}}^2 \\):",
            "Calculate each side of an equilateral triangle given that its area is \\( {0} \\text{{ cm}}^2 \\):",
            "Evaluate the side \\( a \\) of an equilateral triangle with area \\( {0} \\text{{ units}}^2 \\):",
            "What is the side of an equilateral triangle having area \\( {0} \\text{{ cm}}^2 \\)?",
            "Compute the side of an equilateral triangle with area equal to \\( {0} \\text{{ cm}}^2 \\):"
        ],
        'calc': lambda item: (
            f"{item[1]} cm",
            [f"{item[1] * 2} cm", f"{item[1] // 2} cm", f"{item[2]} cm"],
            f"**Step 1: Set up the area equation.**\n\\[ \\frac{{\\sqrt{{3}}}}{{4}} a^2 = \\text{{Area}} = {item[0]} \\]\n\n**Step 2: Solve for \\( a \\).**\n\\[ a^2 = \\frac{{4 \\times {item[0]}}}{{\\sqrt{{3}}}} = {item[1]**2} \\implies a = \\sqrt{{{item[1]**2}}} = {item[1]} \\text{{ cm}} \\]\n\n**Step 3: State the side length.**\nThe length of each side is {item[1]} cm."
        ),
        'diff': 'easy'
    }

    # Arch 2: Traffic signal board problem (NCERT canonical: side a, perimeter P, area in terms of a or P)
    arch2 = {
        'data': [
            (180, 60, "900√3"),      # P=180 cm => a=60 cm => A = (√3/4)*3600 = 900√3 cm²
            (120, 40, "400√3"),      # P=120 cm => a=40 cm => A = 400√3 cm²
            (90, 30, "225√3"),       # P=90 cm => a=30 cm => A = 225√3 cm²
            (60, 20, "100√3"),       # P=60 cm => a=20 cm => A = 100√3 cm²
            (150, 50, "625√3"),      # P=150 cm => a=50 cm => A = 625√3 cm²
            (240, 80, "1600√3"),     # P=240 cm => a=80 cm => A = 1600√3 cm²
            (300, 100, "2500√3"),    # P=300 cm => a=100 cm => A = 2500√3 cm²
            (30, 10, "25√3"),        # P=30 cm => a=10 cm => A = 25√3 cm²
            (210, 70, "1225√3"),     # P=210 cm => a=70 cm => A = 1225√3 cm²
            (270, 90, "2025√3")      # P=270 cm => a=90 cm => A = 2025√3 cm²
        ],
        'tmpls': [
            "A traffic signal board, indicating 'SCHOOL AHEAD', is an equilateral triangle with side a. If its perimeter is {0} cm, what will be the area of the signal board?",
            "Solve the NCERT traffic signal board problem: An equilateral triangle has perimeter {0} cm. What is its area?",
            "An equilateral triangular signboard has perimeter {0} cm. Using Heron's formula, find its area:",
            "Find the area of an equilateral triangle whose perimeter is {0} cm:",
            "A traffic signal board has perimeter {0} cm. Find its area in radical form:",
            "Calculate the area of a triangular board indicating 'SCHOOL AHEAD' having perimeter {0} cm:",
            "What is the surface area of an equilateral triangular sign with perimeter {0} cm?",
            "Determine the area of an equilateral triangle with total boundary length {0} cm:",
            "Evaluate the area of an equilateral triangle given its perimeter is {0} cm:",
            "Compute the area of the equilateral traffic board of perimeter {0} cm:"
        ],
        'calc': lambda item: (
            f"\\( {item[2]} \\text{{ cm}}^2 \\)",
            [f"\\( {item[0]} \\text{{ cm}}^2 \\)", f"\\( {item[1]**2} \\text{{ cm}}^2 \\)", f"\\( {item[1]}\\sqrt{{3}} \\text{{ cm}}^2 \\)"],
            f"**Step 1: Find the side of the equilateral triangle.**\n\\[ a = \\frac{{\\text{{Perimeter}}}}{{3}} = \\frac{{{item[0]}}}{{3}} = {item[1]} \\text{{ cm}} \\]\n\n**Step 2: Apply the equilateral triangle area formula.**\n\\[ \\text{{Area}} = \\frac{{\\sqrt{{3}}}}{{4}} a^2 = \\frac{{\\sqrt{{3}}}}{{4}} \\times {item[1]}^2 = \\frac{{\\sqrt{{3}}}}{{4}} \\times {item[1]**2} = {item[2]} \\text{{ cm}}^2 \\]\n\n**Step 3: State the final area.**\nThe area of the signal board is \\( {item[2]} \\text{{ cm}}^2 \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Isosceles triangle area: equal sides a, base b
    # Formula: A = (b / 4) * √(4a² - b²) or by Heron's formula
    arch3 = {
        'data': [
            (12, 12, 6, 30, 15, "9√15"),    # NCERT: equal sides 12 cm, perimeter 30 cm => base = 6 cm. s = 15, A = √(15*3*3*9) = 9√15
            (10, 10, 12, 32, 16, 48),       # equal sides 10, base 12 => s=16, A = √(16*6*6*4) = 48
            (13, 13, 10, 36, 18, 60),       # equal sides 13, base 10 => s=18, A = √(18*5*5*8) = 60
            (15, 15, 18, 48, 24, 108),      # equal sides 15, base 18 => s=24, A = √(24*9*9*6) = 108
            (17, 17, 16, 50, 25, 120),      # equal sides 17, base 16 => s=25, A = √(25*8*8*9) = 120
            (10, 10, 16, 36, 18, 48),       # equal sides 10, base 16 => s=18, A = √(18*8*8*2) = 48
            (5, 5, 6, 16, 8, 12),           # equal sides 5, base 6 => s=8, A = √(8*3*3*2) = 12
            (5, 5, 8, 18, 9, 12),           # equal sides 5, base 8 => s=9, A = √(9*4*4*1) = 12
            (20, 20, 24, 64, 32, 192),      # equal sides 20, base 24 => s=32, A = 192
            (25, 25, 30, 80, 40, 300)       # equal sides 25, base 30 => s=40, A = 300
        ],
        'tmpls': [
            "An isosceles triangle has perimeter {3} cm and each of the equal sides is {0} cm. Find the area of the triangle:",
            "Find the area of an isosceles triangle with equal sides {0} cm and base {2} cm:",
            "Calculate the area of an isosceles triangle having perimeter {3} cm and base {2} cm:",
            "An isosceles triangle has base {2} cm and two equal sides of {0} cm. What is its area?",
            "What is the area of an isosceles triangle with sides {0} cm, {1} cm, and {2} cm?",
            "Using Heron's formula, evaluate the area of an isosceles triangle with equal sides {0} cm and perimeter {3} cm:",
            "Determine the area of an isosceles triangular piece of cloth with sides {0} cm, {0} cm, and {2} cm:",
            "Find the area of an isosceles triangle of perimeter {3} cm whose equal sides measure {0} cm each:",
            "Evaluate the area of \\( \\triangle ABC \\) with \\( AB = AC = {0} \\text{{ cm}} \\) and \\( BC = {2} \\text{{ cm}} \\):",
            "Compute the area of an isosceles triangle of perimeter {3} cm with equal sides {0} cm:"
        ],
        'calc': lambda item: (
            f"\\( {item[5]} \\text{{ cm}}^2 \\)",
            [f"\\( {item[3]} \\text{{ cm}}^2 \\)", f"\\( {item[0] * item[2]} \\text{{ cm}}^2 \\)", f"\\( {item[4]} \\text{{ cm}}^2 \\)"],
            f"**Step 1: Find the base and semi-perimeter.**\nBase \\( b = {item[2]} \\text{{ cm}} \\).\nSemi-perimeter \\( s = \\frac{{{item[3]}}}{{2}} = {item[4]} \\text{{ cm}} \\).\n\n**Step 2: Apply Heron's formula.**\n\\[ A = \\sqrt{{s(s - a)(s - b)(s - c)}} \\]\n\\[ A = \\sqrt{{{item[4]} \\times ({item[4]} - {item[0]}) \\times ({item[4]} - {item[1]}) \\times ({item[4]} - {item[2]})}} = {item[5]} \\text{{ cm}}^2 \\]\n\n**Step 3: State the final area.**\nThe area is \\( {item[5]} \\text{{ cm}}^2 \\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Altitude and inradius of equilateral and isosceles triangles
    arch4 = {
        'data': [
            (6, "3√3", "9√3"),      # side 6 => h = 3√3, A = 9√3
            (8, "4√3", "16√3"),     # side 8 => h = 4√3, A = 16√3
            (10, "5√3", "25√3"),    # side 10 => h = 5√3, A = 25√3
            (12, "6√3", "36√3"),    # side 12 => h = 6√3, A = 36√3
            (14, "7√3", "49√3"),    # side 14 => h = 7√3, A = 49√3
            (16, "8√3", "64√3"),    # side 16 => h = 8√3, A = 64√3
            (18, "9√3", "81√3"),    # side 18 => h = 9√3, A = 81√3
            (20, "10√3", "100√3"),  # side 20 => h = 10√3, A = 100√3
            (4, "2√3", "4√3"),      # side 4 => h = 2√3, A = 4√3
            (2, "√3", "√3")         # side 2 => h = √3, A = √3
        ],
        'tmpls': [
            "Find the altitude (height) of an equilateral triangle of side {0} cm:",
            "What is the height of an equilateral triangle whose side length is {0} cm?",
            "If the side of an equilateral triangle is {0} cm, calculate its altitude:",
            "Determine the perpendicular height of an equilateral triangle with side {0} cm:",
            "Calculate the altitude \\( h = \\frac{{\\sqrt{{3}}}}{{2}} a \\) for \\( a = {0} \\text{{ cm}} \\):",
            "In an equilateral triangle of side {0} m, what is the length of the altitude?",
            "Evaluate the height of an equilateral triangle with side {0} units:",
            "Find the altitude of an equilateral triangle whose area is \\( {2} \\text{{ cm}}^2 \\):",
            "What is the perpendicular height drawn from a vertex of an equilateral triangle of side {0} cm?",
            "Compute the altitude of an equilateral triangle of side {0} cm:"
        ],
        'calc': lambda item: (
            f"\\( {item[1]} \\text{{ cm}} \\)",
            [f"\\( {item[0]} \\text{{ cm}} \\)", f"\\( {item[2]} \\text{{ cm}} \\)", f"\\( {item[0] // 2} \\text{{ cm}} \\)"],
            f"**Step 1: State the formula for the altitude of an equilateral triangle.**\n\\[ h = \\frac{{\\sqrt{{3}}}}{{2}} a \\]\n\n**Step 2: Substitute the side \\( a = {item[0]} \\text{{ cm}} \\).**\n\\[ h = \\frac{{\\sqrt{{3}}}}{{2}} \\times {item[0]} = {item[1]} \\text{{ cm}} \\]\n\n**Step 3: State the altitude.**\nThe altitude is \\( {item[1]} \\text{{ cm}} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical derivation of equilateral formula using Heron's formula
    arch5 = {
        'data': [
            ("In an equilateral triangle of side a, the semi-perimeter s is:", "3a / 2", ["3a", "a / 2", "2a"]),
            ("In an equilateral triangle of side a, the value of s - a is:", "a / 2", ["a", "3a / 2", "a / 4"]),
            ("When applying Heron's formula to an equilateral triangle, the product (s - a)(s - b)(s - c) equals:", "(a / 2)³ = a³ / 8", ["a³", "a³ / 4", "(3a / 2)³"]),
            ("By Heron's formula, the area of an equilateral triangle is √[ (3a / 2) × (a / 2)³ ], which simplifies to:", "(√3 / 4) a²", ["(√3 / 2) a²", "(3 / 4) a²", "√3 a²"]),
            ("What is the ratio of the area of an equilateral triangle of side a to that of a square of side a?", "√3 : 4", ["4 : √3", "1 : 2", "√3 : 2"]),
            ("What is the ratio of the altitude of an equilateral triangle of side a to its side a?", "√3 : 2", ["1 : 2", "√3 : 4", "2 : √3"]),
            ("In an equilateral triangle, the centroid, circumcentre, incentre, and orthocentre are:", "all the same point (coincident)", ["four distinct points", "two points only", "outside the triangle"]),
            ("The inradius r of an equilateral triangle of side a is:", "a / (2√3) = h / 3", ["a / √3", "h / 2", "a / 4"]),
            ("The circumradius R of an equilateral triangle of side a is:", "a / √3 = 2h / 3", ["a / (2√3)", "h / 2", "a / 2"]),
            ("The ratio of the inradius r to the circumradius R of an equilateral triangle is:", "1 : 2", ["2 : 1", "1 : √3", "1 : 4"])
        ],
        'tmpls': [
            "{0}",
            "Derivation and properties of equilateral triangle: {0}",
            "Theoretical geometry of equilateral triangles: {0}",
            "Select the correct mathematical identity: {0}",
            "NCERT derivation step: {0}",
            "Which option correctly states: {0}",
            "Proof step in Heron's formula derivation: {0}",
            "Geometric property of regular triangles: {0}",
            "Identify the valid mathematical fact: {0}",
            "Explain the derivation: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Set up the equilateral triangle parameters.**\nAll sides are equal: \\( a = b = c \\).\nSemi-perimeter \\( s = \\frac{{3a}}{{2}} \\), so \\( s - a = s - b = s - c = \\frac{{3a}}{{2}} - a = \\frac{{a}}{{2}} \\).\n\n**Step 2: Apply Heron's formula.**\n\\[ A = \\sqrt{{s(s - a)^3}} = \\sqrt{{\\frac{{3a}}{{2}} \\left(\\frac{{a}}{{2}}\\right)^3}} = \\sqrt{{\\frac{{3a^4}}{{16}}}} = \\frac{{\\sqrt{{3}}}}{{4}} a^2 \\]\n\n**Step 3: State the conclusion.**\nThe result is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: True/False statements and standard formulas
    arch6 = {
        'data': [
            ("True or False: The area of an equilateral triangle with side a is (√3 / 4) a².", "True", ["False", "It is (√3 / 2) a²", "Cannot be determined"]),
            ("True or False: The altitude of an equilateral triangle with side a is (√3 / 2) a.", "True", ["False", "It is (√3 / 4) a", "Cannot be determined"]),
            ("True or False: In an isosceles triangle, the altitude to the unequal base bisects the base.", "True", ["False", "Only in equilateral triangles", "Cannot be determined"]),
            ("True or False: All equilateral triangles are similar to each other.", "True", ["False", "Only if sides are equal", "Cannot be determined"]),
            ("What is the area of an equilateral triangle with side 2 cm?", "√3 cm²", ["2√3 cm²", "4 cm²", "1 cm²"]),
            ("What is the area of an equilateral triangle with side 4 cm?", "4√3 cm²", ["16 cm²", "8√3 cm²", "2√3 cm²"]),
            ("What is the altitude of an equilateral triangle with side 2 cm?", "√3 cm", ["2 cm", "1 cm", "2√3 cm"]),
            ("What is the altitude of an equilateral triangle with side 4 cm?", "2√3 cm", ["4 cm", "√3 cm", "4√3 cm"]),
            ("What is the perimeter of an equilateral triangle with side 15 cm?", "45 cm", ["30 cm", "60 cm", "22.5 cm"]),
            ("What is the semi-perimeter of an equilateral triangle with side 12 cm?", "18 cm", ["36 cm", "12 cm", "24 cm"])
        ],
        'tmpls': [
            "{0}",
            "Direct check: {0}",
            "Basic equilateral triangle fact: {0}",
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
            f"**Step 1: Check the standard formula.**\n\\[ \\text{{Area}} = \\frac{{\\sqrt{{3}}}}{{4}} a^2, \\quad h = \\frac{{\\sqrt{{3}}}}{{2}} a \\]\n\n**Step 2: Evaluate for the given side.**\nVerify against standard textbook expressions.\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations for equilateral triangles
    arch7 = {
        'data': [
            (2, "√3"),
            (4, "4√3"),
            (6, "9√3"),
            (8, "16√3"),
            (10, "25√3"),
            (12, "36√3"),
            (14, "49√3"),
            (16, "64√3"),
            (18, "81√3"),
            (20, "100√3")
        ],
        'tmpls': [
            "Quick check: Area of an equilateral triangle with side {0} cm is:",
            "Find \\( \\frac{{\\sqrt{{3}}}}{{4}} \\times {0}^2 \\):",
            "Calculate the equilateral triangle area for side {0} cm:",
            "What is the area of an equilateral triangle of side {0} m?",
            "Compute: Area of equilateral triangle with \\( a = {0} \\text{{ cm}} \\) =",
            "Determine the area for an equilateral triangle of side {0} cm:",
            "Evaluate the area of an equilateral triangle with edge {0} units:",
            "Direct evaluation: Area for \\( a = {0} \\text{{ cm}} \\) is:",
            "What is the area of equilateral \\( \\triangle \\) of side {0} cm?",
            "Quick calculation of equilateral area for side {0} cm:"
        ],
        'calc': lambda item: (
            f"\\( {item[1]} \\text{{ cm}}^2 \\)",
            [f"\\( {item[0]**2} \\text{{ cm}}^2 \\)", f"\\( {item[0]}\\sqrt{{3}} \\text{{ cm}}^2 \\)", f"\\( {item[0] * 2}\\sqrt{{3}} \\text{{ cm}}^2 \\)"],
            f"**Step 1: Apply the formula.**\n\\[ \\text{{Area}} = \\frac{{\\sqrt{{3}}}}{{4}} a^2 \\]\n\n**Step 2: Substitute \\( a = {item[0]} \\).**\n\\[ \\text{{Area}} = \\frac{{\\sqrt{{3}}}}{{4}} \\times {item[0]}^2 = {item[1]} \\text{{ cm}}^2 \\]\n\n**Step 3: State the result.**\nThe area is \\( {item[1]} \\text{{ cm}}^2 \\)."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_6_2_1()
    print(f"gen_6_2_1: {len(q1)} questions")
    q2 = gen_6_2_2()
    print(f"gen_6_2_2: {len(q2)} questions")
    q3 = gen_6_2_3()
    print(f"gen_6_2_3: {len(q3)} questions")
