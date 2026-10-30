# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-3-3.4
Topic: Finding Rational Numbers Between Two Rational Numbers
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-3-3.4"

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
    ("How many rational numbers exist between any two distinct rational numbers?",
     ["Infinitely many", "Exactly one", "A finite number depending on the denominator", "Zero"],
     "A", "OSC", "easy",
     "By the density property of rational numbers, between any two distinct rational numbers there exist infinitely many other rational numbers."),

    # 2
    ("If \\(a\\) and \\(b\\) are two rational numbers with \\(a < b\\), which formula always gives a rational number strictly between them?",
     ["\\(\\frac{a + b}{2}\\)", "\\(\\frac{a - b}{2}\\)", "\\(a \\times b\\)", "\\(\\frac{a}{b}\\)"],
     "A", "OSC", "easy",
     "The arithmetic mean \\(\\frac{a + b}{2}\\) represents the midpoint of the interval \\([a, b]\\), satisfying \\(a < \\frac{a + b}{2} < b\\)."),

    # 3
    ("Find a rational number halfway between \\(\\frac{1}{4}\\) and \\(\\frac{1}{2}\\) using the mean method.",
     ["\\(\\frac{3}{8}\\)", "\\(\\frac{2}{6} = \\frac{1}{3}\\)", "\\(\\frac{1}{8}\\)", "\\(\\frac{5}{8}\\)"],
     "A", "OSC", "easy",
     "Mean = \\(\\frac{1/4 + 1/2}{2} = \\frac{1/4 + 2/4}{2} = \\frac{3/4}{2} = \\frac{3}{8}\\)."),

    # 4
    ("Find a rational number strictly between \\(-2\\) and \\(0\\).",
     ["-1", "-2", "0", "1"],
     "A", "OSC", "easy",
     "The integer -1 lies strictly between -2 and 0 (mean = \\(\\frac{-2 + 0}{2} = -1\\))."),

    # 5
    ("Which of the following rational numbers lies between \\(\\frac{2}{3}\\) and \\(\\frac{4}{5}\\)?",
     ["\\(\\frac{11}{15}\\)", "\\(\\frac{3}{4}\\)", "\\(\\frac{7}{10}\\)", "\\(\\frac{13}{15}\\)"],
     "A", "OSC", "medium",
     "Convert to common denominator 15: \\(\\frac{2}{3} = \\frac{10}{15}\\) and \\(\\frac{4}{5} = \\frac{12}{15}\\). The number \\(\\frac{11}{15}\\) lies strictly between \\(\\frac{10}{15}\\) and \\(\\frac{12}{15}\\)."),

    # 6
    ("To find 5 rational numbers between \\(\\frac{-2}{5}\\) and \\(\\frac{1}{2}\\), what is the most convenient common denominator?",
     ["20 (or any multiple of 10 like 10, 20, 30)",
      "7", "3", "5"],
     "A", "OSC", "easy",
     "LCM of 5 and 2 is 10. Expressing with denominator 20: \\(\\frac{-2}{5} = \\frac{-8}{20}\\) and \\(\\frac{1}{2} = \\frac{10}{20}\\), which provides 17 intermediate integers (from -7 to +9)."),

    # 7
    ("Which of the following rational numbers lies between \\(\\frac{-5}{6}\\) and \\(\\frac{5}{8}\\)?",
     ["0", "-1", "1", "\\(\\frac{7}{8}\\)"],
     "A", "OSC", "easy",
     "Since \\(-\\frac{5}{6} < 0 < \\frac{5}{8}\\), zero lies strictly between this negative and positive rational number."),

    # 8
    ("Find three rational numbers between \\(-2\\) and \\(-1\\).",
     ["\\(-\\frac{7}{4}, -\\frac{6}{4}, -\\frac{5}{4}\\)",
      "\\(-3, -4, -5\\)",
      "\\(0, 1, 2\\)",
      "\\(-\\frac{9}{4}, -\\frac{8}{4}, -\\frac{7}{4}\\)"],
     "A", "OSC", "medium",
     "Write \\(-2 = -\\frac{8}{4}\\) and \\(-1 = -\\frac{4}{4}\\). Intermediate numbers are \\(-\\frac{7}{4}, -\\frac{6}{4} = -\\frac{3}{2}, -\\frac{5}{4}\\)."),

    # 9
    ("Which of the following rational numbers does NOT lie between \\(\\frac{1}{3}\\) and \\(\\frac{1}{2}\\)?",
     ["\\(\\frac{1}{5}\\)", "\\(\\frac{5}{12}\\)", "\\(\\frac{9}{24}\\)", "\\(\\frac{7}{18}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{1}{3} \\approx 0.333\\) and \\(\\frac{1}{2} = 0.5\\). Here \\(\\frac{1}{5} = 0.2 < 0.333\\), so \\(\\frac{1}{5}\\) does not lie in the interval."),

    # 10
    ("Find a rational number between \\(\\frac{3}{5}\\) and \\(\\frac{4}{5}\\).",
     ["\\(\\frac{7}{10}\\)", "\\(\\frac{1}{5}\\)", "\\(\\frac{9}{10}\\)", "\\(1\\)"],
     "A", "OSC", "easy",
     "Multiply by 2/2: \\(\\frac{3}{5} = \\frac{6}{10}\\) and \\(\\frac{4}{5} = \\frac{8}{10}\\). The intermediate number is \\(\\frac{7}{10}\\)."),

    # 11
    ("Find 3 rational numbers between \\(\\frac{1}{4}\\) and \\(\\frac{3}{4}\\).",
     ["\\(\\frac{3}{8}, \\frac{4}{8}, \\frac{5}{8}\\)",
      "\\(\\frac{1}{8}, \\frac{2}{8}, \\frac{3}{8}\\)",
      "\\(\\frac{5}{8}, \\frac{6}{8}, \\frac{7}{8}\\)",
      "\\(1, 2, 3\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{1}{4} = \\frac{2}{8}\\) and \\(\\frac{3}{4} = \\frac{6}{8}\\). The numbers between them are \\(\\frac{3}{8}, \\frac{4}{8} = \\frac{1}{2}, \\frac{5}{8}\\)."),

    # 12
    ("What is the arithmetic mean of \\(\\frac{-3}{5}\\) and \\(\\frac{1}{5}\\)?",
     ["\\(-\\frac{1}{5}\\)", "\\(-\\frac{2}{5}\\)", "0", "\\(\\frac{1}{5}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{-3/5 + 1/5}{2} = \\frac{-2/5}{2} = -\\frac{1}{5}\\)."),

    # 13
    ("Find a rational number between \\(\\frac{-1}{3}\\) and \\(\\frac{1}{2}\\).",
     ["\\(\\frac{1}{12}\\)", "\\(-\\frac{5}{12}\\)", "\\(\\frac{7}{12}\\)", "-1"],
     "A", "OSC", "easy",
     "Mean = \\(\\frac{-1/3 + 1/2}{2} = \\frac{-2/6 + 3/6}{2} = \\frac{1/6}{2} = \\frac{1}{12}\\)."),

    # 14
    ("Find 5 rational numbers between \\(\\frac{2}{3}\\) and \\(\\frac{4}{5}\\). Using denominator 30:",
     ["\\(\\frac{21}{30}, \\frac{22}{30}, \\frac{23}{30}\\)",
      "\\(\\frac{15}{30}, \\frac{16}{30}, \\frac{17}{30}\\)",
      "\\(\\frac{25}{30}, \\frac{26}{30}, \\frac{27}{30}\\)",
      "\\(\\frac{1}{30}, \\frac{2}{30}, \\frac{3}{30}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{2}{3} = \\frac{20}{30}\\) and \\(\\frac{4}{5} = \\frac{24}{30}\\). The intermediate numbers include \\(\\frac{21}{30}, \\frac{22}{30}, \\frac{23}{30}\\)."),

    # 15
    ("Which of the following rational numbers lies between \\(-1\\) and \\(0\\)?",
     ["\\(-\\frac{3}{5}\\)", "\\(-\\frac{5}{3}\\)", "\\(\\frac{1}{2}\\)", "-2"],
     "A", "OSC", "easy",
     "\\(-1 < -\\frac{3}{5} = -0.6 < 0\\)."),

    # 16
    ("How many integers exist between \\(-3\\) and \\(3\\)?",
     ["5 integers (-2, -1, 0, 1, 2)", "Infinitely many", "6 integers", "7 integers"],
     "A", "OSC", "easy",
     "Unlike rational numbers which are infinitely dense, integers are discrete. Between -3 and 3 there are exactly 5 integers: -2, -1, 0, 1, 2."),

    # 17
    ("Why is the statement 'there are 3 numbers between 2 and 5' ambiguous?",
     ["Because while there are exactly 2 integers (3 and 4), there are infinitely many rational numbers",
      "Because 2 and 5 cannot be compared",
      "Because 5 is a prime number",
      "Because zero is not included"],
     "A", "OSC", "easy",
     "Between 2 and 5, there are only two integers (3 and 4), but there are an infinite number of rational and real numbers."),

    # 18
    ("Find a rational number between \\(\\frac{1}{8}\\) and \\(\\frac{1}{4}\\).",
     ["\\(\\frac{3}{16}\\)", "\\(\\frac{1}{16}\\)", "\\(\\frac{5}{16}\\)", "\\(\\frac{1}{6}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{1}{8} = \\frac{2}{16}\\) and \\(\\frac{1}{4} = \\frac{4}{16}\\). The intermediate fraction is \\(\\frac{3}{16}\\)."),

    # 19
    ("Find a rational number between \\(\\frac{-3}{4}\\) and \\(\\frac{-1}{2}\\).",
     ["\\(-\\frac{5}{8}\\)", "\\(-\\frac{3}{8}\\)", "\\(-\\frac{7}{8}\\)", "\\(-\\frac{1}{8}\\)"],
     "A", "OSC", "easy",
     "\\(-\\frac{3}{4} = -\\frac{6}{8}\\) and \\(-\\frac{1}{2} = -\\frac{4}{8}\\). The number halfway between them is \\(-\\frac{5}{8}\\)."),

    # 20
    ("Find the mean of \\(\\frac{3}{8}\\) and \\(\\frac{5}{8}\\).",
     ["\\(\\frac{1}{2}\\)", "\\(\\frac{4}{8}\\)", "\\(\\frac{3}{4}\\)", "\\(\\frac{1}{4}\\)"],
     "A", "OSC", "easy",
     "Mean = \\(\\frac{3/8 + 5/8}{2} = \\frac{8/8}{2} = \\frac{1}{2}\\)."),

    # 21
    ("If we need to insert \\(n\\) rational numbers between two integers, a standard method is to convert both integers into fractions with denominator _____.",
     ["\\(n + 1\\)", "\\(n - 1\\)", "\\(n\\)", "\\(2n\\)"],
     "A", "OSC", "easy",
     "Multiplying by \\(n + 1\\) divides the unit interval into \\(n + 1\\) segments, creating exactly \\(n\\) intermediate tick marks."),

    # 22
    ("Insert 10 rational numbers between \\(\\frac{-3}{11}\\) and \\(\\frac{8}{11}\\). Which of the following is one of them?",
     ["0", "-1", "1", "\\(\\frac{9}{11}\\)"],
     "A", "OSC", "easy",
     "Numerators range from -3 to 8, with 10 intermediate integers: -2, -1, 0, 1, 2, 3, 4, 5, 6, 7. Thus 0 (i.e. \\(\\frac{0}{11}\\)) is in the set."),

    # 23
    ("Which rational number lies between \\(0.1\\) and \\(0.2\\)?",
     ["0.15", "0.25", "0.05", "0.3"],
     "A", "OSC", "easy",
     "\\(0.1 < 0.15 = \\frac{3}{20} < 0.2\\)."),

    # 24
    ("Which rational number lies between \\(\\frac{1}{7}\\) and \\(\\frac{2}{7}\\)?",
     ["\\(\\frac{3}{14}\\)", "\\(\\frac{1}{14}\\)", "\\(\\frac{5}{14}\\)", "\\(\\frac{4}{7}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{1}{7} = \\frac{2}{14}\\) and \\(\\frac{2}{7} = \\frac{4}{14}\\). The intermediate fraction is \\(\\frac{3}{14}\\)."),

    # 25
    ("Which rational number lies between \\(-\\frac{1}{5}\\) and \\(-\\frac{2}{5}\\)?",
     ["\\(-\\frac{3}{10}\\)", "\\(-\\frac{1}{10}\\)", "\\(-\\frac{5}{10}\\)", "\\(\\frac{3}{10}\\)"],
     "A", "OSC", "easy",
     "\\(-\\frac{2}{5} = -\\frac{4}{10}\\) and \\(-\\frac{1}{5} = -\\frac{2}{10}\\). The intermediate fraction is \\(-\\frac{3}{10}\\)."),

    # 26
    ("Find the mean of \\(\\frac{-2}{3}\\) and \\(\\frac{-1}{3}\\).",
     ["\\(-\\frac{1}{2}\\)", "\\(-\\frac{3}{6}\\)", "\\(-\\frac{1}{6}\\)", "\\(-\\frac{5}{6}\\)"],
     "A", "OSC", "easy",
     "Mean = \\(\\frac{-2/3 + (-1/3)}{2} = \\frac{-3/3}{2} = -\\frac{1}{2}\\)."),

    # 27
    ("Which of the following numbers lies between \\(\\frac{3}{4}\\) and \\(1\\)?",
     ["\\(\\frac{7}{8}\\)", "\\(\\frac{5}{8}\\)", "\\(\\frac{1}{2}\\)", "\\(\\frac{9}{8}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{3}{4} = \\frac{6}{8}\\) and \\(1 = \\frac{8}{8}\\). The number \\(\\frac{7}{8}\\) lies strictly between them."),

    # 28
    ("Which number lies between \\(0\\) and \\(\\frac{1}{10}\\)?",
     ["\\(\\frac{1}{20}\\)", "\\(\\frac{1}{5}\\)", "\\(\\frac{3}{10}\\)", "\\(-\\frac{1}{20}\\)"],
     "A", "OSC", "easy",
     "\\(0 < \\frac{1}{20} = 0.05 < \\frac{1}{10} = 0.1\\)."),

    # 29
    ("What is the arithmetic mean of \\(a\\) and \\(b\\) if \\(a = \\frac{1}{3}\\) and \\(b = \\frac{1}{5}\\)?",
     ["\\(\\frac{4}{15}\\)", "\\(\\frac{8}{15}\\)", "\\(\\frac{2}{15}\\)", "\\(\\frac{1}{4}\\)"],
     "A", "OSC", "medium",
     "\\(a + b = \\frac{5 + 3}{15} = \\frac{8}{15}\\). The mean is \\(\\frac{8/15}{2} = \\frac{4}{15}\\)."),

    # 30
    ("What is the arithmetic mean of \\(\\frac{-5}{7}\\) and \\(\\frac{-1}{7}\\)?",
     ["\\(-\\frac{3}{7}\\)", "\\(-\\frac{4}{7}\\)", "\\(-\\frac{2}{7}\\)", "\\(-\\frac{6}{7}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{-5/7 + (-1/7)}{2} = \\frac{-6/7}{2} = -\\frac{3}{7}\\)."),

    # 31
    ("Find three rational numbers between \\(0\\) and \\(0.1\\).",
     ["\\(0.02, 0.05, 0.08\\)", "\\(0.2, 0.5, 0.8\\)", "\\(-0.01, 0.02, 0.05\\)", "\\(0.11, 0.12, 0.13\\)"],
     "A", "OSC", "easy",
     "All three values lie strictly between 0 and 0.1."),

    # 32
    ("Find a rational number between \\(\\frac{5}{6}\\) and \\(\\frac{7}{8}\\).",
     ["\\(\\frac{41}{48}\\)", "\\(\\frac{39}{48}\\)", "\\(\\frac{43}{48}\\)", "\\(\\frac{12}{14}\\)"],
     "A", "OSC", "medium",
     "Common denominator 48: \\(\\frac{5}{6} = \\frac{40}{48}\\) and \\(\\frac{7}{8} = \\frac{42}{48}\\). The intermediate fraction is \\(\\frac{41}{48}\\)."),

    # 33
    ("Find a rational number between \\(-\\frac{3}{8}\\) and \\(-\\frac{1}{4}\\).",
     ["\\(-\\frac{5}{16}\\)", "\\(-\\frac{7}{16}\\)", "\\(-\\frac{3}{16}\\)", "\\(-\\frac{1}{16}\\)"],
     "A", "OSC", "medium",
     "\\(-\\frac{3}{8} = -\\frac{6}{16}\\) and \\(-\\frac{1}{4} = -\\frac{4}{16}\\). The intermediate fraction is \\(-\\frac{5}{16}\\)."),

    # 34
    ("Assertion (A): Between any two distinct rational numbers, there are infinitely many rational numbers.\nReason (R): For any two rational numbers \\(a\\) and \\(b\\), their arithmetic mean \\(\\frac{a+b}{2}\\) is always a new rational number between them, and this process can be repeated infinitely.",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "Because taking the mean of endpoints creates a new intermediate rational number indefinitely, the set of rational numbers is dense, proving (A)."),

    # 35
    ("Assertion (A): There is no integer between 3 and 4, but there are infinitely many rational numbers between 3 and 4.\nReason (R): Integers are discrete, whereas rational numbers possess the density property.",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "Consecutive integers differ by 1 with no integers between them, but rational numbers form a dense order on the number line."),

    # 36
    ("True or False: There is a 'next' rational number immediately after \\(\\frac{1}{2}\\).",
     ["False", "True"],
     "A", "OTF", "easy",
     "No rational number has an immediate successor or predecessor because between \\(\\frac{1}{2}\\) and any proposed 'next' number \\(x\\), another rational number \\(\\frac{1/2 + x}{2}\\) always exists."),

    # 37
    ("True or False: The arithmetic mean of two rational numbers is always rational.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Because rational numbers are closed under addition and division by 2 (a non-zero rational), \\(\\frac{a+b}{2}\\) is always rational."),

    # 38
    ("Fill in the blank: The property that between any two rational numbers there are infinitely many rational numbers is called the _____ property.",
     ["density", "closure", "associative", "commutative"],
     "A", "OFB", "easy",
     "This is known as the density property of rational numbers."),

    # 39
    ("Fill in the blank: The midpoint between \\(-a\\) and \\(+a\\) on the number line is always _____.",
     ["0", "1", "\\(a\\)", "\\(2a\\)"],
     "A", "OFB", "easy",
     "\\(\\frac{-a + a}{2} = \\frac{0}{2} = 0\\)."),

    # 40
    ("What is the numerical integer value of \\(\\frac{-6 + 10}{2}\\), the midpoint between \\(-6\\) and \\(10\\)?",
     ["2", "4", "-2", "8"],
     "A", "ONE", "easy",
     "\\(\\frac{-6 + 10}{2} = \\frac{4}{2} = 2\\)."),
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    ("Find the mean of \\(\\frac{1}{2}\\) and \\(\\frac{3}{4}\\).",
     ["\\(\\frac{5}{8}\\)", "\\(\\frac{4}{6}\\)", "\\(\\frac{1}{4}\\)", "\\(\\frac{7}{8}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{2/4 + 3/4}{2} = \\frac{5/4}{2} = \\frac{5}{8}\\)."),

    # 42
    ("Find the mean of \\(-\\frac{1}{2}\\) and \\(\\frac{1}{2}\\).",
     ["0", "1", "-1", "\\(\\frac{1}{4}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{-1/2 + 1/2}{2} = 0\\)."),

    # 43
    ("Find the mean of \\(-\\frac{3}{4}\\) and \\(-\\frac{1}{4}\\).",
     ["\\(-\\frac{1}{2}\\)", "\\(-\\frac{4}{8}\\)", "\\(-\\frac{1}{4}\\)", "0"],
     "A", "OSC", "easy",
     "\\(\\frac{-3/4 - 1/4}{2} = \\frac{-4/4}{2} = -\\frac{1}{2}\\)."),

    # 44
    ("Find a rational number between \\(\\frac{1}{5}\\) and \\(\\frac{1}{3}\\).",
     ["\\(\\frac{4}{15}\\)", "\\(\\frac{2}{15}\\)", "\\(\\frac{1}{4}\\)", "\\(\\frac{7}{15}\\)"],
     "A", "OSC", "easy",
     "Mean = \\(\\frac{3/15 + 5/15}{2} = \\frac{8/15}{2} = \\frac{4}{15}\\)."),

    # 45
    ("Find a rational number between \\(\\frac{2}{7}\\) and \\(\\frac{3}{7}\\).",
     ["\\(\\frac{5}{14}\\)", "\\(\\frac{1}{14}\\)", "\\(\\frac{5}{7}\\)", "\\(\\frac{6}{14}\\)"],
     "A", "OSC", "easy",
     "Mean = \\(\\frac{2/7 + 3/7}{2} = \\frac{5/7}{2} = \\frac{5}{14}\\)."),

    # 46
    ("Find a rational number between \\(-3\\) and \\(-2\\).",
     ["\\(-\\frac{5}{2}\\)", "\\(-\\frac{7}{2}\\)", "\\(-\\frac{3}{2}\\)", "-1"],
     "A", "OSC", "easy",
     "\\(\\frac{-3 + (-2)}{2} = -\\frac{5}{2} = -2.5\\)."),

    # 47
    ("Find a rational number between \\(0\\) and \\(1\\).",
     ["\\(\\frac{1}{2}\\)", "1", "0", "2"],
     "A", "OSC", "easy",
     "\\(\\frac{0 + 1}{2} = \\frac{1}{2}\\)."),

    # 48
    ("Find 2 rational numbers between \\(\\frac{1}{3}\\) and \\(\\frac{2}{3}\\). Using denominator 9:",
     ["\\(\\frac{4}{9}, \\frac{5}{9}\\)", "\\(\\frac{1}{9}, \\frac{2}{9}\\)", "\\(\\frac{7}{9}, \\frac{8}{9}\\)", "\\(\\frac{2}{9}, \\frac{4}{9}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{1}{3} = \\frac{3}{9}\\) and \\(\\frac{2}{3} = \\frac{6}{9}\\). Intermediate numbers are \\(\\frac{4}{9}\\) and \\(\\frac{5}{9}\\)."),

    # 49
    ("Find 3 rational numbers between \\(\\frac{-1}{2}\\) and \\(\\frac{1}{2}\\).",
     ["\\(-\\frac{1}{4}, 0, \\frac{1}{4}\\)",
      "\\(-1, 0, 1\\)",
      "\\(-\\frac{3}{4}, 0, \\frac{3}{4}\\)",
      "\\(-\\frac{1}{2}, 0, \\frac{1}{2}\\)"],
     "A", "OSC", "easy",
     "All three points lie strictly inside \\((-0.5, 0.5)\\)."),

    # 50
    ("Find 4 rational numbers between \\(\\frac{3}{5}\\) and \\(\\frac{4}{5}\\). Using denominator 25:",
     ["\\(\\frac{16}{25}, \\frac{17}{25}, \\frac{18}{25}, \\frac{19}{25}\\)",
      "\\(\\frac{11}{25}, \\frac{12}{25}, \\frac{13}{25}, \\frac{14}{25}\\)",
      "\\(\\frac{21}{25}, \\frac{22}{25}, \\frac{23}{25}, \\frac{24}{25}\\)",
      "\\(\\frac{1}{25}, \\frac{2}{25}, \\frac{3}{25}, \\frac{4}{25}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{3}{5} = \\frac{15}{25}\\) and \\(\\frac{4}{5} = \\frac{20}{25}\\). Intermediate fractions are \\(\\frac{16}{25}, \\frac{17}{25}, \\frac{18}{25}, \\frac{19}{25}\\)."),

    # 51
    ("Find 5 rational numbers between \\(-1\\) and \\(0\\).",
     ["\\(-\\frac{5}{6}, -\\frac{4}{6}, -\\frac{3}{6}, -\\frac{2}{6}, -\\frac{1}{6}\\)",
      "\\(-1, -2, -3, -4, -5\\)",
      "\\(0, 1, 2, 3, 4\\)",
      "\\(-\\frac{7}{6}, -\\frac{8}{6}, -\\frac{9}{6}, -\\frac{10}{6}, -\\frac{11}{6}\\)"],
     "A", "OSC", "medium",
     "Write \\(-1 = -\\frac{6}{6}\\) and \\(0 = \\frac{0}{6}\\). Intermediate numerators are -5, -4, -3, -2, -1."),

    # 52
    ("Which of the following is between \\(\\frac{1}{10}\\) and \\(\\frac{2}{10}\\)?",
     ["\\(\\frac{3}{20}\\)", "\\(\\frac{1}{20}\\)", "\\(\\frac{5}{20}\\)", "\\(\\frac{7}{20}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{1}{10} = \\frac{2}{20}\\) and \\(\\frac{2}{10} = \\frac{4}{20}\\). Intermediate is \\(\\frac{3}{20}\\)."),

    # 53
    ("Which of the following is between \\(\\frac{-2}{7}\\) and \\(\\frac{-1}{7}\\)?",
     ["\\(-\\frac{3}{14}\\)", "\\(-\\frac{1}{14}\\)", "\\(-\\frac{5}{14}\\)", "\\(\\frac{3}{14}\\)"],
     "A", "OSC", "easy",
     "\\(-\\frac{2}{7} = -\\frac{4}{14}\\) and \\(-\\frac{1}{7} = -\\frac{2}{14}\\). Intermediate is \\(-\\frac{3}{14}\\)."),

    # 54
    ("What is the midpoint between \\(\\frac{2}{9}\\) and \\(\\frac{8}{9}\\)?",
     ["\\(\\frac{5}{9}\\)", "\\(\\frac{6}{9}\\)", "\\(\\frac{4}{9}\\)", "\\(\\frac{10}{9}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{2/9 + 8/9}{2} = \\frac{10/9}{2} = \\frac{5}{9}\\)."),

    # 55
    ("What is the midpoint between \\(-\\frac{7}{11}\\) and \\(\\frac{3}{11}\\)?",
     ["\\(-\\frac{2}{11}\\)", "\\(-\\frac{4}{11}\\)", "\\(-\\frac{5}{11}\\)", "\\(-\\frac{1}{11}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{-7/11 + 3/11}{2} = \\frac{-4/11}{2} = -\\frac{2}{11}\\)."),

    # 56
    ("Find the mean of \\(\\frac{1}{6}\\) and \\(\\frac{1}{4}\\).",
     ["\\(\\frac{5}{24}\\)", "\\(\\frac{2}{10}\\)", "\\(\\frac{1}{5}\\)", "\\(\\frac{7}{24}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{1}{6} + \\frac{1}{4} = \\frac{2 + 3}{12} = \\frac{5}{12}\\). Mean = \\(\\frac{5/12}{2} = \\frac{5}{24}\\)."),

    # 57
    ("Find the mean of \\(-\\frac{1}{3}\\) and \\(-\\frac{1}{4}\\).",
     ["\\(-\\frac{7}{24}\\)", "\\(-\\frac{5}{24}\\)", "\\(-\\frac{1}{7}\\)", "\\(-\\frac{7}{12}\\)"],
     "A", "OSC", "medium",
     "\\(-\\frac{1}{3} - \\frac{1}{4} = -\\frac{7}{12}\\). Mean = \\(-\\frac{7/12}{2} = -\\frac{7}{24}\\)."),

    # 58
    ("Find a rational number between \\(2.5\\) and \\(2.6\\).",
     ["\\(2.55 = \\frac{51}{20}\\)", "\\(2.65\\)", "\\(2.45\\)", "\\(3.0\\)"],
     "A", "OSC", "easy",
     "\\(2.5 < 2.55 < 2.6\\)."),

    # 59
    ("Find a rational number between \\(-0.4\\) and \\(-0.3\\).",
     ["\\(-0.35\\)", "\\(-0.45\\)", "\\(-0.25\\)", "\\(0.35\\)"],
     "A", "OSC", "easy",
     "\\(-0.4 < -0.35 < -0.3\\)."),

    # 60
    ("Which of the following is between \\(\\frac{4}{5}\\) and \\(1\\)?",
     ["\\(\\frac{9}{10}\\)", "\\(\\frac{7}{10}\\)", "\\(\\frac{3}{5}\\)", "\\(\\frac{11}{10}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{4}{5} = \\frac{8}{10}\\) and \\(1 = \\frac{10}{10}\\). Intermediate is \\(\\frac{9}{10}\\)."),

    # 61
    ("Find a rational number between \\(\\frac{-1}{6}\\) and \\(\\frac{1}{6}\\).",
     ["0", "\\(\\frac{1}{3}\\)", "\\(-\\frac{1}{3}\\)", "1"],
     "A", "OSC", "easy",
     "The midpoint of \\(-\\frac{1}{6}\\) and \\(\\frac{1}{6}\\) is 0."),

    # 62
    ("Find a rational number between \\(\\frac{7}{10}\\) and \\(\\frac{8}{10}\\).",
     ["\\(\\frac{15}{20} = \\frac{3}{4}\\)", "\\(\\frac{13}{20}\\)", "\\(\\frac{17}{20}\\)", "\\(\\frac{9}{10}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{7}{10} = \\frac{14}{20}\\) and \\(\\frac{8}{10} = \\frac{16}{20}\\). Intermediate is \\(\\frac{15}{20} = \\frac{3}{4}\\)."),

    # 63
    ("Which of the following numbers lies between \\(\\frac{-3}{5}\\) and \\(\\frac{-2}{5}\\)?",
     ["\\(-\\frac{1}{2}\\)", "\\(-\\frac{7}{10}\\)", "\\(-\\frac{3}{10}\\)", "\\(-\\frac{1}{5}\\)"],
     "A", "OSC", "easy",
     "\\(-\\frac{3}{5} = -0.6\\) and \\(-\\frac{2}{5} = -0.4\\). Midpoint is \\(-0.5 = -\\frac{1}{2}\\)."),

    # 64
    ("Find a rational number between \\(\\frac{5}{12}\\) and \\(\\frac{7}{12}\\).",
     ["\\(\\frac{1}{2}\\)", "\\(\\frac{1}{3}\\)", "\\(\\frac{2}{3}\\)", "\\(\\frac{3}{4}\\)"],
     "A", "OSC", "easy",
     "Intermediate numerator is 6: \\(\\frac{6}{12} = \\frac{1}{2}\\)."),

    # 65
    ("Find a rational number between \\(-\\frac{5}{9}\\) and \\(-\\frac{3}{9}\\).",
     ["\\(-\\frac{4}{9}\\)", "\\(-\\frac{2}{9}\\)", "\\(-\\frac{6}{9}\\)", "0"],
     "A", "OSC", "easy",
     "Intermediate is \\(-\\frac{4}{9}\\)."),

    # 66
    ("True or False: If \\(a < b\\), then \\(a < \\frac{a+b}{2} < b\\).",
     ["True", "False"],
     "A", "OTF", "easy",
     "The arithmetic mean of two distinct numbers always lies strictly between them."),

    # 67
    ("True or False: The number of integers between 1 and 2 is infinite.",
     ["False", "True"],
     "A", "OTF", "easy",
     "There are zero integers between 1 and 2."),

    # 68
    ("Fill in the blank: To find 9 rational numbers between 0 and 1, we write 0 as \\(\\frac{0}{10}\\) and 1 as _____.",
     ["\\(\\frac{10}{10}\\)", "\\(\\frac{9}{10}\\)", "\\(\\frac{1}{10}\\)", "\\(\\frac{100}{10}\\)"],
     "A", "OFB", "easy",
     "Writing \\(1 = \\frac{10}{10}\\) yields the 9 intermediate fractions \\(\\frac{1}{10}, \\frac{2}{10}, \\dots, \\frac{9}{10}\\)."),

    # 69
    ("Fill in the blank: The rational number halfway between \\(\\frac{1}{3}\\) and \\(\\frac{2}{3}\\) is _____.",
     ["\\(\\frac{1}{2}\\)", "\\(\\frac{3}{6}\\)", "\\(\\frac{1}{4}\\)", "\\(\\frac{3}{4}\\)"],
     "A", "OFB", "easy",
     "\\(\\frac{1/3 + 2/3}{2} = \\frac{1}{2}\\)."),

    # 70
    ("What is the numerical integer value of the numerator when the mean of \\(\\frac{1}{4}\\) and \\(\\frac{3}{4}\\) is written in simplest form?",
     ["1", "2", "4", "3"],
     "A", "ONE", "easy",
     "Mean = \\(\\frac{1/4 + 3/4}{2} = \\frac{1}{2}\\). The numerator is 1."),
]

# 12 MOCK / FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">The Arithmetic Mean Method: a &lt; (a+b)/2 &lt; b</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Horizontal Interval line -->
    <line x1="40" y1="75" x2="300" y2="75" stroke="#64748b" stroke-width="3"/>
    <!-- Endpoint a = 1/4 -->
    <circle cx="60" cy="75" r="7" fill="#3b82f6"/>
    <text x="60" y="55" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">a = 1/4</text>
    <!-- Endpoint b = 1/2 -->
    <circle cx="280" cy="75" r="7" fill="#3b82f6"/>
    <text x="280" y="55" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">b = 1/2</text>
    <!-- Midpoint (a+b)/2 = 3/8 -->
    <circle cx="170" cy="75" r="8" fill="#10b981" stroke="#34d399" stroke-width="2"/>
    <text x="170" y="55" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">c₁ = 3/8</text>
    <line x1="170" y1="65" x2="170" y2="85" stroke="#10b981" stroke-width="2"/>
    <!-- Equal distances indicators -->
    <text x="115" y="95" fill="#fde047" font-size="11" text-anchor="middle">dist = 1/8</text>
    <text x="225" y="95" fill="#fde047" font-size="11" text-anchor="middle">dist = 1/8</text>
    <!-- Formula -->
    <text x="170" y="130" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">c₁ = (1/4 + 1/2) / 2 = 3/8</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What rational number lies exactly halfway between \(a = \frac{1}{4}\) and \(b = \frac{1}{2}\)?</p>
</div>""",
     ["\\(\\frac{3}{8}\\)", "\\(\\frac{1}{3}\\)", "\\(\\frac{2}{6}\\)", "\\(\\frac{5}{8}\\)"],
     "A", "OSC", "easy",
     "\\(c_1 = \\frac{1/4 + 2/4}{2} = \\frac{3/4}{2} = \\frac{3}{8}\\)."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Recursive Bisection: Generating Infinite Rationals</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Line -->
    <line x1="30" y1="70" x2="310" y2="70" stroke="#64748b" stroke-width="2.5"/>
    <!-- 0 and 1 -->
    <circle cx="50" cy="70" r="5" fill="#f8fafc"/>
    <text x="50" y="92" fill="#f8fafc" font-size="11" text-anchor="middle">0</text>
    <circle cx="290" cy="70" r="5" fill="#f8fafc"/>
    <text x="290" y="92" fill="#f8fafc" font-size="11" text-anchor="middle">1</text>
    <!-- Generation 1: 1/2 -->
    <circle cx="170" cy="70" r="6" fill="#10b981"/>
    <text x="170" y="55" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">1/2</text>
    <!-- Generation 2: 1/4 and 3/4 -->
    <circle cx="110" cy="70" r="5" fill="#3b82f6"/>
    <text x="110" y="55" fill="#93c5fd" font-size="10" text-anchor="middle">1/4</text>
    <circle cx="230" cy="70" r="5" fill="#3b82f6"/>
    <text x="230" y="55" fill="#93c5fd" font-size="10" text-anchor="middle">3/4</text>
    <!-- Generation 3: 1/8, 3/8, 5/8, 7/8 -->
    <circle cx="80" cy="70" r="3.5" fill="#f59e0b"/>
    <circle cx="140" cy="70" r="3.5" fill="#f59e0b"/>
    <circle cx="200" cy="70" r="3.5" fill="#f59e0b"/>
    <circle cx="260" cy="70" r="3.5" fill="#f59e0b"/>
    <!-- Footnote -->
    <text x="170" y="125" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Every midpoint creates two new subintervals endlessly</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What principle does this recursive branching illustrate?</p>
</div>""",
     ["The density property: infinitely many rational numbers can be generated",
      "That fractions terminate at 1/8",
      "That rational numbers are discrete",
      "That division is commutative"],
     "A", "OSC", "easy",
     "Repeatedly taking midpoints generates an infinite set of unique rational numbers in any interval, demonstrating the density property."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Equivalent Fraction Expansion Method (× 10)</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Step 1: 3/5 and 4/5 -->
    <rect x="25" y="25" width="125" height="40" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="87" y="48" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">3/5  and  4/5</text>
    <!-- Arrow with x10 label -->
    <path d="M 160,45 L 185,45" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="185,40 195,45 185,50" fill="#f59e0b"/>
    <text x="172" y="35" fill="#fbbf24" font-size="10" text-anchor="middle">×10/10</text>
    <!-- Step 2: 30/50 and 40/50 -->
    <rect x="200" y="25" width="120" height="40" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="260" y="48" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">30/50  and  40/50</text>
    <!-- Revealed 9 numbers card -->
    <rect x="35" y="80" width="270" height="45" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="170" y="100" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Revealed 9 intermediate fractions:</text>
    <text x="170" y="116" fill="#e2e8f0" font-size="10" text-anchor="middle">31/50, 32/50, 33/50, 34/50, 35/50, ..., 39/50</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">By scaling \(\frac{3}{5}\) and \(\frac{4}{5}\) by 10, which rational number is immediately revealed between them?</p>
</div>""",
     ["\\(\\frac{35}{50} = \\frac{7}{10}\\)", "\\(\\frac{25}{50}\\)", "\\(\\frac{45}{50}\\)", "\\(\\frac{15}{50}\\)"],
     "A", "OSC", "easy",
     "Scaling gives \\(\\frac{30}{50}\\) and \\(\\frac{40}{50}\\), containing \\(\\frac{35}{50} = \\frac{7}{10}\\)."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Finding Numbers Between -2/5 and 1/2 via Common Denominator 20</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Scale line -->
    <line x1="20" y1="70" x2="320" y2="70" stroke="#64748b" stroke-width="2.5"/>
    <!-- Left: -8/20 -->
    <circle cx="50" cy="70" r="6" fill="#ef4444"/>
    <text x="50" y="55" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">-8/20 (-2/5)</text>
    <!-- Origin: 0 -->
    <circle cx="160" cy="70" r="4" fill="#f8fafc"/>
    <text x="160" y="90" fill="#f8fafc" font-size="11" text-anchor="middle">0 (0/20)</text>
    <!-- Right: +10/20 -->
    <circle cx="280" cy="70" r="6" fill="#10b981"/>
    <text x="280" y="55" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">+10/20 (1/2)</text>
    <!-- Intermediate samples -->
    <text x="95" y="74" fill="#fbbf24" font-size="11" text-anchor="middle">-5/20</text>
    <text x="220" y="74" fill="#fbbf24" font-size="11" text-anchor="middle">+5/20</text>
    <!-- Summary -->
    <text x="170" y="125" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Span contains 17 distinct twentieths from -7/20 to +9/20</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Which of the following rational numbers lies strictly between \(-\frac{2}{5}\) and \(\frac{1}{2}\)?</p>
</div>""",
     ["\\(-\\frac{1}{20}\\)", "\\(-\\frac{9}{20}\\)", "\\(\\frac{11}{20}\\)", "1"],
     "A", "OSC", "easy",
     "\\(-\\frac{2}{5} = -\\frac{8}{20}\\) and \\(\\frac{1}{2} = \\frac{10}{20}\\). \\(-\\frac{1}{20}\\) falls squarely inside this interval."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Comparison of Mean Method vs LCM Scaling</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Method A: Mean Method -->
    <rect x="25" y="25" width="135" height="90" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="92" y="48" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">Mean Method</text>
    <text x="92" y="70" fill="#cbd5e1" font-size="10" text-anchor="middle">c = (a + b) / 2</text>
    <text x="92" y="88" fill="#ffffff" font-size="10" text-anchor="middle">Best for 1-2 numbers</text>
    <text x="92" y="105" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Guaranteed midpoint</text>
    <!-- Method B: LCM Scaling -->
    <rect x="180" y="25" width="135" height="90" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="247" y="48" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">LCM Scaling Method</text>
    <text x="247" y="70" fill="#cbd5e1" font-size="10" text-anchor="middle">Expand to common base</text>
    <text x="247" y="88" fill="#ffffff" font-size="10" text-anchor="middle">Best for 5, 10, 100 Qs</text>
    <text x="247" y="105" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Generates batch list</text>
    <text x="170" y="135" fill="#fbbf24" font-size="10" text-anchor="middle">Both methods rigorously preserve the density property</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Which method is most efficient when asked to find 10 rational numbers between two fractions?</p>
</div>""",
     ["LCM Scaling / Equivalent Fraction method", "Repeated Mean method", "Trial and error division", "Squaring both numbers"],
     "A", "OSC", "easy",
     "LCM scaling produces an entire batch of evenly-spaced rational numbers in a single step, whereas repeated means require 10 sequential midpoint calculations."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Fractional Density Magnification Window</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Macro Interval: 0 to 1 -->
    <line x1="30" y1="35" x2="310" y2="35" stroke="#64748b" stroke-width="2"/>
    <circle cx="50" cy="35" r="4" fill="#f8fafc"/>
    <text x="50" y="25" fill="#f8fafc" font-size="10" text-anchor="middle">0</text>
    <circle cx="290" cy="35" r="4" fill="#f8fafc"/>
    <text x="290" y="25" fill="#f8fafc" font-size="10" text-anchor="middle">1</text>
    <!-- Magnified segment from 0.1 to 0.2 -->
    <rect x="70" y="55" width="200" height="55" rx="6" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
    <text x="170" y="75" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">Zoom: Between 0.1 and 0.2</text>
    <text x="170" y="95" fill="#fde047" font-size="11" text-anchor="middle">0.11, 0.12, 0.13, 0.14, 0.15, ...</text>
    <!-- Banner -->
    <text x="170" y="132" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Infinitely many subdivisions at every scale</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Between \(0.1\) and \(0.2\), how many decimal rational numbers can be formed?</p>
</div>""",
     ["Infinitely many", "Exactly 9", "Exactly 99", "Only 1 (namely 0.15)"],
     "A", "OSC", "easy",
     "By adding decimal places (e.g. 0.101, 0.1001, etc.), infinitely many rational numbers can be created between any two decimals."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Finding Rational Numbers with Negative Endpoints</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Scale line from -2 to -1 -->
    <line x1="30" y1="70" x2="310" y2="70" stroke="#64748b" stroke-width="2.5"/>
    <!-- Left: -2 = -8/4 -->
    <circle cx="60" cy="70" r="6" fill="#ef4444"/>
    <text x="60" y="52" fill="#fca5a5" font-size="12" font-weight="bold" text-anchor="middle">-2 (-8/4)</text>
    <!-- Intermediate ticks: -7/4, -6/4, -5/4 -->
    <circle cx="120" cy="70" r="5" fill="#f59e0b"/>
    <text x="120" y="95" fill="#fde047" font-size="11" text-anchor="middle">-7/4</text>
    <circle cx="180" cy="70" r="5" fill="#f59e0b"/>
    <text x="180" y="95" fill="#fde047" font-size="11" text-anchor="middle">-6/4 (-3/2)</text>
    <circle cx="240" cy="70" r="5" fill="#f59e0b"/>
    <text x="240" y="95" fill="#fde047" font-size="11" text-anchor="middle">-5/4</text>
    <!-- Right: -1 = -4/4 -->
    <circle cx="280" cy="70" r="6" fill="#10b981"/>
    <text x="280" y="52" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">-1 (-4/4)</text>
    <text x="170" y="130" fill="#38bdf8" font-size="11" text-anchor="middle">Numerator range: -8 &lt; {-7, -6, -5} &lt; -4</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Which of the following rational numbers lies between \(-2\) and \(-1\)?</p>
</div>""",
     ["\\(-\\frac{3}{2}\\)", "\\(-\\frac{5}{2}\\)", "\\(-\\frac{1}{2}\\)", "0"],
     "A", "OSC", "easy",
     "\\(-\\frac{3}{2} = -1.5\\), which lies strictly between -2 and -1."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Fractional Midpoint Formula Verification</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Endpoints card -->
    <rect x="35" y="25" width="270" height="40" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="170" y="50" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">Midpoint of 1/3 and 1/5</text>
    <!-- Step by step -->
    <text x="170" y="85" fill="#e2e8f0" font-size="11" text-anchor="middle">Sum = 1/3 + 1/5 = (5 + 3) / 15 = 8/15</text>
    <rect x="80" y="98" width="180" height="30" rx="5" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="118" fill="#6ee7b7" font-size="13" font-weight="bold" text-anchor="middle">Mean = (8/15) ÷ 2 = 4/15</text>
    <text x="170" y="140" fill="#fde047" font-size="10" text-anchor="middle">1/5 (3/15) &lt; 4/15 &lt; 1/3 (5/15)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the arithmetic mean of \(\frac{1}{3}\) and \(\frac{1}{5}\)?</p>
</div>""",
     ["\\(\\frac{4}{15}\\)", "\\(\\frac{8}{15}\\)", "\\(\\frac{2}{15}\\)", "\\(\\frac{1}{4}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{1/3 + 1/5}{2} = \\frac{8/15}{2} = \\frac{4}{15}\\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Consecutive Integer vs Consecutive Rational Fallacy</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Integers: Gap with no elements -->
    <rect x="25" y="25" width="135" height="95" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="92" y="48" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Integers</text>
    <text x="92" y="70" fill="#ffffff" font-size="12" text-anchor="middle">Between 3 and 4:</text>
    <text x="92" y="95" fill="#f87171" font-size="14" font-weight="bold" text-anchor="middle">NO Integers (0)</text>
    <!-- Rationals: Infinite elements -->
    <rect x="180" y="25" width="135" height="95" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="247" y="48" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">Rational Numbers</text>
    <text x="247" y="70" fill="#ffffff" font-size="12" text-anchor="middle">Between 3 and 4:</text>
    <text x="247" y="95" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">INFINITE (∞)</text>
    <text x="170" y="135" fill="#fde047" font-size="11" text-anchor="middle">There is no such concept as 'consecutive rational numbers'</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Why is there no 'next' rational number immediately following \(\frac{3}{4}\)?</p>
</div>""",
     ["Because between \\(\\frac{3}{4}\\) and any other number, another rational number always exists",
      "Because rational numbers only exist as integers",
      "Because fractions cannot be ordered",
      "Because denominator 4 is an even number"],
     "A", "OSC", "easy",
     "Between \\(\\frac{3}{4}\\) and any candidate successor \\(x\\), their midpoint \\(\\frac{3/4 + x}{2}\\) is another rational number closer to \\(\\frac{3}{4}\\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Finding 3 Rationals between 1/4 and 3/4</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Scale line -->
    <line x1="30" y1="70" x2="310" y2="70" stroke="#64748b" stroke-width="2.5"/>
    <circle cx="50" cy="70" r="6" fill="#3b82f6"/>
    <text x="50" y="52" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">1/4 (2/8)</text>
    <!-- intermediate 3/8, 4/8, 5/8 -->
    <circle cx="110" cy="70" r="5" fill="#10b981"/>
    <text x="110" y="95" fill="#6ee7b7" font-size="11" text-anchor="middle">3/8</text>
    <circle cx="170" cy="70" r="5" fill="#10b981"/>
    <text x="170" y="95" fill="#6ee7b7" font-size="11" text-anchor="middle">4/8 (1/2)</text>
    <circle cx="230" cy="70" r="5" fill="#10b981"/>
    <text x="230" y="95" fill="#6ee7b7" font-size="11" text-anchor="middle">5/8</text>
    <circle cx="290" cy="70" r="6" fill="#3b82f6"/>
    <text x="290" y="52" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">3/4 (6/8)</text>
    <text x="170" y="130" fill="#fde047" font-size="11" text-anchor="middle">Converting to eighths reveals 3/8, 4/8, 5/8 evenly</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Which of the following is NOT one of the intermediate eighths between \(\frac{1}{4}\) and \(\frac{3}{4}\)?</p>
</div>""",
     ["\\(\\frac{7}{8}\\)", "\\(\\frac{3}{8}\\)", "\\(\\frac{4}{8}\\)", "\\(\\frac{5}{8}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{7}{8} > \\frac{6}{8} = \\frac{3}{4}\\), so it lies outside the interval to the right."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Rational Numbers between 0 and 0.1</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Scale line -->
    <line x1="30" y1="75" x2="310" y2="75" stroke="#64748b" stroke-width="2.5"/>
    <circle cx="50" cy="75" r="5" fill="#f8fafc"/>
    <text x="50" y="95" fill="#f8fafc" font-size="11" text-anchor="middle">0 (0.00)</text>
    <circle cx="290" cy="75" r="5" fill="#f8fafc"/>
    <text x="290" y="95" fill="#f8fafc" font-size="11" text-anchor="middle">0.1 (0.10)</text>
    <!-- Intermediate points -->
    <circle cx="100" cy="75" r="4" fill="#38bdf8"/>
    <text x="100" y="60" fill="#38bdf8" font-size="10" text-anchor="middle">0.02</text>
    <circle cx="170" cy="75" r="5" fill="#10b981"/>
    <text x="170" y="60" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">0.05 (1/20)</text>
    <circle cx="240" cy="75" r="4" fill="#38bdf8"/>
    <text x="240" y="60" fill="#38bdf8" font-size="10" text-anchor="middle">0.08</text>
    <text x="170" y="130" fill="#fbbf24" font-size="11" text-anchor="middle">0.05 is the exact midpoint between 0 and 0.1</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the midpoint between \(0\) and \(0.1\)?</p>
</div>""",
     ["\\(0.05 = \\frac{1}{20}\\)", "\\(0.5\\)", "\\(0.01\\)", "\\(0.02\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{0 + 0.1}{2} = 0.05 = \\frac{5}{100} = \\frac{1}{20}\\)."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Equivalent Fraction Method Formula Card</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Step cards -->
    <rect x="25" y="25" width="290" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="48" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Finding n Rational Numbers between p/q and r/s</text>
    <text x="170" y="70" fill="#cbd5e1" font-size="11" text-anchor="middle">Step 1: Convert to common denominator LCM(q, s)</text>
    <text x="170" y="90" fill="#6ee7b7" font-size="11" text-anchor="middle">Step 2: Multiply numerator and denominator by (n + 1)</text>
    <text x="170" y="105" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Step 3: List numerators consecutive between scaled bounds</text>
    <text x="170" y="135" fill="#fbbf24" font-size="10" text-anchor="middle">Works universally for positive, negative, and mixed rationals</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">To insert \(9\) rational numbers between two equivalent fractions, by what minimum integer should both be scaled?</p>
</div>""",
     ["10", "9", "8", "2"],
     "A", "OSC", "easy",
     "Multiplying by \\(n + 1 = 9 + 1 = 10\\) creates an interval of length 10 in the numerators, providing exactly 9 intermediate integers.")
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch3_topic4.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
