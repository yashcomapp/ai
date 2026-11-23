import json
import random

random.seed(81616)

def build_ch16_questions():
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
    # 16.1.1 Total surface area = 2(lb + bh + lh) (80 questions)
    # -------------------------------------------------------------
    tc_1611 = "MH-8-MTH-16-16.1.1"
    name_1611 = "Total surface area = 2(lb + bh + lh)"
    cuboid_data = [
        (10, 8, 5, 340), (12, 10, 6, 504), (15, 12, 8, 792), (8, 6, 4, 208),
        (20, 15, 10, 1300), (14, 10, 5, 520), (16, 12, 10, 944), (18, 14, 8, 1016),
        (25, 20, 12, 2080), (30, 20, 15, 2700), (9, 7, 5, 286), (11, 8, 6, 404),
        (13, 9, 7, 542), (16, 10, 8, 736), (22, 16, 10, 1464), (24, 18, 12, 1872)
    ]
    for i in range(80):
        l, b, h, tsa = cuboid_data[i % len(cuboid_data)]
        ans = f"\\({tsa}\\text{{ cm}}^2\\)"
        w1 = f"\\({tsa + 20}\\text{{ cm}}^2\\)"
        w2 = f"\\({max(20, tsa - 20)}\\text{{ cm}}^2\\)"
        w3 = f"\\({tsa * 2}\\text{{ cm}}^2\\)"
        
        q = make_q(
            tc_1611, name_1611,
            f"Calculate the total surface area of a cuboid measuring \\(l = {l}\\text{{ cm}}\\), \\(b = {b}\\text{{ cm}}\\), and \\(h = {h}\\text{{ cm}}\\).",
            ans, [w1, w2, w3],
            f"Use the total surface area formula for a cuboid: \\(\\text{{TSA}} = 2(lb + bh + lh)\\).",
            f"Substitute the dimensions: \\(\\text{{TSA}} = 2(({l} \\times {b}) + ({b} \\times {h}) + ({l} \\times {h})) = 2({l*b} + {b*h} + {l*h})\\).",
            f"Evaluating the arithmetic gives \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 16.1.2 Volume of cuboid = l * b * h (80 questions)
    # -------------------------------------------------------------
    tc_1612 = "MH-8-MTH-16-16.1.2"
    name_1612 = "Volume of cuboid = l * b * h"
    for i in range(80):
        l, b, h, _ = cuboid_data[i % len(cuboid_data)]
        vol = l * b * h
        ans = f"\\({vol:,}\\text{{ cm}}^3\\)".replace(",", "")
        w1 = f"\\({vol + 100:,}\\text{{ cm}}^3\\)".replace(",", "")
        w2 = f"\\({max(50, vol - 100):,}\\text{{ cm}}^3\\)".replace(",", "")
        w3 = f"\\({vol * 2:,}\\text{{ cm}}^3\\)".replace(",", "")
        
        q = make_q(
            tc_1612, name_1612,
            f"Find the volume of a cuboid with length \\({l}\\text{{ cm}}\\), breadth \\({b}\\text{{ cm}}\\), and height \\({h}\\text{{ cm}}\\).",
            ans, [w1, w2, w3],
            f"The volume of a cuboid is calculated as: \\(\\text{{Volume}} = l \\times b \\times h\\).",
            f"Substitute the given side lengths: \\(\\text{{Volume}} = {l} \\times {b} \\times {h}\\).",
            f"Multiplying gives \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 16.1.3 TSA of cube = 6l², Volume = l³ (80 questions)
    # -------------------------------------------------------------
    tc_1613 = "MH-8-MTH-16-16.1.3"
    name_1613 = "TSA of cube = 6l², Volume = l³"
    cube_sides = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 25]
    for i in range(80):
        s = cube_sides[i % len(cube_sides)]
        tsa = 6 * (s ** 2)
        vol = s ** 3
        
        if i % 2 == 0:
            ans = f"\\({tsa}\\text{{ cm}}^2\\)"
            w1 = f"\\({4 * (s**2)}\\text{{ cm}}^2\\)"
            w2 = f"\\({tsa + 12}\\text{{ cm}}^2\\)"
            w3 = f"\\({max(10, tsa - 12)}\\text{{ cm}}^2\\)"
            prompt = f"Find the total surface area of a solid cube having edge length \\({s}\\text{{ cm}}\\)."
            s1 = f"The total surface area of a cube is given by \\(\\text{{TSA}} = 6l^2\\), where \\(l\\) is the side length."
            s2 = f"Calculate: \\(6 \\times {s}^2 = 6 \\times {s**2}\\)."
            s3 = f"Multiplying gives \\({ans}\\)."
        else:
            ans = f"\\({vol:,}\\text{{ cm}}^3\\)".replace(",", "")
            w1 = f"\\({vol + 50:,}\\text{{ cm}}^3\\)".replace(",", "")
            w2 = f"\\({max(10, vol - 50):,}\\text{{ cm}}^3\\)".replace(",", "")
            w3 = f"\\({vol * 2:,}\\text{{ cm}}^3\\)".replace(",", "")
            prompt = f"Find the volume of a solid cube whose edge length is \\({s}\\text{{ cm}}\\)."
            s1 = f"The volume of a cube is computed as \\(\\text{{Volume}} = l^3\\), where \\(l = {s}\\text{{ cm}}\\)."
            s2 = f"Calculate: \\({s}^3 = {s} \\times {s} \\times {s}\\)."
            s3 = f"The volume is \\({ans}\\)."
            
        q = make_q(tc_1613, name_1613, prompt, ans, [w1, w2, w3], s1, s2, s3, diffs[i], vaults[i])
        questions.append(q)

    # -------------------------------------------------------------
    # 16.2.1 Curved surface area = 2πrh (80 questions)
    # -------------------------------------------------------------
    tc_1621 = "MH-8-MTH-16-16.2.1"
    name_1621 = "Curved surface area = 2πrh"
    cyl_csa = [
        (7, 10, 440), (14, 15, 1320), (7, 20, 880), (21, 10, 1320), (14, 25, 2200),
        (7, 5, 220), (28, 15, 2640), (7, 15, 660), (14, 10, 880), (21, 20, 2640),
        (35, 12, 2640), (7, 25, 1100), (14, 30, 2640), (28, 10, 1760), (7, 30, 1320),
        (21, 15, 1980)
    ]
    for i in range(80):
        r, h, csa = cyl_csa[i % len(cyl_csa)]
        ans = f"\\({csa}\\text{{ cm}}^2\\)"
        w1 = f"\\({csa + 40}\\text{{ cm}}^2\\)"
        w2 = f"\\({max(20, csa - 40)}\\text{{ cm}}^2\\)"
        w3 = f"\\({csa * 2}\\text{{ cm}}^2\\)"
        
        q = make_q(
            tc_1621, name_1621,
            f"Find the curved surface area of a circular cylinder having base radius \\(r = {r}\\text{{ cm}}\\) and height \\(h = {h}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)).",
            ans, [w1, w2, w3],
            f"The formula for the curved surface area of a cylinder is \\(\\text{{CSA}} = 2\\pi rh\\).",
            f"Substitute the dimensions: \\(\\text{{CSA}} = 2 \\times \\frac{{22}}{{7}} \\times {r} \\times {h}\\).",
            f"Evaluating the product gives \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 16.2.2 Total surface area = 2πr(r + h) (80 questions)
    # -------------------------------------------------------------
    tc_1622 = "MH-8-MTH-16-16.2.2"
    name_1622 = "Total surface area = 2πr(r + h)"
    cyl_tsa = [
        (7, 10, 748), (14, 16, 2640), (7, 13, 880), (7, 23, 1320), (14, 21, 3080),
        (7, 3, 440), (7, 8, 660), (14, 6, 1760), (21, 9, 3960), (7, 18, 1100),
        (14, 11, 2200), (21, 19, 5280), (7, 28, 1540), (14, 26, 3520), (28, 12, 7040),
        (7, 33, 1760)
    ]
    for i in range(80):
        r, h, tsa = cyl_tsa[i % len(cyl_tsa)]
        ans = f"\\({tsa}\\text{{ cm}}^2\\)"
        w1 = f"\\({tsa + 44}\\text{{ cm}}^2\\)"
        w2 = f"\\({max(40, tsa - 44)}\\text{{ cm}}^2\\)"
        w3 = f"\\({tsa * 2}\\text{{ cm}}^2\\)"
        
        q = make_q(
            tc_1622, name_1622,
            f"Calculate the total surface area of a closed cylinder having radius \\(r = {r}\\text{{ cm}}\\) and height \\(h = {h}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)).",
            ans, [w1, w2, w3],
            f"The total surface area of a closed cylinder is \\(\\text{{TSA}} = 2\\pi r(r + h)\\).",
            f"Substitute the values: \\(\\text{{TSA}} = 2 \\times \\frac{{22}}{{7}} \\times {r} \\times ({r} + {h}) = 2 \\times \\frac{{22}}{{7}} \\times {r} \\times {r+h}\\).",
            f"Evaluating the arithmetic yields \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 16.3.1 Volume = πr²h (80 questions)
    # -------------------------------------------------------------
    tc_1631 = "MH-8-MTH-16-16.3.1"
    name_1631 = "Volume = πr²h"
    cyl_vol = [
        (7, 10, 1540), (14, 10, 6160), (7, 20, 3080), (21, 10, 13860), (14, 15, 9240),
        (7, 15, 2310), (7, 5, 770), (28, 5, 12320), (14, 20, 12320), (21, 20, 27720),
        (7, 25, 3850), (14, 25, 15400), (35, 10, 38500), (7, 30, 4620), (28, 10, 24640),
        (21, 15, 20790)
    ]
    for i in range(80):
        r, h, vol = cyl_vol[i % len(cyl_vol)]
        ans = f"\\({vol:,}\\text{{ cm}}^3\\)".replace(",", "")
        w1 = f"\\({vol + 140:,}\\text{{ cm}}^3\\)".replace(",", "")
        w2 = f"\\({max(100, vol - 140):,}\\text{{ cm}}^3\\)".replace(",", "")
        w3 = f"\\({vol * 2:,}\\text{{ cm}}^3\\)".replace(",", "")
        
        q = make_q(
            tc_1631, name_1631,
            f"Find the volume of a cylinder with radius \\(r = {r}\\text{{ cm}}\\) and height \\(h = {h}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)).",
            ans, [w1, w2, w3],
            f"The formula for the volume of a cylinder is \\(\\text{{Volume}} = \\pi r^2 h\\).",
            f"Substitute the dimensions: \\(\\text{{Volume}} = \\frac{{22}}{{7}} \\times {r}^2 \\times {h} = \\frac{{22}}{{7}} \\times {r*r} \\times {h}\\).",
            f"Calculating gives the volume \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 16.3.2 Conversion: 1 litre = 1000 cm³, 1 m³ = 1000 litres (80 questions)
    # -------------------------------------------------------------
    tc_1632 = "MH-8-MTH-16-16.3.2"
    name_1632 = "Conversion: 1 litre = 1000 cm³, 1 m³ = 1000 litres"
    conv_data = [
        ("How many cubic centimetres (\\(\\text{cm}^3\\)) are in 1 litre?", "\\(1000\\text{ cm}^3\\)", ["\\(100\\text{ cm}^3\\)", "\\(10000\\text{ cm}^3\\)", "\\(10\\text{ cm}^3\\)"]),
        ("How many litres are in \\(1\\text{ m}^3\\) of liquid capacity?", "\\(1000\\text{ litres}\\)", ["\\(100\\text{ litres}\\)", "\\(10000\\text{ litres}\\)", "\\(500\\text{ litres}\\)"]),
        ("A cylindrical tank has a volume of \\(15400\\text{ cm}^3\\). What is its capacity in litres?", "\\(15.4\\text{ litres}\\)", ["\\(154\\text{ litres}\\)", "\\(1.54\\text{ litres}\\)", "\\(1540\\text{ litres}\\)"]),
        ("A water reservoir contains \\(5\\text{ m}^3\\) of water. Convert this capacity into litres.", "\\(5000\\text{ litres}\\)", ["\\(500\\text{ litres}\\)", "\\(50000\\text{ litres}\\)", "\\(50\\text{ litres}\\)"]),
        ("Convert \\(3500\\text{ cm}^3\\) of milk into litres.", "\\(3.5\\text{ litres}\\)", ["\\(35\\text{ litres}\\)", "\\(0.35\\text{ litres}\\)", "\\(350\\text{ litres}\\)"]),
        ("A tank holds \\(2500\\text{ litres}\\) of oil. What is its volume in cubic metres (\\(\\text{m}^3\\))?", "\\(2.5\\text{ m}^3\\)", ["\\(25\\text{ m}^3\\)", "\\(0.25\\text{ m}^3\\)", "\\(250\\text{ m}^3\\)"]),
        ("How many millilitres (\\(\\text{mL}\\)) are equivalent to \\(1\\text{ cm}^3\\)?", "\\(1\\text{ mL}\\)", ["\\(10\\text{ mL}\\)", "\\(100\\text{ mL}\\)", "\\(0.1\\text{ mL}\\)"]),
        ("A vessel with capacity \\(8.2\\text{ litres}\\) has a volume of how many \\(\\text{cm}^3\\)?", "\\(8200\\text{ cm}^3\\)", ["\\(820\\text{ cm}^3\\)", "\\(82000\\text{ cm}^3\\)", "\\(82\\text{ cm}^3\\)"])
    ]
    for i in range(80):
        prompt, ans, wrongs = conv_data[i % len(conv_data)]
        q = make_q(
            tc_1632, name_1632,
            f"Capacity and metric volume conversion: {prompt}",
            ans, wrongs,
            "Recall standard metric conversion factors: \\(1\\text{ litre} = 1000\\text{ cm}^3 = 1000\\text{ mL}\\) and \\(1\\text{ m}^3 = 1000\\text{ litres}\\).",
            "Apply the appropriate multiplication or division ratio.",
            f"Therefore, the converted value is {ans}.",
            diffs[i], vaults[i]
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch16_questions()
    print(f"Generated {len(qs)} questions for Chapter 16.")
    out_path = "scripts/mh8_mth_ch16_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
