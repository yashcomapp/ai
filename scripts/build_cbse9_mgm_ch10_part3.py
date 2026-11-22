# scripts/build_cbse9_mgm_ch10_part3.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 10: How Quantities Combine: Understanding Data
Part 3:
- Subtopic 10.3.1: Mean, median, and mode for ungrouped data
- Subtopic 10.3.2: Weighted arithmetic mean and mixing proportions
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 10
CH_NAME = "How Quantities Combine: Understanding Data"

# ==============================================================================
# SUBTOPIC 10.3.1: Mean, median, and mode for ungrouped data
# ==============================================================================
def gen_10_3_1():
    tc = "CBSE-9-MGM-10-10.3.1"
    tname = "Mean, median, and mode for ungrouped data"

    # Arch 0: Arithmetic Mean of raw ungrouped data
    arch0 = {
        'data': [
            ("4, 6, 8, 10, 12", 40, 5, 8.0, "(4+6+8+10+12)/5 = 40/5 = 8"),
            ("10, 15, 20, 25, 30", 100, 5, 20.0, "(10+15+20+25+30)/5 = 100/5 = 20"),
            ("5, 9, 12, 14, 15", 55, 5, 11.0, "(5+9+12+14+15)/5 = 55/5 = 11"),
            ("2, 3, 5, 7, 11, 14", 42, 6, 7.0, "(2+3+5+7+11+14)/6 = 42/6 = 7"),
            ("12, 18, 24, 30, 36", 120, 5, 24.0, "(12+18+24+30+36)/5 = 120/5 = 24"),
            ("7, 11, 15, 19, 23, 27", 102, 6, 17.0, "(7+11+15+19+23+27)/6 = 102/6 = 17"),
            ("20, 22, 25, 28, 30", 125, 5, 25.0, "(20+22+25+28+30)/5 = 125/5 = 25"),
            ("1, 2, 3, 4, 5, 6, 7", 28, 7, 4.0, "28/7 = 4"),
            ("8, 12, 16, 20, 24, 28, 32", 140, 7, 20.0, "140/7 = 20"),
            ("50, 60, 70, 80, 90", 350, 5, 70.0, "350/5 = 70")
        ],
        'tmpls': [
            "Find the arithmetic mean of the raw data: {0}:",
            "What is the mean of the numbers: {0}?",
            "Calculate \\( \\bar{{x}} = \\frac{{\\sum x_i}}{{n}} \\) for the dataset: {0}:",
            "Determine the average of the observations: {0}:",
            "Compute the mean score: {0}:",
            "Evaluate the arithmetic mean of the values: {0}:",
            "What is the mean of: {0}?",
            "Find the average for the sample: {0}:",
            "Calculate the mean of the dataset: {0}:",
            "Determine the mean value of: {0}:"
        ],
        'calc': lambda item: (
            f"{int(item[3]) if item[3].is_integer() else item[3]}",
            [f"{int(item[3]) + 2}", f"{int(item[3]) - 2 if item[3] > 2 else int(item[3]) + 4}", f"{int(item[3]) + 5}"],
            f"**Step 1: Write down the formula for the arithmetic mean.**\n\\[ \\bar{{x}} = \\frac{{\\sum x_i}}{{n}} \\]\n\n**Step 2: Sum the observations and divide by \\( n = {item[2]} \\).**\n\\[ \\sum x_i = {item[1]} \\implies \\bar{{x}} = {item[4]} \\]\n\n**Step 3: State the answer.**\nThe arithmetic mean is {int(item[3]) if item[3].is_integer() else item[3]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Median of raw ungrouped data for ODD n
    arch1 = {
        'data': [
            ("12, 5, 8, 20, 15", "5, 8, 12, 15, 20", 5, 12, "3rd term in sorted list = 12"),
            ("25, 18, 32, 10, 45", "10, 18, 25, 32, 45", 5, 25, "3rd term = 25"),
            ("7, 2, 9, 4, 11, 8, 5", "2, 4, 5, 7, 8, 9, 11", 7, 7, "4th term in sorted list = 7"),
            ("14, 22, 9, 31, 18", "9, 14, 18, 22, 31", 5, 18, "3rd term = 18"),
            ("40, 15, 60, 25, 80, 50, 30", "15, 25, 30, 40, 50, 60, 80", 7, 40, "4th term = 40"),
            ("3, 11, 7, 19, 15", "3, 7, 11, 15, 19", 5, 11, "3rd term = 11"),
            ("52, 38, 65, 44, 70", "38, 44, 52, 65, 70", 5, 52, "3rd term = 52"),
            ("8, 1, 15, 4, 12, 19, 6", "1, 4, 6, 8, 12, 15, 19", 7, 8, "4th term = 8"),
            ("90, 45, 75, 60, 80", "45, 60, 75, 80, 90", 5, 75, "3rd term = 75"),
            ("10, 30, 20, 50, 40", "10, 20, 30, 40, 50", 5, 30, "3rd term = 30")
        ],
        'tmpls': [
            "Find the median of the raw data: {0}:",
            "What is the median value of the numbers: {0}?",
            "Calculate the median for the dataset: {0}:",
            "Determine the median of the observations: {0}:",
            "Arrange the data in ascending order and find the median: {0}:",
            "Evaluate the median of: {0}:",
            "What is the median observation among: {0}?",
            "Find the median for: {0}:",
            "Compute the median score of: {0}:",
            "Determine the middle value (median) of: {0}:"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            [f"{item[3] + 3}", f"{item[3] - 4}", f"{item[3] + 8}"],
            f"**Step 1: Arrange the data in ascending order.**\nOrdered dataset: \\( {item[1]} \\).\n\n**Step 2: Find the middle term.**\nSince \\( n = {item[2]} \\) is odd, \\( \\text{{Median}} = \\left(\\frac{{{item[2]} + 1}}{{2}}\\right)\\text{{-th observation}} \\).\n{item[4]}.\n\n**Step 3: State the answer.**\nThe median is {item[3]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Median of raw ungrouped data for EVEN n
    arch2 = {
        'data': [
            ("8, 12, 5, 15, 20, 10", "5, 8, 10, 12, 15, 20", 6, 11.0, "(10 + 12) / 2 = 11"),
            ("14, 22, 8, 18, 30, 10", "8, 10, 14, 18, 22, 30", 6, 16.0, "(14 + 18) / 2 = 16"),
            ("25, 40, 15, 30, 50, 20", "15, 20, 25, 30, 40, 50", 6, 27.5, "(25 + 30) / 2 = 27.5"),
            ("6, 11, 4, 15, 9, 20, 13, 2", "2, 4, 6, 9, 11, 13, 15, 20", 8, 10.0, "(9 + 11) / 2 = 10"),
            ("35, 12, 45, 28, 50, 18", "12, 18, 28, 35, 45, 50", 6, 31.5, "(28 + 35) / 2 = 31.5"),
            ("7, 13, 19, 5, 25, 11", "5, 7, 11, 13, 19, 25", 6, 12.0, "(11 + 13) / 2 = 12"),
            ("60, 40, 80, 50, 90, 70", "40, 50, 60, 70, 80, 90", 6, 65.0, "(60 + 70) / 2 = 65"),
            ("16, 24, 12, 32, 20, 28", "12, 16, 20, 24, 28, 32", 6, 22.0, "(20 + 24) / 2 = 22"),
            ("3, 9, 15, 5, 12, 7", "3, 5, 7, 9, 12, 15", 6, 8.0, "(7 + 9) / 2 = 8"),
            ("44, 56, 32, 68, 48, 60", "32, 44, 48, 56, 60, 68", 6, 52.0, "(48 + 56) / 2 = 52")
        ],
        'tmpls': [
            "Find the median of the even-numbered raw data set: {0}:",
            "What is the median for the observations: {0}?",
            "Calculate the median for: {0} (where n is even):",
            "Determine the median of the numbers: {0}:",
            "Arrange the dataset {0} in order and calculate its median:",
            "Evaluate the median of: {0}:",
            "What is the average of the two middle terms for: {0}?",
            "Find the median value of: {0}:",
            "Compute the median for the sample: {0}:",
            "Determine the median of: {0}:"
        ],
        'calc': lambda item: (
            f"{int(item[3]) if item[3].is_integer() else item[3]}",
            [f"{item[3] + 2}", f"{item[3] - 2}", f"{item[3] + 5}"],
            f"**Step 1: Arrange the observations in ascending order.**\nOrdered list: \\( {item[1]} \\).\n\n**Step 2: Apply the median formula for even \\( n = {item[2]} \\).**\n\\[ \\text{{Median}} = \\frac{{\\left(\\frac{{n}}{{2}}\\right)\\text{{-th observation}} + \\left(\\frac{{n}}{{2}} + 1\\right)\\text{{-th observation}}}}{{2}} \\]\n\\[ \\text{{Median}} = {item[4]} = {int(item[3]) if item[3].is_integer() else item[3]} \\]\n\n**Step 3: State the answer.**\nThe median is {int(item[3]) if item[3].is_integer() else item[3]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Mode of raw ungrouped data
    arch3 = {
        'data': [
            ("4, 6, 8, 6, 10, 6, 12", 6, 3, "6 appears 3 times (highest frequency)"),
            ("14, 25, 14, 28, 14, 18, 25", 14, 3, "14 appears 3 times"),
            ("2, 5, 2, 8, 2, 9, 5, 2", 2, 4, "2 appears 4 times"),
            ("15, 20, 22, 20, 25, 20, 30", 20, 3, "20 appears 3 times"),
            ("7, 9, 11, 9, 13, 9, 15, 9", 9, 4, "9 appears 4 times"),
            ("32, 45, 32, 50, 32, 60", 32, 3, "32 appears 3 times"),
            ("11, 13, 15, 13, 17, 13, 19", 13, 3, "13 appears 3 times"),
            ("40, 50, 40, 60, 40, 70, 80", 40, 3, "40 appears 3 times"),
            ("5, 8, 12, 8, 15, 8, 20", 8, 3, "8 appears 3 times"),
            ("100, 105, 100, 110, 100, 115", 100, 3, "100 appears 3 times")
        ],
        'tmpls': [
            "Find the mode of the numbers: {0}:",
            "What is the mode of the dataset: {0}?",
            "Determine the most frequently occurring value (mode) in: {0}:",
            "Calculate the mode for the observations: {0}:",
            "Identify the mode of: {0}:",
            "Which observation represents the mode in: {0}?",
            "Find the mode of the raw data: {0}:",
            "What is the modal value of: {0}?",
            "Evaluate the mode of: {0}:",
            "Determine the mode for: {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1] + 2}", f"{item[1] - 1}", f"{item[1] + 5}"],
            f"**Step 1: Count the frequency of each observation in the dataset.**\n{item[3]}.\n\n**Step 2: State the definition of mode.**\nThe mode is the observation that occurs with the maximum frequency.\n\n**Step 3: State the answer.**\nThe mode is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 4: Missing value problem using Mean
    arch4 = {
        'data': [
            ("5, 8, 12, x, 15", 10, 5, 50, 40, 10, "5 * 10 - (5+8+12+15) = 50 - 40 = 10"),
            ("10, 15, 20, x, 30", 20, 5, 100, 75, 25, "5 * 20 - 75 = 100 - 75 = 25"),
            ("6, 9, x, 14, 18", 12, 5, 60, 47, 13, "5 * 12 - 47 = 60 - 47 = 13"),
            ("3, 7, 11, x, 19, 23", 13, 6, 78, 63, 15, "6 * 13 - 63 = 78 - 63 = 15"),
            ("25, 30, x, 40, 45", 35, 5, 175, 140, 35, "5 * 35 - 140 = 175 - 140 = 35"),
            ("12, x, 16, 20, 24", 18, 5, 90, 72, 18, "5 * 18 - 72 = 90 - 72 = 18"),
            ("8, 14, x, 22, 26", 18, 5, 90, 70, 20, "5 * 18 - 70 = 90 - 70 = 20"),
            ("4, 8, 12, 16, x", 12, 5, 60, 40, 20, "5 * 12 - 40 = 60 - 40 = 20"),
            ("50, 60, 70, x, 90", 72, 5, 360, 270, 90, "5 * 72 - 270 = 360 - 270 = 90"),
            ("2, 5, 8, x, 15, 18", 10, 6, 60, 48, 12, "6 * 10 - 48 = 60 - 48 = 12")
        ],
        'tmpls': [
            "If the mean of the observations {0} is {1}, find the value of x:",
            "The average of the numbers {0} is {1}. What is the unknown value x?",
            "Given that \\( \\bar{{x}} = {1} \\) for the dataset {0}, solve for x:",
            "Find x such that the arithmetic mean of {0} equals {1}:",
            "Calculate x if the mean of {0} is {1}:",
            "Determine the missing observation x in {0} having mean {1}:",
            "What is the value of x when the average of {0} is {1}?",
            "Solve for x in the data set {0} with given mean {1}:",
            "Evaluate x given that the mean of {0} is {1}:",
            "Find the unknown observation x in: {0} (Mean = {1}):"
        ],
        'calc': lambda item: (
            f"{item[5]}",
            [f"{item[5] + 2}", f"{item[5] - 3}", f"{item[5] + 5}"],
            f"**Step 1: Set up the mean equation.**\n\\[ \\frac{{\\sum x_i}}{{n}} = {item[1]} \\implies \\sum x_i = {item[2]} \\times {item[1]} = {item[3]} \\]\n\n**Step 2: Sum the known numbers and solve for \\( x \\).**\n\\[ {item[4]} + x = {item[3]} \\implies x = {item[3]} - {item[4]} = {item[5]} \\]\n\n**Step 3: State the answer.**\nThe value of \\( x \\) is {item[5]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Linear Transformation Properties of the Mean
    arch5 = {
        'data': [
            ("If the mean of 10 observations is 25, and 3 is added to each observation, what is the new mean?", 28, "25 + 3 = 28", "Adding constant c increases mean by c"),
            ("If the mean of 15 numbers is 40, and each number is multiplied by 2, what is the new mean?", 80, "40 * 2 = 80", "Multiplying by c multiplies mean by c"),
            ("If the mean of 20 scores is 55, and 5 is subtracted from each score, what is the new mean?", 50, "55 - 5 = 50", "Subtracting c reduces mean by c"),
            ("If the mean of 8 observations is 32, and each observation is divided by 4, what is the new mean?", 8, "32 / 4 = 8", "Dividing by c divides mean by c"),
            ("If the mean of a dataset is x̄, and each observation xi is transformed to 2xi + 5, what is the new mean?", "2x̄ + 5", "New Mean = a * x̄ + b", "Linear transformation property"),
            ("If the mean of 5 numbers is 18, and one number is removed, the mean becomes 16. What was the removed number?", 26, "5 * 18 - 4 * 16 = 90 - 64 = 26", "Total sum subtraction"),
            ("If the mean of 5 numbers is 20, and a 6th number 32 is included, what is the new mean?", 22, "(5 * 20 + 32) / 6 = 132 / 6 = 22", "Total sum addition"),
            ("Does adding a constant to all observations change the standard deviation or range?", "No, range remains unchanged", "Shift does not change spread", "Invariance of dispersion to location shift"),
            ("What is the sum of the deviations of all observations from their arithmetic mean \\( \\sum (x_i - \\bar{x}) \\)?", "Always equal to 0", "Sum of (xi - mean) = 0", "Fundamental property of the mean"),
            ("If the mean of 12 numbers is 15, what is the total sum of the 12 numbers?", 180, "12 * 15 = 180", "Sum = n * mean")
        ],
        'tmpls': [
            "{0}",
            "Apply the transformation property of the mean: {0}",
            "What is the effect on the mean: {0}?",
            "Calculate the new arithmetic mean: {0}",
            "Determine the transformed mean: {0}",
            "In linear transformation of statistics: {0}",
            "Evaluate the altered mean: {0}",
            "Solve the mean modification problem: {0}",
            "Find the correct answer for: {0}",
            "Select the accurate result: {0}"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1]} + 4" if isinstance(item[1], int) else "x̄ + 10", f"{item[1]} - 3" if isinstance(item[1], int) else "2x̄", "100" if isinstance(item[1], int) else "Always positive"],
            f"**Step 1: Recall the mathematical property of the arithmetic mean.**\n{item[3]}.\n\n**Step 2: Carry out the calculation.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Mean of an ungrouped frequency table (sum fi xi / sum fi)
    arch6 = {
        'data': [
            ("xi: [10, 20, 30, 40], fi: [2, 3, 3, 2]", 10, 250, 25.0, "Sum fi = 10, Sum fi xi = 20 + 60 + 90 + 80 = 250; Mean = 250/10 = 25"),
            ("xi: [5, 10, 15, 20], fi: [4, 6, 6, 4]", 20, 250, 12.5, "Sum fi = 20, Sum fi xi = 20 + 60 + 90 + 80 = 250; Mean = 250/20 = 12.5"),
            ("xi: [2, 4, 6, 8], fi: [3, 5, 7, 5]", 20, 108, 5.4, "Sum fi = 20, Sum fi xi = 6 + 20 + 42 + 40 = 108; Mean = 108/20 = 5.4"),
            ("xi: [1, 2, 3, 4, 5], fi: [5, 4, 3, 2, 1]", 15, 35, 2.33, "Sum fi = 15, Sum fi xi = 5 + 8 + 9 + 8 + 5 = 35; Mean = 35/15 ≈ 2.33"),
            ("xi: [20, 40, 60, 80], fi: [1, 2, 3, 4]", 10, 600, 60.0, "Sum fi = 10, Sum fi xi = 20 + 80 + 180 + 320 = 600; Mean = 600/10 = 60"),
            ("xi: [3, 5, 7, 9, 11], fi: [2, 4, 6, 5, 3]", 20, 148, 7.4, "Sum fi = 20, Sum fi xi = 6 + 20 + 42 + 45 + 33 = 148; Mean = 148/20 = 7.4"),
            ("xi: [12, 14, 16, 18], fi: [2, 3, 3, 2]", 10, 150, 15.0, "Sum fi = 10, Sum fi xi = 24 + 42 + 48 + 36 = 150; Mean = 150/10 = 15"),
            ("xi: [100, 200, 300], fi: [5, 3, 2]", 10, 1700, 170.0, "Sum fi = 10, Sum fi xi = 500 + 600 + 600 = 1700; Mean = 1700/10 = 170"),
            ("xi: [15, 25, 35, 45], fi: [4, 6, 6, 4]", 20, 600, 30.0, "Sum fi = 20, Sum fi xi = 60 + 150 + 210 + 180 = 600; Mean = 600/20 = 30"),
            ("xi: [6, 8, 10, 12], fi: [5, 8, 5, 2]", 20, 168, 8.4, "Sum fi = 20, Sum fi xi = 30 + 64 + 50 + 24 = 168; Mean = 168/20 = 8.4")
        ],
        'tmpls': [
            "Find the mean of the discrete frequency distribution: {0}:",
            "Calculate \\( \\bar{{x}} = \\frac{{\\sum f_i x_i}}{{\\sum f_i}} \\) for: {0}:",
            "Compute the average for the frequency table: {0}:",
            "Determine the mean for: {0}:",
            "Evaluate the arithmetic mean of the table: {0}:",
            "What is the mean of the given distribution: {0}?",
            "Find the mean score from the table: {0}:",
            "Calculate the weighted average of the discrete distribution: {0}:",
            "Solve for the mean of: {0}:",
            "Determine the mean value of the frequency data: {0}:"
        ],
        'calc': lambda item: (
            f"{int(item[3]) if isinstance(item[3], float) and item[3].is_integer() else item[3]}",
            [f"{float(item[3]) + 2:.1f}", f"{float(item[3]) - 1.5:.1f}", f"{float(item[3]) + 5:.1f}"],
            f"**Step 1: Compute \\( \\sum f_i \\) and \\( \\sum f_i x_i \\).**\n\\[ \\sum f_i = {item[1]}, \\quad \\sum f_i x_i = {item[2]} \\]\n\n**Step 2: Divide \\( \\sum f_i x_i \\) by \\( \\sum f_i \\).**\n\\[ \\bar{{x}} = \\frac{{{item[2]}}}{{{item[1]}}} = {item[4]} \\]\n\n**Step 3: State the answer.**\nThe mean is {item[3]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Selecting the appropriate measure of central tendency
    arch7 = {
        'data': [
            ("Which measure of central tendency is MOST affected by extreme values (outliers)?", "The Mean", "Every single observation enters the sum directly, pulling mean toward outliers"),
            ("Which measure of central tendency is BEST to use when data contains severe outliers or is heavily skewed (like household income)?", "The Median", "The median is robust and insensitive to extreme outlier magnitudes"),
            ("Which measure of central tendency is used by a shoe store manager to decide which shoe sizes to order most?", "The Mode", "The mode identifies the most frequently requested / most popular size"),
            ("A ready-made garment manufacturer wanting to know the most common collar size should calculate the:", "Mode", "Modal size reflects highest sales volume"),
            ("If a student scores 90, 92, 94, 91, and 10 (absent/sick for one exam), which measure fairly reflects typical performance?", "Median (91)", "The outlier 10 drastically pulls the mean down to 75.4, while median 91 represents true ability"),
            ("Which measure of central tendency can be determined visually from the highest peak of a histogram?", "The Mode (Modal Class)", "Mode corresponds to peak frequency"),
            ("Which measure divides an ordered dataset into two halves of equal count (50% below, 50% above)?", "The Median", "50th percentile"),
            ("Can a dataset have more than one mode?", "Yes, a dataset can be bimodal (two modes) or multimodal", "Multiple peaks in frequency"),
            ("Can a dataset have more than one median?", "No, the median is always a uniquely defined single numerical value", "Uniqueness of median"),
            ("What is the unique mathematical property of the Mean regarding deviations?", "The sum of deviations of all observations from the mean is always zero: \\( \\sum (x_i - \\bar{x}) = 0 \\)", "Balance point / center of gravity")
        ],
        'tmpls': [
            "{0}",
            "In evaluating measures of central tendency: {0}",
            "Choose the appropriate statistical measure: {0}",
            "Which average should be used: {0}?",
            "Identify the correct central tendency measure for: {0}",
            "Analyze the scenario: {0}",
            "Determine the best average: {0}",
            "In applied statistics and NCERT Class 9: {0}",
            "Select the accurate statistical recommendation: {0}",
            "Regarding Mean, Median, and Mode: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The Geometric Mean",
                "The Harmonic Mean",
                "None of the measures can be used"
            ],
            f"**Step 1: Analyze the properties of the measures of central tendency.**\n- Mean: balance point, sensitive to outliers.\n- Median: middle position, robust to outliers.\n- Mode: most frequent value, used for categorical popularity.\n\n**Step 2: Match to the question.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 10.3.2: Weighted arithmetic mean and mixing proportions
# ==============================================================================
def gen_10_3_2():
    tc = "CBSE-9-MGM-10-10.3.2"
    tname = "Weighted arithmetic mean and mixing proportions"

    # Arch 0: The Weighted Mean Formula
    arch0 = {
        'data': [
            ("Values: 80, 90 with weights: 1, 3", 1, 3, 80, 90, 87.5, "(1*80 + 3*90)/(1+3) = 350/4 = 87.5"),
            ("Values: 60, 80 with weights: 2, 3", 2, 3, 60, 80, 72.0, "(2*60 + 3*80)/(2+3) = 360/5 = 72"),
            ("Values: 50, 100 with weights: 3, 2", 3, 2, 50, 100, 70.0, "(3*50 + 2*100)/(3+2) = 350/5 = 70"),
            ("Values: 40, 60, 80 with weights: 1, 2, 1", 1, 2, 40, 60, 60.0, "(1*40 + 2*60 + 1*80)/4 = 240/4 = 60"),
            ("Values: 70, 85 with weights: 1, 2", 1, 2, 70, 85, 80.0, "(1*70 + 2*85)/3 = 240/3 = 80"),
            ("Values: 10, 20 with weights: 4, 1", 4, 1, 10, 20, 12.0, "(4*10 + 1*20)/5 = 60/5 = 12"),
            ("Values: 100, 200 with weights: 3, 1", 3, 1, 100, 200, 125.0, "(3*100 + 1*200)/4 = 500/4 = 125"),
            ("Values: 45, 75 with weights: 2, 1", 2, 1, 45, 75, 55.0, "(2*45 + 1*75)/3 = 165/3 = 55"),
            ("Values: 30, 50 with weights: 1, 3", 1, 3, 30, 50, 45.0, "(1*30 + 3*50)/4 = 180/4 = 45"),
            ("Values: 65, 80 with weights: 2, 3", 2, 3, 65, 80, 74.0, "(2*65 + 3*80)/5 = 370/5 = 74")
        ],
        'tmpls': [
            "Calculate the weighted arithmetic mean for {0}:",
            "What is the weighted mean \\( \\bar{{x}}_w = \\frac{{\\sum w_i x_i}}{{\\sum w_i}} \\) for: {0}?",
            "Evaluate the weighted average: {0}:",
            "Find \\( \\bar{{x}}_w \\) given {0}:",
            "Determine the weighted mean of the numbers: {0}:",
            "Compute the weighted average for: {0}:",
            "What is the result of weighting: {0}?",
            "Calculate the weighted mean of the values: {0}:",
            "Find the weighted average: {0}:",
            "Determine the weighted mean value for: {0}:"
        ],
        'calc': lambda item: (
            f"{int(item[5]) if isinstance(item[5], float) and item[5].is_integer() else item[5]}",
            [f"{float(item[5]) + 5:.1f}", f"{float(item[5]) - 4:.1f}", f"{float(item[5]) + 10:.1f}"],
            f"**Step 1: Write down the formula for the weighted arithmetic mean.**\n\\[ \\bar{{x}}_w = \\frac{{\\sum w_i x_i}}{{\\sum w_i}} \\]\n\n**Step 2: Compute the numerator and denominator.**\n\\[ {item[6]} \\]\n\n**Step 3: State the answer.**\nThe weighted mean is {item[5]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Weighted academic test scores (Assignments, Midterms, Finals)
    arch1 = {
        'data': [
            ("Assignments: 80 (weight 20%), Midterm: 70 (weight 30%), Final: 90 (weight 50%)", 82.0, "0.20*80 + 0.30*70 + 0.50*90 = 16 + 21 + 45 = 82"),
            ("Unit Test: 75 (weight 25%), Project: 85 (weight 25%), Term Exam: 80 (weight 50%)", 80.0, "0.25*75 + 0.25*85 + 0.50*80 = 18.75 + 21.25 + 40 = 80"),
            ("Theory: 60 (weight 70%), Practical: 90 (weight 30%)", 69.0, "0.70*60 + 0.30*90 = 42 + 27 = 69"),
            ("Attendance: 100 (weight 10%), Quiz: 80 (weight 20%), Exam: 70 (weight 70%)", 75.0, "0.10*100 + 0.20*80 + 0.70*70 = 10 + 16 + 49 = 75"),
            ("Homework: 90 (weight 15%), Lab: 80 (weight 25%), Exam: 80 (weight 60%)", 81.5, "0.15*90 + 0.25*80 + 0.60*80 = 13.5 + 20 + 48 = 81.5"),
            ("Internal: 80 (weight 40%), External: 60 (weight 60%)", 68.0, "0.40*80 + 0.60*60 = 32 + 36 = 68"),
            ("Assignment: 95 (weight 10%), Test: 75 (weight 40%), Final: 85 (weight 50%)", 82.0, "0.10*95 + 0.40*75 + 0.50*85 = 9.5 + 30 + 42.5 = 82"),
            ("Oral: 90 (weight 20%), Written: 70 (weight 80%)", 74.0, "0.20*90 + 0.80*70 = 18 + 56 = 74"),
            ("Quiz: 60 (weight 20%), Midterm: 80 (weight 30%), Final: 70 (weight 50%)", 71.0, "0.20*60 + 0.30*80 + 0.50*70 = 12 + 24 + 35 = 71"),
            ("Continuous: 85 (weight 50%), End-sem: 75 (weight 50%)", 80.0, "0.50*85 + 0.50*75 = 42.5 + 37.5 = 80")
        ],
        'tmpls': [
            "A student's grades and component weightages are: {0}. Calculate the student's overall weighted course grade:",
            "Determine the final weighted score for a student with: {0}:",
            "Calculate the composite mark given: {0}:",
            "What is the overall average grade for: {0}?",
            "Evaluate the weighted course score for: {0}:",
            "Find the final weighted grade: {0}:",
            "Compute the composite percentage: {0}:",
            "From the weighted grading scheme: {0}, calculate the final mark:",
            "Solve the weighted grading problem: {0}:",
            "Determine the final grade based on weights: {0}:"
        ],
        'calc': lambda item: (
            f"{int(item[1]) if isinstance(item[1], float) and item[1].is_integer() else item[1]}",
            [f"{float(item[1]) + 5:.1f}", f"{float(item[1]) - 4:.1f}", f"{float(item[1]) + 8:.1f}"],
            f"**Step 1: Multiply each score by its percentage weight (or decimal weight).**\n\n**Step 2: Sum the weighted components.**\n\\[ {item[2]} \\]\n\n**Step 3: State the answer.**\nThe final weighted grade is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Combined Mean of Two Groups (n1 x1 + n2 x2) / (n1 + n2)
    arch2 = {
        'data': [
            ("Section A (30 students, mean 60) and Section B (20 students, mean 70)", 30, 60, 20, 70, 64.0, "(30*60 + 20*70)/(30+20) = (1800+1400)/50 = 3200/50 = 64"),
            ("Boys (25, mean height 160 cm) and Girls (25, mean height 150 cm)", 25, 160, 25, 150, 155.0, "(25*160 + 25*150)/50 = 155"),
            ("Class 9A (40 students, mean 75) and Class 9B (60 students, mean 65)", 40, 75, 60, 65, 69.0, "(40*75 + 60*65)/100 = (3000+3900)/100 = 69"),
            ("Group 1 (15 workers, mean wage ₹300) and Group 2 (10 workers, mean wage ₹400)", 15, 300, 10, 400, 340.0, "(15*300 + 10*400)/25 = (4500+4000)/25 = 8500/25 = 340"),
            ("Batch 1 (50 items, mean weight 40 g) and Batch 2 (50 items, mean weight 60 g)", 50, 40, 50, 60, 50.0, "(50*40 + 50*60)/100 = 50"),
            ("Team A (6 players, mean score 20) and Team B (4 players, mean score 30)", 6, 20, 4, 30, 24.0, "(6*20 + 4*30)/10 = (120+120)/10 = 24"),
            ("Factory Day shift (100 workers, mean output 50) and Night shift (50 workers, mean output 44)", 100, 50, 50, 44, 48.0, "(100*50 + 50*44)/150 = (5000+2200)/150 = 7200/150 = 48"),
            ("Morning batch (20 students, mean 85) and Evening batch (30 students, mean 75)", 20, 85, 30, 75, 79.0, "(20*85 + 30*75)/50 = (1700+2250)/50 = 3950/50 = 79"),
            ("Urban group (80 people, mean age 35) and Rural group (20 people, mean age 45)", 80, 35, 20, 45, 37.0, "(80*35 + 20*45)/100 = (2800+900)/100 = 37"),
            ("Junior group (10 kids, mean 12) and Senior group (10 kids, mean 18)", 10, 12, 10, 18, 15.0, "(10*12 + 10*18)/20 = 15")
        ],
        'tmpls': [
            "Find the combined mean of the two groups: {0}:",
            "Calculate the overall combined mean for: {0}:",
            "What is the combined average of the combined sample: {0}?",
            "Using \\( \\bar{{X}}_{{12}} = \\frac{{n_1 \\bar{{X}}_1 + n_2 \\bar{{X}}_2}}{{n_1 + n_2}} \\), evaluate for {0}:",
            "Determine the combined mean for: {0}:",
            "Compute the total weighted mean of both groups: {0}:",
            "Find the pooled mean for: {0}:",
            "What is the combined mean score of: {0}?",
            "Calculate the pooled average for: {0}:",
            "Determine the combined mean of: {0}:"
        ],
        'calc': lambda item: (
            f"{int(item[5]) if isinstance(item[5], float) and item[5].is_integer() else item[5]}",
            [f"{float(item[5]) + 4:.1f}", f"{float(item[5]) - 3:.1f}", f"{float(item[5]) + 10:.1f}"],
            f"**Step 1: Write down the combined mean formula.**\n\\[ \\bar{{X}}_{{12}} = \\frac{{n_1 \\bar{{X}}_1 + n_2 \\bar{{X}}_2}}{{n_1 + n_2}} \\]\n\n**Step 2: Substitute the group values.**\n\\[ {item[6]} \\]\n\n**Step 3: State the answer.**\nThe combined mean is {int(item[5]) if isinstance(item[5], float) and item[5].is_integer() else item[5]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Mixing Solutions of Different Concentrations (Alligation / Mixing Proportions)
    arch3 = {
        'data': [
            (2, 20, 3, 30, 26.0, "(2*20 + 3*30)/(2+3) = (40+90)/5 = 130/5 = 26%"),
            (1, 10, 3, 50, 40.0, "(1*10 + 3*50)/(1+3) = (10+150)/4 = 160/4 = 40%"),
            (4, 15, 6, 25, 21.0, "(4*15 + 6*25)/(4+6) = (60+150)/10 = 210/10 = 21%"),
            (5, 40, 5, 60, 50.0, "(5*40 + 5*60)/10 = 50%"),
            (3, 10, 2, 60, 30.0, "(3*10 + 2*60)/(3+2) = (30+120)/5 = 150/5 = 30%"),
            (1, 80, 4, 30, 40.0, "(1*80 + 4*30)/(1+4) = (80+120)/5 = 200/5 = 40%"),
            (2, 50, 8, 20, 26.0, "(2*50 + 8*20)/10 = (100+160)/10 = 26%"),
            (3, 25, 7, 45, 39.0, "(3*25 + 7*45)/10 = (75+315)/10 = 39%"),
            (4, 70, 1, 20, 60.0, "(4*70 + 1*20)/5 = (280+20)/5 = 300/5 = 60%"),
            (6, 30, 4, 80, 50.0, "(6*30 + 4*80)/10 = (180+320)/10 = 50%")
        ],
        'tmpls': [
            "If {0} litres of {1}% acid solution is mixed with {2} litres of {3}% acid solution, what is the concentration of the resulting mixture?",
            "A chemist mixes {0} L of {1}% salt solution with {2} L of {3}% salt solution. What is the percentage concentration of the mix?",
            "Calculate the concentration when {0} units of a {1}% solution are blended with {2} units of a {3}% solution:",
            "What is the final concentration of a mixture formed by combining {0} L at {1}% and {2} L at {3}%?",
            "Find the percentage of acid in the mixture of {0} litres at {1}% and {2} litres at {3}%:",
            "Determine the resulting concentration of: {0} L of {1}% + {2} L of {3}%:",
            "Compute the mixture percentage for: {0} kg ({1}%) mixed with {2} kg ({3}%):",
            "What concentration results from blending {0} L of {1}% concentration with {2} L of {3}%?",
            "Evaluate the combined concentration: {0} parts at {1}% and {2} parts at {3}%:",
            "Calculate the mixture proportion: {0} L ({1}%) and {2} L ({3}%):"
        ],
        'calc': lambda item: (
            f"{int(item[4]) if isinstance(item[4], float) and item[4].is_integer() else item[4]}%",
            [f"{float(item[4]) + 5:.1f}%", f"{float(item[4]) - 5:.1f}%", f"{float(item[4]) + 10:.1f}%"],
            f"**Step 1: Write down the weighted mixture formula.**\n\\[ C_{{\\text{{mix}}}} = \\frac{{V_1 C_1 + V_2 C_2}}{{V_1 + V_2}} \\]\n\n**Step 2: Substitute the volumes and concentrations.**\n\\[ C_{{\\text{{mix}}}} = {item[5]} \\]\n\n**Step 3: State the answer.**\nThe resulting concentration is {int(item[4]) if isinstance(item[4], float) and item[4].is_integer() else item[4]}%."
        ),
        'diff': 'medium'
    }

    # Arch 4: Average price per unit (Commodity mixtures)
    arch4 = {
        'data': [
            (5, 40, 3, 60, 47.5, "(5*40 + 3*60)/(5+3) = (200+180)/8 = 380/8 = ₹47.50"),
            (4, 50, 6, 75, 65.0, "(4*50 + 6*75)/(4+6) = (200+450)/10 = 650/10 = ₹65.00"),
            (10, 30, 15, 50, 42.0, "(10*30 + 15*50)/(10+15) = (300+750)/25 = 1050/25 = ₹42.00"),
            (2, 100, 3, 150, 130.0, "(2*100 + 3*150)/5 = (200+450)/5 = 650/5 = ₹130.00"),
            (8, 25, 12, 35, 31.0, "(8*25 + 12*35)/20 = (200+420)/20 = 620/20 = ₹31.00"),
            (3, 80, 2, 120, 96.0, "(3*80 + 2*120)/5 = (240+240)/5 = 480/5 = ₹96.00"),
            (6, 45, 4, 70, 55.0, "(6*45 + 4*70)/10 = (270+280)/10 = 550/10 = ₹55.00"),
            (5, 60, 5, 80, 70.0, "(5*60 + 5*80)/10 = ₹70.00"),
            (7, 30, 3, 50, 36.0, "(7*30 + 3*50)/10 = (210+150)/10 = 360/10 = ₹36.00"),
            (1, 150, 4, 200, 190.0, "(1*150 + 4*200)/5 = (150+800)/5 = 950/5 = ₹190.00")
        ],
        'tmpls': [
            "A merchant mixes {0} kg of rice at ₹{1}/kg with {2} kg of rice at ₹{3}/kg. What is the average price per kg of the mixture?",
            "A grocer buys {0} kg of tea at ₹{1}/kg and {2} kg at ₹{3}/kg. What is the weighted average cost per kg?",
            "Calculate the average cost per unit if {0} units are bought at ₹{1} and {2} units at ₹{3}:",
            "What is the blended price per kg when {0} kg costing ₹{1}/kg is mixed with {2} kg costing ₹{3}/kg?",
            "Find the cost per kg of the blended mixture: {0} kg at ₹{1} + {2} kg at ₹{3}:",
            "Determine the average unit price for {0} items at ₹{1} each and {2} items at ₹{3} each:",
            "Compute the average price per kg of the mixture: {0} kg @ ₹{1} and {2} kg @ ₹{3}:",
            "What is the price per kg of the composite product: {0} kg (₹{1}) and {2} kg (₹{3})?",
            "Evaluate the weighted average price: {0} kg at ₹{1} and {2} kg at ₹{3}:",
            "Calculate the mean price per kg: {0} kg at ₹{1}/kg and {2} kg at ₹{3}/kg:"
        ],
        'calc': lambda item: (
            f"₹{item[4]:.2f}",
            [f"₹{item[4] + 5:.2f}", f"₹{item[4] - 4:.2f}", f"₹{item[4] + 10:.2f}"],
            f"**Step 1: Compute total expenditure.**\nTotal Cost = \\( {item[0]} \\times {item[1]} + {item[2]} \\times {item[3]} \\).\n\n**Step 2: Divide by total quantity.**\nTotal Weight = \\( {item[0]} + {item[2]} \\).\n\\[ \\text{{Average Price}} = {item[5]} \\]\n\n**Step 3: State the answer.**\nThe average price per kg is ₹{item[4]:.2f}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Correcting erroneous mean (Data Entry Error correction)
    arch5 = {
        'data': [
            (20, 45, 54, 34, 44.0, "Old Sum = 20*45 = 900; Correct Sum = 900 - 54 + 34 = 880; Correct Mean = 880/20 = 44"),
            (10, 50, 70, 50, 48.0, "Old Sum = 10*50 = 500; Correct Sum = 500 - 70 + 50 = 480; Correct Mean = 480/10 = 48"),
            (25, 60, 40, 65, 61.0, "Old Sum = 25*60 = 1500; Correct Sum = 1500 - 40 + 65 = 1525; Correct Mean = 1525/25 = 61"),
            (40, 30, 25, 65, 31.0, "Old Sum = 40*30 = 1200; Correct Sum = 1200 - 25 + 65 = 1240; Correct Mean = 1240/40 = 31"),
            (50, 80, 92, 42, 79.0, "Old Sum = 50*80 = 4000; Correct Sum = 4000 - 92 + 42 = 3950; Correct Mean = 3950/50 = 79"),
            (15, 35, 60, 30, 33.0, "Old Sum = 15*35 = 525; Correct Sum = 525 - 60 + 30 = 495; Correct Mean = 495/15 = 33"),
            (30, 40, 15, 45, 41.0, "Old Sum = 30*40 = 1200; Correct Sum = 1200 - 15 + 45 = 1230; Correct Mean = 1230/30 = 41"),
            (100, 55, 83, 53, 54.7, "Old Sum = 100*55 = 5500; Correct Sum = 5500 - 83 + 53 = 5470; Correct Mean = 5470/100 = 54.7"),
            (20, 25, 40, 20, 24.0, "Old Sum = 20*25 = 500; Correct Sum = 500 - 40 + 20 = 480; Correct Mean = 480/20 = 24"),
            (50, 75, 50, 100, 76.0, "Old Sum = 50*75 = 3750; Correct Sum = 3750 - 50 + 100 = 3800; Correct Mean = 3800/50 = 76")
        ],
        'tmpls': [
            "The mean of {0} numbers was found to be {1}. Later, it was discovered that one observation was misread as {2} instead of {3}. Find the correct mean:",
            "The average score of {0} students was calculated as {1}. It was then detected that a score of {3} was wrongly entered as {2}. What is the correct average?",
            "For {0} observations, mean = {1}. If an item {2} was wrongly included instead of {3}, calculate the correct mean:",
            "Find the corrected mean: n = {0}, calculated mean = {1}, wrong value = {2}, correct value = {3}:",
            "Correct the arithmetic mean: {0} values with mean {1}, where {2} should be replaced by {3}:",
            "What is the true mean of {0} observations calculated as {1} if {2} was recorded in place of {3}?",
            "Recompute the mean for {0} items (mean = {1}) when error {2} is replaced with {3}:",
            "Calculate the corrected average: n = {0}, mean = {1}, incorrect = {2}, correct = {3}:",
            "Determine the actual mean of {0} scores having mean {1} after correcting {2} to {3}:",
            "Solve the data correction problem: n = {0}, mean = {1}, wrong = {2}, correct = {3}:"
        ],
        'calc': lambda item: (
            f"{int(item[4]) if isinstance(item[4], float) and item[4].is_integer() else item[4]}",
            [f"{float(item[4]) + 2:.1f}", f"{float(item[4]) - 2:.1f}", f"{float(item[4]) + 5:.1f}"],
            f"**Step 1: Compute the incorrect total sum.**\n\\[ \\text{{Old Sum}} = n \\times \\bar{{x}}_{{\\text{{old}}}} = {item[0]} \\times {item[1]} = {item[0] * item[1]} \\]\n\n**Step 2: Correct the sum by subtracting the wrong value and adding the correct value.**\n\\[ \\text{{Correct Sum}} = \\text{{Old Sum}} - {item[2]} + {item[3]} \\]\n\n**Step 3: Divide by \\( n = {item[0]} \\) to find the correct mean.**\n{item[5]}.\n\nThe correct mean is {int(item[4]) if isinstance(item[4], float) and item[4].is_integer() else item[4]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Grade Point Average (GPA / Credit hours) as Weighted Mean
    arch6 = {
        'data': [
            ("Math: 4 credits (Grade 9), Physics: 3 credits (Grade 8), English: 2 credits (Grade 7)", 4, 9, 3, 8, 2, 7, 8.22, "(4*9 + 3*8 + 2*7)/(4+3+2) = (36+24+14)/9 = 74/9 ≈ 8.22"),
            ("Course A: 3 credits (Grade 10), Course B: 3 credits (Grade 8), Course C: 4 credits (Grade 7)", 3, 10, 3, 8, 4, 7, 8.0, "(30+24+28)/10 = 82/10 = 8.2"),
            ("Subject 1: 4 credits (Grade 8), Subject 2: 4 credits (Grade 6), Subject 3: 2 credits (Grade 10)", 4, 8, 4, 6, 2, 10, 7.6, "(32+24+20)/10 = 76/10 = 7.6"),
            ("Major: 5 credits (Grade 9), Minor: 3 credits (Grade 7), Elective: 2 credits (Grade 8)", 5, 9, 3, 7, 2, 8, 8.2, "(45+21+16)/10 = 82/10 = 8.2"),
            ("Lab 1: 2 credits (Grade 10), Theory 1: 3 credits (Grade 8), Theory 2: 3 credits (Grade 6)", 2, 10, 3, 8, 3, 6, 7.75, "(20+24+18)/8 = 62/8 = 7.75"),
            ("Science: 4 credits (Grade 8), Social: 3 credits (Grade 9), Hindi: 3 credits (Grade 8)", 4, 8, 3, 9, 3, 8, 8.3, "(32+27+24)/10 = 83/10 = 8.3"),
            ("Math: 5 credits (Grade 10), Bio: 3 credits (Grade 6), Chem: 2 credits (Grade 8)", 5, 10, 3, 6, 2, 8, 8.4, "(50+18+16)/10 = 84/10 = 8.4"),
            ("Paper 1: 3 credits (Grade 7), Paper 2: 3 credits (Grade 9), Paper 3: 4 credits (Grade 8)", 3, 7, 3, 9, 4, 8, 8.0, "(21+27+32)/10 = 80/10 = 8.0"),
            ("Core 1: 4 credits (Grade 9), Core 2: 4 credits (Grade 9), Skill: 2 credits (Grade 7)", 4, 9, 4, 9, 2, 7, 8.6, "(36+36+14)/10 = 86/10 = 8.6"),
            ("Project: 6 credits (Grade 9), Seminar: 4 credits (Grade 7)", 6, 9, 4, 7, 0, 0, 8.2, "(54+28)/10 = 82/10 = 8.2")
        ],
        'tmpls': [
            "Calculate the Grade Point Average (GPA) using weighted mean for: {0}:",
            "What is the credit-weighted GPA for a student with: {0}?",
            "Compute the GPA from the course credits and grades: {0}:",
            "Determine the student's weighted GPA: {0}:",
            "Evaluate the cumulative GPA for: {0}:",
            "Find the weighted average grade point: {0}:",
            "Calculate the weighted score for credit allocation: {0}:",
            "From the academic transcript: {0}, calculate GPA:",
            "Solve the credit-weighted grade problem: {0}:",
            "Determine the composite grade: {0}:"
        ],
        'calc': lambda item: (
            f"{item[7]:.2f}",
            [f"{item[7] + 0.5:.2f}", f"{item[7] - 0.4:.2f}", f"{item[7] + 1.0:.2f}"],
            f"**Step 1: Multiply each grade point by its credit hours.**\n\n**Step 2: Sum credit-points and divide by total credits.**\n\\[ \\text{{GPA}} = \\frac{{\\sum (\\text{{Credit}} \\times \\text{{Grade}})}}{{\\sum \\text{{Credits}}}} \\]\n{item[8]}.\n\n**Step 3: State the answer.**\nThe GPA is {item[7]:.2f}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Foundational Invariants of Weighted Means
    arch7 = {
        'data': [
            ("If all weights wi in a weighted mean are equal (e.g. w1 = w2 = ... = wn = 1), what does the weighted mean become?", "The Simple Arithmetic Mean \\( \\bar{x} = \\frac{\\sum x_i}{n} \\)", "Equal weights yield simple mean"),
            ("Can the weighted mean of a set of numbers ever be greater than the maximum number in the set?", "No, the weighted mean must strictly lie between the minimum and maximum values: min(xi) <= x̄w <= max(xi)", "Boundedness invariant"),
            ("Can the weighted mean ever be less than the minimum number in the set?", "No, it is strictly bounded below by the minimum observation", "Boundedness invariant"),
            ("If all component numbers xi are multiplied by a constant k, what happens to the weighted mean?", "The weighted mean is multiplied by k", "Homogeneity of degree 1"),
            ("If all weights wi are multiplied by a constant c (c > 0), what happens to the weighted mean?", "The weighted mean remains COMPLETELY UNCHANGED (scale invariance of weights)", "Ratio c cancels out in numerator and denominator"),
            ("Why is the simple arithmetic mean sometimes called a 'special case' of the weighted mean?", "Because it is simply the weighted mean where every observation has an identical weight of 1", "Special case with w_i = 1"),
            ("In combining two groups, if Group 1 has 3 times as many members as Group 2 (n1 = 3n2), where does the combined mean lie?", "It lies 3 times closer to the mean of Group 1 than to the mean of Group 2", "Inverse distance weighting / center of mass"),
            ("What physical principle is mathematically identical to the weighted arithmetic mean?", "The Center of Mass (Center of Gravity) of point masses placed on a line", "Center of mass analogy: x_cm = sum m_i x_i / sum m_i"),
            ("If a student scores 60 on an exam with weight 1 and 80 on an exam with weight 3, which score has more influence on the final result?", "The score 80 has 3 times more influence than the score 60", "Weight reflects proportional influence"),
            ("What is the sum of the weighted deviations \\( \\sum w_i (x_i - \\bar{x}_w) \\)?", "Always equal to 0", "Weighted balance point property")
        ],
        'tmpls': [
            "{0}",
            "In the mathematical theory of weighted averages: {0}",
            "Analyze the invariant property of weighted means: {0}",
            "Identify the foundational principle: {0}",
            "Which statement correctly characterizes: {0}?",
            "What is the mathematical consequence: {0}?",
            "Determine the accurate answer: {0}",
            "In NCERT Class 9 statistics and data analysis: {0}",
            "Select the accurate insight: {0}",
            "Evaluate the weighted mean property: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The weighted mean is multiplied by c^2",
                "It can exceed the maximum number if weights are large",
                "Weighted mean is always equal to the median"
            ],
            f"**Step 1: Review the foundational properties of the weighted mean.**\n\\( \\bar{{x}}_w = \\frac{{\\sum w_i x_i}}{{\\sum w_i}} \\).\n\n**Step 2: Apply the property.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_10_3_1()
    q2 = gen_10_3_2()
    print(f"gen_10_3_1: {len(q1)} questions")
    print(f"gen_10_3_2: {len(q2)} questions")
