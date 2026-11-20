# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-7-7.4
Topic: The Rule of Three (Trairasika) & Direct Proportion Word Problems
Subtopic 7.4.1: Trairasika method for finding the fourth proportional
Subtopic 7.4.2: Direct proportion word problems
Vaults: 40 Exam (001-040) + 30 Practice (041-070) + 12 Foundation (071-082)
"""

import json
import os

PARENT_TOPIC_CODE = "CBSE-8-MGP1-7-7.4"
PARENT_TOPIC_NAME = "The Rule of Three (Trairasika) & Direct Proportion Word Problems"
CH_NUM = 7
SUB1_CODE = "CBSE-8-MGP1-7-7.4.1"
SUB1_NAME = "Trairasika method for finding the fourth proportional"
SUB2_CODE = "CBSE-8-MGP1-7-7.4.2"
SUB2_NAME = "Direct proportion word problems"

def make_q(seq, sub_code, sub_name, text, options, answer_letter, qtype, difficulty, vault, category, explanation):
    qnum_str = f"{seq:03d}"
    doc_id = f"CBSE-8-MGP1-7-7.4-{qtype}-{qnum_str}"
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
# EXAM VAULT: Questions 001 - 040 (20 for 7.4.1, 20 for 7.4.2)
# =========================================================================

sub1_exam = [
    (1, r"In ancient Indian mathematics (Aryabhatiya and Lilavati), what is the Rule of Three called?",
     [r"Trairasika (त्रैराशिक)", r"Pancharasika", r"Saptarasika", r"Kuttaka"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nThe method of finding an unknown fourth quantity from three given related quantities in proportion is historically termed Trairasika (त्रैराशिक) in ancient Indian mathematics.\n\n### 2. Option Analysis:\n- Option A is correct: Trairasika."),

    (2, r"In the classical Trairasika method, if Pramana (measure), Phala (fruit/yield), and Iccha (requisition/desire) are known, what is the formula for Icchaphala (desired result)?",
     [r"\(\text{Icchaphala} = \frac{\text{Phala} \times \text{Iccha}}{\text{Pramana}}\)",
      r"\(\text{Icchaphala} = \frac{\text{Pramana} \times \text{Phala}}{\text{Iccha}}\)",
      r"\(\text{Icchaphala} = \frac{\text{Pramana} \times \text{Iccha}}{\text{Phala}}\)",
      r"\(\text{Icchaphala} = \text{Phala} \times \text{Iccha} \times \text{Pramana}\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nAccording to Bhaskaracharya's Lilavati:\n\\[\n\\text{Icchaphala} = \\frac{\\text{Phala} \\times \\text{Iccha}}{\\text{Pramana}}\n\\]\nSince \(\\frac{\\text{Pramana}}{\\text{Phala}} = \\frac{\\text{Iccha}}{\\text{Icchaphala}}\).\n\n### 2. Option Analysis:\n- Option A is correct."),

    (3, r"If 5 kg of rice costs \(₹240\), what is the cost of 12 kg of rice at the same rate?",
     [r"\(₹576\)", r"\(₹540\)", r"\(₹600\)", r"\(₹480\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nDirect proportion: \(\frac{\text{Cost}_1}{\text{Weight}_1} = \frac{\text{Cost}_2}{\text{Weight}_2}\).\n\n### 2. Step-by-Step Calculation:\n\(\text{Cost} = \frac{240}{5} \times 12 = 48 \times 12 = ₹576\).\n\n### 3. Option Analysis:\n- Option A is correct: \(₹576\)."),

    (4, r"A car consumes 4 litres of petrol to travel \(60\text{ km}\). How far can it travel on 15 litres of petrol?",
     [r"\(225\text{ km}\)", r"\(240\text{ km}\)", r"\(200\text{ km}\)", r"\(180\text{ km}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nDistance per litre \(= \frac{60}{4} = 15\text{ km/L}\).\nDistance on 15 L \(= 15 \times 15 = 225\text{ km}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(225\text{ km}\)."),

    (5, r"If 18 workers construct a \(90\text{ m}\) boundary wall in one day, how many meters of wall can 30 workers construct in one day under the same conditions?",
     [r"\(150\text{ m}\)", r"\(160\text{ m}\)", r"\(120\text{ m}\)", r"\(140\text{ m}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nLength \(= \frac{90}{18} \times 30 = 5 \times 30 = 150\text{ m}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(150\text{ m}\)."),

    (6, r"If a machine labels 450 bottles in 15 minutes, how many bottles does it label in 1 hour?",
     [r"\(1800\)", r"\(1500\)", r"\(1200\)", r"\(2400\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n1 hour \(= 60\text{ minutes}\).\nRate \(= \frac{450}{15} = 30\text{ bottles/min}\).\nTotal bottles \(= 30 \times 60 = 1800\).\n\n### 2. Option Analysis:\n- Option A is correct: 1800."),

    (7, r"The cost of 16 meters of ribbon is \(₹256\). How many meters of the same ribbon can be purchased for \(₹400\)?",
     [r"\(25\text{ m}\)", r"\(20\text{ m}\)", r"\(30\text{ m}\)", r"\(24\text{ m}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nCost per meter \(= \frac{256}{16} = ₹16\text{ /m}\).\nMeters for \(₹400 = \frac{400}{16} = 25\text{ m}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(25\text{ m}\)."),

    (8, r"If 3 men take 15 days to paint a house, does the time taken increase or decrease with more men? Is this direct or inverse proportion?",
     [r"Decreases; Inverse proportion", r"Increases; Direct proportion", r"Decreases; Direct proportion", r"Increases; Inverse proportion"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nMore workers require less time to complete the same task (\(\text{Men} \times \text{Days} = \text{Constant}\)). Therefore, this is an Inverse proportion, not direct.\n\n### 2. Option Analysis:\n- Option A is correct."),

    (9, r"If 8 identical books weigh \(4.8\text{ kg}\), what is the weight of 25 such books?",
     [r"\(15\text{ kg}\)", r"\(12\text{ kg}\)", r"\(16\text{ kg}\)", r"\(14.4\text{ kg}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nWeight per book \(= \frac{4.8}{8} = 0.6\text{ kg}\).\nWeight of 25 books \(= 25 \times 0.6 = 15\text{ kg}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(15\text{ kg}\)."),

    (10, r"A train travels \(165\text{ km}\) in 3 hours at constant speed. How far will it travel in 7 hours?",
     [r"\(385\text{ km}\)", r"\(350\text{ km}\)", r"\(400\text{ km}\)", r"\(375\text{ km}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nSpeed \(= \frac{165}{3} = 55\text{ km/h}\).\nDistance \(= 55 \times 7 = 385\text{ km}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(385\text{ km}\)."),

    (11, r"If a shadow of a \(14\text{ m}\) tall tree is \(10\text{ m}\), what is the height of a pole that casts a shadow of \(15\text{ m}\) at the same time?",
     [r"\(21\text{ m}\)", r"\(20\text{ m}\)", r"\(18\text{ m}\)", r"\(25\text{ m}\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{14}{10} = \frac{H}{15} \implies H = \frac{14 \times 15}{10} = \frac{210}{10} = 21\text{ m}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(21\text{ m}\)."),

    (12, r"A water tap fills a \(120\text{ L}\) tank in 8 minutes. How long does it take to fill a \(300\text{ L}\) tank at the same flow rate?",
     [r"\(20\text{ minutes}\)", r"\(18\text{ minutes}\)", r"\(24\text{ minutes}\)", r"\(15\text{ minutes}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nFlow rate \(= \frac{120}{8} = 15\text{ L/min}\).\nTime \(= \frac{300}{15} = 20\text{ minutes}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(20\text{ minutes}\)."),

    (13, r"If \(₹1500\) yields an interest of \(₹90\) in one year, what interest will \(₹4500\) yield at the same rate in one year?",
     [r"\(₹270\)", r"\(₹250\)", r"\(₹300\)", r"\(₹180\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nInterest is directly proportional to Principal: \(\frac{90}{1500} \times 4500 = 90 \times 3 = ₹270\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹270\)."),

    (14, r"The cost of 5 dozen bananas is \(₹300\). What is the cost of 8 dozen bananas?",
     [r"\(₹480\)", r"\(₹450\)", r"\(₹400\)", r"\(₹500\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nCost per dozen \(= \frac{300}{5} = ₹60\).\nCost of 8 dozen \(= 8 \times 60 = ₹480\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹480\)."),

    (15, r"A recipe for 4 servings needs \(250\text{ g}\) of pasta. How much pasta is required for 10 servings?",
     [r"\(625\text{ g}\)", r"\(500\text{ g}\)", r"\(600\text{ g}\)", r"\(750\text{ g}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nPasta per serving \(= \frac{250}{4} = 62.5\text{ g}\).\nFor 10 servings \(= 10 \times 62.5 = 625\text{ g}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(625\text{ g}\)."),

    (16, r"A car uses 18 litres of fuel for \(216\text{ km}\). How much fuel is required to travel \(360\text{ km}\)?",
     [r"\(30\text{ litres}\)", r"\(25\text{ litres}\)", r"\(32\text{ litres}\)", r"\(28\text{ litres}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nFuel needed \(= \frac{18}{216} \times 360 = \frac{1}{12} \times 360 = 30\text{ litres}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(30\text{ litres}\)."),

    (17, r"If 9 sheets of paper weigh \(36\text{ grams}\), how many sheets of the same paper will weigh \(1\text{ kilogram}\)?",
     [r"\(250\)", r"\(200\)", r"\(300\)", r"\(225\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\n\(1\text{ kg} = 1000\text{ g}\).\nWeight per sheet \(= \frac{36}{9} = 4\text{ g}\).\nNumber of sheets \(= \frac{1000}{4} = 250\).\n\n### 2. Option Analysis:\n- Option A is correct: 250."),

    (18, r"A wheel rotates 240 times in 2 minutes. How many times will it rotate in 7 minutes at constant angular speed?",
     [r"\(840\)", r"\(720\)", r"\(960\)", r"\(800\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nRotations per minute \(= \frac{240}{2} = 120\text{ rpm}\).\nRotations in 7 min \(= 120 \times 7 = 840\).\n\n### 2. Option Analysis:\n- Option A is correct: 840."),

    (19, r"If the annual premium for a medical insurance of \(₹500{,}000\) is \(₹12{,}500\), what would be the premium for an insurance cover of \(₹800{,}000\) at the same proportionate rate?",
     [r"\(₹20{,}000\)", r"\(₹18{,}000\)", r"\(₹22{,}500\)", r"\(₹16{,}000\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nPremium \(= \frac{12{,}500}{500{,}000} \times 800{,}000 = 0.025 \times 800{,}000 = ₹20{,}000\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹20{,}000\)."),

    (20, r"In Lilavati, Bhaskara poses: 'If two and a half palas of saffron are purchased for three-sevenths of a nishka, how many palas will be obtained for nine nishkas?' This problem is an application of which method?",
     [r"Trairasika (Rule of Three)", r"Kuttaka (Pulverizer)", r"Bijaganita", r"Virasika"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nThis is the classic example of Trairasika (Rule of Three) given by Bhaskaracharya in Lilavati Chapter 5.\n\n### 2. Option Analysis:\n- Option A is correct: Trairasika.")
]

for seq, text, opts, ans, qtype, diff, exp in sub1_exam:
    questions.append(make_q(seq, SUB1_CODE, SUB1_NAME, text, opts, ans, qtype, diff, "exam", "standard", exp))

# --- SUBTOPIC 7.4.2: Direct Proportion Word Problems (021 - 040) ---
sub2_exam = [
    (21, r"A train travels \(75\text{ km}\) in 45 minutes at uniform speed. How long will it take to travel \(250\text{ km}\)?",
     [r"\(2\text{ hours } 30\text{ minutes}\)", r"\(2\text{ hours } 15\text{ minutes}\)", r"\(3\text{ hours}\)", r"\(2\text{ hours } 45\text{ minutes}\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nSpeed \(= \frac{75}{45/60} = 100\text{ km/h}\).\nTime for \(250\text{ km} = \frac{250}{100} = 2.5\text{ hours} = 2\text{ h } 30\text{ min}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(2\text{ h } 30\text{ min}\)."),

    (22, r"If 15 envelops cost \(₹37.50\), how many such envelops can be bought for \(₹100\)?",
     [r"\(40\)", r"\(35\)", r"\(45\)", r"\(50\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nCost per envelope \(= \frac{37.50}{15} = ₹2.50\).\nEnvelopes for \(₹100 = \frac{100}{2.50} = 40\).\n\n### 2. Option Analysis:\n- Option A is correct: 40."),

    (23, r"A loaded truck travels \(14\text{ km}\) in 25 minutes. If the speed remains constant, how far can it travel in 5 hours?",
     [r"\(168\text{ km}\)", r"\(140\text{ km}\)", r"\(150\text{ km}\)", r"\(175\text{ km}\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\n5 hours \(= 300\text{ minutes}\).\nDistance \(= \frac{14}{25} \times 300 = 14 \times 12 = 168\text{ km}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(168\text{ km}\)."),

    (24, r"If the cost of 7 meters of cloth is \(₹1470\), find the cost of 5 meters of cloth.",
     [r"\(₹1050\)", r"\(₹1100\)", r"\(₹980\)", r"\(₹1200\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nCost per meter \(= \frac{1470}{7} = ₹210\).\nCost of 5 meters \(= 5 \times 210 = ₹1050\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹1050\)."),

    (25, r"A typist types 540 words in 12 minutes. How many words will the typist type in 35 minutes at the same pace?",
     [r"\(1575\)", r"\(1500\)", r"\(1620\)", r"\(1440\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nWords per minute \(= \frac{540}{12} = 45\).\nIn 35 minutes \(= 35 \times 45 = 1575\text{ words}\).\n\n### 2. Option Analysis:\n- Option A is correct: 1575."),

    (26, r"The weight of 65 tea packets of equal size is \(26\text{ kg}\). How many packets will weigh \(12\text{ kg}\)?",
     [r"\(30\)", r"\(25\)", r"\(35\)", r"\(28\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nWeight per packet \(= \frac{26}{65} = \frac{2}{5} = 0.4\text{ kg}\).\nNumber of packets \(= \frac{12}{0.4} = 30\).\n\n### 2. Option Analysis:\n- Option A is correct: 30."),

    (27, r"If 12 men earn \(₹3600\) in one day, how much will 20 men earn in one day at the same daily wage?",
     [r"\(₹6000\)", r"\(₹5400\)", r"\(₹6500\)", r"\(₹5000\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nDaily wage per man \(= \frac{3600}{12} = ₹300\).\nEarnings of 20 men \(= 20 \times 300 = ₹6000\).\n\n### 2. Option Analysis:\n- Option A is correct: \(₹6000\)."),

    (28, r"A machine in a soft drink factory fills 840 bottles in 6 hours. How many bottles will it fill in 5 hours?",
     [r"\(700\)", r"\(720\)", r"\(680\)", r"\(750\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\nBottles per hour \(= \frac{840}{6} = 140\).\nIn 5 hours \(= 140 \times 5 = 700\text{ bottles}\).\n\n### 2. Option Analysis:\n- Option A is correct: 700."),

    (29, r"If a shadow of a \(5\text{ m } 60\text{ cm}\) high vertical pole is \(3\text{ m } 20\text{ cm}\) long, what is the length of the shadow cast by another pole \(10\text{ m } 50\text{ cm}\) high at the same time?",
     [r"\(6\text{ m}\)", r"\(5\text{ m } 50\text{ cm}\)", r"\(6\text{ m } 40\text{ cm}\)", r"\(7\text{ m}\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nConvert to cm: Pole 1 \(= 560\text{ cm}\), Shadow 1 \(= 320\text{ cm}\).\nPole 2 \(= 1050\text{ cm}\).\n\(\frac{560}{320} = \frac{1050}{S} \implies S = \frac{320 \times 1050}{560} = \frac{4 \times 1050}{7} = 4 \times 150 = 600\text{ cm} = 6\text{ m}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(6\text{ m}\)."),

    (30, r"An electric pole \(14\text{ m}\) high casts a shadow of \(10\text{ m}\). Find the height of a tree that casts a shadow of \(15\text{ m}\) under similar conditions.",
     [r"\(21\text{ m}\)", r"\(20\text{ m}\)", r"\(18\text{ m}\)", r"\(22.5\text{ m}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(\frac{14}{10} = \frac{H}{15} \implies H = \frac{14 \times 15}{10} = 21\text{ m}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(21\text{ m}\)."),

    (31, r"A photograph of a bacteria enlarged 50,000 times attains a length of \(5\text{ cm}\). What is the actual length of the bacteria?",
     [r"\(10^{-4}\text{ cm}\)", r"\(10^{-3}\text{ cm}\)", r"\(10^{-5}\text{ cm}\)", r"\(5 \times 10^{-4}\text{ cm}\)"], "A", "OSC", "medium",
     r"### 1. Mathematical Concept & Principle:\nActual length \(= \frac{5\text{ cm}}{50{,}000} = \frac{1}{10{,}000}\text{ cm} = 10^{-4}\text{ cm}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(10^{-4}\text{ cm}\)."),

    (32, r"If the thickness of a pile of 16 cardboard sheets is \(44\text{ mm}\), how many sheets of the same cardboard will be in a pile of thickness \(71.5\text{ cm}\)?",
     [r"\(260\)", r"\(240\)", r"\(250\)", r"\(280\)"], "A", "OSC", "hard",
     r"### 1. Mathematical Concept & Principle:\nThickness of 1 sheet \(= \frac{44}{16} = 2.75\text{ mm}\).\nTotal thickness \(= 71.5\text{ cm} = 715\text{ mm}\).\nNumber of sheets \(= \frac{715}{2.75} = 260\).\n\n### 2. Option Analysis:\n- Option A is correct: 260."),

    (33, r"A car is traveling at an average speed of \(60\text{ km/h}\). How much distance will it cover in 20 minutes?",
     [r"\(20\text{ km}\)", r"\(15\text{ km}\)", r"\(18\text{ km}\)", r"\(30\text{ km}\)"], "A", "OSC", "easy",
     r"### 1. Mathematical Concept & Principle:\n\(20\text{ minutes} = \frac{20}{60} = \frac{1}{3}\text{ hour}\).\nDistance \(= 60 \times \frac{1}{3} = 20\text{ km}\).\n\n### 2. Option Analysis:\n- Option A is correct: \(20\text{ km}\)."),

    # 34: OAR
    (34, r"Assertion (A): As the number of articles purchased increases, the total cost increases proportionately at a fixed unit price.\nReason (R): Two quantities \(x\) and \(y\) are in direct proportion if the ratio \(\frac{x}{y}\) remains constant.",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"], "A", "OAR", "easy",
     r"### 1. Mathematical Concept & Principle:\nTotal Cost \(= \text{Unit Price} \times \text{Quantity}\). The ratio \(\frac{\text{Cost}}{\text{Quantity}} = \text{Unit Price} = \text{Constant}\). Hence Assertion and Reason are true, and (R) explains (A).\n\n### 2. Option Analysis:\n- Option A is correct."),

    # 35: OAR
    (35, r"Assertion (A): If the speed of a vehicle is doubled, the time taken to cover a fixed distance is also doubled.\nReason (R): Speed and time taken for a fixed distance vary inversely, not directly.",
     ["(A) is false but (R) is true",
      "Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false"], "A", "OAR", "easy",
     r"### 1. Mathematical Concept & Principle:\nWhen speed is doubled for a fixed distance, time is halved (\(\text{Time} = \frac{\text{Distance}}{\text{Speed}}\)). Thus (A) is false and (R) correctly explains that speed and time are inversely proportional.\n\n### 2. Option Analysis:\n- Option A is correct."),

    # 36: OTF
    (36, r"True or False: If two quantities \(x\) and \(y\) vary directly, then when \(x\) increases, \(y\) also increases in such a manner that their ratio \(\frac{x}{y} = k\) remains constant.",
     ["True", "False"], "A", "OTF", "easy",
     r"This is the strict mathematical definition of direct variation. True."),

    (37, r"True or False: The age of a person and their height throughout their entire life are in direct proportion.",
     ["False", "True"], "A", "OTF", "easy",
     r"Height increases during childhood but stops growing in adulthood. Therefore, height and age do NOT form a direct proportion throughout life. False."),

    # 38: OFB
    (38, r"If 12 pens cost \(₹180\), then 20 pens will cost ₹ _____.",
     [r"\(300\)", r"\(280\)", r"\(240\)", r"\(320\)"], "A", "OFB", "easy",
     r"Cost per pen \(= \frac{180}{12} = ₹15\). For 20 pens \(= 20 \times 15 = ₹300\)."),

    # 39: OFB
    (39, r"A car travels \(90\text{ km}\) in \(1.5\text{ hours}\). At the same speed, it will cover _____ km in 4 hours.",
     [r"\(240\)", r"\(200\)", r"\(360\)", r"\(270\)"], "A", "OFB", "easy",
     r"Speed \(= \frac{90}{1.5} = 60\text{ km/h}\). In 4 hours \(= 60 \times 4 = 240\text{ km}\)."),

    # 40: ONE
    (40, r"If 15 workers complete a job earning \(₹18{,}000\) collectively, how much will 8 workers earn collectively at the same individual rate? (in ₹)",
     [r"\(9600\)", r"\(9000\)", r"\(10000\)", r"\(8800\)"], "A", "ONE", "easy",
     r"Earnings per worker \(= \frac{18{,}000}{15} = ₹1200\). For 8 workers \(= 8 \times 1200 = ₹9600\).")
]

for seq, text, opts, ans, qtype, diff, exp in sub2_exam:
    questions.append(make_q(seq, SUB2_CODE, SUB2_NAME, text, opts, ans, qtype, diff, "exam", "standard", exp))

# =========================================================================
# PRACTICE VAULT: Questions 041 - 070 (15 for 7.4.1, 15 for 7.4.2)
# =========================================================================

sub1_practice = [
    (41, r"Using Trairasika: If 6 palas of sandalwood oil cost 4 dharanas, how many dharanas will 15 palas of the same oil cost?",
     [r"\(10\)", r"\(12\)", r"\(8\)", r"\(15\)"], "A", "OSC", "medium",
     r"\(\text{Icchaphala} = \frac{4 \times 15}{6} = \frac{60}{6} = 10\text{ dharanas}\)."),

    (42, r"If 7 meters of wire costs \(₹56\), how much will 21 meters of the same wire cost?",
     [r"\(₹168\)", r"\(₹144\)", r"\(₹156\)", r"\(₹180\)"], "A", "OSC", "easy",
     r"Cost \(= \frac{56}{7} \times 21 = 8 \times 21 = ₹168\)."),

    (43, r"A baker uses \(450\text{ g}\) of sugar to bake 3 cakes. How much sugar is needed for 8 such cakes?",
     [r"\(1200\text{ g}\)", r"\(1000\text{ g}\)", r"\(1500\text{ g}\)", r"\(1350\text{ g}\)"], "A", "OSC", "easy",
     r"Sugar per cake \(= 150\text{ g}\). For 8 cakes \(= 8 \times 150 = 1200\text{ g}\)."),

    (44, r"If a sprinkler waters \(40\text{ m}^2\) of lawn in 12 minutes, how many square meters will it water in 45 minutes?",
     [r"\(150\text{ m}^2\)", r"\(120\text{ m}^2\)", r"\(160\text{ m}^2\)", r"\(180\text{ m}^2\)"], "A", "OSC", "easy",
     r"Rate \(= \frac{40}{12} = \frac{10}{3}\text{ m}^2/\text{min}\). Area in 45 min \(= 45 \times \frac{10}{3} = 150\text{ m}^2\)."),

    (45, r"A printer prints 36 pages in 3 minutes. How many pages can it print in 25 minutes?",
     [r"\(300\)", r"\(250\)", r"\(280\)", r"\(320\)"], "A", "OSC", "easy",
     r"Speed \(= 12\text{ pages/min}\). In 25 min \(= 25 \times 12 = 300\text{ pages}\)."),

    (46, r"If 18 textbooks cost \(₹3240\), what is the cost of 25 such textbooks?",
     [r"\(₹4500\)", r"\(₹4200\)", r"\(₹4800\)", r"\(₹4000\)"], "A", "OSC", "easy",
     r"Cost per book \(= \frac{3240}{18} = ₹180\). For 25 books \(= 25 \times 180 = ₹4500\)."),

    (47, r"If 5 truckloads contain 45 tonnes of gravel, how many tonnes will 12 truckloads contain?",
     [r"\(108\text{ tonnes}\)", r"\(100\text{ tonnes}\)", r"\(120\text{ tonnes}\)", r"\(96\text{ tonnes}\)"], "A", "OSC", "easy",
     r"Tonnage per truck \(= 9\text{ tonnes}\). For 12 trucks \(= 12 \times 9 = 108\text{ tonnes}\)."),

    (48, r"A tree \(12\text{ m}\) high casts a shadow of \(8\text{ m}\). What shadow length will a \(21\text{ m}\) building cast at the same time?",
     [r"\(14\text{ m}\)", r"\(16\text{ m}\)", r"\(12\text{ m}\)", r"\(15\text{ m}\)"], "A", "OSC", "easy",
     r"\(\frac{12}{8} = \frac{21}{S} \implies S = \frac{21 \times 8}{12} = 14\text{ m}\)."),

    (49, r"If \(8\text{ kg}\) of apples cost \(₹640\), how many kilograms of apples can be bought for \(₹1200\)?",
     [r"\(15\text{ kg}\)", r"\(12\text{ kg}\)", r"\(16\text{ kg}\)", r"\(18\text{ kg}\)"], "A", "OSC", "easy",
     r"Cost per kg \(= ₹80\). Weight \(= \frac{1200}{80} = 15\text{ kg}\)."),

    (50, r"A factory produces 720 toys in 6 hours. How many toys will it produce in an 8-hour shift?",
     [r"\(960\)", r"\(840\)", r"\(900\)", r"\(1000\)"], "A", "OSC", "easy",
     r"Rate \(= 120\text{ toys/h}\). In 8 hours \(= 8 \times 120 = 960\text{ toys}\)."),

    (51, r"In Trairasika, which three terms must be provided to determine the unknown fourth term?",
     [r"Pramana (measure), Phala (fruit), and Iccha (requisition)",
      r"Kala, Desa, and Dravya",
      r"Rupa, Vyavahara, and Samya",
      r"Anu, Parama, and Guru"], "A", "OSC", "medium",
     r"Classical Sanskrit terminology defines Pramana, Phala, and Iccha as the three prerequisite terms."),

    (52, r"A uniform iron bar of length \(15\text{ m}\) weighs \(45\text{ kg}\). What is the weight of a \(22\text{ m}\) long bar of the same cross-section?",
     [r"\(66\text{ kg}\)", r"\(60\text{ kg}\)", r"\(70\text{ kg}\)", r"\(65\text{ kg}\)"], "A", "OSC", "easy",
     r"Weight per meter \(= \frac{45}{15} = 3\text{ kg/m}\). Weight \(= 22 \times 3 = 66\text{ kg}\)."),

    (53, r"If 9 workers lay \(135\text{ m}\) of drainage pipe in one day, how many workers are needed to lay \(270\text{ m}\) of pipe in one day?",
     [r"\(18\)", r"\(15\)", r"\(20\)", r"\(24\)"], "A", "OSC", "easy",
     r"Output per worker \(= 15\text{ m}\). Workers required \(= \frac{270}{15} = 18\)."),

    (54, r"True or False: In direct proportion, the constant of proportionality \(k = \frac{y}{x}\) represents the unit rate of the dependent quantity.",
     ["True", "False"], "A", "OTF", "easy",
     r"\(k = \frac{y}{x}\) is the slope or unit rate in direct variation \(y = kx\). True."),

    (55, r"If 4 meters of curtain fabric costs \(₹360\), then 9 meters will cost ₹ _____.",
     [r"\(810\)", r"\(720\)", r"\(800\)", r"\(900\)"], "A", "OFB", "easy",
     r"Cost per meter \(= ₹90\). For 9 meters \(= 9 \times 90 = ₹810\).")
]

for seq, text, opts, ans, qtype, diff, exp in sub1_practice:
    questions.append(make_q(seq, SUB1_CODE, SUB1_NAME, text, opts, ans, qtype, diff, "practice", "standard", exp))

# --- 7.4.2 Practice (056 - 070) ---
sub2_practice = [
    (56, r"A cyclist rides \(42\text{ km}\) in 3 hours at constant speed. How long will it take to ride \(70\text{ km}\)?",
     [r"\(5\text{ hours}\)", r"\(4.5\text{ hours}\)", r"\(6\text{ hours}\)", r"\(4\text{ hours}\)"], "A", "OSC", "easy",
     r"Speed \(= \frac{42}{3} = 14\text{ km/h}\). Time \(= \frac{70}{14} = 5\text{ hours}\)."),

    (57, r"If 14 kg of pulses cost \(₹1260\), how much will 22 kg of the same pulses cost?",
     [r"\(₹1980\)", r"\(₹1850\)", r"\(₹2000\)", r"\(₹1920\)"], "A", "OSC", "easy",
     r"Cost per kg \(= \frac{1260}{14} = ₹90\). For 22 kg \(= 22 \times 90 = ₹1980\)."),

    (58, r"A car consumes 12 litres of petrol in traveling \(180\text{ km}\). How many litres of petrol are needed for a journey of \(450\text{ km}\)?",
     [r"\(30\text{ L}\)", r"\(25\text{ L}\)", r"\(35\text{ L}\)", r"\(28\text{ L}\)"], "A", "OSC", "easy",
     r"Mileage \(= \frac{180}{12} = 15\text{ km/L}\). Petrol needed \(= \frac{450}{15} = 30\text{ litres}\)."),

    (59, r"If 25 metres of uniform copper cable weighs \(17.5\text{ kg}\), what is the weight of \(40\text{ metres}\) of the same cable?",
     [r"\(28\text{ kg}\)", r"\(25\text{ kg}\)", r"\(30\text{ kg}\)", r"\(32\text{ kg}\)"], "A", "OSC", "easy",
     r"Weight per meter \(= \frac{17.5}{25} = 0.7\text{ kg/m}\). For 40 m \(= 40 \times 0.7 = 28\text{ kg}\)."),

    (60, r"An airplane flies \(1500\text{ km}\) in 2 hours. How far will it fly in 3 hours and 30 minutes at the same cruising speed?",
     [r"\(2625\text{ km}\)", r"\(2500\text{ km}\)", r"\(2750\text{ km}\)", r"\(2400\text{ km}\)"], "A", "OSC", "easy",
     r"Speed \(= 750\text{ km/h}\). In 3.5 hours \(= 750 \times 3.5 = 2625\text{ km}\)."),

    (61, r"A photocopy shop charges \(₹18\) for 12 pages. How much will it charge for 75 pages?",
     [r"\(₹112.50\)", r"\(₹110.00\)", r"\(₹115.00\)", r"\(₹120.00\)"], "A", "OSC", "easy",
     r"Cost per page \(= \frac{18}{12} = ₹1.50\). For 75 pages \(= 75 \times 1.50 = ₹112.50\)."),

    (62, r"If 16 men can consume a sack of grain in 30 days, does grain consumption per day vary directly with the number of men?",
     [r"Yes, daily grain consumption is directly proportional to the number of men",
      r"No, it varies inversely",
      r"No, consumption is constant",
      r"Cannot be evaluated"], "A", "OSC", "medium",
     r"Total grain eaten per day \(= \text{men} \times \text{consumption per man}\). Daily consumption is directly proportional to number of men."),

    (63, r"If 8 workers assemble 48 circuit boards in one hour, how many circuit boards will 20 workers assemble in one hour at the same rate?",
     [r"\(120\)", r"\(100\)", r"\(140\)", r"\(110\)"], "A", "OSC", "easy",
     r"Boards per worker \(= \frac{48}{8} = 6\). For 20 workers \(= 20 \times 6 = 120\)."),

    (64, r"A rainfall gauge records \(12\text{ mm}\) of rain in 4 hours. How much rainfall will be recorded in 14 hours at the same constant rate?",
     [r"\(42\text{ mm}\)", r"\(36\text{ mm}\)", r"\(48\text{ mm}\)", r"\(40\text{ mm}\)"], "A", "OSC", "easy",
     r"Rainfall rate \(= 3\text{ mm/h}\). In 14 hours \(= 14 \times 3 = 42\text{ mm}\)."),

    (65, r"A recipe for 6 people calls for \(450\text{ g}\) of flour. How many people can be served with \(1.2\text{ kg}\) of flour?",
     [r"\(16\)", r"\(15\)", r"\(18\)", r"\(14\)"], "A", "OSC", "medium",
     r"\(1.2\text{ kg} = 1200\text{ g}\). Flour per person \(= \frac{450}{6} = 75\text{ g}\). People served \(= \frac{1200}{75} = 16\)."),

    (66, r"True or False: If \(y\) is directly proportional to \(x\) and \(y = 12\) when \(x = 4\), then \(y = 27\) when \(x = 9\).",
     ["True", "False"], "A", "OTF", "easy",
     r"\(k = \frac{12}{4} = 3\). When \(x = 9\), \(y = 3 \times 9 = 27\). True."),

    (67, r"True or False: The number of days taken to complete a fixed task is directly proportional to the number of workers employed.",
     ["False", "True"], "A", "OTF", "easy",
     r"More workers take FEWER days for a fixed task. This is inverse variation, not direct. False."),

    (68, r"If 15 notebooks cost \(₹300\), then 28 notebooks will cost ₹ _____.",
     [r"\(560\)", r"\(520\)", r"\(600\)", r"\(540\)"], "A", "OFB", "easy",
     r"Cost per notebook \(= ₹20\). For 28 notebooks \(= 28 \times 20 = ₹560\)."),

    (69, r"A runner covers \(400\text{ m}\) in 50 seconds. At this rate, the time taken to run \(1\text{ km}\) is _____ seconds.",
     [r"\(125\)", r"\(120\)", r"\(150\)", r"\(100\)"], "A", "OFB", "easy",
     r"Speed \(= 8\text{ m/s}\). Time for \(1000\text{ m} = \frac{1000}{8} = 125\text{ s}\)."),

    (70, r"If 6 workers build \(18\text{ m}\) of road per day, calculate the number of meters of road built by 15 workers in one day.",
     [r"\(45\)", r"\(40\)", r"\(50\)", r"\(36\)"], "A", "ONE", "easy",
     r"Output per worker \(= 3\text{ m}\). Output for 15 workers \(= 15 \times 3 = 45\text{ m}\).")
]

for seq, text, opts, ans, qtype, diff, exp in sub2_practice:
    questions.append(make_q(seq, SUB2_CODE, SUB2_NAME, text, opts, ans, qtype, diff, "practice", "standard", exp))

# =========================================================================
# FOUNDATION VAULT: Questions 071 - 082 (Challenging / Olympiad)
# =========================================================================

foundation_q = [
    (71, SUB1_CODE, SUB1_NAME,
     r"Bhaskaracharya's Lilavati problem: If 2 palas of fine camphor are bought for \(\frac{3}{5}\) of a gold coin, how many palas can be bought for 12 gold coins?",
     [r"\(40\text{ palas}\)", r"\(36\text{ palas}\)", r"\(45\text{ palas}\)", r"\(30\text{ palas}\)"], "A", "OSC", "hard",
     r"### 1. Mathematical Concept & Principle:\nTrairasika: \(\text{Icchaphala} = \frac{\text{Phala} \times \text{Iccha}}{\text{Pramana}}\).\n\n### 2. Step-by-Step Calculation:\nHere, Pramana \(= \frac{3}{5}\) coin, Phala \(= 2\) palas, Iccha \(= 12\) coins.\n\(\text{Palas} = \frac{2 \times 12}{3/5} = \frac{24 \times 5}{3} = 40\text{ palas}\).\n\n### 3. Option Analysis:\n- Option A is correct: \(40\text{ palas}\)."),

    (72, SUB1_CODE, SUB1_NAME,
     r"In a classical Compound Rule of Five (Pancharasika), 8 bullocks plough 24 bighas of land in 9 days. How many bighas of land will 10 bullocks plough in 18 days?",
     [r"\(60\text{ bighas}\)", r"\(54\text{ bighas}\)", r"\(48\text{ bighas}\)", r"\(72\text{ bighas}\)"], "A", "OSC", "hard",
     r"Work done is directly proportional to Bullocks and Days: \(\text{Work} = k \times B \times D\).\n\(24 = k \times 8 \times 9 = 72k \implies k = \frac{1}{3}\).\nNew work \(= \frac{1}{3} \times 10 \times 18 = 60\text{ bighas}\)."),

    (73, SUB1_CODE, SUB1_NAME,
     r"An express train leaves station A at \(60\text{ km/h}\). Two hours later, a superfast bullet train leaves station A in the same direction at \(100\text{ km/h}\). At what distance from station A will the bullet train overtake the express train?",
     [r"\(300\text{ km}\)", r"\(240\text{ km}\)", r"\(360\text{ km}\)", r"\(280\text{ km}\)"], "A", "OSC", "hard",
     r"Head start distance \(= 60 \times 2 = 120\text{ km}\).\nRelative speed \(= 100 - 60 = 40\text{ km/h}\).\nTime to overtake \(= \frac{120}{40} = 3\text{ hours}\).\nDistance from station A \(= 100 \times 3 = 300\text{ km}\)."),

    (74, SUB1_CODE, SUB1_NAME,
     r"A contractor estimates that 15 men working 8 hours a day can complete a canal excavation in 20 days. How many men working 6 hours a day would be required to complete the same excavation in 25 days?",
     [r"\(16\)", r"\(18\)", r"\(15\)", r"\(20\)" ], "A", "OSC", "hard",
     r"Total man-hours required \(= 15 \times 8 \times 20 = 2400\text{ man-hours}\).\nLet required men be \(M\): \(M \times 6 \times 25 = 150M\).\n\(150M = 2400 \implies M = 16\text{ men}\)."),

    (75, SUB1_CODE, SUB1_NAME,
     r"A pendulum clock's period \(T\) is directly proportional to the square root of its pendulum length \(L\) (\(T \propto \sqrt{L}\)). If the length is increased by \(44\%\), by what percentage does the period increase?",
     [r"\(20\%\)", r"\(22\%\)", r"\(44\%\)", r"\(12\%\)"], "A", "OSC", "hard",
     r"New length \(L' = 1.44L\).\nNew period \(T' \propto \sqrt{1.44L} = 1.2\sqrt{L} = 1.2T\).\nPercentage increase \(= (1.2 - 1) \times 100\% = 20\%\)."),

    (76, SUB1_CODE, SUB1_NAME,
     r"The illumination (brightness) received on a screen varies directly with the source candlepower \(I\) and inversely with the square of distance \(d\) (\(E \propto \frac{I}{d^2}\)). If the distance of the screen from a 100-candlepower lamp is tripled, how much must the candlepower be increased to maintain original brightness?",
     [r"Must increase to 900 candlepower", r"Must increase to 300 candlepower", r"Must increase to 600 candlepower", r"Must increase to 2700 candlepower"], "A", "OSC", "hard",
     r"Distance tripled means \(d' = 3d \implies d'^2 = 9d^2\).\nTo keep \(E = \frac{I'}{9d^2}\) equal to \(\frac{I}{d^2}\), \(I' = 9I = 9 \times 100 = 900\text{ candlepower}\)."),

    (77, SUB2_CODE, SUB2_NAME,
     r"A train traveling at uniform speed crosses a \(150\text{ m}\) platform in 18 seconds, and a \(250\text{ m}\) platform in 26 seconds. What is the length of the train?",
     [r"\(75\text{ m}\)", r"\(80\text{ m}\)", r"\(60\text{ m}\)", r"\(90\text{ m}\)"], "A", "OSC", "hard",
     r"Let train length be \(L\). Speed \(= \frac{L + 150}{18} = \frac{L + 250}{26}\).\n\(26(L + 150) = 18(L + 250) \implies 26L + 3900 = 18L + 4500\)\n\(8L = 600 \implies L = 75\text{ m}\)."),

    (78, SUB2_CODE, SUB2_NAME,
     r"If 12 cows eat as much grass as 15 sheep, how many sheep will eat as much grass as 36 cows?",
     [r"\(45\)", r"\(40\)", r"\(48\)", r"\(50\)"], "A", "OSC", "medium",
     r"Ratio of cows to sheep is \(12 : 15 = 4 : 5\).\n\(\frac{4}{5} = \frac{36}{S} \implies S = \frac{36 \times 5}{4} = 45\text{ sheep}\)."),

    (79, SUB2_CODE, SUB2_NAME,
     r"A water pipe of internal diameter \(2\text{ cm}\) discharges 20 liters of water per minute. If flow velocity is kept constant, what volume of water per minute will be discharged by a pipe of diameter \(4\text{ cm}\)?",
     [r"\(80\text{ L/min}\)", r"\(40\text{ L/min}\)", r"\(60\text{ L/min}\)", r"\(160\text{ L/min}\)"], "A", "OSC", "hard",
     r"Discharge rate is directly proportional to cross-sectional area: \(Q \propto \pi r^2 \propto d^2\).\nDiameter doubled from 2 to 4 means area quadrupled: \(2^2 = 4\).\nNew discharge \(= 20 \times 4 = 80\text{ L/min}\)."),

    (80, SUB2_CODE, SUB2_NAME,
     r"A military fort has provisions for 300 soldiers for 40 days. After 10 days, 50 soldiers leave the fort. For how many more days will the remaining provisions last?",
     [r"\(36\text{ days}\)", r"\(35\text{ days}\)", r"\(32\text{ days}\)", r"\(40\text{ days}\)"], "A", "OSC", "hard",
     r"Remaining food is enough for 300 soldiers for \(40 - 10 = 30\text{ days}\).\nRemaining soldiers \(= 300 - 50 = 250\).\n\(300 \times 30 = 250 \times D \implies D = \frac{9000}{250} = 36\text{ days}\)."),

    (81, SUB2_CODE, SUB2_NAME,
     r"A car travels the first \(120\text{ km}\) of a journey at \(40\text{ km/h}\) and the remaining \(180\text{ km}\) at \(60\text{ km/h}\). Calculate the average speed of the car for the entire journey in km/h.",
     [r"\(50\)", r"\(48\)", r"\(52\)", r"\(45\)"], "A", "ONE", "hard",
     r"Time 1 \(= \frac{120}{40} = 3\text{ h}\).\nTime 2 \(= \frac{180}{60} = 3\text{ h}\).\nTotal distance \(= 300\text{ km}\), Total time \(= 6\text{ h}\).\nAverage speed \(= \frac{300}{6} = 50\text{ km/h}\)."),

    (82, SUB2_CODE, SUB2_NAME,
     r"In a factory, 3 machines P, Q, and R together produce 1800 screws in 6 hours. Machine P produces screws twice as fast as Q, and Q produces screws twice as fast as R. How many screws does Machine P produce in 2 hours?",
     [r"\(343\)", r"\(400\)", r"\(300\)", r"\(350\)"], "A", "OSC", "hard",
     r"Let R's rate be \(r\) screws/h. Then Q is \(2r\), P is \(4r\).\nTotal rate \(= 4r + 2r + r = 7r\).\nTotal produced in 6 h: \(6 \times 7r = 42r = 1800 \implies r = \frac{1800}{42} = \frac{300}{7}\).\nP's hourly rate \(= 4 \times \frac{300}{7} = \frac{1200}{7}\).\nIn 2 hours: \(2 \times \frac{1200}{7} = \frac{2400}{7} \approx 343\). Let's use clean numbers: if total is 2100 in 6 hours: \(42r = 2100 \implies r = 50\). Then P produces \(4 \times 50 = 200\) screws/h, so in 2 h it produces 400 screws!\nLet's update problem text: 2100 screws in 6 hours, options: [400, 200, 100, 300].")
]

# Adjust 82 for exact whole numbers
foundation_q[11] = (82, SUB2_CODE, SUB2_NAME,
     r"In a factory, 3 machines P, Q, and R together produce 2100 screws in 6 hours. Machine P produces screws twice as fast as Q, and Q produces screws twice as fast as R. How many screws does Machine P produce in 2 hours?",
     [r"\(400\)", r"\(200\)", r"\(100\)", r"\(300\)"], "A", "OSC", "hard",
     r"Let R's rate be \(r\). Then \(Q = 2r\) and \(P = 4r\).\nTotal rate \(= 4r + 2r + r = 7r\).\nTotal screws in 6 hours: \(6 \times 7r = 42r = 2100 \implies r = 50\text{ screws/h}\).\nP's rate \(= 4 \times 50 = 200\text{ screws/h}\).\nIn 2 hours, P produces \(200 \times 2 = 400\text{ screws}\).")

for seq, sub_code, sub_name, text, opts, ans, qtype, diff, exp in foundation_q:
    questions.append(make_q(seq, sub_code, sub_name, text, opts, ans, qtype, diff, "foundation", "foundation", exp))

out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch7_t4.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"✅ Generated {len(questions)} questions for Topic 7.4 -> {out_path}")
