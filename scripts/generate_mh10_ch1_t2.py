# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 1: Linear Equations in Two Variables (Topics 1.2, 1.3, 1.4, 1.5)
Each topic gets exactly 82 canonical questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# ==============================================================================
# TOPIC 1.2: Graphical Method of Solving Linear Equations (MH-10-MTH1-1-1.2)
# ==============================================================================
t12_exam = [
    # 1
    ("Which of the following represents the graph of a linear equation in two variables?",
     ["A straight line", "A parabola", "A circle", "A hyperbola"],
     "A", "OSC", "easy",
     "The graph of every linear equation in two variables \\(ax + by + c = 0\\) is always a straight line in the coordinate plane."),

    # 2
    ("How many points are practically recommended to be plotted when drawing the graph of a linear equation in two variables to ensure correctness?",
     ["At least 4 ordered pairs (three or four points)", "Exactly 1 point", "At least 10 points", "At least 100 points"],
     "A", "OSC", "easy",
     "Although theoretically two points determine a unique line, finding and plotting at least 3 or 4 points is recommended so that if any point is calculated incorrectly, the points will not be collinear, immediately alerting the student to the mistake."),

    # 3
    ("What are the coordinates of the point where the line \\(2x + 3y = 6\\) intersects the X-axis?",
     ["\\((3, 0)\\)", "\\((0, 2)\\)", "\\((2, 0)\\)", "\\((0, 3)\\)"],
     "A", "OSC", "easy",
     "On the X-axis, the Y-coordinate is 0. Substituting \\(y = 0\\) into \\(2x + 3(0) = 6 \\implies 2x = 6 \\implies x = 3\\). Thus, the X-intercept is \\((3, 0)\\)."),

    # 4
    ("What are the coordinates of the point where the line \\(2x + 3y = 6\\) intersects the Y-axis?",
     ["\\((0, 2)\\)", "\\((3, 0)\\)", "\\((0, 3)\\)", "\\((2, 0)\\)"],
     "A", "OSC", "easy",
     "On the Y-axis, the X-coordinate is 0. Substituting \\(x = 0\\) into \\(2(0) + 3y = 6 \\implies 3y = 6 \\implies y = 2\\). Thus, the Y-intercept is \\((0, 2)\\)."),

    # 5
    ("What is the graphical solution of the simultaneous equations \\(x + y = 4\\) and \\(2x - y = 2\\)?",
     ["\\((2, 2)\\)", "\\((3, 1)\\)", "\\((1, 3)\\)", "\\((4, 0)\\)"],
     "A", "OSC", "easy",
     "Solving simultaneously: Adding the equations gives \\(3x = 6 \\implies x = 2\\). Then \\(y = 4 - 2 = 2\\). The point of intersection on the Cartesian coordinate graph is \\((2, 2)\\)."),

    # 6
    ("What is the nature of the line represented by the equation \\(y = 4\\)?",
     ["A straight line parallel to the X-axis at a distance of 4 units above the origin",
      "A straight line parallel to the Y-axis at a distance of 4 units to the right",
      "A straight line passing through the origin",
      "A line perpendicular to the Y-axis at \\(x = 4\\)"],
     "A", "OSC", "easy",
     "The equation \\(y = 4\\) has constant ordinate 4 for all values of \\(x\\). It represents a straight line parallel to the X-axis at distance 4 units in the positive Y direction."),

    # 7
    ("What is the nature of the line represented by the equation \\(x = -3\\)?",
     ["A straight line parallel to the Y-axis at a distance of 3 units to the left of the origin",
      "A straight line parallel to the X-axis at a distance of 3 units below the origin",
      "A straight line passing through origin",
      "A point at \\((-3, 0)\\)"],
     "A", "OSC", "easy",
     "The equation \\(x = -3\\) has constant abscissa \\(-3\\) for all values of \\(y\\). It is a vertical straight line parallel to the Y-axis at distance 3 units to the left."),

    # 8
    ("What is the equation of the X-axis?",
     ["\\(y = 0\\)", "\\(x = 0\\)", "\\(x + y = 0\\)", "\\(x - y = 0\\)"],
     "A", "OSC", "easy",
     "Every point on the X-axis has a Y-coordinate of 0. Hence, the equation of the X-axis is \\(y = 0\\)."),

    # 9
    ("What is the equation of the Y-axis?",
     ["\\(x = 0\\)", "\\(y = 0\\)", "\\(x = y\\)", "\\(x = 1\\)"],
     "A", "OSC", "easy",
     "Every point on the Y-axis has an X-coordinate of 0. Hence, the equation of the Y-axis is \\(x = 0\\)."),

    # 10
    ("If the graph of \\(kx - 3y = 12\\) passes through the point \\((3, -2)\\), find the value of \\(k\\).",
     ["2", "3", "4", "-2"],
     "A", "OSC", "medium",
     "Substitute \\(x = 3, y = -2\\): \\(k(3) - 3(-2) = 12 \\implies 3k + 6 = 12 \\implies 3k = 6 \\implies k = 2\\)."),

    # 11
    ("Find the coordinates of the point of intersection of \\(x + y = 0\\) and \\(2x - y = 9\\).",
     ["\\((3, -3)\\)", "\\((-3, 3)\\)", "\\((3, 3)\\)", "\\((0, 0)\\)"],
     "A", "OSC", "medium",
     "From \\(x + y = 0\\), \\(y = -x\\). Substitute into second: \\(2x - (-x) = 9 \\implies 3x = 9 \\implies x = 3\\). Then \\(y = -3\\). The intersection point is \\((3, -3)\\)."),

    # 12
    ("What is the area of the triangle formed by the line \\(x + y = 6\\), the X-axis, and the Y-axis?",
     ["18 sq units", "36 sq units", "12 sq units", "24 sq units"],
     "A", "OSC", "medium",
     "The line intersects the X-axis at \\((6, 0)\\) (base = 6) and the Y-axis at \\((0, 6)\\) (height = 6). The area of the right-angled triangle is \\(\\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 6 \\times 6 = 18\\) square units."),

    # 13
    ("What is the area of the triangle formed by the lines \\(y = x\\), \\(y = -x\\), and \\(y = 4\\)?",
     ["16 sq units", "8 sq units", "32 sq units", "4 sq units"],
     "A", "OSC", "hard",
     "The line \\(y = 4\\) intersects \\(y = x\\) at \\((4, 4)\\) and \\(y = -x\\) at \\((-4, 4)\\). The length of the horizontal base is \\(4 - (-4) = 8\\). The height from the origin \\((0, 0)\\) to \\(y = 4\\) is 4. Area = \\(\\frac{1}{2} \\times 8 \\times 4 = 16\\) sq units."),

    # 14
    ("If the lines \\(3x + 2ky = 2\\) and \\(2x + 5y + 1 = 0\\) are parallel, what is the value of \\(k\\)?",
     ["\\(\\frac{15}{4}\\)", "\\(\\frac{4}{15}\\)", "\\(-\\frac{15}{4}\\)", "5"],
     "A", "OSC", "medium",
     "For parallel lines, \\(\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\implies \\frac{3}{2} = \\frac{2k}{5} \\implies 4k = 15 \\implies k = \\frac{15}{4}\\)."),

    # 15
    ("Complete the ordered pair for the equation \\(x - y = 1\\): if \\(x = 3\\), then \\(y = \\text{?}\\)",
     ["2", "4", "-2", "1"],
     "A", "OSC", "easy",
     "\\(3 - y = 1 \\implies y = 3 - 1 = 2\\). Ordered pair is \\((3, 2)\\)."),

    # 16
    ("Complete the ordered pair for \\(x - y = 1\\): if \\(y = 0\\), then \\(x = \\text{?}\\)",
     ["1", "-1", "0", "2"],
     "A", "OSC", "easy",
     "\\(x - 0 = 1 \\implies x = 1\\). Ordered pair is \\((1, 0)\\)."),

    # 17
    ("Which of the following points lies in Quadrant II?",
     ["\\((-3, 4)\\)", "\\((3, 4)\\)", "\\((-3, -4)\\)", "\\((3, -4)\\)"],
     "A", "OSC", "easy",
     "In Quadrant II, the X-coordinate is negative and the Y-coordinate is positive. Thus \\((-3, 4)\\) lies in Quadrant II."),

    # 18
    ("Which of the following points lies on the Y-axis?",
     ["\\((0, -5)\\)", "\\((-5, 0)\\)", "\\((5, 5)\\)", "\\((-5, -5)\\)"],
     "A", "OSC", "easy",
     "A point lies on the Y-axis if its X-coordinate is 0. Thus \\((0, -5)\\) lies on the Y-axis."),

    # 19
    ("Solve graphically: \\(x + y = 0\\) and \\(2x - y = 9\\). What are the coordinates of intersection?",
     ["\\((3, -3)\\)", "\\((2, -2)\\)", "\\((-3, 3)\\)", "\\((4, -4)\\)"],
     "A", "OSC", "easy",
     "From \\(x + y = 0\\), \\(y = -x\\). Substituting into \\(2x - (-x) = 9 \\implies 3x = 9 \\implies x = 3, y = -3\\)."),

    # 20
    ("If two lines intersect at \\((2, -1)\\), then \\((2, -1)\\) is:",
     ["The unique common solution satisfying both linear equations",
      "The Y-intercept of both lines",
      "The X-intercept of both lines",
      "An extraneous root that must be discarded"],
     "A", "OSC", "easy",
     "The point of intersection of two lines represents the exact pair of values \\((x, y)\\) that simultaneously satisfies both equations."),

    # 21
    ("Find the point of intersection of \\(3x - y = 2\\) and \\(2x - y = 3\\).",
     ["\\((-1, -5)\\)", "\\((1, 1)\\)", "\\((5, 13)\\)", "\\((-1, 5)\\)"],
     "A", "OSC", "medium",
     "Subtract equation 2 from equation 1: \\((3x - y) - (2x - y) = 2 - 3 \\implies x = -1\\). Then \\(2(-1) - y = 3 \\implies -2 - y = 3 \\implies y = -5\\). Solution is \\((-1, -5)\\)."),

    # 22
    ("At what point do the lines \\(x = 4\\) and \\(y = -3\\) intersect?",
     ["\\((4, -3)\\)", "\\((-3, 4)\\)", "\\((0, 0)\\)", "\\((4, 0)\\)"],
     "A", "OSC", "easy",
     "The vertical line \\(x = 4\\) and horizontal line \\(y = -3\\) intersect at the point \\((4, -3)\\)."),

    # 23
    ("What is the slope (gradient) of a line parallel to the X-axis?",
     ["0", "1", "Undefined (infinite)", "-1"],
     "A", "OSC", "easy",
     "A horizontal line has zero vertical rise for any horizontal run. Hence, its slope is 0."),

    # 24
    ("What is the slope of a line parallel to the Y-axis?",
     ["Undefined (not defined)", "0", "1", "-1"],
     "A", "OSC", "easy",
     "A vertical line has zero run (\\(\\Delta x = 0\\)), causing division by zero in \\(m = \\frac{\\Delta y}{\\Delta x}\\). Hence its slope is undefined."),

    # 25
    ("Solve graphically: \\(3x - 4y = -7\\) and \\(5x - 2y = 0\\). The lines intersect at:",
     ["\\((1, 2.5)\\)", "\\((2, 5)\\)", "\\((0, 0)\\)", "\\((-1, 1)\\)"],
     "A", "OSC", "medium",
     "From \\(5x - 2y = 0\\), \\(y = 2.5x\\). Substitute into \\(3x - 4(2.5x) = -7 \\implies -7x = -7 \\implies x = 1\\). Then \\(y = 2.5\\). Intersection point is \\((1, 2.5)\\)."),

    # 26
    ("What is the distance of the point \\((3, 4)\\) from the origin \\((0, 0)\\)?",
     ["5 units", "7 units", "\\(\\sqrt{7}\\) units", "25 units"],
     "A", "OSC", "easy",
     "Using the distance formula: \\(d = \\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5\\) units."),

    # 27
    ("What is the distance of the point \\((-6, 8)\\) from the X-axis?",
     ["8 units", "6 units", "10 units", "-6 units"],
     "A", "OSC", "easy",
     "The distance of any point \\((x, y)\\) from the X-axis is given by \\(|y|\\). Here \\(|8| = 8\\) units."),

    # 28
    ("What is the distance of the point \\((-6, 8)\\) from the Y-axis?",
     ["6 units", "-6 units", "8 units", "14 units"],
     "A", "OSC", "easy",
     "The distance of any point \\((x, y)\\) from the Y-axis is given by \\(|x|\\). Here \\(|-6| = 6\\) units."),

    # 29
    ("Do the points \\((1, 2)\\), \\((2, 4)\\), and \\((3, 6)\\) lie on the same straight line?",
     ["Yes, they are collinear and all satisfy the equation \\(y = 2x\\)",
      "No, they form a right triangle",
      "No, they form an equilateral triangle",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "For all three points, \\(\\frac{y}{x} = 2\\), which satisfies \\(y = 2x\\). Since they satisfy the same linear equation, they are collinear."),

    # 30
    ("If the graph of \\(2x + 3y = k\\) passes through \\((1, 1)\\), find \\(k\\).",
     ["5", "1", "6", "-1"],
     "A", "OSC", "easy",
     "\\(2(1) + 3(1) = 2 + 3 = 5 = k\\)."),

    # 31
    ("Find the intersection of \\(x + y = 5\\) and \\(x - y = 3\\).",
     ["\\((4, 1)\\)", "\\((1, 4)\\)", "\\((3, 2)\\)", "\\((5, 0)\\)"],
     "A", "OSC", "easy",
     "Adding: \\(2x = 8 \\implies x = 4\\). Subtracting: \\(2y = 2 \\implies y = 1\\)."),

    # 32
    ("Solve graphically: \\(2x - 3y = 4\\) and \\(3y - x = 4\\). Find the intersection point.",
     ["\\((8, 4)\\)", "\\((4, 8)\\)", "\\((2, 2)\\)", "\\((6, 3)\\)"],
     "A", "OSC", "medium",
     "Rewrite second equation: \\(-x + 3y = 4\\). Adding to \\(2x - 3y = 4\\) gives \\(x = 8\\). Then \\(3y = x + 4 = 8 + 4 = 12 \\implies y = 4\\). Point is \\((8, 4)\\)."),

    # 33
    ("At what point does the line \\(3x + 4y = 12\\) intersect the line \\(x = 0\\)?",
     ["\\((0, 3)\\)", "\\((4, 0)\\)", "\\((0, 4)\\)", "\\((3, 0)\\)"],
     "A", "OSC", "easy",
     "\\(x = 0\\) is the Y-axis. Substituting \\(x = 0\\) gives \\(4y = 12 \\implies y = 3\\). Point is \\((0, 3)\\)."),

    # 34
    ("At what point does the line \\(3x + 4y = 12\\) intersect the line \\(y = 0\\)?",
     ["\\((4, 0)\\)", "\\((0, 3)\\)", "\\((3, 0)\\)", "\\((0, 4)\\)"],
     "A", "OSC", "easy",
     "\\(y = 0\\) is the X-axis. Substituting \\(y = 0\\) gives \\(3x = 12 \\implies x = 4\\). Point is \\((4, 0)\\)."),

    # 35
    ("What is the perimeter of the triangle formed by the axes and the line \\(3x + 4y = 12\\)?",
     ["12 units", "7 units", "14 units", "10 units"],
     "A", "OSC", "medium",
     "The vertices are \\((0, 0)\\), \\((4, 0)\\), and \\((0, 3)\\). The sides are 4 (along X-axis), 3 (along Y-axis), and hypotenuse \\(\\sqrt{3^2 + 4^2} = 5\\). Perimeter = \\(3 + 4 + 5 = 12\\) units."),

    # 36
    ("Which of the following lines passes through the origin \\((0, 0)\\)?",
     ["\\(y = 3x\\)", "\\(y = 3x + 1\\)", "\\(x + y = 2\\)", "\\(2x - 3y = 5\\)"],
     "A", "OSC", "easy",
     "A line passes through the origin if its constant term is 0. Substituting \\((0, 0)\\) into \\(y = 3x\\) gives \\(0 = 0\\), which is true."),

    # 37
    ("What is the angle made by the line \\(y = x\\) with the positive direction of the X-axis?",
     ["\\(45^\\circ\\)", "\\(30^\\circ\\)", "\\(60^\\circ\\)", "\\(90^\\circ\\)"],
     "A", "OSC", "easy",
     "The slope of \\(y = x\\) is \\(m = 1\\). Since \\(\\tan \\theta = m = 1\\), the inclination \\(\\theta = 45^\\circ\\)."),

    # 38
    ("Find the midpoint of the line segment joining \\((2, 4)\\) and \\((6, 8)\\).",
     ["\\((4, 6)\\)", "\\((8, 12)\\)", "\\((3, 5)\\)", "\\((4, 4)\\)"],
     "A", "OSC", "easy",
     "Midpoint formula: \\(M = \\left(\\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2}\\right) = \\left(\\frac{2+6}{2}, \\frac{4+8}{2}\\right) = (4, 6)\\)."),

    # 39
    ("If a system of linear equations is solved graphically and the two lines turn out to be parallel, what does this indicate about the system?",
     ["The system has no common solution (inconsistent)",
      "The system has infinitely many solutions",
      "The system has a unique solution at infinity",
      "The equations were graphed incorrectly"],
     "A", "OSC", "easy",
     "Parallel lines have equal slopes and different intercepts, meaning they never intersect. Hence, there is no common pair \\((x, y)\\) and the system has no solution."),

    # 40
    ("If two lines intersect at a right angle (perpendicular), what is the relation between their slopes \\(m_1\\) and \\(m_2\\)?",
     ["\\(m_1 \\times m_2 = -1\\)", "\\(m_1 = m_2\\)", "\\(m_1 + m_2 = 0\\)", "\\(m_1 - m_2 = 1\\)"],
     "A", "OSC", "easy",
     "Two non-vertical lines are perpendicular if and only if the product of their slopes is \\(-1\\), i.e., \\(m_1 m_2 = -1\\).")
]

# 30 Practice (41-70)
t12_prac = [
    # 41
    ("Find the solution of \\(x + y = 3\\) and \\(x - y = 1\\) by graph.",
     ["\\((2, 1)\\)", "\\((1, 2)\\)", "\\((3, 0)\\)", "\\((0, 3)\\)"],
     "A", "OSC", "easy",
     "Adding equations: \\(2x = 4 \\implies x = 2\\). Subtracting: \\(2y = 2 \\implies y = 1\\). The lines intersect at \\((2, 1)\\)."),

    # 42
    ("Complete the table for \\(x + y = 5\\): when \\(x = 2\\), \\(y = \\text{?}\\)",
     ["3", "2", "4", "5"],
     "A", "OSC", "easy",
     "\\(2 + y = 5 \\implies y = 3\\)."),

    # 43
    ("Complete the table for \\(x + y = 5\\): when \\(y = 5\\), \\(x = \\text{?}\\)",
     ["0", "5", "1", "-5"],
     "A", "OSC", "easy",
     "\\(x + 5 = 5 \\implies x = 0\\)."),

    # 44
    ("Complete the table for \\(x + y = 5\\): when \\(x = -1\\), \\(y = \\text{?}\\)",
     ["6", "4", "5", "-6"],
     "A", "OSC", "easy",
     "\\(-1 + y = 5 \\implies y = 6\\)."),

    # 45
    ("For \\(x - y = 3\\), if \\(x = 0\\), find \\(y\\).",
     ["-3", "3", "0", "1"],
     "A", "OSC", "easy",
     "\\(0 - y = 3 \\implies y = -3\\)."),

    # 46
    ("For \\(x - y = 3\\), if \\(y = 0\\), find \\(x\\).",
     ["3", "-3", "0", "1"],
     "A", "OSC", "easy",
     "\\(x - 0 = 3 \\implies x = 3\\)."),

    # 47
    ("For \\(x - y = 3\\), if \\(x = 5\\), find \\(y\\).",
     ["2", "3", "8", "-2"],
     "A", "OSC", "easy",
     "\\(5 - y = 3 \\implies y = 2\\)."),

    # 48
    ("Find the intersection of \\(x + y = 5\\) and \\(x - y = 3\\).",
     ["\\((4, 1)\\)", "\\((1, 4)\\)", "\\((3, 2)\\)", "\\((2, 3)\\)"],
     "A", "OSC", "easy",
     "Adding gives \\(2x = 8 \\implies x = 4\\); \\(y = 5 - 4 = 1\\)."),

    # 49
    ("Solve graphically: \\(x + y = 6\\) and \\(x - y = 4\\). What is \\(x\\)?",
     ["5", "1", "6", "4"],
     "A", "OSC", "easy",
     "\\(2x = 10 \\implies x = 5\\)."),

    # 50
    ("From the previous question, what is \\(y\\)?",
     ["1", "5", "2", "0"],
     "A", "OSC", "easy",
     "\\(y = 6 - 5 = 1\\)."),

    # 51
    ("Find the coordinates where \\(y = 2x - 4\\) cuts the X-axis.",
     ["\\((2, 0)\\)", "\\((0, -4)\\)", "\\((-2, 0)\\)", "\\((0, 4)\\)"],
     "A", "OSC", "easy",
     "Set \\(y = 0\\): \\(2x - 4 = 0 \\implies 2x = 4 \\implies x = 2\\)."),

    # 52
    ("Find the coordinates where \\(y = 2x - 4\\) cuts the Y-axis.",
     ["\\((0, -4)\\)", "\\((2, 0)\\)", "\\((0, 4)\\)", "\\((-4, 0)\\)"],
     "A", "OSC", "easy",
     "Set \\(x = 0\\): \\(y = 2(0) - 4 = -4\\)."),

    # 53
    ("Solve graphically: \\(2x - y = 2\\) and \\(4x - y = 4\\). The intersection point is:",
     ["\\((1, 0)\\)", "\\((0, -2)\\)", "\\((2, 2)\\)", "\\((0, 0)\\)"],
     "A", "OSC", "medium",
     "Subtracting equation 1 from equation 2: \\(2x = 2 \\implies x = 1\\). Then \\(y = 2(1) - 2 = 0\\). Solution is \\((1, 0)\\)."),

    # 54
    ("What type of line is represented by \\(2x = 8\\)?",
     ["A vertical line parallel to the Y-axis passing through \\((4, 0)\\)",
      "A horizontal line parallel to the X-axis",
      "A line passing through the origin",
      "A line with slope 2"],
     "A", "OSC", "easy",
     "\\(2x = 8 \\implies x = 4\\), which is a vertical straight line parallel to the Y-axis."),

    # 55
    ("What type of line is represented by \\(3y + 9 = 0\\)?",
     ["A horizontal line parallel to the X-axis passing through \\((0, -3)\\)",
      "A vertical line parallel to the Y-axis",
      "A line inclined at 45 degrees",
      "A circle of radius 3"],
     "A", "OSC", "easy",
     "\\(3y = -9 \\implies y = -3\\), which is a horizontal straight line parallel to the X-axis at \\(y = -3\\)."),

    # 56
    ("What is the area of the region bounded by \\(x = 0\\), \\(y = 0\\), and \\(x + y = 4\\)?",
     ["8 sq units", "16 sq units", "4 sq units", "12 sq units"],
     "A", "OSC", "medium",
     "Right-angled triangle with legs of length 4 along the axes. Area = \\(\\frac{1}{2} \\times 4 \\times 4 = 8\\) sq units."),

    # 57
    ("Solve graphically: \\(3x - y = 2\\) and \\(2x - y = 3\\). The lines intersect in which quadrant?",
     ["Quadrant III", "Quadrant I", "Quadrant II", "Quadrant IV"],
     "A", "OSC", "medium",
     "Solving gives \\(x = -1, y = -5\\). Both coordinates are negative, so the point lies in Quadrant III."),

    # 58
    ("In which quadrant does the point \\((4, -3)\\) lie?",
     ["Quadrant IV", "Quadrant I", "Quadrant II", "Quadrant III"],
     "A", "OSC", "easy",
     "Positive X and negative Y defines Quadrant IV."),

    # 59
    ("In which quadrant does the point \\((-5, -2)\\) lie?",
     ["Quadrant III", "Quadrant I", "Quadrant II", "Quadrant IV"],
     "A", "OSC", "easy",
     "Negative X and negative Y defines Quadrant III."),

    # 60
    ("Find the solution of \\(x - 2y = 4\\) and \\(2x - 4y = 8\\).",
     ["Infinitely many solutions (coincident lines)", "Unique solution", "No solution", "Cannot be solved"],
     "A", "OSC", "easy",
     "The second equation is simply twice the first equation. Both represent identical lines, so there are infinitely many solutions."),

    # 61
    ("Find the solution of \\(x - 2y = 4\\) and \\(2x - 4y = 12\\).",
     ["No solution (parallel lines)", "Unique solution", "Infinitely many solutions", "One root only"],
     "A", "OSC", "easy",
     "Here \\(\\frac{1}{2} = \\frac{-2}{-4} \\neq \\frac{4}{12}\\). The lines are parallel and do not intersect, giving no solution."),

    # 62
    ("Which of the following points satisfies the inequality \\(x + y < 5\\)?",
     ["\\((1, 2)\\)", "\\((3, 3)\\)", "\\((4, 2)\\)", "\\((5, 1)\\)"],
     "A", "OSC", "easy",
     "For \\((1, 2)\\), \\(1 + 2 = 3 < 5\\), which is true."),

    # 63
    ("Solve graphically: \\(x + y = 10\\) and \\(x - y = 2\\). What is \\((x, y)\\)?",
     ["\\((6, 4)\\)", "\\((4, 6)\\)", "\\((7, 3)\\)", "\\((5, 5)\\)"],
     "A", "OSC", "easy",
     "\\(2x = 12 \\implies x = 6\\), and \\(y = 10 - 6 = 4\\)."),

    # 64
    ("The line \\(y = mx + c\\) has slope \\(m\\) and Y-intercept \\(c\\). For \\(2x + y = 7\\), what are \\(m\\) and \\(c\\)?",
     ["\\(m = -2, c = 7\\)", "\\(m = 2, c = 7\\)", "\\(m = -2, c = -7\\)", "\\(m = 2, c = -7\\)"],
     "A", "OSC", "easy",
     "Rewriting: \\(y = -2x + 7\\). Thus slope \\(m = -2\\) and Y-intercept \\(c = 7\\)."),

    # 65
    ("What is the Y-intercept of \\(3x - 5y = 15\\)?",
     ["-3", "3", "5", "-5"],
     "A", "OSC", "easy",
     "Set \\(x = 0\\): \\(-5y = 15 \\implies y = -3\\)."),

    # 66
    ("What is the X-intercept of \\(3x - 5y = 15\\)?",
     ["5", "-5", "3", "-3"],
     "A", "OSC", "easy",
     "Set \\(y = 0\\): \\(3x = 15 \\implies x = 5\\)."),

    # 67
    ("Solve: \\(2x + y = 6\\) and \\(2x - y = 2\\). What is \\(x\\)?",
     ["2", "3", "1", "4"],
     "A", "OSC", "easy",
     "Adding gives \\(4x = 8 \\implies x = 2\\)."),

    # 68
    ("From the previous question, what is \\(y\\)?",
     ["2", "1", "3", "0"],
     "A", "OSC", "easy",
     "\\(y = 6 - 2(2) = 2\\)."),

    # 69
    ("Do the lines \\(x + y = 2\\), \\(2x + 2y = 4\\), and \\(3x + 3y = 6\\) represent different lines?",
     ["No, all three equations represent the exact same straight line",
      "Yes, they form a triangle",
      "Yes, they are three distinct parallel lines",
      "No, they intersect at three points"],
     "A", "OSC", "easy",
     "Dividing equation 2 by 2 gives \\(x + y = 2\\). Dividing equation 3 by 3 also gives \\(x + y = 2\\). All three are coincident."),

    # 70
    ("What are the coordinates of the origin?",
     ["\\((0, 0)\\)", "\\((1, 1)\\)", "\\((0, 1)\\)", "\\((1, 0)\\)"],
     "A", "OSC", "easy",
     "The origin is the intersection of the X-axis and Y-axis, where both coordinates are 0: \\((0, 0)\\).")
]

# 12 Mock/Foundation (71-82)
t12_mock = [
    # 71
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="200" viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="200" fill="#0f172a" rx="8"/>
  <!-- Axes -->
  <line x1="30" y1="100" x2="310" y2="100" stroke="#64748b" stroke-width="1.5"/>
  <line x1="170" y1="20" x2="170" y2="180" stroke="#64748b" stroke-width="1.5"/>
  <text x="305" y="95" fill="#94a3b8" font-size="10">X</text>
  <text x="175" y="30" fill="#94a3b8" font-size="10">Y</text>
  <!-- Line 1: x + y = 4 (passes through (0, 140) and (140, 0) relative) -->
  <line x1="70" y1="40" x2="270" y2="160" stroke="#38bdf8" stroke-width="2"/>
  <text x="275" y="165" fill="#38bdf8" font-size="9">L1: x + y = 4</text>
  <!-- Line 2: 2x - y = 2 -->
  <line x1="110" y1="170" x2="230" y2="30" stroke="#4ade80" stroke-width="2"/>
  <text x="235" y="35" fill="#4ade80" font-size="9">L2: 2x - y = 2</text>
  <!-- Intersection point (2, 2) -->
  <circle cx="190" cy="80" r="4" fill="#facc15"/>
  <text x="200" y="80" fill="#facc15" font-size="10" font-weight="bold">(2, 2)</text>
</svg>
</div>
In the graphical representation above, what does the intersection point \\((2, 2)\\) signify?""",
     ["It is the unique common solution that satisfies both linear equations simultaneously",
      "It is the midpoint of line L1",
      "It represents an imaginary root",
      "It represents the area between the lines"],
     "A", "OSC", "easy",
     "The coordinates of the point where two lines intersect on a graph satisfy both equations at the same time, representing the unique solution to the simultaneous system."),

    # 72
    ("If the graph of a pair of equations consists of coincident lines, the system has:",
     ["Infinitely many solutions", "No solution", "Exactly one solution", "Two solutions"],
     "A", "OSC", "easy",
     "Coincident lines share all points along their length, meaning every point on the line is a solution, yielding infinitely many solutions."),

    # 73
    ("If the graph of a pair of equations consists of parallel lines, the system has:",
     ["No solution", "A unique solution", "Infinitely many solutions", "Four solutions"],
     "A", "OSC", "easy",
     "Parallel lines have no point of intersection. Therefore, there are no coordinates satisfying both equations simultaneously."),

    # 74
    ("What is the minimum number of points required to determine a straight line?",
     ["2 points", "1 point", "3 points", "4 points"],
     "A", "OSC", "easy",
     "According to Euclidean geometry, exactly one straight line passes through any two distinct points."),

    # 75
    ("Why is finding three or four points advised when plotting lines in school algebra?",
     ["To check collinearity and detect any arithmetic errors in calculation",
      "Because two points cannot define a line",
      "Because the line curves after two points",
      "To find the parabola"],
     "A", "OSC", "easy",
     "If three or more calculated points do not lie on a single straight line, it is immediately clear that a calculation error occurred."),

    # 76
    ("Find the solution of \\(x + y = 7\\) and \\(x - y = 1\\).",
     ["\\((4, 3)\\)", "\\((3, 4)\\)", "\\((5, 2)\\)", "\\((2, 5)\\)"],
     "A", "OSC", "easy",
     "Adding gives \\(2x = 8 \\implies x = 4\\). Then \\(y = 7 - 4 = 3\\)."),

    # 77
    ("What are the coordinates of the Y-intercept for \\(y = 3x - 9\\)?",
     ["\\((0, -9)\\)", "\\((-9, 0)\\)", "\\((0, 3)\\)", "\\((3, 0)\\)"],
     "A", "OSC", "easy",
     "At \\(x = 0\\), \\(y = -9\\). Point is \\((0, -9)\\)."),

    # 78
    ("What are the coordinates of the X-intercept for \\(y = 3x - 9\\)?",
     ["\\((3, 0)\\)", "\\((0, 3)\\)", "\\((-3, 0)\\)", "\\((0, -9)\\)"],
     "A", "OSC", "easy",
     "At \\(y = 0\\), \\(3x = 9 \\implies x = 3\\). Point is \\((3, 0)\\)."),

    # 79
    ("What is the slope of the line \\(x - y = 0\\)?",
     ["1", "-1", "0", "Undefined"],
     "A", "OSC", "easy",
     "\\(y = x \\implies m = 1\\)."),

    # 80
    ("What is the slope of the line \\(x + y = 0\\)?",
     ["-1", "1", "0", "Undefined"],
     "A", "OSC", "easy",
     "\\(y = -x \\implies m = -1\\)."),

    # 81
    ("Find the area of the rectangle whose vertices are \\((0,0)\\), \\((5,0)\\), \\((5,3)\\), and \\((0,3)\\).",
     ["15 sq units", "8 sq units", "16 sq units", "30 sq units"],
     "A", "OSC", "easy",
     "Length = 5, breadth = 3. Area = \\(5 \\times 3 = 15\\) sq units."),

    # 82
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0b132b" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1c2541" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Summary of Graphical Solutions</text>
  <text x="170" y="80" fill="#4ade80" font-size="11" text-anchor="middle">Intersecting Lines -> Exactly One Unique Solution</text>
  <text x="170" y="105" fill="#f87171" font-size="11" text-anchor="middle">Parallel Lines -> No Solution (Inconsistent)</text>
</svg>
</div>
What graphical condition corresponds to an inconsistent system of linear equations?""",
     ["The lines are parallel and never intersect",
      "The lines intersect at origin",
      "The lines are perpendicular",
      "The lines are coincident"],
     "A", "OSC", "easy",
     "An inconsistent system has zero solutions, which graphically means the lines are parallel and have no common intersection point.")
]

all_q_12 = build_topic_questions("MH-10-MTH1-1-1.2", t12_exam, t12_prac, t12_mock)
out_12 = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch1_t2.json")
with open(out_12, "w", encoding="utf-8") as f:
    json.dump(all_q_12, f, indent=2, ensure_ascii=False)
print(f"Generated {len(all_q_12)} questions for MH-10-MTH1-1-1.2 -> {out_12}")
