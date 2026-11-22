# scripts/build_clean_mth1_ch7_part2.py
# Generator for Chapter 7: Statistics (Subtopics 7.2.2, 7.3.1, 7.3.2, 7.3.3 = 320 Questions)
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from engine_algebra import generate_subtopic

CH_NUM = 7
CH_NAME = "Statistics"

def build_part2():
    with open('scripts/mh9_mth1_ch7_temp.json', 'r', encoding='utf-8') as f:
        all_qs = json.load(f)

    # -------------------------------------------------------------------------
    # 7.2.2: Frequency interpretation
    # -------------------------------------------------------------------------
    tc_722 = "MH-9-MTH1-7-7.2.2"
    tn_722 = "Frequency interpretation"
    archs_722 = []

    # Arch 0: Identifying the Modal Class (class with highest frequency)
    archs_722.append({
        'data': [
            ("0-10: 4, 10-20: 9, 20-30: 18, 30-40: 12, 40-50: 7", "20-30 (highest frequency = 18)"),
            ("10-20: 5, 20-30: 14, 30-40: 22, 40-50: 11, 50-60: 8", "30-40 (highest frequency = 22)"),
            ("0-15: 8, 15-30: 16, 30-45: 25, 45-60: 13, 60-75: 6", "30-45 (highest frequency = 25)"),
            ("20-30: 7, 30-40: 15, 40-50: 19, 50-60: 10, 60-70: 5", "40-50 (highest frequency = 19)"),
            ("0-20: 6, 20-40: 11, 40-60: 24, 60-80: 14, 80-100: 5", "40-60 (highest frequency = 24)"),
            ("10-25: 9, 25-40: 21, 40-55: 15, 55-70: 8", "25-40 (highest frequency = 21)"),
            ("50-60: 10, 60-70: 28, 70-80: 17, 80-90: 9", "60-70 (highest frequency = 28)"),
            ("0-10: 3, 10-20: 8, 20-30: 12, 30-40: 20, 40-50: 7", "30-40 (highest frequency = 20)"),
            ("25-35: 6, 35-45: 18, 45-55: 11, 55-65: 5", "35-45 (highest frequency = 18)"),
            ("0-25: 7, 25-50: 19, 50-75: 32, 75-100: 14", "50-75 (highest frequency = 32)")
        ],
        'tmpls': [
            "In the grouped frequency distribution: {0}, which class interval is the Modal Class?",
            "Identify the modal class interval from the distribution: {0}:",
            "What is the modal class for the grouped data: {0}?",
            "Find the modal class in the frequency table: {0}:",
            "Determine the modal class interval given the data: {0}:",
            "Which class interval corresponds to the modal class in: {0}?",
            "For the frequency distribution: {0}, specify the modal class:",
            "Identify the interval with highest frequency (modal class) in: {0}:",
            "What is the modal class of the distribution: {0}?",
            "Find the modal class interval from the frequencies: {0}:"
        ],
        'calc': lambda item: (
            item[1],
            ["0-10 (first class)", "40-50 (last class)", "Class with lowest frequency"],
            f"Step 1: Modal class is the class interval possessing the highest frequency in the distribution.\nStep 2: Inspect frequencies: {item[0]}.\nStep 3: Result: {item[1]}."
        ),
        'diff': 'easy'
    })

    # Arch 1: Identifying the Median Class (class where cumulative frequency >= N/2)
    archs_722.append({
        'data': [
            ("0-10: 4, 10-20: 8, 20-30: 14, 30-40: 10, 40-50: 4 (Total N = 40)", "20-30 (N/2 = 20; cumulative frequency of 20-30 is 26 >= 20)"),
            ("10-20: 6, 20-30: 12, 30-40: 18, 40-50: 10, 50-60: 4 (Total N = 50)", "30-40 (N/2 = 25; cumulative frequency of 30-40 is 36 >= 25)"),
            ("0-20: 5, 20-40: 11, 40-60: 15, 60-80: 9 (Total N = 40)", "40-60 (N/2 = 20; cumulative frequency of 40-60 is 31 >= 20)"),
            ("10-25: 7, 25-40: 13, 40-55: 16, 55-70: 8 (Total N = 44)", "40-55 (N/2 = 22; cumulative frequency of 40-55 is 36 >= 22)"),
            ("0-15: 4, 15-30: 9, 30-45: 17, 45-60: 10 (Total N = 40)", "30-45 (N/2 = 20; cumulative frequency of 30-45 is 30 >= 20)"),
            ("20-30: 8, 30-40: 14, 40-50: 20, 50-60: 8 (Total N = 50)", "40-50 (N/2 = 25; cumulative frequency of 40-50 is 42 >= 25)"),
            ("0-10: 5, 10-20: 11, 20-30: 19, 30-40: 15 (Total N = 50)", "20-30 (N/2 = 25; cumulative frequency of 20-30 is 35 >= 25)"),
            ("25-35: 6, 35-45: 12, 45-55: 18, 55-65: 14 (Total N = 50)", "45-55 (N/2 = 25; cumulative frequency of 45-55 is 36 >= 25)"),
            ("50-60: 7, 60-70: 15, 70-80: 22, 80-90: 16 (Total N = 60)", "70-80 (N/2 = 30; cumulative frequency of 70-80 is 44 >= 30)"),
            ("0-25: 8, 25-50: 17, 50-75: 25, 75-100: 10 (Total N = 60)", "50-75 (N/2 = 30; cumulative frequency of 50-75 is 50 >= 30)")
        ],
        'tmpls': [
            "For the distribution: {0}, determine the Median Class:",
            "Find the median class interval for the grouped data: {0}:",
            "What is the median class of the frequency table: {0}?",
            "Identify the median class in the distribution: {0}:",
            "Compute the median class interval from: {0}:",
            "Which class interval serves as the median class in: {0}?",
            "For the grouped observations: {0}, locate the median class:",
            "Determine which interval is the median class in: {0}:",
            "Find the median class for the data set: {0}:",
            "Evaluate the distribution: {0} to find the median class:"
        ],
        'calc': lambda item: (
            item[1],
            ["Class with highest frequency (Modal class)", "The very first class interval", "The very last class interval"],
            f"Step 1: Compute total frequency N and find N/2.\nStep 2: Identify the class whose cumulative frequency is just greater than or equal to N/2.\nStep 3: Result: {item[1]}."
        ),
        'diff': 'medium'
    })

    # Arch 2: Relative Frequency calculation (Frequency / Total Frequency N)
    archs_722.append({
        'data': [
            (10, 50, "0.20 (or 20%)"), (12, 60, "0.20 (or 20%)"),
            (15, 50, "0.30 (or 30%)"), (8, 40, "0.20 (or 20%)"),
            (14, 70, "0.20 (or 20%)"), (20, 80, "0.25 (or 25%)"),
            (18, 90, "0.20 (or 20%)"), (25, 100, "0.25 (or 25%)"),
            (16, 80, "0.20 (or 20%)"), (21, 70, "0.30 (or 30%)")
        ],
        'tmpls': [
            "In a statistical sample of total size N = {1}, a class interval has frequency f = {0}. What is its Relative Frequency?",
            "Calculate the relative frequency of a class with frequency {0} in a total distribution of {1} observations:",
            "If a class has frequency f = {0} out of total N = {1}, find its relative frequency:",
            "Determine the relative frequency for f = {0} and N = {1}:",
            "What is the proportion of total observations (relative frequency) for f = {0} when N = {1}?",
            "Compute the relative frequency for a class frequency of {0} out of total {1}:",
            "Find the relative frequency value when class frequency is {0} and total frequency is {1}:",
            "For frequency f = {0} in a sample of N = {1}, what is the relative frequency?",
            "Calculate relative frequency for f = {0} with total N = {1}:",
            "Determine relative frequency of an interval with f = {0} out of N = {1}:"
        ],
        'calc': lambda item: (
            item[2],
            [f"{(item[0]/item[1]) + 0.15:.2f}", f"{(item[0]/item[1]) - 0.08:.2f}", f"{item[0] / 100:.2f}"],
            f"Step 1: Formula: Relative Frequency = Class Frequency f / Total Frequency N.\nStep 2: Calculate: {item[0]} / {item[1]} = {item[0]/item[1]:.2f}.\nStep 3: Relative Frequency = {item[2]}."
        ),
        'diff': 'easy'
    })

    # Arch 3: Frequency Density calculation (Frequency / Class Width)
    archs_722.append({
        'data': [
            (20, 10), (15, 5), (30, 10), (25, 5), (40, 20),
            (18, 6), (24, 8), (35, 7), (50, 25), (28, 14)
        ],
        'tmpls': [
            "In a histogram with unequal class widths, a class has frequency {0} and class width {1}. Calculate its Frequency Density:",
            "Find the frequency density of a class interval having frequency f = {0} and width h = {1}:",
            "What is the frequency density for a class of frequency {0} and length {1}?",
            "Calculate frequency density (f / h) for a class with frequency {0} and size {1}:",
            "Determine the frequency density when frequency is {0} and class width is {1}:",
            "Compute the frequency density for class frequency = {0} and interval width = {1}:",
            "In drawing a histogram with varying widths, find frequency density for f = {0}, width = {1}:",
            "What is the height of the rectangle (frequency density) for frequency {0} and width {1}?",
            "Find the frequency per unit width (frequency density) for f = {0} and h = {1}:",
            "Calculate frequency density of an interval with f = {0} and width = {1}:"
        ],
        'calc': lambda item: (
            f"{item[0] // item[1]}",
            [f"{(item[0] // item[1]) + 2}", f"{(item[0] // item[1]) - 1}", f"{item[0] * item[1]}"],
            f"Step 1: Formula: Frequency Density = Class Frequency / Class Width.\nStep 2: Divide: {item[0]} / {item[1]}.\nStep 3: Frequency Density = {item[0] // item[1]}."
        ),
        'diff': 'medium'
    })

    # Arch 4: Percentage Frequency calculation ( (f / N) * 100 )
    archs_722.append({
        'data': [
            (12, 50), (15, 60), (18, 72), (20, 80), (10, 40),
            (25, 100), (14, 70), (16, 80), (22, 110), (24, 120)
        ],
        'tmpls': [
            "A class interval has a frequency of {0} out of a total frequency of {1}. What is the percentage frequency?",
            "Calculate percentage frequency for a class with f = {0} and total N = {1}:",
            "Find the percentage of observations falling in a class having frequency {0} among {1} total data points:",
            "What percent of the distribution is represented by a class with frequency {0} out of {1}?",
            "Determine the percentage frequency for f = {0} when N = {1}:",
            "Compute the percentage share of a class possessing frequency {0} in total N = {1}:",
            "For a class frequency {0} out of total sample {1}, calculate percentage frequency:",
            "Find the percentage frequency corresponding to f = {0} and N = {1}:",
            "What is the percentage frequency of an interval with f = {0} out of total N = {1}?",
            "Calculate the percentage frequency value for f = {0} in a distribution of {1}:"
        ],
        'calc': lambda item: (
            f"{(item[0] * 100) // item[1]}%",
            [f"{((item[0] * 100) // item[1]) + 5}%", f"{((item[0] * 100) // item[1]) - 4}%", f"{((item[0] * 100) // item[1]) + 15}%"],
            f"Step 1: Formula: Percentage Frequency = (Class Frequency f / Total N) * 100.\nStep 2: Calculate: ({item[0]} / {item[1]}) * 100.\nStep 3: Result: {(item[0] * 100) // item[1]}%."
        ),
        'diff': 'easy'
    })

    # Arch 5: Interpretation of Central Angles in a Pie Chart (Angle = (f / N) * 360°)
    archs_722.append({
        'data': [
            (10, 40), (15, 60), (20, 80), (25, 100), (12, 72),
            (18, 90), (30, 120), (16, 80), (14, 70), (24, 120)
        ],
        'tmpls': [
            "In a pie diagram, a sector represents a category with frequency {0} out of total {1}. What is the central angle of this sector?",
            "Calculate the central angle of the sector for frequency f = {0} in a total frequency N = {1}:",
            "Find the central angle in degrees representing a component with frequency {0} out of total {1}:",
            "What central angle should be drawn in a pie chart for a component of value {0} when total is {1}?",
            "Determine the sector angle for a frequency of {0} out of a total distribution of {1}:",
            "Compute the central angle for f = {0} and N = {1} in pie chart representation:",
            "For a pie chart with total frequency {1}, find the angle corresponding to category count {0}:",
            "Calculate the measure of the central angle for a sub-group of {0} out of total {1}:",
            "Find the central angle in a pie chart for a frequency of {0} out of {1}:",
            "What is the sector central angle representing {0} units out of total {1} units?"
        ],
        'calc': lambda item: (
            f"{(item[0] * 360) // item[1]}°",
            [f"{((item[0] * 360) // item[1]) + 20}°", f"{((item[0] * 360) // item[1]) - 15}°", f"{(item[0] * 100) // item[1]}° (percentage)"],
            f"Step 1: Formula: Central Angle θ = (Component Value / Total Value) * 360°.\nStep 2: Calculate: ({item[0]} / {item[1]}) * 360°.\nStep 3: Central Angle = {(item[0] * 360) // item[1]}°."
        ),
        'diff': 'medium'
    })

    # Arch 6: Reading observations above or below a certain limit from a table
    archs_722.append({
        'data': [
            ("0-10: 5, 10-20: 12, 20-30: 18, 30-40: 11, 40-50: 4", 20, 33, "scored 20 marks or more"),
            ("0-15: 4, 15-30: 10, 30-45: 16, 45-60: 14, 60-75: 6", 30, 36, "scored 30 marks or more"),
            ("10-20: 6, 20-30: 14, 30-40: 20, 40-50: 12, 50-60: 8", 30, 40, "scored 30 or more"),
            ("0-20: 8, 20-40: 16, 40-60: 22, 60-80: 14", 40, 36, "scored 40 or more"),
            ("0-25: 7, 25-50: 15, 50-75: 24, 75-100: 14", 50, 38, "scored 50 or more"),
            ("10-25: 5, 25-40: 13, 40-55: 18, 55-70: 10", 40, 28, "scored 40 or more"),
            ("0-10: 3, 10-20: 8, 20-30: 15, 30-40: 18, 40-50: 6", 30, 24, "scored 30 or more"),
            ("20-30: 6, 30-40: 11, 40-50: 19, 50-60: 14", 40, 33, "scored 40 or more"),
            ("0-50: 12, 50-100: 28, 100-150: 34, 150-200: 16", 100, 50, "scored 100 or more"),
            ("0-20: 5, 20-40: 10, 40-60: 25, 60-80: 15, 80-100: 5", 40, 45, "scored 40 or more")
        ],
        'tmpls': [
            "In a test with score distribution: {0}. How many students {3}?",
            "From the frequency table: {0}, determine the number of students who {3}:",
            "Based on the distribution: {0}, calculate how many individuals {3}:",
            "Refer to the score distribution: {0}. Find the total number of students who {3}:",
            "Using the data: {0}, how many candidates {3}?",
            "From the table: {0}, compute the count of students who {3}:",
            "In the grouped test scores: {0}, find how many students {3}:",
            "Determine the number of students who {3} from: {0}:",
            "According to the distribution: {0}, how many students {3}?",
            "Find the count of students who {3} given: {0}:"
        ],
        'calc': lambda item: (
            f"{item[2]} students",
            [f"{item[2] + 6} students", f"{item[2] - 5} students", f"{item[2] + 14} students"],
            f"Step 1: '{item[3]}' requires summing frequencies of all classes with lower limits >= {item[1]}.\nStep 2: Add relevant class frequencies.\nStep 3: Result: {item[2]} students."
        ),
        'diff': 'medium'
    })

    # Arch 7: Conceptual rules of frequency distributions
    archs_722.append({
        'data': [
            ("What does the frequency of a class interval represent?", "The total number of observations falling within that specific class interval", ["The difference between lower and upper limits", "The square of the class mark", "The ratio of mean to standard deviation"]),
            ("What is the sum of all relative frequencies across all classes in a complete distribution?", "Exactly 1.0 (or 100% when expressed as percentage)", ["Exactly 0", "Equal to the range", "Equal to the mean"]),
            ("What is the sum of all central angles in a pie diagram?", "360°", ["180°", "100°", "90°"]),
            ("Can a frequency in a statistical frequency table ever be negative?", "No, frequencies represent counts of physical observations and must be non-negative integers (>= 0)", ["Yes, when observations are below zero", "Yes, in winter season datasets", "Yes, when profits are negative"]),
            ("What is an open-ended class interval?", "A class interval that lacks an explicit lower boundary (e.g. 'Below 20') or upper boundary (e.g. '80 and above')", ["A class interval with zero frequency", "A class interval with infinite width", "A class used only on internet websites"]),
            ("What problem arises when using open-ended classes in computing the arithmetic mean?", "The class mark (mid-point) cannot be determined without making arbitrary assumptions about boundaries", ["The frequency becomes negative", "Histograms cannot be displayed in textbooks", "The median cannot be determined"]),
            ("Which measure of central tendency can be easily determined even when a distribution has open-ended classes?", "Median and Mode (since they depend on position and highest frequency rather than all values)", ["Arithmetic Mean", "Standard Deviation", "Geometric Mean"]),
            ("What does a frequency of zero for a particular class interval indicate?", "No observation in the collected dataset fell within that specific interval range", ["The data was recorded incorrectly", "The class size is infinite", "The entire survey is invalid"]),
            ("What is a bi-modal frequency distribution?", "A distribution that contains two distinct peaks (two classes sharing the maximum frequency)", ["A distribution with two variables", "A distribution drawn in two different colors", "A distribution containing zero frequencies"]),
            ("Why is grouping raw data into class intervals advantageous?", "It condenses large unwieldy datasets into a manageable, comprehensible form revealing the overall pattern", ["It increases the total number of data points", "It makes all numbers equal to their average", "It eliminates all mathematical errors"])
        ],
        'tmpls': [
            "In frequency distribution theory: {0}",
            "Understanding frequency concepts: {0}",
            "Core principles of grouped data: {0}",
            "Evaluating distribution properties: {0}",
            "Key knowledge on statistical frequency: {0}",
            "Properties of frequency tables: {0}",
            "Statistical theory of data grouping: {0}",
            "Fundamentals of frequency analysis: {0}",
            "Theoretical rules of frequency tables: {0}",
            "Essential concepts of statistical frequency: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: In statistical science, {item[1]}."
        ),
        'diff': 'foundation'
    })

    qs_722 = generate_subtopic(tc_722, tn_722, CH_NUM, CH_NAME, archs_722)
    all_qs.extend(qs_722)
    print(f"Generated {len(qs_722)} for {tc_722}")

    # -------------------------------------------------------------------------
    # 7.3.1: Mean: X̄ = Σx / N and Σ(f*x) / N
    # -------------------------------------------------------------------------
    tc_731 = "MH-9-MTH1-7-7.3.1"
    tn_731 = "Mean: X̄ = Σx / N and Σ(f*x) / N"
    archs_731 = []

    # Arch 0: Mean of ungrouped raw data: Σx / N
    archs_731.append({
        'data': [
            ([12, 18, 14, 16, 20], 80, 5),
            ([25, 30, 35, 20, 40], 150, 5),
            ([8, 12, 15, 9, 16], 60, 5),
            ([42, 38, 45, 50, 35], 210, 5),
            ([10, 15, 20, 25, 30], 100, 5),
            ([14, 17, 21, 28, 10], 90, 5),
            ([32, 28, 40, 36, 24], 160, 5),
            ([55, 60, 45, 50, 65], 275, 5),
            ([7, 13, 19, 21, 15], 75, 5),
            ([18, 22, 26, 30, 24], 120, 5)
        ],
        'tmpls': [
            "Calculate the arithmetic mean of the raw observations: {0}:",
            "Find the mean (average) of the dataset: {0}:",
            "What is the arithmetic mean of the numbers: {0}?",
            "Compute the mean of the given values: {0}:",
            "Determine the mean for the observation set: {0}:",
            "Calculate the average (mean) of: {0}:",
            "Find the arithmetic mean for: {0}:",
            "For the numbers {0}, what is the mean?",
            "Compute the average value of: {0}:",
            "Identify the arithmetic mean of the scores: {0}:"
        ],
        'calc': lambda item: (
            f"{item[1] // item[2]}",
            [f"{(item[1] // item[2]) + 3}", f"{(item[1] // item[2]) - 2}", f"{(item[1] // item[2]) + 6}"],
            f"Step 1: Formula: Mean X̄ = (Sum of all observations Σx) / (Total number of observations N).\nStep 2: Σx = {' + '.join(str(x) for x in item[0])} = {item[1]}.\nStep 3: Mean = {item[1]} / {item[2]} = {item[1] // item[2]}."
        ),
        'diff': 'easy'
    })

    # Arch 1: Mean of raw data with decimal result
    archs_731.append({
        'data': [
            ([10, 12, 15, 18, 21, 24], 100, 6),
            ([5, 8, 12, 14, 17], 56, 5),
            ([20, 22, 25, 28], 95, 4),
            ([14, 16, 19, 22, 25], 96, 5),
            ([30, 32, 35, 38, 42], 177, 5),
            ([8, 11, 13, 17, 20], 69, 5),
            ([15, 18, 22, 26, 30], 111, 5),
            ([24, 28, 31, 35], 118, 4),
            ([12, 15, 18, 20, 23], 88, 5),
            ([40, 42, 45, 48, 51], 226, 5)
        ],
        'tmpls': [
            "Find the arithmetic mean of the observations: {0}:",
            "Calculate the mean value of the data: {0}:",
            "What is the mean of the scores: {0}?",
            "Determine the arithmetic mean for the set: {0}:",
            "Compute the mean of the numbers: {0}:",
            "For the observation list {0}, calculate the mean:",
            "What is the arithmetic average of: {0}?",
            "Find the mean of the numerical data: {0}:",
            "Compute the arithmetic mean of: {0}:",
            "Calculate the average for: {0}:"
        ],
        'calc': lambda item: (
            f"{item[1] / item[2]:.2f}",
            [f"{(item[1] / item[2]) + 1.5:.2f}", f"{(item[1] / item[2]) - 1.2:.2f}", f"{(item[1] / item[2]) + 3.0:.2f}"],
            f"Step 1: Formula: Mean X̄ = Σx / N.\nStep 2: Σx = {item[1]}, N = {item[2]}.\nStep 3: Mean = {item[1]} / {item[2]} = {item[1] / item[2]:.2f}."
        ),
        'diff': 'medium'
    })

    # Arch 2: Finding a missing observation given the mean
    archs_731.append({
        'data': [
            ([12, 15, 18, 20], 17, 5, "x"),
            ([24, 28, 30, 32], 29, 5, "k"),
            ([10, 14, 16, 22], 16, 5, "p"),
            ([35, 40, 45, 50], 43, 5, "y"),
            ([8, 12, 15, 19], 14, 5, "x"),
            ([20, 25, 30, 35], 28, 5, "a"),
            ([15, 18, 21, 24], 20, 5, "m"),
            ([30, 34, 38, 42], 37, 5, "x"),
            ([14, 17, 20, 23], 19, 5, "k"),
            ([45, 50, 55, 60], 53, 5, "z")
        ],
        'tmpls': [
            "The mean of five observations {0[0]}, {0[1]}, {0[2]}, {0[3]}, and {3} is {1}. Find the value of {3}:",
            "If the arithmetic mean of {0[0]}, {0[1]}, {0[2]}, {0[3]}, and {3} is {1}, calculate {3}:",
            "Given that the mean of the five numbers {0[0]}, {0[1]}, {0[2]}, {0[3]}, {3} is {1}, find {3}:",
            "Find the unknown value {3} if the mean of {0[0]}, {0[1]}, {0[2]}, {0[3]}, {3} equals {1}:",
            "Five scores are {0[0]}, {0[1]}, {0[2]}, {0[3]}, and {3}. If their average is {1}, determine {3}:",
            "What is the value of {3} when the mean of {0[0]}, {0[1]}, {0[2]}, {0[3]}, and {3} is {1}?",
            "Calculate {3} such that the arithmetic mean of {0[0]}, {0[1]}, {0[2]}, {0[3]}, {3} is {1}:",
            "Determine the missing observation {3} if the average of {0[0]}, {0[1]}, {0[2]}, {0[3]}, {3} is {1}:",
            "The average of observations {0[0]}, {0[1]}, {0[2]}, {0[3]}, and {3} is {1}. Compute {3}:",
            "Find {3} given that the mean of {0[0]}, {0[1]}, {0[2]}, {0[3]}, {3} is {1}:"
        ],
        'calc': lambda item: (
            f"{item[1] * item[2] - sum(item[0])}",
            [f"{item[1] * item[2] - sum(item[0]) + 4}", f"{item[1] * item[2] - sum(item[0]) - 3}", f"{item[1] * item[2] - sum(item[0]) + 8}"],
            f"Step 1: Formula: Sum of all observations = Mean * N = {item[1]} * {item[2]} = {item[1] * item[2]}.\nStep 2: Sum of known observations = {' + '.join(str(x) for x in item[0])} = {sum(item[0])}.\nStep 3: {item[3]} = Total Sum - Known Sum = {item[1] * item[2]} - {sum(item[0])} = {item[1] * item[2] - sum(item[0])}."
        ),
        'diff': 'medium'
    })

    # Arch 3: Mean of frequency distribution: Σ(f*x) / N (Direct method)
    archs_731.append({
        'data': [
            ([(2, 3), (4, 5), (6, 7), (8, 5)], 100, 20),
            ([(10, 4), (20, 6), (30, 8), (40, 2)], 480, 20),
            ([(5, 2), (15, 4), (25, 3), (35, 1)], 180, 10),
            ([(3, 4), (5, 6), (7, 5), (9, 5)], 122, 20),
            ([(12, 3), (14, 5), (16, 7), (18, 5)], 314, 20),
            ([(6, 5), (8, 7), (10, 5), (12, 3)], 172, 20),
            ([(20, 2), (30, 5), (40, 2), (50, 1)], 320, 10),
            ([(15, 3), (25, 4), (35, 2), (45, 1)], 260, 10),
            ([(4, 5), (6, 8), (8, 5), (10, 2)], 128, 20),
            ([(8, 4), (12, 6), (16, 8), (20, 2)], 272, 20)
        ],
        'tmpls': [
            "Calculate the mean X̄ = Σ(f*x) / Σf for the frequency distribution with (value, frequency) pairs: {0}:",
            "Find the mean for the discrete distribution: {0}:",
            "What is the arithmetic mean of the frequency table: {0}?",
            "Compute the mean using the direct method for data: {0}:",
            "Determine the mean value for the pairs (x, f): {0}:",
            "For the frequency distribution {0}, calculate the mean X̄:",
            "Calculate the arithmetic mean from the frequency table: {0}:",
            "Find the direct mean for the observations and frequencies: {0}:",
            "What is the average X̄ of the distribution given by: {0}?",
            "Compute the mean X̄ = Σfx / N for: {0}:"
        ],
        'calc': lambda item: (
            f"{item[1] / item[2]:g}",
            [f"{(item[1] / item[2]) + 1.5:g}", f"{(item[1] / item[2]) - 1.2:g}", f"{(item[1] / item[2]) + 3.0:g}"],
            f"Step 1: Compute Σ(f*x) and N = Σf.\nStep 2: Σ(f*x) = {item[1]}, N = {item[2]}.\nStep 3: Mean X̄ = {item[1]} / {item[2]} = {item[1] / item[2]:g}."
        ),
        'diff': 'medium'
    })

    # Arch 4: Effect of adding/subtracting a constant 'k' to all observations
    archs_731.append({
        'data': [
            (25, 5, "add 5"), (40, 8, "add 8"), (55, 10, "add 10"),
            (32, 4, "subtract 4"), (60, 7, "subtract 7"), (45, 5, "subtract 5"),
            (70, 12, "add 12"), (38, 6, "subtract 6"), (50, 9, "add 9"),
            (65, 15, "subtract 15")
        ],
        'tmpls': [
            "The mean of 20 observations is {0}. If we {2} to every observation, what is the new mean of the data?",
            "If the arithmetic mean of a dataset is {0} and we {2} to each observation, find the new mean:",
            "A distribution has mean = {0}. What will the new mean be if we {2} to all data values?",
            "Calculate the updated mean when we {2} to each observation of a dataset having mean {0}:",
            "Determine the new average if we {2} to every item in a distribution with initial mean {0}:",
            "What is the resulting mean if we {2} to each value in a dataset having mean {0}?",
            "For a set of observations with mean {0}, find the new mean after we {2} to every value:",
            "If initial mean is {0} and we {2} to all observations, compute the new mean:",
            "Find the new arithmetic mean when we {2} to each observation having original mean {0}:",
            "What happens to the mean {0} if we {2} to every observation in the series?"
        ],
        'calc': lambda item: (
            f"{item[0] + item[1] if 'add' in item[2] else item[0] - item[1]}",
            [f"{item[0]} (unchanged)", f"{item[0] + item[1] if 'subtract' in item[2] else item[0] - item[1]}", f"{item[0] * item[1]}"],
            f"Property of Mean: If a constant k is added to (or subtracted from) every observation, the mean increases (or decreases) by the exact same constant k.\nNew Mean = {item[0]} {'+' if 'add' in item[2] else '-'} {item[1]} = {item[0] + item[1] if 'add' in item[2] else item[0] - item[1]}."
        ),
        'diff': 'easy'
    })

    # Arch 5: Effect of multiplying/dividing all observations by a constant 'k'
    archs_731.append({
        'data': [
            (15, 2, "multiply by 2"), (20, 3, "multiply by 3"), (12, 4, "multiply by 4"),
            (30, 2, "divide by 2"), (60, 3, "divide by 3"), (40, 4, "divide by 4"),
            (25, 2, "multiply by 2"), (50, 5, "divide by 5"), (18, 3, "multiply by 3"),
            (80, 4, "divide by 4")
        ],
        'tmpls': [
            "The mean of 15 numbers is {0}. If every number is subjected to '{2}', what is the new mean?",
            "If the mean of a data set is {0} and each value is {2}, find the new mean:",
            "What is the updated mean if we {2} every observation in a distribution with original mean {0}?",
            "Calculate the new arithmetic mean when every score with mean {0} is {2}:",
            "Determine the resulting average if we {2} all values of a dataset having mean {0}:",
            "For a distribution having mean {0}, what is the new mean if each observation is {2}?",
            "Compute the new mean when each number in a dataset of mean {0} is {2}:",
            "If original mean is {0} and every observation is {2}, find the new mean:",
            "Find the resulting mean after we {2} all observations in a dataset with mean {0}:",
            "What is the new mean of a series with mean {0} when each item is {2}?"
        ],
        'calc': lambda item: (
            f"{item[0] * item[1] if 'multiply' in item[2] else item[0] // item[1]}",
            [f"{item[0]} (unchanged)", f"{item[0] + item[1]}", f"{item[0] // item[1] if 'multiply' in item[2] else item[0] * item[1]}"],
            f"Property of Mean: If every observation is multiplied (or divided) by a constant k, the new mean is the original mean multiplied (or divided) by k.\nNew Mean = {item[0]} {'*' if 'multiply' in item[2] else '/'} {item[1]} = {item[0] * item[1] if 'multiply' in item[2] else item[0] // item[1]}."
        ),
        'diff': 'easy'
    })

    # Arch 6: Combined Mean of two groups: X̄_c = (N1*X̄1 + N2*X̄2) / (N1 + N2)
    archs_731.append({
        'data': [
            (20, 60, 30, 70, "Group A", "Group B"),
            (25, 50, 25, 70, "Section 1", "Section 2"),
            (40, 65, 60, 75, "Boys", "Girls"),
            (30, 45, 20, 55, "Batch X", "Batch Y"),
            (50, 80, 50, 90, "School P", "School Q"),
            (15, 40, 35, 60, "Class 9A", "Class 9B"),
            (20, 55, 30, 65, "Team Red", "Team Blue"),
            (10, 70, 40, 80, "Shift 1", "Shift 2"),
            (30, 50, 70, 60, "Division M", "Division N"),
            (40, 75, 10, 85, "Center 1", "Center 2")
        ],
        'tmpls': [
            "{4} has {0} students with mean score {1}. {5} has {2} students with mean score {3}. Find the combined mean score of all students:",
            "Calculate the combined mean for {4} (N={0}, mean={1}) and {5} (N={2}, mean={3}):",
            "What is the combined average score of {4} ({0} students, mean {1}) and {5} ({2} students, mean {3})?",
            "Find the overall mean when {4} has {0} members with mean {1} and {5} has {2} members with mean {3}:",
            "Determine the combined mean of two groups: {4} ({0} items, mean {1}) and {5} ({2} items, mean {3}):",
            "Compute the pooled mean of {4} (size {0}, mean {1}) and {5} (size {2}, mean {3}):",
            "For two classes {4} (N={0}, mean={1}) and {5} (N={2}, mean={3}), calculate the combined mean:",
            "What is the combined mean of the whole group comprising {4} (N={0}, mean={1}) and {5} (N={2}, mean={3})?",
            "Calculate pooled average for {4} ({0} candidates, average {1}) and {5} ({2} candidates, average {3}):",
            "Find the combined mean for the combined strength of {4} ({0} at {1}) and {5} ({2} at {3}):"
        ],
        'calc': lambda item: (
            f"{(item[0] * item[1] + item[2] * item[3]) // (item[0] + item[2])}",
            [
                f"{((item[0] * item[1] + item[2] * item[3]) // (item[0] + item[2])) + 4}",
                f"{((item[0] * item[1] + item[2] * item[3]) // (item[0] + item[2])) - 3}",
                f"{(item[1] + item[3]) // 2} (simple average of means)"
            ],
            f"Step 1: Formula: Combined Mean X̄_c = (N1 * X̄1 + N2 * X̄2) / (N1 + N2).\nStep 2: Total Sum = ({item[0]} * {item[1]}) + ({item[2]} * {item[3]}) = {item[0] * item[1]} + {item[2] * item[3]} = {item[0] * item[1] + item[2] * item[3]}.\nStep 3: Total N = {item[0]} + {item[2]} = {item[0] + item[2]}.\nStep 4: Combined Mean = {item[0] * item[1] + item[2] * item[3]} / {item[0] + item[2]} = {(item[0] * item[1] + item[2] * item[3]) // (item[0] + item[2])}."
        ),
        'diff': 'hard'
    })

    # Arch 7: Properties and limitations of the Arithmetic Mean
    archs_731.append({
        'data': [
            ("What is the sum of deviations of all observations from their arithmetic mean (Σ(x - X̄))?", "Always equal to zero (Σ(x - X̄) = 0)", ["Always equal to 1", "Always equal to the sample size N", "Always equal to variance"]),
            ("Which measure of central tendency is based on every single observation in the dataset?", "Arithmetic Mean", ["Median", "Mode", "Range"]),
            ("What is the primary drawback/limitation of the Arithmetic Mean?", "It is heavily distorted and influenced by extreme values (outliers)", ["It cannot be computed for numbers", "It is always a whole number", "It has no algebraic formula"]),
            ("When a dataset contains severe extreme outliers, which measure of central tendency is most appropriate to use instead of the mean?", "Median", ["Arithmetic Mean", "Range", "Standard Deviation"]),
            ("Can the arithmetic mean be determined graphically from a histogram or ogive?", "No, the mean cannot be determined graphically (unlike Median and Mode)", ["Yes, from the highest bar of a histogram", "Yes, from the intersection of ogives", "Yes, from a pie diagram directly"]),
            ("If a data distribution is symmetric, what is the relationship between Mean, Median, and Mode?", "Mean = Median = Mode", ["The three measures are completely independent and never relate", "Mean is always twice the product of Median and Mode", "Mode is equal to zero while Mean and Median diverge"]),
            ("What is the direct formula for the mean of grouped data?", "X̄ = Σ(f * x) / Σf", ["X̄ = Σf / Σx", "X̄ = Σ(x - f) / N", "X̄ = (f_max - f_min) / 2"]),
            ("Why is the mean considered the most widely used measure of central tendency?", "Because it is rigidly defined, includes all observations, and lends itself to further algebraic treatment", ["Because it requires zero calculation", "Because it ignores all large numbers", "Because it is always equal to 100"]),
            ("If the mean of 10 observations is 25, what is the sum of these 10 observations?", "250 (Sum = Mean * N = 25 * 10)", ["25", "10", "2.5"]),
            ("An observation 45 was mistakenly recorded as 54. What will happen to the mean when the error is corrected?", "The corrected mean will decrease (since 45 < 54)", ["The corrected mean will increase", "The mean will remain unchanged", "The mean will become zero"])
        ],
        'tmpls': [
            "In statistical properties of Mean: {0}",
            "Theoretical concept of Arithmetic Mean: {0}",
            "Key mathematical property of Mean: {0}",
            "Evaluating central tendency: {0}",
            "Properties and limitations of Mean: {0}",
            "Understanding the Arithmetic Mean: {0}",
            "Algebraic characteristics of Mean: {0}",
            "Core principle of Arithmetic Mean: {0}",
            "Fundamental law of statistical Mean: {0}",
            "Mathematical theorem on Mean: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: In statistical mathematics, {item[1]}."
        ),
        'diff': 'foundation'
    })

    qs_731 = generate_subtopic(tc_731, tn_731, CH_NUM, CH_NAME, archs_731)
    all_qs.extend(qs_731)
    print(f"Generated {len(qs_731)} for {tc_731}")

    # -------------------------------------------------------------------------
    # 7.3.2: Median: Middle value of sorted array (N odd/even)
    # -------------------------------------------------------------------------
    tc_732 = "MH-9-MTH1-7-7.3.2"
    tn_732 = "Median: Middle value of sorted array (N odd/even)"
    archs_732 = []

    # Arch 0: Median of odd number of raw observations (N odd => ((N+1)/2)-th value)
    archs_732.append({
        'data': [
            ([12, 18, 14, 25, 16], [12, 14, 16, 18, 25], 16),
            ([30, 22, 45, 18, 38], [18, 22, 30, 38, 45], 30),
            ([8, 15, 12, 20, 10], [8, 10, 12, 15, 20], 12),
            ([40, 52, 35, 60, 48, 32, 55], [32, 35, 40, 48, 52, 55, 60], 48),
            ([7, 14, 21, 9, 18, 11, 16], [7, 9, 11, 14, 16, 18, 21], 14),
            ([25, 32, 28, 40, 20], [20, 25, 28, 32, 40], 28),
            ([50, 65, 45, 70, 55], [45, 50, 55, 65, 70], 55),
            ([15, 24, 19, 31, 28, 12, 22], [12, 15, 19, 22, 24, 28, 31], 22),
            ([60, 75, 50, 85, 68], [50, 60, 68, 75, 85], 68),
            ([11, 19, 14, 25, 16, 22, 13], [11, 13, 14, 16, 19, 22, 25], 16)
        ],
        'tmpls': [
            "Find the median of the raw observation set: {0}:",
            "Calculate the median for the data: {0}:",
            "What is the median value of the numbers: {0}?",
            "Determine the median of the observations: {0}:",
            "Compute the median for the dataset: {0}:",
            "For the observations {0}, find the median:",
            "What is the median of the list: {0}?",
            "Find the middle value (median) of: {0}:",
            "Calculate the median of the scores: {0}:",
            "Identify the median observation in: {0}:"
        ],
        'calc': lambda item: (
            f"{item[2]} (Sorted: {', '.join(str(x) for x in item[1])})",
            [f"{item[2] + 4}", f"{item[2] - 3}", f"{item[1][0]}"],
            f"Step 1: Arrange observations in ascending order: {', '.join(str(x) for x in item[1])}.\nStep 2: Here N = {len(item[1])} (odd).\nStep 3: Median is ((N+1)/2)-th observation = (({len(item[1])}+1)/2)-th = {item[2]}."
        ),
        'diff': 'easy'
    })

    # Arch 1: Median of even number of raw observations (average of N/2 and (N/2 + 1) terms)
    archs_732.append({
        'data': [
            ([12, 18, 14, 20, 16, 22], [12, 14, 16, 18, 20, 22], 17),
            ([25, 30, 22, 35, 28, 40], [22, 25, 28, 30, 35, 40], 29),
            ([8, 15, 12, 20, 10, 18], [8, 10, 12, 15, 18, 20], 13.5),
            ([40, 50, 35, 60, 45, 55], [35, 40, 45, 50, 55, 60], 47.5),
            ([10, 14, 18, 22, 26, 30], [10, 14, 18, 22, 26, 30], 20),
            ([32, 40, 28, 45, 36, 50], [28, 32, 36, 40, 45, 50], 38),
            ([15, 25, 20, 35, 30, 40], [15, 20, 25, 30, 35, 40], 27.5),
            ([50, 62, 44, 70, 56, 68], [44, 50, 56, 62, 68, 70], 59),
            ([18, 24, 21, 30, 27, 33], [18, 21, 24, 27, 30, 33], 25.5),
            ([60, 75, 65, 80, 70, 85], [60, 65, 70, 75, 80, 85], 72.5)
        ],
        'tmpls': [
            "Find the median of the {0} observations: {0}:",
            "Calculate the median for the even dataset: {0}:",
            "What is the median of the observations: {0}?",
            "Determine the median value for: {0}:",
            "Compute the median of the data: {0}:",
            "For the observation list {0}, calculate the median:",
            "What is the median of the scores: {0}?",
            "Find the median for the set of numbers: {0}:",
            "Calculate the middle value (median) of: {0}:",
            "Identify the median of the data points: {0}:"
        ],
        'calc': lambda item: (
            f"{item[2]:g} (Average of {item[1][len(item[1])//2 - 1]} and {item[1][len(item[1])//2]})",
            [f"{item[2] + 2:g}", f"{item[2] - 2.5:g}", f"{item[1][len(item[1])//2]}"],
            f"Step 1: Arrange observations in ascending order: {', '.join(str(x) for x in item[1])}.\nStep 2: Here N = {len(item[1])} (even). The two middle terms are {item[1][len(item[1])//2 - 1]} and {item[1][len(item[1])//2]}.\nStep 3: Median = ({item[1][len(item[1])//2 - 1]} + {item[1][len(item[1])//2]}) / 2 = {item[2]:g}."
        ),
        'diff': 'medium'
    })

    # Arch 2: Finding unknown 'x' in a pre-sorted data list given the median
    archs_732.append({
        'data': [
            ([12, 14, 16, "x", "x + 2", 24, 28, 30], 21, 20),
            ([20, 22, 25, "x", "x + 4", 35, 38, 40], 30, 28),
            ([10, 12, 15, "x", "x + 2", 22, 25, 28], 18, 17),
            ([30, 32, 36, "x", "x + 2", 44, 48, 52], 41, 40),
            ([15, 18, 20, "x", "x + 6", 32, 35, 38], 27, 24),
            ([8, 11, 14, "x", "x + 2", 20, 23, 26], 17, 16),
            ([40, 44, 48, "x", "x + 4", 60, 64, 68], 54, 52),
            ([25, 28, 32, "x", "x + 2", 40, 44, 48], 37, 36),
            ([14, 16, 18, "x", "x + 2", 24, 26, 28], 21, 20),
            ([50, 55, 60, "x", "x + 10", 80, 85, 90], 70, 65)
        ],
        'tmpls': [
            "Observations arranged in ascending order are: {0}. If the median of these 8 observations is {1}, find x:",
            "The data {0} is in ascending order. Given median = {1}, calculate the value of x:",
            "If the median of the sorted array {0} is {1}, determine the value of x:",
            "For the ascending data {0} with median = {1}, what is the value of x?",
            "Find x if the median of the sorted numbers {0} equals {1}:",
            "Calculate x when the median of the ordered series {0} is {1}:",
            "Given ordered observations {0} having median {1}, find x:",
            "What is the value of x if the median of sorted observations {0} is {1}?",
            "Determine x from the ordered observations {0} with median {1}:",
            "Find the unknown x in the ordered dataset {0} where median = {1}:"
        ],
        'calc': lambda item: (
            f"x = {item[2]}",
            [f"x = {item[2] + 4}", f"x = {item[2] - 3}", f"x = {item[1]}"],
            f"Step 1: Since N = 8 (even), Median is the average of 4th and 5th terms: (x + {item[0][4]}) / 2 = {item[1]}.\nStep 2: Solve equation for x.\nStep 3: x = {item[2]}."
        ),
        'diff': 'hard'
    })

    # Arch 3: Median of discrete frequency table using cumulative frequency
    archs_732.append({
        'data': [
            ([(10, 3), (20, 5), (30, 8), (40, 4)], 30, 20),
            ([(15, 4), (25, 7), (35, 9), (45, 5)], 35, 25),
            ([(5, 2), (10, 6), (15, 11), (20, 5)], 15, 24),
            ([(20, 5), (30, 8), (40, 12), (50, 5)], 40, 30),
            ([(8, 3), (12, 7), (16, 10), (20, 4)], 16, 24),
            ([(25, 4), (35, 9), (45, 11), (55, 6)], 45, 30),
            ([(12, 5), (18, 8), (24, 14), (30, 5)], 24, 32),
            ([(30, 6), (40, 10), (50, 15), (60, 9)], 50, 40),
            ([(14, 4), (21, 9), (28, 12), (35, 5)], 28, 30),
            ([(40, 5), (50, 11), (60, 16), (70, 8)], 60, 40)
        ],
        'tmpls': [
            "Find the median for the discrete frequency distribution with (value x, frequency f) pairs: {0}:",
            "Calculate the median of the discrete distribution: {0}:",
            "What is the median value for the frequency table: {0}?",
            "Determine the median observation for the pairs (x, f): {0}:",
            "Compute the median from the frequency table: {0}:",
            "For the discrete distribution {0}, find the median:",
            "Calculate median value of the data: {0}:",
            "Find the median for the frequency observations: {0}:",
            "What is the median for the table of values: {0}?",
            "Identify the median in the discrete distribution: {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]} (Total N = {item[2]}, N/2 = {item[2]//2})",
            [f"{item[1] + 10}", f"{item[1] - 10}", f"{item[2]//2}"],
            f"Step 1: Compute cumulative frequencies (cf).\nStep 2: Total N = {item[2]}, N/2 = {item[2]//2}.\nStep 3: The observation x corresponding to cf >= {item[2]//2} is {item[1]}."
        ),
        'diff': 'medium'
    })

    # Arch 4: Effect of extreme outliers on Median vs Mean
    archs_732.append({
        'data': [
            ([10, 12, 14, 16, 100], 14, 30.4),
            ([20, 22, 24, 26, 250], 24, 68.4),
            ([15, 18, 20, 22, 180], 20, 51.0),
            ([5, 8, 10, 12, 95], 10, 26.0),
            ([30, 32, 35, 38, 300], 35, 87.0),
            ([12, 15, 18, 21, 150], 18, 43.2),
            ([25, 28, 30, 32, 220], 30, 67.0),
            ([14, 16, 19, 21, 140], 19, 42.0),
            ([40, 42, 45, 48, 400], 45, 115.0),
            ([18, 20, 22, 24, 190], 22, 54.8)
        ],
        'tmpls': [
            "Consider the dataset with an extreme outlier: {0}. Calculate the Median and observe why it represents the data better than the Mean:",
            "For the dataset {0} containing an extreme outlier, what is the Median?",
            "Find the median of the observation set: {0}:",
            "What is the median of {0}, and does the extreme value affect it?",
            "Determine the median of the data {0}:",
            "Calculate the median for the dataset with outlier: {0}:",
            "Find the median of: {0}:",
            "Compute the median of the observations: {0}:",
            "What is the median of the set: {0}?",
            "Identify the median value for: {0}:"
        ],
        'calc': lambda item: (
            f"Median = {item[1]} (unaffected by outlier, whereas Mean is inflated to {item[2]:.1f})",
            [f"Median = {item[2]:.1f} (same as mean)", f"Median = {item[1] + 10}", f"Median = {item[0][-1]} (the outlier)"],
            f"Step 1: Sort data: {', '.join(str(x) for x in item[0])}.\nStep 2: Middle value (3rd of 5) is {item[1]}.\nStep 3: Median = {item[1]}. Notice that while the Mean is inflated to {item[2]:.1f} by the outlier, the Median remains completely robust."
        ),
        'diff': 'medium'
    })

    # Arch 5: Definition and positional nature of Median
    archs_732.append({
        'data': [
            ("What is the statistical Median?", "The middle-most observation when all data values are arranged in ascending or descending order", ["The most frequently occurring value in the dataset", "The sum of all values divided by total count", "The difference between maximum and minimum"]),
            ("Why is the Median called a 'positional average'?", "Because its value depends strictly on its position in the sorted array, dividing data into two equal halves", ["Because it changes with geographical position", "Because it is measured using GPS coordinates", "Because it can only be calculated for positive numbers"]),
            ("What percentage of total observations lie below the Median?", "Exactly 50% of the observations", ["25% of observations", "75% of observations", "100% of observations"]),
            ("What percentage of total observations lie above the Median?", "Exactly 50% of the observations", ["10% of observations", "33.3% of observations", "0% of observations"]),
            ("What is the second quartile (Q2) of a distribution identical to?", "The Median", ["The Mode", "The Arithmetic Mean", "The Range"]),
            ("What is the 50th percentile (P50) of a distribution equal to?", "The Median", ["The Mean", "The Upper Quartile", "The Interquartile Range"]),
            ("Can the Median be determined when a frequency distribution has open-ended classes at the extremes?", "Yes, because the median depends only on the central observations and not on extreme boundary values", ["No, open-ended classes prevent finding the median", "Yes, but only if all frequencies are equal", "No, medians require closed circles"]),
            ("In an ordered dataset of N = 9 observations, which observation is the Median?", "The 5th observation ((9 + 1)/2 = 5)", ["The 4th observation", "The 9th observation", "The 1st observation"]),
            ("In an ordered dataset of N = 10 observations, which observations determine the Median?", "The average of the 5th and 6th observations", ["The 5th observation only", "The 10th observation only", "The 1st and 10th observations"]),
            ("Which graphical method allows direct determination of the Median?", "The X-coordinate of the intersection point of less-than and more-than ogive curves", ["The highest point of a bar chart", "The center of a pie chart", "The slope of a trend line"])
        ],
        'tmpls': [
            "In statistical theory of Median: {0}",
            "Understanding the Median: {0}",
            "Core concept of positional average: {0}",
            "Evaluating properties of Median: {0}",
            "Key knowledge on statistical Median: {0}",
            "Properties of the Median: {0}",
            "Positional nature of Median: {0}",
            "Mathematical definition of Median: {0}",
            "Fundamental law of the Median: {0}",
            "Essential principles of Median: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: In statistical science, {item[1]}."
        ),
        'diff': 'foundation'
    })

    # Arch 6: Effect of adding a new observation on Median
    archs_732.append({
        'data': [
            ([10, 14, 18, 22, 26], 20, 18, 19),
            ([15, 20, 25, 30, 35], 28, 25, 26.5),
            ([8, 12, 16, 20, 24], 14, 16, 15),
            ([30, 35, 40, 45, 50], 42, 40, 41),
            ([5, 10, 15, 20, 25], 12, 15, 13.5),
            ([20, 25, 30, 35, 40], 32, 30, 31),
            ([12, 16, 20, 24, 28], 18, 20, 19),
            ([40, 45, 50, 55, 60], 52, 50, 51),
            ([14, 18, 22, 26, 30], 25, 22, 23.5),
            ([50, 60, 70, 80, 90], 75, 70, 72.5)
        ],
        'tmpls': [
            "A dataset has 5 sorted observations: {0} with median {2}. If a new observation {1} is added, what is the new median?",
            "Given 5 values {0} (median = {2}), find the new median after including {1}:",
            "The median of {0} is {2}. What will the median be when {1} is added to the dataset?",
            "Calculate the new median of the observations {0} after introducing {1}:",
            "Determine the updated median of {0} once the value {1} is included:",
            "For the observations {0}, median is {2}. Find the new median when {1} is appended:",
            "What is the new median of {0} after adding {1}?",
            "Find the revised median of the numbers {0} upon adding {1}:",
            "Compute the new median when {1} is added to the five numbers {0}:",
            "Identify the new median of {0} after the addition of {1}:"
        ],
        'calc': lambda item: (
            f"{item[3]:g}",
            [f"{item[2]:g} (unchanged)", f"{item[3] + 2:g}", f"{item[1]}"],
            f"Step 1: Original sorted values: {item[0]}, original median = {item[2]}.\nStep 2: Add {item[1]} and re-sort: {sorted(item[0] + [item[1]])}.\nStep 3: New N = 6 (even). Middle two values are averaged to give {item[3]:g}."
        ),
        'diff': 'medium'
    })

    # Arch 7: Comparison between Mean and Median
    archs_732.append({
        'data': [
            ("Which measure of central tendency is preferable when studying highly skewed data like national income or wealth distribution?", "Median (unaffected by billionaire extreme incomes)", ["Arithmetic Mean", "Range", "Standard Deviation"]),
            ("Why is the mean higher than the median in a positively skewed (right-skewed) distribution?", "Because extremely high values pull the mean towards the right tail", ["Because median ignores positive numbers", "Because mean is always twice the median", "Because frequencies are negative"]),
            ("In a perfectly symmetrical bell-shaped normal distribution, what is true about Mean and Median?", "Mean equals Median (Mean = Median)", ["Mean is 10 times larger than Median", "Median is always zero", "Mean is undefined"]),
            ("Does changing the value of the largest observation in a dataset change the Median?", "No, the median remains unchanged as long as the altered value remains on the same side of the middle", ["Yes, the median always doubles", "Yes, the median becomes undefined", "Yes, the median moves to zero"]),
            ("Does changing the value of the largest observation in a dataset change the Arithmetic Mean?", "Yes, the mean will immediately increase or decrease because it incorporates every value", ["No, the mean never changes", "Only if the change is negative", "Only if approved by census"]),
            ("Which average represents the value such that the sum of absolute deviations (|x - A|) is minimized?", "Median (Σ|x - Median| is a minimum)", ["Arithmetic Mean", "Mode", "Geometric Mean"]),
            ("Which average represents the value such that the sum of squared deviations ((x - A)^2) is minimized?", "Arithmetic Mean (Σ(x - Mean)^2 is a minimum)", ["Median", "Mode", "Range"]),
            ("Can the Median be negative?", "Yes, if the middle observation of the dataset is negative", ["No, medians are strictly positive", "No, medians cannot be less than zero", "Only in financial bankruptcy"]),
            ("Can the Median be a fraction when all observations are integers?", "Yes, when N is even and the two middle observations have an odd sum (e.g. (3+4)/2 = 3.5)", ["No, medians of integers are always integers", "No, fractions are impossible in statistics", "Only for continuous variables"]),
            ("Which average is best suited for qualitative or ranked data (e.g. ranking students 1st, 2nd, 3rd in honesty)?", "Median", ["Arithmetic Mean", "Standard Deviation", "Root Mean Square"])
        ],
        'tmpls': [
            "In comparing Mean and Median: {0}",
            "Theoretical comparison of averages: {0}",
            "Core distinction between Mean and Median: {0}",
            "Evaluating central tendency metrics: {0}",
            "Key contrast between Mean and Median: {0}",
            "Properties of Mean versus Median: {0}",
            "Comparative statistics of central tendency: {0}",
            "Mathematical properties of Mean and Median: {0}",
            "Fundamental contrast in averages: {0}",
            "Principles of selecting Mean or Median: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: In statistical methodology, {item[1]}."
        ),
        'diff': 'foundation'
    })

    qs_732 = generate_subtopic(tc_732, tn_732, CH_NUM, CH_NAME, archs_732)
    all_qs.extend(qs_732)
    print(f"Generated {len(qs_732)} for {tc_732}")

    # -------------------------------------------------------------------------
    # 7.3.3: Mode: Most frequently occurring value
    # -------------------------------------------------------------------------
    tc_733 = "MH-9-MTH1-7-7.3.3"
    tn_733 = "Mode: Most frequently occurring value"
    archs_733 = []

    # Arch 0: Mode of raw ungrouped data (Unimodal)
    archs_733.append({
        'data': [
            ([12, 15, 18, 15, 20, 15, 22], 15, 3),
            ([24, 28, 30, 28, 35, 28, 40], 28, 3),
            ([8, 12, 10, 12, 15, 12, 18], 12, 3),
            ([45, 50, 45, 55, 60, 45, 65], 45, 3),
            ([14, 19, 14, 21, 14, 25, 28], 14, 3),
            ([32, 38, 35, 38, 42, 38, 48], 38, 3),
            ([5, 9, 7, 9, 11, 9, 13], 9, 3),
            ([50, 65, 50, 70, 50, 80, 55], 50, 3),
            ([18, 22, 26, 22, 30, 22, 34], 22, 3),
            ([40, 48, 42, 48, 55, 48, 60], 48, 3)
        ],
        'tmpls': [
            "Find the mode of the raw observation set: {0}:",
            "Calculate the mode of the numbers: {0}:",
            "What is the mode of the data: {0}?",
            "Determine the mode for the observation list: {0}:",
            "Compute the mode of the dataset: {0}:",
            "For the observations {0}, find the mode:",
            "What is the mode of the scores: {0}?",
            "Find the most frequent observation (mode) in: {0}:",
            "Calculate the mode of the values: {0}:",
            "Identify the mode in the data set: {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]} (occurs {item[2]} times)",
            [f"{item[1] + 3}", f"{item[1] - 4}", f"{item[0][0]}"],
            f"Step 1: Count the frequency of each distinct value in {item[0]}.\nStep 2: Value {item[1]} occurs {item[2]} times, which is the highest frequency.\nStep 3: Mode = {item[1]}."
        ),
        'diff': 'easy'
    })

    # Arch 1: Bimodal datasets (Two modes)
    archs_733.append({
        'data': [
            ([12, 15, 18, 15, 20, 18, 22], "15 and 18 (both occur 2 times)"),
            ([24, 28, 30, 28, 35, 30, 40], "28 and 30 (both occur 2 times)"),
            ([8, 12, 10, 12, 15, 10, 18], "10 and 12 (both occur 2 times)"),
            ([45, 50, 45, 55, 50, 60, 65], "45 and 50 (both occur 2 times)"),
            ([14, 19, 14, 21, 19, 25, 28], "14 and 19 (both occur 2 times)"),
            ([32, 38, 35, 38, 35, 42, 48], "35 and 38 (both occur 2 times)"),
            ([5, 9, 7, 9, 7, 11, 13], "7 and 9 (both occur 2 times)"),
            ([50, 65, 50, 70, 65, 80, 55], "50 and 65 (both occur 2 times)"),
            ([18, 22, 26, 22, 26, 30, 34], "22 and 26 (both occur 2 times)"),
            ([40, 48, 42, 48, 42, 55, 60], "42 and 48 (both occur 2 times)")
        ],
        'tmpls': [
            "Find the mode(s) of the dataset: {0}:",
            "What are the modes of the observation set: {0}?",
            "Identify the mode(s) for the numbers: {0}:",
            "Determine the mode(s) of the data list: {0}:",
            "Calculate the mode(s) for the observations: {0}:",
            "For the observations {0}, state the mode(s):",
            "What are the most frequent values (modes) in: {0}?",
            "Find the mode(s) of the scores: {0}:",
            "Compute the mode(s) of the values: {0}:",
            "Identify the bimodal values in: {0}:"
        ],
        'calc': lambda item: (
            item[1],
            ["No mode exists in this dataset", "The arithmetic mean of all numbers", f"{item[0][0]} only"],
            f"Step 1: Tally frequencies for {item[0]}.\nStep 2: Two values tie for the highest frequency.\nStep 3: Distribution is bimodal: {item[1]}."
        ),
        'diff': 'medium'
    })

    # Arch 2: Dataset with No Mode (all values have equal frequency)
    archs_733.append({
        'data': [
            ([10, 15, 20, 25, 30], "No mode (each value appears exactly once)"),
            ([12, 14, 16, 18, 20], "No mode (all observations occur with equal frequency of 1)"),
            ([25, 35, 45, 55, 65], "No mode (all values occur once with equal frequency)"),
            ([8, 12, 16, 20, 24], "No mode (no single value occurs more frequently than others)"),
            ([40, 50, 60, 70, 80], "No mode (each observation occurs exactly once)"),
            ([7, 14, 21, 28, 35], "No mode (all numbers have identical frequency of 1)"),
            ([32, 42, 52, 62, 72], "No mode (no value repeats more than others)"),
            ([18, 24, 30, 36, 42], "No mode (all items have equal frequency of 1)"),
            ([11, 22, 33, 44, 55], "No mode (every observation appears exactly once)"),
            ([50, 60, 70, 80, 90], "No mode (uniform frequency across all distinct values)")
        ],
        'tmpls': [
            "Find the mode of the dataset: {0}:",
            "What is the mode of the observation set: {0}?",
            "Determine the mode of the numbers: {0}:",
            "Calculate the mode for the data: {0}:",
            "For the observations {0}, identify the mode:",
            "What is the mode of the scores: {0}?",
            "State the mode for the values: {0}:",
            "Identify the mode of the dataset: {0}:",
            "Compute the mode for: {0}:",
            "Find the mode corresponding to: {0}:"
        ],
        'calc': lambda item: (
            item[1],
            [f"Mode is {item[0][len(item[0])//2]} (the middle number)", f"Mode is {item[0][0]} (the first number)", "Mode is 0"],
            f"Rule: If every value in a dataset occurs with the exact same frequency, the dataset has NO mode.\nResult: {item[1]}."
        ),
        'diff': 'easy'
    })

    # Arch 3: Mode of discrete frequency table (value with highest frequency)
    archs_733.append({
        'data': [
            ([(10, 4), (20, 12), (30, 8), (40, 5)], 20, 12),
            ([(15, 6), (25, 15), (35, 9), (45, 4)], 25, 15),
            ([(5, 3), (10, 7), (15, 18), (20, 6)], 15, 18),
            ([(30, 5), (40, 14), (50, 22), (60, 8)], 50, 22),
            ([(8, 4), (12, 16), (16, 11), (20, 5)], 12, 16),
            ([(25, 7), (35, 20), (45, 13), (55, 6)], 35, 20),
            ([(14, 5), (21, 11), (28, 25), (35, 9)], 28, 25),
            ([(40, 8), (50, 17), (60, 24), (70, 10)], 60, 24),
            ([(12, 6), (18, 14), (24, 19), (30, 8)], 24, 19),
            ([(50, 9), (60, 21), (70, 30), (80, 12)], 70, 30)
        ],
        'tmpls': [
            "Find the mode for the discrete frequency distribution with (value x, frequency f) pairs: {0}:",
            "What is the mode of the frequency table: {0}?",
            "Identify the mode for the discrete pairs (x, f): {0}:",
            "Determine the mode of the distribution: {0}:",
            "Calculate the mode from the frequency data: {0}:",
            "For the discrete distribution {0}, what is the mode?",
            "Find the mode of the data given as: {0}:",
            "Compute the mode of the frequency distribution: {0}:",
            "What is the mode value for the pairs: {0}?",
            "Identify the mode in the frequency table: {0}:"
        ],
        'calc': lambda item: (
            f"Mode = {item[1]} (highest frequency = {item[2]})",
            [f"Mode = {item[2]} (the frequency itself)", f"Mode = {item[1] + 10}", f"Mode = {item[0][0][0]}"],
            f"Step 1: In a discrete frequency table, Mode is the observation value x that has the maximum frequency f.\nStep 2: Highest frequency is {item[2]}, corresponding to x = {item[1]}.\nStep 3: Mode = {item[1]}."
        ),
        'diff': 'easy'
    })

    # Arch 4: Empirical relationship between Mean, Median, and Mode: Mode = 3*Median - 2*Mean
    archs_733.append({
        'data': [
            (30, 32, "Mean = 30, Median = 32"),
            (40, 42, "Mean = 40, Median = 42"),
            (50, 54, "Mean = 50, Median = 54"),
            (25, 28, "Mean = 25, Median = 28"),
            (60, 63, "Mean = 60, Median = 63"),
            (35, 38, "Mean = 35, Median = 38"),
            (45, 48, "Mean = 45, Median = 48"),
            (20, 24, "Mean = 20, Median = 24"),
            (55, 58, "Mean = 55, Median = 58"),
            (65, 70, "Mean = 65, Median = 70")
        ],
        'tmpls': [
            "For a moderately skewed distribution, {2}. Using the empirical relationship (Mode = 3*Median - 2*Mean), calculate the Mode:",
            "Given {2}, find the Mode using the empirical formula Mode = 3*Median - 2*Mean:",
            "Calculate Mode when {2} using the standard empirical formula:",
            "What is the Mode of a distribution having {2} as per Mode = 3*Median - 2*Mean?",
            "Determine the Mode using empirical relation given {2}:",
            "Apply Karl Pearson's empirical formula (Mode = 3*Median - 2*Mean) to find Mode when {2}:",
            "Compute the Mode for a distribution with {2}:",
            "Find the Mode from {2} using empirical formula:",
            "What is the empirical Mode for a data set with {2}?",
            "Calculate Mode = 3*Median - 2*Mean for {2}:"
        ],
        'calc': lambda item: (
            f"{3 * item[1] - 2 * item[0]}",
            [f"{3 * item[1] - 2 * item[0] + 4}", f"{3 * item[1] - 2 * item[0] - 5}", f"{(item[0] + item[1]) // 2}"],
            f"Step 1: Formula: Mode = 3 * Median - 2 * Mean.\nStep 2: Substitute: 3 * {item[1]} - 2 * {item[0]} = {3 * item[1]} - {2 * item[0]}.\nStep 3: Mode = {3 * item[1] - 2 * item[0]}."
        ),
        'diff': 'medium'
    })

    # Arch 5: Empirical relationship: Finding Mean given Mode and Median
    # 2*Mean = 3*Median - Mode => Mean = (3*Median - Mode) / 2
    archs_733.append({
        'data': [
            (36, 32, "Mode = 36, Median = 32"),
            (46, 42, "Mode = 46, Median = 42"),
            (62, 54, "Mode = 62, Median = 54"),
            (34, 28, "Mode = 34, Median = 28"),
            (69, 63, "Mode = 69, Median = 63"),
            (44, 38, "Mode = 44, Median = 38"),
            (54, 48, "Mode = 54, Median = 48"),
            (32, 24, "Mode = 32, Median = 24"),
            (64, 58, "Mode = 64, Median = 58"),
            (80, 70, "Mode = 80, Median = 70")
        ],
        'tmpls': [
            "For a moderately skewed distribution, {2}. Using Mode = 3*Median - 2*Mean, find the Mean:",
            "Given {2}, calculate the Mean using the empirical relationship:",
            "Calculate the Mean for a distribution with {2} using Mode = 3*Median - 2*Mean:",
            "What is the Mean when {2} as per the empirical formula?",
            "Determine the Mean using empirical relation given {2}:",
            "Compute Mean from {2} using Mode = 3*Median - 2*Mean:",
            "Find the Mean for a distribution having {2}:",
            "What is the value of Mean given {2}?",
            "Calculate Mean = (3*Median - Mode) / 2 for {2}:",
            "Identify the Mean for a data set with {2}:"
        ],
        'calc': lambda item: (
            f"{(3 * item[1] - item[0]) // 2}",
            [f"{((3 * item[1] - item[0]) // 2) + 3}", f"{((3 * item[1] - item[0]) // 2) - 4}", f"{item[0]}"],
            f"Step 1: Formula: Mode = 3 * Median - 2 * Mean => 2 * Mean = 3 * Median - Mode => Mean = (3 * Median - Mode) / 2.\nStep 2: Calculate: (3 * {item[1]} - {item[0]}) / 2 = ({3 * item[1]} - {item[0]}) / 2 = {3 * item[1] - item[0]} / 2.\nStep 3: Mean = {(3 * item[1] - item[0]) // 2}."
        ),
        'diff': 'hard'
    })

    # Arch 6: Real-world business applications of the Mode
    archs_733.append({
        'data': [
            ("A footwear manufacturer wants to know which shoe size to produce in the largest quantity. Which measure of central tendency should they analyze?", "Mode (the most popular/frequently sold shoe size)", ["Arithmetic Mean (which might be a fractional non-existent shoe size)", "Median", "Standard Deviation"]),
            ("A garment factory manager tracks daily sales of shirts (sizes 38, 40, 42, 44) to optimize inventory. Which average is most useful?", "Mode", ["Arithmetic Mean", "Median", "Range"]),
            ("A bakery owner wants to decide which cake flavor is most demanded by customers each week. Which measure is appropriate?", "Mode", ["Arithmetic Mean", "Median", "Geometric Mean"]),
            ("Which average is uniquely suitable for nominal categorical data that cannot be arranged in numerical order?", "Mode", ["Arithmetic Mean", "Median", "Variance"]),
            ("Can a dataset have more than one Mode?", "Yes, a dataset can be bimodal (two modes), trimodal (three modes), or multimodal", ["No, every statistical average is strictly unique", "Only if approved by the bank", "Only if the mean is negative"]),
            ("Can the Mode be determined graphically from a Histogram?", "Yes, by identifying the highest rectangle and drawing intersecting diagonals to the X-axis", ["No, mode can only be read from pie charts", "No, mode has no graphical depiction", "Only from a scatter plot"]),
            ("Why is the Mode not ideal for advanced algebraic manipulation?", "Because it is not rigidly defined and not based on all observations of the dataset", ["Because computers cannot calculate mode", "Because mode is always equal to zero", "Because mode requires drawing circles"]),
            ("If a set of numbers is 4, 4, 4, 5, 6, 7, what is the mode?", "4 (appears 3 times, which is the highest frequency)", ["5", "6", "4.5"]),
            ("Which average is least influenced by extreme outlier values at the tails of a distribution?", "Mode and Median", ["Arithmetic Mean", "Root Mean Square", "Harmonic Mean"]),
            ("In market research, finding the most preferred brand of smartphone among college students identifies the:", "Mode of brand preferences", ["Arithmetic Mean of brands", "Median brand", "Standard deviation of brands"])
        ],
        'tmpls': [
            "In practical applications of Mode: {0}",
            "Business application of statistical averages: {0}",
            "Core concept of Mode in industry: {0}",
            "Evaluating practical usage of Mode: {0}",
            "Key knowledge on statistical Mode: {0}",
            "Real-world relevance of Mode: {0}",
            "Commerce and statistical Mode: {0}",
            "Applied statistics in decision making: {0}",
            "Fundamental utility of the Mode: {0}",
            "Choosing the Mode in commercial planning: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: In applied statistics and business planning, {item[1]}."
        ),
        'diff': 'foundation'
    })

    # Arch 7: Summary concepts: Comparing Mean, Median, and Mode
    archs_733.append({
        'data': [
            ("Which of the three measures of central tendency is based on all observations in a dataset?", "Arithmetic Mean only", ["Median only", "Mode only", "Both Median and Mode"]),
            ("Which measure of central tendency divides an ordered dataset into two exactly equal halves?", "Median", ["Mean", "Mode", "Range"]),
            ("Which measure of central tendency represents the most common or popular observation?", "Mode", ["Mean", "Median", "Standard Deviation"]),
            ("What is the empirical relation connecting Mean, Median, and Mode for a moderately asymmetrical distribution?", "Mode = 3 * Median - 2 * Mean", ["Mode = 2 * Median - 3 * Mean", "Mean = 3 * Mode - 2 * Median", "Median = 3 * Mean - 2 * Mode"]),
            ("If Mean = 25 and Median = 25 in a symmetrical distribution, what is the Mode?", "25 (in a symmetrical distribution, Mean = Median = Mode)", ["50", "0", "12.5"]),
            ("Which measure of central tendency can be located graphically from the highest bar of a histogram?", "Mode", ["Mean", "Median", "Standard Error"]),
            ("Which measure of central tendency can be located graphically from ogive curves?", "Median", ["Mean", "Mode", "Variance"]),
            ("Which average is unaffected by an extreme value added to the high end of a dataset?", "Median and Mode", ["Arithmetic Mean", "Combined Mean", "Weighted Mean"]),
            ("What is a distribution called when all three measures of central tendency coincide (Mean = Median = Mode)?", "Symmetrical Distribution", ["Positively Skewed Distribution", "Negatively Skewed Distribution", "Bimodal Distribution"]),
            ("Why are Mean, Median, and Mode collectively called 'Measures of Central Tendency'?", "Because they represent the central or typical value around which the observations tend to cluster", ["Because they are measured only in the center of India", "Because they apply only to round circles", "Because they equal zero at the origin"])
        ],
        'tmpls': [
            "In comparative central tendency theory: {0}",
            "Core summary of central tendency: {0}",
            "Comparing Mean, Median, and Mode: {0}",
            "Fundamental principles of statistical averages: {0}",
            "Evaluating measures of central tendency: {0}",
            "Synthesis of Mean, Median, and Mode: {0}",
            "Key relationships in descriptive statistics: {0}",
            "Overview of central tendency metrics: {0}",
            "Theoretical summary of statistical averages: {0}",
            "Essential concepts of central tendency: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: In descriptive statistics, {item[1]}."
        ),
        'diff': 'foundation'
    })

    qs_733 = generate_subtopic(tc_733, tn_733, CH_NUM, CH_NAME, archs_733)
    all_qs.extend(qs_733)
    print(f"Generated {len(qs_733)} for {tc_733}")

    with open('scripts/mh9_mth1_ch7_perfect.json', 'w', encoding='utf-8') as f:
        json.dump(all_qs, f, indent=2)
    print(f"🎉 Complete Chapter 7 compiled! Total questions: {len(all_qs)}")

build_part2()
