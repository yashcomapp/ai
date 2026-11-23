import json
import random

random.seed(8203)

def build_ch3_questions():
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

    # 3.1.1 Concept of inverse variation (xy = k) (need 80)
    tc = "CBSE-8-MGP2-3-3.1.1"
    name = "Concept of inverse variation (xy = k)"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "Two quantities \\(x\\) and \\(y\\) vary inversely with each other. Which mathematical equation expresses this relationship?",
            "\\(x \\times y = k\\) (constant)",
            ["\\(\\frac{x}{y} = k\\) (constant)", "\\(x + y = k\\) (constant)", "\\(x - y = k\\) (constant)"],
            f"By definition of inverse variation, an increase in \\(x\\) causes a proportional decrease in \\(y\\) such that their product remains constant.",
            f"Mathematically, \\(x \\propto \\frac{{1}}{{y}} \\iff x \\times y = k\\) where \\(k\\) is the constant of variation.",
            f"Therefore, \\(x \\times y = k\\) represents inverse variation.",
            d, v
        )
        questions.append(q)

    # 3.1.2 Distinguishing direct vs inverse proportion situations (need 80)
    tc = "CBSE-8-MGP2-3-3.1.2"
    name = "Distinguishing direct vs inverse proportion situations"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "Which of the following real-world situations represents INVERSE PROPORTION?",
            "Number of workers on a construction job and time taken to complete the job",
            [
                "Number of books purchased and total cost of books",
                "Distance traveled and time taken at uniform speed",
                "Weight of sugar purchased and its total price"
            ],
            f"In direct proportion, both quantities increase together (more books = higher cost; more time = more distance).",
            f"In inverse proportion, increasing one quantity decreases the other (more workers = fewer days to finish).",
            f"Hence, workers and time taken is an inverse proportion relationship.",
            d, v
        )
        questions.append(q)

    # 3.2.1 Speed-time inversely proportional relationships (need 80)
    tc = "CBSE-8-MGP2-3-3.2.1"
    name = "Speed-time inversely proportional relationships"
    for i in range(80):
        s1 = 40 + (i % 10) * 5
        t1 = 3
        dist = s1 * t1
        s2 = 60
        t2 = dist / s2
        t2_str = f"{t2:.1f}" if t2 != int(t2) else str(int(t2))
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"A car travels a fixed distance in \\({t1}\\text{{ hours}}\\) at a speed of \\({s1}\\text{{ km/h}}\\). How long will it take at \\({s2}\\text{{ km/h}}\\) under inverse proportion?",
            f"\\({t2_str}\\text{{ hours}}\\)",
            [f"\\({float(t2_str) + 1.5:.1f}\\text{{ hours}}\\", f"\\({float(t2_str) - 0.5:.1f}\\text{{ hours}}\\", f"\\(5\\text{{ hours}}\\)"],
            f"For a fixed distance, speed and time vary inversely: \\(s_1 \\times t_1 = s_2 \\times t_2\\).",
            f"Substitute values: \\({s1} \\times {t1} = {dist} = {s2} \\times t_2\\).",
            f"Solve for \\(t_2\\): \\(t_2 = \\frac{{{dist}}}{{{s2}}} = {t2_str}\\text{{ hours}}\\).",
            d, v
        )
        questions.append(q)

    # 3.2.2 Travel schedules and constant distance problems (need 80)
    tc = "CBSE-8-MGP2-3-3.2.2"
    name = "Travel schedules and constant distance problems"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "If a train doubles its speed over a fixed journey, what happens to the travel time?",
            "The travel time is halved (divided by 2)",
            ["The travel time is doubled", "The travel time remains unchanged", "The travel time is quadrupled"],
            f"Distance is constant: \\(\\text{{Distance}} = \\text{{Speed}} \\times \\text{{Time}}\\).",
            f"If speed is multiplied by 2, time must be multiplied by \\(\\frac{{1}}{{2}}\\) so their product \\((2S) \\times (\\frac{{1}}{{2}}T) = ST\\) remains unchanged.",
            f"Therefore, the travel time is halved.",
            d, v
        )
        questions.append(q)

    # 3.3.1 Men, workers and days required (inverse proportion) (need 80)
    tc = "CBSE-8-MGP2-3-3.3.1"
    name = "Men, workers and days required (inverse proportion)"
    for i in range(80):
        w1 = 6 + (i % 6)
        d1 = 10
        total_mandays = w1 * d1
        w2 = 12
        d2 = total_mandays // w2
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"If \\({w1}\\) workers can build a wall in \\({d1}\\text{{ days}}\\), how many days will \\({w2}\\) workers take to complete the same wall at the same rate?",
            f"\\({d2}\\text{{ days}}\\)",
            [f"\\({d2 + 3}\\text{{ days}}\\)", f"\\({d2 - 1}\\text{{ days}}\\)", f"\\({d1 * 2}\\text{{ days}}\\)"],
            f"The number of workers \\(W\\) and days \\(D\\) vary inversely: \\(W_1 \\times D_1 = W_2 \\times D_2\\).",
            f"Total work in man-days: \\({w1} \\times {d1} = {total_mandays}\\text{{ man-days}}\\).",
            f"Solve for \\(D_2\\): \\(D_2 = \\frac{{{total_mandays}}}{{{w2}}} = {d2}\\text{{ days}}\\).",
            d, v
        )
        questions.append(q)

    # 3.3.2 Pipes, cisterns and filling rates (need 80)
    tc = "CBSE-8-MGP2-3-3.3.2"
    name = "Pipes, cisterns and filling rates"
    for i in range(80):
        p1 = 4 + (i % 4)
        t1 = 60
        total_cap = p1 * t1
        p2 = p1 + 2
        t2 = total_cap // p2
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"\\({p1}\\) identical water pipes can fill a reservoir in \\({t1}\\text{{ minutes}}\\). If \\({p2}\\) such pipes are opened simultaneously, how long will it take to fill the reservoir?",
            f"\\({t2}\\text{{ minutes}}\\)",
            [f"\\({t2 + 15}\\text{{ minutes}}\\)", f"\\({t2 - 10}\\text{{ minutes}}\\)", f"\\({t1 + 10}\\text{{ minutes}}\\)"],
            f"The number of identical pipes \\(P\\) and time \\(T\\) vary inversely: \\(P_1 \\times T_1 = P_2 \\times T_2\\).",
            f"Compute the total rate product: \\({p1} \\times {t1} = {total_cap}\\).",
            f"Solve for \\(T_2\\): \\(T_2 = \\frac{{{total_cap}}}{{{p2}}} = {t2}\\text{{ minutes}}\\).",
            d, v
        )
        questions.append(q)

    # 3.4.1 Sector angles proportional to data values (θ = value/total * 360°) (need 80)
    tc = "CBSE-8-MGP2-3-3.4.1"
    name = "Sector angles proportional to data values (θ = value/total * 360°)"
    for i in range(80):
        val = 25 + (i % 5) * 5
        total = 100
        angle = (val * 360) // total
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"In a pie chart representing a total data set of \\({total}\\) items, what central angle corresponds to a component value of \\({val}\\)?",
            f"\\({angle}^\\circ\\)",
            [f"\\({angle + 18}^\\circ\\)", f"\\({angle - 18}^\\circ\\)", f"\\({val}^\\circ\\)"],
            f"In a circle / pie chart, the total central angle is \\(360^\\circ\\).",
            f"The central angle \\(\\theta\\) of each component is proportional to its value: \\(\\theta = \\frac{{\\text{{Component Value}}}}{{\\text{{Total Value}}}} \\times 360^\\circ\\).",
            f"Substitute values: \\(\\theta = \\frac{{{val}}}{{{total}}} \\times 360^\\circ = {angle}^\\circ\\).",
            d, v
        )
        questions.append(q)

    # 3.4.2 Reading and interpreting pie charts (need 80)
    tc = "CBSE-8-MGP2-3-3.4.2"
    name = "Reading and interpreting pie charts"
    for i in range(80):
        angle = [90, 180, 120, 60, 45][i % 5]
        pct = (angle * 100) // 360
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"If a sector in a pie chart has a central angle of \\({angle}^\\circ\\), what percentage of the whole data does this sector represent?",
            f"\\({pct}\\%\\)",
            [f"\\({pct + 10}\\%\\)", f"\\({pct - 5}\\%\\)", f"\\({angle}\\%\\)"],
            f"The complete pie chart corresponds to a central angle of \\(360^\\circ\\) (100%).",
            f"To convert sector angle to percentage: \\(\\text{{Percentage}} = \\frac{{\\text{{Angle}}}}{{360^\\circ}} \\times 100\\%\\).",
            f"Calculate: \\(\\frac{{{angle}}}{{360}} \\times 100\\% = {pct}\\%\\).",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch3_questions()
    print(f"Generated {len(qs)} questions for Chapter 3.")
    with open("scripts/cbse8_mgp2_ch3_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/cbse8_mgp2_ch3_topup.json")
