# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for MH-10-MTH1-2-2.2
Topic: Solving Quadratic Equations by Factorisation Method
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

TOPIC_CODE = "MH-10-MTH1-2-2.2"

# 40 EXAM (1-40)
exam_data = [
    # 1
    ("What mathematical property is the foundation of the Factorisation Method for solving quadratic equations?",
     ["Zero Product Property: If \\(A \\times B = 0\\), then either \\(A = 0\\) or \\(B = 0\\) (or both)",
      "Distributive Property only",
      "Commutative Property of Addition",
      "Pythagorean Theorem"],
     "A", "OSC", "easy",
     "The factorisation method relies on expressing the quadratic polynomial as a product of two linear factors \\((x - \\alpha)(x - \\beta) = 0\\). By the Zero Product Property, if a product of two real expressions is zero, at least one of the factors must be zero."),

    # 2
    ("Solve by factorisation: \\(x^2 - 15x + 54 = 0\\). What are the roots?",
     ["\\(9\\) and \\(6\\)", "\\(-9\\) and \\(-6\\)", "\\(18\\) and \\(3\\)", "\\(-18\\) and \\(-3\\)"],
     "A", "OSC", "easy",
     "We find two numbers whose product is 54 and sum is \\(-15\\). These are \\(-9\\) and \\(-6\\). Thus \\((x - 9)(x - 6) = 0 \\implies x = 9\\) or \\(x = 6\\)."),

    # 3
    ("Solve by factorisation: \\(x^2 + x - 20 = 0\\). What are the roots?",
     ["\\(-5\\) and \\(4\\)", "\\(5\\) and \\(-4\\)", "\\(10\\) and \\(-2\\)", "\\(-10\\) and \\(2\\)"],
     "A", "OSC", "easy",
     "Product is \\(-20\\) and sum is \\(+1\\). The numbers are \\(+5\\) and \\(-4\\). \\((x + 5)(x - 4) = 0 \\implies x = -5\\) or \\(x = 4\\)."),

    # 4
    ("Solve: \\(2y^2 + 27y + 13 = 0\\). What are the roots?",
     ["\\(-\\frac{1}{2}\\) and \\(-13\\)",
      "\\(\\frac{1}{2}\\) and \\(13\\)",
      "\\(-1\\) and \\(-26\\)",
      "\\(2\\) and \\(13\\)"],
     "A", "OSC", "medium",
     "Product is \\(2 \\times 13 = 26\\), sum is 27. Split 27y into \\(26y + y\\): \\(2y^2 + 26y + y + 13 = 0 \\implies 2y(y + 13) + 1(y + 13) = 0 \\implies (2y + 1)(y + 13) = 0\\). Thus \\(y = -1/2\\) or \\(y = -13\\)."),

    # 5
    ("Solve: \\(5m^2 = 22m + 15\\). What are the roots?",
     ["\\(-\\frac{3}{5}\\) and \\(5\\)",
      "\\(\\frac{3}{5}\\) and \\(-5\\)",
      "\\(3\\) and \\(-5\\)",
      "\\(-\\frac{5}{3}\\) and \\(5\\)"],
     "A", "OSC", "medium",
     "Rewrite in standard form: \\(5m^2 - 22m - 15 = 0\\). Product is \\(5 \\times (-15) = -75\\), sum is \\(-22\\). Numbers are \\(-25\\) and \\(+3\\). \\(5m^2 - 25m + 3m - 15 = 0 \\implies 5m(m - 5) + 3(m - 5) = 0 \\implies (5m + 3)(m - 5) = 0\\). Roots are \\(m = -3/5\\) and \\(m = 5\\)."),

    # 6
    ("Solve: \\(2x^2 - 2x + \\frac{1}{2} = 0\\). What are the roots?",
     ["\\(\\frac{1}{2}\\) (repeated root)",
      "\\(-\\frac{1}{2}\\) (repeated root)",
      "\\(1\\) and \\(2\\)",
      "\\(\\frac{1}{4}\\) and \\(1\\)"],
     "A", "OSC", "medium",
     "Multiply throughout by 2: \\(4x^2 - 4x + 1 = 0\\). This is a perfect square: \\((2x - 1)^2 = 0 \\implies 2x - 1 = 0 \\implies x = 1/2\\)."),

    # 7
    ("Solve: \\(\\sqrt{2}x^2 + 7x + 5\\sqrt{2} = 0\\). What are the roots?",
     ["\\(-\\sqrt{2}\\) and \\(-\\frac{5}{\\sqrt{2}}\\) (or \\(-\\frac{5\\sqrt{2}}{2}\\))",
      "\\(\\sqrt{2}\\) and \\(\\frac{5}{\\sqrt{2}}\\)",
      "\\(-2\\) and \\(-5\\)",
      "\\(-\\sqrt{5}\\) and \\(-\\sqrt{2}\\)"],
     "A", "OSC", "hard",
     "Product is \\(\\sqrt{2} \\times 5\\sqrt{2} = 5 \\times 2 = 10\\). Sum is 7. Numbers are 5 and 2. Split: \\(\\sqrt{2}x^2 + 2x + 5x + 5\\sqrt{2} = 0 \\implies \\sqrt{2}x(x + \\sqrt{2}) + 5(x + \\sqrt{2}) = 0 \\implies (\\sqrt{2}x + 5)(x + \\sqrt{2}) = 0\\). Roots are \\(x = -\\sqrt{2}\\) and \\(x = -5/\\sqrt{2}\\)."),

    # 8
    ("Solve: \\(3x^2 - 2\\sqrt{6}x + 2 = 0\\). What are the roots?",
     ["\\(\\sqrt{\\frac{2}{3}}\\) (repeated root)",
      "\\(\\sqrt{6}\\) and \\(-\\sqrt{6}\\)",
      "\\(\\frac{2}{3}\\) and \\(1\\)",
      "\\(-\\sqrt{\\frac{2}{3}}\\) (repeated root)"],
     "A", "OSC", "hard",
     "Notice that \\(3x^2 = (\\sqrt{3}x)^2\\), \\(2 = (\\sqrt{2})^2\\), and the middle term is \\(2(\\sqrt{3}x)(\\sqrt{2}) = 2\\sqrt{6}x\\). Hence \\((\\sqrt{3}x - \\sqrt{2})^2 = 0 \\implies x = \\frac{\\sqrt{2}}{\\sqrt{3}} = \\sqrt{\\frac{2}{3}}\\)."),

    # 9
    ("Solve: \\(2m(m - 24) = 50\\). What are the roots?",
     ["\\(25\\) and \\(-1\\)", "\\(-25\\) and \\(1\\)", "\\(24\\) and \\(2\\)", "\\(50\\) and \\(-1\\)"],
     "A", "OSC", "medium",
     "\\(2m^2 - 48m - 50 = 0\\). Divide by 2: \\(m^2 - 24m - 25 = 0\\). Product is \\(-25\\), sum is \\(-24\\). Numbers are \\(-25\\) and \\(+1\\). \\((m - 25)(m + 1) = 0 \\implies m = 25\\) or \\(m = -1\\)."),

    # 10
    ("Solve: \\(25m^2 = 9\\). What are the roots?",
     ["\\(\\frac{3}{5}\\) and \\(-\\frac{3}{5}\\)",
      "\\(\\frac{9}{25}\\) only",
      "\\(3\\) and \\(-3\\)",
      "\\(\\frac{5}{3}\\) and \\(-\\frac{5}{3}\\)"],
     "A", "OSC", "easy",
     "\\(25m^2 - 9 = 0 \\implies (5m - 3)(5m + 3) = 0 \\implies m = 3/5\\) or \\(m = -3/5\\)."),

    # 11
    ("Solve: \\(7m^2 = 21m\\). What are the roots?",
     ["\\(0\\) and \\(3\\)", "\\(3\\) only", "\\(0\\) and \\(7\\)", "\\(21\\) and \\(7\\)"],
     "A", "OSC", "easy",
     "\\(7m^2 - 21m = 0 \\implies 7m(m - 3) = 0 \\implies m = 0\\) or \\(m = 3\\). (Note: dividing by \\(m\\) incorrectly loses the root \\(m = 0\\)!)"),

    # 12
    ("Solve: \\(m^2 - 11 = 0\\). What are the roots?",
     ["\\(\\sqrt{11}\\) and \\(-\\sqrt{11}\\)",
      "\\(11\\) and \\(-11\\)",
      "\\(\\sqrt{11}\\) only",
      "No real roots"],
     "A", "OSC", "easy",
     "\\(m^2 - (\\sqrt{11})^2 = 0 \\implies (m - \\sqrt{11})(m + \\sqrt{11}) = 0 \\implies m = \\pm \\sqrt{11}\\)."),

    # 13
    ("Solve by factorisation: \\(x^2 - 3x - 10 = 0\\).",
     ["\\(5\\) and \\(-2\\)", "\\(-5\\) and \\(2\\)", "\\(10\\) and \\(-1\\)", "\\(-10\\) and \\(1\\)"],
     "A", "OSC", "easy",
     "\\((x - 5)(x + 2) = 0 \\implies x = 5\\) or \\(x = -2\\)."),

    # 14
    ("Solve: \\(x^2 - 8x + 16 = 0\\).",
     ["\\(4\\) (repeated root)", "\\(-4\\) (repeated root)", "\\(8\\) and \\(2\\)", "\\(16\\) and \\(1\\)"],
     "A", "OSC", "easy",
     "\\((x - 4)^2 = 0 \\implies x = 4\\)."),

    # 15
    ("Solve: \\(3x^2 - x - 2 = 0\\).",
     ["\\(1\\) and \\(-\\frac{2}{3}\\)",
      "\\(-1\\) and \\(\\frac{2}{3}\\)",
      "\\(2\\) and \\(-\\frac{1}{3}\\)",
      "\\(-2\\) and \\(1\\)"],
     "A", "OSC", "medium",
     "Product is \\(3 \\times (-2) = -6\\), sum is \\(-1\\). Numbers are \\(-3\\) and \\(+2\\). \\(3x^2 - 3x + 2x - 2 = 0 \\implies 3x(x - 1) + 2(x - 1) = 0 \\implies (3x + 2)(x - 1) = 0 \\implies x = 1\\) or \\(x = -2/3\\)."),

    # 16
    ("Solve: \\(6x - \\frac{2}{x} = 1\\).",
     ["\\(\\frac{2}{3}\\) and \\(-\\frac{1}{2}\\)",
      "\\(-\\frac{2}{3}\\) and \\(\\frac{1}{2}\\)",
      "\\(2\\) and \\(-1\\)",
      "\\(3\\) and \\(-2\\)"],
     "A", "OSC", "medium",
     "Multiply by \\(x\\): \\(6x^2 - 2 = x \\implies 6x^2 - x - 2 = 0\\). Product is \\(-12\\), sum is \\(-1\\). Split: \\(-4\\) and \\(+3\\). \\(6x^2 - 4x + 3x - 2 = 0 \\implies 2x(3x - 2) + 1(3x - 2) = 0 \\implies x = 2/3\\) or \\(x = -1/2\\)."),

    # 17
    ("Solve: \\(4x^2 - 12x + 9 = 0\\).",
     ["\\(\\frac{3}{2}\\) (repeated root)",
      "\\(-\\frac{3}{2}\\) (repeated root)",
      "\\(3\\) and \\(2\\)",
      "\\(9\\) and \\(4\\)"],
     "A", "OSC", "easy",
     "\\((2x - 3)^2 = 0 \\implies 2x - 3 = 0 \\implies x = 3/2\\)."),

    # 18
    ("Solve: \\(x^2 - 4x = 0\\).",
     ["\\(0\\) and \\(4\\)", "\\(2\\) and \\(-2\\)", "\\(4\\) only", "\\(0\\) and \\(-4\\)"],
     "A", "OSC", "easy",
     "\\(x(x - 4) = 0 \\implies x = 0\\) or \\(x = 4\\)."),

    # 19
    ("Solve: \\(2x^2 + 7x + 3 = 0\\).",
     ["\\(-\\frac{1}{2}\\) and \\(-3\\)",
      "\\(\\frac{1}{2}\\) and \\(3\\)",
      "\\(-1\\) and \\(-6\\)",
      "\\(-2\\) and \\(-3\\)"],
     "A", "OSC", "medium",
     "Product is 6, sum is 7. Numbers are 6 and 1. \\(2x^2 + 6x + x + 3 = 0 \\implies 2x(x + 3) + 1(x + 3) = 0 \\implies (2x + 1)(x + 3) = 0 \\implies x = -1/2\\) or \\(x = -3\\)."),

    # 20
    ("Solve: \\(x^2 - 2x - 15 = 0\\).",
     ["\\(5\\) and \\(-3\\)", "\\(-5\\) and \\(3\\)", "\\(15\\) and \\(-1\\)", "\\(-15\\) and \\(1\\)"],
     "A", "OSC", "easy",
     "\\((x - 5)(x + 3) = 0 \\implies x = 5\\) or \\(x = -3\\)."),

    # 21
    ("Solve: \\(x^2 + 6x + 9 = 0\\).",
     ["\\(-3\\) (repeated root)", "\\(3\\) (repeated root)", "\\(9\\) and \\(1\\)", "\\(-9\\) and \\(-1\\)"],
     "A", "OSC", "easy",
     "\\((x + 3)^2 = 0 \\implies x = -3\\)."),

    # 22
    ("Solve: \\(2x^2 - 5x + 2 = 0\\).",
     ["\\(2\\) and \\(\\frac{1}{2}\\)",
      "\\(-2\\) and \\(-\\frac{1}{2}\\)",
      "\\(4\\) and \\(1\\)",
      "\\(2\\) and \\(1\\)"],
     "A", "OSC", "medium",
     "Product is 4, sum is \\(-5\\). Numbers are \\(-4\\) and \\(-1\\). \\(2x^2 - 4x - x + 2 = 0 \\implies 2x(x - 2) - 1(x - 2) = 0 \\implies (2x - 1)(x - 2) = 0 \\implies x = 2\\) or \\(x = 1/2\\)."),

    # 23
    ("Solve: \\(x^2 - 49 = 0\\).",
     ["\\(7\\) and \\(-7\\)", "\\(49\\) and \\(-49\\)", "\\(0\\) and \\(7\\)", "\\(14\\) and \\(-14\\)"],
     "A", "OSC", "easy",
     "\\((x - 7)(x + 7) = 0 \\implies x = \\pm 7\\)."),

    # 24
    ("Solve: \\(3x^2 - 12 = 0\\).",
     ["\\(2\\) and \\(-2\\)", "\\(4\\) and \\(-4\\)", "\\(12\\) and \\(-12\\)", "\\(6\\) and \\(-6\\)"],
     "A", "OSC", "easy",
     "\\(3(x^2 - 4) = 0 \\implies x^2 = 4 \\implies x = \\pm 2\\)."),

    # 25
    ("Solve: \\(x^2 + 5x + 6 = 0\\).",
     ["\\(-2\\) and \\(-3\\)", "\\(2\\) and \\(3\\)", "\\(-1\\) and \\(-6\\)", "\\(1\\) and \\(6\\)"],
     "A", "OSC", "easy",
     "\\((x + 2)(x + 3) = 0 \\implies x = -2\\) or \\(x = -3\\)."),

    # 26
    ("Solve: \\(x^2 - 5x + 6 = 0\\).",
     ["\\(2\\) and \\(3\\)", "\\(-2\\) and \\(-3\\)", "\\(1\\) and \\(6\\)", "\\(-1\\) and \\(-6\\)"],
     "A", "OSC", "easy",
     "\\((x - 2)(x - 3) = 0 \\implies x = 2\\) or \\(x = 3\\)."),

    # 27
    ("Solve: \\(x^2 - x - 6 = 0\\).",
     ["\\(3\\) and \\(-2\\)", "\\(-3\\) and \\(2\\)", "\\(6\\) and \\(-1\\)", "\\(-6\\) and \\(1\\)"],
     "A", "OSC", "easy",
     "\\((x - 3)(x + 2) = 0 \\implies x = 3\\) or \\(x = -2\\)."),

    # 28
    ("Solve: \\(x^2 + x - 6 = 0\\).",
     ["\\(-3\\) and \\(2\\)", "\\(3\\) and \\(-2\\)", "\\(-6\\) and \\(1\\)", "\\(6\\) and \\(-1\\)"],
     "A", "OSC", "easy",
     "\\((x + 3)(x - 2) = 0 \\implies x = -3\\) or \\(x = 2\\)."),

    # 29
    ("Solve: \\(5x^2 - 4x = 0\\).",
     ["\\(0\\) and \\(\\frac{4}{5}\\)",
      "\\(\\frac{4}{5}\\) only",
      "\\(0\\) and \\(-\\frac{4}{5}\\)",
      "\\(5\\) and \\(4\\)"],
     "A", "OSC", "easy",
     "\\(x(5x - 4) = 0 \\implies x = 0\\) or \\(x = 4/5\\)."),

    # 30
    ("Solve: \\(x^2 - 1 = 0\\).",
     ["\\(1\\) and \\(-1\\)", "\\(1\\) only", "\\(0\\) and \\(1\\)", "\\(2\\) and \\(-2\\)"],
     "A", "OSC", "easy",
     "\\((x - 1)(x + 1) = 0 \\implies x = \\pm 1\\)."),

    # 31
    ("Solve: \\(100x^2 - 20x + 1 = 0\\).",
     ["\\(\\frac{1}{10}\\) (repeated root)",
      "\\(-\\frac{1}{10}\\) (repeated root)",
      "\\(10\\) and \\(-10\\)",
      "\\(1\\) and \\(20\\)"],
     "A", "OSC", "easy",
     "\\((10x - 1)^2 = 0 \\implies 10x - 1 = 0 \\implies x = 1/10\\)."),

    # 32
    ("Solve: \\(x^2 - 10x + 25 = 0\\).",
     ["\\(5\\) (repeated root)", "\\(-5\\) (repeated root)", "\\(25\\) and \\(1\\)", "\\(10\\) and \\(2\\)"],
     "A", "OSC", "easy",
     "\\((x - 5)^2 = 0 \\implies x = 5\\)."),

    # 33
    ("Solve: \\(2x^2 + x - 6 = 0\\).",
     ["\\(-2\\) and \\(\\frac{3}{2}\\)",
      "\\(2\\) and \\(-\\frac{3}{2}\\)",
      "\\(-3\\) and \\(2\\)",
      "\\(3\\) and \\(-2\\)"],
     "A", "OSC", "medium",
     "Product is \\(-12\\), sum is 1. Numbers are 4 and \\(-3\\). \\(2x(x + 2) - 3(x + 2) = 0 \\implies (2x - 3)(x + 2) = 0 \\implies x = 3/2\\) or \\(x = -2\\)."),

    # 34
    ("Solve: \\(x^2 - 11x + 28 = 0\\).",
     ["\\(7\\) and \\(4\\)", "\\(-7\\) and \\(-4\\)", "\\(14\\) and \\(2\\)", "\\(-14\\) and \\(-2\\)"],
     "A", "OSC", "easy",
     "\\((x - 7)(x - 4) = 0 \\implies x = 7\\) or \\(x = 4\\)."),

    # 35
    ("Solve: \\(x^2 - 13x + 36 = 0\\).",
     ["\\(9\\) and \\(4\\)", "\\(-9\\) and \\(-4\\)", "\\(12\\) and \\(3\\)", "\\(-12\\) and \\(-3\\)"],
     "A", "OSC", "easy",
     "\\((x - 9)(x - 4) = 0 \\implies x = 9\\) or \\(x = 4\\)."),

    # 36
    ("Solve: \\(x^2 - 12x + 36 = 0\\).",
     ["\\(6\\) (repeated root)", "\\(-6\\) (repeated root)", "\\(12\\) and \\(3\\)", "\\(9\\) and \\(4\\)"],
     "A", "OSC", "easy",
     "\\((x - 6)^2 = 0 \\implies x = 6\\)."),

    # 37
    ("Solve: \\(3x^2 - 5x - 2 = 0\\).",
     ["\\(2\\) and \\(-\\frac{1}{3}\\)",
      "\\(-2\\) and \\(\\frac{1}{3}\\)",
      "\\(3\\) and \\(-2\\)",
      "\\(1\\) and \\(-2\\)"],
     "A", "OSC", "medium",
     "Product is \\(-6\\), sum is \\(-5\\). Numbers are \\(-6\\) and \\(+1\\). \\(3x^2 - 6x + x - 2 = 0 \\implies 3x(x - 2) + 1(x - 2) = 0 \\implies (3x + 1)(x - 2) = 0 \\implies x = 2\\) or \\(x = -1/3\\)."),

    # 38
    ("Solve: \\(x^2 - 100 = 0\\).",
     ["\\(10\\) and \\(-10\\)", "\\(100\\) and \\(-100\\)", "\\(50\\) and \\(-50\\)", "\\(0\\) and \\(10\\)"],
     "A", "OSC", "easy",
     "\\((x - 10)(x + 10) = 0 \\implies x = \\pm 10\\)."),

    # 39
    ("Solve: \\(x^2 + 14x + 49 = 0\\).",
     ["\\(-7\\) (repeated root)", "\\(7\\) (repeated root)", "\\(49\\) and \\(1\\)", "\\(-49\\) and \\(-1\\)"],
     "A", "OSC", "easy",
     "\\((x + 7)^2 = 0 \\implies x = -7\\)."),

    # 40
    ("When can a quadratic equation NOT be easily solved by factorisation over rational numbers?",
     ["When the discriminant \\(b^2 - 4ac\\) is not a perfect square, resulting in irrational or complex roots",
      "When the leading coefficient is 1",
      "When the constant term is negative",
      "When the equation has two roots"],
     "A", "OSC", "easy",
     "Factorisation over rational numbers requires finding two integers whose product is \\(ac\\) and sum is \\(b\\), which is only possible when the discriminant \\(b^2 - 4ac\\) is a perfect square.")
]

# 30 PRACTICE (41-70)
practice_data = [
    # 41
    ("Factorise: \\(x^2 - 7x + 12 = 0\\). Find roots.",
     ["\\(4\\) and \\(3\\)", "\\(-4\\) and \\(-3\\)", "\\(6\\) and \\(2\\)", "\\(-6\\) and \\(-2\\)"],
     "A", "OSC", "easy",
     "\\((x - 4)(x - 3) = 0 \\implies x = 4\\) or \\(x = 3\\)."),

    # 42
    ("Factorise: \\(x^2 + 7x + 12 = 0\\). Find roots.",
     ["\\(-4\\) and \\(-3\\)", "\\(4\\) and \\(3\\)", "\\(-6\\) and \\(-2\\)", "\\(6\\) and \\(2\\)"],
     "A", "OSC", "easy",
     "\\((x + 4)(x + 3) = 0 \\implies x = -4\\) or \\(x = -3\\)."),

    # 43
    ("Factorise: \\(x^2 - x - 12 = 0\\). Find roots.",
     ["\\(4\\) and \\(-3\\)", "\\(-4\\) and \\(3\\)", "\\(6\\) and \\(-2\\)", "\\(-6\\) and \\(2\\)"],
     "A", "OSC", "easy",
     "\\((x - 4)(x + 3) = 0 \\implies x = 4\\) or \\(x = -3\\)."),

    # 44
    ("Factorise: \\(x^2 + x - 12 = 0\\). Find roots.",
     ["\\(-4\\) and \\(3\\)", "\\(4\\) and \\(-3\\)", "\\(-6\\) and \\(2\\)", "\\(6\\) and \\(-2\\)"],
     "A", "OSC", "easy",
     "\\((x + 4)(x - 3) = 0 \\implies x = -4\\) or \\(x = 3\\)."),

    # 45
    ("Solve: \\(2x^2 - 3x - 5 = 0\\).",
     ["\\(\\frac{5}{2}\\) and \\(-1\\)",
      "\\(-\\frac{5}{2}\\) and \\(1\\)",
      "\\(5\\) and \\(-2\\)",
      "\\(-5\\) and \\(2\\)"],
     "A", "OSC", "medium",
     "Product is \\(-10\\), sum is \\(-3\\). Numbers are \\(-5\\) and \\(+2\\). \\(2x^2 - 5x + 2x - 5 = 0 \\implies x(2x - 5) + 1(2x - 5) = 0 \\implies x = 5/2\\) or \\(x = -1\\)."),

    # 46
    ("Solve: \\(3x^2 + 10x + 8 = 0\\).",
     ["\\(-2\\) and \\(-\\frac{4}{3}\\)",
      "\\(2\\) and \\(\\frac{4}{3}\\)",
      "\\(-4\\) and \\(-2\\)",
      "\\(-1\\) and \\(-8\\)"],
     "A", "OSC", "medium",
     "Product is 24, sum is 10. Numbers are 6 and 4. \\(3x^2 + 6x + 4x + 8 = 0 \\implies 3x(x + 2) + 4(x + 2) = 0 \\implies x = -2\\) or \\(x = -4/3\\)."),

    # 47
    ("Solve: \\(4x^2 - 1 = 0\\).",
     ["\\(\\frac{1}{2}\\) and \\(-\\frac{1}{2}\\)",
      "\\(1\\) and \\(-1\\)",
      "\\(\\frac{1}{4}\\) and \\(-\\frac{1}{4}\\)",
      "\\(2\\) and \\(-2\\)"],
     "A", "OSC", "easy",
     "\\((2x - 1)(2x + 1) = 0 \\implies x = \\pm 1/2\\)."),

    # 48
    ("Solve: \\(9x^2 - 16 = 0\\).",
     ["\\(\\frac{4}{3}\\) and \\(-\\frac{4}{3}\\)",
      "\\(\\frac{3}{4}\\) and \\(-\\frac{3}{4}\\)",
      "\\(4\\) and \\(-4\\)",
      "\\(16\\) and \\(-16\\)"],
     "A", "OSC", "easy",
     "\\((3x - 4)(3x + 4) = 0 \\implies x = \\pm 4/3\\)."),

    # 49
    ("Solve: \\(x^2 - 9x = 0\\).",
     ["\\(0\\) and \\(9\\)", "\\(3\\) and \\(-3\\)", "\\(9\\) only", "\\(0\\) and \\(-9\\)"],
     "A", "OSC", "easy",
     "\\(x(x - 9) = 0 \\implies x = 0\\) or \\(x = 9\\)."),

    # 50
    ("Solve: \\(x^2 + 8x = 0\\).",
     ["\\(0\\) and \\(-8\\)", "\\(0\\) and \\(8\\)", "\\(-8\\) only", "\\(4\\) and \\(-4\\)"],
     "A", "OSC", "easy",
     "\\(x(x + 8) = 0 \\implies x = 0\\) or \\(x = -8\\)."),

    # 51
    ("Solve: \\(x^2 - 14x + 45 = 0\\).",
     ["\\(9\\) and \\(5\\)", "\\(-9\\) and \\(-5\\)", "\\(15\\) and \\(3\\)", "\\(-15\\) and \\(-3\\)"],
     "A", "OSC", "easy",
     "\\((x - 9)(x - 5) = 0 \\implies x = 9\\) or \\(x = 5\\)."),

    # 52
    ("Solve: \\(x^2 - 16x + 63 = 0\\).",
     ["\\(9\\) and \\(7\\)", "\\(-9\\) and \\(-7\\)", "\\(21\\) and \\(3\\)", "\\(-21\\) and \\(-3\\)"],
     "A", "OSC", "easy",
     "\\((x - 9)(x - 7) = 0 \\implies x = 9\\) or \\(x = 7\\)."),

    # 53
    ("Solve: \\(x^2 + 15x + 56 = 0\\).",
     ["\\(-8\\) and \\(-7\\)", "\\(8\\) and \\(7\\)", "\\(-14\\) and \\(-4\\)", "\\(14\\) and \\(4\\)"],
     "A", "OSC", "easy",
     "\\((x + 8)(x + 7) = 0 \\implies x = -8\\) or \\(x = -7\\)."),

    # 54
    ("Solve: \\(x^2 - 17x + 72 = 0\\).",
     ["\\(9\\) and \\(8\\)", "\\(-9\\) and \\(-8\\)", "\\(12\\) and \\(6\\)", "\\(-12\\) and \\(-6\\)"],
     "A", "OSC", "easy",
     "\\((x - 9)(x - 8) = 0 \\implies x = 9\\) or \\(x = 8\\)."),

    # 55
    ("Solve: \\(x^2 - 19x + 90 = 0\\).",
     ["\\(10\\) and \\(9\\)", "\\(-10\\) and \\(-9\\)", "\\(15\\) and \\(6\\)", "\\(-15\\) and \\(-6\\)"],
     "A", "OSC", "easy",
     "\\((x - 10)(x - 9) = 0 \\implies x = 10\\) or \\(x = 9\\)."),

    # 56
    ("Solve: \\(2x^2 - 7x + 6 = 0\\).",
     ["\\(2\\) and \\(\\frac{3}{2}\\)",
      "\\(-2\\) and \\(-\\frac{3}{2}\\)",
      "\\(4\\) and \\(3\\)",
      "\\(1\\) and \\(6\\)"],
     "A", "OSC", "medium",
     "Product is 12, sum is \\(-7\\). Numbers are \\(-4\\) and \\(-3\\). \\(2x(x - 2) - 3(x - 2) = 0 \\implies (2x - 3)(x - 2) = 0 \\implies x = 2\\) or \\(x = 3/2\\)."),

    # 57
    ("Solve: \\(3x^2 + 7x + 2 = 0\\).",
     ["\\(-2\\) and \\(-\\frac{1}{3}\\)",
      "\\(2\\) and \\(\\frac{1}{3}\\)",
      "\\(-1\\) and \\(-6\\)",
      "\\(-3\\) and \\(-2\\)"],
     "A", "OSC", "medium",
     "Product is 6, sum is 7. Numbers are 6 and 1. \\(3x(x + 2) + 1(x + 2) = 0 \\implies (3x + 1)(x + 2) = 0 \\implies x = -2\\) or \\(x = -1/3\\)."),

    # 58
    ("Solve: \\(x^2 - 25 = 0\\).",
     ["\\(5\\) and \\(-5\\)", "\\(25\\) and \\(-25\\)", "\\(0\\) and \\(5\\)", "\\(10\\) and \\(-10\\)"],
     "A", "OSC", "easy",
     "\\(x = \\pm 5\\)."),

    # 59
    ("Solve: \\(x^2 - 36 = 0\\).",
     ["\\(6\\) and \\(-6\\)", "\\(36\\) and \\(-36\\)", "\\(18\\) and \\(-18\\)", "\\(0\\) and \\(6\\)"],
     "A", "OSC", "easy",
     "\\(x = \\pm 6\\)."),

    # 60
    ("Solve: \\(x^2 - 64 = 0\\).",
     ["\\(8\\) and \\(-8\\)", "\\(64\\) and \\(-64\\)", "\\(16\\) and \\(-16\\)", "\\(0\\) and \\(8\\)"],
     "A", "OSC", "easy",
     "\\(x = \\pm 8\\)."),

    # 61
    ("Solve: \\(x^2 - 81 = 0\\).",
     ["\\(9\\) and \\(-9\\)", "\\(81\\) and \\(-81\\)", "\\(27\\) and \\(-27\\)", "\\(0\\) and \\(9\\)"],
     "A", "OSC", "easy",
     "\\(x = \\pm 9\\)."),

    # 62
    ("Solve: \\(x^2 - 4x + 4 = 0\\).",
     ["\\(2\\) (repeated root)", "\\(-2\\) (repeated root)", "\\(4\\) and \\(1\\)", "\\(-4\\) and \\(-1\\)"],
     "A", "OSC", "easy",
     "\\((x - 2)^2 = 0 \\implies x = 2\\)."),

    # 63
    ("Solve: \\(x^2 + 10x + 25 = 0\\).",
     ["\\(-5\\) (repeated root)", "\\(5\\) (repeated root)", "\\(25\\) and \\(1\\)", "\\(-25\\) and \\(-1\\)"],
     "A", "OSC", "easy",
     "\\((x + 5)^2 = 0 \\implies x = -5\\)."),

    # 64
    ("Solve: \\(x^2 + 12x + 36 = 0\\).",
     ["\\(-6\\) (repeated root)", "\\(6\\) (repeated root)", "\\(12\\) and \\(3\\)", "\\(9\\) and \\(4\\)"],
     "A", "OSC", "easy",
     "\\((x + 6)^2 = 0 \\implies x = -6\\)."),

    # 65
    ("Solve: \\(x^2 - 16x + 64 = 0\\).",
     ["\\(8\\) (repeated root)", "\\(-8\\) (repeated root)", "\\(16\\) and \\(4\\)", "\\(64\\) and \\(1\\)"],
     "A", "OSC", "easy",
     "\\((x - 8)^2 = 0 \\implies x = 8\\)."),

    # 66
    ("Solve: \\(x^2 + 18x + 81 = 0\\).",
     ["\\(-9\\) (repeated root)", "\\(9\\) (repeated root)", "\\(27\\) and \\(3\\)", "\\(81\\) and \\(1\\)"],
     "A", "OSC", "easy",
     "\\((x + 9)^2 = 0 \\implies x = -9\\)."),

    # 67
    ("Solve: \\(x^2 - 20x + 100 = 0\\).",
     ["\\(10\\) (repeated root)", "\\(-10\\) (repeated root)", "\\(20\\) and \\(5\\)", "\\(50\\) and \\(2\\)"],
     "A", "OSC", "easy",
     "\\((x - 10)^2 = 0 \\implies x = 10\\)."),

    # 68
    ("Solve: \\(x^2 - 7 = 0\\).",
     ["\\(\\sqrt{7}\\) and \\(-\\sqrt{7}\\)", "\\(7\\) and \\(-7\\)", "\\(49\\) and \\(-49\\)", "\\(3.5\\) and \\(-3.5\\)"],
     "A", "OSC", "easy",
     "\\(x = \\pm \\sqrt{7}\\)."),

    # 69
    ("Solve: \\(x^2 - 5 = 0\\).",
     ["\\(\\sqrt{5}\\) and \\(-\\sqrt{5}\\)", "\\(5\\) and \\(-5\\)", "\\(25\\) and \\(-25\\)", "\\(2.5\\) and \\(-2.5\\)"],
     "A", "OSC", "easy",
     "\\(x = \\pm \\sqrt{5}\\)."),

    # 70
    ("Solve: \\(x^2 - 3 = 0\\).",
     ["\\(\\sqrt{3}\\) and \\(-\\sqrt{3}\\)", "\\(3\\) and \\(-3\\)", "\\(9\\) and \\(-9\\)", "\\(1.5\\) and \\(-1.5\\)"],
     "A", "OSC", "easy",
     "\\(x = \\pm \\sqrt{3}\\).")
]

# 12 MOCK (71-82)
mock_data = [
    # 71
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0f172a" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Splitting the Middle Term</text>
  <text x="170" y="80" fill="#f8fafc" font-size="11" text-anchor="middle">ax² + bx + c = 0</text>
  <text x="170" y="105" fill="#4ade80" font-size="11" text-anchor="middle">Find p, q such that: p * q = a * c and p + q = b</text>
</svg>
</div>
What two algebraic conditions must be satisfied when choosing numbers \\(p\\) and \\(q\\) to split the middle term \\(b\\)?""",
     ["Their product must equal a * c and their algebraic sum must equal b",
      "Their product must equal b and their sum must equal a * c",
      "Both numbers must be positive primes",
      "Their difference must equal 0"],
     "A", "OSC", "easy",
     "When factorising \\(ax^2 + bx + c = 0\\), we decompose the linear term \\(bx\\) into \\(px + qx\\) where \\(p \\times q = a \\times c\\) and \\(p + q = b\\)."),

    # 72
    ("Factorise \\(x^2 - 9 = 0\\). What are the roots?",
     ["\\(3\\) and \\(-3\\)", "\\(9\\) and \\(-9\\)", "\\(0\\) and \\(3\\)", "\\(1\\) and \\(-9\\)"],
     "A", "OSC", "easy",
     "\\((x - 3)(x + 3) = 0 \\implies x = \\pm 3\\)."),

    # 73
    ("Factorise \\(x^2 - 2x + 1 = 0\\). What are the roots?",
     ["\\(1\\) (repeated root)", "\\(-1\\) (repeated root)", "\\(2\\) and \\(1\\)", "\\(0\\) and \\(2\\)"],
     "A", "OSC", "easy",
     "\\((x - 1)^2 = 0 \\implies x = 1\\)."),

    # 74
    ("Factorise \\(x^2 + 2x + 1 = 0\\). What are the roots?",
     ["\\(-1\\) (repeated root)", "\\(1\\) (repeated root)", "\\(-2\\) and \\(-1\\)", "\\(0\\) and \\(-1\\)"],
     "A", "OSC", "easy",
     "\\((x + 1)^2 = 0 \\implies x = -1\\)."),

    # 75
    ("Factorise \\(x^2 - 4 = 0\\). What are the roots?",
     ["\\(2\\) and \\(-2\\)", "\\(4\\) and \\(-4\\)", "\\(0\\) and \\(2\\)", "\\(1\\) and \\(-4\\)"],
     "A", "OSC", "easy",
     "\\(x = \\pm 2\\)."),

    # 76
    ("Solve: \\(x^2 - 6x + 8 = 0\\).",
     ["\\(4\\) and \\(2\\)", "\\(-4\\) and \\(-2\\)", "\\(8\\) and \\(1\\)", "\\(-8\\) and \\(-1\\)"],
     "A", "OSC", "easy",
     "\\((x - 4)(x - 2) = 0 \\implies x = 4\\) or \\(x = 2\\)."),

    # 77
    ("Solve: \\(x^2 - x - 2 = 0\\).",
     ["\\(2\\) and \\(-1\\)", "\\(-2\\) and \\(1\\)", "\\(1\\) and \\(-2\\)", "\\(0\\) and \\(2\\)"],
     "A", "OSC", "easy",
     "\\((x - 2)(x + 1) = 0 \\implies x = 2\\) or \\(x = -1\\)."),

    # 78
    ("Solve: \\(x^2 + x - 2 = 0\\).",
     ["\\(-2\\) and \\(1\\)", "\\(2\\) and \\(-1\\)", "\\(-1\\) and \\(-2\\)", "\\(0\\) and \\(-2\\)"],
     "A", "OSC", "easy",
     "\\((x + 2)(x - 1) = 0 \\implies x = -2\\) or \\(x = 1\\)."),

    # 79
    ("Solve: \\(x^2 - 3x + 2 = 0\\).",
     ["\\(2\\) and \\(1\\)", "\\(-2\\) and \\(-1\\)", "\\(3\\) and \\(1\\)", "\\(-3\\) and \\(-1\\)"],
     "A", "OSC", "easy",
     "\\((x - 2)(x - 1) = 0 \\implies x = 2\\) or \\(x = 1\\)."),

    # 80
    ("Solve: \\(x^2 + 3x + 2 = 0\\).",
     ["\\(-2\\) and \\(-1\\)", "\\(2\\) and \\(1\\)", "\\(-3\\) and \\(1\\)", "\\(3\\) and \\(-1\\)"],
     "A", "OSC", "easy",
     "\\((x + 2)(x + 1) = 0 \\implies x = -2\\) or \\(x = -1\\)."),

    # 81
    ("If a quadratic equation is \\((x - p)(x - q) = 0\\), what are its roots?",
     ["\\(x = p\\) and \\(x = q\\)",
      "\\(x = -p\\) and \\(x = -q\\)",
      "\\(x = p + q\\)",
      "\\(x = pq\\)"],
     "A", "OSC", "easy",
     "Setting each factor to zero: \\(x - p = 0 \\implies x = p\\), and \\(x - q = 0 \\implies x = q\\)."),

    # 82
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0b132b" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1c2541" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Summary: Factorisation Method</text>
  <text x="170" y="80" fill="#f8fafc" font-size="11" text-anchor="middle">Express as (x - α)(x - β) = 0</text>
  <text x="170" y="105" fill="#4ade80" font-size="11" text-anchor="middle">Apply Zero Product Property -> Roots are α, β</text>
</svg>
</div>
Why must common factors (such as x) NOT be cancelled by dividing both sides of an equation like \\(7m^2 = 21m\\)?""",
     ["Because dividing by a variable expression assumes it is non-zero, thereby illegally eliminating the root m = 0",
      "Because 7 is not divisible by 21",
      "Because the equation becomes cubic",
      "Because roots would become negative"],
     "A", "OSC", "easy",
     "Dividing both sides by an unknown variable expression \\(m\\) assumes \\(m \\neq 0\\). If \\(m = 0\\) is actually a valid root, dividing by \\(m\\) commits division by zero and destroys that solution.")
]

all_q_22 = build_topic_questions(TOPIC_CODE, exam_data, practice_data, mock_data)
out_22 = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch2_t2.json")
with open(out_22, "w", encoding="utf-8") as f:
    json.dump(all_q_22, f, indent=2, ensure_ascii=False)
print(f"Generated {len(all_q_22)} questions for {TOPIC_CODE} -> {out_22}")
