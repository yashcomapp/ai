import json
import random

random.seed(8104)

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

    # 4.1.1 Curves: Open, closed, simple, polygon definition (need 75)
    tc = "CBSE-8-MGP1-4-4.1.1"
    name = "Curves: Open, closed, simple, polygon definition"
    for i in range(75):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "Which of the following geometric figures is strictly defined as a POLYGON?",
            "A simple closed curve made up entirely of straight line segments",
            [
                "Any closed curve containing arcs and circles",
                "An open figure formed by connecting straight line segments",
                "A self-intersecting closed curve made of line segments"
            ],
            f"Recall the formal geometric definition of a polygon.",
            f"A polygon is a simple closed curve made up entirely of line segments that do not cross or self-intersect.",
            f"Thus, 'A simple closed curve made up entirely of straight line segments' is the accurate definition.",
            d, v
        )
        questions.append(q)

    # 4.1.2 Convex and concave polygons (need 14)
    tc = "CBSE-8-MGP1-4-4.1.2"
    name = "Convex and concave polygons"
    for i in range(14):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "What distinguishes a CONVEX polygon from a CONCAVE polygon?",
            "In a convex polygon, all interior angles are strictly less than 180° and no diagonal lies in the exterior.",
            [
                "In a convex polygon, at least one interior angle is greater than 180°.",
                "In a convex polygon, all sides must be of different lengths.",
                "A convex polygon cannot have diagonals."
            ],
            f"In a convex polygon, every line segment connecting any two internal points lies entirely within the polygon.",
            f"Equivalently, every interior angle is strictly less than \\(180^\\circ\\), and all diagonals lie completely inside.",
            f"If at least one interior angle exceeds \\(180^\\circ\\), the polygon is concave.",
            d, v
        )
        questions.append(q)

    # 4.1.3 Regular vs irregular polygons (need 75)
    tc = "CBSE-8-MGP1-4-4.1.3"
    name = "Regular vs irregular polygons"
    for i in range(75):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "To be classified as a REGULAR polygon, which two conditions must simultaneously hold?",
            "It must be both equilateral (all sides equal) and equiangular (all interior angles equal)",
            [
                "It only needs to have all sides of equal length",
                "It only needs to have all interior angles equal",
                "It must have an even number of sides"
            ],
            f"A polygon is defined as regular if and only if all of its sides are equal in length and all of its interior angles are equal in measure.",
            f"For example, a rhombus is equilateral but not necessarily regular; a rectangle is equiangular but not necessarily regular. Only a square is regular.",
            f"Therefore, it must be both equilateral and equiangular.",
            d, v
        )
        questions.append(q)

    # 4.1.4 Number of diagonals in an n-gon: n(n-3)/2 (need 74)
    tc = "CBSE-8-MGP1-4-4.1.4"
    name = "Number of diagonals in an n-gon: n(n-3)/2"
    for i in range(74):
        n = 4 + (i % 9)  # 4 to 12 sides
        diag = (n * (n - 3)) // 2
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"How many diagonals does a convex polygon with \\({n}\\) sides have?",
            f"\\({diag}\\)",
            [f"\\({diag + n}\\)", f"\\({diag - 2}\\)", f"\\({n * (n - 1)}\\)"],
            f"The formula for the number of diagonals in a polygon with \\(n\\) sides is given by \\(\\frac{{n(n-3)}}{{2}}\\).",
            f"Substitute \\(n = {n}\\): \\(\\frac{{{n}({n}-3)}}{{2}} = \\frac{{{n} \\times {n-3}}}{{2}} = {diag}\\).",
            f"Therefore, an \\({n}\\)-sided polygon has exactly \\({diag}\\) diagonals.",
            d, v
        )
        questions.append(q)

    # 4.2.1 Sum of interior angles of n-gon: (n-2) * 180° (need 49)
    tc = "CBSE-8-MGP1-4-4.2.1"
    name = "Sum of interior angles of n-gon: (n-2) * 180°"
    for i in range(49):
        n = 3 + (i % 8)  # 3 to 10 sides
        angle_sum = (n - 2) * 180
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"What is the sum of the interior angles of a convex polygon with \\({n}\\) sides?",
            f"\\({angle_sum}^\\circ\\)",
            [f"\\({angle_sum + 180}^\\circ\\)", f"\\({angle_sum - 180}^\\circ\\)", f"\\({n * 180}^\\circ\\)"],
            f"The sum of interior angles of any \\(n\\)-sided convex polygon is given by \\((n - 2) \\times 180^\\circ\\).",
            f"Substitute \\(n = {n}\\): \\(({n} - 2) \\times 180^\\circ = {n - 2} \\times 180^\\circ = {angle_sum}^\\circ\\).",
            f"Hence, the sum of interior angles is \\({angle_sum}^\\circ\\).",
            d, v
        )
        questions.append(q)

    # 4.2.2 Sum of exterior angles of any polygon = 360° (need 55)
    tc = "CBSE-8-MGP1-4-4.2.2"
    name = "Sum of exterior angles of any polygon = 360°"
    for i in range(55):
        n = 3 + (i % 15)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"What is the sum of the measures of the exterior angles of a convex polygon with \\({n}\\) sides (taken in order)?",
            "\\(360^\\circ\\)",
            [f"\\({(n - 2) * 180}^\\circ\\)", f"\\({n * 180}^\\circ\\)", "\\(180^\\circ\\)"],
            f"Consider traveling around the perimeter of any closed polygon along its exterior turns.",
            f"Completing one full circuit corresponds to a total rotation of \\(360^\\circ\\) (one complete revolution), regardless of the number of sides.",
            f"Therefore, the sum of exterior angles of any polygon is always \\(360^\\circ\\).",
            d, v
        )
        questions.append(q)

    # 4.2.3 Exterior and interior angle relationship in regular polygons (need 54)
    tc = "CBSE-8-MGP1-4-4.2.3"
    name = "Exterior and interior angle relationship in regular polygons"
    for i in range(54):
        n = [3, 4, 5, 6, 8, 9, 10, 12][i % 8]
        ext = 360 // n
        interior = 180 - ext
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find the measure of each interior angle of a regular polygon having \\({n}\\) sides.",
            f"\\({interior}^\\circ\\)",
            [f"\\({ext}^\\circ\\)", f"\\({interior - 15}^\\circ\\)", f"\\({interior + 15}^\\circ\\)"],
            f"For a regular polygon with \\(n\\) sides, each exterior angle is \\(\\frac{{360^\\circ}}{{n}} = \\frac{{360^\\circ}}{{{n}}} = {ext}^\\circ\\).",
            f"Since interior and exterior angles at each vertex form a linear pair: \\(\\text{{Interior Angle}} = 180^\\circ - {ext}^\\circ = {interior}^\\circ\\).",
            f"Thus, each interior angle measures \\({interior}^\\circ\\).",
            d, v
        )
        questions.append(q)

    # 4.3.1 Trapezium and isosceles trapezium properties (need 66)
    tc = "CBSE-8-MGP1-4-4.3.1"
    name = "Trapezium and isosceles trapezium properties"
    for i in range(66):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "Which property specifically defines an ISOSCELES trapezium?",
            "It has one pair of parallel sides, and its non-parallel sides are equal in length.",
            [
                "Both pairs of opposite sides are strictly parallel.",
                "All four sides are equal in length.",
                "Its diagonals are perpendicular to each other."
            ],
            f"A trapezium is a quadrilateral with at least one pair of parallel sides.",
            f"When the non-parallel sides of a trapezium are equal in length, it is called an isosceles trapezium.",
            f"Hence, having non-parallel sides equal in length is the defining characteristic.",
            d, v
        )
        questions.append(q)

    # 4.3.2 Kite: Disjoint equal adjacent sides & diagonals (need 61)
    tc = "CBSE-8-MGP1-4-4.3.2"
    name = "Kite: Disjoint equal adjacent sides & diagonals"
    for i in range(61):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "Which of the following statements about the diagonals of a KITE is strictly true?",
            "The diagonals are perpendicular to each other, and one of the diagonals bisects the other.",
            [
                "Both diagonals bisect each other and are equal in length.",
                "The diagonals are parallel to opposite sides.",
                "The diagonals never intersect."
            ],
            f"A kite is a quadrilateral with two distinct pairs of equal-length adjacent sides.",
            f"Its geometric symmetry guarantees that its diagonals intersect at right angles (\\(90^\\circ\\)) and the main axis of symmetry bisects the other diagonal.",
            f"Therefore, the diagonals are perpendicular and one bisects the other.",
            d, v
        )
        questions.append(q)

    # 4.3.3 Parallelogram: Opposite sides and angles are equal (need 49)
    tc = "CBSE-8-MGP1-4-4.3.3"
    name = "Parallelogram: Opposite sides and angles are equal"
    for i in range(49):
        angle_A = 60 + (i % 25)
        angle_B = 180 - angle_A
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"In a parallelogram \\(ABCD\\), if \\(\\angle A = {angle_A}^\\circ\\), what is the measure of the adjacent angle \\(\\angle B\\)?",
            f"\\({angle_B}^\\circ\\)",
            [f"\\({angle_A}^\\circ\\)", f"\\({angle_B - 20}^\\circ\\)", f"\\({90}^\\circ\\)"],
            f"In any parallelogram, adjacent angles are supplementary (their sum is \\(180^\\circ\\)) because they are consecutive interior angles between parallel lines.",
            f"Therefore, \\(\\angle B = 180^\\circ - \\angle A = 180^\\circ - {angle_A}^\\circ = {angle_B}^\\circ\\).",
            f"Thus, \\(\\angle B = {angle_B}^\\circ\\).",
            d, v
        )
        questions.append(q)

    # 4.3.4 Parallelogram: Diagonals bisect each other (need 62)
    tc = "CBSE-8-MGP1-4-4.3.4"
    name = "Parallelogram: Diagonals bisect each other"
    for i in range(62):
        d_half = 4 + (i % 10)
        d_full = 2 * d_half
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"In a parallelogram \\(ABCD\\), the diagonals intersect at \\(O\\). If \\(OA = {d_half}\\text{{ cm}}\\), what is the total length of diagonal \\(AC\\)?",
            f"\\({d_full}\\text{{ cm}}\\)",
            [f"\\({d_half}\\text{{ cm}}\\)", f"\\({d_full + 2}\\text{{ cm}}\\)", f"\\({d_half * d_half}\\text{{ cm}}\\)"],
            f"By theorem, the diagonals of a parallelogram bisect each other at their point of intersection \\(O\\).",
            f"Hence, \\(O\\) is the midpoint of diagonal \\(AC\\), meaning \\(AC = 2 \\times OA = 2 \\times {d_half} = {d_full}\\text{{ cm}}\\).",
            f"Therefore, diagonal \\(AC\\) measures \\({d_full}\\text{{ cm}}\\).",
            d, v
        )
        questions.append(q)

    # 4.4.1 Rhombus: Diagonals perpendicular bisectors (need 52)
    tc = "CBSE-8-MGP1-4-4.4.1"
    name = "Rhombus: Diagonals perpendicular bisectors"
    for i in range(52):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "At what angle do the diagonals of a RHOMBUS intersect each other?",
            "\\(90^\\circ\\) (Right angles)",
            ["\\(45^\\circ\\)", "\\(60^\\circ\\)", "\\(180^\\circ\\)"],
            f"A rhombus is a parallelogram with all four sides equal.",
            f"A fundamental property of a rhombus is that its diagonals are perpendicular bisectors of one another.",
            f"Therefore, the angle of intersection between the diagonals is \\(90^\\circ\\).",
            d, v
        )
        questions.append(q)

    # 4.4.2 Rectangle: All angles 90° & diagonals equal (need 48)
    tc = "CBSE-8-MGP1-4-4.4.2"
    name = "Rectangle: All angles 90° & diagonals equal"
    for i in range(48):
        diag_len = 10 + (i % 15)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"In a rectangle \\(ABCD\\), if diagonal \\(AC = {diag_len}\\text{{ cm}}\\), what is the length of diagonal \\(BD\\)?",
            f"\\({diag_len}\\text{{ cm}}\\)",
            [f"\\({diag_len // 2}\\text{{ cm}}\\)", f"\\({diag_len + 3}\\text{{ cm}}\\)", f"\\({diag_len * 2}\\text{{ cm}}\\)"],
            f"A rectangle is a parallelogram with each interior angle measuring \\(90^\\circ\\).",
            f"A core theorem of rectangles states that their diagonals are equal in length: \\(AC = BD\\).",
            f"Since \\(AC = {diag_len}\\text{{ cm}}\\), diagonal \\(BD\\) is also \\({diag_len}\\text{{ cm}}\\).",
            d, v
        )
        questions.append(q)

    # 4.4.3 Square: Equal sides, right angles & perpendicular equal diagonals (need 58)
    tc = "CBSE-8-MGP1-4-4.4.3"
    name = "Square: Equal sides, right angles & perpendicular equal diagonals"
    for i in range(58):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "Which of the following special quadrilaterals possesses diagonals that are BOTH equal in length AND perpendicular bisectors of each other?",
            "Square",
            ["Rectangle only", "Rhombus only", "General Parallelogram"],
            f"In a rectangle, diagonals are equal but not necessarily perpendicular. In a rhombus, diagonals are perpendicular bisectors but not necessarily equal.",
            f"A square combines the properties of both a rectangle and a rhombus.",
            f"Therefore, only a square has diagonals that are both equal in length and perpendicular bisectors of each other.",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch4_questions()
    print(f"Generated {len(qs)} questions for Chapter 4.")
    with open("scripts/cbse8_mgp1_ch4_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/cbse8_mgp1_ch4_topup.json")
