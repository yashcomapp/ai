import json
import random

random.seed(8102)

def build_ch2_questions():
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

    # 2.1.1 Multiplicative inverse using negative exponents (need 54)
    tc = "CBSE-8-MGP1-2-2.1.1"
    name = "Multiplicative inverse using negative exponents"
    for i in range(54):
        base = 2 + (i % 8)
        exp = 2 + (i % 5)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"What is the multiplicative inverse (reciprocal) of \\({base}^{{-{exp}}}\\)?",
            f"\\({base}^{{{exp}}}\\)",
            [f"\\(-{base}^{{{exp}}}\\)", f"\\({base}^{{-{exp}}}\\)", f"\\(\\frac{{1}}{{{base}^{{{exp+1}}}}}\\)"],
            f"Recall the law of negative exponents: \\(a^{{-m}} = \\frac{{1}}{{a^m}}\\). Thus \\({base}^{{-{exp}}} = \\frac{{1}}{{{base}^{{{exp}}}}}\\).",
            f"The multiplicative inverse of a fraction \\(\\frac{{1}}{{x}}\\) is \\(x\\). Here, \\(x = {base}^{{{exp}}}\\).",
            f"Therefore, the multiplicative inverse of \\({base}^{{-{exp}}}\\) is \\({base}^{{{exp}}}\\).",
            d, v
        )
        questions.append(q)

    # 2.1.2 Evaluating powers with negative exponents (need 52)
    tc = "CBSE-8-MGP1-2-2.1.2"
    name = "Evaluating powers with negative exponents"
    for i in range(52):
        base = [2, 3, 4, 5][i % 4]
        exp = 2 + (i % 3)
        val = base ** exp
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Evaluate the value of the exponential expression: \\(({base})^{{-{exp}}}\\).",
            f"\\(\\frac{{1}}{{{val}}}\\)",
            [f"\\(-{val}\\)", f"\\({val}\\)", f"\\(\\frac{{1}}{{{val * base}}}\\)"],
            f"Apply the definition of negative exponents: \\(a^{{-m}} = \\frac{{1}}{{a^m}}\\).",
            f"Substitute \\(a = {base}\\) and \\(m = {exp}\\): \\({base}^{{-{exp}}} = \\frac{{1}}{{{base}^{{{exp}}}}} = \\frac{{1}}{{{val}}}\\).",
            f"Hence, the evaluated numerical value is \\(\\frac{{1}}{{{val}}}\\).",
            d, v
        )
        questions.append(q)

    # 2.1.3 Expanded form of numbers using negative powers of 10 (need 52)
    tc = "CBSE-8-MGP1-2-2.1.3"
    name = "Expanded form of numbers using negative powers of 10"
    for i in range(52):
        d1 = 1 + (i % 9)
        d2 = (i * 3) % 9
        d3 = (i * 7 + 1) % 9
        num_str = f"0.{d1}{d2}{d3}"
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        correct_exp = f"\\({d1} \\times 10^{{-1}} + {d2} \\times 10^{{-2}} + {d3} \\times 10^{{-3}}\\)"
        wrongs = [
            f"\\({d1} \\times 10^{{1}} + {d2} \\times 10^{{2}} + {d3} \\times 10^{{3}}\\)",
            f"\\({d1} \\times 10^{{-2}} + {d2} \\times 10^{{-3}} + {d3} \\times 10^{{-4}}\\)",
            f"\\({d1} \\times 10^{{0}} + {d2} \\times 10^{{-1}} + {d3} \\times 10^{{-2}}\\)"
        ]
        q = make_q(
            tc, name,
            f"Express the decimal number \\({num_str}\\) in expanded form using negative powers of 10.",
            correct_exp, wrongs,
            f"Identify the decimal places: \\({d1}\\) is in tenths place (\\(10^{{-1}}\\)), \\({d2}\\) is in hundredths place (\\(10^{{-2}}\\)), and \\({d3}\\) is in thousandths place (\\(10^{{-3}}\\)).",
            f"Multiply each digit by its respective place value: \\({d1} \\times 10^{{-1}} + {d2} \\times 10^{{-2}} + {d3} \\times 10^{{-3}}\\).",
            f"Hence, this matches the standard exponential expanded form.",
            d, v
        )
        questions.append(q)

    # 2.2.1 Product of powers law (a^m * a^n = a^(m+n)) (need 64)
    tc = "CBSE-8-MGP1-2-2.2.1"
    name = "Product of powers law (a^m * a^n = a^(m+n))"
    for i in range(64):
        a = 2 + (i % 7)
        m = (i % 5) - 3  # can be negative
        n = ((i * 2) % 6) - 2
        sum_exp = m + n
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Simplify the expression using exponential laws: \\({a}^{{{m}}} \\times {a}^{{{n}}}\\).",
            f"\\({a}^{{{sum_exp}}}\\)",
            [f"\\({a}^{{{m * n}}}\\)", f"\\({a}^{{{m - n}}}\\)", f"\\({2 * a}^{{{sum_exp}}}\\)"],
            f"Use the product of powers rule: for any non-zero base \\(a\\), \\(a^m \\times a^n = a^{{m+n}}\\).",
            f"Add the exponents: \\({m} + ({n}) = {sum_exp}\\).",
            f"Therefore, the simplified form is \\({a}^{{{sum_exp}}}\\).",
            d, v
        )
        questions.append(q)

    # 2.2.2 Quotient of powers law (a^m / a^n = a^(m-n)) (need 65)
    tc = "CBSE-8-MGP1-2-2.2.2"
    name = "Quotient of powers law (a^m / a^n = a^(m-n))"
    for i in range(65):
        a = 3 + (i % 6)
        m = (i % 6) - 2
        n = ((i * 3) % 5) - 2
        diff_exp = m - n
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Simplify the quotient using exponential laws: \\(\\frac{{{a}^{{{m}}}}}{{{a}^{{{n}}}}}\\).",
            f"\\({a}^{{{diff_exp}}}\\)",
            [f"\\({a}^{{{m + n}}}\\)", f"\\({a}^{{{m * n}}}\\)", f"\\(1^{{{diff_exp}}}\\)"],
            f"Apply the quotient rule of powers: \\(\\frac{{a^m}}{{a^n}} = a^{{m-n}}\\).",
            f"Subtract the exponent in the denominator from the numerator: \\({m} - ({n}) = {diff_exp}\\).",
            f"Thus, the result is \\({a}^{{{diff_exp}}}\\).",
            d, v
        )
        questions.append(q)

    # 2.2.3 Power of a power law ((a^m)^n = a^(mn)) (need 63)
    tc = "CBSE-8-MGP1-2-2.2.3"
    name = "Power of a power law ((a^m)^n = a^(mn))"
    for i in range(63):
        a = 2 + (i % 8)
        m = (i % 4) - 2
        if m == 0: m = 3
        n = ((i + 1) % 4) - 2
        if n == 0: n = -2
        prod_exp = m * n
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Simplify the expression using the power of a power law: \\(({a}^{{{m}}})^{{{n}}}\\).",
            f"\\({a}^{{{prod_exp}}}\\)",
            [f"\\({a}^{{{m + n}}}\\)", f"\\({a}^{{{m - n}}}\\)", f"\\({a}^{{{prod_exp + 1}}}\\)"],
            f"Recall the power of a power rule: \\((a^m)^n = a^{{m \\times n}}\\).",
            f"Multiply the exponents together: \\({m} \\times ({n}) = {prod_exp}\\).",
            f"Hence, the simplified expression is \\({a}^{{{prod_exp}}}\\).",
            d, v
        )
        questions.append(q)

    # 2.2.4 Powers with same exponent (a^m * b^m = (ab)^m) (need 65)
    tc = "CBSE-8-MGP1-2-2.2.4"
    name = "Powers with same exponent (a^m * b^m = (ab)^m)"
    for i in range(65):
        a = 2 + (i % 5)
        b = 3 + (i % 4)
        if a == b: b = 7
        m = ((i % 5) - 3)
        if m == 0: m = -2
        prod_base = a * b
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Simplify the product: \\({a}^{{{m}}} \\times {b}^{{{m}}}\\).",
            f"\\({prod_base}^{{{m}}}\\)",
            [f"\\({a + b}^{{{m}}}\\)", f"\\({prod_base}^{{{2 * m}}}\\)", f"\\({a * b}^{{{m + 1}}}\\)"],
            f"By the law of exponents for equal powers: \\(a^m \\times b^m = (a \\times b)^m\\).",
            f"Multiply the bases: \\({a} \\times {b} = {prod_base}\\), keeping the exponent \\({m}\\).",
            f"Therefore, the simplified form is \\({prod_base}^{{{m}}}\\).",
            d, v
        )
        questions.append(q)

    # 2.2.5 Zero exponent (a^0 = 1) (need 61)
    tc = "CBSE-8-MGP1-2-2.2.5"
    name = "Zero exponent (a^0 = 1)"
    for i in range(61):
        base_val = 5 + i * 3
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Evaluate the value of \\(({base_val})^0\\) where \\({base_val} \\neq 0\\).",
            "\\(1\\)",
            ["\\(0\\)", f"\\({base_val}\\)", "\\(-1\\)"],
            f"Recall the zero exponent property: for any non-zero real number \\(a\\), \\(a^0 = 1\\).",
            f"This arises from the quotient law \\(\\frac{{a^m}}{{a^m}} = a^{{m-m}} = a^0 = 1\\).",
            f"Since \\({base_val} \\neq 0\\), \\(({base_val})^0 = 1\\).",
            d, v
        )
        questions.append(q)

    # 2.3.1 Expressing very small numbers in standard form (need 76)
    tc = "CBSE-8-MGP1-2-2.3.1"
    name = "Expressing very small numbers in standard form"
    for i in range(76):
        lead_zeros = 3 + (i % 5)
        coeff = 1 + (i % 8)
        num_str = "0." + ("0" * lead_zeros) + str(coeff)
        neg_exp = -(lead_zeros + 1)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Express the number \\({num_str}\\) in scientific standard form \\(m \\times 10^n\\) where \\(1 \\le m < 10\\).",
            f"\\({coeff} \\times 10^{{{neg_exp}}}\\)",
            [f"\\({coeff} \\times 10^{{{neg_exp + 1}}}\\)", f"\\({coeff} \\times 10^{{{neg_exp - 1}}}\\)", f"\\({coeff * 10} \\times 10^{{{neg_exp}}}\\)"],
            f"Standard form requires \\(m \\times 10^n\\) with \\(1 \\le m < 10\\). Here \\(m = {coeff}\\).",
            f"Count the number of places the decimal point shifts to the right: exactly \\({abs(neg_exp)}\\) places.",
            f"Hence, the standard form is \\({coeff} \\times 10^{{{neg_exp}}}\\).",
            d, v
        )
        questions.append(q)

    # 2.3.2 Expressing very large numbers in standard form (need 7)
    tc = "CBSE-8-MGP1-2-2.3.2"
    name = "Expressing very large numbers in standard form"
    for i in range(7):
        zeros_cnt = 5 + i
        coeff = 3 + i
        num_str = str(coeff) + ("0" * zeros_cnt)
        pos_exp = zeros_cnt
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Express the large number \\({num_str}\\) in standard scientific form \\(m \\times 10^n\\).",
            f"\\({coeff} \\times 10^{{{pos_exp}}}\\)",
            [f"\\({coeff} \\times 10^{{{pos_exp - 1}}}\\)", f"\\({coeff} \\times 10^{{{pos_exp + 1}}}\\)", f"\\({coeff * 10} \\times 10^{{{pos_exp}}}\\)"],
            f"Move the decimal point to the left so that the coefficient lies in \\([1, 10)\\).",
            f"The decimal shifts \\({pos_exp}\\) positions to the left.",
            f"Therefore, the standard form is \\({coeff} \\times 10^{{{pos_exp}}}\\).",
            d, v
        )
        questions.append(q)

    # 2.3.3 Converting standard form back to usual decimal form (need 75)
    tc = "CBSE-8-MGP1-2-2.3.3"
    name = "Converting standard form back to usual decimal form"
    for i in range(75):
        lead_zeros = 2 + (i % 4)
        coeff = 2 + (i % 7)
        neg_exp = -(lead_zeros + 1)
        usual_str = "0." + ("0" * lead_zeros) + str(coeff)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Convert the standard form number \\({coeff} \\times 10^{{{neg_exp}}}\\) into usual decimal notation.",
            f"\\({usual_str}\\)",
            [f"0.{('0' * (lead_zeros + 1))}{coeff}", f"0.{('0' * max(0, lead_zeros - 1))}{coeff}", f"{coeff}.{lead_zeros}"],
            f"A negative power of 10 indicates shifting the decimal point to the left.",
            f"For \\(10^{{{neg_exp}}}\\), move the decimal point \\({abs(neg_exp)}\\) places to the left from \\({coeff}\\).",
            f"This produces \\({usual_str}\\).",
            d, v
        )
        questions.append(q)

    # 2.4.1 Comparing very large and very small quantities (need 42)
    tc = "CBSE-8-MGP1-2-2.4.1"
    name = "Comparing very large and very small quantities"
    for i in range(42):
        exp1 = 4 + (i % 5)
        exp2 = exp1 + 2
        diff_power = exp2 - exp1
        ratio = 10 ** diff_power
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"How many times larger is \\(10^{{{exp2}}}\\) compared to \\(10^{{{exp1}}}\\)?",
            f"\\({ratio}\\) times",
            [f"\\({ratio // 10}\\) times", f"\\({ratio * 10}\\) times", f"\\({diff_power}\\) times"],
            f"To find how many times larger, compute the ratio: \\(\\frac{{10^{{{exp2}}}}}{{10^{{{exp1}}}}}\\).",
            f"Apply the quotient of powers law: \\(10^{{{exp2} - {exp1}}} = 10^{{{diff_power}}} = {ratio}\\).",
            f"Hence, it is \\({ratio}\\) times larger.",
            d, v
        )
        questions.append(q)

    # 2.4.2 Addition and subtraction of numbers in standard form (need 36)
    tc = "CBSE-8-MGP1-2-2.4.2"
    name = "Addition and subtraction of numbers in standard form"
    for i in range(36):
        c1 = 2 + (i % 4)
        c2 = 3 + (i % 3)
        exp = 4 + (i % 4)
        sum_c = c1 + c2
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Perform the addition: \\(({c1} \\times 10^{{{exp}}}) + ({c2} \\times 10^{{{exp}}})\\).",
            f"\\({sum_c} \\times 10^{{{exp}}}\\)",
            [f"\\({sum_c} \\times 10^{{{2 * exp}}}\\)", f"\\({c1 * c2} \\times 10^{{{exp}}}\\)", f"\\({sum_c} \\times 10^{{{exp + 1}}}\\)"],
            f"Factor out the common power of 10: \\(({c1} + {c2}) \\times 10^{{{exp}}}\\).",
            f"Add the coefficients: \\({c1} + {c2} = {sum_c}\\).",
            f"Since \\({sum_c} < 10\\), the result in standard form is \\({sum_c} \\times 10^{{{exp}}}\\).",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch2_questions()
    print(f"Generated {len(qs)} questions for Chapter 2.")
    with open("scripts/cbse8_mgp1_ch2_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/cbse8_mgp1_ch2_topup.json")
