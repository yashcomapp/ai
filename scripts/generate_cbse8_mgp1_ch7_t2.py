# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-7-7.2
Topic: Comparing Mixtures & Concentration using Ratios
Subtopic 7.2.1: Comparing sweetness/taste/mixtures using ratios
Subtopic 7.2.2: Unit conversions for ratio consistency
Vaults: 40 Exam (001-040) + 30 Practice (041-070) + 12 Foundation (071-082)
"""

import json
import os

PARENT_TOPIC_CODE = "CBSE-8-MGP1-7-7.2"
PARENT_TOPIC_NAME = "Comparing Mixtures & Concentration using Ratios"
CH_NUM = 7
SUB1_CODE = "CBSE-8-MGP1-7-7.2.1"
SUB1_NAME = "Comparing sweetness/taste/mixtures using ratios"
SUB2_CODE = "CBSE-8-MGP1-7-7.2.2"
SUB2_NAME = "Unit conversions for ratio consistency"

def make_q(seq, sub_code, sub_name, text, options, answer_letter, qtype, difficulty, vault, category, explanation):
    qnum_str = f"{seq:03d}"
    doc_id = f"CBSE-8-MGP1-7-7.2-{qtype}-{qnum_str}"
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
# EXAM VAULT: Questions 001 - 040 (20 for 7.2.1, 20 for 7.2.2)
# =========================================================================

sub1_exam = [
    (1, r"Lemonade Mix A is prepared with 2 spoons of sugar in \(250\text{ mL}\) of water, while Mix B has 3 spoons of sugar in \(300\text{ mL}\) of water. Which mix is sweeter?",
     [r"Mix B", r"Mix A", r"Both are equally sweet", r"Cannot be compared without knowing spoon volume"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nSweetness is determined by the ratio of solute (sugar) to solvent (water) or total volume.\n\n### 2. Step-by-Step Calculation:\nMix A: \(\frac{2}{250} = \frac{1}{125} = 0.008\text{ spoons/mL}\).\nMix B: \(\frac{3}{300} = \frac{1}{100} = 0.010\text{ spoons/mL}\).\nSince \(0.010 > 0.008\), Mix B has a higher concentration of sugar and is sweeter.\n\n### 3. Option Analysis:\n- Option A is correct: Mix B."),

    (2, r"Jar 1 has a milk-to-water ratio of \(3 : 1\), and Jar 2 has a milk-to-water ratio of \(5 : 2\). Which jar has a higher concentration of milk?",
     [r"Jar 1", r"Jar 2", r"Both have equal concentration", r"Jar 2 because it has 5 parts milk"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nCompare the fraction of milk in the total mixture for each jar.\n\n### 2. Step-by-Step Calculation:\nJar 1 fraction of milk: \(\frac{3}{3+1} = \frac{3}{4} = 75\%\).\nJar 2 fraction of milk: \(\frac{5}{5+2} = \frac{5}{7} \approx 71.4\%\).\nSince \(75\% > 71.4\%\), Jar 1 is more concentrated in milk.\n\n### 3. Option Analysis:\n- Option A is correct: Jar 1."),

    (3, r"In a chemical dye, Blue dye and Yellow dye are mixed in the ratio \(2 : 3\) to make green paint. In a batch of \(30\text{ litres}\) of green paint, how many litres of blue dye are present?",
     [r"\(12\text{ L}\)", r"\(18\text{ L}\)", r"\(15\text{ L}\)", r"\(10\text{ L}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nFraction of Blue \(= \frac{2}{2+3} = \frac{2}{5}\).\nVolume of Blue \(= \frac{2}{5} \times 30 = 12\text{ litres}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(12\text{ L}\)."),

    (4, r"Two sugar syrups are tested: Syrup P contains \(40\text{ g}\) sugar in \(200\text{ g}\) syrup. Syrup Q contains \(50\text{ g}\) sugar in \(300\text{ g}\) syrup. Which syrup has a higher percentage concentration?",
     [r"Syrup P", r"Syrup Q", r"Both are equal", r"Syrup Q has more sugar, so it is higher"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nConcentration P: \(\frac{40}{200} \times 100\% = 20\%\).\nConcentration Q: \(\frac{50}{300} \times 100\% \approx 16.67\%\).\nSyrup P has higher concentration.\n\n### 2. Option Analysis:\n- Option A is correct: Syrup P."),

    (5, r"A brass alloy contains Copper and Zinc in the ratio \(7 : 3\). If an ornament made of this brass weighs \(450\text{ g}\), what is the mass of zinc in it?",
     [r"\(135\text{ g}\)", r"\(315\text{ g}\)", r"\(150\text{ g}\)", r"\(100\text{ g}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nZinc fraction \(= \frac{3}{7+3} = \frac{3}{10}\).\nMass of Zinc \(= \frac{3}{10} \times 450 = 135\text{ g}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(135\text{ g}\)."),

    (6, r"A tea vendor prepares Chai Batch 1 with 4 cups milk and 1 cup water. Batch 2 is prepared with 7 cups milk and 2 cups water. Which batch has a richer milk taste?",
     [r"Batch 1", r"Batch 2", r"Both have identical richness", r"Cannot be evaluated"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nBatch 1 milk fraction: \(\frac{4}{4+1} = \frac{4}{5} = 0.80\) (\(80\%\)).\nBatch 2 milk fraction: \(\frac{7}{7+2} = \frac{7}{9} \approx 0.778\) (\(77.8\%\)).\nBatch 1 has higher milk proportion.\n\n### 2. Option Analysis:\n- Option A is correct: Batch 1."),

    (7, r"A saline solution has a salt-to-water ratio of \(1 : 19\). What is the percentage of salt in this solution?",
     [r"\(5\%\)", r"\(5.26\%\)", r"\(10\%\)", r"\(19\%\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nTotal parts \(= 1 + 19 = 20\).\nPercentage of salt \(= \frac{1}{20} \times 100\% = 5\%\).\n\n### 2. Option Analysis:\n- Option A is correct: \(5\%\)."),

    (8, r"In Mixture A, acid and water are in the ratio \(1 : 4\). In Mixture B, acid and water are in the ratio \(1 : 3\). If equal quantities of both are taken, which contains more acid?",
     [r"Mixture B", r"Mixture A", r"Both contain equal acid", r"Depends on the total volume"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nFraction of acid in A \(= \frac{1}{5} = 0.20\).\nFraction of acid in B \(= \frac{1}{4} = 0.25\).\nSince \(0.25 > 0.20\), Mixture B contains more acid.\n\n### 2. Option Analysis:\n- Option A is correct: Mixture B."),

    (9, r"To paint a wall, a painter mixes red paint and white paint in the ratio \(3 : 5\) to get pink. If he uses \(15\text{ litres}\) of white paint, how much red paint is required?",
     [r"\(9\text{ L}\)", r"\(10\text{ L}\)", r"\(12\text{ L}\)", r"\(25\text{ L}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{\text{Red}}{\text{White}} = \frac{3}{5} \implies \frac{\text{Red}}{15} = \frac{3}{5} \implies \text{Red} = \frac{3 \times 15}{5} = 9\text{ litres}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(9\text{ L}\)."),

    (10, r"A concrete mixture requires cement, sand, and gravel in the ratio \(1 : 2 : 4\). How many kilograms of sand are needed to make \(140\text{ kg}\) of concrete?",
     [r"\(40\text{ kg}\)", r"\(20\text{ kg}\)", r"\(80\text{ kg}\)", r"\(70\text{ kg}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nTotal parts \(= 1 + 2 + 4 = 7\).\nSand amount \(= \frac{2}{7} \times 140 = 40\text{ kg}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(40\text{ kg}\)."),

    (11, r"In an orchard, the ratio of mango trees to apple trees is \(7 : 4\). If there are 84 mango trees, how many apple trees are there?",
     [r"\(48\)", r"\(56\)", r"\(36\)", r"\(42\)" ], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{7}{4} = \frac{84}{\text{Apple}} \implies \text{Apple} = \frac{84 \times 4}{7} = 12 \times 4 = 48\).\n\n### 2. Option Analysis:\n- Option A is correct: 48."),

    (12, r"A bronze statue contains copper, tin, and zinc in the ratio \(85 : 12 : 3\). In a statue weighing \(50\text{ kg}\), what is the mass of tin?",
     [r"\(6\text{ kg}\)", r"\(12\text{ kg}\)", r"\(4.5\text{ kg}\)", r"\(1.5\text{ kg}\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nTotal parts \(= 85 + 12 + 3 = 100\).\nMass of tin \(= \frac{12}{100} \times 50 = 6\text{ kg}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(6\text{ kg}\)."),

    (13, r"Two syrups X and Y are mixed in equal amounts. X is \(20\%\) sugar solution and Y is \(40\%\) sugar solution. What is the sugar concentration of the resulting mixture?",
     [r"\(30\%\)", r"\(60\%\)", r"\(25\%\)", r"\(35\%\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nSince equal volumes are mixed, the concentration is the arithmetic mean: \(\frac{20 + 40}{2} = 30\%\).\n\n### 2. Option Analysis:\n- Option A is correct: \(30\%\)."),

    (14, r"A recipe for fruit punch calls for orange juice and pineapple juice in the ratio \(5 : 3\). If you have \(1.5\text{ litres}\) of pineapple juice, how much orange juice must you use?",
     [r"\(2.5\text{ L}\)", r"\(2.0\text{ L}\)", r"\(3.0\text{ L}\)", r"\(1.8\text{ L}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{\text{Orange}}{1.5} = \frac{5}{3} \implies \text{Orange} = \frac{5 \times 1.5}{3} = 2.5\text{ L}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(2.5\text{ L}\)."),

    (15, r"A liquid detergent recommends diluting 1 part concentrate with 9 parts water. What is the concentration of the detergent in the final diluted solution?",
     [r"\(10\%\)", r"\(11.1\%\)", r"\(9\%\)", r"\(1\%\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nTotal parts \(= 1 + 9 = 10\).\nConcentration \(= \frac{1}{10} \times 100\% = 10\%\).\n\n### 2. Option Analysis:\n- Option A is correct: \(10\%\)."),

    (16, r"Container 1 has milk and water in the ratio \(4 : 1\). Container 2 has milk and water in the ratio \(7 : 3\). Which container has a greater proportion of water?",
     [r"Container 2", r"Container 1", r"Both have equal water proportion", r"Container 1 because it has only 1 part water"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nWater fraction in C1 \(= \frac{1}{4+1} = \frac{1}{5} = 20\%\).\nWater fraction in C2 \(= \frac{3}{7+3} = \frac{3}{10} = 30\%\).\nSince \(30\% > 20\%\), Container 2 has a greater proportion of water.\n\n### 2. Option Analysis:\n- Option A is correct: Container 2."),

    (17, r"An alloy consists of \(60\%\) gold, \(30\%\) silver, and the rest copper. What is the simplified ratio of gold : silver : copper?",
     [r"\(6 : 3 : 1\)", r"\(2 : 1 : 1\)", r"\(3 : 2 : 1\)", r"\(6 : 3 : 2\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nCopper percentage \(= 100\% - (60\% + 30\%) = 10\%\).\nRatio \(= 60 : 30 : 10 = 6 : 3 : 1\).\n\n### 2. Option Analysis:\n- Option A is correct: \(6 : 3 : 1\)."),

    (18, r"If \(500\text{ mL}\) of pure alcohol is mixed with \(1500\text{ mL}\) of water, what is the ratio of alcohol to the total mixture?",
     [r"\(1 : 4\)", r"\(1 : 3\)", r"\(3 : 4\)", r"\(1 : 5\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nTotal mixture \(= 500 + 1500 = 2000\text{ mL}\).\nRatio \(= \frac{500}{2000} = \frac{1}{4} = 1 : 4\).\n\n### 2. Option Analysis:\n- Option A is correct: \(1 : 4\)."),

    (19, r"To make cough syrup, medicine base and honey are mixed in the ratio \(1 : 8\). In \(720\text{ mL}\) of cough syrup, what volume of honey is present?",
     [r"\(640\text{ mL}\)", r"\(600\text{ mL}\)", r"\(80\text{ mL}\)", r"\(560\text{ mL}\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nTotal parts \(= 1 + 8 = 9\).\nHoney volume \(= \frac{8}{9} \times 720 = 8 \times 80 = 640\text{ mL}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(640\text{ mL}\)."),

    (20, r"Two brands of soil fertilizer have Nitrogen to Potassium ratios: Brand A has \(3 : 2\) and Brand B has \(4 : 3\). Which brand provides a higher proportion of Nitrogen?",
     [r"Brand A", r"Brand B", r"Both are equal", r"Brand B has 4 parts, so it is always higher"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nNitrogen fraction in Brand A \(= \frac{3}{3+2} = \frac{3}{5} = 0.60\) (\(60\%\)).\nNitrogen fraction in Brand B \(= \frac{4}{4+3} = \frac{4}{7} \approx 0.571\) (\(57.1\%\)).\nBrand A has higher nitrogen concentration.\n\n### 2. Option Analysis:\n- Option A is correct: Brand A.")
]

for seq, text, opts, ans, qtype, diff, exp in sub1_exam:
    questions.append(make_q(seq, SUB1_CODE, SUB1_NAME, text, opts, ans, qtype, diff, "exam", "standard", exp))

# --- SUBTOPIC 7.2.2: Unit Conversions for Ratio Consistency (021 - 040) ---
sub2_exam = [
    (21, r"What is the ratio of \(40\text{ paise}\) to \(₹2\) in simplest form?",
     [r"\(1 : 5\)", r"\(1 : 20\)", r"\(20 : 1\)", r"\(1 : 50\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nConvert rupees to paise: \(₹2 = 200\text{ paise}\).\n\(\text{Ratio} = \frac{40}{200} = \frac{1}{5} = 1 : 5\).\n\n### 2. Option Analysis:\n- Option A is correct: \(1 : 5\)."),

    (22, r"Express the ratio of \(75\text{ cm}\) to \(1.5\text{ metres}\) in lowest terms.",
     [r"\(1 : 2\)", r"\(1 : 5\)", r"\(2 : 1\)", r"\(1 : 20\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(1.5\text{ m} = 150\text{ cm}\).\nRatio \(= \frac{75}{150} = \frac{1}{2} = 1 : 2\).\n\n### 2. Option Analysis:\n- Option A is correct: \(1 : 2\)."),

    (23, r"What is the simplest ratio comparing \(250\text{ grams}\) to \(2\text{ kilograms}\)?",
     [r"\(1 : 8\)", r"\(1 : 4\)", r"\(1 : 16\)", r"\(8 : 1\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(2\text{ kg} = 2000\text{ g}\).\nRatio \(= \frac{250}{2000} = \frac{1}{8} = 1 : 8\).\n\n### 2. Option Analysis:\n- Option A is correct: \(1 : 8\)."),

    (24, r"What is the ratio of \(30\text{ minutes}\) to \(2\text{ hours } 15\text{ minutes}\)?",
     [r"\(2 : 9\)", r"\(1 : 4\)", r"\(2 : 7\)", r"\(1 : 5\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\n\(2\text{ h } 15\text{ min} = (2 \times 60) + 15 = 135\text{ min}\).\nRatio \(= \frac{30}{135} = \frac{2}{9} = 2 : 9\).\n\n### 2. Option Analysis:\n- Option A is correct: \(2 : 9\)."),

    (25, r"Find the ratio of \(1.2\text{ litres}\) to \(400\text{ millilitres}\).",
     [r"\(3 : 1\)", r"\(1 : 3\)", r"\(4 : 3\)", r"\(30 : 1\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(1.2\text{ L} = 1200\text{ mL}\).\nRatio \(= \frac{1200}{400} = \frac{3}{1} = 3 : 1\).\n\n### 2. Option Analysis:\n- Option A is correct: \(3 : 1\)."),

    (26, r"What is the ratio of \(6\text{ days}\) to \(3\text{ weeks}\)?",
     [r"\(2 : 7\)", r"\(1 : 2\)", r"\(2 : 1\)", r"\(1 : 7\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(3\text{ weeks} = 3 \times 7 = 21\text{ days}\).\nRatio \(= \frac{6}{21} = \frac{2}{7} = 2 : 7\).\n\n### 2. Option Analysis:\n- Option A is correct: \(2 : 7\)."),

    (27, r"What is the ratio of \(500\text{ m}\) to \(3.5\text{ km}\)?",
     [r"\(1 : 7\)", r"\(1 : 5\)", r"\(5 : 3.5\)", r"\(1 : 70\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(3.5\text{ km} = 3500\text{ m}\).\nRatio \(= \frac{500}{3500} = \frac{1}{7} = 1 : 7\).\n\n### 2. Option Analysis:\n- Option A is correct: \(1 : 7\)."),

    (28, r"Express the ratio of \(5\text{ mm}\) to \(2\text{ cm}\) in lowest terms.",
     [r"\(1 : 4\)", r"\(5 : 2\)", r"\(1 : 2\)", r"\(1 : 40\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(2\text{ cm} = 20\text{ mm}\).\nRatio \(= \frac{5}{20} = \frac{1}{4} = 1 : 4\).\n\n### 2. Option Analysis:\n- Option A is correct: \(1 : 4\)."),

    (29, r"What is the ratio of \(3\text{ hours}\) to \(1\text{ day}\)?",
     [r"\(1 : 8\)", r"\(1 : 6\)", r"\(3 : 24\)", r"\(1 : 12\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(1\text{ day} = 24\text{ hours}\).\nRatio \(= \frac{3}{24} = \frac{1}{8} = 1 : 8\).\n\n### 2. Option Analysis:\n- Option A is correct: \(1 : 8\)."),

    (30, r"Find the ratio of \(1.5\text{ metric tonnes}\) to \(750\text{ kg}\). (\(1\text{ tonne} = 1000\text{ kg}\))",
     [r"\(2 : 1\)", r"\(1 : 2\)", r"\(15 : 7.5\)", r"\(20 : 1\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(1.5\text{ tonnes} = 1500\text{ kg}\).\nRatio \(= \frac{1500}{750} = \frac{2}{1} = 2 : 1\).\n\n### 2. Option Analysis:\n- Option A is correct: \(2 : 1\)."),

    (31, r"What is the ratio of \(12\text{ dozen}\) to \(2\text{ gross}\)? (\(1\text{ gross} = 12\text{ dozen} = 144\))",
     [r"\(1 : 2\)", r"\(6 : 1\)", r"\(1 : 12\)", r"\(2 : 1\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\n\(2\text{ gross} = 2 \times 12\text{ dozen} = 24\text{ dozen}\).\nRatio \(= \frac{12}{24} = \frac{1}{2} = 1 : 2\).\n\n### 2. Option Analysis:\n- Option A is correct: \(1 : 2\)."),

    (32, r"Compare the speed of a cyclist riding at \(18\text{ km/h}\) with a sprinter running at \(6\text{ m/s}\) as a ratio.",
     [r"\(5 : 6\)", r"\(3 : 1\)", r"\(6 : 5\)", r"\(1 : 1\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nConvert \(18\text{ km/h}\) to \(\text{m/s}\): \(18 \times \frac{5}{18} = 5\text{ m/s}\).\nRatio \(= \frac{5\text{ m/s}}{6\text{ m/s}} = 5 : 6\).\n\n### 2. Option Analysis:\n- Option A is correct: \(5 : 6\)."),

    (33, r"What is the ratio of \(200\text{ square centimeters}\) to \(1\text{ square meter}\)?",
     [r"\(1 : 50\)", r"\(1 : 5\)", r"\(1 : 500\)", r"\(2 : 1\)"], "A", "OSC", "hard",
     r"### 1. Mathematical Concept & Principle:\n\(1\text{ m}^2 = 100\text{ cm} \times 100\text{ cm} = 10{,}000\text{ cm}^2\).\nRatio \(= \frac{200}{10{,}000} = \frac{1}{50} = 1 : 50\).\n\n### 2. Option Analysis:\n- Option A is correct: \(1 : 50\)."),

    # 34: OAR
    (34, r"Assertion (A): The ratio of \(250\text{ g}\) to \(1\text{ kg}\) is \(1 : 4\).\nReason (R): In evaluating the ratio of two physical quantities, both must always be converted into the same unit before division.",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"], "A", "OAR", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(1\text{ kg} = 1000\text{ g}\). Ratio \(= \frac{250}{1000} = \frac{1}{4} = 1 : 4\). Assertion and Reason are true, and (R) explains (A).\n\n### 2. Option Analysis:\n- Option A is correct."),

    # 35: OAR
    (35, r"Assertion (A): The ratio between \(4\text{ hours}\) and \(40\text{ km}\) is \(1 : 10\).\nReason (R): Quantities with different units cannot form a ratio.",
     ["(A) is false but (R) is true",
      "Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false"], "A", "OAR", "medium",
     r"### 1. Mathematical Concept & Principle:\nA ratio is only defined between quantities of the SAME kind (same physical dimension). Time cannot be compared to Distance by ratio. Hence (A) is false and (R) is true.\n\n### 2. Option Analysis:\n- Option A is correct."),

    # 36: OTF
    (36, r"True or False: To find the ratio of \(2\text{ weeks}\) to \(14\text{ days}\), both must be expressed in days, yielding the ratio \(1 : 1\).",
     ["True", "False"], "A", "OTF", "easy",
     r"\(2\text{ weeks} = 14\text{ days}\). Ratio is \(\frac{14}{14} = 1 : 1\). Statement is True."),

    (37, r"True or False: The ratio of \(50\text{ paise}\) to \(₹5\) is \(1 : 10\).",
     ["True", "False"], "A", "OTF", "easy",
     r"\(₹5 = 500\text{ paise}\). \(\frac{50}{500} = \frac{1}{10} = 1 : 10\). Statement is True."),

    # 38: OFB
    (38, r"The ratio of \(750\text{ mL}\) to \(3\text{ L}\) in simplest form is 1 : _____.",
     [r"\(4\)", r"\(2\)", r"\(5\)", r"\(3\)"], "A", "OFB", "easy",
     r"\(3\text{ L} = 3000\text{ mL}\). \(\frac{750}{3000} = \frac{1}{4} = 1 : 4\)."),

    # 39: OFB
    (39, r"The ratio of \(45\text{ minutes}\) to \(1\text{ hour } 15\text{ minutes}\) in simplest form is _____ : _____.",
     [r"\(3 : 5\)", r"\(5 : 3\)", r"\(3 : 4\)", r"\(9 : 15\)"], "A", "OFB", "easy",
     r"\(1\text{ h } 15\text{ min} = 75\text{ min}\). Ratio \(= \frac{45}{75} = \frac{3}{5} = 3 : 5\)."),

    # 40: ONE
    (40, r"Evaluate the simplified ratio of \(1.5\text{ km}\) to \(600\text{ m}\). Express your answer as a decimal number.",
     [r"\(2.5\)", r"\(2.25\)", r"\(0.4\)", r"\(2.0\)"], "A", "ONE", "easy",
     r"\(1.5\text{ km} = 1500\text{ m}\). Ratio \(= \frac{1500}{600} = \frac{5}{2} = 2.5\).")
]

for seq, text, opts, ans, qtype, diff, exp in sub2_exam:
    questions.append(make_q(seq, SUB2_CODE, SUB2_NAME, text, opts, ans, qtype, diff, "exam", "standard", exp))

# =========================================================================
# PRACTICE VAULT: Questions 041 - 070 (15 for 7.2.1, 15 for 7.2.2)
# =========================================================================

sub1_practice = [
    (41, r"In a sweet shop, Rasgulla syrup has sugar and water in the ratio \(3 : 7\), while Gulab Jamun syrup has sugar and water in the ratio \(2 : 5\). Which syrup has a higher sugar percentage?",
     [r"Rasgulla syrup", r"Gulab Jamun syrup", r"Both are equal", r"Cannot be compared"], "A", "OSC", "medium",
     r"Rasgulla: \(\frac{3}{10} = 30\%\). Gulab Jamun: \(\frac{2}{7} \approx 28.57\%\). Rasgulla is higher."),

    (42, r"A blend of green tea contains Darjeeling leaf and Assam leaf in the ratio \(5 : 2\). How much Assam leaf is needed to prepare \(350\text{ g}\) of the blend?",
     [r"\(100\text{ g}\)", r"\(250\text{ g}\)", r"\(150\text{ g}\)", r"\(70\text{ g}\)"], "A", "OSC", "easy",
     r"Assam fraction \(= \frac{2}{7}\). Amount \(= \frac{2}{7} \times 350 = 100\text{ g}\)."),

    (43, r"Two car radiator coolants are tested: Coolant A has antifreeze to water ratio \(1 : 3\); Coolant B has antifreeze to water ratio \(2 : 5\). Which coolant has greater freeze protection (higher antifreeze concentration)?",
     [r"Coolant B", r"Coolant A", r"Both provide equal protection", r"Coolant A because it has only 1 part"], "A", "OSC", "medium",
     r"Coolant A: \(\frac{1}{4} = 25\%\). Coolant B: \(\frac{2}{7} \approx 28.6\%\). Coolant B has higher concentration."),

    (44, r"Mortar for bricklaying requires cement and sand in the ratio \(1 : 5\). How many bags of sand are needed if a builder uses 6 bags of cement?",
     [r"\(30\)", r"\(25\)", r"\(36\)", r"\(18\)"], "A", "OSC", "easy",
     r"Sand \(= 6 \times 5 = 30\text{ bags}\)."),

    (45, r"In a school library, the ratio of fiction books to non-fiction books is \(5 : 8\). If there are 600 fiction books, how many non-fiction books are in the library?",
     [r"\(960\)", r"\(840\)", r"\(1000\)", r"\(750\)"], "A", "OSC", "easy",
     r"\(\frac{5}{8} = \frac{600}{N} \implies N = \frac{600 \times 8}{5} = 960\)."),

    (46, r"A fruit drink contains \(15\%\) real fruit juice and the rest is sugar water. What is the ratio of real fruit juice to sugar water?",
     [r"\(3 : 17\)", r"\(3 : 20\)", r"\(1 : 6\)", r"\(3 : 14\)"], "A", "OSC", "easy",
     r"Sugar water \(= 100 - 15 = 85\%\). Ratio \(= \frac{15}{85} = \frac{3}{17} = 3 : 17\)."),

    (47, r"An alloy consists of \(70\%\) copper and \(30\%\) nickel. What is the ratio of nickel to copper?",
     [r"\(3 : 7\)", r"\(7 : 3\)", r"\(3 : 10\)", r"\(7 : 10\)"], "A", "OSC", "easy",
     r"Ratio nickel : copper \(= \frac{30}{70} = 3 : 7\)."),

    (48, r"Two bottles of orange squash: Bottle 1 instructions say mix 1 part squash with 4 parts water. Bottle 2 says mix 1 part squash with 5 parts water. Which prepared glass is more concentrated in fruit squash?",
     [r"Bottle 1", r"Bottle 2", r"Both are equal", r"Bottle 2 because it uses 5 parts water"], "A", "OSC", "easy",
     r"Bottle 1: \(\frac{1}{5} = 20\%\). Bottle 2: \(\frac{1}{6} \approx 16.7\%\). Bottle 1 is more concentrated."),

    (49, r"In an exam, the ratio of students who passed to students who failed is \(9 : 2\). If 18 students failed, what is the total number of students who appeared for the exam?",
     [r"\(99\)", r"\(81\)", r"\(90\)", r"\(108\)"], "A", "OSC", "medium",
     r"\(2x = 18 \implies x = 9\). Total students \(= (9+2)x = 11 \times 9 = 99\)."),

    (50, r"A baker mixes whole wheat flour and refined flour in the ratio \(3 : 2\) to make multi-grain bread. To make \(25\text{ kg}\) of flour blend, how much whole wheat flour is needed?",
     [r"\(15\text{ kg}\)", r"\(10\text{ kg}\)", r"\(12.5\text{ kg}\)", r"\(18\text{ kg}\)"], "A", "OSC", "easy",
     r"Amount \(= \frac{3}{5} \times 25 = 15\text{ kg}\)."),

    (51, r"In a solution of salt water, salt makes up \(8\%\) of the total mass. What is the ratio of salt to water?",
     [r"\(2 : 23\)", r"\(2 : 25\)", r"\(8 : 100\)", r"\(1 : 12\)"], "A", "OSC", "medium",
     r"Water percentage \(= 92\%\). Ratio \(= \frac{8}{92} = \frac{2}{23} = 2 : 23\)."),

    (52, r"A metal solder is an alloy of lead and tin in the ratio \(3 : 2\). What percentage of the solder is tin?",
     [r"\(40\%\)", r"\(60\%\)", r"\(20\%\)", r"\(66.7\%\)"], "A", "OSC", "easy",
     r"Tin percentage \(= \frac{2}{5} \times 100\% = 40\%\)."),

    (53, r"In a survey, 4 out of every 5 respondents preferred home-cooked meals over restaurant food. What is the ratio of respondents preferring home-cooked food to those preferring restaurant food?",
     [r"\(4 : 1\)", r"\(4 : 5\)", r"\(5 : 4\)", r"\(1 : 4\)"], "A", "OSC", "easy",
     r"Restaurant preference \(= 5 - 4 = 1\). Ratio is \(4 : 1\)."),

    (54, r"True or False: If Solution X has milk to water ratio \(2 : 3\) and Solution Y has milk to water ratio \(3 : 2\), Solution Y contains a higher concentration of milk.",
     ["True", "False"], "A", "OTF", "easy",
     r"Solution X milk fraction is \(\frac{2}{5} = 40\%\). Solution Y milk fraction is \(\frac{3}{5} = 60\%\). True."),

    (55, r"A brass bell weighs \(1200\text{ g}\) and is made of copper and zinc in the ratio \(5 : 1\). The mass of copper in the bell is _____ grams.",
     [r"\(1000\)", r"\(200\)", r"\(800\)", r"\(900\)"], "A", "OFB", "easy",
     r"Copper mass \(= \frac{5}{6} \times 1200 = 1000\text{ g}\).")
]

for seq, text, opts, ans, qtype, diff, exp in sub1_practice:
    questions.append(make_q(seq, SUB1_CODE, SUB1_NAME, text, opts, ans, qtype, diff, "practice", "standard", exp))

# --- 7.2.2 Practice (056 - 070) ---
sub2_practice = [
    (56, r"What is the simplest form of the ratio comparing \(15\text{ cm}\) to \(2\text{ m}\)?",
     [r"\(3 : 40\)", r"\(3 : 4\)", r"\(15 : 2\)", r"\(3 : 20\)"], "A", "OSC", "easy",
     r"\(2\text{ m} = 200\text{ cm}\). \(\frac{15}{200} = \frac{3}{40} = 3 : 40\)."),

    (57, r"Find the ratio of \(250\text{ mL}\) to \(2\text{ L } 500\text{ mL}\).",
     [r"\(1 : 10\)", r"\(1 : 5\)", r"\(1 : 9\)", r"\(1 : 25\)"], "A", "OSC", "easy",
     r"\(2\text{ L } 500\text{ mL} = 2500\text{ mL}\). \(\frac{250}{2500} = \frac{1}{10} = 1 : 10\)."),

    (58, r"What is the ratio of \(1\text{ hour } 45\text{ minutes}\) to \(35\text{ minutes}\)?",
     [r"\(3 : 1\)", r"\(1 : 3\)", r"\(2 : 1\)", r"\(5 : 1\)"], "A", "OSC", "easy",
     r"\(1\text{ h } 45\text{ min} = 105\text{ min}\). \(\frac{105}{35} = \frac{3}{1} = 3 : 1\)."),

    (59, r"What is the ratio of \(50\text{ cm}^2\) to \(1\text{ m}^2\)?",
     [r"\(1 : 200\)", r"\(1 : 20\)", r"\(1 : 50\)", r"\(1 : 2000\)"], "A", "OSC", "hard",
     r"\(1\text{ m}^2 = 10{,}000\text{ cm}^2\). \(\frac{50}{10{,}000} = \frac{1}{200} = 1 : 200\)."),

    (60, r"What is the ratio of \(300\text{ g}\) to \(1.5\text{ kg}\)?",
     [r"\(1 : 5\)", r"\(1 : 2\)", r"\(2 : 1\)", r"\(1 : 50\)"], "A", "OSC", "easy",
     r"\(1.5\text{ kg} = 1500\text{ g}\). \(\frac{300}{1500} = \frac{1}{5} = 1 : 5\)."),

    (61, r"Find the ratio of \(90\text{ seconds}\) to \(3\text{ minutes}\).",
     [r"\(1 : 2\)", r"\(1 : 3\)", r"\(2 : 1\)", r"\(3 : 1\)"], "A", "OSC", "easy",
     r"\(3\text{ min} = 180\text{ s}\). \(\frac{90}{180} = \frac{1}{2} = 1 : 2\)."),

    (62, r"Express \(8\text{ months} : 2\text{ years}\) in simplest form.",
     [r"\(1 : 3\)", r"\(4 : 1\)", r"\(1 : 4\)", r"\(2 : 3\)"], "A", "OSC", "easy",
     r"\(2\text{ years} = 24\text{ months}\). \(\frac{8}{24} = \frac{1}{3} = 1 : 3\)."),

    (63, r"What is the ratio of \(4\text{ m } 50\text{ cm}\) to \(9\text{ m}\)?",
     [r"\(1 : 2\)", r"\(1 : 3\)", r"\(2 : 1\)", r"\(1 : 4\)"], "A", "OSC", "easy",
     r"\(450\text{ cm} : 900\text{ cm} = 1 : 2\)."),

    (64, r"What is the ratio of \(75\text{ paise}\) to \(₹1.50\)?",
     [r"\(1 : 2\)", r"\(1 : 3\)", r"\(2 : 1\)", r"\(3 : 4\)"], "A", "OSC", "easy",
     r"\(₹1.50 = 150\text{ paise}\). \(\frac{75}{150} = \frac{1}{2} = 1 : 2\)."),

    (65, r"What is the ratio of \(25\text{ mm}\) to \(1\text{ m}\)?",
     [r"\(1 : 40\)", r"\(1 : 4\)", r"\(1 : 400\)", r"\(1 : 25\)"], "A", "OSC", "medium",
     r"\(1\text{ m} = 1000\text{ mm}\). \(\frac{25}{1000} = \frac{1}{40} = 1 : 40\)."),

    (66, r"True or False: The ratio of \(50\text{ mL}\) to \(1\text{ L}\) is \(1 : 20\).",
     ["True", "False"], "A", "OTF", "easy",
     r"\(1\text{ L} = 1000\text{ mL}\). \(\frac{50}{1000} = \frac{1}{20} = 1 : 20\). True."),

    (67, r"True or False: The ratio of \(2\text{ km}\) to \(200\text{ m}\) is \(10 : 1\).",
     ["True", "False"], "A", "OTF", "easy",
     r"\(2\text{ km} = 2000\text{ m}\). \(\frac{2000}{200} = 10 : 1\). True."),

    (68, r"The ratio of \(20\text{ minutes}\) to \(1\text{ hour } 20\text{ minutes}\) in lowest terms is 1 : _____.",
     [r"\(4\)", r"\(3\)", r"\(5\)", r"\(6\)"], "A", "OFB", "easy",
     r"\(1\text{ h } 20\text{ min} = 80\text{ min}\). \(\frac{20}{80} = \frac{1}{4} = 1 : 4\)."),

    (69, r"The ratio of \(350\text{ g}\) to \(1.4\text{ kg}\) in simplest form is 1 : _____.",
     [r"\(4\)", r"\(2\)", r"\(3\)", r"\(5\)"], "A", "OFB", "easy",
     r"\(1.4\text{ kg} = 1400\text{ g}\). \(\frac{350}{1400} = \frac{1}{4} = 1 : 4\)."),

    (70, r"Compute the numerical value of the ratio of \(72\text{ km/h}\) to \(25\text{ m/s}\).",
     [r"\(0.8\)", r"\(1.2\)", r"\(0.72\)", r"\(1.0\)"], "A", "ONE", "medium",
     r"\(72\text{ km/h} = 72 \times \frac{5}{18} = 20\text{ m/s}\). Ratio \(= \frac{20}{25} = 0.8\).")
]

for seq, text, opts, ans, qtype, diff, exp in sub2_practice:
    questions.append(make_q(seq, SUB2_CODE, SUB2_NAME, text, opts, ans, qtype, diff, "practice", "standard", exp))

# =========================================================================
# FOUNDATION VAULT: Questions 071 - 082 (Challenging / Olympiad)
# =========================================================================

foundation_q = [
    (71, SUB1_CODE, SUB1_NAME,
     r"Two vessels A and B contain mixtures of milk and water in the ratios \(7 : 2\) and \(5 : 1\) respectively. In what ratio should the contents of both vessels be mixed to obtain a new mixture containing milk and water in the ratio \(4 : 1\)?",
     [r"\(3 : 2\)", r"\(2 : 3\)", r"\(1 : 2\)", r"\(5 : 3\)"], "A", "OSC", "hard",
     r"### 1. Mathematical Concept & Principle:\nUse allegation rule on milk fractions: Milk in A \(= \frac{7}{9}\), Milk in B \(= \frac{5}{6}\), Target milk \(= \frac{4}{5}\).\n\n### 2. Step-by-Step Calculation:\nDifference 1: \(|\frac{5}{6} - \frac{4}{5}| = \frac{1}{30}\).\nDifference 2: \(|\frac{4}{5} - \frac{7}{9}| = \frac{36 - 35}{45} = \frac{1}{45}\).\nRatio of A : B \(= \frac{1/30}{1/45} = \frac{45}{30} = \frac{3}{2} = 3 : 2\).\n\n### 3. Option Analysis:\n- Option A is correct: \(3 : 2\)."),

    (72, SUB1_CODE, SUB1_NAME,
     r"A \(60\text{ litre}\) container is filled with a mixture of milk and water in the ratio \(2 : 1\). How much water must be added to this mixture so that the ratio of milk to water becomes \(1 : 2\)?",
     [r"\(60\text{ L}\)", r"\(40\text{ L}\)", r"\(80\text{ L}\)", r"\(20\text{ L}\)"], "A", "OSC", "hard",
     r"Initially: Milk \(= 40\text{ L}\), Water \(= 20\text{ L}\).\nLet added water be \(w\).\n\(\frac{40}{20+w} = \frac{1}{2} \implies 20 + w = 80 \implies w = 60\text{ litres}\)."),

    (73, SUB1_CODE, SUB1_NAME,
     r"A mixture contains alcohol and water in the ratio \(4 : 3\). If \(5\text{ litres}\) of water is added to the mixture, the ratio becomes \(4 : 5\). Find the original quantity of alcohol in the mixture.",
     [r"\(10\text{ L}\)", r"\(8\text{ L}\)", r"\(12\text{ L}\)", r"\(15\text{ L}\)"], "A", "OSC", "hard",
     r"Let alcohol \(= 4x\), water \(= 3x\).\n\(\frac{4x}{3x+5} = \frac{4}{5} \implies 5x = 3x + 5 \implies 2x = 5 \implies x = 2.5\).\nAlcohol \(= 4(2.5) = 10\text{ litres}\)."),

    (74, SUB1_CODE, SUB1_NAME,
     r"Two alloys both contain Copper and Zinc. Alloy 1 has Copper to Zinc in ratio \(3 : 2\) and Alloy 2 in ratio \(4 : 1\). If \(20\text{ kg}\) of Alloy 1 and \(30\text{ kg}\) of Alloy 2 are melted together, what is the ratio of Copper to Zinc in the new ingot?",
     [r"\(18 : 7\)", r"\(7 : 18\)", r"\(5 : 2\)", r"\(16 : 9\)"], "A", "OSC", "hard",
     r"In Alloy 1 (\(20\text{ kg}\)): Copper \(= \frac{3}{5} \times 20 = 12\text{ kg}\), Zinc \(= 8\text{ kg}\).\nIn Alloy 2 (\(30\text{ kg}\)): Copper \(= \frac{4}{5} \times 30 = 24\text{ kg}\), Zinc \(= 6\text{ kg}\).\nTotal Copper \(= 12 + 24 = 36\text{ kg}\).\nTotal Zinc \(= 8 + 6 = 14\text{ kg}\).\nRatio \(= \frac{36}{14} = \frac{18}{7} = 18 : 7\)."),

    (75, SUB1_CODE, SUB1_NAME,
     r"A container has \(80\text{ litres}\) of pure milk. \(8\text{ litres}\) of milk is drawn out and replaced by water. This process is repeated one more time. What is the final quantity of milk remaining in the container?",
     [r"\(64.8\text{ L}\)", r"\(64.0\text{ L}\)", r"\(62.4\text{ L}\)", r"\(66.2\text{ L}\)"], "A", "OSC", "hard",
     r"Formula: \(Q = Q_0 \left(1 - \frac{x}{Q_0}\right)^n = 80 \left(1 - \frac{8}{80}\right)^2 = 80 (0.9)^2 = 80 \times 0.81 = 64.8\text{ L}\)."),

    (76, SUB1_CODE, SUB1_NAME,
     r"In two alloys of Gold and Silver, the ratio of gold to silver is \(7 : 2\) and \(7 : 11\). If equal weights of both alloys are melted together to form a third alloy, find the ratio of gold to silver in the third alloy.",
     [r"\(7 : 5\)", r"\(5 : 7\)", r"\(14 : 13\)", r"\(9 : 7\)"], "A", "OSC", "hard",
     r"Let equal weights be \(18\text{ g}\) each (LCM of 9 and 18).\nFrom Alloy 1 (\(18\text{ g}\)): Gold \(= \frac{7}{9} \times 18 = 14\text{ g}\), Silver \(= 4\text{ g}\).\nFrom Alloy 2 (\(18\text{ g}\)): Gold \(= \frac{7}{18} \times 18 = 7\text{ g}\), Silver \(= 11\text{ g}\).\nTotal Gold \(= 14 + 7 = 21\text{ g}\).\nTotal Silver \(= 4 + 11 = 15\text{ g}\).\nRatio \(= \frac{21}{15} = \frac{7}{5} = 7 : 5\)."),

    (77, SUB2_CODE, SUB2_NAME,
     r"If the speed of Sound in air is \(340\text{ m/s}\) and a commercial jet travels at \(850\text{ km/h}\), what is the ratio of the speed of the jet to the speed of sound?",
     [r"\(25 : 36\)", r"\(36 : 25\)", r"\(5 : 7\)", r"\(2 : 3\)"], "A", "OSC", "hard",
     r"Jet speed \(= 850 \times \frac{5}{18} = \frac{4250}{18} = \frac{2125}{9}\text{ m/s}\).\nRatio \(= \frac{2125/9}{340} = \frac{2125}{3060} = \frac{25}{36} = 25 : 36\)."),

    (78, SUB2_CODE, SUB2_NAME,
     r"The mass of Earth is approximately \(6 \times 10^{24}\text{ kg}\) and the mass of the Moon is \(7.5 \times 10^{22}\text{ kg}\). What is the ratio of the mass of the Earth to the mass of the Moon in simplest integer form?",
     [r"\(80 : 1\)", r"\(8 : 1\)", r"\(800 : 1\)", r"\(100 : 1\)"], "A", "OSC", "hard",
     r"Ratio \(= \frac{6 \times 10^{24}}{7.5 \times 10^{22}} = \frac{600}{7.5} = 80 = 80 : 1\)."),

    (79, SUB2_CODE, SUB2_NAME,
     r"A water pump discharges water at a rate of \(15\text{ liters per second}\). Another pump fills a tank at \(72\text{ cubic meters per hour}\). What is the ratio of the pumping rate of the first pump to that of the second pump?",
     [r"\(3 : 4\)", r"\(4 : 3\)", r"\(1 : 2\)", r"\(5 : 6\)"], "A", "OSC", "hard",
     r"Pump 1: \(15\text{ L/s} = 15 \times 3600\text{ L/h} = 54{,}000\text{ L/h} = 54\text{ m}^3\text{/h}\).\nRatio \(= \frac{54}{72} = \frac{3}{4} = 3 : 4\)."),

    (80, SUB2_CODE, SUB2_NAME,
     r"On a topographic map with scale \(1 : 25{,}000\), an irregular forest reserve measures \(16\text{ cm}^2\). What is the actual area of the reserve in square kilometers?",
     [r"\(1\text{ km}^2\)", r"\(4\text{ km}^2\)", r"\(0.5\text{ km}^2\)", r"\(2\text{ km}^2\)"], "A", "OSC", "hard",
     r"Linear scale: \(1\text{ cm} = 250\text{ m} = 0.25\text{ km}\).\nArea scale: \(1\text{ cm}^2 = (0.25)^2\text{ km}^2 = 0.0625\text{ km}^2\).\nActual area \(= 16 \times 0.0625 = 1\text{ km}^2\)."),

    (81, SUB2_CODE, SUB2_NAME,
     r"A car travels at \(54\text{ km/h}\) for 20 minutes, then accelerates to \(90\text{ km/h}\) for the next 40 minutes. Calculate the ratio of distance covered in the first part to distance covered in the second part in decimal form.",
     [r"\(0.30\)", r"\(0.25\)", r"\(0.50\)", r"\(0.40\)"], "A", "ONE", "hard",
     r"Distance 1 \(= 54 \times \frac{20}{60} = 18\text{ km}\).\nDistance 2 \(= 90 \times \frac{40}{60} = 60\text{ km}\).\nRatio \(= \frac{18}{60} = \frac{3}{10} = 0.30\)."),

    (82, SUB2_CODE, SUB2_NAME,
     r"Three vessels each of capacity 10 liters contain mixtures of acid and water in the ratios \(2 : 1\), \(3 : 1\), and \(3 : 2\). If all three vessels are emptied into a large vat, find the ratio of total acid to total water in the vat.",
     [r"\(121 : 59\)", r"\(59 : 121\)", r"\(2 : 1\)", r"\(110 : 70\)"], "A", "OSC", "hard",
     r"Let each capacity be 60 units (LCM of 3, 4, 5 is 60).\nIn V1: Acid \(= \frac{2}{3} \times 60 = 40\), Water \(= 20\).\nIn V2: Acid \(= \frac{3}{4} \times 60 = 45\), Water \(= 15\).\nIn V3: Acid \(= \frac{3}{5} \times 60 = 36\), Water \(= 24\).\nTotal Acid \(= 40 + 45 + 36 = 121\).\nTotal Water \(= 20 + 15 + 24 = 59\).\nRatio \(= 121 : 59\).")
]

for seq, sub_code, sub_name, text, opts, ans, qtype, diff, exp in foundation_q:
    questions.append(make_q(seq, sub_code, sub_name, text, opts, ans, qtype, diff, "foundation", "foundation", exp))

out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch7_t2.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"✅ Generated {len(questions)} questions for Topic 7.2 -> {out_path}")
