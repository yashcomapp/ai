# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-2-2.3
Topic: Standard Form (Scientific Notation) for Large & Small Numbers
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-2-2.3"

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
    ("What is the general format of a number expressed in standard form (scientific notation)?",
     ["\\(k \\times 10^n\\), where \\(1.0 \\le k < 10\\) and \\(n\\) is an integer",
      "\\(k \\times 10^n\\), where \\(0 < k < 1\\) and \\(n\\) is an integer",
      "\\(k \\times 10^n\\), where \\(10 \\le k < 100\\)",
      "\\(k \\times n^{10}\\), where \\(k\\) is any real number"],
     "A", "OSC", "easy",
     "A number is in standard form when written as \\(k \\times 10^n\\), where \\(k\\) is a decimal number such that \\(1.0 \\le k < 10\\) and \\(n\\) is any positive or negative integer."),

    # 2
    ("Express \\(0.000035\\) in standard form.",
     ["\\(3.5 \\times 10^{-5}\\)", "\\(3.5 \\times 10^{-4}\\)", "\\(35 \\times 10^{-6}\\)", "\\(0.35 \\times 10^{-4}\\)"],
     "A", "OSC", "easy",
     "Move the decimal point 5 places to the right to obtain 3.5. Since the original number is less than 1, the exponent is negative: \\(3.5 \\times 10^{-5}\\)."),

    # 3
    ("Express \\(4050000\\) in standard form.",
     ["\\(4.05 \\times 10^6\\)", "\\(40.5 \\times 10^5\\)", "\\(4.05 \\times 10^5\\)", "\\(405 \\times 10^4\\)"],
     "A", "OSC", "easy",
     "Move the decimal point 6 places to the left: \\(4050000 = 4.05 \\times 10^6\\)."),

    # 4
    ("Express \\(0.0000000000085\\) in standard form.",
     ["\\(8.5 \\times 10^{-12}\\)", "\\(8.5 \\times 10^{-11}\\)", "\\(85 \\times 10^{-13}\\)", "\\(0.85 \\times 10^{-11}\\)"],
     "A", "OSC", "medium",
     "Moving the decimal point 12 places to the right to place it between 8 and 5 gives \\(8.5 \\times 10^{-12}\\)."),

    # 5
    ("The size of a plant cell is \\(0.00001275\\text{ m}\\). Express this in standard form.",
     ["\\(1.275 \\times 10^{-5}\\text{ m}\\)",
      "\\(1.275 \\times 10^{-4}\\text{ m}\\)",
      "\\(12.75 \\times 10^{-6}\\text{ m}\\)",
      "\\(0.1275 \\times 10^{-4}\\text{ m}\\)"],
     "A", "OSC", "easy",
     "Shifting the decimal point 5 places to the right gives \\(1.275 \\times 10^{-5}\\text{ m}\\)."),

    # 6
    ("The diameter of a red blood cell is \\(0.000007\\text{ m}\\). Express this in standard form.",
     ["\\(7.0 \\times 10^{-6}\\text{ m}\\)",
      "\\(7.0 \\times 10^{-5}\\text{ m}\\)",
      "\\(0.7 \\times 10^{-5}\\text{ m}\\)",
      "\\(70 \\times 10^{-7}\\text{ m}\\)"],
     "A", "OSC", "easy",
     "Moving the decimal point 6 places to the right gives \\(7.0 \\times 10^{-6}\\text{ m}\\)."),

    # 7
    ("The thickness of a sheet of paper is \\(0.0016\\text{ cm}\\). What is this in standard form?",
     ["\\(1.6 \\times 10^{-3}\\text{ cm}\\)",
      "\\(1.6 \\times 10^{-2}\\text{ cm}\\)",
      "\\(16 \\times 10^{-4}\\text{ cm}\\)",
      "\\(0.16 \\times 10^{-2}\\text{ cm}\\)"],
     "A", "OSC", "easy",
     "Moving the decimal point 3 places right gives \\(1.6 \\times 10^{-3}\\text{ cm}\\)."),

    # 8
    ("The charge on an electron is \\(0.00000000000000000016\\text{ C}\\). In scientific notation, this is:",
     ["\\(1.6 \\times 10^{-19}\\text{ C}\\)",
      "\\(1.6 \\times 10^{-18}\\text{ C}\\)",
      "\\(16 \\times 10^{-20}\\text{ C}\\)",
      "\\(0.16 \\times 10^{-18}\\text{ C}\\)"],
     "A", "OSC", "medium",
     "Counting decimal places: moving 19 places to the right places the decimal between 1 and 6, giving \\(1.6 \\times 10^{-19}\\text{ C}\\)."),

    # 9
    ("The distance from the Earth to the Sun is approximately \\(149,600,000,000\\text{ m}\\). In standard form, this is:",
     ["\\(1.496 \\times 10^{11}\\text{ m}\\)",
      "\\(1.496 \\times 10^{10}\\text{ m}\\)",
      "\\(14.96 \\times 10^{10}\\text{ m}\\)",
      "\\(1.496 \\times 10^{12}\\text{ m}\\)"],
     "A", "OSC", "medium",
     "Moving the decimal point 11 places to the left gives \\(1.496 \\times 10^{11}\\text{ m}\\)."),

    # 10
    ("Speed of light in vacuum is \\(300,000,000\\text{ m/s}\\). In standard form, this equals:",
     ["\\(3.0 \\times 10^8\\text{ m/s}\\)",
      "\\(3.0 \\times 10^7\\text{ m/s}\\)",
      "\\(30 \\times 10^7\\text{ m/s}\\)",
      "\\(0.3 \\times 10^9\\text{ m/s}\\)"],
     "A", "OSC", "easy",
     "There are 8 zeros after 3: \\(300,000,000 = 3.0 \\times 10^8\\text{ m/s}\\)."),

    # 11
    ("Express \\(3.02 \\times 10^{-6}\\) in usual ordinary decimal form.",
     ["0.00000302", "0.0000302", "0.000302", "0.000000302"],
     "A", "OSC", "medium",
     "Moving the decimal point 6 places to the left: 1 place moves past 3, followed by 5 preceding zeros: \\(0.00000302\\)."),

    # 12
    ("Express \\(4.5 \\times 10^4\\) in usual form.",
     ["45000", "4500", "450000", "450"],
     "A", "OSC", "easy",
     "Moving the decimal point 4 places right gives \\(45000\\)."),

    # 13
    ("Express \\(1.0001 \\times 10^9\\) in usual form.",
     ["1,000,100,000", "10,001,000,000", "100,010,000", "1,000,000,100"],
     "A", "OSC", "medium",
     "Moving the decimal point 9 places right: 4 digits (0001) take 4 places, followed by 5 additional zeros: \\(1,000,100,000\\)."),

    # 14
    ("Express \\(3.61492 \\times 10^6\\) in usual decimal form.",
     ["3614920", "361492", "36149200", "36149.2"],
     "A", "OSC", "easy",
     "Moving the decimal point 6 places right: 5 digits take 5 places, plus 1 trailing zero: \\(3614920\\)."),

    # 15
    ("Express \\(5.8 \\times 10^{12}\\) in usual form.",
     ["5,800,000,000,000", "58,000,000,000", "580,000,000,000", "5,800,000,000"],
     "A", "OSC", "easy",
     "Moving decimal 12 places right: 1 place for 8, followed by 11 zeros, giving 5.8 trillion (\\(5,800,000,000,000\\))."),

    # 16
    ("Which of the following numbers is properly written in scientific standard form?",
     ["\\(4.82 \\times 10^{-3}\\)", "\\(48.2 \\times 10^{-4}\\)", "\\(0.482 \\times 10^{-2}\\)", "\\(482 \\times 10^{-5}\\)"],
     "A", "OSC", "easy",
     "In standard form, the leading number \\(k\\) must satisfy \\(1.0 \\le k < 10\\). Only \\(4.82\\) satisfies this condition."),

    # 17
    ("Why is \\(0.75 \\times 10^{-4}\\) NOT in standard form?",
     ["Because the coefficient \\(0.75\\) is strictly less than 1.0",
      "Because the exponent is negative",
      "Because 10 is the base",
      "Because 0.75 is a terminating decimal"],
     "A", "OSC", "easy",
     "Standard form requires the coefficient \\(k\\) to be at least 1.0 (\\(1.0 \\le k < 10\\)). Here \\(0.75 < 1.0\\), so the correct standard form is \\(7.5 \\times 10^{-5}\\)."),

    # 18
    ("Why is \\(25.4 \\times 10^6\\) NOT in standard form?",
     ["Because the coefficient \\(25.4\\) is greater than or equal to 10",
      "Because the exponent 6 is positive",
      "Because it contains a decimal point",
      "Because it is an even number"],
     "A", "OSC", "easy",
     "Standard form requires \\(k < 10\\). Here \\(25.4 \\ge 10\\). The correct standard form is \\(2.54 \\times 10^7\\)."),

    # 19
    ("The size of a bacteria is \\(0.0000005\\text{ m}\\). Express in standard form.",
     ["\\(5.0 \\times 10^{-7}\\text{ m}\\)",
      "\\(5.0 \\times 10^{-6}\\text{ m}\\)",
      "\\(0.5 \\times 10^{-6}\\text{ m}\\)",
      "\\(50 \\times 10^{-8}\\text{ m}\\)"],
     "A", "OSC", "easy",
     "Shifting decimal 7 places to the right gives \\(5.0 \\times 10^{-7}\\text{ m}\\)."),

    # 20
    ("Mass of a dust particle is about \\(0.000000000753\\text{ kg}\\). In standard form:",
     ["\\(7.53 \\times 10^{-10}\\text{ kg}\\)",
      "\\(7.53 \\times 10^{-9}\\text{ kg}\\)",
      "\\(75.3 \\times 10^{-11}\\text{ kg}\\)",
      "\\(0.753 \\times 10^{-9}\\text{ kg}\\)"],
     "A", "OSC", "medium",
     "Moving decimal 10 places to the right gives \\(7.53 \\times 10^{-10}\\text{ kg}\\)."),

    # 21
    ("The diameter of a wire on a computer chip is \\(0.000003\\text{ m}\\). In standard form:",
     ["\\(3.0 \\times 10^{-6}\\text{ m}\\)",
      "\\(3.0 \\times 10^{-5}\\text{ m}\\)",
      "\\(30 \\times 10^{-7}\\text{ m}\\)",
      "\\(0.3 \\times 10^{-5}\\text{ m}\\)"],
     "A", "OSC", "easy",
     "Moving decimal 6 places right gives \\(3.0 \\times 10^{-6}\\text{ m}\\)."),

    # 22
    ("Express \\(0.0000000837\\) in standard form.",
     ["\\(8.37 \\times 10^{-8}\\)", "\\(8.37 \\times 10^{-7}\\)", "\\(83.7 \\times 10^{-9}\\)", "\\(0.837 \\times 10^{-7}\\)"],
     "A", "OSC", "medium",
     "Moving 8 places right gives \\(8.37 \\times 10^{-8}\\)."),

    # 23
    ("Express \\(9460000000000\\text{ km}\\) (1 light year) in scientific notation.",
     ["\\(9.46 \\times 10^{12}\\text{ km}\\)",
      "\\(9.46 \\times 10^{11}\\text{ km}\\)",
      "\\(94.6 \\times 10^{11}\\text{ km}\\)",
      "\\(9.46 \\times 10^{13}\\text{ km}\\)"],
     "A", "OSC", "medium",
     "Shifting decimal 12 places left gives \\(9.46 \\times 10^{12}\\text{ km}\\)."),

    # 24
    ("Express \\(7.54 \\times 10^{-4}\\) in usual decimal form.",
     ["0.000754", "0.00754", "0.0000754", "0.0754"],
     "A", "OSC", "easy",
     "Moving decimal 4 places left gives \\(0.000754\\)."),

    # 25
    ("Express \\(9.0 \\times 10^{-8}\\) in usual decimal form.",
     ["0.00000009", "0.0000009", "0.000000009", "0.00009"],
     "A", "OSC", "medium",
     "Moving decimal 8 places left yields 7 zeros followed by 9: \\(0.00000009\\)."),

    # 26
    ("Express \\(2.0005 \\times 10^{-5}\\) in usual form.",
     ["0.000020005", "0.00020005", "0.0000020005", "0.0020005"],
     "A", "OSC", "medium",
     "Moving decimal 5 places left gives 4 leading zeros after decimal: \\(0.000020005\\)."),

    # 27
    ("The mass of Earth is \\(5.97 \\times 10^{24}\\text{ kg}\\) and the mass of the Moon is \\(7.35 \\times 10^{22}\\text{ kg}\\). What is their combined total mass in standard form?",
     ["\\(6.0435 \\times 10^{24}\\text{ kg}\\)",
      "\\(13.32 \\times 10^{23}\\text{ kg}\\)",
      "\\(6.0435 \\times 10^{22}\\text{ kg}\\)",
      "\\(5.97735 \\times 10^{24}\\text{ kg}\\)"],
     "A", "OSC", "hard",
     "Express both with exponent 24: \\(7.35 \\times 10^{22} = 0.0735 \\times 10^{24}\\). Adding: \\((5.97 + 0.0735) \\times 10^{24} = 6.0435 \\times 10^{24}\\text{ kg}\\)."),

    # 28
    ("In a stack there are 5 books each of thickness \\(20\\text{ mm}\\) and 5 paper sheets each of thickness \\(0.016\\text{ mm}\\). What is the total thickness of the stack in standard form?",
     ["\\(1.0008 \\times 10^2\\text{ mm}\\)",
      "\\(1.0008 \\times 10^1\\text{ mm}\\)",
      "\\(1.08 \\times 10^2\\text{ mm}\\)",
      "\\(10.008 \\times 10^1\\text{ mm}\\)"],
     "A", "OSC", "hard",
     "Thickness of books = \\(5 \\times 20 = 100\\text{ mm}\\). Thickness of paper = \\(5 \\times 0.016 = 0.08\\text{ mm}\\). Total = \\(100 + 0.08 = 100.08\\text{ mm} = 1.0008 \\times 10^2\\text{ mm}\\)."),

    # 29
    ("Multiply \\(3.0 \\times 10^4\\) by \\(2.0 \\times 10^{-7}\\) and write in standard form.",
     ["\\(6.0 \\times 10^{-3}\\)", "\\(6.0 \\times 10^3\\)", "\\(6.0 \\times 10^{-11}\\)", "\\(5.0 \\times 10^{-3}\\)"],
     "A", "OSC", "easy",
     "Multiply coefficients: \\(3.0 \\times 2.0 = 6.0\\). Add exponents: \\(10^{4 + (-7)} = 10^{-3}\\). Standard form is \\(6.0 \\times 10^{-3}\\)."),

    # 30
    ("Divide \\(8.4 \\times 10^7\\) by \\(2.1 \\times 10^3\\) in standard form.",
     ["\\(4.0 \\times 10^4\\)", "\\(4.0 \\times 10^{10}\\)", "\\(4.0 \\times 10^2\\)", "\\(0.4 \\times 10^5\\)"],
     "A", "OSC", "easy",
     "Divide coefficients: \\(8.4 / 2.1 = 4.0\\). Subtract exponents: \\(10^{7 - 3} = 10^4\\). Result: \\(4.0 \\times 10^4\\)."),

    # 31
    ("Evaluate \\((1.2 \\times 10^{-3}) \\times (5.0 \\times 10^{-4})\\) in standard form.",
     ["\\(6.0 \\times 10^{-7}\\)", "\\(6.0 \\times 10^{-8}\\)", "\\(6.0 \\times 10^{-6}\\)", "\\(0.6 \\times 10^{-6}\\)"],
     "A", "OSC", "medium",
     "\\(1.2 \\times 5.0 = 6.0\\). Powers: \\(10^{-3 + (-4)} = 10^{-7}\\). Result is \\(6.0 \\times 10^{-7}\\)."),

    # 32
    ("Evaluate \\((4.0 \\times 10^5) \\times (5.0 \\times 10^3)\\) in standard form.",
     ["\\(2.0 \\times 10^9\\)", "\\(20.0 \\times 10^8\\)", "\\(2.0 \\times 10^8\\)", "\\(2.0 \\times 10^{15}\\)"],
     "A", "OSC", "medium",
     "\\(4.0 \\times 5.0 = 20.0\\). Powers: \\(10^{5 + 3} = 10^8\\). Since 20 is not in standard form (\\(k \\ge 10\\)), rewrite \\(20.0 \\times 10^8 = 2.0 \\times 10^9\\)."),

    # 33
    ("Evaluate \\((1.5 \\times 10^{-6}) \\div (6.0 \\times 10^{-2})\\) in standard form.",
     ["\\(2.5 \\times 10^{-5}\\)", "\\(0.25 \\times 10^{-4}\\)", "\\(2.5 \\times 10^{-4}\\)", "\\(9.0 \\times 10^{-8}\\)"],
     "A", "OSC", "medium",
     "\\(1.5 / 6.0 = 0.25\\). Powers: \\(10^{-6 - (-2)} = 10^{-4}\\). Since \\(0.25 < 1\\), convert to standard form: \\(0.25 \\times 10^{-4} = 2.5 \\times 10^{-5}\\)."),

    # 34
    ("Assertion (A): \\(0.00045\\) in standard form is \\(4.5 \\times 10^{-4}\\).\nReason (R): For any number less than 1, standard form has a negative exponent of 10 representing the number of places the decimal point is shifted right.",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "Shifting 4 places right gives \\(4.5\\), so the power is \\(-4\\), matching the rule for numbers strictly between 0 and 1."),

    # 35
    ("Assertion (A): \\(53.2 \\times 10^4\\) is written in standard form.\nReason (R): In standard form, the coefficient \\(k\\) in \\(k \\times 10^n\\) must be an integer.",
     ["Both (A) and (R) are false",
      "Both (A) and (R) are true",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "Both are false: (A) is false because \\(53.2 \\ge 10\\), and (R) is false because \\(k\\) is any real decimal such that \\(1.0 \\le k < 10\\), not necessarily an integer."),

    # 36
    ("True or False: If a number is greater than 10, the exponent of 10 in its standard form is positive.",
     ["True", "False"],
     "A", "OTF", "easy",
     "For any number \\(\\ge 10\\), the decimal point must be moved left, requiring a positive integer power of 10."),

    # 37
    ("True or False: The number \\(1.0 \\times 10^0\\) is in standard form.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Here \\(k = 1.0\\) (which satisfies \\(1.0 \\le k < 10\\)) and \\(n = 0\\) (an integer), which is valid standard form for the number 1."),

    # 38
    ("Fill in the blank: In standard form \\(k \\times 10^n\\), the value of \\(k\\) must satisfy _____.",
     ["\\(1.0 \\le k < 10\\)", "\\(0 < k < 1\\)", "\\(1 < k \\le 10\\)", "\\(k \\ge 10\\)"],
     "A", "OFB", "easy",
     "By definition of standard form, \\(k\\) must be at least 1 and strictly less than 10."),

    # 39
    ("Fill in the blank: To convert \\(0.00006\\) into standard form, the decimal point is shifted _____ places to the right.",
     ["5", "4", "6", "3"],
     "A", "OFB", "easy",
     "Moving 5 places right yields 6.0, so the exponent is \\(-5\\)."),

    # 40
    ("What is the numerical integer exponent \\(n\\) when \\(0.000000042\\) is written as \\(4.2 \\times 10^n\\)?",
     ["-8", "-7", "-9", "-6"],
     "A", "ONE", "easy",
     "Moving the decimal point 8 places to the right gives \\(4.2 \\times 10^{-8}\\), so \\(n = -8\\)."),
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    ("Express \\(0.00000000000942\\) in standard form.",
     ["\\(9.42 \\times 10^{-12}\\)", "\\(9.42 \\times 10^{-11}\\)", "\\(94.2 \\times 10^{-13}\\)", "\\(0.942 \\times 10^{-11}\\)"],
     "A", "OSC", "medium",
     "Shift decimal 12 places to the right: \\(9.42 \\times 10^{-12}\\)."),

    # 42
    ("Express \\(6020000000000000\\) in standard form.",
     ["\\(6.02 \\times 10^{15}\\)", "\\(6.02 \\times 10^{14}\\)", "\\(60.2 \\times 10^{14}\\)", "\\(6.02 \\times 10^{16}\\)"],
     "A", "OSC", "medium",
     "Shift decimal 15 places to the left: \\(6.02 \\times 10^{15}\\)."),

    # 43
    ("Express \\(0.0000000085\\) in standard form.",
     ["\\(8.5 \\times 10^{-9}\\)", "\\(8.5 \\times 10^{-8}\\)", "\\(85 \\times 10^{-10}\\)", "\\(0.85 \\times 10^{-8}\\)"],
     "A", "OSC", "easy",
     "Shift 9 places right: \\(8.5 \\times 10^{-9}\\)."),

    # 44
    ("Express \\(31860000000\\) in standard form.",
     ["\\(3.186 \\times 10^{10}\\)", "\\(3.186 \\times 10^9\\)", "\\(31.86 \\times 10^9\\)", "\\(3.186 \\times 10^{11}\\)"],
     "A", "OSC", "easy",
     "Shift 10 places left: \\(3.186 \\times 10^{10}\\)."),

    # 45
    ("Size of a red blood cell is \\(0.000007\\text{ m}\\) and size of a plant cell is \\(0.00001275\\text{ m}\\). Express the size of plant cell in scientific notation.",
     ["\\(1.275 \\times 10^{-5}\\text{ m}\\)",
      "\\(1.275 \\times 10^{-4}\\text{ m}\\)",
      "\\(12.75 \\times 10^{-6}\\text{ m}\\)",
      "\\(0.1275 \\times 10^{-4}\\text{ m}\\)"],
     "A", "OSC", "easy",
     "Moving 5 places right gives \\(1.275 \\times 10^{-5}\\text{ m}\\)."),

    # 46
    ("Express \\(5.08 \\times 10^{-6}\\) in usual form.",
     ["0.00000508", "0.0000508", "0.000508", "0.000000508"],
     "A", "OSC", "easy",
     "Shift decimal 6 places left: \\(0.00000508\\)."),

    # 47
    ("Express \\(7.004 \\times 10^8\\) in usual form.",
     ["700,400,000", "70,040,000", "7,004,000,000", "700,040,000"],
     "A", "OSC", "easy",
     "Shift decimal 8 places right: \\(700,400,000\\)."),

    # 48
    ("Express \\(1.4335 \\times 10^{12}\\text{ m}\\) (distance of Saturn from Sun) in usual form.",
     ["1,433,500,000,000 m", "143,350,000,000 m", "14,335,000,000 m", "1,433,500,000 m"],
     "A", "OSC", "medium",
     "Moving decimal 12 places right gives 1 trillion 433 billion 500 million: \\(1,433,500,000,000\\text{ m}\\)."),

    # 49
    ("The mass of an oxygen atom is \\(2.656 \\times 10^{-23}\\text{ g}\\). What is this number in ordinary decimal notation?",
     ["A decimal starting with 22 zeros after the decimal point followed by 2656",
      "A decimal with 23 zeros followed by 2656",
      "A decimal with 21 zeros followed by 2656",
      "2656 preceded by 24 zeros"],
     "A", "OSC", "medium",
     "Moving decimal 23 places left from 2.656 requires 22 zeros after the decimal point before 2656."),

    # 50
    ("Average human body contains about \\(3.72 \\times 10^{13}\\) cells. Write in standard form.",
     ["\\(3.72 \\times 10^{13}\\)", "\\(37.2 \\times 10^{12}\\)", "\\(0.372 \\times 10^{14}\\)", "\\(372 \\times 10^{11}\\)"],
     "A", "OSC", "easy",
     "It is already correctly in standard form with \\(1.0 \\le 3.72 < 10\\)."),

    # 51
    ("Find the product of \\(2.5 \\times 10^{-4}\\) and \\(4.0 \\times 10^{-3}\\) in standard form.",
     ["\\(1.0 \\times 10^{-6}\\)", "\\(1.0 \\times 10^{-7}\\)", "\\(10.0 \\times 10^{-7}\\)", "\\(1.0 \\times 10^{-5}\\)"],
     "A", "OSC", "medium",
     "\\(2.5 \\times 4.0 = 10.0\\). Powers: \\(10^{-4 + (-3)} = 10^{-7}\\). Then \\(10.0 \\times 10^{-7} = 1.0 \\times 10^{-6}\\)."),

    # 52
    ("Find the quotient of \\((4.8 \\times 10^{-2}) \\div (1.6 \\times 10^{-6})\\) in standard form.",
     ["\\(3.0 \\times 10^4\\)", "\\(3.0 \\times 10^{-8}\\)", "\\(3.0 \\times 10^{-4}\\)", "\\(0.3 \\times 10^5\\)"],
     "A", "OSC", "easy",
     "\\(4.8 / 1.6 = 3.0\\). Powers: \\(10^{-2 - (-6)} = 10^4\\). Result: \\(3.0 \\times 10^4\\)."),

    # 53
    ("Add \\(4.5 \\times 10^5\\) and \\(3.2 \\times 10^4\\) in standard form.",
     ["\\(4.82 \\times 10^5\\)", "\\(7.7 \\times 10^9\\)", "\\(7.7 \\times 10^5\\)", "\\(4.82 \\times 10^4\\)"],
     "A", "OSC", "medium",
     "Convert to common power \\(10^5\\): \\(3.2 \\times 10^4 = 0.32 \\times 10^5\\). Sum: \\((4.5 + 0.32) \\times 10^5 = 4.82 \\times 10^5\\)."),

    # 54
    ("Subtract \\(1.2 \\times 10^{-4}\\) from \\(3.5 \\times 10^{-3}\\) in standard form.",
     ["\\(3.38 \\times 10^{-3}\\)", "\\(2.3 \\times 10^{-3}\\)", "\\(2.3 \\times 10^{-4}\\)", "\\(3.38 \\times 10^{-4}\\)"],
     "A", "OSC", "medium",
     "Convert \\(1.2 \\times 10^{-4} = 0.12 \\times 10^{-3}\\). Subtracting: \\((3.5 - 0.12) \\times 10^{-3} = 3.38 \\times 10^{-3}\\)."),

    # 55
    ("Evaluate: \\((7.2 \\times 10^{-5}) \\div (9.0 \\times 10^{-2})\\) in standard form.",
     ["\\(8.0 \\times 10^{-4}\\)", "\\(0.8 \\times 10^{-3}\\)", "\\(8.0 \\times 10^{-3}\\)", "\\(8.0 \\times 10^{-7}\\)"],
     "A", "OSC", "medium",
     "\\(7.2 / 9.0 = 0.8\\). Powers: \\(10^{-5 - (-2)} = 10^{-3}\\). Rewriting in standard form: \\(0.8 \\times 10^{-3} = 8.0 \\times 10^{-4}\\)."),

    # 56
    ("Express \\(0.00000000005\\text{ m}\\) (approximate size of an atom) in scientific notation.",
     ["\\(5.0 \\times 10^{-11}\\text{ m}\\)",
      "\\(5.0 \\times 10^{-10}\\text{ m}\\)",
      "\\(50 \\times 10^{-12}\\text{ m}\\)",
      "\\(0.5 \\times 10^{-10}\\text{ m}\\)"],
     "A", "OSC", "easy",
     "Moving 11 places right gives \\(5.0 \\times 10^{-11}\\text{ m}\\)."),

    # 57
    ("Express \\(1\\text{ micron} = \\frac{1}{1000000}\\text{ m}\\) in standard form.",
     ["\\(1.0 \\times 10^{-6}\\text{ m}\\)",
      "\\(1.0 \\times 10^{-5}\\text{ m}\\)",
      "\\(1.0 \\times 10^{-7}\\text{ m}\\)",
      "\\(10 \\times 10^{-7}\\text{ m}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{1}{10^6} = 1.0 \\times 10^{-6}\\text{ m}\\)."),

    # 58
    ("Express \\(2.16 \\times 10^5\\) in usual form.",
     ["216,000", "21,600", "2,160,000", "216"],
     "A", "OSC", "easy",
     "Moving decimal 5 places right: \\(216,000\\)."),

    # 59
    ("Express \\(6.4 \\times 10^{-5}\\) in usual form.",
     ["0.000064", "0.00064", "0.0000064", "0.0064"],
     "A", "OSC", "easy",
     "Moving decimal 5 places left: \\(0.000064\\)."),

    # 60
    ("Express \\(8.005 \\times 10^{-3}\\) in usual form.",
     ["0.008005", "0.08005", "0.0008005", "0.8005"],
     "A", "OSC", "easy",
     "Moving decimal 3 places left: \\(0.008005\\)."),

    # 61
    ("Find the value of \\(x\\) if \\(0.000078 = 7.8 \\times 10^x\\).",
     ["\\(-5\\)", "5", "\\(-4\\)", "\\(-6\\)"],
     "A", "OSC", "easy",
     "Moving decimal 5 places right gives exponent \\(-5\\)."),

    # 62
    ("Find the value of \\(y\\) if \\(93000000 = 9.3 \\times 10^y\\).",
     ["7", "6", "8", "\\(-7\\)"],
     "A", "OSC", "easy",
     "Moving decimal 7 places left gives exponent 7."),

    # 63
    ("Which is larger: \\(5.4 \\times 10^{-4}\\) or \\(9.2 \\times 10^{-5}\\)?",
     ["\\(5.4 \\times 10^{-4}\\)", "\\(9.2 \\times 10^{-5}\\)", "Both are equal", "Cannot be determined"],
     "A", "OSC", "easy",
     "Compare powers of 10: \\(10^{-4} > 10^{-5}\\). In fact, \\(5.4 \\times 10^{-4} = 0.00054\\) while \\(9.2 \\times 10^{-5} = 0.000092\\). Thus \\(5.4 \\times 10^{-4}\\) is nearly 6 times larger."),

    # 64
    ("Which is smaller: \\(2.7 \\times 10^{-8}\\) or \\(1.3 \\times 10^{-7}\\)?",
     ["\\(2.7 \\times 10^{-8}\\)", "\\(1.3 \\times 10^{-7}\\)", "Both are equal", "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(10^{-8} < 10^{-7}\\), so \\(2.7 \\times 10^{-8} = 0.27 \\times 10^{-7} < 1.3 \\times 10^{-7}\\)."),

    # 65
    ("Express \\(0.0000016\\text{ cm}^2\\) in standard form.",
     ["\\(1.6 \\times 10^{-6}\\text{ cm}^2\\)",
      "\\(1.6 \\times 10^{-5}\\text{ cm}^2\\)",
      "\\(16 \\times 10^{-7}\\text{ cm}^2\\)",
      "\\(0.16 \\times 10^{-5}\\text{ cm}^2\\)"],
     "A", "OSC", "easy",
     "Moving 6 places right gives \\(1.6 \\times 10^{-6}\\text{ cm}^2\\)."),

    # 66
    ("True or False: A negative exponent in scientific notation implies that the number itself must be negative.",
     ["False", "True"],
     "A", "OTF", "easy",
     "A negative exponent means the number is between 0 and 1 (a small positive fraction), NOT that the number is negative. For instance, \\(3 \\times 10^{-4} = +0.0003 > 0\\)."),

    # 67
    ("True or False: In standard form \\(k \\times 10^n\\), \\(k\\) can be equal to \\(1.0\\).",
     ["True", "False"],
     "A", "OTF", "easy",
     "Yes, the range is \\(1.0 \\le k < 10\\), which explicitly includes \\(1.0\\)."),

    # 68
    ("Fill in the blank: To write a number smaller than 1 in standard form, the power of 10 must be _____.",
     ["negative", "positive", "zero", "fractional"],
     "A", "OFB", "easy",
     "Numbers less than 1 require moving the decimal point to the right, which corresponds to a negative exponent of 10."),

    # 69
    ("Fill in the blank: \\(1.0 \\times 10^6\\) in ordinary notation is called one _____.",
     ["million", "billion", "lakh", "crore"],
     "A", "OFB", "easy",
     "\\(10^6 = 1,000,000\\), which is 1 million."),

    # 70
    ("What is the numerical integer exponent \\(n\\) when \\(450,000\\) is written as \\(4.5 \\times 10^n\\)?",
     ["5", "4", "6", "-5"],
     "A", "ONE", "easy",
     "Moving the decimal point 5 places left gives \\(4.5 \\times 10^5\\), so \\(n = 5\\)."),
]

# 12 MOCK / FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Decimal Shift Direction & Sign of Exponent</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Large Number: Shift LEFT => Positive Exponent -->
    <rect x="20" y="25" width="140" height="55" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2"/>
    <text x="90" y="45" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">Large Number: 149600000</text>
    <text x="90" y="60" fill="#38bdf8" font-size="11" text-anchor="middle">Shift LEFT ←</text>
    <text x="90" y="73" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">Exponent: +8</text>
    <!-- Small Number: Shift RIGHT => Negative Exponent -->
    <rect x="180" y="25" width="140" height="55" rx="6" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
    <text x="250" y="45" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Small Number: 0.000035</text>
    <text x="250" y="60" fill="#fbbf24" font-size="11" text-anchor="middle">Shift RIGHT →</text>
    <text x="250" y="73" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">Exponent: -5</text>
    <!-- Standard Form Definition banner -->
    <rect x="35" y="95" width="270" height="40" rx="5" fill="#0f172a" stroke="#475569"/>
    <text x="170" y="112" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">Standard Form: k × 10ⁿ</text>
    <text x="170" y="128" fill="#fbbf24" font-size="11" text-anchor="middle">where 1.0 ≤ k &lt; 10 and n is an integer</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">When expressing \(0.0000085\) in standard form, in which direction and by how many places must the decimal shift?</p>
</div>""",
     ["6 places to the right (exponent -6)", "5 places to the right (exponent -5)", "6 places to the left (exponent +6)", "7 places to the right (exponent -7)"],
     "A", "OSC", "easy",
     "Moving from 0.0000085 to 8.5 moves the decimal point 6 places to the right, yielding \\(8.5 \\times 10^{-6}\\)."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Comparative Microscopic Scale Chart</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Bar 1: Plant Cell 1.275 x 10^-5 m -->
    <rect x="25" y="25" width="200" height="20" rx="3" fill="#10b981"/>
    <text x="35" y="39" fill="#ffffff" font-size="10" font-weight="bold">Plant Cell: 1.275 × 10⁻⁵ m</text>
    <!-- Bar 2: Red Blood Cell 7.0 x 10^-6 m -->
    <rect x="25" y="55" width="120" height="20" rx="3" fill="#ef4444"/>
    <text x="35" y="69" fill="#ffffff" font-size="10" font-weight="bold">Red Blood Cell: 7 × 10⁻⁶ m</text>
    <!-- Bar 3: Bacterium 5.0 x 10^-7 m -->
    <rect x="25" y="85" width="40" height="20" rx="3" fill="#3b82f6"/>
    <text x="75" y="99" fill="#93c5fd" font-size="10" font-weight="bold">Bacterium: 5 × 10⁻⁷ m</text>
    <!-- Ratio Annotation -->
    <text x="170" y="132" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Plant Cell ≈ 2× RBC  |  RBC ≈ 14× Bacterium</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Based on the scale chart, which object has the smallest diameter?</p>
</div>""",
     ["Bacterium (\\(5 \\times 10^{-7}\\text{ m}\\))",
      "Red Blood Cell (\\(7 \\times 10^{-6}\\text{ m}\\))",
      "Plant Cell (\\(1.275 \\times 10^{-5}\\text{ m}\\))",
      "Sheet of paper (\\(1.6 \\times 10^{-4}\\text{ m}\\))"],
     "A", "OSC", "easy",
     "\\(10^{-7} < 10^{-6} < 10^{-5}\\). With the smallest power \\(10^{-7}\\), the bacterium is the smallest object."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Converting Standard Form to Usual Form</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Step cards -->
    <rect x="25" y="30" width="105" height="50" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2"/>
    <text x="77" y="52" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">4.5 × 10⁴</text>
    <text x="77" y="70" fill="#cbd5e1" font-size="10" text-anchor="middle">Power +4: Move 4 right</text>
    <!-- Arrow -->
    <path d="M 140,55 L 180,55" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="180,50 190,55 180,60" fill="#f59e0b"/>
    <!-- Result -->
    <rect x="200" y="30" width="115" height="50" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="257" y="55" fill="#6ee7b7" font-size="14" font-weight="bold" text-anchor="middle">45,000</text>
    <text x="257" y="70" fill="#e2e8f0" font-size="10" text-anchor="middle">4 zeros/digits shifted</text>
    <!-- Footer Note -->
    <text x="170" y="125" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Positive power expands to a number ≥ 10</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is \(3.75 \times 10^5\) in usual decimal notation?</p>
</div>""",
     ["375,000", "37,500", "3,750,000", "0.0000375"],
     "A", "OSC", "easy",
     "Moving 5 places right: 2 places for '75', followed by 3 zeros: \\(375,000\\)."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Converting Negative Powers to Usual Decimals</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Start Form -->
    <rect x="25" y="30" width="105" height="50" rx="6" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
    <text x="77" y="52" fill="#fde047" font-size="13" font-weight="bold" text-anchor="middle">3.02 × 10⁻⁶</text>
    <text x="77" y="70" fill="#cbd5e1" font-size="10" text-anchor="middle">Power -6: Move 6 left</text>
    <!-- Arrow -->
    <path d="M 140,55 L 175,55" stroke="#38bdf8" stroke-width="2.5" fill="none"/>
    <polygon points="175,50 185,55 175,60" fill="#38bdf8"/>
    <!-- Target Usual Form -->
    <rect x="195" y="30" width="125" height="50" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="257" y="55" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">0.00000302</text>
    <text x="257" y="70" fill="#e2e8f0" font-size="10" text-anchor="middle">5 preceding zeros</text>
    <!-- Rule Footer -->
    <text x="170" y="125" fill="#38bdf8" font-size="11" text-anchor="middle">Rule: (n - 1) zeros placed immediately after decimal point</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is \(7.2 \times 10^{-4}\) in ordinary decimal form?</p>
</div>""",
     ["0.00072", "0.0072", "0.000072", "0.072"],
     "A", "OSC", "easy",
     "Moving 4 places left puts 3 zeros immediately after the decimal: \\(0.00072\\)."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Standard Form Validity Check: 1.0 ≤ k &lt; 10</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Invalid k < 1 -->
    <rect x="20" y="30" width="90" height="55" rx="6" fill="#7f1d1d" stroke="#ef4444" stroke-width="1.5"/>
    <text x="65" y="50" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">0.45 × 10⁴</text>
    <text x="65" y="70" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">INVALID (k &lt; 1)</text>
    <!-- VALID 1 <= k < 10 -->
    <rect x="125" y="25" width="90" height="65" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="50" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">4.5 × 10³</text>
    <text x="170" y="75" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">VALID</text>
    <!-- Invalid k >= 10 -->
    <rect x="230" y="30" width="90" height="55" rx="6" fill="#7f1d1d" stroke="#ef4444" stroke-width="1.5"/>
    <text x="275" y="50" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">45.0 × 10²</text>
    <text x="275" y="70" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">INVALID (k ≥ 10)</text>
    <!-- Footnote -->
    <text x="170" y="128" fill="#fde047" font-size="11" text-anchor="middle">Only one non-zero digit is permitted to the left of the decimal point</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Which of the following is written in correct standard form?</p>
</div>""",
     ["\\(6.25 \\times 10^{-7}\\)", "\\(62.5 \\times 10^{-8}\\)", "\\(0.625 \\times 10^{-6}\\)", "\\(625 \\times 10^{-9}\\)"],
     "A", "OSC", "easy",
     "Only \\(6.25\\) has exactly one non-zero digit before the decimal point (satisfying \\(1.0 \\le k < 10\\))."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Addition in Standard Form by Matching Powers</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Number A -->
    <text x="170" y="25" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">Sum: (4.5 × 10⁵) + (3.2 × 10⁴)</text>
    <!-- Match power step -->
    <rect x="35" y="40" width="270" height="40" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="170" y="58" fill="#93c5fd" font-size="11" text-anchor="middle">Rewrite 3.2 × 10⁴ as 0.32 × 10⁵</text>
    <text x="170" y="73" fill="#cbd5e1" font-size="11" text-anchor="middle">= (4.5 + 0.32) × 10⁵</text>
    <!-- Final Sum Card -->
    <rect x="80" y="90" width="180" height="35" rx="5" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="112" fill="#6ee7b7" font-size="14" font-weight="bold" text-anchor="middle">= 4.82 × 10⁵</text>
    <text x="170" y="140" fill="#fbbf24" font-size="10" text-anchor="middle">Always express in common higher power before adding</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the sum of \(5.0 \times 10^6\) and \(4.0 \times 10^5\) in standard form?</p>
</div>""",
     ["\\(5.4 \\times 10^6\\)", "\\(9.0 \\times 10^{11}\\)", "\\(9.0 \\times 10^6\\)", "\\(5.4 \\times 10^5\\)"],
     "A", "OSC", "easy",
     "\\(4.0 \\times 10^5 = 0.4 \\times 10^6\\). Sum: \\((5.0 + 0.4) \\times 10^6 = 5.4 \\times 10^6\\)."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Electron Charge vs Astronomical Light Year</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Electron box -->
    <rect x="25" y="30" width="135" height="75" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="92" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Subatomic Realm</text>
    <text x="92" y="75" fill="#ffffff" font-size="11" text-anchor="middle">Electron Charge</text>
    <text x="92" y="95" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">1.6 × 10⁻¹⁹ C</text>
    <!-- Light year box -->
    <rect x="180" y="30" width="135" height="75" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="247" y="55" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Cosmic Realm</text>
    <text x="247" y="75" fill="#ffffff" font-size="11" text-anchor="middle">1 Light Year</text>
    <text x="247" y="95" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">9.46 × 10¹² km</text>
    <!-- Scale span footer -->
    <text x="170" y="132" fill="#cbd5e1" font-size="11" text-anchor="middle">Powers of 10 span 31 orders of magnitude seamlessly</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">How many orders of magnitude separate \(10^{12}\) and \(10^{-19}\)?</p>
</div>""",
     ["31 orders of magnitude", "7 orders of magnitude", "12 orders of magnitude", "-7 orders of magnitude"],
     "A", "OSC", "easy",
     "Subtracting exponents: \\(12 - (-19) = 12 + 19 = 31\\) orders of magnitude."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Stack Thickness Word Problem Diagram</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- 5 Books pile -->
    <rect x="40" y="60" width="100" height="40" fill="#3b82f6" stroke="#60a5fa" stroke-width="1.5"/>
    <text x="90" y="85" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">5 Books = 100 mm</text>
    <!-- 5 Sheets pile -->
    <rect x="40" y="50" width="100" height="8" fill="#f59e0b" stroke="#fbbf24" stroke-width="1"/>
    <text x="90" y="42" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">5 Sheets = 0.08 mm</text>
    <!-- Total formula -->
    <rect x="170" y="45" width="150" height="60" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="245" y="68" fill="#6ee7b7" font-size="11" text-anchor="middle">Total = 100.08 mm</text>
    <text x="245" y="90" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">= 1.0008 × 10² mm</text>
    <text x="170" y="132" fill="#e2e8f0" font-size="10" text-anchor="middle">Paper thickness adds directly to the decimal portion</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">A stack has 4 books of thickness \(25\text{ mm}\) and 4 paper sheets of thickness \(0.02\text{ mm}\). Express total thickness in standard form.</p>
</div>""",
     ["\\(1.0008 \\times 10^2\\text{ mm}\\)",
      "\\(1.08 \\times 10^2\\text{ mm}\\)",
      "\\(1.008 \\times 10^2\\text{ mm}\\)",
      "\\(1.0008 \\times 10^1\\text{ mm}\\)"],
     "A", "OSC", "medium",
     "Books: \\(4 \\times 25 = 100\\text{ mm}\\). Sheets: \\(4 \\times 0.02 = 0.08\\text{ mm}\\). Total = \\(100.08\\text{ mm} = 1.0008 \\times 10^2\\text{ mm}\\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Standard Form Multiplication Normalisation</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Multiplication -->
    <text x="170" y="25" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">(4.0 × 10⁵) × (5.0 × 10³)</text>
    <!-- Raw product -->
    <rect x="35" y="40" width="120" height="40" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="95" y="58" fill="#fca5a5" font-size="11" text-anchor="middle">20.0 × 10⁸</text>
    <text x="95" y="72" fill="#ef4444" font-size="9" text-anchor="middle">NOT Standard (20 ≥ 10)</text>
    <!-- Arrow -->
    <path d="M 165,60 L 195,60" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="195,55 205,60 195,65" fill="#f59e0b"/>
    <!-- Normalised -->
    <rect x="205" y="40" width="110" height="40" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="260" y="58" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">2.0 × 10⁹</text>
    <text x="260" y="72" fill="#34d399" font-size="9" text-anchor="middle">VALID (1 ≤ 2 &lt; 10)</text>
    <!-- Footer tip -->
    <text x="170" y="125" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">When coefficient reaches 10, increment exponent by 1</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the standard form of \((6.0 \times 10^4) \times (5.0 \times 10^3)\)?</p>
</div>""",
     ["\\(3.0 \\times 10^8\\)", "\\(30.0 \\times 10^7\\)", "\\(3.0 \\times 10^7\\)", "\\(3.0 \\times 10^9\\)"],
     "A", "OSC", "easy",
     "\\(6.0 \\times 5.0 = 30.0\\). Powers: \\(10^{4+3} = 10^7\\). Then \\(30.0 \\times 10^7 = 3.0 \\times 10^8\\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Standard Form Division Underflow Normalisation</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Division -->
    <text x="170" y="25" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">(1.8 × 10⁻⁴) ÷ (9.0 × 10⁻²)</text>
    <!-- Raw quotient -->
    <rect x="35" y="40" width="120" height="40" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="95" y="58" fill="#fca5a5" font-size="11" text-anchor="middle">0.2 × 10⁻²</text>
    <text x="95" y="72" fill="#ef4444" font-size="9" text-anchor="middle">NOT Standard (0.2 &lt; 1)</text>
    <!-- Arrow -->
    <path d="M 165,60 L 195,60" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="195,55 205,60 195,65" fill="#f59e0b"/>
    <!-- Normalised -->
    <rect x="205" y="40" width="110" height="40" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="260" y="58" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">2.0 × 10⁻³</text>
    <text x="260" y="72" fill="#34d399" font-size="9" text-anchor="middle">VALID (1 ≤ 2 &lt; 10)</text>
    <!-- Footer tip -->
    <text x="170" y="125" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">When coefficient drops below 1, decrement exponent by 1</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is \((1.2 \times 10^{-5}) \div (4.0 \times 10^{-2})\) in standard form?</p>
</div>""",
     ["\\(3.0 \\times 10^{-4}\\)", "\\(0.3 \\times 10^{-3}\\)", "\\(3.0 \\times 10^{-3}\\)", "\\(4.8 \\times 10^{-7}\\)"],
     "A", "OSC", "easy",
     "\\(1.2 / 4.0 = 0.3\\). Powers: \\(10^{-5 - (-2)} = 10^{-3}\\). Normalising gives \\(0.3 \\times 10^{-3} = 3.0 \\times 10^{-4}\\)."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Comparing Very Small Decimal Quantities</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Quantity A -->
    <rect x="30" y="30" width="120" height="60" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="90" y="55" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">5.4 × 10⁻⁴</text>
    <text x="90" y="75" fill="#cbd5e1" font-size="11" text-anchor="middle">= 0.00054</text>
    <!-- Comparison sign -->
    <text x="170" y="65" fill="#10b981" font-size="22" font-weight="bold" text-anchor="middle">&gt;</text>
    <!-- Quantity B -->
    <rect x="190" y="30" width="120" height="60" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <text x="250" y="55" fill="#fca5a5" font-size="13" font-weight="bold" text-anchor="middle">9.2 × 10⁻⁵</text>
    <text x="250" y="75" fill="#cbd5e1" font-size="11" text-anchor="middle">= 0.000092</text>
    <!-- Principle banner -->
    <text x="170" y="130" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">A larger exponent (-4 > -5) always dominates the coefficient</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Which of the following statements is mathematically true?</p>
</div>""",
     ["\\(5.4 \\times 10^{-4} > 9.2 \\times 10^{-5}\\)",
      "\\(9.2 \\times 10^{-5} > 5.4 \\times 10^{-4}\\)",
      "\\(5.4 \\times 10^{-4} = 9.2 \\times 10^{-5}\\)",
      "Neither is defined"],
     "A", "OSC", "easy",
     "Because \\(10^{-4} = 10 \\times 10^{-5}\\), \\(5.4 \\times 10^{-4} = 54 \\times 10^{-5} > 9.2 \\times 10^{-5}\\)."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Ratio Comparison of Two Standard Form Quantities</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Ratio Fraction -->
    <rect x="40" y="25" width="120" height="75" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="100" y="52" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">Sun: 1.4 × 10⁹ m</text>
    <line x1="55" y1="62" x2="145" y2="62" stroke="#60a5fa" stroke-width="2"/>
    <text x="100" y="82" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">Earth: 1.275 × 10⁷ m</text>
    <!-- Arrow -->
    <path d="M 175,60 L 205,60" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="205,55 215,60 205,65" fill="#f59e0b"/>
    <!-- Ratio Result -->
    <rect x="220" y="35" width="90" height="55" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="265" y="60" fill="#6ee7b7" font-size="14" font-weight="bold" text-anchor="middle">≈ 100</text>
    <text x="265" y="78" fill="#e2e8f0" font-size="10" text-anchor="middle">Sun ≈ 100× Earth</text>
    <!-- Footnote -->
    <text x="170" y="132" fill="#fde047" font-size="11" text-anchor="middle">Subtracting powers: 10⁹ ÷ 10⁷ = 10² = 100 times larger</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Approximately how many times larger is the diameter of the Sun (\(1.4 \times 10^9\text{ m}\)) compared to Earth (\(1.275 \times 10^7\text{ m}\))?</p>
</div>""",
     ["Approximately 100 times", "Approximately 10 times", "Approximately 1000 times", "Approximately 2 times"],
     "A", "OSC", "easy",
     "\\(\\frac{1.4 \\times 10^9}{1.275 \\times 10^7} \\approx \\frac{1.4}{1.275} \\times 10^2 \\approx 1.1 \\times 100 \\approx 100\\) times.")
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch2_topic3.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
