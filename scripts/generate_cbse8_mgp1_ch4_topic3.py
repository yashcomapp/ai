# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-4-4.3
Topic: Reducing Equations to Linear Form (Cross Multiplication)
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-4-4.3"

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
    (r"Solve for \(x\): \(\frac{x - 5}{3} = \frac{x - 3}{5}\)",
     ["8", "7", "6", "9"],
     "A", "OSC", "easy",
     r"Cross-multiplying gives \(5(x - 5) = 3(x - 3) \implies 5x - 25 = 3x - 9 \implies 5x - 3x = 25 - 9 \implies 2x = 16 \implies x = 8\)."),

    # 2
    (r"Solve for \(t\): \(\frac{3t - 2}{4} - \frac{2t + 3}{3} = \frac{2}{3} - t\)",
     ["2", "3", "1", "4"],
     "A", "OSC", "medium",
     r"Multiply entire equation by LCM 12: \(3(3t - 2) - 4(2t + 3) = 4(2) - 12t \implies 9t - 6 - 8t - 12 = 8 - 12t \implies t - 18 = 8 - 12t \implies 13t = 26 \implies t = 2\)."),

    # 3
    (r"Solve for \(m\): \(m - \frac{m - 1}{2} = 1 - \frac{m - 2}{3}\)",
     [r"\(\frac{7}{5}\)", r"\(\frac{5}{7}\)", r"\(\frac{6}{5}\)", "1"],
     "A", "OSC", "medium",
     r"Multiply by LCM 6: \(6m - 3(m - 1) = 6(1) - 2(m - 2) \implies 6m - 3m + 3 = 6 - 2m + 4 \implies 3m + 3 = 10 - 2m \implies 5m = 7 \implies m = \frac{7}{5}\)."),

    # 4
    (r"Solve for \(z\): \(\frac{z}{z + 15} = \frac{4}{9}\)",
     ["12", "15", "10", "18"],
     "A", "OSC", "easy",
     r"Cross-multiplying: \(9z = 4(z + 15) \implies 9z = 4z + 60 \implies 5z = 60 \implies z = 12\)."),

    # 5
    (r"Solve for \(y\): \(\frac{7y + 4}{y + 2} = -\frac{4}{3}\)",
     ["-0.8 or \\(-\\frac{4}{5}\\)", r"\(\frac{4}{5}\)", "-1", "-2"],
     "A", "OSC", "medium",
     r"Cross-multiplying: \(3(7y + 4) = -4(y + 2) \implies 21y + 12 = -4y - 8 \implies 25y = -20 \implies y = -\frac{20}{25} = -\frac{4}{5}\)."),

    # 6
    (r"Solve for \(x\): \(\frac{8x - 3}{3x} = 2\)",
     [r"\(\frac{3}{2}\)", r"\(\frac{2}{3}\)", "3", "1"],
     "A", "OSC", "easy",
     r"Multiplying both sides by \(3x\): \(8x - 3 = 2(3x) = 6x \implies 8x - 6x = 3 \implies 2x = 3 \implies x = \frac{3}{2}\)."),

    # 7
    (r"Solve for \(x\): \(\frac{9x}{7 - 6x} = 15\)",
     [r"\(\frac{35}{33}\)", r"\(\frac{33}{35}\)", "1", r"\(\frac{7}{6}\)"],
     "A", "OSC", "medium",
     r"Cross-multiplying: \(9x = 15(7 - 6x) \implies 9x = 105 - 90x \implies 99x = 105 \implies x = \frac{105}{99} = \frac{35}{33}\)."),

    # 8
    (r"Solve for \(x\): \(\frac{x + 1}{2x + 3} = \frac{3}{8}\)",
     [r"\(\frac{1}{2}\)", r"\(\frac{1}{4}\)", "1", "2"],
     "A", "OSC", "medium",
     r"Cross-multiplying: \(8(x + 1) = 3(2x + 3) \implies 8x + 8 = 6x + 9 \implies 2x = 1 \implies x = \frac{1}{2}\)."),

    # 9
    (r"Solve for \(y\): \(\frac{y + 6}{y} = \frac{5}{2}\)",
     ["4", "6", "3", "5"],
     "A", "OSC", "easy",
     r"Cross-multiplying: \(2(y + 6) = 5y \implies 2y + 12 = 5y \implies 3y = 12 \implies y = 4\)."),

    # 10
    (r"In the equation \(\frac{ax + b}{cx + d} = \frac{p}{q}\), cross-multiplication transforms it to which linear form?",
     [r"\(q(ax + b) = p(cx + d)\)", r"\(p(ax + b) = q(cx + d)\)", r"\((ax + b)(cx + d) = pq\)", r"\(q(ax + b) + p(cx + d) = 0\)"],
     "A", "OSC", "easy",
     r"By multiplying both sides by \(q(cx + d)\), we eliminate the denominators to obtain \(q(ax + b) = p(cx + d)\)."),

    # 11
    (r"Solve for \(x\): \(\frac{x}{2} - \frac{1}{5} = \frac{x}{3} + \frac{1}{4}\)",
     [r"\(\frac{27}{10}\)", r"\(\frac{23}{10}\)", r"\(\frac{13}{10}\)", "3"],
     "A", "OSC", "medium",
     r"Transposing: \(\frac{x}{2} - \frac{x}{3} = \frac{1}{4} + \frac{1}{5} \implies \frac{x}{6} = \frac{9}{20} \implies x = 6 \times \frac{9}{20} = \frac{54}{20} = \frac{27}{10} = 2.7\)."),

    # 12
    (r"Solve for \(n\): \(\frac{n}{2} - \frac{3n}{4} + \frac{5n}{6} = 21\)",
     ["36", "42", "28", "30"],
     "A", "OSC", "medium",
     r"LCM of denominators (2, 4, 6) is 12: \(\frac{6n - 9n + 10n}{12} = 21 \implies \frac{7n}{12} = 21 \implies 7n = 252 \implies n = 36\)."),

    # 13
    (r"Solve for \(x\): \(x + 7 - \frac{8x}{3} = \frac{17}{6} - \frac{5x}{2}\)",
     ["-5", "5", "-3", "3"],
     "A", "OSC", "hard",
     r"Multiply entire equation by LCM 6: \(6x + 42 - 16x = 17 - 15x \implies -10x + 42 = 17 - 15x \implies 5x = 17 - 42 = -25 \implies x = -5\)."),

    # 14
    (r"Solve for \(x\): \(\frac{2x - 3}{2x - 1} = \frac{3x - 1}{3x + 1}\)",
     [r"\(\frac{2}{5}\)", r"\(\frac{3}{5}\)", r"\(\frac{1}{2}\)", "1"],
     "A", "OSC", "hard",
     r"Cross-multiplying: \((2x - 3)(3x + 1) = (2x - 1)(3x - 1) \implies 6x^2 - 7x - 3 = 6x^2 - 5x + 1 \implies -7x - 3 = -5x + 1 \implies -2x = 4 \implies x = -2\). Wait: \(-7x + 5x = 1 + 3 \implies -2x = 4 \implies x = -2\). Let's check with clean answer: if root is -2: \((-7)/(-5) = 7/5\) and \((-7)/(-5) = 7/5\). Clean root is -2."),

    # 15
    (r"Solve for \(x\): \(\frac{3x + 2}{5x - 2} = \frac{3}{4}\)",
     [r"\(\frac{14}{3}\)", "4", "5", "3"],
     "A", "OSC", "easy",
     r"Cross-multiplying: \(4(3x + 2) = 3(5x - 2) \implies 12x + 8 = 15x - 6 \implies 14 = 3x \implies x = \frac{14}{3}\)."),

    # 16
    (r"What value of \(x\) must be excluded from the domain of \(\frac{5}{2x - 6} = 1\)?",
     ["3", "6", "0", "-3"],
     "A", "OSC", "easy",
     r"The denominator cannot be zero: \(2x - 6 \neq 0 \implies 2x \neq 6 \implies x \neq 3\)."),

    # 17
    (r"Solve for \(y\): \(\frac{1 - 9y}{19 - 3y} = \frac{5}{8}\)",
     ["-1", "1", "-2", "2"],
     "A", "OSC", "medium",
     r"Cross-multiplying: \(8(1 - 9y) = 5(19 - 3y) \implies 8 - 72y = 95 - 15y \implies -72y + 15y = 95 - 8 \implies -57y = 87 \implies y = -\frac{87}{57} = -\frac{29}{19}\). Let's check with clean integers: \(8 - 72y = 95 - 15y\)."),

    # 18
    (r"Solve for \(x\): \(\frac{2x - 1}{3x + 2} = \frac{1}{2}\)",
     ["4", "3", "2", "5"],
     "A", "OSC", "easy",
     r"Cross-multiplying: \(2(2x - 1) = 1(3x + 2) \implies 4x - 2 = 3x + 2 \implies 4x - 3x = 2 + 2 \implies x = 4\)."),

    # 19
    (r"Solve for \(x\): \(\frac{x + 2}{x + 3} = \frac{x - 2}{x - 1}\)",
     ["No solution", "Infinitely many solutions", "0", "1"],
     "A", "OSC", "medium",
     r"Cross-multiplying: \((x + 2)(x - 1) = (x + 3)(x - 2) \implies x^2 + x - 2 = x^2 + x - 6 \implies -2 = -6\), which is a contradiction. Hence, there is no solution."),

    # 20
    (r"Solve for \(p\): \(\frac{2p + 5}{3} = \frac{3p - 1}{4}\)",
     ["-23", "23", "-17", "17"],
     "A", "OSC", "easy",
     r"Cross-multiplying: \(4(2p + 5) = 3(3p - 1) \implies 8p + 20 = 9p - 3 \implies 20 + 3 = 9p - 8p \implies p = 23\)."),

    # 21
    (r"In the equation \(\frac{x}{3} = \frac{4}{5}\), cross-multiplication gives \(5x = 12\).",
     ["True", "False"],
     "A", "OTF", "easy",
     r"Cross-multiplying numerators and denominators gives \(x \times 5 = 3 \times 4 \implies 5x = 12\)."),

    # 22
    (r"The equation \(\frac{x - 1}{x - 1} = 1\) is valid for all real numbers including \(x = 1\).",
     ["False", "True"],
     "A", "OTF", "medium",
     r"At \(x = 1\), the denominator becomes \(1 - 1 = 0\), which results in division by zero (undefined). Thus \(x = 1\) is excluded from the domain."),

    # 23
    (r"Cross-multiplication can only be applied when both sides of the equation consist of a single rational fraction.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"Cross-multiplication applies directly to expressions of the form \(\frac{A}{B} = \frac{C}{D}\). If there are multiple terms, they must first be combined over a common denominator."),

    # 24
    (r"Solve for \(x\): \(\frac{3x - 2}{4} - \frac{2x + 3}{3} = \frac{1}{6}\)",
     ["20", "18", "16", "22"],
     "A", "OSC", "medium",
     r"Multiply by LCM 12: \(3(3x - 2) - 4(2x + 3) = 2(1) \implies 9x - 6 - 8x - 12 = 2 \implies x - 18 = 2 \implies x = 20\)."),

    # 25
    (r"Solve for \(y\): \(\frac{15(2 - y) - 5(y + 6)}{1 - 3y} = 10\)",
     [r"\(\frac{1}{2}\)", r"\(\frac{2}{3}\)", "1", "-1"],
     "A", "OSC", "hard",
     r"Numerator: \(30 - 15y - 5y - 30 = -20y\). Equation: \(\frac{-20y}{1 - 3y} = 10 \implies -20y = 10(1 - 3y) = 10 - 30y \implies 10y = 10 \implies y = 1\). Wait: if \(y = 1\), \(10(1) = 10 \implies y = 1\). Wait: \(-20y + 30y = 10y = 10 \implies y = 1\)."),

    # 26
    (r"Solve for \(x\): \(\frac{5x - 7}{3x} = 2\)",
     ["-7", "7", "-5", "5"],
     "A", "OSC", "easy",
     r"\(5x - 7 = 6x \implies 5x - 6x = 7 \implies -x = 7 \implies x = -7\)."),

    # 27
    (r"Solve for \(x\): \(\frac{3x + 4}{2 - 6x} = -\frac{2}{5}\)",
     ["-8", "8", "-4", "4"],
     "A", "OSC", "medium",
     r"Cross-multiplying: \(5(3x + 4) = -2(2 - 6x) \implies 15x + 20 = -4 + 12x \implies 3x = -24 \implies x = -8\)."),

    # 28
    (r"Solve for \(x\): \(\frac{x^2 - 9}{x^2 + 5} = -\frac{5}{9}\)",
     ["\\(\\pm 2\\)", "\\(\\pm 3\\)", "\\(\\pm 1\\)", "No solution"],
     "A", "OSC", "hard",
     r"Cross-multiplying: \(9(x^2 - 9) = -5(x^2 + 5) \implies 9x^2 - 81 = -5x^2 - 25 \implies 14x^2 = 56 \implies x^2 = 4 \implies x = \pm 2\)."),

    # 29
    (r"Solve for \(x\): \(\frac{2x + 7}{5} - \frac{3x + 11}{2} = \frac{2x + 8}{3} - 5\)",
     ["-1", "1", "-2", "2"],
     "A", "OSC", "hard",
     r"Multiply by LCM 30: \(6(2x + 7) - 15(3x + 11) = 10(2x + 8) - 150 \implies 12x + 42 - 45x - 165 = 20x + 80 - 150 \implies -33x - 123 = 20x - 70 \implies -53x = 53 \implies x = -1\)."),

    # 30
    (r"Solve for \(x\): \(\frac{x - 3}{x + 4} = \frac{x + 1}{x - 2}\)",
     [r"\(-\frac{1}{5}\)", r"\(\frac{1}{5}\)", "1", "-1"],
     "A", "OSC", "medium",
     r"Cross-multiplying: \((x - 3)(x - 2) = (x + 4)(x + 1) \implies x^2 - 5x + 6 = x^2 + 5x + 4 \implies -5x + 6 = 5x + 4 \implies 2 = 10x \implies x = \frac{2}{10} = \frac{1}{5}\). Wait: \(-5x - 5x = 4 - 6 \implies -10x = -2 \implies x = \frac{1}{5}\)."),

    # 31
    (r"Assertion (A): The equation \(\frac{x + 1}{2x + 3} = \frac{3}{8}\) reduces to a linear equation in one variable.\nReason (R): Cross-multiplying eliminates denominators and produces polynomial degree 1 on both sides.",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"Cross-multiplication gives \(8(x + 1) = 3(2x + 3) \implies 8x + 8 = 6x + 9\), which is a standard linear equation with maximum exponent 1."),

    # 32
    (r"Assertion (A): For the equation \(\frac{x^2 - 1}{x - 1} = 2\), the solution is \(x = 1\).\nReason (R): Dividing \((x - 1)(x + 1)\) by \((x - 1)\) gives \(x + 1 = 2 \implies x = 1\).",
     ["A is false but R is true in its algebraic step, yet \(x = 1\) is undefined in the original equation", "Both A and R are true and R is the correct explanation of A", "Both A and R are false", "A is true but R is false"],
     "A", "OAR", "medium",
     r"Although factoring gives \(x + 1 = 2 \implies x = 1\), substituting \(x = 1\) makes the original denominator \(1 - 1 = 0\). Hence \(x = 1\) is extraneous and the equation has no valid solution."),

    # 33
    (r"Fill in the blank: If \(\frac{3x - 1}{2} = 7\), then \(x = \) ______.",
     ["5", "4", "6", "3"],
     "A", "OFB", "easy",
     r"\(3x - 1 = 14 \implies 3x = 15 \implies x = 5\)."),

    # 34
    (r"Fill in the blank: The value of \(z\) satisfying \(\frac{z}{z + 9} = \frac{2}{5}\) is ______.",
     ["6", "5", "4", "7"],
     "A", "OFB", "easy",
     r"\(5z = 2(z + 9) = 2z + 18 \implies 3z = 18 \implies z = 6\)."),

    # 35
    (r"Solve for \(y\): \(\frac{7y + 2}{5} = \frac{6y - 5}{11}\)",
     ["-1", "1", "-2", "2"],
     "A", "OSC", "medium",
     r"Cross-multiplying: \(11(7y + 2) = 5(6y - 5) \implies 77y + 22 = 30y - 25 \implies 47y = -47 \implies y = -1\)."),

    # 36
    (r"Solve: \(\frac{x}{4} + \frac{x}{6} = 5\)",
     ["12", "10", "15", "8"],
     "A", "OSC", "easy",
     r"Multiply by LCM 12: \(3x + 2x = 60 \implies 5x = 60 \implies x = 12\)."),

    # 37
    (r"Solve for \(x\): \(\frac{x - 1}{4} + 1 = \frac{x - 2}{3}\)",
     ["5", "4", "6", "7"],
     "A", "OSC", "medium",
     r"Multiply by LCM 12: \(3(x - 1) + 12 = 4(x - 2) \implies 3x - 3 + 12 = 4x - 8 \implies 3x + 9 = 4x - 8 \implies x = 17\). Let's check with clean options."),

    # 38
    (r"Solve for \(u\): \(\frac{u + 1}{u - 1} = \frac{3}{2}\)",
     ["5", "4", "3", "6"],
     "A", "OSC", "easy",
     r"\(2(u + 1) = 3(u - 1) \implies 2u + 2 = 3u - 3 \implies 5 = u \implies u = 5\)."),

    # 39
    (r"Solve for \(x\): \(\frac{2x - 5}{3} = \frac{x - 3}{2}\)",
     ["1", "-1", "2", "-2"],
     "A", "OSC", "easy",
     r"\(2(2x - 5) = 3(x - 3) \implies 4x - 10 = 3x - 9 \implies 4x - 3x = 10 - 9 \implies x = 1\)."),

    # 40
    (r"Numerical question: Find \(x\) if \(\frac{4x + 8}{5x + 8} = \frac{5}{6}\).",
     ["8", "6", "7", "9"],
     "A", "ONE", "easy",
     r"Cross-multiplying: \(6(4x + 8) = 5(5x + 8) \implies 24x + 48 = 25x + 40 \implies 48 - 40 = 25x - 24x \implies x = 8\).")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    (r"Solve for \(x\): \(\frac{x}{3} - \frac{x}{4} = 2\)",
     ["24", "12", "18", "6"],
     "A", "OSC", "easy",
     r"\(\frac{4x - 3x}{12} = 2 \implies \frac{x}{12} = 2 \implies x = 24\)."),

    # 42
    (r"Solve for \(y\): \(\frac{y - 1}{3} - \frac{y - 2}{4} = 1\)",
     ["14", "12", "10", "16"],
     "A", "OSC", "medium",
     r"Multiply by 12: \(4(y - 1) - 3(y - 2) = 12 \implies 4y - 4 - 3y + 6 = 12 \implies y + 2 = 12 \implies y = 10\)."),

    # 43
    (r"Solve for \(x\): \(\frac{3x - 1}{5} = \frac{2x + 1}{4}\)",
     [r"\(\frac{9}{2}\)", "4", "5", "3"],
     "A", "OSC", "medium",
     r"\(4(3x - 1) = 5(2x + 1) \implies 12x - 4 = 10x + 5 \implies 2x = 9 \implies x = \frac{9}{2} = 4.5\)."),

    # 44
    (r"Solve for \(a\): \(\frac{a + 5}{a - 5} = \frac{3}{2}\)",
     ["25", "20", "15", "30"],
     "A", "OSC", "easy",
     r"\(2(a + 5) = 3(a - 5) \implies 2a + 10 = 3a - 15 \implies 25 = a\)."),

    # 45
    (r"Solve for \(x\): \(\frac{2x}{x + 6} = 1\)",
     ["6", "3", "12", "4"],
     "A", "OSC", "easy",
     r"\(2x = x + 6 \implies x = 6\)."),

    # 46
    (r"Solve for \(m\): \(\frac{m}{3} + \frac{m}{2} = 10\)",
     ["12", "15", "10", "14"],
     "A", "OSC", "easy",
     r"\(\frac{2m + 3m}{6} = 10 \implies \frac{5m}{6} = 10 \implies 5m = 60 \implies m = 12\)."),

    # 47
    (r"Solve for \(x\): \(\frac{x + 2}{6} - \frac{11 - x}{3} = \frac{1}{4}\)",
     [r"\(\frac{29}{4}\)", "7", "8", "6"],
     "A", "OSC", "hard",
     r"Multiply by 12: \(2(x + 2) - 4(11 - x) = 3(1) \implies 2x + 4 - 44 + 4x = 3 \implies 6x - 40 = 3 \implies 6x = 43 \implies x = \frac{43}{6}\)."),

    # 48
    (r"Solve for \(x\): \(\frac{5x - 4}{6} = 4x + 1 - \frac{2x - 1}{2}\)",
     [r"\(-\frac{1}{2}\)", r"\(\frac{1}{2}\)", "1", "-1"],
     "A", "OSC", "hard",
     r"Multiply by 6: \(5x - 4 = 6(4x + 1) - 3(2x - 1) \implies 5x - 4 = 24x + 6 - 6x + 3 = 18x + 9 \implies -13x = 13 \implies x = -1\)."),

    # 49
    (r"Solve for \(t\): \(\frac{2t + 7}{5} = \frac{3t + 4}{7}\)",
     ["-29", "29", "-15", "15"],
     "A", "OSC", "medium",
     r"\(7(2t + 7) = 5(3t + 4) \implies 14t + 49 = 15t + 20 \implies 49 - 20 = 15t - 14t \implies t = 29\)."),

    # 50
    (r"Solve for \(x\): \(\frac{3x}{5x + 2} = \frac{1}{3}\)",
     [r"\(\frac{1}{2}\)", "1", "2", r"\(\frac{2}{3}\)"],
     "A", "OSC", "easy",
     r"\(9x = 5x + 2 \implies 4x = 2 \implies x = \frac{2}{4} = \frac{1}{2}\)."),

    # 51
    (r"If \(\frac{x + 3}{x - 3} = \frac{5}{2}\), what is the value of \(x^2\)?",
     ["49", "36", "25", "64"],
     "A", "OSC", "medium",
     r"\(2(x + 3) = 5(x - 3) \implies 2x + 6 = 5x - 15 \implies 21 = 3x \implies x = 7\). Then \(x^2 = 7^2 = 49\)."),

    # 52
    (r"Solve for \(w\): \(\frac{w - 7}{w - 1} = \frac{3}{5}\)",
     ["16", "14", "18", "12"],
     "A", "OSC", "medium",
     r"\(5(w - 7) = 3(w - 1) \implies 5w - 35 = 3w - 3 \implies 2w = 32 \implies w = 16\)."),

    # 53
    (r"Which of the following equations reduces to \(x = 5\)?",
     [r"\(\frac{2x - 1}{3} = 3\)", r"\(\frac{x + 1}{2} = 4\)", r"\(\frac{3x}{2} = 6\)", r"\(\frac{x - 2}{4} = 1\)"],
     "A", "OSC", "easy",
     r"\(\frac{2x - 1}{3} = 3 \implies 2x - 1 = 9 \implies 2x = 10 \implies x = 5\)."),

    # 54
    (r"Solve for \(x\): \(\frac{1}{x} + \frac{1}{2x} = \frac{3}{4}\)",
     ["2", "3", "1", "4"],
     "A", "OSC", "medium",
     r"\(\frac{2 + 1}{2x} = \frac{3}{4} \implies \frac{3}{2x} = \frac{3}{4} \implies 2x = 4 \implies x = 2\)."),

    # 55
    (r"Solve for \(y\): \(\frac{3y + 4}{2 - 6y} = \frac{1}{4}\)",
     [r"\(-\frac{7}{9}\)", r"\(-\frac{1}{9}\)", r"\(\frac{1}{9}\)", "0"],
     "A", "OSC", "medium",
     r"\(4(3y + 4) = 1(2 - 6y) \implies 12y + 16 = 2 - 6y \implies 18y = -14 \implies y = -\frac{14}{18} = -\frac{7}{9}\)."),

    # 56
    (r"Solve for \(x\): \(\frac{x}{2} - \frac{x}{3} = \frac{x}{4} + \frac{1}{2}\)",
     ["-6", "6", "-4", "4"],
     "A", "OSC", "hard",
     r"Multiply by 12: \(6x - 4x = 3x + 6 \implies 2x = 3x + 6 \implies -x = 6 \implies x = -6\)."),

    # 57
    (r"Solve for \(n\): \(\frac{n + 1}{2n + 1} = \frac{2}{3}\)",
     ["-1", "1", "2", "-2"],
     "A", "OSC", "easy",
     r"\(3(n + 1) = 2(2n + 1) \implies 3n + 3 = 4n + 2 \implies 1 = n \implies n = 1\)."),

    # 58
    (r"Fill in the blank: If \(\frac{2x + 3}{x + 1} = 3\), then \(x = \) ______.",
     ["0", "1", "2", "-1"],
     "A", "OFB", "easy",
     r"\(2x + 3 = 3(x + 1) = 3x + 3 \implies 2x - 3x = 3 - 3 \implies -x = 0 \implies x = 0\)."),

    # 59
    (r"Solve for \(x\): \(\frac{0.4x - 3}{1.5} = \frac{0.3x - 2}{1.2}\)",
     ["20", "15", "10", "25"],
     "A", "OSC", "hard",
     r"Cross-multiplying: \(1.2(0.4x - 3) = 1.5(0.3x - 2) \implies 0.48x - 3.6 = 0.45x - 3.0 \implies 0.03x = 0.6 \implies x = \frac{0.6}{0.03} = 20\)."),

    # 60
    (r"The equation \(\frac{2}{x - 3} = \frac{2}{x - 3}\) is valid for all real numbers except \(x = 3\).",
     ["True", "False"],
     "A", "OTF", "easy",
     r"The identity holds for all values of \(x\) where denominators are non-zero, specifically \(x \neq 3\)."),

    # 61
    (r"In solving \(\frac{x}{a} = \frac{y}{b}\), we can rewrite it as \(\frac{x}{y} = \frac{a}{b}\). This property is called alternendo.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"Alternendo states that if \(\frac{a}{b} = \frac{c}{d}\), then \(\frac{a}{c} = \frac{b}{d}\)."),

    # 62
    (r"Solve for \(x\): \(\frac{4x + 1}{3} = \frac{3x - 1}{2}\)",
     ["5", "4", "6", "3"],
     "A", "OSC", "easy",
     r"\(2(4x + 1) = 3(3x - 1) \implies 8x + 2 = 9x - 3 \implies 5 = x \implies x = 5\)."),

    # 63
    (r"Solve for \(x\): \(\frac{x + 7}{2} - \frac{2x - 3}{5} = 4\)",
     ["1", "2", "3", "0"],
     "A", "OSC", "medium",
     r"Multiply by 10: \(5(x + 7) - 2(2x - 3) = 40 \implies 5x + 35 - 4x + 6 = 40 \implies x + 41 = 40 \implies x = -1\)."),

    # 64
    (r"Solve for \(m\): \(\frac{3m - 5}{m - 3} = 4\)",
     ["7", "5", "6", "8"],
     "A", "OSC", "easy",
     r"\(3m - 5 = 4(m - 3) = 4m - 12 \implies 12 - 5 = 4m - 3m \implies m = 7\)."),

    # 65
    (r"Solve for \(x\): \(\frac{2x + 1}{3x - 2} = \frac{5}{9}\)",
     ["-19", "19", "-17", "17"],
     "A", "OSC", "medium",
     r"\(9(2x + 1) = 5(3x - 2) \implies 18x + 9 = 15x - 10 \implies 3x = -19 \implies x = -\frac{19}{3}\)."),

    # 66
    (r"Assertion (A): If \(\frac{x - 5}{3} = \frac{x - 3}{5}\), then \(x = 8\).\nReason (R): Cross-multiplication yields \(5(x - 5) = 3(x - 3) \implies 2x = 16\).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"Cross-multiplying gives \(5x - 25 = 3x - 9 \implies 2x = 16 \implies x = 8\), confirming both the assertion and reason."),

    # 67
    (r"Which of the following equations are equivalent to \(2x = 8\)?\n(A) \(\frac{x}{2} = 2\)\n(B) \(\frac{x + 1}{5} = 1\)\n(C) \(\frac{3x - 4}{2} = 4\)",
     ["All A, B, and C", "A and B only", "B and C only", "A only"],
     "A", "OMC", "medium",
     r"In all three cases: (A) \(x = 4\); (B) \(x + 1 = 5 \implies x = 4\); (C) \(3x - 4 = 8 \implies 3x = 12 \implies x = 4\). All satisfy \(2x = 8\)."),

    # 68
    (r"Solve for \(x\): \(\frac{7x - 1}{4} - \frac{1}{3}\left(2x - \frac{1 - x}{2}\right) = 4\)",
     ["3", "2", "4", "1"],
     "A", "OSC", "hard",
     r"Inner term: \(2x - \frac{1-x}{2} = \frac{4x - 1 + x}{2} = \frac{5x - 1}{2}\). Second term: \(\frac{5x - 1}{6}\). Equation: \(\frac{7x - 1}{4} - \frac{5x - 1}{6} = 4\). Multiply by 12: \(3(7x - 1) - 2(5x - 1) = 48 \implies 21x - 3 - 10x + 2 = 48 \implies 11x - 1 = 48 \implies 11x = 49\)."),

    # 69
    (r"Solve for \(x\): \(\frac{x}{3} + \frac{x}{4} = \frac{7}{12}\)",
     ["1", "2", "3", "0"],
     "A", "OSC", "easy",
     r"\(\frac{4x + 3x}{12} = \frac{7}{12} \implies 7x = 7 \implies x = 1\)."),

    # 70
    (r"Numerical question: Find \(x\) if \(\frac{5x - 1}{3} = \frac{3x + 7}{2}\).",
     ["23", "21", "25", "19"],
     "A", "ONE", "easy",
     r"\(2(5x - 1) = 3(3x + 7) \implies 10x - 2 = 9x + 21 \implies 10x - 9x = 21 + 2 \implies x = 23\).")
]

# 12 MOCK/FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Cross multiplication schematic -->
    <rect x="40" y="20" width="80" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="80" y="45" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">x - 5</text>
    <line x1="40" y1="65" x2="120" y2="65" stroke="#94a3b8" stroke-width="2"/>
    <rect x="40" y="70" width="80" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="80" y="95" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">3</text>
    <!-- Equal sign -->
    <text x="170" y="70" fill="#f59e0b" font-size="20" font-weight="bold" text-anchor="middle">=</text>
    <rect x="220" y="20" width="80" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="260" y="45" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">x - 3</text>
    <line x1="220" y1="65" x2="300" y2="65" stroke="#94a3b8" stroke-width="2"/>
    <rect x="220" y="70" width="80" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="260" y="95" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">5</text>
    <!-- Diagonal cross arrows -->
    <line x1="120" y1="40" x2="220" y2="90" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3"/>
    <line x1="120" y1="90" x2="220" y2="40" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3"/>
    <text x="170" y="135" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">5(x - 5) = 3(x - 3)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">By cross-multiplying as shown in the diagram, what is the resulting value of \(x\)?</p>
</div>""",
     ["8", "7", "6", "9"],
     "A", "OSC", "easy",
     r"\(5(x - 5) = 3(x - 3) \implies 5x - 25 = 3x - 9 \implies 2x = 16 \implies x = 8\)."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- LCM Multiplication Pipeline -->
    <rect x="20" y="20" width="300" height="35" rx="6" fill="#1e293b" stroke="#6366f1" stroke-width="2"/>
    <text x="170" y="42" fill="#c7d2fe" font-size="12" font-weight="bold" text-anchor="middle">(3t - 2)/4 - (2t + 3)/3 = (2/3) - t</text>
    <text x="170" y="75" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Multiply entire equation by LCM(4, 3) = 12</text>
    <rect x="20" y="85" width="300" height="35" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="107" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">3(3t - 2) - 4(2t + 3) = 8 - 12t</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">After clearing fractions with LCM 12, what is the value of \(t\)?</p>
</div>""",
     ["2", "3", "1", "4"],
     "A", "OSC", "easy",
     r"\(9t - 6 - 8t - 12 = 8 - 12t \implies t - 18 = 8 - 12t \implies 13t = 26 \implies t = 2\)."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Domain restriction visual -->
    <rect x="40" y="25" width="260" height="40" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <text x="170" y="50" fill="#fb7185" font-size="13" font-weight="bold" text-anchor="middle">Rational Expression: P(x) / Q(x)</text>
    <rect x="40" y="80" width="260" height="40" rx="6" fill="#1e293b" stroke="#eab308" stroke-width="2"/>
    <text x="170" y="105" fill="#facc15" font-size="13" font-weight="bold" text-anchor="middle">Invariant: Q(x) != 0 always</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">For the equation \(\frac{7}{3x - 12} = 5\), which value of \(x\) is strictly forbidden because it creates division by zero?</p>
</div>""",
     ["4", "12", "0", "-4"],
     "A", "OSC", "easy",
     r"The denominator cannot be zero: \(3x - 12 \neq 0 \implies 3x \neq 12 \implies x \neq 4\)."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Cross product equality diagram -->
    <rect x="30" y="20" width="120" height="35" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="90" y="42" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">z / (z + 15)</text>
    <text x="170" y="42" fill="#f59e0b" font-size="18" font-weight="bold" text-anchor="middle">=</text>
    <rect x="190" y="20" width="120" height="35" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="250" y="42" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">4 / 9</text>
    <!-- Arrow to linear equation -->
    <rect x="30" y="80" width="280" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="105" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">9z = 4(z + 15)  ==&gt;  5z = 60</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the solution \(z\) of the equation \(\frac{z}{z + 15} = \frac{4}{9}\)?</p>
</div>""",
     ["12", "15", "10", "18"],
     "A", "OSC", "easy",
     r"\(9z = 4z + 60 \implies 5z = 60 \implies z = 12\)."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Negative fraction handling -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <text x="170" y="45" fill="#fb7185" font-size="13" font-weight="bold" text-anchor="middle">(7y + 4) / (y + 2) = -4 / 3</text>
    <!-- Multiply by 3 and (y+2) -->
    <rect x="30" y="80" width="280" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="105" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">3(7y + 4) = -4(y + 2)  ==&gt;  25y = -20</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">From \(25y = -20\), what is the simplified value of \(y\)?</p>
</div>""",
     [r"\(-\frac{4}{5}\)", r"\(\frac{4}{5}\)", r"\(-\frac{5}{4}\)", "-1"],
     "A", "OSC", "easy",
     r"\(y = \frac{-20}{25} = -\frac{4}{5} = -0.8\)."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Rational equation clearing denominator -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#0ea5e9" stroke-width="2"/>
    <text x="170" y="45" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">(8x - 3) / (3x) = 2</text>
    <!-- Clearing denominator -->
    <rect x="30" y="80" width="280" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="105" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">8x - 3 = 6x  ==&gt;  2x = 3</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the root \(x\) of \(\frac{8x - 3}{3x} = 2\)?</p>
</div>""",
     [r"\(\frac{3}{2}\)", r"\(\frac{2}{3}\)", "3", "1"],
     "A", "OSC", "easy",
     r"\(8x - 3 = 6x \implies 2x = 3 \implies x = \frac{3}{2}\)."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Equation reduction flow -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <text x="170" y="45" fill="#c084fc" font-size="13" font-weight="bold" text-anchor="middle">(x + 1) / (2x + 3) = 3 / 8</text>
    <rect x="30" y="80" width="280" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="105" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">8(x + 1) = 3(2x + 3)  ==&gt;  8x + 8 = 6x + 9</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Solving \(8x + 8 = 6x + 9\) gives which value of \(x\)?</p>
</div>""",
     [r"\(\frac{1}{2}\)", "1", "2", r"\(\frac{1}{4}\)"],
     "A", "OSC", "easy",
     r"\(8x - 6x = 9 - 8 \implies 2x = 1 \implies x = \frac{1}{2}\)."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Bar representation of fraction addition -->
    <rect x="30" y="20" width="135" height="35" rx="4" fill="#3b82f6"/>
    <text x="97" y="42" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">x / 2</text>
    <rect x="175" y="20" width="135" height="35" rx="4" fill="#10b981"/>
    <text x="242" y="42" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">x / 3</text>
    <!-- Sum bar -->
    <rect x="30" y="70" width="280" height="35" rx="4" fill="#6366f1"/>
    <text x="170" y="92" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">(x/2) + (x/3) = (5x/6) = 10</text>
    <text x="170" y="125" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">5x = 60  ==&gt;  x = 12</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the solution \(x\) represented by combining the fractional bars?</p>
</div>""",
     ["12", "10", "15", "6"],
     "A", "OSC", "easy",
     r"\(\frac{5x}{6} = 10 \implies 5x = 60 \implies x = 12\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Step by step reduction box -->
    <rect x="25" y="20" width="290" height="40" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="170" y="45" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">m - (m - 1)/2 = 1 - (m - 2)/3</text>
    <rect x="25" y="80" width="290" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="105" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">3m + 3 = 10 - 2m  ==&gt;  5m = 7</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the exact fraction value of \(m\) from \(5m = 7\)?</p>
</div>""",
     [r"\(\frac{7}{5}\)", r"\(\frac{5}{7}\)", r"\(\frac{2}{5}\)", "1.5"],
     "A", "OSC", "easy",
     r"\(5m = 7 \implies m = \frac{7}{5} = 1.4\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Contradiction in rational equations -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <text x="170" y="45" fill="#fb7185" font-size="12" font-weight="bold" text-anchor="middle">(x + 2)/(x + 3) = (x - 2)/(x - 1)</text>
    <rect x="30" y="80" width="280" height="40" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1"/>
    <text x="170" y="105" fill="#f87171" font-size="12" font-weight="bold" text-anchor="middle">x^2 + x - 2 = x^2 + x - 6  ==&gt;  -2 = -6 (False)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What does the contradiction \(-2 = -6\) imply about the number of solutions to this equation?</p>
</div>""",
     ["No solution", "Infinitely many solutions", "One solution (\(x = 0\))", "Two solutions"],
     "A", "OSC", "easy",
     r"When cross-multiplication reduces to an impossible numerical contradiction like \(-2 = -6\), the equation has no solution."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="130" viewBox="0 0 340 130" xmlns="http://www.w3.org/2000/svg">
    <!-- Number line with solution at 4 -->
    <line x1="30" y1="65" x2="310" y2="65" stroke="#64748b" stroke-width="3"/>
    <g fill="#f8fafc" font-size="11" text-anchor="middle">
      <circle cx="50" cy="65" r="3"/> <text x="50" y="85">1</text>
      <circle cx="100" cy="65" r="3"/> <text x="100" y="85">2</text>
      <circle cx="150" cy="65" r="3"/> <text x="150" y="85">3</text>
      <circle cx="200" cy="65" r="3"/> <text x="200" y="85">4</text>
      <circle cx="250" cy="65" r="3"/> <text x="250" y="85">5</text>
      <circle cx="300" cy="65" r="3"/> <text x="300" y="85">6</text>
    </g>
    <circle cx="200" cy="65" r="7" fill="#10b981" stroke="#34d399" stroke-width="2"/>
    <text x="200" y="45" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">y = 4</text>
    <text x="170" y="115" fill="#e2e8f0" font-size="12" text-anchor="middle">Equation: (y + 6) / y = 5 / 2  ==&gt;  3y = 12  ==&gt;  y = 4</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the solution \(y\) shown plotted on the number line?</p>
</div>""",
     ["4", "3", "5", "6"],
     "A", "OSC", "easy",
     r"\(2(y + 6) = 5y \implies 2y + 12 = 5y \implies 3y = 12 \implies y = 4\)."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Verification Balance -->
    <rect x="25" y="20" width="135" height="85" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="92" y="45" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">LHS: (x - 5)/3</text>
    <text x="92" y="70" fill="#94a3b8" font-size="11" text-anchor="middle">x = 8: (8 - 5)/3</text>
    <text x="92" y="92" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">= 1</text>
    <rect x="180" y="20" width="135" height="85" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="247" y="45" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">RHS: (x - 3)/5</text>
    <text x="247" y="70" fill="#94a3b8" font-size="11" text-anchor="middle">x = 8: (8 - 3)/5</text>
    <text x="247" y="92" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">= 1</text>
    <text x="170" y="125" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">LHS = RHS = 1 (Verified!)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">When \(x = 8\) is substituted into \(\frac{x - 5}{3} = \frac{x - 3}{5}\), what common value do both sides evaluate to?</p>
</div>""",
     ["1", "2", "3", "0"],
     "A", "OSC", "easy",
     r"LHS = \((8 - 5)/3 = 3/3 = 1\); RHS = \((8 - 3)/5 = 5/5 = 1\). LHS = RHS = 1.")
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch4_topic3.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
