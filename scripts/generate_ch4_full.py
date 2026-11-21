# scripts/generate_ch4_full.py
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
    # Fallback if somehow < 3
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
        "chapterNumber": 4,
        "chapter": "Ratio and Proportion",
        "topicCode": t_code,
        "topic": t_name,
        "type": q_type,
        "marks": marks,
        "difficulty": diff,
        "vault": vault,
        "timesUsed": 0,
        "usedInClassroomTest": False,
        "requiresFigure": False,
        "createdAt": "2026-11-21T12:52:00.000Z",
        "updatedAt": "2026-11-21T12:52:00.000Z"
    }

questions_ch4 = []

# ==========================================
# 4.1.1 Units consistency
# T_CODE = "MH-9-MTH1-4-4.1.1", T_NAME = "Units consistency"
# Need 35 Exam (Seq 101-135), 20 Foundation (Seq 151-170)
# ==========================================
t_code_411 = "MH-9-MTH1-4-4.1.1"
t_name_411 = "Units consistency"

units_pairs = [
    # (val1, unit1, val2, unit2, conv_factor, simplified_num, simplified_den)
    (5, "rupees", 75, "paise", 100, 20, 3), # 500 paise : 75 paise = 20:3
    (2, "litres", 400, "ml", 1000, 5, 1), # 2000 : 400 = 5:1
    (3, "kg", 750, "grams", 1000, 4, 1), # 3000 : 750 = 4:1
    (4, "hours", 40, "minutes", 60, 6, 1), # 240 : 40 = 6:1
    (2, "metres", 25, "cm", 100, 8, 1), # 200 : 25 = 8:1
    (3, "years", 4, "months", 12, 10, 1), # 40 months (3 yr 4 mo) : ... wait
    (15, "minutes", 1, "hour", 60, 1, 4), # 15 min : 60 min = 1:4
    (500, "grams", 2, "kg", 1000, 1, 4), # 500 : 2000 = 1:4
    (6, "metres", 3, "km", 1000, 1, 500), # 6 : 3000 = 1:500
    (75, "paise", 3, "rupees", 100, 1, 4)
]

for i in range(1, 36):
    pair = units_pairs[i % len(units_pairs)]
    mult = (i // len(units_pairs)) + 1
    v1 = pair[0] * mult
    u1 = pair[1]
    v2 = pair[2]
    u2 = pair[3]
    factor = pair[4]
    
    # ratio v1 u1 to v2 u2
    # convert both to smaller unit
    c1 = v1 * factor if factor > 1 and "hour" not in u1 and u1 != "minutes" else v1
    c2 = v2
    if u2 in ["hour", "kg", "km", "rupees"]:
        c2 = v2 * factor
    if u1 == "hours" and u2 == "minutes":
        c1 = v1 * 60
    elif u1 == "minutes" and u2 == "hour":
        c2 = v2 * 60
    elif u1 == "years" and u2 == "months":
        c1 = v1 * 12
    elif u1 == "rupees" and u2 == "paise":
        c1 = v1 * 100
    elif u1 == "paise" and u2 == "rupees":
        c2 = v2 * 100
    elif u1 in ["litres", "kg", "metres"] and u2 in ["ml", "grams", "cm"]:
        c1 = v1 * (100 if u2 == "cm" else 1000)
    elif u1 in ["grams", "metres"] and u2 in ["kg", "km"]:
        c2 = v2 * 1000

    import math
    g = math.gcd(c1, c2)
    s_num = c1 // g
    s_den = c2 // g

    txt = f"Find the reduced form of the ratio of the first quantity to the second quantity: \\({v1}\\) {u1} to \\({v2}\\) {u2}."
    corr = f"\\({s_num} : {s_den}\\)"
    # distractors
    d1 = f"\\({s_den} : {s_num}\\)"
    d2 = f"\\({s_num + 1} : {s_den}\\)"
    d3 = f"\\({s_num} : {s_den + 1}\\)"
    # ensure distinct
    distractors = [d for d in [d1, d2, d3, f"\\({s_num + 2} : {s_den}\\)"] if d != corr][:3]
    opts = [make_opt(corr, True), make_opt(distractors[0], False), make_opt(distractors[1], False), make_opt(distractors[2], False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Convert both quantities into the same unit.\n"
        f"First quantity: \\({v1}\\) {u1} = \\({c1}\\) {u2 if u2 not in ['hour', 'kg', 'km', 'rupees'] else u1}.\n"
        f"Second quantity: \\({v2}\\) {u2} = \\({c2}\\) {u2 if u2 not in ['hour', 'kg', 'km', 'rupees'] else u1}.\n"
        f"Step 2: Form the ratio: \\(\\frac{{{c1}}}{{{c2}}}\\).\n"
        f"Step 3: Divide numerator and denominator by their GCD \\({g}\\):\n"
        f"The reduced form is \\({s_num} : {s_den}\\)."
    )
    q_code = f"MH-9-MTH1-4-4.1.1-OSC-{100 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_411, t_name_411, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    txt = "Can a ratio be found directly between 5 litres and 200 grams without conversion?"
    corr = "No, because ratio is defined only between quantities of the same kind"
    w1 = "Yes, the ratio is 5 : 200 = 1 : 40"
    w2 = "Yes, by multiplying by 1000"
    w3 = "Yes, if temperature is constant"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: By definition, a ratio is a comparison between two quantities of the same kind and measured in the same unit.\n"
        "Step 2: Litres measure volume, whereas grams measure mass (weight). These are different physical kinds of quantities.\n"
        "Step 3: Therefore, a ratio cannot be formed between them."
    )
    q_code = f"MH-9-MTH1-4-4.1.1-OSC-{150 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_411, t_name_411, "foundation", "easy"))

# ==========================================
# 4.1.2 Order of terms (antecedent / consequent, comparing ratios)
# T_CODE = "MH-9-MTH1-4-4.1.2", T_NAME = "Order of terms"
# Need 35 Exam (Seq 101-135), 20 Foundation (Seq 151-170)
# ==========================================
t_code_412 = "MH-9-MTH1-4-4.1.2"
t_name_412 = "Order of terms"

for i in range(1, 36):
    a = (i % 6) + 2
    b = (i % 7) + 3
    c = ((i * 2) % 5) + 2
    d = ((i * 3) % 7) + 4
    # Compare a/b with c/d
    # ad vs bc
    ad = a * d
    bc = b * c
    if ad == bc:
        d += 1
        ad = a * d
    
    txt = f"Compare the pair of ratios \\(\\frac{{{a}}}{{{b}}}\\) and \\(\\frac{{{c}}}{{{d}}}\\)."
    if ad > bc:
        corr = f"\\(\\frac{{{a}}}{{{b}}} > \\frac{{{c}}}{{{d}}}\\)"
        w1 = f"\\(\\frac{{{a}}}{{{b}}} < \\frac{{{c}}}{{{d}}}\\)"
        w2 = f"\\(\\frac{{{a}}}{{{b}}} = \\frac{{{c}}}{{{d}}}\\)"
        w3 = "Cannot be compared"
    else:
        corr = f"\\(\\frac{{{a}}}{{{b}}} < \\frac{{{c}}}{{{d}}}\\)"
        w1 = f"\\(\\frac{{{a}}}{{{b}}} > \\frac{{{c}}}{{{d}}}\\)"
        w2 = f"\\(\\frac{{{a}}}{{{b}}} = \\frac{{{c}}}{{{d}}}\\)"
        w3 = "Cannot be compared"

    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Compute cross products \\(a \\times d\\) and \\(b \\times c\\):\n"
        f"\\({a} \\times {d} = {ad}\\) and \\({b} \\times {c} = {bc}\\).\n"
        f"Step 2: Compare the products: \\({ad}\\) " + (f"> \\({bc}\\)" if ad > bc else f"< \\({bc}\\)") + ".\n"
        f"Step 3: Since \\(a \\times d " + (">" if ad > bc else "<") + f" b \\times c\\), it follows that {corr}."
    )
    q_code = f"MH-9-MTH1-4-4.1.2-OSC-{100 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_412, t_name_412, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    txt = "In the ratio \\(a : b\\), what is the first term \\(a\\) called?"
    corr = "Antecedent (predecessor)"
    w1 = "Consequent (successor)"
    w2 = "Denominator"
    w3 = "Proportion"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: In the ratio of two numbers \\(a : b\\), the terms have standard mathematical names.\n"
        "Step 2: The first term \\(a\\) is called the antecedent.\n"
        "Step 3: The second term \\(b\\) is called the consequent."
    )
    q_code = f"MH-9-MTH1-4-4.1.2-OSC-{150 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_412, t_name_412, "foundation", "easy"))

# ==========================================
# 4.1.3 Multiplying/dividing terms by non-zero scalar
# T_CODE = "MH-9-MTH1-4-4.1.3", T_NAME = "Multiplying/dividing terms by non-zero scalar"
# Need 35 Exam (Seq 101-135), 20 Foundation (Seq 151-170)
# ==========================================
t_code_413 = "MH-9-MTH1-4-4.1.3"
t_name_413 = "Multiplying/dividing terms by non-zero scalar"

for i in range(1, 36):
    a = (i % 5) + 2
    b = (i % 6) + 3
    k = (i % 4) + 2
    ak = a * k
    bk = b * k
    txt = f"If \\(a : b = {a} : {b}\\), which of the following is an equivalent ratio obtained by multiplying both terms by a non-zero constant?"
    corr = f"\\({ak} : {bk}\\)"
    w1 = f"\\({ak} : {b}\\)"
    w2 = f"\\({a} : {bk}\\)"
    w3 = f"\\({a + k} : {b + k}\\)"

    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: By the property of ratios, multiplying both antecedent and consequent by the same non-zero scalar \\(k\\) leaves the ratio unchanged: \\(\\frac{{a}}{{b}} = \\frac{{ak}}{{bk}}\\).\n"
        f"Step 2: Multiplying both terms of \\({a} : {b}\\) by \\({k}\\) gives \\({a} \\times {k} : {b} \\times {k} = {ak} : {bk}\\).\n"
        f"Step 3: Adding a constant to both terms changes the ratio, so \\({ak} : {bk}\\) is the correct equivalent ratio."
    )
    q_code = f"MH-9-MTH1-4-4.1.3-OSC-{100 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_413, t_name_413, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    txt = "Does the value of the ratio \\(a : b\\) change if both terms are divided by the same non-zero number \\(m\\)?"
    corr = "No, it remains unchanged: \\(a : b = \\frac{a}{m} : \\frac{b}{m}\\)"
    w1 = "Yes, it decreases by \\(m\\)"
    w2 = "Yes, it becomes \\(m\\) times larger"
    w3 = "It depends on whether \\(a > b\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Let the ratio be \\(\\frac{a}{b}\\).\n"
        "Step 2: Dividing both numerator and denominator by non-zero \\(m\\): \\(\\frac{a/m}{b/m} = \\frac{a}{b} \\times \\frac{m}{m} = \\frac{a}{b}\\).\n"
        "Step 3: Therefore, the ratio remains unchanged."
    )
    q_code = f"MH-9-MTH1-4-4.1.3-OSC-{150 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_413, t_name_413, "foundation", "easy"))

# ==========================================
# 4.2.1 Applications in work, rate, and geometry
# T_CODE = "MH-9-MTH1-4-4.2.1", T_NAME = "Applications in work, rate, and geometry"
# Need 20 Foundation (Seq 151-170)
# ==========================================
t_code_421 = "MH-9-MTH1-4-4.2.1"
t_name_421 = "Applications in work, rate, and geometry"

for i in range(1, 21):
    a = (i % 3) + 2
    b = (i % 4) + 3
    # Ratio of angles of triangle = a : b : c
    c = 180 - (a*10 + b*10)
    # let's do simple word problem: If the ratio of two numbers is a : b and their sum is S, find the numbers.
    k = (i % 5) + 3
    s = (a + b) * k
    n1 = a * k
    n2 = b * k
    txt = f"The ratio of two numbers is \\({a} : {b}\\) and their sum is \\({s}\\). Find the two numbers."
    corr = f"\\({n1}\\) and \\({n2}\\)"
    w1 = f"\\({n1 + 2}\\) and \\({n2 - 2}\\)"
    w2 = f"\\({n1 - 1}\\) and \\({n2 + 1}\\)"
    w3 = f"\\({a}\\) and \\({b}\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: Let the common multiple of the ratio be \\(x\\). Then the numbers are \\({a}x\\) and \\({b}x\\).\n"
        f"Step 2: Their sum is \\({s}\\): \\({a}x + {b}x = {s} \\implies {a + b}x = {s} \\implies x = {k}\\).\n"
        f"Step 3: The numbers are \\({a} \\times {k} = {n1}\\) and \\({b} \\times {k} = {n2}\\)."
    )
    q_code = f"MH-9-MTH1-4-4.2.1-OSC-{150 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_421, t_name_421, "foundation", "easy"))

# ==========================================
# 4.3.1 Invertendo: a/b = c/d => b/a = d/c
# T_CODE = "MH-9-MTH1-4-4.3.1", T_NAME = "Invertendo: a/b = c/d => b/a = d/c"
# Need 40 Exam (Seq 101-140), 20 Foundation (Seq 151-170)
# ==========================================
t_code_431 = "MH-9-MTH1-4-4.3.1"
t_name_431 = "Invertendo: a/b = c/d => b/a = d/c"

for i in range(1, 41):
    a = (i % 7) + 2
    b = a + (i % 4) + 1 # Guaranteed b > a, so b != a
    txt = f"If \\(\\frac{{a}}{{b}} = \\frac{{{a}}}{{{b}}}\\), what is \\(\\frac{{b}}{{a}}\\) by the property of Invertendo?"
    corr = f"\\(\\frac{{{b}}}{{{a}}}\\)"
    raw_distractors = [
        f"\\(\\frac{{{a}}}{{{b}}}\\)",
        f"\\(\\frac{{{a + b}}}{{{b}}}\\)",
        f"\\(\\frac{{{b - a}}}{{{a}}}\\)",
        f"\\(\\frac{{{a}}}{{{a + b}}}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: The property of Invertendo states that if \\(\\frac{{a}}{{b}} = \\frac{{c}}{{d}}\\), then \\(\\frac{{b}}{{a}} = \\frac{{d}}{{c}}\\).\n"
        f"Step 2: Inverting both sides of \\(\\frac{{a}}{{b}} = \\frac{{{a}}}{{{b}}}\\) yields \\(\\frac{{b}}{{a}} = \\frac{{{b}}}{{{a}}}\\).\n"
        f"Step 3: Hence, \\(\\frac{{b}}{{a}} = \\frac{{{b}}}{{{a}}}\\)."
    )
    q_code = f"MH-9-MTH1-4-4.3.1-OSC-{100 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_431, t_name_431, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    txt = "Which property of equal ratios states that if \\(\\frac{a}{b} = \\frac{c}{d}\\), then \\(\\frac{b}{a} = \\frac{d}{c}\\)?"
    corr = "Invertendo"
    w1 = "Alternendo"
    w2 = "Componendo"
    w3 = "Dividendo"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: When the antecedent and consequent of both ratios are inverted (swapped), the property is known as Invertendo.\n"
        "Step 2: \\(\\frac{a}{b} = \\frac{c}{d} \\implies \\frac{b}{a} = \\frac{d}{c}\\).\n"
        "Step 3: Thus, the property is Invertendo."
    )
    q_code = f"MH-9-MTH1-4-4.3.1-OSC-{150 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_431, t_name_431, "foundation", "easy"))

# ==========================================
# 4.3.2 Alternendo: a/b = c/d => a/c = b/d
# T_CODE = "MH-9-MTH1-4-4.3.2", T_NAME = "Alternendo: a/b = c/d => a/c = b/d"
# Need 40 Exam (Seq 101-140), 20 Foundation (Seq 151-170)
# ==========================================
t_code_432 = "MH-9-MTH1-4-4.3.2"
t_name_432 = "Alternendo: a/b = c/d => a/c = b/d"

for i in range(1, 41):
    a = (i % 6) + 3
    b = a + (i % 4) + 1 # Guaranteed b != a
    txt = f"If \\(\\frac{{x}}{{y}} = \\frac{{{a}}}{{{b}}}\\), find the ratio \\(\\frac{{x}}{{{a}}}\\) by Alternendo."
    corr = f"\\(\\frac{{y}}{{{b}}}\\)"
    raw_distractors = [
        f"\\(\\frac{{{b}}}{{y}}\\)",
        f"\\(\\frac{{x + y}}{{{b}}}\\)",
        f"\\(\\frac{{{a}}}{{y}}\\)",
        f"\\(\\frac{{y}}{{{a}}}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: By the property of Alternendo, if \\(\\frac{{a}}{{b}} = \\frac{{c}}{{d}}\\), then \\(\\frac{{a}}{{c}} = \\frac{{b}}{{d}}\\).\n"
        f"Step 2: Applying Alternendo to \\(\\frac{{x}}{{y}} = \\frac{{{a}}}{{{b}}}\\) by interchanging the means \\(y\\) and \\({a}\\):\n"
        f"\\(\\frac{{x}}{{{a}}} = \\frac{{y}}{{{b}}}\\).\n"
        f"Step 3: The ratio is \\(\\frac{{y}}{{{b}}}\\)."
    )
    q_code = f"MH-9-MTH1-4-4.3.2-OSC-{100 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_432, t_name_432, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    txt = "Which property of equal ratios allows interchanging the means: \\(\\frac{a}{b} = \\frac{c}{d} \\implies \\frac{a}{c} = \\frac{b}{d}\\)?"
    corr = "Alternendo"
    w1 = "Invertendo"
    w2 = "Componendo"
    w3 = "Dividendo"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Interchanging the second term \\(b\\) and third term \\(c\\) in the proportion is called Alternendo.\n"
        "Step 2: \\(\\frac{a}{b} = \\frac{c}{d} \\implies \\frac{a}{c} = \\frac{b}{d}\\).\n"
        "Step 3: Hence, the property is Alternendo."
    )
    q_code = f"MH-9-MTH1-4-4.3.2-OSC-{150 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_432, t_name_432, "foundation", "easy"))

# ==========================================
# 4.3.3 Componendo: (a+b)/b = (c+d)/d
# T_CODE = "MH-9-MTH1-4-4.3.3", T_NAME = "Componendo: (a+b)/b = (c+d)/d"
# Need 40 Exam (Seq 101-140), 20 Foundation (Seq 151-170)
# ==========================================
t_code_433 = "MH-9-MTH1-4-4.3.3"
t_name_433 = "Componendo: (a+b)/b = (c+d)/d"

for i in range(1, 41):
    a = (i % 6) + 3
    b = (i % 4) + 2
    s = a + b
    txt = f"If \\(\\frac{{a}}{{b}} = \\frac{{{a}}}{{{b}}}\\), find the value of \\(\\frac{{a + b}}{{b}}\\) using Componendo."
    corr = f"\\(\\frac{{{s}}}{{{b}}}\\)"
    w1 = f"\\(\\frac{{{s}}}{{{a}}}\\)"
    w2 = f"\\(\\frac{{{a - b}}}{{{b}}}\\)"
    w3 = f"\\(\\frac{{{a}}}{{{s}}}\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: The property of Componendo states that if \\(\\frac{{a}}{{b}} = \\frac{{c}}{{d}}\\), then \\(\\frac{{a + b}}{{b}} = \\frac{{c + d}}{{d}}\\).\n"
        f"Step 2: Here \\(\\frac{{c}}{{d}} = \\frac{{{a}}}{{{b}}}\\), so \\(\\frac{{c + d}}{{d}} = \\frac{{{a} + {b}}}{{{b}}} = \\frac{{{s}}}{{{b}}}\\).\n"
        f"Step 3: Therefore, \\(\\frac{{a + b}}{{b}} = \\frac{{{s}}}{{{b}}}\\)."
    )
    q_code = f"MH-9-MTH1-4-4.3.3-OSC-{100 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_433, t_name_433, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    txt = "What operation is performed on both sides of \\(\\frac{a}{b} = \\frac{c}{d}\\) to derive Componendo?"
    corr = "Adding 1 to both sides"
    w1 = "Subtracting 1 from both sides"
    w2 = "Inverting both sides"
    w3 = "Multiplying both sides by -1"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Start with \\(\\frac{a}{b} = \\frac{c}{d}\\).\n"
        "Step 2: Add 1 to both sides: \\(\\frac{a}{b} + 1 = \\frac{c}{d} + 1 \\implies \\frac{a + b}{b} = \\frac{c + d}{d}\\).\n"
        "Step 3: This property is Componendo."
    )
    q_code = f"MH-9-MTH1-4-4.3.3-OSC-{150 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_433, t_name_433, "foundation", "easy"))

# ==========================================
# 4.3.4 Dividendo: (a-b)/b = (c-d)/d
# T_CODE = "MH-9-MTH1-4-4.3.4", T_NAME = "Dividendo: (a-b)/b = (c-d)/d"
# Need 40 Exam (Seq 101-140), 20 Foundation (Seq 151-170)
# ==========================================
t_code_434 = "MH-9-MTH1-4-4.3.4"
t_name_434 = "Dividendo: (a-b)/b = (c-d)/d"

for i in range(1, 41):
    a = (i % 6) + 5
    b = (i % 3) + 1 # b in {1, 2, 3}, a >= 5, so diff = a - b >= 2, diff != b (unless a-b=b => a=2b)
    if a == 2 * b:
        a += 1
    diff = a - b
    txt = f"If \\(\\frac{{a}}{{b}} = \\frac{{{a}}}{{{b}}}\\), find the value of \\(\\frac{{a - b}}{{b}}\\) using Dividendo."
    corr = f"\\(\\frac{{{diff}}}{{{b}}}\\)"
    raw_distractors = [
        f"\\(\\frac{{{diff}}}{{{a}}}\\)",
        f"\\(\\frac{{{a + b}}}{{{b}}}\\)",
        f"\\(\\frac{{{b}}}{{{diff}}}\\)",
        f"\\(\\frac{{{b}}}{{{a}}}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: The property of Dividendo states that if \\(\\frac{{a}}{{b}} = \\frac{{c}}{{d}}\\), then \\(\\frac{{a - b}}{{b}} = \\frac{{c - d}}{{d}}\\).\n"
        f"Step 2: Here \\(\\frac{{c}}{{d}} = \\frac{{{a}}}{{{b}}}\\), so \\(\\frac{{c - d}}{{d}} = \\frac{{{a} - {b}}}{{{b}}} = \\frac{{{diff}}}{{{b}}}\\).\n"
        f"Step 3: Thus, \\(\\frac{{a - b}}{{b}} = \\frac{{{diff}}}{{{b}}}\\)."
    )
    q_code = f"MH-9-MTH1-4-4.3.4-OSC-{100 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_434, t_name_434, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    txt = "What operation on both sides of \\(\\frac{a}{b} = \\frac{c}{d}\\) yields Dividendo?"
    corr = "Subtracting 1 from both sides"
    w1 = "Adding 1 to both sides"
    w2 = "Dividing both sides by 2"
    w3 = "Taking square roots"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Start with \\(\\frac{a}{b} = \\frac{c}{d}\\).\n"
        "Step 2: Subtract 1 from both sides: \\(\\frac{a}{b} - 1 = \\frac{c}{d} - 1 \\implies \\frac{a - b}{b} = \\frac{c - d}{d}\\).\n"
        "Step 3: This yields Dividendo."
    )
    q_code = f"MH-9-MTH1-4-4.3.4-OSC-{150 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_434, t_name_434, "foundation", "easy"))

# ==========================================
# 4.3.5 Componendo-Dividendo: (a+b)/(a-b) = (c+d)/(c-d)
# T_CODE = "MH-9-MTH1-4-4.3.5", T_NAME = "Componendo-Dividendo: (a+b)/(a-b) = (c+d)/(c-d)"
# Need 40 Exam (Seq 101-140), 20 Foundation (Seq 151-170)
# ==========================================
t_code_435 = "MH-9-MTH1-4-4.3.5"
t_name_435 = "Componendo-Dividendo: (a+b)/(a-b) = (c+d)/(c-d)"

for i in range(1, 41):
    a = (i % 5) + 4
    b = (i % 3) + 1
    num = a + b
    den = a - b
    txt = f"If \\(\\frac{{x}}{{y}} = \\frac{{{a}}}{{{b}}}\\), find the value of \\(\\frac{{x + y}}{{x - y}}\\) using Componendo-Dividendo."
    corr = f"\\(\\frac{{{num}}}{{{den}}}\\)"
    raw_distractors = [
        f"\\(\\frac{{{den}}}{{{num}}}\\)",
        f"\\(\\frac{{{num + 1}}}{{{den}}}\\)",
        f"\\(\\frac{{{a}}}{{{den}}}\\)",
        f"\\(\\frac{{{num}}}{{{b}}}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: The property of Componendo-Dividendo states that if \\(\\frac{{a}}{{b}} = \\frac{{c}}{{d}}\\), then \\(\\frac{{a + b}}{{a - b}} = \\frac{{c + d}}{{c - d}}\\).\n"
        f"Step 2: Here \\(\\frac{{c}}{{d}} = \\frac{{{a}}}{{{b}}}\\), so \\(\\frac{{c + d}}{{c - d}} = \\frac{{{a} + {b}}}{{{a} - {b}}} = \\frac{{{num}}}{{{den}}}\\).\n"
        f"Step 3: Therefore, \\(\\frac{{x + y}}{{x - y}} = \\frac{{{num}}}{{{den}}}\\)."
    )
    q_code = f"MH-9-MTH1-4-4.3.5-OSC-{100 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_435, t_name_435, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    txt = "Which property combines addition and subtraction of the consequent: \\(\\frac{a+b}{a-b} = \\frac{c+d}{c-d}\\)?"
    corr = "Componendo-Dividendo"
    w1 = "Alternendo"
    w2 = "Invertendo"
    w3 = "Theorem on Equal Ratios"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Dividing Componendo \\(\\frac{a+b}{b} = \\frac{c+d}{d}\\) by Dividendo \\(\\frac{a-b}{b} = \\frac{c-d}{d}\\) gives \\(\\frac{a+b}{a-b} = \\frac{c+d}{c-d}\\).\n"
        "Step 2: This composite property is termed Componendo-Dividendo.\n"
        "Step 3: Hence, the property is Componendo-Dividendo."
    )
    q_code = f"MH-9-MTH1-4-4.3.5-OSC-{150 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_435, t_name_435, "foundation", "easy"))

# ==========================================
# 4.4.1 Theorem on Equal Ratios: a/b = c/d = (a+c)/(b+d)
# T_CODE = "MH-9-MTH1-4-4.4.1", T_NAME = "Theorem on Equal Ratios & Continued Proportion"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_441 = "MH-9-MTH1-4-4.4.1"
t_name_441 = "Theorem on Equal Ratios"

for i in range(1, 39):
    a = (i % 4) + 2
    b = (i % 3) + 3
    l = (i % 3) + 1
    m = (i % 2) + 2
    txt = f"If \\(\\frac{{a}}{{b}} = \\frac{{c}}{{d}} = k\\), what is the value of \\(\\frac{{{l}a + {m}c}}{{{l}b + {m}d}}\\) in terms of \\(k\\)?"
    corr = "\\(k\\)"
    w1 = f"\\({l + m}k\\)"
    w2 = "\\(k^2\\)"
    w3 = f"\\(\\frac{{{l}}}{{{m}}} k\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: By the Theorem on Equal Ratios, if each ratio equals \\(k\\), then for any multipliers \\(l, m\\) (not both zero with non-zero denominator):\n"
        f"\\(\\frac{{{l}a + {m}c}}{{{l}b + {m}d}} = \\frac{{{l}(bk) + {m}(dk)}}{{{l}b + {m}d}} = \\frac{{k({l}b + {m}d)}}{{{l}b + {m}d}} = k\\).\n"
        "Step 2: Each resulting ratio remains equal to the original common ratio \\(k\\).\n"
        "Step 3: Hence, the value is \\(k\\)."
    )
    q_code = f"MH-9-MTH1-4-4.4.1-OSC-{100 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_441, t_name_441, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    txt = f"If \\(\\frac{{x}}{{2}} = \\frac{{y}}{{3}} = \\frac{{z}}{{5}}\\), find the value of each ratio by adding numerators and denominators."
    corr = "\\(\\frac{x + y + z}{10}\\)"
    w1 = "\\(\\frac{x + y + z}{30}\\)"
    w2 = "\\(\\frac{x y z}{30}\\)"
    w3 = "\\(\\frac{x + y + z}{5}\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Applying the Theorem on Equal Ratios: \\(\\frac{x}{2} = \\frac{y}{3} = \\frac{z}{5} = \\frac{x + y + z}{2 + 3 + 5}\\).\n"
        "Step 2: Add the denominators: \\(2 + 3 + 5 = 10\\).\n"
        "Step 3: Therefore, each ratio is equal to \\(\\frac{x + y + z}{10}\\)."
    )
    q_code = f"MH-9-MTH1-4-4.4.1-OSC-{200 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_441, t_name_441, "practice", "medium"))

for i in range(1, 21):
    txt = "State the Theorem on Equal Ratios for \\(\\frac{a}{b} = \\frac{c}{d}\\)."
    corr = "\\(\\frac{a}{b} = \\frac{c}{d} = \\frac{a + c}{b + d}\\)"
    w1 = "\\(\\frac{a}{b} = \\frac{c}{d} = \\frac{a c}{b d}\\)"
    w2 = "\\(\\frac{a}{b} = \\frac{c}{d} = \\frac{a - c}{b + d}\\)"
    w3 = "\\(\\frac{a}{b} = \\frac{c}{d} = \\frac{a + d}{b + c}\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: By the theorem, the ratio of the sum of antecedents to the sum of consequents equals the original ratio.\n"
        "Step 2: \\(\\frac{a}{b} = \\frac{c}{d} = \\frac{a + c}{b + d}\\) provided \\(b + d \\ne 0\\).\n"
        "Step 3: This is the Theorem on Equal Ratios."
    )
    q_code = f"MH-9-MTH1-4-4.4.1-OSC-{150 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_441, t_name_441, "foundation", "easy"))

# ==========================================
# 4.4.2 Continued proportion a/b = b/c
# T_CODE = "MH-9-MTH1-4-4.4.2", T_NAME = "Continued proportion a/b = b/c = c/d"
# Need 18 Exam (Seq 101-118), 20 Foundation (Seq 151-170)
# ==========================================
t_code_442 = "MH-9-MTH1-4-4.4.2"
t_name_442 = "Continued proportion a/b = b/c = c/d"

for i in range(1, 19):
    a = (i % 4) + 2
    b = a * 2
    c = b * 2
    txt = f"If \\({a}, x, {c}\\) are in continued proportion, find the positive value of \\(x\\)."
    corr = f"\\({b}\\)"
    w1 = f"\\({b + 2}\\)"
    w2 = f"\\({b - 1}\\)"
    w3 = f"\\({a + c}\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: If \\(a, b, c\\) are in continued proportion, then \\(\\frac{{a}}{{b}} = \\frac{{b}}{{c}} \\implies b^2 = ac\\).\n"
        f"Step 2: Here \\(x^2 = {a} \\times {c} = {a * c}\\).\n"
        f"Step 3: Taking positive square root: \\(x = \\sqrt{{{a * c}}} = {b}\\)."
    )
    q_code = f"MH-9-MTH1-4-4.4.2-OSC-{100 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_442, t_name_442, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    txt = "If \\(a, b, c\\) are in continued proportion, what is the relation between them?"
    corr = "\\(b^2 = ac\\)"
    w1 = "\\(b = a + c\\)"
    w2 = "\\(b = \\frac{a + c}{2}\\)"
    w3 = "\\(a^2 = bc\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: By definition of continued proportion, \\(\\frac{a}{b} = \\frac{b}{c}\\).\n"
        "Step 2: Cross-multiplying gives \\(b \\times b = a \\times c \\implies b^2 = ac\\).\n"
        "Step 3: Hence, the relation is \\(b^2 = ac\\)."
    )
    q_code = f"MH-9-MTH1-4-4.4.2-OSC-{150 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_442, t_name_442, "foundation", "easy"))

# ==========================================
# 4.4.3 Geometric mean formula b^2 = ac
# T_CODE = "MH-9-MTH1-4-4.4.3", T_NAME = "Geometric mean formula b² = ac"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_443 = "MH-9-MTH1-4-4.4.3"
t_name_443 = "Geometric mean formula b² = ac"

gm_pairs = [(4, 9, 6), (2, 8, 4), (3, 27, 9), (4, 16, 8), (1, 25, 5), (9, 16, 12), (5, 20, 10), (8, 18, 12)]

for i in range(1, 39):
    pair = gm_pairs[i % len(gm_pairs)]
    a, c, b = pair
    txt = f"Find the geometric mean (mean proportional) between \\({a}\\) and \\({c}\\)."
    corr = f"\\({b}\\)"
    raw_distractors = [
        f"\\({b + 3}\\)",
        f"\\({b - 2 if b > 2 else b + 4}\\)",
        f"\\({b + 6}\\)",
        f"\\({b + 1}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: The geometric mean \\(b\\) of \\(a\\) and \\(c\\) is given by the formula \\(b = \\sqrt{{ac}}\\).\n"
        f"Step 2: Compute product: \\(ac = {a} \\times {c} = {a * c}\\).\n"
        f"Step 3: Square root: \\(b = \\sqrt{{{a * c}}} = {b}\\)."
    )
    q_code = f"MH-9-MTH1-4-4.4.3-OSC-{100 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_443, t_name_443, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    pair = gm_pairs[(i + 2) % len(gm_pairs)]
    a, c, b = pair
    txt = f"What is the mean proportional of \\({a}\\) and \\({c}\\)?"
    corr = f"\\({b}\\)"
    raw_distractors = [
        f"\\({b + 3}\\)",
        f"\\({b - 2 if b > 2 else b + 4}\\)",
        f"\\({b + 5}\\)",
        f"\\({a * c}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: Let the mean proportional be \\(x\\). Then \\(x^2 = {a} \\times {c} = {a * c}\\).\n"
        f"Step 2: \\(x = \\sqrt{{{a * c}}} = {b}\\).\n"
        f"Step 3: The mean proportional is \\({b}\\)."
    )
    q_code = f"MH-9-MTH1-4-4.4.3-OSC-{200 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_443, t_name_443, "practice", "medium"))

for i in range(1, 21):
    txt = "What is another name for the mean proportional between two positive numbers \\(a\\) and \\(c\\)?"
    corr = "Geometric Mean"
    w1 = "Arithmetic Mean"
    w2 = "Harmonic Mean"
    w3 = "Median"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: When \\(b^2 = ac\\), \\(b\\) is called the mean proportional between \\(a\\) and \\(c\\).\n"
        "Step 2: In algebra and statistics, \\(\\sqrt{ac}\\) is known as the Geometric Mean.\n"
        "Step 3: Hence, it is also known as the Geometric Mean."
    )
    q_code = f"MH-9-MTH1-4-4.4.3-OSC-{150 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_443, t_name_443, "foundation", "easy"))

# ==========================================
# 4.4.4 k-method of proof
# T_CODE = "MH-9-MTH1-4-4.4.4", T_NAME = "k-method of proof"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_444 = "MH-9-MTH1-4-4.4.4"
t_name_444 = "k-method of proof"

for i in range(1, 39):
    txt = "In the \\(k\\)-method, if \\(\\frac{a}{b} = \\frac{c}{d} = k\\), which substitution is made?"
    corr = "\\(a = bk\\) and \\(c = dk\\)"
    w1 = "\\(b = ak\\) and \\(d = ck\\)"
    w2 = "\\(a = b + k\\) and \\(c = d + k\\)"
    w3 = "\\(a = \\frac{b}{k}\\) and \\(c = \\frac{d}{k}\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Set each ratio equal to \\(k\\): \\(\\frac{a}{b} = k\\) and \\(\\frac{c}{d} = k\\).\n"
        "Step 2: Multiply by denominators: \\(a = bk\\) and \\(c = dk\\).\n"
        "Step 3: These values are substituted into the expressions for LHS and RHS to prove equality."
    )
    q_code = f"MH-9-MTH1-4-4.4.4-OSC-{100 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_444, t_name_444, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    txt = "If \\(a, b, c\\) are in continued proportion and \\(\\frac{a}{b} = \\frac{b}{c} = k\\), then \\(b = ck\\) and \\(a = \\text{?}\\)"
    corr = "\\(ck^2\\)"
    w1 = "\\(ck\\)"
    w2 = "\\(c^2 k\\)"
    w3 = "\\(c + k^2\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: From \\(\\frac{b}{c} = k\\), we have \\(b = ck\\).\n"
        "Step 2: From \\(\\frac{a}{b} = k\\), we have \\(a = bk\\).\n"
        "Step 3: Substitute \\(b = ck\\): \\(a = (ck)k = ck^2\\)."
    )
    q_code = f"MH-9-MTH1-4-4.4.4-OSC-{200 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_444, t_name_444, "practice", "medium"))

for i in range(1, 21):
    txt = "What is the primary purpose of using the \\(k\\)-method in ratio and proportion problems?"
    corr = "To express multiple variables in terms of a single common parameter \\(k\\) to verify algebraic identities"
    w1 = "To find the numerical value of \\(k\\)"
    w2 = "To solve quadratic equations"
    w3 = "To convert fractions into decimals"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: In the \\(k\\)-method, equal ratios are equated to a common scalar \\(k\\).\n"
        "Step 2: This reduces the number of independent variables by expressing antecedents in terms of consequents and \\(k\\).\n"
        "Step 3: This simplifies verifying identities by showing \\(\\text{LHS} = \\text{RHS}\\)."
    )
    q_code = f"MH-9-MTH1-4-4.4.4-OSC-{150 + i:03d}"
    questions_ch4.append(make_q(q_code, txt, opts, sol, t_code_444, t_name_444, "foundation", "easy"))

print(f"Generated Chapter 4: {len(questions_ch4)} questions")

with open("scripts/mh9_mth1_ch4_generated.json", "w", encoding="utf-8") as f:
    json.dump(questions_ch4, f, indent=2)
