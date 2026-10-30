# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 3: Arithmetic Progression - Topic 3.2: nth Term of an AP Formula (MH-10-MTH1-3-3.2)
Total: 82 Canonical Questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# TOPIC 3.2: nth Term of an AP Formula: t_n = a + (n - 1)d
t32_exam = [
    # 1
    ("What is the formula for the \\(n^{\\text{th}}\\) term (\\(t_n\\)) of an Arithmetic Progression with first term \\(a\\) and common difference \\(d\\)?",
     ["\\(t_n = a + (n - 1)d\\)", "\\(t_n = a + nd\\)", "\\(t_n = a - (n - 1)d\\)", "\\(t_n = \\frac{a + d}{n}\\)"],
     "A", "OSC", "easy",
     "The general term or \\(n^{\\text{th}}\\) term of an AP is given by the standard formula \\(t_n = a + (n - 1)d\\)."),

    # 2
    ("In an AP, if \\(a = 5\\) and \\(d = 3\\), find the \\(10^{\\text{th}}\\) term (\\(t_{10}\\)).",
     ["\\(32\\)", "\\(35\\)", "\\(30\\)", "\\(29\\)"],
     "A", "OSC", "easy",
     "\\(t_{10} = a + (10 - 1)d = 5 + 9(3) = 5 + 27 = 32\\)."),

    # 3
    ("Find the \\(21^{\\text{st}}\\) term of the AP: \\(9, 15, 21, 27, \\dots\\)",
     ["\\(129\\)", "\\(135\\)", "\\(123\\)", "\\(132\\)"],
     "A", "OSC", "easy",
     "Here \\(a = 9\\) and \\(d = 15 - 9 = 6\\). \\(t_{21} = a + 20d = 9 + 20(6) = 9 + 120 = 129\\)."),

    # 4
    ("Find the \\(19^{\\text{th}}\\) term of the AP: \\(7, 13, 19, 25, \\dots\\)",
     ["\\(115\\)", "\\(121\\)", "\\(109\\)", "\\(113\\)"],
     "A", "OSC", "easy",
     "Here \\(a = 7\\), \\(d = 6\\). \\(t_{19} = 7 + (19 - 1) \\times 6 = 7 + 18 \\times 6 = 7 + 108 = 115\\)."),

    # 5
    ("Find the \\(27^{\\text{th}}\\) term of the following AP: \\(12, 16, 20, 24, \\dots\\)",
     ["\\(116\\)", "\\(120\\)", "\\(112\\)", "\\(108\\)"],
     "A", "OSC", "easy",
     "Here \\(a = 12\\), \\(d = 4\\). \\(t_{27} = 12 + (27 - 1) \\times 4 = 12 + 26 \\times 4 = 12 + 104 = 116\\)."),

    # 6
    ("Which term of the AP \\(5, 11, 17, 23, \\dots\\) is \\(149\\)?",
     ["\\(25^{\\text{th}}\\) term", "\\(24^{\\text{th}}\\) term", "\\(26^{\\text{th}}\\) term", "\\(23^{\\text{rd}}\\) term"],
     "A", "OSC", "medium",
     "Here \\(a = 5, d = 6\\). \\(t_n = a + (n - 1)d \\implies 149 = 5 + (n - 1)6 \\implies 144 = 6(n - 1) \\implies n - 1 = 24 \\implies n = 25\\)."),

    # 7
    ("Which term of the AP \\(51, 47, 43, 39, \\dots\\) is \\(11\\)?",
     ["\\(11^{\\text{th}}\\) term", "\\(10^{\\text{th}}\\) term", "\\(12^{\\text{th}}\\) term", "\\(9^{\\text{th}}\\) term"],
     "A", "OSC", "medium",
     "\\(a = 51\\), \\(d = -4\\). \\(t_n = 51 + (n - 1)(-4) = 11 \\implies -4(n - 1) = -40 \\implies n - 1 = 10 \\implies n = 11\\)."),

    # 8
    ("How many three-digit natural numbers are divisible by \\(5\\)?",
     ["\\(180\\)", "\\(179\\)", "\\(181\\)", "\\(175\\)"],
     "A", "OSC", "medium",
     "Three-digit numbers divisible by 5 are \\(105, 110, 115, \\dots, 995\\). Here \\(a = 105, d = 5, t_n = 995\\). \\(995 = 105 + (n - 1)5 \\implies 890 = 5(n - 1) \\implies n - 1 = 178 \\implies n = 180\\)."),

    # 9
    ("How many two-digit numbers are divisible by \\(4\\)?",
     ["\\(22\\)", "\\(23\\)", "\\(21\\)", "\\(20\\)"],
     "A", "OSC", "medium",
     "Two-digit numbers divisible by 4 are \\(12, 16, \\dots, 96\\). \\(a = 12, d = 4, t_n = 96\\). \\(96 = 12 + (n - 1)4 \\implies 84 = 4(n - 1) \\implies n - 1 = 21 \\implies n = 22\\)."),

    # 10
    ("In an AP, the \\(11^{\\text{th}}\\) term is \\(16\\) and the \\(21^{\\text{st}}\\) term is \\(29\\). Find the \\(41^{\\text{st}}\\) term.",
     ["\\(55\\)", "\\(52\\)", "\\(58\\)", "\\(60\\)"],
     "A", "OSC", "hard",
     "\\(t_{11} = a + 10d = 16\\), \\(t_{21} = a + 20d = 29\\). Subtracting gives \\(10d = 13 \\implies d = 1.3\\). Then \\(t_{41} = t_{21} + 20d = 29 + 20(1.3) = 29 + 26 = 55\\)."),

    # 11
    ("In an AP, the \\(17^{\\text{th}}\\) term is \\(7\\) more than its \\(10^{\\text{th}}\\) term. Find the common difference \\(d\\).",
     ["\\(1\\)", "\\(2\\)", "\\(7\\)", "\\(-1\\)"],
     "A", "OSC", "easy",
     "\\(t_{17} - t_{10} = (a + 16d) - (a + 9d) = 7d\\). Given \\(7d = 7 \\implies d = 1\\)."),

    # 12
    ("Check whether \\(-150\\) is a term of the AP: \\(11, 8, 5, 2, \\dots\\)",
     ["No, because \\(n\\) is not a natural number",
      "Yes, it is the \\(55^{\\text{th}}\\) term",
      "Yes, it is the \\(54^{\\text{th}}\\) term",
      "Cannot be determined"],
     "A", "OSC", "medium",
     "\\(a = 11, d = -3\\). \\(-150 = 11 + (n - 1)(-3) \\implies -161 = -3(n - 1) \\implies n - 1 = \\frac{161}{3} = 53.67\\), which is not an integer. Since \\(n \\notin \\mathbb{N}\\), \\(-150\\) is not a term."),

    # 13
    ("If \\(a = 2\\) and \\(d = 2.5\\), what is the \\(5^{\\text{th}}\\) term \\(t_5\\)?",
     ["\\(12\\)", "\\(10\\)", "\\(14.5\\)", "\\(11.5\\)"],
     "A", "OSC", "easy",
     "\\(t_5 = 2 + 4(2.5) = 2 + 10 = 12\\)."),

    # 14
    ("Find the first negative term of the AP: \\(20, 17, 14, 11, \\dots\\)",
     ["\\(8^{\\text{th}}\\) term (\\(-1\\))", "\\(7^{\\text{th}}\\) term (\\(2\\))", "\\(9^{\\text{th}}\\) term (\\(-4\\))", "\\(10^{\\text{th}}\\) term (\\(-7\\))"],
     "A", "OSC", "medium",
     "\\(a = 20, d = -3\\). \\(t_n < 0 \\implies 20 + (n - 1)(-3) < 0 \\implies 23 - 3n < 0 \\implies 3n > 23 \\implies n > 7.67\\). Smallest integer \\(n = 8\\). \\(t_8 = 20 + 7(-3) = -1\\)."),

    # 15
    ("If the \\(n^{\\text{th}}\\) term of a sequence is given by \\(t_n = 3n - 2\\), what is the common difference \\(d\\)?",
     ["\\(3\\)", "\\(-2\\)", "\\(1\\)", "\\(5\\)"],
     "A", "OSC", "easy",
     "For any linear sequence \\(t_n = An + B\\), the common difference is the coefficient of \\(n\\), which is \\(3\\). (Check: \\(t_1 = 1, t_2 = 4 \\implies d = 3\\))."),

    # 16
    ("If the \\(n^{\\text{th}}\\) term is \\(t_n = 5 - 2n\\), find \\(t_1\\) and \\(d\\).",
     ["\\(t_1 = 3, d = -2\\)", "\\(t_1 = 5, d = -2\\)", "\\(t_1 = 3, d = 2\\)", "\\(t_1 = -2, d = 5\\)"],
     "A", "OSC", "easy",
     "\\(t_1 = 5 - 2(1) = 3\\); \\(t_2 = 5 - 2(2) = 1\\); \\(d = t_2 - t_1 = 1 - 3 = -2\\)."),

    # 17
    ("For an AP, if \\(t_6 = -10\\) and \\(t_{10} = -26\\), find \\(a\\) and \\(d\\).",
     ["\\(a = 10, d = -4\\)", "\\(a = -10, d = -4\\)", "\\(a = 6, d = -4\\)", "\\(a = 14, d = -4\\)"],
     "A", "OSC", "medium",
     "\\(t_{10} - t_6 = 4d = -26 - (-10) = -16 \\implies d = -4\\). \\(t_6 = a + 5(-4) = -10 \\implies a - 20 = -10 \\implies a = 10\\)."),

    # 18
    ("In an AP, \\(7\\) times the \\(7^{\\text{th}}\\) term is equal to \\(11\\) times the \\(11^{\\text{th}}\\) term. What is the value of the \\(18^{\\text{th}}\\) term (\\(t_{18}\\))?",
     ["\\(0\\)", "\\(1\\)", "\\(18\\)", "\\(77\\)"],
     "A", "OSC", "hard",
     "\\(7(a + 6d) = 11(a + 10d) \\implies 7a + 42d = 11a + 110d \\implies 4a + 68d = 0 \\implies 4(a + 17d) = 0 \\implies a + 17d = 0\\). Since \\(t_{18} = a + 17d\\), \\(t_{18} = 0\\)."),

    # 19
    ("The \\(4^{\\text{th}}\\) term of an AP is zero. What is the relation between the \\(25^{\\text{th}}\\) term and the \\(11^{\\text{th}}\\) term?",
     ["\\(t_{25} = 3 \\cdot t_{11}\\)", "\\(t_{25} = 2 \\cdot t_{11}\\)", "\\(t_{25} = 4 \\cdot t_{11}\\)", "\\(t_{25} = t_{11}\\)"],
     "A", "OSC", "hard",
     "\\(t_4 = a + 3d = 0 \\implies a = -3d\\). \\(t_{11} = a + 10d = -3d + 10d = 7d\\). \\(t_{25} = a + 24d = -3d + 24d = 21d = 3(7d) = 3 \\cdot t_{11}\\)."),

    # 20
    ("Find the \\(10^{\\text{th}}\\) term from the end of the AP: \\(4, 9, 14, \\dots, 254\\).",
     ["\\(209\\)", "\\(214\\)", "\\(204\\)", "\\(199\\)"],
     "A", "OSC", "hard",
     "Reversing the sequence gives first term \\(a' = 254\\) and common difference \\(d' = -5\\). The \\(10^{\\text{th}}\\) term is \\(254 + 9(-5) = 254 - 45 = 209\\)."),

    # 21
    ("Find the number of terms in the AP: \\(7, 13, 19, \\dots, 205\\).",
     ["\\(34\\)", "\\(33\\)", "\\(35\\)", "\\(32\\)"],
     "A", "OSC", "medium",
     "\\(a = 7, d = 6\\). \\(205 = 7 + (n - 1)6 \\implies 198 = 6(n - 1) \\implies n - 1 = 33 \\implies n = 34\\)."),

    # 22
    ("Find the number of terms in the AP: \\(18, 15\\frac{1}{2}, 13, \\dots, -47\\).",
     ["\\(27\\)", "\\(26\\)", "\\(28\\)", "\\(25\\)"],
     "A", "OSC", "medium",
     "\\(a = 18, d = 15.5 - 18 = -2.5 = -5/2\\). \\(-47 = 18 + (n - 1)(-5/2) \\implies -65 = (n - 1)(-5/2) \\implies n - 1 = 26 \\implies n = 27\\)."),

    # 23
    ("In an AP, if \\(d = -4, n = 7, t_n = 4\\), find \\(a\\).",
     ["\\(28\\)", "\\(24\\)", "\\(20\\)", "\\(32\\)"],
     "A", "OSC", "easy",
     "\\(t_7 = a + 6(-4) = 4 \\implies a - 24 = 4 \\implies a = 28\\)."),

    # 24
    ("In an AP, if \\(a = 3.5, d = 0, n = 101\\), find \\(t_n\\).",
     ["\\(3.5\\)", "\\(0\\)", "\\(104.5\\)", "\\(353.5\\)"],
     "A", "OSC", "easy",
     "Since \\(d = 0\\), every term in the AP is equal to \\(a = 3.5\\)."),

    # 25
    ("What is the \\(15^{\\text{th}}\\) term of the AP: \\(-40, -15, 10, 35, \\dots\\)?",
     ["\\(310\\)", "\\(285\\)", "\\(335\\)", "\\(260\\)"],
     "A", "OSC", "easy",
     "\\(a = -40, d = -15 - (-40) = 25\\). \\(t_{15} = -40 + 14(25) = -40 + 350 = 310\\)."),

    # 26
    ("Which of the following represents the \\(p^{\\text{th}}\\) term from the beginning of an AP?",
     ["\\(a + (p - 1)d\\)", "\\(a + pd\\)", "\\(a - (p - 1)d\\)", "\\(p(a + d)\\)"],
     "A", "OSC", "easy",
     "By definition of the general term, \\(t_p = a + (p - 1)d\\)."),

    # 27
    ("If \\(m\\) times the \\(m^{\\text{th}}\\) term of an AP is equal to \\(n\\) times its \\(n^{\\text{th}}\\) term (where \\(m \\neq n\\)), what is the \\((m + n)^{\\text{th}}\\) term?",
     ["\\(0\\)", "\\(m + n\\)", "\\(1\\)", "\\(mn\\)"],
     "A", "OSC", "hard",
     "\\(m[a + (m-1)d] = n[a + (n-1)d] \\implies a(m - n) + d[m^2 - m - n^2 + n] = 0 \\implies (m - n)[a + (m + n - 1)d] = 0\\). Since \\(m \\neq n\\), \\(a + (m + n - 1)d = 0 = t_{m+n}\\)."),

    # 28
    ("In an AP, if \\(t_p = q\\) and \\(t_q = p\\), what is the \\(n^{\\text{th}}\\) term \\(t_n\\)?",
     ["\\(p + q - n\\)", "\\(p + q + n\\)", "\\(p - q + n\\)", "\\(n - p - q\\)"],
     "A", "OSC", "hard",
     "\\(a + (p-1)d = q\\) and \\(a + (q-1)d = p\\). Subtracting: \\((p - q)d = q - p \\implies d = -1\\). Then \\(a = p + q - 1\\). Thus \\(t_n = (p + q - 1) + (n - 1)(-1) = p + q - n\\)."),

    # 29
    ("If the \\(p^{\\text{th}}\\) term is \\(1/q\\) and the \\(q^{\\text{th}}\\) term is \\(1/p\\), find the \\((pq)^{\\text{th}}\\) term.",
     ["\\(1\\)", "\\(0\\)", "\\(pq\\)", "\\(1/(pq)\\)"],
     "A", "OSC", "hard",
     "Subtracting gives \\((p - q)d = \\frac{1}{q} - \\frac{1}{p} = \\frac{p-q}{pq} \\implies d = \\frac{1}{pq}\\). Then \\(a = \\frac{1}{pq}\\). \\(t_{pq} = a + (pq - 1)d = \\frac{1}{pq} + \\frac{pq - 1}{pq} = 1\\)."),

    # 30
    ("Two APs have the same common difference. The difference between their \\(100^{\\text{th}}\\) terms is \\(100\\). What is the difference between their \\(1000^{\\text{th}}\\) terms?",
     ["\\(100\\)", "\\(1000\\)", "\\(0\\)", "\\(900\\)"],
     "A", "OSC", "medium",
     "Let first terms be \\(a_1, a_2\\). \\(t_{100} - t'_{100} = (a_1 + 99d) - (a_2 + 99d) = a_1 - a_2 = 100\\). For any \\(n\\), \\(t_n - t'_n = a_1 - a_2 = 100\\). Thus the difference between the \\(1000^{\\text{th}}\\) terms is also \\(100\\)."),

    # 31
    ("Find the middle term of the AP: \\(6, 13, 20, \\dots, 216\\).",
     ["\\(111\\)", "\\(118\\)", "\\(104\\)", "\\(115\\)"],
     "A", "OSC", "medium",
     "\\(a = 6, d = 7\\). \\(216 = 6 + (n - 1)7 \\implies 210 = 7(n - 1) \\implies n = 31\\). The middle term is \\(\\frac{31+1}{2} = 16^{\\text{th}}\\) term. \\(t_{16} = 6 + 15(7) = 6 + 105 = 111\\)."),

    # 32
    ("How many natural numbers between \\(10\\) and \\(250\\) are multiples of \\(4\\)?",
     ["\\(60\\)", "\\(59\\)", "\\(61\\)", "\\(62\\)"],
     "A", "OSC", "medium",
     "The multiples of 4 between 10 and 250 are \\(12, 16, 20, \\dots, 248\\). \\(248 = 12 + (n - 1)4 \\implies 236 = 4(n - 1) \\implies n - 1 = 59 \\implies n = 60\\)."),

    # 33
    ("In an AP, if \\(a = -18.9, d = 2.5, t_n = 3.6\\), find \\(n\\).",
     ["\\(10\\)", "\\(9\\)", "\\(11\\)", "\\(12\\)"],
     "A", "OSC", "medium",
     "\\(3.6 = -18.9 + (n - 1)(2.5) \\implies 22.5 = 2.5(n - 1) \\implies n - 1 = 9 \\implies n = 10\\)."),

    # 34
    ("Find the \\(31^{\\text{st}}\\) term of an AP whose \\(11^{\\text{th}}\\) term is \\(38\\) and the \\(16^{\\text{th}}\\) term is \\(73\\).",
     ["\\(178\\)", "\\(185\\)", "\\(171\\)", "\\(164\\)"],
     "A", "OSC", "medium",
     "\\(t_{16} - t_{11} = 5d = 73 - 38 = 35 \\implies d = 7\\). \\(t_{31} = t_{16} + 15d = 73 + 15(7) = 73 + 105 = 178\\)."),

    # 35
    ("What is the \\(8^{\\text{th}}\\) term of the AP: \\(\\sqrt{2}, 3\\sqrt{2}, 5\\sqrt{2}, \\dots\\)?",
     ["\\(15\\sqrt{2}\\)", "\\(17\\sqrt{2}\\)", "\\(16\\sqrt{2}\\)", "\\(13\\sqrt{2}\\)"],
     "A", "OSC", "easy",
     "\\(a = \\sqrt{2}, d = 2\\sqrt{2}\\). \\(t_8 = \\sqrt{2} + 7(2\\sqrt{2}) = \\sqrt{2} + 14\\sqrt{2} = 15\\sqrt{2}\\)."),

    # 36
    ("An AP consists of \\(50\\) terms of which \\(3^{\\text{rd}}\\) term is \\(12\\) and the last term is \\(106\\). Find the \\(29^{\\text{th}}\\) term.",
     ["\\(64\\)", "\\(62\\)", "\\(66\\)", "\\(68\\)"],
     "A", "OSC", "medium",
     "\\(t_3 = a + 2d = 12\\), \\(t_{50} = a + 49d = 106\\). Subtracting: \\(47d = 94 \\implies d = 2\\). \\(a = 12 - 4 = 8\\). \\(t_{29} = 8 + 28(2) = 8 + 56 = 64\\)."),

    # 37
    ("If \\(k - 2, 4k - 1, 5k + 2\\) are in AP, what is the value of \\(k\\)?",
     ["\\(1\\)", "\\(2\\)", "\\(3\\)", "\\(-1\\)"],
     "A", "OSC", "medium",
     "\\(2(4k - 1) = (k - 2) + (5k + 2) \\implies 8k - 2 = 6k \\implies 2k = 2 \\implies k = 1\\)."),

    # 38
    ("If \\(x + 2, 2x, 2x + 3\\) are three consecutive terms of an AP, find \\(x\\).",
     ["\\(5\\)", "\\(4\\)", "\\(3\\)", "\\(6\\)"],
     "A", "OSC", "medium",
     "\\(2(2x) = (x + 2) + (2x + 3) \\implies 4x = 3x + 5 \\implies x = 5\\)."),

    # 39
    ("Is the sequence \\(t_n = 2n^2 + 1\\) an AP?",
     ["No, because the general term is quadratic, not linear",
      "Yes, with common difference 4",
      "Yes, with common difference 2",
      "Yes, because terms increase steadily"],
     "A", "OSC", "easy",
     "A sequence is an AP if and only if its \\(n^{\\text{th}}\\) term is a linear polynomial in \\(n\\). Since \\(t_n\\) is quadratic in \\(n\\), the differences between terms are not constant, so it is not an AP."),

    # 40
    ("Find the common difference of the AP whose \\(n^{\\text{th}}\\) term is \\(t_n = 6 - 4n\\).",
     ["\\(-4\\)", "\\(4\\)", "\\(6\\)", "\\(2\\)"],
     "A", "OSC", "easy",
     "\\(t_{n+1} - t_n = [6 - 4(n + 1)] - [6 - 4n] = -4\\).")
]

t32_prac = [
    # 41
    ("Find the \\(12^{\\text{th}}\\) term of the AP: \\(2, 7, 12, 17, \\dots\\)",
     ["\\(57\\)", "\\(52\\)", "\\(62\\)", "\\(60\\)"],
     "A", "OSC", "easy",
     "\\(a = 2, d = 5\\). \\(t_{12} = 2 + 11(5) = 2 + 55 = 57\\)."),

    # 42
    ("Find the \\(15^{\\text{th}}\\) term of the AP: \\(10, 7, 4, 1, \\dots\\)",
     ["\\(-32\\)", "\\(-35\\)", "\\(-29\\)", "\\(-38\\)"],
     "A", "OSC", "easy",
     "\\(a = 10, d = -3\\). \\(t_{15} = 10 + 14(-3) = 10 - 42 = -32\\)."),

    # 43
    ("Which term of the AP: \\(21, 18, 15, \\dots\\) is \\(-81\\)?",
     ["\\(35^{\\text{th}}\\) term", "\\(34^{\\text{th}}\\) term", "\\(36^{\\text{th}}\\) term", "\\(33^{\\text{rd}}\\) term"],
     "A", "OSC", "medium",
     "\\(a = 21, d = -3\\). \\(-81 = 21 + (n - 1)(-3) \\implies -102 = -3(n - 1) \\implies n - 1 = 34 \\implies n = 35\\)."),

    # 44
    ("Find the \\(20^{\\text{th}}\\) term from the end of the AP: \\(3, 8, 13, \\dots, 253\\).",
     ["\\(158\\)", "\\(153\\)", "\\(163\\)", "\\(148\\)"],
     "A", "OSC", "hard",
     "\\(l = 253, d = 5\\). Term from the end: \\(l - (n - 1)d = 253 - 19(5) = 253 - 95 = 158\\)."),

    # 45
    ("How many multiples of \\(7\\) are there between \\(100\\) and \\(300\\)?",
     ["\\(28\\)", "\\(29\\)", "\\(27\\)", "\\(30\\)"],
     "A", "OSC", "medium",
     "First multiple is 105, last multiple is 294. \\(294 = 105 + (n - 1)7 \\implies 189 = 7(n - 1) \\implies n - 1 = 27 \\implies n = 28\\)."),

    # 46
    ("If the \\(9^{\\text{th}}\\) term of an AP is \\(0\\), what is the ratio of its \\(29^{\\text{th}}\\) term to its \\(19^{\\text{th}}\\) term?",
     ["\\(2 : 1\\)", "\\(3 : 1\\)", "\\(1 : 2\\)", "\\(4 : 1\\)"],
     "A", "OSC", "hard",
     "\\(t_9 = a + 8d = 0 \\implies a = -8d\\). \\(t_{29} = a + 28d = 20d\\). \\(t_{19} = a + 18d = 10d\\). Ratio \\(t_{29}/t_{19} = 20d/10d = 2/1\\)."),

    # 47
    ("The \\(8^{\\text{th}}\\) term of an AP is half its second term and the \\(11^{\\text{th}}\\) term exceeds one third of its fourth term by \\(1\\). Find the common difference.",
     ["\\(-1/15\\)", "\\(1/5\\)", "\\(-1\\)", "\\(2\\)"],
     "A", "OSC", "hard",
     "\\(a + 7d = \\frac{1}{2}(a + d) \\implies 2a + 14d = a + d \\implies a = -13d\\). Also \\(a + 10d = \\frac{1}{3}(a + 3d) + 1 \\implies 3a + 30d = a + 3d + 3 \\implies 2a + 27d = 3\\). Substituting \\(a = -13d\\): \\(2(-13d) + 27d = 3 \\implies d = 3\\). Let's check: if \\(d = 3, a = -39\\). Then \\(t_8 = -39 + 21 = -18\\), \\(t_2 = -39 + 3 = -36\\), half is \\(-18\\). Correct! Option with common difference: here \\(d = 3\\). Let's adjust options cleanly to include 3."),
]
# Replacing 47 cleanly
t32_prac[-1] = (
    "The \\(8^{\\text{th}}\\) term of an AP is half its second term and the \\(11^{\\text{th}}\\) term exceeds one third of its fourth term by \\(1\\). Find the common difference \\(d\\).",
    ["\\(3\\)", "\\(2\\)", "\\(1\\)", "\\(4\\)"],
    "A", "OSC", "hard",
    "\\(a + 7d = \\frac{1}{2}(a + d) \\implies a = -13d\\). Also \\(a + 10d = \\frac{1}{3}(a + 3d) + 1 \\implies 2a + 27d = 3\\). Substituting \\(a = -13d \\implies -26d + 27d = 3 \\implies d = 3\\)."
)

t32_prac.extend([
    # 48
    ("Find the \\(10^{\\text{th}}\\) term of the sequence: \\(\\frac{1}{m}, \\frac{1+m}{m}, \\frac{1+2m}{m}, \\dots\\)",
     ["\\(\\frac{1+9m}{m}\\)", "\\(\\frac{1+10m}{m}\\)", "\\(\\frac{10}{m}\\)", "\\(10\\)"],
     "A", "OSC", "medium",
     "\\(a = 1/m\\), \\(d = \\frac{1+m}{m} - \\frac{1}{m} = 1\\). \\(t_{10} = 1/m + 9(1) = \\frac{1+9m}{m}\\)."),

    # 49
    ("Which term of the AP: \\(3, 15, 27, 39, \\dots\\) will be \\(132\\) more than its \\(54^{\\text{th}}\\) term?",
     ["\\(65^{\\text{th}}\\) term", "\\(64^{\\text{th}}\\) term", "\\(66^{\\text{th}}\\) term", "\\(63^{\\text{rd}}\\) term"],
     "A", "OSC", "hard",
     "\\(d = 12\\). \\(t_n - t_{54} = 132 \\implies (n - 54)d = 132 \\implies (n - 54)(12) = 132 \\implies n - 54 = 11 \\implies n = 65\\)."),

    # 50
    ("If \\(a = -3\\) and \\(d = 4\\), find \\(t_7\\).",
     ["\\(21\\)", "\\(25\\)", "\\(24\\)", "\\(18\\)"],
     "A", "OSC", "easy",
     "\\(t_7 = -3 + 6(4) = -3 + 24 = 21\\)."),

    # 51
    ("Find the \\(18^{\\text{th}}\\) term of the AP: \\(\\sqrt{3}, \\sqrt{12}, \\sqrt{27}, \\dots\\)",
     ["\\(18\\sqrt{3}\\)", "\\(17\\sqrt{3}\\)", "\\(19\\sqrt{3}\\)", "\\(36\\)"],
     "A", "OSC", "medium",
     "The terms are \\(\\sqrt{3}, 2\\sqrt{3}, 3\\sqrt{3}, \\dots\\). Here \\(a = \\sqrt{3}, d = \\sqrt{3}\\). Thus \\(t_{18} = a + 17d = \\sqrt{3} + 17\\sqrt{3} = 18\\sqrt{3}\\)."),

    # 52
    ("Find the \\(25^{\\text{th}}\\) term of the AP: \\(-5, -5/2, 0, 5/2, \\dots\\)",
     ["\\(55\\)", "\\(60\\)", "\\(50\\)", "\\(65\\)"],
     "A", "OSC", "easy",
     "\\(a = -5, d = 2.5 = 5/2\\). \\(t_{25} = -5 + 24(2.5) = -5 + 60 = 55\\)."),

    # 53
    ("In an AP, if \\(t_{24} = 2 \\cdot t_{10}\\), what is the relation between \\(a\\) and \\(d\\)?",
     ["\\(a = 5d\\)", "\\(a = 4d\\)", "\\(a = 3d\\)", "\\(a = 2d\\)"],
     "A", "OSC", "medium",
     "\\(a + 23d = 2(a + 9d) = 2a + 18d \\implies a = 5d\\)."),

    # 54
    ("If the \\(p^{\\text{th}}\\) term of an AP is \\(q\\) and the \\(q^{\\text{th}}\\) term is \\(p\\), what is its \\((p+q)^{\\text{th}}\\) term?",
     ["\\(0\\)", "\\(p+q\\)", "\\(1\\)", "\\(-1\\)"],
     "A", "OSC", "hard",
     "Since \\(t_n = p + q - n\\), \\(t_{p+q} = p + q - (p + q) = 0\\)."),

    # 55
    ("Determine the AP whose \\(3^{\\text{rd}}\\) term is \\(5\\) and the \\(7^{\\text{th}}\\) term is \\(9\\).",
     ["\\(3, 4, 5, 6, 7, \\dots\\)", "\\(1, 3, 5, 7, 9, \\dots\\)", "\\(2, 4, 6, 8, \\dots\\)", "\\(0, 2, 4, 6, \\dots\\)"],
     "A", "OSC", "easy",
     "\\(t_7 - t_3 = 4d = 9 - 5 = 4 \\implies d = 1\\). \\(a = 5 - 2(1) = 3\\). The AP is \\(3, 4, 5, 6, 7, \\dots\\)."),

    # 56
    ("Find the value of \\(x\\) if \\(8x + 4, 6x - 2, 2x + 7\\) are in AP.",
     ["\\(7.5\\)", "\\(5\\)", "\\(6\\)", "\\(4.5\\)"],
     "A", "OSC", "medium",
     "\\(2(6x - 2) = (8x + 4) + (2x + 7) \\implies 12x - 4 = 10x + 11 \\implies 2x = 15 \\implies x = 7.5\\)."),

    # 57
    ("What is the \\(11^{\\text{th}}\\) term of an AP whose first two terms are \\(-3\\) and \\(4\\)?",
     ["\\(67\\)", "\\(70\\)", "\\(64\\)", "\\(60\\)"],
     "A", "OSC", "easy",
     "\\(a = -3, d = 4 - (-3) = 7\\). \\(t_{11} = -3 + 10(7) = 67\\)."),

    # 58
    ("Which term of the AP: \\(121, 117, 113, \\dots\\) is its first negative term?",
     ["\\(32^{\\text{nd}}\\) term", "\\(31^{\\text{st}}\\) term", "\\(33^{\\text{rd}}\\) term", "\\(30^{\\text{th}}\\) term"],
     "A", "OSC", "medium",
     "\\(a = 121, d = -4\\). \\(121 + (n - 1)(-4) < 0 \\implies 125 - 4n < 0 \\implies 4n > 125 \\implies n > 31.25\\). Smallest integer is \\(32\\)."),

    # 59
    ("For what value of \\(n\\) are the \\(n^{\\text{th}}\\) terms of two APs \\(63, 65, 67, \\dots\\) and \\(3, 10, 17, \\dots\\) equal?",
     ["\\(13\\)", "\\(12\\)", "\\(14\\)", "\\(15\\)"],
     "A", "OSC", "medium",
     "\\(63 + (n - 1)2 = 3 + (n - 1)7 \\implies 63 + 2n - 2 = 3 + 7n - 7 \\implies 61 + 2n = 7n - 4 \\implies 5n = 65 \\implies n = 13\\)."),

    # 60
    ("In an AP, if \\(S_n\\) denotes the sum of first \\(n\\) terms, how can \\(t_n\\) be expressed in terms of \\(S_n\\)?",
     ["\\(t_n = S_n - S_{n-1}\\)", "\\(t_n = S_n + S_{n-1}\\)", "\\(t_n = S_{n-1} - S_n\\)", "\\(t_n = \\frac{S_n}{n}\\)"],
     "A", "OSC", "easy",
     "The \\(n^{\\text{th}}\\) term is obtained by subtracting the sum of the first \\((n-1)\\) terms from the sum of the first \\(n\\) terms: \\(t_n = S_n - S_{n-1}\\) (for \\(n \\ge 2\\))."),

    # 61
    ("Find the \\(20^{\\text{th}}\\) term of the AP whose \\(n^{\\text{th}}\\) term is \\(t_n = 4n + 5\\).",
     ["\\(85\\)", "\\(80\\)", "\\(90\\)", "\\(75\\)"],
     "A", "OSC", "easy",
     "\\(t_{20} = 4(20) + 5 = 80 + 5 = 85\\)."),

    # 62
    ("Find the \\(16^{\\text{th}}\\) term of the AP: \\(10.0, 10.5, 11.0, 11.5, \\dots\\)",
     ["\\(17.5\\)", "\\(18.0\\)", "\\(17.0\\)", "\\(18.5\\)"],
     "A", "OSC", "easy",
     "\\(a = 10, d = 0.5\\). \\(t_{16} = 10 + 15(0.5) = 10 + 7.5 = 17.5\\)."),

    # 63
    ("How many terms are there in the finite AP: \\(20, 25, 30, \\dots, 100\\)?",
     ["\\(17\\)", "\\(16\\)", "\\(18\\)", "\\(15\\)"],
     "A", "OSC", "easy",
     "\\(100 = 20 + (n - 1)5 \\implies 80 = 5(n - 1) \\implies n - 1 = 16 \\implies n = 17\\)."),

    # 64
    ("Find the \\(50^{\\text{th}}\\) term of the AP: \\(1, 4, 7, 10, \\dots\\)",
     ["\\(148\\)", "\\(151\\)", "\\(145\\)", "\\(150\\)"],
     "A", "OSC", "easy",
     "\\(a = 1, d = 3\\). \\(t_{50} = 1 + 49(3) = 1 + 147 = 148\\)."),

    # 65
    ("Find \\(d\\) if \\(t_{18} - t_{14} = 32\\).",
     ["\\(8\\)", "\\(6\\)", "\\(4\\)", "\\(10\\)"],
     "A", "OSC", "easy",
     "\\(t_{18} - t_{14} = (a + 17d) - (a + 13d) = 4d = 32 \\implies d = 8\\)."),

    # 66
    ("If \\(t_2 = 13\\) and \\(t_5 = 25\\), find the first term \\(a\\).",
     ["\\(9\\)", "\\(8\\)", "\\(10\\)", "\\(7\\)"],
     "A", "OSC", "medium",
     "\\(t_5 - t_2 = 3d = 25 - 13 = 12 \\implies d = 4\\). \\(a = t_2 - d = 13 - 4 = 9\\)."),

    # 67
    ("Is \\(301\\) a term of the sequence \\(5, 11, 17, 23, \\dots\\)?",
     ["No, because \\(n\\) is not a whole number",
      "Yes, it is the \\(50^{\\text{th}}\\) term",
      "Yes, it is the \\(51^{\\text{st}}\\) term",
      "Cannot be determined"],
     "A", "OSC", "medium",
     "\\(301 = 5 + (n - 1)6 \\implies 296 = 6(n - 1) \\implies n - 1 = 296/6 = 49.33\\). Since \\(n \\notin \\mathbb{N}\\), 301 is not a term."),

    # 68
    ("Find the \\(6^{\\text{th}}\\) term from the end of the AP: \\(17, 14, 11, \\dots, -40\\).",
     ["\\(-25\\)", "\\(-22\\)", "\\(-28\\)", "\\(-19\\)"],
     "A", "OSC", "medium",
     "\\(l = -40, d = -3\\). Term from end: \\(l - (n - 1)d = -40 - 5(-3) = -40 + 15 = -25\\)."),

    # 69
    ("If \\(a = 7\\) and \\(t_n = 84\\) with \\(d = 3.5\\), find \\(n\\).",
     ["\\(23\\)", "\\(22\\)", "\\(24\\)", "\\(21\\)"],
     "A", "OSC", "easy",
     "\\(84 = 7 + (n - 1)(3.5) \\implies 77 = 3.5(n - 1) \\implies n - 1 = 22 \\implies n = 23\\)."),

    # 70
    ("If \\(3x, x + 2, 8\\) are in AP, find \\(x\\).",
     ["\\(4\\)", "\\(2\\)", "\\(3\\)", "\\(5\\)"],
     "A", "OSC", "medium",
     "\\(2(x + 2) = 3x + 8 \\implies 2x + 4 = 3x + 8 \\implies x = -4\\). Let's fix options: \\(-4, 4, 2, -2\\).")
])
t32_prac[-1] = (
    "If \\(3x, x + 2, 8\\) are in AP, find \\(x\\).",
    ["\\(-4\\)", "\\(4\\)", "\\(2\\)", "\\(-2\\)"],
    "A", "OSC", "medium",
    "\\(2(x + 2) = 3x + 8 \\implies 2x + 4 = 3x + 8 \\implies x = -4\\)."
)

t32_mock = [
    # 71
    ("What does \\(t_n\\) represent in the formula \\(t_n = a + (n - 1)d\\)?",
     ["The \\(n^{\\text{th}}\\) term of the arithmetic progression",
      "The sum of the first \\(n\\) terms",
      "The common difference",
      "The total number of terms"],
     "A", "OSC", "easy",
     "In arithmetic progression terminology, \\(t_n\\) denotes the value of the \\(n^{\\text{th}}\\) term."),

    # 72
    ("What does \\(d\\) stand for in an Arithmetic Progression?",
     ["Common difference between consecutive terms",
      "Common divisor of all terms",
      "Degree of the sequence polynomial",
      "Distance between graphs"],
     "A", "OSC", "easy",
     "In an AP, \\(d = t_{k+1} - t_k\\) is called the common difference."),

    # 73
    ("In an AP, the first term is represented by which symbol?",
     ["\\(a\\) or \\(t_1\\)", "\\(d\\)", "\\(S_n\\)", "\\(n\\)"],
     "A", "OSC", "easy",
     "The first term of an AP is conventionally denoted by \\(a\\) or \\(t_1\\)."),

    # 74
    ("If the common difference \\(d = 0\\), what is the \\(100^{\\text{th}}\\) term if \\(t_1 = 7\\)?",
     ["\\(7\\)", "\\(700\\)", "\\(0\\)", "\\(107\\)"],
     "A", "OSC", "easy",
     "When \\(d = 0\\), all terms are identical: \\(t_n = a = 7\\)."),

    # 75
    ("What is the \\(2^{\\text{nd}}\\) term of the AP where \\(a = 4\\) and \\(d = -3\\)?",
     ["\\(1\\)", "\\(7\\)", "\\(-1\\)", "\\(-2\\)"],
     "A", "OSC", "easy",
     "\\(t_2 = a + d = 4 + (-3) = 1\\)."),

    # 76
    ("What is the \\(3^{\\text{rd}}\\) term of the AP where \\(a = -5\\) and \\(d = 2\\)?",
     ["\\(-1\\)", "\\(-3\\)", "\\(1\\)", "\\(-7\\)"],
     "A", "OSC", "easy",
     "\\(t_3 = a + 2d = -5 + 2(2) = -5 + 4 = -1\\)."),

    # 77
    ("If \\(t_1 = 10\\) and \\(t_2 = 15\\), what is \\(t_3\\)?",
     ["\\(20\\)", "\\(25\\)", "\\(18\\)", "\\(30\\)"],
     "A", "OSC", "easy",
     "\\(d = 15 - 10 = 5\\). \\(t_3 = 15 + 5 = 20\\)."),

    # 78
    ("Can \\(n\\), the term number in an AP, ever be negative or a fraction?",
     ["No, \\(n\\) must always be a positive integer (natural number \\(n \\in \\mathbb{N}\\))",
      "Yes, \\(n\\) can be any real number",
      "Yes, \\(n\\) can be a fraction for partial terms",
      "Yes, \\(n\\) can be negative for preceding terms"],
     "A", "OSC", "easy",
     "The position or index of a term \\(n\\) represents a counting number, so \\(n\\) must be a natural number (\\(1, 2, 3, \\dots\\))."),

    # 79
    ("What is the difference between the \\(10^{\\text{th}}\\) term and the \\(5^{\\text{th}}\\) term in any AP?",
     ["\\(5d\\)", "\\(4d\\)", "\\(6d\\)", "\\(5a\\)"],
     "A", "OSC", "easy",
     "\\(t_{10} - t_5 = (a + 9d) - (a + 4d) = 5d\\)."),

    # 80
    ("If \\(t_n = 2n + 1\\), what is the first term \\(a\\)?",
     ["\\(3\\)", "\\(1\\)", "\\(2\\)", "\\(5\\)"],
     "A", "OSC", "easy",
     "\\(t_1 = 2(1) + 1 = 3\\)."),

    # 81
    ("If \\(a = 0\\) and \\(d = 5\\), what is the \\(10^{\\text{th}}\\) term?",
     ["\\(45\\)", "\\(50\\)", "\\(40\\)", "\\(55\\)"],
     "A", "OSC", "easy",
     "\\(t_{10} = 0 + 9(5) = 45\\)."),

    # 82
    ("What is the value of \\(t_1\\) if \\(t_n = a + (n - 1)d\\) when \\(n = 1\\)?",
     ["\\(a\\)", "\\(a + d\\)", "\\(0\\)", "\\(d\\)"],
     "A", "OSC", "easy",
     "\\(t_1 = a + (1 - 1)d = a + 0 = a\\).")
]

if __name__ == "__main__":
    topic_code = "MH-10-MTH1-3-3.2"
    all_qs = build_topic_questions(topic_code, t32_exam, t32_prac, t32_mock)
    out_path = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch3_t2.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {topic_code} -> {out_path}")
