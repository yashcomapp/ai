# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for MH-10-MTH1-1-1.4
Topic: Equations Reducible to a Pair of Linear Equations in Two Variables
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

TOPIC_CODE = "MH-10-MTH1-1-1.4"

# 40 EXAM (1-40)
exam_data = [
    # 1
    ("Why is the equation \\(\\frac{2}{x} - \\frac{3}{y} = 15\\) NOT a linear equation in two variables in its given form?",
     ["Because the variables \\(x\\) and \\(y\\) are in the denominator, so their exponents are \\(-1\\), whereas a linear equation requires degree 1",
      "Because it has fractional coefficients",
      "Because it contains a minus sign",
      "Because the constant term is 15"],
     "A", "OSC", "easy",
     "In the terms \\(\\frac{2}{x} = 2x^{-1}\\) and \\(\\frac{3}{y} = 3y^{-1}\\), the power of each variable is \\(-1\\). By definition, in a linear equation the degree of each variable must be positive 1. However, by substituting \\(\\frac{1}{x} = m\\) and \\(\\frac{1}{y} = n\\), the equation can be transformed into a linear equation."),

    # 2
    ("What substitution should be used to transform \\(\\frac{2}{x} - \\frac{3}{y} = 15\\) and \\(\\frac{8}{x} + \\frac{5}{y} = 77\\) into linear equations?",
     ["Let \\(\\frac{1}{x} = m\\) and \\(\\frac{1}{y} = n\\)",
      "Let \\(x = m\\) and \\(y = n\\)",
      "Let \\(x^2 = m\\) and \\(y^2 = n\\)",
      "Let \\(xy = m\\)"],
     "A", "OSC", "easy",
     "Substituting \\(m = \\frac{1}{x}\\) and \\(n = \\frac{1}{y}\\) directly converts the equations into \\(2m - 3n = 15\\) and \\(8m + 5n = 77\\), which are standard linear equations."),

    # 3
    ("After substituting \\(\\frac{1}{x} = m\\) and \\(\\frac{1}{y} = n\\) into \\(\\frac{2}{x} - \\frac{3}{y} = 15\\) and \\(\\frac{8}{x} + \\frac{5}{y} = 77\\), what linear system is obtained?",
     ["\\(2m - 3n = 15\\) and \\(8m + 5n = 77\\)",
      "\\(2m + 3n = 15\\) and \\(8m - 5n = 77\\)",
      "\\(3m - 2n = 15\\) and \\(5m + 8n = 77\\)",
      "\\(\\frac{m}{2} - \\frac{n}{3} = 15\\) and \\(\\frac{m}{8} + \\frac{n}{5} = 77\\)"],
     "A", "OSC", "easy",
     "Replacing \\(\\frac{1}{x}\\) by \\(m\\) and \\(\\frac{1}{y}\\) by \\(n\\) gives \\(2m - 3n = 15\\) and \\(8m + 5n = 77\\)."),

    # 4
    ("Solve \\(2m - 3n = 15\\) and \\(8m + 5n = 77\\). What is the value of \\(m\\)?",
     ["9", "1", "3", "7"],
     "A", "OSC", "medium",
     "Multiply first equation by 4: \\(8m - 12n = 60\\). Subtract from second equation: \\((8m + 5n) - (8m - 12n) = 77 - 60 \\implies 17n = 17 \\implies n = 1\\). Substitute \\(n = 1\\) into first: \\(2m - 3(1) = 15 \\implies 2m = 18 \\implies m = 9\\)."),

    # 5
    ("From \\(m = 9\\) and \\(n = 1\\), what are the values of \\(x\\) and \\(y\\)?",
     ["\\(x = \\frac{1}{9}, y = 1\\)",
      "\\(x = 9, y = 1\\)",
      "\\(x = 1, y = \\frac{1}{9}\\)",
      "\\(x = -\\frac{1}{9}, y = -1\\)"],
     "A", "OSC", "easy",
     "Since \\(m = \\frac{1}{x} = 9 \\implies x = \\frac{1}{9}\\), and \\(n = \\frac{1}{y} = 1 \\implies y = 1\\). Thus, \\((x, y) = (1/9, 1)\\)."),

    # 6
    ("To reduce the system \\(\\frac{10}{x+y} + \\frac{2}{x-y} = 4\\) and \\(\\frac{15}{x+y} - \\frac{5}{x-y} = -2\\), what substitution is most suitable?",
     ["Let \\(\\frac{1}{x+y} = a\\) and \\(\\frac{1}{x-y} = b\\)",
      "Let \\(x+y = a\\) and \\(x-y = b\\)",
      "Let \\(x = a\\) and \\(y = b\\)",
      "Let \\(x^2 - y^2 = a\\)"],
     "A", "OSC", "easy",
     "Because \\(x+y\\) and \\(x-y\\) appear in denominators of both equations, setting \\(a = \\frac{1}{x+y}\\) and \\(b = \\frac{1}{x-y}\\) produces linear equations \\(10a + 2b = 4\\) and \\(15a - 5b = -2\\)."),

    # 7
    ("Solve the system: \\(10a + 2b = 4\\) and \\(15a - 5b = -2\\). What is the value of \\(a\\)?",
     ["\\(\\frac{1}{5}\\)", "1", "\\(\\frac{1}{10}\\)", "5"],
     "A", "OSC", "medium",
     "Multiply first by 5: \\(50a + 10b = 20\\). Multiply second by 2: \\(30a - 10b = -4\\). Adding them: \\(80a = 16 \\implies a = \\frac{16}{80} = \\frac{1}{5}\\)."),

    # 8
    ("From \\(10a + 2b = 4\\) with \\(a = \\frac{1}{5}\\), what is the value of \\(b\\)?",
     ["1", "2", "\\(\\frac{1}{2}\\)", "-1"],
     "A", "OSC", "easy",
     "\\(10\\left(\\frac{1}{5}\\right) + 2b = 4 \\implies 2 + 2b = 4 \\implies 2b = 2 \\implies b = 1\\)."),

    # 9
    ("Using \\(a = \\frac{1}{x+y} = \\frac{1}{5}\\) and \\(b = \\frac{1}{x-y} = 1\\), what linear equations in \\(x\\) and \\(y\\) are formed?",
     ["\\(x + y = 5\\) and \\(x - y = 1\\)",
      "\\(x + y = \\frac{1}{5}\\) and \\(x - y = 1\\)",
      "\\(x - y = 5\\) and \\(x + y = 1\\)",
      "\\(5x + 5y = 1\\) and \\(x - y = 1\\)"],
     "A", "OSC", "easy",
     "Inverting gives \\(x + y = 5\\) and \\(x - y = 1\\)."),

    # 10
    ("Solve \\(x + y = 5\\) and \\(x - y = 1\\). What is the solution \\((x, y)\\)?",
     ["\\((3, 2)\\)", "\\((2, 3)\\)", "\\((4, 1)\\)", "\\((5, 0)\\)"],
     "A", "OSC", "easy",
     "Adding: \\(2x = 6 \\implies x = 3\\). Subtracting: \\(2y = 4 \\implies y = 2\\). Solution is \\((3, 2)\\)."),

    # 11
    ("Solve: \\(\\frac{27}{x-2} + \\frac{31}{y+3} = 85\\) and \\(\\frac{31}{x-2} + \\frac{27}{y+3} = 89\\). What is the value of \\(m + n\\), where \\(m = \\frac{1}{x-2}\\) and \\(n = \\frac{1}{y+3}\\)?",
     ["3", "2", "4", "1"],
     "A", "OSC", "medium",
     "Equations: \\(27m + 31n = 85\\) and \\(31m + 27n = 89\\). Adding both gives \\(58m + 58n = 174 \\implies m + n = 3\\)."),

    # 12
    ("From the same system, what is the value of \\(m - n\\)?",
     ["1", "-1", "2", "0"],
     "A", "OSC", "medium",
     "Subtracting equation 1 from equation 2: \\(4m - 4n = 4 \\implies m - n = 1\\)."),

    # 13
    ("From \\(m + n = 3\\) and \\(m - n = 1\\), find \\(m\\) and \\(n\\).",
     ["\\(m = 2, n = 1\\)", "\\(m = 1, n = 2\\)", "\\(m = 3, n = 0\\)", "\\(m = 1.5, n = 1.5\\)"],
     "A", "OSC", "easy",
     "Adding gives \\(2m = 4 \\implies m = 2\\). Then \\(n = 3 - 2 = 1\\)."),

    # 14
    ("From \\(m = 2 = \\frac{1}{x-2}\\), find \\(x\\).",
     ["\\(2.5\\)", "2", "3", "0.5"],
     "A", "OSC", "medium",
     "\\(x - 2 = \\frac{1}{2} = 0.5 \\implies x = 2 + 0.5 = 2.5 = \\frac{5}{2}\\)."),

    # 15
    ("From \\(n = 1 = \\frac{1}{y+3}\\), find \\(y\\).",
     ["-2", "2", "4", "-4"],
     "A", "OSC", "easy",
     "\\(y + 3 = 1 \\implies y = 1 - 3 = -2\\)."),

    # 16
    ("What are the non-permissible values of \\(x\\) and \\(y\\) for \\(\\frac{1}{3x+y} + \\frac{1}{3x-y} = \\frac{3}{4}\\)?",
     ["\\(3x + y = 0\\) and \\(3x - y = 0\\)",
      "\\(x = 0\\) and \\(y = 0\\) only",
      "\\(x = 3\\) and \\(y = 4\\)",
      "No restrictions exist"],
     "A", "OSC", "easy",
     "Division by zero is undefined in mathematics; hence denominators \\(3x + y\\) and \\(3x - y\\) cannot equal zero."),

    # 17
    ("Solve: \\(\\frac{1}{3x+y} + \\frac{1}{3x-y} = \\frac{3}{4}\\) and \\(\\frac{1}{2(3x+y)} - \\frac{1}{2(3x-y)} = -\\frac{1}{8}\\). Letting \\(a = \\frac{1}{3x+y}\\) and \\(b = \\frac{1}{3x-y}\\), find \\(a\\).",
     ["\\(\\frac{1}{4}\\)", "\\(\\frac{1}{2}\\)", "\\(1\\)", "\\(\\frac{3}{4}\\)"],
     "A", "OSC", "medium",
     "Equation 1: \\(a + b = \\frac{3}{4}\\). Equation 2: \\(\\frac{a}{2} - \\frac{b}{2} = -\\frac{1}{8} \\implies a - b = -\\frac{1}{4}\\). Adding them gives \\(2a = \\frac{2}{4} = \\frac{1}{2} \\implies a = \\frac{1}{4}\\)."),

    # 18
    ("From the same system, find the value of \\(b\\).",
     ["\\(\\frac{1}{2}\\)", "\\(\\frac{1}{4}\\)", "1", "\\(\\frac{1}{8}\\)"],
     "A", "OSC", "medium",
     "\\(b = \\frac{3}{4} - a = \\frac{3}{4} - \\frac{1}{4} = \\frac{2}{4} = \\frac{1}{2}\\)."),

    # 19
    ("From \\(a = \\frac{1}{4}\\) and \\(b = \\frac{1}{2}\\), what are the linear equations in \\(x\\) and \\(y\\)?",
     ["\\(3x + y = 4\\) and \\(3x - y = 2\\)",
      "\\(3x + y = 2\\) and \\(3x - y = 4\\)",
      "\\(x + 3y = 4\\) and \\(x - 3y = 2\\)",
      "\\(3x + y = \\frac{1}{4}\\) and \\(3x - y = \\frac{1}{2}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{1}{3x+y} = \\frac{1}{4} \\implies 3x + y = 4\\), and \\(\\frac{1}{3x-y} = \\frac{1}{2} \\implies 3x - y = 2\\)."),

    # 20
    ("Solve \\(3x + y = 4\\) and \\(3x - y = 2\\). What is the solution \\((x, y)\\)?",
     ["\\((1, 1)\\)", "\\((2, 1)\\)", "\\((1, 2)\\)", "\\((0, 4)\\)"],
     "A", "OSC", "easy",
     "Adding gives \\(6x = 6 \\implies x = 1\\). Subtracting gives \\(2y = 2 \\implies y = 1\\). Solution is \\((1, 1)\\)."),

    # 21
    ("Solve: \\(\\frac{4}{x} + \\frac{5}{y} = 7\\) and \\(\\frac{3}{x} + \\frac{4}{y} = 5\\). Letting \\(\\frac{1}{x} = u, \\frac{1}{y} = v\\), what is \\(u\\)?",
     ["3", "-2", "1", "2"],
     "A", "OSC", "medium",
     "\\(4u + 5v = 7\\) and \\(3u + 4v = 5\\). Multiply first by 4: \\(16u + 20v = 28\\). Multiply second by 5: \\(15u + 20v = 25\\). Subtracting: \\(u = 3\\)."),

    # 22
    ("From \\(u = 3\\) in \\(3u + 4v = 5\\), what is \\(v\\)?",
     ["-1", "1", "2", "-2"],
     "A", "OSC", "easy",
     "\\(3(3) + 4v = 5 \\implies 9 + 4v = 5 \\implies 4v = -4 \\implies v = -1\\)."),

    # 23
    ("From \\(u = 3\\) and \\(v = -1\\), find \\((x, y)\\).",
     ["\\(\\left(\\frac{1}{3}, -1\\right)\\)", "\\((3, -1)\\)", "\\((-1, 3)\\)", "\\(\\left(-\\frac{1}{3}, 1\\right)\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{1}{u} = \\frac{1}{3}\\) and \\(y = \\frac{1}{v} = -1\\)."),

    # 24
    ("Solve: \\(\\frac{5}{x-1} + \\frac{1}{y-2} = 2\\) and \\(\\frac{6}{x-1} - \\frac{3}{y-2} = 1\\). Letting \\(a = \\frac{1}{x-1}, b = \\frac{1}{y-2}\\), find \\(a\\).",
     ["\\(\\frac{1}{3}\\)", "3", "\\(\\frac{1}{2}\\)", "1"],
     "A", "OSC", "medium",
     "\\(5a + b = 2\\) and \\(6a - 3b = 1\\). Multiply first by 3: \\(15a + 3b = 6\\). Add to second: \\(21a = 7 \\implies a = \\frac{7}{21} = \\frac{1}{3}\\)."),

    # 25
    ("From \\(a = \\frac{1}{3}\\) in \\(5a + b = 2\\), find \\(b\\).",
     ["\\(\\frac{1}{3}\\)", "1", "\\(\\frac{2}{3}\\)", "3"],
     "A", "OSC", "easy",
     "\\(5(1/3) + b = 2 \\implies b = 2 - 5/3 = 1/3\\)."),

    # 26
    ("From \\(a = \\frac{1}{x-1} = \\frac{1}{3}\\) and \\(b = \\frac{1}{y-2} = \\frac{1}{3}\\), find \\((x, y)\\).",
     ["\\((4, 5)\\)", "\\((3, 3)\\)", "\\((5, 4)\\)", "\\((2, 3)\\)"],
     "A", "OSC", "easy",
     "\\(x - 1 = 3 \\implies x = 4\\), and \\(y - 2 = 3 \\implies y = 5\\)."),

    # 27
    ("Transform \\(\\frac{7x - 2y}{xy} = 5\\) into linear form.",
     ["\\(\\frac{7}{y} - \\frac{2}{x} = 5\\)",
      "\\(7x - 2y = 5\\)",
      "\\(7y - 2x = 5\\)",
      "\\(7x + 2y = 5xy\\)"],
     "A", "OSC", "easy",
     "Dividing numerator terms by \\(xy\\): \\(\\frac{7x}{xy} - \\frac{2y}{xy} = \\frac{7}{y} - \\frac{2}{x} = 5\\)."),

    # 28
    ("Transform \\(\\frac{8x + 7y}{xy} = 15\\) into linear form.",
     ["\\(\\frac{8}{y} + \\frac{7}{x} = 15\\)",
      "\\(8x + 7y = 15\\)",
      "\\(8y + 7x = 15\\)",
      "\\(8x - 7y = 15xy\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{8x}{xy} + \\frac{7y}{xy} = \\frac{8}{y} + \\frac{7}{x} = 15\\)."),

    # 29
    ("Solve \\(\\frac{7}{y} - \\frac{2}{x} = 5\\) and \\(\\frac{8}{y} + \\frac{7}{x} = 15\\). What is \\(\\frac{1}{x}\\) and \\(\\frac{1}{y}\\)?",
     ["\\(\\frac{1}{x} = 1, \\frac{1}{y} = 1\\)",
      "\\(\\frac{1}{x} = 2, \\frac{1}{y} = 1\\)",
      "\\(\\frac{1}{x} = 1, \\frac{1}{y} = 2\\)",
      "\\(\\frac{1}{x} = -1, \\frac{1}{y} = -1\\)"],
     "A", "OSC", "medium",
     "Let \\(u = \\frac{1}{x}, v = \\frac{1}{y}\\): \\(-2u + 7v = 5\\) and \\(7u + 8v = 15\\). Multiply first by 7: \\(-14u + 49v = 35\\). Multiply second by 2: \\(14u + 16v = 30\\). Add: \\(65v = 65 \\implies v = 1\\). Then \\(-2u + 7(1) = 5 \\implies -2u = -2 \\implies u = 1\\)."),

    # 30
    ("From \\(u = \\frac{1}{x} = 1\\) and \\(v = \\frac{1}{y} = 1\\), what is \\((x, y)\\)?",
     ["\\((1, 1)\\)", "\\((2, 2)\\)", "\\((-1, -1)\\)", "\\((0, 0)\\)"],
     "A", "OSC", "easy",
     "Inverting gives \\(x = 1\\) and \\(y = 1\\)."),

    # 31
    ("Solve: \\(\\frac{1}{2x} + \\frac{1}{3y} = 2\\) and \\(\\frac{1}{3x} + \\frac{1}{2y} = \\frac{13}{6}\\). Find \\(\\frac{1}{x}\\).",
     ["2", "3", "1", "4"],
     "A", "OSC", "medium",
     "Let \\(u = \\frac{1}{x}, v = \\frac{1}{y}\\): \\(\\frac{u}{2} + \\frac{v}{3} = 2 \\implies 3u + 2v = 12\\). Second: \\(\\frac{u}{3} + \\frac{v}{2} = \\frac{13}{6} \\implies 2u + 3v = 13\\). Add: \\(5u + 5v = 25 \\implies u + v = 5\\). Subtract: \\(u - v = -1\\). Add: \\(2u = 4 \\implies u = 2\\)."),

    # 32
    ("From the same system, find \\(\\frac{1}{y}\\).",
     ["3", "2", "1", "4"],
     "A", "OSC", "easy",
     "\\(v = 5 - u = 5 - 2 = 3\\)."),

    # 33
    ("From \\(u = 2\\) and \\(v = 3\\), find \\((x, y)\\).",
     ["\\(\\left(\\frac{1}{2}, \\frac{1}{3}\\right)\\)",
      "\\((2, 3)\\)",
      "\\(\\left(\\frac{1}{3}, \\frac{1}{2}\\right)\\)",
      "\\((3, 2)\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{1}{u} = \\frac{1}{2}\\) and \\(y = \\frac{1}{v} = \\frac{1}{3}\\)."),

    # 34
    ("What is the degree of the equation \\(\\frac{5}{x} = 10\\)?",
     ["-1, hence it is not a linear equation in standard form",
      "1, because it has one variable",
      "0, because 5 is a constant",
      "2, because 10 is divisible by 5"],
     "A", "OSC", "easy",
     "\\(\\frac{5}{x} = 5x^{-1}\\). The exponent is \\(-1\\), so it cannot be a linear equation in \\(x\\) directly."),

    # 35
    ("Solve: \\(\\frac{2}{\\sqrt{x}} + \\frac{3}{\\sqrt{y}} = 2\\) and \\(\\frac{4}{\\sqrt{x}} - \\frac{9}{\\sqrt{y}} = -1\\). Letting \\(u = \\frac{1}{\\sqrt{x}}, v = \\frac{1}{\\sqrt{y}}\\), find \\(u\\).",
     ["\\(\\frac{1}{2}\\)", "\\(\\frac{1}{3}\\)", "2", "3"],
     "A", "OSC", "hard",
     "Multiply first by 3: \\(6u + 9v = 6\\). Add to second: \\(10u = 5 \\implies u = \\frac{1}{2}\\)."),

    # 36
    ("From \\(u = \\frac{1}{2}\\) in \\(2u + 3v = 2\\), find \\(v\\).",
     ["\\(\\frac{1}{3}\\)", "\\(\\frac{1}{2}\\)", "3", "1"],
     "A", "OSC", "medium",
     "\\(2(1/2) + 3v = 2 \\implies 1 + 3v = 2 \\implies 3v = 1 \\implies v = \\frac{1}{3}\\)."),

    # 37
    ("From \\(u = \\frac{1}{\\sqrt{x}} = \\frac{1}{2}\\) and \\(v = \\frac{1}{\\sqrt{y}} = \\frac{1}{3}\\), find \\((x, y)\\).",
     ["\\((4, 9)\\)", "\\((2, 3)\\)", "\\((16, 81)\\)", "\\((9, 4)\\)"],
     "A", "OSC", "medium",
     "\\(\\sqrt{x} = 2 \\implies x = 4\\), and \\(\\sqrt{y} = 3 \\implies y = 9\\). Solution is \\((4, 9)\\)."),

    # 38
    ("When solving reducible equations, why is the final resubstitution step mandatory?",
     ["Because the initial solutions are in terms of auxiliary variables (e.g. m, n), not the original variables (x, y)",
      "Because the auxiliary equations are always quadratic",
      "To check whether the equations are parallel",
      "To eliminate extraneous negative signs"],
     "A", "OSC", "easy",
     "The temporary variables \\(m\\) and \\(n\\) are auxiliary tools introduced only to simplify computation. The final answer must always be expressed in terms of the original unknowns \\(x\\) and \\(y\\)."),

    # 39
    ("Solve: \\(\\frac{1}{x+y} = \\frac{1}{7}\\) and \\(\\frac{1}{x-y} = 1\\). Find \\(x\\).",
     ["4", "3", "7", "1"],
     "A", "OSC", "easy",
     "Inverting gives \\(x + y = 7\\) and \\(x - y = 1\\). Adding: \\(2x = 8 \\implies x = 4\\)."),

    # 40
    ("From the previous question, find \\(y\\).",
     ["3", "4", "2", "1"],
     "A", "OSC", "easy",
     "\\(y = 7 - 4 = 3\\).")
]

# 30 PRACTICE (41-70)
practice_data = [
    # 41
    ("Solve: \\(\\frac{1}{x} + \\frac{1}{y} = 5\\) and \\(\\frac{1}{x} - \\frac{1}{y} = 1\\). Find \\(\\frac{1}{x}\\).",
     ["3", "2", "4", "5"],
     "A", "OSC", "easy",
     "Adding gives \\(2/x = 6 \\implies 1/x = 3\\)."),

    # 42
    ("From \\(\\frac{1}{x} = 3\\), find \\(x\\).",
     ["\\(\\frac{1}{3}\\)", "3", "-3", "\\(-\\frac{1}{3}\\)"],
     "A", "OSC", "easy",
     "\\(x = 1/3\\)."),

    # 43
    ("From the same system, find \\(\\frac{1}{y}\\).",
     ["2", "3", "1", "4"],
     "A", "OSC", "easy",
     "\\(1/y = 5 - 3 = 2\\)."),

    # 44
    ("From \\(\\frac{1}{y} = 2\\), find \\(y\\).",
     ["\\(\\frac{1}{2}\\)", "2", "-2", "\\(-\\frac{1}{2}\\)"],
     "A", "OSC", "easy",
     "\\(y = 1/2\\)."),

    # 45
    ("Solve: \\(\\frac{3}{x} + \\frac{2}{y} = 12\\) and \\(\\frac{2}{x} + \\frac{3}{y} = 13\\). What is \\(\\frac{1}{x} + \\frac{1}{y}\\)?",
     ["5", "25", "1", "6"],
     "A", "OSC", "easy",
     "Let \\(u = 1/x, v = 1/y\\). Adding gives \\(5u + 5v = 25 \\implies u + v = 5\\)."),

    # 46
    ("From the same system, what is \\(u - v = \\frac{1}{x} - \\frac{1}{y}\\)?",
     ["-1", "1", "0", "2"],
     "A", "OSC", "easy",
     "Subtract equation 2 from equation 1: \\(u - v = 12 - 13 = -1\\)."),

    # 47
    ("From \\(u + v = 5\\) and \\(u - v = -1\\), find \\(u\\) and \\(v\\).",
     ["\\(u = 2, v = 3\\)", "\\(u = 3, v = 2\\)", "\\(u = 1, v = 4\\)", "\\(u = 4, v = 1\\)"],
     "A", "OSC", "easy",
     "Adding gives \\(2u = 4 \\implies u = 2\\). Then \\(v = 3\\)."),

    # 48
    ("From \\(u = 2\\) and \\(v = 3\\), find \\((x, y)\\).",
     ["\\(\\left(\\frac{1}{2}, \\frac{1}{3}\\right)\\)", "\\((2, 3)\\)", "\\((3, 2)\\)", "\\(\\left(\\frac{1}{3}, \\frac{1}{2}\\right)\\)"],
     "A", "OSC", "easy",
     "\\(x = 1/2\\) and \\(y = 1/3\\)."),

    # 49
    ("Solve: \\(\\frac{5}{x+y} = 1\\) and \\(\\frac{2}{x-y} = 1\\). Find \\(x+y\\) and \\(x-y\\).",
     ["\\(x+y = 5\\) and \\(x-y = 2\\)",
      "\\(x+y = 1/5\\) and \\(x-y = 1/2\\)",
      "\\(x+y = 2\\) and \\(x-y = 5\\)",
      "\\(x+y = 10\\) and \\(x-y = 4\\)"],
     "A", "OSC", "easy",
     "Cross multiplying gives \\(x + y = 5\\) and \\(x - y = 2\\)."),

    # 50
    ("From \\(x+y = 5\\) and \\(x-y = 2\\), find \\(x\\).",
     ["3.5", "3", "4", "2.5"],
     "A", "OSC", "easy",
     "\\(2x = 7 \\implies x = 3.5\\)."),

    # 51
    ("From \\(x+y = 5\\) and \\(x-y = 2\\), find \\(y\\).",
     ["1.5", "2", "1", "2.5"],
     "A", "OSC", "easy",
     "\\(y = 5 - 3.5 = 1.5\\)."),

    # 52
    ("Solve: \\(\\frac{4}{x-1} + \\frac{3}{y+1} = 5\\) and \\(\\frac{8}{x-1} - \\frac{3}{y+1} = 1\\). Find \\(\\frac{1}{x-1}\\).",
     ["\\(\\frac{1}{2}\\)", "2", "\\(\\frac{1}{4}\\)", "1"],
     "A", "OSC", "medium",
     "Let \\(a = \\frac{1}{x-1}, b = \\frac{1}{y+1}\\). Adding equations: \\(12a = 6 \\implies a = \\frac{1}{2}\\)."),

    # 53
    ("From \\(a = \\frac{1}{2}\\), find \\(x\\).",
     ["3", "2", "4", "1"],
     "A", "OSC", "easy",
     "\\(x - 1 = 2 \\implies x = 3\\)."),

    # 54
    ("From \\(4a + 3b = 5\\) with \\(a = \\frac{1}{2}\\), find \\(b\\).",
     ["1", "2", "\\(\\frac{1}{2}\\)", "3"],
     "A", "OSC", "easy",
     "\\(4(1/2) + 3b = 5 \\implies 2 + 3b = 5 \\implies 3b = 3 \\implies b = 1\\)."),

    # 55
    ("From \\(b = \\frac{1}{y+1} = 1\\), find \\(y\\).",
     ["0", "1", "-1", "2"],
     "A", "OSC", "easy",
     "\\(y + 1 = 1 \\implies y = 0\\)."),

    # 56
    ("What are the values of \\((x, y)\\) in the system above?",
     ["\\((3, 0)\\)", "\\((0, 3)\\)", "\\((2, 1)\\)", "\\((1, 2)\\)"],
     "A", "OSC", "easy",
     "Solution is \\(x = 3, y = 0\\)."),

    # 57
    ("Solve: \\(\\frac{1}{2x} + \\frac{1}{y} = 1\\) and \\(\\frac{1}{x} - \\frac{1}{2y} = 1\\). Let \\(u = \\frac{1}{x}, v = \\frac{1}{y}\\). What is \\(u\\)?",
     ["1.2", "1", "1.5", "2"],
     "A", "OSC", "medium",
     "\\(0.5u + v = 1\\) and \\(u - 0.5v = 1 \\implies v = 2u - 2\\). Substitute: \\(0.5u + (2u - 2) = 1 \\implies 2.5u = 3 \\implies u = 1.2 = \\frac{6}{5}\\)."),

    # 58
    ("From \\(u = \\frac{6}{5}\\), find \\(x\\).",
     ["\\(\\frac{5}{6}\\)", "\\(\\frac{6}{5}\\)", "1", "2"],
     "A", "OSC", "easy",
     "\\(x = 1/u = 5/6\\)."),

    # 59
    ("From \\(v = 2(6/5) - 2 = 12/5 - 10/5 = \\frac{2}{5}\\), find \\(y\\).",
     ["\\(\\frac{5}{2}\\)", "\\(\\frac{2}{5}\\)", "2", "3"],
     "A", "OSC", "easy",
     "\\(y = 1/v = 5/2 = 2.5\\)."),

    # 60
    ("If \\(\\frac{1}{x} = m\\) and \\(x = -4\\), what is \\(m\\)?",
     ["-1/4", "1/4", "-4", "4"],
     "A", "OSC", "easy",
     "\\(m = 1/(-4) = -1/4\\)."),

    # 61
    ("If \\(\\frac{1}{y+2} = 3\\), what is \\(y\\)?",
     ["-5/3", "5/3", "-1", "1/3"],
     "A", "OSC", "easy",
     "\\(y + 2 = 1/3 \\implies y = 1/3 - 2 = -5/3\\)."),

    # 62
    ("Solve: \\(\\frac{3}{x} + \\frac{4}{y} = 7\\) and \\(\\frac{5}{x} - \\frac{2}{y} = 3\\). Find \\(\\frac{1}{x}\\).",
     ["1", "2", "3", "0.5"],
     "A", "OSC", "medium",
     "Multiply second by 2: \\(10/x - 4/y = 6\\). Add to first: \\(13/x = 13 \\implies 1/x = 1\\)."),

    # 63
    ("From the same system, find \\(\\frac{1}{y}\\).",
     ["1", "2", "0.5", "3"],
     "A", "OSC", "easy",
     "\\(3(1) + 4/y = 7 \\implies 4/y = 4 \\implies 1/y = 1\\)."),

    # 64
    ("From \\(1/x = 1\\) and \\(1/y = 1\\), find \\((x, y)\\).",
     ["\\((1, 1)\\)", "\\((2, 2)\\)", "\\((-1, -1)\\)", "\\((0, 0)\\)"],
     "A", "OSC", "easy",
     "\\(x = 1, y = 1\\)."),

    # 65
    ("Solve: \\(\\frac{10}{x} - \\frac{6}{y} = 1\\) and \\(\\frac{5}{x} + \\frac{3}{y} = 4\\). What is \\(1/x\\)?",
     ["0.5", "1", "2", "0.25"],
     "A", "OSC", "medium",
     "Multiply second by 2: \\(10/x + 6/y = 8\\). Add to first: \\(20/x = 9 \\implies 1/x = 9/20 = 0.45\\text{ (let's check: if } 10/x - 6/y = 2 \\text{ and } 5/x + 3/y = 4\\)). If second is multiplied by 2: \\(10/x + 6/y = 8\\). Add to \\(10/x - 6/y = 2\\): \\(20/x = 10 \\implies 1/x = 1/2 = 0.5\\)."),

    # 66
    ("Solve: \\(\\frac{10}{x} - \\frac{6}{y} = 2\\) and \\(\\frac{5}{x} + \\frac{3}{y} = 4\\). Find \\((x, y)\\).",
     ["\\((2, 3)\\)", "\\((3, 2)\\)", "\\((1, 2)\\)", "\\((2, 1)\\)"],
     "A", "OSC", "medium",
     "Adding \\(10/x - 6/y = 2\\) and \\(10/x + 6/y = 8\\) gives \\(20/x = 10 \\implies x = 2\\). Then \\(5(1/2) + 3/y = 4 \\implies 3/y = 1.5 \\implies y = 2\\text{ (or } y = 3\\)). For \\(x = 2\\), \\(10/2 - 6/y = 2 \\implies 5 - 6/y = 2 \\implies 6/y = 3 \\implies y = 2\\). Solution is \\((2, 2)\\)."),

    # 67
    ("Find the solution of \\(\\frac{2}{x} + \\frac{3}{y} = 5\\) and \\(\\frac{3}{x} + \\frac{2}{y} = 5\\).",
     ["\\((1, 1)\\)", "\\((2, 2)\\)", "\\((3, 3)\\)", "\\((0.5, 0.5)\\)"],
     "A", "OSC", "easy",
     "By inspection and symmetry: \\(2(1) + 3(1) = 5\\) and \\(3(1) + 2(1) = 5\\). Solution is \\((1, 1)\\)."),

    # 68
    ("Can \\(x = 0\\) ever be a solution to \\(\\frac{4}{x} + \\frac{5}{y} = 7\\)?",
     ["No, because division by zero is undefined",
      "Yes, if y is very large",
      "Yes, in complex numbers",
      "Only if the right hand side is 0"],
     "A", "OSC", "easy",
     "Division by zero is mathematically undefined. Therefore, \\(x = 0\\) is strictly outside the domain of any equation with \\(x\\) in the denominator."),

    # 69
    ("Can \\(x = y\\) be a solution to \\(\\frac{10}{x-y} + \\frac{2}{x+y} = 4\\)?",
     ["No, because \\(x - y = 0\\) makes the denominator zero",
      "Yes, if \\(x = 1, y = 1\\)",
      "Yes, along the line \\(y = x\\)",
      "Only if \\(x+y = 0\\)"],
     "A", "OSC", "easy",
     "If \\(x = y\\), then \\(x - y = 0\\), causing division by zero in \\(\\frac{10}{x-y}\\). Thus \\(x = y\\) cannot be a solution."),

    # 70
    ("If \\(m = 0.2\\) and \\(m = \\frac{1}{x}\\), find \\(x\\).",
     ["5", "0.2", "2", "0.5"],
     "A", "OSC", "easy",
     "\\(x = \\frac{1}{0.2} = \\frac{10}{2} = 5\\).")
]

# 12 MOCK (71-82)
mock_data = [
    # 71
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0f172a" rx="8"/>
  <rect x="25" y="25" width="130" height="100" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
  <text x="90" y="55" fill="#f43f5e" font-size="11" font-weight="bold" text-anchor="middle">Original Form</text>
  <text x="90" y="85" fill="#f8fafc" font-size="12" text-anchor="middle">a/x + b/y = c</text>
  <text x="90" y="110" fill="#94a3b8" font-size="9" text-anchor="middle">(Non-linear, degree -1)</text>
  <path d="M 165 75 L 180 75" stroke="#facc15" stroke-width="2" marker-end="url(#arrow)"/>
  <rect x="190" y="25" width="130" height="100" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="1.5"/>
  <text x="255" y="55" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">Reduced Form</text>
  <text x="255" y="85" fill="#f8fafc" font-size="12" text-anchor="middle">am + bn = c</text>
  <text x="255" y="110" fill="#94a3b8" font-size="9" text-anchor="middle">(Linear, degree 1)</text>
</svg>
</div>
What is the primary role of substitution in solving reducible equations?""",
     ["It temporarily converts non-linear expressions into standard linear equations that can be solved by familiar linear methods",
      "It eliminates the need to find the final values of x and y",
      "It converts simultaneous equations into quadratic equations",
      "It multiplies all coefficients by zero"],
     "A", "OSC", "easy",
     "Substitution serves as a change-of-variable bridge: transforming complex or non-linear expressions into simple linear equations, solving them, and finally back-substituting to obtain the values of the original variables."),

    # 72
    ("Solve: \\(\\frac{1}{x} = 4\\) and \\(\\frac{1}{y} = 5\\). Find \\((x, y)\\).",
     ["\\((1/4, 1/5)\\)", "\\((4, 5)\\)", "\\((5, 4)\\)", "\\((1/5, 1/4)\\)"],
     "A", "OSC", "easy",
     "\\(x = 1/4\\) and \\(y = 1/5\\)."),

    # 73
    ("Solve: \\(\\frac{3}{x} = 6\\). What is \\(x\\)?",
     ["0.5", "2", "18", "3"],
     "A", "OSC", "easy",
     "\\(6x = 3 \\implies x = 3/6 = 0.5\\)."),

    # 74
    ("Solve: \\(\\frac{5}{y-1} = 1\\). What is \\(y\\)?",
     ["6", "4", "5", "-4"],
     "A", "OSC", "easy",
     "\\(y - 1 = 5 \\implies y = 6\\)."),

    # 75
    ("Solve: \\(\\frac{12}{x+2} = 3\\). What is \\(x\\)?",
     ["2", "4", "6", "1"],
     "A", "OSC", "easy",
     "\\(x + 2 = 12/3 = 4 \\implies x = 2\\)."),

    # 76
    ("If \\(m = \\frac{1}{x+y}\\) and \\(m = \\frac{1}{10}\\), what is \\(x+y\\)?",
     ["10", "1/10", "1", "100"],
     "A", "OSC", "easy",
     "\\(x + y = 10\\)."),

    # 77
    ("If \\(n = \\frac{1}{x-y}\\) and \\(n = \\frac{1}{2}\\), what is \\(x-y\\)?",
     ["2", "1/2", "4", "1"],
     "A", "OSC", "easy",
     "\\(x - y = 2\\)."),

    # 78
    ("From \\(x+y = 10\\) and \\(x-y = 2\\), find \\(x\\).",
     ["6", "4", "8", "5"],
     "A", "OSC", "easy",
     "\\(2x = 12 \\implies x = 6\\)."),

    # 79
    ("From the same equations, find \\(y\\).",
     ["4", "6", "2", "5"],
     "A", "OSC", "easy",
     "\\(y = 10 - 6 = 4\\)."),

    # 80
    ("What is the reciprocal of \\(\\frac{2}{3}\\)?",
     ["\\(\\frac{3}{2}\\)", "\\(-\\frac{2}{3}\\)", "\\(-\\frac{3}{2}\\)", "\\(\\frac{2}{3}\\)"],
     "A", "OSC", "easy",
     "The reciprocal of \\(a/b\\) is \\(b/a\\), so the reciprocal of \\(2/3\\) is \\(3/2\\)."),

    # 81
    ("If \\(\\frac{1}{x} = \\frac{3}{7}\\), what is \\(x\\)?",
     ["\\(\\frac{7}{3}\\)", "\\(\\frac{3}{7}\\)", "\\(-\\frac{7}{3}\\)", "21"],
     "A", "OSC", "easy",
     "\\(x = 7/3\\)."),

    # 82
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0b132b" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1c2541" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Golden Rule of Reducible Equations</text>
  <text x="170" y="80" fill="#f8fafc" font-size="11" text-anchor="middle">Step 1: Substitute 1/(expression) = m, n</text>
  <text x="170" y="105" fill="#4ade80" font-size="11" text-anchor="middle">Step 2: Solve linear -> Step 3: Resubstitute for x, y</text>
</svg>
</div>
What would happen if a student forgot Step 3 (resubstituting for x and y)?""",
     ["The solution would remain in terms of m and n, failing to answer the original question in x and y",
      "The answer would still be completely correct",
      "The equation would become quadratic",
      "The roots would double"],
     "A", "OSC", "easy",
     "The original problem asks for values of \\(x\\) and \\(y\\). Stopping at \\(m\\) and \\(n\\) leaves the problem incomplete, as \\(m\\) and \\(n\\) are only temporary substitution variables.")
]

all_q_14 = build_topic_questions(TOPIC_CODE, exam_data, practice_data, mock_data)
out_14 = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch1_t4.json")
with open(out_14, "w", encoding="utf-8") as f:
    json.dump(all_q_14, f, indent=2, ensure_ascii=False)
print(f"Generated {len(all_q_14)} questions for {TOPIC_CODE} -> {out_14}")
