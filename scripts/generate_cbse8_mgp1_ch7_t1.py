# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-7-7.1
Topic: Ratios, Equivalent Ratios & Scaling
Subtopic 7.1.1: Observing similarity in change: Dimension scaling
Subtopic 7.1.2: Ratios in simplest form (reducing by HCF)
Vaults: 40 Exam (001-040) + 30 Practice (041-070) + 12 Foundation (071-082)
"""

import json
import os

PARENT_TOPIC_CODE = "CBSE-8-MGP1-7-7.1"
PARENT_TOPIC_NAME = "Ratios, Equivalent Ratios & Scaling"
CH_NUM = 7
SUB1_CODE = "CBSE-8-MGP1-7-7.1.1"
SUB1_NAME = "Observing similarity in change: Dimension scaling"
SUB2_CODE = "CBSE-8-MGP1-7-7.1.2"
SUB2_NAME = "Ratios in simplest form (reducing by HCF)"

def make_q(seq, sub_code, sub_name, text, options, answer_letter, qtype, difficulty, vault, category, explanation):
    qnum_str = f"{seq:03d}"
    doc_id = f"CBSE-8-MGP1-7-7.1-{qtype}-{qnum_str}"
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
# EXAM VAULT: Questions 001 - 040 (20 for 7.1.1, 20 for 7.1.2)
# =========================================================================

# --- SUBTOPIC 7.1.1: Dimension Scaling & Similarity (001 - 020) ---
sub1_exam = [
    (1, r"A photographic print of dimensions \(10\text{ cm} \times 15\text{ cm}\) is enlarged such that its length becomes \(30\text{ cm}\). If similarity is preserved, what is its new width?",
     [r"\(20\text{ cm}\)", r"\(25\text{ cm}\)", r"\(18\text{ cm}\)", r"\(22.5\text{ cm}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nWhen a 2D shape is enlarged preserving similarity, both dimensions scale by the same constant scale factor \(k\).\n\n### 2. Step-by-Step Calculation:\nScale factor \(k = \frac{\text{New Length}}{\text{Original Length}} = \frac{30}{15} = 2\).\nTherefore, New Width \(= 10 \times 2 = 20\text{ cm}\).\n\n### 3. Option Analysis:\n- Option A is correct: \(20\text{ cm}\).\n- Options B, C, D do not preserve the constant scale factor of 2."),

    (2, r"A map has a scale of \(1 : 50{,}000\). What actual ground distance is represented by a distance of \(4\text{ cm}\) on the map?",
     [r"\(2\text{ km}\)", r"\(20\text{ km}\)", r"\(5\text{ km}\)", r"\(200\text{ m}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nA scale of \(1 : n\) means 1 unit on the map corresponds to \(n\) units in reality.\n\n### 2. Step-by-Step Calculation:\nGround distance \(= 4\text{ cm} \times 50{,}000 = 200{,}000\text{ cm}\).\nConvert to meters: \(\frac{200{,}000}{100} = 2{,}000\text{ m}\).\nConvert to kilometers: \(\frac{2{,}000}{1{,}000} = 2\text{ km}\).\n\n### 3. Option Analysis:\n- Option A is correct: \(2\text{ km}\)."),

    (3, r"If the linear dimensions of a rectangle are each scaled up by a factor of 3, by what factor does its area increase?",
     [r"\(9\)", r"\(3\)", r"\(6\)", r"\(27\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nIf linear dimensions are scaled by factor \(k\), the area scales by \(k^2\).\n\n### 2. Step-by-Step Calculation:\n\(\text{New Area} = (3 \times L) \times (3 \times B) = 9 \times (L \times B) = 9 \times \text{Original Area}\).\n\n### 3. Option Analysis:\n- Option A is correct: \(3^2 = 9\)."),

    (4, r"A model of a ship is built to a scale of \(1 : 200\). If the mast of the actual ship is \(30\text{ m}\) high, what is the height of the model mast?",
     [r"\(15\text{ cm}\)", r"\(1.5\text{ cm}\)", r"\(6\text{ cm}\)", r"\(60\text{ cm}\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nModel dimension \(= \frac{\text{Actual Dimension}}{\text{Scale Factor}}\).\n\n### 2. Step-by-Step Calculation:\nActual height \(= 30\text{ m} = 3{,}000\text{ cm}\).\nModel height \(= \frac{3{,}000\text{ cm}}{200} = 15\text{ cm}\).\n\n### 3. Option Analysis:\n- Option A is correct: \(15\text{ cm}\)."),

    (5, r"Two squares have side lengths in the ratio \(2 : 5\). What is the ratio of their perimeters?",
     [r"\(2 : 5\)", r"\(4 : 25\)", r"\(8 : 125\)", r"\(1 : 2.5\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nPerimeter is a one-dimensional linear measure. The ratio of perimeters of similar figures equals the ratio of their corresponding linear dimensions.\n\n### 2. Step-by-Step Calculation:\n\(\frac{P_1}{P_2} = \frac{4s_1}{4s_2} = \frac{s_1}{s_2} = \frac{2}{5}\).\n\n### 3. Option Analysis:\n- Option A is correct: \(2 : 5\)."),

    (6, r"The sides of a triangle are \(6\text{ cm}\), \(8\text{ cm}\), and \(10\text{ cm}\). A similar triangle has its longest side equal to \(25\text{ cm}\). What is the perimeter of the larger triangle?",
     [r"\(60\text{ cm}\)", r"\(48\text{ cm}\)", r"\(50\text{ cm}\)", r"\(72\text{ cm}\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nOriginal perimeter \(= 6 + 8 + 10 = 24\text{ cm}\). Scale factor \(k = \frac{25}{10} = 2.5\).\n\n### 2. Step-by-Step Calculation:\nNew perimeter \(= 24 \times 2.5 = 60\text{ cm}\).\n\n### 3. Option Analysis:\n- Option A is correct: \(60\text{ cm}\)."),

    (7, r"On an architectural blueprint, a room of actual length \(6\text{ m}\) is drawn as \(12\text{ cm}\). What is the drawing scale expressed in ratio form?",
     [r"\(1 : 50\)", r"\(1 : 20\)", r"\(1 : 100\)", r"\(1 : 500\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nDrawing scale \(= \frac{\text{Drawing Length}}{\text{Actual Length}}\).\n\n### 2. Step-by-Step Calculation:\n\(6\text{ m} = 600\text{ cm}\).\nScale \(= \frac{12}{600} = \frac{1}{50} = 1 : 50\).\n\n### 3. Option Analysis:\n- Option A is correct: \(1 : 50\)."),

    (8, r"When a circle's radius is doubled, what happens to its circumference and area respectively?",
     [r"Circumference doubles; area quadruples", r"Both double", r"Both quadruple", r"Circumference quadruples; area doubles"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nCircumference \(C = 2\pi r\) (linear, scales by \(k=2\)). Area \(A = \pi r^2\) (quadratic, scales by \(k^2=4\)).\n\n### 2. Option Analysis:\n- Option A is correct: Circumference doubles and area quadruples."),

    (9, r"A shadow cast by a \(2\text{ m}\) pole is \(3\text{ m}\) long. At the exact same time, a tree casts a shadow of \(18\text{ m}\). What is the height of the tree?",
     [r"\(12\text{ m}\)", r"\(10\text{ m}\)", r"\(15\text{ m}\)", r"\(27\text{ m}\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nAt any given time, sun ray angles produce similar right-angled triangles: \(\frac{\text{Height}}{\text{Shadow}} = \text{constant}\).\n\n### 2. Step-by-Step Calculation:\n\(\frac{H}{18} = \frac{2}{3} \implies H = \frac{2 \times 18}{3} = 12\text{ m}\).\n\n### 3. Option Analysis:\n- Option A is correct: \(12\text{ m}\)."),

    (10, r"A square of side \(s\) is enlarged so that its perimeter increases by \(50\%\). By what percentage does its side length increase?",
     [r"\(50\%\)", r"\(25\%\)", r"\(100\%\)", r"\(125\%\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nBecause perimeter \(P = 4s\) is directly proportional to side length \(s\), any percentage change in perimeter is identical to the percentage change in side length: \(50\%\).\n\n### 2. Option Analysis:\n- Option A is correct: \(50\%\)."),

    (11, r"A rectangular swimming pool measures \(25\text{ m} \times 10\text{ m}\). A scale drawing uses the scale \(1\text{ cm} : 5\text{ m}\). What are the dimensions on paper?",
     [r"\(5\text{ cm} \times 2\text{ cm}\)", r"\(5\text{ cm} \times 5\text{ cm}\)", r"\(2.5\text{ cm} \times 1\text{ cm}\)", r"\(10\text{ cm} \times 4\text{ cm}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nLength on paper \(= \frac{25}{5} = 5\text{ cm}\); Width on paper \(= \frac{10}{5} = 2\text{ cm}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(5\text{ cm} \times 2\text{ cm}\)."),

    (12, r"If a cube has its edges scaled by factor \(k = 2\), the ratio of its original surface area to its new surface area is:",
     [r"\(1 : 4\)", r"\(1 : 2\)", r"\(1 : 8\)", r"\(1 : 6\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nSurface area scales by \(k^2\). For \(k = 2\), ratio is \(1 : 2^2 = 1 : 4\).\n\n### 2. Option Analysis:\n- Option A is correct: \(1 : 4\)."),

    (13, r"A triangle with base \(b\) and height \(h\) has its base tripled and height doubled. What is the ratio of the new area to the original area?",
     [r"\(6 : 1\)", r"\(5 : 1\)", r"\(3 : 2\)", r"\(12 : 1\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\n\(\text{New Area} = \frac{1}{2} (3b)(2h) = 6 \left(\frac{1}{2}bh\right) = 6 \times \text{Original Area}\).\nRatio is \(6 : 1\).\n\n### 2. Option Analysis:\n- Option A is correct: \(6 : 1\)."),

    (14, r"Two gears mesh together. Gear A has 12 teeth and Gear B has 36 teeth. What is the scale ratio of teeth on Gear A to Gear B?",
     [r"\(1 : 3\)", r"\(3 : 1\)", r"\(1 : 4\)", r"\(2 : 5\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nRatio \(= \frac{12}{36} = \frac{1}{3} = 1 : 3\).\n\n### 2. Option Analysis:\n- Option A is correct: \(1 : 3\)."),

    (15, r"A miniature dollhouse table is \(8\text{ cm}\) long. If the dollhouse scale is \(1 : 12\), what is the actual length of the full-sized table?",
     [r"\(96\text{ cm}\)", r"\(1.5\text{ m}\)", r"\(84\text{ cm}\)", r"\(108\text{ cm}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nActual length \(= 8\text{ cm} \times 12 = 96\text{ cm}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(96\text{ cm}\)."),

    (16, r"A cylindrical water bottle is geometrically scaled down such that its height is halved and radius is halved. What fraction of the original volume is the new volume?",
     [r"\(\frac{1}{8}\)", r"\(\frac{1}{4}\)", r"\(\frac{1}{2}\)", r"\(\frac{1}{16}\)"], "A", "OSC", "hard",
     r"### 1. Mathematical Concept & Principle:\nVolume of cylinder \(V = \pi r^2 h\). Both \(r\) and \(h\) scale by \(\frac{1}{2}\).\n\n### 2. Step-by-Step Calculation:\n\(\text{New Volume} = \pi \left(\frac{r}{2}\right)^2 \left(\frac{h}{2}\right) = \frac{1}{8} \pi r^2 h = \frac{1}{8} V\).\n\n### 3. Option Analysis:\n- Option A is correct: \(\frac{1}{8}\)."),

    (17, r"The scale factor between two similar geometric figures is denoted by \(k\). Which of the following statements is ALWAYS true?",
     [r"The ratio of corresponding perimeters is \(k\) and the ratio of corresponding areas is \(k^2\)",
      r"Both perimeters and areas scale by \(k\)",
      r"Perimeter scales by \(k^2\) and area scales by \(k^3\)",
      r"Perimeter scales by \(4k\) and area scales by \(2k\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nLinear measures (length, width, perimeter, circumference) scale by \(k\). Two-dimensional measures (surface area, cross-section area) scale by \(k^2\).\n\n### 2. Option Analysis:\n- Option A is the precise mathematical rule."),

    (18, r"A circular garden plot has diameter \(14\text{ m}\). On a landscape design map, its diameter is \(7\text{ cm}\). What is the representative fraction (RF) of the map?",
     [r"\(1 : 200\)", r"\(1 : 20\)", r"\(1 : 50\)", r"\(1 : 2000\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nConvert actual diameter to cm: \(14\text{ m} = 1400\text{ cm}\).\n\(\text{RF} = \frac{7}{1400} = \frac{1}{200} = 1 : 200\).\n\n### 2. Option Analysis:\n- Option A is correct: \(1 : 200\)."),

    (19, r"If a photo is scaled down by \(20\%\), what is the ratio of the new length to the original length?",
     [r"\(4 : 5\)", r"\(1 : 5\)", r"\(3 : 5\)", r"\(4 : 1\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nNew length \(= 100\% - 20\% = 80\% = \frac{80}{100} = \frac{4}{5}\).\nRatio is \(4 : 5\).\n\n### 2. Option Analysis:\n- Option A is correct: \(4 : 5\)."),

    (20, r"Two concentric circles have radii \(3\text{ cm}\) and \(6\text{ cm}\). What is the ratio of the area of the smaller circle to the area of the ring (annulus) between them?",
     [r"\(1 : 3\)", r"\(1 : 4\)", r"\(1 : 2\)", r"\(1 : 1\)"], "A", "OSC", "hard",
     r"### 1. Mathematical Concept & Principle:\nArea of inner circle \(= \pi (3^2) = 9\pi\).\nArea of outer circle \(= \pi (6^2) = 36\pi\).\nArea of annulus \(= 36\pi - 9\pi = 27\pi\).\nRatio \(= \frac{9\pi}{27\pi} = \frac{1}{3} = 1 : 3\).\n\n### 2. Option Analysis:\n- Option A is correct: \(1 : 3\).")
]

for seq, text, opts, ans, qtype, diff, exp in sub1_exam:
    questions.append(make_q(seq, SUB1_CODE, SUB1_NAME, text, opts, ans, qtype, diff, "exam", "standard", exp))

# --- SUBTOPIC 7.1.2: Ratios in Simplest Form (021 - 040) ---
sub2_exam = [
    (21, r"What is the ratio \(45 : 75\) expressed in its simplest form?",
     [r"\(3 : 5\)", r"\(5 : 3\)", r"\(9 : 15\)", r"\(15 : 25\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nTo express a ratio in simplest form, divide antecedent and consequent by their Highest Common Factor (HCF).\n\n### 2. Step-by-Step Calculation:\n\(\text{HCF}(45, 75) = 15\).\n\(\frac{45 \div 15}{75 \div 15} = \frac{3}{5} = 3 : 5\).\n\n### 3. Option Analysis:\n- Option A is correct: \(3 : 5\)."),

    (22, r"Simplify the ratio of \(250\text{ mL}\) to \(1.5\text{ litres}\).",
     [r"\(1 : 6\)", r"\(1 : 5\)", r"\(5 : 3\)", r"\(1 : 60\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nBoth quantities must be converted to identical units before computing the ratio.\n\n### 2. Step-by-Step Calculation:\n\(1.5\text{ L} = 1500\text{ mL}\).\nRatio \(= \frac{250}{1500} = \frac{1}{6} = 1 : 6\).\n\n### 3. Option Analysis:\n- Option A is correct: \(1 : 6\)."),

    (23, r"What is the simplest form of the ratio \(3\text{ weeks} : 30\text{ days}\)?",
     [r"\(7 : 10\)", r"\(1 : 10\)", r"\(3 : 10\)", r"\(21 : 10\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(3\text{ weeks} = 3 \times 7 = 21\text{ days}\).\nRatio \(= \frac{21}{30} = \frac{7}{10} = 7 : 10\).\n\n### 3. Option Analysis:\n- Option A is correct: \(7 : 10\)."),

    (24, r"Express the ratio \(\frac{2}{3} : \frac{4}{5}\) as a ratio of whole numbers in simplest form.",
     [r"\(5 : 6\)", r"\(6 : 5\)", r"\(8 : 15\)", r"\(10 : 12\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nMultiply both fractions by the LCM of their denominators (\(\text{LCM}(3, 5) = 15\)).\n\n### 2. Step-by-Step Calculation:\n\(\frac{2}{3} \times 15 = 10\); \(\frac{4}{5} \times 15 = 12\).\nRatio \(= 10 : 12 = 5 : 6\).\n\n### 3. Option Analysis:\n- Option A is correct: \(5 : 6\)."),

    (25, r"What is the simplest form of the compound ratio of \(2 : 3\) and \(9 : 4\)?",
     [r"\(3 : 2\)", r"\(2 : 3\)", r"\(18 : 12\)", r"\(1 : 2\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nCompound ratio of \(a : b\) and \(c : d\) is \((a \times c) : (b \times d)\).\n\n### 2. Step-by-Step Calculation:\n\(\frac{2 \times 9}{3 \times 4} = \frac{18}{12} = \frac{3}{2} = 3 : 2\).\n\n### 3. Option Analysis:\n- Option A is correct: \(3 : 2\)."),

    (26, r"Which of the following ratios is equivalent to \(4 : 7\)?",
     [r"\(28 : 49\)", r"\(20 : 30\)", r"\(16 : 21\)", r"\(8 : 15\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nMultiply both terms by 7: \((4 \times 7) : (7 \times 7) = 28 : 49\).\n\n### 2. Option Analysis:\n- Option A is correct: \(28 : 49\)."),

    (27, r"Simplify the continuous ratio \(12 : 18 : 30\).",
     [r"\(2 : 3 : 5\)", r"\(4 : 6 : 10\)", r"\(6 : 9 : 15\)", r"\(1 : 2 : 3\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(\text{HCF}(12, 18, 30) = 6\).\nDividing each term by 6 gives \(2 : 3 : 5\).\n\n### 2. Option Analysis:\n- Option A is correct: \(2 : 3 : 5\)."),

    (28, r"What is the ratio of \(75\text{ paise}\) to \(₹3\)?",
     [r"\(1 : 4\)", r"\(1 : 25\)", r"\(25 : 1\)", r"\(3 : 4\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(₹3 = 300\text{ paise}\).\nRatio \(= \frac{75}{300} = \frac{1}{4} = 1 : 4\).\n\n### 2. Option Analysis:\n- Option A is correct: \(1 : 4\)."),

    (29, r"Simplify the ratio \(1.2 : 0.48\) to whole numbers in lowest terms.",
     [r"\(5 : 2\)", r"\(2 : 5\)", r"\(12 : 5\)", r"\(5 : 4\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nMultiply both numbers by 100 to clear decimals: \(120 : 48\).\nDivide by \(\text{HCF}(120, 48) = 24\): \(\frac{120}{24} : \frac{48}{24} = 5 : 2\).\n\n### 2. Option Analysis:\n- Option A is correct: \(5 : 2\)."),

    (30, r"If \(\frac{A}{B} = \frac{2}{3}\) and \(\frac{B}{C} = \frac{4}{5}\), what is the combined ratio \(A : B : C\)?",
     [r"\(8 : 12 : 15\)", r"\(2 : 4 : 5\)", r"\(6 : 12 : 15\)", r"\(8 : 10 : 15\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nMake the common term \(B\) equal by finding \(\text{LCM}(3, 4) = 12\).\n\n### 2. Step-by-Step Calculation:\n\(A : B = (2 \times 4) : (3 \times 4) = 8 : 12\).\n\(B : C = (4 \times 3) : (5 \times 3) = 12 : 15\).\nTherefore, \(A : B : C = 8 : 12 : 15\).\n\n### 3. Option Analysis:\n- Option A is correct: \(8 : 12 : 15\)."),

    (31, r"What is the duplicate ratio of \(4 : 5\)?",
     [r"\(16 : 25\)", r"\(2 : \sqrt{5}\)", r"\(8 : 10\)", r"\(64 : 125\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nThe duplicate ratio of \(a : b\) is defined as \(a^2 : b^2\).\n\n### 2. Step-by-Step Calculation:\n\(4^2 : 5^2 = 16 : 25\).\n\n### 3. Option Analysis:\n- Option A is correct: \(16 : 25\)."),

    (32, r"What is the sub-duplicate ratio of \(36 : 49\)?",
     [r"\(6 : 7\)", r"\(7 : 6\)", r"\(18 : 24.5\)", r"\(1296 : 2401\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nThe sub-duplicate ratio of \(a : b\) is \(\sqrt{a} : \sqrt{b}\).\n\n### 2. Step-by-Step Calculation:\n\(\sqrt{36} : \sqrt{49} = 6 : 7\).\n\n### 3. Option Analysis:\n- Option A is correct: \(6 : 7\)."),

    (33, r"Which of the two ratios is greater: \(5 : 8\) or \(7 : 11\)?",
     [r"\(7 : 11\)", r"\(5 : 8\)", r"Both are equal", r"Cannot be compared without units"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nCross-multiply to compare: \(5 \times 11 = 55\) and \(7 \times 8 = 56\).\nSince \(56 > 55\), \(\frac{7}{11} > \frac{5}{8}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(7 : 11\)."),

    # 34: OAR
    (34, r"Assertion (A): The ratio of \(500\text{ m}\) to \(2\text{ km}\) is \(1 : 4\).\nReason (R): Two quantities of the same kind can only be compared by ratio after converting them into the same unit.",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"], "A", "OAR", "medium",
     r"### 1. Mathematical Concept & Principle:\nConverting \(2\text{ km} = 2000\text{ m}\) gives \(\frac{500}{2000} = \frac{1}{4} = 1 : 4\). Hence Assertion is true. Reason correctly states the foundational rule of ratios.\n\n### 2. Option Analysis:\n- Option A is correct."),

    # 35: OAR
    (35, r"Assertion (A): The ratio \(3 : 4\) has no units.\nReason (R): A ratio is a quotient obtained by dividing two quantities of the exact same unit, so units cancel out.",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"], "A", "OAR", "easy",
     r"### 1. Mathematical Concept & Principle:\nRatios are pure unitless numbers because the common units in numerator and denominator cancel out.\n\n### 2. Option Analysis:\n- Option A is correct."),

    # 36: OTF
    (36, r"True or False: If both terms of a ratio \(a : b\) are multiplied by the same non-zero constant \(m\), the value of the ratio remains unchanged.",
     ["True", "False"], "A", "OTF", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{ma}{mb} = \frac{a}{b}\) for any non-zero real number \(m\). Multiplying or dividing both terms by a common non-zero number produces an equivalent ratio.\n\n### 2. Option Analysis:\n- Statement is True."),

    # 37: OTF
    (37, r"True or False: The ratio of \(20\text{ cm}\) to \(2\text{ kg}\) can be written as \(10 : 1\).",
     ["False", "True"], "A", "OTF", "easy",
     r"### 1. Mathematical Concept & Principle:\nRatios can ONLY compare quantities of the same physical dimension. Length (\(\text{cm}\)) cannot be compared to Mass (\(\text{kg}\)).\n\n### 2. Option Analysis:\n- Statement is False."),

    # 38: OFB
    (38, r"The simplest integer form of the ratio \(0.75 : 1.25\) is _____ : _____.",
     [r"\(3 : 5\)", r"\(5 : 3\)", r"\(7 : 12\)", r"\(15 : 25\)"], "A", "OFB", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{0.75}{1.25} = \frac{75}{125} = \frac{3}{5} = 3 : 5\).\n\n### 2. Option Analysis:\n- Option A is correct: \(3 : 5\)."),

    # 39: OFB
    (39, r"If a ratio is \(x : 28\) and its simplest equivalent form is \(3 : 4\), then the value of \(x\) is _____.",
     [r"\(21\)", r"\(24\)", r"\(18\)", r"\(20\)"], "A", "OFB", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{x}{28} = \frac{3}{4} \implies x = \frac{3 \times 28}{4} = 21\).\n\n### 2. Option Analysis:\n- Option A is correct: \(21\)."),

    # 40: ONE
    (40, r"In a class of 40 students, 24 are girls and the rest are boys. Calculate the numerical value of the ratio of boys to girls in simplest decimal form.",
     [r"\(0.67\)", r"\(0.60\)", r"\(1.50\)", r"\(0.40\)"], "A", "ONE", "medium",
     r"### 1. Mathematical Concept & Principle:\nNumber of boys \(= 40 - 24 = 16\).\n\(\text{Ratio} = \frac{16}{24} = \frac{2}{3} \approx 0.67\).\n\n### 2. Option Analysis:\n- Option A is correct: \(0.67\).")
]

for seq, text, opts, ans, qtype, diff, exp in sub2_exam:
    questions.append(make_q(seq, SUB2_CODE, SUB2_NAME, text, opts, ans, qtype, diff, "exam", "standard", exp))

# =========================================================================
# PRACTICE VAULT: Questions 041 - 070 (15 for 7.1.1, 15 for 7.1.2)
# =========================================================================

# --- 7.1.1 Practice (041 - 055) ---
sub1_practice = [
    (41, r"A scale model of a building is \(45\text{ cm}\) tall. The actual building is \(90\text{ m}\) tall. What is the scale factor of the model?",
     [r"\(1 : 200\)", r"\(1 : 20\)", r"\(1 : 500\)", r"\(1 : 2000\)"], "A", "OSC", "easy",
     r"Scale factor \(= \frac{45\text{ cm}}{9000\text{ cm}} = \frac{1}{200} = 1 : 200\)."),

    (42, r"A rectangular field has length \(80\text{ m}\) and width \(50\text{ m}\). On a map with scale \(1 : 1000\), what is the perimeter of the field?",
     [r"\(26\text{ cm}\)", r"\(13\text{ cm}\)", r"\(52\text{ cm}\)", r"\(2.6\text{ cm}\)"], "A", "OSC", "medium",
     r"Actual perimeter \(= 2(80 + 50) = 260\text{ m} = 26{,}000\text{ cm}\).\nMap perimeter \(= \frac{26{,}000}{1000} = 26\text{ cm}\)."),

    (43, r"If the linear dimensions of a square are increased by \(10\%\), by what percentage does its area increase?",
     [r"\(21\%\)", r"\(20\%\)", r"\(10\%\)", r"\(100\%\)"], "A", "OSC", "medium",
     r"New side \(= 1.1s\). New area \(= (1.1)^2 s^2 = 1.21 s^2\), which is a \(21\%\) increase."),

    (44, r"Two similar cylinders have radii in the ratio \(3 : 4\). What is the ratio of their base areas?",
     [r"\(9 : 16\)", r"\(3 : 4\)", r"\(27 : 64\)", r"\(6 : 8\)"], "A", "OSC", "easy",
     r"Base area is proportional to \(r^2\). Ratio is \(3^2 : 4^2 = 9 : 16\)."),

    (45, r"A shadow of a vertical stick of length \(1.5\text{ m}\) is \(2.5\text{ m}\). What length of shadow will be cast by a tower \(15\text{ m}\) high at the same instant?",
     [r"\(25\text{ m}\)", r"\(20\text{ m}\)", r"\(30\text{ m}\)", r"\(22.5\text{ m}\)"], "A", "OSC", "medium",
     r"\(\frac{S}{15} = \frac{2.5}{1.5} \implies S = \frac{2.5 \times 15}{1.5} = 25\text{ m}\)."),

    (46, r"On a map with scale \(1\text{ cm} : 25\text{ km}\), two cities are separated by \(3.6\text{ cm}\). What is the actual distance between them?",
     [r"\(90\text{ km}\)", r"\(75\text{ km}\)", r"\(100\text{ km}\)", r"\(80\text{ km}\)"], "A", "OSC", "easy",
     r"Distance \(= 3.6 \times 25 = 90\text{ km}\)."),

    (47, r"If the scale ratio of drawing to actual is \(1 : 25\), what actual area is represented by \(4\text{ cm}^2\) on the drawing?",
     [r"\(2500\text{ cm}^2\)", r"\(100\text{ cm}^2\)", r"\(625\text{ cm}^2\)", r"\(10{,}000\text{ cm}^2\)"], "A", "OSC", "medium",
     r"Area scale factor \(= 25^2 = 625\). Actual area \(= 4 \times 625 = 2500\text{ cm}^2\)."),

    (48, r"A triangle with vertices has area \(12\text{ cm}^2\). If each coordinate is dilated from the origin by a factor of 2.5, what is the new area?",
     [r"\(75\text{ cm}^2\)", r"\(30\text{ cm}^2\)", r"\(60\text{ cm}^2\)", r"\(150\text{ cm}^2\)"], "A", "OSC", "hard",
     r"New area \(= 12 \times (2.5)^2 = 12 \times 6.25 = 75\text{ cm}^2\)."),

    (49, r"A road \(4.8\text{ km}\) long is represented on a map by a line of \(9.6\text{ cm}\). What is the representative fraction of the map?",
     [r"\(1 : 50{,}000\)", r"\(1 : 5{,}000\)", r"\(1 : 20{,}000\)", r"\(1 : 500{,}000\)"], "A", "OSC", "medium",
     r"\(4.8\text{ km} = 480{,}000\text{ cm}\). RF \(= \frac{9.6}{480{,}000} = \frac{1}{50{,}000}\)."),

    (50, r"Two rectangular photo frames are similar. The smaller frame is \(6\text{ cm} \times 9\text{ cm}\). The larger frame has a perimeter of \(60\text{ cm}\). What is the area of the larger frame?",
     [r"\(216\text{ cm}^2\)", r"\(180\text{ cm}^2\)", r"\(240\text{ cm}^2\)", r"\(144\text{ cm}^2\)"], "A", "OSC", "hard",
     r"Smaller perimeter \(= 2(6+9) = 30\text{ cm}\). Linear scale factor \(k = \frac{60}{30} = 2\).\nSmaller area \(= 54\text{ cm}^2\). Larger area \(= 54 \times 2^2 = 216\text{ cm}^2\)."),

    (51, r"If the diameter of a circle is reduced by half, its perimeter is reduced by what percentage?",
     [r"\(50\%\)", r"\(75\%\)", r"\(25\%\)", r"\(100\%\)"], "A", "OSC", "easy",
     r"Perimeter is linear with diameter, so it also reduces by \(50\%\)."),

    (52, r"A rectangular plot of land has dimensions \(150\text{ m} \times 90\text{ m}\). What is the ratio of its breadth to its length?",
     [r"\(3 : 5\)", r"\(5 : 3\)", r"\(2 : 3\)", r"\(3 : 2\)"], "A", "OSC", "easy",
     r"Ratio \(= \frac{90}{150} = \frac{3}{5} = 3 : 5\)."),

    (53, r"A flagpole \(8\text{ m}\) tall casts a shadow of \(6\text{ m}\). At the same moment, a nearby cell tower casts a shadow of \(45\text{ m}\). What is the height of the tower?",
     [r"\(60\text{ m}\)", r"\(50\text{ m}\)", r"\(72\text{ m}\)", r"\(48\text{ m}\)"], "A", "OSC", "medium",
     r"\(\frac{H}{45} = \frac{8}{6} \implies H = \frac{8 \times 45}{6} = 60\text{ m}\)."),

    (54, r"True or False: If two solids are similar with scale factor \(k\), their volumes scale by \(k^3\).",
     ["True", "False"], "A", "OTF", "easy",
     r"Volume is a three-dimensional cubic measure, so it scales strictly by \(k^3\)."),

    (55, r"A miniature car model is \(10\text{ cm}\) long. If the actual car is \(4\text{ m}\) long, the scale ratio in simplest form is 1 : _____.",
     [r"\(40\)", r"\(4\)", r"\(400\)", r"\(25\)"], "A", "OFB", "easy",
     r"\(4\text{ m} = 400\text{ cm}\). Scale \(= \frac{10}{400} = \frac{1}{40} = 1 : 40\).")
]

for seq, text, opts, ans, qtype, diff, exp in sub1_practice:
    questions.append(make_q(seq, SUB1_CODE, SUB1_NAME, text, opts, ans, qtype, diff, "practice", "standard", exp))

# --- 7.1.2 Practice (056 - 070) ---
sub2_practice = [
    (56, r"Express \(1\text{ hour } 20\text{ minutes} : 2\text{ hours}\) in simplest ratio form.",
     [r"\(2 : 3\)", r"\(1 : 2\)", r"\(3 : 4\)", r"\(4 : 5\)"], "A", "OSC", "easy",
     r"\(1\text{ h } 20\text{ min} = 80\text{ min}\); \(2\text{ h} = 120\text{ min}\). Ratio \(= \frac{80}{120} = \frac{2}{3} = 2 : 3\)."),

    (57, r"What is the simplest form of \(1.8\text{ kg} : 600\text{ g}\)?",
     [r"\(3 : 1\)", r"\(1 : 3\)", r"\(18 : 6\)", r"\(30 : 1\)"], "A", "OSC", "easy",
     r"\(1.8\text{ kg} = 1800\text{ g}\). Ratio \(= \frac{1800}{600} = \frac{3}{1} = 3 : 1\)."),

    (58, r"Simplify the fraction ratio \(\frac{3}{8} : \frac{5}{12}\).",
     [r"\(9 : 10\)", r"\(10 : 9\)", r"\(15 : 24\)", r"\(3 : 5\)"], "A", "OSC", "medium",
     r"Multiply by \(\text{LCM}(8, 12) = 24\): \(\frac{3}{8} \times 24 = 9\); \(\frac{5}{12} \times 24 = 10\). Ratio is \(9 : 10\)."),

    (59, r"If \(x : y = 3 : 5\), find the ratio of \((2x + 3y) : (5x - y)\).",
     [r"\(21 : 10\)", r"\(10 : 21\)", r"\(7 : 4\)", r"\(15 : 8\)"], "A", "OSC", "medium",
     r"Substitute \(x = 3k, y = 5k\): \(\frac{2(3) + 3(5)}{5(3) - 5} = \frac{6 + 15}{15 - 5} = \frac{21}{10} = 21 : 10\)."),

    (60, r"Simplify the three-term ratio \(0.5 : 1.25 : 2.5\).",
     [r"\(2 : 5 : 10\)", r"\(1 : 2.5 : 5\)", r"\(4 : 10 : 25\)", r"\(1 : 3 : 5\)"], "A", "OSC", "medium",
     r"Multiply by 100: \(50 : 125 : 250\). Divide by 25: \(2 : 5 : 10\)."),

    (61, r"Which ratio is larger: \(4 : 5\) or \(5 : 6\)?",
     [r"\(5 : 6\)", r"\(4 : 5\)", r"Both are equal", r"Cannot be evaluated"], "A", "OSC", "easy",
     r"\(\frac{4}{5} = 0.80\) and \(\frac{5}{6} \approx 0.833\). Since \(0.833 > 0.80\), \(5 : 6\) is larger."),

    (62, r"What is the triplicate ratio of \(2 : 3\)?",
     [r"\(8 : 27\)", r"\(6 : 9\)", r"\(4 : 9\)", r"\(16 : 81\)"], "A", "OSC", "medium",
     r"Triplicate ratio is \(a^3 : b^3 = 2^3 : 3^3 = 8 : 27\)."),

    (63, r"If \(A : B = 5 : 6\) and \(B : C = 8 : 9\), what is \(A : C\)?",
     [r"\(20 : 27\)", r"\(5 : 9\)", r"\(10 : 13\)", r"\(40 : 54\)"], "A", "OSC", "medium",
     r"\(\frac{A}{C} = \frac{A}{B} \times \frac{B}{C} = \frac{5}{6} \times \frac{8}{9} = \frac{40}{54} = \frac{20}{27}\)."),

    (64, r"What is the sub-triplicate ratio of \(64 : 343\)?",
     [r"\(4 : 7\)", r"\(8 : 49\)", r"\(16 : 49\)", r"\(7 : 4\)"], "A", "OSC", "medium",
     r"Sub-triplicate ratio is \(\sqrt[3]{64} : \sqrt[3]{343} = 4 : 7\)."),

    (65, r"In a bouquet of 60 flowers, 25 are roses, 15 are lilies, and the rest are orchids. What is the simplified ratio of orchids to roses?",
     [r"\(4 : 5\)", r"\(5 : 4\)", r"\(3 : 5\)", r"\(1 : 2\)"], "A", "OSC", "medium",
     r"Orchids \(= 60 - (25 + 15) = 20\). Ratio orchids : roses \(= \frac{20}{25} = \frac{4}{5} = 4 : 5\)."),

    (66, r"True or False: If \(a : b = c : d\), then \((a + b) : b = (c + d) : d\). (Componendo property)",
     ["True", "False"], "A", "OTF", "medium",
     r"\(\frac{a}{b} + 1 = \frac{c}{d} + 1 \implies \frac{a+b}{b} = \frac{c+d}{d}\). This is the Componendo property, which is True."),

    (67, r"True or False: The inverse ratio of \(7 : 11\) is \(11 : 7\).",
     ["True", "False"], "A", "OTF", "easy",
     r"The reciprocal / inverse ratio of \(a : b\) is \(b : a\). Statement is True."),

    (68, r"The simplest ratio of \(45\text{ seconds}\) to \(3\text{ minutes}\) is 1 : _____.",
     [r"\(4\)", r"\(6\)", r"\(3\)", r"\(15\)"], "A", "OFB", "easy",
     r"\(3\text{ min} = 180\text{ s}\). \(\frac{45}{180} = \frac{1}{4} = 1 : 4\)."),

    (69, r"If \(3A = 4B = 6C\), then \(A : B : C\) in simplest integer terms is _____ : _____ : _____.",
     [r"\(4 : 3 : 2\)", r"\(3 : 4 : 6\)", r"\(6 : 4 : 3\)", r"\(2 : 3 : 4\)"], "A", "OFB", "hard",
     r"Divide by \(\text{LCM}(3,4,6) = 12\): \(\frac{3A}{12} = \frac{4B}{12} = \frac{6C}{12} \implies \frac{A}{4} = \frac{B}{3} = \frac{C}{2}\). Ratio is \(4 : 3 : 2\)."),

    (70, r"Two numbers are in the ratio \(7 : 9\). If their sum is 144, find the smaller number.",
     [r"\(63\)", r"\(81\)", r"\(56\)", r"\(72\)"], "A", "ONE", "medium",
     r"\(7x + 9x = 16x = 144 \implies x = 9\). Smaller number \(= 7 \times 9 = 63\).")
]

for seq, text, opts, ans, qtype, diff, exp in sub2_practice:
    questions.append(make_q(seq, SUB2_CODE, SUB2_NAME, text, opts, ans, qtype, diff, "practice", "standard", exp))

# =========================================================================
# FOUNDATION VAULT: Questions 071 - 082 (Challenging / Olympiad)
# =========================================================================
foundation_q = [
    (71, SUB1_CODE, SUB1_NAME,
     r"A solid gold statue of height \(10\text{ cm}\) weighs \(2\text{ kg}\). A geometrically similar statue of the exact same solid gold has a height of \(20\text{ cm}\). What is the weight of the larger statue?",
     [r"\(16\text{ kg}\)", r"\(8\text{ kg}\)", r"\(4\text{ kg}\)", r"\(32\text{ kg}\)"], "A", "OSC", "hard",
     r"### 1. Mathematical Concept & Principle:\nMass and weight of solid objects of uniform density scale with volume (\(k^3\)).\n\n### 2. Step-by-Step Calculation:\nScale factor \(k = \frac{20}{10} = 2\).\nVolume scales by \(k^3 = 2^3 = 8\).\nNew weight \(= 2\text{ kg} \times 8 = 16\text{ kg}\).\n\n### 3. Option Analysis:\n- Option A is correct: \(16\text{ kg}\)."),

    (72, SUB1_CODE, SUB1_NAME,
     r"A square sheet of metal of side \(10\text{ cm}\) expands uniformly when heated such that its area increases by \(4.04\%\). By what percentage does its side length increase?",
     [r"\(2\%\)", r"\(4\%\)", r"\(1.02\%\)", r"\(2.02\%\)"], "A", "OSC", "hard",
     r"New Area \(= 1.0404 A\). Scale factor \(k = \sqrt{1.0404} = 1.02\).\nPercentage increase in side length \(= (1.02 - 1) \times 100\% = 2\%\)."),

    (73, SUB1_CODE, SUB1_NAME,
     r"In a blueprint drawing with scale \(1 : 50\), a circular fountain is depicted with area \(12\pi\text{ cm}^2\). What is the actual ground area occupied by the fountain in square meters?",
     [r"\(30\pi\text{ m}^2\)", r"\(3\pi\text{ m}^2\)", r"\(15\pi\text{ m}^2\)", r"\(60\pi\text{ m}^2\)"], "A", "OSC", "hard",
     r"Area scale factor \(= 50^2 = 2500\).\nActual area \(= 12\pi \times 2500\text{ cm}^2 = 30{,}000\pi\text{ cm}^2 = 3\pi\text{ m}^2\). Wait: \(30{,}000 / 10{,}000 = 3\pi\text{ m}^2\). Let's check options: [\(3\pi\text{ m}^2\), \(30\pi\text{ m}^2\), \(1.2\pi\text{ m}^2\), \(12\pi\text{ m}^2\)].",
     ),

    (74, SUB1_CODE, SUB1_NAME,
     r"Two similar water reservoirs have capacity ratio \(27 : 64\). If the surface water area of the smaller reservoir is \(180\text{ m}^2\), what is the surface water area of the larger reservoir?",
     [r"\(320\text{ m}^2\)", r"\(240\text{ m}^2\)", r"\(400\text{ m}^2\)", r"\(426.6\text{ m}^2\)"], "A", "OSC", "hard",
     r"Capacity is volume: \(\frac{V_1}{V_2} = \left(\frac{r_1}{r_2}\right)^3 = \frac{27}{64} \implies \frac{r_1}{r_2} = \frac{3}{4}\).\nArea scales with square of linear dimensions: \(\frac{A_1}{A_2} = \left(\frac{3}{4}\right)^2 = \frac{9}{16}\).\n\(A_2 = 180 \times \frac{16}{9} = 320\text{ m}^2\)."),

    (75, SUB1_CODE, SUB1_NAME,
     r"An aerial drone photo covers a rectangular farmland parcel measuring \(6\text{ cm} \times 4\text{ cm}\). If the actual farm area is \(6\text{ hectares}\) (\(1\text{ ha} = 10{,}000\text{ m}^2\)), what is the scale ratio of the photo?",
     [r"\(1 : 5{,}000\)", r"\(1 : 2{,}500\)", r"\(1 : 10{,}000\)", r"\(1 : 50{,}000\)"], "A", "OSC", "hard",
     r"Actual area \(= 6 \times 10{,}000\text{ m}^2 = 60{,}000\text{ m}^2 = 600{,}000{,}000\text{ cm}^2\).\nPhoto area \(= 24\text{ cm}^2\).\nArea ratio \(= \frac{600{,}000{,}000}{24} = 25{,}000{,}000\).\nLinear scale ratio \(= \sqrt{25{,}000{,}000} = 5{,}000\), so scale is \(1 : 5{,}000\)."),

    (76, SUB1_CODE, SUB1_NAME,
     r"A cone is sliced by a horizontal plane parallel to its base at half its vertical height from the apex. What is the ratio of the volume of the smaller cone to the volume of the frustum remaining below?",
     [r"\(1 : 7\)", r"\(1 : 8\)", r"\(1 : 4\)", r"\(1 : 3\)"], "A", "OSC", "hard",
     r"Linear scale factor of small cone is \(\frac{1}{2}\). Volume of small cone is \(\left(\frac{1}{2}\right)^3 = \frac{1}{8}\) of the total cone volume.\nFrustum volume \(= 1 - \frac{1}{8} = \frac{7}{8}\).\nRatio of small cone to frustum \(= \frac{1/8}{7/8} = 1 : 7\)."),

    (77, SUB2_CODE, SUB2_NAME,
     r"If \(\frac{a}{b+c} = \frac{b}{c+a} = \frac{c}{a+b}\) for non-zero real numbers with \(a+b+c \neq 0\), what is the unique common numerical value of each ratio?",
     [r"\(\frac{1}{2}\)", r"\(1\)", r"\(2\)", r"\(\frac{1}{3}\)"], "A", "OSC", "hard",
     r"By the theorem of equal ratios, each ratio equals \(\frac{a+b+c}{(b+c)+(c+a)+(a+b)} = \frac{a+b+c}{2(a+b+c)} = \frac{1}{2}\)."),

    (78, SUB2_CODE, SUB2_NAME,
     r"If \(x : y = 2 : 3\), \(y : z = 4 : 5\), and \(z : w = 6 : 7\), what is the value of \(x : w\)?",
     [r"\(16 : 35\)", r"\(8 : 35\)", r"\(12 : 35\)", r"\(24 : 35\)"], "A", "OSC", "hard",
     r"\(\frac{x}{w} = \frac{x}{y} \times \frac{y}{z} \times \frac{z}{w} = \frac{2}{3} \times \frac{4}{5} \times \frac{6}{7} = \frac{48}{105} = \frac{16}{35}\)."),

    (79, SUB2_CODE, SUB2_NAME,
     r"What quantity must be added to each term of the ratio \(7 : 11\) so that it becomes equal to \(3 : 4\)?",
     [r"\(5\)", r"\(4\)", r"\(6\)", r"\(3\)"], "A", "OSC", "medium",
     r"\(\frac{7+x}{11+x} = \frac{3}{4} \implies 28 + 4x = 33 + 3x \implies x = 5\)."),

    (80, SUB2_CODE, SUB2_NAME,
     r"If \(x, y, z\) satisfy \(\frac{x}{2} = \frac{y}{3} = \frac{z}{5}\) and \(2x - 3y + 4z = 60\), find the value of \(x + y + z\).",
     [r"\(40\)", r"\(50\)", r"\(30\)", r"\(60\)"], "A", "OSC", "hard",
     r"Let \(\frac{x}{2} = \frac{y}{3} = \frac{z}{5} = k\). Then \(x=2k, y=3k, z=5k\).\n\(2(2k) - 3(3k) + 4(5k) = 4k - 9k + 20k = 15k = 60 \implies k = 4\).\n\(x + y + z = 2k + 3k + 5k = 10k = 10 \times 4 = 40\)."),

    (81, SUB2_CODE, SUB2_NAME,
     r"Two positive numbers are in the ratio \(3 : 5\). If 8 is added to both, the ratio becomes \(2 : 3\). Determine the numerical value of the larger number.",
     [r"\(40\)", r"\(24\)", r"\(32\)", r"\(48\)"], "A", "ONE", "hard",
     r"\(\frac{3x+8}{5x+8} = \frac{2}{3} \implies 9x + 24 = 10x + 16 \implies x = 8\).\nLarger number \(= 5x = 5 \times 8 = 40\)."),

    (82, SUB2_CODE, SUB2_NAME,
     r"Three containers have capacities in the ratio \(1 : 2 : 3\). All are completely filled with milk and water mixtures where the ratio of milk to water is \(2 : 3\), \(3 : 1\), and \(4 : 5\) respectively. If all contents are poured into a large vessel, find the ratio of total milk to total water.",
     [r"\(283 : 317\)", r"\(260 : 340\)", r"\(1 : 1\)", r"\(317 : 283\)"], "A", "OSC", "hard",
     r"Take capacities as 20, 40, 60 (total 120, LCM of 5, 4, 9 is 180; let total capacities be 180, 360, 540).\nIn C1 (180): Milk \(= \frac{2}{5} \times 180 = 72\), Water \(= 108\).\nIn C2 (360): Milk \(= \frac{3}{4} \times 360 = 270\), Water \(= 90\).\nIn C3 (540): Milk \(= \frac{4}{9} \times 540 = 240\), Water \(= 300\).\nTotal Milk \(= 72 + 270 + 240 = 582\).\nTotal Water \(= 108 + 90 + 300 = 498\).\nWait: \(\frac{582}{498} = \frac{97}{83}\). Let's use direct options: [r\"\(97 : 83\)\", r\"\(83 : 97\)\", r\"\(3 : 2\)\", r\"\(4 : 3\)\"]. Correct: \(97 : 83\).")
]

# Fix 73 options
foundation_q[2] = (73, SUB1_CODE, SUB1_NAME,
     r"In a blueprint drawing with scale \(1 : 50\), a circular fountain is depicted with area \(12\pi\text{ cm}^2\). What is the actual ground area occupied by the fountain in square meters?",
     [r"\(3\pi\text{ m}^2\)", r"\(30\pi\text{ m}^2\)", r"\(1.2\pi\text{ m}^2\)", r"\(12\pi\text{ m}^2\)"], "A", "OSC", "hard",
     r"Area scale factor \(= 50^2 = 2500\).\nActual area \(= 12\pi \times 2500\text{ cm}^2 = 30{,}000\pi\text{ cm}^2 = 3\pi\text{ m}^2\).")

# Fix 82 options
foundation_q[11] = (82, SUB2_CODE, SUB2_NAME,
     r"Three containers have capacities in the ratio \(1 : 2 : 3\). All are completely filled with milk and water mixtures where the ratio of milk to water is \(2 : 3\), \(3 : 1\), and \(4 : 5\) respectively. If all contents are poured into a large vessel, find the ratio of total milk to total water in simplest form.",
     [r"\(97 : 83\)", r"\(83 : 97\)", r"\(3 : 2\)", r"\(4 : 3\)"], "A", "OSC", "hard",
     r"Take capacities as 180, 360, 540 (ratio \(1 : 2 : 3\)).\nIn Container 1: Milk \(= \frac{2}{5} \times 180 = 72\), Water \(= 108\).\nIn Container 2: Milk \(= \frac{3}{4} \times 360 = 270\), Water \(= 90\).\nIn Container 3: Milk \(= \frac{4}{9} \times 540 = 240\), Water \(= 300\).\nTotal Milk \(= 72 + 270 + 240 = 582\).\nTotal Water \(= 108 + 90 + 300 = 498\).\nRatio \(= \frac{582}{498} = \frac{97}{83}\).")

for seq, sub_code, sub_name, text, opts, ans, qtype, diff, exp in foundation_q:
    questions.append(make_q(seq, sub_code, sub_name, text, opts, ans, qtype, diff, "foundation", "foundation", exp))

out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch7_t1.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"✅ Generated {len(questions)} questions for Topic 7.1 -> {out_path}")
