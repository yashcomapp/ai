# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-1-1.1
Topic: Properties of Square Numbers & Unit Digits
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-1-1.1"

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
    ("Which of the following digits can NEVER appear in the units place of a perfect square in base 10?",
     ["2, 3, 7, and 8", "0, 1, 4, and 9", "1, 5, and 6", "0, 4, 5, and 6"],
     "A", "OSC", "easy",
     "When squaring any integer from 0 to 9, the units digits obtained are \\(0^2=0\\), \\(1^2=1\\), \\(2^2=4\\), \\(3^2=9\\), \\(4^2=6\\), \\(5^2=5\\), \\(6^2=6\\), \\(7^2=9\\), \\(8^2=4\\), and \\(9^2=1\\). Thus, a perfect square can only end in 0, 1, 4, 5, 6, or 9. The digits 2, 3, 7, and 8 can never be the unit digit of any square number."),

    # 2
    ("What is the unit digit of the square of \\(2349\\)?",
     ["1", "9", "7", "3"],
     "A", "OSC", "easy",
     "The unit digit of \\(2349^2\\) depends solely on the square of its unit digit, which is 9. Since \\(9^2 = 81\\), the unit digit of \\(2349^2\\) is 1."),

    # 3
    ("Without calculating the actual value, determine which of the following numbers cannot be a perfect square: \\(1057\\), \\(23453\\), \\(7928\\), and \\(222222\\).",
     ["All of them, because their unit digits are 7, 3, 8, and 2 respectively",
      "Only 1057",
      "Only 7928",
      "None of them, all are perfect squares"],
     "A", "OSC", "easy",
     "No integer whose last digit is 2, 3, 7, or 8 can be a perfect square. The numbers end in 7, 3, 8, and 2, so none of them can be a perfect square."),

    # 4
    ("What is the units digit of the square of \\(15234\\)?",
     ["6", "4", "8", "2"],
     "A", "OSC", "easy",
     "The unit digit of \\(15234\\) is 4. Squaring 4 gives \\(4^2 = 16\\), whose unit digit is 6. Therefore, the square of any integer ending in 4 has 6 in its units place."),

    # 5
    ("If a natural number has unit digit 2 or 8, what is the unit digit of its square?",
     ["4", "6", "2", "8"],
     "A", "OSC", "easy",
     "For any number ending in 2, \\(2^2 = 4\\). For any number ending in 8, \\(8^2 = 64\\), which ends in 4. Hence, squares of numbers ending in 2 or 8 always end in 4."),

    # 6
    ("What can be said about the number of zeros at the end of a perfect square?",
     ["A perfect square must always end in an even number of zeros",
      "A perfect square must always end in an odd number of zeros",
      "A perfect square can end in any number of zeros",
      "A perfect square can never end in zero"],
     "A", "OSC", "easy",
     "If a number ends in \\(k\\) zeros, its square will end in \\(2k\\) zeros because \\((a \\times 10^k)^2 = a^2 \\times 10^{2k}\\). Since \\(2k\\) is always an even integer, a square number never ends in an odd number of zeros."),

    # 7
    ("Which of the following numbers cannot be a perfect square based on its trailing zeros?",
     ["\\(25000\\)", "\\(3600\\)", "\\(490000\\)", "\\(6400\\)"],
     "A", "OSC", "easy",
     "\\(25000\\) ends in 3 zeros (an odd count). A perfect square cannot end in an odd number of zeros. In contrast, 3600 has 2 zeros, 490000 has 4 zeros, and 6400 has 2 zeros, all of which are even counts."),

    # 8
    ("The square of an odd natural number is always:",
     ["An odd number", "An even number", "A prime number", "A negative number"],
     "A", "OSC", "easy",
     "Any odd integer can be written as \\(2k + 1\\). Its square is \\((2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1\\), which is in the form \\(2m + 1\\) and therefore always odd."),

    # 9
    ("The square of an even natural number is always:",
     ["An even number", "An odd number", "A prime number", "A fractional number"],
     "A", "OSC", "easy",
     "Any even integer can be written as \\(2k\\). Its square is \\((2k)^2 = 4k^2 = 2(2k^2)\\), which is a multiple of 2 (and 4), hence always even."),

    # 10
    ("Which of the following numbers will have an odd square?",
     ["\\(431\\)", "\\(2826\\)", "\\(7779\\)", "Both \\(431\\) and \\(7779\\)"],
     "D", "OSC", "easy",
     "The square of an odd number is odd, and the square of an even number is even. Both 431 and 7779 are odd numbers, so both of their squares are odd."),

    # 11
    ("What is the units digit of the square of \\(6587\\)?",
     ["9", "7", "3", "1"],
     "A", "OSC", "easy",
     "The unit digit of 6587 is 7. Since \\(7^2 = 49\\), the unit digit of \\(6587^2\\) is 9."),

    # 12
    ("What are the possible unit digits of a number whose square ends in 6?",
     ["4 or 6", "2 or 8", "3 or 7", "1 or 9"],
     "A", "OSC", "easy",
     "Checking unit digit squares: \\(4^2 = 16\\) (ends in 6) and \\(6^2 = 36\\) (ends in 6). No other single-digit squares end in 6. Thus, the original number must end in 4 or 6."),

    # 13
    ("What are the possible unit digits of a number whose square ends in 1?",
     ["1 or 9", "3 or 7", "4 or 6", "5 only"],
     "A", "OSC", "easy",
     "Since \\(1^2 = 1\\) and \\(9^2 = 81\\) (which ends in 1), any integer whose square ends in 1 must have 1 or 9 as its units digit."),

    # 14
    ("What are the possible unit digits of a number whose square ends in 4?",
     ["2 or 8", "1 or 9", "4 or 6", "0 only"],
     "A", "OSC", "easy",
     "Since \\(2^2 = 4\\) and \\(8^2 = 64\\) (ends in 4), the only digits whose squares yield a unit digit of 4 are 2 and 8."),

    # 15
    ("What are the possible unit digits of a number whose square ends in 9?",
     ["3 or 7", "1 or 9", "2 or 8", "4 or 6"],
     "A", "OSC", "easy",
     "Since \\(3^2 = 9\\) and \\(7^2 = 49\\) (ends in 9), any integer whose square ends in 9 must end in 3 or 7."),

    # 16
    ("If a natural number ends in 5, what must its square always end in?",
     ["25", "15", "35", "75"],
     "A", "OSC", "easy",
     "Any number ending in 5 can be written as \\(10a + 5\\). Its square is \\((10a + 5)^2 = 100a^2 + 100a + 25 = 100a(a + 1) + 25\\). This shows the last two digits are always 25."),

    # 17
    ("What is the value of \\(35^2\\) using the shortcut rule \\(a(a+1) \\times 100 + 25\\)?",
     ["\\(1225\\)", "\\(1125\\)", "\\(1250\\)", "\\(1525\\)"],
     "A", "OSC", "easy",
     "Here \\(a = 3\\). The rule gives \\(a(a + 1) = 3 \\times 4 = 12\\) followed by 25, giving \\(1225\\). Indeed, \\(35 \\times 35 = 1225\\)."),

    # 18
    ("What is the value of \\(75^2\\) using the property of numbers ending in 5?",
     ["\\(5625\\)", "\\(4925\\)", "\\(5425\\)", "\\(6425\\)"],
     "A", "OSC", "easy",
     "For 75, \\(a = 7\\). Computing \\(a(a + 1) = 7 \\times 8 = 56\\). Suffixing 25 yields \\(5625\\)."),

    # 19
    ("How many perfect squares lie strictly between 1 and 100?",
     ["8", "10", "9", "7"],
     "A", "OSC", "medium",
     "The perfect squares up to 100 are \\(1^2=1, 2^2=4, 3^2=9, 4^2=16, 5^2=25, 6^2=36, 7^2=49, 8^2=64, 9^2=81, 10^2=100\\). The question specifies *strictly between* 1 and 100, so excluding 1 and 100 leaves \\(4, 9, 16, 25, 36, 49, 64, 81\\), which is exactly 8 numbers."),

    # 20
    ("When any perfect square is divided by 3, what are the only possible remainders?",
     ["0 or 1", "0 or 2", "1 or 2", "0, 1, or 2"],
     "A", "OSC", "medium",
     "Any integer is of the form \\(3k\\), \\(3k+1\\), or \\(3k+2\\). Squaring each: \\((3k)^2 = 9k^2 = 3(3k^2) \\implies\\) remainder 0; \\((3k+1)^2 = 9k^2+6k+1 = 3(3k^2+2k)+1 \\implies\\) remainder 1; \\((3k+2)^2 = 9k^2+12k+4 = 3(3k^2+4k+1)+1 \\implies\\) remainder 1. A square can never leave remainder 2 when divided by 3."),

    # 21
    ("When any perfect square is divided by 4, what are the only possible remainders?",
     ["0 or 1", "0 or 2", "1 or 3", "2 or 3"],
     "A", "OSC", "medium",
     "Even numbers: \\((2k)^2 = 4k^2 \\implies\\) remainder 0 when divided by 4. Odd numbers: \\((2k+1)^2 = 4k^2+4k+1 = 4(k^2+k)+1 \\implies\\) remainder 1 when divided by 4. Thus, a perfect square divided by 4 always leaves remainder 0 or 1, never 2 or 3."),

    # 22
    ("Which of the following numbers cannot be a perfect square because it leaves a remainder of 2 when divided by 3?",
     ["\\(50\\)", "\\(49\\)", "\\(81\\)", "\\(100\\)"],
     "A", "OSC", "easy",
     "\\(50 = 3 \\times 16 + 2\\), which leaves a remainder of 2. Since no perfect square can leave a remainder of 2 when divided by 3, 50 cannot be a square. (49 leaves remainder 1, 81 leaves 0, 100 leaves 1)."),

    # 23
    ("What is the unit digit of \\((1234567)^2\\)?",
     ["9", "7", "4", "1"],
     "A", "OSC", "easy",
     "The unit digit of 1234567 is 7. Since \\(7^2 = 49\\), the unit digit of the square is 9."),

    # 24
    ("What is the unit digit of \\((999998)^2\\)?",
     ["4", "8", "6", "2"],
     "A", "OSC", "easy",
     "The unit digit is 8. Since \\(8^2 = 64\\), its unit digit is 4."),

    # 25
    ("What is the unit digit of \\((55555)^2\\)?",
     ["5", "0", "2", "6"],
     "A", "OSC", "easy",
     "The unit digit is 5. Since \\(5^2 = 25\\), the unit digit of the square is always 5."),

    # 26
    ("Which of the following numbers is a perfect square?",
     ["\\(441\\)", "\\(442\\)", "\\(443\\)", "\\(447\\)"],
     "A", "OSC", "easy",
     "Numbers ending in 2, 3, or 7 (442, 443, 447) cannot be squares. \\(441 = 21^2\\), which is a perfect square."),

    # 27
    ("Is \\(4000\\) a perfect square? Why or why not?",
     ["No, because it ends in an odd number of zeros (three zeros)",
      "Yes, because 4 is a perfect square",
      "Yes, because \\(4000 = 200^2\\)",
      "No, because its first digit is 4"],
     "A", "OSC", "easy",
     "4000 has 3 zeros at the end. Any square number must have an even number of trailing zeros. Since 3 is odd, 4000 cannot be a perfect square (\\(60^2=3600, 70^2=4900\\))."),

    # 28
    ("How many trailing zeros will the square of \\(7000\\) have?",
     ["6", "3", "4", "5"],
     "A", "OSC", "easy",
     "7000 has 3 trailing zeros. Squaring it doubles the number of zeros: \\(3 \\times 2 = 6\\) zeros. Indeed, \\(7000^2 = 49,000,000\\)."),

    # 29
    ("What is the units digit of \\(105^2 + 106^2\\)?",
     ["1", "5", "6", "0"],
     "A", "OSC", "medium",
     "The unit digit of \\(105^2\\) is 5 (since \\(5^2=25\\)). The unit digit of \\(106^2\\) is 6 (since \\(6^2=36\\)). Adding their unit digits: \\(5 + 6 = 11\\), so the units digit of the sum is 1."),

    # 30
    ("What is the units digit of \\(99^2 - 88^2\\)?",
     ["7", "1", "4", "5"],
     "A", "OSC", "medium",
     "The unit digit of \\(99^2\\) is 1 (since \\(9^2=81\\)). The unit digit of \\(88^2\\) is 4 (since \\(8^2=64\\)). Subtracting units digits with regrouping: \\(11 - 4 = 7\\). Thus, the units digit is 7."),

    # 31
    ("Which of the following statements is FALSE?",
     ["A number ending in an even number of zeros is always a perfect square",
      "A perfect square never ends in 2, 3, 7, or 8",
      "The square of an even number is always even",
      "The square of an odd number is always odd"],
     "A", "OSC", "easy",
     "Having an even number of zeros is a *necessary* condition for trailing zeros, but not *sufficient*. For example, 200, 300, 500, and 700 end in an even number of zeros (two zeros), but none of them are perfect squares."),

    # 32
    ("A number \\(N\\) leaves a remainder of 3 when divided by 4. Can \\(N\\) be a perfect square?",
     ["No, because every perfect square leaves a remainder of either 0 or 1 when divided by 4",
      "Yes, if \\(N\\) is odd",
      "Yes, if \\(N\\) is large enough",
      "It cannot be determined without knowing \\(N\\)"],
     "A", "OSC", "medium",
     "Every integer squared is either \\((2k)^2 = 4k^2 \\equiv 0 \\pmod 4\\) or \\((2k+1)^2 = 4(k^2+k)+1 \\equiv 1 \\pmod 4\\). No square can ever be of the form \\(4m + 3\\)."),

    # 33
    ("If \\(n\\) is a single-digit natural number, for how many values of \\(n\\) does \\(n^2\\) end in 4?",
     ["Two values (2 and 8)", "One value (2 only)", "Four values", "Zero values"],
     "A", "OSC", "easy",
     "Checking single digits: \\(2^2 = 4\\) and \\(8^2 = 64\\) (ends in 4). No other single-digit squared ends in 4. Thus, exactly 2 values (2 and 8)."),

    # 34
    ("What is the unit digit of the sum \\(1^2 + 2^2 + 3^2 + 4^2 + 5^2\\)?",
     ["5", "0", "4", "9"],
     "A", "OSC", "medium",
     "Calculating the squares: \\(1 + 4 + 9 + 16 + 25 = 55\\). The units digit is 5."),

    # 35
    ("What is the tens digit of the square of any integer ending in 5?",
     ["2", "5", "0", "7"],
     "A", "OSC", "easy",
     "Every number ending in 5 is \\(10a + 5\\). Its square is \\(100a(a + 1) + 25\\). Since the first term \\(100a(a+1)\\) is a multiple of 100, the last two digits are solely determined by 25. Thus, the tens digit is always 2."),

    # 36
    ("Which of the following numbers cannot be a square because its tens digit is not 2 despite ending in 5?",
     ["\\(375\\)", "\\(625\\)", "\\(1225\\)", "\\(2025\\)"],
     "A", "OSC", "medium",
     "A perfect square ending in 5 must end in 25. The number 375 ends in 75 (tens digit is 7, not 2), so it cannot be a perfect square. (625, 1225, 2025 all end in 25)."),

    # 37
    ("What is the units digit of \\(73^2 \\times 84^2\\)?",
     ["4", "6", "9", "2"],
     "A", "OSC", "medium",
     "The unit digit of \\(73^2\\) is \\(3^2 = 9\\). The unit digit of \\(84^2\\) is \\(4^2 = 16 \\implies 6\\). Multiplying their unit digits gives \\(9 \\times 6 = 54\\), so the units digit of the product is 4."),

    # 38
    ("If the square of a number ends in 0000, what is the minimum number of zeros the original number must have?",
     ["2", "1", "4", "3"],
     "A", "OSC", "easy",
     "Since the square doubles the number of trailing zeros, if the square ends in 4 zeros, the original number must end in at least \\(4 / 2 = 2\\) zeros."),

    # 39
    ("Which of the following square numbers ends in 1?",
     ["\\(81\\)", "\\(64\\)", "\\(36\\)", "\\(25\\)"],
     "A", "OSC", "easy",
     "\\(81 = 9^2\\), which ends in 1. (64 ends in 4, 36 ends in 6, 25 ends in 5)."),

    # 40
    ("What is the units digit of \\((111111)^2\\)?",
     ["1", "2", "6", "9"],
     "A", "OSC", "easy",
     "The units digit of 111111 is 1. Since \\(1^2 = 1\\), the units digit of its square is 1.")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    ("Find the units digit of the square of \\(52698\\).",
     ["4", "8", "6", "2"],
     "A", "OSC", "easy",
     "The unit digit of 52698 is 8. Squaring 8 gives \\(8^2 = 64\\), so the unit digit of the square is 4."),

    # 42
    ("Find the units digit of the square of \\(99880\\).",
     ["0", "1", "4", "5"],
     "A", "OSC", "easy",
     "The unit digit of 99880 is 0. Since \\(0^2 = 0\\), the unit digit of its square is 0 (specifically, it will end in at least two zeros)."),

    # 43
    ("Which of the following numbers can be a perfect square: 1052, 1053, 1057, or 1089?",
     ["1089", "1052", "1053", "1057"],
     "A", "OSC", "easy",
     "Numbers ending in 2, 3, or 7 can never be perfect squares. 1089 ends in 9, which is a permissible ending digit. In fact, \\(33^2 = 1089\\)."),

    # 44
    ("What is the units digit of \\(1234^2 + 5678^2\\)?",
     ["0", "6", "4", "2"],
     "A", "OSC", "medium",
     "Unit digit of \\(1234^2\\) is \\(4^2 = 16 \\implies 6\\). Unit digit of \\(5678^2\\) is \\(8^2 = 64 \\implies 4\\). Adding them: \\(6 + 4 = 10\\), which ends in 0."),

    # 45
    ("Evaluate \\(45^2\\) using the formula \\(a(a+1) \\times 100 + 25\\).",
     ["\\(2025\\)", "\\(2525\\)", "\\(1825\\)", "\\(2050\\)"],
     "A", "OSC", "easy",
     "For 45, \\(a = 4\\). Compute \\(4 \\times (4 + 1) = 4 \\times 5 = 20\\). Appending 25 gives \\(2025\\)."),

    # 46
    ("Evaluate \\(95^2\\) using the formula for numbers ending in 5.",
     ["\\(9025\\)", "\\(8125\\)", "\\(9525\\)", "\\(8925\\)"],
     "A", "OSC", "easy",
     "Here \\(a = 9\\). Compute \\(9 \\times (9 + 1) = 9 \\times 10 = 90\\). Appending 25 gives \\(9025\\)."),

    # 47
    ("Evaluate \\(115^2\\) using the formula for numbers ending in 5.",
     ["\\(13225\\)", "\\(12125\\)", "\\(13525\\)", "\\(14225\\)"],
     "A", "OSC", "medium",
     "Here \\(a = 11\\). Compute \\(11 \\times (11 + 1) = 11 \\times 12 = 132\\). Appending 25 yields \\(13225\\)."),

    # 48
    ("How many natural numbers between 1 and 50 are perfect squares?",
     ["7", "6", "8", "5"],
     "A", "OSC", "easy",
     "The perfect squares up to 50 are \\(1^2=1, 2^2=4, 3^2=9, 4^2=16, 5^2=25, 6^2=36, 7^2=49\\). The next square is \\(8^2=64 > 50\\). Thus, there are 7 perfect squares."),

    # 49
    ("Which of the following numbers cannot be written as the square of an integer?",
     ["\\(1234567\\)", "\\(144\\)", "\\(256\\)", "\\(400\\)"],
     "A", "OSC", "easy",
     "The number 1234567 ends in 7. No integer square ends in 7. (144 = 12², 256 = 16², 400 = 20²)."),

    # 50
    ("What is the unit digit of \\((82)^2 + (83)^2 + (87)^2\\)?",
     ["2", "4", "9", "6"],
     "A", "OSC", "medium",
     "Unit digit of \\(82^2\\) is \\(2^2 = 4\\). Unit digit of \\(83^2\\) is \\(3^2 = 9\\). Unit digit of \\(87^2\\) is \\(7^2 = 49 \\implies 9\\). Sum of unit digits: \\(4 + 9 + 9 = 22\\), which ends in 2."),

    # 51
    ("If a square number is divided by 8, what are the possible remainders for odd squares?",
     ["1 only", "0 or 1", "1, 3, or 5", "0, 1, or 4"],
     "A", "OSC", "hard",
     "Any odd integer is \\(2k + 1\\). Its square is \\((2k+1)^2 = 4k^2 + 4k + 1 = 4k(k+1) + 1\\). Since either \\(k\\) or \\(k+1\\) is always even, \\(k(k+1)\\) is an even number \\(2m\\). Thus \\(4k(k+1) = 4(2m) = 8m\\). Therefore, \\((2k+1)^2 = 8m + 1\\), which always leaves a remainder of 1 when divided by 8."),

    # 52
    ("Check whether \\(105\\) can be a perfect square using division by 3.",
     ["\\(105 = 3 \\times 35 + 0\\), so division by 3 does not rule it out, but its tens digit is 0 instead of 2 (it ends in 05, not 25), so it is not a square",
      "Yes, 105 is a perfect square",
      "No, because 105 divided by 3 leaves remainder 2",
      "No, because 105 ends in 5"],
     "A", "OSC", "medium",
     "105 is divisible by 3 (remainder 0), so the mod 3 test does not eliminate it. However, a square ending in 5 must end in 25. Since 105 ends in 05, it cannot be a square (\\(10^2=100, 11^2=121\\))."),

    # 53
    ("What is the units digit of \\((31)^2 \\times (46)^2\\)?",
     ["6", "1", "7", "4"],
     "A", "OSC", "easy",
     "Unit digit of \\(31^2\\) is 1. Unit digit of \\(46^2\\) is \\(6^2 = 36 \\implies 6\\). The product has unit digit \\(1 \\times 6 = 6\\)."),

    # 54
    ("What is the units digit of \\((17)^2 - (13)^2\\)?",
     ["0", "9", "6", "4"],
     "A", "OSC", "medium",
     "Both \\(17^2\\) and \\(13^2\\) end in 9 (since \\(7^2=49\\) and \\(3^2=9\\)). Their difference \\(9 - 9 = 0\\), so the units digit is 0. (Indeed, \\(289 - 169 = 120\\))."),

    # 55
    ("What is the remainder when \\(17^2\\) is divided by 4?",
     ["1", "0", "2", "3"],
     "A", "OSC", "easy",
     "Since 17 is an odd number, its square must leave a remainder of 1 when divided by 4. Indeed, \\(17^2 = 289 = 4 \\times 72 + 1\\)."),

    # 56
    ("What is the remainder when \\(24^2\\) is divided by 4?",
     ["0", "1", "2", "3"],
     "A", "OSC", "easy",
     "Since 24 is an even number, its square is divisible by 4 (remainder 0). Indeed, \\(24^2 = 576 = 4 \\times 144 + 0\\)."),

    # 57
    ("The product of two consecutive odd numbers \\((2n - 1)(2n + 1)\\) is equal to:",
     ["\\((2n)^2 - 1\\) (one less than a perfect square)",
      "A perfect square",
      "\\((2n)^2 + 1\\)",
      "\\(4n^2 + 1\\)"],
     "A", "OSC", "medium",
     "Using the identity \\((a - b)(a + b) = a^2 - b^2\\), \\((2n - 1)(2n + 1) = (2n)^2 - 1^2 = 4n^2 - 1\\). Thus, the product of two consecutive odd numbers is always one less than the square of the even number between them."),

    # 58
    ("For example, \\(11 \\times 13 = 143\\). Which square is 143 one less than?",
     ["\\(12^2 = 144\\)", "\\(10^2 = 100\\)", "\\(14^2 = 196\\)", "\\(13^2 = 169\\)"],
     "A", "OSC", "easy",
     "\\(11 \\times 13 = (12 - 1)(12 + 1) = 12^2 - 1 = 144 - 1 = 143\\)."),

    # 59
    ("Similarly, \\(19 \\times 21\\) can be quickly computed as:",
     ["\\(20^2 - 1 = 400 - 1 = 399\\)",
      "\\(19^2 + 1 = 362\\)",
      "\\(21^2 - 1 = 440\\)",
      "\\(20^2 + 1 = 401\\)"],
     "A", "OSC", "easy",
     "\\(19 \\times 21 = (20 - 1)(20 + 1) = 20^2 - 1 = 400 - 1 = 399\\)."),

    # 60
    ("What is the product of two consecutive even numbers \\(2n(2n + 2)\\)?",
     ["\\((2n + 1)^2 - 1\\) (one less than the square of the odd number between them)",
      "A perfect square",
      "\\((2n)^2 + 2\\)",
      "\\(4n^2 + 4\\)"],
     "A", "OSC", "medium",
     "Let the odd number between them be \\(x = 2n + 1\\). Then the numbers are \\(x - 1\\) and \\(x + 1\\). Their product is \\((x - 1)(x + 1) = x^2 - 1 = (2n + 1)^2 - 1\\)."),

    # 61
    ("Compute \\(29 \\times 31\\) without standard long multiplication.",
     ["\\(30^2 - 1 = 900 - 1 = 899\\)",
      "\\(30^2 + 1 = 901\\)",
      "\\(29^2 + 1 = 842\\)",
      "\\(31^2 - 1 = 960\\)"],
     "A", "OSC", "easy",
     "\\(29 \\times 31 = (30 - 1)(30 + 1) = 30^2 - 1 = 900 - 1 = 899\\)."),

    # 62
    ("Compute \\(44 \\times 46\\) using the difference of squares property.",
     ["\\(45^2 - 1 = 2025 - 1 = 2024\\)",
      "\\(45^2 + 1 = 2026\\)",
      "\\(40^2 + 24 = 1624\\)",
      "\\(46^2 - 44 = 2072\\)"],
     "A", "OSC", "medium",
     "\\(44 \\times 46 = (45 - 1)(45 + 1) = 45^2 - 1 = 2025 - 1 = 2024\\)."),

    # 63
    ("How many natural numbers are there from 1 to 1000 whose squares end in 5?",
     ["100 numbers (every number ending in 5)",
      "10 numbers",
      "50 numbers",
      "200 numbers"],
     "A", "OSC", "medium",
     "A number's square ends in 5 if and only if the number itself ends in 5. In each set of 10 consecutive integers, exactly one ends in 5. From 1 to 1000, there are \\(1000 / 10 = 100\\) numbers ending in 5."),

    # 64
    ("What is the units digit of \\(1^2 + 2^2 + 3^2 + \\dots + 9^2\\)?",
     ["5", "0", "4", "6"],
     "A", "OSC", "medium",
     "Summing the units digits: \\(1 + 4 + 9 + 6 + 5 + 6 + 9 + 4 + 1 = 45\\). The units digit is 5."),

    # 65
    ("What is the units digit of \\(1^2 + 2^2 + 3^2 + \\dots + 10^2\\)?",
     ["5", "0", "1", "9"],
     "A", "OSC", "medium",
     "Since \\(10^2 = 100\\) contributes 0 to the units digit, the sum of units digits from 1 to 10 is \\(45 + 0 = 45\\), which ends in 5."),

    # 66
    ("Which of the following numbers is the square of an even number?",
     ["\\(576\\)", "\\(169\\)", "\\(625\\)", "\\(289\\)"],
     "A", "OSC", "easy",
     "The square of an even number must be even. Among the options, 576 is the only even number (\\(24^2 = 576\\)). 169 (13²), 625 (25²), and 289 (17²) are all squares of odd numbers."),

    # 67
    ("If \\(k\\) is an integer, what can be the unit digit of \\(k^2 + 2\\)?",
     ["2, 3, 6, 7, 8, or 1",
      "0, 1, 4, 5, 6, or 9",
      "4 only",
      "None of these"],
     "A", "OSC", "hard",
     "The unit digits of \\(k^2\\) are 0, 1, 4, 5, 6, 9. Adding 2 to each yields: \\(0+2=2\\), \\(1+2=3\\), \\(4+2=6\\), \\(5+2=7\\), \\(6+2=8\\), and \\(9+2=11 \\implies 1\\). Thus, the unit digit of \\(k^2 + 2\\) can be 2, 3, 6, 7, 8, or 1."),

    # 68
    ("Can \\(k^2 + 2\\) ever end in 0?",
     ["No, because \\(k^2\\) never ends in 8 (since \\(8 + 2 = 10\\))",
      "Yes, when \\(k = 8\\)",
      "Yes, when \\(k = 0\\)",
      "Yes, when \\(k\\) is odd"],
     "A", "OSC", "medium",
     "For \\(k^2 + 2\\) to end in 0, \\(k^2\\) must end in 8 (because \\(8 + 2 = 10\\)). But no square number can ever end in 8. Therefore, \\(k^2 + 2\\) can never end in 0."),

    # 69
    ("Can \\(k^2 + 3\\) ever end in 5?",
     ["No, because \\(k^2\\) never ends in 2",
      "Yes, when \\(k = 5\\)",
      "Yes, when \\(k = 2\\)",
      "Yes, for all even numbers"],
     "A", "OSC", "medium",
     "For \\(k^2 + 3\\) to end in 5, \\(k^2\\) must end in 2. But 2 is never a unit digit of any perfect square. Hence, \\(k^2 + 3\\) can never end in 5."),

    # 70
    ("What is the units digit of \\((12345)^2 + (67890)^2\\)?",
     ["5", "0", "2", "6"],
     "A", "OSC", "easy",
     "The unit digit of \\(12345^2\\) is 5. The unit digit of \\(67890^2\\) is 0. Adding their unit digits: \\(5 + 0 = 5\\).")
]

# 12 MOCK / FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71: Visual Proof of Square Array (3x3 vs 4x4)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- 3x3 Square Array (Left) -->
  <rect x="30" y="30" width="130" height="130" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="95" y="50" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">3 x 3 = 9 Dots</text>
  <!-- 9 Dots Grid -->
  <circle cx="65" cy="80" r="6" fill="#38bdf8"/>
  <circle cx="95" cy="80" r="6" fill="#38bdf8"/>
  <circle cx="125" cy="80" r="6" fill="#38bdf8"/>
  <circle cx="65" cy="110" r="6" fill="#38bdf8"/>
  <circle cx="95" cy="110" r="6" fill="#38bdf8"/>
  <circle cx="125" cy="110" r="6" fill="#38bdf8"/>
  <circle cx="65" cy="140" r="6" fill="#38bdf8"/>
  <circle cx="95" cy="140" r="6" fill="#38bdf8"/>
  <circle cx="125" cy="140" r="6" fill="#38bdf8"/>
  <!-- 4x4 Square Array (Right) -->
  <rect x="210" y="30" width="160" height="130" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="1.5"/>
  <text x="290" y="50" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">4 x 4 = 16 Dots</text>
  <!-- 16 Dots Grid -->
  <circle cx="245" cy="75" r="5" fill="#4ade80"/>
  <circle cx="275" cy="75" r="5" fill="#4ade80"/>
  <circle cx="305" cy="75" r="5" fill="#4ade80"/>
  <circle cx="335" cy="75" r="5" fill="#4ade80"/>
  <circle cx="245" cy="100" r="5" fill="#4ade80"/>
  <circle cx="275" cy="100" r="5" fill="#4ade80"/>
  <circle cx="305" cy="100" r="5" fill="#4ade80"/>
  <circle cx="335" cy="100" r="5" fill="#4ade80"/>
  <circle cx="245" cy="125" r="5" fill="#4ade80"/>
  <circle cx="275" cy="125" r="5" fill="#4ade80"/>
  <circle cx="305" cy="125" r="5" fill="#4ade80"/>
  <circle cx="335" cy="125" r="5" fill="#4ade80"/>
  <circle cx="245" cy="148" r="5" fill="#4ade80"/>
  <circle cx="275" cy="148" r="5" fill="#4ade80"/>
  <circle cx="305" cy="148" r="5" fill="#4ade80"/>
  <circle cx="335" cy="148" r="5" fill="#4ade80"/>
  <!-- Footer Note -->
  <text x="200" y="185" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">A number is a perfect square if its items can form a symmetric equal row-column square grid!</text>
</svg>
</div>
Why is 16 considered a 'square number' geometrically while 12 is not?""",
     ["16 identical dots can be arranged into a perfect square grid of 4 equal rows and 4 equal columns (\\(4 \\times 4\\)), whereas 12 cannot form an integer square",
      "Because 16 is divisible by 2",
      "Because 16 is greater than 10",
      "Because 12 is an odd number"],
     "A", "OSC", "easy",
     "Geometrically, square numbers represent quantities that can be arranged in a symmetric planar grid of \\(n\\) rows by \\(n\\) columns. Since \\(4 \\times 4 = 16\\), it forms a complete square. 12 cannot be factored into two equal integers (\\(\\sqrt{12} \\approx 3.464\\)), so it cannot form a square grid."),

    # 72: Unit Digits Table & Complementary Pairs
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Unit Digit Symmetry: Complementary Pairs (Sum = 10)</text>
  <!-- Table Header -->
  <rect x="30" y="38" width="340" height="25" fill="#1e293b" rx="3"/>
  <text x="120" y="55" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Ending Digits of Number (n)</text>
  <text x="280" y="55" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Ending Digit of Square (n²)</text>
  <!-- Rows -->
  <text x="120" y="80" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">1 or 9 (1+9=10)</text>
  <text x="280" y="80" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">1</text>
  <text x="120" y="105" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">2 or 8 (2+8=10)</text>
  <text x="280" y="105" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">4</text>
  <text x="120" y="130" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">3 or 7 (3+7=10)</text>
  <text x="280" y="130" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">9</text>
  <text x="120" y="155" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">4 or 6 (4+6=10)</text>
  <text x="280" y="155" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">6</text>
  <text x="120" y="180" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">5</text>
  <text x="280" y="180" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">5 (ends in 25)</text>
  <!-- Disallowed List on Bottom Right -->
  <rect x="230" y="165" width="140" height="25" fill="#450a0a" rx="3"/>
  <text x="300" y="181" fill="#ef4444" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">NEVER: 2, 3, 7, 8</text>
</svg>
</div>
Why do pairs of numbers that add up to 10 (such as 3 and 7, or 2 and 8) always produce the exact same unit digit when squared?""",
     ["Because \\((10 - d)^2 = 100 - 20d + d^2\\); modulo 10, the terms \\(100\\) and \\(-20d\\) vanish, leaving the exact same remainder \\(d^2 \\pmod{10}\\)",
      "Because numbers that add to 10 are twins",
      "Because 10 is an even number",
      "Because square roots reverse the addition"],
     "A", "OSC", "medium",
     "Expanding \\((10 - d)^2 = 100 - 20d + d^2\\). Since both 100 and \\(20d\\) are multiples of 10, their contribution to the units digit is 0. Therefore, the unit digit of \\((10 - d)^2\\) is identical to the unit digit of \\(d^2\\). For example, \\(3^2 = 9\\) and \\((10 - 3)^2 = 7^2 = 49 \\implies 9\\)."),

    # 73: Even vs Odd Trailing Zeros Rule
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Allowed: Even Zeros (Left) -->
  <rect x="25" y="25" width="165" height="140" rx="6" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="107" y="50" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">PERMISSIBLE: EVEN ZEROS</text>
  <text x="107" y="75" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle">10² = 100 (2 zeros)</text>
  <text x="107" y="100" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle">20² = 400 (2 zeros)</text>
  <text x="107" y="125" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle">100² = 10000 (4 zeros)</text>
  <text x="107" y="150" fill="#86efac" font-size="7" font-family="sans-serif" text-anchor="middle">Rule: k zeros squared = 2k zeros</text>
  <!-- Disallowed: Odd Zeros (Right) -->
  <rect x="210" y="25" width="165" height="140" rx="6" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
  <text x="292" y="50" fill="#f87171" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">IMPOSSIBLE: ODD ZEROS</text>
  <text x="292" y="75" fill="#fca5a5" font-size="10" font-family="sans-serif" text-anchor="middle">5000 (3 zeros) -> NOT square</text>
  <text x="292" y="100" fill="#fca5a5" font-size="10" font-family="sans-serif" text-anchor="middle">80 (1 zero) -> NOT square</text>
  <text x="292" y="125" fill="#fca5a5" font-size="10" font-family="sans-serif" text-anchor="middle">64000 (3 zeros) -> NOT square</text>
  <text x="292" y="150" fill="#fca5a5" font-size="7" font-family="sans-serif" text-anchor="middle">Cannot be split into two equal integers!</text>
  <!-- Summary Box -->
  <text x="200" y="180" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">A number ending in an odd count of zeros can NEVER be a perfect square!</text>
</svg>
</div>
Based on the algebraic doubling of trailing zeros shown above, why can \\(64000\\) never be a perfect square even though 64 is a perfect square?""",
     ["64000 has 3 zeros; because squaring doubles any zero count, a square number must have an even number of trailing zeros",
      "Because 64000 is an odd number",
      "Because 64 is not divisible by 8",
      "Because 64000 is greater than 10000"],
     "A", "OSC", "easy",
     "Any number ending in zeros can be written as \\(a \\times 10^k\\). Its square is \\(a^2 \\times 10^{2k}\\). Since the exponent of 10 is \\(2k\\), the number of zeros in any perfect square is always an even integer (2, 4, 6, ...). 64000 ends in 3 zeros (odd), so it cannot be a square."),

    # 74: Geometric Proof for Numbers Ending in 5: a(a+1)*100 + 25
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Formula Banner -->
  <rect x="25" y="20" width="350" height="35" rx="4" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="200" y="42" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">(10a + 5)² = 100a(a + 1) + 25</text>
  <!-- Visual Geometric Split: 35 x 35 (a = 3) -->
  <rect x="60" y="70" width="90" height="90" fill="#3b0764" stroke="#c084fc" stroke-width="1.5"/>
  <text x="105" y="120" fill="#c084fc" font-size="8" font-family="sans-serif" text-anchor="middle">30 x 30 = 900</text>
  <!-- Two side rectangles: 30x5 and 5x30 -->
  <rect x="150" y="70" width="25" height="90" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="162" y="120" fill="#4ade80" font-size="7" font-family="sans-serif" text-anchor="middle">150</text>
  <rect x="60" y="160" width="90" height="25" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="105" y="176" fill="#4ade80" font-size="7" font-family="sans-serif" text-anchor="middle">150</text>
  <!-- Corner 5x5 Square -->
  <rect x="150" y="160" width="25" height="25" fill="#78350f" stroke="#facc15" stroke-width="1.5"/>
  <text x="162" y="176" fill="#facc15" font-size="7" font-family="sans-serif" text-anchor="middle">25</text>
  <!-- Summation Result on Right -->
  <rect x="200" y="80" width="170" height="90" rx="5" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="285" y="105" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Calculation for 35²:</text>
  <text x="285" y="125" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle">a = 3  ->  3 x 4 = 12</text>
  <text x="285" y="145" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Result: 1225</text>
  <text x="285" y="162" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Tens digit is always 2!</text>
</svg>
</div>
Using the algebraic identity \\((10a + 5)^2 = 100a(a+1) + 25\\), what must be the last two digits of the square of ANY integer ending in 5?""",
     ["Always 25, with tens digit 2 and units digit 5",
      "Always 15",
      "Always 75",
      "It varies depending on whether \\(a\\) is even or odd"],
     "A", "OSC", "easy",
     "Expanding \\((10a + 5)^2 = 100a^2 + 100a + 25 = 100a(a + 1) + 25\\). Because \\(100a(a + 1)\\) is an exact multiple of 100, its tens and units digits are both 00. Adding 25 guarantees that the last two digits of any integer ending in 5 are always 25."),

    # 75: Modulo 3 Remainder Test
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Modulo 3 Arithmetic: Why n² mod 3 is NEVER 2</text>
  <!-- Case 1: n = 3k -->
  <rect x="25" y="40" width="110" height="105" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="80" y="60" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Case 1: n = 3k</text>
  <text x="80" y="80" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">n² = 9k²</text>
  <text x="80" y="100" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">= 3(3k²)</text>
  <text x="80" y="130" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Rem = 0</text>
  <!-- Case 2: n = 3k + 1 -->
  <rect x="145" y="40" width="110" height="105" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="200" y="60" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Case 2: n = 3k + 1</text>
  <text x="200" y="80" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">n² = 9k² + 6k + 1</text>
  <text x="200" y="100" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">= 3(...) + 1</text>
  <text x="200" y="130" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Rem = 1</text>
  <!-- Case 3: n = 3k + 2 -->
  <rect x="265" y="40" width="110" height="105" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="320" y="60" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Case 3: n = 3k + 2</text>
  <text x="320" y="80" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">n² = 9k² + 12k + 4</text>
  <text x="320" y="100" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">= 3(...) + 1</text>
  <text x="320" y="130" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Rem = 1</text>
  <!-- Conclusion Banner -->
  <text x="200" y="170" fill="#ef4444" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">IMPOSSIBILITY THEOREM: A square number divided by 3 NEVER leaves a remainder of 2!</text>
</svg>
</div>
A student tests whether \\(2003\\) is a perfect square. Using division by 3, what is the conclusion?""",
     ["\\(2003 = 3 \\times 667 + 2\\) (remainder 2); since no square leaves remainder 2 on division by 3, \\(2003\\) is definitely NOT a square",
      "\\(2003\\) is a perfect square because 3 is odd",
      "Division by 3 proves \\(2003\\) is a square",
      "The remainder is 1, so \\(2003\\) is a square"],
     "A", "OSC", "medium",
     "Sum of digits of 2003 is \\(2 + 0 + 0 + 3 = 5\\). \\(5 = 3 \\times 1 + 2\\), which leaves remainder 2 when divided by 3. Because every integer square \\(n^2 \\equiv 0 \\text{ or } 1 \\pmod 3\\), no number leaving remainder 2 can ever be a perfect square."),

    # 76: Modulo 4 Remainder Test
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Modulo 4 Partition: Even vs Odd Squares</text>
  <!-- Even Branch (Left) -->
  <rect x="30" y="40" width="160" height="110" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="110" y="65" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">EVEN NUMBERS: (2k)</text>
  <text x="110" y="90" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">(2k)² = 4k²</text>
  <text x="110" y="115" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Multiple of 4</text>
  <text x="110" y="138" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Remainder mod 4 = 0</text>
  <!-- Odd Branch (Right) -->
  <rect x="210" y="40" width="160" height="110" rx="5" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="290" y="65" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">ODD NUMBERS: (2k + 1)</text>
  <text x="290" y="90" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">(2k + 1)² = 4k² + 4k + 1</text>
  <text x="290" y="115" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">= 4(k² + k) + 1</text>
  <text x="290" y="138" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Remainder mod 4 = 1</text>
  <!-- Bottom Warning -->
  <text x="200" y="173" fill="#ef4444" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Remainders 2 and 3 are STRICTLY IMPOSSIBLE for any integer square!</text>
</svg>
</div>
Which of the following numbers can be immediately ruled out as a perfect square because its remainder modulo 4 is 3?""",
     ["\\(79\\) (since \\(79 = 4 \\times 19 + 3\\))",
      "\\(64\\) (since \\(64 = 4 \\times 16 + 0\\))",
      "\\(81\\) (since \\(81 = 4 \\times 20 + 1\\))",
      "\\(100\\) (since \\(100 = 4 \\times 25 + 0\\))"],
     "A", "OSC", "easy",
     "Dividing 79 by 4 gives \\(79 = 4 \\times 19 + 3\\) (remainder 3). As proven above, all integer squares are of the form \\(4m\\) or \\(4m + 1\\). Any number of the form \\(4m + 2\\) or \\(4m + 3\\) is never a square."),

    # 77: Parity Conservation in Squaring
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Conservation of Parity Under Squaring</text>
  <!-- Even Squared Box -->
  <rect x="30" y="45" width="160" height="90" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="110" y="70" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">EVEN NUMBER (2k)</text>
  <text x="110" y="95" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle">(2k)² = 4k²</text>
  <text x="110" y="120" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">ALWAYS EVEN</text>
  <!-- Odd Squared Box -->
  <rect x="210" y="45" width="160" height="90" rx="6" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="290" y="70" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">ODD NUMBER (2k + 1)</text>
  <text x="290" y="95" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle">(2k + 1)² = 2(...) + 1</text>
  <text x="290" y="120" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">ALWAYS ODD</text>
  <!-- Summary Rule -->
  <text x="200" y="165" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Even² = Even  |  Odd² = Odd  (Parity is always strictly preserved)</text>
</svg>
</div>
Without computing, which of the following expressions must evaluate to an ODD number?""",
     ["\\((143)^2 + (256)^2\\)",
      "\\((143)^2 + (345)^2\\)",
      "\\((256)^2 + (458)^2\\)",
      "\\((100)^2 + (200)^2\\)"],
     "A", "OSC", "medium",
     "\\(143\\) is odd, so \\(143^2\\) is odd. \\(256\\) is even, so \\(256^2\\) is even. The sum of an odd number and an even number is always odd (\\(\\text{Odd} + \\text{Even} = \\text{Odd}\\)). In contrast, Option B is \\(\\text{Odd} + \\text{Odd} = \\text{Even}\\), and Options C & D are \\(\\text{Even} + \\text{Even} = \\text{Even}\\)."),

    # 78: Consecutive Squares and Difference Identity (n+1)^2 - n^2 = 2n + 1
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Difference Between Consecutive Squares: (n + 1)² - n² = 2n + 1</text>
  <!-- Geometric Diagram: n x n square in center -->
  <rect x="70" y="45" width="80" height="80" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="110" y="90" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle">n²</text>
  <!-- Added Strip of width 1 on top and right -->
  <rect x="150" y="45" width="20" height="80" fill="#14532d" stroke="#4ade80" stroke-width="1"/>
  <text x="160" y="90" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">n</text>
  <rect x="70" y="125" width="80" height="20" fill="#14532d" stroke="#4ade80" stroke-width="1"/>
  <text x="110" y="138" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">n</text>
  <rect x="150" y="125" width="20" height="20" fill="#78350f" stroke="#facc15" stroke-width="1"/>
  <text x="160" y="138" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">1</text>
  <!-- Formula Details on Right -->
  <rect x="200" y="45" width="170" height="100" rx="5" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="285" y="70" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">L-shaped Border Added:</text>
  <text x="285" y="90" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Border = n + n + 1 = 2n + 1</text>
  <text x="285" y="110" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Sum of the two bases!</text>
  <text x="285" y="130" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">(n+1)² - n² = (n+1) + n</text>
  <!-- Summary Footer -->
  <text x="200" y="172" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Example: 25² - 24² = 25 + 24 = 49 (Instant mental arithmetic!)</text>
</svg>
</div>
Using the geometric difference \\((n + 1)^2 - n^2 = (n + 1) + n\\), what is the value of \\(101^2 - 100^2\\)?""",
     ["\\(201\\) (calculated directly as \\(101 + 100\\))",
      "\\(101\\)",
      "\\(200\\)",
      "\\(1\\)"],
     "A", "OSC", "easy",
     "Using \\(a^2 - b^2 = (a - b)(a + b)\\), with \\(a = 101\\) and \\(b = 100\\): since \\(a - b = 1\\), the difference is simply \\(a + b = 101 + 100 = 201\\)."),

    # 79: Units Digit Multiplication Table for Square Roots
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Deducing Possible Units Digits of the Square Root</text>
  <!-- Diagram Layout: Square Units Digit -> Square Root Units Digits -->
  <rect x="30" y="40" width="100" height="110" rx="5" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="80" y="60" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Unit Digit of n²</text>
  <text x="80" y="85" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">1</text>
  <text x="80" y="105" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">4</text>
  <text x="80" y="125" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">6</text>
  <text x="80" y="145" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">9</text>
  <!-- Arrows -->
  <line x1="140" y1="85" x2="190" y2="85" stroke="#4ade80" stroke-width="2"/>
  <line x1="140" y1="105" x2="190" y2="105" stroke="#4ade80" stroke-width="2"/>
  <line x1="140" y1="125" x2="190" y2="125" stroke="#4ade80" stroke-width="2"/>
  <line x1="140" y1="145" x2="190" y2="145" stroke="#4ade80" stroke-width="2"/>
  <!-- Root Units Digit Output -->
  <rect x="200" y="40" width="170" height="110" rx="5" fill="#1e293b" stroke="#4ade80" stroke-width="1.5"/>
  <text x="285" y="60" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Possible Unit Digits of √n</text>
  <text x="285" y="85" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">1 or 9  (1+9 = 10)</text>
  <text x="285" y="105" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">2 or 8  (2+8 = 10)</text>
  <text x="285" y="125" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">4 or 6  (4+6 = 10)</text>
  <text x="285" y="145" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">3 or 7  (3+7 = 10)</text>
  <!-- Summary Box -->
  <text x="200" y="173" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Square root unit digits always come in complementary pairs totaling 10!</text>
</svg>
</div>
If a large perfect square number ends in 4, what are the only two possible unit digits of its square root?""",
     ["2 or 8", "1 or 9", "4 or 6", "3 or 7"],
     "A", "OSC", "easy",
     "Checking squares of single digits: \\(2^2 = 4\\) and \\(8^2 = 64\\) (ends in 4). No other single-digit squared produces 4 in the units place. Thus, the square root can only end in 2 or 8."),

    # 80: Sum of Digits Digital Root Property (9k, 9k+1, 9k+4, 9k+7)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Digital Root Theorem: Sum of Digits of Any Perfect Square</text>
  <!-- Permitted Digital Roots -->
  <rect x="25" y="40" width="165" height="105" rx="5" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="107" y="60" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">ALLOWED DIGITAL ROOTS</text>
  <text x="107" y="85" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">1, 4, 7, or 9 (0)</text>
  <text x="107" y="110" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Examples: 49 -> 4+9=13 -> 1+3=4</text>
  <text x="107" y="125" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">64 -> 6+4=10 -> 1+0=1</text>
  <!-- Forbidden Digital Roots -->
  <rect x="210" y="40" width="165" height="105" rx="5" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="292" y="60" fill="#f87171" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">FORBIDDEN DIGITAL ROOTS</text>
  <text x="292" y="85" fill="#fca5a5" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">2, 3, 5, 6, 8</text>
  <text x="292" y="110" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">If digital root is in this list,</text>
  <text x="292" y="125" fill="#ef4444" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">it is NEVER a square number!</text>
  <!-- Summary Box -->
  <text x="200" y="168" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Digital root modulo 9 provides a rapid mental test to discard non-square numbers!</text>
</svg>
</div>
The digital root (repeated sum of digits) of \\(3452\\) is \\(3 + 4 + 5 + 2 = 14 \\implies 1 + 4 = 5\\). Can \\(3452\\) be a square number?""",
     ["No, because the digital root of any perfect square can only be 1, 4, 7, or 9; digital root 5 is strictly impossible",
      "Yes, because 5 is a prime number",
      "Yes, because 3452 is an even number",
      "It cannot be determined from the digital root"],
     "A", "OSC", "medium",
     "Modulo 9, any integer squared satisfies \\(n^2 \\equiv 0^2, 1^2, 2^2, 3^2, 4^2, 5^2, 6^2, 7^2, 8^2 \\pmod 9\\), which evaluate to \\(0, 1, 4, 0, 7, 7, 0, 4, 1\\). Thus, the only possible digital roots of any square number are 1, 4, 7, and 9. Since 3452 has digital root 5, it cannot be a square number."),

    # 81: Non-Square Numbers Between Consecutive Squares: 2n
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Non-Square Numbers Between n² and (n + 1)²: Exactly 2n Numbers</text>
  <!-- Visual Number Line between 3²=9 and 4²=16 -->
  <rect x="30" y="50" width="50" height="50" rx="4" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="55" y="75" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">3² = 9</text>
  <!-- Non-squares in between -->
  <rect x="90" y="55" width="220" height="40" rx="4" fill="#1e293b" stroke="#facc15" stroke-width="1"/>
  <text x="200" y="75" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Non-Squares: 10, 11, 12, 13, 14, 15</text>
  <text x="200" y="88" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Count = 6 numbers = 2 x 3 = 2n</text>
  <!-- Next square 4²=16 -->
  <rect x="320" y="50" width="50" height="50" rx="4" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="345" y="75" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">4² = 16</text>
  <!-- Derivation Box -->
  <rect x="30" y="115" width="340" height="55" rx="4" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
  <text x="200" y="132" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Formula: Non-squares = (n + 1)² - n² - 1 = (2n + 1) - 1 = 2n</text>
  <text x="200" y="152" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Between 12² and 13²: exactly 2 x 12 = 24 non-square numbers!</text>
</svg>
</div>
How many non-square natural numbers lie strictly between \\(15^2\\) and \\(16^2\\)?""",
     ["\\(30\\) numbers (calculated as \\(2n = 2 \\times 15\\))",
      "\\(31\\) numbers",
      "\\(29\\) numbers",
      "\\(15\\) numbers"],
     "A", "OSC", "easy",
     "Between \\(n^2\\) and \\((n + 1)^2\\), the count of non-square natural numbers is given by \\((n + 1)^2 - n^2 - 1 = 2n + 1 - 1 = 2n\\). With \\(n = 15\\), the count is \\(2 \\times 15 = 30\\)."),

    # 82: Square of Sum Formula Geometrical Decomposition (a+b)^2
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="22" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Geometric Proof: (a + b)² = a² + 2ab + b²</text>
  <!-- Outer Square composed of 4 sub-rectangles -->
  <!-- a x a square (Upper Left) -->
  <rect x="60" y="40" width="70" height="70" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1.5"/>
  <text x="95" y="80" fill="#93c5fd" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">a²</text>
  <!-- a x b rectangle (Upper Right) -->
  <rect x="130" y="40" width="40" height="70" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="150" y="80" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">ab</text>
  <!-- b x a rectangle (Lower Left) -->
  <rect x="60" y="110" width="70" height="40" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="95" y="133" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">ab</text>
  <!-- b x b square (Lower Right) -->
  <rect x="130" y="110" width="40" height="40" fill="#78350f" stroke="#facc15" stroke-width="1.5"/>
  <text x="150" y="133" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">b²</text>
  <!-- Right Explanation Box -->
  <rect x="195" y="40" width="175" height="110" rx="5" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="282" y="65" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Mental Squaring of 52:</text>
  <text x="282" y="85" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">52 = 50 + 2 (a=50, b=2)</text>
  <text x="282" y="103" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">a² = 2500, 2ab = 200, b² = 4</text>
  <text x="282" y="123" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle">Sum = 2500 + 200 + 4</text>
  <text x="282" y="142" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">= 2704</text>
  <!-- Summary Footer -->
  <text x="200" y="173" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Algebraic decomposition breaks difficult squares into simple mental arithmetic!</text>
</svg>
</div>
How can \\(52^2\\) be evaluated mentally using the geometric expansion \\((a + b)^2 = a^2 + 2ab + b^2\\)?""",
     ["Write \\(52 = 50 + 2\\); then \\(50^2 + 2(50)(2) + 2^2 = 2500 + 200 + 4 = 2704\\)",
      "Multiply \\(5 \\times 2 = 10\\) and add 52 to get 62",
      "Square 5 to get 25 and square 2 to get 4, writing 254",
      "Multiply 52 by 2 to get 104"],
     "A", "OSC", "easy",
     "Decomposing \\(52\\) as \\((50 + 2)\\): \\((50 + 2)^2 = 50^2 + 2 \\times 50 \\times 2 + 2^2 = 2500 + 200 + 4 = 2704\\). This geometric decomposition allows rapid, error-free mental calculation.")
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

output_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch1_topic1.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
