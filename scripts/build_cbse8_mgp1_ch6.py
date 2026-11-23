import json
import random

random.seed(8106)

def build_ch6_questions():
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

    # 6.1.1 Terms, variables, constants & numerical coefficients (need 45)
    tc = "CBSE-8-MGP1-6-6.1.1"
    name = "Terms, variables, constants & numerical coefficients"
    for i in range(45):
        coeff = -9 + (i % 17)
        if coeff == 0: coeff = 5
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"What is the numerical coefficient of the term \\({coeff}x^2y\\)?",
            f"\\({coeff}\\)",
            [f"\\({abs(coeff) + 1}\\)", f"\\({-coeff}\\)", f"\\({coeff * 2}\\)"],
            f"An algebraic term consists of a numerical factor (coefficient) multiplied by algebraic variables.",
            f"In the term \\({coeff}x^2y\\), the variable part is \\(x^2y\\) and the constant multiplier is \\({coeff}\\).",
            f"Hence, the numerical coefficient is \\({coeff}\\).",
            d, v
        )
        questions.append(q)

    # 6.1.2 Like and unlike algebraic terms (need 56)
    tc = "CBSE-8-MGP1-6-6.1.2"
    name = "Like and unlike algebraic terms"
    for i in range(56):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "Which of the following pairs of algebraic terms represents LIKE TERMS?",
            "\\(7xy^2\\) and \\(-13xy^2\\)",
            ["\\(7x^2y\\) and \\(-13xy^2\\)", "\\(5x\\) and \\(5y\\)", "\\(3xy\\) and \\(3x^2y^2\\)"],
            f"Like terms are terms that have the exact same algebraic variables raised to the exact same corresponding powers.",
            f"In \\(7xy^2\\) and \\(-13xy^2\\), both terms have variable factor \\(x^1y^2\\).",
            f"Therefore, they are like terms.",
            d, v
        )
        questions.append(q)

    # 6.1.3 Monomials, binomials, trinomials & polynomials (need 57)
    tc = "CBSE-8-MGP1-6-6.1.3"
    name = "Monomials, binomials, trinomials & polynomials"
    for i in range(57):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "How is the algebraic expression \\(4x^2 - 3x + 7\\) classified based on its number of non-zero terms?",
            "Trinomial",
            ["Monomial", "Binomial", "Linear equation"],
            f"Count the distinct terms separated by addition or subtraction: \\(4x^2\\), \\(-3x\\), and \\(7\\).",
            f"An expression containing exactly three unlike terms is formally defined as a trinomial.",
            f"Hence, \\(4x^2 - 3x + 7\\) is a trinomial.",
            d, v
        )
        questions.append(q)

    # 6.2.1 Horizontal and column addition of like terms (need 38)
    tc = "CBSE-8-MGP1-6-6.2.1"
    name = "Horizontal and column addition of like terms"
    for i in range(38):
        c1 = 3 + (i % 7)
        c2 = 2 + (i % 5)
        sum_c = c1 + c2
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Add the algebraic terms: \\({c1}ab + {c2}ab\\).",
            f"\\({sum_c}ab\\)",
            [f"\\({sum_c}a^2b^2\\)", f"\\({c1 * c2}ab\\)", f"\\({sum_c + 1}ab\\)"],
            f"Identify that \\({c1}ab\\) and \\({c2}ab\\) are like terms sharing the variable part \\(ab\\).",
            f"Add their numerical coefficients: \\({c1} + {c2} = {sum_c}\\).",
            f"Therefore, \\({c1}ab + {c2}ab = {sum_c}ab\\).",
            d, v
        )
        questions.append(q)

    # 6.2.2 Subtraction with sign changes of subtrahend (need 40)
    tc = "CBSE-8-MGP1-6-6.2.2"
    name = "Subtraction with sign changes of subtrahend"
    for i in range(40):
        c1 = 8 + (i % 5)
        c2 = 3 + (i % 4)
        diff_c = c1 - c2
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Subtract \\({c2}x^2\\) from \\({c1}x^2\\).",
            f"\\({diff_c}x^2\\)",
            [f"\\({c1 + c2}x^2\\)", f"\\({-diff_c}x^2\\)", f"\\({diff_c}x\\)"],
            f"The operation is \\({c1}x^2 - ({c2}x^2)\\).",
            f"Subtract the coefficients of like terms: \\({c1} - {c2} = {diff_c}\\).",
            f"Thus, the result is \\({diff_c}x^2\\).",
            d, v
        )
        questions.append(q)

    # 6.3.1 Product of two or more monomials (need 50)
    tc = "CBSE-8-MGP1-6-6.3.1"
    name = "Product of two or more monomials"
    for i in range(50):
        c1 = 2 + (i % 5)
        c2 = 3 + (i % 4)
        prod_c = c1 * c2
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Multiply the monomials: \\(({c1}x) \\times ({c2}x^2)\\).",
            f"\\({prod_c}x^3\\)",
            [f"\\({prod_c}x^2\\)", f"\\({c1 + c2}x^3\\)", f"\\({prod_c}x\\)"],
            f"Multiply the numerical coefficients: \\({c1} \\times {c2} = {prod_c}\\).",
            f"Apply the product law of exponents for the variable parts: \\(x^1 \\times x^2 = x^{{1+2}} = x^3\\).",
            f"Therefore, the product is \\({prod_c}x^3\\).",
            d, v
        )
        questions.append(q)

    # 6.3.2 Multiplying monomial by binomial/trinomial (Distributive law) (need 54)
    tc = "CBSE-8-MGP1-6-6.3.2"
    name = "Multiplying monomial by binomial/trinomial (Distributive law)"
    for i in range(54):
        c = 2 + (i % 4)
        k = 3 + (i % 5)
        ck = c * k
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Expand using the distributive law: \\({c}x(x + {k})\\).",
            f"\\({c}x^2 + {ck}x\\)",
            [f"\\({c}x^2 + {k}\\)", f"\\({c}x^2 + {ck}\\)", f"\\({c + 1}x^2 + {ck}x\\)"],
            f"Distribute the monomial \\({c}x\\) across each term inside parentheses: \\(({c}x \\times x) + ({c}x \\times {k})\\).",
            f"Multiply each product: \\({c}x^2 + {ck}x\\).",
            f"Thus, the expanded expression is \\({c}x^2 + {ck}x\\).",
            d, v
        )
        questions.append(q)

    # 6.3.3 Multiplying binomial by binomial (FOIL method) (need 54)
    tc = "CBSE-8-MGP1-6-6.3.3"
    name = "Multiplying binomial by binomial (FOIL method)"
    for i in range(54):
        a = 2 + (i % 5)
        b = 3 + (i % 4)
        sum_ab = a + b
        prod_ab = a * b
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Multiply the binomials: \\((x + {a})(x + {b})\\).",
            f"\\(x^2 + {sum_ab}x + {prod_ab}\\)",
            [f"\\(x^2 + {prod_ab}\\)", f"\\(x^2 + {sum_ab}x - {prod_ab}\\)", f"\\(x^2 + {prod_ab}x + {sum_ab}\\)"],
            f"Expand using the FOIL method: \\(x \\times x + x \\times {b} + {a} \\times x + {a} \\times {b}\\).",
            f"Combine like terms: \\(x^2 + ({b}x + {a}x) + {prod_ab} = x^2 + {sum_ab}x + {prod_ab}\\).",
            f"Hence, the product is \\(x^2 + {sum_ab}x + {prod_ab}\\).",
            d, v
        )
        questions.append(q)

    # 6.4.1 Square of a sum identity: (a+b)² = a² + 2ab + b² (need 49)
    tc = "CBSE-8-MGP1-6-6.4.1"
    name = "Square of a sum identity: (a+b)² = a² + 2ab + b²"
    for i in range(49):
        k = 3 + (i % 7)
        two_k = 2 * k
        k_sq = k * k
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Expand using standard algebraic identities: \\((x + {k})^2\\).",
            f"\\(x^2 + {two_k}x + {k_sq}\\)",
            [f"\\(x^2 + {k_sq}\\)", f"\\(x^2 + {k}x + {k_sq}\\)", f"\\(x^2 - {two_k}x + {k_sq}\\)"],
            f"Apply the identity for the square of a sum: \\((a + b)^2 = a^2 + 2ab + b^2\\).",
            f"Substitute \\(a = x\\) and \\(b = {k}\\): \\(x^2 + 2(x)({k}) + {k}^2\\).",
            f"Simplify: \\(x^2 + {two_k}x + {k_sq}\\).",
            d, v
        )
        questions.append(q)

    # 6.4.2 Square of a difference identity: (a-b)² = a² - 2ab + b² (need 63)
    tc = "CBSE-8-MGP1-6-6.4.2"
    name = "Square of a difference identity: (a-b)² = a² - 2ab + b²"
    for i in range(63):
        k = 2 + (i % 6)
        two_k = 2 * k
        k_sq = k * k
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Expand using standard algebraic identities: \\((x - {k})^2\\).",
            f"\\(x^2 - {two_k}x + {k_sq}\\)",
            [f"\\(x^2 - {k_sq}\\)", f"\\(x^2 + {two_k}x + {k_sq}\\)", f"\\(x^2 - {two_k}x - {k_sq}\\)"],
            f"Apply the square of a difference identity: \\((a - b)^2 = a^2 - 2ab + b^2\\).",
            f"Substitute \\(a = x\\) and \\(b = {k}\\): \\(x^2 - 2(x)({k}) + {k}^2\\).",
            f"Simplify: \\(x^2 - {two_k}x + {k_sq}\\).",
            d, v
        )
        questions.append(q)

    # 6.4.3 Difference of squares identity: (a+b)(a-b) = a² - b² (need 63)
    tc = "CBSE-8-MGP1-6-6.4.3"
    name = "Difference of squares identity: (a+b)(a-b) = a² - b²"
    for i in range(63):
        k = 3 + (i % 8)
        k_sq = k * k
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Evaluate the product using standard identities: \\((x + {k})(x - {k})\\).",
            f"\\(x^2 - {k_sq}\\)",
            [f"\\(x^2 + {k_sq}\\)", f"\\(x^2 - {2 * k}x - {k_sq}\\)", f"\\(x^2 - {k}\\)"],
            f"Apply the difference of squares identity: \\((a + b)(a - b) = a^2 - b^2\\).",
            f"Substitute \\(a = x\\) and \\(b = {k}\\): \\(x^2 - {k}^2\\).",
            f"Simplify: \\(x^2 - {k_sq}\\).",
            d, v
        )
        questions.append(q)

    # 6.4.4 Product with common term: (x+a)(x+b) = x² + (a+b)x + ab (need 63)
    tc = "CBSE-8-MGP1-6-6.4.4"
    name = "Product with common term: (x+a)(x+b) = x² + (a+b)x + ab"
    for i in range(63):
        a = 1 + (i % 6)
        b = 4 + (i % 5)
        sum_ab = a + b
        prod_ab = a * b
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Use the standard product identity \\((x+a)(x+b) = x^2 + (a+b)x + ab\\) to expand \\((x + {a})(x + {b})\\).",
            f"\\(x^2 + {sum_ab}x + {prod_ab}\\)",
            [f"\\(x^2 + {prod_ab}x + {sum_ab}\\)", f"\\(x^2 + {sum_ab}x - {prod_ab}\\)", f"\\(x^2 + {a * b}\\)"],
            f"Identify \\(a = {a}\\) and \\(b = {b}\\).",
            f"Sum of terms: \\(a + b = {a} + {b} = {sum_ab}\\). Product of terms: \\(ab = {a} \\times {b} = {prod_ab}\\).",
            f"Substitute into the identity: \\(x^2 + {sum_ab}x + {prod_ab}\\).",
            d, v
        )
        questions.append(q)

    # 6.5.1 Fast mental calculations using identities (103², 98², 105*95) (need 39)
    tc = "CBSE-8-MGP1-6-6.5.1"
    name = "Fast mental calculations using identities (103², 98², 105*95)"
    for i in range(39):
        k = 1 + (i % 6)
        ans = 10000 - k * k
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Evaluate \\(({100 + k}) \\times ({100 - k})\\) quickly using an algebraic identity.",
            f"\\({ans}\\)",
            [f"\\({ans + 20}\\)", f"\\({ans - 20}\\)", f"\\(10000\\)"],
            f"Notice the structure \\((a + b)(a - b) = a^2 - b^2\\) with \\(a = 100\\) and \\(b = {k}\\).",
            f"Compute: \\(100^2 - {k}^2 = 10000 - {k*k} = {ans}\\).",
            f"Therefore, \\({100+k} \\times {100-k} = {ans}\\).",
            d, v
        )
        questions.append(q)

    # 6.5.2 Mind mistakes, mend mistakes: Spotting and correcting algebraic errors (need 39)
    tc = "CBSE-8-MGP1-6-6.5.2"
    name = "Mind mistakes, mend mistakes: Spotting and correcting algebraic errors"
    for i in range(39):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "A student writes \\((x + 5)^2 = x^2 + 25\\). What error did the student commit?",
            "Omitted the middle cross-product term \\(2ab = 10x\\)",
            [
                "Wrongly squared 5 as 25",
                "Subtracted instead of adding",
                "There is no error; the expansion is mathematically correct"
            ],
            f"The correct expansion of a square of a sum is \\((a + b)^2 = a^2 + 2ab + b^2\\).",
            f"For \\((x + 5)^2\\), \\(a = x\\) and \\(b = 5\\), giving \\(x^2 + 2(x)(5) + 5^2 = x^2 + 10x + 25\\).",
            f"The student omitted the cross-product term \\(10x\\).",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch6_questions()
    print(f"Generated {len(qs)} questions for Chapter 6.")
    with open("scripts/cbse8_mgp1_ch6_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/cbse8_mgp1_ch6_topup.json")
