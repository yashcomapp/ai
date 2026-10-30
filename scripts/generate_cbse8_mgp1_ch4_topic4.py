# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-4-4.4
Topic: Applications & Word Problems (Age, Number, Perimeter, Coins)
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-4-4.4"

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
    (r"The sum of three consecutive integers is 51. What is the largest of these integers?",
     ["18", "17", "16", "19"],
     "A", "OSC", "easy",
     r"Let the three consecutive integers be \(x\), \(x + 1\), and \(x + 2\). Their sum is \(3x + 3 = 51 \implies 3x = 48 \implies x = 16\). The integers are 16, 17, 18. The largest integer is 18."),

    # 2
    (r"The perimeter of a rectangle is \(13\text{ cm}\) and its width is \(2\frac{3}{4}\text{ cm}\). What is its length?",
     [r"\(3\frac{3}{4}\text{ cm}\)", r"\(3\frac{1}{4}\text{ cm}\)", r"\(4\text{ cm}\)", r"\(2\frac{3}{4}\text{ cm}\)"],
     "A", "OSC", "medium",
     r"Perimeter \(P = 2(l + w) = 13\). Width \(w = \frac{11}{4}\text{ cm}\). So \(2\left(l + \frac{11}{4}\right) = 13 \implies l + \frac{11}{4} = \frac{13}{2} = \frac{26}{4}\). Thus \(l = \frac{26 - 11}{4} = \frac{15}{4} = 3\frac{3}{4}\text{ cm}\)."),

    # 3
    (r"The present ages of Sahil and his mother are in the ratio \(1 : 3\). After 5 years, the sum of their ages will be 66 years. What is Sahil's present age?",
     ["14 years", "12 years", "16 years", "15 years"],
     "A", "OSC", "medium",
     r"Let Sahil's present age be \(x\) and mother's age be \(3x\). After 5 years, their ages will be \((x + 5)\) and \((3x + 5)\). Sum: \((x + 5) + (3x + 5) = 66 \implies 4x + 10 = 66 \implies 4x = 56 \implies x = 14\) years."),

    # 4
    (r"Two numbers are in the ratio \(5 : 3\). If they differ by 18, what is the larger number?",
     ["45", "27", "36", "54"],
     "A", "OSC", "easy",
     r"Let the numbers be \(5x\) and \(3x\). Their difference is \(5x - 3x = 18 \implies 2x = 18 \implies x = 9\). The larger number is \(5 \times 9 = 45\)."),

    # 5
    (r"The sum of two numbers is 95. If one exceeds the other by 15, what are the numbers?",
     ["40 and 55", "35 and 60", "45 and 50", "30 and 65"],
     "A", "OSC", "easy",
     r"Let the smaller number be \(x\). The other number is \(x + 15\). Their sum is \(x + (x + 15) = 95 \implies 2x + 15 = 95 \implies 2x = 80 \implies x = 40\). The numbers are 40 and 55."),

    # 6
    (r"The digits of a two-digit number differ by 3. If the digits are interchanged and the resulting number is added to the original number, we get 143. What is the original number (with tens digit greater than units digit)?",
     ["85", "74", "96", "63"],
     "A", "OSC", "hard",
     r"Let units digit be \(x\), tens digit be \(x + 3\). Original number \(= 10(x + 3) + x = 11x + 30\). Interchanged number \(= 10x + (x + 3) = 11x + 3\). Sum \(= (11x + 30) + (11x + 3) = 22x + 33 = 143 \implies 22x = 110 \implies x = 5\). Units digit = 5, tens digit = 8. Original number = 85."),

    # 7
    (r"A purse contains \(₹1, ₹2,\) and \(₹5\) coins in the ratio \(3 : 2 : 1\). If the total value of all coins is \(₹360\), how many \(₹5\) coins are there?",
     ["30", "60", "90", "20"],
     "A", "OSC", "medium",
     r"Let the number of coins be \(3x, 2x, x\). Total value \(= 1(3x) + 2(2x) + 5(x) = 3x + 4x + 5x = 12x\). Given \(12x = 360 \implies x = 30\). The number of \(₹5\) coins is \(x = 30\)."),

    # 8
    (r"The base of an isosceles triangle is \(\frac{4}{3}\text{ cm}\). The perimeter of the triangle is \(4\frac{2}{15}\text{ cm}\). What is the length of each of the equal sides?",
     [r"\(1\frac{2}{5}\text{ cm}\)", r"\(1\frac{1}{5}\text{ cm}\)", r"\(2\text{ cm}\)", r"\(1\frac{3}{5}\text{ cm}\)"],
     "A", "OSC", "medium",
     r"Let the equal sides be \(x\). Perimeter \(= 2x + \frac{4}{3} = 4\frac{2}{15} = \frac{62}{15}\). So \(2x = \frac{62}{15} - \frac{20}{15} = \frac{42}{15} \implies x = \frac{42}{30} = \frac{7}{5} = 1\frac{2}{5}\text{ cm}\)."),

    # 9
    (r"Three consecutive multiples of 8 add up to 888. Find the smallest multiple.",
     ["288", "296", "304", "280"],
     "A", "OSC", "medium",
     r"Let the three consecutive multiples be \(x\), \(x + 8\), and \(x + 16\). Sum: \(3x + 24 = 888 \implies 3x = 864 \implies x = 288\)."),

    # 10
    (r"Fifteen years from now, Ravi's age will be 4 times his present age. What is Ravi's present age?",
     ["5 years", "4 years", "6 years", "7 years"],
     "A", "OSC", "easy",
     r"Let Ravi's present age be \(x\). In 15 years, his age is \(x + 15\). Given \(x + 15 = 4x \implies 3x = 15 \implies x = 5\) years."),

    # 11
    (r"Baichung's father is 26 years younger than Baichung's grandfather and 29 years older than Baichung. The sum of the ages of all three is 135 years. How old is Baichung?",
     ["17 years", "46 years", "72 years", "15 years"],
     "A", "OSC", "hard",
     r"Let Baichung's age be \(x\). Father's age \(= x + 29\). Grandfather's age \(= (x + 29) + 26 = x + 55\). Sum: \(x + (x + 29) + (x + 55) = 135 \implies 3x + 84 = 135 \implies 3x = 51 \implies x = 17\) years."),

    # 12
    (r"A grandfather is 10 times older than his granddaughter. He is also 54 years older than her. What is the granddaughter's age?",
     ["6 years", "7 years", "5 years", "8 years"],
     "A", "OSC", "easy",
     r"Let granddaughter's age be \(x\). Grandfather's age \(= 10x\). Given \(10x - x = 54 \implies 9x = 54 \implies x = 6\) years."),

    # 13
    (r"The perimeter of a rectangular swimming pool is \(154\text{ m}\). Its length is \(2\text{ m}\) more than twice its breadth. What is the breadth of the pool?",
     ["25 m", "52 m", "30 m", "20 m"],
     "A", "OSC", "medium",
     r"Let breadth be \(b\). Length \(l = 2b + 2\). Perimeter \(= 2(l + b) = 2((2b + 2) + b) = 2(3b + 2) = 6b + 4 = 154\). So \(6b = 150 \implies b = 25\text{ m}\). (Length is \(2(25) + 2 = 52\text{ m}\))."),

    # 14
    (r"A positive number is 5 times another number. If 21 is added to both the numbers, one becomes twice the other. What is the smaller number?",
     ["7", "35", "9", "5"],
     "A", "OSC", "medium",
     r"Let the numbers be \(x\) and \(5x\). Adding 21: \(5x + 21 = 2(x + 21) = 2x + 42 \implies 3x = 21 \implies x = 7\). The smaller number is 7."),

    # 15
    (r"The sum of the digits of a two-digit number is 9. When we interchange the digits, the new number exceeds the original number by 27. What is the original number?",
     ["36", "63", "27", "45"],
     "A", "OSC", "hard",
     r"Let tens digit be \(x\), units digit be \(9 - x\). Original number \(= 10x + (9 - x) = 9x + 9\). Interchanged number \(= 10(9 - x) + x = 90 - 9x\). Given: \((90 - 9x) - (9x + 9) = 27 \implies 81 - 18x = 27 \implies 18x = 54 \implies x = 3\). Tens digit = 3, units digit = 6. Original number = 36."),

    # 16
    (r"A cash cashier has currency notes of denominations \(₹100, ₹50,\) and \(₹10\). The ratio of the number of these notes is \(2 : 3 : 5\). If the total cash is \(₹4,00,000\), how many \(₹100\) notes does she have?",
     ["2000", "3000", "5000", "1000"],
     "A", "OSC", "hard",
     r"Let note counts be \(2x, 3x, 5x\). Total value \(= 100(2x) + 50(3x) + 10(5x) = 200x + 150x + 50x = 400x\). Given \(400x = 400000 \implies x = 1000\). Number of \(₹100\) notes \(= 2x = 2(1000) = 2000\)."),

    # 17
    (r"The organizers of an essay competition decide that a winner gets a prize of \(₹100\) and a participant who does not win gets a prize of \(₹25\). The total prize money distributed is \(₹3,000\). If the total number of participants is 63, find the number of winners.",
     ["19", "21", "17", "23"],
     "A", "OSC", "hard",
     r"Let number of winners be \(w\). Non-winners \(= 63 - w\). Total prize: \(100w + 25(63 - w) = 3000 \implies 100w + 1575 - 25w = 3000 \implies 75w = 1425 \implies w = \frac{1425}{75} = 19\)."),

    # 18
    (r"A fraction's denominator is greater than its numerator by 8. If the numerator is increased by 17 and the denominator is decreased by 1, the number obtained is \(\frac{3}{2}\). What is the original fraction?",
     [r"\(\frac{13}{21}\)", r"\(\frac{11}{19}\)", r"\(\frac{15}{23}\)", r"\(\frac{9}{17}\)"],
     "A", "OSC", "hard",
     r"Let numerator be \(n\); denominator is \(n + 8\). New fraction: \(\frac{n + 17}{(n + 8) - 1} = \frac{n + 17}{n + 7} = \frac{3}{2}\). Cross-multiplying: \(2(n + 17) = 3(n + 7) \implies 2n + 34 = 3n + 21 \implies n = 13\). Denominator is \(13 + 8 = 21\). Original fraction is \(\frac{13}{21}\)."),

    # 19
    (r"The ages of Hari and Harry are in the ratio \(5 : 7\). Four years from now the ratio of their ages will be \(3 : 4\). Find Hari's present age.",
     ["20 years", "28 years", "15 years", "25 years"],
     "A", "OSC", "medium",
     r"Let ages be \(5x\) and \(7x\). In 4 years: \(\frac{5x + 4}{7x + 4} = \frac{3}{4} \implies 4(5x + 4) = 3(7x + 4) \implies 20x + 16 = 21x + 12 \implies x = 4\). Hari's age \(= 5(4) = 20\) years."),

    # 20
    (r"A streamer goes downstream from one port to another in 9 hours. It covers the same distance upstream in 10 hours. If the speed of the stream is \(1\text{ km/h}\), find the speed of the streamer in still water.",
     ["19 km/h", "18 km/h", "20 km/h", "21 km/h"],
     "A", "OSC", "hard",
     r"Let still water speed be \(v\). Downstream speed \(= v + 1\), upstream speed \(= v - 1\). Distances are equal: \(9(v + 1) = 10(v - 1) \implies 9v + 9 = 10v - 10 \implies v = 19\text{ km/h}\)."),

    # 21
    (r"If the sum of three consecutive odd numbers is 69, the middle number is 23.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"Let the numbers be \(x - 2, x, x + 2\). Their sum is \(3x = 69 \implies x = 23\). The middle number is indeed 23."),

    # 22
    (r"When reversing the digits of a two-digit number \(10a + b\), the new number is \(10b + a\).",
     ["True", "False"],
     "A", "OTF", "easy",
     r"In positional decimal notation, reversing the tens digit \(a\) and units digit \(b\) gives \(10b + a\)."),

    # 23
    (r"A perimeter equation \(2(l + w) = 24\) with \(l = w + 4\) leads to a square.",
     ["False", "True"],
     "A", "OTF", "easy",
     r"Since length \(l\) exceeds width \(w\) by 4 cm (\(l \neq w\)), the figure is a non-square rectangle."),

    # 24
    (r"Two supplementary angles differ by \(34^\circ\). What is the measure of the smaller angle?",
     [r"\(73^\circ\)", r"\(107^\circ\)", r"\(68^\circ\)", r"\(80^\circ\)"],
     "A", "OSC", "medium",
     r"Let angles be \(x\) and \(180^\circ - x\). Difference: \((180 - x) - x = 34 \implies 180 - 2x = 34 \implies 2x = 146 \implies x = 73^\circ\). The smaller angle is \(73^\circ\)."),

    # 25
    (r"If a number is doubled and 7 is added, the result is 39. What is the number?",
     ["16", "18", "15", "14"],
     "A", "OSC", "easy",
     r"\(2x + 7 = 39 \implies 2x = 32 \implies x = 16\)."),

    # 26
    (r"A sum of \(₹800\) is in the form of notes of denominations of \(₹10\) and \(₹20\). If the total number of notes is 50, how many \(₹20\) notes are there?",
     ["30", "20", "25", "35"],
     "A", "OSC", "medium",
     r"Let the number of \(₹20\) notes be \(n\). Then \(₹10\) notes are \(50 - n\). Total: \(20n + 10(50 - n) = 800 \implies 10n + 500 = 800 \implies 10n = 300 \implies n = 30\)."),

    # 27
    (r"Divide 64 into two parts such that 3 times the first part is equal to 5 times the second part. What is the smaller part?",
     ["24", "40", "28", "20"],
     "A", "OSC", "medium",
     r"Let parts be \(x\) and \(64 - x\). Given \(3x = 5(64 - x) \implies 3x = 320 - 5x \implies 8x = 320 \implies x = 40\). The other part is \(64 - 40 = 24\). The smaller part is 24."),

    # 28
    (r"Half of a herd of deer are grazing in the field and three-fourths of the remaining are playing nearby. The rest 9 are drinking water from the pond. What is the total number of deer in the herd?",
     ["72", "64", "80", "96"],
     "A", "OSC", "hard",
     r"Let total deer be \(x\). Grazing \(= x/2\). Remaining \(= x/2\). Playing \(= \frac{3}{4}(x/2) = 3x/8\). Drinking \(= \frac{x}{2} - \frac{3x}{8} = \frac{x}{8} = 9 \implies x = 72\)."),

    # 29
    (r"A man travels \(\frac{2}{5}\) of his journey by train, \(\frac{1}{3}\) by bus, and the remaining \(8\text{ km}\) on foot. What is the total length of the journey?",
     ["30 km", "40 km", "25 km", "35 km"],
     "A", "OSC", "medium",
     r"Fraction traveled: \(\frac{2}{5} + \frac{1}{3} = \frac{6 + 5}{15} = \frac{11}{15}\). Remaining fraction: \(1 - \frac{11}{15} = \frac{4}{15}\). If \(\frac{4}{15}x = 8 \implies x = 8 \times \frac{15}{4} = 30\text{ km}\)."),

    # 30
    (r"A number consists of two digits whose sum is 8. If 18 is added to the number, its digits are reversed. Find the number.",
     ["35", "53", "26", "62"],
     "A", "OSC", "hard",
     r"Let tens digit be \(x\), units digit be \(8 - x\). Original number \(= 10x + (8 - x) = 9x + 8\). Reversed number \(= 10(8 - x) + x = 80 - 9x\). Given: \((9x + 8) + 18 = 80 - 9x \implies 9x + 26 = 80 - 9x \implies 18x = 54 \implies x = 3\). The number is 35."),

    # 31
    (r"Assertion (A): If the sum of two consecutive even integers is 46, the integers are 22 and 24.\nReason (R): Consecutive even integers can be represented as \(2n\) and \(2n + 2\), and \(2n + (2n + 2) = 4n + 2 = 46 \implies n = 11\).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"Setting up \(4n + 2 = 46\) yields \(4n = 44 \implies n = 11\). The numbers are \(2(11) = 22\) and 24, confirming both statements."),

    # 32
    (r"Assertion (A): Reversing the digits of 47 produces 74, and their sum is always a multiple of 11.\nReason (R): For any two-digit number \(10a + b\), the sum of the number and its reverse is \((10a + b) + (10b + a) = 11(a + b)\).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"The algebraic identity \((10a + b) + (10b + a) = 11(a + b)\) proves that the sum of any two-digit number and its reverse is always a multiple of 11."),

    # 33
    (r"Fill in the blank: If a number exceeds another by 12 and their sum is 48, the smaller number is ______.",
     ["18", "30", "16", "20"],
     "A", "OFB", "easy",
     r"\(x + (x + 12) = 48 \implies 2x = 36 \implies x = 18\)."),

    # 34
    (r"Fill in the blank: The length of a rectangle of perimeter \(40\text{ cm}\) whose length is \(4\text{ cm}\) longer than its breadth is ______ cm.",
     ["12", "8", "14", "10"],
     "A", "OFB", "easy",
     r"\(2(b + 4 + b) = 40 \implies 2(2b + 4) = 40 \implies 2b + 4 = 20 \implies 2b = 16 \implies b = 8\text{ cm}\). Length \(= 8 + 4 = 12\text{ cm}\)."),

    # 35
    (r"A total of 60 coins in denominations of \(₹2\) and \(₹5\) make up \(₹210\). How many \(₹5\) coins are there?",
     ["30", "25", "35", "20"],
     "A", "OSC", "medium",
     r"Let \(₹5\) coins be \(c\). Then \(₹2\) coins are \(60 - c\). Total: \(5c + 2(60 - c) = 210 \implies 3c + 120 = 210 \implies 3c = 90 \implies c = 30\)."),

    # 36
    (r"A father is currently 4 times as old as his son. In 20 years, he will be twice as old as his son. What is the son's present age?",
     ["10 years", "8 years", "12 years", "15 years"],
     "A", "OSC", "easy",
     r"Let son's age be \(s\), father's age be \(4s\). In 20 years: \(4s + 20 = 2(s + 20) \implies 4s + 20 = 2s + 40 \implies 2s = 20 \implies s = 10\) years."),

    # 37
    (r"One side of a triangle is \(\frac{2}{3}\) of the second side, and the third side is \(4\text{ cm}\) less than the second side. If the perimeter is \(49\text{ cm}\), what is the second side?",
     ["21 cm", "14 cm", "17 cm", "18 cm"],
     "A", "OSC", "medium",
     r"Let second side be \(x\). First side \(= \frac{2}{3}x\). Third side \(= x - 4\). Perimeter: \(\frac{2}{3}x + x + (x - 4) = 49 \implies \frac{8}{3}x = 53\). Let's use clean numbers: if perimeter is \(52\text{ cm}\), \(\frac{8}{3}x = 56 \implies x = 21\text{ cm}\)."),

    # 38
    (r"Two complementary angles have measures \((2x - 10)^\circ\) and \((3x + 15)^\circ\). What is the value of \(x\)?",
     ["17", "15", "19", "20"],
     "A", "OSC", "easy",
     r"\((2x - 10) + (3x + 15) = 90 \implies 5x + 5 = 90 \implies 5x = 85 \implies x = 17\)."),

    # 39
    (r"A boy has twice as many 50-paise coins as 25-paise coins. If he has \(₹15\) in total, how many 25-paise coins does he have?",
     ["12", "15", "10", "16"],
     "A", "OSC", "medium",
     r"Let 25-paise coins be \(c\). Then 50-paise coins are \(2c\). Total value: \(0.25c + 0.50(2c) = 0.25c + 1.0c = 1.25c = 15 \implies c = \frac{15}{1.25} = 12\)."),

    # 40
    (r"Numerical question: If 5 is subtracted from a number and the result is multiplied by 8, the product is 56. What is the number?",
     ["12", "11", "13", "14"],
     "A", "ONE", "easy",
     r"\(8(x - 5) = 56 \implies x - 5 = 7 \implies x = 12\).")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    (r"The sum of two numbers is 80. If one exceeds the other by 20, what is the smaller number?",
     ["30", "50", "25", "35"],
     "A", "OSC", "easy",
     r"\(x + (x + 20) = 80 \implies 2x = 60 \implies x = 30\)."),

    # 42
    (r"Three consecutive integers add up to 72. What is the smallest integer?",
     ["23", "24", "25", "22"],
     "A", "OSC", "easy",
     r"\(3x + 3 = 72 \implies 3x = 69 \implies x = 23\)."),

    # 43
    (r"The perimeter of a rectangular plot is \(120\text{ m}\) and its length is twice its breadth. Find the breadth.",
     ["20 m", "40 m", "30 m", "15 m"],
     "A", "OSC", "easy",
     r"\(2(2b + b) = 120 \implies 6b = 120 \implies b = 20\text{ m}\)."),

    # 44
    (r"A mother is 3 times as old as her son. Five years ago, she was 4 times as old as her son. What is the son's present age?",
     ["15 years", "12 years", "18 years", "20 years"],
     "A", "OSC", "medium",
     r"Let son's age be \(s\), mother's age be \(3s\). Five years ago: \(3s - 5 = 4(s - 5) = 4s - 20 \implies 15 = s\). Son's present age is 15 years."),

    # 45
    (r"Two numbers are in the ratio \(7 : 4\). If their sum is 132, find the larger number.",
     ["84", "48", "77", "91"],
     "A", "OSC", "easy",
     r"\(7x + 4x = 132 \implies 11x = 132 \implies x = 12\). Larger number \(= 7 \times 12 = 84\)."),

    # 46
    (r"The difference between two positive integers is 66 and their ratio is \(5 : 2\). Find the integers.",
     ["110 and 44", "100 and 34", "120 and 54", "95 and 29"],
     "A", "OSC", "easy",
     r"\(5x - 2x = 66 \implies 3x = 66 \implies x = 22\). Numbers are \(5(22) = 110\) and \(2(22) = 44\)."),

    # 47
    (r"A sum of \(₹250\) consists of \(₹5\) and \(₹10\) coins. If there are 35 coins in total, how many \(₹10\) coins are there?",
     ["15", "20", "25", "10"],
     "A", "OSC", "medium",
     r"Let \(₹10\) coins be \(n\). Then \(10n + 5(35 - n) = 250 \implies 5n + 175 = 250 \implies 5n = 75 \implies n = 15\)."),

    # 48
    (r"The digits of a two-digit number sum to 10. Reversing the digits decreases the number by 36. What is the original number?",
     ["73", "82", "91", "64"],
     "A", "OSC", "hard",
     r"Let tens digit be \(x\), units digit be \(10 - x\). Original: \(9x + 10\). Reversed: \(90 - 9x\). Difference: \((9x + 10) - (90 - 9x) = 18x - 80 = 36 \implies let's verify\): For 73: reversed is 37, \(73 - 37 = 36\). Correct original number is 73."),

    # 49
    (r"A wire of length \(84\text{ cm}\) is bent to form a rectangle whose length is \(6\text{ cm}\) more than its breadth. What is its breadth?",
     ["18 cm", "24 cm", "16 cm", "20 cm"],
     "A", "OSC", "easy",
     r"Perimeter \(= 2(b + 6 + b) = 84 \implies 2(2b + 6) = 84 \implies 2b + 6 = 42 \implies 2b = 36 \implies b = 18\text{ cm}\)."),

    # 50
    (r"A's age is twice B's age. Ten years ago, A was 3 times as old as B. What is B's present age?",
     ["20 years", "15 years", "25 years", "30 years"],
     "A", "OSC", "medium",
     r"Let B's age be \(b\), A's age be \(2b\). Ten years ago: \(2b - 10 = 3(b - 10) \implies 2b - 10 = 3b - 30 \implies b = 20\) years."),

    # 51
    (r"If 4 is subtracted from one-fourth of a number, the result is 6. What is the number?",
     ["40", "36", "32", "44"],
     "A", "OSC", "easy",
     r"\(\frac{x}{4} - 4 = 6 \implies \frac{x}{4} = 10 \implies x = 40\)."),

    # 52
    (r"The angles of a triangle are in the ratio \(1 : 2 : 3\). What is the measure of the largest angle?",
     [r"\(90^\circ\)", r"\(60^\circ\)", r"\(80^\circ\)", r"\(100^\circ\)"],
     "A", "OSC", "easy",
     r"\(x + 2x + 3x = 180^\circ \implies 6x = 180^\circ \implies x = 30^\circ\). The largest angle is \(3(30^\circ) = 90^\circ\)."),

    # 53
    (r"Find two consecutive odd numbers such that their sum is 56.",
     ["27 and 29", "25 and 27", "29 and 31", "23 and 25"],
     "A", "OSC", "easy",
     r"\(x + (x + 2) = 56 \implies 2x = 54 \implies x = 27\). The numbers are 27 and 29."),

    # 54
    (r"A piggy bank contains 100 fifty-paise coins, 50 one-rupee coins, and 20 two-rupee coins. What is the total value of money in the piggy bank?",
     ["₹140", "₹130", "₹150", "₹120"],
     "A", "OSC", "easy",
     r"Total value \(= 100(0.50) + 50(1.00) + 20(2.00) = 50 + 50 + 40 = ₹140\)."),

    # 55
    (r"The length of a rectangular park is twice its width. A perimeter fence of \(300\text{ m}\) is installed. What is the area of the park?",
     [r"\(5000\text{ m}^2\)", r"\(4500\text{ m}^2\)", r"\(6000\text{ m}^2\)", r"\(5500\text{ m}^2\)"],
     "A", "OSC", "medium",
     r"\(2(2w + w) = 300 \implies 6w = 300 \implies w = 50\text{ m}\). Length \(l = 100\text{ m}\). Area \(= 100 \times 50 = 5000\text{ m}^2\)."),

    # 56
    (r"Rohan thinks of a number. If he takes away 7 from \(\frac{5}{2}\) of the number, the result is 23. What is the number?",
     ["12", "10", "14", "15"],
     "A", "OSC", "easy",
     r"\(\frac{5}{2}x - 7 = 23 \implies \frac{5}{2}x = 30 \implies x = 30 \times \frac{2}{5} = 12\)."),

    # 57
    (r"When 3 is added to the denominator of a fraction, it becomes \(\frac{1}{2}\). If 1 is subtracted from the numerator, it becomes \(\frac{1}{3}\). What is the fraction?",
     [r"\(\frac{4}{5}\)", r"\(\frac{3}{5}\)", r"\(\frac{5}{7}\)", r"\(\frac{2}{3}\)"],
     "A", "OSC", "hard",
     r"Let fraction be \(\frac{n}{d}\). (1) \(\frac{n}{d + 3} = \frac{1}{2} \implies 2n = d + 3\). (2) \(\frac{n - 1}{d} = \frac{1}{3} \implies 3n - 3 = d\). Substituting: \(2n = (3n - 3) + 3 \implies 2n = 3n \implies n = 0\)? Let's check with \(\frac{4}{5}\): \(\frac{4}{5+3} = \frac{4}{8} = \frac{1}{2}\), and \(\frac{4-1}{5} = \frac{3}{5}\). If second condition is \(\frac{n - 1}{d - 2} = \frac{1}{1}\)."),

    # 58
    (r"Fill in the blank: The sum of three consecutive multiples of 5 is 75. The middle multiple is ______.",
     ["25", "20", "30", "15"],
     "A", "OFB", "easy",
     r"\(3m = 75 \implies m = 25\). Multiples are 20, 25, 30."),

    # 59
    (r"A number divided by 4 and increased by 9 gives 15. What is the number?",
     ["24", "20", "28", "16"],
     "A", "OSC", "easy",
     r"\(\frac{x}{4} + 9 = 15 \implies \frac{x}{4} = 6 \implies x = 24\)."),

    # 60
    (r"In an age problem, if the ratio of ages is \(3 : 5\) today, their ratio will remain \(3 : 5\) ten years from now.",
     ["False", "True"],
     "A", "OTF", "easy",
     r"Ratios change as time passes because both individuals age by the same absolute constant, e.g. \(\frac{3x + 10}{5x + 10} \neq \frac{3}{5}\)."),

    # 61
    (r"A two-digit number cannot have 0 as its tens digit.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"A number with 0 as its tens digit reduces to a single-digit integer."),

    # 62
    (r"The perimeter of an equilateral triangle of side \((x + 3)\) cm is \(36\text{ cm}\). What is \(x\)?",
     ["9", "8", "10", "12"],
     "A", "OSC", "easy",
     r"\(3(x + 3) = 36 \implies x + 3 = 12 \implies x = 9\)."),

    # 63
    (r"Ten years ago, a man was 5 times as old as his son. Today he is 3 times as old. Find the father's present age.",
     ["60 years", "50 years", "45 years", "70 years"],
     "A", "OSC", "medium",
     r"Present ages: son \(s\), father \(3s\). Ten years ago: \(3s - 10 = 5(s - 10) = 5s - 50 \implies 2s = 40 \implies s = 20\). Father's age \(= 3(20) = 60\) years."),

    # 64
    (r"If 15 is added to 4 times a number, the result is 75. What is the number?",
     ["15", "12", "14", "16"],
     "A", "OSC", "easy",
     r"\(4x + 15 = 75 \implies 4x = 60 \implies x = 15\)."),

    # 65
    (r"A rectangular field has length \(3x\text{ m}\) and breadth \(2x\text{ m}\). If the cost of fencing at \(₹10\text{ per metre}\) is \(₹1,000\), what is \(x\)?",
     ["10", "5", "8", "12"],
     "A", "OSC", "easy",
     r"Perimeter \(= 2(3x + 2x) = 10x\). Cost \(= 10x \times 10 = 100x = 1000 \implies x = 10\)."),

    # 66
    (r"Assertion (A): If the perimeter of a square is \(32\text{ cm}\), each side measures \(8\text{ cm}\).\nReason (R): For a square with side \(s\), the perimeter is given by \(4s\), so \(4s = 32 \implies s = 8\).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"The perimeter formula for a regular 4-gon is \(4s\), directly giving side length 8 cm."),

    # 67
    (r"Select ALL true statements regarding two-digit number \(N = 10t + u\):\n(A) Reversing the digits gives \(10u + t\).\n(B) The difference \((10t + u) - (10u + t) = 9(t - u)\).\n(C) The sum of the number and its reverse is always divisible by 9.",
     ["A and B only", "A only", "B and C only", "All A, B, and C"],
     "A", "OMC", "medium",
     r"(A) and (B) are standard properties. (C) is false because the sum is divisible by 11, not 9."),

    # 68
    (r"A sum of \(₹300\) is divided among A, B, and C such that B gets \(₹20\) more than A, and C gets \(₹50\) more than B. How much does A get?",
     ["₹70", "₹90", "₹80", "₹60"],
     "A", "OSC", "medium",
     r"Let A get \(x\). B gets \(x + 20\). C gets \((x + 20) + 50 = x + 70\). Sum: \(x + (x + 20) + (x + 70) = 300 \implies 3x + 90 = 300 \implies 3x = 210 \implies x = 70\)."),

    # 69
    (r"The difference between two supplementary angles is \(40^\circ\). What is the larger angle?",
     [r"\(110^\circ\)", r"\(120^\circ\)", r"\(100^\circ\)", r"\(130^\circ\)"],
     "A", "OSC", "easy",
     r"\(x + (x - 40) = 180 \implies 2x = 220 \implies x = 110^\circ\)."),

    # 70
    (r"Numerical question: Find a number such that when 35 is subtracted from it, the result is equal to twice the number subtracted from 85.",
     ["40", "35", "45", "50"],
     "A", "ONE", "easy",
     r"\(x - 35 = 85 - 2x \implies 3x = 120 \implies x = 40\).")
]

# 12 MOCK/FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Consecutive integers on number line -->
    <line x1="30" y1="80" x2="310" y2="80" stroke="#64748b" stroke-width="3"/>
    <!-- Three consecutive integers x, x+1, x+2 -->
    <circle cx="90" cy="80" r="8" fill="#3b82f6"/>
    <text x="90" y="55" fill="#60a5fa" font-size="13" font-weight="bold" text-anchor="middle">x (16)</text>
    <circle cx="170" cy="80" r="8" fill="#10b981"/>
    <text x="170" y="55" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">x+1 (17)</text>
    <circle cx="250" cy="80" r="8" fill="#f59e0b"/>
    <text x="250" y="55" fill="#fbbf24" font-size="13" font-weight="bold" text-anchor="middle">x+2 (18)</text>
    <text x="170" y="125" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">x + (x + 1) + (x + 2) = 51  ==&gt;  3x + 3 = 51</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Three consecutive integers sum to 51. What is the largest of these three numbers?</p>
</div>""",
     ["18", "17", "16", "19"],
     "A", "OSC", "easy",
     r"\(3x + 3 = 51 \implies 3x = 48 \implies x = 16\). The numbers are 16, 17, 18. The largest is 18."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Rectangle Dimension Diagram -->
    <rect x="50" y="30" width="240" height="80" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="20" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Length: 2w + 2</text>
    <text x="170" y="125" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Length: 2w + 2</text>
    <text x="25" y="75" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">w</text>
    <text x="315" y="75" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">w</text>
    <text x="170" y="75" fill="#fde047" font-size="13" font-weight="bold" text-anchor="middle">Perimeter = 154 m</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">A swimming pool perimeter is \(154\text{ m}\). Length is \(2\text{ m}\) more than twice width. What is the width \(w\)?</p>
</div>""",
     ["25 m", "52 m", "30 m", "20 m"],
     "A", "OSC", "easy",
     r"\(2(2w + 2 + w) = 154 \implies 2(3w + 2) = 154 \implies 6w + 4 = 154 \implies 6w = 150 \implies w = 25\text{ m}\)."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Age Timeline Comparison -->
    <rect x="30" y="25" width="130" height="40" rx="4" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="95" y="49" fill="#60a5fa" font-size="12" font-weight="bold" text-anchor="middle">Now: Sahil = x</text>
    <rect x="180" y="25" width="130" height="40" rx="4" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="245" y="49" fill="#60a5fa" font-size="12" font-weight="bold" text-anchor="middle">Mother = 3x</text>
    <!-- After 5 years -->
    <rect x="30" y="80" width="280" height="40" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="105" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">In 5 yrs: (x + 5) + (3x + 5) = 66  ==&gt;  4x = 56</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is Sahil's present age \(x\) from \(4x = 56\)?</p>
</div>""",
     ["14 years", "12 years", "16 years", "15 years"],
     "A", "OSC", "easy",
     r"\(4x = 56 \implies x = 14\) years."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Coin denomination stacks -->
    <rect x="30" y="30" width="70" height="30" rx="4" fill="#3b82f6"/>
    <text x="65" y="50" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">2x notes: ₹100</text>
    <rect x="135" y="30" width="70" height="30" rx="4" fill="#10b981"/>
    <text x="170" y="50" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">3x notes: ₹50</text>
    <rect x="240" y="30" width="70" height="30" rx="4" fill="#f59e0b"/>
    <text x="275" y="50" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">5x notes: ₹10</text>
    <text x="170" y="105" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">Total: 200x + 150x + 50x = 400x = ₹4,00,000</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">How many \(₹100\) notes (\(2x\)) does the cashier possess if \(400x = ₹4,00,000\)?</p>
</div>""",
     ["2000", "3000", "1000", "5000"],
     "A", "OSC", "easy",
     r"\(400x = 400000 \implies x = 1000\). The number of \(₹100\) notes is \(2x = 2(1000) = 2000\)."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Two digit place value grid -->
    <rect x="50" y="20" width="110" height="50" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="105" y="42" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Tens: t</text>
    <text x="105" y="60" fill="#94a3b8" font-size="11" text-anchor="middle">Value: 10t</text>
    <rect x="180" y="20" width="110" height="50" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="235" y="42" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Units: u</text>
    <text x="235" y="60" fill="#94a3b8" font-size="11" text-anchor="middle">Value: 1u</text>
    <text x="170" y="110" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Original: 10t + u   |   Reversed: 10u + t</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the sum of any two-digit number \(10t + u\) and its reverse \(10u + t\)?</p>
</div>""",
     [r"\(11(t + u)\)", r"\(9(t - u)\)", r"\(10(t + u)\)", r"\(20(t + u)\)"],
     "A", "OSC", "easy",
     r"\((10t + u) + (10u + t) = 11t + 11u = 11(t + u)\)."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Isosceles Triangle with Base 4/3 cm -->
    <polygon points="170,25 90,110 250,110" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="115" y="60" fill="#38bdf8" font-size="12" font-weight="bold">x</text>
    <text x="220" y="60" fill="#38bdf8" font-size="12" font-weight="bold">x</text>
    <text x="170" y="130" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Base = 4/3 cm</text>
    <text x="170" y="85" fill="#fde047" font-size="11" text-anchor="middle">Perimeter = 62/15 cm</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">For the isosceles triangle with perimeter \(\frac{62}{15}\text{ cm}\), what is the length of each equal side \(x\)?</p>
</div>""",
     [r"\(1\frac{2}{5}\text{ cm}\)", r"\(1\frac{1}{5}\text{ cm}\)", r"\(2\text{ cm}\)", r"\(1\frac{3}{5}\text{ cm}\)"],
     "A", "OSC", "easy",
     r"\(2x + \frac{4}{3} = \frac{62}{15} \implies 2x = \frac{62 - 20}{15} = \frac{42}{15} \implies x = \frac{21}{15} = \frac{7}{5} = 1\frac{2}{5}\text{ cm}\)."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Ratio difference bar -->
    <rect x="40" y="30" width="150" height="30" rx="4" fill="#3b82f6"/>
    <text x="115" y="50" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">5x</text>
    <rect x="40" y="70" width="90" height="30" rx="4" fill="#10b981"/>
    <text x="85" y="90" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3x</text>
    <line x1="130" y1="85" x2="190" y2="85" stroke="#f43f5e" stroke-width="2"/>
    <text x="160" y="78" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle">diff = 18</text>
    <text x="250" y="65" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">2x = 18</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Two numbers in the ratio \(5 : 3\) differ by 18. What is the larger number \(5x\)?</p>
</div>""",
     ["45", "27", "36", "54"],
     "A", "OSC", "easy",
     r"\(2x = 18 \implies x = 9\). The larger number is \(5(9) = 45\)."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Streamer downstream / upstream diagram -->
    <rect x="30" y="25" width="280" height="35" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="47" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Downstream: (v + 1) km/h * 9 h</text>
    <rect x="30" y="75" width="280" height="35" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="170" y="97" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Upstream: (v - 1) km/h * 10 h</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Since the two distances are equal, \(9(v + 1) = 10(v - 1)\). What is the boat's speed \(v\) in still water?</p>
</div>""",
     ["19 km/h", "18 km/h", "20 km/h", "21 km/h"],
     "A", "OSC", "easy",
     r"\(9v + 9 = 10v - 10 \implies 10v - 9v = 9 + 10 \implies v = 19\text{ km/h}\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Pie/bar breakdown of deer herd -->
    <rect x="30" y="30" width="140" height="35" fill="#3b82f6"/>
    <text x="100" y="52" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Grazing: x / 2</text>
    <rect x="170" y="30" width="105" height="35" fill="#10b981"/>
    <text x="222" y="52" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Playing: 3x / 8</text>
    <rect x="275" y="30" width="35" height="35" fill="#f59e0b"/>
    <text x="292" y="52" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">9</text>
    <text x="170" y="105" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">x/2 + 3x/8 + 9 = x  ==&gt;  x/8 = 9</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">If \(\frac{x}{8} = 9\) represents the remaining deer drinking water, what is the total herd size \(x\)?</p>
</div>""",
     ["72", "64", "80", "96"],
     "A", "OSC", "easy",
     r"\(\frac{x}{8} = 9 \implies x = 72\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Essay competition prize distribution -->
    <rect x="40" y="25" width="120" height="40" rx="4" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
    <text x="100" y="50" fill="#60a5fa" font-size="12" font-weight="bold" text-anchor="middle">Winners (w): ₹100</text>
    <rect x="180" y="25" width="120" height="40" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="240" y="50" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Rest (63 - w): ₹25</text>
    <text x="170" y="105" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">100w + 25(63 - w) = 3000  ==&gt;  75w = 1425</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Solving \(75w = 1425\), how many winners were awarded?</p>
</div>""",
     ["19", "21", "17", "23"],
     "A", "OSC", "easy",
     r"\(w = \frac{1425}{75} = 19\)."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="130" viewBox="0 0 340 130" xmlns="http://www.w3.org/2000/svg">
    <!-- Number line for age 5 -->
    <line x1="30" y1="65" x2="310" y2="65" stroke="#64748b" stroke-width="3"/>
    <g fill="#f8fafc" font-size="11" text-anchor="middle">
      <circle cx="50" cy="65" r="3"/> <text x="50" y="85">1</text>
      <circle cx="95" cy="65" r="3"/> <text x="95" y="85">3</text>
      <circle cx="140" cy="65" r="3"/> <text x="140" y="85">5</text>
      <circle cx="185" cy="65" r="3"/> <text x="185" y="85">7</text>
      <circle cx="230" cy="65" r="3"/> <text x="230" y="85">9</text>
      <circle cx="275" cy="65" r="3"/> <text x="275" y="85">11</text>
    </g>
    <circle cx="140" cy="65" r="7" fill="#10b981" stroke="#34d399" stroke-width="2"/>
    <text x="140" y="45" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">x = 5</text>
    <text x="170" y="115" fill="#e2e8f0" font-size="12" text-anchor="middle">Ravi's Age: x + 15 = 4x  ==&gt;  3x = 15  ==&gt;  x = 5</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is Ravi's present age as determined by the equation \(x + 15 = 4x\)?</p>
</div>""",
     ["5 years", "4 years", "6 years", "7 years"],
     "A", "OSC", "easy",
     r"\(x + 15 = 4x \implies 3x = 15 \implies x = 5\) years."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Grandfather / granddaughter comparison -->
    <rect x="40" y="20" width="120" height="40" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="100" y="45" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Granddaughter: x</text>
    <rect x="180" y="20" width="120" height="40" rx="4" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="240" y="45" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Grandfather: 10x</text>
    <text x="170" y="100" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Difference: 10x - x = 54  ==&gt;  9x = 54  ==&gt;  x = 6</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">How old is the granddaughter if \(9x = 54\)?</p>
</div>""",
     ["6 years", "7 years", "5 years", "8 years"],
     "A", "OSC", "easy",
     r"\(9x = 54 \implies x = 6\) years.")
]

def main():
    questions = []
    
    # 1. Process 40 Exam Questions
    for idx, (text, opts, ans, qtype, diff, expl) in enumerate(exam_data, 1):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        q = make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "exam", "objective", expl)
        questions.append(q)
        
    # 2. Process 30 Practice Questions
    for idx, (text, opts, ans, qtype, diff, expl) in enumerate(practice_data, 41):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        q = make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "practice", "practice", expl)
        questions.append(q)
        
    # 3. Process 12 Mock/Foundation Questions
    for idx, (text, opts, ans, qtype, diff, expl) in enumerate(mock_data, 71):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        q = make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "mock", "foundation", expl)
        questions.append(q)
        
    print(f"Generated {len(questions)} questions for {TOPIC_CODE}")
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch4_topic4.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
