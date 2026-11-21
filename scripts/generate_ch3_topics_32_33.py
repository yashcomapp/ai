# scripts/generate_ch3_topics_32_33.py
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
        "createdAt": "2026-11-21T12:49:00.000Z",
        "updatedAt": "2026-11-21T12:49:00.000Z"
    }

questions_32_33 = []

# ==========================================
# Topic 3.2: Operations on Polynomials: Addition, Subtraction, Multiplication
# T_CODE = "MH-9-MTH1-3-3.2", T_NAME = "Operations on Polynomials: Addition, Subtraction, Multiplication"
# Need 6 Exam (Seq 101 to 106), 20 Foundation (Seq 151 to 170)
# ==========================================
t_code_32 = "MH-9-MTH1-3-3.2"
t_name_32 = "Operations on Polynomials: Addition, Subtraction, Multiplication"

exam_32 = [
    # 1
    (
        r"Subtract \((2x^3 - 4x^2 + 3x - 5)\) from \((5x^3 - 2x^2 - x + 4)\).",
        [make_opt(r"\(3x^3 + 2x^2 - 4x + 9\)", True), make_opt(r"\(3x^3 - 6x^2 + 2x - 1\)", False), make_opt(r"\(7x^3 - 6x^2 + 2x - 1\)", False), make_opt(r"\(3x^3 + 2x^2 + 2x + 9\)", False)],
        r"Step 1: Write the subtraction expression: \((5x^3 - 2x^2 - x + 4) - (2x^3 - 4x^2 + 3x - 5)\)." + "\n" +
        r"Step 2: Change signs of subtrahend: \(5x^3 - 2x^2 - x + 4 - 2x^3 + 4x^2 - 3x + 5\)." + "\n" +
        r"Step 3: Combine like terms: \((5-2)x^3 + (-2+4)x^2 + (-1-3)x + (4+5) = 3x^3 + 2x^2 - 4x + 9\)."
    ),
    # 2
    (
        r"Multiply \((2x^2 - 3)\) by \((3x^2 + 4x - 1)\). What is the coefficient of \(x^2\) in the product?",
        [make_opt(r"\(-11\)", True), make_opt(r"\(-9\)", False), make_opt(r"\(8\)", False), make_opt(r"\(-2\)", False)],
        r"Step 1: Distribute: \(2x^2(3x^2 + 4x - 1) - 3(3x^2 + 4x - 1) = 6x^4 + 8x^3 - 2x^2 - 9x^2 - 12x + 3\)." + "\n" +
        r"Step 2: Combine the \(x^2\) terms: \(-2x^2 - 9x^2 = -11x^2\)." + "\n" +
        r"Step 3: The coefficient of \(x^2\) is \(-11\)."
    ),
    # 3
    (
        r"Add the polynomials \(p(m) = 3m^2 n - 5m n^2 + 7\) and \(q(m) = 2m n^2 - m^2 n + 3\).",
        [make_opt(r"\(2m^2 n - 3m n^2 + 10\)", True), make_opt(r"\(4m^2 n - 7m n^2 + 10\)", False), make_opt(r"\(2m^2 n + 3m n^2 + 10\)", False), make_opt(r"\(m^2 n - 3m n^2 + 4\)", False)],
        r"Step 1: Group like terms together: \((3m^2 n - m^2 n) + (-5m n^2 + 2m n^2) + (7 + 3)\)." + "\n" +
        r"Step 2: Simplify each group: \(2m^2 n - 3m n^2 + 10\)." + "\n" +
        r"Step 3: The resulting sum is \(2m^2 n - 3m n^2 + 10\)."
    ),
    # 4
    (
        r"What must be added to \((3x^2 - 5x + 6)\) to obtain \((5x^2 - 2x + 1)\)?",
        [make_opt(r"\(2x^2 + 3x - 5\)", True), make_opt(r"\(2x^2 - 7x + 7\)", False), make_opt(r"\(8x^2 - 7x + 7\)", False), make_opt(r"\(-2x^2 - 3x + 5\)", False)],
        r"Step 1: Required polynomial is \((5x^2 - 2x + 1) - (3x^2 - 5x + 6)\)." + "\n" +
        r"Step 2: Distribute negative sign: \(5x^2 - 2x + 1 - 3x^2 + 5x - 6\)." + "\n" +
        r"Step 3: Combine like terms: \((5-3)x^2 + (-2+5)x + (1-6) = 2x^2 + 3x - 5\)."
    ),
    # 5
    (
        r"Simplify \((x + 2)(x - 3)(x + 4)\). What is the constant term?",
        [make_opt(r"\(-24\)", True), make_opt(r"\(24\)", False), make_opt(r"\(-12\)", False), make_opt(r"\(12\)", False)],
        r"Step 1: The constant term of a product of linear factors is the product of their individual constant terms." + "\n" +
        r"Step 2: Here the constants are \(2, -3, 4\)." + "\n" +
        r"Step 3: Product = \(2 \times (-3) \times 4 = -24\)."
    ),
    # 6
    (
        r"Multiply \((x^3 - 2)\) by \((x^2 + 2x + 4)\).",
        [make_opt(r"\(x^5 + 2x^4 + 4x^3 - 2x^2 - 4x - 8\)", True), make_opt(r"\(x^5 - 8\)", False), make_opt(r"\(x^5 + 4x^3 - 8\)", False), make_opt(r"\(x^6 - 8\)", False)],
        r"Step 1: Expand by distribution: \(x^3(x^2 + 2x + 4) - 2(x^2 + 2x + 4)\)." + "\n" +
        r"Step 2: Multiply each term: \(x^5 + 2x^4 + 4x^3 - 2x^2 - 4x - 8\)." + "\n" +
        r"Step 3: Since all exponents are distinct (5, 4, 3, 2, 1, 0), this is the simplest form."
    )
]

for idx, (txt, opts, sol) in enumerate(exam_32):
    q_code = f"MH-9-MTH1-3-3.2-OSC-{101 + idx:03d}"
    questions_32_33.append(make_q(q_code, txt, opts, sol, t_code_32, t_name_32, "exam", "medium"))

found_32 = [
    # 1
    (
        r"Add \((2x + 3)\) and \((3x + 5)\).",
        [make_opt(r"\(5x + 8\)", True), make_opt(r"\(6x + 8\)", False), make_opt(r"\(5x + 15\)", False), make_opt(r"\(6x + 15\)", False)],
        r"Step 1: Group like terms: \((2x + 3x) + (3 + 5)\)." + "\n" +
        r"Step 2: Add coefficients: \(2 + 3 = 5\) and constants \(3 + 5 = 8\)." + "\n" +
        r"Step 3: Sum is \(5x + 8\)."
    ),
    # 2
    (
        r"Subtract \((x + 2)\) from \((4x + 7)\).",
        [make_opt(r"\(3x + 5\)", True), make_opt(r"\(3x + 9\)", False), make_opt(r"\(5x + 5\)", False), make_opt(r"\(3x - 5\)", False)],
        r"Step 1: Write expression: \((4x + 7) - (x + 2)\)." + "\n" +
        r"Step 2: Distribute subtraction: \(4x + 7 - x - 2\)." + "\n" +
        r"Step 3: Combine like terms: \((4-1)x + (7-2) = 3x + 5\)."
    ),
    # 3
    (
        r"Multiply \(3x\) by \((2x - 4)\).",
        [make_opt(r"\(6x^2 - 12x\)", True), make_opt(r"\(6x - 12\)", False), make_opt(r"\(5x^2 - 12x\)", False), make_opt(r"\(6x^2 - 7x\)", False)],
        r"Step 1: Distribute \(3x\) across parentheses: \(3x \times 2x - 3x \times 4\)." + "\n" +
        r"Step 2: Compute products: \(6x^2 - 12x\)." + "\n" +
        r"Step 3: Result is \(6x^2 - 12x\)."
    ),
    # 4
    (
        r"What is \((x + 3)(x + 5)\)?",
        [make_opt(r"\(x^2 + 8x + 15\)", True), make_opt(r"\(x^2 + 15x + 8\)", False), make_opt(r"\(x^2 + 8x + 8\)", False), make_opt(r"\(2x + 8\)", False)],
        r"Step 1: Use binomial multiplication formula \((x+a)(x+b) = x^2 + (a+b)x + ab\)." + "\n" +
        r"Step 2: Here \(a = 3, b = 5\). So \(a+b = 8\) and \(ab = 15\)." + "\n" +
        r"Step 3: Result is \(x^2 + 8x + 15\)."
    ),
    # 5
    (
        r"Add \((x^2 - 3x)\) and \((2x^2 + 5x)\).",
        [make_opt(r"\(3x^2 + 2x\)", True), make_opt(r"\(3x^2 + 8x\)", False), make_opt(r"\(2x^2 + 2x\)", False), make_opt(r"\(3x^2 - 2x\)", False)],
        r"Step 1: Group like terms: \((x^2 + 2x^2) + (-3x + 5x)\)." + "\n" +
        r"Step 2: Simplify: \((1+2)x^2 + (-3+5)x = 3x^2 + 2x\)." + "\n" +
        r"Step 3: Sum is \(3x^2 + 2x\)."
    ),
    # 6
    (
        r"Find \((2x - 1)(x + 4)\).",
        [make_opt(r"\(2x^2 + 7x - 4\)", True), make_opt(r"\(2x^2 + 8x - 4\)", False), make_opt(r"\(2x^2 + 7x + 4\)", False), make_opt(r"\(2x^2 - 7x - 4\)", False)],
        r"Step 1: Expand: \(2x(x + 4) - 1(x + 4) = 2x^2 + 8x - x - 4\)." + "\n" +
        r"Step 2: Combine linear terms: \(8x - x = 7x\)." + "\n" +
        r"Step 3: Result is \(2x^2 + 7x - 4\)."
    ),
    # 7
    (
        r"Subtract \((3y^2 + 2)\) from \((5y^2 + 6)\).",
        [make_opt(r"\(2y^2 + 4\)", True), make_opt(r"\(8y^2 + 8\)", False), make_opt(r"\(2y^2 - 4\)", False), make_opt(r"\(-2y^2 - 4\)", False)],
        r"Step 1: \((5y^2 + 6) - (3y^2 + 2) = 5y^2 + 6 - 3y^2 - 2\)." + "\n" +
        r"Step 2: \((5-3)y^2 + (6-2) = 2y^2 + 4\)." + "\n" +
        r"Step 3: Result is \(2y^2 + 4\)."
    ),
    # 8
    (
        r"What is the degree of the product \((x^2 + 1)(x^3 + 2)\)?",
        [make_opt(r"\(5\)", True), make_opt(r"\(6\)", False), make_opt(r"\(3\)", False), make_opt(r"\(2\)", False)],
        r"Step 1: Leading term of first factor is \(x^2\) (degree 2)." + "\n" +
        r"Step 2: Leading term of second factor is \(x^3\) (degree 3)." + "\n" +
        r"Step 3: Degree of product is \(2 + 3 = 5\)."
    ),
    # 9
    (
        r"Simplify \((a + b) + (a - b)\).",
        [make_opt(r"\(2a\)", True), make_opt(r"\(2b\)", False), make_opt(r"\(a^2 - b^2\)", False), make_opt(r"\(0\)", False)],
        r"Step 1: Group like terms: \((a + a) + (b - b)\)." + "\n" +
        r"Step 2: \(a + a = 2a\) and \(b - b = 0\)." + "\n" +
        r"Step 3: Sum is \(2a\)."
    ),
    # 10
    (
        r"Simplify \((a + b)(a - b)\).",
        [make_opt(r"\(a^2 - b^2\)", True), make_opt(r"\(a^2 + b^2\)", False), make_opt(r"\(a^2 - 2ab + b^2\)", False), make_opt(r"\(2a\)", False)],
        r"Step 1: Expand product: \(a(a - b) + b(a - b) = a^2 - ab + ab - b^2\)." + "\n" +
        r"Step 2: Cancel \(-ab + ab = 0\)." + "\n" +
        r"Step 3: Result is the standard algebraic identity \(a^2 - b^2\)."
    ),
    # 11
    (
        r"Add \((4x^3 - 1)\) and \((2x^3 + 7)\).",
        [make_opt(r"\(6x^3 + 6\)", True), make_opt(r"\(6x^6 + 6\)", False), make_opt(r"\(2x^3 + 6\)", False), make_opt(r"\(6x^3 - 6\)", False)],
        r"Step 1: Combine like cubic terms: \(4x^3 + 2x^3 = 6x^3\)." + "\n" +
        r"Step 2: Combine constants: \(-1 + 7 = 6\)." + "\n" +
        r"Step 3: Result is \(6x^3 + 6\)."
    ),
    # 12
    (
        r"Multiply \(-2x\) by \((x^2 - 3x + 4)\).",
        [make_opt(r"\(-2x^3 + 6x^2 - 8x\)", True), make_opt(r"\(-2x^3 - 6x^2 + 8x\)", False), make_opt(r"\(2x^3 - 6x^2 + 8x\)", False), make_opt(r"\(-2x^3 + 6x^2 + 8x\)", False)],
        r"Step 1: Distribute \(-2x\): \((-2x)(x^2) + (-2x)(-3x) + (-2x)(4)\)." + "\n" +
        r"Step 2: Calculate each term: \(-2x^3 + 6x^2 - 8x\)." + "\n" +
        r"Step 3: Result is \(-2x^3 + 6x^2 - 8x\)."
    ),
    # 13
    (
        r"Subtract \((5x - 2)\) from \((5x - 2)\).",
        [make_opt(r"\(0\)", True), make_opt(r"\(10x - 4\)", False), make_opt(r"\(1\)", False), make_opt(r"\(-10x + 4\)", False)],
        r"Step 1: Any polynomial subtracted from itself equals zero: \(P(x) - P(x) = 0\)." + "\n" +
        r"Step 2: \((5x - 2) - (5x - 2) = 5x - 2 - 5x + 2 = 0\)." + "\n" +
        r"Step 3: Result is \(0\)."
    ),
    # 14
    (
        r"What is \((x + 4)^2\)?",
        [make_opt(r"\(x^2 + 8x + 16\)", True), make_opt(r"\(x^2 + 16\)", False), make_opt(r"\(x^2 + 4x + 16\)", False), make_opt(r"\(x^2 + 8x + 8\)", False)],
        r"Step 1: Use identity \((a + b)^2 = a^2 + 2ab + b^2\)." + "\n" +
        r"Step 2: With \(a = x, b = 4\): \(x^2 + 2(x)(4) + 4^2 = x^2 + 8x + 16\)." + "\n" +
        r"Step 3: Result is \(x^2 + 8x + 16\)."
    ),
    # 15
    (
        r"What is \((x - 5)^2\)?",
        [make_opt(r"\(x^2 - 10x + 25\)", True), make_opt(r"\(x^2 - 25\)", False), make_opt(r"\(x^2 + 10x + 25\)", False), make_opt(r"\(x^2 - 5x + 25\)", False)],
        r"Step 1: Use identity \((a - b)^2 = a^2 - 2ab + b^2\)." + "\n" +
        r"Step 2: With \(a = x, b = 5\): \(x^2 - 2(x)(5) + 5^2 = x^2 - 10x + 25\)." + "\n" +
        r"Step 3: Result is \(x^2 - 10x + 25\)."
    ),
    # 16
    (
        r"Simplify \((3x^2) \times (4x^3)\).",
        [make_opt(r"\(12x^5\)", True), make_opt(r"\(12x^6\)", False), make_opt(r"\(7x^5\)", False), make_opt(r"\(7x^6\)", False)],
        r"Step 1: Multiply numerical coefficients: \(3 \times 4 = 12\)." + "\n" +
        r"Step 2: Add exponents of variable: \(x^2 \times x^3 = x^{2+3} = x^5\)." + "\n" +
        r"Step 3: Result is \(12x^5\)."
    ),
    # 17
    (
        r"Add \((x + y + z)\) and \((x - y - z)\).",
        [make_opt(r"\(2x\)", True), make_opt(r"\(2x + 2y + 2z\)", False), make_opt(r"\(0\)", False), make_opt(r"\(2y + 2z\)", False)],
        r"Step 1: Combine like terms: \((x + x) + (y - y) + (z - z)\)." + "\n" +
        r"Step 2: \(x + x = 2x\), while \(y - y = 0\) and \(z - z = 0\)." + "\n" +
        r"Step 3: Sum is \(2x\)."
    ),
    # 18
    (
        r"What is the coefficient of \(x\) in \((x + 2)(x - 7)\)?",
        [make_opt(r"\(-5\)", True), make_opt(r"\(5\)", False), make_opt(r"\(-14\)", False), make_opt(r"\(2\)", False)],
        r"Step 1: Expand: \(x^2 - 7x + 2x - 14 = x^2 - 5x - 14\)." + "\n" +
        r"Step 2: The term containing \(x\) is \(-5x\)." + "\n" +
        r"Step 3: The coefficient is \(-5\)."
    ),
    # 19
    (
        r"Subtract \((2x - 3)\) from \((7x + 1)\).",
        [make_opt(r"\(5x + 4\)", True), make_opt(r"\(5x - 2\)", False), make_opt(r"\(9x - 2\)", False), make_opt(r"\(5x - 4\)", False)],
        r"Step 1: \((7x + 1) - (2x - 3) = 7x + 1 - 2x + 3\)." + "\n" +
        r"Step 2: \((7-2)x + (1+3) = 5x + 4\)." + "\n" +
        r"Step 3: Result is \(5x + 4\)."
    ),
    # 20
    (
        r"Multiply \((x + 1)\) by \(0\).",
        [make_opt(r"\(0\)", True), make_opt(r"\(x + 1\)", False), make_opt(r"\(1\)", False), make_opt(r"Undefined", False)],
        r"Step 1: Multiplying any polynomial by the zero polynomial results in the zero polynomial." + "\n" +
        r"Step 2: \(0 \times (x + 1) = 0\)." + "\n" +
        r"Step 3: Result is \(0\)."
    )
]

for idx, (txt, opts, sol) in enumerate(found_32):
    q_code = f"MH-9-MTH1-3-3.2-OSC-{151 + idx:03d}"
    questions_32_33.append(make_q(q_code, txt, opts, sol, t_code_32, t_name_32, "foundation", "easy"))

print(f"Total after 3.2: {len(questions_32_33)} questions")

# Save checkpoint
with open("scripts/mh9_mth1_ch3_32_generated.json", "w", encoding="utf-8") as f:
    json.dump(questions_32_33, f, indent=2)
