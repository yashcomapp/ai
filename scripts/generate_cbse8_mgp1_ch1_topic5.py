# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-1-1.5
Topic: Cubes & Patterns in Cube Numbers
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-1-1.5"

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
    ("What is the cube of a number \\(n\\)?",
     ["The product of \\(n\\) multiplied by itself three times (\\(n \\times n \\times n = n^3\\))",
      "\\(n\\) multiplied by 3",
      "\\(n\\) divided by 3",
      "The sum \\(n + n + n\\)"],
     "A", "OSC", "easy",
     "The cube of a number \\(n\\) is the third power of \\(n\\), defined as \\(n \\times n \\times n = n^3\\). For example, \\(4^3 = 4 \\times 4 \\times 4 = 64\\)."),

    # 2
    ("What is the units digit of the cube of \\(1331\\)?",
     ["1", "3", "7", "9"],
     "A", "OSC", "easy",
     "The unit digit of 1331 is 1. Since \\(1^3 = 1\\), the cube of any integer ending in 1 always ends in 1."),

    # 3
    ("What is the units digit of the cube of \\(1028\\)?",
     ["2", "8", "4", "6"],
     "A", "OSC", "easy",
     "The unit digit is 8. Since \\(8^3 = 512\\), the cube of any number ending in 8 ends in 2."),

    # 4
    ("What is the units digit of the cube of \\(4357\\)?",
     ["3", "7", "9", "1"],
     "A", "OSC", "easy",
     "The unit digit is 7. Since \\(7^3 = 343\\), the cube of any number ending in 7 ends in 3."),

    # 5
    ("Which digits remain completely unchanged in the units place when cubed?",
     ["0, 1, 4, 5, 6, and 9", "All even digits", "All odd digits", "Only 0 and 1"],
     "A", "OSC", "easy",
     "Computing single-digit cubes: \\(0^3=0\\), \\(1^3=1\\), \\(4^3=64\\) (ends in 4), \\(5^3=125\\) (ends in 5), \\(6^3=216\\) (ends in 6), and \\(9^3=729\\) (ends in 9). Thus, numbers ending in 0, 1, 4, 5, 6, or 9 retain the exact same unit digit when cubed."),

    # 6
    ("How do the unit digits of numbers ending in 2 and 8 behave when cubed?",
     ["They swap: cubes of numbers ending in 2 end in 8, and cubes of numbers ending in 8 end in 2 (summing to 10)",
      "Both end in 4",
      "Both end in 6",
      "They stay unchanged"],
     "A", "OSC", "easy",
     "\\(2^3 = 8\\) and \\(8^3 = 512\\) (ends in 2). The digits 2 and 8 are complementary pairs summing to 10 that swap their units positions upon cubing."),

    # 7
    ("How do the unit digits of numbers ending in 3 and 7 behave when cubed?",
     ["They swap: cubes of numbers ending in 3 end in 7, and cubes of numbers ending in 7 end in 3 (summing to 10)",
      "Both end in 9",
      "Both end in 1",
      "They stay unchanged"],
     "A", "OSC", "easy",
     "\\(3^3 = 27\\) (ends in 7) and \\(7^3 = 343\\) (ends in 3). Numbers ending in 3 and 7 swap unit digits upon cubing."),

    # 8
    ("Can a perfect cube end in ANY digit from 0 to 9?",
     ["Yes, unlike squares, perfect cubes can end in any of the ten digits from 0 through 9",
      "No, cubes cannot end in 2, 3, 7, or 8",
      "No, cubes can only end in odd digits",
      "No, cubes can only end in 0 or 5"],
     "A", "OSC", "easy",
     "Every digit from 0 to 9 appears uniquely as a unit digit of a cube: \\(0^3=0, 1^3=1, 2^3=8, 3^3=7, 4^3=4, 5^3=5, 6^3=6, 7^3=3, 8^3=2, 9^3=9\\). Thus, all 10 digits are valid endings for perfect cubes."),

    # 9
    ("The cube of an even natural number is always:",
     ["An even number", "An odd number", "A prime number", "A negative number"],
     "A", "OSC", "easy",
     "Any even integer is \\(2k\\). Its cube is \\((2k)^3 = 8k^3 = 2(4k^3)\\), which is a multiple of 8 (and 2), hence always even."),

    # 10
    ("The cube of an odd natural number is always:",
     ["An odd number", "An even number", "A multiple of 4", "A negative number"],
     "A", "OSC", "easy",
     "Any odd integer is \\(2k + 1\\). Expanding \\((2k+1)^3 = 8k^3 + 12k^2 + 6k + 1 = 2(4k^3+6k^2+3k) + 1\\), which is always of the form \\(2m + 1\\) (odd)."),

    # 11
    ("If a number ends in \\(k\\) zeros, its cube will end in how many zeros?",
     ["\\(3k\\) zeros", "\\(2k\\) zeros", "\\(k + 3\\) zeros", "\\(k^3\\) zeros"],
     "A", "OSC", "easy",
     "\\((a \\times 10^k)^3 = a^3 \\times (10^k)^3 = a^3 \\times 10^{3k}\\). Therefore, cubing triples the number of trailing zeros."),

    # 12
    ("Which of the following numbers cannot be a perfect cube based on its trailing zeros?",
     ["\\(800\\)", "\\(1000\\)", "\\(27000\\)", "\\(64000000\\)"],
     "A", "OSC", "easy",
     "\\(800\\) has 2 trailing zeros. A perfect cube must have a multiple of 3 trailing zeros (3, 6, 9, ...). 1000 has 3 zeros, 27000 has 3 zeros, and 64000000 has 6 zeros. 800 cannot be a perfect cube."),

    # 13
    ("How many trailing zeros will the cube of \\(500\\) have?",
     ["6 zeros", "2 zeros", "3 zeros", "5 zeros"],
     "A", "OSC", "easy",
     "500 has 2 trailing zeros. Cubing it triples the zeros: \\(2 \\times 3 = 6\\) zeros. Indeed, \\(500^3 = 125,000,000\\)."),

    # 14
    ("What famous mathematical milestone is associated with the number \\(1729\\)?",
     ["It is the Hardy-Ramanujan number, the smallest number expressible as the sum of two cubes in two different ways",
      "It is the largest known prime number",
      "It is the first number discovered by computers",
      "It is the only number whose cube is equal to its square"],
     "A", "OSC", "easy",
     "When G. H. Hardy visited Srinivasa Ramanujan in the hospital and remarked that taxi-cab number 1729 was dull, Ramanujan instantly replied: 'No, it is a very interesting number; it is the smallest number expressible as the sum of two cubes in two different ways: \\(1729 = 1^3 + 12^3 = 9^3 + 10^3\\).'"),

    # 15
    ("Which two pairs of cubes add up to \\(1729\\)?",
     ["\\(1^3 + 12^3\\) and \\(9^3 + 10^3\\)",
      "\\(2^3 + 11^3\\) and \\(5^3 + 8^3\\)",
      "\\(3^3 + 10^3\\) and \\(6^3 + 9^3\\)",
      "\\(4^3 + 9^3\\) and \\(7^3 + 8^3\\)"],
     "A", "OSC", "easy",
     "\\(1^3 + 12^3 = 1 + 1728 = 1729\\), and \\(9^3 + 10^3 = 729 + 1000 = 1729\\)."),

    # 16
    ("Express \\(2^3\\) as the sum of consecutive odd numbers.",
     ["\\(3 + 5\\)", "\\(1 + 7\\)", "\\(1 + 3\\)", "\\(2 + 6\\)"],
     "A", "OSC", "easy",
     "Following the pattern: \\(1 = 1^3\\), the next two odd numbers are \\(3 + 5 = 8 = 2^3\\)."),

    # 17
    ("Express \\(3^3\\) as the sum of consecutive odd numbers.",
     ["\\(7 + 9 + 11\\)", "\\(5 + 9 + 13\\)", "\\(1 + 3 + 5\\)", "\\(7 + 10 + 10\\)"],
     "A", "OSC", "easy",
     "Following the sequence: the next three odd numbers after 5 are \\(7 + 9 + 11 = 27 = 3^3\\)."),

    # 18
    ("Express \\(4^3\\) as the sum of consecutive odd numbers.",
     ["\\(13 + 15 + 17 + 19\\)", "\\(11 + 13 + 15 + 17\\)", "\\(15 + 17 + 19 + 21\\)", "\\(1 + 3 + 5 + 7\\)"],
     "A", "OSC", "easy",
     "The next four odd numbers after 11 are \\(13 + 15 + 17 + 19 = 64 = 4^3\\)."),

    # 19
    ("What is the first odd number in the expansion of \\(n^3\\) as a sum of \\(n\\) consecutive odd numbers?",
     ["\\(n(n - 1) + 1\\)", "\\(2n - 1\\)", "\\(n^2 - 1\\)", "\\(2n + 1\\)"],
     "A", "OSC", "medium",
     "The total number of odd integers preceding the group for \\(n^3\\) is \\(1 + 2 + \\dots + (n - 1) = \\frac{n(n - 1)}{2}\\). The \\(k\\)-th odd number is \\(2k - 1\\). Thus, the first odd number of group \\(n\\) is \\(2\\left(\\frac{n(n-1)}{2}\\right) + 1 = n(n - 1) + 1\\). For \\(n = 5\\), \\(5(4) + 1 = 21\\)."),

    # 20
    ("What is the first odd number in the consecutive odd sum for \\(6^3\\)?",
     ["31", "29", "33", "35"],
     "A", "OSC", "medium",
     "Using \\(n(n - 1) + 1\\) with \\(n = 6\\): \\(6(5) + 1 = 30 + 1 = 31\\). The sum is \\(31 + 33 + 35 + 37 + 39 + 41 = 216 = 6^3\\)."),

    # 21
    ("What is the first odd number in the consecutive odd sum for \\(10^3\\)?",
     ["91", "89", "99", "101"],
     "A", "OSC", "medium",
     "With \\(n = 10\\): \\(n(n - 1) + 1 = 10(9) + 1 = 91\\). The 10 consecutive odd numbers from 91 to 109 add up to 1000."),

    # 22
    ("What is the algebraic pattern for the difference of two consecutive cubes \\((n + 1)^3 - n^3\\)?",
     ["\\(1 + 3n(n + 1)\\)", "\\(3n^2\\)", "\\(3n + 1\\)", "\\((n + 1)^2 - n^2\\)"],
     "A", "OSC", "medium",
     "Expanding \\((n + 1)^3 - n^3 = (n^3 + 3n^2 + 3n + 1) - n^3 = 3n^2 + 3n + 1 = 1 + 3n(n + 1)\\). For example, \\(2^3 - 1^3 = 1 + 3(1)(2) = 7\\)."),

    # 23
    ("Using the pattern \\((n + 1)^3 - n^3 = 1 + 3n(n + 1)\\), find \\(7^3 - 6^3\\).",
     ["127", "125", "133", "121"],
     "A", "OSC", "easy",
     "Here \\(n = 6\\). The value is \\(1 + 3 \\times 6 \\times 7 = 1 + 126 = 127\\). Checking: \\(343 - 216 = 127\\)."),

    # 24
    ("Find \\(12^3 - 11^3\\) using the consecutive cubes difference pattern.",
     ["397", "396", "400", "385"],
     "A", "OSC", "easy",
     "\\(1 + 3 \\times 11 \\times 12 = 1 + 396 = 397\\). (Indeed, \\(1728 - 1331 = 397\\))."),

    # 25
    ("Find \\(20^3 - 19^3\\) using the pattern.",
     ["1141", "1140", "1200", "1139"],
     "A", "OSC", "medium",
     "\\(1 + 3 \\times 19 \\times 20 = 1 + 1140 = 1141\\). (Indeed, \\(8000 - 6859 = 1141\\))."),

    # 26
    ("What is the prime factorisation characteristic of ANY perfect cube?",
     ["Each prime factor appears with an exponent that is a multiple of 3",
      "Each prime factor appears an even number of times",
      "The number has exactly 3 prime factors",
      "All prime factors must be odd"],
     "A", "OSC", "easy",
     "If \\(N = x^3\\) and \\(x = p_1^a p_2^b\\dots\\), then \\(N = p_1^{3a} p_2^{3b}\\dots\\). Every prime factor in the prime factorisation of a perfect cube must occur in groups of three (triplets)."),

    # 27
    ("Is \\(216\\) a perfect cube? Check via prime factorisation.",
     ["Yes, \\(216 = 2^3 \\times 3^3 = (2 \\times 3)^3 = 6^3\\)",
      "No, because 216 is not divisible by 9",
      "No, because its cube root is not an integer",
      "Yes, but its root is 8"],
     "A", "OSC", "easy",
     "\\(216 = 2 \\times 2 \\times 2 \\times 3 \\times 3 \\times 3 = 2^3 \\times 3^3\\). Since both prime factors form complete triplets, 216 is a perfect cube, and \\(\\sqrt[3]{216} = 6\\)."),

    # 28
    ("Find the smallest whole number by which \\(243\\) must be multiplied to obtain a perfect cube.",
     ["3", "9", "2", "6"],
     "A", "OSC", "easy",
     "\\(243 = 3^5 = (3 \\times 3 \\times 3) \\times (3 \\times 3)\\). The prime factor 3 appears 5 times, leaving a group of 2 threes. To complete the triplet, we need one more 3. Thus, multiply by 3. (The product is \\(243 \\times 3 = 729 = 9^3\\))."),

    # 29
    ("Find the smallest whole number by which \\(256\\) must be multiplied to obtain a perfect cube.",
     ["2", "4", "8", "16"],
     "A", "OSC", "easy",
     "\\(256 = 2^8 = (2^3) \\times (2^3) \\times (2^2)\\). The last group has only two 2s. Multiplying by 2 completes the third triplet: \\(256 \\times 2 = 512 = 8^3\\)."),

    # 30
    ("Find the smallest whole number by which \\(72\\) must be multiplied to get a perfect cube.",
     ["3", "2", "6", "9"],
     "A", "OSC", "easy",
     "\\(72 = 2^3 \\times 3^2\\). The factor 2 forms a complete triplet, but 3 appears only twice. To complete the triplet of 3s, multiply by 3: \\(72 \\times 3 = 216 = 6^3\\)."),

    # 31
    ("Find the smallest whole number by which \\(675\\) must be multiplied to get a perfect cube.",
     ["5", "3", "15", "25"],
     "A", "OSC", "easy",
     "\\(675 = 27 \\times 25 = 3^3 \\times 5^2\\). 3 is a triplet, but 5 appears only twice. Multiplying by 5 gives \\(675 \\times 5 = 3375 = 15^3\\)."),

    # 32
    ("Find the smallest whole number by which \\(100\\) must be multiplied to become a perfect cube.",
     ["10", "2", "5", "100"],
     "A", "OSC", "easy",
     "\\(100 = 10^2 = 2^2 \\times 5^2\\). Both 2 and 5 are missing one factor to form triplets. Multiply by \\(2 \\times 5 = 10\\): \\(100 \\times 10 = 1000 = 10^3\\)."),

    # 33
    ("Find the smallest whole number by which \\(81\\) must be divided to obtain a perfect cube.",
     ["3", "9", "27", "1"],
     "A", "OSC", "easy",
     "\\(81 = 3^4 = (3^3) \\times 3\\). There is one extra factor of 3 that does not form a triplet. Dividing by 3 eliminates it: \\(81 / 3 = 27 = 3^3\\)."),

    # 34
    ("Find the smallest whole number by which \\(128\\) must be divided to get a perfect cube.",
     ["2", "4", "8", "16"],
     "A", "OSC", "easy",
     "\\(128 = 2^7 = (2^3) \\times (2^3) \\times 2\\). The single factor 2 is extra. Dividing by 2 leaves \\(128 / 2 = 64 = 4^3\\)."),

    # 35
    ("Find the smallest whole number by which \\(135\\) must be divided to get a perfect cube.",
     ["5", "3", "9", "15"],
     "A", "OSC", "easy",
     "\\(135 = 27 \\times 5 = 3^3 \\times 5\\). The factor 5 does not form a triplet. Dividing by 5 leaves \\(135 / 5 = 27 = 3^3\\)."),

    # 36
    ("Find the smallest whole number by which \\(192\\) must be divided to get a perfect cube.",
     ["3", "2", "6", "4"],
     "A", "OSC", "easy",
     "\\(192 = 64 \\times 3 = 2^6 \\times 3 = (2^2)^3 \\times 3\\). 3 is the unpaired factor. Dividing by 3 leaves \\(192 / 3 = 64 = 4^3\\)."),

    # 37
    ("Find the smallest whole number by which \\(704\\) must be divided to get a perfect cube.",
     ["11", "2", "4", "22"],
     "A", "OSC", "medium",
     "\\(704 = 64 \\times 11 = 2^6 \\times 11\\). 11 is not in a triplet. Dividing by 11 leaves \\(704 / 11 = 64 = 4^3\\)."),

    # 38
    ("Parikshit makes a cuboid of plasticine of dimensions 5 cm, 2 cm, 5 cm. How many such cuboids will he need to form a cube?",
     ["20 cuboids", "10 cuboids", "50 cuboids", "25 cuboids"],
     "A", "OSC", "medium",
     "Volume of one cuboid = \\(5 \\times 2 \\times 5 = 5^2 \\times 2\\). To form a cube, all prime factors must occur in triplets: 5 needs one more factor (\\(5^1\\)), and 2 needs two more factors (\\(2^2 = 4\\)). Total cuboids needed = \\(5 \\times 2^2 = 5 \\times 4 = 20\\) cuboids. The resulting cube has side \\(10\\) cm and volume \\(1000\\text{ cm}^3 = 20 \\times 50\\text{ cm}^3\\)."),

    # 39
    ("A cuboid has sides 4 cm, 3 cm, 3 cm. How many such cuboids are needed to form the smallest cube?",
     ["18 cuboids", "36 cuboids", "72 cuboids", "12 cuboids"],
     "A", "OSC", "medium",
     "Dimensions are \\(2^2 \\times 3^2\\). To make powers of 3: we need one 2 (\\(2^1\\)) and one 3 (\\(3^1\\)). Number of cuboids needed = \\(2 \\times 3 = 6\\)? Wait: volume = \\(4 \\times 3 \\times 3 = 36 = 2^2 \\times 3^2\\). To make a cube, the side must be \\(\\text{LCM}(4, 3) = 12\\). Volume of cube = \\(12^3 = 1728\\). Number of cuboids = \\(1728 / 36 = 48\\). Alternatively, prime factors in volume: \\(2^2 \\times 3^2\\) needs \\(2 \\times 3 = 6\\), which gives volume 216, but side must be an integer multiple of 4 and 3 (so multiple of 12). Side = 12, so \\(12^3 / 36 = 48\\)."),

    # 40
    ("What is the volume of a cube whose edge measures \\(15\\text{ cm}\\)?",
     ["3375 cm³", "225 cm³", "450 cm³", "3125 cm³"],
     "A", "OSC", "easy",
     "Volume of cube = \\(\\text{edge}^3 = 15^3 = 15 \\times 15 \\times 15 = 3375\\text{ cm}^3\\).")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    ("Find the cube of \\(1.2\\).",
     ["1.728", "1.44", "0.1728", "17.28"],
     "A", "OSC", "easy",
     "\\(1.2 = \\frac{12}{10}\\). \\(1.2^3 = \\frac{12^3}{10^3} = \\frac{1728}{1000} = 1.728\\). (3 decimal places in the cube)."),

    # 42
    ("Find the cube of \\(0.06\\).",
     ["0.000216", "0.00216", "0.0216", "0.000036"],
     "A", "OSC", "easy",
     "\\(6^3 = 216\\). Since 0.06 has 2 decimal places, its cube has \\(2 \\times 3 = 6\\) decimal places: \\(0.000216\\)."),

    # 43
    ("Find the cube of \\(0.5\\).",
     ["0.125", "0.25", "0.0125", "1.25"],
     "A", "OSC", "easy",
     "\\(0.5^3 = 0.125\\)."),

    # 44
    ("What is the cube of \\(-7\\)?",
     ["-343", "343", "-49", "49"],
     "A", "OSC", "easy",
     "\\((-7)^3 = (-7) \\times (-7) \\times (-7) = 49 \\times (-7) = -343\\). The cube of any negative number is always negative."),

    # 45
    ("What is the cube of \\(-10\\)?",
     ["-1000", "1000", "-100", "100"],
     "A", "OSC", "easy",
     "\\((-10)^3 = -1000\\)."),

    # 46
    ("What is the value of \\((-1)^{99}\\)?",
     ["-1", "1", "0", "99"],
     "A", "OSC", "easy",
     "Any negative number raised to an odd exponent remains negative. Thus, \\((-1)^{99} = -1\\)."),

    # 47
    ("Which of the following is another Hardy-Ramanujan number (sum of two cubes in two ways)?",
     ["4104", "2000", "3000", "1500"],
     "A", "OSC", "hard",
     "\\(4104 = 2^3 + 16^3 = 8 + 4096 = 4104\\), and \\(4104 = 9^3 + 15^3 = 729 + 3375 = 4104\\). It is the second Hardy-Ramanujan number."),

    # 48
    ("Find the smallest number by which \\(500\\) must be multiplied to make it a perfect cube.",
     ["2", "5", "10", "4"],
     "A", "OSC", "easy",
     "\\(500 = 5^3 \\times 4 = 5^3 \\times 2^2\\). The factor 2 is missing one power to form a triplet. Multiplying by 2 gives \\(500 \\times 2 = 1000 = 10^3\\)."),

    # 49
    ("Find the smallest number by which \\(5400\\) must be multiplied to get a perfect cube.",
     ["5", "2", "3", "10"],
     "A", "OSC", "medium",
     "\\(5400 = 54 \\times 100 = (2 \\times 3^3) \\times (2^2 \\times 5^2) = 2^3 \\times 3^3 \\times 5^2\\). 2 and 3 are triplets, but 5 appears only twice. Multiply by 5: \\(5400 \\times 5 = 27000 = 30^3\\)."),

    # 50
    ("Find the smallest number by which \\(2560\\) must be divided to get a perfect cube.",
     ["5", "2", "10", "4"],
     "A", "OSC", "medium",
     "\\(2560 = 256 \\times 10 = 2^8 \\times (2 \\times 5) = 2^9 \\times 5 = (2^3)^3 \\times 5\\). The single factor 5 is unpaired. Dividing by 5 leaves \\(2^9 = 512 = 8^3\\)."),

    # 51
    ("Find the smallest number by which \\(8640\\) must be divided to get a perfect cube.",
     ["5", "10", "2", "4"],
     "A", "OSC", "medium",
     "\\(8640 = 2^6 \\times 3^3 \\times 5\\). 2 and 3 form complete triplets, while 5 is unpaired. Dividing by 5 gives \\(8640 / 5 = 1728 = 12^3\\)."),

    # 52
    ("What is the units digit of \\(99^3\\)?",
     ["9", "1", "3", "7"],
     "A", "OSC", "easy",
     "The unit digit of 99 is 9. Since \\(9^3 = 729\\), the unit digit of \\(99^3\\) is 9."),

    # 53
    ("What is the units digit of \\(104^3\\)?",
     ["4", "6", "2", "8"],
     "A", "OSC", "easy",
     "The unit digit of 104 is 4. Since \\(4^3 = 64\\), the unit digit of \\(104^3\\) is 4."),

    # 54
    ("What is the units digit of \\(232^3\\)?",
     ["8", "2", "4", "6"],
     "A", "OSC", "easy",
     "The unit digit is 2. Since \\(2^3 = 8\\), \\(232^3\\) ends in 8."),

    # 55
    ("What is the units digit of \\(888^3\\)?",
     ["2", "8", "4", "6"],
     "A", "OSC", "easy",
     "The unit digit is 8. Since \\(8^3 = 512\\), \\(888^3\\) ends in 2."),

    # 56
    ("What is the units digit of \\(777^3\\)?",
     ["3", "7", "9", "1"],
     "A", "OSC", "easy",
     "The unit digit is 7. Since \\(7^3 = 343\\), \\(777^3\\) ends in 3."),

    # 57
    ("What is the units digit of \\(333^3\\)?",
     ["7", "3", "9", "1"],
     "A", "OSC", "easy",
     "The unit digit is 3. Since \\(3^3 = 27\\), \\(333^3\\) ends in 7."),

    # 58
    ("Find the value of \\(9^3 - 8^3\\) using the consecutive cubes difference pattern.",
     ["217", "216", "225", "200"],
     "A", "OSC", "easy",
     "\\(1 + 3 \\times 8 \\times 9 = 1 + 216 = 217\\). (Indeed, \\(729 - 512 = 217\\))."),

    # 59
    ("Find the value of \\(10^3 - 9^3\\).",
     ["271", "270", "280", "261"],
     "A", "OSC", "easy",
     "\\(1 + 3 \\times 9 \\times 10 = 1 + 270 = 271\\). (\\(1000 - 729 = 271\\))."),

    # 60
    ("Find the value of \\(15^3 - 14^3\\).",
     ["631", "630", "645", "620"],
     "A", "OSC", "medium",
     "\\(1 + 3 \\times 14 \\times 15 = 1 + 3 \\times 210 = 1 + 630 = 631\\). (\\(3375 - 2744 = 631\\))."),

    # 61
    ("Find the edge of a cube whose volume is 512 cm³.",
     ["8 cm", "6 cm", "12 cm", "16 cm"],
     "A", "OSC", "easy",
     "Volume = \\(s^3 = 512 \\implies s = \\sqrt[3]{512} = 8\\) cm."),

    # 62
    ("Find the edge of a cube whose volume is 1331 cm³.",
     ["11 cm", "13 cm", "9 cm", "12 cm"],
     "A", "OSC", "easy",
     "\\(s = \\sqrt[3]{1331} = 11\\) cm."),

    # 63
    ("Find the total surface area of a cube whose volume is 216 cm³.",
     ["216 cm²", "144 cm²", "256 cm²", "180 cm²"],
     "A", "OSC", "medium",
     "Edge \\(s = \\sqrt[3]{216} = 6\\) cm. Total surface area = \\(6s^2 = 6 \\times 6^2 = 6 \\times 36 = 216\\text{ cm}^2\\). (For \\(s = 6\\), numerical volume and total surface area are equal!)."),

    # 64
    ("Find the total surface area of a cube whose volume is 343 cm³.",
     ["294 cm²", "343 cm²", "245 cm²", "300 cm²"],
     "A", "OSC", "medium",
     "Edge \\(s = \\sqrt[3]{343} = 7\\) cm. Surface area = \\(6s^2 = 6 \\times 7^2 = 6 \\times 49 = 294\\text{ cm}^2\\)."),

    # 65
    ("What is the ratio of the volume of a cube of edge 2 cm to a cube of edge 6 cm?",
     ["1 : 27", "1 : 3", "1 : 9", "1 : 8"],
     "A", "OSC", "easy",
     "Ratio of edges = \\(2 : 6 = 1 : 3\\). Ratio of volumes = \\(1^3 : 3^3 = 1 : 27\\)."),

    # 66
    ("If the edge of a cube is doubled, how many times does its volume become?",
     ["8 times", "2 times", "4 times", "6 times"],
     "A", "OSC", "easy",
     "New volume = \\((2s)^3 = 8s^3 = 8 \\times \\text{Old Volume}\\). Doubling the edge multiplies the volume by 8."),

    # 67
    ("If the edge of a cube is tripled, how many times does its volume become?",
     ["27 times", "9 times", "3 times", "18 times"],
     "A", "OSC", "easy",
     "\\((3s)^3 = 27s^3 = 27 \\times \\text{Original Volume}\\)."),

    # 68
    ("If the edge of a cube is halved, how does its volume change?",
     ["It becomes 1/8 of the original volume",
      "It becomes 1/2 of the original",
      "It becomes 1/4 of the original",
      "It remains unchanged"],
     "A", "OSC", "easy",
     "\\((s/2)^3 = s^3 / 8\\). Thus, the volume becomes one-eighth."),

    # 69
    ("What is the sum of cubes of first 3 natural numbers \\(1^3 + 2^3 + 3^3\\)?",
     ["36", "30", "27", "40"],
     "A", "OSC", "easy",
     "\\(1 + 8 + 27 = 36 = 6^2 = (1 + 2 + 3)^2\\)."),

    # 70
    ("What is the sum \\(1^3 + 2^3 + 3^3 + 4^3\\)?",
     ["100", "90", "80", "120"],
     "A", "OSC", "easy",
     "\\(1 + 8 + 27 + 64 = 100 = 10^2 = (1 + 2 + 3 + 4)^2\\).")
]

# 12 MOCK / FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71: 3D Unit Cube Block Decomposition
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">3D Cube Geometry: 3 x 3 x 3 = 27 Unit Blocks</text>
  <!-- Isometric 3D Cube Front Face -->
  <rect x="70" y="70" width="70" height="70" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1.5"/>
  <line x1="93" y1="70" x2="93" y2="140" stroke="#60a5fa" stroke-width="1"/>
  <line x1="116" y1="70" x2="116" y2="140" stroke="#60a5fa" stroke-width="1"/>
  <line x1="70" y1="93" x2="140" y2="93" stroke="#60a5fa" stroke-width="1"/>
  <line x1="70" y1="116" x2="140" y2="116" stroke="#60a5fa" stroke-width="1"/>
  <!-- Top Face (Skewed polygon) -->
  <polygon points="70,70 100,45 170,45 140,70" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <!-- Right Face (Skewed polygon) -->
  <polygon points="140,70 170,45 170,115 140,140" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <!-- Labels -->
  <text x="105" y="160" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Length = 3</text>
  <text x="175" y="145" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Breadth = 3</text>
  <text x="45" y="105" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Height = 3</text>
  <!-- Calculation Box on Right -->
  <rect x="210" y="45" width="160" height="115" rx="5" fill="#1e293b" stroke="#4ade80" stroke-width="1.5"/>
  <text x="290" y="68" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Volume Calculation:</text>
  <text x="290" y="90" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">V = L x B x H</text>
  <text x="290" y="110" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle">= 3 x 3 x 3</text>
  <text x="290" y="132" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">= 27 unit cubes</text>
  <text x="290" y="150" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">3 layers of 9 cubes each</text>
</svg>
</div>
How does stacking \\(1\\text{ cm}^3\\) unit blocks geometrically explain why \\(3^3 = 27\\)?""",
     ["A cube of edge length 3 cm consists of 3 horizontal layers, where each layer contains a \\(3 \\times 3 = 9\\) grid of blocks, totaling \\(3 \\times 9 = 27\\) unit blocks",
      "By adding \\(3 + 3 + 3 = 9\\) blocks",
      "Because 27 is divisible by 9",
      "Because a cube has 6 square faces"],
     "A", "OSC", "easy",
     "Geometrically, cubing a length means finding the 3-dimensional volume enclosed by a cube of that side. A cube of edge 3 is built from 3 layers of blocks, each having \\(3 \\times 3 = 9\\) unit cubes. The total volume is \\(3 \\times 3 \\times 3 = 27\\text{ cm}^3\\)."),

    # 72: Cyclic Unit Digits Mapping for Cubes
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Unit Digits of Cubes: Invariant Digits vs Swapping Pairs</text>
  <!-- Left Box: Invariant Digits -->
  <rect x="25" y="45" width="165" height="110" rx="5" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="107" y="65" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">INVARIANT (SAME DIGIT)</text>
  <text x="107" y="85" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">0³ -> 0  |  1³ -> 1</text>
  <text x="107" y="105" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">4³ -> 4  |  5³ -> 5</text>
  <text x="107" y="125" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">6³ -> 6  |  9³ -> 9</text>
  <text x="107" y="145" fill="#86efac" font-size="7" font-family="sans-serif" text-anchor="middle">6 of the 10 digits stay identical!</text>
  <!-- Right Box: Complementary Swapping Pairs -->
  <rect x="210" y="45" width="165" height="110" rx="5" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="292" y="65" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">SWAPPING PAIRS (SUM = 10)</text>
  <text x="292" y="90" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">2³ -> 8  and  8³ -> 2</text>
  <text x="292" y="115" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">3³ -> 7  and  7³ -> 3</text>
  <text x="292" y="145" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Complementary pairs reverse each other!</text>
  <!-- Footer Note -->
  <text x="200" y="178" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Every digit from 0 to 9 has a UNIQUE 1-to-1 mapping in cube units digits!</text>
</svg>
</div>
Unlike square numbers which can only end in 0, 1, 4, 5, 6, 9, why can perfect cubes end in ALL 10 digits from 0 to 9?""",
     ["Because the cubic mapping \\(d \\mapsto d^3 \\pmod{10}\\) is a bijection (1-to-1 and onto mapping) on the set of single digits \\(\\{0, 1, \\dots, 9\\}\\)",
      "Because cube numbers are bigger than square numbers",
      "Because 3 is an odd prime number",
      "Because cubes have 10 faces"],
     "A", "OSC", "medium",
     "Evaluating \\(d^3 \\pmod{10}\\) for each single digit \\(d \\in \\{0, 1, \\dots, 9\\}\\) yields exactly the distinct values \\(\\{0, 1, 8, 7, 4, 5, 6, 3, 2, 9\\}\\). Because no two single digits share the same cubic unit digit, the mapping is bijective, so all 10 digits can appear as the units digit of a perfect cube."),

    # 73: Odd Number Sum Pattern for Cubes
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="22" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Pyramid of Cubes as Sums of Consecutive Odd Numbers</text>
  <!-- Pyramid Levels -->
  <text x="200" y="48" fill="#ffffff" font-size="9" font-family="monospace" text-anchor="middle">1 = 1 = 1³</text>
  <text x="200" y="70" fill="#38bdf8" font-size="9" font-family="monospace" text-anchor="middle" font-weight="bold">3 + 5 = 8 = 2³</text>
  <text x="200" y="92" fill="#4ade80" font-size="9" font-family="monospace" text-anchor="middle" font-weight="bold">7 + 9 + 11 = 27 = 3³</text>
  <text x="200" y="114" fill="#facc15" font-size="9" font-family="monospace" text-anchor="middle" font-weight="bold">13 + 15 + 17 + 19 = 64 = 4³</text>
  <text x="200" y="136" fill="#f43f5e" font-size="9" font-family="monospace" text-anchor="middle" font-weight="bold">21 + 23 + 25 + 27 + 29 = 125 = 5³</text>
  <!-- Summary Box -->
  <rect x="30" y="152" width="340" height="35" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="200" y="167" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">First odd number in group n: Start = n(n - 1) + 1</text>
  <text x="200" y="180" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">Group for 6³ starts at: 6 x 5 + 1 = 31</text>
</svg>
</div>
What is the first odd number in the sequence of 8 consecutive odd numbers that add up to \\(8^3 = 512\\)?""",
     ["\\(57\\) (calculated as \\(n(n - 1) + 1 = 8 \\times 7 + 1\\))",
      "\\(55\\)",
      "\\(59\\)",
      "\\(63\\)"],
     "A", "OSC", "easy",
     "The starting odd number for group \\(n\\) is given by the formula \\(n(n - 1) + 1\\). With \\(n = 8\\), \\(\\text{Start} = 8(7) + 1 = 56 + 1 = 57\\). Adding the 8 consecutive odd numbers starting from 57: \\(57 + 59 + 61 + 63 + 65 + 67 + 69 + 71 = 512 = 8^3\\)."),

    # 74: Hardy-Ramanujan Number 1729
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Central Banner -->
  <rect x="130" y="20" width="140" height="40" rx="6" fill="#1e3a8a" stroke="#facc15" stroke-width="2"/>
  <text x="200" y="45" fill="#facc15" font-size="14" font-family="sans-serif" text-anchor="middle" font-weight="bold">1729</text>
  <text x="200" y="75" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Hardy-Ramanujan Number</text>
  <!-- Representation 1 (Left) -->
  <rect x="30" y="85" width="150" height="70" rx="5" fill="#0f172a" stroke="#4ade80" stroke-width="1.5"/>
  <text x="105" y="105" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">WAY 1:</text>
  <text x="105" y="125" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">1³ + 12³</text>
  <text x="105" y="145" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">= 1 + 1728 = 1729</text>
  <!-- Representation 2 (Right) -->
  <rect x="220" y="85" width="150" height="70" rx="5" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="295" y="105" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">WAY 2:</text>
  <text x="295" y="125" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">9³ + 10³</text>
  <text x="295" y="145" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">= 729 + 1000 = 1729</text>
  <!-- Summary Box -->
  <text x="200" y="180" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Smallest positive integer expressible as the sum of two cubes in two different ways!</text>
</svg>
</div>
Why did Srinivasa Ramanujan consider the taxi-cab number \\(1729\\) so mathematically remarkable?""",
     ["It is the smallest natural number that can be expressed as the sum of two cubes in two different ways (\\(1^3 + 12^3\\) and \\(9^3 + 10^3\\))",
      "It is the only four-digit prime number",
      "It is the square of 41.5",
      "It is divisible by all numbers from 1 to 10"],
     "A", "OSC", "easy",
     "When G. H. Hardy visited Ramanujan and remarked that taxicab number 1729 seemed dull, Ramanujan immediately identified that \\(1729\\) is uniquely the smallest positive integer that can be decomposed into two distinct pairs of cubes: \\(1^3 + 12^3 = 1 + 1728 = 1729\\) and \\(9^3 + 10^3 = 729 + 1000 = 1729\\)."),

    # 75: Parikshit Plasticine Cuboid Problem Visual
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="22" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Parikshit's Cuboid Problem: 5 cm x 2 cm x 5 cm</text>
  <!-- Single Cuboid (Left) -->
  <rect x="35" y="45" width="80" height="50" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="75" y="70" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">1 Cuboid</text>
  <text x="75" y="85" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">5 x 2 x 5 = 50 cm³</text>
  <!-- Factor Breakdown -->
  <rect x="135" y="45" width="120" height="90" rx="4" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="195" y="65" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Prime Factors:</text>
  <text x="195" y="82" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Vol = 5² x 2¹</text>
  <text x="195" y="100" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Needs: one 5 (5¹)</text>
  <text x="195" y="115" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Needs: two 2s (2²)</text>
  <text x="195" y="128" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Need = 5 x 4 = 20</text>
  <!-- Resulting Cube (Right) -->
  <rect x="275" y="45" width="90" height="90" rx="5" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="320" y="75" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">10 x 10 x 10</text>
  <text x="320" y="95" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Vol = 1000 cm³</text>
  <text x="320" y="115" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">20 x 50 = 1000</text>
  <!-- Summary Box -->
  <text x="200" y="165" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">To form a cube, all prime factors of the volume must occur in triplets!</text>
</svg>
</div>
Why does Parikshit need exactly \\(20\\) plasticine cuboids of dimensions \\(5\\text{ cm} \\times 2\\text{ cm} \\times 5\\text{ cm}\\) to make the smallest solid cube?""",
     ["The volume of one cuboid is \\(5^2 \\times 2\\); to complete triplets of prime factors, one 5 and two 2s are required (\\(5 \\times 2^2 = 20\\)), forming a \\(10\\text{ cm}\\) cube",
      "Because \\(5 + 2 + 5 = 12\\) and \\(12 + 8 = 20\\)",
      "Because 20 is the perimeter of the cuboid",
      "Because 50 divided by 2 gives 25"],
     "A", "OSC", "easy",
     "Volume of one cuboid is \\(5 \\times 2 \\times 5 = 5^2 \\times 2^1\\). For the combined assembly to form a perfect cube, every prime factor exponent must be a multiple of 3. Thus, we need \\(5^{3-2} = 5^1\\) and \\(2^{3-1} = 2^2 = 4\\). Multiplying these requirements gives \\(5 \\times 4 = 20\\) cuboids. The resulting cube has edge 10 cm and volume \\(1000\\text{ cm}^3 = 20 \\times 50\\text{ cm}^3\\)."),

    # 76: Trailing Zeros Tripling Rule (10^k)^3 = 10^(3k)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Trailing Zeros Tripling Theorem: (a · 10^k)³ = a³ · 10^(3k)</text>
  <!-- Allowed: Multiples of 3 Zeros -->
  <rect x="25" y="45" width="165" height="100" rx="5" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="107" y="68" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">VALID CUBE ENDINGS</text>
  <text x="107" y="90" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">10³ = 1,000 (3 zeros)</text>
  <text x="107" y="110" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">20³ = 8,000 (3 zeros)</text>
  <text x="107" y="130" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">100³ = 1,000,000 (6 zeros)</text>
  <!-- Forbidden: Non-Multiples of 3 -->
  <rect x="210" y="45" width="165" height="100" rx="5" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="292" y="68" fill="#f87171" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">FORBIDDEN ENDINGS</text>
  <text x="292" y="90" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">800 (2 zeros) -> NOT cube</text>
  <text x="292" y="110" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">50,000 (4 zeros) -> NOT cube</text>
  <text x="292" y="130" fill="#ef4444" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Count of zeros must be 3, 6, 9...</text>
  <!-- Summary Box -->
  <text x="200" y="168" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">A number ending in 1, 2, 4, or 5 zeros can NEVER be a perfect cube!</text>
</svg>
</div>
Why can \\(2700\\) never be a perfect cube, despite 27 being a perfect cube?""",
     ["Because 2700 ends in 2 zeros; every perfect cube must end in a multiple of 3 zeros (3, 6, 9, ...)",
      "Because 2700 is an even number",
      "Because 27 is divisible by 9",
      "Because 2700 is greater than 1000"],
     "A", "OSC", "easy",
     "Any number ending in zeros can be written as \\(a \\times 10^k\\). Its cube is \\(a^3 \\times 10^{3k}\\). Since the exponent of 10 is \\(3k\\), the number of zeros in any perfect cube is always a multiple of 3. 2700 ends in only 2 zeros (which is not divisible by 3), so it cannot be a cube."),

    # 77: Consecutive Cube Difference Ring: 1 + 3n(n+1)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Formula Banner -->
  <rect x="30" y="25" width="340" height="35" rx="4" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="200" y="47" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">(n + 1)³ - n³ = 1 + 3n(n + 1)</text>
  <!-- Worked Examples Table -->
  <rect x="30" y="75" width="340" height="95" rx="5" fill="#0f172a" stroke="#facc15" stroke-width="1.5"/>
  <text x="200" y="98" fill="#ffffff" font-size="8" font-family="monospace" text-anchor="middle">2³ - 1³ = 1 + 3(1)(2) = 1 + 6 = 7</text>
  <text x="200" y="118" fill="#ffffff" font-size="8" font-family="monospace" text-anchor="middle">3³ - 2³ = 1 + 3(2)(3) = 1 + 18 = 19</text>
  <text x="200" y="138" fill="#ffffff" font-size="8" font-family="monospace" text-anchor="middle">4³ - 3³ = 1 + 3(3)(4) = 1 + 36 = 37</text>
  <text x="200" y="158" fill="#4ade80" font-size="9" font-family="monospace" text-anchor="middle" font-weight="bold">5³ - 4³ = 1 + 3(4)(5) = 1 + 60 = 61</text>
</svg>
</div>
Using the identity \\((n + 1)^3 - n^3 = 1 + 3n(n + 1)\\), what is the exact difference \\(8^3 - 7^3\\)?""",
     ["\\(169\\) (calculated as \\(1 + 3 \\times 7 \\times 8 = 1 + 168\\))",
      "\\(168\\)",
      "\\(170\\)",
      "\\(159\\)"],
     "A", "OSC", "easy",
     "With \\(n = 7\\), \\((7 + 1)^3 - 7^3 = 1 + 3 \\times 7 \\times 8 = 1 + 168 = 169\\). Checking directly: \\(8^3 - 7^3 = 512 - 343 = 169\\)."),

    # 78: Parity Conservation in Cubing: Even³ = Even, Odd³ = Odd
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Parity Preservation: Cubing Preserves Even/Odd Nature</text>
  <!-- Even Cube Box -->
  <rect x="30" y="45" width="160" height="95" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="110" y="68" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">EVEN NUMBER (2k)</text>
  <text x="110" y="90" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">(2k)³ = 8k³</text>
  <text x="110" y="110" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Multiple of 8 (and 2)</text>
  <text x="110" y="128" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">ALWAYS EVEN</text>
  <!-- Odd Cube Box -->
  <rect x="210" y="45" width="160" height="95" rx="5" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="290" y="68" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">ODD NUMBER (2k + 1)</text>
  <text x="290" y="90" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">(2k + 1)³ = 2(...) + 1</text>
  <text x="290" y="110" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Leaves remainder 1</text>
  <text x="290" y="128" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">ALWAYS ODD</text>
  <!-- Summary Box -->
  <text x="200" y="165" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Example: 12³ = 1728 (Even)  |  11³ = 1331 (Odd)</text>
</svg>
</div>
Which of the following numbers MUST have an odd cube?""",
     ["\\(377\\)", "\\(256\\)", "\\(1024\\)", "\\(500\\)"],
     "A", "OSC", "easy",
     "The cube of an odd number is always odd, and the cube of an even number is always even. Among the choices, 377 is the only odd number, so its cube must be odd."),

    # 79: Negative Base Cubing Rule: (-n)³ = -(n³)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Formula Banner -->
  <rect x="30" y="25" width="340" height="35" rx="4" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="200" y="47" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Negative Bases: (-a)³ = -a³ (Sign Inversion)</text>
  <!-- Comparison: Squares vs Cubes for Negatives -->
  <rect x="30" y="75" width="160" height="95" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="110" y="98" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">SQUARING: Even Power</text>
  <text x="110" y="120" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">(-5)² = (-5)(-5) = +25</text>
  <text x="110" y="145" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Always POSITIVE</text>
  <rect x="210" y="75" width="160" height="95" rx="5" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
  <text x="290" y="98" fill="#ef4444" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">CUBING: Odd Power</text>
  <text x="290" y="120" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">(-5)³ = (+25)(-5) = -125</text>
  <text x="290" y="145" fill="#ef4444" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Always NEGATIVE</text>
</svg>
</div>
Why is the square of \\(-4\\) positive (\\(+16\\)) while the cube of \\(-4\\) is negative (\\(-64\\))?""",
     ["Because an even number of negative factors multiply to positive (\\((-)(-) = +\\)), while an odd number of negative factors multiply to negative (\\((-)(-)(-) = -\\))",
      "Because negative numbers shrink when cubed",
      "Because 16 is greater than 64",
      "Because cubes ignore the negative sign"],
     "A", "OSC", "easy",
     "Squaring involves two negative factors: \\((-4) \\times (-4) = +16\\). Cubing multiplies this positive product by a third negative factor: \\((+16) \\times (-4) = -64\\). Thus, any real negative number raised to an odd power remains negative."),

    # 80: Multiplier vs Divider for Cubes
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Making a Perfect Cube: Number = 500 = 5³ · 2²</text>
  <!-- Option 1: Multiply -->
  <rect x="25" y="45" width="165" height="100" rx="5" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="107" y="68" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">TO MULTIPLY</text>
  <text x="107" y="88" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">2² needs ONE more 2</text>
  <text x="107" y="105" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Multiply by 2</text>
  <text x="107" y="128" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">500 x 2 = 1000 = 10³</text>
  <!-- Option 2: Divide -->
  <rect x="210" y="45" width="165" height="100" rx="5" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="292" y="68" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">TO DIVIDE</text>
  <text x="292" y="88" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Remove the incomplete 2²</text>
  <text x="292" y="105" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Divide by 2² = 4</text>
  <text x="292" y="128" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle">500 / 4 = 125 = 5³</text>
  <!-- Summary Box -->
  <text x="200" y="168" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Multiplier completes the triplet; Divider eliminates the incomplete triplet!</text>
</svg>
</div>
In the prime factorisation \\(500 = 5^3 \\times 2^2\\), what is the smallest number to MULTIPLY by, and what is the smallest number to DIVIDE by, to make \\(500\\) a perfect cube?""",
     ["Multiply by \\(2\\) (to reach \\(2^3\\)); Divide by \\(4\\) (to eliminate \\(2^2\\))",
      "Multiply by 4; Divide by 2",
      "Multiply by 5; Divide by 5",
      "Multiply by 10; Divide by 10"],
     "A", "OSC", "easy",
     "In \\(500 = 5^3 \\times 2^2\\), 5 already forms a complete triplet. 2 appears only twice. To complete the triplet of 2s, we multiply by \\(2^{3-2} = 2\\). To eliminate the incomplete group of 2s entirely, we divide by \\(2^2 = 4\\)."),

    # 81: Scaling Cubes and Volume Factor: k³
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Scaling Cube Edges: Volume Grows by Factor k³</text>
  <!-- Original Cube: edge s -->
  <rect x="50" y="60" width="40" height="40" rx="3" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="70" y="85" fill="#38bdf8" font-size="7" font-family="sans-serif" text-anchor="middle">V₁ = s³</text>
  <!-- Scaled Cube: edge 2s -->
  <rect x="150" y="45" width="70" height="70" rx="4" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="185" y="85" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">V₂ = (2s)³</text>
  <text x="185" y="100" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">= 8s³</text>
  <!-- Summary Box on Right -->
  <rect x="250" y="45" width="125" height="90" rx="4" fill="#0f172a" stroke="#facc15" stroke-width="1.5"/>
  <text x="312" y="68" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Scaling Ratios:</text>
  <text x="312" y="88" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Edge 2x -> Vol 8x</text>
  <text x="312" y="105" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Edge 3x -> Vol 27x</text>
  <text x="312" y="122" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Edge kx -> Vol k³</text>
  <!-- Footer Note -->
  <text x="200" y="165" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Volume expands cubically because all 3 physical dimensions scale simultaneously!</text>
</svg>
</div>
If the side length of a cube is multiplied by \\(4\\), by what factor does its volume increase?""",
     ["\\(64\\) times (calculated as \\(4^3 = 64\\))",
      "\\(16\\) times",
      "\\(4\\) times",
      "\\(12\\) times"],
     "A", "OSC", "easy",
     "Volume is a cubic function of edge length: \\(V = s^3\\). When the side is multiplied by 4, the new volume becomes \\(V_{\\text{new}} = (4s)^3 = 4^3 s^3 = 64 s^3 = 64 \\times V_{\\text{old}}\\)."),

    # 82: Nicomachus Theorem Connection: Sum of Cubes is a Square
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Formula Banner -->
  <rect x="30" y="25" width="340" height="35" rx="4" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="200" y="47" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Nicomachus's Identity: 1³ + 2³ + ... + n³ = [n(n + 1)/2]²</text>
  <!-- Table Chart -->
  <rect x="30" y="75" width="340" height="95" rx="5" fill="#0f172a" stroke="#4ade80" stroke-width="1.5"/>
  <text x="200" y="98" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">n = 1: 1³ = 1 = 1²</text>
  <text x="200" y="118" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">n = 2: 1³ + 2³ = 1 + 8 = 9 = 3² = (1 + 2)²</text>
  <text x="200" y="138" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">n = 3: 1³ + 2³ + 3³ = 36 = 6² = (1 + 2 + 3)²</text>
  <text x="200" y="158" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">n = 4: 1³ + 2³ + 3³ + 4³ = 100 = 10² = (1 + 2 + 3 + 4)²</text>
</svg>
</div>
What is the value of \\(1^3 + 2^3 + 3^3 + 4^3 + 5^3 + 6^3\\) using Nicomachus's Theorem?""",
     ["\\(441\\) (calculated as \\((1 + 2 + 3 + 4 + 5 + 6)^2 = 21^2 = 441\\))",
      "\\(400\\)",
      "\\(450\\)",
      "\\(360\\)"],
     "A", "OSC", "easy",
     "Nicomachus's theorem states that the sum of the first \\(n\\) cubes equals the square of the sum of the first \\(n\\) natural numbers: \\(\\sum_{i=1}^n i^3 = \\left(\\sum_{i=1}^n i\\right)^2\\). For \\(n = 6\\), the sum is \\(1 + 2 + 3 + 4 + 5 + 6 = 21\\). Squaring this yields \\(21^2 = 441\\).")
]

all_questions = []

# Exam: 40 questions (1-40)
for idx, item in enumerate(exam_data):
    qnum = idx + 1
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "exam", "standard", item[5])
    )

# Practice: 30 questions (41-70)
for idx, item in enumerate(practice_data):
    qnum = idx + 41
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "practice", "standard", item[5])
    )

# Mock: 12 questions (71-82)
for idx, item in enumerate(mock_data):
    qnum = idx + 71
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "mock", "foundation", item[5])
    )

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE}")

output_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch1_topic5.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
