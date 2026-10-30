# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 3: Arithmetic Progression - Topic 3.3: Sum of First n Terms of an AP (MH-10-MTH1-3-3.3)
Total: 82 Canonical Questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# TOPIC 3.3: Sum of First n Terms of an AP: S_n = n/2 [2a + (n - 1)d]
t33_exam = [
    # 1
    ("Which of the following is the standard formula for the sum of the first \\(n\\) terms (\\(S_n\\)) of an AP?",
     ["\\(S_n = \\frac{n}{2}[2a + (n - 1)d]\\)", "\\(S_n = n[a + (n - 1)d]\\)", "\\(S_n = \\frac{n}{2}[a + nd]\\)", "\\(S_n = \\frac{n}{2}[2a - (n - 1)d]\\)"],
     "A", "OSC", "easy",
     "The sum of the first \\(n\\) terms of an AP with first term \\(a\\) and common difference \\(d\\) is given by \\(S_n = \\frac{n}{2}[2a + (n - 1)d]\\)."),

    # 2
    ("When the first term \\(t_1\\) and the last term \\(t_n\\) are known, what formula gives \\(S_n\\)?",
     ["\\(S_n = \\frac{n}{2}(t_1 + t_n)\\)", "\\(S_n = n(t_1 + t_n)\\)", "\\(S_n = \\frac{n}{2}(t_1 - t_n)\\)", "\\(S_n = \\frac{t_1 + t_n}{2n}\\)"],
     "A", "OSC", "easy",
     "Since \\(2a + (n - 1)d = a + [a + (n - 1)d] = t_1 + t_n\\), the sum is conveniently written as \\(S_n = \\frac{n}{2}(t_1 + t_n)\\)."),

    # 3
    ("Find the sum of the first \\(n\\) natural numbers.",
     ["\\(S_n = \\frac{n(n + 1)}{2}\\)", "\\(S_n = n(n + 1)\\)", "\\(S_n = n^2\\)", "\\(S_n = \\frac{n(n - 1)}{2}\\)"],
     "A", "OSC", "easy",
     "For the sequence \\(1, 2, 3, \\dots, n\\), \\(a = 1\\) and \\(t_n = n\\). Thus \\(S_n = \\frac{n}{2}(1 + n) = \\frac{n(n + 1)}{2}\\)."),

    # 4
    ("What is the sum of the first \\(n\\) even natural numbers?",
     ["\\(n(n + 1)\\)", "\\(n^2\\)", "\\(\\frac{n(n + 1)}{2}\\)", "\\(2n(n + 1)\\)"],
     "A", "OSC", "easy",
     "For \\(2, 4, 6, \\dots, 2n\\), \\(a = 2, d = 2\\). \\(S_n = \\frac{n}{2}[4 + (n - 1)2] = \\frac{n}{2}[2n + 2] = n(n + 1)\\)."),

    # 5
    ("What is the sum of the first \\(n\\) odd natural numbers?",
     ["\\(n^2\\)", "\\(n(n + 1)\\)", "\\(2n^2\\)", "\\(n^2 + 1\\)"],
     "A", "OSC", "easy",
     "For \\(1, 3, 5, \\dots, (2n - 1)\\), \\(a = 1, t_n = 2n - 1\\). \\(S_n = \\frac{n}{2}[1 + (2n - 1)] = \\frac{n}{2}(2n) = n^2\\)."),

    # 6
    ("Find the sum of the first \\(123\\) even natural numbers.",
     ["\\(15252\\)", "\\(15129\\)", "\\(15376\\)", "\\(15000\\)"],
     "A", "OSC", "medium",
     "Using \\(S_n = n(n + 1)\\) for even natural numbers: \\(S_{123} = 123 \\times (123 + 1) = 123 \\times 124 = 15252\\)."),

    # 7
    ("Find the sum of all even natural numbers from \\(1\\) to \\(350\\).",
     ["\\(30800\\)", "\\(30625\\)", "\\(31000\\)", "\\(61425\\)"],
     "A", "OSC", "medium",
     "Even numbers from 1 to 350 are \\(2, 4, 6, \\dots, 350\\). Here \\(n = 350 / 2 = 175\\). \\(S_{175} = n(n + 1) = 175 \\times 176 = 30800\\)."),

    # 8
    ("Find the sum of all natural numbers between \\(1\\) and \\(140\\) which are divisible by \\(4\\).",
     ["\\(2380\\)", "\\(2450\\)", "\\(2310\\)", "\\(2520\\)"],
     "A", "OSC", "medium",
     "Natural numbers between 1 and 140 divisible by 4 are \\(4, 8, 12, \\dots, 136\\). \\(a = 4, d = 4, t_n = 136\\). \\(136 = 4 + 4(n - 1) \\implies n = 34\\). \\(S_{34} = \\frac{34}{2}(4 + 136) = 17 \\times 140 = 2380\\)."),

    # 9
    ("In an AP, the \\(19^{\\text{th}}\\) term is \\(52\\) and the \\(38^{\\text{th}}\\) term is \\(128\\). Find the sum of its first \\(56\\) terms.",
     ["\\(5040\\)", "\\(5080\\)", "\\(4980\\)", "\\(5120\\)"],
     "A", "OSC", "hard",
     "\\(t_{19} = a + 18d = 52\\) and \\(t_{38} = a + 37d = 128\\). Adding both: \\(2a + 55d = 180\\). The sum of first 56 terms is \\(S_{56} = \\frac{56}{2}[2a + 55d] = 28 \\times 180 = 5040\\)."),

    # 10
    ("In an AP, the sum of the first \\(55\\) terms is \\(3300\\). Find its \\(28^{\\text{th}}\\) term (\\(t_{28}\\)).",
     ["\\(60\\)", "\\(55\\)", "\\(65\\)", "\\(50\\)"],
     "A", "OSC", "medium",
     "\\(S_{55} = \\frac{55}{2}[2a + 54d] = 55(a + 27d) = 3300\\). Since \\(t_{28} = a + 27d\\), we get \\(55 \\times t_{28} = 3300 \\implies t_{28} = \\frac{3300}{55} = 60\\)."),

    # 11
    ("Find the sum of the first \\(20\\) terms of the AP: \\(5, 8, 11, 14, \\dots\\)",
     ["\\(670\\)", "\\(650\\)", "\\(690\\)", "\\(700\\)"],
     "A", "OSC", "easy",
     "\\(a = 5, d = 3\\). \\(S_{20} = \\frac{20}{2}[2(5) + 19(3)] = 10[10 + 57] = 10(67) = 670\\)."),

    # 12
    ("Find the sum of the first \\(10\\) terms of the AP: \\(2, 7, 12, \\dots\\)",
     ["\\(245\\)", "\\(250\\)", "\\(240\\)", "\\(255\\)"],
     "A", "OSC", "easy",
     "\\(a = 2, d = 5\\). \\(S_{10} = \\frac{10}{2}[2(2) + 9(5)] = 5[4 + 45] = 5(49) = 245\\)."),

    # 13
    ("Find the sum: \\(34 + 32 + 30 + \\dots + 10\\).",
     ["\\(286\\)", "\\(290\\)", "\\(280\\)", "\\(300\\)"],
     "A", "OSC", "medium",
     "\\(a = 34, d = -2, t_n = 10\\). \\(10 = 34 + (n - 1)(-2) \\implies -24 = -2(n - 1) \\implies n = 13\\). \\(S_{13} = \\frac{13}{2}(34 + 10) = \\frac{13}{2}(44) = 13 \\times 22 = 286\\)."),

    # 14
    ("Find the sum: \\((-5) + (-8) + (-11) + \\dots + (-230)\\).",
     ["\\(-8930\\)", "\\(-8900\\)", "\\(-8950\\)", "\\(-9000\\)"],
     "A", "OSC", "medium",
     "\\(a = -5, d = -3, t_n = -230\\). \\(-230 = -5 + (n - 1)(-3) \\implies -225 = -3(n - 1) \\implies n = 76\\). \\(S_{76} = \\frac{76}{2}[-5 + (-230)] = 38(-235) = -8930\\)."),

    # 15
    ("In an AP, given \\(a = 7, t_{13} = 35\\), find \\(d\\) and \\(S_{13}\\).",
     ["\\(d = 7/3, S_{13} = 273\\)", "\\(d = 2, S_{13} = 260\\)", "\\(d = 3, S_{13} = 280\\)", "\\(d = 7/3, S_{13} = 265\\)"],
     "A", "OSC", "medium",
     "\\(t_{13} = 7 + 12d = 35 \\implies 12d = 28 \\implies d = 28/12 = 7/3\\). \\(S_{13} = \\frac{13}{2}(a + t_{13}) = \\frac{13}{2}(7 + 35) = \\frac{13}{2}(42) = 13 \\times 21 = 273\\)."),

    # 16
    ("How many terms of the AP \\(9, 17, 25, \\dots\\) must be taken to give a sum of \\(636\\)?",
     ["\\(12\\)", "\\(11\\)", "\\(13\\)", "\\(14\\)"],
     "A", "OSC", "hard",
     "\\(a = 9, d = 8\\). \\(S_n = \\frac{n}{2}[18 + (n - 1)8] = \\frac{n}{2}[8n + 10] = n(4n + 5) = 636 \\implies 4n^2 + 5n - 636 = 0\\). \\((4n + 53)(n - 12) = 0\\). Since \\(n \\in \\mathbb{N}\\), \\(n = 12\\)."),

    # 17
    ("The first and the last terms of an AP are \\(17\\) and \\(350\\) respectively. If the common difference is \\(9\\), how many terms are there and what is their sum?",
     ["\\(n = 38, S_{38} = 6973\\)", "\\(n = 37, S_{37} = 6800\\)", "\\(n = 39, S_{39} = 7150\\)", "\\(n = 38, S_{38} = 6850\\)"],
     "A", "OSC", "medium",
     "\\(350 = 17 + (n - 1)9 \\implies 333 = 9(n - 1) \\implies n - 1 = 37 \\implies n = 38\\). \\(S_{38} = \\frac{38}{2}(17 + 350) = 19 \\times 367 = 6973\\)."),

    # 18
    ("Find the sum of first \\(51\\) terms of an AP whose second and third terms are \\(14\\) and \\(18\\) respectively.",
     ["\\(5610\\)", "\\(5500\\)", "\\(5650\\)", "\\(5700\\)"],
     "A", "OSC", "medium",
     "\\(d = t_3 - t_2 = 18 - 14 = 4\\). \\(a = 14 - 4 = 10\\). \\(S_{51} = \\frac{51}{2}[2(10) + 50(4)] = \\frac{51}{2}[20 + 200] = \\frac{51}{2}(220) = 51 \\times 110 = 5610\\)."),

    # 19
    ("If the sum of first \\(7\\) terms of an AP is \\(49\\) and that of \\(17\\) terms is \\(289\\), find the sum of first \\(n\\) terms.",
     ["\\(n^2\\)", "\\(2n^2\\)", "\\(n(n + 1)\\)", "\\(n^2 + n\\)"],
     "A", "OSC", "medium",
     "\\(S_7 = \\frac{7}{2}[2a + 6d] = 49 \\implies a + 3d = 7\\). \\(S_{17} = \\frac{17}{2}[2a + 16d] = 289 \\implies a + 8d = 17\\). Subtracting: \\(5d = 10 \\implies d = 2\\), \\(a = 1\\). Thus \\(S_n = \\frac{n}{2}[2(1) + (n - 1)2] = n^2\\)."),

    # 20
    ("If the sum of the first \\(n\\) terms of an AP is given by \\(S_n = 4n - n^2\\), what is the first term \\(t_1\\) and the second term \\(t_2\\)?",
     ["\\(t_1 = 3, t_2 = 1\\)", "\\(t_1 = 4, t_2 = 2\\)", "\\(t_1 = 3, t_2 = 5\\)", "\\(t_1 = 2, t_2 = 0\\)"],
     "A", "OSC", "medium",
     "\\(t_1 = S_1 = 4(1) - 1^2 = 3\\). \\(S_2 = 4(2) - 2^2 = 8 - 4 = 4\\). \\(t_2 = S_2 - S_1 = 4 - 3 = 1\\)."),

    # 21
    ("If the sum of the first \\(n\\) terms of an AP is \\(S_n = 3n^2 + 5n\\), what is its \\(n^{\\text{th}}\\) term \\(t_n\\)?",
     ["\\(6n + 2\\)", "\\(6n - 2\\)", "\\(3n + 2\\)", "\\(6n + 5\\)"],
     "A", "OSC", "hard",
     "\\(t_n = S_n - S_{n-1} = (3n^2 + 5n) - [3(n - 1)^2 + 5(n - 1)] = 3n^2 + 5n - [3n^2 - 6n + 3 + 5n - 5] = 6n + 2\\)."),

    # 22
    ("Find the sum of the first \\(15\\) multiples of \\(8\\).",
     ["\\(960\\)", "\\(920\\)", "\\(980\\)", "\\(1000\\)"],
     "A", "OSC", "easy",
     "The multiples of 8 are \\(8, 16, \\dots, 120\\). \\(a = 8, d = 8, n = 15\\). \\(S_{15} = \\frac{15}{2}(8 + 120) = \\frac{15}{2}(128) = 15 \\times 64 = 960\\)."),

    # 23
    ("Find the sum of the odd numbers between \\(0\\) and \\(50\\).",
     ["\\(625\\)", "\\(600\\)", "\\(650\\)", "\\(576\\)"],
     "A", "OSC", "easy",
     "Odd numbers from 0 to 50 are \\(1, 3, 5, \\dots, 49\\). The number of terms is \\(n = 25\\). Using \\(S_n = n^2\\), \\(S_{25} = 25^2 = 625\\)."),

    # 24
    ("Sum of three consecutive terms in an AP is \\(27\\) and their product is \\(504\\). What are the three terms?",
     ["\\(7, 9, 11\\) (or \\(11, 9, 7\\))", "\\(6, 9, 12\\)", "\\(5, 9, 13\\)", "\\(8, 9, 10\\)"],
     "A", "OSC", "hard",
     "Let terms be \\(a - d, a, a + d\\). Sum \\(= 3a = 27 \\implies a = 9\\). Product \\(= (9 - d)(9)(9 + d) = 504 \\implies 9(81 - d^2) = 504 \\implies 81 - d^2 = 56 \\implies d^2 = 25 \\implies d = \\pm 5\\). If \\(d = 2\\) or \\(5\\): \\(9 - 2 = 7, 9, 11\\). Terms are \\(7, 9, 11\\)."),

    # 25
    ("What standard form should be chosen for four consecutive terms in an AP?",
     ["\\(a - 3d, a - d, a + d, a + 3d\\) (common difference \\(2d\\)) or \\(a - d, a, a + d, a + 2d\\)",
      "\\(a, 2a, 3a, 4a\\)",
      "\\(a, a^2, a^3, a^4\\)",
      "\\(a, a + d, a + d^2, a + d^3\\)"],
     "A", "OSC", "easy",
     "For an even number of terms (4 terms), choosing symmetric terms \\(a - 3d, a - d, a + d, a + 3d\\) with common difference \\(2d\\) (or \\(a - d, a, a + d, a + 2d\\)) simplifies the sum to a single variable."),

    # 26
    ("Sum of four consecutive terms in an AP is \\(12\\) and sum of \\(3^{\\text{rd}}\\) and \\(4^{\\text{th}}\\) terms is \\(14\\). Find the terms.",
     ["\\(-3, 1, 5, 9\\)", "\\(-1, 1, 3, 5\\)", "\\(-2, 1, 4, 7\\)", "\\(0, 2, 4, 6\\)"],
     "A", "OSC", "hard",
     "Let the terms be \\(a - d, a, a + d, a + 2d\\). Sum \\(= 4a + 2d = 12 \\implies 2a + d = 6\\). Sum of 3rd and 4th terms \\(= (a + d) + (a + 2d) = 2a + 3d = 14\\). Subtracting: \\(2d = 8 \\implies d = 4\\). Then \\(2a + 4 = 6 \\implies a = 1\\). Terms: \\(1 - 4 = -3, 1, 1 + 4 = 5, 1 + 8 = 9\\)."),

    # 27
    ("Find the sum of the first \\(24\\) terms of the AP: \\(12, 10, 8, 6, \\dots\\)",
     ["\\(-264\\)", "\\(-240\\)", "\\(-288\\)", "\\(-250\\)"],
     "A", "OSC", "medium",
     "\\(a = 12, d = -2\\). \\(S_{24} = \\frac{24}{2}[2(12) + 23(-2)] = 12[24 - 46] = 12(-22) = -264\\)."),

    # 28
    ("In an AP, if \\(S_{10} = 150\\) and \\(S_9 = 126\\), find the \\(10^{\\text{th}}\\) term (\\(t_{10}\\)).",
     ["\\(24\\)", "\\(25\\)", "\\(22\\)", "\\(26\\)"],
     "A", "OSC", "easy",
     "\\(t_{10} = S_{10} - S_9 = 150 - 126 = 24\\)."),

    # 29
    ("If \\(S_n = n(4n + 1)\\), find the first three terms of the AP.",
     ["\\(5, 13, 21\\)", "\\(5, 9, 13\\)", "\\(4, 12, 20\\)", "\\(5, 14, 23\\)"],
     "A", "OSC", "medium",
     "\\(t_1 = S_1 = 1(5) = 5\\). \\(S_2 = 2(9) = 18 \\implies t_2 = S_2 - S_1 = 18 - 5 = 13\\). \\(d = 13 - 5 = 8\\). Thus \\(t_3 = 13 + 8 = 21\\). The terms are \\(5, 13, 21\\)."),

    # 30
    ("Find the sum of the first \\(100\\) positive integers.",
     ["\\(5050\\)", "\\(5000\\)", "\\(5100\\)", "\\(5025\\)"],
     "A", "OSC", "easy",
     "Using \\(S_n = \\frac{n(n + 1)}{2}\\): \\(S_{100} = \\frac{100 \\times 101}{2} = 5050\\)."),

    # 31
    ("Find the sum of all integers between \\(50\\) and \\(500\\) which are divisible by \\(7\\).",
     ["\\(17696\\)", "\\(17500\\)", "\\(17750\\)", "\\(18000\\)"],
     "A", "OSC", "hard",
     "First term is 56, last term is 497. \\(497 = 56 + (n - 1)7 \\implies 441 = 7(n - 1) \\implies n - 1 = 63 \\implies n = 64\\). \\(S_{64} = \\frac{64}{2}(56 + 497) = 32(553) = 17696\\)."),

    # 32
    ("The sum of the first \\(6\\) terms of an AP is \\(42\\). The ratio of its \\(10^{\\text{th}}\\) term to its \\(30^{\\text{th}}\\) term is \\(1 : 3\\). Calculate \\(t_1\\) and \\(t_{13}\\).",
     ["\\(t_1 = 2, t_{13} = 26\\)", "\\(t_1 = 1, t_{13} = 25\\)", "\\(t_1 = 2, t_{13} = 24\\)", "\\(t_1 = 3, t_{13} = 27\\)"],
     "A", "OSC", "hard",
     "\\(S_6 = \\frac{6}{2}[2a + 5d] = 3(2a + 5d) = 42 \\implies 2a + 5d = 14\\). Ratio: \\(\\frac{a + 9d}{a + 29d} = \\frac{1}{3} \\implies 3a + 27d = a + 29d \\implies 2a = 2d \\implies a = d\\). Substituting into \\(2a + 5d = 14 \\implies 7a = 14 \\implies a = 2, d = 2\\). Then \\(t_{13} = a + 12d = 2 + 24 = 26\\)."),

    # 33
    ("Find the sum of the first \\(16\\) terms of the AP: \\(10, 6, 2, \\dots\\)",
     ["\\(-320\\)", "\\(-300\\)", "\\(-340\\)", "\\(-280\\)"],
     "A", "OSC", "easy",
     "\\(a = 10, d = -4\\). \\(S_{16} = \\frac{16}{2}[20 + 15(-4)] = 8[20 - 60] = 8(-40) = -320\\)."),

    # 34
    ("In an AP, if \\(a = 1, t_n = 20\\) and \\(S_n = 399\\), find \\(n\\).",
     ["\\(38\\)", "\\(36\\)", "\\(40\\)", "\\(42\\)"],
     "A", "OSC", "easy",
     "\\(S_n = \\frac{n}{2}(a + t_n) \\implies 399 = \\frac{n}{2}(1 + 20) = \\frac{21n}{2} \\implies 21n = 798 \\implies n = 38\\)."),

    # 35
    ("What is the sum of the series \\(1 + 3 + 5 + \\dots + 99\\)?",
     ["\\(2500\\)", "\\(2400\\)", "\\(2600\\)", "\\(2450\\)"],
     "A", "OSC", "easy",
     "The odd numbers from 1 to 99 are \\(n = 50\\) terms. Sum \\(S_{50} = n^2 = 50^2 = 2500\\)."),

    # 36
    ("If \\(S_m = S_n\\) in an AP (with \\(m \\neq n\\)), what is the sum of the first \\(m + n\\) terms (\\(S_{m+n}\\))?",
     ["\\(0\\)", "\\(m + n\\)", "\\(mn\\)", "\\(1\\)"],
     "A", "OSC", "hard",
     "\\(\\frac{m}{2}[2a + (m-1)d] = \\frac{n}{2}[2a + (n-1)d] \\implies 2a(m - n) + d[m^2 - m - n^2 + n] = 0 \\implies (m - n)[2a + (m + n - 1)d] = 0\\). Since \\(m \\neq n\\), \\(2a + (m + n - 1)d = 0\\). Thus \\(S_{m+n} = \\frac{m+n}{2}[2a + (m+n-1)d] = 0\\)."),

    # 37
    ("The sum of first \\(n\\) terms of an AP is \\(5n^2 - 3n\\). Find the \\(10^{\\text{th}}\\) term.",
     ["\\(92\\)", "\\(95\\)", "\\(90\\)", "\\(88\\)"],
     "A", "OSC", "medium",
     "\\(t_n = S_n - S_{n-1} = 10n - 8\\). For \\(n = 10\\): \\(t_{10} = 10(10) - 8 = 92\\)."),

    # 38
    ("In an AP, \\(a = 3, n = 8, S_n = 192\\). Find \\(d\\).",
     ["\\(6\\)", "\\(4\\)", "\\(8\\)", "\\(5\\)"],
     "A", "OSC", "easy",
     "\\(192 = \\frac{8}{2}[2(3) + 7d] = 4[6 + 7d] \\implies 6 + 7d = 48 \\implies 7d = 42 \\implies d = 6\\)."),

    # 39
    ("Given \\(l = 28, S = 144\\), and there are total \\(9\\) terms. Find \\(a\\).",
     ["\\(4\\)", "\\(3\\)", "\\(5\\)", "\\(6\\)"],
     "A", "OSC", "easy",
     "\\(S_9 = \\frac{9}{2}(a + l) \\implies 144 = \\frac{9}{2}(a + 28) \\implies 16 = \\frac{a + 28}{2} \\implies a + 28 = 32 \\implies a = 4\\)."),

    # 40
    ("Find the sum of all two-digit odd positive integers.",
     ["\\(2475\\)", "\\(2500\\)", "\\(2450\\)", "\\(2400\\)"],
     "A", "OSC", "medium",
     "Two-digit odd integers are \\(11, 13, \\dots, 99\\). Total terms \\(= 45\\). \\(S_{45} = \\frac{45}{2}(11 + 99) = \\frac{45}{2}(110) = 45 \\times 55 = 2475\\).")
]

t33_prac = [
    # 41
    ("Find the sum of the first \\(22\\) terms of the AP: \\(8, 3, -2, \\dots\\)",
     ["\\(-979\\)", "\\(-989\\)", "\\(-969\\)", "\\(-959\\)"],
     "A", "OSC", "easy",
     "\\(a = 8, d = -5\\). \\(S_{22} = \\frac{22}{2}[16 + 21(-5)] = 11[16 - 105] = 11(-89) = -979\\)."),

    # 42
    ("If \\(S_n = 3n^2 + n\\), find the common difference \\(d\\).",
     ["\\(6\\)", "\\(3\\)", "\\(4\\)", "\\(2\\)"],
     "A", "OSC", "easy",
     "For \\(S_n = An^2 + Bn\\), the common difference is \\(2A\\). Here \\(A = 3\\), so \\(d = 2(3) = 6\\). (Verification: \\(S_1 = 4, S_2 = 14 \\implies t_1 = 4, t_2 = 10 \\implies d = 6\\))."),

    # 43
    ("Find the sum of the first \\(25\\) terms of the AP whose \\(n^{\\text{th}}\\) term is \\(t_n = 2 - 3n\\).",
     ["\\(-925\\)", "\\(-950\\)", "\\(-900\\)", "\\(-975\\)"],
     "A", "OSC", "medium",
     "\\(t_1 = 2 - 3 = -1\\). \\(t_{25} = 2 - 3(25) = -73\\). \\(S_{25} = \\frac{25}{2}[(-1) + (-73)] = \\frac{25}{2}(-74) = 25(-37) = -925\\)."),

    # 44
    ("Find the sum of all natural numbers between \\(250\\) and \\(1000\\) which are divisible by \\(3\\).",
     ["\\(156375\\)", "\\(156000\\)", "\\(156750\\)", "\\(155000\\)"],
     "A", "OSC", "hard",
     "First term is 252, last is 999. \\(999 = 252 + 3(n - 1) \\implies 747 = 3(n - 1) \\implies n = 250\\). \\(S_{250} = \\frac{250}{2}(252 + 999) = 125(1251) = 156375\\)."),

    # 45
    ("How many terms of the AP: \\(24, 21, 18, \\dots\\) must be taken so that their sum is \\(78\\)?",
     ["\\(4\\) or \\(13\\)", "\\(4\\) only", "\\(13\\) only", "\\(5\\) or \\(12\\)"],
     "A", "OSC", "hard",
     "\\(a = 24, d = -3\\). \\(S_n = \\frac{n}{2}[48 + (n - 1)(-3)] = 78 \\implies n(51 - 3n) = 156 \\implies 3n^2 - 51n + 156 = 0 \\implies n^2 - 17n + 52 = 0 \\implies (n - 4)(n - 13) = 0\\). Both 4 and 13 are valid (sum of terms from 5th to 13th is zero)."),

    # 46
    ("Find the sum of first \\(20\\) terms of an AP in which \\(d = 5\\) and \\(t_{20} = 100\\).",
     ["\\(1050\\)", "\\(1000\\)", "\\(1100\\)", "\\(950\\)"],
     "A", "OSC", "easy",
     "\\(t_{20} = a + 19(5) = 100 \\implies a + 95 = 100 \\implies a = 5\\). \\(S_{20} = \\frac{20}{2}(a + t_{20}) = 10(5 + 100) = 1050\\)."),

    # 47
    ("The sum of first \\(n\\) terms of an AP is given by \\(S_n = \\frac{3n^2 + 5n}{2}\\). Find the \\(15^{\\text{th}}\\) term.",
     ["\\(46\\)", "\\(44\\)", "\\(48\\)", "\\(50\\)"],
     "A", "OSC", "medium",
     "\\(S_n - S_{n-1} = 3n + 1\\). For \\(n = 15\\): \\(t_{15} = 3(15) + 1 = 46\\)."),

    # 48
    ("Find the sum of the first \\(30\\) natural numbers divisible by \\(6\\).",
     ["\\(2790\\)", "\\(2700\\)", "\\(2850\\)", "\\(2640\\)"],
     "A", "OSC", "easy",
     "Multiples are \\(6, 12, \\dots, 180\\). \\(S_{30} = \\frac{30}{2}(6 + 180) = 15 \\times 186 = 2790\\)."),

    # 49
    ("If \\(a = 5, d = 3, t_n = 50\\), find \\(S_n\\).",
     ["\\(440\\)", "\\(450\\)", "\\(430\\)", "\\(420\\)"],
     "A", "OSC", "easy",
     "\\(50 = 5 + 3(n - 1) \\implies n = 16\\). \\(S_{16} = \\frac{16}{2}(5 + 50) = 8(55) = 440\\)."),

    # 50
    ("Find the sum of first \\(40\\) positive integers divisible by \\(6\\).",
     ["\\(4920\\)", "\\(4800\\)", "\\(5040\\)", "\\(4900\\)"],
     "A", "OSC", "easy",
     "\\(S_{40} = \\frac{40}{2}[2(6) + 39(6)] = 20(6)(41) = 120 \\times 41 = 4920\\)."),

    # 51
    ("Sum of 3 consecutive terms of an AP is \\(33\\) and their product is \\(1155\\). Find the terms.",
     ["\\(7, 11, 15\\)", "\\(5, 11, 17\\)", "\\(9, 11, 13\\)", "\\(6, 11, 16\\)"],
     "A", "OSC", "medium",
     "Let terms be \\(a - d, a, a + d\\). Sum \\(= 3a = 33 \\implies a = 11\\). Product \\(= (11 - d)(11)(11 + d) = 1155 \\implies 121 - d^2 = 105 \\implies d^2 = 16 \\implies d = 4\\). Terms are \\(7, 11, 15\\)."),

    # 52
    ("Find the sum of the first \\(100\\) even natural numbers.",
     ["\\(10100\\)", "\\(10000\\)", "\\(10200\\)", "\\(10050\\)"],
     "A", "OSC", "easy",
     "\\(S_n = n(n + 1) = 100 \\times 101 = 10100\\)."),

    # 53
    ("Find the sum of the first \\(100\\) odd natural numbers.",
     ["\\(10000\\)", "\\(10100\\)", "\\(9900\\)", "\\(10200\\)"],
     "A", "OSC", "easy",
     "\\(S_n = n^2 = 100^2 = 10000\\)."),

    # 54
    ("Find the sum of all three-digit numbers which are divisible by \\(7\\).",
     ["\\(70336\\)", "\\(70000\\)", "\\(70500\\)", "\\(69800\\)"],
     "A", "OSC", "hard",
     "First is 105, last is 994. \\(994 = 105 + (n - 1)7 \\implies n = 128\\). \\(S_{128} = \\frac{128}{2}(105 + 994) = 64 \\times 1099 = 70336\\)."),

    # 55
    ("If the ratio of the sums of \\(m\\) and \\(n\\) terms of an AP is \\(m^2 : n^2\\), what is the ratio of their \\(m^{\\text{th}}\\) and \\(n^{\\text{th}}\\) terms?",
     ["\\((2m - 1) : (2n - 1)\\)", "\\(m : n\\)", "\\(m^2 : n^2\\)", "\\((m + 1) : (n + 1)\\)"],
     "A", "OSC", "hard",
     "Given \\(\\frac{S_m}{S_n} = \\frac{m^2}{n^2} \\implies \\frac{2a + (m - 1)d}{2a + (n - 1)d} = \\frac{m}{n}\\). Replacing \\(m\\) by \\(2m - 1\\) and \\(n\\) by \\(2n - 1\\) yields \\(\\frac{t_m}{t_n} = \\frac{2m - 1}{2n - 1}\\)."),

    # 56
    ("Sum of first \\(n\\) terms of an AP is \\(3n^2 + 4n\\). What is its first term \\(a\\)?",
     ["\\(7\\)", "\\(3\\)", "\\(4\\)", "\\(10\\)"],
     "A", "OSC", "easy",
     "\\(a = t_1 = S_1 = 3(1)^2 + 4(1) = 7\\)."),

    # 57
    ("Sum of first \\(n\\) terms of an AP is \\(2n^2 + 5n\\). Find its common difference \\(d\\).",
     ["\\(4\\)", "\\(2\\)", "\\(5\\)", "\\(7\\)"],
     "A", "OSC", "easy",
     "The coefficient of \\(n^2\\) is \\(d/2 = 2 \\implies d = 4\\)."),

    # 58
    ("In an AP, \\(a = 2, d = 8, S_n = 90\\). Find \\(n\\).",
     ["\\(5\\)", "\\(4\\)", "\\(6\\)", "\\(7\\)"],
     "A", "OSC", "medium",
     "\\(90 = \\frac{n}{2}[4 + (n - 1)8] = \\frac{n}{2}[8n - 4] = n(4n - 2) \\implies 4n^2 - 2n - 90 = 0 \\implies 2n^2 - n - 45 = 0 \\implies (2n + 9)(n - 5) = 0\\). Since \\(n \\in \\mathbb{N}\\), \\(n = 5\\)."),

    # 59
    ("Find the sum: \\(7 + 10\\frac{1}{2} + 14 + \\dots + 84\\).",
     ["\\(1046.5\\)", "\\(1050\\)", "\\(1040\\)", "\\(1045\\)"],
     "A", "OSC", "medium",
     "\\(a = 7, d = 3.5 = 7/2, t_n = 84\\). \\(84 = 7 + (n - 1)(7/2) \\implies 77 = (n - 1)(7/2) \\implies n - 1 = 22 \\implies n = 23\\). \\(S_{23} = \\frac{23}{2}(7 + 84) = \\frac{23 \\times 91}{2} = \\frac{2093}{2} = 1046.5\\)."),

    # 60
    ("In an AP, \\(t_n = 4, d = 2, S_n = -14\\). Find \\(n\\) and \\(a\\).",
     ["\\(n = 7, a = -8\\)", "\\(n = 6, a = -6\\)", "\\(n = 8, a = -10\\)", "\\(n = 7, a = -6\\)"],
     "A", "OSC", "hard",
     "\\(t_n = a + 2(n - 1) = 4 \\implies a = 6 - 2n\\). \\(S_n = \\frac{n}{2}(a + 4) = -14 \\implies n(6 - 2n + 4) = -28 \\implies n(10 - 2n) = -28 \\implies 2n^2 - 10n - 28 = 0 \\implies n^2 - 5n - 14 = 0 \\implies (n - 7)(n + 2) = 0\\). Since \\(n \\in \\mathbb{N}\\), \\(n = 7\\), and \\(a = 6 - 14 = -8\\)."),

    # 61
    ("Find the sum of the first \\(15\\) terms of the AP: \\(1/15, 1/12, 1/10, \\dots\\)",
     ["\\(33/20\\)", "\\(31/20\\)", "\\(7/4\\)", "\\(3/2\\)"],
     "A", "OSC", "medium",
     "\\(a = 1/15\\). \\(d = 1/12 - 1/15 = 1/60\\). \\(S_{15} = \\frac{15}{2}[2/15 + 14/60] = \\frac{15}{2}[8/60 + 14/60] = \\frac{15}{2}[22/60] = \\frac{15}{2} \\times \\frac{11}{30} = \\frac{11}{4} = 33/12\\) let's recompute: \\(15/2 \\times 22/60 = (15 \\times 11)/60 = 165/60 = 33/12 = 11/4\\). Let's fix options to 11/4, 9/4, 13/4, 5/2."),
]
t33_prac[-1] = (
    "Find the sum of the first \\(15\\) terms of the AP: \\(\\frac{1}{15}, \\frac{1}{12}, \\frac{1}{10}, \\dots\\)",
    ["\\(\\frac{11}{4}\\)", "\\(\\frac{9}{4}\\)", "\\(\\frac{13}{4}\\)", "\\(\\frac{5}{2}\\)"],
    "A", "OSC", "medium",
    "\\(a = 1/15, d = 1/12 - 1/15 = 1/60\\). \\(S_{15} = \\frac{15}{2}[2(1/15) + 14(1/60)] = \\frac{15}{2}[8/60 + 14/60] = \\frac{15}{2} \\times \\frac{22}{60} = \\frac{15 \\times 11}{60} = \\frac{11}{4}\\)."
)

t33_prac.extend([
    # 62
    ("What is the sum of the first \\(10\\) terms of the AP: \\(0.6, 1.7, 2.8, \\dots\\)?",
     ["\\(55.5\\)", "\\(55.0\\)", "\\(56.0\\)", "\\(54.5\\)"],
     "A", "OSC", "easy",
     "\\(a = 0.6, d = 1.1\\). \\(S_{10} = 5[2(0.6) + 9(1.1)] = 5[1.2 + 9.9] = 5(11.1) = 55.5\\)."),

    # 63
    ("If \\(S_n = 2n^2 + 3n\\), find \\(t_5\\).",
     ["\\(21\\)", "\\(19\\)", "\\(23\\)", "\\(25\\)"],
     "A", "OSC", "medium",
     "\\(t_n = S_n - S_{n-1} = 4n + 1\\). For \\(n = 5\\): \\(t_5 = 4(5) + 1 = 21\\)."),

    # 64
    ("Find the sum of first \\(20\\) terms of the AP: \\(1, 4, 7, 10, \\dots\\)",
     ["\\(590\\)", "\\(600\\)", "\\(580\\)", "\\(610\\)"],
     "A", "OSC", "easy",
     "\\(a = 1, d = 3\\). \\(S_{20} = 10[2 + 19(3)] = 10(59) = 590\\)."),

    # 65
    ("Sum of 5 consecutive terms of an AP is \\(65\\). What is the middle term?",
     ["\\(13\\)", "\\(15\\)", "\\(11\\)", "\\(12\\)"],
     "A", "OSC", "easy",
     "Let terms be \\(a - 2d, a - d, a, a + d, a + 2d\\). Sum \\(= 5a = 65 \\implies a = 13\\)."),

    # 66
    ("Sum of first \\(8\\) terms of an AP is \\(64\\) and sum of first \\(19\\) terms is \\(361\\). What is the sum of first \\(n\\) terms?",
     ["\\(n^2\\)", "\\(2n^2\\)", "\\(n(n+1)\\)", "\\(n^2 - n\\)"],
     "A", "OSC", "easy",
     "Notice \\(S_8 = 8^2 = 64\\) and \\(S_{19} = 19^2 = 361\\). Hence \\(S_n = n^2\\)."),

    # 67
    ("Find the sum: \\(2 + 4 + 6 + \\dots + 50\\).",
     ["\\(650\\)", "\\(625\\)", "\\(600\\)", "\\(675\\)"],
     "A", "OSC", "easy",
     "\\(n = 25\\). \\(S_{25} = 25 \\times 26 = 650\\)."),

    # 68
    ("If \\(t_1 = 5, t_{20} = 45\\), what is \\(S_{20}\\)?",
     ["\\(500\\)", "\\(450\\)", "\\(550\\)", "\\(400\\)"],
     "A", "OSC", "easy",
     "\\(S_{20} = \\frac{20}{2}(5 + 45) = 10 \\times 50 = 500\\)."),

    # 69
    ("Find the sum of all natural numbers from \\(1\\) to \\(50\\).",
     ["\\(1275\\)", "\\(1250\\)", "\\(1300\\)", "\\(1225\\)"],
     "A", "OSC", "easy",
     "\\(S_{50} = \\frac{50 \\times 51}{2} = 25 \\times 51 = 1275\\)."),

    # 70
    ("If \\(S_1, S_2, S_3\\) are the sums of \\(n, 2n, 3n\\) terms of an AP respectively, then which relation is always true?",
     ["\\(S_3 = 3(S_2 - S_1)\\)", "\\(S_3 = S_1 + S_2\\)", "\\(S_3 = 2(S_2 - S_1)\\)", "\\(S_3 = S_2 + 2S_1\\)"],
     "A", "OSC", "hard",
     "\\(S_2 - S_1 = \\frac{n}{2}[2a + (3n - 1)d]\\). Multiplying by 3 gives \\(\\frac{3n}{2}[2a + (3n - 1)d] = S_3\\). Thus \\(S_3 = 3(S_2 - S_1)\\).")
])

t33_mock = [
    # 71
    ("What does \\(S_n\\) represent in Arithmetic Progression?",
     ["The sum of the first \\(n\\) terms of the AP",
      "The value of the \\(n^{\\text{th}}\\) term",
      "The product of the first \\(n\\) terms",
      "The average of the terms"],
     "A", "OSC", "easy",
     "\\(S_n\\) denotes the sum of the first \\(n\\) terms of an arithmetic progression."),

    # 72
    ("What is the sum of the first \\(1\\) term of an AP?",
     ["\\(S_1 = t_1 = a\\)", "\\(0\\)", "\\(d\\)", "\\(2a\\)"],
     "A", "OSC", "easy",
     "The sum of the first 1 term is simply the first term itself: \\(S_1 = a\\)."),

    # 73
    ("If \\(S_n = \\frac{n}{2}[t_1 + t_n]\\), what does \\(t_n\\) represent?",
     ["The last or \\(n^{\\text{th}}\\) term of the sequence",
      "The total sum of all terms",
      "The common difference",
      "The total number of terms"],
     "A", "OSC", "easy",
     "\\(t_n\\) represents the \\(n^{\\text{th}}\\) term (last term in a finite series of \\(n\\) terms)."),

    # 74
    ("What is the sum of the first \\(3\\) natural numbers \\(1, 2, 3\\)?",
     ["\\(6\\)", "\\(5\\)", "\\(7\\)", "\\(4\\)"],
     "A", "OSC", "easy",
     "\\(1 + 2 + 3 = 6\\). Formula: \\(\\frac{3(4)}{2} = 6\\)."),

    # 75
    ("What is the sum of the first \\(2\\) terms of an AP with \\(a = 3\\) and \\(d = 4\\)?",
     ["\\(10\\)", "\\(7\\)", "\\(8\\)", "\\(11\\)"],
     "A", "OSC", "easy",
     "\\(t_1 = 3, t_2 = 7\\). \\(S_2 = 3 + 7 = 10\\)."),

    # 76
    ("If \\(S_3 = 15\\) and \\(S_2 = 9\\), what is the \\(3^{\\text{rd}}\\) term \\(t_3\\)?",
     ["\\(6\\)", "\\(5\\)", "\\(7\\)", "\\(4\\)"],
     "A", "OSC", "easy",
     "\\(t_3 = S_3 - S_2 = 15 - 9 = 6\\)."),

    # 77
    ("What is the sum of the first \\(4\\) odd numbers \\(1, 3, 5, 7\\)?",
     ["\\(16\\)", "\\(12\\)", "\\(20\\)", "\\(14\\)"],
     "A", "OSC", "easy",
     "Using \\(n^2\\) for \\(n = 4\\): \\(4^2 = 16\\)."),

    # 78
    ("What is the sum of the first \\(3\\) even numbers \\(2, 4, 6\\)?",
     ["\\(12\\)", "\\(10\\)", "\\(14\\)", "\\(16\\)"],
     "A", "OSC", "easy",
     "Using \\(n(n+1)\\) for \\(n = 3\\): \\(3 \\times 4 = 12\\)."),

    # 79
    ("If all terms of an AP are \\(5\\) (i.e. \\(d = 0\\)), what is the sum of the first \\(10\\) terms?",
     ["\\(50\\)", "\\(5\\)", "\\(25\\)", "\\(100\\)"],
     "A", "OSC", "easy",
     "When each term is 5, \\(S_{10} = 10 \\times 5 = 50\\)."),

    # 80
    ("Can \\(S_n\\), the sum of an AP, be negative?",
     ["Yes, when terms are negative or the sum of negative terms dominates",
      "No, a sum can never be negative",
      "Only if the first term is zero",
      "Only for geometric progressions"],
     "A", "OSC", "easy",
     "A sum of terms can certainly be negative, for example \\(-5 + (-8) + (-11) = -24\\)."),

    # 81
    ("What is the value of \\(S_2\\) if \\(t_1 = -4\\) and \\(t_2 = 4\\)?",
     ["\\(0\\)", "\\(8\\)", "\\(-8\\)", "\\(4\\)"],
     "A", "OSC", "easy",
     "\\(S_2 = t_1 + t_2 = -4 + 4 = 0\\)."),

    # 82
    ("Which mathematician is famously credited with quickly summing the numbers from \\(1\\) to \\(100\\) in grade school?",
     ["Carl Friedrich Gauss", "Leonhard Euler", "Isaac Newton", "Euclid"],
     "A", "OSC", "easy",
     "Carl Friedrich Gauss famously discovered the pairing method \\((1 + 100) \\times 50 = 5050\\) as a young schoolboy.")
]

if __name__ == "__main__":
    topic_code = "MH-10-MTH1-3-3.3"
    all_qs = build_topic_questions(topic_code, t33_exam, t33_prac, t33_mock)
    out_path = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch3_t3.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {topic_code} -> {out_path}")
