# scripts/generate_ch3_rest.py
import json

def make_opt(text, is_correct):
    return {"text": text, "isCorrect": is_correct}

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
        "chapterNumber": 3,
        "chapter": "Polynomials",
        "topicCode": t_code,
        "topic": t_name,
        "type": q_type,
        "marks": marks,
        "difficulty": diff,
        "vault": vault,
        "timesUsed": 0,
        "usedInClassroomTest": False,
        "requiresFigure": False,
        "createdAt": "2026-11-21T12:50:00.000Z",
        "updatedAt": "2026-11-21T12:50:00.000Z"
    }

questions_rest = []

# ==========================================
# 3.3.1 Synthetic Division Algorithm
# T_CODE = "MH-9-MTH1-3-3.3.1", T_NAME = "Synthetic division algorithm using opposite coefficients"
# Needs 31 Exam (Seq 101-131), 20 Foundation (Seq 151-170)
# ==========================================
t_code_331 = "MH-9-MTH1-3-3.3.1"
t_name_331 = "Synthetic division algorithm using opposite coefficients"

# Generating 31 Exam Qs for 3.3.1
# In synthetic division of P(x) by (x - a), opposite of divisor constant is a.
for i in range(1, 32):
    # Variety of divisors and dividends
    a = (i % 5) + 1  # 1, 2, 3, 4, 5
    sign = -1 if i % 2 == 0 else 1
    root = a * sign # divisor is (x - root)
    div_str = f"(x {'-' if root > 0 else '+'} {abs(root)})"
    # P(x) = (x - root)(q2 x^2 + q1 x + q0) + r
    q2 = (i % 3) + 1
    q1 = ((i * 2) % 7) - 3
    q0 = ((i * 3) % 9) - 4
    r = (i * 5) % 11 - 5
    # P(x) = q2 x^3 + (q1 - root*q2) x^2 + (q0 - root*q1) x + (r - root*q0)
    c3 = q2
    c2 = q1 - root * q2
    c1 = q0 - root * q1
    c0 = - root * q0 + r

    # Let's formulate question
    txt = f"Divide the polynomial \\({c3}x^3 {'+' if c2 >= 0 else '-'} {abs(c2)}x^2 {'+' if c1 >= 0 else '-'} {abs(c1)}x {'+' if c0 >= 0 else '-'} {abs(c0)}\\) by \\({div_str}\\) using synthetic division. Find the quotient and remainder."
    
    q_str = f"Quotient: \\({q2}x^2 {'+' if q1 >= 0 else '-'} {abs(q1)}x {'+' if q0 >= 0 else '-'} {abs(q0)}\\), Remainder: \\({r}\\)"
    w1_str = f"Quotient: \\({q2}x^2 {'+' if q1 >= 0 else '-'} {abs(q1)}x {'+' if q0 >= 0 else '-'} {abs(q0)}\\), Remainder: \\({r + 2}\\)"
    w2_str = f"Quotient: \\({q2}x^2 {'+' if (q1+1) >= 0 else '-'} {abs(q1+1)}x {'+' if q0 >= 0 else '-'} {abs(q0)}\\), Remainder: \\({r}\\)"
    w3_str = f"Quotient: \\({q2+1}x^2 {'+' if q1 >= 0 else '-'} {abs(q1)}x {'+' if q0 >= 0 else '-'} {abs(q0)}\\), Remainder: \\({r - 1}\\)"

    opts = [
        make_opt(q_str, True),
        make_opt(w1_str, False),
        make_opt(w2_str, False),
        make_opt(w3_str, False)
    ]
    # shuffle deterministically
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Write the dividend in coefficient form: \\(({c3}, {c2}, {c1}, {c0})\\).\n"
        f"Step 2: The divisor is \\({div_str}\\), so the opposite of the constant term is \\({root}\\).\n"
        f"Step 3: Perform synthetic division:\n"
        f"Bring down leading coefficient {c3}. Multiply by {root} and add consecutively:\n"
        f"Quotient coefficients are \\(({q2}, {q1}, {q0})\\), which corresponds to polynomial \\({q2}x^2 {'+' if q1 >= 0 else '-'} {abs(q1)}x {'+' if q0 >= 0 else '-'} {abs(q0)}\\).\n"
        f"The remainder is the last number in the bottom row: \\({r}\\)."
    )

    q_code = f"MH-9-MTH1-3-3.3.1-OSC-{100 + i:03d}"
    questions_rest.append(make_q(q_code, txt, opts, sol, t_code_331, t_name_331, "exam", "medium" if i % 2 == 0 else "hard"))

# Generating 20 Foundation Qs for 3.3.1
for i in range(1, 21):
    root = (i % 4) + 1
    div_str = f"(x - {root})"
    # Simple linear quotient: (x - root)(x + k) + r
    k = (i % 5) + 1
    # P(x) = x^2 + (k - root)x - root*k + r
    c2 = 1
    c1 = k - root
    c0 = -root * k
    r = 0
    txt = f"What is the number written on the left in the synthetic division algorithm when dividing by \\({div_str}\\)?"
    corr = f"\\({root}\\)"
    w1 = f"\\({-root}\\)"
    w2 = f"\\({root + 1}\\)"
    w3 = f"\\(0\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: In synthetic division, if the divisor is \\((x - a)\\), the divisor root written on the left is the opposite of \\(-a\\), which is \\(a\\).\n"
        f"Step 2: Here the divisor is \\({div_str}\\), so \\(a = {root}\\).\n"
        f"Step 3: Hence, \\({root}\\) is written on the left."
    )
    q_code = f"MH-9-MTH1-3-3.3.1-OSC-{150 + i:03d}"
    questions_rest.append(make_q(q_code, txt, opts, sol, t_code_331, t_name_331, "foundation", "easy"))

# ==========================================
# 3.3.2 Linear Division Method
# T_CODE = "MH-9-MTH1-3-3.3.2", T_NAME = "Linear division method"
# Needs 31 Exam (Seq 101-131), 20 Foundation (Seq 151-170)
# ==========================================
t_code_332 = "MH-9-MTH1-3-3.3.2"
t_name_332 = "Linear division method"

for i in range(1, 32):
    m = (i % 3) + 1
    a = (i % 4) + 1
    q1 = (i % 3) + 1
    q0 = ((i * 3) % 7) - 2
    r = (i * 2) % 9 - 3
    # P(x) = (x + a)(q1 x + q0) + r = q1 x^2 + (q0 + a*q1) x + (a*q0 + r)
    c2 = q1
    c1 = q0 + a * q1
    c0 = a * q0 + r

    txt = f"Using the linear division method, divide \\({c2}x^2 {'+' if c1 >= 0 else '-'} {abs(c1)}x {'+' if c0 >= 0 else '-'} {abs(c0)}\\) by \\((x + {a})\\). What is the quotient and remainder?"
    corr = f"Quotient: \\({q1}x {'+' if q0 >= 0 else '-'} {abs(q0)}\\), Remainder: \\({r}\\)"
    w1 = f"Quotient: \\({q1}x {'+' if q0 >= 0 else '-'} {abs(q0)}\\), Remainder: \\({r + 3}\\)"
    w2 = f"Quotient: \\({q1+1}x {'+' if q0 >= 0 else '-'} {abs(q0)}\\), Remainder: \\({r}\\)"
    w3 = f"Quotient: \\({q1}x {'+' if (q0-1) >= 0 else '-'} {abs(q0-1)}\\), Remainder: \\({r - 1}\\)"

    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: In the linear method, express each higher power term using the divisor \\((x + {a})\\):\n"
        f"\\({c2}x^2 = {c2}x(x + {a}) - {c2 * a}x\\).\n"
        f"Step 2: Combine remaining linear terms: \\(({c1} - {c2 * a})x = {q0}x = {q0}(x + {a}) - {q0 * a}\\).\n"
        f"Step 3: Combine constants: \\({c0} - {q0 * a} = {r}\\).\n"
        f"Therefore, \\(P(x) = (x + {a})({q1}x {'+' if q0 >= 0 else '-'} {abs(q0)}) + ({r})\\).\n"
        f"Quotient is \\({q1}x {'+' if q0 >= 0 else '-'} {abs(q0)}\\) and Remainder is \\({r}\\)."
    )
    q_code = f"MH-9-MTH1-3-3.3.2-OSC-{100 + i:03d}"
    questions_rest.append(make_q(q_code, txt, opts, sol, t_code_332, t_name_332, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    div_a = (i % 4) + 2
    txt = f"In the linear method of division, what is the first step when dividing a polynomial \\(P(x)\\) by \\((x - {div_a})\\)?"
    corr = f"Express the leading term of \\(P(x)\\) in terms of \\((x - {div_a})\\)"
    w1 = f"Multiply the entire polynomial by \\((x - {div_a})\\)"
    w2 = f"Differentiate the polynomial"
    w3 = f"Equate the polynomial to zero"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: The linear method works by expressing each power of the variable sequentially in terms of the linear divisor \\((x - a)\\).\n"
        f"Step 2: For divisor \\((x - {div_a})\\), we write the leading term \\(a_n x^n = a_n x^{{n-1}}(x - {div_a}) + {div_a} a_n x^{{n-1}}\\).\n"
        f"Step 3: Hence, the first step is expressing the leading term in terms of \\((x - {div_a})\\)."
    )
    q_code = f"MH-9-MTH1-3-3.3.2-OSC-{150 + i:03d}"
    questions_rest.append(make_q(q_code, txt, opts, sol, t_code_332, t_name_332, "foundation", "easy"))

# ==========================================
# 3.4.1 Evaluating p(x) for x = a
# T_CODE = "MH-9-MTH1-3-3.4.1", T_NAME = "Evaluating p(x) for x = a"
# Needs 33 Exam (Seq 101-133), 20 Foundation (Seq 151-170)
# ==========================================
t_code_341 = "MH-9-MTH1-3-3.4.1"
t_name_341 = "Evaluating p(x) for x = a"

for i in range(1, 34):
    val_x = ((i * 2) % 7) - 3  # -3, -2, -1, 0, 1, 2, 3
    if val_x == 0:
        val_x = 2
    a = (i % 3) + 1
    b = ((i * 3) % 5) - 2
    c = ((i * 5) % 11) - 4
    # p(x) = a x^2 + b x + c
    res = a * (val_x ** 2) + b * val_x + c

    txt = f"If \\(p(x) = {a}x^2 {'+' if b >= 0 else '-'} {abs(b)}x {'+' if c >= 0 else '-'} {abs(c)}\\), find the value of \\(p({val_x})\\)."
    corr = f"\\({res}\\)"
    # Ensure options are strictly distinct
    w_vals = [res + 2, res - 3, -res if -res != res and -res != res + 2 and -res != res - 3 else res + 5]
    if len(set([res] + w_vals)) < 4:
        w_vals = [res + 1, res + 2, res + 3]
    w1, w2, w3 = f"\\({w_vals[0]}\\)", f"\\({w_vals[1]}\\)", f"\\({w_vals[2]}\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Substitute \\(x = {val_x}\\) into \\(p(x)\\):\n"
        f"\\(p({val_x}) = {a}({val_x})^2 {'+' if b >= 0 else '-'} {abs(b)}({val_x}) {'+' if c >= 0 else '-'} {abs(c)}\\).\n"
        f"Step 2: Calculate each term: \\({a} \\times {val_x**2} = {a * val_x**2}\\), \\({b} \\times {val_x} = {b * val_x}\\), and constant \\({c}\\).\n"
        f"Step 3: Sum the terms: \\({a * val_x**2} + ({b * val_x}) + ({c}) = {res}\\)."
    )
    q_code = f"MH-9-MTH1-3-3.4.1-OSC-{100 + i:03d}"
    questions_rest.append(make_q(q_code, txt, opts, sol, t_code_341, t_name_341, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    val_x = (i % 4) + 1
    k = (i % 5) + 2
    res = k * val_x + 3
    txt = f"Find the value of the polynomial \\(p(x) = {k}x + 3\\) when \\(x = {val_x}\\)."
    corr = f"\\({res}\\)"
    w1 = f"\\({res + 1}\\)"
    w2 = f"\\({res - 2}\\)"
    w3 = f"\\({k * val_x}\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: Substitute \\(x = {val_x}\\) in \\(p(x)\\).\n"
        f"Step 2: \\(p({val_x}) = {k}({val_x}) + 3 = {k * val_x} + 3 = {res}\\).\n"
        f"Step 3: The value of the polynomial is \\({res}\\)."
    )
    q_code = f"MH-9-MTH1-3-3.4.1-OSC-{150 + i:03d}"
    questions_rest.append(make_q(q_code, txt, opts, sol, t_code_341, t_name_341, "foundation", "easy"))

# ==========================================
# 3.4.2 Remainder theorem statement & verification
# T_CODE = "MH-9-MTH1-3-3.4.2", T_NAME = "Remainder theorem statement & verification"
# Needs 31 Exam (Seq 101-131), 20 Foundation (Seq 151-170)
# ==========================================
t_code_342 = "MH-9-MTH1-3-3.4.2"
t_name_342 = "Remainder theorem statement & verification"

for i in range(1, 32):
    a = (i % 4) + 1
    # Divisor is (x - a)
    # p(x) = x^3 - k x^2 + 2x - 5
    k = (i % 3) + 1
    # Remainder by theorem is p(a) = a^3 - k a^2 + 2a - 5
    rem = (a ** 3) - k * (a ** 2) + 2 * a - 5

    txt = f"Find the remainder when the polynomial \\(p(x) = x^3 - {k}x^2 + 2x - 5\\) is divided by \\((x - {a})\\) using the Remainder Theorem."
    corr = f"\\({rem}\\)"
    w1 = f"\\({rem + 4}\\)"
    w2 = f"\\({rem - 3}\\)"
    w3 = f"\\({-rem}\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: By the Remainder Theorem, if a polynomial \\(p(x)\\) is divided by \\((x - a)\\), the remainder is \\(p(a)\\).\n"
        f"Step 2: Here the divisor is \\((x - {a})\\), so \\(a = {a}\\).\n"
        f"Step 3: Evaluate \\(p({a}) = ({a})^3 - {k}({a})^2 + 2({a}) - 5 = {a**3} - {k * a**2} + {2*a} - 5 = {rem}\\).\n"
        f"Therefore, the remainder is \\({rem}\\)."
    )
    q_code = f"MH-9-MTH1-3-3.4.2-OSC-{100 + i:03d}"
    questions_rest.append(make_q(q_code, txt, opts, sol, t_code_342, t_name_342, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    txt = "According to the Remainder Theorem, when a polynomial \\(P(x)\\) is divided by \\((x - a)\\), what is the remainder?"
    corr = "\\(P(a)\\)"
    w1 = "\\(P(-a)\\)"
    w2 = "\\(0\\)"
    w3 = "\\(P(0)\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: By the division algorithm, \\(P(x) = (x - a) Q(x) + R\\), where \\(R\\) is a constant (degree < 1).\n"
        "Step 2: Substituting \\(x = a\\) gives \\(P(a) = (a - a) Q(a) + R = 0 + R = R\\).\n"
        "Step 3: Therefore, the remainder is \\(P(a)\\)."
    )
    q_code = f"MH-9-MTH1-3-3.4.2-OSC-{150 + i:03d}"
    questions_rest.append(make_q(q_code, txt, opts, sol, t_code_342, t_name_342, "foundation", "easy"))

# ==========================================
# 3.4.3 Factor theorem for checking factorability
# T_CODE = "MH-9-MTH1-3-3.4.3", T_NAME = "Factor theorem for checking factorability"
# Needs 31 Exam (Seq 101-131), 20 Foundation (Seq 151-170)
# ==========================================
t_code_343 = "MH-9-MTH1-3-3.4.3"
t_name_343 = "Factor theorem for checking factorability"

for i in range(1, 32):
    a = (i % 4) + 1
    # Check if (x - a) is a factor of p(x)
    is_fac = (i % 2 == 1)
    # p(x) = (x - a)(x + k) + (0 if is_fac else 4)
    k = (i % 3) + 2
    rem = 0 if is_fac else 4
    # p(x) = x^2 + (k - a)x - a*k + rem
    b = k - a
    c = -a * k + rem

    txt = f"Using the Factor Theorem, determine whether \\((x - {a})\\) is a factor of \\(p(x) = x^2 {'+' if b >= 0 else '-'} {abs(b)}x {'+' if c >= 0 else '-'} {abs(c)}\\)."
    if is_fac:
        corr = f"Yes, because \\(p({a}) = 0\\)"
        w1 = f"No, because \\(p({a}) \\ne 0\\)"
        w2 = f"Yes, because \\(p(-{a}) = 0\\)"
        w3 = f"Cannot be determined without division"
    else:
        corr = f"No, because \\(p({a}) = {rem} \\ne 0\\)"
        w1 = f"Yes, because \\(p({a}) = 0\\)"
        w2 = f"No, because degree is 2"
        w3 = f"Yes, by inspection"

    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: The Factor Theorem states that \\((x - a)\\) is a factor of \\(p(x)\\) if and only if \\(p(a) = 0\\).\n"
        f"Step 2: Here \\(a = {a}\\). Evaluate \\(p({a}) = ({a})^2 {'+' if b >= 0 else '-'} {abs(b)}({a}) {'+' if c >= 0 else '-'} {abs(c)} = {rem}\\).\n"
        f"Step 3: Since \\(p({a}) = {rem}\\)" + (" is equal to 0, \\((x - " + str(a) + ")\\) is indeed a factor." if is_fac else " is not equal to 0, \\((x - " + str(a) + ")\\) is not a factor.")
    )
    q_code = f"MH-9-MTH1-3-3.4.3-OSC-{100 + i:03d}"
    questions_rest.append(make_q(q_code, txt, opts, sol, t_code_343, t_name_343, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    txt = "Under what condition is \\((x - a)\\) a factor of a polynomial \\(P(x)\\)?"
    corr = "\\(P(a) = 0\\)"
    w1 = "\\(P(a) > 0\\)"
    w2 = "\\(P(-a) = 0\\)"
    w3 = "\\(P(0) = a\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: By the Remainder Theorem, dividing \\(P(x)\\) by \\((x - a)\\) gives remainder \\(R = P(a)\\).\n"
        "Step 2: A polynomial divides another exactly (is a factor) if and only if the remainder is zero.\n"
        "Step 3: Therefore, \\((x - a)\\) is a factor if and only if \\(P(a) = 0\\)."
    )
    q_code = f"MH-9-MTH1-3-3.4.3-OSC-{150 + i:03d}"
    questions_rest.append(make_q(q_code, txt, opts, sol, t_code_343, t_name_343, "foundation", "easy"))

# ==========================================
# 3.5.1 Factoring quadratic expressions
# T_CODE = "MH-9-MTH1-3-3.5.1", T_NAME = "Factoring quadratic expressions (x² - x)² - 8(x² - x) + 12"
# Needs 32 Exam (Seq 101-132), 20 Foundation (Seq 151-170)
# ==========================================
t_code_351 = "MH-9-MTH1-3-3.5.1"
t_name_351 = "Factoring quadratic expressions (x² - x)² - 8(x² - x) + 12"

for i in range(1, 33):
    p = (i % 4) + 1
    q = (i % 3) + 2
    # Expression: (x^2 - 2x)^2 - (p + q)(x^2 - 2x) + p*q
    s = p + q
    prod = p * q
    txt = f"Factorise the polynomial completely: \\((x^2 - 2x)^2 - {s}(x^2 - 2x) + {prod}\\)."
    corr = f"\\((x^2 - 2x - {p})(x^2 - 2x - {q})\\)"
    w1 = f"\\((x^2 - 2x + {p})(x^2 - 2x + {q})\\)"
    w2 = f"\\((x^2 - 2x - {p+1})(x^2 - 2x - {q})\\)"
    w3 = f"\\((x^2 - 2x - {prod})(x^2 - 2x - 1)\\)"

    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Let \\(y = x^2 - 2x\\). The expression becomes \\(y^2 - {s}y + {prod}\\).\n"
        f"Step 2: Factorise the quadratic in \\(y\\) by splitting the middle term:\n"
        f"\\(y^2 - {p}y - {q}y + {prod} = y(y - {p}) - {q}(y - {p}) = (y - {p})(y - {q})\\).\n"
        f"Step 3: Substitute back \\(y = x^2 - 2x\\):\n"
        f"The factorised form is \\((x^2 - 2x - {p})(x^2 - 2x - {q})\\)."
    )
    q_code = f"MH-9-MTH1-3-3.5.1-OSC-{100 + i:03d}"
    questions_rest.append(make_q(q_code, txt, opts, sol, t_code_351, t_name_351, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    a = (i % 4) + 1
    b = (i % 5) + 2
    s = a + b
    p = a * b
    txt = f"Factorise the quadratic expression \\(x^2 + {s}x + {p}\\)."
    corr = f"\\((x + {a})(x + {b})\\)"
    w1 = f"\\((x - {a})(x - {b})\\)"
    w2 = f"\\((x + {a})(x - {b})\\)"
    w3 = f"\\((x + {p})(x + 1)\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        f"Step 1: Find two numbers whose product is {p} and sum is {s}.\n"
        f"Step 2: The numbers are {a} and {b} because \\({a} \\times {b} = {p}\\) and \\({a} + {b} = {s}\\).\n"
        f"Step 3: Therefore, \\(x^2 + {s}x + {p} = (x + {a})(x + {b})\\)."
    )
    q_code = f"MH-9-MTH1-3-3.5.1-OSC-{150 + i:03d}"
    questions_rest.append(make_q(q_code, txt, opts, sol, t_code_351, t_name_351, "foundation", "easy"))

# ==========================================
# 3.5.2 Factoring cubic polynomials
# T_CODE = "MH-9-MTH1-3-3.5.2", T_NAME = "Factoring cubic polynomials"
# Needs 31 Exam (Seq 101-131), 20 Foundation (Seq 151-170)
# ==========================================
t_code_352 = "MH-9-MTH1-3-3.5.2"
t_name_352 = "Factoring cubic polynomials"

for i in range(1, 32):
    r1 = 1 if i % 2 == 1 else -1
    r2 = 2 if (i // 2) % 2 == 1 else -2
    r3 = 3 if (i // 4) % 2 == 1 else -3
    # P(x) = (x - r1)(x - r2)(x - r3)
    # = (x^2 - (r1+r2)x + r1*r2)(x - r3)
    # = x^3 - (r1+r2+r3)x^2 + (r1*r2 + r2*r3 + r3*r1)x - r1*r2*r3
    s1 = r1 + r2 + r3
    s2 = r1*r2 + r2*r3 + r3*r1
    s3 = r1*r2*r3

    f1 = f"(x {'-' if r1 > 0 else '+'} {abs(r1)})"
    f2 = f"(x {'-' if r2 > 0 else '+'} {abs(r2)})"
    f3 = f"(x {'-' if r3 > 0 else '+'} {abs(r3)})"

    txt = f"Factorise the cubic polynomial \\(x^3 {'-' if s1 >= 0 else '+'} {abs(s1)}x^2 {'+' if s2 >= 0 else '-'} {abs(s2)}x {'-' if s3 >= 0 else '+'} {abs(s3)}\\)."
    corr = f"\\({f1}{f2}{f3}\\)"
    # Build strictly distinct distractors
    cands = [
        f"\\((x + 4)(x - 5)(x + 2)\\)",
        f"\\((x - 4)(x + 5)(x - 2)\\)",
        f"\\({f1}(x^2 + 9)\\)",
        f"\\({f1}(x^2 - 16)\\)",
        f"\\((x + 7)(x - 1)(x + 3)\\)"
    ]
    distinct_distractors = [c for c in cands if c != corr][:3]
    w1, w2, w3 = distinct_distractors[0], distinct_distractors[1], distinct_distractors[2]

    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Test factors of the constant term \\({-s3}\\). Testing \\(x = {r1}\\) gives \\(p({r1}) = 0\\), so \\({f1}\\) is a factor.\n"
        f"Step 2: Divide the cubic polynomial by \\({f1}\\) using synthetic division to find the quadratic quotient.\n"
        f"Step 3: Factorise the quadratic quotient into \\({f2}{f3}\\).\n"
        f"Thus, the complete factorisation is \\({f1}{f2}{f3}\\)."
    )
    q_code = f"MH-9-MTH1-3-3.5.2-OSC-{100 + i:03d}"
    questions_rest.append(make_q(q_code, txt, opts, sol, t_code_352, t_name_352, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    txt = "What is the maximum number of linear factors a cubic polynomial can have?"
    corr = "\\(3\\)"
    w1 = "\\(2\\)"
    w2 = "\\(4\\)"
    w3 = "\\(1\\)"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: By the Fundamental Theorem of Algebra, a polynomial of degree \\(n\\) has at most \\(n\\) roots.\n"
        "Step 2: A cubic polynomial has degree 3.\n"
        "Step 3: Therefore, it can have at most 3 linear factors."
    )
    q_code = f"MH-9-MTH1-3-3.5.2-OSC-{150 + i:03d}"
    questions_rest.append(make_q(q_code, txt, opts, sol, t_code_352, t_name_352, "foundation", "easy"))

print(f"Generated rest of Chapter 3: {len(questions_rest)} questions")

# Save checkpoint
with open("scripts/mh9_mth1_ch3_rest_generated.json", "w", encoding="utf-8") as f:
    json.dump(questions_rest, f, indent=2)
