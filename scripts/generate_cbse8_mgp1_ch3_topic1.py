# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-3-3.1
Topic: Rational Numbers & Closure, Commutative Properties
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-3-3.1"

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
    ("What is the formal mathematical definition of a rational number?",
     ["A number that can be written in the form \\(\\frac{p}{q}\\), where \\(p\\) and \\(q\\) are integers and \\(q \\neq 0\\)",
      "A number that can be written as \\(\\frac{p}{q}\\), where \\(p\\) and \\(q\\) are whole numbers and \\(q = 0\\)",
      "Any number with an infinite, non-repeating decimal expansion",
      "Only positive fractions whose numerator is smaller than the denominator"],
     "A", "OSC", "easy",
     "A rational number is defined as any number that can be expressed as the quotient \\(\\frac{p}{q}\\), where \\(p\\) and \\(q\\) are integers and \\(q \\neq 0\\)."),

    # 2
    ("Is \\(0\\) a rational number?",
     ["Yes, because it can be written as \\(\\frac{0}{q}\\) where \\(q\\) is any non-zero integer (e.g. \\(\\frac{0}{1}\\))",
      "No, because zero has no value",
      "No, because division by zero is not allowed",
      "Yes, but only when written as \\(\\frac{0}{0}\\)"],
     "A", "OSC", "easy",
     "Zero is a rational number because it can be written in \\(\\frac{p}{q}\\) form where \\(p = 0\\) and \\(q\\) is any non-zero integer, such as \\(\\frac{0}{1}\\) or \\(\\frac{0}{5}\\)."),

    # 3
    ("Under which of the following operations are rational numbers NOT closed?",
     ["Division", "Addition", "Subtraction", "Multiplication"],
     "A", "OSC", "easy",
     "Rational numbers are not closed under division because division by zero is undefined (for example, \\(\\frac{5}{0}\\) is not a rational number)."),

    # 4
    ("Which of the following operations on rational numbers is commutative?",
     ["Addition and Multiplication", "Subtraction and Division", "Addition and Subtraction", "Multiplication and Division"],
     "A", "OSC", "easy",
     "Addition and multiplication are commutative for rational numbers (\\(a + b = b + a\\) and \\(a \\times b = b \\times a\\)). Subtraction and division are not commutative."),

    # 5
    ("What is the standard form of the rational number \\(\\frac{-28}{84}\\)?",
     ["\\(-\\frac{1}{3}\\)", "\\(-\\frac{2}{6}\\)", "\\(\\frac{1}{3}\\)", "\\(-\\frac{7}{21}\\)"],
     "A", "OSC", "easy",
     "Divide both numerator and denominator by their greatest common divisor \\(\\gcd(28, 84) = 28\\): \\(\\frac{-28 \\div 28}{84 \\div 28} = -\\frac{1}{3}\\)."),

    # 6
    ("What is the standard form of \\(\\frac{45}{-105}\\)?",
     ["\\(-\\frac{3}{7}\\)", "\\(\\frac{3}{-7}\\)", "\\(-\\frac{9}{21}\\)", "\\(\\frac{3}{7}\\)"],
     "A", "OSC", "easy",
     "In standard form, the denominator must be positive and numerator/denominator coprime. Dividing by 15: \\(\\frac{45 \\div 15}{-105 \\div 15} = \\frac{3}{-7} = -\\frac{3}{7}\\)."),

    # 7
    ("Evaluate: \\(\\frac{-3}{8} + \\frac{5}{8}\\)",
     ["\\(\\frac{1}{4}\\)", "\\(\\frac{2}{8}\\)", "\\(-\\frac{1}{4}\\)", "\\(1\\)"],
     "A", "OSC", "easy",
     "Since denominators are identical: \\(\\frac{-3 + 5}{8} = \\frac{2}{8} = \\frac{1}{4}\\)."),

    # 8
    ("Evaluate: \\(\\frac{-2}{3} + \\frac{3}{5}\\)",
     ["\\(-\\frac{1}{15}\\)", "\\(\\frac{1}{15}\\)", "\\(-\\frac{5}{15}\\)", "\\(\\frac{5}{8}\\)"],
     "A", "OSC", "easy",
     "LCM of 3 and 5 is 15: \\(\\frac{-10 + 9}{15} = -\\frac{1}{15}\\)."),

    # 9
    ("Evaluate: \\(\\frac{4}{7} - \\frac{-3}{7}\\)",
     ["\\(1\\)", "\\(\\frac{1}{7}\\)", "\\(-\\frac{1}{7}\\)", "\\(\\frac{7}{14}\\)"],
     "A", "OSC", "easy",
     "Subtracting a negative fraction is equivalent to adding: \\(\\frac{4}{7} - \\left(-\\frac{3}{7}\\right) = \\frac{4 + 3}{7} = \\frac{7}{7} = 1\\)."),

    # 10
    ("Evaluate: \\(\\frac{-5}{6} - \\frac{1}{4}\\)",
     ["\\(-\\frac{13}{12}\\)", "\\(-\\frac{11}{12}\\)", "\\(-\\frac{7}{12}\\)", "\\(\\frac{13}{12}\\)"],
     "A", "OSC", "medium",
     "LCM of 6 and 4 is 12: \\(\\frac{-10 - 3}{12} = -\\frac{13}{12}\\)."),

    # 11
    ("Evaluate: \\(\\frac{-3}{7} \\times \\frac{14}{15}\\)",
     ["\\(-\\frac{2}{5}\\)", "\\(\\frac{2}{5}\\)", "\\(-\\frac{6}{35}\\)", "\\(-\\frac{1}{5}\\)"],
     "A", "OSC", "easy",
     "Multiply and simplify: \\(\\frac{-3 \\times 14}{7 \\times 15} = \\frac{-1 \\times 2}{1 \\times 5} = -\\frac{2}{5}\\)."),

    # 12
    ("Evaluate: \\(\\frac{-8}{25} \\div \\frac{-4}{15}\\)",
     ["\\(\\frac{6}{5}\\)", "\\(-\\frac{6}{5}\\)", "\\(\\frac{32}{375}\\)", "\\(\\frac{5}{6}\\)"],
     "A", "OSC", "medium",
     "Multiplying by reciprocal: \\(\\frac{-8}{25} \\times \\frac{15}{-4} = \\frac{-8 \\times 15}{25 \\times -4} = \\frac{2 \\times 3}{5 \\times 1} = \\frac{6}{5}\\)."),

    # 13
    ("Which property is illustrated by \\(\\frac{-2}{3} + \\frac{5}{7} = \\frac{5}{7} + \\left(\\frac{-2}{3}\\right)\\)?",
     ["Commutative property of addition",
      "Associative property of addition",
      "Distributive property",
      "Closure property of addition"],
     "A", "OSC", "easy",
     "Changing the order of the two terms without changing the sum demonstrates the commutative property of addition: \\(a + b = b + a\\)."),

    # 14
    ("Which property is illustrated by \\(\\frac{-4}{5} \\times \\frac{3}{8} = \\frac{3}{8} \\times \\left(\\frac{-4}{5}\\right)\\)?",
     ["Commutative property of multiplication",
      "Associative property of multiplication",
      "Closure property of multiplication",
      "Identity property"],
     "A", "OSC", "easy",
     "\\(a \\times b = b \\times a\\) demonstrates commutativity of multiplication."),

    # 15
    ("Is subtraction of rational numbers commutative? Check with \\(\\frac{1}{2} - \\frac{1}{3}\\) and \\(\\frac{1}{3} - \\frac{1}{2}\\).",
     ["No, because \\(\\frac{1}{2} - \\frac{1}{3} = \\frac{1}{6}\\) whereas \\(\\frac{1}{3} - \\frac{1}{2} = -\\frac{1}{6}\\)",
      "Yes, both equal \\(\\frac{1}{6}\\)",
      "Yes, both equal 0",
      "No, because rational numbers cannot be subtracted"],
     "A", "OSC", "easy",
     "\\(\\frac{1}{2} - \\frac{1}{3} = \\frac{1}{6}\\), while \\(\\frac{1}{3} - \\frac{1}{2} = -\\frac{1}{6}\\). Since \\(\\frac{1}{6} \\neq -\\frac{1}{6}\\), subtraction is not commutative."),

    # 16
    ("Is division of rational numbers commutative? Compare \\(\\frac{2}{3} \\div \\frac{4}{5}\\) and \\(\\frac{4}{5} \\div \\frac{2}{3}\\).",
     ["No, because \\(\\frac{2}{3} \\div \\frac{4}{5} = \\frac{5}{6}\\) whereas \\(\\frac{4}{5} \\div \\frac{2}{3} = \\frac{6}{5}\\)",
      "Yes, both equal 1",
      "Yes, both equal \\(\\frac{5}{6}\\)",
      "No, because fractions cannot be divided"],
     "A", "OSC", "easy",
     "\\(\\frac{2}{3} \\times \\frac{5}{4} = \\frac{5}{6}\\), but \\(\\frac{4}{5} \\times \\frac{3}{2} = \\frac{6}{5}\\). Since \\(\\frac{5}{6} \\neq \\frac{6}{5}\\), division is not commutative."),

    # 17
    ("Which of the following numbers is NOT a rational number?",
     ["\\(\\sqrt{5}\\)", "\\(\\frac{22}{7}\\)", "\\(3.14\\)", "\\(-7\\)"],
     "A", "OSC", "easy",
     "\\(\\sqrt{5}\\) is an irrational number because 5 is not a perfect square, so its decimal expansion is non-terminating and non-repeating. \\(\\frac{22}{7}\\), \\(3.14 = \\frac{314}{100}\\), and \\(-7 = \\frac{-7}{1}\\) are all rational numbers."),

    # 18
    ("Which rational number is equal to its own opposite (negative)?",
     ["0", "1", "-1", "No such number exists"],
     "A", "OSC", "easy",
     "\\(-0 = 0\\), so zero is the unique rational number that equals its own additive inverse."),

    # 19
    ("Which rational numbers are equal to their own reciprocals?",
     ["1 and -1", "0 and 1", "Only 1", "All positive integers"],
     "A", "OSC", "easy",
     "The reciprocal of 1 is \\(\\frac{1}{1} = 1\\), and the reciprocal of -1 is \\(\\frac{1}{-1} = -1\\). Hence 1 and -1 are their own reciprocals."),

    # 20
    ("Which rational number has NO reciprocal?",
     ["0", "1", "-1", "\\(\\frac{1}{2}\\)"],
     "A", "OSC", "easy",
     "The reciprocal of 0 would be \\(\\frac{1}{0}\\), which is undefined because division by zero is mathematically impossible."),

    # 21
    ("Compare the rational numbers \\(\\frac{-4}{9}\\) and \\(\\frac{-5}{12}\\). Which is greater?",
     ["\\(\\frac{-5}{12}\\)", "\\(\\frac{-4}{9}\\)", "Both are equal", "Cannot be determined"],
     "A", "OSC", "medium",
     "LCM of 9 and 12 is 36: \\(\\frac{-4}{9} = \\frac{-16}{36}\\) and \\(\\frac{-5}{12} = \\frac{-15}{36}\\). On the number line, \\(-15 > -16\\), so \\(\\frac{-15}{36} > \\frac{-16}{36}\\), meaning \\(\\frac{-5}{12} > \\frac{-4}{9}\\)."),

    # 22
    ("Compare \\(\\frac{-7}{10}\\) and \\(\\frac{5}{-8}\\). Which is smaller?",
     ["\\(\\frac{-7}{10}\\)", "\\(\\frac{5}{-8}\\)", "Both are equal", "Cannot be determined"],
     "A", "OSC", "medium",
     "Standard forms: \\(\\frac{-7}{10} = \\frac{-28}{40}\\) and \\(\\frac{-5}{8} = \\frac{-25}{40}\\). Since \\(-28 < -25\\), \\(\\frac{-7}{10}\\) is smaller."),

    # 23
    ("Simplify: \\(\\left(\\frac{-3}{5} + \\frac{7}{10}\\right) - \\frac{1}{2}\\)",
     ["\\(-\\frac{2}{5}\\)", "\\(\\frac{2}{5}\\)", "\\(-\\frac{1}{10}\\)", "\\(0\\)"],
     "A", "OSC", "medium",
     "Inside parentheses: \\(\\frac{-6 + 7}{10} = \\frac{1}{10}\\). Then \\(\\frac{1}{10} - \\frac{1}{2} = \\frac{1 - 5}{10} = -\\frac{4}{10} = -\\frac{2}{5}\\)."),

    # 24
    ("Simplify: \\(\\frac{-5}{9} \\times \\left(\\frac{18}{25} - \\frac{3}{5}\\right)\\)",
     ["\\(-\\frac{1}{15}\\)", "\\(\\frac{1}{15}\\)", "\\(-\\frac{2}{15}\\)", "\\(\\frac{2}{5}\\)"],
     "A", "OSC", "medium",
     "Inside: \\(\\frac{18}{25} - \\frac{15}{25} = \\frac{3}{25}\\). Multiply: \\(\\frac{-5}{9} \\times \\frac{3}{25} = \\frac{-1 \\times 1}{3 \\times 5} = -\\frac{1}{15}\\)."),

    # 25
    ("What must be added to \\(\\frac{-5}{8}\\) to get \\(\\frac{-3}{2}\\)?",
     ["\\(-\\frac{7}{8}\\)", "\\(\\frac{7}{8}\\)", "\\(-\\frac{11}{8}\\)", "\\(\\frac{11}{8}\\)"],
     "A", "OSC", "medium",
     "Let the required number be \\(x\\). Then \\(\\frac{-5}{8} + x = -\\frac{3}{2} \\implies x = -\\frac{3}{2} - \\left(-\\frac{5}{8}\\right) = -\\frac{12}{8} + \\frac{5}{8} = -\\frac{7}{8}\\)."),

    # 26
    ("What must be subtracted from \\(\\frac{-2}{3}\\) to get \\(\\frac{-1}{6}\\)?",
     ["\\(-\\frac{1}{2}\\)", "\\(\\frac{1}{2}\\)", "\\(-\\frac{5}{6}\\)", "\\(\\frac{5}{6}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{-2}{3} - x = -\\frac{1}{6} \\implies x = -\\frac{2}{3} - \\left(-\\frac{1}{6}\\right) = -\\frac{4}{6} + \\frac{1}{6} = -\\frac{3}{6} = -\\frac{1}{2}\\)."),

    # 27
    ("The product of two rational numbers is \\(\\frac{-16}{9}\\). If one of them is \\(\\frac{-4}{3}\\), find the other.",
     ["\\(\\frac{4}{3}\\)", "\\(-\\frac{4}{3}\\)", "\\(\\frac{64}{27}\\)", "\\(-\\frac{64}{27}\\)"],
     "A", "OSC", "medium",
     "Other number = \\(\\frac{-16}{9} \\div \\frac{-4}{3} = \\frac{-16}{9} \\times \\frac{3}{-4} = \\frac{4 \\times 1}{3 \\times 1} = \\frac{4}{3}\\)."),

    # 28
    ("By what rational number should \\(\\frac{-3}{4}\\) be divided to get \\(\\frac{9}{16}\\)?",
     ["\\(-\\frac{4}{3}\\)", "\\(\\frac{4}{3}\\)", "\\(-\\frac{3}{4}\\)", "\\(-\\frac{27}{64}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{-3}{4} \\div x = \\frac{9}{16} \\implies x = \\frac{-3}{4} \\div \\frac{9}{16} = \\frac{-3}{4} \\times \\frac{16}{9} = -\\frac{4}{3}\\)."),

    # 29
    ("The sum of two rational numbers is \\(-2\\). If one of them is \\(\\frac{-14}{5}\\), find the other.",
     ["\\(\\frac{4}{5}\\)", "\\(-\\frac{4}{5}\\)", "\\(\\frac{24}{5}\\)", "\\(-\\frac{24}{5}\\)"],
     "A", "OSC", "medium",
     "Other number = \\(-2 - \\left(-\\frac{14}{5}\\right) = -\\frac{10}{5} + \\frac{14}{5} = \\frac{4}{5}\\)."),

    # 30
    ("Which of the following rational numbers is in standard form?",
     ["\\(\\frac{-7}{15}\\)", "\\(\\frac{4}{-10}\\)", "\\(\\frac{-6}{9}\\)", "\\(\\frac{14}{21}\\)"],
     "A", "OSC", "easy",
     "In \\(\\frac{-7}{15}\\), the denominator 15 is positive and \\(\\gcd(7, 15) = 1\\). In all other options, numerator and denominator share common factors or have negative denominators."),

    # 31
    ("Find the value of \\(x\\) if \\(\\frac{-3}{5} = \\frac{x}{20}\\).",
     ["-12", "12", "-15", "15"],
     "A", "OSC", "easy",
     "Cross multiplying: \\(5x = -3 \\times 20 = -60 \\implies x = -12\\)."),

    # 32
    ("Find the value of \\(y\\) if \\(\\frac{7}{-4} = \\frac{-21}{y}\\).",
     ["12", "-12", "14", "-14"],
     "A", "OSC", "easy",
     "\\(\\frac{-7}{4} = \\frac{-21}{y} \\implies -7y = 4 \\times (-21) = -84 \\implies y = 12\\)."),

    # 33
    ("Express \\(\\frac{-3}{7}\\) as a rational number with denominator 35.",
     ["\\(\\frac{-15}{35}\\)", "\\(\\frac{-12}{35}\\)", "\\(\\frac{15}{35}\\)", "\\(\\frac{-21}{35}\\)"],
     "A", "OSC", "easy",
     "Multiply both numerator and denominator by 5: \\(\\frac{-3 \\times 5}{7 \\times 5} = \\frac{-15}{35}\\)."),

    # 34
    ("Assertion (A): The sum of two rational numbers is always a rational number.\nReason (R): Rational numbers are closed under addition.",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "By definition of closure under addition, the sum of any two elements in the set of rational numbers is itself an element of the set."),

    # 35
    ("Assertion (A): Subtraction is commutative for rational numbers.\nReason (R): For any two rational numbers \\(a\\) and \\(b\\), \\(a - b = -(b - a) \\neq b - a\\) (unless \\(a = b\\)).",
     ["(A) is false but (R) is true",
      "Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false"],
     "A", "OAR", "medium",
     "(A) is false because subtraction is definitely not commutative. (R) correctly explains why commutativity fails: reversing the subtraction reverses the algebraic sign."),

    # 36
    ("True or False: Every integer is also a rational number.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Any integer \\(n\\) can be written as \\(\\frac{n}{1}\\), where \\(n\\) and 1 are integers with non-zero denominator, so every integer is rational."),

    # 37
    ("True or False: Rational numbers are closed under division by non-zero rational numbers.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Excluding division by zero, the quotient of any two rational numbers \\(\\frac{p}{q} \\div \\frac{r}{s} = \\frac{ps}{qr}\\) is always a valid rational number."),

    # 38
    ("Fill in the blank: A rational number \\(\\frac{p}{q}\\) is in lowest terms if \\(\\gcd(|p|, |q|) = \\) _____.",
     ["1", "0", "\\(p\\)", "\\(q\\)"],
     "A", "OFB", "easy",
     "A fraction is in lowest terms (irreducible) when numerator and denominator have no common factor other than 1."),

    # 39
    ("Fill in the blank: Division of rational numbers is _____ under multiplication.",
     ["closed", "not commutative", "commutative", "associative"],
     "A", "OFB", "easy",
     "Rational numbers are closed under multiplication."),

    # 40
    ("What is the numerical integer value of \\(\\frac{-15}{4} \\times \\frac{-8}{5}\\)?",
     ["6", "-6", "12", "-12"],
     "A", "ONE", "easy",
     "\\(\\frac{-15 \\times (-8)}{4 \\times 5} = \\frac{120}{20} = 6\\)."),
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    ("Evaluate: \\(\\frac{7}{11} + \\frac{-4}{11}\\)",
     ["\\(\\frac{3}{11}\\)", "\\(-\\frac{3}{11}\\)", "\\(\\frac{11}{11} = 1\\)", "\\(-\\frac{11}{11}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{7 + (-4)}{11} = \\frac{3}{11}\\)."),

    # 42
    ("Evaluate: \\(\\frac{-5}{12} + \\frac{7}{18}\\)",
     ["\\(-\\frac{1}{36}\\)", "\\(\\frac{1}{36}\\)", "\\(-\\frac{2}{30}\\)", "\\(\\frac{2}{36}\\)"],
     "A", "OSC", "medium",
     "LCM of 12 and 18 is 36: \\(\\frac{-15 + 14}{36} = -\\frac{1}{36}\\)."),

    # 43
    ("Evaluate: \\(\\frac{3}{8} - \\frac{5}{12}\\)",
     ["\\(-\\frac{1}{24}\\)", "\\(\\frac{1}{24}\\)", "\\(-\\frac{2}{4}\\)", "\\(-\\frac{1}{12}\\)"],
     "A", "OSC", "easy",
     "LCM of 8 and 12 is 24: \\(\\frac{9 - 10}{24} = -\\frac{1}{24}\\)."),

    # 44
    ("Evaluate: \\(\\frac{-4}{9} - \\frac{-7}{12}\\)",
     ["\\(\\frac{5}{36}\\)", "\\(-\\frac{5}{36}\\)", "\\(\\frac{11}{36}\\)", "\\(-\\frac{11}{36}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{-4}{9} + \\frac{7}{12} = \\frac{-16 + 21}{36} = \\frac{5}{36}\\)."),

    # 45
    ("Evaluate: \\(\\frac{-9}{16} \\times \\frac{-4}{3}\\)",
     ["\\(\\frac{3}{4}\\)", "\\(-\\frac{3}{4}\\)", "\\(\\frac{27}{64}\\)", "\\(-\\frac{27}{64}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{-9 \\times (-4)}{16 \\times 3} = \\frac{36}{48} = \\frac{3}{4}\\)."),

    # 46
    ("Evaluate: \\(\\frac{14}{25} \\times \\frac{-15}{28}\\)",
     ["\\(-\\frac{3}{10}\\)", "\\(\\frac{3}{10}\\)", "\\(-\\frac{5}{14}\\)", "\\(-\\frac{1}{2}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{14 \\times (-15)}{25 \\times 28} = \\frac{1 \\times (-3)}{5 \\times 2} = -\\frac{3}{10}\\)."),

    # 47
    ("Evaluate: \\(\\frac{-13}{18} \\div \\frac{-26}{27}\\)",
     ["\\(\\frac{3}{4}\\)", "\\(-\\frac{3}{4}\\)", "\\(\\frac{4}{3}\\)", "\\(-\\frac{4}{3}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{-13}{18} \\times \\frac{27}{-26} = \\frac{-1 \\times 3}{2 \\times (-2)} = \\frac{3}{4}\\)."),

    # 48
    ("Evaluate: \\(\\frac{21}{32} \\div \\frac{-7}{8}\\)",
     ["\\(-\\frac{3}{4}\\)", "\\(\\frac{3}{4}\\)", "\\(-\\frac{4}{3}\\)", "\\(-\\frac{147}{256}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{21}{32} \\times \\frac{8}{-7} = \\frac{3 \\times 1}{4 \\times (-1)} = -\\frac{3}{4}\\)."),

    # 49
    ("Reduce \\(\\frac{-72}{108}\\) to lowest terms.",
     ["\\(-\\frac{2}{3}\\)", "\\(-\\frac{4}{6}\\)", "\\(\\frac{2}{3}\\)", "\\(-\\frac{8}{12}\\)"],
     "A", "OSC", "easy",
     "\\(\\gcd(72, 108) = 36\\). Divide both by 36: \\(\\frac{-72 \\div 36}{108 \\div 36} = -\\frac{2}{3}\\)."),

    # 50
    ("Reduce \\(\\frac{56}{-96}\\) to standard form.",
     ["\\(-\\frac{7}{12}\\)", "\\(\\frac{7}{-12}\\)", "\\(-\\frac{14}{24}\\)", "\\(\\frac{7}{12}\\)"],
     "A", "OSC", "easy",
     "\\(\\gcd(56, 96) = 8\\). Divide both by 8: \\(\\frac{7}{-12} = -\\frac{7}{12}\\)."),

    # 51
    ("Which of the pairs are equivalent rational numbers?",
     ["\\(\\frac{-3}{8}\\) and \\(\\frac{15}{-40}\\)",
      "\\(\\frac{-3}{8}\\) and \\(\\frac{-15}{40}\\) (opposite sign)",
      "\\(\\frac{2}{3}\\) and \\(\\frac{3}{2}\\)",
      "\\(\\frac{-4}{5}\\) and \\(\\frac{5}{-4}\\)"],
     "A", "OSC", "easy",
     "Cross multiplication: \\(-3 \\times (-40) = 120\\) and \\(8 \\times 15 = 120\\). Since cross products match, they are equivalent."),

    # 52
    ("Find the value of \\(x\\) if \\(\\frac{-4}{9} = \\frac{-28}{x}\\).",
     ["63", "-63", "56", "-56"],
     "A", "OSC", "easy",
     "\\(-4x = 9 \\times (-28) = -252 \\implies x = 63\\)."),

    # 53
    ("Find the value of \\(p\\) if \\(\\frac{p}{14} = \\frac{-5}{2}\\).",
     ["-35", "35", "-28", "28"],
     "A", "OSC", "easy",
     "\\(2p = 14 \\times (-5) = -70 \\implies p = -35\\)."),

    # 54
    ("What must be added to \\(\\frac{-7}{12}\\) to get \\(0\\)?",
     ["\\(\\frac{7}{12}\\)", "\\(-\\frac{7}{12}\\)", "1", "-1"],
     "A", "OSC", "easy",
     "The additive inverse of \\(\\frac{-7}{12}\\) is \\(\\frac{7}{12}\\)."),

    # 55
    ("What is the reciprocal of \\(\\frac{-3}{5} \\times \\frac{-10}{9}\\)?",
     ["\\(\\frac{3}{2}\\)", "\\(-\\frac{3}{2}\\)", "\\(\\frac{2}{3}\\)", "\\(-\\frac{2}{3}\\)"],
     "A", "OSC", "medium",
     "Product = \\(\\frac{(-3) \\times (-10)}{5 \\times 9} = \\frac{30}{45} = \\frac{2}{3}\\). The reciprocal of \\(\\frac{2}{3}\\) is \\(\\frac{3}{2}\\)."),

    # 56
    ("Simplify: \\(\\left(\\frac{2}{3} \\times \\frac{-5}{4}\\right) + \\left(\\frac{-3}{2} \\times \\frac{-1}{6}\\right)\\)",
     ["\\(-\\frac{7}{12}\\)", "\\(\\frac{7}{12}\\)", "\\(-\\frac{5}{6}\\)", "\\(\\frac{1}{4}\\)"],
     "A", "OSC", "medium",
     "First product: \\(\\frac{2 \\times (-5)}{3 \\times 4} = -\\frac{5}{6} = -\\frac{10}{12}\\). Second product: \\(\\frac{(-3) \\times (-1)}{2 \\times 6} = \\frac{3}{12} = \\frac{1}{4}\\). Sum: \\(-\\frac{10}{12} + \\frac{3}{12} = -\\frac{7}{12}\\)."),

    # 57
    ("Simplify: \\(\\left(\\frac{-3}{8} \\div \\frac{9}{16}\\right) - \\left(\\frac{5}{6} \\div \\frac{-10}{9}\\right)\\)",
     ["\\(\\frac{1}{12}\\)", "\\(-\\frac{1}{12}\\)", "\\(-\\frac{17}{12}\\)", "\\(\\frac{17}{12}\\)"],
     "A", "OSC", "medium",
     "First term: \\(\\frac{-3}{8} \\times \\frac{16}{9} = -\\frac{2}{3} = -\\frac{8}{12}\\). Second term: \\(\\frac{5}{6} \\times \\frac{9}{-10} = -\\frac{3}{4} = -\\frac{9}{12}\\). Subtracting: \\(-\\frac{8}{12} - \\left(-\\frac{9}{12}\\right) = -\\frac{8}{12} + \\frac{9}{12} = \\frac{1}{12}\\)."),

    # 58
    ("A car travels \\(120\\frac{1}{2}\\text{ km}\\) in \\(2\\frac{1}{2}\\text{ hours}\\). What is its average speed in km/h?",
     ["\\(48.2\\text{ km/h}\\)", "\\(50\\text{ km/h}\\)", "\\(48\\text{ km/h}\\)", "\\(52\\text{ km/h}\\)"],
     "A", "OSC", "medium",
     "Distance = \\(\\frac{241}{2}\\text{ km}\\), Time = \\(\\frac{5}{2}\\text{ h}\\). Speed = \\(\\frac{241}{2} \\div \\frac{5}{2} = \\frac{241}{2} \\times \\frac{2}{5} = \\frac{241}{5} = 48.2\\text{ km/h}\\)."),

    # 59
    ("The perimeter of an equilateral triangle is \\(14\\frac{1}{4}\\text{ cm}\\). Find the length of each side.",
     ["\\(4\\frac{3}{4}\\text{ cm}\\)",
      "\\(4\\frac{1}{4}\\text{ cm}\\)",
      "\\(4\\frac{1}{2}\\text{ cm}\\)",
      "\\(5\\text{ cm}\\)"],
     "A", "OSC", "medium",
     "Side = Perimeter / 3 = \\(\\frac{57}{4} \\div 3 = \\frac{57}{4} \\times \\frac{1}{3} = \\frac{19}{4} = 4\\frac{3}{4}\\text{ cm}\\)."),

    # 60
    ("From a rope of length \\(20\\text{ m}\\), two pieces of lengths \\(3\\frac{5}{8}\\text{ m}\\) and \\(8\\frac{1}{4}\\text{ m}\\) are cut off. What is the length of the remaining rope?",
     ["\\(8\\frac{1}{8}\\text{ m}\\)",
      "\\(8\\frac{3}{8}\\text{ m}\\)",
      "\\(7\\frac{7}{8}\\text{ m}\\)",
      "\\(9\\frac{1}{8}\\text{ m}\\)"],
     "A", "OSC", "medium",
     "Total cut = \\(\\frac{29}{8} + \\frac{33}{4} = \\frac{29 + 66}{8} = \\frac{95}{8}\\text{ m}\\). Remaining = \\(20 - \\frac{95}{8} = \\frac{160 - 95}{8} = \\frac{65}{8} = 8\\frac{1}{8}\\text{ m}\\)."),

    # 61
    ("Which of the following is equivalent to \\(\\frac{-2}{5}\\)?",
     ["\\(\\frac{-10}{25}\\)", "\\(\\frac{10}{25}\\)", "\\(\\frac{-10}{-25}\\)", "\\(\\frac{-6}{10}\\)"],
     "A", "OSC", "easy",
     "Multiply numerator and denominator by 5: \\(\\frac{-2 \\times 5}{5 \\times 5} = \\frac{-10}{25}\\)."),

    # 62
    ("Which rational number lies between \\(0\\) and \\(-1\\)?",
     ["\\(-\\frac{1}{2}\\)", "\\(-\\frac{3}{2}\\)", "\\(\\frac{1}{2}\\)", "\\(-2\\)"],
     "A", "OSC", "easy",
     "\\(-0.5\\) lies strictly between 0 and -1."),

    # 63
    ("What is the sum of \\(\\frac{-3}{7}\\) and its additive inverse?",
     ["0", "1", "-1", "\\(-\\frac{6}{7}\\)"],
     "A", "OSC", "easy",
     "The sum of any number and its additive inverse is 0: \\(\\frac{-3}{7} + \\frac{3}{7} = 0\\)."),

    # 64
    ("What is the product of \\(\\frac{-4}{9}\\) and its reciprocal?",
     ["1", "-1", "0", "\\(\\frac{16}{81}\\)"],
     "A", "OSC", "easy",
     "The product of any non-zero rational number and its reciprocal is 1: \\(\\frac{-4}{9} \\times \\frac{-9}{4} = 1\\)."),

    # 65
    ("Simplify: \\(\\frac{-4}{5} \\times 1\\)",
     ["\\(-\\frac{4}{5}\\)", "\\(\\frac{4}{5}\\)", "1", "0"],
     "A", "OSC", "easy",
     "1 is the multiplicative identity: \\(a \\times 1 = a\\)."),

    # 66
    ("True or False: The product of two negative rational numbers is always positive.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Negative times negative equals positive: \\(\\left(-\\frac{a}{b}\\right) \\times \\left(-\\frac{c}{d}\\right) = +\\frac{ac}{bd}\\)."),

    # 67
    ("True or False: Every rational number has an additive inverse.",
     ["True", "False"],
     "A", "OTF", "easy",
     "For every rational number \\(x\\), \\(-x\\) exists such that \\(x + (-x) = 0\\)."),

    # 68
    ("Fill in the blank: The rational number _____ has no sign (neither positive nor negative).",
     ["0", "1", "-1", "Infinity"],
     "A", "OFB", "easy",
     "Zero is the only neutral number that is neither positive nor negative."),

    # 69
    ("Fill in the blank: If \\(\\frac{a}{b} = \\frac{c}{d}\\), then \\(ad = \\) _____.",
     ["\\(bc\\)", "\\(ac\\)", "\\(bd\\)", "\\(a+d\\)"],
     "A", "OFB", "easy",
     "By the fundamental property of equivalent fractions, the cross products are equal: \\(ad = bc\\)."),

    # 70
    ("What is the numerical integer value of \\(\\left(\\frac{-18}{5}\\right) \\div \\left(\\frac{-3}{5}\\right)\\)?",
     ["6", "-6", "9", "-9"],
     "A", "ONE", "easy",
     "\\(\\frac{-18}{5} \\times \\frac{5}{-3} = 6\\)."),
]

# 12 MOCK / FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Hierarchy of Number Sets (Venn Diagram)</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Nested Ellipses -->
    <!-- Rationals Q -->
    <ellipse cx="170" cy="80" rx="150" ry="60" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="50" y="45" fill="#38bdf8" font-size="12" font-weight="bold">Q: Rationals (p/q, -3/4, 0.5)</text>
    <!-- Integers Z -->
    <ellipse cx="185" cy="88" rx="115" ry="45" fill="#1e293b" stroke="#818cf8" stroke-width="1.5"/>
    <text x="100" y="65" fill="#a5b4fc" font-size="11" font-weight="bold">Z: Integers (-3, -2, -1)</text>
    <!-- Whole Numbers W -->
    <ellipse cx="205" cy="95" rx="80" ry="32" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
    <text x="155" y="83" fill="#6ee7b7" font-size="10" font-weight="bold">W: Whole (0)</text>
    <!-- Natural Numbers N -->
    <ellipse cx="225" cy="103" rx="45" ry="20" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="225" y="108" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">N: Natural (1,2,3)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Which of the following statements is correctly illustrated by the nested sets diagram?</p>
</div>""",
     ["Every integer is a rational number, but not every rational number is an integer",
      "Every rational number is an integer",
      "Natural numbers contain all rational numbers",
      "Integers and rational numbers have zero overlap"],
     "A", "OSC", "easy",
     "Integers \\(\\mathbb{Z}\\) are completely enclosed inside rational numbers \\(\\mathbb{Q}\\), proving every integer is a rational number (with denominator 1). Fractions like \\(\\frac{1}{2}\\) are rational but not integers."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Closure Property Matrix across Operations</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Table Grid -->
    <g fill="#334155" stroke="#475569" stroke-width="1">
      <rect x="20" y="25" width="70" height="25"/>
      <rect x="90" y="25" width="55" height="25"/>
      <rect x="145" y="25" width="55" height="25"/>
      <rect x="200" y="25" width="55" height="25"/>
      <rect x="255" y="25" width="65" height="25"/>
      <rect x="20" y="50" width="70" height="40"/>
      <rect x="90" y="50" width="55" height="40"/>
      <rect x="145" y="50" width="55" height="40"/>
      <rect x="200" y="50" width="55" height="40"/>
      <rect x="255" y="50" width="65" height="40"/>
    </g>
    <!-- Headers -->
    <text x="55" y="42" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="middle">Number Set</text>
    <text x="117" y="42" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">+</text>
    <text x="172" y="42" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">-</text>
    <text x="227" y="42" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">×</text>
    <text x="287" y="42" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">÷</text>
    <!-- Rational Numbers Row -->
    <text x="55" y="74" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Rationals</text>
    <text x="117" y="75" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">YES</text>
    <text x="172" y="75" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">YES</text>
    <text x="227" y="75" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">YES</text>
    <text x="287" y="75" fill="#f87171" font-size="12" font-weight="bold" text-anchor="middle">NO (÷0)</text>
    <!-- Footnote -->
    <text x="170" y="125" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Rationals are closed under +, -, and × but NOT ÷</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Why is the set of all rational numbers NOT closed under division?</p>
</div>""",
     ["Because division by zero is not defined",
      "Because dividing fractions produces irrational numbers",
      "Because negative fractions cannot be divided",
      "Because division is not commutative"],
     "A", "OSC", "easy",
     "For any rational number \\(a\\), \\(a \\div 0\\) is undefined and does not yield a rational number, so rational numbers are not closed under division."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Commutative Addition vs Non-Commutative Subtraction</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Addition Balance (Balanced) -->
    <rect x="25" y="25" width="135" height="95" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
    <text x="92" y="48" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">Addition: a + b = b + a</text>
    <text x="92" y="70" fill="#ffffff" font-size="12" text-anchor="middle">1/2 + 1/3 = 5/6</text>
    <text x="92" y="90" fill="#ffffff" font-size="12" text-anchor="middle">1/3 + 1/2 = 5/6</text>
    <text x="92" y="110" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">COMMUTATIVE (BALANCED)</text>
    <!-- Subtraction Inequality (Tilted) -->
    <rect x="180" y="25" width="135" height="95" rx="6" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
    <text x="247" y="48" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">Subtraction: a - b ≠ b - a</text>
    <text x="247" y="70" fill="#ffffff" font-size="12" text-anchor="middle">1/2 - 1/3 = +1/6</text>
    <text x="247" y="90" fill="#ffffff" font-size="12" text-anchor="middle">1/3 - 1/2 = -1/6</text>
    <text x="247" y="110" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">NOT COMMUTATIVE (+ ≠ -)</text>
    <text x="170" y="138" fill="#fde047" font-size="10" text-anchor="middle">Reversing subtraction reverses the algebraic sign</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the relationship between \((a - b)\) and \((b - a)\) for any rational numbers?</p>
</div>""",
     ["\\(a - b = -(b - a)\\)", "\\(a - b = b - a\\)", "\\(a - b = \\frac{1}{b - a}\\)", "\\(a - b = (b - a)^2\\)"],
     "A", "OSC", "easy",
     "\\(a - b = -(b - a)\\). They have equal magnitudes but opposite signs, confirming subtraction is not commutative."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Reduction to Standard Form</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Step 1: Transfer negative sign to numerator -->
    <rect x="20" y="30" width="85" height="50" rx="5" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="62" y="52" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">36 / -54</text>
    <text x="62" y="70" fill="#cbd5e1" font-size="9" text-anchor="middle">Negative in denom</text>
    <!-- Arrow 1 -->
    <text x="120" y="60" fill="#f59e0b" font-size="16" text-anchor="middle">→</text>
    <!-- Step 2: -36 / 54 -->
    <rect x="135" y="30" width="85" height="50" rx="5" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="177" y="52" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">-36 / 54</text>
    <text x="177" y="70" fill="#cbd5e1" font-size="9" text-anchor="middle">q &gt; 0 enforced</text>
    <!-- Arrow 2 -->
    <text x="235" y="60" fill="#f59e0b" font-size="16" text-anchor="middle">→</text>
    <!-- Step 3: Divide by GCD 18 -->
    <rect x="250" y="30" width="75" height="50" rx="5" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="287" y="52" fill="#6ee7b7" font-size="15" font-weight="bold" text-anchor="middle">-2 / 3</text>
    <text x="287" y="70" fill="#e2e8f0" font-size="9" text-anchor="middle">gcd(2,3) = 1</text>
    <!-- Bottom rule -->
    <text x="170" y="125" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Standard Form Criteria: (1) Denominator &gt; 0, (2) GCD(|p|, q) = 1</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the standard form of \(\frac{36}{-54}\)?</p>
</div>""",
     ["\\(-\\frac{2}{3}\\)", "\\(\\frac{2}{-3}\\)", "\\(-\\frac{6}{9}\\)", "\\(\\frac{2}{3}\\)"],
     "A", "OSC", "easy",
     "Transfer the minus sign to the numerator and divide both 36 and 54 by their GCD 18: \\(\\frac{-36 \\div 18}{54 \\div 18} = -\\frac{2}{3}\\)."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Fraction Comparison by Cross-Multiplication</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Fraction A -->
    <rect x="40" y="25" width="80" height="50" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="80" y="55" fill="#93c5fd" font-size="16" font-weight="bold" text-anchor="middle">-3 / 5</text>
    <!-- Fraction B -->
    <rect x="220" y="25" width="80" height="50" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="260" y="55" fill="#93c5fd" font-size="16" font-weight="bold" text-anchor="middle">-2 / 3</text>
    <!-- Diagonal arrows for cross multiplication -->
    <path d="M 90,45 L 250,75" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4"/>
    <text x="90" y="105" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">(-3) × 3 = -9</text>
    <path d="M 250,45 L 90,75" stroke="#10b981" stroke-width="2" stroke-dasharray="4"/>
    <text x="250" y="105" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">(-2) × 5 = -10</text>
    <!-- Comparison conclusion -->
    <text x="170" y="135" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Since -9 &gt; -10,  -3/5 &gt; -2/3</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Using cross-multiplication, which rational number is greater: \(\\frac{-3}{5}\) or \(\\frac{-2}{3}\)?</p>
</div>""",
     ["\\(-\\frac{3}{5}\\)", "\\(-\\frac{2}{3}\\)", "Both are equal", "Cannot be determined"],
     "A", "OSC", "easy",
     "Cross products: \\((-3) \\times 3 = -9\\) and \\(5 \\times (-2) = -10\\). Since \\(-9 > -10\\), \\(-\\frac{3}{5} > -\\frac{2}{3}\\)."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Fraction Addition via Common Denominator</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Visual fraction bars -->
    <text x="170" y="25" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">Sum: (-2/3) + (3/5)</text>
    <!-- Bar 1: -10/15 -->
    <rect x="35" y="40" width="130" height="35" rx="5" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="100" y="62" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">-2/3 = -10/15</text>
    <!-- Bar 2: +9/15 -->
    <rect x="175" y="40" width="130" height="35" rx="5" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
    <text x="240" y="62" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">+3/5 = +9/15</text>
    <!-- Sum card -->
    <rect x="70" y="85" width="200" height="35" rx="5" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="170" y="107" fill="#fbbf24" font-size="13" font-weight="bold" text-anchor="middle">(-10 + 9) / 15 = -1/15</text>
    <text x="170" y="138" fill="#e2e8f0" font-size="11" text-anchor="middle">LCM(3, 5) = 15 creates a shared unit scale</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the sum of \(\\frac{-2}{3}\) and \(\\frac{3}{5}\)?</p>
</div>""",
     ["\\(-\\frac{1}{15}\\)", "\\(\\frac{1}{15}\\)", "\\(-\\frac{5}{8}\\)", "\\(\\frac{1}{8}\\)"],
     "A", "OSC", "easy",
     "LCM is 15: \\(\\frac{-10 + 9}{15} = -\\frac{1}{15}\\)."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Reciprocal Multiplication Cancellation</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Factor 1 -->
    <rect x="40" y="30" width="90" height="60" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="85" y="65" fill="#93c5fd" font-size="16" font-weight="bold" text-anchor="middle">-4 / 7</text>
    <!-- Operator -->
    <circle cx="150" cy="60" r="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="150" y="65" fill="#fbbf24" font-size="14" font-weight="bold" text-anchor="middle">×</text>
    <!-- Factor 2 (Reciprocal) -->
    <rect x="170" y="30" width="90" height="60" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="215" y="65" fill="#6ee7b7" font-size="16" font-weight="bold" text-anchor="middle">-7 / 4</text>
    <!-- Equals 1 -->
    <text x="280" y="65" fill="#f59e0b" font-size="20" font-weight="bold" text-anchor="middle">=</text>
    <text x="310" y="65" fill="#34d399" font-size="22" font-weight="bold" text-anchor="middle">1</text>
    <!-- Rule footnote -->
    <text x="170" y="125" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">(p / q) × (q / p) = 1 for any non-zero rational</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the multiplicative inverse (reciprocal) of \(-\frac{5}{9}\)?</p>
</div>""",
     ["\\(-\\frac{9}{5}\\)", "\\(\\frac{9}{5}\\)", "\\(\\frac{5}{9}\\)", "1"],
     "A", "OSC", "easy",
     "Inverting the fraction while retaining the negative sign gives \\(-\\frac{9}{5}\\), since \\(\\left(-\\frac{5}{9}\\right) \\times \\left(-\\frac{9}{5}\\right) = 1\\)."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Additive Inverse on Balanced Axis</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Number line -->
    <line x1="30" y1="80" x2="310" y2="80" stroke="#64748b" stroke-width="2.5"/>
    <!-- Center 0 -->
    <circle cx="170" cy="80" r="5" fill="#f8fafc"/>
    <text x="170" y="105" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">0</text>
    <!-- Negative value -->
    <circle cx="90" cy="80" r="5" fill="#ef4444"/>
    <text x="90" y="65" fill="#f87171" font-size="12" font-weight="bold" text-anchor="middle">-3/4</text>
    <!-- Positive value -->
    <circle cx="250" cy="80" r="5" fill="#10b981"/>
    <text x="250" y="65" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">+3/4</text>
    <!-- Distance arcs -->
    <path d="M 90,70 Q 130,45 170,70" fill="none" stroke="#f87171" stroke-dasharray="3"/>
    <path d="M 170,70 Q 210,45 250,70" fill="none" stroke="#34d399" stroke-dasharray="3"/>
    <!-- Sum card -->
    <text x="170" y="135" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">(-3/4) + (+3/4) = 0 (Additive Identity)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the additive inverse of \(-\frac{11}{17}\)?</p>
</div>""",
     ["\\(\\frac{11}{17}\\)", "\\(-\\frac{17}{11}\\)", "\\(\\frac{17}{11}\\)", "0"],
     "A", "OSC", "easy",
     "The additive inverse of \\(-x\\) is \\(+x\\), so for \\(-\\frac{11}{17}\\) it is \\(\\frac{11}{17}\\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Commutative Multiplication Grid Area</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Rectangle 1: 3 x 2 -->
    <rect x="40" y="30" width="80" height="50" rx="4" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="80" y="58" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">3/4 × 2/5</text>
    <text x="80" y="72" fill="#ffffff" font-size="10" text-anchor="middle">= 6/20 = 3/10</text>
    <!-- Equal sign -->
    <text x="170" y="60" fill="#f59e0b" font-size="22" font-weight="bold" text-anchor="middle">=</text>
    <!-- Rectangle 2: 2 x 3 -->
    <rect x="220" y="30" width="80" height="50" rx="4" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
    <text x="260" y="58" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">2/5 × 3/4</text>
    <text x="260" y="72" fill="#ffffff" font-size="10" text-anchor="middle">= 6/20 = 3/10</text>
    <!-- Banner -->
    <text x="170" y="125" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Rotating a rectangle doesn't change its area (a × b = b × a)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Which law guarantees that \(\frac{3}{4} \times \frac{2}{5} = \frac{2}{5} \times \frac{3}{4}\)?</p>
</div>""",
     ["Commutative law of multiplication", "Associative law of multiplication", "Distributive law", "Closure law"],
     "A", "OSC", "easy",
     "Commutativity of multiplication states that changing the order of factors does not alter the product."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Division Inversion Mechanism: (a/b) ÷ (c/d) = (a/b) × (d/c)</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Division problem -->
    <rect x="30" y="30" width="110" height="50" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="85" y="60" fill="#fca5a5" font-size="13" font-weight="bold" text-anchor="middle">(-3/4) ÷ (5/8)</text>
    <!-- Arrow with reciprocal flip note -->
    <path d="M 150,55 L 180,55" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="180,50 190,55 180,60" fill="#f59e0b"/>
    <text x="165" y="42" fill="#fbbf24" font-size="9" text-anchor="middle">Invert 5/8</text>
    <!-- Multiplication problem -->
    <rect x="200" y="30" width="110" height="50" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="255" y="60" fill="#6ee7b7" font-size="13" font-weight="bold" text-anchor="middle">(-3/4) × (8/5)</text>
    <!-- Final result -->
    <text x="170" y="125" fill="#fde047" font-size="13" font-weight="bold" text-anchor="middle">= -24 / 20 = -6 / 5</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the result of \(\left(-\frac{3}{4}\right) \div \frac{5}{8}\)?</p>
</div>""",
     ["\\(-\\frac{6}{5}\\)", "\\(\\frac{6}{5}\\)", "\\(-\\frac{15}{32}\\)", "\\(\\frac{15}{32}\\)"],
     "A", "OSC", "easy",
     "\\(-\\frac{3}{4} \\times \\frac{8}{5} = -\\frac{3 \\times 2}{1 \\times 5} = -\\frac{6}{5}\\)."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Fraction Cutting Word Problem</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Full 20m ribbon -->
    <rect x="30" y="35" width="280" height="25" rx="4" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="170" y="52" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Total Ribbon = 20 m</text>
    <!-- Segment A: 3 5/8 m -->
    <rect x="30" y="65" width="50" height="25" rx="3" fill="#3b82f6"/>
    <text x="55" y="82" fill="#ffffff" font-size="9" text-anchor="middle">3 5/8 m</text>
    <!-- Segment B: 8 1/4 m -->
    <rect x="85" y="65" width="115" height="25" rx="3" fill="#6366f1"/>
    <text x="142" y="82" fill="#ffffff" font-size="9" text-anchor="middle">8 1/4 m</text>
    <!-- Remaining segment -->
    <rect x="205" y="65" width="105" height="25" rx="3" fill="#10b981"/>
    <text x="257" y="82" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Left = 8 1/8 m</text>
    <!-- Calculation line -->
    <text x="170" y="125" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">20 - (29/8 + 66/8) = 160/8 - 95/8 = 65/8 = 8 1/8 m</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">A ribbon of \(20\text{ m}\) has pieces of \(3\frac{5}{8}\text{ m}\) and \(8\frac{1}{4}\text{ m}\) cut from it. What is the length remaining?</p>
</div>""",
     ["\\(8\\frac{1}{8}\\text{ m}\\)",
      "\\(8\\frac{3}{8}\\text{ m}\\)",
      "\\(7\\frac{7}{8}\\text{ m}\\)",
      "\\(9\\frac{1}{8}\\text{ m}\\)"],
     "A", "OSC", "easy",
     "Total cut = \\(\\frac{29}{8} + \\frac{66}{8} = \\frac{95}{8}\\). Remaining = \\(\\frac{160 - 95}{8} = \\frac{65}{8} = 8\\frac{1}{8}\\text{ m}\\)."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Density Property: Infinite Fractions Between Any Two</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Number line segment from 0 to 1 -->
    <line x1="40" y1="75" x2="300" y2="75" stroke="#64748b" stroke-width="3"/>
    <!-- Point 0 -->
    <circle cx="50" cy="75" r="5" fill="#f8fafc"/>
    <text x="50" y="95" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">0</text>
    <!-- Point 1 -->
    <circle cx="290" cy="75" r="5" fill="#f8fafc"/>
    <text x="290" y="95" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">1</text>
    <!-- Subdivisions 1/4, 1/2, 3/4 -->
    <circle cx="110" cy="75" r="4" fill="#38bdf8"/>
    <text x="110" y="60" fill="#38bdf8" font-size="10" text-anchor="middle">1/4</text>
    <circle cx="170" cy="75" r="4" fill="#10b981"/>
    <text x="170" y="60" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">1/2</text>
    <circle cx="230" cy="75" r="4" fill="#38bdf8"/>
    <text x="230" y="60" fill="#38bdf8" font-size="10" text-anchor="middle">3/4</text>
    <!-- Micro divisions dots -->
    <text x="140" y="79" fill="#fbbf24" font-size="12" text-anchor="middle">•••</text>
    <text x="200" y="79" fill="#fbbf24" font-size="12" text-anchor="middle">•••</text>
    <!-- Footnote -->
    <text x="170" y="130" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Between ANY two rational numbers lie infinitely many rational numbers</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">How many rational numbers exist between \(0\) and \(1\)?</p>
</div>""",
     ["Infinitely many", "Exactly 9", "Exactly 99", "Only 1 (namely 1/2)"],
     "A", "OSC", "easy",
     "By the density property of rational numbers, between any two distinct rational numbers there exist infinitely many other rational numbers.")
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch3_topic1.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
