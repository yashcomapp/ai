import json
import random
from math import gcd

random.seed(8107)

def build_ch7_questions():
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

    # 7.1.1 Observing similarity in change: Dimension scaling (need 39)
    tc = "CBSE-8-MGP1-7-7.1.1"
    name = "Observing similarity in change: Dimension scaling"
    for i in range(39):
        scale = 2 + (i % 5)
        scale_sq = scale * scale
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"If all linear dimensions (length and width) of a rectangle are scaled by a factor of \\({scale}\\), by what factor does its area scale?",
            f"\\({scale_sq}\\)",
            [f"\\({scale}\\)", f"\\({2 * scale}\\)", f"\\({scale ** 3}\\)"],
            f"Area is a two-dimensional quantity: \\(\\text{{Area}} = \\text{{length}} \\times \\text{{width}}\\).",
            f"When both length and width scale by \\({scale}\\), the new area is \\(({scale} \\times L) \\times ({scale} \\times W) = {scale}^2 \\times (L \\times W) = {scale_sq} \\times \\text{{Area}}\\).",
            f"Therefore, the area scales by a factor of \\({scale_sq}\\).",
            d, v
        )
        questions.append(q)

    # 7.1.2 Ratios in simplest form (reducing by HCF) (need 39)
    tc = "CBSE-8-MGP1-7-7.1.2"
    name = "Ratios in simplest form (reducing by HCF)"
    for i in range(39):
        hcf = 3 + (i % 6)
        r1 = 2 + (i % 4)
        r2 = 5 + (i % 5)
        if r1 == r2: r2 += 1
        a = r1 * hcf
        b = r2 * hcf
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Express the ratio \\({a} : {b}\\) in its simplest (irreducible) form.",
            f"\\({r1} : {r2}\\)",
            [f"\\({r1 + 1} : {r2}\\)", f"\\({r1} : {r2 + 1}\\)", f"\\({b} : {a}\\)"],
            f"Find the Highest Common Factor (HCF) of \\({a}\\) and \\({b}\\): \\(\\text{{HCF}}({a}, {b}) = {hcf}\\).",
            f"Divide both antecedent and consequent by their HCF: \\(\\frac{{{a}}}{{{hcf}}} : \\frac{{{b}}}{{{hcf}}} = {r1} : {r2}\\).",
            f"Hence, the simplest form is \\({r1} : {r2}\\).",
            d, v
        )
        questions.append(q)

    # 7.2.1 Comparing sweetness/taste/mixtures using ratios (need 39)
    tc = "CBSE-8-MGP1-7-7.2.1"
    name = "Comparing sweetness/taste/mixtures using ratios"
    for i in range(39):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "Mixture A has 3 spoons of sugar in 5 cups of water (ratio 3:5), and Mixture B has 4 spoons of sugar in 6 cups of water (ratio 4:6 = 2:3). Which mixture is sweeter?",
            "Mixture B (concentration \\(\\frac{2}{3} \\approx 0.67\\) is greater than Mixture A \\(\\frac{3}{5} = 0.60\\))",
            [
                "Mixture A (concentration 0.60 is greater)",
                "Both mixtures are equally sweet",
                "Sweetness cannot be compared using ratios"
            ],
            f"Convert each mixture ratio (solute to solvent) to a decimal fraction to compare concentrations.",
            f"Mixture A: \\(\\frac{{3}}{{5}} = 0.60\\). Mixture B: \\(\\frac{{4}}{{6}} = \\frac{{2}}{{3}} \\approx 0.67\\).",
            f"Since \\(0.67 > 0.60\\), Mixture B has a higher sugar concentration and is sweeter.",
            d, v
        )
        questions.append(q)

    # 7.2.2 Unit conversions for ratio consistency (need 39)
    tc = "CBSE-8-MGP1-7-7.2.2"
    name = "Unit conversions for ratio consistency"
    for i in range(39):
        m = 2 + (i % 5)
        cm = m * 100
        comp_cm = 40 + (i % 30)
        g = gcd(cm, comp_cm)
        r1 = cm // g
        r2 = comp_cm // g
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find the ratio of \\({m}\\text{{ m}}\\) to \\({comp_cm}\\text{{ cm}}\\) in simplest form.",
            f"\\({r1} : {r2}\\)",
            [f"\\({m} : {comp_cm}\\)", f"\\({r2} : {r1}\\)", f"\\({r1 + 2} : {r2}\\)"],
            f"Two quantities must be in the exact same units before computing their ratio. Convert \\({m}\\text{{ m}}\\) to centimeters: \\({m} \\times 100 = {cm}\\text{{ cm}}\\).",
            f"Form the ratio: \\({cm} : {comp_cm}\\). Divide by \\(\\gcd({cm}, {comp_cm}) = {g}\\).",
            f"Thus, the simplest ratio is \\({r1} : {r2}\\).",
            d, v
        )
        questions.append(q)

    # 7.3.1 Checking proportion: Equivalence & cross-product (ad = bc) (need 39)
    tc = "CBSE-8-MGP1-7-7.3.1"
    name = "Checking proportion: Equivalence & cross-product (ad = bc)"
    for i in range(39):
        a, b = 2 + (i % 4), 3 + (i % 3)
        k = 4 + (i % 3)
        c, d_val = a * k, b * k
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Determine whether \\({a}, {b}, {c}, {d_val}\\) are in proportion by evaluating the cross-product of extremes and means.",
            f"Yes, because \\(\\text{{Product of Extremes}} = {a} \\times {d_val} = {a * d_val}\\) equals \\(\\text{{Product of Means}} = {b} \\times {c} = {b * c}\\).",
            [
                f"No, because \\({a} \\times {d_val} \\neq {b} \\times {c}\\).",
                f"No, because the terms are not consecutive integers.",
                "Cannot be determined without a fifth value."
            ],
            f"Four numbers \\(a, b, c, d\\) are in proportion \\(a : b :: c : d\\) if and only if \\(a \\times d = b \\times c\\).",
            f"Extremes product: \\({a} \\times {d_val} = {a * d_val}\\). Means product: \\({b} \\times {c} = {b * c}\\).",
            f"Since both products are equal, the four numbers are in proportion.",
            d, v
        )
        questions.append(q)

    # 7.3.2 Finding missing terms in proportions (need 39)
    tc = "CBSE-8-MGP1-7-7.3.2"
    name = "Finding missing terms in proportions"
    for i in range(39):
        a = 3 + (i % 5)
        b = 5 + (i % 4)
        k = 2 + (i % 4)
        c = a * k
        missing_x = b * k
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find the value of \\(x\\) in the proportion: \\({a} : {b} :: {c} : x\\).",
            f"\\({missing_x}\\)",
            [f"\\({missing_x + 2}\\)", f"\\({missing_x - 2}\\)", f"\\({missing_x * 2}\\)"],
            f"In any proportion \\(a : b :: c : x\\), the product of extremes equals the product of means: \\(a \\times x = b \\times c\\).",
            f"Substitute values: \\({a}x = {b} \\times {c} = {b * c}\\).",
            f"Solve for \\(x\\): \\(x = \\frac{{{b * c}}}{{{a}}} = {missing_x}\\).",
            d, v
        )
        questions.append(q)

    # 7.4.1 Trairasika method for finding the fourth proportional (need 39)
    tc = "CBSE-8-MGP1-7-7.4.1"
    name = "Trairasika method for finding the fourth proportional"
    for i in range(39):
        p1 = 4 + (i % 4)
        cost1 = p1 * 15
        p2 = 7 + (i % 5)
        ans_cost = p2 * 15
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Using the ancient Indian Rule of Three (Trairasika), if \\({p1}\\) notebooks cost ₹\\({cost1}\\), what will \\({p2}\\) notebooks cost under direct proportion?",
            f"₹\\({ans_cost}\\)",
            [f"₹\\({ans_cost + 15}\\)", f"₹\\({ans_cost - 15}\\)", f"₹\\({p2 * 20}\\)"],
            f"In Trairasika (Rule of Three), three quantities are known: Pramana (measure) = \\({p1}\\), Phala (fruit/cost) = \\({cost1}\\), and Iccha (desire) = \\({p2}\\).",
            f"The formula for Iccha-phala (result) is \\(\\frac{{\\text{{Phala}} \\times \\text{{Iccha}}}}{{\\text{{Pramana}}}} = \\frac{{{cost1} \\times {p2}}}{{{p1}}}\\).",
            f"Calculate: \\(15 \\times {p2} = {ans_cost}\\). Thus, the cost is ₹\\({ans_cost}\\).",
            d, v
        )
        questions.append(q)

    # 7.4.2 Direct proportion word problems (need 39)
    tc = "CBSE-8-MGP1-7-7.4.2"
    name = "Direct proportion word problems"
    for i in range(39):
        dist = 60 + (i % 20) * 10
        time = 2
        speed = dist // time
        t2 = 5
        ans_dist = speed * t2
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"A car travels \\({dist}\\text{{ km}}\\) in \\({time}\\text{{ hours}}\\) at a constant speed. How far will it travel in \\({t2}\\text{{ hours}}\\) under direct variation?",
            f"\\({ans_dist}\\text{{ km}}\\)",
            [f"\\({ans_dist - 30}\\text{{ km}}\\)", f"\\({ans_dist + 30}\\text{{ km}}\\)", f"\\({dist * 3}\\text{{ km}}\\)"],
            f"At constant speed, distance is directly proportional to time: \\(\\frac{{d_1}}{{t_1}} = \\frac{{d_2}}{{t_2}}\\).",
            f"Substitute: \\(\\frac{{{dist}}}{{{time}}} = \\frac{{d_2}}{{{t2}}} \\implies {speed} = \\frac{{d_2}}{{{t2}}}\\).",
            f"Solve for \\(d_2\\): \\(d_2 = {speed} \\times {t2} = {ans_dist}\\text{{ km}}\\).",
            d, v
        )
        questions.append(q)

    # 7.5.1 Dividing total amounts into parts proportional to ratio (need 39)
    tc = "CBSE-8-MGP1-7-7.5.1"
    name = "Dividing total amounts into parts proportional to ratio"
    for i in range(39):
        r1, r2 = 2 + (i % 3), 3 + (i % 4)
        sum_r = r1 + r2
        mult = 50 + (i % 10) * 10
        total = sum_r * mult
        part1 = r1 * mult
        part2 = r2 * mult
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Divide ₹\\({total}\\) between \\(A\\) and \\(B\\) in the ratio \\({r1} : {r2}\\). How much does \\(A\\) receive?",
            f"₹\\({part1}\\)",
            [f"₹\\({part2}\\)", f"₹\\({part1 + 50}\\)", f"₹\\({total // 2}\\)"],
            f"Sum of the ratio terms: \\({r1} + {r2} = {sum_r}\\).",
            f"Calculate \\(A\\)'s share: \\(\\frac{{{r1}}}{{{sum_r}}} \\times {total} = {r1} \\times {mult} = {part1}\\).",
            f"Hence, \\(A\\) receives ₹\\({part1}\\).",
            d, v
        )
        questions.append(q)

    # 7.5.2 Difference between parts, ratio comparisons and multi-way sharing (need 39)
    tc = "CBSE-8-MGP1-7-7.5.2"
    name = "Difference between parts, ratio comparisons and multi-way sharing"
    for i in range(39):
        r1, r2 = 3, 5
        diff_r = r2 - r1  # 2
        unit_val = 20 + i * 5
        diff_val = diff_r * unit_val
        total_val = (r1 + r2) * unit_val
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Two quantities are in the ratio \\(3 : 5\\). If the second quantity exceeds the first by \\({diff_val}\\), find the sum of the two quantities.",
            f"\\({total_val}\\)",
            [f"\\({total_val - 40}\\)", f"\\({total_val + 40}\\)", f"\\({diff_val * 2}\\)"],
            f"Let the two quantities be \\(3x\\) and \\(5x\\). Their difference is \\(5x - 3x = 2x = {diff_val}\\), which gives \\(x = {unit_val}\\).",
            f"The sum of both quantities is \\(3x + 5x = 8x\\).",
            f"Calculate the sum: \\(8 \\times {unit_val} = {total_val}\\).",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch7_questions()
    print(f"Generated {len(qs)} questions for Chapter 7.")
    with open("scripts/cbse8_mgp1_ch7_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/cbse8_mgp1_ch7_topup.json")
