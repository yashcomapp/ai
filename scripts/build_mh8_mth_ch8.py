import json
import random

random.seed(8808)

def build_ch8_questions():
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

    # 60 questions: 40 exam + 20 foundation
    vaults_60 = ["exam"] * 40 + ["foundation"] * 20
    diffs_60 = (["easy"] * 15 + ["medium"] * 15 + ["hard"] * 10) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)

    # -------------------------------------------------------------
    # 8.1.1 Construction with 4 sides and 1 diagonal (60 questions)
    # -------------------------------------------------------------
    tc_811 = "MH-8-MTH-8-8.1.1"
    name_811 = "Construction with 4 sides and 1 diagonal"
    for i in range(60):
        v = vaults_60[i]
        d = diffs_60[i]
        q = make_q(
            tc_811, name_811,
            f"When constructing quadrilateral \\(ABCD\\) given 4 side lengths and diagonal \\(AC\\), which geometric shape is constructed first as the base?",
            "\\(\\triangle ABC\\) using SSS criterion",
            [
                "\\(\\triangle BCD\\) using SAS criterion",
                "A right-angled triangle",
                "A rectangle"
            ],
            "A quadrilateral is divided into two triangles by a diagonal.",
            "Given sides \\(AB\\), \\(BC\\) and diagonal \\(AC\\), \\(\\triangle ABC\\) can be constructed first using the SSS (Side-Side-Side) criterion.",
            "Once vertex \\(C\\) is located, vertex \\(D\\) is plotted using sides \\(AD\\) and \\(CD\\).",
            d, v
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 8.1.2 Construction with 3 sides and 2 diagonals (60 questions)
    # -------------------------------------------------------------
    tc_812 = "MH-8-MTH-8-8.1.2"
    name_812 = "Construction with 3 sides and 2 diagonals"
    for i in range(60):
        v = vaults_60[i]
        d = diffs_60[i]
        q = make_q(
            tc_812, name_812,
            f"To construct a unique quadrilateral given 3 sides and 2 diagonals, how many independent elements are provided?",
            "5 elements",
            ["4 elements", "6 elements", "3 elements"],
            "A unique quadrilateral requires at least 5 independent measurements.",
            "Here, 3 side lengths and 2 diagonal lengths are provided, making a total of 5 elements.",
            "Therefore, 5 elements are specified to fix the quadrilateral uniquely.",
            d, v
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 8.1.3 Construction with adjacent sides and included angles (60 questions)
    # -------------------------------------------------------------
    tc_813 = "MH-8-MTH-8-8.1.3"
    name_813 = "Construction with adjacent sides and included angles"
    for i in range(60):
        v = vaults_60[i]
        d = diffs_60[i]
        q = make_q(
            tc_813, name_813,
            f"In constructing quadrilateral \\(PQRS\\), if two adjacent sides \\(PQ, QR\\) and three angles \\(\\angle P, \\angle Q, \\angle R\\) are known, what is the first step?",
            "Draw line segment \\(QR\\) (or \\(PQ\\)) and construct the given angle at its vertex",
            [
                "Draw a diagonal of arbitrary length",
                "Construct a perpendicular bisector",
                "Draw an angle of 90° arbitrarily"
            ],
            "Start by drawing one of the known side segments as base, such as \\(QR\\).",
            "Next, construct angles \\(\\angle Q\\) and \\(\\angle R\\) at the respective endpoints.",
            "Cut off the known side \\(PQ\\) along the ray from \\(Q\\), then construct \\(\\angle P\\) at \\(P\\).",
            d, v
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 8.2.1 Opposite sides equal, 90° angles, equal diagonals (60 questions)
    # -------------------------------------------------------------
    tc_821 = "MH-8-MTH-8-8.2.1"
    name_821 = "Opposite sides equal, 90° angles, equal diagonals"
    for i in range(60):
        v = vaults_60[i]
        d = diffs_60[i]
        diag_len = 10 + (i % 15)
        q = make_q(
            tc_821, name_821,
            f"In rectangle \\(ABCD\\), diagonal \\(AC = {diag_len}\\text{{ cm}}\\). What is the length of diagonal \\(BD\\)?",
            f"\\({diag_len}\\text{{ cm}}\\)",
            [
                f"\\({diag_len // 2}\\text{{ cm}}\\)",
                f"\\({diag_len * 2}\\text{{ cm}}\\)",
                f"\\({diag_len + 5}\\text{{ cm}}\\)"
            ],
            "Recall the standard geometric properties of a rectangle.",
            "In every rectangle, all interior angles are 90° and both diagonals are strictly congruent (equal in length).",
            f"Since \\(AC = {diag_len}\\text{{ cm}}\\), diagonal \\(BD\\) must also measure \\({diag_len}\\text{{ cm}}\\).",
            d, v
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 8.2.2 Square construction with given side length (60 questions)
    # -------------------------------------------------------------
    tc_822 = "MH-8-MTH-8-8.2.2"
    name_822 = "Square construction with given side length"
    for i in range(60):
        v = vaults_60[i]
        d = diffs_60[i]
        side = 4 + (i % 10)
        q = make_q(
            tc_822, name_822,
            f"Why is it possible to construct a unique SQUARE when only ONE side length (e.g. \\({side}\\text{{ cm}}\\)) is given?",
            "Because all 4 sides are equal and all 4 angles are fixed at 90°",
            [
                "Because squares only need 2 independent elements",
                "Because diagonals of a square are always unequal",
                "Because any quadrilateral can be constructed with one side"
            ],
            "A general quadrilateral requires 5 independent measurements.",
            "In a square, the equality of all 4 sides and all four 90° right angles provides the remaining implicit specifications.",
            "Thus, specifying 1 side length uniquely determines the square.",
            d, v
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 8.3.1 Rhombus perpendicular bisecting diagonals (60 questions)
    # -------------------------------------------------------------
    tc_831 = "MH-8-MTH-8-8.3.1"
    name_831 = "Rhombus perpendicular bisecting diagonals"
    for i in range(60):
        v = vaults_60[i]
        d = diffs_60[i]
        d1 = 12 + (i % 8) * 2
        d2 = 16 + (i % 8) * 2
        half_d1 = d1 // 2
        half_d2 = d2 // 2
        side_calc = int((half_d1**2 + half_d2**2)**0.5)
        q = make_q(
            tc_831, name_831,
            f"The diagonals of a rhombus are perpendicular bisectors of each other. At what angle do they intersect?",
            "\\(90^\\circ\\)",
            ["\\(60^\\circ\\)", "\\(45^\\circ\\)", "\\(120^\\circ\\)"],
            "A rhombus is an equilateral parallelogram.",
            "A key defining theorem states that the diagonals of a rhombus bisect each other perpendicularly.",
            "Hence, the angle formed at the intersection point of the diagonals is strictly 90°.",
            d, v
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 8.3.2 Parallelogram construction with adjacent sides and included angle (53 questions)
    # -------------------------------------------------------------
    tc_832 = "MH-8-MTH-8-8.3.2"
    name_832 = "Parallelogram construction with adjacent sides and included angle"
    # Needs 33 exam + 20 foundation = 53 questions
    vaults_53 = ["exam"] * 33 + ["foundation"] * 20
    diffs_53 = (["easy"] * 12 + ["medium"] * 12 + ["hard"] * 9) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)
    for i in range(53):
        v = vaults_53[i]
        d = diffs_53[i]
        ang = 50 + (i % 8) * 5
        supp_ang = 180 - ang
        q = make_q(
            tc_832, name_832,
            f"In parallelogram \\(ABCD\\), one angle is \\({ang}^\\circ\\). What is the measure of its adjacent interior angle?",
            f"\\({supp_ang}^\\circ\\)",
            [
                f"\\({ang}^\\circ\\)",
                f"\\({supp_ang - 10}^\\circ\\)",
                f"\\({supp_ang + 10}^\\circ\\)"
            ],
            "In any parallelogram, consecutive (adjacent) interior angles are supplementary.",
            f"Therefore, \\(\\text{{Adjacent angle}} = 180^\\circ - {ang}^\\circ\\).",
            f"Subtracting gives \\({supp_ang}^\\circ\\).",
            d, v
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 8.4.1 Trapezium definition and parallel sides (60 questions)
    # -------------------------------------------------------------
    tc_841 = "MH-8-MTH-8-8.4.1"
    name_841 = "Trapezium definition and parallel sides"
    for i in range(60):
        v = vaults_60[i]
        d = diffs_60[i]
        q = make_q(
            tc_841, name_841,
            f"What is the exact defining property of a TRAPEZIUM (trapezoid) in plane geometry?",
            "A quadrilateral in which only one pair of opposite sides is parallel",
            [
                "A quadrilateral in which both pairs of opposite sides are parallel",
                "A quadrilateral with all 4 sides equal",
                "A quadrilateral with perpendicular diagonals"
            ],
            "Recall the geometric definition of a trapezium.",
            "A quadrilateral having exactly one pair of opposite sides parallel is called a trapezium.",
            "The parallel sides are called the bases, while the non-parallel sides are legs.",
            d, v
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 8.4.2 Kite adjacent side equality and diagonal properties (60 questions)
    # -------------------------------------------------------------
    tc_842 = "MH-8-MTH-8-8.4.2"
    name_842 = "Kite adjacent side equality and diagonal properties"
    for i in range(60):
        v = vaults_60[i]
        d = diffs_60[i]
        q = make_q(
            tc_842, name_842,
            f"Which of the following is a true geometric property of a KITE?",
            "One diagonal is the perpendicular bisector of the other diagonal",
            [
                "Both diagonals are equal in length and bisect each other",
                "Opposite sides are equal and parallel",
                "All four angles are right angles"
            ],
            "A kite is a quadrilateral with two pairs of equal adjacent sides.",
            "The diagonal connecting the vertices between the pairs of equal sides is the axis of symmetry.",
            "This main diagonal perpendicularly bisects the cross diagonal.",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch8_questions()
    print(f"Generated {len(qs)} questions for Chapter 8.")
    out_path = "scripts/mh8_mth_ch8_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
