# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 2: Quadratic Equations (Topics 2.5 & 2.6)
Each topic: exactly 82 canonical questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# ==============================================================================
# TOPIC 2.5: Nature of Roots & Discriminant (MH-10-MTH1-2-2.5)
# ==============================================================================
t25_exam = [
    # 1
    ("What determines the nature of the roots of the quadratic equation \\(ax^2 + bx + c = 0\\)?",
     ["The value of the discriminant \\(\\Delta = b^2 - 4ac\\)",
      "The value of the leading coefficient a only",
      "The constant term c only",
      "The sum of coefficients a + b + c"],
     "A", "OSC", "easy",
     "The expression \\(b^2 - 4ac\\) is called the discriminant because its sign (positive, zero, or negative) discriminates the nature of the roots."),

    # 2
    ("If \\(\\Delta = b^2 - 4ac > 0\\), what is the nature of the roots?",
     ["Real and unequal (distinct)",
      "Real and equal",
      "Not real (complex conjugates)",
      "Zero"],
     "A", "OSC", "easy",
     "When \\(\\Delta > 0\\), \\(\\sqrt{\\Delta}\\) is a non-zero real number, resulting in two distinct real roots \\(\\frac{-b + \\sqrt{\\Delta}}{2a}\\) and \\(\\frac{-b - \\sqrt{\\Delta}}{2a}\\)."),

    # 3
    ("If \\(\\Delta = b^2 - 4ac = 0\\), what is the nature of the roots?",
     ["Real and equal (coincident roots)",
      "Real and unequal",
      "Not real",
      "Undefined"],
     "A", "OSC", "easy",
     "When \\(\\Delta = 0\\), the \\(\\pm \\sqrt{\\Delta}\\) term vanishes, giving two equal real roots: \\(x_1 = x_2 = -\\frac{b}{2a}\\)."),

    # 4
    ("If \\(\\Delta = b^2 - 4ac < 0\\), what is the nature of the roots?",
     ["Not real (roots are imaginary/complex conjugates)",
      "Real and equal",
      "Real and unequal",
      "Rational and equal"],
     "A", "OSC", "easy",
     "The square root of a negative number is not a real number. Therefore, when \\(\\Delta < 0\\), the roots are not real."),

    # 5
    ("Determine the nature of the roots of \\(x^2 + 7x - 1 = 0\\).",
     ["Real and unequal, because \\(\\Delta = 53 > 0\\)",
      "Real and equal, because \\(\\Delta = 0\\)",
      "Not real, because \\(\\Delta < 0\\)",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(a = 1, b = 7, c = -1\\). \\(\\Delta = b^2 - 4ac = 7^2 - 4(1)(-1) = 49 + 4 = 53\\). Since \\(\\Delta > 0\\), the roots are real and unequal."),

    # 6
    ("Determine the nature of the roots of \\(2y^2 - 5y + 10 = 0\\).",
     ["Not real, because \\(\\Delta = -55 < 0\\)",
      "Real and unequal, because \\(\\Delta > 0\\)",
      "Real and equal, because \\(\\Delta = 0\\)",
      "Rational and equal"],
     "A", "OSC", "easy",
     "\\(a = 2, b = -5, c = 10\\). \\(\\Delta = (-5)^2 - 4(2)(10) = 25 - 80 = -55\\). Since \\(\\Delta < 0\\), the roots are not real."),

    # 7
    ("Determine the nature of the roots of \\(\\sqrt{2}x^2 + 4x + 2\\sqrt{2} = 0\\).",
     ["Real and equal, because \\(\\Delta = 0\\)",
      "Real and unequal, because \\(\\Delta > 0\\)",
      "Not real, because \\(\\Delta < 0\\)",
      "Irrational and unequal"],
     "A", "OSC", "medium",
     "\\(a = \\sqrt{2}, b = 4, c = 2\\sqrt{2}\\). \\(\\Delta = 4^2 - 4(\\sqrt{2})(2\\sqrt{2}) = 16 - 4(4) = 16 - 16 = 0\\). Since \\(\\Delta = 0\\), roots are real and equal."),

    # 8
    ("Find the value of \\(k\\) for which \\(3y^2 + ky + 12 = 0\\) has real and equal roots.",
     ["\\(\\pm 12\\)", "\\(12\\) only", "\\(\\pm 6\\)", "\\(144\\)"],
     "A", "OSC", "medium",
     "For real and equal roots, \\(\\Delta = 0 \\implies k^2 - 4(3)(12) = 0 \\implies k^2 - 144 = 0 \\implies k^2 = 144 \\implies k = \\pm 12\\)."),

    # 9
    ("Find the value of \\(k\\) for which \\(kx(x - 2) + 6 = 0\\) has real and equal roots (where \\(k \\neq 0\\)).",
     ["6", "0", "4", "-6"],
     "A", "OSC", "medium",
     "\\(kx^2 - 2kx + 6 = 0\\). Here \\(a = k, b = -2k, c = 6\\). For equal roots: \\((-2k)^2 - 4(k)(6) = 0 \\implies 4k^2 - 24k = 0 \\implies 4k(k - 6) = 0\\). Since \\(k \\neq 0\\) (otherwise not quadratic), \\(k = 6\\)."),

    # 10
    ("If \\(b^2 - 4ac\\) is a perfect square and \\(a, b, c\\) are rational numbers, what is the nature of the roots?",
     ["Real, rational, and unequal (if \\(\\Delta > 0\\))",
      "Real, irrational, and unequal",
      "Not real",
      "Equal to zero"],
     "A", "OSC", "medium",
     "When \\(\\Delta\\) is a perfect square of a rational number, \\(\\sqrt{\\Delta}\\) is rational, making both roots rational."),

    # 11
    ("If \\(b^2 - 4ac > 0\\) but is NOT a perfect square (with rational coefficients), what is the nature of the roots?",
     ["Real, irrational, and unequal, occurring in conjugate surd pairs \\(p \\pm \\sqrt{q}\\)",
      "Real and rational",
      "Real and equal",
      "Not real"],
     "A", "OSC", "medium",
     "Because \\(\\sqrt{\\Delta}\\) cannot be simplified to a rational number, the roots are irrational and occur as conjugate surd pairs \\(p + \\sqrt{q}\\) and \\(p - \\sqrt{q}\\)."),

    # 12
    ("Find \\(\\Delta\\) for \\(x^2 - 4x + 4 = 0\\) and state the nature of roots.",
     ["\\(\\Delta = 0\\); roots are real and equal",
      "\\(\\Delta = 16\\); roots are real and unequal",
      "\\(\\Delta = -16\\); roots are not real",
      "\\(\\Delta = 4\\); roots are real and unequal"],
     "A", "OSC", "easy",
     "\\(\\Delta = (-4)^2 - 4(1)(4) = 16 - 16 = 0\\). Roots are real and equal."),

    # 13
    ("Find \\(\\Delta\\) for \\(x^2 - 5x + 6 = 0\\) and state the nature of roots.",
     ["\\(\\Delta = 1\\); roots are real, rational, and unequal",
      "\\(\\Delta = 0\\); roots are real and equal",
      "\\(\\Delta = -1\\); roots are not real",
      "\\(\\Delta = 25\\); roots are real and unequal"],
     "A", "OSC", "easy",
     "\\(\\Delta = 25 - 24 = 1 > 0\\) (perfect square). Roots are real, rational, and unequal."),

    # 14
    ("Find \\(\\Delta\\) for \\(x^2 + 2x + 5 = 0\\) and state the nature of roots.",
     ["\\(\\Delta = -16\\); roots are not real",
      "\\(\\Delta = 16\\); roots are real and unequal",
      "\\(\\Delta = 0\\); roots are real and equal",
      "\\(\\Delta = -4\\); roots are not real"],
     "A", "OSC", "easy",
     "\\(\\Delta = 4 - 4(1)(5) = 4 - 20 = -16 < 0\\). Roots are not real."),

    # 15
    ("For what value of \\(k\\) will \\(x^2 - kx + 9 = 0\\) have equal roots?",
     ["\\(\\pm 6\\)", "\\(6\\) only", "\\(\\pm 9\\)", "\\(3\\)"],
     "A", "OSC", "easy",
     "\\((-k)^2 - 4(1)(9) = 0 \\implies k^2 - 36 = 0 \\implies k = \\pm 6\\)."),

    # 16
    ("For what value of \\(k\\) will \\(2x^2 + kx + 2 = 0\\) have equal roots?",
     ["\\(\\pm 4\\)", "\\(4\\) only", "\\(\\pm 2\\)", "\\(\\pm 8\\)"],
     "A", "OSC", "easy",
     "\\(k^2 - 4(2)(2) = 0 \\implies k^2 - 16 = 0 \\implies k = \\pm 4\\)."),

    # 17
    ("For what value of \\(k\\) will \\(4x^2 - kx + 1 = 0\\) have equal roots?",
     ["\\(\\pm 4\\)", "\\(4\\) only", "\\(\\pm 1\\)", "\\(\\pm 2\\)"],
     "A", "OSC", "easy",
     "\\(k^2 - 4(4)(1) = 0 \\implies k^2 = 16 \\implies k = \\pm 4\\)."),

    # 18
    ("For what value of \\(k\\) will \\(9x^2 + kx + 4 = 0\\) have equal roots?",
     ["\\(\\pm 12\\)", "\\(12\\) only", "\\(\\pm 6\\)", "\\(\\pm 36\\)"],
     "A", "OSC", "easy",
     "\\(k^2 - 4(9)(4) = 0 \\implies k^2 - 144 = 0 \\implies k = \\pm 12\\)."),

    # 19
    ("If the roots of \\(px^2 - 4x + 2 = 0\\) are real and equal, find \\(p\\).",
     ["2", "4", "1", "0.5"],
     "A", "OSC", "easy",
     "\\((-4)^2 - 4(p)(2) = 0 \\implies 16 - 8p = 0 \\implies 8p = 16 \\implies p = 2\\)."),

    # 20
    ("If the roots of \\(3x^2 - 6x + k = 0\\) are real and equal, find \\(k\\).",
     ["3", "6", "9", "1"],
     "A", "OSC", "easy",
     "\\((-6)^2 - 4(3)(k) = 0 \\implies 36 - 12k = 0 \\implies 12k = 36 \\implies k = 3\\)."),

    # 21
    ("What can be said about the roots of \\(ax^2 + bx + c = 0\\) if \\(ac < 0\\)?",
     ["Roots are definitely real and unequal, because \\(-4ac > 0\\), making \\(\\Delta = b^2 - 4ac > 0\\)",
      "Roots are not real",
      "Roots are equal to zero",
      "Roots are coincident"],
     "A", "OSC", "medium",
     "If \\(ac < 0\\), then \\(-4ac > 0\\). Since \\(b^2 \\ge 0\\), the discriminant \\(b^2 - 4ac\\) is strictly positive, guaranteeing two distinct real roots."),

    # 22
    ("Find the value of \\(\\Delta\\) for \\(x^2 - 4\\sqrt{3}x + 12 = 0\\).",
     ["0", "12", "24", "-12"],
     "A", "OSC", "medium",
     "\\(\\Delta = (-4\\sqrt{3})^2 - 4(1)(12) = (16 \\times 3) - 48 = 48 - 48 = 0\\). Roots are real and equal."),

    # 23
    ("From the previous question, what are the equal roots?",
     ["\\(2\\sqrt{3}\\)", "\\(-2\\sqrt{3}\\)", "\\(4\\sqrt{3}\\)", "\\(3\\)"],
     "A", "OSC", "easy",
     "\\(x = -b/(2a) = -(-4\\sqrt{3}) / 2 = 2\\sqrt{3}\\)."),

    # 24
    ("Determine the nature of roots of \\(2x^2 - 6x + 3 = 0\\).",
     ["Real, irrational, and unequal (\\(\\Delta = 12\\))",
      "Real, rational, and unequal",
      "Real and equal",
      "Not real"],
     "A", "OSC", "medium",
     "\\(\\Delta = 36 - 4(2)(3) = 36 - 24 = 12 > 0\\). Since 12 is not a perfect square, roots are real, irrational, and unequal."),

    # 25
    ("Determine the nature of roots of \\(3x^2 - 4\\sqrt{3}x + 4 = 0\\).",
     ["Real and equal (\\(\\Delta = 0\\))",
      "Real and unequal",
      "Not real",
      "Zero"],
     "A", "OSC", "medium",
     "\\(\\Delta = (-4\\sqrt{3})^2 - 4(3)(4) = 48 - 48 = 0\\). Roots are real and equal."),

    # 26
    ("From the previous question, what is the repeated root?",
     ["\\(\\frac{2}{\\sqrt{3}}\\) (or \\(\\frac{2\\sqrt{3}}{3}\\))",
      "\\(\\sqrt{3}\\)",
      "\\(\\frac{4}{3}\\)",
      "\\(2\\sqrt{3}\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{4\\sqrt{3}}{2(3)} = \\frac{2\\sqrt{3}}{3} = \\frac{2}{\\sqrt{3}}\\)."),

    # 27
    ("Determine the nature of roots of \\(2x^2 - 3x + 5 = 0\\).",
     ["Not real (\\(\\Delta = -31 < 0\\))",
      "Real and equal",
      "Real and unequal",
      "Rational and equal"],
     "A", "OSC", "easy",
     "\\(\\Delta = (-3)^2 - 4(2)(5) = 9 - 40 = -31 < 0\\). Roots are not real."),

    # 28
    ("If \\(k\\) is positive, for what value of \\(k\\) does \\(x^2 - kx + 16 = 0\\) have equal roots?",
     ["8", "4", "16", "2"],
     "A", "OSC", "easy",
     "\\(k^2 - 64 = 0 \\implies k = 8\\) (since \\(k > 0\\))."),

    # 29
    ("If \\(k\\) is positive, for what value of \\(k\\) does \\(x^2 - kx + 25 = 0\\) have equal roots?",
     ["10", "5", "25", "20"],
     "A", "OSC", "easy",
     "\\(k^2 - 100 = 0 \\implies k = 10\\)."),

    # 30
    ("If \\(k\\) is positive, for what value of \\(k\\) does \\(x^2 - kx + 36 = 0\\) have equal roots?",
     ["12", "6", "36", "18"],
     "A", "OSC", "easy",
     "\\(k^2 - 144 = 0 \\implies k = 12\\)."),

    # 31
    ("If \\(k\\) is positive, for what value of \\(k\\) does \\(x^2 - kx + 49 = 0\\) have equal roots?",
     ["14", "7", "49", "21"],
     "A", "OSC", "easy",
     "\\(k^2 - 196 = 0 \\implies k = 14\\)."),

    # 32
    ("If \\(k\\) is positive, for what value of \\(k\\) does \\(x^2 - kx + 64 = 0\\) have equal roots?",
     ["16", "8", "64", "32"],
     "A", "OSC", "easy",
     "\\(k^2 - 256 = 0 \\implies k = 16\\)."),

    # 33
    ("If \\(k\\) is positive, for what value of \\(k\\) does \\(x^2 - kx + 81 = 0\\) have equal roots?",
     ["18", "9", "81", "27"],
     "A", "OSC", "easy",
     "\\(k^2 - 324 = 0 \\implies k = 18\\)."),

    # 34
    ("If \\(k\\) is positive, for what value of \\(k\\) does \\(x^2 - kx + 100 = 0\\) have equal roots?",
     ["20", "10", "100", "50"],
     "A", "OSC", "easy",
     "\\(k^2 - 400 = 0 \\implies k = 20\\)."),

    # 35
    ("What is the graphical interpretation of \\(\\Delta > 0\\) for the parabola \\(y = ax^2 + bx + c\\)?",
     ["The parabola intersects the X-axis at two distinct points",
      "The parabola touches the X-axis at exactly one point",
      "The parabola does not intersect or touch the X-axis",
      "The parabola passes through the origin"],
     "A", "OSC", "medium",
     "When \\(\\Delta > 0\\), there are two distinct real roots, meaning the graph crosses the X-axis at two distinct points \\((x_1, 0)\\) and \\((x_2, 0)\\)."),

    # 36
    ("What is the graphical interpretation of \\(\\Delta = 0\\)?",
     ["The parabola touches the X-axis at exactly one point (the vertex lies on the X-axis)",
      "The parabola crosses the X-axis at two points",
      "The parabola lies entirely above or below the X-axis",
      "The graph is a straight line"],
     "A", "OSC", "medium",
     "When \\(\\Delta = 0\\), the two roots coincide, meaning the parabola is tangent to the X-axis at its vertex."),

    # 37
    ("What is the graphical interpretation of \\(\\Delta < 0\\)?",
     ["The parabola does not intersect or touch the X-axis (lies entirely above or below it)",
      "The parabola crosses the X-axis at origin",
      "The parabola intersects the X-axis at two points",
      "The vertex is at (0, 0)"],
     "A", "OSC", "medium",
     "When \\(\\Delta < 0\\), there are no real roots, so the curve never touches or crosses the line \\(y = 0\\)."),

    # 38
    ("If \\(b = 0\\) and \\(a, c\\) have the same sign (both positive or both negative), what is the nature of the roots?",
     ["Not real (\\(\\Delta = -4ac < 0\\))",
      "Real and equal",
      "Real and unequal",
      "Zero"],
     "A", "OSC", "easy",
     "\\(\\Delta = 0 - 4ac = -4ac\\). Since \\(a\\) and \\(c\\) have the same sign, \\(ac > 0\\), making \\(-4ac < 0\\). Thus roots are not real."),

    # 39
    ("If \\(b = 0\\) and \\(a, c\\) have opposite signs, what is the nature of the roots?",
     ["Real, unequal, and symmetric: \\(\\pm \\sqrt{-c/a}\\)",
      "Not real",
      "Real and equal",
      "Zero"],
     "A", "OSC", "easy",
     "\\(ax^2 + c = 0 \\implies x^2 = -c/a\\). Since signs are opposite, \\(-c/a > 0\\), giving real roots \\(\\pm \\sqrt{-c/a}\\)."),

    # 40
    ("State whether \\(x^2 + 1 = 0\\) has real roots.",
     ["No real roots, because \\(\\Delta = -4 < 0\\) (and \\(x^2 = -1\\))",
      "Yes, 1 and -1",
      "Yes, 1 only",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(\\Delta = 0^2 - 4(1)(1) = -4 < 0\\). No real number squared can equal \\(-1\\).")
]

t25_prac = [
    # 41
    ("Find \\(\\Delta\\) for \\(x^2 - 2x + 1 = 0\\).", ["0", "4", "-4", "1"], "A", "OSC", "easy", "\\(4 - 4 = 0\\)."),
    # 42
    ("Find \\(\\Delta\\) for \\(x^2 - 4x + 3 = 0\\).", ["4", "16", "12", "0"], "A", "OSC", "easy", "\\(16 - 12 = 4\\)."),
    # 43
    ("Find \\(\\Delta\\) for \\(x^2 - 6x + 8 = 0\\).", ["4", "36", "32", "0"], "A", "OSC", "easy", "\\(36 - 32 = 4\\)."),
    # 44
    ("Find \\(\\Delta\\) for \\(x^2 - 8x + 15 = 0\\).", ["4", "64", "60", "0"], "A", "OSC", "easy", "\\(64 - 60 = 4\\)."),
    # 45
    ("Find \\(\\Delta\\) for \\(x^2 - 10x + 24 = 0\\).", ["4", "100", "96", "0"], "A", "OSC", "easy", "\\(100 - 96 = 4\\)."),
    # 46
    ("Find \\(\\Delta\\) for \\(x^2 - 12x + 35 = 0\\).", ["4", "144", "140", "0"], "A", "OSC", "easy", "\\(144 - 140 = 4\\)."),
    # 47
    ("Find \\(\\Delta\\) for \\(x^2 - 14x + 48 = 0\\).", ["4", "196", "192", "0"], "A", "OSC", "easy", "\\(196 - 192 = 4\\)."),
    # 48
    ("Find \\(\\Delta\\) for \\(x^2 - 16x + 63 = 0\\).", ["4", "256", "252", "0"], "A", "OSC", "easy", "\\(256 - 252 = 4\\)."),
    # 49
    ("Find \\(\\Delta\\) for \\(x^2 - 18x + 80 = 0\\).", ["4", "324", "320", "0"], "A", "OSC", "easy", "\\(324 - 320 = 4\\)."),
    # 50
    ("Find \\(\\Delta\\) for \\(x^2 - 20x + 99 = 0\\).", ["4", "400", "396", "0"], "A", "OSC", "easy", "\\(400 - 396 = 4\\)."),
    # 51
    ("Find \\(\\Delta\\) for \\(x^2 + 2x + 1 = 0\\).", ["0", "4", "-4", "1"], "A", "OSC", "easy", "\\(4 - 4 = 0\\)."),
    # 52
    ("Find \\(\\Delta\\) for \\(x^2 + 4x + 3 = 0\\).", ["4", "16", "12", "0"], "A", "OSC", "easy", "\\(16 - 12 = 4\\)."),
    # 53
    ("Find \\(\\Delta\\) for \\(x^2 + 6x + 8 = 0\\).", ["4", "36", "32", "0"], "A", "OSC", "easy", "\\(36 - 32 = 4\\)."),
    # 54
    ("Find \\(\\Delta\\) for \\(x^2 + 8x + 15 = 0\\).", ["4", "64", "60", "0"], "A", "OSC", "easy", "\\(64 - 60 = 4\\)."),
    # 55
    ("Find \\(\\Delta\\) for \\(x^2 + 10x + 24 = 0\\).", ["4", "100", "96", "0"], "A", "OSC", "easy", "\\(100 - 96 = 4\\)."),
    # 56
    ("Find \\(\\Delta\\) for \\(x^2 + 12x + 35 = 0\\).", ["4", "144", "140", "0"], "A", "OSC", "easy", "\\(144 - 140 = 4\\)."),
    # 57
    ("Find \\(\\Delta\\) for \\(x^2 + 14x + 48 = 0\\).", ["4", "196", "192", "0"], "A", "OSC", "easy", "\\(196 - 192 = 4\\)."),
    # 58
    ("Find \\(\\Delta\\) for \\(x^2 + 16x + 63 = 0\\).", ["4", "256", "252", "0"], "A", "OSC", "easy", "\\(256 - 252 = 4\\)."),
    # 59
    ("Find \\(\\Delta\\) for \\(x^2 + 18x + 80 = 0\\).", ["4", "324", "320", "0"], "A", "OSC", "easy", "\\(324 - 320 = 4\\)."),
    # 60
    ("Find \\(\\Delta\\) for \\(x^2 + 20x + 99 = 0\\).", ["4", "400", "396", "0"], "A", "OSC", "easy", "\\(400 - 396 = 4\\)."),
    # 61
    ("Find \\(k\\) for equal roots: \\(x^2 + kx + 1 = 0\\).", ["\\(\\pm 2\\)", "\\(2\\) only", "\\(\\pm 4\\)", "\\(1\\)"], "A", "OSC", "easy", "\\(k^2 - 4 = 0 \\implies k = \\pm 2\\)."),
    # 62
    ("Find \\(k\\) for equal roots: \\(x^2 + kx + 4 = 0\\).", ["\\(\\pm 4\\)", "\\(4\\) only", "\\(\\pm 2\\)", "\\(16\\)"], "A", "OSC", "easy", "\\(k^2 - 16 = 0 \\implies k = \\pm 4\\)."),
    # 63
    ("Find \\(k\\) for equal roots: \\(x^2 + kx + 9 = 0\\).", ["\\(\\pm 6\\)", "\\(6\\) only", "\\(\\pm 3\\)", "\\(36\\)"], "A", "OSC", "easy", "\\(k^2 - 36 = 0 \\implies k = \\pm 6\\)."),
    # 64
    ("Find \\(k\\) for equal roots: \\(x^2 + kx + 16 = 0\\).", ["\\(\\pm 8\\)", "\\(8\\) only", "\\(\\pm 4\\)", "\\(64\\)"], "A", "OSC", "easy", "\\(k^2 - 64 = 0 \\implies k = \\pm 8\\)."),
    # 65
    ("Find \\(k\\) for equal roots: \\(x^2 + kx + 25 = 0\\).", ["\\(\\pm 10\\)", "\\(10\\) only", "\\(\\pm 5\\)", "\\(100\\)"], "A", "OSC", "easy", "\\(k^2 - 100 = 0 \\implies k = \\pm 10\\)."),
    # 66
    ("Find \\(k\\) for equal roots: \\(x^2 + kx + 36 = 0\\).", ["\\(\\pm 12\\)", "\\(12\\) only", "\\(\\pm 6\\)", "\\(144\\)"], "A", "OSC", "easy", "\\(k^2 - 144 = 0 \\implies k = \\pm 12\\)."),
    # 67
    ("Find \\(k\\) for equal roots: \\(x^2 + kx + 49 = 0\\).", ["\\(\\pm 14\\)", "\\(14\\) only", "\\(\\pm 7\\)", "\\(196\\)"], "A", "OSC", "easy", "\\(k^2 - 196 = 0 \\implies k = \\pm 14\\)."),
    # 68
    ("Find \\(k\\) for equal roots: \\(x^2 + kx + 64 = 0\\).", ["\\(\\pm 16\\)", "\\(16\\) only", "\\(\\pm 8\\)", "\\(256\\)"], "A", "OSC", "easy", "\\(k^2 - 256 = 0 \\implies k = \\pm 16\\)."),
    # 69
    ("Find \\(k\\) for equal roots: \\(x^2 + kx + 81 = 0\\).", ["\\(\\pm 18\\)", "\\(18\\) only", "\\(\\pm 9\\)", "\\(324\\)"], "A", "OSC", "easy", "\\(k^2 - 324 = 0 \\implies k = \\pm 18\\)."),
    # 70
    ("Find \\(k\\) for equal roots: \\(x^2 + kx + 100 = 0\\).", ["\\(\\pm 20\\)", "\\(20\\) only", "\\(\\pm 10\\)", "\\(400\\)"], "A", "OSC", "easy", "\\(k^2 - 400 = 0 \\implies k = \\pm 20\\).")
]

t25_mock = [
    # 71
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0f172a" rx="8"/>
  <rect x="15" y="25" width="95" height="100" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="1.5"/>
  <text x="62" y="55" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">Δ > 0</text>
  <text x="62" y="85" fill="#f8fafc" font-size="10" text-anchor="middle">Real &amp;</text>
  <text x="62" y="105" fill="#f8fafc" font-size="10" text-anchor="middle">Unequal</text>
  <rect x="122" y="25" width="95" height="100" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Δ = 0</text>
  <text x="170" y="85" fill="#f8fafc" font-size="10" text-anchor="middle">Real &amp;</text>
  <text x="170" y="105" fill="#f8fafc" font-size="10" text-anchor="middle">Equal</text>
  <rect x="230" y="25" width="95" height="100" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
  <text x="277" y="55" fill="#f43f5e" font-size="11" font-weight="bold" text-anchor="middle">Δ &lt; 0</text>
  <text x="277" y="85" fill="#f8fafc" font-size="10" text-anchor="middle">Not Real</text>
  <text x="277" y="105" fill="#f8fafc" font-size="10" text-anchor="middle">(Complex)</text>
</svg>
</div>
What are the three canonical classifications of roots based on the discriminant \\(\\Delta\\)?""",
     ["\\(\\Delta > 0\\): Real & Unequal; \\(\\Delta = 0\\): Real & Equal; \\(\\Delta < 0\\): Not Real",
      "\\(\\Delta > 0\\): Not Real; \\(\\Delta = 0\\): Infinite; \\(\\Delta < 0\\): Zero",
      "\\(\\Delta > 0\\): Complex; \\(\\Delta = 0\\): Real; \\(\\Delta < 0\\): Rational",
      "\\(\\Delta\\) has no relation to root classification"],
     "A", "OSC", "easy",
     "The three fundamental cases of the discriminant determine whether roots are two distinct real numbers (\\(\\Delta > 0\\)), one repeated real number (\\(\\Delta = 0\\)), or non-real complex numbers (\\(\\Delta < 0\\))."),

    # 72
    ("If \\(\\Delta = 49\\), nature of roots is:", ["Real, rational, and unequal", "Real and equal", "Not real", "Zero"], "A", "OSC", "easy", "49 is a positive perfect square."),
    # 73
    ("If \\(\\Delta = 50\\), nature of roots is:", ["Real, irrational, and unequal", "Real and rational", "Real and equal", "Not real"], "A", "OSC", "easy", "50 is positive but not a perfect square."),
    # 74
    ("If \\(\\Delta = 0\\), nature of roots is:", ["Real and equal", "Real and unequal", "Not real", "Zero"], "A", "OSC", "easy", "Roots coincide at \\(-b/2a\\)."),
    # 75
    ("If \\(\\Delta = -9\\), nature of roots is:", ["Not real", "Real and equal", "Real and unequal", "Rational"], "A", "OSC", "easy", "Negative discriminant implies non-real roots."),
    # 76
    ("If \\(\\Delta = -1\\), nature of roots is:", ["Not real", "Real and equal", "Real and unequal", "Rational"], "A", "OSC", "easy", "Negative discriminant implies no real solutions exist."),
    # 77
    ("Find \\(\\Delta\\) for \\(x^2 = 0\\).", ["0", "1", "-1", "Undefined"], "A", "OSC", "easy", "\\(b^2 - 4ac = 0 - 0 = 0\\)."),
    # 78
    ("Find \\(\\Delta\\) for \\(x^2 - 1 = 0\\).", ["4", "0", "-4", "1"], "A", "OSC", "easy", "\\(0 - 4(1)(-1) = 4\\)."),
    # 79
    ("Find \\(\\Delta\\) for \\(x^2 + 1 = 0\\).", ["-4", "4", "0", "-1"], "A", "OSC", "easy", "\\(0 - 4(1)(1) = -4\\)."),
    # 80
    ("Find \\(\\Delta\\) for \\(x^2 - 4 = 0\\).", ["16", "0", "-16", "4"], "A", "OSC", "easy", "\\(0 - 4(1)(-4) = 16\\)."),
    # 81
    ("Find \\(\\Delta\\) for \\(x^2 + 4 = 0\\).", ["-16", "16", "0", "-4"], "A", "OSC", "easy", "\\(0 - 4(1)(4) = -16\\)."),
    # 82
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0b132b" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1c2541" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Equal Roots Condition</text>
  <text x="170" y="80" fill="#f8fafc" font-size="12" text-anchor="middle">b² - 4ac = 0</text>
  <text x="170" y="105" fill="#4ade80" font-size="11" text-anchor="middle">Used to solve for unknown parameter k</text>
</svg>
</div>
Why is the condition \\(\\Delta = 0\\) widely used in board exam problems to find an unknown coefficient \\(k\\)?""",
     ["Because it sets up a single solvable equation in k, directly determining the parameter values that guarantee coincident roots",
      "Because it eliminates the constant term",
      "Because it makes all roots equal to zero",
      "Because it converts the equation into a cubic"],
     "A", "OSC", "easy",
     "Setting \\(b^2 - 4ac = 0\\) converts the condition of equal roots into an exact algebraic relation involving the unknown constant \\(k\\), allowing \\(k\\) to be found immediately.")
]

all_q_25 = build_topic_questions("MH-10-MTH1-2-2.5", t25_exam, t25_prac, t25_mock)
out_25 = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch2_t5.json")
with open(out_25, "w", encoding="utf-8") as f:
    json.dump(all_q_25, f, indent=2, ensure_ascii=False)
print(f"Generated {len(all_q_25)} questions for MH-10-MTH1-2-2.5 -> {out_25}")
