import json
import random

random.seed(81414)

def build_ch14_questions():
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
    # 14.1.1 Principal, Rate, Period in years (80 questions)
    # -------------------------------------------------------------
    tc_1411 = "MH-8-MTH-14-14.1.1"
    name_1411 = "Principal, Rate, Period in years"
    p_r_n_cases = [
        ("In financial mathematics, what does 'Principal' (P) refer to?", "The initial sum of money borrowed, lent, or deposited", ["The total interest paid at the end", "The annual percentage rate", "The duration of the investment"]),
        ("In the formula \\(A = P\\left(1 + \\frac{R}{100}\\right)^N\\), what does the variable \\(R\\) represent?", "The annual rate of interest in percentage (p.c.p.a.)", ["The remaining balance", "The repayment period", "The ratio of principal to time"]),
        ("In compound interest computations, how is the time period \\(N\\) expressed?", "The number of years (or compounding conversion periods)", ["In months without conversion", "In days multiplied by 365", "In currency units"]),
        ("How does Compound Interest differ fundamentally from Simple Interest?", "In compound interest, interest earned is added to the principal for calculating interest in subsequent periods", ["In compound interest, the principal remains strictly fixed each year", "Compound interest is always lower than simple interest", "Simple interest charges interest on interest"])
    ]
    for i in range(80):
        ctx, ans, wrongs = p_r_n_cases[i % len(p_r_n_cases)]
        q = make_q(
            tc_1411, name_1411,
            f"Financial mathematics fundamentals: {ctx}",
            ans, wrongs,
            "Review the definitions and variables used in compound interest calculations.",
            "Principal (P) is the capital amount, Rate (R) is percentage per annum, and Period (N) is duration.",
            f"Therefore, the accurate definition is '{ans}'.",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 14.1.2 Calculation of total amount A and Interest I = A - P (80 questions)
    # -------------------------------------------------------------
    tc_1412 = "MH-8-MTH-14-14.1.2"
    name_1412 = "Calculation of total amount A and Interest I = A - P"
    ci_data = [
        (10000, 10, 2, 12100, 2100), (20000, 10, 2, 24200, 4200), (5000, 10, 2, 6050, 1050),
        (10000, 5, 2, 11025, 1025), (4000, 5, 2, 4410, 410), (8000, 5, 2, 8820, 820),
        (1000, 10, 3, 1331, 331), (2000, 10, 3, 2662, 662), (5000, 20, 2, 7200, 2200),
        (10000, 20, 2, 14400, 4400), (12000, 10, 2, 14520, 2520), (15000, 10, 2, 18150, 3150),
        (25000, 10, 2, 30250, 5250), (6000, 10, 2, 7260, 1260), (30000, 10, 2, 36300, 6300),
        (50000, 10, 2, 60500, 10500)
    ]
    for i in range(80):
        p, r, n, a, ci = ci_data[i % len(ci_data)]
        ans = f"\\(₹{ci}\\)"
        w1 = f"\\(₹{ci + 100}\\)"
        w2 = f"\\(₹{max(50, ci - 100)}\\)"
        w3 = f"\\(₹{ci + 200}\\)"
        
        q = make_q(
            tc_1412, name_1412,
            f"Find the compound interest on \\(₹{p}\\) at \\({r}\\%\\) p.c.p.a. for \\({n}\\) years compounded annually.",
            ans, [w1, w2, w3],
            f"Apply the amount formula: \\(A = P\\left(1 + \\frac{{R}}{{100}}\\right)^N = {p}\\left(1 + \\frac{{{r}}}{{100}}\\right)^{{{n}}}\\).",
            f"Calculate total amount: \\(A = ₹{a}\\).",
            f"Determine compound interest: \\(I = A - P = ₹{a} - ₹{p} = {ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 14.2.1 Formula for appreciation: A = P(1 + r/100)^N (80 questions)
    # -------------------------------------------------------------
    tc_1421 = "MH-8-MTH-14-14.2.1"
    name_1421 = "Formula for appreciation: A = P(1 + r/100)^N"
    pop_data = [
        (10000, 10, 2, 12100), (20000, 5, 2, 22050), (50000, 10, 2, 60500),
        (40000, 5, 2, 44100), (100000, 10, 2, 121000), (80000, 5, 2, 88200),
        (60000, 10, 2, 72600), (25000, 10, 2, 30250), (15000, 10, 2, 18150),
        (30000, 10, 2, 36300)
    ]
    for i in range(80):
        p, r, n, a = pop_data[i % len(pop_data)]
        ans = f"\\({a:,}\\)".replace(",", "")
        w1 = f"\\({a + 500:,}\\)".replace(",", "")
        w2 = f"\\({a - 500:,}\\)".replace(",", "")
        w3 = f"\\({a + 1000:,}\\)".replace(",", "")
        
        q = make_q(
            tc_1421, name_1421,
            f"The present population of a town is \\({p:,}\\). If the population grows at an annual rate of \\({r}\\%\\), what will be its population after \\({n}\\) years?".replace(",", ""),
            ans, [w1, w2, w3],
            f"Use the growth formula: \\(A = P\\left(1 + \\frac{{R}}{{100}}\\right)^N\\), where \\(P = {p}, R = {r}, N = {n}\\).",
            f"Substitute and compute: \\(A = {p}\\left(1 + \\frac{{{r}}}{{100}}\\right)^{{{n}}} = {p}\\left(\\frac{{{100+r}}}{{100}}\\right)^{{{n}}}\\).",
            f"Calculating gives the population \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 14.2.2 Formula for depreciation / decay: A = P(1 - r/100)^N (80 questions)
    # -------------------------------------------------------------
    tc_1422 = "MH-8-MTH-14-14.2.2"
    name_1422 = "Formula for depreciation / decay: A = P(1 - r/100)^N"
    dep_data = [
        (10000, 10, 2, 8100), (20000, 10, 2, 16200), (50000, 10, 2, 40500),
        (40000, 5, 2, 36100), (100000, 10, 2, 81000), (80000, 10, 2, 64800),
        (60000, 10, 2, 48600), (25000, 10, 2, 20250), (50000, 20, 2, 32000),
        (100000, 20, 2, 64000)
    ]
    for i in range(80):
        p, r, n, a = dep_data[i % len(dep_data)]
        ans = f"\\(₹{a:,}\\)".replace(",", "")
        w1 = f"\\(₹{a + 500:,}\\)".replace(",", "")
        w2 = f"\\(₹{a - 500:,}\\)".replace(",", "")
        w3 = f"\\(₹{a + 1000:,}\\)".replace(",", "")
        
        q = make_q(
            tc_1422, name_1422,
            f"A machine was purchased for \\(₹{p:,}\\). If its value depreciates annually at \\({r}\\%\\), find its depreciated value after \\({n}\\) years.".replace(",", ""),
            ans, [w1, w2, w3],
            f"Use the depreciation decay formula: \\(A = P\\left(1 - \\frac{{R}}{{100}}\\right)^N\\), where \\(P = {p}, R = {r}, N = {n}\\).",
            f"Substitute the values: \\(A = {p}\\left(1 - \\frac{{{r}}}{{100}}\\right)^{{{n}}} = {p}\\left(\\frac{{{100-r}}}{{100}}\\right)^{{{n}}}\\).",
            f"Computing gives the depreciated value \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch14_questions()
    print(f"Generated {len(qs)} questions for Chapter 14.")
    out_path = "scripts/mh8_mth_ch14_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
