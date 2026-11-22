# scripts/build_cbse9_mgm_ch13_part3.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 13: Two Variables, One Line
Part 3:
- Subtopic 13.3.1: Plotting solutions and drawing straight line graph
- Subtopic 13.3.2: Equations of lines parallel to axes (x = k, y = k)
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 13
CH_NAME = "Two Variables, One Line"

# ==============================================================================
# SUBTOPIC 13.3.1: Plotting solutions and drawing straight line graph
# ==============================================================================
def gen_13_3_1():
    tc = "CBSE-9-MGM-13-13.3.1"
    tname = "Plotting solutions and drawing straight line graph"

    # Arch 0: Minimum points needed to draw graph of linear equation
    arch0 = {
        'data': [
            (2, "Two points", "Axiom 5.1: Given two distinct points, there is a unique line that passes through them"),
            (3, "Three points", "Third point is used as a check/verification"),
            (1, "One point", "Infinitely many lines pass through one point"),
            (4, "Four points", "Redundant, two are sufficient"),
            (2, "Two distinct points", "Two points uniquely determine a straight line"),
            (2, "2 points", "Minimal geometric requirement"),
            (2, "At least two points", "Euclidean postulate"),
            (2, "Two points", "Standard method for plotting ax + by + c = 0"),
            (2, "Two points", "Sufficient to draw graph"),
            (2, "Two points", "Unique line property")
        ],
        'tmpls': [
            "What is the minimum number of points required to uniquely plot and draw the graph of a linear equation in two variables?",
            "To draw the graph of a linear equation in two variables, the minimum number of distinct points needed is:",
            "How many distinct solution points are minimally necessary to determine a straight line graph?",
            "A unique straight line graph of \\(ax + by + c = 0\\) can be drawn by plotting at least how many points?",
            "What is the minimum number of solutions of \\(ax + by + c = 0\\) that must be plotted to draw its graph?",
            "To graph a linear equation in two variables, at least how many coordinate pairs must be plotted?",
            "The minimum number of points needed to fix the position of a straight line on the Cartesian plane is:",
            "How many points are minimally required to graph \\(2x + 3y = 6\\)?",
            "In coordinate geometry, the minimum number of points needed to plot a linear equation is:",
            "To draw the graph of any linear equation in two variables, we need at least:"
        ],
        'calc': lambda item: (
            "\\(2\\) points",
            [
                "\\(1\\) point",
                "\\(3\\) points",
                "\\(4\\) points"
            ],
            "**Step 1: State Euclid's axiom on lines.**\nGiven two distinct points, there is one and only one line that passes through both of them.\n\n**Step 2: Connect to linear equations.**\nThe graph of a linear equation in two variables is a straight line.\n\n**Step 3: Conclude the minimum requirement.**\nTherefore, at least **2 points** are required to draw the graph uniquely."
        ),
        'diff': 'easy'
    }

    # Arch 1: Area of Triangle Formed by Line with Coordinate Axes
    arch1 = {
        'data': [
            (2, 3, 6, 3, 2, 3.0, "x-int = 3, y-int = 2 => Area = 1/2 * 3 * 2 = 3 sq units"),
            (3, 4, 12, 4, 3, 6.0, "x-int = 4, y-int = 3 => Area = 1/2 * 4 * 3 = 6 sq units"),
            (1, 2, 4, 4, 2, 4.0, "x-int = 4, y-int = 2 => Area = 1/2 * 4 * 2 = 4 sq units"),
            (4, 5, 20, 5, 4, 10.0, "x-int = 5, y-int = 4 => Area = 1/2 * 5 * 4 = 10 sq units"),
            (2, 5, 10, 5, 2, 5.0, "x-int = 5, y-int = 2 => Area = 1/2 * 5 * 2 = 5 sq units"),
            (6, 7, 42, 7, 6, 21.0, "x-int = 7, y-int = 6 => Area = 1/2 * 7 * 6 = 21 sq units"),
            (3, 2, 6, 2, 3, 3.0, "x-int = 2, y-int = 3 => Area = 1/2 * 2 * 3 = 3 sq units"),
            (5, 3, 15, 3, 5, 7.5, "x-int = 3, y-int = 5 => Area = 1/2 * 3 * 5 = 7.5 sq units"),
            (4, 3, 12, 3, 4, 6.0, "x-int = 3, y-int = 4 => Area = 1/2 * 3 * 4 = 6 sq units"),
            (1, 1, 6, 6, 6, 18.0, "x-int = 6, y-int = 6 => Area = 1/2 * 6 * 6 = 18 sq units")
        ],
        'tmpls': [
            "Find the area of the triangle formed by the line \\({0}x + {1}y = {2}\\) with the coordinate axes:",
            "What is the area of the triangle enclosed by the line \\({0}x + {1}y = {2}\\) and the two axes?",
            "Calculate the area of the right triangle formed by the line \\({0}x + {1}y = {2}\\) and the coordinate axes:",
            "The line \\({0}x + {1}y = {2}\\) intersects the axes at two points. What is the area of the triangle formed with the origin?",
            "Determine the area of the triangle bounded by \\({0}x + {1}y = {2}\\), the \\(x\\)-axis, and the \\(y\\)-axis:",
            "Compute the area of the triangle formed by the graph of \\({0}x + {1}y = {2}\\) with the axes:",
            "Evaluate the area of the triangular region enclosed by \\({0}x + {1}y = {2}\\) and the axes:",
            "Find the area of \\(\\triangle OAB\\) where \\(A, B\\) are intercepts of \\({0}x + {1}y = {2}\\) on the axes:",
            "What is the area of the triangle bounded by the coordinate axes and the line \\({0}x + {1}y = {2}\\)?",
            "Calculate the area enclosed between \\({0}x + {1}y = {2}\\) and the coordinate planes:"
        ],
        'calc': lambda item: (
            f"\\({item[5]}\\text{{ sq units}}\\)",
            [
                f"\\({item[5] * 2}\\text{{ sq units}}\\)",
                f"\\({item[5] + 2}\\text{{ sq units}}\\)",
                f"\\({item[3] + item[4]}\\text{{ sq units}}\\)"
            ],
            f"**Step 1: Find the intercepts on the coordinate axes.**\n- Put \\(y = 0 \\implies {item[0]}x = {item[2]} \\implies x = {item[3]}\\) (Base \\(= {item[3]}\\)).\n- Put \\(x = 0 \\implies {item[1]}y = {item[2]} \\implies y = {item[4]}\\) (Height \\(= {item[4]}\\)).\n\n**Step 2: Apply the right-triangle area formula.**\n\\(\\text{{Area}} = \\frac{1}{2} \\times \\text{{base}} \\times \\text{{height}} = \\frac{1}{2} \\times {item[3]} \\times {item[4]}\\).\n\n**Step 3: Calculate the area.**\n\\(\\text{{Area}} = {item[5]}\\text{{ sq units}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Number of Lines Passing Through a Given Point
    arch2 = {
        'data': [
            ("(2, 14)", "Infinitely many lines", "Through one point, infinitely many lines can be drawn (e.g., 7x - y = 0, x + y = 16)"),
            ("(1, 2)", "Infinitely many lines", "Through any single point, infinite lines pass"),
            ("(0, 0)", "Infinitely many lines", "Family of lines y = mx"),
            ("(3, 5)", "Infinitely many lines", "Infinitely many straight lines pass through a point"),
            ("(-2, 4)", "Infinitely many lines", "Infinite lines satisfy ax + by + c = 0"),
            ("(4, -3)", "Infinitely many lines", "Through one point in the plane, infinitely many lines pass"),
            ("(5, 1)", "Infinitely many lines", "Infinitely many linear equations have this point as solution"),
            ("(-1, -1)", "Infinitely many lines", "Infinite lines pass through any single point"),
            ("(6, 0)", "Infinitely many lines", "Infinite lines pass through this point on the x-axis"),
            ("(0, -7)", "Infinitely many lines", "Infinite lines pass through this point on the y-axis")
        ],
        'tmpls': [
            "How many linear equations in \\(x\\) and \\(y\\) can be satisfied by \\(x = {0[1]}, y = {0[2]}\\)?" if False else "How many straight lines can pass through the point \\({0}\\)?",
            "How many linear equations can have \\({0}\\) as their solution?",
            "The number of straight lines passing through the point \\({0}\\) is:",
            "How many lines pass through the given point \\({0}\\)?",
            "Through the point \\({0}\\), how many distinct straight lines can be drawn?",
            "What is the total number of lines that pass through \\({0}\\)?",
            "How many linear equations in two variables are satisfied by the point \\({0}\\)?",
            "Through the coordinate point \\({0}\\), there exist:",
            "Determine the number of straight lines that pass through \\({0}\\):",
            "How many lines in the coordinate plane pass through \\({0}\\)?"
        ],
        'calc': lambda item: (
            "Infinitely many lines",
            [
                "Only one line",
                "Only two lines",
                "Zero lines"
            ],
            f"**Step 1: State Euclid's axiom on lines through a point.**\nThrough a given single point, infinitely many straight lines can be drawn in various directions.\n\n**Step 2: Express in terms of linear equations.**\nFor the point \\({item[0]}\\), we can construct equations like \\(x + y = c\\), \\(y = mx + c\\), etc., with different slopes.\n\n**Step 3: Conclude the answer.**\nThere are **infinitely many lines** passing through \\({item[0]}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 3: Intersection of Two Straight Lines
    arch3 = {
        'data': [
            ("x + y = 4", "x - y = 2", "(3, 1)", "2x = 6 => x = 3, y = 1"),
            ("x + y = 7", "x - y = 3", "(5, 2)", "2x = 10 => x = 5, y = 2"),
            ("x + y = 10", "x - y = 4", "(7, 3)", "2x = 14 => x = 7, y = 3"),
            ("2x + y = 8", "2x - y = 4", "(3, 2)", "4x = 12 => x = 3, y = 2"),
            ("x + 2y = 8", "x - 2y = 0", "(4, 2)", "2x = 8 => x = 4, y = 2"),
            ("3x + y = 11", "3x - y = 7", "(3, 2)", "6x = 18 => x = 3, y = 2"),
            ("x + y = 5", "x - y = 1", "(3, 2)", "2x = 6 => x = 3, y = 2"),
            ("2x + 3y = 13", "2x - 3y = -5", "(2, 3)", "4x = 8 => x = 2, y = 3"),
            ("x + 3y = 10", "x - 3y = 4", "(7, 1)", "2x = 14 => x = 7, y = 1"),
            ("4x + y = 9", "4x - y = 7", "(2, 1)", "8x = 16 => x = 2, y = 1")
        ],
        'tmpls': [
            "Find the point of intersection of the graphs of the two linear equations \\({0}\\) and \\({1}\\):",
            "At which point do the lines \\({0}\\) and \\({1}\\) intersect?",
            "What are the coordinates of the common solution of \\({0}\\) and \\({1}\\)?",
            "Calculate the intersection point of the straight lines \\({0}\\) and \\({1}\\):",
            "The graphs of \\({0}\\) and \\({1}\\) cross each other at:",
            "Determine the point of concurrency of the lines \\({0}\\) and \\({1}\\):",
            "Where do the lines \\({0}\\) and \\({1}\\) meet on the Cartesian plane?",
            "Evaluate the point of intersection of lines \\({0}\\) and \\({1}\\):",
            "Find the common point of the linear graphs \\({0}\\) and \\({1}\\):",
            "The lines \\({0}\\) and \\({1}\\) intersect at the ordered pair:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\)",
            [
                f"\\((1, 1)\\)",
                f"\\((0, 0)\\)",
                f"\\({item[2].replace('1', '2') if '1' in item[2] else item[2].replace('2', '1')}\\)"
            ],
            f"**Step 1: Add the two linear equations.**\n\\(({item[0].split('=')[0]}) + ({item[1].split('=')[0]}) = ({item[0].split('=')[1]}) + ({item[1].split('=')[1]})\\).\n\n**Step 2: Solve for the first variable.**\n{item[3]}.\n\n**Step 3: State the point of intersection.**\nThe graphs intersect at \\({item[2]}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Work Done - Force Problem (NCERT Classic)
    arch4 = {
        'data': [
            (5, 2, 10, "Work = Force * Distance = 5 * 2 = 10 units"),
            (5, 0, 0, "Work = 5 * 0 = 0 units"),
            (5, 3, 15, "Work = 5 * 3 = 15 units"),
            (5, 4, 20, "Work = 5 * 4 = 20 units"),
            (6, 3, 18, "Work = 6 * 3 = 18 units"),
            (4, 5, 20, "Work = 4 * 5 = 20 units"),
            (3, 4, 12, "Work = 3 * 4 = 12 units"),
            (8, 2, 16, "Work = 8 * 2 = 16 units"),
            (7, 3, 21, "Work = 7 * 3 = 21 units"),
            (10, 5, 50, "Work = 10 * 5 = 50 units")
        ],
        'tmpls': [
            "If the work done (\\(y\\)) by a body on application of a constant force of \\({0}\\text{{ units}}\\) is proportional to the distance travelled (\\(x\\)), what is the work done when distance is \\({1}\\text{{ units}}\\)?:",
            "Taking a constant force of \\({0}\\text{{ units}}\\) with equation \\(y = {0}x\\), find the work done \\(y\\) when the distance travelled \\(x = {1}\\text{{ units}}\\):",
            "In \\(y = {0}x\\) (where \\(y\\) is work done and \\(x\\) is distance under constant force \\({0}\\)), find \\(y\\) for \\(x = {1}\\):",
            "Calculate the work done \\(y\\) when a force of \\({0}\\text{{ units}}\\) moves a body through a distance of \\({1}\\text{{ units}}\\) (\\(y = {0}x\\)):",
            "What is the work done corresponding to distance \\({1}\\text{{ units}}\\) if force is constant at \\({0}\\text{{ units}}\\)?:",
            "Evaluate the work done \\(y\\) for distance \\(x = {1}\\text{{ units}}\\) in \\(y = {0}x\\):",
            "Determine the work done when distance travelled is \\({1}\\text{{ units}}\\) under a constant force of \\({0}\\text{{ units}}\\):",
            "Find \\(y\\) (work done) from the graph \\(y = {0}x\\) when \\(x = {1}\\text{{ units}}\\):",
            "Under constant force \\({0}\\text{{ units}}\\), find the work done when the body moves \\({1}\\text{{ units}}\\):",
            "Using \\(y = {0}x\\), calculate work done \\(y\\) for \\(x = {1}\\text{{ units}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ units}}\\)",
            [
                f"\\({item[2] + 5}\\text{{ units}}\\)",
                f"\\({item[0] + item[1]}\\text{{ units}}\\)",
                f"\\({item[0]}\\text{{ units}}\\)"
            ],
            f"**Step 1: Write down the linear work-force equation.**\n\\(y = {item[0]}x\\), where \\(y\\) is work done and \\(x\\) is distance.\n\n**Step 2: Substitute the distance \\(x = {item[1]}\\text{{ units}}\\).**\n\\(y = {item[0]} \\times {item[1]}\\).\n\n**Step 3: Calculate the work done.**\n\\(y = {item[2]}\\text{{ units}}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 5: Quadrants Traversed by a Straight Line
    arch5 = {
        'data': [
            ("x + y = 4", "Quadrant III", "Passes through I, II, IV; does not pass through III"),
            ("x - y = 4", "Quadrant II", "Passes through I, III, IV; does not pass through II"),
            ("-x + y = 4", "Quadrant IV", "Passes through I, II, III; does not pass through IV"),
            ("-x - y = 4", "Quadrant I", "Passes through II, III, IV; does not pass through I"),
            ("2x + 3y = 6", "Quadrant III", "Passes through I, II, IV; does not pass through III"),
            ("3x - 2y = 6", "Quadrant II", "Passes through I, III, IV; does not pass through II"),
            ("x + 2y = 8", "Quadrant III", "Passes through I, II, IV; does not pass through III"),
            ("2x - 5y = 10", "Quadrant II", "Passes through I, III, IV; does not pass through II"),
            ("4x + 3y = 12", "Quadrant III", "Passes through I, II, IV; does not pass through III"),
            ("5x - 2y = 10", "Quadrant II", "Passes through I, III, IV; does not pass through II")
        ],
        'tmpls': [
            "The graph of the linear equation \\({0}\\) does NOT pass through which quadrant?",
            "Through which quadrant does the line \\({0}\\) NOT pass?",
            "Which quadrant is completely avoided by the graph of \\({0}\\)?",
            "The straight line \\({0}\\) fails to pass through:",
            "Identify the quadrant in which no point of the line \\({0}\\) lies:",
            "Which of the four quadrants does NOT contain any part of the graph of \\({0}\\)?",
            "Determine the quadrant that the line \\({0}\\) does NOT traverse:",
            "The line \\({0}\\) intersects coordinate axes in positive territory. Which quadrant does it miss?",
            "Which quadrant has no intersection with the line \\({0}\\)?",
            "The graph of \\({0}\\) passes through three quadrants. Which is the excluded quadrant?"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Quadrant I",
                "Quadrant IV" if item[1] != "Quadrant IV" else "Quadrant II",
                "None; it passes through all 4 quadrants"
            ],
            f"**Step 1: Find the intercepts on the axes.**\nFor \\({item[0]}\\), find the \\(x\\)-intercept and \\(y\\)-intercept.\n\n**Step 2: Trace the line segment connecting the intercepts.**\n{item[2]}.\n\n**Step 3: Identify the excluded quadrant.**\nThe line does not pass through **{item[1]}**."
        ),
        'diff': 'medium'
    }

    # Arch 6: Collinearity of Three Points Tested via Linear Equation
    arch6 = {
        'data': [
            ("y = 2x", "(1, 2), (2, 4), (3, 6)", "Collinear", "All three points satisfy y = 2x"),
            ("x + y = 5", "(1, 4), (2, 3), (3, 2)", "Collinear", "All three points satisfy x + y = 5"),
            ("y = 3x - 1", "(0, -1), (1, 2), (2, 5)", "Collinear", "All three points satisfy y = 3x - 1"),
            ("2x - y = 1", "(1, 1), (2, 3), (3, 5)", "Collinear", "All three points satisfy 2x - y = 1"),
            ("x - y = 0", "(1, 1), (2, 2), (3, 3)", "Collinear", "All three points lie on line y = x"),
            ("3x + y = 6", "(0, 6), (1, 3), (2, 0)", "Collinear", "All three points satisfy 3x + y = 6"),
            ("x + 2y = 4", "(0, 2), (2, 1), (4, 0)", "Collinear", "All three points satisfy x + 2y = 4"),
            ("y = -x + 3", "(0, 3), (1, 2), (2, 1)", "Collinear", "All three points satisfy y = -x + 3"),
            ("4x - y = 0", "(1, 4), (2, 8), (3, 12)", "Collinear", "All three points satisfy y = 4x"),
            ("2x + 3y = 12", "(0, 4), (3, 2), (6, 0)", "Collinear", "All three points satisfy 2x + 3y = 12")
        ],
        'tmpls': [
            "Are the three points \\({1}\\) collinear?",
            "Do the three points \\({1}\\) lie on the same straight line?",
            "Check whether the points \\({1}\\) are collinear:",
            "Determine if the points \\({1}\\) lie on a single straight line graph:",
            "Verify the collinearity of the three points \\({1}\\):",
            "What is the geometric relationship among the three points \\({1}\\)?",
            "The points \\({1}\\) all satisfy the equation \\({0}\\). Therefore they are:",
            "Are the points \\({1}\\) on the line \\({0}\\)?",
            "Can a single straight line pass through all three points \\({1}\\)?",
            "The points \\({1}\\) are:"
        ],
        'calc': lambda item: (
            "Yes, they are collinear (lie on the same straight line)",
            [
                "No, they form a triangle",
                "Only two of them lie on the line",
                "Cannot be determined"
            ],
            f"**Step 1: Test the coordinates in the equation \\({item[0]}\\).**\nSubstitute each of the three points \\({item[1]}\\) into the equation.\n\n**Step 2: Verify satisfaction.**\n{item[3]}.\n\n**Step 3: Conclude collinearity.**\nSince all three points satisfy the linear equation, they lie on the same straight line and are **collinear**."
        ),
        'diff': 'medium'
    }

    # Arch 7: Slope-Intercept Properties / Nature of the Graph
    arch7 = {
        'data': [
            ("ax + by + c = 0", "A straight line", "The degree of the equation is 1 in both variables"),
            ("Every point on the line", "Is a solution of the equation", "One-to-one geometric-algebraic correspondence"),
            ("Every solution of the equation", "Corresponds to a point on the line", "Fundamental theorem of analytic geometry"),
            ("Graph of x = 0", "The y-axis", "x is 0 everywhere on the y-axis"),
            ("Graph of y = 0", "The x-axis", "y is 0 everywhere on the x-axis"),
            ("Graph of y = mx", "A line passing through the origin", "Constant term c = 0"),
            ("Graph of y = mx + c", "A line with y-intercept c", "Slope-intercept form"),
            ("Points not on the line", "Do not satisfy the equation", "Non-solutions"),
            ("Linear polynomial equation", "Straight line locus", "Geometric definition"),
            ("Graph of 2-variable linear equation", "Always a straight line", "Degree 1 in both variables")
        ],
        'tmpls': [
            "The geometrical representation of any linear equation in two variables \\(ax + by + c = 0\\) is always:",
            "The graph of every linear equation in two variables represents:",
            "What shape is formed on the Cartesian plane by the graph of a linear equation in two variables?",
            "Which geometric curve corresponds to the equation \\(ax + by + c = 0\\)?",
            "A linear equation in two variables geometrically represents:",
            "The locus of points satisfying \\(ax + by + c = 0\\) is:",
            "In coordinate geometry, the graph of \\(ax + by + c = 0\\) is always a:",
            "What kind of graph does a degree-1 equation in two variables produce?",
            "The set of all solution pairs \\((x, y)\\) of \\(ax + by + c = 0\\) forms:",
            "Any equation of the form \\(ax + by + c = 0\\) with \\(a^2 + b^2 \\neq 0\\) graphs as:"
        ],
        'calc': lambda item: (
            "A straight line",
            [
                "A parabola",
                "A circle",
                "A hyperbola"
            ],
            "**Step 1: Examine the degree of the equation.**\nIn \\(ax + by + c = 0\\), the maximum power of each variable is 1 (first-degree polynomial equation).\n\n**Step 2: Recall the fundamental theorem of coordinate geometry.**\nEvery first-degree equation in two variables represents a straight line in the coordinate plane.\n\n**Step 3: State the conclusion.**\nThe graph is always **a straight line**."
        ),
        'diff': 'easy'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 13.3.2: Equations of lines parallel to axes (x = k, y = k)
# ==============================================================================
def gen_13_3_2():
    tc = "CBSE-9-MGM-13-13.3.2"
    tname = "Equations of lines parallel to axes (x = k, y = k)"

    # Arch 0: Equations of the coordinate axes themselves
    arch0 = {
        'data': [
            ("x-axis", "y = 0", "Every point on the x-axis has y-coordinate 0"),
            ("y-axis", "x = 0", "Every point on the y-axis has x-coordinate 0"),
            ("horizontal axis", "y = 0", "Equation of the x-axis"),
            ("vertical axis", "x = 0", "Equation of the y-axis"),
            ("line containing all points of form (x, 0)", "y = 0", "Equation of the x-axis"),
            ("line containing all points of form (0, y)", "x = 0", "Equation of the y-axis"),
            ("axis of abscissa", "y = 0", "The x-axis"),
            ("axis of ordinates", "x = 0", "The y-axis"),
            ("line y = 0", "The x-axis", "The x-axis itself"),
            ("line x = 0", "The y-axis", "The y-axis itself")
        ],
        'tmpls': [
            "What is the equation of the {0} in the Cartesian coordinate plane?",
            "The equation representing the {0} is:",
            "Which equation defines the {0}?",
            "What algebraic equation represents the {0}?",
            "The mathematical equation of the {0} is given by:",
            "In two-dimensional coordinate geometry, the equation of the {0} is:",
            "Identify the equation of the {0}:",
            "Write the linear equation representing the {0}:",
            "What is the standard equation of the {0}?",
            "The {0} is represented by the linear equation:"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\)",
            [
                "\\(x = 1\\)" if "y" in item[1] else "\\(y = 1\\)",
                "\\(x + y = 0\\)",
                "\\(xy = 0\\)"
            ],
            f"**Step 1: Consider the coordinates of any point on the {item[0]}.**\n{item[2]}.\n\n**Step 2: Formulate the equation.**\nSince the coordinate is fixed at 0 for all points on the axis, the equation is \\({item[1]}\\).\n\n**Step 3: State the answer.**\n\\({item[1]}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Line parallel to x-axis: y = k
    arch1 = {
        'data': [
            (3, "y = 3", "parallel to the x-axis at a distance of 3 units above it"),
            (-2, "y = -2", "parallel to the x-axis at a distance of 2 units below it"),
            (5, "y = 5", "parallel to the x-axis at a distance of 5 units above it"),
            (-4, "y = -4", "parallel to the x-axis at a distance of 4 units below it"),
            (1, "y = 1", "parallel to the x-axis at a distance of 1 unit above it"),
            (-5, "y = -5", "parallel to the x-axis at a distance of 5 units below it"),
            (7, "y = 7", "parallel to the x-axis at a distance of 7 units above it"),
            (-3, "y = -3", "parallel to the x-axis at a distance of 3 units below it"),
            (4, "y = 4", "parallel to the x-axis at a distance of 4 units above it"),
            (-6, "y = -6", "parallel to the x-axis at a distance of 6 units below it")
        ],
        'tmpls': [
            "The graph of the linear equation \\({1}\\) is a straight line:",
            "Which axis is the line \\({1}\\) parallel to?",
            "Describe the orientation of the line \\({1}\\) in the coordinate plane:",
            "The equation \\({1}\\) represents a line:",
            "In the Cartesian plane, the graph of \\({1}\\) is parallel to:",
            "What is the direction of the line \\({1}\\) relative to the coordinate axes?",
            "The line \\({1}\\) is parallel to which axis?",
            "Graphically, \\({1}\\) is a line:",
            "Which of the following describes the graph of \\({1}\\)?",
            "The equation \\({1}\\) represents a straight line that is:"
        ],
        'calc': lambda item: (
            f"Parallel to the \\(x\\)-axis at a distance of \\({abs(item[0])}\\) units {'above' if item[0] > 0 else 'below'} it",
            [
                f"Parallel to the \\(y\\)-axis at a distance of \\({abs(item[0])}\\) units",
                "Passing through the origin \\((0, 0)\\)",
                "Inclined at \\(45^\\circ\\) to both axes"
            ],
            f"**Step 1: Write down the equation.**\n\\({item[1]}\\) (or \\(0x + 1y = {item[0]}\\)).\n\n**Step 2: Analyze the coordinates.**\nFor every value of \\(x\\), the \\(y\\)-coordinate is fixed at \\({item[0]}\\).\n\n**Step 3: Determine the orientation.**\nThis forms a horizontal line **parallel to the \\(x\\)-axis at a distance of \\({abs(item[0])}\\) units {'above' if item[0] > 0 else 'below'} it**."
        ),
        'diff': 'easy'
    }

    # Arch 2: Line parallel to y-axis: x = k
    arch2 = {
        'data': [
            (3, "x = 3", "parallel to the y-axis at a distance of 3 units to the right"),
            (-2, "x = -2", "parallel to the y-axis at a distance of 2 units to the left"),
            (4, "x = 4", "parallel to the y-axis at a distance of 4 units to the right"),
            (-5, "x = -5", "parallel to the y-axis at a distance of 5 units to the left"),
            (1, "x = 1", "parallel to the y-axis at a distance of 1 unit to the right"),
            (-3, "x = -3", "parallel to the y-axis at a distance of 3 units to the left"),
            (6, "x = 6", "parallel to the y-axis at a distance of 6 units to the right"),
            (-4, "x = -4", "parallel to the y-axis at a distance of 4 units to the left"),
            (5, "x = 5", "parallel to the y-axis at a distance of 5 units to the right"),
            (-1, "x = -1", "parallel to the y-axis at a distance of 1 unit to the left")
        ],
        'tmpls': [
            "The graph of the linear equation \\({1}\\) is a straight line:",
            "Which axis is the line \\({1}\\) parallel to?",
            "Describe the orientation of the line \\({1}\\) in the coordinate plane:",
            "The equation \\({1}\\) represents a line:",
            "In the Cartesian plane, the graph of \\({1}\\) is parallel to:",
            "What is the direction of the line \\({1}\\) relative to the coordinate axes?",
            "The line \\({1}\\) is parallel to which axis?",
            "Graphically, \\({1}\\) is a line:",
            "Which of the following describes the graph of \\({1}\\)?",
            "The equation \\({1}\\) represents a straight line that is:"
        ],
        'calc': lambda item: (
            f"Parallel to the \\(y\\)-axis at a distance of \\({abs(item[0])}\\) units to the {'right' if item[0] > 0 else 'left'}",
            [
                f"Parallel to the \\(x\\)-axis at a distance of \\({abs(item[0])}\\) units",
                "Passing through the origin \\((0, 0)\\)",
                "Perpendicular to the \\(y\\)-axis"
            ],
            f"**Step 1: Write down the equation.**\n\\({item[1]}\\) (or \\(1x + 0y = {item[0]}\\)).\n\n**Step 2: Analyze the coordinates.**\nFor every value of \\(y\\), the \\(x\\)-coordinate remains constant at \\({item[0]}\\).\n\n**Step 3: Determine the orientation.**\nThis forms a vertical line **parallel to the \\(y\\)-axis at a distance of \\({abs(item[0])}\\) units to the {'right' if item[0] > 0 else 'left'}**."
        ),
        'diff': 'easy'
    }

    # Arch 3: Geometric representation of 2x + 9 = 0 (NCERT Ex 4.4 Q2)
    arch3 = {
        'data': [
            ("2x + 9 = 0", -4.5, "x = -4.5", "parallel to y-axis at distance 4.5 units to the left of origin"),
            ("2x - 9 = 0", 4.5, "x = 4.5", "parallel to y-axis at distance 4.5 units to the right of origin"),
            ("y - 3 = 0", 3, "y = 3", "parallel to x-axis at distance 3 units above origin"),
            ("y + 3 = 0", -3, "y = -3", "parallel to x-axis at distance 3 units below origin"),
            ("3x + 6 = 0", -2, "x = -2", "parallel to y-axis at distance 2 units to the left"),
            ("2y - 5 = 0", 2.5, "y = 2.5", "parallel to x-axis at distance 2.5 units above origin"),
            ("4x - 12 = 0", 3, "x = 3", "parallel to y-axis at distance 3 units to the right"),
            ("3y + 9 = 0", -3, "y = -3", "parallel to x-axis at distance 3 units below origin"),
            ("5x + 15 = 0", -3, "x = -3", "parallel to y-axis at distance 3 units to the left"),
            ("2y + 7 = 0", -3.5, "y = -3.5", "parallel to x-axis at distance 3.5 units below origin")
        ],
        'tmpls': [
            "Give the geometric representation of \\({0}\\) as an equation in two variables:",
            "In two variables \\(x\\) and \\(y\\), the geometric representation of \\({0}\\) is:",
            "When \\({0}\\) is represented geometrically in two variables, it is a line:",
            "What is the graph of \\({0}\\) in the two-dimensional Cartesian plane?",
            "Represented in two variables, \\({0}\\) defines a line that is:",
            "The equation \\({0}\\) plotted as a two-variable equation is:",
            "How is \\({0}\\) represented geometrically in two variables?",
            "In two variables, the graph of \\({0}\\) is a straight line:",
            "Identify the two-variable geometric graph of \\({0}\\):",
            "In the \\((x, y)\\) coordinate plane, \\({0}\\) represents a line:"
        ],
        'calc': lambda item: (
            f"Parallel to the {'y' if 'x' in item[0] else 'x'}-axis at a distance of \\({abs(item[1])}\\) units",
            [
                f"Parallel to the {'x' if 'x' in item[0] else 'y'}-axis at a distance of \\({abs(item[1])}\\) units",
                f"A single isolated point \\(({item[1]}, 0)\\)",
                "A line passing through the origin"
            ],
            f"**Step 1: Solve the equation for the single variable.**\n\\({item[0]} \\implies {item[2]}\\).\n\n**Step 2: Express in two variables.**\n\\({('1x + 0y' if 'x' in item[0] else '0x + 1y')} = {item[1]}\\).\n\n**Step 3: State the geometric locus.**\nIn two variables, this represents a line **parallel to the {'y' if 'x' in item[0] else 'x'}-axis at a distance of \\({abs(item[1])}\\) units**."
        ),
        'diff': 'medium'
    }

    # Arch 4: Intersection of x = a and y = b
    arch4 = {
        'data': [
            (2, 3, "(2, 3)", "Lines x = 2 and y = 3 intersect at (2, 3)"),
            (-1, 4, "(-1, 4)", "Lines x = -1 and y = 4 intersect at (-1, 4)"),
            (5, -2, "(5, -2)", "Lines x = 5 and y = -2 intersect at (5, -2)"),
            (-3, -5, "(-3, -5)", "Lines x = -3 and y = -5 intersect at (-3, -5)"),
            (0, 7, "(0, 7)", "Lines x = 0 (y-axis) and y = 7 intersect at (0, 7)"),
            (4, 0, "(4, 0)", "Lines x = 4 and y = 0 (x-axis) intersect at (4, 0)"),
            (1, -1, "(1, -1)", "Lines x = 1 and y = -1 intersect at (1, -1)"),
            (-4, 2, "(-4, 2)", "Lines x = -4 and y = 2 intersect at (-4, 2)"),
            (6, 6, "(6, 6)", "Lines x = 6 and y = 6 intersect at (6, 6)"),
            (-2, -2, "(-2, -2)", "Lines x = -2 and y = -2 intersect at (-2, -2)")
        ],
        'tmpls': [
            "The lines \\(x = {0}\\) and \\(y = {1}\\) intersect at which point in the coordinate plane?",
            "What is the point of intersection of the straight lines \\(x = {0}\\) and \\(y = {1}\\)?",
            "At what point do the lines \\(x = {0}\\) and \\(y = {1}\\) cross each other?",
            "Find the coordinates of the intersection of \\(x = {0}\\) and \\(y = {1}\\):",
            "The common point of the perpendicular lines \\(x = {0}\\) and \\(y = {1}\\) is:",
            "Where do the lines \\(x = {0}\\) and \\(y = {1}\\) meet?",
            "Evaluate the point of intersection of \\(x = {0}\\) and \\(y = {1}\\):",
            "The system of equations \\(x = {0}\\) and \\(y = {1}\\) has the unique solution:",
            "Determine the intersection point of the lines \\(x = {0}\\) and \\(y = {1}\\):",
            "The lines \\(x = {0}\\) and \\(y = {1}\\) meet at the point:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\)",
            [
                f"\\(({item[1]}, {item[0]})\\)",
                f"\\((0, 0)\\)",
                f"\\(({item[0] + 1}, {item[1] + 1})\\)"
            ],
            f"**Step 1: Identify the line properties.**\n- \\(x = {item[0]}\\) is a vertical line where every point has \\(x\\)-coordinate \\({item[0]}\\).\n- \\(y = {item[1]}\\) is a horizontal line where every point has \\(y\\)-coordinate \\({item[1]}\\).\n\n**Step 2: Find the simultaneous solution.**\nThe only point satisfying both equations is \\((x, y) = ({item[0]}, {item[1]})\\).\n\n**Step 3: State the intersection point.**\nThe lines intersect at \\({item[2]}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 5: Distance Between Two Parallel Lines
    arch5 = {
        'data': [
            ("x = 3", "x = -2", 5, "3 - (-2) = 5 units"),
            ("x = 5", "x = 1", 4, "5 - 1 = 4 units"),
            ("y = 4", "y = -3", 7, "4 - (-3) = 7 units"),
            ("y = 6", "y = 2", 4, "6 - 2 = 4 units"),
            ("x = -1", "x = -6", 5, "-1 - (-6) = 5 units"),
            ("y = -2", "y = -8", 6, "-2 - (-8) = 6 units"),
            ("x = 7", "x = -3", 10, "7 - (-3) = 10 units"),
            ("y = 5", "y = -5", 10, "5 - (-5) = 10 units"),
            ("x = 4", "x = -4", 8, "4 - (-4) = 8 units"),
            ("y = 3", "y = -1", 4, "3 - (-1) = 4 units")
        ],
        'tmpls': [
            "What is the distance between the two parallel lines \\({0}\\) and \\({1}\\)?",
            "Find the perpendicular distance between the lines \\({0}\\) and \\({1}\\):",
            "The distance separating the parallel lines \\({0}\\) and \\({1}\\) is:",
            "Calculate the distance between the lines \\({0}\\) and \\({1}\\):",
            "Determine the distance between parallel straight lines \\({0}\\) and \\({1}\\):",
            "How far apart are the two parallel lines \\({0}\\) and \\({1}\\)?",
            "Evaluate the distance between the lines \\({0}\\) and \\({1}\\):",
            "What is the separation between the graphs of \\({0}\\) and \\({1}\\)?",
            "The perpendicular distance between \\({0}\\) and \\({1}\\) is equal to:",
            "Find the distance between the parallel lines \\({0}\\) and \\({1}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ units}}\\)",
            [
                f"\\({item[2] + 2}\\text{{ units}}\\)",
                f"\\({item[2] - 2}\\text{{ units}}\\)",
                f"\\({item[2] * 2}\\text{{ units}}\\)"
            ],
            f"**Step 1: Identify the common coordinate direction.**\nBoth lines are perpendicular to the same axis (both are {'vertical' if 'x' in item[0] else 'horizontal'}).\n\n**Step 2: Calculate the difference between their intercepts.**\nDistance \\(= |k_1 - k_2|\\).\n\n**Step 3: State the distance.**\nDistance \\(= {item[3]}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 6: Points Satisfying x = k or y = k
    arch6 = {
        'data': [
            ("x = 3", "(3, 5)", "(5, 3)", "Every point on x = 3 has x-coordinate 3"),
            ("x = -2", "(-2, 7)", "(7, -2)", "Every point on x = -2 has x-coordinate -2"),
            ("y = 4", "(1, 4)", "(4, 1)", "Every point on y = 4 has y-coordinate 4"),
            ("y = -3", "(6, -3)", "(-3, 6)", "Every point on y = -3 has y-coordinate -3"),
            ("x = 0", "(0, 8)", "(8, 0)", "Points on y-axis have x = 0"),
            ("y = 0", "(5, 0)", "(0, 5)", "Points on x-axis have y = 0"),
            ("x = 5", "(5, -1)", "(-1, 5)", "Every point on x = 5 has x-coordinate 5"),
            ("y = -2", "(-4, -2)", "(-2, -4)", "Every point on y = -2 has y-coordinate -2"),
            ("x = -4", "(-4, 0)", "(0, -4)", "Every point on x = -4 has x-coordinate -4"),
            ("y = 6", "(0, 6)", "(6, 0)", "Every point on y = 6 has y-coordinate 6")
        ],
        'tmpls': [
            "Which of the following points lies on the line \\({0}\\)?",
            "The line \\({0}\\) contains which of the following points?",
            "Which ordered pair satisfies the equation \\({0}\\)?",
            "Identify the point that lies on the graph of \\({0}\\):",
            "Which of these coordinates belongs to the line \\({0}\\)?",
            "Determine which point lies on \\({0}\\):",
            "Which point is situated on the line \\({0}\\)?",
            "Select the point that lies on the straight line \\({0}\\):",
            "Which coordinate pair is on the line \\({0}\\)?",
            "The graph of \\({0}\\) passes through the point:"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\)",
            [
                f"\\({item[2]}\\)",
                "\\((1, 1)\\)",
                "\\((0, 0)\\)" if "0" not in item[0] else "\\((1, 2)\\)"
            ],
            f"**Step 1: Recall the definition of the line \\({item[0]}\\).**\n{item[3]}.\n\n**Step 2: Check the options.**\nOnly \\({item[1]}\\) has the required coordinate.\n\n**Step 3: State the answer.**\nThe point is \\({item[1]}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 7: Angle of Intersection Between x = a and y = b
    arch7 = {
        'data': [
            ("x = 2 and y = 3", 90, "One is vertical (parallel to y-axis), one is horizontal (parallel to x-axis)"),
            ("x = -1 and y = 4", 90, "Horizontal and vertical lines are mutually perpendicular"),
            ("x = 5 and y = -2", 90, "Perpendicular lines form an angle of 90°"),
            ("x-axis and y-axis", 90, "Coordinate axes are perpendicular to each other"),
            ("x = k and y = c", 90, "Any vertical line and horizontal line meet at 90°"),
            ("2x = 6 and 3y = 12", 90, "Lines are x = 3 and y = 4, which meet at 90°"),
            ("x = 0 and y = 5", 90, "y-axis and horizontal line y = 5 meet at 90°"),
            ("y = 0 and x = -3", 90, "x-axis and vertical line x = -3 meet at 90°"),
            ("x = a and y = b", 90, "General vertical and horizontal lines meet at 90°"),
            ("x = -4 and y = -4", 90, "Meet at 90°")
        ],
        'tmpls': [
            "At what angle do the lines \\({0}\\) intersect each other?",
            "The angle between the straight lines \\({0}\\) is:",
            "What is the measure of the angle between \\({0}\\)?",
            "Find the angle of intersection of the lines \\({0}\\):",
            "The lines \\({0}\\) are mutually:",
            "Calculate the angle formed by the intersection of \\({0}\\):",
            "What is the angle between the graphs of \\({0}\\)?",
            "Evaluate the measure of the angle between lines \\({0}\\):",
            "The lines \\({0}\\) intersect at an angle of:",
            "Determine the angle of intersection between \\({0}\\):"
        ],
        'calc': lambda item: (
            "\\(90^\\circ\\) (they are mutually perpendicular)",
            [
                "\\(0^\\circ\\) (they are parallel)",
                "\\(45^\\circ\\)",
                "\\(180^\\circ\\)"
            ],
            f"**Step 1: Identify the nature of both lines.**\n- The line of the form \\(x = a\\) is parallel to the \\(y\\)-axis (vertical).\n- The line of the form \\(y = b\\) is parallel to the \\(x\\)-axis (horizontal).\n\n**Step 2: State the angle between horizontal and vertical lines.**\nHorizontal and vertical lines in the Cartesian plane are perpendicular to each other.\n\n**Step 3: State the angle.**\nThe angle of intersection is **\\(90^\\circ\\)**."
        ),
        'diff': 'easy'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_13_3_1()
    q2 = gen_13_3_2()
    print(f"gen_13_3_1: {len(q1)} questions")
    print(f"gen_13_3_2: {len(q2)} questions")
