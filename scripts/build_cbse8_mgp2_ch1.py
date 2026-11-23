import json
import random

random.seed(8201)

def build_ch1_questions():
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

    # 1.1.1 Converting between fractions, decimals and percentages (need 80)
    tc = "CBSE-8-MGP2-1-1.1.1"
    name = "Converting between fractions, decimals and percentages"
    for i in range(80):
        den = [2, 4, 5, 10, 20, 25, 50][i % 7]
        num = 1 + (i % (den - 1)) if den > 2 else 1
        pct = (num * 100) // den
        dec = round(num / den, 2)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Convert the fraction \\(\\frac{{{num}}}{{{den}}}\\) into its equivalent percentage.",
            f"\\({pct}\\%\\)",
            [f"\\({pct + 5}\\%\\)", f"\\({pct - 5}\\%\\)", f"\\({pct * 2}\\%\\)"],
            f"To convert a fraction to a percentage, multiply the fraction by 100: \\(\\frac{{{num}}}{{{den}}} \\times 100\\%\\).",
            f"Calculate: \\(\\frac{{{num} \\times 100}}{{{den}}} = \\frac{{{num * 100}}}{{{den}}} = {pct}\\%\\).",
            f"Therefore, \\(\\frac{{{num}}}{{{den}}} = {pct}\\%\\).",
            d, v
        )
        questions.append(q)

    # 1.1.2 Fractional and decimal percentage benchmarks (need 80)
    tc = "CBSE-8-MGP2-1-1.1.2"
    name = "Fractional and decimal percentage benchmarks"
    for i in range(80):
        benchmarks = [
            (25, "\\frac{1}{4}", "0.25"),
            (50, "\\frac{1}{2}", "0.5"),
            (75, "\\frac{3}{4}", "0.75"),
            (20, "\\frac{1}{5}", "0.2"),
            (10, "\\frac{1}{10}", "0.1"),
            (12.5, "\\frac{1}{8}", "0.125")
        ]
        p_val, frac_val, dec_val = benchmarks[i % len(benchmarks)]
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"What is the exact fractional benchmark equivalent of \\({p_val}\\%\\)?",
            f"\\({frac_val}\\)",
            ["\\(\\frac{1}{3}\\)", "\\(\\frac{2}{5}\\)", "\\(\\frac{1}{6}\\)"],
            f"By definition of percent (per hundred), \\({p_val}\\% = \\frac{{{p_val}}}{{100}}\\).",
            f"Reduce the fraction by dividing the numerator and denominator by their greatest common divisor.",
            f"This simplifies directly to \\({frac_val}\\).",
            d, v
        )
        questions.append(q)

    # 1.2.1 Finding percentage of a given quantity (need 80)
    tc = "CBSE-8-MGP2-1-1.2.1"
    name = "Finding percentage of a given quantity"
    for i in range(80):
        pct = 10 + (i % 9) * 5
        base = 200 + (i % 15) * 20
        ans = (pct * base) // 100
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Evaluate \\({pct}\\%\\) of \\({base}\\).",
            f"\\({ans}\\)",
            [f"\\({ans + 10}\\)", f"\\({ans - 10}\\)", f"\\({ans * 2}\\)"],
            f"Express the percentage as a fraction with denominator 100: \\(\\frac{{{pct}}}{{100}}\\).",
            f"Multiply by the given quantity: \\(\\frac{{{pct}}}{{100}} \\times {base} = {pct} \\times {base // 100}\\).",
            f"Calculate the product: \\({ans}\\). Thus, \\({pct}\\%\\) of \\({base}\\) is \\({ans}\\).",
            d, v
        )
        questions.append(q)

    # 1.2.2 Percentage increase and decrease calculations (need 80)
    tc = "CBSE-8-MGP2-1-1.2.2"
    name = "Percentage increase and decrease calculations"
    for i in range(80):
        orig = 400 + (i % 10) * 50
        inc_pct = 10 + (i % 6) * 5
        inc_val = (orig * inc_pct) // 100
        new_val = orig + inc_val
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"A salary of ₹\\({orig}\\) is increased by \\({inc_pct}\\%\\). What is the new salary?",
            f"₹\\({new_val}\\)",
            [f"₹\\({new_val + 20}\\)", f"₹\\({new_val - 20}\\)", f"₹\\({orig + inc_pct}\\)"],
            f"Calculate the amount of increase: \\(\\text{{Increase}} = \\frac{{{inc_pct}}}{{100}} \\times {orig} = {inc_val}\\).",
            f"Add the increase to the original amount: \\(\\text{{New Salary}} = {orig} + {inc_val} = {new_val}\\).",
            f"Therefore, the new salary is ₹\\({new_val}\\).",
            d, v
        )
        questions.append(q)

    # 1.3.1 Cost price, selling price, profit and loss percent (need 80)
    tc = "CBSE-8-MGP2-1-1.3.1"
    name = "Cost price, selling price, profit and loss percent"
    for i in range(80):
        cp = 500 + (i % 10) * 50
        p_pct = 10 + (i % 5) * 5
        profit = (cp * p_pct) // 100
        sp = cp + profit
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"An article bought for ₹\\({cp}\\) (CP) is sold for ₹\\({sp}\\) (SP). Calculate the profit percentage.",
            f"\\({p_pct}\\%\\)",
            [f"\\({p_pct + 5}\\%\\)", f"\\({p_pct - 5}\\%\\)", f"\\({p_pct * 2}\\%\\)"],
            f"Find the total profit: \\(\\text{{Profit}} = \\text{{SP}} - \\text{{CP}} = {sp} - {cp} = {profit}\\).",
            f"Calculate the profit percentage based on CP: \\(\\text{{Profit \\%}} = \\frac{{\\text{{Profit}}}}{{\\text{{CP}}}} \\times 100 = \\frac{{{profit}}}{{{cp}}} \\times 100\\).",
            f"Simplify: \\(\\frac{{{profit * 100}}}{{{cp}}} = {p_pct}\\%\\).",
            d, v
        )
        questions.append(q)

    # 1.3.2 Marked price, discount and discount percentage (need 80)
    tc = "CBSE-8-MGP2-1-1.3.2"
    name = "Marked price, discount and discount percentage"
    for i in range(80):
        mp = 800 + (i % 10) * 100
        d_pct = 10 + (i % 5) * 5
        disc = (mp * d_pct) // 100
        sp = mp - disc
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"An item with Marked Price (MP) of ₹\\({mp}\\) is offered at a discount of \\({d_pct}\\%\\). Find the selling price (SP).",
            f"₹\\({sp}\\)",
            [f"₹\\({sp + 30}\\)", f"₹\\({sp - 30}\\)", f"₹\\({mp - d_pct}\\)"],
            f"Calculate the discount amount: \\(\\text{{Discount}} = \\frac{{{d_pct}}}{{100}} \\times {mp} = {disc}\\).",
            f"Subtract the discount from the marked price: \\(\\text{{SP}} = \\text{{MP}} - \\text{{Discount}} = {mp} - {disc} = {sp}\\).",
            f"Hence, the selling price is ₹\\({sp}\\).",
            d, v
        )
        questions.append(q)

    # 1.4.1 Calculating GST added to bill amount (need 80)
    tc = "CBSE-8-MGP2-1-1.4.1"
    name = "Calculating GST added to bill amount"
    for i in range(80):
        price = 1000 + (i % 10) * 100
        gst_pct = [5, 12, 18, 28][i % 4]
        gst_amt = (price * gst_pct) // 100
        total_bill = price + gst_amt
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"A product costs ₹\\({price}\\) before tax. If GST is levied at \\({gst_pct}\\%\\), what is the total bill amount including GST?",
            f"₹\\({total_bill}\\)",
            [f"₹\\({total_bill + 50}\\)", f"₹\\({total_bill - 50}\\)", f"₹\\({price + gst_pct}\\)"],
            f"Calculate the GST amount: \\(\\text{{GST}} = \\frac{{{gst_pct}}}{{100}} \\times {price} = {gst_amt}\\).",
            f"Add the GST to the original price: \\(\\text{{Total Bill}} = {price} + {gst_amt} = {total_bill}\\).",
            f"Therefore, the total bill amount is ₹\\({total_bill}\\).",
            d, v
        )
        questions.append(q)

    # 1.4.2 Finding price before GST was added (need 80)
    tc = "CBSE-8-MGP2-1-1.4.2"
    name = "Finding price before GST was added"
    for i in range(80):
        orig_price = 500 + (i % 10) * 50
        gst_pct = 10
        total_paid = orig_price + (orig_price * gst_pct) // 100
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"An article was purchased for ₹\\({total_paid}\\) including a GST of \\({gst_pct}\\%\\). Find its original price before GST was added.",
            f"₹\\({orig_price}\\)",
            [f"₹\\({orig_price + 30}\\)", f"₹\\({orig_price - 30}\\)", f"₹\\({total_paid - gst_pct}\\)"],
            f"Let the original price before GST be ₹\\(x\\). Then \\(x + \\frac{{{gst_pct}}}{{100}}x = {total_paid}\\).",
            f"Combine terms: \\(\\frac{{110}}{{100}}x = {total_paid} \\implies x = \\frac{{{total_paid} \\times 100}}{{110}}\\).",
            f"Calculate: \\(x = {orig_price}\\). Hence, the price before GST was ₹\\({orig_price}\\).",
            d, v
        )
        questions.append(q)

    # 1.5.1 Simple interest vs compound interest difference (need 80)
    tc = "CBSE-8-MGP2-1-1.5.1"
    name = "Simple interest vs compound interest difference"
    for i in range(80):
        P = 1000 + (i % 10) * 500
        R = 10
        # for 2 years: SI = P*R*2/100, CI = P*(1+R/100)^2 - P
        # CI - SI = P*(R/100)^2
        diff = (P * R * R) // 10000
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"What is the difference between Compound Interest (CI) and Simple Interest (SI) on a principal of ₹\\({P}\\) for 2 years at \\({R}\\%\\) per annum?",
            f"₹\\({diff}\\)",
            [f"₹\\({diff + 10}\\)", f"₹\\({diff - 5}\\)", f"₹\\(0\\)"],
            f"For 2 years, the difference between CI and SI is given by the formula \\(\\text{{CI}} - \\text{{SI}} = P\\left(\\frac{{R}}{{100}}\\right)^2\\).",
            f"Substitute \\(P = {P}\\) and \\(R = {R}\\): \\({P} \\times \\left(\\frac{{{R}}}{{100}}\\right)^2 = {P} \\times \\frac{{{R*R}}}{{10000}}\\).",
            f"Calculate: \\(\\frac{{{P * R * R}}}{{10000}} = {diff}\\). Hence, the difference is ₹\\({diff}\\).",
            d, v
        )
        questions.append(q)

    # 1.5.2 Compound interest formula A = P(1 + r/100)^n (need 80)
    tc = "CBSE-8-MGP2-1-1.5.2"
    name = "Compound interest formula A = P(1 + r/100)^n"
    for i in range(80):
        P = 2000 + (i % 10) * 1000
        R = 10
        n = 2
        A = (P * 121) // 100
        CI = A - P
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Calculate the total compound amount \\(A\\) on a principal of ₹\\({P}\\) for \\({n}\\) years at \\({R}\\%\\) per annum compounded annually.",
            f"₹\\({A}\\)",
            [f"₹\\({A + 100}\\)", f"₹\\({A - 100}\\)", f"₹\\({P + 2 * P * R // 100}\\)"],
            f"Use the compound interest amount formula: \\(A = P\\left(1 + \\frac{{R}}{{100}}\\right)^n\\).",
            f"Substitute \\(P = {P}, R = {R}, n = {n}\\): \\(A = {P}\\left(1 + \\frac{{10}}{{100}}\\right)^2 = {P}\\left(\\frac{{11}}{{10}}\\right)^2 = {P} \\times \\frac{{121}}{{100}}\\).",
            f"Compute: \\({P} \\times 1.21 = {A}\\). Thus, the amount is ₹\\({A}\\).",
            d, v
        )
        questions.append(q)

    # 1.5.3 Compounded half-yearly calculations (need 80)
    tc = "CBSE-8-MGP2-1-1.5.3"
    name = "Compounded half-yearly calculations"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "When interest is compounded HALF-YEARLY, how are the annual interest rate \\(R\\) and time period \\(n\\) years adjusted in the compound interest formula?",
            "Rate becomes \\(\\frac{R}{2}\\%\\) and time becomes \\(2n\\) conversion periods",
            [
                "Rate becomes \\(2R\\%\\) and time becomes \\(\\frac{n}{2}\\)",
                "Rate remains \\(R\\%\\) and time becomes \\(2n\\)",
                "Rate becomes \\(\\frac{R}{4}\\%\\) and time becomes \\(4n\\)"
            ],
            f"In half-yearly compounding, interest is calculated and added to the principal every 6 months (twice a year).",
            f"The annual rate is divided by 2: \\(\\text{{Half-yearly Rate}} = \\frac{{R}}{{2}}\\%\\).",
            f"The number of conversion periods is doubled: \\(\\text{{Periods}} = 2n\\).",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch1_questions()
    print(f"Generated {len(qs)} questions for Chapter 1.")
    with open("scripts/cbse8_mgp2_ch1_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/cbse8_mgp2_ch1_topup.json")
