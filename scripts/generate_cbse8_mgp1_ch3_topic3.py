# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-3-3.3
Topic: Representation of Rational Numbers on the Number Line
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-3-3.3"

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
    ("To represent the rational number \\(\\frac{3}{5}\\) on a number line, into how many equal parts must the unit interval between 0 and 1 be divided?",
     ["5 equal parts", "3 equal parts", "2 equal parts", "8 equal parts"],
     "A", "OSC", "easy",
     "The denominator of \\(\\frac{3}{5}\\) is 5. Therefore, the unit length between 0 and 1 is divided into 5 equal parts, and \\(\\frac{3}{5}\\) corresponds to the 3rd point from 0 to the right."),

    # 2
    ("Between which two consecutive integers does the rational number \\(\\frac{7}{4}\\) lie on the number line?",
     ["Between 1 and 2", "Between 0 and 1", "Between 2 and 3", "Between 7 and 8"],
     "A", "OSC", "easy",
     "Convert to a mixed fraction: \\(\\frac{7}{4} = 1\\frac{3}{4}\\). Since \\(1 < 1\\frac{3}{4} < 2\\), \\(\\frac{7}{4}\\) lies between 1 and 2."),

    # 3
    ("Between which two consecutive integers does \\(-\\frac{5}{3}\\) lie on the number line?",
     ["Between -1 and -2", "Between 0 and -1", "Between -2 and -3", "Between 1 and 2"],
     "A", "OSC", "easy",
     "\\(-\\frac{5}{3} = -1\\frac{2}{3}\\). On the negative axis, \\(-2 < -1\\frac{2}{3} < -1\\), so it lies between -1 and -2."),

    # 4
    ("On which side of zero does the rational number \\(-\\frac{3}{8}\\) lie on the number line?",
     ["To the left of zero", "To the right of zero", "Directly at zero", "Both sides"],
     "A", "OSC", "easy",
     "All negative numbers are located to the left of zero on the horizontal number line."),

    # 5
    ("On a number line, if a unit interval from 0 to 1 is divided into 8 equal parts, what rational number does the 7th mark to the right of 0 represent?",
     ["\\(\\frac{7}{8}\\)", "\\(\\frac{8}{7}\\)", "\\(\\frac{1}{8}\\)", "\\(\\frac{7}{10}\\)"],
     "A", "OSC", "easy",
     "Each part has length \\(\\frac{1}{8}\\). The 7th mark from 0 represents \\(7 \\times \\frac{1}{8} = \\frac{7}{8}\\)."),

    # 6
    ("On a number line, what is the length of each subdivision when the interval between 0 and 1 is divided into 6 equal parts?",
     ["\\(\\frac{1}{6}\\)", "\\(\\frac{1}{5}\\)", "\\(6\\)", "\\(\\frac{1}{12}\\)"],
     "A", "OSC", "easy",
     "Dividing a unit interval of length 1 into 6 equal segments makes each subdivision \\(\\frac{1}{6}\\) units wide."),

    # 7
    ("Which of the following points on the number line is located further to the left: \\(-\\frac{4}{5}\\) or \\(-\\frac{2}{5}\\)?",
     ["\\(-\\frac{4}{5}\\)", "\\(-\\frac{2}{5}\\)", "Both are at the same point", "Cannot be determined"],
     "A", "OSC", "easy",
     "On the negative axis, numbers with larger absolute values lie further to the left. Since \\(|-4/5| > |-2/5|\\), \\(-\\frac{4}{5} < -\\frac{2}{5}\\), so \\(-\\frac{4}{5}\\) is further to the left."),

    # 8
    ("To plot \\(-\\frac{5}{6}\\) on the number line, into how many equal segments should the interval between 0 and -1 be divided?",
     ["6 equal segments", "5 equal segments", "11 equal segments", "1 equal segment"],
     "A", "OSC", "easy",
     "The denominator is 6, so the interval from 0 to -1 is divided into 6 equal parts, and \\(-\\frac{5}{6}\\) is the 5th mark to the left of 0."),

    # 9
    ("What rational number is represented by the point halfway between 0 and 1 on the number line?",
     ["\\(\\frac{1}{2}\\)", "\\(\\frac{1}{4}\\)", "\\(1\\)", "\\(\\frac{3}{4}\\)"],
     "A", "OSC", "easy",
     "The midpoint of 0 and 1 is \\(\\frac{0 + 1}{2} = \\frac{1}{2}\\)."),

    # 10
    ("What rational number is represented by the point halfway between 0 and -1 on the number line?",
     ["\\(-\\frac{1}{2}\\)", "\\(\\frac{1}{2}\\)", "\\(-1\\)", "0"],
     "A", "OSC", "easy",
     "The midpoint is \\(\\frac{0 + (-1)}{2} = -\\frac{1}{2}\\)."),

    # 11
    ("If point P lies between 2 and 3 such that the interval is divided into 5 equal parts and P is at the 3rd mark past 2, what rational number does P represent?",
     ["\\(\\frac{13}{5}\\)", "\\(\\frac{8}{5}\\)", "\\(\\frac{11}{5}\\)", "\\(\\frac{14}{5}\\)"],
     "A", "OSC", "medium",
     "\\(P = 2 + \\frac{3}{5} = \\frac{10 + 3}{5} = \\frac{13}{5} = 2\\frac{3}{5}\\)."),

    # 12
    ("If point Q lies between -2 and -3 such that the interval is divided into 4 equal parts and Q is at the 1st mark to the left of -2, what rational number does Q represent?",
     ["\\(-\\frac{9}{4}\\)", "\\(-\\frac{7}{4}\\)", "\\(-\\frac{11}{4}\\)", "\\(-\\frac{5}{4}\\)"],
     "A", "OSC", "medium",
     "Starting from -2 and moving 1 mark of length \\(\\frac{1}{4}\\) to the left gives \\(-2 - \\frac{1}{4} = -\\frac{9}{4} = -2\\frac{1}{4}\\)."),

    # 13
    ("Which of the following rational numbers lies strictly between 0 and \\(\\frac{1}{2}\\)?",
     ["\\(\\frac{1}{4}\\)", "\\(\\frac{3}{4}\\)", "\\(1\\)", "\\(-\\frac{1}{4}\\)"],
     "A", "OSC", "easy",
     "\\(0 < \\frac{1}{4} = 0.25 < \\frac{1}{2} = 0.5\\)."),

    # 14
    ("Which rational number lies strictly between \\(-\\frac{1}{2}\\) and 0?",
     ["\\(-\\frac{1}{4}\\)", "\\(-\\frac{3}{4}\\)", "\\(-\\frac{1}{2}\\)", "\\(\\frac{1}{4}\\)"],
     "A", "OSC", "easy",
     "\\(-\\frac{1}{2} = -0.5 < -\\frac{1}{4} = -0.25 < 0\\)."),

    # 15
    ("On the number line, if \\(a < b\\), then which of the following is always true?",
     ["The point representing \\(a\\) lies to the left of the point representing \\(b\\)",
      "The point representing \\(a\\) lies to the right of the point representing \\(b\\)",
      "\\(a\\) is always positive",
      "\\(b\\) is always negative"],
     "A", "OSC", "easy",
     "By definition of the real number line, values increase from left to right, so \\(a < b\\) means \\(a\\) lies to the left of \\(b\\)."),

    # 16
    ("How many equal parts should the interval between each consecutive integer be divided into to represent \\(\\frac{11}{3}\\)?",
     ["3 equal parts", "11 equal parts", "4 equal parts", "2 equal parts"],
     "A", "OSC", "easy",
     "The denominator is 3, so every unit interval is divided into 3 equal parts. \\(\\frac{11}{3} = 3\\frac{2}{3}\\) is plotted at the 2nd subdivision between 3 and 4."),

    # 17
    ("Between which two integers does \\(\\frac{11}{3}\\) lie?",
     ["Between 3 and 4", "Between 2 and 3", "Between 4 and 5", "Between 11 and 12"],
     "A", "OSC", "easy",
     "\\(\\frac{11}{3} = 3\\frac{2}{3}\\), which lies strictly between 3 and 4."),

    # 18
    ("Between which two integers does \\(-\\frac{9}{2}\\) lie?",
     ["Between -4 and -5", "Between -3 and -4", "Between -5 and -6", "Between 4 and 5"],
     "A", "OSC", "easy",
     "\\(-\\frac{9}{2} = -4.5\\), which lies strictly between -4 and -5."),

    # 19
    ("What is the distance on the number line between \\(\\frac{1}{3}\\) and \\(\\frac{2}{3}\\)?",
     ["\\(\\frac{1}{3}\\)", "\\(\\frac{3}{3} = 1\\)", "\\(\\frac{2}{3}\\)", "\\(\\frac{1}{6}\\)"],
     "A", "OSC", "easy",
     "Distance = \\(|\\frac{2}{3} - \\frac{1}{3}| = \\frac{1}{3}\\)."),

    # 20
    ("What is the distance on the number line between \\(-\\frac{3}{4}\\) and \\(\\frac{1}{4}\\)?",
     ["1", "\\(\\frac{1}{2}\\)", "\\(\\frac{1}{4}\\)", "\\(-\\frac{1}{2}\\)"],
     "A", "OSC", "easy",
     "Distance = \\(\\frac{1}{4} - \\left(-\\frac{3}{4}\\right) = \\frac{1}{4} + \\frac{3}{4} = \\frac{4}{4} = 1\\)."),

    # 21
    ("What point is exactly halfway between \\(\\frac{1}{4}\\) and \\(\\frac{3}{4}\\)?",
     ["\\(\\frac{1}{2}\\)", "\\(\\frac{1}{4}\\)", "\\(\\frac{5}{8}\\)", "\\(\\frac{3}{8}\\)"],
     "A", "OSC", "easy",
     "Midpoint = \\(\\frac{1/4 + 3/4}{2} = \\frac{1}{2}\\)."),

    # 22
    ("What point is exactly halfway between \\(-\\frac{2}{3}\\) and \\(\\frac{2}{3}\\)?",
     ["0", "\\(\\frac{1}{3}\\)", "\\(-\\frac{1}{3}\\)", "1"],
     "A", "OSC", "easy",
     "The midpoint of two opposite numbers is \\(\\frac{-x + x}{2} = 0\\)."),

    # 23
    ("On a number line, if point A is at \\(-\\frac{5}{2}\\) and point B is at \\(\\frac{5}{2}\\), what is the coordinate of the midpoint of segment AB?",
     ["0", "5", "\\(\\frac{5}{4}\\)", "-5"],
     "A", "OSC", "easy",
     "Midpoint = \\(\\frac{-5/2 + 5/2}{2} = 0\\)."),

    # 24
    ("What is the distance between \\(-\\frac{5}{2}\\) and \\(\\frac{5}{2}\\)?",
     ["5", "0", "\\(\\frac{5}{2}\\)", "10"],
     "A", "OSC", "easy",
     "Distance = \\(\\frac{5}{2} - \\left(-\\frac{5}{2}\\right) = \\frac{10}{2} = 5\\)."),

    # 25
    ("Where does the number \\(\\frac{-8}{4}\\) lie on the number line?",
     ["Exactly at the integer -2", "Between -1 and -2", "Between -2 and -3", "At zero"],
     "A", "OSC", "easy",
     "\\(\\frac{-8}{4} = -2\\), so it falls exactly on the integer tick mark -2."),

    # 26
    ("Where does \\(\\frac{15}{5}\\) lie on the number line?",
     ["Exactly at the integer 3", "Between 2 and 3", "Between 3 and 4", "At 15"],
     "A", "OSC", "easy",
     "\\(\\frac{15}{5} = 3\\), which coincides exactly with the integer 3."),

    # 27
    ("If a number line is divided into twelfths (each mark = \\(\\frac{1}{12}\\)), which mark corresponds to \\(\\frac{3}{4}\\)?",
     ["The 9th mark from 0", "The 8th mark from 0", "The 6th mark from 0", "The 7th mark from 0"],
     "A", "OSC", "easy",
     "Convert to equivalent fraction with denominator 12: \\(\\frac{3}{4} = \\frac{9}{12}\\). Thus it is the 9th mark."),

    # 28
    ("Which mark on a sixteenths number line (each mark = \\(\\frac{1}{16}\\)) corresponds to \\(\\frac{-5}{8}\\)?",
     ["The 10th mark to the left of 0",
      "The 5th mark to the left of 0",
      "The 8th mark to the left of 0",
      "The 10th mark to the right of 0"],
     "A", "OSC", "easy",
     "\\(\\frac{-5}{8} = \\frac{-10}{16}\\). It is the 10th subdivision mark to the left of zero."),

    # 29
    ("Which of the following rational numbers is closest to zero on the number line?",
     ["\\(-\\frac{1}{10}\\)", "\\(\\frac{1}{5}\\)", "\\(-\\frac{1}{3}\\)", "\\(\\frac{1}{2}\\)"],
     "A", "OSC", "medium",
     "Compare absolute values (distances from 0): \\(|-1/10| = 0.1\\), \\(|1/5| = 0.2\\), \\(|-1/3| \\approx 0.33\\), \\(|1/2| = 0.5\\). The smallest distance is 0.1, so \\(-\\frac{1}{10}\\) is closest to zero."),

    # 30
    ("Which of the following numbers is furthest to the right on the number line?",
     ["\\(\\frac{7}{3}\\)", "\\(\\frac{9}{4}\\)", "\\(2\\)", "\\(\\frac{13}{6}\\)"],
     "A", "OSC", "medium",
     "Convert to decimals: \\(\\frac{7}{3} \\approx 2.333\\), \\(\\frac{9}{4} = 2.25\\), \\(2 = 2.0\\), \\(\\frac{13}{6} \\approx 2.167\\). The largest value is \\(\\frac{7}{3}\\), so it is furthest to the right."),

    # 31
    ("Which of the following numbers is furthest to the left on the number line?",
     ["\\(-\\frac{8}{3}\\)", "\\(-\\frac{7}{3}\\)", "\\(-2\\)", "\\(-\\frac{5}{2}\\)"],
     "A", "OSC", "medium",
     "Convert to decimals: \\(-\\frac{8}{3} \\approx -2.67\\), \\(-\\frac{7}{3} \\approx -2.33\\), \\(-2 = -2.0\\), \\(-\\frac{5}{2} = -2.5\\). The smallest number is \\(-\\frac{8}{3}\\), so it lies furthest to the left."),

    # 32
    ("On the number line, if point M is at \\(\\frac{2}{3}\\) and point N is at \\(-\\frac{1}{3}\\), what is the midpoint of MN?",
     ["\\(\\frac{1}{6}\\)", "\\(\\frac{1}{3}\\)", "0", "\\(\\frac{1}{2}\\)"],
     "A", "OSC", "medium",
     "Midpoint = \\(\\frac{2/3 + (-1/3)}{2} = \\frac{1/3}{2} = \\frac{1}{6}\\)."),

    # 33
    ("On the number line, how many unit lengths are there between \\(-3\\) and \\(+4\\)?",
     ["7 units", "1 unit", "-7 units", "12 units"],
     "A", "OSC", "easy",
     "Distance = \\(4 - (-3) = 7\\) units."),

    # 34
    ("Assertion (A): The rational number \\(\\frac{4}{7}\\) lies strictly between 0 and 1 on the number line.\nReason (R): For any proper fraction \\(\\frac{p}{q}\\) where \\(0 < p < q\\), its value is strictly between 0 and 1.",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "Because \\(0 < 4 < 7\\), \\(\\frac{4}{7}\\) is a proper fraction, and all positive proper fractions lie strictly between 0 and 1 on the number line."),

    # 35
    ("Assertion (A): \\(-\\frac{3}{5}\\) lies to the right of \\(-\\frac{4}{5}\\) on the number line.\nReason (R): On the negative axis, \\(-3 > -4\\), so \\(-\\frac{3}{5} > -\\frac{4}{5}\\).",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "Since \\(-3 > -4\\), \\(-\\frac{3}{5} > -\\frac{4}{5}\\), which directly means \\(-\\frac{3}{5}\\) lies to the right of \\(-\\frac{4}{5}\\)."),

    # 36
    ("True or False: The number line extends indefinitely in both positive and negative directions.",
     ["True", "False"],
     "A", "OTF", "easy",
     "The number line is infinite in both directions, covering all real numbers from \\(-\\infty\\) to \\(+\\infty\\)."),

    # 37
    ("True or False: An improper fraction \\(\\frac{p}{q}\\) (with \\(p > q > 0\\)) always lies beyond 1 on the positive number line.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Since \\(p > q\\), \\(\\frac{p}{q} > 1\\), placing it strictly to the right of 1."),

    # 38
    ("Fill in the blank: On the number line, every rational number is represented by a _____ point.",
     ["unique", "multiple", "non-existent", "circular"],
     "A", "OFB", "easy",
     "Every rational number corresponds to exactly one unique point on the number line."),

    # 39
    ("Fill in the blank: To locate \\(-\\frac{7}{4}\\), we convert it to mixed fraction \\(-1\\frac{3}{4}\\) and divide the segment between -1 and _____ into 4 equal parts.",
     ["-2", "0", "-3", "1"],
     "A", "OFB", "easy",
     "\\(-1\\frac{3}{4}\\) lies between -1 and -2."),

    # 40
    ("What is the numerical integer coordinate of the point on the number line halfway between \\(-7\\) and \\(+3\\)?",
     ["-2", "-4", "-5", "2"],
     "A", "ONE", "easy",
     "Midpoint = \\(\\frac{-7 + 3}{2} = \\frac{-4}{2} = -2\\)."),
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    ("Find the rational number represented by point P which is the 2nd division mark from 0 to 1 when divided into 7 equal parts.",
     ["\\(\\frac{2}{7}\\)", "\\(\\frac{5}{7}\\)", "\\(\\frac{7}{2}\\)", "\\(\\frac{1}{7}\\)"],
     "A", "OSC", "easy",
     "\\(P = \\frac{2}{7}\\)."),

    # 42
    ("Find the rational number represented by point Q which is the 4th mark to the left of 0 when each unit interval has 9 subdivisions.",
     ["\\(-\\frac{4}{9}\\)", "\\(\\frac{4}{9}\\)", "\\(-\\frac{5}{9}\\)", "\\(-\\frac{9}{4}\\)"],
     "A", "OSC", "easy",
     "Moving 4 units of length \\(\\frac{1}{9}\\) to the left gives \\(-\\frac{4}{9}\\)."),

    # 43
    ("Identify the integer interval containing \\(\\frac{13}{4}\\).",
     ["Between 3 and 4", "Between 2 and 3", "Between 4 and 5", "Between 1 and 2"],
     "A", "OSC", "easy",
     "\\(\\frac{13}{4} = 3\\frac{1}{4}\\), which lies between 3 and 4."),

    # 44
    ("Identify the integer interval containing \\(-\\frac{17}{5}\\).",
     ["Between -3 and -4", "Between -2 and -3", "Between -4 and -5", "Between 3 and 4"],
     "A", "OSC", "easy",
     "\\(-\\frac{17}{5} = -3\\frac{2}{5}\\), which lies between -3 and -4."),

    # 45
    ("What is the distance between \\(\\frac{3}{8}\\) and \\(\\frac{7}{8}\\) on the number line?",
     ["\\(\\frac{1}{2}\\)", "\\(\\frac{4}{8}\\)", "\\(\\frac{5}{8}\\)", "\\(1\\)"],
     "A", "OSC", "easy",
     "Distance = \\(\\frac{7}{8} - \\frac{3}{8} = \\frac{4}{8} = \\frac{1}{2}\\)."),

    # 46
    ("What is the distance between \\(-\\frac{2}{5}\\) and \\(\\frac{3}{5}\\) on the number line?",
     ["1", "\\(\\frac{1}{5}\\)", "\\(-\\frac{1}{5}\\)", "\\(\\frac{5}{10}\\)"],
     "A", "OSC", "easy",
     "Distance = \\(\\frac{3}{5} - \\left(-\\frac{2}{5}\\right) = \\frac{5}{5} = 1\\)."),

    # 47
    ("What is the midpoint between \\(\\frac{1}{6}\\) and \\(\\frac{5}{6}\\)?",
     ["\\(\\frac{1}{2}\\)", "\\(\\frac{3}{6}\\)", "\\(\\frac{2}{3}\\)", "\\(\\frac{1}{3}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{1/6 + 5/6}{2} = \\frac{6/6}{2} = \\frac{1}{2}\\)."),

    # 48
    ("What is the midpoint between \\(-\\frac{3}{2}\\) and \\(\\frac{1}{2}\\)?",
     ["\\(-\\frac{1}{2}\\)", "\\(\\frac{1}{2}\\)", "-1", "0"],
     "A", "OSC", "easy",
     "\\(\\frac{-3/2 + 1/2}{2} = \\frac{-2/2}{2} = -\\frac{1}{2}\\)."),

    # 49
    ("Which point on the number line is 3 units to the right of \\(-1\\frac{1}{2}\\)?",
     ["\\(1\\frac{1}{2}\\)", "\\(2\\)", "\\(2\\frac{1}{2}\\)", "\\(1\\)"],
     "A", "OSC", "easy",
     "\\(-1.5 + 3 = 1.5 = 1\\frac{1}{2}\\)."),

    # 50
    ("Which point on the number line is 4 units to the left of \\(1\\frac{1}{3}\\)?",
     ["\\(-2\\frac{2}{3}\\)", "\\(-2\\frac{1}{3}\\)", "\\(-3\\)", "\\(-1\\frac{2}{3}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{4}{3} - 4 = \\frac{4 - 12}{3} = -\\frac{8}{3} = -2\\frac{2}{3}\\)."),

    # 51
    ("If point A represents \\(\\frac{-5}{7}\\) and point B represents \\(\\frac{2}{7}\\), what fraction of the distance from A to B is the origin 0?",
     ["\\(\\frac{5}{7}\\)", "\\(\\frac{2}{7}\\)", "\\(\\frac{1}{2}\\)", "\\(\\frac{3}{7}\\)"],
     "A", "OSC", "medium",
     "Total distance AB = \\(\\frac{2}{7} - \\left(-\\frac{5}{7}\\right) = \\frac{7}{7} = 1\\). Distance from A to 0 is \\(\\frac{5}{7}\\). Fraction = \\(\\frac{5/7}{1} = \\frac{5}{7}\\)."),

    # 52
    ("Between which two consecutive integers does \\(\\frac{22}{7}\\) lie?",
     ["Between 3 and 4", "Between 2 and 3", "Between 4 and 5", "Between 21 and 22"],
     "A", "OSC", "easy",
     "\\(\\frac{22}{7} = 3\\frac{1}{7}\\), which lies between 3 and 4."),

    # 53
    ("Between which two consecutive integers does \\(-\\frac{31}{6}\\) lie?",
     ["Between -5 and -6", "Between -4 and -5", "Between -6 and -7", "Between 5 and 6"],
     "A", "OSC", "easy",
     "\\(-\\frac{31}{6} = -5\\frac{1}{6}\\), which lies between -5 and -6."),

    # 54
    ("Which mark on a tenths line corresponds to \\(\\frac{-3}{5}\\)?",
     ["The 6th mark to the left of 0",
      "The 3rd mark to the left of 0",
      "The 5th mark to the left of 0",
      "The 6th mark to the right of 0"],
     "A", "OSC", "easy",
     "\\(\\frac{-3}{5} = \\frac{-6}{10}\\), which is the 6th mark to the left of 0."),

    # 55
    ("Which mark on a twentieths line corresponds to \\(\\frac{7}{4}\\)?",
     ["The 35th mark to the right of 0",
      "The 28th mark to the right of 0",
      "The 14th mark to the right of 0",
      "The 7th mark to the right of 0"],
     "A", "OSC", "medium",
     "\\(\\frac{7}{4} = \\frac{35}{20}\\). It is the 35th subdivision mark from 0."),

    # 56
    ("What is the coordinate of the point that is \\(\\frac{3}{4}\\) units to the right of \\(-\\frac{1}{2}\\)?",
     ["\\(\\frac{1}{4}\\)", "\\(-\\frac{1}{4}\\)", "\\(1\\)", "\\(\\frac{1}{2}\\)"],
     "A", "OSC", "easy",
     "\\(-\\frac{1}{2} + \\frac{3}{4} = -\\frac{2}{4} + \\frac{3}{4} = \\frac{1}{4}\\)."),

    # 57
    ("What is the coordinate of the point that is \\(\\frac{5}{6}\\) units to the left of \\(\\frac{1}{3}\\)?",
     ["\\(-\\frac{1}{2}\\)", "\\(\\frac{1}{2}\\)", "\\(-\\frac{7}{6}\\)", "\\(-\\frac{1}{6}\\)"],
     "A", "OSC", "medium",
     "\\(\\frac{1}{3} - \\frac{5}{6} = \\frac{2}{6} - \\frac{5}{6} = -\\frac{3}{6} = -\\frac{1}{2}\\)."),

    # 58
    ("Which of the following points is equidistant from \\(-2\\) and \\(+4\\)?",
     ["1", "2", "0", "-1"],
     "A", "OSC", "easy",
     "Midpoint = \\(\\frac{-2 + 4}{2} = \\frac{2}{2} = 1\\)."),

    # 59
    ("Which point is equidistant from \\(-\\frac{3}{4}\\) and \\(\\frac{7}{4}\\)?",
     ["\\(\\frac{1}{2}\\)", "1", "0", "\\(\\frac{1}{4}\\)"],
     "A", "OSC", "easy",
     "Midpoint = \\(\\frac{-3/4 + 7/4}{2} = \\frac{4/4}{2} = \\frac{1}{2}\\)."),

    # 60
    ("If point X is at \\(-\\frac{7}{3}\\) and point Y is at \\(-\\frac{1}{3}\\), find the midpoint of XY.",
     ["\\(-\\frac{4}{3}\\)", "\\(-\\frac{8}{3}\\)", "\\(-1\\)", "\\(-\\frac{2}{3}\\)"],
     "A", "OSC", "easy",
     "Midpoint = \\(\\frac{-7/3 + (-1/3)}{2} = \\frac{-8/3}{2} = -\\frac{4}{3}\\)."),

    # 61
    ("Where does \\(\\frac{0}{7}\\) lie on the number line?",
     ["Exactly at zero", "To the right of zero", "To the left of zero", "Between 0 and 1"],
     "A", "OSC", "easy",
     "\\(\\frac{0}{7} = 0\\), which is the origin 0."),

    # 62
    ("Where does \\(\\frac{8}{-2}\\) lie on the number line?",
     ["At -4", "At +4", "Between -3 and -4", "Between 3 and 4"],
     "A", "OSC", "easy",
     "\\(\\frac{8}{-2} = -4\\)."),

    # 63
    ("On a number line, which integer is closest to \\(\\frac{17}{3}\\)?",
     ["6", "5", "7", "17"],
     "A", "OSC", "easy",
     "\\(\\frac{17}{3} = 5\\frac{2}{3} \\approx 5.67\\). Distance to 6 is \\(0.33\\) while distance to 5 is \\(0.67\\). Thus 6 is closest."),

    # 64
    ("Which integer is closest to \\(-\\frac{19}{4}\\)?",
     ["-5", "-4", "-6", "-19"],
     "A", "OSC", "easy",
     "\\(-\\frac{19}{4} = -4.75\\). Distance to -5 is 0.25 while distance to -4 is 0.75. So -5 is closest."),

    # 65
    ("True or False: Every point on a calibrated number line represents a unique real number.",
     ["True", "False"],
     "A", "OTF", "easy",
     "There is a one-to-one correspondence between the points on the number line and the real numbers."),

    # 66
    ("True or False: Rational numbers with the same denominator have equal distances between consecutive multiples.",
     ["True", "False"],
     "A", "OTF", "easy",
     "For any fixed denominator \\(q\\), the distance between \\(\\frac{k}{q}\\) and \\(\\frac{k+1}{q}\\) is uniformly \\(\\frac{1}{q}\\)."),

    # 67
    ("True or False: The number \\(-\\frac{1}{100}\\) lies to the right of zero.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Any negative quantity lies strictly to the left of zero."),

    # 68
    ("Fill in the blank: To plot \\(\\frac{p}{q}\\), the unit segment is divided into _____ equal parts.",
     ["\\(q\\)", "\\(p\\)", "\\(p+q\\)", "\\(p-q\\)"],
     "A", "OFB", "easy",
     "The denominator \\(q\\) determines the number of equal sub-divisions per unit length."),

    # 69
    ("Fill in the blank: The point halfway between two numbers \\(a\\) and \\(b\\) on the number line is given by _____.",
     ["\\(\\frac{a+b}{2}\\)", "\\(a-b\\)", "\\(a \\times b\\)", "\\(\\frac{a-b}{2}\\)"],
     "A", "OFB", "easy",
     "The midpoint of \\(a\\) and \\(b\\) is their arithmetic mean \\(\\frac{a+b}{2}\\)."),

    # 70
    ("What is the numerical integer value of the distance between \\(-8\\) and \\(+8\\) on the number line?",
     ["16", "0", "8", "-16"],
     "A", "ONE", "easy",
     "Distance = \\(8 - (-8) = 16\\)."),
]

# 12 MOCK / FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Unit Length Division into 4 Equal Quarters</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Horizontal Axis from 0 to 1 -->
    <line x1="30" y1="75" x2="310" y2="75" stroke="#64748b" stroke-width="3"/>
    <!-- Tick 0 -->
    <line x1="50" y1="65" x2="50" y2="85" stroke="#f8fafc" stroke-width="3"/>
    <text x="50" y="105" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">0</text>
    <!-- Tick 1/4 -->
    <line x1="105" y1="68" x2="105" y2="82" stroke="#38bdf8" stroke-width="2"/>
    <text x="105" y="60" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">1/4</text>
    <!-- Tick 2/4 = 1/2 -->
    <line x1="160" y1="68" x2="160" y2="82" stroke="#38bdf8" stroke-width="2"/>
    <text x="160" y="60" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">2/4</text>
    <!-- Tick 3/4 (Target P) -->
    <circle cx="215" cy="75" r="6" fill="#f59e0b" stroke="#fbbf24" stroke-width="2"/>
    <text x="215" y="55" fill="#fde047" font-size="13" font-weight="bold" text-anchor="middle">P (3/4)</text>
    <line x1="215" y1="68" x2="215" y2="82" stroke="#f59e0b" stroke-width="2"/>
    <!-- Tick 4/4 = 1 -->
    <line x1="270" y1="65" x2="270" y2="85" stroke="#f8fafc" stroke-width="3"/>
    <text x="270" y="105" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">1</text>
    <!-- Sub-interval width label -->
    <text x="170" y="132" fill="#94a3b8" font-size="11" text-anchor="middle">Each subdivision = 1/4 unit width</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">On the number line shown, what rational number does point P represent?</p>
</div>""",
     ["\\(\\frac{3}{4}\\)", "\\(\\frac{2}{4}\\)", "\\(\\frac{1}{4}\\)", "\\(\\frac{4}{3}\\)"],
     "A", "OSC", "easy",
     "Point P is the 3rd subdivision mark to the right of 0 on a line partitioned into 4 equal segments per unit, representing \\(\\frac{3}{4}\\)."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Negative Rational Number Partitioning (0 to -1)</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Horizontal Axis from -1 to 0 -->
    <line x1="30" y1="75" x2="310" y2="75" stroke="#64748b" stroke-width="3"/>
    <!-- Tick -1 -->
    <line x1="50" y1="65" x2="50" y2="85" stroke="#f8fafc" stroke-width="3"/>
    <text x="50" y="105" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">-1</text>
    <!-- Tick -5/6 -->
    <circle cx="85" cy="75" r="5" fill="#ef4444"/>
    <text x="85" y="60" fill="#f87171" font-size="10" font-weight="bold" text-anchor="middle">-5/6</text>
    <!-- Tick -4/6 -->
    <line x1="120" y1="68" x2="120" y2="82" stroke="#64748b"/>
    <!-- Tick -3/6 = -1/2 (Point M) -->
    <circle cx="155" cy="75" r="6" fill="#10b981" stroke="#34d399" stroke-width="2"/>
    <text x="155" y="55" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">M (-1/2)</text>
    <!-- Tick -2/6 -->
    <line x1="190" y1="68" x2="190" y2="82" stroke="#64748b"/>
    <!-- Tick -1/6 -->
    <line x1="225" y1="68" x2="225" y2="82" stroke="#64748b"/>
    <!-- Tick 0 -->
    <line x1="260" y1="65" x2="260" y2="85" stroke="#f8fafc" stroke-width="3"/>
    <text x="260" y="105" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">0</text>
    <!-- Footnote -->
    <text x="170" y="132" fill="#cbd5e1" font-size="11" text-anchor="middle">Counting 3 steps left from 0 gives -3/6 = -1/2</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the coordinate of point M located at the exact midpoint between -1 and 0?</p>
</div>""",
     ["\\(-\\frac{1}{2}\\)", "\\(-\\frac{1}{4}\\)", "\\(-\\frac{3}{4}\\)", "\\(\\frac{1}{2}\\)"],
     "A", "OSC", "easy",
     "The midpoint of -1 and 0 is \\(\\frac{-1 + 0}{2} = -\\frac{1}{2}\\)."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Locating Improper Fractions: 7/4 = 1 + 3/4</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Horizontal Axis from 0 to 2 -->
    <line x1="20" y1="75" x2="320" y2="75" stroke="#64748b" stroke-width="2.5"/>
    <!-- Integer 0 -->
    <line x1="40" y1="65" x2="40" y2="85" stroke="#f8fafc" stroke-width="2"/>
    <text x="40" y="105" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">0</text>
    <!-- Integer 1 -->
    <line x1="160" y1="65" x2="160" y2="85" stroke="#f8fafc" stroke-width="2"/>
    <text x="160" y="105" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">1</text>
    <!-- Integer 2 -->
    <line x1="280" y1="65" x2="280" y2="85" stroke="#f8fafc" stroke-width="2"/>
    <text x="280" y="105" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">2</text>
    <!-- Subdivisions between 1 and 2 -->
    <line x1="190" y1="70" x2="190" y2="80" stroke="#94a3b8"/>
    <line x1="220" y1="70" x2="220" y2="80" stroke="#94a3b8"/>
    <!-- Target Point 7/4 = 1 3/4 -->
    <circle cx="250" cy="75" r="6" fill="#f59e0b" stroke="#fbbf24" stroke-width="2"/>
    <text x="250" y="55" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">7/4 (1 ¾)</text>
    <!-- Rule Card -->
    <text x="170" y="132" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Convert 7/4 to 1 ¾: 3rd quarter past 1 toward 2</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Between which two integers is the improper fraction \(\frac{7}{4}\) located?</p>
</div>""",
     ["Between 1 and 2", "Between 0 and 1", "Between 2 and 3", "Between 7 and 8"],
     "A", "OSC", "easy",
     "\\(\\frac{7}{4} = 1\\frac{3}{4}\\), which lies strictly between integers 1 and 2."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Locating Negative Improper Fraction: -5/3 = -1 ⅔</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Line from -2 to 0 -->
    <line x1="20" y1="75" x2="320" y2="75" stroke="#64748b" stroke-width="2.5"/>
    <!-- Tick -2 -->
    <line x1="60" y1="65" x2="60" y2="85" stroke="#f8fafc" stroke-width="2"/>
    <text x="60" y="105" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">-2</text>
    <!-- Target Point -5/3 = -1 2/3 -->
    <circle cx="100" cy="75" r="6" fill="#ef4444" stroke="#f87171" stroke-width="2"/>
    <text x="100" y="55" fill="#fca5a5" font-size="12" font-weight="bold" text-anchor="middle">-5/3</text>
    <!-- Tick -4/3 = -1 1/3 -->
    <line x1="140" y1="70" x2="140" y2="80" stroke="#94a3b8"/>
    <!-- Tick -1 -->
    <line x1="180" y1="65" x2="180" y2="85" stroke="#f8fafc" stroke-width="2"/>
    <text x="180" y="105" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">-1</text>
    <!-- Tick 0 -->
    <line x1="300" y1="65" x2="300" y2="85" stroke="#f8fafc" stroke-width="2"/>
    <text x="300" y="105" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">0</text>
    <!-- Footnote -->
    <text x="170" y="132" fill="#fbbf24" font-size="11" text-anchor="middle">-5/3 = -1 ⅔ lies 2/3 of the way from -1 toward -2</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Between which two integers does \(-\frac{5}{3}\) lie on the number line?</p>
</div>""",
     ["Between -1 and -2", "Between 0 and -1", "Between -2 and -3", "Between 1 and 2"],
     "A", "OSC", "easy",
     "\\(-\\frac{5}{3} = -1\\frac{2}{3}\\), which lies between -1 and -2 on the negative axis."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Comparison of Multiple Points: P, Q, R, S</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Main axis -->
    <line x1="20" y1="75" x2="320" y2="75" stroke="#64748b" stroke-width="2"/>
    <!-- Origin 0 -->
    <circle cx="170" cy="75" r="4" fill="#f8fafc"/>
    <text x="170" y="95" fill="#f8fafc" font-size="11" text-anchor="middle">0</text>
    <!-- Point P: -3/2 -->
    <circle cx="60" cy="75" r="6" fill="#ef4444"/>
    <text x="60" y="60" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">P (-1.5)</text>
    <!-- Point Q: -1/2 -->
    <circle cx="125" cy="75" r="6" fill="#f59e0b"/>
    <text x="125" y="60" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Q (-0.5)</text>
    <!-- Point R: +3/4 -->
    <circle cx="225" cy="75" r="6" fill="#10b981"/>
    <text x="225" y="60" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">R (0.75)</text>
    <!-- Point S: +7/4 -->
    <circle cx="285" cy="75" r="6" fill="#3b82f6"/>
    <text x="285" y="60" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">S (1.75)</text>
    <!-- Order rule -->
    <text x="170" y="130" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">Order: P &lt; Q &lt; 0 &lt; R &lt; S</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Based on the positions on the number line, which point has the smallest value?</p>
</div>""",
     ["Point P", "Point Q", "Point R", "Point S"],
     "A", "OSC", "easy",
     "Point P is furthest to the left (\\(-1.5\\)), so it represents the smallest value."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Equidistant Invariance around Zero</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Axis -->
    <line x1="30" y1="80" x2="310" y2="80" stroke="#64748b" stroke-width="2.5"/>
    <!-- Origin 0 -->
    <circle cx="170" cy="80" r="5" fill="#f8fafc"/>
    <text x="170" y="105" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">0</text>
    <!-- Left Point -5/7 -->
    <circle cx="80" cy="80" r="6" fill="#ef4444"/>
    <text x="80" y="62" fill="#f87171" font-size="12" font-weight="bold" text-anchor="middle">-5/7</text>
    <!-- Right Point +5/7 -->
    <circle cx="260" cy="80" r="6" fill="#10b981"/>
    <text x="260" y="62" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">+5/7</text>
    <!-- Symmetric Arcs -->
    <path d="M 80,72 Q 125,40 170,72" fill="none" stroke="#f87171" stroke-width="2" stroke-dasharray="4"/>
    <path d="M 170,72 Q 215,40 260,72" fill="none" stroke="#34d399" stroke-width="2" stroke-dasharray="4"/>
    <text x="125" y="45" fill="#cbd5e1" font-size="10" text-anchor="middle">d = 5/7</text>
    <text x="215" y="45" fill="#cbd5e1" font-size="10" text-anchor="middle">d = 5/7</text>
    <!-- Footnote -->
    <text x="170" y="132" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Opposite rational numbers are reflections across 0</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the distance of \(-\frac{5}{7}\) from the origin \(0\)?</p>
</div>""",
     ["\\(\\frac{5}{7}\\) units", "\\(-\\frac{5}{7}\\) units", "0 units", "\\(\\frac{10}{7}\\) units"],
     "A", "OSC", "easy",
     "Distance is always non-negative: \\(|-5/7 - 0| = \\frac{5}{7}\\) units."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Fraction Subdivisions: Finding Intermediate Tenths</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Number line from 0 to 1 -->
    <line x1="30" y1="75" x2="310" y2="75" stroke="#64748b" stroke-width="2.5"/>
    <line x1="40" y1="65" x2="40" y2="85" stroke="#f8fafc" stroke-width="2"/>
    <text x="40" y="105" fill="#f8fafc" font-size="12" text-anchor="middle">0</text>
    <!-- 10 subdivisions -->
    <line x1="66" y1="70" x2="66" y2="80" stroke="#94a3b8"/>
    <line x1="92" y1="70" x2="92" y2="80" stroke="#94a3b8"/>
    <line x1="118" y1="70" x2="118" y2="80" stroke="#94a3b8"/>
    <line x1="144" y1="70" x2="144" y2="80" stroke="#94a3b8"/>
    <line x1="170" y1="68" x2="170" y2="82" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="60" fill="#38bdf8" font-size="10" text-anchor="middle">5/10 = 1/2</text>
    <!-- 8th tick: 8/10 = 4/5 -->
    <circle cx="248" cy="75" r="5" fill="#10b981"/>
    <text x="248" y="60" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">4/5</text>
    <line x1="300" y1="65" x2="300" y2="85" stroke="#f8fafc" stroke-width="2"/>
    <text x="300" y="105" fill="#f8fafc" font-size="12" text-anchor="middle">1</text>
    <!-- Note -->
    <text x="170" y="132" fill="#fbbf24" font-size="11" text-anchor="middle">8th mark = 8/10 = 4/5 (equivalent fraction placement)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Which mark from 0 represents \(\frac{4}{5}\) on a line divided into tenths?</p>
</div>""",
     ["The 8th mark", "The 4th mark", "The 5th mark", "The 9th mark"],
     "A", "OSC", "easy",
     "\\(\\frac{4}{5} = \\frac{8}{10}\\), so it corresponds to the 8th subdivision mark."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Distance Between Two Rationals: |b - a|</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Axis -->
    <line x1="30" y1="75" x2="310" y2="75" stroke="#64748b" stroke-width="2"/>
    <!-- Point A = -3/4 -->
    <circle cx="80" cy="75" r="5" fill="#ef4444"/>
    <text x="80" y="95" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">A = -3/4</text>
    <!-- Point B = +1/4 -->
    <circle cx="240" cy="75" r="5" fill="#10b981"/>
    <text x="240" y="95" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">B = +1/4</text>
    <!-- Origin mark -->
    <circle cx="200" cy="75" r="3" fill="#f8fafc"/>
    <text x="200" y="95" fill="#f8fafc" font-size="10" text-anchor="middle">0</text>
    <!-- Measurement bracket -->
    <line x1="80" y1="50" x2="240" y2="50" stroke="#f59e0b" stroke-width="2"/>
    <line x1="80" y1="45" x2="80" y2="55" stroke="#f59e0b" stroke-width="2"/>
    <line x1="240" y1="45" x2="240" y2="55" stroke="#f59e0b" stroke-width="2"/>
    <text x="160" y="42" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Distance = 1/4 - (-3/4) = 4/4 = 1 unit</text>
    <!-- Banner -->
    <text x="170" y="130" fill="#38bdf8" font-size="11" text-anchor="middle">Distance is always independent of the chosen direction</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the distance between \(A = -\frac{3}{4}\) and \(B = \frac{1}{4}\)?</p>
</div>""",
     ["1 unit", "\\(\\frac{1}{2}\\) unit", "\\(\\frac{1}{4}\\) unit", "\\(2\\) units"],
     "A", "OSC", "easy",
     "\\(\\frac{1}{4} - \\left(-\\frac{3}{4}\\right) = \\frac{4}{4} = 1\\) unit."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Midpoint of Two Rational Coordinates</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Segment line -->
    <line x1="40" y1="75" x2="300" y2="75" stroke="#64748b" stroke-width="2.5"/>
    <!-- Left endpoint -1/2 -->
    <circle cx="60" cy="75" r="6" fill="#3b82f6"/>
    <text x="60" y="55" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">A = -1/2</text>
    <!-- Right endpoint +3/2 -->
    <circle cx="280" cy="75" r="6" fill="#3b82f6"/>
    <text x="280" y="55" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">B = +3/2</text>
    <!-- Midpoint M -->
    <circle cx="170" cy="75" r="7" fill="#10b981" stroke="#34d399" stroke-width="2"/>
    <text x="170" y="55" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">M = 1/2</text>
    <line x1="170" y1="65" x2="170" y2="85" stroke="#10b981" stroke-width="2"/>
    <!-- Calculation footnote -->
    <text x="170" y="115" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">M = [ (-1/2) + 3/2 ] / 2 = (1) / 2 = 1/2</text>
    <text x="170" y="135" fill="#cbd5e1" font-size="10" text-anchor="middle">Distance AM = Distance MB = 1 unit</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the midpoint between \(A = -\frac{1}{2}\) and \(B = \frac{3}{2}\)?</p>
</div>""",
     ["\\(\\frac{1}{2}\\)", "1", "0", "\\(-\\frac{1}{2}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{-1/2 + 3/2}{2} = \\frac{1}{2}\\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Fraction Shifting Right: Addition of Offset</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Base Axis -->
    <line x1="30" y1="80" x2="310" y2="80" stroke="#64748b" stroke-width="2.5"/>
    <!-- Start Point -1/2 -->
    <circle cx="80" cy="80" r="6" fill="#ef4444"/>
    <text x="80" y="105" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">Start: -1/2</text>
    <!-- Shift arrow of length 3/4 -->
    <path d="M 85,65 Q 155,30 225,65" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
    <polygon points="225,60 232,68 222,70" fill="#f59e0b"/>
    <text x="155" y="40" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">+ 3/4 to the right</text>
    <!-- End Point +1/4 -->
    <circle cx="230" cy="80" r="6" fill="#10b981"/>
    <text x="230" y="105" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">End: +1/4</text>
    <!-- Calculation footnote -->
    <text x="170" y="132" fill="#38bdf8" font-size="11" text-anchor="middle">-1/2 + 3/4 = -2/4 + 3/4 = 1/4</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Starting at \(-\frac{1}{2}\) and moving \(\frac{3}{4}\) units to the right lands at which coordinate?</p>
</div>""",
     ["\\(\\frac{1}{4}\\)", "\\(-\\frac{1}{4}\\)", "\\(1\\)", "\\(\\frac{1}{2}\\)"],
     "A", "OSC", "easy",
     "\\(-\\frac{1}{2} + \\frac{3}{4} = -\\frac{2}{4} + \\frac{3}{4} = \\frac{1}{4}\\)."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Ordering Fractions on Number Line</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Scale axis -->
    <line x1="20" y1="75" x2="320" y2="75" stroke="#64748b" stroke-width="2"/>
    <!-- Points: -7/12, -4/12, +5/12, +11/12 -->
    <circle cx="50" cy="75" r="5" fill="#ef4444"/>
    <text x="50" y="60" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">-7/12</text>
    <circle cx="110" cy="75" r="5" fill="#f59e0b"/>
    <text x="110" y="60" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">-4/12</text>
    <circle cx="160" cy="75" r="3" fill="#f8fafc"/>
    <text x="160" y="95" fill="#f8fafc" font-size="10" text-anchor="middle">0</text>
    <circle cx="220" cy="75" r="5" fill="#10b981"/>
    <text x="220" y="60" fill="#6ee7b7" font-size="10" font-weight="bold" text-anchor="middle">+5/12</text>
    <circle cx="290" cy="75" r="5" fill="#3b82f6"/>
    <text x="290" y="60" fill="#93c5fd" font-size="10" font-weight="bold" text-anchor="middle">+11/12</text>
    <!-- Ordering statement -->
    <text x="170" y="130" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">-7/12 &lt; -4/12 &lt; 0 &lt; 5/12 &lt; 11/12</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Which of the marked fractions is greatest in value?</p>
</div>""",
     ["\\(\\frac{11}{12}\\)", "\\(\\frac{5}{12}\\)", "\\(-\\frac{4}{12}\\)", "\\(-\\frac{7}{12}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{11}{12}\\) lies furthest to the right, so it is greatest."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;text-align:center;color:#f8fafc;font-family:sans-serif;">
  <h4 style="margin:0 0 10px 0;color:#38bdf8;">Mixed Number Decomposition on Number Line</h4>
  <svg width="340" height="150" viewBox="0 0 340 150" style="background:#1e293b;border-radius:6px;">
    <!-- Whole number part card -->
    <rect x="25" y="30" width="130" height="60" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2"/>
    <text x="90" y="55" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">Improper: 11 / 4</text>
    <text x="90" y="75" fill="#ffffff" font-size="12" text-anchor="middle">= 2 + 3/4</text>
    <!-- Arrow -->
    <path d="M 165,60 L 195,60" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <polygon points="195,55 205,60 195,65" fill="#f59e0b"/>
    <!-- Position on axis card -->
    <rect x="205" y="30" width="115" height="60" rx="6" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="262" y="55" fill="#6ee7b7" font-size="12" font-weight="bold" text-anchor="middle">Interval [2, 3]</text>
    <text x="262" y="75" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">3rd quarter tick</text>
    <!-- Footnote -->
    <text x="170" y="125" fill="#fde047" font-size="11" text-anchor="middle">Quotient gives lower integer; remainder/divisor gives fractional offset</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What integer interval and fractional offset represent \(\frac{11}{4}\)?</p>
</div>""",
     ["Between 2 and 3, offset \\(\\frac{3}{4}\\)",
      "Between 1 and 2, offset \\(\\frac{3}{4}\\)",
      "Between 3 and 4, offset \\(\\frac{1}{4}\\)",
      "Between 2 and 3, offset \\(\\frac{1}{4}\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{11}{4} = 2\\frac{3}{4}\\), so it is between 2 and 3 at offset \\(\\frac{3}{4}\\).")
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch3_topic3.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
