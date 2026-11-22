# scripts/build_cbse9_mgm_ch14_part1.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 14: Math of Space: Surface Area and Volume
Part 1:
- Subtopic 14.1.1: Slant height formula: l = √(r² + h²)
- Subtopic 14.1.2: Curved Surface Area = πrl
- Subtopic 14.1.3: Total Surface Area = πr(r + l)
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 240 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 14
CH_NAME = "Math of Space: Surface Area and Volume"

# ==============================================================================
# SUBTOPIC 14.1.1: Slant height formula: l = √(r² + h²)
# ==============================================================================
def gen_14_1_1():
    tc = "CBSE-9-MGM-14-14.1.1"
    tname = "Slant height formula: l = √(r² + h²)"

    # Arch 0: Given r and h (Pythagorean triples), find slant height l
    arch0 = {
        'data': [
            (3, 4, 5, "l = √(3^2 + 4^2) = √(9 + 16) = 5"),
            (6, 8, 10, "l = √(6^2 + 8^2) = √(36 + 64) = 10"),
            (5, 12, 13, "l = √(5^2 + 12^2) = √(25 + 144) = 13"),
            (8, 15, 17, "l = √(8^2 + 15^2) = √(64 + 225) = 17"),
            (7, 24, 25, "l = √(7^2 + 24^2) = √(49 + 576) = 25"),
            (9, 12, 15, "l = √(9^2 + 12^2) = √(81 + 144) = 15"),
            (12, 16, 20, "l = √(12^2 + 16^2) = √(144 + 256) = 20"),
            (10, 24, 26, "l = √(10^2 + 24^2) = √(100 + 576) = 26"),
            (15, 20, 25, "l = √(15^2 + 20^2) = √(225 + 400) = 25"),
            (20, 21, 29, "l = √(20^2 + 21^2) = √(400 + 441) = 29")
        ],
        'tmpls': [
            "A right circular cone has base radius \\(r = {0}\\text{{ cm}}\\) and vertical height \\(h = {1}\\text{{ cm}}\\). What is its slant height \\(l\\)?",
            "Find the slant height \\(l\\) of a right circular cone with radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\):",
            "In a cone, if \\(r = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\), calculate the slant height \\(l\\):",
            "What is the slant height of a right cone having base radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\)?:",
            "Calculate \\(l\\) for a right circular cone with dimensions \\(r = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\):",
            "Determine the slant height of a conical vessel with base radius \\({0}\\text{{ cm}}\\) and altitude \\({1}\\text{{ cm}}\\):",
            "If the radius and height of a cone are \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\) respectively, find \\(l\\):",
            "Evaluate the slant height \\(l = \\sqrt{{r^2 + h^2}}\\) for \\(r = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\):",
            "Find \\(l\\) of a right circular cone given \\(r = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\):",
            "Compute the slant height of a cone of base radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}\\)",
            [
                f"\\({item[0] + item[1]}\\text{{ cm}}\\)",
                f"\\({item[2] + 2}\\text{{ cm}}\\)",
                f"\\({item[2] - 2}\\text{{ cm}}\\)"
            ],
            f"**Step 1: State the slant height formula.**\nIn a right circular cone, \\(l = \\sqrt{{r^2 + h^2}}\\).\n\n**Step 2: Substitute the given dimensions.**\n\\(l = \\sqrt{{{item[0]}^2 + {item[1]}^2}} = \\sqrt{{{item[0]**2} + {item[1]**2}}} = \\sqrt{{{item[2]**2}}}\\).\n\n**Step 3: Calculate the slant height.**\n\\(l = {item[2]}\\text{{ cm}}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Given slant height l and radius r, find height h
    arch1 = {
        'data': [
            (5, 3, 4, "h = √(5^2 - 3^2) = √(25 - 9) = 4"),
            (10, 6, 8, "h = √(10^2 - 6^2) = √(100 - 36) = 8"),
            (13, 5, 12, "h = √(13^2 - 5^2) = √(169 - 25) = 12"),
            (17, 8, 15, "h = √(17^2 - 8^2) = √(289 - 64) = 15"),
            (25, 7, 24, "h = √(25^2 - 7^2) = √(625 - 49) = 24"),
            (15, 9, 12, "h = √(15^2 - 9^2) = √(225 - 81) = 12"),
            (20, 12, 16, "h = √(20^2 - 12^2) = √(400 - 144) = 16"),
            (26, 10, 24, "h = √(26^2 - 10^2) = √(676 - 100) = 24"),
            (25, 15, 20, "h = √(25^2 - 15^2) = √(625 - 225) = 20"),
            (29, 20, 21, "h = √(29^2 - 20^2) = √(841 - 400) = 21")
        ],
        'tmpls': [
            "A cone has slant height \\(l = {0}\\text{{ cm}}\\) and base radius \\(r = {1}\\text{{ cm}}\\). What is its vertical height \\(h\\)?",
            "Find the vertical height \\(h\\) of a right circular cone with slant height \\({0}\\text{{ cm}}\\) and base radius \\({1}\\text{{ cm}}\\):",
            "In a cone, if \\(l = {0}\\text{{ cm}}\\) and \\(r = {1}\\text{{ cm}}\\), calculate height \\(h\\):",
            "What is the height of a conical tent having slant height \\({0}\\text{{ cm}}\\) and base radius \\({1}\\text{{ cm}}\\)?:",
            "Calculate \\(h\\) for a cone given \\(l = {0}\\text{{ cm}}\\) and \\(r = {1}\\text{{ cm}}\\):",
            "Determine the vertical altitude of a cone with slant height \\({0}\\text{{ cm}}\\) and radius \\({1}\\text{{ cm}}\\):",
            "If slant height is \\({0}\\text{{ cm}}\\) and radius is \\({1}\\text{{ cm}}\\), find the height \\(h\\) of the cone:",
            "Evaluate \\(h = \\sqrt{{l^2 - r^2}}\\) for \\(l = {0}\\text{{ cm}}\\) and \\(r = {1}\\text{{ cm}}\\):",
            "Find height \\(h\\) of a right circular cone having \\(l = {0}\\text{{ cm}}\\) and \\(r = {1}\\text{{ cm}}\\):",
            "Compute the altitude of a right cone with slant height \\({0}\\text{{ cm}}\\) and radius \\({1}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}\\)",
            [
                f"\\({item[0] - item[1]}\\text{{ cm}}\\)",
                f"\\({item[2] + 2}\\text{{ cm}}\\)",
                f"\\({item[2] - 2}\\text{{ cm}}\\)"
            ],
            f"**Step 1: State the formula connecting \\(h, l, r\\).**\nFrom \\(l^2 = r^2 + h^2\\), we have \\(h = \\sqrt{{l^2 - r^2}}\\).\n\n**Step 2: Substitute the known values.**\n\\(h = \\sqrt{{{item[0]}^2 - {item[1]}^2}} = \\sqrt{{{item[0]**2} - {item[1]**2}}} = \\sqrt{{{item[2]**2}}}\\).\n\n**Step 3: Calculate the vertical height.**\n\\(h = {item[2]}\\text{{ cm}}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Given slant height l and height h, find base radius r
    arch2 = {
        'data': [
            (5, 4, 3, "r = √(5^2 - 4^2) = 3"),
            (10, 8, 6, "r = √(10^2 - 8^2) = 6"),
            (13, 12, 5, "r = √(13^2 - 12^2) = 5"),
            (17, 15, 8, "r = √(17^2 - 15^2) = 8"),
            (25, 24, 7, "r = √(25^2 - 24^2) = 7"),
            (15, 12, 9, "r = √(15^2 - 12^2) = 9"),
            (20, 16, 12, "r = √(20^2 - 16^2) = 12"),
            (26, 24, 10, "r = √(26^2 - 24^2) = 10"),
            (25, 20, 15, "r = √(25^2 - 20^2) = 15"),
            (29, 21, 20, "r = √(29^2 - 21^2) = 20")
        ],
        'tmpls': [
            "A cone has slant height \\(l = {0}\\text{{ cm}}\\) and vertical height \\(h = {1}\\text{{ cm}}\\). What is its base radius \\(r\\)?",
            "Find the base radius \\(r\\) of a right circular cone with slant height \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\):",
            "In a cone, if \\(l = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\), calculate the radius \\(r\\):",
            "What is the radius of the circular base of a cone having slant height \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\)?:",
            "Calculate \\(r\\) for a cone given \\(l = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\):",
            "Determine the base radius of a conical heap with slant height \\({0}\\text{{ cm}}\\) and depth \\({1}\\text{{ cm}}\\):",
            "If slant height is \\({0}\\text{{ cm}}\\) and altitude is \\({1}\\text{{ cm}}\\), find the base radius \\(r\\):",
            "Evaluate \\(r = \\sqrt{{l^2 - h^2}}\\) for \\(l = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\):",
            "Find radius \\(r\\) of a right cone having \\(l = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\):",
            "Compute the radius of a cone with slant height \\({0}\\text{{ cm}}\\) and vertical height \\({1}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}\\)",
            [
                f"\\({item[0] - item[1]}\\text{{ cm}}\\)",
                f"\\({item[2] + 2}\\text{{ cm}}\\)",
                f"\\({item[2] - 2}\\text{{ cm}}\\)"
            ],
            f"**Step 1: State the formula for radius.**\n\\(r = \\sqrt{{l^2 - h^2}}\\).\n\n**Step 2: Substitute the known values.**\n\\(r = \\sqrt{{{item[0]}^2 - {item[1]}^2}} = \\sqrt{{{item[0]**2} - {item[1]**2}}} = \\sqrt{{{item[2]**2}}}\\).\n\n**Step 3: Calculate the base radius.**\n\\(r = {item[2]}\\text{{ cm}}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 3: Given diameter d and height h, find slant height l
    arch3 = {
        'data': [
            (6, 4, 3, 5, "d = 6 => r = 3. l = √(3^2 + 4^2) = 5"),
            (12, 8, 6, 10, "d = 12 => r = 6. l = √(6^2 + 8^2) = 10"),
            (10, 12, 5, 13, "d = 10 => r = 5. l = √(5^2 + 12^2) = 13"),
            (16, 15, 8, 17, "d = 16 => r = 8. l = √(8^2 + 15^2) = 17"),
            (14, 24, 7, 25, "d = 14 => r = 7. l = √(7^2 + 24^2) = 25"),
            (18, 12, 9, 15, "d = 18 => r = 9. l = √(9^2 + 12^2) = 15"),
            (24, 16, 12, 20, "d = 24 => r = 12. l = √(12^2 + 16^2) = 20"),
            (20, 24, 10, 26, "d = 20 => r = 10. l = √(10^2 + 24^2) = 26"),
            (30, 20, 15, 25, "d = 30 => r = 15. l = √(15^2 + 20^2) = 25"),
            (40, 21, 20, 29, "d = 40 => r = 20. l = √(20^2 + 21^2) = 29")
        ],
        'tmpls': [
            "The base diameter of a cone is \\({0}\\text{{ cm}}\\) and its vertical height is \\({1}\\text{{ cm}}\\). What is its slant height \\(l\\)?",
            "A conical tent has base diameter \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\). Find its slant height:",
            "Find the slant height of a right cone with diameter \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\):",
            "In a right circular cone, base diameter is \\({0}\\text{{ cm}}\\) and vertical height is \\({1}\\text{{ cm}}\\). Calculate \\(l\\):",
            "What is the slant height of a cone whose base diameter is \\({0}\\text{{ cm}}\\) and height is \\({1}\\text{{ cm}}\\)?:",
            "Calculate \\(l\\) for a cone with base diameter \\({0}\\text{{ cm}}\\) and altitude \\({1}\\text{{ cm}}\\):",
            "Determine the slant height of a right circular cone of diameter \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\):",
            "If base diameter is \\({0}\\text{{ cm}}\\) and height is \\({1}\\text{{ cm}}\\), evaluate the slant height \\(l\\):",
            "Evaluate \\(l\\) for a conical structure with diameter \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\):",
            "Compute the slant height of a cone having diameter \\({0}\\text{{ cm}}\\) and vertical height \\({1}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\text{{ cm}}\\)",
            [
                f"\\({item[0] + item[1]}\\text{{ cm}}\\)",
                f"\\({item[3] + 2}\\text{{ cm}}\\)",
                f"\\({item[2] + item[1]}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Find the base radius from diameter.**\n\\(r = \\frac{{d}}{{2}} = \\frac{{{item[0]}}}{{2}} = {item[2]}\\text{{ cm}}\\).\n\n**Step 2: Use the slant height formula.**\n\\(l = \\sqrt{{r^2 + h^2}} = \\sqrt{{{item[2]}^2 + {item[1]}^2}} = \\sqrt{{{item[2]**2} + {item[1]**2}}} = \\sqrt{{{item[3]**2}}}\\).\n\n**Step 3: Calculate \\(l\\).**\n\\(l = {item[3]}\\text{{ cm}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Right-Angled Triangle Revolved to Form a Cone
    arch4 = {
        'data': [
            (5, 12, 13, 12, "Revolving about side 12 cm gives h = 12, r = 5, l = 13"),
            (3, 4, 5, 4, "Revolving about side 4 cm gives h = 4, r = 3, l = 5"),
            (6, 8, 10, 8, "Revolving about side 8 cm gives h = 8, r = 6, l = 10"),
            (8, 15, 17, 15, "Revolving about side 15 cm gives h = 15, r = 8, l = 17"),
            (7, 24, 25, 24, "Revolving about side 24 cm gives h = 24, r = 7, l = 25"),
            (9, 12, 15, 12, "Revolving about side 12 cm gives h = 12, r = 9, l = 15"),
            (12, 16, 20, 16, "Revolving about side 16 cm gives h = 16, r = 12, l = 20"),
            (10, 24, 26, 24, "Revolving about side 24 cm gives h = 24, r = 10, l = 26"),
            (15, 20, 25, 20, "Revolving about side 20 cm gives h = 20, r = 15, l = 25"),
            (20, 21, 29, 21, "Revolving about side 21 cm gives h = 21, r = 20, l = 29")
        ],
        'tmpls': [
            "A right triangle with sides \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\) containing the right angle is revolved about the side of length \\({3}\\text{{ cm}}\\). What is the slant height of the cone so formed?",
            "If a right triangle with legs \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\) is rotated about its leg \\({3}\\text{{ cm}}\\), what is the slant height of the resulting cone?",
            "A cone is generated by revolving a right-angled triangle having legs \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\) about side \\({3}\\text{{ cm}}\\). Find its slant height \\(l\\):",
            "What is the slant height of the cone formed by revolving a right-angled triangle of sides \\({0}\\text{{ cm}}, {1}\\text{{ cm}}\\) and hypotenuse \\({2}\\text{{ cm}}\\) about its side \\({3}\\text{{ cm}}\\)?:",
            "Calculate the slant height of the cone generated by rotating a right-angled triangle with hypotenuse \\({2}\\text{{ cm}}\\) about leg \\({3}\\text{{ cm}}\\):",
            "Determine the slant height \\(l\\) of a solid cone formed by rotating a right triangle (legs \\({0}\\text{{ cm}}, {1}\\text{{ cm}}\\)) about side \\({3}\\text{{ cm}}\\):",
            "A right triangle with hypotenuse \\({2}\\text{{ cm}}\\) is rotated about one of its legs. The slant height of the cone formed is:",
            "Find the slant height of the cone produced by rotating a right triangle with perpendicular sides \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\):",
            "Evaluate the slant height \\(l\\) of the cone swept by revolving a right triangle with hypotenuse \\({2}\\text{{ cm}}\\):",
            "When a right triangle of legs \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\) is revolved about side \\({3}\\text{{ cm}}\\), its slant height is:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}\\)",
            [
                f"\\({item[3]}\\text{{ cm}}\\)",
                f"\\({item[0]}\\text{{ cm}}\\)",
                f"\\({item[2] + 2}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Identify the roles of the triangle's sides.**\nWhen the right triangle is revolved about the side \\({3}\\text{{ cm}}\\) (which becomes the vertical height \\(h = {3}\\text{{ cm}}\\)), the other perpendicular side \\({item[0]}\\text{{ cm}}\\) becomes the base radius \\(r = {item[0]}\\text{{ cm}}\\).\n\n**Step 2: Relate the hypotenuse to slant height.**\nThe hypotenuse of the right triangle generates the curved surface and becomes the slant height \\(l\\).\n\n**Step 3: State the slant height.**\n\\(l = \\sqrt{{{item[0]}^2 + {item[1]}^2}} = {item[2]}\\text{{ cm}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 5: Trigonometric Ratios / Semi-Vertical Angle of Cone
    arch5 = {
        'data': [
            (3, 4, 5, "\\frac{3}{5}", "\\sin \\alpha = r/l = 3/5"),
            (5, 12, 13, "\\frac{5}{13}", "\\sin \\alpha = r/l = 5/13"),
            (8, 15, 17, "\\frac{8}{17}", "\\sin \\alpha = r/l = 8/17"),
            (7, 24, 25, "\\frac{7}{25}", "\\sin \\alpha = r/l = 7/25"),
            (6, 8, 10, "\\frac{3}{5}", "\\sin \\alpha = 6/10 = 3/5"),
            (9, 12, 15, "\\frac{3}{5}", "\\sin \\alpha = 9/15 = 3/5"),
            (12, 16, 20, "\\frac{3}{5}", "\\sin \\alpha = 12/20 = 3/5"),
            (10, 24, 26, "\\frac{5}{13}", "\\sin \\alpha = 10/26 = 5/13"),
            (15, 20, 25, "\\frac{3}{5}", "\\sin \\alpha = 15/25 = 3/5"),
            (20, 21, 29, "\\frac{20}{29}", "\\sin \\alpha = 20/29")
        ],
        'tmpls': [
            "In a right circular cone of radius \\(r = {0}\\text{{ cm}}\\) and vertical height \\(h = {1}\\text{{ cm}}\\), what is the sine of its semi-vertical angle \\(\\alpha\\)?",
            "If \\(\\alpha\\) is the semi-vertical angle of a cone with \\(r = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\), find \\(\\sin \\alpha\\):",
            "Calculate \\(\\sin \\alpha\\) where \\(\\alpha\\) is the semi-vertical angle of a cone with radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\):",
            "What is the value of \\(\\sin \\alpha\\) for a cone having base radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\)?:",
            "For a cone of dimensions \\(r = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\), find the ratio \\(\\frac{{r}}{{l}}\\) (which equals \\(\\sin \\alpha\\)):",
            "Determine \\(\\sin \\alpha\\) in a right circular cone having \\(r = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\):",
            "Evaluate \\(\\sin \\alpha = \\frac{{r}}{{l}}\\) for a cone with radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\):",
            "Find \\(\\sin \\alpha\\) of the cone with base radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\):",
            "Compute the ratio \\(\\frac{{r}}{{l}}\\) representing the sine of the semi-vertical angle for \\(r = {0}\\text{{ cm}}, h = {1}\\text{{ cm}}\\):",
            "In a cone of radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\), \\(\\sin \\alpha\\) is:"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\)",
            [
                f"\\({item[1]}/{item[2]}\\)",
                "\\(1\\)",
                "\\(\\frac{1}{2}\\)"
            ],
            f"**Step 1: Calculate the slant height \\(l\\).**\n\\(l = \\sqrt{{r^2 + h^2}} = \\sqrt{{{item[0]}^2 + {item[1]}^2}} = {item[2]}\\text{{ cm}}\\).\n\n**Step 2: Write the definition of the semi-vertical angle \\(\\alpha\\).**\nIn the axial right-angled triangle, \\(\\sin \\alpha = \\frac{{\\text{{opposite}}}}{{\\text{{hypotenuse}}}} = \\frac{{r}}{{l}}\\).\n\n**Step 3: Calculate \\(\\sin \\alpha\\).**\n\\(\\sin \\alpha = \\frac{{{item[0]}}}{{{item[2]}}} = {item[3]}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 6: Percentage Change / Scaling in Slant Height
    arch6 = {
        'data': [
            (2, 4, "If r and h are doubled, l is doubled: √( (2r)^2 + (2h)^2 ) = 2l"),
            (3, 9, "If r and h are tripled, l is tripled: √( (3r)^2 + (3h)^2 ) = 3l"),
            (4, 16, "If r and h are quadrupled, l is multiplied by 4"),
            (0.5, 0.25, "If r and h are halved, l is halved"),
            (10, 100, "If r and h are increased by factor 10, l increases by factor 10"),
            (5, 25, "If r and h are scaled by 5, l is scaled by 5"),
            (1.5, 2.25, "If r and h are increased by 50% (factor 1.5), l is increased by 50%"),
            (2.5, 6.25, "If r and h are scaled by 2.5, l is scaled by 2.5"),
            (0.1, 0.01, "If r and h are scaled by 0.1, l is scaled by 0.1"),
            (1, 1, "If dimensions remain unchanged, slant height is unchanged")
        ],
        'tmpls': [
            "If both the base radius and vertical height of a right circular cone are multiplied by a factor of \\({0}\\), by what factor does its slant height \\(l\\) change?",
            "When both \\(r\\) and \\(h\\) of a cone are scaled by \\({0}\\), the new slant height \\(l'\\) is how many times the original \\(l\\)?",
            "If both radius and height of a cone are changed by a factor of \\({0}\\), what is the factor of change in slant height?",
            "By what multiple does the slant height increase if both radius and altitude are multiplied by \\({0}\\)?",
            "What happens to the slant height \\(l\\) of a cone if both \\(r\\) and \\(h\\) are multiplied by \\({0}\\)?",
            "Determine the factor by which slant height \\(l\\) scales when both \\(r\\) and \\(h\\) are multiplied by \\({0}\\):",
            "If the radius and height of a cone are both scaled by \\({0}\\), the new slant height is:",
            "Evaluate the scaling factor for slant height when both \\(r\\) and \\(h\\) are multiplied by \\({0}\\):",
            "Calculate the new slant height multiple if \\(r' = {0}r\\) and \\(h' = {0}h\\):",
            "When the linear dimensions \\(r\\) and \\(h\\) of a cone are multiplied by \\({0}\\), slant height \\(l\\) is multiplied by:"
        ],
        'calc': lambda item: (
            f"Multiplied by \\({item[0]}\\)",
            [
                f"Multiplied by \\({item[1]}\\)",
                f"Multiplied by \\({item[0]**2}\\)",
                "Remains unchanged"
            ],
            f"**Step 1: Write the new slant height formula.**\n\\(l' = \\sqrt{{(r')^2 + (h')^2}} = \\sqrt{{({item[0]}r)^2 + ({item[0]}h)^2}}\\).\n\n**Step 2: Factor out the scalar.**\n\\(l' = \\sqrt{{{item[0]}^2 (r^2 + h^2)}} = {item[0]} \\sqrt{{r^2 + h^2}} = {item[0]}l\\).\n\n**Step 3: Conclude the scaling factor.**\nThe slant height is **multiplied by \\({item[0]}\\)**."
        ),
        'diff': 'medium'
    }

    # Arch 7: Definitions: Vertical Height vs Slant Height
    arch7 = {
        'data': [
            ("Slant height (l)", "Distance from the vertex to any point on the circular base boundary", "l = √(r² + h²)"),
            ("Vertical height (h)", "Perpendicular distance from the vertex to the center of the base", "Altitude of the cone"),
            ("Radius (r)", "Distance from the center of the base to any point on the circular boundary", "Base radius"),
            ("Right circular cone", "Cone whose axis is perpendicular to its circular base", "Symmetric cone"),
            ("Apex / Vertex", "The fixed point opposite to the circular base", "Top vertex of cone"),
            ("Generatrix", "The slant line segment that sweeps out the cone's curved surface", "Generates the cone"),
            ("Hypotenuse of axial triangle", "Slant height l is always greater than both r and h (l > h and l > r)", "Inequality in right triangle"),
            ("l² = r² + h²", "Fundamental Pythagorean relation connecting the three linear dimensions of a cone", "Geometric foundation"),
            ("Axis of the cone", "Line segment joining the vertex to the center of the circular base", "Line of rotational symmetry"),
            ("Curved surface of cone", "Can be unrolled into a sector of a circle of radius l", "Development of conical surface")
        ],
        'tmpls': [
            "In a right circular cone, what is the geometric definition of {0}?",
            "Which of the following correctly describes the {0} of a right circular cone?",
            "What does {0} represent in the geometry of a cone?",
            "Define the term {0} in a right circular cone:",
            "Which statement precisely defines the {0} of a right circular cone?",
            "In conical geometry, {0} is defined as:",
            "Identify the correct description for {0} of a right cone:",
            "What is meant by {0} in a right circular cone?",
            "The term {0} in a right circular cone refers to:",
            "How is {0} defined in the context of a cone?"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The perimeter of the base circle",
                "The total surface area divided by the radius",
                "The angle between the base and the slant surface"
            ],
            f"**Step 1: Understand the geometry of a right circular cone.**\n{item[0]}.\n\n**Step 2: Recall the formal definition.**\n{item[1]}.\n\n**Step 3: Note the mathematical relationship.**\n{item[2]}."
        ),
        'diff': 'easy'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 14.1.2: Curved Surface Area = πrl
# ==============================================================================
def gen_14_1_2():
    tc = "CBSE-9-MGM-14-14.1.2"
    tname = "Curved Surface Area = πrl"

    # Arch 0: Direct CSA calculation with r and l (using π = 22/7)
    arch0 = {
        'data': [
            (7, 10, 220, "CSA = (22/7) * 7 * 10 = 220"),
            (7, 14, 308, "CSA = (22/7) * 7 * 14 = 308"),
            (14, 15, 660, "CSA = (22/7) * 14 * 15 = 660"),
            (7, 25, 550, "CSA = (22/7) * 7 * 25 = 550"),
            (21, 10, 660, "CSA = (22/7) * 21 * 10 = 660"),
            (14, 20, 880, "CSA = (22/7) * 14 * 20 = 880"),
            (7, 12, 264, "CSA = (22/7) * 7 * 12 = 264"),
            (3.5, 10, 110, "CSA = (22/7) * 3.5 * 10 = 110"),
            (14, 25, 1100, "CSA = (22/7) * 14 * 25 = 1100"),
            (28, 15, 1320, "CSA = (22/7) * 28 * 15 = 1320")
        ],
        'tmpls': [
            "Find the curved surface area of a right circular cone whose base radius is \\({0}\\text{{ cm}}\\) and slant height is \\({1}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "Calculate the curved surface area (CSA) of a cone with \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\):",
            "What is the curved surface area of a cone having radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\)?:",
            "In a right cone, \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\). Determine its curved surface area:",
            "Compute the CSA of a conical shape with base radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "Determine the lateral surface area of a cone of radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "Evaluate \\(\\text{{CSA}} = \\pi r l\\) for \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\):",
            "A right circular cone has \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\). Find its curved surface area:",
            "Find the lateral area of a right cone having \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\):",
            "Calculate the curved surface area of a cone with radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[2] + 20}\\text{{ cm}}^2\\)",
                f"\\({item[2] - 20}\\text{{ cm}}^2\\)",
                f"\\({item[0] * item[1]}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: State the formula for Curved Surface Area of a cone.**\n\\(\\text{{CSA}} = \\pi r l\\).\n\n**Step 2: Substitute the given dimensions.**\n\\(\\text{{CSA}} = \\frac{{22}}{{7}} \\times {item[0]} \\times {item[1]}\\).\n\n**Step 3: Calculate the area.**\n\\(\\text{{CSA}} = {item[2]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Given CSA and slant height l, find radius r
    arch1 = {
        'data': [
            (220, 10, 7, "r = 220 / ((22/7)*10) = 7"),
            (308, 14, 7, "r = 308 / ((22/7)*14) = 7"),
            (660, 15, 14, "r = 660 / ((22/7)*15) = 14"),
            (550, 25, 7, "r = 550 / ((22/7)*25) = 7"),
            (880, 20, 14, "r = 880 / ((22/7)*20) = 14"),
            (264, 12, 7, "r = 264 / ((22/7)*12) = 7"),
            (110, 10, 3.5, "r = 110 / ((22/7)*10) = 3.5"),
            (1100, 25, 14, "r = 1100 / ((22/7)*25) = 14"),
            (1320, 15, 28, "r = 1320 / ((22/7)*15) = 28"),
            (330, 15, 7, "r = 330 / ((22/7)*15) = 7")
        ],
        'tmpls': [
            "The curved surface area of a cone is \\({0}\\text{{ cm}}^2\\) and its slant height is \\({1}\\text{{ cm}}\\). What is its base radius? (use \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "A cone has \\(\\text{{CSA}} = {0}\\text{{ cm}}^2\\) and slant height \\({1}\\text{{ cm}}\\). Find the radius of its base:",
            "Find the radius of a cone having curved surface area \\({0}\\text{{ cm}}^2\\) and slant height \\({1}\\text{{ cm}}\\):",
            "Calculate \\(r\\) for a cone with \\(\\text{{CSA}} = {0}\\text{{ cm}}^2\\) and \\(l = {1}\\text{{ cm}}\\):",
            "Determine the base radius of a conical tent if its curved area is \\({0}\\text{{ cm}}^2\\) and slant height is \\({1}\\text{{ cm}}\\):",
            "What is the base radius of a cone with curved surface \\({0}\\text{{ cm}}^2\\) and slant height \\({1}\\text{{ cm}}\\)?:",
            "Evaluate \\(r = \\frac{{\\text{{CSA}}}}{{\\pi l}}\\) for \\(\\text{{CSA}} = {0}\\text{{ cm}}^2\\) and \\(l = {1}\\text{{ cm}}\\):",
            "Find \\(r\\) given \\(\\text{{CSA}} = {0}\\text{{ cm}}^2\\) and \\(l = {1}\\text{{ cm}}\\) for a right cone:",
            "Compute the radius of the base of a cone with \\(\\text{{CSA}} = {0}\\text{{ cm}}^2\\) and \\(l = {1}\\text{{ cm}}\\):",
            "If curved surface area is \\({0}\\text{{ cm}}^2\\) and slant height is \\({1}\\text{{ cm}}\\), find the base radius:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}\\)",
            [
                f"\\({item[2] + 2}\\text{{ cm}}\\)",
                f"\\({item[2] - 2}\\text{{ cm}}\\)",
                f"\\({item[1]}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Set up the formula for Curved Surface Area.**\n\\(\\text{{CSA}} = \\pi r l \\implies r = \\frac{{\\text{{CSA}}}}{{\\pi l}}\\).\n\n**Step 2: Substitute the values.**\n\\(r = \\frac{{{item[0]}}}{{\\frac{{22}}{{7}} \\times {item[1]}}} = \\frac{{{item[0]} \\times 7}}{{22 \\times {item[1]}}}\\).\n\n**Step 3: Calculate the radius.**\n\\(r = {item[2]}\\text{{ cm}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Given CSA and radius r, find slant height l
    arch2 = {
        'data': [
            (220, 7, 10, "l = 220 / ((22/7)*7) = 10"),
            (308, 7, 14, "l = 308 / ((22/7)*7) = 14"),
            (660, 14, 15, "l = 660 / ((22/7)*14) = 15"),
            (550, 7, 25, "l = 550 / ((22/7)*7) = 25"),
            (880, 14, 20, "l = 880 / ((22/7)*14) = 20"),
            (264, 7, 12, "l = 264 / ((22/7)*7) = 12"),
            (110, 3.5, 10, "l = 110 / ((22/7)*3.5) = 10"),
            (1100, 14, 25, "l = 1100 / ((22/7)*14) = 25"),
            (1320, 28, 15, "l = 1320 / ((22/7)*28) = 15"),
            (330, 7, 15, "l = 330 / ((22/7)*7) = 15")
        ],
        'tmpls': [
            "The curved surface area of a cone is \\({0}\\text{{ cm}}^2\\) and its base radius is \\({1}\\text{{ cm}}\\). What is its slant height? (use \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "A cone has \\(\\text{{CSA}} = {0}\\text{{ cm}}^2\\) and base radius \\({1}\\text{{ cm}}\\). Find its slant height:",
            "Find the slant height of a cone having curved surface area \\({0}\\text{{ cm}}^2\\) and radius \\({1}\\text{{ cm}}\\):",
            "Calculate \\(l\\) for a cone with \\(\\text{{CSA}} = {0}\\text{{ cm}}^2\\) and \\(r = {1}\\text{{ cm}}\\):",
            "Determine the slant height of a conical tent if its curved area is \\({0}\\text{{ cm}}^2\\) and radius is \\({1}\\text{{ cm}}\\):",
            "What is the slant height of a cone with curved surface \\({0}\\text{{ cm}}^2\\) and base radius \\({1}\\text{{ cm}}\\)?:",
            "Evaluate \\(l = \\frac{{\\text{{CSA}}}}{{\\pi r}}\\) for \\(\\text{{CSA}} = {0}\\text{{ cm}}^2\\) and \\(r = {1}\\text{{ cm}}\\):",
            "Find \\(l\\) given \\(\\text{{CSA}} = {0}\\text{{ cm}}^2\\) and \\(r = {1}\\text{{ cm}}\\) for a right cone:",
            "Compute the slant height of a cone with \\(\\text{{CSA}} = {0}\\text{{ cm}}^2\\) and \\(r = {1}\\text{{ cm}}\\):",
            "If curved surface area is \\({0}\\text{{ cm}}^2\\) and radius is \\({1}\\text{{ cm}}\\), find the slant height:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}\\)",
            [
                f"\\({item[2] + 2}\\text{{ cm}}\\)",
                f"\\({item[2] - 2}\\text{{ cm}}\\)",
                f"\\({item[1]}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Express slant height from the CSA formula.**\n\\(\\text{{CSA}} = \\pi r l \\implies l = \\frac{{\\text{{CSA}}}}{{\\pi r}}\\).\n\n**Step 2: Substitute the known values.**\n\\(l = \\frac{{{item[0]}}}{{\\frac{{22}}{{7}} \\times {item[1]}}} = \\frac{{{item[0]} \\times 7}}{{22 \\times {item[1]}}}\\).\n\n**Step 3: Calculate the slant height.**\n\\(l = {item[2]}\\text{{ cm}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Conical Tent Canvas Area & Cost
    arch3 = {
        'data': [
            (7, 24, 25, 550, 70, 38500, "r=7, h=24 => l=25. CSA = 550 m^2. Cost = 550 * 70 = ₹38,500"),
            (14, 48, 50, 2200, 50, 110000, "r=14, h=48 => l=50. CSA = 2200 m^2. Cost = ₹1,10,000"),
            (6, 8, 10, 188.57, 100, 18857, "r=6, h=8 => l=10. CSA = π*6*10 = 60π m^2"),
            (7, 10, 10, 220, 25, 5500, "r=7, l=10. CSA = 220 m^2. Cost = 220 * 25 = ₹5500"),
            (14, 20, 20, 880, 40, 35200, "r=14, l=20. CSA = 880 m^2. Cost = 880 * 40 = ₹35,200"),
            (7, 25, 25, 550, 50, 27500, "r=7, l=25. CSA = 550 m^2. Cost = 550 * 50 = ₹27,500"),
            (21, 20, 29, 1914, 30, 57420, "r=21, h=20 => l=29. CSA = (22/7)*21*29 = 1914. Cost = ₹57,420"),
            (14, 15, 15, 660, 80, 52800, "r=14, l=15. CSA = 660 m^2. Cost = 660 * 80 = ₹52,800"),
            (7, 14, 14, 308, 60, 18480, "r=7, l=14. CSA = 308 m^2. Cost = 308 * 60 = ₹18,480"),
            (3.5, 10, 10, 110, 100, 11000, "r=3.5, l=10. CSA = 110 m^2. Cost = 110 * 100 = ₹11,000")
        ],
        'tmpls': [
            "A conical tent has base radius \\({0}\\text{{ m}}\\) and slant height \\({2}\\text{{ m}}\\). Find the cost of canvas required to make the tent at the rate of ₹\\({4}\\) per \\(\\text{{m}}^2\\) (use \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "What is the cost of canvas needed to erect a conical tent of radius \\({0}\\text{{ m}}\\) and slant height \\({2}\\text{{ m}}\\) at ₹\\({4}/\\text{{m}}^2\\)?",
            "Find the cost of canvas for a conical tent with \\(r = {0}\\text{{ m}}\\) and \\(l = {2}\\text{{ m}}\\) at ₹\\({4}\\) per square metre:",
            "Calculate the expenditure on canvas to construct a conical tent with radius \\({0}\\text{{ m}}\\) and slant height \\({2}\\text{{ m}}\\) at ₹\\({4}/\\text{{m}}^2\\):",
            "How much will it cost to cover a conical tent of radius \\({0}\\text{{ m}}\\) and slant height \\({2}\\text{{ m}}\\) with canvas at ₹\\({4}\\) per \\(\\text{{m}}^2\\)?",
            "Determine the total cost of canvas at ₹\\({4}/\\text{{m}}^2\\) for a conical tent with base radius \\({0}\\text{{ m}}\\) and slant height \\({2}\\text{{ m}}\\):",
            "Evaluate the cost of canvas required for a cone with \\(r = {0}\\text{{ m}}\\) and \\(l = {2}\\text{{ m}}\\) at ₹\\({4}\\) per square metre:",
            "A circus tent is conical with \\(r = {0}\\text{{ m}}\\) and \\(l = {2}\\text{{ m}}\\). Find the canvas cost at ₹\\({4}/\\text{{m}}^2\\):",
            "Compute the cost of canvas at ₹\\({4}\\) per \\(\\text{{m}}^2\\) for a conical pavilion with \\(r = {0}\\text{{ m}}\\) and \\(l = {2}\\text{{ m}}\\):",
            "Find the cost of canvas for making a conical tent of radius \\({0}\\text{{ m}}\\) and slant height \\({2}\\text{{ m}}\\) at rate ₹\\({4}/\\text{{m}}^2\\):"
        ],
        'calc': lambda item: (
            f"₹\\({item[5]}\\)",
            [
                f"₹\\({item[5] + 1000}\\)",
                f"₹\\({item[5] - 1000}\\)",
                f"₹\\({item[3]}\\)"
            ],
            f"**Step 1: Calculate the canvas area (Curved Surface Area).**\nA tent has no canvas on the ground (base is open), so only the curved surface area is required.\n\\(\\text{{CSA}} = \\pi r l = \\frac{{22}}{{7}} \\times {item[0]} \\times {item[2]} = {item[3]}\\text{{ m}}^2\\).\n\n**Step 2: Multiply by the cost per square metre.**\n\\(\\text{{Total Cost}} = \\text{{CSA}} \\times \\text{{rate}} = {item[3]} \\times {item[4]}\\).\n\n**Step 3: State the final cost.**\nTotal Cost \\(= \\text{{₹}}{item[5]}\\)."
        ),
        'diff': 'hard'
    }

    # Arch 4: Given diameter and slant height, calculate CSA
    arch4 = {
        'data': [
            (14, 10, 7, 220, "d = 14 => r = 7. CSA = (22/7)*7*10 = 220"),
            (14, 14, 7, 308, "d = 14 => r = 7. CSA = (22/7)*7*14 = 308"),
            (28, 15, 14, 660, "d = 28 => r = 14. CSA = (22/7)*14*15 = 660"),
            (14, 25, 7, 550, "d = 14 => r = 7. CSA = (22/7)*7*25 = 550"),
            (42, 10, 21, 660, "d = 42 => r = 21. CSA = (22/7)*21*10 = 660"),
            (28, 20, 14, 880, "d = 28 => r = 14. CSA = (22/7)*14*20 = 880"),
            (14, 12, 7, 264, "d = 14 => r = 7. CSA = (22/7)*7*12 = 264"),
            (7, 10, 3.5, 110, "d = 7 => r = 3.5. CSA = (22/7)*3.5*10 = 110"),
            (28, 25, 14, 1100, "d = 28 => r = 14. CSA = (22/7)*14*25 = 1100"),
            (56, 15, 28, 1320, "d = 56 => r = 28. CSA = (22/7)*28*15 = 1320")
        ],
        'tmpls': [
            "Diameter of the base of a cone is \\({0}\\text{{ cm}}\\) and its slant height is \\({1}\\text{{ cm}}\\). Find its curved surface area (use \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "A right circular cone has base diameter \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\). What is its curved surface area?",
            "Find the CSA of a cone having diameter \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "Calculate the curved surface area of a cone with base diameter \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "Determine the curved surface area of a conical dome of diameter \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "What is the lateral area of a cone having base diameter \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\)?:",
            "Evaluate \\(\\text{{CSA}}\\) for a cone with diameter \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "Compute the curved surface area of a right cone with \\(d = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\):",
            "If the base diameter is \\({0}\\text{{ cm}}\\) and slant height is \\({1}\\text{{ cm}}\\), find the cone's curved surface area:",
            "Find the curved surface area of a cone with base diameter \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[3] * 2}\\text{{ cm}}^2\\)",
                f"\\({item[3] + 20}\\text{{ cm}}^2\\)",
                f"\\({item[0] * item[1]}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: Find the radius from diameter.**\n\\(r = \\frac{{d}}{{2}} = \\frac{{{item[0]}}}{{2}} = {item[2]}\\text{{ cm}}\\).\n\n**Step 2: Apply the CSA formula.**\n\\(\\text{{CSA}} = \\pi r l = \\frac{{22}}{{7}} \\times {item[2]} \\times {item[1]}\\).\n\n**Step 3: Calculate the area.**\n\\(\\text{{CSA}} = {item[3]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'easy'
    }

    # Arch 5: Ratio of CSAs of Two Cones
    arch5 = {
        'data': [
            ("1 : 2", "2 : 1", 1, 2, 2, 1, "1 : 1", "(1*2)/(2*1) = 1/1 => 1 : 1"),
            ("2 : 3", "3 : 4", 2, 3, 3, 4, "1 : 2", "(2*3)/(3*4) = 6/12 = 1/2 => 1 : 2"),
            ("3 : 5", "5 : 3", 3, 5, 5, 3, "1 : 1", "(3*5)/(5*3) = 1/1 => 1 : 1"),
            ("1 : 3", "3 : 2", 1, 3, 3, 2, "1 : 2", "(1*3)/(3*2) = 3/6 = 1/2 => 1 : 2"),
            ("2 : 1", "1 : 4", 2, 1, 1, 4, "1 : 2", "(2*1)/(1*4) = 2/4 = 1/2 => 1 : 2"),
            ("4 : 5", "5 : 2", 4, 5, 5, 2, "2 : 1", "(4*5)/(5*2) = 20/10 = 2/1 => 2 : 1"),
            ("3 : 4", "4 : 1", 3, 4, 4, 1, "3 : 1", "(3*4)/(4*1) = 12/4 = 3/1 => 3 : 1"),
            ("1 : 4", "2 : 1", 1, 4, 2, 1, "1 : 2", "(1*2)/(4*1) = 2/4 = 1/2 => 1 : 2"),
            ("3 : 2", "2 : 3", 3, 2, 2, 3, "1 : 1", "(3*2)/(2*3) = 1/1 => 1 : 1"),
            ("5 : 2", "2 : 5", 5, 2, 2, 5, "1 : 1", "(5*2)/(2*5) = 1/1 => 1 : 1")
        ],
        'tmpls': [
            "The base radii of two cones are in the ratio \\({0}\\) and their slant heights are in the ratio \\({1}\\). What is the ratio of their curved surface areas?",
            "If the ratio of radii of two cones is \\({0}\\) and the ratio of their slant heights is \\({1}\\), find the ratio of their CSAs:",
            "Find the ratio of the curved surface areas of two cones having radii in ratio \\({0}\\) and slant heights in ratio \\({1}\\):",
            "Calculate \\(\\text{{CSA}}_1 : \\text{{CSA}}_2\\) for two cones with radius ratio \\({0}\\) and slant height ratio \\({1}\\):",
            "Two cones have radii proportioned as \\({0}\\) and slant heights as \\({1}\\). What is the proportion of their lateral surface areas?",
            "Determine the ratio of curved surface areas of two cones if their radii are in ratio \\({0}\\) and slant heights in ratio \\({1}\\):",
            "What is the ratio of the curved areas of two cones with radii in the ratio \\({0}\\) and slant heights in the ratio \\({1}\\)?",
            "Evaluate \\(\\frac{{\\text{{CSA}}_1}}{{\\text{{CSA}}_2}}\\) given \\(r_1 : r_2 = {0}\\) and \\(l_1 : l_2 = {1}\\):",
            "Compute the ratio of CSAs of two right cones whose radii are as \\({0}\\) and slant heights are as \\({1}\\):",
            "If radii of two cones are in ratio \\({0}\\) and their slant heights are in ratio \\({1}\\), the ratio of their curved surfaces is:"
        ],
        'calc': lambda item: (
            f"\\({item[6]}\\)",
            [
                f"\\({item[0]}\\)",
                f"\\({item[1]}\\)",
                "\\(1 : 4\\)" if item[6] != "1 : 4" else "\\(4 : 1\\)"
            ],
            f"**Step 1: Write the ratio of curved surface areas.**\n\\(\\frac{{\\text{{CSA}}_1}}{{\\text{{CSA}}_2}} = \\frac{{\\pi r_1 l_1}}{{\\pi r_2 l_2}} = \\left(\\frac{{r_1}}{{r_2}}\\right) \\times \\left(\\frac{{l_1}}{{l_2}}\\right)\\).\n\n**Step 2: Substitute the given ratios.**\n\\(\\frac{{\\text{{CSA}}_1}}{{\\text{{CSA}}_2}} = \\left(\\frac{{{item[2]}}}{{{item[3]}}}\\right) \\times \\left(\\frac{{{item[4]}}}{{{item[5]}}}\\right) = \\frac{{{item[2] * item[4]}}}{{{item[3] * item[5]}}}\\).\n\n**Step 3: Simplify the ratio.**\n{item[7]}.\nTherefore, the ratio is \\({item[6]}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 6: Given Base Circumference and Slant Height, Find CSA
    arch6 = {
        'data': [
            (44, 10, 7, 220, "2πr = 44 => r = 7. CSA = 1/2 * (2πr) * l = 1/2 * 44 * 10 = 220"),
            (44, 14, 7, 308, "CSA = 1/2 * 44 * 14 = 308"),
            (88, 15, 14, 660, "CSA = 1/2 * 88 * 15 = 660"),
            (44, 25, 7, 550, "CSA = 1/2 * 44 * 25 = 550"),
            (132, 10, 21, 660, "CSA = 1/2 * 132 * 10 = 660"),
            (88, 20, 14, 880, "CSA = 1/2 * 88 * 20 = 880"),
            (44, 12, 7, 264, "CSA = 1/2 * 44 * 12 = 264"),
            (22, 10, 3.5, 110, "CSA = 1/2 * 22 * 10 = 110"),
            (88, 25, 14, 1100, "CSA = 1/2 * 88 * 25 = 1100"),
            (176, 15, 28, 1320, "CSA = 1/2 * 176 * 15 = 1320")
        ],
        'tmpls': [
            "The circumference of the base of a cone is \\({0}\\text{{ cm}}\\) and its slant height is \\({1}\\text{{ cm}}\\). What is its curved surface area?",
            "A cone has base circumference \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\). Find its curved surface area:",
            "Find the curved surface area of a cone having base perimeter \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "Calculate the CSA of a cone with base circumference \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "What is the curved surface area of a conical hat whose base circumference is \\({0}\\text{{ cm}}\\) and slant height is \\({1}\\text{{ cm}}\\)?:",
            "Determine the CSA of a right circular cone of base perimeter \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "Evaluate \\(\\text{{CSA}} = \\frac{1}{2} \\times (2\\pi r) \\times l\\) for circumference \\({0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\):",
            "If base circumference of a cone is \\({0}\\text{{ cm}}\\) and slant height is \\({1}\\text{{ cm}}\\), find its CSA:",
            "Compute the curved area of a cone with perimeter of base \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "Find the lateral surface area of a cone given base perimeter \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[0] * item[1]}\\text{{ cm}}^2\\)",
                f"\\({item[3] + 20}\\text{{ cm}}^2\\)",
                f"\\({item[3] // 2}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: Relate base circumference to radius.**\n\\(2\\pi r = {item[0]}\\text{{ cm}}\\).\n\n**Step 2: Use the formula for CSA in terms of perimeter.**\n\\(\\text{{CSA}} = \\pi r l = \\frac{1}{2} \\times (2\\pi r) \\times l\\).\n\n**Step 3: Calculate the area.**\n\\(\\text{{CSA}} = \\frac{1}{2} \\times {item[0]} \\times {item[1]} = {item[3]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'medium'
    }

    # Arch 7: Sector of a Circle Rolled into a Cone
    arch7 = {
        'data': [
            (12, 120, 4, "Sector angle 120° of circle R = 12 cm gives l = 12 cm, 2πr = (120/360)*2π(12) => r = 4 cm"),
            (10, 216, 6, "Sector angle 216° of circle R = 10 cm gives l = 10 cm, r = (216/360)*10 = 6 cm"),
            (14, 180, 7, "Semicircular sheet of R = 14 cm bent into cone: l = 14 cm, r = 7 cm"),
            (20, 90, 5, "Quadrant of circle R = 20 cm: l = 20 cm, r = (90/360)*20 = 5 cm"),
            (15, 120, 5, "Sector angle 120° of circle R = 15 cm: l = 15 cm, r = 5 cm"),
            (21, 120, 7, "Sector angle 120° of circle R = 21 cm: l = 21 cm, r = 7 cm"),
            (18, 180, 9, "Semicircle of R = 18 cm: l = 18 cm, r = 9 cm"),
            (16, 90, 4, "Quadrant of R = 16 cm: l = 16 cm, r = 4 cm"),
            (24, 60, 4, "Sector angle 60° of circle R = 24 cm: l = 24 cm, r = (60/360)*24 = 4 cm"),
            (28, 180, 14, "Semicircle of R = 28 cm: l = 28 cm, r = 14 cm")
        ],
        'tmpls': [
            "A sector of a circle of radius \\({0}\\text{{ cm}}\\) with central angle \\({1}^\\circ\\) is rolled up to form a right circular cone. What is the base radius \\(r\\) of the cone?",
            "When a circular sector of radius \\({0}\\text{{ cm}}\\) and central angle \\({1}^\\circ\\) is bent to form a cone, what is the base radius of the cone?",
            "A sector of radius \\({0}\\text{{ cm}}\\) and angle \\({1}^\\circ\\) has its straight edges joined to form a cone. Find the radius of the cone's base:",
            "What is the base radius of the cone formed by rolling a sector of a circle of radius \\({0}\\text{{ cm}}\\) subtending \\({1}^\\circ\\) at the centre?",
            "Calculate base radius \\(r\\) of a cone constructed from a circular sector of radius \\({0}\\text{{ cm}}\\) and angle \\({1}^\\circ\\):",
            "Determine the base radius of the cone made by folding a sector of radius \\({0}\\text{{ cm}}\\) and angle \\({1}^\\circ\\):",
            "If a sector of radius \\({0}\\text{{ cm}}\\) with sector angle \\({1}^\\circ\\) is folded into a cone, what is the radius of the cone?",
            "Evaluate the base radius \\(r\\) of a cone formed from a circular sector with \\(R = {0}\\text{{ cm}}\\) and \\(\\theta = {1}^\\circ\\):",
            "Find the base radius of a cone made by curling a sector of radius \\({0}\\text{{ cm}}\\) and central angle \\({1}^\\circ\\):",
            "In folding a sector of radius \\({0}\\text{{ cm}}\\) and angle \\({1}^\\circ\\) into a cone, the radius of the resulting cone is:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}\\)",
            [
                f"\\({item[0]}\\text{{ cm}}\\)",
                f"\\({item[2] + 2}\\text{{ cm}}\\)",
                f"\\({item[2] * 2}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Understand the geometric transformation.**\nWhen a sector of radius \\(R\\) is folded into a cone:\n- The slant height \\(l\\) of the cone equals the radius of the sector (\\(l = R = {item[0]}\\text{{ cm}}\\)).\n- The arc length of the sector becomes the circumference of the base of the cone (\\(2\\pi r = \\text{{arc length}}\\)).\n\n**Step 2: Calculate the arc length of the sector.**\n\\(\\text{{Arc length}} = \\frac{{{item[1]}^\\circ}}{{360^\\circ}} \\times 2\\pi R = \\frac{{{item[1]}}}{{360}} \\times 2\\pi({item[0]})\\).\n\n**Step 3: Solve for \\(r\\).**\n\\(2\\pi r = \\frac{{{item[1]}}}{{360}} \\times 2\\pi({item[0]}) \\implies r = \\frac{{{item[1]}}}{{360}} \\times {item[0]} = {item[2]}\\text{{ cm}}\\)."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 14.1.3: Total Surface Area = πr(r + l)
# ==============================================================================
def gen_14_1_3():
    tc = "CBSE-9-MGM-14-14.1.3"
    tname = "Total Surface Area = πr(r + l)"

    # Arch 0: Direct TSA calculation with r and l (using π = 22/7)
    arch0 = {
        'data': [
            (7, 10, 17, 374, "TSA = (22/7) * 7 * (7 + 10) = 22 * 17 = 374"),
            (7, 14, 21, 462, "TSA = (22/7) * 7 * (7 + 14) = 22 * 21 = 462"),
            (14, 15, 29, 1276, "TSA = (22/7) * 14 * (14 + 15) = 44 * 29 = 1276"),
            (7, 25, 32, 704, "TSA = (22/7) * 7 * (7 + 25) = 22 * 32 = 704"),
            (21, 10, 31, 2046, "TSA = (22/7) * 21 * (21 + 10) = 66 * 31 = 2046"),
            (14, 20, 34, 1496, "TSA = (22/7) * 14 * (14 + 20) = 44 * 34 = 1496"),
            (7, 12, 19, 418, "TSA = (22/7) * 7 * (7 + 12) = 22 * 19 = 418"),
            (3.5, 10, 13.5, 148.5, "TSA = (22/7) * 3.5 * (3.5 + 10) = 11 * 13.5 = 148.5"),
            (14, 25, 39, 1716, "TSA = (22/7) * 14 * (14 + 25) = 44 * 39 = 1716"),
            (28, 15, 43, 3784, "TSA = (22/7) * 28 * (28 + 15) = 88 * 43 = 3784")
        ],
        'tmpls': [
            "Find the total surface area of a cone if its slant height is \\({1}\\text{{ cm}}\\) and radius of its base is \\({0}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "Calculate the total surface area (TSA) of a cone with \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\):",
            "What is the total surface area of a solid right circular cone having radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\)?:",
            "In a solid cone, \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\). Determine its total surface area:",
            "Compute the TSA of a solid cone with base radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "Determine the total surface area of a cone of radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "Evaluate \\(\\text{{TSA}} = \\pi r(r + l)\\) for \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\):",
            "A solid right circular cone has \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\). Find its total surface area:",
            "Find the total surface area of a closed cone having \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\):",
            "Calculate the total surface area of a solid cone with radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[3] + 20}\\text{{ cm}}^2\\)",
                f"\\({item[3] - 20}\\text{{ cm}}^2\\)",
                f"\\({item[0] * item[1]}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: State the formula for Total Surface Area of a cone.**\n\\(\\text{{TSA}} = \\pi r(r + l)\\).\n\n**Step 2: Substitute the known values.**\n\\(\\text{{TSA}} = \\frac{{22}}{{7}} \\times {item[0]} \\times ({item[0]} + {item[1]}) = \\frac{{22}}{{7}} \\times {item[0]} \\times {item[2]}\\).\n\n**Step 3: Calculate the area.**\n\\(\\text{{TSA}} = {item[3]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Given TSA and radius r, find slant height l
    arch1 = {
        'data': [
            (374, 7, 10, "TSA = 374 => 22*(7+l) = 374 => 7+l = 17 => l = 10"),
            (462, 7, 14, "22*(7+l) = 462 => 7+l = 21 => l = 14"),
            (1276, 14, 15, "44*(14+l) = 1276 => 14+l = 29 => l = 15"),
            (704, 7, 25, "22*(7+l) = 704 => 7+l = 32 => l = 25"),
            (2046, 21, 10, "66*(21+l) = 2046 => 21+l = 31 => l = 10"),
            (1496, 14, 20, "44*(14+l) = 1496 => 14+l = 34 => l = 20"),
            (418, 7, 12, "22*(7+l) = 418 => 7+l = 19 => l = 12"),
            (1716, 14, 25, "44*(14+l) = 1716 => 14+l = 39 => l = 25"),
            (3784, 28, 15, "88*(28+l) = 3784 => 28+l = 43 => l = 15"),
            (748, 7, 27, "22*(7+l) = 748 => 7+l = 34 => l = 27")
        ],
        'tmpls': [
            "The total surface area of a solid cone is \\({0}\\text{{ cm}}^2\\) and its base radius is \\({1}\\text{{ cm}}\\). What is its slant height? (use \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "A solid cone has \\(\\text{{TSA}} = {0}\\text{{ cm}}^2\\) and base radius \\({1}\\text{{ cm}}\\). Find its slant height:",
            "Find the slant height of a cone having total surface area \\({0}\\text{{ cm}}^2\\) and radius \\({1}\\text{{ cm}}\\):",
            "Calculate \\(l\\) for a cone with \\(\\text{{TSA}} = {0}\\text{{ cm}}^2\\) and \\(r = {1}\\text{{ cm}}\\):",
            "Determine the slant height of a solid cone if its total area is \\({0}\\text{{ cm}}^2\\) and radius is \\({1}\\text{{ cm}}\\):",
            "What is the slant height of a solid cone with total surface \\({0}\\text{{ cm}}^2\\) and base radius \\({1}\\text{{ cm}}\\)?:",
            "Evaluate \\(l\\) from \\(\\text{{TSA}} = \\pi r(r + l)\\) when \\(\\text{{TSA}} = {0}\\text{{ cm}}^2\\) and \\(r = {1}\\text{{ cm}}\\):",
            "Find \\(l\\) given \\(\\text{{TSA}} = {0}\\text{{ cm}}^2\\) and \\(r = {1}\\text{{ cm}}\\) for a right solid cone:",
            "Compute the slant height of a cone with \\(\\text{{TSA}} = {0}\\text{{ cm}}^2\\) and \\(r = {1}\\text{{ cm}}\\):",
            "If total surface area is \\({0}\\text{{ cm}}^2\\) and radius is \\({1}\\text{{ cm}}\\), find the slant height:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}\\)",
            [
                f"\\({item[2] + 2}\\text{{ cm}}\\)",
                f"\\({item[2] - 2}\\text{{ cm}}\\)",
                f"\\({item[1]}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Write down the TSA formula.**\n\\(\\text{{TSA}} = \\pi r(r + l)\\).\n\n**Step 2: Substitute the known values.**\n\\({item[0]} = \\frac{{22}}{{7}} \\times {item[1]} \\times ({item[1]} + l)\\).\n\n**Step 3: Solve for \\(l\\).**\n\\({item[1]} + l = \\frac{{{item[0]}}}{{\\frac{{22}}{{7}} \\times {item[1]}}} = {item[1] + item[2]}\\)\n\\(l = {item[1] + item[2]} - {item[1]} = {item[2]}\\text{{ cm}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Difference between TSA and CSA: Base Area
    arch2 = {
        'data': [
            (7, 154, "Base area = πr^2 = (22/7)*7*7 = 154 cm^2"),
            (14, 616, "Base area = πr^2 = (22/7)*14*14 = 616 cm^2"),
            (21, 1386, "Base area = πr^2 = (22/7)*21*21 = 1386 cm^2"),
            (3.5, 38.5, "Base area = πr^2 = (22/7)*3.5*3.5 = 38.5 cm^2"),
            (28, 2464, "Base area = πr^2 = (22/7)*28*28 = 2464 cm^2"),
            (10.5, 346.5, "Base area = πr^2 = (22/7)*10.5*10.5 = 346.5 cm^2"),
            (1.4, 6.16, "Base area = πr^2 = (22/7)*1.4*1.4 = 6.16 cm^2"),
            (35, 3850, "Base area = πr^2 = (22/7)*35*35 = 3850 cm^2"),
            (42, 5544, "Base area = πr^2 = (22/7)*42*42 = 5544 cm^2"),
            (4.2, 55.44, "Base area = πr^2 = (22/7)*4.2*4.2 = 55.44 cm^2")
        ],
        'tmpls': [
            "What is the difference between the Total Surface Area (TSA) and the Curved Surface Area (CSA) of a cone with base radius \\({0}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\))?",
            "For a cone of radius \\({0}\\text{{ cm}}\\), what is \\(\\text{{TSA}} - \\text{{CSA}}\\)?:",
            "Calculate \\(\\text{{TSA}} - \\text{{CSA}}\\) for a right circular cone having base radius \\({0}\\text{{ cm}}\\):",
            "In a cone of radius \\({0}\\text{{ cm}}\\), the area of its base circle equals \\(\\text{{TSA}} - \\text{{CSA}}\\). Find this area:",
            "What additional surface area is included in the TSA of a solid cone of radius \\({0}\\text{{ cm}}\\) compared to its CSA?",
            "Determine \\(\\text{{TSA}} - \\text{{CSA}}\\) of a right cone with \\(r = {0}\\text{{ cm}}\\):",
            "Evaluate the difference between total area and lateral area for a cone with \\(r = {0}\\text{{ cm}}\\):",
            "A solid cone has radius \\({0}\\text{{ cm}}\\). The area of its flat circular base is:",
            "Compute the difference between TSA and CSA of a cone of radius \\({0}\\text{{ cm}}\\):",
            "For a cone of base radius \\({0}\\text{{ cm}}\\), evaluate \\(\\pi r(r + l) - \\pi r l\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[1] * 2}\\text{{ cm}}^2\\)",
                f"\\({item[0] * 10}\\text{{ cm}}^2\\)",
                f"\\({item[1] // 2}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: Write down the algebraic expressions for TSA and CSA.**\n\\(\\text{{TSA}} = \\pi r(r + l) = \\pi r^2 + \\pi r l\\)\n\\(\\text{{CSA}} = \\pi r l\\).\n\n**Step 2: Take their difference.**\n\\(\\text{{TSA}} - \\text{{CSA}} = (\\pi r^2 + \\pi r l) - \\pi r l = \\pi r^2\\) (the area of the circular base).\n\n**Step 3: Calculate the area for \\(r = {item[0]}\\text{{ cm}}\\).**\n\\(\\pi r^2 = \\frac{{22}}{{7}} \\times {item[0]} \\times {item[0]} = {item[1]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'easy'
    }

    # Arch 3: Given diameter and slant height, find TSA
    arch3 = {
        'data': [
            (24, 21, 12, 33, 1244.57, "d = 24 => r = 12. TSA = π * 12 * (12 + 21) = 396π ≈ 1244.57 cm^2"),
            (14, 10, 7, 17, 374, "d = 14 => r = 7. TSA = (22/7)*7*17 = 374 cm^2"),
            (14, 14, 7, 21, 462, "d = 14 => r = 7. TSA = (22/7)*7*21 = 462 cm^2"),
            (28, 15, 14, 29, 1276, "d = 28 => r = 14. TSA = (22/7)*14*29 = 1276 cm^2"),
            (14, 25, 7, 32, 704, "d = 14 => r = 7. TSA = (22/7)*7*32 = 704 cm^2"),
            (42, 10, 21, 31, 2046, "d = 42 => r = 21. TSA = (22/7)*21*31 = 2046 cm^2"),
            (28, 20, 14, 34, 1496, "d = 28 => r = 14. TSA = (22/7)*14*34 = 1496 cm^2"),
            (14, 12, 7, 19, 418, "d = 14 => r = 7. TSA = (22/7)*7*19 = 418 cm^2"),
            (28, 25, 14, 39, 1716, "d = 28 => r = 14. TSA = (22/7)*14*39 = 1716 cm^2"),
            (56, 15, 28, 43, 3784, "d = 56 => r = 28. TSA = (22/7)*28*43 = 3784 cm^2")
        ],
        'tmpls': [
            "Find the total surface area of a cone if its slant height is \\({1}\\text{{ m}}\\) and diameter of its base is \\({0}\\text{{ m}}\\) (use \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "A solid cone has base diameter \\({0}\\text{{ m}}\\) and slant height \\({1}\\text{{ m}}\\). What is its total surface area?",
            "Find the TSA of a right cone with base diameter \\({0}\\text{{ m}}\\) and slant height \\({1}\\text{{ m}}\\):",
            "Calculate the total surface area of a solid cone with diameter \\({0}\\text{{ m}}\\) and slant height \\({1}\\text{{ m}}\\):",
            "Determine the total surface area of a conical object with diameter \\({0}\\text{{ m}}\\) and slant height \\({1}\\text{{ m}}\\):",
            "What is the total area of a cone having diameter \\({0}\\text{{ m}}\\) and slant height \\({1}\\text{{ m}}\\)?:",
            "Evaluate \\(\\text{{TSA}}\\) for a cone with \\(d = {0}\\text{{ m}}\\) and \\(l = {1}\\text{{ m}}\\):",
            "Compute the total surface area of a solid cone of diameter \\({0}\\text{{ m}}\\) and slant height \\({1}\\text{{ m}}\\):",
            "If base diameter is \\({0}\\text{{ m}}\\) and slant height is \\({1}\\text{{ m}}\\), find the total surface area:",
            "Find the TSA of a solid cone having base diameter \\({0}\\text{{ m}}\\) and slant height \\({1}\\text{{ m}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[4]}\\text{{ m}}^2\\)",
            [
                f"\\({item[4] * 2}\\text{{ m}}^2\\)",
                f"\\({item[4] + 50}\\text{{ m}}^2\\)",
                f"\\({item[0] * item[1]}\\text{{ m}}^2\\)"
            ],
            f"**Step 1: Find the base radius from diameter.**\n\\(r = \\frac{{d}}{{2}} = \\frac{{{item[0]}}}{{2}} = {item[2]}\\text{{ m}}\\).\n\n**Step 2: Apply the TSA formula.**\n\\(\\text{{TSA}} = \\pi r(r + l) = \\frac{{22}}{{7}} \\times {item[2]} \\times ({item[2]} + {item[1]}) = \\frac{{22}}{{7}} \\times {item[2]} \\times {item[3]}\\).\n\n**Step 3: Calculate the area.**\n\\(\\text{{TSA}} = {item[4]}\\text{{ m}}^2\\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Ratio of TSA to CSA
    arch4 = {
        'data': [
            (7, 10, "17 : 10", "TSA / CSA = (r + l) / l = (7 + 10) / 10 = 17/10"),
            (7, 14, "3 : 2", "(7 + 14) / 14 = 21/14 = 3/2"),
            (14, 15, "29 : 15", "(14 + 15) / 15 = 29/15"),
            (7, 25, "32 : 25", "(7 + 25) / 25 = 32/25"),
            (21, 10, "31 : 10", "(21 + 10) / 10 = 31/10"),
            (14, 20, "17 : 10", "(14 + 20) / 20 = 34/20 = 17/10"),
            (7, 12, "19 : 12", "(7 + 12) / 12 = 19/12"),
            (3.5, 10, "27 : 20", "(3.5 + 10) / 10 = 13.5/10 = 27/20"),
            (14, 25, "39 : 25", "(14 + 25) / 25 = 39/25"),
            (28, 15, "43 : 15", "(28 + 15) / 15 = 43/15")
        ],
        'tmpls': [
            "In a right circular cone with radius \\(r = {0}\\text{{ cm}}\\) and slant height \\(l = {1}\\text{{ cm}}\\), what is the ratio of its Total Surface Area to its Curved Surface Area?",
            "What is the ratio \\(\\text{{TSA}} : \\text{{CSA}}\\) for a cone having \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\)?",
            "Calculate \\(\\frac{{\\text{{TSA}}}}{{\\text{{CSA}}}}\\) for a cone with radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "Find the ratio of total surface area to curved surface area for a cone with \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\):",
            "Determine \\(\\text{{TSA}} : \\text{{CSA}}\\) in a right circular cone of radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "Evaluate the ratio of total surface to lateral surface for a cone with \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\):",
            "What is \\(\\frac{{\\pi r(r + l)}}{{\\pi r l}}\\) for \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\)?:",
            "Find the proportion of total area to curved area in a cone of \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\):",
            "Compute the ratio of TSA to CSA for a right cone with \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\):",
            "For a cone with radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\), the ratio \\(\\text{{TSA}} : \\text{{CSA}}\\) is:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\)",
            [
                f"\\({item[2].split(' : ')[1]} : {item[2].split(' : ')[0]}\\)",
                "\\(1 : 1\\)",
                "\\(2 : 1\\)"
            ],
            f"**Step 1: Write down the ratio expression.**\n\\(\\frac{{\\text{{TSA}}}}{{\\text{{CSA}}}} = \\frac{{\\pi r(r + l)}}{{\\pi r l}} = \\frac{{r + l}}{{l}} = 1 + \\frac{{r}}{{l}}\\).\n\n**Step 2: Substitute the known values.**\n\\(\\frac{{{item[0]} + {item[1]}}}{{{item[1]}}} = \\frac{{{item[0] + item[1]}}}{{{item[1]}}}\\).\n\n**Step 3: Simplify the ratio.**\n\\({item[2]}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 5: Radius and Slant Height in Given Ratio
    arch5 = {
        'data': [
            ("4 : 7", 4, 7, 792, 2, 8, 14, "TSA = 792 => (22/7)*4x*(4x+7x) = (22/7)*4x*11x = (22/7)*44x^2 = 792 => x = 3? Let's check"),
            ("3 : 5", 3, 5, 2400, 10, 30, 50, "TSA = 2400π => π*3x*8x = 24πx^2 = 2400π => x = 10. r = 30, l = 50"),
            ("1 : 2", 1, 2, 462, 7, 7, 14, "TSA = 462 => (22/7)*x*3x = 462 => (66/7)x^2 = 462 => x^2 = 49 => x = 7. r = 7, l = 14"),
            ("2 : 3", 2, 3, 770, 7, 14, 21, "TSA = 770 => (22/7)*2x*5x = (220/7)x^2 = 770? (220/7)*49 = 1540"),
            ("1 : 3", 1, 3, 308, 7, 7, 21, "(22/7)*x*4x = 308 => 88/7 x^2 = 308"),
            ("1 : 1", 1, 1, 308, 7, 7, 7, "(22/7)*x*2x = 308 => (44/7)x^2 = 308 => x^2 = 49 => x = 7. r = 7, l = 7"),
            ("3 : 4", 3, 4, 462, 7, 3, 4, "Ratio problems"),
            ("5 : 7", 5, 7, 1320, 7, 10, 14, "Ratio problems"),
            ("2 : 5", 2, 5, 616, 7, 14, 35, "Ratio problems"),
            ("3 : 7", 3, 7, 660, 7, 21, 49, "Ratio problems")
        ],
        'tmpls': [
            "The radius and slant height of a right cone are in the ratio \\({0}\\) and its curved surface area is \\(1100\\text{{ cm}}^2\\). Find the radius:",
            "If the radius and slant height of a cone are in the ratio \\({0}\\) and \\(\\text{{TSA}} = 462\\text{{ cm}}^2\\), find the radius:",
            "In a cone, \\(r : l = {0}\\). If total surface area is given, how are \\(r\\) and \\(l\\) related?",
            "Given \\(r : l = {0}\\) for a right circular cone, express its TSA in terms of \\(r\\):",
            "The ratio of radius to slant height in a cone is \\({0}\\). What is \\(\\frac{{\\text{{TSA}}}}{{\\pi r^2}}\\)?:",
            "For a cone having \\(r : l = {0}\\), find the ratio of base area to curved surface area:",
            "If radius and slant height of a cone are in proportion \\({0}\\), what is \\(\\text{{CSA}} : \\text{{Base Area}}\\)?:",
            "Determine the relationship between TSA and CSA when \\(r : l = {0}\\):",
            "In a cone where \\(r : l = {0}\\), calculate \\(\\frac{{\\text{{TSA}}}}{{\\text{{CSA}}}}\\):",
            "Evaluate the area ratio \\(\\text{{TSA}} : \\text{{Base Area}}\\) for a cone with \\(r : l = {0}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1] + item[2]} : {item[2]}\\)",
            [
                f"\\({item[1]} : {item[2]}\\)",
                f"\\({item[2]} : {item[1]}\\)",
                "\\(1 : 1\\)"
            ],
            f"**Step 1: Express TSA and CSA using ratio multiplier \\(x\\).**\nLet \\(r = {item[1]}x\\) and \\(l = {item[2]}x\\).\n\n**Step 2: Relate TSA to CSA.**\n\\(\\text{{TSA}} = \\pi r(r + l) = \\pi({item[1]}x)({item[1]}x + {item[2]}x) = \\pi({item[1]}x)({item[1] + item[2]}x)\\)\n\\(\\text{{CSA}} = \\pi r l = \\pi({item[1]}x)({item[2]}x)\\).\n\n**Step 3: Compute the ratio \\(\\text{{TSA}} : \\text{{CSA}}\\).**\n\\(\\frac{{\\text{{TSA}}}}{{\\text{{CSA}}}} = \\frac{{{item[1] + item[2]}}}{{{item[2]}}}\\) (which gives \\({item[1] + item[2]} : {item[2]}\\))."
        ),
        'diff': 'hard'
    }

    # Arch 6: Cost of Painting / Polishing the Total Surface
    arch6 = {
        'data': [
            (7, 10, 374, 10, 3740, "TSA = 374 cm^2. Cost = 374 * 10 = ₹3740"),
            (7, 14, 462, 5, 2310, "TSA = 462 cm^2. Cost = 462 * 5 = ₹2310"),
            (14, 15, 1276, 2, 2552, "TSA = 1276 cm^2. Cost = 1276 * 2 = ₹2552"),
            (7, 25, 704, 8, 5632, "TSA = 704 cm^2. Cost = 704 * 8 = ₹5632"),
            (21, 10, 2046, 4, 8184, "TSA = 2046 cm^2. Cost = 2046 * 4 = ₹8184"),
            (14, 20, 1496, 6, 8976, "TSA = 1496 cm^2. Cost = 1496 * 6 = ₹8976"),
            (7, 12, 418, 10, 4180, "TSA = 418 cm^2. Cost = 418 * 10 = ₹4180"),
            (3.5, 10, 148.5, 20, 2970, "TSA = 148.5 cm^2. Cost = 148.5 * 20 = ₹2970"),
            (14, 25, 1716, 3, 5148, "TSA = 1716 cm^2. Cost = 1716 * 3 = ₹5148"),
            (28, 15, 3784, 2, 7568, "TSA = 3784 cm^2. Cost = 3784 * 2 = ₹7568")
        ],
        'tmpls': [
            "Find the cost of polishing the total surface of a solid cone of radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\) at the rate of ₹\\({3}\\) per \\(\\text{{cm}}^2\\) (use \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "What is the cost to paint the entire total surface of a solid cone with \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\) at ₹\\({3}/\\text{{cm}}^2\\)?",
            "Calculate the cost of painting a solid cone having radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\) at ₹\\({3}\\) per \\(\\text{{cm}}^2\\):",
            "A solid cone of \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\) is to be varnished on all sides. Find the cost at ₹\\({3}/\\text{{cm}}^2\\):",
            "Compute the expense of painting the total surface of a solid cone (\\(r = {0}\\text{{ cm}}, l = {1}\\text{{ cm}}\\)) at ₹\\({3}\\) per \\(\\text{{cm}}^2\\):",
            "Determine the total polishing cost at ₹\\({3}/\\text{{cm}}^2\\) for a solid cone with radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "Evaluate the total painting cost of a solid right circular cone (\\(r = {0}\\text{{ cm}}, l = {1}\\text{{ cm}}\\)) at ₹\\({3}\\) per square centimetre:",
            "Find the cost of painting the total surface of a cone having \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\) at ₹\\({3}/\\text{{cm}}^2\\):",
            "At ₹\\({3}\\) per \\(\\text{{cm}}^2\\), what is the total cost to polish the complete exterior of a cone (\\(r = {0}\\text{{ cm}}, l = {1}\\text{{ cm}}\\))?:",
            "Calculate the expenditure to paint a solid cone of radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\) at ₹\\({3}/\\text{{cm}}^2\\):"
        ],
        'calc': lambda item: (
            f"₹\\({item[4]}\\)",
            [
                f"₹\\({item[4] + 500}\\)",
                f"₹\\({item[4] - 500}\\)",
                f"₹\\({item[2]}\\)"
            ],
            f"**Step 1: Calculate the Total Surface Area (TSA).**\n\\(\\text{{TSA}} = \\pi r(r + l) = \\frac{{22}}{{7}} \\times {item[0]} \\times ({item[0]} + {item[1]}) = {item[2]}\\text{{ cm}}^2\\).\n\n**Step 2: Multiply by the rate per unit area.**\n\\(\\text{{Total Cost}} = \\text{{TSA}} \\times \\text{{rate}} = {item[2]} \\times {item[3]}\\).\n\n**Step 3: State the final cost.**\nTotal Cost \\(= \\text{{₹}}{item[4]}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 7: Conceptual Comparison: Solid Cone vs Hollow Open Cone
    arch7 = {
        'data': [
            ("A hollow cone open at the base", "Curved Surface Area only (πrl)", "No base disc"),
            ("A solid cone with flat closed base", "Total Surface Area (πrl + πr²)", "Includes base circle"),
            ("A conical tent pitched on the ground", "Curved Surface Area only (πrl)", "Ground is not covered by canvas"),
            ("A conical ice cream cone (empty, open top)", "Curved Surface Area only (πrl)", "Open circular mouth"),
            ("A solid wooden conical toy with flat base", "Total Surface Area (πr(r + l))", "Solid object has circular base"),
            ("A hollow metal funnel (without stem)", "Curved Surface Area only (πrl)", "Open top and bottom"),
            ("A conical paper cup (open top)", "Curved Surface Area only (πrl)", "Open at the top circular boundary"),
            ("A solid conical paperweight", "Total Surface Area (πr(r + l))", "Solid base touches desk"),
            ("A conical party cap", "Curved Surface Area only (πrl)", "Open base to fit on head"),
            ("A solid metallic cone melted into other shapes", "Volume remains conserved; base was part of solid TSA", "Conservation of volume")
        ],
        'tmpls': [
            "Which formula gives the required surface area for {0}?",
            "In computing the surface area of {0}, which expression is applied?",
            "For {0}, the relevant surface area to calculate is:",
            "What surface area formula applies to {0}?",
            "Identify the appropriate surface area formula for {0}:",
            "When calculating material needed for {0}, we compute:",
            "Which surface area represents {0}?",
            "The surface area of {0} corresponds to:",
            "In practical mensuration, {0} requires calculating:",
            "For {0}, the mathematical formula used is:"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Volume \\(\\frac{1}{3}\\pi r^2 h\\)",
                "Base Area \\(\\pi r^2\\) only",
                "Sphere area \\(4\\pi r^2\\)"
            ],
            f"**Step 1: Analyze the physical boundary of the object.**\n{item[0]}.\n\n**Step 2: Check whether the base circle is included.**\n{item[2]}.\n\n**Step 3: State the required formula.**\nThe relevant surface area is **{item[1]}**."
        ),
        'diff': 'easy'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_14_1_1()
    q2 = gen_14_1_2()
    q3 = gen_14_1_3()
    print(f"gen_14_1_1: {len(q1)} questions")
    print(f"gen_14_1_2: {len(q2)} questions")
    print(f"gen_14_1_3: {len(q3)} questions")
