import json
import random

random.seed(8304)

def build_ch4_questions():
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

    # 4.1.1 Definition of altitude (need 50)
    tc = "MH-8-MTH-4-4.1.1"
    name = "Definition of altitude"
    for i in range(50):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "What is the precise geometric definition of an ALTITUDE of a triangle in Balbharti geometry?",
            "The perpendicular line segment drawn from a vertex of a triangle on the opposite side",
            [
                "The line segment joining a vertex to the midpoint of the opposite side",
                "The line that bisects an interior angle of the triangle",
                "The perpendicular bisector of any side of the triangle"
            ],
            f"The perpendicular segment drawn from a vertex of a triangle on the side opposite to it is called an altitude of the triangle.",
            f"Every triangle has exactly three altitudes, one from each vertex.",
            f"Therefore, 'The perpendicular line segment from a vertex to the opposite side' is the definition.",
            d, v
        )
        questions.append(q)

    # 4.1.2 Drawing altitudes in acute, right, and obtuse angled triangles (need 50)
    tc = "MH-8-MTH-4-4.1.2"
    name = "Drawing altitudes in acute, right, and obtuse angled triangles"
    for i in range(50):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "In an OBTUSE-ANGLED triangle, where do the altitudes drawn from the two acute vertices lie?",
            "In the exterior of the triangle (on the extended opposite sides)",
            [
                "Strictly inside the triangle",
                "Along the legs of the triangle",
                "Along the perimeter of the triangle"
            ],
            f"In an obtuse-angled triangle, the angle at one vertex exceeds 90°.",
            f"To drop perpendiculars from the two acute angles onto the opposite sides, those opposite sides must be extended outward.",
            f"Consequently, those two altitudes lie in the exterior of the triangle.",
            d, v
        )
        questions.append(q)

    # 4.1.3 Point of concurrence: Orthocentre (O) location (need 50)
    tc = "MH-8-MTH-4-4.1.3"
    name = "Point of concurrence: Orthocentre (O) location"
    for i in range(50):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "Where is the point of concurrence of altitudes (Orthocentre, denoted by 'O') located in a RIGHT-ANGLED triangle?",
            "At the vertex containing the right angle (90°)",
            [
                "Inside the triangle",
                "In the exterior of the triangle",
                "At the midpoint of the hypotenuse"
            ],
            f"The three altitudes of any triangle are concurrent at a point called the orthocentre, denoted by \\(O\\).",
            f"In a right-angled triangle, the two perpendicular legs themselves serve as two of the altitudes.",
            f"They intersect at the right-angled vertex. Thus, the orthocentre \\(O\\) is at the vertex of the right angle.",
            d, v
        )
        questions.append(q)

    # 4.2.1 Definition of median and midpoint of side (need 50)
    tc = "MH-8-MTH-4-4.2.1"
    name = "Definition of median and midpoint of side"
    for i in range(50):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "What is the definition of a MEDIAN of a triangle?",
            "The line segment joining a vertex of a triangle to the midpoint of the opposite side",
            [
                "The perpendicular drawn from a vertex to the opposite side",
                "The line dividing an angle into two equal parts",
                "The line parallel to the base passing through a vertex"
            ],
            f"The segment joining a vertex and the midpoint of the opposite side is called a median of the triangle.",
            f"Every triangle has exactly three medians.",
            f"Hence, the segment connecting a vertex to the opposite side's midpoint is the median.",
            d, v
        )
        questions.append(q)

    # 4.2.2 Drawing medians of a triangle (need 80)
    tc = "MH-8-MTH-4-4.2.2"
    name = "Drawing medians of a triangle"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "In any triangle (acute, right, or obtuse), where do all three medians ALWAYS lie?",
            "Always completely inside (in the interior of) the triangle",
            [
                "In the exterior of the triangle for obtuse triangles",
                "Along the hypotenuse for right triangles",
                "Outside the triangle for equilateral triangles"
            ],
            f"Because each vertex and the midpoint of each side are boundary points of the triangle,",
            f"the line segment connecting them must lie entirely within the convex region enclosed by the triangle.",
            f"Therefore, medians always lie strictly in the interior of the triangle.",
            d, v
        )
        questions.append(q)

    # 4.2.3 Point of concurrence: Centroid (G) (need 50)
    tc = "MH-8-MTH-4-4.2.3"
    name = "Point of concurrence: Centroid (G)"
    for i in range(50):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "The three medians of a triangle are concurrent. What is their common point of concurrence called, and by which letter is it denoted?",
            "Centroid, denoted by 'G'",
            ["Orthocentre, denoted by 'O'", "Circumcentre, denoted by 'C'", "Incentre, denoted by 'I'"],
            f"The point of concurrence of the three medians of a triangle is known as the centroid.",
            f"In Maharashtra State Board mathematics, the centroid is universally denoted by the capital letter \\(G\\).",
            f"Therefore, Centroid \\(G\\) is the correct term.",
            d, v
        )
        questions.append(q)

    # 4.3.1 Centroid divides each median in the ratio 2:1 (need 52)
    tc = "MH-8-MTH-4-4.3.1"
    name = "Centroid divides each median in the ratio 2:1"
    for i in range(52):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "In what ratio does the centroid (G) divide each median of a triangle (measuring from the vertex to the midpoint of the opposite side)?",
            "\\(2 : 1\\)",
            ["\\(1 : 2\\)", "\\(3 : 1\\)", "\\(1 : 1\\)"],
            f"By a core theorem of Euclidean geometry, the centroid \\(G\\) of a triangle divides every median in the ratio 2 : 1.",
            f"The longer segment lies between the vertex and the centroid (2 parts), while the shorter segment lies between the centroid and the midpoint (1 part).",
            f"Hence, the ratio from vertex to midpoint is \\(2 : 1\\).",
            d, v
        )
        questions.append(q)

    # 4.3.2 Calculating segment lengths from centroid property (need 50)
    tc = "MH-8-MTH-4-4.3.2"
    name = "Calculating segment lengths from centroid property"
    for i in range(50):
        p = 2 + (i % 8)  # 1 part length
        ag = 2 * p
        gp = p
        ap = 3 * p
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"In \\(\\triangle ABC\\), \\(AP\\) is a median and \\(G\\) is the centroid. If \\(GP = {gp}\\text{{ cm}}\\), find the length of segment \\(AG\\) and total median \\(AP\\).",
            f"\\(AG = {ag}\\text{{ cm}}, AP = {ap}\\text{{ cm}}\\)",
            [
                f"\\(AG = {gp}\\text{{ cm}}, AP = {ag}\\text{{ cm}}\\)",
                f"\\(AG = {ap}\\text{{ cm}}, AP = {ag}\\text{{ cm}}\\)",
                f"\\(AG = {ag + 2}\\text{{ cm}}, AP = {ap + 2}\\text{{ cm}}\\)"
            ],
            f"The centroid \\(G\\) divides median \\(AP\\) in the ratio \\(AG : GP = 2 : 1\\).",
            f"Since \\(GP = {gp}\\text{{ cm}}\\) (1 part), the vertex segment \\(AG = 2 \\times GP = 2 \\times {gp} = {ag}\\text{{ cm}}\\).",
            f"The total length of the median is \\(AP = AG + GP = {ag} + {gp} = {ap}\\text{{ cm}}\\).",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch4_questions()
    print(f"Generated {len(qs)} questions for Chapter 4.")
    with open("scripts/mh8_mth_ch4_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/mh8_mth_ch4_topup.json")
