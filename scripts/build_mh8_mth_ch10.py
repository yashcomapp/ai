import json
import random

random.seed(81010)

def build_ch10_questions():
    questions = []
    start_seq = 300

    def make_q(topic_code, subtopic_name, text, correct, wrongs, step1, step2, step3, diff="medium", vault="exam"):
        nonlocal start_seq
        opts_text = [correct]
        used = {correct.strip().lower()}
        for w in wrongs:
            w_clean = w.strip().lower()
            if w_clean not in used:
                opts_text.append(w)
                used.add(w_clean)
        
        cand_offset = 1
        while len(opts_text) < 4:
            cand = f"\\({cand_offset}\\)"
            if cand.lower() not in used:
                opts_text.append(cand)
                used.add(cand.lower())
            cand_offset += 1
        opts_text = opts_text[:4]

        indices = list(range(4))
        random.shuffle(indices)
        shuffled_opts = [opts_text[i] for i in indices]
        correct_idx = shuffled_opts.index(correct)
        opt_letters = ["A", "B", "C", "D"]
        correct_letter = opt_letters[correct_idx]

        options = [
            {"id": opt_letters[i], "text": shuffled_opts[i], "isCorrect": (i == correct_idx)}
            for i in range(4)
        ]

        solution = f"**Step 1:** {step1}\n**Step 2:** {step2}\n**Step 3:** {step3}"
        q_code = f"{topic_code}-OSC-{start_seq}"
        start_seq += 1

        return {
            "questionCode": q_code,
            "text": text,
            "options": options,
            "correctAnswer": correct_letter,
            "solution": solution,
            "difficulty": diff,
            "topicCode": topic_code,
            "subtopic": subtopic_name,
            "vault": vault,
            "type": "OSC",
            "marks": 4,
            "bloomsTaxonomy": "apply" if diff == "hard" else "understand",
            "estimatedTime": 90 if diff == "hard" else 60
        }

    vaults = ["exam"] * 40 + ["practice"] * 20 + ["foundation"] * 20
    diffs = (["easy"] * 15 + ["medium"] * 15 + ["hard"] * 10) + (["easy"] * 6 + ["medium"] * 8 + ["hard"] * 6) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)

    # -------------------------------------------------------------
    # 10.1.1 Definition of polynomial in one variable (80 questions)
    # -------------------------------------------------------------
    tc_1011 = "MH-8-MTH-10-10.1.1"
    name_1011 = "Definition of polynomial in one variable"
    poly_checks = [
        ("\\(3x^2 + 5x - 7\\)", "Yes, it is a polynomial because all exponents of x are whole numbers", ["No, because it has three terms", "No, because the constant term is negative", "No, because degree is 2"]),
        ("\\(x^2 + \\frac{1}{x}\\)", "No, it is not a polynomial because \\(\\frac{1}{x} = x^{-1}\\) has a negative exponent", ["Yes, it is a rational polynomial", "Yes, because the highest power is 2", "Yes, all algebraic expressions are polynomials"]),
        ("\\(4y^3 - 2\\sqrt{y} + 1\\)", "No, it is not a polynomial because \\(\\sqrt{y} = y^{1/2}\\) has a fractional exponent", ["Yes, it is a cubic polynomial", "Yes, radicals do not affect polynomials", "Yes, if y is positive"]),
        ("\\(5m^4 - 3m^2 + 8\\)", "Yes, it is a polynomial because all exponents of m are non-negative integers", ["No, because power of m is even", "No, because there is no m term", "No, because 8 has no variable"]),
        ("\\(7p^5 + 4p^3 - p + 12\\)", "Yes, it is a polynomial in one variable p", ["No, it has four terms", "No, it is an equation not an expression", "No, 12 is too large"]),
        ("\\(\\frac{3}{x^2} + 2x - 5\\)", "No, it is not a polynomial because x has a negative power \\(x^{-2}\\)", ["Yes, because degree is 2", "Yes, it is a quadratic fraction", "Yes, all fractions are polynomials"]),
        ("\\(6z^3 + 2z^2 - \\sqrt{3}z + 9\\)", "Yes, it is a polynomial because the variable exponents are whole numbers", ["No, because \\(\\sqrt{3}\\) is irrational", "No, coefficients must be integers", "No, because degree is 3"]),
        ("\\(x^{3/2} + 4x + 1\\)", "No, it is not a polynomial because \\(3/2\\) is not a whole number", ["Yes, because 3/2 is greater than 1", "Yes, it is a fractional polynomial", "Yes, because it is in one variable"])
    ]
    for i in range(80):
        expr, ans, wrongs = poly_checks[i % len(poly_checks)]
        q = make_q(
            tc_1011, name_1011,
            f"Determine whether the algebraic expression {expr} is a polynomial in one variable.",
            ans, wrongs,
            "Recall the definition of a polynomial: an algebraic expression where the exponent of every variable term is a non-negative integer (whole number: 0, 1, 2, 3, ...).",
            "Examine each power of the variable in the given expression.",
            f"Based on the exponents, {ans}.",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 10.1.2 Degree of monomial and polynomial (80 questions)
    # -------------------------------------------------------------
    tc_1012 = "MH-8-MTH-10-10.1.2"
    name_1012 = "Degree of monomial and polynomial"
    degrees_1012 = [
        ("7x^5 - 3x^2 + 4", 5), ("4y^7 + 2y^3 - y + 1", 7), ("3x^2 - 8x + 9", 2),
        ("5m^8 + m^4 - 2m", 8), ("12p^3 + 6p^2 - 5", 3), ("9x^4 - 2x^6 + 3x - 1", 6),
        ("15", 0), ("8x", 1), ("2y^9 - 4y^5 + y^2", 9), ("6z^10 - 3z^7 + 2", 10),
        ("4a^3 - a^4 + 7", 4), ("100m^2 + 50m", 2), ("x^6 + 3x^5 - x^3", 6),
        ("18", 0), ("7y", 1), ("3x^5 - 4x^3 + 2x^2", 5)
    ]
    for i in range(80):
        poly_str, deg = degrees_1012[i % len(degrees_1012)]
        ans = f"\\({deg}\\)"
        w1 = f"\\({deg + 1}\\)"
        w2 = f"\\({max(0, deg - 1)}\\)"
        w3 = f"\\({deg + 2}\\)"
        
        q = make_q(
            tc_1012, name_1012,
            f"Find the degree of the polynomial: \\({poly_str}\\).",
            ans, [w1, w2, w3],
            "The degree of a polynomial in one variable is the highest exponent (power) of the variable in the non-zero terms.",
            f"Identify the power of each term in \\({poly_str}\\). The maximum exponent is \\({deg}\\).",
            f"Hence, the degree of the polynomial is \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 10.2.1 Exponent subtraction in variable division (80 questions)
    # -------------------------------------------------------------
    tc_1021 = "MH-8-MTH-10-10.2.1"
    name_1021 = "Exponent subtraction in variable division"
    exp_divs = [
        ("x^7", "x^3", "x^4"), ("y^9", "y^4", "y^5"), ("m^8", "m^2", "m^6"),
        ("a^10", "a^5", "a^5"), ("p^6", "p^2", "p^4"), ("z^12", "z^7", "z^5"),
        ("x^5", "x^4", "x"), ("y^8", "y^3", "y^5"), ("m^11", "m^6", "m^5"),
        ("a^9", "a^3", "a^6"), ("p^7", "p^5", "p^2"), ("z^8", "z^6", "z^2")
    ]
    for i in range(80):
        num, den, res = exp_divs[i % len(exp_divs)]
        ans = f"\\({res}\\)"
        w1 = f"\\({res}^2\\)"
        w2 = f"\\(\\frac{{1}}{{{res}}}\\)"
        w3 = f"\\({num}{den}\\)"
        
        q = make_q(
            tc_1021, name_1021,
            f"Divide the variable terms using the laws of exponents: \\(\\frac{{{num}}}{{{den}}}\\).",
            ans, [w1, w2, w3],
            "Recall the quotient rule for exponents with the same base: \\(\\frac{a^m}{a^n} = a^{m-n}\\).",
            f"Subtract the exponent of the denominator from the exponent of the numerator.",
            f"This gives \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 10.2.2 Coefficient division (80 questions)
    # -------------------------------------------------------------
    tc_1022 = "MH-8-MTH-10-10.2.2"
    name_1022 = "Coefficient division"
    monomial_divs = [
        ("15x^5", "3x^2", "5x^3"), ("24y^6", "6y^2", "4y^4"), ("36m^4", "9m", "4m^3"),
        ("40a^7", "5a^3", "8a^4"), ("48p^8", "8p^5", "6p^3"), ("56z^6", "7z^4", "8z^2"),
        ("-20x^4", "4x^2", "-5x^2"), ("-35y^5", "-7y^2", "5y^3"), ("42m^6", "-6m^3", "-7m^3"),
        ("-64a^7", "-8a^4", "8a^3"), ("60p^5", "12p^2", "5p^3"), ("72z^9", "9z^6", "8z^3"),
        ("18x^3", "6x", "3x^2"), ("-50y^4", "10y", "-5y^3"), ("81m^5", "9m^2", "9m^3"),
        ("100a^6", "25a^4", "4a^2")
    ]
    for i in range(80):
        num, den, res = monomial_divs[i % len(monomial_divs)]
        ans = f"\\({res}\\)"
        w1 = f"\\({res.replace('-', '')}\\)" if '-' in res else f"\\(-{res}\\)"
        w2 = f"\\({res}^2\\)"
        w3 = f"\\(2{res}\\)"
        
        q = make_q(
            tc_1022, name_1022,
            f"Divide the monomial \\({num}\\) by the monomial \\({den}\\).",
            ans, [w1, w2, w3],
            "Divide the numerical coefficients first, and then apply the exponent subtraction law on the variable part.",
            f"Coefficient division: divide the numerator's coefficient by the denominator's coefficient.",
            f"Combining the divided coefficient with the reduced variable exponent produces \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 10.3.1 Long division algorithm for polynomials (80 questions)
    # -------------------------------------------------------------
    tc_1031 = "MH-8-MTH-10-10.3.1"
    name_1031 = "Long division algorithm for polynomials"
    long_divs = [
        ("(x^2 + 5x + 6) \\div (x + 2)", "\\text{Quotient} = x + 3, \\text{Remainder} = 0", ["\\text{Quotient} = x - 3, \\text{Remainder} = 0", "\\text{Quotient} = x + 2, \\text{Remainder} = 1", "\\text{Quotient} = x + 1, \\text{Remainder} = 2"]),
        ("(x^2 + 7x + 12) \\div (x + 3)", "\\text{Quotient} = x + 4, \\text{Remainder} = 0", ["\\text{Quotient} = x - 4, \\text{Remainder} = 0", "\\text{Quotient} = x + 3, \\text{Remainder} = 1", "\\text{Quotient} = x + 2, \\text{Remainder} = 0"]),
        ("(x^2 + 4x + 5) \\div (x + 1)", "\\text{Quotient} = x + 3, \\text{Remainder} = 2", ["\\text{Quotient} = x + 3, \\text{Remainder} = 0", "\\text{Quotient} = x + 4, \\text{Remainder} = 1", "\\text{Quotient} = x + 2, \\text{Remainder} = 3"]),
        ("(2x^2 + 5x + 3) \\div (x + 1)", "\\text{Quotient} = 2x + 3, \\text{Remainder} = 0", ["\\text{Quotient} = 2x - 3, \\text{Remainder} = 0", "\\text{Quotient} = x + 3, \\text{Remainder} = 0", "\\text{Quotient} = 2x + 1, \\text{Remainder} = 2"]),
        ("(3x^2 + 10x + 8) \\div (x + 2)", "\\text{Quotient} = 3x + 4, \\text{Remainder} = 0", ["\\text{Quotient} = 3x - 4, \\text{Remainder} = 0", "\\text{Quotient} = 3x + 2, \\text{Remainder} = 0", "\\text{Quotient} = x + 4, \\text{Remainder} = 1"]),
        ("(x^2 - 5x + 6) \\div (x - 2)", "\\text{Quotient} = x - 3, \\text{Remainder} = 0", ["\\text{Quotient} = x + 3, \\text{Remainder} = 0", "\\text{Quotient} = x - 2, \\text{Remainder} = 1", "\\text{Quotient} = x - 1, \\text{Remainder} = 0"]),
        ("(x^3 + 1) \\div (x + 1)", "\\text{Quotient} = x^2 - x + 1, \\text{Remainder} = 0", ["\\text{Quotient} = x^2 + x + 1, \\text{Remainder} = 0", "\\text{Quotient} = x^2 - 1, \\text{Remainder} = 0", "\\text{Quotient} = x^2 + 1, \\text{Remainder} = 0"]),
        ("(x^3 - 8) \\div (x - 2)", "\\text{Quotient} = x^2 + 2x + 4, \\text{Remainder} = 0", ["\\text{Quotient} = x^2 - 2x + 4, \\text{Remainder} = 0", "\\text{Quotient} = x^2 - 4, \\text{Remainder} = 0", "\\text{Quotient} = x^2 + 4, \\text{Remainder} = 0"])
    ]
    for i in range(80):
        prob, ans, wrongs = long_divs[i % len(long_divs)]
        q = make_q(
            tc_1031, name_1031,
            f"Divide using the polynomial long division method: \\({prob}\\).",
            f"\\({ans}\\)", [f"\\({w}\\)" for w in wrongs],
            "Arrange both dividend and divisor in descending powers of the variable.",
            "Divide the first term of the dividend by the first term of the divisor to get each term of the quotient, then multiply and subtract.",
            f"Repeat until the degree of the remainder is strictly less than the degree of the divisor: \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 10.3.2 Dividend = Divisor * Quotient + Remainder (80 questions)
    # -------------------------------------------------------------
    tc_1032 = "MH-8-MTH-10-10.3.2"
    name_1032 = "Dividend = Divisor * Quotient + Remainder"
    rel_checks = [
        ("What fundamental division identity connects the dividend \\(P(x)\\), divisor \\(D(x)\\), quotient \\(Q(x)\\), and remainder \\(R(x)\\)?", "\\(P(x) = D(x) \\times Q(x) + R(x)\\)", ["\\(P(x) = D(x) + Q(x) \\times R(x)\\)", "\\(P(x) = D(x) \\times Q(x) - R(x)\\)", "\\(P(x) = \\frac{D(x)}{Q(x)} + R(x)\\)"]),
        ("In the polynomial division algorithm, what is the required condition on the degree of the remainder \\(R(x)\\)?", "\\(\\text{degree of } R(x) < \\text{degree of } D(x)\\text{ (or } R(x) = 0\\text{)}\\)", ["\\(\\text{degree of } R(x) = \\text{degree of } D(x)\\)", "\\(\\text{degree of } R(x) > \\text{degree of } D(x)\\)", "\\(\\text{degree of } R(x) = 0\\text{ always}\\)"]),
        ("If \\(D(x) = x + 3\\), \\(Q(x) = x + 4\\), and \\(R(x) = 0\\), find the dividend \\(P(x)\\).", "\\(x^2 + 7x + 12\\)", ["\\(x^2 + 12\\)", "\\(x^2 + 7x - 12\\)", "\\(2x + 7\\)"]),
        ("If \\(D(x) = x - 2\\), \\(Q(x) = x + 5\\), and \\(R(x) = 3\\), find the dividend \\(P(x)\\).", "\\(x^2 + 3x - 7\\)", ["\\(x^2 + 3x - 10\\)", "\\(x^2 + 3x + 3\\)", "\\(x^2 - 10\\)"])
    ]
    for i in range(80):
        ctx, ans, wrongs = rel_checks[i % len(rel_checks)]
        q = make_q(
            tc_1032, name_1032,
            f"In polynomial algebra: {ctx}",
            ans if ans.startswith("\\(") else f"\\({ans}\\)",
            [w if w.startswith("\\(") else f"\\({w}\\)" for w in wrongs],
            "Recall the Euclidean division algorithm for polynomials.",
            "The dividend equals the product of divisor and quotient plus the remainder: Dividend = Divisor × Quotient + Remainder.",
            f"Therefore, the relationship is {ans}.",
            diffs[i], vaults[i]
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch10_questions()
    print(f"Generated {len(qs)} questions for Chapter 10.")
    out_path = "scripts/mh8_mth_ch10_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
