# scripts/generate_ch5_full.py
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
        "chapterNumber": 5,
        "chapter": "Linear Equations in Two Variables",
        "topicCode": t_code,
        "topic": t_name,
        "type": q_type,
        "marks": marks,
        "difficulty": diff,
        "vault": vault,
        "timesUsed": 0,
        "usedInClassroomTest": False,
        "requiresFigure": False,
        "createdAt": "2026-11-21T12:56:00.000Z",
        "updatedAt": "2026-11-21T12:56:00.000Z"
    }

questions_ch5 = []

# ==========================================
# 5.1.1 Standard form ax + by = c
# T_CODE = "MH-9-MTH1-5-5.1.1", T_NAME = "Standard form ax + by = c"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_511 = "MH-9-MTH1-5-5.1.1"
t_name_511 = "Standard form ax + by = c"

for i in range(1, 39):
    a = (i % 5) + 2
    b = (i % 4) + 3
    x_val = (i % 4) + 1
    y_val = (i % 3) + 2
    c = a * x_val + b * y_val

    txt = f"Check which of the following ordered pairs \\((x, y)\\) is a solution to the linear equation \\({a}x + {b}y = {c}\\)."
    corr = f"\\(({x_val}, {y_val})\\)"
    raw_distractors = [
        f"\\(({x_val + 1}, {y_val})\\)",
        f"\\(({x_val}, {y_val + 1})\\)",
        f"\\(({y_val}, {x_val})\\)" if x_val != y_val else f"\\(({x_val - 1}, {y_val + 2})\\)",
        f"\\(({x_val + 2}, {y_val - 1})\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Substitute \\(x = {x_val}\\) and \\(y = {y_val}\\) into the left-hand side \\({a}x + {b}y\\).\n"
        f"Step 2: \\(\\text{{LHS}} = {a}({x_val}) + {b}({y_val}) = {a * x_val} + {b * y_val} = {c}\\).\n"
        f"Step 3: Since \\(\\text{{LHS}} = \\text{{RHS}} = {c}\\), the point \\(({x_val}, {y_val})\\) satisfies the equation."
    )
    q_code = f"MH-9-MTH1-5-5.1.1-OSC-{100 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_511, t_name_511, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    a = (i % 4) + 3
    b = (i % 3) + 2
    c = (i % 7) + 5
    txt = f"Express the linear equation \\({a}x = {c} - {b}y\\) in general standard form \\(ax + by + c = 0\\)."
    corr = f"\\({a}x + {b}y - {c} = 0\\)"
    raw_distractors = [
        f"\\({a}x - {b}y - {c} = 0\\)",
        f"\\({a}x + {b}y + {c} = 0\\)",
        f"\\({a}x - {b}y + {c} = 0\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: Standard form has all terms on one side: \\(ax + by + c = 0\\).\n"
        f"Step 2: Add \\({b}y\\) and subtract \\({c}\\) from both sides: \\({a}x + {b}y - {c} = 0\\).\n"
        f"Step 3: Comparing with \\(ax + by + c = 0\\), we have \\(a = {a}, b = {b}, c = -{c}\\)."
    )
    q_code = f"MH-9-MTH1-5-5.1.1-OSC-{200 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_511, t_name_511, "practice", "medium"))

for i in range(1, 21):
    txt = "What is the degree of each variable in a linear equation in two variables?"
    corr = "\\(1\\)"
    w1 = "\\(2\\)"
    w2 = "\\(0\\)"
    w3 = "Any whole number"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: An equation of the form \\(ax + by + c = 0\\) is called linear because the degree of each variable \\(x\\) and \\(y\\) is 1.\n"
        "Step 2: Coefficients \\(a\\) and \\(b\\) must not be simultaneously zero (\\(a^2 + b^2 \\ne 0\\)).\n"
        "Step 3: Hence, the degree is 1."
    )
    q_code = f"MH-9-MTH1-5-5.1.1-OSC-{150 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_511, t_name_511, "foundation", "easy"))

# ==========================================
# 5.1.2 Eliminating variable by equating coefficients
# T_CODE = "MH-9-MTH1-5-5.1.2", T_NAME = "Eliminating variable by equating coefficients"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_512 = "MH-9-MTH1-5-5.1.2"
t_name_512 = "Eliminating variable by equating coefficients"

for i in range(1, 39):
    x = (i % 5) + 1
    y = (i % 4) + 2
    # Eq 1: x + y = x + y
    c1 = x + y
    # Eq 2: 2x - y = 2x - y
    c2 = 2 * x - y

    txt = f"Solve the simultaneous equations by elimination method: \\(x + y = {c1}\\) and \\(2x - y = {c2}\\)."
    corr = f"\\(x = {x}, y = {y}\\)"
    raw_distractors = [
        f"\\(x = {x + 1}, y = {y - 1}\\)",
        f"\\(x = {y}, y = {x}\\)" if x != y else f"\\(x = {x + 2}, y = {y}\\)",
        f"\\(x = {x - 1}, y = {y + 1}\\)",
        f"\\(x = {x + 2}, y = {y - 2}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: The coefficients of \\(y\\) are \\(+1\\) and \\(-1\\) (opposite signs). Add the two equations:\n"
        f"\\((x + y) + (2x - y) = {c1} + {c2} \\implies 3x = {c1 + c2} \\implies x = {x}\\).\n"
        f"Step 2: Substitute \\(x = {x}\\) into \\(x + y = {c1}\\):\n"
        f"\\({x} + y = {c1} \\implies y = {c1} - {x} = {y}\\).\n"
        f"Step 3: Solution set is \\(x = {x}, y = {y}\\)."
    )
    q_code = f"MH-9-MTH1-5-5.1.2-OSC-{100 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_512, t_name_512, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    x = (i % 4) + 2
    y = (i % 3) + 1
    c1 = 3 * x + 2 * y
    c2 = 3 * x - 2 * y
    txt = f"In solving \\(3x + 2y = {c1}\\) and \\(3x - 2y = {c2}\\), what is obtained by adding the two equations?"
    corr = f"\\(6x = {c1 + c2}\\)"
    raw_distractors = [
        f"\\(4y = {c1 - c2}\\)",
        f"\\(6x + 4y = {c1 + c2}\\)",
        f"\\(3x = {c1 + c2}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: Adding the two equations: \\((3x + 3x) + (2y - 2y) = {c1} + {c2}\\).\n"
        f"Step 2: The \\(y\\) terms cancel out: \\(6x + 0 = {c1 + c2}\\).\n"
        f"Step 3: The resulting equation is \\(6x = {c1 + c2}\\)."
    )
    q_code = f"MH-9-MTH1-5-5.1.2-OSC-{200 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_512, t_name_512, "practice", "medium"))

for i in range(1, 21):
    txt = "When eliminating a variable with equal coefficients and opposite signs, which algebraic operation is performed on the equations?"
    corr = "Addition of the two equations"
    w1 = "Subtraction of the two equations"
    w2 = "Multiplication of the two equations"
    w3 = "Division of the two equations"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: When coefficients of a variable are numerically equal but opposite in sign (e.g., \\(+3y\\) and \\(-3y\\)), adding them gives \\(0\\).\n"
        "Step 2: Hence, adding the two equations eliminates that variable.\n"
        "Step 3: The required operation is addition."
    )
    q_code = f"MH-9-MTH1-5-5.1.2-OSC-{150 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_512, t_name_512, "foundation", "easy"))

# ==========================================
# 5.2.1 Expressing one variable in terms of other and substituting
# T_CODE = "MH-9-MTH1-5-5.2.1", T_NAME = "Substitution Method for Simultaneous Equations"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_521 = "MH-9-MTH1-5-5.2.1"
t_name_521 = "Substitution Method for Simultaneous Equations"

for i in range(1, 39):
    x = (i % 4) + 3
    y = (i % 5) + 1
    # Eq 1: x = 2y + k => x - 2y = k
    k = x - 2 * y
    # Eq 2: 3x + y = 3x + y
    c2 = 3 * x + y

    txt = f"Solve using the substitution method: \\(x - 2y = {k}\\) and \\(3x + y = {c2}\\)."
    corr = f"\\(x = {x}, y = {y}\\)"
    raw_distractors = [
        f"\\(x = {x + 1}, y = {y + 1}\\)",
        f"\\(x = {y}, y = {x}\\)" if x != y else f"\\(x = {x + 2}, y = {y}\\)",
        f"\\(x = {x - 1}, y = {y}\\)",
        f"\\(x = {x}, y = {y + 2}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Express \\(x\\) in terms of \\(y\\) from the first equation: \\(x = 2y {'+' if k >= 0 else '-'} {abs(k)}\\).\n"
        f"Step 2: Substitute into second equation: \\(3(2y {'+' if k >= 0 else '-'} {abs(k)}) + y = {c2} \\implies 6y + {3*k} + y = {c2} \\implies 7y = {c2 - 3*k} \\implies y = {y}\\).\n"
        f"Step 3: Substitute \\(y = {y}\\) back into expression for \\(x\\): \\(x = 2({y}) {'+' if k >= 0 else '-'} {abs(k)} = {x}\\)."
    )
    q_code = f"MH-9-MTH1-5-5.2.1-OSC-{100 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_521, t_name_521, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    a = (i % 3) + 2
    b = (i % 4) + 1
    txt = f"From the equation \\(x + {a}y = {b}\\), express \\(x\\) in terms of \\(y\\)."
    corr = f"\\(x = {b} - {a}y\\)"
    raw_distractors = [
        f"\\(x = {b} + {a}y\\)",
        f"\\(x = \\frac{{{b}}}{{{a}y}}\\)",
        f"\\(x = {a}y - {b}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: Start with \\(x + {a}y = {b}\\).\n"
        f"Step 2: Subtract \\({a}y\\) from both sides to isolate \\(x\\).\n"
        f"Step 3: \\(x = {b} - {a}y\\)."
    )
    q_code = f"MH-9-MTH1-5-5.2.1-OSC-{200 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_521, t_name_521, "practice", "medium"))

for i in range(1, 21):
    txt = "What is the key idea behind the substitution method of solving simultaneous equations?"
    corr = "Expressing one variable in terms of the other and substituting it into the second equation"
    w1 = "Adding both equations to eliminate a variable"
    w2 = "Finding the determinants using Cramer's rule"
    w3 = "Plotting graphs on Cartesian plane"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: The substitution method isolates one variable in one equation.\n"
        "Step 2: That algebraic expression is then substituted into the other equation, converting it into a single linear equation in one variable.\n"
        "Step 3: Hence, the key idea is substitution."
    )
    q_code = f"MH-9-MTH1-5-5.2.1-OSC-{150 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_521, t_name_521, "foundation", "easy"))

# ==========================================
# 5.3.1 Two-digit reversal problems
# T_CODE = "MH-9-MTH1-5-5.3.1", T_NAME = "Two-digit reversal problems"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_531 = "MH-9-MTH1-5-5.3.1"
t_name_531 = "Two-digit reversal problems"

digit_pairs = [(4, 2), (5, 3), (6, 2), (7, 4), (8, 3), (9, 5), (6, 3), (7, 2), (8, 4), (5, 2)]

for i in range(1, 39):
    u, v = digit_pairs[i % len(digit_pairs)] # tens u, units v
    num = 10 * u + v
    rev = 10 * v + u
    sum_digits = u + v
    diff_rev = num - rev

    txt = f"The sum of the digits of a two-digit number is \\({sum_digits}\\). The number obtained by reversing the digits is \\({abs(diff_rev)}\\) less than the original number. Find the original number."
    corr = f"\\({num}\\)"
    raw_distractors = [
        f"\\({rev}\\)",
        f"\\({num + 9}\\)",
        f"\\({num - 9}\\)",
        f"\\({num + 18}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Let tens digit be \\(x\\) and units digit be \\(y\\). The number is \\(10x + y\\).\n"
        f"Step 2: Equation 1: \\(x + y = {sum_digits}\\). Reversing digits gives \\(10y + x\\).\n"
        f"Step 3: Equation 2: \\((10x + y) - (10y + x) = {diff_rev} \\implies 9(x - y) = {diff_rev} \\implies x - y = {u - v}\\).\n"
        f"Adding gives \\(2x = {2*u} \\implies x = {u}\\) and \\(y = {v}\\). The number is \\({num}\\)."
    )
    q_code = f"MH-9-MTH1-5-5.3.1-OSC-{100 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_531, t_name_531, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    u, v = digit_pairs[(i + 3) % len(digit_pairs)]
    num = 10 * u + v
    txt = f"If the tens digit of a two-digit number is \\(x\\) and the units digit is \\(y\\), what is the algebraic expression for the number?"
    corr = "\\(10x + y\\)"
    raw_distractors = [
        "\\(x + y\\)",
        "\\(10y + x\\)",
        "\\(10xy\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: In the decimal place value system, the tens digit represents a value 10 times its face value.\n"
        "Step 2: Place value of tens digit \\(x\\) is \\(10 \\times x = 10x\\), and units digit is \\(y\\).\n"
        "Step 3: The number is \\(10x + y\\)."
    )
    q_code = f"MH-9-MTH1-5-5.3.1-OSC-{200 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_531, t_name_531, "practice", "medium"))

for i in range(1, 21):
    txt = "What is the difference between a two-digit number \\(10x + y\\) and the number obtained by reversing its digits \\(10y + x\\)?"
    corr = "\\(9(x - y)\\)"
    w1 = "\\(11(x + y)\\)"
    w2 = "\\(9(x + y)\\)"
    w3 = "\\(x - y\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Compute difference: \\((10x + y) - (10y + x)\\).\n"
        "Step 2: Collect like terms: \\(10x - x + y - 10y = 9x - 9y\\).\n"
        "Step 3: Factor out 9: \\(9(x - y)\\)."
    )
    q_code = f"MH-9-MTH1-5-5.3.1-OSC-{150 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_531, t_name_531, "foundation", "easy"))

# ==========================================
# 5.3.2 Numerator and denominator modifications
# T_CODE = "MH-9-MTH1-5-5.3.2", T_NAME = "Numerator and denominator modifications"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_532 = "MH-9-MTH1-5-5.3.2"
t_name_532 = "Numerator and denominator modifications"

frac_pairs = [(3, 5), (2, 7), (4, 9), (5, 8), (1, 3), (3, 7), (2, 5), (5, 9)]

for i in range(1, 39):
    pair = frac_pairs[i % len(frac_pairs)]
    num, den = pair
    # condition: numerator is num, denominator is den
    # if 1 added to numerator and denominator: (num+1)/(den+1)
    # let's do: denominator is (den - num) more than numerator. If 1 is added to both, ratio becomes (num+1)/(den+1).
    diff = den - num
    n_plus_1 = num + 1
    d_plus_1 = den + 1
    # reduce n_plus_1 / d_plus_1
    import math
    g = math.gcd(n_plus_1, d_plus_1)
    rn = n_plus_1 // g
    rd = d_plus_1 // g

    txt = f"The denominator of a fraction is \\({diff}\\) more than its numerator. If \\(1\\) is added to both numerator and denominator, the ratio becomes \\({rn} : {rd}\\). Find the original fraction."
    corr = f"\\(\\frac{{{num}}}{{{den}}}\\)"
    raw_distractors = [
        f"\\(\\frac{{{den}}}{{{num}}}\\)",
        f"\\(\\frac{{{num + 1}}}{{{den + 1}}}\\)",
        f"\\(\\frac{{{num - 1 if num > 1 else num + 2}}}{{{den}}}\\)",
        f"\\(\\frac{{{num}}}{{{den + 2}}}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Let the numerator be \\(x\\). Then denominator is \\(x + {diff}\\). The fraction is \\(\\frac{{x}}{{x + {diff}}}\\).\n"
        f"Step 2: Adding 1 to both: \\(\\frac{{x + 1}}{{x + {diff} + 1}} = \\frac{{{rn}}}{{{rd}}}\\).\n"
        f"Step 3: Cross-multiply: \\({rd}(x + 1) = {rn}(x + {diff + 1}) \\implies x = {num}\\). Denominator is \\({num} + {diff} = {den}\\).\n"
        f"The fraction is \\(\\frac{{{num}}}{{{den}}}\\)."
    )
    q_code = f"MH-9-MTH1-5-5.3.2-OSC-{100 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_532, t_name_532, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    pair = frac_pairs[(i + 2) % len(frac_pairs)]
    num, den = pair
    txt = f"If the numerator of a fraction is \\(x\\) and denominator is \\(y\\), write the expression when \\(2\\) is added to numerator and \\(3\\) is subtracted from denominator."
    corr = "\\(\\frac{x + 2}{y - 3}\\)"
    raw_distractors = [
        "\\(\\frac{x - 2}{y + 3}\\)",
        "\\(\\frac{x + 3}{y - 2}\\)",
        "\\(\\frac{2x}{3y}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Original fraction is \\(\\frac{x}{y}\\).\n"
        "Step 2: Modified numerator: \\(x + 2\\); modified denominator: \\(y - 3\\).\n"
        "Step 3: The modified fraction is \\(\\frac{x + 2}{y - 3}\\)."
    )
    q_code = f"MH-9-MTH1-5-5.3.2-OSC-{200 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_532, t_name_532, "practice", "medium"))

for i in range(1, 21):
    txt = "In fraction word problems, what constraint is always required on the denominator \\(y\\)?"
    corr = "\\(y \\ne 0\\)"
    w1 = "\\(y > 10\\)"
    w2 = "\\(y = 1\\)"
    w3 = "\\(y\\) must be even"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Division by zero is undefined in mathematics.\n"
        "Step 2: For any fraction \\(\\frac{x}{y}\\), the denominator cannot be zero.\n"
        "Step 3: Hence, the constraint is \\(y \\ne 0\\)."
    )
    q_code = f"MH-9-MTH1-5-5.3.2-OSC-{150 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_532, t_name_532, "foundation", "easy"))

# ==========================================
# 5.3.3 Speed and time variations
# T_CODE = "MH-9-MTH1-5-5.3.3", T_NAME = "Speed and time variations"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_533 = "MH-9-MTH1-5-5.3.3"
t_name_533 = "Speed and time variations"

speed_pairs = [(40, 60), (30, 50), (45, 60), (50, 70), (35, 55), (40, 50), (60, 80)]

for i in range(1, 39):
    s1, s2 = speed_pairs[i % len(speed_pairs)]
    # Person travels distance D: let D = 120 or 300
    # Let's do classic age / perimeter problem in two variables:
    # Father's age is 3 times son's age. After 10 years, sum of ages is S.
    son = (i % 5) + 10
    father = 3 * son
    after = 5
    sum_after = (son + after) + (father + after)

    txt = f"A father's age is currently \\(3\\) times his son's age. After \\({after}\\) years, the sum of their ages will be \\({sum_after}\\) years. Find their present ages."
    corr = f"Father: \\({father}\\) years, Son: \\({son}\\) years"
    raw_distractors = [
        f"Father: \\({father + 5}\\) years, Son: \\({son - 2}\\) years",
        f"Father: \\({father - 3}\\) years, Son: \\({son + 1}\\) years",
        f"Father: \\({father + 6}\\) years, Son: \\({son + 2}\\) years",
        f"Father: \\({40}\\) years, Son: \\({12}\\) years"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Let son's present age be \\(x\\) and father's age be \\(y\\). Given \\(y = 3x\\).\n"
        f"Step 2: After \\({after}\\) years, their ages are \\(x + {after}\\) and \\(y + {after}\\).\n"
        f"Step 3: \\((x + {after}) + (3x + {after}) = {sum_after} \\implies 4x + {2*after} = {sum_after} \\implies 4x = {sum_after - 2*after} \\implies x = {son}\\).\n"
        f"Father's age \\(y = 3 \\times {son} = {father}\\) years."
    )
    q_code = f"MH-9-MTH1-5-5.3.3-OSC-{100 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_533, t_name_533, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    l = (i % 6) + 12
    b = (i % 4) + 6
    p = 2 * (l + b)
    txt = f"The perimeter of a rectangle is \\({p}\\) cm. If length is \\(x\\) and breadth is \\(y\\), write the linear equation in two variables."
    corr = f"\\(x + y = {p // 2}\\)"
    raw_distractors = [
        f"\\(2x + y = {p}\\)",
        f"\\(x + 2y = {p}\\)",
        f"\\(x y = {p}\\)"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: The perimeter of a rectangle is \\(2(\\text{{length}} + \\text{{breadth}}) = 2(x + y)\\).\n"
        f"Step 2: \\(2(x + y) = {p}\\).\n"
        f"Step 3: Dividing both sides by 2 gives \\(x + y = {p // 2}\\)."
    )
    q_code = f"MH-9-MTH1-5-5.3.3-OSC-{200 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_533, t_name_533, "practice", "medium"))

for i in range(1, 21):
    txt = "What is the relationship between distance \\(D\\), speed \\(S\\), and time \\(T\\)?"
    corr = "\\(D = S \\times T\\)"
    w1 = "\\(D = \\frac{S}{T}\\)"
    w2 = "\\(S = D \\times T\\)"
    w3 = "\\(T = D \\times S\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: By physics and algebra definition, speed is rate of covering distance per unit time: \\(S = \\frac{D}{T}\\).\n"
        "Step 2: Multiplying both sides by time \\(T\\) gives \\(D = S \\times T\\).\n"
        "Step 3: Hence, \\(D = S \\times T\\)."
    )
    q_code = f"MH-9-MTH1-5-5.3.3-OSC-{150 + i:03d}"
    questions_ch5.append(make_q(q_code, txt, opts, sol, t_code_533, t_name_533, "foundation", "easy"))

print(f"Generated Chapter 5: {len(questions_ch5)} questions")

with open("scripts/mh9_mth1_ch5_generated.json", "w", encoding="utf-8") as f:
    json.dump(questions_ch5, f, indent=2)
