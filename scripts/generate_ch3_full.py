# scripts/generate_ch3_full.py
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
        "createdAt": "2026-11-21T12:48:00.000Z",
        "updatedAt": "2026-11-21T12:48:00.000Z"
    }

questions = []

# Load questions from generate_ch3_topup.py logic for 3.1.1
import generate_ch3_topup
questions.extend(generate_ch3_topup.questions)
print(f"Loaded 3.1.1: {len(questions)} questions")

# ==========================================
# Topic 3.1.2: Standard form, Index form, and Coefficient form
# T_CODE = "MH-9-MTH1-3-3.1.2", T_NAME = "Standard form, Index form, and Coefficient form"
# Need 20 Exam, 20 Foundation
# ==========================================
t_code = "MH-9-MTH1-3-3.1.2"
t_name = "Standard form, Index form, and Coefficient form"

exam_data_312 = [
    # 1
    (
        r"Write the polynomial \(p(x) = 3 - 5x + 2x^4 - x^2\) in standard form.",
        [make_opt(r"\(2x^4 - x^2 - 5x + 3\)", True), make_opt(r"\(3 - 5x - x^2 + 2x^4\)", False), make_opt(r"\(2x^4 + x^2 - 5x + 3\)", False), make_opt(r"\(-5x + 2x^4 - x^2 + 3\)", False)],
        r"Step 1: Standard form arranges terms in descending order of powers of the variable." + "\n" +
        r"Step 2: Powers of \(x\) present are 4, 2, 1, 0." + "\n" +
        r"Step 3: Arranging descendingly gives \(2x^4 - x^2 - 5x + 3\)."
    ),
    # 2
    (
        r"What is the index form of the polynomial \(5x^4 - 2x + 7\)?",
        [make_opt(r"\(5x^4 + 0x^3 + 0x^2 - 2x + 7\)", True), make_opt(r"\(5x^4 + x^3 + x^2 - 2x + 7\)", False), make_opt(r"\(5x^4 - 2x^2 + 7\)", False), make_opt(r"\(5x^4 - 2x + 7\)", False)],
        r"Step 1: Degree of the polynomial is 4." + "\n" +
        r"Step 2: Index form writes all powers from 4 down to 0, using coefficient 0 for missing terms (\(x^3\) and \(x^2\))." + "\n" +
        r"Step 3: The index form is \(5x^4 + 0x^3 + 0x^2 - 2x + 7\)."
    ),
    # 3
    (
        r"What is the coefficient form of the polynomial \(x^3 - 8\)?",
        [make_opt(r"\((1, -8)\)", False), make_opt(r"\((1, 0, 0, -8)\)", True), make_opt(r"\((1, 0, -8)\)", False), make_opt(r"\((0, 0, 1, -8)\)", False)],
        r"Step 1: Write the polynomial in index form: \(x^3 + 0x^2 + 0x - 8\)." + "\n" +
        r"Step 2: List the coefficients in order of descending powers enclosed in parentheses: 1, 0, 0, -8." + "\n" +
        r"Step 3: The coefficient form is \((1, 0, 0, -8)\)."
    ),
    # 4
    (
        r"Convert the coefficient form \((2, -3, 0, 5, -1)\) into polynomial form with variable \(m\).",
        [make_opt(r"\(2m^4 - 3m^3 + 5m - 1\)", True), make_opt(r"\(2m^5 - 3m^4 + 5m^2 - m\)", False), make_opt(r"\(2m^4 - 3m^3 + 5m^2 - 1\)", False), make_opt(r"\(2m^3 - 3m^2 + 5m - 1\)", False)],
        r"Step 1: Number of coefficients in \((2, -3, 0, 5, -1)\) is \(5\)." + "\n" +
        r"Step 2: Degree of the polynomial is \(5 - 1 = 4\)." + "\n" +
        r"Step 3: Writing with variable \(m\): \(2m^4 - 3m^3 + 0m^2 + 5m - 1 = 2m^4 - 3m^3 + 5m - 1\)."
    ),
    # 5
    (
        r"How many zeros are present in the index form of the polynomial \(y^5 - 1\)?",
        [make_opt(r"\(3\)", False), make_opt(r"\(4\)", True), make_opt(r"\(5\)", False), make_opt(r"\(2\)", False)],
        r"Step 1: The polynomial is \(y^5 - 1\), with degree 5." + "\n" +
        r"Step 2: In index form: \(y^5 + 0y^4 + 0y^3 + 0y^2 + 0y - 1\)." + "\n" +
        r"Step 3: The terms with zero coefficient are \(0y^4, 0y^3, 0y^2, 0y\), giving exactly 4 zeros."
    ),
    # 6
    (
        r"If the coefficient form of a polynomial is \((-4, 0, 7)\), what is its degree?",
        [make_opt(r"\(3\)", False), make_opt(r"\(2\)", True), make_opt(r"\(1\)", False), make_opt(r"\(0\)", False)],
        r"Step 1: Count the number of entries in the coefficient tuple: \(n = 3\)." + "\n" +
        r"Step 2: For any non-zero polynomial, \(\text{Degree} = \text{number of coefficients} - 1\)." + "\n" +
        r"Step 3: Degree is \(3 - 1 = 2\)."
    ),
    # 7
    (
        r"Express the constant polynomial \(-7\) in coefficient form.",
        [make_opt(r"\((-7)\)", True), make_opt(r"\((-7, 0)\)", False), make_opt(r"\((0, -7)\)", False), make_opt(r"\((-7, 0, 0)\)", False)],
        r"Step 1: The degree of \(-7\) is 0." + "\n" +
        r"Step 2: Number of coefficients is \(\text{degree} + 1 = 0 + 1 = 1\)." + "\n" +
        r"Step 3: The coefficient form is \((-7)\)."
    ),
    # 8
    (
        r"Write \(-2y^3 + 4y - y^5 + 6\) in index form.",
        [make_opt(r"\(-y^5 + 0y^4 - 2y^3 + 0y^2 + 4y + 6\)", True), make_opt(r"\(-y^5 - 2y^3 + 4y + 6\)", False), make_opt(r"\(y^5 + 0y^4 + 2y^3 + 0y^2 - 4y - 6\)", False), make_opt(r"\(-y^5 + 0y^4 - 2y^3 + 4y^2 + 0y + 6\)", False)],
        r"Step 1: Identify highest power: 5. Term is \(-y^5\)." + "\n" +
        r"Step 2: Add missing powers \(y^4\) and \(y^2\) with coefficient 0." + "\n" +
        r"Step 3: Descending index form is \(-y^5 + 0y^4 - 2y^3 + 0y^2 + 4y + 6\)."
    ),
    # 9
    (
        r"What is the coefficient form of \(p(x) = \frac{2}{3}x^2 - 5\)?",
        [make_opt(r"\(\left(\frac{2}{3}, 0, -5\right)\)", True), make_opt(r"\(\left(\frac{2}{3}, -5\right)\)", False), make_opt(r"\(\left(\frac{2}{3}, -5, 0\right)\)", False), make_opt(r"\((2, 0, -15)\)", False)],
        r"Step 1: Write in index form: \(\frac{2}{3}x^2 + 0x - 5\)." + "\n" +
        r"Step 2: Coefficients in descending order are \(\frac{2}{3}, 0, -5\)." + "\n" +
        r"Step 3: Hence, the coefficient form is \(\left(\frac{2}{3}, 0, -5\right)\)."
    ),
    # 10
    (
        r"What polynomial corresponds to the coefficient form \((1, 0, 0, 0, 1)\) using variable \(x\)?",
        [make_opt(r"\(x^4 + 1\)", True), make_opt(r"\(x^5 + 1\)", False), make_opt(r"\(x^3 + 1\)", False), make_opt(r"\(x^4 + x + 1\)", False)],
        r"Step 1: Number of coefficients = 5. Degree = \(5 - 1 = 4\)." + "\n" +
        r"Step 2: Terms are \(1 \cdot x^4 + 0 \cdot x^3 + 0 \cdot x^2 + 0 \cdot x + 1\)." + "\n" +
        r"Step 3: Simplifying gives \(x^4 + 1\)."
    ),
    # 11
    (
        r"Assertion (A): The coefficient form of \(3x^2 + 5\) is \((3, 0, 5)\)." + "\n" +
        r"Reason (R): Missing terms in descending powers must be represented with a coefficient of 0.",
        [make_opt(r"Both A and R are true and R is the correct explanation of A", True),
         make_opt(r"Both A and R are true but R is not the correct explanation of A", False),
         make_opt(r"A is true but R is false", False),
         make_opt(r"A is false but R is true", False)],
        r"Step 1: In \(3x^2 + 5\), the term with \(x^1\) is missing." + "\n" +
        r"Step 2: By rule of index form, we write \(3x^2 + 0x + 5\), so coefficient form is \((3, 0, 5)\). Thus A is true." + "\n" +
        r"Step 3: R states the standard rule for writing index and coefficient forms, accurately explaining A."
    ),
    # 12
    (
        r"Write \(p(m) = 5m^3 - m + 2m^4 - 8\) in standard form.",
        [make_opt(r"\(2m^4 + 5m^3 - m - 8\)", True), make_opt(r"\(5m^3 + 2m^4 - m - 8\)", False), make_opt(r"\(2m^4 - 8 + 5m^3 - m\)", False), make_opt(r"\(-8 - m + 5m^3 + 2m^4\)", False)],
        r"Step 1: Identify terms and powers: \(2m^4\) (power 4), \(5m^3\) (power 3), \(-m\) (power 1), \(-8\) (power 0)." + "\n" +
        r"Step 2: Standard form requires descending powers of variable." + "\n" +
        r"Step 3: Standard form is \(2m^4 + 5m^3 - m - 8\)."
    ),
    # 13
    (
        r"What is the coefficient form of \(7x^3 - 3x^2 + 4x - 9\)?",
        [make_opt(r"\((7, -3, 4, -9)\)", True), make_opt(r"\((7, 3, 4, 9)\)", False), make_opt(r"\((-9, 4, -3, 7)\)", False), make_opt(r"\((7, -3, 0, 4, -9)\)", False)],
        r"Step 1: Check if any powers from 3 to 0 are missing: 3, 2, 1, 0 are all present." + "\n" +
        r"Step 2: Coefficients in descending order: 7, -3, 4, -9." + "\n" +
        r"Step 3: Coefficient form is \((7, -3, 4, -9)\)."
    ),
    # 14
    (
        r"The coefficient form of a polynomial is \((3, -2, 0, 7, 0, -4)\). What is its degree and number of terms?",
        [make_opt(r"Degree 5, 4 non-zero terms", True), make_opt(r"Degree 6, 6 non-zero terms", False), make_opt(r"Degree 5, 6 non-zero terms", False), make_opt(r"Degree 4, 4 non-zero terms", False)],
        r"Step 1: Total entries = 6. Degree = \(6 - 1 = 5\)." + "\n" +
        r"Step 2: Non-zero entries are 3, -2, 7, -4, which is 4 non-zero terms." + "\n" +
        r"Step 3: Degree is 5, non-zero terms is 4."
    ),
    # 15
    (
        r"Which of the following polynomials in standard form is equivalent to \(4 - 3x^2 + x^3\)?",
        [make_opt(r"\(x^3 - 3x^2 + 4\)", True), make_opt(r"\(x^3 + 3x^2 + 4\)", False), make_opt(r"\(-3x^2 + x^3 + 4\)", False), make_opt(r"\(4 + x^3 - 3x^2\)", False)],
        r"Step 1: Arrange powers 3, 2, 0 in descending order." + "\n" +
        r"Step 2: Leading term is \(x^3\), next is \(-3x^2\), constant is \(+4\)." + "\n" +
        r"Step 3: Equivalent standard form is \(x^3 - 3x^2 + 4\)."
    ),
    # 16
    (
        r"Express the polynomial with coefficient form \((-1, 1)\) using variable \(y\).",
        [make_opt(r"\(-y + 1\)", True), make_opt(r"\(y - 1\)", False), make_opt(r"\(-y^2 + 1\)", False), make_opt(r"\(-1 + y\)", False)],
        r"Step 1: Number of coefficients = 2. Degree = \(2 - 1 = 1\)." + "\n" +
        r"Step 2: Polynomial is \(-1 \cdot y^1 + 1 \cdot y^0 = -y + 1\)." + "\n" +
        r"Step 3: The polynomial is \(-y + 1\)."
    ),
    # 17
    (
        r"Write \(p(t) = -t^2 + 5t^4 - 6\) in index form.",
        [make_opt(r"\(5t^4 + 0t^3 - t^2 + 0t - 6\)", True), make_opt(r"\(5t^4 - t^2 - 6\)", False), make_opt(r"\(-t^2 + 5t^4 + 0t^3 + 0t - 6\)", False), make_opt(r"\(5t^4 + 0t^3 + t^2 + 0t - 6\)", False)],
        r"Step 1: Degree is 4. Descending powers are 4, 3, 2, 1, 0." + "\n" +
        r"Step 2: Coefficients: \(t^4\) is 5, \(t^3\) is 0, \(t^2\) is -1, \(t^1\) is 0, constant is -6." + "\n" +
        r"Step 3: Index form is \(5t^4 + 0t^3 - t^2 + 0t - 6\)."
    ),
    # 18
    (
        r"What is the coefficient form of \(4x^4\)?",
        [make_opt(r"\((4, 0, 0, 0, 0)\)", True), make_opt(r"\((4, 0, 0, 0)\)", False), make_opt(r"\((4)\)", False), make_opt(r"\((0, 0, 0, 0, 4)\)", False)],
        r"Step 1: Degree of \(4x^4\) is 4." + "\n" +
        r"Step 2: Number of coefficients in coefficient form is \(\text{degree} + 1 = 4 + 1 = 5\)." + "\n" +
        r"Step 3: In index form: \(4x^4 + 0x^3 + 0x^2 + 0x + 0\). Thus, coefficient form is \((4, 0, 0, 0, 0)\)."
    ),
    # 19
    (
        r"What is the coefficient form of \(x^2 - x\)?",
        [make_opt(r"\((1, -1, 0)\)", True), make_opt(r"\((1, -1)\)", False), make_opt(r"\((1, 0, -1)\)", False), make_opt(r"\((-1, 1, 0)\)", False)],
        r"Step 1: Degree is 2. Descending powers: 2, 1, 0." + "\n" +
        r"Step 2: Index form: \(1x^2 - 1x + 0\)." + "\n" +
        r"Step 3: Coefficient form is \((1, -1, 0)\)."
    ),
    # 20
    (
        r"If the coefficient form of \(P(x)\) is \((a, b, c)\) and \(a \ne 0\), what type of polynomial is \(P(x)\)?",
        [make_opt(r"Quadratic polynomial", True), make_opt(r"Cubic polynomial", False), make_opt(r"Linear polynomial", False), make_opt(r"Constant polynomial", False)],
        r"Step 1: Count entries: 3 entries." + "\n" +
        r"Step 2: Degree is \(3 - 1 = 2\)." + "\n" +
        r"Step 3: A polynomial of degree 2 with non-zero leading coefficient \(a\) is a quadratic polynomial."
    )
]

for idx, (txt, opts, sol) in enumerate(exam_data_312):
    q_code = f"MH-9-MTH1-3-3.1.2-OSC-{101 + idx:03d}"
    questions.append(make_q(q_code, txt, opts, sol, t_code, t_name, "exam", "medium" if idx % 2 == 0 else "hard"))

found_data_312 = [
    # 1
    (
        r"Write \(3x + x^2 + 2\) in standard form.",
        [make_opt(r"\(x^2 + 3x + 2\)", True), make_opt(r"\(2 + 3x + x^2\)", False), make_opt(r"\(3x + x^2 + 2\)", False), make_opt(r"\(x^2 + 2 + 3x\)", False)],
        r"Step 1: Identify powers of \(x\): 1, 2, 0." + "\n" +
        r"Step 2: Arrange in decreasing order of powers: 2, then 1, then 0." + "\n" +
        r"Step 3: The standard form is \(x^2 + 3x + 2\)."
    ),
    # 2
    (
        r"What is the coefficient form of \(2x + 5\)?",
        [make_opt(r"\((2, 5)\)", True), make_opt(r"\((5, 2)\)", False), make_opt(r"\((2, 0, 5)\)", False), make_opt(r"\((2)\)", False)],
        r"Step 1: The polynomial is linear (degree 1)." + "\n" +
        r"Step 2: Coefficients from power 1 down to power 0 are 2 and 5." + "\n" +
        r"Step 3: The coefficient form is \((2, 5)\)."
    ),
    # 3
    (
        r"Convert the coefficient form \((3, 4)\) into polynomial form with variable \(x\).",
        [make_opt(r"\(3x + 4\)", True), make_opt(r"\(3x^2 + 4\)", False), make_opt(r"\(4x + 3\)", False), make_opt(r"\(3 + 4x\)", False)],
        r"Step 1: Number of coefficients is 2. Degree is \(2 - 1 = 1\)." + "\n" +
        r"Step 2: Powers: \(3 \cdot x^1 + 4 \cdot x^0\)." + "\n" +
        r"Step 3: The polynomial is \(3x + 4\)."
    ),
    # 4
    (
        r"What is the coefficient of \(x\) in \((5, -2, 7)\) using variable \(x\)?",
        [make_opt(r"\(-2\)", True), make_opt(r"\(5\)", False), make_opt(r"\(7\)", False), make_opt(r"\(0\)", False)],
        r"Step 1: Degree is \(3 - 1 = 2\)." + "\n" +
        r"Step 2: The polynomial is \(5x^2 - 2x + 7\)." + "\n" +
        r"Step 3: The coefficient of \(x\) is \(-2\)."
    ),
    # 5
    (
        r"What is the index form of \(x^2 - 9\)?",
        [make_opt(r"\(x^2 + 0x - 9\)", True), make_opt(r"\(x^2 - 9x\)", False), make_opt(r"\(x^2 - 0x - 9\)", False), make_opt(r"\(x^2 - 9\)", False)],
        r"Step 1: The linear term (\(x^1\)) is missing." + "\n" +
        r"Step 2: Add \(0x\) to show all descending powers 2, 1, 0." + "\n" +
        r"Step 3: The index form is \(x^2 + 0x - 9\)."
    ),
    # 6
    (
        r"What is the degree of a polynomial having coefficient form \((1, 2, 3, 4)\)?",
        [make_opt(r"\(3\)", True), make_opt(r"\(4\)", False), make_opt(r"\(2\)", False), make_opt(r"\(1\)", False)],
        r"Step 1: Count the elements in the tuple: 4 elements." + "\n" +
        r"Step 2: Degree equals number of elements minus 1." + "\n" +
        r"Step 3: Degree is \(4 - 1 = 3\)."
    ),
    # 7
    (
        r"Write \(5\) in coefficient form.",
        [make_opt(r"\((5)\)", True), make_opt(r"\((5, 0)\)", False), make_opt(r"\((0, 5)\)", False), make_opt(r"\((1, 5)\)", False)],
        r"Step 1: 5 is a constant polynomial of degree 0." + "\n" +
        r"Step 2: It has only 1 coefficient, which is 5." + "\n" +
        r"Step 3: The coefficient form is \((5)\)."
    ),
    # 8
    (
        r"What is the standard form of \(7 - x\)?",
        [make_opt(r"\(-x + 7\)", True), make_opt(r"\(x - 7\)", False), make_opt(r"\(7 - x\)", False), make_opt(r"\(-x - 7\)", False)],
        r"Step 1: Arrange variable term first, constant term second." + "\n" +
        r"Step 2: Variable term is \(-x\), constant term is \(+7\)." + "\n" +
        r"Step 3: Standard form is \(-x + 7\)."
    ),
    # 9
    (
        r"What polynomial corresponds to \((1, 0, -4)\)?",
        [make_opt(r"\(x^2 - 4\)", True), make_opt(r"\(x - 4\)", False), make_opt(r"\(x^3 - 4\)", False), make_opt(r"\(x^2 - 4x\)", False)],
        r"Step 1: Number of coefficients = 3, so degree = 2." + "\n" +
        r"Step 2: Expression: \(1x^2 + 0x - 4\)." + "\n" +
        r"Step 3: Simplifying gives \(x^2 - 4\)."
    ),
    # 10
    (
        r"What is the coefficient form of \(x^3\)?",
        [make_opt(r"\((1, 0, 0, 0)\)", True), make_opt(r"\((1)\)", False), make_opt(r"\((1, 0, 0)\)", False), make_opt(r"\((0, 0, 0, 1)\)", False)],
        r"Step 1: In index form, \(x^3 = 1x^3 + 0x^2 + 0x + 0\)." + "\n" +
        r"Step 2: List coefficients: 1, 0, 0, 0." + "\n" +
        r"Step 3: Coefficient form is \((1, 0, 0, 0)\)."
    ),
    # 11
    (
        r"How many coefficients are there in the coefficient form of a polynomial of degree 4?",
        [make_opt(r"\(5\)", True), make_opt(r"\(4\)", False), make_opt(r"\(3\)", False), make_opt(r"\(6\)", False)],
        r"Step 1: The terms in index form range from power 4 to power 0: \(x^4, x^3, x^2, x^1, x^0\)." + "\n" +
        r"Step 2: Count the powers: \(4 - 0 + 1 = 5\)." + "\n" +
        r"Step 3: Therefore, there are 5 coefficients."
    ),
    # 12
    (
        r"Write \(p(y) = y^3 + 4y\) in index form.",
        [make_opt(r"\(y^3 + 0y^2 + 4y + 0\)", True), make_opt(r"\(y^3 + 4y\)", False), make_opt(r"\(y^3 + 4y^2 + 0y\)", False), make_opt(r"\(y^3 + 0y^2 + 4y\)", False)],
        r"Step 1: Degree is 3. Powers needed: 3, 2, 1, 0." + "\n" +
        r"Step 2: Missing terms are \(y^2\) and constant \(y^0\)." + "\n" +
        r"Step 3: Index form is \(y^3 + 0y^2 + 4y + 0\)."
    ),
    # 13
    (
        r"What is the coefficient form of \(3y^2 - 2y + 1\)?",
        [make_opt(r"\((3, -2, 1)\)", True), make_opt(r"\((3, 2, 1)\)", False), make_opt(r"\((1, -2, 3)\)", False), make_opt(r"\((3, -2)\)", False)],
        r"Step 1: All terms are in descending order: degree 2, 1, 0." + "\n" +
        r"Step 2: The coefficients are 3, -2, 1." + "\n" +
        r"Step 3: The coefficient form is \((3, -2, 1)\)."
    ),
    # 14
    (
        r"Which of the following is in standard form?",
        [make_opt(r"\(5x^3 - 2x^2 + x - 7\)", True), make_opt(r"\(x - 7 + 5x^3 - 2x^2\)", False), make_opt(r"\(-7 + x - 2x^2 + 5x^3\)", False), make_opt(r"\(5x^3 + x - 2x^2 - 7\)", False)],
        r"Step 1: Standard form requires powers to be strictly decreasing: 3, 2, 1, 0." + "\n" +
        r"Step 2: In \(5x^3 - 2x^2 + x - 7\), exponents are 3, 2, 1, 0." + "\n" +
        r"Step 3: This polynomial is in standard form."
    ),
    # 15
    (
        r"Convert coefficient form \((6, 0, 0)\) to polynomial form with variable \(x\).",
        [make_opt(r"\(6x^2\)", True), make_opt(r"\(6x\)", False), make_opt(r"\(6x^3\)", False), make_opt(r"\(6\)", False)],
        r"Step 1: Number of entries is 3, so degree is \(3 - 1 = 2\)." + "\n" +
        r"Step 2: Expression: \(6x^2 + 0x + 0\)." + "\n" +
        r"Step 3: Simplifying gives \(6x^2\)."
    ),
    # 16
    (
        r"What is the constant term in the polynomial represented by \((4, 3, -8)\)?",
        [make_opt(r"\(-8\)", True), make_opt(r"\(4\)", False), make_opt(r"\(3\)", False), make_opt(r"\(0\)", False)],
        r"Step 1: The polynomial is \(4x^2 + 3x - 8\)." + "\n" +
        r"Step 2: The last entry in coefficient form corresponds to the constant term (power 0)." + "\n" +
        r"Step 3: The constant term is \(-8\)."
    ),
    # 17
    (
        r"Write \(-x^2 + 8\) in coefficient form.",
        [make_opt(r"\((-1, 0, 8)\)", True), make_opt(r"\((-1, 8)\)", False), make_opt(r"\((1, 0, 8)\)", False), make_opt(r"\((-1, 8, 0)\)", False)],
        r"Step 1: Index form: \(-1x^2 + 0x + 8\)." + "\n" +
        r"Step 2: List coefficients: -1, 0, 8." + "\n" +
        r"Step 3: Coefficient form is \((-1, 0, 8)\)."
    ),
    # 18
    (
        r"What is the leading coefficient of the polynomial represented by \((-5, 2, 1, 4)\)?",
        [make_opt(r"\(-5\)", True), make_opt(r"\(4\)", False), make_opt(r"\(2\)", False), make_opt(r"\(1\)", False)],
        r"Step 1: The leading coefficient is the coefficient of the highest power term." + "\n" +
        r"Step 2: In coefficient form, the first entry is the leading coefficient." + "\n" +
        r"Step 3: Hence, the leading coefficient is \(-5\)."
    ),
    # 19
    (
        r"What is the coefficient form of \(0\)?",
        [make_opt(r"\((0)\)", True), make_opt(r"\((0, 0)\)", False), make_opt(r"Undefined", False), make_opt(r"\(()\)", False)],
        r"Step 1: The zero polynomial has a single coefficient 0." + "\n" +
        r"Step 2: Enclosing in parentheses gives \((0)\)." + "\n" +
        r"Step 3: Coefficient form is \((0)\)."
    ),
    # 20
    (
        r"What polynomial corresponds to \((2, 0, 3, 0)\) with variable \(y\)?",
        [make_opt(r"\(2y^3 + 3y\)", True), make_opt(r"\(2y^2 + 3\)", False), make_opt(r"\(2y^4 + 3y^2\)", False), make_opt(r"\(2y^3 + 3y^2\)", False)],
        r"Step 1: Number of entries = 4, degree = \(4 - 1 = 3\)." + "\n" +
        r"Step 2: Expression: \(2y^3 + 0y^2 + 3y^1 + 0 = 2y^3 + 3y\)." + "\n" +
        r"Step 3: Result is \(2y^3 + 3y\)."
    )
]

for idx, (txt, opts, sol) in enumerate(found_data_312):
    q_code = f"MH-9-MTH1-3-3.1.2-OSC-{151 + idx:03d}"
    questions.append(make_q(q_code, txt, opts, sol, t_code, t_name, "foundation", "easy"))

print(f"Total after 3.1.2: {len(questions)} questions")

# Save checkpoint
with open("scripts/mh9_mth1_ch3_all_generated.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)
