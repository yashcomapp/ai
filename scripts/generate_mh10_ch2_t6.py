# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 2: Quadratic Equations (Topic 2.6: Relation Between Roots and Coefficients)
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

TOPIC_CODE = "MH-10-MTH1-2-2.6"

# 40 EXAM (1-40)
exam_data = [
    # 1
    ("If \\(\\alpha\\) and \\(\\beta\\) are the roots of the quadratic equation \\(ax^2 + bx + c = 0\\), what is the formula for their sum \\(\\alpha + \\beta\\)?",
     ["\\(-\\frac{b}{a}\\)", "\\(\\frac{b}{a}\\)", "\\(\\frac{c}{a}\\)", "\\(-\\frac{c}{a}\\)"],
     "A", "OSC", "easy",
     "From the quadratic formula \\(\\alpha = \\frac{-b + \\sqrt{\\Delta}}{2a}\\) and \\(\\beta = \\frac{-b - \\sqrt{\\Delta}}{2a}\\), adding gives \\(\\alpha + \\beta = \\frac{-2b}{2a} = -\\frac{b}{a}\\)."),

    # 2
    ("If \\(\\alpha\\) and \\(\\beta\\) are the roots of \\(ax^2 + bx + c = 0\\), what is the formula for their product \\(\\alpha \\beta\\)?",
     ["\\(\\frac{c}{a}\\)", "\\(-\\frac{c}{a}\\)", "\\(-\\frac{b}{a}\\)", "\\(\\frac{b}{a}\\)"],
     "A", "OSC", "easy",
     "Multiplying \\(\\alpha\\) and \\(\\beta\\): \\(\\alpha \\beta = \\frac{(-b)^2 - (\\Delta)}{4a^2} = \\frac{b^2 - (b^2 - 4ac)}{4a^2} = \\frac{4ac}{4a^2} = \\frac{c}{a}\\)."),

    # 3
    ("What is the general form of a quadratic equation whose roots are \\(\\alpha\\) and \\(\\beta\\)?",
     ["\\(x^2 - (\\alpha + \\beta)x + \\alpha \\beta = 0\\)",
      "\\(x^2 + (\\alpha + \\beta)x + \\alpha \\beta = 0\\)",
      "\\(x^2 - (\\alpha + \\beta)x - \\alpha \\beta = 0\\)",
      "\\(x^2 + (\\alpha - \\beta)x + \\alpha \\beta = 0\\)"],
     "A", "OSC", "easy",
     "Since \\((x - \\alpha)(x - \\beta) = 0\\), expanding gives \\(x^2 - \\alpha x - \\beta x + \\alpha \\beta = 0 \\implies x^2 - (\\alpha + \\beta)x + \\alpha \\beta = 0\\)."),

    # 4
    ("Form the quadratic equation whose roots are \\(0\\) and \\(4\\).",
     ["\\(x^2 - 4x = 0\\)", "\\(x^2 + 4x = 0\\)", "\\(x^2 - 16 = 0\\)", "\\(x^2 - 4 = 0\\)"],
     "A", "OSC", "easy",
     "Sum of roots = \\(0 + 4 = 4\\), product of roots = \\(0 \\times 4 = 0\\). Equation: \\(x^2 - 4x + 0 = 0 \\implies x^2 - 4x = 0\\)."),

    # 5
    ("Form the quadratic equation whose roots are \\(3\\) and \\(-10\\).",
     ["\\(x^2 + 7x - 30 = 0\\)", "\\(x^2 - 7x - 30 = 0\\)", "\\(x^2 + 7x + 30 = 0\\)", "\\(x^2 - 13x - 30 = 0\\)"],
     "A", "OSC", "easy",
     "Sum = \\(3 + (-10) = -7\\), product = \\(3(-10) = -30\\). Equation: \\(x^2 - (-7)x + (-30) = 0 \\implies x^2 + 7x - 30 = 0\\)."),

    # 6
    ("Form the quadratic equation whose roots are \\(\\frac{1}{2}\\) and \\(-\\frac{1}{2}\\).",
     ["\\(4x^2 - 1 = 0\\)", "\\(2x^2 - 1 = 0\\)", "\\(4x^2 + 1 = 0\\)", "\\(x^2 - 1 = 0\\)"],
     "A", "OSC", "easy",
     "Sum = \\(1/2 - 1/2 = 0\\), product = \\(-1/4\\). Equation: \\(x^2 - 0x - 1/4 = 0 \\implies 4x^2 - 1 = 0\\)."),

    # 7
    ("Form the quadratic equation whose roots are \\(2 - \\sqrt{5}\\) and \\(2 + \\sqrt{5}\\).",
     ["\\(x^2 - 4x - 1 = 0\\)", "\\(x^2 + 4x - 1 = 0\\)", "\\(x^2 - 4x + 1 = 0\\)", "\\(x^2 - 5x - 4 = 0\\)"],
     "A", "OSC", "medium",
     "Sum = \\((2 - \\sqrt{5}) + (2 + \\sqrt{5}) = 4\\). Product = \\((2 - \\sqrt{5})(2 + \\sqrt{5}) = 4 - 5 = -1\\). Equation: \\(x^2 - 4x - 1 = 0\\)."),

    # 8
    ("If \\(\\alpha\\) and \\(\\beta\\) are the roots of \\(y^2 - 2y - 7 = 0\\), find the value of \\(\\alpha^2 + \\beta^2\\).",
     ["18", "4", "25", "11"],
     "A", "OSC", "medium",
     "Here \\(\\alpha + \\beta = -(-2)/1 = 2\\) and \\(\\alpha \\beta = -7/1 = -7\\). Using identity \\(\\alpha^2 + \\beta^2 = (\\alpha + \\beta)^2 - 2\\alpha \\beta = 2^2 - 2(-7) = 4 + 14 = 18\\)."),

    # 9
    ("From the same equation \\(y^2 - 2y - 7 = 0\\), find the value of \\(\\alpha^3 + \\beta^3\\).",
     ["50", "34", "42", "-34"],
     "A", "OSC", "hard",
     "Identity: \\(\\alpha^3 + \\beta^3 = (\\alpha + \\beta)^3 - 3\\alpha \\beta(\\alpha + \\beta) = 2^3 - 3(-7)(2) = 8 + 42 = 50\\)."),

    # 10
    ("If the sum of the roots of the quadratic equation \\(x^2 - 4kx + k + 3 = 0\\) is double their product, find the value of \\(k\\).",
     ["3", "2", "4", "1"],
     "A", "OSC", "medium",
     "\\(a = 1, b = -4k, c = k + 3\\). Sum \\(\\alpha + \\beta = 4k\\), product \\(\\alpha \\beta = k + 3\\). Given: \\(4k = 2(k + 3) \\implies 4k = 2k + 6 \\implies 2k = 6 \\implies k = 3\\)."),

    # 11
    ("The roots of \\(x^2 - kx + 54 = 0\\) differ by 3. Find the positive value of \\(k\\).",
     ["15", "12", "18", "9"],
     "A", "OSC", "hard",
     "Given \\(\\alpha - \\beta = 3\\). \\(\\alpha + \\beta = k, \\alpha \\beta = 54\\). Identity: \\((\\alpha - \\beta)^2 = (\\alpha + \\beta)^2 - 4\\alpha \\beta \\implies 3^2 = k^2 - 4(54) \\implies 9 = k^2 - 216 \\implies k^2 = 225 \\implies k = 15\\)."),

    # 12
    ("If one root of \\(kx^2 - 14x - 5 = 0\\) is 6 times the other, what is the ratio of the roots?",
     ["\\(6:1\\)", "\\(1:6\\)", "\\(7:1\\)", "\\(5:1\\)"],
     "A", "OSC", "easy",
     "By definition, if \\(\\alpha = 6\\beta\\), the ratio \\(\\alpha / \\beta = 6/1 = 6:1\\)."),

    # 13
    ("Find the sum and product of the roots of \\(2x^2 - 4x + 3 = 0\\).",
     ["Sum = 2, Product = 1.5",
      "Sum = -2, Product = 1.5",
      "Sum = 4, Product = 3",
      "Sum = -4, Product = -3"],
     "A", "OSC", "easy",
     "Sum = \\(-(-4)/2 = 2\\). Product = \\(3/2 = 1.5\\)."),

    # 14
    ("Find the sum and product of the roots of \\(3x^2 + 5x - 2 = 0\\).",
     ["Sum = -5/3, Product = -2/3",
      "Sum = 5/3, Product = 2/3",
      "Sum = -5/3, Product = 2/3",
      "Sum = 5, Product = -2"],
     "A", "OSC", "easy",
     "Sum = \\(-5/3\\). Product = \\(-2/3\\)."),

    # 15
    ("What is the value of \\(\\frac{1}{\\alpha} + \\frac{1}{\\beta}\\) in terms of coefficients for \\(ax^2 + bx + c = 0\\)?",
     ["\\(-\\frac{b}{c}\\)", "\\(\\frac{b}{c}\\)", "\\(-\\frac{c}{b}\\)", "\\(\\frac{a}{c}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{1}{\\alpha} + \\frac{1}{\\beta} = \\frac{\\alpha + \\beta}{\\alpha \\beta} = \\frac{-b/a}{c/a} = -\\frac{b}{c}\\)."),

    # 16
    ("For \\(2x^2 - 6x + 5 = 0\\), find the value of \\(\\frac{1}{\\alpha} + \\frac{1}{\\beta}\\).",
     ["\\(\\frac{6}{5}\\)", "\\(-\\frac{6}{5}\\)", "\\(\\frac{5}{6}\\)", "\\(3\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{1}{\\alpha} + \\frac{1}{\\beta} = -\\frac{b}{c} = -\\frac{-6}{5} = \\frac{6}{5}\\)."),

    # 17
    ("For \\(3x^2 + 7x + 2 = 0\\), find \\(\\frac{1}{\\alpha} + \\frac{1}{\\beta}\\).",
     ["\\(-\\frac{7}{2}\\)", "\\(\\frac{7}{2}\\)", "\\(-\\frac{2}{7}\\)", "\\(-\\frac{7}{3}\\)"],
     "A", "OSC", "easy",
     "\\(-\\frac{b}{c} = -\\frac{7}{2}\\)."),

    # 18
    ("If the roots of \\(x^2 - px + q = 0\\) are \\(2\\) and \\(3\\), find \\(p\\) and \\(q\\).",
     ["\\(p = 5, q = 6\\)", "\\(p = -5, q = 6\\)", "\\(p = 6, q = 5\\)", "\\(p = 1, q = 6\\)"],
     "A", "OSC", "easy",
     "\\(p = \\alpha + \\beta = 2 + 3 = 5\\), and \\(q = \\alpha \\beta = 2 \\times 3 = 6\\)."),

    # 19
    ("If the roots of \\(x^2 - px + q = 0\\) are \\(-4\\) and \\(5\\), find \\(p\\) and \\(q\\).",
     ["\\(p = 1, q = -20\\)", "\\(p = -1, q = -20\\)", "\\(p = 9, q = -20\\)", "\\(p = 1, q = 20\\)"],
     "A", "OSC", "easy",
     "\\(p = -4 + 5 = 1\\), and \\(q = (-4)(5) = -20\\)."),

    # 20
    ("If the roots of \\(ax^2 + bx + c = 0\\) are reciprocals of each other (\\(\\alpha = 1/\\beta\\)), what is the relation between coefficients?",
     ["\\(a = c\\)", "\\(a = -c\\)", "\\(b = 0\\)", "\\(b^2 = 4ac\\)"],
     "A", "OSC", "easy",
     "If roots are reciprocals, their product is 1: \\(\\alpha \\beta = 1 \\implies \\frac{c}{a} = 1 \\implies c = a\\)."),

    # 21
    ("If the roots of \\(ax^2 + bx + c = 0\\) are equal in magnitude but opposite in sign (\\(\\alpha = -\\beta\\)), what must be true?",
     ["\\(b = 0\\)", "\\(a = c\\)", "\\(c = 0\\)", "\\(a = 0\\)"],
     "A", "OSC", "easy",
     "If \\(\\alpha = -\\beta\\), their sum is 0: \\(\\alpha + \\beta = 0 \\implies -\\frac{b}{a} = 0 \\implies b = 0\\)."),

    # 22
    ("Form the quadratic equation whose roots are \\(5\\) and \\(5\\) (equal roots).",
     ["\\(x^2 - 10x + 25 = 0\\)", "\\(x^2 + 10x + 25 = 0\\)", "\\(x^2 - 25 = 0\\)", "\\(x^2 - 5x + 25 = 0\\)"],
     "A", "OSC", "easy",
     "Sum = 10, product = 25. \\(x^2 - 10x + 25 = 0\\)."),

    # 23
    ("Form the quadratic equation whose roots are \\(-3\\) and \\(-3\\).",
     ["\\(x^2 + 6x + 9 = 0\\)", "\\(x^2 - 6x + 9 = 0\\)", "\\(x^2 - 9 = 0\\)", "\\(x^2 + 9x + 6 = 0\\)"],
     "A", "OSC", "easy",
     "Sum = \\(-6\\), product = 9. \\(x^2 - (-6)x + 9 = 0 \\implies x^2 + 6x + 9 = 0\\)."),

    # 24
    ("Form the quadratic equation whose roots are \\(1 + \\sqrt{3}\\) and \\(1 - \\sqrt{3}\\).",
     ["\\(x^2 - 2x - 2 = 0\\)", "\\(x^2 + 2x - 2 = 0\\)", "\\(x^2 - 2x + 2 = 0\\)", "\\(x^2 - 4x - 2 = 0\\)"],
     "A", "OSC", "medium",
     "Sum = 2. Product = \\(1 - 3 = -2\\). Equation: \\(x^2 - 2x - 2 = 0\\)."),

    # 25
    ("Form the quadratic equation whose roots are \\(3 + \\sqrt{2}\\) and \\(3 - \\sqrt{2}\\).",
     ["\\(x^2 - 6x + 7 = 0\\)", "\\(x^2 + 6x + 7 = 0\\)", "\\(x^2 - 6x - 7 = 0\\)", "\\(x^2 - 3x + 7 = 0\\)"],
     "A", "OSC", "medium",
     "Sum = 6. Product = \\(9 - 2 = 7\\). Equation: \\(x^2 - 6x + 7 = 0\\)."),

    # 26
    ("Form the quadratic equation whose roots are \\(5 + 2\\sqrt{6}\\) and \\(5 - 2\\sqrt{6}\\).",
     ["\\(x^2 - 10x + 1 = 0\\)", "\\(x^2 + 10x + 1 = 0\\)", "\\(x^2 - 10x - 1 = 0\\)", "\\(x^2 - 5x + 1 = 0\\)"],
     "A", "OSC", "medium",
     "Sum = 10. Product = \\(25 - (4 \\times 6) = 25 - 24 = 1\\). Equation: \\(x^2 - 10x + 1 = 0\\)."),

    # 27
    ("If \\(\\alpha, \\beta\\) are roots of \\(x^2 - 5x + 4 = 0\\), find \\(\\alpha^2 \\beta + \\alpha \\beta^2\\).",
     ["20", "25", "16", "9"],
     "A", "OSC", "medium",
     "\\(\\alpha^2 \\beta + \\alpha \\beta^2 = \\alpha \\beta(\\alpha + \\beta)\\). Here \\(\\alpha + \\beta = 5, \\alpha \\beta = 4\\). Product = \\(4 \\times 5 = 20\\)."),

    # 28
    ("If \\(\\alpha, \\beta\\) are roots of \\(x^2 - 7x + 10 = 0\\), find \\(\\alpha^2 \\beta + \\alpha \\beta^2\\).",
     ["70", "49", "100", "17"],
     "A", "OSC", "medium",
     "\\(\\alpha \\beta(\\alpha + \\beta) = 10 \\times 7 = 70\\)."),

    # 29
    ("If \\(\\alpha, \\beta\\) are roots of \\(x^2 - 6x + 8 = 0\\), find \\((\\alpha - \\beta)^2\\).",
     ["4", "16", "36", "8"],
     "A", "OSC", "easy",
     "\\((\\alpha - \\beta)^2 = (\\alpha + \\beta)^2 - 4\\alpha \\beta = 6^2 - 4(8) = 36 - 32 = 4\\)."),

    # 30
    ("If \\(\\alpha, \\beta\\) are roots of \\(x^2 - 8x + 12 = 0\\), find \\((\\alpha - \\beta)^2\\).",
     ["16", "64", "48", "4"],
     "A", "OSC", "easy",
     "\\(8^2 - 4(12) = 64 - 48 = 16\\)."),

    # 31
    ("Find \\(k\\) if the sum of the roots of \\(x^2 + kx - 12 = 0\\) is 5.",
     ["-5", "5", "12", "-12"],
     "A", "OSC", "easy",
     "Sum = \\(-k = 5 \\implies k = -5\\)."),

    # 32
    ("Find \\(k\\) if the product of the roots of \\(2x^2 - 5x + k = 0\\) is 4.",
     ["8", "4", "2", "-8"],
     "A", "OSC", "easy",
     "Product = \\(k/2 = 4 \\implies k = 8\\)."),

    # 33
    ("If one root of \\(x^2 - 8x + k = 0\\) is 3, what is the other root?",
     ["5", "3", "8", "-5"],
     "A", "OSC", "easy",
     "Sum of roots is 8: \\(3 + \\beta = 8 \\implies \\beta = 5\\)."),

    # 34
    ("From the previous question, what is the value of \\(k\\)?",
     ["15", "8", "24", "5"],
     "A", "OSC", "easy",
     "\\(k = \\alpha \\beta = 3 \\times 5 = 15\\)."),

    # 35
    ("If one root of \\(x^2 + 10x + k = 0\\) is \\(-2\\), what is the other root?",
     ["-8", "8", "-10", "12"],
     "A", "OSC", "easy",
     "Sum is \\(-10\\): \\(-2 + \\beta = -10 \\implies \\beta = -8\\)."),

    # 36
    ("From the previous problem, what is \\(k\\)?",
     ["16", "-16", "20", "-20"],
     "A", "OSC", "easy",
     "\\(k = (-2)(-8) = 16\\)."),

    # 37
    ("If the roots of \\(3x^2 + kx - 3 = 0\\) are reciprocals of each other, what can be said?",
     ["Product is \\(-3/3 = -1\\), so they are negative reciprocals (\\(\\alpha = -1/\\beta\\))",
      "They are equal",
      "They are positive reciprocals",
      "k must equal 0"],
     "A", "OSC", "easy",
     "\\(c/a = -3/3 = -1\\), so \\(\\alpha \\beta = -1\\), which means the roots are negative reciprocals."),

    # 38
    ("If \\(\\alpha = 7, \\beta = -3\\), what is the quadratic equation?",
     ["\\(x^2 - 4x - 21 = 0\\)", "\\(x^2 + 4x - 21 = 0\\)", "\\(x^2 - 4x + 21 = 0\\)", "\\(x^2 - 10x - 21 = 0\\)"],
     "A", "OSC", "easy",
     "Sum = 4, product = \\(-21\\). Equation: \\(x^2 - 4x - 21 = 0\\)."),

    # 39
    ("If \\(\\alpha = -6, \\beta = -4\\), what is the quadratic equation?",
     ["\\(x^2 + 10x + 24 = 0\\)", "\\(x^2 - 10x + 24 = 0\\)", "\\(x^2 + 10x - 24 = 0\\)", "\\(x^2 - 24x + 10 = 0\\)"],
     "A", "OSC", "easy",
     "Sum = \\(-10\\), product = 24. Equation: \\(x^2 - (-10)x + 24 = 0 \\implies x^2 + 10x + 24 = 0\\)."),

    # 40
    ("If \\(\\alpha = 8, \\beta = 2\\), what is the quadratic equation?",
     ["\\(x^2 - 10x + 16 = 0\\)", "\\(x^2 + 10x + 16 = 0\\)", "\\(x^2 - 10x - 16 = 0\\)", "\\(x^2 - 6x + 16 = 0\\)"],
     "A", "OSC", "easy",
     "Sum = 10, product = 16. \\(x^2 - 10x + 16 = 0\\).")
]

t26_prac = [
    # 41
    ("Form equation for roots 1 and 2.", ["\\(x^2 - 3x + 2 = 0\\)", "\\(x^2 + 3x + 2 = 0\\)", "\\(x^2 - 2x + 3 = 0\\)", "\\(x^2 - 3x - 2 = 0\\)"], "A", "OSC", "easy", "Sum = 3, prod = 2."),
    # 42
    ("Form equation for roots 2 and 3.", ["\\(x^2 - 5x + 6 = 0\\)", "\\(x^2 + 5x + 6 = 0\\)", "\\(x^2 - 6x + 5 = 0\\)", "\\(x^2 - 5x - 6 = 0\\)"], "A", "OSC", "easy", "Sum = 5, prod = 6."),
    # 43
    ("Form equation for roots 3 and 4.", ["\\(x^2 - 7x + 12 = 0\\)", "\\(x^2 + 7x + 12 = 0\\)", "\\(x^2 - 12x + 7 = 0\\)", "\\(x^2 - 7x - 12 = 0\\)"], "A", "OSC", "easy", "Sum = 7, prod = 12."),
    # 44
    ("Form equation for roots 4 and 5.", ["\\(x^2 - 9x + 20 = 0\\)", "\\(x^2 + 9x + 20 = 0\\)", "\\(x^2 - 20x + 9 = 0\\)", "\\(x^2 - 9x - 20 = 0\\)"], "A", "OSC", "easy", "Sum = 9, prod = 20."),
    # 45
    ("Form equation for roots 5 and 6.", ["\\(x^2 - 11x + 30 = 0\\)", "\\(x^2 + 11x + 30 = 0\\)", "\\(x^2 - 30x + 11 = 0\\)", "\\(x^2 - 11x - 30 = 0\\)"], "A", "OSC", "easy", "Sum = 11, prod = 30."),
    # 46
    ("Form equation for roots 6 and 7.", ["\\(x^2 - 13x + 42 = 0\\)", "\\(x^2 + 13x + 42 = 0\\)", "\\(x^2 - 42x + 13 = 0\\)", "\\(x^2 - 13x - 42 = 0\\)"], "A", "OSC", "easy", "Sum = 13, prod = 42."),
    # 47
    ("Form equation for roots 7 and 8.", ["\\(x^2 - 15x + 56 = 0\\)", "\\(x^2 + 15x + 56 = 0\\)", "\\(x^2 - 56x + 15 = 0\\)", "\\(x^2 - 15x - 56 = 0\\)"], "A", "OSC", "easy", "Sum = 15, prod = 56."),
    # 48
    ("Form equation for roots 8 and 9.", ["\\(x^2 - 17x + 72 = 0\\)", "\\(x^2 + 17x + 72 = 0\\)", "\\(x^2 - 72x + 17 = 0\\)", "\\(x^2 - 17x - 72 = 0\\)"], "A", "OSC", "easy", "Sum = 17, prod = 72."),
    # 49
    ("Form equation for roots 9 and 10.", ["\\(x^2 - 19x + 90 = 0\\)", "\\(x^2 + 19x + 90 = 0\\)", "\\(x^2 - 90x + 19 = 0\\)", "\\(x^2 - 19x - 90 = 0\\)"], "A", "OSC", "easy", "Sum = 19, prod = 90."),
    # 50
    ("Form equation for roots 10 and 11.", ["\\(x^2 - 21x + 110 = 0\\)", "\\(x^2 + 21x + 110 = 0\\)", "\\(x^2 - 110x + 21 = 0\\)", "\\(x^2 - 21x - 110 = 0\\)"], "A", "OSC", "easy", "Sum = 21, prod = 110."),
    # 51
    ("Form equation for roots -1 and -2.", ["\\(x^2 + 3x + 2 = 0\\)", "\\(x^2 - 3x + 2 = 0\\)", "\\(x^2 + 2x + 3 = 0\\)", "\\(x^2 + 3x - 2 = 0\\)"], "A", "OSC", "easy", "Sum = -3, prod = 2."),
    # 52
    ("Form equation for roots -2 and -3.", ["\\(x^2 + 5x + 6 = 0\\)", "\\(x^2 - 5x + 6 = 0\\)", "\\(x^2 + 6x + 5 = 0\\)", "\\(x^2 + 5x - 6 = 0\\)"], "A", "OSC", "easy", "Sum = -5, prod = 6."),
    # 53
    ("Form equation for roots -3 and -4.", ["\\(x^2 + 7x + 12 = 0\\)", "\\(x^2 - 7x + 12 = 0\\)", "\\(x^2 + 12x + 7 = 0\\)", "\\(x^2 + 7x - 12 = 0\\)"], "A", "OSC", "easy", "Sum = -7, prod = 12."),
    # 54
    ("Form equation for roots -4 and -5.", ["\\(x^2 + 9x + 20 = 0\\)", "\\(x^2 - 9x + 20 = 0\\)", "\\(x^2 + 20x + 9 = 0\\)", "\\(x^2 + 9x - 20 = 0\\)"], "A", "OSC", "easy", "Sum = -9, prod = 20."),
    # 55
    ("Form equation for roots -5 and -6.", ["\\(x^2 + 11x + 30 = 0\\)", "\\(x^2 - 11x + 30 = 0\\)", "\\(x^2 + 30x + 11 = 0\\)", "\\(x^2 + 11x - 30 = 0\\)"], "A", "OSC", "easy", "Sum = -11, prod = 30."),
    # 56
    ("Form equation for roots -6 and -7.", ["\\(x^2 + 13x + 42 = 0\\)", "\\(x^2 - 13x + 42 = 0\\)", "\\(x^2 + 42x + 13 = 0\\)", "\\(x^2 + 13x - 42 = 0\\)"], "A", "OSC", "easy", "Sum = -13, prod = 42."),
    # 57
    ("Form equation for roots -7 and -8.", ["\\(x^2 + 15x + 56 = 0\\)", "\\(x^2 - 15x + 56 = 0\\)", "\\(x^2 + 56x + 15 = 0\\)", "\\(x^2 + 15x - 56 = 0\\)"], "A", "OSC", "easy", "Sum = -15, prod = 56."),
    # 58
    ("Form equation for roots -8 and -9.", ["\\(x^2 + 17x + 72 = 0\\)", "\\(x^2 - 17x + 72 = 0\\)", "\\(x^2 + 72x + 17 = 0\\)", "\\(x^2 + 17x - 72 = 0\\)"], "A", "OSC", "easy", "Sum = -17, prod = 72."),
    # 59
    ("Form equation for roots -9 and -10.", ["\\(x^2 + 19x + 90 = 0\\)", "\\(x^2 - 19x + 90 = 0\\)", "\\(x^2 + 90x + 19 = 0\\)", "\\(x^2 + 19x - 90 = 0\\)"], "A", "OSC", "easy", "Sum = -19, prod = 90."),
    # 60
    ("Form equation for roots -10 and -11.", ["\\(x^2 + 21x + 110 = 0\\)", "\\(x^2 - 21x + 110 = 0\\)", "\\(x^2 + 110x + 21 = 0\\)", "\\(x^2 + 21x - 110 = 0\\)"], "A", "OSC", "easy", "Sum = -21, prod = 110."),
    # 61
    ("Find sum of roots of \\(5x^2 - 15x + 7 = 0\\).", ["3", "-3", "15", "7/5"], "A", "OSC", "easy", "\\(-(-15)/5 = 3\\)."),
    # 62
    ("Find product of roots of \\(5x^2 - 15x + 7 = 0\\).", ["7/5", "-7/5", "3", "7"], "A", "OSC", "easy", "\\(7/5\\)."),
    # 63
    ("Find sum of roots of \\(4x^2 + 12x - 9 = 0\\).", ["-3", "3", "-9/4", "9/4"], "A", "OSC", "easy", "\\(-12/4 = -3\\)."),
    # 64
    ("Find product of roots of \\(4x^2 + 12x - 9 = 0\\).", ["-9/4", "9/4", "-3", "3"], "A", "OSC", "easy", "\\(-9/4\\)."),
    # 65
    ("Find sum of roots of \\(6x^2 - 18x + 5 = 0\\).", ["3", "-3", "5/6", "-5/6"], "A", "OSC", "easy", "\\(18/6 = 3\\)."),
    # 66
    ("Find product of roots of \\(6x^2 - 18x + 5 = 0\\).", ["5/6", "-5/6", "3", "-3"], "A", "OSC", "easy", "\\(5/6\\)."),
    # 67
    ("Find sum of roots of \\(7x^2 + 21x + 1 = 0\\).", ["-3", "3", "1/7", "-1/7"], "A", "OSC", "easy", "\\(-21/7 = -3\\)."),
    # 68
    ("Find product of roots of \\(7x^2 + 21x + 1 = 0\\).", ["1/7", "-1/7", "-3", "3"], "A", "OSC", "easy", "\\(1/7\\)."),
    # 69
    ("Find sum of roots of \\(8x^2 - 32x + 3 = 0\\).", ["4", "-4", "3/8", "-3/8"], "A", "OSC", "easy", "\\(32/8 = 4\\)."),
    # 70
    ("Find product of roots of \\(8x^2 - 32x + 3 = 0\\).", ["3/8", "-3/8", "4", "-4"], "A", "OSC", "easy", "\\(3/8\\).")
]

t26_mock = [
    # 71
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0f172a" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Roots &amp; Coefficients Bridge</text>
  <text x="170" y="80" fill="#f8fafc" font-size="12" text-anchor="middle">Sum: α + β = -b/a</text>
  <text x="170" y="105" fill="#4ade80" font-size="12" text-anchor="middle">Product: α * β = c/a</text>
</svg>
</div>
What is the fundamental utility of Vieta's formulas (relation between roots and coefficients)?""",
     ["They establish an exact algebraic bridge connecting the solutions (roots) to the equation's coefficients without solving the equation",
      "They prove that all quadratic equations have rational roots",
      "They eliminate the need for variables",
      "They convert quadratic equations into linear equations"],
     "A", "OSC", "easy",
     "The relations \\(\\alpha + \\beta = -b/a\\) and \\(\\alpha \\beta = c/a\\) allow us to evaluate properties, symmetric functions, and conditions on the roots directly from the coefficients without having to find the individual roots."),

    # 72
    ("If \\(\\alpha = 1, \\beta = 1\\), what is the quadratic equation?", ["\\(x^2 - 2x + 1 = 0\\)", "\\(x^2 + 2x + 1 = 0\\)", "\\(x^2 - 1 = 0\\)", "\\(x^2 + 1 = 0\\)"], "A", "OSC", "easy", "\\((x - 1)^2 = x^2 - 2x + 1 = 0\\)."),
    # 73
    ("If \\(\\alpha = -1, \\beta = -1\\), what is the quadratic equation?", ["\\(x^2 + 2x + 1 = 0\\)", "\\(x^2 - 2x + 1 = 0\\)", "\\(x^2 - 1 = 0\\)", "\\(x^2 + 1 = 0\\)"], "A", "OSC", "easy", "\\((x + 1)^2 = x^2 + 2x + 1 = 0\\)."),
    # 74
    ("If \\(\\alpha = 2, \\beta = -2\\), what is the quadratic equation?", ["\\(x^2 - 4 = 0\\)", "\\(x^2 + 4 = 0\\)", "\\(x^2 - 4x + 4 = 0\\)", "\\(x^2 + 4x + 4 = 0\\)"], "A", "OSC", "easy", "Sum = 0, product = \\(-4\\). \\(x^2 - 4 = 0\\)."),
    # 75
    ("If \\(\\alpha = 3, \\beta = -3\\), what is the quadratic equation?", ["\\(x^2 - 9 = 0\\)", "\\(x^2 + 9 = 0\\)", "\\(x^2 - 6x + 9 = 0\\)", "\\(x^2 + 6x + 9 = 0\\)"], "A", "OSC", "easy", "Sum = 0, product = \\(-9\\). \\(x^2 - 9 = 0\\)."),
    # 76
    ("If \\(\\alpha = 4, \\beta = -4\\), what is the quadratic equation?", ["\\(x^2 - 16 = 0\\)", "\\(x^2 + 16 = 0\\)", "\\(x^2 - 8x + 16 = 0\\)", "\\(x^2 + 8x + 16 = 0\\)"], "A", "OSC", "easy", "\\(x^2 - 16 = 0\\)."),
    # 77
    ("If \\(\\alpha = 5, \\beta = -5\\), what is the quadratic equation?", ["\\(x^2 - 25 = 0\\)", "\\(x^2 + 25 = 0\\)", "\\(x^2 - 10x + 25 = 0\\)", "\\(x^2 + 10x + 25 = 0\\)"], "A", "OSC", "easy", "\\(x^2 - 25 = 0\\)."),
    # 78
    ("If \\(\\alpha + \\beta = 0\\), what must be the coefficient of \\(x\\)?", ["0", "1", "-1", "Cannot be determined"], "A", "OSC", "easy", "\\(-b/a = 0 \\implies b = 0\\)."),
    # 79
    ("If \\(\\alpha \\beta = 0\\), what must be the constant term \\(c\\)?", ["0", "1", "-1", "Cannot be determined"], "A", "OSC", "easy", "\\(c/a = 0 \\implies c = 0\\)."),
    # 80
    ("If \\(\\alpha \\beta = 1\\), what must be the relation between \\(a\\) and \\(c\\)?", ["\\(a = c\\)", "\\(a = -c\\)", "\\(a + c = 0\\)", "\\(a = 1\\)"], "A", "OSC", "easy", "\\(c/a = 1 \\implies a = c\\)."),
    # 81
    ("If \\(\\alpha \\beta = -1\\), what must be the relation between \\(a\\) and \\(c\\)?", ["\\(c = -a\\)", "\\(a = c\\)", "\\(ac = 1\\)", "\\(b = 0\\)"], "A", "OSC", "easy", "\\(c/a = -1 \\implies c = -a\\)."),
    # 82
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0b132b" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1c2541" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Symmetric Functions of Roots</text>
  <text x="170" y="80" fill="#f8fafc" font-size="11" text-anchor="middle">α² + β² = (α + β)² - 2αβ</text>
  <text x="170" y="105" fill="#4ade80" font-size="11" text-anchor="middle">α³ + β³ = (α + β)³ - 3αβ(α + β)</text>
</svg>
</div>
Why are \\(\\alpha^2 + \\beta^2\\) and \\(\\alpha^3 + \\beta^3\\) termed 'symmetric functions' of roots?""",
     ["Because exchanging α and β leaves the numerical value of the expression completely unchanged",
      "Because their graphs are symmetric circles",
      "Because both roots must be positive integers",
      "Because they equal zero"],
     "A", "OSC", "easy",
     "A function \\(f(\\alpha, \\beta)\\) is symmetric if \\(f(\\alpha, \\beta) = f(\\beta, \\alpha)\\). Since interchanging \\(\\alpha\\) and \\(\\beta\\) produces identical expressions, they can always be represented strictly using basic symmetric sums \\(\\alpha + \\beta\\) and products \\(\\alpha \\beta\\).")
]

all_q_26 = build_topic_questions(TOPIC_CODE, exam_data, t26_prac, t26_mock)
out_26 = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch2_t6.json")
with open(out_26, "w", encoding="utf-8") as f:
    json.dump(all_q_26, f, indent=2, ensure_ascii=False)
print(f"Generated {len(all_q_26)} questions for {TOPIC_CODE} -> {out_26}")
