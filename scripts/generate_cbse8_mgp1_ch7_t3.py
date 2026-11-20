# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-7-7.3
Topic: Proportional Ratios, Cross-Multiplication & Checking Proportions
Subtopic 7.3.1: Checking proportion: Equivalence & cross-product (ad = bc)
Subtopic 7.3.2: Finding missing terms in proportions
Vaults: 40 Exam (001-040) + 30 Practice (041-070) + 12 Foundation (071-082)
"""

import json
import os

PARENT_TOPIC_CODE = "CBSE-8-MGP1-7-7.3"
PARENT_TOPIC_NAME = "Proportional Ratios, Cross-Multiplication & Checking Proportions"
CH_NUM = 7
SUB1_CODE = "CBSE-8-MGP1-7-7.3.1"
SUB1_NAME = "Checking proportion: Equivalence & cross-product (ad = bc)"
SUB2_CODE = "CBSE-8-MGP1-7-7.3.2"
SUB2_NAME = "Finding missing terms in proportions"

def make_q(seq, sub_code, sub_name, text, options, answer_letter, qtype, difficulty, vault, category, explanation):
    qnum_str = f"{seq:03d}"
    doc_id = f"CBSE-8-MGP1-7-7.3-{qtype}-{qnum_str}"
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
# EXAM VAULT: Questions 001 - 040 (20 for 7.3.1, 20 for 7.3.2)
# =========================================================================

sub1_exam = [
    (1, r"Four numbers \(a, b, c, d\) are said to be in proportion if and only if which of the following cross-product relationships holds true?",
     [r"\(ad = bc\)", r"\(ab = cd\)", r"\(ac = bd\)", r"\(a + d = b + c\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nIf \(\frac{a}{b} = \frac{c}{d}\), multiplying both sides by \(bd\) gives the fundamental cross-product rule:\n\\[\n\\text{Product of Extremes} = \\text{Product of Means} \\iff ad = bc\n\\]\n\n### 2. Option Analysis:\n- Option A is correct: \(ad = bc\)."),

    (2, r"Which of the following sets of four numbers forms a valid proportion?",
     [r"\(12, 18, 28, 42\)", r"\(10, 15, 20, 25\)", r"\(6, 9, 14, 20\)", r"\(4, 8, 12, 16\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nCheck if \(a \times d = b \times c\).\nFor \(12, 18, 28, 42\):\n\(12 \times 42 = 504\)\n\(18 \times 28 = 504\)\nSince \(504 = 504\), they are in proportion.\n\n### 2. Option Analysis:\n- Option A is correct."),

    (3, r"In the proportion \(24 : 36 :: 16 : x\), what are the extremes and what are the means?",
     [r"Extremes are 24 and \(x\); Means are 36 and 16",
      r"Extremes are 36 and 16; Means are 24 and \(x\)",
      r"Extremes are 24 and 16; Means are 36 and \(x\)",
      r"Extremes are 24 and 36; Means are 16 and \(x\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nIn \(a : b :: c : d\), the first and fourth terms (\(a, d\)) are extremes, while the middle two terms (\(b, c\)) are means.\n\n### 2. Option Analysis:\n- Option A is correct."),

    (4, r"Do the ratios \(25\text{ g} : 30\text{ g}\) and \(40\text{ kg} : 48\text{ kg}\) form a proportion?",
     [r"Yes, both reduce to \(5 : 6\)", r"No, because grams and kilograms cannot form a proportion", r"No, because \(25 \times 48 \neq 30 \times 40\)", r"Cannot be evaluated"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{25}{30} = \frac{5}{6}\) and \(\frac{40}{48} = \frac{5}{6}\). Since both ratios are numerically equivalent to \(5 : 6\), they form a valid proportion. Note: Within each ratio, units match.\n\n### 2. Option Analysis:\n- Option A is correct."),

    (5, r"What is the mean proportional between 9 and 25?",
     [r"\(15\)", r"\(17\)", r"\(12\)", r"\(225\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nThe mean proportional between \(a\) and \(b\) is \(\sqrt{ab}\).\n\n### 2. Step-by-Step Calculation:\n\(\sqrt{9 \times 25} = \sqrt{225} = 15\).\n\n### 3. Option Analysis:\n- Option A is correct: 15."),

    (6, r"If three numbers \(a, b, c\) are in continued proportion, which of the following is true?",
     [r"\(b^2 = ac\)", r"\(b = ac\)", r"\(a^2 = bc\)", r"\(2b = a + c\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nContinued proportion means \(\frac{a}{b} = \frac{b}{c} \implies b^2 = ac\).\n\n### 2. Option Analysis:\n- Option A is correct."),

    (7, r"Which of the following does NOT form a continued proportion?",
     [r"\(4, 8, 12\)", r"\(2, 6, 18\)", r"\(3, 6, 12\)", r"\(4, 12, 36\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nCheck if \(b^2 = ac\).\nFor \(4, 8, 12\): \(8^2 = 64 \neq 4 \times 12 = 48\). Thus \(4, 8, 12\) does NOT form a continued proportion.\n\n### 2. Option Analysis:\n- Option A is correct."),

    (8, r"What is the third proportional to 8 and 12?",
     [r"\(18\)", r"\(16\)", r"\(24\)", r"\(15\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nIf \(c\) is the third proportional, \(\frac{8}{12} = \frac{12}{c} \implies 8c = 144 \implies c = 18\).\n\n### 2. Option Analysis:\n- Option A is correct: 18."),

    (9, r"Test whether the ratios \(1.5 : 2.5\) and \(6 : 10\) are in proportion using cross-multiplication.",
     [r"Yes, since \(1.5 \times 10 = 15\) and \(2.5 \times 6 = 15\)",
      r"No, because \(1.5 \times 10 \neq 2.5 \times 6\)",
      r"No, decimals cannot form proportions",
      r"Yes, because their sum is equal"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(1.5 \times 10 = 15\) and \(2.5 \times 6 = 15\). Both products are identical (15), confirming the proportion.\n\n### 2. Option Analysis:\n- Option A is correct."),

    (10, r"If \(a : b :: c : d\), then by the Invertendo property:",
     [r"\(b : a :: d : c\)", r"\(a : c :: b : d\)", r"\(a + b : b :: c + d : d\)", r"\(a - b : b :: c - d : d\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nInvertendo means taking reciprocals on both sides: \(\frac{a}{b} = \frac{c}{d} \implies \frac{b}{a} = \frac{d}{c}\).\n\n### 2. Option Analysis:\n- Option A is correct."),

    (11, r"If \(a : b :: c : d\), which property states that \(a : c :: b : d\)?",
     [r"Alternando", r"Invertendo", r"Componendo", r"Dividendo"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nInterchanging the means (\(b\) and \(c\)) gives \(\frac{a}{c} = \frac{b}{d}\), which is the Alternando property.\n\n### 2. Option Analysis:\n- Option A is correct."),

    (12, r"Are the numbers \(8, 12, 14, 21\) in proportion?",
     [r"Yes, because \(8 \times 21 = 12 \times 14 = 168\)",
      r"No, because \(8 \times 21 \neq 12 \times 14\)",
      r"No, because 21 is odd",
      r"Cannot be evaluated"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(8 \times 21 = 168\); \(12 \times 14 = 168\). Product of extremes equals product of means.\n\n### 2. Option Analysis:\n- Option A is correct."),

    (13, r"What is the mean proportional between 4 and 64?",
     [r"\(16\)", r"\(32\)", r"\(8\)", r"\(256\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(\sqrt{4 \times 64} = \sqrt{256} = 16\).\n\n### 2. Option Analysis:\n- Option A is correct: 16."),

    (14, r"If the cost of 4 notebooks is \(₹100\) and the cost of 7 notebooks is \(₹175\), do these quantities form a proportion?",
     [r"Yes, \(4 : 7 :: 100 : 175\)", r"No, because \(4 \times 175 \neq 7 \times 100\)", r"No, units are different", r"Cannot be compared"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(4 \times 175 = 700\); \(7 \times 100 = 700\). Both cross-products equal 700, so they form a valid proportion.\n\n### 2. Option Analysis:\n- Option A is correct."),

    (15, r"What is the third proportional to \(2.5\) and \(5\)?",
     [r"\(10\)", r"\(7.5\)", r"\(12.5\)", r"\(20\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{2.5}{5} = \frac{5}{x} \implies 2.5x = 25 \implies x = 10\).\n\n### 2. Option Analysis:\n- Option A is correct: 10."),

    (16, r"Which term completes the proportion \(15 : 20 :: 21 : ?\)?",
     [r"\(28\)", r"\(26\)", r"\(30\)", r"\(25\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{15}{20} = \frac{3}{4} \implies \frac{21}{x} = \frac{3}{4} \implies x = \frac{21 \times 4}{3} = 28\).\n\n### 2. Option Analysis:\n- Option A is correct: 28."),

    (17, r"If \(x : 6 :: 24 : 36\), what is the value of \(x\)?",
     [r"\(4\)", r"\(6\)", r"\(8\)", r"\(9\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(36x = 6 \times 24 = 144 \implies x = \frac{144}{36} = 4\).\n\n### 2. Option Analysis:\n- Option A is correct: 4."),

    (18, r"What is the fourth proportional to \(3, 7, 9\)?",
     [r"\(21\)", r"\(18\)", r"\(24\)", r"\(27\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{3}{7} = \frac{9}{x} \implies 3x = 63 \implies x = 21\).\n\n### 2. Option Analysis:\n- Option A is correct: 21."),

    (19, r"If \(x\) is the mean proportional between 16 and 36, what is \(x\)?",
     [r"\(24\)", r"\(26\)", r"\(20\)", r"\(28\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\n\(x = \sqrt{16 \times 36} = 4 \times 6 = 24\).\n\n### 2. Option Analysis:\n- Option A is correct: 24."),

    (20, r"Determine the middle terms (means) in the proportion \(5\text{ m} : 10\text{ m} :: 25\text{ kg} : 50\text{ kg}\).",
     [r"\(10\text{ m}\) and \(25\text{ kg}\)", r"\(5\text{ m}\) and \(50\text{ kg}\)", r"\(5\text{ m}\) and \(10\text{ m}\)", r"\(25\text{ kg}\) and \(50\text{ kg}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nThe second and third terms are the means: \(10\text{ m}\) and \(25\text{ kg}\).\n\n### 2. Option Analysis:\n- Option A is correct.")
]

for seq, text, opts, ans, qtype, diff, exp in sub1_exam:
    questions.append(make_q(seq, SUB1_CODE, SUB1_NAME, text, opts, ans, qtype, diff, "exam", "standard", exp))

# --- SUBTOPIC 7.3.2: Finding Missing Terms in Proportions (021 - 040) ---
sub2_exam = [
    (21, r"Find \(x\) in the proportion \(x : 5 = 28 : 35\).",
     [r"\(4\)", r"\(7\)", r"\(5\)", r"\(3\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(35x = 5 \times 28 = 140 \implies x = \frac{140}{35} = 4\).\n\n### 2. Option Analysis:\n- Option A is correct: 4."),

    (22, r"Solve for \(m\): \(\frac{14}{m} = \frac{21}{45}\).",
     [r"\(30\)", r"\(25\)", r"\(35\)", r"\(28\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(21m = 14 \times 45 = 630 \implies m = \frac{630}{21} = 30\).\n\n### 2. Option Analysis:\n- Option A is correct: 30."),

    (23, r"If \(9 : x :: x : 4\), find the positive value of \(x\).",
     [r"\(6\)", r"\(13\)", r"\(5\)", r"\(36\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(x^2 = 9 \times 4 = 36 \implies x = 6\).\n\n### 2. Option Analysis:\n- Option A is correct: 6."),

    (24, r"Find the missing value of \(y\) such that \(18 : 24 :: y : 36\).",
     [r"\(27\)", r"\(24\)", r"\(30\)", r"\(25\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(24y = 18 \times 36 = 648 \implies y = \frac{648}{24} = 27\).\n\n### 2. Option Analysis:\n- Option A is correct: 27."),

    (25, r"Solve for \(p\): \(0.4 : 1.2 :: 1.5 : p\).",
     [r"\(4.5\)", r"\(3.6\)", r"\(5.0\)", r"\(4.0\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\n\(0.4p = 1.2 \times 1.5 = 1.8 \implies p = \frac{1.8}{0.4} = 4.5\).\n\n### 2. Option Analysis:\n- Option A is correct: 4.5."),

    (26, r"If \(\frac{2}{3} : \frac{5}{6} :: \frac{4}{5} : x\), what is the value of \(x\)?",
     [r"\(1\)", r"\(\frac{8}{9}\)", r"\(\frac{4}{3}\)", r"\(\frac{5}{4}\)"], "A", "OSC", "hard",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{2}{3} \times x = \frac{5}{6} \times \frac{4}{5} = \frac{2}{3}\).\nSince \(\frac{2}{3} x = \frac{2}{3}\), \(x = 1\).\n\n### 2. Option Analysis:\n- Option A is correct: 1."),

    (27, r"Find the fourth proportional to \(2.4, 3.6, 4.8\).",
     [r"\(7.2\)", r"\(6.4\)", r"\(8.0\)", r"\(5.4\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\n\(2.4x = 3.6 \times 4.8 = 17.28 \implies x = \frac{17.28}{2.4} = 7.2\).\n\n### 2. Option Analysis:\n- Option A is correct: 7.2."),

    (28, r"What is the third proportional to 16 and 24?",
     [r"\(36\)", r"\(32\)", r"\(48\)", r"\(30\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{16}{24} = \frac{24}{x} \implies 16x = 576 \implies x = 36\).\n\n### 2. Option Analysis:\n- Option A is correct: 36."),

    (29, r"If \(7, x, 28\) are in continued proportion, find the positive value of \(x\).",
     [r"\(14\)", r"\(12\)", r"\(16\)", r"\(21\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(x^2 = 7 \times 28 = 196 \implies x = 14\).\n\n### 2. Option Analysis:\n- Option A is correct: 14."),

    (30, r"Solve for \(k\): \(\frac{k+2}{6} = \frac{15}{18}\).",
     [r"\(3\)", r"\(5\)", r"\(4\)", r"\(2\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{15}{18} = \frac{5}{6}\). So \(\frac{k+2}{6} = \frac{5}{6} \implies k + 2 = 5 \implies k = 3\).\n\n### 2. Option Analysis:\n- Option A is correct: 3."),

    (31, r"If \(a : 8 = 15 : 20\), then \(a + 4\) is equal to:",
     [r"\(10\)", r"\(6\)", r"\(12\)", r"\(8\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(20a = 8 \times 15 = 120 \implies a = 6\).\nTherefore, \(a + 4 = 6 + 4 = 10\).\n\n### 2. Option Analysis:\n- Option A is correct: 10."),

    (32, r"Find \(y\) if \(y : 21 :: 12 : 28\).",
     [r"\(9\)", r"\(7\)", r"\(8\)", r"\(14\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(28y = 21 \times 12 = 252 \implies y = \frac{252}{28} = 9\).\n\n### 2. Option Analysis:\n- Option A is correct: 9."),

    (33, r"If \((2x + 1) : 5 :: 9 : 15\), find the value of \(x\).",
     [r"\(1\)", r"\(2\)", r"\(3\)", r"\(0.5\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{9}{15} = \frac{3}{5}\). So \(\frac{2x+1}{5} = \frac{3}{5} \implies 2x + 1 = 3 \implies 2x = 2 \implies x = 1\).\n\n### 2. Option Analysis:\n- Option A is correct: 1."),

    # 34: OAR
    (34, r"Assertion (A): If \(a : b :: c : d\), then the product of extremes equals the product of means.\nReason (R): Multiplying both sides of the equation \(\frac{a}{b} = \frac{c}{d}\) by the non-zero common denominator \(bd\) directly yields \(ad = bc\).",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"], "A", "OAR", "easy",
     r"### 1. Mathematical Concept & Principle:\nAssertion is the cross-product property of proportions. Reason provides the direct algebraic proof by clearing denominators.\n\n### 2. Option Analysis:\n- Option A is correct."),

    # 35: OAR
    (35, r"Assertion (A): The mean proportional between 2 and 8 is 4.\nReason (R): If \(x\) is the mean proportional between \(a\) and \(b\), then \(x = \frac{a+b}{2}\).",
     ["(A) is true but (R) is false",
      "Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is false but (R) is true"], "A", "OAR", "medium",
     r"### 1. Mathematical Concept & Principle:\nMean proportional is defined by geometric mean \(x = \sqrt{ab} = \sqrt{2 \times 8} = 4\). The arithmetic mean \(\frac{a+b}{2}\) in Reason is incorrect for geometric mean proportionality. Hence (A) is true and (R) is false.\n\n### 2. Option Analysis:\n- Option A is correct."),

    # 36: OTF
    (36, r"True or False: In any proportion \(a : b :: c : d\), if three terms are known, the fourth term can always be uniquely calculated using cross-multiplication.",
     ["True", "False"], "A", "OTF", "easy",
     r"Given \(ad = bc\), any single variable can be found by dividing the product of the other two by the third (e.g. \(d = \frac{bc}{a}\)). True."),

    (37, r"True or False: The numbers 5, 10, 20 are in continued proportion.",
     ["True", "False"], "A", "OTF", "easy",
     r"\(10^2 = 100\) and \(5 \times 20 = 100\). Since \(10^2 = 5 \times 20\), they are in continued proportion. True."),

    # 38: OFB
    (38, r"If \(16 : x :: 24 : 36\), then the value of \(x\) is _____.",
     [r"\(24\)", r"\(20\)", r"\(18\)", r"\(28\)"], "A", "OFB", "easy",
     r"\(24x = 16 \times 36 = 576 \implies x = \frac{576}{24} = 24\)."),

    # 39: OFB
    (39, r"The fourth proportional to 6, 8, and 9 is _____.",
     [r"\(12\)", r"\(14\)", r"\(10\)", r"\(16\)"], "A", "OFB", "easy",
     r"\(\frac{6}{8} = \frac{9}{x} \implies 6x = 72 \implies x = 12\)."),

    # 40: ONE
    (40, r"Find the third proportional to 4 and 10. Express your answer as a number.",
     [r"\(25\)", r"\(20\)", r"\(16\)", r"\(30\)"], "A", "ONE", "medium",
     r"\(\frac{4}{10} = \frac{10}{x} \implies 4x = 100 \implies x = 25\).")
]

for seq, text, opts, ans, qtype, diff, exp in sub2_exam:
    questions.append(make_q(seq, SUB2_CODE, SUB2_NAME, text, opts, ans, qtype, diff, "exam", "standard", exp))

# =========================================================================
# PRACTICE VAULT: Questions 041 - 070 (15 for 7.3.1, 15 for 7.3.2)
# =========================================================================

sub1_practice = [
    (41, r"Check if the four numbers \(14, 21, 22, 33\) are in proportion.",
     [r"Yes, \(14 \times 33 = 21 \times 22 = 462\)", r"No, because \(14 \times 33 \neq 21 \times 22\)", r"No, numbers are not multiples", r"Cannot be checked without units"], "A", "OSC", "easy",
     r"\(14 \times 33 = 462\); \(21 \times 22 = 462\). They form a proportion."),

    (42, r"Which of the following is in continued proportion?",
     [r"\(9, 12, 16\)", r"\(4, 8, 14\)", r"\(3, 6, 10\)", r"\(5, 10, 15\)"], "A", "OSC", "easy",
     r"\(12^2 = 144\) and \(9 \times 16 = 144\). Thus \(9, 12, 16\) is in continued proportion."),

    (43, r"What is the mean proportional between 12 and 27?",
     [r"\(18\)", r"\(16\)", r"\(20\)", r"\(24\)"], "A", "OSC", "medium",
     r"\(\sqrt{12 \times 27} = \sqrt{324} = 18\)."),

    (44, r"If \(\frac{a}{b} = \frac{c}{d}\), which property gives \(\frac{a+b}{b} = \frac{c+d}{d}\)?",
     [r"Componendo", r"Dividendo", r"Invertendo", r"Alternando"], "A", "OSC", "easy",
     r"Adding 1 to both sides: \(\frac{a}{b} + 1 = \frac{c}{d} + 1 \implies \frac{a+b}{b} = \frac{c+d}{d}\) is Componendo."),

    (45, r"Which property gives \(\frac{a-b}{b} = \frac{c-d}{d}\) from \(\frac{a}{b} = \frac{c}{d}\)?",
     [r"Dividendo", r"Componendo", r"Invertendo", r"Alternando"], "A", "OSC", "easy",
     r"Subtracting 1 from both sides gives Dividendo."),

    (46, r"Are \(15\text{ cm} : 20\text{ cm}\) and \(45\text{ seconds} : 60\text{ seconds}\) in proportion?",
     [r"Yes, both ratios simplify to \(3 : 4\)", r"No, because length and time cannot be compared", r"No, because cross-product fails", r"Cannot be determined"], "A", "OSC", "easy",
     r"\(\frac{15}{20} = \frac{3}{4}\) and \(\frac{45}{60} = \frac{3}{4}\). Both ratios are \(3 : 4\), so they form a valid proportion."),

    (47, r"Find the mean proportional between \(0.04\) and \(0.36\).",
     [r"\(0.12\)", r"\(0.06\)", r"\(0.18\)", r"\(0.24\)"], "A", "OSC", "medium",
     r"\(\sqrt{0.04 \times 0.36} = \sqrt{0.0144} = 0.12\)."),

    (48, r"What is the third proportional to 9 and 15?",
     [r"\(25\)", r"\(20\)", r"\(22.5\)", r"\(30\)"], "A", "OSC", "easy",
     r"\(\frac{9}{15} = \frac{15}{x} \implies 9x = 225 \implies x = 25\)."),

    (49, r"If 6, 18, and \(x\) are in continued proportion, find \(x\).",
     [r"\(54\)", r"\(36\)", r"\(48\)", r"\(72\)"], "A", "OSC", "easy",
     r"\(\frac{6}{18} = \frac{18}{x} \implies 6x = 324 \implies x = 54\)."),

    (50, r"Which of the following sets forms a proportion?",
     [r"\(8, 14, 20, 35\)", r"\(6, 10, 15, 20\)", r"\(4, 6, 8, 10\)", r"\(10, 15, 25, 30\)"], "A", "OSC", "medium",
     r"\(8 \times 35 = 280\); \(14 \times 20 = 280\). They form a proportion."),

    (51, r"What is the fourth proportional to \(2, 5, 8\)?",
     [r"\(20\)", r"\(15\)", r"\(25\)", r"\(16\)"], "A", "OSC", "easy",
     r"\(\frac{2}{5} = \frac{8}{x} \implies 2x = 40 \implies x = 20\)."),

    (52, r"If \(ad = bc\), can we write \(\frac{a}{c} = \frac{b}{d}\)?",
     [r"Yes, dividing both sides by \(cd\)", r"No, this violates cross-multiplication", r"Only if \(a = d\)", r"Only if all are positive integers"], "A", "OSC", "easy",
     r"Dividing \(ad = bc\) by \(cd\) gives \(\frac{a}{c} = \frac{b}{d}\). True."),

    (53, r"Determine the mean proportional between 8 and 18.",
     [r"\(12\)", r"\(14\)", r"\(16\)", r"\(10\)"], "A", "OSC", "easy",
     r"\(\sqrt{8 \times 18} = \sqrt{144} = 12\)."),

    (54, r"True or False: If \(a : b :: b : c\), then \(b = \pm \sqrt{ac}\).",
     ["True", "False"], "A", "OTF", "easy",
     r"\(b^2 = ac \implies b = \sqrt{ac}\) (or \(\pm\sqrt{ac}\)). Statement is True."),

    (55, r"The fourth proportional to 5, 8, and 15 is _____.",
     [r"\(24\)", r"\(20\)", r"\(28\)", r"\(30\)"], "A", "OFB", "easy",
     r"\(\frac{5}{8} = \frac{15}{x} \implies 5x = 120 \implies x = 24\).")
]

for seq, text, opts, ans, qtype, diff, exp in sub1_practice:
    questions.append(make_q(seq, SUB1_CODE, SUB1_NAME, text, opts, ans, qtype, diff, "practice", "standard", exp))

# --- 7.3.2 Practice (056 - 070) ---
sub2_practice = [
    (56, r"Solve for \(x\): \(\frac{x}{12} = \frac{15}{20}\).",
     [r"\(9\)", r"\(8\)", r"\(10\)", r"\(6\)"], "A", "OSC", "easy",
     r"\(\frac{15}{20} = \frac{3}{4}\). \(x = \frac{3 \times 12}{4} = 9\)."),

    (57, r"Find \(y\) in the proportion \(42 : y :: 35 : 25\).",
     [r"\(30\)", r"\(28\)", r"\(32\)", r"\(35\)"], "A", "OSC", "easy",
     r"\(35y = 42 \times 25 = 1050 \implies y = \frac{1050}{35} = 30\)."),

    (58, r"If \(k : 18 :: 14 : 21\), find the value of \(k\).",
     [r"\(12\)", r"\(10\)", r"\(14\)", r"\(16\)"], "A", "OSC", "easy",
     r"\(21k = 18 \times 14 = 252 \implies k = 12\)."),

    (59, r"Find the value of \(x\) if \(2.5 : x :: 1.5 : 4.5\).",
     [r"\(7.5\)", r"\(6.0\)", r"\(5.0\)", r"\(8.0\)"], "A", "OSC", "easy",
     r"\(1.5x = 2.5 \times 4.5 = 11.25 \implies x = \frac{11.25}{1.5} = 7.5\)."),

    (60, r"Solve for \(n\): \(\frac{2n - 1}{7} = \frac{9}{21}\).",
     [r"\(2\)", r"\(3\)", r"\(1\)", r"\(4\)"], "A", "OSC", "medium",
     r"\(\frac{9}{21} = \frac{3}{7}\). So \(2n - 1 = 3 \implies 2n = 4 \implies n = 2\)."),

    (61, r"Find \(p\) if \(16, p, 64\) are in continued proportion.",
     [r"\(32\)", r"\(24\)", r"\(40\)", r"\(48\)"], "A", "OSC", "easy",
     r"\(p^2 = 16 \times 64 = 1024 \implies p = 32\)."),

    (62, r"What is the fourth proportional to \(\frac{1}{2}, \frac{1}{3}, \frac{1}{4}\)?",
     [r"\(\frac{1}{6}\)", r"\(\frac{1}{8}\)", r"\(\frac{2}{3}\)", r"\(\frac{1}{12}\)"], "A", "OSC", "medium",
     r"\(\frac{1/2}{1/3} = \frac{1/4}{x} \implies \frac{3}{2} = \frac{1}{4x} \implies 4x \times 3 = 2 \implies 12x = 2 \implies x = \frac{1}{6}\)."),

    (63, r"If \(3 : x :: x : 75\), find the positive value of \(x\).",
     [r"\(15\)", r"\(12\)", r"\(25\)", r"\(225\)"], "A", "OSC", "easy",
     r"\(x^2 = 3 \times 75 = 225 \implies x = 15\)."),

    (64, r"Solve for \(m\): \(45 : 60 :: 36 : m\).",
     [r"\(48\)", r"\(50\)", r"\(44\)", r"\(52\)"], "A", "OSC", "easy",
     r"\(45m = 60 \times 36 = 2160 \implies m = \frac{2160}{45} = 48\)."),

    (65, r"If \((x+3) : (x+8) = 2 : 3\), what is the value of \(x\)?",
     [r"\(7\)", r"\(5\)", r"\(6\)", r"\(8\)"], "A", "OSC", "medium",
     r"\(3(x+3) = 2(x+8) \implies 3x + 9 = 2x + 16 \implies x = 7\)."),

    (66, r"True or False: If \(x\) is the fourth proportional to \(a, b, c\), then \(x = \frac{bc}{a}\).",
     ["True", "False"], "A", "OTF", "easy",
     r"\(\frac{a}{b} = \frac{c}{x} \implies ax = bc \implies x = \frac{bc}{a}\). True."),

    (67, r"True or False: The mean proportional between \(a\) and \(b\) is always greater than or equal to both numbers.",
     ["False", "True"], "A", "OTF", "medium",
     r"The geometric mean \(\sqrt{ab}\) always lies BETWEEN \(a\) and \(b\). It cannot be greater than both. False."),

    (68, r"If \(8 : 12 :: 14 : x\), then \(x = \) _____.",
     [r"\(21\)", r"\(18\)", r"\(20\)", r"\(24\)"], "A", "OFB", "easy",
     r"\(8x = 12 \times 14 = 168 \implies x = 21\)."),

    (69, r"If 12, \(x\), 48 are in continued proportion, then the positive value of \(x\) is _____.",
     [r"\(24\)", r"\(36\)", r"\(20\)", r"\(30\)"], "A", "OFB", "easy",
     r"\(x^2 = 12 \times 48 = 576 \implies x = 24\)."),

    (70, r"Evaluate \(x\) in the proportion \(\frac{x}{3.5} = \frac{16}{14}\).",
     [r"\(4.0\)", r"\(3.5\)", r"\(4.5\)", r"\(5.0\)"], "A", "ONE", "easy",
     r"\(\frac{16}{14} = \frac{8}{7}\). \(x = 3.5 \times \frac{8}{7} = 0.5 \times 8 = 4.0\).")
]

for seq, text, opts, ans, qtype, diff, exp in sub2_practice:
    questions.append(make_q(seq, SUB2_CODE, SUB2_NAME, text, opts, ans, qtype, diff, "practice", "standard", exp))

# =========================================================================
# FOUNDATION VAULT: Questions 071 - 082 (Challenging / Olympiad)
# =========================================================================

foundation_q = [
    (71, SUB1_CODE, SUB1_NAME,
     r"What number must be subtracted from each of the numbers \(21, 38, 55, 106\) so that the remainders are in proportion?",
     [r"\(4\)", r"\(2\)", r"\(6\)", r"\(5\)"], "A", "OSC", "hard",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{21-x}{38-x} = \frac{55-x}{106-x}\).\n\n### 2. Step-by-Step Calculation:\n\((21-x)(106-x) = (38-x)(55-x)\)\n\(2226 - 127x + x^2 = 2090 - 93x + x^2\)\n\(2226 - 2090 = 127x - 93x\)\n\(136 = 34x \implies x = 4\).\n\n### 3. Option Analysis:\n- Option A is correct: 4."),

    (72, SUB1_CODE, SUB1_NAME,
     r"What number must be added to each of the numbers \(6, 15, 20, 43\) so that the resulting numbers are in proportion?",
     [r"\(5\)", r"\(3\)", r"\(4\)", r"\(2\)"], "A", "OSC", "hard",
     r"\(\frac{6+x}{15+x} = \frac{20+x}{43+x}\).\n\((6+x)(43+x) = (15+x)(20+x)\)\n\(258 + 49x + x^2 = 300 + 35x + x^2\)\n\(14x = 42 \implies x = 3\). Wait! Let's check: \(6+3=9, 15+3=18\) (ratio \(1:2\)). \(20+3=23, 43+3=46\) (ratio \(1:2\)).\nCorrect answer is 3! Let's update options so A is 3."),

    (73, SUB1_CODE, SUB1_NAME,
     r"If \(x, y, z\) are in continued proportion, prove which of the following equals \(\frac{x+y}{y+z}\):",
     [r"\(\frac{x}{y}\)", r"\(\frac{y}{x}\)", r"\(\frac{z}{x}\)", r"\(\frac{x^2}{z^2}\)"], "A", "OSC", "hard",
     r"Since \(\frac{x}{y} = \frac{y}{z} = k\), \(x = yk\) and \(y = zk\).\n\(\frac{x+y}{y+z} = \frac{yk + y}{zk + z} = \frac{y(k+1)}{z(k+1)} = \frac{y}{z} = \frac{x}{y}\)."),

    (74, SUB1_CODE, SUB1_NAME,
     r"If \(\frac{a}{b} = \frac{c}{d}\), evaluate \(\frac{ma + nc}{mb + nd}\) in terms of \(\frac{a}{b}\).",
     [r"Equal to \(\frac{a}{b}\)", r"Equal to \(\frac{m}{n}\)", r"Equal to \(\frac{ma}{nd}\)", r"Equal to \(\frac{a^2}{b^2}\)"], "A", "OSC", "hard",
     r"By the principle of equal ratios, if \(\frac{a}{b} = \frac{c}{d} = k\), then \(\frac{ma + nc}{mb + nd} = \frac{m(bk) + n(dk)}{mb + nd} = \frac{k(mb + nd)}{mb + nd} = k = \frac{a}{b}\)."),

    (75, SUB1_CODE, SUB1_NAME,
     r"If \((a+b+c+d)(a-b-c+d) = (a+b-c-d)(a-b+c-d)\), then \(a, b, c, d\) are in proportion. What is this proportion?",
     [r"\(a : b :: c : d\)", r"\(a : d :: b : c\)", r"\(a : c :: d : b\)", r"\(a : b :: d : c\)"], "A", "OSC", "hard",
     r"Using componendo and dividendo twice on the expanded terms yields \(\frac{a}{b} = \frac{c}{d}\)."),

    (76, SUB1_CODE, SUB1_NAME,
     r"If \(\frac{x}{b-c} = \frac{y}{c-a} = \frac{z}{a-b}\), then what is the value of \(x + y + z\)?",
     [r"\(0\)", r"\(1\)", r"\(a+b+c\)", r"\(abc\)"], "A", "OSC", "hard",
     r"By theorem of equal ratios, each ratio equals \(\frac{x+y+z}{(b-c)+(c-a)+(a-b)} = \frac{x+y+z}{0}\). For this to be finite, the numerator must be zero: \(x + y + z = 0\)."),

    (77, SUB2_CODE, SUB2_NAME,
     r"If \(x = \frac{\sqrt{a+1} + \sqrt{a-1}}{\sqrt{a+1} - \sqrt{a-1}}\), find the value of \(x^2 - 2ax + 1\).",
     [r"\(0\)", r"\(1\)", r"\(2a\)", r"\(-1\)"], "A", "OSC", "hard",
     r"By Componendo and Dividendo: \(\frac{x+1}{x-1} = \frac{\sqrt{a+1}}{\sqrt{a-1}}\).\nSquaring both sides: \(\frac{x^2+2x+1}{x^2-2x+1} = \frac{a+1}{a-1}\).\nApplying C & D again: \(\frac{2(x^2+1)}{4x} = \frac{2a}{2} = a \implies \frac{x^2+1}{2x} = a \implies x^2 + 1 = 2ax \implies x^2 - 2ax + 1 = 0\)."),

    (78, SUB2_CODE, SUB2_NAME,
     r"If \(a, b, c\) are in continued proportion, then \(\frac{a^2 + b^2}{b^2 + c^2}\) simplifies to:",
     [r"\(\frac{a}{c}\)", r"\(\frac{c}{a}\)", r"\(\frac{b}{c}\)", r"\(\frac{a^2}{c^2}\)"], "A", "OSC", "hard",
     r"Since \(b^2 = ac\):\n\(\frac{a^2 + b^2}{b^2 + c^2} = \frac{a^2 + ac}{ac + c^2} = \frac{a(a+c)}{c(a+c)} = \frac{a}{c}\)."),

    (79, SUB2_CODE, SUB2_NAME,
     r"Find the positive value of \(x\) if \(\frac{\sqrt{5x+4} + \sqrt{5x-4}}{\sqrt{5x+4} - \sqrt{5x-4}} = 3\).",
     [r"\(1\)", r"\(2\)", r"\(0.8\)", r"\(1.5\)"], "A", "OSC", "hard",
     r"Apply C & D: \(\frac{2\sqrt{5x+4}}{2\sqrt{5x-4}} = \frac{3+1}{3-1} = 2\).\nSquaring: \(\frac{5x+4}{5x-4} = 4 \implies 5x + 4 = 20x - 16 \implies 15x = 20 \implies x = \frac{4}{3}\). Wait: Let's adjust options: if \(x = \frac{4}{3} \approx 1.33\). Let's use clean numbers: if rhs = 2: \(\frac{\sqrt{x+1}+\sqrt{x-1}}{\sqrt{x+1}-\sqrt{x-1}} = 2 \implies \frac{\sqrt{x+1}}{\sqrt{x-1}} = 3 \implies \frac{x+1}{x-1} = 9 \implies x+1 = 9x - 9 \implies 8x = 10 \implies x = 1.25\)."),

    (80, SUB2_CODE, SUB2_NAME,
     r"If \(y\) is the mean proportional between \(x\) and \(z\), then \(\frac{x^2 - y^2 + z^2}{x^{-2} - y^{-2} + z^{-2}}\) is equal to:",
     [r"\(y^4\)", r"\(y^2\)", r"\(xz\)", r"\(y^6\)"], "A", "OSC", "hard",
     r"\(y^2 = xz\). The denominator \(= \frac{1}{x^2} - \frac{1}{xz} + \frac{1}{z^2} = \frac{z^2 - xz + x^2}{x^2 z^2} = \frac{x^2 - y^2 + z^2}{y^4}\).\nDividing numerator by denominator yields \(y^4\)."),

    (81, SUB2_CODE, SUB2_NAME,
     r"Find the value of \(x\) such that \(x+1, x+5, x+17\) are in continued proportion.",
     [r"\(7\)", r"\(5\)", r"\(4\)", r"\(8\)"], "A", "ONE", "hard",
     r"\((x+5)^2 = (x+1)(x+17) \implies x^2 + 10x + 25 = x^2 + 18x + 17 \implies 8x = 8 \implies x = 1\). Wait: if \(x=1\), \(2, 6, 18\) (continued proportion \(6^2 = 2 \times 18 = 36\)). So \(x=1\)!\nLet's set option A to 1!"),

    (82, SUB2_CODE, SUB2_NAME,
     r"If \(a : b = c : d\), which of the following is equal to \(\frac{a^3 + 3ab^2}{3a^2 b + b^3}\)?",
     [r"\(\frac{c^3 + 3cd^2}{3c^2 d + d^3}\)", r"\(\frac{c^2 + d^2}{cd}\)", r"\(\frac{c+d}{c-d}\)", r"\(1\)"], "A", "OSC", "hard",
     r"Let \(\frac{a}{b} = \frac{c}{d} = k\). Then \(a = bk, c = dk\).\n\(\frac{b^3 k^3 + 3bk(b^2)}{3b^2 k^2 (b) + b^3} = \frac{k^3 + 3k}{3k^2 + 1}\).\nThe same calculation with \(c\) and \(d\) yields \(\frac{k^3 + 3k}{3k^2 + 1}\). They are identically equal.")
]

# Adjust 72
foundation_q[1] = (72, SUB1_CODE, SUB1_NAME,
     r"What number must be added to each of the numbers \(6, 15, 20, 43\) so that the resulting numbers are in proportion?",
     [r"\(3\)", r"\(5\)", r"\(4\)", r"\(2\)"], "A", "OSC", "hard",
     r"\(\frac{6+x}{15+x} = \frac{20+x}{43+x} \implies 258 + 49x + x^2 = 300 + 35x + x^2 \implies 14x = 42 \implies x = 3\).")

# Adjust 79
foundation_q[8] = (79, SUB2_CODE, SUB2_NAME,
     r"Find the value of \(x\) if \(\frac{\sqrt{x+1} + \sqrt{x-1}}{\sqrt{x+1} - \sqrt{x-1}} = 2\).",
     [r"\(1.25\)", r"\(1.50\)", r"\(2.00\)", r"\(1.75\)"], "A", "OSC", "hard",
     r"Applying C & D: \(\frac{\sqrt{x+1}}{\sqrt{x-1}} = \frac{2+1}{2-1} = 3\).\nSquaring: \(\frac{x+1}{x-1} = 9 \implies x + 1 = 9x - 9 \implies 8x = 10 \implies x = 1.25\).")

# Adjust 81
foundation_q[10] = (81, SUB2_CODE, SUB2_NAME,
     r"Find the value of \(x\) such that \(x+1, x+5, x+17\) are in continued proportion.",
     [r"\(1\)", r"\(2\)", r"\(3\)", r"\(4\)"], "A", "ONE", "hard",
     r"\((x+5)^2 = (x+1)(x+17) \implies x^2 + 10x + 25 = x^2 + 18x + 17 \implies 8x = 8 \implies x = 1\).")

for seq, sub_code, sub_name, text, opts, ans, qtype, diff, exp in foundation_q:
    questions.append(make_q(seq, sub_code, sub_name, text, opts, ans, qtype, diff, "foundation", "foundation", exp))

out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch7_t3.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"✅ Generated {len(questions)} questions for Topic 7.3 -> {out_path}")
