# scripts/build_cbse9_mgm_ch13_part1.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 13: Two Variables, One Line
Part 1:
- Subtopic 13.1.1: Identifying coefficients a, b, c
- Subtopic 13.1.2: Expressing word problems as two-variable linear equations
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 13
CH_NAME = "Two Variables, One Line"

# ==============================================================================
# SUBTOPIC 13.1.1: Identifying coefficients a, b, c
# ==============================================================================
def gen_13_1_1():
    tc = "CBSE-9-MGM-13-13.1.1"
    tname = "Identifying coefficients a, b, c"

    # Arch 0: Standard rearrangement: ax + by = c -> ax + by - c = 0
    arch0 = {
        'data': [
            (2, 3, 4.37, "2x + 3y = 4.37 => 2x + 3y - 4.37 = 0 => a=2, b=3, c=-4.37"),
            (3, 4, 12, "3x + 4y = 12 => 3x + 4y - 12 = 0 => a=3, b=4, c=-12"),
            (5, -2, 7, "5x - 2y = 7 => 5x - 2y - 7 = 0 => a=5, b=-2, c=-7"),
            (4, 5, 20, "4x + 5y = 20 => 4x + 5y - 20 = 0 => a=4, b=5, c=-20"),
            (7, -3, 14, "7x - 3y = 14 => 7x - 3y - 14 = 0 => a=7, b=-3, c=-14"),
            (1, -4, 9, "x - 4y = 9 => x - 4y - 9 = 0 => a=1, b=-4, c=-9"),
            (6, 7, 42, "6x + 7y = 42 => 6x + 7y - 42 = 0 => a=6, b=7, c=-42"),
            (8, -5, 16, "8x - 5y = 16 => 8x - 5y - 16 = 0 => a=8, b=-5, c=-16"),
            (9, 2, 18, "9x + 2y = 18 => 9x + 2y - 18 = 0 => a=9, b=2, c=-18"),
            (3, -8, 24, "3x - 8y = 24 => 3x - 8y - 24 = 0 => a=3, b=-8, c=-24")
        ],
        'tmpls': [
            "Write the equation \\({0}x + {1}y = {2}\\) in the standard form \\(ax + by + c = 0\\) and identify \\(c\\):",
            "Express \\({0}x + {1}y = {2}\\) in the form \\(ax + by + c = 0\\). What is the value of \\(c\\)?",
            "In the standard form \\(ax + by + c = 0\\) of the equation \\({0}x + {1}y = {2}\\), find \\(c\\):",
            "When \\({0}x + {1}y = {2}\\) is compared with \\(ax + by + c = 0\\), what is \\(c\\)?",
            "Convert \\({0}x + {1}y = {2}\\) to \\(ax + by + c = 0\\) and determine \\(c\\):",
            "Determine the coefficient \\(c\\) when \\({0}x + {1}y = {2}\\) is written as \\(ax + by + c = 0\\):",
            "Find \\(c\\) in \\(ax + by + c = 0\\) for the linear equation \\({0}x + {1}y = {2}\\):",
            "What is the constant term \\(c\\) when \\({0}x + {1}y = {2}\\) is represented in standard form \\(ax + by + c = 0\\)?",
            "Evaluate \\(c\\) for \\({0}x + {1}y = {2}\\) in the form \\(ax + by + c = 0\\):",
            "Express the linear equation \\({0}x + {1}y = {2}\\) as \\(ax + by + c = 0\\). The value of \\(c\\) is:"
        ],
        'calc': lambda item: (
            f"\\({-item[2]}\\)",
            [
                f"\\({item[2]}\\)",
                f"\\({item[0]}\\)",
                f"\\({item[1]}\\)"
            ],
            f"**Step 1: Write down the given linear equation.**\n\\({item[0]}x + ({item[1]})y = {item[2]}\\).\n\n**Step 2: Transpose all terms to the left-hand side to match \\(ax + by + c = 0\\).**\n\\({item[0]}x + ({item[1]})y - ({item[2]}) = 0\\).\n\n**Step 3: Compare with \\(ax + by + c = 0\\).**\n\\(a = {item[0]}, \\; b = {item[1]}, \\; c = {-item[2]}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Single variable equation expressed in two variables
    arch1 = {
        'data': [
            ("2x = 3", 2, 0, -3, "2x + 0y - 3 = 0 => a=2, b=0, c=-3"),
            ("y = 2", 0, 1, -2, "0x + 1y - 2 = 0 => a=0, b=1, c=-2"),
            ("x = -5", 1, 0, 5, "1x + 0y + 5 = 0 => a=1, b=0, c=5"),
            ("5y = 2", 0, 5, -2, "0x + 5y - 2 = 0 => a=0, b=5, c=-2"),
            ("3x = -7", 3, 0, 7, "3x + 0y + 7 = 0 => a=3, b=0, c=7"),
            ("y = -4", 0, 1, 4, "0x + 1y + 4 = 0 => a=0, b=1, c=4"),
            ("4x = 9", 4, 0, -9, "4x + 0y - 9 = 0 => a=4, b=0, c=-9"),
            ("2y = 7", 0, 2, -7, "0x + 2y - 7 = 0 => a=0, b=2, c=-7"),
            ("x = 8", 1, 0, -8, "1x + 0y - 8 = 0 => a=1, b=0, c=-8"),
            ("3y = -11", 0, 3, 11, "0x + 3y + 11 = 0 => a=0, b=3, c=11")
        ],
        'tmpls': [
            "Express the equation \\({0}\\) in the two-variable form \\(ax + by + c = 0\\) and find the value of \\(b\\):",
            "When \\({0}\\) is expressed as a linear equation in two variables \\(ax + by + c = 0\\), what is \\(b\\)?",
            "In writing \\({0}\\) in the form \\(ax + by + c = 0\\), what is the coefficient \\(b\\)?",
            "Represent \\({0}\\) in standard two-variable form \\(ax + by + c = 0\\). What is \\(b\\)?",
            "What is the coefficient of \\(y\\) (i.e. \\(b\\)) when \\({0}\\) is written as \\(ax + by + c = 0\\)?",
            "Find \\(b\\) when \\({0}\\) is converted to \\(ax + by + c = 0\\):",
            "Evaluate the coefficient \\(b\\) in \\(ax + by + c = 0\\) for the equation \\({0}\\):",
            "Convert \\({0}\\) to \\(ax + by + c = 0\\). The value of \\(b\\) is:",
            "Determine \\(b\\) in \\(ax + by + c = 0\\) representing the line \\({0}\\):",
            "What is \\(b\\) when the single-variable equation \\({0}\\) is written in two variables as \\(ax + by + c = 0\\)?"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\)",
            [
                f"\\({item[1]}\\)",
                f"\\({item[3]}\\)",
                "\\(1\\)" if item[2] != 1 else "\\(0\\)"
            ],
            f"**Step 1: Identify the missing variable.**\nThe given equation is \\({item[0]}\\).\n\n**Step 2: Introduce the missing variable with coefficient 0.**\nWe write it with both \\(x\\) and \\(y\\):\n\\({item[1]}x + {item[2]}y + ({item[3]}) = 0\\).\n\n**Step 3: State the coefficient \\(b\\).**\nThe coefficient of \\(y\\) is \\(b = {item[2]}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Fractional coefficients
    arch2 = {
        'data': [
            ("x - \\frac{y}{5} - 10 = 0", 1, -0.2, -10, "1", "-\\frac{1}{5}", "-10"),
            ("x - \\frac{y}{2} - 5 = 0", 1, -0.5, -5, "1", "-\\frac{1}{2}", "-5"),
            ("\\frac{x}{2} + \\frac{y}{3} = 1", 0.5, 1/3, -1, "\\frac{1}{2}", "\\frac{1}{3}", "-1"),
            ("\\frac{x}{3} - \\frac{y}{4} = 2", 1/3, -0.25, -2, "\\frac{1}{3}", "-\\frac{1}{4}", "-2"),
            ("2x - \\frac{y}{3} + 4 = 0", 2, -1/3, 4, "2", "-\\frac{1}{3}", "4"),
            ("\\frac{x}{4} + y - 7 = 0", 0.25, 1, -7, "\\frac{1}{4}", "1", "-7"),
            ("3x + \\frac{y}{2} - 8 = 0", 3, 0.5, -8, "3", "\\frac{1}{2}", "-8"),
            ("\\frac{x}{5} - \\frac{y}{5} = 3", 0.2, -0.2, -3, "\\frac{1}{5}", "-\\frac{1}{5}", "-3"),
            ("x + \\frac{y}{4} = 6", 1, 0.25, -6, "1", "\\frac{1}{4}", "-6"),
            ("\\frac{x}{7} - y + 2 = 0", 1/7, -1, 2, "\\frac{1}{7}", "-1", "2")
        ],
        'tmpls': [
            "In the linear equation \\({0}\\), what is the coefficient \\(b\\) in standard form \\(ax + by + c = 0\\)?",
            "Compare \\({0}\\) with \\(ax + by + c = 0\\). What is the value of \\(b\\)?",
            "Identify coefficient \\(b\\) in the linear equation \\({0}\\):",
            "What is \\(b\\) when \\({0}\\) is written as \\(ax + by + c = 0\\)?",
            "Find the coefficient of \\(y\\) in \\({0}\\):",
            "Determine \\(b\\) in \\(ax + by + c = 0\\) for \\({0}\\):",
            "Evaluate the value of \\(b\\) in \\({0}\\):",
            "What is the value of \\(b\\) for the linear equation \\({0}\\)?",
            "Find \\(b\\) from the equation \\({0}\\):",
            "In \\(ax + by + c = 0\\), what is \\(b\\) for \\({0}\\)?"
        ],
        'calc': lambda item: (
            f"\\({item[5]}\\)",
            [
                f"\\({item[4]}\\)",
                f"\\({item[6]}\\)",
                "\\(5\\)" if "5" in item[5] else "\\(2\\)"
            ],
            f"**Step 1: Write down the equation in standard form \\(ax + by + c = 0\\).**\n\\({item[0]}\\).\n\n**Step 2: Identify the coefficient multiplying \\(y\\).**\nThe term involving \\(y\\) has coefficient \\({item[5]}\\).\n\n**Step 3: State the value of \\(b\\).**\n\\(b = {item[5]}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Irrational / Radical coefficients
    arch3 = {
        'data': [
            ("\\sqrt{2}x + \\sqrt{3}y = 5", "\\sqrt{2}", "\\sqrt{3}", "-5"),
            ("\\sqrt{3}x - \\sqrt{2}y = 7", "\\sqrt{3}", "-\\sqrt{2}", "-7"),
            ("2x - \\sqrt{5}y = 9", "2", "-\\sqrt{5}", "-9"),
            ("\\sqrt{5}x + 3y = 4", "\\sqrt{5}", "3", "-4"),
            ("\\sqrt{2}x + 5y = \\sqrt{7}", "\\sqrt{2}", "5", "-\\sqrt{7}"),
            ("3x - \\sqrt{7}y = 8", "3", "-\\sqrt{7}", "-8"),
            ("\\sqrt{3}x + \\sqrt{5}y = 11", "\\sqrt{3}", "\\sqrt{5}", "-11"),
            ("\\sqrt{7}x - 2y = 3", "\\sqrt{7}", "-2", "-3"),
            ("x - \\sqrt{3}y = 4", "1", "-\\sqrt{3}", "-4"),
            ("\\sqrt{2}x - \\sqrt{2}y = 6", "\\sqrt{2}", "-\\sqrt{2}", "-6")
        ],
        'tmpls': [
            "For the equation \\({0}\\), write in standard form \\(ax + by + c = 0\\) and determine \\((a, b, c)\\):",
            "Compare \\({0}\\) with \\(ax + by + c = 0\\). Which tuple represents \\((a, b, c)\\)?",
            "Express \\({0}\\) in the form \\(ax + by + c = 0\\). The values of \\(a, b, c\\) are:",
            "Find \\((a, b, c)\\) when \\({0}\\) is written as \\(ax + by + c = 0\\):",
            "What are the coefficients \\(a, b\\) and constant \\(c\\) for \\({0}\\)?",
            "Identify \\(a, b, c\\) in standard form for \\({0}\\):",
            "Determine \\((a, b, c)\\) for \\({0}\\):",
            "Evaluate \\((a, b, c)\\) in \\(ax + by + c = 0\\) for \\({0}\\):",
            "Match \\({0}\\) to \\(ax + by + c = 0\\). The correct set of coefficients is:",
            "In \\(ax + by + c = 0\\), what is the triple \\((a, b, c)\\) for \\({0}\\)?"
        ],
        'calc': lambda item: (
            f"\\(a = {item[1]}, \\; b = {item[2]}, \\; c = {item[3]}\\)",
            [
                f"\\(a = {item[1]}, \\; b = {item[2]}, \\; c = {item[3].replace('-', '')}\\)",
                f"\\(a = {item[2]}, \\; b = {item[1]}, \\; c = {item[3]}\\)",
                f"\\(a = 1, \\; b = 1, \\; c = {item[3]}\\)"
            ],
            f"**Step 1: Transpose all terms to LHS.**\n\\({item[0]} \\implies {item[1]}x + ({item[2]})y + ({item[3]}) = 0\\).\n\n**Step 2: Match with \\(ax + by + c = 0\\).**\n\\(a = {item[1]}\\), \\(b = {item[2]}\\), \\(c = {item[3]}\\).\n\n**Step 3: State the triple.**\n\\((a, b, c) = ({item[1]}, {item[2]}, {item[3]})\\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Right-to-Left Transposition (c = ax + by)
    arch4 = {
        'data': [
            ("4 = 5x - 3y", 5, -3, -4, "5x - 3y - 4 = 0"),
            ("7 = 2x + 3y", 2, 3, -7, "2x + 3y - 7 = 0"),
            ("12 = 4x - 5y", 4, -5, -12, "4x - 5y - 12 = 0"),
            ("9 = x + 4y", 1, 4, -9, "x + 4y - 9 = 0"),
            ("5 = 3x - 2y", 3, -2, -5, "3x - 2y - 5 = 0"),
            ("8 = 7x + y", 7, 1, -8, "7x + y - 8 = 0"),
            ("15 = 6x - 7y", 6, -7, -15, "6x - 7y - 15 = 0"),
            ("10 = 2x - 9y", 2, -9, -10, "2x - 9y - 10 = 0"),
            ("6 = 3x + 5y", 3, 5, -6, "3x + 5y - 6 = 0"),
            ("14 = 8x - 3y", 8, -3, -14, "8x - 3y - 14 = 0")
        ],
        'tmpls': [
            "Write \\({0}\\) in the form \\(ax + by + c = 0\\) with \\(a > 0\\) and find \\(c\\):",
            "When \\({0}\\) is rewritten as \\(ax + by + c = 0\\) (with \\(a > 0\\)), what is \\(c\\)?",
            "Express \\({0}\\) in the standard form \\(ax + by + c = 0\\). What is the value of \\(c\\)?",
            "Find \\(c\\) when \\({0}\\) is expressed in standard form with positive coefficient of \\(x\\):",
            "In the form \\(ax + by + c = 0\\) with \\(a = {1}\\), what is \\(c\\) for \\({0}\\)?",
            "Determine \\(c\\) for \\({0}\\) written as \\(ax + by + c = 0\\):",
            "Evaluate \\(c\\) when \\({0}\\) is arranged into \\(ax + by + c = 0\\):",
            "What is \\(c\\) in \\(ax + by + c = 0\\) corresponding to \\({0}\\)?",
            "Convert \\({0}\\) into \\(ax + by + c = 0\\). The constant term \\(c\\) is:",
            "Find the constant term \\(c\\) for \\({0}\\) in standard linear form:"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\)",
            [
                f"\\({-item[3]}\\)",
                f"\\({item[1]}\\)",
                f"\\({item[2]}\\)"
            ],
            f"**Step 1: Rewrite the equation with \\(x\\) and \\(y\\) terms first.**\nFrom \\({item[0]}\\), subtract the constant from both sides:\n\\({item[1]}x + ({item[2]})y + ({item[3]}) = 0\\).\n\n**Step 2: Match with \\(ax + by + c = 0\\).**\n\\(a = {item[1]}, \\; b = {item[2]}, \\; c = {item[3]}\\).\n\n**Step 3: State the value of \\(c\\).**\n\\(c = {item[3]}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 5: Definition and Conditions for Linear Equation in Two Variables
    arch5 = {
        'data': [
            ("a and b are not both zero", "a² + b² ≠ 0", "Condition for ax + by + c = 0 to be a linear equation in two variables"),
            ("Degree of both x and y is 1", "Linear polynomial in two variables", "Defines linearity"),
            ("Straight line", "Geometrical representation of ax + by + c = 0", "Graph of a linear equation"),
            ("Infinitely many solutions", "Every point on the line is a solution", "Solution set of ax + by + c = 0"),
            ("Real numbers", "Coefficients a, b, and c belong to the real numbers ℝ", "Domain of coefficients"),
            ("a = 0 and b ≠ 0", "Line is parallel to the x-axis (by + c = 0)", "Horizontal line"),
            ("b = 0 and a ≠ 0", "Line is parallel to the y-axis (ax + c = 0)", "Vertical line"),
            ("c = 0", "Line passes through the origin (0, 0)", "ax + by = 0"),
            ("Two independent variables", "x and y", "Two variables"),
            ("ax + by + c = 0", "Standard form of a linear equation in two variables", "Canonical standard form")
        ],
        'tmpls': [
            "An equation of the form \\(ax + by + c = 0\\) is called a linear equation in two variables \\(x\\) and \\(y\\) if:",
            "What condition must coefficients \\(a\\) and \\(b\\) satisfy in \\(ax + by + c = 0\\) to be a linear equation in two variables?",
            "For \\(ax + by + c = 0\\) to represent a valid linear equation in two variables, which condition is essential?",
            "Which condition ensures that \\(ax + by + c = 0\\) contains two variables?",
            "In \\(ax + by + c = 0\\), the mathematical condition that \\(a\\) and \\(b\\) are not both zero is symbolically written as:",
            "What is the fundamental algebraic condition on \\(a\\) and \\(b\\) for \\(ax + by + c = 0\\)?",
            "A linear equation in two variables must satisfy:",
            "Under what condition does \\(ax + by + c = 0\\) define a straight line in the coordinate plane?",
            "The equation \\(ax + by + c = 0\\) is a linear equation in two variables if and only if:",
            "Which of the following is the necessary condition on \\(a\\) and \\(b\\) in \\(ax + by + c = 0\\)?"
        ],
        'calc': lambda item: (
            "\\(a\\) and \\(b\\) are not both zero (\\(a^2 + b^2 \\neq 0\\))",
            [
                "\\(a = 0\\) and \\(b = 0\\)",
                "\\(a\\) and \\(b\\) must both be positive integers",
                "\\(c\\) must not be zero"
            ],
            "**Step 1: State the definition of a linear equation in two variables.**\nAn equation of the form \\(ax + by + c = 0\\), where \\(a, b, c\\) are real numbers, is a linear equation in two variables if \\(a\\) and \\(b\\) are not both zero.\n\n**Step 2: Express this condition symbolically.**\nThis condition is compactly expressed as \\(a^2 + b^2 \\neq 0\\).\n\n**Step 3: State the conclusion.**\n\\(a\\) and \\(b\\) are not both zero (\\(a^2 + b^2 \\neq 0\\))."
        ),
        'diff': 'easy'
    }

    # Arch 6: Evaluating a + b + c
    arch6 = {
        'data': [
            (2, 3, 5, 2, 3, -5, 0, "2x + 3y = 5 => 2 + 3 - 5 = 0"),
            (3, 4, 12, 3, 4, -12, -5, "3x + 4y = 12 => 3 + 4 - 12 = -5"),
            (5, -2, 10, 5, -2, -10, -7, "5x - 2y = 10 => 5 - 2 - 10 = -7"),
            (1, -3, 6, 1, -3, -6, -8, "x - 3y = 6 => 1 - 3 - 6 = -8"),
            (4, 3, 7, 4, 3, -7, 0, "4x + 3y = 7 => 4 + 3 - 7 = 0"),
            (6, -1, 5, 6, -1, -5, 0, "6x - y = 5 => 6 - 1 - 5 = 0"),
            (2, 5, 9, 2, 5, -9, -2, "2x + 5y = 9 => 2 + 5 - 9 = -2"),
            (7, 2, 14, 7, 2, -14, -5, "7x + 2y = 14 => 7 + 2 - 14 = -5"),
            (3, -5, 15, 3, -5, -15, -17, "3x - 5y = 15 => 3 - 5 - 15 = -17"),
            (8, 3, 24, 8, 3, -24, -13, "8x + 3y = 24 => 8 + 3 - 24 = -13")
        ],
        'tmpls': [
            "If the equation \\({0}x + ({1})y = {2}\\) is written in standard form \\(ax + by + c = 0\\), what is \\(a + b + c\\)?",
            "Express \\({0}x + ({1})y = {2}\\) as \\(ax + by + c = 0\\). Find the value of \\(a + b + c\\):",
            "In \\(ax + by + c = 0\\) for the equation \\({0}x + ({1})y = {2}\\), calculate \\(a + b + c\\):",
            "Find the sum \\(a + b + c\\) after writing \\({0}x + ({1})y = {2}\\) in the form \\(ax + by + c = 0\\):",
            "Calculate \\(a + b + c\\) for \\({0}x + ({1})y = {2}\\) compared to \\(ax + by + c = 0\\):",
            "Determine \\(a + b + c\\) when \\({0}x + ({1})y = {2}\\) is put into standard form:",
            "What is \\(a + b + c\\) for the linear equation \\({0}x + ({1})y = {2}\\)?",
            "Evaluate \\(a + b + c\\) where \\(a, b, c\\) are coefficients of \\({0}x + ({1})y = {2}\\) in standard form:",
            "Compute \\(a + b + c\\) for \\({0}x + ({1})y = {2}\\) written as \\(ax + by + c = 0\\):",
            "Given \\({0}x + ({1})y = {2}\\), find the sum of coefficients and constant \\(a + b + c\\):"
        ],
        'calc': lambda item: (
            f"\\({item[6]}\\)",
            [
                f"\\({item[6] + 2}\\)",
                f"\\({item[6] - 2}\\)",
                f"\\({abs(item[6])}\\)"
            ],
            f"**Step 1: Write the equation in standard form \\(ax + by + c = 0\\).**\n\\({item[0]}x + ({item[1]})y - ({item[2]}) = 0\\).\n\n**Step 2: Identify \\(a, b, c\\).**\n\\(a = {item[3]}, \\; b = {item[4]}, \\; c = {item[5]}\\).\n\n**Step 3: Compute \\(a + b + c\\).**\n\\(a + b + c = {item[3]} + ({item[4]}) + ({item[5]}) = {item[6]}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 7: Geometric meaning of ax + by = 0 (Passing through origin)
    arch7 = {
        'data': [
            ("y = 2x", "2x - y = 0", "(0, 0)", "Passes through origin because c = 0"),
            ("y = -3x", "3x + y = 0", "(0, 0)", "Passes through origin because c = 0"),
            ("3x = 4y", "3x - 4y = 0", "(0, 0)", "Passes through origin because c = 0"),
            ("x = y", "x - y = 0", "(0, 0)", "Bisector of 1st and 3rd quadrants, passes through origin"),
            ("x + y = 0", "x + y = 0", "(0, 0)", "Bisector of 2nd and 4th quadrants, passes through origin"),
            ("5x + 2y = 0", "5x + 2y = 0", "(0, 0)", "Passes through origin because c = 0"),
            ("y = mx", "mx - y = 0", "(0, 0)", "Standard family of lines through the origin"),
            ("4x - 7y = 0", "4x - 7y = 0", "(0, 0)", "Passes through origin because c = 0"),
            ("2x + 9y = 0", "2x + 9y = 0", "(0, 0)", "Passes through origin because c = 0"),
            ("y = -x", "x + y = 0", "(0, 0)", "Passes through origin because c = 0")
        ],
        'tmpls': [
            "The graph of the linear equation \\({0}\\) always passes through which specific point?",
            "Which point necessarily lies on the line \\({0}\\)?",
            "The line given by \\({0}\\) passes through:",
            "At which point does the line \\({0}\\) intersect the axes simultaneously?",
            "What special point is guaranteed to be a solution of \\({0}\\)?",
            "The linear equation \\({0}\\) has no constant term (\\(c = 0\\)). Its graph passes through:",
            "Find the point through which the graph of \\({0}\\) passes:",
            "Which coordinate pair satisfies the equation \\({0}\\)?",
            "Where does the line \\({0}\\) cross the origin?",
            "The equation \\({0}\\) represents a line passing through:"
        ],
        'calc': lambda item: (
            "The origin \\((0, 0)\\)",
            [
                "\\((1, 1)\\)",
                "\\((0, 1)\\)",
                "\\((1, 0)\\)"
            ],
            f"**Step 1: Write the equation in standard form.**\n\\({item[1]}\\).\n\n**Step 2: Note the value of the constant term \\(c\\).**\nHere \\(c = 0\\).\n\n**Step 3: Test the origin \\((0, 0)\\).**\nSubstituting \\(x = 0, y = 0\\):\n\\(0 + 0 = 0\\), which is true. Therefore, the line passes through **the origin \\((0, 0)\\)**."
        ),
        'diff': 'easy'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 13.1.2: Expressing word problems as two-variable linear equations
# ==============================================================================
def gen_13_1_2():
    tc = "CBSE-9-MGM-13-13.1.2"
    tname = "Expressing word problems as two-variable linear equations"

    # Arch 0: Cost of notebook and pen: x = 2y -> x - 2y = 0
    arch0 = {
        'data': [
            (2, "x - 2y = 0", "Notebook cost (x) is twice pen cost (y)"),
            (3, "x - 3y = 0", "Notebook cost (x) is 3 times pen cost (y)"),
            (4, "x - 4y = 0", "Book cost (x) is 4 times pen cost (y)"),
            (5, "x - 5y = 0", "Bag cost (x) is 5 times bottle cost (y)"),
            (1.5, "2x - 3y = 0", "Notebook cost (x) is 1.5 times pen cost (y) => x = 1.5y => 2x - 3y = 0"),
            (2.5, "2x - 5y = 0", "x = 2.5y => 2x - 5y = 0"),
            (6, "x - 6y = 0", "x is 6 times y"),
            (10, "x - 10y = 0", "x is 10 times y"),
            (7, "x - 7y = 0", "x is 7 times y"),
            (8, "x - 8y = 0", "x is 8 times y")
        ],
        'tmpls': [
            "The cost of a notebook (\\(x\\)) is {0} times the cost of a pen (\\(y\\)). Write a linear equation in two variables to represent this statement:",
            "If the price of an article \\(x\\) is {0} times the price of article \\(y\\), which linear equation represents this condition?",
            "Express the statement 'The cost of a notebook is {0} times the cost of a pen' as a linear equation in two variables (\\(x\\) and \\(y\\)):",
            "A notebook costs \\(x\\) rupees and a pen costs \\(y\\) rupees. If \\(x\\) is {0} times \\(y\\), write the linear equation in standard form:",
            "Which linear equation in two variables models: 'The cost of a notebook (\\(x\\)) is {0} times the cost of a pen (\\(y\\))'?",
            "Write in standard form: The price \\(x\\) of a notebook is {0} times the price \\(y\\) of a pen:",
            "Translate into a two-variable linear equation: 'The cost of item \\(x\\) is {0} times the cost of item \\(y\\)':",
            "If notebook cost is \\(x\\) and pen cost is \\(y\\), and \\(x\\) is {0} times \\(y\\), the equation is:",
            "Represent as \\(ax + by + c = 0\\): The cost of \\(x\\) equals {0} times the cost of \\(y\\):",
            "What is the linear equation for 'The cost of a notebook (\\(x\\)) is {0} times the cost of a pen (\\(y\\))'?"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\)",
            [
                f"\\({item[1].replace('-', '+')}\\)",
                f"\\(x + y = {item[0]}\\)",
                f"\\(xy = {item[0]}\\)"
            ],
            f"**Step 1: Assign algebraic variables.**\nLet the cost of a notebook be \\(x\\) and the cost of a pen be \\(y\\).\n\n**Step 2: Translate the word condition into an equation.**\nAccording to the statement, cost of notebook = {item[0]} \\(\\times\\) cost of pen:\n\\(x = {item[0]}y\\).\n\n**Step 3: Write in standard form \\(ax + by + c = 0\\).**\n\\({item[1]}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Combined sports score / joint total: x + y = Total
    arch1 = {
        'data': [
            (176, "x + y = 176", "Yamini and Fatima together contributed ₹176 / scored 176 runs"),
            (100, "x + y = 100", "Combined contribution of ₹100 towards PM Relief Fund"),
            (150, "x + y = 150", "Together scored 150 runs in a cricket match"),
            (200, "x + y = 200", "Total collection is ₹200"),
            (85, "x + y = 85", "Combined marks in two subjects is 85"),
            (120, "x + y = 120", "Total expenditure is ₹120"),
            (180, "x + y = 180", "Supplementary angles sum: x + y = 180"),
            (90, "x + y = 90", "Complementary angles sum: x + y = 90"),
            (250, "x + y = 250", "Total donation is ₹250"),
            (360, "x + y = 360", "Sum of angles: x + y = 360")
        ],
        'tmpls': [
            "Two students together contributed ₹\\({0}\\) towards the Prime Minister's Relief Fund. If their individual contributions are \\(x\\) and \\(y\\), write a linear equation to satisfy this data:",
            "In a cricket match, two batsmen together scored \\({0}\\) runs. Let runs scored by them be \\(x\\) and \\(y\\). The linear equation representing this is:",
            "The sum of money contributed by person \\(A\\) (\\(x\\)) and person \\(B\\) (\\(y\\)) is ₹\\({0}\\). Express this in linear equation form:",
            "Write a linear equation in two variables for: 'The total score of two players \\(x\\) and \\(y\\) is \\({0}\\)':",
            "Express the statement: 'Two friends \\(x\\) and \\(y\\) together have \\({0}\\) marbles' as a linear equation:",
            "Which equation models: 'The combined weight of two objects \\(x\\) and \\(y\\) is \\({0}\\text{{ kg}}'?",
            "Translate into a two-variable linear equation: 'The sum of quantities \\(x\\) and \\(y\\) is equal to \\({0}\\)':",
            "What is the linear equation representing: 'Person \\(X\\) and Person \\(Y\\) together contributed ₹\\({0}\\)'?",
            "If \\(x\\) and \\(y\\) represent two quantities that sum to \\({0}\\), the linear equation is:",
            "Write the linear equation for: 'The combined value of \\(x\\) and \\(y\\) is \\({0}\\)':"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\)",
            [
                f"\\(x - y = {item[0]}\\)",
                f"\\(2x + y = {item[0]}\\)",
                f"\\(xy = {item[0]}\\)"
            ],
            f"**Step 1: Identify the two quantities.**\nLet the two contributions/scores be \\(x\\) and \\(y\\).\n\n**Step 2: Translate 'together' or 'sum' to addition.**\n\\(x + y = {item[0]}\\).\n\n**Step 3: State the final linear equation.**\n\\({item[1]}\\) (or \\(x + y - {item[0]} = 0\\))."
        ),
        'diff': 'easy'
    }

    # Arch 2: Taxi Fare Problem
    arch2 = {
        'data': [
            (50, 12, "y = 50 + 12(x - 1) = 12x + 38 => 12x - y + 38 = 0", 12, 38),
            (20, 8, "y = 20 + 8(x - 1) = 8x + 12 => 8x - y + 12 = 0", 8, 12),
            (15, 10, "y = 15 + 10(x - 1) = 10x + 5 => 10x - y + 5 = 0", 10, 5),
            (30, 15, "y = 30 + 15(x - 1) = 15x + 15 => 15x - y + 15 = 0", 15, 15),
            (25, 9, "y = 25 + 9(x - 1) = 9x + 16 => 9x - y + 16 = 0", 9, 16),
            (40, 11, "y = 40 + 11(x - 1) = 11x + 29 => 11x - y + 29 = 0", 11, 29),
            (10, 6, "y = 10 + 6(x - 1) = 6x + 4 => 6x - y + 4 = 0", 6, 4),
            (35, 14, "y = 35 + 14(x - 1) = 14x + 21 => 14x - y + 21 = 0", 14, 21),
            (45, 13, "y = 45 + 13(x - 1) = 13x + 32 => 13x - y + 32 = 0", 13, 32),
            (60, 16, "y = 60 + 16(x - 1) = 16x + 44 => 16x - y + 44 = 0", 16, 44)
        ],
        'tmpls': [
            "A taxi charges ₹\\({0}\\) for the first kilometre and ₹\\({1}\\) per km for subsequent distance. Taking distance as \\(x\\text{{ km}}\\) and total fare as ₹\\(y\\), write the linear equation:",
            "The taxi fare in a city is ₹\\({0}\\) for the first km and ₹\\({1}\\)/km for each additional km. Taking total distance as \\(x\\) and fare as \\(y\\), the linear equation is:",
            "For a journey of \\(x\\text{{ km}}\\), the taxi fare is ₹\\({0}\\) for the 1st km and ₹\\({1}\\) for every subsequent km. Write the linear equation relating fare \\(y\\) and distance \\(x\\):",
            "Express the total taxi fare \\(y\\) for a trip of \\(x\\text{{ km}}\\) where first km costs ₹\\({0}\\) and remaining distance costs ₹\\({1}\\)/km:",
            "Which linear equation relates total fare \\(y\\) to distance \\(x\\) with base fare ₹\\({0}\\) for 1 km and ₹\\({1}\\)/km thereafter?",
            "Write the equation in \\(x\\) and \\(y\\) for taxi fare with fixed first-km rate ₹\\({0}\\) and subsequent rate ₹\\({1}\\)/km:",
            "A cab charges ₹\\({0}\\) for the 1st km and ₹\\({1}\\) for each km after that. If total distance is \\(x\\) and fare is \\(y\\), find the equation:",
            "Find the linear equation for taxi fare \\(y\\) over \\(x\\text{{ km}}\\) where the 1st km fare is ₹\\({0}\\) and thereafter ₹\\({1}\\)/km:",
            "Model the taxi fare: 1st km costs ₹\\({0}\\), subsequent kms cost ₹\\({1}\\)/km. Total fare \\(y\\) for \\(x\\text{{ km}}\\) is:",
            "What linear equation gives total fare \\(y\\) for \\(x\\text{{ km}}\\) if first km is ₹\\({0}\\) and each following km is ₹\\({1}\\)?"
        ],
        'calc': lambda item: (
            f"\\({item[3]}x - y + {item[4]} = 0\\)",
            [
                f"\\({item[3]}x + y + {item[4]} = 0\\)",
                f"\\({item[0]}x + {item[1]}y = 0\\)",
                f"\\(y = {item[1]}x + {item[0]}\\)"
            ],
            f"**Step 1: Break down the fare components.**\nFor total distance \\(x\\text{{ km}}\\) (\\(x \\ge 1\\)):\n- Fare for the first 1 km = ₹\\({item[0]}\\)\n- Remaining distance = \\((x - 1)\\text{{ km}}\\) at ₹\\({item[1]}\\)/km.\n\n**Step 2: Express total fare \\(y\\).**\n\\(y = {item[0]} + {item[1]}(x - 1) = {item[0]} + {item[1]}x - {item[1]} = {item[3]}x + {item[4]}\\).\n\n**Step 3: Write in standard form.**\n\\({item[3]}x - y + {item[4]} = 0\\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Age Relation Problems
    arch3 = {
        'data': [
            (3, 5, "x - 3y - 5 = 0", "Father's age (x) is 5 years more than 3 times son's age (y)"),
            (4, 2, "x - 4y - 2 = 0", "Mother's age (x) is 2 years more than 4 times daughter's age (y)"),
            (2, 10, "x - 2y - 10 = 0", "Age x is 10 years more than twice age y"),
            (3, 7, "x - 3y - 7 = 0", "Age x is 7 years more than 3 times age y"),
            (5, 4, "x - 5y - 4 = 0", "Age x is 4 years more than 5 times age y"),
            (2, 15, "x - 2y - 15 = 0", "Age x is 15 years more than twice age y"),
            (3, 2, "x - 3y - 2 = 0", "Age x is 2 years more than 3 times age y"),
            (4, 6, "x - 4y - 6 = 0", "Age x is 6 years more than 4 times age y"),
            (2, 20, "x - 2y - 20 = 0", "Age x is 20 years more than twice age y"),
            (3, 12, "x - 3y - 12 = 0", "Age x is 12 years more than 3 times age y")
        ],
        'tmpls': [
            "A father's present age (\\(x\\)) is {1} years more than {0} times his son's age (\\(y\\)). Write a linear equation in two variables representing this relation:",
            "If \\(x\\) is {1} more than {0} times \\(y\\), express this relation as a linear equation in standard form \\(ax + by + c = 0\\):",
            "A person's age \\(x\\) exceeds {0} times another person's age \\(y\\) by {1} years. What is the linear equation?",
            "Write the equation in standard form: Age \\(x\\) is {1} years greater than {0} times age \\(y\\):",
            "Which linear equation in two variables represents: 'The value of \\(x\\) is {1} more than {0} times \\(y\\)'?",
            "Translate into standard form \\(ax + by + c = 0\\): \\(x\\) is {1} more than {0} times \\(y\\):",
            "Formulate the linear equation for: 'Father's age (\\(x\\)) is {1} more than {0} times son's age (\\(y\\))':",
            "If \\(x = {0}y + {1}\\), what is this equation in the standard form \\(ax + by + c = 0\\)?",
            "What is the linear equation representing: '\\(x\\) equals {1} added to {0} times \\(y\\)'?",
            "Represent as \\(ax + by + c = 0\\): The age \\(x\\) is {1} years more than {0} times the age \\(y\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\)",
            [
                f"\\({item[2].replace('-', '+')}\\)",
                f"\\(x + {item[0]}y = {item[1]}\\)",
                f"\\({item[0]}x - y - {item[1]} = 0\\)"
            ],
            f"**Step 1: Write the given relationship directly.**\n\\(x = {item[0]}y + {item[1]}\\).\n\n**Step 2: Transpose all terms to the LHS.**\n\\(x - {item[0]}y - {item[1]} = 0\\).\n\n**Step 3: State the standard form.**\n\\({item[2]}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Perimeter of Rectangle
    arch4 = {
        'data': [
            (64, 32, "x + y = 32", "Perimeter = 64 => 2(x + y) = 64 => x + y = 32"),
            (40, 20, "x + y = 20", "Perimeter = 40 => 2(x + y) = 40 => x + y = 20"),
            (50, 25, "x + y = 25", "Perimeter = 50 => x + y = 25"),
            (80, 40, "x + y = 40", "Perimeter = 80 => x + y = 40"),
            (36, 18, "x + y = 18", "Perimeter = 36 => x + y = 18"),
            (72, 36, "x + y = 36", "Perimeter = 72 => x + y = 36"),
            (100, 50, "x + y = 50", "Perimeter = 100 => x + y = 50"),
            (56, 28, "x + y = 28", "Perimeter = 56 => x + y = 28"),
            (48, 24, "x + y = 24", "Perimeter = 48 => x + y = 24"),
            (90, 45, "x + y = 45", "Perimeter = 90 => x + y = 45")
        ],
        'tmpls': [
            "The perimeter of a rectangle with length \\(x\\) and breadth \\(y\\) is \\({0}\\text{{ cm}}\\). Write the linear equation in two variables in simplified form:",
            "A rectangular field has length \\(x\\text{{ m}}\\) and breadth \\(y\\text{{ m}}\\). If its perimeter is \\({0}\\text{{ m}}\\), what is the simplified linear equation relating \\(x\\) and \\(y\\)?",
            "Express the statement: 'The perimeter of a rectangle of dimensions \\(x\\) and \\(y\\) is \\({0}\\)' as a simplified linear equation:",
            "Which equation represents the perimeter \\({0}\\) of a rectangle of length \\(x\\) and width \\(y\\)?",
            "If length is \\(x\\) and breadth is \\(y\\), write the linear equation for a rectangle having perimeter \\({0}\\text{{ cm}}\\):",
            "A rectangular park has perimeter \\({0}\\text{{ m}}\\). With sides \\(x\\) and \\(y\\), the simplified linear equation is:",
            "Translate into a simplified linear equation: 'The perimeter of rectangle with sides \\(x\\) and \\(y\\) is \\({0}\\)':",
            "What is the simplified equation for the perimeter \\({0}\\) of a rectangle of length \\(x\\) and breadth \\(y\\)?",
            "Write the simplified linear relation between length \\(x\\) and breadth \\(y\\) of a rectangle with perimeter \\({0}\\):",
            "A rectangle has length \\(x\\), breadth \\(y\\), and perimeter \\({0}\\). The simplified equation is:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\)",
            [
                f"\\(2x + y = {item[0]}\\)",
                f"\\(x - y = {item[1]}\\)",
                f"\\(xy = {item[0]}\\)"
            ],
            f"**Step 1: State the formula for the perimeter of a rectangle.**\nPerimeter \\(= 2(\\text{{length}} + \\text{{breadth}}) = 2(x + y)\\).\n\n**Step 2: Equate to the given perimeter value.**\n\\(2(x + y) = {item[0]}\\).\n\n**Step 3: Divide both sides by 2.**\n\\(x + y = {item[1]}\\) (or \\(x + y - {item[1]} = 0\\))."
        ),
        'diff': 'easy'
    }

    # Arch 5: Two-Digit Number Digit Relation
    arch5 = {
        'data': [
            (9, "x + y = 9", "The sum of the digits of a two-digit number is 9"),
            (11, "x + y = 11", "The sum of the digits of a two-digit number is 11"),
            (12, "x + y = 12", "The sum of the digits of a two-digit number is 12"),
            (8, "x + y = 8", "The sum of the digits of a two-digit number is 8"),
            (10, "x + y = 10", "The sum of the digits of a two-digit number is 10"),
            (7, "x + y = 7", "The sum of the digits of a two-digit number is 7"),
            (13, "x + y = 13", "The sum of the digits of a two-digit number is 13"),
            (6, "x + y = 6", "The sum of the digits of a two-digit number is 6"),
            (14, "x + y = 14", "The sum of the digits of a two-digit number is 14"),
            (15, "x + y = 15", "The sum of the digits of a two-digit number is 15")
        ],
        'tmpls': [
            "In a two-digit number, the tens digit is \\(x\\) and the units digit is \\(y\\). If the sum of the digits is \\({0}\\), write the linear equation in two variables:",
            "The sum of the digits of a two-digit number with tens digit \\(x\\) and units digit \\(y\\) is \\({0}\\). Express this as a linear equation:",
            "Write a linear equation in two variables for: 'The sum of the tens digit \\(x\\) and units digit \\(y\\) of a number is \\({0}\\)':",
            "If \\(x\\) and \\(y\\) represent the tens and units digits of a two-digit number whose digits add up to \\({0}\\), the equation is:",
            "Which equation models: 'The digits \\(x\\) and \\(y\\) of a two-digit number have a sum of \\({0}\\)'?",
            "Translate into a linear equation: 'The sum of the two digits \\(x\\) and \\(y\\) of a number is \\({0}\\)':",
            "What is the linear equation for: 'The tens digit \\(x\\) and units digit \\(y\\) add to \\({0}\\)'?",
            "Express the condition that the sum of the digits \\(x\\) and \\(y\\) of a two-digit number is \\({0}\\):",
            "Represent the statement: 'The digits \\(x\\) and \\(y\\) sum to \\({0}\\)' as a linear equation:",
            "For a two-digit number with digits \\(x\\) and \\(y\\), if their sum is \\({0}\\), the linear equation is:"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\)",
            [
                f"\\(10x + y = {item[0]}\\)",
                f"\\(x - y = {item[0]}\\)",
                f"\\(10y + x = {item[0]}\\)"
            ],
            f"**Step 1: Identify the digits.**\nTens digit = \\(x\\), Units digit = \\(y\\).\n\n**Step 2: Add the individual digits.**\nSum of the digits \\(= x + y\\).\n\n**Step 3: Equate to the given value.**\n\\(x + y = {item[0]}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 6: Temperature Conversion Formula F = (9/5)C + 32
    arch6 = {
        'data': [
            (0, 32, "C = 0 => F = (9/5)(0) + 32 = 32°F"),
            (100, 212, "C = 100 => F = (9/5)(100) + 32 = 180 + 32 = 212°F"),
            (30, 86, "C = 30 => F = (9/5)(30) + 32 = 54 + 32 = 86°F"),
            (25, 77, "C = 25 => F = (9/5)(25) + 32 = 45 + 32 = 77°F"),
            (35, 95, "C = 35 => F = (9/5)(35) + 32 = 63 + 32 = 95°F"),
            (40, 104, "C = 40 => F = (9/5)(40) + 32 = 72 + 32 = 104°F"),
            (20, 68, "C = 20 => F = (9/5)(20) + 32 = 36 + 32 = 68°F"),
            (10, 50, "C = 10 => F = (9/5)(10) + 32 = 18 + 32 = 50°F"),
            (-40, -40, "C = -40 => F = (9/5)(-40) + 32 = -72 + 32 = -40°F (equal temperature)"),
            (-10, 14, "C = -10 => F = (9/5)(-10) + 32 = -18 + 32 = 14°F")
        ],
        'tmpls': [
            "In the linear equation \\(F = \\frac{9}{5}C + 32\\), if the temperature is \\({0}^\\circ\\text{{C}}\\), what is the temperature in Fahrenheit?",
            "Using the temperature conversion equation \\(F = \\frac{9}{5}C + 32\\), calculate the Fahrenheit temperature for \\(C = {0}^\\circ\\text{{C}}\\):",
            "If the temperature is \\({0}^\\circ\\text{{C}}\\), find the temperature in Fahrenheit using \\(F = \\frac{9}{5}C + 32\\):",
            "What is the value of \\(F\\) when \\(C = {0}\\) in the linear relation \\(F = \\frac{9}{5}C + 32\\)?",
            "Calculate \\(F\\) for \\(C = {0}^\\circ\\text{{C}}\\) using \\(F = \\frac{9}{5}C + 32\\):",
            "Determine the temperature in Fahrenheit corresponding to \\({0}^\\circ\\text{{C}}\\) using \\(F = \\frac{9}{5}C + 32\\):",
            "Evaluate \\(F\\) if \\(C = {0}\\) in the linear equation \\(F = \\frac{9}{5}C + 32\\):",
            "Find the Fahrenheit equivalent of \\({0}^\\circ\\text{{C}}\\) from \\(F = \\frac{9}{5}C + 32\\):",
            "What is the Fahrenheit temperature for \\({0}^\\circ\\text{{C}}\\) according to \\(F = \\frac{9}{5}C + 32\\)?",
            "In \\(F = \\frac{9}{5}C + 32\\), find \\(F\\) when \\(C = {0}^\\circ\\text{{C}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}^\\circ\\text{{F}}\\)",
            [
                f"\\({item[1] + 10}^\\circ\\text{{F}}\\)",
                f"\\({item[1] - 10}^\\circ\\text{{F}}\\)",
                f"\\({item[0]}^\\circ\\text{{F}}\\)"
            ],
            f"**Step 1: State the linear temperature conversion formula.**\n\\(F = \\frac{9}{5}C + 32\\).\n\n**Step 2: Substitute \\(C = {item[0]}^\\circ\\text{{C}}\\).**\n\\(F = \\frac{9}{5}({item[0]}) + 32 = {item[1] - 32} + 32\\).\n\n**Step 3: Calculate \\(F\\).**\n\\(F = {item[1]}^\\circ\\text{{F}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 7: Work and Wages / Daily Earnings Problem
    arch7 = {
        'data': [
            (300, 250, 2450, "300x + 250y = 2450", "Man earns ₹300/day, woman earns ₹250/day. Total = ₹2450"),
            (400, 300, 3100, "400x + 300y = 3100", "Daily wage equation"),
            (500, 350, 4250, "500x + 350y = 4250", "Daily wage equation"),
            (250, 200, 2050, "250x + 200y = 2050", "Daily wage equation"),
            (350, 280, 2870, "350x + 280y = 2870", "Daily wage equation"),
            (450, 320, 3730, "450x + 320y = 3730", "Daily wage equation"),
            (200, 150, 1550, "200x + 150y = 1550", "Daily wage equation"),
            (600, 400, 4600, "600x + 400y = 4600", "Daily wage equation"),
            (550, 380, 4340, "550x + 380y = 4340", "Daily wage equation"),
            (480, 360, 3720, "480x + 360y = 3720", "Daily wage equation")
        ],
        'tmpls': [
            "A skilled worker earns ₹\\({0}\\) per day and an unskilled worker earns ₹\\({1}\\) per day. If \\(x\\) skilled and \\(y\\) unskilled workers together earn ₹\\({2}\\) in a day, write the linear equation:",
            "The daily wages of an adult and a child are ₹\\({0}\\) and ₹\\({1}\\) respectively. If the total wage bill for \\(x\\) adults and \\(y\\) children is ₹\\({2}\\), the linear equation is:",
            "Express as a linear equation: 'The total cost of \\(x\\) items at ₹\\({0}\\) each and \\(y\\) items at ₹\\({1}\\) each is ₹\\({2}\\)':",
            "Write a linear equation in two variables for: '\\(x\\) tickets at ₹\\({0}\\) and \\(y\\) tickets at ₹\\({1}\\) cost a total of ₹\\({2}\\)':",
            "Which equation models: '\\(x\\) kg of rice at ₹\\({0}\\)/kg and \\(y\\) kg of wheat at ₹\\({1}\\)/kg costs ₹\\({2}\\)'?",
            "Translate into a two-variable linear equation: 'The total amount for \\(x\\) units at ₹\\({0}\\) and \\(y\\) units at ₹\\({1}\\) is ₹\\({2}\\)':",
            "What is the linear equation representing: 'Total cost of \\(x\\) tables at ₹\\({0}\\) and \\(y\\) chairs at ₹\\({1}\\) is ₹\\({2}\\)'?",
            "If \\(x\\) items cost ₹\\({0}\\) each and \\(y\\) items cost ₹\\({1}\\) each, and the total spent is ₹\\({2}\\), the equation is:",
            "Model the equation for total expenses ₹\\({2}\\) incurred by buying \\(x\\) units at ₹\\({0}\\) and \\(y\\) units at ₹\\({1}\\):",
            "Write the linear equation for: 'The combined value of \\(x\\) items at ₹\\({0}\\) each and \\(y\\) items at ₹\\({1}\\) each is ₹\\({2}\\)':"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\)",
            [
                f"\\({item[0]}x - {item[1]}y = {item[2]}\\)",
                f"\\(x + y = {item[2]}\\)",
                f"\\({item[1]}x + {item[0]}y = {item[2]}\\)"
            ],
            f"**Step 1: Compute total cost for each category.**\nCost for \\(x\\) units = \\({item[0]}x\\).\nCost for \\(y\\) units = \\({item[1]}y\\).\n\n**Step 2: Sum the costs and equate to the total bill.**\n\\({item[0]}x + {item[1]}y = {item[2]}\\).\n\n**Step 3: State the final linear equation.**\n\\({item[3]}\\)."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_13_1_1()
    q2 = gen_13_1_2()
    print(f"gen_13_1_1: {len(q1)} questions")
    print(f"gen_13_1_2: {len(q2)} questions")
