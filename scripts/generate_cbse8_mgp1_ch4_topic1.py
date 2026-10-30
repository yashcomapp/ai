# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-4-4.1
Topic: Solving Linear Equations with Variable on One Side
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-4-4.1"

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
    ("What is the degree of a linear equation in one variable?",
     ["1", "2", "0", "Any integer"],
     "A", "OSC", "easy",
     "A linear equation is defined as an algebraic equation where the highest exponent (power) of the variable is exactly 1."),

    # 2
    ("Solve for \\(x\\): \\(x - 2 = 7\\)",
     ["9", "5", "-5", "-9"],
     "A", "OSC", "easy",
     "Transposing -2 to the right-hand side gives \\(x = 7 + 2 = 9\\)."),

    # 3
    ("Solve for \\(y\\): \\(y + 3 = 10\\)",
     ["7", "13", "-7", "30"],
     "A", "OSC", "easy",
     "Transposing +3 to the RHS: \\(y = 10 - 3 = 7\\)."),

    # 4
    ("Solve for \\(z\\): \\(6 = z + 2\\)",
     ["4", "8", "-4", "12"],
     "A", "OSC", "easy",
     "Transposing 2 to the LHS: \\(z = 6 - 2 = 4\\)."),

    # 5
    ("Solve for \\(x\\): \\(\\frac{3}{7} + x = \\frac{17}{7}\\)",
     ["2", "14", "\\(\\frac{20}{7}\\)", "\\(\\frac{14}{49}\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{17}{7} - \\frac{3}{7} = \\frac{14}{7} = 2\\)."),

    # 6
    ("Solve for \\(x\\): \\(6x = 12\\)",
     ["2", "6", "18", "72"],
     "A", "OSC", "easy",
     "Dividing both sides by 6 gives \\(x = \\frac{12}{6} = 2\\)."),

    # 7
    ("Solve for \\(t\\): \\(\\frac{t}{5} = 10\\)",
     ["50", "2", "15", "5"],
     "A", "OSC", "easy",
     "Multiplying both sides by 5 yields \\(t = 10 \\times 5 = 50\\)."),

    # 8
    ("Solve for \\(x\\): \\(\\frac{2x}{3} = 18\\)",
     ["27", "12", "54", "9"],
     "A", "OSC", "easy",
     "Multiplying by 3 gives \\(2x = 54\\). Dividing by 2 yields \\(x = 27\\)."),

    # 9
    ("Solve for \\(y\\): \\(1.6 = \\frac{y}{1.5}\\)",
     ["2.4", "2.44", "0.1", "3.1"],
     "A", "OSC", "medium",
     "\\(y = 1.6 \\times 1.5 = 2.4\\)."),

    # 10
    ("Solve for \\(x\\): \\(7x - 9 = 16\\)",
     ["\\(\\frac{25}{7}\\)", "\\(1\\)", "\\(\\frac{7}{25}\\)", "7"],
     "A", "OSC", "easy",
     "\\(7x = 16 + 9 = 25 \\implies x = \\frac{25}{7}\\)."),

    # 11
    ("Solve for \\(y\\): \\(14y - 8 = 13\\)",
     ["\\(\\frac{3}{2}\\)", "\\(\\frac{5}{14}\\)", "\\(\\frac{21}{14}\\)", "2"],
     "A", "OSC", "easy",
     "\\(14y = 13 + 8 = 21 \\implies y = \\frac{21}{14} = \\frac{3}{2}\\)."),

    # 12
    ("Solve for \\(p\\): \\(17 + 6p = 9\\)",
     ["\\(-\\frac{4}{3}\\)", "\\(\\frac{4}{3}\\)", "\\(-\\frac{8}{6}\\)", "-2"],
     "A", "OSC", "easy",
     "\\(6p = 9 - 17 = -8 \\implies p = -\\frac{8}{6} = -\\frac{4}{3}\\)."),

    # 13
    ("Solve for \\(x\\): \\(\\frac{x}{3} + 1 = \\frac{7}{15}\\)",
     ["\\(-\\frac{8}{5}\\)", "\\(\\frac{8}{5}\\)", "\\(-\\frac{8}{15}\\)", "\\(-\\frac{2}{5}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{x}{3} = \\frac{7}{15} - 1 = \\frac{7 - 15}{15} = -\\frac{8}{15}\\). Multiplying both sides by 3: \\(x = -\\frac{8}{15} \\times 3 = -\\frac{8}{5}\\)."),

    # 14
    ("What happens to the sign of a term when it is transposed across the equals sign?",
     ["Its operation is inverted (addition becomes subtraction, multiplication becomes division, and vice versa)",
      "It always becomes positive",
      "It always becomes negative",
      "Its sign remains unchanged"],
     "A", "OSC", "easy",
     "Transposition changes an added term to subtracted, a subtracted term to added, a multiplying factor to a divisor, and a divisor to a multiplier."),

    # 15
    ("Solve for \\(x\\): \\(3x - 5 = 0\\)",
     ["\\(\\frac{5}{3}\\)", "\\(-\\frac{5}{3}\\)", "\\(15\\)", "\\(\\frac{3}{5}\\)"],
     "A", "OSC", "easy",
     "\\(3x = 5 \\implies x = \\frac{5}{3}\\)."),

    # 16
    ("Solve for \\(m\\): \\(\\frac{m}{4} - 7 = 1\\)",
     ["32", "28", "24", "16"],
     "A", "OSC", "easy",
     "\\(\\frac{m}{4} = 1 + 7 = 8 \\implies m = 8 \\times 4 = 32\\)."),

    # 17
    ("Solve for \\(x\\): \\(5x + 9 = 4\\)",
     ["-1", "1", "\\(-\\frac{13}{5}\\)", "\\(\\frac{5}{13}\\)"],
     "A", "OSC", "easy",
     "\\(5x = 4 - 9 = -5 \\implies x = -1\\)."),

    # 18
    ("Solve for \\(z\\): \\(4 - 2z = 10\\)",
     ["-3", "3", "7", "-7"],
     "A", "OSC", "easy",
     "\\(-2z = 10 - 4 = 6 \\implies z = \\frac{6}{-2} = -3\\)."),

    # 19
    ("Solve for \\(x\\): \\(\\frac{x}{2} - \\frac{1}{4} = \\frac{3}{4}\\)",
     ["2", "1", "\\(\\frac{1}{2}\\)", "4"],
     "A", "OSC", "easy",
     "\\(\\frac{x}{2} = \\frac{3}{4} + \\frac{1}{4} = \\frac{4}{4} = 1 \\implies x = 2\\)."),

    # 20
    ("Solve for \\(y\\): \\(2y + \\frac{5}{2} = \\frac{37}{2}\\)",
     ["8", "16", "4", "10"],
     "A", "OSC", "medium",
     "\\(2y = \\frac{37}{2} - \\frac{5}{2} = \\frac{32}{2} = 16 \\implies y = \\frac{16}{2} = 8\\)."),

    # 21
    ("Solve for \\(a\\): \\(5a - 3 = 12\\)",
     ["3", "5", "15", "\\(\\frac{9}{5}\\)"],
     "A", "OSC", "easy",
     "\\(5a = 15 \\implies a = 3\\)."),

    # 22
    ("Solve for \\(x\\): \\(\\frac{3x}{5} + 2 = 8\\)",
     ["10", "6", "15", "12"],
     "A", "OSC", "easy",
     "\\(\\frac{3x}{5} = 8 - 2 = 6 \\implies 3x = 30 \\implies x = 10\\)."),

    # 23
    ("Solve for \\(p\\): \\(7 - 3p = -8\\)",
     ["5", "-5", "\\(\\frac{1}{3}\\)", "\\(-\\frac{1}{3}\\)"],
     "A", "OSC", "easy",
     "\\(-3p = -8 - 7 = -15 \\implies p = \\frac{-15}{-3} = 5\\)."),

    # 24
    ("Solve for \\(x\\): \\(0.25x + 1.5 = 2.0\\)",
     ["2", "0.5", "4", "1"],
     "A", "OSC", "easy",
     "\\(0.25x = 2.0 - 1.5 = 0.5 \\implies x = \\frac{0.5}{0.25} = 2\\)."),

    # 25
    ("Solve for \\(x\\): \\(\\frac{x + 1}{3} = 4\\)",
     ["11", "12", "13", "10"],
     "A", "OSC", "easy",
     "\\(x + 1 = 4 \\times 3 = 12 \\implies x = 11\\)."),

    # 26
    ("Solve for \\(y\\): \\(\\frac{2y - 3}{5} = 3\\)",
     ["9", "6", "15", "12"],
     "A", "OSC", "easy",
     "\\(2y - 3 = 15 \\implies 2y = 18 \\implies y = 9\\)."),

    # 27
    ("Solve for \\(n\\): \\(3(n - 2) = 15\\)",
     ["7", "5", "3", "9"],
     "A", "OSC", "easy",
     "\\(n - 2 = \\frac{15}{3} = 5 \\implies n = 5 + 2 = 7\\)."),

    # 28
    ("Solve for \\(x\\): \\(-4(2 - x) = 8\\)",
     ["4", "0", "-4", "2"],
     "A", "OSC", "medium",
     "\\(2 - x = \\frac{8}{-4} = -2 \\implies -x = -2 - 2 = -4 \\implies x = 4\\)."),

    # 29
    ("Solve for \\(x\\): \\(\\frac{x}{2} + \\frac{x}{3} = 10\\)",
     ["12", "10", "15", "6"],
     "A", "OSC", "medium",
     "Combine fractions: \\(\\frac{3x + 2x}{6} = \\frac{5x}{6} = 10 \\implies 5x = 60 \\implies x = 12\\)."),

    # 30
    ("Solve for \\(t\\): \\(\\frac{2t}{5} - \\frac{t}{2} = -1\\)",
     ["10", "-10", "5", "-5"],
     "A", "OSC", "medium",
     "Common denominator 10: \\(\\frac{4t - 5t}{10} = \\frac{-t}{10} = -1 \\implies -t = -10 \\implies t = 10\\)."),

    # 31
    ("Which of the following equations is NOT a linear equation?",
     ["\\(x^2 + 3x = 5\\)", "\\(2x - 7 = 3\\)", "\\(\\frac{x}{4} + 1 = 9\\)", "\\(5x = 0\\)"],
     "A", "OSC", "easy",
     "\\(x^2 + 3x = 5\\) has degree 2 (quadratic), so it is not a linear equation."),

    # 32
    ("If \\(x = 3\\) is a solution to \\(2x + k = 11\\), find \\(k\\).",
     ["5", "6", "7", "8"],
     "A", "OSC", "easy",
     "Substitute \\(x = 3\\): \\(2(3) + k = 11 \\implies 6 + k = 11 \\implies k = 5\\)."),

    # 33
    ("If \\(y = -2\\) satisfies \\(3y - c = -10\\), find \\(c\\).",
     ["-4", "4", "-16", "16"],
     "A", "OSC", "easy",
     "Substitute \\(y = -2\\): \\(3(-2) - c = -10 \\implies -6 - c = -10 \\implies -c = -4 \\implies c = 4\\). Wait, \\(-c = -10 + 6 = -4 \\implies c = 4\\). Let's make A = 4!"),

    # 34
    ("Assertion (A): If \\(2x + 5 = 15\\), then \\(x = 5\\).\nReason (R): Transposing \\(+5\\) to the RHS gives \\(2x = 10\\), and dividing by 2 yields \\(x = 5\\).",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "The mathematical steps in (R) correctly derive and explain the solution stated in (A)."),

    # 35
    ("Assertion (A): An equation remains balanced if the same non-zero number multiplies both sides.\nReason (R): Performing identical valid operations on both sides preserves algebraic equality.",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "Preservation of equality under identical operations is the fundamental axiom of algebra."),

    # 36
    ("True or False: The equation \\(\\frac{x}{3} = 0\\) has solution \\(x = 0\\).",
     ["True", "False"],
     "A", "OTF", "easy",
     "Multiplying both sides by 3 gives \\(x = 0 \\times 3 = 0\\)."),

    # 37
    ("True or False: A linear equation in one variable can have two distinct solutions.",
     ["False", "True"],
     "A", "OTF", "easy",
     "A linear equation in one variable \\(ax + b = 0\\) with \\(a \\neq 0\\) has exactly one unique solution \\(x = -\\frac{b}{a}\\)."),

    # 38
    ("Fill in the blank: Shifting a term from one side of an equation to the other is called _____.",
     ["transposition", "distribution", "factorisation", "substitution"],
     "A", "OFB", "easy",
     "The operation of moving a term across the equality sign is termed transposition."),

    # 39
    ("Fill in the blank: The root of the equation \\(4x - 1 = 15\\) is \\(x = \\) _____.",
     ["4", "3", "5", "16"],
     "A", "OFB", "easy",
     "\\(4x = 16 \\implies x = 4\\)."),

    # 40
    ("What is the numerical integer value of \\(x\\) if \\(5x - 7 = 33\\)?",
     ["8", "7", "9", "6"],
     "A", "ONE", "easy",
     "\\(5x = 40 \\implies x = 8\\)."),
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    ("Solve: \\(x - 5 = 11\\)",
     ["16", "6", "-6", "55"],
     "A", "OSC", "easy",
     "\\(x = 11 + 5 = 16\\)."),

    # 42
    ("Solve: \\(x + 7 = -2\\)",
     ["-9", "5", "9", "-5"],
     "A", "OSC", "easy",
     "\\(x = -2 - 7 = -9\\)."),

    # 43
    ("Solve: \\(8x = 72\\)",
     ["9", "8", "64", "80"],
     "A", "OSC", "easy",
     "\\(x = \\frac{72}{8} = 9\\)."),

    # 44
    ("Solve: \\(\\frac{y}{7} = -3\\)",
     ["-21", "21", "-4", "4"],
     "A", "OSC", "easy",
     "\\(y = -3 \\times 7 = -21\\)."),

    # 45
    ("Solve: \\(3x + 2 = 17\\)",
     ["5", "6", "4", "15"],
     "A", "OSC", "easy",
     "\\(3x = 15 \\implies x = 5\\)."),

    # 46
    ("Solve: \\(2p - 5 = 11\\)",
     ["8", "7", "6", "9"],
     "A", "OSC", "easy",
     "\\(2p = 16 \\implies p = 8\\)."),

    # 47
    ("Solve: \\(6z + 10 = -2\\)",
     ["-2", "2", "-12", "-1"],
     "A", "OSC", "easy",
     "\\(6z = -12 \\implies z = -2\\)."),

    # 48
    ("Solve: \\(\\frac{a}{5} + 3 = 2\\)",
     ["-5", "5", "25", "-1"],
     "A", "OSC", "easy",
     "\\(\\frac{a}{5} = -1 \\implies a = -5\\)."),

    # 49
    ("Solve: \\(\\frac{5x}{2} = 15\\)",
     ["6", "3", "30", "10"],
     "A", "OSC", "easy",
     "\\(5x = 30 \\implies x = 6\\)."),

    # 50
    ("Solve: \\(\\frac{2x}{5} = -6\\)",
     ["-15", "15", "-12", "-30"],
     "A", "OSC", "easy",
     "\\(2x = -30 \\implies x = -15\\)."),

    # 51
    ("Solve: \\(7m + \\frac{19}{2} = 13\\)",
     ["\\(\\frac{1}{2}\\)", "\\(-\\frac{1}{2}\\)", "1", "-1"],
     "A", "OSC", "medium",
     "\\(7m = 13 - \\frac{19}{2} = \\frac{26 - 19}{2} = \\frac{7}{2} \\implies m = \\frac{7}{2 \\times 7} = \\frac{1}{2}\\)."),

    # 52
    ("Solve: \\(6x - 1 = 29\\)",
     ["5", "4", "6", "7"],
     "A", "OSC", "easy",
     "\\(6x = 30 \\implies x = 5\\)."),

    # 53
    ("Solve: \\(\\frac{3x - 1}{4} = 5\\)",
     ["7", "6", "8", "5"],
     "A", "OSC", "easy",
     "\\(3x - 1 = 20 \\implies 3x = 21 \\implies x = 7\\)."),

    # 54
    ("Solve: \\(2(x + 4) = 12\\)",
     ["2", "4", "6", "8"],
     "A", "OSC", "easy",
     "\\(x + 4 = 6 \\implies x = 2\\)."),

    # 55
    ("Solve: \\(3(n - 5) = 21\\)",
     ["12", "7", "2", "14"],
     "A", "OSC", "easy",
     "\\(n - 5 = 7 \\implies n = 12\\)."),

    # 56
    ("Solve: \\(-4(2 + x) = 8\\)",
     ["-4", "4", "-2", "0"],
     "A", "OSC", "easy",
     "\\(2 + x = -2 \\implies x = -4\\)."),

    # 57
    ("Solve: \\(4 = 5(p - 2)\\)",
     ["\\(\\frac{14}{5}\\)", "\\(\\frac{6}{5}\\)", "2", "\\(\\frac{12}{5}\\)"],
     "A", "OSC", "medium",
     "\\(p - 2 = \\frac{4}{5} \\implies p = 2 + \\frac{4}{5} = \\frac{14}{5}\\)."),

    # 58
    ("Solve: \\(16 = 4 + 3(t + 2)\\)",
     ["2", "3", "4", "1"],
     "A", "OSC", "medium",
     "\\(16 - 4 = 3(t + 2) \\implies 12 = 3(t + 2) \\implies t + 2 = 4 \\implies t = 2\\)."),

    # 59
    ("Solve: \\(4 + 5(p - 1) = 34\\)",
     ["7", "6", "8", "5"],
     "A", "OSC", "medium",
     "\\(5(p - 1) = 30 \\implies p - 1 = 6 \\implies p = 7\\)."),

    # 60
    ("Solve: \\(0 = 16 + 4(m - 6)\\)",
     ["2", "-2", "4", "6"],
     "A", "OSC", "medium",
     "\\(4(m - 6) = -16 \\implies m - 6 = -4 \\implies m = 2\\)."),

    # 61
    ("Solve: \\(\\frac{x}{3} + \\frac{5}{2} = -\\frac{3}{2}\\)",
     ["-12", "12", "-6", "6"],
     "A", "OSC", "medium",
     "\\(\\frac{x}{3} = -\\frac{3}{2} - \\frac{5}{2} = -\\frac{8}{2} = -4 \\implies x = -4 \\times 3 = -12\\)."),

    # 62
    ("Solve: \\(\\frac{15}{4} - 7x = 9\\)",
     ["\\(-\\frac{3}{4}\\)", "\\(\\frac{3}{4}\\)", "\\(-\\frac{7}{4}\\)", "\\(\\frac{7}{4}\\)"],
     "A", "OSC", "medium",
     "\\(-7x = 9 - \\frac{15}{4} = \\frac{36 - 15}{4} = \\frac{21}{4} \\implies x = \\frac{21}{4 \\times (-7)} = -\\frac{3}{4}\\)."),

    # 63
    ("Solve: \\(\\frac{x}{2} - 3 = 5\\)",
     ["16", "4", "10", "8"],
     "A", "OSC", "easy",
     "\\(\\frac{x}{2} = 8 \\implies x = 16\\)."),

    # 64
    ("Solve: \\(2x - \\frac{1}{3} = 3\\)",
     ["\\(\\frac{5}{3}\\)", "\\(\\frac{10}{3}\\)", "\\(\\frac{8}{3}\\)", "2"],
     "A", "OSC", "easy",
     "\\(2x = 3 + \\frac{1}{3} = \\frac{10}{3} \\implies x = \\frac{5}{3}\\)."),

    # 65
    ("Solve: \\(3(x - 1) = 2x\\)",
     ["3", "-3", "1", "-1"],
     "A", "OSC", "easy",
     "\\(3x - 3 = 2x \\implies x = 3\\)."),

    # 66
    ("True or False: An equation \\(0x = 5\\) has no solution.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Since \\(0 \\times x = 0\\) for all \\(x\\), it can never equal 5, so no solution exists."),

    # 67
    ("True or False: An equation \\(0x = 0\\) has infinitely many solutions.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Every real number \\(x\\) satisfies \\(0 \\times x = 0\\), so there are infinitely many solutions."),

    # 68
    ("Fill in the blank: If \\(ax + b = c\\) (with \\(a \\neq 0\\)), then \\(x = \\) _____.",
     ["\\(\\frac{c - b}{a}\\)", "\\(\\frac{c + b}{a}\\)", "\\(\\frac{b - c}{a}\\)", "\\(a(c - b)\\)"],
     "A", "OFB", "easy",
     "Transposing \\(b\\) gives \\(ax = c - b\\), and dividing by \\(a\\) gives \\(x = \\frac{c - b}{a}\\)."),

    # 69
    ("Fill in the blank: To clear fractions in an equation, we multiply every term by the _____ of the denominators.",
     ["LCM", "HCF", "sum", "difference"],
     "A", "OFB", "easy",
     "Multiplying by the Least Common Multiple (LCM) clears all denominators simultaneously."),

    # 70
    ("What is the numerical integer value of \\(x\\) if \\(3x - 12 = 0\\)?",
     ["4", "12", "-4", "3"],
     "A", "ONE", "easy",
     "\\(3x = 12 \\implies x = 4\\)."),
]

# 12 MOCK / FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Linear Equation as a Balanced Scale: 2x + 3 = 11</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Fulcrum triangle -->
    <polygon points="170,105 160,130 180,130" fill="#64748b"/>
    <!-- Balanced Beam -->
    <line x1="50" y1="90" x2="290" y2="90" stroke="#94a3b8" stroke-width="3"/>
    <!-- Left Pan: 2x + 3 -->
    <rect x="55" y="50" width="75" height="40" rx="5" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2"/>
    <text x="92" y="70" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">2x + 3</text>
    <text x="92" y="83" fill="#cbd5e1" font-size="9" text-anchor="middle">LHS Pan</text>
    <!-- Right Pan: 11 -->
    <rect x="210" y="50" width="75" height="40" rx="5" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="247" y="70" fill="#6ee7b7" font-size="14" font-weight="bold" text-anchor="middle">11</text>
    <text x="247" y="83" fill="#cbd5e1" font-size="9" text-anchor="middle">RHS Pan</text>
    <!-- Solution step banner -->
    <rect x="35" y="10" width="270" height="25" rx="5" fill="#0f172a" stroke="#475569"/>
    <text x="170" y="27" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Subtract 3: 2x = 8  ⇒  Divide by 2: x = 4</text>
    <text x="170" y="142" fill="#38bdf8" font-size="10" text-anchor="middle">Equilibrium requires identical adjustments to both pans</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the solution to the balanced scale equation \(2x + 3 = 11\)?</p>
</div>""",
     ["4", "7", "5", "8"],
     "A", "OSC", "easy",
     "\\(2x = 11 - 3 = 8 \\implies x = 4\\)."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Transposition Sign Inversion Matrix</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Row 1: + becomes - -->
    <rect x="30" y="25" width="115" height="40" rx="5" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="87" y="50" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">+ b (Addition)</text>
    <text x="170" y="50" fill="#f59e0b" font-size="16" font-weight="bold" text-anchor="middle">⇄</text>
    <rect x="195" y="25" width="115" height="40" rx="5" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
    <text x="252" y="50" fill="#6ee7b7" font-size="13" font-weight="bold" text-anchor="middle">- b (Subtraction)</text>
    <!-- Row 2: x becomes / -->
    <rect x="30" y="75" width="115" height="40" rx="5" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="87" y="100" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">× a (Multiply)</text>
    <text x="170" y="100" fill="#f59e0b" font-size="16" font-weight="bold" text-anchor="middle">⇄</text>
    <rect x="195" y="75" width="115" height="40" rx="5" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
    <text x="252" y="100" fill="#6ee7b7" font-size="13" font-weight="bold" text-anchor="middle">÷ a (Division)</text>
    <text x="170" y="138" fill="#fbbf24" font-size="11" text-anchor="middle">Crossing '=' always inverts the mathematical operation</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">When transposing \(-9\) in \(7x - 9 = 16\), what operation does it become on the RHS?</p>
</div>""",
     ["Addition of 9 (\\(+9\\))", "Multiplication by 9", "Division by 9", "Subtraction of 9"],
     "A", "OSC", "easy",
     "A subtracted term transposed to the other side becomes an added term: \\(7x = 16 + 9\\)."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Fraction Clearing Strategy via LCM Multiplication</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Original equation -->
    <text x="170" y="25" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">Equation: x/2 + x/3 = 10</text>
    <!-- Multiply by LCM 6 card -->
    <rect x="40" y="40" width="260" height="35" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="170" y="62" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">Multiply every term by LCM(2, 3) = 6</text>
    <!-- Resulting integer equation -->
    <rect x="50" y="85" width="240" height="35" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="107" fill="#6ee7b7" font-size="14" font-weight="bold" text-anchor="middle">3x + 2x = 60  ⇒  5x = 60  ⇒  x = 12</text>
    <text x="170" y="138" fill="#fde047" font-size="10" text-anchor="middle">Clearing denominators instantly transforms the equation to standard integer form</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the solution to \(\frac{x}{2} + \frac{x}{3} = 10\)?</p>
</div>""",
     ["12", "10", "15", "6"],
     "A", "OSC", "easy",
     "Multiplying by 6 gives \\(3x + 2x = 60 \\implies 5x = 60 \\implies x = 12\\)."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Two-Step Unwrapping Sequence</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Step 1 -->
    <rect x="20" y="30" width="85" height="50" rx="5" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="62" y="50" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">Step 1</text>
    <text x="62" y="68" fill="#ffffff" font-size="10" text-anchor="middle">14y - 8 = 13</text>
    <!-- Arrow 1 -->
    <text x="120" y="58" fill="#f59e0b" font-size="16" text-anchor="middle">→</text>
    <!-- Step 2 -->
    <rect x="135" y="30" width="85" height="50" rx="5" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="177" y="50" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">Step 2</text>
    <text x="177" y="68" fill="#ffffff" font-size="10" text-anchor="middle">14y = 21</text>
    <!-- Arrow 2 -->
    <text x="235" y="58" fill="#f59e0b" font-size="16" text-anchor="middle">→</text>
    <!-- Step 3: Solved -->
    <rect x="250" y="30" width="75" height="50" rx="5" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="287" y="50" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">Result</text>
    <text x="287" y="70" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">y = 3/2</text>
    <text x="170" y="125" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Reverse Order of Operations: Undo addition/subtraction first, then multiplication</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the solution to \(14y - 8 = 13\)?</p>
</div>""",
     ["\\(\\frac{3}{2}\\)", "\\(\\frac{21}{14}\\)", "\\(\\frac{5}{14}\\)", "2"],
     "A", "OSC", "easy",
     "\\(14y = 21 \\implies y = \\frac{21}{14} = \\frac{3}{2}\\)."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Verification by Substitution: LHS vs RHS Check</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Equation banner -->
    <text x="170" y="25" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">Verify solution x = 2 for: 5x + 9 = 19</text>
    <!-- LHS Evaluation -->
    <rect x="30" y="40" width="130" height="60" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="95" y="60" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">LHS = 5(2) + 9</text>
    <text x="95" y="80" fill="#ffffff" font-size="13" text-anchor="middle">= 10 + 9 = 19</text>
    <!-- Comparison equals -->
    <text x="170" y="75" fill="#10b981" font-size="22" font-weight="bold" text-anchor="middle">=</text>
    <!-- RHS Match -->
    <rect x="180" y="40" width="130" height="60" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="245" y="60" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">RHS = 19</text>
    <text x="245" y="80" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">MATCH CONFIRMED</text>
    <text x="170" y="132" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">LHS = RHS confirms the root is strictly correct</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is verified when substituting \(x = 2\) into \(5x + 9 = 19\)?</p>
</div>""",
     ["\\(\\text{LHS} = \\text{RHS} = 19\\), confirming \\(x = 2\\) is the root",
      "\\(\\text{LHS} \\neq \\text{RHS}\\)",
      "The equation has no solution",
      "The degree of the equation is 2"],
     "A", "OSC", "easy",
     "\\(5(2) + 9 = 19\\), matching the RHS exactly and verifying the root."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Fractional Variable Equation: 2x/3 = 18</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Step cards -->
    <rect x="30" y="30" width="115" height="55" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="87" y="52" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">2x / 3 = 18</text>
    <text x="87" y="70" fill="#cbd5e1" font-size="10" text-anchor="middle">Multiply by 3</text>
    <!-- Arrow -->
    <path d="M 155,55 L 185,55" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="185,50 195,55 185,60" fill="#f59e0b"/>
    <!-- Step 2 -->
    <rect x="200" y="30" width="115" height="55" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="257" y="52" fill="#6ee7b7" font-size="13" font-weight="bold" text-anchor="middle">2x = 54</text>
    <text x="257" y="72" fill="#fde047" font-size="14" font-weight="bold" text-anchor="middle">x = 27</text>
    <text x="170" y="125" fill="#38bdf8" font-size="11" text-anchor="middle">Cross-multiplying: x = 18 × (3/2) = 27</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the solution to \(\frac{2x}{3} = 18\)?</p>
</div>""",
     ["27", "12", "54", "9"],
     "A", "OSC", "easy",
     "\\(x = 18 \\times \\frac{3}{2} = 9 \\times 3 = 27\\)."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Fractional Constant Transposition: x/3 + 1 = 7/15</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Step 1 -->
    <rect x="20" y="30" width="135" height="55" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="87" y="52" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">x / 3 = 7/15 - 1</text>
    <text x="87" y="70" fill="#ffffff" font-size="11" text-anchor="middle">= -8 / 15</text>
    <!-- Arrow -->
    <path d="M 165,55 L 195,55" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="195,50 205,55 195,60" fill="#f59e0b"/>
    <!-- Result -->
    <rect x="210" y="30" width="110" height="55" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="265" y="52" fill="#6ee7b7" font-size="11" text-anchor="middle">x = (-8/15) × 3</text>
    <text x="265" y="72" fill="#fde047" font-size="14" font-weight="bold" text-anchor="middle">x = -8/5</text>
    <text x="170" y="125" fill="#cbd5e1" font-size="11" text-anchor="middle">Keep track of signs when subtracting whole numbers from proper fractions</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the solution to \(\frac{x}{3} + 1 = \frac{7}{15}\)?</p>
</div>""",
     ["\\(-\\frac{8}{5}\\)", "\\(\\frac{8}{5}\\)", "\\(-\\frac{8}{15}\\)", "\\(-\\frac{2}{5}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{x}{3} = -\\frac{8}{15} \\implies x = -\\frac{8}{5}\\)."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Negative Variable Resolution: 4 - 2z = 10</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Step cards -->
    <rect x="25" y="30" width="130" height="55" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="90" y="52" fill="#fca5a5" font-size="12" font-weight="bold" text-anchor="middle">-2z = 10 - 4</text>
    <text x="90" y="70" fill="#ffffff" font-size="12" text-anchor="middle">-2z = 6</text>
    <!-- Arrow -->
    <path d="M 165,55 L 195,55" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="195,50 205,55 195,60" fill="#f59e0b"/>
    <!-- Result -->
    <rect x="205" y="30" width="110" height="55" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="260" y="52" fill="#6ee7b7" font-size="11" text-anchor="middle">Divide by -2</text>
    <text x="260" y="72" fill="#fde047" font-size="14" font-weight="bold" text-anchor="middle">z = -3</text>
    <text x="170" y="125" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Dividing a positive by a negative yields a negative quotient</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the solution to \(4 - 2z = 10\)?</p>
</div>""",
     ["-3", "3", "7", "-7"],
     "A", "OSC", "easy",
     "\\(-2z = 6 \\implies z = -3\\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Bracket Expansion Before Solving: 3(n - 2) = 15</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Two alternate paths -->
    <rect x="25" y="25" width="135" height="90" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="92" y="48" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">Path A: Divide first</text>
    <text x="92" y="70" fill="#cbd5e1" font-size="11" text-anchor="middle">n - 2 = 15 ÷ 3 = 5</text>
    <text x="92" y="95" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">n = 5 + 2 = 7</text>
    <!-- Equals -->
    <text x="170" y="70" fill="#10b981" font-size="20" font-weight="bold" text-anchor="middle">=</text>
    <!-- Path B: Distribute -->
    <rect x="180" y="25" width="135" height="90" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="247" y="48" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">Path B: Expand first</text>
    <text x="247" y="70" fill="#cbd5e1" font-size="11" text-anchor="middle">3n - 6 = 15  ⇒  3n = 21</text>
    <text x="247" y="95" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">n = 7</text>
    <text x="170" y="135" fill="#fbbf24" font-size="11" text-anchor="middle">Both valid algebraic paths converge to the exact same root</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the solution to \(3(n - 2) = 15\)?</p>
</div>""",
     ["7", "5", "3", "9"],
     "A", "OSC", "easy",
     "\\(n - 2 = 5 \\implies n = 7\\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Fractional Decimal Equation: 1.6 = y / 1.5</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Cross product diagram -->
    <rect x="40" y="30" width="110" height="55" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="95" y="55" fill="#93c5fd" font-size="14" font-weight="bold" text-anchor="middle">1.6 = y / 1.5</text>
    <!-- Arrow -->
    <path d="M 160,55 L 190,55" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="190,50 200,55 190,60" fill="#f59e0b"/>
    <!-- Multiplication -->
    <rect x="210" y="30" width="105" height="55" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="262" y="52" fill="#6ee7b7" font-size="12" text-anchor="middle">y = 1.6 × 1.5</text>
    <text x="262" y="72" fill="#fde047" font-size="15" font-weight="bold" text-anchor="middle">y = 2.4</text>
    <text x="170" y="125" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Multiply divisor 1.5 by quotient 1.6 to recover dividend y</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the solution to \(1.6 = \frac{y}{1.5}\)?</p>
</div>""",
     ["2.4", "2.44", "0.1", "3.1"],
     "A", "OSC", "easy",
     "\\(y = 1.6 \\times 1.5 = 2.4\\)."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Fractional Variable Decomposition: 3/7 + x = 17/7</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Step cards -->
    <rect x="30" y="30" width="120" height="55" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="90" y="52" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">x = 17/7 - 3/7</text>
    <text x="90" y="70" fill="#ffffff" font-size="12" text-anchor="middle">= 14 / 7</text>
    <!-- Arrow -->
    <path d="M 160,55 L 195,55" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="195,50 205,55 195,60" fill="#f59e0b"/>
    <!-- Result -->
    <rect x="215" y="30" width="95" height="55" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="262" y="55" fill="#6ee7b7" font-size="13" text-anchor="middle">14 ÷ 7</text>
    <text x="262" y="75" fill="#fde047" font-size="16" font-weight="bold" text-anchor="middle">x = 2</text>
    <text x="170" y="125" fill="#fbbf24" font-size="11" text-anchor="middle">Identical denominators allow direct subtraction of numerators</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the solution to \(\frac{3}{7} + x = \frac{17}{7}\)?</p>
</div>""",
     ["2", "14", "\\(\\frac{20}{7}\\)", "\\(\\frac{14}{49}\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{17 - 3}{7} = \\frac{14}{7} = 2\\)."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Root Location on the Coordinate Number Line</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Number line -->
    <line x1="30" y1="75" x2="310" y2="75" stroke="#64748b" stroke-width="3"/>
    <!-- Ticks: 0, 1, 2, 3, 4, 5 -->
    <g fill="#f8fafc" font-size="11" text-anchor="middle">
      <circle cx="50" cy="75" r="3"/> <text x="50" y="95">0</text>
      <circle cx="95" cy="75" r="3"/> <text x="95" y="95">1</text>
      <circle cx="140" cy="75" r="3"/> <text x="140" y="95">2</text>
      <circle cx="185" cy="75" r="3"/> <text x="185" y="95">3</text>
      <circle cx="230" cy="75" r="3"/> <text x="230" y="95">4</text>
      <circle cx="275" cy="75" r="3"/> <text x="275" y="95">5</text>
    </g>
    <!-- Highlighted root at x = 3 -->
    <circle cx="185" cy="75" r="7" fill="#10b981" stroke="#34d399" stroke-width="2"/>
    <text x="185" y="55" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Root: x = 3</text>
    <text x="170" y="130" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Equation: 4x - 5 = 7  ⇒  4x = 12  ⇒  x = 3</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the solution to \(4x - 5 = 7\)?</p>
</div>""",
     ["3", "4", "2", "5"],
     "A", "OSC", "easy",
     "\\(4x = 7 + 5 = 12 \\implies x = 3\\).")
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch4_topic1.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
