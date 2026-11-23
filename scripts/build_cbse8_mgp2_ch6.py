import json
import random

random.seed(8206)

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

    # 6.1.1 Algebraic balance concept: Add, subtract, multiply, divide both sides (need 39)
    tc = "CBSE-8-MGP2-6-6.1.1"
    name = "Algebraic balance concept: Add, subtract, multiply, divide both sides"
    for i in range(39):
        c = 3 + (i % 7)
        k = 5 + (i % 8)
        ans = 2 + (i % 6)
        rhs = c * ans + k
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Solve for \\(x\\) using the balance method: \\({c}x + {k} = {rhs}\\).",
            f"\\(x = {ans}\\)",
            [f"\\(x = {ans + 1}\\)", f"\\(x = {ans - 1}\\)", f"\\(x = {ans * 2}\\)"],
            f"Subtract \\({k}\\) from both sides to maintain equality: \\({c}x = {rhs} - {k} = {rhs - k}\\).",
            f"Divide both sides by \\({c}\\): \\(x = \\frac{{{rhs - k}}}{{{c}}} = {ans}\\).",
            f"Hence, \\(x = {ans}\\).",
            d, v
        )
        questions.append(q)

    # 6.1.2 Transposition method for solving equations (need 39)
    tc = "CBSE-8-MGP2-6-6.1.2"
    name = "Transposition method for solving equations"
    for i in range(39):
        a = 2 + (i % 5)
        ans = 4 + (i % 6)
        b = 7 + (i % 9)
        rhs = a * ans - b
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Solve the linear equation by transposing constants: \\({a}x - {b} = {rhs}\\).",
            f"\\(x = {ans}\\)",
            [f"\\(x = {ans + 2}\\)", f"\\(x = {ans - 2}\\)", f"\\(x = {ans + 5}\\)"],
            f"Transpose \\(-{b}\\) to the right-hand side, changing its sign to \\(+{b}\\): \\({a}x = {rhs} + {b} = {rhs + b}\\).",
            f"Transpose coefficient \\({a}\\) by division: \\(x = \\frac{{{rhs + b}}}{{{a}}} = {ans}\\).",
            f"Therefore, \\(x = {ans}\\).",
            d, v
        )
        questions.append(q)

    # 6.2.1 Grouping like variable terms on one side (need 39)
    tc = "CBSE-8-MGP2-6-6.2.1"
    name = "Grouping like variable terms on one side"
    for i in range(39):
        x_val = 3 + (i % 5)
        # 5x - 4 = 2x + (3x_val - 4)
        c1, c2 = 5, 2
        diff_c = c1 - c2  # 3
        k1 = 4
        k2 = diff_c * x_val - k1
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Solve the equation with variables on both sides: \\({c1}x - {k1} = {c2}x + {k2}\\).",
            f"\\(x = {x_val}\\)",
            [f"\\(x = {x_val + 1}\\)", f"\\(x = {x_val - 1}\\)", f"\\(x = {x_val * 2}\\)"],
            f"Transpose variable term \\({c2}x\\) to LHS and constant \\(-{k1}\\) to RHS: \\({c1}x - {c2}x = {k2} + {k1}\\).",
            f"Simplify both sides: \\({diff_c}x = {k2 + k1}\\).",
            f"Divide by \\({diff_c}\\): \\(x = \\frac{{{k2 + k1}}}{{{diff_c}}} = {x_val}\\).",
            d, v
        )
        questions.append(q)

    # 6.2.2 Equations with parentheses and brackets (need 39)
    tc = "CBSE-8-MGP2-6-6.2.2"
    name = "Equations with parentheses and brackets"
    for i in range(39):
        ans = 2 + (i % 6)
        m = 3
        k = 2
        # 3(x - 2) = 3x - 6 = 3*ans - 6
        rhs = m * (ans - k)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Solve for \\(x\\): \\({m}(x - {k}) = {rhs}\\).",
            f"\\(x = {ans}\\)",
            [f"\\(x = {ans + 2}\\)", f"\\(x = {ans - 2}\\)", f"\\(x = {ans + 4}\\)"],
            f"Expand the parentheses on LHS: \\({m}x - {m * k} = {rhs}\\).",
            f"Transpose \\(-{m * k}\\) to RHS: \\({m}x = {rhs} + {m * k} = {rhs + m * k}\\).",
            f"Solve for \\(x\\): \\(x = \\frac{{{rhs + m * k}}}{{{m}}} = {ans}\\).",
            d, v
        )
        questions.append(q)

    # 6.3.1 Cross multiplication method for fractional equations (need 39)
    tc = "CBSE-8-MGP2-6-6.3.1"
    name = "Cross multiplication method for fractional equations"
    for i in range(39):
        ans = 5 + (i % 5)
        # (x + 1) / (x + 4) = num / den
        num = ans + 1
        den = ans + 4
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Solve using cross-multiplication: \\(\\frac{{x + 1}}{{x + 4}} = \\frac{{{num}}}{{{den}}}\\).",
            f"\\(x = {ans}\\)",
            [f"\\(x = {ans + 2}\\)", f"\\(x = {ans - 2}\\)", f"\\(x = 1\\)"],
            f"Apply cross-multiplication: \\({den}(x + 1) = {num}(x + 4)\\).",
            f"Expand both sides: \\({den}x + {den} = {num}x + {num * 4}\\).",
            f"Group like terms and solve: \\(({den} - {num})x = {num * 4} - {den} \\implies x = {ans}\\).",
            d, v
        )
        questions.append(q)

    # 6.3.2 Clearing denominators using LCM (need 39)
    tc = "CBSE-8-MGP2-6-6.3.2"
    name = "Clearing denominators using LCM"
    for i in range(39):
        ans = 6 + (i % 6)
        # x/2 + x/3 = 5x/6
        rhs_num = 5 * ans
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Solve the equation by clearing denominators using LCM: \\(\\frac{{x}}{{2}} + \\frac{{x}}{{3}} = \\frac{{{rhs_num}}}{{6}}\\).",
            f"\\(x = {ans}\\)",
            [f"\\(x = {ans + 3}\\)", f"\\(x = {ans - 2}\\)", f"\\(x = {rhs_num}\\)"],
            f"Find the LCM of the denominators \\(2, 3, 6\\), which is \\(6\\). Multiply the entire equation by 6.",
            f"\\(6\\left(\\frac{{x}}{{2}}\\right) + 6\\left(\\frac{{x}}{{3}}\\right) = 6\\left(\\frac{{{rhs_num}}}{{6}}\\right) \\implies 3x + 2x = {rhs_num}\\).",
            f"Combine terms: \\(5x = {rhs_num} \\implies x = \\frac{{{rhs_num}}}{{5}} = {ans}\\).",
            d, v
        )
        questions.append(q)

    # 6.4.1 Decoding 'think of a number' and calendar date tricks (need 66)
    tc = "CBSE-8-MGP2-6-6.4.1"
    name = "Decoding 'think of a number' and calendar date tricks"
    for i in range(66):
        n = 4 + (i % 15)
        # multiply by 4, add 10, result = 4n + 10
        res = 4 * n + 10
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"A puzzle says: 'I think of a number, multiply it by 4, and add 10. The result is \\({res}\\).' What was the original number?",
            f"\\({n}\\)",
            [f"\\({n + 2}\\)", f"\\({n - 2}\\)", f"\\({res // 4}\\)"],
            f"Translate the word puzzle into an algebraic equation: Let the number be \\(x\\). Then \\(4x + 10 = {res}\\).",
            f"Subtract 10 from both sides: \\(4x = {res} - 10 = {res - 10}\\).",
            f"Divide by 4: \\(x = \\frac{{{res - 10}}}{{4}} = {n}\\).",
            d, v
        )
        questions.append(q)

    # 6.4.2 Word problems on numbers, digits and consecutive integers (need 65)
    tc = "CBSE-8-MGP2-6-6.4.2"
    name = "Word problems on numbers, digits and consecutive integers"
    for i in range(65):
        first = 11 + (i % 20)
        s = 3 * first + 3  # n + (n+1) + (n+2)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"The sum of three consecutive natural numbers is \\({s}\\). Find the smallest of the three numbers.",
            f"\\({first}\\)",
            [f"\\({first + 1}\\)", f"\\({first - 1}\\)", f"\\({first + 2}\\)"],
            f"Let the three consecutive integers be \\(x\\), \\(x+1\\), and \\(x+2\\).",
            f"Set up equation: \\(x + (x+1) + (x+2) = 3x + 3 = {s}\\).",
            f"Solve for \\(x\\): \\(3x = {s} - 3 = {s - 3} \\implies x = \\frac{{{s - 3}}}{{3}} = {first}\\).",
            d, v
        )
        questions.append(q)

    # 6.4.3 Word problems on age comparisons (need 39)
    tc = "CBSE-8-MGP2-6-6.4.3"
    name = "Word problems on age comparisons"
    for i in range(39):
        son = 10 + (i % 6)
        father = 3 * son
        # in 10 years: father + 10 = 2 * (son + 10) + (father - 2*son - 10)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"A father is currently 3 times as old as his son. If the sum of their current ages is \\({father + son}\\text{{ years}}\\), how old is the son?",
            f"\\({son}\\text{{ years}}\\)",
            [f"\\({son + 4}\\text{{ years}}\\)", f"\\({son - 2}\\text{{ years}}\\)", f"\\({father // 2}\\text{{ years}}\\)"],
            f"Let the son's present age be \\(x\\). Then the father's present age is \\(3x\\).",
            f"Sum of their ages: \\(x + 3x = 4x = {father + son}\\).",
            f"Solve for \\(x\\): \\(x = \\frac{{{father + son}}}{{4}} = {son}\\text{{ years}}\\).",
            d, v
        )
        questions.append(q)

    # 6.4.4 Word problems on perimeter, geometry, coins and notes (need 68)
    tc = "CBSE-8-MGP2-6-6.4.4"
    name = "Word problems on perimeter, geometry, coins and notes"
    for i in range(68):
        b = 5 + (i % 10)
        l = b + 3
        peri = 2 * (l + b)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"The length of a rectangular plot is \\(3\\text{{ m}}\\) more than its breadth. If the perimeter is \\({peri}\\text{{ m}}\\), find its breadth.",
            f"\\({b}\\text{{ m}}\\)",
            [f"\\({b + 3}\\text{{ m}}\\)", f"\\({b - 2}\\text{{ m}}\\)", f"\\({peri // 4}\\text{{ m}}\\)"],
            f"Let breadth be \\(x\\text{{ m}}\\). Then length is \\((x + 3)\\text{{ m}}\\).",
            f"Perimeter formula: \\(2(\\text{{length}} + \\text{{breadth}}) = 2((x + 3) + x) = 2(2x + 3) = 4x + 6 = {peri}\\).",
            f"Solve for \\(x\\): \\(4x = {peri} - 6 = {peri - 6} \\implies x = \\frac{{{peri - 6}}}{{4}} = {b}\\text{{ m}}\\).",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch6_questions()
    print(f"Generated {len(qs)} questions for Chapter 6.")
    with open("scripts/cbse8_mgp2_ch6_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/cbse8_mgp2_ch6_topup.json")
