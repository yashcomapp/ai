# scripts/build_cbse9_mgm_ch10_part2.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 10: How Quantities Combine: Understanding Data
Part 2:
- Subtopic 10.2.1: Class marks (Upper limit + Lower limit)/2
- Subtopic 10.2.2: Constructing frequency polygons with and without histograms
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 10
CH_NAME = "How Quantities Combine: Understanding Data"

# ==============================================================================
# SUBTOPIC 10.2.1: Class marks (Upper limit + Lower limit)/2
# ==============================================================================
def gen_10_2_1():
    tc = "CBSE-9-MGM-10-10.2.1"
    tname = "Class marks (Upper limit + Lower limit)/2"

    # Arch 0: Class mark formula for continuous classes
    arch0 = {
        'data': [
            ("10-20", 10, 20, 15, "(10 + 20) / 2 = 15"),
            ("25-35", 25, 35, 30, "(25 + 35) / 2 = 30"),
            ("40-60", 40, 60, 50, "(40 + 60) / 2 = 50"),
            ("100-120", 100, 120, 110, "(100 + 120) / 2 = 110"),
            ("0-10", 0, 10, 5, "(0 + 10) / 2 = 5"),
            ("15-25", 15, 25, 20, "(15 + 25) / 2 = 20"),
            ("70-90", 70, 90, 80, "(70 + 90) / 2 = 80"),
            ("130-150", 130, 150, 140, "(130 + 150) / 2 = 140"),
            ("55-65", 55, 65, 60, "(55 + 65) / 2 = 60"),
            ("80-100", 80, 100, 90, "(80 + 100) / 2 = 90")
        ],
        'tmpls': [
            "Calculate the class mark (mid-value) of the class interval {0}:",
            "What is the class mark for the interval {0}?",
            "Using the formula \\( \\text{{Class Mark}} = \\frac{{\\text{{Upper Limit}} + \\text{{Lower Limit}}}}{{2}} \\), evaluate for {0}:",
            "Find the midpoint value representing the class interval {0}:",
            "Determine the class mark of {0}:",
            "What numerical value is plotted on the horizontal axis for the class {0} in a frequency polygon?",
            "Compute the class mark \\( x_i \\) for the interval {0}:",
            "Evaluate the mid-value of: {0}:",
            "What is the class mark corresponding to: {0}?",
            "Find \\( x_i \\) for the continuous class {0}:"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            [f"{item[3] + 5}", f"{item[3] - 5}", f"{item[1]}"],
            f"**Step 1: Write down the class mark formula.**\n\\[ \\text{{Class Mark}} = \\frac{{\\text{{Upper Limit}} + \\text{{Lower Limit}}}}{{2}} \\]\n\n**Step 2: Substitute the limits of {item[0]}.**\n\\[ \\text{{Class Mark}} = {item[4]} = {item[3]} \\]\n\n**Step 3: State the answer.**\nThe class mark is {item[3]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Class marks for inclusive (discontinuous) classes
    arch1 = {
        'data': [
            ("1-10", 1, 10, 5.5, "(1 + 10) / 2 = 5.5"),
            ("11-20", 11, 20, 15.5, "(11 + 20) / 2 = 15.5"),
            ("21-30", 21, 30, 25.5, "(21 + 30) / 2 = 25.5"),
            ("31-40", 31, 40, 35.5, "(31 + 40) / 2 = 35.5"),
            ("6-10", 6, 10, 8.0, "(6 + 10) / 2 = 8.0"),
            ("16-20", 16, 20, 18.0, "(16 + 20) / 2 = 18.0"),
            ("41-50", 41, 50, 45.5, "(41 + 50) / 2 = 45.5"),
            ("51-60", 51, 60, 55.5, "(51 + 60) / 2 = 55.5"),
            ("101-110", 101, 110, 105.5, "(101 + 110) / 2 = 105.5"),
            ("71-80", 71, 80, 75.5, "(71 + 80) / 2 = 75.5")
        ],
        'tmpls': [
            "Find the class mark of the inclusive (discontinuous) class interval {0}:",
            "What is the class mark for the class: {0}?",
            "Calculate \\( \\frac{{\\text{{Upper}} + \\text{{Lower}}}}{{2}} \\) for the interval {0}:",
            "Determine the mid-value of the inclusive class: {0}:",
            "Compute the class mark for {0}:",
            "Evaluate the class mark of the group {0}:",
            "What midpoint represents the inclusive class {0}?",
            "Find the class mark for the group {0}:",
            "Calculate the mid-point of: {0}:",
            "Determine the class mark for: {0}:"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            [f"{item[3] + 1}", f"{item[3] - 1}", f"{int(item[3])}"],
            f"**Step 1: State the formula for class mark.**\n\\[ \\text{{Class Mark}} = \\frac{{\\text{{Upper Limit}} + \\text{{Lower Limit}}}}{{2}} \\]\n(Note: Whether using stated limits \\( ({item[1]}+{item[2]})/2 \\) or true boundaries \\( ({item[1]}-0.5 + {item[2]}+0.5)/2 \\), the class mark is identical).\n\n**Step 2: Calculate the value.**\n\\[ {item[4]} = {item[3]} \\]\n\n**Step 3: State the answer.**\nThe class mark is {item[3]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Finding class limits from given class marks and class size
    arch2 = {
        'data': [
            ("15, 25, 35, 45", 10, 15, "10-20", "Lower = 15 - 10/2 = 10, Upper = 15 + 10/2 = 20"),
            ("12, 17, 22, 27", 5, 12, "9.5-14.5", "Lower = 12 - 5/2 = 9.5, Upper = 12 + 5/2 = 14.5"),
            ("50, 60, 70, 80", 10, 50, "45-55", "Lower = 50 - 10/2 = 45, Upper = 50 + 10/2 = 55"),
            ("105, 115, 125, 135", 10, 105, "100-110", "Lower = 105 - 10/2 = 100, Upper = 105 + 10/2 = 110"),
            ("7.5, 12.5, 17.5, 22.5", 5, 7.5, "5-10", "Lower = 7.5 - 5/2 = 5, Upper = 7.5 + 5/2 = 10"),
            ("22, 28, 34, 40", 6, 22, "19-25", "Lower = 22 - 6/2 = 19, Upper = 22 + 6/2 = 25"),
            ("32, 42, 52, 62", 10, 32, "27-37", "Lower = 32 - 10/2 = 27, Upper = 32 + 10/2 = 37"),
            ("100, 150, 200, 250", 50, 100, "75-125", "Lower = 100 - 50/2 = 75, Upper = 100 + 50/2 = 125"),
            ("20, 24, 28, 32", 4, 20, "18-22", "Lower = 20 - 4/2 = 18, Upper = 20 + 4/2 = 22"),
            ("47, 52, 57, 62", 5, 47, "44.5-49.5", "Lower = 47 - 5/2 = 44.5, Upper = 47 + 5/2 = 49.5")
        ],
        'tmpls': [
            "The class marks of a distribution are: {0}. Find the class interval corresponding to the first class mark ({2}):",
            "Given consecutive class marks {0} with class size \\( h = {1} \\), what is the class interval for the mark {2}?",
            "If the class marks of a frequency distribution are {0}, determine the true class limits of the class with class mark {2}:",
            "Find the class interval corresponding to class mark {2} where class marks are {0}:",
            "What interval gives a class mark of {2} with class width {1}?",
            "Reconstruct the class interval for class mark {2} from the series {0}:",
            "Determine the class boundaries for class mark {2} (class size = {1}):",
            "From the class marks {0}, find the lower and upper limits of the class with midpoint {2}:",
            "Calculate the class limits for class mark {2}:",
            "Identify the class interval whose midpoint is {2} (class width = {1}):"
        ],
        'calc': lambda item: (
            item[3],
            [
                f"{float(item[2]) - float(item[1])}-{float(item[2])}",
                f"{float(item[2])}-{float(item[2]) + float(item[1])}",
                f"{int(float(item[2])) - 1}-{int(float(item[2])) + 1}"
            ],
            f"**Step 1: Find the class size \\( h \\).**\n\\( h = x_{{i+1}} - x_i = {item[1]} \\).\n\n**Step 2: Apply the class limits formulas.**\n\\[ \\text{{Lower Limit}} = x_i - \\frac{{h}}{{2}}, \\quad \\text{{Upper Limit}} = x_i + \\frac{{h}}{{2}} \\]\nFor \\( x_i = {item[2]} \\):\n{item[4]}.\n\n**Step 3: State the answer.**\nThe class interval is {item[3]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: The imaginary class intervals before the first and after the last (Frequency 0)
    arch3 = {
        'data': [
            ("10-20 to 50-60 (width 10)", "0-10", "60-70", "Class mark 5 and class mark 65, both with frequency 0"),
            ("20-30 to 60-70 (width 10)", "10-20", "70-80", "Class mark 15 and class mark 75, both with frequency 0"),
            ("100-150 to 300-350 (width 50)", "50-100", "350-400", "Class mark 75 and class mark 375, frequency 0"),
            ("5-10 to 25-30 (width 5)", "0-5", "30-35", "Class mark 2.5 and class mark 32.5, frequency 0"),
            ("40-50 to 80-90 (width 10)", "30-40", "90-100", "Class mark 35 and class mark 95, frequency 0"),
            ("15-25 to 55-65 (width 10)", "5-15", "65-75", "Class mark 10 and class mark 70, frequency 0"),
            ("30-45 to 75-90 (width 15)", "15-30", "90-105", "Class mark 22.5 and class mark 97.5, frequency 0"),
            ("200-250 to 450-500 (width 50)", "150-200", "500-550", "Class mark 175 and class mark 525, frequency 0"),
            ("12-18 to 36-42 (width 6)", "6-12", "42-48", "Class mark 9 and class mark 45, frequency 0"),
            ("50-70 to 110-130 (width 20)", "30-50", "130-150", "Class mark 40 and class mark 140, frequency 0")
        ],
        'tmpls': [
            "To complete a frequency polygon for distribution {0}, what imaginary classes with frequency 0 are added before the first and after the last class?",
            "Which two hypothetical class intervals (each with frequency 0) must be included to close the frequency polygon for: {0}?",
            "What are the preceding and succeeding class intervals added to close the polygon for: {0}?",
            "To make the area of a frequency polygon equal to the histogram for {0}, what extra classes with zero frequency are assumed?",
            "Identify the two boundary classes (frequency = 0) used to anchor the frequency polygon for: {0}:",
            "What class precedes the first interval to close the polygon on the horizontal axis for: {0}?",
            "Determine the zero-frequency class intervals for: {0}:",
            "In drawing a frequency polygon for {0}, which classes are joined to the X-axis?",
            "What extra intervals are needed to ground the frequency polygon for: {0}?",
            "Select the correct imaginary classes for: {0}:"
        ],
        'calc': lambda item: (
            f"Preceding: {item[1]}, Succeeding: {item[2]}",
            [
                f"Preceding: 0-0, Succeeding: 1000-1000",
                f"Preceding: {item[2]}, Succeeding: {item[1]}",
                "No extra classes are needed; polygons do not touch the X-axis"
            ],
            f"**Step 1: Determine the class width \\( h \\).**\nClass width is uniform across the distribution.\n\n**Step 2: Add one preceding class and one succeeding class of identical width with frequency 0.**\nPreceding class: {item[1]}; Succeeding class: {item[2]}.\n{item[3]}.\n\n**Step 3: State the answer.**\nPreceding: {item[1]}, Succeeding: {item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Relation between consecutive class marks and class size (h = x_{i+1} - x_i)
    arch4 = {
        'data': [
            ("10, 20, 30, 40", 10, "20 - 10 = 10"),
            ("15, 25, 35, 45", 10, "25 - 15 = 10"),
            ("12.5, 17.5, 22.5, 27.5", 5, "17.5 - 12.5 = 5"),
            ("105, 115, 125, 135", 10, "115 - 105 = 10"),
            ("22, 26, 30, 34", 4, "26 - 22 = 4"),
            ("50, 70, 90, 110", 20, "70 - 50 = 20"),
            ("7.5, 15, 22.5, 30", 7.5, "15 - 7.5 = 7.5"),
            ("100, 150, 200, 250", 50, "150 - 100 = 50"),
            ("35, 42, 49, 56", 7, "42 - 35 = 7"),
            ("14.5, 19.5, 24.5, 29.5", 5, "19.5 - 14.5 = 5")
        ],
        'tmpls': [
            "If the class marks of a continuous frequency distribution are {0}, what is the class size (class width)?",
            "From the given sequence of class marks {0}, find the class width \\( h \\):",
            "What is the class width if consecutive class marks are {0}?",
            "Calculate \\( h = x_{{i+1}} - x_i \\) for the class marks {0}:",
            "Determine the common difference between consecutive class marks in: {0}:",
            "Find the class size corresponding to the class marks: {0}:",
            "Evaluate the class width from the midpoint sequence: {0}:",
            "What is the size of each class interval for the class marks: {0}?",
            "Identify the class width from the midpoints: {0}:",
            "Calculate the class size for: {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{float(item[1]) + 2}", f"{float(item[1]) * 2}", f"{float(item[1]) / 2 if float(item[1]) > 2 else 1}"],
            f"**Step 1: State the relation between consecutive class marks and class size.**\nFor uniform continuous intervals, the class size \\( h \\) equals the difference between any two consecutive class marks: \\( h = x_{{i+1}} - x_i \\).\n\n**Step 2: Calculate the difference.**\n\\[ h = {item[2]} = {item[1]} \\]\n\n**Step 3: State the answer.**\nThe class size is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Class mark in grouped mean computation
    arch5 = {
        'data': [
            ("In calculating the mean of grouped data using \\( \\bar{x} = \\frac{\\sum f_i x_i}{\\sum f_i} \\), what does \\( x_i \\) represent?", "The class mark (midpoint) of the ith class interval", "Class mark as representative value of the interval"),
            ("Why is the class mark used as the representative value for an entire class interval?", "Because it is the central midpoint, assuming observations are distributed evenly across the interval", "Midpoint assumption"),
            ("If a class interval is 20-30 with frequency 8, what is its contribution \\( f_i x_i \\) to the sum?", "8 * 25 = 200", "f_i = 8, x_i = (20+30)/2 = 25, f_i x_i = 200"),
            ("If a class interval is 40-50 with frequency 10, what is \\( f_i x_i \\)?", "10 * 45 = 450", "f_i = 10, x_i = 45, f_i x_i = 450"),
            ("If a class interval is 10-20 with frequency 6, what is \\( f_i x_i \\)?", "6 * 15 = 90", "f_i = 6, x_i = 15, f_i x_i = 90"),
            ("If a class interval is 30-40 with frequency 5, what is \\( f_i x_i \\)?", "5 * 35 = 175", "f_i = 5, x_i = 35, f_i x_i = 175"),
            ("If a class interval is 0-10 with frequency 12, what is \\( f_i x_i \\)?", "12 * 5 = 60", "f_i = 12, x_i = 5, f_i x_i = 60"),
            ("If class marks are 15, 25, 35 with frequencies 4, 6, 10, what is \\( \\sum f_i x_i \\)?", "4*15 + 6*25 + 10*35 = 60 + 150 + 350 = 560", "Total f_i x_i sum"),
            ("In the same distribution (frequencies 4, 6, 10), what is the mean \\( \\bar{x} = 560 / 20 \\)?", "28", "560 / 20 = 28"),
            ("Does changing class limits while keeping class marks unchanged affect the value of \\( \\sum f_i x_i \\)?", "No, because the computation depends strictly on \\( f_i \\) and \\( x_i \\)", "Dependence solely on x_i")
        ],
        'tmpls': [
            "{0}",
            "In grouped data arithmetic calculations: {0}",
            "Calculate \\( f_i x_i \\) or analyze the role of class marks: {0}",
            "What is the mathematical value or meaning in: {0}?",
            "Determine the accurate product or definition: {0}",
            "Evaluate the contribution of class mark: {0}",
            "Find the required quantity: {0}",
            "In computing the mean of grouped distributions: {0}",
            "Select the accurate statistical result: {0}",
            "Regarding class marks and frequencies: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The lower limit of the interval",
                "The upper limit of the interval",
                "The class width of the interval"
            ] if not item[1].isdigit() and not "200" in item[1] and not "450" in item[1] and not "90" in item[1] and not "175" in item[1] and not "60" in item[1] and not "560" in item[1] else [
                "100",
                "300",
                "50"
            ],
            f"**Step 1: Determine the class mark \\( x_i = \\frac{{\\text{{Upper}} + \\text{{Lower}}}}{{2}} \\).**\n\n**Step 2: Multiply by class frequency \\( f_i \\).**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Class mark for decimal and open-ended intervals
    arch6 = {
        'data': [
            ("0.5-1.5", 0.5, 1.5, 1.0, "(0.5 + 1.5) / 2 = 1.0"),
            ("1.5-2.5", 1.5, 2.5, 2.0, "(1.5 + 2.5) / 2 = 2.0"),
            ("2.5-4.5", 2.5, 4.5, 3.5, "(2.5 + 4.5) / 2 = 3.5"),
            ("0.2-0.8", 0.2, 0.8, 0.5, "(0.2 + 0.8) / 2 = 0.5"),
            ("3.1-4.9", 3.1, 4.9, 4.0, "(3.1 + 4.9) / 2 = 4.0"),
            ("10.5-20.5", 10.5, 20.5, 15.5, "(10.5 + 20.5) / 2 = 15.5"),
            ("20.5-30.5", 20.5, 30.5, 25.5, "(20.5 + 30.5) / 2 = 25.5"),
            ("9.5-19.5", 9.5, 19.5, 14.5, "(9.5 + 19.5) / 2 = 14.5"),
            ("19.5-29.5", 19.5, 29.5, 24.5, "(19.5 + 29.5) / 2 = 24.5"),
            ("29.5-39.5", 29.5, 39.5, 34.5, "(29.5 + 39.5) / 2 = 34.5")
        ],
        'tmpls': [
            "Find the class mark of the decimal class interval: {0}:",
            "What is the mid-point of the class {0}?",
            "Calculate the class mark for: {0}:",
            "Determine the midpoint value for {0}:",
            "Compute \\( \\frac{{\\text{{Upper}} + \\text{{Lower}}}}{{2}} \\) for: {0}:",
            "Evaluate the class mark of the true limits: {0}:",
            "Find \\( x_i \\) for the interval: {0}:",
            "What is the class mark for the continuous boundaries {0}?",
            "Calculate the mid-point of: {0}:",
            "Determine the class mark of: {0}:"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            [f"{item[3] + 1.0}", f"{item[3] - 0.5}", f"{item[1]}"],
            f"**Step 1: Write down the class mark formula.**\n\\[ \\text{{Class Mark}} = \\frac{{\\text{{Upper Limit}} + \\text{{Lower Limit}}}}{{2}} \\]\n\n**Step 2: Substitute the decimal limits {item[0]}.**\n\\[ {item[4]} = {item[3]} \\]\n\n**Step 3: State the answer.**\nThe class mark is {item[3]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Conceptual invariants of class marks in NCERT Class 9
    arch7 = {
        'data': [
            ("What single property defines the class mark of any interval?", "It is the exact arithmetic mean (midpoint) of the upper and lower limits of that class", "Definition of class mark"),
            ("If both the lower and upper limits of a class interval are increased by 5, what happens to the class mark?", "The class mark increases by exactly 5", "Shift property of midpoints"),
            ("If both limits of a class interval are multiplied by 2, what happens to the class mark?", "The class mark is multiplied by 2", "Scale property of midpoints"),
            ("Can a class mark ever lie outside the class interval?", "No, the class mark must strictly lie inside the interval, exactly at its center", "Centroid property of interval"),
            ("In plotting a frequency polygon, what coordinates represent the point for class i?", "(Class Mark xi, Class Frequency fi)", "Ordered pair (x_i, f_i)"),
            ("Why are class marks plotted on the X-axis rather than class limits in a frequency polygon?", "Because a polygon connects single points, and the class mark is the single representative value for the entire interval", "Single point representation"),
            ("If the class width is h, what is the distance from the lower limit to the class mark?", "h / 2 (half of the class width)", "Midpoint is at distance h/2 from either limit"),
            ("What is the distance from the class mark to the upper limit?", "h / 2 (half of the class width)", "Symmetry of midpoint"),
            ("If the class mark is 25 and class size is 10, what are the lower and upper limits?", "Lower = 25 - 5 = 20, Upper = 25 + 5 = 30", "Reconstructing interval 20-30"),
            ("If the class mark is 52 and class size is 6, what are the lower and upper limits?", "Lower = 52 - 3 = 49, Upper = 52 + 3 = 55", "Reconstructing interval 49-55")
        ],
        'tmpls': [
            "{0}",
            "In the mathematical theory of frequency distributions: {0}",
            "Analyze the class mark concept: {0}",
            "Identify the invariant property: {0}",
            "Which statement correctly characterizes: {0}?",
            "What is the mathematical consequence: {0}?",
            "Determine the correct answer: {0}",
            "In NCERT Class 9 statistics: {0}",
            "Select the accurate insight: {0}",
            "Evaluate the class mark property: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The class mark increases by 10",
                "It lies at the upper boundary",
                "(Lower limit, Frequency)"
            ],
            f"**Step 1: Review the geometric and algebraic properties of midpoints.**\nThe class mark \\( x_i = \\frac{{L + U}}{{2}} \\) represents the center of mass of the interval.\n\n**Step 2: Apply the property.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 10.2.2: Constructing frequency polygons with and without histograms
# ==============================================================================
def gen_10_2_2():
    tc = "CBSE-9-MGM-10-10.2.2"
    tname = "Constructing frequency polygons with and without histograms"

    # Arch 0: Method 1: Constructing Frequency Polygon WITH a Histogram
    arch0 = {
        'data': [
            ("To construct a frequency polygon using an existing histogram, what points are marked and joined?", "The midpoints of the upper horizontal sides of the rectangles of the histogram are joined by straight line segments", "Standard construction with histogram"),
            ("How is the frequency polygon completed (closed) at both ends when drawn on a histogram?", "By joining the first midpoint to the midpoint of an imaginary class preceding the first, and the last midpoint to an imaginary class succeeding the last (both on the X-axis with frequency 0)", "Grounding polygon to X-axis"),
            ("Why is the resulting figure called a 'polygon'?", "Because when joined to the horizontal axis at the zero-frequency midpoints, it forms a closed multi-sided planar figure (polygon)", "Definition of closed polygon"),
            ("Are the points of a frequency polygon joined by a smooth curve or by straight line segments?", "Strictly by straight line segments (using a ruler)", "Straight line segments requirement"),
            ("What type of graph is formed if the points are joined by a smooth hand-drawn curve rather than straight line segments?", "A Frequency Curve (not a frequency polygon)", "Polygon vs smooth curve"),
            ("In a frequency polygon drawn on a histogram, what does each plotted vertex represent?", "(Class Mark, Class Frequency)", "Coordinates of polygon vertices"),
            ("Does drawing a frequency polygon require any new numerical calculations if the histogram is already constructed?", "No, you simply mark the midpoints of the tops of the existing rectangles and join them with a ruler", "Direct geometric construction"),
            ("Can a frequency polygon be drawn if the class widths of the histogram are unequal?", "Yes, but it is much more commonly and simply drawn for uniform histograms", "Applicability"),
            ("What is the primary visual advantage of drawing the frequency polygon on top of the histogram?", "It clearly illustrates how the polygon models the continuous distribution of the histogram bars", "Visual synthesis"),
            ("In examination questions, if asked to draw 'a histogram and frequency polygon on the same graph', what is the order of drawing?", "First construct the histogram completely, then mark the midpoints of the tops of the bars, and join them including the zero-frequency ends", "Standard examination sequence")
        ],
        'tmpls': [
            "{0}",
            "In drawing a frequency polygon with a histogram: {0}",
            "What is the procedure for: {0}?",
            "Identify the correct construction rule: {0}",
            "Which statement accurately explains: {0}?",
            "How do we construct: {0}?",
            "Analyze the method of drawing a frequency polygon: {0}",
            "Determine the accurate step for: {0}",
            "Select the correct answer: {0}",
            "In NCERT Class 9 graph drawing: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The bottom corners of the rectangles are joined",
                "Points are joined by freehand circles",
                "The polygon must never touch the X-axis"
            ],
            f"**Step 1: Understand the construction of a frequency polygon with a histogram.**\n1. Draw the histogram.\n2. Mark the midpoint of the top edge of each rectangle.\n3. Join adjacent midpoints with straight line segments.\n4. Connect to X-axis at zero-frequency midpoints before and after.\n\n**Step 2: Detail the specific step.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Method 2: Constructing Frequency Polygon WITHOUT a Histogram
    arch1 = {
        'data': [
            ("To construct a frequency polygon independently WITHOUT drawing a histogram, what values are first calculated for each class?", "The Class Marks (Midpoints) of each class interval: \\( x_i = \\frac{\\text{Lower} + \\text{Upper}}{2} \\)", "Mandatory class mark calculation"),
            ("Once class marks are computed, what points \\( (x, y) \\) are plotted on the Cartesian plane?", "Points \\( (x_i, f_i) \\) where x_i is the class mark and f_i is the corresponding class frequency", "Plotting (x_i, f_i)"),
            ("After plotting the points \\( (x_i, f_i) \\), how are they connected?", "They are joined sequentially by straight line segments using a ruler", "Straight line connection"),
            ("To close the polygon on the horizontal axis, what two additional points are plotted?", "Points \\( (x_0, 0) \\) and \\( (x_{n+1}, 0) \\) corresponding to the midpoints of the preceding and succeeding imaginary classes", "Zero-frequency anchor points"),
            ("If the first class is 10-20 (width 10, class mark 15), what is the preceding anchor point on the X-axis?", "(5, 0)", "Preceding class is 0-10, class mark is 5, frequency is 0"),
            ("If the last class is 50-60 (width 10, class mark 55), what is the succeeding anchor point on the X-axis?", "(65, 0)", "Succeeding class is 60-70, class mark is 65, frequency is 0"),
            ("If class marks are 12, 16, 20, 24 (class width = 4), what are the two closing points on the X-axis?", "(8, 0) and (28, 0)", "12 - 4 = 8, 24 + 4 = 28"),
            ("Why is drawing a frequency polygon WITHOUT a histogram much faster?", "Because you do not need to construct dozens of rectangular vertical edges, saving significant drawing time in exams", "Drawing efficiency"),
            ("Is the resulting frequency polygon identical whether drawn with or without a histogram?", "Yes, the exact same polygon is produced by both methods", "Equivalence of methods"),
            ("Which method is mandatory when comparing TWO distributions on the SAME graph paper?", "The method without a histogram (plotting both frequency polygons directly on the same axes)", "Comparative superiority of polygons")
        ],
        'tmpls': [
            "{0}",
            "In constructing a frequency polygon without a histogram: {0}",
            "What is the first step or rule in: {0}?",
            "Identify the correct procedure: {0}",
            "Which coordinates are plotted: {0}?",
            "How do we anchor the polygon: {0}?",
            "Analyze the independent frequency polygon method: {0}",
            "Determine the accurate step: {0}",
            "Select the correct answer: {0}",
            "In NCERT Class 9 examination problems: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Plot (Lower Limit, Frequency)",
                "Plot (Upper Limit, Frequency)",
                "Points are joined by a parabolic spline"
            ],
            f"**Step 1: Calculate the class marks \\( x_i \\) for all classes.**\n\n**Step 2: Plot the points \\( (x_i, f_i) \\).**\nAnchor with \\( (x_0, 0) \\) and \\( (x_{{n+1}}, 0) \\).\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: The Area Equality Theorem (Area of Polygon = Area of Histogram)
    arch2 = {
        'data': [
            ("What is the fundamental mathematical theorem relating a frequency polygon to its corresponding histogram?", "The area enclosed by the frequency polygon and the horizontal axis is strictly EQUAL to the total area of the histogram", "Area Equality Theorem"),
            ("Why is the area of the frequency polygon equal to the total area of the histogram?", "Because the small triangular areas of the histogram excluded by the polygon segments are congruent to the extra triangular areas included outside the histogram bars", "Congruence of included and excluded triangles"),
            ("In the proof of the Area Equality Theorem, which triangle congruence criterion proves that the excluded and included triangles are congruent?", "ASA or AAS criterion (sharing vertical midpoint, equal alternate angles, and equal horizontal segment h/2)", "Congruence of triangular compensation"),
            ("Does the area equality property hold if the frequency polygon is NOT anchored to the X-axis at the zero-frequency midpoints?", "No, without closing the polygon on the X-axis, it is not a closed polygon and has no enclosed area", "Necessity of anchoring"),
            ("What does the total enclosed area of a frequency polygon represent statistically (when width = 1)?", "The total frequency \\( N = \\sum f_i \\) of the entire distribution", "Enclosed area represents total frequency"),
            ("If the total area of the rectangles of a histogram is 120 cm², what is the area enclosed by its frequency polygon?", "120 cm²", "Strict equality of areas"),
            ("If a student forgets to anchor the frequency polygon to the X-axis at both ends, what error is committed?", "The figure remains an open zigzag line with zero enclosed area, failing the definition of a polygon", "Open figure error"),
            ("Can the Area Equality Theorem hold if class intervals have unequal widths?", "Yes, the triangular compensation proof extends geometrically to any histogram", "General geometric validity"),
            ("Who first formalized the frequency polygon and its area equality theorem in modern statistics?", "Karl Pearson", "Historical attribution"),
            ("What is the pedagogical significance of the Area Equality Theorem in Class 9?", "It bridges discrete histogram bars with continuous frequency distributions in calculus and higher statistics", "Conceptual bridge to continuous probability")
        ],
        'tmpls': [
            "{0}",
            "Regarding the Area Equality Theorem of frequency polygons: {0}",
            "What is the mathematical relation between the areas: {0}?",
            "Identify the reason why: {0}",
            "Which statement correctly formulates: {0}?",
            "Analyze the area equivalence: {0}",
            "Determine the accurate geometric consequence: {0}",
            "Why is it true that: {0}?",
            "In Euclidean proof of graphical properties: {0}",
            "Select the accurate insight: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The polygon area is always half the histogram area",
                "The polygon area is always double the histogram area",
                "There is no relation between the two areas"
            ],
            f"**Step 1: State the Area Equality Theorem.**\n\\( \\text{{Area of Frequency Polygon}} = \\text{{Area of Histogram}} \\).\n\n**Step 2: Explain the geometric mechanism.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Comparing Two Distributions on the Same Graph (The Killer Feature of Polygons)
    arch3 = {
        'data': [
            ("Why cannot two different datasets (e.g. Section A and Section B test marks) be effectively displayed as two histograms on the same set of axes?", "Because the rectangles of the two histograms would overlap, cover each other, and create an unreadable visual mess", "Overlapping bars problem"),
            ("Which graphical representation is specifically designed and ideal for comparing two or more distributions on the SAME axes?", "Frequency Polygons", "Multiple polygons can be plotted with distinct colors/dashes without occlusion"),
            ("When comparing Section A and Section B using two frequency polygons on the same graph, how are they distinguished?", "By using different line styles (e.g. solid line for Section A, dashed line for Section B) or different colors, with a clear legend", "Legend and line differentiation"),
            ("If the frequency polygon of Section A is shifted to the right of Section B, what does this indicate about performance?", "Section A performed better overall than Section B (higher scores)", "Rightward shift indicates higher central values"),
            ("If the frequency polygon of Section A is tall and narrow while Section B is broad and flat, what does this indicate?", "Section A has low variability (scores clustered tightly), while Section B has high spread/dispersion", "Dispersion and spread interpretation"),
            ("In the classic NCERT example of two cricket teams (Team A and Team B runs per over), why must continuous class intervals be established before plotting?", "Because overs 1-6, 7-12, 13-18 are discontinuous (gap of 1) and must be converted to 0.5-6.5, 6.5-12.5 to compute true class marks", "Mandatory continuous conversion in NCERT cricket example"),
            ("In the NCERT cricket match example with overs 1-6, 7-12, 13-18, what is the class mark for overs 1-6 (0.5 to 6.5)?", "(0.5 + 6.5) / 2 = 3.5", "(1 + 6) / 2 = 3.5"),
            ("What is the class mark for the second group of overs 7-12 (6.5 to 12.5)?", "(6.5 + 12.5) / 2 = 9.5", "(7 + 12) / 2 = 9.5"),
            ("What is the class mark for the third group of overs 13-18 (12.5 to 18.5)?", "(12.5 + 18.5) / 2 = 15.5", "(13 + 18) / 2 = 15.5"),
            ("What is the class size (over increment) between consecutive class marks (9.5 - 3.5)?", "6 overs", "Uniform width of 6 overs")
        ],
        'tmpls': [
            "{0}",
            "In comparing two distributions with frequency polygons: {0}",
            "Why are frequency polygons preferred for: {0}?",
            "In the classic NCERT cricket over comparison: {0}",
            "How do we interpret comparative frequency polygons: {0}?",
            "Analyze the multi-distribution comparison: {0}",
            "Determine the accurate comparative statement: {0}",
            "What does this visual comparison indicate: {0}?",
            "In CBSE Class 9 comparative statistics: {0}",
            "Select the accurate insight: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Histograms are always better than frequency polygons for comparing two groups",
                "Section B performed better because its graph is wider",
                "Discontinuous overs can be plotted directly without class marks"
            ],
            f"**Step 1: Understand why frequency polygons excel at comparison.**\nBecause polygons use thin line segments rather than solid filled bars, multiple polygons can be overlaid transparently on the same axes.\n\n**Step 2: Detail the interpretation.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Reading and interpreting coordinates on a Frequency Polygon
    arch4 = {
        'data': [
            ("A vertex of a frequency polygon is located at (25, 14). What does this point represent?", "A class interval with class mark 25 has a frequency of 14", "Class mark = 25, frequency = 14"),
            ("If the class width is 10 and a polygon point is (35, 20), what is the class interval?", "30-40 (since 35 - 5 = 30 and 35 + 5 = 40)", "Reconstructed interval 30-40"),
            ("If the highest peak of a frequency polygon occurs at (45, 32), what is the modal class (class width = 10)?", "40-50", "Highest peak at class mark 45 corresponds to 40-50"),
            ("A frequency polygon has vertices at (15, 6), (25, 12), (35, 18), (45, 10), (55, 4). What is the total frequency N?", 50, "6 + 12 + 18 + 10 + 4 = 50"),
            ("In the same polygon, how many observations fall in classes with class mark >= 35?", 32, "18 + 10 + 4 = 32"),
            ("In the same polygon, how many observations fall in classes with class mark < 35?", 18, "6 + 12 = 18"),
            ("What are the two closing points on the X-axis for the polygon with marks 15, 25, 35, 45, 55 (width 10)?", "(5, 0) and (65, 0)", "15 - 10 = 5, 55 + 10 = 65"),
            ("If a polygon passes through (10, 0), what is the frequency of that point?", 0, "Y-coordinate is 0"),
            ("If a polygon vertex is at (105, 8) with class size 10, what are the class limits?", "100-110", "105 - 5 = 100, 105 + 5 = 110"),
            ("What is the ratio of frequencies between peak (35, 18) and lowest class (55, 4)?", "18 : 4 = 9 : 2 (or 4.5)", "18 / 4 = 4.5")
        ],
        'tmpls': [
            "{0}",
            "From the given frequency polygon data: {0}",
            "Read and interpret the polygon coordinates: {0}",
            "Calculate the required frequency or value: {0}",
            "Determine the accurate answer from the polygon: {0}",
            "Evaluate the frequency polygon points: {0}",
            "Find the required quantity from the graph: {0}",
            "Using the frequency polygon vertices: {0}",
            "What is the result for: {0}?",
            "Analyze the polygon coordinates: {0}"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1]} + 5" if isinstance(item[1], int) else "(20, 10)", f"{item[1]} - 5" if isinstance(item[1], int) else "(0, 0)", "100" if isinstance(item[1], int) else "3 : 1"],
            f"**Step 1: Read the coordinates \\( (x, y) \\) from the frequency polygon.**\n\\( x = \\text{{Class Mark}} \\), \\( y = \\text{{Class Frequency}} \\).\n\n**Step 2: Carry out the requested calculation.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Bimodal and Skewed distributions seen via Frequency Polygons
    arch5 = {
        'data': [
            ("A frequency polygon displays two prominent peaks separated by a valley. This distribution is classified as:", "Bimodal", "Two local maxima / modes"),
            ("What practical real-world scenario commonly produces a bimodal frequency polygon?", "A combined height distribution of adult men and adult women", "Two distinct sub-populations"),
            ("If the frequency polygon peak is located on the far left and the curve tails off gradually to the right, the distribution is:", "Positively skewed (Right-skewed)", "Long right tail"),
            ("If the frequency polygon peak is located on the far right and tails off to the left, the distribution is:", "Negatively skewed (Left-skewed)", "Long left tail"),
            ("In a perfectly symmetric, bell-shaped frequency polygon, where do the Mean, Median, and Mode lie?", "All three coincide at the exact central peak of the polygon", "Mean = Median = Mode in symmetric unimodal distribution"),
            ("In a positively skewed frequency polygon, what is the relative order of Mean, Median, and Mode from left to right?", "Mode < Median < Mean (Mean is pulled furthest into the long right tail)", "Order in right-skewed distribution"),
            ("In a negatively skewed frequency polygon, what is the relative order from left to right?", "Mean < Median < Mode (Mean is pulled into the long left tail)", "Order in left-skewed distribution"),
            ("Why is the Mean pulled further into the tail than the Median in skewed frequency polygons?", "Because the Mean is sensitive to extreme values (outliers), whereas the Median depends only on rank order", "Robustness of median vs sensitivity of mean"),
            ("What does a sharp, steep peak in a frequency polygon indicate about the dataset?", "High concentration of data around the central value (leptokurtic / low dispersion)", "Low spread around mode"),
            ("What does a broad, gentle peak in a frequency polygon indicate?", "Wide spread and high dispersion of values across the range (platykurtic)", "High dispersion")
        ],
        'tmpls': [
            "{0}",
            "In statistical analysis of polygon shapes: {0}",
            "Identify the distribution property from the polygon: {0}",
            "Regarding skewness and peaks in frequency polygons: {0}",
            "Which description characterizes: {0}?",
            "What does this polygon profile signify: {0}?",
            "Analyze the shape of the frequency polygon: {0}",
            "Determine the accurate statistical term: {0}",
            "Select the correct answer: {0}",
            "In interpreting frequency polygon profiles: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Uniform distribution",
                "Mean > Median > Mode always in all distributions",
                "Mean is unaffected by extreme values"
            ],
            f"**Step 1: Identify the shape and peak structure of the polygon.**\nExamine symmetry, peaks (modes), and tails (skewness).\n\n**Step 2: Match to the statistical property.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Step-by-Step Procedure for Full Polygon Construction in Exams
    arch6 = {
        'data': [
            ("Step 1 in constructing a frequency polygon without a histogram for discontinuous data like 1-5, 6-10 is:", "Convert the classes into continuous form (0.5-5.5, 5.5-10.5)", "Mandatory continuity step"),
            ("Step 2 in the procedure is:", "Compute the class mark of each class interval: (Upper + Lower) / 2", "Calculating class marks"),
            ("Step 3 in the procedure is:", "Determine the imaginary preceding class mark (with frequency 0) and succeeding class mark (with frequency 0)", "Finding closing anchor points"),
            ("Step 4 in the procedure is:", "Plot all points (xi, fi) including the zero-frequency endpoints on the graph sheet", "Plotting points"),
            ("Step 5 in the procedure is:", "Join all plotted points in sequential order using straight line segments with a ruler", "Joining with ruler"),
            ("Why is using a freehand curve instead of a ruler an error in drawing a frequency polygon?", "Because a frequency polygon by definition consists of straight line segments (polygonal edges)", "Must use ruler"),
            ("What essential elements must accompany the graph for full marks in CBSE exams?", "Graph Title, axis labels with units, explicit scale written in corner, and clear point markers", "Full marking scheme requirements"),
            ("If the class marks start at 105, what must be drawn near the origin on the X-axis?", "A kink (zigzag / broken axis line)", "Kink requirement"),
            ("Can frequencies on the Y-axis ever be negative in a frequency polygon?", "No, frequency is a count of items and is always >= 0", "Non-negativity of frequency"),
            ("Why must the line segments of a frequency polygon never cross each other?", "Because each class mark is strictly greater than the preceding one (monotonically increasing on X-axis)", "Sequential ordering on X-axis")
        ],
        'tmpls': [
            "{0}",
            "In the examination procedure for frequency polygons: {0}",
            "What is the required step in: {0}?",
            "Identify the correct construction phase: {0}",
            "Which rule must be strictly followed in: {0}?",
            "Explain the technical step: {0}",
            "Determine the accurate examination protocol: {0}",
            "In NCERT Class 9 frequency polygon drawing: {0}",
            "Select the accurate methodological step: {0}",
            "Follow the algorithm for frequency polygons: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Points can be joined in any random order",
                "Join points using a compass curve",
                "Omit the scale to save space"
            ],
            f"**Step 1: Review the 5-step protocol for frequency polygons.**\n1. Ensure continuous classes.\n2. Compute class marks \\( x_i \\).\n3. Find anchor points with \\( f = 0 \\).\n4. Plot \\( (x_i, f_i) \\).\n5. Join with straight line segments using a ruler.\n\n**Step 2: Detail the specific requirement.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Practical Problem Solving using Frequency Polygons
    arch7 = {
        'data': [
            ("A frequency polygon has vertices at (5, 4), (15, 10), (25, 16), (35, 12), (45, 8). What is the class width?", 10, "15 - 5 = 10"),
            ("In the same polygon, which class interval has the highest frequency?", "20-30 (class mark 25, frequency 16)", "Modal class 20-30"),
            ("What percentage of total observations (total = 50) fall in the modal class (freq = 16)?", "32%", "(16 / 50) * 100% = 32%"),
            ("How many observations are in classes with class mark <= 25?", 30, "4 + 10 + 16 = 30"),
            ("How many observations are in classes with class mark > 25?", 20, "12 + 8 = 20"),
            ("What is the ratio of observations in class mark 15 to class mark 45?", "10 : 8 = 5 : 4", "10 / 8 = 5/4"),
            ("What are the coordinates of the left anchor point on the X-axis?", "(-5, 0)", "5 - 10 = -5"),
            ("What are the coordinates of the right anchor point on the X-axis?", "(55, 0)", "45 + 10 = 55"),
            ("If each unit on Y-axis represents 2 students, how many students are in the class with peak height 8 units?", 16, "8 * 2 = 16 students"),
            ("Why is the frequency polygon considered one of the most powerful elementary visualizations in statistics?", "Because it displays distribution shape, central tendency, dispersion, and enables easy multi-group comparisons simultaneously", "Comprehensive statistical utility")
        ],
        'tmpls': [
            "Consider the frequency polygon with vertices: {0}. {1}",
            "From the frequency polygon data: {0}. {1}",
            "Using the polygon coordinates: {0}, solve: {1}",
            "Analyze the given frequency polygon: {0}. {1}",
            "Based on the frequency polygon vertices: {0}, answer: {1}",
            "Evaluate the distribution from the polygon: {0}. {1}",
            "For the frequency polygon: {0}, calculate: {1}",
            "Refer to the polygon points: {0}. Determine: {1}",
            "Solve using the frequency polygon: {0}: {1}",
            "From the plotted frequency polygon: {0}, {1}"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1]} + 5" if isinstance(item[1], int) else "25%", f"{item[1]} - 5" if isinstance(item[1], int) else "40%", "50" if isinstance(item[1], int) else "1 : 1"],
            f"**Step 1: Extract the relevant information from the frequency polygon vertices.**\n\n**Step 2: Perform the requested calculation.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_10_2_1()
    q2 = gen_10_2_2()
    print(f"gen_10_2_1: {len(q1)} questions")
    print(f"gen_10_2_2: {len(q2)} questions")
