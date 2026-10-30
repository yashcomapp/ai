# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-6-6.1
Topic: Terms, Factors, Coefficients & Classification of Polynomials
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-6-6.1"

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
    (r"What is the numerical coefficient of the term \(-7x^2y\)?",
     ["-7", "7", r"\(x^2y\)", "-1"],
     "A", "OSC", "easy",
     r"In the term \(-7x^2y\), the constant numerical factor multiplying the algebraic variables is \(-7\)."),

    # 2
    (r"How many terms are there in the algebraic expression \(4x^2 - 3xy + 5y^2 - 8\)?",
     ["4", "3", "5", "2"],
     "A", "OSC", "easy",
     r"The terms separated by addition/subtraction signs are \(4x^2\), \(-3xy\), \(5y^2\), and \(-8\), giving a total of 4 terms."),

    # 3
    (r"An algebraic expression containing exactly one term is called a:",
     ["Monomial", "Binomial", "Trinomial", "Linear equation"],
     "A", "OSC", "easy",
     r"An expression having only a single term (such as \(7xy\) or \(-5x^2\)) is defined as a monomial."),

    # 4
    (r"An algebraic expression containing exactly two unlike terms is called a:",
     ["Binomial", "Monomial", "Trinomial", "Constant"],
     "A", "OSC", "easy",
     r"An expression composed of exactly two terms (e.g. \(a + b\) or \(4l + 2m\)) is a binomial."),

    # 5
    (r"Which of the following expressions is a trinomial?",
     [r"\(x + y + z\)", r"\(2x + 3y\)", r"\(5xyz\)", r"\(a^2 + b^2 + c^2 + d^2\)"],
     "A", "OSC", "easy",
     r"\(x + y + z\) has exactly three distinct unlike terms, so it is a trinomial."),

    # 6
    (r"Which of the following pairs represents 'like terms'?",
     [r"\(7xy\) and \(-5yx\)", r"\(7x\) and \(7y\)", r"\(4x^2y\) and \(4xy^2\)", r"\(12a\) and \(12a^2\)"],
     "A", "OSC", "easy",
     r"Like terms have the exact same algebraic factors and powers. Since \(xy = yx\), \(7xy\) and \(-5yx\) are like terms."),

    # 7
    (r"Which of the following pairs consists of 'unlike terms'?",
     [r"\(2x^2y\) and \(2xy^2\)", r"\(-29x\) and \(\frac{5}{2}x\)", r"\(14xy\) and \(42yx\)", r"\(100\) and \(-5\)"],
     "A", "OSC", "easy",
     r"In \(2x^2y\), \(x\) has power 2 and \(y\) has power 1, whereas in \(2xy^2\), \(x\) has power 1 and \(y\) has power 2. Different powers make them unlike terms."),

    # 8
    (r"What are the factors of the algebraic term \(12a^2b\)?",
     [r"\(12, a, a, b\)", r"\(12, a, b\)", r"\(12a, b\)", r"\(6, a, b\)"],
     "A", "OSC", "easy",
     r"The irreducible product factors constituting \(12a^2b\) are \(12 \times a \times a \times b\) (or the prime factors \(2, 2, 3, a, a, b\))."),

    # 9
    (r"What is the coefficient of \(y\) in the expression \(4x - 3y + 5\)?",
     ["-3", "3", "4", "5"],
     "A", "OSC", "easy",
     r"The term containing \(y\) is \(-3y\), whose numerical coefficient is \(-3\)."),

    # 10
    (r"What is the degree of the polynomial \(5x^4 - 3x^2 + 7x - 9\)?",
     ["4", "2", "1", "0"],
     "A", "OSC", "easy",
     r"The degree of a polynomial in one variable is the highest exponent of the variable, which is 4."),

    # 11
    (r"In the expression \(1 + x + x^2\), what is the coefficient of \(x^2\)?",
     ["1", "0", "2", "-1"],
     "A", "OSC", "easy",
     r"\(x^2 = 1 \cdot x^2\), so its numerical coefficient is 1."),

    # 12
    (r"Which of the following is NOT a polynomial?",
     [r"\(x + \frac{1}{x}\)", r"\(x^2 + 2x + 1\)", r"\(5x^3 - 4\)", r"\(3\)"],
     "A", "OSC", "medium",
     r"In a polynomial, the exponent of any variable must be a non-negative integer (whole number). In \(x + \frac{1}{x} = x + x^{-1}\), the exponent \(-1\) is negative, so it is not a polynomial."),

    # 13
    (r"What is the coefficient of \(x^2\) in \(\frac{\pi}{2}x^2 + x\)?",
     [r"\(\frac{\pi}{2}\)", r"\(\pi\)", "1", "2"],
     "A", "OSC", "easy",
     r"The constant multiplying \(x^2\) is \(\frac{\pi}{2}\)."),

    # 14
    (r"What type of polynomial is \(4p^2q - 4pq^2 + 5pq\)?",
     ["Trinomial", "Binomial", "Monomial", "Linear polynomial"],
     "A", "OSC", "easy",
     r"It consists of three non-zero unlike terms, so it is classified as a trinomial."),

    # 15
    (r"What is the degree of a non-zero constant polynomial like \(7\)?",
     ["0", "1", "Undefined", "7"],
     "A", "OSC", "easy",
     r"Any non-zero constant \(c\) can be expressed as \(c \cdot x^0\), meaning its degree is 0."),

    # 16
    (r"Identify the coefficient of \(x\) in the term \(-\frac{x}{3}\).",
     [r"\(-\frac{1}{3}\)", r"\(\frac{1}{3}\)", "-3", "3"],
     "A", "OSC", "easy",
     r"\(-\frac{x}{3} = -\frac{1}{3} \cdot x\), so the coefficient is \(-\frac{1}{3}\)."),

    # 17
    (r"Which of the following is a monomial?",
     [r"\(7\)", r"\(2x + 1\)", r"\(x^2 - y^2\)", r"\(a + b + c\)"],
     "A", "OSC", "easy",
     r"A single constant number like 7 consists of only one term, so it is a monomial."),

    # 18
    (r"In the expression \(3x^2y - 5xy^2 + 7xy - 2\), what is the constant term?",
     ["-2", "2", "7", "3"],
     "A", "OSC", "easy",
     r"The constant term is the term that contains no variables, which is \(-2\)."),

    # 19
    (r"Can the expression \(2x + 3x\) be classified as a binomial?",
     ["No, because like terms combine to form the single term 5x (monomial)", "Yes, because it is written with two parts", "Yes, because it has variable x twice", "No, it is a trinomial"],
     "A", "OSC", "medium",
     r"Since \(2x\) and \(3x\) are like terms, they simplify to \(5x\), which is a monomial."),

    # 20
    (r"What is the degree of the term \(3x^2y^3\)?",
     ["5", "2", "3", "6"],
     "A", "OSC", "medium",
     r"The degree of a monomial in multiple variables is the sum of the exponents of its variables: \(2 + 3 = 5\)."),

    # 21
    (r"The terms of an algebraic expression are added to form the expression.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"An algebraic expression is built by taking terms and combining them via addition or subtraction."),

    # 22
    (r"A binomial can have degree 100.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"Yes; for instance \(x^{100} - 1\) is a binomial of degree 100."),

    # 23
    (r"Like terms must have identical numerical coefficients.",
     ["False", "True"],
     "A", "OTF", "easy",
     r"Like terms must have identical algebraic (variable) parts, but their numerical coefficients can be completely different (e.g. \(3x\) and \(-8x\))."),

    # 24
    (r"The expression \(\sqrt{x} + 3\) is a polynomial.",
     ["False", "True"],
     "A", "OTF", "easy",
     r"\(\sqrt{x} = x^{1/2}\) has a fractional exponent \(\frac{1}{2}\), which violates the requirement that exponents of variables in polynomials must be non-negative integers."),

    # 25
    (r"Group the like terms together from: \(12x, 12, -25x, -25, -25y, 1, x\). Which group consists of like terms in \(x\)?",
     [r"\(12x, -25x, x\)", r"\(12, -25, 1\)", r"\(-25x, -25y\)", r"\(12x, x, -25y\)"],
     "A", "OSC", "easy",
     r"\(12x\), \(-25x\), and \(x\) all share the exact same variable factor \(x\) with power 1."),

    # 26
    (r"What are the terms in the expression \(0.1p^2 + 0.2q^2\)?",
     [r"\(0.1p^2\) and \(0.2q^2\)", r"\(p^2\) and \(q^2\)", r"\(0.1\) and \(0.2\)", r"\(0.3p^2q^2\)"],
     "A", "OSC", "easy",
     r"The two individual additive components are \(0.1p^2\) and \(0.2q^2\)."),

    # 27
    (r"What is the coefficient of \(x\) in the term \(-px\)?",
     ["-p", "p", "-1", "x"],
     "A", "OSC", "easy",
     r"Factoring out \(x\), the remaining multiplier is \(-p\)."),

    # 28
    (r"What is the degree of the polynomial \(7x^3 - 5x^5 + 2x - 1\)?",
     ["5", "3", "1", "7"],
     "A", "OSC", "easy",
     r"The highest power of the variable \(x\) is 5 (in the term \(-5x^5\)), so the degree is 5."),

    # 29
    (r"Which of the following is a binomial of degree 1?",
     [r"\(2x + 5\)", r"\(x^2 + 5\)", r"\(3x\)", r"\(x^3 - x\)"],
     "A", "OSC", "easy",
     r"\(2x + 5\) has two terms (binomial) and the highest exponent of \(x\) is 1 (degree 1)."),

    # 30
    (r"What is the coefficient of \(y^2\) in the expression \(5 - 3y^2 + 2y\)?",
     ["-3", "3", "5", "2"],
     "A", "OSC", "easy",
     r"The term involving \(y^2\) is \(-3y^2\), so its coefficient is \(-3\)."),

    # 31
    (r"Assertion (A): The expression \(3x^2y\) and \(-5yx^2\) are like terms.\nReason (R): Multiplication of real numbers and variables is commutative, so \(x^2y = yx^2\).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"Because the order of multiplication does not change the product (\(x^2y = yx^2\)), the variable factors are identical, confirming they are like terms."),

    # 32
    (r"Assertion (A): The expression \(\frac{2}{x} + 5\) is not a polynomial.\nReason (R): In a polynomial, the exponents of all variables must be whole numbers (non-negative integers).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"\(\frac{2}{x} = 2x^{-1}\) has exponent \(-1\), which is not a non-negative integer, disqualifying it from being a polynomial."),

    # 33
    (r"Fill in the blank: An algebraic expression having three unlike terms is called a ______.",
     ["Trinomial", "Binomial", "Monomial", "Polynomial of degree 3"],
     "A", "OFB", "easy",
     r"An expression with three unlike terms is a trinomial."),

    # 34
    (r"Fill in the blank: In the term \(-xy\), the numerical coefficient is ______.",
     ["-1", "1", "0", "-xy"],
     "A", "OFB", "easy",
     r"\(-xy = (-1) \cdot xy\), so the numerical coefficient is \(-1\)."),

    # 35
    (r"Which of the following polynomials is a monomial of degree 2?",
     [r"\(5x^2\)", r"\(x^2 + 1\)", r"\(2x\)", r"\(x^2 - x\)"],
     "A", "OSC", "easy",
     r"\(5x^2\) is a single term (monomial) with power 2 (degree 2)."),

    # 36
    (r"What is the degree of the polynomial \(0\)?",
     ["Not defined", "0", "1", "-1"],
     "A", "OSC", "medium",
     r"By convention in algebra, the zero polynomial has no non-zero terms, so its degree is not defined."),

    # 37
    (r"State the number of terms in \(a^2 - 2ab + b^2\).",
     ["3", "2", "1", "4"],
     "A", "OSC", "easy",
     r"The three terms are \(a^2\), \(-2ab\), and \(b^2\)."),

    # 38
    (r"What is the coefficient of \(x^0\) in the polynomial \(3x^2 - 5x + 8\)?",
     ["8", "-5", "3", "0"],
     "A", "OSC", "easy",
     r"Since \(x^0 = 1\), the term with \(x^0\) is the constant term \(8\)."),

    # 39
    (r"Which of the following expressions is a linear monomial?",
     [r"\(4x\)", r"\(4x + 1\)", r"\(4x^2\)", r"\(4\)"],
     "A", "OSC", "easy",
     r"\(4x\) is a single term (monomial) with power 1 (linear)."),

    # 40
    (r"Numerical question: What is the sum of the coefficients in the expression \(3x^2 - 5x + 7\)?",
     ["5", "15", "10", "4"],
     "A", "ONE", "easy",
     r"Sum of coefficients \(= 3 + (-5) + 7 = 5\). (Equivalently, evaluating at \(x = 1\) gives \(3(1)^2 - 5(1) + 7 = 5\)).")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    (r"Identify the numerical coefficient in the term \(\frac{2}{3}xy\).",
     [r"\(\frac{2}{3}\)", "2", "3", r"\(xy\)"],
     "A", "OSC", "easy",
     r"The constant multiplier is \(\frac{2}{3}\)."),

    # 42
    (r"What are the terms in the expression \(4x - 5y\)?",
     [r"\(4x\) and \(-5y\)", r"\(4x\) and \(5y\)", r"\(4\) and \(-5\)", r"\(x\) and \(y\)"],
     "A", "OSC", "easy",
     r"The terms are \(4x\) and \(-5y\)."),

    # 43
    (r"Classify the expression \(7mn\) as a monomial, binomial, or trinomial.",
     ["Monomial", "Binomial", "Trinomial", "None of these"],
     "A", "OSC", "easy",
     r"\(7mn\) consists of a single term, making it a monomial."),

    # 44
    (r"Classify the expression \(a^2 + b^2\) as a monomial, binomial, or trinomial.",
     ["Binomial", "Monomial", "Trinomial", "Constant"],
     "A", "OSC", "easy",
     r"It has two unlike terms, so it is a binomial."),

    # 45
    (r"Which of the following is like to \(14xy\)?",
     [r"\(-2yx\)", r"\(14x\)", r"\(14y\)", r"\(14x^2y\)"],
     "A", "OSC", "easy",
     r"\(-2yx = -2xy\), which has identical variable factors."),

    # 46
    (r"Which of the following is like to \(-4a^2b\)?",
     [r"\(7ba^2\)", r"\(4ab^2\)", r"\(-4a\)", r"\(7ab\)"],
     "A", "OSC", "easy",
     r"\(ba^2 = a^2b\), having the same variables and powers."),

    # 47
    (r"What is the degree of the polynomial \(x^5 - x^4 + 3\)?",
     ["5", "4", "3", "1"],
     "A", "OSC", "easy",
     r"The highest exponent of \(x\) is 5."),

    # 48
    (r"What is the degree of the polynomial \(2 - y^2 - y^3 + 2y^8\)?",
     ["8", "3", "2", "0"],
     "A", "OSC", "easy",
     r"The highest power is 8 (in \(2y^8\))."),

    # 49
    (r"What is the coefficient of \(x\) in the expression \(z - x + y\)?",
     ["-1", "1", "0", "-x"],
     "A", "OSC", "easy",
     r"The term is \(-x = (-1) \cdot x\), so the coefficient is \(-1\)."),

    # 50
    (r"Identify the constant term in \(2x^2 - 3x + \frac{5}{2}\).",
     [r"\(\frac{5}{2}\)", "2", "-3", "5"],
     "A", "OSC", "easy",
     r"The term independent of \(x\) is \(\frac{5}{2}\)."),

    # 51
    (r"Can two unlike terms be added together into a single term without addition symbols?",
     ["No, they can only be written connected with '+' or '-'", "Yes, their coefficients multiply", "Yes, their variables combine", "Always"],
     "A", "OSC", "easy",
     r"Unlike terms cannot be combined into a single term; their sum can only be indicated as an expression like \(2x + 3y\)."),

    # 52
    (r"How many terms does the expression \(5x^2y \times 2xy\) have?",
     ["1", "2", "3", "4"],
     "A", "OSC", "easy",
     r"Multiplication yields \(10x^3y^2\), which is a single term (monomial)."),

    # 53
    (r"What is the degree of the polynomial \(4\)?",
     ["0", "1", "4", "Undefined"],
     "A", "OSC", "easy",
     r"A non-zero constant has degree 0 since \(4 = 4x^0\)."),

    # 54
    (r"Which of the following is a polynomial in one variable?",
     [r"\(x^2 - 2x + 7\)", r"\(x + y + z\)", r"\(x + \frac{1}{x}\)", r"\(2\sqrt{t} + t\sqrt{2}\)"],
     "A", "OSC", "easy",
     r"\(x^2 - 2x + 7\) has only the single variable \(x\) with whole-number exponents."),

    # 55
    (r"What is the coefficient of \(x^3\) in \(2 - x^3 + x^2\)?",
     ["-1", "1", "2", "0"],
     "A", "OSC", "easy",
     r"\(-x^3 = (-1)x^3\), so its coefficient is \(-1\)."),

    # 56
    (r"Is \(y + \frac{2}{y}\) a polynomial?",
     ["No, because 2/y has exponent -1", "Yes, it is a binomial", "Yes, degree is 1", "Yes, degree is 2"],
     "A", "OSC", "easy",
     r"\(2/y = 2y^{-1}\); the exponent is not a whole number, so it is not a polynomial."),

    # 57
    (r"Classify \(1 + x\) as a monomial, binomial, or trinomial.",
     ["Binomial", "Monomial", "Trinomial", "None"],
     "A", "OSC", "easy",
     r"It consists of two terms: 1 and \(x\)."),

    # 58
    (r"Fill in the blank: A polynomial of degree 1 is called a ______ polynomial.",
     ["Linear", "Quadratic", "Cubic", "Constant"],
     "A", "OFB", "easy",
     r"A degree 1 polynomial like \(ax + b\) is termed a linear polynomial."),

    # 59
    (r"Fill in the blank: A polynomial of degree 2 is called a ______ polynomial.",
     ["Quadratic", "Linear", "Cubic", "Biquadratic"],
     "A", "OFB", "easy",
     r"A degree 2 polynomial like \(ax^2 + bx + c\) is quadratic."),

    # 60
    (r"The coefficient of \(x\) in \(5\) is 0.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"In the expression 5, \(x\) does not appear, so its coefficient is 0 (\(0 \cdot x\))."),

    # 61
    (r"The factors of \(5xy\) are \(5, x,\) and \(y\).",
     ["True", "False"],
     "A", "OTF", "easy",
     r"\(5xy\) is the product of \(5\), \(x\), and \(y\)."),

    # 62
    (r"An expression of the form \(ax^2 + bx + c\) with \(a \neq 0\) is always a trinomial.",
     ["False", "True"],
     "A", "OTF", "medium",
     r"If \(b = 0\) or \(c = 0\), it has fewer than 3 terms (e.g. \(ax^2\) has 1 term). It is only a trinomial if all three coefficients \(a, b, c\) are non-zero."),

    # 63
    (r"Find the value of the polynomial \(5x - 4x^2 + 3\) at \(x = 0\).",
     ["3", "0", "5", "4"],
     "A", "OSC", "easy",
     r"Substituting \(x = 0\): \(5(0) - 4(0)^2 + 3 = 3\)."),

    # 64
    (r"Find the value of the polynomial \(5x - 4x^2 + 3\) at \(x = 1\).",
     ["4", "3", "5", "2"],
     "A", "OSC", "easy",
     r"Substituting \(x = 1\): \(5(1) - 4(1)^2 + 3 = 5 - 4 + 3 = 4\)."),

    # 65
    (r"Which of the following is an algebraic factor of the term \(-8p^2q\)?",
     [r"\(p^2q\)", r"\(-8\)", r"\(8\)", r"\(-1\)"],
     "A", "OSC", "easy",
     r"The algebraic (variable) part of the term is \(p^2q\)."),

    # 66
    (r"Assertion (A): The expression \(7x^2 - 3x + 2\) is a quadratic trinomial.\nReason (R): It has three unlike terms (trinomial) and its highest power of variable is 2 (quadratic).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"Three terms make it a trinomial, and maximum degree 2 makes it quadratic, directly explaining both properties."),

    # 67
    (r"Select ALL like terms from the list:\n(A) \(3x^2y\)\n(B) \(-7yx^2\)\n(C) \(4xy^2\)\n(D) \(\frac{1}{2}x^2y\)",
     ["A, B, and D only", "A and B only", "A, B, and C only", "All A, B, C, and D"],
     "A", "OMC", "medium",
     r"\(3x^2y\), \(-7yx^2\), and \(\frac{1}{2}x^2y\) all have variable part \(x^2y\). (C) has \(xy^2\), which is unlike."),

    # 68
    (r"In the term \(-15a^2bc\), what is the coefficient of \(a^2bc\)?",
     ["-15", "15", "-1", "a^2bc"],
     "A", "OSC", "easy",
     r"The numerical multiplier of \(a^2bc\) is \(-15\)."),

    # 69
    (r"What is the degree of the polynomial \(p(x) = x^3 - 3x^2 + 2x - 5\)?",
     ["3", "2", "1", "0"],
     "A", "OSC", "easy",
     r"The highest exponent is 3."),

    # 70
    (r"Numerical question: How many terms are in the simplified form of \((2x + 3y) + (4x - 3y)\)?",
     ["1", "2", "3", "0"],
     "A", "ONE", "easy",
     r"\((2x + 4x) + (3y - 3y) = 6x + 0 = 6x\), which is a single term (1 term).")
]

# 12 MOCK/FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Factor Tree of an Algebraic Term -->
    <rect x="130" y="15" width="80" height="35" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="38" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">4x²y</text>
    <!-- Branch lines -->
    <line x1="145" y1="50" x2="60" y2="90" stroke="#64748b" stroke-width="2"/>
    <line x1="160" y1="50" x2="130" y2="90" stroke="#64748b" stroke-width="2"/>
    <line x1="180" y1="50" x2="210" y2="90" stroke="#64748b" stroke-width="2"/>
    <line x1="195" y1="50" x2="280" y2="90" stroke="#64748b" stroke-width="2"/>
    <!-- Factor nodes -->
    <circle cx="60" cy="105" r="16" fill="#334155" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="60" y="110" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">4</text>
    <circle cx="130" cy="105" r="16" fill="#334155" stroke="#10b981" stroke-width="1.5"/>
    <text x="130" y="110" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">x</text>
    <circle cx="210" cy="105" r="16" fill="#334155" stroke="#10b981" stroke-width="1.5"/>
    <text x="210" y="110" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">x</text>
    <circle cx="280" cy="105" r="16" fill="#334155" stroke="#10b981" stroke-width="1.5"/>
    <text x="280" y="110" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">y</text>
    <text x="170" y="142" fill="#e2e8f0" font-size="11" text-anchor="middle">Factors: 4, x, x, y</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What are the individual irreducible factors of the term \(4x^2y\) shown in the factor tree?</p>
</div>""",
     [r"\(4, x, x, y\)", r"\(4, x, y\)", r"\(4x, y\)", r"\(2, x, y\)"],
     "A", "OSC", "easy",
     r"The factor tree resolves \(4x^2y\) into its constituent factors: \(4 \times x \times x \times y\) (or prime factors \(2, 2, x, x, y\))."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Like Terms vs Unlike Terms Box -->
    <rect x="20" y="20" width="140" height="95" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="90" y="45" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Like Terms</text>
    <text x="90" y="70" fill="#f8fafc" font-size="11" text-anchor="middle">7xy and -5yx</text>
    <text x="90" y="95" fill="#94a3b8" font-size="10" text-anchor="middle">Same variables &amp; powers</text>
    <rect x="180" y="20" width="140" height="95" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <text x="250" y="45" fill="#fb7185" font-size="12" font-weight="bold" text-anchor="middle">Unlike Terms</text>
    <text x="250" y="70" fill="#f8fafc" font-size="11" text-anchor="middle">7x²y and 7xy²</text>
    <text x="250" y="95" fill="#94a3b8" font-size="10" text-anchor="middle">Different exponents</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Why are \(7x^2y\) and \(7xy^2\) classified as unlike terms?</p>
</div>""",
     ["The exponents of the variables are different", "The numerical coefficients are equal", "They have different signs", "They cannot be multiplied"],
     "A", "OSC", "easy",
     r"In \(7x^2y\), \(x\) is squared, while in \(7xy^2\), \(y\) is squared. Because the exponents assigned to variables differ, they are unlike terms."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Polynomial Classification Flow -->
    <rect x="20" y="25" width="90" height="70" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="50" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Monomial</text>
    <text x="65" y="75" fill="#f8fafc" font-size="11" text-anchor="middle">1 Term</text>
    <rect x="125" y="25" width="90" height="70" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="50" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">Binomial</text>
    <text x="170" y="75" fill="#f8fafc" font-size="11" text-anchor="middle">2 Terms</text>
    <rect x="230" y="25" width="90" height="70" rx="4" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="275" y="50" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Trinomial</text>
    <text x="275" y="75" fill="#f8fafc" font-size="11" text-anchor="middle">3 Terms</text>
    <text x="170" y="125" fill="#e2e8f0" font-size="11" text-anchor="middle">Example: 3x² - 5x + 7 is a Trinomial</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">How is the expression \(3x^2 - 5x + 7\) classified based on its number of terms?</p>
</div>""",
     ["Trinomial", "Binomial", "Monomial", "Constant"],
     "A", "OSC", "easy",
     r"An expression with three unlike terms is classified as a trinomial."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Non-negative integer exponent condition -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="45" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Valid: 5x³ - 2x² + 7 (Powers: 3, 2, 0)</text>
    <rect x="30" y="75" width="280" height="40" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <text x="170" y="100" fill="#fb7185" font-size="13" font-weight="bold" text-anchor="middle">Not a Polynomial: x + 1/x = x + x⁻¹</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Why is \(x + \frac{1}{x}\) NOT an algebraic polynomial?</p>
</div>""",
     ["The exponent of \(x\) in \(\frac{1}{x}\) is \(-1\), which is not a whole number", "It contains the fraction \(\frac{1}{x}\)", "It has two terms", "The variable \(x\) cannot be in a denominator for any function"],
     "A", "OSC", "easy",
     r"In a polynomial, all exponents of variables must be non-negative integers. Since \(\frac{1}{x} = x^{-1}\), the negative exponent disqualifies it."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Degree definition box -->
    <rect x="30" y="20" width="280" height="45" rx="6" fill="#1e293b" stroke="#8b5cf6" stroke-width="2"/>
    <text x="170" y="48" fill="#c4b5fd" font-size="13" font-weight="bold" text-anchor="middle">P(x) = 5x⁴ - 3x² + 7x - 9</text>
    <rect x="30" y="80" width="280" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="105" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Degree = Highest Exponent = 4</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the degree of the polynomial \(5x^4 - 3x^2 + 7x - 9\)?</p>
</div>""",
     ["4", "2", "1", "0"],
     "A", "OSC", "easy",
     r"The degree is the maximum exponent of the variable \(x\), which is 4."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Numerical Coefficient Identification -->
    <rect x="40" y="25" width="260" height="40" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="170" y="50" fill="#fbbf24" font-size="14" font-weight="bold" text-anchor="middle">Term: -7x²y</text>
    <rect x="40" y="80" width="260" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="105" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Numerical Coefficient = -7</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the numerical coefficient of the term \(-7x^2y\)?</p>
</div>""",
     ["-7", "7", r"\(x^2y\)", "-1"],
     "A", "OSC", "easy",
     r"The numerical factor multiplying the variables is \(-7\)."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Commutative like terms card -->
    <rect x="30" y="25" width="130" height="70" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="95" y="55" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">7 · (x · y)</text>
    <text x="95" y="80" fill="#94a3b8" font-size="11" text-anchor="middle">= 7xy</text>
    <rect x="180" y="25" width="130" height="70" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="245" y="55" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">-5 · (y · x)</text>
    <text x="245" y="80" fill="#94a3b8" font-size="11" text-anchor="middle">= -5xy</text>
    <text x="170" y="125" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">xy ≡ yx  ==&gt;  Like Terms!</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Why are \(7xy\) and \(-5yx\) like terms despite the reversed letter order?</p>
</div>""",
     ["Multiplication of variables is commutative (\(xy = yx\))", "Both have negative coefficients", "They both equal zero", "They are constants"],
     "A", "OSC", "easy",
     r"Since variable multiplication is commutative (\(xy = yx\)), the algebraic factors are identical, confirming they are like terms."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Constant term identification -->
    <rect x="30" y="25" width="280" height="40" rx="6" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
    <text x="170" y="50" fill="#f472b6" font-size="13" font-weight="bold" text-anchor="middle">3x²y - 5xy² + 7xy - 2</text>
    <rect x="30" y="80" width="280" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="105" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Constant Term (Independent of x, y) = -2</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the constant term in the expression shown?</p>
</div>""",
     ["-2", "2", "7", "3"],
     "A", "OSC", "easy",
     r"The constant term contains no variable factors, which is \(-2\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Degree of Multivariable Monomial -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="45" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Monomial: 3x²y³</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Degree = Exponent of x + Exponent of y = 2 + 3 = 5</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the degree of the multivariable term \(3x^2y^3\)?</p>
</div>""",
     ["5", "2", "3", "6"],
     "A", "OSC", "easy",
     r"The degree of a monomial in multiple variables is the sum of their powers: \(2 + 3 = 5\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Constant Polynomial Degree 0 -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="170" y="45" fill="#fbbf24" font-size="13" font-weight="bold" text-anchor="middle">Non-Zero Constant: 7</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">7 = 7 * x⁰  ==&gt;  Degree = 0</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the degree of any non-zero constant polynomial like 7?</p>
</div>""",
     ["0", "1", "7", "Undefined"],
     "A", "OSC", "easy",
     r"Since \(7 = 7x^0\), the degree of any non-zero constant polynomial is 0."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="130" viewBox="0 0 340 130" xmlns="http://www.w3.org/2000/svg">
    <!-- Coefficient of x^2 in 1 + x + x^2 -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#0ea5e9" stroke-width="2"/>
    <text x="170" y="45" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Expression: 1 + x + x²</text>
    <rect x="30" y="75" width="280" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="100" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">x² = 1 * x²  ==&gt;  Coefficient = 1</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the numerical coefficient of \(x^2\) in the polynomial \(1 + x + x^2\)?</p>
</div>""",
     ["1", "0", "2", "-1"],
     "A", "OSC", "easy",
     r"When no explicit number precedes a variable term with positive sign, the coefficient is \(1\)."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Sum of coefficients box -->
    <rect x="25" y="20" width="290" height="40" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <text x="170" y="45" fill="#c084fc" font-size="13" font-weight="bold" text-anchor="middle">P(x) = 3x² - 5x + 7</text>
    <rect x="25" y="75" width="290" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Sum of Coefficients = 3 + (-5) + 7 = 5</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the sum of the coefficients of the polynomial \(3x^2 - 5x + 7\)?</p>
</div>""",
     ["5", "15", "10", "4"],
     "A", "OSC", "easy",
     r"Sum \(= 3 - 5 + 7 = 5\).")
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch6_topic1.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
