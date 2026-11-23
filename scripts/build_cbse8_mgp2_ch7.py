import json
import random

random.seed(8207)

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

    # 7.1.1 Area and perimeter of rectangles and squares (need 80)
    tc = "CBSE-8-MGP2-7-7.1.1"
    name = "Area and perimeter of rectangles and squares"
    for i in range(80):
        side = 6 + (i % 15)
        area = side * side
        peri = 4 * side
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"A square garden has a perimeter of \\({peri}\\text{{ m}}\\). What is its total area?",
            f"\\({area}\\text{{ m}}^2\\)",
            [f"\\({area + 12}\\text{{ m}}^2\\)", f"\\({area - 8}\\text{{ m}}^2\\)", f"\\({peri * 2}\\text{{ m}}^2\\)"],
            f"For a square of side \\(s\\), the perimeter is \\(4s = {peri}\\text{{ m}}\\).",
            f"Solve for the side: \\(s = \\frac{{{peri}}}{{4}} = {side}\\text{{ m}}\\).",
            f"Calculate the area: \\(\\text{{Area}} = s^2 = {side}^2 = {area}\\text{{ m}}^2\\).",
            d, v
        )
        questions.append(q)

    # 7.1.2 Area of triangle: 1/2 * base * height (need 80)
    tc = "CBSE-8-MGP2-7-7.1.2"
    name = "Area of triangle: 1/2 * base * height"
    for i in range(80):
        base = 8 + (i % 12) * 2
        height = 5 + (i % 8)
        area = (base * height) // 2
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Calculate the area of a triangle with base \\({base}\\text{{ cm}}\\) and corresponding altitude \\({height}\\text{{ cm}}\\).",
            f"\\({area}\\text{{ cm}}^2\\)",
            [f"\\({base * height}\\text{{ cm}}^2\\)", f"\\({area + 6}\\text{{ cm}}^2\\)", f"\\({area - 4}\\text{{ cm}}^2\\)"],
            f"The area of a triangle is given by the formula: \\(\\text{{Area}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}}\\).",
            f"Substitute \\(\\text{{base}} = {base}\\text{{ cm}}\\) and \\(\\text{{height}} = {height}\\text{{ cm}}\\): \\(\\frac{{1}}{{2}} \\times {base} \\times {height}\\).",
            f"Compute: \\(\\frac{{{base * height}}}{{2}} = {area}\\text{{ cm}}^2\\).",
            d, v
        )
        questions.append(q)

    # 7.2.1 Area of parallelogram = base * height (need 80)
    tc = "CBSE-8-MGP2-7-7.2.1"
    name = "Area of parallelogram = base * height"
    for i in range(80):
        base = 7 + (i % 9)
        height = 4 + (i % 6)
        area = base * height
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find the area of a parallelogram with base \\({base}\\text{{ cm}}\\) and corresponding height \\({height}\\text{{ cm}}\\).",
            f"\\({area}\\text{{ cm}}^2\\)",
            [f"\\({area // 2}\\text{{ cm}}^2\\)", f"\\({area + 5}\\text{{ cm}}^2\\)", f"\\({2 * (base + height)}\\text{{ cm}}^2\\)"],
            f"The formula for the area of a parallelogram is \\(\\text{{Area}} = \\text{{base}} \\times \\text{{height}}\\).",
            f"Substitute \\(\\text{{base}} = {base}\\text{{ cm}}\\) and \\(\\text{{height}} = {height}\\text{{ cm}}\\).",
            f"Calculate: \\({base} \\times {height} = {area}\\text{{ cm}}^2\\).",
            d, v
        )
        questions.append(q)

    # 7.2.2 Area of rhombus = 1/2 * d1 * d2 using perpendicular diagonals (need 80)
    tc = "CBSE-8-MGP2-7-7.2.2"
    name = "Area of rhombus = 1/2 * d1 * d2 using perpendicular diagonals"
    for i in range(80):
        d1 = 10 + (i % 8) * 2
        d2 = 8 + (i % 6) * 2
        area = (d1 * d2) // 2
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find the area of a rhombus whose diagonals measure \\({d1}\\text{{ cm}}\\) and \\({d2}\\text{{ cm}}\\).",
            f"\\({area}\\text{{ cm}}^2\\)",
            [f"\\({d1 * d2}\\text{{ cm}}^2\\)", f"\\({area + 8}\\text{{ cm}}^2\\)", f"\\({d1 + d2}\\text{{ cm}}^2\\)"],
            f"The diagonals of a rhombus are perpendicular bisectors of each other.",
            f"The area of a rhombus is given by \\(\\text{{Area}} = \\frac{{1}}{{2}} \\times d_1 \\times d_2\\).",
            f"Substitute \\(d_1 = {d1}\\) and \\(d_2 = {d2}\\): \\(\\frac{{1}}{{2}} \\times {d1} \\times {d2} = \\frac{{{d1 * d2}}}{{2}} = {area}\\text{{ cm}}^2\\).",
            d, v
        )
        questions.append(q)

    # 7.3.1 Area of trapezium = 1/2 * (sum of parallel sides) * height (need 80)
    tc = "CBSE-8-MGP2-7-7.3.1"
    name = "Area of trapezium = 1/2 * (sum of parallel sides) * height"
    for i in range(80):
        a = 6 + (i % 6)
        b = 10 + (i % 6)
        h = 4 + (i % 5) * 2
        sum_ab = a + b
        area = (sum_ab * h) // 2
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"The parallel sides of a trapezium are \\({a}\\text{{ cm}}\\) and \\({b}\\text{{ cm}}\\), and the perpendicular distance between them is \\({h}\\text{{ cm}}\\). Find its area.",
            f"\\({area}\\text{{ cm}}^2\\)",
            [f"\\({sum_ab * h}\\text{{ cm}}^2\\)", f"\\({area + 10}\\text{{ cm}}^2\\)", f"\\({area - 10}\\text{{ cm}}^2\\)"],
            f"The area of a trapezium is given by \\(\\text{{Area}} = \\frac{{1}}{{2}} \\times (a + b) \\times h\\).",
            f"Substitute \\(a = {a}\\text{{ cm}}, b = {b}\\text{{ cm}}, h = {h}\\text{{ cm}}\\): \\(\\frac{{1}}{{2}} \\times ({a} + {b}) \\times {h} = \\frac{{1}}{{2}} \\times {sum_ab} \\times {h}\\).",
            f"Compute: \\(\\frac{{{sum_ab * h}}}{{2}} = {area}\\text{{ cm}}^2\\).",
            d, v
        )
        questions.append(q)

    # 7.3.2 Finding height or parallel side when area is given (need 80)
    tc = "CBSE-8-MGP2-7-7.3.2"
    name = "Finding height or parallel side when area is given"
    for i in range(80):
        a = 8 + (i % 6)
        b = 12 + (i % 6)
        h = 5 + (i % 5)
        sum_ab = a + b
        area = (sum_ab * h) // 2
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"The area of a trapezium is \\({area}\\text{{ cm}}^2\\). If the parallel sides are \\({a}\\text{{ cm}}\\) and \\({b}\\text{{ cm}}\\), find its perpendicular height.",
            f"\\({h}\\text{{ cm}}\\)",
            [f"\\({h + 2}\\text{{ cm}}\\)", f"\\({h - 2}\\text{{ cm}}\\)", f"\\({sum_ab // 2}\\text{{ cm}}\\)"],
            f"Use the trapezium area formula: \\(\\text{{Area}} = \\frac{{1}}{{2}} \\times (a + b) \\times h\\).",
            f"Substitute known values: \\({area} = \\frac{{1}}{{2}} \\times ({a} + {b}) \\times h = \\frac{{{sum_ab}}}{{2}} \\times h\\).",
            f"Solve for \\(h\\): \\(h = \\frac{{2 \\times {area}}}{{{sum_ab}}} = \\frac{{{2 * area}}}{{{sum_ab}}} = {h}\\text{{ cm}}\\).",
            d, v
        )
        questions.append(q)

    # 7.4.1 Dividing quadrilateral into two triangles along diagonal (need 80)
    tc = "CBSE-8-MGP2-7-7.4.1"
    name = "Dividing quadrilateral into two triangles along diagonal"
    for i in range(80):
        d_diag = 12 + (i % 6) * 2
        h1 = 4 + (i % 4)
        h2 = 6 + (i % 4)
        sum_h = h1 + h2
        area = (d_diag * sum_h) // 2
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"A diagonal of a general quadrilateral is \\({d_diag}\\text{{ cm}}\\) long, and the perpendicular offsets drawn from the opposite vertices to this diagonal are \\({h1}\\text{{ cm}}\\) and \\({h2}\\text{{ cm}}\\). Find the area of the quadrilateral.",
            f"\\({area}\\text{{ cm}}^2\\)",
            [f"\\({d_diag * sum_h}\\text{{ cm}}^2\\)", f"\\({area + 12}\\text{{ cm}}^2\\)", f"\\({area - 10}\\text{{ cm}}^2\\)"],
            f"A general quadrilateral is divided into two triangles along the diagonal \\(d\\).",
            f"The total area is the sum of both triangle areas: \\(\\text{{Area}} = \\frac{{1}}{{2}} d(h_1 + h_2)\\).",
            f"Substitute values: \\(\\frac{{1}}{{2}} \\times {d_diag} \\times ({h1} + {h2}) = \\frac{{{d_diag} \\times {sum_h}}}{{2}} = {area}\\text{{ cm}}^2\\).",
            d, v
        )
        questions.append(q)

    # 7.4.2 Survey field book method (triangulation and trapezoids) (need 80)
    tc = "CBSE-8-MGP2-7-7.4.2"
    name = "Survey field book method (triangulation and trapezoids)"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "In land surveying, how is the total area of an irregular polygon field calculated using a central baseline in a field book?",
            "By decomposing the irregular polygon into right-angled triangles and trapeziums aligned to offsets along the baseline and summing their areas",
            [
                "By treating the entire irregular field as a single large circle",
                "By measuring only the outer perimeter and multiplying by 2",
                "By drawing a random diagonal and guessing the offset"
            ],
            f"The survey field book method establishes a straight central baseline across the irregular plot.",
            f"Perpendicular offsets are measured from the baseline to all boundary vertices.",
            f"This partitions the field into standard geometric figures: right triangles and trapeziums whose individual areas are calculated and added together.",
            d, v
        )
        questions.append(q)

    # 7.5.1 Total and lateral surface area of cube (6a², 4a²) (need 80)
    tc = "CBSE-8-MGP2-7-7.5.1"
    name = "Total and lateral surface area of cube (6a², 4a²)"
    for i in range(80):
        a = 3 + (i % 10)
        tsa = 6 * a * a
        lsa = 4 * a * a
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find the Total Surface Area (TSA) and Lateral Surface Area (LSA) of a solid cube having edge length \\({a}\\text{{ cm}}\\).",
            f"TSA = \\({tsa}\\text{{ cm}}^2\\), LSA = \\({lsa}\\text{{ cm}}^2\\)",
            [
                f"TSA = \\({lsa}\\text{{ cm}}^2\\), LSA = \\({tsa}\\text{{ cm}}^2\\)",
                f"TSA = \\({a**3}\\text{{ cm}}^2\\), LSA = \\({4 * a}\\text{{ cm}}^2\\)",
                f"TSA = \\({tsa + 10}\\text{{ cm}}^2\\), LSA = \\({lsa - 5}\\text{{ cm}}^2\\)"
            ],
            f"A cube has 6 identical square faces, each of area \\(a^2\\). Hence, \\(\\text{{TSA}} = 6a^2 = 6({a}^2) = 6 \\times {a*a} = {tsa}\\text{{ cm}}^2\\).",
            f"The lateral surface area excludes top and bottom faces (4 vertical faces): \\(\\text{{LSA}} = 4a^2 = 4({a}^2) = 4 \\times {a*a} = {lsa}\\text{{ cm}}^2\\).",
            f"Therefore, \\(\\text{{TSA}} = {tsa}\\text{{ cm}}^2\\) and \\(\\text{{LSA}} = {lsa}\\text{{ cm}}^2\\).",
            d, v
        )
        questions.append(q)

    # 7.5.2 Total and lateral surface area of cuboid (2(lb+bh+hl), 2h(l+b)) (need 80)
    tc = "CBSE-8-MGP2-7-7.5.2"
    name = "Total and lateral surface area of cuboid (2(lb+bh+hl), 2h(l+b))"
    for i in range(80):
        l = 5 + (i % 6)
        b = 4 + (i % 4)
        h = 3 + (i % 3)
        tsa = 2 * (l * b + b * h + h * l)
        lsa = 2 * h * (l + b)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Calculate the Total Surface Area of a cuboidal box with dimensions length \\(l = {l}\\text{{ cm}}\\), breadth \\(b = {b}\\text{{ cm}}\\), and height \\(h = {h}\\text{{ cm}}\\).",
            f"\\({tsa}\\text{{ cm}}^2\\)",
            [f"\\({lsa}\\text{{ cm}}^2\\)", f"\\({l * b * h}\\text{{ cm}}^2\\)", f"\\({tsa + 15}\\text{{ cm}}^2\\)"],
            f"The total surface area of a cuboid is given by \\(\\text{{TSA}} = 2(lb + bh + hl)\\).",
            f"Compute pairwise face areas: \\(lb = {l * b}\\), \\(bh = {b * h}\\), \\(hl = {h * l}\\). Sum = \\({l*b + b*h + h*l}\\).",
            f"Multiply by 2: \\(2 \\times {l*b + b*h + h*l} = {tsa}\\text{{ cm}}^2\\).",
            d, v
        )
        questions.append(q)

    # 7.5.3 Curved and total surface area of cylinder (2πrh, 2πr(r+h)) (need 80)
    tc = "CBSE-8-MGP2-7-7.5.3"
    name = "Curved and total surface area of cylinder (2πrh, 2πr(r+h))"
    for i in range(80):
        r = 7  # multiple of 7 for π = 22/7
        h = 5 + (i % 10)
        # CSA = 2 * (22/7) * 7 * h = 44 * h
        csa = 44 * h
        # TSA = 2 * (22/7) * 7 * (r + h) = 44 * (7 + h)
        tsa = 44 * (r + h)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find the Curved Surface Area (CSA) of a solid right circular cylinder of base radius \\(r = {r}\\text{{ cm}}\\) and height \\(h = {h}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)).",
            f"\\({csa}\\text{{ cm}}^2\\)",
            [f"\\({tsa}\\text{{ cm}}^2\\)", f"\\({csa + 22}\\text{{ cm}}^2\\)", f"\\({csa - 22}\\text{{ cm}}^2\\)"],
            f"The curved surface area of a cylinder is given by \\(\\text{{CSA}} = 2\\pi rh\\).",
            f"Substitute \\(r = {r}\\), \\(h = {h}\\), and \\(\\pi = \\frac{{22}}{{7}}\\): \\(2 \\times \\frac{{22}}{{7}} \\times {r} \\times {h} = 44 \\times {h}\\).",
            f"Compute: \\(44 \\times {h} = {csa}\\text{{ cm}}^2\\).",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch7_questions()
    print(f"Generated {len(qs)} questions for Chapter 7.")
    with open("scripts/cbse8_mgp2_ch7_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/cbse8_mgp2_ch7_topup.json")
