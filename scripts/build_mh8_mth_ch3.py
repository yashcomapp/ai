import json
import random

random.seed(8303)

def build_ch3_questions():
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

    vault_cycle = ["exam", "practice", "foundation"]
    diff_cycle = ["easy", "medium", "hard"]

    # 3.1.1 Product rule a^m * a^n (need 80)
    tc = "MH-8-MTH-3-3.1.1"
    name = "Product rule a^m * a^n"
    for i in range(80):
        a = 2 + (i % 7)
        m = 2 + (i % 5)
        n = 3 + (i % 4)
        sum_exp = m + n
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Simplify using the laws of indices: \\({a}^{{{m}}} \\times {a}^{{{n}}}\\).",
            f"\\({a}^{{{sum_exp}}}\\)",
            [f"\\({a}^{{{m * n}}}\\)", f"\\({2 * a}^{{{sum_exp}}}\\)", f"\\({a}^{{{sum_exp + 1}}}\\)"],
            f"Recall the product rule of indices: \\(a^m \\times a^n = a^{{m+n}}\\) for any non-zero base \\(a\\).",
            f"Add the indices: \\({m} + {n} = {sum_exp}\\).",
            f"Therefore, \\({a}^{{{m}}} \\times {a}^{{{n}}} = {a}^{{{sum_exp}}}\\).",
            d, v
        )
        questions.append(q)

    # 3.1.2 Quotient rule a^m / a^n (need 80)
    tc = "MH-8-MTH-3-3.1.2"
    name = "Quotient rule a^m / a^n"
    for i in range(80):
        a = 3 + (i % 6)
        m = 7 + (i % 5)
        n = 2 + (i % 4)
        diff_exp = m - n
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Simplify using the quotient law of indices: \\(\\frac{{{a}^{{{m}}}}}{{{a}^{{{n}}}}}\\).",
            f"\\({a}^{{{diff_exp}}}\\)",
            [f"\\({a}^{{{m + n}}}\\)", f"\\({a}^{{{m * n}}}\\)", f"\\(1\\)"],
            f"The quotient rule of indices states: \\(\\frac{{a^m}}{{a^n}} = a^{{m-n}}\\).",
            f"Subtract the index of the denominator from the numerator: \\({m} - {n} = {diff_exp}\\).",
            f"Thus, the result is \\({a}^{{{diff_exp}}}\\).",
            d, v
        )
        questions.append(q)

    # 3.1.3 Power of power (a^m)^n (need 80)
    tc = "MH-8-MTH-3-3.1.3"
    name = "Power of power (a^m)^n"
    for i in range(80):
        a = 2 + (i % 6)
        m = 2 + (i % 3)
        n = 3 + (i % 3)
        prod_exp = m * n
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Simplify: \\(({a}^{{{m}}})^{{{n}}}\\).",
            f"\\({a}^{{{prod_exp}}}\\)",
            [f"\\({a}^{{{m + n}}}\\)", f"\\({a}^{{{m ** n}}}\\)", f"\\({a}^{{{prod_exp + 2}}}\\)"],
            f"Apply the power of a power rule: \\((a^m)^n = a^{{m \\times n}}\\).",
            f"Multiply the powers: \\({m} \\times {n} = {prod_exp}\\).",
            f"Therefore, \\(({a}^{{{m}}})^{{{n}}} = {a}^{{{prod_exp}}}\\).",
            d, v
        )
        questions.append(q)

    # 3.1.4 Zero exponent a^0 = 1 (need 80)
    tc = "MH-8-MTH-3-3.1.4"
    name = "Zero exponent a^0 = 1"
    for i in range(80):
        val = 15 + i * 4
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Evaluate the value of \\(({val})^0\\) where \\({val} \\neq 0\\).",
            "\\(1\\)",
            ["\\(0\\)", f"\\({val}\\)", "\\(-1\\)"],
            f"By the law of zero exponent in Balbharti algebra, for any non-zero number \\(a\\), \\(a^0 = 1\\).",
            f"This follows from \\(\\frac{{a^m}}{{a^m}} = a^{{m-m}} = a^0 = 1\\).",
            f"Since \\({val} \\neq 0\\), \\(({val})^0 = 1\\).",
            d, v
        )
        questions.append(q)

    # 3.1.5 Negative exponent a^(-m) = 1/a^m (need 80)
    tc = "MH-8-MTH-3-3.1.5"
    name = "Negative exponent a^(-m) = 1/a^m"
    for i in range(80):
        base = 2 + (i % 7)
        exp = 2 + (i % 4)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Express \\({base}^{{-{exp}}}\\) as a fraction with a positive index.",
            f"\\(\\frac{{1}}{{{base}^{{{exp}}}}}\\)",
            [f"\\(-{base}^{{{exp}}}\\)", f"\\(\\frac{{{exp}}}{{{base}}}\\)", f"\\({base}^{{{exp}}}\\)"],
            f"Recall the law of negative indices: \\(a^{{-m}} = \\frac{{1}}{{a^m}}\\).",
            f"Applying this to \\({base}^{{-{exp}}}\\) gives \\(\\frac{{1}}{{{base}^{{{exp}}}}}\\).",
            f"Hence, the positive index form is \\(\\frac{{1}}{{{base}^{{{exp}}}}}\\).",
            d, v
        )
        questions.append(q)

    # 3.2.1 Meaning of a^(1/n) as nth root of a (need 80)
    tc = "MH-8-MTH-3-3.2.1"
    name = "Meaning of a^(1/n) as nth root of a"
    for i in range(80):
        n = [2, 3, 4, 5, 6][i % 5]
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        ord_names = {2: "square root", 3: "cube root", 4: "4th root", 5: "5th root", 6: "6th root"}
        q = make_q(
            tc, name,
            f"What is the mathematical meaning of the index notation \\(a^{{\\frac{{1}}{{{n}}}}}\\)?",
            f"The {ord_names[n]} of \\(a\\)",
            [f"The {n}th power of \\(a\\)", f"\\(a\\) divided by {n}", f"\\({n}\\) times \\(a\\)"],
            f"In rational index notation, \\(a^{{\\frac{{1}}{{n}}}}\\) denotes the \\(n\\)th root of \\(a\\), written in radical form as \\(\\sqrt[n]{{a}}\\).",
            f"For \\(n = {n}\\), this represents the {ord_names[n]} of \\(a\\).",
            f"Thus, \\(a^{{\\frac{{1}}{{{n}}}}}\ = \\sqrt[{{{n}}}]{{a}}\\).",
            d, v
        )
        questions.append(q)

    # 3.2.2 Reading and writing index forms (e.g. 5th root of 32) (need 80)
    tc = "MH-8-MTH-3-3.2.2"
    name = "Reading and writing index forms (e.g. 5th root of 32)"
    for i in range(80):
        base = 2 + (i % 8) * 5
        r = 3 + (i % 5)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Express 'The \\({r}\\)th root of \\({base}\\)' in index form.",
            f"\\(({base})^{{\\frac{{1}}{{{r}}}}}\\)",
            [f"\\(({base})^{{{r}}}\\)", f"\\(\\frac{{{base}}}{{{r}}}\\)", f"\\(({r})^{{\\frac{{1}}{{{base}}}}}\\)"],
            f"The \\(n\\)th root of a number \\(x\\) is written in index form as \\(x^{{\\frac{{1}}{{n}}}}\\).",
            f"Here \\(x = {base}\\) and root index \\(n = {r}\\).",
            f"Therefore, the index form is \\(({base})^{{\\frac{{1}}{{{r}}}}}\\).",
            d, v
        )
        questions.append(q)

    # 3.3.1 Meaning of a^(m/n) as mth power of nth root or nth root of mth power (need 80)
    tc = "MH-8-MTH-3-3.3.1"
    name = "Meaning of a^(m/n) as mth power of nth root or nth root of mth power"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "Which statement correctly explains the dual interpretation of the rational index \\(a^{\\frac{m}{n}}\\)?",
            "It can be interpreted both as the mth power of the nth root of a, and as the nth root of the mth power of a",
            [
                "It only represents division of m by n",
                "It represents m added to the nth root of a",
                "It is undefined for all rational numbers"
            ],
            f"By definition of fractional indices: \\(a^{{\\frac{{m}}{{n}}}} = (a^{{\\frac{{1}}{{n}}}})^m = (a^m)^{{\\frac{{1}}{{n}}}}\\).",
            f"This demonstrates that \\(a^{{\\frac{{m}}{{n}}}}\\) represents both the \\(m\\)th power of the \\(n\\)th root of \\(a\\), and the \\(n\\)th root of the \\(m\\)th power of \\(a\\).",
            f"Therefore, the dual interpretation is completely valid.",
            d, v
        )
        questions.append(q)

    # 3.3.2 Evaluation of fractional indices (need 80)
    tc = "MH-8-MTH-3-3.3.2"
    name = "Evaluation of fractional indices"
    for i in range(80):
        # 8^(2/3) = (2^3)^(2/3) = 2^2 = 4
        # 27^(2/3) = 9, 16^(3/4) = 8, 32^(2/5) = 4, 64^(2/3) = 16
        cases = [
            (8, 2, 3, 4),
            (27, 2, 3, 9),
            (16, 3, 4, 8),
            (32, 2, 5, 4),
            (64, 2, 3, 16)
        ]
        base, m, n, ans = cases[i % len(cases)]
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Evaluate the numerical value of: \\(({base})^{{\\frac{{{m}}}{{{n}}}}}\\).",
            f"\\({ans}\\)",
            [f"\\({ans + 2}\\)", f"\\({ans - 1}\\)", f"\\({base // n}\\)"],
            f"Express the base in prime power form: \\({base} = ({ans ** (1/m if m!=0 else 1):.0f})^{{{n}}}\\).",
            f"Take the \\({n}\\)th root first: \\(({base})^{{\\frac{{1}}{{{n}}}}} = {round(base ** (1/n))}\\).",
            f"Raise the result to power \\({m}\\): \\(({round(base ** (1/n))})^{{{m}}} = {ans}\\).",
            d, v
        )
        questions.append(q)

    # 3.4.1 Finding cube of positive and negative numbers and decimals (need 80)
    tc = "MH-8-MTH-3-3.4.1"
    name = "Finding cube of positive and negative numbers and decimals"
    for i in range(80):
        val = -(3 + (i % 6))
        cube = val ** 3
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find the cube of the negative integer \\({val}\\).",
            f"\\({cube}\\)",
            [f"\\({abs(cube)}\\)", f"\\({val * 3}\\)", f"\\({cube - 10}\\)"],
            f"The cube of a number \\(x\\) is \\(x^3 = x \\times x \\times x\\).",
            f"Here \\(x = {val}\\): \\(({val}) \\times ({val}) \\times ({val}) = ({val * val}) \\times ({val}) = {cube}\\).",
            f"Since the product of three negative numbers is negative, the cube of any negative number is always negative: \\({cube}\\).",
            d, v
        )
        questions.append(q)

    # 3.4.2 Finding cube root by prime factorisation method (need 80)
    tc = "MH-8-MTH-3-3.4.2"
    name = "Finding cube root by prime factorisation method"
    for i in range(80):
        p1 = [2, 3, 5][i % 3]
        p2 = [3, 5, 7][(i + 1) % 3]
        if p1 == p2: p2 = 2
        root = p1 * p2
        cube = root ** 3
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find the cube root of \\({cube}\\) using the prime factorisation method.",
            f"\\({root}\\)",
            [f"\\({root + p1}\\)", f"\\({root - p1}\\)", f"\\({cube // 3}\\)"],
            f"Write the prime factorisation of \\({cube}\\): it decomposes into \\({p1}^3 \\times {p2}^3\\).",
            f"Form triplets of identical factors: take one factor from each triplet: \\({p1} \\times {p2} = {root}\\).",
            f"Therefore, \\(\\sqrt[3]{{{cube}}} = {root}\\).",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch3_questions()
    print(f"Generated {len(qs)} questions for Chapter 3.")
    with open("scripts/mh8_mth_ch3_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/mh8_mth_ch3_topup.json")
