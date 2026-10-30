# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 6: Statistics - Topic 6.1: Mean: Direct Method (MH-10-MTH1-6-6.1)
Total: 82 Canonical Questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# TOPIC 6.1: Mean of Grouped Frequency Distribution: Direct Method
t61_exam = [
    # 1
    ("What is the formula to calculate the Mean (\\(\\bar{X}\\)) of grouped data by the Direct Method?",
     ["\\(\\bar{X} = \\frac{\\sum f_i x_i}{\\sum f_i}\\)",
      "\\(\\bar{X} = \\frac{\\sum f_i}{\\sum f_i x_i}\\)",
      "\\(\\bar{X} = A + \\frac{\\sum f_i d_i}{N}\\)",
      "\\(\\bar{X} = \\sum f_i x_i\\)"],
     "A", "OSC", "easy",
     "In the Direct Method, the mean is the sum of products of frequencies and class marks divided by the total frequency: \\(\\bar{X} = \\frac{\\sum f_i x_i}{\\sum f_i}\\)."),

    # 2
    ("What is the 'class mark' (\\(x_i\\)) of a class interval?",
     ["The midpoint or average of the lower and upper class limits: \\(x_i = \\frac{\\text{Lower limit} + \\text{Upper limit}}{2}\\)",
      "The difference between upper and lower limits",
      "The frequency of that class",
      "The total number of classes"],
     "A", "OSC", "easy",
     "Class mark is defined as the midpoint of the class interval: \\(x_i = \\frac{L + U}{2}\\)."),

    # 3
    ("Find the class mark of the class interval \\(20 - 30\\).",
     ["\\(25\\)", "\\(10\\)", "\\(50\\)", "\\(20\\)"],
     "A", "OSC", "easy",
     "\\(x_i = \\frac{20 + 30}{2} = 25\\)."),

    # 4
    ("Find the class mark of the class interval \\(15 - 25\\).",
     ["\\(20\\)", "\\(10\\)", "\\(40\\)", "\\(25\\)"],
     "A", "OSC", "easy",
     "\\(x_i = \\frac{15 + 25}{2} = 20\\)."),

    # 5
    ("What is the class width (or class size \\(h\\)) of the interval \\(40 - 50\\)?",
     ["\\(10\\)", "\\(45\\)", "\\(90\\)", "\\(5\\)"],
     "A", "OSC", "easy",
     "\\(h = 50 - 40 = 10\\)."),

    # 6
    ("For the given distribution: \\(\\sum f_i x_i = 1260\\) and \\(\\sum f_i = 50\\). Find the Mean \\(\\bar{X}\\).",
     ["\\(25.2\\)", "\\(25.0\\)", "\\(26.0\\)", "\\(24.8\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{X} = \\frac{1260}{50} = 25.2\\)."),

    # 7
    ("If \\(\\sum f_i x_i = 1860\\) and \\(\\sum f_i = 30\\), what is the mean?",
     ["\\(62\\)", "\\(60\\)", "\\(64\\)", "\\(58\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{X} = \\frac{1860}{30} = 62\\)."),

    # 8
    ("In a grouped frequency distribution, the classes and frequencies are: \\(0-10\\) (freq 3), \\(10-20\\) (freq 5), \\(20-30\\) (freq 2). Find the mean.",
     ["\\(14\\)", "\\(15\\)", "\\(13.5\\)", "\\(14.5\\)"],
     "A", "OSC", "medium",
     "Class marks: 5, 15, 25. \\(\\sum f_i x_i = (3 \\times 5) + (5 \\times 15) + (2 \\times 25) = 15 + 75 + 50 = 140\\). Total frequency \\(\\sum f_i = 3 + 5 + 2 = 10\\). \\(\\bar{X} = 140 / 10 = 14\\)."),

    # 9
    ("The following table shows the frequency distribution of time (in hours) spent by 50 students in studies: \\(0-2\\) (7), \\(2-4\\) (18), \\(4-6\\) (12), \\(6-8\\) (10), \\(8-10\\) (3). Find the mean time spent by students using Direct Method.",
     ["\\(4.36\\text{ hours}\\)", "\\(4.50\\text{ hours}\\)", "\\(4.20\\text{ hours}\\)", "\\(4.60\\text{ hours}\\)"],
     "A", "OSC", "hard",
     "Class marks: 1, 3, 5, 7, 9. \\(\\sum f_i x_i = (7 \\times 1) + (18 \\times 3) + (12 \\times 5) + (10 \\times 7) + (3 \\times 9) = 7 + 54 + 60 + 70 + 27 = 218\\). \\(\\bar{X} = 218 / 50 = 4.36\\text{ hours}\\)."),

    # 10
    ("In a direct method calculation table, which columns are constructed?",
     ["Class Interval, Class Mark (\\(x_i\\)), Frequency (\\(f_i\\)), and Product (\\(f_i x_i\\))",
      "Class Interval, Cumulative Frequency, and Rank",
      "Lower limit, Upper limit, and Logarithm",
      "Class Interval and Percentage only"],
     "A", "OSC", "easy",
     "The 4 standard columns of the Direct Method table are Class, Class Mark (\\(x_i\\)), Frequency (\\(f_i\\)), and \\(f_i x_i\\)."),

    # 11
    ("Find the class mark of the class \\(0.5 - 1.0\\).",
     ["\\(0.75\\)", "\\(0.50\\)", "\\(1.50\\)", "\\(0.25\\)"],
     "A", "OSC", "easy",
     "\\(x_i = \\frac{0.5 + 1.0}{2} = 0.75\\)."),

    # 12
    ("If the mean of the numbers \\(6, 8, 5, 7, x\\) is \\(7\\), find \\(x\\).",
     ["\\(9\\)", "\\(8\\)", "\\(7\\)", "\\(10\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{6 + 8 + 5 + 7 + x}{5} = 7 \\implies 26 + x = 35 \\implies x = 9\\)."),

    # 13
    ("If the mean of \\(x, x+2, x+4, x+6, x+8\\) is \\(11\\), find \\(x\\).",
     ["\\(7\\)", "\\(9\\)", "\\(11\\)", "\\(5\\)"],
     "A", "OSC", "easy",
     "Mean is the middle term \\(x + 4\\). \\(x + 4 = 11 \\implies x = 7\\)."),

    # 14
    ("The classes are: \\(10-20\\) (freq 4), \\(20-30\\) (freq 6). Find the mean.",
     ["\\(21\\)", "\\(20\\)", "\\(22\\)", "\\(25\\)"],
     "A", "OSC", "easy",
     "Class marks: 15, 25. \\(\\sum f_i x_i = (4 \\times 15) + (6 \\times 25) = 60 + 150 = 210\\). Total freq \\(= 10\\). \\(\\bar{X} = 210 / 10 = 21\\)."),

    # 15
    ("What does \\(\\sum f_i\\) represent in a frequency distribution?",
     ["The total number of observations (or sample size \\(N\\))",
      "The sum of all class marks",
      "The mean of the data",
      "The range of the data"],
     "A", "OSC", "easy",
     "\\(\\sum f_i = N\\) is the sum of all individual frequencies, representing the total number of observations."),

    # 16
    ("If each observation in a dataset is increased by \\(5\\), what happens to the mean?",
     ["The mean increases by \\(5\\)",
      "The mean remains unchanged",
      "The mean is multiplied by 5",
      "The mean increases by 2.5"],
     "A", "OSC", "easy",
     "Adding a constant \\(k\\) to every observation increases the mean by exactly \\(k\\)."),

    # 17
    ("If each observation in a dataset is multiplied by \\(3\\), what happens to the mean?",
     ["The mean is multiplied by \\(3\\)",
      "The mean increases by 3",
      "The mean is divided by 3",
      "The mean remains unchanged"],
     "A", "OSC", "easy",
     "Multiplying each data value by \\(k\\) scales the mean by \\(k\\)."),

    # 18
    ("Find the mean of the first \\(5\\) natural numbers.",
     ["\\(3\\)", "\\(2.5\\)", "\\(3.5\\)", "\\(4\\)"],
     "A", "OSC", "easy",
     "Numbers: 1, 2, 3, 4, 5. Sum \\(= 15\\). Mean \\(= 15 / 5 = 3\\)."),

    # 19
    ("Find the mean of the first \\(6\\) whole numbers.",
     ["\\(2.5\\)", "\\(3.0\\)", "\\(3.5\\)", "\\(2.0\\)"],
     "A", "OSC", "easy",
     "Whole numbers: 0, 1, 2, 3, 4, 5. Sum \\(= 15\\). Mean \\(= 15 / 6 = 2.5\\)."),

    # 20
    ("Find the mean of the first \\(5\\) prime numbers.",
     ["\\(5.6\\)", "\\(5.0\\)", "\\(6.0\\)", "\\(4.8\\)"],
     "A", "OSC", "easy",
     "First 5 primes: 2, 3, 5, 7, 11. Sum \\(= 28\\). Mean \\(= 28 / 5 = 5.6\\)."),

    # 21
    ("If the mean of \\(2, 4, 6, 8, 10, 12\\) is \\(7\\), what is the mean of \\(4, 8, 12, 16, 20, 24\\)?",
     ["\\(14\\)", "\\(21\\)", "\\(12\\)", "\\(10\\)"],
     "A", "OSC", "easy",
     "Each number is multiplied by 2, so the mean becomes \\(7 \\times 2 = 14\\)."),

    # 22
    ("Find the class mark of the class \\(100 - 150\\).",
     ["\\(125\\)", "\\(120\\)", "\\(130\\)", "\\(50\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{100 + 150}{2} = 125\\)."),

    # 23
    ("In a school, 40 teachers have mean age 35 years. If a teacher aged 35 leaves, what is the mean age of remaining 39 teachers?",
     ["\\(35\\text{ years}\\)", "\\(34.5\\text{ years}\\)", "\\(35.5\\text{ years}\\)", "\\(36\\text{ years}\\)"],
     "A", "OSC", "easy",
     "Since the leaving teacher's age is exactly equal to the mean, the mean of the remaining teachers remains unchanged at 35 years."),

    # 24
    ("Find the value of \\(p\\) if the mean of the following data is \\(6\\): values \\(2, 4, 6, 10, p+5\\) with frequencies \\(3, 2, 3, 1, 2\\).",
     ["\\(7\\)", "\\(8\\)", "\\(6\\)", "\\(5\\)"],
     "A", "OSC", "hard",
     "\\(\\sum f_i = 3 + 2 + 3 + 1 + 2 = 11\\). \\(\\sum f_i x_i = (3 \\times 2) + (2 \\times 4) + (3 \\times 6) + (1 \\times 10) + 2(p+5) = 6 + 8 + 18 + 10 + 2p + 10 = 52 + 2p\\). \\(\\frac{52 + 2p}{11} = 6 \\implies 52 + 2p = 66 \\implies 2p = 14 \\implies p = 7\\)."),

    # 25
    ("What is an inclusive class interval system?",
     ["A system where the upper limit is included in the class (e.g. 1-10, 11-20)",
      "A system where classes are continuous",
      "A system with unequal intervals",
      "A system without frequencies"],
     "A", "OSC", "easy",
     "In an inclusive (discrete) continuous system (e.g. 1-10, 11-20), both limits belong to the interval."),

    # 26
    ("What is an exclusive class interval system?",
     ["A continuous system where the upper limit belongs to the next class (e.g. 0-10, 10-20)",
      "A system where all numbers are excluded",
      "A system with gaps",
      "A pie chart"],
     "A", "OSC", "easy",
     "In an exclusive (continuous) system (0-10, 10-20), 10 is excluded from the first class and included in the second."),

    # 27
    ("To convert inclusive classes \\(1-10, 11-20\\) into continuous exclusive classes, what adjustment is made?",
     ["Subtract 0.5 from lower limits and add 0.5 to upper limits: \\(0.5 - 10.5, 10.5 - 20.5\\)",
      "Add 1 to all limits",
      "Subtract 1 from all limits",
      "Multiply all limits by 2"],
     "A", "OSC", "easy",
     "The gap is \\(11 - 10 = 1\\). Dividing by 2 gives 0.5. Thus lower limits are reduced by 0.5 and upper limits increased by 0.5."),

    # 28
    ("Does converting inclusive classes to continuous classes change the class mark \\(x_i\\)?",
     ["No, the midpoint remains exactly identical",
      "Yes, it increases by 0.5",
      "Yes, it decreases by 0.5",
      "It doubles"],
     "A", "OSC", "easy",
     "For 1-10: \\((1+10)/2 = 5.5\\). For 0.5-10.5: \\((0.5+10.5)/2 = 5.5\\). The class mark is completely unaffected."),

    # 29
    ("Find the mean of \\(10, 20, 30, 40, 50\\).",
     ["\\(30\\)", "\\(25\\)", "\\(35\\)", "\\(40\\)"],
     "A", "OSC", "easy",
     "Sum \\(= 150\\). Mean \\(= 150 / 5 = 30\\)."),

    # 30
    ("If \\(\\sum f_i = 100\\) and \\(\\sum f_i x_i = 3450\\), find \\(\\bar{X}\\).",
     ["\\(34.5\\)", "\\(34.0\\)", "\\(35.0\\)", "\\(345\\)"],
     "A", "OSC", "easy",
     "\\(3450 / 100 = 34.5\\)."),

    # 31
    ("Find the class mark of the class \\(300 - 400\\).",
     ["\\(350\\)", "\\(100\\)", "\\(700\\)", "\\(375\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{300 + 400}{2} = 350\\)."),

    # 32
    ("The classes are: \\(0-4\\) (freq 2), \\(4-8\\) (freq 3). Find \\(\\sum f_i x_i\\).",
     ["\\(22\\)", "\\(20\\)", "\\(24\\)", "\\(18\\)"],
     "A", "OSC", "easy",
     "Class marks: 2, 6. \\(\\sum f_i x_i = (2 \\times 2) + (3 \\times 6) = 4 + 18 = 22\\)."),

    # 33
    ("In Question 32, what is the mean?",
     ["\\(4.4\\)", "\\(4.0\\)", "\\(5.0\\)", "\\(4.2\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{X} = 22 / 5 = 4.4\\)."),

    # 34
    ("Find the mean of \\(12, 14, 16, 18, 20\\).",
     ["\\(16\\)", "\\(15\\)", "\\(17\\)", "\\(18\\)"],
     "A", "OSC", "easy",
     "Symmetric AP around 16: Mean \\(= 16\\)."),

    # 35
    ("What is the algebraic sum of deviations of all observations from their arithmetic mean?",
     ["Always \\(0\\) (\\(\\sum (x_i - \\bar{X}) = 0\\))",
      "Always 1",
      "Always positive",
      "Equal to total frequency"],
     "A", "OSC", "easy",
     "A fundamental property of arithmetic mean is that the algebraic sum of deviations from the mean is always zero: \\(\\sum (x_i - \\bar{X}) = 0\\)."),

    # 36
    ("Find the mean of the first \\(10\\) odd natural numbers.",
     ["\\(10\\)", "\\(9\\)", "\\(11\\)", "\\(100\\)"],
     "A", "OSC", "easy",
     "The sum of the first \\(n\\) odd natural numbers is \\(n^2\\). Mean \\(= n^2 / n = n = 10\\)."),

    # 37
    ("Find the mean of the first \\(10\\) even natural numbers.",
     ["\\(11\\)", "\\(10\\)", "\\(12\\)", "\\(20\\)"],
     "A", "OSC", "easy",
     "Sum \\(= n(n+1) = 10 \\times 11 = 110\\). Mean \\(= 110 / 10 = 11\\)."),

    # 38
    ("If the mean of 5 observations is 12, what is the sum of these 5 observations?",
     ["\\(60\\)", "\\(50\\)", "\\(12\\)", "\\(72\\)"],
     "A", "OSC", "easy",
     "Sum \\(= 5 \\times 12 = 60\\)."),

    # 39
    ("If the mean of 20 observations is 15, and 2 new observations with values 25 and 35 are added, what is the new mean of the 22 observations?",
     ["\\(16.36\\)", "\\(16.00\\)", "\\(15.50\\)", "\\(17.00\\)"],
     "A", "OSC", "medium",
     "Initial sum \\(= 20 \\times 15 = 300\\). New sum \\(= 300 + 25 + 35 = 360\\). New mean \\(= 360 / 22 = 16.36\\)."),

    # 40
    ("What is the primary advantage of the Direct Method?",
     ["Simple, direct calculation suitable when numbers and frequencies are small",
      "Requires no calculations",
      "Eliminates fractions",
      "Always gives integer answers"],
     "A", "OSC", "easy",
     "The Direct Method is straightforward and intuitive when class marks and frequencies are relatively small integers.")
]

t61_prac = [
    # 41
    ("Find the class mark of the class \\(50 - 60\\).",
     ["\\(55\\)", "\\(50\\)", "\\(60\\)", "\\(10\\)"],
     "A", "OSC", "easy",
     "\\((50 + 60)/2 = 55\\)."),

    # 42
    ("Find the class mark of the class \\(75 - 85\\).",
     ["\\(80\\)", "\\(75\\)", "\\(85\\)", "\\(10\\)"],
     "A", "OSC", "easy",
     "\\((75 + 85)/2 = 80\\)."),

    # 43
    ("If \\(\\sum f_i x_i = 840\\) and \\(\\sum f_i = 40\\), find the mean.",
     ["\\(21\\)", "\\(20\\)", "\\(22\\)", "\\(24\\)"],
     "A", "OSC", "easy",
     "\\(840 / 40 = 21\\)."),

    # 44
    ("Find the mean of \\(3, 5, 7, 9, 11\\).",
     ["\\(7\\)", "\\(6\\)", "\\(8\\)", "\\(5\\)"],
     "A", "OSC", "easy",
     "Mean is the middle term 7."),

    # 45
    ("If the mean of \\(4, 7, 8, x\\) is \\(6\\), find \\(x\\).",
     ["\\(5\\)", "\\(6\\)", "\\(4\\)", "\\(7\\)"],
     "A", "OSC", "easy",
     "\\(19 + x = 24 \\implies x = 5\\)."),

    # 46
    ("Find the class size of \\(25 - 35\\).",
     ["\\(10\\)", "\\(30\\)", "\\(5\\)", "\\(20\\)"],
     "A", "OSC", "easy",
     "\\(35 - 25 = 10\\)."),

    # 47
    ("Classes are \\(0-10\\) (freq 4) and \\(10-20\\) (freq 6). Find the mean.",
     ["\\(11\\)", "\\(10\\)", "\\(12\\)", "\\(15\\)"],
     "A", "OSC", "easy",
     "\\(\\sum f_i x_i = 4(5) + 6(15) = 20 + 90 = 110\\). \\(N = 10\\). \\(\\bar{X} = 110 / 10 = 11\\)."),

    # 48
    ("If the mean of 10 observations is 25, find their sum.",
     ["\\(250\\)", "\\(25\\)", "\\(500\\)", "\\(100\\)"],
     "A", "OSC", "easy",
     "\\(10 \\times 25 = 250\\)."),

    # 49
    ("Find the class mark of \\(12.5 - 17.5\\).",
     ["\\(15\\)", "\\(14\\)", "\\(16\\)", "\\(5\\)"],
     "A", "OSC", "easy",
     "\\((12.5 + 17.5)/2 = 15\\)."),

    # 50
    ("If \\(\\sum f_i x_i = 480\\) and mean is \\(12\\), find \\(\\sum f_i\\).",
     ["\\(40\\)", "\\(48\\)", "\\(36\\)", "\\(50\\)"],
     "A", "OSC", "easy",
     "\\(N = 480 / 12 = 40\\)."),

    # 51
    ("Find the mean of the first 4 multiples of 5 (5, 10, 15, 20).",
     ["\\(12.5\\)", "\\(10\\)", "\\(15\\)", "\\(12\\)"],
     "A", "OSC", "easy",
     "\\(50 / 4 = 12.5\\)."),

    # 52
    ("Find the mean of \\(1, 2, 3, 4, 5, 6, 7\\).",
     ["\\(4\\)", "\\(3.5\\)", "\\(4.5\\)", "\\(5\\)"],
     "A", "OSC", "easy",
     "Middle term is 4."),

    # 53
    ("If the mean of \\(x, x+1, x+2\\) is \\(10\\), find \\(x\\).",
     ["\\(9\\)", "\\(10\\)", "\\(8\\)", "\\(11\\)"],
     "A", "OSC", "easy",
     "Middle term \\(x + 1 = 10 \\implies x = 9\\)."),

    # 54
    ("Find the class mark of \\(80 - 100\\).",
     ["\\(90\\)", "\\(20\\)", "\\(85\\)", "\\(95\\)"],
     "A", "OSC", "easy",
     "\\((80 + 100)/2 = 90\\)."),

    # 55
    ("If each of 10 observations is decreased by 4, the mean decreases by:",
     ["\\(4\\)", "\\(40\\)", "\\(0.4\\)", "\\(0\\)"],
     "A", "OSC", "easy",
     "Subtracting 4 from all numbers reduces the mean by 4."),

    # 56
    ("If \\(\\sum f_i x_i = 600\\) and \\(\\sum f_i = 25\\), find the mean.",
     ["\\(24\\)", "\\(25\\)", "\\(20\\)", "\\(22\\)"],
     "A", "OSC", "easy",
     "\\(600 / 25 = 24\\)."),

    # 57
    ("What is the class width of \\(100 - 125\\)?",
     ["\\(25\\)", "\\(112.5\\)", "\\(50\\)", "\\(12.5\\)"],
     "A", "OSC", "easy",
     "\\(125 - 100 = 25\\)."),

    # 58
    ("Find the class mark of \\(100 - 125\\).",
     ["\\(112.5\\)", "\\(25\\)", "\\(110\\)", "\\(115\\)"],
     "A", "OSC", "easy",
     "\\((100 + 125)/2 = 112.5\\)."),

    # 59
    ("If 5 students score 20, 30, 40, 50, 60, find their average score.",
     ["\\(40\\)", "\\(35\\)", "\\(45\\)", "\\(50\\)"],
     "A", "OSC", "easy",
     "Average is 40."),

    # 60
    ("If the mean of \\(3, 4, 8, 5, x, 3, 2, 1\\) is \\(4\\), find \\(x\\).",
     ["\\(6\\)", "\\(5\\)", "\\(7\\)", "\\(4\\)"],
     "A", "OSC", "easy",
     "Sum \\(= 26 + x = 4 \\times 8 = 32 \\implies x = 6\\)."),

    # 61
    ("Find the class mark of \\(0 - 50\\).",
     ["\\(25\\)", "\\(50\\)", "\\(0\\)", "\\(10\\)"],
     "A", "OSC", "easy",
     "\\(50 / 2 = 25\\)."),

    # 62
    ("Find the class mark of \\(50 - 100\\).",
     ["\\(75\\)", "\\(50\\)", "\\(70\\)", "\\(80\\)"],
     "A", "OSC", "easy",
     "\\(150 / 2 = 75\\)."),

    # 63
    ("If \\(\\sum f_i x_i = 1500\\) and \\(N = 60\\), find \\(\\bar{X}\\).",
     ["\\(25\\)", "\\(20\\)", "\\(30\\)", "\\(24\\)"],
     "A", "OSC", "easy",
     "\\(1500 / 60 = 25\\)."),

    # 64
    ("Find the mean of \\(2, 4, 6, 8\\).",
     ["\\(5\\)", "\\(4\\)", "\\(6\\)", "\\(4.5\\)"],
     "A", "OSC", "easy",
     "\\(20 / 4 = 5\\)."),

    # 65
    ("Find the mean of \\(1, 3, 5, 7\\).",
     ["\\(4\\)", "\\(3\\)", "\\(5\\)", "\\(4.5\\)"],
     "A", "OSC", "easy",
     "\\(16 / 4 = 4\\)."),

    # 66
    ("If \\(\\sum f_i = 20\\) and \\(\\bar{X} = 15\\), what is \\(\\sum f_i x_i\\)?",
     ["\\(300\\)", "\\(200\\)", "\\(150\\)", "\\(350\\)"],
     "A", "OSC", "easy",
     "\\(20 \\times 15 = 300\\)."),

    # 67
    ("Find the class mark of \\(200 - 250\\).",
     ["\\(225\\)", "\\(50\\)", "\\(220\\)", "\\(230\\)"],
     "A", "OSC", "easy",
     "\\(450 / 2 = 225\\)."),

    # 68
    ("What is the class width of \\(200 - 250\\)?",
     ["\\(50\\)", "\\(225\\)", "\\(25\\)", "\\(100\\)"],
     "A", "OSC", "easy",
     "\\(250 - 200 = 50\\)."),

    # 69
    ("The classes are \\(10-14\\) (freq 2), \\(15-19\\) (freq 3). What is the class mark of the first class?",
     ["\\(12\\)", "\\(10\\)", "\\(14\\)", "\\(12.5\\)"],
     "A", "OSC", "easy",
     "\\((10 + 14)/2 = 12\\)."),

    # 70
    ("In Question 69, what is the class mark of the second class?",
     ["\\(17\\)", "\\(15\\)", "\\(19\\)", "\\(16.5\\)"],
     "A", "OSC", "easy",
     "\\((15 + 19)/2 = 17\\).")
]

t61_mock = [
    # 71
    ("What does arithmetic mean measure?",
     ["The central tendency or average of a data set",
      "The spread of the data",
      "The highest frequency",
      "The median value"],
     "A", "OSC", "easy",
     "Mean is a primary measure of central tendency representing the mathematical average."),

    # 72
    ("What is a class interval in grouped data?",
     ["A range or group into which continuous data is divided",
      "The frequency of an observation",
      "The total number of students",
      "A pie slice"],
     "A", "OSC", "easy",
     "A class interval is a sub-range of data values used to group large frequency distributions."),

    # 73
    ("What does \\(x_i\\) denote in the Direct Method formula?",
     ["The class mark (midpoint) of the \\(i^{\\text{th}}\\) class interval",
      "The frequency of the class",
      "The cumulative frequency",
      "The lower limit"],
     "A", "OSC", "easy",
     "\\(x_i\\) represents the class mark (representative midpoint value) of each interval."),

    # 74
    ("What does \\(f_i\\) denote in frequency distribution?",
     ["The frequency (number of observations) in the \\(i^{\\text{th}}\\) class",
      "The class mark",
      "The lower limit",
      "The class size"],
     "A", "OSC", "easy",
     "\\(f_i\\) is the frequency of occurrence in the \\(i^{\\text{th}}\\) interval."),

    # 75
    ("What does the symbol \\(\\sum\\) (sigma) indicate?",
     ["Summation (sum of all terms)", "Multiplication", "Division", "Square root"],
     "A", "OSC", "easy",
     "\\(\\sum\\) is the Greek capital letter sigma used to represent mathematical summation."),

    # 76
    ("What is the class mark of \\(0 - 10\\)?",
     ["\\(5\\)", "\\(10\\)", "\\(0\\)", "\\(2.5\\)"],
     "A", "OSC", "easy",
     "\\((0 + 10)/2 = 5\\)."),

    # 77
    ("What is the class mark of \\(10 - 20\\)?",
     ["\\(15\\)", "\\(10\\)", "\\(20\\)", "\\(5\\)"],
     "A", "OSC", "easy",
     "\\((10 + 20)/2 = 15\\)."),

    # 78
    ("If \\(f_1 = 2\\) and \\(x_1 = 5\\), what is \\(f_1 x_1\\)?",
     ["\\(10\\)", "\\(7\\)", "\\(2.5\\)", "\\(3\\)"],
     "A", "OSC", "easy",
     "\\(2 \\times 5 = 10\\)."),

    # 79
    ("Can the mean of positive numbers ever be negative?",
     ["No, the average of positive numbers must always be positive",
      "Yes, if frequencies are large",
      "Yes, in grouped data",
      "Only for fractions"],
     "A", "OSC", "easy",
     "The mean of strictly positive values is always strictly positive."),

    # 80
    ("If all values in a dataset are \\(8\\), what is the mean?",
     ["\\(8\\)", "\\(0\\)", "\\(16\\)", "\\(4\\)"],
     "A", "OSC", "easy",
     "If all observations are identical to a constant \\(k\\), the mean is \\(k = 8\\)."),

    # 81
    ("What is the average of \\(0\\) and \\(100\\)?",
     ["\\(50\\)", "\\(100\\)", "\\(0\\)", "\\(25\\)"],
     "A", "OSC", "easy",
     "\\((0 + 100)/2 = 50\\)."),

    # 82
    ("Why do we use class marks in grouped data calculations?",
     ["Because individual raw data values within the interval are lost, so the midpoint represents the interval",
      "Because computers cannot multiply decimals",
      "Because frequencies must be even",
      "To make numbers bigger"],
     "A", "OSC", "easy",
     "In grouped data, the exact individual values are grouped together, so the class mark acts as the best representative value for all data in that interval.")
]

if __name__ == "__main__":
    topic_code = "MH-10-MTH1-6-6.1"
    all_qs = build_topic_questions(topic_code, t61_exam, t61_prac, t61_mock)
    out_path = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch6_t1.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {topic_code} -> {out_path}")
