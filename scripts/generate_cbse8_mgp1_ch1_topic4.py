# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-1-1.4
Topic: Finding Square Roots by Long Division & Decimals
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-1-1.4"

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
    ("In the long division method for finding square roots of integers, how are bars (periods) placed over the digits?",
     ["Starting from the units place (right to left) in pairs of two digits; the leftmost period may have one or two digits",
      "From left to right in groups of three digits",
      "Only over the first and last digits",
      "From the center outward in pairs"],
     "A", "OSC", "easy",
     "To extract square roots by division, digits of the integer part are grouped into pairs (periods) from right to left starting at the units digit. The leftmost group may contain either 1 or 2 digits."),

    # 2
    ("Find the square root of \\(529\\) using the division method.",
     ["23", "27", "17", "33"],
     "A", "OSC", "easy",
     "Placing bars: \\(\\overline{5}\\ \\overline{29}\\). The largest square \\(\\le 5\\) is \\(2^2 = 4\\). Divisor 2, quotient 2, remainder 1. Bring down 29 to get 129. Double quotient 2 to get 4. Find digit \\(x\\) such that \\(4x \\times x = 129\\); with \\(x = 3\\), \\(43 \\times 3 = 129\\). Remainder is 0. Thus, \\(\\sqrt{529} = 23\\)."),

    # 3
    ("Find the square root of \\(1369\\) using the division method.",
     ["37", "33", "43", "47"],
     "A", "OSC", "easy",
     "Bars: \\(\\overline{13}\\ \\overline{69}\\). The largest square \\(\\le 13\\) is \\(3^2 = 9\\). Quotient = 3, remainder = 4. Bring down 69 to get 469. Double 3 to get 6. Test \\(6x \\times x = 469\\): \\(67 \\times 7 = 469\\). Quotient is 37, so \\(\\sqrt{1369} = 37\\)."),

    # 4
    ("Find the square root of \\(3481\\).",
     ["59", "51", "61", "69"],
     "A", "OSC", "easy",
     "Bars: \\(\\overline{34}\\ \\overline{81}\\). Largest square \\(\\le 34\\) is \\(5^2 = 25\\). Remainder = 9, bring down 81 \\(\\implies 981\\). Double 5 to get 10. \\(109 \\times 9 = 981\\). Quotient = 59, so \\(\\sqrt{3481} = 59\\)."),

    # 5
    ("Find the square root of \\(5776\\).",
     ["76", "74", "84", "86"],
     "A", "OSC", "easy",
     "Bars: \\(\\overline{57}\\ \\overline{76}\\). Largest square \\(\\le 57\\) is \\(7^2 = 49\\). Remainder = 8, bring down 76 \\(\\implies 876\\). Double 7 to get 14. \\(146 \\times 6 = 876\\). Thus, \\(\\sqrt{5776} = 76\\)."),

    # 6
    ("Find the square root of \\(7921\\).",
     ["89", "81", "91", "99"],
     "A", "OSC", "easy",
     "Bars: \\(\\overline{79}\\ \\overline{21}\\). Largest square \\(\\le 79\\) is \\(8^2 = 64\\). Remainder = 15, bring down 21 \\(\\implies 1521\\). Double 8 to get 16. \\(169 \\times 9 = 1521\\). Thus, \\(\\sqrt{7921} = 89\\)."),

    # 7
    ("Find the square root of the decimal number \\(2.56\\).",
     ["1.6", "0.16", "16", "1.4"],
     "A", "OSC", "easy",
     "Write \\(2.56 = \\frac{256}{100}\\). Then \\(\\sqrt{2.56} = \\frac{\\sqrt{256}}{\\sqrt{100}} = \\frac{16}{10} = 1.6\\)."),

    # 8
    ("Find the square root of \\(7.29\\).",
     ["2.7", "0.27", "2.3", "3.3"],
     "A", "OSC", "easy",
     "\\(7.29 = \\frac{729}{100}\\). \\(\\sqrt{729} = 27\\), so \\(\\sqrt{7.29} = \\frac{27}{10} = 2.7\\)."),

    # 9
    ("Find the square root of \\(51.84\\).",
     ["7.2", "7.8", "6.8", "8.2"],
     "A", "OSC", "easy",
     "\\(\\sqrt{51.84} = \\frac{\\sqrt{5184}}{10} = \\frac{72}{10} = 7.2\\)."),

    # 10
    ("Find the square root of \\(42.25\\).",
     ["6.5", "6.25", "7.5", "5.5"],
     "A", "OSC", "easy",
     "Notice \\(42 = 6 \\times 7\\). A number ending in 25 with leading product \\(a(a+1) = 42\\) has square root \\(65\\). Thus, \\(\\sqrt{42.25} = 6.5\\)."),

    # 11
    ("Find the square root of \\(31.36\\).",
     ["5.6", "5.4", "6.4", "4.6"],
     "A", "OSC", "easy",
     "\\(\\sqrt{3136} = 56\\). Dividing by 10 gives \\(\\sqrt{31.36} = 5.6\\)."),

    # 12
    ("Find the least number that must be subtracted from \\(402\\) to get a perfect square.",
     ["2", "3", "4", "1"],
     "A", "OSC", "easy",
     "Performing long division on 402: \\(20^2 = 400 < 402\\). Remainder is \\(402 - 400 = 2\\). Subtracting 2 leaves \\(402 - 2 = 400 = 20^2\\). Thus, the least number to subtract is 2."),

    # 13
    ("Find the least number that must be subtracted from \\(1989\\) so as to get a perfect square.",
     ["53", "45", "50", "39"],
     "A", "OSC", "medium",
     "Testing squares near 1989: \\(44^2 = 1936\\) and \\(45^2 = 2025\\). Long division gives quotient 44 and remainder \\(1989 - 1936 = 53\\). Subtracting 53 gives \\(1989 - 53 = 1936 = 44^2\\)."),

    # 14
    ("Find the least number that must be subtracted from \\(3250\\) to get a perfect square.",
     ["1", "5", "9", "25"],
     "A", "OSC", "easy",
     "\\(57^2 = 3249\\). Comparing with 3250: \\(3250 - 3249 = 1\\). Thus, the least number to subtract is 1."),

    # 15
    ("Find the least number that must be subtracted from \\(825\\) to get a perfect square.",
     ["41", "25", "35", "15"],
     "A", "OSC", "medium",
     "\\(28^2 = 784\\) and \\(29^2 = 841\\). Long division on 825 yields quotient 28 and remainder \\(825 - 784 = 41\\). Subtracting 41 gives \\(825 - 41 = 784 = 28^2\\)."),

    # 16
    ("Find the least number that must be subtracted from \\(4000\\) to get a perfect square.",
     ["31", "35", "25", "41"],
     "A", "OSC", "medium",
     "\\(63^2 = 3969\\) and \\(64^2 = 4096\\). Remainder when dividing 4000 is \\(4000 - 3969 = 31\\). Subtracting 31 leaves \\(3969 = 63^2\\)."),

    # 17
    ("Find the least number that must be added to \\(525\\) so as to get a perfect square.",
     ["4", "5", "9", "15"],
     "A", "OSC", "easy",
     "Testing squares around 525: \\(22^2 = 484 < 525 < 23^2 = 529\\). The next perfect square is \\(23^2 = 529\\). The number to add is \\(529 - 525 = 4\\)."),

    # 18
    ("Find the least number that must be added to \\(1750\\) so as to get a perfect square.",
     ["14", "25", "10", "16"],
     "A", "OSC", "medium",
     "\\(41^2 = 1681 < 1750 < 42^2 = 1764\\). The next perfect square is \\(42^2 = 1764\\). Number to add = \\(1764 - 1750 = 14\\)."),

    # 19
    ("Find the least number that must be added to \\(252\\) so as to get a perfect square.",
     ["37", "4", "13", "25"],
     "A", "OSC", "easy",
     "\\(15^2 = 225 < 252 < 16^2 = 256\\). The next perfect square is \\(16^2 = 256\\). The number to add is \\(256 - 252 = 4\\)."),

    # 20
    ("Find the least number that must be added to \\(1825\\) so as to get a perfect square.",
     ["24", "15", "18", "30"],
     "A", "OSC", "medium",
     "\\(42^2 = 1764 < 1825 < 43^2 = 1849\\). The next square is \\(43^2 = 1849\\). Number to add = \\(1849 - 1825 = 24\\)."),

    # 21
    ("Find the least number that must be added to \\(6412\\) so as to get a perfect square.",
     ["149", "125", "135", "159"],
     "A", "OSC", "medium",
     "\\(80^2 = 6400 < 6412 < 81^2 = 6561\\). Next square is \\(81^2 = 6561\\). Number to add = \\(6561 - 6412 = 149\\)."),

    # 22
    ("Find the greatest 4-digit number which is a perfect square.",
     ["9801", "9900", "9999", "9604"],
     "A", "OSC", "medium",
     "The largest 4-digit number is 9999. Performing division on 9999 gives quotient 99 with remainder 198 (since \\(99^2 = 9801\\) and \\(9999 - 198 = 9801\\)). Thus, 9801 is the greatest 4-digit perfect square."),

    # 23
    ("Find the least 4-digit number which is a perfect square.",
     ["1024", "1000", "1089", "1156"],
     "A", "OSC", "medium",
     "The smallest 4-digit number is 1000. \\(31^2 = 961 < 1000 < 32^2 = 1024\\). The smallest 4-digit square is \\(32^2 = 1024\\)."),

    # 24
    ("Find the greatest 5-digit number which is a perfect square.",
     ["99856", "99999", "99225", "98596"],
     "A", "OSC", "hard",
     "The greatest 5-digit number is 99999. Extracting square root: \\(316^2 = 99856\\) and \\(317^2 = 100489\\) (6 digits). Remainder is \\(99999 - 99856 = 143\\). Subtracting 143 gives 99856, which is \\(316^2\\)."),

    # 25
    ("Find the least 5-digit number which is a perfect square.",
     ["10000", "10201", "10404", "10048"],
     "A", "OSC", "easy",
     "The smallest 5-digit number is 10000. Since \\(100^2 = 10000\\), 10000 is itself a perfect square!"),

    # 26
    ("Find the length of the side of a square whose area is 441 m².",
     ["21 m", "19 m", "23 m", "25 m"],
     "A", "OSC", "easy",
     "\\(\\text{Side} = \\sqrt{441} = 21\\) meters."),

    # 27
    ("In a right-angled triangle ABC, \\(\\angle B = 90^\\circ\\). If \\(AB = 6\\) cm and \\(BC = 8\\) cm, find \\(AC\\).",
     ["10 cm", "12 cm", "14 cm", "9 cm"],
     "A", "OSC", "easy",
     "By Pythagoras theorem, \\(AC^2 = AB^2 + BC^2 = 6^2 + 8^2 = 36 + 64 = 100\\). Thus \\(AC = \\sqrt{100} = 10\\) cm."),

    # 28
    ("In a right-angled triangle ABC, \\(\\angle B = 90^\\circ\\). If \\(AC = 13\\) cm and \\(BC = 5\\) cm, find \\(AB\\).",
     ["12 cm", "11 cm", "10 cm", "8 cm"],
     "A", "OSC", "easy",
     "\\(AB^2 = AC^2 - BC^2 = 13^2 - 5^2 = 169 - 25 = 144\\). Thus \\(AB = \\sqrt{144} = 12\\) cm."),

    # 29
    ("A gardener has 1000 plants. He wants to plant these in such a way that the number of rows and the number of columns remain the same. Find the minimum number of plants he needs more for this.",
     ["24 plants", "20 plants", "30 plants", "14 plants"],
     "A", "OSC", "medium",
     "He needs a square number greater than or equal to 1000. \\(31^2 = 961 < 1000 < 32^2 = 1024\\). The next square is 1024. He needs \\(1024 - 1000 = 24\\) more plants."),

    # 30
    ("There are 500 children in a school. For a P.T. drill they have to stand in such a manner that the number of rows is equal to number of columns. How many children would be left out in this arrangement?",
     ["16 children", "10 children", "20 children", "25 children"],
     "A", "OSC", "medium",
     "\\(22^2 = 484 < 500 < 23^2 = 529\\). The largest square formation that can be arranged from 500 children is \\(22 \\times 22 = 484\\) children. The number of children left out is \\(500 - 484 = 16\\)."),

    # 31
    ("How many bars (periods) will be placed over the number \\(390625\\) to find its square root?",
     ["3 bars", "2 bars", "4 bars", "6 bars"],
     "A", "OSC", "easy",
     "390625 is a 6-digit number. Pairing from right to left: \\(\\overline{39}\\ \\overline{06}\\ \\overline{25}\\). There are 3 bars, so the square root has 3 digits (indeed, \\(\\sqrt{390625} = 625\\))."),

    # 32
    ("How many digits are in the square root of \\(27225\\)?",
     ["3 digits", "2 digits", "4 digits", "5 digits"],
     "A", "OSC", "easy",
     "27225 has 5 digits. Using \\(\\frac{n+1}{2} = \\frac{5+1}{2} = 3\\) digits. (Bars: \\(\\overline{2}\\ \\overline{72}\\ \\overline{25}\\)). Indeed, \\(\\sqrt{27225} = 165\\)."),

    # 33
    ("Estimate the square root of \\(250\\) to the nearest whole number.",
     ["16", "15", "17", "14"],
     "A", "OSC", "medium",
     "\\(15^2 = 225\\) and \\(16^2 = 256\\). The distance from 250 to 225 is 25, while the distance from 250 to 256 is only 6. Since 250 is much closer to 256, \\(\\sqrt{250} \\approx 16\\)."),

    # 34
    ("Estimate the square root of \\(80\\) to the nearest integer.",
     ["9", "8", "10", "7"],
     "A", "OSC", "easy",
     "\\(8^2 = 64\\) and \\(9^2 = 81\\). 80 is only 1 away from 81 (9²). Thus, \\(\\sqrt{80} \\approx 9\\)."),

    # 35
    ("Estimate the square root of \\(1000\\) to the nearest integer.",
     ["32", "31", "30", "33"],
     "A", "OSC", "medium",
     "\\(31^2 = 961\\) (diff = 39) and \\(32^2 = 1024\\) (diff = 24). Since 1000 is closer to 1024, \\(\\sqrt{1000} \\approx 32\\)."),

    # 36
    ("Estimate the square root of \\(500\\) to the nearest integer.",
     ["22", "23", "21", "24"],
     "A", "OSC", "medium",
     "\\(22^2 = 484\\) (diff = 16) and \\(23^2 = 529\\) (diff = 29). 500 is closer to 484. Thus, \\(\\sqrt{500} \\approx 22\\)."),

    # 37
    ("What is the square root of \\(0.0064\\)?",
     ["0.08", "0.8", "0.008", "0.04"],
     "A", "OSC", "easy",
     "\\(0.0064 = \\frac{64}{10000}\\). \\(\\sqrt{0.0064} = \\frac{\\sqrt{64}}{\\sqrt{10000}} = \\frac{8}{100} = 0.08\\)."),

    # 38
    ("What is the square root of \\(0.000169\\)?",
     ["0.013", "0.13", "0.0013", "0.017"],
     "A", "OSC", "easy",
     "6 decimal places in the square \\(\\implies 6 / 2 = 3\\) decimal places in the square root. Since \\(\\sqrt{169} = 13\\), \\(\\sqrt{0.000169} = 0.013\\)."),

    # 39
    ("What is the square root of \\(0.000001\\)?",
     ["0.001", "0.01", "0.0001", "0.1"],
     "A", "OSC", "easy",
     "6 decimal places divided by 2 = 3 decimal places: \\(0.001\\). Indeed, \\((0.001)^2 = 0.000001\\)."),

    # 40
    ("What is the square root of \\(1.44\\)?",
     ["1.2", "0.12", "12", "1.4"],
     "A", "OSC", "easy",
     "\\(1.44 = \\frac{144}{100}\\). \\(\\sqrt{1.44} = \\frac{12}{10} = 1.2\\).")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    ("Find the square root of \\(7396\\) by the division method.",
     ["86", "84", "94", "96"],
     "A", "OSC", "medium",
     "Bars: \\(\\overline{73}\\ \\overline{96}\\). \\(8^2 = 64 \\le 73\\), rem = 9, bring down 96 \\(\\implies 996\\). Double 8 to get 16. Test \\(166 \\times 6 = 996\\). Thus, \\(\\sqrt{7396} = 86\\)."),

    # 42
    ("Find the square root of \\(8649\\).",
     ["93", "97", "83", "87"],
     "A", "OSC", "medium",
     "Bars: \\(\\overline{86}\\ \\overline{49}\\). \\(9^2 = 81\\), rem = 5, bring down 49 \\(\\implies 549\\). Double 9 to get 18. \\(183 \\times 3 = 549\\). Thus, \\(\\sqrt{8649} = 93\\)."),

    # 43
    ("Find the square root of \\(10609\\).",
     ["103", "107", "93", "97"],
     "A", "OSC", "medium",
     "Bars: \\(\\overline{1}\\ \\overline{06}\\ \\overline{09}\\). 1st digit: 1, rem = 0. Bring down 06. Double 1 gives 2. \\(20 \\times 0 = 0\\), rem = 6. Bring down 09 \\(\\implies 609\\). Double 10 to get 20. \\(203 \\times 3 = 609\\). Thus, \\(\\sqrt{10609} = 103\\)."),

    # 44
    ("Find the square root of \\(11449\\).",
     ["107", "103", "117", "97"],
     "A", "OSC", "medium",
     "Bars: \\(\\overline{1}\\ \\overline{14}\\ \\overline{49}\\). Digits are 1, 0, 7. \\(107^2 = 11449\\)."),

    # 45
    ("Find the square root of \\(9.61\\).",
     ["3.1", "3.9", "2.9", "3.01"],
     "A", "OSC", "easy",
     "\\(9.61 = \\frac{961}{100}\\). Since \\(\\sqrt{961} = 31\\), \\(\\sqrt{9.61} = 3.1\\)."),

    # 46
    ("Find the square root of \\(0.0081\\).",
     ["0.09", "0.9", "0.009", "0.03"],
     "A", "OSC", "easy",
     "\\(\\sqrt{\\frac{81}{10000}} = \\frac{9}{100} = 0.09\\)."),

    # 47
    ("Find the square root of \\(0.0121\\).",
     ["0.11", "0.011", "1.1", "0.0121"],
     "A", "OSC", "easy",
     "\\(\\sqrt{121 / 10000} = 11 / 100 = 0.11\\)."),

    # 48
    ("Find the least number to subtract from \\(1300\\) to get a perfect square.",
     ["4", "9", "16", "25"],
     "A", "OSC", "medium",
     "\\(36^2 = 1296\\) and \\(37^2 = 1369\\). \\(1300 - 1296 = 4\\). So subtract 4."),

    # 49
    ("Find the least number to subtract from \\(194491\\) to get a perfect square.",
     ["10", "15", "5", "1"],
     "A", "OSC", "hard",
     "\\(441^2 = 194481\\). \\(194491 - 194481 = 10\\). Thus, 10 must be subtracted."),

    # 50
    ("Find the least number to add to \\(1000\\) to get a perfect square.",
     ["24", "25", "30", "15"],
     "A", "OSC", "easy",
     "\\(31^2 = 961 < 1000 < 32^2 = 1024\\). Number to add = \\(1024 - 1000 = 24\\)."),

    # 51
    ("Find the least number to add to \\(4000\\) to get a perfect square.",
     ["96", "95", "100", "85"],
     "A", "OSC", "medium",
     "\\(63^2 = 3969 < 4000 < 64^2 = 4096\\). Number to add = \\(4096 - 4000 = 96\\)."),

    # 52
    ("Find the least number to add to \\(8400\\) to get a perfect square.",
     ["64", "60", "74", "84"],
     "A", "OSC", "medium",
     "\\(91^2 = 8281 < 8400 < 92^2 = 8464\\). Number to add = \\(8464 - 8400 = 64\\)."),

    # 53
    ("Estimate \\(\\sqrt{350}\\) to the nearest integer.",
     ["19", "18", "20", "17"],
     "A", "OSC", "medium",
     "\\(18^2 = 324\\) and \\(19^2 = 361\\). \\(350 - 324 = 26\\), while \\(361 - 350 = 11\\). Closer to 361, so \\(\\sqrt{350} \\approx 19\\)."),

    # 54
    ("Estimate \\(\\sqrt{150}\\) to the nearest integer.",
     ["12", "13", "11", "14"],
     "A", "OSC", "easy",
     "\\(12^2 = 144\\) (diff 6) and \\(13^2 = 169\\) (diff 19). Closer to 144, so \\(\\approx 12\\)."),

    # 55
    ("Estimate \\(\\sqrt{600}\\) to the nearest integer.",
     ["24", "25", "23", "26"],
     "A", "OSC", "medium",
     "\\(24^2 = 576\\) (diff 24) and \\(25^2 = 625\\) (diff 25). 576 is slightly closer (24 vs 25), so \\(\\approx 24\\)."),

    # 56
    ("What is \\(\\sqrt{0.0009}\\)?",
     ["0.03", "0.3", "0.003", "0.0003"],
     "A", "OSC", "easy",
     "\\(\\sqrt{9 / 10000} = 3 / 100 = 0.03\\)."),

    # 57
    ("What is \\(\\sqrt{0.000025}\\)?",
     ["0.005", "0.05", "0.0005", "0.5"],
     "A", "OSC", "easy",
     "6 decimal places \\(\\implies 6 / 2 = 3\\) decimal places: \\(0.005\\)."),

    # 58
    ("What is \\(\\sqrt{0.000081}\\)?",
     ["0.009", "0.09", "0.0009", "0.9"],
     "A", "OSC", "easy",
     "\\(\\sqrt{81 / 10^6} = 9 / 10^3 = 0.009\\)."),

    # 59
    ("What is \\(\\sqrt{0.00000049}\\)?",
     ["0.0007", "0.007", "0.07", "0.00007"],
     "A", "OSC", "medium",
     "8 decimal places \\(\\implies 8 / 2 = 4\\) decimal places: \\(0.0007\\)."),

    # 60
    ("What is \\(\\sqrt{0.00000001}\\)?",
     ["0.0001", "0.001", "0.01", "0.00001"],
     "A", "OSC", "medium",
     "8 decimal places \\(\\implies 8 / 2 = 4\\) decimal places: \\(0.0001\\)."),

    # 61
    ("Find the perimeter of a square field of area 2025 m².",
     ["180 m", "90 m", "45 m", "200 m"],
     "A", "OSC", "easy",
     "Side = \\(\\sqrt{2025} = 45\\) m. Perimeter = \\(4 \\times 45 = 180\\) m."),

    # 62
    ("Find the perimeter of a square park of area 6084 m².",
     ["312 m", "78 m", "156 m", "320 m"],
     "A", "OSC", "medium",
     "Side = \\(\\sqrt{6084} = 78\\) m. Perimeter = \\(4 \\times 78 = 312\\) m."),

    # 63
    ("Find the side of a square carrom board whose area is 841 cm².",
     ["29 cm", "27 cm", "31 cm", "21 cm"],
     "A", "OSC", "easy",
     "Side = \\(\\sqrt{841} = 29\\) cm."),

    # 64
    ("Find the side of a square chess board whose area is 576 cm².",
     ["24 cm", "26 cm", "22 cm", "28 cm"],
     "A", "OSC", "easy",
     "Side = \\(\\sqrt{576} = 24\\) cm."),

    # 65
    ("What is the value of \\(\\sqrt{10.24}\\)?",
     ["3.2", "3.8", "2.8", "3.02"],
     "A", "OSC", "easy",
     "\\(10.24 = 1024 / 100\\). \\(\\sqrt{1024} = 32\\), so \\(32 / 10 = 3.2\\)."),

    # 66
    ("What is the value of \\(\\sqrt{12.96}\\)?",
     ["3.6", "3.4", "4.6", "3.16"],
     "A", "OSC", "easy",
     "\\(\\sqrt{1296} = 36\\), so \\(\\sqrt{12.96} = 3.6\\)."),

    # 67
    ("What is the value of \\(\\sqrt{17.64}\\)?",
     ["4.2", "4.4", "4.8", "3.8"],
     "A", "OSC", "easy",
     "\\(\\sqrt{1764} = 42\\), so \\(\\sqrt{17.64} = 4.2\\)."),

    # 68
    ("What is the value of \\(\\sqrt{23.04}\\)?",
     ["4.8", "4.2", "5.2", "4.6"],
     "A", "OSC", "easy",
     "\\(\\sqrt{2304} = 48\\), so \\(\\sqrt{23.04} = 4.8\\)."),

    # 69
    ("What is the value of \\(\\sqrt{54.76}\\)?",
     ["7.4", "7.6", "6.4", "8.4"],
     "A", "OSC", "easy",
     "\\(\\sqrt{5476} = 74\\), so \\(\\sqrt{54.76} = 7.4\\)."),

    # 70
    ("What is the value of \\(\\sqrt{70.56}\\)?",
     ["8.4", "8.6", "7.4", "8.2"],
     "A", "OSC", "easy",
     "\\(\\sqrt{7056} = 84\\), so \\(\\sqrt{70.56} = 8.4\\).")
]

# 12 MOCK / FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71: Long Division Pairing and Period Bars Diagram
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Bar Placement (Periods) for Long Division</text>
  <!-- Integer Example: 7396 -->
  <rect x="25" y="45" width="165" height="105" rx="5" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="107" y="65" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">INTEGER: 7396</text>
  <!-- Bars above 73 and 96 -->
  <line x1="75" y1="85" x2="105" y2="85" stroke="#4ade80" stroke-width="3"/>
  <line x1="110" y1="85" x2="140" y2="85" stroke="#4ade80" stroke-width="3"/>
  <text x="90" y="105" fill="#ffffff" font-size="12" font-family="monospace">73</text>
  <text x="125" y="105" fill="#ffffff" font-size="12" font-family="monospace">96</text>
  <text x="107" y="130" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">Pairs from Right to Left</text>
  <!-- Decimal Example: 17.64 -->
  <rect x="210" y="45" width="165" height="105" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="292" y="65" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">DECIMAL: 17.64</text>
  <!-- Bars: Leftward for int, Rightward for dec -->
  <line x1="260" y1="85" x2="285" y2="85" stroke="#facc15" stroke-width="3"/>
  <line x1="300" y1="85" x2="325" y2="85" stroke="#facc15" stroke-width="3"/>
  <text x="272" y="105" fill="#ffffff" font-size="12" font-family="monospace">17</text>
  <text x="292" y="105" fill="#facc15" font-size="12" font-family="monospace">.</text>
  <text x="312" y="105" fill="#ffffff" font-size="12" font-family="monospace">64</text>
  <text x="292" y="130" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Decimals pair Left to Right!</text>
  <!-- Footer Note -->
  <text x="200" y="175" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Integral part pairs $\leftarrow$ from units; Decimal part pairs $\rightarrow$ from decimal point!</text>
</svg>
</div>
Why must the decimal part of a number be paired from left to right (from the decimal point outward) rather than right to left?""",
     ["Because place values after the decimal point descend to the right (tenths, hundredths); pairing must preserve the correct power-of-10 positional weighting",
      "Because decimal points can only move backward",
      "Because decimals do not follow math rules",
      "Because right to left pairing is illegal in algebra"],
     "A", "OSC", "easy",
     "In decimals, the first period after the decimal point corresponds to hundredths (\\(10^{-2}\\)), the second to ten-thousandths (\\(10^{-4}\\)), etc. Pairing rightwards from the decimal point ensures that each period corresponds to an exact power of \\(10^{-2k}\\), whose square root has \\(10^{-k}\\)."),

    # 72: Long Division Step-by-Step Layout Box
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Division Bracket Frame -->
  <text x="140" y="35" fill="#4ade80" font-size="12" font-family="monospace" font-weight="bold">Quotient: 2 3</text>
  <line x1="70" y1="45" x2="220" y2="45" stroke="#64748b" stroke-width="2"/>
  <line x1="70" y1="45" x2="70" y2="155" stroke="#64748b" stroke-width="2"/>
  <!-- Stepped Work inside bracket -->
  <text x="45" y="70" fill="#38bdf8" font-size="10" font-family="monospace">2</text>
  <text x="90" y="70" fill="#ffffff" font-size="11" font-family="monospace">5 29</text>
  <text x="90" y="90" fill="#ef4444" font-size="11" font-family="monospace">-4</text>
  <line x1="85" y1="95" x2="160" y2="95" stroke="#64748b" stroke-width="1"/>
  <!-- Second stage -->
  <text x="35" y="115" fill="#facc15" font-size="10" font-family="monospace">43</text>
  <text x="90" y="115" fill="#ffffff" font-size="11" font-family="monospace">1 29</text>
  <text x="90" y="135" fill="#ef4444" font-size="11" font-family="monospace">-1 29</text>
  <line x1="85" y1="140" x2="160" y2="140" stroke="#64748b" stroke-width="1"/>
  <text x="120" y="155" fill="#4ade80" font-size="11" font-family="monospace" font-weight="bold">0</text>
  <!-- Explanation Panel on Right -->
  <rect x="235" y="45" width="145" height="110" rx="5" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="307" y="68" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Stage 2 Trial Divisor:</text>
  <text x="307" y="88" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Double quotient 2 -> 4</text>
  <text x="307" y="106" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Find x: 4x · x ≤ 129</text>
  <text x="307" y="126" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">43 · 3 = 129 (Exact!)</text>
  <text x="307" y="145" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">√529 = 23</text>
</svg>
</div>
In the long division layout above, how was the new divisor \\(43\\) in the second stage constructed?""",
     ["The previous quotient digit 2 was doubled to form the tens digit (4), and the units digit 3 was chosen so that \\(43 \\times 3 = 129\\)",
      "By adding 40 and 3 together arbitrarily",
      "By multiplying 2 by 21.5",
      "By guessing numbers randomly"],
     "A", "OSC", "easy",
     "In the square root division algorithm, the trial divisor at each step is formed by doubling the entire quotient obtained so far (\\(2 \\times 2 = 4\\)) to form the leading digits, and finding the largest unit digit \\(x\\) such that \\((40 + x) \\times x \\le 129\\). Since \\(43 \\times 3 = 129\\), \\(x = 3\\)."),

    # 73: Subtract vs Add to Make Perfect Square
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="22" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Number to Subtract vs Number to Add: N = 1000</text>
  <!-- Number Line Representation -->
  <line x1="40" y1="80" x2="360" y2="80" stroke="#64748b" stroke-width="2"/>
  <!-- Lower Square: 31² = 961 -->
  <circle cx="80" cy="80" r="5" fill="#38bdf8"/>
  <text x="80" y="105" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">31² = 961</text>
  <!-- Given Number: 1000 -->
  <circle cx="180" cy="80" r="7" fill="#ef4444"/>
  <text x="180" y="65" fill="#ef4444" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">N = 1000</text>
  <!-- Higher Square: 32² = 1024 -->
  <circle cx="300" cy="80" r="5" fill="#4ade80"/>
  <text x="300" y="105" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">32² = 1024</text>
  <!-- Subtract Arrow (Leftward) -->
  <path d="M 175 70 Q 130 40 85 70" stroke="#facc15" stroke-width="2" fill="none"/>
  <text x="130" y="42" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">SUBTRACT: 1000 - 961 = 39</text>
  <!-- Add Arrow (Rightward) -->
  <path d="M 185 70 Q 240 40 295 70" stroke="#4ade80" stroke-width="2" fill="none"/>
  <text x="240" y="42" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">ADD: 1024 - 1000 = 24</text>
  <!-- Summary Box -->
  <rect x="30" y="125" width="340" height="55" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="200" y="145" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">To get previous square (961): SUBTRACT remainder = 39</text>
  <text x="200" y="165" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">To get next square (1024): ADD difference to (q+1)² = 24</text>
</svg>
</div>
For the number \\(1000\\), what is the fundamental difference between the 'least number to subtract' and the 'least number to add' to obtain a perfect square?""",
     ["Subtracting removes the remainder to reach the lower square \\(31^2 = 961\\) (subtract 39), whereas adding bridges the gap to reach the next higher square \\(32^2 = 1024\\) (add 24)",
      "They are always the exact same number",
      "Subtracting always yields a negative number",
      "Adding is only possible for odd numbers"],
     "A", "OSC", "easy",
     "Since \\(31^2 = 961 < 1000 < 32^2 = 1024\\), 1000 lies between two consecutive squares. To make 1000 a square by subtraction, we subtract the excess remainder: \\(1000 - 961 = 39\\). To make it a square by addition, we add the deficit to the next integer square: \\(1024 - 1000 = 24\\)."),

    # 74: Estimating Square Roots using Neighboring Squares
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Square Root Estimation: √250 to Nearest Whole Number</text>
  <!-- Number Line -->
  <line x1="40" y1="90" x2="360" y2="90" stroke="#64748b" stroke-width="2"/>
  <!-- 15² = 225 -->
  <circle cx="80" cy="90" r="6" fill="#38bdf8"/>
  <text x="80" y="115" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">15² = 225</text>
  <!-- 250 -->
  <circle cx="280" cy="90" r="7" fill="#facc15"/>
  <text x="280" y="70" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">250</text>
  <!-- 16² = 256 -->
  <circle cx="320" cy="90" r="6" fill="#4ade80"/>
  <text x="320" y="115" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">16² = 256</text>
  <!-- Distances -->
  <text x="180" y="80" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Distance = 25</text>
  <text x="300" y="80" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Diff = 6!</text>
  <!-- Summary Box -->
  <rect x="30" y="135" width="340" height="40" rx="4" fill="#0f172a" stroke="#4ade80" stroke-width="1.5"/>
  <text x="200" y="158" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Since 250 is much closer to 256 than to 225: √250 ≈ 16</text>
</svg>
</div>
How does comparing the numerical distances from \\(250\\) to the neighboring squares \\(225\\) and \\(256\\) estimate \\(\\sqrt{250}\\)?""",
     ["\\(|250 - 256| = 6\\) while \\(|250 - 225| = 25\\); because 250 is significantly closer to \\(16^2 = 256\\), \\(\\sqrt{250}\\) rounds to 16",
      "By calculating the average of 15 and 16",
      "Because 250 ends in 0",
      "Because 250 is divisible by 5"],
     "A", "OSC", "easy",
     "\\(15^2 = 225\\) and \\(16^2 = 256\\). The gap from 250 to 225 is 25, while the gap from 250 to 256 is only 6. Since 250 is much closer to 256, its square root is closer to 16 than to 15, so \\(\\sqrt{250} \\approx 16\\)."),

    # 75: Greatest 4-digit Square Derivation
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Deriving the Greatest 4-Digit Perfect Square</text>
  <!-- Step Boxes -->
  <rect x="25" y="45" width="105" height="100" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="77" y="65" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">STARTING POINT</text>
  <text x="77" y="85" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Largest 4-digit</text>
  <text x="77" y="100" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">number is:</text>
  <text x="77" y="125" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">9999</text>
  <!-- Long Division Step -->
  <rect x="145" y="45" width="110" height="100" rx="4" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="200" y="65" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">LONG DIVISION</text>
  <text x="200" y="85" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Quotient = 99</text>
  <text x="200" y="105" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">99² = 9801</text>
  <text x="200" y="125" fill="#ef4444" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Remainder = 198</text>
  <!-- Result -->
  <rect x="265" y="45" width="110" height="100" rx="4" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="320" y="65" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">SUBTRACT EXCESS</text>
  <text x="320" y="85" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">9999 - 198</text>
  <text x="320" y="110" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">9801</text>
  <text x="320" y="130" fill="#86efac" font-size="7" font-family="sans-serif" text-anchor="middle">= 99² (Exact!)</text>
  <!-- Footer Note -->
  <text x="200" y="170" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">9801 is the largest 4-digit square; the next square 100² = 10000 has 5 digits!</text>
</svg>
</div>
Why is \\(9801\\) the greatest 4-digit perfect square?""",
     ["Because \\(99^2 = 9801\\), and the very next square \\(100^2 = 10000\\) is a 5-digit number",
      "Because 9801 is the largest number ending in 1",
      "Because 9801 is divisible by 9",
      "Because 9999 divided by 2 gives 9801"],
     "A", "OSC", "easy",
     "The largest 2-digit integer is 99, whose square is \\(99^2 = 9801\\) (a 4-digit number). The next integer is 100, whose square is \\(100^2 = 10000\\) (a 5-digit number). Therefore, 9801 is the greatest 4-digit square."),

    # 76: Least 4-digit Square Derivation
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Deriving the Least 4-Digit Perfect Square</text>
  <!-- Step 1: Smallest 4-digit number -->
  <rect x="25" y="45" width="105" height="100" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="77" y="65" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">SMALLEST 4-DIGIT</text>
  <text x="77" y="90" fill="#ffffff" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">1000</text>
  <text x="77" y="115" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Not a square (3 zeros)</text>
  <!-- Step 2: Bracket Between Consecutive Squares -->
  <rect x="145" y="45" width="110" height="100" rx="4" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="200" y="65" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">BRACKETING</text>
  <text x="200" y="85" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">31² = 961 (3 digits)</text>
  <text x="200" y="105" fill="#ef4444" font-size="8" font-family="sans-serif" text-anchor="middle">961 &lt; 1000 &lt; 32²</text>
  <text x="200" y="125" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">Next square = 32²</text>
  <!-- Step 3: Result -->
  <rect x="265" y="45" width="110" height="100" rx="4" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="320" y="65" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">LEAST 4-DIGIT</text>
  <text x="320" y="90" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">1024</text>
  <text x="320" y="112" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">= 32²</text>
  <text x="320" y="130" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Add 1024 - 1000 = 24</text>
  <!-- Footer Note -->
  <text x="200" y="170" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">1024 is the smallest 4-digit square; the preceding square 31² = 961 has only 3 digits!</text>
</svg>
</div>
Why is \\(1024\\) the least 4-digit number that is a perfect square?""",
     ["Because \\(31^2 = 961\\) has only 3 digits, while the next consecutive square \\(32^2 = 1024\\) is the first to reach 4 digits",
      "Because 1024 is divisible by 2",
      "Because 1024 ends in 4",
      "Because 1000 is divisible by 32"],
     "A", "OSC", "easy",
     "The smallest 4-digit number is 1000. Testing integer squares: \\(31^2 = 961\\) (3 digits) and \\(32^2 = 1024\\) (4 digits). Therefore, 1024 is the first and least 4-digit square."),

    # 77: Number of Digits in √N from Bars Formula
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Formula for Digits in Square Root: n/2 vs (n + 1)/2</text>
  <!-- Even n (Left) -->
  <rect x="30" y="45" width="160" height="95" rx="5" fill="#1e293b" stroke="#4ade80" stroke-width="1.5"/>
  <text x="110" y="68" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">IF n IS EVEN</text>
  <text x="110" y="90" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">Digits in √N = n / 2</text>
  <text x="110" y="112" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Example: 4-digit number (1764)</text>
  <text x="110" y="128" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">4 / 2 = 2 digits (42)</text>
  <!-- Odd n (Right) -->
  <rect x="210" y="45" width="160" height="95" rx="5" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
  <text x="290" y="68" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">IF n IS ODD</text>
  <text x="290" y="90" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">Digits in √N = (n + 1) / 2</text>
  <text x="290" y="112" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Example: 5-digit number (14400)</text>
  <text x="290" y="128" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">(5 + 1)/2 = 3 digits (120)</text>
  <!-- Footer Note -->
  <text x="200" y="165" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">The number of digits in √N exactly equals the number of periods (bars) placed over N!</text>
</svg>
</div>
Without computing the square root, how many digits are present in \\(\\sqrt{1048576}\\) (a 7-digit number)?""",
     ["\\(4\\) digits (calculated as \\((7 + 1) / 2 = 4\\))",
      "\\(3\\) digits",
      "\\(5\\) digits",
      "\\(7\\) digits"],
     "A", "OSC", "easy",
     "For an odd number of digits \\(n = 7\\), the number of digits in its square root is \\(\\frac{n + 1}{2} = \\frac{7 + 1}{2} = 4\\). (Indeed, \\(\\sqrt{1048576} = 1024\\), which has 4 digits)."),

    # 78: Decimal Square Root Halving Property
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Decimal Place Halving Theorem</text>
  <!-- Flow Diagram -->
  <rect x="30" y="50" width="130" height="75" rx="5" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="95" y="75" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Square Number N</text>
  <text x="95" y="98" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">2k decimal places</text>
  <!-- Arrow -->
  <line x1="165" y1="87" x2="235" y2="87" stroke="#4ade80" stroke-width="2.5"/>
  <polygon points="235,87 225,82 225,92" fill="#4ade80"/>
  <text x="200" y="78" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">Square Root</text>
  <!-- Root Box -->
  <rect x="240" y="50" width="130" height="75" rx="5" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="305" y="75" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Square Root √N</text>
  <text x="305" y="98" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">k decimal places</text>
  <!-- Summary Box -->
  <text x="200" y="160" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Example: 0.000144 (6 places) -> √0.000144 = 0.012 (3 places!)</text>
</svg>
</div>
If a number has an odd number of decimal places (e.g. \\(0.4\\)), why must a trailing zero be appended (\\(0.40\\)) before extracting its square root?""",
     ["Because digits after the decimal point must be paired in complete periods of 2 digits (hundredths, ten-thousandths); \\(0.40\\) creates the complete period 40",
      "Because 0 makes the number smaller",
      "Because square roots cannot process the digit 4",
      "Because calculators require two zeros"],
     "A", "OSC", "easy",
     "Every period after the decimal represents \\(10^{-2k}\\). A single decimal digit like \\(0.4\\) represents \\(4/10\\), whose denominator is not a square. Writing \\(0.40 = 40/100\\) gives an exact square denominator (100), enabling valid long division."),

    # 79: P.T. Drill Children Left Out Word Problem Setup
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">P.T. Drill Problem: 500 Students into Equal Rows & Columns</text>
  <!-- Square Formation Grid (22 x 22) -->
  <rect x="50" y="45" width="95" height="95" rx="5" fill="#1e3a8a" stroke="#38bdf8" stroke-width="2"/>
  <text x="97" y="90" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">22 x 22 Square</text>
  <text x="97" y="110" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">= 484 Students</text>
  <!-- Leftover Students Box -->
  <rect x="180" y="65" width="180" height="60" rx="4" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
  <text x="270" y="88" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">LEFTOVER STUDENTS</text>
  <text x="270" y="108" fill="#ef4444" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">500 - 484 = 16 Students</text>
  <!-- Summary Box -->
  <text x="200" y="165" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Students left out = Remainder from square root division of 500!</text>
</svg>
</div>
In a school P.T. drill with 500 students arranged in a square, why are exactly 16 students left out?""",
     ["The largest integer whose square is less than or equal to 500 is 22 (\\(22^2 = 484\\)); the remaining \\(500 - 484 = 16\\) students cannot fit into the square",
      "Because 16 is divisible by 4",
      "Because 500 students cannot stand in rows",
      "Because 22 students were absent"],
     "A", "OSC", "easy",
     "A square formation requires an equal number of rows and columns (\\(n \\times n = n^2\\)). The largest square \\(\\le 500\\) is \\(22^2 = 484\\). Therefore, 484 students form the square, leaving \\(500 - 484 = 16\\) students out."),

    # 80: Gardener Plants Needed Word Problem Setup
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Gardener Problem: 1000 Plants (Need Next Higher Square)</text>
  <!-- Current: 1000 -->
  <rect x="30" y="50" width="100" height="75" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="80" y="75" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">CURRENT PLANTS</text>
  <text x="80" y="100" fill="#ffffff" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">1000</text>
  <!-- Next Square: 1024 -->
  <rect x="270" y="50" width="100" height="75" rx="5" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="320" y="75" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">TARGET SQUARE</text>
  <text x="320" y="100" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">32² = 1024</text>
  <!-- Difference Arrow -->
  <line x1="135" y1="87" x2="265" y2="87" stroke="#facc15" stroke-width="2.5"/>
  <polygon points="265,87 255,82 255,92" fill="#facc15"/>
  <text x="200" y="78" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">NEED MORE:</text>
  <text x="200" y="105" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">1024 - 1000 = 24</text>
  <!-- Summary Box -->
  <text x="200" y="160" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">To complete the 32 x 32 square, the gardener must acquire exactly 24 additional plants!</text>
</svg>
</div>
Why does the gardener who has 1000 plants need exactly 24 more plants to make equal rows and columns?""",
     ["Because \\(31^2 = 961 < 1000 < 32^2 = 1024\\); to form the next complete square without discarding any plants, he must reach \\(32^2 = 1024\\), requiring \\(1024 - 1000 = 24\\) more plants",
      "Because 1000 is not divisible by 24",
      "Because 24 is a lucky gardening number",
      "Because each row must have 24 plants"],
     "A", "OSC", "easy",
     "Since the gardener wants to plant all 1000 plants plus additional ones, the final total must be the smallest perfect square greater than 1000. \\(31^2 = 961\\) and \\(32^2 = 1024\\). To reach 1024, he must buy \\(1024 - 1000 = 24\\) more plants."),

    # 81: Area to Side of Square Formula: Side = √Area
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Inverting Area to Find Side & Perimeter of Square Field</text>
  <!-- Square Field Graphic -->
  <rect x="50" y="45" width="90" height="90" rx="4" fill="#1e3a8a" stroke="#38bdf8" stroke-width="2"/>
  <text x="95" y="85" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Area = s²</text>
  <text x="95" y="105" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">= 441 m²</text>
  <text x="95" y="150" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle">side s</text>
  <!-- Side & Perimeter Calculations -->
  <rect x="180" y="45" width="190" height="90" rx="5" fill="#0f172a" stroke="#4ade80" stroke-width="1.5"/>
  <text x="275" y="68" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Two-Step Solution:</text>
  <text x="275" y="90" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Step 1: side s = √441 = 21 m</text>
  <text x="275" y="112" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Step 2: Perimeter = 4 x s</text>
  <text x="275" y="128" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">= 4 x 21 = 84 meters</text>
</svg>
</div>
What is the perimeter of a square plot whose area is \\(441\\text{ m}^2\\)?""",
     ["\\(84\\text{ m}\\) (calculated as \\(\\text{side} = \\sqrt{441} = 21\\text{ m}\\); \\(\\text{Perimeter} = 4 \\times 21 = 84\\text{ m}\\))",
      "\\(42\\text{ m}\\)",
      "\\(21\\text{ m}\\)",
      "\\(105\\text{ m}\\)"],
     "A", "OSC", "easy",
     "Area of a square is \\(s^2\\). Given \\(s^2 = 441\\text{ m}^2\\), the side length is \\(s = \\sqrt{441} = 21\\text{ m}\\). The perimeter of a square is the sum of its 4 equal sides: \\(P = 4s = 4 \\times 21 = 84\\text{ m}\\)."),

    # 82: Pythagoras Theorem Diagonal Application: d = √(s² + s²) = s√2
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Pythagoras Application: Diagonal of a Rectangle / Right Triangle</text>
  <!-- Right Triangle: 6 cm, 8 cm, Hypotenuse 10 cm -->
  <polygon points="60,140 180,140 180,60" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <rect x="168" y="128" width="12" height="12" fill="none" stroke="#facc15" stroke-width="1.5"/>
  <text x="120" y="155" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Base = 8 cm</text>
  <text x="200" y="105" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Height = 6 cm</text>
  <text x="105" y="90" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Hypotenuse = d</text>
  <!-- Formula Details on Right -->
  <rect x="235" y="45" width="140" height="95" rx="5" fill="#0f172a" stroke="#4ade80" stroke-width="1.5"/>
  <text x="305" y="68" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Pythagoras Formula:</text>
  <text x="305" y="90" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">d² = 6² + 8² = 36 + 64</text>
  <text x="305" y="108" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle">d² = 100</text>
  <text x="305" y="130" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">d = √100 = 10 cm</text>
</svg>
</div>
In a right-angled triangle with perpendicular legs of lengths \\(6\\text{ cm}\\) and \\(8\\text{ cm}\\), what is the length of the hypotenuse?""",
     ["\\(10\\text{ cm}\\) (calculated as \\(\\sqrt{6^2 + 8^2} = \\sqrt{36 + 64} = \\sqrt{100} = 10\\text{ cm}\\))",
      "\\(14\\text{ cm}\\)",
      "\\(12\\text{ cm}\\)",
      "\\(9\\text{ cm}\\)"],
     "A", "OSC", "easy",
     "By Pythagoras theorem, \\(c^2 = a^2 + b^2\\). Substituting the leg lengths gives \\(c^2 = 6^2 + 8^2 = 36 + 64 = 100\\). Taking the square root yields \\(c = \\sqrt{100} = 10\\text{ cm}\\).")
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

output_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch1_topic4.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
