import json
import random

random.seed(81515)

def build_ch15_questions():
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
    # 15.1.1 Formula and derivation (80 questions)
    # -------------------------------------------------------------
    tc_1511 = "MH-8-MTH-15-15.1.1"
    name_1511 = "Formula and derivation"
    base_heights = [
        (10, 6, 60), (12, 8, 96), (15, 10, 150), (18, 12, 216), (20, 14, 280),
        (25, 16, 400), (30, 20, 600), (14, 9, 126), (16, 11, 176), (22, 15, 330),
        (8, 5, 40), (9, 7, 63), (11, 8, 88), (13, 9, 117), (24, 15, 360),
        (28, 12, 336)
    ]
    for i in range(80):
        b, h, a = base_heights[i % len(base_heights)]
        ans = f"\\({a}\\text{{ cm}}^2\\)"
        w1 = f"\\({a + 10}\\text{{ cm}}^2\\)"
        w2 = f"\\({max(10, a - 10)}\\text{{ cm}}^2\\)"
        w3 = f"\\({a // 2}\\text{{ cm}}^2\\)"
        
        q = make_q(
            tc_1511, name_1511,
            f"Calculate the area of a parallelogram having base \\({b}\\text{{ cm}}\\) and corresponding height \\({h}\\text{{ cm}}\\).",
            ans, [w1, w2, w3],
            f"The area formula for a parallelogram is: \\(\\text{{Area}} = \\text{{Base}} \\times \\text{{Height}}\\).",
            f"Substitute the measurements: \\(\\text{{Area}} = {b} \\times {h}\\).",
            f"Multiplying yields \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 15.1.2 Finding height or base when area is given (80 questions)
    # -------------------------------------------------------------
    tc_1512 = "MH-8-MTH-15-15.1.2"
    name_1512 = "Finding height or base when area is given"
    for i in range(80):
        b, h, a = base_heights[i % len(base_heights)]
        ans = f"\\({h}\\text{{ cm}}\\)"
        w1 = f"\\({h + 2}\\text{{ cm}}\\)"
        w2 = f"\\({max(1, h - 2)}\\text{{ cm}}\\)"
        w3 = f"\\({h * 2}\\text{{ cm}}\\)"
        
        q = make_q(
            tc_1512, name_1512,
            f"The area of a parallelogram is \\({a}\\text{{ cm}}^2\\). If its base measures \\({b}\\text{{ cm}}\\), what is its corresponding height?",
            ans, [w1, w2, w3],
            f"From \\(\\text{{Area}} = \\text{{Base}} \\times \\text{{Height}}\\), the height is \\(\\text{{Height}} = \\frac{{\\text{{Area}}}}{{\\text{{Base}}}}\\).",
            f"Substitute \\(\\text{{Area}} = {a}\\) and \\(\\text{{Base}} = {b}\\): \\(\\text{{Height}} = \\frac{{{a}}}{{{b}}}\\).",
            f"Dividing gives \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 15.2.1 Formula: 1/2 * d1 * d2 (80 questions)
    # -------------------------------------------------------------
    tc_1521 = "MH-8-MTH-15-15.2.1"
    name_1521 = "Formula: 1/2 * d1 * d2"
    diags_data = [
        (12, 16, 96), (10, 14, 70), (16, 20, 160), (18, 24, 216), (22, 30, 330),
        (8, 12, 48), (14, 18, 126), (20, 26, 260), (15, 20, 150), (24, 32, 384),
        (10, 12, 60), (12, 14, 84), (16, 18, 144), (20, 24, 240), (25, 30, 375),
        (30, 40, 600)
    ]
    for i in range(80):
        d1, d2, a = diags_data[i % len(diags_data)]
        ans = f"\\({a}\\text{{ cm}}^2\\)"
        w1 = f"\\({a * 2}\\text{{ cm}}^2\\)"
        w2 = f"\\({a + 10}\\text{{ cm}}^2\\)"
        w3 = f"\\({max(10, a - 10)}\\text{{ cm}}^2\\)"
        
        q = make_q(
            tc_1521, name_1521,
            f"Find the area of a rhombus whose diagonals measure \\({d1}\\text{{ cm}}\\) and \\({d2}\\text{{ cm}}\\).",
            ans, [w1, w2, w3],
            f"The area of a rhombus is given by \\(\\text{{Area}} = \\frac{{1}}{{2}} \\times d_1 \\times d_2\\).",
            f"Substitute the diagonal lengths: \\(\\text{{Area}} = \\frac{{1}}{{2}} \\times {d1} \\times {d2}\\).",
            f"Simplifying the product gives \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 15.2.2 Pythagoras theorem relation with rhombus sides and half diagonals (80 questions)
    # -------------------------------------------------------------
    tc_1522 = "MH-8-MTH-15-15.2.2"
    name_1522 = "Pythagoras theorem relation with rhombus sides and half diagonals"
    triplets = [
        (12, 16, 10), (16, 30, 17), (10, 24, 13), (20, 48, 26), (14, 48, 25),
        (18, 24, 15), (6, 8, 5), (30, 40, 25), (24, 70, 37), (16, 63, 65)
    ]
    for i in range(80):
        d1, d2, side = triplets[i % len(triplets)]
        h1 = d1 // 2
        h2 = d2 // 2
        ans = f"\\({side}\\text{{ cm}}\\)"
        w1 = f"\\({side + 2}\\text{{ cm}}\\)"
        w2 = f"\\({max(1, side - 2)}\\text{{ cm}}\\)"
        w3 = f"\\({side + 5}\\text{{ cm}}\\)"
        
        q = make_q(
            tc_1522, name_1522,
            f"The diagonals of a rhombus measure \\({d1}\\text{{ cm}}\\) and \\({d2}\\text{{ cm}}\\). Using the property that diagonals bisect each other perpendicularly, find the side length of the rhombus.",
            ans, [w1, w2, w3],
            f"Diagonals bisect at right angles, creating four congruent right triangles with legs \\(\\frac{{d_1}}{{2}} = {h1}\\text{{ cm}}\\) and \\(\\frac{{d_2}}{{2}} = {h2}\\text{{ cm}}\\).",
            f"Apply the Pythagoras theorem: \\(\\text{{side}}^2 = {h1}^2 + {h2}^2 = {h1**2} + {h2**2} = {side**2}\\).",
            f"Taking the square root gives \\(\\text{{side}} = {ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 15.3.1 Formula: 1/2 * (a + b) * h (80 questions)
    # -------------------------------------------------------------
    tc_1531 = "MH-8-MTH-15-15.3.1"
    name_1531 = "Formula: 1/2 * (a + b) * h"
    trap_data = [
        (10, 14, 6, 72), (12, 18, 8, 120), (15, 25, 10, 200), (8, 12, 5, 50),
        (14, 20, 7, 119), (16, 24, 9, 180), (20, 30, 12, 300), (18, 22, 10, 200),
        (22, 28, 8, 200), (25, 35, 12, 360), (30, 40, 15, 525), (12, 16, 6, 84),
        (15, 21, 8, 144), (18, 26, 10, 220), (24, 36, 14, 420), (10, 16, 7, 91)
    ]
    for i in range(80):
        p1, p2, h, a = trap_data[i % len(trap_data)]
        ans = f"\\({a}\\text{{ cm}}^2\\)"
        w1 = f"\\({a + 15}\\text{{ cm}}^2\\)"
        w2 = f"\\({max(10, a - 15)}\\text{{ cm}}^2\\)"
        w3 = f"\\({a * 2}\\text{{ cm}}^2\\)"
        
        q = make_q(
            tc_1531, name_1531,
            f"Find the area of a trapezium whose parallel sides measure \\({p1}\\text{{ cm}}\\) and \\({p2}\\text{{ cm}}\\), with perpendicular distance between them \\({h}\\text{{ cm}}\\).",
            ans, [w1, w2, w3],
            f"The area formula for a trapezium is: \\(\\text{{Area}} = \\frac{{1}}{{2}} \\times (a + b) \\times h\\).",
            f"Substitute the dimensions: \\(\\text{{Area}} = \\frac{{1}}{{2}} \\times ({p1} + {p2}) \\times {h} = \\frac{{1}}{{2}} \\times {p1+p2} \\times {h}\\).",
            f"Calculating gives \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 15.3.2 Word problems on cross-sectional canal and road areas (80 questions)
    # -------------------------------------------------------------
    tc_1532 = "MH-8-MTH-15-15.3.2"
    name_1532 = "Word problems on cross-sectional canal and road areas"
    for i in range(80):
        top_w = 8 + (i % 8)
        bot_w = 4 + (i % 6)
        depth = 3 + (i % 4)
        area = int(0.5 * (top_w + bot_w) * depth)
        
        ans = f"\\({area}\\text{{ m}}^2\\)"
        w1 = f"\\({area + 5}\\text{{ m}}^2\\)"
        w2 = f"\\({max(2, area - 5)}\\text{{ m}}^2\\)"
        w3 = f"\\({area * 2}\\text{{ m}}^2\\)"
        
        q = make_q(
            tc_1532, name_1532,
            f"A drainage canal has a cross-section in the shape of a trapezium. The top width is \\({top_w}\\text{{ m}}\\), bottom width is \\({bot_w}\\text{{ m}}\\), and depth is \\({depth}\\text{{ m}}\\). Find its cross-sectional area.",
            ans, [w1, w2, w3],
            f"The canal cross-section is a trapezium with parallel sides \\(a = {top_w}\\text{{ m}}, b = {bot_w}\\text{{ m}}\\) and height \\(h = {depth}\\text{{ m}}\\).",
            f"Apply the trapezium area formula: \\(\\text{{Area}} = \\frac{{1}}{{2}} \\times ({top_w} + {bot_w}) \\times {depth}\\).",
            f"Evaluating the arithmetic gives \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 15.4.1 Semi-perimeter s = (a+b+c)/2 (80 questions)
    # -------------------------------------------------------------
    tc_1541 = "MH-8-MTH-15-15.4.1"
    name_1541 = "Semi-perimeter s = (a+b+c)/2"
    tri_sides = [
        (13, 14, 15, 21), (5, 12, 13, 15), (6, 8, 10, 12), (9, 10, 11, 15),
        (15, 20, 25, 30), (12, 16, 20, 24), (7, 24, 25, 28), (8, 15, 17, 20),
        (10, 17, 21, 24), (20, 21, 29, 35), (11, 13, 14, 19), (16, 25, 39, 40),
        (14, 16, 18, 24), (18, 24, 30, 36), (12, 15, 21, 24), (21, 28, 35, 42)
    ]
    for i in range(80):
        s1, s2, s3, semi = tri_sides[i % len(tri_sides)]
        perim = s1 + s2 + s3
        ans = f"\\({semi}\\text{{ cm}}\\)"
        w1 = f"\\({perim}\\text{{ cm}}\\)"
        w2 = f"\\({semi + 2}\\text{{ cm}}\\)"
        w3 = f"\\({max(1, semi - 2)}\\text{{ cm}}\\)"
        
        q = make_q(
            tc_1541, name_1541,
            f"Find the semi-perimeter \\(s\\) of a triangle having side lengths \\({s1}\\text{{ cm}}\\), \\({s2}\\text{{ cm}}\\), and \\({s3}\\text{{ cm}}\\).",
            ans, [w1, w2, w3],
            f"Semi-perimeter \\(s\\) is half of the total perimeter: \\(s = \\frac{{a + b + c}}{{2}}\\).",
            f"Add the side lengths: \\(a + b + c = {s1} + {s2} + {s3} = {perim}\\text{{ cm}}\\).",
            f"Divide by 2: \\(s = \\frac{{{perim}}}{{2}} = {ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 15.4.2 Formula: A = √[s(s-a)(s-b)(s-c)] (80 questions)
    # -------------------------------------------------------------
    tc_1542 = "MH-8-MTH-15-15.4.2"
    name_1542 = "Formula: A = √[s(s-a)(s-b)(s-c)]"
    heron_triangles = [
        (13, 14, 15, 84), (5, 12, 13, 30), (6, 8, 10, 24), (15, 20, 25, 150),
        (7, 24, 25, 84), (8, 15, 17, 60), (10, 17, 21, 84), (20, 21, 29, 210),
        (12, 16, 20, 96), (18, 24, 30, 216), (21, 28, 35, 294), (9, 12, 15, 54)
    ]
    for i in range(80):
        s1, s2, s3, area = heron_triangles[i % len(heron_triangles)]
        ans = f"\\({area}\\text{{ cm}}^2\\)"
        w1 = f"\\({area + 12}\\text{{ cm}}^2\\)"
        w2 = f"\\({max(10, area - 12)}\\text{{ cm}}^2\\)"
        w3 = f"\\({area * 2}\\text{{ cm}}^2\\)"
        
        q = make_q(
            tc_1542, name_1542,
            f"Use Heron's formula to find the area of a triangle with sides \\({s1}\\text{{ cm}}\\), \\({s2}\\text{{ cm}}\\), and \\({s3}\\text{{ cm}}\\).",
            ans, [w1, w2, w3],
            f"Recall Heron's area formula: \\(A = \\sqrt{{s(s - a)(s - b)(s - c)}}\\).",
            f"Calculate \\(s = \\frac{{{s1} + {s2} + {s3}}}{{2}}\\) and the differences \\((s-a), (s-b), (s-c)\\).",
            f"Multiply the terms under the square root and extract the root to get \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 15.5.1 Dividing plots into triangles and trapeziums (80 questions)
    # -------------------------------------------------------------
    tc_1551 = "MH-8-MTH-15-15.5.1"
    name_1551 = "Dividing plots into triangles and trapeziums"
    plot_q1 = [
        ("To find the area of an irregular land plot or polygon, what standard surveying technique is used?", "Decomposing the polygon into smaller standard geometric figures (triangles and trapeziums)", ["Approximating it as a single circle", "Measuring only the perimeter and dividing by 4", "Assuming it is a perfect square"]),
        ("In surveying a land plot, perpendicular offsets are drawn from boundaries to a central baseline to form:", "Right-angled triangles and trapeziums", ["Concentric circles", "Regular hexagons", "Spheres"]),
        ("Why are irregular land plots partitioned specifically into triangles and trapeziums?", "Because exact geometric area formulas exist for triangles and trapeziums", ["Because they use fewer numbers", "Because angles do not need measurement", "Because irregular shapes have no area"]),
        ("When survey offsets divide a field into 3 triangles and 2 trapeziums, the total plot area is:", "The sum of the areas of the 3 triangles and 2 trapeziums", ["The product of all individual areas", "The average area of the shapes", "The area of the largest shape only"])
    ]
    for i in range(80):
        ctx, ans, wrongs = plot_q1[i % len(plot_q1)]
        q = make_q(
            tc_1551, name_1551,
            f"Surveying of land plots: {ctx}",
            ans, wrongs,
            "Review field-book land surveying and polygon decomposition principles in geometry.",
            "Complex polygonal regions are decomposed into non-overlapping elementary triangles and trapeziums.",
            f"Hence, '{ans}' is the correct procedure.",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 15.5.2 Summing individual region areas (80 questions)
    # -------------------------------------------------------------
    tc_1552 = "MH-8-MTH-15-15.5.2"
    name_1552 = "Summing individual region areas"
    plot_sums = [
        ([120, 150, 180], 450), ([200, 250, 300, 150], 900), ([80, 110, 130, 90], 410),
        ([150, 220, 180, 150], 700), ([300, 400, 350], 1050), ([100, 140, 160, 200], 600),
        ([250, 350, 400], 1000), ([90, 120, 150, 140], 500), ([160, 240, 200], 600),
        ([180, 220, 260, 140], 800)
    ]
    for i in range(80):
        parts, total_area = plot_sums[i % len(plot_sums)]
        parts_str = " + ".join([f"{p}\\text{{ m}}^2" for p in parts])
        ans = f"\\({total_area}\\text{{ m}}^2\\)"
        w1 = f"\\({total_area + 50}\\text{{ m}}^2\\)"
        w2 = f"\\({max(50, total_area - 50)}\\text{{ m}}^2\\)"
        w3 = f"\\({total_area + 100}\\text{{ m}}^2\\)"
        
        q = make_q(
            tc_1552, name_1552,
            f"An irregular field plot is partitioned into sub-regions with calculated individual areas: \\({parts_str}\\). What is the total area of the field?",
            ans, [w1, w2, w3],
            "By the area addition postulate, the total area of a non-overlapping composite polygon is the sum of its constituent component areas.",
            f"Add the individual region areas together: \\({' + '.join(map(str, parts))}\\).",
            f"The total area of the plot is \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch15_questions()
    print(f"Generated {len(qs)} questions for Chapter 15.")
    out_path = "scripts/mh8_mth_ch15_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
