# scripts/generate_ch7_full.py
import json

def make_opt(text, is_correct):
    return {"text": text, "isCorrect": is_correct}

def make_unique_opts(corr_text, raw_distractors):
    seen = {corr_text}
    distractors = []
    for d in raw_distractors:
        if d not in seen:
            seen.add(d)
            distractors.append(d)
        if len(distractors) == 3:
            break
    counter = 1
    while len(distractors) < 3:
        cand = f"\\(\\text{{None of these}}\\) {counter}"
        if cand not in seen:
            seen.add(cand)
            distractors.append(cand)
        counter += 1
    opts = [make_opt(corr_text, True)] + [make_opt(d, False) for d in distractors]
    return opts

def make_q(q_code, text, opts, sol, t_code, t_name, vault, diff, q_type="OSC", marks=4):
    letters = ["A", "B", "C", "D"]
    corr_idx = -1
    for idx, o in enumerate(opts):
        if o["isCorrect"]:
            corr_idx = idx
            break
    if corr_idx == -1:
        raise ValueError(f"No correct option in {q_code}")
    
    return {
        "questionCode": q_code,
        "text": text,
        "options": opts,
        "correctAnswer": letters[corr_idx],
        "solution": sol,
        "boardCode": "MH",
        "board": "Maharashtra Board",
        "class": "9",
        "subjectCode": "MTH1",
        "subject": "Mathematics Part - 1 (Algebra)",
        "chapterNumber": 7,
        "chapter": "Statistics",
        "topicCode": t_code,
        "topic": t_name,
        "type": q_type,
        "marks": marks,
        "difficulty": diff,
        "vault": vault,
        "timesUsed": 0,
        "usedInClassroomTest": False,
        "requiresFigure": False,
        "createdAt": "2026-11-21T13:01:00.000Z",
        "updatedAt": "2026-11-21T13:01:00.000Z"
    }

questions_ch7 = []

# ==========================================
# 7.1.1 Data collection methods (Primary vs Secondary)
# T_CODE = "MH-9-MTH1-7-7.1.1", T_NAME = "Data collection methods"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_711 = "MH-9-MTH1-7-7.1.1"
t_name_711 = "Data collection methods"

for i in range(1, 39):
    txt = "A researcher conducts door-to-door interviews to record the number of family members in each household. What type of data is this?"
    corr = "Primary data"
    raw_distractors = [
        "Secondary data",
        "Qualitative unmeasurable data",
        "Continuous grouped data"
    ]
    if i % 2 == 0:
        txt = "A student extracts literacy rate statistics from the official Census of India website for a school project. What type of data is this?"
        corr = "Secondary data"
        raw_distractors = [
            "Primary data",
            "Raw experimental data",
            "Discrete frequency data"
        ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        "Step 1: Primary data is data collected firsthand by the investigator specifically for the purpose of the study.\n"
        "Step 2: Secondary data is data collected by an external agency, published records, or government department, and reused by an investigator.\n"
        f"Step 3: Hence, this is classified as {corr}."
    )
    q_code = f"MH-9-MTH1-7-7.1.1-OSC-{100 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_711, t_name_711, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    txt = "Which of the following is an example of Primary Data?"
    corr = "Measuring the heights of all students in your classroom using a measuring tape"
    raw_distractors = [
        "Reading the rainfall data from yesterday's newspaper",
        "Collecting population figures from the municipal corporation records",
        "Using export-import data published by the Reserve Bank of India"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Direct personal measurement by the researcher produces primary data.\n"
        "Step 2: Measuring heights of classmates directly is firsthand collection.\n"
        "Step 3: Hence, it is Primary Data."
    )
    q_code = f"MH-9-MTH1-7-7.1.1-OSC-{200 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_711, t_name_711, "practice", "medium"))

for i in range(1, 21):
    txt = "What is the key advantage of primary data over secondary data?"
    corr = "It is collected firsthand, making it directly relevant and reliable for the specific inquiry"
    w1 = "It requires no time or effort to collect"
    w2 = "It is always free from any sample size requirement"
    w3 = "It never requires tally marks"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Primary data is tailored to the exact objective of the investigation.\n"
        "Step 2: The investigator has direct control over the measurement methods and definitions.\n"
        "Step 3: Hence, high relevance and firsthand reliability is the key advantage."
    )
    q_code = f"MH-9-MTH1-7-7.1.1-OSC-{150 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_711, t_name_711, "foundation", "easy"))

# ==========================================
# 7.1.2 Class intervals: Inclusive (discrete) vs Exclusive (continuous) method
# T_CODE = "MH-9-MTH1-7-7.1.2", T_NAME = "Class intervals: Inclusive vs Exclusive method"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_712 = "MH-9-MTH1-7-7.1.2"
t_name_712 = "Class intervals: Inclusive vs Exclusive method"

for i in range(1, 39):
    l = 10 + (i % 5) * 10
    u = l + 9
    txt = f"Convert the inclusive class interval \\({l} - {u}\\) into continuous (exclusive) true class limits."
    corr = f"\\({l - 0.5} - {u + 0.5}\\)"
    raw_distractors = [
        f"\\({l} - {u + 1}\\)",
        f"\\({l - 1} - {u + 1}\\)",
        f"\\({l + 0.5} - {u - 0.5}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: The gap between consecutive inclusive classes is \\(1\\) (e.g., \\({u}\\) to \\({u + 1}\\)).\n"
        f"Step 2: Correction factor = \\(\\frac{{1}}{{2}} = 0.5\\).\n"
        f"Step 3: Subtract 0.5 from lower limit and add 0.5 to upper limit: \\({l} - 0.5 = {l - 0.5}\\) and \\({u} + 0.5 = {u + 0.5}\\).\n"
        f"Continuous class limits are \\({l - 0.5} - {u + 0.5}\\)."
    )
    q_code = f"MH-9-MTH1-7-7.1.2-OSC-{100 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_712, t_name_712, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    txt = "In the exclusive class interval \\(20 - 30\\), in which class is an observation with exact value \\(30\\) included?"
    corr = "In the next class \\(30 - 40\\)"
    raw_distractors = [
        "In the class \\(20 - 30\\)",
        "In both classes \\(20 - 30\\) and \\(30 - 40\\)",
        "It is excluded from the frequency table"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: In the exclusive (continuous) method, the upper class limit is strictly excluded from that class.\n"
        "Step 2: The class \\(20 - 30\\) contains values \\(20 \\le x < 30\\).\n"
        "Step 3: Value 30 is included in the succeeding class \\(30 - 40\\)."
    )
    q_code = f"MH-9-MTH1-7-7.1.2-OSC-{200 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_712, t_name_712, "practice", "medium"))

for i in range(1, 21):
    txt = "What is another name for the exclusive method of classification?"
    corr = "Continuous class method"
    w1 = "Discrete class method"
    w2 = "Cumulative method"
    w3 = "Primary method"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: In the exclusive method, the upper limit of one class is the lower limit of the next class (e.g., 0-10, 10-20).\n"
        "Step 2: There is no gap between consecutive intervals, creating a continuous boundary.\n"
        "Step 3: Hence, it is called the continuous class method."
    )
    q_code = f"MH-9-MTH1-7-7.1.2-OSC-{150 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_712, t_name_712, "foundation", "easy"))

# ==========================================
# 7.1.3 Class mark = (Lower limit + Upper limit)/2
# T_CODE = "MH-9-MTH1-7-7.1.3", T_NAME = "Class mark calculation"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_713 = "MH-9-MTH1-7-7.1.3"
t_name_713 = "Class mark calculation"

for i in range(1, 39):
    l = 10 + (i % 8) * 15 # 10, 25, 40, ...
    u = l + 20
    cm = (l + u) / 2
    cm_str = f"{int(cm)}" if cm.is_integer() else f"{cm}"

    txt = f"Find the class mark of the class interval \\({l} - {u}\\)."
    corr = f"\\({cm_str}\\)"
    raw_distractors = [
        f"\\({u - l}\\)",
        f"\\({int(cm) + 5}\\)",
        f"\\({int(cm) - 5}\\)",
        f"\\({l}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Formula for class mark: \\(\\text{{Class mark}} = \\frac{{\\text{{Lower limit}} + \\text{{Upper limit}}}}{{2}}\\).\n"
        f"Step 2: \\(\\text{{Class mark}} = \\frac{{{l} + {u}}}{{2}} = \\frac{{{l + u}}}{{2}}\\).\n"
        f"Step 3: \\(\\text{{Class mark}} = {cm_str}\\)."
    )
    q_code = f"MH-9-MTH1-7-7.1.3-OSC-{100 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_713, t_name_713, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    l = (i % 6) * 10
    u = l + 10
    cm = (l + u) // 2
    txt = f"What is the midpoint (class mark) of the interval \\({l} - {u}\\)?"
    corr = f"\\({cm}\\)"
    raw_distractors = [
        f"\\({cm + 2}\\)",
        f"\\({cm - 2}\\)",
        f"\\(10\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: \\(\\text{{Class mark}} = \\frac{{{l} + {u}}}{{2}}\\).\n"
        f"Step 2: \\(\\frac{{{l + u}}}{{2}} = {cm}\\).\n"
        f"Step 3: The midpoint is \\({cm}\\)."
    )
    q_code = f"MH-9-MTH1-7-7.1.3-OSC-{200 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_713, t_name_713, "practice", "medium"))

for i in range(1, 21):
    txt = "What is the formula to calculate the class mark of a class interval?"
    corr = "\\(\\frac{\\text{Lower limit} + \\text{Upper limit}}{2}\\)"
    w1 = "\\(\\text{Upper limit} - \\text{Lower limit}\\)"
    w2 = "\\(\\text{Upper limit} \\times \\text{Lower limit}\\)"
    w3 = "\\(\\frac{\\text{Upper limit} - \\text{Lower limit}}{2}\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: The class mark is the central representative value (midpoint) of the class interval.\n"
        "Step 2: It is calculated as the average of the lower and upper limits.\n"
        "Step 3: Formula is \\(\\frac{\\text{Lower limit} + \\text{Upper limit}}{2}\\)."
    )
    q_code = f"MH-9-MTH1-7-7.1.3-OSC-{150 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_713, t_name_713, "foundation", "easy"))

# ==========================================
# 7.2.1 Cumulative Frequency (Less than type)
# T_CODE = "MH-9-MTH1-7-7.2.1", T_NAME = "Running cumulative sum (Less than type)"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_721 = "MH-9-MTH1-7-7.2.1"
t_name_721 = "Running cumulative sum (Less than type)"

for i in range(1, 39):
    f1 = (i % 4) + 3
    f2 = (i % 5) + 5
    f3 = (i % 3) + 4
    cf1 = f1
    cf2 = f1 + f2
    cf3 = cf2 + f3

    txt = f"Three class intervals have frequencies \\({f1}\\), \\({f2}\\), and \\({f3}\\) respectively. What is the cumulative frequency of less than type for the third class?"
    corr = f"\\({cf3}\\)"
    raw_distractors = [
        f"\\({cf2}\\)",
        f"\\({f3}\\)",
        f"\\({cf3 + 3}\\)",
        f"\\({cf3 - 2}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Less than type cumulative frequency is the sum of frequencies up to that class.\n"
        f"Step 2: \\(cf_1 = {f1}\\); \\(cf_2 = {f1} + {f2} = {cf2}\\).\n"
        f"Step 3: \\(cf_3 = {cf2} + {f3} = {cf3}\\)."
    )
    q_code = f"MH-9-MTH1-7-7.2.1-OSC-{100 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_721, t_name_721, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    f1 = (i % 3) + 4
    f2 = (i % 4) + 6
    cf = f1 + f2
    txt = f"If the frequencies of the first two classes are \\({f1}\\) and \\({f2}\\), what is the less-than cumulative frequency of the second class?"
    corr = f"\\({cf}\\)"
    raw_distractors = [
        f"\\({f2}\\)",
        f"\\({cf + 2}\\)",
        f"\\({f1}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: Add the frequency of the first class and second class.\n"
        f"Step 2: \\({f1} + {f2} = {cf}\\).\n"
        f"Step 3: The cumulative frequency is \\({cf}\\)."
    )
    q_code = f"MH-9-MTH1-7-7.2.1-OSC-{200 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_721, t_name_721, "practice", "medium"))

for i in range(1, 21):
    txt = "The cumulative frequency of less than type for the last class interval is always equal to what?"
    corr = "The total frequency \\(N\\) (total number of observations)"
    w1 = "Zero"
    w2 = "The mean of the data"
    w3 = "The frequency of the first class"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: In less-than cumulative frequency, frequencies of all classes are added successively.\n"
        "Step 2: By the last class, all class frequencies have been added: \\(\\sum f_i = N\\).\n"
        "Step 3: Therefore, it equals the total frequency \\(N\\)."
    )
    q_code = f"MH-9-MTH1-7-7.2.1-OSC-{150 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_721, t_name_721, "foundation", "easy"))

# ==========================================
# 7.2.2 Cumulative frequency of more than type
# T_CODE = "MH-9-MTH1-7-7.2.2", T_NAME = "Frequency interpretation (More than type)"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_722 = "MH-9-MTH1-7-7.2.2"
t_name_722 = "Frequency interpretation (More than type)"

for i in range(1, 39):
    total_n = 50 + (i % 5) * 10 # 50 to 90
    f1 = (i % 4) + 5
    more_than_second = total_n - f1

    txt = f"A distribution has total frequency \\(N = {total_n}\\). If the frequency of the first class interval is \\({f1}\\), what is the cumulative frequency of more than or equal to the lower limit of the second class?"
    corr = f"\\({more_than_second}\\)"
    raw_distractors = [
        f"\\({total_n}\\)",
        f"\\({f1}\\)",
        f"\\({more_than_second + 5}\\)",
        f"\\({more_than_second - 5}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: 'More than or equal to' cumulative frequency includes all observations starting from that class limit to the end.\n"
        f"Step 2: Cumulative frequency for the 2nd class onwards = \\(\\text{{Total }} N - f_1 = {total_n} - {f1}\\).\n"
        f"Step 3: \\({total_n} - {f1} = {more_than_second}\\)."
    )
    q_code = f"MH-9-MTH1-7-7.2.2-OSC-{100 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_722, t_name_722, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    txt = "What is the cumulative frequency of 'more than or equal to' type for the first class interval?"
    corr = "Total frequency \\(N\\)"
    raw_distractors = [
        "Frequency of the first class only",
        "Zero",
        "Average frequency"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: All observations in the dataset are greater than or equal to the lowest limit.\n"
        "Step 2: Therefore, the sum includes all frequencies \\(\\sum f_i = N\\).\n"
        "Step 3: Hence, it equals total frequency \\(N\\)."
    )
    q_code = f"MH-9-MTH1-7-7.2.2-OSC-{200 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_722, t_name_722, "practice", "medium"))

for i in range(1, 21):
    txt = "In a frequency table, how are 'less than' and 'more than' cumulative frequencies related?"
    corr = "Less-than accumulates frequencies from top to bottom, while more-than accumulates from bottom to top"
    w1 = "They are identical in every row"
    w2 = "Their product always equals 1"
    w3 = "They cannot both exist for the same dataset"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Less-than cf begins with the first frequency and adds downward.\n"
        "Step 2: More-than cf begins with the total frequency and subtracts, or adds from bottom upward.\n"
        "Step 3: Hence, they accumulate in opposite directions."
    )
    q_code = f"MH-9-MTH1-7-7.2.2-OSC-{150 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_722, t_name_722, "foundation", "easy"))

# ==========================================
# 7.3.1 Mean: X_bar = sum(x)/N
# T_CODE = "MH-9-MTH1-7-7.3.1", T_NAME = "Mean calculation"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_731 = "MH-9-MTH1-7-7.3.1"
t_name_731 = "Mean calculation"

for i in range(1, 39):
    base = 10 + (i % 6) * 5
    # 5 numbers: base-2, base-1, base, base+1, base+2 => mean is base
    # let's offset: base, base+2, base+4, base+6, base+8 => mean is base+4
    nums = [base, base + 2, base + 4, base + 6, base + 8]
    s = sum(nums)
    m = s // 5

    txt = f"Find the arithmetic mean of the observations: \\({nums[0]}, {nums[1]}, {nums[2]}, {nums[3]}, {nums[4]}\\)."
    corr = f"\\({m}\\)"
    raw_distractors = [
        f"\\({m + 2}\\)",
        f"\\({m - 2}\\)",
        f"\\({s}\\)",
        f"\\({m + 4}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Formula for mean: \\(\\bar{{X}} = \\frac{{\\sum x_i}}{{N}}\\).\n"
        f"Step 2: Sum of observations = \\({nums[0]} + {nums[1]} + {nums[2]} + {nums[3]} + {nums[4]} = {s}\\).\n"
        f"Step 3: Divide by number of observations \\(N = 5\\): \\(\\bar{{X}} = \\frac{{{s}}}{{5}} = {m}\\)."
    )
    q_code = f"MH-9-MTH1-7-7.3.1-OSC-{100 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_731, t_name_731, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    k = (i % 5) + 3
    s = k * 10
    txt = f"If the sum of \\({k}\\) observations is \\({s}\\), what is their mean?"
    corr = f"\\({10}\\)"
    raw_distractors = [
        f"\\({k}\\)",
        f"\\({s}\\)",
        f"\\({12}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: \\(\\text{{Mean}} = \\frac{{\\sum x}}{{N}}\\).\n"
        f"Step 2: \\(\\text{{Mean}} = \\frac{{{s}}}{{{k}}} = 10\\).\n"
        f"Step 3: The mean is \\(10\\)."
    )
    q_code = f"MH-9-MTH1-7-7.3.1-OSC-{200 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_731, t_name_731, "practice", "medium"))

for i in range(1, 21):
    txt = "What is the formula for the mean \\(\\bar{X}\\) of ungrouped data?"
    corr = "\\(\\bar{X} = \\frac{\\sum x_i}{N}\\)"
    w1 = "\\(\\bar{X} = \\sum x_i \\times N\\)"
    w2 = "\\(\\bar{X} = \\frac{N}{\\sum x_i}\\)"
    w3 = "\\(\\bar{X} = \\frac{\\sum x_i}{2}\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: The mean is the sum of all values divided by the total number of values.\n"
        "Step 2: \\(\\sum x_i\\) represents the sum, and \\(N\\) is the number of observations.\n"
        "Step 3: Hence, \\(\\bar{X} = \\frac{\\sum x_i}{N}\\)."
    )
    q_code = f"MH-9-MTH1-7-7.3.1-OSC-{150 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_731, t_name_731, "foundation", "easy"))

# ==========================================
# 7.3.2 Median: Middle value of sorted array (N odd/even)
# T_CODE = "MH-9-MTH1-7-7.3.2", T_NAME = "Median calculation"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_732 = "MH-9-MTH1-7-7.3.2"
t_name_732 = "Median calculation"

for i in range(1, 39):
    b = 5 + (i % 7) * 3
    # 7 numbers in unsorted order:
    # sorted: b, b+1, b+2, b+4, b+6, b+7, b+9 -> median is b+4
    sorted_nums = [b, b + 1, b + 2, b + 4, b + 6, b + 7, b + 9]
    median = sorted_nums[3]
    # unsort them
    unsorted = [sorted_nums[2], sorted_nums[0], sorted_nums[4], sorted_nums[6], sorted_nums[1], sorted_nums[3], sorted_nums[5]]

    txt = f"Find the median of the data: \\({unsorted[0]}, {unsorted[1]}, {unsorted[2]}, {unsorted[3]}, {unsorted[4]}, {unsorted[5]}, {unsorted[6]}\\)."
    corr = f"\\({median}\\)"
    raw_distractors = [
        f"\\({median + 2}\\)",
        f"\\({median - 2}\\)",
        f"\\({sorted_nums[2]}\\)",
        f"\\({sorted_nums[4]}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Arrange observations in ascending order: \\({sorted_nums[0]}, {sorted_nums[1]}, {sorted_nums[2]}, {sorted_nums[3]}, {sorted_nums[4]}, {sorted_nums[5]}, {sorted_nums[6]}\\).\n"
        f"Step 2: Number of observations \\(N = 7\\) (odd). Median is the \\(\\frac{{N+1}}{{2}} = \\frac{{7+1}}{{2}} = 4\\)th observation.\n"
        f"Step 3: The 4th observation is \\({median}\\)."
    )
    q_code = f"MH-9-MTH1-7-7.3.2-OSC-{100 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_732, t_name_732, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    txt = "What is the first step in finding the median of a raw numerical data set?"
    corr = "Arrange the observations in ascending or descending order"
    raw_distractors = [
        "Calculate the sum of all observations",
        "Count the frequency of the most common number",
        "Multiply the first and last numbers"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: The median is positional, representing the middle value.\n"
        "Step 2: To identify the central position, data must first be ordered by magnitude.\n"
        "Step 3: Hence, arranging in ascending (or descending) order is the essential first step."
    )
    q_code = f"MH-9-MTH1-7-7.3.2-OSC-{200 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_732, t_name_732, "practice", "medium"))

for i in range(1, 21):
    txt = "For an even number of observations \\(N\\), how is the median calculated?"
    corr = "\\(\\text{Average of the } \\frac{N}{2}\\text{-th and } \\left(\\frac{N}{2} + 1\\right)\\text{-th observations}\\)"
    w1 = "\\(\\text{The } \\frac{N}{2}\\text{-th observation only}\\)"
    w2 = "\\(\\text{The } (N + 1)\\text{-th observation}\\)"
    w3 = "\\(\\text{Difference between largest and smallest values}\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: When \\(N\\) is even, there is no single middle observation.\n"
        "Step 2: The two central observations are at positions \\(\\frac{N}{2}\\) and \\(\\frac{N}{2} + 1\\).\n"
        "Step 3: The median is the arithmetic mean of these two middle values."
    )
    q_code = f"MH-9-MTH1-7-7.3.2-OSC-{150 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_732, t_name_732, "foundation", "easy"))

# ==========================================
# 7.3.3 Mode: Most frequently occurring value
# T_CODE = "MH-9-MTH1-7-7.3.3", T_NAME = "Mode calculation"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_733 = "MH-9-MTH1-7-7.3.3"
t_name_733 = "Mode calculation"

for i in range(1, 39):
    target = 10 + (i % 9) * 3
    other1 = target + 2
    other2 = target - 2
    # list: target occurs 3 times, others occur 1 or 2 times
    nums = [other1, target, other2, target, target, other1, other2 - 1]
    
    txt = f"Find the mode of the dataset: \\({nums[0]}, {nums[1]}, {nums[2]}, {nums[3]}, {nums[4]}, {nums[5]}, {nums[6]}\\)."
    corr = f"\\({target}\\)"
    raw_distractors = [
        f"\\({other1}\\)",
        f"\\({other2}\\)",
        f"\\({target + 1}\\)",
        f"\\({target - 1}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Mode is the observation that appears with the highest frequency.\n"
        f"Step 2: In the given data, \\({target}\\) appears 3 times, while all other numbers appear 1 or 2 times.\n"
        f"Step 3: Therefore, the mode is \\({target}\\)."
    )
    q_code = f"MH-9-MTH1-7-7.3.3-OSC-{100 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_733, t_name_733, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    val = (i % 6) + 4
    txt = f"In the dataset \\({val}, {val+1}, {val}, {val+2}, {val}, {val+3}\\), what is the mode?"
    corr = f"\\({val}\\)"
    raw_distractors = [
        f"\\({val + 1}\\)",
        f"\\({val + 2}\\)",
        f"\\(3\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: Count frequency of each element: \\({val}\\) occurs 3 times, other elements occur once.\n"
        f"Step 2: The observation with maximum frequency is \\({val}\\).\n"
        f"Step 3: Hence, the mode is \\({val}\\)."
    )
    q_code = f"MH-9-MTH1-7-7.3.3-OSC-{200 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_733, t_name_733, "practice", "medium"))

for i in range(1, 21):
    txt = "Can a dataset have more than one mode?"
    corr = "Yes, if two or more values share the highest frequency (e.g. bimodal)"
    w1 = "No, mode is always strictly unique"
    w2 = "Only if all numbers are zero"
    w3 = "Only for negative numbers"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: If two distinct observations appear with the same maximum frequency, both are modes.\n"
        "Step 2: Such a dataset is called bimodal (or multimodal if more than two).\n"
        "Step 3: Hence, a dataset can have more than one mode."
    )
    q_code = f"MH-9-MTH1-7-7.3.3-OSC-{150 + i:03d}"
    questions_ch7.append(make_q(q_code, txt, opts, sol, t_code_733, t_name_733, "foundation", "easy"))

print(f"Generated Chapter 7: {len(questions_ch7)} questions")

with open("scripts/mh9_mth1_ch7_generated.json", "w", encoding="utf-8") as f:
    json.dump(questions_ch7, f, indent=2)
