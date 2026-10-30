# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 3: Arithmetic Progression - Topic 3.4: Applied Word Problems on AP (MH-10-MTH1-3-3.4)
Total: 82 Canonical Questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# TOPIC 3.4: Applied Word Problems on AP
t34_exam = [
    # 1
    ("On 1st Jan 2016, Sanika decides to save ₹10, ₹11 on second day, ₹12 on third day and so on. If she decides to save like this, what would be her total savings on 31st Dec 2016?",
     ["₹70,455", "\\(₹70,000\\)", "\\(₹69,850\\)", "\\(₹71,200\\)"],
     "A", "OSC", "medium",
     "The year 2016 is a leap year, having \\(n = 366\\) days. Savings form an AP: \\(a = 10, d = 1, n = 366\\). \\(S_{366} = \\frac{366}{2}[2(10) + 365(1)] = 183(20 + 365) = 183 \\times 385 = 70,455\\)."),

    # 2
    ("A man borrows ₹8,000 and agrees to repay with total interest of ₹1,360 in 12 monthly installments. Each installment is less than the preceding one by ₹40. Find the amount of the first installment.",
     ["₹1,000", "\\(₹960\\)", "\\(₹1,040\\)", "\\(₹1,080\\)"],
     "A", "OSC", "hard",
     "Total amount to repay \\(= 8000 + 1360 = 9360\\). \\(n = 12, d = -40\\). \\(S_{12} = \\frac{12}{2}[2a + 11(-40)] = 6(2a - 440) = 9360 \\implies 2a - 440 = 1560 \\implies 2a = 2000 \\implies a = 1000\\)."),

    # 3
    ("In the loan repayment problem where a man repays ₹9,360 in 12 installments with \\(a = 1000\\) and \\(d = -40\\), what is the amount of the last (\\(12^{\\text{th}}\\) installment)?",
     ["₹560", "\\(₹520\\)", "\\(₹600\\)", "\\(₹480\\)"],
     "A", "OSC", "easy",
     "Last installment \\(t_{12} = a + 11d = 1000 + 11(-40) = 1000 - 440 = 560\\)."),

    # 4
    ("Sachin invested in a National Saving Certificate scheme: ₹5,000 in 1st year, ₹7,000 in 2nd year, ₹9,000 in 3rd year and so on. Find the total amount he invested in 12 years.",
     ["₹1,92,000", "\\(₹1,80,000\\)", "\\(₹1,96,000\\)", "\\(₹2,04,000\\)"],
     "A", "OSC", "medium",
     "\\(a = 5000, d = 2000, n = 12\\). \\(S_{12} = \\frac{12}{2}[2(5000) + 11(2000)] = 6[10000 + 22000] = 6 \\times 32000 = 1,92,000\\)."),

    # 5
    ("There is an auditorium with 27 rows of seats: 20 seats in the 1st row, 22 in the 2nd row, 24 in the 3rd row, and so on. How many seats are there in the \\(15^{\\text{th}}\\) row?",
     ["\\(48\\) seats", "\\(50\\) seats", "\\(46\\) seats", "\\(52\\) seats"],
     "A", "OSC", "easy",
     "\\(a = 20, d = 2\\). \\(t_{15} = a + 14d = 20 + 14(2) = 20 + 28 = 48\\)."),

    # 6
    ("In the auditorium with 27 rows (20 seats in 1st row, increasing by 2 in each subsequent row), find the total number of seats in the auditorium.",
     ["\\(1242\\) seats", "\\(1200\\) seats", "\\(1260\\) seats", "\\(1188\\) seats"],
     "A", "OSC", "medium",
     "\\(S_{27} = \\frac{27}{2}[2(20) + 26(2)] = \\frac{27}{2}[40 + 52] = \\frac{27}{2} \\times 92 = 27 \\times 46 = 1242\\)."),

    # 7
    ("Kargil's temperatures from Monday to Saturday formed an AP. The sum of temperatures of Monday and Saturday was \\(5^\\circ\\text{C}\\) more than the sum of temperatures of Tuesday and Saturday. If Wednesday's temperature was \\(-30^\\circ\\text{C}\\), find Monday's temperature.",
     ["\\(-20^\\circ\\text{C}\\)", "\\(-25^\\circ\\text{C}\\)", "\\(-15^\\circ\\text{C}\\)", "\\(-35^\\circ\\text{C}\\)"],
     "A", "OSC", "hard",
     "Let temperatures be \\(a, a+d, a+2d, a+3d, a+4d, a+5d\\). Given \\((a + a + 5d) = (a + d + a + 5d) + 5 \\implies 2a + 5d = 2a + 6d + 5 \\implies d = -5^\\circ\\text{C}\\). Wednesday is \\(a + 2d = -30 \\implies a + 2(-5) = -30 \\implies a - 10 = -30 \\implies a = -20^\\circ\\text{C}\\)."),

    # 8
    ("In the Kargil temperature problem (Monday = \\(-20^\\circ\\text{C}\\), \\(d = -5^\\circ\\text{C}\\)), what was Saturday's temperature?",
     ["\\(-45^\\circ\\text{C}\\)", "\\(-40^\\circ\\text{C}\\)", "\\(-50^\\circ\\text{C}\\)", "\\(-35^\\circ\\text{C}\\)"],
     "A", "OSC", "easy",
     "Saturday is the \\(6^{\\text{th}}\\) day: \\(t_6 = a + 5d = -20 + 5(-5) = -20 - 25 = -45^\\circ\\text{C}\\)."),

    # 9
    ("On World Environment Day, trees were planted on a triangular ground: 1 tree in 1st row, 2 in 2nd row, 3 in 3rd row, up to 25 rows. Find total trees planted.",
     ["\\(325\\)", "\\(350\\)", "\\(300\\)", "\\(315\\)"],
     "A", "OSC", "easy",
     "Sum of natural numbers from 1 to 25: \\(S_{25} = \\frac{25 \\times 26}{2} = 25 \\times 13 = 325\\)."),

    # 10
    ("A manufacturer of TV sets produced 600 sets in the third year and 700 sets in the seventh year. Assuming that the production increases uniformly by a fixed number every year, find the production in the 1st year.",
     ["\\(550\\) sets", "\\(525\\) sets", "\\(575\\) sets", "\\(500\\) sets"],
     "A", "OSC", "medium",
     "\\(t_3 = a + 2d = 600\\) and \\(t_7 = a + 6d = 700\\). Subtracting gives \\(4d = 100 \\implies d = 25\\). Thus \\(a = 600 - 2(25) = 550\\)."),

    # 11
    ("For the TV manufacturer with initial production 550 sets and annual increase of 25 sets, find the production in the \\(10^{\\text{th}}\\) year.",
     ["\\(775\\) sets", "\\(750\\) sets", "\\(800\\) sets", "\\(825\\) sets"],
     "A", "OSC", "easy",
     "\\(t_{10} = a + 9d = 550 + 9(25) = 550 + 225 = 775\\)."),

    # 12
    ("Find the total production of the TV manufacturer in the first \\(7\\) years.",
     ["\\(4375\\) sets", "\\(4250\\) sets", "\\(4500\\) sets", "\\(4125\\) sets"],
     "A", "OSC", "medium",
     "\\(S_7 = \\frac{7}{2}(t_1 + t_7) = \\frac{7}{2}(550 + 700) = \\frac{7}{2}(1250) = 7 \\times 625 = 4375\\)."),

    # 13
    ("A contract on construction job specifies a penalty for delay of completion beyond a certain date as follows: ₹200 for the first day, ₹250 for the second day, ₹300 for the third day, etc. How much penalty must the contractor pay if he has delayed the work by 30 days?",
     ["₹27,750", "\\(₹28,000\\)", "\\(₹26,500\\)", "\\(₹27,500\\)"],
     "A", "OSC", "hard",
     "\\(a = 200, d = 50, n = 30\\). \\(S_{30} = \\frac{30}{2}[2(200) + 29(50)] = 15[400 + 1450] = 15(1850) = 27,750\\)."),

    # 14
    ("A sum of ₹700 is to be used to give seven cash prizes to students of a school for their overall academic performance. If each prize is ₹20 less than its preceding prize, find the value of the first prize.",
     ["₹160", "\\(₹140\\)", "\\(₹150\\)", "\\(₹180\\)"],
     "A", "OSC", "medium",
     "\\(n = 7, d = -20, S_7 = 700\\). \\(S_7 = \\frac{7}{2}[2a + 6(-20)] = 700 \\implies \\frac{7}{2}[2a - 120] = 700 \\implies 2a - 120 = 200 \\implies 2a = 320 \\implies a = 160\\)."),

    # 15
    ("In a school, students thought of planting trees in and around the school to reduce air pollution. Each class was to plant trees equal to the class number (Class 1 plants 1 tree, Class 2 plants 2, ..., Class 12 plants 12). If there are 3 sections of each class, how many trees were planted by the students?",
     ["\\(234\\) trees", "\\(216\\) trees", "\\(240\\) trees", "\\(228\\) trees"],
     "A", "OSC", "medium",
     "Trees planted by one section of classes 1 to 12 \\(= 1 + 2 + \\dots + 12 = \\frac{12 \\times 13}{2} = 78\\). Since each class has 3 sections: \\(3 \\times 78 = 234\\)."),

    # 16
    ("A spiral is made up of successive semicircles, with centres alternately at \\(A\\) and \\(B\\), starting with centre at \\(A\\), of radii \\(0.5\\text{ cm}, 1.0\\text{ cm}, 1.5\\text{ cm}, 2.0\\text{ cm}, \\dots\\) What is the total length of such a spiral made up of thirteen consecutive semicircles? (Take \\(\\pi = 22/7\\))",
     ["\\(143\\text{ cm}\\)", "\\(140\\text{ cm}\\)", "\\(132\\text{ cm}\\)", "\\(154\\text{ cm}\\)"],
     "A", "OSC", "hard",
     "Length of semicircle \\(= \\pi r\\). Lengths: \\(0.5\\pi, 1.0\\pi, 1.5\\pi, \\dots\\) This is an AP with \\(a = 0.5\\pi, d = 0.5\\pi, n = 13\\). \\(S_{13} = \\frac{13}{2}[2(0.5\\pi) + 12(0.5\\pi)] = \\frac{13}{2}(7\\pi) = \\frac{13}{2} \\times 7 \\times \\frac{22}{7} = 143\\text{ cm}\\)."),

    # 17
    ("200 logs are stacked in the following manner: 20 logs in the bottom row, 19 in the next row, 18 in the row next to it and so on. In how many rows are the 200 logs placed, and how many logs are in the top row?",
     ["\\(16\\) rows, \\(5\\) logs in top row", "\\(25\\) rows, \\(-4\\) logs in top row", "\\(15\\) rows, \\(6\\) logs in top row", "\\(20\\) rows, \\(1\\) log in top row"],
     "A", "OSC", "hard",
     "\\(a = 20, d = -1, S_n = 200\\). \\(200 = \\frac{n}{2}[40 + (n - 1)(-1)] \\implies 400 = n(41 - n) \\implies n^2 - 41n + 400 = 0 \\implies (n - 16)(n - 25) = 0\\). For \\(n = 25\\), \\(t_{25} = 20 + 24(-1) = -4\\) (impossible). Thus \\(n = 16\\), and top row has \\(t_{16} = 20 + 15(-1) = 5\\) logs."),

    # 18
    ("In a potato race, a bucket is placed at the starting point, which is 5 m from the first potato, and the other potatoes are placed 3 m apart in a straight line. There are 10 potatoes in the line. A competitor starts from the bucket, picks up the nearest potato, runs back with it, drops it in the bucket, and runs back for the next potato. What is the total distance the competitor has to run?",
     ["\\(370\\text{ m}\\)", "\\(350\\text{ m}\\)", "\\(360\\text{ m}\\)", "\\(380\\text{ m}\\)"],
     "A", "OSC", "hard",
     "Distances run for potatoes: 1st potato \\(= 2 \\times 5 = 10\\text{ m}\\); 2nd potato \\(= 2 \\times (5 + 3) = 16\\text{ m}\\); 3rd potato \\(= 2 \\times (5 + 6) = 22\\text{ m}\\). This forms an AP with \\(a = 10, d = 6, n = 10\\). \\(S_{10} = \\frac{10}{2}[2(10) + 9(6)] = 5[20 + 54] = 5 \\times 74 = 370\\text{ m}\\)."),

    # 19
    ("A man saved ₹16,500 in ten years. In each year after the first year he saved ₹100 more than he did in the preceding year. How much did he save in the first year?",
     ["₹1,200", "\\(₹1,100\\)", "\\(₹1,300\\)", "\\(₹1,000\\)"],
     "A", "OSC", "medium",
     "\\(n = 10, d = 100, S_{10} = 16500\\). \\(S_{10} = 5[2a + 9(100)] = 16500 \\implies 2a + 900 = 3300 \\implies 2a = 2400 \\implies a = 1200\\)."),

    # 20
    ("A car travels 20 km in the first hour, 22 km in the second hour, 24 km in the third hour, and so on. How far will it travel in 10 hours?",
     ["\\(290\\text{ km}\\)", "\\(280\\text{ km}\\)", "\\(300\\text{ km}\\)", "\\(310\\text{ km}\\)"],
     "A", "OSC", "easy",
     "\\(a = 20, d = 2, n = 10\\). \\(S_{10} = \\frac{10}{2}[2(20) + 9(2)] = 5[40 + 18] = 5(58) = 290\\text{ km}\\)."),

    # 21
    ("A person pays ₹975 in monthly installments, each installment being less than the former by ₹5. The amount of the first installment is ₹100. In how many installments will the entire amount be paid?",
     ["\\(15\\) installments", "\\(25\\) installments", "\\(13\\) installments", "\\(10\\) installments"],
     "A", "OSC", "hard",
     "\\(S_n = 975, a = 100, d = -5\\). \\(975 = \\frac{n}{2}[200 + (n - 1)(-5)] \\implies 1950 = n(205 - 5n) \\implies 5n^2 - 205n + 1950 = 0 \\implies n^2 - 41n + 390 = 0 \\implies (n - 15)(n - 26) = 0\\). For \\(n = 26\\), installment becomes negative (\\(100 - 125 = -25\\)), so \\(n = 15\\)."),

    # 22
    ("A club has 20 members. On the first day of a fundraiser, each member donates ₹50. Every subsequent day, each member donates ₹10 more than the previous day. How much total money is raised in 7 days by all members?",
     ["₹11,200", "\\(₹10,500\\)", "\\(₹12,000\\)", "\\(₹11,500\\)"],
     "A", "OSC", "medium",
     "Daily donations per member: \\(a = 50, d = 10, n = 7\\). One member donates \\(S_7 = \\frac{7}{2}[100 + 6(10)] = \\frac{7}{2}(160) = 560\\). All 20 members donate \\(20 \\times 560 = 11,200\\)."),

    # 23
    ("A worker’s salary increases by ₹500 every year. If his salary in the first year was ₹15,000, what will be his salary in the \\(15^{\\text{th}}\\) year?",
     ["₹22,000", "\\(₹22,500\\)", "\\(₹21,500\\)", "\\(₹23,000\\)"],
     "A", "OSC", "easy",
     "\\(a = 15000, d = 500, n = 15\\). \\(t_{15} = 15000 + 14(500) = 15000 + 7000 = 22,000\\)."),

    # 24
    ("What are the total earnings of the worker in Question 23 over the 15-year period?",
     ["₹2,77,500", "\\(₹2,80,000\\)", "\\(₹2,75,000\\)", "\\(₹2,85,000\\)"],
     "A", "OSC", "medium",
     "\\(S_{15} = \\frac{15}{2}(t_1 + t_{15}) = \\frac{15}{2}(15000 + 22000) = \\frac{15}{2}(37000) = 15 \\times 18500 = 2,77,500\\)."),

    # 25
    ("A runner starts training by running 2 km on day 1, and increases his distance by 0.5 km each day. On which day will he run 10 km?",
     ["Day \\(17\\)", "Day \\(16\\)", "Day \\(18\\)", "Day \\(15\\)"],
     "A", "OSC", "easy",
     "\\(a = 2, d = 0.5, t_n = 10\\). \\(10 = 2 + (n - 1)(0.5) \\implies 8 = 0.5(n - 1) \\implies n - 1 = 16 \\implies n = 17\\)."),

    # 26
    ("How many total kilometers will the runner in Question 25 have run in those 17 days?",
     ["\\(102\\text{ km}\\)", "\\(100\\text{ km}\\)", "\\(104\\text{ km}\\)", "\\(98\\text{ km}\\)"],
     "A", "OSC", "easy",
     "\\(S_{17} = \\frac{17}{2}(a + t_{17}) = \\frac{17}{2}(2 + 10) = \\frac{17}{2}(12) = 17 \\times 6 = 102\\text{ km}\\)."),

    # 27
    ("A book has 300 pages. A student reads 15 pages on the first day and increases his reading rate by 5 pages every day. In how many days will he finish reading the book?",
     ["\\(8\\) days", "\\(7\\) days", "\\(9\\) days", "\\(10\\) days"],
     "A", "OSC", "hard",
     "\\(a = 15, d = 5, S_n \\ge 300\\). \\(\\frac{n}{2}[30 + (n - 1)5] = 300 \\implies n(5n + 25) = 600 \\implies 5n^2 + 25n - 600 = 0 \\implies n^2 + 5n - 120 = 0\\). Using quadratic formula: \\(n = \\frac{-5 \\pm \\sqrt{25 + 480}}{2} = \\frac{-5 + \\sqrt{505}}{2} \\approx \\frac{-5 + 22.47}{2} = 8.73\\). In 8 days he reads \\(S_8 = 4(30 + 35) = 260\\) pages, so he finishes on the 9th day (or after 8 full days and part of day 9). If the problem specifies exactly 300 pages: let's adjust \\(a = 15, d = 5, S_n = 300\\) to exact integers: \\(a = 10, d = 5, S_n = 325 \\implies n(5n + 15) = 650 \\implies n^2 + 3n - 130 = 0 \\implies (n + 13)(n - 10) = 0\\). Let's use \\(a = 10, d = 5, S_n = 325\\)."),
]
# Clean replacement of question 27
t34_exam[-1] = (
    "A book has 325 pages. A student reads 10 pages on the first day and increases his reading rate by 5 pages every day. In how many days will he finish reading the book?",
    ["\\(10\\) days", "\\(9\\) days", "\\(11\\) days", "\\(12\\) days"],
    "A", "OSC", "hard",
    "\\(a = 10, d = 5, S_n = 325\\). \\(\\frac{n}{2}[20 + 5(n - 1)] = 325 \\implies n(5n + 15) = 650 \\implies n^2 + 3n - 130 = 0 \\implies (n - 10)(n + 13) = 0\\). Since \\(n > 0\\), \\(n = 10\\) days."
)

t34_exam.extend([
    # 28
    ("A ball rolling down an incline moves 6 meters in the first second, 10 meters in the second second, 14 meters in the third second, and so on. How far does it roll in the \\(8^{\\text{th}}\\) second?",
     ["\\(34\\text{ m}\\)", "\\(32\\text{ m}\\)", "\\(36\\text{ m}\\)", "\\(38\\text{ m}\\)"],
     "A", "OSC", "easy",
     "\\(a = 6, d = 4\\). Distance in 8th second is \\(t_8 = a + 7d = 6 + 7(4) = 6 + 28 = 34\\text{ m}\\)."),

    # 29
    ("What is the total distance rolled by the ball in Question 28 during the first 8 seconds?",
     ["\\(160\\text{ m}\\)", "\\(150\\text{ m}\\)", "\\(170\\text{ m}\\)", "\\(155\\text{ m}\\)"],
     "A", "OSC", "easy",
     "\\(S_8 = \\frac{8}{2}(t_1 + t_8) = 4(6 + 34) = 4(40) = 160\\text{ m}\\)."),

    # 30
    ("In a lottery, the first prize is ₹50,000 and each subsequent prize decreases by ₹5,000. If there are 8 prizes in total, what is the total prize money distributed?",
     ["₹2,60,000", "\\(₹2,50,000\\)", "\\(₹2,70,000\\)", "\\(₹2,40,000\\)"],
     "A", "OSC", "medium",
     "\\(a = 50000, d = -5000, n = 8\\). \\(S_8 = 4[2(50000) + 7(-5000)] = 4[100000 - 35000] = 4(65000) = 2,60,000\\)."),

    # 31
    ("A water tank leaks 3 liters on the first day, 5 liters on the second day, 7 liters on the third day, and so on. If the tank was empty after 15 days, how much water was initially in the tank?",
     ["\\(255\\text{ liters}\\)", "\\(250\\text{ liters}\\)", "\\(260\\text{ liters}\\)", "\\(245\\text{ liters}\\)"],
     "A", "OSC", "medium",
     "\\(a = 3, d = 2, n = 15\\). \\(S_{15} = \\frac{15}{2}[6 + 14(2)] = \\frac{15}{2}[34] = 15 \\times 17 = 255\\text{ liters}\\)."),

    # 32
    ("A farmer buys a tractor for ₹12,00,000. He pays ₹6,00,000 in cash and agrees to pay the balance in annual installments of ₹50,000 plus 12% interest on the unpaid amount. How much will the tractor cost him in total?",
     ["₹16,68,000", "\\(₹16,50,000\\)", "\\(₹17,00,000\\)", "\\(₹16,00,000\\)"],
     "A", "OSC", "hard",
     "Unpaid balance \\(= 6,00,000\\). Paid in \\(600000 / 50000 = 12\\) installments of 50,000 plus interest. Interest paid in year 1 is \\(12\\%\\) of 6,00,000 \\(= 72,000\\); year 2 is \\(12\\%\\) of 5,50,000 \\(= 66,000\\), ..., year 12 is \\(12\\%\\) of 50,000 \\(= 6,000\\). Interest is an AP: \\(a = 72000, d = -6000, n = 12\\). Total interest \\(S_{12} = 6(72000 + 6000) = 6 \\times 78000 = 4,68,000\\). Total cost \\(= 12,00,000 + 4,68,000 = 16,68,000\\)."),

    # 33
    ("A shamiana is supported by 15 poles. The height of the shortest pole is 3 m and the height increases uniformly by 0.2 m for each subsequent pole. What is the height of the tallest pole?",
     ["\\(5.8\\text{ m}\\)", "\\(6.0\\text{ m}\\)", "\\(5.6\\text{ m}\\)", "\\(5.4\\text{ m}\\)"],
     "A", "OSC", "easy",
     "\\(a = 3, d = 0.2, n = 15\\). \\(t_{15} = 3 + 14(0.2) = 3 + 2.8 = 5.8\\text{ m}\\)."),

    # 34
    ("The angles of a triangle are in AP. If the smallest angle is \\(30^\\circ\\), what are the other two angles?",
     ["\\(60^\\circ, 90^\\circ\\)", "\\(50^\\circ, 100^\\circ\\)", "\\(55^\\circ, 95^\\circ\\)", "\\(45^\\circ, 105^\\circ\\)"],
     "A", "OSC", "easy",
     "Let angles be \\(a, a + d, a + 2d\\). Sum \\(= 3a + 3d = 180^\\circ \\implies a + d = 60^\\circ\\). Given \\(a = 30^\\circ \\implies d = 30^\\circ\\). The angles are \\(30^\\circ, 60^\\circ, 90^\\circ\\)."),

    # 35
    ("The angles of a quadrilateral are in AP. If the common difference is \\(10^\\circ\\), find the smallest angle.",
     ["\\(75^\\circ\\)", "\\(70^\\circ\\)", "\\(80^\\circ\\)", "\\(65^\\circ\\)"],
     "A", "OSC", "medium",
     "Sum of angles of quadrilateral \\(= 360^\\circ\\). \\(S_4 = 2[2a + 3(10)] = 360 \\implies 2a + 30 = 180 \\implies 2a = 150 \\implies a = 75^\\circ\\)."),

    # 36
    ("A clock strikes once at 1 o'clock, twice at 2 o'clock, thrice at 3 o'clock, and so on. How many times will it strike in 12 hours?",
     ["\\(78\\) times", "\\(72\\) times", "\\(84\\) times", "\\(75\\) times"],
     "A", "OSC", "easy",
     "\\(1 + 2 + 3 + \\dots + 12 = \\frac{12 \\times 13}{2} = 78\\) times."),

    # 37
    ("How many times does the clock in Question 36 strike in a full 24-hour day?",
     ["\\(156\\) times", "\\(144\\) times", "\\(160\\) times", "\\(150\\) times"],
     "A", "OSC", "easy",
     "In 24 hours, the 12-hour cycle repeats twice: \\(2 \\times 78 = 156\\) times."),

    # 38
    ("A well of depth 20 meters is dug. The cost of digging is ₹150 for the first meter and increases by ₹50 for each succeeding meter. What is the total cost of digging the well?",
     ["₹12,500", "\\(₹12,000\\)", "\\(₹13,000\\)", "\\(₹11,500\\)"],
     "A", "OSC", "medium",
     "\\(a = 150, d = 50, n = 20\\). \\(S_{20} = 10[300 + 19(50)] = 10[300 + 950] = 10(1250) = 12,500\\)."),

    # 39
    ("A student deposits money in her piggy bank: ₹5 on day 1, ₹10 on day 2, ₹15 on day 3, up to day 30. How much total money is in the piggy bank at the end of 30 days?",
     ["₹2,325", "\\(₹2,300\\)", "\\(₹2,400\\)", "\\(₹2,250\\)"],
     "A", "OSC", "easy",
     "\\(a = 5, d = 5, n = 30\\). \\(S_{30} = 15(5 + 150) = 15(155) = 2,325\\)."),

    # 40
    ("In an auditorium, seats in rows are in AP. If row 1 has 18 seats and row 20 has 56 seats, what is the increase in seats per row?",
     ["\\(2\\) seats", "\\(3\\) seats", "\\(1.5\\) seats", "\\(2.5\\) seats"],
     "A", "OSC", "easy",
     "\\(t_{20} - t_1 = 19d = 56 - 18 = 38 \\implies d = 2\\) seats.")
])

t34_prac = [
    # 41
    ("A taxi fare is ₹20 for the first kilometer and increases by ₹8 for each additional kilometer. What is the fare for a journey of 15 km?",
     ["₹132", "\\(₹140\\)", "\\(₹128\\)", "\\(₹136\\)"],
     "A", "OSC", "easy",
     "Fare for 15 km \\(= 20 + 14 \\times 8 = 20 + 112 = 132\\)."),

    # 42
    ("In the taxi fare scenario of Question 41, what is the fare for 25 km?",
     ["₹212", "\\(₹220\\)", "\\(₹204\\)", "\\(₹216\\)"],
     "A", "OSC", "easy",
     "Fare \\(= 20 + 24(8) = 20 + 192 = 212\\)."),

    # 43
    ("A man saves ₹32 during the first month, ₹36 in the second month, ₹40 in the third month, and so on. In how many months will his total savings be ₹2,000?",
     ["\\(25\\) months", "\\(20\\) months", "\\(30\\) months", "\\(24\\) months"],
     "A", "OSC", "hard",
     "\\(a = 32, d = 4, S_n = 2000\\). \\(\\frac{n}{2}[64 + (n - 1)4] = 2000 \\implies n(30 + 2n) = 2000 \\implies 2n^2 + 30n - 2000 = 0 \\implies n^2 + 15n - 1000 = 0 \\implies (n - 25)(n + 40) = 0\\). Since \\(n > 0\\), \\(n = 25\\) months."),

    # 44
    ("A builder agrees to build an apartment block in 100 days. If delayed, penalty is ₹500 for day 1, ₹600 for day 2, ₹700 for day 3, etc. If he finishes in 110 days (10 days delay), what penalty does he pay?",
     ["₹9,500", "\\(₹9,000\\)", "\\(₹10,000\\)", "\\(₹8,500\\)"],
     "A", "OSC", "easy",
     "\\(a = 500, d = 100, n = 10\\). \\(S_{10} = 5[1000 + 9(100)] = 5[1900] = 9,500\\)."),

    # 45
    ("A machine depreciates in value such that it loses ₹12,000 in the first year, ₹11,000 in the second year, ₹10,000 in the third year, and so on. What is the total depreciation over 8 years?",
     ["₹68,000", "\\(₹65,000\\)", "\\(₹70,000\\)", "\\(₹66,000\\)"],
     "A", "OSC", "medium",
     "\\(a = 12000, d = -1000, n = 8\\). \\(S_8 = 4[24000 + 7(-1000)] = 4(17000) = 68,000\\)."),

    # 46
    ("An auditorium has 30 rows. There are 25 seats in the front row and each succeeding row has 2 more seats than the row in front of it. Find the total seating capacity.",
     ["\\(1620\\) seats", "\\(1600\\) seats", "\\(1650\\) seats", "\\(1580\\) seats"],
     "A", "OSC", "medium",
     "\\(a = 25, d = 2, n = 30\\). \\(S_{30} = 15[50 + 29(2)] = 15[50 + 58] = 15(108) = 1620\\)."),

    # 47
    ("In Question 46, how many seats are in the back row (\\(30^{\\text{th}}\\) row)?",
     ["\\(83\\) seats", "\\(85\\) seats", "\\(81\\) seats", "\\(79\\) seats"],
     "A", "OSC", "easy",
     "\\(t_{30} = 25 + 29(2) = 25 + 58 = 83\\)."),

    # 48
    ("A bank customer pays back a loan of ₹3,600 by 40 annual installments which form an AP. When 30 of the installments are paid, he dies leaving one-third of the loan unpaid. Find the value of the first installment.",
     ["₹51", "\\(₹50\\)", "\\(₹48\\)", "\\(₹55\\)"],
     "A", "OSC", "hard",
     "Total loan \\(S_{40} = 3600 \\implies 20(2a + 39d) = 3600 \\implies 2a + 39d = 180\\). After 30 installments, one-third (₹1200) is unpaid, so \\(S_{30} = 2400 \\implies 15(2a + 29d) = 2400 \\implies 2a + 29d = 160\\). Subtracting: \\(10d = 20 \\implies d = 2\\). Then \\(2a + 58 = 160 \\implies 2a = 102 \\implies a = 51\\)."),

    # 49
    ("A school rewards top students with cash scholarships: 1st gets ₹1,000, 2nd gets ₹900, 3rd gets ₹800, and so on down to the 8th student. What is the total prize amount?",
     ["₹5,200", "\\(₹5,000\\)", "\\(₹5,400\\)", "\\(₹4,800\\)"],
     "A", "OSC", "easy",
     "\\(a = 1000, d = -100, n = 8\\). \\(t_8 = 1000 - 700 = 300\\). \\(S_8 = 4(1000 + 300) = 4 \\times 1300 = 5,200\\)."),

    # 50
    ("In a polygon of \\(n\\) sides, the interior angles are in AP. The smallest angle is \\(120^\\circ\\) and the common difference is \\(5^\\circ\\). Find \\(n\\).",
     ["\\(9\\)", "\\(16\\)", "\\(9\\) or \\(16\\)", "\\(12\\)"],
     "A", "OSC", "hard",
     "Sum of interior angles \\(= (n - 2) \\times 180^\\circ\\). Also \\(S_n = \\frac{n}{2}[240 + (n - 1)5]\\). \\(\\frac{n}{2}[5n + 235] = 180n - 360 \\implies 5n^2 + 235n = 360n - 720 \\implies 5n^2 - 125n + 720 = 0 \\implies n^2 - 25n + 144 = 0 \\implies (n - 9)(n - 16) = 0\\). If \\(n = 16\\), the largest angle \\(t_{16} = 120 + 15(5) = 195^\\circ > 180^\\circ\\) (impossible for a convex polygon). Hence \\(n = 9\\)."),

    # 51
    ("A company manufactures 500 bicycles in its 2nd year and 800 bicycles in its 5th year. Assuming uniform annual growth, what was its 1st year production?",
     ["\\(400\\) bicycles", "\\(420\\) bicycles", "\\(380\\) bicycles", "\\(450\\) bicycles"],
     "A", "OSC", "medium",
     "\\(t_5 - t_2 = 3d = 800 - 500 = 300 \\implies d = 100\\). \\(a = t_2 - d = 500 - 100 = 400\\)."),

    # 52
    ("For the bicycle company in Question 51, what will be the production in its 8th year?",
     ["\\(1100\\) bicycles", "\\(1050\\) bicycles", "\\(1150\\) bicycles", "\\(1200\\) bicycles"],
     "A", "OSC", "easy",
     "\\(t_8 = 400 + 7(100) = 1100\\)."),

    # 53
    ("A gardener waters 20 flower pots placed along a line at intervals of 3 meters. The water source is located at the first pot. How far does he walk if he waters each pot individually and returns to the source each time?",
     ["\\(1140\\text{ m}\\)", "\\(1100\\text{ m}\\)", "\\(1200\\text{ m}\\)", "\\(1080\\text{ m}\\)"],
     "A", "OSC", "hard",
     "First pot is at source (0 m). Next 19 pots are at \\(3, 6, 9, \\dots, 57\\) meters. For each, round trip is \\(6, 12, 18, \\dots, 114\\) meters. \\(S_{19} = \\frac{19}{2}(6 + 114) = 19 \\times 60 = 1140\\text{ m}\\)."),

    # 54
    ("A person climbs a 10-meter ladder. The lowest rung is 45 cm wide and the width decreases uniformly to 25 cm at the top rung. What is the average width of the rungs?",
     ["\\(35\\text{ cm}\\)", "\\(34\\text{ cm}\\)", "\\(36\\text{ cm}\\)", "\\(33\\text{ cm}\\)"],
     "A", "OSC", "easy",
     "For any AP, the average of all terms is simply the average of the first and last terms: \\(\\frac{45 + 25}{2} = 35\\text{ cm}\\)."),

    # 55
    ("A solar company installs 10 panels in month 1, 14 panels in month 2, 18 in month 3, and so on. After how many months will they have installed a total of 260 panels?",
     ["\\(10\\) months", "\\(9\\) months", "\\(11\\) months", "\\(12\\) months"],
     "A", "OSC", "medium",
     "\\(a = 10, d = 4, S_n = 260\\). \\(\\frac{n}{2}[20 + (n - 1)4] = 260 \\implies n(2n + 8) = 260 \\implies 2n^2 + 8n - 260 = 0 \\implies n^2 + 4n - 130 = 0\\) let's re-check: \\(n(4n + 16)/2 = n(2n + 8) = 2n^2 + 8n = 260 \\implies n^2 + 4n - 130 = 0\\), discriminant \\(16 + 520 = 536\\) not a square! Let's adjust \\(S_n = 280 \\implies n^2 + 4n - 140 = 0 \\implies (n + 14)(n - 10) = 0 \\implies n = 10\\)."),
]
# Clean fix for 55
t34_prac[-1] = (
    "A solar company installs 10 panels in month 1, 14 panels in month 2, 18 in month 3, and so on. After how many months will they have installed a total of 280 panels?",
    ["\\(10\\) months", "\\(9\\) months", "\\(11\\) months", "\\(12\\) months"],
    "A", "OSC", "medium",
    "\\(a = 10, d = 4, S_n = 280\\). \\(\\frac{n}{2}[20 + (n - 1)4] = 280 \\implies n(2n + 8) = 280 \\implies n^2 + 4n - 140 = 0 \\implies (n - 10)(n + 14) = 0\\). Thus \\(n = 10\\) months."
)

t34_prac.extend([
    # 56
    ("A student solves 5 math problems on Monday, 8 on Tuesday, 11 on Wednesday, and so on for 7 days. How many problems does he solve on Sunday?",
     ["\\(23\\) problems", "\\(20\\) problems", "\\(26\\) problems", "\\(21\\) problems"],
     "A", "OSC", "easy",
     "\\(a = 5, d = 3\\). Sunday is 7th day: \\(t_7 = 5 + 6(3) = 23\\)."),

    # 57
    ("What is the total number of problems the student in Question 56 solves during the entire week?",
     ["\\(98\\) problems", "\\(95\\) problems", "\\(102\\) problems", "\\(92\\) problems"],
     "A", "OSC", "easy",
     "\\(S_7 = \\frac{7}{2}(5 + 23) = \\frac{7}{2}(28) = 7 \\times 14 = 98\\)."),

    # 58
    ("A fuel tank's gauge drops by 4 liters on hour 1, 5.5 liters on hour 2, 7 liters on hour 3, and so on. How much fuel is consumed in the 6th hour?",
     ["\\(11.5\\text{ liters}\\)", "\\(11.0\\text{ liters}\\)", "\\(12.0\\text{ liters}\\)", "\\(10.5\\text{ liters}\\)"],
     "A", "OSC", "easy",
     "\\(a = 4, d = 1.5\\). \\(t_6 = 4 + 5(1.5) = 4 + 7.5 = 11.5\\text{ liters}\\)."),

    # 59
    ("A library adds 50 new books in January, 75 in February, 100 in March, and so on. How many books were added in total by December of that year?",
     ["\\(2250\\) books", "\\(2200\\) books", "\\(2300\\) books", "\\(2150\\) books"],
     "A", "OSC", "medium",
     "\\(a = 50, d = 25, n = 12\\). \\(S_{12} = 6[100 + 11(25)] = 6[100 + 275] = 6(375) = 2250\\)."),

    # 60
    ("A swimmer swims 10 laps on week 1, 13 on week 2, 16 on week 3, up to week 15. How many laps does she swim in week 15?",
     ["\\(52\\) laps", "\\(55\\) laps", "\\(49\\) laps", "\\(50\\) laps"],
     "A", "OSC", "easy",
     "\\(t_{15} = 10 + 14(3) = 10 + 42 = 52\\)."),

    # 61
    ("What is the total number of laps swum by the swimmer in Question 60 over all 15 weeks?",
     ["\\(465\\) laps", "\\(450\\) laps", "\\(480\\) laps", "\\(460\\) laps"],
     "A", "OSC", "easy",
     "\\(S_{15} = \\frac{15}{2}(10 + 52) = \\frac{15}{2}(62) = 15 \\times 31 = 465\\)."),

    # 62
    ("A mobile company’s subscriber count grows by 1500 each month. If they had 20,000 subscribers initially, how many subscribers will they have after 24 months?",
     ["\\(56,000\\)", "\\(55,000\\)", "\\(54,500\\)", "\\(57,000\\)"],
     "A", "OSC", "easy",
     "\\(20000 + 24(1500) = 20000 + 36000 = 56,000\\)."),

    # 63
    ("A delivery driver delivers 40 parcels on day 1, 44 on day 2, 48 on day 3, etc. On which day will he deliver 80 parcels?",
     ["Day \\(11\\)", "Day \\(10\\)", "Day \\(12\\)", "Day \\(9\\)"],
     "A", "OSC", "easy",
     "\\(80 = 40 + (n - 1)4 \\implies 40 = 4(n - 1) \\implies n - 1 = 10 \\implies n = 11\\)."),

    # 64
    ("Find the total parcels delivered in those 11 days in Question 63.",
     ["\\(660\\) parcels", "\\(640\\) parcels", "\\(680\\) parcels", "\\(650\\) parcels"],
     "A", "OSC", "easy",
     "\\(S_{11} = \\frac{11}{2}(40 + 80) = \\frac{11}{2}(120) = 11 \\times 60 = 660\\)."),

    # 65
    ("A savings scheme gives an interest of ₹200 in the first year, ₹250 in the second year, ₹300 in the third year, etc. In how many years will the total interest accumulated be ₹3,500?",
     ["\\(10\\) years", "\\(9\\) years", "\\(11\\) years", "\\(8\\) years"],
     "A", "OSC", "medium",
     "\\(a = 200, d = 50, S_n = 3500\\). \\(\\frac{n}{2}[400 + 50(n - 1)] = 3500 \\implies n(50n + 350) = 7000 \\implies 50n^2 + 350n - 7000 = 0 \\implies n^2 + 7n - 140 = 0 \\implies (n - 10)(n + 14) = 0 \\implies n = 10\\)."),

    # 66
    ("A ladder has rungs spaced 25 cm apart. The total length of the ladder is 2.5 m (250 cm). How many rungs are there on the ladder?",
     ["\\(11\\) rungs", "\\(10\\) rungs", "\\(12\\) rungs", "\\(9\\) rungs"],
     "A", "OSC", "medium",
     "Number of spaces \\(= 250 / 25 = 10\\). The number of rungs is one more than the number of spaces: \\(10 + 1 = 11\\) rungs."),

    # 67
    ("A factory produces 100 units in month 1 and doubles production each month. Does this follow an Arithmetic Progression?",
     ["No, because consecutive terms have a constant ratio rather than a constant difference",
      "Yes, because production increases each month",
      "Yes, with common difference 100",
      "Yes, because it is a sequence"],
     "A", "OSC", "easy",
     "Doubling means each term is multiplied by 2 (Geometric Progression), not adding a constant difference. Hence it is NOT an AP."),

    # 68
    ("A runner burns 100 calories on lap 1, 110 on lap 2, 120 on lap 3, and so on. How many calories does he burn in lap 10?",
     ["\\(190\\) calories", "\\(200\\) calories", "\\(180\\) calories", "\\(210\\) calories"],
     "A", "OSC", "easy",
     "\\(t_{10} = 100 + 9(10) = 190\\) calories."),

    # 69
    ("What are the total calories burned by the runner in Question 68 over 10 laps?",
     ["\\(1450\\) calories", "\\(1400\\) calories", "\\(1500\\) calories", "\\(1420\\) calories"],
     "A", "OSC", "easy",
     "\\(S_{10} = 5(100 + 190) = 5(290) = 1450\\) calories."),

    # 70
    ("A student's test score improved by 3 marks each week: 45, 48, 51, ..., 75. For how many weeks did he take tests?",
     ["\\(11\\) weeks", "\\(10\\) weeks", "\\(12\\) weeks", "\\(9\\) weeks"],
     "A", "OSC", "easy",
     "\\(75 = 45 + (n - 1)3 \\implies 30 = 3(n - 1) \\implies n - 1 = 10 \\implies n = 11\\).")
])

t34_mock = [
    # 71
    ("Why can word problems involving equal periodic increments be solved using AP?",
     ["Because equal periodic increments create a constant common difference (d) between consecutive terms",
      "Because all real world problems are arithmetic progressions",
      "Because equations in one variable cannot solve word problems",
      "Because sums of money are always linear functions"],
     "A", "OSC", "easy",
     "Whenever a quantity increases or decreases by a fixed amount in each regular interval, the sequence of values forms an Arithmetic Progression."),

    # 72
    ("In an AP word problem, what does the variable \\(n\\) typically represent?",
     ["The number of time intervals, periods, rows, days, or items",
      "The total money saved",
      "The interest rate",
      "The change per day"],
     "A", "OSC", "easy",
     "\\(n\\) is the counting index representing the number of installments, days, rows, or steps."),

    # 73
    ("In Sanika's savings problem, why was the number of days taken as 366 instead of 365?",
     ["Because the year 2016 was a leap year",
      "Because Sanika saved for an extra day in January",
      "Because arithmetic progressions require an even number of terms",
      "Because of a printing error in textbook"],
     "A", "OSC", "easy",
     "2016 is divisible by 4, making it a leap year with 366 days (February had 29 days)."),

    # 74
    ("If an installment decreases by ₹50 each month, what is the value of the common difference \\(d\\)?",
     ["\\(-50\\)", "\\(50\\)", "\\(0\\)", "\\(1/50\\)"],
     "A", "OSC", "easy",
     "A decreasing amount implies a negative common difference: \\(d = -50\\)."),

    # 75
    ("If a loan repayment specifies 12 monthly installments, what is \\(n\\)?",
     ["\\(12\\)", "\\(1\\)", "\\(10\\)", "\\(24\\)"],
     "A", "OSC", "easy",
     "There are 12 installments, so \\(n = 12\\)."),

    # 76
    ("If each row has 2 more seats than the preceding row, what is \\(d\\)?",
     ["\\(2\\)", "\\(-2\\)", "\\(1\\)", "\\(0\\)"],
     "A", "OSC", "easy",
     "The difference between any row and the previous row is \\(+2\\)."),

    # 77
    ("When finding total seats in an auditorium across all rows, which formula is used?",
     ["\\(S_n = \\frac{n}{2}[2a + (n - 1)d]\\)", "\\(t_n = a + (n - 1)d\\)", "\\(v = u + at\\)", "\\(A = P(1 + r)^t\\)"],
     "A", "OSC", "easy",
     "The total seats across all rows is the sum of terms of the AP: \\(S_n\\)."),

    # 78
    ("When finding the number of seats in the \\(15^{\\text{th}}\\) row only, which formula is used?",
     ["\\(t_{15} = a + 14d\\)", "\\(S_{15} = \\frac{15}{2}(2a + 14d)\\)", "\\(15a\\)", "\\(15d\\)"],
     "A", "OSC", "easy",
     "The number of seats in a single specific row is given by the general term formula \\(t_n\\)."),

    # 79
    ("Can a physical quantity like number of rows or number of logs be negative or fractional?",
     ["No, count of objects must be a positive integer (natural number)",
      "Yes, half logs and negative rows are valid",
      "Yes, quadratic solutions are always accepted",
      "Only if roots are real"],
     "A", "OSC", "easy",
     "Physical counts must be positive integers; extraneous negative or fractional roots from quadratic equations are rejected."),

    # 80
    ("If a person saves ₹10 on day 1, ₹20 on day 2, ₹30 on day 3, what is \\(a\\) and \\(d\\)?",
     ["\\(a = 10, d = 10\\)", "\\(a = 10, d = 20\\)", "\\(a = 0, d = 10\\)", "\\(a = 20, d = 10\\)"],
     "A", "OSC", "easy",
     "\\(a = 10\\) and \\(d = 20 - 10 = 10\\)."),

    # 81
    ("If daily temperatures decrease uniformly, is the common difference positive or negative?",
     ["Negative", "Positive", "Zero", "Variable"],
     "A", "OSC", "easy",
     "When values decrease consecutively, \\(t_{k+1} - t_k < 0\\), so \\(d\\) is negative."),

    # 82
    ("In a triangular tree plantation where row 1 has 1 tree, row 2 has 2 trees, ..., row \\(n\\) has \\(n\\) trees, what formula gives total trees?",
     ["\\(\\frac{n(n + 1)}{2}\\)", "\\(n^2\\)", "\\(n(n - 1)\\)", "\\(2n + 1\\)"],
     "A", "OSC", "easy",
     "This is the sum of the first \\(n\\) natural numbers: \\(S_n = \\frac{n(n + 1)}{2}\\).")
]

if __name__ == "__main__":
    topic_code = "MH-10-MTH1-3-3.4"
    all_qs = build_topic_questions(topic_code, t34_exam, t34_prac, t34_mock)
    out_path = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch3_t4.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {topic_code} -> {out_path}")
