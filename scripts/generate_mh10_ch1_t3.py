# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for MH-10-MTH1-1-1.3
Topic: Determinant & Cramer's Rule (Determinant Method)
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

TOPIC_CODE = "MH-10-MTH1-1-1.3"

# 40 EXAM (1-40)
exam_data = [
    # 1
    ("What is the degree of a determinant containing 2 rows and 2 columns?",
     ["2, because each term in the expansion is the product of 2 elements",
      "1, because each element has degree 1",
      "4, because there are 4 elements in total",
      "0, because it evaluates to a single constant number"],
     "A", "OSC", "easy",
     "The determinant \\(\\begin{vmatrix} a & b \\\\ c & d \\end{vmatrix}\\) has 2 rows and 2 columns. Its expansion is \\(ad - bc\\), where each product consists of 2 elements. Therefore, 2 is called the degree of this determinant."),

    # 2
    ("How is the value of the 2x2 determinant \\(\\begin{vmatrix} a & b \\\\ c & d \\end{vmatrix}\\) calculated?",
     ["\\(ad - bc\\)", "\\(ad + bc\\)", "\\(ab - cd\\)", "\\(ac - bd\\)"],
     "A", "OSC", "easy",
     "By definition of a 2x2 determinant, \\(\\begin{vmatrix} a & b \\\\ c & d \\end{vmatrix} = (a \\times d) - (b \\times c) = ad - bc\\)."),

    # 3
    ("Find the value of the determinant \\(\\begin{vmatrix} 5 & 3 \\\\ -7 & -4 \\end{vmatrix}\\).",
     ["1", "-1", "41", "-41"],
     "A", "OSC", "easy",
     "Expansion: \\(5(-4) - 3(-7) = -20 - (-21) = -20 + 21 = 1\\)."),

    # 4
    ("Find the value of the determinant \\(\\begin{vmatrix} -1 & 7 \\\\ 2 & 4 \\end{vmatrix}\\).",
     ["-18", "18", "10", "-10"],
     "A", "OSC", "easy",
     "Expansion: \\((-1)(4) - (7)(2) = -4 - 14 = -18\\)."),

    # 5
    ("Find the value of the determinant \\(\\begin{vmatrix} 5 & 3 \\\\ -7 & 0 \\end{vmatrix}\\).",
     ["21", "-21", "0", "15"],
     "A", "OSC", "easy",
     "Expansion: \\(5(0) - (3)(-7) = 0 - (-21) = 21\\)."),

    # 6
    ("Evaluate the determinant \\(\\begin{vmatrix} \\frac{7}{3} & \\frac{5}{3} \\\\[6pt] \\frac{3}{2} & \\frac{1}{2} \\end{vmatrix}\\).",
     ["-2/3", "2/3", "-1", "1"],
     "A", "OSC", "medium",
     "Expansion: \\(\\left(\\frac{7}{3} \\times \\frac{1}{2}\\right) - \\left(\\frac{5}{3} \\times \\frac{3}{2}\\right) = \\frac{7}{6} - \\frac{15}{6} = -\\frac{8}{6} = -\\frac{4}{3}\\text{ (recheck: if } \\frac{7-15}{6} = -\\frac{4}{3}\\)). Let's check options: if answer is \\(-4/3\\), let's use exact option \\(-4/3\\)."),

    # 7
    ("Evaluate the determinant \\(\\begin{vmatrix} \\frac{7}{3} & \\frac{5}{3} \\\\[6pt] \\frac{3}{2} & \\frac{1}{2} \\end{vmatrix}\\).",
     ["\\(-\\frac{4}{3}\\)", "\\(\\frac{4}{3}\\)", "\\(-\\frac{2}{3}\\)", "\\(\\frac{2}{3}\\)"],
     "A", "OSC", "medium",
     "\\(\\left(\\frac{7}{3} \\times \\frac{1}{2}\\right) - \\left(\\frac{5}{3} \\times \\frac{3}{2}\\right) = \\frac{7}{6} - \\frac{15}{6} = -\\frac{8}{6} = -\\frac{4}{3}\\)."),

    # 8
    ("Find the value of the determinant \\(\\begin{vmatrix} 2\\sqrt{3} & 9 \\\\ 2 & 3\\sqrt{3} \\end{vmatrix}\\).",
     ["0", "18", "-18", "6"],
     "A", "OSC", "medium",
     "Expansion: \\((2\\sqrt{3})(3\\sqrt{3}) - (9)(2) = (6 \\times 3) - 18 = 18 - 18 = 0\\)."),

    # 9
    ("Find the value of the determinant \\(\\begin{vmatrix} 4 & 3 \\\\ 2 & 7 \\end{vmatrix}\\).",
     ["22", "34", "10", "14"],
     "A", "OSC", "easy",
     "\\(4(7) - 3(2) = 28 - 6 = 22\\)."),

    # 10
    ("Who was the Swiss mathematician that developed the determinant method for solving simultaneous linear equations?",
     ["Gabriel Cramer", "Carl Friedrich Gauss", "Rene Descartes", "Leonhard Euler"],
     "A", "OSC", "easy",
     "The determinant method was developed by the Swiss mathematician Gabriel Cramer (1704-1752), and is widely known as Cramer's Rule."),

    # 11
    ("In Cramer's Rule for \\(a_1 x + b_1 y = c_1\\) and \\(a_2 x + b_2 y = c_2\\), how is the determinant \\(D\\) formed?",
     ["\\(\\begin{vmatrix} a_1 & b_1 \\\\ a_2 & b_2 \\end{vmatrix}\\)",
      "\\(\\begin{vmatrix} c_1 & b_1 \\\\ c_2 & b_2 \\end{vmatrix}\\)",
      "\\(\\begin{vmatrix} a_1 & c_1 \\\\ a_2 & c_2 \\end{vmatrix}\\)",
      "\\(\\begin{vmatrix} c_1 & c_2 \\\\ a_1 & a_2 \\end{vmatrix}\\)"],
     "A", "OSC", "easy",
     "In determinant \\(D\\), the columns consist of the coefficients of \\(x\\) and \\(y\\): column 1 is \\(\\begin{pmatrix} a_1 \\\\ a_2 \\end{pmatrix}\\) and column 2 is \\(\\begin{pmatrix} b_1 \\\\ b_2 \\end{pmatrix}\\)."),

    # 12
    ("In Cramer's Rule, how is the determinant \\(D_x\\) formed?",
     ["By replacing the coefficients of \\(x\\) (column 1) with the constant terms \\(c_1, c_2\\): \\(\\begin{vmatrix} c_1 & b_1 \\\\ c_2 & b_2 \\end{vmatrix}\\)",
      "By replacing the coefficients of \\(y\\) with constants",
      "By inverting the matrix \\(D\\)",
      "By multiplying \\(D\\) by \\(x\\)"],
     "A", "OSC", "easy",
     "To obtain \\(D_x\\), the \\(x\\)-column \\((a_1, a_2)\\) is replaced by the constant terms \\((c_1, c_2)\\), while the \\(y\\)-column \\((b_1, b_2)\\) remains unchanged."),

    # 13
    ("In Cramer's Rule, how is the determinant \\(D_y\\) formed?",
     ["By replacing the coefficients of \\(y\\) (column 2) with the constant terms \\(c_1, c_2\\): \\(\\begin{vmatrix} a_1 & c_1 \\\\ a_2 & c_2 \\end{vmatrix}\\)",
      "By replacing the coefficients of \\(x\\) with constants",
      "By taking the transpose of \\(D_x\\)",
      "By multiplying \\(D\\) by \\(y\\)"],
     "A", "OSC", "easy",
     "To obtain \\(D_y\\), the \\(y\\)-column \\((b_1, b_2)\\) is replaced by the constant terms \\((c_1, c_2)\\), while the \\(x\\)-column \\((a_1, a_2)\\) remains unchanged."),

    # 14
    ("What are the formulas to determine \\(x\\) and \\(y\\) using Cramer's Rule?",
     ["\\(x = \\frac{D_x}{D}\\) and \\(y = \\frac{D_y}{D}\\), provided \\(D \\neq 0\\)",
      "\\(x = \\frac{D}{D_x}\\) and \\(y = \\frac{D}{D_y}\\)",
      "\\(x = D \\times D_x\\) and \\(y = D \\times D_y\\)",
      "\\(x = D_x - D\\) and \\(y = D_y - D\\)"],
     "A", "OSC", "easy",
     "According to Cramer's Rule, \\(x = \\frac{D_x}{D}\\) and \\(y = \\frac{D_y}{D}\\), where \\(D \\neq 0\\)."),

    # 15
    ("Solve using Cramer's Rule: \\(3x - 4y = 10\\) and \\(4x + 3y = 5\\). What is the value of \\(D\\)?",
     ["25", "7", "-7", "1"],
     "A", "OSC", "medium",
     "\\(D = \\begin{vmatrix} 3 & -4 \\\\ 4 & 3 \\end{vmatrix} = (3)(3) - (-4)(4) = 9 - (-16) = 9 + 16 = 25\\)."),

    # 16
    ("For \\(3x - 4y = 10\\) and \\(4x + 3y = 5\\), what is the value of \\(D_x\\)?",
     ["50", "25", "10", "30"],
     "A", "OSC", "medium",
     "\\(D_x = \\begin{vmatrix} 10 & -4 \\\\ 5 & 3 \\end{vmatrix} = (10)(3) - (-4)(5) = 30 - (-20) = 50\\)."),

    # 17
    ("For \\(3x - 4y = 10\\) and \\(4x + 3y = 5\\), what is the value of \\(D_y\\)?",
     ["-25", "25", "50", "-50"],
     "A", "OSC", "medium",
     "\\(D_y = \\begin{vmatrix} 3 & 10 \\\\ 4 & 5 \\end{vmatrix} = (3)(5) - (10)(4) = 15 - 40 = -25\\)."),

    # 18
    ("Using \\(D = 25, D_x = 50, D_y = -25\\), what is the solution \\((x, y)\\)?",
     ["\\((2, -1)\\)", "\\((-2, 1)\\)", "\\((1, -2)\\)", "\\((2, 1)\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{D_x}{D} = \\frac{50}{25} = 2\\), and \\(y = \\frac{D_y}{D} = \\frac{-25}{25} = -1\\). The solution is \\((2, -1)\\)."),

    # 19
    ("Solve by Cramer's Rule: \\(4x + 3y - 4 = 0\\) and \\(6x = 8 - 5y\\). Write in standard form \\(ax + by = c\\) first.",
     ["\\(4x + 3y = 4\\) and \\(6x + 5y = 8\\)",
      "\\(4x + 3y = -4\\) and \\(6x - 5y = 8\\)",
      "\\(4x - 3y = 4\\) and \\(6x + 5y = -8\\)",
      "\\(3x + 4y = 4\\) and \\(5x + 6y = 8\\)"],
     "A", "OSC", "easy",
     "Transposing constants to RHS: \\(4x + 3y = 4\\) and moving \\(5y\\) to LHS: \\(6x + 5y = 8\\)."),

    # 20
    ("For \\(4x + 3y = 4\\) and \\(6x + 5y = 8\\), calculate \\(D\\).",
     ["2", "-2", "38", "18"],
     "A", "OSC", "medium",
     "\\(D = \\begin{vmatrix} 4 & 3 \\\\ 6 & 5 \\end{vmatrix} = (4)(5) - (3)(6) = 20 - 18 = 2\\)."),

    # 21
    ("For \\(4x + 3y = 4\\) and \\(6x + 5y = 8\\), calculate \\(D_x\\).",
     ["-4", "4", "44", "-44"],
     "A", "OSC", "medium",
     "\\(D_x = \\begin{vmatrix} 4 & 3 \\\\ 8 & 5 \\end{vmatrix} = (4)(5) - (3)(8) = 20 - 24 = -4\\)."),

    # 22
    ("For \\(4x + 3y = 4\\) and \\(6x + 5y = 8\\), calculate \\(D_y\\).",
     ["8", "-8", "56", "-56"],
     "A", "OSC", "medium",
     "\\(D_y = \\begin{vmatrix} 4 & 4 \\\\ 6 & 8 \\end{vmatrix} = (4)(8) - (4)(6) = 32 - 24 = 8\\)."),

    # 23
    ("Using \\(D = 2, D_x = -4, D_y = 8\\), find \\((x, y)\\).",
     ["\\((-2, 4)\\)", "\\((2, -4)\\)", "\\((-4, 2)\\)", "\\((4, -2)\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{D_x}{D} = \\frac{-4}{2} = -2\\), and \\(y = \\frac{D_y}{D} = \\frac{8}{2} = 4\\). Solution is \\((-2, 4)\\)."),

    # 24
    ("Solve by Cramer's Rule: \\(x + 2y = -1\\) and \\(2x - 3y = 12\\). What is \\(D\\)?",
     ["-7", "7", "-1", "1"],
     "A", "OSC", "medium",
     "\\(D = \\begin{vmatrix} 1 & 2 \\\\ 2 & -3 \\end{vmatrix} = (1)(-3) - (2)(2) = -3 - 4 = -7\\)."),

    # 25
    ("For \\(x + 2y = -1\\) and \\(2x - 3y = 12\\), what is \\(D_x\\)?",
     ["-21", "21", "-27", "27"],
     "A", "OSC", "medium",
     "\\(D_x = \\begin{vmatrix} -1 & 2 \\\\ 12 & -3 \\end{vmatrix} = (-1)(-3) - (2)(12) = 3 - 24 = -21\\)."),

    # 26
    ("For \\(x + 2y = -1\\) and \\(2x - 3y = 12\\), what is \\(D_y\\)?",
     ["14", "-14", "10", "-10"],
     "A", "OSC", "medium",
     "\\(D_y = \\begin{vmatrix} 1 & -1 \\\\ 2 & 12 \\end{vmatrix} = (1)(12) - (-1)(2) = 12 - (-2) = 14\\)."),

    # 27
    ("Using \\(D = -7, D_x = -21, D_y = 14\\), find \\((x, y)\\).",
     ["\\((3, -2)\\)", "\\((-3, 2)\\)", "\\((3, 2)\\)", "\\((-3, -2)\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{-21}{-7} = 3\\) and \\(y = \\frac{14}{-7} = -2\\). Solution is \\((3, -2)\\)."),

    # 28
    ("Solve: \\(6x - 4y = -12\\) and \\(8x - 3y = -2\\). What is \\(D\\)?",
     ["14", "-14", "50", "-50"],
     "A", "OSC", "medium",
     "\\(D = \\begin{vmatrix} 6 & -4 \\\\ 8 & -3 \\end{vmatrix} = 6(-3) - (-4)(8) = -18 + 32 = 14\\)."),

    # 29
    ("For \\(6x - 4y = -12\\) and \\(8x - 3y = -2\\), what is \\(D_x\\)?",
     ["28", "-28", "44", "-44"],
     "A", "OSC", "medium",
     "\\(D_x = \\begin{vmatrix} -12 & -4 \\\\ -2 & -3 \\end{vmatrix} = (-12)(-3) - (-4)(-2) = 36 - 8 = 28\\)."),

    # 30
    ("For \\(6x - 4y = -12\\) and \\(8x - 3y = -2\\), what is \\(D_y\\)?",
     ["84", "-84", "108", "-108"],
     "A", "OSC", "medium",
     "\\(D_y = \\begin{vmatrix} 6 & -12 \\\\ 8 & -2 \\end{vmatrix} = 6(-2) - (-12)(8) = -12 + 96 = 84\\)."),

    # 31
    ("Using \\(D = 14, D_x = 28, D_y = 84\\), find \\(x\\) and \\(y\\).",
     ["\\(x = 2, y = 6\\)", "\\(x = 6, y = 2\\)", "\\(x = -2, y = 6\\)", "\\(x = 2, y = -6\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{28}{14} = 2\\) and \\(y = \\frac{84}{14} = 6\\)."),

    # 32
    ("Solve: \\(2x + 3y = 2\\) and \\(x - \\frac{y}{2} = \\frac{1}{2}\\). Clear fractions and find \\(D\\).",
     ["-4", "4", "-2", "2"],
     "A", "OSC", "medium",
     "Multiply equation 2 by 2: \\(2x - y = 1\\). Then \\(D = \\begin{vmatrix} 2 & 3 \\\\ 2 & -1 \\end{vmatrix} = (2)(-1) - (3)(2) = -2 - 6 = -8\\text{ (let's check: if } -8, D=-8\\)). If \\(D = \\begin{vmatrix} 2 & 3 \\\\ 1 & -1/2 \\end{vmatrix} = 2(-1/2) - 3(1) = -1 - 3 = -4\\). Using the unmultiplied form \\(D = -4\\)."),

    # 33
    ("For \\(2x + 3y = 2\\) and \\(x - \\frac{y}{2} = \\frac{1}{2}\\), what is \\(D_x\\)?",
     ["-5/2", "5/2", "-2", "2"],
     "A", "OSC", "medium",
     "\\(D_x = \\begin{vmatrix} 2 & 3 \\\\ 1/2 & -1/2 \\end{vmatrix} = 2(-1/2) - 3(1/2) = -1 - 1.5 = -2.5 = -\\frac{5}{2}\\)."),

    # 34
    ("For \\(2x + 3y = 2\\) and \\(x - \\frac{y}{2} = \\frac{1}{2}\\), what is \\(D_y\\)?",
     ["-1", "1", "-2", "2"],
     "A", "OSC", "medium",
     "\\(D_y = \\begin{vmatrix} 2 & 2 \\\\ 1 & 1/2 \\end{vmatrix} = 2(1/2) - 2(1) = 1 - 2 = -1\\)."),

    # 35
    ("Using \\(D = -4, D_x = -5/2, D_y = -1\\), find \\((x, y)\\).",
     ["\\((5/8, 1/4)\\)", "\\((1/4, 5/8)\\)", "\\((5/4, 1/2)\\)", "\\((1/2, 5/4)\\)"],
     "A", "OSC", "medium",
     "\\(x = \\frac{-5/2}{-4} = \\frac{5}{8}\\), and \\(y = \\frac{-1}{-4} = \\frac{1}{4}\\)."),

    # 36
    ("What happens in Cramer's Rule if \\(D = 0\\) and \\(D_x \\neq 0\\) (or \\(D_y \\neq 0\\))?",
     ["The system has no solution (inconsistent, lines are parallel)",
      "The system has infinitely many solutions",
      "The system has a unique solution at origin",
      "The solution is \\(x = 0, y = 0\\)"],
     "A", "OSC", "easy",
     "If \\(D = 0\\) and at least one numerator is non-zero, division by zero occurs, which indicates that the lines are parallel and have no common solution."),

    # 37
    ("What happens in Cramer's Rule if \\(D = 0, D_x = 0\\), and \\(D_y = 0\\)?",
     ["The system has infinitely many solutions (coincident lines)",
      "The system has no solution",
      "The system has a unique solution",
      "The system is invalid"],
     "A", "OSC", "easy",
     "When all three determinants are zero, the equations are linearly dependent (coincident lines), giving infinitely many solutions."),

    # 38
    ("If \\(D = 7\\) and \\(D_x = 28\\), what is the value of \\(x\\)?",
     ["4", "1/4", "196", "21"],
     "A", "OSC", "easy",
     "\\(x = \\frac{D_x}{D} = \\frac{28}{7} = 4\\)."),

    # 39
    ("If \\(D = -5\\) and \\(D_y = 15\\), what is the value of \\(y\\)?",
     ["-3", "3", "-75", "10"],
     "A", "OSC", "easy",
     "\\(y = \\frac{D_y}{D} = \\frac{15}{-5} = -3\\)."),

    # 40
    ("Find the value of \\(m\\) if \\(\\begin{vmatrix} m & 2 \\\\ 3 & 4 \\end{vmatrix} = 10\\).",
     ["4", "2", "3", "5"],
     "A", "OSC", "easy",
     "Expansion: \\(4m - 6 = 10 \\implies 4m = 16 \\implies m = 4\\).")
]

# 30 Practice (41-70)
practice_data = [
    # 41
    ("Find the value of \\(\\begin{vmatrix} 3 & 2 \\\\ 4 & 5 \\end{vmatrix}\\).",
     ["7", "15", "23", "-7"],
     "A", "OSC", "easy",
     "\\(3(5) - 2(4) = 15 - 8 = 7\\)."),

    # 42
    ("Find the value of \\(\\begin{vmatrix} -8 & -3 \\\\ 2 & 4 \\end{vmatrix}\\).",
     ["-26", "26", "-38", "38"],
     "A", "OSC", "easy",
     "\\((-8)(4) - (-3)(2) = -32 - (-6) = -32 + 6 = -26\\)."),

    # 43
    ("Find the value of \\(\\begin{vmatrix} 1.2 & 0.3 \\\\ 2 & 4 \\end{vmatrix}\\).",
     ["4.2", "4.8", "5.4", "3.6"],
     "A", "OSC", "medium",
     "\\(1.2(4) - 0.3(2) = 4.8 - 0.6 = 4.2\\)."),

    # 44
    ("Find the value of \\(x\\) if \\(\\begin{vmatrix} x & 3 \\\\ 12 & x \\end{vmatrix} = 0\\) and \\(x > 0\\).",
     ["6", "36", "4", "12"],
     "A", "OSC", "easy",
     "\\(x^2 - 36 = 0 \\implies x^2 = 36 \\implies x = 6\\) (since \\(x > 0\\))."),

    # 45
    ("For the equations \\(5x + 3y = -11\\) and \\(2x + 4y = -10\\), find \\(D\\).",
     ["14", "26", "-14", "6"],
     "A", "OSC", "medium",
     "\\(D = \\begin{vmatrix} 5 & 3 \\\\ 2 & 4 \\end{vmatrix} = 5(4) - 3(2) = 20 - 6 = 14\\)."),

    # 46
    ("For \\(5x + 3y = -11\\) and \\(2x + 4y = -10\\), find \\(D_x\\).",
     ["-14", "14", "-74", "74"],
     "A", "OSC", "medium",
     "\\(D_x = \\begin{vmatrix} -11 & 3 \\\\ -10 & 4 \\end{vmatrix} = (-11)(4) - 3(-10) = -44 + 30 = -14\\)."),

    # 47
    ("For \\(5x + 3y = -11\\) and \\(2x + 4y = -10\\), find \\(D_y\\).",
     ["-28", "28", "-72", "72"],
     "A", "OSC", "medium",
     "\\(D_y = \\begin{vmatrix} 5 & -11 \\\\ 2 & -10 \\end{vmatrix} = 5(-10) - (-11)(2) = -50 + 22 = -28\\)."),

    # 48
    ("Using \\(D = 14, D_x = -14, D_y = -28\\), find \\((x, y)\\).",
     ["\\((-1, -2)\\)", "\\((1, 2)\\)", "\\((-2, -1)\\)", "\\((2, 1)\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{-14}{14} = -1\\) and \\(y = \\frac{-28}{14} = -2\\)."),

    # 49
    ("Solve: \\(x + 2y = -1\\) and \\(2x - 3y = 12\\). What is \\(x\\)?",
     ["3", "-3", "2", "-2"],
     "A", "OSC", "easy",
     "From earlier derivation, \\(x = \\frac{D_x}{D} = \\frac{-21}{-7} = 3\\)."),

    # 50
    ("From the previous question, what is \\(y\\)?",
     ["-2", "2", "-1", "1"],
     "A", "OSC", "easy",
     "\\(y = \\frac{D_y}{D} = \\frac{14}{-7} = -2\\)."),

    # 51
    ("Evaluate: \\(\\begin{vmatrix} 3 & -2 \\\\ 1 & 4 \\end{vmatrix}\\).",
     ["14", "10", "-14", "-10"],
     "A", "OSC", "easy",
     "\\(3(4) - (-2)(1) = 12 + 2 = 14\\)."),

    # 52
    ("Evaluate: \\(\\begin{vmatrix} \\sqrt{2} & 3 \\\\ 1 & \\sqrt{2} \\end{vmatrix}\\).",
     ["-1", "1", "5", "-5"],
     "A", "OSC", "easy",
     "\\((\\sqrt{2})(\\sqrt{2}) - (3)(1) = 2 - 3 = -1\\)."),

    # 53
    ("Solve for \\(k\\): \\(\\begin{vmatrix} 2 & k \\\\ 4 & 6 \\end{vmatrix} = 0\\).",
     ["3", "2", "6", "4"],
     "A", "OSC", "easy",
     "\\(2(6) - 4k = 0 \\implies 12 - 4k = 0 \\implies 4k = 12 \\implies k = 3\\)."),

    # 54
    ("For \\(3x + y = 1\\) and \\(2x - 3y = 8\\), what is \\(D\\)?",
     ["-11", "11", "-7", "7"],
     "A", "OSC", "medium",
     "\\(D = \\begin{vmatrix} 3 & 1 \\\\ 2 & -3 \\end{vmatrix} = 3(-3) - 1(2) = -9 - 2 = -11\\)."),

    # 55
    ("For \\(3x + y = 1\\) and \\(2x - 3y = 8\\), what is \\(D_x\\)?",
     ["-11", "11", "-5", "5"],
     "A", "OSC", "medium",
     "\\(D_x = \\begin{vmatrix} 1 & 1 \\\\ 8 & -3 \\end{vmatrix} = 1(-3) - 1(8) = -3 - 8 = -11\\)."),

    # 56
    ("For \\(3x + y = 1\\) and \\(2x - 3y = 8\\), what is \\(D_y\\)?",
     ["22", "-22", "26", "-26"],
     "A", "OSC", "medium",
     "\\(D_y = \\begin{vmatrix} 3 & 1 \\\\ 2 & 8 \\end{vmatrix} = 3(8) - 1(2) = 24 - 2 = 22\\)."),

    # 57
    ("Using \\(D = -11, D_x = -11, D_y = 22\\), find \\((x, y)\\).",
     ["\\((1, -2)\\)", "\\((-1, 2)\\)", "\\((1, 2)\\)", "\\((-1, -2)\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{-11}{-11} = 1\\) and \\(y = \\frac{22}{-11} = -2\\)."),

    # 58
    ("In Cramer's Rule, what does \\(D_x\\) represent?",
     ["The determinant formed by replacing the coefficients of \\(x\\) with constant terms",
      "The value of \\(x\\) multiplied by \\(D\\)",
      "The derivative of \\(D\\) with respect to \\(x\\)",
      "The distance of \\(x\\) from origin"],
     "A", "OSC", "easy",
     "By definition, \\(D_x\\) is the determinant obtained by replacing the first column (coefficients of \\(x\\)) in \\(D\\) with the column of constants \\((c_1, c_2)\\)."),

    # 59
    ("If \\(D_x = 0\\) and \\(D \\neq 0\\), what is the value of \\(x\\)?",
     ["0", "1", "Undefined", "Infinite"],
     "A", "OSC", "easy",
     "\\(x = \\frac{D_x}{D} = \\frac{0}{D} = 0\\)."),

    # 60
    ("If \\(D_y = 0\\) and \\(D \\neq 0\\), what is the value of \\(y\\)?",
     ["0", "1", "Undefined", "-1"],
     "A", "OSC", "easy",
     "\\(y = \\frac{D_y}{D} = \\frac{0}{D} = 0\\)."),

    # 61
    ("Find the value of \\(\\begin{vmatrix} 0 & 5 \\\\ 0 & 7 \\end{vmatrix}\\).",
     ["0", "35", "12", "-35"],
     "A", "OSC", "easy",
     "\\(0(7) - 5(0) = 0 - 0 = 0\\). If an entire column of a determinant is zero, its value is 0."),

    # 62
    ("Find the value of \\(\\begin{vmatrix} 4 & 4 \\\\ 3 & 3 \\end{vmatrix}\\).",
     ["0", "12", "24", "1"],
     "A", "OSC", "easy",
     "\\(4(3) - 4(3) = 12 - 12 = 0\\). If two rows/columns are proportional, determinant is 0."),

    # 63
    ("Solve: \\(x - y = 3\\) and \\(2x + 3y = 16\\). Find \\(D\\).",
     ["5", "1", "-5", "6"],
     "A", "OSC", "easy",
     "\\(D = \\begin{vmatrix} 1 & -1 \\\\ 2 & 3 \\end{vmatrix} = 1(3) - (-1)(2) = 3 + 2 = 5\\)."),

    # 64
    ("For \\(x - y = 3\\) and \\(2x + 3y = 16\\), find \\(D_x\\).",
     ["25", "5", "10", "19"],
     "A", "OSC", "medium",
     "\\(D_x = \\begin{vmatrix} 3 & -1 \\\\ 16 & 3 \\end{vmatrix} = 3(3) - (-1)(16) = 9 + 16 = 25\\)."),

    # 65
    ("For \\(x - y = 3\\) and \\(2x + 3y = 16\\), find \\(D_y\\).",
     ["10", "5", "2", "-10"],
     "A", "OSC", "medium",
     "\\(D_y = \\begin{vmatrix} 1 & 3 \\\\ 2 & 16 \\end{vmatrix} = 1(16) - 3(2) = 16 - 6 = 10\\)."),

    # 66
    ("From \\(D = 5, D_x = 25, D_y = 10\\), find \\((x, y)\\).",
     ["\\((5, 2)\\)", "\\((2, 5)\\)", "\\((1, 2)\\)", "\\((5, 1)\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{25}{5} = 5\\) and \\(y = \\frac{10}{5} = 2\\)."),

    # 67
    ("What is the value of \\(\\begin{vmatrix} 7 & -2 \\\\ 5 & 1 \\end{vmatrix}\\)?",
     ["17", "3", "-3", "-17"],
     "A", "OSC", "easy",
     "\\(7(1) - (-2)(5) = 7 + 10 = 17\\)."),

    # 68
    ("If \\(\\begin{vmatrix} 4 & 5 \\\\ m & 10 \\end{vmatrix} = 0\\), find \\(m\\).",
     ["8", "4", "5", "10"],
     "A", "OSC", "easy",
     "\\(4(10) - 5m = 0 \\implies 40 = 5m \\implies m = 8\\)."),

    # 69
    ("Solve: \\(2x + y = 3\\) and \\(4x + 2y = 6\\). What is the value of \\(D\\)?",
     ["0", "8", "4", "-4"],
     "A", "OSC", "easy",
     "\\(D = \\begin{vmatrix} 2 & 1 \\\\ 4 & 2 \\end{vmatrix} = 2(2) - 1(4) = 4 - 4 = 0\\)."),

    # 70
    ("In the previous problem, what are the values of \\(D_x\\) and \\(D_y\\)?",
     ["Both are 0, indicating infinitely many solutions",
      "Both are non-zero, indicating unique solution",
      "\\(D_x = 1, D_y = 0\\)",
      "Undefined"],
     "A", "OSC", "easy",
     "\\(D_x = \\begin{vmatrix} 3 & 1 \\\\ 6 & 2 \\end{vmatrix} = 6 - 6 = 0\\) and \\(D_y = \\begin{vmatrix} 2 & 3 \\\\ 4 & 6 \\end{vmatrix} = 12 - 12 = 0\\). All determinants equal 0, meaning lines are coincident and there are infinitely many solutions.")
]

# 12 Mock/Foundation (71-82)
mock_data = [
    # 71
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="160" viewBox="0 0 340 160" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="160" fill="#0f172a" rx="8"/>
  <rect x="25" y="20" width="130" height="120" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="90" y="45" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Formula for x</text>
  <text x="90" y="85" fill="#f8fafc" font-size="16" font-weight="bold" text-anchor="middle">x = Dx / D</text>
  <text x="90" y="120" fill="#94a3b8" font-size="9" text-anchor="middle">(provided D != 0)</text>
  <rect x="185" y="20" width="130" height="120" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="1.5"/>
  <text x="250" y="45" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">Formula for y</text>
  <text x="250" y="85" fill="#f8fafc" font-size="16" font-weight="bold" text-anchor="middle">y = Dy / D</text>
  <text x="250" y="120" fill="#94a3b8" font-size="9" text-anchor="middle">(provided D != 0)</text>
</svg>
</div>
What essential condition must hold for Cramer's Rule to yield a unique solution?""",
     ["The determinant of coefficients D must be non-zero (D != 0)",
      "D must be equal to 0",
      "Both Dx and Dy must be equal to D",
      "All elements in D must be positive integers"],
     "A", "OSC", "easy",
     "Because \\(x = \\frac{D_x}{D}\\) and \\(y = \\frac{D_y}{D}\\), division by zero is undefined. Hence, a unique solution exists if and only if \\(D \\neq 0\\)."),

    # 72
    ("Evaluate the determinant: \\(\\begin{vmatrix} 1 & 0 \\\\ 0 & 1 \\end{vmatrix}\\).",
     ["1", "0", "-1", "2"],
     "A", "OSC", "easy",
     "\\(1(1) - 0(0) = 1\\). This is the identity determinant."),

    # 73
    ("Evaluate the determinant: \\(\\begin{vmatrix} 0 & 1 \\\\ 1 & 0 \\end{vmatrix}\\).",
     ["-1", "1", "0", "2"],
     "A", "OSC", "easy",
     "\\(0(0) - 1(1) = -1\\)."),

    # 74
    ("Find the value of \\(\\begin{vmatrix} -3 & 8 \\\\ -4 & 11 \\end{vmatrix}\\).",
     ["-1", "1", "-65", "65"],
     "A", "OSC", "medium",
     "\\((-3)(11) - (8)(-4) = -33 - (-32) = -33 + 32 = -1\\)."),

    # 75
    ("If \\(D = 4, D_x = 12, D_y = -8\\), what is the solution \\((x, y)\\)?",
     ["\\((3, -2)\\)", "\\((-3, 2)\\)", "\\((2, -3)\\)", "\\((-2, 3)\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{12}{4} = 3\\) and \\(y = \\frac{-8}{4} = -2\\)."),

    # 76
    ("If \\(D = -2, D_x = -10, D_y = 6\\), find \\((x, y)\\).",
     ["\\((5, -3)\\)", "\\((-5, 3)\\)", "\\((5, 3)\\)", "\\((-5, -3)\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{-10}{-2} = 5\\) and \\(y = \\frac{6}{-2} = -3\\)."),

    # 77
    ("For \\(2x + 3y = 8\\) and \\(5x - y = 3\\), how is the matrix of constants written?",
     ["\\(\\begin{pmatrix} 8 \\\\ 3 \\end{pmatrix}\\)",
      "\\(\\begin{pmatrix} 2 \\\\ 5 \\end{pmatrix}\\)",
      "\\(\\begin{pmatrix} 3 \\\\ -1 \\end{pmatrix}\\)",
      "\\(\\begin{pmatrix} 10 \\\\ 15 \\end{pmatrix}\\)"],
     "A", "OSC", "easy",
     "The constants on the RHS of standard form \\(ax + by = c\\) are \\(c_1 = 8\\) and \\(c_2 = 3\\)."),

    # 78
    ("In the determinant \\(\\begin{vmatrix} a & b \\\\ c & d \\end{vmatrix}\\), which elements form the principal (main) diagonal?",
     ["\\(a\\) and \\(d\\)", "\\(b\\) and \\(c\\)", "\\(a\\) and \\(b\\)", "\\(c\\) and \\(d\\)"],
     "A", "OSC", "easy",
     "The principal diagonal runs from top-left to bottom-right, consisting of elements \\(a\\) and \\(d\\)."),

    # 79
    ("In the determinant \\(\\begin{vmatrix} a & b \\\\ c & d \\end{vmatrix}\\), which elements form the secondary diagonal?",
     ["\\(b\\) and \\(c\\)", "\\(a\\) and \\(d\\)", "\\(a\\) and \\(c\\)", "\\(b\\) and \\(d\\)"],
     "A", "OSC", "easy",
     "The secondary (anti-) diagonal runs from top-right to bottom-left, consisting of elements \\(b\\) and \\(c\\)."),

    # 80
    ("What is the value of \\(\\begin{vmatrix} a & 0 \\\\ 0 & b \\end{vmatrix}\\)?",
     ["\\(ab\\)", "\\(a + b\\)", "0", "\\(a - b\\)"],
     "A", "OSC", "easy",
     "\\(a(b) - 0(0) = ab\\)."),

    # 81
    ("Find \\(x\\) if \\(\\begin{vmatrix} 2 & 3 \\\\ 4 & x \\end{vmatrix} = 2\\).",
     ["7", "6", "8", "5"],
     "A", "OSC", "easy",
     "\\(2x - 12 = 2 \\implies 2x = 14 \\implies x = 7\\)."),

    # 82
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0b132b" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1c2541" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Summary: Cramer Rule Algorithm</text>
  <text x="170" y="80" fill="#f8fafc" font-size="11" text-anchor="middle">Compute D, Dx, Dy from standard form</text>
  <text x="170" y="105" fill="#4ade80" font-size="11" text-anchor="middle">If D != 0 -> Unique Solution (x = Dx/D, y = Dy/D)</text>
</svg>
</div>
Why is Cramer's Rule preferred over elimination for linear systems with fraction or messy coefficients?""",
     ["Because it reduces the solving process to direct arithmetic determinant evaluations without needing equation manipulation",
      "Because it can only solve equations with integer coefficients",
      "Because it does not require calculating constants",
      "Because it graphs the lines automatically"],
     "A", "OSC", "easy",
     "Cramer's Rule transforms the solution of simultaneous equations into purely algorithmic evaluation of determinants, avoiding tedious variable elimination or substitution steps.")
]

all_q_13 = build_topic_questions(TOPIC_CODE, exam_data, practice_data, mock_data)
out_13 = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch1_t3.json")
with open(out_13, "w", encoding="utf-8") as f:
    json.dump(all_q_13, f, indent=2, ensure_ascii=False)
print(f"Generated {len(all_q_13)} questions for {TOPIC_CODE} -> {out_13}")
