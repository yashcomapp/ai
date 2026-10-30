# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 2: Quadratic Equations (Topic 2.7: Applied Word Problems)
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

TOPIC_CODE = "MH-10-MTH1-2-2.7"

# 40 EXAM (1-40)
exam_data = [
    # 1
    ("Product of Pragati's age 2 years ago and 3 years hence is 84. Find her present age.",
     ["9 years", "8 years", "10 years", "12 years"],
     "A", "OSC", "medium",
     "Let her present age be \\(x\\) years. Given: \\((x - 2)(x + 3) = 84 \\implies x^2 + x - 6 = 84 \\implies x^2 + x - 90 = 0\\). Factoring: \\((x + 10)(x - 9) = 0\\). Since age cannot be negative, \\(x = 9\\) years."),

    # 2
    ("The sum of the squares of two consecutive even natural numbers is 244. Find the numbers.",
     ["10 and 12", "8 and 10", "12 and 14", "14 and 16"],
     "A", "OSC", "medium",
     "Let the consecutive even natural numbers be \\(x\\) and \\(x + 2\\). Given: \\(x^2 + (x + 2)^2 = 244 \\implies x^2 + x^2 + 4x + 4 = 244 \\implies 2x^2 + 4x - 240 = 0 \\implies x^2 + 2x - 120 = 0\\). Factoring: \\((x + 12)(x - 10) = 0\\). Since natural numbers are positive, \\(x = 10\\). The numbers are 10 and 12."),

    # 3
    ("In an orange garden, there are 150 orange trees. The number of trees in each column is 5 more than that in each row. Find the number of trees in each row.",
     ["10 trees", "15 trees", "12 trees", "20 trees"],
     "A", "OSC", "medium",
     "Let number of trees in each row be \\(x\\). Then in each column is \\(x + 5\\). Total trees = \\(x(x + 5) = 150 \\implies x^2 + 5x - 150 = 0\\). Factoring: \\((x + 15)(x - 10) = 0\\). Since count of trees is positive, \\(x = 10\\)."),

    # 4
    ("From the previous problem, find the number of trees in each column.",
     ["15 trees", "10 trees", "20 trees", "25 trees"],
     "A", "OSC", "easy",
     "Number of trees in each column = \\(10 + 5 = 15\\)."),

    # 5
    ("Vivek is 5 years older than Kishor. The sum of the reciprocals of their ages is \\(\\frac{1}{6}\\). Find the present age of Kishor.",
     ["10 years", "15 years", "12 years", "8 years"],
     "A", "OSC", "hard",
     "Let Kishor's age be \\(x\\) and Vivek's be \\(x + 5\\). \\(\\frac{1}{x} + \\frac{1}{x+5} = \\frac{1}{6} \\implies \\frac{2x + 5}{x^2 + 5x} = \\frac{1}{6} \\implies 12x + 30 = x^2 + 5x \\implies x^2 - 7x - 30 = 0\\). Factoring: \\((x - 10)(x + 3) = 0\\). Age is positive, so Kishor is 10 years old."),

    # 6
    ("From the previous problem, what is the present age of Vivek?",
     ["15 years", "10 years", "20 years", "25 years"],
     "A", "OSC", "easy",
     "Vivek's age = \\(10 + 5 = 15\\) years."),

    # 7
    ("Suyash scored 10 marks more in his second test than in the first test. 5 times the score of the second test is the same as the square of the score in the first test. Find his score in the first test.",
     ["10 marks", "15 marks", "20 marks", "25 marks"],
     "A", "OSC", "medium",
     "Let first test score be \\(x\\). Second test score is \\(x + 10\\). Given: \\(5(x + 10) = x^2 \\implies x^2 - 5x - 50 = 0\\). Factoring: \\((x - 10)(x + 5) = 0\\). Since score cannot be negative here, \\(x = 10\\)."),

    # 8
    ("Kasam makes earthen pots on a daily basis. The production cost of each pot is Rs 40 more than 10 times the number of pots made per day. If total production cost per day is Rs 600, find the number of pots made per day.",
     ["6 pots", "10 pots", "8 pots", "12 pots"],
     "A", "OSC", "hard",
     "Let number of pots be \\(x\\). Cost per pot is \\(10x + 40\\). Total cost = \\(x(10x + 40) = 600 \\implies 10x^2 + 40x - 600 = 0 \\implies x^2 + 4x - 60 = 0\\). Factoring: \\((x + 10)(x - 6) = 0\\). Since pot count is positive, \\(x = 6\\) pots."),

    # 9
    ("From the previous problem, what is the production cost of one earthen pot?",
     ["Rs 100", "Rs 60", "Rs 140", "Rs 80"],
     "A", "OSC", "easy",
     "Cost per pot = \\(10(6) + 40 = 60 + 40 = 100\\) Rs."),

    # 10
    ("Pratik takes 8 hours to travel 36 km downstream and return to the same spot. The speed of the boat in still water is 12 km/h. Find the speed of the water current.",
     ["6 km/h", "4 km/h", "5 km/h", "3 km/h"],
     "A", "OSC", "hard",
     "Let current speed be \\(y\\) km/h. Downstream speed = \\(12 + y\\), upstream speed = \\(12 - y\\). \\(\\frac{36}{12 - y} + \\frac{36}{12 + y} = 8 \\implies 36\\left(\\frac{12 + y + 12 - y}{144 - y^2}\\right) = 8 \\implies \\frac{864}{144 - y^2} = 8 \\implies 144 - y^2 = 108 \\implies y^2 = 36 \\implies y = 6\\) km/h."),

    # 11
    ("Pintu takes 6 days more than Nishu to complete a certain work. If they work together they finish it in 4 days. How many days would Nishu take alone to complete the work?",
     ["6 days", "12 days", "8 days", "10 days"],
     "A", "OSC", "hard",
     "Let Nishu take \\(x\\) days and Pintu take \\(x + 6\\) days. One day work: \\(\\frac{1}{x} + \\frac{1}{x+6} = \\frac{1}{4} \\implies \\frac{2x + 6}{x^2 + 6x} = \\frac{1}{4} \\implies 8x + 24 = x^2 + 6x \\implies x^2 - 2x - 24 = 0\\). Factoring: \\((x - 6)(x + 4) = 0\\). Days must be positive, so Nishu takes 6 days."),

    # 12
    ("From the work problem above, how many days would Pintu take alone?",
     ["12 days", "6 days", "10 days", "16 days"],
     "A", "OSC", "easy",
     "Pintu takes \\(6 + 6 = 12\\) days."),

    # 13
    ("If 460 is divided by a natural number, the quotient is 6 more than five times the divisor and remainder is 1. Find the divisor.",
     ["9", "8", "10", "7"],
     "A", "OSC", "hard",
     "Dividend = Divisor \\(\\times\\) Quotient + Remainder. Let divisor be \\(x\\). Quotient = \\(5x + 6\\). \\(460 = x(5x + 6) + 1 \\implies 5x^2 + 6x + 1 = 460 \\implies 5x^2 + 6x - 459 = 0\\). \\((5x + 51)(x - 9) = 0\\). Since \\(x\\) is a natural number, \\(x = 9\\)."),

    # 14
    ("From the division problem above, what is the quotient?",
     ["51", "45", "56", "48"],
     "A", "OSC", "easy",
     "Quotient = \\(5(9) + 6 = 45 + 6 = 51\\)."),

    # 15
    ("The area of a trapezium is 33 sq cm. The parallel sides are \\(x\\) cm and \\(2x + 1\\) cm, and the altitude (distance between parallel sides) is \\(x - 4\\) cm. Find \\(x\\).",
     ["7 cm", "6 cm", "8 cm", "5 cm"],
     "A", "OSC", "hard",
     "Area = \\(\\frac{1}{2}(b_1 + b_2) \\times h = \\frac{1}{2}(x + 2x + 1)(x - 4) = 33 \\implies (3x + 1)(x - 4) = 66 \\implies 3x^2 - 11x - 4 = 66 \\implies 3x^2 - 11x - 70 = 0\\). Factoring: \\((3x + 14)(x - 7) = 0\\). Lengths are positive, so \\(x = 7\\) cm."),

    # 16
    ("From the trapezium problem above, what are the lengths of the two parallel sides?",
     ["7 cm and 15 cm", "6 cm and 13 cm", "8 cm and 17 cm", "5 cm and 11 cm"],
     "A", "OSC", "easy",
     "Parallel sides are \\(x = 7\\) cm and \\(2(7) + 1 = 15\\) cm."),

    # 17
    ("The sum of the squares of two consecutive natural numbers is 313. Find the numbers.",
     ["12 and 13", "11 and 12", "13 and 14", "10 and 11"],
     "A", "OSC", "medium",
     "\\(x^2 + (x + 1)^2 = 313 \\implies 2x^2 + 2x + 1 = 313 \\implies 2x^2 + 2x - 312 = 0 \\implies x^2 + x - 156 = 0\\). Factoring: \\((x + 13)(x - 12) = 0\\). Natural number \\(x = 12\\). Numbers are 12 and 13."),

    # 18
    ("The product of two consecutive positive integers is 306. Find the smaller integer.",
     ["17", "18", "16", "15"],
     "A", "OSC", "medium",
     "\\(x(x + 1) = 306 \\implies x^2 + x - 306 = 0 \\implies (x + 18)(x - 17) = 0 \\implies x = 17\\)."),

    # 19
    ("From the previous question, what is the larger integer?",
     ["18", "17", "19", "20"],
     "A", "OSC", "easy",
     "Larger integer is \\(17 + 1 = 18\\)."),

    # 20
    ("Rohan's mother is 26 years older than him. The product of their ages 3 years from now will be 360. Find Rohan's present age.",
     ["7 years", "8 years", "6 years", "10 years"],
     "A", "OSC", "medium",
     "Let Rohan be \\(x\\). Mother is \\(x + 26\\). In 3 years: \\((x + 3)(x + 29) = 360 \\implies x^2 + 32x + 87 = 360 \\implies x^2 + 32x - 273 = 0\\). Factoring: \\((x + 39)(x - 7) = 0 \\implies x = 7\\) years."),

    # 21
    ("A train travels a distance of 480 km at a uniform speed. If the speed had been 8 km/h less, then it would have taken 3 hours more to cover the same distance. Find the speed of the train.",
     ["40 km/h", "48 km/h", "36 km/h", "50 km/h"],
     "A", "OSC", "hard",
     "\\(\\frac{480}{s - 8} - \\frac{480}{s} = 3 \\implies 480\\left(\\frac{s - (s - 8)}{s(s - 8)}\\right) = 3 \\implies \\frac{480 \\times 8}{s^2 - 8s} = 3 \\implies 160 \\times 8 = s^2 - 8s \\implies s^2 - 8s - 1280 = 0\\). Factoring: \\((s - 40)(s + 32) = 0 \\implies s = 40\\) km/h."),

    # 22
    ("The altitude of a right triangle is 7 cm less than its base. If the hypotenuse is 13 cm, find the base.",
     ["12 cm", "5 cm", "10 cm", "8 cm"],
     "A", "OSC", "medium",
     "By Pythagoras: \\(b^2 + (b - 7)^2 = 13^2 = 169 \\implies b^2 + b^2 - 14b + 49 = 169 \\implies 2b^2 - 14b - 120 = 0 \\implies b^2 - 7b - 60 = 0\\). Factoring: \\((b - 12)(b + 5) = 0 \\implies b = 12\\) cm."),

    # 23
    ("From the right triangle problem above, what is the altitude?",
     ["5 cm", "12 cm", "7 cm", "6 cm"],
     "A", "OSC", "easy",
     "Altitude = \\(12 - 7 = 5\\) cm."),

    # 24
    ("The hypotenuse of a right-angled triangle is 25 cm. The difference between the other two sides is 5 cm. Find the longer side.",
     ["20 cm", "15 cm", "24 cm", "18 cm"],
     "A", "OSC", "medium",
     "Let sides be \\(x\\) and \\(x - 5\\). \\(x^2 + (x - 5)^2 = 25^2 = 625 \\implies 2x^2 - 10x + 25 = 625 \\implies 2x^2 - 10x - 600 = 0 \\implies x^2 - 5x - 300 = 0\\). Factoring: \\((x - 20)(x + 15) = 0 \\implies x = 20\\) cm."),

    # 25
    ("From the previous question, what is the shorter side?",
     ["15 cm", "20 cm", "10 cm", "12 cm"],
     "A", "OSC", "easy",
     "Shorter side = \\(20 - 5 = 15\\) cm."),

    # 26
    ("The perimeter of a rectangular plot is 50 m and its area is 150 sq m. Find its length.",
     ["15 m", "10 m", "20 m", "25 m"],
     "A", "OSC", "easy",
     "\\(2(l + w) = 50 \\implies l + w = 25\\). Area \\(l(25 - l) = 150 \\implies l^2 - 25l + 150 = 0 \\implies (l - 15)(l - 10) = 0\\). Length is 15 m (and width is 10 m)."),

    # 27
    ("Two water taps together can fill a tank in \\(9\\frac{3}{8}\\) hours (\\(\\frac{75}{8}\\) hours). The tap of larger diameter takes 10 hours less than the smaller one to fill the tank separately. Find the time taken by the smaller tap.",
     ["25 hours", "15 hours", "20 hours", "30 hours"],
     "A", "OSC", "hard",
     "\\(\\frac{1}{x} + \\frac{1}{x - 10} = \\frac{8}{75} \\implies \\frac{2x - 10}{x^2 - 10x} = \\frac{8}{75} \\implies 75(2x - 10) = 8(x^2 - 10x) \\implies 150x - 750 = 8x^2 - 80x \\implies 8x^2 - 230x + 750 = 0 \\implies 4x^2 - 115x + 375 = 0\\). Factoring: \\((4x - 15)(x - 25) = 0\\). Since \\(x > 10\\), \\(x = 25\\) hours."),

    # 28
    ("From the water tap problem above, how long does the larger tap take alone?",
     ["15 hours", "25 hours", "10 hours", "12 hours"],
     "A", "OSC", "easy",
     "Time for larger tap = \\(25 - 10 = 15\\) hours."),

    # 29
    ("An express train takes 1 hour less than a passenger train to travel 132 km between Mysore and Bangalore. If the average speed of express train is 11 km/h more than passenger train, find passenger train speed.",
     ["33 km/h", "44 km/h", "30 km/h", "35 km/h"],
     "A", "OSC", "hard",
     "\\(\\frac{132}{s} - \\frac{132}{s + 11} = 1 \\implies 132(11) = s(s + 11) \\implies s^2 + 11s - 1452 = 0\\). Factoring: \\((s + 44)(s - 33) = 0 \\implies s = 33\\) km/h."),

    # 30
    ("From the train problem above, what is the speed of the express train?",
     ["44 km/h", "33 km/h", "55 km/h", "40 km/h"],
     "A", "OSC", "easy",
     "Express speed = \\(33 + 11 = 44\\) km/h."),

    # 31
    ("Sum of the areas of two squares is 468 sq m. If the difference of their perimeters is 24 m, find the side of the larger square.",
     ["18 m", "12 m", "15 m", "16 m"],
     "A", "OSC", "hard",
     "Let sides be \\(x\\) and \\(y\\). Difference of perimeters: \\(4x - 4y = 24 \\implies x - y = 6 \\implies y = x - 6\\). Sum of areas: \\(x^2 + (x - 6)^2 = 468 \\implies 2x^2 - 12x + 36 = 468 \\implies 2x^2 - 12x - 432 = 0 \\implies x^2 - 6x - 216 = 0\\). Factoring: \\((x - 18)(x + 12) = 0 \\implies x = 18\\) m."),

    # 32
    ("From the previous question, what is the side of the smaller square?",
     ["12 m", "18 m", "6 m", "10 m"],
     "A", "OSC", "easy",
     "Side of smaller square = \\(18 - 6 = 12\\) m."),

    # 33
    ("A motor boat whose speed is 18 km/h in still water takes 1 hour more to go 24 km upstream than to return downstream to the same spot. Find the speed of the stream.",
     ["6 km/h", "4 km/h", "5 km/h", "3 km/h"],
     "A", "OSC", "hard",
     "\\(\\frac{24}{18 - s} - \\frac{24}{18 + s} = 1 \\implies 24(2s) = 324 - s^2 \\implies 48s = 324 - s^2 \\implies s^2 + 48s - 324 = 0\\). Factoring: \\((s + 54)(s - 6) = 0 \\implies s = 6\\) km/h."),

    # 34
    ("The sum of a number and its reciprocal is \\(\\frac{10}{3}\\). Find the number.",
     ["3 (or 1/3)", "4", "2", "5"],
     "A", "OSC", "medium",
     "\\(x + \\frac{1}{x} = \\frac{10}{3} \\implies 3x^2 - 10x + 3 = 0 \\implies (3x - 1)(x - 3) = 0 \\implies x = 3\\) or \\(x = 1/3\\)."),

    # 35
    ("The sum of a number and its reciprocal is \\(\\frac{26}{5}\\). Find the number.",
     ["5 (or 1/5)", "6", "4", "2"],
     "A", "OSC", "medium",
     "\\(x + \\frac{1}{x} = \\frac{26}{5} \\implies 5x^2 - 26x + 5 = 0 \\implies (5x - 1)(x - 5) = 0 \\implies x = 5\\) or \\(1/5\\)."),

    # 36
    ("The difference between a positive number and its reciprocal is \\(\\frac{15}{4}\\). Find the number.",
     ["4", "1/4", "3", "5"],
     "A", "OSC", "medium",
     "\\(x - \\frac{1}{x} = \\frac{15}{4} \\implies 4x^2 - 15x - 4 = 0 \\implies (4x + 1)(x - 4) = 0\\). Since \\(x > 0\\), \\(x = 4\\)."),

    # 37
    ("Divide 16 into two parts such that twice the square of the larger part exceeds the square of the smaller part by 164. Find the larger part.",
     ["10", "6", "12", "8"],
     "A", "OSC", "hard",
     "Let larger part be \\(x\\) and smaller be \\(16 - x\\). \\(2x^2 - (16 - x)^2 = 164 \\implies 2x^2 - (256 - 32x + x^2) = 164 \\implies x^2 + 32x - 420 = 0\\). Factoring: \\((x + 42)(x - 10) = 0 \\implies x = 10\\)."),

    # 38
    ("From the previous question, what is the smaller part?",
     ["6", "10", "8", "4"],
     "A", "OSC", "easy",
     "Smaller part = \\(16 - 10 = 6\\)."),

    # 39
    ("In a flight of 600 km, an aircraft was slowed down due to bad weather. Its average speed for the trip was reduced by 200 km/h and time of flight increased by 30 minutes (1/2 hour). Find the original scheduled duration of flight.",
     ["1 hour", "1.5 hours", "2 hours", "2.5 hours"],
     "A", "OSC", "hard",
     "\\(\\frac{600}{s - 200} - \\frac{600}{s} = \\frac{1}{2} \\implies 600(200)(2) = s^2 - 200s \\implies s^2 - 200s - 240000 = 0 \\implies (s - 600)(s + 400) = 0 \\implies s = 600\\) km/h. Duration = \\(600/600 = 1\\) hour."),

    # 40
    ("From the flight problem above, what was the original scheduled speed of the aircraft?",
     ["600 km/h", "400 km/h", "500 km/h", "700 km/h"],
     "A", "OSC", "easy",
     "Original speed was 600 km/h.")
]

t27_prac = [
    # 41
    ("Find two consecutive natural numbers whose product is 20.", ["4 and 5", "5 and 6", "2 and 10", "1 and 20"], "A", "OSC", "easy", "\\(x(x+1) = 20 \\implies x = 4\\)."),
    # 42
    ("Find two consecutive natural numbers whose product is 42.", ["6 and 7", "5 and 6", "7 and 8", "4 and 9"], "A", "OSC", "easy", "\\(x(x+1) = 42 \\implies x = 6\\)."),
    # 43
    ("Find two consecutive natural numbers whose product is 72.", ["8 and 9", "7 and 8", "9 and 10", "6 and 12"], "A", "OSC", "easy", "\\(x(x+1) = 72 \\implies x = 8\\)."),
    # 44
    ("Find two consecutive natural numbers whose product is 90.", ["9 and 10", "8 and 9", "10 and 11", "7 and 13"], "A", "OSC", "easy", "\\(x(x+1) = 90 \\implies x = 9\\)."),
    # 45
    ("Find two consecutive natural numbers whose product is 110.", ["10 and 11", "9 and 10", "11 and 12", "8 and 14"], "A", "OSC", "easy", "\\(x(x+1) = 110 \\implies x = 10\\)."),
    # 46
    ("Find two consecutive natural numbers whose product is 132.", ["11 and 12", "10 and 11", "12 and 13", "9 and 15"], "A", "OSC", "easy", "\\(x(x+1) = 132 \\implies x = 11\\)."),
    # 47
    ("Find two consecutive natural numbers whose product is 156.", ["12 and 13", "11 and 12", "13 and 14", "10 and 16"], "A", "OSC", "easy", "\\(x(x+1) = 156 \\implies x = 12\\)."),
    # 48
    ("Find two consecutive natural numbers whose product is 182.", ["13 and 14", "12 and 13", "14 and 15", "11 and 17"], "A", "OSC", "easy", "\\(x(x+1) = 182 \\implies x = 13\\)."),
    # 49
    ("Find two consecutive natural numbers whose product is 210.", ["14 and 15", "13 and 14", "15 and 16", "12 and 18"], "A", "OSC", "easy", "\\(x(x+1) = 210 \\implies x = 14\\)."),
    # 50
    ("Find two consecutive natural numbers whose product is 240.", ["15 and 16", "14 and 15", "16 and 17", "13 and 19"], "A", "OSC", "easy", "\\(x(x+1) = 240 \\implies x = 15\\)."),
    # 51
    ("Perimeter of a square is 40 m. Find its area.", ["100 sq m", "40 sq m", "160 sq m", "80 sq m"], "A", "OSC", "easy", "Side = 10 m, Area = 100 sq m."),
    # 52
    ("Perimeter of a rectangle is 20 m and area is 24 sq m. Find length.", ["6 m", "4 m", "5 m", "8 m"], "A", "OSC", "easy", "\\(l+w=10, lw=24 \\implies l=6, w=4\\)."),
    # 53
    ("Perimeter of a rectangle is 24 m and area is 35 sq m. Find length.", ["7 m", "5 m", "6 m", "8 m"], "A", "OSC", "easy", "\\(l+w=12, lw=35 \\implies l=7, w=5\\)."),
    # 54
    ("Perimeter of a rectangle is 26 m and area is 40 sq m. Find length.", ["8 m", "5 m", "10 m", "6 m"], "A", "OSC", "easy", "\\(l+w=13, lw=40 \\implies l=8, w=5\\)."),
    # 55
    ("Perimeter of a rectangle is 28 m and area is 48 sq m. Find length.", ["8 m", "6 m", "7 m", "9 m"], "A", "OSC", "easy", "\\(l+w=14, lw=48 \\implies l=8, w=6\\)."),
    # 56
    ("Perimeter of a rectangle is 30 m and area is 54 sq m. Find length.", ["9 m", "6 m", "8 m", "10 m"], "A", "OSC", "easy", "\\(l+w=15, lw=54 \\implies l=9, w=6\\)."),
    # 57
    ("Perimeter of a rectangle is 32 m and area is 60 sq m. Find length.", ["10 m", "6 m", "8 m", "12 m"], "A", "OSC", "easy", "\\(l+w=16, lw=60 \\implies l=10, w=6\\)."),
    # 58
    ("Perimeter of a rectangle is 34 m and area is 70 sq m. Find length.", ["10 m", "7 m", "9 m", "12 m"], "A", "OSC", "easy", "\\(l+w=17, lw=70 \\implies l=10, w=7\\)."),
    # 59
    ("Perimeter of a rectangle is 36 m and area is 80 sq m. Find length.", ["10 m", "8 m", "9 m", "12 m"], "A", "OSC", "easy", "\\(l+w=18, lw=80 \\implies l=10, w=8\\)."),
    # 60
    ("Perimeter of a rectangle is 38 m and area is 88 sq m. Find length.", ["11 m", "8 m", "10 m", "12 m"], "A", "OSC", "easy", "\\(l+w=19, lw=88 \\implies l=11, w=8\\)."),
    # 61
    ("Difference of two numbers is 4 and their product is 45. Find positive numbers.", ["9 and 5", "10 and 6", "8 and 4", "15 and 3"], "A", "OSC", "easy", "\\(x(x-4) = 45 \\implies x = 9, 5\\)."),
    # 62
    ("Difference of two numbers is 5 and their product is 50. Find positive numbers.", ["10 and 5", "15 and 10", "8 and 3", "25 and 2"], "A", "OSC", "easy", "\\(x(x-5) = 50 \\implies x = 10, 5\\)."),
    # 63
    ("Difference of two numbers is 6 and their product is 72. Find positive numbers.", ["12 and 6", "10 and 4", "9 and 3", "18 and 4"], "A", "OSC", "easy", "\\(x(x-6) = 72 \\implies x = 12, 6\\)."),
    # 64
    ("Difference of two numbers is 7 and their product is 60. Find positive numbers.", ["12 and 5", "10 and 3", "15 and 4", "14 and 7"], "A", "OSC", "easy", "\\(x(x-7) = 60 \\implies x = 12, 5\\)."),
    # 65
    ("Difference of two numbers is 8 and their product is 65. Find positive numbers.", ["13 and 5", "10 and 2", "15 and 7", "11 and 3"], "A", "OSC", "easy", "\\(x(x-8) = 65 \\implies x = 13, 5\\)."),
    # 66
    ("Difference of two numbers is 9 and their product is 70. Find positive numbers.", ["14 and 5", "12 and 3", "16 and 7", "10 and 1"], "A", "OSC", "easy", "\\(x(x-9) = 70 \\implies x = 14, 5\\)."),
    # 67
    ("Difference of two numbers is 10 and their product is 75. Find positive numbers.", ["15 and 5", "12 and 2", "20 and 10", "25 and 3"], "A", "OSC", "easy", "\\(x(x-10) = 75 \\implies x = 15, 5\\)."),
    # 68
    ("A number is 4 times another number and their product is 64. Find the positive numbers.", ["16 and 4", "8 and 2", "32 and 2", "12 and 3"], "A", "OSC", "easy", "\\(4x^2 = 64 \\implies x = 4, 4x = 16\\)."),
    # 69
    ("A number is 5 times another number and their product is 125. Find the positive numbers.", ["25 and 5", "15 and 3", "20 and 4", "50 and 2"], "A", "OSC", "easy", "\\(5x^2 = 125 \\implies x = 5, 5x = 25\\)."),
    # 70
    ("A number is 6 times another number and their product is 216. Find the positive numbers.", ["36 and 6", "18 and 3", "24 and 4", "30 and 5"], "A", "OSC", "easy", "\\(6x^2 = 216 \\implies x = 6, 6x = 36\\).")
]

t27_mock = [
    # 71
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0f172a" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Quadratic Word Problem Cycle</text>
  <text x="170" y="80" fill="#f8fafc" font-size="11" text-anchor="middle">Read Problem -> Form Quadratic ax² + bx + c = 0</text>
  <text x="170" y="105" fill="#4ade80" font-size="11" text-anchor="middle">Solve Roots -> Discard Inadmissible / Negative Values</text>
</svg>
</div>
Why does a quadratic word problem frequently yield two roots, of which only one is valid?""",
     ["Because quadratic equations algebraically generate two roots, but physical constraints (like positive ages, lengths, counts) eliminate negative or impossible values",
      "Because one root is always imaginary",
      "Because the second root is a typo",
      "Because quadratic equations can only have one root"],
     "A", "OSC", "easy",
     "While quadratic equations mathematically have up to two roots, physical quantities in real-world applications (speed, time, distance, age, physical objects) cannot be negative. Negative roots are extraneous in context."),

    # 72
    ("If the product of two positive numbers is 100 and their difference is 15, what are the numbers?", ["20 and 5", "25 and 4", "15 and 10", "50 and 2"], "A", "OSC", "easy", "\\(20 \\times 5 = 100, 20 - 5 = 15\\)."),
    # 73
    ("If the area of a square is 144 sq cm, what is its perimeter?", ["48 cm", "24 cm", "36 cm", "56 cm"], "A", "OSC", "easy", "Side = 12 cm, perimeter = \\(4 \\times 12 = 48\\) cm."),
    # 74
    ("If the area of a square is 169 sq cm, what is its perimeter?", ["52 cm", "26 cm", "39 cm", "60 cm"], "A", "OSC", "easy", "Side = 13 cm, perimeter = \\(4 \\times 13 = 52\\) cm."),
    # 75
    ("If the area of a square is 196 sq cm, what is its perimeter?", ["56 cm", "28 cm", "42 cm", "64 cm"], "A", "OSC", "easy", "Side = 14 cm, perimeter = \\(4 \\times 14 = 56\\) cm."),
    # 76
    ("If the area of a square is 225 sq cm, what is its perimeter?", ["60 cm", "30 cm", "45 cm", "75 cm"], "A", "OSC", "easy", "Side = 15 cm, perimeter = \\(4 \\times 15 = 60\\) cm."),
    # 77
    ("If the area of a square is 256 sq cm, what is its perimeter?", ["64 cm", "32 cm", "48 cm", "80 cm"], "A", "OSC", "easy", "Side = 16 cm, perimeter = \\(4 \\times 16 = 64\\) cm."),
    # 78
    ("If the area of a square is 289 sq cm, what is its perimeter?", ["68 cm", "34 cm", "51 cm", "85 cm"], "A", "OSC", "easy", "Side = 17 cm, perimeter = \\(4 \\times 17 = 68\\) cm."),
    # 79
    ("If the area of a square is 324 sq cm, what is its perimeter?", ["72 cm", "36 cm", "54 cm", "90 cm"], "A", "OSC", "easy", "Side = 18 cm, perimeter = \\(4 \\times 18 = 72\\) cm."),
    # 80
    ("If the area of a square is 361 sq cm, what is its perimeter?", ["76 cm", "38 cm", "57 cm", "95 cm"], "A", "OSC", "easy", "Side = 19 cm, perimeter = \\(4 \\times 19 = 76\\) cm."),
    # 81
    ("If the area of a square is 400 sq cm, what is its perimeter?", ["80 cm", "40 cm", "60 cm", "100 cm"], "A", "OSC", "easy", "Side = 20 cm, perimeter = \\(4 \\times 20 = 80\\) cm."),
    # 82
    ("""<div style="text-align:center; margin:12px 0;">
<svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="150" fill="#0b132b" rx="8"/>
  <rect x="25" y="25" width="290" height="100" rx="6" fill="#1c2541" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="170" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Verification Checklist</text>
  <text x="170" y="80" fill="#f8fafc" font-size="11" text-anchor="middle">1. Re-check equation setup from text</text>
  <text x="170" y="105" fill="#4ade80" font-size="11" text-anchor="middle">2. Ensure units are explicitly stated (cm, km/h, years)</text>
</svg>
</div>
What final detail must always accompany the numerical answers in applied word problems?""",
     ["Appropriate units of measurement (such as cm, km/h, years, rupees, trees)",
      "A sketch of the author",
      "The value of pi",
      "A logarithm table"],
     "A", "OSC", "easy",
     "Real-world word problems involve physical quantities. Providing the answer with its appropriate units (years, km/h, rupees, etc.) is essential for completeness and accuracy.")
]

all_q_27 = build_topic_questions(TOPIC_CODE, exam_data, t27_prac, t27_mock)
out_27 = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch2_t7.json")
with open(out_27, "w", encoding="utf-8") as f:
    json.dump(all_q_27, f, indent=2, ensure_ascii=False)
print(f"Generated {len(all_q_27)} questions for {TOPIC_CODE} -> {out_27}")
