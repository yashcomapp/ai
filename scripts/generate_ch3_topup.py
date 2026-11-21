# scripts/generate_ch3_topup.py
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
        "createdAt": "2026-11-21T12:46:00.000Z",
        "updatedAt": "2026-11-21T12:46:00.000Z"
    }

questions = []

# ==========================================
# Topic 3.1.1: Degree in one and more variables
# T_CODE = "MH-9-MTH1-3-3.1.1", T_NAME = "Degree in one and more variables"
# Need 20 Exam, 20 Foundation
# ==========================================
t_code = "MH-9-MTH1-3-3.1.1"
t_name = "Degree in one and more variables"

# 20 Exam (Seq 101 to 120)
exam_data_311 = [
    # 1
    (
        r"What is the degree of the multivariable polynomial \(7x^3 y^4 - 5x^2 y^6 + 9xy^2 - 11\)?",
        [make_opt(r"\(7\)", False), make_opt(r"\(8\)", True), make_opt(r"\(6\)", False), make_opt(r"\(9\)", False)],
        r"Step 1: In a multivariable polynomial, the degree of each term is the sum of exponents of the variables in that term." + "\n" +
        r"Step 2: Calculate degree of each term: \(7x^3y^4 \rightarrow 3+4=7\); \(-5x^2y^6 \rightarrow 2+6=8\); \(9xy^2 \rightarrow 1+2=3\)." + "\n" +
        r"Step 3: The highest sum is \(8\), so the degree of the polynomial is \(8\)."
    ),
    # 2
    (
        r"Which of the following algebraic expressions is a valid polynomial?",
        [make_opt(r"\(3x^2 + \frac{5}{x} - 7\)", False), make_opt(r"\(4\sqrt{x} + 2x - 1\)", False), make_opt(r"\(\frac{2}{3}y^3 - \sqrt{5}y^2 + \pi\)", True), make_opt(r"\(x^{-2} + 6x + 9\)", False)],
        r"Step 1: An algebraic expression is a polynomial if and only if all powers of the variable(s) are non-negative integers (whole numbers)." + "\n" +
        r"Step 2: In \(\frac{2}{3}y^3 - \sqrt{5}y^2 + \pi\), the exponents of \(y\) are 3 and 2 (whole numbers). The coefficients \(\frac{2}{3}, -\sqrt{5}, \pi\) are real numbers, which is permitted." + "\n" +
        r"Step 3: Expressions with \(\frac{1}{x} = x^{-1}\), \(\sqrt{x} = x^{1/2}\), or negative powers are not polynomials."
    ),
    # 3
    (
        r"What is the degree of the zero polynomial \(0\)?",
        [make_opt(r"\(0\)", False), make_opt(r"\(1\)", False), make_opt(r"Not defined", True), make_opt(r"\(-1\)", False)],
        r"Step 1: The degree of any non-zero constant polynomial (e.g., \(5 = 5x^0\)) is 0." + "\n" +
        r"Step 2: However, for the zero polynomial \(P(x) = 0\), it can be written as \(0x^n\) for any \(n \ge 0\)." + "\n" +
        r"Step 3: By mathematical definition and Maharashtra State Board convention, the degree of the zero polynomial is not defined."
    ),
    # 4
    (
        r"Find the degree of the polynomial \(m^5 n^2 p - 3m^4 n^4 p^2 + 8mnp^5\).",
        [make_opt(r"\(8\)", False), make_opt(r"\(10\)", True), make_opt(r"\(7\)", False), make_opt(r"\(9\)", False)],
        r"Step 1: Sum powers of variables in each term:" + "\n" +
        r"Term 1: \(m^5 n^2 p \rightarrow 5 + 2 + 1 = 8\)." + "\n" +
        r"Term 2: \(-3m^4 n^4 p^2 \rightarrow 4 + 4 + 2 = 10\)." + "\n" +
        r"Term 3: \(8mnp^5 \rightarrow 1 + 1 + 5 = 7\)." + "\n" +
        r"Step 2: The highest sum of powers is \(10\)." + "\n" +
        r"Step 3: Thus, the degree of the polynomial is \(10\)."
    ),
    # 5
    (
        r"What is the degree of the constant polynomial \(-\sqrt{17}\)?",
        [make_opt(r"\(0\)", True), make_opt(r"\(\frac{1}{2}\)", False), make_opt(r"\(1\)", False), make_opt(r"Not defined", False)],
        r"Step 1: A constant polynomial \(c \ne 0\) can be expressed as \(c \cdot x^0\)." + "\n" +
        r"Step 2: Here, \(-\sqrt{17} = -\sqrt{17} \cdot x^0\) with \(x \ne 0\)." + "\n" +
        r"Step 3: The highest exponent of the variable is \(0\), so its degree is \(0\)."
    ),
    # 6
    (
        r"If the degree of polynomial \(P(x)\) is \(5\) and the degree of polynomial \(Q(x)\) is \(3\), what is the degree of \(P(x) \times Q(x)\)?",
        [make_opt(r"\(15\)", False), make_opt(r"\(8\)", True), make_opt(r"\(5\)", False), make_opt(r"\(2\)", False)],
        r"Step 1: The product of the leading terms \(a x^5\) and \(b x^3\) gives \(ab x^{5+3} = ab x^8\) where \(ab \ne 0\)." + "\n" +
        r"Step 2: Hence, \(\deg(P \times Q) = \deg(P) + \deg(Q) = 5 + 3 = 8\)." + "\n" +
        r"Step 3: Therefore, the degree of the product is \(8\)."
    ),
    # 7
    (
        r"If the degree of polynomial \(P(x)\) is \(6\) and the degree of polynomial \(Q(x)\) is \(4\), what is the degree of \(P(x) + Q(x)\)?",
        [make_opt(r"\(10\)", False), make_opt(r"\(6\)", True), make_opt(r"\(4\)", False), make_opt(r"\(2\)", False)],
        r"Step 1: In the sum \(P(x) + Q(x)\), the highest power term comes from \(P(x)\), which has power 6." + "\n" +
        r"Step 2: Since \(\deg(P) > \deg(Q)\), the term of degree 6 cannot be cancelled by \(Q(x)\)." + "\n" +
        r"Step 3: Therefore, \(\deg(P + Q) = \max(\deg(P), \deg(Q)) = 6\)."
    ),
    # 8
    (
        r"What is the degree of the polynomial \((x^3 + 2)(x^4 - 5x + 1)\)?",
        [make_opt(r"\(12\)", False), make_opt(r"\(7\)", True), make_opt(r"\(4\)", False), make_opt(r"\(3\)", False)],
        r"Step 1: Leading term of first factor is \(x^3\) (degree 3)." + "\n" +
        r"Step 2: Leading term of second factor is \(x^4\) (degree 4)." + "\n" +
        r"Step 3: Product leading term is \(x^3 \times x^4 = x^{3+4} = x^7\). Thus the degree is \(7\)."
    ),
    # 9
    (
        r"In the polynomial \(5x^4 - 3x^6 + 2x^2 + 10\), what is the leading coefficient?",
        [make_opt(r"\(5\)", False), make_opt(r"\(-3\)", True), make_opt(r"\(10\)", False), make_opt(r"\(2\)", False)],
        r"Step 1: Identify the degree of the polynomial: the highest power of \(x\) is \(6\)." + "\n" +
        r"Step 2: The term with the highest power is \(-3x^6\)." + "\n" +
        r"Step 3: The leading coefficient is the coefficient of this term, which is \(-3\)."
    ),
    # 10
    (
        r"Classify the polynomial \(p(y) = 2y - 9\) according to its degree.",
        [make_opt(r"Linear polynomial", True), make_opt(r"Quadratic polynomial", False), make_opt(r"Cubic polynomial", False), make_opt(r"Constant polynomial", False)],
        r"Step 1: Find the highest exponent of the variable \(y\) in \(2y - 9\)." + "\n" +
        r"Step 2: The highest exponent is \(1\), so the degree of the polynomial is \(1\)." + "\n" +
        r"Step 3: A polynomial of degree \(1\) is called a linear polynomial."
    ),
    # 11
    (
        r"Classify the polynomial \(3x^2 - 5x + 7\) according to its number of terms.",
        [make_opt(r"Monomial", False), make_opt(r"Binomial", False), make_opt(r"Trinomial", True), make_opt(r"Linear", False)],
        r"Step 1: Count the number of non-zero terms separated by \(+\) or \(-\)." + "\n" +
        r"Step 2: The terms are \(3x^2\), \(-5x\), and \(7\), giving exactly 3 terms." + "\n" +
        r"Step 3: A polynomial having three non-zero terms is classified as a trinomial."
    ),
    # 12
    (
        r"What is the degree of the polynomial \(2a^2 b^3 c - 7a^4 b c^2 + a b^2 c^3\)?",
        [make_opt(r"\(6\)", False), make_opt(r"\(7\)", True), make_opt(r"\(8\)", False), make_opt(r"\(5\)", False)],
        r"Step 1: Sum degrees in each term:" + "\n" +
        r"Term 1: \(2a^2 b^3 c \rightarrow 2 + 3 + 1 = 6\)." + "\n" +
        r"Term 2: \(-7a^4 b c^2 \rightarrow 4 + 1 + 2 = 7\)." + "\n" +
        r"Term 3: \(a b^2 c^3 \rightarrow 1 + 2 + 3 = 6\)." + "\n" +
        r"Step 2: The maximum sum is 7." + "\n" +
        r"Step 3: The degree of the polynomial is \(7\)."
    ),
    # 13
    (
        r"Which of the following is a cubic polynomial in one variable?",
        [make_opt(r"\(x^3 + y^3 + z^3\)", False), make_opt(r"\(4x^3 - 2x^2 + 7x - 1\)", True), make_opt(r"\(3x^2 - x + 5\)", False), make_opt(r"\(x^4 - 1\)", False)],
        r"Step 1: A cubic polynomial has degree 3." + "\n" +
        r"Step 2: 'In one variable' means only a single variable (such as \(x\)) is present." + "\n" +
        r"Step 3: \(4x^3 - 2x^2 + 7x - 1\) has single variable \(x\) and highest power 3, making it a cubic polynomial in one variable."
    ),
    # 14
    (
        r"Find the degree of the polynomial \((y^2 + 3)(y^3 - y + 4)\).",
        [make_opt(r"\(6\)", False), make_opt(r"\(5\)", True), make_opt(r"\(4\)", False), make_opt(r"\(3\)", False)],
        r"Step 1: Leading term of \((y^2 + 3)\) is \(y^2\) (degree 2)." + "\n" +
        r"Step 2: Leading term of \((y^3 - y + 4)\) is \(y^3\) (degree 3)." + "\n" +
        r"Step 3: Highest degree term in product is \(y^2 \times y^3 = y^5\). So the degree is \(5\)."
    ),
    # 15
    (
        r"If \(p(x) = x^4 - 2x^3 + 5\) and \(q(x) = -x^4 + 3x^2 - 8\), what is the degree of \(p(x) + q(x)\)?",
        [make_opt(r"\(4\)", False), make_opt(r"\(3\)", True), make_opt(r"\(2\)", False), make_opt(r"\(7\)", False)],
        r"Step 1: Write \(p(x) + q(x) = (x^4 - 2x^3 + 5) + (-x^4 + 3x^2 - 8)\)." + "\n" +
        r"Step 2: The \(x^4\) terms cancel: \(x^4 - x^4 = 0\)." + "\n" +
        r"Step 3: The resulting polynomial is \(-2x^3 + 3x^2 - 3\), whose highest power is \(3\). So degree is \(3\)."
    ),
    # 16
    (
        r"What is the degree of the polynomial \(9\)?",
        [make_opt(r"\(1\)", False), make_opt(r"\(0\)", True), make_opt(r"\(9\)", False), make_opt(r"Undefined", False)],
        r"Step 1: 9 is a non-zero real number (constant)." + "\n" +
        r"Step 2: We can write \(9 = 9x^0\)." + "\n" +
        r"Step 3: The exponent of the variable is 0, so the degree is \(0\)."
    ),
    # 17
    (
        r"Assertion (A): The degree of the polynomial \(x^2 y^3 z + 4xyz^2\) is 6." + "\n" +
        r"Reason (R): The degree of a polynomial in more than one variable is the maximum sum of powers of the variables in any term.",
        [make_opt(r"Both A and R are true and R is the correct explanation of A", True),
         make_opt(r"Both A and R are true but R is not the correct explanation of A", False),
         make_opt(r"A is true but R is false", False),
         make_opt(r"A is false but R is true", False)],
        r"Step 1: Check term degrees: \(x^2 y^3 z \rightarrow 2 + 3 + 1 = 6\); \(4xyz^2 \rightarrow 1 + 1 + 2 = 4\)." + "\n" +
        r"Step 2: Maximum sum is 6, so degree is 6. Assertion A is true." + "\n" +
        r"Step 3: Reason R defines the degree of a multivariable polynomial correctly and explains A."
    ),
    # 18
    (
        r"Which term in the polynomial \(6u^3 v^2 - 4u^4 v + 7u^2 v^4 - u v\) has the highest degree?",
        [make_opt(r"\(6u^3 v^2\)", False), make_opt(r"\(-4u^4 v\)", False), make_opt(r"\(7u^2 v^4\)", True), make_opt(r"\(-uv\)", False)],
        r"Step 1: Calculate power sums: \(6u^3v^2 \rightarrow 3+2=5\); \(-4u^4v \rightarrow 4+1=5\); \(7u^2v^4 \rightarrow 2+4=6\); \(-uv \rightarrow 1+1=2\)." + "\n" +
        r"Step 2: The term \(7u^2v^4\) has degree \(6\), which is highest." + "\n" +
        r"Step 3: Thus, the term with the highest degree is \(7u^2 v^4\)."
    ),
    # 19
    (
        r"What is the degree of \((x^2 + 1)^3\)?",
        [make_opt(r"\(5\)", False), make_opt(r"\(6\)", True), make_opt(r"\(3\)", False), make_opt(r"\(8\)", False)],
        r"Step 1: Using binomial expansion, \((x^2 + 1)^3 = (x^2)^3 + 3(x^2)^2(1) + 3(x^2)(1)^2 + 1^3\)." + "\n" +
        r"Step 2: The leading term is \((x^2)^3 = x^{2 \times 3} = x^6\)." + "\n" +
        r"Step 3: Therefore, the degree of \((x^2 + 1)^3\) is \(6\)."
    ),
    # 20
    (
        r"If \(\deg(P) = m\) and \(\deg(Q) = n\) with \(m > n\), what is \(\deg(P - Q)\)?",
        [make_opt(r"\(m - n\)", False), make_opt(r"\(m\)", True), make_opt(r"\(n\)", False), make_opt(r"\(m + n\)", False)],
        r"Step 1: The highest power in \(P(x)\) is \(m\) and in \(Q(x)\) is \(n\)." + "\n" +
        r"Step 2: Since \(m > n\), the term of power \(m\) in \(P(x)\) cannot be cancelled by subtracting \(Q(x)\)." + "\n" +
        r"Step 3: Hence, the highest power of the difference remains \(m\), so \(\deg(P - Q) = m\)."
    )
]

for idx, (txt, opts, sol) in enumerate(exam_data_311):
    q_code = f"MH-9-MTH1-3-3.1.1-OSC-{101 + idx:03d}"
    questions.append(make_q(q_code, txt, opts, sol, t_code, t_name, "exam", "medium" if idx % 2 == 0 else "hard"))

# 20 Foundation (Seq 151 to 170)
found_data_311 = [
    # 1
    (
        r"What is the degree of the polynomial \(7x\)?",
        [make_opt(r"\(0\)", False), make_opt(r"\(1\)", True), make_opt(r"\(7\)", False), make_opt(r"Not defined", False)],
        r"Step 1: In the expression \(7x\), the variable is \(x\)." + "\n" +
        r"Step 2: The exponent of \(x\) is 1 since \(x = x^1\)." + "\n" +
        r"Step 3: Therefore, the degree of \(7x\) is \(1\)."
    ),
    # 2
    (
        r"What is the degree of the polynomial \(x^2 - 4x + 4\)?",
        [make_opt(r"\(1\)", False), make_opt(r"\(2\)", True), make_opt(r"\(4\)", False), make_opt(r"\(0\)", False)],
        r"Step 1: Identify all exponents of \(x\): 2, 1, and 0." + "\n" +
        r"Step 2: The highest exponent is 2." + "\n" +
        r"Step 3: Hence, the degree is \(2\)."
    ),
    # 3
    (
        r"What is the degree of the polynomial \(5y^3\)?",
        [make_opt(r"\(3\)", True), make_opt(r"\(5\)", False), make_opt(r"\(1\)", False), make_opt(r"\(0\)", False)],
        r"Step 1: The variable is \(y\) and its exponent is 3." + "\n" +
        r"Step 2: Since this is a monomial, the degree is simply the power of the variable." + "\n" +
        r"Step 3: The degree is \(3\)."
    ),
    # 4
    (
        r"Which of the following is a monomial?",
        [make_opt(r"\(2x + 1\)", False), make_opt(r"\(5x^3\)", True), make_opt(r"\(x^2 - 3x + 2\)", False), make_opt(r"\(x^4 + x\)", False)],
        r"Step 1: A monomial is a polynomial having only one term." + "\n" +
        r"Step 2: \(5x^3\) consists of a single term." + "\n" +
        r"Step 3: Thus, \(5x^3\) is a monomial."
    ),
    # 5
    (
        r"Which of the following is a binomial?",
        [make_opt(r"\(3y\)", False), make_opt(r"\(y^2 - 9\)", True), make_opt(r"\(y^3 + 2y - 1\)", False), make_opt(r"\(7\)", False)],
        r"Step 1: A binomial is a polynomial consisting of exactly two non-zero terms." + "\n" +
        r"Step 2: \(y^2 - 9\) has two terms: \(y^2\) and \(-9\)." + "\n" +
        r"Step 3: Hence, \(y^2 - 9\) is a binomial."
    ),
    # 6
    (
        r"What is the coefficient of \(x^2\) in the polynomial \(4x^3 - 7x^2 + 2x - 5\)?",
        [make_opt(r"\(4\)", False), make_opt(r"\(-7\)", True), make_opt(r"\(7\)", False), make_opt(r"\(2\)", False)],
        r"Step 1: Locate the term containing \(x^2\)." + "\n" +
        r"Step 2: The term is \(-7x^2\)." + "\n" +
        r"Step 3: The coefficient is the constant factor multiplying \(x^2\), which is \(-7\)."
    ),
    # 7
    (
        r"What is the degree of the constant polynomial \(100\)?",
        [make_opt(r"\(100\)", False), make_opt(r"\(1\)", False), make_opt(r"\(0\)", True), make_opt(r"Undefined", False)],
        r"Step 1: Any non-zero constant number can be written as \(c \cdot x^0\)." + "\n" +
        r"Step 2: Here, \(100 = 100x^0\)." + "\n" +
        r"Step 3: The power of \(x\) is 0, so the degree is \(0\)."
    ),
    # 8
    (
        r"In the monomial \(8x y\), what is the degree?",
        [make_opt(r"\(1\)", False), make_opt(r"\(2\)", True), make_opt(r"\(8\)", False), make_opt(r"\(0\)", False)],
        r"Step 1: The monomial has two variables: \(x\) and \(y\)." + "\n" +
        r"Step 2: The exponent of \(x\) is 1 and the exponent of \(y\) is 1." + "\n" +
        r"Step 3: The degree is the sum of exponents: \(1 + 1 = 2\)."
    ),
    # 9
    (
        r"What is the constant term in the polynomial \(3x^2 - 4x + 8\)?",
        [make_opt(r"\(3\)", False), make_opt(r"\(-4\)", False), make_opt(r"\(8\)", True), make_opt(r"\(0\)", False)],
        r"Step 1: A constant term is the term that does not contain any variable (or contains variable with power 0)." + "\n" +
        r"Step 2: In \(3x^2 - 4x + 8\), the term independent of \(x\) is 8." + "\n" +
        r"Step 3: Therefore, the constant term is \(8\)."
    ),
    # 10
    (
        r"What is the degree of \(x^5\)?",
        [make_opt(r"\(5\)", True), make_opt(r"\(1\)", False), make_opt(r"\(0\)", False), make_opt(r"\(25\)", False)],
        r"Step 1: The variable is \(x\)." + "\n" +
        r"Step 2: The power of \(x\) is 5." + "\n" +
        r"Step 3: Therefore, the degree of the polynomial is \(5\)."
    ),
    # 11
    (
        r"Which of the following polynomials is a linear polynomial?",
        [make_opt(r"\(5x^2 - 1\)", False), make_opt(r"\(3x + 7\)", True), make_opt(r"\(x^3\)", False), make_opt(r"\(9\)", False)],
        r"Step 1: A linear polynomial is a polynomial of degree 1." + "\n" +
        r"Step 2: In \(3x + 7\), the highest power of \(x\) is 1." + "\n" +
        r"Step 3: Hence, \(3x + 7\) is a linear polynomial."
    ),
    # 12
    (
        r"Which of the following polynomials is a quadratic polynomial?",
        [make_opt(r"\(4x + 3\)", False), make_opt(r"\(2x^2 + 5x - 1\)", True), make_opt(r"\(x^3 - 8\)", False), make_opt(r"\(6\)", False)],
        r"Step 1: A quadratic polynomial is a polynomial of degree 2." + "\n" +
        r"Step 2: In \(2x^2 + 5x - 1\), the highest power of \(x\) is 2." + "\n" +
        r"Step 3: Thus, \(2x^2 + 5x - 1\) is a quadratic polynomial."
    ),
    # 13
    (
        r"State whether the expression \(\sqrt{3}x^2 + 5x - 2\) is a polynomial.",
        [make_opt(r"Yes, it is a polynomial", True), make_opt(r"No, because the coefficient is a surd", False), make_opt(r"No, because of negative sign", False), make_opt(r"Cannot be determined", False)],
        r"Step 1: Check the exponents of the variable \(x\): powers are 2 and 1, both non-negative integers." + "\n" +
        r"Step 2: The coefficients are \(\sqrt{3}, 5, -2\), all real numbers." + "\n" +
        r"Step 3: Real coefficients with whole number powers define a valid polynomial. So yes, it is a polynomial."
    ),
    # 14
    (
        r"What is the degree of the polynomial \(2x^3 y\)?",
        [make_opt(r"\(3\)", False), make_opt(r"\(4\)", True), make_opt(r"\(1\)", False), make_opt(r"\(2\)", False)],
        r"Step 1: Power of \(x\) is 3; power of \(y\) is 1." + "\n" +
        r"Step 2: Sum of powers in the monomial is \(3 + 1 = 4\)." + "\n" +
        r"Step 3: Therefore, the degree is \(4\)."
    ),
    # 15
    (
        r"What is the degree of the polynomial \(m^3 + 3m^5 + 1\)?",
        [make_opt(r"\(3\)", False), make_opt(r"\(5\)", True), make_opt(r"\(8\)", False), make_opt(r"\(1\)", False)],
        r"Step 1: The terms are \(m^3\) (power 3), \(3m^5\) (power 5), and \(1\) (power 0)." + "\n" +
        r"Step 2: The greatest power of variable \(m\) is 5." + "\n" +
        r"Step 3: Therefore, the degree of the polynomial is \(5\)."
    ),
    # 16
    (
        r"In the polynomial \(x^4 - 3x^2 + 7x\), what is the coefficient of \(x^3\)?",
        [make_opt(r"\(1\)", False), make_opt(r"\(0\)", True), make_opt(r"\(-3\)", False), make_opt(r"\(7\)", False)],
        r"Step 1: The term \(x^3\) does not appear explicitly in the given polynomial." + "\n" +
        r"Step 2: We can write the polynomial in index form with missing terms: \(x^4 + 0x^3 - 3x^2 + 7x + 0\)." + "\n" +
        r"Step 3: The coefficient of \(x^3\) is \(0\)."
    ),
    # 17
    (
        r"What is the degree of the polynomial \(a b + c\)?",
        [make_opt(r"\(1\)", False), make_opt(r"\(2\)", True), make_opt(r"\(3\)", False), make_opt(r"\(0\)", False)],
        r"Step 1: Term \(ab\) has degree \(1 + 1 = 2\)." + "\n" +
        r"Step 2: Term \(c\) has degree \(1\)." + "\n" +
        r"Step 3: The highest degree among the terms is 2, so the degree is \(2\)."
    ),
    # 18
    (
        r"Is the expression \(\frac{1}{y} + 2\) a polynomial?",
        [make_opt(r"Yes, it is linear", False), make_opt(r"No, the power of variable is \(-1\)", True), make_opt(r"Yes, with degree 0", False), make_opt(r"Cannot be decided", False)],
        r"Step 1: Express \(\frac{1}{y}\) with an exponent: \(\frac{1}{y} = y^{-1}\)." + "\n" +
        r"Step 2: The exponent is \(-1\), which is not a whole number (non-negative integer)." + "\n" +
        r"Step 3: Hence, \(\frac{1}{y} + 2\) is not a polynomial."
    ),
    # 19
    (
        r"What is the coefficient of \(x\) in \(-x + 9\)?",
        [make_opt(r"\(1\)", False), make_opt(r"\(-1\)", True), make_opt(r"\(9\)", False), make_opt(r"\(0\)", False)],
        r"Step 1: The term containing \(x\) is \(-x\)." + "\n" +
        r"Step 2: This can be written as \((-1) \cdot x\)." + "\n" +
        r"Step 3: Thus, the coefficient of \(x\) is \(-1\)."
    ),
    # 20
    (
        r"What is the degree of the polynomial \(p^2 q^2 - 3p q^3\)?",
        [make_opt(r"\(2\)", False), make_opt(r"\(3\)", False), make_opt(r"\(4\)", True), make_opt(r"\(5\)", False)],
        r"Step 1: Degree of \(p^2 q^2\) is \(2 + 2 = 4\)." + "\n" +
        r"Step 2: Degree of \(-3p q^3\) is \(1 + 3 = 4\)." + "\n" +
        r"Step 3: Both terms have degree 4, so the degree of the polynomial is \(4\)."
    )
]

for idx, (txt, opts, sol) in enumerate(found_data_311):
    q_code = f"MH-9-MTH1-3-3.1.1-OSC-{151 + idx:03d}"
    questions.append(make_q(q_code, txt, opts, sol, t_code, t_name, "foundation", "easy"))

print(f"Added Topic 3.1.1: {len(questions)} questions")

# Save as test check
with open("scripts/mh9_mth1_ch3_part1_test.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)
