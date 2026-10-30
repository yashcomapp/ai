# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 6: Statistics - Topic 6.2: Assumed Mean & Step Deviation Methods (MH-10-MTH1-6-6.2)
Total: 82 Canonical Questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# TOPIC 6.2: Mean by Assumed Mean Method & Step Deviation Method
t62_exam = [
    # 1
    ("What is the formula to calculate the Mean (\\(\\bar{X}\\)) using the Assumed Mean Method?",
     ["\\(\\bar{X} = A + \\bar{d} = A + \\frac{\\sum f_i d_i}{\\sum f_i}\\)",
      "\\(\\bar{X} = A - \\frac{\\sum f_i d_i}{\\sum f_i}\\)",
      "\\(\\bar{X} = \\frac{\\sum f_i d_i}{\\sum f_i}\\)",
      "\\(\\bar{X} = A \\times \\frac{\\sum f_i d_i}{N}\\)"],
     "A", "OSC", "easy",
     "In the Assumed Mean Method, \\(\\bar{X} = A + \\bar{d}\\), where \\(A\\) is the assumed mean and \\(\\bar{d} = \\frac{\\sum f_i d_i}{\\sum f_i}\\)."),

    # 2
    ("How is the deviation (\\(d_i\\)) calculated in the Assumed Mean Method?",
     ["\\(d_i = x_i - A\\)", "\\(d_i = A - x_i\\)", "\\(d_i = x_i + A\\)", "\\(d_i = \\frac{x_i}{A}\\)"],
     "A", "OSC", "easy",
     "Deviation \\(d_i\\) is the difference between each class mark \\(x_i\\) and the assumed mean \\(A\\): \\(d_i = x_i - A\\)."),

    # 3
    ("From which column is the Assumed Mean \\(A\\) usually chosen?",
     ["Class Marks (\\(x_i\\)), typically a central or median class mark",
      "Frequencies (\\(f_i\\))",
      "Cumulative frequencies",
      "Class sizes"],
     "A", "OSC", "easy",
     "The assumed mean \\(A\\) is selected from the middle values of the class mark column \\(x_i\\) to keep deviations small and balanced."),

    # 4
    ("What is the formula to calculate the Mean (\\(\\bar{X}\\)) using the Step Deviation Method?",
     ["\\(\\bar{X} = A + (\\bar{u} \\times g)\\) where \\(\\bar{u} = \\frac{\\sum f_i u_i}{\\sum f_i}\\)",
      "\\(\\bar{X} = A + \\bar{u}\\)",
      "\\(\\bar{X} = A - (\\bar{u} \\times g)\\)",
      "\\(\\bar{X} = \\bar{u} \\times g\\)"],
     "A", "OSC", "easy",
     "In the Step Deviation Method, \\(u_i = \\frac{d_i}{g}\\), \\(\\bar{u} = \\frac{\\sum f_i u_i}{\\sum f_i}\\), and \\(\\bar{X} = A + \\bar{u} \\cdot g\\), where \\(g\\) is the common factor of deviations."),

    # 5
    ("How is the step-deviation variable \\(u_i\\) defined?",
     ["\\(u_i = \\frac{x_i - A}{g} = \\frac{d_i}{g}\\)",
      "\\(u_i = (x_i - A) \\times g\\)",
      "\\(u_i = x_i + g\\)",
      "\\(u_i = \\frac{f_i}{g}\\)"],
     "A", "OSC", "easy",
     "\\(u_i\\) scales down the deviations by dividing by the common class width or greatest common divisor \\(g\\): \\(u_i = \\frac{d_i}{g}\\)."),

    # 6
    ("In an Assumed Mean calculation: \\(A = 300, \\sum f_i = 50, \\sum f_i d_i = 420\\). Find the Mean \\(\\bar{X}\\).",
     ["\\(308.4\\)", "\\(308.0\\)", "\\(310.0\\)", "\\(291.6\\)"],
     "A", "OSC", "medium",
     "\\(\\bar{d} = \\frac{\\sum f_i d_i}{\\sum f_i} = \\frac{420}{50} = 8.4\\). \\(\\bar{X} = A + \\bar{d} = 300 + 8.4 = 308.4\\)."),

    # 7
    ("In an Assumed Mean calculation: \\(A = 50, \\sum f_i = 40, \\sum f_i d_i = -120\\). Find the Mean \\(\\bar{X}\\).",
     ["\\(47\\)", "\\(53\\)", "\\(48\\)", "\\(46.5\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{d} = \\frac{-120}{40} = -3\\). \\(\\bar{X} = A + \\bar{d} = 50 + (-3) = 47\\)."),

    # 8
    ("In a Step Deviation calculation: \\(A = 25, g = 10, \\sum f_i = 100, \\sum f_i u_i = 15\\). Find the Mean \\(\\bar{X}\\).",
     ["\\(26.5\\)", "\\(25.15\\)", "\\(27.0\\)", "\\(26.0\\)"],
     "A", "OSC", "medium",
     "\\(\\bar{u} = \\frac{15}{100} = 0.15\\). \\(\\bar{X} = A + (\\bar{u} \\times g) = 25 + (0.15 \\times 10) = 25 + 1.5 = 26.5\\)."),

    # 9
    ("In a Step Deviation calculation: \\(A = 150, g = 20, \\sum f_i = 50, \\sum f_i u_i = -8\\). Find the Mean \\(\\bar{X}\\).",
     ["\\(146.8\\)", "\\(153.2\\)", "\\(147.0\\)", "\\(145.5\\)"],
     "A", "OSC", "medium",
     "\\(\\bar{u} = -8 / 50 = -0.16\\). \\(\\bar{X} = 150 + (-0.16 \\times 20) = 150 - 3.2 = 146.8\\)."),

    # 10
    ("Do the Direct Method, Assumed Mean Method, and Step Deviation Method yield different values of the Mean for the same dataset?",
     ["No, all three methods mathematically yield the EXACT same Mean",
      "Yes, Step Deviation gives higher accuracy",
      "Yes, Assumed Mean always rounds off decimals",
      "Direct method is always 10% smaller"],
     "A", "OSC", "easy",
     "All three methods are algebraically equivalent transformations of the arithmetic mean formula and always yield identical values."),

    # 11
    ("Why is the Step Deviation Method preferred when dealing with large numbers and large frequencies?",
     ["It simplifies calculations by reducing large numbers into small integers (like -2, -1, 0, 1, 2)",
      "It eliminates the need to draw tables",
      "It guarantees no decimals in the final answer",
      "It requires no multiplication"],
     "A", "OSC", "easy",
     "Dividing deviations by common factor \\(g\\) reduces large numbers to small single-digit integers, minimizing calculation errors."),

    # 12
    ("What are the 5 columns used in the Assumed Mean Method table?",
     ["Class Interval, Class Mark (\\(x_i\\)), Deviation (\\(d_i = x_i - A\\)), Frequency (\\(f_i\\)), Product (\\(f_i d_i\\))",
      "Class Interval, Midpoint, Cumulative frequency, Frequency, Log",
      "Class, Frequency, Cumulative frequency, Mode, Mean",
      "Lower limit, Upper limit, Deviation, Square, Frequency"],
     "A", "OSC", "easy",
     "The Assumed Mean table has 5 standard columns: Class, \\(x_i\\), \\(d_i = x_i - A\\), \\(f_i\\), and \\(f_i d_i\\)."),

    # 13
    ("What are the 6 columns used in the Step Deviation Method table?",
     ["Class, Class Mark (\\(x_i\\)), Deviation (\\(d_i\\)), Reduced variable (\\(u_i = d_i/g\\)), Frequency (\\(f_i\\)), Product (\\(f_i u_i\\))",
      "Class, Frequency, Cumulative frequency, Rank, Deviation, Mean",
      "Lower limit, Upper limit, \\(u_i\\), \\(f_i\\), \\(x_i\\), \\(cf\\)",
      "Class, Midpoint, Angle, Percent, Frequency, Product"],
     "A", "OSC", "easy",
     "The Step Deviation table has 6 columns: Class, \\(x_i\\), \\(d_i\\), \\(u_i = d_i/g\\), \\(f_i\\), and \\(f_i u_i\\)."),

    # 14
    ("If the class marks are \\(15, 25, 35, 45, 55\\) and \\(A = 35\\), what are the deviations \\(d_i\\)?",
     ["\\(-20, -10, 0, 10, 20\\)", "\\(10, 20, 30, 40, 50\\)", "\\(-2, -1, 0, 1, 2\\)", "\\(0, 10, 20, 30, 40\\)"],
     "A", "OSC", "easy",
     "\\(d_i = x_i - 35\\): \\(15-35 = -20\\), \\(25-35 = -10\\), \\(35-35 = 0\\), \\(45-35 = 10\\), \\(55-35 = 20\\)."),

    # 15
    ("In Question 14, if \\(g = 10\\), what are the reduced step-deviation values \\(u_i\\)?",
     ["\\(-2, -1, 0, 1, 2\\)", "\\(-20, -10, 0, 10, 20\\)", "\\(-1, 0, 1, 2, 3\\)", "\\(1, 2, 3, 4, 5\\)"],
     "A", "OSC", "easy",
     "\\(u_i = d_i / 10\\): \\(-20/10 = -2\\), \\(-10/10 = -1\\), \\(0/10 = 0\\), \\(10/10 = 1\\), \\(20/10 = 2\\)."),

    # 16
    ("If \\(A = 225, g = 50, \\bar{u} = -0.2\\), find the Mean \\(\\bar{X}\\).",
     ["\\(215\\)", "\\(235\\)", "\\(220\\)", "\\(224.8\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{X} = A + (\\bar{u} \\times g) = 225 + (-0.2 \\times 50) = 225 - 10 = 215\\)."),

    # 17
    ("The daily wages of 50 workers have \\(A = 250\\) and \\(\\sum f_i d_i = 1000\\). What is the mean wage?",
     ["₹270", "₹260", "₹250", "₹280"],
     "A", "OSC", "easy",
     "\\(\\bar{d} = 1000 / 50 = 20\\). \\(\\bar{X} = 250 + 20 = ₹270\\)."),

    # 18
    ("In a survey, \\(A = 70, \\sum f_i = 80, \\sum f_i d_i = 0\\). What is the Mean?",
     ["\\(70\\)", "\\(0\\)", "\\(80\\)", "\\(1\\)"],
     "A", "OSC", "easy",
     "When \\(\\sum f_i d_i = 0\\), \\(\\bar{d} = 0\\), so the mean equals the assumed mean \\(A = 70\\)."),

    # 19
    ("Can the assumed mean \\(A\\) be chosen as any real number, even one not in the class marks?",
     ["Yes, any number can mathematically be chosen as A, but choosing a central class mark simplifies computation",
      "No, A must be the smallest class mark",
      "No, A must be the largest frequency",
      "No, A must be an integer ending in 0"],
     "A", "OSC", "easy",
     "Mathematically any value of \\(A\\) yields the correct mean, but choosing a central class mark produces balanced positive and negative deviations that cancel out."),

    # 20
    ("If the deviations \\(d_i\\) are \\(-100, -50, 0, 50, 100\\), what is the most convenient value of \\(g\\)?",
     ["\\(50\\)", "\\(10\\)", "\\(100\\)", "\\(25\\)"],
     "A", "OSC", "easy",
     "The greatest common divisor of all deviations is \\(g = 50\\), reducing them to \\(-2, -1, 0, 1, 2\\)."),

    # 21
    ("If \\(A = 500, g = 100, \\bar{u} = 0.45\\), what is \\(\\bar{X}\\)?",
     ["\\(545\\)", "\\(54.5\\)", "\\(504.5\\)", "\\(550\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{X} = 500 + (0.45 \\times 100) = 500 + 45 = 545\\)."),

    # 22
    ("A table has \\(N = 120, A = 18, \\sum f_i d_i = -36\\). Find the Mean.",
     ["\\(17.7\\)", "\\(18.3\\)", "\\(17.5\\)", "\\(18.0\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{d} = -36 / 120 = -0.3\\). \\(\\bar{X} = 18 + (-0.3) = 17.7\\)."),

    # 23
    ("What happens to \\(u_i\\) when \\(x_i = A\\)?",
     ["\\(u_i = 0\\)", "\\(u_i = 1\\)", "\\(u_i = A\\)", "\\(u_i = g\\)"],
     "A", "OSC", "easy",
     "When \\(x_i = A\\), \\(d_i = 0\\), so \\(u_i = 0/g = 0\\)."),

    # 24
    ("If class marks are \\(125, 175, 225, 275, 325\\), what is the class width \\(g\\)?",
     ["\\(50\\)", "\\(25\\)", "\\(100\\)", "\\(75\\)"],
     "A", "OSC", "easy",
     "The difference between consecutive class marks is \\(175 - 125 = 50\\)."),

    # 25
    ("In an assumed mean calculation, if \\(\\sum f_i d_i\\) is positive, is the true mean greater than or less than \\(A\\)?",
     ["Greater than \\(A\\)", "Less than \\(A\\)", "Equal to \\(A\\)", "Zero"],
     "A", "OSC", "easy",
     "Since \\(\\bar{X} = A + \\bar{d}\\) and \\(\\bar{d} > 0\\), the true mean is strictly greater than \\(A\\)."),

    # 26
    ("In an assumed mean calculation, if \\(\\sum f_i d_i\\) is negative, is the true mean greater than or less than \\(A\\)?",
     ["Less than \\(A\\)", "Greater than \\(A\\)", "Equal to \\(A\\)", "Zero"],
     "A", "OSC", "easy",
     "Since \\(\\bar{d} < 0\\), \\(\\bar{X} = A + \\bar{d} < A\\)."),

    # 27
    ("For classes \\(0-20, 20-40, 40-60, 60-80, 80-100\\), what is the most logical assumed mean \\(A\\)?",
     ["\\(50\\) (midpoint of central class 40-60)", "\\(10\\)", "\\(90\\)", "\\(30\\)"],
     "A", "OSC", "easy",
     "Class marks are 10, 30, 50, 70, 90. The central value is 50, which is the most logical choice for \\(A\\)."),

    # 28
    ("In Question 27, what is \\(g\\)?",
     ["\\(20\\)", "\\(10\\)", "\\(50\\)", "\\(40\\)"],
     "A", "OSC", "easy",
     "The common class width is \\(20 - 0 = 20\\)."),

    # 29
    ("In Question 27 with \\(A = 50\\) and \\(g = 20\\), what are the values of \\(u_i\\)?",
     ["\\(-2, -1, 0, 1, 2\\)", "\\(-1, 0, 1, 2, 3\\)", "\\(-4, -2, 0, 2, 4\\)", "\\(1, 2, 3, 4, 5\\)"],
     "A", "OSC", "easy",
     "Deviations are -40, -20, 0, 20, 40. Dividing by 20 gives \\(-2, -1, 0, 1, 2\\)."),

    # 30
    ("If \\(A = 40, \\sum f_i = 25, \\sum f_i d_i = 75\\), find \\(\\bar{X}\\).",
     ["\\(43\\)", "\\(42\\)", "\\(44\\)", "\\(45\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{d} = 75 / 25 = 3\\). \\(\\bar{X} = 40 + 3 = 43\\)."),

    # 31
    ("If \\(A = 100, g = 10, \\bar{u} = 1.2\\), find \\(\\bar{X}\\).",
     ["\\(112\\)", "\\(101.2\\)", "\\(120\\)", "\\(110\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{X} = 100 + (1.2 \\times 10) = 100 + 12 = 112\\)."),

    # 32
    ("If \\(A = 100, g = 10, \\bar{u} = -1.5\\), find \\(\\bar{X}\\).",
     ["\\(85\\)", "\\(98.5\\)", "\\(95\\)", "\\(80\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{X} = 100 + (-1.5 \\times 10) = 100 - 15 = 85\\)."),

    # 33
    ("In an assumed mean problem: \\(A = 200, N = 50\\). If \\(\\bar{X} = 204\\), what is \\(\\sum f_i d_i\\)?",
     ["\\(200\\)", "\\(4\\)", "\\(50\\)", "\\(400\\)"],
     "A", "OSC", "medium",
     "\\(\\bar{d} = \\bar{X} - A = 204 - 200 = 4\\). \\(\\sum f_i d_i = N \\times \\bar{d} = 50 \\times 4 = 200\\)."),

    # 34
    ("In a step deviation problem: \\(A = 50, g = 10, N = 40\\). If \\(\\bar{X} = 52.5\\), what is \\(\\sum f_i u_i\\)?",
     ["\\(10\\)", "\\(2.5\\)", "\\(25\\)", "\\(40\\)"],
     "A", "OSC", "medium",
     "\\(\\bar{u} \\times 10 = 52.5 - 50 = 2.5 \\implies \\bar{u} = 0.25\\). \\(\\sum f_i u_i = N \\times \\bar{u} = 40 \\times 0.25 = 10\\)."),

    # 35
    ("What condition is necessary to apply the Step Deviation Method conveniently?",
     ["All class intervals should have equal width (or deviations should have a common divisor)",
      "All frequencies must be equal",
      "There must be an odd number of classes",
      "Data must be discrete"],
     "A", "OSC", "easy",
     "Step deviation requires deviations to have a common factor \\(g\\), which naturally happens when class intervals have uniform width."),

    # 36
    ("If class intervals have unequal widths, which method is generally preferred over Step Deviation?",
     ["Direct Method or Assumed Mean Method", "Pie Chart", "Median formula", "Empirical rule"],
     "A", "OSC", "easy",
     "When class intervals are unequal, common factor \\(g\\) does not exist uniformly, making Direct or Assumed Mean methods more appropriate."),

    # 37
    ("If \\(d_i = x_i - 150\\), what is the assumed mean?",
     ["\\(150\\)", "\\(0\\)", "\\(x_i\\)", "\\(75\\)"],
     "A", "OSC", "easy",
     "Comparing with \\(d_i = x_i - A\\), \\(A = 150\\)."),

    # 38
    ("If \\(u_i = \\frac{x_i - 75}{10}\\), what are \\(A\\) and \\(g\\)?",
     ["\\(A = 75, g = 10\\)", "\\(A = 10, g = 75\\)", "\\(A = -75, g = 10\\)", "\\(A = 75, g = 1\\)"],
     "A", "OSC", "easy",
     "Comparing with \\(u_i = \\frac{x_i - A}{g}\\), \\(A = 75\\) and \\(g = 10\\)."),

    # 39
    ("If \\(u_i = \\frac{x_i - 200}{50}\\) and \\(\\bar{u} = 0\\), what is the Mean \\(\\bar{X}\\)?",
     ["\\(200\\)", "\\(0\\)", "\\(250\\)", "\\(50\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{X} = A + \\bar{u} \\cdot g = 200 + 0 = 200\\)."),

    # 40
    ("Who introduced the Step Deviation technique in grouped data calculations?",
     ["Classical statisticians to simplify hand calculations before modern calculators",
      "Ancient Greek astronomers",
      "Bankers in New York",
      "Computer scientists in 1990"],
     "A", "OSC", "easy",
     "Short-cut and step-deviation methods were developed by statisticians to make large-scale arithmetic computations manageable by hand.")
]

t62_prac = [
    # 41
    ("If \\(A = 20, N = 30, \\sum f_i d_i = 60\\), find \\(\\bar{X}\\).",
     ["\\(22\\)", "\\(20\\)", "\\(24\\)", "\\(26\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{d} = 60/30 = 2\\). \\(\\bar{X} = 20 + 2 = 22\\)."),

    # 42
    ("If \\(A = 45, N = 50, \\sum f_i d_i = -50\\), find \\(\\bar{X}\\).",
     ["\\(44\\)", "\\(46\\)", "\\(45\\)", "\\(43\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{d} = -50/50 = -1\\). \\(\\bar{X} = 45 - 1 = 44\\)."),

    # 43
    ("If \\(A = 30, g = 5, \\bar{u} = 2\\), find \\(\\bar{X}\\).",
     ["\\(40\\)", "\\(35\\)", "\\(32\\)", "\\(45\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{X} = 30 + (2 \\times 5) = 40\\)."),

    # 44
    ("If \\(A = 60, g = 10, \\bar{u} = -1.2\\), find \\(\\bar{X}\\).",
     ["\\(48\\)", "\\(58.8\\)", "\\(50\\)", "\\(52\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{X} = 60 - 12 = 48\\)."),

    # 45
    ("Class marks are \\(10, 20, 30, 40, 50\\). If \\(A = 30\\), what is \\(d_1\\)?",
     ["\\(-20\\)", "\\(20\\)", "\\(-10\\)", "\\(0\\)"],
     "A", "OSC", "easy",
     "\\(d_1 = 10 - 30 = -20\\)."),

    # 46
    ("In Question 45, what is \\(d_5\\)?",
     ["\\(20\\)", "\\(-20\\)", "\\(10\\)", "\\(50\\)"],
     "A", "OSC", "easy",
     "\\(d_5 = 50 - 30 = 20\\)."),

    # 47
    ("In Question 45, if \\(g = 10\\), what is \\(u_1\\)?",
     ["\\(-2\\)", "\\(-20\\)", "\\(2\\)", "\\(1\\)"],
     "A", "OSC", "easy",
     "\\(u_1 = -20 / 10 = -2\\)."),

    # 48
    ("If \\(A = 15, \\sum f_i d_i = 0\\), what is \\(\\bar{X}\\)?",
     ["\\(15\\)", "\\(0\\)", "\\(30\\)", "\\(1\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{X} = 15 + 0 = 15\\)."),

    # 49
    ("If \\(\\bar{X} = 55\\) and \\(A = 50\\), what is \\(\\bar{d}\\)?",
     ["\\(5\\)", "\\(-5\\)", "\\(105\\)", "\\(0\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{d} = 55 - 50 = 5\\)."),

    # 50
    ("If \\(\\bar{X} = 42\\) and \\(A = 45\\), what is \\(\\bar{d}\\)?",
     ["\\(-3\\)", "\\(3\\)", "\\(87\\)", "\\(0\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{d} = 42 - 45 = -3\\)."),

    # 51
    ("If \\(A = 70, g = 5, \\bar{X} = 75\\), what is \\(\\bar{u}\\)?",
     ["\\(1\\)", "\\(5\\)", "\\(0.5\\)", "\\(2\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{u} \\times 5 = 75 - 70 = 5 \\implies \\bar{u} = 1\\)."),

    # 52
    ("If \\(A = 70, g = 5, \\bar{X} = 65\\), what is \\(\\bar{u}\\)?",
     ["\\(-1\\)", "\\(1\\)", "\\(-5\\)", "\\(-2\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{u} \\times 5 = 65 - 70 = -5 \\implies \\bar{u} = -1\\)."),

    # 53
    ("What is the deviation of the assumed mean \\(A\\) from itself?",
     ["\\(0\\)", "\\(1\\)", "\\(A\\)", "\\(-A\\)"],
     "A", "OSC", "easy",
     "\\(A - A = 0\\)."),

    # 54
    ("If \\(A = 120, N = 40, \\sum f_i d_i = 80\\), find \\(\\bar{X}\\).",
     ["\\(122\\)", "\\(120\\)", "\\(124\\)", "\\(121\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{d} = 80/40 = 2\\). \\(\\bar{X} = 120 + 2 = 122\\)."),

    # 55
    ("If \\(A = 120, N = 40, \\sum f_i d_i = -80\\), find \\(\\bar{X}\\).",
     ["\\(118\\)", "\\(120\\)", "\\(116\\)", "\\(122\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{X} = 120 - 2 = 118\\)."),

    # 56
    ("In Step Deviation, what is \\(g\\) called?",
     ["Class size or common factor of deviations", "Frequency", "Median", "Assumed mean"],
     "A", "OSC", "easy",
     "\\(g\\) is the common divisor or class width."),

    # 57
    ("If \\(A = 500, g = 50, N = 20, \\sum f_i u_i = 6\\), find \\(\\bar{X}\\).",
     ["\\(515\\)", "\\(506\\)", "\\(530\\)", "\\(512\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{u} = 6/20 = 0.3\\). \\(\\bar{X} = 500 + (0.3 \\times 50) = 515\\)."),

    # 58
    ("If \\(A = 500, g = 50, N = 20, \\sum f_i u_i = -6\\), find \\(\\bar{X}\\).",
     ["\\(485\\)", "\\(494\\)", "\\(470\\)", "\\(488\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{X} = 500 - 15 = 485\\)."),

    # 59
    ("If class marks are \\(25, 75, 125, 175, 225\\), what is the middle value to choose as \\(A\\)?",
     ["\\(125\\)", "\\(75\\)", "\\(175\\)", "\\(25\\)"],
     "A", "OSC", "easy",
     "The central term is 125."),

    # 60
    ("In Question 59, what is the common factor \\(g\\)?",
     ["\\(50\\)", "\\(25\\)", "\\(100\\)", "\\(75\\)"],
     "A", "OSC", "easy",
     "\\(75 - 25 = 50\\)."),

    # 61
    ("In Question 59 with \\(A = 125\\) and \\(g = 50\\), what is \\(u_4\\)?",
     ["\\(1\\)", "\\(2\\)", "\\(0\\)", "\\(-1\\)"],
     "A", "OSC", "easy",
     "\\(x_4 = 175 \\implies d_4 = 175 - 125 = 50 \\implies u_4 = 50/50 = 1\\)."),

    # 62
    ("In Question 59 with \\(A = 125\\) and \\(g = 50\\), what is \\(u_2\\)?",
     ["\\(-1\\)", "\\(-2\\)", "\\(0\\)", "\\(1\\)"],
     "A", "OSC", "easy",
     "\\(x_2 = 75 \\implies d_2 = 75 - 125 = -50 \\implies u_2 = -50/50 = -1\\)."),

    # 63
    ("If \\(A = 10, N = 10, \\sum f_i d_i = 15\\), find \\(\\bar{X}\\).",
     ["\\(11.5\\)", "\\(12.0\\)", "\\(11.0\\)", "\\(12.5\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{d} = 15/10 = 1.5\\). \\(\\bar{X} = 10 + 1.5 = 11.5\\)."),

    # 64
    ("If \\(A = 10, N = 10, \\sum f_i d_i = -15\\), find \\(\\bar{X}\\).",
     ["\\(8.5\\)", "\\(9.0\\)", "\\(8.0\\)", "\\(7.5\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{X} = 10 - 1.5 = 8.5\\)."),

    # 65
    ("Does changing the assumed mean \\(A\\) change the calculated value of \\(\\bar{X}\\)?",
     ["No, the final calculated value of Mean remains identical",
      "Yes, larger A gives larger mean",
      "Yes, smaller A gives smaller mean",
      "Only for odd frequencies"],
     "A", "OSC", "easy",
     "Any choice of \\(A\\) results in the same final mean because \\(\\bar{d}\\) compensates for the shift in \\(A\\)."),

    # 66
    ("If \\(A = 35\\) gives \\(\\bar{d} = 2\\), what is \\(\\bar{X}\\)?",
     ["\\(37\\)", "\\(33\\)", "\\(35\\)", "\\(70\\)"],
     "A", "OSC", "easy",
     "\\(35 + 2 = 37\\)."),

    # 67
    ("If \\(A = 40\\) on the same data as Question 66, what must \\(\\bar{d}\\) be?",
     ["\\(-3\\)", "\\(3\\)", "\\(0\\)", "\\(-2\\)"],
     "A", "OSC", "easy",
     "Since \\(\\bar{X} = 37\\), \\(\\bar{d} = \\bar{X} - A = 37 - 40 = -3\\)."),

    # 68
    ("In Step Deviation, if \\(\\sum f_i u_i = 0\\), what is \\(\\bar{X}\\)?",
     ["\\(A\\)", "\\(0\\)", "\\(g\\)", "\\(1\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{u} = 0 \\implies \\bar{X} = A + 0 = A\\)."),

    # 69
    ("If \\(g = 1\\), does the Step Deviation Method become identical to the Assumed Mean Method?",
     ["Yes, because u_i = d_i / 1 = d_i",
      "No, formulas are different",
      "Only if A = 0",
      "Only for fractions"],
     "A", "OSC", "easy",
     "When \\(g = 1\\), \\(u_i = d_i\\), making Step Deviation identical to Assumed Mean."),

    # 70
    ("If \\(A = 0\\) and \\(g = 1\\), does Step Deviation become identical to the Direct Method?",
     ["Yes, because u_i = x_i and X_bar = 0 + sum(f_i x_i)/N",
      "No, they are never identical",
      "Only if N = 100",
      "Only for prime numbers"],
     "A", "OSC", "easy",
     "When \\(A = 0\\) and \\(g = 1\\), \\(u_i = x_i\\), reproducing the Direct Method formula exactly.")
]

t62_mock = [
    # 71
    ("Why is it called the 'Assumed Mean' method?",
     ["Because we assume a tentative mean value (A) to measure deviations",
      "Because the answer is only an assumption",
      "Because the teacher assumes the marks",
      "Because it is not a real average"],
     "A", "OSC", "easy",
     "We pick a preliminary 'assumed' mean \\(A\\) and then calculate the exact correction \\(\\bar{d}\\)."),

    # 72
    ("Is the answer obtained from Assumed Mean Method an estimate or exact?",
     ["It is the mathematically EXACT arithmetic mean",
      "It is only an estimate",
      "It is an approximation within 5%",
      "It depends on computer software"],
     "A", "OSC", "easy",
     "It is mathematically exact and equal to the Direct Method."),

    # 73
    ("What does \\(d_i\\) represent in statistics?",
     ["Deviation of class mark from assumed mean: \\(x_i - A\\)",
      "Diameter of a circle",
      "Distance between graphs",
      "Degree of polynomial"],
     "A", "OSC", "easy",
     "\\(d_i\\) represents deviation: \\(d_i = x_i - A\\)."),

    # 74
    ("What does \\(u_i\\) represent in Step Deviation?",
     ["The reduced deviation: \\(u_i = d_i / g\\)",
      "Universal set",
      "Unit vector",
      "Upper limit"],
     "A", "OSC", "easy",
     "\\(u_i\\) is the normalized deviation obtained by dividing by common factor \\(g\\)."),

    # 75
    ("What does \\(A\\) stand for in these formulas?",
     ["Assumed Mean", "Area", "Amplitude", "Average frequency"],
     "A", "OSC", "easy",
     "\\(A\\) denotes the Assumed Mean."),

    # 76
    ("What does \\(g\\) stand for in Step Deviation?",
     ["Common factor or class width", "Acceleration due to gravity", "Growth rate", "Geometric mean"],
     "A", "OSC", "easy",
     "\\(g\\) represents the common class size or common factor."),

    # 77
    ("If \\(A = 50\\) and \\(\\bar{d} = 0\\), what is the mean?",
     ["\\(50\\)", "\\(0\\)", "\\(100\\)", "\\(25\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{X} = 50 + 0 = 50\\)."),

    # 78
    ("If \\(A = 50\\) and \\(\\bar{d} = 10\\), what is the mean?",
     ["\\(60\\)", "\\(50\\)", "\\(40\\)", "\\(55\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{X} = 50 + 10 = 60\\)."),

    # 79
    ("If \\(A = 50\\) and \\(\\bar{d} = -10\\), what is the mean?",
     ["\\(40\\)", "\\(60\\)", "\\(50\\)", "\\(45\\)"],
     "A", "OSC", "easy",
     "\\(\\bar{X} = 50 - 10 = 40\\)."),

    # 80
    ("Can \\(d_i\\) be negative?",
     ["Yes, whenever the class mark is smaller than the assumed mean (x_i < A)",
      "No, deviations are always positive",
      "Only if frequencies are negative",
      "Only for odd numbers"],
     "A", "OSC", "easy",
     "When \\(x_i < A\\), \\(d_i = x_i - A < 0\\)."),

    # 81
    ("Can \\(u_i\\) be negative?",
     ["Yes, whenever d_i is negative",
      "No, u_i is always positive",
      "Only if g is negative",
      "Only in fractions"],
     "A", "OSC", "easy",
     "Since \\(u_i = d_i / g\\) and \\(g > 0\\), \\(u_i\\) is negative whenever \\(d_i\\) is negative."),

    # 82
    ("Why do we multiply by \\(g\\) at the end of the Step Deviation formula?",
     ["To reverse the division by g performed earlier when defining u_i",
      "Because g is the gravity constant",
      "To make the number larger",
      "To convert to percentage"],
     "A", "OSC", "easy",
     "Since \\(u_i = d_i / g\\), we have \\(d_i = u_i \\cdot g\\). Hence \\(\\bar{d} = \\bar{u} \\cdot g\\), and \\(\\bar{X} = A + \\bar{u} \\cdot g\\).")
]

if __name__ == "__main__":
    topic_code = "MH-10-MTH1-6-6.2"
    all_qs = build_topic_questions(topic_code, t62_exam, t62_prac, t62_mock)
    out_path = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch6_t2.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {topic_code} -> {out_path}")
