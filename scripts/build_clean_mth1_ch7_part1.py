# scripts/build_clean_mth1_ch7_part1.py
# Generator for Chapter 7: Statistics (Subtopics 7.1.1 to 7.2.1 = 320 Questions)
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from engine_algebra import generate_subtopic

CH_NUM = 7
CH_NAME = "Statistics"

all_qs = []

# ==============================================================================
# 7.1.1: Data collection methods (Primary data vs Secondary data)
# ==============================================================================
tc_711 = "MH-9-MTH1-7-7.1.1"
tn_711 = "Data collection methods"
archs_711 = []

# Arch 0: Definition of Primary Data
archs_711.append({
    'data': [
        ("When an investigator collects information directly from the source by conducting personal interviews or direct measurements, what is the data called?", "Primary Data", ["Secondary Data", "Hypothetical Data", "Archival Data"]),
        ("Data collected by a student directly counting the number of trees in their school campus is:", "Primary Data", ["Secondary Data", "Extrapolated Data", "Secondary Census Record"]),
        ("Which of the following is a primary method of data collection?", "Direct personal observation or door-to-door survey", ["Reading statistics from an encyclopedia", "Downloading a summary table from a website", "Extracting numbers from an old newspaper report"]),
        ("Why is primary data generally considered more reliable and precise for a specific investigation?", "Because it is collected first-hand for the exact inquiry at hand", ["Because it requires zero effort to obtain", "Because it is always published in textbooks", "Because it is checked by municipal corporations"]),
        ("What is the primary drawback of gathering primary data compared to secondary data?", "Requires more time, financial expense, and field labor", ["It is always mathematically incorrect", "It cannot be displayed in tables", "It is prohibited by national statistical laws"]),
        ("A researcher distributes a questionnaire directly to 50 local shopkeepers to study their daily sales. This is:", "Primary Data collection", ["Secondary Data retrieval", "Indirect literature search", "Library compilation"]),
        ("Measurements of height and weight of students taken directly by the physical education teacher are:", "Primary Data", ["Secondary Data", "Historical Archive Data", "Synthetic Simulated Data"]),
        ("Which term describes original data collected for the first time by an investigator for a predetermined purpose?", "Primary Data", ["Secondary Data", "Derivative Data", "Quaternary Data"]),
        ("A survey conducted by interviewing villagers face-to-face regarding water supply issues yields:", "Primary Data", ["Secondary Data", "Tertiary Compilation", "Unverified Rumor"]),
        ("Data gathered through direct experiments conducted in a physics laboratory represents:", "Primary Data", ["Secondary Data", "Secondary Reference", "Published Index"])
    ],
    'tmpls': [
        "In statistical data collection: {0}",
        "Fundamental concept of statistical data: {0}",
        "Data collection methodology: {0}",
        "Statistical inquiry principle: {0}",
        "Classifying statistical information: {0}",
        "Evaluating research methods: {0}",
        "Statistical literacy question: {0}",
        "Types of statistical data: {0}",
        "Core principle of data collection: {0}",
        "Understanding data origin: {0}"
    ],
    'calc': lambda item: (
        item[1],
        item[2],
        f"Explanation: In statistics, {item[1]}."
    ),
    'diff': 'foundation'
})

# Arch 1: Definition of Secondary Data
archs_711.append({
    'data': [
        ("Information obtained from already published reports, government bulletins, or internet archives is known as:", "Secondary Data", ["Primary Data", "Raw Unprocessed Data", "Experimental Observation"]),
        ("Data compiled by a student from the official Census of India website for a project is:", "Secondary Data", ["Primary Data", "Laboratory Measurement", "Field Interview Data"]),
        ("Which of the following constitutes secondary data?", "Weather rainfall records retrieved from a meteorological department publication", ["Rainfall measured directly using a raingauge in your backyard", "Counting raindrops on a window pane", "Personal stopwatch timing of rainfall duration"]),
        ("What is an advantage of using secondary data?", "Saves considerable time, effort, and financial cost", ["Guarantees 100% accuracy without verification", "Collected specifically for your unique problem", "Eliminates need for any analysis"]),
        ("What precaution is essential when utilizing secondary data?", "Scrutinizing the reliability, source credibility, and suitability for the current study", ["Accepting all figures uncritically without checking", "Assuming older records are always superior", "Never citing the original author"]),
        ("A student extracts crime statistics from the local police annual report for an essay. This data is:", "Secondary Data", ["Primary Data", "Direct Observation", "Experimental Result"]),
        ("Financial figures taken from the published balance sheet of a listed corporation represent:", "Secondary Data", ["Primary Data", "Direct Field Count", "Unprocessed Field Notes"]),
        ("Which of the following is a published source of secondary data?", "Government gazettes and statistical abstracts", ["Personal door-to-door interview logbook", "Laboratory notebook of ongoing experiment", "Student classroom roll-call tally sheet"]),
        ("When a journalist quotes employment figures published by the Ministry of Labour, they are using:", "Secondary Data", ["Primary Data", "Private Diary", "Experimental Measurement"]),
        ("Data obtained from historical archives or encyclopedias for academic research is classified as:", "Secondary Data", ["Primary Data", "Field Survey Data", "Original First-hand Log"])
    ],
    'tmpls': [
        "Regarding secondary data: {0}",
        "In empirical research: {0}",
        "Understanding secondary sources: {0}",
        "Statistical source classification: {0}",
        "Key feature of secondary data: {0}",
        "Evaluating data origins: {0}",
        "Research methodology question: {0}",
        "Classification of research information: {0}",
        "Statistical survey concepts: {0}",
        "Data origin and reliability: {0}"
    ],
    'calc': lambda item: (
        item[1],
        item[2],
        f"Explanation: In statistics, {item[1]}."
    ),
    'diff': 'foundation'
})

# Arch 2: Classifying specific real-world scenarios as Primary or Secondary Data
archs_711.append({
    'data': [
        ("Blood groups of 40 students determined by testing blood samples directly in a biology lab", "Primary Data"),
        ("Number of absent students noted by checking the school office attendance register", "Secondary Data"),
        ("Literacy rate of Maharashtra obtained from the 2011 Census report", "Secondary Data"),
        ("Heart rates of 15 athletes measured using a pulse monitor after a 100m sprint", "Primary Data"),
        ("Daily maximum temperatures recorded by a student using a thermometer in the garden", "Primary Data"),
        ("Population growth trend of Pune city taken from the Municipal Corporation handbook", "Secondary Data"),
        ("Responses collected by administering an opinion survey to 100 shoppers at a mall", "Primary Data"),
        ("Export-import values obtained from the Reserve Bank of India annual bulletin", "Secondary Data"),
        ("Heights of 30 plants measured weekly using a measuring tape in an agricultural experiment", "Primary Data"),
        ("Railway ticket booking statistics downloaded from the IRCTC annual press release", "Secondary Data")
    ],
    'tmpls': [
        "Classify the nature of the data collected in this scenario: '{0}':",
        "Determine whether the following is Primary Data or Secondary Data: '{0}':",
        "Identify the data category for the investigation: '{0}':",
        "In statistical analysis, what type of data is represented by: '{0}'?",
        "Assess the collection method for: '{0}':",
        "Which classification applies to this inquiry: '{0}'?",
        "Categorize the origin of data in this study: '{0}':",
        "State the data classification for the project: '{0}':",
        "Under statistical definitions, classify: '{0}':",
        "Specify the data category represented by: '{0}':"
    ],
    'calc': lambda item: (
        item[1],
        ["Secondary Data" if item[1] == "Primary Data" else "Primary Data", "Hypothetical Extrapolation", "Synthetic Simulation"],
        f"Explanation: '{item[0]}' represents {item[1]} because of how the data was acquired."
    ),
    'diff': 'easy'
})

# Arch 3: Qualitative vs Quantitative Data
archs_711.append({
    'data': [
        ("Data that can be numerically measured and expressed in numbers (e.g. height, weight, marks) is:", "Quantitative Data", ["Qualitative Descriptive Attribute", "Unordered Subjective Category", "Nominal Label Classification"]),
        ("Characteristics or attributes that cannot be measured on a numerical scale (e.g. honesty, beauty, intelligence) are:", "Qualitative Data (Attributes)", ["Quantitative Data", "Continuous Variate", "Discrete Frequency"]),
        ("Which of the following represents quantitative data?", "Scores of students in a 100-mark mathematics examination", ["Favorite color of clothing", "Level of customer satisfaction (satisfied/dissatisfied)", "Eye color of children in a kindergarten"]),
        ("Which of the following represents qualitative data?", "Grades of honesty or artistic creativity awarded in a competition", ["Number of pages in a textbook", "Temperature of boiling water in degrees Celsius", "Distance traveled in kilometers"]),
        ("Variables that can take any real value within a continuous interval (e.g. weight, time) are:", "Continuous Variables", ["Discrete Variables", "Qualitative Attributes", "Categorical Factors"]),
        ("Variables that can take only isolated, specific distinct values (usually whole numbers, e.g. number of siblings) are:", "Discrete Variables", ["Continuous Variables", "Infinite Variates", "Interval Decimals"]),
        ("The number of cars passing a traffic toll booth in one hour is an example of a:", "Discrete Quantitative Variable", ["Continuous Quantitative Variable", "Qualitative Attribute", "Subjective Quality"]),
        ("The exact time taken by a swimmer to complete 50 meters (e.g. 24.38 seconds) is an example of a:", "Continuous Quantitative Variable", ["Discrete Variable", "Qualitative Attribute", "Nominal Category"]),
        ("The blood pressure reading of a patient measured in mmHg is a:", "Quantitative Variable", ["Qualitative Attribute", "Subjective Factor", "Nominal Label"]),
        ("Customer feedback categorized as 'Poor', 'Average', 'Good', 'Excellent' represents:", "Qualitative / Categorical Data", ["Continuous Numerical Metric", "Discrete Integer Metric", "Exact Ratio Scale"])
    ],
    'tmpls': [
        "In data categorization: {0}",
        "Understanding variable types: {0}",
        "Core distinction in statistical variables: {0}",
        "Classification of statistical data: {0}",
        "Identifying variable characteristics: {0}",
        "Statistical theory concept: {0}",
        "Quantitative vs qualitative insight: {0}",
        "Variable classification rule: {0}",
        "Basic nature of statistical variables: {0}",
        "Fundamentals of statistical metrics: {0}"
    ],
    'calc': lambda item: (
        item[1],
        item[2],
        f"Explanation: In statistics, {item[1]}."
    ),
    'diff': 'medium'
})

# Arch 4: Raw data and Array formation
archs_711.append({
    'data': [
        ([15, 22, 18, 12, 25, 19, 21, 14], 12, 25),
        ([45, 52, 38, 65, 41, 58, 32, 60], 32, 65),
        ([72, 85, 68, 91, 74, 88, 63, 95], 63, 95),
        ([10, 24, 18, 35, 12, 29, 40, 15], 10, 40),
        ([55, 62, 48, 70, 51, 68, 44, 75], 44, 75),
        ([80, 92, 75, 88, 71, 95, 66, 99], 66, 99),
        ([25, 38, 20, 45, 29, 42, 18, 50], 18, 50),
        ([60, 72, 54, 81, 63, 77, 50, 85], 50, 85),
        ([33, 46, 28, 55, 38, 50, 24, 60], 24, 60),
        ([88, 96, 79, 92, 83, 99, 74, 95], 74, 99)
    ],
    'tmpls': [
        "Consider the raw data set: {0}. What is the range of this data (Range = Maximum value - Minimum value)?",
        "Find the range of the following observation list: {0}:",
        "Calculate the range for the raw observations: {0}:",
        "If a data set consists of values {0}, what is the statistical range?",
        "Determine the range of the numerical data: {0}:",
        "What is the range of the raw scores: {0}?",
        "Compute the range of the observations given by: {0}:",
        "For the statistical data: {0}, calculate Range:",
        "Find the statistical range of the set: {0}:",
        "What is the difference between the maximum and minimum observations in: {0}?"
    ],
    'calc': lambda item: (
        f"{item[2] - item[1]} (Max: {item[2]}, Min: {item[1]})",
        [f"{item[2] - item[1] + 5}", f"{item[2] - item[1] - 4}", f"{item[2] + item[1]}"],
        f"Step 1: Identify maximum value = {item[2]} and minimum value = {item[1]}.\nStep 2: Range = Maximum - Minimum = {item[2]} - {item[1]}.\nStep 3: Range = {item[2] - item[1]}."
    ),
    'diff': 'easy'
})

# Arch 5: Frequency distribution table basics (Tally marks)
archs_711.append({
    'data': [
        (4, "four vertical bars (||||)"),
        (5, "a bundle of five (four vertical bars crossed diagonally: <s>||||</s>)"),
        (7, "one bundle of five plus two vertical bars (<s>||||</s> ||)"),
        (9, "one bundle of five plus four vertical bars (<s>||||</s> ||||)"),
        (10, "two bundles of five (<s>||||</s> <s>||||</s>)"),
        (12, "two bundles of five plus two vertical bars (<s>||||</s> <s>||||</s> ||)"),
        (14, "two bundles of five plus four vertical bars (<s>||||</s> <s>||||</s> ||||)"),
        (15, "three complete bundles of five (<s>||||</s> <s>||||</s> <s>||||</s>)"),
        (8, "one bundle of five plus three vertical bars (<s>||||</s> |||)"),
        (13, "two bundles of five plus three vertical bars (<s>||||</s> <s>||||</s> |||)")
    ],
    'tmpls': [
        "In a frequency distribution table, how is the count/frequency of {0} represented using standard tally marks?",
        "What is the standard tally mark representation for a frequency of {0}?",
        "How is the number {0} recorded using tally marks in statistical tables?",
        "Identify the correct tally mark notation for count {0}:",
        "In tally mark notation, the frequency {0} is depicted as:",
        "Which tally mark group corresponds to a frequency of {0}?",
        "Determine the tally mark representation for frequency = {0}:",
        "How do tally marks denote an observation count of {0}?",
        "State the tally mark structure for an occurrence count of {0}:",
        "What does the tally mark display look like for frequency {0}?"
    ],
    'calc': lambda item: (
        item[1],
        ["one continuous horizontal line", f"{item[0]} unbundled scattered dots", "a single circular symbol"],
        f"Explanation: In standard statistical tally notation, counts are grouped into bundles of five. For {item[0]}, it is {item[1]}."
    ),
    'diff': 'easy'
})

# Arch 6: Sample vs Population concepts
archs_711.append({
    'data': [
        ("The entire collection of all individuals, items, or units under consideration in a statistical inquiry is called:", "Population (or Universe)", ["Sample", "Class Interval", "Variance"]),
        ("A smaller representative subset selected from the total population to infer characteristics of the whole is called:", "Sample", ["Population", "Census", "Quartile"]),
        ("When data is gathered from every single unit of the entire population, the survey is called a:", "Complete Enumeration Survey (Census)", ["Sample Survey", "Pilot Study", "Case Study"]),
        ("Why are sample surveys used much more frequently than complete census surveys?", "Because studying a sample requires vastly less time, cost, and manpower while providing high accuracy", ["Because census surveys are illegal", "Because samples always examine 100% of citizens", "Because samples produce zero numbers"]),
        ("What quality must a sample possess to provide reliable inferences about the population?", "It must be representative and unbiased", ["It must contain only the tallest people", "It must be selected from a single street", "It must ignore all women and children"]),
        ("Selecting students randomly from every class of a school to study average study hours is an example of:", "Representative Sampling", ["Complete Census", "Biased Guesswork", "Census Enumeration"]),
        ("Testing a spoonful of soup to judge the flavor of the entire cooking pot represents the principle of:", "Sampling (Sample representing Population)", ["Complete Census Enumeration", "Secondary Data Compilation", "Qualitative Survey"]),
        ("What is the main risk of using a sample that is too small or biased?", "The sample may not represent the population accurately, leading to erroneous conclusions", ["The sample will cost more than a complete census", "The data can never be written in numbers", "All calculators will display errors"]),
        ("The Decennial Census of India conducted every ten years is an example of a:", "Population Census (Complete Enumeration)", ["Sample Survey of 100 people", "Laboratory Experiment", "Private Commercial Survey"]),
        ("In exit polls conducted on voting day, interviewing a few thousand voters to predict election results is an example of:", "Sample Survey", ["Complete Population Census", "Desk Research", "Archival Record"])
    ],
    'tmpls': [
        "In sampling and survey theory: {0}",
        "Understanding sample and population: {0}",
        "Core survey methodology concept: {0}",
        "Statistical inference principle: {0}",
        "Evaluating survey designs: {0}",
        "Key concept in statistical sampling: {0}",
        "Theory of sampling: {0}",
        "Basic principle of statistical investigation: {0}",
        "Sampling versus census: {0}",
        "Fundamentals of population studies: {0}"
    ],
    'calc': lambda item: (
        item[1],
        item[2],
        f"Explanation: In statistical methodology, {item[1]}."
    ),
    'diff': 'foundation'
})

# Arch 7: Calculating Total Frequency from a grouped table
archs_711.append({
    'data': [
        ([5, 8, 12, 10, 5], 40),
        ([4, 9, 15, 11, 6], 45),
        ([6, 11, 14, 12, 7], 50),
        ([3, 7, 10, 8, 2], 30),
        ([8, 12, 18, 14, 8], 60),
        ([5, 10, 16, 12, 7], 50),
        ([7, 13, 20, 15, 10], 65),
        ([6, 8, 11, 9, 6], 40),
        ([4, 6, 12, 10, 8], 40),
        ([9, 14, 21, 16, 10], 70)
    ],
    'tmpls': [
        "A frequency table has class frequencies: {0}. What is the total number of observations (N = Σf)?",
        "Calculate the total frequency N for the class distribution: {0}:",
        "Find the total number of data values N when class frequencies are: {0}:",
        "If the frequencies across classes are {0}, compute the sum of frequencies (N = Σf):",
        "Determine the total frequency N given frequencies: {0}:",
        "What is the total sample size N from the frequency list: {0}?",
        "Compute the sum of frequencies N for: {0}:",
        "For a grouped distribution with frequencies {0}, calculate N = Σf:",
        "Find the aggregate frequency N for: {0}:",
        "What is the sum of all frequencies in the distribution: {0}?"
    ],
    'calc': lambda item: (
        f"{sum(item[0])}",
        [f"{sum(item[0]) + 5}", f"{sum(item[0]) - 4}", f"{sum(item[0]) + 10}"],
        f"Step 1: Formula: N = Σf.\nStep 2: Add all frequencies: {' + '.join(str(x) for x in item[0])}.\nStep 3: Total N = {sum(item[0])}."
    ),
    'diff': 'easy'
})

qs_711 = generate_subtopic(tc_711, tn_711, CH_NUM, CH_NAME, archs_711)
all_qs.extend(qs_711)
print(f"Generated {len(qs_711)} for {tc_711}")

# ==============================================================================
# 7.1.2: Class intervals: Inclusive (discrete) vs Exclusive (continuous) method
# ==============================================================================
tc_712 = "MH-9-MTH1-7-7.1.2"
tn_712 = "Class intervals: Inclusive (discrete) vs Exclusive (continuous) method"
archs_712 = []

# Arch 0: Identifying Exclusive (Continuous) method
archs_712.append({
    'data': [
        ("0-10, 10-20, 20-30, 30-40", "Exclusive (Continuous) method: upper limit of one class is the lower limit of the next class"),
        ("10-20, 20-30, 30-40, 40-50", "Exclusive (Continuous) method: continuous intervals without gaps between classes"),
        ("20-25, 25-30, 30-35, 35-40", "Exclusive (Continuous) method: observation equal to upper limit is excluded from that class and included in the next"),
        ("0-5, 5-10, 10-15, 15-20", "Exclusive (Continuous) method: seamless continuity between adjacent classes"),
        ("50-60, 60-70, 70-80, 80-90", "Exclusive (Continuous) method: suitable for continuous variables like height, weight, time"),
        ("100-150, 150-200, 200-250, 250-300", "Exclusive (Continuous) method: no correction factor needed for graphical representation"),
        ("25-30, 30-35, 35-40, 40-45", "Exclusive (Continuous) method: upper boundary touches next lower boundary"),
        ("40-60, 60-80, 80-100, 100-120", "Exclusive (Continuous) method: boundary values overlap seamlessly"),
        ("15-20, 20-25, 25-30, 30-35", "Exclusive (Continuous) method: upper limit observation is counted in the succeeding class"),
        ("70-80, 80-90, 90-100, 100-110", "Exclusive (Continuous) method: standard format required for drawing histograms")
    ],
    'tmpls': [
        "In grouping data, classes are written as '{0}'. Which method of classification does this represent?",
        "Identify the classification method for the classes '{0}':",
        "Classes formatted as '{0}' belong to which classification type?",
        "What type of class interval system is exemplified by '{0}'?",
        "Determine the grouping method represented by '{0}':",
        "Which classification standard is illustrated by '{0}'?",
        "Class intervals structured as '{0}' are known as:",
        "Evaluate the class interval pattern '{0}':",
        "Under statistical terminology, '{0}' represents:",
        "State the classification method used for classes '{0}':"
    ],
    'calc': lambda item: (
        item[1],
        ["Inclusive (Discrete) method where both limits are included", "Open-ended distribution without upper boundaries", "Unequal class width irregular system"],
        f"Explanation: In classes '{item[0]}', {item[1]}."
    ),
    'diff': 'easy'
})

# Arch 1: Identifying Inclusive (Discrete) method
archs_712.append({
    'data': [
        ("1-10, 11-20, 21-30, 31-40", "Inclusive (Discrete) method: both lower limit and upper limit are included in the same class"),
        ("10-19, 20-29, 30-39, 40-49", "Inclusive (Discrete) method: there is a gap of 1 unit between the upper limit of one class and lower limit of next"),
        ("21-25, 26-30, 31-35, 36-40", "Inclusive (Discrete) method: discrete classes with gap between adjacent intervals"),
        ("1-5, 6-10, 11-15, 16-20", "Inclusive (Discrete) method: upper limit observation is retained inside the class"),
        ("51-60, 61-70, 71-80, 81-90", "Inclusive (Discrete) method: requires boundary correction to make continuous for histograms"),
        ("101-150, 151-200, 201-250, 251-300", "Inclusive (Discrete) method: separated by a discrete gap of 1 unit"),
        ("26-30, 31-35, 36-40, 41-45", "Inclusive (Discrete) method: non-overlapping class boundaries"),
        ("41-60, 61-80, 81-100, 101-120", "Inclusive (Discrete) method: common in reporting discrete whole number counts"),
        ("16-20, 21-25, 26-30, 31-35", "Inclusive (Discrete) method: both boundaries belong strictly to that interval"),
        ("71-80, 81-90, 91-100, 101-110", "Inclusive (Discrete) method: discrete intervals with gap of 1 unit")
    ],
    'tmpls': [
        "In statistical frequency tables, classes are given as '{0}'. Which classification method is this?",
        "Identify the classification method for '{0}':",
        "Classes structured as '{0}' are classified under which method?",
        "What type of grouping is represented by the classes '{0}'?",
        "Determine the classification system of '{0}':",
        "Which method of class intervals is used in '{0}'?",
        "The class distribution '{0}' follows which method?",
        "Evaluate the class structure in '{0}':",
        "Under statistical conventions, '{0}' is an example of:",
        "State the method of classification represented by '{0}':"
    ],
    'calc': lambda item: (
        item[1],
        ["Exclusive (Continuous) method where upper limit touches lower limit", "Open-ended frequency distribution", "Cumulative frequency polygon method"],
        f"Explanation: In classes '{item[0]}', {item[1]}."
    ),
    'diff': 'easy'
})

# Arch 2: Where does an observation equal to a boundary value go in Exclusive method?
archs_712.append({
    'data': [
        (20, "10-20 and 20-30", "Class 20-30 (in Exclusive method, value equal to upper limit is excluded from 10-20 and included in next class 20-30)"),
        (30, "20-30 and 30-40", "Class 30-40 (in Exclusive method, value 30 is included in 30-40, not 20-30)"),
        (15, "10-15 and 15-20", "Class 15-20 (excluded from 10-15, counted in 15-20)"),
        (25, "20-25 and 25-30", "Class 25-30 (included in 25-30, excluded from 20-25)"),
        (50, "40-50 and 50-60", "Class 50-60 (included in 50-60, excluded from 40-50)"),
        (40, "30-40 and 40-50", "Class 40-50 (counted in 40-50, excluded from 30-40)"),
        (60, "50-60 and 60-70", "Class 60-70 (included in 60-70, excluded from 50-60)"),
        (75, "70-75 and 75-80", "Class 75-80 (included in 75-80, excluded from 70-75)"),
        (100, "90-100 and 100-110", "Class 100-110 (included in 100-110, excluded from 90-100)"),
        (35, "30-35 and 35-40", "Class 35-40 (included in 35-40, excluded from 30-35)")
    ],
    'tmpls': [
        "In an exclusive continuous grouping with classes {1}, in which class interval is an observation of exactly {0} included?",
        "If an observation has a value of {0}, in which class interval ({1}) is it placed under the exclusive method?",
        "Under the exclusive method with classes {1}, where is the observation {0} recorded?",
        "In which class interval does the observation {0} fall when classes are {1}?",
        "Determine the correct class for an observation of {0} in the exclusive distribution {1}:",
        "An observation equals {0}. In the exclusive series {1}, which class contains it?",
        "For exclusive classes {1}, which class includes the data point {0}?",
        "Where is a score of {0} tallied when given exclusive classes {1}?",
        "Find the class interval that contains the observation {0} among {1}:",
        "Which class interval accommodates the value {0} in the continuous system {1}?"
    ],
    'calc': lambda item: (
        item[2],
        [f"Class {item[1].split(' and ')[0]} (included in lower class)", "Counted equally in both classes (0.5 in each)", "Excluded entirely from the frequency table"],
        f"Rule: In the Exclusive method, an observation equal to the upper limit of a class is excluded from that class and included in the next class as its lower limit.\nTherefore, {item[0]} belongs to {item[2]}."
    ),
    'diff': 'medium'
})

# Arch 3: Converting Inclusive class to True Class Boundaries (Continuous)
archs_712.append({
    'data': [
        ((11, 20), (10.5, 20.5)),
        ((21, 30), (20.5, 30.5)),
        ((31, 40), (30.5, 40.5)),
        ((41, 50), (40.5, 50.5)),
        ((51, 60), (50.5, 60.5)),
        ((1, 10), (0.5, 10.5)),
        ((61, 70), (60.5, 70.5)),
        ((71, 80), (70.5, 80.5)),
        ((81, 90), (80.5, 90.5)),
        ((91, 100), (90.5, 100.5))
    ],
    'tmpls': [
        "In an inclusive frequency table with gap 1, convert the class {0[0]}-{0[1]} into true continuous class boundaries:",
        "Find the true class boundaries (continuous limits) for the inclusive class {0[0]}-{0[1]}:",
        "What are the continuous class boundaries corresponding to the inclusive class {0[0]}-{0[1]}?",
        "Convert the discrete class interval {0[0]}-{0[1]} into an exclusive continuous boundary:",
        "Calculate the true class boundaries for {0[0]}-{0[1]} using the correction factor 0.5:",
        "Determine the continuous class interval for {0[0]}-{0[1]} in an inclusive series:",
        "Transform the inclusive class {0[0]}-{0[1]} into its true boundary form:",
        "For inclusive interval {0[0]}-{0[1]}, find the lower and upper class boundaries:",
        "What is the continuous boundary equivalent of inclusive class {0[0]}-{0[1]}?",
        "Convert inclusive interval {0[0]}-{0[1]} to continuous boundaries:"
    ],
    'calc': lambda item: (
        f"{item[1][0]} - {item[1][1]}",
        [f"{item[0][0]} - {item[0][1]} (unmodified)", f"{item[0][0] - 1} - {item[0][1] + 1}", f"{item[1][0] - 0.5} - {item[1][1] + 0.5}"],
        f"Step 1: Correction factor d = (Lower limit of next class - Upper limit of current class) / 2 = 1 / 2 = 0.5.\nStep 2: Lower boundary = Lower limit - 0.5 = {item[0][0]} - 0.5 = {item[1][0]}.\nStep 3: Upper boundary = Upper limit + 0.5 = {item[0][1]} + 0.5 = {item[1][1]}.\nResult: {item[1][0]} - {item[1][1]}."
    ),
    'diff': 'medium'
})

# Arch 4: Class Width (Size of class interval) calculation
archs_712.append({
    'data': [
        (10, 20), (20, 30), (30, 45), (50, 70), (100, 150),
        (25, 35), (40, 60), (70, 100), (120, 180), (35, 50)
    ],
    'tmpls': [
        "Find the class width (class size h) of the continuous class interval {0}-{1}:",
        "What is the width of the class interval {0}-{1}?",
        "Calculate class size (h = Upper limit - Lower limit) for class {0}-{1}:",
        "Determine the class width for the interval {0}-{1}:",
        "For the class interval {0}-{1}, compute the class width:",
        "How wide is the class interval {0}-{1}?",
        "Find the class size h of interval {0}-{1}:",
        "What is the length/size of class interval {0}-{1}?",
        "What is the size of the class interval spanning from {0} to {1}?",
        "Calculate the size of the class {0}-{1}:"
    ],
    'calc': lambda item: (
        f"{item[1] - item[0]}",
        [f"{item[1] - item[0] + 5}", f"{item[1] - item[0] - 2}", f"{(item[1] + item[0]) // 2}"],
        f"Step 1: Formula: Class Width h = Upper limit - Lower limit.\nStep 2: Subtract: {item[1]} - {item[0]}.\nStep 3: Class width = {item[1] - item[0]}."
    ),
    'diff': 'easy'
})

# Arch 5: Lower and Upper limits identification
archs_712.append({
    'data': [
        (15, 25), (30, 40), (45, 60), (20, 35), (50, 75),
        (10, 20), (60, 80), (80, 100), (100, 125), (40, 55)
    ],
    'tmpls': [
        "For the class interval {0}-{1}, state the lower class limit and upper class limit:",
        "Identify the lower limit and upper limit of the class interval {0}-{1}:",
        "In the class interval {0}-{1}, which values are the lower and upper limits?",
        "What are the lower and upper limits of the class interval {0}-{1}?",
        "Determine the lower class limit and upper class limit for {0}-{1}:",
        "Specify the lower and upper limits for the interval {0}-{1}:",
        "Find the lower limit and upper limit in class {0}-{1}:",
        "For interval {0}-{1}, identify: Lower Limit and Upper Limit:",
        "Which pair represents the lower and upper limits of {0}-{1}?",
        "State the boundary limits for the class {0}-{1}:"
    ],
    'calc': lambda item: (
        f"Lower limit = {item[0]}, Upper limit = {item[1]}",
        [f"Lower limit = {item[1]}, Upper limit = {item[0]}", f"Lower limit = {item[0] - 1}, Upper limit = {item[1] + 1}", f"Lower limit = 0, Upper limit = {item[1] - item[0]}"],
        f"Step 1: In the class interval notation {item[0]}-{item[1]}, the smaller value on the left is the Lower Limit.\nStep 2: The larger value on the right is the Upper Limit.\nStep 3: Lower limit = {item[0]}, Upper limit = {item[1]}."
    ),
    'diff': 'easy'
})

# Arch 6: Why are continuous classes required for Histograms?
archs_712.append({
    'data': [
        ("Why must inclusive classes be converted into continuous class boundaries before drawing a histogram?", "Because histograms have adjacent contiguous rectangles with no gaps between them", ["Because histograms only display circles", "Because inclusive classes have negative frequencies", "Because textbooks prohibit inclusive tables"]),
        ("What is the graphical representation of a continuous frequency distribution using adjacent vertical bars called?", "Histogram", ["Bar Graph with gaps", "Pie Chart", "Pictograph"]),
        ("What does the area of each rectangle in a histogram represent when class widths are equal?", "The frequency of the corresponding class interval", ["The class mark of the interval", "The cumulative percentage of the entire population", "The standard deviation"]),
        ("In a histogram, what is plotted along the horizontal X-axis?", "Continuous class boundaries", ["Class frequencies", "Cumulative percentages", "Tally marks"]),
        ("In a histogram, what is plotted along the vertical Y-axis?", "Class frequencies", ["Class boundaries", "Class marks", "Cumulative sums"]),
        ("What symbol is drawn on the X-axis near the origin when the first class interval does not begin at zero?", "A kink (crink / zig-zag break) symbol", ["A full black circle", "A dotted triangle", "An arrow pointing right"]),
        ("What does a kink (zig-zag line) on the horizontal axis indicate in a histogram?", "That the scale is broken and numbers between 0 and the first lower limit are omitted", ["That the graph has a mathematical error", "That frequencies are all equal to zero", "That the scale is logarithmic"]),
        ("How is a Frequency Polygon constructed from a histogram?", "By joining the mid-points of the tops of consecutive rectangles with straight line segments", ["By connecting the four corners of every rectangle", "By drawing a circle around the highest bar", "By joining the bottoms of the bars"]),
        ("What is the primary difference between a simple Bar Diagram and a Histogram?", "Bar diagrams have equal gaps between bars, whereas histogram rectangles touch each other without gaps", ["Bar diagrams are drawn horizontally only", "Histograms never use numbers", "Bar diagrams require continuous boundaries"]),
        ("Can a frequency polygon be drawn directly without first constructing a histogram?", "Yes, by plotting points (Class Mark, Frequency) and joining them with line segments", ["No, a histogram is legally mandatory before a polygon", "Yes, but only for qualitative attributes", "No, polygons can only be drawn with computers"])
    ],
    'tmpls': [
        "In statistical graphical representation: {0}",
        "Understanding histograms and polygons: {0}",
        "Core rule of graphical presentation: {0}",
        "Theory of histograms: {0}",
        "Constructing statistical graphs: {0}",
        "Evaluating graphical methods: {0}",
        "Key knowledge on histograms: {0}",
        "Graphical data analysis: {0}",
        "Visualizing frequency distributions: {0}",
        "Fundamentals of statistical charts: {0}"
    ],
    'calc': lambda item: (
        item[1],
        item[2],
        f"Explanation: In statistical visualization, {item[1]}."
    ),
    'diff': 'foundation'
})

# Arch 7: Finding the missing frequency given total frequency N
archs_712.append({
    'data': [
        ([5, 8, 12, 6], 40, "f"),
        ([7, 10, 15, 8], 50, "x"),
        ([4, 9, 11, 7], 35, "f"),
        ([6, 12, 14, 10], 50, "k"),
        ([8, 14, 16, 7], 55, "y"),
        ([5, 11, 13, 9], 45, "f"),
        ([9, 15, 20, 11], 65, "x"),
        ([6, 9, 12, 8], 40, "k"),
        ([4, 8, 10, 6], 32, "f"),
        ([10, 16, 22, 14], 75, "y")
    ],
    'tmpls': [
        "A frequency distribution has frequencies {0[0]}, {0[1]}, {2}, {0[2]}, and {0[3]}. If the total frequency N is {1}, find the missing frequency {2}:",
        "The frequencies of 5 classes are {0[0]}, {0[1]}, {2}, {0[2]}, and {0[3]}. Given total frequency N = {1}, calculate {2}:",
        "Find the unknown frequency {2} if the class frequencies are {0[0]}, {0[1]}, {2}, {0[2]}, {0[3]} and total N = {1}:",
        "If total frequency is {1} and known frequencies are {0[0]}, {0[1]}, {0[2]}, {0[3]}, compute missing frequency {2}:",
        "Determine the value of missing frequency {2} when total frequency N = {1} and other frequencies are {0[0]}, {0[1]}, {0[2]}, {0[3]}:",
        "What is the missing frequency {2} in a distribution of sum {1} with known values {0[0]}, {0[1]}, {0[2]}, {0[3]}?",
        "Calculate the unknown frequency {2} from total N = {1} and given frequencies {0[0]}, {0[1]}, {0[2]}, {0[3]}:",
        "For total observations N = {1}, find missing frequency {2} among {0[0]}, {0[1]}, {2}, {0[2]}, {0[3]}:",
        "Solve for missing frequency {2} where total N = {1} and known frequencies are {0[0]}, {0[1]}, {0[2]}, {0[3]}:",
        "Find the value of {2} in the frequency distribution with total N = {1} and components {0[0]}, {0[1]}, {2}, {0[2]}, {0[3]}:"
    ],
    'calc': lambda item: (
        f"{item[1] - sum(item[0])}",
        [f"{item[1] - sum(item[0]) + 3}", f"{item[1] - sum(item[0]) - 2}", f"{item[1] - sum(item[0]) + 7}"],
        f"Step 1: Formula: Total N = Sum of all frequencies.\nStep 2: {item[1]} = ({' + '.join(str(x) for x in item[0])}) + {item[2]} = {sum(item[0])} + {item[2]}.\nStep 3: {item[2]} = {item[1]} - {sum(item[0])} = {item[1] - sum(item[0])}."
    ),
    'diff': 'medium'
})

qs_712 = generate_subtopic(tc_712, tn_712, CH_NUM, CH_NAME, archs_712)
all_qs.extend(qs_712)
print(f"Generated {len(qs_712)} for {tc_712}")

# ==============================================================================
# 7.1.3: Class mark = (Lower limit + Upper limit)/2
# ==============================================================================
tc_713 = "MH-9-MTH1-7-7.1.3"
tn_713 = "Class mark = (Lower limit + Upper limit)/2"
archs_713 = []

# Arch 0: Class mark of continuous intervals (L + U) / 2
archs_713.append({
    'data': [
        (10, 20), (20, 30), (30, 40), (40, 50), (50, 60),
        (0, 10), (60, 70), (70, 80), (80, 90), (90, 100)
    ],
    'tmpls': [
        "What is the class mark of the class interval {0}-{1}?",
        "Find the class mark (mid-value) of the class {0}-{1}:",
        "Calculate the class mark for the interval {0}-{1}:",
        "Determine the class mark of class {0}-{1}:",
        "Compute the mid-point (class mark) of {0}-{1}:",
        "For the class interval {0}-{1}, what is the class mark?",
        "What value represents the class mark of {0}-{1}?",
        "Find the mid-value of the class interval {0}-{1}:",
        "Calculate the class mark for interval {0}-{1}:",
        "Identify the class mark corresponding to class {0}-{1}:"
    ],
    'calc': lambda item: (
        f"{(item[0] + item[1]) / 2:g}",
        [f"{((item[0] + item[1]) / 2) + 5:g}", f"{((item[0] + item[1]) / 2) - 4:g}", f"{item[1] - item[0]}"],
        f"Step 1: Formula: Class Mark = (Lower Limit + Upper Limit) / 2.\nStep 2: Substitute: ({item[0]} + {item[1]}) / 2 = {item[0] + item[1]} / 2.\nStep 3: Class Mark = {(item[0] + item[1]) / 2:g}."
    ),
    'diff': 'easy'
})

# Arch 1: Class mark of fractional / odd-sum intervals
archs_713.append({
    'data': [
        (10, 25), (25, 40), (15, 30), (35, 50), (5, 20),
        (20, 35), (45, 60), (55, 70), (65, 80), (75, 90)
    ],
    'tmpls': [
        "Calculate the class mark for the class interval {0}-{1}:",
        "Find the class mark of the interval {0}-{1}:",
        "What is the mid-point (class mark) of the class {0}-{1}?",
        "Determine the class mark for class {0}-{1}:",
        "Compute the class mark of interval {0}-{1}:",
        "For interval {0}-{1}, calculate the class mark:",
        "Find the class mark corresponding to {0}-{1}:",
        "What is the exact class mark of {0}-{1}?",
        "Calculate the mid-value for class {0}-{1}:",
        "Identify the class mark for interval {0}-{1}:"
    ],
    'calc': lambda item: (
        f"{(item[0] + item[1]) / 2:.1f}",
        [f"{((item[0] + item[1]) / 2) + 2:.1f}", f"{((item[0] + item[1]) / 2) - 3:.1f}", f"{item[1] - item[0]}"],
        f"Step 1: Formula: Class Mark = (Lower limit + Upper limit) / 2.\nStep 2: Calculate: ({item[0]} + {item[1]}) / 2 = {item[0] + item[1]} / 2.\nStep 3: Class Mark = {(item[0] + item[1]) / 2:.1f}."
    ),
    'diff': 'easy'
})

# Arch 2: Class mark of larger intervals (e.g. 100-150, 200-300)
archs_713.append({
    'data': [
        (100, 150), (150, 200), (200, 250), (250, 300), (300, 350),
        (100, 200), (200, 300), (300, 400), (400, 500), (500, 600)
    ],
    'tmpls': [
        "What is the class mark of the class interval {0}-{1}?",
        "Find the mid-value (class mark) of the interval {0}-{1}:",
        "Calculate the class mark for the class {0}-{1}:",
        "Determine the class mark of interval {0}-{1}:",
        "Compute the class mark for class {0}-{1}:",
        "For the class interval {0}-{1}, what is the class mark?",
        "What is the class mark representing the interval {0}-{1}?",
        "Find the class mark of interval {0}-{1}:",
        "Calculate the class mark for class interval {0}-{1}:",
        "Identify the class mark of {0}-{1}:"
    ],
    'calc': lambda item: (
        f"{(item[0] + item[1]) // 2}",
        [f"{((item[0] + item[1]) // 2) + 20}", f"{((item[0] + item[1]) // 2) - 25}", f"{item[1] - item[0]}"],
        f"Step 1: Class Mark = (Lower limit + Upper limit) / 2.\nStep 2: ({item[0]} + {item[1]}) / 2 = {item[0] + item[1]} / 2.\nStep 3: Class Mark = {(item[0] + item[1]) // 2}."
    ),
    'diff': 'easy'
})

# Arch 3: Given class mark and class width, find lower and upper limits
# Lower = Mid - h/2, Upper = Mid + h/2
archs_713.append({
    'data': [
        (25, 10), (35, 10), (45, 10), (55, 10), (65, 10),
        (50, 20), (70, 20), (90, 20), (150, 50), (250, 50)
    ],
    'tmpls': [
        "The class mark of a continuous class interval is {0} and its class width is {1}. Find the class interval:",
        "If class mark is {0} and class size is {1}, determine the class interval:",
        "Find the class interval whose mid-value is {0} and width is {1}:",
        "A class interval has mid-point {0} and class width {1}. What is the interval?",
        "Calculate the lower and upper limits of a class having class mark {0} and width {1}:",
        "Determine the continuous class interval with class mark = {0} and class size = {1}:",
        "What is the class interval having mid-value {0} and length {1}?",
        "Find the class whose class mark is {0} and class width is {1}:",
        "Identify the class interval with mid-point {0} and interval width {1}:",
        "Compute the class interval given class mark {0} and size {1}:"
    ],
    'calc': lambda item: (
        f"{item[0] - item[1]//2} - {item[0] + item[1]//2}",
        [f"{item[0] - item[1]} - {item[0] + item[1]}", f"{item[0]} - {item[0] + item[1]}", f"{item[0] - item[1]//2 - 5} - {item[0] + item[1]//2 + 5}"],
        f"Step 1: Lower limit = Class Mark - (Class Width / 2) = {item[0]} - ({item[1]} / 2) = {item[0]} - {item[1]//2} = {item[0] - item[1]//2}.\nStep 2: Upper limit = Class Mark + (Class Width / 2) = {item[0]} + {item[1]//2} = {item[0] + item[1]//2}.\nStep 3: Class Interval is {item[0] - item[1]//2} - {item[0] + item[1]//2}."
    ),
    'diff': 'medium'
})

# Arch 4: Given class mark and upper limit, find lower limit (Lower = 2 * Mid - Upper)
archs_713.append({
    'data': [
        (25, 30), (35, 40), (45, 50), (55, 60), (15, 20),
        (50, 60), (70, 80), (90, 100), (125, 150), (175, 200)
    ],
    'tmpls': [
        "The class mark of a class interval is {0} and its upper limit is {1}. Find its lower limit:",
        "If the mid-value of a class is {0} and upper limit is {1}, calculate the lower limit:",
        "Find the lower limit of a class having class mark {0} and upper limit {1}:",
        "What is the lower limit of a class interval with mid-point {0} and upper boundary {1}?",
        "Determine the lower class limit when class mark = {0} and upper limit = {1}:",
        "Calculate the lower limit for a class whose class mark is {0} and upper limit is {1}:",
        "For a class with mid-value {0} and upper limit {1}, find the lower limit:",
        "Compute the lower limit of the class interval with class mark {0} and upper limit {1}:",
        "Identify the lower limit of a class having mid-point {0} and upper limit {1}:",
        "Find the lower boundary of an interval whose class mark is {0} and upper limit is {1}:"
    ],
    'calc': lambda item: (
        f"{2 * item[0] - item[1]}",
        [f"{2 * item[0] - item[1] + 5}", f"{2 * item[0] - item[1] - 4}", f"{item[1] - item[0]}"],
        f"Step 1: Formula: Class Mark = (Lower + Upper) / 2 => Lower = 2 * Class Mark - Upper.\nStep 2: Lower = 2 * {item[0]} - {item[1]} = {2 * item[0]} - {item[1]}.\nStep 3: Lower limit = {2 * item[0] - item[1]}."
    ),
    'diff': 'medium'
})

# Arch 5: Given class mark and lower limit, find upper limit (Upper = 2 * Mid - Lower)
archs_713.append({
    'data': [
        (25, 20), (35, 30), (45, 40), (55, 50), (15, 10),
        (50, 40), (70, 60), (90, 80), (125, 100), (175, 150)
    ],
    'tmpls': [
        "The class mark of a class interval is {0} and its lower limit is {1}. Find its upper limit:",
        "If the mid-point of a class is {0} and lower limit is {1}, calculate the upper limit:",
        "Find the upper limit of a class having class mark {0} and lower limit {1}:",
        "What is the upper limit of a class interval with class mark {0} and lower boundary {1}?",
        "Determine the upper class limit when class mark = {0} and lower limit = {1}:",
        "Calculate the upper limit for a class whose class mark is {0} and lower limit is {1}:",
        "For a class with mid-value {0} and lower limit {1}, find the upper limit:",
        "Compute the upper limit of the class interval with class mark {0} and lower limit {1}:",
        "Identify the upper limit of a class having mid-point {0} and lower limit {1}:",
        "Find the upper boundary of an interval whose class mark is {0} and lower limit is {1}:"
    ],
    'calc': lambda item: (
        f"{2 * item[0] - item[1]}",
        [f"{2 * item[0] - item[1] + 5}", f"{2 * item[0] - item[1] - 6}", f"{item[0] + item[1]}"],
        f"Step 1: Formula: Class Mark = (Lower + Upper) / 2 => Upper = 2 * Class Mark - Lower.\nStep 2: Upper = 2 * {item[0]} - {item[1]} = {2 * item[0]} - {item[1]}.\nStep 3: Upper limit = {2 * item[0] - item[1]}."
    ),
    'diff': 'medium'
})

# Arch 6: Consecutive class marks difference equals class width
archs_713.append({
    'data': [
        ([15, 25, 35, 45], 10),
        ([12, 17, 22, 27], 5),
        ([20, 40, 60, 80], 20),
        ([125, 175, 225, 275], 50),
        ([10, 16, 22, 28], 6),
        ([50, 65, 80, 95], 15),
        ([100, 200, 300, 400], 100),
        ([14, 21, 28, 35], 7),
        ([30, 42, 54, 66], 12),
        ([25, 33, 41, 49], 8)
    ],
    'tmpls': [
        "The consecutive class marks of a frequency distribution are {0}. What is the class width (class size h)?",
        "If class marks of consecutive classes are {0}, determine the class size:",
        "Find the class width of a distribution having consecutive class marks {0}:",
        "What is the uniform class size for classes with mid-values {0}?",
        "Calculate the class width given the sequential class marks {0}:",
        "Given consecutive class marks {0}, find the class interval width:",
        "Determine the class size h from the series of class marks: {0}:",
        "For a distribution with class marks {0}, what is the width of each class?",
        "Compute the class size h from consecutive class marks {0}:",
        "Find the class interval size from the sequence of class marks {0}:"
    ],
    'calc': lambda item: (
        f"{item[1]} (Difference between consecutive class marks: {item[0][1]} - {item[0][0]})",
        [f"{item[1] + 4}", f"{item[1] - 3}", f"{item[0][0]}"],
        f"Step 1: In a uniform distribution, Class Width h equals the difference between any two consecutive class marks.\nStep 2: Subtract: {item[0][1]} - {item[0][0]} = {item[1]}.\nStep 3: Class width = {item[1]}."
    ),
    'diff': 'easy'
})

# Arch 7: Purpose and role of Class Mark in calculating Mean
archs_713.append({
    'data': [
        ("Why is the class mark (mid-value x_i) calculated for each class in grouped data?", "It serves as the single representative numerical value of the class for computing the mean (Σf*x / N)", ["It is used to color the bars of a histogram", "It replaces the total frequency N", "It eliminates the need for tally marks"]),
        ("In the direct method of calculating the mean of grouped data, what does x_i represent?", "The class mark of the i-th class interval", ["The frequency of the i-th class", "The lower limit of the first class", "The range of the entire data set"]),
        ("What is the formula for the class mark of an interval with lower limit L and upper limit U?", "Class Mark = (L + U) / 2", ["Class Mark = (U - L) / 2", "Class Mark = L * U", "Class Mark = U - L"]),
        ("Does the class mark depend on whether the class intervals are inclusive or exclusive?", "No, the mid-value formula (L + U)/2 gives the exact middle point in both systems", ["Yes, inclusive classes have zero class mark", "Yes, exclusive classes double the class mark", "Yes, class marks exist only for inclusive classes"]),
        ("In a frequency polygon, what are the coordinates of the plotted points?", "(Class Mark, Class Frequency)", ["(Lower Limit, Upper Limit)", "(Class Frequency, Cumulative Frequency)", "(Class Width, Range)"]),
        ("What assumption is made when replacing a class interval with its class mark in mean calculation?", "Observations within the class are uniformly distributed and symmetrically centered around the mid-value", ["All observations in the class are equal to zero", "All observations in the class equal the maximum limit", "No observations actually exist inside the class"]),
        ("What is the class mark of the class 0-10?", "5", ["0", "10", "50"]),
        ("If class mark is 15 and class width is 10, what is the lower limit?", "10", ["5", "15", "20"]),
        ("If class mark is 15 and class width is 10, what is the upper limit?", "20", ["15", "25", "30"]),
        ("Can a class mark be a decimal or fraction?", "Yes, when the sum of lower and upper limits is an odd number (e.g., (10+25)/2 = 17.5)", ["No, class marks must always be round integers", "No, decimals are forbidden in statistics", "Only if approved by court order"])
    ],
    'tmpls': [
        "In statistical calculations: {0}",
        "Understanding the class mark: {0}",
        "Core role of class mid-points: {0}",
        "Statistical theory of grouped data: {0}",
        "Evaluating class mark properties: {0}",
        "Key knowledge on class marks: {0}",
        "Grouped data representation: {0}",
        "Mathematical property of class marks: {0}",
        "Principles of grouped frequency: {0}",
        "Fundamentals of class mark usage: {0}"
    ],
    'calc': lambda item: (
        item[1],
        item[2],
        f"Explanation: In statistics, {item[1]}."
    ),
    'diff': 'foundation'
})

qs_713 = generate_subtopic(tc_713, tn_713, CH_NUM, CH_NAME, archs_713)
all_qs.extend(qs_713)
print(f"Generated {len(qs_713)} for {tc_713}")

# ==============================================================================
# 7.2.1: Running cumulative sum (Less than type vs More than type cumulative frequency)
# ==============================================================================
tc_721 = "MH-9-MTH1-7-7.2.1"
tn_721 = "Running cumulative sum"
archs_721 = []

# Arch 0: Less than type cumulative frequency calculation (running sum from top)
archs_721.append({
    'data': [
        ([4, 7, 10, 6], [4, 11, 21, 27]),
        ([5, 8, 12, 9], [5, 13, 25, 34]),
        ([3, 6, 11, 8], [3, 9, 20, 28]),
        ([6, 10, 14, 8], [6, 16, 30, 38]),
        ([8, 12, 15, 10], [8, 20, 35, 45]),
        ([5, 9, 13, 7], [5, 14, 27, 34]),
        ([7, 11, 16, 12], [7, 18, 34, 46]),
        ([4, 8, 14, 10], [4, 12, 26, 36]),
        ([6, 9, 15, 11], [6, 15, 30, 41]),
        ([5, 10, 18, 12], [5, 15, 33, 45])
    ],
    'tmpls': [
        "A distribution has consecutive class frequencies: {0}. Calculate the 'less than type' cumulative frequencies:",
        "Find the running 'less than' cumulative frequencies for class frequencies {0}:",
        "What are the cumulative frequencies (less than type) for frequencies {0}?",
        "Compute the 'less than type' cumulative frequency series for: {0}:",
        "Determine the cumulative frequency column (less than type) for frequencies {0}:",
        "For class frequencies {0}, calculate the less-than cumulative sum:",
        "What is the running cumulative frequency (less than type) corresponding to {0}?",
        "Calculate the cumulative frequencies of less-than type for: {0}:",
        "Find the less than cumulative frequency list for frequencies {0}:",
        "Derive the less than type cumulative frequency column for: {0}:"
    ],
    'calc': lambda item: (
        f"{', '.join(str(x) for x in item[1])}",
        [
            f"{', '.join(str(x) for x in item[0])} (simple frequencies)",
            f"{', '.join(str(x) for x in [item[1][0], item[1][1]+2, item[1][2]-1, item[1][3]+3])}",
            f"{', '.join(str(x) for x in reversed(item[1]))} (more than type)"
        ],
        f"Step 1: 'Less than' cumulative frequency is obtained by adding frequencies sequentially from the top.\nStep 2: 1st = {item[0][0]}; 2nd = {item[0][0]} + {item[0][1]} = {item[1][1]}; 3rd = {item[1][1]} + {item[0][2]} = {item[1][2]}; 4th = {item[1][2]} + {item[0][3]} = {item[1][3]}.\nStep 3: Result: {', '.join(str(x) for x in item[1])}."
    ),
    'diff': 'medium'
})

# Arch 1: More than type cumulative frequency calculation (running sum from bottom)
archs_721.append({
    'data': [
        ([4, 7, 10, 6], [27, 23, 16, 6]),
        ([5, 8, 12, 9], [34, 29, 21, 9]),
        ([3, 6, 11, 8], [28, 25, 19, 8]),
        ([6, 10, 14, 8], [38, 32, 22, 8]),
        ([8, 12, 15, 10], [45, 37, 25, 10]),
        ([5, 9, 13, 7], [34, 29, 20, 7]),
        ([7, 11, 16, 12], [46, 39, 28, 12]),
        ([4, 8, 14, 10], [36, 32, 24, 10]),
        ([6, 9, 15, 11], [41, 35, 26, 11]),
        ([5, 10, 18, 12], [45, 40, 30, 12])
    ],
    'tmpls': [
        "A distribution has class frequencies: {0}. Calculate the 'more than type' cumulative frequencies from the first class to the last class:",
        "Find the 'more than type' cumulative frequencies corresponding to class frequencies {0}:",
        "What is the 'more than type' cumulative frequency series for frequencies {0}?",
        "Compute the running 'more than' cumulative frequencies for: {0}:",
        "Determine the more than type cumulative frequency values for {0}:",
        "For class frequencies {0}, calculate the more-than cumulative distribution:",
        "What are the cumulative frequencies of more than type for: {0}?",
        "Calculate the more than type cumulative column for frequencies {0}:",
        "Find the more than cumulative frequency sequence for: {0}:",
        "Derive the more than type cumulative frequencies for: {0}:"
    ],
    'calc': lambda item: (
        f"{', '.join(str(x) for x in item[1])}",
        [
            f"{', '.join(str(x) for x in item[0])}",
            f"{', '.join(str(x) for x in reversed(item[1]))} (less than type)",
            f"{', '.join(str(x) for x in [item[1][0], item[1][1]-3, item[1][2]+2, item[1][3]-1])}"
        ],
        f"Step 1: 'More than' cumulative frequency starts with total N = {item[1][0]} at the first lower limit and subtracts preceding frequencies progressively.\nStep 2: Values: {', '.join(str(x) for x in item[1])}."
    ),
    'diff': 'medium'
})

# Arch 2: Meaning of the last entry in 'less than type' cumulative frequency
archs_721.append({
    'data': [
        (40, "Total number of observations (Total frequency N = 40)"),
        (50, "Total number of observations (Total frequency N = 50)"),
        (60, "Total number of observations (Total frequency N = 60)"),
        (35, "Total number of observations (Total frequency N = 35)"),
        (45, "Total number of observations (Total frequency N = 45)"),
        (55, "Total number of observations (Total frequency N = 55)"),
        (70, "Total number of observations (Total frequency N = 70)"),
        (80, "Total number of observations (Total frequency N = 80)"),
        (65, "Total number of observations (Total frequency N = 65)"),
        (75, "Total number of observations (Total frequency N = 75)")
    ],
    'tmpls': [
        "In a 'less than type' cumulative frequency table, the last cumulative frequency entry is {0}. What does this value signify?",
        "If the final entry in a less-than cumulative frequency column is {0}, what does it represent?",
        "What is represented by the last number {0} in a less than cumulative frequency table?",
        "In less-than cumulative frequency analysis, the final figure is {0}. What does this mean?",
        "Determine the meaning of the last cumulative frequency value {0}:",
        "The last row of a less-than cumulative frequency table shows {0}. What does this indicate?",
        "What statistical metric is equal to the terminal cumulative frequency {0}?",
        "Identify what the final less-than cumulative frequency of {0} represents:",
        "State the significance of the last entry {0} in a less-than cumulative column:",
        "What does the bottom-most cumulative frequency of {0} indicate?"
    ],
    'calc': lambda item: (
        item[1],
        ["The class mark of the final class", "The frequency of the first class only", "The arithmetic mean of all observations"],
        f"Rule: In a 'less than type' cumulative frequency table, the cumulative frequency of the last class is always equal to the sum of all frequencies (Total frequency N = Σf = {item[0]})."
    ),
    'diff': 'easy'
})

# Arch 3: Meaning of the first entry in 'more than type' cumulative frequency
archs_721.append({
    'data': [
        (50, "Total number of observations in the entire distribution (N = 50)"),
        (60, "Total number of observations in the entire distribution (N = 60)"),
        (40, "Total number of observations in the entire distribution (N = 40)"),
        (75, "Total number of observations in the entire distribution (N = 75)"),
        (80, "Total number of observations in the entire distribution (N = 80)"),
        (45, "Total number of observations in the entire distribution (N = 45)"),
        (65, "Total number of observations in the entire distribution (N = 65)"),
        (70, "Total number of observations in the entire distribution (N = 70)"),
        (55, "Total number of observations in the entire distribution (N = 55)"),
        (90, "Total number of observations in the entire distribution (N = 90)")
    ],
    'tmpls': [
        "In a 'more than type' cumulative frequency distribution, the very first entry is {0}. What does this represent?",
        "If the initial value in a more-than cumulative frequency column is {0}, what does it indicate?",
        "What does the top-most cumulative frequency {0} in a more-than distribution signify?",
        "In more-than cumulative tables, the first cumulative frequency is {0}. State its meaning:",
        "Identify what the top number {0} in a more-than cumulative frequency table represents:",
        "What is represented by the initial cumulative frequency {0} in more-than cumulative data?",
        "The first entry of a more-than cumulative frequency table reads {0}. What is this value?",
        "Determine what the top cumulative frequency {0} in more-than tables denotes:",
        "State the significance of the opening value {0} in a more-than cumulative distribution:",
        "What statistical quantity corresponds to the first entry {0} in more-than cumulative analysis?"
    ],
    'calc': lambda item: (
        item[1],
        ["The class mark of the first interval", "The frequency of the last class only", "The mode of the distribution"],
        f"Rule: In a 'more than type' cumulative frequency table, the first entry (corresponding to 'more than or equal to the lowest limit') always equals the Total frequency N = Σf = {item[0]}."
    ),
    'diff': 'easy'
})

# Arch 4: Recovering individual class frequency from cumulative frequency column
# f_i = cf_i - cf_{i-1}
archs_721.append({
    'data': [
        (15, 23, "3rd class"), (8, 17, "2nd class"), (22, 35, "4th class"),
        (12, 19, "2nd class"), (27, 42, "4th class"), (18, 29, "3rd class"),
        (31, 45, "5th class"), (14, 25, "3rd class"), (25, 38, "4th class"),
        (33, 48, "5th class")
    ],
    'tmpls': [
        "In a less-than cumulative table, the cumulative frequency of the preceding class is {0} and that of the {2} is {1}. What is the simple frequency of the {2}?",
        "If cumulative frequencies of consecutive classes are {0} and {1}, find the individual class frequency of the {2}:",
        "Calculate the simple frequency of the {2} given that its cumulative frequency is {1} and the prior cumulative frequency was {0}:",
        "The cumulative frequencies for two adjacent classes are {0} and {1}. What is the frequency of the {2}?",
        "Determine the class frequency of the {2} having cumulative frequency {1} when the previous cumulative sum is {0}:",
        "What is the frequency of the {2} if its less-than cf is {1} and the preceding cf is {0}?",
        "Find the individual frequency of the {2} with cumulative frequency {1} following a cumulative frequency of {0}:",
        "Compute the class frequency for the {2} whose cumulative frequency advances from {0} to {1}:",
        "Given previous cf = {0} and current cf = {1}, what is the frequency of the {2}?",
        "Calculate the specific frequency of the {2} where cumulative totals are {0} and {1}:"
    ],
    'calc': lambda item: (
        f"{item[1] - item[0]}",
        [f"{item[1] - item[0] + 3}", f"{item[1] - item[0] - 2}", f"{item[1] + item[0]}"],
        f"Step 1: Formula: Class Frequency f_i = Cumulative Frequency cf_i - Preceding Cumulative Frequency cf_{{i-1}}.\nStep 2: Subtract: {item[1]} - {item[0]}.\nStep 3: Class frequency = {item[1] - item[0]}."
    ),
    'diff': 'medium'
})

# Arch 5: Ogive curve concepts (Cumulative Frequency Polygon)
archs_721.append({
    'data': [
        ("What is the graphical curve of a cumulative frequency distribution called?", "Ogive (or Cumulative Frequency Curve)", ["Histogram", "Bar Chart", "Pie Diagram"]),
        ("At what point do the 'less than ogive' and 'more than ogive' curves intersect?", "At a point whose X-coordinate is the Median of the distribution", ["At the Mode", "At the Arithmetic Mean", "At the Y-axis origin (0,0)"]),
        ("In a 'less than ogive', which values are plotted on the horizontal X-axis?", "Upper class boundaries", ["Lower class boundaries", "Class marks", "Class widths"]),
        ("In a 'more than ogive', which values are plotted on the horizontal X-axis?", "Lower class boundaries", ["Upper class boundaries", "Class marks", "Tally frequencies"]),
        ("What is plotted on the vertical Y-axis for both types of ogives?", "Cumulative frequencies", ["Simple class frequencies", "Class sizes", "Percentage errors"]),
        ("What is the general shape of a 'less than ogive'?", "An elongated S-shape curve that rises from left to right (increasing function)", ["A horizontal flat line", "A curve that falls from left to right", "A closed circular ellipse"]),
        ("What is the general shape of a 'more than ogive'?", "A curve that slopes downwards from top-left to bottom-right (decreasing function)", ["A curve rising from bottom-left to top-right", "A vertical straight line", "A stepped square block"]),
        ("What statistical measure of central tendency can be determined graphically from the intersection of the two ogives?", "Median", ["Mean", "Standard Deviation", "Range"]),
        ("To find the median using only the 'less than ogive', at what value on the Y-axis do we draw a horizontal line to the curve?", "N / 2 (half of the total frequency N)", ["N (total frequency)", "N / 4", "3N / 4"]),
        ("Why are ogives particularly useful in educational and economic statistics?", "To easily read percentiles, quartiles, deciles, and the median directly from the graph", ["To compute the exact formula of variance", "To eliminate all negative numbers", "To print color photographs"])
    ],
    'tmpls': [
        "In cumulative graphical analysis: {0}",
        "Understanding ogive curves: {0}",
        "Core theory of cumulative frequency graphs: {0}",
        "Evaluating cumulative curves: {0}",
        "Key knowledge on ogive curves: {0}",
        "Graphical determination of median: {0}",
        "Properties of cumulative polygons: {0}",
        "Statistical visualization of cumulative data: {0}",
        "Characteristics of ogive curves: {0}",
        "Fundamentals of ogive graphing: {0}"
    ],
    'calc': lambda item: (
        item[1],
        item[2],
        f"Explanation: In statistical graphics, {item[1]}."
    ),
    'diff': 'foundation'
})

# Arch 6: Reading number of students scoring less than a threshold
archs_721.append({
    'data': [
        ("0-20: 5, 20-40: 12, 40-60: 18, 60-80: 10, 80-100: 5", 60, 35, "marks less than 60"),
        ("0-10: 4, 10-20: 8, 20-30: 15, 30-40: 11, 40-50: 7", 30, 27, "marks less than 30"),
        ("0-25: 6, 25-50: 14, 50-75: 20, 75-100: 10", 75, 40, "scores less than 75"),
        ("0-20: 8, 20-40: 15, 40-60: 22, 60-80: 11, 80-100: 4", 40, 23, "marks less than 40"),
        ("0-10: 3, 10-20: 7, 20-30: 12, 30-40: 14, 40-50: 6", 20, 10, "marks less than 20"),
        ("0-50: 10, 50-100: 25, 100-150: 35, 150-200: 15", 150, 70, "wages less than 150"),
        ("0-20: 7, 20-40: 13, 40-60: 21, 60-80: 9", 60, 41, "scores less than 60"),
        ("0-10: 5, 10-20: 10, 20-30: 16, 30-40: 9", 30, 31, "marks less than 30"),
        ("0-20: 6, 20-40: 11, 40-60: 17, 60-80: 12, 80-100: 4", 80, 46, "scores less than 80"),
        ("0-25: 8, 25-50: 16, 50-75: 24, 75-100: 12", 50, 24, "marks less than 50")
    ],
    'tmpls': [
        "In a test with score distribution: {0}. How many students scored {3}?",
        "From the frequency table: {0}, determine the number of candidates who obtained {3}:",
        "Based on the distribution: {0}, calculate how many individuals had {3}:",
        "Consider the score table: {0}. Find the cumulative number of students with {3}:",
        "In the given data: {0}, how many students achieved {3}?",
        "Using the frequency distribution: {0}, find the count of students scoring {3}:",
        "From the test results: {0}, compute the total number of students with {3}:",
        "Examine the grouped data: {0}. How many students scored {3}?",
        "According to the distribution: {0}, determine the total students with {3}:",
        "Evaluate the score table: {0}. What is the number of students having {3}?"
    ],
    'calc': lambda item: (
        f"{item[2]} students",
        [f"{item[2] + 5} students", f"{item[2] - 4} students", f"{item[2] + 12} students"],
        f"Step 1: 'Less than {item[1]}' represents the cumulative sum of frequencies of all classes with upper limits <= {item[1]}.\nStep 2: Sum the corresponding class frequencies.\nStep 3: Result = {item[2]} students."
    ),
    'diff': 'medium'
})

# Arch 7: Calculating percentage of observations below a threshold
archs_721.append({
    'data': [
        (25, 50, "50% (25 out of 50 students)"),
        (30, 60, "50% (30 out of 60 students)"),
        (20, 80, "25% (20 out of 80 students)"),
        (45, 60, "75% (45 out of 60 students)"),
        (35, 70, "50% (35 out of 70 students)"),
        (24, 40, "60% (24 out of 40 students)"),
        (32, 80, "40% (32 out of 80 students)"),
        (15, 50, "30% (15 out of 50 students)"),
        (48, 60, "80% (48 out of 60 students)"),
        (28, 40, "70% (28 out of 40 students)")
    ],
    'tmpls': [
        "If {0} students out of a total class of {1} scored less than 50 marks, what percentage of students scored less than 50?",
        "Find the percentage of students scoring below 50 when {0} out of {1} students fall in this range:",
        "What percent of the {1} students scored less than 50 marks if {0} students are below 50?",
        "Calculate the percentage of observations below the threshold where {0} out of {1} individuals qualify:",
        "Determine what percentage of students scored less than 50 given {0} out of {1} students:",
        "In a class of {1} students, {0} scored under 50. What is this proportion as a percentage?",
        "Compute the percentage of students scoring less than 50 marks ({0} out of {1}):",
        "What is the percentage of candidates having scores below 50 if {0} out of {1} students did so?",
        "Find the percentage equivalent of {0} students out of {1} scoring less than 50:",
        "Calculate the proportion as percentage for {0} out of {1} students scoring under 50:"
    ],
    'calc': lambda item: (
        item[2],
        [f"{(item[0]*100)//item[1] + 10}%", f"{(item[0]*100)//item[1] - 15}%", f"{(item[0]*100)//item[1] + 25}%"],
        f"Step 1: Formula: Percentage = (Favorable Cumulative Frequency / Total Frequency) * 100.\nStep 2: Calculate: ({item[0]} / {item[1]}) * 100.\nStep 3: Percentage = {item[2]}."
    ),
    'diff': 'easy'
})

qs_721 = generate_subtopic(tc_721, tn_721, CH_NUM, CH_NAME, archs_721)
all_qs.extend(qs_721)
print(f"Generated {len(qs_721)} for {tc_721}")

with open('scripts/mh9_mth1_ch7_temp.json', 'w', encoding='utf-8') as f:
    json.dump(all_qs, f, indent=2)
print("Saved temporary Ch 7 Part 1")
