import json
import random

random.seed(8909)

def build_ch9_questions():
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
    # 9.1.1 Discount = Marked Price - Selling Price (80 questions)
    # -------------------------------------------------------------
    tc_911 = "MH-8-MTH-9-9.1.1"
    name_911 = "Discount = Marked Price - Selling Price"
    items_911 = [
        (500, 420), (800, 720), (1200, 1050), (1500, 1300), (2000, 1750),
        (2500, 2200), (3000, 2600), (450, 380), (650, 580), (950, 850),
        (1600, 1400), (1800, 1550), (2200, 1900), (2800, 2450), (3500, 3100),
        (4000, 3500), (5000, 4250), (6000, 5100), (7500, 6500), (10000, 8800)
    ]
    for i in range(80):
        mp, sp = items_911[i % len(items_911)]
        mult = (i // 20) + 1
        mp_val = mp * mult
        sp_val = sp * mult
        disc = mp_val - sp_val
        
        ans = f"\\(₹{disc}\\)"
        w1 = f"\\(₹{disc + 50}\\)"
        w2 = f"\\(₹{max(10, disc - 50)}\\)"
        w3 = f"\\(₹{disc + 100}\\)"
        
        q = make_q(
            tc_911, name_911,
            f"An article with a Marked Price of \\(₹{mp_val}\\) is sold at a Selling Price of \\(₹{sp_val}\\). Calculate the total discount offered.",
            ans, [w1, w2, w3],
            f"The formula connecting marked price, selling price, and discount is: \\(\\text{{Discount}} = \\text{{Marked Price}} - \\text{{Selling Price}}\\).",
            f"Substitute the given financial amounts: \\(\\text{{Discount}} = ₹{mp_val} - ₹{sp_val}\\).",
            f"Subtracting gives \\(\\text{{Discount}} = {ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 9.1.2 Discount % = (Discount / Marked Price) * 100 (80 questions)
    # -------------------------------------------------------------
    tc_912 = "MH-8-MTH-9-9.1.2"
    name_912 = "Discount % = (Discount / Marked Price) * 100"
    rates_912 = [
        (1000, 100, 10), (500, 50, 10), (800, 120, 15), (1200, 240, 20), (1500, 375, 25),
        (2000, 300, 15), (2500, 500, 20), (600, 90, 15), (400, 48, 12), (500, 90, 18),
        (1000, 150, 15), (2000, 400, 20), (3000, 300, 10), (4000, 800, 20), (5000, 1250, 25),
        (800, 160, 20), (1200, 144, 12), (1600, 320, 20), (2400, 360, 15), (3200, 640, 20)
    ]
    for i in range(80):
        mp, disc, rate = rates_912[i % len(rates_912)]
        ans = f"\\({rate}\\%\\)"
        w1 = f"\\({rate + 5}\\%\\)"
        w2 = f"\\({max(1, rate - 5)}\\%\\)"
        w3 = f"\\({rate * 2}\\%\\)"
        
        q = make_q(
            tc_912, name_912,
            f"The marked price of a shirt is \\(₹{mp}\\) and the discount allowed is \\(₹{disc}\\). Find the discount percentage.",
            ans, [w1, w2, w3],
            f"Use the discount percentage formula: \\(\\text{{Discount \\%}} = \\left(\\frac{{\\text{{Discount}}}}{{\\text{{Marked Price}}}}\\right) \\times 100\\).",
            f"Substitute \\(\\text{{Discount}} = {disc}\\) and \\(\\text{{Marked Price}} = {mp}\\): \\(\\left(\\frac{{{disc}}}{{{mp}}}\\right) \\times 100\\).",
            f"Simplifying the fraction gives \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 9.2.1 Commission definition and rate percent (80 questions)
    # -------------------------------------------------------------
    tc_921 = "MH-8-MTH-9-9.2.1"
    name_921 = "Commission definition and rate percent"
    comm_cases = [
        ("What is the payment made to a middleman/broker for executing a business sale or purchase called?", "Commission", ["Rebate", "Subsidy", "Overhead expense"]),
        ("Commission is generally calculated as a percentage of which financial value?", "Selling Price / Total Turnover Value", ["Cost Price to manufacturer", "Marked Price on catalog", "Net profit only"]),
        ("A person who brings buyer and seller together to execute a property deal is legally known as:", "Commission agent / Broker", ["Wholesaler", "Consumer", "Auditor"]),
        ("When a commission agent charges 2% on a transaction, this 2% is termed:", "Rate of commission", ["Rebate percentage", "Depreciation rate", "Sales tax rate"])
    ]
    for i in range(80):
        ctx, ans, wrongs = comm_cases[i % len(comm_cases)]
        q = make_q(
            tc_921, name_921,
            f"In commercial mathematics: {ctx}",
            ans, wrongs,
            f"Analyze commercial trading practices and standard business terminology.",
            f"The service fee or percentage remuneration paid to an agent or broker for facilitating transactions is called commission.",
            f"Therefore, the correct standard term is '{ans}'.",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 9.2.2 Income calculation of commission agents (80 questions)
    # -------------------------------------------------------------
    tc_922 = "MH-8-MTH-9-9.2.2"
    name_922 = "Income calculation of commission agents"
    agent_sales = [
        (50000, 2), (100000, 3), (250000, 2), (400000, 1.5), (600000, 2),
        (80000, 5), (120000, 4), (150000, 3), (300000, 2.5), (500000, 2),
        (75000, 4), (90000, 3), (200000, 2), (350000, 2), (450000, 1),
        (180000, 5), (240000, 2.5), (320000, 3), (550000, 2), (700000, 1.5)
    ]
    for i in range(80):
        sale, rate = agent_sales[i % len(agent_sales)]
        inc = int(sale * (rate / 100))
        
        ans = f"\\(₹{inc:,}\\)".replace(",", "")
        w1 = f"\\(₹{inc + 500:,}\\)".replace(",", "")
        w2 = f"\\(₹{max(100, inc - 500):,}\\)".replace(",", "")
        w3 = f"\\(₹{inc + 1000:,}\\)".replace(",", "")
        
        q = make_q(
            tc_922, name_922,
            f"A commission agent facilitated the sale of grain worth \\(₹{sale:,}\\) at a commission rate of \\({rate}\\%\\). Calculate the agent's commission income.".replace(",", ""),
            ans, [w1, w2, w3],
            f"The commission amount is computed as: \\(\\text{{Commission}} = \\text{{Total Sale Value}} \\times \\frac{{\\text{{Rate}}}}{{100}}\\).",
            f"Substitute the figures: \\(\\text{{Commission}} = {sale} \\times \\frac{{{rate}}}{{100}}\\).",
            f"Multiplying gives \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 9.3.1 Government subsidy and rebate discounts (80 questions)
    # -------------------------------------------------------------
    tc_931 = "MH-8-MTH-9-9.3.1"
    name_931 = "Government subsidy and rebate discounts"
    rebate_info = [
        ("What is the special concession or discount offered on Khadi and Handloom products sponsored by the government called?", "Rebate", ["Brokerage", "Commission", "Dividend"]),
        ("Who bears the financial cost of a rebate given to consumers during Khadi festival promotions?", "The Government / Khadi Board", ["The retail buyer", "The local bank", "The transport agent"]),
        ("On which price is the government rebate percentage calculated for handloom garments?", "Marked / Sale Price", ["Manufacturing overhead only", "Wholesale tax value", "Profit margin"]),
        ("Rebate on handloom items serves primarily as:", "A promotional subsidy to support traditional weavers and artisans", ["A penalty for late payment", "An import customs duty", "A compound interest penalty"])
    ]
    for i in range(80):
        ctx, ans, wrongs = rebate_info[i % len(rebate_info)]
        q = make_q(
            tc_931, name_931,
            f"In social and retail economics: {ctx}",
            ans, wrongs,
            f"Consider state-supported incentives on cottage and khadi industries.",
            f"A discount given to customers by organisations that is compensated or subsidized by the government is known as a rebate.",
            f"Hence, the correct answer is '{ans}'.",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 9.3.2 Net amount paid by consumer (80 questions)
    # -------------------------------------------------------------
    tc_932 = "MH-8-MTH-9-9.3.2"
    name_932 = "Net amount paid by consumer"
    khadi_items = [
        (1000, 20), (1500, 15), (2000, 25), (2500, 20), (3000, 10),
        (1200, 20), (1800, 25), (2200, 15), (3500, 20), (4000, 12),
        (800, 20), (1600, 25), (2400, 20), (2800, 15), (3200, 25),
        (4500, 20), (5000, 20), (6000, 25), (7500, 20), (8000, 15)
    ]
    for i in range(80):
        bill, r_pct = khadi_items[i % len(khadi_items)]
        reb = int(bill * (r_pct / 100))
        net = bill - reb
        
        ans = f"\\(₹{net}\\)"
        w1 = f"\\(₹{net + reb}\\)"
        w2 = f"\\(₹{net + 100}\\)"
        w3 = f"\\(₹{max(10, net - 100)}\\)"
        
        q = make_q(
            tc_932, name_932,
            f"A customer purchased Khadi clothes with a total bill of \\(₹{bill}\\). If a government rebate of \\({r_pct}\\%\\) is provided, what is the net amount paid by the customer?",
            ans, [w1, w2, w3],
            f"Calculate the total rebate amount: \\(\\text{{Rebate}} = {bill} \\times \\frac{{{r_pct}}}{{100}} = ₹{reb}\\).",
            f"Subtract the rebate from the total cost: \\(\\text{{Net Amount}} = \\text{{Total Bill}} - \\text{{Rebate}} = ₹{bill} - ₹{reb}\\).",
            f"The final amount paid is \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch9_questions()
    print(f"Generated {len(qs)} questions for Chapter 9.")
    out_path = "scripts/mh8_mth_ch9_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
