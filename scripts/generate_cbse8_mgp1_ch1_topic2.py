# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-1-1.2
Topic: Patterns in Square Numbers & Pythagorean Triplets
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-1-1.2"

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
    ("What is the sum of the first \\(n\\) consecutive odd natural numbers?",
     ["\\(n^2\\)", "\\(2n\\)", "\\(n(n+1)\\)", "\\(n^2 - 1\\)"],
     "A", "OSC", "easy",
     "The sum of the first \\(n\\) odd natural numbers \\(1 + 3 + 5 + \\dots + (2n - 1)\\) is always equal to \\(n^2\\). For example, \\(1 + 3 = 4 = 2^2\\), and \\(1 + 3 + 5 = 9 = 3^2\\)."),

    # 2
    ("Express \\(49\\) as the sum of consecutive odd numbers starting from 1.",
     ["\\(1 + 3 + 5 + 7 + 9 + 11 + 13\\)",
      "\\(1 + 3 + 5 + 7 + 9 + 11\\)",
      "\\(3 + 5 + 7 + 9 + 11 + 14\\)",
      "\\(1 + 2 + 3 + 4 + 5 + 6 + 7\\)"],
     "A", "OSC", "easy",
     "Since \\(49 = 7^2\\), it is the sum of the first 7 odd numbers: \\(1 + 3 + 5 + 7 + 9 + 11 + 13 = 49\\)."),

    # 3
    ("Express \\(121\\) as the sum of odd numbers.",
     ["Sum of first 11 odd numbers (from 1 to 21)",
      "Sum of first 10 odd numbers",
      "Sum of first 12 odd numbers",
      "Sum of first 9 odd numbers"],
     "A", "OSC", "easy",
     "Since \\(121 = 11^2\\), it equals the sum of the first 11 consecutive odd numbers: \\(1 + 3 + 5 + \\dots + 21 = 121\\)."),

    # 4
    ("How many non-square natural numbers lie between \\(12^2\\) and \\(13^2\\)?",
     ["24", "25", "26", "12"],
     "A", "OSC", "easy",
     "The number of non-square natural numbers between \\(n^2\\) and \\((n+1)^2\\) is given by \\(2n\\). With \\(n = 12\\), the count is \\(2 \\times 12 = 24\\). (Between 144 and 169, the numbers are 145 to 168, which is \\(168 - 145 + 1 = 24\\))."),

    # 5
    ("How many non-square natural numbers lie between \\(25^2\\) and \\(26^2\\)?",
     ["50", "51", "52", "25"],
     "A", "OSC", "easy",
     "Using the formula \\(2n\\) for the count of non-squares between \\(n^2\\) and \\((n+1)^2\\), with \\(n = 25\\), we get \\(2 \\times 25 = 50\\)."),

    # 6
    ("How many non-square numbers lie between \\(99^2\\) and \\(100^2\\)?",
     ["198", "199", "200", "99"],
     "A", "OSC", "easy",
     "Here \\(n = 99\\). The count of non-square numbers is \\(2n = 2 \\times 99 = 198\\)."),

    # 7
    ("Which algebraic formula generates a Pythagorean triplet for any natural number \\(m > 1\\)?",
     ["\\((2m, m^2 - 1, m^2 + 1)\\)",
      "\\((m, m+1, m+2)\\)",
      "\\((m^2, m^2+1, m^2+2)\\)",
      "\\((2m, 2m+1, 2m+2)\\)"],
     "A", "OSC", "easy",
     "For any integer \\(m > 1\\), \\((2m)^2 + (m^2 - 1)^2 = 4m^2 + m^4 - 2m^2 + 1 = m^4 + 2m^2 + 1 = (m^2 + 1)^2\\). Thus, \\(2m\\), \\(m^2 - 1\\), and \\(m^2 + 1\\) always form a Pythagorean triplet."),

    # 8
    ("Find the Pythagorean triplet whose smallest member is 6.",
     ["(6, 8, 10)", "(6, 9, 12)", "(6, 12, 14)", "(6, 7, 8)"],
     "A", "OSC", "easy",
     "Let \\(2m = 6 \\implies m = 3\\). Then \\(m^2 - 1 = 3^2 - 1 = 8\\), and \\(m^2 + 1 = 3^2 + 1 = 10\\). Checking: \\(6^2 + 8^2 = 36 + 64 = 100 = 10^2\\). Thus, the triplet is (6, 8, 10)."),

    # 9
    ("Find the Pythagorean triplet whose smallest member is 14.",
     ["(14, 48, 50)", "(14, 40, 42)", "(14, 52, 54)", "(14, 28, 30)"],
     "A", "OSC", "easy",
     "Let \\(2m = 14 \\implies m = 7\\). Then \\(m^2 - 1 = 7^2 - 1 = 49 - 1 = 48\\), and \\(m^2 + 1 = 7^2 + 1 = 49 + 1 = 50\\). Checking: \\(14^2 + 48^2 = 196 + 2304 = 2500 = 50^2\\)."),

    # 10
    ("Find the Pythagorean triplet whose smallest member is 16.",
     ["(16, 63, 65)", "(16, 60, 62)", "(16, 30, 34)", "(16, 40, 44)"],
     "A", "OSC", "easy",
     "Let \\(2m = 16 \\implies m = 8\\). Then \\(m^2 - 1 = 8^2 - 1 = 63\\), and \\(m^2 + 1 = 8^2 + 1 = 65\\). Indeed, \\(16^2 + 63^2 = 256 + 3969 = 4225 = 65^2\\)."),

    # 11
    ("Find the Pythagorean triplet whose one member is 12 (where 12 is the \\(2m\\) member).",
     ["(12, 35, 37)", "(12, 30, 32)", "(12, 24, 28)", "(12, 16, 20)"],
     "A", "OSC", "easy",
     "Set \\(2m = 12 \\implies m = 6\\). Then \\(m^2 - 1 = 36 - 1 = 35\\) and \\(m^2 + 1 = 36 + 1 = 37\\). Checking: \\(12^2 + 35^2 = 144 + 1225 = 1369 = 37^2\\)."),

    # 12
    ("What is the value of \\(1111^2\\) using the digit 1 palindrome pattern?",
     ["1234321", "123454321", "12321", "11111111"],
     "A", "OSC", "easy",
     "The square of a number composed of \\(k\\) ones counts up from 1 to \\(k\\) and then counts down to 1. For 1111 (4 ones), \\(1111^2 = 1234321\\)."),

    # 13
    ("What is the value of \\(11111^2\\)?",
     ["123454321", "12345654321", "1234321", "1111100000"],
     "A", "OSC", "easy",
     "11111 has 5 ones. Counting up to 5 and back down gives \\(123454321\\)."),

    # 14
    ("What is the value of \\(67^2\\) based on the pattern \\(7^2 = 49, 67^2 = 4489\\)?",
     ["4489", "4889", "4488", "4498"],
     "A", "OSC", "easy",
     "The pattern produces one more 4 and one more 8: \\(7^2 = 49\\), \\(67^2 = 4489\\), \\(667^2 = 444889\\). Thus, \\(67^2 = 4489\\)."),

    # 15
    ("What is the value of \\(667^2\\)?",
     ["444889", "444489", "448889", "444888"],
     "A", "OSC", "easy",
     "Following the pattern: 667 has two 6s, so its square has three 4s, two 8s, and ends in 9: \\(444889\\). Indeed, \\(667 \\times 667 = 444889\\)."),

    # 16
    ("In the pattern \\(1^2 + 2^2 + 2^2 = 3^2\\), \\(2^2 + 3^2 + 6^2 = 7^2\\), and \\(3^2 + 4^2 + 12^2 = 13^2\\), what is the missing number in \\(4^2 + 5^2 + \\_\\_^2 = 21^2\\)?",
     ["20", "15", "18", "25"],
     "A", "OSC", "medium",
     "The third base is the product of the first two bases: \\(n(n+1)\\). Here \\(4 \\times 5 = 20\\). The fourth base is \\(n(n+1) + 1 = 20 + 1 = 21\\). Thus, the missing number is 20."),

    # 17
    ("In the same pattern, find the missing sum: \\(5^2 + 6^2 + 30^2 = \\_\\_^2\\).",
     ["\\(31^2\\)", "\\(35^2\\)", "\\(30^2\\)", "\\(32^2\\)"],
     "A", "OSC", "easy",
     "The right-hand base is always one greater than the third base: \\(30 + 1 = 31\\). So the sum equals \\(31^2\\)."),

    # 18
    ("In the same pattern, what is \\(6^2 + 7^2 + 42^2\\) equal to?",
     ["\\(43^2\\)", "\\(42^2\\)", "\\(49^2\\)", "\\(45^2\\)"],
     "A", "OSC", "easy",
     "Here \\(6 \\times 7 = 42\\), so the right-hand base is \\(42 + 1 = 43\\). Thus, \\(6^2 + 7^2 + 42^2 = 43^2\\)."),

    # 19
    ("What are triangular numbers?",
     ["Numbers whose dot patterns can be arranged as equilateral triangles: 1, 3, 6, 10, 15, ...",
      "Numbers divisible by 3",
      "Numbers with 3 digits",
      "Numbers equal to three times a square"],
     "A", "OSC", "easy",
     "Triangular numbers are generated by \\(T_n = \\frac{n(n+1)}{2}\\). The first few are 1, 3, 6, 10, 15, 21, which represent quantities of dots arranged in triangular arrays."),

    # 20
    ("What is obtained when any two consecutive triangular numbers are added together?",
     ["A perfect square", "Another triangular number", "A prime number", "An odd number always"],
     "A", "OSC", "medium",
     "The sum of consecutive triangular numbers is \\(T_{n-1} + T_n = \\frac{(n-1)n}{2} + \\frac{n(n+1)}{2} = \\frac{n^2 - n + n^2 + n}{2} = \\frac{2n^2}{2} = n^2\\), which is always a perfect square (e.g. \\(1+3=4=2^2\\), \\(3+6=9=3^2\\), \\(6+10=16=4^2\\))."),

    # 21
    ("Which two consecutive triangular numbers add up to \\(25\\)?",
     ["10 and 15", "6 and 19", "12 and 13", "9 and 16"],
     "A", "OSC", "easy",
     "The 4th triangular number is \\(T_4 = 10\\) and the 5th is \\(T_5 = 15\\). Their sum is \\(10 + 15 = 25 = 5^2\\)."),

    # 22
    ("Which two consecutive triangular numbers add up to \\(36\\)?",
     ["15 and 21", "16 and 20", "10 and 26", "18 and 18"],
     "A", "OSC", "easy",
     "The 5th triangular number is 15 and the 6th is 21. Their sum is \\(15 + 21 = 36 = 6^2\\)."),

    # 23
    ("Without adding the terms individually, find the sum of \\(1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19\\).",
     ["100", "90", "110", "81"],
     "A", "OSC", "easy",
     "There are 10 consecutive odd numbers starting from 1. Their sum is \\(10^2 = 100\\)."),

    # 24
    ("Find the sum of \\(1 + 3 + 5 + 7 + 9 + 11 + 13 + 15\\).",
     ["64", "49", "81", "72"],
     "A", "OSC", "easy",
     "There are 8 consecutive odd numbers starting from 1. Their sum is \\(8^2 = 64\\)."),

    # 25
    ("Can \\(37\\) be expressed as the sum of consecutive odd natural numbers starting from 1?",
     ["No, because 37 is not a perfect square",
      "Yes, because 37 is odd",
      "Yes, as the sum of 6 odd numbers",
      "Yes, as 1 + 36"],
     "A", "OSC", "easy",
     "Every sum of consecutive odd numbers starting from 1 must equal \\(n^2\\) (a perfect square). Since 37 is not a square (\\(6^2=36, 7^2=49\\)), it can never be expressed as such a sum."),

    # 26
    ("If \\(1 + 3 + 5 + \\dots + (2k - 1) = 225\\), what is the value of \\(k\\)?",
     ["15", "25", "14", "16"],
     "A", "OSC", "easy",
     "The sum of the first \\(k\\) odd numbers is \\(k^2\\). Setting \\(k^2 = 225\\) gives \\(k = \\sqrt{225} = 15\\)."),

    # 27
    ("If \\((8, 15, x)\\) is a Pythagorean triplet, what is the value of \\(x\\)?",
     ["17", "16", "19", "23"],
     "A", "OSC", "easy",
     "\\(8^2 + 15^2 = 64 + 225 = 289\\). Since \\(\\sqrt{289} = 17\\), \\(x = 17\\)."),

    # 28
    ("If \\((9, 40, y)\\) is a Pythagorean triplet, what is the value of \\(y\\)?",
     ["41", "42", "45", "49"],
     "A", "OSC", "easy",
     "\\(9^2 + 40^2 = 81 + 1600 = 1681\\). Since \\(\\sqrt{1681} = 41\\), \\(y = 41\\)."),

    # 29
    ("Is \\((5, 12, 13)\\) a Pythagorean triplet? Verify.",
     ["Yes, because \\(5^2 + 12^2 = 25 + 144 = 169 = 13^2\\)",
      "No, because 13 is an odd number",
      "No, because 5 is a prime number",
      "No, because 12 is divisible by 3"],
     "A", "OSC", "easy",
     "\\(5^2 + 12^2 = 25 + 144 = 169\\), which equals \\(13^2\\). Since \\(a^2 + b^2 = c^2\\) holds true, (5, 12, 13) is a valid Pythagorean triplet."),

    # 30
    ("Is \\((7, 24, 25)\\) a Pythagorean triplet?",
     ["Yes, because \\(7^2 + 24^2 = 49 + 576 = 625 = 25^2\\)",
      "No, because \\(7 + 24 \\neq 25\\)",
      "No, because 25 is not prime",
      "No, because 24 is even"],
     "A", "OSC", "easy",
     "\\(7^2 + 24^2 = 49 + 576 = 625 = 25^2\\). Thus, it satisfies the Pythagorean relation."),

    # 31
    ("What is the sum of the digits of \\(111^2\\)?",
     ["9", "6", "12", "15"],
     "A", "OSC", "medium",
     "\\(111^2 = 12321\\). The sum of its digits is \\(1 + 2 + 3 + 2 + 1 = 9\\). Notice that for \\(k\\) ones, the sum of digits of the square is \\(k^2\\); here \\(3^2 = 9\\)."),

    # 32
    ("What is the sum of the digits of \\(1111^2\\)?",
     ["16", "12", "14", "18"],
     "A", "OSC", "medium",
     "\\(1111^2 = 1234321\\). The sum of its digits is \\(1 + 2 + 3 + 4 + 3 + 2 + 1 = 16\\). This equals \\(4^2 = 16\\)."),

    # 33
    ("In a Pythagorean triplet \\((a, b, c)\\) generated by \\(m\\), if \\(m^2 - 1 = 15\\), what is the value of \\(m\\)?",
     ["4", "3", "5", "16"],
     "A", "OSC", "easy",
     "\\(m^2 - 1 = 15 \\implies m^2 = 16 \\implies m = 4\\). The full triplet is \\((2m, m^2-1, m^2+1) = (8, 15, 17)\\)."),

    # 34
    ("If \\(m^2 + 1 = 26\\), what are the members of the Pythagorean triplet?",
     ["(10, 24, 26)", "(10, 20, 26)", "(12, 24, 26)", "(8, 24, 26)"],
     "A", "OSC", "easy",
     "\\(m^2 + 1 = 26 \\implies m^2 = 25 \\implies m = 5\\). Then \\(2m = 2(5) = 10\\) and \\(m^2 - 1 = 25 - 1 = 24\\). Thus, the triplet is (10, 24, 26)."),

    # 35
    ("How many numbers lie between \\(n^2\\) and \\((n+1)^2\\) inclusive of both squares?",
     ["\\(2n + 2\\)", "\\(2n\\)", "\\(2n + 1\\)", "\\(n^2\\)"],
     "A", "OSC", "medium",
     "The total number of integers from \\(n^2\\) to \\((n+1)^2\\) inclusive is \\((n+1)^2 - n^2 + 1 = (2n + 1) + 1 = 2n + 2\\)."),

    # 36
    ("How many numbers lie strictly between \\(10^2\\) and \\(11^2\\)?",
     ["20", "21", "22", "19"],
     "A", "OSC", "easy",
     "\\(2n = 2 \\times 10 = 20\\). The numbers are 101 through 120, which is exactly 20 numbers."),

    # 37
    ("What is the next number in the sequence of triangular numbers: 1, 3, 6, 10, 15, 21, ...?",
     ["28", "25", "27", "30"],
     "A", "OSC", "easy",
     "The differences between successive triangular numbers increase by 1: \\(+2, +3, +4, +5, +6\\). The next difference is \\(+7\\), so \\(21 + 7 = 28\\). Alternatively, \\(T_7 = \\frac{7 \\times 8}{2} = 28\\)."),

    # 38
    ("Which of the following is NOT a Pythagorean triplet?",
     ["(5, 7, 9)", "(3, 4, 5)", "(5, 12, 13)", "(8, 15, 17)"],
     "A", "OSC", "easy",
     "Check (5, 7, 9): \\(5^2 + 7^2 = 25 + 49 = 74\\), but \\(9^2 = 81 \\neq 74\\). Thus, (5, 7, 9) is not a Pythagorean triplet."),

    # 39
    ("What is \\(10^2 - 9^2\\)?",
     ["19", "1", "10", "100"],
     "A", "OSC", "easy",
     "Using \\((n+1)^2 - n^2 = (n+1) + n\\): \\(10 + 9 = 19\\). Indeed, \\(100 - 81 = 19\\)."),

    # 40
    ("What is \\(50^2 - 49^2\\)?",
     ["99", "100", "1", "98"],
     "A", "OSC", "easy",
     "\\(50 + 49 = 99\\). Indeed, \\(2500 - 2401 = 99\\).")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    ("How many non-square numbers lie between \\(40^2\\) and \\(41^2\\)?",
     ["80", "81", "82", "40"],
     "A", "OSC", "easy",
     "Between \\(n^2\\) and \\((n+1)^2\\), there are \\(2n\\) non-square numbers. For \\(n = 40\\), \\(2 \\times 40 = 80\\)."),

    # 42
    ("How many non-square numbers lie between \\(50^2\\) and \\(51^2\\)?",
     ["100", "101", "102", "50"],
     "A", "OSC", "easy",
     "\\(2n = 2 \\times 50 = 100\\)."),

    # 43
    ("Express 100 as the sum of 10 odd numbers.",
     ["\\(1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19\\)",
      "\\(1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 21\\)",
      "\\(3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 + 21\\)",
      "\\(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10\\)"],
     "A", "OSC", "easy",
     "Since \\(100 = 10^2\\), it is the sum of the first 10 consecutive odd numbers starting from 1."),

    # 44
    ("Find the smallest member of a Pythagorean triplet whose largest member is 65 (using \\(m^2+1 = 65\\)).",
     ["16", "8", "63", "32"],
     "A", "OSC", "medium",
     "Setting \\(m^2 + 1 = 65 \\implies m^2 = 64 \\implies m = 8\\). The smallest member is \\(2m = 2 \\times 8 = 16\\). The full triplet is (16, 63, 65)."),

    # 45
    ("Find the Pythagorean triplet whose one member is 18.",
     ["(18, 80, 82)", "(18, 36, 40)", "(18, 72, 74)", "(18, 50, 52)"],
     "A", "OSC", "medium",
     "Let \\(2m = 18 \\implies m = 9\\). Then \\(m^2 - 1 = 9^2 - 1 = 80\\) and \\(m^2 + 1 = 9^2 + 1 = 82\\). Checking: \\(18^2 + 80^2 = 324 + 6400 = 6724 = 82^2\\)."),

    # 46
    ("Find the Pythagorean triplet whose one member is 20.",
     ["(20, 99, 101)", "(20, 40, 45)", "(20, 80, 82)", "(20, 60, 64)"],
     "A", "OSC", "medium",
     "Let \\(2m = 20 \\implies m = 10\\). Then \\(m^2 - 1 = 100 - 1 = 99\\) and \\(m^2 + 1 = 100 + 1 = 101\\). Indeed, \\(20^2 + 99^2 = 400 + 9801 = 10201 = 101^2\\)."),

    # 47
    ("What is the value of \\(6667^2\\) using the pattern?",
     ["44448889", "44488889", "44448888", "44488899"],
     "A", "OSC", "medium",
     "6667 has three 6s. The pattern yields four 4s, three 8s, and one 9: \\(44448889\\)."),

    # 48
    ("What is the value of \\(66667^2\\)?",
     ["4444488889", "4444888889", "4444488888", "4444888899"],
     "A", "OSC", "medium",
     "66667 has four 6s. Squaring it produces five 4s, four 8s, and one 9: \\(4444488889\\)."),

    # 49
    ("Which of the following is a Pythagorean triplet with an odd smallest member \\(2m + 1\\)?",
     ["(3, 4, 5)", "(4, 6, 8)", "(2, 3, 4)", "(6, 8, 12)"],
     "A", "OSC", "easy",
     "In (3, 4, 5), \\(3^2 + 4^2 = 9 + 16 = 25 = 5^2\\). 3 is the smallest member and is odd."),

    # 50
    ("What is the missing term in: \\(7^2 + 8^2 + 56^2 = \\_\\_^2\\)?",
     ["\\(57^2\\)", "\\(56^2\\)", "\\(64^2\\)", "\\(58^2\\)"],
     "A", "OSC", "easy",
     "Here \\(7 \\times 8 = 56\\). The right-hand side is \\((56 + 1)^2 = 57^2\\)."),

    # 51
    ("What is the missing term in: \\(8^2 + 9^2 + \\_\\_^2 = 73^2\\)?",
     ["72", "71", "70", "81"],
     "A", "OSC", "easy",
     "The missing base is \\(8 \\times 9 = 72\\). Checking: \\(72 + 1 = 73\\), so \\(8^2 + 9^2 + 72^2 = 73^2\\)."),

    # 52
    ("What is the missing term in: \\(9^2 + 10^2 + 90^2 = \\_\\_^2\\)?",
     ["\\(91^2\\)", "\\(90^2\\)", "\\(100^2\\)", "\\(92^2\\)"],
     "A", "OSC", "easy",
     "\\(90 + 1 = 91\\). Thus, the sum is \\(91^2\\)."),

    # 53
    ("What is the sum of \\(T_6\\) and \\(T_7\\) (the 6th and 7th triangular numbers)?",
     ["49", "36", "64", "45"],
     "A", "OSC", "easy",
     "\\(T_6 = 21\\) and \\(T_7 = 28\\). Adding them: \\(21 + 28 = 49 = 7^2\\)."),

    # 54
    ("What is the sum of \\(T_7\\) and \\(T_8\\)?",
     ["64", "49", "81", "56"],
     "A", "OSC", "easy",
     "\\(T_7 = 28\\) and \\(T_8 = 36\\). Adding them: \\(28 + 36 = 64 = 8^2\\)."),

    # 55
    ("What is the sum of \\(T_9\\) and \\(T_{10}\\)?",
     ["100", "81", "121", "90"],
     "A", "OSC", "easy",
     "\\(T_{n-1} + T_n = n^2\\). With \\(n = 10\\), \\(T_9 + T_{10} = 10^2 = 100\\). (Indeed, \\(45 + 55 = 100\\))."),

    # 56
    ("What is the difference between \\(75^2\\) and \\(74^2\\)?",
     ["149", "150", "1", "148"],
     "A", "OSC", "easy",
     "\\(75 + 74 = 149\\)."),

    # 57
    ("What is the difference between \\(100^2\\) and \\(99^2\\)?",
     ["199", "200", "1", "198"],
     "A", "OSC", "easy",
     "\\(100 + 99 = 199\\)."),

    # 58
    ("If \\(x^2 - (x - 1)^2 = 85\\), what is the value of \\(x\\)?",
     ["43", "42", "44", "41"],
     "A", "OSC", "medium",
     "\\(x^2 - (x - 1)^2 = x + (x - 1) = 2x - 1\\). Setting \\(2x - 1 = 85 \\implies 2x = 86 \\implies x = 43\\). Check: \\(43^2 - 42^2 = 43 + 42 = 85\\)."),

    # 59
    ("If \\((y + 1)^2 - y^2 = 135\\), what is the value of \\(y\\)?",
     ["67", "68", "66", "70"],
     "A", "OSC", "medium",
     "\\((y + 1) + y = 2y + 1 = 135 \\implies 2y = 134 \\implies y = 67\\). Check: \\(68^2 - 67^2 = 68 + 67 = 135\\)."),

    # 60
    ("What is \\(1 + 3 + 5 + \\dots + 39\\)?",
     ["400", "361", "441", "380"],
     "A", "OSC", "medium",
     "The last term is \\(2n - 1 = 39 \\implies 2n = 40 \\implies n = 20\\). The sum of the first 20 odd numbers is \\(20^2 = 400\\)."),

    # 61
    ("What is \\(1 + 3 + 5 + \\dots + 49\\)?",
     ["625", "576", "676", "525"],
     "A", "OSC", "medium",
     "\\(2n - 1 = 49 \\implies 2n = 50 \\implies n = 25\\). Sum is \\(25^2 = 625\\)."),

    # 62
    ("How many odd numbers are added together to make \\(900\\)?",
     ["30", "45", "15", "60"],
     "A", "OSC", "easy",
     "\\(n^2 = 900 \\implies n = 30\\). Thus, 30 consecutive odd numbers starting from 1."),

    # 63
    ("How many non-square numbers lie between \\(70^2\\) and \\(71^2\\)?",
     ["140", "141", "142", "70"],
     "A", "OSC", "easy",
     "\\(2n = 2 \\times 70 = 140\\)."),

    # 64
    ("How many non-square numbers lie between \\(85^2\\) and \\(86^2\\)?",
     ["170", "171", "172", "85"],
     "A", "OSC", "easy",
     "\\(2n = 2 \\times 85 = 170\\)."),

    # 65
    ("What is the hypotenuse of a right triangle with legs of length 20 cm and 21 cm?",
     ["29 cm", "28 cm", "31 cm", "25 cm"],
     "A", "OSC", "medium",
     "\\(20^2 + 21^2 = 400 + 441 = 841\\). Since \\(\\sqrt{841} = 29\\), the hypotenuse is 29 cm. (20, 21, 29) forms a Pythagorean triplet."),

    # 66
    ("What is the hypotenuse of a right triangle with legs of length 11 cm and 60 cm?",
     ["61 cm", "62 cm", "59 cm", "65 cm"],
     "A", "OSC", "medium",
     "\\(11^2 + 60^2 = 121 + 3600 = 3721 = 61^2\\). Thus, the hypotenuse is 61 cm."),

    # 67
    ("What is the hypotenuse of a right triangle with legs of length 12 cm and 16 cm?",
     ["20 cm", "22 cm", "18 cm", "24 cm"],
     "A", "OSC", "easy",
     "Notice that 12, 16 are \\(4 \\times 3\\) and \\(4 \\times 4\\). Scaling the primitive triplet (3, 4, 5) by 4 gives \\(4 \\times 5 = 20\\) cm."),

    # 68
    ("If a primitive Pythagorean triplet is multiplied by an integer \\(k\\), is the result \\((ka, kb, kc)\\) also a Pythagorean triplet?",
     ["Yes, because \\((ka)^2 + (kb)^2 = k^2(a^2 + b^2) = k^2 c^2 = (kc)^2\\)",
      "No, only original triplets work",
      "Only if \\(k\\) is prime",
      "Only if \\(k\\) is even"],
     "A", "OSC", "easy",
     "Multiplying each side of \\(a^2 + b^2 = c^2\\) by \\(k^2\\) gives \\(k^2 a^2 + k^2 b^2 = k^2 c^2 \\implies (ka)^2 + (kb)^2 = (kc)^2\\). Thus, any multiple of a Pythagorean triplet is also a Pythagorean triplet."),

    # 69
    ("Multiply the triplet (3, 4, 5) by \\(k = 5\\). What triplet is produced?",
     ["(15, 20, 25)", "(15, 20, 30)", "(10, 15, 20)", "(8, 9, 10)"],
     "A", "OSC", "easy",
     "\\(3 \\times 5 = 15\\), \\(4 \\times 5 = 20\\), \\(5 \\times 5 = 25\\). Checking: \\(15^2 + 20^2 = 225 + 400 = 625 = 25^2\\)."),

    # 70
    ("What is the sum of \\(1 + 3 + 5 + \\dots + 99\\)?",
     ["2500", "2401", "2601", "2450"],
     "A", "OSC", "medium",
     "The odd numbers from 1 to 99: \\(2n - 1 = 99 \\implies 2n = 100 \\implies n = 50\\). Sum of the first 50 odd numbers is \\(50^2 = 2500\\).")
]

# 12 MOCK / FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71: Visual Proof of Sum of Odd Numbers (L-shaped Gnomons)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="22" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Visual Proof: Sum of Consecutive Odd Numbers = n²</text>
  <!-- 1st square (1x1 = 1) -->
  <rect x="40" y="40" width="25" height="25" fill="#facc15" stroke="#eab308" stroke-width="1.5"/>
  <text x="52" y="56" fill="#000000" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">1</text>
  <!-- 2nd L-bracket (+3 -> 2x2 = 4) -->
  <rect x="65" y="40" width="25" height="25" fill="#38bdf8"/>
  <rect x="65" y="65" width="25" height="25" fill="#38bdf8"/>
  <rect x="40" y="65" width="25" height="25" fill="#38bdf8"/>
  <text x="65" y="80" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">+3</text>
  <!-- 3rd L-bracket (+5 -> 3x3 = 9) -->
  <rect x="90" y="40" width="25" height="75" fill="#4ade80" opacity="0.8"/>
  <rect x="40" y="90" width="50" height="25" fill="#4ade80" opacity="0.8"/>
  <text x="95" y="105" fill="#000000" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">+5</text>
  <!-- 4th L-bracket (+7 -> 4x4 = 16) -->
  <rect x="115" y="40" width="25" height="100" fill="#f43f5e" opacity="0.8"/>
  <rect x="40" y="115" width="75" height="25" fill="#f43f5e" opacity="0.8"/>
  <text x="120" y="130" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">+7</text>
  <!-- Explanation Panel on Right -->
  <rect x="180" y="40" width="195" height="120" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="277" y="62" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Gnomon Layering:</text>
  <text x="277" y="80" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Layer 1: 1 = 1²</text>
  <text x="277" y="96" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Layer 2: 1 + 3 = 4 = 2²</text>
  <text x="277" y="112" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Layer 3: 1 + 3 + 5 = 9 = 3²</text>
  <text x="277" y="128" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Layer 4: 1 + 3 + 5 + 7 = 16 = 4²</text>
  <text x="277" y="148" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Sum of first n odds = n²</text>
  <!-- Footer Note -->
  <text x="200" y="185" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Each new square is built by wrapping an L-shaped strip (gnomon) of (2n - 1) dots!</text>
</svg>
</div>
How does the geometric L-bracket (gnomon) diagram above visually prove that \\(1 + 3 + 5 + 7 = 4^2\\)?""",
     ["Each successive odd number \\(2k - 1\\) wraps around the previous \\((k-1) \\times (k-1)\\) square as an L-shaped strip of width 1, creating a new \\(k \\times k\\) square",
      "By adding four separate rectangles of equal areas",
      "Because odd numbers always form circles",
      "Because 16 is divisible by 4"],
     "A", "OSC", "easy",
     "Starting with a \\(1 \\times 1\\) square (1 dot), adding an L-shaped border of 3 dots forms a \\(2 \\times 2\\) square (4 dots). Adding 5 dots forms a \\(3 \\times 3\\) square (9 dots). Adding 7 dots forms a \\(4 \\times 4\\) square (16 dots). In general, adding the \\(n\\)-th odd number \\(2n - 1\\) completes an \\(n \\times n\\) square of area \\(n^2\\)."),

    # 72: Pythagorean Triplet Right-Angled Triangle
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Right Triangle: legs 2m, m²-1, hyp m²+1 -->
  <polygon points="70,150 210,150 210,50" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <!-- Right Angle Marker -->
  <rect x="195" y="135" width="15" height="15" fill="none" stroke="#facc15" stroke-width="1.5"/>
  <!-- Dimension Labels -->
  <text x="140" y="168" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Base = 2m</text>
  <text x="235" y="105" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Height = m² - 1</text>
  <text x="120" y="90" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Hypotenuse = m² + 1</text>
  <!-- Proof Box on Right -->
  <rect x="255" y="30" width="130" height="145" rx="5" fill="#0f172a" stroke="#4ade80" stroke-width="1.5"/>
  <text x="320" y="50" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Algebraic Proof:</text>
  <text x="320" y="70" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">(2m)² = 4m²</text>
  <text x="320" y="90" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">(m²-1)² = m⁴ - 2m² + 1</text>
  <text x="320" y="112" fill="#facc15" font-size="7" font-family="sans-serif" text-anchor="middle">Sum = m⁴ + 2m² + 1</text>
  <text x="320" y="132" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">= (m² + 1)²</text>
  <text x="320" y="155" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Exact Match!</text>
</svg>
</div>
In the right triangle shown above, why are \\(2m\\), \\(m^2 - 1\\), and \\(m^2 + 1\\) guaranteed to form integer side lengths of a right triangle for any integer \\(m > 1\\)?""",
     ["Expanding \\((2m)^2 + (m^2 - 1)^2 = 4m^2 + m^4 - 2m^2 + 1 = m^4 + 2m^2 + 1 = (m^2 + 1)^2\\), which identically satisfies Pythagoras theorem \\(a^2 + b^2 = c^2\\)",
      "Because right triangles always have integer coordinates",
      "Because \\(m^2 + 1\\) is always an odd number",
      "Because \\(2m\\) is an even integer"],
     "A", "OSC", "medium",
     "By algebraic identity, \\((2m)^2 + (m^2 - 1)^2 = 4m^2 + (m^4 - 2m^2 + 1) = m^4 + 2m^2 + 1 = (m^2 + 1)^2\\). Since the sum of the squares of the two shorter sides identically equals the square of the longest side for any integer \\(m > 1\\), the three lengths always satisfy the Pythagorean theorem."),

    # 73: Triangular Numbers Merging into a Square
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="22" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Geometric Pairing: Two Consecutive Triangular Numbers Form a Square</text>
  <!-- Triangular Number T3 = 6 (Cyan dots) -->
  <rect x="30" y="35" width="90" height="90" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="75" y="52" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">T3 = 6</text>
  <circle cx="50" cy="70" r="4" fill="#38bdf8"/>
  <circle cx="50" cy="90" r="4" fill="#38bdf8"/>
  <circle cx="70" cy="90" r="4" fill="#38bdf8"/>
  <circle cx="50" cy="110" r="4" fill="#38bdf8"/>
  <circle cx="70" cy="110" r="4" fill="#38bdf8"/>
  <circle cx="90" cy="110" r="4" fill="#38bdf8"/>
  <!-- Plus sign -->
  <text x="135" y="85" fill="#ffffff" font-size="16" font-family="sans-serif" text-anchor="middle" font-weight="bold">+</text>
  <!-- Triangular Number T4 = 10 (Green dots) -->
  <rect x="150" y="35" width="90" height="90" rx="4" fill="#1e293b" stroke="#4ade80" stroke-width="1.5"/>
  <text x="195" y="52" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">T4 = 10</text>
  <!-- 10 dots -->
  <circle cx="165" cy="65" r="3.5" fill="#4ade80"/>
  <circle cx="165" cy="80" r="3.5" fill="#4ade80"/>
  <circle cx="180" cy="80" r="3.5" fill="#4ade80"/>
  <circle cx="165" cy="95" r="3.5" fill="#4ade80"/>
  <circle cx="180" cy="95" r="3.5" fill="#4ade80"/>
  <circle cx="195" cy="95" r="3.5" fill="#4ade80"/>
  <circle cx="165" cy="110" r="3.5" fill="#4ade80"/>
  <circle cx="180" cy="110" r="3.5" fill="#4ade80"/>
  <circle cx="195" cy="110" r="3.5" fill="#4ade80"/>
  <circle cx="210" cy="110" r="3.5" fill="#4ade80"/>
  <!-- Equals sign -->
  <text x="255" y="85" fill="#ffffff" font-size="16" font-family="sans-serif" text-anchor="middle" font-weight="bold">=</text>
  <!-- Merged 4x4 Square (16 dots) -->
  <rect x="275" y="35" width="105" height="105" rx="5" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
  <text x="327" y="52" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">4 x 4 = 16 = 4²</text>
  <text x="327" y="155" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">6 + 10 = 16</text>
  <!-- Summary text -->
  <text x="200" y="180" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Formula: T_{n-1} + T_n = n(n-1)/2 + n(n+1)/2 = n²</text>
</svg>
</div>
What fundamental property of numbers is demonstrated by combining the two triangular arrays \\(T_3 = 6\\) and \\(T_4 = 10\\) into a \\(4 \\times 4\\) square?""",
     ["The sum of any two consecutive triangular numbers \\(T_{n-1} + T_n\\) is always equal to the square number \\(n^2\\)",
      "Triangular numbers cannot be added together",
      "The sum of two triangular numbers is always an odd number",
      "Squares can only be formed by even numbers"],
     "A", "OSC", "easy",
     "A triangular number is \\(T_n = \\frac{n(n+1)}{2}\\). Combining \\(T_{n-1}\\) and \\(T_n\\) joins two complementary staircase triangles along their diagonal to form a solid square grid of \\(n \\times n = n^2\\) dots. Here, \\(T_3 + T_4 = 6 + 10 = 16 = 4^2\\)."),

    # 74: Palindromic Digit 1 Pyramid Pattern
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="22" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Palindromic Digit-1 Square Pyramid Pattern</text>
  <!-- Pyramid Lines -->
  <text x="200" y="48" fill="#ffffff" font-size="9" font-family="monospace" text-anchor="middle">1² = 1</text>
  <text x="200" y="68" fill="#ffffff" font-size="9" font-family="monospace" text-anchor="middle">11² = 1 2 1</text>
  <text x="200" y="88" fill="#ffffff" font-size="9" font-family="monospace" text-anchor="middle">111² = 1 2 3 2 1</text>
  <text x="200" y="108" fill="#facc15" font-size="9" font-family="monospace" text-anchor="middle" font-weight="bold">1111² = 1 2 3 4 3 2 1</text>
  <text x="200" y="128" fill="#4ade80" font-size="9" font-family="monospace" text-anchor="middle" font-weight="bold">11111² = 1 2 3 4 5 4 3 2 1</text>
  <text x="200" y="148" fill="#38bdf8" font-size="9" font-family="monospace" text-anchor="middle" font-weight="bold">111111² = 1 2 3 4 5 6 5 4 3 2 1</text>
  <!-- Rule Banner -->
  <rect x="30" y="162" width="340" height="25" rx="3" fill="#1e293b" stroke="#facc15" stroke-width="1"/>
  <text x="200" y="178" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Symmetric Peak: The center digit always equals the number of 1s in the base!</text>
</svg>
</div>
Using the palindromic pyramid pattern illustrated above, what is the value of \\((1111111)^2\\) (the square of 7 ones)?""",
     ["\\(1234567654321\\)",
      "\\(12345654321\\)",
      "\\(123456787654321\\)",
      "\\(11111110000000\\)"],
     "A", "OSC", "easy",
     "When squaring a number consisting of \\(k\\) ones (for \\(k \\le 9\\)), the product is a numerical palindrome whose digits count incrementally from 1 up to \\(k\\) and then back down to 1. For 7 ones, the peak digit is 7, yielding \\(1234567654321\\)."),

    # 75: Consecutive Squares Non-Square Interval (2n)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Counting Non-Square Numbers: Exactly 2n Numbers Between n² and (n + 1)²</text>
  <!-- Left Square: 5² = 25 -->
  <rect x="30" y="50" width="55" height="50" rx="4" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="57" y="75" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">5² = 25</text>
  <!-- Middle Non-Squares Array -->
  <rect x="95" y="50" width="210" height="50" rx="4" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="200" y="70" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Non-squares: 26, 27, 28, 29, 30, 31, 32, 33, 34, 35</text>
  <text x="200" y="88" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Total Count = 10 = 2 x 5 = 2n numbers</text>
  <!-- Right Square: 6² = 36 -->
  <rect x="315" y="50" width="55" height="50" rx="4" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="342" y="75" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">6² = 36</text>
  <!-- Mathematical Derivation -->
  <rect x="30" y="115" width="340" height="55" rx="4" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
  <text x="200" y="133" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Formula: [(n + 1)² - 1] - [n²] = n² + 2n + 1 - 1 - n² = 2n</text>
  <text x="200" y="153" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Between 100² and 101²: exactly 2 x 100 = 200 non-square integers!</text>
</svg>
</div>
How many non-square natural numbers lie strictly between \\(20^2\\) and \\(21^2\\)?""",
     ["\\(40\\) numbers (given by \\(2n = 2 \\times 20\\))",
      "\\(41\\) numbers",
      "\\(39\\) numbers",
      "\\(20\\) numbers"],
     "A", "OSC", "easy",
     "The count of non-square integers between \\(n^2\\) and \\((n+1)^2\\) is given by \\((n+1)^2 - n^2 - 1 = (2n + 1) - 1 = 2n\\). With \\(n = 20\\), the count is \\(2 \\times 20 = 40\\)."),

    # 76: Special Algebraic Triplet Generator Pattern: 1² + 2² + 2² = 3²
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="22" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Identity: n² + (n + 1)² + [n(n + 1)]² = [n(n + 1) + 1]²</text>
  <!-- Pattern Rows -->
  <rect x="30" y="38" width="340" height="110" rx="5" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="200" y="58" fill="#ffffff" font-size="9" font-family="monospace" text-anchor="middle">1² + 2² +  2² =  3²  (1 x 2 = 2,  2 + 1 = 3)</text>
  <text x="200" y="80" fill="#ffffff" font-size="9" font-family="monospace" text-anchor="middle">2² + 3² +  6² =  7²  (2 x 3 = 6,  6 + 1 = 7)</text>
  <text x="200" y="102" fill="#ffffff" font-size="9" font-family="monospace" text-anchor="middle">3² + 4² + 12² = 13²  (3 x 4 = 12, 12 + 1 = 13)</text>
  <text x="200" y="124" fill="#4ade80" font-size="9" font-family="monospace" text-anchor="middle" font-weight="bold">4² + 5² + 20² = 21²  (4 x 5 = 20, 20 + 1 = 21)</text>
  <!-- Bottom Takeaway -->
  <text x="200" y="170" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">The 3rd base is the product of the first two; the 4th base is the 3rd base plus 1!</text>
</svg>
</div>
Using the mathematical identity \\(n^2 + (n+1)^2 + [n(n+1)]^2 = [n(n+1)+1]^2\\), what is the missing value in \\(10^2 + 11^2 + \\_\\_^2 = 111^2\\)?""",
     ["\\(110\\) (calculated as \\(10 \\times 11\\))",
      "\\(105\\)",
      "\\(111\\)",
      "\\(100\\)"],
     "A", "OSC", "easy",
     "In this pattern, the third base is the product of the first two consecutive numbers: \\(n \\times (n+1) = 10 \\times 11 = 110\\). The right-hand base is \\(110 + 1 = 111\\). Thus, the missing number is 110."),

    # 77: Pattern of 6s and 7s
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Pattern in Squares of Numbers Ending in 7 with Leading 6s</text>
  <!-- Table Rows -->
  <rect x="40" y="40" width="320" height="105" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="120" y="62" fill="#ffffff" font-size="9" font-family="monospace">7²</text>
  <text x="180" y="62" fill="#38bdf8" font-size="9" font-family="monospace">=</text>
  <text x="240" y="62" fill="#4ade80" font-size="9" font-family="monospace" font-weight="bold">49</text>
  <text x="120" y="82" fill="#ffffff" font-size="9" font-family="monospace">67²</text>
  <text x="180" y="82" fill="#38bdf8" font-size="9" font-family="monospace">=</text>
  <text x="240" y="82" fill="#4ade80" font-size="9" font-family="monospace" font-weight="bold">4489</text>
  <text x="120" y="102" fill="#ffffff" font-size="9" font-family="monospace">667²</text>
  <text x="180" y="102" fill="#38bdf8" font-size="9" font-family="monospace">=</text>
  <text x="240" y="102" fill="#4ade80" font-size="9" font-family="monospace" font-weight="bold">444889</text>
  <text x="120" y="122" fill="#ffffff" font-size="9" font-family="monospace">6667²</text>
  <text x="180" y="122" fill="#38bdf8" font-size="9" font-family="monospace">=</text>
  <text x="240" y="122" fill="#4ade80" font-size="9" font-family="monospace" font-weight="bold">44448889</text>
  <!-- Rule -->
  <text x="200" y="168" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Rule: If there are k sixes, the square has (k + 1) fours, k eights, and ends in 9!</text>
</svg>
</div>
If a number has five 6s followed by a 7 (i.e. \\(666667\\)), how many 4s and 8s will appear in its square?""",
     ["Six 4s and five 8s, ending in 9 (i.e. \\(444444888889\\))",
      "Five 4s and five 8s",
      "Seven 4s and six 8s",
      "Six 4s and six 8s"],
     "A", "OSC", "easy",
     "Following the structural rule: for \\(k\\) digits of 6, the square contains \\((k + 1)\\) fours, \\(k\\) eights, and a final 9. With 5 sixes (\\(k = 5\\)), the square has \\(5 + 1 = 6\\) fours and 5 eights, ending in 9: \\(444444888889\\)."),

    # 78: Non-Zero Difference of Consecutive Squares
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Rapid Difference of Consecutive Squares: a² - b² = a + b (when a - b = 1)</text>
  <!-- Visual Demonstration -->
  <rect x="30" y="45" width="160" height="90" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="110" y="70" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Example 1: 51² - 50²</text>
  <text x="110" y="95" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle">= 51 + 50</text>
  <text x="110" y="120" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">= 101</text>
  <!-- Example 2 -->
  <rect x="210" y="45" width="160" height="90" rx="4" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="290" y="70" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Example 2: 125² - 124²</text>
  <text x="290" y="95" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle">= 125 + 124</text>
  <text x="290" y="120" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">= 249</text>
  <!-- Summary Box -->
  <text x="200" y="165" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Whenever two numbers differ by 1, the difference of their squares is simply their sum!</text>
</svg>
</div>
Using the property \\(a^2 - b^2 = a + b\\) for consecutive integers, what is \\(500^2 - 499^2\\)?""",
     ["\\(999\\) (calculated as \\(500 + 499\\))",
      "\\(1000\\)",
      "\\(1\\)",
      "\\(998\\)"],
     "A", "OSC", "easy",
     "Since \\(500 - 499 = 1\\), \\(500^2 - 499^2 = (500 - 499)(500 + 499) = 1 \\times (500 + 499) = 999\\)."),

    # 79: Square and Sum of First n Cubes Identity
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Nicomachus Theorem: 1³ + 2³ + 3³ + ... + n³ = (1 + 2 + 3 + ... + n)²</text>
  <!-- Calculations -->
  <rect x="30" y="45" width="340" height="100" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="200" y="68" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">n = 1:  1³ = 1 = 1²</text>
  <text x="200" y="88" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">n = 2:  1³ + 2³ = 1 + 8 = 9 = (1 + 2)² = 3²</text>
  <text x="200" y="108" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">n = 3:  1³ + 2³ + 3³ = 1 + 8 + 27 = 36 = (1 + 2 + 3)² = 6²</text>
  <text x="200" y="128" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">n = 4:  1³ + 2³ + 3³ + 4³ = 100 = (1 + 2 + 3 + 4)² = 10²</text>
  <!-- Summary text -->
  <text x="200" y="168" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">The sum of the first n cubes is ALWAYS the square of the n-th triangular number!</text>
</svg>
</div>
What is the value of \\(1^3 + 2^3 + 3^3 + 4^3 + 5^3\\) using Nicomachus's Theorem?""",
     ["\\(225\\) (calculated as \\((1 + 2 + 3 + 4 + 5)^2 = 15^2\\))",
      "\\(150\\)",
      "\\(200\\)",
      "\\(125\\)"],
     "A", "OSC", "easy",
     "According to Nicomachus's theorem, \\(1^3 + 2^3 + \\dots + n^3 = (1 + 2 + \\dots + n)^2\\). For \\(n = 5\\), the base sum is \\(1 + 2 + 3 + 4 + 5 = 15\\). Squaring this gives \\(15^2 = 225\\)."),

    # 80: Generating Pythagorean Triplets from Odd Numbers
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Pythagorean Triplets from Odd Numbers: a, (a² - 1)/2, (a² + 1)/2</text>
  <!-- Example: a = 3 -->
  <rect x="25" y="45" width="105" height="100" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="77" y="65" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">a = 3</text>
  <text x="77" y="85" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">3² = 9</text>
  <text x="77" y="105" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">(9-1)/2 = 4</text>
  <text x="77" y="125" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">(9+1)/2 = 5</text>
  <text x="77" y="140" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">(3, 4, 5)</text>
  <!-- Example: a = 5 -->
  <rect x="145" y="45" width="105" height="100" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="197" y="65" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">a = 5</text>
  <text x="197" y="85" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">5² = 25</text>
  <text x="197" y="105" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">(25-1)/2 = 12</text>
  <text x="197" y="125" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">(25+1)/2 = 13</text>
  <text x="197" y="140" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">(5, 12, 13)</text>
  <!-- Example: a = 7 -->
  <rect x="265" y="45" width="105" height="100" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="317" y="65" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">a = 7</text>
  <text x="317" y="85" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">7² = 49</text>
  <text x="317" y="105" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">(49-1)/2 = 24</text>
  <text x="317" y="125" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">(49+1)/2 = 25</text>
  <text x="317" y="140" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">(7, 24, 25)</text>
  <!-- Summary Box -->
  <text x="200" y="170" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">For any odd number a: square it, then split a² into two consecutive integers!</text>
</svg>
</div>
Using the odd number method shown above, generate the Pythagorean triplet whose smallest odd member is \\(9\\).""",
     ["(9, 40, 41) (since \\(9^2 = 81\\); \\((81-1)/2 = 40\\), \\((81+1)/2 = 41\\))",
      "(9, 36, 45)",
      "(9, 18, 27)",
      "(9, 40, 45)"],
     "A", "OSC", "easy",
     "Square the odd number: \\(9^2 = 81\\). The other two sides are consecutive integers whose sum is 81: \\(\\frac{81 - 1}{2} = 40\\) and \\(\\frac{81 + 1}{2} = 41\\). Checking: \\(9^2 + 40^2 = 81 + 1600 = 1681 = 41^2\\). Thus, the triplet is (9, 40, 41)."),

    # 81: Partitioning Numbers of Consecutive Digits
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Product of Consecutive Numbers: (n - 1)(n + 1) = n² - 1</text>
  <!-- Geometric visual -->
  <rect x="40" y="45" width="140" height="95" rx="5" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="110" y="70" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Case 1: 15 x 17</text>
  <text x="110" y="92" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">= (16 - 1)(16 + 1)</text>
  <text x="110" y="112" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">= 16² - 1 = 256 - 1</text>
  <text x="110" y="132" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">= 255</text>
  <!-- Case 2 -->
  <rect x="220" y="45" width="140" height="95" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="290" y="70" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Case 2: 24 x 26</text>
  <text x="290" y="92" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">= (25 - 1)(25 + 1)</text>
  <text x="290" y="112" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">= 25² - 1 = 625 - 1</text>
  <text x="290" y="132" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">= 624</text>
  <!-- Summary Box -->
  <text x="200" y="168" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Product of two numbers differing by 2 is always ONE LESS than the square of their average!</text>
</svg>
</div>
Using the identity \\((n - 1)(n + 1) = n^2 - 1\\), calculate the product \\(39 \\times 41\\) mentally.""",
     ["\\(1599\\) (calculated as \\(40^2 - 1 = 1600 - 1\\))",
      "\\(1601\\)",
      "\\(1590\\)",
      "\\(1619\\)"],
     "A", "OSC", "easy",
     "The average of 39 and 41 is 40. Applying the difference of squares identity: \\(39 \\times 41 = (40 - 1)(40 + 1) = 40^2 - 1^2 = 1600 - 1 = 1599\\)."),

    # 82: Visualizing Non-Square Gaps Growing by 2: 2, 4, 6, 8, 10
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Evolution of Non-Square Gaps: Growing Linearly as 2n</text>
  <!-- Table Chart -->
  <rect x="25" y="40" width="350" height="105" rx="5" fill="#1e293b" stroke="#4ade80" stroke-width="1.5"/>
  <text x="100" y="60" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Between Squares</text>
  <text x="230" y="60" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Non-Square Numbers</text>
  <text x="330" y="60" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Count (2n)</text>
  <text x="100" y="80" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">1² and 2² (1 to 4)</text>
  <text x="230" y="80" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">2, 3</text>
  <text x="330" y="80" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">2 (2x1)</text>
  <text x="100" y="98" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">2² and 3² (4 to 9)</text>
  <text x="230" y="98" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">5, 6, 7, 8</text>
  <text x="330" y="98" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">4 (2x2)</text>
  <text x="100" y="116" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">3² and 4² (9 to 16)</text>
  <text x="230" y="116" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">10, 11, 12, 13, 14, 15</text>
  <text x="330" y="116" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">6 (2x3)</text>
  <text x="100" y="134" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">4² and 5² (16 to 25)</text>
  <text x="230" y="134" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">17, 18, 19, 20, 21, 22, 23, 24</text>
  <text x="330" y="134" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">8 (2x4)</text>
  <!-- Summary Box -->
  <text x="200" y="170" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">The gap between consecutive squares increases by exactly 2 at each successive step!</text>
</svg>
</div>
How does the count of non-square numbers between successive square numbers change as \\(n\\) increases by 1?""",
     ["The count increases by exactly 2 at each successive step (i.e. \\(2, 4, 6, 8, 10, \\dots, 2n\\))",
      "The count stays constant at 2",
      "The count doubles at each step",
      "The count increases by 1 at each step"],
     "A", "OSC", "easy",
     "Since the number of non-square integers between \\(n^2\\) and \\((n+1)^2\\) is \\(2n\\), when \\(n\\) increases to \\(n+1\\), the new count becomes \\(2(n+1) = 2n + 2\\). The difference is \\((2n + 2) - 2n = 2\\). Thus, each consecutive interval between squares contains exactly 2 more non-square numbers than the previous one.")
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

output_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch1_topic2.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
