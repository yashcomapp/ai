import json
import random

random.seed(81111)

def build_ch11_questions():
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
    # 11.1.1 Mean formula: X̄ = Σx / N (80 questions)
    # -------------------------------------------------------------
    tc_1111 = "MH-8-MTH-11-11.1.1"
    name_1111 = "Mean formula: X̄ = Σx / N"
    data_sets = [
        ([10, 20, 30, 40, 50], 30), ([12, 14, 16, 18, 20], 16), ([5, 10, 15, 20, 25], 15),
        ([4, 6, 8, 10, 12, 14], 9), ([7, 9, 11, 13, 15], 11), ([20, 25, 30, 35, 40], 30),
        ([15, 18, 21, 24, 27], 21), ([8, 12, 16, 20, 24], 16), ([11, 13, 15, 17, 19], 15),
        ([14, 17, 20, 23, 26], 20), ([10, 15, 20, 25, 30, 35], 22.5), ([6, 12, 18, 24, 30], 18),
        ([22, 24, 26, 28, 30], 26), ([13, 15, 17, 19, 21], 17), ([9, 11, 13, 15, 17], 13),
        ([25, 30, 35, 40, 45], 35)
    ]
    for i in range(80):
        nums, mean_val = data_sets[i % len(data_sets)]
        sum_val = sum(nums)
        n = len(nums)
        nums_str = ", ".join(map(str, nums))
        
        ans = f"\\({mean_val}\\)"
        w1 = f"\\({mean_val + 2}\\)"
        w2 = f"\\({max(1.0, mean_val - 2)}\\)"
        w3 = f"\\({mean_val + 5}\\)"
        
        q = make_q(
            tc_1111, name_1111,
            f"Calculate the arithmetic mean of the following observation set: \\({nums_str}\\).",
            ans, [w1, w2, w3],
            f"Use the arithmetic mean formula: \\(\\bar{{X}} = \\frac{{\\sum x}}{{N}}\\), where \\(\\sum x\\) is the sum of observations and \\(N\\) is the count.",
            f"Sum of observations: \\(\\sum x = {' + '.join(map(str, nums))} = {sum_val}\\), with \\(N = {n}\\).",
            f"Calculate: \\(\\bar{{X}} = \\frac{{{sum_val}}}{{{n}}} = {mean_val}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 11.1.2 Weighted mean calculations using frequency tables Σ(f * x) / N (80 questions)
    # -------------------------------------------------------------
    tc_1112 = "MH-8-MTH-11-11.1.2"
    name_1112 = "Weighted mean calculations using frequency tables Σ(f * x) / N"
    table_sets = [
        ([(2, 3), (4, 2), (6, 5)], 4.4), ([(10, 2), (20, 3), (30, 5)], 23.0),
        ([(5, 4), (10, 3), (15, 3)], 9.5), ([(1, 5), (2, 4), (3, 1)], 1.6),
        ([(4, 2), (8, 4), (12, 4)], 8.8), ([(15, 2), (25, 4), (35, 4)], 27.0),
        ([(20, 5), (30, 3), (40, 2)], 27.0), ([(6, 3), (12, 4), (18, 3)], 12.0),
        ([(8, 2), (16, 5), (24, 3)], 16.8), ([(5, 2), (15, 5), (25, 3)], 16.0)
    ]
    for i in range(80):
        pairs, mean_val = table_sets[i % len(table_sets)]
        total_f = sum(f for x, f in pairs)
        total_fx = sum(x * f for x, f in pairs)
        
        tab_desc = ", ".join([f"(x={x}, f={f})" for x, f in pairs])
        ans = f"\\({mean_val}\\)"
        w1 = f"\\({round(mean_val + 1.5, 1)}\\)"
        w2 = f"\\({round(max(1.0, mean_val - 1.5), 1)}\\)"
        w3 = f"\\({round(mean_val + 3.0, 1)}\\)"
        
        q = make_q(
            tc_1112, name_1112,
            f"Given the frequency distribution data {tab_desc}, calculate the mean using \\(\\bar{{X}} = \\frac{{\\sum (f \\times x)}}{{N}}\\).",
            ans, [w1, w2, w3],
            f"Calculate the product \\(f \\times x\\) for each observation and sum them: \\(\\sum (f \\times x) = {total_fx}\\).",
            f"Find the total frequency: \\(N = \\sum f = {total_f}\\).",
            f"Divide total \\(fx\\) by \\(N\\): \\(\\bar{{X}} = \\frac{{{total_fx}}}{{{total_f}}} = {mean_val}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 11.2.1 Subdividing bar heights for multiple component data (80 questions)
    # -------------------------------------------------------------
    tc_1121 = "MH-8-MTH-11-11.2.1"
    name_1121 = "Subdividing bar heights for multiple component data"
    bar_q1 = [
        ("In a subdivided bar diagram, the total height of a bar represents:", "The total magnitude/sum of all constituent components", ["Only the highest individual component", "The arithmetic mean of components", "The difference between components"]),
        ("Why are different shades, colors, or hatchings used in each segment of a subdivided bar?", "To clearly distinguish each component category within the total", ["To indicate error margins", "To represent the scale of the x-axis", "Purely for decoration without meaning"]),
        ("If Class 8 has 25 boys and 35 girls, what is the total height of the bar in a subdivided bar diagram?", "60 units (representing total 60 students)", ["35 units", "25 units", "10 units"]),
        ("In a subdivided bar diagram representing agricultural production (Wheat = 40 quintals, Rice = 60 quintals), what is the total bar height?", "100 quintals", ["60 quintals", "40 quintals", "20 quintals"])
    ]
    for i in range(80):
        ctx, ans, wrongs = bar_q1[i % len(bar_q1)]
        q = make_q(
            tc_1121, name_1121,
            f"In graphical statistics: {ctx}",
            ans, wrongs,
            "Recall the construction principles of a subdivided (component) bar diagram.",
            "Each bar corresponds to the total quantity, and it is partitioned into parts proportional to the component values.",
            f"Hence, the correct answer is '{ans}'.",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 11.2.2 Scale and labeling on graph (80 questions)
    # -------------------------------------------------------------
    tc_1122 = "MH-8-MTH-11-11.2.2"
    name_1122 = "Scale and labeling on graph"
    scale_q = [
        ("On a graph paper, if the scale is '1 cm = 10 units', how tall should a bar representing 65 units be drawn?", "6.5 cm", ["65 cm", "6.0 cm", "7.0 cm"]),
        ("If the scale on the Y-axis is '1 cm = 50 students', what value does a bar of height 7 cm represent?", "350 students", ["50 students", "70 students", "500 students"]),
        ("Where is the chosen scale normally written on a statistical graph?", "In the top right corner of the graph sheet", ["At the origin (0, 0)", "Along the bottom margin", "Behind the sheet"]),
        ("On which axis are the categorical entities (such as years, classes, or towns) plotted in a vertical bar diagram?", "X-axis (Horizontal axis)", ["Y-axis (Vertical axis)", "Z-axis", "Secondary axis"])
    ]
    for i in range(80):
        ctx, ans, wrongs = scale_q[i % len(scale_q)]
        q = make_q(
            tc_1122, name_1122,
            f"Statistical graphing standard: {ctx}",
            ans, wrongs,
            "Review graph plotting rules and coordinate axis conventions in Balbharti statistics.",
            "The scale specifies how many units each division (centimeter) represents, typically written at the upper right.",
            f"Therefore, the correct specification is '{ans}'.",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 11.3.1 Converting component frequencies to percentages (100%) (80 questions)
    # -------------------------------------------------------------
    tc_1131 = "MH-8-MTH-11-11.3.1"
    name_1131 = "Converting component frequencies to percentages (100%)"
    pct_sets = [
        (30, 50, 60), (20, 80, 25), (45, 60, 75), (15, 60, 25), (40, 200, 20),
        (50, 200, 25), (75, 100, 75), (36, 120, 30), (48, 160, 30), (35, 70, 50),
        (18, 90, 20), (28, 70, 40), (60, 150, 40), (64, 80, 80), (12, 40, 30)
    ]
    for i in range(80):
        part, total, pct = pct_sets[i % len(pct_sets)]
        ans = f"\\({pct}\\%\\)"
        w1 = f"\\({pct + 5}\\%\\)"
        w2 = f"\\({max(1, pct - 5)}\\%\\)"
        w3 = f"\\({pct + 10}\\%\\)"
        
        q = make_q(
            tc_1131, name_1131,
            f"In a survey of \\({total}\\) residents, \\({part}\\) prefer cycling. Convert this component frequency to a percentage for a percentage bar diagram.",
            ans, [w1, w2, w3],
            f"Use the percentage conversion formula: \\(\\text{{Percentage}} = \\left(\\frac{{\\text{{Component Frequency}}}}{{\\text{{Total Frequency}}}}\\right) \\times 100\\).",
            f"Substitute the figures: \\(\\left(\\frac{{{part}}}{{{total}}}\\right) \\times 100\\).",
            f"Simplifying the fraction gives \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 11.3.2 Constructing percentage bars and comparative analysis (80 questions)
    # -------------------------------------------------------------
    tc_1132 = "MH-8-MTH-11-11.3.2"
    name_1132 = "Constructing percentage bars and comparative analysis"
    pct_bars = [
        ("What is the uniform total height of EVERY bar in a percentage bar diagram?", "100% (or 10 cm representing 100%)", ["It varies according to sample size", "50%", "The sum of all totals combined"]),
        ("Why are percentage bar diagrams particularly advantageous for comparing two datasets with different total sizes?", "Because normalizing to 100% allows direct relative comparison regardless of unequal totals", ["Because it eliminates the need to draw bars", "Because it only uses whole numbers", "Because total sample size does not matter in statistics"]),
        ("In a school of 200 boys (60% passed) and 100 girls (70% passed), which group had a higher pass rate when viewed on a percentage bar diagram?", "Girls (70% vs 60%)", ["Boys (because 120 boys passed vs 70 girls)", "Both are equal", "Cannot be determined without raw marks"]),
        ("In a percentage bar, if component A is 35% and component B is 45%, what is the percentage of the remaining component C?", "20%", ["10%", "25%", "30%"])
    ]
    for i in range(80):
        ctx, ans, wrongs = pct_bars[i % len(pct_bars)]
        q = make_q(
            tc_1132, name_1132,
            f"Percentage bar diagram methodology: {ctx}",
            ans, wrongs,
            "Recall the definition and construction rules of percentage bar diagrams.",
            "All bars in a percentage bar graph are made of identical height corresponding to 100%, and subdivided proportionally.",
            f"Therefore, the correct conclusion is '{ans}'.",
            diffs[i], vaults[i]
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch11_questions()
    print(f"Generated {len(qs)} questions for Chapter 11.")
    out_path = "scripts/mh8_mth_ch11_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
