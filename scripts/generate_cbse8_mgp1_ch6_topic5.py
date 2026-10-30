# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-6-6.5
Topic: Applications of Identities in Numerical Calculations
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-6-6.5"

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
    (r"What is the value of \(103^2\) evaluated using the identity \((a + b)^2 = a^2 + 2ab + b^2\)?",
     ["10,609", "10,909", "10,309", "10,600"],
     "A", "OSC", "easy",
     r"Write \(103^2 = (100 + 3)^2 = 100^2 + 2(100)(3) + 3^2 = 10,000 + 600 + 9 = 10,609\)."),

    # 2
    (r"Evaluate \(99^2\) without direct multiplication using \((a - b)^2\):",
     ["9,801", "9,901", "9,701", "9,810"],
     "A", "OSC", "easy",
     r"Write \(99^2 = (100 - 1)^2 = 100^2 - 2(100)(1) + 1^2 = 10,000 - 200 + 1 = 9,801\)."),

    # 3
    (r"Using the identity \((a + b)(a - b) = a^2 - b^2\), what is the product \(103 \times 97\)?",
     ["9,991", "9,981", "9,999", "9,919"],
     "A", "OSC", "easy",
     r"\(103 \times 97 = (100 + 3)(100 - 3) = 100^2 - 3^2 = 10,000 - 9 = 9,991\)."),

    # 4
    (r"Calculate \(105 \times 106\) using the identity \((x + a)(x + b) = x^2 + (a + b)x + ab\):",
     ["11,130", "11,030", "11,230", "11,120"],
     "A", "OSC", "medium",
     r"Here \(x = 100, a = 5, b = 6\). Then \((100+5)(100+6) = 100^2 + (5+6)100 + 5 \times 6 = 10,000 + 1,100 + 30 = 11,130\)."),

    # 5
    (r"Evaluate \(5.2^2\) using an algebraic identity:",
     ["27.04", "26.04", "27.40", "25.04"],
     "A", "OSC", "medium",
     r"\(5.2^2 = (5 + 0.2)^2 = 5^2 + 2(5)(0.2) + 0.2^2 = 25 + 2.0 + 0.04 = 27.04\)."),

    # 6
    (r"Evaluate \(9.8^2\) using an algebraic identity:",
     ["96.04", "96.40", "98.04", "95.04"],
     "A", "OSC", "medium",
     r"\(9.8^2 = (10 - 0.2)^2 = 10^2 - 2(10)(0.2) + 0.2^2 = 100 - 4.0 + 0.04 = 96.04\)."),

    # 7
    (r"Compute \(51^2 - 49^2\) without squaring each number:",
     ["200", "100", "400", "2"],
     "A", "OSC", "easy",
     r"Using \(a^2 - b^2 = (a + b)(a - b)\): \(51^2 - 49^2 = (51 + 49)(51 - 49) = 100 \times 2 = 200\)."),

    # 8
    (r"Evaluate \(1.02 \times 0.98\) using the difference of squares identity:",
     ["0.9996", "0.9992", "0.9984", "0.9960"],
     "A", "OSC", "medium",
     r"\(1.02 \times 0.98 = (1 + 0.02)(1 - 0.02) = 1^2 - (0.02)^2 = 1 - 0.0004 = 0.9996\)."),

    # 9
    (r"What is the value of \(297 \times 303\)?",
     ["89,991", "89,919", "89,999", "89,901"],
     "A", "OSC", "easy",
     r"\(297 \times 303 = (300 - 3)(300 + 3) = 300^2 - 3^2 = 90,000 - 9 = 89,991\)."),

    # 10
    (r"Evaluate \(78 \times 82\) using an identity:",
     ["6,396", "6,384", "6,404", "6,296"],
     "A", "OSC", "easy",
     r"\(78 \times 82 = (80 - 2)(80 + 2) = 80^2 - 2^2 = 6,400 - 4 = 6,396\)."),

    # 11
    (r"Evaluate \(8.9^2\) using \((a - b)^2\):",
     ["79.21", "79.12", "80.21", "78.21"],
     "A", "OSC", "medium",
     r"\(8.9^2 = (9 - 0.1)^2 = 9^2 - 2(9)(0.1) + 0.1^2 = 81 - 1.8 + 0.01 = 79.21\)."),

    # 12
    (r"Calculate \(10.5 \times 9.5\) using \((a + b)(a - b)\):",
     ["99.75", "99.25", "100.25", "98.75"],
     "A", "OSC", "medium",
     r"\(10.5 \times 9.5 = (10 + 0.5)(10 - 0.5) = 10^2 - (0.5)^2 = 100 - 0.25 = 99.75\)."),

    # 13
    (r"Find the product \(95 \times 96\) using \((x + a)(x + b)\) with base 100:",
     ["9,120", "9,110", "9,220", "9,020"],
     "A", "OSC", "medium",
     r"\(95 \times 96 = (100 - 5)(100 - 4) = 100^2 + (-5 - 4)100 + (-5)(-4) = 10,000 - 900 + 20 = 9,120\)."),

    # 14
    (r"Find the product \(104 \times 96\) using an algebraic identity:",
     ["9,984", "9,974", "9,994", "9,884"],
     "A", "OSC", "easy",
     r"\(104 \times 96 = (100 + 4)(100 - 4) = 100^2 - 4^2 = 10,000 - 16 = 9,984\)."),

    # 15
    (r"Evaluate \(153^2 - 147^2\):",
     ["1,800", "1,600", "2,000", "900"],
     "A", "OSC", "easy",
     r"\(153^2 - 147^2 = (153 + 147)(153 - 147) = 300 \times 6 = 1,800\)."),

    # 16
    (r"Evaluate \(12.1^2 - 7.9^2\):",
     ["84", "84.2", "80", "88"],
     "A", "OSC", "medium",
     r"\(12.1^2 - 7.9^2 = (12.1 + 7.9)(12.1 - 7.9) = 20 \times 4.2 = 84\)."),

    # 17
    (r"Evaluate \(\frac{198 \times 198 - 102 \times 102}{96}\):",
     ["300", "200", "96", "400"],
     "A", "OSC", "medium",
     r"Numerator is \(198^2 - 102^2 = (198 + 102)(198 - 102) = 300 \times 96\). Dividing by 96 gives 300."),

    # 18
    (r"If \(4x = 52^2 - 48^2\), find the value of \(x\):",
     ["100", "200", "50", "400"],
     "A", "OSC", "medium",
     r"\(4x = (52 + 48)(52 - 48) = 100 \times 4 = 400 \implies x = \frac{400}{4} = 100\)."),

    # 19
    (r"If \(5x = 73^2 - 27^2\), what is \(x\)?",
     ["920", "460", "1,000", "184"],
     "A", "OSC", "medium",
     r"\(5x = (73 + 27)(73 - 27) = 100 \times 46 = 4,600 \implies x = \frac{4,600}{5} = 920\)."),

    # 20
    (r"Evaluate \(1,002^2\) without actual multiplication:",
     ["1,004,004", "1,004,040", "1,002,004", "1,000,404"],
     "A", "OSC", "medium",
     r"\(1,002^2 = (1,000 + 2)^2 = 1,000^2 + 2(1,000)(2) + 2^2 = 1,000,000 + 4,000 + 4 = 1,004,004\)."),

    # 21
    (r"Evaluate \(999^2\) using an identity:",
     ["998,001", "999,001", "997,001", "998,100"],
     "A", "OSC", "medium",
     r"\(999^2 = (1,000 - 1)^2 = 1,000^2 - 2(1,000)(1) + 1^2 = 1,000,000 - 2,000 + 1 = 998,001\)."),

    # 22
    (r"Find the product \(201 \times 199\):",
     ["39,999", "39,991", "40,001", "39,901"],
     "A", "OSC", "easy",
     r"\(201 \times 199 = (200 + 1)(200 - 1) = 200^2 - 1^2 = 40,000 - 1 = 39,999\)."),

    # 23
    (r"Evaluate \(501 \times 502\) using \((x + a)(x + b)\):",
     ["251,502", "251,002", "250,502", "252,502"],
     "A", "OSC", "hard",
     r"\((500 + 1)(500 + 2) = 500^2 + (1 + 2)500 + 1 \times 2 = 250,000 + 1,500 + 2 = 251,502\)."),

    # 24
    (r"Which identity is best suited to compute \(103 \times 98\)?",
     [r"\((x + a)(x + b) = x^2 + (a + b)x + ab\) with \(x = 100, a = 3, b = -2\)",
      r"\((a + b)^2 = a^2 + 2ab + b^2\)",
      r"\((a - b)^2 = a^2 - 2ab + b^2\)",
      r"\((a + b)(a - b) = a^2 - b^2\)"],
     "A", "OSC", "medium",
     r"Since 103 is \(100 + 3\) and 98 is \(100 - 2\), the terms added to 100 are different (\(+3\) and \(-2\)), so \((x + a)(x + b)\) is the exact match."),

    # 25
    (r"Using \((x + a)(x + b)\), what is \(103 \times 98\)?",
     ["10,094", "10,104", "10,084", "9,994"],
     "A", "OSC", "medium",
     r"\((100 + 3)(100 - 2) = 100^2 + (3 - 2)100 + (3)(-2) = 10,000 + 100 - 6 = 10,094\)."),

    # 26
    (r"Evaluate \(71^2\) using \((a + b)^2\):",
     ["5,041", "5,021", "4,941", "5,141"],
     "A", "OSC", "easy",
     r"\(71^2 = (70 + 1)^2 = 70^2 + 2(70)(1) + 1^2 = 4,900 + 140 + 1 = 5,041\)."),

    # 27
    (r"Evaluate \(69^2\) using \((a - b)^2\):",
     ["4,761", "4,741", "4,861", "4,661"],
     "A", "OSC", "easy",
     r"\(69^2 = (70 - 1)^2 = 70^2 - 2(70)(1) + 1^2 = 4,900 - 140 + 1 = 4,761\)."),

    # 28
    (r"Evaluate \(\frac{7.83 \times 7.83 - 1.17 \times 1.17}{6.66}\):",
     ["9.00", "6.66", "8.00", "7.83"],
     "A", "OSC", "medium",
     r"The numerator is \(a^2 - b^2 = (7.83 + 1.17)(7.83 - 1.17) = 9.00 \times 6.66\). Dividing by 6.66 gives 9.00."),

    # 29
    (r"What is the value of \(194 \times 206\)?",
     ["39,964", "39,974", "39,954", "39,864"],
     "A", "OSC", "easy",
     r"\(194 \times 206 = (200 - 6)(200 + 6) = 200^2 - 6^2 = 40,000 - 36 = 39,964\)."),

    # 30
    (r"Evaluate \(1.05 \times 9.5\) rewritten as \(\frac{1}{10}(105 \times 95)\):",
     ["9.975", "9.925", "10.025", "9.875"],
     "A", "OSC", "medium",
     r"\(105 \times 95 = (100 + 5)(100 - 5) = 10,000 - 25 = 9,975\). Dividing by 1,000 (from \(1.05 \times 9.5\)) gives \(9.975\)."),

    # 31
    (r"True or False: The numerical identity \((100 + 1)^2 = 100^2 + 1^2 = 10,001\) is correct.",
     ["False, the cross-term \(2(100)(1) = 200\) must be added, yielding 10,201", "True, squaring each term independently is valid", "False, the result is 10,101", "True, because 1 squared is 1"],
     "A", "OTF", "easy",
     r"\((a + b)^2 = a^2 + 2ab + b^2\). For \(101^2\), omitting \(2ab = 200\) gives an incorrect answer. The correct value is 10,201."),

    # 32
    (r"Evaluate \(10.2 \times 9.8\) using \((a + b)(a - b)\):",
     ["99.96", "99.84", "99.92", "100.04"],
     "A", "OSC", "medium",
     r"\((10 + 0.2)(10 - 0.2) = 10^2 - 0.2^2 = 100 - 0.04 = 99.96\)."),

    # 33
    (r"Find the value of \(m\) if \(12m = 61^2 - 49^2\):",
     ["110", "120", "100", "220"],
     "A", "OSC", "medium",
     r"\(61^2 - 49^2 = (61 + 49)(61 - 49) = 110 \times 12\). Thus \(12m = 110 \times 12 \implies m = 110\)."),

    # 34
    (r"Which of the following equals \((50 + 2)(50 - 2)\)?",
     ["2,496", "2,504", "2,500", "2,492"],
     "A", "OSC", "easy",
     r"\((50 + 2)(50 - 2) = 50^2 - 2^2 = 2,500 - 4 = 2,496\)."),

    # 35
    (r"Assertion (A): \(105 \times 95\) can be evaluated in one step without long multiplication.\nReason (R): It can be expressed as \((100 + 5)(100 - 5) = 100^2 - 5^2\).",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "medium",
     r"Expressing symmetric factors around 100 as \((100 + 5)(100 - 5)\) allows immediate evaluation using Identity III (\(a^2 - b^2\)), so both A and R are true, and R explains A."),

    # 36
    (r"Fill in the blank: \(102 \times 103 = 100^2 + (2 + 3)100 + ______ = 10,506\).",
     ["6", "5", "10", "12"],
     "A", "OFB", "easy",
     r"In \((x + a)(x + b) = x^2 + (a + b)x + ab\), the last term is \(a \times b = 2 \times 3 = 6\)."),

    # 37
    (r"Evaluate \(9.7 \times 9.7\) using \((10 - 0.3)^2\):",
     ["94.09", "94.90", "95.09", "93.09"],
     "A", "OSC", "medium",
     r"\((10 - 0.3)^2 = 10^2 - 2(10)(0.3) + (0.3)^2 = 100 - 6.0 + 0.09 = 94.09\)."),

    # 38
    (r"Evaluate \(0.54 \times 0.54 - 0.46 \times 0.46\):",
     ["0.08", "0.80", "0.008", "0.10"],
     "A", "OSC", "hard",
     r"\(0.54^2 - 0.46^2 = (0.54 + 0.46)(0.54 - 0.46) = 1.00 \times 0.08 = 0.08\)."),

    # 39
    (r"Evaluate \((300 + 4)^2 - (300 - 4)^2\):",
     ["4,800", "9,600", "2,400", "1,200"],
     "A", "OSC", "hard",
     r"Using \((a + b)^2 - (a - b)^2 = 4ab\): here \(a = 300, b = 4\), so \(4(300)(4) = 4,800\)."),

    # 40
    (r"Find the value of \(67^2 - 33^2\):",
     ["3,400", "3,300", "3,500", "3,200"],
     "A", "OSC", "easy",
     r"\(67^2 - 33^2 = (67 + 33)(67 - 33) = 100 \times 34 = 3,400\)."),
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    (r"Evaluate \(104^2\) using \((a + b)^2\):",
     ["10,816", "10,806", "10,916", "10,416"],
     "A", "OSC", "easy",
     r"\(104^2 = (100 + 4)^2 = 100^2 + 2(100)(4) + 4^2 = 10,000 + 800 + 16 = 10,816\)."),

    # 42
    (r"Evaluate \(98^2\) using \((a - b)^2\):",
     ["9,604", "9,614", "9,704", "9,804"],
     "A", "OSC", "easy",
     r"\(98^2 = (100 - 2)^2 = 100^2 - 2(100)(2) + 2^2 = 10,000 - 400 + 4 = 9,604\)."),

    # 43
    (r"Evaluate \(102 \times 98\) using \((a + b)(a - b)\):",
     ["9,996", "9,986", "9,976", "9,994"],
     "A", "OSC", "easy",
     r"\(102 \times 98 = (100 + 2)(100 - 2) = 100^2 - 2^2 = 10,000 - 4 = 9,996\)."),

    # 44
    (r"Evaluate \(103 \times 105\) using \((x + a)(x + b)\):",
     ["10,815", "10,825", "10,715", "10,915"],
     "A", "OSC", "medium",
     r"\((100 + 3)(100 + 5) = 100^2 + (3 + 5)100 + 3 \times 5 = 10,000 + 800 + 15 = 10,815\)."),

    # 45
    (r"Find \(53^2 - 47^2\) using difference of squares:",
     ["600", "500", "700", "300"],
     "A", "OSC", "easy",
     r"\(53^2 - 47^2 = (53 + 47)(53 - 47) = 100 \times 6 = 600\)."),

    # 46
    (r"Evaluate \(4.1^2\) using an identity:",
     ["16.81", "16.41", "17.81", "16.01"],
     "A", "OSC", "medium",
     r"\(4.1^2 = (4 + 0.1)^2 = 4^2 + 2(4)(0.1) + 0.1^2 = 16 + 0.8 + 0.01 = 16.81\)."),

    # 47
    (r"Evaluate \(3.9^2\) using an identity:",
     ["15.21", "15.12", "15.81", "14.81"],
     "A", "OSC", "medium",
     r"\(3.9^2 = (4 - 0.1)^2 = 4^2 - 2(4)(0.1) + 0.1^2 = 16 - 0.8 + 0.01 = 15.21\)."),

    # 48
    (r"Evaluate \(48 \times 52\) using \((a - b)(a + b)\):",
     ["2,496", "2,486", "2,504", "2,396"],
     "A", "OSC", "easy",
     r"\(48 \times 52 = (50 - 2)(50 + 2) = 50^2 - 2^2 = 2,500 - 4 = 2,496\)."),

    # 49
    (r"Compute \(97 \times 98\) using \((x + a)(x + b)\) with \(x = 100\):",
     ["9,506", "9,516", "9,406", "9,606"],
     "A", "OSC", "medium",
     r"\((100 - 3)(100 - 2) = 100^2 + (-3 - 2)100 + (-3)(-2) = 10,000 - 500 + 6 = 9,506\)."),

    # 50
    (r"Calculate \(202^2\) using identity \((a + b)^2\):",
     ["40,804", "40,404", "40,840", "40,604"],
     "A", "OSC", "medium",
     r"\(202^2 = (200 + 2)^2 = 200^2 + 2(200)(2) + 2^2 = 40,000 + 800 + 4 = 40,804\)."),

    # 51
    (r"Evaluate \(198^2\) using identity \((a - b)^2\):",
     ["39,204", "39,404", "39,240", "39,104"],
     "A", "OSC", "medium",
     r"\(198^2 = (200 - 2)^2 = 200^2 - 2(200)(2) + 2^2 = 40,000 - 800 + 4 = 39,204\)."),

    # 52
    (r"Evaluate \(2.03 \times 1.97\) using \((a + b)(a - b)\):",
     ["3.9991", "3.9919", "4.0009", "3.9891"],
     "A", "OSC", "hard",
     r"\(2.03 \times 1.97 = (2 + 0.03)(2 - 0.03) = 2^2 - (0.03)^2 = 4 - 0.0009 = 3.9991\)."),

    # 53
    (r"What is the value of \(85^2 - 15^2\)?",
     ["7,000", "6,800", "7,200", "5,000"],
     "A", "OSC", "easy",
     r"\(85^2 - 15^2 = (85 + 15)(85 - 15) = 100 \times 70 = 7,000\)."),

    # 54
    (r"Solve for \(k\) if \(8k = 54^2 - 46^2\):",
     ["100", "50", "200", "80"],
     "A", "OSC", "medium",
     r"\(54^2 - 46^2 = (54 + 46)(54 - 46) = 100 \times 8 = 800 \implies 8k = 800 \implies k = 100\)."),

    # 55
    (r"Evaluate \(\frac{88 \times 88 - 12 \times 12}{76}\):",
     ["100", "76", "88", "120"],
     "A", "OSC", "easy",
     r"Numerator is \(88^2 - 12^2 = (88 + 12)(88 - 12) = 100 \times 76\). Dividing by 76 yields 100."),

    # 56
    (r"Evaluate \(101 \times 102\) using \((x + a)(x + b)\):",
     ["10,302", "10,202", "10,402", "10,102"],
     "A", "OSC", "easy",
     r"\((100 + 1)(100 + 2) = 100^2 + (1 + 2)100 + 1 \times 2 = 10,000 + 300 + 2 = 10,302\)."),

    # 57
    (r"Evaluate \(99 \times 101\) using \((a - b)(a + b)\):",
     ["9,999", "9,989", "9,991", "10,001"],
     "A", "OSC", "easy",
     r"\(99 \times 101 = (100 - 1)(100 + 1) = 100^2 - 1^2 = 10,000 - 1 = 9,999\)."),

    # 58
    (r"Evaluate \(498^2\) using \((500 - 2)^2\):",
     ["248,004", "248,040", "249,004", "247,004"],
     "A", "OSC", "hard",
     r"\(498^2 = (500 - 2)^2 = 500^2 - 2(500)(2) + 2^2 = 250,000 - 2,000 + 4 = 248,004\)."),

    # 59
    (r"Evaluate \(502^2\) using \((500 + 2)^2\):",
     ["252,004", "252,040", "251,004", "250,004"],
     "A", "OSC", "hard",
     r"\(502^2 = (500 + 2)^2 = 500^2 + 2(500)(2) + 2^2 = 250,000 + 2,000 + 4 = 252,004\)."),

    # 60
    (r"Compute \(9.5^2\) using \((10 - 0.5)^2\):",
     ["90.25", "90.50", "91.25", "89.25"],
     "A", "OSC", "medium",
     r"\(9.5^2 = (10 - 0.5)^2 = 100 - 2(10)(0.5) + 0.25 = 100 - 10 + 0.25 = 90.25\)."),

    # 61
    (r"Compute \(10.5^2\) using \((10 + 0.5)^2\):",
     ["110.25", "110.50", "111.25", "109.25"],
     "A", "OSC", "medium",
     r"\(10.5^2 = (10 + 0.5)^2 = 100 + 2(10)(0.5) + 0.25 = 100 + 10 + 0.25 = 110.25\)."),

    # 62
    (r"Evaluate \(107 \times 93\):",
     ["9,951", "9,941", "9,961", "9,851"],
     "A", "OSC", "easy",
     r"\(107 \times 93 = (100 + 7)(100 - 7) = 100^2 - 7^2 = 10,000 - 49 = 9,951\)."),

    # 63
    (r"Evaluate \(56^2 - 44^2\):",
     ["1,200", "1,000", "1,400", "1,100"],
     "A", "OSC", "easy",
     r"\(56^2 - 44^2 = (56 + 44)(56 - 44) = 100 \times 12 = 1,200\)."),

    # 64
    (r"If \(16x = 58^2 - 42^2\), what is the value of \(x\)?",
     ["100", "50", "200", "150"],
     "A", "OSC", "medium",
     r"\(58^2 - 42^2 = (58 + 42)(58 - 42) = 100 \times 16 = 1,600 \implies x = \frac{1,600}{16} = 100\)."),

    # 65
    (r"Evaluate \((50 + 1)^2 - (50 - 1)^2\):",
     ["200", "100", "400", "50"],
     "A", "OSC", "medium",
     r"Using \((a + b)^2 - (a - b)^2 = 4ab\): here \(a = 50, b = 1\), so \(4(50)(1) = 200\)."),

    # 66
    (r"Evaluate \((100 + 5)^2 + (100 - 5)^2\):",
     ["20,050", "20,100", "20,025", "20,000"],
     "A", "OSC", "hard",
     r"Using \((a + b)^2 + (a - b)^2 = 2(a^2 + b^2)\): here \(2(100^2 + 5^2) = 2(10,000 + 25) = 2(10,025) = 20,050\)."),

    # 67
    (r"Find the value of \(106 \times 94\):",
     ["9,964", "9,974", "9,954", "9,864"],
     "A", "OSC", "easy",
     r"\(106 \times 94 = (100 + 6)(100 - 6) = 10,000 - 36 = 9,964\)."),

    # 68
    (r"Evaluate \(995^2\) using \((1000 - 5)^2\):",
     ["990,025", "990,050", "995,025", "989,025"],
     "A", "OSC", "hard",
     r"\(995^2 = (1,000 - 5)^2 = 1,000^2 - 2(1,000)(5) + 5^2 = 1,000,000 - 10,000 + 25 = 990,025\)."),

    # 69
    (r"Evaluate \(1,005^2\) using \((1000 + 5)^2\):",
     ["1,010,025", "1,010,050", "1,005,025", "1,009,025"],
     "A", "OSC", "hard",
     r"\(1,005^2 = (1,000 + 5)^2 = 1,000^2 + 2(1,000)(5) + 5^2 = 1,000,000 + 10,000 + 25 = 1,010,025\)."),

    # 70
    (r"Find the value of \(\frac{6.5 \times 6.5 - 3.5 \times 3.5}{3.0}\):",
     ["10.0", "3.0", "6.5", "13.0"],
     "A", "OSC", "medium",
     r"Numerator is \(6.5^2 - 3.5^2 = (6.5 + 3.5)(6.5 - 3.5) = 10.0 \times 3.0\). Dividing by 3.0 gives 10.0."),
]

# 12 MOCK/FOUNDATION QUESTIONS (71-82) WITH DARK VECTOR SVGs
mock_data = [
    # 71
    (r"The diagram below visualizes the expansion of \(102^2\) into four sub-regions using \((100 + 2)^2\). What is the total sum of all four areas?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 260" width="100%" height="220">
  <rect width="440" height="260" fill="#0f172a" rx="10"/>
  <rect x="50" y="30" width="180" height="180" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="140" y="125" fill="#38bdf8" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">100 × 100</text>
  <text x="140" y="145" fill="#94a3b8" font-size="13" font-family="sans-serif" text-anchor="middle">= 10,000</text>
  <rect x="230" y="30" width="40" height="180" fill="#334155" stroke="#f59e0b" stroke-width="2"/>
  <text x="250" y="125" fill="#f59e0b" font-size="12" font-family="sans-serif" text-anchor="middle" transform="rotate(90, 250, 125)">100 × 2 = 200</text>
  <rect x="50" y="210" width="180" height="40" fill="#334155" stroke="#f59e0b" stroke-width="2"/>
  <text x="140" y="235" fill="#f59e0b" font-size="13" font-family="sans-serif" text-anchor="middle">2 × 100 = 200</text>
  <rect x="230" y="210" width="40" height="40" fill="#1e3a5f" stroke="#10b981" stroke-width="2"/>
  <text x="250" y="235" fill="#10b981" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">2² = 4</text>
  <text x="350" y="120" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Total Area:</text>
  <text x="350" y="145" fill="#38bdf8" font-size="14" font-family="sans-serif" text-anchor="middle">10,000 + 400 + 4</text>
  <text x="350" y="170" fill="#4ade80" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">= 10,404</text>
</svg>""",
     ["10,404", "10,204", "10,440", "10,004"],
     "A", "OSC", "easy",
     r"The visual geometric decomposition of \((100 + 2)^2\) sums the main square \(10,000\), two rectangles \(200 + 200 = 400\), and the small corner square \(4\), giving exactly 10,404."),

    # 72
    (r"Refer to the geometric breakdown of \(103 \times 97\) as difference of squares \((100 + 3)(100 - 3)\). What is the calculated value?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 240" width="100%" height="200">
  <rect width="440" height="240" fill="#0f172a" rx="10"/>
  <rect x="40" y="30" width="180" height="180" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="130" y="125" fill="#38bdf8" font-size="15" font-family="sans-serif" text-anchor="middle">Big Square: 100² = 10,000</text>
  <rect x="180" y="30" width="40" height="40" fill="#dc2626" fill-opacity="0.5" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="200" y="55" fill="#fca5a5" font-size="11" font-family="sans-serif" text-anchor="middle">Cut 3² = 9</text>
  <path d="M 240 120 L 280 120" stroke="#f8fafc" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="350" y="90" fill="#94a3b8" font-size="13" font-family="sans-serif" text-anchor="middle">Formula:</text>
  <text x="350" y="115" fill="#38bdf8" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">100² - 3²</text>
  <text x="350" y="145" fill="#94a3b8" font-size="13" font-family="sans-serif" text-anchor="middle">= 10,000 - 9</text>
  <text x="350" y="175" fill="#4ade80" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">= 9,991</text>
</svg>""",
     ["9,991", "9,981", "9,999", "9,919"],
     "A", "OSC", "easy",
     r"The geometric difference of squares cuts a \(3 \times 3\) corner from the \(100 \times 100\) square: \(10,000 - 9 = 9,991\)."),

    # 73
    (r"The diagram below demonstrates using \((x + a)(x + b)\) to compute \(104 \times 103\). What is the total evaluated product?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 240" width="100%" height="200">
  <rect width="440" height="240" fill="#0f172a" rx="10"/>
  <g transform="translate(30, 30)">
    <rect x="0" y="0" width="140" height="140" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="70" y="75" fill="#38bdf8" font-size="13" font-family="sans-serif" text-anchor="middle">100² = 10,000</text>
    <rect x="140" y="0" width="50" height="140" fill="#334155" stroke="#f59e0b" stroke-width="2"/>
    <text x="165" y="75" fill="#f59e0b" font-size="11" font-family="sans-serif" text-anchor="middle" transform="rotate(90, 165, 75)">4 × 100 = 400</text>
    <rect x="0" y="140" width="140" height="40" fill="#334155" stroke="#f59e0b" stroke-width="2"/>
    <text x="70" y="165" fill="#f59e0b" font-size="12" font-family="sans-serif" text-anchor="middle">3 × 100 = 300</text>
    <rect x="140" y="140" width="50" height="40" fill="#1e3a5f" stroke="#10b981" stroke-width="2"/>
    <text x="165" y="165" fill="#10b981" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">4 × 3 = 12</text>
  </g>
  <text x="330" y="100" fill="#f8fafc" font-size="14" font-family="sans-serif" text-anchor="middle">Sum of 4 regions:</text>
  <text x="330" y="125" fill="#94a3b8" font-size="13" font-family="sans-serif" text-anchor="middle">10,000 + 700 + 12</text>
  <text x="330" y="155" fill="#4ade80" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">= 10,712</text>
</svg>""",
     ["10,712", "10,702", "10,812", "10,612"],
     "A", "OSC", "easy",
     r"\((100 + 4)(100 + 3) = 100^2 + (4 + 3)100 + 4 \times 3 = 10,000 + 700 + 12 = 10,712\)."),

    # 74
    (r"Examine the illustrated identity for evaluating \(98^2 = (100 - 2)^2\). What is the step-by-step result?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="180">
  <rect width="440" height="220" fill="#0f172a" rx="10"/>
  <rect x="30" y="30" width="380" height="160" fill="#1e293b" rx="8" stroke="#334155" stroke-width="2"/>
  <text x="50" y="65" fill="#38bdf8" font-size="14" font-family="sans-serif" font-weight="bold">Step 1: Express as difference from 100</text>
  <text x="70" y="90" fill="#94a3b8" font-size="13" font-family="sans-serif">98² = (100 - 2)²</text>
  <text x="50" y="125" fill="#f59e0b" font-size="14" font-family="sans-serif" font-weight="bold">Step 2: Expand using (a - b)² = a² - 2ab + b²</text>
  <text x="70" y="150" fill="#94a3b8" font-size="13" font-family="sans-serif">= 10,000 - 400 + 4</text>
  <text x="50" y="175" fill="#4ade80" font-size="15" font-family="sans-serif" font-weight="bold">Result: 9,604</text>
</svg>""",
     ["9,604", "9,614", "9,704", "9,804"],
     "A", "OSC", "easy",
     r"\(100^2 - 2(100)(2) + 2^2 = 10,000 - 400 + 4 = 9,604\)."),

    # 75
    (r"The vector diagram shows the evaluation of difference of squares \(51^2 - 49^2\). What is the final calculated value?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="180">
  <rect width="440" height="220" fill="#0f172a" rx="10"/>
  <circle cx="90" cy="110" r="50" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="90" y="105" fill="#38bdf8" font-size="13" font-family="sans-serif" text-anchor="middle">Sum</text>
  <text x="90" y="125" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">51 + 49 = 100</text>
  <text x="170" y="115" fill="#f59e0b" font-size="20" font-family="sans-serif" font-weight="bold" text-anchor="middle">×</text>
  <circle cx="250" cy="110" r="50" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  <text x="250" y="105" fill="#10b981" font-size="13" font-family="sans-serif" text-anchor="middle">Diff</text>
  <text x="250" y="125" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">51 - 49 = 2</text>
  <text x="330" y="115" fill="#f8fafc" font-size="20" font-family="sans-serif" font-weight="bold" text-anchor="middle">=</text>
  <rect x="360" y="80" width="60" height="60" fill="#1e3a5f" stroke="#38bdf8" stroke-width="2" rx="6"/>
  <text x="390" y="115" fill="#4ade80" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">200</text>
</svg>""",
     ["200", "100", "400", "2"],
     "A", "OSC", "easy",
     r"\(a^2 - b^2 = (a + b)(a - b) = (51 + 49)(51 - 49) = 100 \times 2 = 200\)."),

    # 76
    (r"What is the value of \(1.03 \times 0.97\) represented in the diagram below?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="180">
  <rect width="440" height="220" fill="#0f172a" rx="10"/>
  <rect x="40" y="40" width="360" height="140" fill="#1e293b" rx="8" stroke="#38bdf8" stroke-width="2"/>
  <text x="220" y="75" fill="#38bdf8" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">(1 + 0.03)(1 - 0.03) = 1² - (0.03)²</text>
  <text x="220" y="110" fill="#94a3b8" font-size="14" font-family="sans-serif" text-anchor="middle">= 1 - 0.0009</text>
  <text x="220" y="145" fill="#4ade80" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="middle">= 0.9991</text>
</svg>""",
     ["0.9991", "0.9919", "0.9999", "0.9981"],
     "A", "OSC", "medium",
     r"\(1^2 - (0.03)^2 = 1 - 0.0009 = 0.9991\)."),

    # 77
    (r"The diagram illustrates the mental calculation of \(72 \times 68\) using \((70 + 2)(70 - 2)\). What is the product?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="180">
  <rect width="440" height="220" fill="#0f172a" rx="10"/>
  <rect x="50" y="30" width="340" height="160" fill="#1e293b" rx="8" stroke="#f59e0b" stroke-width="2"/>
  <text x="220" y="70" fill="#f59e0b" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">Base 70 Decomposition</text>
  <text x="220" y="105" fill="#38bdf8" font-size="14" font-family="sans-serif" text-anchor="middle">70² - 2² = 4,900 - 4</text>
  <text x="220" y="145" fill="#4ade80" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="middle">= 4,896</text>
</svg>""",
     ["4,896", "4,886", "4,904", "4,796"],
     "A", "OSC", "easy",
     r"\(70^2 - 2^2 = 4,900 - 4 = 4,896\)."),

    # 78
    (r"What is the area of the green remaining region in the difference of squares model below?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 240" width="100%" height="200">
  <rect width="440" height="240" fill="#0f172a" rx="10"/>
  <rect x="50" y="30" width="180" height="180" fill="#10b981" fill-opacity="0.3" stroke="#10b981" stroke-width="2"/>
  <rect x="170" y="30" width="60" height="60" fill="#ef4444" fill-opacity="0.6" stroke="#ef4444" stroke-width="2"/>
  <text x="200" y="65" fill="#ffffff" font-size="12" font-family="sans-serif" text-anchor="middle">Cut: 6² = 36</text>
  <text x="110" y="130" fill="#10b981" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Outer: 56²</text>
  <text x="330" y="100" fill="#f8fafc" font-size="14" font-family="sans-serif" text-anchor="middle">Area = 56² - 6²</text>
  <text x="330" y="125" fill="#94a3b8" font-size="13" font-family="sans-serif" text-anchor="middle">= (56 + 6)(56 - 6)</text>
  <text x="330" y="150" fill="#94a3b8" font-size="13" font-family="sans-serif" text-anchor="middle">= 62 × 50</text>
  <text x="330" y="180" fill="#4ade80" font-size="17" font-family="sans-serif" font-weight="bold" text-anchor="middle">= 3,100</text>
</svg>""",
     ["3,100", "3,136", "3,064", "3,200"],
     "A", "OSC", "medium",
     r"\(56^2 - 6^2 = (56 + 6)(56 - 6) = 62 \times 50 = 3,100\)."),

    # 79
    (r"Based on the flow diagram for calculating \(9.9^2\), what is the final decimal result?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="180">
  <rect width="440" height="220" fill="#0f172a" rx="10"/>
  <rect x="30" y="40" width="110" height="60" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="6"/>
  <text x="85" y="75" fill="#38bdf8" font-size="13" font-family="sans-serif" text-anchor="middle">(10 - 0.1)²</text>
  <path d="M 140 70 L 175 70" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>
  <rect x="180" y="40" width="120" height="60" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="6"/>
  <text x="240" y="65" fill="#f59e0b" font-size="12" font-family="sans-serif" text-anchor="middle">100 - 2(1) + 0.01</text>
  <text x="240" y="85" fill="#94a3b8" font-size="12" font-family="sans-serif" text-anchor="middle">= 100 - 2 + 0.01</text>
  <path d="M 300 70 L 335 70" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>
  <rect x="340" y="40" width="80" height="60" fill="#1e3a5f" stroke="#10b981" stroke-width="2" rx="6"/>
  <text x="380" y="75" fill="#4ade80" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">98.01</text>
  <text x="220" y="160" fill="#94a3b8" font-size="13" font-family="sans-serif" text-anchor="middle">Identity: (a - b)² = a² - 2ab + b²</text>
</svg>""",
     ["98.01", "98.10", "99.01", "97.01"],
     "A", "OSC", "easy",
     r"\(9.9^2 = (10 - 0.1)^2 = 100 - 2 + 0.01 = 98.01\)."),

    # 80
    (r"What is the evaluated value of the product \(105 \times 95\) shown in the card below?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 200" width="100%" height="160">
  <rect width="440" height="200" fill="#0f172a" rx="10"/>
  <rect x="40" y="30" width="360" height="140" fill="#1e293b" rx="8" stroke="#a855f7" stroke-width="2"/>
  <text x="220" y="70" fill="#c084fc" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">Symmetric Product: 105 × 95</text>
  <text x="220" y="105" fill="#f8fafc" font-size="14" font-family="sans-serif" text-anchor="middle">(100 + 5)(100 - 5) = 100² - 5²</text>
  <text x="220" y="140" fill="#4ade80" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="middle">= 10,000 - 25 = 9,975</text>
</svg>""",
     ["9,975", "9,985", "9,965", "9,925"],
     "A", "OSC", "easy",
     r"\(100^2 - 5^2 = 10,000 - 25 = 9,975\)."),

    # 81
    (r"The balance scale below equates \(4x\) to \(52^2 - 48^2\). What is the balance value of \(x\)?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="180">
  <rect width="440" height="220" fill="#0f172a" rx="10"/>
  <line x1="100" y1="90" x2="340" y2="90" stroke="#94a3b8" stroke-width="4"/>
  <polygon points="220,90 205,150 235,150" fill="#475569"/>
  <rect x="60" y="40" width="80" height="50" fill="#1e3a5f" stroke="#38bdf8" stroke-width="2" rx="4"/>
  <text x="100" y="70" fill="#38bdf8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">4x</text>
  <rect x="270" y="40" width="130" height="50" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="4"/>
  <text x="335" y="65" fill="#f59e0b" font-size="13" font-family="sans-serif" text-anchor="middle">52² - 48²</text>
  <text x="335" y="82" fill="#94a3b8" font-size="11" font-family="sans-serif" text-anchor="middle">= 100 × 4 = 400</text>
  <text x="220" y="190" fill="#4ade80" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">x = 400 / 4 = 100</text>
</svg>""",
     ["100", "200", "50", "400"],
     "A", "OSC", "easy",
     r"\(4x = 52^2 - 48^2 = (52 + 48)(52 - 48) = 100 \times 4 = 400 \implies x = 100\)."),

    # 82
    (r"According to the numerical trick summary below, what is the value of \(106 \times 107 - 10,000\)?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="180">
  <rect width="440" height="220" fill="#0f172a" rx="10"/>
  <rect x="30" y="30" width="380" height="160" fill="#1e293b" rx="8" stroke="#38bdf8" stroke-width="2"/>
  <text x="220" y="65" fill="#38bdf8" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">(100 + a)(100 + b) Expansion</text>
  <text x="220" y="95" fill="#f8fafc" font-size="13" font-family="sans-serif" text-anchor="middle">106 × 107 = (100 + 6)(100 + 7)</text>
  <text x="220" y="125" fill="#94a3b8" font-size="13" font-family="sans-serif" text-anchor="middle">= 10,000 + (6 + 7)×100 + (6 × 7) = 10,000 + 1,300 + 42</text>
  <text x="220" y="155" fill="#4ade80" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">Surplus over 10,000 = 1,342</text>
</svg>""",
     ["1,342", "1,300", "1,340", "1,442"],
     "A", "OSC", "easy",
     r"\(106 \times 107 = 10,000 + 1,300 + 42 = 11,342\). Subtracting 10,000 gives 1,342."),
]

def generate_questions():
    questions = []
    
    # 1-40: Exam
    for idx, (text, opts, ans, qtype, diff, exp) in enumerate(exam_data, start=1):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        questions.append(make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "exam", "school", exp))
        
    # 41-70: Practice
    for idx, (text, opts, ans, qtype, diff, exp) in enumerate(practice_data, start=41):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        questions.append(make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "practice", "school", exp))
        
    # 71-82: Mock / Foundation
    for idx, (text, opts, ans, qtype, diff, exp) in enumerate(mock_data, start=71):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        questions.append(make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "mock", "foundation", exp))
        
    return questions

if __name__ == "__main__":
    qs = generate_questions()
    print(f"Generated {len(qs)} questions for {TOPIC_CODE}")
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch6_topic5.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_path}")
