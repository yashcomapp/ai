# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-1-1.6
Topic: Cube Roots by Prime Factorisation & Estimation
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-1-1.6"

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
    ("What does the symbol \\(\\sqrt[3]{x}\\) denote?",
     ["The cube root of \\(x\\)",
      "The square root of \\(x\\)",
      "\\(x\\) divided by 3",
      "\\(3\\) times \\(x\\)"],
     "A", "OSC", "easy",
     "The radical sign with index 3, written as \\(\\sqrt[3]{x}\\), denotes the cube root of \\(x\\). It represents the number which when raised to the third power equals \\(x\\)."),

    # 2
    ("What is the cube root of 216?",
     ["6", "4", "8", "16"],
     "A", "OSC", "easy",
     "Since \\(6^3 = 6 \\times 6 \\times 6 = 216\\), \\(\\sqrt[3]{216} = 6\\)."),

    # 3
    ("What is the cube root of \\(-512\\)?",
     ["\\(-8\\)", "8", "\\(-16\\)", "16"],
     "A", "OSC", "easy",
     "For any positive integer \\(a\\), \\(\\sqrt[3]{-a} = -\\sqrt[3]{a}\\). Since \\(8^3 = 512\\), \\(\\sqrt[3]{-512} = -8\\)."),

    # 4
    ("What is the value of \\(\\sqrt[3]{1728}\\)?",
     ["12", "14", "16", "18"],
     "A", "OSC", "easy",
     "Prime factorisation of 1728 is \\(2^6 \\times 3^3 = (2^2 \\times 3)^3 = 12^3\\). Hence \\(\\sqrt[3]{1728} = 12\\)."),

    # 5
    ("What is the value of \\(\\sqrt[3]{3375}\\)?",
     ["15", "25", "35", "5"],
     "A", "OSC", "easy",
     "Prime factorising 3375 gives \\(3^3 \\times 5^3 = (3 \\times 5)^3 = 15^3\\). Therefore \\(\\sqrt[3]{3375} = 15\\)."),

    # 6
    ("Which mathematical property is used when computing \\(\\sqrt[3]{a \\times b}\\)?",
     ["\\(\\sqrt[3]{a \\times b} = \\sqrt[3]{a} \\times \\sqrt[3]{b}\\)",
      "\\(\\sqrt[3]{a \\times b} = \\sqrt[3]{a} + \\sqrt[3]{b}\\)",
      "\\(\\sqrt[3]{a \\times b} = 3\\sqrt{a} \\times 3\\sqrt{b}\\)",
      "\\(\\sqrt[3]{a \\times b} = a \\times \\sqrt[3]{b}\\)"],
     "A", "OSC", "easy",
     "The radical of a product distributes across multiplication: \\(\\sqrt[3]{a \\times b} = \\sqrt[3]{a} \\times \\sqrt[3]{b}\\)."),

    # 7
    ("What is the value of \\(\\sqrt[3]{\\frac{27}{125}}\\)?",
     ["\\(\\frac{3}{5}\\)", "\\(\\frac{9}{25}\\)", "\\(\\frac{3}{25}\\)", "\\(\\frac{9}{5}\\)"],
     "A", "OSC", "easy",
     "\\(\\sqrt[3]{\\frac{27}{125}} = \\frac{\\sqrt[3]{27}}{\\sqrt[3]{125}} = \\frac{3}{5}\\)."),

    # 8
    ("What is the cube root of \\(0.008\\)?",
     ["0.2", "0.02", "0.002", "2.0"],
     "A", "OSC", "easy",
     "\\(0.008 = \\frac{8}{1000}\\). Taking cube roots: \\(\\sqrt[3]{\\frac{8}{1000}} = \\frac{\\sqrt[3]{8}}{\\sqrt[3]{1000}} = \\frac{2}{10} = 0.2\\)."),

    # 9
    ("What is the units digit of the cube root of a perfect cube ending in 7?",
     ["3", "7", "1", "9"],
     "A", "OSC", "easy",
     "The only single digit whose cube ends in 7 is 3 (since \\(3^3 = 27\\)). Thus, any perfect cube ending in 7 has a cube root ending in 3."),

    # 10
    ("What is the units digit of the cube root of a perfect cube ending in 8?",
     ["2", "8", "4", "6"],
     "A", "OSC", "easy",
     "Since \\(2^3 = 8\\), any perfect cube ending in 8 must have a cube root whose units digit is 2."),

    # 11
    ("What is the units digit of the cube root of a perfect cube ending in 4?",
     ["4", "6", "2", "8"],
     "A", "OSC", "easy",
     "Since \\(4^3 = 64\\), digits ending in 4 retain 4 when cubed, so the cube root of a number ending in 4 also ends in 4."),

    # 12
    ("What is the units digit of the cube root of 19683?",
     ["7", "3", "9", "1"],
     "A", "OSC", "easy",
     "The number 19683 ends in 3. Since \\(7^3 = 343\\) (which ends in 3), the cube root must end in 7."),

    # 13
    ("Estimate the cube root of 17576 using the grouping method.",
     ["26", "24", "36", "16"],
     "A", "OSC", "medium",
     "Divide into groups from the right: Group 1 is 576, Group 2 is 17. Group 1 ends in 6, so units digit is 6. Group 2 is 17, and \\(2^3 = 8 \\le 17 < 3^3 = 27\\), so tens digit is 2. Hence \\(\\sqrt[3]{17576} = 26\\)."),

    # 14
    ("Estimate the cube root of 85184.",
     ["44", "46", "34", "54"],
     "A", "OSC", "medium",
     "Dividing into groups: Group 1 is 184 (ends in 4, so units digit is 4). Group 2 is 85; since \\(4^3 = 64 \\le 85 < 5^3 = 125\\), tens digit is 4. Thus \\(\\sqrt[3]{85184} = 44\\)."),

    # 15
    ("Estimate the cube root of 110592.",
     ["48", "42", "58", "38"],
     "A", "OSC", "medium",
     "Group 1 is 592 (ends in 2, so units digit is 8 since \\(8^3 = 512\\)). Group 2 is 110; since \\(4^3 = 64 \\le 110 < 5^3 = 125\\), tens digit is 4. Thus \\(\\sqrt[3]{110592} = 48\\)."),

    # 16
    ("What is the cube root of \\(4096\\)?",
     ["16", "14", "18", "24"],
     "A", "OSC", "easy",
     "\\(4096 = 2^{12} = (2^4)^3 = 16^3\\). Hence \\(\\sqrt[3]{4096} = 16\\)."),

    # 17
    ("What is the cube root of \\(5832\\)?",
     ["18", "16", "22", "28"],
     "A", "OSC", "easy",
     "Prime factors of 5832 are \\(2^3 \\times 3^6 = (2 \\times 3^2)^3 = 18^3\\). Therefore \\(\\sqrt[3]{5832} = 18\\)."),

    # 18
    ("What is the cube root of \\(9261\\)?",
     ["21", "19", "23", "31"],
     "A", "OSC", "easy",
     "Prime factors of 9261 are \\(3^3 \\times 7^3 = (3 \\times 7)^3 = 21^3\\). Thus \\(\\sqrt[3]{9261} = 21\\)."),

    # 19
    ("What is the value of \\(\\sqrt[3]{-1331}\\)?",
     ["\\(-11\\)", "11", "\\(-21\\)", "21"],
     "A", "OSC", "easy",
     "\\(11^3 = 1331\\). Therefore \\(\\sqrt[3]{-1331} = -11\\)."),

    # 20
    ("What is the cube root of \\(0.000064\\)?",
     ["0.04", "0.004", "0.4", "0.0004"],
     "A", "OSC", "medium",
     "\\(0.000064 = \\frac{64}{1000000}\\). Cube root is \\(\\frac{\\sqrt[3]{64}}{\\sqrt[3]{1000000}} = \\frac{4}{100} = 0.04\\)."),

    # 21
    ("Find the edge length of a cube whose volume is \\(2744\\text{ cm}^3\\).",
     ["14 cm", "12 cm", "16 cm", "18 cm"],
     "A", "OSC", "medium",
     "Volume of cube \\(V = s^3 = 2744\\text{ cm}^3\\). \\(2744 = 2^3 \\times 7^3 = (14)^3\\). So \\(s = 14\\text{ cm}\\)."),

    # 22
    ("Find the edge of a cube whose volume is \\(10648\\text{ m}^3\\).",
     ["22 m", "24 m", "18 m", "28 m"],
     "A", "OSC", "medium",
     "Volume \\(V = s^3 = 10648\\). Prime factorising: \\(10648 = 2^3 \\times 11^3 = (22)^3\\). So \\(s = 22\\text{ m}\\)."),

    # 23
    ("Evaluate: \\(\\sqrt[3]{-27} \\times \\sqrt[3]{-64}\\)",
     ["12", "\\(-12\\)", "7", "\\(-7\\)"],
     "A", "OSC", "medium",
     "\\(\\sqrt[3]{-27} = -3\\) and \\(\\sqrt[3]{-64} = -4\\). Multiplying gives \\((-3) \\times (-4) = 12\\)."),

    # 24
    ("Evaluate: \\(\\sqrt[3]{1000} + \\sqrt[3]{0.001} - \\sqrt[3]{0.125}\\)",
     ["9.6", "10.5", "9.5", "10.6"],
     "A", "OSC", "medium",
     "\\(\\sqrt[3]{1000} = 10\\), \\(\\sqrt[3]{0.001} = 0.1\\), and \\(\\sqrt[3]{0.125} = 0.5\\). Calculating: \\(10 + 0.1 - 0.5 = 9.6\\)."),

    # 25
    ("What is the value of \\(\\sqrt[3]{729 \\times 64}\\)?",
     ["72", "54", "36", "81"],
     "A", "OSC", "medium",
     "\\(\\sqrt[3]{729} \\times \\sqrt[3]{64} = 9 \\times 4 = 36\\)."),

    # 26
    ("What is the value of \\(\\sqrt[3]{\\frac{-216}{343}}\\)?",
     ["\\(-\\frac{6}{7}\\)", "\\(\\frac{6}{7}\\)", "\\(-\\frac{36}{49}\\)", "\\(-\\frac{6}{49}\\)"],
     "A", "OSC", "easy",
     "\\(\\sqrt[3]{\\frac{-216}{343}} = \\frac{\\sqrt[3]{-216}}{\\sqrt[3]{343}} = \\frac{-6}{7} = -\\frac{6}{7}\\)."),

    # 27
    ("Estimate the cube root of 32768.",
     ["32", "28", "38", "42"],
     "A", "OSC", "medium",
     "Group 1: 768 (ends in 8, so units digit is 2). Group 2: 32; since \\(3^3 = 27 \\le 32 < 4^3 = 64\\), tens digit is 3. Hence \\(\\sqrt[3]{32768} = 32\\)."),

    # 28
    ("Estimate the cube root of 59319.",
     ["39", "49", "31", "41"],
     "A", "OSC", "medium",
     "Group 1: 319 (ends in 9, so units digit is 9). Group 2: 59; since \\(3^3 = 27 \\le 59 < 4^3 = 64\\), tens digit is 3. Hence \\(\\sqrt[3]{59319} = 39\\)."),

    # 29
    ("What is the cube root of \\(13824\\)?",
     ["24", "26", "22", "28"],
     "A", "OSC", "medium",
     "Prime factorisation: \\(13824 = 2^9 \\times 3^3 = (2^3 \\times 3)^3 = (8 \\times 3)^3 = 24^3\\). Hence \\(\\sqrt[3]{13824} = 24\\)."),

    # 30
    ("What is the cube root of \\(15625\\)?",
     ["25", "15", "35", "45"],
     "A", "OSC", "easy",
     "\\(15625 = 5^6 = (5^2)^3 = 25^3\\). Thus \\(\\sqrt[3]{15625} = 25\\)."),

    # 31
    ("Which of the following numbers has a cube root that is an irrational number?",
     ["32", "64", "125", "216"],
     "A", "OSC", "medium",
     "64, 125, and 216 are perfect cubes (cubes of 4, 5, 6). 32 is not a perfect cube (\\(2^5\\)), so \\(\\sqrt[3]{32} = 2\\sqrt[3]{4}\\), which is irrational."),

    # 32
    ("What is the value of \\(\\sqrt[3]{1 + \\sqrt{64}}\\)?",
     ["\\(\\sqrt[3]{9}\\)", "3", "2", "1"],
     "A", "OSC", "medium",
     "First evaluate inside: \\(\\sqrt{64} = 8\\). Then \\(1 + 8 = 9\\). The expression is \\(\\sqrt[3]{9}\\)."),

    # 33
    ("What is the value of \\(\\sqrt{\\sqrt[3]{4096}}\\)?",
     ["4", "8", "2", "16"],
     "A", "OSC", "medium",
     "First, \\(\\sqrt[3]{4096} = 16\\). Then taking the square root: \\(\\sqrt{16} = 4\\)."),

    # 34
    ("Assertion (A): The cube root of any negative integer is always negative.\nReason (R): The product of three negative numbers is negative.",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "Because \\((-x) \\times (-x) \\times (-x) = -x^3\\), the cube of a negative number is negative, which means the cube root of a negative number is always negative."),

    # 35
    ("Assertion (A): The cube root of 1728 can be found by grouping 1728 into 728 and 1.\nReason (R): The units digit of 728 gives 2, and 1 gives 1, so the cube root is 12.",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "Grouping 1728 gives Group 1 = 728 (ends in 8, so units digit of cube root is 2) and Group 2 = 1 (tens digit is 1). This confirms the estimation method gives 12."),

    # 36
    ("True or False: Every integer has a unique real cube root.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Unlike square roots (where negative numbers have no real square root and positive numbers have two), every real number has exactly one unique real cube root."),

    # 37
    ("True or False: The estimation method for cube roots works accurately for any arbitrary non-cube number.",
     ["False", "True"],
     "A", "OTF", "easy",
     "The shortcut estimation method applies ONLY when the number is already known to be a perfect cube."),

    # 38
    ("Fill in the blank: The cube root of a number ending in 5 always ends in _____.",
     ["5", "0", "25", "125"],
     "A", "OFB", "easy",
     "Since \\(5^3 = 125\\), any perfect cube ending in 5 must have a cube root whose units digit is 5."),

    # 39
    ("Fill in the blank: If \\(V\\) is the volume of a cube, its side length \\(s\\) is given by \\(s = \\) _____.",
     ["\\(\\sqrt[3]{V}\\)", "\\(\\sqrt{V}\\)", "\\(V^3\\)", "\\(\\frac{V}{3}\\)"],
     "A", "OFB", "easy",
     "Since volume is \\(V = s^3\\), taking the cube root of both sides gives \\(s = \\sqrt[3]{V}\\)."),

    # 40
    ("What is the numerical value of \\(\\sqrt[3]{2197}\\)?",
     ["13", "17", "19", "23"],
     "A", "ONE", "easy",
     "\\(13^3 = 13 \\times 13 \\times 13 = 169 \\times 13 = 2197\\). Thus \\(\\sqrt[3]{2197} = 13\\)."),
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    ("Find \\(\\sqrt[3]{512}\\) by prime factorisation.",
     ["8", "6", "12", "16"],
     "A", "OSC", "easy",
     "\\(512 = 2^9 = (2^3)^3 = 8^3\\). Hence \\(\\sqrt[3]{512} = 8\\)."),

    # 42
    ("Find \\(\\sqrt[3]{729}\\) by prime factorisation.",
     ["9", "7", "11", "3"],
     "A", "OSC", "easy",
     "\\(729 = 3^6 = (3^2)^3 = 9^3\\). Hence \\(\\sqrt[3]{729} = 9\\)."),

    # 43
    ("Find \\(\\sqrt[3]{1000}\\).",
     ["10", "100", "20", "5"],
     "A", "OSC", "easy",
     "\\(1000 = 10^3\\). Thus \\(\\sqrt[3]{1000} = 10\\)."),

    # 44
    ("Find the cube root of \\(27000\\).",
     ["30", "300", "90", "27"],
     "A", "OSC", "easy",
     "\\(27000 = 27 \\times 1000 = 3^3 \\times 10^3 = (3 \\times 10)^3 = 30^3\\). Thus \\(\\sqrt[3]{27000} = 30\\)."),

    # 45
    ("Find the cube root of \\(64000\\).",
     ["40", "400", "20", "80"],
     "A", "OSC", "easy",
     "\\(64000 = 64 \\times 1000 = 4^3 \\times 10^3 = 40^3\\). Therefore \\(\\sqrt[3]{64000} = 40\\)."),

    # 46
    ("Find the cube root of \\(125000\\).",
     ["50", "500", "25", "15"],
     "A", "OSC", "easy",
     "\\(125000 = 125 \\times 1000 = 5^3 \\times 10^3 = 50^3\\). Thus \\(\\sqrt[3]{125000} = 50\\)."),

    # 47
    ("Evaluate: \\(\\sqrt[3]{216 \\times 343}\\)",
     ["42", "48", "36", "56"],
     "A", "OSC", "medium",
     "\\(\\sqrt[3]{216} \\times \\sqrt[3]{343} = 6 \\times 7 = 42\\)."),

    # 48
    ("Evaluate: \\(\\sqrt[3]{125 \\times 64}\\)",
     ["20", "25", "40", "15"],
     "A", "OSC", "easy",
     "\\(\\sqrt[3]{125} \\times \\sqrt[3]{64} = 5 \\times 4 = 20\\)."),

    # 49
    ("Evaluate: \\(\\sqrt[3]{-1000} \\times \\sqrt[3]{-8}\\)",
     ["20", "\\(-20\\)", "80", "\\(-80\\)"],
     "A", "OSC", "easy",
     "\\(\\sqrt[3]{-1000} = -10\\) and \\(\\sqrt[3]{-8} = -2\\). Then \\((-10) \\times (-2) = 20\\)."),

    # 50
    ("What is the cube root of \\(1.728\\)?",
     ["1.2", "0.12", "12", "0.012"],
     "A", "OSC", "medium",
     "\\(1.728 = \\frac{1728}{1000}\\). Cube root is \\(\\frac{\\sqrt[3]{1728}}{\\sqrt[3]{1000}} = \\frac{12}{10} = 1.2\\)."),

    # 51
    ("What is the cube root of \\(0.027\\)?",
     ["0.3", "0.03", "3", "0.003"],
     "A", "OSC", "easy",
     "\\(0.027 = \\frac{27}{1000}\\). Taking cube root gives \\(\\frac{3}{10} = 0.3\\)."),

    # 52
    ("What is the cube root of \\(0.000125\\)?",
     ["0.05", "0.5", "0.005", "0.25"],
     "A", "OSC", "medium",
     "\\(0.000125 = \\frac{125}{1000000}\\). Cube root is \\(\\frac{5}{100} = 0.05\\)."),

    # 53
    ("Estimate the cube root of 4913.",
     ["17", "13", "19", "27"],
     "A", "OSC", "medium",
     "Group 1: 913 (ends in 3, so unit digit is 7 since \\(7^3 = 343\\)). Group 2: 4; since \\(1^3 = 1 \\le 4 < 2^3 = 8\\), tens digit is 1. Thus \\(\\sqrt[3]{4913} = 17\\)."),

    # 54
    ("Estimate the cube root of 12167.",
     ["23", "27", "13", "33"],
     "A", "OSC", "medium",
     "Group 1: 167 (ends in 7, so units digit is 3 since \\(3^3 = 27\\)). Group 2: 12; since \\(2^3 = 8 \\le 12 < 3^3 = 27\\), tens digit is 2. So \\(\\sqrt[3]{12167} = 23\\)."),

    # 55
    ("Estimate the cube root of 24389.",
     ["29", "19", "39", "21"],
     "A", "OSC", "medium",
     "Group 1: 389 (ends in 9, so units digit is 9). Group 2: 24; since \\(2^3 = 8 \\le 24 < 3^3 = 27\\), tens digit is 2. So \\(\\sqrt[3]{24389} = 29\\)."),

    # 56
    ("Estimate the cube root of 68921.",
     ["41", "31", "51", "21"],
     "A", "OSC", "medium",
     "Group 1: 921 (ends in 1, so units digit is 1). Group 2: 68; since \\(4^3 = 64 \\le 68 < 5^3 = 125\\), tens digit is 4. So \\(\\sqrt[3]{68921} = 41\\)."),

    # 57
    ("Estimate the cube root of 91125.",
     ["45", "35", "55", "25"],
     "A", "OSC", "medium",
     "Group 1: 125 (ends in 5, so units digit is 5). Group 2: 91; since \\(4^3 = 64 \\le 91 < 5^3 = 125\\), tens digit is 4. Thus \\(\\sqrt[3]{91125} = 45\\)."),

    # 58
    ("Estimate the cube root of 140608.",
     ["52", "42", "62", "58"],
     "A", "OSC", "medium",
     "Group 1: 608 (ends in 8, so units digit is 2). Group 2: 140; since \\(5^3 = 125 \\le 140 < 6^3 = 216\\), tens digit is 5. So \\(\\sqrt[3]{140608} = 52\\)."),

    # 59
    ("Estimate the cube root of 175616.",
     ["56", "46", "66", "54"],
     "A", "OSC", "medium",
     "Group 1: 616 (ends in 6, so units digit is 6). Group 2: 175; since \\(5^3 = 125 \\le 175 < 6^3 = 216\\), tens digit is 5. Thus \\(\\sqrt[3]{175616} = 56\\)."),

    # 60
    ("A cubical water tank holds \\(216000\\text{ litres}\\) of water. If \\(1\\text{ m}^3 = 1000\\text{ litres}\\), find the inner edge of the tank in metres.",
     ["6 m", "60 m", "3.6 m", "16 m"],
     "A", "OSC", "medium",
     "Capacity in \\(\\text{m}^3\\) is \\(\\frac{216000}{1000} = 216\\text{ m}^3\\). The edge is \\(s = \\sqrt[3]{216} = 6\\text{ m}\\)."),

    # 61
    ("Three solid metal cubes of edges \\(3\\text{ cm}\\), \\(4\\text{ cm}\\), and \\(5\\text{ cm}\\) are melted together into a single large cube. What is the edge of the new cube?",
     ["6 cm", "7 cm", "8 cm", "12 cm"],
     "A", "OSC", "medium",
     "Total volume = \\(3^3 + 4^3 + 5^3 = 27 + 64 + 125 = 216\\text{ cm}^3\\). The new edge is \\(\\sqrt[3]{216} = 6\\text{ cm}\\)."),

    # 62
    ("Evaluate: \\(\\sqrt[3]{-0.000343}\\)",
     ["\\(-0.07\\)", "0.07", "\\(-0.7\\)", "\\(-0.007\\)"],
     "A", "OSC", "medium",
     "\\(-0.000343 = -\\frac{343}{1000000}\\). The cube root is \\(-\\frac{7}{100} = -0.07\\)."),

    # 63
    ("Evaluate: \\(\\sqrt[3]{\\frac{512}{729}}\\)",
     ["\\(\\frac{8}{9}\\)", "\\(\\frac{16}{27}\\)", "\\(\\frac{4}{9}\\)", "\\(\\frac{8}{27}\\)"],
     "A", "OSC", "easy",
     "\\(\\sqrt[3]{512} = 8\\) and \\(\\sqrt[3]{729} = 9\\). Hence the answer is \\(\\frac{8}{9}\\)."),

    # 64
    ("Evaluate: \\(\\sqrt[3]{125} + \\sqrt[3]{-27} + \\sqrt[3]{-8}\\)",
     ["0", "10", "4", "6"],
     "A", "OSC", "easy",
     "\\(5 + (-3) + (-2) = 5 - 5 = 0\\)."),

    # 65
    ("What is the value of \\(\\sqrt[3]{-21952}\\)?",
     ["\\(-28\\)", "28", "\\(-38\\)", "\\(-18\\)"],
     "A", "OSC", "medium",
     "\\(21952 = 2^6 \\times 7^3 = (4 \\times 7)^3 = 28^3\\). Hence \\(\\sqrt[3]{-21952} = -28\\)."),

    # 66
    ("True or False: If a number ends in three zeros, its cube root always ends in one zero.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Since \\((10k)^3 = 1000k^3\\), every block of 3 trailing zeros in a cube corresponds to 1 trailing zero in its cube root."),

    # 67
    ("True or False: \\(\\sqrt[3]{x + y} = \\sqrt[3]{x} + \\sqrt[3]{y}\\) for all non-zero numbers.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Cube root does not distribute across addition. For example, \\(\\sqrt[3]{1 + 7} = \\sqrt[3]{8} = 2\\), but \\(\\sqrt[3]{1} + \\sqrt[3]{7} = 1 + 1.913 \\approx 2.913\\)."),

    # 68
    ("Fill in the blank: The cube root of a number ending in 2 always ends in _____.",
     ["8", "2", "4", "6"],
     "A", "OFB", "easy",
     "Since \\(8^3 = 512\\) (ends in 2), the cube root of any number ending in 2 ends in 8."),

    # 69
    ("Fill in the blank: To find the cube root of a large number by estimation, we divide its digits into groups of _____ starting from the right.",
     ["3", "2", "4", "1"],
     "A", "OFB", "easy",
     "The estimation method divides digits into periods/groups of 3 starting from the units digit."),

    # 70
    ("What is the numerical edge length of a cube (in cm) whose volume is \\(343\\text{ cm}^3\\)?",
     ["7", "6", "8", "9"],
     "A", "ONE", "easy",
     "Volume \\(s^3 = 343 = 7^3\\). Hence the edge is 7 cm."),
]

# 12 MOCK / FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Visualising the Cube Root as Inverse of Volume</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Solid Cube 3D projection -->
    <polygon points="40,90 90,90 120,60 70,60" fill="#3b82f6" opacity="0.8" stroke="#60a5fa" stroke-width="2"/>
    <polygon points="90,90 120,60 120,110 90,140" fill="#1d4ed8" opacity="0.9" stroke="#60a5fa" stroke-width="2"/>
    <polygon points="40,90 90,90 90,140 40,140" fill="#2563eb" stroke="#60a5fa" stroke-width="2"/>
    <text x="65" y="148" fill="#e2e8f0" font-size="12" text-anchor="middle">edge s</text>
    <text x="75" y="105" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">V = s³ = 216</text>
    <!-- Arrow indicating cube root operation -->
    <path d="M 140,95 L 200,95" stroke="#f59e0b" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="200,90 215,95 200,100" fill="#f59e0b"/>
    <text x="170" y="80" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">∛V</text>
    <!-- Resulting line segment edge -->
    <line x1="240" y1="95" x2="310" y2="95" stroke="#10b981" stroke-width="4"/>
    <circle cx="240" cy="95" r="4" fill="#10b981"/>
    <circle cx="310" cy="95" r="4" fill="#10b981"/>
    <text x="275" y="85" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">edge s = 6</text>
    <text x="275" y="120" fill="#94a3b8" font-size="11" text-anchor="middle">6 × 6 × 6 = 216</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">In the diagram, a solid cube of volume \(216\text{ cm}^3\) has edge \(s\). What is the side length \(s\)?</p>
</div>""",
     ["6 cm", "4 cm", "8 cm", "12 cm"],
     "A", "OSC", "easy",
     "The cube root represents finding the side of a cube given its volume. Since \(V = s^3 = 216\), \(s = \\sqrt[3]{216} = 6\\text{ cm}\)."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Triplets of Prime Factors Method</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Factor tree / triplets display -->
    <text x="170" y="25" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">Prime Factorisation of 1728</text>
    <!-- Triplet 1: 2 x 2 x 2 -->
    <rect x="25" y="45" width="85" height="35" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2"/>
    <text x="67" y="67" fill="#60a5fa" font-size="12" font-weight="bold" text-anchor="middle">2 × 2 × 2</text>
    <!-- Triplet 2: 2 x 2 x 2 -->
    <rect x="125" y="45" width="85" height="35" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2"/>
    <text x="167" y="67" fill="#60a5fa" font-size="12" font-weight="bold" text-anchor="middle">2 × 2 × 2</text>
    <!-- Triplet 3: 3 x 3 x 3 -->
    <rect x="225" y="45" width="85" height="35" rx="6" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
    <text x="267" y="67" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">3 × 3 × 3</text>
    <!-- One representative from each triplet -->
    <text x="67" y="115" fill="#93c5fd" font-size="14" font-weight="bold" text-anchor="middle">2</text>
    <text x="117" y="115" fill="#e2e8f0" font-size="14" text-anchor="middle">×</text>
    <text x="167" y="115" fill="#93c5fd" font-size="14" font-weight="bold" text-anchor="middle">2</text>
    <text x="217" y="115" fill="#e2e8f0" font-size="14" text-anchor="middle">×</text>
    <text x="267" y="115" fill="#fcd34d" font-size="14" font-weight="bold" text-anchor="middle">3</text>
    <!-- Total product line -->
    <text x="170" y="140" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">= 12</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">By selecting one prime factor from each group of three equal factors, what is \(\sqrt[3]{1728}\)?</p>
</div>""",
     ["12", "18", "24", "16"],
     "A", "OSC", "easy",
     "Factoring 1728 gives \((2 \\times 2 \\times 2) \\times (2 \\times 2 \\times 2) \\times (3 \\times 3 \\times 3)\). Taking one factor from each triplet yields \(2 \\times 2 \\times 3 = 12\)."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">The Two-Group Estimation Method</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Large Number Display -->
    <rect x="70" y="20" width="80" height="40" rx="6" fill="#312e81" stroke="#6366f1" stroke-width="2"/>
    <text x="110" y="46" fill="#a5b4fc" font-size="16" font-weight="bold" text-anchor="middle">17</text>
    <text x="110" y="75" fill="#94a3b8" font-size="10" text-anchor="middle">Group II</text>
    <rect x="170" y="20" width="100" height="40" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
    <text x="220" y="46" fill="#6ee7b7" font-size="16" font-weight="bold" text-anchor="middle">576</text>
    <text x="220" y="75" fill="#94a3b8" font-size="10" text-anchor="middle">Group I (right 3)</text>
    <!-- Deducing digits -->
    <text x="110" y="105" fill="#c7d2fe" font-size="11" text-anchor="middle">2³ ≤ 17 &lt; 3³</text>
    <text x="110" y="125" fill="#fcd34d" font-size="14" font-weight="bold" text-anchor="middle">Tens = 2</text>
    <text x="220" y="105" fill="#a7f3d0" font-size="11" text-anchor="middle">Ends in 6 ⇒ 6³=216</text>
    <text x="220" y="125" fill="#fcd34d" font-size="14" font-weight="bold" text-anchor="middle">Units = 6</text>
    <!-- Final root -->
    <text x="165" y="145" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Combined Root = 26</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Using the two-group estimation method shown for \(17576\), what is \(\sqrt[3]{17576}\)?</p>
</div>""",
     ["26", "24", "36", "16"],
     "A", "OSC", "easy",
     "The rightmost 3 digits (576) end in 6, so units digit is 6. The remaining group (17) lies between \(2^3=8\) and \(3^3=27\), giving tens digit 2. Hence \(\\sqrt[3]{17576} = 26\)."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Estimation Method for \(\sqrt[3]{110592}\)</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Grouping boxes -->
    <rect x="60" y="20" width="90" height="40" rx="6" fill="#4c1d95" stroke="#8b5cf6" stroke-width="2"/>
    <text x="105" y="46" fill="#ddd6fe" font-size="16" font-weight="bold" text-anchor="middle">110</text>
    <text x="105" y="75" fill="#94a3b8" font-size="10" text-anchor="middle">Group II</text>
    <rect x="175" y="20" width="105" height="40" rx="6" fill="#134e4a" stroke="#14b8a6" stroke-width="2"/>
    <text x="227" y="46" fill="#99f6e4" font-size="16" font-weight="bold" text-anchor="middle">592</text>
    <text x="227" y="75" fill="#94a3b8" font-size="10" text-anchor="middle">Group I</text>
    <!-- Reasoning -->
    <text x="105" y="105" fill="#c4b5fd" font-size="11" text-anchor="middle">4³ = 64 ≤ 110 &lt; 5³ = 125</text>
    <text x="105" y="125" fill="#fde047" font-size="14" font-weight="bold" text-anchor="middle">Tens: 4</text>
    <text x="227" y="105" fill="#5eead4" font-size="11" text-anchor="middle">Ends in 2 ⇒ 8³ = 512</text>
    <text x="227" y="125" fill="#fde047" font-size="14" font-weight="bold" text-anchor="middle">Units: 8</text>
    <text x="166" y="145" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Cube Root = 48</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Applying the two-step estimation method to \(110592\), what is the resulting cube root?</p>
</div>""",
     ["48", "42", "58", "38"],
     "A", "OSC", "easy",
     "Group 1 (592) ends in 2, whose cube root units digit is 8. Group 2 (110) falls between \(4^3=64\) and \(5^3=125\), giving tens digit 4. Thus the cube root is 48."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Cube Roots of Negative Integers on Number Line</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Horizontal Axis -->
    <line x1="30" y1="80" x2="310" y2="80" stroke="#64748b" stroke-width="2"/>
    <!-- Center 0 -->
    <circle cx="170" cy="80" r="5" fill="#f8fafc"/>
    <text x="170" y="105" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">0</text>
    <!-- Positive Cube Root -->
    <circle cx="260" cy="80" r="5" fill="#10b981"/>
    <text x="260" y="65" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">+3 = ∛27</text>
    <text x="260" y="105" fill="#6ee7b7" font-size="11" text-anchor="middle">3³ = +27</text>
    <!-- Negative Cube Root -->
    <circle cx="80" cy="80" r="5" fill="#ef4444"/>
    <text x="80" y="65" fill="#f87171" font-size="12" font-weight="bold" text-anchor="middle">-3 = ∛(-27)</text>
    <text x="80" y="105" fill="#fca5a5" font-size="11" text-anchor="middle">(-3)³ = -27</text>
    <!-- Formula banner -->
    <rect x="70" y="120" width="200" height="25" rx="4" fill="#0f172a" stroke="#475569"/>
    <text x="170" y="137" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">∛(-x) = -∛x</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Based on the reflectional symmetry of cube roots, what is the value of \(\sqrt[3]{-343}\)?</p>
</div>""",
     ["-7", "7", "-49", "49"],
     "A", "OSC", "easy",
     "Because \((-x)^3 = -x^3\), we have \(\\sqrt[3]{-343} = -\\sqrt[3]{343} = -7\)."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Cube Root of Rational Fractions</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Large Fraction Box -->
    <rect x="40" y="25" width="100" height="90" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="90" y="60" fill="#60a5fa" font-size="18" font-weight="bold" text-anchor="middle">216</text>
    <line x1="55" y1="70" x2="125" y2="70" stroke="#94a3b8" stroke-width="3"/>
    <text x="90" y="98" fill="#60a5fa" font-size="18" font-weight="bold" text-anchor="middle">343</text>
    <text x="25" y="75" fill="#f59e0b" font-size="22" font-weight="bold" text-anchor="middle">∛</text>
    <!-- Arrow -->
    <path d="M 155,70 L 195,70" stroke="#f59e0b" stroke-width="3" fill="none"/>
    <polygon points="195,65 205,70 195,75" fill="#f59e0b"/>
    <!-- Separated Radical -->
    <rect x="215" y="25" width="95" height="90" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="262" y="58" fill="#34d399" font-size="16" font-weight="bold" text-anchor="middle">∛216 = 6</text>
    <line x1="230" y1="70" x2="295" y2="70" stroke="#94a3b8" stroke-width="3"/>
    <text x="262" y="98" fill="#34d399" font-size="16" font-weight="bold" text-anchor="middle">∛343 = 7</text>
    <text x="170" y="138" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Result = 6/7</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">By taking the cube root of the numerator and denominator independently, find \(\sqrt[3]{\frac{216}{343}}\).</p>
</div>""",
     ["6/7", "7/6", "36/49", "6/49"],
     "A", "OSC", "easy",
     "\\(\\sqrt[3]{\\frac{216}{343}} = \\frac{\\sqrt[3]{216}}{\\sqrt[3]{343}} = \\frac{6}{7}\\)."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Decimal Cube Roots and Fraction Conversion</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Step 1: Decimal -->
    <rect x="20" y="40" width="80" height="50" rx="6" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="60" y="70" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">0.064</text>
    <!-- Arrow 1 -->
    <text x="115" y="70" fill="#38bdf8" font-size="18" text-anchor="middle">→</text>
    <!-- Step 2: Fraction -->
    <rect x="135" y="30" width="85" height="70" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="177" y="55" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">64</text>
    <line x1="145" y1="65" x2="210" y2="65" stroke="#60a5fa" stroke-width="2"/>
    <text x="177" y="85" fill="#93c5fd" font-size="13" font-weight="bold" text-anchor="middle">1000</text>
    <!-- Arrow 2 -->
    <text x="235" y="70" fill="#38bdf8" font-size="18" text-anchor="middle">→</text>
    <!-- Step 3: Result -->
    <rect x="250" y="30" width="75" height="70" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
    <text x="287" y="55" fill="#6ee7b7" font-size="13" font-weight="bold" text-anchor="middle">4 / 10</text>
    <line x1="260" y1="65" x2="315" y2="65" stroke="#34d399" stroke-width="2"/>
    <text x="287" y="88" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">= 0.4</text>
    <!-- Footer tip -->
    <text x="170" y="132" fill="#fbbf24" font-size="11" text-anchor="middle">3 decimal places in cube ⇒ 1 decimal place in root</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the cube root of \(0.000027\)?</p>
</div>""",
     ["0.03", "0.003", "0.3", "0.0003"],
     "A", "OSC", "medium",
     "\(0.000027 = \\frac{27}{1000000}\). The cube root is \(\\frac{\\sqrt[3]{27}}{\\sqrt[3]{1000000}} = \\frac{3}{100} = 0.03\). Six decimal places reduce to \(6/3 = 2\) decimal places."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Melting Cubes into a Unified Cube</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Small cubes -->
    <rect x="20" y="70" width="25" height="25" fill="#3b82f6" stroke="#60a5fa" stroke-width="1.5"/>
    <text x="32" y="87" fill="#ffffff" font-size="10" text-anchor="middle">3³</text>
    <text x="55" y="87" fill="#94a3b8" font-size="14" text-anchor="middle">+</text>
    <rect x="70" y="60" width="35" height="35" fill="#6366f1" stroke="#818cf8" stroke-width="1.5"/>
    <text x="87" y="82" fill="#ffffff" font-size="11" text-anchor="middle">4³</text>
    <text x="115" y="87" fill="#94a3b8" font-size="14" text-anchor="middle">+</text>
    <rect x="130" y="50" width="45" height="45" fill="#8b5cf6" stroke="#a78bfa" stroke-width="1.5"/>
    <text x="152" y="77" fill="#ffffff" font-size="12" text-anchor="middle">5³</text>
    <!-- Arrow -->
    <path d="M 190,75 L 225,75" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="225,70 235,75 225,80" fill="#f59e0b"/>
    <!-- Large unified cube -->
    <rect x="250" y="40" width="60" height="60" fill="#10b981" stroke="#34d399" stroke-width="2"/>
    <text x="280" y="75" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">S³ = 216</text>
    <!-- Total volume text -->
    <text x="170" y="132" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">27 + 64 + 125 = 216 ⇒ S = ∛216 = 6 cm</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Three metal cubes of edges \(3\text{ cm}\), \(4\text{ cm}\), and \(5\text{ cm}\) are melted to form one cube. What is the edge \(S\) of the new cube?</p>
</div>""",
     ["6 cm", "8 cm", "12 cm", "7 cm"],
     "A", "OSC", "medium",
     "Total volume = \(3^3 + 4^3 + 5^3 = 27 + 64 + 125 = 216\\text{ cm}^3\). The edge of the new cube is \(S = \\sqrt[3]{216} = 6\\text{ cm}\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Finding the Smallest Multiplier to Form a Perfect Cube</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Factor triplets balancing -->
    <text x="170" y="25" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">Factors of 675 = 3³ × 5²</text>
    <!-- Triplet for 3: COMPLETE -->
    <rect x="40" y="45" width="110" height="35" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
    <text x="95" y="67" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">3 × 3 × 3 (Complete)</text>
    <!-- Pair for 5: INCOMPLETE -->
    <rect x="180" y="45" width="120" height="35" rx="6" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
    <text x="240" y="67" fill="#fca5a5" font-size="12" font-weight="bold" text-anchor="middle">5 × 5 × ? (Missing 1)</text>
    <!-- Missing factor indicator -->
    <path d="M 240,90 L 240,110" stroke="#f59e0b" stroke-width="2" marker-end="url(#arr)"/>
    <text x="170" y="132" fill="#fcd34d" font-size="13" font-weight="bold" text-anchor="middle">Multiply by 5 to make 5³ ⇒ ∛(675 × 5) = 15</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">By prime factorisation, \(675 = 3^3 \times 5^2\). What is the smallest natural number by which \(675\) must be multiplied to yield a perfect cube?</p>
</div>""",
     ["5", "3", "25", "15"],
     "A", "OSC", "easy",
     "In \(675 = 3^3 \\times 5^2\), the factor 3 appears in a triplet, while the factor 5 appears only twice. To complete the triplet of 5s, we must multiply by 5. Then \(675 \\times 5 = 3375 = 15^3\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Smallest Divisor to Form a Perfect Cube</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Factors of 192 -->
    <text x="170" y="25" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">Prime Factorisation of 192 = 2⁶ × 3¹</text>
    <!-- 2^6 grouped as two triplets -->
    <rect x="30" y="45" width="90" height="35" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="75" y="67" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">2 × 2 × 2</text>
    <rect x="130" y="45" width="90" height="35" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="175" y="67" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">2 × 2 × 2</text>
    <!-- Unpaired factor 3 -->
    <rect x="235" y="45" width="75" height="35" rx="6" fill="#7f1d1d" stroke="#f87171" stroke-width="2"/>
    <text x="272" y="67" fill="#fca5a5" font-size="12" font-weight="bold" text-anchor="middle">× 3 (Extra)</text>
    <!-- Division action -->
    <text x="170" y="115" fill="#f87171" font-size="12" text-anchor="middle">Divide by 3 to remove the surplus factor</text>
    <text x="170" y="138" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">192 ÷ 3 = 64 = 4³</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the smallest natural number by which \(192\) must be divided so that the quotient is a perfect cube?</p>
</div>""",
     ["3", "2", "6", "4"],
     "A", "OSC", "easy",
     "Prime factors of \(192\) are \(2^6 \\times 3 = (2^2)^3 \\times 3\). The factor 3 is not in a triplet. Dividing by 3 eliminates it, leaving \(64 = 4^3\)."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Cubic Capacity of an Oil Tanker</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- 3D Tank Outline -->
    <polygon points="60,85 130,85 160,55 90,55" fill="#0284c7" opacity="0.7" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="130,85 160,55 160,115 130,145" fill="#0369a1" opacity="0.8" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="60,85 130,85 130,145 60,145" fill="#0ea5e9" stroke="#38bdf8" stroke-width="2"/>
    <text x="95" y="120" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">V = 13824 m³</text>
    <!-- Conversion & Root Card -->
    <rect x="180" y="55" width="140" height="75" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="250" y="78" fill="#94a3b8" font-size="11" text-anchor="middle">Side s = ∛13824</text>
    <text x="250" y="98" fill="#fcd34d" font-size="13" font-weight="bold" text-anchor="middle">Group 1: 824 ⇒ 4</text>
    <text x="250" y="118" fill="#fcd34d" font-size="13" font-weight="bold" text-anchor="middle">Group 2: 13 ⇒ 2</text>
    <text x="250" y="142" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Edge s = 24 m</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">A cubical storage reservoir holds \(13824\text{ m}^3\) of liquid. What is the inner side length of the reservoir?</p>
</div>""",
     ["24 m", "26 m", "22 m", "28 m"],
     "A", "OSC", "easy",
     "The volume \(V = s^3 = 13824\text{ m}^3\). Grouping gives: 824 ends in 4 (so units digit is 4); 13 lies between \(2^3=8\) and \(3^3=27\) (so tens digit is 2). Thus \(s = 24\\text{ m}\)."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Consecutive Integer Bounds on Cube Roots</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Bounding interval -->
    <line x1="40" y1="75" x2="300" y2="75" stroke="#475569" stroke-width="3"/>
    <!-- Left Bound 4^3 = 64 -->
    <circle cx="80" cy="75" r="7" fill="#3b82f6"/>
    <text x="80" y="55" fill="#60a5fa" font-size="13" font-weight="bold" text-anchor="middle">4³ = 64</text>
    <text x="80" y="100" fill="#93c5fd" font-size="12" text-anchor="middle">s = 4</text>
    <!-- Interior target 85 -->
    <circle cx="160" cy="75" r="7" fill="#f59e0b"/>
    <text x="160" y="55" fill="#fbbf24" font-size="14" font-weight="bold" text-anchor="middle">85</text>
    <text x="160" y="100" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">4 &lt; ∛85 &lt; 5</text>
    <!-- Right Bound 5^3 = 125 -->
    <circle cx="260" cy="75" r="7" fill="#10b981"/>
    <text x="260" y="55" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">5³ = 125</text>
    <text x="260" y="100" fill="#6ee7b7" font-size="12" text-anchor="middle">s = 5</text>
    <!-- Footer equation -->
    <text x="170" y="135" fill="#e2e8f0" font-size="11" text-anchor="middle">64 &lt; 85 &lt; 125 ⇒ integer part of ∛85 is 4</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Between which two consecutive integers does \(\sqrt[3]{85}\) lie?</p>
</div>""",
     ["Between 4 and 5", "Between 3 and 4", "Between 5 and 6", "Between 8 and 9"],
     "A", "OSC", "easy",
     "Since \(4^3 = 64\) and \(5^3 = 125\), and \(64 < 85 < 125\), taking cube roots gives \(4 < \\sqrt[3]{85} < 5\).")
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch1_topic6.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
