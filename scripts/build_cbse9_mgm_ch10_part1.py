# scripts/build_cbse9_mgm_ch10_part1.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 10: How Quantities Combine: Understanding Data
Part 1:
- Subtopic 10.1.1: Grouped frequency distribution tables
- Subtopic 10.1.2: Constructing bar graphs and uniform histograms
- Subtopic 10.1.3: Histograms with varying intervals: adjusted frequency
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 240 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 10
CH_NAME = "How Quantities Combine: Understanding Data"

# ==============================================================================
# SUBTOPIC 10.1.1: Grouped frequency distribution tables
# ==============================================================================
def gen_10_1_1():
    tc = "CBSE-9-MGM-10-10.1.1"
    tname = "Grouped frequency distribution tables"

    # Arch 0: Class limits, class size / width
    arch0 = {
        'data': [
            ("20-30", 20, 30, 10, "30 - 20 = 10"),
            ("10-25", 10, 25, 15, "25 - 10 = 15"),
            ("35-40", 35, 40, 5, "40 - 35 = 5"),
            ("100-150", 100, 150, 50, "150 - 100 = 50"),
            ("0-10", 0, 10, 10, "10 - 0 = 10"),
            ("45-65", 45, 65, 20, "65 - 45 = 20"),
            ("70-100", 70, 100, 30, "100 - 70 = 30"),
            ("15-20", 15, 20, 5, "20 - 15 = 5"),
            ("200-250", 200, 250, 50, "250 - 200 = 50"),
            ("80-95", 80, 95, 15, "95 - 80 = 15")
        ],
        'tmpls': [
            "For the class interval {0}, determine the class size (class width):",
            "In the grouped frequency distribution with class interval {0}, what is the lower limit and upper limit?",
            "Calculate the width of the class interval: {0}:",
            "What is the difference between the upper class limit and lower class limit for {0}?",
            "Find the class size for the interval: {0}:",
            "Determine the class width of: {0}:",
            "In the class interval {0}, the lower limit is {1}. What is the class width?",
            "Evaluate the class width of: {0}:",
            "What is the size of the interval: {0}?",
            "For the interval {0}, state the class width:"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            [f"{item[3] + 5}", f"{item[3] - 2 if item[3] > 2 else item[3] + 8}", f"{item[1]}"],
            f"**Step 1: Identify the lower limit and upper limit of the class interval.**\nFor the interval \\( {item[0]} \\), lower limit \\( L = {item[1]} \\) and upper limit \\( U = {item[2]} \\).\n\n**Step 2: Calculate the class size (class width).**\n\\[ \\text{{Class Width}} = U - L = {item[4]} = {item[3]} \\]\n\n**Step 3: State the answer.**\nThe class size is {item[3]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Range of raw data (Maximum - Minimum)
    arch1 = {
        'data': [
            ("25, 18, 32, 45, 12, 50, 29", 50, 12, 38, "50 - 12 = 38"),
            ("10, 85, 42, 67, 95, 23, 71", 95, 10, 85, "95 - 10 = 85"),
            ("5, 15, 9, 3, 21, 14, 18", 21, 3, 18, "21 - 3 = 18"),
            ("104, 112, 98, 145, 120, 131", 145, 98, 47, "145 - 98 = 47"),
            ("40, 52, 65, 38, 70, 44, 59", 70, 38, 32, "70 - 38 = 32"),
            ("2, 8, 14, 20, 35, 11, 4", 35, 2, 33, "35 - 2 = 33"),
            ("88, 92, 79, 65, 99, 84, 73", 99, 65, 34, "99 - 65 = 34"),
            ("15, 28, 35, 42, 19, 56, 31", 56, 15, 41, "56 - 15 = 41"),
            ("60, 45, 90, 30, 75, 80, 55", 90, 30, 60, "90 - 30 = 60"),
            ("12, 24, 36, 48, 60, 18, 9", 60, 9, 51, "60 - 9 = 51")
        ],
        'tmpls': [
            "Find the range of the raw data set: {0}:",
            "What is the range of the following numerical observations: {0}?",
            "Calculate the statistical range for the data: {0}:",
            "Determine the difference between the maximum and minimum observations in: {0}:",
            "Evaluate the range of the given data points: {0}:",
            "What is the range of the data set: {0}?",
            "Compute the range of the numbers: {0}:",
            "From the given observations {0}, find the range:",
            "Find the range for the distribution: {0}:",
            "Determine the range of the sample: {0}:"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            [f"{item[3] + 6}", f"{item[3] - 4}", f"{item[1]}"],
            f"**Step 1: Identify the maximum and minimum values in the data set.**\nMaximum value = \\( {item[1]} \\), Minimum value = \\( {item[2]} \\).\n\n**Step 2: Compute the range.**\n\\[ \\text{{Range}} = \\text{{Maximum}} - \\text{{Minimum}} = {item[4]} = {item[3]} \\]\n\n**Step 3: State the answer.**\nThe range is {item[3]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Continuous vs Discontinuous Class Intervals (Adjustment Factor 0.5)
    arch2 = {
        'data': [
            ("1-10, 11-20, 21-30", "0.5-10.5, 10.5-20.5, 20.5-30.5", "0.5", "Subtract 0.5 from lower limit, add 0.5 to upper limit"),
            ("10-19, 20-29, 30-39", "9.5-19.5, 19.5-29.5, 29.5-39.5", "0.5", "Lower limit - 0.5, Upper limit + 0.5"),
            ("31-35, 36-40, 41-45", "30.5-35.5, 35.5-40.5, 40.5-45.5", "0.5", "Gap = 1, Adjustment = 1/2 = 0.5"),
            ("100-109, 110-119, 120-129", "99.5-109.5, 109.5-119.5, 119.5-129.5", "0.5", "Adjustment factor = 0.5"),
            ("6-10, 11-15, 16-20", "5.5-10.5, 10.5-15.5, 15.5-20.5", "0.5", "Adjustment factor = 0.5"),
            ("21-25, 26-30, 31-35", "20.5-25.5, 25.5-30.5, 30.5-35.5", "0.5", "Adjustment factor = 0.5"),
            ("41-50, 51-60, 61-70", "40.5-50.5, 50.5-60.5, 60.5-70.5", "0.5", "Adjustment factor = 0.5"),
            ("81-90, 91-100, 101-110", "80.5-90.5, 90.5-100.5, 100.5-110.5", "0.5", "Adjustment factor = 0.5"),
            ("16-20, 21-25, 26-30", "15.5-20.5, 20.5-25.5, 25.5-30.5", "0.5", "Adjustment factor = 0.5"),
            ("1-5, 6-10, 11-15", "0.5-5.5, 5.5-10.5, 10.5-15.5", "0.5", "Adjustment factor = 0.5")
        ],
        'tmpls': [
            "Convert the discontinuous (inclusive) class intervals {0} into continuous (exclusive) intervals:",
            "What are the continuous class boundaries for the inclusive classes: {0}?",
            "In converting {0} to continuous form, what is the adjustment factor subtracted from lower limits and added to upper limits?",
            "Convert the grouped distribution {0} to true class limits:",
            "How are the discontinuous classes {0} made continuous for histogram construction?",
            "Find the true continuous class boundaries for: {0}:",
            "Make the intervals continuous for: {0}:",
            "What continuous intervals correspond to the inclusive classes: {0}?",
            "To construct a histogram for {0}, what continuous intervals must be used?",
            "Transform into continuous intervals: {0}:"
        ],
        'calc': lambda item: (
            item[1] if not item[0].startswith("In converting") else item[2],
            [
                "0-10, 10-20, 20-30" if not item[0].startswith("In converting") else "1.0",
                "1.5-10.5, 11.5-20.5" if not item[0].startswith("In converting") else "0.25",
                "2-11, 12-21, 22-31" if not item[0].startswith("In converting") else "2.0"
            ],
            f"**Step 1: Determine the gap between consecutive class intervals.**\nGap = Lower limit of second class - Upper limit of first class = 1.\nAdjustment factor = \\( \\frac{{1}}{{2}} = 0.5 \\).\n\n**Step 2: Adjust limits.**\n{item[3]}.\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Boundary inclusion convention in continuous intervals [a, b)
    arch3 = {
        'data': [
            ("20", "10-20 and 20-30", "20-30", "In continuous classes [a, b), the upper limit is excluded and belongs to the next class [b, c)"),
            ("30", "20-30 and 30-40", "30-40", "30 is included in 30-40, not 20-30"),
            ("15", "10-15 and 15-20", "15-20", "15 is included in 15-20, not 10-15"),
            ("50", "40-50 and 50-60", "50-60", "50 is included in 50-60, not 40-50"),
            ("25", "20-25 and 25-30", "25-30", "25 is included in 25-30, not 20-25"),
            ("10", "0-10 and 10-20", "10-20", "10 is included in 10-20, not 0-10"),
            ("40", "30-40 and 40-50", "40-50", "40 is included in 40-50, not 30-40"),
            ("100", "50-100 and 100-150", "100-150", "100 is included in 100-150, not 50-100"),
            ("35", "30-35 and 35-40", "35-40", "35 is included in 35-40, not 30-35"),
            ("60", "50-60 and 60-70", "60-70", "60 is included in 60-70, not 50-60")
        ],
        'tmpls': [
            "In continuous class intervals {1}, in which class interval is the observation {0} included?",
            "According to standard convention in grouped frequency distributions, in which class does the value {0} fall: {1}?",
            "Where is the observation {0} recorded among the intervals: {1}?",
            "An observation of {0} occurs. In which interval is it counted: {1}?",
            "Determine the correct class interval for the boundary value {0} among: {1}:",
            "In an exclusive frequency table with intervals {1}, the value {0} is included in:",
            "Which class interval contains the observation {0}: {1}?",
            "Identify the correct interval containing {0} between: {1}:",
            "For the observation {0}, select the correct class interval from {1}:",
            "In which group is {0} placed: {1}?"
        ],
        'calc': lambda item: (
            item[2],
            [
                item[1].split(' and ')[0],
                "Both intervals simultaneously",
                "Neither interval (it is discarded)"
            ],
            f"**Step 1: Recall the standard convention for continuous class intervals.**\nIn the continuous (exclusive) method, an interval \\( [a, b) \\) includes values \\( x \\) such that \\( a \\le x < b \\).\n\n**Step 2: Determine where the boundary value falls.**\n{item[3]}.\n\n**Step 3: State the answer.**\nThe observation {item[0]} is included in {item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Cumulative frequency and total frequency sum (N = sum f_i)
    arch4 = {
        'data': [
            ("[5, 8, 12, 10, 5]", 40, "5 + 8 + 12 + 10 + 5 = 40"),
            ("[3, 7, 15, 20, 5]", 50, "3 + 7 + 15 + 20 + 5 = 50"),
            ("[4, 6, 8, 7, 5]", 30, "4 + 6 + 8 + 7 + 5 = 30"),
            ("[10, 15, 25, 30, 20]", 100, "10 + 15 + 25 + 30 + 20 = 100"),
            ("[2, 4, 6, 8, 5]", 25, "2 + 4 + 6 + 8 + 5 = 25"),
            ("[8, 12, 16, 14, 10]", 60, "8 + 12 + 16 + 14 + 10 = 60"),
            ("[1, 3, 5, 7, 4]", 20, "1 + 3 + 5 + 7 + 4 = 20"),
            ("[6, 9, 14, 11, 10]", 50, "6 + 9 + 14 + 11 + 10 = 50"),
            ("[12, 18, 22, 16, 12]", 80, "12 + 18 + 22 + 16 + 12 = 80"),
            ("[5, 10, 15, 12, 8]", 50, "5 + 10 + 15 + 12 + 8 = 50")
        ],
        'tmpls': [
            "In a grouped frequency distribution with class frequencies {0}, find the total number of observations \\( N = \\sum f_i \\):",
            "What is the total sample size \\( N \\) for a distribution with frequencies {0}?",
            "Calculate \\( \\sum f_i \\) for the frequencies: {0}:",
            "Determine the total frequency of the distribution with frequencies: {0}:",
            "Compute the total number of students surveyed if class frequencies are {0}:",
            "Find \\( N \\) given the frequency list: {0}:",
            "Evaluate the sum of frequencies: {0}:",
            "What is the total count of observations for: {0}?",
            "Compute \\( N = \\sum f \\) for: {0}:",
            "Calculate the total frequency \\( N \\) for the grouped data: {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1] + 5}", f"{item[1] - 5}", f"{item[1] + 10}"],
            f"**Step 1: Sum the frequencies of all class intervals.**\n\\[ N = \\sum f_i = {item[2]} \\]\n\n**Step 2: Conclude the total frequency.**\nThe total number of observations is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Class mark calculation ((Upper limit + Lower limit)/2)
    arch5 = {
        'data': [
            ("10-20", 10, 20, 15, "(10 + 20) / 2 = 15"),
            ("20-30", 20, 30, 25, "(20 + 30) / 2 = 25"),
            ("30-40", 30, 40, 35, "(30 + 40) / 2 = 35"),
            ("40-50", 40, 50, 45, "(40 + 50) / 2 = 45"),
            ("0-10", 0, 10, 5, "(0 + 10) / 2 = 5"),
            ("50-70", 50, 70, 60, "(50 + 70) / 2 = 60"),
            ("15-25", 15, 25, 20, "(15 + 25) / 2 = 20"),
            ("70-90", 70, 90, 80, "(70 + 90) / 2 = 80"),
            ("100-120", 100, 120, 110, "(100 + 120) / 2 = 110"),
            ("25-35", 25, 35, 30, "(25 + 35) / 2 = 30")
        ],
        'tmpls': [
            "Find the class mark of the class interval {0}:",
            "What is the mid-point (class mark) of the interval {0}?",
            "Calculate the class mark \\( x_i \\) for the class: {0}:",
            "Determine the midpoint value representing the class interval {0}:",
            "Compute the class mark for: {0}:",
            "What is the mid-value of the class: {0}?",
            "Evaluate the class mark of: {0}:",
            "Find \\( x_i = \\frac{{\\text{{Upper}} + \\text{{Lower}}}}{{2}} \\) for {0}:",
            "Calculate the midpoint of the interval: {0}:",
            "For the interval {0}, determine its class mark:"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            [f"{item[3] + 5}", f"{item[3] - 5}", f"{item[1]}"],
            f"**Step 1: Write down the class mark formula.**\n\\[ \\text{{Class Mark}} = \\frac{{\\text{{Upper Limit}} + \\text{{Lower Limit}}}}{{2}} \\]\n\n**Step 2: Substitute the limits of the class interval {item[0]}.**\n\\[ \\text{{Class Mark}} = {item[4]} = {item[3]} \\]\n\n**Step 3: State the answer.**\nThe class mark is {item[3]}."
        ),
        'diff': 'easy'
    }

    # Arch 6: Relative frequency and percentage frequency
    arch6 = {
        'data': [
            (8, 40, "8 / 40 = 0.20", "20%"),
            (12, 50, "12 / 50 = 0.24", "24%"),
            (15, 60, "15 / 60 = 0.25", "25%"),
            (25, 100, "25 / 100 = 0.25", "25%"),
            (7, 35, "7 / 35 = 0.20", "20%"),
            (18, 90, "18 / 90 = 0.20", "20%"),
            (9, 30, "9 / 30 = 0.30", "30%"),
            (10, 25, "10 / 25 = 0.40", "40%"),
            (16, 80, "16 / 80 = 0.20", "20%"),
            (14, 70, "14 / 70 = 0.20", "20%")
        ],
        'tmpls': [
            "A class interval has a frequency of {0} out of a total of {1} observations. Find its percentage frequency:",
            "What percentage of the total data ({1} observations) falls in a class with frequency {0}?",
            "Calculate the relative percentage frequency for frequency = {0} and total \\( N = {1} \\):",
            "Determine the percentage frequency corresponding to \\( f = {0} \\) and \\( N = {1} \\):",
            "Find the percentage of total observations for class frequency {0} with total sample size {1}:",
            "What is the percentage frequency when \\( f_i = {0} \\) and \\( \\sum f_i = {1} \\)?",
            "Compute the relative percentage for {0} out of {1}:",
            "Evaluate the percentage representation: {0} / {1}:",
            "For a group having {0} items out of {1}, find the percentage frequency:",
            "Determine the percentage of data in a category with frequency {0} and total {1}:"
        ],
        'calc': lambda item: (
            item[3],
            [
                f"{int(item[3].replace('%', '')) + 10}%",
                f"{int(item[3].replace('%', '')) - 5}%",
                "50%"
            ],
            f"**Step 1: Write down the percentage frequency formula.**\n\\[ \\text{{Percentage Frequency}} = \\frac{{\\text{{Frequency}}}}{{N}} \\times 100\\% \\]\n\n**Step 2: Substitute \\( f = {item[0]} \\) and \\( N = {item[1]} \\).**\n\\[ \\frac{{{item[0]}}}{{{item[1]}}} \\times 100\\% = {item[2]} \\times 100\\% = {item[3]} \\]\n\n**Step 3: State the answer.**\nThe percentage frequency is {item[3]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Interpreting frequency distribution tables for problem solving
    arch7 = {
        'data': [
            ("Marks: 0-10 (4), 10-20 (8), 20-30 (15), 30-40 (10), 40-50 (3). Passing mark is 20.", "How many students passed the exam?", 28, "15 + 10 + 3 = 28 passed"),
            ("Marks: 0-10 (4), 10-20 (8), 20-30 (15), 30-40 (10), 40-50 (3). Passing mark is 20.", "How many students failed the exam (scored < 20)?", 12, "4 + 8 = 12 failed"),
            ("Marks: 0-10 (5), 10-20 (12), 20-30 (18), 30-40 (11), 40-50 (4). Distinction is >= 40.", "How many students scored distinction?", 4, "4 students scored >= 40"),
            ("Ages: 10-20 (6), 20-30 (14), 30-40 (20), 40-50 (10).", "How many individuals are at least 20 years old?", 44, "14 + 20 + 10 = 44"),
            ("Ages: 10-20 (6), 20-30 (14), 30-40 (20), 40-50 (10).", "How many individuals are under 30 years old?", 20, "6 + 14 = 20"),
            ("Heights (cm): 140-145 (4), 145-150 (11), 150-155 (15), 155-160 (8), 160-165 (2).", "How many students have height < 155 cm?", 30, "4 + 11 + 15 = 30"),
            ("Heights (cm): 140-145 (4), 145-150 (11), 150-155 (15), 155-160 (8), 160-165 (2).", "How many students have height >= 155 cm?", 10, "8 + 2 = 10"),
            ("Daily Wages (₹): 100-150 (5), 150-200 (10), 200-250 (15), 250-300 (12), 300-350 (8).", "How many workers earn less than ₹250 daily?", 30, "5 + 10 + 15 = 30"),
            ("Daily Wages (₹): 100-150 (5), 150-200 (10), 200-250 (15), 250-300 (12), 300-350 (8).", "How many workers earn at least ₹250 daily?", 20, "12 + 8 = 20"),
            ("Weights (kg): 40-45 (6), 45-50 (12), 50-55 (16), 55-60 (10), 60-65 (6).", "How many people weigh between 45 kg and 60 kg?", 38, "12 + 16 + 10 = 38")
        ],
        'tmpls': [
            "Given the frequency distribution table: {0}. {1}",
            "From the grouped distribution data: {0}. {1}",
            "Refer to the table: {0}. Answer: {1}",
            "Using the frequency distribution: {0}, solve: {1}",
            "Analyze the grouped table: {0}. {1}",
            "Based on the frequency distribution: {0}, find: {1}",
            "In the grouped data table: {0}, calculate: {1}",
            "Consider the distribution: {0}. Determine: {1}",
            "From the survey results: {0}, {1}",
            "Solve using the frequency table: {0}: {1}"
        ],
        'calc': lambda item: (
            f"{item[2]}",
            [f"{item[2] + 4}", f"{item[2] - 4}", f"{item[2] + 10}"],
            f"**Step 1: Identify the relevant class intervals.**\nLocate all intervals that satisfy the condition stated in the question.\n\n**Step 2: Add their corresponding frequencies.**\n\\[ {item[3]} \\]\n\n**Step 3: State the answer.**\nThe answer is {item[2]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 10.1.2: Constructing bar graphs and uniform histograms
# ==============================================================================
def gen_10_1_2():
    tc = "CBSE-9-MGM-10-10.1.2"
    tname = "Constructing bar graphs and uniform histograms"

    # Arch 0: Fundamental Differences between Bar Graph and Histogram
    arch0 = {
        'data': [
            ("Which graphical representation displays categorical/discrete data with equal spaces between bars?", "Bar Graph (Bar Chart)", "Bars have equal spacing and represent discrete categories"),
            ("Which graphical representation displays continuous grouped numerical data using adjacent rectangles with NO spaces between them?", "Histogram", "Adjacent contiguous rectangles representing continuous class intervals"),
            ("In a uniform histogram (where all class widths are equal), what does the height of each rectangle represent?", "The frequency of the class interval", "Height = frequency when class widths are equal"),
            ("In any histogram, what does the AREA of each rectangle represent?", "The frequency of that class interval", "Area is proportional to frequency"),
            ("Can spaces/gaps be left between rectangles in a standard histogram representing continuous data?", "No, rectangles must be contiguous (adjacent with no gaps) because intervals are continuous", "Contiguous intervals"),
            ("On which axis are the class intervals typically marked in a histogram?", "Horizontal axis (X-axis)", "Class boundaries on X-axis"),
            ("On which axis are the frequencies marked in a uniform histogram?", "Vertical axis (Y-axis)", "Frequencies on Y-axis"),
            ("Why is a bar graph inappropriate for continuous data like height or weight?", "Because continuous data has no gaps between intervals and requires adjacent area representation", "Continuous vs discrete"),
            ("What does the width of each rectangle in a histogram represent?", "The class size (class width)", "Class interval on X-axis"),
            ("In a bar graph, does the width of the bars have any mathematical significance?", "No, bar width is arbitrary and has no mathematical meaning (only height matters)", "Bar graph convention")
        ],
        'tmpls': [
            "{0}",
            "In data visualization and statistics: {0}",
            "Distinguish between bar graphs and histograms: {0}",
            "Identify the correct graphical property: {0}",
            "Which statement accurately describes: {0}?",
            "What is the key rule regarding: {0}?",
            "Analyze the graphical representation: {0}",
            "Determine the correct answer for: {0}",
            "Select the accurate distinction: {0}",
            "Regarding histograms and bar charts: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Line graph",
                "Pie chart",
                "Frequency polygon without intervals"
            ],
            f"**Step 1: Understand the nature of graphical representations.**\nBar graphs depict categorical data with spaces; histograms represent continuous intervals with contiguous rectangles whose area reflects frequency.\n\n**Step 2: Detail the property.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: The 'Kink' (Zigzag / Broken Axis) on the horizontal axis
    arch1 = {
        'data': [
            ("When the class intervals of a histogram begin at 100 instead of 0, what symbol is drawn near the origin on the X-axis?", "A 'kink' (or zigzag / broken line)", "Indicates suppressed scale from 0 to 100"),
            ("Why is a kink (broken axis) used on the horizontal axis of a histogram?", "To indicate that the scale is broken between 0 and the first class boundary (values near 0 are omitted)", "Prevents misleading empty space"),
            ("If class intervals are 0-10, 10-20, 20-30, is a kink required on the X-axis?", "No, because the intervals start directly from the origin (0)", "No suppression needed when starting at 0"),
            ("If class intervals are 40-50, 50-60, 60-70, is a kink required on the X-axis?", "Yes, because the interval 0 to 40 is omitted on the scale", "Suppression of 0 to 40"),
            ("What would happen if a kink were NOT drawn when starting at 500 without a broken scale?", "The distance from 0 to 500 would misleadingly appear equal to the distance from 500 to 510", "Scale distortion"),
            ("Can a kink also be used on the Y-axis if frequencies start at a very high number?", "Yes, a kink can be used on either axis where values between 0 and the first plotted number are omitted", "General axis suppression rule"),
            ("In NCERT Class 9, the kink symbol is visually represented as:", "A jagged zigzag line near the origin on the axis", "Visual notation for broken scale"),
            ("Which of the following datasets REQUIRES a kink on the X-axis?", "Heights of adults: 150-155, 155-160, 160-165, 165-170", "Starts at 150, far from 0"),
            ("Which of the following datasets does NOT require a kink on the X-axis?", "Number of books read: 0-5, 5-10, 10-15, 15-20", "Starts directly at 0"),
            ("The kink preserves which fundamental principle of graphical integrity?", "Proportionality and accuracy of scale across the plotted region", "Preserving scale fidelity")
        ],
        'tmpls': [
            "{0}",
            "Regarding the kink (broken axis) in histograms: {0}",
            "In constructing a histogram: {0}",
            "Why and when is a kink used: {0}?",
            "Identify the correct rule for broken scales: {0}",
            "Analyze the use of the zigzag symbol: {0}",
            "Determine the accurate statement: {0}",
            "Which dataset requires a kink: {0}?",
            "Select the accurate graphical principle: {0}",
            "In Class 9 histogram construction: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "A circular mark indicating the median",
                "A dashed arrow pointing to infinity",
                "No symbol is ever permitted on an axis"
            ],
            f"**Step 1: Understand the purpose of a kink (broken axis).**\nA kink is used when the scale on an axis does not start from 0, showing that the range from 0 to the first marked number is compressed.\n\n**Step 2: Detail the convention.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Reading frequencies from a uniform histogram
    arch2 = {
        'data': [
            ("A histogram has uniform class width 10. The rectangle on interval 20-30 has height 14 units. What is the frequency of class 20-30?", 14, "Height equals frequency for uniform width"),
            ("A uniform histogram shows class 30-40 with rectangle height 22. What is the number of observations in this class?", 22, "Frequency is directly read from height"),
            ("In a uniform histogram of test scores, the bar on 50-60 reaches height 18. How many students scored between 50 and 60?", 18, "Frequency = 18"),
            ("The heights of rectangles in a uniform histogram are: 10-20 (5), 20-30 (12), 30-40 (20), 40-50 (15), 50-60 (8). What is the modal class (class with highest frequency)?", "30-40 (frequency = 20)", "Highest rectangle corresponds to modal class"),
            ("From the heights: 10-20 (5), 20-30 (12), 30-40 (20), 40-50 (15), 50-60 (8), what is the total number of observations?", 60, "5 + 12 + 20 + 15 + 8 = 60"),
            ("In the same histogram, how many observations are >= 30?", 43, "20 + 15 + 8 = 43"),
            ("In the same histogram, how many observations are < 30?", 17, "5 + 12 = 17"),
            ("In a uniform histogram, the lowest rectangle is on 10-20 with height 5. What is the frequency of the least common class?", 5, "Lowest height = minimum frequency"),
            ("What is the ratio of frequencies of class 30-40 to class 20-30 if their heights are 20 and 10?", "2 : 1", "20 / 10 = 2/1"),
            ("If 1 cm on the Y-axis represents 5 units of frequency, what is the frequency of a bar of height 6 cm?", 30, "6 * 5 = 30")
        ],
        'tmpls': [
            "{0}",
            "From the uniform histogram description: {0}",
            "Solve the histogram reading problem: {0}",
            "Calculate the frequency from the histogram: {0}",
            "Determine the correct count: {0}",
            "Evaluate the histogram observation: {0}",
            "Find the required quantity from the histogram: {0}",
            "Using the uniform histogram data: {0}",
            "What is the result for: {0}?",
            "Analyze the histogram: {0}"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1]} + 5" if isinstance(item[1], int) else "3 : 1", f"{item[1]} - 3" if isinstance(item[1], int) else "1 : 2", "50" if isinstance(item[1], int) else "4 : 1"],
            f"**Step 1: Read the height corresponding to the given class.**\nIn a uniform histogram where all widths are identical, the height of each rectangle directly equals its frequency.\n\n**Step 2: Calculate the requested value.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Scale selection on axes (X-axis and Y-axis)
    arch3 = {
        'data': [
            ("If frequencies range from 2 to 48, which scale on the vertical axis (Y-axis) is most appropriate for a standard 10 cm graph page?", "1 cm = 5 units (covering 0 to 50 in 10 cm)", "Standard optimal scale selection"),
            ("If class intervals are 0-10, 10-20, 20-30, 30-40, 40-50, which horizontal scale is suitable for a 10 cm axis?", "1 cm = 5 units (each class width of 10 takes 2 cm)", "Clear representation with 2 cm per bar"),
            ("Why must the scale on an axis be strictly uniform (equal distances represent equal increments)?", "To prevent visual distortion of data and ensure honest graphic communication", "Graphic integrity rule"),
            ("If a student chooses 1 cm = 2 units on Y-axis for a maximum frequency of 80, what problem arises?", "The graph will require 40 cm, exceeding standard graph paper size", "Scale too small (oversized graph)"),
            ("If a student chooses 1 cm = 50 units for a maximum frequency of 15, what problem arises?", "All bars will be less than 0.3 cm high, making the graph unreadable", "Scale too large (compressed graph)"),
            ("Should the chosen scale on both axes always be explicitly written in the top-right corner of a graph sheet?", "Yes, writing 'Scale: X-axis: 1 cm = ..., Y-axis: 1 cm = ...' is mandatory for full marks", "Examination convention"),
            ("If 1 unit on Y-axis = 4 students, what height represents a frequency of 28 students?", "7 units (28 / 4 = 7)", "28 / 4 = 7 units"),
            ("If 1 unit on Y-axis = 10 units, how many units of height represent 65?", "6.5 units (65 / 10 = 6.5)", "65 / 10 = 6.5 units"),
            ("Can different scales be used on the X-axis and Y-axis?", "Yes, the scales on the X-axis and Y-axis are completely independent and chosen based on their respective data ranges", "Axes independence"),
            ("What should the vertical axis always begin with unless a kink is drawn?", "Zero (0)", "Zero baseline rule")
        ],
        'tmpls': [
            "{0}",
            "Regarding scale selection in graphical data representation: {0}",
            "In graph construction for Class 9: {0}",
            "How should the scale be chosen: {0}?",
            "Identify the correct scaling principle: {0}",
            "Analyze the axis scale question: {0}",
            "Determine the accurate scaling rule: {0}",
            "Which option correctly answers: {0}?",
            "In drawing histograms and bar graphs: {0}",
            "Select the accurate scale guidance: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "1 cm = 100 units",
                "Axes must always use the exact same scale regardless of data",
                "Scale choice does not matter in mathematics"
            ],
            f"**Step 1: Determine the range of values to be plotted on the axis.**\nDivide the data range by available graph space (typically 10-15 cm).\n\n**Step 2: Choose a clean, convenient unit increment (1, 2, 5, 10, etc.).**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Constructing Bar Graphs for Categorical Data
    arch4 = {
        'data': [
            ("A survey shows preferred sports: Cricket (35), Football (25), Badminton (20), Tennis (10), Hockey (10). What is the total number of students?", 100, "35 + 25 + 20 + 10 + 10 = 100"),
            ("In the sports bar graph, what is the ratio of students who prefer Cricket to Tennis?", "35 : 10 = 7 : 2", "35 / 10 = 7/2"),
            ("What percentage of students prefer Football in the sports survey (total = 100)?", "25%", "25 / 100 = 25%"),
            ("Which sport is represented by the tallest bar in the bar graph?", "Cricket (height = 35)", "Maximum frequency"),
            ("Which two sports have bars of equal height?", "Tennis and Hockey (both height = 10)", "Equal frequencies"),
            ("Monthly family expenditure: Grocery (₹4000), Rent (₹5000), Education (₹3000), Medicine (₹2000), Savings (₹6000). What is the total income?", "₹20,000", "4000 + 5000 + 3000 + 2000 + 6000 = 20000"),
            ("In the expenditure bar graph, which category has the highest expenditure bar?", "Savings (₹6,000)", "Tallest bar"),
            ("What fraction of total income is spent on Rent (₹5,000 out of ₹20,000)?", "1/4 (or 25%)", "5000 / 20000 = 1/4"),
            ("In drawing a bar graph, why must all bars have the same width?", "Because bar width has no mathematical meaning, so differing widths would introduce unintended visual bias", "Prevent visual distortion"),
            ("Why must the spaces between bars in a bar graph be equal?", "To maintain visual consistency and indicate that categories are discrete and separate", "Discrete category spacing")
        ],
        'tmpls': [
            "{0}",
            "From the bar graph description: {0}",
            "Solve using the bar graph data: {0}",
            "Calculate from the bar graph: {0}",
            "Determine the correct answer from the bar graph: {0}",
            "Analyze the categorical bar chart: {0}",
            "Evaluate the bar graph scenario: {0}",
            "What is the result for: {0}?",
            "Find the required quantity from the bar chart: {0}",
            "Using the survey bar graph data: {0}"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1]} + 10" if isinstance(item[1], int) else "3 : 1", f"{item[1]} - 5" if isinstance(item[1], int) else "1 : 1", "50" if isinstance(item[1], int) else "₹15,000"],
            f"**Step 1: Read the heights/values of the categories in the bar graph.**\nEach bar height represents the value of that specific discrete category.\n\n**Step 2: Perform the required calculation.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Percentage distribution and comparison from histograms
    arch5 = {
        'data': [
            ("In a uniform histogram with 50 total students, class 60-70 has frequency 15. What percentage of students scored in this range?", "30%", "(15 / 50) * 100% = 30%"),
            ("In a histogram with 80 workers, class 200-250 has frequency 20. What percentage of workers earn in this range?", "25%", "(20 / 80) * 100% = 25%"),
            ("In a histogram with 40 plants, class 10-15 cm has frequency 16. What percentage of plants have this height?", "40%", "(16 / 40) * 100% = 40%"),
            ("In a histogram of 100 batteries, class 3.0-3.5 years life has frequency 35. What percentage of batteries last 3.0-3.5 years?", "35%", "(35 / 100) * 100% = 35%"),
            ("A histogram represents 60 students. Class 0-10 has 6 students, 10-20 has 12, 20-30 has 24, 30-40 has 18. What percentage scored >= 20?", "70%", "(24 + 18) / 60 = 42/60 = 70%"),
            ("In the same histogram, what percentage scored < 20?", "30%", "(6 + 12) / 60 = 18/60 = 30%"),
            ("In a histogram of 200 cars, class 40-60 km/h has frequency 80. What percentage of cars travel at this speed?", "40%", "(80 / 200) * 100% = 40%"),
            ("In a histogram of 50 lamps, class 800-900 hours has frequency 11. What percentage of lamps last 800-900 hours?", "22%", "(11 / 50) * 100% = 22%"),
            ("If two adjacent classes in a uniform histogram have heights 12 and 18, what is their combined frequency?", 30, "12 + 18 = 30"),
            ("What percentage of total area in a uniform histogram does a rectangle of height 25 out of total height 100 occupy?", "25%", "25 / 100 = 25%")
        ],
        'tmpls': [
            "{0}",
            "Calculate the percentage from the histogram: {0}",
            "Determine the percentage of observations: {0}",
            "What percentage is represented in the histogram: {0}?",
            "Evaluate the percentage proportion: {0}",
            "From the given histogram data: {0}",
            "Find the percentage share from the histogram: {0}",
            "Compute the percentage representation: {0}",
            "Solve the histogram percentage problem: {0}",
            "Analyze the proportion: {0}"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{int(str(item[1]).replace('%','')) + 10}%" if '%' in str(item[1]) else f"{item[1] + 5}", f"{int(str(item[1]).replace('%','')) - 5}%" if '%' in str(item[1]) else f"{item[1] - 5}", "50%"],
            f"**Step 1: Find the frequency of the specified class and total frequency \\( N \\).**\n\n**Step 2: Compute the percentage.**\n\\[ \\text{{Percentage}} = \\frac{{\\text{{Frequency}}}}{{N}} \\times 100\\% \\]\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Modal Class and Distribution Skewness from Histogram
    arch6 = {
        'data': [
            ("In a histogram, the class interval corresponding to the rectangle with the greatest height is called the:", "Modal Class", "Class containing the highest frequency / mode"),
            ("If a histogram has its tallest bar at 30-40 with height 28, what is the modal class?", "30-40", "Class with maximum frequency"),
            ("If a histogram shows bars rising gradually to a peak in the center and declining symmetrically on both sides, the distribution is:", "Symmetric (Bell-shaped)", "Symmetric unimodal distribution"),
            ("If a histogram has a long tail stretching to the right (higher values), the distribution is:", "Positively skewed (skewed to the right)", "Right-skewed distribution"),
            ("If a histogram has a long tail stretching to the left (lower values), the distribution is:", "Negatively skewed (skewed to the left)", "Left-skewed distribution"),
            ("If a histogram has two distinct peaks of approximately equal height, the distribution is described as:", "Bimodal", "Two distinct modes"),
            ("Can the exact mode of a grouped distribution be determined solely by looking at the histogram without using the modal formula?", "No, the histogram identifies the modal class, but the exact mode requires the interpolation formula", "Modal class vs exact mode"),
            ("In a uniform histogram, is the modal class always the one with the largest area?", "Yes, because all widths are equal, so greatest height implies greatest area", "Height directly reflects area"),
            ("What does a flat, rectangular histogram where all bars have roughly the same height indicate?", "A uniform distribution", "Equal frequencies across all classes"),
            ("Which measure of central tendency corresponds visually to the balance point (center of mass) of a histogram?", "The Mean (Arithmetic Average)", "Mean as center of gravity")
        ],
        'tmpls': [
            "{0}",
            "In statistical analysis of histograms: {0}",
            "Identify the distribution characteristic: {0}",
            "Regarding the shape and modal class of a histogram: {0}",
            "Which description characterizes: {0}?",
            "What does this histogram feature signify: {0}?",
            "Analyze the distribution shape: {0}",
            "Determine the accurate statistical term: {0}",
            "Select the correct answer: {0}",
            "In interpreting histogram profiles: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Median class",
                "Range interval",
                "Zero-variance distribution"
            ],
            f"**Step 1: Identify the graphical feature of the histogram.**\nExamine the peak (tallest bar), symmetry, or tails of the distribution.\n\n**Step 2: Match to the statistical concept.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Step-by-Step Procedure for Constructing a Uniform Histogram
    arch7 = {
        'data': [
            ("What is the first prerequisite step before drawing a histogram for discontinuous (inclusive) classes like 1-10, 11-20?", "Convert the classes into continuous form (0.5-10.5, 10.5-20.5) by applying the 0.5 adjustment factor", "Mandatory continuity step"),
            ("After marking continuous class limits on the horizontal axis and frequencies on the vertical axis, how are the rectangles drawn?", "Erect vertical rectangles over each class interval with base equal to class width and height equal to class frequency", "Standard histogram construction"),
            ("Why should the rectangles in a histogram share common vertical boundaries?", "Because the upper boundary of one continuous class is identical to the lower boundary of the next class", "Contiguity of intervals"),
            ("Can class intervals on the X-axis have gaps between rectangles in a histogram?", "No, because the underlying data is continuous, so rectangles must touch each other", "No gaps in histograms"),
            ("If a class interval has a frequency of 0, what does the histogram show for that class?", "No vertical rectangle is drawn (height = 0), leaving a flat base on the X-axis", "Zero frequency representation"),
            ("What information must always be written on a completed histogram?", "Title of graph, labels on both axes with units, and the scale used", "Complete graph specifications"),
            ("If the first class interval is 50-60, what must be drawn between 0 and 50 on the X-axis?", "A kink (broken line / zigzag mark)", "Axis break mark"),
            ("In NCERT Class 9, what type of graph is drawn by joining the midpoints of the tops of the rectangles of a histogram?", "A Frequency Polygon", "Construction of frequency polygon"),
            ("Why is shade or light hatching sometimes applied to histogram rectangles?", "To visually distinguish adjacent bars and improve graphical readability", "Aesthetic and presentation clarity"),
            ("What is the fundamental law of histograms that must NEVER be violated?", "The area of each rectangle must be directly proportional to the frequency of that class interval", "The Area Principle of Histograms")
        ],
        'tmpls': [
            "{0}",
            "In constructing a standard uniform histogram: {0}",
            "What is the required step or rule: {0}?",
            "Identify the correct procedure for histogram construction: {0}",
            "Which guideline must be followed in: {0}?",
            "Explain the technical step: {0}",
            "Determine the accurate construction rule: {0}",
            "What is the standard procedure for: {0}?",
            "Select the accurate construction protocol: {0}",
            "In NCERT Class 9 histogram drawing: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Leave 1 cm gap between all rectangles",
                "Draw circular arcs instead of rectangles",
                "Omit the axes entirely"
            ],
            f"**Step 1: Review the formal rules of histogram construction.**\n1. Ensure continuous classes.\n2. Mark class limits on X-axis and frequency on Y-axis.\n3. Draw contiguous rectangles with height equal to frequency.\n\n**Step 2: Detail the specific requirement.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 10.1.3: Histograms with varying intervals: adjusted frequency
# ==============================================================================
def gen_10_1_3():
    tc = "CBSE-9-MGM-10-10.1.3"
    tname = "Histograms with varying intervals: adjusted frequency"

    # Arch 0: The fundamental reason for adjusting frequencies
    arch0 = {
        'data': [
            ("In a histogram where class intervals have varying (unequal) widths, why CANNOT we directly use the given frequencies as rectangle heights?", "Because in a histogram, AREA represents frequency. If width varies, drawing unadjusted height creates a distorted area that gives a false impression", "The Area Principle of Histograms"),
            ("What does the height of each rectangle represent in a histogram with varying class intervals?", "Adjusted Frequency (or Frequency Density = Frequency / Class Width)", "Height represents frequency density"),
            ("If a class interval has double the width of the minimum class width, how must its height be adjusted to keep area proportional to frequency?", "The height must be halved: Adjusted Height = Frequency / 2", "Compensating for double width"),
            ("If a class interval has triple the width of the minimum class width, how must its height be adjusted?", "The height must be divided by 3: Adjusted Height = Frequency / 3", "Compensating for triple width"),
            ("What is the standard NCERT formula for Adjusted Frequency of a class?", "Adjusted Frequency = (Minimum Class Width / Class Width of this class) * Given Frequency", "Standard NCERT adjustment formula"),
            ("In the adjusted frequency formula, what does 'Minimum Class Width' represent?", "The smallest class width among all the class intervals in the given table", "Base unit width"),
            ("Why does drawing a histogram with unadjusted heights for varying widths mislead the viewer?", "Because wider classes would have artificially huge areas, making low-frequency wide classes look dominant", "Visual distortion of area"),
            ("When all class widths are equal, what does the ratio (Minimum Class Width / Class Width) equal?", "1 (which is why no adjustment is needed for uniform histograms)", "Special case of uniform width"),
            ("What physical analogy describes the height of a rectangle in a varying-width histogram?", "Density (Mass per unit volume = Frequency per unit width)", "Frequency density analogy"),
            ("In NCERT Class 9, is varying-width histogram construction a core tested topic?", "Yes, it is one of the most important concepts tested in Class 9 statistics", "Core NCERT curriculum topic")
        ],
        'tmpls': [
            "{0}",
            "In histograms with unequal class widths: {0}",
            "Why must frequencies be adjusted: {0}?",
            "Regarding histograms with varying class intervals: {0}",
            "Identify the fundamental principle behind: {0}",
            "Which statement correctly explains: {0}?",
            "What is the mathematical reason for: {0}?",
            "Analyze the varying-width histogram rule: {0}",
            "Determine the correct formula or concept: {0}",
            "Select the accurate explanation: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Heights are always plotted directly without any modification",
                "Widths must be changed to make all intervals equal",
                "Histograms cannot be drawn for unequal intervals"
            ],
            f"**Step 1: Understand the Area Principle of Histograms.**\nIn a histogram, \\( \\text{{Area}} \\propto \\text{{Frequency}} \\).\nSince \\( \\text{{Area}} = \\text{{Width}} \\times \\text{{Height}} \\), we must have \\( \\text{{Height}} \\propto \\frac{{\\text{{Frequency}}}}{{\\text{{Width}}}} \\).\n\n**Step 2: State the adjustment rule.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Applying the Adjusted Frequency Formula (Standard NCERT Calculations)
    arch1 = {
        'data': [
            (1, 2, 6, 3, "(1 / 2) * 6 = 3"),
            (1, 3, 9, 3, "(1 / 3) * 9 = 3"),
            (1, 5, 20, 4, "(1 / 5) * 20 = 4"),
            (1, 2, 12, 6, "(1 / 2) * 12 = 6"),
            (1, 4, 16, 4, "(1 / 4) * 16 = 4"),
            (2, 4, 10, 5, "(2 / 4) * 10 = 5"),
            (2, 6, 18, 6, "(2 / 6) * 18 = 6"),
            (2, 10, 30, 6, "(2 / 10) * 30 = 6"),
            (5, 10, 24, 12, "(5 / 10) * 24 = 12"),
            (5, 15, 36, 12, "(5 / 15) * 36 = 12")
        ],
        'tmpls': [
            "In a dataset where the minimum class width is {0}, a class has width {1} and frequency {2}. What is its adjusted frequency (height of rectangle)?",
            "Calculate the adjusted frequency for a class of width {1} with frequency {2}, given that the minimum class width in the table is {0}:",
            "What height should be drawn for a class interval of width {1} and frequency {2} if the minimum interval width is {0}?",
            "Using the NCERT formula, evaluate the adjusted frequency for minimum width = {0}, class width = {1}, and frequency = {2}:",
            "Find the adjusted height: minimum width {0}, current class width {1}, frequency {2}:",
            "Compute the adjusted frequency: \\( \\frac{{{0}}}{{{1}}} \\times {2} \\):",
            "What is the adjusted frequency when min width is {0}, class width is {1}, and frequency is {2}?",
            "Determine the height of the rectangle for width {1} and frequency {2} (minimum width = {0}):",
            "Evaluate adjusted frequency for: min width {0}, width {1}, frequency {2}:",
            "Calculate the adjusted frequency for this class: {0}, {1}, {2}:"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            [f"{item[3] + 2}", f"{item[3] * 2}", f"{item[2]}"],
            f"**Step 1: Write down the adjusted frequency formula.**\n\\[ \\text{{Adjusted Frequency}} = \\frac{{\\text{{Minimum Class Width}}}}{{\\text{{Class Width}}}} \\times \\text{{Frequency}} \\]\n\n**Step 2: Substitute \\( \\text{{min width}} = {item[0]} \\), \\( \\text{{width}} = {item[1]} \\), and \\( f = {item[2]} \\).**\n\\[ \\text{{Adjusted Frequency}} = \\frac{{{item[0]}}}{{{item[1]}}} \\times {item[2]} = {item[4]} \\]\n\n**Step 3: State the answer.**\nThe adjusted frequency is {item[3]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Full Table Example: Children Playing in a Park (Classic NCERT Example)
    arch2 = {
        'data': [
            ("Age: 1-2 (width 1, freq 5)", 1, 1, 5, 5, "(1 / 1) * 5 = 5"),
            ("Age: 2-3 (width 1, freq 3)", 1, 1, 3, 3, "(1 / 1) * 3 = 3"),
            ("Age: 3-5 (width 2, freq 6)", 1, 2, 6, 3, "(1 / 2) * 6 = 3"),
            ("Age: 5-7 (width 2, freq 12)", 1, 2, 12, 6, "(1 / 2) * 12 = 6"),
            ("Age: 7-10 (width 3, freq 9)", 1, 3, 9, 3, "(1 / 3) * 9 = 3"),
            ("Age: 10-15 (width 5, freq 10)", 1, 5, 10, 2, "(1 / 5) * 10 = 2"),
            ("Age: 15-17 (width 2, freq 4)", 1, 2, 4, 2, "(1 / 2) * 4 = 2"),
            ("In the NCERT park example (ages 1-2 to 15-17), what is the minimum class width in the table?", 1, 1, 1, 1, "Ages 1-2 and 2-3 have minimum width = 1"),
            ("For age group 10-15 (width 5, frequency 10, min width 1), what is the adjusted height of the rectangle?", 1, 5, 10, 2, "(1 / 5) * 10 = 2"),
            ("For age group 5-7 (width 2, frequency 12, min width 1), what is the adjusted height of the rectangle?", 1, 2, 12, 6, "(1 / 2) * 12 = 6")
        ],
        'tmpls': [
            "In the classic NCERT park age distribution with minimum class width = 1: for {0}, what is the adjusted frequency?",
            "Calculate the adjusted frequency for: {0} (minimum width = 1):",
            "What height of rectangle should be drawn for: {0}?",
            "Using the NCERT adjusted frequency formula, evaluate the height for: {0}:",
            "Determine the adjusted frequency for: {0}:",
            "Find the rectangle height for: {0} with min width = 1:",
            "From the NCERT varying-width example: {0}, calculate the adjusted height:",
            "Compute the adjusted frequency for the class: {0}:",
            "Evaluate the adjusted height for: {0}:",
            "What is the plotted height for: {0}?"
        ],
        'calc': lambda item: (
            f"{item[4]}",
            [f"{item[4] + 2}", f"{item[4] * 2}", f"{item[3]}"],
            f"**Step 1: Identify the minimum class width and the class width of this interval.**\nMinimum width = \\( {item[1]} \\), Class width = \\( {item[2]} \\), Given frequency = \\( {item[3]} \\).\n\n**Step 2: Compute adjusted frequency.**\n\\[ \\text{{Adjusted Frequency}} = \\frac{{{item[1]}}}{{{item[2]}}} \\times {item[3]} = {item[5]} \\]\n\n**Step 3: State the answer.**\nThe adjusted frequency is {item[4]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Another Classic NCERT Example: Letters in Surnames
    arch3 = {
        'data': [
            ("Letters 1-4 (width 3, freq 6)", 2, 3, 6, 4, "(2 / 3) * 6 = 4"),
            ("Letters 4-6 (width 2, freq 30)", 2, 2, 30, 30, "(2 / 2) * 30 = 30"),
            ("Letters 6-8 (width 2, freq 44)", 2, 2, 44, 44, "(2 / 2) * 44 = 44"),
            ("Letters 8-12 (width 4, freq 16)", 2, 4, 16, 8, "(2 / 4) * 16 = 8"),
            ("Letters 12-20 (width 8, freq 4)", 2, 8, 4, 1, "(2 / 8) * 4 = 1"),
            ("In the surname letters dataset (1-4, 4-6, 6-8, 8-12, 12-20), what is the minimum class width?", 2, 2, 2, 2, "Classes 4-6 and 6-8 have minimum width = 2"),
            ("For letters 8-12 (width 4, frequency 16, min width 2), what is the adjusted frequency?", 2, 4, 16, 8, "(2 / 4) * 16 = 8"),
            ("For letters 12-20 (width 8, frequency 4, min width 2), what is the adjusted frequency?", 2, 8, 4, 1, "(2 / 8) * 4 = 1"),
            ("For letters 1-4 (width 3, frequency 6, min width 2), what is the adjusted frequency?", 2, 3, 6, 4, "(2 / 3) * 6 = 4"),
            ("In this surname histogram, which interval has the tallest adjusted rectangle?", 2, 2, 44, 44, "Class 6-8 has tallest adjusted height = 44")
        ],
        'tmpls': [
            "In the NCERT surname letters distribution where minimum class width is 2: for {0}, what is the adjusted frequency?",
            "Calculate the adjusted frequency for: {0} (min width = 2):",
            "What height should be drawn for: {0}?",
            "Evaluate the adjusted frequency for: {0}:",
            "Determine the rectangle height for: {0}:",
            "Find the adjusted frequency of: {0}:",
            "Using min width = 2, compute the adjusted height for: {0}:",
            "What is the plotted height for: {0}?",
            "Calculate adjusted frequency for class: {0}:",
            "From the surname letters table: {0}, find the adjusted frequency:"
        ],
        'calc': lambda item: (
            f"{item[4]}" if isinstance(item[4], int) else item[4],
            [f"{item[4] + 4}" if isinstance(item[4], int) else "Class 4-6", f"{item[4] // 2 if isinstance(item[4], int) and item[4] > 2 else 2}" if isinstance(item[4], int) else "Class 1-4", f"{item[3]}" if isinstance(item[4], int) else "Class 8-12"],
            f"**Step 1: Identify min width, class width, and frequency.**\nMinimum width = \\( {item[1]} \\), Class width = \\( {item[2]} \\), Frequency = \\( {item[3]} \\).\n\n**Step 2: Apply the NCERT adjusted frequency formula.**\n\\[ \\text{{Adjusted Frequency}} = \\frac{{{item[1]}}}{{{item[2]}}} \\times {item[3]} = {item[5]} \\]\n\n**Step 3: State the answer.**\nThe adjusted frequency is {item[4]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Verifying area conservation in varying-width histograms
    arch4 = {
        'data': [
            ("A class of width 4 has frequency 16 (min width 2). Its adjusted height is 8. What is the area of its rectangle (width * height)?", 4, 8, 32, "Area = 4 * 8 = 32 = 2 * 16 (proportional to frequency by factor min width 2)"),
            ("A class of width 8 has frequency 4 (min width 2). Its adjusted height is 1. What is the area of its rectangle?", 8, 1, 8, "Area = 8 * 1 = 8 = 2 * 4 (proportional to frequency by factor 2)"),
            ("A class of width 5 has frequency 10 (min width 1). Its adjusted height is 2. What is the area of its rectangle?", 5, 2, 10, "Area = 5 * 2 = 10 = 1 * 10 (strictly equal to frequency)"),
            ("A class of width 3 has frequency 9 (min width 1). Its adjusted height is 3. What is the area of its rectangle?", 3, 3, 9, "Area = 3 * 3 = 9 = 1 * 9 (strictly equal to frequency)"),
            ("When minimum class width is 1, the area of each rectangle in the histogram is:", "Strictly equal to the frequency of that class interval", "Area = Width * (1/Width * Frequency) = Frequency"),
            ("When minimum class width is c, the area of each rectangle in the histogram is:", "Equal to c * Frequency", "Area = Width * (c/Width * Frequency) = c * Frequency"),
            ("Does the total area of all rectangles in a varying-width histogram (with min width 1) equal the total frequency N?", "Yes, the total area exactly equals the total frequency N", "Area conservation principle"),
            ("Why does the area representation ensure fairness between narrow and wide intervals?", "Because a wide interval spread over a large base has its height reduced so its total visual weight matches its actual frequency", "Visual fairness and statistical integrity"),
            ("If a class has frequency 20 and width 10, and another class has frequency 20 and width 2, which rectangle is taller?", "The class with width 2 is 5 times taller than the class with width 10", "20/2 = 10 vs 20/10 = 2"),
            ("In the previous question, which of the two rectangles has larger area?", "Both rectangles have the exact same area, correctly showing they have the exact same frequency (20)", "Equal frequency means equal area")
        ],
        'tmpls': [
            "{0}",
            "Regarding area conservation in histograms: {0}",
            "In histograms with unequal intervals: {0}",
            "Calculate or analyze the area: {0}",
            "What is the mathematical relationship: {0}?",
            "Analyze the area principle: {0}",
            "Determine the accurate conclusion: {0}",
            "Which statement correctly evaluates: {0}?",
            "In Class 9 statistics: {0}",
            "Select the accurate area insight: {0}"
        ],
        'calc': lambda item: (
            f"{item[3]}" if len(item) > 4 else item[1],
            [
                f"{item[3] + 10}" if len(item) > 4 else "The rectangle with width 10 has 5 times larger area",
                f"{item[3] - 5}" if len(item) > 4 else "Area is not related to frequency",
                "100" if len(item) > 4 else "The taller rectangle always has larger area"
            ],
            f"**Step 1: Understand how area is calculated in a histogram.**\n\\( \\text{{Area}} = \\text{{Class Width}} \\times \\text{{Adjusted Height}} \\).\n\n**Step 2: Compute the area.**\n{item[4] if len(item) > 4 else item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[3] if len(item) > 4 else item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Frequency Density concept (Frequency / Class Width)
    arch5 = {
        'data': [
            (20, 5, 4.0, "20 / 5 = 4.0"),
            (35, 7, 5.0, "35 / 7 = 5.0"),
            (18, 6, 3.0, "18 / 6 = 3.0"),
            (45, 9, 5.0, "45 / 9 = 5.0"),
            (12, 4, 3.0, "12 / 4 = 3.0"),
            (50, 10, 5.0, "50 / 10 = 5.0"),
            (15, 3, 5.0, "15 / 3 = 5.0"),
            (28, 7, 4.0, "28 / 7 = 4.0"),
            (16, 8, 2.0, "16 / 8 = 2.0"),
            (30, 15, 2.0, "30 / 15 = 2.0")
        ],
        'tmpls': [
            "Calculate the Frequency Density for a class interval with frequency {0} and class width {1}:",
            "What is the frequency density \\( \\frac{{\\text{{Frequency}}}}{{\\text{{Class Width}}}} \\) for \\( f = {0} \\) and \\( w = {1} \\)?",
            "Find the frequency per unit width for a class with {0} observations spread over width {1}:",
            "Determine the frequency density for: frequency = {0}, width = {1}:",
            "Compute the density ratio \\( {0} / {1} \\):",
            "Evaluate frequency density: \\( f = {0}, w = {1} \\):",
            "What is the frequency density of this group: frequency {0}, class size {1}?",
            "Find the frequency density for class width {1} having frequency {0}:",
            "Calculate \\( \\text{{Frequency Density}} = \\frac{{{0}}}{{{1}}} \\):",
            "For frequency {0} and width {1}, find the frequency density:"
        ],
        'calc': lambda item: (
            f"{item[2]}",
            [f"{item[2] + 1.0}", f"{item[2] - 1.0 if item[2] > 1.0 else item[2] + 2.0}", f"{item[0]}"],
            f"**Step 1: Write down the definition of Frequency Density.**\n\\[ \\text{{Frequency Density}} = \\frac{{\\text{{Class Frequency}}}}{{\\text{{Class Width}}}} \\]\n\n**Step 2: Substitute \\( f = {item[0]} \\) and \\( w = {item[1]} \\).**\n\\[ \\text{{Frequency Density}} = \\frac{{{item[0]}}}{{{item[1]}}} = {item[3]} = {item[2]} \\]\n\n**Step 3: State the answer.**\nThe frequency density is {item[2]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Identifying errors in student-drawn histograms with unequal intervals
    arch6 = {
        'data': [
            ("A student draws a histogram for classes 0-10, 10-20, 20-40, 40-70 by plotting the given raw frequencies directly as heights. What is the fundamental error?", "Failing to adjust frequencies for unequal class widths (violating the Area Principle)", "Area of 20-40 and 40-70 will be 2x and 3x too large"),
            ("In the same flawed graph, class 20-40 has frequency 10 and class 10-20 has frequency 10. How do their drawn rectangle areas compare?", "The rectangle for 20-40 has TWICE the area of 10-20, falsely implying it has twice the frequency", "Visual distortion: width 20 vs 10"),
            ("How should the student correct the height of class 20-40 (frequency 10, width 20, min width 10)?", "Draw height = (10/20) * 10 = 5 units instead of 10 units", "Adjusted frequency = 5"),
            ("How should the student correct the height of class 40-70 (frequency 15, width 30, min width 10)?", "Draw height = (10/30) * 15 = 5 units instead of 15 units", "Adjusted frequency = 5"),
            ("Why is drawing unequal intervals on the X-axis as equal segments (e.g. making 0-10, 10-20, 20-50 all 2 cm wide) completely wrong?", "Because the X-axis must maintain a uniform numerical scale; a width of 30 must physically be 3 times wider than a width of 10", "X-axis must maintain strict physical scale"),
            ("Can you make all rectangles have the same width by changing the dataset's class intervals arbitrarily?", "No, altering class boundaries would corrupt the raw data grouping", "Must adjust heights, not boundaries"),
            ("What single mathematical invariant must be preserved across every histogram ever drawn?", "Rectangle Area must be directly proportional to Class Frequency", "The Area Invariant"),
            ("If a student divides the frequency by the class width without multiplying by the minimum class width, is the resulting histogram geometrically valid?", "Yes, it is valid because all heights are scaled by the constant factor (minimum class width), preserving exact area proportions", "Frequency density histogram"),
            ("What is the advantage of multiplying by the minimum class width (the NCERT formula)?", "It ensures that for the narrowest classes (width = min width), the drawn height exactly equals the original given frequency", "Convenience of NCERT formula"),
            ("In an exam question with unequal intervals, what fraction of marks is typically deducted if adjusted frequency is not computed?", "Typically 50% to 100% of the graph marks, because plotting raw heights is a conceptual failure", "Severe grading penalty for unadjusted heights")
        ],
        'tmpls': [
            "{0}",
            "In diagnosing errors in histogram construction: {0}",
            "Why is this student's histogram flawed: {0}?",
            "Regarding common mistakes in varying-width histograms: {0}",
            "Identify the conceptual error: {0}",
            "Analyze the flawed graphical representation: {0}",
            "Determine the correct remedy for the error: {0}",
            "Which description accurately identifies the mistake: {0}?",
            "In CBSE Class 9 grading criteria: {0}",
            "Select the accurate statistical correction: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The student forgot to use a kink on the Y-axis",
                "The graph is completely correct as drawn",
                "Histograms cannot have widths greater than 10"
            ],
            f"**Step 1: Identify the error in treating unequal intervals like equal intervals.**\nPlotting raw frequencies when widths differ violates the Area Principle.\n\n**Step 2: State the correct statistical rule.**\n{item[2]}.\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Step-by-Step Construction Procedure for Varying-Width Histograms
    arch7 = {
        'data': [
            ("Step 1 in constructing a varying-width histogram is to compute the class width of each class interval: Width = Upper limit - Lower limit. What is Step 2?", "Identify the minimum class width among all the class intervals", "Finding base width"),
            ("What is Step 3 in the varying-width histogram procedure?", "Compute the Adjusted Frequency for each class using (Min Width / Class Width) * Frequency", "Calculating adjusted heights"),
            ("What is Step 4 in the procedure?", "Set up a uniform scale on the X-axis and Y-axis, plotting class limits on the X-axis and Adjusted Frequencies on the Y-axis", "Setting up scales"),
            ("What is Step 5 in the procedure?", "Draw contiguous rectangles over each class interval with base equal to class width and height equal to Adjusted Frequency", "Drawing adjusted rectangles"),
            ("In the completed graph, what should the vertical axis (Y-axis) be labeled?", "'Adjusted Frequency' (or 'Proportion of Frequency per unit width')", "Accurate axis labeling"),
            ("If the class intervals are 10-15 (width 5), 15-20 (width 5), 20-30 (width 10), 30-50 (width 20), what is the minimum class width?", "5", "Smallest width is 5"),
            ("For class 30-50 (width 20, frequency 24, min width 5), what is the adjusted frequency?", "(5 / 20) * 24 = 6", "(5/20)*24 = 6"),
            ("For class 20-30 (width 10, frequency 18, min width 5), what is the adjusted frequency?", "(5 / 10) * 18 = 9", "(5/10)*18 = 9"),
            ("For class 10-15 (width 5, frequency 7, min width 5), what is the adjusted frequency?", "(5 / 5) * 7 = 7", "Width equals min width, so height = frequency"),
            ("Why does the completed varying-width histogram give an honest and accurate visualization of data?", "Because the visual area perceived by the eye correctly mirrors the actual number of observations in every single interval", "Visual fidelity and honest representation")
        ],
        'tmpls': [
            "{0}",
            "In the full procedure for drawing varying-width histograms: {0}",
            "What is the required step in: {0}?",
            "Identify the correct construction phase: {0}",
            "Which step corresponds to: {0}?",
            "Explain the systematic procedure: {0}",
            "Determine the accurate protocol: {0}",
            "In NCERT Class 9 varying-width histograms: {0}",
            "Select the accurate methodological step: {0}",
            "Follow the algorithm for varying intervals: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Change all class widths to 10",
                "Omit the wider class intervals",
                "Draw separate unconnected bar charts"
            ],
            f"**Step 1: Follow the systematic 5-step algorithm.**\n1. Find width of each class.\n2. Find minimum width.\n3. Calculate adjusted frequencies.\n4. Set uniform axis scales.\n5. Draw contiguous rectangles.\n\n**Step 2: Detail the specific step.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_10_1_1()
    q2 = gen_10_1_2()
    q3 = gen_10_1_3()
    print(f"gen_10_1_1: {len(q1)} questions")
    print(f"gen_10_1_2: {len(q2)} questions")
    print(f"gen_10_1_3: {len(q3)} questions")
