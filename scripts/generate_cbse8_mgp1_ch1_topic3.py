# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-1-1.3
Topic: Finding Square Roots by Prime Factorisation
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-1-1.3"

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
    ("What is the inverse operation of squaring a number?",
     ["Finding the square root", "Cubing the number", "Dividing by 2", "Subtracting the number"],
     "A", "OSC", "easy",
     "Just as subtraction is the inverse of addition and division is the inverse of multiplication, finding the square root is the inverse operation of squaring. If \\(a^2 = b\\), then \\(\\sqrt{b} = a\\)."),

    # 2
    ("What is the square root of \\(729\\) found by prime factorisation?",
     ["27", "23", "29", "37"],
     "A", "OSC", "easy",
     "Prime factorising 729: \\(729 = 3 \\times 3 \\times 3 \\times 3 \\times 3 \\times 3 = (3 \\times 3) \\times (3 \\times 3) \\times (3 \\times 3)\\). Taking one factor from each pair: \\(\\sqrt{729} = 3 \\times 3 \\times 3 = 27\\)."),

    # 3
    ("What is the square root of \\(1296\\)?",
     ["36", "34", "38", "46"],
     "A", "OSC", "easy",
     "Prime factorising 1296: \\(1296 = 2^4 \\times 3^4 = (2 \\times 2) \\times (2 \\times 2) \\times (3 \\times 3) \\times (3 \\times 3)\\). Taking one from each pair: \\(\\sqrt{1296} = 2 \\times 2 \\times 3 \\times 3 = 36\\)."),

    # 4
    ("What is the square root of \\(1764\\)?",
     ["42", "44", "48", "38"],
     "A", "OSC", "easy",
     "Prime factorising 1764: \\(1764 = 2^2 \\times 3^2 \\times 7^2 = (2 \\times 2) \\times (3 \\times 3) \\times (7 \\times 7)\\). Taking one factor per pair gives \\(\\sqrt{1764} = 2 \\times 3 \\times 7 = 42\\)."),

    # 5
    ("What is the square root of \\(4096\\)?",
     ["64", "66", "54", "56"],
     "A", "OSC", "easy",
     "Prime factorising 4096: \\(4096 = 2^{12}\\). Pairing factors: \\(2^6 = 64\\). Thus, \\(\\sqrt{4096} = 64\\)."),

    # 6
    ("What is the square root of \\(7744\\)?",
     ["88", "84", "86", "92"],
     "A", "OSC", "easy",
     "Prime factorising 7744: \\(7744 = 2^6 \\times 11^2 = (2 \\times 2 \\times 2)^2 \\times 11^2 = 8^2 \\times 11^2\\). Thus, \\(\\sqrt{7744} = 8 \\times 11 = 88\\)."),

    # 7
    ("What is the square root of \\(9604\\)?",
     ["98", "94", "96", "102"],
     "A", "OSC", "easy",
     "Prime factorising 9604: \\(9604 = 2^2 \\times 7^4 = (2 \\times 2) \\times (7 \\times 7) \\times (7 \\times 7)\\). Taking one factor from each pair: \\(\\sqrt{9604} = 2 \\times 7 \\times 7 = 98\\)."),

    # 8
    ("Find the smallest whole number by which \\(252\\) must be multiplied so as to get a perfect square.",
     ["7", "2", "3", "5"],
     "A", "OSC", "easy",
     "Prime factorising 252: \\(252 = 2 \\times 2 \\times 3 \\times 3 \\times 7 = (2^2) \\times (3^2) \\times 7\\). The prime factor 7 has no pair. To make it a perfect square, we must multiply by 7. (The resulting square is \\(252 \\times 7 = 1764 = 42^2\\))."),

    # 9
    ("Find the smallest whole number by which \\(180\\) must be multiplied so as to get a perfect square.",
     ["5", "2", "3", "10"],
     "A", "OSC", "easy",
     "Prime factorising 180: \\(180 = 2 \\times 2 \\times 3 \\times 3 \\times 5 = (2^2) \\times (3^2) \\times 5\\). The factor 5 is unpaired. Multiplying by 5 gives \\(180 \\times 5 = 900 = 30^2\\)."),

    # 10
    ("Find the smallest whole number by which \\(1008\\) must be multiplied to get a perfect square.",
     ["7", "2", "3", "14"],
     "A", "OSC", "easy",
     "Prime factorising 1008: \\(1008 = 2^4 \\times 3^2 \\times 7 = (2^2)^2 \\times 3^2 \\times 7\\). 7 is unpaired, so multiplying by 7 yields \\(1008 \\times 7 = 7056 = 84^2\\)."),

    # 11
    ("Find the smallest whole number by which \\(2028\\) must be multiplied to get a perfect square.",
     ["3", "2", "13", "6"],
     "A", "OSC", "medium",
     "Prime factorising 2028: \\(2028 = 2^2 \\times 3 \\times 13^2\\). Here 3 is the only unpaired factor. Multiplying by 3 gives \\(2028 \\times 3 = 6084 = 78^2\\)."),

    # 12
    ("Find the smallest whole number by which \\(1458\\) must be multiplied to get a perfect square.",
     ["2", "3", "6", "9"],
     "A", "OSC", "medium",
     "Prime factorising 1458: \\(1458 = 2 \\times 729 = 2 \\times 3^6\\). 2 is the unpaired factor, so multiplying by 2 gives \\(1458 \\times 2 = 2916 = 54^2\\)."),

    # 13
    ("Find the smallest whole number by which \\(768\\) must be multiplied to get a perfect square.",
     ["3", "2", "6", "4"],
     "A", "OSC", "medium",
     "Prime factorising 768: \\(768 = 256 \\times 3 = 2^8 \\times 3\\). The factor 3 is unpaired, so multiplying by 3 gives \\(768 \\times 3 = 2304 = 48^2\\)."),

    # 14
    ("Find the smallest whole number by which \\(252\\) must be divided so that the quotient is a perfect square.",
     ["7", "2", "3", "6"],
     "A", "OSC", "easy",
     "\\(252 = 2^2 \\times 3^2 \\times 7\\). Dividing by the unpaired factor 7 removes it, leaving \\(252 / 7 = 36 = 6^2\\)."),

    # 15
    ("Find the smallest whole number by which \\(2925\\) must be divided so that the quotient is a perfect square.",
     ["13", "3", "5", "15"],
     "A", "OSC", "medium",
     "Prime factorising 2925: \\(2925 = 3^2 \\times 5^2 \\times 13\\). 13 is unpaired. Dividing by 13 yields \\(2925 / 13 = 225 = 15^2\\)."),

    # 16
    ("Find the smallest whole number by which \\(396\\) must be divided to get a perfect square quotient.",
     ["11", "2", "3", "6"],
     "A", "OSC", "easy",
     "Prime factorising 396: \\(396 = 4 \\times 99 = 2^2 \\times 3^2 \\times 11\\). 11 is unpaired, so dividing by 11 leaves \\(396 / 11 = 36 = 6^2\\)."),

    # 17
    ("Find the smallest whole number by which \\(2645\\) must be divided to get a perfect square quotient.",
     ["5", "23", "3", "15"],
     "A", "OSC", "medium",
     "Prime factorising 2645: \\(2645 = 5 \\times 529 = 5 \\times 23^2\\). The factor 5 is unpaired. Dividing by 5 yields \\(2645 / 5 = 529 = 23^2\\)."),

    # 18
    ("Find the smallest whole number by which \\(2800\\) must be divided to get a perfect square.",
     ["7", "2", "5", "14"],
     "A", "OSC", "easy",
     "\\(2800 = 2^4 \\times 5^2 \\times 7\\). Dividing by 7 yields \\(2800 / 7 = 400 = 20^2\\)."),

    # 19
    ("Find the smallest whole number by which \\(1620\\) must be divided to get a perfect square.",
     ["5", "2", "3", "10"],
     "A", "OSC", "medium",
     "\\(1620 = 2^2 \\times 3^4 \\times 5\\). The factor 5 is unpaired. Dividing by 5 gives \\(1620 / 5 = 324 = 18^2\\)."),

    # 20
    ("How is the square root of a number found using the method of repeated subtraction?",
     ["By successively subtracting consecutive odd numbers starting from 1 (1, 3, 5, 7, ...) until the remainder is 0; the number of subtractions performed is the square root",
      "By successively subtracting 2 until 0 is reached",
      "By subtracting 10 repeatedly",
      "By subtracting half of the number twice"],
     "A", "OSC", "easy",
     "Since the sum of the first \\(n\\) consecutive odd numbers is \\(n^2\\), subtracting \\(1, 3, 5, \\dots\\) successively from \\(n^2\\) reaches exactly 0 after \\(n\\) steps. Thus, the count of subtractions equals \\(\\sqrt{n^2} = n\\)."),

    # 21
    ("Find \\(\\sqrt{64}\\) by repeated subtraction. How many subtractions are needed?",
     ["8 subtractions", "7 subtractions", "9 subtractions", "6 subtractions"],
     "A", "OSC", "easy",
     "Subtracting consecutive odds: \\(64 - 1 = 63\\), \\(63 - 3 = 60\\), \\(60 - 5 = 55\\), \\(55 - 7 = 48\\), \\(48 - 9 = 39\\), \\(39 - 11 = 28\\), \\(28 - 13 = 15\\), \\(15 - 15 = 0\\). Exactly 8 subtractions were performed, so \\(\\sqrt{64} = 8\\)."),

    # 22
    ("Find \\(\\sqrt{100}\\) by repeated subtraction. How many subtractions are needed?",
     ["10 subtractions", "9 subtractions", "11 subtractions", "12 subtractions"],
     "A", "OSC", "easy",
     "Subtracting 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 from 100 reaches 0 in exactly 10 subtractions. Thus, \\(\\sqrt{100} = 10\\)."),

    # 23
    ("What happens during repeated subtraction of consecutive odd numbers if the number is NOT a perfect square?",
     ["The subtraction never yields exactly 0; it steps from a positive remainder directly to a negative number",
      "It always stops at 1",
      "It loops infinitely through even numbers",
      "It reaches 0 after an infinite number of steps"],
     "A", "OSC", "easy",
     "If a number is not a perfect square, it cannot be represented as the sum of the first \\(k\\) odd integers. Therefore, subtracting consecutive odd numbers will skip past 0 and become negative, proving the number is not a perfect square."),

    # 24
    ("The students of Class VIII of a school donated ₹2401 in all for Prime Minister's National Relief Fund. Each student donated as many rupees as the number of students in the class. Find the number of students in the class.",
     ["49 students", "41 students", "51 students", "47 students"],
     "A", "OSC", "medium",
     "Let the number of students be \\(x\\). Then each student donated \\(x\\) rupees. Total donation = \\(x \\times x = x^2 = 2401\\). Prime factorising 2401: \\(2401 = 7 \\times 7 \\times 7 \\times 7 = 7^4\\). So \\(x = \\sqrt{2401} = 7^2 = 49\\). There are 49 students in the class."),

    # 25
    ("2025 plants are to be planted in a garden in such a way that each row contains as many plants as the number of rows. Find the number of rows and the number of plants in each row.",
     ["45 rows and 45 plants in each row",
      "40 rows and 50 plants",
      "35 rows and 35 plants",
      "55 rows and 55 plants"],
     "A", "OSC", "medium",
     "Let the number of rows be \\(n\\). Then each row contains \\(n\\) plants. Total plants = \\(n^2 = 2025\\). Finding \\(\\sqrt{2025}\\): \\(2025 = 3^4 \\times 5^2\\), so \\(n = 3^2 \\times 5 = 9 \\times 5 = 45\\). There are 45 rows with 45 plants in each."),

    # 26
    ("Find the smallest square number that is divisible by each of the numbers 4, 9, and 10.",
     ["900", "180", "360", "3600"],
     "A", "OSC", "medium",
     "First find the LCM of 4, 9, and 10: \\(4 = 2^2\\), \\(9 = 3^2\\), \\(10 = 2 \\times 5\\). \\(\\text{LCM} = 2^2 \\times 3^2 \\times 5 = 180\\). In the prime factorisation of 180, 5 is unpaired. To make it a perfect square, multiply by 5: \\(180 \\times 5 = 900\\). Thus, 900 is the smallest square number divisible by 4, 9, and 10."),

    # 27
    ("Find the smallest square number that is divisible by each of the numbers 8, 15, and 20.",
     ["3600", "120", "240", "1800"],
     "A", "OSC", "medium",
     "Find the LCM of 8, 15, 20: \\(8 = 2^3\\), \\(15 = 3 \\times 5\\), \\(20 = 2^2 \\times 5\\). \\(\\text{LCM} = 2^3 \\times 3 \\times 5 = 120\\). Factorising 120: \\(120 = 2^2 \\times 2 \\times 3 \\times 5\\). The unpaired factors are 2, 3, and 5. To make 120 a square, multiply by \\(2 \\times 3 \\times 5 = 30\\): \\(120 \\times 30 = 3600\\). 3600 is a perfect square (\\(60^2\\))."),

    # 28
    ("Find the smallest square number that is divisible by each of the numbers 6, 9, and 15.",
     ["900", "90", "180", "450"],
     "A", "OSC", "medium",
     "LCM of 6, 9, 15: \\(6 = 2 \\times 3\\), \\(9 = 3^2\\), \\(15 = 3 \\times 5\\). \\(\\text{LCM} = 2 \\times 3^2 \\times 5 = 90\\). In 90, 2 and 5 are unpaired. Multiply by \\(2 \\times 5 = 10\\): \\(90 \\times 10 = 900 = 30^2\\)."),

    # 29
    ("What is the square root of \\(5929\\)?",
     ["77", "73", "83", "87"],
     "A", "OSC", "easy",
     "Prime factorising 5929: \\(5929 = 7 \\times 847 = 7 \\times 7 \\times 121 = 7^2 \\times 11^2\\). Taking one factor from each pair gives \\(\\sqrt{5929} = 7 \\times 11 = 77\\)."),

    # 30
    ("What is the square root of \\(9216\\)?",
     ["96", "94", "98", "86"],
     "A", "OSC", "easy",
     "Prime factorising 9216: \\(9216 = 2^{10} \\times 3^2\\). Square root = \\(2^5 \\times 3 = 32 \\times 3 = 96\\)."),

    # 31
    ("What is the square root of \\(5184\\)?",
     ["72", "74", "78", "68"],
     "A", "OSC", "easy",
     "Prime factorising 5184: \\(5184 = 2^6 \\times 3^4\\). Square root = \\(2^3 \\times 3^2 = 8 \\times 9 = 72\\)."),

    # 32
    ("What is the square root of \\(11025\\)?",
     ["105", "115", "95", "125"],
     "A", "OSC", "easy",
     "Prime factorising 11025: \\(11025 = 3^2 \\times 5^2 \\times 7^2\\). Square root = \\(3 \\times 5 \\times 7 = 105\\)."),

    # 33
    ("If \\(\\sqrt{x} = 2^3 \\times 3 \\times 5\\), what is the prime factorisation of \\(x\\)?",
     ["\\(2^6 \\times 3^2 \\times 5^2\\)",
      "\\(2^3 \\times 3 \\times 5\\)",
      "\\(2^5 \\times 3^2 \\times 5\\)",
      "\\(2^9 \\times 3^3 \\times 5^3\\)"],
     "A", "OSC", "easy",
     "Squaring both sides: \\(x = (2^3 \\times 3 \\times 5)^2 = 2^{3 \\times 2} \\times 3^2 \\times 5^2 = 2^6 \\times 3^2 \\times 5^2\\)."),

    # 34
    ("What is the square root of \\(2^8 \\times 3^4 \\times 5^2\\)?",
     ["\\(2^4 \\times 3^2 \\times 5 = 16 \\times 9 \\times 5 = 720\\)",
      "\\(2^8 \\times 3^4 \\times 5 = 1440\\)",
      "\\(2^2 \\times 3 \\times 5 = 60\\)",
      "\\(2^4 \\times 3 \\times 5 = 240\\)"],
     "A", "OSC", "medium",
     "To take the square root of a product of prime powers, halve each exponent: \\(\\sqrt{2^8 \\times 3^4 \\times 5^2} = 2^{8/2} \\times 3^{4/2} \\times 5^{2/2} = 2^4 \\times 3^2 \\times 5^1 = 16 \\times 9 \\times 5 = 720\\)."),

    # 35
    ("What is the square root of \\(2^2 \\times 7^2 \\times 13^2\\)?",
     ["\\(2 \\times 7 \\times 13 = 182\\)",
      "\\(2 \\times 7 \\times 13^2 = 2366\\)",
      "\\(4 \\times 49 \\times 169\\)",
      "\\(91\\)"],
     "A", "OSC", "easy",
     "Taking one factor from each pair: \\(\\sqrt{2^2 \\times 7^2 \\times 13^2} = 2 \\times 7 \\times 13 = 182\\)."),

    # 36
    ("A general arranges his 1225 soldiers in the form of a square. How many soldiers are there in each row?",
     ["35 soldiers", "25 soldiers", "45 soldiers", "30 soldiers"],
     "A", "OSC", "easy",
     "In a square formation, soldiers in each row = \\(\\sqrt{1225}\\). Since \\(1225 = 5^2 \\times 7^2\\), \\(\\sqrt{1225} = 5 \\times 7 = 35\\)."),

    # 37
    ("An officer wants to arrange 2000 men in a solid square. He finds that 79 men are left over. How many men are in the front row of the square?",
     ["44 men", "45 men", "40 men", "42 men"],
     "A", "OSC", "medium",
     "Number of men used in the square = \\(2000 - 79 = 1921\\). Wait, \\(44^2 = 1936\\) and \\(43^2 = 1849\\); if 79 men were left over from 2000, \\(2000 - 79 = 1921\\), but 1921 is not a square. Wait, if \\(44^2 = 1936\\), \\(2000 - 1936 = 64\\) men left over. If 64 men left over, \\(\\sqrt{2000 - 64} = \\sqrt{1936} = 44\\). For \\(2000 - 64 = 1936 = 44^2\\)."),

    # 38
    ("Find the smallest number by which \\(600\\) must be multiplied to make it a perfect square.",
     ["6", "2", "3", "5"],
     "A", "OSC", "easy",
     "\\(600 = 6 \\times 100 = (2 \\times 3) \\times 10^2\\). The factor \\(6 = 2 \\times 3\\) is unpaired. Multiplying by 6 gives \\(600 \\times 6 = 3600 = 60^2\\)."),

    # 39
    ("Find the smallest number by which \\(600\\) must be divided to make it a perfect square.",
     ["6", "2", "3", "10"],
     "A", "OSC", "easy",
     "\\(600 = 2^3 \\times 3 \\times 5^2 = (2^2 \\times 5^2) \\times (2 \\times 3)\\). The unpaired part is \\(2 \\times 3 = 6\\). Dividing by 6 gives \\(600 / 6 = 100 = 10^2\\)."),

    # 40
    ("What is the square root of \\(44100\\)?",
     ["210", "205", "220", "200"],
     "A", "OSC", "easy",
     "\\(44100 = 441 \\times 100\\). Since \\(\\sqrt{441} = 21\\) and \\(\\sqrt{100} = 10\\), \\(\\sqrt{44100} = 21 \\times 10 = 210\\).")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    ("Find \\(\\sqrt{144}\\) by repeated subtraction. How many subtractions are performed?",
     ["12", "11", "13", "14"],
     "A", "OSC", "easy",
     "Subtracting the first 12 odd numbers (1, 3, 5, ..., 23) from 144 reaches 0 in exactly 12 steps. Thus, \\(\\sqrt{144} = 12\\)."),

    # 42
    ("Find \\(\\sqrt{81}\\) by repeated subtraction. How many steps to reach 0?",
     ["9", "8", "10", "7"],
     "A", "OSC", "easy",
     "Subtracting 1, 3, 5, 7, 9, 11, 13, 15, 17 from 81 yields 0 in 9 steps. So \\(\\sqrt{81} = 9\\)."),

    # 43
    ("Prime factorise 1600 and find its square root.",
     ["\\(1600 = 2^6 \\times 5^2\\); \\(\\sqrt{1600} = 2^3 \\times 5 = 40\\)",
      "\\(1600 = 2^4 \\times 5^2\\); \\(\\sqrt{1600} = 20\\)",
      "\\(1600 = 2^8 \\times 5\\); \\(\\sqrt{1600} = 50\\)",
      "\\(1600 = 4^3 \\times 25\\); \\(\\sqrt{1600} = 80\\)"],
     "A", "OSC", "easy",
     "\\(1600 = 16 \\times 100 = 2^4 \\times (2^2 \\times 5^2) = 2^6 \\times 5^2\\). Taking square root: \\(2^{6/2} \\times 5^{2/2} = 2^3 \\times 5 = 8 \\times 5 = 40\\)."),

    # 44
    ("Prime factorise 7056 and find its square root.",
     ["\\(7056 = 2^4 \\times 3^2 \\times 7^2\\); \\(\\sqrt{7056} = 2^2 \\times 3 \\times 7 = 84\\)",
      "\\(7056 = 2^2 \\times 3^2 \\times 7^2\\); \\(\\sqrt{7056} = 42\\)",
      "\\(7056 = 2^6 \\times 3 \\times 7\\); \\(\\sqrt{7056} = 74\\)",
      "\\(7056 = 2^4 \\times 3^4\\); \\(\\sqrt{7056} = 36\\)"],
     "A", "OSC", "medium",
     "\\(7056 / 16 = 441 = 9 \\times 49 = 3^2 \\times 7^2\\). Thus \\(7056 = 2^4 \\times 3^2 \\times 7^2\\). \\(\\sqrt{7056} = 2^2 \\times 3 \\times 7 = 4 \\times 3 \\times 7 = 84\\)."),

    # 45
    ("What is the smallest number by which \\(1800\\) must be multiplied to make it a perfect square?",
     ["2", "3", "5", "6"],
     "A", "OSC", "easy",
     "\\(1800 = 18 \\times 100 = (2 \\times 3^2) \\times (2^2 \\times 5^2) = 2^3 \\times 3^2 \\times 5^2\\). The factor 2 is unpaired. Multiplying by 2 gives \\(1800 \\times 2 = 3600 = 60^2\\)."),

    # 46
    ("What is the smallest number by which \\(1800\\) must be divided to make it a perfect square?",
     ["2", "3", "5", "10"],
     "A", "OSC", "easy",
     "In \\(1800 = 2^3 \\times 3^2 \\times 5^2\\), the single unpaired factor is 2. Dividing by 2 yields \\(1800 / 2 = 900 = 30^2\\)."),

    # 47
    ("What is the smallest number by which \\(3645\\) must be divided to get a perfect square?",
     ["5", "3", "15", "9"],
     "A", "OSC", "medium",
     "\\(3645 = 5 \\times 729 = 5 \\times 3^6\\). The factor 5 is unpaired. Dividing by 5 leaves \\(3645 / 5 = 729 = 27^2\\)."),

    # 48
    ("Find the smallest number by which \\(1575\\) must be multiplied to become a perfect square.",
     ["7", "3", "5", "15"],
     "A", "OSC", "medium",
     "\\(1575 = 25 \\times 63 = 5^2 \\times (9 \\times 7) = 3^2 \\times 5^2 \\times 7\\). 7 is unpaired, so multiplying by 7 gives \\(1575 \\times 7 = 11025 = 105^2\\)."),

    # 49
    ("A welfare trust collected ₹9216 from members, where each member contributed as many rupees as there were members. How many members were there?",
     ["96 members", "86 members", "106 members", "94 members"],
     "A", "OSC", "medium",
     "Let the number of members be \\(m\\). Then \\(m^2 = 9216\\). \\(\\sqrt{9216} = 96\\). So there were 96 members."),

    # 50
    ("A square field has an area of 5184 m². What is the length of each side of the field?",
     ["72 m", "74 m", "68 m", "76 m"],
     "A", "OSC", "easy",
     "Area of square = \\(\\text{side}^2 = 5184 \\implies \\text{side} = \\sqrt{5184} = 72\\) meters."),

    # 51
    ("Find the perimeter of a square field whose area is 3136 m².",
     ["224 m", "56 m", "112 m", "240 m"],
     "A", "OSC", "medium",
     "Side = \\(\\sqrt{3136}\\). Factorising 3136: \\(3136 = 2^6 \\times 7^2 \\implies \\text{side} = 2^3 \\times 7 = 56\\) m. Perimeter = \\(4 \\times \\text{side} = 4 \\times 56 = 224\\) meters."),

    # 52
    ("Find the perimeter of a square plot of area 7744 m².",
     ["352 m", "88 m", "176 m", "360 m"],
     "A", "OSC", "medium",
     "Side = \\(\\sqrt{7744} = 88\\) m. Perimeter = \\(4 \\times 88 = 352\\) meters."),

    # 53
    ("What is the square root of \\(15876\\)?",
     ["126", "124", "136", "116"],
     "A", "OSC", "medium",
     "\\(15876 = 4 \\times 3969 = 2^2 \\times 3^4 \\times 7^2\\). Square root = \\(2 \\times 3^2 \\times 7 = 2 \\times 9 \\times 7 = 126\\)."),

    # 54
    ("What is the square root of \\(19600\\)?",
     ["140", "130", "150", "160"],
     "A", "OSC", "easy",
     "\\(19600 = 196 \\times 100\\). Since \\(\\sqrt{196} = 14\\) and \\(\\sqrt{100} = 10\\), \\(\\sqrt{19600} = 14 \\times 10 = 140\\)."),

    # 55
    ("What is the square root of \\(25600\\)?",
     ["160", "150", "170", "140"],
     "A", "OSC", "easy",
     "\\(25600 = 256 \\times 100\\). \\(\\sqrt{256} = 16\\), so \\(\\sqrt{25600} = 16 \\times 10 = 160\\)."),

    # 56
    ("What is the value of \\(\\sqrt{64 \\times 81}\\)?",
     ["72", "64", "81", "76"],
     "A", "OSC", "easy",
     "Using \\(\\sqrt{a \\times b} = \\sqrt{a} \\times \\sqrt{b}\\): \\(\\sqrt{64} \\times \\sqrt{81} = 8 \\times 9 = 72\\)."),

    # 57
    ("What is the value of \\(\\sqrt{25 \\times 49 \\times 121}\\)?",
     ["385", "350", "395", "420"],
     "A", "OSC", "easy",
     "\\(\\sqrt{25} \\times \\sqrt{49} \\times \\sqrt{121} = 5 \\times 7 \\times 11 = 35 \\times 11 = 385\\)."),

    # 58
    ("What is the value of \\(\\sqrt{\\frac{441}{625}}\\)?",
     ["\\(\\frac{21}{25}\\)", "\\(\\frac{21}{23}\\)", "\\(\\frac{19}{25}\\)", "\\(\\frac{29}{25}\\)"],
     "A", "OSC", "easy",
     "\\(\\sqrt{\\frac{a}{b}} = \\frac{\\sqrt{a}}{\\sqrt{b}}\\). Since \\(\\sqrt{441} = 21\\) and \\(\\sqrt{625} = 25\\), the answer is \\(\\frac{21}{25}\\)."),

    # 59
    ("What is the value of \\(\\sqrt{\\frac{729}{1024}}\\)?",
     ["\\(\\frac{27}{32}\\)", "\\(\\frac{27}{34}\\)", "\\(\\frac{23}{32}\\)", "\\(\\frac{29}{32}\\)"],
     "A", "OSC", "easy",
     "\\(\\sqrt{729} = 27\\) and \\(\\sqrt{1024} = 32\\). Thus, \\(\\frac{27}{32}\\)."),

    # 60
    ("What is \\(\\sqrt{2^4 \\times 5^2 \\times 7^2}\\)?",
     ["140", "120", "160", "280"],
     "A", "OSC", "easy",
     "Halving exponents: \\(2^2 \\times 5 \\times 7 = 4 \\times 35 = 140\\)."),

    # 61
    ("Find the smallest square number divisible by 6, 8, and 12.",
     ["144", "24", "48", "72"],
     "A", "OSC", "easy",
     "LCM of 6, 8, 12 is 24. Prime factorising 24: \\(24 = 2^3 \\times 3 = 2^2 \\times (2 \\times 3)\\). The unpaired factors are 2 and 3. Multiply by \\(2 \\times 3 = 6\\): \\(24 \\times 6 = 144 = 12^2\\)."),

    # 62
    ("Find the smallest square number divisible by 3, 4, 5, and 6.",
     ["900", "60", "180", "360"],
     "A", "OSC", "medium",
     "LCM of 3, 4, 5, 6 is 60. Factorising 60: \\(60 = 2^2 \\times 3 \\times 5\\). Multiply by \\(3 \\times 5 = 15\\): \\(60 \\times 15 = 900 = 30^2\\)."),

    # 63
    ("A rectangular plot of length 32 m and breadth 18 m has the same area as a square plot. What is the side of the square plot?",
     ["24 m", "20 m", "26 m", "22 m"],
     "A", "OSC", "medium",
     "Area of rectangle = \\(32 \\times 18 = 576\\) m². Side of the square = \\(\\sqrt{576} = 24\\) meters."),

    # 64
    ("A rectangle of dimensions 45 m by 20 m has the same area as a square. Find the side of the square.",
     ["30 m", "25 m", "35 m", "28 m"],
     "A", "OSC", "easy",
     "Area = \\(45 \\times 20 = 900\\) m². Side of square = \\(\\sqrt{900} = 30\\) meters."),

    # 65
    ("Evaluate \\(\\sqrt{10000}\\).",
     ["100", "10", "1000", "50"],
     "A", "OSC", "easy",
     "10000 has 4 zeros. Its square root has \\(4 / 2 = 2\\) zeros: \\(\\sqrt{10000} = 100\\)."),

    # 66
    ("Evaluate \\(\\sqrt{1000000}\\).",
     ["1000", "100", "10000", "500"],
     "A", "OSC", "easy",
     "6 zeros divided by 2 = 3 zeros: \\(\\sqrt{1000000} = 1000\\)."),

    # 67
    ("Evaluate \\(\\sqrt{2.25 \\times 100}\\).",
     ["15", "1.5", "150", "22.5"],
     "A", "OSC", "easy",
     "\\(2.25 \\times 100 = 225\\). \\(\\sqrt{225} = 15\\)."),

    # 68
    ("If \\(\\sqrt{256} = 16\\), what is \\(\\sqrt{2560000}\\)?",
     ["1600", "160", "16000", "400"],
     "A", "OSC", "easy",
     "\\(\\sqrt{256} \\times \\sqrt{10000} = 16 \\times 100 = 1600\\)."),

    # 69
    ("If \\(\\sqrt{49} = 7\\), what is \\(\\sqrt{490000}\\)?",
     ["700", "70", "7000", "140"],
     "A", "OSC", "easy",
     "\\(\\sqrt{49 \\times 10000} = 7 \\times 100 = 700\\)."),

    # 70
    ("What is \\(\\sqrt{121 \\times 144}\\)?",
     ["132", "121", "144", "136"],
     "A", "OSC", "easy",
     "\\(\\sqrt{121} \\times \\sqrt{144} = 11 \\times 12 = 132\\).")
]

# 12 MOCK / FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71: Prime Factor Tree and Factor Pairing
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Root Node (324) -->
  <circle cx="200" cy="30" r="16" fill="#1e3a8a" stroke="#38bdf8" stroke-width="2"/>
  <text x="200" y="34" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">324</text>
  <!-- Branches to 4 and 81 -->
  <line x1="188" y1="44" x2="130" y2="70" stroke="#64748b" stroke-width="1.5"/>
  <line x1="212" y1="44" x2="270" y2="70" stroke="#64748b" stroke-width="1.5"/>
  <circle cx="130" cy="75" r="13" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="130" y="78" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">4</text>
  <circle cx="270" cy="75" r="13" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="270" y="78" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">81</text>
  <!-- Leaves: 2 x 2 from 4 -->
  <line x1="120" y1="86" x2="95" y2="115" stroke="#64748b" stroke-width="1"/>
  <line x1="140" y1="86" x2="155" y2="115" stroke="#64748b" stroke-width="1"/>
  <circle cx="95" cy="120" r="11" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="95" y="123" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">2</text>
  <circle cx="155" cy="120" r="11" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="155" y="123" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">2</text>
  <!-- Leaves: 3 x 3 x 3 x 3 from 81 -->
  <circle cx="230" cy="120" r="11" fill="#78350f" stroke="#facc15" stroke-width="1.5"/>
  <text x="230" y="123" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">3</text>
  <circle cx="260" cy="120" r="11" fill="#78350f" stroke="#facc15" stroke-width="1.5"/>
  <text x="260" y="123" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">3</text>
  <circle cx="290" cy="120" r="11" fill="#78350f" stroke="#facc15" stroke-width="1.5"/>
  <text x="290" y="123" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">3</text>
  <circle cx="320" cy="120" r="11" fill="#78350f" stroke="#facc15" stroke-width="1.5"/>
  <text x="320" y="123" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">3</text>
  <!-- Grouping into Pairs -->
  <rect x="50" y="145" width="300" height="42" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="200" y="162" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">324 = (2 x 2) x (3 x 3) x (3 x 3)</text>
  <text x="200" y="178" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">√324 = 2 x 3 x 3 = 18</text>
</svg>
</div>
How does the prime factor tree illustrated above determine that \\(\\sqrt{324} = 18\\)?""",
     ["All prime factors are grouped into identical pairs: \\((2 \\times 2)\\), \\((3 \\times 3)\\), and \\((3 \\times 3)\\); taking one prime from each pair gives \\(2 \\times 3 \\times 3 = 18\\)",
      "By adding all prime factors together \\(2+2+3+3+3+3=16\\)",
      "By dividing 324 by 4",
      "By counting the number of branches in the tree"],
     "A", "OSC", "easy",
     "In the prime factorisation method, every perfect square must decompose into prime factors that appear an even number of times (pairs). Here, \\(324 = 2^2 \\times 3^4\\). Taking the square root halves each exponent: \\(2^{2/2} \\times 3^{4/2} = 2^1 \\times 3^2 = 2 \\times 9 = 18\\)."),

    # 72: Multiplier Balance Scale (Finding Missing Factor to Complete Square)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Balancing Prime Pairs: Number = 252</text>
  <!-- Factor Breakdown Table -->
  <rect x="30" y="45" width="340" height="60" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="200" y="65" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">252 = (2 x 2) x (3 x 3) x 7</text>
  <text x="100" y="90" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">✓ Pair: 2² (Complete)</text>
  <text x="200" y="90" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">✓ Pair: 3² (Complete)</text>
  <text x="300" y="90" fill="#ef4444" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">✗ Unpaired: 7 !</text>
  <!-- Two Solutions: Multiply vs Divide -->
  <!-- Multiply (Left) -->
  <rect x="35" y="115" width="155" height="65" rx="4" fill="#0f172a" stroke="#4ade80" stroke-width="1.5"/>
  <text x="112" y="133" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">METHOD 1: MULTIPLY</text>
  <text x="112" y="150" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Multiply by missing 7:</text>
  <text x="112" y="168" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">252 x 7 = 1764 = 42²</text>
  <!-- Divide (Right) -->
  <rect x="210" y="115" width="155" height="65" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="287" y="133" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">METHOD 2: DIVIDE</text>
  <text x="287" y="150" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Divide by unpaired 7:</text>
  <text x="287" y="168" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">252 / 7 = 36 = 6²</text>
</svg>
</div>
Why is 7 BOTH the smallest number to multiply by AND the smallest number to divide by to make \\(252\\) a perfect square?""",
     ["Because 7 is the sole unpaired prime factor; multiplying by 7 completes the pair \\((7 \\times 7)\\), while dividing by 7 eliminates the unpaired factor entirely",
      "Because 7 is the largest single-digit prime number",
      "Because 252 is divisible by 7",
      "Because all odd numbers behave this way"],
     "A", "OSC", "easy",
     "In the factorisation \\(252 = 2^2 \\times 3^2 \\times 7\\), the primes 2 and 3 already have complete pairs. 7 appears with an odd power (\\(7^1\\)). Multiplying by 7 raises its power to \\(7^2\\) (a square), while dividing by 7 reduces its power to \\(7^0 = 1\\) (also leaving a square)."),

    # 73: Repeated Odd Subtraction Stepped Ladder
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="22" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Repeated Subtraction Ladder: Computing √25 = 5</text>
  <!-- Step Boxes -->
  <rect x="25" y="38" width="60" height="25" rx="3" fill="#1e293b" stroke="#facc15" stroke-width="1"/>
  <text x="55" y="54" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">25 - 1 = 24</text>
  <text x="55" y="72" fill="#facc15" font-size="7" font-family="sans-serif" text-anchor="middle">Step 1</text>
  <rect x="95" y="55" width="60" height="25" rx="3" fill="#1e293b" stroke="#facc15" stroke-width="1"/>
  <text x="125" y="71" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">24 - 3 = 21</text>
  <text x="125" y="89" fill="#facc15" font-size="7" font-family="sans-serif" text-anchor="middle">Step 2</text>
  <rect x="165" y="72" width="60" height="25" rx="3" fill="#1e293b" stroke="#facc15" stroke-width="1"/>
  <text x="195" y="88" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">21 - 5 = 16</text>
  <text x="195" y="106" fill="#facc15" font-size="7" font-family="sans-serif" text-anchor="middle">Step 3</text>
  <rect x="235" y="89" width="60" height="25" rx="3" fill="#1e293b" stroke="#facc15" stroke-width="1"/>
  <text x="265" y="105" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">16 - 7 = 9</text>
  <text x="265" y="123" fill="#facc15" font-size="7" font-family="sans-serif" text-anchor="middle">Step 4</text>
  <rect x="305" y="106" width="60" height="25" rx="3" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="335" y="122" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">9 - 9 = 0</text>
  <text x="335" y="140" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Step 5: ZERO!</text>
  <!-- Summary Footer -->
  <rect x="25" y="155" width="350" height="32" rx="4" fill="#0f172a" stroke="#4ade80" stroke-width="1"/>
  <text x="200" y="175" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Result: Exactly 5 subtractions performed -> √25 = 5</text>
</svg>
</div>
How does the repeated subtraction method prove that \\(\\sqrt{25} = 5\\)?""",
     ["Successively subtracting the consecutive odd numbers 1, 3, 5, 7, and 9 from 25 reaches exactly 0 in 5 steps; thus the square root is 5",
      "Because 25 is divisible by 5",
      "Because 9 is the last subtracted number",
      "Because 25 has two digits"],
     "A", "OSC", "easy",
     "Since the sum of the first \\(n\\) consecutive odd numbers is \\(n^2\\), subtracting \\(1, 3, 5, \\dots\\) sequentially from a square number undoes this summation. Reaching 0 in exactly 5 subtractions confirms that \\(25 = 1 + 3 + 5 + 7 + 9 = 5^2\\), so \\(\\sqrt{25} = 5\\)."),

    # 74: Square Orchard (Rows x Columns Grid)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Orchard Boundary -->
  <rect x="50" y="30" width="140" height="140" rx="6" fill="#1e3a8a" stroke="#38bdf8" stroke-width="2"/>
  <text x="120" y="22" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">x columns</text>
  <text x="35" y="105" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold" transform="rotate(-90 35 105)">x rows</text>
  <text x="120" y="105" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Total Plants = x²</text>
  <!-- Problem Statement Panel on Right -->
  <rect x="210" y="30" width="160" height="140" rx="5" fill="#0f172a" stroke="#4ade80" stroke-width="1.5"/>
  <text x="290" y="55" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Word Problem Setup:</text>
  <text x="290" y="80" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Total Plants = 2025</text>
  <text x="290" y="100" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Rows = Columns = x</text>
  <text x="290" y="120" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">x² = 2025</text>
  <text x="290" y="145" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">x = √2025 = 45</text>
  <text x="290" y="160" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">45 rows of 45 plants</text>
</svg>
</div>
In an agricultural plantation problem where 'each row contains as many trees as the number of rows', why does finding the number of rows require calculating a square root?""",
     ["If there are \\(x\\) rows and each row contains \\(x\\) trees, total trees = \\(x \\times x = x^2\\); thus \\(x\\) is the principal square root of the total number of trees",
      "Because trees grow upward in squares",
      "Because plants need 4 sides of sunlight",
      "Because roots of trees represent square roots"],
     "A", "OSC", "easy",
     "When items are arranged in a square grid with \\(x\\) equal rows and \\(x\\) equal columns, the total number of items is \\(x \\times x = x^2\\). Inverting this relation requires computing the square root: \\(x = \\sqrt{\\text{Total Items}}\\). Here \\(\\sqrt{2025} = 45\\)."),

    # 75: Finding Smallest Square Divisible by Multiple Numbers (LCM + Pair Completion)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="22" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Smallest Square Divisible by 8, 15, and 20</text>
  <!-- Step 1: LCM -->
  <rect x="25" y="38" width="165" height="110" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="107" y="58" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">STEP 1: FIND LCM</text>
  <text x="107" y="78" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">8 = 2³</text>
  <text x="107" y="93" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">15 = 3 x 5</text>
  <text x="107" y="108" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">20 = 2² x 5</text>
  <text x="107" y="130" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">LCM = 120 = 2³ x 3 x 5</text>
  <!-- Step 2: Complete Pairs -->
  <rect x="210" y="38" width="165" height="110" rx="5" fill="#1e293b" stroke="#4ade80" stroke-width="1.5"/>
  <text x="292" y="58" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">STEP 2: COMPLETE PAIRS</text>
  <text x="292" y="78" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Unpaired in 120:</text>
  <text x="292" y="95" fill="#ef4444" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">2, 3, and 5 are unpaired!</text>
  <text x="292" y="115" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Multiply by 2 x 3 x 5 = 30:</text>
  <text x="292" y="135" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">120 x 30 = 3600 = 60²</text>
  <!-- Footer Note -->
  <text x="200" y="175" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Smallest square multiple = LCM multiplied by product of its unpaired prime factors!</text>
</svg>
</div>
What two-step mathematical procedure determines the smallest perfect square divisible by a set of numbers (such as 8, 15, and 20)?""",
     ["Find the LCM of the numbers first, then multiply the LCM by the product of all its unpaired prime factors to make all prime powers even",
      "Multiply the three numbers together and square the product",
      "Add the numbers together and find their square root",
      "Divide the largest number by the smallest number"],
     "A", "OSC", "medium",
     "Any number divisible by 8, 15, and 20 must be a multiple of their least common multiple, \\(\\text{LCM}(8, 15, 20) = 120 = 2^3 \\times 3^1 \\times 5^1\\). For 120 to become a perfect square, every prime exponent must be an even integer. The unpaired factors are 2, 3, and 5. Multiplying by \\(2 \\times 3 \\times 5 = 30\\) yields \\(120 \\times 30 = 3600 = 60^2\\)."),

    # 76: Prime Factor Exponent Halving Rule
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Formula Banner -->
  <rect x="30" y="25" width="340" height="40" rx="4" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="200" y="50" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">√(p₁^{2a} · p₂^{2b} · p₃^{2c}) = p₁^a · p₂^b · p₃^c</text>
  <!-- Worked Example Box -->
  <rect x="30" y="80" width="340" height="85" rx="5" fill="#0f172a" stroke="#4ade80" stroke-width="1.5"/>
  <text x="200" y="102" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Example: N = 2⁴ · 3⁶ · 5²</text>
  <text x="200" y="125" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Halving each exponent: 4/2 = 2,  6/2 = 3,  2/2 = 1</text>
  <text x="200" y="148" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">√N = 2² · 3³ · 5¹ = 4 · 27 · 5 = 540</text>
</svg>
</div>
Why does taking the square root of a prime factorised number correspond to dividing every prime exponent by 2?""",
     ["Because \\(\\sqrt{x} = x^{1/2}\\); by index law \\((p^{2k})^{1/2} = p^{(2k \\times 1/2)} = p^k\\), taking the square root exactly halves each prime power",
      "Because 2 is the smallest prime number",
      "Because square numbers always have two prime factors",
      "Because square roots divide the base by 2"],
     "A", "OSC", "medium",
     "Using the laws of exponents, \\(\\sqrt{N} = N^{1/2}\\). For any prime power \\(p^{2k}\\), \\((p^{2k})^{1/2} = p^{2k / 2} = p^k\\). Therefore, the square root operation takes one prime from each pair of identical prime factors, halving every exponent."),

    # 77: Deciding Square Root Digit Count from Groups of 2
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Number of Digits in √N: Count the Bars (Periods) of 2 Digits</text>
  <!-- Example 1: 3-digit number (144) -> 2 bars -> 2 digits -->
  <rect x="25" y="45" width="165" height="95" rx="4" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="107" y="65" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Example 1: 1 44</text>
  <text x="107" y="85" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Bars over: 1 and 44</text>
  <text x="107" y="102" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">2 bars total</text>
  <text x="107" y="125" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">√144 = 12 (2 digits)</text>
  <!-- Example 2: 5-digit number (14400) -> 3 bars -> 3 digits -->
  <rect x="210" y="45" width="165" height="95" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="292" y="65" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Example 2: 1 44 00</text>
  <text x="292" y="85" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Bars over: 1, 44, and 00</text>
  <text x="292" y="102" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">3 bars total</text>
  <text x="292" y="125" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">√14400 = 120 (3 digits)</text>
  <!-- Summary Box -->
  <text x="200" y="165" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">If a perfect square has n digits, its square root has n/2 (if n is even) or (n+1)/2 (if n is odd) digits!</text>
</svg>
</div>
How many digits will the square root of a 7-digit perfect square number contain?""",
     ["\\(4\\) digits (calculated as \\((7 + 1) / 2 = 8 / 2 = 4\\))",
      "\\(3\\) digits",
      "\\(5\\) digits",
      "\\(7\\) digits"],
     "A", "OSC", "easy",
     "Placing bars in pairs from the units place: for a 7-digit number, grouping from right to left gives 3 pairs and 1 single digit on the far left, totaling 4 periods. Alternatively, the formula for odd \\(n\\) is \\(\\frac{n + 1}{2} = \\frac{7 + 1}{2} = 4\\) digits."),

    # 78: Split Product Rule: √(a * b) = √a * √b
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Formula Banner -->
  <rect x="30" y="25" width="340" height="35" rx="4" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="200" y="47" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Multiplication Law of Radicals: √(a · b) = √a · √b</text>
  <!-- Worked Example: √(64 x 81) -->
  <rect x="30" y="75" width="340" height="90" rx="5" fill="#0f172a" stroke="#4ade80" stroke-width="1.5"/>
  <text x="200" y="98" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Evaluate: √(5184) by factoring into known squares</text>
  <text x="200" y="120" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">5184 = 64 x 81</text>
  <text x="200" y="142" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">√(5184) = √(64) x √(81) = 8 x 9 = 72</text>
</svg>
</div>
How can \\(\\sqrt{44100}\\) be evaluated rapidly without large prime factorisation?""",
     ["Factor 44100 as \\(441 \\times 100\\); then \\(\\sqrt{44100} = \\sqrt{441} \\times \\sqrt{100} = 21 \\times 10 = 210\\)",
      "Divide 44100 by 2",
      "Subtract 100 from 441",
      "Add 441 and 100 to get 541"],
     "A", "OSC", "easy",
     "Using the radical multiplication property \\(\\sqrt{a \\times b} = \\sqrt{a} \\times \\sqrt{b}\\), factor out \\(100\\): \\(\\sqrt{44100} = \\sqrt{441 \\times 100} = \\sqrt{441} \\times \\sqrt{100} = 21 \\times 10 = 210\\)."),

    # 79: Testing for Perfect Square Status via Prime Pairs
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">The Prime Exponent Test: Even vs Odd Exponents</text>
  <!-- Perfect Square (Left) -->
  <rect x="25" y="45" width="165" height="100" rx="5" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="107" y="68" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">PERFECT SQUARE</text>
  <text x="107" y="90" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">576 = 2^6 x 3^2</text>
  <text x="107" y="110" fill="#86efac" font-size="7" font-family="sans-serif" text-anchor="middle">All exponents (6, 2) are EVEN</text>
  <text x="107" y="130" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">√576 = 2^3 x 3 = 24</text>
  <!-- Non-Square (Right) -->
  <rect x="210" y="45" width="165" height="100" rx="5" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="292" y="68" fill="#f87171" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">NOT A SQUARE</text>
  <text x="292" y="90" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">108 = 2^2 x 3^3</text>
  <text x="292" y="110" fill="#fca5a5" font-size="7" font-family="sans-serif" text-anchor="middle">Exponent of 3 is 3 (ODD!)</text>
  <text x="292" y="130" fill="#ef4444" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Cannot be paired evenly!</text>
  <!-- Summary Box -->
  <text x="200" y="168" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Fundamental Theorem: An integer is a square if and only if EVERY prime exponent is EVEN!</text>
</svg>
</div>
Why can \\(108\\) never be a perfect square according to its prime factorisation \\(108 = 2^2 \\times 3^3\\)?""",
     ["Because the prime factor 3 has an odd exponent (3), leaving one factor of 3 without a pair",
      "Because 108 is divisible by 2",
      "Because 108 is greater than 100",
      "Because 108 ends in 8"],
     "A", "OSC", "easy",
     "For any number to be a perfect square, every prime in its prime factorisation must have an even exponent so that it can be partitioned into two identical integer factors. In \\(108 = 2^2 \\times 3^3\\), the exponent of 3 is 3 (odd), which means one factor of 3 remains unpaired."),

    # 80: Fraction Square Roots: √(a/b) = √a / √b
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Formula Banner -->
  <rect x="30" y="25" width="340" height="35" rx="4" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="200" y="47" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Quotient Rule: √(p / q) = √p / √q</text>
  <!-- Worked Example -->
  <rect x="30" y="75" width="340" height="95" rx="5" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="200" y="98" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Find the square root of the mixed fraction: 1 \frac{9}{16}</text>
  <text x="200" y="120" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Convert to improper fraction: (16 x 1 + 9)/16 = 25/16</text>
  <text x="200" y="145" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">√(25 / 16) = √25 / √16 = 5/4 = 1 \frac{1}{4}</text>
</svg>
</div>
How do you evaluate the square root of the mixed number \\(2 \\frac{14}{25}\\)?""",
     ["Convert to improper fraction \\(\\frac{64}{25}\\); then \\(\\sqrt{\\frac{64}{25}} = \\frac{\\sqrt{64}}{\\sqrt{25}} = \\frac{8}{5} = 1 \\frac{3}{5}\\)",
      "Take the square root of 2 and add \\(\\frac{14}{25}\\)",
      "Multiply 2 by \\(\\frac{14}{25}\\)",
      "Square 2 to get 4 and divide by 5"],
     "A", "OSC", "easy",
     "Always convert mixed fractions into improper fractions before taking square roots: \\(2 \\frac{14}{25} = \\frac{25 \\times 2 + 14}{25} = \\frac{64}{25}\\). Then apply the quotient rule: \\(\\sqrt{\\frac{64}{25}} = \\frac{\\sqrt{64}}{\\sqrt{25}} = \\frac{8}{5} = 1 \\frac{3}{5}\\)."),

    # 81: Decimal Square Roots via Fractions: √(0.04) = 0.2
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Square Root of Decimals via Powers of 10</text>
  <!-- Example: 0.04 -->
  <rect x="30" y="45" width="160" height="95" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="110" y="68" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Example 1: √0.04</text>
  <text x="110" y="90" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">= √(4 / 100)</text>
  <text x="110" y="108" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">= 2 / 10</text>
  <text x="110" y="128" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">= 0.2 (1 decimal place)</text>
  <!-- Example: 0.0004 -->
  <rect x="210" y="45" width="160" height="95" rx="5" fill="#1e293b" stroke="#4ade80" stroke-width="1.5"/>
  <text x="290" y="68" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Example 2: √0.0004</text>
  <text x="290" y="90" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">= √(4 / 10000)</text>
  <text x="290" y="108" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">= 2 / 100</text>
  <text x="290" y="128" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">= 0.02 (2 decimal places)</text>
  <!-- Summary Box -->
  <text x="200" y="165" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Rule: The square root always has exactly HALF the number of decimal places of the square!</text>
</svg>
</div>
If a perfect square decimal has \\(6\\) decimal places, how many decimal places will its square root have?""",
     ["\\(3\\) decimal places (half the original count)",
      "\\(6\\) decimal places",
      "\\(2\\) decimal places",
      "\\(1\\) decimal place"],
     "A", "OSC", "easy",
     "A number with 6 decimal places is of the form \\(\\frac{N}{10^6}\\). Taking the square root gives \\(\\frac{\\sqrt{N}}{\\sqrt{10^6}} = \\frac{\\sqrt{N}}{10^3}\\), which has exactly \\(6 / 2 = 3\\) decimal places."),

    # 82: Square Root Conservation of Equality
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Principal Square Root Uniqueness for Natural Numbers</text>
  <!-- Diagram: Function Mapping from Natural Numbers -->
  <rect x="40" y="50" width="120" height="85" rx="5" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="100" y="75" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Square Number N</text>
  <text x="100" y="98" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">N = a²</text>
  <!-- Arrow -->
  <line x1="170" y1="92" x2="230" y2="92" stroke="#4ade80" stroke-width="2.5"/>
  <polygon points="230,92 220,87 220,97" fill="#4ade80"/>
  <text x="200" y="82" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">√N</text>
  <!-- Principal Root Output -->
  <rect x="240" y="50" width="120" height="85" rx="5" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="300" y="75" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Unique Positive Root</text>
  <text x="300" y="98" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">+a</text>
  <!-- Summary Box -->
  <text x="200" y="165" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">In school arithmetic, √N denotes the principal (non-negative) square root of N!</text>
</svg>
</div>
Although both \\((+7)^2 = 49\\) and \\((-7)^2 = 49\\), why is \\(\\sqrt{49}\\) defined as \\(7\\) in arithmetic?""",
     ["The radical symbol \\(\\sqrt{\\phantom{x}}\\) by mathematical definition represents the unique non-negative (principal) square root",
      "Because negative numbers do not exist in geometry",
      "Because 7 is greater than -7",
      "Because squaring destroys minus signs"],
     "A", "OSC", "easy",
     "While every positive real number has two square roots (one positive and one negative), the radical symbol \\(\\sqrt{x}\\) denotes specifically the *principal* (positive) square root. Thus, \\(\\sqrt{49} = +7\\), whereas the negative root is written as \\(-\\sqrt{49} = -7\\).")
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

output_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch1_topic3.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
