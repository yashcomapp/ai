# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-2-2.1
Topic: Powers with Negative Integral Exponents
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-2-2.1"

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
    ("For any non-zero rational number \\(a\\) and positive integer \\(m\\), what does \\(a^{-m}\\) equal?",
     ["\\(\\frac{1}{a^m}\\)", "\\(-a^m\\)", "\\(-\\frac{1}{a^m}\\)", "\\(a \\times (-m)\\)"],
     "A", "OSC", "easy",
     "By definition of negative integral exponents, \\(a^{-m}\\) is the reciprocal of \\(a^m\\), which equals \\(\\frac{1}{a^m}\\)."),

    # 2
    ("What is the value of \\(2^{-3}\\)?",
     ["\\(\\frac{1}{8}\\)", "\\(-8\\)", "\\(-\\frac{1}{8}\\)", "\\(\\frac{1}{6}\\)"],
     "A", "OSC", "easy",
     "\\(2^{-3} = \\frac{1}{2^3} = \\frac{1}{2 \\times 2 \\times 2} = \\frac{1}{8}\\)."),

    # 3
    ("What is the multiplicative inverse of \\(10^{-5}\\)?",
     ["\\(10^5\\)", "\\(-10^5\\)", "\\(10^{-5}\\)", "\\(-10^{-5}\\)"],
     "A", "OSC", "easy",
     "The multiplicative inverse of a number \\(x\\) is \\(\\frac{1}{x}\\). For \\(10^{-5}\\), the inverse is \\(\\frac{1}{10^{-5}} = 10^5\\), since \\(10^{-5} \\times 10^5 = 10^0 = 1\\)."),

    # 4
    ("What is the multiplicative inverse of \\(5^4\\)?",
     ["\\(5^{-4}\\)", "\\(-5^4\\)", "\\(5^{\\frac{1}{4}}\\)", "\\(-5^{-4}\\)"],
     "A", "OSC", "easy",
     "The multiplicative inverse of \\(a^m\\) is \\(a^{-m}\\), because \\(a^m \\times a^{-m} = 1\\). Hence for \\(5^4\\), it is \\(5^{-4}\\)."),

    # 5
    ("What is the value of \\((-3)^{-4}\\)?",
     ["\\(\\frac{1}{81}\\)", "\\(-\\frac{1}{81}\\)", "\\(-81\\)", "81"],
     "A", "OSC", "easy",
     "\\((-3)^{-4} = \\frac{1}{(-3)^4}\\). Since the exponent 4 is even, \\((-3)^4 = 81\\). Thus \\((-3)^{-4} = \\frac{1}{81}\\)."),

    # 6
    ("What is the value of \\((-2)^{-5}\\)?",
     ["\\(-\\frac{1}{32}\\)", "\\(\\frac{1}{32}\\)", "\\(-32\\)", "32"],
     "A", "OSC", "easy",
     "\\((-2)^{-5} = \\frac{1}{(-2)^5}\\). Since the exponent 5 is odd, \\((-2)^5 = -32\\). Therefore \\((-2)^{-5} = -\\frac{1}{32}\\)."),

    # 7
    ("What is the value of \\(\\left(\\frac{1}{3}\\right)^{-2}\\)?",
     ["9", "\\(\\frac{1}{9}\\)", "\\(-9\\)", "\\(-\\frac{1}{9}\\)"],
     "A", "OSC", "easy",
     "Using \\(\\left(\\frac{a}{b}\\right)^{-m} = \\left(\\frac{b}{a}\\right)^m\\), we get \\(\\left(\\frac{1}{3}\\right)^{-2} = \\left(\\frac{3}{1}\\right)^2 = 3^2 = 9\\)."),

    # 8
    ("What is the value of \\(\\left(\\frac{2}{3}\\right)^{-3}\\)?",
     ["\\(\\frac{27}{8}\\)", "\\(\\frac{8}{27}\\)", "\\(-\\frac{27}{8}\\)", "\\(-\\frac{8}{27}\\)"],
     "A", "OSC", "easy",
     "Inverting the fraction to make the power positive: \\(\\left(\\frac{2}{3}\\right)^{-3} = \\left(\\frac{3}{2}\\right)^3 = \\frac{3^3}{2^3} = \\frac{27}{8}\\)."),

    # 9
    ("What is the value of \\(\\left(-\\frac{3}{4}\\right)^{-3}\\)?",
     ["\\(-\\frac{64}{27}\\)", "\\(\\frac{64}{27}\\)", "\\(-\\frac{27}{64}\\)", "\\(\\frac{27}{64}\\)"],
     "A", "OSC", "medium",
     "\\(\\left(-\\frac{3}{4}\\right)^{-3} = \\left(-\\frac{4}{3}\\right)^3 = \\frac{(-4)^3}{3^3} = -\\frac{64}{27}\\)."),

    # 10
    ("What is the multiplicative inverse of \\(\\left(\\frac{5}{7}\\right)^{-2}\\)?",
     ["\\(\\left(\\frac{5}{7}\\right)^2\\)", "\\(\\left(\\frac{7}{5}\\right)^2\\)", "\\(\\left(-\\frac{5}{7}\\right)^2\\)", "\\(-\\frac{25}{49}\\)"],
     "A", "OSC", "easy",
     "The multiplicative inverse of any term \\(x^{-m}\\) is \\(x^m\\). Therefore the multiplicative inverse of \\(\\left(\\frac{5}{7}\\right)^{-2}\\) is \\(\\left(\\frac{5}{7}\\right)^2\\)."),

    # 11
    ("What is the value of \\(10^{-1} + 10^{-2}\\)?",
     ["0.11", "0.011", "1.1", "0.02"],
     "A", "OSC", "easy",
     "\\(10^{-1} = 0.1\\) and \\(10^{-2} = 0.01\\). Summing them: \\(0.1 + 0.01 = 0.11\\)."),

    # 12
    ("Express \\(0.007\\) using powers of 10 in expanded form.",
     ["\\(7 \\times 10^{-3}\\)", "\\(7 \\times 10^{-2}\\)", "\\(7 \\times 10^{-4}\\)", "\\(7 \\times 10^3\\)"],
     "A", "OSC", "easy",
     "\\(0.007 = \\frac{7}{1000} = 7 \\times \\frac{1}{10^3} = 7 \\times 10^{-3}\\)."),

    # 13
    ("Express the number \\(42.5\\) in expanded form using powers of 10.",
     ["\\(4 \\times 10^1 + 2 \\times 10^0 + 5 \\times 10^{-1}\\)",
      "\\(4 \\times 10^2 + 2 \\times 10^1 + 5 \\times 10^0\\)",
      "\\(4 \\times 10^1 + 2 \\times 10^0 + 5 \\times 10^{-2}\\)",
      "\\(4 \\times 10^2 + 2 \\times 10^{-1} + 5 \\times 10^{-2}\\)"],
     "A", "OSC", "medium",
     "The place values are: 4 in tens place (\\(4 \\times 10^1\\)), 2 in units place (\\(2 \\times 10^0\\)), and 5 in tenths place (\\(5 \\times 10^{-1}\\))."),

    # 14
    ("Express \\(1025.63\\) in expanded form using powers of 10.",
     ["\\(1 \\times 10^3 + 2 \\times 10^1 + 5 \\times 10^0 + 6 \\times 10^{-1} + 3 \\times 10^{-2}\\)",
      "\\(1 \\times 10^4 + 2 \\times 10^2 + 5 \\times 10^1 + 6 \\times 10^{-1} + 3 \\times 10^{-2}\\)",
      "\\(1 \\times 10^3 + 2 \\times 10^2 + 5 \\times 10^0 + 6 \\times 10^{-2} + 3 \\times 10^{-3}\\)",
      "\\(1 \\times 10^3 + 2 \\times 10^1 + 5 \\times 10^0 + 6 \\times 10^1 + 3 \\times 10^2\\)"],
     "A", "OSC", "medium",
     "\\(1025.63 = 1 \\times 10^3 + 0 \\times 10^2 + 2 \\times 10^1 + 5 \\times 10^0 + 6 \\times 10^{-1} + 3 \\times 10^{-2}\\). Omitting the zero term gives the correct expansion."),

    # 15
    ("What is the decimal value of \\(3 \\times 10^1 + 7 \\times 10^0 + 4 \\times 10^{-1} + 9 \\times 10^{-3}\\)?",
     ["37.409", "37.49", "370.409", "3.7409"],
     "A", "OSC", "medium",
     "Tens: \\(30\\), Units: \\(7\\), Tenths: \\(0.4\\), Hundredths: \\(0\\), Thousandths: \\(0.009\\). Summing gives \\(37.409\\)."),

    # 16
    ("What is the value of \\(4^{-2}\\)?",
     ["\\(\\frac{1}{16}\\)", "\\(\\frac{1}{8}\\)", "\\(-16\\)", "\\(-8\\)"],
     "A", "OSC", "easy",
     "\\(4^{-2} = \\frac{1}{4^2} = \\frac{1}{16}\\)."),

    # 17
    ("What is the value of \\(5^{-3}\\)?",
     ["\\(\\frac{1}{125}\\)", "\\(\\frac{1}{25}\\)", "\\(-125\\)", "\\(-\\frac{1}{125}\\)"],
     "A", "OSC", "easy",
     "\\(5^{-3} = \\frac{1}{5^3} = \\frac{1}{125}\\)."),

    # 18
    ("What is the value of \\((-1)^{-99}\\)?",
     ["\\(-1\\)", "1", "99", "\\(-99\\)"],
     "A", "OSC", "easy",
     "\\((-1)^{-99} = \\frac{1}{(-1)^{99}}\\). Since 99 is odd, \\((-1)^{99} = -1\\). Hence \\(\\frac{1}{-1} = -1\\)."),

    # 19
    ("What is the value of \\((-1)^{-100}\\)?",
     ["1", "\\(-1\\)", "100", "\\(-100\\)"],
     "A", "OSC", "easy",
     "\\((-1)^{-100} = \\frac{1}{(-1)^{100}}\\). Since 100 is even, \\((-1)^{100} = 1\\). Thus \\(\\frac{1}{1} = 1\\)."),

    # 20
    ("What is the multiplicative inverse of \\((-4)^{-3}\\)?",
     ["\\((-4)^3\\)", "\\(4^{-3}\\)", "\\(4^3\\)", "\\(-4^{-3}\\)"],
     "A", "OSC", "easy",
     "The multiplicative inverse of \\(x^{-m}\\) is \\(x^m\\). For \\((-4)^{-3}\\), it is \\((-4)^3\\), since \\((-4)^{-3} \\times (-4)^3 = 1\\)."),

    # 21
    ("Evaluate: \\(2^{-1} + 3^{-1}\\)",
     ["\\(\\frac{5}{6}\\)", "\\(\\frac{1}{5}\\)", "\\(\\frac{2}{3}\\)", "\\(\\frac{1}{6}\\)"],
     "A", "OSC", "medium",
     "\\(2^{-1} = \\frac{1}{2}\\) and \\(3^{-1} = \\frac{1}{3}\\). Summing them: \\(\\frac{1}{2} + \\frac{1}{3} = \\frac{3 + 2}{6} = \\frac{5}{6}\\)."),

    # 22
    ("Evaluate: \\((2^{-1} \\times 4^{-1}) \\div 2^{-2}\\)",
     ["\\(\\frac{1}{2}\\)", "1", "2", "\\(\\frac{1}{4}\\)"],
     "A", "OSC", "medium",
     "\\(2^{-1} \\times 4^{-1} = \\frac{1}{2} \\times \\frac{1}{4} = \\frac{1}{8}\\). Also \\(2^{-2} = \\frac{1}{4}\\). Dividing gives \\(\\frac{1}{8} \\div \\frac{1}{4} = \\frac{1}{8} \\times 4 = \\frac{1}{2}\\)."),

    # 23
    ("Evaluate: \\(\\left(\\frac{1}{2}\\right)^{-2} + \\left(\\frac{1}{3}\\right)^{-2} + \\left(\\frac{1}{4}\\right)^{-2}\\)",
     ["29", "14", "9", "36"],
     "A", "OSC", "medium",
     "\\(\\left(\\frac{1}{2}\\right)^{-2} = 2^2 = 4\\), \\(\\left(\\frac{1}{3}\\right)^{-2} = 3^2 = 9\\), and \\(\\left(\\frac{1}{4}\\right)^{-2} = 4^2 = 16\\). Sum: \\(4 + 9 + 16 = 29\\)."),

    # 24
    ("Evaluate: \\((3^{-1} + 4^{-1} + 5^{-1})^0\\)",
     ["1", "0", "\\(\\frac{47}{60}\\)", "12"],
     "A", "OSC", "easy",
     "Any non-zero real expression raised to the power 0 equals 1: \\(x^0 = 1\\). Since \\(3^{-1} + 4^{-1} + 5^{-1} \\neq 0\\), the result is 1."),

    # 25
    ("Evaluate: \\(\\left\\{ \\left(-\\frac{2}{3}\\right)^{-2} \\right\\}^2\\)",
     ["\\(\\frac{81}{16}\\)", "\\(\\frac{16}{81}\\)", "\\(-\\frac{81}{16}\\)", "\\(\\frac{9}{4}\\)"],
     "A", "OSC", "medium",
     "\\(\\left(-\\frac{2}{3}\\right)^{-2} = \\left(-\\frac{3}{2}\\right)^2 = \\frac{9}{4}\\). Squaring that gives \\(\\left(\\frac{9}{4}\\right)^2 = \\frac{81}{16}\\)."),

    # 26
    ("What is the value of \\(x\\) if \\(3^{x} = \\frac{1}{243}\\)?",
     ["\\(-5\\)", "5", "\\(-4\\)", "\\(-6\\)"],
     "A", "OSC", "medium",
     "\\(243 = 3^5\\), so \\(\\frac{1}{243} = 3^{-5}\\). Comparing exponents in \\(3^x = 3^{-5}\\) yields \\(x = -5\\)."),

    # 27
    ("What is the value of \\(x\\) if \\(5^{2x-1} = \\frac{1}{125}\\)?",
     ["\\(-1\\)", "1", "\\(-2\\)", "2"],
     "A", "OSC", "medium",
     "\\(\\frac{1}{125} = 5^{-3}\\). Therefore \\(2x - 1 = -3 \\implies 2x = -2 \\implies x = -1\\)."),

    # 28
    ("Find the value of \\(m\\) for which \\(7^m \\div 7^{-3} = 7^5\\).",
     ["2", "8", "\\(-2\\)", "15"],
     "A", "OSC", "medium",
     "Using quotient of powers rule: \\(7^{m - (-3)} = 7^{m + 3}\\). Given \\(7^{m+3} = 7^5\\), equating powers yields \\(m + 3 = 5 \\implies m = 2\\)."),

    # 29
    ("Evaluate: \\(\\left(\\frac{5}{8}\\right)^{-7} \\times \\left(\\frac{8}{5}\\right)^{-5}\\)",
     ["\\(\\frac{25}{64}\\)", "\\(\\frac{64}{25}\\)", "1", "\\(\\frac{5}{8}\\)"],
     "A", "OSC", "medium",
     "Rewrite \\(\\left(\\frac{8}{5}\\right)^{-5}\\) as \\(\\left(\\frac{5}{8}\\right)^5\\). Then \\(\\left(\\frac{5}{8}\\right)^{-7} \\times \\left(\\frac{5}{8}\\right)^5 = \\left(\\frac{5}{8}\\right)^{-7 + 5} = \\left(\\frac{5}{8}\\right)^{-2} = \\left(\\frac{8}{5}\\right)^2 = \\frac{64}{25}\\). Wait, \\(\\left(\\frac{8}{5}\\right)^2 = \\frac{64}{25}\\). Let's check: \\(\\left(\\frac{5}{8}\\right)^{-7} = \\left(\\frac{8}{5}\\right)^7\\). Multiplying by \\(\\left(\\frac{8}{5}\\right)^{-5}\\) gives \\(\\left(\\frac{8}{5}\\right)^{7-5} = \\left(\\frac{8}{5}\\right)^2 = \\frac{64}{25}\\)."),

    # 30
    ("What is the value of \\(\\left(6^{-1} - 8^{-1}\\right)^{-1}\\)?",
     ["24", "\\(\\frac{1}{24}\\)", "\\(-24\\)", "48"],
     "A", "OSC", "medium",
     "\\(6^{-1} = \\frac{1}{6}\\) and \\(8^{-1} = \\frac{1}{8}\\). Difference: \\(\\frac{1}{6} - \\frac{1}{8} = \\frac{4 - 3}{24} = \\frac{1}{24}\\). Taking the reciprocal: \\(\\left(\\frac{1}{24}\\right)^{-1} = 24\\)."),

    # 31
    ("What is the value of \\(\\left(2^{-1} + 3^{-1}\\right)^{-1}\\)?",
     ["\\(\\frac{6}{5}\\)", "\\(\\frac{5}{6}\\)", "5", "6"],
     "A", "OSC", "medium",
     "\\(2^{-1} + 3^{-1} = \\frac{1}{2} + \\frac{1}{3} = \\frac{5}{6}\\). The reciprocal is \\(\\left(\\frac{5}{6}\\right)^{-1} = \\frac{6}{5}\\)."),

    # 32
    ("Evaluate: \\(\\left(\\frac{1}{3}\\right)^{-1} - \\left(\\frac{1}{4}\\right)^{-1}\\)",
     ["\\(-1\\)", "1", "7", "\\(\\frac{1}{12}\\)"],
     "A", "OSC", "easy",
     "\\(\\left(\\frac{1}{3}\\right)^{-1} = 3\\) and \\(\\left(\\frac{1}{4}\\right)^{-1} = 4\\). Subtracting: \\(3 - 4 = -1\\)."),

    # 33
    ("Evaluate: \\(\\left[ \\left(\\frac{1}{3}\\right)^{-1} - \\left(\\frac{1}{4}\\right)^{-1} \\right]^{-1}\\)",
     ["\\(-1\\)", "1", "\\(-\\frac{1}{12}\\)", "12"],
     "A", "OSC", "easy",
     "Inside brackets: \\(3 - 4 = -1\\). Then \\((-1)^{-1} = \\frac{1}{-1} = -1\\)."),

    # 34
    ("Assertion (A): For any non-zero number \\(a\\), \\(a^{-1} = \\frac{1}{a}\\).\nReason (R): The product \\(a \\times a^{-1} = a^{1 + (-1)} = a^0 = 1\\), meaning \\(a^{-1}\\) is the multiplicative inverse of \\(a\\).",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "By definition of negative exponents and the product law of exponents, multiplying \\(a\\) by \\(a^{-1}\\) yields \\(a^0 = 1\\), proving that \\(a^{-1}\\) is the multiplicative inverse \\(\\frac{1}{a}\\)."),

    # 35
    ("Assertion (A): \\((-5)^{-2} = \\frac{1}{25}\\).\nReason (R): A negative base raised to any negative power always yields a positive number.",
     ["(A) is true but (R) is false",
      "Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "(A) is true because \\((-5)^{-2} = \\frac{1}{(-5)^2} = \\frac{1}{25}\\). But (R) is false because if the power is odd (e.g. \\((-5)^{-3} = -\\frac{1}{125}\\)), the result is negative."),

    # 36
    ("True or False: The multiplicative inverse of \\((-2)^4\\) is \\((-2)^{-4}\\).",
     ["True", "False"],
     "A", "OTF", "easy",
     "For any non-zero base \\(a\\), the multiplicative inverse of \\(a^m\\) is \\(a^{-m}\\) because \\(a^m \\times a^{-m} = a^0 = 1\\)."),

    # 37
    ("True or False: \\(a^{-m} = -a^m\\) for all non-zero numbers \\(a\\).",
     ["False", "True"],
     "A", "OTF", "easy",
     "A negative exponent indicates reciprocal, not negation: \\(a^{-m} = \\frac{1}{a^m} \\neq -a^m\\). For example, \\(2^{-3} = \\frac{1}{8} \\neq -8\\)."),

    # 38
    ("Fill in the blank: The multiplicative inverse of \\(\\left(\\frac{a}{b}\\right)^{-m}\\) is _____.",
     ["\\(\\left(\\frac{a}{b}\\right)^m\\)", "\\(\\left(\\frac{b}{a}\\right)^m\\)", "\\(-\\left(\\frac{a}{b}\\right)^m\\)", "\\(\\left(\\frac{a}{b}\\right)^{-m}\\)"],
     "A", "OFB", "easy",
     "The product \\(\\left(\\frac{a}{b}\\right)^{-m} \\times \\left(\\frac{a}{b}\\right)^m = \\left(\\frac{a}{b}\\right)^0 = 1\\), so its multiplicative inverse is \\(\\left(\\frac{a}{b}\\right)^m\\)."),

    # 39
    ("Fill in the blank: In the decimal expanded form of \\(0.045\\), the digit 5 is multiplied by _____.",
     ["\\(10^{-3}\\)", "\\(10^{-2}\\)", "\\(10^{-1}\\)", "\\(10^{-4}\\)"],
     "A", "OFB", "easy",
     "The digit 5 is in the thousandths place, which is represented by \\(10^{-3}\\)."),

    # 40
    ("What is the numerical integer value of \\(\\left(\\frac{1}{5}\\right)^{-3}\\)?",
     ["125", "25", "\\(-125\\)", "\\(\\frac{1}{125}\\)"],
     "A", "ONE", "easy",
     "\\(\\left(\\frac{1}{5}\\right)^{-3} = 5^3 = 5 \\times 5 \\times 5 = 125\\)."),
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    ("Find the value of \\(3^{-2}\\).",
     ["\\(\\frac{1}{9}\\)", "\\(-9\\)", "\\(\\frac{1}{6}\\)", "\\(-6\\)"],
     "A", "OSC", "easy",
     "\\(3^{-2} = \\frac{1}{3^2} = \\frac{1}{9}\\)."),

    # 42
    ("Find the value of \\(10^{-4}\\).",
     ["\\(\\frac{1}{10000}\\)", "\\(\\frac{1}{1000}\\)", "\\(-10000\\)", "0.00001"],
     "A", "OSC", "easy",
     "\\(10^{-4} = \\frac{1}{10^4} = \\frac{1}{10000} = 0.0001\\)."),

    # 43
    ("Find the value of \\((-4)^{-2}\\).",
     ["\\(\\frac{1}{16}\\)", "\\(-\\frac{1}{16}\\)", "\\(-16\\)", "16"],
     "A", "OSC", "easy",
     "\\((-4)^{-2} = \\frac{1}{(-4)^2} = \\frac{1}{16}\\)."),

    # 44
    ("Find the value of \\((-4)^{-3}\\).",
     ["\\(-\\frac{1}{64}\\)", "\\(\\frac{1}{64}\\)", "\\(-64\\)", "64"],
     "A", "OSC", "easy",
     "\\((-4)^{-3} = \\frac{1}{(-4)^3} = \\frac{1}{-64} = -\\frac{1}{64}\\)."),

    # 45
    ("What is the multiplicative inverse of \\(8^{-2}\\)?",
     ["\\(8^2\\)", "\\(-8^2\\)", "\\(8^{-2}\\)", "\\(\\frac{1}{64}\\)"],
     "A", "OSC", "easy",
     "The multiplicative inverse of \\(a^{-m}\\) is \\(a^m\\). For \\(8^{-2}\\), it is \\(8^2 = 64\\)."),

    # 46
    ("What is the multiplicative inverse of \\(11^{-3}\\)?",
     ["\\(11^3\\)", "\\(-11^3\\)", "\\(11^{-3}\\)", "\\(\\frac{1}{1331}\\)"],
     "A", "OSC", "easy",
     "The multiplicative inverse of \\(11^{-3}\\) is \\(11^3 = 1331\\)."),

    # 47
    ("What is the value of \\(\\left(\\frac{3}{5}\\right)^{-2}\\)?",
     ["\\(\\frac{25}{9}\\)", "\\(\\frac{9}{25}\\)", "\\(-\\frac{25}{9}\\)", "\\(-\\frac{9}{25}\\)"],
     "A", "OSC", "easy",
     "\\(\\left(\\frac{3}{5}\\right)^{-2} = \\left(\\frac{5}{3}\\right)^2 = \\frac{25}{9}\\)."),

    # 48
    ("What is the value of \\(\\left(-\\frac{1}{5}\\right)^{-3}\\)?",
     ["\\(-125\\)", "125", "\\(-\\frac{1}{125}\\)", "\\(\\frac{1}{125}\\)"],
     "A", "OSC", "easy",
     "\\(\\left(-\\frac{1}{5}\\right)^{-3} = (-5)^3 = -125\\)."),

    # 49
    ("What is the value of \\(\\left(-\\frac{2}{5}\\right)^{-4}\\)?",
     ["\\(\\frac{625}{16}\\)", "\\(-\\frac{625}{16}\\)", "\\(\\frac{16}{625}\\)", "\\(-\\frac{16}{625}\\)"],
     "A", "OSC", "medium",
     "\\(\\left(-\\frac{2}{5}\\right)^{-4} = \\left(-\\frac{5}{2}\\right)^4 = \\frac{(-5)^4}{2^4} = \\frac{625}{16}\\)."),

    # 50
    ("Write \\(0.0005\\) as a power of 10 times an integer.",
     ["\\(5 \\times 10^{-4}\\)", "\\(5 \\times 10^{-3}\\)", "\\(5 \\times 10^{-5}\\)", "\\(50 \\times 10^{-4}\\)"],
     "A", "OSC", "easy",
     "\\(0.0005 = \\frac{5}{10000} = 5 \\times 10^{-4}\\)."),

    # 51
    ("Write \\(0.000032\\) in terms of powers of 10.",
     ["\\(3.2 \\times 10^{-5}\\)", "\\(32 \\times 10^{-4}\\)", "\\(3.2 \\times 10^{-4}\\)", "\\(32 \\times 10^{-6}\\)"],
     "A", "OSC", "easy",
     "Moving decimal 5 places right gives \\(3.2 \\times 10^{-5}\\)."),

    # 52
    ("Expand \\(235.14\\) using powers of 10.",
     ["\\(2 \\times 10^2 + 3 \\times 10^1 + 5 \\times 10^0 + 1 \\times 10^{-1} + 4 \\times 10^{-2}\\)",
      "\\(2 \\times 10^3 + 3 \\times 10^2 + 5 \\times 10^1 + 1 \\times 10^{-1} + 4 \\times 10^{-2}\\)",
      "\\(2 \\times 10^2 + 3 \\times 10^1 + 5 \\times 10^0 + 1 \\times 10^{-2} + 4 \\times 10^{-3}\\)",
      "\\(2 \\times 10^1 + 3 \\times 10^0 + 5 \\times 10^{-1} + 1 \\times 10^{-2} + 4 \\times 10^{-3}\\)"],
     "A", "OSC", "medium",
     "Hundreds: \\(2 \\times 10^2\\), Tens: \\(3 \\times 10^1\\), Units: \\(5 \\times 10^0\\), Tenths: \\(1 \\times 10^{-1}\\), Hundredths: \\(4 \\times 10^{-2}\\)."),

    # 53
    ("What number has the expanded form \\(5 \\times 10^2 + 8 \\times 10^0 + 3 \\times 10^{-1} + 2 \\times 10^{-3}\\)?",
     ["508.302", "580.32", "508.32", "58.302"],
     "A", "OSC", "medium",
     "Hundreds: 5, Tens: 0, Units: 8, Tenths: 3, Hundredths: 0, Thousandths: 2. This gives \\(508.302\\)."),

    # 54
    ("Evaluate: \\(4^{-1} + 8^{-1}\\)",
     ["\\(\\frac{3}{8}\\)", "\\(\\frac{1}{12}\\)", "\\(\\frac{1}{4}\\)", "\\(\\frac{5}{8}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{1}{4} + \\frac{1}{8} = \\frac{2 + 1}{8} = \\frac{3}{8}\\)."),

    # 55
    ("Evaluate: \\((3^{-1} + 6^{-1})^{-1}\\)",
     ["2", "\\(\\frac{1}{2}\\)", "\\(\\frac{9}{18}\\)", "9"],
     "A", "OSC", "medium",
     "\\(3^{-1} + 6^{-1} = \\frac{1}{3} + \\frac{1}{6} = \\frac{2 + 1}{6} = \\frac{3}{6} = \\frac{1}{2}\\). Taking reciprocal gives 2."),

    # 56
    ("Evaluate: \\((5^{-1} - 10^{-1})^{-1}\\)",
     ["10", "\\(\\frac{1}{10}\\)", "5", "\\(\\frac{1}{5}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{1}{5} - \\frac{1}{10} = \\frac{2 - 1}{10} = \\frac{1}{10}\\). Reciprocal is 10."),

    # 57
    ("Evaluate: \\(\\left(\\frac{1}{4}\\right)^{-2} - \\left(\\frac{1}{3}\\right)^{-2}\\)",
     ["7", "\\(-7\\)", "1", "25"],
     "A", "OSC", "easy",
     "\\(4^2 - 3^2 = 16 - 9 = 7\\)."),

    # 58
    ("Evaluate: \\(2^{-3} + 4^{-2}\\)",
     ["\\(\\frac{3}{16}\\)", "\\(\\frac{1}{8}\\)", "\\(\\frac{1}{16}\\)", "\\(\\frac{5}{16}\\)"],
     "A", "OSC", "medium",
     "\\(2^{-3} = \\frac{1}{8} = \\frac{2}{16}\\) and \\(4^{-2} = \\frac{1}{16}\\). Sum: \\(\\frac{2}{16} + \\frac{1}{16} = \\frac{3}{16}\\)."),

    # 59
    ("Evaluate: \\(\\left(-\\frac{1}{2}\\right)^{-5}\\)",
     ["\\(-32\\)", "32", "\\(-\\frac{1}{32}\\)", "\\(\\frac{1}{32}\\)"],
     "A", "OSC", "easy",
     "\\((-2)^5 = -32\\)."),

    # 60
    ("Find the value of \\(x\\) if \\(2^{x} = \\frac{1}{64}\\).",
     ["\\(-6\\)", "6", "\\(-5\\)", "\\(-7\\)"],
     "A", "OSC", "easy",
     "\\(64 = 2^6\\), so \\(\\frac{1}{64} = 2^{-6}\\). Hence \\(x = -6\\)."),

    # 61
    ("Find the value of \\(n\\) if \\(4^{n} = \\frac{1}{256}\\).",
     ["\\(-4\\)", "4", "\\(-3\\)", "\\(-5\\)"],
     "A", "OSC", "easy",
     "\\(256 = 4^4\\), so \\(4^n = 4^{-4} \\implies n = -4\\)."),

    # 62
    ("Evaluate: \\((4^0 + 4^{-1}) \\times 2^2\\)",
     ["5", "4", "8", "6"],
     "A", "OSC", "medium",
     "\\(4^0 = 1\\) and \\(4^{-1} = \\frac{1}{4}\\). Inside brackets: \\(1 + \\frac{1}{4} = \\frac{5}{4}\\). Multiplying by \\(2^2 = 4\\): \\(\\frac{5}{4} \\times 4 = 5\\)."),

    # 63
    ("Evaluate: \\((2^{-1} \\times 3^{-1})^2\\)",
     ["\\(\\frac{1}{36}\\)", "\\(\\frac{1}{6}\\)", "\\(\\frac{1}{12}\\)", "\\(\\frac{1}{18}\\)"],
     "A", "OSC", "easy",
     "\\(2^{-1} \\times 3^{-1} = \\frac{1}{6}\\). Squaring: \\(\\left(\\frac{1}{6}\\right)^2 = \\frac{1}{36}\\)."),

    # 64
    ("Evaluate: \\((3^{-1} + 4^{-1})^{-1} \\times 7\\)",
     ["12", "\\(\\frac{7}{12}\\)", "\\(\\frac{12}{7}\\)", "7"],
     "A", "OSC", "medium",
     "\\(\\frac{1}{3} + \\frac{1}{4} = \\frac{7}{12}\\). Reciprocal is \\(\\frac{12}{7}\\). Multiplying by 7: \\(\\frac{12}{7} \\times 7 = 12\\)."),

    # 65
    ("Evaluate: \\(\\left(\\frac{1}{2}\\right)^{-1} + \\left(\\frac{1}{3}\\right)^{-1} + \\left(\\frac{1}{4}\\right)^{-1}\\)",
     ["9", "\\(\\frac{1}{9}\\)", "10", "24"],
     "A", "OSC", "easy",
     "\\(2 + 3 + 4 = 9\\)."),

    # 66
    ("True or False: \\((a + b)^{-1} = a^{-1} + b^{-1}\\) for all non-zero numbers \\(a, b\\).",
     ["False", "True"],
     "A", "OTF", "easy",
     "Taking reciprocal does not distribute over addition. For instance, \\((1 + 1)^{-1} = \\frac{1}{2}\\), but \\(1^{-1} + 1^{-1} = 1 + 1 = 2\\)."),

    # 67
    ("True or False: If \\(x > 1\\), then \\(x^{-1} < 1\\).",
     ["True", "False"],
     "A", "OTF", "easy",
     "For any number \\(x > 1\\), its reciprocal \\(\\frac{1}{x}\\) lies strictly between 0 and 1, so \\(x^{-1} < 1\\)."),

    # 68
    ("Fill in the blank: The value of \\((-1)^{-2n}\\) for any integer \\(n\\) is always _____.",
     ["1", "\\(-1\\)", "0", "Undefined"],
     "A", "OFB", "easy",
     "Since \\(2n\\) is always an even integer, \\((-1)^{2n} = 1\\), so \\((-1)^{-2n} = \\frac{1}{1} = 1\\)."),

    # 69
    ("Fill in the blank: \\(10^{-3}\\) written as a decimal fraction is _____.",
     ["0.001", "0.01", "0.0001", "0.1"],
     "A", "OFB", "easy",
     "\\(10^{-3} = \\frac{1}{10^3} = \\frac{1}{1000} = 0.001\\)."),

    # 70
    ("What is the integer value of \\(\\left(\\frac{1}{3}\\right)^{-4}\\)?",
     ["81", "27", "12", "\\(-81\\)"],
     "A", "ONE", "easy",
     "\\(\\left(\\frac{1}{3}\\right)^{-4} = 3^4 = 81\\)."),
]

# 12 MOCK / FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Powers of 10: Step-Down Division Ladder</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Step boxes -->
    <rect x="15" y="25" width="55" height="40" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2"/>
    <text x="42" y="45" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">10²</text>
    <text x="42" y="60" fill="#e2e8f0" font-size="10" text-anchor="middle">100</text>
    <!-- Arrow 1 -->
    <text x="80" y="48" fill="#f59e0b" font-size="11" text-anchor="middle">÷10</text>
    <!-- Step 2 -->
    <rect x="95" y="25" width="55" height="40" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2"/>
    <text x="122" y="45" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">10¹</text>
    <text x="122" y="60" fill="#e2e8f0" font-size="10" text-anchor="middle">10</text>
    <!-- Arrow 2 -->
    <text x="160" y="48" fill="#f59e0b" font-size="11" text-anchor="middle">÷10</text>
    <!-- Step 3 -->
    <rect x="175" y="25" width="55" height="40" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="202" y="45" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">10⁰</text>
    <text x="202" y="60" fill="#e2e8f0" font-size="10" text-anchor="middle">1</text>
    <!-- Arrow 3 -->
    <text x="240" y="48" fill="#f59e0b" font-size="11" text-anchor="middle">÷10</text>
    <!-- Step 4 -->
    <rect x="255" y="25" width="70" height="40" rx="6" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
    <text x="290" y="45" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">10⁻¹</text>
    <text x="290" y="60" fill="#e2e8f0" font-size="10" text-anchor="middle">1/10 = 0.1</text>
    <!-- Rule explanation -->
    <rect x="40" y="90" width="260" height="45" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="170" y="110" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Pattern: Decreasing power by 1 divides value by 10</text>
    <text x="170" y="127" fill="#cbd5e1" font-size="11" text-anchor="middle">10⁻² = 1/100 = 0.01  |  10⁻³ = 1/1000 = 0.001</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Following the pattern in the ladder diagram, what is the value of \(10^{-3}\)?</p>
</div>""",
     ["0.001", "0.01", "0.0001", "-1000"],
     "A", "OSC", "easy",
     "Each step rightward divides by 10. Following \(10^{-1} = 0.1\) and \(10^{-2} = 0.01\), dividing by 10 once more gives \(10^{-3} = 0.001\)."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Multiplicative Inverse Balance</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Seesaw Balance -->
    <polygon points="170,110 160,135 180,135" fill="#64748b"/>
    <line x1="60" y1="95" x2="280" y2="95" stroke="#94a3b8" stroke-width="3"/>
    <!-- Left pan: 2^4 -->
    <rect x="65" y="55" width="60" height="40" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2"/>
    <text x="95" y="75" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">2⁴</text>
    <text x="95" y="90" fill="#e2e8f0" font-size="10" text-anchor="middle">= 16</text>
    <!-- Multiplication center operator -->
    <circle cx="170" cy="70" r="14" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="75" fill="#34d399" font-size="16" font-weight="bold" text-anchor="middle">×</text>
    <!-- Right pan: 2^(-4) -->
    <rect x="215" y="55" width="60" height="40" rx="6" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
    <text x="245" y="75" fill="#fde047" font-size="13" font-weight="bold" text-anchor="middle">2⁻⁴</text>
    <text x="245" y="90" fill="#e2e8f0" font-size="10" text-anchor="middle">= 1/16</text>
    <!-- Product Banner -->
    <rect x="70" y="15" width="200" height="25" rx="5" fill="#0f172a" stroke="#60a5fa" stroke-width="1.5"/>
    <text x="170" y="32" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Product = 16 × (1/16) = 1 = 2⁰</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the multiplicative inverse of \(3^{-4}\)?</p>
</div>""",
     ["3⁴", "-3⁴", "3⁻⁴", "-3⁻⁴"],
     "A", "OSC", "easy",
     "The multiplicative inverse of \(a^{-m}\) is \(a^m\) because \(a^{-m} \\times a^m = a^0 = 1\). Thus the multiplicative inverse of \(3^{-4}\) is \(3^4\)."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Fraction Inversion with Negative Exponents</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Expression 1: (a/b)^(-m) -->
    <rect x="30" y="30" width="100" height="70" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="70" y="60" fill="#93c5fd" font-size="16" font-weight="bold" text-anchor="middle">( 2 / 5 )</text>
    <text x="115" y="48" fill="#f59e0b" font-size="13" font-weight="bold" text-anchor="middle">⁻³</text>
    <!-- Transition Arrow -->
    <path d="M 145,65 L 185,65" stroke="#f59e0b" stroke-width="3" fill="none"/>
    <polygon points="185,60 195,65 185,70" fill="#f59e0b"/>
    <!-- Inverted expression: (b/a)^m -->
    <rect x="205" y="30" width="105" height="70" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="247" y="60" fill="#6ee7b7" font-size="16" font-weight="bold" text-anchor="middle">( 5 / 2 )</text>
    <text x="292" y="48" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">³</text>
    <!-- Value Result -->
    <text x="170" y="130" fill="#fde047" font-size="13" font-weight="bold" text-anchor="middle">= 5³ / 2³ = 125 / 8</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Using the identity \(\left(\frac{a}{b}\right)^{-m} = \left(\frac{b}{a}\right)^m\), evaluate \(\left(\frac{2}{5}\right)^{-3}\).</p>
</div>""",
     ["125/8", "8/125", "-125/8", "-8/125"],
     "A", "OSC", "easy",
     "\\(\\left(\\frac{2}{5}\\right)^{-3} = \\left(\\frac{5}{2}\\right)^3 = \\frac{5^3}{2^3} = \\frac{125}{8}\\)."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Decimal Place Value Grid with Powers of 10</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Columns for 10^2, 10^1, 10^0, decimal, 10^-1, 10^-2 -->
    <g fill="#334155" stroke="#475569" stroke-width="1">
      <rect x="20" y="25" width="45" height="40"/>
      <rect x="70" y="25" width="45" height="40"/>
      <rect x="120" y="25" width="45" height="40"/>
      <circle cx="170" cy="65" r="4" fill="#f59e0b"/>
      <rect x="175" y="25" width="45" height="40"/>
      <rect x="225" y="25" width="45" height="40"/>
      <rect x="275" y="25" width="45" height="40"/>
    </g>
    <!-- Exponent labels -->
    <text x="42" y="42" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">10²</text>
    <text x="92" y="42" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">10¹</text>
    <text x="142" y="42" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">10⁰</text>
    <text x="197" y="42" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">10⁻¹</text>
    <text x="247" y="42" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">10⁻²</text>
    <text x="297" y="42" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle">10⁻³</text>
    <!-- Place values names -->
    <text x="42" y="58" fill="#cbd5e1" font-size="9" text-anchor="middle">100s</text>
    <text x="92" y="58" fill="#cbd5e1" font-size="9" text-anchor="middle">10s</text>
    <text x="142" y="58" fill="#cbd5e1" font-size="9" text-anchor="middle">1s</text>
    <text x="197" y="58" fill="#cbd5e1" font-size="9" text-anchor="middle">1/10</text>
    <text x="247" y="58" fill="#cbd5e1" font-size="9" text-anchor="middle">1/100</text>
    <text x="297" y="58" fill="#cbd5e1" font-size="9" text-anchor="middle">1/1000</text>
    <!-- Sample Number: 3 4 5 . 6 7 8 -->
    <text x="170" y="105" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">Number: 345.678</text>
    <text x="170" y="128" fill="#38bdf8" font-size="11" text-anchor="middle">Digit 7 place value = 7 × 10⁻² = 0.07</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">In the decimal number \(345.678\), what is the place value of the digit \(7\)?</p>
</div>""",
     ["\\(7 \\times 10^{-2}\\)", "\\(7 \\times 10^{-1}\\)", "\\(7 \\times 10^{-3}\\)", "\\(7 \\times 10^1\\)"],
     "A", "OSC", "easy",
     "The digit 7 is two places to the right of the decimal point, representing hundredths. Hence its value is \\(7 \\times 10^{-2} = 0.07\\)."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Sign Behavior of Negative Base with Negative Exponent</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Case A: Even power -->
    <rect x="25" y="25" width="135" height="95" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
    <text x="92" y="48" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">Even Power: (-2)⁻⁴</text>
    <text x="92" y="70" fill="#ffffff" font-size="12" text-anchor="middle">= 1 / (-2)⁴</text>
    <text x="92" y="90" fill="#ffffff" font-size="12" text-anchor="middle">= 1 / 16</text>
    <text x="92" y="110" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">(POSITIVE)</text>
    <!-- Case B: Odd power -->
    <rect x="180" y="25" width="135" height="95" rx="6" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
    <text x="247" y="48" fill="#fca5a5" font-size="12" font-weight="bold" text-anchor="middle">Odd Power: (-2)⁻³</text>
    <text x="247" y="70" fill="#ffffff" font-size="12" text-anchor="middle">= 1 / (-2)³</text>
    <text x="247" y="90" fill="#ffffff" font-size="12" text-anchor="middle">= 1 / (-8)</text>
    <text x="247" y="110" fill="#f87171" font-size="12" font-weight="bold" text-anchor="middle">(NEGATIVE)</text>
    <!-- Rule footnote -->
    <text x="170" y="138" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Sign depends solely on whether exponent is even or odd</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the value of \((-5)^{-3}\)?</p>
</div>""",
     ["-1/125", "1/125", "-125", "125"],
     "A", "OSC", "easy",
     "\\((-5)^{-3} = \\frac{1}{(-5)^3}\\). Since the exponent 3 is odd, \\((-5)^3 = -125\\). Thus \\((-5)^{-3} = -\\frac{1}{125}\\)."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Parentheses vs No Parentheses Distinction</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Left Box: (-3)^(-2) -->
    <rect x="25" y="25" width="135" height="95" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="92" y="48" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">(-3)⁻²</text>
    <text x="92" y="70" fill="#cbd5e1" font-size="11" text-anchor="middle">Base is (-3)</text>
    <text x="92" y="90" fill="#cbd5e1" font-size="11" text-anchor="middle">= 1 / [(-3)²]</text>
    <text x="92" y="110" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">= +1 / 9</text>
    <!-- Right Box: -3^(-2) -->
    <rect x="180" y="25" width="135" height="95" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="247" y="48" fill="#fbbf24" font-size="13" font-weight="bold" text-anchor="middle">-3⁻²</text>
    <text x="247" y="70" fill="#cbd5e1" font-size="11" text-anchor="middle">Base is 3 (negated)</text>
    <text x="247" y="90" fill="#cbd5e1" font-size="11" text-anchor="middle">= - (1 / 3²)</text>
    <text x="247" y="110" fill="#f87171" font-size="12" font-weight="bold" text-anchor="middle">= -1 / 9</text>
    <text x="170" y="138" fill="#e2e8f0" font-size="11" text-anchor="middle">Parentheses dictate whether the minus sign is squared</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the value of \(-4^{-2}\)?</p>
</div>""",
     ["-1/16", "1/16", "-8", "16"],
     "A", "OSC", "medium",
     "Without parentheses, the exponent applies only to the base 4, not the negative sign: \\(-4^{-2} = -\\frac{1}{4^2} = -\\frac{1}{16}\\)."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Fractional Negative Power Reciprocal Swap</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Left fraction: 1 / 3^(-3) -->
    <rect x="40" y="30" width="100" height="70" rx="8" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2"/>
    <text x="90" y="52" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">1</text>
    <line x1="55" y1="62" x2="125" y2="62" stroke="#60a5fa" stroke-width="2"/>
    <text x="90" y="85" fill="#93c5fd" font-size="14" font-weight="bold" text-anchor="middle">3⁻³</text>
    <!-- Arrow -->
    <path d="M 155,65 L 195,65" stroke="#f59e0b" stroke-width="3" fill="none"/>
    <polygon points="195,60 205,65 195,70" fill="#f59e0b"/>
    <!-- Right result: 3^3 = 27 -->
    <rect x="215" y="30" width="85" height="70" rx="8" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="257" y="60" fill="#6ee7b7" font-size="16" font-weight="bold" text-anchor="middle">3³</text>
    <text x="257" y="85" fill="#ffffff" font-size="14" text-anchor="middle">= 27</text>
    <!-- Footnote -->
    <text x="170" y="130" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Rule: 1 / a⁻ᵐ = aᵐ</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the value of \(\frac{1}{2^{-5}}\)?</p>
</div>""",
     ["32", "1/32", "-32", "-1/32"],
     "A", "OSC", "easy",
     "Moving a factor with a negative exponent from denominator to numerator reverses the exponent sign: \\(\\frac{1}{2^{-5}} = 2^5 = 32\\)."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Sum of Reciprocals vs Power of Sum</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Side A: 2^(-1) + 3^(-1) -->
    <rect x="25" y="30" width="135" height="75" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="92" y="55" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">2⁻¹ + 3⁻¹</text>
    <text x="92" y="75" fill="#cbd5e1" font-size="12" text-anchor="middle">= 1/2 + 1/3</text>
    <text x="92" y="95" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">= 5 / 6</text>
    <!-- NOT EQUAL symbol -->
    <text x="170" y="70" fill="#ef4444" font-size="22" font-weight="bold" text-anchor="middle">≠</text>
    <!-- Side B: (2 + 3)^(-1) -->
    <rect x="180" y="30" width="135" height="75" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <text x="247" y="55" fill="#fca5a5" font-size="13" font-weight="bold" text-anchor="middle">(2 + 3)⁻¹</text>
    <text x="247" y="75" fill="#cbd5e1" font-size="12" text-anchor="middle">= 5⁻¹</text>
    <text x="247" y="95" fill="#f87171" font-size="13" font-weight="bold" text-anchor="middle">= 1 / 5</text>
    <text x="170" y="132" fill="#fbbf24" font-size="11" text-anchor="middle">(a + b)⁻¹ DOES NOT EQUAL a⁻¹ + b⁻¹</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the exact value of \(3^{-1} + 6^{-1}\)?</p>
</div>""",
     ["1/2", "1/9", "2/9", "1/18"],
     "A", "OSC", "easy",
     "\\(3^{-1} + 6^{-1} = \\frac{1}{3} + \\frac{1}{6} = \\frac{2 + 1}{6} = \\frac{3}{6} = \\frac{1}{2}\\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Solving Exponential Equations with Negative Powers</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Equation Display -->
    <text x="170" y="30" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">Solve for x:  5ˣ = 1 / 625</text>
    <!-- Step 1: Express RHS in prime base -->
    <rect x="50" y="45" width="110" height="40" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="105" y="65" fill="#93c5fd" font-size="11" text-anchor="middle">625 = 5⁴</text>
    <text x="105" y="78" fill="#e2e8f0" font-size="10" text-anchor="middle">1/625 = 5⁻⁴</text>
    <!-- Arrow -->
    <path d="M 170,65 L 195,65" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="195,60 205,65 195,70" fill="#f59e0b"/>
    <!-- Step 2: Equate bases -->
    <rect x="215" y="45" width="85" height="40" rx="6" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
    <text x="257" y="65" fill="#6ee7b7" font-size="11" text-anchor="middle">5ˣ = 5⁻⁴</text>
    <text x="257" y="78" fill="#fcd34d" font-size="12" font-weight="bold" text-anchor="middle">x = -4</text>
    <!-- Bottom banner -->
    <text x="170" y="125" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Since bases match (5 = 5), exponents must be equal</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the value of \(x\) if \(2^{x} = \frac{1}{128}\)?</p>
</div>""",
     ["-7", "7", "-6", "-8"],
     "A", "OSC", "easy",
     "\\(128 = 2^7\\), so \\(\\frac{1}{128} = 2^{-7}\\). Therefore \\(2^x = 2^{-7} \\implies x = -7\\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Fractional Negative Power Double Inversion</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Nested expression -->
    <rect x="40" y="25" width="110" height="80" rx="6" fill="#1e293b" stroke="#6366f1" stroke-width="2"/>
    <text x="95" y="55" fill="#a5b4fc" font-size="13" font-weight="bold" text-anchor="middle">[ (1/2)⁻¹ ]⁻¹</text>
    <text x="95" y="80" fill="#cbd5e1" font-size="11" text-anchor="middle">= [ 2 ]⁻¹</text>
    <!-- Arrow -->
    <path d="M 165,65 L 195,65" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="195,60 205,65 195,70" fill="#f59e0b"/>
    <!-- Final result -->
    <rect x="210" y="25" width="90" height="80" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="255" y="60" fill="#6ee7b7" font-size="16" font-weight="bold" text-anchor="middle">1 / 2</text>
    <text x="255" y="85" fill="#e2e8f0" font-size="11" text-anchor="middle">Back to start</text>
    <!-- Footnote -->
    <text x="170" y="132" fill="#fbbf24" font-size="11" text-anchor="middle">Inverting twice returns to the original rational number</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the value of \(\left[ \left(\frac{3}{7}\right)^{-1} \right]^{-1}\)?</p>
</div>""",
     ["3/7", "7/3", "-3/7", "9/49"],
     "A", "OSC", "easy",
     "Applying power of a power: \\((-1) \\times (-1) = 1\\), so \\(\\left[\\left(\\frac{3}{7}\\right)^{-1}\\right]^{-1} = \\left(\\frac{3}{7}\\right)^1 = \\frac{3}{7}\\)."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Decimal Form to Negative Powers of 10</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Step cards -->
    <rect x="20" y="30" width="85" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="62" y="55" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">0.0003</text>
    <text x="62" y="73" fill="#94a3b8" font-size="10" text-anchor="middle">4 decimals</text>
    <!-- Arrow 1 -->
    <text x="120" y="60" fill="#f59e0b" font-size="16" text-anchor="middle">→</text>
    <!-- Fraction -->
    <rect x="135" y="25" width="85" height="65" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="177" y="50" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">3</text>
    <line x1="145" y1="58" x2="210" y2="58" stroke="#60a5fa" stroke-width="2"/>
    <text x="177" y="78" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">10000</text>
    <!-- Arrow 2 -->
    <text x="235" y="60" fill="#f59e0b" font-size="16" text-anchor="middle">→</text>
    <!-- Exponential Form -->
    <rect x="250" y="30" width="75" height="55" rx="6" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
    <text x="287" y="62" fill="#6ee7b7" font-size="13" font-weight="bold" text-anchor="middle">3 × 10⁻⁴</text>
    <!-- Bottom line -->
    <text x="170" y="125" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">n decimal places to right = multiplication by 10⁻ⁿ</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">How is \(0.00008\) expressed in exponential notation?</p>
</div>""",
     ["\\(8 \\times 10^{-5}\\)", "\\(8 \\times 10^{-4}\\)", "\\(8 \\times 10^{-6}\\)", "\\(80 \\times 10^{-5}\\)"],
     "A", "OSC", "easy",
     "Counting places to the right: the digit 8 is in the fifth decimal place (hundred-thousandths). Hence \\(0.00008 = \\frac{8}{100000} = 8 \\times 10^{-5}\\)."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Zero Exponent as the Boundary between Positive and Negative Powers</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Horizontal Power Axis -->
    <line x1="30" y1="80" x2="310" y2="80" stroke="#64748b" stroke-width="3"/>
    <!-- Left: Negative Powers (< 1) -->
    <rect x="35" y="45" width="80" height="30" rx="4" fill="#78350f" stroke="#f59e0b"/>
    <text x="75" y="65" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">2⁻¹ = 1/2</text>
    <!-- Center: 2^0 = 1 -->
    <rect x="135" y="40" width="70" height="35" rx="5" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="63" fill="#6ee7b7" font-size="13" font-weight="bold" text-anchor="middle">2⁰ = 1</text>
    <!-- Right: Positive Powers (> 1) -->
    <rect x="225" y="45" width="80" height="30" rx="4" fill="#1e3a8a" stroke="#3b82f6"/>
    <text x="265" y="65" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">2¹ = 2</text>
    <!-- Axis Labels -->
    <text x="75" y="105" fill="#fcd34d" font-size="11" text-anchor="middle">Fractions (&lt; 1)</text>
    <text x="170" y="105" fill="#6ee7b7" font-size="11" text-anchor="middle">Unit Pivot (1)</text>
    <text x="265" y="105" fill="#93c5fd" font-size="11" text-anchor="middle">Integers (&gt; 1)</text>
    <text x="170" y="135" fill="#e2e8f0" font-size="11" text-anchor="middle">a⁰ = aᵐ ÷ aᵐ = 1 for any a ≠ 0</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the value of \((7^0 + 5^0) \times 3^{-1}\)?</p>
</div>""",
     ["2/3", "1/3", "2", "3/2"],
     "A", "OSC", "easy",
     "\\(7^0 = 1\\) and \\(5^0 = 1\\), so \\(7^0 + 5^0 = 1 + 1 = 2\\). Multiplying by \\(3^{-1} = \\frac{1}{3}\\) gives \\(2 \\times \\frac{1}{3} = \\frac{2}{3}\\).")
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch2_topic1.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
