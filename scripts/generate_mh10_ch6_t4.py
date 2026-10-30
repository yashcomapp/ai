# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 6: Statistics - Topic 6.4: Mode of Grouped Frequency Distribution (MH-10-MTH1-6-6.4)
Total: 82 Canonical Questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# TOPIC 6.4: Mode of Grouped Frequency Distribution Formula
t64_exam = [
    # 1
    ("What is the standard formula to calculate the Mode of a grouped frequency distribution?",
     ["\\(\\text{Mode} = L + \\left[\\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\\right] \\times h\\)",
      "\\(\\text{Mode} = L + \\left[\\frac{f_0 - f_1}{2f_1 - f_0 - f_2}\\right] \\times h\\)",
      "\\(\\text{Mode} = L + \\left[\\frac{\\frac{N}{2} - cf}{f}\\right] \\times h\\)",
      "\\(\\text{Mode} = \\frac{f_1 - f_0}{f_1 + f_2} \\times h\\)"],
     "A", "OSC", "easy",
     "The formula for the mode of grouped data is \\(\\text{Mode} = L + \\left[\\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\\right] h\\)."),

    # 2
    ("In the mode formula, what does \\(L\\) represent?",
     ["The lower class limit of the modal class (using continuous classes)",
      "The length of the entire table",
      "The last frequency",
      "The largest frequency"],
     "A", "OSC", "easy",
     "\\(L\\) is the lower boundary of the modal class interval."),

    # 3
    ("In the mode formula, what does \\(f_1\\) represent?",
     ["Frequency of the modal class (the maximum frequency)",
      "Frequency of the first class",
      "Frequency of the class preceding the modal class",
      "Frequency of the succeeding class"],
     "A", "OSC", "easy",
     "\\(f_1\\) is the frequency of the modal class, which is the highest frequency in the distribution."),

    # 4
    ("In the mode formula, what does \\(f_0\\) represent?",
     ["Frequency of the class PRECEDING the modal class",
      "Frequency of the modal class",
      "Frequency of the succeeding class",
      "Zero frequency"],
     "A", "OSC", "easy",
     "\\(f_0\\) is the frequency of the class immediately before (preceding) the modal class."),

    # 5
    ("In the mode formula, what does \\(f_2\\) represent?",
     ["Frequency of the class SUCCEEDING (following) the modal class",
      "Frequency of the modal class",
      "Frequency of the preceding class",
      "Double the frequency"],
     "A", "OSC", "easy",
     "\\(f_2\\) is the frequency of the class immediately after (succeeding) the modal class."),

    # 6
    ("How is the 'Modal Class' identified in a grouped frequency distribution?",
     ["The class interval having the MAXIMUM frequency",
      "The middle class of the table",
      "The class with the smallest frequency",
      "The class with the largest class mark"],
     "A", "OSC", "easy",
     "The modal class is directly identified as the class interval with the highest frequency."),

    # 7
    ("In a grouped distribution: \\(L = 40, f_1 = 50, f_0 = 30, f_2 = 20, h = 10\\). Calculate the Mode.",
     ["\\(44\\)", "\\(45\\)", "\\(43.5\\)", "\\(46\\)"],
     "A", "OSC", "easy",
     "\\(2f_1 - f_0 - f_2 = 2(50) - 30 - 20 = 100 - 50 = 50\\). \\(\\text{Mode} = 40 + \\left[\\frac{50 - 30}{50}\\right] \\times 10 = 40 + \\frac{20}{50} \\times 10 = 40 + 4 = 44\\)."),

    # 8
    ("In a grouped distribution: \\(L = 60, f_1 = 40, f_0 = 25, f_2 = 15, h = 20\\). Find the Mode.",
     ["\\(67.5\\)", "\\(65.0\\)", "\\(70.0\\)", "\\(68.0\\)"],
     "A", "OSC", "medium",
     "Numerator: \\(40 - 25 = 15\\). Denominator: \\(2(40) - 25 - 15 = 80 - 40 = 40\\). \\(\\text{Mode} = 60 + \\frac{15}{40} \\times 20 = 60 + 7.5 = 67.5\\)."),

    # 9
    ("In a grouped distribution: \\(L = 30, f_1 = 36, f_0 = 18, f_2 = 18, h = 10\\). Find the Mode.",
     ["\\(35\\)", "\\(34\\)", "\\(36\\)", "\\(33.5\\)"],
     "A", "OSC", "easy",
     "Numerator: \\(36 - 18 = 18\\). Denominator: \\(2(36) - 18 - 18 = 72 - 36 = 36\\). \\(\\text{Mode} = 30 + \\frac{18}{36} \\times 10 = 30 + 5 = 35\\)."),

    # 10
    ("What is the empirical relationship connecting Mean, Median, and Mode in a moderately skewed distribution?",
     ["\\(\\text{Mode} \\approx 3\\text{ Median} - 2\\text{ Mean}\\)",
      "\\(\\text{Mode} \\approx 2\\text{ Median} - 3\\text{ Mean}\\)",
      "\\(\\text{Mode} \\approx \\text{Mean} + \\text{Median}\\)",
      "\\(\\text{Mode} \\approx 3\\text{ Mean} - 2\\text{ Median}\\)"],
     "A", "OSC", "easy",
     "The empirical relationship established by Karl Pearson is \\(\\text{Mode} \\approx 3\\text{ Median} - 2\\text{ Mean}\\)."),

    # 11
    ("If \\(\\text{Mean} = 20\\) and \\(\\text{Median} = 22\\), find the approximate Mode using the empirical formula.",
     ["\\(26\\)", "\\(24\\)", "\\(28\\)", "\\(25\\)"],
     "A", "OSC", "easy",
     "\\(\\text{Mode} = 3(22) - 2(20) = 66 - 40 = 26\\)."),

    # 12
    ("If \\(\\text{Mode} = 18\\) and \\(\\text{Mean} = 24\\), find the approximate Median.",
     ["\\(22\\)", "\\(21\\)", "\\(20\\)", "\\(23\\)"],
     "A", "OSC", "medium",
     "\\(18 = 3\\text{ Median} - 2(24) \\implies 18 = 3\\text{ Median} - 48 \\implies 3\\text{ Median} = 66 \\implies \\text{Median} = 22\\)."),

    # 13
    ("In a distribution: classes are \\(0-20\\) (freq 10), \\(20-40\\) (freq 35), \\(40-60\\) (freq 52), \\(60-80\\) (freq 61), \\(80-100\\) (freq 38), \\(100-120\\) (freq 29). What is the modal class?",
     ["\\(60 - 80\\)", "\\(40 - 60\\)", "\\(80 - 100\\)", "\\(20 - 40\\)"],
     "A", "OSC", "easy",
     "The highest frequency is 61, which corresponds to the class interval \\(60 - 80\\)."),

    # 14
    ("In Question 13, what are the values of \\(L, f_1, f_0, f_2, h\\)?",
     ["\\(L = 60, f_1 = 61, f_0 = 52, f_2 = 38, h = 20\\)",
      "\\(L = 60, f_1 = 52, f_0 = 61, f_2 = 38, h = 20\\)",
      "\\(L = 80, f_1 = 61, f_0 = 38, f_2 = 52, h = 20\\)",
      "\\(L = 60, f_1 = 61, f_0 = 38, f_2 = 52, h = 10\\)"],
     "A", "OSC", "medium",
     "Modal class is 60-80. \\(L = 60\\), \\(f_1 = 61\\), preceding frequency \\(f_0 = 52\\), succeeding frequency \\(f_2 = 38\\), width \\(h = 20\\)."),

    # 15
    ("In Questions 13 and 14, calculate the exact Mode of the data.",
     ["\\(65.625\\)", "\\(66.50\\)", "\\(64.80\\)", "\\(67.20\\)"],
     "A", "OSC", "medium",
     "Numerator: \\(61 - 52 = 9\\). Denominator: \\(2(61) - 52 - 38 = 122 - 90 = 32\\). \\(\\text{Mode} = 60 + \\frac{9}{32} \\times 20 = 60 + \\frac{180}{32} = 60 + 5.625 = 65.625\\)."),

    # 16
    ("Find the mode of the raw data: \\(4, 7, 5, 4, 8, 4, 9, 3, 4\\).",
     ["\\(4\\)", "\\(5\\)", "\\(7\\)", "\\(8\\)"],
     "A", "OSC", "easy",
     "The number 4 occurs most frequently (4 times), so the mode is 4."),

    # 17
    ("Can a dataset have more than one mode?",
     ["Yes, a distribution can be bimodal (2 modes), trimodal, or multimodal",
      "No, mode must always be unique like the mean",
      "Only for fractions",
      "Only if sample size is greater than 1000"],
     "A", "OSC", "easy",
     "If two or more values share the highest frequency, the distribution is bimodal or multimodal."),

    # 18
    ("If all values in a dataset occur with equal frequency (e.g. 2, 4, 6, 8 once each), what is the mode?",
     ["There is no mode (or all values are modes)",
      "The mode is 0",
      "The mode is the average",
      "The mode is the first number"],
     "A", "OSC", "easy",
     "When no value occurs more frequently than any other, the data is said to have no mode."),

    # 19
    ("What measure of central tendency is ideal for finding the most popular shoe size or readymade shirt size sold in a store?",
     ["Mode", "Mean", "Median", "Standard Deviation"],
     "A", "OSC", "easy",
     "Commercial demand focuses on the most frequent size sold (maximum frequency), which is represented by the Mode."),

    # 20
    ("In a grouped distribution: \\(L = 10, f_1 = 12, f_0 = 8, f_2 = 10, h = 5\\). Find the Mode.",
     ["\\(13.33\\)", "\\(12.50\\)", "\\(14.00\\)", "\\(13.00\\)"],
     "A", "OSC", "medium",
     "Numerator: \\(12 - 8 = 4\\). Denominator: \\(2(12) - 8 - 10 = 24 - 18 = 6\\). \\(\\text{Mode} = 10 + \\frac{4}{6} \\times 5 = 10 + \\frac{20}{6} = 10 + 3.33 = 13.33\\)."),

    # 21
    ("What must be done if class intervals are given in discontinuous form (e.g. 1-3, 4-6, 7-9) before computing the Mode?",
     ["Convert them into continuous classes (e.g. 0.5-3.5, 3.5-6.5, 6.5-9.5)",
      "Delete the first class",
      "Multiply frequencies by 2",
      "Nothing, discontinuous classes are fine for Mode"],
     "A", "OSC", "easy",
     "The lower limit \\(L\\) and width \\(h\\) must be determined from continuous class boundaries to avoid boundary gaps."),

    # 22
    ("If the modal class of a distribution is \\(20 - 30\\), can the mode be \\(18\\) or \\(32\\)?",
     ["No, the mode must strictly lie inside the modal class interval [20, 30]",
      "Yes, if f_0 > f_1",
      "Yes, if f_2 = 0",
      "Only for negative numbers"],
     "A", "OSC", "easy",
     "The calculated mode is mathematically bounded within the limits of the modal class: \\(L \\le \\text{Mode} \\le L + h\\)."),

    # 23
    ("In a symmetric normal distribution, what is the relation between Mean, Median, and Mode?",
     ["\\(\\text{Mean} = \\text{Median} = \\text{Mode}\\)",
      "\\(\\text{Mean} > \\text{Median} > \\text{Mode}\\)",
      "\\(\\text{Mode} = 3\\text{ Mean}\\)",
      "\\(\\text{Mean} + \\text{Mode} = 0\\)"],
     "A", "OSC", "easy",
     "In a perfectly symmetrical distribution, all three measures of central tendency coincide exactly: Mean = Median = Mode."),

    # 24
    ("In a grouped distribution: \\(L = 100, f_1 = 30, f_0 = 18, f_2 = 22, h = 50\\). Find the Mode.",
     ["\\(130\\)", "\\(125\\)", "\\(135\\)", "\\(120\\)"],
     "A", "OSC", "medium",
     "Numerator: \\(30 - 18 = 12\\). Denominator: \\(2(30) - 18 - 22 = 60 - 40 = 20\\). \\(\\text{Mode} = 100 + \\frac{12}{20} \\times 50 = 100 + 30 = 130\\)."),

    # 25
    ("In a grouped distribution: \\(L = 20, f_1 = 15, f_0 = 10, f_2 = 10, h = 10\\). Find the Mode.",
     ["\\(25\\)", "\\(24\\)", "\\(26\\)", "\\(23.5\\)"],
     "A", "OSC", "easy",
     "Numerator: \\(15 - 10 = 5\\). Denominator: \\(30 - 10 - 10 = 10\\). \\(\\text{Mode} = 20 + \\frac{5}{10} \\times 10 = 20 + 5 = 25\\)."),

    # 26
    ("What happens when the frequencies preceding and succeeding the modal class are equal (\\(f_0 = f_2\\))?",
     ["The mode lies exactly at the midpoint of the modal class interval",
      "The mode equals the lower limit L",
      "The mode equals the upper limit",
      "The mode becomes zero"],
     "A", "OSC", "easy",
     "When \\(f_0 = f_2\\), \\(\\frac{f_1 - f_0}{2f_1 - 2f_0} = \\frac{1}{2}\\), so \\(\\text{Mode} = L + \\frac{1}{2}h\\), which is the exact midpoint of the modal class."),

    # 27
    ("In a distribution: \\(L = 50, f_1 = 40, f_0 = 20, f_2 = 20, h = 20\\). Find the Mode.",
     ["\\(60\\) (exact midpoint of [50, 70])", "\\(55\\)", "\\(65\\)", "\\(58\\)"],
     "A", "OSC", "easy",
     "Since \\(f_0 = f_2 = 20\\), the mode is the midpoint: \\(50 + 10 = 60\\)."),

    # 28
    ("If the modal class is the first class of the distribution, what value is taken for \\(f_0\\)?",
     ["\\(f_0 = 0\\)", "\\(f_0 = f_1\\)", "\\(f_0 = 1\\)", "\\(f_0 = f_2\\)"],
     "A", "OSC", "easy",
     "If the modal class is the very first interval, there is no preceding class, so its frequency \\(f_0\\) is taken as 0."),

    # 29
    ("If the modal class is the last class of the distribution, what value is taken for \\(f_2\\)?",
     ["\\(f_2 = 0\\)", "\\(f_2 = f_1\\)", "\\(f_2 = 1\\)", "\\(f_2 = f_0\\)"],
     "A", "OSC", "easy",
     "If the modal class is the final interval, there is no succeeding class, so \\(f_2\\) is taken as 0."),

    # 30
    ("In a distribution: \\(L = 0, f_1 = 20, f_0 = 0, f_2 = 12, h = 10\\). Find the Mode.",
     ["\\(7.14\\)", "\\(6.50\\)", "\\(8.00\\)", "\\(5.00\\)"],
     "A", "OSC", "medium",
     "Numerator: \\(20 - 0 = 20\\). Denominator: \\(2(20) - 0 - 12 = 40 - 12 = 28\\). \\(\\text{Mode} = 0 + \\frac{20}{28} \\times 10 = \\frac{5}{7} \\times 10 = 7.14\\)."),

    # 31
    ("If \\(\\text{Mean} = 30\\) and \\(\\text{Mode} = 24\\), find the Median using Karl Pearson's empirical relation.",
     ["\\(28\\)", "\\(27\\)", "\\(29\\)", "\\(26\\)"],
     "A", "OSC", "medium",
     "\\(3\\text{ Median} = \\text{Mode} + 2\\text{ Mean} = 24 + 2(30) = 84 \\implies \\text{Median} = 84 / 3 = 28\\)."),

    # 32
    ("If \\(\\text{Median} = 15\\) and \\(\\text{Mode} = 15\\), what must be the Mean in a moderately skewed distribution?",
     ["\\(15\\)", "\\(30\\)", "\\(0\\)", "\\(20\\)"],
     "A", "OSC", "easy",
     "\\(15 = 3(15) - 2\\text{ Mean} \\implies 2\\text{ Mean} = 45 - 15 = 30 \\implies \\text{Mean} = 15\\)."),

    # 33
    ("In a grouped distribution: \\(L = 15, f_1 = 25, f_0 = 15, f_2 = 20, h = 5\\). Find the Mode.",
     ["\\(18.33\\)", "\\(17.50\\)", "\\(19.00\\)", "\\(18.00\\)"],
     "A", "OSC", "medium",
     "Numerator: \\(25 - 15 = 10\\). Denominator: \\(50 - 15 - 20 = 15\\). \\(\\text{Mode} = 15 + \\frac{10}{15} \\times 5 = 15 + \\frac{50}{15} = 15 + 3.33 = 18.33\\)."),

    # 34
    ("Which graphical diagram can directly provide the Mode of a frequency distribution?",
     ["Histogram (by drawing lines from the top corners of the highest rectangle to adjacent rectangles)",
      "Pie chart",
      "Ogive",
      "Frequency polygon alone"],
     "A", "OSC", "easy",
     "In a histogram, connecting the top corners of the highest bar to the opposite top corners of the adjacent bars gives the mode at the x-intercept of their intersection."),

    # 35
    ("In a distribution: \\(L = 80, f_1 = 45, f_0 = 35, f_2 = 25, h = 10\\). Find the Mode.",
     ["\\(83.33\\)", "\\(84.00\\)", "\\(82.50\\)", "\\(85.00\\)"],
     "A", "OSC", "medium",
     "Numerator: \\(45 - 35 = 10\\). Denominator: \\(90 - 35 - 25 = 30\\). \\(\\text{Mode} = 80 + \\frac{10}{30} \\times 10 = 80 + 3.33 = 83.33\\)."),

    # 36
    ("What happens to the denominator \\(2f_1 - f_0 - f_2\\) in the mode formula?",
     ["It is always strictly positive because \\(f_1 > f_0\\) and \\(f_1 > f_2\\)",
      "It can be negative",
      "It is always zero",
      "It equals the total frequency"],
     "A", "OSC", "easy",
     "Since \\(f_1\\) is the maximum frequency, \\(f_1 - f_0 > 0\\) and \\(f_1 - f_2 > 0\\). Adding them gives \\(2f_1 - f_0 - f_2 > 0\\)."),

    # 37
    ("In a distribution: \\(L = 200, f_1 = 60, f_0 = 40, f_2 = 50, h = 50\\). Find the Mode.",
     ["\\(233.33\\)", "\\(225.00\\)", "\\(240.00\\)", "\\(230.00\\)"],
     "A", "OSC", "medium",
     "Numerator: \\(60 - 40 = 20\\). Denominator: \\(120 - 40 - 50 = 30\\). \\(\\text{Mode} = 200 + \\frac{20}{30} \\times 50 = 200 + 33.33 = 233.33\\)."),

    # 38
    ("Find the mode of the numbers: \\(2, 2, 3, 3, 3, 4, 4, 5\\).",
     ["\\(3\\)", "\\(2\\)", "\\(4\\)", "\\(3.5\\)"],
     "A", "OSC", "easy",
     "The number 3 appears 3 times, which is more than any other number."),

    # 39
    ("In a distribution: \\(L = 35, f_1 = 23, f_0 = 21, f_2 = 14, h = 10\\). Find the Mode.",
     ["\\(36.82\\)", "\\(37.50\\)", "\\(36.00\\)", "\\(38.20\\)"],
     "A", "OSC", "medium",
     "Numerator: \\(23 - 21 = 2\\). Denominator: \\(46 - 21 - 14 = 11\\). \\(\\text{Mode} = 35 + \\frac{2}{11} \\times 10 = 35 + 1.82 = 36.82\\)."),

    # 40
    ("Why is cumulative frequency NOT needed when calculating the Mode?",
     ["Because the mode depends solely on local peak frequency rather than rank or running accumulation",
      "Because mode is always an integer",
      "Because frequencies cannot be added",
      "To save paper"],
     "A", "OSC", "easy",
     "Mode is determined strictly by the peak frequency and its immediate neighbors, not by running totals.")
]

t64_prac = [
    # 41
    ("Find the mode of \\(5, 8, 2, 8, 7, 8, 3\\).",
     ["\\(8\\)", "\\(5\\)", "\\(7\\)", "\\(3\\)"],
     "A", "OSC", "easy",
     "8 appears 3 times."),

    # 42
    ("In a distribution: \\(L = 10, f_1 = 15, f_0 = 10, f_2 = 12, h = 4\\). Find Mode.",
     ["\\(12.5\\)", "\\(12.0\\)", "\\(13.0\\)", "\\(11.5\\)"],
     "A", "OSC", "easy",
     "Numerator: 5. Denominator: \\(30 - 22 = 8\\). \\(\\text{Mode} = 10 + (5/8) \\times 4 = 10 + 2.5 = 12.5\\)."),

    # 43
    ("If \\(\\text{Median} = 10\\) and \\(\\text{Mean} = 10\\), what is the Mode?",
     ["\\(10\\)", "\\(20\\)", "\\(0\\)", "\\(5\\)"],
     "A", "OSC", "easy",
     "\\(3(10) - 2(10) = 10\\)."),

    # 44
    ("In a distribution: \\(L = 50, f_1 = 20, f_0 = 12, f_2 = 16, h = 10\\). Find Mode.",
     ["\\(56.67\\)", "\\(55.00\\)", "\\(58.00\\)", "\\(54.50\\)"],
     "A", "OSC", "medium",
     "Numerator: 8. Denominator: \\(40 - 28 = 12\\). \\(50 + (8/12) \\times 10 = 50 + 6.67 = 56.67\\)."),

    # 45
    ("If the modal class is \\(40 - 50\\), what is \\(L\\)?",
     ["\\(40\\)", "\\(50\\)", "\\(45\\)", "\\(10\\)"],
     "A", "OSC", "easy",
     "The lower limit is 40."),

    # 46
    ("In Question 45, what is \\(h\\)?",
     ["\\(10\\)", "\\(40\\)", "\\(50\\)", "\\(45\\)"],
     "A", "OSC", "easy",
     "\\(50 - 40 = 10\\)."),

    # 47
    ("If \\(f_1 = 30, f_0 = 20, f_2 = 20\\), what is \\(\\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\\)?",
     ["\\(0.5\\)", "\\(1.0\\)", "\\(0.25\\)", "\\(0.75\\)"],
     "A", "OSC", "easy",
     "\\(10 / (60 - 40) = 10 / 20 = 0.5\\)."),

    # 48
    ("In a distribution: \\(L = 100, f_1 = 25, f_0 = 15, f_2 = 15, h = 20\\). Find Mode.",
     ["\\(110\\)", "\\(105\\)", "\\(115\\)", "\\(120\\)"],
     "A", "OSC", "easy",
     "Since \\(f_0 = f_2\\), mode is the midpoint \\(100 + 10 = 110\\)."),

    # 49
    ("If \\(\\text{Mean} = 50\\) and \\(\\text{Median} = 48\\), find Mode.",
     ["\\(44\\)", "\\(46\\)", "\\(48\\)", "\\(42\\)"],
     "A", "OSC", "easy",
     "\\(3(48) - 2(50) = 144 - 100 = 44\\)."),

    # 50
    ("Find the mode of \\(12, 14, 12, 16, 18, 12, 14\\).",
     ["\\(12\\)", "\\(14\\)", "\\(16\\)", "\\(18\\)"],
     "A", "OSC", "easy",
     "12 occurs 3 times."),

    # 51
    ("In a distribution: \\(L = 25, f_1 = 18, f_0 = 10, f_2 = 14, h = 6\\). Find Mode.",
     ["\\(29\\)", "\\(28\\)", "\\(30\\)", "\\(27.5\\)"],
     "A", "OSC", "easy",
     "Numerator: 8. Denominator: \\(36 - 24 = 12\\). \\(25 + (8/12) \\times 6 = 25 + 4 = 29\\)."),

    # 52
    ("If the modal class is \\(60 - 75\\), what is \\(h\\)?",
     ["\\(15\\)", "\\(60\\)", "\\(75\\)", "\\(67.5\\)"],
     "A", "OSC", "easy",
     "\\(75 - 60 = 15\\)."),

    # 53
    ("In Question 52, what is the class mark?",
     ["\\(67.5\\)", "\\(15\\)", "\\(65\\)", "\\(70\\)"],
     "A", "OSC", "easy",
     "\\((60 + 75)/2 = 67.5\\)."),

    # 54
    ("In a distribution: \\(L = 0, f_1 = 10, f_0 = 6, f_2 = 8, h = 3\\). Find Mode.",
     ["\\(2\\)", "\\(1.5\\)", "\\(2.5\\)", "\\(1\\)"],
     "A", "OSC", "easy",
     "Numerator: 4. Denominator: \\(20 - 14 = 6\\). \\(0 + (4/6) \\times 3 = 2\\)."),

    # 55
    ("If \\(f_1 = f_0\\), what is the value of the Mode?",
     ["Equal to \\(L\\)", "Zero", "\\(L + h\\)", "Cannot be determined"],
     "A", "OSC", "easy",
     "When \\(f_1 - f_0 = 0\\), the entire added term is 0, so \\(\\text{Mode} = L\\)."),

    # 56
    ("In a distribution: \\(L = 70, f_1 = 30, f_0 = 20, f_2 = 25, h = 15\\). Find Mode.",
     ["\\(80\\)", "\\(75\\)", "\\(82\\)", "\\(78\\)"],
     "A", "OSC", "medium",
     "Numerator: 10. Denominator: \\(60 - 45 = 15\\). \\(70 + (10/15) \\times 15 = 70 + 10 = 80\\)."),

    # 57
    ("If \\(\\text{Mode} = 35\\) and \\(\\text{Median} = 35\\), what is \\(\\text{Mean}\\)?",
     ["\\(35\\)", "\\(0\\)", "\\(70\\)", "\\(17.5\\)"],
     "A", "OSC", "easy",
     "All three are 35."),

    # 58
    ("In a distribution: \\(L = 30, f_1 = 40, f_0 = 24, f_2 = 32, h = 12\\). Find Mode.",
     ["\\(38\\)", "\\(36\\)", "\\(40\\)", "\\(37\\)"],
     "A", "OSC", "medium",
     "Numerator: 16. Denominator: \\(80 - 56 = 24\\). \\(30 + (16/24) \\times 12 = 30 + 8 = 38\\)."),

    # 59
    ("Can the mode be determined graphically from a Histogram?",
     ["Yes, using the intersection of diagonal lines across the highest bar",
      "No, only from pie charts",
      "No, mode cannot be found on graphs",
      "Only if bars are red"],
     "A", "OSC", "easy",
     "The mode is found by connecting the peak rectangle's upper corners to adjacent bars."),

    # 60
    ("In a distribution: \\(L = 120, f_1 = 50, f_0 = 35, f_2 = 45, h = 20\\). Find Mode.",
     ["\\(135\\)", "\\(130\\)", "\\(140\\)", "\\(132.5\\)"],
     "A", "OSC", "medium",
     "Numerator: 15. Denominator: \\(100 - 80 = 20\\). \\(120 + (15/20) \\times 20 = 120 + 15 = 135\\)."),

    # 61
    ("Find the mode of \\(7, 9, 7, 5, 7, 3, 7\\).",
     ["\\(7\\)", "\\(9\\)", "\\(5\\)", "\\(3\\)"],
     "A", "OSC", "easy",
     "7 appears 4 times."),

    # 62
    ("If \\(\\text{Mean} = 18\\) and \\(\\text{Mode} = 12\\), find \\(\\text{Median}\\).",
     ["\\(16\\)", "\\(15\\)", "\\(17\\)", "\\(14\\)"],
     "A", "OSC", "easy",
     "\\(3\\text{ Median} = 12 + 2(18) = 12 + 36 = 48 \\implies \\text{Median} = 16\\)."),

    # 63
    ("In a distribution: \\(L = 15, f_1 = 8, f_0 = 5, f_2 = 7, h = 4\\). Find Mode.",
     ["\\(18\\)", "\\(17\\)", "\\(19\\)", "\\(16.5\\)"],
     "A", "OSC", "easy",
     "Numerator: 3. Denominator: \\(16 - 12 = 4\\). \\(15 + (3/4) \\times 4 = 15 + 3 = 18\\)."),

    # 64
    ("What is the relationship between the peak of a frequency curve and the Mode?",
     ["The mode corresponds to the highest peak (maximum ordinate) of the frequency curve",
      "The mode is at the bottom",
      "The mode is at the starting point",
      "There is no relationship"],
     "A", "OSC", "easy",
     "The highest point of a frequency curve represents the mode."),

    # 65
    ("In a distribution: \\(L = 8, f_1 = 12, f_0 = 7, f_2 = 9, h = 4\\). Find Mode.",
     ["\\(10.5\\)", "\\(10.0\\)", "\\(11.0\\)", "\\(9.5\\)"],
     "A", "OSC", "easy",
     "Numerator: 5. Denominator: \\(24 - 16 = 8\\). \\(8 + (5/8) \\times 4 = 8 + 2.5 = 10.5\\)."),

    # 66
    ("Find the mode of \\(100, 200, 100, 300, 100\\).",
     ["\\(100\\)", "\\(200\\)", "\\(300\\)", "\\(150\\)"],
     "A", "OSC", "easy",
     "100 occurs 3 times."),

    # 67
    ("In a distribution: \\(L = 200, f_1 = 16, f_0 = 12, f_2 = 14, h = 50\\). Find Mode.",
     ["\\(233.33\\)", "\\(225.00\\)", "\\(240.00\\)", "\\(220.00\\)"],
     "A", "OSC", "medium",
     "Numerator: 4. Denominator: \\(32 - 26 = 6\\). \\(200 + (4/6) \\times 50 = 200 + 33.33 = 233.33\\)."),

    # 68
    ("If \\(\\text{Median} = 25\\) and \\(\\text{Mode} = 21\\), find \\(\\text{Mean}\\).",
     ["\\(27\\)", "\\(26\\)", "\\(28\\)", "\\(25\\)"],
     "A", "OSC", "easy",
     "\\(21 = 3(25) - 2\\text{ Mean} \\implies 2\\text{ Mean} = 75 - 21 = 54 \\implies \\text{Mean} = 27\\)."),

    # 69
    ("In a distribution: \\(L = 500, f_1 = 35, f_0 = 25, f_2 = 25, h = 100\\). Find Mode.",
     ["\\(550\\)", "\\(540\\)", "\\(560\\)", "\\(525\\)"],
     "A", "OSC", "easy",
     "Since \\(f_0 = f_2\\), mode is the midpoint \\(500 + 50 = 550\\)."),

    # 70
    ("In a distribution: \\(L = 40, f_1 = 20, f_0 = 15, f_2 = 17, h = 8\\). Find Mode.",
     ["\\(45\\)", "\\(44\\)", "\\(46\\)", "\\(43.5\\)"],
     "A", "OSC", "easy",
     "Numerator: 5. Denominator: \\(40 - 32 = 8\\). \\(40 + (5/8) \\times 8 = 45\\).")
]

t64_mock = [
    # 71
    ("What does 'Mode' signify in statistics?",
     ["The most frequent or popular observation in a dataset",
      "The average of all values",
      "The middle value when sorted",
      "The difference between high and low values"],
     "A", "OSC", "easy",
     "Mode denotes the value that occurs with greatest frequency."),

    # 72
    ("What does \\(f_1\\) represent?",
     ["The maximum frequency (frequency of the modal class)",
      "First frequency",
      "Preceding frequency",
      "Succeeding frequency"],
     "A", "OSC", "easy",
     "\\(f_1\\) is the frequency of the modal class."),

    # 73
    ("What does \\(f_0\\) represent?",
     ["Frequency of the class before the modal class",
      "Zero frequency",
      "Highest frequency",
      "Average frequency"],
     "A", "OSC", "easy",
     "\\(f_0\\) is the preceding class frequency."),

    # 74
    ("What does \\(f_2\\) represent?",
     ["Frequency of the class after the modal class",
      "Double frequency",
      "Second class frequency",
      "Total frequency"],
     "A", "OSC", "easy",
     "\\(f_2\\) is the succeeding class frequency."),

    # 75
    ("What does \\(L\\) denote in the mode formula?",
     ["Lower limit of the modal class", "Length of table", "Last frequency", "Logarithm"],
     "A", "OSC", "easy",
     "\\(L\\) is the lower boundary of the modal class."),

    # 76
    ("What does \\(h\\) denote in the mode formula?",
     ["Class width of the modal class", "Height of the student", "Half of frequency", "Horizontal scale"],
     "A", "OSC", "easy",
     "\\(h\\) represents the width of the modal class interval."),

    # 77
    ("What is the mode of \\(1, 2, 2, 3\\)?",
     ["\\(2\\)", "\\(1\\)", "\\(3\\)", "\\(2.5\\)"],
     "A", "OSC", "easy",
     "2 occurs twice."),

    # 78
    ("Can a distribution have two modes?",
     ["Yes, such a distribution is called bimodal", "No, never", "Only if mean is 0", "Only for integers"],
     "A", "OSC", "easy",
     "When two values share the highest frequency, it is bimodal."),

    # 79
    ("What is the mode of \\(7, 7, 7, 7\\)?",
     ["\\(7\\)", "\\(0\\)", "\\(4\\)", "\\(28\\)"],
     "A", "OSC", "easy",
     "The value 7 occurs exclusively."),

    # 80
    ("If \\(f_1 = 10, f_0 = 5, f_2 = 5\\), does the mode lie at the midpoint of the modal class?",
     ["Yes, because the preceding and succeeding frequencies are equal",
      "No, it lies at L",
      "No, it lies at upper limit",
      "Cannot be determined"],
     "A", "OSC", "easy",
     "Equal neighbor frequencies balance the mode exactly at the class midpoint."),

    # 81
    ("Is the mode affected by extreme outliers in the data?",
     ["No, outliers have virtually no effect on the mode",
      "Yes, outliers change the mode drastically",
      "Yes, more than the mean",
      "Only for negative numbers"],
     "A", "OSC", "easy",
     "Mode is solely concerned with the most frequent values, so extreme high/low values do not affect it."),

    # 82
    ("Which measure of central tendency is the only one that can be used for non-numerical (qualitative) data like favorite color?",
     ["Mode", "Mean", "Median", "Standard Deviation"],
     "A", "OSC", "easy",
     "Qualitative categories (like most popular color or best-selling flavor) can only have a Mode (the most frequent category); Mean and Median cannot be computed for non-numerical categories.")
]

if __name__ == "__main__":
    topic_code = "MH-10-MTH1-6-6.4"
    all_qs = build_topic_questions(topic_code, t64_exam, t64_prac, t64_mock)
    out_path = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch6_t4.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {topic_code} -> {out_path}")
