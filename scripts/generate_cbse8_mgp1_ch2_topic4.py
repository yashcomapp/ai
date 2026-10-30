# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-2-2.4
Topic: Comparison & Arithmetic with Exponential Quantities
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-2-2.4"

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
    ("What is the essential first step before adding or subtracting two numbers expressed in scientific notation?",
     ["Convert both numbers to have the exact same power of 10",
      "Multiply the two exponents together",
      "Add the exponents directly",
      "Convert the coefficients to whole integers"],
     "A", "OSC", "easy",
     "Before adding or subtracting numbers in scientific notation, they must be converted to share a common power of 10 so that the distributive property \\(A \\times 10^n + B \\times 10^n = (A + B) \\times 10^n\\) can be applied."),

    # 2
    ("The mass of the Earth is \\(5.97 \\times 10^{24}\\text{ kg}\\) and the mass of the Moon is \\(7.35 \\times 10^{22}\\text{ kg}\\). What is their combined mass in standard form?",
     ["\\(6.0435 \\times 10^{24}\\text{ kg}\\)",
      "\\(13.32 \\times 10^{24}\\text{ kg}\\)",
      "\\(6.0435 \\times 10^{22}\\text{ kg}\\)",
      "\\(1.332 \\times 10^{23}\\text{ kg}\\)"],
     "A", "OSC", "medium",
     "Convert the Moon's mass to exponent 24: \\(7.35 \\times 10^{22} = 0.0735 \\times 10^{24}\\). Adding: \\((5.97 + 0.0735) \\times 10^{24} = 6.0435 \\times 10^{24}\\text{ kg}\\)."),

    # 3
    ("What is the difference between the mass of the Earth (\\(5.97 \\times 10^{24}\\text{ kg}\\)) and the Moon (\\(7.35 \\times 10^{22}\\text{ kg}\\))?",
     ["\\(5.8965 \\times 10^{24}\\text{ kg}\\)",
      "\\(5.8965 \\times 10^{22}\\text{ kg}\\)",
      "\\(5.235 \\times 10^{24}\\text{ kg}\\)",
      "\\(1.38 \\times 10^{24}\\text{ kg}\\)"],
     "A", "OSC", "medium",
     "\\((5.97 - 0.0735) \\times 10^{24} = 5.8965 \\times 10^{24}\\text{ kg}\\)."),

    # 4
    ("The diameter of the Sun is \\(1.4 \\times 10^9\\text{ m}\\) and the diameter of the Earth is \\(1.2756 \\times 10^7\\text{ m}\\). Approximately how many times larger is the Sun's diameter than Earth's?",
     ["About 110 times", "About 10 times", "About 1000 times", "About 50 times"],
     "A", "OSC", "medium",
     "\\(\\frac{1.4 \\times 10^9}{1.2756 \\times 10^7} = \\frac{1.4}{1.2756} \\times 10^2 \\approx 1.0975 \\times 100 \\approx 110\\) times."),

    # 5
    ("The distance from Earth to the Sun is \\(1.496 \\times 10^{11}\\text{ m}\\), and the distance from Earth to the Moon is \\(3.84 \\times 10^8\\text{ m}\\). During a solar eclipse when the Moon comes directly between Earth and the Sun, what is the distance from the Moon to the Sun?",
     ["\\(1.49216 \\times 10^{11}\\text{ m}\\)",
      "\\(1.112 \\times 10^{11}\\text{ m}\\)",
      "\\(1.49216 \\times 10^8\\text{ m}\\)",
      "\\(1.4576 \\times 10^{11}\\text{ m}\\)"],
     "A", "OSC", "hard",
     "Subtract: \\(1.496 \\times 10^{11} - 0.00384 \\times 10^{11} = (1.496 - 0.00384) \\times 10^{11} = 1.49216 \\times 10^{11}\\text{ m}\\)."),

    # 6
    ("The size of a plant cell is \\(1.275 \\times 10^{-5}\\text{ m}\\) and that of a red blood cell is \\(7.0 \\times 10^{-6}\\text{ m}\\). What is the ratio of the size of the plant cell to the red blood cell?",
     ["Approximately 1.8 : 1", "Approximately 1 : 2", "Approximately 18 : 1", "Approximately 1 : 18"],
     "A", "OSC", "medium",
     "Rewrite plant cell size: \\(1.275 \\times 10^{-5} = 12.75 \\times 10^{-6}\\text{ m}\\). Ratio = \\(\\frac{12.75 \\times 10^{-6}}{7.0 \\times 10^{-6}} = \\frac{12.75}{7.0} \\approx 1.82\\), so about 1.8 times."),

    # 7
    ("The mass of Jupiter is \\(1.9 \\times 10^{27}\\text{ kg}\\) and Earth is \\(5.97 \\times 10^{24}\\text{ kg}\\). About how many Earths would equal the mass of Jupiter?",
     ["About 318 Earths", "About 32 Earths", "About 3180 Earths", "About 190 Earths"],
     "A", "OSC", "medium",
     "\\(\\frac{1.9 \\times 10^{27}}{5.97 \\times 10^{24}} = \\frac{1900 \\times 10^{24}}{5.97 \\times 10^{24}} = \\frac{1900}{5.97} \\approx 318.2\\). Thus Jupiter is about 318 times as massive as Earth."),

    # 8
    ("Light travels at \\(3.0 \\times 10^8\\text{ m/s}\\). How far does light travel in \\(500\\text{ seconds}\\) (the time to reach Earth from Sun)?",
     ["\\(1.5 \\times 10^{11}\\text{ m}\\)",
      "\\(1.5 \\times 10^{10}\\text{ m}\\)",
      "\\(1.5 \\times 10^9\\text{ m}\\)",
      "\\(15 \\times 10^{11}\\text{ m}\\)"],
     "A", "OSC", "easy",
     "\\(\\text{Distance} = \\text{Speed} \\times \\text{Time} = (3.0 \\times 10^8) \\times 500 = 1500 \\times 10^8 = 1.5 \\times 10^{11}\\text{ m}\\)."),

    # 9
    ("Evaluate: \\((6.5 \\times 10^7) + (2.8 \\times 10^8)\\) in standard form.",
     ["\\(3.45 \\times 10^8\\)", "\\(9.3 \\times 10^8\\)", "\\(9.3 \\times 10^{15}\\)", "\\(3.45 \\times 10^7\\)"],
     "A", "OSC", "medium",
     "\\(6.5 \\times 10^7 = 0.65 \\times 10^8\\). Sum = \\((0.65 + 2.8) \\times 10^8 = 3.45 \\times 10^8\\)."),

    # 10
    ("Evaluate: \\((8.4 \\times 10^{-4}) - (2.1 \\times 10^{-5})\\) in standard form.",
     ["\\(8.19 \\times 10^{-4}\\)", "\\(6.3 \\times 10^{-4}\\)", "\\(6.3 \\times 10^{-5}\\)", "\\(8.19 \\times 10^{-5}\\)"],
     "A", "OSC", "medium",
     "\\(2.1 \\times 10^{-5} = 0.21 \\times 10^{-4}\\). Difference = \\((8.4 - 0.21) \\times 10^{-4} = 8.19 \\times 10^{-4}\\)."),

    # 11
    ("Find the product: \\((4.2 \\times 10^{-3}) \\times (3.0 \\times 10^{-5})\\) in scientific notation.",
     ["\\(1.26 \\times 10^{-7}\\)", "\\(1.26 \\times 10^{-8}\\)", "\\(12.6 \\times 10^{-8}\\)", "\\(1.26 \\times 10^{-15}\\)"],
     "A", "OSC", "medium",
     "\\(4.2 \\times 3.0 = 12.6\\). Powers: \\(10^{-3 + (-5)} = 10^{-8}\\). Standard form: \\(12.6 \\times 10^{-8} = 1.26 \\times 10^{-7}\\)."),

    # 12
    ("Divide \\((9.6 \\times 10^6)\\) by \\((3.2 \\times 10^{-2})\\) in standard form.",
     ["\\(3.0 \\times 10^8\\)", "\\(3.0 \\times 10^4\\)", "\\(3.0 \\times 10^{-8}\\)", "\\(0.3 \\times 10^9\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{9.6}{3.2} = 3.0\\). Powers: \\(10^{6 - (-2)} = 10^8\\). Result: \\(3.0 \\times 10^8\\)."),

    # 13
    ("A container holds \\(4.8 \\times 10^4\\text{ g}\\) of chemical A and \\(7.2 \\times 10^3\\text{ g}\\) of chemical B. What is the total mass of the mixture?",
     ["\\(5.52 \\times 10^4\\text{ g}\\)",
      "\\(1.2 \\times 10^5\\text{ g}\\)",
      "\\(5.52 \\times 10^3\\text{ g}\\)",
      "\\(1.2 \\times 10^4\\text{ g}\\)"],
     "A", "OSC", "medium",
     "\\(7.2 \\times 10^3 = 0.72 \\times 10^4\\). Total = \\((4.8 + 0.72) \\times 10^4 = 5.52 \\times 10^4\\text{ g}\\)."),

    # 14
    ("The thickness of 500 sheets of paper is \\(4.5\\text{ cm}\\). What is the thickness of 1 sheet in standard form?",
     ["\\(9.0 \\times 10^{-3}\\text{ cm}\\)",
      "\\(9.0 \\times 10^{-2}\\text{ cm}\\)",
      "\\(9.0 \\times 10^{-4}\\text{ cm}\\)",
      "\\(0.9 \\times 10^{-3}\\text{ cm}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{4.5}{500} = \\frac{4.5}{5 \\times 10^2} = 0.9 \\times 10^{-2} = 9.0 \\times 10^{-3}\\text{ cm}\\)."),

    # 15
    ("A wire has a radius of \\(2.0 \\times 10^{-4}\\text{ m}\\). What is its cross-sectional area (using \\(\\pi \\approx 3.14\\)) in standard form?",
     ["\\(1.256 \\times 10^{-7}\\text{ m}^2\\)",
      "\\(1.256 \\times 10^{-8}\\text{ m}^2\\)",
      "\\(1.256 \\times 10^{-6}\\text{ m}^2\\)",
      "\\(6.28 \\times 10^{-8}\\text{ m}^2\\)"],
     "A", "OSC", "hard",
     "Area \\(A = \\pi r^2 = 3.14 \\times (2.0 \\times 10^{-4})^2 = 3.14 \\times 4.0 \\times 10^{-8} = 12.56 \\times 10^{-8} = 1.256 \\times 10^{-7}\\text{ m}^2\\)."),

    # 16
    ("A microscopic organism doubles in population every hour. If the initial population is \\(2.5 \\times 10^3\\), what is the population after 3 hours?",
     ["\\(2.0 \\times 10^4\\)", "\\(7.5 \\times 10^3\\)", "\\(1.0 \\times 10^4\\)", "\\(2.0 \\times 10^3\\)"],
     "A", "OSC", "medium",
     "After 3 doublings, population is multiplied by \\(2^3 = 8\\): \\(2.5 \\times 10^3 \\times 8 = 20.0 \\times 10^3 = 2.0 \\times 10^4\\)."),

    # 17
    ("Compare \\(A = 4.5 \\times 10^{-7}\\) and \\(B = 8.9 \\times 10^{-8}\\). Which statement is correct?",
     ["\\(A > B\\)", "\\(B > A\\)", "\\(A = B\\)", "Cannot be compared"],
     "A", "OSC", "easy",
     "\\(A = 45 \\times 10^{-8}\\) while \\(B = 8.9 \\times 10^{-8}\\). Since \\(45 > 8.9\\), \\(A > B\\) (approximately 5 times larger)."),

    # 18
    ("How many red blood cells of diameter \\(7 \\times 10^{-6}\\text{ m}\\) placed end-to-end would stretch along a length of \\(1.4\\text{ m}\\)?",
     ["\\(2.0 \\times 10^5\\)", "\\(2.0 \\times 10^6\\)", "\\(2.0 \\times 10^4\\)", "\\(5.0 \\times 10^5\\)"],
     "A", "OSC", "medium",
     "Number of cells = \\(\\frac{1.4}{7 \\times 10^{-6}} = \\frac{1.4}{7} \\times 10^6 = 0.2 \\times 10^6 = 2.0 \\times 10^5\\) (200,000 cells)."),

    # 19
    ("The total energy consumed by a city in a year is \\(7.2 \\times 10^{15}\\text{ Joules}\\). If there are \\(3.0 \\times 10^7\\text{ seconds}\\) in a year, what is the average power consumption in Watts (Joules/sec)?",
     ["\\(2.4 \\times 10^8\\text{ W}\\)",
      "\\(2.4 \\times 10^7\\text{ W}\\)",
      "\\(2.4 \\times 10^9\\text{ W}\\)",
      "\\(2.16 \\times 10^{23}\\text{ W}\\)"],
     "A", "OSC", "medium",
     "Power = \\(\\frac{7.2 \\times 10^{15}}{3.0 \\times 10^7} = \\frac{7.2}{3.0} \\times 10^{15 - 7} = 2.4 \\times 10^8\\text{ Watts}\\)."),

    # 20
    ("A spaceship travels at \\(2.5 \\times 10^4\\text{ m/s}\\). How long (in seconds) does it take to travel a distance of \\(1.5 \\times 10^9\\text{ m}\\)?",
     ["\\(6.0 \\times 10^4\\text{ s}\\)",
      "\\(6.0 \\times 10^3\\text{ s}\\)",
      "\\(6.0 \\times 10^5\\text{ s}\\)",
      "\\(3.75 \\times 10^{13}\\text{ s}\\)"],
     "A", "OSC", "medium",
     "Time = \\(\\frac{\\text{Distance}}{\\text{Speed}} = \\frac{1.5 \\times 10^9}{2.5 \\times 10^4} = 0.6 \\times 10^5 = 6.0 \\times 10^4\\text{ seconds}\\) (about 16.7 hours)."),

    # 21
    ("Find the value of \\((3.0 \\times 10^{-4})^2\\) in standard form.",
     ["\\(9.0 \\times 10^{-8}\\)", "\\(9.0 \\times 10^{-6}\\)", "\\(9.0 \\times 10^{-16}\\)", "\\(6.0 \\times 10^{-8}\\)"],
     "A", "OSC", "easy",
     "\\(3.0^2 = 9.0\\) and \\((10^{-4})^2 = 10^{-8}\\). Result: \\(9.0 \\times 10^{-8}\\)."),

    # 22
    ("Find the value of \\((2.0 \\times 10^3)^3\\) in standard form.",
     ["\\(8.0 \\times 10^9\\)", "\\(8.0 \\times 10^6\\)", "\\(6.0 \\times 10^9\\)", "\\(8.0 \\times 10^{27}\\)"],
     "A", "OSC", "easy",
     "\\(2.0^3 = 8.0\\) and \\((10^3)^3 = 10^9\\). Result: \\(8.0 \\times 10^9\\)."),

    # 23
    ("Evaluate \\(\\sqrt{1.44 \\times 10^{-6}}\\) in standard form.",
     ["\\(1.2 \\times 10^{-3}\\)", "\\(1.2 \\times 10^{-6}\\)", "\\(1.2 \\times 10^{-2}\\)", "\\(12 \\times 10^{-4}\\)"],
     "A", "OSC", "medium",
     "\\(\\sqrt{1.44} = 1.2\\) and \\(\\sqrt{10^{-6}} = (10^{-6})^{1/2} = 10^{-3}\\). Result is \\(1.2 \\times 10^{-3}\\)."),

    # 24
    ("Evaluate \\(\\sqrt[3]{8.0 \\times 10^{-9}}\\) in standard form.",
     ["\\(2.0 \\times 10^{-3}\\)", "\\(2.0 \\times 10^{-9}\\)", "\\(2.0 \\times 10^{-6}\\)", "\\(4.0 \\times 10^{-3}\\)"],
     "A", "OSC", "medium",
     "\\(\\sqrt[3]{8.0} = 2.0\\) and \\((10^{-9})^{1/3} = 10^{-3}\\). Standard form: \\(2.0 \\times 10^{-3}\\)."),

    # 25
    ("Evaluate \\(\\frac{(1.8 \\times 10^5) \\times (4.0 \\times 10^{-2})}{1.2 \\times 10^2}\\) in standard form.",
     ["\\(6.0 \\times 10^1\\)", "\\(6.0 \\times 10^2\\)", "\\(6.0 \\times 10^0\\)", "\\(6.0 \\times 10^{-1}\\)"],
     "A", "OSC", "medium",
     "Numerator: \\(1.8 \\times 4.0 = 7.2\\), powers: \\(10^{5 + (-2)} = 10^3\\). Dividing by \\(1.2 \\times 10^2\\): \\(\\frac{7.2}{1.2} = 6.0\\), powers: \\(10^{3 - 2} = 10^1 = 60\\). Standard form: \\(6.0 \\times 10^1\\)."),

    # 26
    ("Add \\(1.5 \\times 10^{-7}\\) and \\(8.5 \\times 10^{-8}\\) in standard form.",
     ["\\(2.35 \\times 10^{-7}\\)", "\\(1.0 \\times 10^{-7}\\)", "\\(10.0 \\times 10^{-8}\\)", "\\(2.35 \\times 10^{-8}\\)"],
     "A", "OSC", "medium",
     "\\(8.5 \\times 10^{-8} = 0.85 \\times 10^{-7}\\). Sum: \\((1.5 + 0.85) \\times 10^{-7} = 2.35 \\times 10^{-7}\\)."),

    # 27
    ("Subtract \\(9.0 \\times 10^4\\) from \\(1.2 \\times 10^6\\) in standard form.",
     ["\\(1.11 \\times 10^6\\)", "\\(3.0 \\times 10^5\\)", "\\(1.11 \\times 10^5\\)", "\\(2.1 \\times 10^6\\)"],
     "A", "OSC", "medium",
     "\\(9.0 \\times 10^4 = 0.09 \\times 10^6\\). Difference: \\((1.2 - 0.09) \\times 10^6 = 1.11 \\times 10^6\\)."),

    # 28
    ("The mass of a water molecule is approximately \\(3.0 \\times 10^{-26}\\text{ kg}\\). How many water molecules are in \\(1.5\\text{ kg}\\) of water?",
     ["\\(5.0 \\times 10^{25}\\)", "\\(5.0 \\times 10^{26}\\)", "\\(4.5 \\times 10^{-26}\\)", "\\(2.0 \\times 10^{25}\\)"],
     "A", "OSC", "medium",
     "Number of molecules = \\(\\frac{1.5}{3.0 \\times 10^{-26}} = 0.5 \\times 10^{26} = 5.0 \\times 10^{25}\\)."),

    # 29
    ("The population of Country A is \\(1.4 \\times 10^9\\) and Country B is \\(3.5 \\times 10^8\\). How many times larger is the population of Country A than Country B?",
     ["4 times", "2.5 times", "5 times", "40 times"],
     "A", "OSC", "easy",
     "\\(\\frac{1.4 \\times 10^9}{3.5 \\times 10^8} = \\frac{14 \\times 10^8}{3.5 \\times 10^8} = \\frac{14}{3.5} = 4\\) times."),

    # 30
    ("If \\(x = 2.0 \\times 10^{-3}\\) and \\(y = 4.0 \\times 10^{-4}\\), what is \\(\\frac{x + y}{x - y}\\)?",
     ["1.5", "2", "3", "1.25"],
     "A", "OSC", "hard",
     "\\(x = 2.0 \\times 10^{-3} = 20 \\times 10^{-4}\\). Then \\(x + y = (20 + 4) \\times 10^{-4} = 24 \\times 10^{-4}\\), and \\(x - y = (20 - 4) \\times 10^{-4} = 16 \\times 10^{-4}\\). The ratio is \\(\\frac{24 \\times 10^{-4}}{16 \\times 10^{-4}} = \\frac{24}{16} = 1.5\\)."),

    # 31
    ("A rectangular field has length \\(2.5 \\times 10^3\\text{ m}\\) and breadth \\(1.6 \\times 10^2\\text{ m}\\). What is its perimeter in standard form?",
     ["\\(5.32 \\times 10^3\\text{ m}\\)",
      "\\(4.1 \\times 10^3\\text{ m}\\)",
      "\\(4.0 \\times 10^5\\text{ m}\\)",
      "\\(2.66 \\times 10^3\\text{ m}\\)"],
     "A", "OSC", "medium",
     "Perimeter = \\(2 \\times (L + B)\\). Convert breadth: \\(1.6 \\times 10^2 = 0.16 \\times 10^3\\). \\(L + B = 2.5 + 0.16 = 2.66 \\times 10^3\\). Multiplying by 2: \\(2 \\times 2.66 \\times 10^3 = 5.32 \\times 10^3\\text{ m}\\)."),

    # 32
    ("What is the area of the rectangular field from question 31 in standard form?",
     ["\\(4.0 \\times 10^5\\text{ m}^2\\)",
      "\\(4.0 \\times 10^6\\text{ m}^2\\)",
      "\\(4.0 \\times 10^4\\text{ m}^2\\)",
      "\\(4.1 \\times 10^5\\text{ m}^2\\)"],
     "A", "OSC", "easy",
     "Area = \\(L \\times B = (2.5 \\times 10^3) \\times (1.6 \\times 10^2) = (2.5 \\times 1.6) \\times 10^{3+2} = 4.0 \\times 10^5\\text{ m}^2\\)."),

    # 33
    ("Express the ratio of \\(4.8 \\times 10^{-5}\\) to \\(1.2 \\times 10^{-7}\\) in standard form.",
     ["\\(4.0 \\times 10^2\\)", "\\(4.0 \\times 10^{-12}\\)", "\\(4.0 \\times 10^{-2}\\)", "\\(0.4 \\times 10^3\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{4.8 \\times 10^{-5}}{1.2 \\times 10^{-7}} = 4.0 \\times 10^{-5 - (-7)} = 4.0 \\times 10^2 = 400\\)."),

    # 34
    ("Assertion (A): To add \\(2.4 \\times 10^5\\) and \\(3.6 \\times 10^4\\), we can rewrite \\(3.6 \\times 10^4\\) as \\(0.36 \\times 10^5\\).\nReason (R): Addition of numbers in scientific notation requires matching the powers of 10 to use the distributive property.",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "Rewriting to identical power \\(10^5\\) allows factoring out \\(10^5\\), making (R) the exact mathematical justification for (A)."),

    # 35
    ("Assertion (A): \\((2 \\times 10^3) + (3 \\times 10^2) = 5 \\times 10^5\\).\nReason (R): When adding exponential quantities, we add the exponents.",
     ["Both (A) and (R) are false",
      "Both (A) and (R) are true",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "Both are false: exponents are never added during addition. The correct sum is \\(2000 + 300 = 2300 = 2.3 \\times 10^3\\)."),

    # 36
    ("True or False: In scientific notation, \\(10^a \\times 10^b = 10^{a+b}\\) regardless of whether \\(a\\) and \\(b\\) are positive or negative.",
     ["True", "False"],
     "A", "OTF", "easy",
     "The product rule for powers applies universally to all real/integer exponents."),

    # 37
    ("True or False: If \\(A = 3.2 \\times 10^4\\) and \\(B = 1.6 \\times 10^4\\), then \\(A - B = 1.6 \\times 10^4\\).",
     ["True", "False"],
     "A", "OTF", "easy",
     "Since exponents match: \\((3.2 - 1.6) \\times 10^4 = 1.6 \\times 10^4\\)."),

    # 38
    ("Fill in the blank: To compare two numbers in standard form with different powers of 10, the number with the _____ exponent of 10 is always the greater number.",
     ["larger", "smaller", "negative", "even"],
     "A", "OFB", "easy",
     "Because coefficients are bounded between 1 and 10, the quantity with the strictly greater exponent is always larger."),

    # 39
    ("Fill in the blank: The value of \\((4.0 \\times 10^6) \\div (8.0 \\times 10^2)\\) in standard form is _____ \\(\\times 10^3\\).",
     ["5.0", "0.5", "50", "2.0"],
     "A", "OFB", "easy",
     "\\(4.0 / 8.0 = 0.5\\). Powers: \\(10^{6-2} = 10^4\\). Normalising gives \\(0.5 \\times 10^4 = 5.0 \\times 10^3\\)."),

    # 40
    ("What is the numerical integer ratio of \\(6.0 \\times 10^8\\) to \\(1.5 \\times 10^8\\)?",
     ["4", "40", "0.4", "2"],
     "A", "ONE", "easy",
     "\\(\\frac{6.0 \\times 10^8}{1.5 \\times 10^8} = \\frac{6.0}{1.5} = 4\\)."),
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    ("Add: \\((3.2 \\times 10^5) + (4.8 \\times 10^5)\\) in standard form.",
     ["\\(8.0 \\times 10^5\\)", "\\(8.0 \\times 10^{10}\\)", "\\(8.0 \\times 10^6\\)", "\\(1.5 \\times 10^5\\)"],
     "A", "OSC", "easy",
     "Exponents match: \\((3.2 + 4.8) \\times 10^5 = 8.0 \\times 10^5\\)."),

    # 42
    ("Subtract: \\((7.5 \\times 10^{-3}) - (3.2 \\times 10^{-3})\\) in standard form.",
     ["\\(4.3 \\times 10^{-3}\\)", "\\(4.3 \\times 10^{-6}\\)", "\\(4.3 \\times 10^0\\)", "\\(1.07 \\times 10^{-3}\\)"],
     "A", "OSC", "easy",
     "Exponents match: \\((7.5 - 3.2) \\times 10^{-3} = 4.3 \\times 10^{-3}\\)."),

    # 43
    ("Add: \\((1.8 \\times 10^4) + (2.2 \\times 10^3)\\) in standard form.",
     ["\\(2.02 \\times 10^4\\)", "\\(4.0 \\times 10^7\\)", "\\(4.0 \\times 10^4\\)", "\\(2.02 \\times 10^3\\)"],
     "A", "OSC", "medium",
     "\\(2.2 \\times 10^3 = 0.22 \\times 10^4\\). Sum: \\((1.8 + 0.22) \\times 10^4 = 2.02 \\times 10^4\\)."),

    # 44
    ("Subtract: \\((5.6 \\times 10^{-5}) - (4.0 \\times 10^{-6})\\) in standard form.",
     ["\\(5.2 \\times 10^{-5}\\)", "\\(1.6 \\times 10^{-5}\\)", "\\(5.2 \\times 10^{-6}\\)", "\\(1.6 \\times 10^{-11}\\)"],
     "A", "OSC", "medium",
     "\\(4.0 \\times 10^{-6} = 0.4 \\times 10^{-5}\\). Difference: \\((5.6 - 0.4) \\times 10^{-5} = 5.2 \\times 10^{-5}\\)."),

    # 45
    ("Evaluate: \\((2.5 \\times 10^6) \\times (6.0 \\times 10^{-2})\\) in standard form.",
     ["\\(1.5 \\times 10^5\\)", "\\(15.0 \\times 10^4\\)", "\\(1.5 \\times 10^4\\)", "\\(1.5 \\times 10^8\\)"],
     "A", "OSC", "medium",
     "\\(2.5 \\times 6.0 = 15.0\\). Powers: \\(10^{6 - 2} = 10^4\\). Normalising gives \\(1.5 \\times 10^5\\)."),

    # 46
    ("Evaluate: \\((1.44 \\times 10^8) \\div (1.2 \\times 10^3)\\) in standard form.",
     ["\\(1.2 \\times 10^5\\)", "\\(1.2 \\times 10^{11}\\)", "\\(1.2 \\times 10^4\\)", "\\(12 \\times 10^4\\)"],
     "A", "OSC", "easy",
     "\\(1.44 / 1.2 = 1.2\\). Powers: \\(10^{8 - 3} = 10^5\\). Result: \\(1.2 \\times 10^5\\)."),

    # 47
    ("Evaluate: \\((2.0 \\times 10^{-4}) \\times (4.5 \\times 10^{-3})\\) in standard form.",
     ["\\(9.0 \\times 10^{-7}\\)", "\\(9.0 \\times 10^{-12}\\)", "\\(9.0 \\times 10^{-6}\\)", "\\(0.9 \\times 10^{-6}\\)"],
     "A", "OSC", "easy",
     "\\(2.0 \\times 4.5 = 9.0\\). Powers: \\(10^{-4 + (-3)} = 10^{-7}\\). Result: \\(9.0 \\times 10^{-7}\\)."),

    # 48
    ("Evaluate: \\((8.0 \\times 10^{-6}) \\div (2.5 \\times 10^{-2})\\) in standard form.",
     ["\\(3.2 \\times 10^{-4}\\)", "\\(3.2 \\times 10^{-8}\\)", "\\(3.2 \\times 10^{-5}\\)", "\\(0.32 \\times 10^{-3}\\)"],
     "A", "OSC", "medium",
     "\\(8.0 / 2.5 = 3.2\\). Powers: \\(10^{-6 - (-2)} = 10^{-4}\\). Result: \\(3.2 \\times 10^{-4}\\)."),

    # 49
    ("The total surface area of a cube of edge \\(3.0 \\times 10^{-2}\\text{ m}\\) is:",
     ["\\(5.4 \\times 10^{-3}\\text{ m}^2\\)",
      "\\(5.4 \\times 10^{-4}\\text{ m}^2\\)",
      "\\(2.7 \\times 10^{-5}\\text{ m}^2\\)",
      "\\(9.0 \\times 10^{-4}\\text{ m}^2\\)"],
     "A", "OSC", "medium",
     "Surface area = \\(6s^2 = 6 \\times (3.0 \\times 10^{-2})^2 = 6 \\times 9.0 \\times 10^{-4} = 54 \\times 10^{-4} = 5.4 \\times 10^{-3}\\text{ m}^2\\)."),

    # 50
    ("The volume of a cube of edge \\(2.0 \\times 10^{-3}\\text{ m}\\) is:",
     ["\\(8.0 \\times 10^{-9}\\text{ m}^3\\)",
      "\\(8.0 \\times 10^{-6}\\text{ m}^3\\)",
      "\\(6.0 \\times 10^{-9}\\text{ m}^3\\)",
      "\\(8.0 \\times 10^{-27}\\text{ m}^3\\)"],
     "A", "OSC", "easy",
     "Volume = \\(s^3 = (2.0 \\times 10^{-3})^3 = 8.0 \\times 10^{-9}\\text{ m}^3\\)."),

    # 51
    ("If \\(3.6 \\times 10^8\\text{ Joules}\\) of work is done in \\(1.2 \\times 10^4\\text{ seconds}\\), what is the power output?",
     ["\\(3.0 \\times 10^4\\text{ W}\\)",
      "\\(3.0 \\times 10^3\\text{ W}\\)",
      "\\(4.32 \\times 10^{12}\\text{ W}\\)",
      "\\(3.0 \\times 10^5\\text{ W}\\)"],
     "A", "OSC", "easy",
     "Power = \\(\\frac{3.6 \\times 10^8}{1.2 \\times 10^4} = 3.0 \\times 10^4\\text{ Watts}\\)."),

    # 52
    ("A printer prints \\(4.0 \\times 10^2\\) pages per hour. How many pages does it print in \\(2.5 \\times 10^1\\) hours?",
     ["\\(1.0 \\times 10^4\\)", "\\(1.0 \\times 10^3\\)", "\\(1.0 \\times 10^5\\)", "\\(6.5 \\times 10^3\\)"],
     "A", "OSC", "easy",
     "\\(4.0 \\times 10^2 \\times 2.5 \\times 10^1 = 10.0 \\times 10^3 = 1.0 \\times 10^4\\) (10,000 pages)."),

    # 53
    ("Express \\(\\frac{1}{2.0 \\times 10^{-5}}\\) in standard form.",
     ["\\(5.0 \\times 10^4\\)", "\\(5.0 \\times 10^5\\)", "\\(0.5 \\times 10^5\\)", "\\(2.0 \\times 10^5\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{1}{2.0} \\times 10^5 = 0.5 \\times 10^5 = 5.0 \\times 10^4\\)."),

    # 54
    ("Express \\(\\frac{1}{4.0 \\times 10^8}\\) in standard form.",
     ["\\(2.5 \\times 10^{-9}\\)", "\\(2.5 \\times 10^{-8}\\)", "\\(0.25 \\times 10^{-8}\\)", "\\(4.0 \\times 10^{-8}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{1}{4.0} \\times 10^{-8} = 0.25 \\times 10^{-8} = 2.5 \\times 10^{-9}\\)."),

    # 55
    ("Add: \\((7.2 \\times 10^{-4}) + (2.8 \\times 10^{-4})\\) in standard form.",
     ["\\(1.0 \\times 10^{-3}\\)", "\\(10.0 \\times 10^{-4}\\)", "\\(1.0 \\times 10^{-4}\\)", "\\(1.0 \\times 10^{-5}\\)"],
     "A", "OSC", "medium",
     "\\((7.2 + 2.8) \\times 10^{-4} = 10.0 \\times 10^{-4} = 1.0 \\times 10^{-3}\\)."),

    # 56
    ("Subtract: \\((1.0 \\times 10^{-2}) - (1.0 \\times 10^{-3})\\) in standard form.",
     ["\\(9.0 \\times 10^{-3}\\)", "\\(0\\)", "\\(9.0 \\times 10^{-2}\\)", "\\(1.0 \\times 10^{-3}\\)"],
     "A", "OSC", "medium",
     "\\(1.0 \\times 10^{-2} = 10 \\times 10^{-3}\\). Difference: \\((10 - 1) \\times 10^{-3} = 9.0 \\times 10^{-3}\\)."),

    # 57
    ("Evaluate: \\((1.5 \\times 10^3) \\times (4.0 \\times 10^2) \\div (2.0 \\times 10^4)\\) in standard form.",
     ["\\(3.0 \\times 10^1\\)", "\\(3.0 \\times 10^2\\)", "\\(3.0 \\times 10^0\\)", "\\(6.0 \\times 10^1\\)"],
     "A", "OSC", "medium",
     "Numerator = \\(6.0 \\times 10^5\\). Dividing by \\(2.0 \\times 10^4\\) gives \\(3.0 \\times 10^1 = 30\\)."),

    # 58
    ("The mass of atom X is \\(4.8 \\times 10^{-26}\\text{ kg}\\) and atom Y is \\(1.6 \\times 10^{-26}\\text{ kg}\\). What is the mass ratio of X to Y?",
     ["3", "30", "0.33", "4"],
     "A", "OSC", "easy",
     "\\(\\frac{4.8 \\times 10^{-26}}{1.6 \\times 10^{-26}} = \\frac{4.8}{1.6} = 3\\)."),

    # 59
    ("What is the average of \\(4.0 \\times 10^5\\) and \\(6.0 \\times 10^5\\)?",
     ["\\(5.0 \\times 10^5\\)", "\\(5.0 \\times 10^{10}\\)", "\\(1.0 \\times 10^6\\)", "\\(5.0 \\times 10^6\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{(4.0 + 6.0) \\times 10^5}{2} = \\frac{10.0 \\times 10^5}{2} = 5.0 \\times 10^5\\)."),

    # 60
    ("What is the geometric mean \\(\\sqrt{A \\times B}\\) of \\(A = 2.0 \\times 10^3\\) and \\(B = 8.0 \\times 10^7\\)?",
     ["\\(4.0 \\times 10^5\\)", "\\(4.0 \\times 10^4\\)", "\\(1.6 \\times 10^5\\)", "\\(4.0 \\times 10^6\\)"],
     "A", "OSC", "medium",
     "\\(A \\times B = 16.0 \\times 10^{10} = 1.6 \\times 10^{11} = 16 \\times 10^{10}\\). \\(\\sqrt{16 \\times 10^{10}} = 4.0 \\times 10^5\\)."),

    # 61
    ("If \\(m = 1.2 \\times 10^{-3}\\), what is \\(m^2\\)?",
     ["\\(1.44 \\times 10^{-6}\\)", "\\(1.44 \\times 10^{-5}\\)", "\\(1.44 \\times 10^{-9}\\)", "\\(2.4 \\times 10^{-6}\\)"],
     "A", "OSC", "easy",
     "\\(1.2^2 = 1.44\\) and \\((10^{-3})^2 = 10^{-6}\\). Result: \\(1.44 \\times 10^{-6}\\)."),

    # 62
    ("If \\(k = 5.0 \\times 10^4\\), what is \\(2k + 3k\\)?",
     ["\\(2.5 \\times 10^5\\)", "\\(2.5 \\times 10^4\\)", "\\(2.5 \\times 10^9\\)", "\\(5.0 \\times 10^5\\)"],
     "A", "OSC", "easy",
     "\\(2k + 3k = 5k = 5 \\times (5.0 \\times 10^4) = 25.0 \\times 10^4 = 2.5 \\times 10^5\\)."),

    # 63
    ("Express \\((2.5 \\times 10^2)^{-1}\\) in standard form.",
     ["\\(4.0 \\times 10^{-3}\\)", "\\(4.0 \\times 10^{-2}\\)", "\\(0.4 \\times 10^{-2}\\)", "\\(2.5 \\times 10^{-2}\\)"],
     "A", "OSC", "medium",
     "\\(2.5 \\times 10^2 = 250\\). Reciprocal \\(\\frac{1}{250} = 0.004 = 4.0 \\times 10^{-3}\\)."),

    # 64
    ("Add: \\(10^6 + 10^4\\) in standard form.",
     ["\\(1.01 \\times 10^6\\)", "\\(2.0 \\times 10^6\\)", "\\(1.01 \\times 10^4\\)", "\\(10^{10}\\)"],
     "A", "OSC", "medium",
     "\\(1,000,000 + 10,000 = 1,010,000 = 1.01 \\times 10^6\\)."),

    # 65
    ("Subtract: \\(10^5 - 10^3\\) in standard form.",
     ["\\(9.9 \\times 10^4\\)", "\\(9.9 \\times 10^5\\)", "\\(9.0 \\times 10^4\\)", "\\(10^2\\)"],
     "A", "OSC", "medium",
     "\\(100,000 - 1,000 = 99,000 = 9.9 \\times 10^4\\)."),

    # 66
    ("True or False: \\((a \\times 10^m) \\times (b \\times 10^n) = (a \\times b) \\times 10^{m+n}\\).",
     ["True", "False"],
     "A", "OTF", "easy",
     "By associative and commutative properties of real multiplication, coefficients multiply together and powers of 10 add exponents."),

    # 67
    ("True or False: To add \\(3 \\times 10^4\\) and \\(4 \\times 10^3\\), the sum is \\(7 \\times 10^7\\).",
     ["False", "True"],
     "A", "OTF", "easy",
     "Exponents cannot be added during addition of terms. The correct sum is \\(30,000 + 4,000 = 34,000 = 3.4 \\times 10^4\\)."),

    # 68
    ("Fill in the blank: To divide \\(A \\times 10^m\\) by \\(B \\times 10^n\\), the exponent of 10 in the raw quotient is _____.",
     ["\\(m - n\\)", "\\(m + n\\)", "\\(m / n\\)", "\\(m \\times n\\)"],
     "A", "OFB", "easy",
     "By the quotient law of exponents, powers are subtracted: \\(m - n\\)."),

    # 69
    ("Fill in the blank: If distance is \\(3.0 \\times 10^8\\text{ m}\\) and time is \\(1.0\\text{ s}\\), the speed is _____ \\(\\text{m/s}\\).",
     ["\\(3.0 \\times 10^8\\)", "\\(3.0 \\times 10^7\\)", "\\(3.0 \\times 10^9\\)", "\\(1.0 \\times 10^8\\)"],
     "A", "OFB", "easy",
     "\\(\\text{Speed} = \\text{Distance} / \\text{Time} = 3.0 \\times 10^8 / 1.0 = 3.0 \\times 10^8\\text{ m/s}\\)."),

    # 70
    ("What is the numerical integer result of \\(\\frac{8.4 \\times 10^5}{2.1 \\times 10^5}\\)?",
     ["4", "40", "0.4", "2"],
     "A", "ONE", "easy",
     "\\(\\frac{8.4 \\times 10^5}{2.1 \\times 10^5} = \\frac{8.4}{2.1} = 4\\)."),
]

# 12 MOCK / FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Planetary Mass Scale Comparison</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Jupiter: circle r=35 -->
    <circle cx="70" cy="70" r="35" fill="#f59e0b" opacity="0.8" stroke="#fbbf24" stroke-width="2"/>
    <text x="70" y="68" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Jupiter</text>
    <text x="70" y="83" fill="#ffffff" font-size="9" text-anchor="middle">1.9 × 10²⁷ kg</text>
    <!-- Earth: circle r=18 -->
    <circle cx="180" cy="70" r="18" fill="#3b82f6" opacity="0.8" stroke="#60a5fa" stroke-width="2"/>
    <text x="180" y="68" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Earth</text>
    <text x="180" y="80" fill="#ffffff" font-size="8" text-anchor="middle">5.97 × 10²⁴ kg</text>
    <!-- Moon: circle r=8 -->
    <circle cx="270" cy="70" r="8" fill="#94a3b8" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="270" y="55" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle">Moon</text>
    <text x="270" y="93" fill="#cbd5e1" font-size="8" text-anchor="middle">7.35 × 10²² kg</text>
    <!-- Ratio line footer -->
    <text x="170" y="132" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Jupiter ≈ 318 × Earth  |  Earth ≈ 81 × Moon</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">About how many times heavier is the Earth compared to the Moon?</p>
</div>""",
     ["About 81 times", "About 8 times", "About 800 times", "About 15 times"],
     "A", "OSC", "easy",
     "\\(\\frac{5.97 \\times 10^{24}}{7.35 \\times 10^{22}} = \\frac{597 \\times 10^{22}}{7.35 \\times 10^{22}} = \\frac{597}{7.35} \\approx 81.2\\) times."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Cosmic Distance Triangle during Solar Eclipse</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Sun (far left) -->
    <circle cx="40" cy="75" r="22" fill="#f59e0b" stroke="#fbbf24" stroke-width="2"/>
    <text x="40" y="79" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">SUN</text>
    <!-- Moon (in middle) -->
    <circle cx="240" cy="75" r="6" fill="#94a3b8" stroke="#ffffff"/>
    <text x="240" y="60" fill="#cbd5e1" font-size="9" text-anchor="middle">Moon</text>
    <!-- Earth (far right) -->
    <circle cx="300" cy="75" r="12" fill="#3b82f6" stroke="#60a5fa" stroke-width="1.5"/>
    <text x="300" y="79" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Earth</text>
    <!-- Dimension lines -->
    <line x1="40" y1="105" x2="300" y2="105" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="170" y="120" fill="#38bdf8" font-size="10" text-anchor="middle">Earth-Sun = 1.496 × 10¹¹ m</text>
    <line x1="240" y1="35" x2="300" y2="35" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="270" y="28" fill="#f43f5e" font-size="9" text-anchor="middle">3.84 × 10⁸ m</text>
    <!-- Footnote -->
    <text x="170" y="140" fill="#fde047" font-size="10" text-anchor="middle">Moon-Sun = (1.496 - 0.00384) × 10¹¹ m ≈ 1.492 × 10¹¹ m</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the distance from the Moon to the Sun during a total solar eclipse?</p>
</div>""",
     ["\\(1.49216 \\times 10^{11}\\text{ m}\\)",
      "\\(1.112 \\times 10^{11}\\text{ m}\\)",
      "\\(1.496 \\times 10^{11}\\text{ m}\\)",
      "\\(3.84 \\times 10^8\\text{ m}\\)"],
     "A", "OSC", "easy",
     "\\(1.496 \\times 10^{11} - 0.00384 \\times 10^{11} = 1.49216 \\times 10^{11}\\text{ m}\\)."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Microscopic Length vs End-to-End Alignment</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Line of 1 metre -->
    <line x1="30" y1="45" x2="310" y2="45" stroke="#10b981" stroke-width="3"/>
    <text x="170" y="35" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">Total Length = 1.4 metres</text>
    <!-- Red blood cells chain -->
    <g fill="#ef4444" stroke="#f87171" stroke-width="1">
      <circle cx="50" cy="75" r="8"/>
      <circle cx="68" cy="75" r="8"/>
      <circle cx="86" cy="75" r="8"/>
      <circle cx="104" cy="75" r="8"/>
    </g>
    <text x="140" y="80" fill="#94a3b8" font-size="14">. . . . . . .</text>
    <circle cx="280" cy="75" r="8" fill="#ef4444" stroke="#f87171"/>
    <text x="77" y="102" fill="#fca5a5" font-size="10" text-anchor="middle">diameter = 7 × 10⁻⁶ m</text>
    <!-- Calculation card -->
    <text x="170" y="132" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Count = 1.4 ÷ (7 × 10⁻⁶) = 2.0 × 10⁵ cells (200,000)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">How many red blood cells of diameter \(7 \times 10^{-6}\text{ m}\) align along a \(1.4\text{ m}\) segment?</p>
</div>""",
     ["\\(2.0 \\times 10^5\\)", "\\(2.0 \\times 10^6\\)", "\\(5.0 \\times 10^4\\)", "\\(2.0 \\times 10^4\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{1.4}{7 \\times 10^{-6}} = 0.2 \\times 10^6 = 2.0 \\times 10^5\\)."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Standard Form Addition Flowchart</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Step 1 -->
    <rect x="15" y="30" width="90" height="50" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="60" y="50" fill="#93c5fd" font-size="10" font-weight="bold" text-anchor="middle">Step 1</text>
    <text x="60" y="68" fill="#e2e8f0" font-size="9" text-anchor="middle">Match Powers</text>
    <!-- Arrow 1 -->
    <text x="115" y="58" fill="#f59e0b" font-size="16" text-anchor="middle">→</text>
    <!-- Step 2 -->
    <rect x="125" y="30" width="95" height="50" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="172" y="50" fill="#93c5fd" font-size="10" font-weight="bold" text-anchor="middle">Step 2</text>
    <text x="172" y="68" fill="#e2e8f0" font-size="9" text-anchor="middle">Add/Sub Coeffs</text>
    <!-- Arrow 2 -->
    <text x="230" y="58" fill="#f59e0b" font-size="16" text-anchor="middle">→</text>
    <!-- Step 3 -->
    <rect x="240" y="30" width="85" height="50" rx="6" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
    <text x="282" y="50" fill="#6ee7b7" font-size="10" font-weight="bold" text-anchor="middle">Step 3</text>
    <text x="282" y="68" fill="#e2e8f0" font-size="9" text-anchor="middle">Re-normalise</text>
    <!-- Example footer -->
    <rect x="35" y="95" width="270" height="35" rx="5" fill="#0f172a" stroke="#475569"/>
    <text x="170" y="117" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">(2.4 × 10⁵) + (3.6 × 10⁴) = (2.4 + 0.36) × 10⁵ = 2.76 × 10⁵</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the sum of \(2.4 \times 10^5\) and \(3.6 \times 10^4\) in standard form?</p>
</div>""",
     ["\\(2.76 \\times 10^5\\)", "\\(6.0 \\times 10^9\\)", "\\(6.0 \\times 10^5\\)", "\\(2.76 \\times 10^4\\)"],
     "A", "OSC", "easy",
     "\\(3.6 \\times 10^4 = 0.36 \\times 10^5\\). Adding: \\((2.4 + 0.36) \\times 10^5 = 2.76 \\times 10^5\\)."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Sunlight Transit Time to Earth</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Sun -->
    <circle cx="45" cy="75" r="22" fill="#f59e0b" stroke="#fbbf24" stroke-width="2"/>
    <text x="45" y="79" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">SUN</text>
    <!-- Wave packet / photon beam -->
    <path d="M 75,75 Q 95,60 115,75 T 155,75 T 195,75 T 235,75 T 270,75" fill="none" stroke="#fde047" stroke-width="2.5"/>
    <!-- Earth -->
    <circle cx="295" cy="75" r="14" fill="#3b82f6" stroke="#60a5fa" stroke-width="2"/>
    <text x="295" y="79" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Earth</text>
    <!-- Equation annotation -->
    <text x="170" y="40" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">c = 3.0 × 10⁸ m/s  |  d = 1.5 × 10¹¹ m</text>
    <text x="170" y="125" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">Time = d / c = (1.5 × 10¹¹) / (3.0 × 10⁸) = 500 seconds</text>
    <text x="170" y="142" fill="#cbd5e1" font-size="10" text-anchor="middle">500 s = 8 minutes 20 seconds</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Using speed of light \(3.0 \times 10^8\text{ m/s}\), how long does light take to travel \(1.5 \times 10^{11}\text{ m}\)?</p>
</div>""",
     ["500 seconds (8 min 20 s)", "50 seconds", "5000 seconds", "80 seconds"],
     "A", "OSC", "easy",
     "\\(t = \\frac{1.5 \\times 10^{11}}{3.0 \\times 10^8} = 0.5 \\times 10^3 = 500\\text{ seconds}\\) (which equals 8 minutes and 20 seconds)."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Exponent Scaling Factor for Area and Volume</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- 1D Edge -->
    <rect x="25" y="30" width="85" height="40" rx="5" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="67" y="48" fill="#93c5fd" font-size="10" font-weight="bold" text-anchor="middle">Edge s</text>
    <text x="67" y="62" fill="#ffffff" font-size="10" text-anchor="middle">2 × 10⁻³ m</text>
    <!-- 2D Area -->
    <rect x="125" y="30" width="90" height="40" rx="5" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="170" y="48" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Area s²</text>
    <text x="170" y="62" fill="#ffffff" font-size="10" text-anchor="middle">4 × 10⁻⁶ m²</text>
    <!-- 3D Volume -->
    <rect x="230" y="30" width="85" height="40" rx="5" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
    <text x="272" y="48" fill="#6ee7b7" font-size="10" font-weight="bold" text-anchor="middle">Volume s³</text>
    <text x="272" y="62" fill="#ffffff" font-size="10" text-anchor="middle">8 × 10⁻⁹ m³</text>
    <!-- Rule footnote -->
    <text x="170" y="110" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Power of exponent multiplies dimension</text>
    <text x="170" y="130" fill="#cbd5e1" font-size="11" text-anchor="middle">(10⁻³)² = 10⁻⁶  |  (10⁻³)³ = 10⁻⁹</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">If the edge of a cube is \(3.0 \times 10^{-2}\text{ m}\), what is its volume in standard form?</p>
</div>""",
     ["\\(2.7 \\times 10^{-5}\\text{ m}^3\\)",
      "\\(2.7 \\times 10^{-6}\\text{ m}^3\\)",
      "\\(9.0 \\times 10^{-4}\\text{ m}^3\\)",
      "\\(2.7 \\times 10^{-8}\\text{ m}^3\\)"],
     "A", "OSC", "easy",
     "\\(V = s^3 = (3.0 \\times 10^{-2})^3 = 27.0 \\times 10^{-6} = 2.7 \\times 10^{-5}\\text{ m}^3\\)."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Chemical Mixture Total Mass</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Beaker A -->
    <rect x="40" y="40" width="75" height="50" rx="4" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2"/>
    <text x="77" y="62" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">Solute A</text>
    <text x="77" y="78" fill="#ffffff" font-size="10" text-anchor="middle">4.8 × 10⁴ g</text>
    <!-- Plus -->
    <text x="135" y="70" fill="#f59e0b" font-size="18" font-weight="bold" text-anchor="middle">+</text>
    <!-- Beaker B -->
    <rect x="155" y="40" width="75" height="50" rx="4" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="192" y="62" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">Solute B</text>
    <text x="192" y="78" fill="#ffffff" font-size="10" text-anchor="middle">7.2 × 10³ g</text>
    <!-- Arrow & Result -->
    <path d="M 240,65 L 265,65" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="265,60 275,65 265,70" fill="#f59e0b"/>
    <circle cx="300" cy="65" r="22" fill="#4c1d95" stroke="#8b5cf6" stroke-width="2"/>
    <text x="300" y="62" fill="#ddd6fe" font-size="10" font-weight="bold" text-anchor="middle">Total</text>
    <text x="300" y="75" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">5.52×10⁴</text>
    <text x="170" y="125" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">4.8 × 10⁴ + 0.72 × 10⁴ = 5.52 × 10⁴ g</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">A laboratory combines \(4.8 \times 10^4\text{ g}\) and \(7.2 \times 10^3\text{ g}\) of two salts. What is the combined mass?</p>
</div>""",
     ["\\(5.52 \\times 10^4\\text{ g}\\)",
      "\\(1.2 \\times 10^5\\text{ g}\\)",
      "\\(5.52 \\times 10^3\\text{ g}\\)",
      "\\(1.2 \\times 10^4\\text{ g}\\)"],
     "A", "OSC", "easy",
     "\\(4.8 \\times 10^4 + 0.72 \\times 10^4 = 5.52 \\times 10^4\\text{ g}\\)."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Geometric Area of a High-Tech Microchip</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Microchip Outline -->
    <rect x="50" y="25" width="130" height="80" rx="4" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
    <text x="115" y="20" fill="#67e8f9" font-size="11" text-anchor="middle">Length: 2.5 × 10⁻² m</text>
    <text x="20" y="70" fill="#67e8f9" font-size="10" text-anchor="middle" transform="rotate(-90 20,70)">Breadth: 1.2 × 10⁻² m</text>
    <!-- Pins on chip -->
    <line x1="65" y1="105" x2="65" y2="115" stroke="#e2e8f0" stroke-width="2"/>
    <line x1="85" y1="105" x2="85" y2="115" stroke="#e2e8f0" stroke-width="2"/>
    <line x1="105" y1="105" x2="105" y2="115" stroke="#e2e8f0" stroke-width="2"/>
    <line x1="125" y1="105" x2="125" y2="115" stroke="#e2e8f0" stroke-width="2"/>
    <line x1="145" y1="105" x2="145" y2="115" stroke="#e2e8f0" stroke-width="2"/>
    <!-- Area Card -->
    <rect x="195" y="35" width="125" height="60" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="257" y="58" fill="#6ee7b7" font-size="11" text-anchor="middle">Area = L × B</text>
    <text x="257" y="78" fill="#fde047" font-size="13" font-weight="bold" text-anchor="middle">= 3.0 × 10⁻⁴ m²</text>
    <text x="170" y="135" fill="#38bdf8" font-size="11" text-anchor="middle">(2.5 × 1.2) × 10⁻⁴ = 3.0 × 10⁻⁴ m²</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">A rectangular computer chip measures \(2.5 \times 10^{-2}\text{ m}\) by \(1.2 \times 10^{-2}\text{ m}\). What is its surface area?</p>
</div>""",
     ["\\(3.0 \\times 10^{-4}\\text{ m}^2\\)",
      "\\(3.0 \\times 10^{-2}\\text{ m}^2\\)",
      "\\(3.0 \\times 10^{-5}\\text{ m}^2\\)",
      "\\(3.7 \\times 10^{-2}\\text{ m}^2\\)"],
     "A", "OSC", "easy",
     "\\(A = L \\times B = (2.5 \\times 1.2) \\times 10^{-2 + (-2)} = 3.0 \\times 10^{-4}\\text{ m}^2\\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Decay Factor per Cycle</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Step boxes -->
    <rect x="20" y="30" width="70" height="40" rx="5" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="55" y="48" fill="#93c5fd" font-size="10" font-weight="bold" text-anchor="middle">Cycle 0</text>
    <text x="55" y="62" fill="#ffffff" font-size="10" text-anchor="middle">8.0 × 10⁶</text>
    <text x="105" y="52" fill="#f59e0b" font-size="12" text-anchor="middle">÷2</text>
    <rect x="120" y="30" width="70" height="40" rx="5" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="155" y="48" fill="#93c5fd" font-size="10" font-weight="bold" text-anchor="middle">Cycle 1</text>
    <text x="155" y="62" fill="#ffffff" font-size="10" text-anchor="middle">4.0 × 10⁶</text>
    <text x="205" y="52" fill="#f59e0b" font-size="12" text-anchor="middle">÷2</text>
    <rect x="220" y="30" width="70" height="40" rx="5" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
    <text x="255" y="48" fill="#6ee7b7" font-size="10" font-weight="bold" text-anchor="middle">Cycle 2</text>
    <text x="255" y="62" fill="#ffffff" font-size="10" text-anchor="middle">2.0 × 10⁶</text>
    <!-- Footer Note -->
    <text x="170" y="110" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">After 3 cycles: 2.0 × 10⁶ ÷ 2 = 1.0 × 10⁶</text>
    <text x="170" y="130" fill="#cbd5e1" font-size="11" text-anchor="middle">Halving divides the coefficient while power remains 10⁶</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">A radioactive sample of \(8.0 \times 10^6\) nuclei undergoes 3 successive half-lives. What is the remaining count?</p>
</div>""",
     ["\\(1.0 \\times 10^6\\)", "\\(2.0 \\times 10^6\\)", "\\(4.0 \\times 10^6\\)", "\\(1.0 \\times 10^5\\)"],
     "A", "OSC", "easy",
     "After 3 half-lives, the quantity is divided by \\(2^3 = 8\\): \\(\\frac{8.0 \\times 10^6}{8} = 1.0 \\times 10^6\\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Power of 10 Scale Dominance Rule</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Large exponent card -->
    <rect x="30" y="30" width="120" height="60" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="90" y="55" fill="#6ee7b7" font-size="14" font-weight="bold" text-anchor="middle">1.1 × 10⁶</text>
    <text x="90" y="75" fill="#e2e8f0" font-size="11" text-anchor="middle">= 1,100,000</text>
    <!-- Greater than -->
    <text x="170" y="65" fill="#f59e0b" font-size="22" font-weight="bold" text-anchor="middle">&gt;</text>
    <!-- Small exponent card with big coefficient -->
    <rect x="190" y="30" width="120" height="60" rx="6" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
    <text x="250" y="55" fill="#fca5a5" font-size="14" font-weight="bold" text-anchor="middle">9.9 × 10⁵</text>
    <text x="250" y="75" fill="#e2e8f0" font-size="11" text-anchor="middle">= 990,000</text>
    <!-- Rule footnote -->
    <text x="170" y="125" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Even 1.1 × 10⁶ exceeds 9.9 × 10⁵ because 10⁶ &gt; 10⁵</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Which number is greater: \(1.2 \times 10^7\) or \(9.8 \times 10^6\)?</p>
</div>""",
     ["\\(1.2 \\times 10^7\\)", "\\(9.8 \\times 10^6\\)", "Both are equal", "Cannot be determined"],
     "A", "OSC", "easy",
     "\\(1.2 \\times 10^7 = 12 \\times 10^6\\). Since \\(12 > 9.8\\), \\(1.2 \\times 10^7\\) is greater."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Ratio Comparison of Biological vs Physical Scales</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- RBC Diameter -->
    <rect x="35" y="30" width="120" height="55" rx="6" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="95" y="52" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">RBC Diameter</text>
    <text x="95" y="70" fill="#ffffff" font-size="11" text-anchor="middle">7 × 10⁻⁶ m</text>
    <!-- Arrow -->
    <text x="170" y="60" fill="#f59e0b" font-size="18" text-anchor="middle">÷</text>
    <!-- Chip Wire Diameter -->
    <rect x="185" y="30" width="120" height="55" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="245" y="52" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">Chip Wire</text>
    <text x="245" y="70" fill="#ffffff" font-size="11" text-anchor="middle">3 × 10⁻⁶ m</text>
    <!-- Ratio line -->
    <text x="170" y="115" fill="#fde047" font-size="13" font-weight="bold" text-anchor="middle">Ratio = 7 / 3 ≈ 2.33</text>
    <text x="170" y="135" fill="#cbd5e1" font-size="11" text-anchor="middle">Identical powers of 10 cancel completely</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the ratio of a red blood cell (\(7 \times 10^{-6}\text{ m}\)) to a chip wire (\(3 \times 10^{-6}\text{ m}\))?</p>
</div>""",
     ["7 : 3 (approx 2.33)", "3 : 7", "70 : 3", "1 : 1"],
     "A", "OSC", "easy",
     "\\(\\frac{7 \\times 10^{-6}}{3 \\times 10^{-6}} = \\frac{7}{3} \\approx 2.33\\)."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Electron Charge Multiplication: Q = n × e</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Elementary Charge e -->
    <rect x="30" y="30" width="115" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="87" y="52" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">e = 1.6 × 10⁻¹⁹ C</text>
    <text x="87" y="70" fill="#cbd5e1" font-size="10" text-anchor="middle">Charge per electron</text>
    <!-- Multiply by n -->
    <text x="160" y="60" fill="#f59e0b" font-size="16" font-weight="bold" text-anchor="middle">×</text>
    <!-- Particle Count n -->
    <rect x="180" y="30" width="130" height="55" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="245" y="52" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">n = 5.0 × 10¹⁸</text>
    <text x="245" y="70" fill="#cbd5e1" font-size="10" text-anchor="middle">Total electrons</text>
    <!-- Total Charge Q -->
    <text x="170" y="115" fill="#fde047" font-size="13" font-weight="bold" text-anchor="middle">Total Charge Q = (1.6 × 5.0) × 10⁻¹⁹ ⁺ ¹⁸</text>
    <text x="170" y="135" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">= 8.0 × 10⁻¹ C = 0.8 Coulombs</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the total charge carried by \(5.0 \times 10^{18}\) electrons (each of charge \(1.6 \times 10^{-19}\text{ C}\))?</p>
</div>""",
     ["0.8 Coulombs (\\(8.0 \\times 10^{-1}\\text{ C}\\))",
      "8.0 Coulombs",
      "0.08 Coulombs",
      "\\(8.0 \\times 10^{-37}\\text{ C}\\)"],
     "A", "OSC", "easy",
     "\\(Q = n \\times e = (5.0 \\times 1.6) \\times 10^{18 + (-19)} = 8.0 \\times 10^{-1} = 0.8\\text{ Coulombs}\\).")
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch2_topic4.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
