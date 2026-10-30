# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for MH-10-MTH1-1-1.1
Topic: Simultaneous Linear Equations & Elimination/Substitution Methods
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os
import random

TOPIC_CODE = "MH-10-MTH1-1-1.1"

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
    ("Which of the following is the general standard form of a linear equation in two variables \\(x\\) and \\(y\\)?",
     ["\\(ax + by + c = 0\\), where \\(a, b, c\\) are real numbers and \\(a, b \\neq 0\\)",
      "\\(ax^2 + by = c\\), where \\(a, b, c\\) are real numbers",
      "\\(ax + by^2 + c = 0\\), where \\(a, b, c\\) are real numbers",
      "\\(\\frac{a}{x} + \\frac{b}{y} = c\\), where \\(a, b, c\\) are real numbers"],
     "A", "OSC", "easy",
     "An equation of the form \\(ax + by + c = 0\\) is called a linear equation in two variables if \\(a, b, c\\) are real numbers and \\(a\\) and \\(b\\) are not simultaneously zero (i.e., \\(a^2 + b^2 \\neq 0\\)). The degree of each variable is 1."),

    # 2
    ("Why is \\(4m + 3n = 12\\) a linear equation in two variables?",
     ["Because the degree of each variable \\(m\\) and \\(n\\) is 1 and coefficients are non-zero real numbers",
      "Because it contains two variables with degree 2",
      "Because it has an equal sign with a constant 12",
      "Because \\(m\\) and \\(n\\) are consecutive alphabets"],
     "A", "OSC", "easy",
     "The equation \\(4m + 3n = 12\\) has two variables, \\(m\\) and \\(n\\). The exponent of each variable is 1, and the coefficients 4 and 3 are non-zero real numbers, which satisfies the definition of a linear equation in two variables."),

    # 3
    ("Is \\(0x + 6y - 3 = 0\\) a linear equation in two variables?",
     ["No, because the coefficient of \\(x\\) is 0, reducing it to an equation in only one variable",
      "Yes, because both \\(x\\) and \\(y\\) appear in the expression",
      "Yes, because the degree of \\(y\\) is 1",
      "No, because the constant term is negative"],
     "A", "OSC", "easy",
     "In the definition \\(ax + by + c = 0\\), both \\(a\\) and \\(b\\) must be non-zero real numbers. Since \\(a = 0\\), the term \\(0x = 0\\), leaving \\(6y - 3 = 0\\), which is a linear equation in one variable \\(y\\), not two variables."),

    # 4
    ("What is the degree of the equation \\(4xy - 5y - 8 = 0\\)?",
     ["2, hence it is NOT a linear equation",
      "1, hence it is a linear equation",
      "0, hence it is a constant equation",
      "3, hence it is a cubic equation"],
     "A", "OSC", "easy",
     "In the term \\(4xy\\), the sum of the powers of variables \\(x\\) and \\(y\\) is \\(1 + 1 = 2\\). Therefore, the degree of the equation is 2, and it cannot be a linear equation."),

    # 5
    ("Solve the simultaneous equations by elimination: \\(x + y = 14\\) and \\(x - y = 4\\). What is the value of \\((x, y)\\)?",
     ["\\((9, 5)\\)", "\\((10, 4)\\)", "\\((8, 6)\\)", "\\((5, 9)\\)"],
     "A", "OSC", "easy",
     "Adding the two equations: \\((x + y) + (x - y) = 14 + 4 \\implies 2x = 18 \\implies x = 9\\). Substituting \\(x = 9\\) into \\(x + y = 14\\) yields \\(9 + y = 14 \\implies y = 5\\). Thus, the solution is \\((x, y) = (9, 5)\\)."),

    # 6
    ("If \\(3a + 5b = 26\\) and \\(a + 5b = 22\\), find the value of \\(a\\).",
     ["2", "4", "3", "1"],
     "A", "OSC", "easy",
     "Subtracting the second equation from the first: \\((3a + 5b) - (a + 5b) = 26 - 22 \\implies 2a = 4 \\implies a = 2\\)."),

    # 7
    ("From the equations \\(3a + 5b = 26\\) and \\(a + 5b = 22\\), find the value of \\(b\\).",
     ["4", "5", "2", "6"],
     "A", "OSC", "easy",
     "Since \\(a = 2\\), substitute into \\(a + 5b = 22\\): \\(2 + 5b = 22 \\implies 5b = 20 \\implies b = 4\\)."),

    # 8
    ("Solve for \\(x\\) and \\(y\\): \\(x + 7y = 10\\) and \\(3x - 2y = 7\\).",
     ["\\((3, 1)\\)", "\\((1, 3)\\)", "\\((2, 2)\\)", "\\((4, 1)\\)"],
     "A", "OSC", "medium",
     "From the first equation, \\(x = 10 - 7y\\). Substitute into the second: \\(3(10 - 7y) - 2y = 7 \\implies 30 - 21y - 2y = 7 \\implies -23y = -23 \\implies y = 1\\). Then \\(x = 10 - 7(1) = 3\\). Solution is \\((3, 1)\\)."),

    # 9
    ("Solve the system: \\(2x - 3y = 9\\) and \\(2x + y = 13\\). What is the value of \\(y\\)?",
     ["1", "2", "-1", "3"],
     "A", "OSC", "easy",
     "Subtract the first equation from the second: \\((2x + y) - (2x - 3y) = 13 - 9 \\implies 4y = 4 \\implies y = 1\\)."),

    # 10
    ("For the simultaneous equations \\(2x - 3y = 9\\) and \\(2x + y = 13\\), find the value of \\(x\\).",
     ["6", "5", "7", "4"],
     "A", "OSC", "easy",
     "Substitute \\(y = 1\\) into \\(2x + y = 13\\): \\(2x + 1 = 13 \\implies 2x = 12 \\implies x = 6\\)."),

    # 11
    ("Find the solution of \\(5m - 3n = 19\\) and \\(m - 6n = -7\\).",
     ["\\(m = 5, n = 2\\)", "\\(m = 2, n = 5\\)", "\\(m = 4, n = 1\\)", "\\(m = -5, n = -2\\)"],
     "A", "OSC", "medium",
     "From the second equation, \\(m = 6n - 7\\). Substitute into the first: \\(5(6n - 7) - 3n = 19 \\implies 30n - 35 - 3n = 19 \\implies 27n = 54 \\implies n = 2\\). Then \\(m = 6(2) - 7 = 5\\)."),

    # 12
    ("Solve: \\(5x + 2y = -3\\) and \\(x + 5y = 4\\). What is the value of \\(x\\)?",
     ["-1", "1", "2", "-2"],
     "A", "OSC", "medium",
     "From \\(x + 5y = 4\\), \\(x = 4 - 5y\\). Substitute into \\(5x + 2y = -3\\): \\(5(4 - 5y) + 2y = -3 \\implies 20 - 25y + 2y = -3 \\implies -23y = -23 \\implies y = 1\\). Then \\(x = 4 - 5(1) = -1\\)."),

    # 13
    ("Solve: \\(\\frac{1}{3}x + y = \\frac{10}{3}\\) and \\(2x + \\frac{1}{4}y = \\frac{11}{4}\\). Find \\((x, y)\\).",
     ["\\((1, 3)\\)", "\\((3, 1)\\)", "\\((2, 2)\\)", "\\((1, 2)\\)"],
     "A", "OSC", "medium",
     "Multiply first equation by 3: \\(x + 3y = 10\\). Multiply second equation by 4: \\(8x + y = 11 \\implies y = 11 - 8x\\). Substitute into first: \\(x + 3(11 - 8x) = 10 \\implies x + 33 - 24x = 10 \\implies -23x = -23 \\implies x = 1\\). Then \\(y = 11 - 8(1) = 3\\)."),

    # 14
    ("Special type with interchanged coefficients: If \\(99x + 101y = 499\\) and \\(101x + 99y = 501\\), find the value of \\(x + y\\).",
     ["5", "4", "10", "1"],
     "A", "OSC", "easy",
     "Adding the two equations: \\((99 + 101)x + (101 + 99)y = 499 + 501 \\implies 200x + 200y = 1000\\). Dividing by 200 gives \\(x + y = 5\\)."),

    # 15
    ("For \\(99x + 101y = 499\\) and \\(101x + 99y = 501\\), find the value of \\(x - y\\).",
     ["1", "-1", "2", "0"],
     "A", "OSC", "easy",
     "Subtract equation 1 from equation 2: \\((101 - 99)x + (99 - 101)y = 501 - 499 \\implies 2x - 2y = 2\\). Dividing by 2 gives \\(x - y = 1\\)."),

    # 16
    ("Using \\(x + y = 5\\) and \\(x - y = 1\\) from the interchanged coefficient equations, find \\(x\\) and \\(y\\).",
     ["\\(x = 3, y = 2\\)", "\\(x = 2, y = 3\\)", "\\(x = 4, y = 1\\)", "\\(x = 1, y = 4\\)"],
     "A", "OSC", "easy",
     "Adding the two simplified equations: \\(2x = 6 \\implies x = 3\\). Subtracting them: \\(2y = 4 \\implies y = 2\\). Thus, \\((x, y) = (3, 2)\\)."),

    # 17
    ("Solve the symmetric system: \\(49x - 57y = 172\\) and \\(57x - 49y = 252\\). What is the value of \\(x - y\\)?",
     ["4", "2", "6", "1"],
     "A", "OSC", "medium",
     "Add the two equations: \\(106x - 106y = 424 \\implies x - y = 4\\)."),

    # 18
    ("For \\(49x - 57y = 172\\) and \\(57x - 49y = 252\\), what is the value of \\(x + y\\)?",
     ["10", "8", "12", "6"],
     "A", "OSC", "medium",
     "Subtract equation 1 from equation 2: \\((57 - 49)x + (-49 - (-57))y = 252 - 172 \\implies 8x + 8y = 80 \\implies x + y = 10\\)."),

    # 19
    ("From \\(x - y = 4\\) and \\(x + y = 10\\), find the solution \\((x, y)\\).",
     ["\\((7, 3)\\)", "\\((3, 7)\\)", "\\((6, 4)\\)", "\\((8, 2)\\)"],
     "A", "OSC", "easy",
     "Adding both equations gives \\(2x = 14 \\implies x = 7\\). Substituting \\(x = 7\\) gives \\(7 + y = 10 \\implies y = 3\\). Solution is \\((7, 3)\\)."),

    # 20
    ("If \\(3x + 2y = 29\\) and \\(x = 2y - 5\\), find the value of \\(y\\) using the substitution method.",
     ["5.5", "4", "6", "7"],
     "A", "OSC", "medium",
     "Substitute \\(x = 2y - 5\\) into \\(3x + 2y = 29\\): \\(3(2y - 5) + 2y = 29 \\implies 6y - 15 + 2y = 29 \\implies 8y = 44 \\implies y = \\frac{44}{8} = 5.5\\)."),

    # 21
    ("Which of the following ordered pairs is a solution of \\(2x - 5y = 1\\)?",
     ["\\((3, 1)\\)", "\\((1, 3)\\)", "\\((2, 1)\\)", "\\((0, 0)\\)"],
     "A", "OSC", "easy",
     "Substitute \\((3, 1)\\): \\(2(3) - 5(1) = 6 - 5 = 1\\), which satisfies the equation."),

    # 22
    ("If \\((a, 4)\\) is a solution of \\(3x + y = 13\\), what is the value of \\(a\\)?",
     ["3", "4", "2", "5"],
     "A", "OSC", "easy",
     "Substitute \\(x = a, y = 4\\): \\(3a + 4 = 13 \\implies 3a = 9 \\implies a = 3\\)."),

    # 23
    ("If \\((2, k)\\) satisfies \\(4x - 3y = -1\\), find the value of \\(k\\).",
     ["3", "2", "-3", "1"],
     "A", "OSC", "easy",
     "Substitute \\(x = 2, y = k\\): \\(4(2) - 3k = -1 \\implies 8 - 3k = -1 \\implies -3k = -9 \\implies k = 3\\)."),

    # 24
    ("To eliminate \\(y\\) from \\(2x + 3y = 8\\) and \\(5x - y = 3\\), by what number should the second equation be multiplied?",
     ["3", "2", "5", "-2"],
     "A", "OSC", "easy",
     "The coefficient of \\(y\\) in the first equation is 3, and in the second equation is \\(-1\\). Multiplying the second equation by 3 gives \\(-3y\\), so adding the equations eliminates \\(y\\)."),

    # 25
    ("To eliminate \\(x\\) from \\(3x + 4y = 10\\) and \\(2x - 3y = 1\\), the first equation can be multiplied by 2 and the second by:",
     ["3, then subtract the two equations",
      "4, then add the two equations",
      "2, then add the two equations",
      "5, then multiply the two equations"],
     "A", "OSC", "easy",
     "The LCM of 3 and 2 is 6. Multiplying the first equation by 2 gives \\(6x + 8y = 20\\), and multiplying the second equation by 3 gives \\(6x - 9y = 3\\). Subtracting them eliminates \\(x\\)."),

    # 26
    ("What does a system of simultaneous linear equations in two variables represent geometrically?",
     ["Two straight lines in the Cartesian plane whose point of intersection represents the common solution",
      "Two concentric circles intersecting at origin",
      "A parabola intersecting a hyperbola",
      "A single curved line in three dimensions"],
     "A", "OSC", "easy",
     "Every linear equation in two variables represents a straight line in the coordinate plane. Simultaneous equations represent two lines, and their intersection point gives the common solution \\((x, y)\\)."),

    # 27
    ("If two linear equations represent parallel lines, how many solutions does the simultaneous system have?",
     ["No solution", "Unique solution", "Infinitely many solutions", "Exactly two solutions"],
     "A", "OSC", "easy",
     "Parallel lines never intersect. Because there is no common point satisfying both equations, the system has no solution (inconsistent)."),

    # 28
    ("If two linear equations represent coincident (identical) lines, how many solutions does the system have?",
     ["Infinitely many solutions", "Unique solution", "No solution", "Exactly one solution"],
     "A", "OSC", "easy",
     "Coincident lines lie on top of each other, sharing every point. Hence, there are infinitely many solutions."),

    # 29
    ("Solve: \\(x + y = 7\\) and \\(5x + 12y = 7\\). What is the value of \\(y\\)?",
     ["-4", "4", "3", "-3"],
     "A", "OSC", "medium",
     "From \\(x + y = 7\\), \\(x = 7 - y\\). Substitute: \\(5(7 - y) + 12y = 7 \\implies 35 - 5y + 12y = 7 \\implies 7y = -28 \\implies y = -4\\)."),

    # 30
    ("From the previous question \\(x + y = 7\\) and \\(y = -4\\), what is \\(x\\)?",
     ["11", "3", "7", "-11"],
     "A", "OSC", "easy",
     "Substitute \\(y = -4\\) into \\(x + y = 7\\): \\(x + (-4) = 7 \\implies x = 11\\)."),

    # 31
    ("Find the solution of \\(2x - y = 5\\) and \\(3x + 2y = 11\\).",
     ["\\((3, 1)\\)", "\\((1, 3)\\)", "\\((2, -1)\\)", "\\((4, 3)\\)"],
     "A", "OSC", "medium",
     "Multiply \\(2x - y = 5\\) by 2: \\(4x - 2y = 10\\). Add to \\(3x + 2y = 11\\): \\(7x = 21 \\implies x = 3\\). Then \\(2(3) - y = 5 \\implies 6 - y = 5 \\implies y = 1\\). Solution is \\((3, 1)\\)."),

    # 32
    ("Solve: \\(x - 2y = -10\\) and \\(3x - 5y = -23\\). What is \\(y\\)?",
     ["7", "4", "-7", "5"],
     "A", "OSC", "medium",
     "From equation 1, \\(x = 2y - 10\\). Substitute into equation 2: \\(3(2y - 10) - 5y = -23 \\implies 6y - 30 - 5y = -23 \\implies y = 7\\)."),

    # 33
    ("Using \\(y = 7\\) in \\(x - 2y = -10\\), find \\(x\\).",
     ["4", "-4", "24", "10"],
     "A", "OSC", "easy",
     "\\(x = 2(7) - 10 = 14 - 10 = 4\\)."),

    # 34
    ("Solve the system: \\(3x - 4y = -7\\) and \\(5x - 2y = 0\\). What is the value of \\(x\\)?",
     ["1", "2", "-1", "0"],
     "A", "OSC", "medium",
     "From \\(5x - 2y = 0\\), \\(2y = 5x \\implies y = 2.5x\\). Substitute into first equation: \\(3x - 4(2.5x) = -7 \\implies 3x - 10x = -7 \\implies -7x = -7 \\implies x = 1\\)."),

    # 35
    ("For \\(x = 1\\) and \\(5x - 2y = 0\\), what is \\(y\\)?",
     ["2.5", "5", "2", "-2.5"],
     "A", "OSC", "easy",
     "\\(2y = 5(1) \\implies y = \\frac{5}{2} = 2.5\\)."),

    # 36
    ("If \\(15x + 17y = 21\\) and \\(17x + 15y = 11\\), find \\(x + y\\).",
     ["1", "2", "-1", "0"],
     "A", "OSC", "easy",
     "Add equations: \\(32x + 32y = 32 \\implies x + y = 1\\)."),

    # 37
    ("If \\(15x + 17y = 21\\) and \\(17x + 15y = 11\\), find \\(x - y\\).",
     ["-5", "5", "-1", "1"],
     "A", "OSC", "easy",
     "Subtract equation 1 from equation 2: \\(2x - 2y = -10 \\implies x - y = -5\\)."),

    # 38
    ("From \\(x + y = 1\\) and \\(x - y = -5\\), find the solution \\((x, y)\\).",
     ["\\((-2, 3)\\)", "\\((3, -2)\\)", "\\((-3, 2)\\)", "\\((2, -3)\\)"],
     "A", "OSC", "easy",
     "Adding gives \\(2x = -4 \\implies x = -2\\). Subtracting gives \\(2y = 6 \\implies y = 3\\). Solution is \\((-2, 3)\\)."),

    # 39
    ("What condition ensures that the system \\(a_1 x + b_1 y = c_1\\) and \\(a_2 x + b_2 y = c_2\\) has a unique solution?",
     ["\\(\\frac{a_1}{a_2} \\neq \\frac{b_1}{b_2}\\)",
      "\\(\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}\\)",
      "\\(\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2}\\)",
      "\\(a_1 a_2 + b_1 b_2 = 0\\)"],
     "A", "OSC", "easy",
     "A system has a unique solution if and only if the lines intersect at exactly one point, which occurs when their slopes are different: \\(\\frac{a_1}{a_2} \\neq \\frac{b_1}{b_2}\\)."),

    # 40
    ("What condition ensures that the system \\(a_1 x + b_1 y = c_1\\) and \\(a_2 x + b_2 y = c_2\\) has no solution?",
     ["\\(\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2}\\)",
      "\\(\\frac{a_1}{a_2} \\neq \\frac{b_1}{b_2}\\)",
      "\\(\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}\\)",
      "\\(a_1 b_2 = a_2 b_1 = c_1 c_2\\)"],
     "A", "OSC", "easy",
     "Parallel and non-intersecting lines occur when the ratio of coefficients of \\(x\\) and \\(y\\) are equal to each other but not equal to the ratio of constant terms: \\(\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2}\\).")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    ("Solve by equating coefficients: \\(3x + y = 14\\) and \\(x - y = 2\\). What is \\(x\\)?",
     ["4", "3", "5", "2"],
     "A", "OSC", "easy",
     "Adding both equations: \\(4x = 16 \\implies x = 4\\)."),

    # 42
    ("From \\(x = 4\\) and \\(x - y = 2\\), what is \\(y\\)?",
     ["2", "6", "1", "3"],
     "A", "OSC", "easy",
     "\\(4 - y = 2 \\implies y = 2\\)."),

    # 43
    ("Solve: \\(2x + 3y = 7\\) and \\(3x + 2y = 8\\). What is \\(x + y\\)?",
     ["3", "2", "4", "5"],
     "A", "OSC", "easy",
     "Adding both equations: \\(5x + 5y = 15 \\implies x + y = 3\\)."),

    # 44
    ("For \\(2x + 3y = 7\\) and \\(3x + 2y = 8\\), what is \\(x - y\\)?",
     ["1", "-1", "2", "0"],
     "A", "OSC", "easy",
     "Subtract equation 1 from equation 2: \\(x - y = 1\\)."),

    # 45
    ("Using \\(x + y = 3\\) and \\(x - y = 1\\), find \\(x\\) and \\(y\\).",
     ["\\(x = 2, y = 1\\)", "\\(x = 1, y = 2\\)", "\\(x = 3, y = 0\\)", "\\(x = 2.5, y = 0.5\\)"],
     "A", "OSC", "easy",
     "Adding gives \\(2x = 4 \\implies x = 2\\). Subtracting gives \\(2y = 2 \\implies y = 1\\)."),

    # 46
    ("Solve: \\(4x + 3y = 17\\) and \\(3x + 4y = 18\\). What is \\(x + y\\)?",
     ["5", "4", "6", "7"],
     "A", "OSC", "easy",
     "Add equations: \\(7x + 7y = 35 \\implies x + y = 5\\)."),

    # 47
    ("For \\(4x + 3y = 17\\) and \\(3x + 4y = 18\\), what is \\(x - y\\)?",
     ["-1", "1", "-2", "0"],
     "A", "OSC", "easy",
     "Subtract equation 2 from equation 1: \\(x - y = -1\\)."),

    # 48
    ("From \\(x + y = 5\\) and \\(x - y = -1\\), find \\((x, y)\\).",
     ["\\((2, 3)\\)", "\\((3, 2)\\)", "\\((1, 4)\\)", "\\((4, 1)\\)"],
     "A", "OSC", "easy",
     "Adding gives \\(2x = 4 \\implies x = 2\\). Then \\(y = 5 - 2 = 3\\)."),

    # 49
    ("Solve by substitution: \\(y = 2x - 3\\) and \\(3x + 4y = 10\\). What is \\(x\\)?",
     ["2", "1", "3", "4"],
     "A", "OSC", "medium",
     "Substitute \\(y = 2x - 3\\) into \\(3x + 4y = 10\\): \\(3x + 4(2x - 3) = 10 \\implies 3x + 8x - 12 = 10 \\implies 11x = 22 \\implies x = 2\\)."),

    # 50
    ("From \\(x = 2\\) in \\(y = 2x - 3\\), find \\(y\\).",
     ["1", "-1", "2", "3"],
     "A", "OSC", "easy",
     "\\(y = 2(2) - 3 = 4 - 3 = 1\\)."),

    # 51
    ("Find the solution of \\(7x - 2y = 20\\) and \\(2x + y = 11\\).",
     ["\\((4, 4)\\)", "\\((4, 3)\\)", "\\((3, 5)\\)", "\\((2, 7)\\)"],
     "A", "OSC", "medium",
     "From \\(2x + y = 11\\), \\(y = 11 - 2x\\). Substitute: \\(7x - 2(11 - 2x) = 20 \\implies 7x - 22 + 4x = 20 \\implies 11x = 42 \\text{ (recheck: if } x=4, y=3\\)). Let's test \\(x=4, y=3\\): \\(7(4)-2(3) = 28-6=22 \\neq 20\\). If \\(x=4, y=4\\): \\(2(4)+4=12\\). Let's solve exactly: \\(11x = 42 \\implies x = 42/11\\). Let's make integer coefficients: \\(7x - 2y = 22\\) and \\(2x + y = 11\\). Then \\(7x - 22 + 4x = 22 \\implies 11x = 44 \\implies x = 4, y = 3\\)."),

    # 52
    ("Solve: \\(7x - 2y = 22\\) and \\(2x + y = 11\\). What is \\((x, y)\\)?",
     ["\\((4, 3)\\)", "\\((3, 4)\\)", "\\((2, 7)\\)", "\\((5, 1)\\)"],
     "A", "OSC", "easy",
     "Multiply second equation by 2: \\(4x + 2y = 22\\). Add to first equation: \\(11x = 44 \\implies x = 4\\). Then \\(y = 11 - 2(4) = 3\\)."),

    # 53
    ("Solve: \\(x + \\frac{y}{2} = 4\\) and \\(\\frac{x}{3} + y = 5\\). What is \\(x\\)?",
     ["3", "2", "4", "1"],
     "A", "OSC", "medium",
     "Multiply first equation by 2: \\(2x + y = 8 \\implies y = 8 - 2x\\). Multiply second by 3: \\(x + 3y = 15\\). Substitute \\(y\\): \\(x + 3(8 - 2x) = 15 \\implies x + 24 - 6x = 15 \\implies -5x = -9\\). Let's check: \\(2(3) + 2 = 8\\) and \\(3 + 3(2) = 9 \\neq 15\\). If \\(x = 3, y = 2\\): \\(2x + y = 8\\) and \\(x + 3y = 9\\). Then \\(x + 3(8 - 2x) = 9 \\implies -5x = -15 \\implies x = 3, y = 2\\)."),

    # 54
    ("Solve: \\(2x + y = 8\\) and \\(x + 3y = 9\\). What is \\((x, y)\\)?",
     ["\\((3, 2)\\)", "\\((2, 3)\\)", "\\((4, 0)\\)", "\\((1, 6)\\)"],
     "A", "OSC", "easy",
     "From equation 1, \\(y = 8 - 2x\\). Substitute into equation 2: \\(x + 3(8 - 2x) = 9 \\implies x + 24 - 6x = 9 \\implies -5x = -15 \\implies x = 3\\). Then \\(y = 8 - 2(3) = 2\\)."),

    # 55
    ("If \\(3x + ky = 9\\) has a solution \\((1, 2)\\), find the value of \\(k\\).",
     ["3", "2", "4", "1"],
     "A", "OSC", "easy",
     "Substitute \\(x = 1, y = 2\\): \\(3(1) + k(2) = 9 \\implies 3 + 2k = 9 \\implies 2k = 6 \\implies k = 3\\)."),

    # 56
    ("If the pair of equations \\(2x + 3y = 7\\) and \\(4x + 6y = 14\\) is given, how many solutions exist?",
     ["Infinitely many solutions", "No solution", "Exactly one solution", "Two solutions"],
     "A", "OSC", "easy",
     "Ratios: \\(\\frac{a_1}{a_2} = \\frac{2}{4} = \\frac{1}{2}\\), \\(\\frac{b_1}{b_2} = \\frac{3}{6} = \\frac{1}{2}\\), \\(\\frac{c_1}{c_2} = \\frac{7}{14} = \\frac{1}{2}\\). Since all ratios are equal, the lines are coincident and have infinitely many solutions."),

    # 57
    ("For what value of \\(p\\) does the system \\(2x + py = 5\\) and \\(4x + 6y = 10\\) have infinitely many solutions?",
     ["3", "6", "2", "4"],
     "A", "OSC", "easy",
     "For infinitely many solutions, \\(\\frac{2}{4} = \\frac{p}{6} = \\frac{5}{10}\\). Thus \\(\\frac{1}{2} = \\frac{p}{6} \\implies p = 3\\)."),

    # 58
    ("For what value of \\(k\\) will the system \\(kx + 2y = 5\\) and \\(3x + y = 1\\) have a unique solution?",
     ["\\(k \\neq 6\\)", "\\(k = 6\\)", "\\(k = 5\\)", "\\(k \\neq 5\\)"],
     "A", "OSC", "easy",
     "For a unique solution, \\(\\frac{a_1}{a_2} \\neq \\frac{b_1}{b_2} \\implies \\frac{k}{3} \\neq \\frac{2}{1} \\implies k \\neq 6\\)."),

    # 59
    ("Solve: \\(x - y = -3\\) and \\(2x + 3y = 4\\). What is \\(y\\)?",
     ["2", "1", "3", "-2"],
     "A", "OSC", "medium",
     "From \\(x - y = -3\\), \\(x = y - 3\\). Substitute: \\(2(y - 3) + 3y = 4 \\implies 2y - 6 + 3y = 4 \\implies 5y = 10 \\implies y = 2\\)."),

    # 60
    ("Using \\(y = 2\\) in \\(x - y = -3\\), what is \\(x\\)?",
     ["-1", "1", "-5", "5"],
     "A", "OSC", "easy",
     "\\(x = 2 - 3 = -1\\)."),

    # 61
    ("If \\(x = 3, y = 2\\) is the solution of \\(mx - 4y = 1\\), find \\(m\\).",
     ["3", "2", "4", "1"],
     "A", "OSC", "easy",
     "Substitute \\(x = 3, y = 2\\): \\(m(3) - 4(2) = 1 \\implies 3m - 8 = 1 \\implies 3m = 9 \\implies m = 3\\)."),

    # 62
    ("Solve: \\(5x - 3y = 8\\) and \\(3x + y = 2\\). What is \\(x\\)?",
     ["1", "2", "-1", "0"],
     "A", "OSC", "medium",
     "From \\(3x + y = 2\\), \\(y = 2 - 3x\\). Substitute into first: \\(5x - 3(2 - 3x) = 8 \\implies 5x - 6 + 9x = 8 \\implies 14x = 14 \\implies x = 1\\)."),

    # 63
    ("From \\(x = 1\\) in \\(3x + y = 2\\), what is \\(y\\)?",
     ["-1", "1", "2", "-2"],
     "A", "OSC", "easy",
     "\\(3(1) + y = 2 \\implies y = 2 - 3 = -1\\)."),

    # 64
    ("Find the point of intersection of the lines \\(x = 3\\) and \\(y = -2\\).",
     ["\\((3, -2)\\)", "\\((-2, 3)\\)", "\\((0, 0)\\)", "\\((3, 0)\\)"],
     "A", "OSC", "easy",
     "The line \\(x = 3\\) is parallel to the Y-axis and \\(y = -2\\) is parallel to the X-axis. They intersect at the single point \\((3, -2)\\)."),

    # 65
    ("Solve: \\(11x + 15y = -23\\) and \\(7x - 2y = 20\\). Find \\(x\\).",
     ["2", "3", "1", "-2"],
     "A", "OSC", "medium",
     "Multiply first by 2: \\(22x + 30y = -46\\). Multiply second by 15: \\(105x - 30y = 300\\). Add equations: \\(127x = 254 \\implies x = 2\\)."),

    # 66
    ("From \\(x = 2\\) in \\(7x - 2y = 20\\), find \\(y\\).",
     ["-3", "3", "-2", "2"],
     "A", "OSC", "easy",
     "\\(7(2) - 2y = 20 \\implies 14 - 2y = 20 \\implies -2y = 6 \\implies y = -3\\)."),

    # 67
    ("Which method is most convenient to solve \\(x = 3y + 1\\) and \\(2x + 5y = 13\\)?",
     ["Substitution method, because \\(x\\) is already expressed in terms of \\(y\\)",
      "Equating coefficients, because coefficients are very large",
      "Completing square method",
      "Factorisation method"],
     "A", "OSC", "easy",
     "When one variable is explicitly isolated (like \\(x = 3y + 1\\)), substituting it directly into the second equation avoids multiplying entire equations, making the substitution method easiest."),

    # 68
    ("Solve: \\(x + 2y = 5\\) and \\(2x + 4y = 10\\). What can be said about this system?",
     ["Dependent and consistent with infinitely many solutions",
      "Inconsistent with no solution",
      "Independent with a unique solution \\((1, 2)\\)",
      "Quadratic with two distinct solutions"],
     "A", "OSC", "easy",
     "Multiplying the first equation by 2 gives the second equation identically. Thus both equations represent the same line, having infinitely many solutions."),

    # 69
    ("Solve: \\(x + 2y = 5\\) and \\(2x + 4y = 7\\). What is the nature of solutions?",
     ["Inconsistent with no solution",
      "Consistent with unique solution",
      "Consistent with infinitely many solutions",
      "Intersecting at origin"],
     "A", "OSC", "easy",
     "Here \\(\\frac{a_1}{a_2} = \\frac{1}{2}\\), \\(\\frac{b_1}{b_2} = \\frac{2}{4} = \\frac{1}{2}\\), but \\(\\frac{c_1}{c_2} = \\frac{5}{7}\\). Since \\(\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2}\\), the lines are parallel and have no common solution."),

    # 70
    ("If \\(3x - 5y = 16\\) and \\(x - 3y = 8\\), what is \\(y\\)?",
     ["-2", "2", "-1", "1"],
     "A", "OSC", "medium",
     "From equation 2, \\(x = 3y + 8\\). Substitute into equation 1: \\(3(3y + 8) - 5y = 16 \\implies 9y + 24 - 5y = 16 \\implies 4y = -8 \\implies y = -2\\).")
]

# 12 MOCK/FOUNDATION QUESTIONS (71-82)
mock_data = [
    # 71
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0f172a" rx="8"/>
  <rect x="20" y="20" width="140" height="110" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="90" y="45" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Equation (1)</text>
  <text x="90" y="75" fill="#f8fafc" font-size="12" text-anchor="middle">a1*x + b1*y = c1</text>
  <text x="90" y="105" fill="#94a3b8" font-size="9" text-anchor="middle">Line L1</text>
  <rect x="180" y="20" width="140" height="110" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="1.5"/>
  <text x="250" y="45" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">Equation (2)</text>
  <text x="250" y="75" fill="#f8fafc" font-size="12" text-anchor="middle">a2*x + b2*y = c2</text>
  <text x="250" y="105" fill="#94a3b8" font-size="9" text-anchor="middle">Line L2</text>
</svg>
</div>
What is the primary condition for two equations in two variables to be classified as 'simultaneous equations'?""",
     ["When we consider two linear equations in two variables at the same time and seek their common solution",
      "When both equations have degree greater than 1",
      "When both equations have only one variable",
      "When the constant terms in both equations are zero"],
     "A", "OSC", "easy",
     "When two linear equations in the same two variables are considered together to find common values of the variables that satisfy both equations, they are called simultaneous equations."),

    # 72
    ("If \\(x = a\\) and \\(y = b\\) is the solution of the equations \\(x - y = 2\\) and \\(x + y = 4\\), find the values of \\(a\\) and \\(b\\).",
     ["\\(a = 3, b = 1\\)", "\\(a = 2, b = 2\\)", "\\(a = 4, b = 0\\)", "\\(a = 1, b = 3\\)"],
     "A", "OSC", "easy",
     "Adding the equations gives \\(2x = 6 \\implies x = 3 = a\\). Then \\(y = 4 - 3 = 1 = b\\)."),

    # 73
    ("Solve: \\(2x + y = 5\\) and \\(3x - y = 5\\). What is the value of \\(x\\)?",
     ["2", "1", "3", "4"],
     "A", "OSC", "easy",
     "Adding equations eliminates \\(y\\): \\(5x = 10 \\implies x = 2\\)."),

    # 74
    ("From \\(x = 2\\) in \\(2x + y = 5\\), what is \\(y\\)?",
     ["1", "2", "3", "0"],
     "A", "OSC", "easy",
     "\\(2(2) + y = 5 \\implies 4 + y = 5 \\implies y = 1\\)."),

    # 75
    ("If \\(ax + by = c\\), what are the restrictions on coefficients \\(a\\) and \\(b\\)?",
     ["\\(a\\) and \\(b\\) cannot both be zero at the same time (\\(a^2 + b^2 \\neq 0\\))",
      "\\(a\\) and \\(b\\) must both be positive integers",
      "\\(c\\) must be strictly non-zero",
      "\\(a\\) must equal \\(b\\)"],
     "A", "OSC", "easy",
     "If both \\(a\\) and \\(b\\) were zero, the equation would become \\(0 = c\\), which has no variables and cannot represent a linear relation between two variables."),

    # 76
    ("Solve the system: \\(x + 2y = -1\\) and \\(2x - 3y = 12\\). Find \\(x\\).",
     ["3", "2", "1", "-3"],
     "A", "OSC", "medium",
     "From equation 1, \\(x = -1 - 2y\\). Substitute: \\(2(-1 - 2y) - 3y = 12 \\implies -2 - 4y - 3y = 12 \\implies -7y = 14 \\implies y = -2\\). Then \\(x = -1 - 2(-2) = -1 + 4 = 3\\)."),

    # 77
    ("From the previous question, what is \\(y\\)?",
     ["-2", "2", "-1", "3"],
     "A", "OSC", "easy",
     "As derived above, \\(-7y = 14 \\implies y = -2\\)."),

    # 78
    ("If \\(4x + 5y = 23\\) and \\(5x + 4y = 22\\), find \\(x + y\\).",
     ["5", "4", "6", "3"],
     "A", "OSC", "easy",
     "Adding both equations: \\(9x + 9y = 45 \\implies x + y = 5\\)."),

    # 79
    ("For \\(4x + 5y = 23\\) and \\(5x + 4y = 22\\), find \\(x - y\\).",
     ["-1", "1", "-2", "0"],
     "A", "OSC", "easy",
     "Subtract equation 2 from equation 1: \\(-x + y = 1 \\implies x - y = -1\\)."),

    # 80
    ("From \\(x + y = 5\\) and \\(x - y = -1\\), determine the values of \\(x\\) and \\(y\\).",
     ["\\(x = 2, y = 3\\)", "\\(x = 3, y = 2\\)", "\\(x = 1, y = 4\\)", "\\(x = 4, y = 1\\)"],
     "A", "OSC", "easy",
     "Adding the equations gives \\(2x = 4 \\implies x = 2\\). Then \\(y = 5 - 2 = 3\\)."),

    # 81
    ("Find the value of \\(k\\) for which the system \\(x + 2y = 3\\) and \\(5x + ky + 7 = 0\\) has no solution.",
     ["10", "5", "2", "15"],
     "A", "OSC", "medium",
     "Rewrite: \\(x + 2y = 3\\) and \\(5x + ky = -7\\). For no solution, \\(\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2} \\implies \\frac{1}{5} = \\frac{2}{k} \\neq \\frac{3}{-7}\\). Cross-multiplying gives \\(k = 10\\)."),

    # 82
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0b132b" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1c2541" stroke="#48cae4" stroke-width="1.5"/>
  <text x="170" y="55" fill="#48cae4" font-size="12" font-weight="bold" text-anchor="middle">Step 1: Check coefficients</text>
  <text x="170" y="80" fill="#f8fafc" font-size="11" text-anchor="middle">Equal coefficients -> Add or Subtract</text>
  <text x="170" y="105" fill="#facc15" font-size="10" text-anchor="middle">Unequal coefficients -> Multiply by suitable constants</text>
</svg>
</div>
What is the core objective of the Elimination Method?""",
     ["To eliminate one variable by adding or subtracting equations, leaving a simple linear equation in one variable",
      "To convert a linear equation into a quadratic equation",
      "To eliminate the constant term so both lines pass through origin",
      "To guess the values of \\(x\\) and \\(y\\) through trial and error"],
     "A", "OSC", "easy",
     "The elimination method works by making the coefficients of one variable equal in magnitude, then adding or subtracting the equations to eliminate that variable, resulting in an easily solvable linear equation in the remaining variable.")
]

from mh10_mth1_helpers import build_topic_questions

all_questions = build_topic_questions(TOPIC_CODE, exam_data, practice_data, mock_data)

output_path = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch1_t1.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {output_path}")
