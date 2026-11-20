# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-7-7.5
Topic: Sharing Quantities in a Given Ratio
Subtopic 7.5.1: Dividing total amounts into parts proportional to ratio
Subtopic 7.5.2: Difference between parts, ratio comparisons and multi-way sharing
Vaults: 40 Exam (001-040) + 30 Practice (041-070) + 12 Foundation (071-082)
"""

import json
import os

PARENT_TOPIC_CODE = "CBSE-8-MGP1-7-7.5"
PARENT_TOPIC_NAME = "Sharing Quantities in a Given Ratio"
CH_NUM = 7
SUB1_CODE = "CBSE-8-MGP1-7-7.5.1"
SUB1_NAME = "Dividing total amounts into parts proportional to ratio"
SUB2_CODE = "CBSE-8-MGP1-7-7.5.2"
SUB2_NAME = "Difference between parts, ratio comparisons and multi-way sharing"

def make_q(seq, sub_code, sub_name, text, options, answer_letter, qtype, difficulty, vault, category, explanation):
    qnum_str = f"{seq:03d}"
    doc_id = f"CBSE-8-MGP1-7-7.5-{qtype}-{qnum_str}"
    qcode = f"{sub_code}-{qtype}-{qnum_str}"
    return {
        "id": doc_id,
        "questionCode": qcode,
        "chapterNumber": CH_NUM,
        "class": "8",
        "subjectCode": "MGP1",
        "boardCode": "CBSE",
        "board": "CBSE",
        "subject": "Ganit Prakash Part 1",
        "topicCode": sub_code,
        "parentTopicCode": PARENT_TOPIC_CODE,
        "parentTopicName": PARENT_TOPIC_NAME,
        "subtopicCode": sub_code,
        "subtopicName": sub_name,
        "topicNumber": sub_code.split("-")[-1],
        "type": qtype,
        "difficulty": difficulty,
        "bloomLevel": "Apply" if difficulty == "medium" else ("Analyze" if difficulty == "hard" else "Understand"),
        "vault": vault,
        "examCategory": category,
        "marks": 4,
        "text": text,
        "options": options,
        "correctAnswer": answer_letter,
        "solution": explanation,
        "explanation": explanation,
        "status": "active"
    }

questions = []

# =========================================================================
# EXAM VAULT: Questions 001 - 040 (20 for 7.5.1, 20 for 7.5.2)
# =========================================================================

sub1_exam = [
    (1, r"Divide \(₹1200\) between Ananya and Rohit in the ratio \(3 : 5\). How much does Ananya receive?",
     [r"\(₹450\)", r"\(₹750\)", r"\(₹400\)", r"\(₹500\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nTotal parts \(= 3 + 5 = 8\).\nValue of 1 part \(= \frac{1200}{8} = ₹150\).\nAnanya's share \(= 3 \times 150 = ₹450\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹450\)."),

    (2, r"A piece of wire of length \(84\text{ cm}\) is cut into two pieces in the ratio \(2 : 5\). What is the length of the longer piece?",
     [r"\(60\text{ cm}\)", r"\(24\text{ cm}\)", r"\(56\text{ cm}\)", r"\(50\text{ cm}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nTotal parts \(= 2 + 5 = 7\).\nLength per part \(= \frac{84}{7} = 12\text{ cm}\).\nLonger piece \(= 5 \times 12 = 60\text{ cm}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(60\text{ cm}\)."),

    (3, r"Two partners A and B invest capital in the ratio \(4 : 7\). If the total annual profit is \(₹44{,}000\), what is B's profit share?",
     [r"\(₹28{,}000\)", r"\(₹16{,}000\)", r"\(₹24{,}000\)", r"\(₹30{,}000\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nB's share \(= \frac{7}{4+7} \times 44{,}000 = \frac{7}{11} \times 44{,}000 = 7 \times 4000 = ₹28{,}000\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹28{,}000\)."),

    (4, r"Divide 60 sweets among three children X, Y, and Z in the ratio \(1 : 2 : 3\). How many sweets does Y receive?",
     [r"\(20\)", r"\(10\)", r"\(30\)", r"\(15\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nTotal parts \(= 1 + 2 + 3 = 6\).\nY's share \(= \frac{2}{6} \times 60 = 20\text{ sweets}\).\n\n### 2. Option Analysis:\n- Option A is correct: 20."),

    (5, r"A line segment of length \(36\text{ cm}\) is divided internally in the ratio \(4 : 5\). Find the lengths of the two segments.",
     [r"\(16\text{ cm}\) and \(20\text{ cm}\)", r"\(12\text{ cm}\) and \(24\text{ cm}\)", r"\(15\text{ cm}\) and \(21\text{ cm}\)", r"\(18\text{ cm}\) and \(18\text{ cm}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nTotal parts \(= 9\). Each part \(= 4\text{ cm}\).\nSegments are \(4 \times 4 = 16\text{ cm}\) and \(5 \times 4 = 20\text{ cm}\).\n\n### 2. Option Analysis:\n- Option A is correct."),

    (6, r"A prize money of \(₹10{,}000\) is shared among first, second, and third place winners in the ratio \(5 : 3 : 2\). What is the third prize?",
     [r"\(₹2000\)", r"\(₹3000\)", r"\(₹5000\)", r"\(₹1500\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nThird prize \(= \frac{2}{10} \times 10{,}000 = ₹2000\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹2000\)."),

    (7, r"The angles of a triangle are in the ratio \(2 : 3 : 4\). Find the measure of the smallest angle.",
     [r"\(40^\circ\)", r"\(60^\circ\)", r"\(80^\circ\)", r"\(30^\circ\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nSum of angles \(= 180^\circ\). Total parts \(= 2 + 3 + 4 = 9\).\nSmallest angle \(= \frac{2}{9} \times 180^\circ = 40^\circ\).\n\n### 2. Option Analysis:\n- Option A is correct: \(40^\circ\)."),

    (8, r"Divide \(105\text{ kg}\) of wheat between two families in the ratio \(3 : 4\). How much wheat does the second family get?",
     [r"\(60\text{ kg}\)", r"\(45\text{ kg}\)", r"\(55\text{ kg}\)", r"\(70\text{ kg}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nSecond family \(= \frac{4}{7} \times 105 = 4 \times 15 = 60\text{ kg}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(60\text{ kg}\)."),

    (9, r"A sum of \(₹3600\) is divided among A, B, and C such that A gets \(\frac{1}{3}\) of the total, and the rest is divided between B and C in the ratio \(3 : 5\). How much does B receive?",
     [r"\(₹900\)", r"\(₹1500\)", r"\(₹1200\)", r"\(₹1000\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nA's share \(= \frac{1}{3} \times 3600 = ₹1200\).\nRemaining \(= 3600 - 1200 = ₹2400\).\nB's share \(= \frac{3}{3+5} \times 2400 = \frac{3}{8} \times 2400 = ₹900\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹900\)."),

    (10, r"The perimeter of a triangle is \(72\text{ cm}\) and its sides are in the ratio \(3 : 4 : 5\). What is the length of the longest side?",
     [r"\(30\text{ cm}\)", r"\(24\text{ cm}\)", r"\(18\text{ cm}\)", r"\(36\text{ cm}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nTotal parts \(= 3 + 4 + 5 = 12\).\nLongest side \(= \frac{5}{12} \times 72 = 30\text{ cm}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(30\text{ cm}\)."),

    (11, r"Divide \(₹5600\) among P, Q, and R in the ratio \(\frac{1}{2} : \frac{1}{3} : \frac{1}{4}\). How much does P receive?",
     [r"\(₹2584.62\)", r"\(₹2400\)", r"\(₹2800\)", r"\(₹2600\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nConvert to integer ratio by multiplying by 12: \(6 : 4 : 3\).\nTotal parts \(= 13\). If total is \(₹5200\), P gets \(₹2400\). Let's use total \(₹5200\) for clean integer answers! Options: [₹2400, ₹1600, ₹1200, ₹2000]."),

    (12, r"A wooden plank of length \(2.4\text{ m}\) is divided in the ratio \(3 : 5\). Find the length of the shorter piece in centimeters.",
     [r"\(90\text{ cm}\)", r"\(150\text{ cm}\)", r"\(80\text{ cm}\)", r"\(100\text{ cm}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(2.4\text{ m} = 240\text{ cm}\).\nShorter piece \(= \frac{3}{8} \times 240 = 90\text{ cm}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(90\text{ cm}\)."),

    (13, r"In an election, 1200 votes were polled for two candidates in the ratio \(7 : 5\). By how many votes did the winning candidate win?",
     [r"\(200\text{ votes}\)", r"\(100\text{ votes}\)", r"\(300\text{ votes}\)", r"\(150\text{ votes}\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nWinner gets \(7x\), loser gets \(5x\). Total \(= 12x = 1200 \implies x = 100\).\nDifference \(= 7x - 5x = 2x = 2 \times 100 = 200\text{ votes}\).\n\n### 2. Option Analysis:\n- Option A is correct: 200."),

    (14, r"Two numbers are in the ratio \(4 : 9\). If their sum is 91, find the smaller number.",
     [r"\(28\)", r"\(63\)", r"\(36\)", r"\(24\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(4x + 9x = 13x = 91 \implies x = 7\).\nSmaller number \(= 4 \times 7 = 28\).\n\n### 2. Option Analysis:\n- Option A is correct: 28."),

    (15, r"Divide 150 marbles among three friends in the ratio \(2 : 3 : 5\). What is the difference between the largest and smallest shares?",
     [r"\(45\)", r"\(30\)", r"\(60\)", r"\(50\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nTotal parts \(= 10\). One part \(= 15\).\nDifference \(= (5 - 2) \times 15 = 3 \times 15 = 45\).\n\n### 2. Option Analysis:\n- Option A is correct: 45."),

    (16, r"A legacy of \(₹90{,}000\) is divided among a widow, son, and daughter in the ratio \(4 : 3 : 2\). How much does the daughter receive?",
     [r"\(₹20{,}000\)", r"\(₹30{,}000\)", r"\(₹40{,}000\)", r"\(₹25{,}000\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nDaughter's share \(= \frac{2}{9} \times 90{,}000 = ₹20{,}000\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹20{,}000\)."),

    (17, r"The ratio of boys to girls in a school of 720 students is \(7 : 5\). How many more boys are there than girls?",
     [r"\(120\)", r"\(100\)", r"\(80\)", r"\(150\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nTotal parts \(= 12\). One part \(= \frac{720}{12} = 60\).\nDifference \(= (7 - 5) \times 60 = 2 \times 60 = 120\).\n\n### 2. Option Analysis:\n- Option A is correct: 120."),

    (18, r"Divide \(₹750\) into two parts such that the first part is \(\frac{2}{3}\) of the second part.",
     [r"\(₹300\) and \(₹450\)", r"\(₹250\) and \(₹500\)", r"\(₹350\) and \(₹400\)", r"\(₹200\) and \(₹550\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nRatio is \(2 : 3\). Total parts \(= 5\).\nParts are \(\frac{2}{5} \times 750 = ₹300\) and \(\frac{3}{5} \times 750 = ₹450\).\n\n### 2. Option Analysis:\n- Option A is correct."),

    (19, r"Three angles of a quadrilateral are in the ratio \(1 : 2 : 3\) and the fourth angle is \(120^\circ\). Find the measure of the largest of the first three angles.",
     [r"\(120^\circ\)", r"\(80^\circ\)", r"\(40^\circ\)", r"\(100^\circ\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nSum of angles \(= 360^\circ\). Sum of three angles \(= 360^\circ - 120^\circ = 240^\circ\).\nTotal parts \(= 1 + 2 + 3 = 6\).\nLargest of the three \(= \frac{3}{6} \times 240^\circ = 120^\circ\).\n\n### 2. Option Analysis:\n- Option A is correct: \(120^\circ\)."),

    (20, r"Divide \(₹4500\) among A, B, and C in the ratio \(2 : 3 : 4\). What is B's share?",
     [r"\(₹1500\)", r"\(₹1000\)", r"\(₹2000\)", r"\(₹1200\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nTotal parts \(= 9\). B's share \(= \frac{3}{9} \times 4500 = ₹1500\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹1500\).")
]

# Adjust 11
sub1_exam[10] = (11, r"Divide \(₹5200\) among P, Q, and R in the ratio \(\frac{1}{2} : \frac{1}{3} : \frac{1}{4}\). How much does P receive?",
     [r"\(₹2400\)", r"\(₹1600\)", r"\(₹1200\)", r"\(₹2000\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nMultiply by 12: \(6 : 4 : 3\). Total parts \(= 13\).\nP's share \(= \frac{6}{13} \times 5200 = 6 \times 400 = ₹2400\).")

for seq, text, opts, ans, qtype, diff, exp in sub1_exam:
    questions.append(make_q(seq, SUB1_CODE, SUB1_NAME, text, opts, ans, qtype, diff, "exam", "standard", exp))

# --- SUBTOPIC 7.5.2: Difference Between Parts & Multi-way Sharing (021 - 040) ---
sub2_exam = [
    (21, r"The ratio of the incomes of two persons is \(9 : 7\) and the difference between their incomes is \(₹6000\). What is the income of the higher earner?",
     [r"\(₹27{,}000\)", r"\(₹21{,}000\)", r"\(₹36{,}000\)", r"\(₹18{,}000\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(9x - 7x = 2x = 6000 \implies x = 3000\).\nHigher income \(= 9 \times 3000 = ₹27{,}000\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹27{,}000\)."),

    (22, r"Two numbers are in the ratio \(5 : 8\). If the larger number exceeds the smaller number by 45, what is the sum of the two numbers?",
     [r"\(195\)", r"\(180\)", r"\(205\)", r"\(175\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\n\(8x - 5x = 3x = 45 \implies x = 15\).\nSum \(= (5 + 8) \times 15 = 13 \times 15 = 195\).\n\n### 2. Option Analysis:\n- Option A is correct: 195."),

    (23, r"A sum of money is divided among A, B, and C in the ratio \(2 : 3 : 7\). If B receives \(₹1500\), what is the total sum of money divided?",
     [r"\(₹6000\)", r"\(₹5500\)", r"\(₹7000\)", r"\(₹4500\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(3x = 1500 \implies x = 500\).\nTotal sum \(= (2 + 3 + 7) \times 500 = 12 \times 500 = ₹6000\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹6000\)."),

    (24, r"In a partnership, A, B, and C invest in the ratio \(3 : 4 : 5\). If C's share of the annual profit exceeds A's share by \(₹8000\), what is the total profit?",
     [r"\(₹48{,}000\)", r"\(₹40{,}000\)", r"\(₹54{,}000\)", r"\(₹36{,}000\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nDifference between C and A \(= 5x - 3x = 2x = 8000 \implies x = 4000\).\nTotal profit \(= (3 + 4 + 5) \times 4000 = 12 \times 4000 = ₹48{,}000\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹48{,}000\)."),

    (25, r"A sum of \(₹735\) is divided between A, B, and C such that if each of their shares is reduced by \(₹5\), the remainder is in the ratio \(1 : 3 : 2\). What was B's original share?",
     [r"\(₹365\)", r"\(₹360\)", r"\(₹245\)", r"\(₹125\)"], "A", "OSC", "hard",
     r"### 1. Mathematical Concept & Principle:\nTotal reduction \(= 3 \times 5 = ₹15\).\nRemaining sum \(= 735 - 15 = ₹720\).\nTotal parts \(= 1 + 3 + 2 = 6\). One part \(= \frac{720}{6} = ₹120\).\nB's reduced share \(= 3 \times 120 = ₹360\).\nB's original share \(= 360 + 5 = ₹365\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹365\)."),

    (26, r"The ratio of the ages of two brothers is \(4 : 3\) and the difference between their ages is 5 years. What is the age of the elder brother?",
     [r"\(20\text{ years}\)", r"\(25\text{ years}\)", r"\(15\text{ years}\)", r"\(24\text{ years}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(4x - 3x = x = 5\).\nElder brother \(= 4 \times 5 = 20\text{ years}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(20\text{ years}\)."),

    (27, r"If \(₹840\) is divided among three persons such that the second gets twice as much as the first, and the third gets twice as much as the second, how much does the third person get?",
     [r"\(₹480\)", r"\(₹240\)", r"\(₹120\)", r"\(₹360\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nLet first be \(x\), second be \(2x\), third be \(4x\).\nTotal \(= x + 2x + 4x = 7x = 840 \implies x = 120\).\nThird person gets \(4 \times 120 = ₹480\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹480\)."),

    (28, r"Two numbers are in the ratio \(3 : 5\). If each number is increased by 10, the ratio becomes \(5 : 7\). What is the difference between the original numbers?",
     [r"\(10\)", r"\(15\)", r"\(20\)", r"\(8\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{3x+10}{5x+10} = \frac{5}{7} \implies 21x + 70 = 25x + 50 \implies 4x = 20 \implies x = 5\).\nDifference \(= 5x - 3x = 2x = 2 \times 5 = 10\).\n\n### 2. Option Analysis:\n- Option A is correct: 10."),

    (29, r"A copper-zinc alloy of \(40\text{ kg}\) has copper and zinc in the ratio \(5 : 3\). How much copper must be added so that the ratio becomes \(2 : 1\)?",
     [r"\(5\text{ kg}\)", r"\(4\text{ kg}\)", r"\(6\text{ kg}\)", r"\(8\text{ kg}\)"], "A", "OSC", "hard",
     r"### 1. Mathematical Concept & Principle:\nCopper \(= \frac{5}{8} \times 40 = 25\text{ kg}\), Zinc \(= 15\text{ kg}\).\nLet added copper be \(c\):\n\(\frac{25+c}{15} = \frac{2}{1} \implies 25 + c = 30 \implies c = 5\text{ kg}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(5\text{ kg}\)."),

    (30, r"Divide \(₹1870\) into three parts such that half of the first part, one-third of the second part, and one-sixth of the third part are equal. What is the third part?",
     [r"\(₹1020\)", r"\(₹510\)", r"\(₹340\)", r"\(₹850\)"], "A", "OSC", "hard",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{A}{2} = \frac{B}{3} = \frac{C}{6} = k \implies A = 2k, B = 3k, C = 6k\).\nTotal \(= 2k + 3k + 6k = 11k = 1870 \implies k = 170\).\nThird part \(C = 6 \times 170 = ₹1020\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹1020\)."),

    (31, r"In a bag containing red, blue, and green balls in the ratio \(4 : 7 : 9\), there are 25 more green balls than red balls. How many blue balls are in the bag?",
     [r"\(35\)", r"\(28\)", r"\(45\)", r"\(40\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\n\(9x - 4x = 5x = 25 \implies x = 5\).\nBlue balls \(= 7 \times 5 = 35\).\n\n### 2. Option Analysis:\n- Option A is correct: 35."),

    (32, r"Three numbers are in the ratio \(1 : 2 : 3\) and the sum of their squares is 504. Find the largest number.",
     [r"\(18\)", r"\(12\)", r"\(6\)", r"\(24\)"], "A", "OSC", "hard",
     r"### 1. Mathematical Concept & Principle:\n\(x^2 + (2x)^2 + (3x)^2 = x^2 + 4x^2 + 9x^2 = 14x^2 = 504\).\n\(x^2 = \frac{504}{14} = 36 \implies x = 6\).\nLargest number \(= 3x = 3 \times 6 = 18\).\n\n### 2. Option Analysis:\n- Option A is correct: 18."),

    (33, r"A father wishes to divide \(₹77{,}000\) between his son and daughter in the ratio of their ages, which are 12 and 10 years respectively. How much does the son receive?",
     [r"\(₹42{,}000\)", r"\(₹35{,}000\)", r"\(₹40{,}000\)", r"\(₹38{,}500\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nRatio \(= 12 : 10 = 6 : 5\). Total parts \(= 11\).\nSon's share \(= \frac{6}{11} \times 77{,}000 = 6 \times 7000 = ₹42{,}000\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹42{,}000\)."),

    # 34: OAR
    (34, r"Assertion (A): When a sum is divided in the ratio \(a : b\), the ratio of the two shares is always strictly equal to \(a : b\).\nReason (R): Multiplying both terms of a ratio by the common multiplier \(x = \frac{\text{Total}}{a+b}\) scales both parts equally.",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"], "A", "OAR", "easy",
     r"### 1. Mathematical Concept & Principle:\nSharing in ratio \(a : b\) gives shares \(ax\) and \(bx\). The ratio \(\frac{ax}{bx} = \frac{a}{b}\). Both statements are true and (R) explains (A).\n\n### 2. Option Analysis:\n- Option A is correct."),

    # 35: OAR
    (35, r"Assertion (A): If the ratio of two positive numbers is \(3 : 5\) and their difference is 14, then their sum is 56.\nReason (R): If \(ax\) and \(bx\) are the numbers, their difference is \((b-a)x\) and their sum is \((a+b)x\).",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"], "A", "OAR", "medium",
     r"### 1. Mathematical Concept & Principle:\n\(5x - 3x = 2x = 14 \implies x = 7\). Sum \(= (3+5) \times 7 = 56\). Both statements are true and (R) correctly explains (A).\n\n### 2. Option Analysis:\n- Option A is correct."),

    # 36: OTF
    (36, r"True or False: If a quantity \(Q\) is divided in the ratio \(a : b : c\), the share of the first part is \(\frac{a}{a+b+c} \times Q\).",
     ["True", "False"], "A", "OTF", "easy",
     r"This is the exact mathematical formula for multi-way sharing. True."),

    (37, r"True or False: Dividing a sum in the ratio \(2 : 3\) gives the same result as dividing it in the ratio \(4 : 6\).",
     ["True", "False"], "A", "OTF", "easy",
     r"Equivalent ratios produce identical individual shares since \(\frac{2}{2+3} = \frac{4}{4+6} = \frac{2}{5}\). True."),

    # 38: OFB
    (38, r"Divide \(₹900\) in the ratio \(4 : 5\). The smaller share is ₹ _____.",
     [r"\(400\)", r"\(500\)", r"\(450\)", r"\(350\)"], "A", "OFB", "easy",
     r"Smaller share \(= \frac{4}{9} \times 900 = ₹400\)."),

    # 39: OFB
    (39, r"If \(₹1500\) is divided between A and B in the ratio \(2 : 3\), the difference between their shares is ₹ _____.",
     [r"\(300\)", r"\(200\)", r"\(250\)", r"\(150\)"], "A", "OFB", "easy",
     r"Difference \(= \frac{3-2}{5} \times 1500 = \frac{1}{5} \times 1500 = ₹300\)."),

    # 40: ONE
    (40, r"Two numbers are in the ratio \(5 : 7\). If their sum is 144, determine the numerical value of the smaller number.",
     [r"\(60\)", r"\(84\)", r"\(72\)", r"\(50\)"], "A", "ONE", "easy",
     r"\(12x = 144 \implies x = 12\). Smaller number \(= 5 \times 12 = 60\).")
]

for seq, text, opts, ans, qtype, diff, exp in sub2_exam:
    questions.append(make_q(seq, SUB2_CODE, SUB2_NAME, text, opts, ans, qtype, diff, "exam", "standard", exp))

# =========================================================================
# PRACTICE VAULT: Questions 041 - 070 (15 for 7.5.1, 15 for 7.5.2)
# =========================================================================

sub1_practice = [
    (41, r"Divide \(₹800\) between Sita and Geeta in the ratio \(3 : 2\). How much does Sita get?",
     [r"\(₹480\)", r"\(₹320\)", r"\(₹400\)", r"\(₹500\)"], "A", "OSC", "easy",
     r"Sita \(= \frac{3}{5} \times 800 = ₹480\)."),

    (42, r"A wooden stick of length \(1.2\text{ m}\) is broken in the ratio \(1 : 3\). Find the length of the shorter piece in centimeters.",
     [r"\(30\text{ cm}\)", r"\(40\text{ cm}\)", r"\(90\text{ cm}\)", r"\(25\text{ cm}\)"], "A", "OSC", "easy",
     r"\(1.2\text{ m} = 120\text{ cm}\). Shorter \(= \frac{1}{4} \times 120 = 30\text{ cm}\)."),

    (43, r"Divide 84 toffees among three friends in the ratio \(1 : 2 : 4\). What is the largest share?",
     [r"\(48\)", r"\(36\)", r"\(42\)", r"\(56\)"], "A", "OSC", "easy",
     r"Total parts \(= 7\). Largest share \(= \frac{4}{7} \times 84 = 48\)."),

    (44, r"A line segment of \(45\text{ cm}\) is divided into two parts in the ratio \(4 : 5\). What is the length of the shorter part?",
     [r"\(20\text{ cm}\)", r"\(25\text{ cm}\)", r"\(15\text{ cm}\)", r"\(18\text{ cm}\)"], "A", "OSC", "easy",
     r"Shorter part \(= \frac{4}{9} \times 45 = 20\text{ cm}\)."),

    (45, r"Two angles in a linear pair are in the ratio \(2 : 3\). Find the measure of the smaller angle.",
     [r"\(72^\circ\)", r"\(108^\circ\)", r"\(60^\circ\)", r"\(90^\circ\)"], "A", "OSC", "easy",
     r"Linear pair sum \(= 180^\circ\). Smaller angle \(= \frac{2}{5} \times 180^\circ = 72^\circ\)."),

    (46, r"Two complementary angles are in the ratio \(7 : 8\). What is the larger angle?",
     [r"\(48^\circ\)", r"\(42^\circ\)", r"\(50^\circ\)", r"\(45^\circ\)"], "A", "OSC", "easy",
     r"Complementary sum \(= 90^\circ\). Larger angle \(= \frac{8}{15} \times 90^\circ = 48^\circ\)."),

    (47, r"Divide \(₹2100\) among A, B, and C in the ratio \(2 : 3 : 5\). What is C's share?",
     [r"\(₹1050\)", r"\(₹630\)", r"\(₹420\)", r"\(₹900\)"], "A", "OSC", "easy",
     r"C's share \(= \frac{5}{10} \times 2100 = ₹1050\)."),

    (48, r"A rope \(60\text{ m}\) long is divided into three pieces in the ratio \(3 : 4 : 5\). What is the length of the middle piece?",
     [r"\(20\text{ m}\)", r"\(15\text{ m}\)", r"\(25\text{ m}\)", r"\(18\text{ m}\)"], "A", "OSC", "easy",
     r"Total parts \(= 12\). Middle piece \(= \frac{4}{12} \times 60 = 20\text{ m}\)."),

    (49, r"In a class of 45 students, the ratio of boys to girls is \(4 : 5\). How many girls are in the class?",
     [r"\(25\)", r"\(20\)", r"\(24\)", r"\(27\)"], "A", "OSC", "easy",
     r"Girls \(= \frac{5}{9} \times 45 = 25\)."),

    (50, r"Divide \(120\text{ kg}\) of flour between two bakers in the ratio \(5 : 7\). How much does the first baker get?",
     [r"\(50\text{ kg}\)", r"\(70\text{ kg}\)", r"\(60\text{ kg}\)", r"\(45\text{ kg}\)"], "A", "OSC", "easy",
     r"First baker \(= \frac{5}{12} \times 120 = 50\text{ kg}\)."),

    (51, r"The angles of a triangle are in the ratio \(1 : 2 : 3\). What type of triangle is it?",
     [r"Right-angled triangle", r"Equilateral triangle", r"Isosceles triangle", r"Obtuse-angled triangle"], "A", "OSC", "medium",
     r"Angles are \(\frac{1}{6} \times 180 = 30^\circ\), \(60^\circ\), and \(90^\circ\). It is a right-angled triangle."),

    (52, r"Divide \(₹3500\) between A and B in the ratio \(3 : 4\). Find the share of B.",
     [r"\(₹2000\)", r"\(₹1500\)", r"\(₹1800\)", r"\(₹2100\)"], "A", "OSC", "easy",
     r"B's share \(= \frac{4}{7} \times 3500 = ₹2000\)."),

    (53, r"A prize of \(₹5000\) is divided between two winners in the ratio \(3 : 7\). How much does the second winner get?",
     [r"\(₹3500\)", r"\(₹1500\)", r"\(₹3000\)", r"\(₹4000\)"], "A", "OSC", "easy",
     r"Second winner \(= \frac{7}{10} \times 5000 = ₹3500\)."),

    (54, r"True or False: If a sum is divided into three parts in the ratio \(1 : 1 : 1\), all three parts are equal.",
     ["True", "False"], "A", "OTF", "easy",
     r"Equal ratio terms represent identical equal division. True."),

    (55, r"Divide \(₹600\) in the ratio \(2 : 3\). The larger share is ₹ _____.",
     [r"\(360\)", r"\(240\)", r"\(300\)", r"\(400\)"], "A", "OFB", "easy",
     r"Larger share \(= \frac{3}{5} \times 600 = ₹360\).")
]

for seq, text, opts, ans, qtype, diff, exp in sub1_practice:
    questions.append(make_q(seq, SUB1_CODE, SUB1_NAME, text, opts, ans, qtype, diff, "practice", "standard", exp))

# --- 7.5.2 Practice (056 - 070) ---
sub2_practice = [
    (56, r"Two numbers are in the ratio \(7 : 10\) and their difference is 24. Find the smaller number.",
     [r"\(56\)", r"\(80\)", r"\(70\)", r"\(48\)"], "A", "OSC", "easy",
     r"\(10x - 7x = 3x = 24 \implies x = 8\). Smaller number \(= 7 \times 8 = 56\)."),

    (57, r"The ratio of the perimeter to the breadth of a rectangle is \(5 : 1\). If the area of the rectangle is \(216\text{ cm}^2\), what is the length of the rectangle?",
     [r"\(18\text{ cm}\)", r"\(12\text{ cm}\)", r"\(15\text{ cm}\)", r"\(24\text{ cm}\)"], "A", "OSC", "hard",
     r"\(\frac{2(L+B)}{B} = 5 \implies 2L + 2B = 5B \implies 2L = 3B \implies \frac{L}{B} = \frac{3}{2}\).\nLet \(L = 3x, B = 2x\). Area \(= 6x^2 = 216 \implies x^2 = 36 \implies x = 6\).\nLength \(L = 3 \times 6 = 18\text{ cm}\)."),

    (58, r"A sum is divided among X, Y, and Z in the ratio \(4 : 7 : 9\). If Y's share is \(₹2800\), what is the difference between Z's share and X's share?",
     [r"\(₹2000\)", r"\(₹1800\)", r"\(₹2400\)", r"\(₹1600\)"], "A", "OSC", "medium",
     r"\(7x = 2800 \implies x = 400\).\nDifference \(Z - X = (9 - 4) \times 400 = 5 \times 400 = ₹2000\)."),

    (59, r"Two numbers are in the ratio \(3 : 4\). If 5 is added to each number, the ratio becomes \(4 : 5\). Find the sum of the two original numbers.",
     [r"\(35\)", r"\(42\)", r"\(28\)", r"\(49\)"], "A", "OSC", "medium",
     r"\(\frac{3x+5}{4x+5} = \frac{4}{5} \implies 15x + 25 = 16x + 20 \implies x = 5\).\nSum \(= (3+4) \times 5 = 35\)."),

    (60, r"In a mix of red and white marbles, the ratio of red to white is \(5 : 3\). If there are 16 more red marbles than white, what is the total number of marbles?",
     [r"\(64\)", r"\(56\)", r"\(48\)", r"\(72\)"], "A", "OSC", "easy",
     r"\(5x - 3x = 2x = 16 \implies x = 8\).\nTotal \(= (5+3) \times 8 = 64\)."),

    (61, r"Divide \(₹1170\) between A, B, and C in the ratio \(\frac{1}{2} : \frac{1}{3} : \frac{1}{4}\). How much does B receive?",
     [r"\(₹360\)", r"\(₹540\)", r"\(₹270\)", r"\(₹450\)"], "A", "OSC", "medium",
     r"Multiply by 12: \(6 : 4 : 3\). Total parts \(= 13\).\nB \(= \frac{4}{13} \times 1170 = 4 \times 90 = ₹360\)."),

    (62, r"The ratio of incomes of A and B is \(5 : 4\) and the ratio of their expenditures is \(3 : 2\). If each saves \(₹1600\), what is A's income?",
     [r"\(₹4000\)", r"\(₹3200\)", r"\(₹4800\)", r"\(₹3600\)"], "A", "OSC", "hard",
     r"\(\frac{5x - 1600}{4x - 1600} = \frac{3}{2} \implies 10x - 3200 = 12x - 4800 \implies 2x = 1600 \implies x = 800\).\nA's income \(= 5 \times 800 = ₹4000\)."),

    (63, r"A sum of \(₹2000\) is divided among A, B, and C such that A gets twice as much as B, and B gets thrice as much as C. How much does C get?",
     [r"\(₹200\)", r"\(₹600\)", r"\(₹1200\)", r"\(₹300\)"], "A", "OSC", "medium",
     r"Let \(C = x\). Then \(B = 3x\) and \(A = 2(3x) = 6x\).\nTotal \(= 6x + 3x + x = 10x = 2000 \implies x = 200\). C gets \(₹200\)."),

    (64, r"Two numbers are in the ratio \(7 : 11\). If 7 is subtracted from each, the ratio becomes \(2 : 3\). Find the larger original number.",
     [r"\(77\)", r"\(49\)", r"\(66\)", r"\(88\)"], "A", "OSC", "medium",
     r"\(\frac{7x-7}{11x-7} = \frac{2}{3} \implies 21x - 21 = 22x - 14 \implies x = -7\) wait! If \(\frac{7x-7}{11x-7} = \frac{2}{3} \implies 21x - 21 = 22x - 14 \implies x = -7\). Let's use addition: if 7 is added: \(\frac{7x+7}{11x+7} = \frac{2}{3} \implies 21x + 21 = 22x + 14 \implies x = 7\). Then numbers are 49 and 77! Let's update text: 'If 7 is added to each'."),

    (65, r"A line of length \(105\text{ cm}\) is divided into three segments in the ratio \(2 : 3 : 2\). Find the length of the middle segment.",
     [r"\(45\text{ cm}\)", r"\(30\text{ cm}\)", r"\(35\text{ cm}\)", r"\(40\text{ cm}\)"], "A", "OSC", "easy",
     r"Total parts \(= 7\). Middle \(= \frac{3}{7} \times 105 = 45\text{ cm}\)."),

    (66, r"True or False: If \(A : B = 3 : 4\) and \(B : C = 4 : 5\), then \(A : C = 3 : 5\).",
     ["True", "False"], "A", "OTF", "easy",
     r"Since B is 4 in both, \(A : B : C = 3 : 4 : 5\), so \(A : C = 3 : 5\). True."),

    (67, r"True or False: If a sum is divided between two people in the ratio \(1 : 2\), the first person receives \(50\%\) of the total sum.",
     ["False", "True"], "A", "OTF", "easy",
     r"First person receives \(\frac{1}{3} \approx 33.33\%\), not \(50\%\). False."),

    (68, r"The ratio of two numbers is \(4 : 7\) and their difference is 21. The larger number is _____.",
     [r"\(49\)", r"\(28\)", r"\(42\)", r"\(56\)"], "A", "OFB", "easy",
     r"\(7x - 4x = 3x = 21 \implies x = 7\). Larger number \(= 7 \times 7 = 49\)."),

    (69, r"Divide \(₹1500\) in the ratio \(1 : 2 : 3\). The largest share is ₹ _____.",
     [r"\(750\)", r"\(500\)", r"\(600\)", r"\(800\)"], "A", "OFB", "easy",
     r"Total parts \(= 6\). Largest \(= \frac{3}{6} \times 1500 = ₹750\)."),

    (70, r"Two numbers are in the ratio \(3 : 8\). If the smaller number is 27, calculate the numerical value of the larger number.",
     [r"\(72\)", r"\(64\)", r"\(80\)", r"\(54\)"], "A", "ONE", "easy",
     r"\(3x = 27 \implies x = 9\). Larger number \(= 8 \times 9 = 72\).")
]

# Adjust 64 text
sub2_practice[8] = (64, r"Two numbers are in the ratio \(7 : 11\). If 7 is added to each, the ratio becomes \(2 : 3\). Find the larger original number.",
     [r"\(77\)", r"\(49\)", r"\(66\)", r"\(88\)"], "A", "OSC", "medium",
     r"\(\frac{7x+7}{11x+7} = \frac{2}{3} \implies 21x + 21 = 22x + 14 \implies x = 7\). Larger number \(= 11 \times 7 = 77\).")

for seq, text, opts, ans, qtype, diff, exp in sub2_practice:
    questions.append(make_q(seq, SUB2_CODE, SUB2_NAME, text, opts, ans, qtype, diff, "practice", "standard", exp))

# =========================================================================
# FOUNDATION VAULT: Questions 071 - 082 (Challenging / Olympiad)
# =========================================================================

foundation_q = [
    (71, SUB1_CODE, SUB1_NAME,
     r"A sum of \(₹4300\) is divided among 45 people consisting of men, women, and children. The total amount received by men, women, and children is in the ratio \(12 : 15 : 16\), and the amount received by each man, woman, and child is in the ratio \(6 : 5 : 4\). Find the number of women.",
     [r"\(15\)", r"\(10\)", r"\(20\)", r"\(12\)"], "A", "OSC", "hard",
     r"### 1. Mathematical Concept & Principle:\nRatio of number of individuals \(= \frac{\text{Total Amount}}{\text{Individual Share}}\).\n\n### 2. Step-by-Step Calculation:\nMen : Women : Children \(= \frac{12}{6} : \frac{15}{5} : \frac{16}{4} = 2 : 3 : 4\).\nTotal parts \(= 2 + 3 + 4 = 9\).\nTotal people \(= 45 \implies 9x = 45 \implies x = 5\).\nNumber of women \(= 3 \times 5 = 15\).\n\n### 3. Option Analysis:\n- Option A is correct: 15."),

    (72, SUB1_CODE, SUB1_NAME,
     r"A, B, and C enter into a partnership. A invests \(\frac{1}{3}\) of the total capital for \(\frac{1}{4}\) of the time. B invests \(\frac{1}{2}\) of the capital for \(\frac{1}{6}\) of the time, and C invests the rest of the capital for the whole year. In what ratio should the annual profit be divided among A, B, and C?",
     [r"\(1 : 1 : 2\)", r"\(2 : 3 : 4\)", r"\(1 : 2 : 3\)", r"\(2 : 1 : 4\)"], "A", "OSC", "hard",
     r"Profit is proportional to \(\text{Capital} \times \text{Time}\).\nC's capital \(= 1 - (\frac{1}{3} + \frac{1}{2}) = 1 - \frac{5}{6} = \frac{1}{6}\).\nA: \(\frac{1}{3} \times \frac{1}{4} = \frac{1}{12}\).\nB: \(\frac{1}{2} \times \frac{1}{6} = \frac{1}{12}\).\nC: \(\frac{1}{6} \times 1 = \frac{1}{6} = \frac{2}{12}\).\nRatio A : B : C \(= \frac{1}{12} : \frac{1}{12} : \frac{2}{12} = 1 : 1 : 2\)."),

    (73, SUB1_CODE, SUB1_NAME,
     r"A sum of \(₹3300\) was divided among A, B, and C such that A received \(\frac{2}{3}\) as much as B and C together, and B received \(\frac{1}{2}\) as much as A and C together. How much did C receive?",
     [r"\(₹880\)", r"\(₹1320\)", r"\(₹1100\)", r"\(₹990\)"], "A", "OSC", "hard",
     r"\(A = \frac{2}{3}(B+C) \implies A = \frac{2}{5}(A+B+C) = \frac{2}{5} \times 3300 = ₹1320\).\n\(B = \frac{1}{2}(A+C) \implies B = \frac{1}{3}(A+B+C) = \frac{1}{3} \times 3300 = ₹1100\).\n\(C = 3300 - (1320 + 1100) = 3300 - 2420 = ₹880\)."),

    (74, SUB1_CODE, SUB1_NAME,
     r"A bag contains 1-rupee, 50-paise, and 25-paise coins in the ratio \(5 : 6 : 8\). If the total value of all the coins in the bag is \(₹420\), how many 50-paise coins are there in the bag?",
     [r"\(252\)", r"\(210\)", r"\(240\)", r"\(280\)"], "A", "OSC", "hard",
     r"Value of each type: 1-rupee: \(5x \times 1 = 5x\). 50-paise: \(6x \times 0.5 = 3x\). 25-paise: \(8x \times 0.25 = 2x\).\nTotal value \(= 5x + 3x + 2x = 10x = 420 \implies x = 42\).\nNumber of 50-paise coins \(= 6x = 6 \times 42 = 252\)."),

    (75, SUB1_CODE, SUB1_NAME,
     r"The monthly incomes of A and B are in the ratio \(4 : 5\) and their monthly expenditures are in the ratio \(7 : 9\). If each saves \(₹50\), what is the monthly income of A?",
     [r"\(₹400\)", r"\(₹500\)", r"\(₹600\)", r"\(₹350\)"], "A", "OSC", "hard",
     r"\(\frac{4x - 50}{5x - 50} = \frac{7}{9} \implies 36x - 450 = 35x - 350 \implies x = 100\).\nA's income \(= 4 \times 100 = ₹400\)."),

    (76, SUB1_CODE, SUB1_NAME,
     r"A diamond falls and breaks into three pieces whose weights are in the ratio \(1 : 2 : 3\). If the value of the diamond is directly proportional to the square of its weight, and the original diamond was worth \(₹72{,}000\), what is the total loss in value resulting from the breakage?",
     [r"\(₹44{,}000\)", r"\(₹36{,}000\)", r"\(₹28{,}000\)", r"\(₹48{,}000\)"], "A", "OSC", "hard",
     r"Total weight \(= 1 + 2 + 3 = 6\). Original value \(\propto 6^2 = 36\).\nNew value \(\propto 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14\).\nLoss in value \(\propto 36 - 14 = 22\).\nLoss amount \(= \frac{22}{36} \times 72{,}000 = 22 \times 2000 = ₹44{,}000\)."),

    (77, SUB2_CODE, SUB2_NAME,
     r"A vessel contains 80 litres of milk and water in the ratio \(7 : 3\). How much of the mixture must be drawn off and replaced with pure water so that the ratio of milk to water becomes \(1 : 1\)?",
     [r"\(16\text{ litres}\)", r"\(20\text{ litres}\)", r"\(12\text{ litres}\)", r"\(15\text{ litres}\)"], "A", "OSC", "hard",
     r"Initially: Milk \(= 56\text{ L}\), Water \(= 24\text{ L}\).\nLet \(x\) litres be drawn off. In \(x\) litres, milk \(= \frac{7}{10}x\).\nRemaining milk \(= 56 - \frac{7}{10}x\).\nIn final \(80\text{ L}\) mixture of \(1 : 1\), milk must be \(40\text{ L}\).\n\(56 - \frac{7}{10}x = 40 \implies \frac{7}{10}x = 16 \implies x = \frac{160}{7} \approx 22.86\text{ L}\).\nWait, let's use clean numbers: if total is 100 L with \(7 : 3\): Milk \(= 70\), Target \(= 50\). \(70 - 0.7x = 50 \implies 0.7x = 20 \implies x = 28.57\).\nLet initial ratio be \(3 : 1\) in 60 L: Milk \(= 45\), Target \(= 30\). \(45 - \frac{3}{4}x = 30 \implies \frac{3}{4}x = 15 \implies x = 20\text{ litres}\)!\nLet's update problem text: 60 litres with ratio \(3 : 1\). Replacement \(= 20\text{ L}\)."),

    (78, SUB2_CODE, SUB2_NAME,
     r"The ratio of the number of boys to girls in a school was \(5 : 3\). Some new students were admitted, of whom the number of boys was to the number of girls in the ratio \(5 : 7\), at which the total number of students became 1200 and the ratio of boys to girls changed to \(7 : 5\). How many students were there before new admissions?",
     [r"\(960\)", r"\(840\)", r"\(900\)", r"\(1000\)"], "A", "OSC", "hard",
     r"Final total \(= 1200\). Final boys \(= \frac{7}{12} \times 1200 = 700\), girls \(= 500\).\nLet initial students be \(8x\) (boys \(5x\), girls \(3x\)).\nNew admissions \(= 12y\) (boys \(5y\), girls \(7y\)).\n\(8x + 12y = 1200 \implies 2x + 3y = 300\).\nBoys: \(5x + 5y = 700 \implies x + y = 140\).\nMultiply second by 2: \(2x + 2y = 280\).\nSubtract: \(y = 20\).\n\(x = 140 - 20 = 120\).\nInitial students \(= 8x = 8 \times 120 = 960\)."),

    (79, SUB2_CODE, SUB2_NAME,
     r"Gold is 19 times as heavy as water and copper is 9 times as heavy as water. In what ratio must these two metals be mixed so that the resulting alloy is 15 times as heavy as water?",
     [r"\(3 : 2\)", r"\(2 : 3\)", r"\(1 : 2\)", r"\(4 : 3\)"], "A", "OSC", "hard",
     r"By Rule of Alligation:\nGold (\(19\)) and Copper (\(9\)), Target (\(15\)).\nDifference 1: \(15 - 9 = 6\).\nDifference 2: \(19 - 15 = 4\).\nRatio of Gold : Copper \(= 6 : 4 = 3 : 2\)."),

    (80, SUB2_CODE, SUB2_NAME,
     r"Three friends invested in a business in the ratio \(\frac{1}{2} : \frac{1}{3} : \frac{1}{5}\). After 4 months, the first friend withdrew half of his capital. If the total annual profit was \(₹84{,}600\), what was the share of the second friend?",
     [r"\(₹36{,}000\)", r"\(₹28{,}000\)", r"\(₹24{,}000\)", r"\(₹32{,}000\)"], "A", "OSC", "hard",
     r"Initial ratio: \(\frac{1}{2} : \frac{1}{3} : \frac{1}{5} = 15 : 10 : 6\) (multiplying by 30).\nA's capital: \(15 \times 4 + 7.5 \times 8 = 60 + 60 = 120\).\nB's capital: \(10 \times 12 = 120\).\nC's capital: \(6 \times 12 = 72\).\nRatio of profits A : B : C \(= 120 : 120 : 72 = 5 : 5 : 3\).\nTotal parts \(= 13\). Wait, \(84600 / 13\) is not integer. Let's adjust profit: \(120 + 120 + 72 = 312\), divide by 24: \(5 : 5 : 3\) (sum 13). If profit is \(₹91{,}000\), B gets \(\frac{5}{13} \times 91000 = ₹35{,}000\).\nLet's use profit \(₹65{,}000\): B gets \(\frac{5}{13} \times 65000 = ₹25{,}000\). Options: [₹25,000, ₹20,000, ₹15,000, ₹30,000]."),

    (81, SUB2_CODE, SUB2_NAME,
     r"The ratio of incomes of A and B is \(3 : 2\) and their expenditures are in the ratio \(5 : 3\). If each saves \(₹1000\), find the monthly income of B.",
     [r"\(4000\)", r"\(6000\)", r"\(3000\)", r"\(5000\)"], "A", "ONE", "hard",
     r"\(\frac{3x - 1000}{2x - 1000} = \frac{5}{3} \implies 9x - 3000 = 10x - 5000 \implies x = 2000\).\nB's income \(= 2 \times 2000 = 4000\)."),

    (82, SUB2_CODE, SUB2_NAME,
     r"Two casks of equal capacity are full of mixture of wine and water. In the first, the ratio is \(3 : 1\), and in the second, \(5 : 3\). If both casks are emptied into a large vessel, find the ratio of wine to water in the resulting mixture.",
     [r"\(11 : 5\)", r"\(5 : 11\)", r"\(7 : 3\)", r"\(8 : 5\)"], "A", "OSC", "hard",
     r"Let each cask hold 8 units (LCM of 4 and 8).\nIn cask 1: Wine \(= \frac{3}{4} \times 8 = 6\), Water \(= 2\).\nIn cask 2: Wine \(= \frac{5}{8} \times 8 = 5\), Water \(= 3\).\nTotal Wine \(= 6 + 5 = 11\).\nTotal Water \(= 2 + 3 = 5\).\nRatio \(= 11 : 5\).")
]

# Adjust 77
foundation_q[6] = (77, SUB2_CODE, SUB2_NAME,
     r"A vessel contains 60 litres of milk and water in the ratio \(3 : 1\). How much of the mixture must be drawn off and replaced with pure water so that the ratio of milk to water becomes \(1 : 1\)?",
     [r"\(20\text{ litres}\)", r"\(15\text{ litres}\)", r"\(25\text{ litres}\)", r"\(10\text{ litres}\)"], "A", "OSC", "hard",
     r"Initially: Milk \(= 45\text{ L}\), Water \(= 15\text{ L}\).\nLet \(x\) litres be drawn off. Remaining milk \(= 45 - \frac{3}{4}x\).\nIn final \(1 : 1\) mixture of 60 L, milk must be 30 L.\n\(45 - \frac{3}{4}x = 30 \implies \frac{3}{4}x = 15 \implies x = 20\text{ litres}\).")

# Adjust 80
foundation_q[9] = (80, SUB2_CODE, SUB2_NAME,
     r"Three friends invested in a business in the ratio \(\frac{1}{2} : \frac{1}{3} : \frac{1}{5}\). After 4 months, the first friend withdrew half of his capital. If the total annual profit was \(₹65{,}000\), what was the share of the second friend?",
     [r"\(₹25{,}000\)", r"\(₹20{,}000\)", r"\(₹15{,}000\)", r"\(₹30{,}000\)"], "A", "OSC", "hard",
     r"Multiplying by 30: \(15 : 10 : 6\).\nA's capital-time: \(15 \times 4 + 7.5 \times 8 = 120\).\nB's capital-time: \(10 \times 12 = 120\).\nC's capital-time: \(6 \times 12 = 72\).\nRatio: \(120 : 120 : 72 = 5 : 5 : 3\).\nTotal parts \(= 13\).\nB's share \(= \frac{5}{13} \times 65{,}000 = ₹25{,}000\).")

for seq, sub_code, sub_name, text, opts, ans, qtype, diff, exp in foundation_q:
    questions.append(make_q(seq, sub_code, sub_name, text, opts, ans, qtype, diff, "foundation", "foundation", exp))

out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch7_t5.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"✅ Generated {len(questions)} questions for Topic 7.5 -> {out_path}")
