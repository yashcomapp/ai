# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-3-3.2
Topic: Associative, Distributive Properties & Identities
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-3-3.2"

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
    ("Which property of rational numbers states that \\((a + b) + c = a + (b + c)\\)?",
     ["Associative property of addition",
      "Commutative property of addition",
      "Distributive property",
      "Closure property of addition"],
     "A", "OSC", "easy",
     "The associative property of addition states that the grouping of addends does not affect the final sum: \\((a + b) + c = a + (b + c)\\)."),

    # 2
    ("What is the additive identity for rational numbers?",
     ["0", "1", "-1", "Any fraction"],
     "A", "OSC", "easy",
     "Zero is the additive identity because adding 0 to any rational number \\(a\\) leaves its value unchanged: \\(a + 0 = 0 + a = a\\)."),

    # 3
    ("What is the multiplicative identity for rational numbers?",
     ["1", "0", "-1", "Undefined"],
     "A", "OSC", "easy",
     "One is the multiplicative identity because multiplying any rational number \\(a\\) by 1 yields \\(a\\): \\(a \\times 1 = 1 \\times a = a\\)."),

    # 4
    ("What is the additive inverse of \\(\\frac{-7}{19}\\)?",
     ["\\(\\frac{7}{19}\\)", "\\(-\\frac{19}{7}\\)", "\\(\\frac{19}{7}\\)", "0"],
     "A", "OSC", "easy",
     "The additive inverse of a rational number \\(x\\) is \\(-x\\) such that \\(x + (-x) = 0\\). For \\(\\frac{-7}{19}\\), the additive inverse is \\(\\frac{7}{19}\\)."),

    # 5
    ("What is the multiplicative inverse (reciprocal) of \\(\\frac{-13}{21}\\)?",
     ["\\(-\\frac{21}{13}\\)", "\\(\\frac{21}{13}\\)", "\\(\\frac{13}{21}\\)", "1"],
     "A", "OSC", "easy",
     "The multiplicative inverse of \\(\\frac{p}{q}\\) is \\(\\frac{q}{p}\\) such that their product is 1. Hence for \\(\\frac{-13}{21}\\), it is \\(-\\frac{21}{13}\\)."),

    # 6
    ("Which property states that \\(a(b + c) = ab + ac\\) for any rational numbers \\(a, b, c\\)?",
     ["Distributive property of multiplication over addition",
      "Associative property of multiplication",
      "Commutative property of multiplication",
      "Closure property"],
     "A", "OSC", "easy",
     "The distributive property of multiplication over addition states that multiplying a sum by a number gives the same result as multiplying each addend individually and adding: \\(a(b + c) = ab + ac\\)."),

    # 7
    ("Which operations are associative for rational numbers?",
     ["Addition and Multiplication", "Subtraction and Division", "Addition and Subtraction", "Multiplication and Division"],
     "A", "OSC", "easy",
     "Addition and multiplication are associative for rational numbers. Subtraction and division are not associative."),

    # 8
    ("Evaluate using suitable rearrangement: \\(\\frac{3}{7} + \\left(\\frac{-6}{11}\\right) + \\left(\\frac{-8}{21}\\right) + \\left(\\frac{5}{22}\\right)\\)",
     ["\\(-\\frac{125}{462}\\)", "\\(\\frac{125}{462}\\)", "\\(-\\frac{1}{462}\\)", "\\(0\\)"],
     "A", "OSC", "hard",
     "Group terms with related denominators: \\(\\left[\\frac{3}{7} + \\left(-\\frac{8}{21}\\right)\\right] + \\left[\\left(-\\frac{6}{11}\\right) + \\frac{5}{22}\\right]\\). First group: \\(\\frac{9 - 8}{21} = \\frac{1}{21}\\). Second group: \\(\\frac{-12 + 5}{22} = -\\frac{7}{22}\\). Adding: \\(\\frac{1}{21} - \\frac{7}{22} = \\frac{22 - 147}{462} = -\\frac{125}{462}\\)."),

    # 9
    ("Evaluate using distributivity: \\(\\left(\\frac{-3}{7} \\times \\frac{5}{12}\\right) + \\left(\\frac{11}{12} \\times \\frac{-3}{7}\\right)\\)",
     ["\\(-\\frac{4}{7}\\)", "\\(\\frac{4}{7}\\)", "\\(-\\frac{16}{84}\\)", "\\(-\\frac{3}{7}\\)"],
     "A", "OSC", "medium",
     "Factor out \\(\\frac{-3}{7}\\): \\(\\frac{-3}{7} \\times \\left(\\frac{5}{12} + \\frac{11}{12}\\right) = \\frac{-3}{7} \\times \\frac{16}{12} = \\frac{-3}{7} \\times \\frac{4}{3} = -\\frac{4}{7}\\)."),

    # 10
    ("Evaluate using distributivity: \\(\\frac{7}{5} \\times \\left(\\frac{-3}{12}\\right) + \\frac{7}{5} \\times \\frac{5}{12}\\)",
     ["\\(\\frac{7}{30}\\)", "\\(-\\frac{7}{30}\\)", "\\(\\frac{14}{60}\\)", "\\(\\frac{7}{12}\\)"],
     "A", "OSC", "medium",
     "Factor out \\(\\frac{7}{5}\\): \\(\\frac{7}{5} \\times \\left(\\frac{-3 + 5}{12}\\right) = \\frac{7}{5} \\times \\frac{2}{12} = \\frac{7}{5} \\times \\frac{1}{6} = \\frac{7}{30}\\)."),

    # 11
    ("Evaluate using distributivity: \\(\\left(\\frac{-2}{3} \\times \\frac{5}{6}\\right) + \\left(\\frac{-2}{3} \\times \\frac{-2}{6}\\right)\\)",
     ["\\(-\\frac{1}{3}\\)", "\\(\\frac{1}{3}\\)", "\\(-\\frac{7}{9}\\)", "\\(\\frac{2}{3}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{-2}{3} \\times \\left(\\frac{5}{6} + \\frac{-2}{6}\\right) = \\frac{-2}{3} \\times \\frac{3}{6} = \\frac{-2}{3} \\times \\frac{1}{2} = -\\frac{1}{3}\\)."),

    # 12
    ("Which property of multiplication is shown by \\(\\frac{-4}{5} \\times 1 = 1 \\times \\frac{-4}{5} = -\\frac{4}{5}\\)?",
     ["Multiplicative identity property",
      "Multiplicative inverse property",
      "Commutative property only",
      "Closure property"],
     "A", "OSC", "easy",
     "Multiplying by 1 yields the original number identically, demonstrating 1 as the multiplicative identity."),

    # 13
    ("Which property is illustrated by \\(\\frac{-19}{29} \\times \\frac{29}{-19} = 1\\)?",
     ["Multiplicative inverse property",
      "Multiplicative identity property",
      "Associative property",
      "Distributive property"],
     "A", "OSC", "easy",
     "The product of a number and its reciprocal is 1, demonstrating the multiplicative inverse property."),

    # 14
    ("What is the product of \\(\\frac{6}{13}\\) and the reciprocal of \\(\\frac{-7}{16}\\)?",
     ["\\(-\\frac{96}{91}\\)", "\\(\\frac{96}{91}\\)", "\\(-\\frac{42}{208}\\)", "\\(\\frac{91}{96}\\)"],
     "A", "OSC", "medium",
     "The reciprocal of \\(\\frac{-7}{16}\\) is \\(-\\frac{16}{7}\\). Product: \\(\\frac{6}{13} \\times \\left(-\\frac{16}{7}\\right) = -\\frac{96}{91}\\)."),

    # 15
    ("Evaluate: \\(\\frac{-2}{3} \\times \\left[ \\frac{3}{5} + \\left(\\frac{-5}{6}\\right) \\right]\\)",
     ["\\(\\frac{7}{45}\\)", "\\(-\\frac{7}{45}\\)", "\\(\\frac{7}{15}\\)", "\\(-\\frac{1}{3}\\)"],
     "A", "OSC", "medium",
     "Inside: \\(\\frac{3}{5} - \\frac{5}{6} = \\frac{18 - 25}{30} = -\\frac{7}{30}\\). Multiplying: \\(\\frac{-2}{3} \\times \\left(-\\frac{7}{30}\\right) = \\frac{14}{90} = \\frac{7}{45}\\)."),

    # 16
    ("Is subtraction associative for rational numbers? Test with \\(\\left(1 - \\frac{1}{2}\\right) - \\frac{1}{3}\\) and \\(1 - \\left(\\frac{1}{2} - \\frac{1}{3}\\right)\\).",
     ["No, the first gives \\(\\frac{1}{6}\\) while the second gives \\(\\frac{5}{6}\\)",
      "Yes, both give \\(\\frac{1}{6}\\)",
      "Yes, both give \\(\\frac{5}{6}\\)",
      "No, because fractions cannot be grouped"],
     "A", "OSC", "medium",
     "\\(\\left(1 - \\frac{1}{2}\\right) - \\frac{1}{3} = \\frac{1}{2} - \\frac{1}{3} = \\frac{1}{6}\\). But \\(1 - \\left(\\frac{1}{2} - \\frac{1}{3}\\right) = 1 - \\frac{1}{6} = \\frac{5}{6}\\). Since \\(\\frac{1}{6} \\neq \\frac{5}{6}\\), subtraction is not associative."),

    # 17
    ("Is division associative for rational numbers? Test with \\((16 \\div 4) \\div 2\\) and \\(16 \\div (4 \\div 2)\\).",
     ["No, the first gives 2 while the second gives 8",
      "Yes, both equal 2",
      "Yes, both equal 8",
      "No, division is never allowed in groups"],
     "A", "OSC", "easy",
     "\\((16 \\div 4) \\div 2 = 4 \\div 2 = 2\\), whereas \\(16 \\div (4 \\div 2) = 16 \\div 2 = 8\\). Since \\(2 \\neq 8\\), division is not associative."),

    # 18
    ("What is the additive inverse of \\(\\frac{-6}{-11}\\)?",
     ["\\(-\\frac{6}{11}\\)", "\\(\\frac{6}{11}\\)", "\\(\\frac{11}{6}\\)", "\\(-\\frac{11}{6}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{-6}{-11} = \\frac{6}{11}\\) (positive). The additive inverse of a positive number is negative: \\(-\\frac{6}{11}\\)."),

    # 19
    ("What is the multiplicative inverse of \\(-1\\)?",
     ["-1", "1", "0", "Undefined"],
     "A", "OSC", "easy",
     "The reciprocal of -1 is \\(\\frac{1}{-1} = -1\\)."),

    # 20
    ("What is the multiplicative inverse of \\(-1 \\times \\left(-\\frac{2}{5}\\right)\\)?",
     ["\\(\\frac{5}{2}\\)", "\\(-\\frac{5}{2}\\)", "\\(\\frac{2}{5}\\)", "\\(-\\frac{2}{5}\\)"],
     "A", "OSC", "easy",
     "First simplify: \\(-1 \\times \\left(-\\frac{2}{5}\\right) = \\frac{2}{5}\\). The multiplicative inverse of \\(\\frac{2}{5}\\) is \\(\\frac{5}{2}\\)."),

    # 21
    ("What is the value of \\(x\\) if \\(\\frac{-5}{8} \\times x = 1\\)?",
     ["\\(-\\frac{8}{5}\\)", "\\(\\frac{8}{5}\\)", "\\(-\\frac{5}{8}\\)", "1"],
     "A", "OSC", "easy",
     "\\(x\\) is the multiplicative inverse of \\(\\frac{-5}{8}\\), which is \\(-\\frac{8}{5}\\)."),

    # 22
    ("What is the value of \\(y\\) if \\(\\frac{4}{15} + y = 0\\)?",
     ["\\(-\\frac{4}{15}\\)", "\\(\\frac{15}{4}\\)", "\\(-\\frac{15}{4}\\)", "0"],
     "A", "OSC", "easy",
     "\\(y\\) is the additive inverse of \\(\\frac{4}{15}\\), which is \\(-\\frac{4}{15}\\)."),

    # 23
    ("Simplify using properties: \\(\\frac{2}{5} \\times \\left(-\\frac{3}{7}\\right) - \\frac{1}{14} - \\frac{3}{7} \\times \\frac{3}{5}\\)",
     ["\\(-\\frac{1}{2}\\)", "\\(\\frac{1}{2}\\)", "\\(-\\frac{3}{7}\\)", "\\(0\\)"],
     "A", "OSC", "hard",
     "Rearrange: \\(\\left[\\frac{2}{5} \\times \\left(-\\frac{3}{7}\\right) - \\frac{3}{7} \\times \\frac{3}{5}\\right] - \\frac{1}{14} = \\left(-\\frac{3}{7}\\right) \\times \\left(\\frac{2}{5} + \\frac{3}{5}\\right) - \\frac{1}{14} = \\left(-\\frac{3}{7}\\right) \\times 1 - \\frac{1}{14} = -\\frac{6}{14} - \\frac{1}{14} = -\\frac{7}{14} = -\\frac{1}{2}\\)."),

    # 24
    ("Simplify: \\(\\frac{-4}{5} \\times \\left( \\frac{3}{8} + \\frac{5}{12} \\right)\\) using distributive property.",
     ["\\(-\\frac{19}{30}\\)", "\\(\\frac{19}{30}\\)", "\\(-\\frac{19}{60}\\)", "\\(-\\frac{7}{15}\\)"],
     "A", "OSC", "medium",
     "Inside: \\(\\frac{9 + 10}{24} = \\frac{19}{24}\\). Multiplying: \\(\\frac{-4}{5} \\times \\frac{19}{24} = \\frac{-1 \\times 19}{5 \\times 6} = -\\frac{19}{30}\\)."),

    # 25
    ("Distributive property over subtraction states that \\(a \\times (b - c) = \\) _____.",
     ["\\(a \\times b - a \\times c\\)",
      "\\(a \\times b + a \\times c\\)",
      "\\(a \\times (c - b)\\)",
      "\\(b - a \\times c\\)"],
     "A", "OSC", "easy",
     "\\(a \\times (b - c) = ab - ac\\)."),

    # 26
    ("Evaluate: \\(\\frac{9}{16} \\times \\frac{4}{12} + \\frac{9}{16} \\times \\frac{-3}{9}\\)",
     ["0", "\\(\\frac{9}{16}\\)", "1", "\\(-\\frac{9}{16}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{4}{12} = \\frac{1}{3}\\) and \\(\\frac{-3}{9} = -\\frac{1}{3}\\). Sum = \\(\\frac{1}{3} - \\frac{1}{3} = 0\\). Then \\(\\frac{9}{16} \\times 0 = 0\\)."),

    # 27
    ("Which of the following illustrates the distributive property of multiplication over addition?",
     ["\\(\\frac{1}{2} \\times \\left(\\frac{2}{3} + \\frac{3}{4}\\right) = \\left(\\frac{1}{2} \\times \\frac{2}{3}\\right) + \\left(\\frac{1}{2} \\times \\frac{3}{4}\\right)\\)",
      "\\(\\frac{1}{2} + \\frac{2}{3} = \\frac{2}{3} + \\frac{1}{2}\\)",
      "\\(\\left(\\frac{1}{2} + \\frac{2}{3}\\right) + \\frac{3}{4} = \\frac{1}{2} + \\left(\\frac{2}{3} + \\frac{3}{4}\\right)\\)",
      "\\(\\frac{1}{2} \\times 1 = \\frac{1}{2}\\)"],
     "A", "OSC", "easy",
     "Option A distributes \\(\\frac{1}{2}\\) across each term in the sum."),

    # 28
    ("What is the reciprocal of \\(\\left(\\frac{-3}{8}\\right) \\times \\left(\\frac{-7}{13}\\right)\\)?",
     ["\\(\\frac{104}{21}\\)", "\\(-\\frac{104}{21}\\)", "\\(\\frac{21}{104}\\)", "\\(-\\frac{21}{104}\\)"],
     "A", "OSC", "medium",
     "Product = \\(\\frac{(-3) \\times (-7)}{8 \\times 13} = \\frac{21}{104}\\). Reciprocal is \\(\\frac{104}{21}\\)."),

    # 29
    ("Evaluate: \\(0 \\times \\frac{-15}{28}\\)",
     ["0", "1", "\\(-\\frac{15}{28}\\)", "Undefined"],
     "A", "OSC", "easy",
     "Any rational number multiplied by zero equals zero."),

    # 30
    ("If \\(a = \\frac{1}{2}\\), \\(b = \\frac{2}{3}\\), and \\(c = \\frac{3}{4}\\), verify \\(a \\times (b \\times c) = (a \\times b) \\times c\\). What is the value?",
     ["\\(\\frac{1}{4}\\)", "\\(\\frac{1}{2}\\)", "\\(\\frac{3}{8}\\)", "\\(\\frac{6}{24}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{1}{2} \\times \\left(\\frac{2}{3} \\times \\frac{3}{4}\\right) = \\frac{1}{2} \\times \\frac{1}{2} = \\frac{1}{4}\\)."),

    # 31
    ("Find \\(x\\) if \\(\\frac{-13}{17} + x = \\frac{-13}{17}\\).",
     ["0", "1", "-1", "\\(\\frac{26}{17}\\)"],
     "A", "OSC", "easy",
     "Adding \\(x\\) leaves the number unchanged, so \\(x = 0\\) (the additive identity)."),

    # 32
    ("Find \\(y\\) if \\(\\frac{11}{23} \\times y = \\frac{11}{23}\\).",
     ["1", "0", "-1", "\\(\\frac{23}{11}\\)"],
     "A", "OSC", "easy",
     "Multiplying by \\(y\\) preserves the number, so \\(y = 1\\) (the multiplicative identity)."),

    # 33
    ("Simplify: \\(\\left(\\frac{2}{7} \\times \\frac{-5}{8}\\right) - \\left(\\frac{2}{7} \\times \\frac{3}{8}\\right)\\)",
     ["\\(-\\frac{2}{7}\\)", "\\(\\frac{2}{7}\\)", "\\(-\\frac{1}{7}\\)", "\\(0\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{2}{7} \\times \\left(-\\frac{5}{8} - \\frac{3}{8}\\right) = \\frac{2}{7} \\times \\left(-\\frac{8}{8}\\right) = \\frac{2}{7} \\times (-1) = -\\frac{2}{7}\\)."),

    # 34
    ("Assertion (A): The negative of a negative rational number is positive.\nReason (R): For any rational number \\(x\\), \\(-(-x) = x\\).",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "Negating a quantity twice returns the original quantity: \\(-(-x) = x\\), which confirms that the negative of a negative number is positive."),

    # 35
    ("Assertion (A): \\(\\frac{2}{3} \\div \\left(\\frac{3}{4} \\div \\frac{2}{5}\\right) = \\left(\\frac{2}{3} \\div \\frac{3}{4}\\right) \\div \\frac{2}{5}\\).\nReason (R): Division of rational numbers is associative.",
     ["Both (A) and (R) are false",
      "Both (A) and (R) are true",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "Both are false: division of rational numbers is definitely not associative, and the two expressions evaluate to different values."),

    # 36
    ("True or False: Multiplication is distributive over addition for all rational numbers.",
     ["True", "False"],
     "A", "OTF", "easy",
     "\\(a(b + c) = ab + ac\\) holds unconditionally across all rational numbers."),

    # 37
    ("True or False: Zero is the only rational number that does not have a multiplicative inverse.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Every non-zero rational number \\(\\frac{p}{q}\\) has reciprocal \\(\\frac{q}{p}\\). Zero has no reciprocal because division by zero is undefined."),

    # 38
    ("Fill in the blank: The sum of a rational number and its additive inverse is always _____.",
     ["0", "1", "-1", "undefined"],
     "A", "OFB", "easy",
     "By definition of additive inverse, \\(a + (-a) = 0\\)."),

    # 39
    ("Fill in the blank: The product of a non-zero rational number and its reciprocal is always _____.",
     ["1", "0", "-1", "\\(a^2\\)"],
     "A", "OFB", "easy",
     "By definition of multiplicative inverse, \\(a \\times \\frac{1}{a} = 1\\)."),

    # 40
    ("What is the numerical integer value of \\(\\left(\\frac{-3}{4} + \\frac{3}{4}\\right) \\times 100\\)?",
     ["0", "100", "-100", "75"],
     "A", "ONE", "easy",
     "\\(\\left(-\\frac{3}{4} + \\frac{3}{4}\\right) = 0\\), and \\(0 \\times 100 = 0\\)."),
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    ("Find the additive inverse of \\(\\frac{2}{8}\\).",
     ["\\(-\\frac{2}{8}\\)", "\\(\\frac{8}{2}\\)", "\\(-\\frac{8}{2}\\)", "0"],
     "A", "OSC", "easy",
     "Additive inverse is \\(-\\frac{2}{8} = -\\frac{1}{4}\\)."),

    # 42
    ("Find the additive inverse of \\(\\frac{-5}{9}\\).",
     ["\\(\\frac{5}{9}\\)", "\\(-\\frac{5}{9}\\)", "\\(\\frac{9}{5}\\)", "\\(-\\frac{9}{5}\\)"],
     "A", "OSC", "easy",
     "Additive inverse of \\(-\\frac{5}{9}\\) is \\(\\frac{5}{9}\\)."),

    # 43
    ("Find the additive inverse of \\(\\frac{19}{-6}\\).",
     ["\\(\\frac{19}{6}\\)", "\\(-\\frac{19}{6}\\)", "\\(\\frac{6}{19}\\)", "\\(-\\frac{6}{19}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{19}{-6} = -\\frac{19}{6}\\). Its additive inverse is \\(\\frac{19}{6}\\)."),

    # 44
    ("Find the multiplicative inverse of \\(-13\\).",
     ["\\(-\\frac{1}{13}\\)", "\\(\\frac{1}{13}\\)", "13", "-1"],
     "A", "OSC", "easy",
     "Reciprocal of \\(-13\\) is \\(-\\frac{1}{13}\\)."),

    # 45
    ("Find the multiplicative inverse of \\(\\frac{1}{5}\\).",
     ["5", "-5", "\\(\\frac{1}{5}\\)", "1"],
     "A", "OSC", "easy",
     "Reciprocal of \\(\\frac{1}{5}\\) is 5."),

    # 46
    ("Find the multiplicative inverse of \\(\\frac{-5}{8} \\times \\frac{-3}{7}\\).",
     ["\\(\\frac{56}{15}\\)", "\\(-\\frac{56}{15}\\)", "\\(\\frac{15}{56}\\)", "\\(-\\frac{15}{56}\\)"],
     "A", "OSC", "easy",
     "Product = \\(\\frac{15}{56}\\). Reciprocal is \\(\\frac{56}{15}\\)."),

    # 47
    ("Evaluate using distributivity: \\(\\left(\\frac{7}{5} \\times \\frac{-3}{12}\\right) + \\left(\\frac{7}{5} \\times \\frac{5}{12}\\right)\\)",
     ["\\(\\frac{7}{30}\\)", "\\(-\\frac{7}{30}\\)", "\\(\\frac{14}{60}\\)", "\\(\\frac{7}{12}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{7}{5} \\times \\left(\\frac{-3 + 5}{12}\\right) = \\frac{7}{5} \\times \\frac{2}{12} = \\frac{7}{30}\\)."),

    # 48
    ("Evaluate: \\(\\left(\\frac{9}{16} \\times \\frac{4}{12}\\right) + \\left(\\frac{9}{16} \\times \\frac{-3}{9}\\right)\\)",
     ["0", "\\(\\frac{9}{16}\\)", "1", "\\(-\\frac{9}{16}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{4}{12} - \\frac{3}{9} = \\frac{1}{3} - \\frac{1}{3} = 0\\). \\(\\frac{9}{16} \\times 0 = 0\\)."),

    # 49
    ("Multiply \\(\\frac{6}{13}\\) by the reciprocal of \\(\\frac{-7}{16}\\).",
     ["\\(-\\frac{96}{91}\\)", "\\(\\frac{96}{91}\\)", "\\(-\\frac{42}{208}\\)", "\\(\\frac{91}{96}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{6}{13} \\times \\left(-\\frac{16}{7}\\right) = -\\frac{96}{91}\\)."),

    # 50
    ("Simplify: \\(\\left(\\frac{-1}{4} + \\frac{5}{8}\\right) + \\frac{-3}{2}\\)",
     ["\\(-\\frac{9}{8}\\)", "\\(\\frac{9}{8}\\)", "\\(-\\frac{7}{8}\\)", "\\(\\frac{7}{8}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{-2 + 5}{8} = \\frac{3}{8}\\). Then \\(\\frac{3}{8} - \\frac{12}{8} = -\\frac{9}{8}\\)."),

    # 51
    ("Simplify: \\(\\frac{-1}{4} + \\left(\\frac{5}{8} + \\frac{-3}{2}\\right)\\)",
     ["\\(-\\frac{9}{8}\\)", "\\(\\frac{9}{8}\\)", "\\(-\\frac{7}{8}\\)", "\\(\\frac{7}{8}\\)"],
     "A", "OSC", "medium",
     "Inside: \\(\\frac{5 - 12}{8} = -\\frac{7}{8}\\). Then \\(-\\frac{2}{8} - \\frac{7}{8} = -\\frac{9}{8}\\) (confirming associativity of addition)."),

    # 52
    ("Evaluate: \\(\\frac{2}{5} \\times \\left( \\frac{-1}{9} - \\frac{5}{9} \\right)\\)",
     ["\\(-\\frac{4}{15}\\)", "\\(\\frac{4}{15}\\)", "\\(-\\frac{2}{15}\\)", "\\(-\\frac{1}{3}\\)"],
     "A", "OSC", "medium",
     "Inside: \\(\\frac{-1 - 5}{9} = -\\frac{6}{9} = -\\frac{2}{3}\\). Multiplying: \\(\\frac{2}{5} \\times \\left(-\\frac{2}{3}\\right) = -\\frac{4}{15}\\)."),

    # 53
    ("Evaluate: \\(\\left(\\frac{-3}{4} \\times \\frac{2}{3}\\right) + \\left(\\frac{-3}{4} \\times \\frac{-5}{6}\\right)\\)",
     ["\\(\\frac{1}{8}\\)", "\\(-\\frac{1}{8}\\)", "\\(\\frac{1}{4}\\)", "\\(-\\frac{1}{4}\\)"],
     "A", "OSC", "medium",
     "Factor out \\(-\\frac{3}{4}\\): \\(-\\frac{3}{4} \\times \\left(\\frac{2}{3} - \\frac{5}{6}\\right) = -\\frac{3}{4} \\times \\left(\\frac{4 - 5}{6}\\right) = -\\frac{3}{4} \\times \\left(-\\frac{1}{6}\\right) = \\frac{3}{24} = \\frac{1}{8}\\)."),

    # 54
    ("Evaluate: \\(\\left(\\frac{4}{7} \\times \\frac{5}{8}\\right) - \\left(\\frac{4}{7} \\times \\frac{1}{8}\\right)\\)",
     ["\\(\\frac{2}{7}\\)", "\\(-\\frac{2}{7}\\)", "\\(\\frac{1}{7}\\)", "\\(\\frac{4}{7}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{4}{7} \\times \\left(\\frac{5}{8} - \\frac{1}{8}\\right) = \\frac{4}{7} \\times \\frac{4}{8} = \\frac{4}{7} \\times \\frac{1}{2} = \\frac{2}{7}\\)."),

    # 55
    ("What is the additive inverse of \\(0\\)?",
     ["0", "1", "-1", "Does not exist"],
     "A", "OSC", "easy",
     "\\(-0 = 0\\), so zero is its own additive inverse."),

    # 56
    ("What is the product of \\(\\frac{-2}{3}\\) and its additive inverse?",
     ["\\(-\\frac{4}{9}\\)", "\\(\\frac{4}{9}\\)", "0", "1"],
     "A", "OSC", "easy",
     "Additive inverse is \\(\\frac{2}{3}\\). Product: \\(\\left(-\\frac{2}{3}\\right) \\times \\frac{2}{3} = -\\frac{4}{9}\\)."),

    # 57
    ("What is the quotient when \\(\\frac{-4}{7}\\) is divided by its additive inverse?",
     ["-1", "1", "0", "\\(-\\frac{16}{49}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{-4/7}{4/7} = -1\\)."),

    # 58
    ("What is the quotient when \\(\\frac{-4}{7}\\) is divided by its reciprocal?",
     ["\\(\\frac{16}{49}\\)", "\\(-\\frac{16}{49}\\)", "1", "-1"],
     "A", "OSC", "easy",
     "\\(\\frac{-4}{7} \\div \\frac{-7}{4} = \\frac{-4}{7} \\times \\frac{-4}{7} = \\frac{16}{49}\\)."),

    # 59
    ("Verify if \\(a \\times (b + c) = ab + ac\\) for \\(a = -2\\), \\(b = \\frac{1}{3}\\), \\(c = \\frac{1}{4}\\). What is the value?",
     ["\\(-\\frac{7}{6}\\)", "\\(\\frac{7}{6}\\)", "\\(-\\frac{5}{6}\\)", "\\(\\frac{5}{6}\\)"],
     "A", "OSC", "medium",
     "\\(b + c = \\frac{4 + 3}{12} = \\frac{7}{12}\\). Multiplying by \\(-2\\): \\(-2 \\times \\frac{7}{12} = -\\frac{7}{6}\\)."),

    # 60
    ("Simplify: \\(\\left(\\frac{-3}{2} \\times \\frac{4}{5}\\right) \\times \\frac{-5}{6}\\)",
     ["1", "-1", "2", "-2"],
     "A", "OSC", "easy",
     "\\(\\frac{-3 \\times 4 \\times (-5)}{2 \\times 5 \\times 6} = \\frac{60}{60} = 1\\)."),

    # 61
    ("Find the value of \\(x\\) if \\(x + \\left(-\\frac{5}{13}\\right) = 0\\).",
     ["\\(\\frac{5}{13}\\)", "\\(-\\frac{5}{13}\\)", "\\(\\frac{13}{5}\\)", "\\(-\\frac{13}{5}\\)"],
     "A", "OSC", "easy",
     "\\(x = \\frac{5}{13}\\)."),

    # 62
    ("Find the value of \\(k\\) if \\(k \\times \\left(-\\frac{8}{17}\\right) = 1\\).",
     ["\\(-\\frac{17}{8}\\)", "\\(\\frac{17}{8}\\)", "\\(-\\frac{8}{17}\\)", "1"],
     "A", "OSC", "easy",
     "\\(k = -\\frac{17}{8}\\)."),

    # 63
    ("Evaluate: \\(\\left(\\frac{1}{2} + \\frac{1}{3}\\right) \\times 6\\)",
     ["5", "6", "1", "3"],
     "A", "OSC", "easy",
     "Using distributivity: \\(\\left(\\frac{1}{2} \\times 6\\right) + \\left(\\frac{1}{3} \\times 6\\right) = 3 + 2 = 5\\)."),

    # 64
    ("Evaluate: \\(\\left(\\frac{3}{4} - \\frac{1}{2}\\right) \\times 8\\)",
     ["2", "4", "1", "6"],
     "A", "OSC", "easy",
     "Distribute: \\(\\left(\\frac{3}{4} \\times 8\\right) - \\left(\\frac{1}{2} \\times 8\\right) = 6 - 4 = 2\\)."),

    # 65
    ("Evaluate: \\(\\frac{3}{5} \\times \\left( \\frac{1}{2} + \\frac{1}{4} \\right)\\)",
     ["\\(\\frac{9}{20}\\)", "\\(\\frac{3}{20}\\)", "\\(\\frac{3}{10}\\)", "\\(\\frac{7}{20}\\)"],
     "A", "OSC", "easy",
     "Inside: \\(\\frac{2 + 1}{4} = \\frac{3}{4}\\). Multiplying: \\(\\frac{3}{5} \\times \\frac{3}{4} = \\frac{9}{20}\\)."),

    # 66
    ("True or False: The reciprocal of a positive rational number is always positive.",
     ["True", "False"],
     "A", "OTF", "easy",
     "If \\(x > 0\\), then \\(\\frac{1}{x} > 0\\)."),

    # 67
    ("True or False: The reciprocal of a negative rational number is always negative.",
     ["True", "False"],
     "A", "OTF", "easy",
     "If \\(x < 0\\), then \\(\\frac{1}{x} < 0\\)."),

    # 68
    ("Fill in the blank: The property used in \\(\\frac{2}{3} \\times \\left(\\frac{4}{5} \\times \\frac{6}{7}\\right) = \\left(\\frac{2}{3} \\times \\frac{4}{5}\\right) \\times \\frac{6}{7}\\) is _____.",
     ["associative property of multiplication", "commutative property", "distributive property", "closure property"],
     "A", "OFB", "easy",
     "Regrouping factors without changing order is the associative property of multiplication."),

    # 69
    ("Fill in the blank: The additive inverse of \\(-\\frac{a}{b}\\) is _____.",
     ["\\(\\frac{a}{b}\\)", "\\(-\\frac{b}{a}\\)", "\\(\\frac{b}{a}\\)", "0"],
     "A", "OFB", "easy",
     "The opposite of \\(-\\frac{a}{b}\\) is \\(\\frac{a}{b}\\)."),

    # 70
    ("What is the numerical integer value of \\(\\left(\\frac{-5}{7} \\times \\frac{7}{5}\\right) + 1\\)?",
     ["0", "1", "2", "-1"],
     "A", "ONE", "easy",
     "\\(\\frac{-5}{7} \\times \\frac{7}{5} = -1\\). Then \\(-1 + 1 = 0\\)."),
]

# 12 MOCK / FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Associative Regrouping of Addition</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Group 1: (a + b) + c -->
    <rect x="20" y="25" width="140" height="55" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="90" y="47" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">[ (-2/3) + 3/5 ] + (-5/6)</text>
    <text x="90" y="67" fill="#cbd5e1" font-size="11" text-anchor="middle">= -1/15 - 5/6 = -9/10</text>
    <!-- Equal operator -->
    <text x="170" y="60" fill="#10b981" font-size="22" font-weight="bold" text-anchor="middle">=</text>
    <!-- Group 2: a + (b + c) -->
    <rect x="180" y="25" width="140" height="55" rx="6" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
    <text x="250" y="47" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">(-2/3) + [ 3/5 + (-5/6) ]</text>
    <text x="250" y="67" fill="#cbd5e1" font-size="11" text-anchor="middle">= -2/3 - 7/30 = -9/10</text>
    <!-- Bottom rule card -->
    <rect x="35" y="95" width="270" height="40" rx="5" fill="#0f172a" stroke="#475569"/>
    <text x="170" y="112" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">(a + b) + c = a + (b + c)</text>
    <text x="170" y="128" fill="#e2e8f0" font-size="10" text-anchor="middle">Regrouping brackets does not change the total sum</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Which fundamental property of rational numbers is depicted in the diagram?</p>
</div>""",
     ["Associative property of addition", "Commutative property of addition", "Distributive property", "Closure property"],
     "A", "OSC", "easy",
     "The diagram shows that regrouping brackets across three terms produces the exact same sum, which is the associative property of addition."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Distributive Law via Geometric Rectangle Area</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Unified Rectangle split into two sections -->
    <!-- Section 1: width b -->
    <rect x="40" y="35" width="100" height="60" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2"/>
    <text x="90" y="68" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">Area = a × b</text>
    <text x="90" y="25" fill="#e2e8f0" font-size="11" text-anchor="middle">width b</text>
    <!-- Section 2: width c -->
    <rect x="140" y="35" width="120" height="60" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="200" y="68" fill="#6ee7b7" font-size="13" font-weight="bold" text-anchor="middle">Area = a × c</text>
    <text x="200" y="25" fill="#e2e8f0" font-size="11" text-anchor="middle">width c</text>
    <!-- Height a on left -->
    <text x="25" y="70" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">h = a</text>
    <!-- Bottom total area formula -->
    <text x="170" y="125" fill="#fde047" font-size="13" font-weight="bold" text-anchor="middle">Total Area = a × (b + c) = (a × b) + (a × c)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">The area of the partitioned rectangle demonstrates which mathematical identity?</p>
</div>""",
     ["Distributive property of multiplication over addition", "Associative property", "Commutative property", "Closure property"],
     "A", "OSC", "easy",
     "The overall rectangle of height \\(a\\) and combined width \\(b+c\\) splits into two sub-rectangles of area \\(ab\\) and \\(ac\\), geometrically proving \\(a(b+c) = ab + ac\\)."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Additive Identity Neutral Operator (0)</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Input box -->
    <rect x="30" y="40" width="80" height="50" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="70" y="70" fill="#93c5fd" font-size="15" font-weight="bold" text-anchor="middle">-4 / 9</text>
    <!-- Plus Zero circle -->
    <circle cx="160" cy="65" r="18" fill="#0f172a" stroke="#10b981" stroke-width="2.5"/>
    <text x="160" y="71" fill="#34d399" font-size="15" font-weight="bold" text-anchor="middle">+ 0</text>
    <!-- Arrow -->
    <path d="M 190,65 L 225,65" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="225,60 235,65 225,70" fill="#f59e0b"/>
    <!-- Unchanged output -->
    <rect x="245" y="40" width="80" height="50" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="285" y="70" fill="#6ee7b7" font-size="15" font-weight="bold" text-anchor="middle">-4 / 9</text>
    <text x="170" y="125" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">a + 0 = 0 + a = a  (Zero leaves value invariant)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the result when the additive identity is added to \(-\frac{4}{9}\)?</p>
</div>""",
     ["\\(-\\frac{4}{9}\\)", "0", "1", "\\(\\frac{4}{9}\\)"],
     "A", "OSC", "easy",
     "Zero is the additive identity, so adding zero leaves \\(-\\frac{4}{9}\\) completely unchanged."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Multiplicative Identity Mirror Operator (1)</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Input box -->
    <rect x="30" y="40" width="80" height="50" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="70" y="70" fill="#93c5fd" font-size="15" font-weight="bold" text-anchor="middle">-7 / 13</text>
    <!-- Multiply by 1 circle -->
    <circle cx="160" cy="65" r="18" fill="#0f172a" stroke="#fbbf24" stroke-width="2.5"/>
    <text x="160" y="71" fill="#fde047" font-size="15" font-weight="bold" text-anchor="middle">× 1</text>
    <!-- Arrow -->
    <path d="M 190,65 L 225,65" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="225,60 235,65 225,70" fill="#f59e0b"/>
    <!-- Unchanged output -->
    <rect x="245" y="40" width="80" height="50" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="285" y="70" fill="#6ee7b7" font-size="15" font-weight="bold" text-anchor="middle">-7 / 13</text>
    <text x="170" y="125" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">a × 1 = 1 × a = a  (1 is Multiplicative Identity)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the product of \(-\frac{7}{13}\) and the multiplicative identity?</p>
</div>""",
     ["\\(-\\frac{7}{13}\\)", "1", "0", "\\(\\frac{7}{13}\\)"],
     "A", "OSC", "easy",
     "Multiplying by 1 yields the exact same rational number \\(-\\frac{7}{13}\\)."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Factoring Out Common Terms using Distributivity</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Expression -->
    <text x="170" y="25" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">Evaluate: (7/5 × -3/12) + (7/5 × 5/12)</text>
    <!-- Step 1: Factoring -->
    <rect x="35" y="40" width="270" height="35" rx="5" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="170" y="62" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">Factor out 7/5:  7/5 × [ (-3/12) + 5/12 ]</text>
    <!-- Step 2: Sum inside brackets -->
    <rect x="50" y="85" width="240" height="30" rx="5" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
    <text x="170" y="105" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">= 7/5 × (2/12) = 7/5 × 1/6 = 7/30</text>
    <text x="170" y="138" fill="#fbbf24" font-size="11" text-anchor="middle">Avoids bulky common denominators by grouping shared factors</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Using the distributive property shown, evaluate \(\left(\frac{7}{5} \times \frac{-3}{12}\right) + \left(\frac{7}{5} \times \frac{5}{12}\right)\).</p>
</div>""",
     ["\\(\\frac{7}{30}\\)", "\\(-\\frac{7}{30}\\)", "\\(\\frac{14}{60}\\)", "\\(\\frac{1}{6}\\)"],
     "A", "OSC", "easy",
     "Factoring out \\(\\frac{7}{5}\\) gives \\(\\frac{7}{5} \\times \\frac{2}{12} = \\frac{7}{30}\\)."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Failure of Associativity in Subtraction</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Left Branch: (1 - 1/2) - 1/3 -->
    <rect x="25" y="25" width="135" height="95" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="92" y="48" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">[ 1 - 1/2 ] - 1/3</text>
    <text x="92" y="72" fill="#ffffff" font-size="12" text-anchor="middle">= 1/2 - 1/3</text>
    <text x="92" y="95" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">= +1 / 6</text>
    <!-- Not equal -->
    <text x="170" y="70" fill="#ef4444" font-size="22" font-weight="bold" text-anchor="middle">≠</text>
    <!-- Right Branch: 1 - (1/2 - 1/3) -->
    <rect x="180" y="25" width="135" height="95" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <text x="247" y="48" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">1 - [ 1/2 - 1/3 ]</text>
    <text x="247" y="72" fill="#ffffff" font-size="12" text-anchor="middle">= 1 - 1/6</text>
    <text x="247" y="95" fill="#f87171" font-size="14" font-weight="bold" text-anchor="middle">= +5 / 6</text>
    <!-- Footnote -->
    <text x="170" y="138" fill="#fde047" font-size="11" text-anchor="middle">(a - b) - c DOES NOT EQUAL a - (b - c)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What does this comparison prove regarding subtraction of rational numbers?</p>
</div>""",
     ["Subtraction of rational numbers is not associative",
      "Subtraction of rational numbers is associative",
      "Subtraction is commutative",
      "Subtraction is closed"],
     "A", "OSC", "easy",
     "Because \\(\\left(1 - \\frac{1}{2}\\right) - \\frac{1}{3} = \\frac{1}{6}\\) while \\(1 - \\left(\\frac{1}{2} - \\frac{1}{3}\\right) = \\frac{5}{6}\\), subtraction is not associative."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Failure of Associativity in Division</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Left Branch: (16 / 4) / 2 -->
    <rect x="25" y="25" width="135" height="95" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="92" y="48" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">[ 16 ÷ 4 ] ÷ 2</text>
    <text x="92" y="72" fill="#ffffff" font-size="12" text-anchor="middle">= 4 ÷ 2</text>
    <text x="92" y="95" fill="#34d399" font-size="15" font-weight="bold" text-anchor="middle">= 2</text>
    <!-- Not equal -->
    <text x="170" y="70" fill="#ef4444" font-size="22" font-weight="bold" text-anchor="middle">≠</text>
    <!-- Right Branch: 16 / (4 / 2) -->
    <rect x="180" y="25" width="135" height="95" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <text x="247" y="48" fill="#fca5a5" font-size="12" font-weight="bold" text-anchor="middle">16 ÷ [ 4 ÷ 2 ]</text>
    <text x="247" y="72" fill="#ffffff" font-size="12" text-anchor="middle">= 16 ÷ 2</text>
    <text x="247" y="95" fill="#f87171" font-size="15" font-weight="bold" text-anchor="middle">= 8</text>
    <!-- Footnote -->
    <text x="170" y="138" fill="#fbbf24" font-size="11" text-anchor="middle">(a ÷ b) ÷ c DOES NOT EQUAL a ÷ (b ÷ c)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is demonstrated by \((16 \div 4) \div 2 \neq 16 \div (4 \div 2)\)?</p>
</div>""",
     ["Division of rational numbers is not associative",
      "Division is commutative",
      "Division is closed",
      "Division is associative"],
     "A", "OSC", "easy",
     "Different groupings yield 2 and 8, proving division is not associative."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Reciprocal of a Product: (ab)⁻¹ = a⁻¹ × b⁻¹</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Original product -->
    <rect x="30" y="30" width="115" height="60" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="87" y="55" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">Product: (-3/8) × (-7/5)</text>
    <text x="87" y="75" fill="#ffffff" font-size="12" text-anchor="middle">= +21 / 40</text>
    <!-- Arrow -->
    <path d="M 155,60 L 190,60" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="190,55 200,60 190,65" fill="#f59e0b"/>
    <text x="175" y="45" fill="#fbbf24" font-size="10" text-anchor="middle">Invert</text>
    <!-- Reciprocal product -->
    <rect x="210" y="30" width="105" height="60" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="262" y="55" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">Reciprocal</text>
    <text x="262" y="78" fill="#fde047" font-size="15" font-weight="bold" text-anchor="middle">= 40 / 21</text>
    <!-- Footnote -->
    <text x="170" y="125" fill="#38bdf8" font-size="11" text-anchor="middle">The reciprocal of a product is the product of their reciprocals</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the reciprocal of the product \(\left(-\frac{3}{8}\right) \times \left(-\frac{7}{5}\right)\)?</p>
</div>""",
     ["\\(\\frac{40}{21}\\)", "\\(-\\frac{40}{21}\\)", "\\(\\frac{21}{40}\\)", "\\(-\\frac{21}{40}\\)"],
     "A", "OSC", "easy",
     "Product = \\(\\frac{21}{40}\\). Reciprocal is \\(\\frac{40}{21}\\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Double Negation Identity: -(-x) = x</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Start: x -->
    <rect x="25" y="40" width="70" height="45" rx="5" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
    <text x="60" y="68" fill="#6ee7b7" font-size="13" font-weight="bold" text-anchor="middle">x = 11/15</text>
    <!-- Arrow 1: Negate -->
    <text x="110" y="65" fill="#f59e0b" font-size="14" text-anchor="middle">-( ) →</text>
    <!-- Intermediate: -x -->
    <rect x="135" y="40" width="80" height="45" rx="5" fill="#7f1d1d" stroke="#ef4444" stroke-width="1.5"/>
    <text x="175" y="68" fill="#fca5a5" font-size="13" font-weight="bold" text-anchor="middle">-x = -11/15</text>
    <!-- Arrow 2: Negate again -->
    <text x="235" y="65" fill="#f59e0b" font-size="14" text-anchor="middle">-( ) →</text>
    <!-- Final: -(-x) -->
    <rect x="255" y="40" width="70" height="45" rx="5" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="290" y="68" fill="#6ee7b7" font-size="13" font-weight="bold" text-anchor="middle">+11/15</text>
    <!-- Banner -->
    <text x="170" y="125" fill="#fde047" font-size="13" font-weight="bold" text-anchor="middle">-(-x) = x holds for every rational number</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the value of \(-\left(-\frac{11}{15}\right)\)?</p>
</div>""",
     ["\\(\\frac{11}{15}\\)", "\\(-\\frac{11}{15}\\)", "\\(\\frac{15}{11}\\)", "0"],
     "A", "OSC", "easy",
     "\\(-\\left(-\\frac{11}{15}\\right) = +\\frac{11}{15}\\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Strategic Rearrangement using Common Denominators</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Pair 1: 3/7 and -8/21 (multiples of 7) -->
    <rect x="25" y="30" width="135" height="50" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="92" y="52" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">Pair 1: 3/7 + (-8/21)</text>
    <text x="92" y="70" fill="#ffffff" font-size="11" text-anchor="middle">= 9/21 - 8/21 = 1/21</text>
    <!-- Pair 2: -6/11 and 5/22 (multiples of 11) -->
    <rect x="180" y="30" width="135" height="50" rx="6" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="247" y="52" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Pair 2: -6/11 + 5/22</text>
    <text x="247" y="70" fill="#ffffff" font-size="11" text-anchor="middle">= -12/22 + 5/22 = -7/22</text>
    <!-- Combined sum -->
    <text x="170" y="115" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Sum = 1/21 + (-7/22) = (22 - 147) / 462 = -125 / 462</text>
    <text x="170" y="135" fill="#e2e8f0" font-size="10" text-anchor="middle">Group terms with shared factors to simplify mental arithmetic</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the final sum when grouping pairs by common denominator factors?</p>
</div>""",
     ["\\(-\\frac{125}{462}\\)", "\\(\\frac{125}{462}\\)", "\\(-\\frac{1}{462}\\)", "\\(0\\)"],
     "A", "OSC", "easy",
     "Pair 1 gives \\(\\frac{1}{21}\\), Pair 2 gives \\(-\\frac{7}{22}\\). Adding gives \\(\\frac{22 - 147}{462} = -\\frac{125}{462}\\)."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Reciprocal Inversion of Fraction with Negatives</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Top/Bottom Fraction boxes -->
    <rect x="40" y="30" width="100" height="70" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="90" y="55" fill="#ffffff" font-size="15" font-weight="bold" text-anchor="middle">p = -5</text>
    <line x1="55" y1="65" x2="125" y2="65" stroke="#60a5fa" stroke-width="2"/>
    <text x="90" y="88" fill="#ffffff" font-size="15" font-weight="bold" text-anchor="middle">q = 8</text>
    <!-- Invert arrows -->
    <path d="M 155,65 L 185,65" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="185,60 195,65 185,70" fill="#f59e0b"/>
    <!-- Reciprocal -->
    <rect x="205" y="30" width="100" height="70" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="255" y="55" fill="#6ee7b7" font-size="15" font-weight="bold" text-anchor="middle">q = -8</text>
    <line x1="220" y1="65" x2="290" y2="65" stroke="#34d399" stroke-width="2"/>
    <text x="255" y="88" fill="#6ee7b7" font-size="15" font-weight="bold" text-anchor="middle">p = 5</text>
    <text x="170" y="130" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Product = (-5/8) × (-8/5) = +40/40 = 1</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the multiplicative inverse of \(-\frac{5}{8}\)?</p>
</div>""",
     ["\\(-\\frac{8}{5}\\)", "\\(\\frac{8}{5}\\)", "\\(\\frac{5}{8}\\)", "1"],
     "A", "OSC", "easy",
     "Inverting numerator and denominator while preserving the sign gives \\(-\\frac{8}{5}\\)."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Associative Law of Multiplication</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Grouping 1: (a x b) x c -->
    <rect x="20" y="25" width="140" height="55" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="90" y="48" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">[ 2/3 × (-5/7) ] × 3/4</text>
    <text x="90" y="68" fill="#ffffff" font-size="11" text-anchor="middle">= (-10/21) × 3/4 = -5/14</text>
    <!-- Equals -->
    <text x="170" y="60" fill="#10b981" font-size="22" font-weight="bold" text-anchor="middle">=</text>
    <!-- Grouping 2: a x (b x c) -->
    <rect x="180" y="25" width="140" height="55" rx="6" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
    <text x="250" y="48" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">2/3 × [ (-5/7) × 3/4 ]</text>
    <text x="250" y="68" fill="#ffffff" font-size="11" text-anchor="middle">= 2/3 × (-15/28) = -5/14</text>
    <!-- Footer Note -->
    <text x="170" y="125" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">(a × b) × c = a × (b × c) holds unconditionally</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the product \(\left[\frac{2}{3} \times \left(-\frac{5}{7}\right)\right] \times \frac{3}{4}\)?</p>
</div>""",
     ["\\(-\\frac{5}{14}\\)", "\\(\\frac{5}{14}\\)", "\\(-\\frac{15}{28}\\)", "\\(\\frac{10}{21}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{2 \\times (-5) \\times 3}{3 \\times 7 \\times 4} = -\\frac{30}{84} = -\\frac{5}{14}\\).")
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch3_topic2.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
