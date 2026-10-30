# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for MH-10-MTH1-1-1.5
Topic: Applied Word Problems (Numbers, Age, Speed-Distance, Boat & Stream)
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

TOPIC_CODE = "MH-10-MTH1-1-1.5"

# 40 EXAM (1-40)
exam_data = [
    # 1
    ("Two numbers differ by 3. The sum of twice the smaller number and thrice the greater number is 19. Find the numbers.",
     ["5 and 2", "7 and 4", "6 and 3", "8 and 5"],
     "A", "OSC", "medium",
     "Let greater number be \\(x\\) and smaller number be \\(y\\). Given: \\(x - y = 3\\) and \\(3x + 2y = 19\\). From first, \\(x = y + 3\\). Substitute: \\(3(y + 3) + 2y = 19 \\implies 3y + 9 + 2y = 19 \\implies 5y = 10 \\implies y = 2\\). Then \\(x = 2 + 3 = 5\\). The numbers are 5 and 2."),

    # 2
    ("The sum of father's age and twice the age of his son is 70. If we double the age of the father and add it to the age of his son, the sum is 95. Find their present ages.",
     ["Father: 40 years, Son: 15 years",
      "Father: 45 years, Son: 12.5 years",
      "Father: 38 years, Son: 16 years",
      "Father: 50 years, Son: 10 years"],
     "A", "OSC", "medium",
     "Let father's age be \\(x\\) and son's age be \\(y\\). Equations: \\(x + 2y = 70\\) and \\(2x + y = 95\\). Adding both: \\(3x + 3y = 165 \\implies x + y = 55\\). Subtracting first from second: \\(x - y = 25\\). Adding these simplified equations: \\(2x = 80 \\implies x = 40\\). Then \\(y = 55 - 40 = 15\\)."),

    # 3
    ("The denominator of a fraction is 4 more than twice its numerator. Denominator becomes 12 times the numerator if both are reduced by 6. Find the fraction.",
     ["\\(\\frac{7}{18}\\)", "\\(\\frac{5}{14}\\)", "\\(\\frac{3}{10}\\)", "\\(\\frac{9}{22}\\)"],
     "A", "OSC", "hard",
     "Let numerator be \\(x\\) and denominator be \\(y\\). Condition 1: \\(y = 2x + 4 \\implies 2x - y = -4\\). Condition 2: \\(y - 6 = 12(x - 6) \\implies y - 6 = 12x - 72 \\implies 12x - y = 66\\). Subtracting first from second: \\(10x = 70 \\implies x = 7\\). Then \\(y = 2(7) + 4 = 18\\). The fraction is \\(7/18\\)."),

    # 4
    ("In a rectangle, the opposite sides are \\(2x + y + 8\\) and \\(4x - y\\) (lengths), and \\(2y\\) and \\(x + 4\\) (breadths). Find the values of \\(x\\) and \\(y\\).",
     ["\\(x = 12, y = 8\\)", "\\(x = 8, y = 12\\)", "\\(x = 10, y = 6\\)", "\\(x = 14, y = 10\\)"],
     "A", "OSC", "medium",
     "Equating lengths: \\(2x + y + 8 = 4x - y \\implies 2x - 2y = 8 \\implies x - y = 4\\). Equating breadths: \\(x + 4 = 2y \\implies x - 2y = -4\\). Subtracting the equations gives \\(y = 8\\). Then \\(x = 8 + 4 = 12\\)."),

    # 5
    ("Using \\(x = 12, y = 8\\) from the previous rectangle problem, find its perimeter.",
     ["112 units", "100 units", "120 units", "96 units"],
     "A", "OSC", "easy",
     "Length = \\(4(12) - 8 = 48 - 8 = 40\\). Breadth = \\(2(8) = 16\\). Perimeter = \\(2(\\text{length} + \\text{breadth}) = 2(40 + 16) = 2(56) = 112\\) units."),

    # 6
    ("Using length = 40 and breadth = 16, find the area of the rectangle.",
     ["640 sq units", "560 sq units", "720 sq units", "800 sq units"],
     "A", "OSC", "easy",
     "Area = \\(\\text{length} \\times \\text{breadth} = 40 \\times 16 = 640\\) sq units."),

    # 7
    ("Out of 1900 km, Vishal travelled some distance by bus at 60 km/h and the remaining distance by aeroplane at 700 km/h. The entire journey took 5 hours. Find the distance travelled by bus.",
     ["150 km", "200 km", "120 km", "180 km"],
     "A", "OSC", "hard",
     "Let distance by bus be \\(x\\) km and by aeroplane be \\(y\\) km. \\(x + y = 1900\\). Total time: \\(\\frac{x}{60} + \\frac{y}{700} = 5\\). Multiply by 2100: \\(35x + 3y = 10500\\). From first, \\(3x + 3y = 5700\\). Subtracting: \\(32x = 4800 \\implies x = 150\\) km."),

    # 8
    ("In the previous problem, what distance did Vishal travel by aeroplane?",
     ["1750 km", "1700 km", "1800 km", "1650 km"],
     "A", "OSC", "easy",
     "Distance by aeroplane = \\(1900 - 150 = 1750\\) km."),

    # 9
    ("A truck has a capacity of 10 tonnes (10,000 kg). When 150 boxes of type A and 100 boxes of type B are loaded, it weighs 10 tonnes. When 260 boxes of type A and 40 boxes of type B are loaded, it also weighs 10 tonnes. Find the weight of one box of type A.",
     ["30 kg", "25 kg", "40 kg", "50 kg"],
     "A", "OSC", "hard",
     "Let weights be \\(a\\) and \\(b\\) in kg. \\(150a + 100b = 10000 \\implies 3a + 2b = 200\\). Second: \\(260a + 40b = 10000 \\implies 13a + 2b = 500\\). Subtracting: \\(10a = 300 \\implies a = 30\\) kg."),

    # 10
    ("From the box problem above, find the weight of one box of type B.",
     ["55 kg", "50 kg", "60 kg", "45 kg"],
     "A", "OSC", "easy",
     "\\(3(30) + 2b = 200 \\implies 90 + 2b = 200 \\implies 2b = 110 \\implies b = 55\\) kg."),

    # 11
    ("A two-digit number is 4 times the sum of its digits. If 18 is added to the number, the digits reverse their places. Find the number.",
     ["24", "42", "36", "48"],
     "A", "OSC", "medium",
     "Let tens digit be \\(x\\) and units digit be \\(y\\). Number is \\(10x + y\\). Given \\(10x + y = 4(x + y) \\implies 6x - 3y = 0 \\implies y = 2x\\). Reversed number is \\(10y + x\\). Given: \\((10x + y) + 18 = 10y + x \\implies 9y - 9x = 18 \\implies y - x = 2\\). Substitute \\(y = 2x\\): \\(2x - x = 2 \\implies x = 2\\). Then \\(y = 4\\). Number is 24."),

    # 12
    ("The sum of the digits of a two-digit number is 9. Also, nine times this number is twice the number obtained by reversing the order of the digits. Find the number.",
     ["18", "27", "36", "45"],
     "A", "OSC", "medium",
     "\\(x + y = 9\\). Condition: \\(9(10x + y) = 2(10y + x) \\implies 90x + 9y = 20y + 2x \\implies 88x - 11y = 0 \\implies 8x = y\\). Substitute into \\(x + 8x = 9 \\implies 9x = 9 \\implies x = 1, y = 8\\). The number is 18."),

    # 13
    ("A boat goes 30 km upstream and 44 km downstream in 10 hours. In 13 hours, it can go 40 km upstream and 55 km downstream. Find the speed of the boat in still water.",
     ["8 km/h", "6 km/h", "10 km/h", "7 km/h"],
     "A", "OSC", "hard",
     "Let boat speed be \\(x\\) and stream speed be \\(y\\). Upstream speed = \\(x - y\\), downstream speed = \\(x + y\\). \\(\\frac{30}{x-y} + \\frac{44}{x+y} = 10\\) and \\(\\frac{40}{x-y} + \\frac{55}{x+y} = 13\\). Let \\(u = \\frac{1}{x-y}, v = \\frac{1}{x+y}\\). Solving yields \\(u = \\frac{1}{5}, v = \\frac{1}{11}\\). Thus \\(x - y = 5\\) and \\(x + y = 11\\). Adding: \\(2x = 16 \\implies x = 8\\) km/h."),

    # 14
    ("In the boat and stream problem above, what is the speed of the stream?",
     ["3 km/h", "2 km/h", "4 km/h", "1.5 km/h"],
     "A", "OSC", "easy",
     "\\(y = 11 - 8 = 3\\) km/h."),

    # 15
    ("The perimeter of an isosceles triangle is 30 cm. The length of each equal side is 3 cm more than the base. Find the length of the base.",
     ["8 cm", "11 cm", "10 cm", "6 cm"],
     "A", "OSC", "medium",
     "Let base be \\(x\\) and equal sides be \\(y\\). Given: \\(y = x + 3\\). Perimeter: \\(x + 2y = 30\\). Substitute: \\(x + 2(x + 3) = 30 \\implies 3x + 6 = 30 \\implies 3x = 24 \\implies x = 8\\) cm."),

    # 16
    ("From the previous problem, what is the length of each equal side?",
     ["11 cm", "8 cm", "14 cm", "10 cm"],
     "A", "OSC", "easy",
     "\\(y = x + 3 = 8 + 3 = 11\\) cm."),

    # 17
    ("Two angles are complementary. The larger angle is \\(3^\\circ\\) less than twice the measure of the smaller angle. Find the smaller angle.",
     ["\\(31^\\circ\\)", "\\(59^\\circ\\)", "\\(30^\\circ\\)", "\\(28^\\circ\\)"],
     "A", "OSC", "medium",
     "Let angles be \\(x\\) and \\(y\\). Complementary: \\(x + y = 90^\\circ\\). Given: \\(x = 2y - 3\\). Substitute: \\((2y - 3) + y = 90 \\implies 3y = 93 \\implies y = 31^\\circ\\)."),

    # 18
    ("From the previous question, what is the larger complementary angle?",
     ["\\(59^\\circ\\)", "\\(61^\\circ\\)", "\\(60^\\circ\\)", "\\(58^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(x = 90^\\circ - 31^\\circ = 59^\\circ\\)."),

    # 19
    ("The sum of two supplementary angles is \\(180^\\circ\\). If the larger angle exceeds the smaller by \\(36^\\circ\\), find the smaller angle.",
     ["\\(72^\\circ\\)", "\\(108^\\circ\\)", "\\(80^\\circ\\)", "\\(70^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(x + y = 180\\) and \\(x - y = 36\\). Subtracting: \\(2y = 144 \\implies y = 72^\\circ\\)."),

    # 20
    ("From the previous problem, what is the larger supplementary angle?",
     ["\\(108^\\circ\\)", "\\(72^\\circ\\)", "\\(110^\\circ\\)", "\\(120^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(x = 180^\\circ - 72^\\circ = 108^\\circ\\)."),

    # 21
    ("Meena went to a bank to withdraw Rs 2000. She asked the cashier to give her Rs 50 and Rs 100 notes only. Meena got 25 notes in all. How many Rs 50 notes did she receive?",
     ["10", "15", "12", "8"],
     "A", "OSC", "medium",
     "Let number of Rs 50 notes be \\(x\\) and Rs 100 notes be \\(y\\). \\(x + y = 25\\) and \\(50x + 100y = 2000 \\implies x + 2y = 40\\). Subtracting: \\(y = 15\\). Then \\(x = 25 - 15 = 10\\). She got 10 notes of Rs 50."),

    # 22
    ("From the previous problem, how many Rs 100 notes did Meena receive?",
     ["15", "10", "20", "5"],
     "A", "OSC", "easy",
     "\\(y = 15\\) notes of Rs 100."),

    # 23
    ("The taxi fare in a city comprises a fixed charge together with the charge for the distance covered. For a distance of 10 km, the charge paid is Rs 105 and for a journey of 15 km, the charge paid is Rs 155. What is the charge per km?",
     ["Rs 10", "Rs 5", "Rs 15", "Rs 8"],
     "A", "OSC", "medium",
     "Let fixed charge be \\(x\\) and rate per km be \\(y\\). \\(x + 10y = 105\\) and \\(x + 15y = 155\\). Subtracting: \\(5y = 50 \\implies y = 10\\) Rs/km."),

    # 24
    ("From the previous problem, what is the fixed charge of the taxi?",
     ["Rs 5", "Rs 10", "Rs 15", "Rs 0"],
     "A", "OSC", "easy",
     "\\(x + 10(10) = 105 \\implies x + 100 = 105 \\implies x = 5\\) Rs."),

    # 25
    ("How much would a person have to pay for travelling a distance of 25 km in the taxi above?",
     ["Rs 255", "Rs 250", "Rs 260", "Rs 275"],
     "A", "OSC", "easy",
     "Cost = \\(x + 25y = 5 + 25(10) = 5 + 250 = 255\\) Rs."),

    # 26
    ("Five years ago, Nuri was thrice as old as Sonu. Ten years later, Nuri will be twice as old as Sonu. How old is Nuri now?",
     ["50 years", "20 years", "40 years", "60 years"],
     "A", "OSC", "medium",
     "Let Nuri be \\(x\\) and Sonu be \\(y\\). 5 years ago: \\(x - 5 = 3(y - 5) \\implies x - 3y = -10\\). 10 years later: \\(x + 10 = 2(y + 10) \\implies x - 2y = 10\\). Subtracting: \\(y = 20\\). Then \\(x = 2(20) + 10 = 50\\) years."),

    # 27
    ("From the previous problem, how old is Sonu now?",
     ["20 years", "25 years", "15 years", "30 years"],
     "A", "OSC", "easy",
     "Sonu is \\(y = 20\\) years old."),

    # 28
    ("The sum of a two-digit number and the number obtained by reversing the digits is 66. If the digits of the number differ by 2, find the number (if tens digit is greater).",
     ["42", "24", "53", "35"],
     "A", "OSC", "medium",
     "\\((10x + y) + (10y + x) = 66 \\implies 11x + 11y = 66 \\implies x + y = 6\\). If \\(x - y = 2\\), adding gives \\(2x = 8 \\implies x = 4\\), so \\(y = 2\\). The number is 42."),

    # 29
    ("A fraction becomes \\(\\frac{1}{3}\\) when 1 is subtracted from the numerator and it becomes \\(\\frac{1}{4}\\) when 8 is added to its denominator. Find the fraction.",
     ["\\(\\frac{5}{12}\\)", "\\(\\frac{7}{12}\\)", "\\(\\frac{4}{15}\\)", "\\(\\frac{3}{8}\\)"],
     "A", "OSC", "hard",
     "\\(\\frac{x - 1}{y} = \\frac{1}{3} \\implies 3x - y = 3\\). \\(\\frac{x}{y + 8} = \\frac{1}{4} \\implies 4x - y = 8\\). Subtracting: \\(x = 5\\). Then \\(y = 3(5) - 3 = 12\\). Fraction is \\(5/12\\)."),

    # 30
    ("Places A and B are 100 km apart on a highway. One car starts from A and another from B at the same time. If the cars travel in the same direction at different speeds, they meet in 5 hours. If they travel towards each other, they meet in 1 hour. What is the speed of the faster car?",
     ["60 km/h", "40 km/h", "50 km/h", "70 km/h"],
     "A", "OSC", "hard",
     "Let speeds be \\(x\\) and \\(y\\) (with \\(x > y\\)). Same direction: relative speed \\(x - y = \\frac{100}{5} = 20\\). Opposite direction: relative speed \\(x + y = \\frac{100}{1} = 100\\). Adding gives \\(2x = 120 \\implies x = 60\\) km/h."),

    # 31
    ("From the car problem above, what is the speed of the slower car?",
     ["40 km/h", "50 km/h", "30 km/h", "45 km/h"],
     "A", "OSC", "easy",
     "\\(y = 100 - 60 = 40\\) km/h."),

    # 32
    ("The area of a rectangle gets reduced by 9 sq units, if its length is reduced by 5 units and breadth is increased by 3 units. If we increase the length by 3 units and breadth by 2 units, the area increases by 67 sq units. Find the length.",
     ["17 units", "9 units", "15 units", "20 units"],
     "A", "OSC", "hard",
     "Original area = \\(xy\\). Condition 1: \\((x - 5)(y + 3) = xy - 9 \\implies 3x - 5y = 6\\). Condition 2: \\((x + 3)(y + 2) = xy + 67 \\implies 2x + 3y = 61\\). Multiply first by 3: \\(9x - 15y = 18\\). Multiply second by 5: \\(10x + 15y = 305\\). Adding: \\(19x = 323 \\implies x = 17\\) units."),

    # 33
    ("From the rectangle area problem above, find the breadth.",
     ["9 units", "17 units", "12 units", "7 units"],
     "A", "OSC", "easy",
     "\\(3(17) - 5y = 6 \\implies 51 - 5y = 6 \\implies 5y = 45 \\implies y = 9\\) units."),

    # 34
    ("In a \\(\\Delta ABC\\), \\(\\angle C = 3\\angle B = 2(\\angle A + \\angle B)\\). Find the measure of \\(\\angle C\\).",
     ["\\(120^\\circ\\)", "\\(40^\\circ\\)", "\\(20^\\circ\\)", "\\(90^\\circ\\)"],
     "A", "OSC", "hard",
     "Let \\(\\angle B = y\\). Then \\(\\angle C = 3y\\). From \\(3\\angle B = 2(\\angle A + \\angle B) \\implies 3y = 2\\angle A + 2y \\implies \\angle A = 0.5y\\). Sum of angles: \\(\\angle A + \\angle B + \\angle C = 180^\\circ \\implies 0.5y + y + 3y = 180^\\circ \\implies 4.5y = 180^\\circ \\implies y = 40^\\circ\\). Thus \\(\\angle C = 3(40^\\circ) = 120^\\circ\\)."),

    # 35
    ("From the triangle problem above, what is \\(\\angle A\\)?",
     ["\\(20^\\circ\\)", "\\(40^\\circ\\)", "\\(30^\\circ\\)", "\\(50^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\angle A = 0.5(40^\\circ) = 20^\\circ\\)."),

    # 36
    ("From the triangle problem above, what is \\(\\angle B\\)?",
     ["\\(40^\\circ\\)", "\\(20^\\circ\\)", "\\(60^\\circ\\)", "\\(50^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\angle B = 40^\\circ\\)."),

    # 37
    ("The sum of the digits of a two-digit number is 12. If the digits are interchanged, the new number formed is 18 greater than the original number. Find the original number.",
     ["57", "75", "48", "39"],
     "A", "OSC", "medium",
     "\\(x + y = 12\\). Reversing: \\(10y + x = (10x + y) + 18 \\implies 9y - 9x = 18 \\implies y - x = 2\\). Adding: \\(2y = 14 \\implies y = 7\\), and \\(x = 5\\). Original number is 57."),

    # 38
    ("A lending library has a fixed charge for the first three days and an additional charge for each day thereafter. Saritha paid Rs 27 for a book kept for seven days, while Susy paid Rs 21 for the book she kept for five days. Find the fixed charge.",
     ["Rs 15", "Rs 3", "Rs 12", "Rs 18"],
     "A", "OSC", "medium",
     "Let fixed charge (for 3 days) be \\(x\\) and daily charge be \\(y\\). Saritha kept 7 days (3 + 4 days): \\(x + 4y = 27\\). Susy kept 5 days (3 + 2 days): \\(x + 2y = 21\\). Subtracting: \\(2y = 6 \\implies y = 3\\). Then \\(x = 21 - 2(3) = 15\\) Rs."),

    # 39
    ("From the library problem above, what is the charge for each extra day?",
     ["Rs 3", "Rs 5", "Rs 4", "Rs 2"],
     "A", "OSC", "easy",
     "\\(y = 3\\) Rs per extra day."),

    # 40
    ("In a competitive exam, 3 marks are awarded for each correct answer and 1 mark is deducted for each wrong answer. Yash scored 40 marks. If 4 marks were awarded for each correct answer and 2 marks deducted for each incorrect answer, Yash would have scored 50 marks. How many questions were there in the test (assuming all attempted)?",
     ["20 questions", "25 questions", "15 questions", "30 questions"],
     "A", "OSC", "hard",
     "Let correct answers be \\(x\\) and incorrect be \\(y\\). \\(3x - y = 40\\) and \\(4x - 2y = 50 \\implies 2x - y = 25\\). Subtracting: \\(x = 15\\). Then \\(y = 3(15) - 40 = 5\\). Total questions = \\(x + y = 15 + 5 = 20\\).")
]

# 30 PRACTICE (41-70)
practice_data = [
    # 41
    ("The sum of two numbers is 103. If the greater number is divided by the smaller number, the quotient is 2 and the remainder is 19. Find the greater number.",
     ["75", "28", "80", "70"],
     "A", "OSC", "medium",
     "\\(x + y = 103\\). Division algorithm: \\(x = 2y + 19 \\implies x - 2y = 19\\). Subtracting: \\(3y = 84 \\implies y = 28\\). Then \\(x = 103 - 28 = 75\\)."),

    # 42
    ("From the previous problem, what is the smaller number?",
     ["28", "75", "25", "30"],
     "A", "OSC", "easy",
     "Smaller number is \\(y = 28\\)."),

    # 43
    ("Sum of two numbers is 85. If their difference is 15, find the numbers.",
     ["50 and 35", "55 and 30", "60 and 25", "45 and 40"],
     "A", "OSC", "easy",
     "\\(x + y = 85\\) and \\(x - y = 15\\). Adding: \\(2x = 100 \\implies x = 50\\). Then \\(y = 35\\)."),

    # 44
    ("A father is 26 years older than his son. In 3 years, his age will be 3 times his son's age. Find the son's present age.",
     ["10 years", "12 years", "8 years", "15 years"],
     "A", "OSC", "medium",
     "\\(x - y = 26\\). In 3 years: \\(x + 3 = 3(y + 3) \\implies x + 3 = 3y + 9 \\implies x - 3y = 6\\). Subtracting: \\(2y = 20 \\implies y = 10\\)."),

    # 45
    ("From the previous question, what is the father's present age?",
     ["36 years", "40 years", "38 years", "42 years"],
     "A", "OSC", "easy",
     "\\(x = 10 + 26 = 36\\) years."),

    # 46
    ("Ten years ago, a mother was 4 times as old as her daughter. Ten years hence, she will be twice as old. Find the daughter's present age.",
     ["20 years", "15 years", "25 years", "18 years"],
     "A", "OSC", "medium",
     "\\(x - 10 = 4(y - 10) \\implies x - 4y = -30\\). \\(x + 10 = 2(y + 10) \\implies x - 2y = 10\\). Subtracting: \\(2y = 40 \\implies y = 20\\)."),

    # 47
    ("From the previous problem, find the mother's present age.",
     ["50 years", "60 years", "45 years", "55 years"],
     "A", "OSC", "easy",
     "\\(x = 2(20) + 10 = 50\\) years."),

    # 48
    ("In an examination, a student scores 4 marks for every correct answer and loses 1 mark for every wrong answer. If he attempts 60 questions and gets 130 marks, how many questions did he answer correctly?",
     ["38", "40", "36", "42"],
     "A", "OSC", "medium",
     "\\(x + y = 60\\) and \\(4x - y = 130\\). Adding: \\(5x = 190 \\implies x = 38\\)."),

    # 49
    ("From the previous question, how many questions did the student answer incorrectly?",
     ["22", "20", "24", "18"],
     "A", "OSC", "easy",
     "\\(y = 60 - 38 = 22\\)."),

    # 50
    ("The perimeter of a rectangular garden is 36 m. The length is 4 m more than its width. Find the length.",
     ["20 m", "16 m", "18 m", "22 m"],
     "A", "OSC", "easy",
     "\\(2(l + w) = 36 \\implies l + w = 18\\). Given \\(l - w = 4\\). Adding gives \\(2l = 22 \\implies l = 11\\text{ (wait: if half perimeter is 36: } l+w=36 \\implies 2l=40 \\implies l=20\\)). If perimeter = 36 m, half perimeter is 18 m. If half perimeter is 36 m, then \\(l+w=36, l-w=4 \\implies l=20\\) m."),

    # 51
    ("Half the perimeter of a rectangular garden is 36 m. Its length is 4 m more than its width. Find the width.",
     ["16 m", "20 m", "14 m", "18 m"],
     "A", "OSC", "easy",
     "\\(l + w = 36\\) and \\(l = 20\\) m \\(\\implies w = 36 - 20 = 16\\) m."),

    # 52
    ("The sum of the digits of a two-digit number is 8. If 18 is subtracted from the number, the digits interchange their places. Find the number.",
     ["53", "35", "62", "71"],
     "A", "OSC", "medium",
     "\\(x + y = 8\\). Condition: \\((10x + y) - 18 = 10y + x \\implies 9x - 9y = 18 \\implies x - y = 2\\). Adding: \\(2x = 10 \\implies x = 5, y = 3\\). Number is 53."),

    # 53
    ("A boat travels 16 km upstream and 24 km downstream in 6 hours. Also, it travels 12 km upstream and 36 km downstream in the same time. Find the speed of the boat in still water.",
     ["8 km/h", "4 km/h", "6 km/h", "10 km/h"],
     "A", "OSC", "hard",
     "Let \\(u = \\frac{1}{x-y}, v = \\frac{1}{x+y}\\). \\(16u + 24v = 6\\) and \\(12u + 36v = 6\\). Solving gives \\(u = 1/4, v = 1/12\\). Thus \\(x - y = 4\\) and \\(x + y = 12\\). Adding gives \\(2x = 16 \\implies x = 8\\) km/h."),

    # 54
    ("From the boat problem above, find the speed of the stream.",
     ["4 km/h", "2 km/h", "3 km/h", "5 km/h"],
     "A", "OSC", "easy",
     "\\(y = 12 - 8 = 4\\) km/h."),

    # 55
    ("The cost of 5 pens and 6 pencils is Rs 45. The cost of 4 pens and 3 pencils is Rs 30. Find the cost of 1 pen.",
     ["Rs 5", "Rs 4", "Rs 6", "Rs 3"],
     "A", "OSC", "medium",
     "\\(5x + 6y = 45\\) and \\(4x + 3y = 30\\). Multiply second by 2: \\(8x + 6y = 60\\). Subtracting: \\(3x = 15 \\implies x = 5\\) Rs."),

    # 56
    ("From the previous question, find the cost of 1 pencil.",
     ["Rs 3.33 (or Rs 10/3)", "Rs 2.5", "Rs 4", "Rs 2"],
     "A", "OSC", "easy",
     "\\(4(5) + 3y = 30 \\implies 20 + 3y = 30 \\implies 3y = 10 \\implies y = \\frac{10}{3}\\) Rs."),

    # 57
    ("Two supplementary angles differ by \\(40^\\circ\\). Find the smaller angle.",
     ["\\(70^\\circ\\)", "\\(110^\\circ\\)", "\\(60^\\circ\\)", "\\(80^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(x + y = 180\\) and \\(x - y = 40\\). Subtracting: \\(2y = 140 \\implies y = 70^\\circ\\)."),

    # 58
    ("From the previous problem, find the larger angle.",
     ["\\(110^\\circ\\)", "\\(120^\\circ\\)", "\\(100^\\circ\\)", "\\(70^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(x = 180^\\circ - 70^\\circ = 110^\\circ\\)."),

    # 59
    ("The difference between two numbers is 26 and one number is three times the other. Find the smaller number.",
     ["13", "39", "12", "14"],
     "A", "OSC", "easy",
     "\\(x - y = 26\\) and \\(x = 3y\\). Substitute: \\(3y - y = 26 \\implies 2y = 26 \\implies y = 13\\)."),

    # 60
    ("From the previous problem, find the greater number.",
     ["39", "26", "52", "48"],
     "A", "OSC", "easy",
     "\\(x = 3(13) = 39\\)."),

    # 61
    ("If 2 is added to both numerator and denominator of a fraction, it becomes \\(\\frac{9}{11}\\). If 3 is added to both, it becomes \\(\\frac{5}{6}\\). Find the numerator.",
     ["7", "9", "5", "8"],
     "A", "OSC", "medium",
     "\\(\\frac{x+2}{y+2} = \\frac{9}{11} \\implies 11x - 9y = -4\\). \\(\\frac{x+3}{y+3} = \\frac{5}{6} \\implies 6x - 5y = -3\\). Solving gives \\(x = 7, y = 9\\)."),

    # 62
    ("From the previous fraction problem, find the denominator.",
     ["9", "11", "7", "13"],
     "A", "OSC", "easy",
     "Denominator is \\(y = 9\\). The fraction is \\(7/9\\)."),

    # 63
    ("A train covered a certain distance at a uniform speed. If the train had been 10 km/h faster, it would have taken 2 hours less than the scheduled time. If the train were slower by 10 km/h, it would have taken 3 hours more. Find the distance.",
     ["600 km", "500 km", "700 km", "400 km"],
     "A", "OSC", "hard",
     "Let speed be \\(s\\) and time be \\(t\\). Distance \\(d = st\\). \\((s + 10)(t - 2) = st \\implies -2s + 10t = 20\\). \\((s - 10)(t + 3) = st \\implies 3s - 10t = 30\\). Adding gives \\(s = 50\\) km/h. Then \\(10t = 20 + 2(50) = 120 \\implies t = 12\\) h. Distance = \\(50 \\times 12 = 600\\) km."),

    # 64
    ("From the train problem above, find the uniform speed of the train.",
     ["50 km/h", "60 km/h", "40 km/h", "55 km/h"],
     "A", "OSC", "easy",
     "Speed is \\(s = 50\\) km/h."),

    # 65
    ("A person invested Rs 10,000 in two schemes A and B yielding 8% and 10% annual simple interest respectively. If total annual interest received is Rs 920, how much was invested in scheme B?",
     ["Rs 6000", "Rs 4000", "Rs 5000", "Rs 7000"],
     "A", "OSC", "medium",
     "\\(x + y = 10000\\). Interest: \\(0.08x + 0.10y = 920 \\implies 8x + 10y = 92000\\). Subtract \\(8x + 8y = 80000\\): \\(2y = 12000 \\implies y = 6000\\) Rs."),

    # 66
    ("From the previous investment problem, how much was invested in scheme A?",
     ["Rs 4000", "Rs 6000", "Rs 5000", "Rs 3000"],
     "A", "OSC", "easy",
     "\\(x = 10000 - 6000 = 4000\\) Rs."),

    # 67
    ("Two numbers are in the ratio \\(5:6\\). If 8 is subtracted from each, the ratio becomes \\(4:5\\). Find the smaller number.",
     ["40", "48", "35", "45"],
     "A", "OSC", "easy",
     "Let numbers be \\(5k\\) and \\(6k\\). \\(\\frac{5k - 8}{6k - 8} = \\frac{4}{5} \\implies 25k - 40 = 24k - 32 \\implies k = 8\\). Smaller number = \\(5(8) = 40\\)."),

    # 68
    ("From the previous problem, find the larger number.",
     ["48", "40", "56", "50"],
     "A", "OSC", "easy",
     "Larger number = \\(6(8) = 48\\)."),

    # 69
    ("The sum of the digits of a two-digit number is 7. If the digits are reversed, the new number is 9 less than the original. Find the original number.",
     ["43", "34", "52", "61"],
     "A", "OSC", "easy",
     "\\(x + y = 7\\) and \\((10x + y) - (10y + x) = 9 \\implies 9(x - y) = 9 \\implies x - y = 1\\). Adding gives \\(2x = 8 \\implies x = 4\\), so \\(y = 3\\). Number is 43."),

    # 70
    ("If the perimeter of a rectangle is 28 cm and its diagonal is 10 cm, find its length.",
     ["8 cm", "6 cm", "7 cm", "9 cm"],
     "A", "OSC", "medium",
     "\\(2(l + w) = 28 \\implies l + w = 14\\). Diagonal \\(l^2 + w^2 = 10^2 = 100\\). Since \\((l+w)^2 = l^2 + w^2 + 2lw \\implies 196 = 100 + 2lw \\implies 2lw = 96 \\implies lw = 48\\). Numbers with sum 14 and product 48 are 8 and 6. Length = 8 cm.")
]

# 12 MOCK (71-82)
mock_data = [
    # 71
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0f172a" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Step-by-Step Word Problem Modeling</text>
  <text x="170" y="80" fill="#f8fafc" font-size="11" text-anchor="middle">1. Identify unknowns and assign variables (x, y)</text>
  <text x="170" y="105" fill="#4ade80" font-size="11" text-anchor="middle">2. Translate given facts into two linear equations</text>
</svg>
</div>
What is the first and most critical step in solving an algebraic word problem?""",
     ["Carefully identifying the unknown quantities and defining variables (such as x and y) to represent them",
      "Guessing the numerical answer by trial and error",
      "Dividing all numbers by 10",
      "Drawing a circle on graph paper"],
     "A", "OSC", "easy",
     "The foundation of algebraic modeling is clearly identifying the quantities to be found and defining variables like \\(x\\) and \\(y\\) to represent them with proper units."),

    # 72
    ("The sum of two numbers is 15 and their difference is 3. Find the numbers.",
     ["9 and 6", "10 and 5", "8 and 7", "11 and 4"],
     "A", "OSC", "easy",
     "\\(x + y = 15, x - y = 3 \\implies 2x = 18 \\implies x = 9, y = 6\\)."),

    # 73
    ("A number consists of two digits whose sum is 9. If the number is 27 greater than the reverse, find the number.",
     ["63", "36", "72", "54"],
     "A", "OSC", "easy",
     "\\(x + y = 9\\) and \\(9(x - y) = 27 \\implies x - y = 3\\). Adding: \\(2x = 12 \\implies x = 6, y = 3\\). Number is 63."),

    # 74
    ("In a rectangle, length is 3 cm more than breadth and perimeter is 22 cm. Find breadth.",
     ["4 cm", "7 cm", "5 cm", "3 cm"],
     "A", "OSC", "easy",
     "\\(2(l + b) = 22 \\implies l + b = 11\\). With \\(l - b = 3\\), subtracting gives \\(2b = 8 \\implies b = 4\\) cm."),

    # 75
    ("From the previous question, find the length.",
     ["7 cm", "4 cm", "8 cm", "6 cm"],
     "A", "OSC", "easy",
     "\\(l = 4 + 3 = 7\\) cm."),

    # 76
    ("If 5 pencils and 7 pens together cost Rs 50, whereas 7 pencils and 5 pens together cost Rs 46, find the cost of 1 pencil.",
     ["Rs 3", "Rs 5", "Rs 4", "Rs 2"],
     "A", "OSC", "medium",
     "\\(5x + 7y = 50\\) and \\(7x + 5y = 46\\). Adding: \\(12x + 12y = 96 \\implies x + y = 8\\). Subtracting: \\(2x - 2y = -4 \\implies x - y = -2\\). Adding gives \\(2x = 6 \\implies x = 3\\) Rs."),

    # 77
    ("From the previous problem, what is the cost of 1 pen?",
     ["Rs 5", "Rs 3", "Rs 6", "Rs 4"],
     "A", "OSC", "easy",
     "\\(y = 8 - 3 = 5\\) Rs."),

    # 78
    ("If upstream speed is \\(x - y = 6\\) km/h and downstream speed is \\(x + y = 10\\) km/h, find boat speed \\(x\\).",
     ["8 km/h", "2 km/h", "6 km/h", "4 km/h"],
     "A", "OSC", "easy",
     "\\(2x = 16 \\implies x = 8\\) km/h."),

    # 79
    ("From the previous question, find stream speed \\(y\\).",
     ["2 km/h", "4 km/h", "1 km/h", "3 km/h"],
     "A", "OSC", "easy",
     "\\(y = 10 - 8 = 2\\) km/h."),

    # 80
    ("Two complementary angles differ by \\(10^\\circ\\). What are the angles?",
     ["\\(50^\\circ\\) and \\(40^\\circ\\)",
      "\\(55^\\circ\\) and \\(45^\\circ\\)",
      "\\(60^\\circ\\) and \\(50^\\circ\\)",
      "\\(45^\\circ\\) and \\(35^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(x + y = 90\\) and \\(x - y = 10 \\implies 2x = 100 \\implies x = 50^\\circ, y = 40^\\circ\\)."),

    # 81
    ("Two supplementary angles differ by \\(20^\\circ\\). What is the smaller angle?",
     ["\\(80^\\circ\\)", "\\(100^\\circ\\)", "\\(70^\\circ\\)", "\\(90^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(x + y = 180\\) and \\(x - y = 20 \\implies 2y = 160 \\implies y = 80^\\circ\\)."),

    # 82
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0b132b" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1c2541" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Verification of Applied Solutions</text>
  <text x="170" y="80" fill="#f8fafc" font-size="11" text-anchor="middle">Always check answers against practical reality!</text>
  <text x="170" y="105" fill="#4ade80" font-size="11" text-anchor="middle">Ages, lengths, speeds must strictly be positive real numbers</text>
</svg>
</div>
Why must physical quantities like age, length, and speed be verified for positivity after solving?""",
     ["Because negative lengths, negative ages, or negative speeds have no physical reality in word problems",
      "Because negative numbers cannot be factored",
      "Because denominators become zero",
      "Because equations become non-linear"],
     "A", "OSC", "easy",
     "Physical quantities such as lengths, times, speeds, and ages are intrinsically non-negative in the real world. Any extraneous or negative roots from algebraic equations must be rejected.")
]

all_q_15 = build_topic_questions(TOPIC_CODE, exam_data, practice_data, mock_data)
out_15 = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch1_t5.json")
with open(out_15, "w", encoding="utf-8") as f:
    json.dump(all_q_15, f, indent=2, ensure_ascii=False)
print(f"Generated {len(all_q_15)} questions for {TOPIC_CODE} -> {out_15}")
