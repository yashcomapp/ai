# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-6-6.4
Topic: Standard Algebraic Identities & Geometric Proofs
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-6-6.4"

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
    (r"What is the definition of an algebraic identity?",
     ["An equality that is true for ALL values of the variables", "An equation true for only one value of the variable", "An expression without an equal sign", "A formula with no variables"],
     "A", "OSC", "easy",
     r"An identity is an equality relationship that remains true for any real value chosen for its variables, unlike a conditional equation which holds true only for specific root values."),

    # 2
    (r"Which of the following is Standard Identity I?",
     [r"\((a + b)^2 = a^2 + 2ab + b^2\)", r"\((a - b)^2 = a^2 - 2ab + b^2\)", r"\((a + b)(a - b) = a^2 - b^2\)", r"\((x + a)(x + b) = x^2 + (a + b)x + ab\)"],
     "A", "OSC", "easy",
     r"Standard Identity I expresses the square of a sum: \((a + b)^2 = a^2 + 2ab + b^2\)."),

    # 3
    (r"Which of the following is Standard Identity II?",
     [r"\((a - b)^2 = a^2 - 2ab + b^2\)", r"\((a + b)^2 = a^2 + 2ab + b^2\)", r"\((a + b)(a - b) = a^2 - b^2\)", r"\((a - b)^2 = a^2 - b^2\)"],
     "A", "OSC", "easy",
     r"Standard Identity II expresses the square of a difference: \((a - b)^2 = a^2 - 2ab + b^2\)."),

    # 4
    (r"Which of the following is Standard Identity III?",
     [r"\((a + b)(a - b) = a^2 - b^2\)", r"\((a + b)(a - b) = a^2 + b^2\)", r"\((a - b)^2 = a^2 - b^2\)", r"\((a + b)^2 = a^2 + b^2\)"],
     "A", "OSC", "easy",
     r"Standard Identity III is the difference of two squares: \((a + b)(a - b) = a^2 - b^2\)."),

    # 5
    (r"Expand using a suitable identity: \((2y + 5)^2\).",
     [r"\(4y^2 + 20y + 25\)", r"\(4y^2 + 10y + 25\)", r"\(4y^2 + 25\)", r"\(2y^2 + 20y + 25\)"],
     "A", "OSC", "easy",
     r"Using \((a + b)^2 = a^2 + 2ab + b^2\): \((2y)^2 + 2(2y)(5) + 5^2 = 4y^2 + 20y + 25\)."),

    # 6
    (r"Expand: \((2a - 7)^2\).",
     [r"\(4a^2 - 28a + 49\)", r"\(4a^2 - 14a + 49\)", r"\(4a^2 - 49\)", r"\(4a^2 + 28a + 49\)"],
     "A", "OSC", "easy",
     r"Using \((a - b)^2 = a^2 - 2ab + b^2\): \((2a)^2 - 2(2a)(7) + 7^2 = 4a^2 - 28a + 49\)."),

    # 7
    (r"Expand: \(\left(3a - \frac{1}{2}\right)^2\).",
     [r"\(9a^2 - 3a + \frac{1}{4}\)", r"\(9a^2 - 6a + \frac{1}{4}\)", r"\(9a^2 - \frac{1}{4}\)", r"\(9a^2 + 3a + \frac{1}{4}\)"],
     "A", "OSC", "medium",
     r"\((3a)^2 - 2(3a)\left(\frac{1}{2}\right) + \left(\frac{1}{2}\right)^2 = 9a^2 - 3a + \frac{1}{4}\)."),

    # 8
    (r"Expand: \((1.1m - 0.4)(1.1m + 0.4)\).",
     [r"\(1.21m^2 - 0.16\)", r"\(1.21m^2 + 0.16\)", r"\(1.21m^2 - 0.88m - 0.16\)", r"\(1.1m^2 - 0.16\)"],
     "A", "OSC", "easy",
     r"Using \((a - b)(a + b) = a^2 - b^2\): \((1.1m)^2 - (0.4)^2 = 1.21m^2 - 0.16\)."),

    # 9
    (r"Expand: \((a^2 + b^2)(-a^2 + b^2)\).",
     [r"\(b^4 - a^4\)", r"\(a^4 - b^4\)", r"\(a^4 + b^4\)", r"\(-a^4 - b^4\)"],
     "A", "OSC", "medium",
     r"Rearranging terms: \((b^2 + a^2)(b^2 - a^2) = (b^2)^2 - (a^2)^2 = b^4 - a^4\)."),

    # 10
    (r"Expand: \((6x - 7)(6x + 7)\).",
     [r"\(36x^2 - 49\)", r"\(36x^2 + 49\)", r"\(36x^2 - 84x - 49\)", r"\(12x^2 - 49\)"],
     "A", "OSC", "easy",
     r"\((6x)^2 - 7^2 = 36x^2 - 49\)."),

    # 11
    (r"Expand: \((-a + c)(-a + c)\).",
     [r"\(c^2 - 2ac + a^2\)", r"\(a^2 - c^2\)", r"\(c^2 + 2ac + a^2\)", r"\(-a^2 + c^2\)"],
     "A", "OSC", "easy",
     r"\((-a + c)^2 = (c - a)^2 = c^2 - 2ac + a^2\)."),

    # 12
    (r"Expand: \(\left(\frac{x}{2} + \frac{3y}{4}\right)\left(\frac{x}{2} + \frac{3y}{4}\right)\).",
     [r"\(\frac{x^2}{4} + \frac{3xy}{4} + \frac{9y^2}{16}\)", r"\(\frac{x^2}{4} + \frac{9y^2}{16}\)", r"\(\frac{x^2}{4} + \frac{3xy}{2} + \frac{9y^2}{16}\)", r"\(\frac{x^2}{2} + \frac{3xy}{4} + \frac{3y^2}{4}\)"],
     "A", "OSC", "medium",
     r"\(\left(\frac{x}{2}\right)^2 + 2\left(\frac{x}{2}\right)\left(\frac{3y}{4}\right) + \left(\frac{3y}{4}\right)^2 = \frac{x^2}{4} + \frac{3xy}{4} + \frac{9y^2}{16}\)."),

    # 13
    (r"Expand: \((7a - 9b)^2\).",
     [r"\(49a^2 - 126ab + 81b^2\)", r"\(49a^2 - 63ab + 81b^2\)", r"\(49a^2 - 81b^2\)", r"\(49a^2 + 126ab + 81b^2\)"],
     "A", "OSC", "easy",
     r"\((7a)^2 - 2(7a)(9b) + (9b)^2 = 49a^2 - 126ab + 81b^2\)."),

    # 14
    (r"Expand: \((xy + 3z)^2\).",
     [r"\(x^2y^2 + 6xyz + 9z^2\)", r"\(x^2y^2 + 3xyz + 9z^2\)", r"\(x^2y^2 + 9z^2\)", r"\(xy^2 + 6xyz + 9z^2\)"],
     "A", "OSC", "easy",
     r"\((xy)^2 + 2(xy)(3z) + (3z)^2 = x^2y^2 + 6xyz + 9z^2\)."),

    # 15
    (r"Expand: \((6x^2 - 5y)^2\).",
     [r"\(36x^4 - 60x^2y + 25y^2\)", r"\(36x^4 - 30x^2y + 25y^2\)", r"\(36x^4 - 25y^2\)", r"\(36x^2 - 60x^2y + 25y^2\)"],
     "A", "OSC", "medium",
     r"\((6x^2)^2 - 2(6x^2)(5y) + (5y)^2 = 36x^4 - 60x^2y + 25y^2\)."),

    # 16
    (r"Simplify: \((3x + 7)^2 - 84x\).",
     [r"\((3x - 7)^2\)", r"\((3x + 7)^2\)", r"\(9x^2 + 49\)", r"\(9x^2 - 42x\)"],
     "A", "OSC", "medium",
     r"\((9x^2 + 42x + 49) - 84x = 9x^2 - 42x + 49 = (3x - 7)^2\)."),

    # 17
    (r"Simplify: \((9p - 5q)^2 + 180pq\).",
     [r"\((9p + 5q)^2\)", r"\((9p - 5q)^2\)", r"\(81p^2 + 25q^2\)", r"\(81p^2 - 25q^2\)"],
     "A", "OSC", "medium",
     r"\((81p^2 - 90pq + 25q^2) + 180pq = 81p^2 + 90pq + 25q^2 = (9p + 5q)^2\)."),

    # 18
    (r"Simplify: \(\left(\frac{4}{3}m - \frac{3}{4}n\right)^2 + 2mn\).",
     [r"\(\frac{16}{9}m^2 + \frac{9}{16}n^2\)", r"\(\frac{16}{9}m^2 - \frac{9}{16}n^2\)", r"\(\frac{16}{9}m^2 + 4mn + \frac{9}{16}n^2\)", "0"],
     "A", "OSC", "hard",
     r"Expanding the square: \(\frac{16}{9}m^2 - 2\left(\frac{4}{3}m\right)\left(\frac{3}{4}n\right) + \frac{9}{16}n^2 = \frac{16}{9}m^2 - 2mn + \frac{9}{16}n^2\). Adding \(2mn\) cancels the middle term, leaving \(\frac{16}{9}m^2 + \frac{9}{16}n^2\)."),

    # 19
    (r"Simplify: \((4pq + 3q)^2 - (4pq - 3q)^2\).",
     [r"\(48pq^2\)", r"\(24pq^2\)", r"\(16p^2q^2 + 9q^2\)", "0"],
     "A", "OSC", "medium",
     r"Using \((A + B)^2 - (A - B)^2 = 4AB\): \(4(4pq)(3q) = 48pq^2\)."),

    # 20
    (r"Simplify: \((a - b)(a + b) + (b - c)(b + c) + (c - a)(c + a)\).",
     ["0", r"\(2(a^2 + b^2 + c^2)\)", r"\(a^2 + b^2 + c^2\)", r"\(-1\)"],
     "A", "OSC", "easy",
     r"\((a^2 - b^2) + (b^2 - c^2) + (c^2 - a^2) = 0\)."),

    # 21
    (r"The equation \(x^2 - 4 = (x - 2)(x + 2)\) is an identity.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"This equation holds true for every real value of \(x\), satisfying the definition of an identity."),

    # 22
    (r"The equation \(x + 1 = 5\) is an algebraic identity.",
     ["False", "True"],
     "A", "OTF", "easy",
     r"\(x + 1 = 5\) is a conditional equation that holds true ONLY for \(x = 4\), not for all real numbers."),

    # 23
    (r"Geometrically, \((a + b)^2\) represents the area of a square of side \((a + b)\).",
     ["True", "False"],
     "A", "OTF", "easy",
     r"A square of side \(a + b\) has area \((a + b) \times (a + b) = a^2 + 2ab + b^2\)."),

    # 24
    (r"In the geometric dissection of \((a + b)^2\), the square is partitioned into 2 squares and 2 congruent rectangles.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"The four regions are a square of area \(a^2\), a square of area \(b^2\), and two rectangles each of area \(ab\)."),

    # 25
    (r"Simplify: \((2x + 5)^2 - (2x - 5)^2\).",
     [r"\(40x\)", r"\(20x\)", r"\(8x^2 + 50\)", "0"],
     "A", "OSC", "easy",
     r"Using \((A + B)^2 - (A - B)^2 = 4AB\): \(4(2x)(5) = 40x\)."),

    # 26
    (r"Simplify: \((7m - 8n)^2 + (7m + 8n)^2\).",
     [r"\(98m^2 + 128n^2\)", r"\(98m^2 - 128n^2\)", r"\(49m^2 + 64n^2\)", r"\(224mn\)"],
     "A", "OSC", "medium",
     r"Using \((A - B)^2 + (A + B)^2 = 2(A^2 + B^2)\): \(2(49m^2 + 64n^2) = 98m^2 + 128n^2\)."),

    # 27
    (r"Simplify: \((m^2 - n^2m)^2 + 2m^3n^2\).",
     [r"\(m^4 + n^4m^2\)", r"\(m^4 - n^4m^2\)", r"\(m^4 + 4m^3n^2 + n^4m^2\)", r"\(m^4\)"],
     "A", "OSC", "hard",
     r"Expanding the square: \((m^2)^2 - 2(m^2)(n^2m) + (n^2m)^2 = m^4 - 2m^3n^2 + n^4m^2\). Adding \(2m^3n^2\) cancels the middle term, leaving \(m^4 + n^4m^2\)."),

    # 28
    (r"Which identity is best suited to expand \((x + 4)(x + 7)\)?",
     [r"\((x + a)(x + b) = x^2 + (a + b)x + ab\)", r"\((a + b)^2 = a^2 + 2ab + b^2\)", r"\((a - b)^2 = a^2 - 2ab + b^2\)", r"\((a + b)(a - b) = a^2 - b^2\)"],
     "A", "OSC", "easy",
     r"Standard Identity IV is designed specifically for binomials sharing a common variable \(x\) with different constants \(a\) and \(b\)."),

    # 29
    (r"Expand using Identity IV: \((4x - 5)(4x - 1)\).",
     [r"\(16x^2 - 24x + 5\)", r"\(16x^2 + 24x + 5\)", r"\(16x^2 - 20x + 5\)", r"\(16x^2 - 5\)"],
     "A", "OSC", "medium",
     r"Using \((X + a)(X + b) = X^2 + (a + b)X + ab\) where \(X = 4x, a = -5, b = -1\): \((4x)^2 + (-5 - 1)(4x) + (-5)(-1) = 16x^2 - 24x + 5\)."),

    # 30
    (r"Expand: \((4x + 5)(4x - 1)\).",
     [r"\(16x^2 + 16x - 5\)", r"\(16x^2 - 16x - 5\)", r"\(16x^2 + 24x - 5\)", r"\(16x^2 - 5\)"],
     "A", "OSC", "medium",
     r"\((4x)^2 + (5 - 1)(4x) + (5)(-1) = 16x^2 + 4(4x) - 5 = 16x^2 + 16x - 5\)."),

    # 31
    (r"Assertion (A): \((a + b)^2 = a^2 + b^2 + 2ab\) holds true for all numbers \(a\) and \(b\).\nReason (R): Expanding \((a + b)(a + b) = a(a + b) + b(a + b) = a^2 + ab + ba + b^2 = a^2 + 2ab + b^2\).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"The distributive property of multiplication over addition proves the identity for all real numbers."),

    # 32
    (r"Assertion (A): \((x + 3)^2 = x^2 + 9\).\nReason (R): Squaring a binomial means squaring the first term and squaring the second term.",
     ["Both A and R are false", "Both A and R are true", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"This is the classic algebraic mistake. \((x + 3)^2 = x^2 + 6x + 9 \neq x^2 + 9\). The middle term \(2ab = 6x\) cannot be omitted."),

    # 33
    (r"Fill in the blank: \((2x + 3y)^2 = 4x^2 + \) ______ \( + 9y^2\).",
     [r"\(12xy\)", r"\(6xy\)", r"\(24xy\)", r"\(5xy\)"],
     "A", "OFB", "easy",
     r"The middle term is \(2ab = 2(2x)(3y) = 12xy\)."),

    # 34
    (r"Fill in the blank: \((3x - 2y)^2 = 9x^2 - \) ______ \( + 4y^2\).",
     [r"\(12xy\)", r"\(6xy\)", r"\(24xy\)", r"\(4xy\)"],
     "A", "OFB", "easy",
     r"The middle term is \(2ab = 2(3x)(2y) = 12xy\)."),

    # 35
    (r"If \(x + \frac{1}{x} = 5\), what is the value of \(x^2 + \frac{1}{x^2}\)?",
     ["23", "25", "27", "21"],
     "A", "OSC", "medium",
     r"Squaring both sides: \(\left(x + \frac{1}{x}\right)^2 = 5^2 \implies x^2 + 2(x)\left(\frac{1}{x}\right) + \frac{1}{x^2} = 25 \implies x^2 + 2 + \frac{1}{x^2} = 25 \implies x^2 + \frac{1}{x^2} = 25 - 2 = 23\)."),

    # 36
    (r"If \(x - \frac{1}{x} = 4\), find the value of \(x^2 + \frac{1}{x^2}\).",
     ["18", "16", "14", "20"],
     "A", "OSC", "medium",
     r"\(\left(x - \frac{1}{x}\right)^2 = 4^2 \implies x^2 - 2 + \frac{1}{x^2} = 16 \implies x^2 + \frac{1}{x^2} = 16 + 2 = 18\)."),

    # 37
    (r"If \(x + \frac{1}{x} = 3\), what is the value of \(x^4 + \frac{1}{x^4}\)?",
     ["47", "49", "51", "45"],
     "A", "OSC", "hard",
     r"First, \(x^2 + \frac{1}{x^2} = 3^2 - 2 = 7\). Squaring again: \(\left(x^2 + \frac{1}{x^2}\right)^2 = 7^2 \implies x^4 + 2 + \frac{1}{x^4} = 49 \implies x^4 + \frac{1}{x^4} = 49 - 2 = 47\)."),

    # 38
    (r"If \(a + b = 9\) and \(ab = 20\), find the value of \(a^2 + b^2\).",
     ["41", "81", "61", "51"],
     "A", "OSC", "easy",
     r"\(a^2 + b^2 = (a + b)^2 - 2ab = 9^2 - 2(20) = 81 - 40 = 41\)."),

    # 39
    (r"If \(a - b = 6\) and \(ab = 16\), find the value of \(a^2 + b^2\).",
     ["68", "36", "52", "60"],
     "A", "OSC", "easy",
     r"\(a^2 + b^2 = (a - b)^2 + 2ab = 6^2 + 2(16) = 36 + 32 = 68\)."),

    # 40
    (r"Numerical question: Find the value of \((3x + 4y)^2 - (3x - 4y)^2\) when \(x = 1\) and \(y = 1\).",
     ["48", "24", "96", "36"],
     "A", "ONE", "easy",
     r"\((A + B)^2 - (A - B)^2 = 4AB = 4(3x)(4y) = 48xy\). At \(x = 1, y = 1\): \(48(1)(1) = 48\).")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    (r"Expand: \((x + 2)^2\).",
     [r"\(x^2 + 4x + 4\)", r"\(x^2 + 4\)", r"\(x^2 + 2x + 4\)", r"\(x^2 + 4x + 2\)"],
     "A", "OSC", "easy",
     r"\(x^2 + 2(2)x + 2^2 = x^2 + 4x + 4\)."),

    # 42
    (r"Expand: \((x - 3)^2\).",
     [r"\(x^2 - 6x + 9\)", r"\(x^2 - 9\)", r"\(x^2 + 6x + 9\)", r"\(x^2 - 3x + 9\)"],
     "A", "OSC", "easy",
     r"\(x^2 - 2(3)x + 3^2 = x^2 - 6x + 9\)."),

    # 43
    (r"Expand: \((2x - 3y)^2\).",
     [r"\(4x^2 - 12xy + 9y^2\)", r"\(4x^2 - 6xy + 9y^2\)", r"\(4x^2 - 9y^2\)", r"\(4x^2 + 12xy + 9y^2\)"],
     "A", "OSC", "easy",
     r"\((2x)^2 - 2(2x)(3y) + (3y)^2 = 4x^2 - 12xy + 9y^2\)."),

    # 44
    (r"Expand: \((3a + 4b)^2\).",
     [r"\(9a^2 + 24ab + 16b^2\)", r"\(9a^2 + 12ab + 16b^2\)", r"\(9a^2 + 16b^2\)", r"\(9a^2 + 24ab + 8b^2\)"],
     "A", "OSC", "easy",
     r"\((3a)^2 + 2(3a)(4b) + (4b)^2 = 9a^2 + 24ab + 16b^2\)."),

    # 45
    (r"Expand: \((x - 5)(x + 5)\).",
     [r"\(x^2 - 25\)", r"\(x^2 + 25\)", r"\(x^2 - 10x - 25\)", r"\(x^2 - 5\)"],
     "A", "OSC", "easy",
     r"\(x^2 - 5^2 = x^2 - 25\)."),

    # 46
    (r"Expand: \((2a - 3b)(2a + 3b)\).",
     [r"\(4a^2 - 9b^2\)", r"\(4a^2 + 9b^2\)", r"\(4a^2 - 12ab - 9b^2\)", r"\(2a^2 - 3b^2\)"],
     "A", "OSC", "easy",
     r"\((2a)^2 - (3b)^2 = 4a^2 - 9b^2\)."),

    # 47
    (r"Expand: \((x + 1)(x + 2)\).",
     [r"\(x^2 + 3x + 2\)", r"\(x^2 + 2x + 1\)", r"\(x^2 + 3x + 3\)", r"\(x^2 + 2\)"],
     "A", "OSC", "easy",
     r"\(x^2 + (1 + 2)x + 1 \times 2 = x^2 + 3x + 2\)."),

    # 48
    (r"Expand: \((x - 4)(x + 2)\).",
     [r"\(x^2 - 2x - 8\)", r"\(x^2 + 2x - 8\)", r"\(x^2 - 6x - 8\)", r"\(x^2 - 8\)"],
     "A", "OSC", "easy",
     r"\(x^2 + (-4 + 2)x + (-4)(2) = x^2 - 2x - 8\)."),

    # 49
    (r"What is the missing term: \((a + b)^2 = a^2 + b^2 + \) ______.",
     [r"\(2ab\)", r"\(ab\)", r"\(4ab\)", r"\(0\)"],
     "A", "OSC", "easy",
     r"The cross term in \((a + b)^2\) is \(2ab\)."),

    # 50
    (r"What is the missing term: \((a - b)^2 = a^2 + b^2 - \) ______.",
     [r"\(2ab\)", r"\(ab\)", r"\(4ab\)", r"\(b^2\)"],
     "A", "OSC", "easy",
     r"The cross term in \((a - b)^2\) is \(2ab\)."),

    # 51
    (r"Simplify: \((x + y)^2 + (x - y)^2\).",
     [r"\(2(x^2 + y^2)\)", r"\(4xy\)", r"\(2x^2 + 4xy + 2y^2\)", "0"],
     "A", "OSC", "easy",
     r"\((x^2 + 2xy + y^2) + (x^2 - 2xy + y^2) = 2x^2 + 2y^2 = 2(x^2 + y^2)\)."),

    # 52
    (r"Simplify: \((x + y)^2 - (x - y)^2\).",
     [r"\(4xy\)", r"\(2(x^2 + y^2)\)", r"\(2xy\)", "0"],
     "A", "OSC", "easy",
     r"\((x^2 + 2xy + y^2) - (x^2 - 2xy + y^2) = 4xy\)."),

    # 53
    (r"Expand: \(\left(m + \frac{1}{m}\right)^2\).",
     [r"\(m^2 + 2 + \frac{1}{m^2}\)", r"\(m^2 + \frac{1}{m^2}\)", r"\(m^2 + 2m + \frac{1}{m^2}\)", r"\(m^2 + 1 + \frac{1}{m^2}\)"],
     "A", "OSC", "easy",
     r"\(m^2 + 2(m)\left(\frac{1}{m}\right) + \frac{1}{m^2} = m^2 + 2 + \frac{1}{m^2}\)."),

    # 54
    (r"Expand: \(\left(p - \frac{1}{p}\right)^2\).",
     [r"\(p^2 - 2 + \frac{1}{p^2}\)", r"\(p^2 - \frac{1}{p^2}\)", r"\(p^2 + 2 + \frac{1}{p^2}\)", r"\(p^2 - 2p + \frac{1}{p^2}\)"],
     "A", "OSC", "easy",
     r"\(p^2 - 2(p)\left(\frac{1}{p}\right) + \frac{1}{p^2} = p^2 - 2 + \frac{1}{p^2}\)."),

    # 55
    (r"Evaluate \((x + 3)(x - 3)\) when \(x = 7\).",
     ["40", "49", "58", "45"],
     "A", "OSC", "easy",
     r"\(x^2 - 9 = 7^2 - 9 = 49 - 9 = 40\)."),

    # 56
    (r"If \(a^2 + b^2 = 29\) and \(ab = 10\), find \((a + b)^2\).",
     ["49", "39", "59", "69"],
     "A", "OSC", "easy",
     r"\((a + b)^2 = a^2 + b^2 + 2ab = 29 + 2(10) = 49\)."),

    # 57
    (r"If \(a^2 + b^2 = 29\) and \(ab = 10\), find \((a - b)^2\).",
     ["9", "19", "4", "1"],
     "A", "OSC", "easy",
     r"\((a - b)^2 = a^2 + b^2 - 2ab = 29 - 2(10) = 9\)."),

    # 58
    (r"Fill in the blank: \((x + a)(x - b) = x^2 + (a - b)x - \) ______.",
     [r"\(ab\)", r"\(a + b\)", r"\(a^2\)", r"\(b^2\)"],
     "A", "OFB", "easy",
     r"The constant term is \(a \times (-b) = -ab\)."),

    # 59
    (r"Fill in the blank: \((5x - 4)(5x + 4) = 25x^2 - \) ______.",
     ["16", "8", "4", "20"],
     "A", "OFB", "easy",
     r"\(4^2 = 16\)."),

    # 60
    (r"An identity remains true when any variable is replaced by a number or by another algebraic expression.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"Because identities are universally quantified equalities, substitution of any valid expression preserves the equality."),

    # 61
    (r"\((a - b)^2 = (b - a)^2\) for all real numbers \(a\) and \(b\).",
     ["True", "False"],
     "A", "OTF", "easy",
     r"\((b - a)^2 = (-(a - b))^2 = (-1)^2(a - b)^2 = (a - b)^2\)."),

    # 62
    (r"The formula \(a^2 - b^2 = (a - b)(a + b)\) is only valid when \(a > b\).",
     ["False", "True"],
     "A", "OTF", "easy",
     r"The identity holds universally for all real numbers \(a\) and \(b\), including when \(a < b\) or \(a = b\)."),

    # 63
    (r"Expand: \((3x + 5y)(3x - 5y)\).",
     [r"\(9x^2 - 25y^2\)", r"\(9x^2 + 25y^2\)", r"\(9x^2 - 30xy - 25y^2\)", r"\(6x^2 - 10y^2\)"],
     "A", "OSC", "easy",
     r"\((3x)^2 - (5y)^2 = 9x^2 - 25y^2\)."),

    # 64
    (r"Expand: \((x^2 + y^2)^2\).",
     [r"\(x^4 + 2x^2y^2 + y^4\)", r"\(x^4 + y^4\)", r"\(x^4 + x^2y^2 + y^4\)", r"\(x^2 + 2x^2y^2 + y^2\)"],
     "A", "OSC", "easy",
     r"\((x^2)^2 + 2(x^2)(y^2) + (y^2)^2 = x^4 + 2x^2y^2 + y^4\)."),

    # 65
    (r"Expand: \((x^2 - y^2)^2\).",
     [r"\(x^4 - 2x^2y^2 + y^4\)", r"\(x^4 - y^4\)", r"\(x^4 + 2x^2y^2 + y^4\)", r"\(x^4 - x^2y^2 + y^4\)"],
     "A", "OSC", "easy",
     r"\(x^4 - 2x^2y^2 + y^4\)."),

    # 66
    (r"Assertion (A): \((x + 5)(x + 5) = x^2 + 10x + 25\).\nReason (R): This is an application of Identity I with \(a = x\) and \(b = 5\).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"\((x + 5)^2 = x^2 + 2(5)x + 25 = x^2 + 10x + 25\), which is Identity I."),

    # 67
    (r"Select ALL true algebraic identities:\n(A) \((x + y)^2 = x^2 + 2xy + y^2\)\n(B) \((x - y)^2 = x^2 - 2xy + y^2\)\n(C) \((x + y)(x - y) = x^2 - y^2\)",
     ["All A, B, and C", "A and B only", "B and C only", "A and C only"],
     "A", "OMC", "easy",
     r"All three are the standard classical algebraic identities."),

    # 68
    (r"If \(x^2 + \frac{1}{x^2} = 14\), find the positive value of \(x + \frac{1}{x}\).",
     ["4", "16", "3", "5"],
     "A", "OSC", "medium",
     r"\(\left(x + \frac{1}{x}\right)^2 = x^2 + \frac{1}{x^2} + 2 = 14 + 2 = 16 \implies x + \frac{1}{x} = \sqrt{16} = 4\)."),

    # 69
    (r"If \(x^2 + \frac{1}{x^2} = 18\), find the positive value of \(x - \frac{1}{x}\).",
     ["4", "16", "3", "5"],
     "A", "OSC", "medium",
     r"\(\left(x - \frac{1}{x}\right)^2 = x^2 + \frac{1}{x^2} - 2 = 18 - 2 = 16 \implies x - \frac{1}{x} = 4\)."),

    # 70
    (r"Numerical question: Find the value of \((a + b)^2\) if \(a^2 + b^2 = 58\) and \(ab = 21\).",
     ["100", "79", "121", "84"],
     "A", "ONE", "easy",
     r"\((a + b)^2 = a^2 + b^2 + 2ab = 58 + 2(21) = 58 + 42 = 100\).")
]

# 12 MOCK/FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Geometric Proof of (a + b)^2 -->
    <rect x="70" y="20" width="80" height="80" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="110" y="65" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">a²</text>
    <rect x="150" y="20" width="50" height="80" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="175" y="65" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">ab</text>
    <rect x="70" y="100" width="80" height="50" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="110" y="130" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">ab</text>
    <rect x="150" y="100" width="50" height="50" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="175" y="130" fill="#fbbf24" font-size="14" font-weight="bold" text-anchor="middle">b²</text>
    <text x="260" y="80" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">(a + b)²</text>
    <text x="260" y="100" fill="#38bdf8" font-size="11" text-anchor="middle">= a² + 2ab + b²</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">The area of a square of side \((a + b)\) is partitioned into four parts. What is the total sum of these areas?</p>
</div>""",
     [r"\(a^2 + 2ab + b^2\)", r"\(a^2 + b^2\)", r"\(a^2 + ab + b^2\)", r"\(2a^2 + 2b^2\)"],
     "A", "OSC", "easy",
     r"Summing the four sub-regions: \(a^2 + ab + ab + b^2 = a^2 + 2ab + b^2\)."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Geometric Proof of a^2 - b^2 -->
    <rect x="50" y="20" width="120" height="120" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect x="130" y="20" width="40" height="40" fill="#334155" stroke="#f43f5e" stroke-width="2"/>
    <text x="150" y="45" fill="#fb7185" font-size="12" font-weight="bold" text-anchor="middle">b²</text>
    <text x="90" y="85" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">a² - b²</text>
    <line x1="190" y1="80" x2="220" y2="80" stroke="#f59e0b" stroke-width="2" marker-end="url(#arr)"/>
    <rect x="230" y="40" width="90" height="80" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="275" y="85" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">(a + b)(a - b)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Cutting a square of area \(b^2\) from a square of area \(a^2\) produces a region equal to which product?</p>
</div>""",
     [r"\((a + b)(a - b)\)", r"\((a - b)^2\)", r"\((a + b)^2\)", r"\(2(a - b)\)"],
     "A", "OSC", "easy",
     r"Rearranging the remaining area \(a^2 - b^2\) yields a rectangle of dimensions \((a + b)\) by \((a - b)\)."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Expansion flow for (2y + 5)^2 -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#8b5cf6" stroke-width="2"/>
    <text x="170" y="45" fill="#c4b5fd" font-size="13" font-weight="bold" text-anchor="middle">(2y + 5)² = (2y)² + 2(2y)(5) + 5²</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">= 4y² + 20y + 25</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the expanded form of \((2y + 5)^2\)?</p>
</div>""",
     [r"\(4y^2 + 20y + 25\)", r"\(4y^2 + 10y + 25\)", r"\(4y^2 + 25\)", r"\(2y^2 + 20y + 25\)"],
     "A", "OSC", "easy",
     r"\((2y)^2 + 2(2y)(5) + 5^2 = 4y^2 + 20y + 25\)."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Difference of squares cancellation -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
    <text x="170" y="45" fill="#f472b6" font-size="13" font-weight="bold" text-anchor="middle">(6x - 7)(6x + 7)</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">= (6x)² - 7² = 36x² - 49</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the product of \((6x - 7)\) and \((6x + 7)\)?</p>
</div>""",
     [r"\(36x^2 - 49\)", r"\(36x^2 + 49\)", r"\(36x^2 - 84x - 49\)", r"\(12x^2 - 49\)"],
     "A", "OSC", "easy",
     r"\((6x)^2 - 7^2 = 36x^2 - 49\)."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Verification Box for (3x + 7)^2 - 84x -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="45" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">(3x + 7)² - 84x = (9x² + 42x + 49) - 84x</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">= 9x² - 42x + 49 = (3x - 7)²</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">The expression \((3x + 7)^2 - 84x\) simplifies to which binomial square?</p>
</div>""",
     [r"\((3x - 7)^2\)", r"\((3x + 7)^2\)", r"\(9x^2 + 49\)", r"\(9x^2 - 42x\)"],
     "A", "OSC", "easy",
     r"\(9x^2 + 42x + 49 - 84x = 9x^2 - 42x + 49 = (3x - 7)^2\)."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Symmetric Difference Identity -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="170" y="45" fill="#fbbf24" font-size="13" font-weight="bold" text-anchor="middle">(A + B)² - (A - B)²</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">= 4AB</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the simplified algebraic identity for \((A + B)^2 - (A - B)^2\)?</p>
</div>""",
     [r"\(4AB\)", r"\(2(A^2 + B^2)\)", r"\(2AB\)", "0"],
     "A", "OSC", "easy",
     r"\((A^2 + 2AB + B^2) - (A^2 - 2AB + B^2) = 4AB\)."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Sum of Squares from (x + 1/x) -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#0ea5e9" stroke-width="2"/>
    <text x="170" y="45" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Given: x + 1/x = 5</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">x² + 1/x² = 5² - 2 = 25 - 2 = 23</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">If \(x + \frac{1}{x} = 5\), what is the value of \(x^2 + \frac{1}{x^2}\)?</p>
</div>""",
     ["23", "25", "27", "21"],
     "A", "OSC", "easy",
     r"\(\left(x + \frac{1}{x}\right)^2 = x^2 + 2 + \frac{1}{x^2} = 25 \implies x^2 + \frac{1}{x^2} = 23\)."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Cyclical identity sum -->
    <rect x="25" y="20" width="290" height="40" rx="6" fill="#1e293b" stroke="#6366f1" stroke-width="2"/>
    <text x="170" y="45" fill="#c7d2fe" font-size="11" font-weight="bold" text-anchor="middle">(a - b)(a + b) + (b - c)(b + c) + (c - a)(c + a)</text>
    <rect x="25" y="75" width="290" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">= (a² - b²) + (b² - c²) + (c² - a²) = 0</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the sum of the three cyclical difference-of-squares terms?</p>
</div>""",
     ["0", r"\(2(a^2 + b^2 + c^2)\)", r"\(a^2 + b^2 + c^2\)", r"\(-1\)"],
     "A", "OSC", "easy",
     r"\((a^2 - b^2) + (b^2 - c^2) + (c^2 - a^2) = 0\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- (a + b)^2 + (a - b)^2 identity -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <text x="170" y="45" fill="#c084fc" font-size="13" font-weight="bold" text-anchor="middle">(A + B)² + (A - B)²</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">= 2(A² + B²)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the simplified identity for \((A + B)^2 + (A - B)^2\)?</p>
</div>""",
     [r"\(2(A^2 + B^2)\)", r"\(4AB\)", r"\(A^2 + B^2\)", r"\(2AB\)"],
     "A", "OSC", "easy",
     r"\((A^2 + 2AB + B^2) + (A^2 - 2AB + B^2) = 2A^2 + 2B^2 = 2(A^2 + B^2)\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Geometric Dissection of (a - b)^2 -->
    <rect x="60" y="20" width="100" height="100" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="110" y="75" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">(a - b)²</text>
    <text x="240" y="65" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">(a - b)²</text>
    <text x="240" y="85" fill="#34d399" font-size="12" text-anchor="middle">= a² - 2ab + b²</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the algebraic expression for \((a - b)^2\)?</p>
</div>""",
     [r"\(a^2 - 2ab + b^2\)", r"\(a^2 - b^2\)", r"\(a^2 + 2ab + b^2\)", r"\(a^2 - 2ab - b^2\)"],
     "A", "OSC", "easy",
     r"\((a - b)^2 = a^2 - 2ab + b^2\)."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="130" viewBox="0 0 340 130" xmlns="http://www.w3.org/2000/svg">
    <!-- Square of sum vs sum of squares -->
    <rect x="25" y="20" width="140" height="85" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <text x="95" y="45" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle">(x + 3)² = x² + 6x + 9</text>
    <text x="95" y="80" fill="#f87171" font-size="11" text-anchor="middle">≠ x² + 9</text>
    <rect x="175" y="20" width="140" height="85" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="245" y="45" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">Cross Term 2ab = 6x</text>
    <text x="245" y="80" fill="#34d399" font-size="11" text-anchor="middle">Must not be omitted!</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Why is \((x + 3)^2\) NOT equal to \(x^2 + 9\)?</p>
</div>""",
     ["The middle cross-term \(2ab = 6x\) must be included", "Because \(3^2\) is 6, not 9", "Because \(x\) cannot be squared", "Because \(3\) cannot be squared"],
     "A", "OSC", "easy",
     r"Expanding \((x + 3)^2\) gives \(x^2 + 2(3)x + 3^2 = x^2 + 6x + 9\). The middle cross-term \(6x\) cannot be omitted."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Value calculation box -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="170" y="45" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Given: a + b = 9,  ab = 20</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">a² + b² = (a + b)² - 2ab = 9² - 2(20) = 41</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the value of \(a^2 + b^2\) when \(a + b = 9\) and \(ab = 20\)?</p>
</div>""",
     ["41", "81", "61", "51"],
     "A", "OSC", "easy",
     r"\(a^2 + b^2 = (a + b)^2 - 2ab = 81 - 40 = 41\).")
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch6_topic4.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
