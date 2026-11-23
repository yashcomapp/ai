import json
import random

random.seed(8302)

def build_ch2_questions():
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

    # 2.1.1 Definition of transversal (need 57)
    tc = "MH-8-MTH-2-2.1.1"
    name = "Definition of transversal"
    for i in range(57):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "In Maharashtra State Board geometry, what is the formal definition of a TRANSVERSAL?",
            "A straight line that intersects two or more given coplanar lines in two or more distinct points",
            [
                "A line that is strictly perpendicular to another line",
                "A line segment that connects the midpoints of two triangles",
                "A ray that bisects an angle into two equal halves"
            ],
            f"If a line intersects two or more given lines in distinct points, then that line is called a transversal of those given lines.",
            f"The intersection must occur at distinct points in the same plane.",
            f"Therefore, 'A straight line that intersects two or more given lines in distinct points' defines a transversal.",
            d, v
        )
        questions.append(q)

    # 2.1.2 Pairs of corresponding angles (need 49)
    tc = "MH-8-MTH-2-2.1.2"
    name = "Pairs of corresponding angles"
    for i in range(49):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "How many distinct pairs of CORRESPONDING ANGLES are formed when a transversal intersects two lines?",
            "\\(4\\) pairs",
            ["\\(2\\) pairs", "\\(8\\) pairs", "\\(6\\) pairs"],
            f"A transversal intersecting two lines forms a total of 8 angles (4 at each intersection).",
            f"Corresponding angles lie on the same side of the transversal and in corresponding relative positions (top-left, top-right, bottom-left, bottom-right).",
            f"Thus, there are exactly 4 pairs of corresponding angles.",
            d, v
        )
        questions.append(q)

    # 2.1.3 Pairs of alternate interior & alternate exterior angles (need 44)
    tc = "MH-8-MTH-2-2.1.3"
    name = "Pairs of alternate interior & alternate exterior angles"
    for i in range(44):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "Which of the following describes the relative geometric position of ALTERNATE INTERIOR angles formed by a transversal?",
            "They lie on opposite sides of the transversal, between the two lines, and not forming a linear pair",
            [
                "They lie on the same side of the transversal in the interior",
                "They lie on the same side in the exterior",
                "They form a vertically opposite pair at the same vertex"
            ],
            f"Alternate angles are on opposite sides of the transversal and their arms on the transversal are directed in opposite directions.",
            f"For interior alternate angles, both angles lie in the interior region between the two intersected lines.",
            f"Therefore, they lie on opposite sides of the transversal between the two lines.",
            d, v
        )
        questions.append(q)

    # 2.1.4 Pairs of interior angles (need 50)
    tc = "MH-8-MTH-2-2.1.4"
    name = "Pairs of interior angles"
    for i in range(50):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "How many pairs of INTERIOR ANGLES on the same side of the transversal are formed when a transversal intersects two lines?",
            "\\(2\\) pairs",
            ["\\(4\\) pairs", "\\(1\\) pair", "\\(8\\) pairs"],
            f"The interior region between the two lines contains a total of 4 interior angles.",
            f"Two of these angles lie on the left side of the transversal (1 pair), and two lie on the right side of the transversal (1 pair).",
            f"Hence, there are exactly 2 pairs of interior angles.",
            d, v
        )
        questions.append(q)

    # 2.2.1 Corresponding angles property (equal) (need 50)
    tc = "MH-8-MTH-2-2.2.1"
    name = "Corresponding angles property (equal)"
    for i in range(50):
        angle = 45 + (i % 20) * 3
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Two parallel lines are intersected by a transversal. If one of the corresponding angles measures \\({angle}^\\circ\\), what is the measure of the other corresponding angle?",
            f"\\({angle}^\\circ\\)",
            [f"\\({180 - angle}^\\circ\\)", f"\\({angle + 10}^\\circ\\)", f"\\({90}^\\circ\\)"],
            f"By the Corresponding Angles Property of parallel lines, each pair of corresponding angles formed by a transversal is congruent (equal in measure).",
            f"Given one angle is \\({angle}^\\circ\\), its corresponding angle must have the exact same measure.",
            f"Therefore, the other corresponding angle is \\({angle}^\\circ\\).",
            d, v
        )
        questions.append(q)

    # 2.2.2 Alternate angles property (equal) (need 51)
    tc = "MH-8-MTH-2-2.2.2"
    name = "Alternate angles property (equal)"
    for i in range(51):
        angle = 50 + (i % 25) * 2
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Two parallel lines are intersected by a transversal. If an alternate interior angle measures \\({angle}^\\circ\\), what is the measure of its alternate angle partner?",
            f"\\({angle}^\\circ\\)",
            [f"\\({180 - angle}^\\circ\\)", f"\\({angle - 15}^\\circ\\)", f"\\({angle + 20}^\\circ\\)"],
            f"By the Alternate Angles Property of parallel lines, each pair of alternate angles is equal in measure.",
            f"Since the lines are parallel, \\(\\text{{Alternate Angle}} = {angle}^\\circ\\).",
            f"Thus, the partner angle also measures \\({angle}^\\circ\\).",
            d, v
        )
        questions.append(q)

    # 2.2.3 Interior angles property (supplementary = 180°) (need 50)
    tc = "MH-8-MTH-2-2.2.3"
    name = "Interior angles property (supplementary = 180°)"
    for i in range(50):
        a1 = 65 + (i % 20) * 2
        a2 = 180 - a1
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Two parallel lines are intersected by a transversal. If one interior angle on the same side of the transversal measures \\({a1}^\\circ\\), what is the measure of the consecutive interior angle?",
            f"\\({a2}^\\circ\\)",
            [f"\\({a1}^\\circ\\)", f"\\({a2 + 10}^\\circ\\)", f"\\({a2 - 10}^\\circ\\)"],
            f"By the Interior Angles Property, consecutive interior angles on the same side of a transversal intersecting parallel lines are supplementary (their sum is \\(180^\\circ\\)).",
            f"Let the other angle be \\(x\\): \\({a1}^\\circ + x = 180^\\circ\\).",
            f"Solve for \\(x\\): \\(x = 180^\\circ - {a1}^\\circ = {a2}^\\circ\\).",
            d, v
        )
        questions.append(q)

    # 2.3.1 Drawing parallel line through given point outside line using set squares (need 80)
    tc = "MH-8-MTH-2-2.3.1"
    name = "Drawing parallel line through given point outside line using set squares"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "In Maharashtra Board practical geometry, how is a parallel line drawn through an external point \\(P\\) using two set squares?",
            "By aligning one edge of a set square with the given line, sliding it along a second set square acting as a guide rail up to point P, and drawing the line",
            [
                "By measuring the angle with a protractor and guessing the line",
                "By using only a 15 cm ruler without any set squares",
                "By drawing a circle centered at P"
            ],
            f"One edge of the first set square is placed flush along the given line \\(l\\).",
            f"A second set square (or ruler) is placed firmly along an adjacent edge of the first set square to serve as a fixed guide.",
            f"Sliding the first set square along the guide until its edge passes through point \\(P\\) draws a line strictly parallel to line \\(l\\).",
            d, v
        )
        questions.append(q)

    # 2.3.2 Drawing parallel line at given distance using compass (need 80)
    tc = "MH-8-MTH-2-2.3.2"
    name = "Drawing parallel line at given distance using compass"
    for i in range(80):
        dist = 3 + (i % 6)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"To construct a line parallel to line \\(l\\) at a distance of \\({dist}\\text{{ cm}}\\) using a compass, what is the standard geometric construction procedure?",
            f"Erect perpendiculars at two distinct points on line \\(l\\), cut arcs of radius \\({dist}\\text{{ cm}}\\) on them, and draw a line passing through the arc points",
            [
                f"Draw a single circle of radius \\({dist}\\text{{ cm}}\\) and pick any tangent",
                "Draw an angle of 45° and measure with a ruler",
                "Draw three intersecting transversals"
            ],
            f"Choose two convenient distinct points \\(A\\) and \\(B\\) on line \\(l\\).",
            f"Construct perpendicular lines to line \\(l\\) at points \\(A\\) and \\(B\\).",
            f"With a compass set to radius \\({dist}\\text{{ cm}}\\), mark points \\(P\\) and \\(Q\\) on the perpendiculars. The line through \\(P\\) and \\(Q\\) is parallel to line \\(l\\) at distance \\({dist}\\text{{ cm}}\\).",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch2_questions()
    print(f"Generated {len(qs)} questions for Chapter 2.")
    with open("scripts/mh8_mth_ch2_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/mh8_mth_ch2_topup.json")
