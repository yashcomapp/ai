# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 2: Quadratic Equations (Topics 2.1 & 2.2)
Each topic: exactly 82 canonical questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# ==============================================================================
# TOPIC 2.1: Quadratic Equation Definition, Standard Form & Roots (MH-10-MTH1-2-2.1)
# ==============================================================================
t21_exam = [
    # 1
    ("Which of the following is the standard form of a quadratic equation in one variable \\(x\\)?",
     ["\\(ax^2 + bx + c = 0\\), where \\(a, b, c\\) are real numbers and \\(a \\neq 0\\)",
      "\\(ax + b = 0\\), where \\(a \\neq 0\\)",
      "\\(ax^3 + bx^2 + cx + d = 0\\), where \\(a \\neq 0\\)",
      "\\(ax^2 + by^2 + c = 0\\)"],
     "A", "OSC", "easy",
     "The equation \\(ax^2 + bx + c = 0\\) is the standard form of a quadratic equation in one variable \\(x\\), where \\(a, b, c\\) are real numbers and the leading coefficient \\(a \\neq 0\\)."),

    # 2
    ("Why must the coefficient \\(a\\) be non-zero (\\(a \\neq 0\\)) in \\(ax^2 + bx + c = 0\\)?",
     ["If \\(a = 0\\), the term \\(ax^2\\) vanishes, reducing the equation to a linear equation \\(bx + c = 0\\)",
      "Because 0 cannot be multiplied by \\(x^2\\)",
      "Because the equation would have 3 roots",
      "Because \\(b\\) and \\(c\\) would also become zero"],
     "A", "OSC", "easy",
     "If \\(a = 0\\), the degree of the equation is no longer 2; it becomes \\(bx + c = 0\\), which has degree 1 and is a linear equation."),

    # 3
    ("What is the degree (maximum index) of the variable in any quadratic equation?",
     ["2", "1", "3", "0"],
     "A", "OSC", "easy",
     "By definition, an equation involving one variable with maximum index (degree) 2 is called a quadratic equation."),

    # 4
    ("Decide whether \\(x^2 + 5x - 2 = 0\\) is a quadratic equation.",
     ["Yes, because it contains only one variable \\(x\\) and the maximum index of \\(x\\) is 2",
      "No, because the constant term is negative",
      "No, because the coefficient of x is 5",
      "Yes, because it has three terms"],
     "A", "OSC", "easy",
     "In \\(x^2 + 5x - 2 = 0\\), \\(x\\) is the only variable and the highest power of \\(x\\) is 2. Therefore, it is a quadratic equation."),

    # 5
    ("Decide whether \\(y^2 + \\frac{1}{y} = 2\\) is a quadratic equation.",
     ["No, because multiplying by \\(y\\) yields \\(y^3 + 1 = 2y\\), where the degree is 3",
      "Yes, because \\(y^2\\) is present",
      "Yes, because it has one variable",
      "No, because 2 is positive"],
     "A", "OSC", "medium",
     "Multiplying throughout by \\(y\\) to clear fractions gives \\(y^3 + 1 = 2y \\implies y^3 - 2y + 1 = 0\\). The highest power of \\(y\\) is 3 (cubic), not 2, so it is NOT a quadratic equation."),

    # 6
    ("Decide whether \\(x + \\frac{1}{x} = -2\\) is a quadratic equation.",
     ["Yes, multiplying by \\(x\\) gives \\(x^2 + 2x + 1 = 0\\), which has degree 2",
      "No, because \\(x\\) is in the denominator",
      "No, because the right hand side is negative",
      "Yes, because \\(x = -2\\)"],
     "A", "OSC", "medium",
     "Multiplying throughout by \\(x\\) gives \\(x^2 + 1 = -2x \\implies x^2 + 2x + 1 = 0\\). The variable \\(x\\) has maximum index 2, so it is a quadratic equation."),

    # 7
    ("Decide whether \\((m + 2)(m - 5) = 0\\) is a quadratic equation.",
     ["Yes, expanding gives \\(m^2 - 3m - 10 = 0\\), which has maximum index 2",
      "No, because it is written as a product of factors",
      "No, because \\(m\\) has degree 1 in both brackets",
      "Yes, because it has two roots"],
     "A", "OSC", "easy",
     "Expanding: \\(m(m - 5) + 2(m - 5) = m^2 - 5m + 2m - 10 = m^2 - 3m - 10 = 0\\). The degree of variable \\(m\\) is 2, so it is a quadratic equation."),

    # 8
    ("Decide whether \\(m^3 + 3m^2 - 2 = 3m^3\\) is a quadratic equation.",
     ["No, because simplifying gives \\(2m^3 - 3m^2 + 2 = 0\\), which has degree 3",
      "Yes, because \\(3m^2\\) is present",
      "Yes, because the terms on both sides cancel",
      "No, because there are two cubic terms"],
     "A", "OSC", "medium",
     "Transposing: \\(3m^3 - m^3 - 3m^2 + 2 = 0 \\implies 2m^3 - 3m^2 + 2 = 0\\). The highest index of \\(m\\) is 3, so it is not a quadratic equation."),

    # 9
    ("Write \\(2y = 10 - y^2\\) in standard form \\(ax^2 + bx + c = 0\\) and identify the values of \\(a, b, c\\).",
     ["\\(y^2 + 2y - 10 = 0\\); \\(a = 1, b = 2, c = -10\\)",
      "\\(y^2 - 2y + 10 = 0\\); \\(a = 1, b = -2, c = 10\\)",
      "\\(-y^2 + 2y - 10 = 0\\); \\(a = -1, b = 2, c = 10\\)",
      "\\(y^2 + 2y + 10 = 0\\); \\(a = 1, b = 2, c = 10\\)"],
     "A", "OSC", "easy",
     "Transposing terms to the left: \\(y^2 + 2y - 10 = 0\\). Comparing with \\(ay^2 + by + c = 0\\), we get \\(a = 1, b = 2, c = -10\\)."),

    # 10
    ("Write \\((x - 1)^2 = 2x + 3\\) in standard form.",
     ["\\(x^2 - 4x - 2 = 0\\)",
      "\\(x^2 - 2x + 1 = 0\\)",
      "\\(x^2 - 4x + 4 = 0\\)",
      "\\(x^2 + 4x - 2 = 0\\)"],
     "A", "OSC", "medium",
     "Expanding: \\(x^2 - 2x + 1 = 2x + 3 \\implies x^2 - 2x - 2x + 1 - 3 = 0 \\implies x^2 - 4x - 2 = 0\\)."),

    # 11
    ("Write \\(x^2 + 5x = -(3 - x)\\) in standard form and find \\(a, b, c\\).",
     ["\\(x^2 + 4x + 3 = 0\\); \\(a = 1, b = 4, c = 3\\)",
      "\\(x^2 + 6x + 3 = 0\\); \\(a = 1, b = 6, c = 3\\)",
      "\\(x^2 + 4x - 3 = 0\\); \\(a = 1, b = 4, c = -3\\)",
      "\\(x^2 + 5x - 3 = 0\\); \\(a = 1, b = 5, c = -3\\)"],
     "A", "OSC", "easy",
     "\\(x^2 + 5x = -3 + x \\implies x^2 + 5x - x + 3 = 0 \\implies x^2 + 4x + 3 = 0\\). Here \\(a = 1, b = 4, c = 3\\)."),

    # 12
    ("Write \\(3m^2 = 2m^2 - 9\\) in standard form.",
     ["\\(m^2 + 0m + 9 = 0\\)",
      "\\(m^2 - 9 = 0\\)",
      "\\(5m^2 - 9 = 0\\)",
      "\\(m^2 - 2m + 9 = 0\\)"],
     "A", "OSC", "easy",
     "\\(3m^2 - 2m^2 + 9 = 0 \\implies m^2 + 9 = 0\\). In standard form \\(ax^2 + bx + c = 0\\), it is written as \\(m^2 + 0m + 9 = 0\\)."),

    # 13
    ("Write \\(P(3 + 6p) = -5\\) in standard form.",
     ["\\(6p^2 + 3p + 5 = 0\\)",
      "\\(6p^2 + 3p - 5 = 0\\)",
      "\\(3p^2 + 6p + 5 = 0\\)",
      "\\(6p^2 - 3p + 5 = 0\\)"],
     "A", "OSC", "easy",
     "Expanding: \\(3p + 6p^2 = -5 \\implies 6p^2 + 3p + 5 = 0\\)."),

    # 14
    ("Write \\(x^2 - 9 = 13\\) in standard form.",
     ["\\(x^2 + 0x - 22 = 0\\)",
      "\\(x^2 - 22 = 0\\)",
      "\\(x^2 + 0x + 4 = 0\\)",
      "\\(x^2 - 4 = 0\\)"],
     "A", "OSC", "easy",
     "\\(x^2 - 9 - 13 = 0 \\implies x^2 - 22 = 0\\), written as \\(x^2 + 0x - 22 = 0\\)."),

    # 15
    ("What is meant by the 'root' or 'solution' of a quadratic equation?",
     ["Any value of the variable for which both sides (LHS and RHS) of the equation become equal",
      "The value of the coefficient a",
      "The square root of the constant term c",
      "The value of the discriminant"],
     "A", "OSC", "easy",
     "The values of the variable which satisfy the given quadratic equation (making \\(\\text{LHS} = \\text{RHS} = 0\\)) are called the roots or solutions of the equation."),

    # 16
    ("How many roots does a quadratic equation have at most?",
     ["At most 2 roots", "Exactly 1 root", "At most 3 roots", "Infinitely many roots"],
     "A", "OSC", "easy",
     "By the Fundamental Theorem of Algebra, a polynomial equation of degree \\(n\\) has at most \\(n\\) roots. Since a quadratic equation has degree 2, it has at most 2 roots."),

    # 17
    ("Determine whether \\(x = 1\\) is a root of \\(x^2 + 4x - 5 = 0\\).",
     ["Yes, because substituting \\(x = 1\\) yields \\(1^2 + 4(1) - 5 = 0 = \\text{RHS}\\)",
      "No, because \\(1 + 4 - 5 \\neq 0\\)",
      "No, because roots cannot be positive",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(\\text{LHS} = (1)^2 + 4(1) - 5 = 1 + 4 - 5 = 0 = \\text{RHS}\\). Since \\(\\text{LHS} = \\text{RHS}\\), \\(x = 1\\) is a root."),

    # 18
    ("Determine whether \\(x = -1\\) is a root of \\(x^2 + 4x - 5 = 0\\).",
     ["No, because substituting \\(x = -1\\) yields \\((-1)^2 + 4(-1) - 5 = 1 - 4 - 5 = -8 \\neq 0\\)",
      "Yes, because \\((-1)^2 = 1\\)",
      "Yes, because -1 satisfies all equations",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(\\text{LHS} = (-1)^2 + 4(-1) - 5 = 1 - 4 - 5 = -8 \\neq \\text{RHS}\\). Therefore, \\(x = -1\\) is NOT a root."),

    # 19
    ("Determine whether \\(m = 2\\) is a root of \\(2m^2 - 5m = 0\\).",
     ["No, because \\(2(2)^2 - 5(2) = 8 - 10 = -2 \\neq 0\\)",
      "Yes, because \\(2(2)^2 = 8\\)",
      "Yes, because \\(m = 2\\) is an integer",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(\\text{LHS} = 2(2)^2 - 5(2) = 8 - 10 = -2 \\neq 0\\). Hence \\(m = 2\\) is not a root."),

    # 20
    ("Determine whether \\(m = \\frac{5}{2}\\) is a root of \\(2m^2 - 5m = 0\\).",
     ["Yes, because \\(2(25/4) - 5(5/2) = 25/2 - 25/2 = 0 = \\text{RHS}\\)",
      "No, because roots cannot be fractions",
      "No, because \\(25/2 \\neq 0\\)",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(\\text{LHS} = 2\\left(\\frac{5}{2}\\right)^2 - 5\\left(\\frac{5}{2}\\right) = 2\\left(\\frac{25}{4}\\right) - \\frac{25}{2} = \\frac{25}{2} - \\frac{25}{2} = 0 = \\text{RHS}\\). Hence \\(m = 5/2\\) is a root."),

    # 21
    ("Find the value of \\(k\\) if \\(x = 3\\) is a root of equation \\(kx^2 - 10x + 3 = 0\\).",
     ["3", "-3", "10", "1"],
     "A", "OSC", "easy",
     "Substitute \\(x = 3\\): \\(k(3)^2 - 10(3) + 3 = 0 \\implies 9k - 30 + 3 = 0 \\implies 9k - 27 = 0 \\implies 9k = 27 \\implies k = 3\\)."),

    # 22
    ("One of the roots of equation \\(5m^2 + 2m + k = 0\\) is \\(-\\frac{7}{5}\\). Find the value of \\(k\\).",
     ["-7", "7", "5", "-5"],
     "A", "OSC", "medium",
     "Substitute \\(m = -7/5\\): \\(5\\left(-\\frac{7}{5}\\right)^2 + 2\\left(-\\frac{7}{5}\\right) + k = 0 \\implies 5\\left(\\frac{49}{25}\\right) - \\frac{14}{5} + k = 0 \\implies \\frac{49}{5} - \\frac{14}{5} + k = 0 \\implies \\frac{35}{5} + k = 0 \\implies 7 + k = 0 \\implies k = -7\\)."),

    # 23
    ("If \\(x = -2\\) is a root of \\(kx^2 + 2x - 8 = 0\\), find \\(k\\).",
     ["3", "2", "-3", "4"],
     "A", "OSC", "easy",
     "Substitute \\(x = -2\\): \\(k(-2)^2 + 2(-2) - 8 = 0 \\implies 4k - 4 - 8 = 0 \\implies 4k = 12 \\implies k = 3\\)."),

    # 24
    ("If \\(x = \\frac{1}{2}\\) is a root of \\(x^2 + kx - \\frac{5}{4} = 0\\), find the value of \\(k\\).",
     ["2", "-2", "1", "-1"],
     "A", "OSC", "easy",
     "Substitute \\(x = 1/2\\): \\(\\left(\\frac{1}{2}\\right)^2 + k\\left(\\frac{1}{2}\\right) - \\frac{5}{4} = 0 \\implies \\frac{1}{4} + \\frac{k}{2} - \\frac{5}{4} = 0 \\implies \\frac{k}{2} - 1 = 0 \\implies \\frac{k}{2} = 1 \\implies k = 2\\)."),

    # 25
    ("Which of the following is NOT a quadratic equation?",
     ["\\(x^2 + \\frac{1}{x^2} = 2\\)",
      "\\(x^2 - 3x + 2 = 0\\)",
      "\\(2x^2 = 5x\\)",
      "\\((x + 1)(x + 2) = 0\\)"],
     "A", "OSC", "easy",
     "In \\(x^2 + \\frac{1}{x^2} = 2\\), multiplying by \\(x^2\\) gives \\(x^4 + 1 = 2x^2 \\implies x^4 - 2x^2 + 1 = 0\\), which has degree 4 (quartic), not 2."),

    # 26
    ("Decide whether \\((x + 2)^3 = x^3 - 4\\) is a quadratic equation.",
     ["Yes, because expanding gives \\(x^3 + 6x^2 + 12x + 8 = x^3 - 4\\), where \\(x^3\\) cancels leaving \\(6x^2 + 12x + 12 = 0\\)",
      "No, because it has degree 3",
      "No, because it has power 3 in bracket",
      "Cannot be determined"],
     "A", "OSC", "medium",
     "\\(x^3 + 3(x)^2(2) + 3(x)(2)^2 + 2^3 = x^3 - 4 \\implies x^3 + 6x^2 + 12x + 8 = x^3 - 4\\). The \\(x^3\\) terms cancel on both sides, yielding \\(6x^2 + 12x + 12 = 0\\), which has degree 2 and is quadratic."),

    # 27
    ("What are the values of \\(a, b, c\\) for \\(y^2 = 2y - 7\\) when written in standard form?",
     ["\\(a = 1, b = -2, c = 7\\)",
      "\\(a = 1, b = 2, c = -7\\)",
      "\\(a = 1, b = -2, c = -7\\)",
      "\\(a = -1, b = 2, c = 7\\)"],
     "A", "OSC", "easy",
     "\\(y^2 - 2y + 7 = 0\\). Comparing with \\(ay^2 + by + c = 0\\) gives \\(a = 1, b = -2, c = 7\\)."),

    # 28
    ("What are the values of \\(a, b, c\\) for \\(x^2 = -5x\\) in standard form?",
     ["\\(a = 1, b = 5, c = 0\\)",
      "\\(a = 1, b = -5, c = 0\\)",
      "\\(a = 1, b = 0, c = 5\\)",
      "\\(a = -1, b = 5, c = 0\\)"],
     "A", "OSC", "easy",
     "\\(x^2 + 5x + 0 = 0\\). Thus \\(a = 1, b = 5, c = 0\\)."),

    # 29
    ("What are the values of \\(a, b, c\\) for \\(2x = -x^2 + 3\\)?",
     ["\\(a = 1, b = 2, c = -3\\)",
      "\\(a = -1, b = 2, c = 3\\)",
      "\\(a = 1, b = -2, c = 3\\)",
      "\\(a = 2, b = 1, c = -3\\)"],
     "A", "OSC", "easy",
     "Transposing terms: \\(x^2 + 2x - 3 = 0\\). Thus \\(a = 1, b = 2, c = -3\\)."),

    # 30
    ("If \\(x = a\\) satisfies \\(ax^2 + bx + c = 0\\), then \\(x = a\\) is called:",
     ["A root or solution of the equation",
      "The degree of the equation",
      "The coefficient of x",
      "An extraneous constant"],
     "A", "OSC", "easy",
     "By definition, any value that satisfies the equation is called a root or solution."),

    # 31
    ("Find \\(k\\) if \\(x = 1\\) is a root of \\(x^2 + kx + 3 = 0\\).",
     ["-4", "4", "-3", "3"],
     "A", "OSC", "easy",
     "\\(1^2 + k(1) + 3 = 0 \\implies 1 + k + 3 = 0 \\implies k + 4 = 0 \\implies k = -4\\)."),

    # 32
    ("Find \\(k\\) if \\(x = -1\\) is a root of \\(2x^2 - kx + 6 = 0\\).",
     ["-8", "8", "-4", "4"],
     "A", "OSC", "easy",
     "\\(2(-1)^2 - k(-1) + 6 = 0 \\implies 2(1) + k + 6 = 0 \\implies k + 8 = 0 \\implies k = -8\\)."),

    # 33
    ("Check if \\(x = 2\\) is a root of \\(x^2 - 4 = 0\\).",
     ["Yes, because \\(2^2 - 4 = 4 - 4 = 0\\)",
      "No, because 2 is positive",
      "No, because \\(x = -2\\) is the only root",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(2^2 - 4 = 4 - 4 = 0 = \\text{RHS}\\). Hence \\(x = 2\\) is a root."),

    # 34
    ("Check if \\(x = -2\\) is a root of \\(x^2 - 4 = 0\\).",
     ["Yes, because \\((-2)^2 - 4 = 4 - 4 = 0\\)",
      "No, because \\((-2)^2 = -4\\)",
      "No, because negative numbers cannot be roots",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "\\((-2)^2 - 4 = 4 - 4 = 0 = \\text{RHS}\\). Hence \\(x = -2\\) is also a root."),

    # 35
    ("What is the constant term \\(c\\) in \\(3x^2 - 5x = 0\\)?",
     ["0", "3", "-5", "Undefined"],
     "A", "OSC", "easy",
     "Written as \\(3x^2 - 5x + 0 = 0\\), the constant term \\(c = 0\\)."),

    # 36
    ("What is the coefficient \\(b\\) of \\(x\\) in \\(4x^2 - 9 = 0\\)?",
     ["0", "4", "-9", "1"],
     "A", "OSC", "easy",
     "Written as \\(4x^2 + 0x - 9 = 0\\), the linear coefficient \\(b = 0\\)."),

    # 37
    ("Which of the following values of \\(x\\) is a root of \\(x^2 - 5x + 6 = 0\\)?",
     ["2 and 3", "1 and 6", "-2 and -3", "-1 and 5"],
     "A", "OSC", "easy",
     "For \\(x = 2\\): \\(4 - 10 + 6 = 0\\). For \\(x = 3\\): \\(9 - 15 + 6 = 0\\). Both 2 and 3 are roots."),

    # 38
    ("If one root of \\(x^2 - 2kx - 6 = 0\\) is \\(3\\), find \\(k\\).",
     ["0.5", "1", "2", "-0.5"],
     "A", "OSC", "easy",
     "Substitute \\(x = 3\\): \\(3^2 - 2k(3) - 6 = 0 \\implies 9 - 6k - 6 = 0 \\implies 3 - 6k = 0 \\implies 6k = 3 \\implies k = 0.5\\)."),

    # 39
    ("Can a quadratic equation have 3 distinct roots?",
     ["No, a polynomial of degree 2 can have at most 2 roots",
      "Yes, if the constant term is zero",
      "Yes, if the roots are irrational",
      "Yes, in complex numbers"],
     "A", "OSC", "easy",
     "According to the fundamental theorem of algebra, a polynomial of degree \\(n\\) has at most \\(n\\) roots. A quadratic equation cannot have more than 2 roots."),

    # 40
    ("If an equation of degree 2 has more than 2 distinct roots, what must it be?",
     ["An identity (where \\(a = b = c = 0\\))",
      "A cubic equation",
      "A linear equation",
      "An inconsistent equation"],
     "A", "OSC", "medium",
     "If \\(ax^2 + bx + c = 0\\) is satisfied by more than 2 distinct values of \\(x\\), it must be an identity where all coefficients are zero: \\(a = b = c = 0\\).")
]

# 30 PRACTICE (41-70)
t21_prac = [
    # 41
    ("Is \\(y^2 = 5y - 10\\) a quadratic equation?",
     ["Yes, in standard form \\(y^2 - 5y + 10 = 0\\), degree is 2",
      "No, because it has degree 1",
      "No, because the constant is 10",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "Rewriting gives \\(y^2 - 5y + 10 = 0\\). It has one variable \\(y\\) with maximum index 2, so it is a quadratic equation."),

    # 42
    ("Is \\(l + 2(l - 5) = 0\\) a quadratic equation?",
     ["No, expanding gives \\(3l - 10 = 0\\), which has degree 1 (linear)",
      "Yes, because \\(l\\) is multiplied",
      "Yes, because it has brackets",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(l + 2l - 10 = 0 \\implies 3l - 10 = 0\\). The degree is 1, so it is a linear equation, not quadratic."),

    # 43
    ("Is \\(x^2 + \\frac{2}{x} = 3\\) a quadratic equation?",
     ["No, multiplying by \\(x\\) gives \\(x^3 + 2 = 3x\\), which is cubic (degree 3)",
      "Yes, because \\(x^2\\) appears",
      "Yes, because 3 is positive",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "Clearing fraction gives \\(x^3 - 3x + 2 = 0\\). Degree is 3, not 2."),

    # 44
    ("What are \\(a, b, c\\) for \\(x^2 - 2x = -(3 - x)\\)?",
     ["\\(a = 1, b = -3, c = 3\\)",
      "\\(a = 1, b = -1, c = 3\\)",
      "\\(a = 1, b = -3, c = -3\\)",
      "\\(a = 1, b = 3, c = -3\\)"],
     "A", "OSC", "easy",
     "\\(x^2 - 2x = -3 + x \\implies x^2 - 3x + 3 = 0\\). Thus \\(a = 1, b = -3, c = 3\\)."),

    # 45
    ("What are \\(a, b, c\\) for \\(P(p + 1) = 2\\)?",
     ["\\(a = 1, b = 1, c = -2\\)",
      "\\(a = 1, b = 1, c = 2\\)",
      "\\(a = 1, b = -1, c = -2\\)",
      "\\(a = 2, b = 1, c = -2\\)"],
     "A", "OSC", "easy",
     "\\(p^2 + p - 2 = 0\\). Thus \\(a = 1, b = 1, c = -2\\)."),

    # 46
    ("Check if \\(x = -3\\) is a root of \\(2x^2 + 5x - 3 = 0\\).",
     ["Yes, \\(2(-3)^2 + 5(-3) - 3 = 18 - 15 - 3 = 0\\)",
      "No, because \\(18 - 15 - 3 \\neq 0\\)",
      "No, because -3 is negative",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(2(9) - 15 - 3 = 18 - 18 = 0\\). Hence \\(x = -3\\) is a root."),

    # 47
    ("Check if \\(x = \\frac{1}{2}\\) is a root of \\(2x^2 + 5x - 3 = 0\\).",
     ["Yes, \\(2(1/4) + 5(1/2) - 3 = 1/2 + 5/2 - 3 = 3 - 3 = 0\\)",
      "No, because \\(3 - 3 \\neq 0\\)",
      "No, because fractions cannot be roots",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(2(1/4) + 5/2 - 3 = 6/2 - 3 = 3 - 3 = 0\\). Hence \\(x = 1/2\\) is also a root."),

    # 48
    ("Find \\(k\\) if \\(x = 2\\) is a root of \\(kx^2 - 2x + 1 = 0\\).",
     ["\\(\\frac{3}{4}\\)", "\\(\\frac{4}{3}\\)", "1", "-1"],
     "A", "OSC", "easy",
     "\\(k(4) - 4 + 1 = 0 \\implies 4k - 3 = 0 \\implies k = 3/4\\)."),

    # 49
    ("Find \\(k\\) if \\(x = -1\\) is a root of \\(kx^2 + 3x + k = 0\\).",
     ["\\(\\frac{3}{2}\\)", "\\(-\\frac{3}{2}\\)", "3", "-3"],
     "A", "OSC", "medium",
     "\\(k(-1)^2 + 3(-1) + k = 0 \\implies k - 3 + k = 0 \\implies 2k = 3 \\implies k = 3/2\\)."),

    # 50
    ("Write \\(\\frac{x^2}{2} + 3x - 4 = 0\\) in standard integer coefficient form.",
     ["\\(x^2 + 6x - 8 = 0\\)",
      "\\(x^2 + 3x - 4 = 0\\)",
      "\\(2x^2 + 6x - 8 = 0\\)",
      "\\(x^2 + 6x - 4 = 0\\)"],
     "A", "OSC", "easy",
     "Multiply throughout by 2: \\(x^2 + 6x - 8 = 0\\)."),

    # 51
    ("What is the degree of \\((x + 1)(x - 2) = x^2 + 5\\)?",
     ["1, because \\(x^2\\) cancels, leaving \\(-x - 7 = 0\\) (linear)",
      "2, because \\(x^2\\) is present",
      "0, because it is constant",
      "3, cubic"],
     "A", "OSC", "medium",
     "\\(x^2 - x - 2 = x^2 + 5 \\implies -x - 7 = 0\\). The \\(x^2\\) term cancels! Degree is 1, so it is NOT quadratic."),

    # 52
    ("Decide whether \\(x(2x + 3) = x^2 + 1\\) is quadratic.",
     ["Yes, \\(2x^2 + 3x = x^2 + 1 \\implies x^2 + 3x - 1 = 0\\), degree is 2",
      "No, degree is 1",
      "No, degree is 3",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(2x^2 - x^2 + 3x - 1 = 0 \\implies x^2 + 3x - 1 = 0\\). Maximum index is 2, so it is quadratic."),

    # 53
    ("Find \\(a, b, c\\) for \\(4 = 5x - x^2\\) in standard form.",
     ["\\(x^2 - 5x + 4 = 0\\); \\(a = 1, b = -5, c = 4\\)",
      "\\(x^2 + 5x + 4 = 0\\); \\(a = 1, b = 5, c = 4\\)",
      "\\(-x^2 + 5x - 4 = 0\\); \\(a = -1, b = 5, c = 4\\)",
      "\\(x^2 - 5x - 4 = 0\\); \\(a = 1, b = -5, c = -4\\)"],
     "A", "OSC", "easy",
     "Moving all terms to LHS: \\(x^2 - 5x + 4 = 0\\). Thus \\(a = 1, b = -5, c = 4\\)."),

    # 54
    ("If \\(x = 4\\) is a root of \\(x^2 - 5x + 4 = 0\\), check if it is correct.",
     ["Yes, \\(4^2 - 5(4) + 4 = 16 - 20 + 4 = 0\\)",
      "No, because \\(16 - 20 + 4 \\neq 0\\)",
      "No, because 4 is composite",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(16 - 20 + 4 = 0\\). It is a root."),

    # 55
    ("Check if \\(x = 1\\) is also a root of \\(x^2 - 5x + 4 = 0\\).",
     ["Yes, \\(1^2 - 5(1) + 4 = 1 - 5 + 4 = 0\\)",
      "No, because \\(1 - 5 + 4 \\neq 0\\)",
      "No, because 1 is not prime",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(1 - 5 + 4 = 0\\). Both 1 and 4 are roots."),

    # 56
    ("Find \\(k\\) if \\(x = 3\\) is a root of \\(2x^2 + kx - 15 = 0\\).",
     ["-1", "1", "-3", "3"],
     "A", "OSC", "easy",
     "\\(2(9) + 3k - 15 = 0 \\implies 18 + 3k - 15 = 0 \\implies 3k + 3 = 0 \\implies 3k = -3 \\implies k = -1\\)."),

    # 57
    ("What are the roots of \\(x^2 - 16 = 0\\)?",
     ["\\(4\\) and \\(-4\\)", "\\(16\\) and \\(-16\\)", "\\(8\\) and \\(-8\\)", "\\(2\\) and \\(-2\\)"],
     "A", "OSC", "easy",
     "\\(x^2 = 16 \\implies x = \\pm \\sqrt{16} = \\pm 4\\)."),

    # 58
    ("What are the roots of \\(x^2 + 9 = 0\\) in the set of real numbers?",
     ["No real roots (roots are imaginary: \\(\\pm 3i\\))",
      "\\(3\\) and \\(-3\\)",
      "\\(9\\) and \\(-9\\)",
      "\\(0\\) and \\(9\\)"],
     "A", "OSC", "medium",
     "\\(x^2 = -9\\). Since the square of any real number cannot be negative, there are no real roots."),

    # 59
    ("What is the standard form of \\(x(x + 4) = 12\\)?",
     ["\\(x^2 + 4x - 12 = 0\\)",
      "\\(x^2 + 4x + 12 = 0\\)",
      "\\(x^2 - 4x - 12 = 0\\)",
      "\\(x^2 + 4x = 12\\)"],
     "A", "OSC", "easy",
     "\\(x^2 + 4x - 12 = 0\\)."),

    # 60
    ("In \\(ax^2 + bx + c = 0\\), if \\(b = 0\\), the equation is called a:",
     ["Pure quadratic equation", "Linear equation", "Cubic equation", "Identity"],
     "A", "OSC", "easy",
     "A quadratic equation containing no term with the first power of the variable (\\(b = 0\\), e.g. \\(ax^2 + c = 0\\)) is called a pure quadratic equation."),

    # 61
    ("In \\(ax^2 + bx + c = 0\\), if \\(c = 0\\), what is always one of the roots?",
     ["\\(x = 0\\)", "\\(x = 1\\)", "\\(x = -1\\)", "\\(x = a\\)"],
     "A", "OSC", "easy",
     "\\(ax^2 + bx = 0 \\implies x(ax + b) = 0 \\implies x = 0\\) or \\(x = -b/a\\). Thus \\(x = 0\\) is always a root."),

    # 62
    ("Find \\(k\\) if \\(x = -5\\) is a root of \\(2x^2 + 11x + k = 0\\).",
     ["5", "-5", "10", "-10"],
     "A", "OSC", "easy",
     "\\(2(-5)^2 + 11(-5) + k = 0 \\implies 2(25) - 55 + k = 0 \\implies 50 - 55 + k = 0 \\implies -5 + k = 0 \\implies k = 5\\)."),

    # 63
    ("Which of the following is in standard form?",
     ["\\(3x^2 - 7x + 2 = 0\\)",
      "\\(3x^2 = 7x - 2\\)",
      "\\(3x^2 - 7x = -2\\)",
      "\\(3x(x - 2) = 5\\)"],
     "A", "OSC", "easy",
     "Standard form has all terms on one side in descending powers of \\(x\\) equal to 0: \\(ax^2 + bx + c = 0\\)."),

    # 64
    ("What is the value of \\(a\\) in \\(-x^2 + 7x - 10 = 0\\)?",
     ["-1", "1", "7", "-10"],
     "A", "OSC", "easy",
     "The coefficient of \\(x^2\\) is \\(-1\\)."),

    # 65
    ("If \\(m^2 - 49 = 0\\), find the roots.",
     ["\\(7\\) and \\(-7\\)", "\\(49\\) and \\(-49\\)", "\\(0\\) and \\(7\\)", "\\(14\\) and \\(-14\\)"],
     "A", "OSC", "easy",
     "\\(m^2 = 49 \\implies m = \\pm 7\\)."),

    # 66
    ("If \\(3x^2 = 27\\), find the roots.",
     ["\\(3\\) and \\(-3\\)", "\\(9\\) and \\(-9\\)", "\\(1\\) and \\(-1\\)", "\\(27\\) and \\(-27\\)"],
     "A", "OSC", "easy",
     "\\(x^2 = 27/3 = 9 \\implies x = \\pm 3\\)."),

    # 67
    ("Is \\((x - 2)^2 + 1 = 2x - 3\\) a quadratic equation?",
     ["Yes, \\(x^2 - 4x + 4 + 1 = 2x - 3 \\implies x^2 - 6x + 8 = 0\\), degree is 2",
      "No, degree is 1",
      "No, degree is 3",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(x^2 - 4x + 5 - 2x + 3 = 0 \\implies x^2 - 6x + 8 = 0\\). It has degree 2, so it is quadratic."),

    # 68
    ("Is \\(x(x + 1) + 8 = (x + 2)(x - 2)\\) a quadratic equation?",
     ["No, \\(x^2 + x + 8 = x^2 - 4 \\implies x + 12 = 0\\), which is linear",
      "Yes, because \\(x^2\\) is present on both sides",
      "Yes, because 8 and 4 are constants",
      "Cannot be determined"],
     "A", "OSC", "medium",
     "Expanding gives \\(x^2 + x + 8 = x^2 - 4\\). The \\(x^2\\) terms cancel, resulting in \\(x + 12 = 0\\), which is linear."),

    # 69
    ("Find \\(k\\) if \\(x = 2\\) is a root of \\(x^2 + 2x - k = 0\\).",
     ["8", "-8", "4", "-4"],
     "A", "OSC", "easy",
     "\\(2^2 + 2(2) - k = 0 \\implies 4 + 4 - k = 0 \\implies k = 8\\)."),

    # 70
    ("If \\(f(x) = ax^2 + bx + c\\), the roots of the quadratic equation are the values of \\(x\\) where the graph \\(y = f(x)\\) intersects the:",
     ["X-axis (where y = 0)", "Y-axis (where x = 0)", "Origin only", "Line y = x"],
     "A", "OSC", "easy",
     "The roots of \\(f(x) = 0\\) are the X-coordinates of the points where the parabola crosses or touches the X-axis.")
]

# 12 MOCK (71-82)
t21_mock = [
    # 71
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0f172a" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Canonical Form: ax² + bx + c = 0</text>
  <text x="170" y="80" fill="#f8fafc" font-size="11" text-anchor="middle">Condition 1: One variable only</text>
  <text x="170" y="105" fill="#4ade80" font-size="11" text-anchor="middle">Condition 2: Maximum index is strictly 2 and a != 0</text>
</svg>
</div>
What are the two non-negotiable criteria for an equation to be quadratic?""",
     ["It must involve exactly one variable whose maximum power is 2, with leading coefficient a != 0",
      "It must have three variables and degree 1",
      "It must have degree 4 and two negative constants",
      "It must have no constant term"],
     "A", "OSC", "easy",
     "An algebraic equation is quadratic if and only if it contains a single variable whose highest exponent is exactly 2, and the coefficient of the squared term is non-zero."),

    # 72
    ("Decide whether \\(x^2 = 0\\) is a quadratic equation.",
     ["Yes, \\(a = 1 \\neq 0, b = 0, c = 0\\), degree is 2",
      "No, because the RHS is 0",
      "No, because b and c are missing",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(x^2 + 0x + 0 = 0\\). The leading coefficient \\(a = 1 \\neq 0\\) and maximum index is 2. Hence it is quadratic."),

    # 73
    ("Decide whether \\(3x + 5 = 0\\) is a quadratic equation.",
     ["No, because the leading coefficient a = 0 and degree is 1",
      "Yes, because 3 and 5 are real numbers",
      "Yes, if we add 0x²",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "The highest power of \\(x\\) is 1; there is no squared term with a non-zero coefficient. It is a linear equation."),

    # 74
    ("Find the roots of \\(x^2 = 25\\).",
     ["\\(5\\) and \\(-5\\)", "\\(25\\) and \\(-25\\)", "\\(0\\) and \\(5\\)", "\\(10\\) and \\(-10\\)"],
     "A", "OSC", "easy",
     "\\(x = \\pm \\sqrt{25} = \\pm 5\\)."),

    # 75
    ("What are the roots of \\(x^2 - 2x = 0\\)?",
     ["\\(0\\) and \\(2\\)", "\\(2\\) and \\(-2\\)", "\\(0\\) and \\(-2\\)", "\\(1\\) and \\(2\\)"],
     "A", "OSC", "easy",
     "\\(x(x - 2) = 0 \\implies x = 0\\) or \\(x = 2\\)."),

    # 76
    ("What are the roots of \\(x^2 + 3x = 0\\)?",
     ["\\(0\\) and \\(-3\\)", "\\(0\\) and \\(3\\)", "\\(3\\) and \\(-3\\)", "\\(1\\) and \\(-3\\)"],
     "A", "OSC", "easy",
     "\\(x(x + 3) = 0 \\implies x = 0\\) or \\(x = -3\\)."),

    # 77
    ("Find \\(k\\) if \\(x = -4\\) is a root of \\(x^2 + 5x + k = 0\\).",
     ["4", "-4", "20", "-20"],
     "A", "OSC", "easy",
     "\\((-4)^2 + 5(-4) + k = 0 \\implies 16 - 20 + k = 0 \\implies -4 + k = 0 \\implies k = 4\\)."),

    # 78
    ("Find \\(k\\) if \\(x = 1\\) is a root of \\(kx^2 - 5x + 2 = 0\\).",
     ["3", "-3", "5", "2"],
     "A", "OSC", "easy",
     "\\(k(1)^2 - 5(1) + 2 = 0 \\implies k - 3 = 0 \\implies k = 3\\)."),

    # 79
    ("What are the coefficients \\(a, b, c\\) for \\(5x^2 = 20\\)?",
     ["\\(a = 5, b = 0, c = -20\\)",
      "\\(a = 5, b = -20, c = 0\\)",
      "\\(a = 1, b = 0, c = -4\\)",
      "\\(a = 5, b = 20, c = 0\\)"],
     "A", "OSC", "easy",
     "\\(5x^2 + 0x - 20 = 0\\). Thus \\(a = 5, b = 0, c = -20\\)."),

    # 80
    ("What is the degree of \\((x + 1)^2 = 2(x - 3)\\)?",
     ["2, quadratic", "1, linear", "3, cubic", "0, constant"],
     "A", "OSC", "easy",
     "\\(x^2 + 2x + 1 = 2x - 6 \\implies x^2 + 7 = 0\\). Degree is 2, quadratic."),

    # 81
    ("If \\(x = 0\\) and \\(x = 1\\) are the roots of \\(x^2 - x = 0\\), verify if they are valid.",
     ["Both are valid roots because \\(0^2 - 0 = 0\\) and \\(1^2 - 1 = 0\\)",
      "Only 0 is valid",
      "Only 1 is valid",
      "Neither is valid"],
     "A", "OSC", "easy",
     "Substituting \\(x = 0\\) gives \\(0 = 0\\); substituting \\(x = 1\\) gives \\(1 - 1 = 0\\). Both are valid roots."),

    # 82
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0b132b" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1c2541" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Testing Roots by Substitution</text>
  <text x="170" y="80" fill="#4ade80" font-size="11" text-anchor="middle">LHS = RHS = 0 -> Value is a Root</text>
  <text x="170" y="105" fill="#f87171" font-size="11" text-anchor="middle">LHS != 0 -> Value is NOT a Root</text>
</svg>
</div>
What is the universal algebraic test to determine whether a given number is a root of an equation?""",
     ["Substitute the number into the variable of the equation; if LHS equals RHS (0 = 0), it is a root",
      "Take the square root of the number",
      "Multiply the number by the discriminant",
      "Check if the number is prime"],
     "A", "OSC", "easy",
     "A number \\(r\\) is a root of \\(P(x) = 0\\) if and only if \\(P(r) = 0\\). Direct substitution into the LHS to verify if it evaluates to 0 is the universal definition and test of a root.")
]

all_q_21 = build_topic_questions("MH-10-MTH1-2-2.1", t21_exam, t21_prac, t21_mock)
out_21 = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch2_t1.json")
with open(out_21, "w", encoding="utf-8") as f:
    json.dump(all_q_21, f, indent=2, ensure_ascii=False)
print(f"Generated {len(all_q_21)} questions for MH-10-MTH1-2-2.1 -> {out_21}")
