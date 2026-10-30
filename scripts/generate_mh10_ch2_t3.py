# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 2: Quadratic Equations (Topics 2.3 & 2.4)
Each topic: exactly 82 canonical questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# ==============================================================================
# TOPIC 2.3: Completing the Square Method (MH-10-MTH1-2-2.3)
# ==============================================================================
t23_exam = [
    # 1
    ("What is the formula for the third term to make \\(x^2 + bx\\) a perfect square trinomial?",
     ["\\(\\left(\\frac{1}{2} \\times \\text{coefficient of } x\\right)^2 = \\left(\\frac{b}{2}\\right)^2\\)",
      "\\(\\left(\\text{coefficient of } x\\right)^2 = b^2\\)",
      "\\(\\frac{1}{2} \\times b\\)",
      "\\(2 \\times b^2\\)"],
     "A", "OSC", "easy",
     "To transform \\(x^2 + bx\\) into a perfect square \\((x + b/2)^2\\), we must add \\((b/2)^2\\), which is \\([1/2 \\times (\\text{coefficient of } x)]^2\\)."),

    # 2
    ("What third term must be added to \\(x^2 + 6x\\) to complete the square?",
     ["9", "3", "36", "12"],
     "A", "OSC", "easy",
     "\\(\\left(\\frac{1}{2} \\times 6\\right)^2 = 3^2 = 9\\). Then \\(x^2 + 6x + 9 = (x + 3)^2\\)."),

    # 3
    ("What third term must be added to \\(x^2 - 10x\\) to complete the square?",
     ["25", "-25", "100", "5"],
     "A", "OSC", "easy",
     "\\(\\left(\\frac{1}{2} \\times (-10)\\right)^2 = (-5)^2 = 25\\). Then \\(x^2 - 10x + 25 = (x - 5)^2\\)."),

    # 4
    ("What third term must be added to \\(x^2 + x\\) to complete the square?",
     ["\\(\\frac{1}{4}\\)", "\\(\\frac{1}{2}\\)", "1", "\\(4\\)"],
     "A", "OSC", "easy",
     "\\(\\left(\\frac{1}{2} \\times 1\\right)^2 = \\frac{1}{4}\\). Then \\(x^2 + x + 1/4 = (x + 1/2)^2\\)."),

    # 5
    ("What third term must be added to \\(m^2 - 5m\\) to complete the square?",
     ["\\(\\frac{25}{4}\\)", "\\(\\frac{5}{2}\\)", "25", "5"],
     "A", "OSC", "easy",
     "\\(\\left(\\frac{1}{2} \\times (-5)\\right)^2 = \\left(-\\frac{5}{2}\\right)^2 = \\frac{25}{4}\\)."),

    # 6
    ("Solve by completing the square: \\(x^2 + x - 20 = 0\\). What are the roots?",
     ["\\(4\\) and \\(-5\\)", "\\(-4\\) and \\(5\\)", "\\(10\\) and \\(-2\\)", "\\(-10\\) and \\(2\\)"],
     "A", "OSC", "medium",
     "Third term = \\((1/2)^2 = 1/4\\). \\(x^2 + x + 1/4 = 20 + 1/4 \\implies (x + 1/2)^2 = 81/4\\). Taking square root: \\(x + 1/2 = \\pm 9/2\\). Thus \\(x = 9/2 - 1/2 = 4\\) or \\(x = -9/2 - 1/2 = -5\\)."),

    # 7
    ("Solve by completing the square: \\(x^2 + 2x - 5 = 0\\). What are the roots?",
     ["\\(-1 \\pm \\sqrt{6}\\)",
      "\\(1 \\pm \\sqrt{6}\\)",
      "\\(-2 \\pm \\sqrt{5}\\)",
      "\\(-1 \\pm 6\\)"],
     "A", "OSC", "medium",
     "Third term = \\((2/2)^2 = 1\\). \\(x^2 + 2x + 1 = 5 + 1 \\implies (x + 1)^2 = 6 \\implies x + 1 = \\pm \\sqrt{6} \\implies x = -1 \\pm \\sqrt{6}\\)."),

    # 8
    ("Solve: \\(m^2 - 5m = -3\\). What are the roots?",
     ["\\(\\frac{5 \\pm \\sqrt{13}}{2}\\)",
      "\\(\\frac{-5 \\pm \\sqrt{13}}{2}\\)",
      "\\(5 \\pm \\sqrt{13}\\)",
      "\\(\\frac{5 \\pm 13}{2}\\)"],
     "A", "OSC", "medium",
     "Third term = \\((-5/2)^2 = 25/4\\). \\(m^2 - 5m + 25/4 = -3 + 25/4 = 13/4 \\implies (m - 5/2)^2 = 13/4 \\implies m - 5/2 = \\pm \\frac{\\sqrt{13}}{2} \\implies m = \\frac{5 \\pm \\sqrt{13}}{2}\\)."),

    # 9
    ("Solve: \\(9y^2 - 12y + 2 = 0\\). What are the roots?",
     ["\\(\\frac{2 \\pm \\sqrt{2}}{3}\\)",
      "\\(\\frac{-2 \\pm \\sqrt{2}}{3}\\)",
      "\\(\\frac{2 \\pm 2}{3}\\)",
      "\\(2 \\pm \\sqrt{2}\\)"],
     "A", "OSC", "hard",
     "Divide by 9: \\(y^2 - \\frac{4}{3}y + \\frac{2}{9} = 0 \\implies y^2 - \\frac{4}{3}y = -\\frac{2}{9}\\). Third term = \\((-2/3)^2 = 4/9\\). \\((y - 2/3)^2 = -2/9 + 4/9 = 2/9 \\implies y - 2/3 = \\pm \\frac{\\sqrt{2}}{3} \\implies y = \\frac{2 \\pm \\sqrt{2}}{3}\\)."),

    # 10
    ("Solve: \\(2y^2 + 9y + 10 = 0\\) by completing the square.",
     ["\\(-2\\) and \\(-\\frac{5}{2}\\)",
      "\\(2\\) and \\(\\frac{5}{2}\\)",
      "\\(-1\\) and \\(-5\\)",
      "\\(-2\\) and \\(-5\\)"],
     "A", "OSC", "medium",
     "Divide by 2: \\(y^2 + \\frac{9}{2}y = -5\\). Third term = \\((9/4)^2 = 81/16\\). \\((y + 9/4)^2 = -5 + 81/16 = 1/16 \\implies y + 9/4 = \\pm 1/4 \\implies y = -9/4 + 1/4 = -2\\) or \\(y = -9/4 - 1/4 = -5/2\\)."),

    # 11
    ("Solve: \\(5x^2 = 4x + 7\\). What are the roots?",
     ["\\(\\frac{2 \\pm \\sqrt{39}}{5}\\)",
      "\\(\\frac{-2 \\pm \\sqrt{39}}{5}\\)",
      "\\(\\frac{4 \\pm \\sqrt{39}}{5}\\)",
      "\\(2 \\pm \\sqrt{39}\\)"],
     "A", "OSC", "hard",
     "\\(x^2 - \\frac{4}{5}x = \\frac{7}{5}\\). Third term = \\((-2/5)^2 = 4/25\\). \\((x - 2/5)^2 = \\frac{7}{5} + \\frac{4}{25} = \\frac{39}{25} \\implies x - 2/5 = \\pm \\frac{\\sqrt{39}}{5} \\implies x = \\frac{2 \\pm \\sqrt{39}}{5}\\)."),

    # 12
    ("Why must we divide by the coefficient of \\(x^2\\) when using completing the square if \\(a \\neq 1\\)?",
     ["To make the coefficient of \\(x^2\\) equal to 1, allowing direct application of the formula \\((b/2)^2\\)",
      "Because completing the square cannot solve equations with leading coefficients other than 1",
      "To eliminate the constant term",
      "Because fractional roots are illegal"],
     "A", "OSC", "easy",
     "The algebraic identity \\(x^2 + 2kx + k^2 = (x + k)^2\\) has 1 as the coefficient of \\(x^2\\). Dividing by \\(a\\) normalizes the leading term so that the third term is simply \\((b/2a)^2\\)."),

    # 13
    ("Solve: \\(x^2 - 4x - 1 = 0\\). What are the roots?",
     ["\\(2 \\pm \\sqrt{5}\\)", "\\(-2 \\pm \\sqrt{5}\\)", "\\(2 \\pm 5\\)", "\\(4 \\pm \\sqrt{5}\\)"],
     "A", "OSC", "medium",
     "Third term = \\((-2)^2 = 4\\). \\(x^2 - 4x + 4 = 1 + 4 = 5 \\implies (x - 2)^2 = 5 \\implies x = 2 \\pm \\sqrt{5}\\)."),

    # 14
    ("Solve: \\(x^2 + 8x + 12 = 0\\) by completing the square.",
     ["\\(-2\\) and \\(-6\\)", "\\(2\\) and \\(6\\)", "\\(-4\\) and \\(-3\\)", "\\(4\\) and \\(3\\)"],
     "A", "OSC", "easy",
     "Third term = \\(4^2 = 16\\). \\(x^2 + 8x + 16 = -12 + 16 = 4 \\implies (x + 4)^2 = 4 \\implies x + 4 = \\pm 2 \\implies x = -2\\) or \\(x = -6\\)."),

    # 15
    ("Solve: \\(x^2 - 6x - 7 = 0\\) by completing the square.",
     ["\\(7\\) and \\(-1\\)", "\\(-7\\) and \\(1\\)", "\\(6\\) and \\(1\\)", "\\(-6\\) and \\(-1\\)"],
     "A", "OSC", "easy",
     "Third term = \\((-3)^2 = 9\\). \\(x^2 - 6x + 9 = 7 + 9 = 16 \\implies (x - 3)^2 = 16 \\implies x - 3 = \\pm 4 \\implies x = 7\\) or \\(x = -1\\)."),

    # 16
    ("What third term completes the square for \\(y^2 + 3y\\)?",
     ["\\(\\frac{9}{4}\\)", "\\(\\frac{3}{2}\\)", "9", "3"],
     "A", "OSC", "easy",
     "\\((3/2)^2 = 9/4\\)."),

    # 17
    ("What third term completes the square for \\(x^2 - \\frac{2}{3}x\\)?",
     ["\\(\\frac{1}{9}\\)", "\\(\\frac{2}{3}\\)", "\\(\\frac{4}{9}\\)", "\\(\\frac{1}{3}\\)"],
     "A", "OSC", "easy",
     "\\((-1/3)^2 = 1/9\\)."),

    # 18
    ("What third term completes the square for \\(x^2 + \\frac{5}{2}x\\)?",
     ["\\(\\frac{25}{16}\\)", "\\(\\frac{5}{4}\\)", "\\(\\frac{25}{4}\\)", "\\(\\frac{5}{16}\\)"],
     "A", "OSC", "easy",
     "\\((5/4)^2 = 25/16\\)."),

    # 19
    ("Solve: \\(x^2 - 2x - 3 = 0\\) by completing the square.",
     ["\\(3\\) and \\(-1\\)", "\\(-3\\) and \\(1\\)", "\\(2\\) and \\(1\\)", "\\(-2\\) and \\(-1\\)"],
     "A", "OSC", "easy",
     "\\((x - 1)^2 = 3 + 1 = 4 \\implies x - 1 = \\pm 2 \\implies x = 3\\) or \\(x = -1\\)."),

    # 20
    ("Solve: \\(x^2 + 4x + 1 = 0\\). What are the roots?",
     ["\\(-2 \\pm \\sqrt{3}\\)", "\\(2 \\pm \\sqrt{3}\\)", "\\(-2 \\pm 3\\)", "\\(-4 \\pm \\sqrt{3}\\)"],
     "A", "OSC", "medium",
     "\\(x^2 + 4x + 4 = -1 + 4 = 3 \\implies (x + 2)^2 = 3 \\implies x = -2 \\pm \\sqrt{3}\\)."),

    # 21
    ("Solve: \\(x^2 - 6x + 2 = 0\\).",
     ["\\(3 \\pm \\sqrt{7}\\)", "\\(-3 \\pm \\sqrt{7}\\)", "\\(3 \\pm 7\\)", "\\(6 \\pm \\sqrt{7}\\)"],
     "A", "OSC", "medium",
     "\\(x^2 - 6x + 9 = -2 + 9 = 7 \\implies (x - 3)^2 = 7 \\implies x = 3 \\pm \\sqrt{7}\\)."),

    # 22
    ("Solve: \\(x^2 + 10x + 21 = 0\\) by completing the square.",
     ["\\(-3\\) and \\(-7\\)", "\\(3\\) and \\(7\\)", "\\(-5\\) and \\(-2\\)", "\\(5\\) and \\(2\\)"],
     "A", "OSC", "easy",
     "\\((x + 5)^2 = -21 + 25 = 4 \\implies x + 5 = \\pm 2 \\implies x = -3\\) or \\(x = -7\\)."),

    # 23
    ("Solve: \\(x^2 - 12x + 20 = 0\\) by completing the square.",
     ["\\(10\\) and \\(2\\)", "\\(-10\\) and \\(-2\\)", "\\(12\\) and \\(1\\)", "\\(-12\\) and \\(-1\\)"],
     "A", "OSC", "easy",
     "\\((x - 6)^2 = -20 + 36 = 16 \\implies x - 6 = \\pm 4 \\implies x = 10\\) or \\(x = 2\\)."),

    # 24
    ("Solve: \\(2x^2 - 5x + 3 = 0\\) by completing the square.",
     ["\\(1\\) and \\(\\frac{3}{2}\\)",
      "\\(-1\\) and \\(-\\frac{3}{2}\\)",
      "\\(2\\) and \\(3\\)",
      "\\(1\\) and \\(3\\)"],
     "A", "OSC", "medium",
     "Divide by 2: \\(x^2 - \\frac{5}{2}x = -\\frac{3}{2}\\). Third term = \\(25/16\\). \\((x - 5/4)^2 = -3/2 + 25/16 = 1/16 \\implies x - 5/4 = \\pm 1/4 \\implies x = 6/4 = 3/2\\) or \\(x = 4/4 = 1\\)."),

    # 25
    ("Solve: \\(x^2 - 8x + 15 = 0\\).",
     ["\\(5\\) and \\(3\\)", "\\(-5\\) and \\(-3\\)", "\\(15\\) and \\(1\\)", "\\(-15\\) and \\(-1\\)"],
     "A", "OSC", "easy",
     "\\((x - 4)^2 = -15 + 16 = 1 \\implies x - 4 = \\pm 1 \\implies x = 5\\) or \\(x = 3\\)."),

    # 26
    ("Solve: \\(x^2 + 8x + 15 = 0\\).",
     ["\\(-5\\) and \\(-3\\)", "\\(5\\) and \\(3\\)", "\\(-15\\) and \\(-1\\)", "\\(15\\) and \\(1\\)"],
     "A", "OSC", "easy",
     "\\((x + 4)^2 = -15 + 16 = 1 \\implies x + 4 = \\pm 1 \\implies x = -3\\) or \\(x = -5\\)."),

    # 27
    ("Solve: \\(x^2 - 4x - 5 = 0\\).",
     ["\\(5\\) and \\(-1\\)", "\\(-5\\) and \\(1\\)", "\\(4\\) and \\(1\\)", "\\(-4\\) and \\(-1\\)"],
     "A", "OSC", "easy",
     "\\((x - 2)^2 = 5 + 4 = 9 \\implies x - 2 = \\pm 3 \\implies x = 5\\) or \\(x = -1\\)."),

    # 28
    ("Solve: \\(x^2 + 2x - 8 = 0\\).",
     ["\\(2\\) and \\(-4\\)", "\\(-2\\) and \\(4\\)", "\\(8\\) and \\(-1\\)", "\\(-8\\) and \\(1\\)"],
     "A", "OSC", "easy",
     "\\((x + 1)^2 = 8 + 1 = 9 \\implies x + 1 = \\pm 3 \\implies x = 2\\) or \\(x = -4\\)."),

    # 29
    ("Solve: \\(x^2 - 2x - 8 = 0\\).",
     ["\\(4\\) and \\(-2\\)", "\\(-4\\) and \\(2\\)", "\\(8\\) and \\(-1\\)", "\\(-8\\) and \\(1\\)"],
     "A", "OSC", "easy",
     "\\((x - 1)^2 = 8 + 1 = 9 \\implies x - 1 = \\pm 3 \\implies x = 4\\) or \\(x = -2\\)."),

    # 30
    ("If \\((x - 3)^2 = 0\\), what are the roots?",
     ["\\(3\\) (repeated root)", "\\(-3\\)", "\\(9\\)", "\\(\\pm 3\\)"],
     "A", "OSC", "easy",
     "\\(x - 3 = 0 \\implies x = 3\\)."),

    # 31
    ("If \\((x + 5)^2 = 0\\), what are the roots?",
     ["\\(-5\\) (repeated root)", "\\(5\\)", "\\(25\\)", "\\(\\pm 5\\)"],
     "A", "OSC", "easy",
     "\\(x + 5 = 0 \\implies x = -5\\)."),

    # 32
    ("Solve: \\(x^2 - 6x = 0\\) by completing the square.",
     ["\\(6\\) and \\(0\\)", "\\(3\\) and \\(-3\\)", "\\(6\\) only", "\\(0\\) only"],
     "A", "OSC", "easy",
     "\\(x^2 - 6x + 9 = 9 \\implies (x - 3)^2 = 9 \\implies x - 3 = \\pm 3 \\implies x = 6\\) or \\(x = 0\\)."),

    # 33
    ("Solve: \\(x^2 + 10x = 0\\) by completing the square.",
     ["\\(0\\) and \\(-10\\)", "\\(0\\) and \\(10\\)", "\\(-5\\) and \\(5\\)", "\\(-10\\) only"],
     "A", "OSC", "easy",
     "\\((x + 5)^2 = 25 \\implies x + 5 = \\pm 5 \\implies x = 0\\) or \\(x = -10\\)."),

    # 34
    ("What third term is needed for \\(x^2 + 14x\\)?",
     ["49", "7", "196", "28"],
     "A", "OSC", "easy",
     "\\((14/2)^2 = 7^2 = 49\\)."),

    # 35
    ("What third term is needed for \\(x^2 - 16x\\)?",
     ["64", "-64", "256", "16"],
     "A", "OSC", "easy",
     "\\((-8)^2 = 64\\)."),

    # 36
    ("What third term is needed for \\(x^2 + 18x\\)?",
     ["81", "9", "324", "18"],
     "A", "OSC", "easy",
     "\\(9^2 = 81\\)."),

    # 37
    ("What third term is needed for \\(x^2 - 20x\\)?",
     ["100", "-100", "400", "20"],
     "A", "OSC", "easy",
     "\\((-10)^2 = 100\\)."),

    # 38
    ("Solve: \\(x^2 - 4x + 2 = 0\\).",
     ["\\(2 \\pm \\sqrt{2}\\)", "\\(-2 \\pm \\sqrt{2}\\)", "\\(2 \\pm 2\\)", "\\(4 \\pm \\sqrt{2}\\)"],
     "A", "OSC", "medium",
     "\\((x - 2)^2 = -2 + 4 = 2 \\implies x = 2 \\pm \\sqrt{2}\\)."),

    # 39
    ("Solve: \\(x^2 - 6x + 6 = 0\\).",
     ["\\(3 \\pm \\sqrt{3}\\)", "\\(-3 \\pm \\sqrt{3}\\)", "\\(3 \\pm 3\\)", "\\(6 \\pm \\sqrt{3}\\)"],
     "A", "OSC", "medium",
     "\\((x - 3)^2 = -6 + 9 = 3 \\implies x = 3 \\pm \\sqrt{3}\\)."),

    # 40
    ("Solve: \\(x^2 - 8x + 13 = 0\\).",
     ["\\(4 \\pm \\sqrt{3}\\)", "\\(-4 \\pm \\sqrt{3}\\)", "\\(4 \\pm 3\\)", "\\(8 \\pm \\sqrt{3}\\)"],
     "A", "OSC", "medium",
     "\\((x - 4)^2 = -13 + 16 = 3 \\implies x = 4 \\pm \\sqrt{3}\\).")
]

t23_prac = [
    # 41
    ("Find third term for \\(x^2 + 12x\\).", ["36", "6", "144", "24"], "A", "OSC", "easy", "\\(6^2 = 36\\)."),
    # 42
    ("Find third term for \\(x^2 - 14x\\).", ["49", "7", "196", "28"], "A", "OSC", "easy", "\\((-7)^2 = 49\\)."),
    # 43
    ("Solve: \\(x^2 - 10x + 9 = 0\\).", ["\\(9\\) and \\(1\\)", "\\(-9\\) and \\(-1\\)", "\\(10\\) and \\(1\\)", "\\(-10\\) and \\(-1\\)"], "A", "OSC", "easy", "\\((x - 5)^2 = 16 \\implies x = 9, 1\\)."),
    # 44
    ("Solve: \\(x^2 + 10x + 9 = 0\\).", ["\\(-1\\) and \\(-9\\)", "\\(1\\) and \\(9\\)", "\\(-10\\) and \\(-1\\)", "\\(10\\) and \\(1\\)"], "A", "OSC", "easy", "\\((x + 5)^2 = 16 \\implies x = -1, -9\\)."),
    # 45
    ("Solve: \\(x^2 - 2x - 15 = 0\\).", ["\\(5\\) and \\(-3\\)", "\\(-5\\) and \\(3\\)", "\\(15\\) and \\(-1\\)", "\\(-15\\) and \\(1\\)"], "A", "OSC", "easy", "\\((x - 1)^2 = 16 \\implies x = 5, -3\\)."),
    # 46
    ("Solve: \\(x^2 + 2x - 15 = 0\\).", ["\\(-5\\) and \\(3\\)", "\\(5\\) and \\(-3\\)", "\\(-15\\) and \\(1\\)", "\\(15\\) and \\(-1\\)"], "A", "OSC", "easy", "\\((x + 1)^2 = 16 \\implies x = -5, 3\\)."),
    # 47
    ("Solve: \\(x^2 - 4x - 12 = 0\\).", ["\\(6\\) and \\(-2\\)", "\\(-6\\) and \\(2\\)", "\\(4\\) and \\(-3\\)", "\\(-4\\) and \\(3\\)"], "A", "OSC", "easy", "\\((x - 2)^2 = 16 \\implies x = 6, -2\\)."),
    # 48
    ("Solve: \\(x^2 + 4x - 12 = 0\\).", ["\\(-6\\) and \\(2\\)", "\\(6\\) and \\(-2\\)", "\\(-4\\) and \\(3\\)", "\\(4\\) and \\(-3\\)"], "A", "OSC", "easy", "\\((x + 2)^2 = 16 \\implies x = -6, 2\\)."),
    # 49
    ("Solve: \\(x^2 - 6x - 16 = 0\\).", ["\\(8\\) and \\(-2\\)", "\\(-8\\) and \\(2\\)", "\\(6\\) and \\(-2\\)", "\\(-6\\) and \\(2\\)"], "A", "OSC", "easy", "\\((x - 3)^2 = 25 \\implies x = 8, -2\\)."),
    # 50
    ("Solve: \\(x^2 + 6x - 16 = 0\\).", ["\\(-8\\) and \\(2\\)", "\\(8\\) and \\(-2\\)", "\\(-6\\) and \\(2\\)", "\\(6\\) and \\(-2\\)"], "A", "OSC", "easy", "\\((x + 3)^2 = 25 \\implies x = -8, 2\\)."),
    # 51
    ("Find third term for \\(x^2 + 7x\\).", ["\\(\\frac{49}{4}\\)", "\\(\\frac{7}{2}\\)", "49", "7"], "A", "OSC", "easy", "\\((7/2)^2 = 49/4\\)."),
    # 52
    ("Find third term for \\(x^2 - 9x\\).", ["\\(\\frac{81}{4}\\)", "\\(\\frac{9}{2}\\)", "81", "9"], "A", "OSC", "easy", "\\((-9/2)^2 = 81/4\\)."),
    # 53
    ("Find third term for \\(x^2 + 11x\\).", ["\\(\\frac{121}{4}\\)", "\\(\\frac{11}{2}\\)", "121", "11"], "A", "OSC", "easy", "\\((11/2)^2 = 121/4\\)."),
    # 54
    ("Find third term for \\(x^2 - 13x\\).", ["\\(\\frac{169}{4}\\)", "\\(\\frac{13}{2}\\)", "169", "13"], "A", "OSC", "easy", "\\((-13/2)^2 = 169/4\\)."),
    # 55
    ("Solve: \\(x^2 - 2x - 24 = 0\\).", ["\\(6\\) and \\(-4\\)", "\\(-6\\) and \\(4\\)", "\\(12\\) and \\(-2\\)", "\\(-12\\) and \\(2\\)"], "A", "OSC", "easy", "\\((x - 1)^2 = 25 \\implies x = 6, -4\\)."),
    # 56
    ("Solve: \\(x^2 + 2x - 24 = 0\\).", ["\\(-6\\) and \\(4\\)", "\\(6\\) and \\(-4\\)", "\\(-12\\) and \\(2\\)", "\\(12\\) and \\(-2\\)"], "A", "OSC", "easy", "\\((x + 1)^2 = 25 \\implies x = -6, 4\\)."),
    # 57
    ("Solve: \\(x^2 - 4x - 21 = 0\\).", ["\\(7\\) and \\(-3\\)", "\\(-7\\) and \\(3\\)", "\\(21\\) and \\(-1\\)", "\\(-21\\) and \\(1\\)"], "A", "OSC", "easy", "\\((x - 2)^2 = 25 \\implies x = 7, -3\\)."),
    # 58
    ("Solve: \\(x^2 + 4x - 21 = 0\\).", ["\\(-7\\) and \\(3\\)", "\\(7\\) and \\(-3\\)", "\\(-21\\) and \\(1\\)", "\\(21\\) and \\(-1\\)"], "A", "OSC", "easy", "\\((x + 2)^2 = 25 \\implies x = -7, 3\\)."),
    # 59
    ("Solve: \\(x^2 - 8x - 9 = 0\\).", ["\\(9\\) and \\(-1\\)", "\\(-9\\) and \\(1\\)", "\\(8\\) and \\(-1\\)", "\\(-8\\) and \\(1\\)"], "A", "OSC", "easy", "\\((x - 4)^2 = 25 \\implies x = 9, -1\\)."),
    # 60
    ("Solve: \\(x^2 + 8x - 9 = 0\\).", ["\\(-9\\) and \\(1\\)", "\\(9\\) and \\(-1\\)", "\\(-8\\) and \\(1\\)", "\\(8\\) and \\(-1\\)"], "A", "OSC", "easy", "\\((x + 4)^2 = 25 \\implies x = -9, 1\\)."),
    # 61
    ("Solve: \\(x^2 - 10x - 24 = 0\\).", ["\\(12\\) and \\(-2\\)", "\\(-12\\) and \\(2\\)", "\\(6\\) and \\(-4\\)", "\\(-6\\) and \\(4\\)"], "A", "OSC", "easy", "\\((x - 5)^2 = 49 \\implies x = 12, -2\\)."),
    # 62
    ("Solve: \\(x^2 + 10x - 24 = 0\\).", ["\\(-12\\) and \\(2\\)", "\\(12\\) and \\(-2\\)", "\\(-6\\) and \\(4\\)", "\\(6\\) and \\(-4\\)"], "A", "OSC", "easy", "\\((x + 5)^2 = 49 \\implies x = -12, 2\\)."),
    # 63
    ("Solve: \\(x^2 - 6x - 27 = 0\\).", ["\\(9\\) and \\(-3\\)", "\\(-9\\) and \\(3\\)", "\\(6\\) and \\(-3\\)", "\\(-6\\) and \\(3\\)"], "A", "OSC", "easy", "\\((x - 3)^2 = 36 \\implies x = 9, -3\\)."),
    # 64
    ("Solve: \\(x^2 + 6x - 27 = 0\\).", ["\\(-9\\) and \\(3\\)", "\\(9\\) and \\(-3\\)", "\\(-6\\) and \\(3\\)", "\\(6\\) and \\(-3\\)"], "A", "OSC", "easy", "\\((x + 3)^2 = 36 \\implies x = -9, 3\\)."),
    # 65
    ("Solve: \\(x^2 - 12x + 11 = 0\\).", ["\\(11\\) and \\(1\\)", "\\(-11\\) and \\(-1\\)", "\\(12\\) and \\(1\\)", "\\(-12\\) and \\(-1\\)"], "A", "OSC", "easy", "\\((x - 6)^2 = 25 \\implies x = 11, 1\\)."),
    # 66
    ("Solve: \\(x^2 + 12x + 11 = 0\\).", ["\\(-11\\) and \\(-1\\)", "\\(11\\) and \\(1\\)", "\\(-12\\) and \\(-1\\)", "\\(12\\) and \\(1\\)"], "A", "OSC", "easy", "\\((x + 6)^2 = 25 \\implies x = -11, -1\\)."),
    # 67
    ("Solve: \\(x^2 - 14x + 13 = 0\\).", ["\\(13\\) and \\(1\\)", "\\(-13\\) and \\(-1\\)", "\\(14\\) and \\(1\\)", "\\(-14\\) and \\(-1\\)"], "A", "OSC", "easy", "\\((x - 7)^2 = 36 \\implies x = 13, 1\\)."),
    # 68
    ("Solve: \\(x^2 + 14x + 13 = 0\\).", ["\\(-13\\) and \\(-1\\)", "\\(13\\) and \\(1\\)", "\\(-14\\) and \\(-1\\)", "\\(14\\) and \\(1\\)"], "A", "OSC", "easy", "\\((x + 7)^2 = 36 \\implies x = -13, -1\\)."),
    # 69
    ("Solve: \\(x^2 - 16x + 15 = 0\\).", ["\\(15\\) and \\(1\\)", "\\(-15\\) and \\(-1\\)", "\\(16\\) and \\(1\\)", "\\(-16\\) and \\(-1\\)"], "A", "OSC", "easy", "\\((x - 8)^2 = 49 \\implies x = 15, 1\\)."),
    # 70
    ("Solve: \\(x^2 + 16x + 15 = 0\\).", ["\\(-15\\) and \\(-1\\)", "\\(15\\) and \\(1\\)", "\\(-16\\) and \\(-1\\)", "\\(16\\) and \\(1\\)"], "A", "OSC", "easy", "\\((x + 8)^2 = 49 \\implies x = -15, -1\\).")
]

t23_mock = [
    # 71
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0f172a" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Completing the Square Identity</text>
  <text x="170" y="80" fill="#f8fafc" font-size="12" text-anchor="middle">x² + 2kx + k² = (x + k)²</text>
  <text x="170" y="105" fill="#4ade80" font-size="11" text-anchor="middle">Third Term = k² = [ (1/2) * coeff(x) ]²</text>
</svg>
</div>
What algebraic structure does the Completing the Square Method create on the LHS?""",
     ["A perfect square trinomial (x + k)²",
      "A difference of two cubes",
      "A linear expression",
      "A zero matrix"],
     "A", "OSC", "easy",
     "By adding \\((b/2)^2\\) to \\(x^2 + bx\\), the LHS is transformed into a perfect square trinomial \\((x + b/2)^2\\), allowing the roots to be found directly by taking square roots."),

    # 72
    ("Solve: \\((x - 2)^2 = 9\\). What are the roots?", ["\\(5\\) and \\(-1\\)", "\\(2\\) and \\(9\\)", "\\(3\\) and \\(-3\\)", "\\(7\\) and \\(-5\\)"], "A", "OSC", "easy", "\\(x - 2 = \\pm 3 \\implies x = 5\\) or \\(x = -1\\)."),
    # 73
    ("Solve: \\((x + 3)^2 = 16\\). What are the roots?", ["\\(1\\) and \\(-7\\)", "\\(-1\\) and \\(7\\)", "\\(4\\) and \\(-4\\)", "\\(3\\) and \\(16\\)"], "A", "OSC", "easy", "\\(x + 3 = \\pm 4 \\implies x = 1\\) or \\(x = -7\\)."),
    # 74
    ("Solve: \\((x - 5)^2 = 4\\). What are the roots?", ["\\(7\\) and \\(3\\)", "\\(-7\\) and \\(-3\\)", "\\(5\\) and \\(4\\)", "\\(9\\) and \\(1\\)"], "A", "OSC", "easy", "\\(x - 5 = \\pm 2 \\implies x = 7\\) or \\(x = 3\\)."),
    # 75
    ("Solve: \\((x + 1)^2 = 25\\). What are the roots?", ["\\(4\\) and \\(-6\\)", "\\(-4\\) and \\(6\\)", "\\(5\\) and \\(-5\\)", "\\(6\\) and \\(-4\\)"], "A", "OSC", "easy", "\\(x + 1 = \\pm 5 \\implies x = 4\\) or \\(x = -6\\)."),
    # 76
    ("Solve: \\((x - 4)^2 = 36\\). What are the roots?", ["\\(10\\) and \\(-2\\)", "\\(-10\\) and \\(2\\)", "\\(6\\) and \\(-6\\)", "\\(4\\) and \\(36\\)"], "A", "OSC", "easy", "\\(x - 4 = \\pm 6 \\implies x = 10\\) or \\(x = -2\\)."),
    # 77
    ("Solve: \\((x + 2)^2 = 49\\). What are the roots?", ["\\(5\\) and \\(-9\\)", "\\(-5\\) and \\(9\\)", "\\(7\\) and \\(-7\\)", "\\(9\\) and \\(-5\\)"], "A", "OSC", "easy", "\\(x + 2 = \\pm 7 \\implies x = 5\\) or \\(x = -9\\)."),
    # 78
    ("Solve: \\((x - 1)^2 = 64\\). What are the roots?", ["\\(9\\) and \\(-7\\)", "\\(-9\\) and \\(7\\)", "\\(8\\) and \\(-8\\)", "\\(1\\) and \\(64\\)"], "A", "OSC", "easy", "\\(x - 1 = \\pm 8 \\implies x = 9\\) or \\(x = -7\\)."),
    # 79
    ("Solve: \\((x + 6)^2 = 1\\). What are the roots?", ["\\(-5\\) and \\(-7\\)", "\\(5\\) and \\(7\\)", "\\(-1\\) and \\(1\\)", "\\(-6\\) only"], "A", "OSC", "easy", "\\(x + 6 = \\pm 1 \\implies x = -5\\) or \\(x = -7\\)."),
    # 80
    ("Solve: \\((x - 7)^2 = 0\\). What are the roots?", ["\\(7\\) (repeated root)", "\\(-7\\)", "\\(49\\)", "\\(0\\)"], "A", "OSC", "easy", "\\(x - 7 = 0 \\implies x = 7\\)."),
    # 81
    ("If \\((x - k)^2 = d\\) and \\(d < 0\\), what is the nature of the roots in real numbers?",
     ["No real roots (roots are complex/imaginary)", "Two distinct real roots", "Two equal real roots", "Zero"],
     "A", "OSC", "easy",
     "The square of any real number cannot be negative. If \\(d < 0\\), \\(\\sqrt{d}\\) is imaginary, meaning no real roots exist."),
    # 82
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0b132b" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1c2541" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Historical Note</text>
  <text x="170" y="80" fill="#f8fafc" font-size="11" text-anchor="middle">Completing the square is the exact method</text>
  <text x="170" y="105" fill="#4ade80" font-size="11" text-anchor="middle">used to derive the general Quadratic Formula!</text>
</svg>
</div>
How was the general quadratic formula \\(x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}\\) originally derived?""",
     ["By applying the Completing the Square Method to the general equation ax² + bx + c = 0",
      "By guessing roots using trial and error",
      "By calculating determinants of matrices",
      "By differentiating the quadratic function"],
     "A", "OSC", "easy",
     "The quadratic formula is derived directly by dividing \\(ax^2 + bx + c = 0\\) by \\(a\\), completing the square with \\((b/2a)^2\\), and isolating \\(x\\).")
]

all_q_23 = build_topic_questions("MH-10-MTH1-2-2.3", t23_exam, t23_prac, t23_mock)
out_23 = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch2_t3.json")
with open(out_23, "w", encoding="utf-8") as f:
    json.dump(all_q_23, f, indent=2, ensure_ascii=False)
print(f"Generated {len(all_q_23)} questions for MH-10-MTH1-2-2.3 -> {out_23}")
