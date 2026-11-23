import json
import random

random.seed(8707)

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

    vaults = ["exam"] * 40 + ["practice"] * 20 + ["foundation"] * 20
    diffs = (["easy"] * 15 + ["medium"] * 15 + ["hard"] * 10) + (["easy"] * 6 + ["medium"] * 8 + ["hard"] * 6) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)

    # -------------------------------------------------------------
    # 7.1.1 Concept of direct proportion (x ∝ y) (80 questions)
    # -------------------------------------------------------------
    tc_711 = "MH-8-MTH-7-7.1.1"
    name_711 = "Concept of direct proportion (x ∝ y)"
    prop_statements = [
        ("The cost of apples and the number of kilograms purchased", "Direct variation", ["Inverse variation", "No variation", "Joint inverse variation"]),
        ("The distance travelled by a car at uniform speed and the time taken", "Direct variation", ["Inverse variation", "Quadratic variation", "No variation"]),
        ("The number of notebooks purchased and the total amount paid", "Direct variation", ["Inverse variation", "Inverse square variation", "No relationship"]),
        ("The perimeter of a square and the length of its side", "Direct variation", ["Inverse variation", "Inverse square variation", "No variation"]),
        ("The circumference of a circle and its radius", "Direct variation", ["Inverse variation", "Inverse square variation", "No relation"]),
        ("The total wages earned by a daily wage worker and the number of days worked", "Direct variation", ["Inverse variation", "Inverse proportion", "Constant variation"]),
        ("Fuel consumed by a vehicle and the distance driven at steady speed", "Direct variation", ["Inverse variation", "Negative variation", "Uncorrelated"]),
        ("The mass of an object and its volume at constant density", "Direct variation", ["Inverse variation", "Non-linear inverse", "Zero variation"])
    ]
    for i in range(80):
        ctx, ans, wrongs = prop_statements[i % len(prop_statements)]
        q = make_q(
            tc_711, name_711,
            f"Identify the mathematical type of variation represented by: '{ctx}'.",
            ans, wrongs,
            f"Consider whether an increase in one quantity causes a proportional increase in the other quantity.",
            f"As one quantity increases, the other increases such that their ratio remains constant: \\(\\frac{{x}}{{y}} = k\\).",
            f"Therefore, this relationship represents {ans}.",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 7.1.2 Equation of variation x = ky (80 questions)
    # -------------------------------------------------------------
    tc_712 = "MH-8-MTH-7-7.1.2"
    name_712 = "Equation of variation x = ky"
    eq_data = [
        ("p", "q", 3), ("x", "y", 5), ("m", "n", 7), ("u", "v", 4), ("a", "b", 6),
        ("y", "x", 2), ("c", "d", 8), ("s", "t", 9), ("w", "z", 10), ("f", "g", 12)
    ]
    for i in range(80):
        v1, v2, k = eq_data[i % len(eq_data)]
        k_val = k + (i // 10)
        ans = f"\\({v1} = {k_val}{v2}\\)"
        w1 = f"\\({v1}{v2} = {k_val}\\)"
        w2 = f"\\({v1} = \\frac{{{k_val}}}{{{v2}}}\\)"
        w3 = f"\\({v1} + {v2} = {k_val}\\)"
        
        q = make_q(
            tc_712, name_712,
            f"If \\({v1}\\) varies directly as \\({v2}\\) and the constant of variation is \\(k = {k_val}\\), write the equation of variation.",
            ans, [w1, w2, w3],
            f"Direct variation between two variables \\({v1}\\) and \\({v2}\\) is symbolically written as \\({v1} \\propto {v2}\\).",
            f"To convert the proportion into an algebraic equation, multiply by the constant of variation \\(k\\): \\({v1} = k{v2}\\).",
            f"Substituting \\(k = {k_val}\\) yields the equation \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 7.1.3 Finding constant of variation k (80 questions)
    # -------------------------------------------------------------
    tc_713 = "MH-8-MTH-7-7.1.3"
    name_713 = "Finding constant of variation k"
    k_pairs = [
        (12, 3), (15, 5), (24, 6), (36, 4), (40, 8), (50, 10), (28, 7), (45, 9), (64, 8), (72, 9),
        (30, 6), (42, 7), (56, 8), (63, 7), (80, 10), (90, 9), (48, 6), (54, 9), (35, 5), (49, 7)
    ]
    for i in range(80):
        x, y = k_pairs[i % len(k_pairs)]
        scale = (i // 20) + 1
        x_val = x * scale
        y_val = y * scale
        k = x_val // y_val
        
        ans = f"\\(k = {k}\\)"
        w1 = f"\\(k = {x_val * y_val}\\)"
        w2 = f"\\(k = {k + 2}\\)"
        w3 = f"\\(k = {max(1, k - 2)}\\)"
        
        q = make_q(
            tc_713, name_713,
            f"If \\(x \\propto y\\) and \\(x = {x_val}\\) when \\(y = {y_val}\\), find the constant of variation \\(k\\).",
            ans, [w1, w2, w3],
            f"In direct proportion, the ratio between the variables remains constant: \\(k = \\frac{{x}}{{y}}\\).",
            f"Substitute the given values: \\(k = \\frac{{{x_val}}}{{{y_val}}}\\).",
            f"Simplify the fraction: \\({x_val} \\div {y_val} = {k}\\). Therefore, \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 7.2.1 Concept of inverse variation (x ∝ 1/y) (80 questions)
    # -------------------------------------------------------------
    tc_721 = "MH-8-MTH-7-7.2.1"
    name_721 = "Concept of inverse variation (x ∝ 1/y)"
    inv_statements = [
        ("The number of workers on a construction project and the days needed to finish it", "Inverse variation", ["Direct variation", "No variation", "Direct square variation"]),
        ("The speed of a train and the time taken to travel a fixed distance", "Inverse variation", ["Direct variation", "Joint variation", "No relationship"]),
        ("The number of pipes filling a tank and the time taken to fill it completely", "Inverse variation", ["Direct variation", "Direct cubic variation", "No correlation"]),
        ("The price of sugar and the quantity that can be bought for a fixed budget", "Inverse variation", ["Direct variation", "Joint direct variation", "Zero variation"]),
        ("The length of each period in a school and the total number of periods in a fixed school duration", "Inverse variation", ["Direct variation", "Exponential variation", "No variation"]),
        ("The width of a rectangle having a constant area and its length", "Inverse variation", ["Direct variation", "Direct quadratic variation", "No relation"]),
        ("The number of students sharing a fixed hostel mess bill and each student's share", "Inverse variation", ["Direct variation", "Direct proportion", "Constant difference"]),
        ("The volume of a gas at constant temperature and its applied pressure (Boyle's Law)", "Inverse variation", ["Direct variation", "No variation", "Square proportion"])
    ]
    for i in range(80):
        ctx, ans, wrongs = inv_statements[i % len(inv_statements)]
        q = make_q(
            tc_721, name_721,
            f"Identify the mathematical type of variation: '{ctx}'.",
            ans, wrongs,
            f"Observe how one variable changes when the other variable increases.",
            f"When one quantity increases, the other decreases such that their product remains constant: \\(x \\times y = k\\).",
            f"Hence, this relationship exemplifies {ans}.",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 7.2.2 Equation xy = k (80 questions)
    # -------------------------------------------------------------
    tc_722 = "MH-8-MTH-7-7.2.2"
    name_722 = "Equation xy = k"
    inv_eqs = [
        ("p", "q", 24), ("x", "y", 60), ("m", "n", 120), ("a", "b", 48), ("u", "v", 72),
        ("r", "s", 36), ("c", "d", 90), ("f", "g", 100), ("w", "z", 84), ("s", "t", 50)
    ]
    for i in range(80):
        v1, v2, k = inv_eqs[i % len(inv_eqs)]
        k_val = k + (i * 2)
        ans = f"\\({v1}{v2} = {k_val}\\)"
        w1 = f"\\({v1} = {k_val}{v2}\\)"
        w2 = f"\\(\\frac{{{v1}}}{{{v2}}} = {k_val}\\)"
        w3 = f"\\({v1} + {v2} = {k_val}\\)"
        
        q = make_q(
            tc_722, name_722,
            f"If \\({v1}\\) varies inversely as \\({v2}\\) and the constant of variation is \\(k = {k_val}\\), write the equation of variation.",
            ans, [w1, w2, w3],
            f"Inverse variation between \\({v1}\\) and \\({v2}\\) is expressed as \\({v1} \\propto \\frac{{1}}{{{v2}}}\\).",
            f"Equating with the constant of variation \\(k\\) gives \\({v1} = \\frac{{k}}{{{v2}}}\\), which can be written as \\({v1}{v2} = k\\).",
            f"Substituting \\(k = {k_val}\\) produces the equation \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 7.2.3 Solving missing values in tables (80 questions)
    # -------------------------------------------------------------
    tc_723 = "MH-8-MTH-7-7.2.3"
    name_723 = "Solving missing values in tables"
    inv_table_data = [
        (12, 10, 15), (20, 6, 30), (8, 15, 24), (16, 9, 12), (18, 10, 15),
        (25, 4, 10), (30, 4, 20), (5, 24, 12), (6, 20, 15), (10, 18, 9),
        (14, 12, 21), (15, 8, 20), (16, 15, 24), (20, 18, 15), (24, 15, 18),
        (32, 9, 16), (36, 10, 15), (40, 9, 18), (45, 8, 20), (50, 6, 15)
    ]
    for i in range(80):
        x1, y1, x2 = inv_table_data[i % len(inv_table_data)]
        k = x1 * y1
        y2 = k // x2
        
        ans = f"\\(y = {y2}\\)"
        w1 = f"\\(y = {y2 + 2}\\)"
        w2 = f"\\(y = {max(1, y2 - 2)}\\)"
        w3 = f"\\(y = {y2 * 2}\\)"
        
        q = make_q(
            tc_723, name_723,
            f"In an inverse variation table, \\(x\\) and \\(y\\) vary inversely. If \\(x = {x1}\\) when \\(y = {y1}\\), find \\(y\\) when \\(x = {x2}\\).",
            ans, [w1, w2, w3],
            f"In inverse variation, the product of corresponding values is constant: \\(x_1 y_1 = x_2 y_2 = k\\).",
            f"Calculate the constant of variation: \\(k = {x1} \\times {y1} = {k}\\).",
            f"Solve for \\(y_2\\): \\(y_2 = \\frac{{k}}{{x_2}} = \\frac{{{k}}}{{{x2}}} = {y2}\\). Thus, \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 7.3.1 Man-days calculations (80 questions)
    # -------------------------------------------------------------
    tc_731 = "MH-8-MTH-7-7.3.1"
    name_731 = "Man-days calculations"
    mandays = [
        (15, 8, 12), (12, 10, 15), (20, 6, 24), (16, 15, 20), (25, 12, 30),
        (18, 10, 12), (10, 24, 15), (14, 15, 21), (30, 8, 20), (24, 10, 16),
        (8, 30, 12), (15, 16, 20), (18, 20, 24), (20, 15, 25), (24, 18, 36),
        (28, 15, 21), (32, 15, 24), (35, 12, 21), (36, 10, 15), (40, 12, 24)
    ]
    for i in range(80):
        m1, d1, m2 = mandays[i % len(mandays)]
        total_work = m1 * d1
        d2 = total_work // m2
        
        ans = f"\\({d2}\\text{{ days}}\\)"
        w1 = f"\\({d2 + 3}\\text{{ days}}\\)"
        w2 = f"\\({max(1, d2 - 3)}\\text{{ days}}\\)"
        w3 = f"\\({d2 + 6}\\text{{ days}}\\)"
        
        q = make_q(
            tc_731, name_731,
            f"If \\({m1}\\) workers take \\({d1}\\) days to complete a construction job, how many days will \\({m2}\\) workers take to complete the same job?",
            ans, [w1, w2, w3],
            f"The number of workers and the days taken vary inversely: \\(M_1 \\times D_1 = M_2 \\times D_2\\).",
            f"Calculate the total work in man-days: \\({m1} \\times {d1} = {total_work}\\text{{ man-days}}\\).",
            f"Find the days needed with \\({m2}\\) workers: \\(D_2 = \\frac{{{total_work}}}{{{m2}}} = {d2}\\text{{ days}}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 7.3.2 Speed and time variations in transportation (80 questions)
    # -------------------------------------------------------------
    tc_732 = "MH-8-MTH-7-7.3.2"
    name_732 = "Speed and time variations in transportation"
    speed_time = [
        (60, 4, 80), (40, 6, 60), (50, 6, 75), (45, 4, 60), (72, 5, 90),
        (80, 3, 60), (48, 5, 60), (54, 5, 90), (36, 5, 60), (64, 4, 80),
        (75, 4, 100), (90, 4, 60), (45, 6, 90), (50, 4, 80), (70, 6, 84),
        (84, 5, 70), (42, 6, 63), (56, 5, 70), (60, 5, 75), (48, 6, 72)
    ]
    for i in range(80):
        s1, t1, s2 = speed_time[i % len(speed_time)]
        dist = s1 * t1
        t2 = dist // s2
        
        ans = f"\\({t2}\\text{{ hours}}\\)"
        w1 = f"\\({t2 + 1}\\text{{ hours}}\\)"
        w2 = f"\\({max(1, t2 - 1)}\\text{{ hours}}\\)"
        w3 = f"\\({t2 + 2}\\text{{ hours}}\\)"
        
        q = make_q(
            tc_732, name_732,
            f"A bus travels a fixed journey at an average speed of \\({s1}\\text{{ km/h}}\\) in \\({t1}\\text{{ hours}}\\). How much time will it take if its speed is changed to \\({s2}\\text{{ km/h}}\\) at the same distance?",
            ans, [w1, w2, w3],
            f"For a fixed distance, speed and time vary inversely: \\(S_1 \\times T_1 = S_2 \\times T_2 = \\text{{Distance}}\\).",
            f"Calculate the total distance: \\(\\text{{Distance}} = {s1} \\times {t1} = {dist}\\text{{ km}}\\).",
            f"Find the new travel time: \\(T_2 = \\frac{{{dist}}}{{{s2}}} = {t2}\\text{{ hours}}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch7_questions()
    print(f"Generated {len(qs)} questions for Chapter 7.")
    out_path = "scripts/mh8_mth_ch7_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
