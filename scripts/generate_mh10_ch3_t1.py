# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 3: Arithmetic Progression (Topics 3.1 & 3.2)
Each topic: exactly 82 canonical questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# ==============================================================================
# TOPIC 3.1: Sequence & Arithmetic Progression (AP) Concept (MH-10-MTH1-3-3.1)
# ==============================================================================
t31_exam = [
    # 1
    ("What is an Arithmetic Progression (AP)?",
     ["A sequence in which the difference between any two consecutive terms (t_(n+1) - t_n = d) is constant",
      "A sequence where the ratio of consecutive terms is constant",
      "A set of numbers whose sum is always zero",
      "A collection of random prime numbers"],
     "A", "OSC", "easy",
     "An Arithmetic Progression (AP) is defined as a sequence in which the difference between any term and its preceding term is constant throughout the sequence: \\(t_{n+1} - t_n = d\\), where \\(d\\) is the common difference."),

    # 2
    ("What values can the common difference \\(d\\) of an Arithmetic Progression take?",
     ["Positive, negative, or zero",
      "Only positive integers",
      "Only non-zero real numbers",
      "Only rational numbers greater than 1"],
     "A", "OSC", "easy",
     "The common difference \\(d\\) can be positive (increasing AP), negative (decreasing AP), or zero (constant AP)."),

    # 3
    ("Decide whether the sequence \\(2, 4, 6, 8, \\dots\\) is an AP. If so, find the common difference \\(d\\).",
     ["Yes, it is an AP with common difference \\(d = 2\\)",
      "No, it is a geometric progression",
      "Yes, it is an AP with \\(d = 4\\)",
      "No, the difference is not constant"],
     "A", "OSC", "easy",
     "\\(t_2 - t_1 = 4 - 2 = 2\\), \\(t_3 - t_2 = 6 - 4 = 2\\), \\(t_4 - t_3 = 8 - 6 = 2\\). Since the difference between consecutive terms is constant (\\(d = 2\\)), it is an AP."),

    # 4
    ("Decide whether the sequence \\(2, \\frac{5}{2}, 3, \\frac{7}{2}, \\dots\\) is an AP.",
     ["Yes, it is an AP with common difference \\(d = \\frac{1}{2}\\)",
      "No, because fractions cannot form an AP",
      "Yes, it is an AP with \\(d = 1\\)",
      "No, the differences vary"],
     "A", "OSC", "easy",
     "\\(5/2 - 2 = 1/2\\), \\(3 - 5/2 = 1/2\\), \\(7/2 - 3 = 1/2\\). The difference is constant \\(d = 1/2\\), so it is an AP."),

    # 5
    ("Decide whether \\(-10, -6, -2, 2, \\dots\\) is an AP.",
     ["Yes, it is an AP with common difference \\(d = 4\\)",
      "Yes, it is an AP with \\(d = -4\\)",
      "No, because terms switch from negative to positive",
      "No, it is not an AP"],
     "A", "OSC", "easy",
     "\\(-6 - (-10) = 4\\), \\(-2 - (-6) = 4\\), \\(2 - (-2) = 4\\). The common difference is constant \\(d = 4\\), so it is an AP."),

    # 6
    ("Decide whether \\(0.3, 0.33, 0.333, \\dots\\) is an AP.",
     ["No, because the difference \\(t_{n+1} - t_n\\) is not constant",
      "Yes, it is an AP with \\(d = 0.03\\)",
      "Yes, it is an AP with \\(d = 0.3\\)",
      "Yes, because all terms contain 3"],
     "A", "OSC", "easy",
     "\\(0.33 - 0.3 = 0.03\\), whereas \\(0.333 - 0.33 = 0.003\\). Since \\(0.03 \\neq 0.003\\), the difference is not constant, so it is NOT an AP."),

    # 7
    ("Decide whether \\(0, -4, -8, -12, \\dots\\) is an AP.",
     ["Yes, it is an AP with common difference \\(d = -4\\)",
      "Yes, it is an AP with \\(d = 4\\)",
      "No, because it starts with 0",
      "No, because terms are negative"],
     "A", "OSC", "easy",
     "\\(-4 - 0 = -4\\), \\(-8 - (-4) = -4\\), \\(-12 - (-8) = -4\\). The difference is constant \\(d = -4\\), so it is an AP."),

    # 8
    ("Decide whether \\(-\\frac{1}{5}, -\\frac{1}{5}, -\\frac{1}{5}, \\dots\\) is an AP.",
     ["Yes, it is a constant AP with common difference \\(d = 0\\)",
      "No, because the terms do not change",
      "No, because zero cannot be a difference",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(-1/5 - (-1/5) = 0\\). The difference is constant \\(d = 0\\). A sequence of identical numbers is indeed an AP with \\(d = 0\\)."),

    # 9
    ("Decide whether \\(3, 3 + \\sqrt{2}, 3 + 2\\sqrt{2}, 3 + 3\\sqrt{2}, \\dots\\) is an AP.",
     ["Yes, it is an AP with common difference \\(d = \\sqrt{2}\\)",
      "No, because terms contain irrational square roots",
      "Yes, it is an AP with \\(d = 3\\)",
      "No, the difference changes"],
     "A", "OSC", "medium",
     "\\((3 + \\sqrt{2}) - 3 = \\sqrt{2}\\), \\((3 + 2\\sqrt{2}) - (3 + \\sqrt{2}) = \\sqrt{2}\\), \\((3 + 3\\sqrt{2}) - (3 + 2\\sqrt{2}) = \\sqrt{2}\\). The difference is constant \\(d = \\sqrt{2}\\), so it is an AP."),

    # 10
    ("Decide whether \\(127, 132, 137, \\dots\\) is an AP.",
     ["Yes, it is an AP with common difference \\(d = 5\\)",
      "No, the difference is not constant",
      "Yes, with \\(d = 10\\)",
      "No, because terms are three-digit numbers"],
     "A", "OSC", "easy",
     "\\(132 - 127 = 5\\) and \\(137 - 132 = 5\\). Constant difference \\(d = 5\\), so it is an AP."),

    # 11
    ("Write an AP whose first term is \\(a = 10\\) and common difference is \\(d = 5\\).",
     ["\\(10, 15, 20, 25, \\dots\\)",
      "\\(10, 50, 250, \\dots\\)",
      "\\(5, 10, 15, 20, \\dots\\)",
      "\\(10, 20, 30, 40, \\dots\\)"],
     "A", "OSC", "easy",
     "\\(t_1 = 10\\), \\(t_2 = 10 + 5 = 15\\), \\(t_3 = 15 + 5 = 20\\), \\(t_4 = 20 + 5 = 25\\)."),

    # 12
    ("Write an AP whose first term is \\(a = -3\\) and common difference is \\(d = 0\\).",
     ["\\(-3, -3, -3, -3, \\dots\\)",
      "\\(-3, 0, 3, 6, \\dots\\)",
      "\\(0, -3, -6, \\dots\\)",
      "\\(-3, 3, -3, 3, \\dots\\)"],
     "A", "OSC", "easy",
     "Each subsequent term is \\(-3 + 0 = -3\\). The AP is \\(-3, -3, -3, -3, \\dots\\)."),

    # 13
    ("Write an AP whose first term is \\(a = -7\\) and common difference is \\(d = \\frac{1}{2}\\).",
     ["\\(-7, -\\frac{13}{2}, -6, -\\frac{11}{2}, \\dots\\)",
      "\\(-7, -\\frac{15}{2}, -8, \\dots\\)",
      "\\(-7, 7.5, 8, \\dots\\)",
      "\\(-7, -14, -21, \\dots\\)"],
     "A", "OSC", "medium",
     "\\(t_1 = -7\\), \\(t_2 = -7 + 0.5 = -6.5 = -13/2\\), \\(t_3 = -6.5 + 0.5 = -6\\), \\(t_4 = -6 + 0.5 = -5.5 = -11/2\\)."),

    # 14
    ("Write an AP whose first term is \\(a = -1.25\\) and common difference is \\(d = 3\\).",
     ["\\(-1.25, 1.75, 4.75, 7.75, \\dots\\)",
      "\\(-1.25, -4.25, -7.25, \\dots\\)",
      "\\(-1.25, 3, 6, \\dots\\)",
      "\\(3, 1.75, 0.5, \\dots\\)"],
     "A", "OSC", "easy",
     "\\(t_1 = -1.25\\), \\(t_2 = -1.25 + 3 = 1.75\\), \\(t_3 = 1.75 + 3 = 4.75\\), \\(t_4 = 4.75 + 3 = 7.75\\)."),

    # 15
    ("Find the first term \\(a\\) and common difference \\(d\\) for the AP: \\(5, 1, -3, -7, \\dots\\).",
     ["\\(a = 5, d = -4\\)", "\\(a = 5, d = 4\\)", "\\(a = 1, d = -4\\)", "\\(a = -7, d = 4\\)"],
     "A", "OSC", "easy",
     "First term \\(a = 5\\). Common difference \\(d = 1 - 5 = -4\\)."),

    # 16
    ("Find \\(a\\) and \\(d\\) for the AP: \\(0.6, 0.9, 1.2, 1.5, \\dots\\).",
     ["\\(a = 0.6, d = 0.3\\)", "\\(a = 0.6, d = 0.03\\)", "\\(a = 0.9, d = 0.3\\)", "\\(a = 0.6, d = 0.6\\)"],
     "A", "OSC", "easy",
     "\\(a = 0.6\\), \\(d = 0.9 - 0.6 = 0.3\\)."),

    # 17
    ("Find \\(a\\) and \\(d\\) for the AP: \\(127, 135, 143, 151, \\dots\\).",
     ["\\(a = 127, d = 8\\)", "\\(a = 127, d = -8\\)", "\\(a = 135, d = 8\\)", "\\(a = 127, d = 7\\)"],
     "A", "OSC", "easy",
     "\\(a = 127\\), \\(d = 135 - 127 = 8\\)."),

    # 18
    ("Find \\(a\\) and \\(d\\) for the AP: \\(\\frac{1}{4}, \\frac{3}{4}, \\frac{5}{4}, \\frac{7}{4}, \\dots\\).",
     ["\\(a = \\frac{1}{4}, d = \\frac{1}{2}\\)",
      "\\(a = \\frac{1}{4}, d = \\frac{3}{4}\\)",
      "\\(a = \\frac{1}{4}, d = \\frac{1}{4}\\)",
      "\\(a = \\frac{3}{4}, d = \\frac{1}{2}\\)"],
     "A", "OSC", "easy",
     "\\(a = 1/4\\), \\(d = 3/4 - 1/4 = 2/4 = 1/2\\)."),

    # 19
    ("Is the sequence of natural numbers \\(1, 2, 3, 4, \\dots\\) an AP?",
     ["Yes, with first term \\(a = 1\\) and common difference \\(d = 1\\)",
      "No, it is not an AP",
      "Yes, with \\(d = 2\\)",
      "Only for prime numbers"],
     "A", "OSC", "easy",
     "Consecutive natural numbers differ by 1. Thus it is an AP with \\(a = 1, d = 1\\)."),

    # 20
    ("Is the sequence of odd natural numbers \\(1, 3, 5, 7, \\dots\\) an AP?",
     ["Yes, with \\(a = 1\\) and \\(d = 2\\)",
      "No, it is a geometric series",
      "Yes, with \\(d = 1\\)",
      "No, odd numbers cannot form an AP"],
     "A", "OSC", "easy",
     "\\(3 - 1 = 2, 5 - 3 = 2, 7 - 5 = 2\\). Common difference is 2, so it is an AP."),

    # 21
    ("Is the sequence of even natural numbers \\(2, 4, 6, 8, \\dots\\) an AP?",
     ["Yes, with \\(a = 2\\) and \\(d = 2\\)",
      "No, it is not an AP",
      "Yes, with \\(d = 4\\)",
      "No, because 2 is prime"],
     "A", "OSC", "easy",
     "Consecutive even integers differ by 2. Thus it is an AP with \\(a = 2, d = 2\\)."),

    # 22
    ("Which of the following sequences is NOT an AP?",
     ["\\(1, 4, 9, 16, \\dots\\) (squares of natural numbers)",
      "\\(1, 4, 7, 10, \\dots\\)",
      "\\(10, 20, 30, 40, \\dots\\)",
      "\\(-5, 0, 5, 10, \\dots\\)"],
     "A", "OSC", "easy",
     "\\(4 - 1 = 3\\), whereas \\(9 - 4 = 5\\). Differences are not constant, so square numbers do NOT form an AP."),

    # 23
    ("Which of the following sequences is an AP?",
     ["\\(1, -1, -3, -5, \\dots\\)",
      "\\(1, 2, 4, 8, \\dots\\)",
      "\\(1, 3, 9, 27, \\dots\\)",
      "\\(2, 3, 5, 7, \\dots\\) (prime numbers)"],
     "A", "OSC", "easy",
     "In \\(1, -1, -3, -5\\): \\(-1 - 1 = -2\\), \\(-3 - (-1) = -2\\), \\(-5 - (-3) = -2\\). The difference is constant \\(d = -2\\)."),

    # 24
    ("If \\(k, 2k - 1, 2k + 1\\) are three consecutive terms of an AP, find \\(k\\).",
     ["3", "2", "4", "1"],
     "A", "OSC", "medium",
     "In an AP, \\(t_2 - t_1 = t_3 - t_2 \\implies (2k - 1) - k = (2k + 1) - (2k - 1) \\implies k - 1 = 2 \\implies k = 3\\)."),

    # 25
    ("If \\(x, 13, y, 3\\) are in AP, find the values of \\(x\\) and \\(y\\).",
     ["\\(x = 18, y = 8\\)", "\\(x = 16, y = 9\\)", "\\(x = 15, y = 7\\)", "\\(x = 20, y = 10\\)"],
     "A", "OSC", "medium",
     "Here \\(t_2 = 13\\) and \\(t_4 = 3\\). \\(t_4 - t_2 = 2d = 3 - 13 = -10 \\implies d = -5\\). Then \\(x = t_1 = 13 - (-5) = 18\\), and \\(y = t_3 = 13 + (-5) = 8\\)."),

    # 26
    ("If the common difference \\(d = 0\\), what is the sequence called?",
     ["A constant sequence", "A geometric progression", "A divergent sequence", "An invalid sequence"],
     "A", "OSC", "easy",
     "When \\(d = 0\\), all terms are identical: \\(a, a, a, a, \\dots\\). It is termed a constant AP."),

    # 27
    ("What is the next term in the AP: \\(\\sqrt{2}, \\sqrt{8}, \\sqrt{18}, \\sqrt{32}, \\dots\\)?",
     ["\\(\\sqrt{50}\\)", "\\(\\sqrt{40}\\)", "\\(\\sqrt{48}\\)", "\\(\\sqrt{64}\\)"],
     "A", "OSC", "medium",
     "Rewriting: \\(\\sqrt{2}, 2\\sqrt{2}, 3\\sqrt{2}, 4\\sqrt{2}, \\dots\\). The common difference is \\(d = \\sqrt{2}\\). The next term is \\(5\\sqrt{2} = \\sqrt{25 \\times 2} = \\sqrt{50}\\)."),

    # 28
    ("What is the next term in the AP: \\(\\sqrt{3}, \\sqrt{12}, \\sqrt{27}, \\dots\\)?",
     ["\\(\\sqrt{48}\\)", "\\(\\sqrt{36}\\)", "\\(\\sqrt{45}\\)", "\\(\\sqrt{54}\\)"],
     "A", "OSC", "medium",
     "Rewriting: \\(\\sqrt{3}, 2\\sqrt{3}, 3\\sqrt{3}, \\dots\\). The next term is \\(4\\sqrt{3} = \\sqrt{16 \\times 3} = \\sqrt{48}\\)."),

    # 29
    ("Find the 4th term of the AP whose \\(n\\)-th term is given by \\(t_n = 3n + 1\\).",
     ["13", "12", "14", "10"],
     "A", "OSC", "easy",
     "\\(t_4 = 3(4) + 1 = 12 + 1 = 13\\)."),

    # 30
    ("Find the common difference of the AP whose \\(n\\)-th term is \\(t_n = 3n + 1\\).",
     ["3", "1", "4", "2"],
     "A", "OSC", "easy",
     "\\(t_1 = 4, t_2 = 7 \\implies d = 7 - 4 = 3\\). (The coefficient of \\(n\\) in \\(t_n = pn + q\\) is always the common difference \\(d = p\\))."),

    # 31
    ("Find the common difference of the AP whose \\(n\\)-th term is \\(t_n = 5 - 2n\\).",
     ["-2", "2", "5", "3"],
     "A", "OSC", "easy",
     "\\(t_1 = 3, t_2 = 1 \\implies d = 1 - 3 = -2\\)."),

    # 32
    ("Find the common difference of the AP whose \\(n\\)-th term is \\(t_n = 7n - 4\\).",
     ["7", "-4", "3", "11"],
     "A", "OSC", "easy",
     "Common difference \\(d = 7\\)."),

    # 33
    ("What is the first term \\(a\\) of the AP whose \\(n\\)-th term is \\(t_n = 4n - 3\\)?",
     ["1", "4", "-3", "7"],
     "A", "OSC", "easy",
     "For \\(n = 1\\): \\(t_1 = 4(1) - 3 = 1\\)."),

    # 34
    ("What is the first term \\(a\\) of the AP whose \\(n\\)-th term is \\(t_n = 2n + 5\\)?",
     ["7", "2", "5", "9"],
     "A", "OSC", "easy",
     "For \\(n = 1\\): \\(t_1 = 2(1) + 5 = 7\\)."),

    # 35
    ("If \\(a, b, c\\) are in AP, what is the relation between them?",
     ["\\(2b = a + c\\) (or \\(b = \\frac{a + c}{2}\\))",
      "\\(b^2 = ac\\)",
      "\\(a + b = c\\)",
      "\\(b = a - c\\)"],
     "A", "OSC", "easy",
     "Since \\(b - a = c - b\\), rearranging gives \\(2b = a + c\\). The middle term \\(b\\) is called the arithmetic mean of \\(a\\) and \\(c\\)."),

    # 36
    ("What is the arithmetic mean of 10 and 20?",
     ["15", "10", "20", "30"],
     "A", "OSC", "easy",
     "Arithmetic mean = \\(\\frac{10 + 20}{2} = 15\\)."),

    # 37
    ("What is the arithmetic mean of 4 and 16?",
     ["10", "8", "12", "14"],
     "A", "OSC", "easy",
     "\\(\\frac{4 + 16}{2} = \\frac{20}{2} = 10\\)."),

    # 38
    ("Find the missing term in the AP: \\(2, \\square, 26\\).",
     ["14", "12", "16", "13"],
     "A", "OSC", "easy",
     "The missing term is the arithmetic mean: \\(\\frac{2 + 26}{2} = \\frac{28}{2} = 14\\)."),

    # 39
    ("Find the missing term in the AP: \\(5, \\square, 15\\).",
     ["10", "12", "8", "9"],
     "A", "OSC", "easy",
     "\\(\\frac{5 + 15}{2} = 10\\)."),

    # 40
    ("Find the missing term in the AP: \\(-4, \\square, 6\\).",
     ["1", "2", "0", "-1"],
     "A", "OSC", "easy",
     "\\(\\frac{-4 + 6}{2} = \\frac{2}{2} = 1\\).")
]

t31_prac = [
    # 41
    ("Is \\(4, 7, 10, 13\\) an AP?", ["Yes, d = 3", "No", "Yes, d = 4", "Yes, d = 2"], "A", "OSC", "easy", "Common diff is 3."),
    # 42
    ("Is \\(10, 7, 4, 1\\) an AP?", ["Yes, d = -3", "No", "Yes, d = 3", "Yes, d = -4"], "A", "OSC", "easy", "Common diff is -3."),
    # 43
    ("Is \\(3, 8, 13, 18\\) an AP?", ["Yes, d = 5", "No", "Yes, d = 3", "Yes, d = 6"], "A", "OSC", "easy", "Common diff is 5."),
    # 44
    ("Is \\(20, 15, 10, 5\\) an AP?", ["Yes, d = -5", "No", "Yes, d = 5", "Yes, d = -10"], "A", "OSC", "easy", "Common diff is -5."),
    # 45
    ("Is \\(1, 5, 9, 13\\) an AP?", ["Yes, d = 4", "No", "Yes, d = 5", "Yes, d = 3"], "A", "OSC", "easy", "Common diff is 4."),
    # 46
    ("Is \\(15, 11, 7, 3\\) an AP?", ["Yes, d = -4", "No", "Yes, d = 4", "Yes, d = -3"], "A", "OSC", "easy", "Common diff is -4."),
    # 47
    ("Is \\(6, 12, 18, 24\\) an AP?", ["Yes, d = 6", "No", "Yes, d = 12", "Yes, d = 4"], "A", "OSC", "easy", "Common diff is 6."),
    # 48
    ("Is \\(30, 24, 18, 12\\) an AP?", ["Yes, d = -6", "No", "Yes, d = 6", "Yes, d = -8"], "A", "OSC", "easy", "Common diff is -6."),
    # 49
    ("Is \\(7, 14, 21, 28\\) an AP?", ["Yes, d = 7", "No", "Yes, d = 14", "Yes, d = 8"], "A", "OSC", "easy", "Common diff is 7."),
    # 50
    ("Is \\(35, 28, 21, 14\\) an AP?", ["Yes, d = -7", "No", "Yes, d = 7", "Yes, d = -8"], "A", "OSC", "easy", "Common diff is -7."),
    # 51
    ("Find next term in AP: 2, 7, 12, 17, ...", ["22", "21", "23", "25"], "A", "OSC", "easy", "17 + 5 = 22."),
    # 52
    ("Find next term in AP: 50, 43, 36, 29, ...", ["22", "23", "21", "20"], "A", "OSC", "easy", "29 - 7 = 22."),
    # 53
    ("Find next term in AP: -8, -5, -2, 1, ...", ["4", "3", "5", "2"], "A", "OSC", "easy", "1 + 3 = 4."),
    # 54
    ("Find next term in AP: 100, 85, 70, 55, ...", ["40", "45", "35", "50"], "A", "OSC", "easy", "55 - 15 = 40."),
    # 55
    ("Find next term in AP: 1.5, 3.0, 4.5, 6.0, ...", ["7.5", "7.0", "8.0", "6.5"], "A", "OSC", "easy", "6.0 + 1.5 = 7.5."),
    # 56
    ("Find next term in AP: -10, -20, -30, -40, ...", ["-50", "-45", "-60", "-35"], "A", "OSC", "easy", "-40 - 10 = -50."),
    # 57
    ("Find AM of 6 and 14.", ["10", "9", "11", "8"], "A", "OSC", "easy", "(6 + 14)/2 = 10."),
    # 58
    ("Find AM of 12 and 28.", ["20", "18", "22", "16"], "A", "OSC", "easy", "(12 + 28)/2 = 20."),
    # 59
    ("Find AM of -5 and 15.", ["5", "10", "0", "-5"], "A", "OSC", "easy", "(-5 + 15)/2 = 5."),
    # 60
    ("Find AM of -10 and -30.", ["-20", "-15", "-25", "-10"], "A", "OSC", "easy", "(-10 - 30)/2 = -20."),
    # 61
    ("Find AM of 25 and 75.", ["50", "45", "55", "60"], "A", "OSC", "easy", "(25 + 75)/2 = 50."),
    # 62
    ("Find AM of 1.2 and 2.8.", ["2.0", "1.8", "2.2", "2.5"], "A", "OSC", "easy", "(1.2 + 2.8)/2 = 2.0."),
    # 63
    ("Find AM of 3/4 and 5/4.", ["1", "1/2", "2", "3/2"], "A", "OSC", "easy", "(8/4)/2 = 1."),
    # 64
    ("If a = 4, d = 3, find t_2.", ["7", "6", "8", "5"], "A", "OSC", "easy", "4 + 3 = 7."),
    # 65
    ("If a = 4, d = 3, find t_3.", ["10", "9", "11", "8"], "A", "OSC", "easy", "7 + 3 = 10."),
    # 66
    ("If a = 12, d = -5, find t_2.", ["7", "8", "6", "17"], "A", "OSC", "easy", "12 - 5 = 7."),
    # 67
    ("If a = 12, d = -5, find t_3.", ["2", "3", "1", "-2"], "A", "OSC", "easy", "7 - 5 = 2."),
    # 68
    ("If a = 0, d = 4, find t_3.", ["8", "4", "12", "6"], "A", "OSC", "easy", "0 + 2(4) = 8."),
    # 69
    ("If a = -15, d = 5, find t_4.", ["0", "-5", "5", "-10"], "A", "OSC", "easy", "-15 + 3(5) = 0."),
    # 70
    ("If a = 100, d = -20, find t_5.", ["20", "0", "40", "-20"], "A", "OSC", "easy", "100 + 4(-20) = 20.")
]

t31_mock = [
    # 71
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0f172a" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Arithmetic Progression Standard</text>
  <text x="170" y="80" fill="#f8fafc" font-size="12" text-anchor="middle">a, a + d, a + 2d, a + 3d, ...</text>
  <text x="170" y="105" fill="#4ade80" font-size="11" text-anchor="middle">Common Difference: d = t_(n+1) - t_n</text>
</svg>
</div>
What is the core defining rule of an Arithmetic Progression?""",
     ["The difference between any term and its immediately preceding term is always a constant value d",
      "Each term is the square of the previous term",
      "Each term is multiplied by a constant ratio",
      "The terms must always increase"],
     "A", "OSC", "easy",
     "An arithmetic progression is uniquely defined by a constant additive increment \\(d\\): each term is obtained by adding \\(d\\) to the preceding term."),

    # 72
    ("In an AP, what does 'a' represent?", ["The first term (t_1)", "The common difference", "The total sum", "The last term"], "A", "OSC", "easy", "By standard convention, \\(a\\) denotes the first term \\(t_1\\)."),
    # 73
    ("In an AP, what does 'd' represent?", ["The common difference (t_(n+1) - t_n)", "The first term", "The number of terms", "The average"], "A", "OSC", "easy", "\\(d\\) denotes the common difference."),
    # 74
    ("If d > 0, the AP is:", ["Strictly increasing", "Strictly decreasing", "Constant", "Oscillating"], "A", "OSC", "easy", "Each subsequent term is greater than the preceding term."),
    # 75
    ("If d < 0, the AP is:", ["Strictly decreasing", "Strictly increasing", "Constant", "Undefined"], "A", "OSC", "easy", "Each subsequent term is smaller than the preceding term."),
    # 76
    ("If d = 0, the AP is:", ["Constant (all terms equal)", "Increasing", "Decreasing", "Alternating"], "A", "OSC", "easy", "All terms remain equal to the first term \\(a\\)."),
    # 77
    ("Can consecutive terms of an AP be negative?", ["Yes, terms can be negative, zero, or positive", "No, AP is only for positive numbers", "Only if d is positive", "Never"], "A", "OSC", "easy", "The terms of an AP can be any real numbers."),
    # 78
    ("What is the common difference of 0, 0, 0, 0, ...?", ["0", "1", "Undefined", "Infinite"], "A", "OSC", "easy", "\\(0 - 0 = 0\\)."),
    # 79
    ("Is 1, 1/2, 1/3, 1/4, ... an AP?", ["No, differences are not constant (it is a Harmonic Progression)", "Yes, d = 1/2", "Yes, d = -1/2", "Yes, d = 1"], "A", "OSC", "easy", "\\(1/2 - 1 = -1/2\\), but \\(1/3 - 1/2 = -1/6 \\neq -1/2\\). Not an AP."),
    # 80
    ("Is 1, -1, 1, -1, ... an AP?", ["No, differences are -2 and +2 (not constant)", "Yes, d = -2", "Yes, d = 0", "Yes, d = -1"], "A", "OSC", "easy", "Differences oscillate between \\(-2\\) and \\(+2\\), not constant."),
    # 81
    ("Find d for AP: 10, 10, 10, 10, ...", ["0", "10", "1", "-10"], "A", "OSC", "easy", "\\(10 - 10 = 0\\)."),
    # 82
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0b132b" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1c2541" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Verification Rule for AP</text>
  <text x="170" y="80" fill="#f8fafc" font-size="11" text-anchor="middle">Compute t2 - t1, t3 - t2, t4 - t3</text>
  <text x="170" y="105" fill="#4ade80" font-size="11" text-anchor="middle">All differences must be IDENTICAL</text>
</svg>
</div>
How is a sequence formally proved to be an Arithmetic Progression?""",
     ["By verifying that t_(n+1) - t_n yields the exact same constant difference for all given consecutive term pairs",
      "By adding all terms together",
      "By checking if the first term is an integer",
      "By graphing the terms on a circle"],
     "A", "OSC", "easy",
     "A sequence is proven to be an AP if and only if the difference \\(t_{k+1} - t_k\\) is constant and independent of \\(k\\) for every consecutive pair.")
]

all_q_31 = build_topic_questions("MH-10-MTH1-3-3.1", t31_exam, t31_prac, t31_mock)
out_31 = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch3_t1.json")
with open(out_31, "w", encoding="utf-8") as f:
    json.dump(all_q_31, f, indent=2, ensure_ascii=False)
print(f"Generated {len(all_q_31)} questions for MH-10-MTH1-3-3.1 -> {out_31}")
