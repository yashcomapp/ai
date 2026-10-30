# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-6-6.3
Topic: Multiplication of Monomials, Binomials & Polynomials
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-6-6.3"

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
    (r"Find the product of \(4\) and \(7p\).",
     [r"\(28p\)", r"\(11p\)", r"\(28p^2\)", r"\(47p\)"],
     "A", "OSC", "easy",
     r"Multiplying coefficients: \(4 \times 7p = (4 \times 7)p = 28p\)."),

    # 2
    (r"Find the product of \(-4p\) and \(7p\).",
     [r"\(-28p^2\)", r"\(28p^2\)", r"\(-28p\)", r"\(-11p^2\)"],
     "A", "OSC", "easy",
     r"\((-4p) \times (7p) = (-4 \times 7)(p \times p) = -28p^2\)."),

    # 3
    (r"Find the product of \(-4p\) and \(7pq\).",
     [r"\(-28p^2q\)", r"\(28p^2q\)", r"\(-28pq^2\)", r"\(-28pq\)"],
     "A", "OSC", "easy",
     r"\((-4 \times 7) \times (p \times p) \times q = -28p^2q\)."),

    # 4
    (r"Find the product of \(4p^3\) and \(-3p\).",
     [r"\(-12p^4\)", r"\(12p^4\)", r"\(-12p^3\)", r"\(-7p^4\)"],
     "A", "OSC", "easy",
     r"\(4 \times (-3) \times p^3 \times p = -12p^{3+1} = -12p^4\)."),

    # 5
    (r"What is the volume of a rectangular box (cuboid) with length \(2ax\), breadth \(3by\), and height \(5cz\)?",
     [r"\(30abcxyz\)", r"\(10abcxyz\)", r"\(30(a+b+c)(x+y+z)\)", r"\(15abcxyz\)"],
     "A", "OSC", "easy",
     r"\(\text{Volume} = l \times b \times h = 2ax \times 3by \times 5cz = (2 \times 3 \times 5) \times (a \cdot b \cdot c \cdot x \cdot y \cdot z) = 30abcxyz\)."),

    # 6
    (r"Multiply: \(a \times (-a^2) \times a^3\).",
     [r"\(-a^6\)", r"\(a^6\)", r"\(-a^5\)", r"\(a^5\)"],
     "A", "OSC", "easy",
     r"Using laws of exponents: \(a^1 \times (-a^2) \times a^3 = -(a^{1 + 2 + 3}) = -a^6\)."),

    # 7
    (r"Multiply: \(2 \times 4y \times 8y^2 \times 16y^3\).",
     [r"\(1024y^6\)", r"\(512y^6\)", r"\(1024y^5\)", r"\(256y^6\)"],
     "A", "OSC", "medium",
     r"Coefficients: \(2 \times 4 \times 8 \times 16 = 1024\). Powers of \(y\): \(y^{1 + 2 + 3} = y^6\). Result \(= 1024y^6\)."),

    # 8
    (r"Multiply: \(m \times (-mn) \times mnp\).",
     [r"\(-m^3n^2p\)", r"\(m^3n^2p\)", r"\(-m^2n^2p\)", r"\(-m^3np\)"],
     "A", "OSC", "easy",
     r"\(-(m \times m \times m) \times (n \times n) \times p = -m^3n^2p\)."),

    # 9
    (r"Multiply the monomial by binomial: \(4p(q + r)\).",
     [r"\(4pq + 4pr\)", r"\(4pqr\)", r"\(4pq + r\)", r"\(p(4q + 4r)\)"],
     "A", "OSC", "easy",
     r"By the distributive property: \(4p \times q + 4p \times r = 4pq + 4pr\)."),

    # 10
    (r"Multiply: \(ab(a - b)\).",
     [r"\(a^2b - ab^2\)", r"\(a^2b - b\)", r"\(ab^2 - a^2b\)", r"\(a^2 - b^2\)"],
     "A", "OSC", "easy",
     r"\(ab \times a - ab \times b = a^2b - ab^2\)."),

    # 11
    (r"Multiply: \(7a^2b^2(a + b)\).",
     [r"\(7a^3b^2 + 7a^2b^3\)", r"\(7a^2b^2 + 7ab\)", r"\(14a^3b^3\)", r"\(7a^3b^3\)"],
     "A", "OSC", "easy",
     r"\(7a^2b^2 \times a + 7a^2b^2 \times b = 7a^3b^2 + 7a^2b^3\)."),

    # 12
    (r"Multiply: \((a^2 - 9)(4a)\).",
     [r"\(4a^3 - 36a\)", r"\(4a^3 - 9\)", r"\(4a^2 - 36a\)", r"\(4a^3 + 36a\)"],
     "A", "OSC", "easy",
     r"\(4a \times a^2 - 4a \times 9 = 4a^3 - 36a\)."),

    # 13
    (r"Multiply: \(p(6p^2 - 7p + 5)\).",
     [r"\(6p^3 - 7p^2 + 5p\)", r"\(6p^3 - 7p + 5\)", r"\(6p^2 - 7p + 5p\)", r"\(6p^3 + 7p^2 - 5p\)"],
     "A", "OSC", "easy",
     r"\(p \times 6p^2 - p \times 7p + p \times 5 = 6p^3 - 7p^2 + 5p\)."),

    # 14
    (r"Simplify: \(3x(4x - 5) + 3\) and find its value for \(x = 3\).",
     ["66", "63", "69", "72"],
     "A", "OSC", "medium",
     r"Expanding: \(12x^2 - 15x + 3\). For \(x = 3\): \(12(3^2) - 15(3) + 3 = 12(9) - 45 + 3 = 108 - 45 + 3 = 66\)."),

    # 15
    (r"Multiply the binomials: \((2x + 5)(4x - 3)\).",
     [r"\(8x^2 + 14x - 15\)", r"\(8x^2 - 14x - 15\)", r"\(8x^2 + 26x - 15\)", r"\(8x^2 - 15\)"],
     "A", "OSC", "medium",
     r"Expanding: \(2x(4x - 3) + 5(4x - 3) = 8x^2 - 6x + 20x - 15 = 8x^2 + 14x - 15\)."),

    # 16
    (r"Multiply: \((y - 8)(3y - 4)\).",
     [r"\(3y^2 - 28y + 32\)", r"\(3y^2 + 28y + 32\)", r"\(3y^2 - 24y - 32\)", r"\(3y^2 - 32\)"],
     "A", "OSC", "medium",
     r"\(y(3y - 4) - 8(3y - 4) = 3y^2 - 4y - 24y + 32 = 3y^2 - 28y + 32\)."),

    # 17
    (r"Multiply: \((2.5l - 0.5m)(2.5l + 0.5m)\).",
     [r"\(6.25l^2 - 0.25m^2\)", r"\(6.25l^2 + 0.25m^2\)", r"\(5l^2 - m^2\)", r"\(6.25l^2 - 2.5lm - 0.25m^2\)"],
     "A", "OSC", "medium",
     r"\((2.5l)^2 - (0.5m)^2 = 6.25l^2 - 0.25m^2\)."),

    # 18
    (r"Multiply: \((a + 3b)(x + 5)\).",
     [r"\(ax + 5a + 3bx + 15b\)", r"\(ax + 15b\)", r"\(ax + 3bx + 5a\)", r"\(ax + 5a + 3bx\)"],
     "A", "OSC", "easy",
     r"\(a(x + 5) + 3b(x + 5) = ax + 5a + 3bx + 15b\)."),

    # 19
    (r"Multiply: \((2pq + 3q^2)(3pq - 2q^2)\).",
     [r"\(6p^2q^2 + 5pq^3 - 6q^4\)", r"\(6p^2q^2 - 6q^4\)", r"\(6p^2q^2 - 5pq^3 - 6q^4\)", r"\(6pq - 6q^4\)"],
     "A", "OSC", "hard",
     r"\(2pq(3pq - 2q^2) + 3q^2(3pq - 2q^2) = 6p^2q^2 - 4pq^3 + 9pq^3 - 6q^4 = 6p^2q^2 + 5pq^3 - 6q^4\)."),

    # 20
    (r"Multiply: \(\left(\frac{3}{4}a^2 + 3b^2\right) \times 4\left(a^2 - \frac{2}{3}b^2\right)\).",
     [r"\(3a^4 + 10a^2b^2 - 8b^4\)", r"\(3a^4 - 10a^2b^2 - 8b^4\)", r"\(3a^4 - 8b^4\)", r"\(12a^4 + 10a^2b^2 - 8b^4\)"],
     "A", "OSC", "hard",
     r"First, \(4\left(a^2 - \frac{2}{3}b^2\right) = 4a^2 - \frac{8}{3}b^2\). Now: \(\left(\frac{3}{4}a^2 + 3b^2\right)\left(4a^2 - \frac{8}{3}b^2\right) = \frac{3}{4}a^2(4a^2) - \frac{3}{4}a^2\left(\frac{8}{3}b^2\right) + 3b^2(4a^2) - 3b^2\left(\frac{8}{3}b^2\right) = 3a^4 - 2a^2b^2 + 12a^2b^2 - 8b^4 = 3a^4 + 10a^2b^2 - 8b^4\)."),

    # 21
    (r"The product of two monomials is always a monomial.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"Multiplying two single-term expressions results in multiplying their numerical coefficients and combining their variable exponents into another single term."),

    # 22
    (r"The product of a monomial and a binomial always has 2 terms.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"Distributing a non-zero monomial over two unlike terms in a binomial yields two non-zero unlike terms (a binomial)."),

    # 23
    (r"In the expansion of \((x + a)(x + b)\), the middle coefficient is the sum \(a + b\).",
     ["True", "False"],
     "A", "OTF", "easy",
     r"\((x + a)(x + b) = x^2 + bx + ax + ab = x^2 + (a + b)x + ab\)."),

    # 24
    (r"What is the area of a rectangle with length \(3x^2y\) and breadth \(5xy^2\)?",
     [r"\(15x^3y^3\)", r"\(15x^2y^2\)", r"\(8x^3y^3\)", r"\(15xy\)"],
     "A", "OSC", "easy",
     r"\(\text{Area} = \text{length} \times \text{breadth} = 3x^2y \times 5xy^2 = 15x^{2+1}y^{1+2} = 15x^3y^3\)."),

    # 25
    (r"Simplify: \((x + y)(2x + y) + (x + 2y)(x - y)\).",
     [r"\(3x^2 + 4xy - y^2\)", r"\(3x^2 + 2xy - y^2\)", r"\(2x^2 + 4xy - y^2\)", r"\(3x^2 + 4xy + y^2\)"],
     "A", "OSC", "hard",
     r"First part: \(2x^2 + xy + 2xy + y^2 = 2x^2 + 3xy + y^2\). Second part: \(x^2 - xy + 2xy - 2y^2 = x^2 + xy - 2y^2\). Sum: \((2 + 1)x^2 + (3 + 1)xy + (1 - 2)y^2 = 3x^2 + 4xy - y^2\)."),

    # 26
    (r"Simplify: \((a + b + c)(a + b - c)\).",
     [r"\(a^2 + 2ab + b^2 - c^2\)", r"\(a^2 + b^2 - c^2\)", r"\(a^2 - b^2 - c^2\)", r"\(a^2 + 2ab - c^2\)"],
     "A", "OSC", "medium",
     r"Grouping \((a + b)\) as a single term: \(((a + b) + c)((a + b) - c) = (a + b)^2 - c^2 = a^2 + 2ab + b^2 - c^2\)."),

    # 27
    (r"Multiply: \((x + 7y)(7x - y)\).",
     [r"\(7x^2 + 48xy - 7y^2\)", r"\(7x^2 - 48xy - 7y^2\)", r"\(7x^2 + 50xy - 7y^2\)", r"\(7x^2 - 7y^2\)"],
     "A", "OSC", "medium",
     r"\(x(7x - y) + 7y(7x - y) = 7x^2 - xy + 49xy - 7y^2 = 7x^2 + 48xy - 7y^2\)."),

    # 28
    (r"Multiply: \((a^2 + 2b^2)(5a - 3b)\).",
     [r"\(5a^3 - 3a^2b + 10ab^2 - 6b^3\)", r"\(5a^3 + 10ab^2 - 6b^3\)", r"\(5a^3 - 3a^2b - 6b^3\)", r"\(5a^3 + 7ab^2 - 6b^3\)"],
     "A", "OSC", "medium",
     r"\(a^2(5a - 3b) + 2b^2(5a - 3b) = 5a^3 - 3a^2b + 10ab^2 - 6b^3\)."),

    # 29
    (r"Simplify: \(a(a^2 + a + 1) + 5\) and find its value for \(a = 0\).",
     ["5", "0", "1", "6"],
     "A", "OSC", "easy",
     r"Expanding: \(a^3 + a^2 + a + 5\). At \(a = 0\): \(0 + 0 + 0 + 5 = 5\)."),

    # 30
    (r"Simplify the same expression \(a(a^2 + a + 1) + 5\) for \(a = 1\).",
     ["8", "5", "7", "9"],
     "A", "OSC", "easy",
     r"\(1^3 + 1^2 + 1 + 5 = 1 + 1 + 1 + 5 = 8\)."),

    # 31
    (r"Assertion (A): The product of \(-3x\) and \(-5y\) is \(15xy\).\nReason (R): The product of two negative numbers is positive.",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"\((-3) \times (-5) = +15\), so \((-3x) \times (-5y) = 15xy\), which is explained by the rule that the product of two negatives is positive."),

    # 32
    (r"Assertion (A): \((x + 2)(x + 3) = x^2 + 5x + 6\).\nReason (R): Multiplying binomials follows \((x + a)(x + b) = x^2 + (a + b)x + ab\).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"Substituting \(a = 2\) and \(b = 3\) into \(x^2 + (a + b)x + ab\) gives \(x^2 + 5x + 6\)."),

    # 33
    (r"Fill in the blank: The product of \(2x\) and \(0\) is ______.",
     ["0", r"\(2x\)", "2", r"\(x\)"],
     "A", "OFB", "easy",
     r"Any algebraic quantity multiplied by zero equals zero."),

    # 34
    (r"Fill in the blank: \((x - 4)(x + 4) = x^2 - \) ______.",
     ["16", "8", "4", "0"],
     "A", "OFB", "easy",
     r"\((x - 4)(x + 4) = x^2 - 4^2 = x^2 - 16\)."),

    # 35
    (r"Multiply: \((1.5x - 4y)(1.5x + 4y + 3) - 4.5x + 12y\).",
     [r"\(2.25x^2 - 16y^2\)", r"\(2.25x^2 + 16y^2\)", r"\(2.25x^2 - 16y^2 - 9\)", "0"],
     "A", "OSC", "hard",
     r"Expanding: \(1.5x(1.5x + 4y + 3) - 4y(1.5x + 4y + 3) = 2.25x^2 + 6xy + 4.5x - 6xy - 16y^2 - 12y = 2.25x^2 - 16y^2 + 4.5x - 12y\). Now combining with \(- 4.5x + 12y\) yields \(2.25x^2 - 16y^2\)."),

    # 36
    (r"Find the product: \(2xy \times (x^2 - y^2)\).",
     [r"\(2x^3y - 2xy^3\)", r"\(2x^3y + 2xy^3\)", r"\(2x^2y - 2xy^2\)", r"\(x^3y - xy^3\)"],
     "A", "OSC", "easy",
     r"\(2xy \times x^2 - 2xy \times y^2 = 2x^3y - 2xy^3\)."),

    # 37
    (r"Find the product: \((3x^2 + 5x - 2)(x - 1)\).",
     [r"\(3x^3 + 2x^2 - 7x + 2\)", r"\(3x^3 - 2x^2 - 7x + 2\)", r"\(3x^3 + 8x^2 - 7x + 2\)", r"\(3x^3 + 2x^2 + 3x - 2\)"],
     "A", "OSC", "medium",
     r"\(x(3x^2 + 5x - 2) - 1(3x^2 + 5x - 2) = 3x^3 + 5x^2 - 2x - 3x^2 - 5x + 2 = 3x^3 + 2x^2 - 7x + 2\)."),

    # 38
    (r"What is the coefficient of \(x\) in the expansion of \((x - 3)(x + 5)\)?",
     ["2", "-2", "15", "-15"],
     "A", "OSC", "easy",
     r"\((x - 3)(x + 5) = x^2 + (-3 + 5)x - 15 = x^2 + 2x - 15\). The coefficient of \(x\) is 2."),

    # 39
    (r"What is the constant term in the expansion of \((2x - 3)(3x + 4)\)?",
     ["-12", "12", "-1", "6"],
     "A", "OSC", "easy",
     r"The constant term is the product of the numerical constants: \(-3 \times 4 = -12\)."),

    # 40
    (r"Numerical question: Find the value of \((x + 2)(x - 2)\) when \(x = 5\).",
     ["21", "25", "29", "20"],
     "A", "ONE", "easy",
     r"\((5 + 2)(5 - 2) = 7 \times 3 = 21\). (Equivalently \(5^2 - 4 = 25 - 4 = 21\)).")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    (r"Multiply: \(3x \times 5y\).",
     [r"\(15xy\)", r"\(8xy\)", r"\(15x^2y\)", r"\(15x\)"],
     "A", "OSC", "easy",
     r"\(3 \times 5 \times x \times y = 15xy\)."),

    # 42
    (r"Multiply: \(-2a \times 3b\).",
     [r"\(-6ab\)", r"\(6ab\)", r"\(-5ab\)", r"\(-6a^2b\)"],
     "A", "OSC", "easy",
     r"\(-2 \times 3 \times a \times b = -6ab\)."),

    # 43
    (r"Multiply: \(4x^2 \times 3x^3\).",
     [r"\(12x^5\)", r"\(12x^6\)", r"\(7x^5\)", r"\(12x\)"],
     "A", "OSC", "easy",
     r"\(4 \times 3 \times x^{2+3} = 12x^5\)."),

    # 44
    (r"Multiply: \(5x(x + 2)\).",
     [r"\(5x^2 + 10x\)", r"\(5x^2 + 2\)", r"\(5x^2 + 7x\)", r"\(10x^2\)"],
     "A", "OSC", "easy",
     r"\(5x \times x + 5x \times 2 = 5x^2 + 10x\)."),

    # 45
    (r"Multiply: \(-3y(2y - 5)\).",
     [r"\(-6y^2 + 15y\)", r"\(-6y^2 - 15y\)", r"\(6y^2 + 15y\)", r"\(-6y + 15\)"],
     "A", "OSC", "easy",
     r"\(-3y \times 2y - (-3y) \times 5 = -6y^2 + 15y\)."),

    # 46
    (r"Expand: \((x + 3)(x + 4)\).",
     [r"\(x^2 + 7x + 12\)", r"\(x^2 + 12x + 7\)", r"\(x^2 + 7x + 7\)", r"\(x^2 + 12\)"],
     "A", "OSC", "easy",
     r"\(x^2 + (3 + 4)x + (3 \times 4) = x^2 + 7x + 12\)."),

    # 47
    (r"Expand: \((x - 5)(x - 2)\).",
     [r"\(x^2 - 7x + 10\)", r"\(x^2 - 7x - 10\)", r"\(x^2 + 7x + 10\)", r"\(x^2 - 10\)"],
     "A", "OSC", "easy",
     r"\(x^2 + (-5 - 2)x + (-5 \times -2) = x^2 - 7x + 10\)."),

    # 48
    (r"Expand: \((2a + 3)(a - 1)\).",
     [r"\(2a^2 + a - 3\)", r"\(2a^2 - a - 3\)", r"\(2a^2 + 5a - 3\)", r"\(2a^2 - 3\)"],
     "A", "OSC", "easy",
     r"\(2a(a - 1) + 3(a - 1) = 2a^2 - 2a + 3a - 3 = 2a^2 + a - 3\)."),

    # 49
    (r"Find the area of a square of side \(3x\).",
     [r"\(9x^2\)", r"\(6x\)", r"\(12x\)", r"\(9x\)"],
     "A", "OSC", "easy",
     r"\(\text{Area} = (3x)^2 = 9x^2\)."),

    # 50
    (r"Find the volume of a cube of edge \(2a\).",
     [r"\(8a^3\)", r"\(6a^2\)", r"\(4a^3\)", r"\(8a\)"],
     "A", "OSC", "easy",
     r"\(\text{Volume} = (2a)^3 = 8a^3\)."),

    # 51
    (r"Multiply: \(x^2y \times xy^2\).",
     [r"\(x^3y^3\)", r"\(x^2y^2\)", r"\(x^3y^2\)", r"\(x^2y^3\)"],
     "A", "OSC", "easy",
     r"\(x^{2+1}y^{1+2} = x^3y^3\)."),

    # 52
    (r"Multiply: \(-a \times (-b) \times (-c)\).",
     [r"\(-abc\)", r"\(abc\)", r"\(-a - b - c\)", r"\(ab - c\)"],
     "A", "OSC", "easy",
     r"Three negative factors yield a negative product: \(-abc\)."),

    # 53
    (r"Multiply: \(2p(3p^2 - 4)\).",
     [r"\(6p^3 - 8p\)", r"\(6p^2 - 8p\)", r"\(6p^3 - 4\)", r"\(5p^3 - 8p\)"],
     "A", "OSC", "easy",
     r"\(2p \times 3p^2 - 2p \times 4 = 6p^3 - 8p\)."),

    # 54
    (r"Expand: \((3x - 1)(2x + 5)\).",
     [r"\(6x^2 + 13x - 5\)", r"\(6x^2 - 13x - 5\)", r"\(6x^2 + 17x - 5\)", r"\(6x^2 - 5\)"],
     "A", "OSC", "medium",
     r"\(3x(2x + 5) - 1(2x + 5) = 6x^2 + 15x - 2x - 5 = 6x^2 + 13x - 5\)."),

    # 55
    (r"Multiply: \((m + n)(2m - 3n)\).",
     [r"\(2m^2 - mn - 3n^2\)", r"\(2m^2 + mn - 3n^2\)", r"\(2m^2 - 5mn - 3n^2\)", r"\(2m^2 - 3n^2\)"],
     "A", "OSC", "easy",
     r"\(2m^2 - 3mn + 2mn - 3n^2 = 2m^2 - mn - 3n^2\)."),

    # 56
    (r"What is the product of \((x - 1)\) and \((x^2 + x + 1)\)?",
     [r"\(x^3 - 1\)", r"\(x^3 + 1\)", r"\(x^3 - 2x + 1\)", r"\(x^2 - 1\)"],
     "A", "OSC", "medium",
     r"\(x(x^2 + x + 1) - 1(x^2 + x + 1) = x^3 + x^2 + x - x^2 - x - 1 = x^3 - 1\)."),

    # 57
    (r"What is the product of \((x + 1)\) and \((x^2 - x + 1)\)?",
     [r"\(x^3 + 1\)", r"\(x^3 - 1\)", r"\(x^3 + 2x + 1\)", r"\(x^2 + 1\)"],
     "A", "OSC", "medium",
     r"\(x(x^2 - x + 1) + 1(x^2 - x + 1) = x^3 - x^2 + x + x^2 - x + 1 = x^3 + 1\)."),

    # 58
    (r"Fill in the blank: \(4a^2 \times 5a^3 = \) ______.",
     [r"\(20a^5\)", r"\(20a^6\)", r"\(9a^5\)", r"\(20a\)"],
     "A", "OFB", "easy",
     r"\(4 \times 5 \times a^{2+3} = 20a^5\)."),

    # 59
    (r"Fill in the blank: \(2x(3x + y) = 6x^2 + \) ______.",
     [r"\(2xy\)", r"\(xy\)", r"\(5xy\)", r"\(6xy\)"],
     "A", "OFB", "easy",
     r"\(2x \times y = 2xy\)."),

    # 60
    (r"The power rule \(x^a \times x^b = x^{a+b}\) applies when multiplying variable terms with the same base.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"This is the fundamental product rule of exponents."),

    # 61
    (r"Multiplying a binomial by a trinomial can produce at most 6 terms before combining like terms.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"A binomial has 2 terms and a trinomial has 3 terms; \(2 \times 3 = 6\) distinct products are initially formed."),

    # 62
    (r"The product \((x + 0)(y + 0)\) equals \(xy\).",
     ["True", "False"],
     "A", "OTF", "easy",
     r"\(x \times y = xy\)."),

    # 63
    (r"Expand: \((p + 8)(p - 3)\).",
     [r"\(p^2 + 5p - 24\)", r"\(p^2 - 5p - 24\)", r"\(p^2 + 11p - 24\)", r"\(p^2 - 24\)"],
     "A", "OSC", "easy",
     r"\(p^2 + (8 - 3)p - 24 = p^2 + 5p - 24\)."),

    # 64
    (r"Find the product of \(a^2, 2a^{22},\) and \(4a^{26}\).",
     [r"\(8a^{50}\)", r"\(8a^{48}\)", r"\(6a^{50}\)", r"\(8a^{52}\)"],
     "A", "OSC", "medium",
     r"Coefficients: \(1 \times 2 \times 4 = 8\). Exponents: \(a^{2 + 22 + 26} = a^{50}\). Result \(= 8a^{50}\)."),

    # 65
    (r"Find the product: \(\left(-\frac{10}{3}pq^3\right) \times \left(\frac{6}{5}p^3q\right)\).",
     [r"\(-4p^4q^4\)", r"\(4p^4q^4\)", r"\(-4p^3q^3\)", r"\(-\frac{60}{15}pq\)"],
     "A", "OSC", "medium",
     r"Coefficients: \(-\frac{10}{3} \times \frac{6}{5} = -4\). Variables: \(p \cdot p^3 = p^4\), and \(q^3 \cdot q = q^4\). Result \(= -4p^4q^4\)."),

    # 66
    (r"Assertion (A): The degree of the product \((x^2 + 1)(x^3 - 2)\) is 5.\nReason (R): When multiplying polynomials, the degree of the product is the sum of the degrees of the factors: \(2 + 3 = 5\).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"The highest power term is \(x^2 \times x^3 = x^5\), so the degree of the product is \(2 + 3 = 5\)."),

    # 67
    (r"Which of the following products equal \(12x^3y^2\)?\n(A) \(3x^2y \times 4xy\)\n(B) \(6xy \times 2x^2y\)\n(C) \(12x^3 \times y^2\)",
     ["All A, B, and C", "A and B only", "B and C only", "A and C only"],
     "A", "OMC", "easy",
     r"All three combinations multiply to \(12x^3y^2\)."),

    # 68
    (r"Evaluate \(x(x - 3) + 2\) for \(x = 1\).",
     ["0", "-1", "2", "1"],
     "A", "OSC", "easy",
     r"\(1(1 - 3) + 2 = 1(-2) + 2 = -2 + 2 = 0\)."),

    # 69
    (r"Evaluate \(3y(2y - 7) - 3(y - 4) - 63\) for \(y = -2\).",
     ["15", "-15", "21", "12"],
     "A", "OSC", "hard",
     r"For \(y = -2\): \(3(-2)(2(-2) - 7) - 3(-2 - 4) - 63 = -6(-11) - 3(-6) - 63 = 66 + 18 - 63 = 84 - 63 = 21\)."),

    # 70
    (r"Numerical question: Find the value of \((2x + 1)(x + 3)\) when \(x = 2\).",
     ["25", "20", "24", "26"],
     "A", "ONE", "easy",
     r"For \(x = 2\): \((2(2) + 1)(2 + 3) = (4 + 1)(5) = 5 \times 5 = 25\).")
]

# 12 MOCK/FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Area Grid Model for (x + 3)(x + 2) -->
    <rect x="50" y="30" width="100" height="70" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="100" y="70" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">x²</text>
    <rect x="150" y="30" width="80" height="70" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="190" y="70" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">3x</text>
    <rect x="50" y="100" width="100" height="40" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="100" y="125" fill="#fbbf24" font-size="14" font-weight="bold" text-anchor="middle">2x</text>
    <rect x="150" y="100" width="80" height="40" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
    <text x="190" y="125" fill="#f472b6" font-size="14" font-weight="bold" text-anchor="middle">6</text>
    <!-- Labels -->
    <text x="100" y="20" fill="#94a3b8" font-size="12" text-anchor="middle">x</text>
    <text x="190" y="20" fill="#94a3b8" font-size="12" text-anchor="middle">+3</text>
    <text x="35" y="70" fill="#94a3b8" font-size="12" text-anchor="middle">x</text>
    <text x="35" y="125" fill="#94a3b8" font-size="12" text-anchor="middle">+2</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Summing the four sub-areas in the grid gives the expansion of \((x + 3)(x + 2)\). What is the total area?</p>
</div>""",
     [r"\(x^2 + 5x + 6\)", r"\(x^2 + 6x + 5\)", r"\(x^2 + 5x + 5\)", r"\(x^2 + 6\)"],
     "A", "OSC", "easy",
     r"Total area \(= x^2 + 3x + 2x + 6 = x^2 + 5x + 6\)."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Volume of Cuboid Diagram -->
    <polygon points="60,90 180,90 220,50 100,50" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="60,130 180,130 180,90 60,90" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="180,130 220,90 220,50 180,90" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="120" y="145" fill="#38bdf8" font-size="11" text-anchor="middle">length = 2ax</text>
    <text x="215" y="115" fill="#10b981" font-size="11">breadth = 3by</text>
    <text x="45" y="110" fill="#f59e0b" font-size="11" text-anchor="end">height = 5cz</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the algebraic volume of this rectangular cuboid (\(l \times b \times h\))?</p>
</div>""",
     [r"\(30abcxyz\)", r"\(10abcxyz\)", r"\(30(a+b+c)(x+y+z)\)", r"\(15abcxyz\)"],
     "A", "OSC", "easy",
     r"\(\text{Volume} = 2ax \times 3by \times 5cz = 30abcxyz\)."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Distributive Law Arc Flow -->
    <rect x="30" y="30" width="280" height="40" rx="6" fill="#1e293b" stroke="#8b5cf6" stroke-width="2"/>
    <text x="170" y="55" fill="#c4b5fd" font-size="14" font-weight="bold" text-anchor="middle">4p · (q + r)</text>
    <!-- Curved arrows -->
    <path d="M 80 75 Q 120 115 160 75" fill="none" stroke="#f59e0b" stroke-width="2"/>
    <text x="170" y="110" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">= 4pq + 4pr</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">By distributing \(4p\) across \((q + r)\), what is the resulting expression?</p>
</div>""",
     [r"\(4pq + 4pr\)", r"\(4pqr\)", r"\(4pq + r\)", r"\(p(4q + 4r)\)"],
     "A", "OSC", "easy",
     r"\(4p(q + r) = 4pq + 4pr\)."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Exponent Add Rule -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="45" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">(-4p) * (7pq)</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">= (-4 * 7) * (p * p) * q = -28p²q</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the product of \((-4p)\) and \((7pq)\)?</p>
</div>""",
     [r"\(-28p^2q\)", r"\(28p^2q\)", r"\(-28pq^2\)", r"\(-28pq\)"],
     "A", "OSC", "easy",
     r"\((-4p) \times (7pq) = -28p^2q\)."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- FOIL Method Box -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
    <text x="170" y="45" fill="#f472b6" font-size="13" font-weight="bold" text-anchor="middle">(2x + 5)(4x - 3)</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">8x² - 6x + 20x - 15 = 8x² + 14x - 15</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Using FOIL expansion, what is the product of \((2x + 5)\) and \((4x - 3)\)?</p>
</div>""",
     [r"\(8x^2 + 14x - 15\)", r"\(8x^2 - 14x - 15\)", r"\(8x^2 + 26x - 15\)", r"\(8x^2 - 15\)"],
     "A", "OSC", "easy",
     r"\(2x(4x - 3) + 5(4x - 3) = 8x^2 - 6x + 20x - 15 = 8x^2 + 14x - 15\)."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Area of Rectangle -->
    <rect x="60" y="25" width="220" height="80" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="18" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Length: 3x²y</text>
    <text x="35" y="70" fill="#34d399" font-size="11" font-weight="bold">5xy²</text>
    <text x="170" y="70" fill="#fde047" font-size="13" font-weight="bold" text-anchor="middle">Area = 3x²y * 5xy² = 15x³y³</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the area of this rectangle?</p>
</div>""",
     [r"\(15x^3y^3\)", r"\(15x^2y^2\)", r"\(8x^3y^3\)", r"\(15xy\)"],
     "A", "OSC", "easy",
     r"\(\text{Area} = 3x^2y \times 5xy^2 = 15x^3y^3\)."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Difference of squares product -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#0ea5e9" stroke-width="2"/>
    <text x="170" y="45" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">(2.5l - 0.5m)(2.5l + 0.5m)</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">= (2.5l)² - (0.5m)² = 6.25l² - 0.25m²</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the product of \((2.5l - 0.5m)\) and \((2.5l + 0.5m)\)?</p>
</div>""",
     [r"\(6.25l^2 - 0.25m^2\)", r"\(6.25l^2 + 0.25m^2\)", r"\(5l^2 - m^2\)", r"\(6.25l^2 - 2.5lm - 0.25m^2\)"],
     "A", "OSC", "easy",
     r"\((2.5l)^2 - (0.5m)^2 = 6.25l^2 - 0.25m^2\)."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Powers addition with negative sign -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="170" y="45" fill="#fbbf24" font-size="13" font-weight="bold" text-anchor="middle">a * (-a²) * a³</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">= - (a¹⁺²⁺³) = -a⁶</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the simplified power resulting from \(a \times (-a^2) \times a^3\)?</p>
</div>""",
     [r"\(-a^6\)", r"\(a^6\)", r"\(-a^5\)", r"\(a^5\)"],
     "A", "OSC", "easy",
     r"\(a^1 \times (-a^2) \times a^3 = -a^{1+2+3} = -a^6\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Binomial square area grid -->
    <rect x="70" y="20" width="100" height="100" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="120" y="75" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">side = 3x</text>
    <text x="235" y="75" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Area = (3x)² = 9x²</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the area of a square whose side is \(3x\)?</p>
</div>""",
     [r"\(9x^2\)", r"\(6x\)", r"\(12x\)", r"\(9x\)"],
     "A", "OSC", "easy",
     r"\(\text{Area} = (3x)^2 = 9x^2\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Substitution evaluation box -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <text x="170" y="45" fill="#c084fc" font-size="12" font-weight="bold" text-anchor="middle">Evaluate: (x + 2)(x - 2)   at x = 5</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">= (5 + 2)(5 - 2) = 7 * 3 = 21</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the value of \((x + 2)(x - 2)\) when \(x = 5\)?</p>
</div>""",
     ["21", "25", "29", "20"],
     "A", "OSC", "easy",
     r"\((5 + 2)(5 - 2) = 7 \times 3 = 21\)."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="130" viewBox="0 0 340 130" xmlns="http://www.w3.org/2000/svg">
    <!-- Three Monomials Product -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="45" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">m * (-mn) * mnp</text>
    <rect x="30" y="75" width="280" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="100" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">= -(m * m * m) * (n * n) * p = -m³n²p</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the product of \(m\), \(-mn\), and \(mnp\)?</p>
</div>""",
     [r"\(-m^3n^2p\)", r"\(m^3n^2p\)", r"\(-m^2n^2p\)", r"\(-m^3np\)"],
     "A", "OSC", "easy",
     r"\(m \times (-mn) \times mnp = -m^3n^2p\)."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Volume of Cube -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#6366f1" stroke-width="2"/>
    <text x="170" y="45" fill="#c7d2fe" font-size="13" font-weight="bold" text-anchor="middle">Cube Edge = 2a</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Volume = (2a)³ = 2³ * a³ = 8a³</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the algebraic volume of a cube with edge \(2a\)?</p>
</div>""",
     [r"\(8a^3\)", r"\(6a^2\)", r"\(4a^3\)", r"\(8a\)"],
     "A", "OSC", "easy",
     r"\(\text{Volume} = (2a)^3 = 8a^3\).")
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch6_topic3.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
