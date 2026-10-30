# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 6: Statistics - Topic 6.3: Median of Grouped Frequency Distribution (MH-10-MTH1-6-6.3)
Total: 82 Canonical Questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# TOPIC 6.3: Median of Grouped Frequency Distribution Formula
t63_exam = [
    # 1
    ("What is the standard formula to calculate the Median of a grouped frequency distribution?",
     ["\\(\\text{Median} = L + \\left[\\frac{\\frac{N}{2} - cf}{f}\\right] \\times h\\)",
      "\\(\\text{Median} = L - \\left[\\frac{\\frac{N}{2} - cf}{f}\\right] \\times h\\)",
      "\\(\\text{Median} = L + \\left[\\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\\right] \\times h\\)",
      "\\(\\text{Median} = \\frac{N/2 - cf}{f}\\)"],
     "A", "OSC", "easy",
     "The formula for the median of grouped data is \\(\\text{Median} = L + \\left[\\frac{N/2 - cf}{f}\\right] h\\)."),

    # 2
    ("In the median formula, what does \\(L\\) represent?",
     ["The lower class limit of the median class",
      "The length of the entire table",
      "The last cumulative frequency",
      "The largest frequency"],
     "A", "OSC", "easy",
     "\\(L\\) denotes the lower limit of the identified median class (using continuous class boundaries)."),

    # 3
    ("In the median formula, what does \\(cf\\) represent?",
     ["Cumulative frequency of the class PRECEDING the median class",
      "Cumulative frequency of the median class itself",
      "Cumulative frequency of the succeeding class",
      "Class frequency"],
     "A", "OSC", "easy",
     "\\(cf\\) is strictly the cumulative frequency of the class immediately preceding (before) the median class."),

    # 4
    ("In the median formula, what does \\(f\\) represent?",
     ["Frequency of the median class",
      "Total frequency of all classes",
      "Frequency of the class preceding the median class",
      "Frequency of the first class"],
     "A", "OSC", "easy",
     "\\(f\\) is the simple frequency of the median class itself."),

    # 5
    ("In the median formula, what does \\(h\\) represent?",
     ["Class width (or class size) of the median class",
      "Height of the student",
      "Highest frequency",
      "Half of total frequency"],
     "A", "OSC", "easy",
     "\\(h\\) is the class size (upper limit minus lower limit) of the median class."),

    # 6
    ("How is the 'Median Class' identified in a grouped frequency distribution?",
     ["The class interval whose cumulative frequency (\\(cf\\)) is just greater than or equal to \\(N/2\\)",
      "The class with the highest frequency",
      "The first class of the table",
      "The class with the largest class mark"],
     "A", "OSC", "easy",
     "We compute \\(N/2\\) and locate the first class interval whose cumulative frequency is \\(\\ge N/2\\). That class is the Median Class."),

    # 7
    ("What prerequisite must be satisfied by the class intervals before applying the median formula?",
     ["The class intervals must be continuous (exclusive form)",
      "All frequencies must be prime numbers",
      "Total frequency must be an even integer",
      "Classes must start from zero"],
     "A", "OSC", "easy",
     "If classes are discontinuous/inclusive (e.g. 10-19, 20-29), they must first be converted into continuous classes (9.5-19.5, 19.5-29.5) before identifying \\(L\\) and \\(h\\)."),

    # 8
    ("In a grouped distribution: \\(L = 20, N = 50, cf = 15, f = 10, h = 10\\). Calculate the Median.",
     ["\\(30\\)", "\\(25\\)", "\\(35\\)", "\\(28\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 25\\). \\(\\text{Median} = 20 + \\left[\\frac{25 - 15}{10}\\right] \\times 10 = 20 + \\left[\\frac{10}{10}\\right] \\times 10 = 20 + 10 = 30\\)."),

    # 9
    ("In a grouped distribution: \\(L = 10, N = 100, cf = 35, f = 25, h = 5\\). Find the Median.",
     ["\\(13\\)", "\\(12.5\\)", "\\(13.5\\)", "\\(14\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 50\\). \\(\\text{Median} = 10 + \\left[\\frac{50 - 35}{25}\\right] \\times 5 = 10 + \\left[\\frac{15}{25}\\right] \\times 5 = 10 + 3 = 13\\)."),

    # 10
    ("In a grouped distribution: \\(L = 40, N = 60, cf = 22, f = 16, h = 10\\). Find the Median.",
     ["\\(45\\)", "\\(44.5\\)", "\\(46\\)", "\\(43.5\\)"],
     "A", "OSC", "medium",
     "\\(N/2 = 30\\). \\(\\text{Median} = 40 + \\left[\\frac{30 - 22}{16}\\right] \\times 10 = 40 + \\left[\\frac{8}{16}\\right] \\times 10 = 40 + 5 = 45\\)."),

    # 11
    ("If the total frequency is \\(N = 80\\), what is the value of \\(N/2\\) used to locate the median class?",
     ["\\(40\\)", "\\(80\\)", "\\(20\\)", "\\(160\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 80 / 2 = 40\\)."),

    # 12
    ("What measure of central tendency divides an ordered distribution into two equal parts such that 50% of observations lie below it and 50% above it?",
     ["Median", "Mean", "Mode", "Standard Deviation"],
     "A", "OSC", "easy",
     "The median is by definition the positional middle value dividing sorted data into two equal halves."),

    # 13
    ("Which graphical representation can be used to determine the median of grouped data directly from the point of intersection?",
     ["'Less than' and 'More than' Ogives (Cumulative Frequency Curves)",
      "Bar chart",
      "Pie chart",
      "Histogram alone"],
     "A", "OSC", "easy",
     "The x-coordinate of the intersection point of the 'less than' ogive and 'more than' ogive gives the median directly."),

    # 14
    ("Find the median of the raw data: \\(3, 7, 2, 9, 5, 8, 4\\).",
     ["\\(5\\)", "\\(7\\)", "\\(4\\)", "\\(6\\)"],
     "A", "OSC", "easy",
     "Arranging in ascending order: \\(2, 3, 4, 5, 7, 8, 9\\). There are \\(n = 7\\) values. The middle (4th) value is 5."),

    # 15
    ("Find the median of the raw data: \\(12, 18, 14, 10, 16, 20\\).",
     ["\\(15\\)", "\\(14\\)", "\\(16\\)", "\\(14.5\\)"],
     "A", "OSC", "easy",
     "Ascending order: \\(10, 12, 14, 16, 18, 20\\). For \\(n = 6\\), median is the average of 3rd and 4th terms: \\(\\frac{14 + 16}{2} = 15\\)."),

    # 16
    ("If classes are \\(1-10, 11-20, 21-30\\), what is the continuous lower limit of the second class?",
     ["\\(10.5\\)", "\\(11.0\\)", "\\(10.0\\)", "\\(11.5\\)"],
     "A", "OSC", "easy",
     "Continuous boundary is \\(11 - 0.5 = 10.5\\)."),

    # 17
    ("In a distribution, classes are \\(0-10\\) (freq 5), \\(10-20\\) (freq 8), \\(20-30\\) (freq 12), \\(30-40\\) (freq 7). Total \\(N = 32\\). What is the median class?",
     ["\\(20 - 30\\)", "\\(10 - 20\\)", "\\(30 - 40\\)", "\\(0 - 10\\)"],
     "A", "OSC", "medium",
     "\\(N/2 = 16\\). Cumulative frequencies: \\(0-10\\) is 5; \\(10-20\\) is \\(5+8 = 13\\); \\(20-30\\) is \\(13+12 = 25\\). Since 25 is the first \\(cf \\ge 16\\), the median class is \\(20 - 30\\)."),

    # 18
    ("In Question 17, what is the value of \\(L\\)?",
     ["\\(20\\)", "\\(30\\)", "\\(10\\)", "\\(25\\)"],
     "A", "OSC", "easy",
     "The lower limit of median class \\(20-30\\) is \\(L = 20\\)."),

    # 19
    ("In Question 17, what is the value of \\(cf\\)?",
     ["\\(13\\)", "\\(25\\)", "\\(5\\)", "\\(12\\)"],
     "A", "OSC", "easy",
     "\\(cf\\) is the cumulative frequency of the class PRECEDING the median class, which is 13."),

    # 20
    ("In Question 17, what is the value of \\(f\\)?",
     ["\\(12\\)", "\\(13\\)", "\\(25\\)", "\\(8\\)"],
     "A", "OSC", "easy",
     "\\(f\\) is the frequency of the median class, which is 12."),

    # 21
    ("In Question 17, calculate the exact Median.",
     ["\\(22.5\\)", "\\(22.0\\)", "\\(23.0\\)", "\\(21.5\\)"],
     "A", "OSC", "medium",
     "\\(\\text{Median} = 20 + \\left[\\frac{16 - 13}{12}\\right] \\times 10 = 20 + \\frac{3}{12} \\times 10 = 20 + 2.5 = 22.5\\)."),

    # 22
    ("Why is the cumulative frequency of the preceding class (\\(cf\\)) subtracted from \\(N/2\\) in the numerator?",
     ["To find how many remaining observations lie within the median class before reaching the exact middle value",
      "Because frequencies must decrease",
      "To eliminate negative numbers",
      "To convert to percentages"],
     "A", "OSC", "easy",
     "Subtracting \\(cf\\) isolates the rank of the median observation within the median class interval."),

    # 23
    ("In a grouped distribution: \\(L = 100, N = 200, cf = 70, f = 60, h = 50\\). Calculate the Median.",
     ["\\(125\\)", "\\(120\\)", "\\(130\\)", "\\(115\\)"],
     "A", "OSC", "medium",
     "\\(N/2 = 100\\). \\(\\text{Median} = 100 + \\left[\\frac{100 - 70}{60}\\right] \\times 50 = 100 + \\left[\\frac{30}{60}\\right] \\times 50 = 100 + 25 = 125\\)."),

    # 24
    ("If the median of a distribution is \\(35\\), in which class must it lie?",
     ["The median class", "The modal class always", "The last class", "The first class"],
     "A", "OSC", "easy",
     "By definition, the calculated median always falls within the boundaries of the median class."),

    # 25
    ("Can the median be influenced by extreme outliers in the data as heavily as the mean?",
     ["No, the median is a positional average and is robust against extreme outliers",
      "Yes, outliers affect median more than mean",
      "Yes, both are equally sensitive",
      "Only for negative numbers"],
     "A", "OSC", "easy",
     "Because median depends only on rank order and position, extreme unusually large or small values do not distort it."),

    # 26
    ("In a cumulative frequency table, what does the last entry of the 'less than' cumulative frequency column equal?",
     ["The total frequency \\(N\\) (\\(\\sum f_i\\))",
      "The mean of the data",
      "The median",
      "The upper limit of the last class"],
     "A", "OSC", "easy",
     "The last cumulative frequency sums all frequencies, so it is always exactly equal to the total frequency \\(N\\)."),

    # 27
    ("In a grouped distribution: \\(L = 50, N = 80, cf = 30, f = 20, h = 10\\). Find the Median.",
     ["\\(55\\)", "\\(54\\)", "\\(56\\)", "\\(52\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 40\\). \\(\\text{Median} = 50 + \\left[\\frac{40 - 30}{20}\\right] \\times 10 = 50 + 5 = 55\\)."),

    # 28
    ("In a distribution: \\(L = 15, N = 40, cf = 14, f = 12, h = 6\\). Find the Median.",
     ["\\(18\\)", "\\(17.5\\)", "\\(18.5\\)", "\\(19\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 20\\). \\(\\text{Median} = 15 + \\left[\\frac{20 - 14}{12}\\right] \\times 6 = 15 + \\left[\\frac{6}{12}\\right] \\times 6 = 15 + 3 = 18\\)."),

    # 29
    ("If \\(N/2 = cf\\), what is the value of the Median?",
     ["Equal to \\(L\\) (the lower limit of the median class)",
      "Zero",
      "Equal to \\(L + h\\)",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "When \\(N/2 - cf = 0\\), the fraction becomes 0, so \\(\\text{Median} = L + 0 = L\\)."),

    # 30
    ("In a distribution: \\(L = 60, N = 50, cf = 25, f = 10, h = 10\\). Find the Median.",
     ["\\(60\\)", "\\(65\\)", "\\(70\\)", "\\(55\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 25\\). Since \\(N/2 - cf = 25 - 25 = 0\\), \\(\\text{Median} = L = 60\\)."),

    # 31
    ("Find the median of the first \\(9\\) natural numbers \\(1, 2, \\dots, 9\\).",
     ["\\(5\\)", "\\(4.5\\)", "\\(5.5\\)", "\\(6\\)"],
     "A", "OSC", "easy",
     "Middle value of 1 to 9 is \\((9+1)/2 = 5\\)."),

    # 32
    ("Find the median of the first \\(10\\) natural numbers \\(1, 2, \\dots, 10\\).",
     ["\\(5.5\\)", "\\(5\\)", "\\(6\\)", "\\(5.0\\)"],
     "A", "OSC", "easy",
     "Average of 5th and 6th terms: \\((5 + 6)/2 = 5.5\\)."),

    # 33
    ("In a grouped distribution: \\(L = 300, N = 100, cf = 40, f = 25, h = 50\\). Find the Median.",
     ["\\(320\\)", "\\(325\\)", "\\(315\\)", "\\(330\\)"],
     "A", "OSC", "medium",
     "\\(N/2 = 50\\). \\(\\text{Median} = 300 + \\left[\\frac{50 - 40}{25}\\right] \\times 50 = 300 + \\frac{10}{25} \\times 50 = 300 + 20 = 320\\)."),

    # 34
    ("What are the columns needed in a table to calculate the Median of grouped data?",
     ["Class Interval, Continuous Classes (if needed), Frequency (\\(f_i\\)), Cumulative Frequency (less than type)",
      "Class Mark, Deviation, Step deviation, Frequency",
      "Histogram coordinates and Angles",
      "Frequency and Square of frequency"],
     "A", "OSC", "easy",
     "Median calculation requires Class Interval, Continuous Classes, Frequency, and Less-than Cumulative Frequency."),

    # 35
    ("If the median of \\(x, x/2, x/3, x/5\\) (for \\(x > 0\\)) is \\(5\\), what is the median expression and value of \\(x\\)?",
     ["Ascending order is \\(x/5, x/3, x/2, x\\); median is \\(\\frac{x/3 + x/2}{2} = 5x/12 = 5 \\implies x = 12\\)",
      "\\(x = 10\\)", "\\(x = 15\\)", "\\(x = 20\\)"],
     "A", "OSC", "hard",
     "In order: \\(x/5, x/3, x/2, x\\). Median is average of middle two: \\(\\frac{x/3 + x/2}{2} = \\frac{5x/6}{2} = \\frac{5x}{12}\\). \\(\\frac{5x}{12} = 5 \\implies x = 12\\)."),

    # 36
    ("If the median of the numbers \\(11, 12, 14, 18, x+2, x+4, 30, 32, 35, 41\\) arranged in ascending order is \\(24\\), find \\(x\\).",
     ["\\(21\\)", "\\(20\\)", "\\(22\\)", "\\(19\\)"],
     "A", "OSC", "hard",
     "There are 10 numbers. The median is the average of 5th and 6th terms: \\(\\frac{(x+2) + (x+4)}{2} = x + 3\\). \\(x + 3 = 24 \\implies x = 21\\)."),

    # 37
    ("In a distribution: \\(L = 70, N = 80, cf = 36, f = 8, h = 10\\). Find the Median.",
     ["\\(75\\)", "\\(74\\)", "\\(76\\)", "\\(72.5\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 40\\). \\(\\text{Median} = 70 + \\left[\\frac{40 - 36}{8}\\right] \\times 10 = 70 + \\frac{4}{8} \\times 10 = 70 + 5 = 75\\)."),

    # 38
    ("In a distribution: \\(L = 12, N = 50, cf = 20, f = 10, h = 4\\). Find the Median.",
     ["\\(14\\)", "\\(13.5\\)", "\\(14.5\\)", "\\(15\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 25\\). \\(\\text{Median} = 12 + \\left[\\frac{25 - 20}{10}\\right] \\times 4 = 12 + \\frac{5}{10} \\times 4 = 12 + 2 = 14\\)."),

    # 39
    ("Can the median of a dataset be a number that does not appear in the original dataset?",
     ["Yes, for example when averaging two middle numbers of an even sample size",
      "No, median must always be an actual data point",
      "Only for grouped data",
      "Only if data contains negative numbers"],
     "A", "OSC", "easy",
     "For an even number of observations, the median is the arithmetic mean of the two middle values, which may not be present in the original dataset (e.g. median of 2 and 4 is 3)."),

    # 40
    ("Which letter conventionally denotes cumulative frequency?",
     ["cf", "f", "x", "h"],
     "A", "OSC", "easy",
     "Cumulative frequency is conventionally abbreviated as \\(cf\\).")
]

t63_prac = [
    # 41
    ("Find the median of \\(1, 3, 3, 6, 7, 8, 9\\).",
     ["\\(6\\)", "\\(3\\)", "\\(7\\)", "\\(5\\)"],
     "A", "OSC", "easy",
     "There are 7 values. The 4th value is 6."),

    # 42
    ("Find the median of \\(2, 4, 6, 8, 10, 12\\).",
     ["\\(7\\)", "\\(6\\)", "\\(8\\)", "\\(6.5\\)"],
     "A", "OSC", "easy",
     "\\((6 + 8)/2 = 7\\)."),

    # 43
    ("In a distribution: \\(L = 10, N = 20, cf = 6, f = 8, h = 5\\). Find Median.",
     ["\\(12.5\\)", "\\(12.0\\)", "\\(13.0\\)", "\\(11.5\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 10\\). \\(10 + \\frac{10-6}{8} \\times 5 = 10 + 2.5 = 12.5\\)."),

    # 44
    ("If \\(N = 120\\), what is \\(N/2\\)?",
     ["\\(60\\)", "\\(120\\)", "\\(30\\)", "\\(40\\)"],
     "A", "OSC", "easy",
     "\\(120 / 2 = 60\\)."),

    # 45
    ("In a distribution: \\(L = 25, N = 60, cf = 20, f = 20, h = 5\\). Find Median.",
     ["\\(27.5\\)", "\\(28.0\\)", "\\(27.0\\)", "\\(26.5\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 30\\). \\(25 + \\frac{30-20}{20} \\times 5 = 25 + 2.5 = 27.5\\)."),

    # 46
    ("What is cumulative frequency (cf) of the first class?",
     ["Equal to the frequency of the first class itself",
      "Always 0",
      "Total frequency N",
      "Half of N"],
     "A", "OSC", "easy",
     "For the first class, \\(cf_1 = f_1\\)."),

    # 47
    ("If frequencies are 3, 5, 8, 4, what is the cumulative frequency of the 3rd class?",
     ["\\(16\\)", "\\(8\\)", "\\(12\\)", "\\(20\\)"],
     "A", "OSC", "easy",
     "\\(3 + 5 + 8 = 16\\)."),

    # 48
    ("In Question 47, what is the total frequency \\(N\\)?",
     ["\\(20\\)", "\\(16\\)", "\\(24\\)", "\\(18\\)"],
     "A", "OSC", "easy",
     "\\(3 + 5 + 8 + 4 = 20\\)."),

    # 49
    ("In Question 47, which class is the median class (\\(N/2 = 10\\))?",
     ["The 3rd class (cf = 16 >= 10)", "The 2nd class (cf = 8)", "The 1st class", "The 4th class"],
     "A", "OSC", "easy",
     "Cumulative frequencies are 3, 8, 16. 16 is the first \\(cf \\ge 10\\), so the 3rd class is the median class."),

    # 50
    ("In Question 47, what is \\(cf\\) for the median formula?",
     ["\\(8\\) (cumulative frequency of 2nd class)", "\\(16\\)", "\\(3\\)", "\\(5\\)"],
     "A", "OSC", "easy",
     "\\(cf\\) is the cumulative frequency of the preceding (2nd) class, which is 8."),

    # 51
    ("In a distribution: \\(L = 100, N = 40, cf = 15, f = 10, h = 20\\). Find Median.",
     ["\\(110\\)", "\\(105\\)", "\\(115\\)", "\\(120\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 20\\). \\(100 + \\frac{20-15}{10} \\times 20 = 100 + 10 = 110\\)."),

    # 52
    ("If median of \\(5, 7, x, 10, 12\\) is \\(9\\), find \\(x\\) (assuming sorted order).",
     ["\\(9\\)", "\\(8\\)", "\\(10\\)", "\\(7\\)"],
     "A", "OSC", "easy",
     "For 5 numbers, the 3rd number is the median: \\(x = 9\\)."),

    # 53
    ("In a distribution: \\(L = 35, N = 100, cf = 45, f = 10, h = 5\\). Find Median.",
     ["\\(37.5\\)", "\\(38.0\\)", "\\(37.0\\)", "\\(36.5\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 50\\). \\(35 + \\frac{50-45}{10} \\times 5 = 35 + 2.5 = 37.5\\)."),

    # 54
    ("Continuous classes for \\(20-29, 30-39\\) are:",
     ["\\(19.5 - 29.5, 29.5 - 39.5\\)", "\\(20 - 30, 30 - 40\\)", "\\(19 - 29, 29 - 39\\)", "\\(20.5 - 29.5\\)"],
     "A", "OSC", "easy",
     "Subtract 0.5 from lower and add 0.5 to upper limit: \\(19.5 - 29.5, 29.5 - 39.5\\)."),

    # 55
    ("In Question 54, what is the class width \\(h\\)?",
     ["\\(10\\)", "\\(9\\)", "\\(9.5\\)", "\\(10.5\\)"],
     "A", "OSC", "easy",
     "\\(29.5 - 19.5 = 10\\)."),

    # 56
    ("In a distribution: \\(L = 150, N = 50, cf = 20, f = 10, h = 25\\). Find Median.",
     ["\\(162.5\\)", "\\(160\\)", "\\(165\\)", "\\(158.5\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 25\\). \\(150 + \\frac{25-20}{10} \\times 25 = 150 + 12.5 = 162.5\\)."),

    # 57
    ("If \\(N = 50\\), what is \\(N/2\\)?",
     ["\\(25\\)", "\\(50\\)", "\\(10\\)", "\\(12.5\\)"],
     "A", "OSC", "easy",
     "\\(50 / 2 = 25\\)."),

    # 58
    ("In a distribution: \\(L = 0, N = 30, cf = 10, f = 10, h = 10\\). Find Median.",
     ["\\(5\\)", "\\(10\\)", "\\(0\\)", "\\(7.5\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 15\\). \\(0 + \\frac{15-10}{10} \\times 10 = 5\\)."),

    # 59
    ("In a distribution: \\(L = 80, N = 70, cf = 30, f = 10, h = 10\\). Find Median.",
     ["\\(85\\)", "\\(84\\)", "\\(86\\)", "\\(83\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 35\\). \\(80 + \\frac{35-30}{10} \\times 10 = 85\\)."),

    # 60
    ("Find the median of \\(10, 11, 12, 13, 14, 15, 16\\).",
     ["\\(13\\)", "\\(12\\)", "\\(14\\)", "\\(13.5\\)"],
     "A", "OSC", "easy",
     "Middle value of 7 numbers is the 4th value: 13."),

    # 61
    ("Find the median of \\(20, 22, 24, 26\\).",
     ["\\(23\\)", "\\(22\\)", "\\(24\\)", "\\(22.5\\)"],
     "A", "OSC", "easy",
     "\\((22 + 24)/2 = 23\\)."),

    # 62
    ("In a distribution: \\(L = 400, N = 100, cf = 40, f = 20, h = 100\\). Find Median.",
     ["\\(450\\)", "\\(440\\)", "\\(460\\)", "\\(425\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 50\\). \\(400 + \\frac{50-40}{20} \\times 100 = 400 + 50 = 450\\)."),

    # 63
    ("In a distribution: \\(L = 16, N = 80, cf = 32, f = 16, h = 4\\). Find Median.",
     ["\\(18\\)", "\\(17\\)", "\\(19\\)", "\\(17.5\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 40\\). \\(16 + \\frac{40-32}{16} \\times 4 = 16 + 2 = 18\\)."),

    # 64
    ("What happens to the median if every number in a dataset is doubled?",
     ["The median is doubled", "The median remains the same", "The median is halved", "The median increases by 2"],
     "A", "OSC", "easy",
     "Scaling all values by a positive constant scales the median by the same constant."),

    # 65
    ("What happens to the median if 10 is added to every observation?",
     ["The median increases by 10", "The median remains unchanged", "The median is multiplied by 10", "The median increases by 5"],
     "A", "OSC", "easy",
     "Adding a constant shifts all order statistics including the median by that constant."),

    # 66
    ("In a distribution: \\(L = 200, N = 60, cf = 24, f = 12, h = 20\\). Find Median.",
     ["\\(210\\)", "\\(205\\)", "\\(215\\)", "\\(220\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 30\\). \\(200 + \\frac{30-24}{12} \\times 20 = 200 + 10 = 210\\)."),

    # 67
    ("If the median class is \\(30 - 40\\), can the median be \\(28\\) or \\(42\\)?",
     ["No, the median must strictly lie within the median class [30, 40]",
      "Yes, if N is odd",
      "Yes, if f is negative",
      "Only in pie charts"],
     "A", "OSC", "easy",
     "The median must fall within the lower and upper limits of the median class."),

    # 68
    ("In a distribution: \\(L = 5, N = 10, cf = 4, f = 2, h = 2\\). Find Median.",
     ["\\(6\\)", "\\(5.5\\)", "\\(6.5\\)", "\\(7\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 5\\). \\(5 + \\frac{5-4}{2} \\times 2 = 6\\)."),

    # 69
    ("What is an Ogive?",
     ["A cumulative frequency curve", "A bar chart", "A histogram", "A scatter plot"],
     "A", "OSC", "easy",
     "An ogive is the graphical curve representing cumulative frequency distribution."),

    # 70
    ("In a distribution: \\(L = 18, N = 40, cf = 18, f = 4, h = 6\\). Find Median.",
     ["\\(21\\)", "\\(20\\)", "\\(22\\)", "\\(19.5\\)"],
     "A", "OSC", "easy",
     "\\(N/2 = 20\\). \\(18 + \\frac{20-18}{4} \\times 6 = 18 + 3 = 21\\).")
]

t63_mock = [
    # 71
    ("What does the word 'Median' mean in plain English?",
     ["The middle value in a sequence of sorted numbers",
      "The most popular number",
      "The sum of all numbers",
      "The range of numbers"],
     "A", "OSC", "easy",
     "Median signifies the central or middle point of an ordered set."),

    # 72
    ("Why must data be arranged in order before finding the median?",
     ["Because the median is a positional measure that depends on rank ordering",
      "Because math formulas only work forwards",
      "Because negative numbers are deleted",
      "To calculate the total sum"],
     "A", "OSC", "easy",
     "Without sorting, positional order cannot be determined."),

    # 73
    ("What does \\(N\\) stand for in the median formula?",
     ["Total frequency (sum of all frequencies)", "Number of classes", "The highest value", "Normal distribution"],
     "A", "OSC", "easy",
     "\\(N = \\sum f_i\\) is the total frequency of all observations."),

    # 74
    ("What is \\(N/2\\)?",
     ["Half of the total frequency", "Double the frequency", "The median value", "The class size"],
     "A", "OSC", "easy",
     "\\(N/2\\) represents half of the total number of observations."),

    # 75
    ("What is cumulative frequency?",
     ["The running sum of frequencies up to the current class",
      "The frequency squared",
      "The percentage of each class",
      "The product of limits"],
     "A", "OSC", "easy",
     "Cumulative frequency adds each class frequency to the sum of all preceding frequencies."),

    # 76
    ("If \\(N = 50\\), what is \\(N/2\\)?",
     ["\\(25\\)", "\\(50\\)", "\\(10\\)", "\\(20\\)"],
     "A", "OSC", "easy",
     "\\(50 / 2 = 25\\)."),

    # 77
    ("If \\(N = 100\\), what is \\(N/2\\)?",
     ["\\(50\\)", "\\(100\\)", "\\(25\\)", "\\(10\\)"],
     "A", "OSC", "easy",
     "\\(100 / 2 = 50\\)."),

    # 78
    ("If a class is \\(10 - 20\\), what is the lower limit \\(L\\)?",
     ["\\(10\\)", "\\(20\\)", "\\(15\\)", "\\(5\\)"],
     "A", "OSC", "easy",
     "The lower limit is 10."),

    # 79
    ("If a class is \\(10 - 20\\), what is the class size \\(h\\)?",
     ["\\(10\\)", "\\(20\\)", "\\(15\\)", "\\(30\\)"],
     "A", "OSC", "easy",
     "\\(20 - 10 = 10\\)."),

    # 80
    ("What is the median of \\(1, 2, 3\\)?",
     ["\\(2\\)", "\\(1\\)", "\\(3\\)", "\\(1.5\\)"],
     "A", "OSC", "easy",
     "The middle number is 2."),

    # 81
    ("What is the median of \\(1, 2, 3, 4\\)?",
     ["\\(2.5\\)", "\\(2\\)", "\\(3\\)", "\\(2.0\\)"],
     "A", "OSC", "easy",
     "\\((2 + 3)/2 = 2.5\\)."),

    # 82
    ("Can the median of grouped data be calculated if classes are not continuous?",
     ["No, classes must first be converted to continuous boundaries so there are no gaps",
      "Yes, gaps do not matter in math",
      "Only for even frequencies",
      "Only if class marks are integers"],
     "A", "OSC", "easy",
     "Continuous class boundaries are strictly required to avoid mathematical gaps at class boundaries.")
]

if __name__ == "__main__":
    topic_code = "MH-10-MTH1-6-6.3"
    all_qs = build_topic_questions(topic_code, t63_exam, t63_prac, t63_mock)
    out_path = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch6_t3.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {topic_code} -> {out_path}")
