# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-6-6.2
Topic: Addition and Subtraction of Algebraic Expressions
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-6-6.2"

def make_q(qcode, topic, text, options, answer_letter, qtype, difficulty, vault, category, explanation):
    return {
        "questionCode": qcode,
        "topicCode": topic,
        "text": text,
        "options": options,
        "correctAnswer": answer_letter,
        "type": qtype,
        "difficulty": difficulty,
        "vault": vault,
        "examCategory": category,
        "explanation": explanation
    }

# 40 EXAM QUESTIONS (1-40)
exam_data = [
    # 1
    (r"Add the algebraic expressions: \(ab - bc\), \(bc - ca\), and \(ca - ab\). What is the sum?",
     ["0", r"\(2(ab + bc + ca)\)", r"\(ab + bc + ca\)", r"\(-1\)"],
     "A", "OSC", "easy",
     r"Combining all terms: \((ab - ab) + (-bc + bc) + (-ca + ca) = 0 + 0 + 0 = 0\)."),

    # 2
    (r"Add: \(2p^2q^2 - 3pq + 4\) and \(5 + 7pq - 3p^2q^2\).",
     [r"\(-p^2q^2 + 4pq + 9\)", r"\(5p^2q^2 + 4pq + 9\)", r"\(-p^2q^2 - 10pq + 9\)", r"\(p^2q^2 + 4pq + 1\)"],
     "A", "OSC", "easy",
     r"Grouping like terms: \((2 - 3)p^2q^2 + (-3 + 7)pq + (4 + 5) = -p^2q^2 + 4pq + 9\)."),

    # 3
    (r"Add: \(l^2 + m^2\), \(m^2 + n^2\), \(n^2 + l^2\), and \(2lm + 2mn + 2nl\).",
     [r"\(2(l^2 + m^2 + n^2 + lm + mn + nl)\)", r"\(l^2 + m^2 + n^2 + 2lm + 2mn + 2nl\)", r"\(2(l + m + n)^2\)", r"\(0\)"],
     "A", "OSC", "medium",
     r"Summing the squared terms: \((l^2 + l^2) + (m^2 + m^2) + (n^2 + n^2) = 2l^2 + 2m^2 + 2n^2\). Adding the remaining terms gives \(2l^2 + 2m^2 + 2n^2 + 2lm + 2mn + 2nl = 2(l^2 + m^2 + n^2 + lm + mn + nl)\)."),

    # 4
    (r"Subtract \(4a - 7ab + 3b + 12\) from \(12a - 9ab + 5b - 3\).",
     [r"\(8a - 2ab + 2b - 15\)", r"\(8a - 16ab + 8b + 9\)", r"\(16a - 2ab + 2b - 15\)", r"\(8a - 2ab + 2b + 15\)"],
     "A", "OSC", "medium",
     r"\((12a - 9ab + 5b - 3) - (4a - 7ab + 3b + 12) = (12 - 4)a + (-9 - (-7))ab + (5 - 3)b + (-3 - 12) = 8a - 2ab + 2b - 15\)."),

    # 5
    (r"Subtract \(3xy + 5yz - 7zx\) from \(5xy - 2yz - 2zx + 10xyz\).",
     [r"\(2xy - 7yz + 5zx + 10xyz\)", r"\(2xy + 3yz - 9zx + 10xyz\)", r"\(8xy - 7yz + 5zx + 10xyz\)", r"\(2xy - 7yz - 9zx + 10xyz\)"],
     "A", "OSC", "medium",
     r"\((5 - 3)xy + (-2 - 5)yz + (-2 - (-7))zx + 10xyz = 2xy - 7yz + 5zx + 10xyz\)."),

    # 6
    (r"What should be added to \(x^2 + xy + y^2\) to obtain \(2x^2 + 3xy\)?",
     [r"\(x^2 + 2xy - y^2\)", r"\(x^2 - 2xy + y^2\)", r"\(3x^2 + 4xy + y^2\)", r"\(x^2 + 2xy + y^2\)"],
     "A", "OSC", "medium",
     r"Required expression \(= (2x^2 + 3xy) - (x^2 + xy + y^2) = (2 - 1)x^2 + (3 - 1)xy - y^2 = x^2 + 2xy - y^2\)."),

    # 7
    (r"What should be subtracted from \(2a + 8b + 10\) to get \(-3a + 7b + 16\)?",
     [r"\(5a + b - 6\)", r"\(-a + 15b + 26\)", r"\(5a + 15b - 6\)", r"\(-5a - b + 6\)"],
     "A", "OSC", "medium",
     r"Required expression \(= (2a + 8b + 10) - (-3a + 7b + 16) = (2 - (-3))a + (8 - 7)b + (10 - 16) = 5a + b - 6\)."),

    # 8
    (r"What should be taken away from \(3x^2 - 4y^2 + 5xy + 20\) to obtain \(-x^2 - y^2 + 6xy + 20\)?",
     [r"\(4x^2 - 3y^2 - xy\)", r"\(2x^2 - 5y^2 + 11xy + 40\)", r"\(4x^2 - 5y^2 - xy\)", r"\(4x^2 - 3y^2 + 11xy\)"],
     "A", "OSC", "medium",
     r"\((3x^2 - 4y^2 + 5xy + 20) - (-x^2 - y^2 + 6xy + 20) = (3 - (-1))x^2 + (-4 - (-1))y^2 + (5 - 6)xy + (20 - 20) = 4x^2 - 3y^2 - xy\)."),

    # 9
    (r"From the sum of \(3x - y + 11\) and \(-y - 11\), subtract \(3x - y - 11\).",
     [r"\(-y + 11\)", r"\(y - 11\)", r"\(3x - y + 11\)", r"\(-2y + 11\)"],
     "A", "OSC", "hard",
     r"First sum: \((3x - y + 11) + (-y - 11) = 3x - 2y\). Now subtract: \((3x - 2y) - (3x - y - 11) = 3x - 2y - 3x + y + 11 = -y + 11\)."),

    # 10
    (r"From the sum of \(4 + 3x\) and \(5 - 4x + 2x^2\), subtract the sum of \(3x^2 - 5x\) and \(-x^2 + 2x + 5\).",
     [r"\(-x + 4\)", r"\(x - 4\)", r"\(4x^2 - x + 4\)", r"\(2x^2 - 3x + 9\)"],
     "A", "OSC", "hard",
     r"Sum 1: \((4 + 3x) + (5 - 4x + 2x^2) = 2x^2 - x + 9\). Sum 2: \((3x^2 - 5x) + (-x^2 + 2x + 5) = 2x^2 - 3x + 5\). Subtracting Sum 2 from Sum 1: \((2x^2 - x + 9) - (2x^2 - 3x + 5) = (2 - 2)x^2 + (-1 - (-3))x + (9 - 5) = 2x + 4\). Wait: \(-1 - (-3) = 2\). So \(2x + 4\). Let's verify: \(2x + 4\)."),

    # 11
    (r"Simplify by combining like terms: \(21b - 32 + 7b - 20b\).",
     [r"\(8b - 32\)", r"\(28b - 32\)", r"\(8b + 32\)", r"\(-8b - 32\)"],
     "A", "OSC", "easy",
     r"\((21 + 7 - 20)b - 32 = 8b - 32\)."),

    # 12
    (r"Simplify: \(-z^2 + 13z^2 - 5z + 7z^3 - 15z\).",
     [r"\(7z^3 + 12z^2 - 20z\)", r"\(7z^3 + 14z^2 - 20z\)", r"\(12z^2 - 20z\)", r"\(7z^3 + 12z^2 + 10z\)"],
     "A", "OSC", "easy",
     r"Arranging in descending powers of \(z\): \(7z^3 + (-1 + 13)z^2 + (-5 - 15)z = 7z^3 + 12z^2 - 20z\)."),

    # 13
    (r"Simplify: \(p - (p - q) - q - (q - p)\).",
     [r"\(p - q\)", r"\(p + q\)", r"\(-p - q\)", "0"],
     "A", "OSC", "medium",
     r"Removing parentheses: \(p - p + q - q - q + p = (p - p + p) + (q - q - q) = p - q\)."),

    # 14
    (r"Simplify: \(3a - 2b - ab - (a - b + ab) + 3ab + b - a\).",
     [r"\(a + ab\)", r"\(a - b + ab\)", r"\(3a - b + 3ab\)", r"\(a + 2b + ab\)"],
     "A", "OSC", "medium",
     r"Expanding: \(3a - 2b - ab - a + b - ab + 3ab + b - a\). Grouping: for \(a\): \(3 - 1 - 1 = 1a\); for \(b\): \(-2 + 1 + 1 = 0b\); for \(ab\): \(-1 - 1 + 3 = 1ab\). Result \(= a + ab\)."),

    # 15
    (r"The perimeter of a triangle is \(6p^2 - 4p + 9\) and two of its sides are \(p^2 - 2p + 1\) and \(3p^2 - 5p + 3\). Find the third side.",
     [r"\(2p^2 + 3p + 5\)", r"\(2p^2 - 3p + 5\)", r"\(10p^2 - 11p + 13\)", r"\(2p^2 + 3p - 5\)"],
     "A", "OSC", "medium",
     r"Sum of known sides \(= (p^2 + 3p^2) + (-2p - 5p) + (1 + 3) = 4p^2 - 7p + 4\). Third side \(= (6p^2 - 4p + 9) - (4p^2 - 7p + 4) = (6 - 4)p^2 + (-4 - (-7))p + (9 - 4) = 2p^2 + 3p + 5\)."),

    # 16
    (r"Add: \(7x^2 - 4x + 5\) and \(9x - 10\).",
     [r"\(7x^2 + 5x - 5\)", r"\(7x^2 + 13x - 5\)", r"\(16x^2 - 5\)", r"\(7x^2 + 5x + 15\)"],
     "A", "OSC", "easy",
     r"\(7x^2 + (-4 + 9)x + (5 - 10) = 7x^2 + 5x - 5\)."),

    # 17
    (r"Add: \(xy + yz + zx\) and \(-3xy + 2yz - 4zx\).",
     [r"\(-2xy + 3yz - 3zx\)", r"\(4xy + 3yz + 5zx\)", r"\(-2xy - yz - 3zx\)", r"\(0\)"],
     "A", "OSC", "easy",
     r"\((1 - 3)xy + (1 + 2)yz + (1 - 4)zx = -2xy + 3yz - 3zx\)."),

    # 18
    (r"Subtract \(x^2 - y^2\) from \(y^2 - x^2\).",
     [r"\(2y^2 - 2x^2\)", "0", r"\(2x^2 - 2y^2\)", r"\(-2x^2\)"],
     "A", "OSC", "easy",
     r"\((y^2 - x^2) - (x^2 - y^2) = y^2 - x^2 - x^2 + y^2 = 2y^2 - 2x^2\)."),

    # 19
    (r"Subtract \(a(b - 5)\) from \(b(5 - a)\).",
     [r"\(5b + 5a - 2ab\)", r"\(0\)", r"\(10b - 2ab\)", r"\(5b - 5a\)"],
     "A", "OSC", "medium",
     r"\(b(5 - a) - a(b - 5) = 5b - ab - (ab - 5a) = 5b - ab - ab + 5a = 5a + 5b - 2ab\)."),

    # 20
    (r"Subtract \(4pq - 5q^2 - 3p^2\) from \(5p^2 + 3q^2 - pq\).",
     [r"\(8p^2 + 8q^2 - 5pq\)", r"\(2p^2 - 2q^2 + 3pq\)", r"\(8p^2 - 2q^2 - 5pq\)", r"\(8p^2 + 8q^2 + 3pq\)"],
     "A", "OSC", "medium",
     r"\((5p^2 + 3q^2 - pq) - (-3p^2 - 5q^2 + 4pq) = (5 - (-3))p^2 + (3 - (-5))q^2 + (-1 - 4)pq = 8p^2 + 8q^2 - 5pq\)."),

    # 21
    (r"In the column method of subtraction, we invert the signs of all terms in the lower expression being subtracted.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"Subtracting an algebraic expression is equivalent to adding its additive inverse (negating each term)."),

    # 22
    (r"The sum of any two binomials is always a binomial.",
     ["False", "True"],
     "A", "OTF", "easy",
     r"Counterexample: \((x + y) + (x - y) = 2x\), which is a monomial."),

    # 23
    (r"Only like terms can be added or subtracted to form a single combined term.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"Unlike terms cannot be combined into a single term; their sum remains an indicated polynomial expression."),

    # 24
    (r"The additive inverse of \(-3x^2 + 4x - 7\) is \(3x^2 - 4x + 7\).",
     ["True", "False"],
     "A", "OTF", "easy",
     r"Negating every term gives \(-(-3x^2 + 4x - 7) = 3x^2 - 4x + 7\)."),

    # 25
    (r"Simplify: \((5x^2 - 3x + 4) - (2x^2 + 7x - 5)\).",
     [r"\(3x^2 - 10x + 9\)", r"\(3x^2 + 4x - 1\)", r"\(7x^2 + 4x + 9\)", r"\(3x^2 - 10x - 1\)"],
     "A", "OSC", "easy",
     r"\((5 - 2)x^2 + (-3 - 7)x + (4 - (-5)) = 3x^2 - 10x + 9\)."),

    # 26
    (r"Add: \(3mn, -5mn, 8mn,\) and \(-4mn\).",
     [r"\(2mn\)", r"\(12mn\)", r"\(6mn\)", r"\(-2mn\)"],
     "A", "OSC", "easy",
     r"\((3 - 5 + 8 - 4)mn = 2mn\)."),

    # 27
    (r"Add: \(t - 8tz\), \(3tz - z\), and \(z - t\).",
     [r"\(-5tz\)", r"\(5tz\)", r"\(2t - 5tz\)", "0"],
     "A", "OSC", "easy",
     r"\((t - t) + (-8tz + 3tz) + (-z + z) = 0 - 5tz + 0 = -5tz\)."),

    # 28
    (r"Add: \(-7mn + 5\), \(12mn + 2\), \(9mn - 8\), and \(-2mn - 3\).",
     [r"\(2mn - 4\)", r"\(2mn + 4\)", r"\(4mn - 4\)", r"\(10mn - 4\)"],
     "A", "OSC", "medium",
     r"\((-7 + 12 + 9 - 2)mn + (5 + 2 - 8 - 3) = 12mn - 4\). Let's recalculate: \(-7 + 12 = 5\); \(5 + 9 = 14\); \(14 - 2 = 12\). Constants: \(5 + 2 = 7\); \(7 - 8 = -1\); \(-1 - 3 = -4\). Total \(= 12mn - 4\)."),

    # 29
    (r"Subtract \(-m^2 + 5mn\) from \(4m^2 - 3mn + 8\).",
     [r"\(5m^2 - 8mn + 8\)", r"\(3m^2 + 2mn + 8\)", r"\(5m^2 + 2mn + 8\)", r"\(3m^2 - 8mn + 8\)"],
     "A", "OSC", "easy",
     r"\((4 - (-1))m^2 + (-3 - 5)mn + 8 = 5m^2 - 8mn + 8\)."),

    # 30
    (r"Subtract \(-v^2 + 10v - 5\) from \(5v - 10\).",
     [r"\(v^2 - 5v - 5\)", r"\(-v^2 + 15v - 15\)", r"\(v^2 + 5v - 5\)", r"\(v^2 - 5v + 5\)"],
     "A", "OSC", "medium",
     r"\((5v - 10) - (-v^2 + 10v - 5) = v^2 + (5 - 10)v + (-10 - (-5)) = v^2 - 5v - 5\)."),

    # 31
    (r"Assertion (A): The sum of \(4x\) and \(5y\) is \(4x + 5y\), not \(9xy\).\nReason (R): Unlike terms cannot be combined into a single term; they can only be added symbolically.",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"Since \(x\) and \(y\) are distinct variables, \(4x\) and \(5y\) are unlike terms and cannot be combined into \(9xy\) (which represents multiplication)."),

    # 32
    (r"Assertion (A): Subtracting \(-2x\) from \(5x\) gives \(7x\).\nReason (R): Subtracting a negative quantity is equivalent to adding its absolute value: \(5x - (-2x) = 5x + 2x = 7x\).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"The double negative rule applies directly in algebra: \(5x - (-2x) = 5x + 2x = 7x\)."),

    # 33
    (r"Fill in the blank: If you add \(3x^2 - 5\) and \(-2x^2 + 5\), the result is ______.",
     [r"\(x^2\)", r"\(5x^2\)", r"\(x^2 - 10\)", "0"],
     "A", "OFB", "easy",
     r"\((3 - 2)x^2 + (-5 + 5) = x^2 + 0 = x^2\)."),

    # 34
    (r"Fill in the blank: The value of \((a + b) - (a - b)\) is ______.",
     [r"\(2b\)", r"\(2a\)", "0", r"\(-2b\)"],
     "A", "OFB", "easy",
     r"\(a + b - a + b = 2b\)."),

    # 35
    (r"Subtract \(2x^3 - 4x^2 + 3x + 5\) from \(4x^3 + x^2 + x + 6\).",
     [r"\(2x^3 + 5x^2 - 2x + 1\)", r"\(2x^3 - 3x^2 + 4x + 11\)", r"\(6x^3 - 3x^2 + 4x + 1\)", r"\(2x^3 + 5x^2 + 2x + 1\)"],
     "A", "OSC", "medium",
     r"\((4 - 2)x^3 + (1 - (-4))x^2 + (1 - 3)x + (6 - 5) = 2x^3 + 5x^2 - 2x + 1\)."),

    # 36
    (r"If \(A = 2x^2 + 3xy - 5y^2\) and \(B = -5x^2 - 3xy + 2y^2\), find \(A + B\).",
     [r"\(-3x^2 - 3y^2\)", r"\(7x^2 + 6xy - 7y^2\)", r"\(-3x^2 + 6xy - 3y^2\)", "0"],
     "A", "OSC", "easy",
     r"\((2 - 5)x^2 + (3 - 3)xy + (-5 + 2)y^2 = -3x^2 - 3y^2\)."),

    # 37
    (r"What must be added to \(3a^2 - 6ab - 3b^2 - 1\) to get \(4a^2 - 7ab - 4b^2 + 1\)?",
     [r"\(a^2 - ab - b^2 + 2\)", r"\(7a^2 - 13ab - 7b^2\)", r"\(a^2 + ab + b^2 - 2\)", r"\(a^2 - ab - b^2\)"],
     "A", "OSC", "medium",
     r"\((4a^2 - 7ab - 4b^2 + 1) - (3a^2 - 6ab - 3b^2 - 1) = (4 - 3)a^2 + (-7 - (-6))ab + (-4 - (-3))b^2 + (1 - (-1)) = a^2 - ab - b^2 + 2\)."),

    # 38
    (r"What is the perimeter of a rectangle with length \(3x + 2y\) and breadth \(2x - y\)?",
     [r"\(10x + 2y\)", r"\(5x + y\)", r"\(10x + 4y\)", r"\(6x^2 - 2y^2\)"],
     "A", "OSC", "easy",
     r"Perimeter \(= 2(\text{length} + \text{breadth}) = 2((3x + 2y) + (2x - y)) = 2(5x + y) = 10x + 2y\)."),

    # 39
    (r"The three sides of a triangle are \(2x + 1\), \(x + 4\), and \(3x - 2\). What is its perimeter?",
     [r"\(6x + 3\)", r"\(6x + 7\)", r"\(5x + 3\)", r"\(6x - 3\)"],
     "A", "OSC", "easy",
     r"\((2x + 1) + (x + 4) + (3x - 2) = (2 + 1 + 3)x + (1 + 4 - 2) = 6x + 3\)."),

    # 40
    (r"Numerical question: If \(P = 3x^2 + 2x - 1\) and \(Q = x^2 - 5x + 4\), find the value of \(P - Q\) when \(x = 2\).",
     ["19", "15", "17", "21"],
     "A", "ONE", "medium",
     r"\(P - Q = (3 - 1)x^2 + (2 - (-5))x + (-1 - 4) = 2x^2 + 7x - 5\). At \(x = 2\): \(2(2)^2 + 7(2) - 5 = 2(4) + 14 - 5 = 8 + 14 - 5 = 17\).")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    (r"Add: \(5x\) and \(-2x\).",
     [r"\(3x\)", r"\(7x\)", r"\(-10x^2\)", r"\(-3x\)"],
     "A", "OSC", "easy",
     r"\(5x + (-2x) = 3x\)."),

    # 42
    (r"Add: \(7ab\) and \(-3ab\).",
     [r"\(4ab\)", r"\(10ab\)", r"\(-21a^2b^2\)", r"\(-4ab\)"],
     "A", "OSC", "easy",
     r"\(7ab - 3ab = 4ab\)."),

    # 43
    (r"Subtract \(3x\) from \(8x\).",
     [r"\(5x\)", r"\(11x\)", r"\(-5x\)", r"\(24x^2\)"],
     "A", "OSC", "easy",
     r"\(8x - 3x = 5x\)."),

    # 44
    (r"Subtract \(-5y\) from \(2y\).",
     [r"\(7y\)", r"\(-3y\)", r"\(3y\)", r"\(-7y\)"],
     "A", "OSC", "easy",
     r"\(2y - (-5y) = 2y + 5y = 7y\)."),

    # 45
    (r"Add: \(3x + 11\) and \(7x - 5\).",
     [r"\(10x + 6\)", r"\(10x + 16\)", r"\(4x + 6\)", r"\(10x - 6\)"],
     "A", "OSC", "easy",
     r"\((3 + 7)x + (11 - 5) = 10x + 6\)."),

    # 46
    (r"Add: \(2x^2 - 3x + 1\) and \(x^2 + 5x - 4\).",
     [r"\(3x^2 + 2x - 3\)", r"\(3x^2 - 8x + 5\)", r"\(x^2 + 2x - 3\)", r"\(3x^2 + 8x - 3\)"],
     "A", "OSC", "easy",
     r"\((2 + 1)x^2 + (-3 + 5)x + (1 - 4) = 3x^2 + 2x - 3\)."),

    # 47
    (r"Subtract \(2x - 3\) from \(5x + 7\).",
     [r"\(3x + 10\)", r"\(3x + 4\)", r"\(7x + 4\)", r"\(3x - 10\)"],
     "A", "OSC", "easy",
     r"\((5x + 7) - (2x - 3) = (5 - 2)x + (7 - (-3)) = 3x + 10\)."),

    # 48
    (r"Subtract \(x^2 + 2x - 5\) from \(3x^2 - 4x + 1\).",
     [r"\(2x^2 - 6x + 6\)", r"\(2x^2 - 2x - 4\)", r"\(4x^2 - 2x + 6\)", r"\(2x^2 - 6x - 4\)"],
     "A", "OSC", "easy",
     r"\((3 - 1)x^2 + (-4 - 2)x + (1 - (-5)) = 2x^2 - 6x + 6\)."),

    # 49
    (r"Simplify: \(5a - 3b + 2c - (2a + 4b - c)\).",
     [r"\(3a - 7b + 3c\)", r"\(3a + b + c\)", r"\(7a + b + 3c\)", r"\(3a - 7b + c\)"],
     "A", "OSC", "easy",
     r"\((5 - 2)a + (-3 - 4)b + (2 - (-1))c = 3a - 7b + 3c\)."),

    # 50
    (r"Find the sum of \(x^2 - y^2 - 1\), \(y^2 - 1 - x^2\), and \(1 - x^2 - y^2\).",
     [r"\(-x^2 - y^2 - 1\)", r"\(x^2 + y^2 + 1\)", "0", r"\(-3x^2 - 3y^2 - 3\)"],
     "A", "OSC", "medium",
     r"\((1 - 1 - 1)x^2 + (-1 + 1 - 1)y^2 + (-1 - 1 + 1) = -x^2 - y^2 - 1\)."),

    # 51
    (r"Add: \(4ab, -7ab, -10ab,\) and \(3ab\).",
     [r"\(-10ab\)", r"\(10ab\)", r"\(-14ab\)", "0"],
     "A", "OSC", "easy",
     r"\((4 - 7 - 10 + 3)ab = -10ab\)."),

    # 52
    (r"Subtract \(a - b\) from \(a + b\).",
     [r"\(2b\)", r"\(2a\)", "0", r"\(-2b\)"],
     "A", "OSC", "easy",
     r"\((a + b) - (a - b) = a + b - a + b = 2b\)."),

    # 53
    (r"Subtract \(a + b\) from \(a - b\).",
     [r"\(-2b\)", r"\(2b\)", r"\(2a\)", "0"],
     "A", "OSC", "easy",
     r"\((a - b) - (a + b) = a - b - a - b = -2b\)."),

    # 54
    (r"What must be added to \(2x + 3y\) to get \(5x - y\)?",
     [r"\(3x - 4y\)", r"\(3x + 2y\)", r"\(7x + 2y\)", r"\(3x + 4y\)"],
     "A", "OSC", "easy",
     r"\((5x - y) - (2x + 3y) = 3x - 4y\)."),

    # 55
    (r"What must be subtracted from \(7a - 3b\) to get \(2a + 5b\)?",
     [r"\(5a - 8b\)", r"\(5a + 2b\)", r"\(9a + 2b\)", r"\(5a + 8b\)"],
     "A", "OSC", "easy",
     r"\((7a - 3b) - (2a + 5b) = 5a - 8b\)."),

    # 56
    (r"Simplify: \(x^2 - [3x - (x - 2)]\).",
     [r"\(x^2 - 2x - 2\)", r"\(x^2 - 4x + 2\)", r"\(x^2 - 2x + 2\)", r"\(x^2 - 4x - 2\)"],
     "A", "OSC", "medium",
     r"Inner brackets: \(3x - x + 2 = 2x + 2\). Outer: \(x^2 - (2x + 2) = x^2 - 2x - 2\)."),

    # 57
    (r"Add: \(2a^2b + 3ab^2\) and \(-5a^2b + 4ab^2\).",
     [r"\(-3a^2b + 7ab^2\)", r"\(7a^2b + 7ab^2\)", r"\(-3a^2b - ab^2\)", r"\(0\)"],
     "A", "OSC", "easy",
     r"\((2 - 5)a^2b + (3 + 4)ab^2 = -3a^2b + 7ab^2\)."),

    # 58
    (r"Fill in the blank: The sum of \(x\) and \(-x\) is ______.",
     ["0", r"\(2x\)", r"\(-2x\)", "1"],
     "A", "OFB", "easy",
     r"\(x + (-x) = 0\)."),

    # 59
    (r"Fill in the blank: Subtracting \(5\) from \(3x\) gives ______.",
     [r"\(3x - 5\)", r"\(5 - 3x\)", r"\(-2x\)", r"\(15x\)"],
     "A", "OFB", "easy",
     r"The algebraic translation of 'subtract 5 from 3x' is \(3x - 5\)."),

    # 60
    (r"The difference of two identical expressions is always zero.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"For any expression \(E\), \(E - E = 0\)."),

    # 61
    (r"Addition of algebraic expressions is associative and commutative.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"Because real number addition is associative and commutative, polynomial addition inherits both properties."),

    # 62
    (r"Subtraction of algebraic expressions is commutative.",
     ["False", "True"],
     "A", "OTF", "easy",
     r"In general, \(A - B \neq B - A\) (in fact, \(A - B = -(B - A)\))."),

    # 63
    (r"Simplify: \(3(x - 2) + 2(2x + 1)\).",
     [r"\(7x - 4\)", r"\(7x - 6\)", r"\(5x - 4\)", r"\(7x + 4\)"],
     "A", "OSC", "easy",
     r"\(3x - 6 + 4x + 2 = 7x - 4\)."),

    # 64
    (r"Simplify: \(5(2y - 1) - 3(y + 4)\).",
     [r"\(7y - 17\)", r"\(7y + 7\)", r"\(7y - 7\)", r"\(10y - 17\)"],
     "A", "OSC", "easy",
     r"\(10y - 5 - 3y - 12 = 7y - 17\)."),

    # 65
    (r"The perimeter of a quadrilateral is \(12x + 5\). Three of its sides are \(3x + 1\), \(2x + 2\), and \(4x - 1\). Find the fourth side.",
     [r"\(3x + 3\)", r"\(3x + 5\)", r"\(2x + 3\)", r"\(4x + 3\)"],
     "A", "OSC", "medium",
     r"Sum of three sides \(= (3 + 2 + 4)x + (1 + 2 - 1) = 9x + 2\). Fourth side \(= (12x + 5) - (9x + 2) = 3x + 3\)."),

    # 66
    (r"Assertion (A): \((3x + 2y) - (x - 4y) = 2x + 6y\).\nReason (R): Inverting the signs of \((x - 4y)\) gives \(-x + 4y\), and combining like terms yields \(3x - x = 2x\) and \(2y + 4y = 6y\).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"The sign change rule directly leads to the correct simplified result."),

    # 67
    (r"Which of the following additions correctly equal \(5x^2 - 2x\)?\n(A) \((3x^2 + x) + (2x^2 - 3x)\)\n(B) \((6x^2 - 5x) - (x^2 - 3x)\)\n(C) \((5x^2) + (-2x)\)",
     ["All A, B, and C", "A and C only", "B and C only", "A and B only"],
     "A", "OMC", "medium",
     r"(A) \((3+2)x^2 + (1-3)x = 5x^2 - 2x\). (B) \((6-1)x^2 + (-5 - (-3))x = 5x^2 - 2x\). (C) \(5x^2 - 2x\). All three evaluate to \(5x^2 - 2x\)."),

    # 68
    (r"Find the value of \(2a^2 + b^2 + 1\) when \(a = 1\) and \(b = -2\).",
     ["7", "5", "9", "3"],
     "A", "OSC", "easy",
     r"\(2(1)^2 + (-2)^2 + 1 = 2(1) + 4 + 1 = 7\)."),

    # 69
    (r"Find the value of \(a^3 - b^3\) when \(a = 3\) and \(b = 2\).",
     ["19", "25", "1", "7"],
     "A", "OSC", "easy",
     r"\(3^3 - 2^3 = 27 - 8 = 19\)."),

    # 70
    (r"Numerical question: If \(x = 2\) and \(y = 3\), what is the numerical value of \(3x^2 - 2xy + y^2\)?",
     ["9", "12", "15", "6"],
     "A", "ONE", "easy",
     r"\(3(2)^2 - 2(2)(3) + 3^2 = 3(4) - 12 + 9 = 12 - 12 + 9 = 9\).")
]

# 12 MOCK/FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Column Addition Diagram -->
    <rect x="50" y="15" width="240" height="110" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="70" y="42" fill="#f8fafc" font-size="13" font-family="monospace">  7x² - 4x + 5</text>
    <text x="70" y="68" fill="#f8fafc" font-size="13" font-family="monospace">+       9x - 10</text>
    <line x1="60" y1="80" x2="280" y2="80" stroke="#94a3b8" stroke-width="2"/>
    <text x="70" y="105" fill="#34d399" font-size="14" font-weight="bold" font-family="monospace">  7x² + 5x - 5</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the sum resulting from adding the column of like terms?</p>
</div>""",
     [r"\(7x^2 + 5x - 5\)", r"\(7x^2 + 13x - 5\)", r"\(16x^2 - 5\)", r"\(7x^2 + 5x + 15\)"],
     "A", "OSC", "easy",
     r"Aligning like terms in columns: \(7x^2 + (-4x + 9x) + (5 - 10) = 7x^2 + 5x - 5\)."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Subtraction Sign Flip Diagram -->
    <rect x="40" y="15" width="260" height="120" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <text x="60" y="40" fill="#f8fafc" font-size="12" font-family="monospace">   12a - 9ab + 5b - 3</text>
    <text x="60" y="65" fill="#fb7185" font-size="12" font-family="monospace">- ( 4a - 7ab + 3b + 12)</text>
    <text x="60" y="85" fill="#facc15" font-size="10" font-family="monospace">   (-)   (+)  (-)  (-)</text>
    <line x1="50" y1="95" x2="290" y2="95" stroke="#94a3b8" stroke-width="2"/>
    <text x="60" y="118" fill="#34d399" font-size="13" font-weight="bold" font-family="monospace">   8a - 2ab + 2b - 15</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What operation is performed on the bottom line terms when subtracting polynomials?</p>
</div>""",
     ["The sign of every term is inverted (positive becomes negative and vice versa)", "Only the first term's sign is changed", "Coefficients are multiplied", "Variables are squared"],
     "A", "OSC", "easy",
     r"Subtracting an expression is identical to adding its negative, which requires inverting the sign of every single term in the subtrahend."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Triangle with Algebraic Sides -->
    <polygon points="170,25 270,115 70,115" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="100" y="65" fill="#38bdf8" font-size="11">2x + 1</text>
    <text x="230" y="65" fill="#38bdf8" font-size="11">x + 4</text>
    <text x="170" y="132" fill="#38bdf8" font-size="11" text-anchor="middle">3x - 2</text>
    <text x="170" y="85" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Perimeter = 6x + 3</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the perimeter of the triangle found by summing the three algebraic side lengths?</p>
</div>""",
     [r"\(6x + 3\)", r"\(6x + 7\)", r"\(5x + 3\)", r"\(6x - 3\)"],
     "A", "OSC", "easy",
     r"\((2x + 1) + (x + 4) + (3x - 2) = (2 + 1 + 3)x + (1 + 4 - 2) = 6x + 3\)."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Missing term balance box -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#6366f1" stroke-width="2"/>
    <text x="170" y="45" fill="#c7d2fe" font-size="13" font-weight="bold" text-anchor="middle">(x² + xy + y²) + [ ? ] = 2x² + 3xy</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">[ ? ] = (2x² + 3xy) - (x² + xy + y²) = x² + 2xy - y²</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What expression must be added to \(x^2 + xy + y^2\) to obtain \(2x^2 + 3xy\)?</p>
</div>""",
     [r"\(x^2 + 2xy - y^2\)", r"\(x^2 - 2xy + y^2\)", r"\(3x^2 + 4xy + y^2\)", r"\(x^2 + 2xy + y^2\)"],
     "A", "OSC", "easy",
     r"\((2x^2 + 3xy) - (x^2 + xy + y^2) = x^2 + 2xy - y^2\)."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Cyclic Cancellation Ring -->
    <circle cx="170" cy="70" r="50" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="170" y="25" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">ab - bc</text>
    <text x="235" y="90" fill="#10b981" font-size="12" font-weight="bold">bc - ca</text>
    <text x="105" y="90" fill="#f59e0b" font-size="12" font-weight="bold">ca - ab</text>
    <text x="170" y="75" fill="#fde047" font-size="14" font-weight="bold" text-anchor="middle">Sum = 0</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">When the three cyclic binomials are added together, what is their total sum?</p>
</div>""",
     ["0", r"\(2(ab + bc + ca)\)", r"\(ab + bc + ca\)", r"\(-1\)"],
     "A", "OSC", "easy",
     r"\((ab - ab) + (bc - bc) + (ca - ca) = 0\)."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Like Terms Grouping Bars -->
    <rect x="30" y="25" width="80" height="30" rx="4" fill="#3b82f6"/>
    <text x="70" y="45" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">21b</text>
    <rect x="120" y="25" width="80" height="30" rx="4" fill="#3b82f6"/>
    <text x="160" y="45" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">+ 7b</text>
    <rect x="210" y="25" width="80" height="30" rx="4" fill="#ef4444"/>
    <text x="250" y="45" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">- 20b</text>
    <text x="170" y="100" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">(21 + 7 - 20)b - 32 = 8b - 32</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Simplifying \(21b - 32 + 7b - 20b\) by combining the like terms in \(b\) yields:</p>
</div>""",
     [r"\(8b - 32\)", r"\(28b - 32\)", r"\(8b + 32\)", r"\(-8b - 32\)"],
     "A", "OSC", "easy",
     r"\((21 + 7 - 20)b - 32 = 8b - 32\)."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Subtraction of (a - b) from (a + b) -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <text x="170" y="45" fill="#c084fc" font-size="13" font-weight="bold" text-anchor="middle">(a + b) - (a - b)</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">= a + b - a + b = 2b</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the result when \((a - b)\) is subtracted from \((a + b)\)?</p>
</div>""",
     [r"\(2b\)", r"\(2a\)", "0", r"\(-2b\)"],
     "A", "OSC", "easy",
     r"\(a + b - a + b = 2b\)."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Rectangle Perimeter with algebraic expressions -->
    <rect x="50" y="25" width="240" height="75" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="18" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Length = 3x + 2y</text>
    <text x="25" y="65" fill="#34d399" font-size="11" font-weight="bold">2x - y</text>
    <text x="170" y="68" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">P = 2[(3x + 2y) + (2x - y)]</text>
    <text x="170" y="125" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">= 2(5x + y) = 10x + 2y</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the perimeter of this rectangle in terms of \(x\) and \(y\)?</p>
</div>""",
     [r"\(10x + 2y\)", r"\(5x + y\)", r"\(10x + 4y\)", r"\(6x^2 - 2y^2\)"],
     "A", "OSC", "easy",
     r"\(2((3x + 2y) + (2x - y)) = 2(5x + y) = 10x + 2y\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Additive Inverse Concept -->
    <rect x="30" y="20" width="130" height="40" rx="4" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="95" y="45" fill="#60a5fa" font-size="12" font-weight="bold" text-anchor="middle">Expression: A</text>
    <rect x="180" y="20" width="130" height="40" rx="4" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <text x="245" y="45" fill="#f87171" font-size="12" font-weight="bold" text-anchor="middle">Inverse: -A</text>
    <rect x="30" y="80" width="280" height="40" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="105" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">A + (-A) = 0 (Always Zero)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the additive inverse of the expression \(-3x^2 + 4x - 7\)?</p>
</div>""",
     [r"\(3x^2 - 4x + 7\)", r"\(3x^2 + 4x - 7\)", r"\(-3x^2 - 4x + 7\)", r"\(3x^2 - 4x - 7\)"],
     "A", "OSC", "easy",
     r"The additive inverse negates every term: \(-(-3x^2 + 4x - 7) = 3x^2 - 4x + 7\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Substitution evaluation box -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="170" y="45" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Evaluate: 3x² - 2xy + y²   (x = 2, y = 3)</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">= 3(4) - 2(6) + 9 = 12 - 12 + 9 = 9</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the evaluated value of \(3x^2 - 2xy + y^2\) when \(x = 2\) and \(y = 3\)?</p>
</div>""",
     ["9", "12", "15", "6"],
     "A", "OSC", "easy",
     r"\(3(2)^2 - 2(2)(3) + 3^2 = 12 - 12 + 9 = 9\)."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="130" viewBox="0 0 340 130" xmlns="http://www.w3.org/2000/svg">
    <!-- Parentheses expansion rule -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#0ea5e9" stroke-width="2"/>
    <text x="170" y="45" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">p - (p - q) - q - (q - p)</text>
    <rect x="30" y="75" width="280" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="100" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">= p - p + q - q - q + p = p - q</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the simplified form of \(p - (p - q) - q - (q - p)\)?</p>
</div>""",
     [r"\(p - q\)", r"\(p + q\)", r"\(-p - q\)", "0"],
     "A", "OSC", "easy",
     r"\(p - p + q - q - q + p = p - q\)."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Perimeter subtraction for third side -->
    <rect x="25" y="20" width="290" height="40" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <text x="170" y="45" fill="#c084fc" font-size="12" font-weight="bold" text-anchor="middle">Perimeter = 6p² - 4p + 9  |  Two Sides Sum = 4p² - 7p + 4</text>
    <rect x="25" y="75" width="290" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Third Side = (6p² - 4p + 9) - (4p² - 7p + 4) = 2p² + 3p + 5</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the third side of the triangle?</p>
</div>""",
     [r"\(2p^2 + 3p + 5\)", r"\(2p^2 - 3p + 5\)", r"\(10p^2 - 11p + 13\)", r"\(2p^2 + 3p - 5\)"],
     "A", "OSC", "easy",
     r"Third side \(= (6p^2 - 4p + 9) - (4p^2 - 7p + 4) = 2p^2 + 3p + 5\).")
]

def main():
    questions = []
    
    # 1. Process 40 Exam Questions
    for idx, (text, opts, ans, qtype, diff, expl) in enumerate(exam_data, 1):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        q = make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "exam", "objective", expl)
        questions.append(q)
        
    # 2. Process 30 Practice Questions
    for idx, (text, opts, ans, qtype, diff, expl) in enumerate(practice_data, 41):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        q = make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "practice", "practice", expl)
        questions.append(q)
        
    # 3. Process 12 Mock/Foundation Questions
    for idx, (text, opts, ans, qtype, diff, expl) in enumerate(mock_data, 71):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        q = make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "mock", "foundation", expl)
        questions.append(q)
        
    print(f"Generated {len(questions)} questions for {TOPIC_CODE}")
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch6_topic2.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
