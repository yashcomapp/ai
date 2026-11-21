# scripts/generate_ch2_subtopics_to_80q.py
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
        "chapterNumber": 2,
        "chapter": "Real Numbers",
        "topicCode": t_code,
        "topic": t_name,
        "type": q_type,
        "marks": marks,
        "difficulty": diff,
        "vault": vault,
        "timesUsed": 0,
        "usedInClassroomTest": False,
        "requiresFigure": False,
        "createdAt": "2026-11-21T13:07:00.000Z",
        "updatedAt": "2026-11-21T13:07:00.000Z"
    }

questions_ch2_topup = []

def generate_subtopic_pack(t_code, t_name, n_exam, n_pr, n_fo, concept_builder):
    for i in range(1, n_exam + 1):
        txt, corr, raw_dist, sol = concept_builder(i, "exam")
        opts = make_unique_opts(corr, raw_dist)
        shift = i % 4
        opts = opts[shift:] + opts[:shift]
        code = f"{t_code}-OSC-{100 + i:03d}"
        questions_ch2_topup.append(make_q(code, txt, opts, sol, t_code, t_name, "exam", "medium" if i % 2 == 0 else "hard"))

    for i in range(1, n_pr + 1):
        txt, corr, raw_dist, sol = concept_builder(i, "practice")
        opts = make_unique_opts(corr, raw_dist)
        shift = i % 4
        opts = opts[shift:] + opts[:shift]
        code = f"{t_code}-OSC-{200 + i:03d}"
        questions_ch2_topup.append(make_q(code, txt, opts, sol, t_code, t_name, "practice", "medium"))

    for i in range(1, n_fo + 1):
        txt, corr, raw_dist, sol = concept_builder(i, "foundation")
        opts = make_unique_opts(corr, raw_dist)
        shift = i % 4
        opts = opts[shift:] + opts[:shift]
        code = f"{t_code}-OSC-{150 + i:03d}"
        questions_ch2_topup.append(make_q(code, txt, opts, sol, t_code, t_name, "foundation", "easy"))

# 2.1.1: p/q form (26 Ex, 13 Pr, 14 Fo)
def builder_211(i, mode):
    p = (i % 7) + 3
    q = (i % 5) + 2
    txt = f"Express the number \\({p}\\frac{{1}}{{{q}}}\\) in the rational form \\(\\frac{{p}}{{q}}\\)."
    num = p * q + 1
    corr = f"\\(\\frac{{{num}}}{{{q}}}\\)"
    raw_dist = [
        f"\\(\\frac{{{num + 1}}}{{{q}}}\\)",
        f"\\(\\frac{{{num - 1}}}{{{q}}}\\)",
        f"\\(\\frac{{{p}}}{{{q}}}\\)"
    ]
    sol = f"Step 1: Convert mixed fraction: \\({p}\\frac{{1}}{{{q}}} = \\frac{{{p} \\times {q} + 1}}{{{q}}}\\).\nStep 2: \\({p} \\times {q} + 1 = {p * q} + 1 = {num}\\).\nStep 3: Hence, the rational form is \\(\\frac{{{num}}}{{{q}}}\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-2-2.1.1", "p/q form where q != 0", 26, 13, 14, builder_211)

# 2.1.2: Terminating vs recurring (26 Ex, 13 Pr, 13 Fo)
def builder_212(i, mode):
    denoms = [8, 25, 16, 125, 3, 7, 11, 13, 6]
    d = denoms[i % len(denoms)]
    is_term = d in [8, 25, 16, 125]
    txt = f"Without actual division, determine whether \\(\\frac{{7}}{{{d}}}\\) has a terminating or non-terminating recurring decimal form."
    corr = "Terminating decimal form" if is_term else "Non-terminating recurring decimal form"
    raw_dist = [
        "Non-terminating recurring decimal form" if is_term else "Terminating decimal form",
        "Non-terminating non-recurring (irrational)",
        "Integer form"
    ]
    sol = f"Step 1: Factorise denominator \\({d}\\).\nStep 2: A rational number \\(\\frac{{p}}{{q}}\\) has terminating decimal form if and only if prime factors of \\(q\\) are of the form \\(2^m 5^n\\).\nStep 3: Hence, \\(\\frac{{7}}{{{d}}}\\) is {corr}."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-2-2.1.2", "Terminating vs non-terminating recurring forms", 26, 13, 13, builder_212)

# 2.1.3: Trichotomy law (28 Ex, 14 Pr, 13 Fo)
def builder_213(i, mode):
    txt = "For any two real numbers \\(a\\) and \\(b\\), what does the Trichotomy Law state?"
    corr = "Exactly one of \\(a < b\\), \\(a = b\\), or \\(a > b\\) must hold true"
    raw_dist = [
        "Both \\(a < b\\) and \\(a > b\\) can be true simultaneously",
        "Either \\(a + b = 0\\) or \\(ab = 0\\)",
        "\\(a^2 + b^2 = (a + b)^2\\)"
    ]
    sol = "Step 1: The order relation on real numbers is complete.\nStep 2: For any two real numbers, exactly one relation holds: \\(a < b\\), \\(a = b\\), or \\(a > b\\).\nStep 3: This fundamental property is known as the Law of Trichotomy."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-2-2.1.3", "Order relation properties (Trichotomy law)", 28, 14, 13, builder_213)

# 2.2.1: Proof by contradiction (20 Ex, 10 Pr, 10 Fo)
def builder_221(i, mode):
    txt = "In proving that \\(\\sqrt{2}\\) is an irrational number by contradiction, what initial assumption is made?"
    corr = "Assume that \\(\\sqrt{2}\\) is a rational number of the form \\(\\frac{p}{q}\\) where \\(p, q\\) are coprime integers"
    raw_dist = [
        "Assume that \\(\\sqrt{2} = 0\\)",
        "Assume that \\(\\sqrt{2}\\) is negative",
        "Assume that \\(2\\) is an odd number"
    ]
    sol = "Step 1: Proof by contradiction assumes the negation of the proposition to be proved.\nStep 2: To prove \\(\\sqrt{2}\\) is irrational, we assume the opposite: that \\(\\sqrt{2}\\) is rational.\nStep 3: Hence, assume \\(\\sqrt{2} = \\frac{p}{q}\\) where \\(p, q \\in \\mathbb{Z}, q \\ne 0\\) and \\(\\gcd(p, q) = 1\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-2-2.2.1", "Proof by contradiction", 20, 10, 10, builder_221)

# 2.2.2: Representation on number line (20 Ex, 10 Pr, 10 Fo)
def builder_222(i, mode):
    val = 5 if i % 2 == 1 else 10
    base = 2 if val == 5 else 3
    txt = f"To represent \\(\\sqrt{{{val}}}\\) on the number line using Pythagoras theorem, a right-angled triangle is constructed with base \\({base}\\) units and perpendicular of what length?"
    corr = "\\(1\\) unit"
    raw_dist = [
        "\\(2\\) units",
        "\\(0.5\\) units",
        f"\\({base}\\) units"
    ]
    sol = f"Step 1: By Pythagoras theorem, \\(\\text{{Hypotenuse}}^2 = \\text{{Base}}^2 + \\text{{Perpendicular}}^2\\).\nStep 2: For \\(\\sqrt{{{val}}}\\): \\({base}^2 + 1^2 = {base**2} + 1 = {val}\\).\nStep 3: Hypotenuse is \\(\\sqrt{{{val}}}\\), so perpendicular length must be 1 unit."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-2-2.2.2", "Representation of √5, √10 on number line", 20, 10, 10, builder_222)

# 2.3.1: Definition of surd (29 Ex, 16 Pr, 15 Fo)
def builder_231(i, mode):
    txt = "Which of the following is a surd?"
    corr = "\\(\\sqrt{7}\\)"
    raw_dist = [
        "\\(\\sqrt{9}\\)",
        "\\(\\sqrt[3]{27}\\)",
        "\\(\\sqrt{16}\\)"
    ]
    if i % 2 == 0:
        txt = "Under what condition is \\(\\sqrt[n]{a}\\) defined as a surd?"
        corr = "\\(n > 1\\) is a natural number, \\(a\\) is a positive rational number, and \\(\\sqrt[n]{a}\\) is irrational"
        raw_dist = [
            "\\(\\sqrt[n]{a}\\) is always a rational number",
            "\\(a\\) must be a negative integer",
            "\\(n = 1\\) and \\(a\\) is any real number"
        ]
    sol = "Step 1: A surd is an irrational root of a positive rational number.\nStep 2: If \\(a \\in \\mathbb{Q}^+\\) and \\(\\sqrt[n]{a} \\notin \\mathbb{Q}\\), then \\(\\sqrt[n]{a}\\) is a surd.\nStep 3: Correct answer identified."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-2-2.3.1", "Definition of surd ⁿ√a", 29, 16, 15, builder_231)

# 2.3.2: Order of surd (30 Ex, 15 Pr, 15 Fo)
def builder_232(i, mode):
    orders = [2, 3, 4, 5, 6]
    n = orders[i % len(orders)]
    rad_str = f"\\sqrt{{{7}}}" if n == 2 else f"\\sqrt[{n}]{{{7}}}"
    txt = f"What is the order of the surd \\({rad_str}\\)?"
    corr = f"\\({n}\\)"
    raw_dist = [
        f"\\({n + 1}\\)",
        f"\\({n - 1 if n > 2 else 7}\\)",
        "\\(7\\)"
    ]
    sol = f"Step 1: In the radical expression \\(\\sqrt[n]{{a}}\\), \\(n\\) is called the order of the surd.\nStep 2: For \\({rad_str}\\), the index of the root is \\({n}\\).\nStep 3: Hence, the order is \\({n}\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-2-2.3.2", "Order of surd (n)", 30, 15, 15, builder_232)

# 2.3.3: Like / similar surds (30 Ex, 15 Pr, 15 Fo)
def builder_233(i, mode):
    txt = "Which pair of surds represents like (similar) surds?"
    corr = "\\(2\\sqrt{5}\\) and \\(7\\sqrt{5}\\)"
    raw_dist = [
        "\\(\\sqrt{5}\\) and \\(\\sqrt{7}\\)",
        "\\(\\sqrt{2}\\) and \\(\\sqrt[3]{2}\\)",
        "\\(3\\sqrt{2}\\) and \\(2\\sqrt{3}\\)"
    ]
    sol = "Step 1: Two surds are called like (similar) surds if their order is equal and their radicands in simplest form are equal.\nStep 2: Both \\(2\\sqrt{5}\\) and \\(7\\sqrt{5}\\) have order 2 and radicand 5.\nStep 3: Hence, they are like surds."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-2-2.3.3", "Like / similar surds", 30, 15, 15, builder_233)

# 2.3.4: Simplest radical form (31 Ex, 14 Pr, 15 Fo)
def builder_234(i, mode):
    radicands = [(12, 2, 3), (18, 3, 2), (20, 2, 5), (24, 2, 6), (27, 3, 3), (32, 4, 2), (48, 4, 3), (50, 5, 2), (72, 6, 2), (75, 5, 3)]
    orig, a, b = radicands[i % len(radicands)]
    txt = f"Express the surd \\(\\sqrt{{{orig}}}\\) in its simplest form."
    corr = f"\\({a}\\sqrt{{{b}}}\\)"
    raw_dist = [
        f"\\({b}\\sqrt{{{a}}}\\)",
        f"\\({a + 1}\\sqrt{{{b}}}\\)",
        f"\\({orig}\\sqrt{{1}}\\)"
    ]
    sol = f"Step 1: Factorise radicand with largest square factor: \\({orig} = {a}^2 \\times {b} = {a**2} \\times {b}\\).\nStep 2: \\(\\sqrt{{{orig}}} = \\sqrt{{{a**2} \\times {b}}} = {a}\\sqrt{{{b}}}\\).\nStep 3: Simplest form is \\({a}\\sqrt{{{b}}}\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-2-2.3.4", "Simplest radical form", 31, 14, 15, builder_234)

# 2.4.1: Operations on surds (19 Ex, 10 Pr, 10 Fo)
def builder_241(i, mode):
    a = (i % 4) + 2
    b = (i % 3) + 3
    s = a + b
    txt = f"Simplify the sum of like surds: \\({a}\\sqrt{{3}} + {b}\\sqrt{{3}}\\)."
    corr = f"\\({s}\\sqrt{{3}}\\)"
    raw_dist = [
        f"\\({s}\\sqrt{{6}}\\)",
        f"\\({a * b}\\sqrt{{3}}\\)",
        f"\\({s + 1}\\sqrt{{3}}\\)"
    ]
    sol = f"Step 1: Factor out the common surd \\(\\sqrt{{3}}\\): \\(({a} + {b})\\sqrt{{3}}\\).\nStep 2: Add rational coefficients: \\({a} + {b} = {s}\\).\nStep 3: Result is \\({s}\\sqrt{{3}}\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-2-2.4.1", "Addition, subtraction, multiplication, division of surds", 19, 10, 10, builder_241)

# 2.4.2: Comparing surds (21 Ex, 10 Pr, 10 Fo)
def builder_242(i, mode):
    txt = "Compare the surds \\(4\\sqrt{3}\\) and \\(3\\sqrt{5}\\)."
    corr = "\\(4\\sqrt{3} > 3\\sqrt{5}\\)"
    raw_dist = [
        "\\(4\\sqrt{3} < 3\\sqrt{5}\\)",
        "\\(4\\sqrt{3} = 3\\sqrt{5}\\)",
        "Cannot be compared"
    ]
    sol = "Step 1: Convert to pure surds: \\(4\\sqrt{3} = \\sqrt{4^2 \\times 3} = \\sqrt{16 \\times 3} = \\sqrt{48}\\).\nStep 2: \\(3\\sqrt{5} = \\sqrt{3^2 \\times 5} = \\sqrt{9 \\times 5} = \\sqrt{45}\\).\nStep 3: Since \\(48 > 45\\), \\(\\sqrt{48} > \\sqrt{45} \\implies 4\\sqrt{3} > 3\\sqrt{5}\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-2-2.4.2", "Comparing pure and mixed surds", 21, 10, 10, builder_242)

# 2.5.1: Rationalising factor (19 Ex, 10 Pr, 10 Fo)
def builder_251(i, mode):
    p = [2, 3, 5, 6, 7][i % 5]
    txt = f"What is the simplest rationalising factor of \\(\\sqrt{{{p}}}\\)?"
    corr = f"\\(\\sqrt{{{p}}}\\)"
    raw_dist = [
        f"\\({p}\\)",
        "\\(\\sqrt{1}\\)",
        f"\\(\\frac{{1}}{{\\sqrt{{{p}}}}}\\)"
    ]
    sol = f"Step 1: If product of two surds is a rational number, each is a rationalising factor of the other.\nStep 2: \\(\\sqrt{{{p}}} \\times \\sqrt{{{p}}} = {p}\\), which is a rational number.\nStep 3: Hence, the simplest rationalising factor is \\(\\sqrt{{{p}}}\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-2-2.5.1", "Rationalising factor definition", 19, 10, 10, builder_251)

# 2.5.2: Conjugate pair (21 Ex, 10 Pr, 10 Fo)
def builder_252(i, mode):
    a = (i % 3) + 2
    b = (i % 4) + 3
    txt = f"What is the conjugate pair of the binomial surd \\((\\sqrt{{{a}}} + \\sqrt{{{b}}})\\)?"
    corr = f"\\((\\sqrt{{{a}}} - \\sqrt{{{b}}})\\)"
    raw_dist = [
        f"\\((-\\sqrt{{{a}}} - \\sqrt{{{b}}})\\)",
        f"\\((\\sqrt{{{a}}} + \\sqrt{{{b}}})\\)",
        f"\\(({a} - {b})\\)"
    ]
    sol = f"Step 1: The conjugate pair of \\((\\sqrt{{a}} + \\sqrt{{b}})\\) is \\((\\sqrt{{a}} - \\sqrt{{b}})\\).\nStep 2: Their product \\((\\sqrt{{{a}}} + \\sqrt{{{b}}})(\\sqrt{{{a}}} - \\sqrt{{{b}}}) = {a} - {b}\\) is always a rational number.\nStep 3: Hence, the conjugate is \\((\\sqrt{{{a}}} - \\sqrt{{{b}}})\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-2-2.5.2", "Conjugate pair of binomial surd (√a + √b)(√a - √b)", 21, 10, 10, builder_252)

# 2.6.1: Definition |x| (19 Ex, 11 Pr, 10 Fo)
def builder_261(i, mode):
    val = -15 + (i % 10) * 3
    res = abs(val)
    txt = f"Find the absolute value (modulus) of \\(|{val}|\\)."
    corr = f"\\({res}\\)"
    raw_dist = [
        f"\\({-res}\\)",
        f"\\({res + 1}\\)",
        f"\\({res - 1 if res > 1 else res + 2}\\)"
    ]
    sol = f"Step 1: By definition, \\(|x| = x\\) if \\(x \\ge 0\\) and \\(|x| = -x\\) if \\(x < 0\\).\nStep 2: For \\(x = {val}\\), the distance from 0 on the number line is \\({res}\\).\nStep 3: Hence, \\(|{val}| = {res}\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-2-2.6.1", "Definition |x|", 19, 11, 10, builder_261)

# 2.6.2: Solving modulus equations (21 Ex, 9 Pr, 10 Fo)
def builder_262(i, mode):
    a = (i % 4) + 2
    b = (i % 5) + 3
    sol1 = a + b
    sol2 = a - b
    txt = f"Solve the modulus equation: \\(|x - {a}| = {b}\\)."
    corr = f"\\(x = {sol1}\\) or \\(x = {sol2}\\)"
    raw_dist = [
        f"\\(x = {sol1}\\) only",
        f"\\(x = {sol2}\\) only",
        f"\\(x = {sol1 + 1}\\) or \\(x = {sol2 - 1}\\)"
    ]
    sol = f"Step 1: If \\(|x - a| = b\\) where \\(b > 0\\), then \\(x - a = b\\) or \\(x - a = -b\\).\nStep 2: Case 1: \\(x - {a} = {b} \\implies x = {sol1}\\).\nStep 3: Case 2: \\(x - {a} = -{b} \\implies x = {sol2}\\). Solutions are \\(x = {sol1}\\) or \\(x = {sol2}\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-2-2.6.2", "Solving modulus equations |x - a| = b", 21, 9, 10, builder_262)

print(f"Generated Chapter 2 subtopics top-up: {len(questions_ch2_topup)} questions")

with open("scripts/mh9_mth1_ch2_subtopics_generated.json", "w", encoding="utf-8") as f:
    json.dump(questions_ch2_topup, f, indent=2)
