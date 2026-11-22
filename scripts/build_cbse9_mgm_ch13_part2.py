# scripts/build_cbse9_mgm_ch13_part2.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 13: Two Variables, One Line
Part 2:
- Subtopic 13.2.1: Infinitely many solutions property
- Subtopic 13.2.2: Finding distinct solution pairs (x, y)
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 13
CH_NAME = "Two Variables, One Line"

# ==============================================================================
# SUBTOPIC 13.2.1: Infinitely many solutions property
# ==============================================================================
def gen_13_2_1():
    tc = "CBSE-9-MGM-13-13.2.1"
    tname = "Infinitely many solutions property"

    # Arch 0: Fundamental theorem: A linear equation in two variables has infinitely many solutions
    arch0 = {
        'data': [
            ("y = 3x + 5", "Infinitely many solutions", "For every real value of x, there is a corresponding unique value of y"),
            ("2x + 3y = 6", "Infinitely many solutions", "Every point on the line is a solution"),
            ("x - 2y = 4", "Infinitely many solutions", "Straight line contains infinite points"),
            ("3x + 4y = 12", "Infinitely many solutions", "Infinite ordered pairs satisfy the equation"),
            ("y = 2x", "Infinitely many solutions", "Family of points (t, 2t) for all real t"),
            ("4x - y = 8", "Infinitely many solutions", "Linear equation in two variables"),
            ("x + y = 10", "Infinitely many solutions", "Points of the form (x, 10 - x)"),
            ("5x - 2y = 7", "Infinitely many solutions", "General linear equation in two variables"),
            ("2x = y + 3", "Infinitely many solutions", "Linear relation between two continuous variables"),
            ("3x - 5y + 15 = 0", "Infinitely many solutions", "Standard form linear equation in two variables")
        ],
        'tmpls': [
            "Which of the following statements is true for the linear equation \\({0}\\)?",
            "How many solutions does the linear equation \\({0}\\) have in the set of real numbers?",
            "The equation \\({0}\\) has:",
            "What is the total number of solutions for the linear equation in two variables \\({0}\\)?",
            "A linear equation in two variables such as \\({0}\\) possesses:",
            "Determine the number of solutions of the equation \\({0}\\):",
            "For the linear equation \\({0}\\), how many distinct ordered pairs \\((x, y)\\) satisfy it?",
            "How many real solutions exist for \\({0}\\)?",
            "The number of solution pairs \\((x, y)\\) for \\({0}\\) is:",
            "Which describes the number of solutions of \\({0}\\)?"
        ],
        'calc': lambda item: (
            "Infinitely many solutions",
            [
                "A unique solution",
                "Only two solutions",
                "No solution"
            ],
            f"**Step 1: Identify the type of equation.**\nThe given equation \\({item[0]}\\) is a linear equation in two variables \\(x\\) and \\(y\\).\n\n**Step 2: Understand the relationship between the variables.**\n{item[2]}.\n\n**Step 3: State the conclusion.**\nSince there are infinitely many real numbers for \\(x\\), each yielding a unique corresponding real value for \\(y\\), the equation has **infinitely many solutions**."
        ),
        'diff': 'easy'
    }

    # Arch 1: Finding k when (x0, y0) is a solution: 2x + 3y = k
    arch1 = {
        'data': [
            (2, 1, 2, 3, 7, "2(2) + 3(1) = 4 + 3 = 7"),
            (1, 2, 3, 2, 7, "3(1) + 2(2) = 3 + 4 = 7"),
            (3, 1, 4, 1, 13, "4(3) + 1(1) = 12 + 1 = 13"),
            (2, 3, 5, -2, 4, "5(2) - 2(3) = 10 - 6 = 4"),
            (1, -1, 3, 4, -1, "3(1) + 4(-1) = 3 - 4 = -1"),
            (0, 4, 2, 3, 12, "2(0) + 3(4) = 12"),
            (4, 0, 3, 5, 12, "3(4) + 5(0) = 12"),
            (2, 2, 7, -3, 8, "7(2) - 3(2) = 14 - 6 = 8"),
            (-1, 2, 2, 5, 8, "2(-1) + 5(2) = -2 + 10 = 8"),
            (3, -2, 4, 3, 6, "4(3) + 3(-2) = 12 - 6 = 6")
        ],
        'tmpls': [
            "Find the value of \\(k\\), if \\(x = {0}, y = {1}\\) is a solution of the equation \\({2}x + ({3})y = k\\):",
            "If the point \\(({0}, {1})\\) satisfies the linear equation \\({2}x + ({3})y = k\\), what is \\(k\\)?",
            "Calculate \\(k\\) given that \\(x = {0}, y = {1}\\) is a solution of \\({2}x + ({3})y = k\\):",
            "The ordered pair \\(({0}, {1})\\) is a solution of \\({2}x + ({3})y = k\\). Determine \\(k\\):",
            "What is the value of \\(k\\) if \\(({0}, {1})\\) lies on the line \\({2}x + ({3})y = k\\)?",
            "Evaluate \\(k\\) such that \\(x = {0}\\) and \\(y = {1}\\) satisfy \\({2}x + ({3})y = k\\):",
            "Determine \\(k\\) when \\(({0}, {1})\\) is a solution of \\({2}x + ({3})y = k\\):",
            "If \\(x = {0}, y = {1}\\) solves the equation \\({2}x + ({3})y = k\\), find \\(k\\):",
            "Find \\(k\\) for which \\(({0}, {1})\\) is a solution to \\({2}x + ({3})y = k\\):",
            "What is \\(k\\) if the graph of \\({2}x + ({3})y = k\\) passes through \\(({0}, {1})\\)?"
        ],
        'calc': lambda item: (
            f"\\({item[4]}\\)",
            [
                f"\\({item[4] + 2}\\)",
                f"\\({item[4] - 2}\\)",
                f"\\({item[4] + 5}\\)"
            ],
            f"**Step 1: Substitute the given values of \\(x\\) and \\(y\\).**\nSubstitute \\(x = {item[0]}\\) and \\(y = {item[1]}\\) into \\({item[2]}x + ({item[3]})y = k\\).\n\n**Step 2: Evaluate the left-hand side.**\n\\({item[2]}({item[0]}) + ({item[3]})({item[1]}) = {item[2] * item[0]} + ({item[3] * item[1]}) = {item[4]}\\).\n\n**Step 3: State the value of \\(k\\).**\n\\(k = {item[4]}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Verification of Solution (Is (x, y) a solution?)
    arch2 = {
        'data': [
            ("x - 2y = 4", (4, 0), "Yes", "4 - 2(0) = 4 = RHS"),
            ("x - 2y = 4", (0, 2), "No", "0 - 2(2) = -4 ≠ 4"),
            ("x - 2y = 4", (2, 0), "No", "2 - 2(0) = 2 ≠ 4"),
            ("x - 2y = 4", (4, 2), "No", "4 - 2(2) = 0 ≠ 4"),
            ("2x + y = 7", (3, 1), "Yes", "2(3) + 1 = 7 = RHS"),
            ("2x + y = 7", (1, 5), "Yes", "2(1) + 5 = 7 = RHS"),
            ("2x + y = 7", (2, 2), "No", "2(2) + 2 = 6 ≠ 7"),
            ("3x - y = 3", (1, 0), "Yes", "3(1) - 0 = 3 = RHS"),
            ("3x - y = 3", (2, 3), "Yes", "3(2) - 3 = 3 = RHS"),
            ("3x - y = 3", (0, 3), "No", "3(0) - 3 = -3 ≠ 3")
        ],
        'tmpls': [
            "Check whether the point \\({1}\\) is a solution of the equation \\({0}\\):",
            "Is the ordered pair \\({1}\\) a solution of the linear equation \\({0}\\)?",
            "Does the point \\({1}\\) satisfy the equation \\({0}\\)?",
            "Determine if \\({1}\\) lies on the graph of the linear equation \\({0}\\):",
            "Verify whether \\(x = {1[0]}, y = {1[1]}\\) satisfies \\({0}\\):",
            "Test whether \\({1}\\) is a solution of \\({0}\\):",
            "Does the coordinate pair \\({1}\\) solve \\({0}\\)?",
            "Is \\({1}\\) a valid solution for \\({0}\\)?",
            "Check if \\(x = {1[0]}, y = {1[1]}\\) is a solution of \\({0}\\):",
            "Determine whether \\({1}\\) is a solution to \\({0}\\):"
        ],
        'calc': lambda item: (
            item[2],
            [
                "No" if item[2] == "Yes" else "Yes",
                "Indeterminate",
                "Only for positive x"
            ],
            f"**Step 1: Substitute the point into the left-hand side of \\({item[0]}\\).**\nSubstitute \\(x = {item[1][0]}\\) and \\(y = {item[1][1]}\\).\n\n**Step 2: Compare LHS with RHS.**\n{item[3]}.\n\n**Step 3: State the conclusion.**\nThe answer is **{item[2]}**."
        ),
        'diff': 'easy'
    }

    # Arch 3: Finding Unknown Parameter k in Point (k, y) or (x, k)
    arch3 = {
        'data': [
            ("2x + 3y = 12", 2, "y", 3, "2(3) + 3y = 12 => 3y = 6 => y = 2"),
            ("3x + 4y = 24", 3, "x", 4, "3x + 4(3) = 24 => 3x = 12 => x = 4"),
            ("x - 2y = 8", -1, "x", 6, "x - 2(-1) = 8 => x + 2 = 8 => x = 6"),
            ("5x - 2y = 10", 0, "x", 2, "5x - 2(0) = 10 => 5x = 10 => x = 2"),
            ("2x - 5y = 20", 0, "y", -4, "2(0) - 5y = 20 => -5y = 20 => y = -4"),
            ("4x + 3y = 18", 2, "x", 3, "4x + 3(2) = 18 => 4x = 12 => x = 3"),
            ("3x - y = 7", 2, "y", -1, "3(2) - y = 7 => 6 - y = 7 => y = -1"),
            ("x + 4y = 9", 2, "x", 1, "x + 4(2) = 9 => x + 8 = 9 => x = 1"),
            ("2x + y = 11", 5, "y", 1, "2(5) + y = 11 => 10 + y = 11 => y = 1"),
            ("5x + 3y = 30", 0, "y", 10, "5(0) + 3y = 30 => 3y = 30 => y = 10")
        ],
        'tmpls': [
            "If the point where \\(y = {1}\\) lies on the line \\({0}\\), what is the corresponding value of \\(x\\)?" if "x" == "x" else "Find \\(y\\):",
            "In the linear equation \\({0}\\), if one coordinate is given, find the unknown coordinate such that the point satisfies the equation:",
            "Given the line \\({0}\\), determine the unknown coordinate for the point with given coordinate:",
            "Find the unknown variable if the point lies on \\({0}\\):",
            "Calculate the unknown coordinate of a point lying on the graph of \\({0}\\):",
            "What is the value of the missing coordinate for the line \\({0}\\)?",
            "Evaluate the missing coordinate that satisfies \\({0}\\):",
            "Determine the missing coordinate on the line \\({0}\\):",
            "If a point on \\({0}\\) has known value, find the other value:",
            "Find the missing value for the point on \\({0}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\)",
            [
                f"\\({item[3] + 2}\\)",
                f"\\({item[3] - 2}\\)",
                f"\\({item[1]}\\)"
            ],
            f"**Step 1: Substitute the given coordinate into \\({item[0]}\\).**\n\n**Step 2: Solve the resulting linear equation.**\n{item[4]}.\n\n**Step 3: State the answer.**\nThe unknown value is \\({item[3]}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Points on Coordinate Axes (x-intercept and y-intercept)
    arch4 = {
        'data': [
            ("2x + 3y = 6", "(3, 0)", "(0, 2)", "x-intercept: y=0 => 2x=6 => x=3; y-intercept: x=0 => 3y=6 => y=2"),
            ("3x + 4y = 12", "(4, 0)", "(0, 3)", "x-intercept: 3x=12 => x=4; y-intercept: 4y=12 => y=3"),
            ("x - 2y = 4", "(4, 0)", "(0, -2)", "x-intercept: x=4; y-intercept: -2y=4 => y=-2"),
            ("4x + 5y = 20", "(5, 0)", "(0, 4)", "x-intercept: 4x=20 => x=5; y-intercept: 5y=20 => y=4"),
            ("2x - y = 8", "(4, 0)", "(0, -8)", "x-intercept: 2x=8 => x=4; y-intercept: -y=8 => y=-8"),
            ("3x - 2y = 6", "(2, 0)", "(0, -3)", "x-intercept: 3x=6 => x=2; y-intercept: -2y=6 => y=-3"),
            ("5x + 2y = 10", "(2, 0)", "(0, 5)", "x-intercept: 5x=10 => x=2; y-intercept: 2y=10 => y=5"),
            ("x + 3y = 9", "(9, 0)", "(0, 3)", "x-intercept: x=9; y-intercept: 3y=9 => y=3"),
            ("6x + 7y = 42", "(7, 0)", "(0, 6)", "x-intercept: 6x=42 => x=7; y-intercept: 7y=42 => y=6"),
            ("4x - 3y = 12", "(3, 0)", "(0, -4)", "x-intercept: 4x=12 => x=3; y-intercept: -3y=12 => y=-4")
        ],
        'tmpls': [
            "At what point does the graph of the linear equation \\({0}\\) intersect the \\(x\\)-axis?",
            "Find the coordinates of the point where the line \\({0}\\) crosses the \\(x\\)-axis:",
            "The graph of \\({0}\\) cuts the \\(x\\)-axis at the point:",
            "Determine the \\(x\\)-intercept of the line \\({0}\\) as an ordered pair:",
            "What are the coordinates of the point where \\({0}\\) meets the \\(x\\)-axis?",
            "Calculate the point of intersection of the line \\({0}\\) with the \\(x\\)-axis:",
            "Where does the linear equation \\({0}\\) intersect the \\(x\\)-axis?",
            "Find the point on the \\(x\\)-axis that satisfies \\({0}\\):",
            "The line \\({0}\\) meets the \\(x\\)-axis at:",
            "Evaluate the \\(x\\)-axis intersection coordinates for \\({0}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\)",
            [
                f"\\({item[2]}\\)",
                f"\\((0, 0)\\)",
                f"\\({item[1].replace('0', '1')}\\)"
            ],
            f"**Step 1: Recall the condition for a point on the \\(x\\)-axis.**\nAny point on the \\(x\\)-axis has \\(y = 0\\).\n\n**Step 2: Substitute \\(y = 0\\) into the given equation.**\nSubstitute \\(y = 0\\) into \\({item[0]}\\).\n\n**Step 3: Solve for \\(x\\).**\n{item[3].split(';')[0]}.\nTherefore, the point of intersection is \\({item[1]}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 5: y-intercept coordinates
    arch5 = {
        'data': [
            ("2x + 3y = 6", "(0, 2)", "x=0 => 3y=6 => y=2"),
            ("3x + 4y = 12", "(0, 3)", "x=0 => 4y=12 => y=3"),
            ("x - 2y = 4", "(0, -2)", "x=0 => -2y=4 => y=-2"),
            ("4x + 5y = 20", "(0, 4)", "x=0 => 5y=20 => y=4"),
            ("2x - y = 8", "(0, -8)", "x=0 => -y=8 => y=-8"),
            ("3x - 2y = 6", "(0, -3)", "x=0 => -2y=6 => y=-3"),
            ("5x + 2y = 10", "(0, 5)", "x=0 => 2y=10 => y=5"),
            ("x + 3y = 9", "(0, 3)", "x=0 => 3y=9 => y=3"),
            ("6x + 7y = 42", "(0, 6)", "x=0 => 7y=42 => y=6"),
            ("4x - 3y = 12", "(0, -4)", "x=0 => -3y=12 => y=-4")
        ],
        'tmpls': [
            "At what point does the graph of the linear equation \\({0}\\) intersect the \\(y\\)-axis?",
            "Find the coordinates of the point where the line \\({0}\\) crosses the \\(y\\)-axis:",
            "The graph of \\({0}\\) cuts the \\(y\\)-axis at the point:",
            "Determine the \\(y\\)-intercept of the line \\({0}\\) as an ordered pair:",
            "What are the coordinates of the point where \\({0}\\) meets the \\(y\\)-axis?",
            "Calculate the point of intersection of the line \\({0}\\) with the \\(y\\)-axis:",
            "Where does the linear equation \\({0}\\) intersect the \\(y\\)-axis?",
            "Find the point on the \\(y\\)-axis that satisfies \\({0}\\):",
            "The line \\({0}\\) meets the \\(y\\)-axis at:",
            "Evaluate the \\(y\\)-axis intersection coordinates for \\({0}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\)",
            [
                f"\\({item[1].replace('0', '2')}\\)",
                f"\\((0, 0)\\)",
                f"\\({item[1].replace('-', '') if '-' in item[1] else item[1].replace('(', '(-')}\\)"
            ],
            f"**Step 1: Recall the condition for a point on the \\(y\\)-axis.**\nAny point on the \\(y\\)-axis has \\(x = 0\\).\n\n**Step 2: Substitute \\(x = 0\\) into the equation.**\nSubstitute \\(x = 0\\) into \\({item[0]}\\).\n\n**Step 3: Solve for \\(y\\).**\n{item[2]}.\nTherefore, the point of intersection is \\({item[1]}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 6: One variable vs Two variables Solution Comparison
    arch6 = {
        'data': [
            ("2x + 5 = 0", "A unique point on the number line; a line parallel to y-axis in Cartesian plane", "1 variable vs 2 variables"),
            ("y - 3 = 0", "A unique point on the number line; a line parallel to x-axis in Cartesian plane", "1 variable vs 2 variables"),
            ("3x = 9", "A unique point on the number line; a line parallel to y-axis in Cartesian plane", "1 variable vs 2 variables"),
            ("2y = -6", "A unique point on the number line; a line parallel to x-axis in Cartesian plane", "1 variable vs 2 variables"),
            ("x = 4", "A unique point on the number line; a line parallel to y-axis in Cartesian plane", "1 variable vs 2 variables"),
            ("y = -2", "A unique point on the number line; a line parallel to x-axis in Cartesian plane", "1 variable vs 2 variables"),
            ("5x + 10 = 0", "A unique point on the number line; a line parallel to y-axis in Cartesian plane", "1 variable vs 2 variables"),
            ("4y - 8 = 0", "A unique point on the number line; a line parallel to x-axis in Cartesian plane", "1 variable vs 2 variables"),
            ("x + 7 = 0", "A unique point on the number line; a line parallel to y-axis in Cartesian plane", "1 variable vs 2 variables"),
            ("3y + 12 = 0", "A unique point on the number line; a line parallel to x-axis in Cartesian plane", "1 variable vs 2 variables")
        ],
        'tmpls': [
            "The geometric representation of the linear equation \\({0}\\) in one variable is a point, but in two variables \\(x\\) and \\(y\\) it is:",
            "When \\({0}\\) is treated as a linear equation in two variables, its geometrical representation is:",
            "In the Cartesian plane, the graph of \\({0}\\) represents:",
            "How does the geometric representation of \\({0}\\) change from one variable to two variables?",
            "Treated as an equation in two variables, the graph of \\({0}\\) is:",
            "In two variables, what geometric figure does \\({0}\\) represent?",
            "The equation \\({0}\\) plotted in the Cartesian plane \\((x, y)\\) forms:",
            "Graphically, \\({0}\\) in the two-dimensional coordinate system represents:",
            "In two variables \\(x\\) and \\(y\\), the equation \\({0}\\) is represented by:",
            "What is the graph of \\({0}\\) in two variables?"
        ],
        'calc': lambda item: (
            f"A straight line parallel to the {'y' if 'x' in item[0] else 'x'}-axis",
            [
                f"A straight line parallel to the {'x' if 'x' in item[0] else 'y'}-axis",
                "A single isolated point in the plane",
                "A circle centered at the origin"
            ],
            f"**Step 1: Express the equation in two variables.**\n\\({item[0]}\\) can be written as \\({'1x + 0y' if 'x' in item[0] else '0x + 1y'} = c\\).\n\n**Step 2: Understand the geometric locus.**\nEvery point having the fixed coordinate satisfies the equation, regardless of the value of the other coordinate.\n\n**Step 3: State the geometric figure.**\nIn the Cartesian plane, it represents **a straight line parallel to the {'y' if 'x' in item[0] else 'x'}-axis**."
        ),
        'diff': 'medium'
    }

    # Arch 7: Testing which option is NOT a solution
    arch7 = {
        'data': [
            ("2x + y = 7", "(1, 5)", "(2, 3)", "(3, 1)", "(2, 2)", "(2, 2)", "2(2) + 2 = 6 ≠ 7"),
            ("x - 2y = 4", "(4, 0)", "(6, 1)", "(0, -2)", "(1, 1)", "(1, 1)", "1 - 2(1) = -1 ≠ 4"),
            ("3x + y = 6", "(0, 6)", "(1, 3)", "(2, 0)", "(2, 2)", "(2, 2)", "3(2) + 2 = 8 ≠ 6"),
            ("x + y = 5", "(1, 4)", "(2, 3)", "(0, 5)", "(3, 3)", "(3, 3)", "3 + 3 = 6 ≠ 5"),
            ("4x - y = 8", "(2, 0)", "(3, 4)", "(1, -4)", "(2, 2)", "(2, 2)", "4(2) - 2 = 6 ≠ 8"),
            ("2x - 3y = 6", "(3, 0)", "(0, -2)", "(6, 2)", "(4, 1)", "(4, 1)", "2(4) - 3(1) = 5 ≠ 6"),
            ("3x + 2y = 12", "(4, 0)", "(0, 6)", "(2, 3)", "(1, 4)", "(1, 4)", "3(1) + 2(4) = 11 ≠ 12"),
            ("5x - y = 10", "(2, 0)", "(3, 5)", "(1, -5)", "(0, 10)", "(0, 10)", "5(0) - 10 = -10 ≠ 10"),
            ("x + 2y = 8", "(8, 0)", "(0, 4)", "(4, 2)", "(2, 2)", "(2, 2)", "2 + 2(2) = 6 ≠ 8"),
            ("3x - 4y = 12", "(4, 0)", "(0, -3)", "(8, 3)", "(2, -1)", "(2, -1)", "3(2) - 4(-1) = 10 ≠ 12")
        ],
        'tmpls': [
            "Which of the following points is NOT a solution of the linear equation \\({0}\\)?",
            "Which ordered pair does NOT lie on the line \\({0}\\)?",
            "Identify the point that does NOT satisfy the linear equation \\({0}\\):",
            "Which of the given points is NOT on the graph of \\({0}\\)?",
            "All of the following are solutions of \\({0}\\) EXCEPT:",
            "Find the point that does NOT satisfy \\({0}\\):",
            "Which point is NOT a valid solution of \\({0}\\)?",
            "Determine which of the following is NOT a solution to \\({0}\\):",
            "Which coordinate pair does NOT satisfy \\({0}\\)?",
            "Which of these ordered pairs fails to satisfy \\({0}\\)?"
        ],
        'calc': lambda item: (
            f"\\({item[5]}\\)",
            [
                f"\\({item[1]}\\)",
                f"\\({item[2]}\\)",
                f"\\({item[3]}\\)"
            ],
            f"**Step 1: Test each given point by substituting its coordinates into \\({item[0]}\\).**\n\n**Step 2: Check the invalid point.**\nFor \\({item[5]}\\): {item[6]}.\n\n**Step 3: State the conclusion.**\nThe point that is NOT a solution is \\({item[5]}\\)."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 13.2.2: Finding distinct solution pairs (x, y)
# ==============================================================================
def gen_13_2_2():
    tc = "CBSE-9-MGM-13-13.2.2"
    tname = "Finding distinct solution pairs (x, y)"

    # Arch 0: Finding y given x = 1 in ax + by = c
    arch0 = {
        'data': [
            (2, 1, 7, 1, 5, "2(1) + y = 7 => y = 5"),
            (3, 2, 11, 1, 4, "3(1) + 2y = 11 => 2y = 8 => y = 4"),
            (4, -1, 3, 1, 1, "4(1) - y = 3 => y = 1"),
            (5, 3, 14, 1, 3, "5(1) + 3y = 14 => 3y = 9 => y = 3"),
            (1, 4, 9, 1, 2, "1(1) + 4y = 9 => 4y = 8 => y = 2"),
            (6, -2, 4, 1, 1, "6(1) - 2y = 4 => 2y = 2 => y = 1"),
            (2, 5, 17, 1, 3, "2(1) + 5y = 17 => 5y = 15 => y = 3"),
            (7, 3, 16, 1, 3, "7(1) + 3y = 16 => 3y = 9 => y = 3"),
            (3, -4, -1, 1, 1, "3(1) - 4y = -1 => 4y = 4 => y = 1"),
            (4, 3, 19, 1, 5, "4(1) + 3y = 19 => 3y = 15 => y = 5")
        ],
        'tmpls': [
            "In the linear equation \\({0}x + ({1})y = {2}\\), find the value of \\(y\\) when \\(x = {3}\\):",
            "Find the solution \\(({3}, y)\\) for the equation \\({0}x + ({1})y = {2}\\):",
            "If \\(x = {3}\\), what is \\(y\\) in the equation \\({0}x + ({1})y = {2}\\)?",
            "Calculate \\(y\\) when \\(x = {3}\\) in \\({0}x + ({1})y = {2}\\):",
            "Determine the value of \\(y\\) corresponding to \\(x = {3}\\) for \\({0}x + ({1})y = {2}\\):",
            "Evaluate \\(y\\) for \\(x = {3}\\) in \\({0}x + ({1})y = {2}\\):",
            "What is \\(y\\) if \\(x = {3}\\) satisfies \\({0}x + ({1})y = {2}\\)?",
            "Find \\(y\\) such that \\(({3}, y)\\) is a solution of \\({0}x + ({1})y = {2}\\):",
            "Solve for \\(y\\) when \\(x = {3}\\) in \\({0}x + ({1})y = {2}\\):",
            "Find the value of \\(y\\) when \\(x = {3}\\) in the line \\({0}x + ({1})y = {2}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[4]}\\)",
            [
                f"\\({item[4] + 2}\\)",
                f"\\({item[4] - 2}\\)",
                f"\\({item[2]}\\)"
            ],
            f"**Step 1: Substitute \\(x = {item[3]}\\) into the equation.**\n\\({item[0]}({item[3]}) + ({item[1]})y = {item[2]}\\).\n\n**Step 2: Simplify the linear equation in \\(y\\).**\n{item[5]}.\n\n**Step 3: State the value of \\(y\\).**\n\\(y = {item[4]}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Finding x given y = 2 in ax + by = c
    arch1 = {
        'data': [
            (2, 3, 12, 2, 3, "2x + 3(2) = 12 => 2x = 6 => x = 3"),
            (3, 2, 16, 2, 4, "3x + 2(2) = 16 => 3x = 12 => x = 4"),
            (4, -1, 10, 2, 3, "4x - 2 = 10 => 4x = 12 => x = 3"),
            (5, 3, 21, 2, 3, "5x + 3(2) = 21 => 5x = 15 => x = 3"),
            (1, 4, 13, 2, 5, "x + 4(2) = 13 => x + 8 = 13 => x = 5"),
            (6, -3, 12, 2, 3, "6x - 3(2) = 12 => 6x = 18 => x = 3"),
            (2, 5, 18, 2, 4, "2x + 5(2) = 18 => 2x = 8 => x = 4"),
            (7, 2, 25, 2, 3, "7x + 2(2) = 25 => 7x = 21 => x = 3"),
            (3, -5, 5, 2, 5, "3x - 5(2) = 5 => 3x = 15 => x = 5"),
            (4, 3, 26, 2, 5, "4x + 3(2) = 26 => 4x = 20 => x = 5")
        ],
        'tmpls': [
            "In the linear equation \\({0}x + ({1})y = {2}\\), find the value of \\(x\\) when \\(y = {3}\\):",
            "Find the solution \\((x, {3})\\) for the equation \\({0}x + ({1})y = {2}\\):",
            "If \\(y = {3}\\), what is \\(x\\) in the equation \\({0}x + ({1})y = {2}\\)?",
            "Calculate \\(x\\) when \\(y = {3}\\) in \\({0}x + ({1})y = {2}\\):",
            "Determine the value of \\(x\\) corresponding to \\(y = {3}\\) for \\({0}x + ({1})y = {2}\\):",
            "Evaluate \\(x\\) for \\(y = {3}\\) in \\({0}x + ({1})y = {2}\\):",
            "What is \\(x\\) if \\(y = {3}\\) satisfies \\({0}x + ({1})y = {2}\\)?",
            "Find \\(x\\) such that \\((x, {3})\\) is a solution of \\({0}x + ({1})y = {2}\\):",
            "Solve for \\(x\\) when \\(y = {3}\\) in \\({0}x + ({1})y = {2}\\):",
            "Find the value of \\(x\\) when \\(y = {3}\\) in the line \\({0}x + ({1})y = {2}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[4]}\\)",
            [
                f"\\({item[4] + 2}\\)",
                f"\\({item[4] - 2}\\)",
                f"\\({item[3]}\\)"
            ],
            f"**Step 1: Substitute \\(y = {item[3]}\\) into the equation.**\n\\({item[0]}x + ({item[1]})({item[3]}) = {item[2]}\\).\n\n**Step 2: Simplify and solve for \\(x\\).**\n{item[5]}.\n\n**Step 3: State the value of \\(x\\).**\n\\(x = {item[4]}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Finding 4 Distinct Solutions for 2x + y = 7
    arch2 = {
        'data': [
            ("2x + y = 7", "(0, 7), (1, 5), (2, 3), (3, 1)", "Substitute x = 0, 1, 2, 3 => y = 7, 5, 3, 1"),
            ("x + 2y = 6", "(0, 3), (2, 2), (4, 1), (6, 0)", "Substitute y = 0, 1, 2, 3 => x = 6, 4, 2, 0"),
            ("x - 2y = 4", "(0, -2), (2, -1), (4, 0), (6, 1)", "Substitute y = -2, -1, 0, 1 => x = 0, 2, 4, 6"),
            ("3x + y = 9", "(0, 9), (1, 6), (2, 3), (3, 0)", "Substitute x = 0, 1, 2, 3 => y = 9, 6, 3, 0"),
            ("2x - y = 4", "(0, -4), (1, -2), (2, 0), (3, 2)", "Substitute x = 0, 1, 2, 3 => y = -4, -2, 0, 2"),
            ("x + y = 4", "(0, 4), (1, 3), (2, 2), (3, 1)", "Substitute x = 0, 1, 2, 3 => y = 4, 3, 2, 1"),
            ("3x - y = 3", "(0, -3), (1, 0), (2, 3), (3, 6)", "Substitute x = 0, 1, 2, 3 => y = -3, 0, 3, 6"),
            ("4x + y = 8", "(0, 8), (1, 4), (2, 0), (3, -4)", "Substitute x = 0, 1, 2, 3 => y = 8, 4, 0, -4"),
            ("2x + 3y = 12", "(0, 4), (3, 2), (6, 0), (-3, 6)", "Distinct integer solutions"),
            ("x - y = 2", "(0, -2), (1, -1), (2, 0), (3, 1)", "Substitute x = 0, 1, 2, 3 => y = -2, -1, 0, 1")
        ],
        'tmpls': [
            "Which of the following sets represents four distinct solutions of the linear equation \\({0}\\)?",
            "Four distinct solutions of the equation \\({0}\\) are given by:",
            "Find four different solutions for the equation \\({0}\\):",
            "Which set of four ordered pairs all satisfy the equation \\({0}\\)?",
            "Identify four distinct points that all lie on the graph of \\({0}\\):",
            "Determine four solutions for the linear equation \\({0}\\):",
            "Which group of 4 points are all valid solutions of \\({0}\\)?",
            "Evaluate four solution pairs \\((x, y)\\) for \\({0}\\):",
            "Four solutions of \\({0}\\) can be written as:",
            "Select the set containing four correct solutions to \\({0}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\)",
            [
                f"\\({item[1].replace('3', '5')}\\)",
                f"\\({item[1].replace('0', '2')}\\)",
                "\\((1, 1), (2, 2), (3, 3), (4, 4)\\)"
            ],
            f"**Step 1: Express one variable in terms of the other.**\nFrom \\({item[0]}\\), solve for \\(y\\).\n\n**Step 2: Choose 4 convenient values for \\(x\\).**\n{item[2]}.\n\n**Step 3: Collect the four solution pairs.**\n\\({item[1]}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Solutions of πx + y = 9 (NCERT Classic)
    arch3 = {
        'data': [
            ("x = 0", "9", "(0, 9)", "π(0) + y = 9 => y = 9"),
            ("x = 1", "9 - \\pi", "(1, 9 - \\pi)", "π(1) + y = 9 => y = 9 - π"),
            ("x = 2", "9 - 2\\pi", "(2, 9 - 2\\pi)", "π(2) + y = 9 => y = 9 - 2π"),
            ("x = -1", "9 + \\pi", "(-1, 9 + \\pi)", "π(-1) + y = 9 => y = 9 + π"),
            ("y = 0", "\\frac{9}{\\pi}", "(\\frac{9}{\\pi}, 0)", "πx + 0 = 9 => x = 9/π"),
            ("x = 3", "9 - 3\\pi", "(3, 9 - 3\\pi)", "π(3) + y = 9 => y = 9 - 3π"),
            ("x = -2", "9 + 2\\pi", "(-2, 9 + 2\\pi)", "π(-2) + y = 9 => y = 9 + 2π"),
            ("y = 9", "0", "(0, 9)", "πx + 9 = 9 => πx = 0 => x = 0"),
            ("x = \\frac{1}{\\pi}", "8", "(\\frac{1}{\\pi}, 8)", "π(1/π) + y = 9 => 1 + y = 9 => y = 8"),
            ("y = 9 - \\pi", "1", "(1, 9 - \\pi)", "πx + 9 - π = 9 => πx = π => x = 1")
        ],
        'tmpls': [
            "For the linear equation \\(\\pi x + y = 9\\), find the value of the unknown when \\({0}\\):",
            "In \\(\\pi x + y = 9\\), what is the value of the corresponding coordinate when \\({0}\\)?",
            "If \\({0}\\) in the equation \\(\\pi x + y = 9\\), find the other coordinate:",
            "Find the solution of \\(\\pi x + y = 9\\) corresponding to \\({0}\\):",
            "Calculate the unknown coordinate when \\({0}\\) in \\(\\pi x + y = 9\\):",
            "What is the value of the missing variable for \\(\\pi x + y = 9\\) given \\({0}\\)?",
            "Determine the corresponding coordinate on \\(\\pi x + y = 9\\) when \\({0}\\):",
            "Evaluate the other coordinate on the line \\(\\pi x + y = 9\\) where \\({0}\\):",
            "For \\(\\pi x + y = 9\\), find the value when \\({0}\\):",
            "In the line \\(\\pi x + y = 9\\), what is the coordinate when \\({0}\\)?"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\)",
            [
                f"\\({item[1]}\\pi\\)" if "\\pi" not in item[1] else f"\\({item[1].replace('\\pi', '')}\\)",
                f"\\(9\\)",
                f"\\(0\\)"
            ],
            f"**Step 1: Write down the linear equation.**\n\\(\\pi x + y = 9\\).\n\n**Step 2: Substitute \\({item[0]}\\).**\n{item[3]}.\n\n**Step 3: State the resulting value.**\nThe value is \\({item[1]}\\) (giving point \\({item[2]}\\))."
        ),
        'diff': 'medium'
    }

    # Arch 4: Proportional Solutions of x = 4y
    arch4 = {
        'data': [
            (0, 0, "(0, 0)", "y = 0 => x = 4(0) = 0"),
            (1, 4, "(4, 1)", "y = 1 => x = 4(1) = 4"),
            (2, 8, "(8, 2)", "y = 2 => x = 4(2) = 8"),
            (-1, -4, "(-4, -1)", "y = -1 => x = 4(-1) = -4"),
            (3, 12, "(12, 3)", "y = 3 => x = 4(3) = 12"),
            (-2, -8, "(-8, -2)", "y = -2 => x = 4(-2) = -8"),
            (4, 16, "(16, 4)", "y = 4 => x = 4(4) = 16"),
            (0.5, 2, "(2, 0.5)", "y = 0.5 => x = 4(0.5) = 2"),
            (5, 20, "(20, 5)", "y = 5 => x = 4(5) = 20"),
            (-3, -12, "(-12, -3)", "y = -3 => x = 4(-3) = -12")
        ],
        'tmpls': [
            "In the linear equation \\(x = 4y\\), find the value of \\(x\\) when \\(y = {0}\\):",
            "What is \\(x\\) when \\(y = {0}\\) in the equation \\(x = 4y\\)?",
            "Find the solution \\((x, {0})\\) for the line \\(x = 4y\\):",
            "Calculate \\(x\\) for \\(y = {0}\\) in \\(x = 4y\\):",
            "Determine the point on the line \\(x = 4y\\) having \\(y\\)-coordinate equal to \\({0}\\):",
            "Evaluate \\(x\\) when \\(y = {0}\\) in \\(x = 4y\\):",
            "If \\(y = {0}\\), find \\(x\\) such that \\((x, y)\\) satisfies \\(x = 4y\\):",
            "What is the \\(x\\)-coordinate for the point on \\(x = 4y\\) where \\(y = {0}\\)?",
            "Find \\(x\\) given \\(y = {0}\\) for the line \\(x = 4y\\):",
            "For \\(x = 4y\\), calculate \\(x\\) corresponding to \\(y = {0}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\)",
            [
                f"\\({item[0]}\\)",
                f"\\({item[1] + 2}\\)",
                f"\\({item[1] - 2}\\)"
            ],
            f"**Step 1: Write down the equation.**\n\\(x = 4y\\).\n\n**Step 2: Substitute \\(y = {item[0]}\\).**\n\\(x = 4 \\times ({item[0]}) = {item[1]}\\).\n\n**Step 3: State the solution.**\n\\(x = {item[1]}\\) (giving the point \\({item[2]}\\))."
        ),
        'diff': 'easy'
    }

    # Arch 5: Integer Solution Pairs in Standard Form
    arch5 = {
        'data': [
            ("3x + 5y = 30", 5, 3, "(5, 3)", "3(5) + 5(3) = 15 + 15 = 30"),
            ("2x + 7y = 28", 7, 2, "(7, 2)", "2(7) + 7(2) = 14 + 14 = 28"),
            ("4x + 3y = 24", 3, 4, "(3, 4)", "4(3) + 3(4) = 12 + 12 = 24"),
            ("5x + 4y = 40", 4, 5, "(4, 5)", "5(4) + 4(5) = 20 + 20 = 40"),
            ("3x + 2y = 18", 4, 3, "(4, 3)", "3(4) + 2(3) = 12 + 6 = 18"),
            ("2x + 5y = 20", 5, 2, "(5, 2)", "2(5) + 5(2) = 10 + 10 = 20"),
            ("6x + 5y = 60", 5, 6, "(5, 6)", "6(5) + 5(6) = 30 + 30 = 60"),
            ("7x + 3y = 35", 2, 7, "(2, 7)", "7(2) + 3(7) = 14 + 21 = 35"),
            ("4x + 5y = 30", 5, 2, "(5, 2)", "4(5) + 5(2) = 20 + 10 = 30"),
            ("3x + 4y = 25", 3, 4, "(3, 4)", "3(3) + 4(4) = 9 + 16 = 25")
        ],
        'tmpls': [
            "Which of the following integer pairs \\((x, y)\\) satisfies the equation \\({0}\\)?",
            "An integer solution of the linear equation \\({0}\\) is:",
            "Find an integer solution pair for \\({0}\\):",
            "Which pair of positive integers satisfies \\({0}\\)?",
            "Identify the integer solution \\((x, y)\\) that lies on the line \\({0}\\):",
            "Determine an integer coordinate solution for \\({0}\\):",
            "Which of the following points with integer coordinates satisfies \\({0}\\)?",
            "Evaluate which integer pair is a solution to \\({0}\\):",
            "An integer point satisfying \\({0}\\) is:",
            "Select the integer solution pair \\((x, y)\\) of \\({0}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\)",
            [
                f"\\(({item[1] + 1}, {item[2] - 1})\\)",
                f"\\(({item[1]}, {item[2] + 1})\\)",
                f"\\((1, 1)\\)"
            ],
            f"**Step 1: Test the point \\({item[3]}\\) in \\({item[0]}\\).**\nSubstitute \\(x = {item[1]}\\) and \\(y = {item[2]}\\).\n\n**Step 2: Evaluate the LHS.**\n{item[4]}.\nSince LHS = RHS, the point satisfies the equation.\n\n**Step 3: State the answer.**\nThe integer solution is \\({item[3]}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 6: Solutions with Negative Coordinates
    arch6 = {
        'data': [
            ("x - y = 5", -2, -7, "(-2, -7)", "-2 - (-7) = -2 + 7 = 5"),
            ("2x + y = 3", -1, 5, "(-1, 5)", "2(-1) + 5 = -2 + 5 = 3"),
            ("x + 2y = -4", -2, -1, "(-2, -1)", "-2 + 2(-1) = -4"),
            ("3x - y = -8", -2, 2, "(-2, 2)", "3(-2) - 2 = -6 - 2 = -8"),
            ("2x - 3y = -1", -2, -1, "(-2, -1)", "2(-2) - 3(-1) = -4 + 3 = -1"),
            ("x - 3y = 7", -2, -3, "(-2, -3)", "-2 - 3(-3) = -2 + 9 = 7"),
            ("4x + y = -6", -2, 2, "(-2, 2)", "4(-2) + 2 = -8 + 2 = -6"),
            ("2x + 3y = -5", -1, -1, "(-1, -1)", "2(-1) + 3(-1) = -5"),
            ("3x + 2y = -7", -1, -2, "(-1, -2)", "3(-1) + 2(-2) = -7"),
            ("x + y = -3", -2, -1, "(-2, -1)", "-2 + (-1) = -3")
        ],
        'tmpls': [
            "In the linear equation \\({0}\\), find \\(y\\) when \\(x = {1}\\):",
            "If \\(x = {1}\\), what is \\(y\\) in the equation \\({0}\\)?",
            "Find the solution \\(({1}, y)\\) for the equation \\({0}\\):",
            "Calculate \\(y\\) when \\(x = {1}\\) in \\({0}\\):",
            "Determine \\(y\\) corresponding to \\(x = {1}\\) for the line \\({0}\\):",
            "Evaluate \\(y\\) for \\(x = {1}\\) in \\({0}\\):",
            "What is \\(y\\) if \\(x = {1}\\) satisfies \\({0}\\)?",
            "Find \\(y\\) such that \\(({1}, y)\\) is on the line \\({0}\\):",
            "Solve for \\(y\\) when \\(x = {1}\\) in \\({0}\\):",
            "Find the value of \\(y\\) for \\(x = {1}\\) in \\({0}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\)",
            [
                f"\\({item[2] + 2}\\)",
                f"\\({item[2] - 2}\\)",
                f"\\({-item[2]}\\)"
            ],
            f"**Step 1: Substitute \\(x = {item[1]}\\) into the equation \\({item[0]}\\).**\n\n**Step 2: Solve for \\(y\\).**\n{item[4]}.\n\n**Step 3: State the value of \\(y\\).**\n\\(y = {item[2]}\\) (giving point \\({item[3]}\\))."
        ),
        'diff': 'medium'
    }

    # Arch 7: Parametric / General Form Solution Representation (x = t)
    arch7 = {
        'data': [
            ("y = 2x + 3", "(t, 2t + 3)", "For any real number t, x = t gives y = 2t + 3"),
            ("y = 3x - 1", "(t, 3t - 1)", "General parametric solution"),
            ("x + y = 6", "(t, 6 - t)", "General parametric solution"),
            ("2x + y = 5", "(t, 5 - 2t)", "General parametric solution"),
            ("x - 2y = 4", "(2t + 4, t)", "Parametric solution in terms of y = t"),
            ("y = 4x", "(t, 4t)", "Proportional parametric solution"),
            ("3x + y = 10", "(t, 10 - 3t)", "General parametric solution"),
            ("x - y = 7", "(t, t - 7)", "General parametric solution"),
            ("2x - y = 8", "(t, 2t - 8)", "General parametric solution"),
            ("y = -x + 2", "(t, 2 - t)", "General parametric solution")
        ],
        'tmpls': [
            "If \\(x = t\\) (where \\(t\\) is any real parameter), what is the general parametric form of solutions for \\({0}\\)?",
            "Which parametric form represents all solutions of \\({0}\\) in terms of parameter \\(t\\)?",
            "Any solution of the equation \\({0}\\) can be written in the form:",
            "Express the general solution of \\({0}\\) taking \\(x = t\\):",
            "What is the parametric coordinate pair \\((x, y)\\) for \\({0}\\) with parameter \\(t\\)?",
            "In terms of a real parameter \\(t\\), every point on the line \\({0}\\) has coordinates:",
            "The set of all solutions of \\({0}\\) is described by:",
            "Determine the general parametric solution \\((x, y)\\) of \\({0}\\):",
            "Evaluate the parametric form of solutions of \\({0}\\):",
            "Which representation gives all points on the line \\({0}\\) for real parameter \\(t\\)?"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\)",
            [
                f"\\((t, t)\\)",
                f"\\((t, -t)\\)",
                f"\\({item[1].replace('+', '-') if '+' in item[1] else item[1].replace('-', '+')}\\)"
            ],
            f"**Step 1: Express \\(y\\) explicitly in terms of \\(x\\).**\nFrom \\({item[0]}\\), solve for \\(y\\).\n\n**Step 2: Let \\(x = t\\) where \\(t \\in \\mathbb{{R}}\\).**\nSubstitute \\(x = t\\) to get \\(y\\) in terms of \\(t\\).\n\n**Step 3: State the general parametric solution.**\n\\({item[1]}\\)."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_13_2_1()
    q2 = gen_13_2_2()
    print(f"gen_13_2_1: {len(q1)} questions")
    print(f"gen_13_2_2: {len(q2)} questions")
