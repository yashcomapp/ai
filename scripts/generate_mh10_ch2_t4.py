# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 2: Quadratic Equations (Topic 2.4: Formula Method)
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

TOPIC_CODE = "MH-10-MTH1-2-2.4"

# 40 EXAM (1-40)
exam_data = [
    # 1
    ("What is the general quadratic formula for the roots of \\(ax^2 + bx + c = 0\\)?",
     ["\\(x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}\\)",
      "\\(x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{a}\\)",
      "\\(x = \\frac{b \\pm \\sqrt{b^2 - 4ac}}{2a}\\)",
      "\\(x = \\frac{-b \\pm \\sqrt{b^2 + 4ac}}{2a}\\)"],
     "A", "OSC", "easy",
     "The quadratic formula discovered by ancient Indian mathematicians, notably Shreedharacharya, is \\(x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}\\)."),

    # 2
    ("Who was the ancient Indian mathematician who derived the quadratic formula?",
     ["Shreedharacharya", "Aryabhata", "Varahamihira", "Ramanujan"],
     "A", "OSC", "easy",
     "Shreedharacharya (circa 8th-9th century CE) gave the explicit algebraic rule to solve general quadratic equations by completing the square, known historically as Shreedharacharya's Rule."),

    # 3
    ("What is the quantity \\(b^2 - 4ac\\) called in quadratic equations?",
     ["Discriminant, denoted by the Greek letter \\(\\Delta\\) (delta)",
      "Determinant",
      "Derivative",
      "Differential"],
     "A", "OSC", "easy",
     "The expression \\(b^2 - 4ac\\) discriminates the nature of the roots of a quadratic equation and is called the discriminant, denoted by \\(\\Delta\\)."),

    # 4
    ("Solve by formula method: \\(x^2 + 6x + 5 = 0\\). What is the value of the discriminant \\(b^2 - 4ac\\)?",
     ["16", "20", "36", "4"],
     "A", "OSC", "easy",
     "Here \\(a = 1, b = 6, c = 5\\). \\(b^2 - 4ac = 6^2 - 4(1)(5) = 36 - 20 = 16\\)."),

    # 5
    ("Using \\(\\Delta = 16\\), find the roots of \\(x^2 + 6x + 5 = 0\\).",
     ["\\(-1\\) and \\(-5\\)", "\\(1\\) and \\(5\\)", "\\(-2\\) and \\(-3\\)", "\\(2\\) and \\(3\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{-6 \\pm \\sqrt{16}}{2(1)} = \\frac{-6 \\pm 4}{2}\\). Thus \\(x = \\frac{-6 + 4}{2} = -1\\) or \\(x = \\frac{-6 - 4}{2} = -5\\)."),

    # 6
    ("Solve by formula method: \\(x^2 - 3x - 2 = 0\\). What is the value of \\(b^2 - 4ac\\)?",
     ["17", "1", "9", "-1"],
     "A", "OSC", "easy",
     "Here \\(a = 1, b = -3, c = -2\\). \\(b^2 - 4ac = (-3)^2 - 4(1)(-2) = 9 + 8 = 17\\)."),

    # 7
    ("Using \\(\\Delta = 17\\), find the roots of \\(x^2 - 3x - 2 = 0\\).",
     ["\\(\\frac{3 \\pm \\sqrt{17}}{2}\\)",
      "\\(\\frac{-3 \\pm \\sqrt{17}}{2}\\)",
      "\\(3 \\pm \\sqrt{17}\\)",
      "\\(\\frac{3 \\pm 17}{2}\\)"],
     "A", "OSC", "medium",
     "\\(x = \\frac{-(-3) \\pm \\sqrt{17}}{2(1)} = \\frac{3 \\pm \\sqrt{17}}{2}\\)."),

    # 8
    ("Solve: \\(3m^2 + 2m - 7 = 0\\). What is the value of \\(b^2 - 4ac\\)?",
     ["88", "84", "80", "92"],
     "A", "OSC", "medium",
     "\\(a = 3, b = 2, c = -7\\). \\(b^2 - 4ac = 2^2 - 4(3)(-7) = 4 + 84 = 88\\)."),

    # 9
    ("From \\(\\Delta = 88\\), find the simplified roots of \\(3m^2 + 2m - 7 = 0\\).",
     ["\\(\\frac{-1 \\pm \\sqrt{22}}{3}\\)",
      "\\(\\frac{-2 \\pm \\sqrt{88}}{3}\\)",
      "\\(\\frac{1 \\pm \\sqrt{22}}{3}\\)",
      "\\(-1 \\pm \\sqrt{22}\\)"],
     "A", "OSC", "medium",
     "\\(\\sqrt{88} = \\sqrt{4 \\times 22} = 2\\sqrt{22}\\). \\(m = \\frac{-2 \\pm 2\\sqrt{22}}{2(3)} = \\frac{2(-1 \\pm \\sqrt{22})}{6} = \\frac{-1 \\pm \\sqrt{22}}{3}\\)."),

    # 10
    ("Solve: \\(5m^2 - 4m - 2 = 0\\). What is the value of \\(b^2 - 4ac\\)?",
     ["56", "24", "40", "16"],
     "A", "OSC", "medium",
     "\\(a = 5, b = -4, c = -2\\). \\(b^2 - 4ac = (-4)^2 - 4(5)(-2) = 16 + 40 = 56\\)."),

    # 11
    ("From \\(\\Delta = 56\\), find the simplified roots of \\(5m^2 - 4m - 2 = 0\\).",
     ["\\(\\frac{2 \\pm \\sqrt{14}}{5}\\)",
      "\\(\\frac{4 \\pm \\sqrt{56}}{5}\\)",
      "\\(\\frac{-2 \\pm \\sqrt{14}}{5}\\)",
      "\\(2 \\pm \\sqrt{14}\\)"],
     "A", "OSC", "medium",
     "\\(\\sqrt{56} = 2\\sqrt{14}\\). \\(m = \\frac{-(-4) \\pm 2\\sqrt{14}}{2(5)} = \\frac{4 \\pm 2\\sqrt{14}}{10} = \\frac{2 \\pm \\sqrt{14}}{5}\\)."),

    # 12
    ("Solve: \\(y^2 + \\frac{1}{3}y = 2\\). Clear fractions and find \\(a, b, c\\).",
     ["\\(3y^2 + y - 6 = 0\\); \\(a = 3, b = 1, c = -6\\)",
      "\\(y^2 + y - 6 = 0\\); \\(a = 1, b = 1, c = -6\\)",
      "\\(3y^2 + y + 6 = 0\\); \\(a = 3, b = 1, c = 6\\)",
      "\\(3y^2 - y - 6 = 0\\); \\(a = 3, b = -1, c = -6\\)"],
     "A", "OSC", "easy",
     "Multiply throughout by 3: \\(3y^2 + y = 6 \\implies 3y^2 + y - 6 = 0\\). Here \\(a = 3, b = 1, c = -6\\)."),

    # 13
    ("For \\(3y^2 + y - 6 = 0\\), what is \\(b^2 - 4ac\\)?",
     ["73", "72", "71", "-71"],
     "A", "OSC", "easy",
     "\\(b^2 - 4ac = 1^2 - 4(3)(-6) = 1 + 72 = 73\\)."),

    # 14
    ("From \\(\\Delta = 73\\), find the roots of \\(3y^2 + y - 6 = 0\\).",
     ["\\(\\frac{-1 \\pm \\sqrt{73}}{6}\\)",
      "\\(\\frac{1 \\pm \\sqrt{73}}{6}\\)",
      "\\(\\frac{-1 \\pm \\sqrt{73}}{3}\\)",
      "\\(-1 \\pm \\sqrt{73}\\)"],
     "A", "OSC", "medium",
     "\\(y = \\frac{-1 \\pm \\sqrt{73}}{2(3)} = \\frac{-1 \\pm \\sqrt{73}}{6}\\)."),

    # 15
    ("Solve: \\(5x^2 + 13x + 8 = 0\\). What is the value of \\(b^2 - 4ac\\)?",
     ["9", "16", "25", "1"],
     "A", "OSC", "medium",
     "\\(a = 5, b = 13, c = 8\\). \\(b^2 - 4ac = 13^2 - 4(5)(8) = 169 - 160 = 9\\)."),

    # 16
    ("From \\(\\Delta = 9\\), find the roots of \\(5x^2 + 13x + 8 = 0\\).",
     ["\\(-1\\) and \\(-\\frac{8}{5}\\)",
      "\\(1\\) and \\(\\frac{8}{5}\\)",
      "\\(-2\\) and \\(-4\\)",
      "\\(-1\\) and \\(-\\frac{5}{8}\\)"],
     "A", "OSC", "medium",
     "\\(x = \\frac{-13 \\pm \\sqrt{9}}{10} = \\frac{-13 \\pm 3}{10}\\). \\(x = \\frac{-10}{10} = -1\\) or \\(x = \\frac{-16}{10} = -\\frac{8}{5}\\)."),

    # 17
    ("Solve: \\(x^2 + 2\\sqrt{3}x + 3 = 0\\). What is the value of \\(b^2 - 4ac\\)?",
     ["0", "12", "6", "3"],
     "A", "OSC", "medium",
     "\\(a = 1, b = 2\\sqrt{3}, c = 3\\). \\(b^2 - 4ac = (2\\sqrt{3})^2 - 4(1)(3) = 12 - 12 = 0\\)."),

    # 18
    ("From \\(\\Delta = 0\\), find the roots of \\(x^2 + 2\\sqrt{3}x + 3 = 0\\).",
     ["\\(-\\sqrt{3}\\) (repeated root)",
      "\\(\\sqrt{3}\\) (repeated root)",
      "\\(3\\) and \\(-3\\)",
      "\\(0\\) and \\(\\sqrt{3}\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{-2\\sqrt{3} \\pm 0}{2} = -\\sqrt{3}\\)."),

    # 19
    ("Solve by formula method: \\(2x^2 + 5\\sqrt{3}x + 6 = 0\\). Find \\(b^2 - 4ac\\).",
     ["27", "75", "48", "3"],
     "A", "OSC", "medium",
     "\\(a = 2, b = 5\\sqrt{3}, c = 6\\). \\(b^2 - 4ac = (5\\sqrt{3})^2 - 4(2)(6) = (25 \\times 3) - 48 = 75 - 48 = 27\\)."),

    # 20
    ("From \\(\\Delta = 27\\), find the roots of \\(2x^2 + 5\\sqrt{3}x + 6 = 0\\).",
     ["\\(-\\frac{\\sqrt{3}}{2}\\) and \\(-2\\sqrt{3}\\)",
      "\\(\\frac{\\sqrt{3}}{2}\\) and \\(2\\sqrt{3}\\)",
      "\\(-\\sqrt{3}\\) and \\(-3\\)",
      "\\(-\\sqrt{3}\\) and \\(-2\\)"],
     "A", "OSC", "hard",
     "\\(\\sqrt{27} = 3\\sqrt{3}\\). \\(x = \\frac{-5\\sqrt{3} \\pm 3\\sqrt{3}}{4}\\). \\(x_1 = \\frac{-2\\sqrt{3}}{4} = -\\frac{\\sqrt{3}}{2}\\) and \\(x_2 = \\frac{-8\\sqrt{3}}{4} = -2\\sqrt{3}\\)."),

    # 21
    ("Find \\(b^2 - 4ac\\) for \\(x^2 + x + 1 = 0\\).",
     ["-3", "3", "5", "-5"],
     "A", "OSC", "easy",
     "\\(1^2 - 4(1)(1) = 1 - 4 = -3\\)."),

    # 22
    ("Find \\(b^2 - 4ac\\) for \\(2x^2 - 4x + 3 = 0\\).",
     ["-8", "8", "-10", "10"],
     "A", "OSC", "easy",
     "\\((-4)^2 - 4(2)(3) = 16 - 24 = -8\\)."),

    # 23
    ("Solve: \\(x^2 - 4x + 1 = 0\\). What are the roots?",
     ["\\(2 \\pm \\sqrt{3}\\)", "\\(-2 \\pm \\sqrt{3}\\)", "\\(2 \\pm 3\\)", "\\(4 \\pm \\sqrt{3}\\)"],
     "A", "OSC", "medium",
     "\\(\\Delta = 16 - 4 = 12\\). \\(\\sqrt{12} = 2\\sqrt{3}\\). \\(x = \\frac{4 \\pm 2\\sqrt{3}}{2} = 2 \\pm \\sqrt{3}\\)."),

    # 24
    ("Solve: \\(x^2 - 6x + 4 = 0\\).",
     ["\\(3 \\pm \\sqrt{5}\\)", "\\(-3 \\pm \\sqrt{5}\\)", "\\(3 \\pm 5\\)", "\\(6 \\pm \\sqrt{5}\\)"],
     "A", "OSC", "medium",
     "\\(\\Delta = 36 - 16 = 20\\). \\(\\sqrt{20} = 2\\sqrt{5}\\). \\(x = \\frac{6 \\pm 2\\sqrt{5}}{2} = 3 \\pm \\sqrt{5}\\)."),

    # 25
    ("Solve: \\(x^2 - 8x + 6 = 0\\).",
     ["\\(4 \\pm \\sqrt{10}\\)", "\\(-4 \\pm \\sqrt{10}\\)", "\\(4 \\pm 10\\)", "\\(8 \\pm \\sqrt{10}\\)"],
     "A", "OSC", "medium",
     "\\(\\Delta = 64 - 24 = 40\\). \\(\\sqrt{40} = 2\\sqrt{10}\\). \\(x = \\frac{8 \\pm 2\\sqrt{10}}{2} = 4 \\pm \\sqrt{10}\\)."),

    # 26
    ("Solve: \\(x^2 - 2x - 1 = 0\\).",
     ["\\(1 \\pm \\sqrt{2}\\)", "\\(-1 \\pm \\sqrt{2}\\)", "\\(1 \\pm 2\\)", "\\(2 \\pm \\sqrt{2}\\)"],
     "A", "OSC", "easy",
     "\\(\\Delta = 4 - 4(1)(-1) = 8\\). \\(x = \\frac{2 \\pm 2\\sqrt{2}}{2} = 1 \\pm \\sqrt{2}\\)."),

    # 27
    ("Solve: \\(x^2 - 4x - 2 = 0\\).",
     ["\\(2 \\pm \\sqrt{6}\\)", "\\(-2 \\pm \\sqrt{6}\\)", "\\(2 \\pm 6\\)", "\\(4 \\pm \\sqrt{6}\\)"],
     "A", "OSC", "easy",
     "\\(\\Delta = 16 - 4(1)(-2) = 24\\). \\(x = \\frac{4 \\pm 2\\sqrt{6}}{2} = 2 \\pm \\sqrt{6}\\)."),

    # 28
    ("Solve: \\(x^2 - 6x - 1 = 0\\).",
     ["\\(3 \\pm \\sqrt{10}\\)", "\\(-3 \\pm \\sqrt{10}\\)", "\\(3 \\pm 10\\)", "\\(6 \\pm \\sqrt{10}\\)"],
     "A", "OSC", "easy",
     "\\(\\Delta = 36 + 4 = 40\\). \\(x = \\frac{6 \\pm 2\\sqrt{10}}{2} = 3 \\pm \\sqrt{10}\\)."),

    # 29
    ("Solve: \\(2x^2 + 3x - 2 = 0\\). Find \\(\\Delta\\).",
     ["25", "17", "-7", "9"],
     "A", "OSC", "easy",
     "\\(\\Delta = 9 - 4(2)(-2) = 9 + 16 = 25\\)."),

    # 30
    ("From \\(\\Delta = 25\\), find the roots of \\(2x^2 + 3x - 2 = 0\\).",
     ["\\(\\frac{1}{2}\\) and \\(-2\\)",
      "\\(-\\frac{1}{2}\\) and \\(2\\)",
      "\\(1\\) and \\(-2\\)",
      "\\(2\\) and \\(-1\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{-3 \\pm 5}{4} \\implies x = 2/4 = 1/2\\) or \\(x = -8/4 = -2\\)."),

    # 31
    ("Solve: \\(3x^2 - 5x + 1 = 0\\). Find \\(\\Delta\\).",
     ["13", "37", "-13", "25"],
     "A", "OSC", "easy",
     "\\(\\Delta = 25 - 4(3)(1) = 25 - 12 = 13\\)."),

    # 32
    ("From \\(\\Delta = 13\\), find the roots of \\(3x^2 - 5x + 1 = 0\\).",
     ["\\(\\frac{5 \\pm \\sqrt{13}}{6}\\)",
      "\\(\\frac{-5 \\pm \\sqrt{13}}{6}\\)",
      "\\(\\frac{5 \\pm \\sqrt{13}}{3}\\)",
      "\\(5 \\pm \\sqrt{13}\\)"],
     "A", "OSC", "medium",
     "\\(x = \\frac{5 \\pm \\sqrt{13}}{6}\\)."),

    # 33
    ("Solve: \\(4x^2 + 7x + 2 = 0\\). Find \\(\\Delta\\).",
     ["17", "33", "49", "-17"],
     "A", "OSC", "easy",
     "\\(\\Delta = 49 - 4(4)(2) = 49 - 32 = 17\\)."),

    # 34
    ("From \\(\\Delta = 17\\), find the roots of \\(4x^2 + 7x + 2 = 0\\).",
     ["\\(\\frac{-7 \\pm \\sqrt{17}}{8}\\)",
      "\\(\\frac{7 \\pm \\sqrt{17}}{8}\\)",
      "\\(\\frac{-7 \\pm \\sqrt{17}}{4}\\)",
      "\\(-7 \\pm \\sqrt{17}\\)"],
     "A", "OSC", "medium",
     "\\(x = \\frac{-7 \\pm \\sqrt{17}}{8}\\)."),

    # 35
    ("Solve: \\(x^2 - 2x - 4 = 0\\).",
     ["\\(1 \\pm \\sqrt{5}\\)", "\\(-1 \\pm \\sqrt{5}\\)", "\\(1 \\pm 5\\)", "\\(2 \\pm \\sqrt{5}\\)"],
     "A", "OSC", "easy",
     "\\(\\Delta = 4 - 4(1)(-4) = 20\\). \\(x = \\frac{2 \\pm 2\\sqrt{5}}{2} = 1 \\pm \\sqrt{5}\\)."),

    # 36
    ("Solve: \\(x^2 - 4x - 6 = 0\\).",
     ["\\(2 \\pm \\sqrt{10}\\)", "\\(-2 \\pm \\sqrt{10}\\)", "\\(2 \\pm 10\\)", "\\(4 \\pm \\sqrt{10}\\)"],
     "A", "OSC", "easy",
     "\\(\\Delta = 16 + 24 = 40\\). \\(x = \\frac{4 \\pm 2\\sqrt{10}}{2} = 2 \\pm \\sqrt{10}\\)."),

    # 37
    ("Solve: \\(x^2 - 6x - 2 = 0\\).",
     ["\\(3 \\pm \\sqrt{11}\\)", "\\(-3 \\pm \\sqrt{11}\\)", "\\(3 \\pm 11\\)", "\\(6 \\pm \\sqrt{11}\\)"],
     "A", "OSC", "easy",
     "\\(\\Delta = 36 + 8 = 44\\). \\(x = \\frac{6 \\pm 2\\sqrt{11}}{2} = 3 \\pm \\sqrt{11}\\)."),

    # 38
    ("Solve: \\(2x^2 - 6x + 3 = 0\\).",
     ["\\(\\frac{3 \\pm \\sqrt{3}}{2}\\)",
      "\\(\\frac{-3 \\pm \\sqrt{3}}{2}\\)",
      "\\(3 \\pm \\sqrt{3}\\)",
      "\\(\\frac{3 \\pm 3}{2}\\)"],
     "A", "OSC", "medium",
     "\\(\\Delta = 36 - 24 = 12\\). \\(x = \\frac{6 \\pm 2\\sqrt{3}}{4} = \\frac{3 \\pm \\sqrt{3}}{2}\\)."),

    # 39
    ("Solve: \\(3x^2 - 4x - 1 = 0\\).",
     ["\\(\\frac{2 \\pm \\sqrt{7}}{3}\\)",
      "\\(\\frac{-2 \\pm \\sqrt{7}}{3}\\)",
      "\\(\\frac{4 \\pm \\sqrt{7}}{3}\\)",
      "\\(2 \\pm \\sqrt{7}\\)"],
     "A", "OSC", "medium",
     "\\(\\Delta = 16 - 4(3)(-1) = 28\\). \\(x = \\frac{4 \\pm 2\\sqrt{7}}{6} = \\frac{2 \\pm \\sqrt{7}}{3}\\)."),

    # 40
    ("Why is the Formula Method considered the most powerful and universal method for solving quadratic equations?",
     ["Because it works unconditionally for all quadratic equations, whether roots are rational, irrational, or complex",
      "Because it never requires division",
      "Because it only works when a = 1",
      "Because it eliminates the need to calculate square roots"],
     "A", "OSC", "easy",
     "Unlike factorisation (which struggles with irrational or non-obvious roots), the formula directly provides the exact roots of ANY quadratic equation via direct algebraic substitution.")
]

t24_prac = [
    # 41
    ("Find \\(\\Delta\\) for \\(x^2 + 4x + 4 = 0\\).", ["0", "16", "8", "-16"], "A", "OSC", "easy", "\\(16 - 16 = 0\\)."),
    # 42
    ("Find \\(\\Delta\\) for \\(x^2 - 6x + 9 = 0\\).", ["0", "36", "18", "-36"], "A", "OSC", "easy", "\\(36 - 36 = 0\\)."),
    # 43
    ("Find \\(\\Delta\\) for \\(x^2 + 8x + 16 = 0\\).", ["0", "64", "32", "-64"], "A", "OSC", "easy", "\\(64 - 64 = 0\\)."),
    # 44
    ("Find \\(\\Delta\\) for \\(x^2 - 10x + 25 = 0\\).", ["0", "100", "50", "-100"], "A", "OSC", "easy", "\\(100 - 100 = 0\\)."),
    # 45
    ("Solve: \\(x^2 + 2x - 3 = 0\\) by formula. Find \\(\\Delta\\).", ["16", "12", "8", "4"], "A", "OSC", "easy", "\\(4 - 4(1)(-3) = 16\\)."),
    # 46
    ("From \\(\\Delta = 16\\), find roots of \\(x^2 + 2x - 3 = 0\\).", ["\\(1\\) and \\(-3\\)", "\\(-1\\) and \\(3\\)", "\\(2\\) and \\(-3\\)", "\\(-2\\) and \\(3\\)"], "A", "OSC", "easy", "\\((-2 \\pm 4)/2 = 1, -3\\)."),
    # 47
    ("Solve: \\(x^2 - 2x - 3 = 0\\). Find roots.", ["\\(3\\) and \\(-1\\)", "\\(-3\\) and \\(1\\)", "\\(2\\) and \\(-1\\)", "\\(-2\\) and \\(1\\)"], "A", "OSC", "easy", "\\((2 \\pm 4)/2 = 3, -1\\)."),
    # 48
    ("Solve: \\(x^2 + 4x - 5 = 0\\). Find roots.", ["\\(1\\) and \\(-5\\)", "\\(-1\\) and \\(5\\)", "\\(2\\) and \\(-5\\)", "\\(-2\\) and \\(5\\)"], "A", "OSC", "easy", "\\((-4 \\pm 6)/2 = 1, -5\\)."),
    # 49
    ("Solve: \\(x^2 - 4x - 5 = 0\\). Find roots.", ["\\(5\\) and \\(-1\\)", "\\(-5\\) and \\(1\\)", "\\(4\\) and \\(-1\\)", "\\(-4\\) and \\(1\\)"], "A", "OSC", "easy", "\\((4 \\pm 6)/2 = 5, -1\\)."),
    # 50
    ("Find \\(\\Delta\\) for \\(2x^2 + 5x + 2 = 0\\).", ["9", "25", "16", "1"], "A", "OSC", "easy", "\\(25 - 4(2)(2) = 25 - 16 = 9\\)."),
    # 51
    ("From \\(\\Delta = 9\\), find roots of \\(2x^2 + 5x + 2 = 0\\).", ["\\(-\\frac{1}{2}\\) and \\(-2\\)", "\\(\\frac{1}{2}\\) and \\(2\\)", "\\(-1\\) and \\(-4\\)", "\\(1\\) and \\(4\\)"], "A", "OSC", "easy", "\\((-5 \\pm 3)/4 = -1/2, -2\\)."),
    # 52
    ("Find \\(\\Delta\\) for \\(3x^2 - 7x + 2 = 0\\).", ["25", "49", "24", "1"], "A", "OSC", "easy", "\\(49 - 4(3)(2) = 49 - 24 = 25\\)."),
    # 53
    ("From \\(\\Delta = 25\\), find roots of \\(3x^2 - 7x + 2 = 0\\).", ["\\(2\\) and \\(\\frac{1}{3}\\)", "\\(-2\\) and \\(-\\frac{1}{3}\\)", "\\(3\\) and \\(2\\)", "\\(1\\) and \\(2\\)"], "A", "OSC", "easy", "\\((7 \\pm 5)/6 = 2, 1/3\\)."),
    # 54
    ("Find \\(\\Delta\\) for \\(2x^2 - x - 3 = 0\\).", ["25", "1", "24", "-23"], "A", "OSC", "easy", "\\(1 - 4(2)(-3) = 1 + 24 = 25\\)."),
    # 55
    ("From \\(\\Delta = 25\\), find roots of \\(2x^2 - x - 3 = 0\\).", ["\\(\\frac{3}{2}\\) and \\(-1\\)", "\\(-\\frac{3}{2}\\) and \\(1\\)", "\\(3\\) and \\(-2\\)", "\\(-3\\) and \\(2\\)"], "A", "OSC", "easy", "\\((1 \\pm 5)/4 = 3/2, -1\\)."),
    # 56
    ("Find \\(\\Delta\\) for \\(x^2 - 2x + 5 = 0\\).", ["-16", "16", "24", "-24"], "A", "OSC", "easy", "\\(4 - 20 = -16\\)."),
    # 57
    ("Find \\(\\Delta\\) for \\(x^2 + 4x + 5 = 0\\).", ["-4", "4", "36", "-36"], "A", "OSC", "easy", "\\(16 - 20 = -4\\)."),
    # 58
    ("Find \\(\\Delta\\) for \\(x^2 - 6x + 10 = 0\\).", ["-4", "4", "76", "-76"], "A", "OSC", "easy", "\\(36 - 40 = -4\\)."),
    # 59
    ("Find \\(\\Delta\\) for \\(2x^2 - 2x + 1 = 0\\).", ["-4", "4", "12", "-12"], "A", "OSC", "easy", "\\(4 - 4(2)(1) = -4\\)."),
    # 60
    ("Find \\(\\Delta\\) for \\(3x^2 - 4x + 2 = 0\\).", ["-8", "8", "40", "-40"], "A", "OSC", "easy", "\\(16 - 24 = -8\\)."),
    # 61
    ("Find \\(\\Delta\\) for \\(x^2 - 4x - 1 = 0\\).", ["20", "12", "16", "4"], "A", "OSC", "easy", "\\(16 + 4 = 20\\)."),
    # 62
    ("Find \\(\\Delta\\) for \\(x^2 - 6x - 2 = 0\\).", ["44", "28", "36", "8"], "A", "OSC", "easy", "\\(36 + 8 = 44\\)."),
    # 63
    ("Find \\(\\Delta\\) for \\(x^2 - 8x - 3 = 0\\).", ["76", "52", "64", "12"], "A", "OSC", "easy", "\\(64 + 12 = 76\\)."),
    # 64
    ("Find \\(\\Delta\\) for \\(2x^2 - 4x - 1 = 0\\).", ["24", "8", "16", "4"], "A", "OSC", "easy", "\\(16 + 8 = 24\\)."),
    # 65
    ("Find \\(\\Delta\\) for \\(3x^2 - 6x - 2 = 0\\).", ["60", "12", "36", "24"], "A", "OSC", "easy", "\\(36 + 24 = 60\\)."),
    # 66
    ("Solve: \\(x^2 - 5x + 1 = 0\\). What are the roots?", ["\\(\\frac{5 \\pm \\sqrt{21}}{2}\\)", "\\(\\frac{-5 \\pm \\sqrt{21}}{2}\\)", "\\(5 \\pm \\sqrt{21}\\)", "\\(\\frac{5 \\pm 21}{2}\\)"], "A", "OSC", "medium", "\\(\\Delta = 25 - 4 = 21\\). \\(x = \\frac{5 \\pm \\sqrt{21}}{2}\\)."),
    # 67
    ("Solve: \\(x^2 + 5x + 1 = 0\\). What are the roots?", ["\\(\\frac{-5 \\pm \\sqrt{21}}{2}\\)", "\\(\\frac{5 \\pm \\sqrt{21}}{2}\\)", "\\(-5 \\pm \\sqrt{21}\\)", "\\(\\frac{-5 \\pm 21}{2}\\)"], "A", "OSC", "medium", "\\(x = \\frac{-5 \\pm \\sqrt{21}}{2}\\)."),
    # 68
    ("Solve: \\(x^2 - 7x + 2 = 0\\). What are the roots?", ["\\(\\frac{7 \\pm \\sqrt{41}}{2}\\)", "\\(\\frac{-7 \\pm \\sqrt{41}}{2}\\)", "\\(7 \\pm \\sqrt{41}\\)", "\\(\\frac{7 \\pm 41}{2}\\)"], "A", "OSC", "medium", "\\(\\Delta = 49 - 8 = 41\\). \\(x = \\frac{7 \\pm \\sqrt{41}}{2}\\)."),
    # 69
    ("Solve: \\(x^2 + 7x + 2 = 0\\). What are the roots?", ["\\(\\frac{-7 \\pm \\sqrt{41}}{2}\\)", "\\(\\frac{7 \\pm \\sqrt{41}}{2}\\)", "\\(-7 \\pm \\sqrt{41}\\)", "\\(\\frac{-7 \\pm 41}{2}\\)"], "A", "OSC", "medium", "\\(x = \\frac{-7 \\pm \\sqrt{41}}{2}\\)."),
    # 70
    ("Solve: \\(x^2 - 9x + 3 = 0\\). What are the roots?", ["\\(\\frac{9 \\pm \\sqrt{69}}{2}\\)", "\\(\\frac{-9 \\pm \\sqrt{69}}{2}\\)", "\\(9 \\pm \\sqrt{69}\\)", "\\(\\frac{9 \\pm 69}{2}\\)"], "A", "OSC", "medium", "\\(\\Delta = 81 - 12 = 69\\). \\(x = \\frac{9 \\pm \\sqrt{69}}{2}\\).")
]

t24_mock = [
    # 71
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0f172a" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Quadratic Formula Workflow</text>
  <text x="170" y="80" fill="#f8fafc" font-size="11" text-anchor="middle">Step 1: Identify a, b, c -> Step 2: Calculate Δ = b² - 4ac</text>
  <text x="170" y="105" fill="#4ade80" font-size="11" text-anchor="middle">Step 3: Evaluate x = [ -b ± √Δ ] / (2a)</text>
</svg>
</div>
What is the first mandatory step before applying the quadratic formula?""",
     ["Write the equation in standard form ax² + bx + c = 0 and accurately extract coefficients a, b, and c",
      "Multiply all terms by the constant c",
      "Guess the first root",
      "Draw the graph of the equation"],
     "A", "OSC", "easy",
     "Before computing the discriminant or using the formula, the equation must be aligned in standard form \\(ax^2 + bx + c = 0\\) with signs correctly identified for \\(a, b, c\\)."),

    # 72
    ("If \\(b^2 - 4ac = 0\\), the formula simplifies to:", ["\\(x = -\\frac{b}{2a}\\)", "\\(x = 0\\)", "\\(x = \\frac{b}{2a}\\)", "\\(x = -b\\)"], "A", "OSC", "easy", "When \\(\\Delta = 0\\), \\(\\sqrt{\\Delta} = 0\\), leaving \\(x = -\\frac{b}{2a}\\)."),
    # 73
    ("Solve: \\(x^2 - 2x + 1 = 0\\) using formula.", ["\\(1\\) (repeated root)", "\\(-1\\)", "\\(2\\)", "\\(0\\)"], "A", "OSC", "easy", "\\(x = -(-2)/(2) = 1\\)."),
    # 74
    ("Solve: \\(x^2 + 4x + 4 = 0\\) using formula.", ["\\(-2\\) (repeated root)", "\\(2\\)", "\\(4\\)", "\\(-4\\)"], "A", "OSC", "easy", "\\(x = -4/2 = -2\\)."),
    # 75
    ("Solve: \\(x^2 - 6x + 9 = 0\\) using formula.", ["\\(3\\) (repeated root)", "\\(-3\\)", "\\(9\\)", "\\(6\\)"], "A", "OSC", "easy", "\\(x = 6/2 = 3\\)."),
    # 76
    ("Solve: \\(x^2 + 8x + 16 = 0\\) using formula.", ["\\(-4\\) (repeated root)", "\\(4\\)", "\\(8\\)", "\\(-8\\)"], "A", "OSC", "easy", "\\(x = -8/2 = -4\\)."),
    # 77
    ("Solve: \\(x^2 - 10x + 25 = 0\\) using formula.", ["\\(5\\) (repeated root)", "\\(-5\\)", "\\(10\\)", "\\(-10\\)"], "A", "OSC", "easy", "\\(x = 10/2 = 5\\)."),
    # 78
    ("Solve: \\(4x^2 - 4x + 1 = 0\\) using formula.", ["\\(\\frac{1}{2}\\) (repeated root)", "\\(-\\frac{1}{2}\\)", "\\(1\\)", "\\(2\\)"], "A", "OSC", "easy", "\\(x = 4/8 = 1/2\\)."),
    # 79
    ("Solve: \\(9x^2 + 6x + 1 = 0\\) using formula.", ["\\(-\\frac{1}{3}\\) (repeated root)", "\\(\\frac{1}{3}\\)", "\\(-1\\)", "\\(3\\)"], "A", "OSC", "easy", "\\(x = -6/18 = -1/3\\)."),
    # 80
    ("Solve: \\(25x^2 - 10x + 1 = 0\\) using formula.", ["\\(\\frac{1}{5}\\) (repeated root)", "\\(-\\frac{1}{5}\\)", "\\(1\\)", "\\(5\\)"], "A", "OSC", "easy", "\\(x = 10/50 = 1/5\\)."),
    # 81
    ("If \\(b^2 - 4ac > 0\\), how many distinct real roots does the quadratic equation possess?",
     ["Exactly 2 distinct real roots", "Exactly 1 real root", "No real roots", "Infinitely many roots"],
     "A", "OSC", "easy",
     "When \\(\\Delta > 0\\), \\(\\sqrt{\\Delta}\\) is a positive real number, yielding two distinct real values: \\(\\frac{-b + \\sqrt{\\Delta}}{2a}\\) and \\(\\frac{-b - \\sqrt{\\Delta}}{2a}\\)."),
    # 82
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0b132b" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1c2541" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Formula Method Summary</text>
  <text x="170" y="80" fill="#f8fafc" font-size="11" text-anchor="middle">Formula: x = [ -b ± √(b² - 4ac) ] / (2a)</text>
  <text x="170" y="105" fill="#4ade80" font-size="11" text-anchor="middle">Universally applicable across all real polynomials</text>
</svg>
</div>
What is the primary benefit of calculating the discriminant \\(\\Delta = b^2 - 4ac\\) first before using the full formula?""",
     ["It reveals whether real roots exist without doing the full computation, preventing invalid square roots of negative numbers",
      "It eliminates the variable x",
      "It multiplies all coefficients by 2",
      "It converts the equation into a linear equation"],
     "A", "OSC", "easy",
     "Calculating \\(\\Delta\\) first acts as a diagnostic gate: if \\(\\Delta < 0\\), we immediately know that no real roots exist and avoid attempting to compute square roots of negative numbers in the real number system.")
]

all_q_24 = build_topic_questions(TOPIC_CODE, exam_data, t24_prac, t24_mock)
out_24 = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch2_t4.json")
with open(out_24, "w", encoding="utf-8") as f:
    json.dump(all_q_24, f, indent=2, ensure_ascii=False)
print(f"Generated {len(all_q_24)} questions for {TOPIC_CODE} -> {out_24}")
