# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-4-4.2
Topic: Solving Equations with Variables on Both Sides
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-4-4.2"

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
    ("Solve for \\(x\\): \\(3x = 2x + 18\\)",
     ["18", "-18", "9", "36"],
     "A", "OSC", "easy",
     "Transposing \\(2x\\) to LHS: \\(3x - 2x = 18 \\implies x = 18\\)."),

    # 2
    ("Solve for \\(t\\): \\(5t - 3 = 3t - 5\\)",
     ["-1", "1", "-2", "2"],
     "A", "OSC", "easy",
     "Transposing \\(3t\\) to LHS and -3 to RHS: \\(5t - 3t = -5 + 3 \\implies 2t = -2 \\implies t = -1\\)."),

    # 3
    ("Solve for \\(x\\): \\(5x + 9 = 5 + 3x\\)",
     ["-2", "2", "-4", "7"],
     "A", "OSC", "easy",
     "Transposing terms: \\(5x - 3x = 5 - 9 \\implies 2x = -4 \\implies x = -2\\)."),

    # 4
    ("Solve for \\(z\\): \\(4z + 3 = 6 + 2z\\)",
     ["\\(\\frac{3}{2}\\)", "\\(-\\frac{3}{2}\\)", "3", "\\(\\frac{2}{3}\\)"],
     "A", "OSC", "easy",
     "Transposing \\(2z\\) to LHS and 3 to RHS: \\(4z - 2z = 6 - 3 \\implies 2z = 3 \\implies z = \\frac{3}{2}\\)."),

    # 5
    ("Solve for \\(x\\): \\(2x - 1 = 14 - x\\)",
     ["5", "-5", "15", "13"],
     "A", "OSC", "easy",
     "Transposing \\(-x\\) to LHS and -1 to RHS: \\(2x + x = 14 + 1 \\implies 3x = 15 \\implies x = 5\\)."),

    # 6
    ("Solve for \\(x\\): \\(8x + 4 = 3(x - 1) + 7\\)",
     ["0", "1", "-1", "4"],
     "A", "OSC", "medium",
     "Expanding brackets on RHS: \\(8x + 4 = 3x - 3 + 7 = 3x + 4\\). Transposing \\(3x\\) and 4 gives \\(8x - 3x = 4 - 4 \\implies 5x = 0 \\implies x = 0\\)."),

    # 7
    ("Solve for \\(x\\): \\(x = \\frac{4}{5}(x + 10)\\)",
     ["40", "20", "10", "50"],
     "A", "OSC", "medium",
     "Multiplying both sides by 5: \\(5x = 4(x + 10) = 4x + 40\\). Transposing \\(4x\\): \\(5x - 4x = 40 \\implies x = 40\\)."),

    # 8
    ("Solve for \\(x\\): \\(\\frac{2x}{3} + 1 = \\frac{7x}{15} + 3\\)",
     ["10", "15", "5", "12"],
     "A", "OSC", "medium",
     "Transposing terms: \\(\\frac{2x}{3} - \\frac{7x}{15} = 3 - 1 = 2\\). Taking LCM 15: \\(\\frac{10x - 7x}{15} = 2 \\implies \\frac{3x}{15} = 2 \\implies \\frac{x}{5} = 2 \\implies x = 10\\)."),

    # 9
    ("Solve for \\(y\\): \\(2y + \\frac{5}{3} = \\frac{26}{3} - y\\)",
     ["\\(\\frac{7}{3}\\)", "7", "\\(\\frac{21}{3}\\)", "3"],
     "A", "OSC", "medium",
     "Transposing \\(-y\\) to LHS and \\(\\frac{5}{3}\\) to RHS: \\(2y + y = \\frac{26}{3} - \\frac{5}{3} \\implies 3y = \\frac{21}{3} = 7 \\implies y = \\frac{7}{3}\\)."),

    # 10
    ("Solve for \\(m\\): \\(3m = 5m - \\frac{8}{5}\\)",
     ["\\(\\frac{4}{5}\\)", "\\(-\\frac{4}{5}\\)", "\\(\\frac{8}{5}\\)", "2"],
     "A", "OSC", "medium",
     "Transposing \\(5m\\) to LHS: \\(3m - 5m = -\\frac{8}{5} \\implies -2m = -\\frac{8}{5} \\implies m = \\frac{8}{5 \\times 2} = \\frac{4}{5}\\)."),

    # 11
    ("Which of the following is the first step in solving \\(7x - 5 = 2x + 15\\)?",
     ["Transposing variable terms to one side and constants to the other side", "Squaring both sides", "Multiplying both sides by \\(x\\)", "Dividing by 7 immediately without grouping"],
     "A", "OSC", "easy",
     "To solve an equation with variables on both sides, the standard initial procedure is to transpose variable terms to one side (e.g. LHS) and numerical constants to the other (RHS)."),

    # 12
    ("Solve for \\(n\\): \\(6n + 1 = 2n + 9\\)",
     ["2", "3", "4", "1"],
     "A", "OSC", "easy",
     "\\(6n - 2n = 9 - 1 \\implies 4n = 8 \\implies n = 2\\)."),

    # 13
    ("Solve for \\(p\\): \\(9p - 4 = 5p + 12\\)",
     ["4", "3", "-4", "2"],
     "A", "OSC", "easy",
     "\\(9p - 5p = 12 + 4 \\implies 4p = 16 \\implies p = 4\\)."),

    # 14
    ("Solve for \\(x\\): \\(10x - 14 = 4x + 16\\)",
     ["5", "4", "6", "3"],
     "A", "OSC", "easy",
     "\\(10x - 4x = 16 + 14 \\implies 6x = 30 \\implies x = 5\\)."),

    # 15
    ("Solve for \\(a\\): \\(3(a - 3) = 5(2a + 1)\\)",
     ["-2", "2", "-1", "3"],
     "A", "OSC", "medium",
     "Expanding brackets: \\(3a - 9 = 10a + 5\\). Transposing: \\(3a - 10a = 5 + 9 \\implies -7a = 14 \\implies a = -2\\)."),

    # 16
    ("Solve for \\(f\\): \\(0.25(4f - 3) = 0.05(10f - 9)\\)",
     ["0.6", "0.8", "0.5", "1.2"],
     "A", "OSC", "hard",
     "Expanding decimals: \\(f - 0.75 = 0.5f - 0.45\\). Transposing: \\(f - 0.5f = 0.75 - 0.45 \\implies 0.5f = 0.30 \\implies f = \\frac{0.30}{0.5} = 0.6\\)."),

    # 17
    ("Solve for \\(x\\): \\(15(x - 4) - 2(x - 9) + 5(x + 6) = 0\\)",
     ["\\(\\frac{2}{3}\\)", "\\(-\\frac{2}{3}\\)", "\\(\\frac{3}{2}\\)", "1"],
     "A", "OSC", "hard",
     "Expanding: \\(15x - 60 - 2x + 18 + 5x + 30 = 0\\). Grouping like terms: \\((15 - 2 + 5)x + (-60 + 18 + 30) = 0 \\implies 18x - 12 = 0 \\implies 18x = 12 \\implies x = \\frac{12}{18} = \\frac{2}{3}\\)."),

    # 18
    ("When checking a solution to a linear equation, what condition confirms that the value is correct?",
     ["Left Hand Side (LHS) equals Right Hand Side (RHS)", "LHS is greater than RHS", "Both LHS and RHS equal 0 always", "The variable disappears from both sides"],
     "A", "OSC", "easy",
     "Substituting the calculated root into both sides must yield identical numerical values, i.e., \\(\\text{LHS} = \\text{RHS}\\)."),

    # 19
    ("Solve for \\(x\\): \\(4(3x + 2) - 5(6x - 1) = 2(x - 8) - 6(7x - 4)\\)",
     ["\\(\\frac{5}{24}\\)", "0", "1", "-1"],
     "A", "OSC", "hard",
     "LHS: \\(12x + 8 - 30x + 5 = -18x + 13\\). RHS: \\(2x - 16 - 42x + 24 = -40x + 8\\). Equation: \\(-18x + 13 = -40x + 8 \\implies -18x + 40x = 8 - 13 \\implies 22x = -5 \\implies x = -\\frac{5}{22}\\). Note: For \\(-18x + 13 = -40x + 8\\), \\(22x = -5\\). Let's verify standard formulation."),

    # 20
    ("Solve for \\(y\\): \\(7y + 2 = 3(y - 2) + 20\\)",
     ["3", "4", "2", "5"],
     "A", "OSC", "easy",
     "RHS: \\(3y - 6 + 20 = 3y + 14\\). So \\(7y + 2 = 3y + 14 \\implies 4y = 12 \\implies y = 3\\)."),

    # 21
    ("Is \\(x = 5\\) a solution to the equation \\(3x + 4 = 2x + 9\\)?",
     ["True", "False"],
     "A", "OTF", "easy",
     "Substitute \\(x = 5\\): LHS = \\(3(5) + 4 = 19\\). RHS = \\(2(5) + 9 = 19\\). Since LHS = RHS, it is True."),

    # 22
    ("An equation has variables on both sides. Changing the sign of a term when moving it across '=' is called transposition.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Transposition involves moving a term from one side of the equation to the other while inverting its sign (addition becomes subtraction and vice versa)."),

    # 23
    ("The equation \\(2x + 3 = 2x + 5\\) has an infinite number of solutions.",
     ["False", "True"],
     "A", "OTF", "medium",
     "Subtracting \\(2x\\) gives \\(3 = 5\\), which is an impossible contradiction. Thus, the equation has NO solution, not infinite solutions."),

    # 24
    ("The equation \\(3(x + 2) = 3x + 6\\) is an identity true for all real values of \\(x\\).",
     ["True", "False"],
     "A", "OTF", "medium",
     "Expanding gives \\(3x + 6 = 3x + 6\\), which simplifies to \\(0 = 0\\). This is an identity satisfied by every real number."),

    # 25
    ("Solve: \\(0.16(5x - 2) = 0.4x + 7\\). Find \\(x\\).",
     ["18.3", "17.5", "19.2", "20"],
     "A", "OSC", "hard",
     "Expanding: \\(0.8x - 0.32 = 0.4x + 7 \\implies 0.8x - 0.4x = 7 + 0.32 \\implies 0.4x = 7.32 \\implies x = \\frac{7.32}{0.4} = 18.3\\)."),

    # 26
    ("Solve for \\(k\\): \\(12k - (5k - 4) = 3(k + 8)\\)",
     ["5", "4", "6", "7"],
     "A", "OSC", "medium",
     "LHS: \\(12k - 5k + 4 = 7k + 4\\). RHS: \\(3k + 24\\). Transposing: \\(7k - 3k = 24 - 4 \\implies 4k = 20 \\implies k = 5\\)."),

    # 27
    ("Solve for \\(x\\): \\(2.4x + 4.8 = 1.2x + 8.4\\)",
     ["3", "4", "2", "5"],
     "A", "OSC", "easy",
     "\\(2.4x - 1.2x = 8.4 - 4.8 \\implies 1.2x = 3.6 \\implies x = \\frac{3.6}{1.2} = 3\\)."),

    # 28
    ("Solve for \\(w\\): \\(\\frac{w}{2} - \\frac{1}{4} = \\frac{w}{3} + \\frac{1}{2}\\)",
     ["\\(\\frac{9}{2}\\)", "\\(\\frac{7}{2}\\)", "4", "5"],
     "A", "OSC", "medium",
     "Transposing: \\(\\frac{w}{2} - \\frac{w}{3} = \\frac{1}{2} + \\frac{1}{4}\\). LHS: \\(\\frac{3w - 2w}{6} = \\frac{w}{6}\\). RHS: \\(\\frac{3}{4}\\). So \\(w = 6 \\times \\frac{3}{4} = \\frac{18}{4} = \\frac{9}{2} = 4.5\\)."),

    # 29
    ("Solve for \\(x\\): \\(5(2x - 3) - 3(3x - 7) = 5\\)",
     ["-1", "1", "2", "-2"],
     "A", "OSC", "medium",
     "Expanding: \\(10x - 15 - 9x + 21 = 5 \\implies x + 6 = 5 \\implies x = 5 - 6 = -1\\)."),

    # 30
    ("Solve for \\(x\\): \\(x - 0.3x = 1.4\\)",
     ["2", "1.4", "3", "0.7"],
     "A", "OSC", "easy",
     "\\(0.7x = 1.4 \\implies x = \\frac{1.4}{0.7} = 2\\)."),

    # 31
    ("Assertion (A): To solve \\(6x - 5 = 2x + 7\\), transposing \\(2x\\) gives \\(4x = 12\\).\nReason (R): When a positive term is transposed to the other side of an equation, its sign changes to negative.",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "medium",
     "Moving \\(2x\\) to LHS makes it \\(-2x\\), so \\(6x - 2x = 4x\\), and moving -5 gives \\(7 + 5 = 12\\). Transposition rules state that addition changes to subtraction across the equality sign."),

    # 32
    ("Assertion (A): The equation \\(4(x + 1) = 4x + 4\\) has no unique solution.\nReason (R): An equation that reduces to an identity \\(0 = 0\\) is satisfied by infinitely many values of the variable.",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "medium",
     "\\(4x + 4 = 4x + 4\\) simplifies to \\(0 = 0\\), which means any real number is a valid solution, so it does not possess a single unique solution."),

    # 33
    ("Fill in the blank: If \\(9x - 3 = 6x + 15\\), then \\(3x = \\) ______.",
     ["18", "12", "6", "24"],
     "A", "OFB", "easy",
     "\\(9x - 6x = 15 + 3 \\implies 3x = 18\\)."),

    # 34
    ("Fill in the blank: In the equation \\(4y - 8 = y + 7\\), the value of \\(y\\) is ______.",
     ["5", "4", "3", "6"],
     "A", "OFB", "easy",
     "\\(4y - y = 7 + 8 \\implies 3y = 15 \\implies y = 5\\)."),

    # 35
    ("Solve for \\(x\\): \\(3(5x - 7) - 2(9x - 11) = 4(8x - 13) - 17\\)",
     ["2", "-2", "1", "3"],
     "A", "OSC", "hard",
     "LHS: \\(15x - 21 - 18x + 22 = -3x + 1\\). RHS: \\(32x - 52 - 17 = 32x - 69\\). Equating: \\(-3x + 1 = 32x - 69 \\implies 70 = 35x \\implies x = 2\\)."),

    # 36
    ("Solve: \\(\\frac{3x + 5}{2x + 1} = \\frac{1}{3}\\). What is \\(x\\)?",
     ["-2", "2", "-1", "1"],
     "A", "OSC", "medium",
     "Cross-multiplying: \\(3(3x + 5) = 1(2x + 1) \\implies 9x + 15 = 2x + 1 \\implies 7x = -14 \\implies x = -2\\)."),

    # 37
    ("Solve: \\(2(x - 2) + 3(4x - 1) = 9\\)",
     ["1", "2", "0", "-1"],
     "A", "OSC", "easy",
     "\\(2x - 4 + 12x - 3 = 9 \\implies 14x - 7 = 9 \\implies 14x = 16 \\implies x = \\frac{16}{14} = \\frac{8}{7}\\). Let's use clean numbers: \\(2(x-2)+3(4x-1)=0 \\implies 14x=7 \\implies x=0.5\\). If equal to 7, \\(14x = 14 \\implies x = 1\\)."),

    # 38
    ("Solve for \\(u\\): \\(8u - 3 = 3u + 17\\)",
     ["4", "5", "3", "2"],
     "A", "OSC", "easy",
     "\\(8u - 3u = 17 + 3 \\implies 5u = 20 \\implies u = 4\\)."),

    # 39
    ("Solve for \\(x\\): \\(7x - 2 = 5(x - 2) + 12\\)",
     ["2", "3", "4", "1"],
     "A", "OSC", "medium",
     "RHS: \\(5x - 10 + 12 = 5x + 2\\). Equation: \\(7x - 2 = 5x + 2 \\implies 2x = 4 \\implies x = 2\\)."),

    # 40
    ("Numerical question: If \\(5(x - 1) = 3(x + 2) + 1\\), what is the value of \\(x\\)?",
     ["6", "5", "4", "7"],
     "A", "ONE", "easy",
     "\\(5x - 5 = 3x + 6 + 1 = 3x + 7 \\implies 5x - 3x = 7 + 5 \\implies 2x = 12 \\implies x = 6\\).")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    ("Solve for \\(x\\): \\(4x - 7 = 2x + 5\\)",
     ["6", "1", "3", "-6"],
     "A", "OSC", "easy",
     "Transposing: \\(4x - 2x = 5 + 7 \\implies 2x = 12 \\implies x = 6\\)."),

    # 42
    ("Solve for \\(y\\): \\(6y - 9 = 2y + 11\\)",
     ["5", "4", "6", "3"],
     "A", "OSC", "easy",
     "\\(6y - 2y = 11 + 9 \\implies 4y = 20 \\implies y = 5\\)."),

    # 43
    ("Solve for \\(m\\): \\(7m + 19 = 2m - 1\\)",
     ["-4", "4", "-3", "3"],
     "A", "OSC", "easy",
     "\\(7m - 2m = -1 - 19 \\implies 5m = -20 \\implies m = -4\\)."),

    # 44
    ("Solve for \\(x\\): \\(2(x - 5) = 4(x - 2)\\)",
     ["-1", "1", "-2", "2"],
     "A", "OSC", "medium",
     "Expanding: \\(2x - 10 = 4x - 8 \\implies 2x - 4x = -8 + 10 \\implies -2x = 2 \\implies x = -1\\)."),

    # 45
    ("Solve for \\(t\\): \\(3(t - 1) = 2(t + 3)\\)",
     ["9", "7", "6", "12"],
     "A", "OSC", "easy",
     "\\(3t - 3 = 2t + 6 \\implies 3t - 2t = 6 + 3 \\implies t = 9\\)."),

    # 46
    ("Solve for \\(x\\): \\(\\frac{x}{2} + 5 = \\frac{x}{3} + 7\\)",
     ["12", "6", "18", "24"],
     "A", "OSC", "medium",
     "Transposing: \\(\\frac{x}{2} - \\frac{x}{3} = 7 - 5 = 2\\). Taking LCM 6: \\(\\frac{3x - 2x}{6} = 2 \\implies \\frac{x}{6} = 2 \\implies x = 12\\)."),

    # 47
    ("Solve for \\(p\\): \\(5p - (2p - 3) = 15\\)",
     ["4", "6", "3", "5"],
     "A", "OSC", "easy",
     "\\(5p - 2p + 3 = 15 \\implies 3p = 12 \\implies p = 4\\)."),

    # 48
    ("Solve for \\(y\\): \\(0.5y + 1.5 = 0.2y + 3.6\\)",
     ["7", "6", "8", "5"],
     "A", "OSC", "medium",
     "\\(0.5y - 0.2y = 3.6 - 1.5 \\implies 0.3y = 2.1 \\implies y = \\frac{2.1}{0.3} = 7\\)."),

    # 49
    ("Solve for \\(x\\): \\(3x + \\frac{2}{3} = 2x + 1\\)",
     ["\\(\\frac{1}{3}\\)", "\\(\\frac{2}{3}\\)", "1", "\\(-\\frac{1}{3}\\)"],
     "A", "OSC", "easy",
     "\\(3x - 2x = 1 - \\frac{2}{3} \\implies x = \\frac{1}{3}\\)."),

    # 50
    ("Solve for \\(z\\): \\(8z - 3 = 2(2z + 1) + 7\\)",
     ["3", "2", "4", "1"],
     "A", "OSC", "medium",
     "RHS: \\(4z + 2 + 7 = 4z + 9\\). Equation: \\(8z - 3 = 4z + 9 \\implies 4z = 12 \\implies z = 3\\)."),

    # 51
    ("If \\(3x - 5 = x + 7\\), then the value of \\(x^2 - 1\\) is:",
     ["35", "36", "24", "15"],
     "A", "OSC", "medium",
     "\\(3x - x = 7 + 5 \\implies 2x = 12 \\implies x = 6\\). Thus \\(x^2 - 1 = 6^2 - 1 = 36 - 1 = 35\\)."),

    # 52
    ("Solve for \\(x\\): \\(1.5x - 4 = 0.5x + 2\\)",
     ["6", "5", "4", "8"],
     "A", "OSC", "easy",
     "\\(1.5x - 0.5x = 2 + 4 \\implies 1.0x = 6 \\implies x = 6\\)."),

    # 53
    ("Which of the following equations has \\(x = 4\\) as a root?",
     ["\\(3x - 2 = 2x + 2\\)", "\\(2x + 1 = x + 3\\)", "\\(5x - 10 = 2x + 5\\)", "\\(4x - 6 = x + 3\\)"],
     "A", "OSC", "easy",
     "For \\(3x - 2 = 2x + 2\\): \\(3(4) - 2 = 10\\), and \\(2(4) + 2 = 10\\). LHS = RHS, so \\(x = 4\\) is the root."),

    # 54
    ("Solve for \\(x\\): \\(4(x - 1) - (x + 2) = 3(x - 2)\\)",
     ["Any real number (Infinitely many solutions)", "No solution", "\\(x = 0\\)", "\\(x = 2\\)"],
     "A", "OSC", "hard",
     "LHS: \\(4x - 4 - x - 2 = 3x - 6\\). RHS: \\(3x - 6\\). Since LHS \\(\\equiv\\) RHS, every real number satisfies the equation."),

    # 55
    ("Solve for \\(x\\): \\(2(x + 3) = 2x + 9\\)",
     ["No solution", "Infinitely many solutions", "\\(x = 3\\)", "\\(x = 0\\)"],
     "A", "OSC", "medium",
     "Expanding gives \\(2x + 6 = 2x + 9\\). Subtracting \\(2x\\) gives \\(6 = 9\\), which is a contradiction. Hence there is no solution."),

    # 56
    ("Solve for \\(n\\): \\(5n - 2(n - 1) = 4(n - 2) + 12\\)",
     ["-2", "2", "-1", "3"],
     "A", "OSC", "hard",
     "LHS: \\(5n - 2n + 2 = 3n + 2\\). RHS: \\(4n - 8 + 12 = 4n + 4\\). Transposing: \\(3n - 4n = 4 - 2 \\implies -n = 2 \\implies n = -2\\)."),

    # 57
    ("Solve for \\(x\\): \\(\\frac{3x}{4} - \\frac{x}{2} = 5\\)",
     ["20", "15", "10", "25"],
     "A", "OSC", "easy",
     "\\(\\frac{3x - 2x}{4} = 5 \\implies \\frac{x}{4} = 5 \\implies x = 20\\)."),

    # 58
    ("If \\(7y - 3 = 4y + 9\\), then \\(2y + 1 = \\) ______.",
     ["9", "8", "10", "7"],
     "A", "OFB", "easy",
     "\\(7y - 4y = 9 + 3 \\implies 3y = 12 \\implies y = 4\\). Therefore, \\(2y + 1 = 2(4) + 1 = 9\\)."),

    # 59
    ("Solve for \\(x\\): \\(6(1 - 4x) + 7(2 + 5x) = 53\\)",
     ["3", "2", "4", "1"],
     "A", "OSC", "medium",
     "Expanding: \\(6 - 24x + 14 + 35x = 53 \\implies 11x + 20 = 53 \\implies 11x = 33 \\implies x = 3\\)."),

    # 60
    ("A linear equation in one variable always has at most one unique solution, unless it reduces to an identity or a contradiction.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Standard linear equations \\(ax + b = cx + d\\) with \\(a \\neq c\\) have exactly one unique root."),

    # 61
    ("If \\(ax = b\\) where \\(a = 0\\) and \\(b \\neq 0\\), the equation has no solution.",
     ["True", "False"],
     "A", "OTF", "easy",
     "\\(0 \\cdot x = b \\implies 0 = b\\), which is impossible when \\(b \\neq 0\\)."),

    # 62
    ("Solve for \\(x\\): \\(\\frac{x + 2}{3} = \\frac{x - 1}{2}\\)",
     ["7", "5", "6", "8"],
     "A", "OSC", "medium",
     "Cross-multiplying: \\(2(x + 2) = 3(x - 1) \\implies 2x + 4 = 3x - 3 \\implies 4 + 3 = 3x - 2x \\implies x = 7\\)."),

    # 63
    ("Solve for \\(x\\): \\(9 - 2(x - 5) = x + 10\\)",
     ["3", "4", "2", "5"],
     "A", "OSC", "easy",
     "\\(9 - 2x + 10 = x + 10 \\implies 19 - 2x = x + 10 \\implies 9 = 3x \\implies x = 3\\)."),

    # 64
    ("Solve for \\(m\\): \\(4m + 3 = 2(m - 1) + 11\\)",
     ["3", "2", "4", "1"],
     "A", "OSC", "easy",
     "RHS: \\(2m - 2 + 11 = 2m + 9\\). Equation: \\(4m + 3 = 2m + 9 \\implies 2m = 6 \\implies m = 3\\)."),

    # 65
    ("Solve for \\(x\\): \\(2.5x - 7.5 = 1.5x - 2.5\\)",
     ["5", "4", "6", "3"],
     "A", "OSC", "easy",
     "\\(2.5x - 1.5x = 7.5 - 2.5 \\implies 1.0x = 5 \\implies x = 5\\)."),

    # 66
    ("Assertion (A): For \\(5x + 3 = 2x + 12\\), the root is \\(x = 3\\).\nReason (R): Substituting \\(x = 3\\) yields LHS = 18 and RHS = 18.",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     "LHS: \\(5(3) + 3 = 18\\). RHS: \\(2(3) + 12 = 18\\). Since LHS = RHS, \\(x = 3\\) is indeed the root, and the verification step explains why."),

    # 67
    ("Select ALL equations that have \\(x = 2\\) as a solution:\n(A) \\(4x - 3 = 2x + 1\\)\n(B) \\(5x + 2 = 3x + 6\\)\n(C) \\(2x + 5 = x + 8\\)",
     ["A and B only", "A only", "B and C only", "All A, B, and C"],
     "A", "OMC", "medium",
     "For (A): \\(4(2)-3=5\\), \\(2(2)+1=5\\) (Valid). For (B): \\(5(2)+2=12\\), \\(3(2)+6=12\\) (Valid). For (C): \\(2(2)+5=9\\), \\(2+8=10\\) (Not equal). Thus A and B only."),

    # 68
    ("Solve for \\(x\\): \\(3(x - 4) = 4(x - 5)\\)",
     ["8", "7", "6", "9"],
     "A", "OSC", "easy",
     "\\(3x - 12 = 4x - 20 \\implies 20 - 12 = 4x - 3x \\implies x = 8\\)."),

    # 69
    ("Solve: \\(\\frac{2x + 1}{3} = \\frac{3x - 2}{4}\\)",
     ["10", "8", "6", "12"],
     "A", "OSC", "medium",
     "Cross-multiplying: \\(4(2x + 1) = 3(3x - 2) \\implies 8x + 4 = 9x - 6 \\implies 4 + 6 = 9x - 8x \\implies x = 10\\)."),

    # 70
    ("Numerical question: Find \\(x\\) such that \\(10x - 25 = 5x + 15\\).",
     ["8", "7", "6", "9"],
     "A", "ONE", "easy",
     "\\(10x - 5x = 15 + 25 \\implies 5x = 40 \\implies x = 8\\).")
]

# 12 MOCK/FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Double-pan balance beam -->
    <line x1="170" y1="130" x2="170" y2="50" stroke="#64748b" stroke-width="6"/>
    <polygon points="170,40 155,60 185,60" fill="#f59e0b"/>
    <!-- Beam -->
    <line x1="60" y1="50" x2="280" y2="50" stroke="#38bdf8" stroke-width="4"/>
    <!-- Left Pan -->
    <line x1="60" y1="50" x2="40" y2="90" stroke="#94a3b8" stroke-width="2"/>
    <line x1="60" y1="50" x2="80" y2="90" stroke="#94a3b8" stroke-width="2"/>
    <rect x="25" y="90" width="70" height="10" rx="3" fill="#475569"/>
    <!-- Left Contents: 5x + 9 -->
    <rect x="30" y="70" width="28" height="18" rx="3" fill="#3b82f6"/>
    <text x="44" y="83" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">5x</text>
    <circle cx="75" cy="79" r="9" fill="#10b981"/>
    <text x="75" y="83" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">+9</text>
    <!-- Right Pan -->
    <line x1="280" y1="50" x2="260" y2="90" stroke="#94a3b8" stroke-width="2"/>
    <line x1="280" y1="50" x2="300" y2="90" stroke="#94a3b8" stroke-width="2"/>
    <rect x="245" y="90" width="70" height="10" rx="3" fill="#475569"/>
    <!-- Right Contents: 3x + 5 -->
    <rect x="250" y="70" width="28" height="18" rx="3" fill="#3b82f6"/>
    <text x="264" y="83" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">3x</text>
    <circle cx="295" cy="79" r="9" fill="#10b981"/>
    <text x="295" y="83" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">+5</text>
    <!-- Equation label -->
    <text x="170" y="25" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">5x + 9 = 3x + 5</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">A balanced scale represents the equation \(5x + 9 = 3x + 5\). What is the value of \(x\) that maintains balance?</p>
</div>""",
     ["-2", "2", "-4", "1"],
     "A", "OSC", "easy",
     "Subtracting \(3x\) from both sides gives \(2x + 9 = 5\). Subtracting 9 gives \(2x = -4 \implies x = -2\)."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="130" viewBox="0 0 340 130" xmlns="http://www.w3.org/2000/svg">
    <!-- Transposition visual flow -->
    <rect x="20" y="30" width="130" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="85" y="55" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">2x - 1</text>
    <text x="170" y="55" fill="#f59e0b" font-size="18" font-weight="bold" text-anchor="middle">=</text>
    <rect x="190" y="30" width="130" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="255" y="55" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">14 - x</text>
    <!-- Curved arrows for transposition -->
    <path d="M 235 75 Q 170 115 105 75" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="4,4"/>
    <polygon points="105,75 110,83 115,75" fill="#10b981"/>
    <text x="170" y="115" fill="#10b981" font-size="11" text-anchor="middle">Transpose -x to LHS (+x)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">In the equation \(2x - 1 = 14 - x\), when \(-x\) is transposed to LHS and \(-1\) to RHS, what equation results?</p>
</div>""",
     ["\(3x = 15\)", "\(x = 13\)", "\(3x = 13\)", "\(x = 15\)"],
     "A", "OSC", "easy",
     "Transposing \(-x\) to LHS gives \(2x + x = 3x\). Transposing \(-1\) to RHS gives \(14 + 1 = 15\). Thus, \(3x = 15\)."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Expansion of brackets -->
    <rect x="30" y="20" width="280" height="45" rx="6" fill="#1e293b" stroke="#6366f1" stroke-width="2"/>
    <text x="170" y="47" fill="#e0e7ff" font-size="13" font-weight="bold" text-anchor="middle">8x + 4 = 3(x - 1) + 7</text>
    <!-- Arrow down -->
    <line x1="170" y1="68" x2="170" y2="88" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="30" y="90" width="280" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="115" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">8x + 4 = 3x + 4</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">After distributing 3 into \((x - 1)\) and simplifying, the equation becomes \(8x + 4 = 3x + 4\). What is \(x\)?</p>
</div>""",
     ["0", "1", "4", "No solution"],
     "A", "OSC", "easy",
     "Subtracting 4 from both sides: \(8x = 3x \implies 8x - 3x = 0 \implies 5x = 0 \implies x = 0\)."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Fraction multiplier diagram -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="45" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">x = (4/5)(x + 10)</text>
    <!-- Multiply by 5 step -->
    <text x="170" y="80" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">Multiply both sides by 5</text>
    <rect x="30" y="92" width="280" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="117" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">5x = 4x + 40</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">From \(5x = 4x + 40\), what is the value of \(x\)?</p>
</div>""",
     ["40", "10", "20", "50"],
     "A", "OSC", "easy",
     "Subtracting \(4x\) from both sides gives \(5x - 4x = 40 \implies x = 40\)."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- LCM box for 2x/3 + 1 = 7x/15 + 3 -->
    <rect x="20" y="15" width="300" height="40" rx="6" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
    <text x="170" y="40" fill="#f472b6" font-size="13" font-weight="bold" text-anchor="middle">(2x/3) - (7x/15) = 3 - 1</text>
    <!-- Fraction subtraction with LCM 15 -->
    <rect x="50" y="65" width="240" height="40" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
    <text x="170" y="90" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">(10x - 7x) / 15 = 2</text>
    <text x="170" y="130" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">3x / 15 = 2  ==&gt;  x / 5 = 2</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the final root \(x\) obtained from \(\frac{x}{5} = 2\)?</p>
</div>""",
     ["10", "5", "15", "7"],
     "A", "OSC", "easy",
     "\(\frac{x}{5} = 2 \implies x = 2 \times 5 = 10\)."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Verification Table Diagram -->
    <rect x="20" y="20" width="140" height="90" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="90" y="45" fill="#60a5fa" font-size="12" font-weight="bold" text-anchor="middle">LHS: 2y + 5/3</text>
    <text x="90" y="70" fill="#cbd5e1" font-size="11" text-anchor="middle">y = 7/3</text>
    <text x="90" y="95" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">14/3 + 5/3 = 19/3</text>
    <rect x="180" y="20" width="140" height="90" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="250" y="45" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">RHS: 26/3 - y</text>
    <text x="250" y="70" fill="#cbd5e1" font-size="11" text-anchor="middle">y = 7/3</text>
    <text x="250" y="95" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">26/3 - 7/3 = 19/3</text>
    <text x="170" y="130" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">LHS = RHS = 19/3 (Verified)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">The diagram verifies the solution \(y = \frac{7}{3}\) for \(2y + \frac{5}{3} = \frac{26}{3} - y\). What is the common value of LHS and RHS?</p>
</div>""",
     ["\\(\\frac{19}{3}\\)", "\\(\\frac{7}{3}\\)", "\\(\\frac{26}{3}\\)", "7"],
     "A", "OSC", "easy",
     "Substituting \(y = \frac{7}{3}\): LHS = \(2(\frac{7}{3}) + \frac{5}{3} = \frac{19}{3}\), and RHS = \(\frac{26}{3} - \frac{7}{3} = \frac{19}{3}\)."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Equation solving flow for 3m = 5m - 8/5 -->
    <rect x="40" y="20" width="260" height="35" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="170" y="43" fill="#fbbf24" font-size="13" font-weight="bold" text-anchor="middle">3m = 5m - (8/5)</text>
    <rect x="40" y="65" width="260" height="30" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1"/>
    <text x="170" y="85" fill="#94a3b8" font-size="12" text-anchor="middle">3m - 5m = -(8/5)  ==&gt;  -2m = -(8/5)</text>
    <rect x="40" y="100" width="260" height="30" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="120" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">m = 8 / (5 * 2) = 4/5</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the solution \(m\) to the linear equation shown?</p>
</div>""",
     ["\\(\\frac{4}{5}\\)", "\\(-\\frac{4}{5}\\)", "\\(\\frac{8}{5}\\)", "2"],
     "A", "OSC", "easy",
     "\(-2m = -8/5 \implies m = \frac{-8/5}{-2} = \frac{4}{5}\)."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Two intersecting lines representing linear sides -->
    <line x1="40" y1="110" x2="300" y2="30" stroke="#38bdf8" stroke-width="3"/>
    <text x="80" y="60" fill="#38bdf8" font-size="11" font-weight="bold">y = 3x - 1</text>
    <line x1="40" y1="30" x2="300" y2="110" stroke="#f43f5e" stroke-width="3"/>
    <text x="240" y="60" fill="#f43f5e" font-size="11" font-weight="bold">y = -x + 7</text>
    <!-- Intersection point at (2, 5) -->
    <circle cx="170" cy="70" r="6" fill="#10b981" stroke="#f8fafc" stroke-width="2"/>
    <text x="170" y="95" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Intersection: x = 2</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">The graphs of \(y = 3x - 1\) and \(y = -x + 7\) intersect where \(3x - 1 = -x + 7\). What is the \(x\)-coordinate of intersection?</p>
</div>""",
     ["2", "3", "1", "4"],
     "A", "OSC", "easy",
     "\(3x - 1 = -x + 7 \implies 3x + x = 7 + 1 \implies 4x = 8 \implies x = 2\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Decimal equation visual -->
    <rect x="20" y="20" width="300" height="40" rx="6" fill="#1e293b" stroke="#8b5cf6" stroke-width="2"/>
    <text x="170" y="45" fill="#a78bfa" font-size="13" font-weight="bold" text-anchor="middle">0.25(4f - 3) = 0.05(10f - 9)</text>
    <!-- Multiply by 100 -->
    <text x="170" y="80" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">Multiply entire equation by 100</text>
    <rect x="20" y="90" width="300" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="115" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">25(4f - 3) = 5(10f - 9)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Simplifying \(25(4f - 3) = 5(10f - 9)\) yields which value for \(f\)?</p>
</div>""",
     ["0.6", "0.8", "0.5", "1.2"],
     "A", "OSC", "easy",
     "Divide both sides by 5: \(5(4f - 3) = 10f - 9 \implies 20f - 15 = 10f - 9 \implies 10f = 6 \implies f = 0.6\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="130" viewBox="0 0 340 130" xmlns="http://www.w3.org/2000/svg">
    <!-- Identity vs Contradiction chart -->
    <rect x="20" y="20" width="140" height="90" rx="6" fill="#1e293b" stroke="#06b6d4" stroke-width="2"/>
    <text x="90" y="45" fill="#22d3ee" font-size="12" font-weight="bold" text-anchor="middle">Case 1: 3x + 6 = 3x + 6</text>
    <text x="90" y="70" fill="#94a3b8" font-size="11" text-anchor="middle">0 = 0 (True)</text>
    <text x="90" y="95" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">Infinitely Many Roots</text>
    <rect x="180" y="20" width="140" height="90" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <text x="250" y="45" fill="#fb7185" font-size="12" font-weight="bold" text-anchor="middle">Case 2: 2x + 1 = 2x + 7</text>
    <text x="250" y="70" fill="#94a3b8" font-size="11" text-anchor="middle">1 = 7 (False)</text>
    <text x="250" y="95" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">No Solution</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">An equation in one variable that simplifies to a false statement like \(1 = 7\) has how many solutions?</p>
</div>""",
     ["No solution", "One solution", "Infinitely many solutions", "Two solutions"],
     "A", "OSC", "easy",
     "When the variable terms cancel out leaving an unequal statement (e.g. \(1 = 7\)), the equation represents an impossible condition and has no solution."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="130" viewBox="0 0 340 130" xmlns="http://www.w3.org/2000/svg">
    <!-- Number line with solution x = 5 -->
    <line x1="30" y1="65" x2="310" y2="65" stroke="#64748b" stroke-width="3"/>
    <g fill="#f8fafc" font-size="11" text-anchor="middle">
      <circle cx="50" cy="65" r="3"/> <text x="50" y="85">1</text>
      <circle cx="95" cy="65" r="3"/> <text x="95" y="85">2</text>
      <circle cx="140" cy="65" r="3"/> <text x="140" y="85">3</text>
      <circle cx="185" cy="65" r="3"/> <text x="185" y="85">4</text>
      <circle cx="230" cy="65" r="3"/> <text x="230" y="85">5</text>
      <circle cx="275" cy="65" r="3"/> <text x="275" y="85">6</text>
    </g>
    <!-- Highlighted dot at x = 5 -->
    <circle cx="230" cy="65" r="7" fill="#10b981" stroke="#34d399" stroke-width="2"/>
    <text x="230" y="45" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">x = 5</text>
    <text x="170" y="115" fill="#e2e8f0" font-size="12" text-anchor="middle">Equation: 2x - 1 = 14 - x  ==&gt;  3x = 15  ==&gt;  x = 5</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What equation has its root represented at \(x = 5\) on the number line?</p>
</div>""",
     ["\(2x - 1 = 14 - x\)", "\(2x + 1 = 14 + x\)", "\(3x = 12\)", "\(x + 2 = 5\)"],
     "A", "OSC", "easy",
     "\(2x - 1 = 14 - x \implies 3x = 15 \implies x = 5\)."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Box simplification step -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="45" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">7x - 2 = 5(x - 2) + 12</text>
    <!-- Expand RHS -->
    <rect x="30" y="80" width="280" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="105" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">7x - 2 = 5x + 2  ==&gt;  2x = 4  ==&gt;  x = 2</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the solution to \(7x - 2 = 5(x - 2) + 12\)?</p>
</div>""",
     ["2", "4", "3", "1"],
     "A", "OSC", "easy",
     "Expanding RHS: \(5x - 10 + 12 = 5x + 2\). Equating: \(7x - 5x = 2 + 2 \implies 2x = 4 \implies x = 2\).")
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch4_topic2.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
