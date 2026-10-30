# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 6: Statistics - Topic 6.5: Histogram and Frequency Polygon (MH-10-MTH1-6-6.5)
Total: 82 Canonical Questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# TOPIC 6.5: Histogram and Frequency Polygon Construction
t65_exam = [
    # 1
    ("What is a 'Histogram' in statistics?",
     ["A two-dimensional graphical representation of continuous grouped frequency data consisting of adjacent rectangles with no gaps between them",
      "A circular diagram divided into sectors",
      "A line graph plotting only cumulative frequencies",
      "A bar chart with wide gaps between bars"],
     "A", "OSC", "easy",
     "A histogram is a continuous rectangular graph where class intervals lie on the X-axis and frequencies on the Y-axis with zero gaps between adjacent bars."),

    # 2
    ("Which statistical variable is represented along the horizontal X-axis in a histogram?",
     ["Continuous Class Intervals", "Frequencies", "Cumulative frequencies", "Central angles"],
     "A", "OSC", "easy",
     "The continuous class limits are plotted along the horizontal X-axis."),

    # 3
    ("Which statistical variable is represented along the vertical Y-axis in a histogram?",
     ["Frequencies (\\(f_i\\))", "Class marks", "Upper limits", "Class sizes"],
     "A", "OSC", "easy",
     "Frequencies of the class intervals are plotted on the vertical Y-axis."),

    # 4
    ("What is the zigzag mark (or kink mark) drawn on the X-axis between the origin \\((0,0)\\) and the first class boundary called, and why is it drawn?",
     ["Krink mark, drawn to indicate that numbers between 0 and the first class boundary have been omitted from the scale",
      "Broken line indicating an error in the graph",
      "Divider between positive and negative numbers",
      "Mark representing 100 units"],
     "A", "OSC", "easy",
     "The krink mark (zigzag line) indicates scale compression, showing that the range from 0 to the first class limit has been omitted without starting from origin."),

    # 5
    ("When is a krink mark NOT required on the X-axis of a histogram?",
     ["When the very first class interval begins at zero (e.g. 0-10)",
      "When class sizes are unequal",
      "When frequencies are small",
      "When drawing on graph paper"],
     "A", "OSC", "easy",
     "If the first class starts at 0, no numbers are skipped, so no krink mark is needed."),

    # 6
    ("Why must class intervals be strictly continuous before constructing a histogram?",
     ["Because rectangles in a histogram must touch each other with zero gaps at common boundaries",
      "Because graph paper cannot plot discontinuous lines",
      "Because frequencies would become negative",
      "Because of computer software limitations"],
     "A", "OSC", "easy",
     "Rectangles must be adjacent without gaps; any discontinuity (e.g. 1-10, 11-20) creates artificial gaps, so continuous boundaries (0.5-10.5, 10.5-20.5) are required."),

    # 7
    ("What is a 'Frequency Polygon'?",
     ["A closed geometric figure formed by joining the midpoints of the tops of the rectangles of a histogram with straight line segments",
      "A polygon having 100 sides",
      "A circle divided into triangles",
      "A bar chart with triangular tops"],
     "A", "OSC", "easy",
     "A frequency polygon is a line graph formed by connecting the midpoints of the class intervals (class marks) at their respective frequency heights."),

    # 8
    ("How is a frequency polygon closed at both ends to complete a polygon?",
     ["By joining the ends to the X-axis at the class marks of the imaginary preceding and succeeding classes of zero frequency",
      "By joining both ends directly to the origin (0,0)",
      "By connecting the first point to the last point directly",
      "By drawing vertical lines down to the Y-axis"],
     "A", "OSC", "medium",
     "To close the polygon, an imaginary class with frequency 0 is added before the first class and after the last class, and the polygon is brought down to their class marks on the X-axis."),

    # 9
    ("Can a Frequency Polygon be constructed WITHOUT drawing a histogram first?",
     ["Yes, by directly plotting the points \\((x_i, f_i)\\) where \\(x_i\\) is the class mark, and joining them with straight line segments",
      "No, a histogram is always mandatory",
      "Only for data with 3 classes",
      "Only if ogives are drawn"],
     "A", "OSC", "easy",
     "A frequency polygon can be constructed directly by plotting coordinates of class mark vs frequency \\((x_i, f_i)\\) and joining them sequentially."),

    # 10
    ("What is the relationship between the total area enclosed by a Frequency Polygon and the total area of the corresponding Histogram?",
     ["The area of the Frequency Polygon is EXACTLY equal to the area of the Histogram",
      "The Frequency Polygon has half the area",
      "The Frequency Polygon has double the area",
      "There is no fixed relation between their areas"],
     "A", "OSC", "medium",
     "The triangular areas excluded from the rectangles equal the triangular areas included outside them, making the total enclosed area of the polygon identical to the histogram."),

    # 11
    ("If the classes of a histogram are \\(20-30, 30-40, 40-50\\), what is the class mark of the imaginary preceding class added to close the frequency polygon?",
     ["\\(15\\) (class mark of imaginary interval 10-20)", "\\(25\\)", "\\(10\\)", "\\(0\\)"],
     "A", "OSC", "easy",
     "The imaginary preceding class is \\(10 - 20\\), whose class mark is \\(\\frac{10 + 20}{2} = 15\\)."),

    # 12
    ("In Question 11, what is the class mark of the imaginary succeeding class added to close the frequency polygon?",
     ["\\(55\\) (class mark of imaginary interval 50-60)", "\\(50\\)", "\\(60\\)", "\\(65\\)"],
     "A", "OSC", "easy",
     "The imaginary succeeding class is \\(50 - 60\\), whose class mark is \\(\\frac{50 + 60}{2} = 55\\)."),

    # 13
    ("In a histogram, what does the width of each rectangular bar represent?",
     ["The class width (or class size \\(h\\))", "The frequency", "The class mark", "The cumulative frequency"],
     "A", "OSC", "easy",
     "The base of each rectangle corresponds to the class interval width on the X-axis."),

    # 14
    ("In a histogram, what does the height of each rectangular bar represent?",
     ["The frequency of that class interval", "The class mark", "The upper class limit", "The total sample size"],
     "A", "OSC", "easy",
     "The vertical height of each rectangle corresponds to the class frequency on the Y-axis."),

    # 15
    ("What does the area of each rectangle in a histogram represent when class widths are uniform?",
     ["It is proportional to the frequency of that class",
      "The cumulative frequency",
      "The mean of the class",
      "The total population"],
     "A", "OSC", "easy",
     "Area \\(= \\text{width} \\times \\text{height} = h \\times f_i\\), which is directly proportional to frequency."),

    # 16
    ("If class intervals are discontinuous: \\(6-10, 11-15, 16-20\\), what are the continuous class intervals for drawing a histogram?",
     ["\\(5.5-10.5, 10.5-15.5, 15.5-20.5\\)",
      "\\(6-11, 11-16, 16-21\\)",
      "\\(5-10, 10-15, 15-20\\)",
      "\\(6.5-10.5, 11.5-15.5\\)"],
     "A", "OSC", "easy",
     "Lower limits are reduced by 0.5 and upper limits increased by 0.5: \\(5.5-10.5, 10.5-15.5, 15.5-20.5\\)."),

    # 17
    ("What are the coordinates plotted to draw a frequency polygon without a histogram for the class \\(10 - 20\\) with frequency \\(7\\)?",
     ["\\((15, 7)\\)", "\\((10, 7)\\)", "\\((20, 7)\\)", "\\((7, 15)\\)"],
     "A", "OSC", "easy",
     "The coordinates are \\((x_i, f_i)\\). For class \\(10 - 20\\), class mark \\(x_i = 15\\) and frequency is 7, so point is \\((15, 7)\\)."),

    # 18
    ("For classes \\(0-10\\) (freq 4), \\(10-20\\) (freq 8), \\(20-30\\) (freq 6), what are the coordinates of the 3 points plotted?",
     ["\\((5, 4), (15, 8), (25, 6)\\)",
      "\\((0, 4), (10, 8), (20, 6)\\)",
      "\\((10, 4), (20, 8), (30, 6)\\)",
      "\\((4, 5), (8, 15), (6, 25)\\)"],
     "A", "OSC", "easy",
     "Class marks are 5, 15, 25. Points plotted are \\((5, 4), (15, 8), (25, 6)\\)."),

    # 19
    ("In Question 18, to which points on the X-axis will the frequency polygon be extended to close it?",
     ["\\((-5, 0)\\) and \\((35, 0)\\)", "\\((0, 0)\\) and \\((30, 0)\\)", "\\((5, 0)\\) and \\((25, 0)\\)", "\\((-10, 0)\\) and \\((40, 0)\\)"],
     "A", "OSC", "medium",
     "Imaginary preceding class is \\(-10 - 0\\) with midpoint \\(-5\\); succeeding class is \\(30 - 40\\) with midpoint \\(35\\). Points on X-axis: \\((-5, 0)\\) and \\((35, 0)\\)."),

    # 20
    ("Can two frequency polygons of different distributions be drawn on the SAME axes to compare their performance?",
     ["Yes, frequency polygons are ideal for comparing two or more distributions on the same graph",
      "No, only one polygon is allowed per graph sheet",
      "Only if both distributions have identical means",
      "Only for circular data"],
     "A", "OSC", "easy",
     "Because frequency polygons consist of clean lines rather than solid bars, multiple distributions can easily be overlaid on the same graph for visual comparison."),

    # 21
    ("Why can two histograms NOT be easily overlaid on the same graph to compare two distributions?",
     ["Because their solid rectangular bars would overlap and obscure each other",
      "Because histograms have no heights",
      "Because graph sheets are too small",
      "Because class marks would conflict"],
     "A", "OSC", "easy",
     "Overlapping solid rectangular bars obscure visual clarity, making frequency polygons far superior for comparing two sets of data simultaneously."),

    # 22
    ("What tool is used to find the Mode graphically from a Histogram?",
     ["Connecting the top vertices of the modal rectangle to the adjacent upper corners of neighboring rectangles and dropping a perpendicular from the intersection to the X-axis",
      "Measuring the area of the smallest bar",
      "Drawing a diagonal across the entire page",
      "Reading the Y-intercept"],
     "A", "OSC", "easy",
     "The intersection of diagonal lines across the peak rectangle projects down to the mode on the X-axis."),

    # 23
    ("In a histogram, if the class intervals are \\(100-150, 150-200, 200-250\\), what scale on the X-axis is indicated?",
     ["\\(1\\text{ cm} = 50\\text{ units}\\)", "\\(1\\text{ cm} = 100\\text{ units}\\)", "\\(1\\text{ cm} = 25\\text{ units}\\)", "\\(1\\text{ cm} = 10\\text{ units}\\)"],
     "A", "OSC", "easy",
     "Each step is \\(150 - 100 = 50\\) units, which corresponds to \\(1\\text{ cm} = 50\\) units on graph paper."),

    # 24
    ("If the frequencies are \\(15, 30, 45, 20\\), what is a suitable Y-axis scale on graph paper?",
     ["\\(1\\text{ cm} = 5\\text{ units}\\) (or \\(10\\text{ units}\\))",
      "\\(1\\text{ cm} = 50\\text{ units}\\)",
      "\\(1\\text{ cm} = 100\\text{ units}\\)",
      "\\(1\\text{ cm} = 1\\text{ unit}\\)"],
     "A", "OSC", "easy",
     "A scale of \\(1\\text{ cm} = 5\\) or 10 units comfortably spans the range 0 to 50 on standard 15-20 cm graph sheets."),

    # 25
    ("What is written at the top right corner of a graph sheet when constructing a histogram or frequency polygon?",
     ["Scale for X-axis and Y-axis (e.g. On X-axis: 1 cm = ..., On Y-axis: 1 cm = ...)",
      "Student roll number only",
      "Title of the textbook",
      "The formula for mode"],
     "A", "OSC", "easy",
     "Every statistical graph must clearly display the chosen Scale for both axes in the top right corner."),

    # 26
    ("What are the points of a frequency polygon connected with?",
     ["Straight line segments using a ruler", "Freehand smooth curves", "Circular arcs", "Dotted zigzags"],
     "A", "OSC", "easy",
     "By definition, a polygon is formed by straight line segments drawn with a ruler connecting consecutive points."),

    # 27
    ("What is a smooth, freehand curve drawn through the points of a frequency polygon called?",
     ["Frequency Curve", "Histogram", "Ogive", "Pie chart"],
     "A", "OSC", "easy",
     "A smooth freehand curve passing through the points rather than ruler line segments is called a Frequency Curve."),

    # 28
    ("In a histogram, the heights of rectangles are \\(6, 14, 20, 10, 4\\). Which interval contains the Mode?",
     ["The third interval (height 20, the highest bar)",
      "The first interval",
      "The middle interval always",
      "The last interval"],
     "A", "OSC", "easy",
     "The highest bar (height 20) represents the modal class containing the mode."),

    # 29
    ("Can frequencies on the Y-axis be negative?",
     ["No, count of observations is always non-negative",
      "Yes, for loss-making companies",
      "Yes, below the X-axis",
      "Only for debt funds"],
     "A", "OSC", "easy",
     "Frequencies represent counts of real occurrences, which can never be negative; thus histograms always stay on or above the X-axis."),

    # 30
    ("What shape does a histogram take for a symmetric bell-shaped normal distribution?",
     ["Tallest in the center, tapering symmetrically down on both left and right sides",
      "Flat horizontal line",
      "A straight upward ramp",
      "U-shaped with peak at ends"],
     "A", "OSC", "easy",
     "A normal distribution produces a symmetric bell-shaped histogram with peak in the middle."),

    # 31
    ("If a histogram has two distinct peaks of equal or near-equal height, what is the distribution called?",
     ["Bimodal distribution", "Unimodal distribution", "Normal distribution", "Uniform distribution"],
     "A", "OSC", "easy",
     "A distribution showing two separate peaks is called bimodal."),

    # 32
    ("If all rectangles in a histogram have the exact same height, what is the distribution called?",
     ["Uniform (or rectangular) distribution", "Normal distribution", "Skewed distribution", "Exponential distribution"],
     "A", "OSC", "easy",
     "When every interval has identical frequency, the distribution is called a uniform distribution."),

    # 33
    ("When constructing a frequency polygon on top of an existing histogram, which points are marked first?",
     ["The midpoints of the upper horizontal edges of all rectangles",
      "The bottom left corners",
      "The center of the paper",
      "The highest Y-axis mark"],
     "A", "OSC", "easy",
     "The midpoints of the upper horizontal edges of each rectangle are marked as the vertices of the polygon."),

    # 34
    ("What coordinate point is plotted for the imaginary class preceding \\(30 - 40\\) (with class width 10)?",
     ["\\((25, 0)\\)", "\\((20, 0)\\)", "\\((30, 0)\\)", "\\((35, 0)\\)"],
     "A", "OSC", "easy",
     "Preceding class is \\(20 - 30\\), whose midpoint is 25, and its frequency is 0, so coordinate is \\((25, 0)\\)."),

    # 35
    ("What coordinate point is plotted for the imaginary class succeeding \\(70 - 80\\) (width 10)?",
     ["\\((85, 0)\\)", "\\((80, 0)\\)", "\\((90, 0)\\)", "\\((75, 0)\\)"],
     "A", "OSC", "easy",
     "Succeeding class is \\(80 - 90\\), midpoint is 85, coordinate is \\((85, 0)\\)."),

    # 36
    ("If the classes are \\(0-5, 5-10, 10-15\\), what is the class width?",
     ["\\(5\\)", "\\(10\\)", "\\(2.5\\)", "\\(15\\)"],
     "A", "OSC", "easy",
     "\\(5 - 0 = 5\\)."),

    # 37
    ("In a histogram, the width of the bars must be:",
     ["Equal to the class width of the intervals", "Arbitrary", "Always 1 cm", "Always 2 cm"],
     "A", "OSC", "easy",
     "The bar width directly represents the numerical class width according to the scale."),

    # 38
    ("In a standard bar graph (for categorical data), gaps exist between bars. In a histogram (for continuous data), do gaps exist between bars?",
     ["No gaps exist between adjacent bars in a histogram",
      "Gaps of 1 cm must be kept",
      "Gaps depend on the student",
      "Gaps are kept only for odd numbers"],
     "A", "OSC", "easy",
     "Histograms represent continuous data where the upper limit of one class is the lower limit of the next, so bars touch with zero gaps."),

    # 39
    ("Why is a histogram called a two-dimensional diagram?",
     ["Because both its length (width = class size) and breadth (height = frequency) are significant",
      "Because it is drawn on a flat sheet",
      "Because it uses two pencils",
      "Because it has two colors"],
     "A", "OSC", "easy",
     "In a histogram, both dimensions matter: base represents class width and height represents frequency, so area represents data frequency."),

    # 40
    ("What does the word 'polygon' mean in mathematics?",
     ["A closed plane figure bounded by straight line segments",
      "A circle",
      "A curved line",
      "An open graph"],
     "A", "OSC", "easy",
     "A polygon is any closed plane figure composed of straight line segments.")
]

t65_prac = [
    # 41
    ("Find the class mark of \\(30 - 50\\) to plot on a frequency polygon.",
     ["\\(40\\)", "\\(35\\)", "\\(45\\)", "\\(20\\)"],
     "A", "OSC", "easy",
     "\\((30 + 50)/2 = 40\\)."),

    # 42
    ("If a class is \\(40 - 60\\) with frequency \\(12\\), what point is plotted?",
     ["\\((50, 12)\\)", "\\((40, 12)\\)", "\\((60, 12)\\)", "\\((12, 50)\\)"],
     "A", "OSC", "easy",
     "Midpoint is 50, frequency is 12: \\((50, 12)\\)."),

    # 43
    ("If a class is \\(60 - 80\\) with frequency \\(18\\), what point is plotted?",
     ["\\((70, 18)\\)", "\\((60, 18)\\)", "\\((80, 18)\\)", "\\((18, 70)\\)"],
     "A", "OSC", "easy",
     "\\((70, 18)\\)."),

    # 44
    ("What is the class mark of the preceding class for \\(40 - 60\\) (width 20)?",
     ["\\(30\\) (midpoint of 20 - 40)", "\\(20\\)", "\\(10\\)", "\\(40\\)"],
     "A", "OSC", "easy",
     "Preceding class is \\(20 - 40\\), midpoint is 30."),

    # 45
    ("What is the class mark of the succeeding class for \\(60 - 80\\) (width 20)?",
     ["\\(90\\) (midpoint of 80 - 100)", "\\(80\\)", "\\(100\\)", "\\(85\\)"],
     "A", "OSC", "easy",
     "Succeeding class is \\(80 - 100\\), midpoint is 90."),

    # 46
    ("Does a histogram show individual data points?",
     ["No, individual values are grouped into intervals",
      "Yes, every single point is visible",
      "Only the minimum and maximum",
      "Only prime numbers"],
     "A", "OSC", "easy",
     "Individual data values are grouped within class boundaries."),

    # 47
    ("If the first class is \\(10 - 20\\), is a krink mark needed on the X-axis?",
     ["Yes, because numbers between 0 and 10 are skipped",
      "No, never needed",
      "Only for negative numbers",
      "Only if frequency is 0"],
     "A", "OSC", "easy",
     "Since the first interval starts at 10 instead of 0, a krink mark is required between 0 and 10."),

    # 48
    ("If the first class is \\(0 - 50\\), is a krink mark needed?",
     ["No, because the interval starts directly from origin (0)",
      "Yes, always needed",
      "Only if 50 is big",
      "Yes, for 50 units"],
     "A", "OSC", "easy",
     "No numbers are skipped when starting from 0, so no krink mark is needed."),

    # 49
    ("What are continuous classes for \\(10-19, 20-29, 30-39\\)?",
     ["\\(9.5 - 19.5, 19.5 - 29.5, 29.5 - 39.5\\)",
      "\\(10 - 20, 20 - 30, 30 - 40\\)",
      "\\(9 - 19, 19 - 29\\)",
      "\\(10.5 - 19.5\\)"],
     "A", "OSC", "easy",
     "Subtract 0.5 from lower limits and add 0.5 to upper limits."),

    # 50
    ("In Question 49, what is the class width \\(h\\)?",
     ["\\(10\\)", "\\(9\\)", "\\(9.5\\)", "\\(10.5\\)"],
     "A", "OSC", "easy",
     "\\(19.5 - 9.5 = 10\\)."),

    # 51
    ("What is the class mark of \\(9.5 - 19.5\\)?",
     ["\\(14.5\\)", "\\(14.0\\)", "\\(15.0\\)", "\\(10.0\\)"],
     "A", "OSC", "easy",
     "\\((9.5 + 19.5)/2 = 14.5\\)."),

    # 52
    ("What is the class mark of \\(19.5 - 29.5\\)?",
     ["\\(24.5\\)", "\\(24.0\\)", "\\(25.0\\)", "\\(20.0\\)"],
     "A", "OSC", "easy",
     "\\((19.5 + 29.5)/2 = 24.5\\)."),

    # 53
    ("In a histogram, can rectangles be of different widths?",
     ["Yes, when class intervals have unequal sizes, though standard syllabus uses uniform widths",
      "No, rectangles must always be identical in width by law",
      "Only in pie charts",
      "Only for line graphs"],
     "A", "OSC", "easy",
     "If class intervals have unequal widths, the rectangle bases will be unequal, with heights adjusted for frequency density."),

    # 54
    ("What is the total area under a histogram?",
     ["Sum of (class width × frequency) across all classes",
      "Total frequency N",
      "The mean of the data",
      "360 degrees"],
     "A", "OSC", "easy",
     "Total area is the sum of areas of all constituent rectangles: \\(\\sum (h_i \\times f_i)\\)."),

    # 55
    ("If all class widths are \\(h = 10\\) and \\(N = 50\\), what is the total area of the histogram?",
     ["\\(500\\) square units", "\\(50\\) square units", "\\(5\\) square units", "\\(1000\\) square units"],
     "A", "OSC", "easy",
     "Total area \\(= h \\times \\sum f_i = 10 \\times 50 = 500\\) square units."),

    # 56
    ("In Question 55, what is the area enclosed by the corresponding Frequency Polygon?",
     ["\\(500\\) square units", "\\(250\\) square units", "\\(1000\\) square units", "\\(50\\) square units"],
     "A", "OSC", "easy",
     "The area enclosed by the frequency polygon is identical to the total area of the histogram (500 square units)."),

    # 57
    ("Can a frequency polygon be drawn using a curved freehand line?",
     ["No, a frequency polygon MUST use straight line segments drawn with a ruler",
      "Yes, freehand curves are called polygons",
      "Only on computer screens",
      "Only for circles"],
     "A", "OSC", "easy",
     "A polygon by definition requires straight line segments; a freehand smooth curve is called a frequency curve."),

    # 58
    ("Which axis represents independent continuous class intervals in a histogram?",
     ["X-axis (abscissa)", "Y-axis (ordinate)", "Z-axis", "Diagonal axis"],
     "A", "OSC", "easy",
     "The horizontal X-axis represents class intervals."),

    # 59
    ("Which axis represents dependent frequency counts in a histogram?",
     ["Y-axis (ordinate)", "X-axis", "Radial axis", "Origin"],
     "A", "OSC", "easy",
     "The vertical Y-axis represents frequencies."),

    # 60
    ("What is the midpoint of \\(50 - 70\\)?",
     ["\\(60\\)", "\\(55\\)", "\\(65\\)", "\\(20\\)"],
     "A", "OSC", "easy",
     "\\((50 + 70)/2 = 60\\)."),

    # 61
    ("If frequency is 25 for class \\(50 - 70\\), the point plotted is:",
     ["\\((60, 25)\\)", "\\((50, 25)\\)", "\\((70, 25)\\)", "\\((25, 60)\\)"],
     "A", "OSC", "easy",
     "\\((60, 25)\\)."),

    # 62
    ("What is the imaginary class preceding \\(50 - 70\\)?",
     ["\\(30 - 50\\) with midpoint \\(40\\)", "\\(40 - 50\\)", "\\(0 - 50\\)", "\\(20 - 40\\)"],
     "A", "OSC", "easy",
     "Class width is 20, so preceding class is \\(30 - 50\\), midpoint 40."),

    # 63
    ("In Question 62, what is the point on the X-axis?",
     ["\\((40, 0)\\)", "\\((30, 0)\\)", "\\((50, 0)\\)", "\\((0, 40)\\)"],
     "A", "OSC", "easy",
     "\\((40, 0)\\)."),

    # 64
    ("What is the imaginary class succeeding \\(70 - 90\\)?",
     ["\\(90 - 110\\) with midpoint \\(100\\)", "\\(80 - 100\\)", "\\(100 - 120\\)", "\\(95\\)"],
     "A", "OSC", "easy",
     "Succeeding class is \\(90 - 110\\), midpoint 100."),

    # 65
    ("In Question 64, what is the point on the X-axis?",
     ["\\((100, 0)\\)", "\\((90, 0)\\)", "\\((110, 0)\\)", "\\((0, 100)\\)"],
     "A", "OSC", "easy",
     "\\((100, 0)\\)."),

    # 66
    ("What is the primary visual difference between a Bar Graph and a Histogram?",
     ["Bar graphs have spaces between bars; histograms have continuous touching bars without gaps",
      "Bar graphs are circular; histograms are square",
      "Histograms use no numbers",
      "Bar graphs are always 3D"],
     "A", "OSC", "easy",
     "Bar graphs display discrete categories with gaps; histograms display continuous grouped intervals with touching bars."),

    # 67
    ("Can a Histogram be used for ungrouped qualitative data like blood groups?",
     ["No, histograms are strictly for continuous grouped numerical data; qualitative data uses bar graphs or pie charts",
      "Yes, any data can be plotted as a histogram",
      "Only if converted to numbers",
      "Only for AB blood group"],
     "A", "OSC", "easy",
     "Histograms require continuous numerical class boundaries and cannot be used for qualitative categories."),

    # 68
    ("If a histogram has rectangles of heights 5, 10, 15, 8, 2, what is the total number of observations \\(N\\)?",
     ["\\(40\\)", "\\(35\\)", "\\(45\\)", "\\(50\\)"],
     "A", "OSC", "easy",
     "\\(5 + 10 + 15 + 8 + 2 = 40\\)."),

    # 69
    ("In Question 68, which class contains the Mode?",
     ["The 3rd class (height 15)", "The 1st class", "The 5th class", "The 2nd class"],
     "A", "OSC", "easy",
     "The highest rectangle has height 15 (modal class)."),

    # 70
    ("What does the krink mark look like?",
     ["A zigzag / broken wave line (~) on the axis", "A circle", "A triangle", "An arrow"],
     "A", "OSC", "easy",
     "The krink mark is drawn as a zigzag broken line.")
]

t65_mock = [
    # 71
    ("Why is a histogram useful in real life?",
     ["It gives an immediate visual display of data distribution, spread, peaks, and skewness",
      "It calculates exact square roots",
      "It replaces calculators completely",
      "It prints money"],
     "A", "OSC", "easy",
     "Histograms provide an intuitive visual representation of the shape and spread of continuous data."),

    # 72
    ("What is plotted on the X-axis of a histogram?",
     ["Class intervals (continuous limits)", "Frequencies", "Pie angles", "Names of students"],
     "A", "OSC", "easy",
     "Continuous class intervals are on the X-axis."),

    # 73
    ("What is plotted on the Y-axis of a histogram?",
     ["Frequency of each class", "Class mark", "Upper limit", "Median"],
     "A", "OSC", "easy",
     "Frequencies are on the Y-axis."),

    # 74
    ("Are there spaces between bars in a histogram?",
     ["No, adjacent bars touch each other without any gaps",
      "Yes, 1 cm space between every bar",
      "Yes, 2 cm space",
      "Only for negative numbers"],
     "A", "OSC", "easy",
     "Histograms have no gaps between bars because classes are continuous."),

    # 75
    ("What is a frequency polygon?",
     ["A line graph joining the midpoints of the tops of the histogram bars",
      "A circle with 8 sectors",
      "A 3D cube",
      "A single straight line"],
     "A", "OSC", "easy",
     "It is a line graph formed by connecting the midpoints of class intervals."),

    # 76
    ("What is a class mark?",
     ["The midpoint of a class interval: (Lower + Upper) / 2",
      "The frequency",
      "The class width",
      "The exam mark"],
     "A", "OSC", "easy",
     "Class mark is the midpoint of the class interval."),

    # 77
    ("What is the midpoint of \\(0 - 20\\)?",
     ["\\(10\\)", "\\(20\\)", "\\(0\\)", "\\(5\\)"],
     "A", "OSC", "easy",
     "\\(20 / 2 = 10\\)."),

    # 78
    ("What is the midpoint of \\(20 - 40\\)?",
     ["\\(30\\)", "\\(20\\)", "\\(40\\)", "\\(25\\)"],
     "A", "OSC", "easy",
     "\\((20 + 40)/2 = 30\\)."),

    # 79
    ("Why do we add imaginary classes with 0 frequency at the ends of a frequency polygon?",
     ["To close the polygon by touching the X-axis on both sides",
      "Because math requires 0",
      "To increase the total area",
      "To make the graph wider"],
     "A", "OSC", "easy",
     "Extending to 0 frequency at the ends brings the line down to the X-axis, completing a closed polygon."),

    # 80
    ("Can a frequency polygon be drawn directly without a histogram?",
     ["Yes, by plotting (class mark, frequency) points directly",
      "No, histogram is mandatory",
      "Only on Sundays",
      "Only for 100 students"],
     "A", "OSC", "easy",
     "Plotting coordinates of class mark vs frequency directly produces a frequency polygon without a histogram."),

    # 81
    ("What indicates the omission of numbers between 0 and the first class?",
     ["A krink mark (zigzag line)", "A dotted circle", "An exclamation mark", "A red arrow"],
     "A", "OSC", "easy",
     "The zigzag krink mark denotes scale compression."),

    # 82
    ("Is the area of a frequency polygon equal to the area of the histogram?",
     ["Yes, both areas are exactly equal",
      "No, polygon area is half",
      "No, polygon area is double",
      "Only for squares"],
     "A", "OSC", "easy",
     "The areas of the histogram and its corresponding frequency polygon are algebraically identical.")
]

if __name__ == "__main__":
    topic_code = "MH-10-MTH1-6-6.5"
    all_qs = build_topic_questions(topic_code, t65_exam, t65_prac, t65_mock)
    out_path = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch6_t5.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {topic_code} -> {out_path}")
