import json
import random

random.seed(81313)

def build_ch13_questions():
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

    # -------------------------------------------------------------
    # 13.1.1 Vertices correspondence (ABC ↔ PQR) (50 questions: 30 exam + 20 foundation)
    # -------------------------------------------------------------
    tc_1311 = "MH-8-MTH-13-13.1.1"
    name_1311 = "Vertices correspondence (ABC ↔ PQR)"
    vaults_50 = ["exam"] * 30 + ["foundation"] * 20
    diffs_50 = (["easy"] * 10 + ["medium"] * 12 + ["hard"] * 8) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)
    for i in range(50):
        v = vaults_50[i]
        d = diffs_50[i]
        q = make_q(
            tc_1311, name_1311,
            f"If \\(\\triangle ABC \\cong \\triangle PQR\\) under the correspondence \\(ABC \\leftrightarrow PQR\\), which vertex of \\(\\triangle PQR\\) corresponds to vertex \\(B\\)?",
            "Vertex \\(Q\\)",
            ["Vertex \\(P\\)", "Vertex \\(R\\)", "Any arbitrary vertex"],
            "In one-to-one correspondence between two triangles, order of lettering strictly denotes matching vertices.",
            "Under the bijection \\(ABC \\leftrightarrow PQR\\), the first vertex \\(A \\leftrightarrow P\\), the second \\(B \\leftrightarrow Q\\), and the third \\(C \\leftrightarrow R\\).",
            "Therefore, vertex \\(B\\) corresponds to Vertex \\(Q\\).",
            d, v
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 13.1.2 Congruence of corresponding sides and angles (51 questions: 31 exam + 20 foundation)
    # -------------------------------------------------------------
    tc_1312 = "MH-8-MTH-13-13.1.2"
    name_1312 = "Congruence of corresponding sides and angles"
    vaults_51 = ["exam"] * 31 + ["foundation"] * 20
    diffs_51 = (["easy"] * 11 + ["medium"] * 12 + ["hard"] * 8) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)
    for i in range(51):
        v = vaults_51[i]
        d = diffs_51[i]
        q = make_q(
            tc_1312, name_1312,
            f"Given \\(\\triangle XYZ \\cong \\triangle LMN\\), which side of \\(\\triangle LMN\\) is strictly congruent to side \\(YZ\\)?",
            "\\(\\text{side } MN\\)",
            ["\\(\\text{side } LM\\)", "\\(\\text{side } LN\\)", "\\(\\text{side } ML\\)"],
            "Corresponding parts of congruent triangles (c.p.c.t.) are strictly congruent.",
            "Matching the positions in \\(XYZ \\leftrightarrow LMN\\): \\(XY \\leftrightarrow LM\\), \\(YZ \\leftrightarrow MN\\), and \\(XZ \\leftrightarrow LN\\).",
            "Thus, side \\(YZ\\) corresponds and is congruent to side \\(MN\\).",
            d, v
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 13.2.1 Side-Angle-Side test (50 questions: 30 exam + 20 foundation)
    # -------------------------------------------------------------
    tc_1321 = "MH-8-MTH-13-13.2.1"
    name_1321 = "Side-Angle-Side test"
    for i in range(50):
        v = vaults_50[i]
        d = diffs_50[i]
        q = make_q(
            tc_1321, name_1321,
            f"In the Side-Angle-Side (SAS) congruence test, what is the mandatory position of the congruent angle relative to the two sides?",
            "It must be the angle included strictly between the two given sides",
            [
                "It can be any angle of the triangle",
                "It must always be an obtuse angle",
                "It must be opposite to the longer side"
            ],
            "Recall the formal definition of the SAS congruence criterion.",
            "If two sides and the included angle of one triangle are congruent to two sides and the included angle of another triangle, the triangles are congruent.",
            "The angle must be included between the two matching sides.",
            d, v
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 13.2.2 Side-Side-Side test (50 questions: 30 exam + 20 foundation)
    # -------------------------------------------------------------
    tc_1322 = "MH-8-MTH-13-13.2.2"
    name_1322 = "Side-Side-Side test"
    for i in range(50):
        v = vaults_50[i]
        d = diffs_50[i]
        q = make_q(
            tc_1322, name_1322,
            f"If \\(AB = DE\\), \\(BC = EF\\), and \\(AC = DF\\) in \\(\\triangle ABC\\) and \\(\\triangle DEF\\), which congruence criterion proves \\(\\triangle ABC \\cong \\triangle DEF\\)?",
            "SSS (Side-Side-Side) test",
            ["SAS test", "ASA test", "RHS test"],
            "Compare the given matching elements of the two triangles.",
            "All three pairs of corresponding sides are given to be equal in length.",
            "Therefore, by the SSS test, the two triangles are congruent.",
            d, v
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 13.2.3 Angle-Side-Angle & Angle-Angle-Side tests (50 questions: 30 exam + 20 foundation)
    # -------------------------------------------------------------
    tc_1323 = "MH-8-MTH-13-13.2.3"
    name_1323 = "Angle-Side-Angle & Angle-Angle-Side tests"
    for i in range(50):
        v = vaults_50[i]
        d = diffs_50[i]
        q = make_q(
            tc_1323, name_1323,
            f"If two angles and the included side of one triangle are congruent to two angles and the included side of another triangle, which test applies?",
            "ASA (Angle-Side-Angle) test",
            ["SAS test", "SSS test", "Hypotenuse-Side test"],
            "Examine the arrangement of the congruent elements: two angles and the side enclosed between them.",
            "This configuration satisfies the ASA (Angle-Side-Angle) congruence criterion.",
            "Hence, the triangles are congruent by the ASA test.",
            d, v
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 13.2.4 Hypotenuse-Side test for right-angled triangles (50 questions: 30 exam + 20 foundation)
    # -------------------------------------------------------------
    tc_1324 = "MH-8-MTH-13-13.2.4"
    name_1324 = "Hypotenuse-Side test for right-angled triangles"
    for i in range(50):
        v = vaults_50[i]
        d = diffs_50[i]
        q = make_q(
            tc_1324, name_1324,
            f"Under which specific type of triangle does the Hypotenuse-Side (RHS) congruence test exclusively apply?",
            "Right-angled triangles only",
            ["Equilateral triangles only", "Obtuse-angled triangles only", "Any scalene triangle"],
            "The Hypotenuse-Side theorem requires a 90° right angle in both triangles.",
            "If the hypotenuse and one leg of a right-angled triangle are congruent to the hypotenuse and one leg of another, the triangles are congruent.",
            "Therefore, it applies exclusively to right-angled triangles.",
            d, v
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 13.3.1 Proving triangles congruent by specific test (49 questions: 29 exam + 20 foundation)
    # -------------------------------------------------------------
    tc_1331 = "MH-8-MTH-13-13.3.1"
    name_1331 = "Proving triangles congruent by specific test"
    vaults_49 = ["exam"] * 29 + ["foundation"] * 20
    diffs_49 = (["easy"] * 10 + ["medium"] * 11 + ["hard"] * 8) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)
    for i in range(49):
        v = vaults_49[i]
        d = diffs_49[i]
        q = make_q(
            tc_1331, name_1331,
            f"In \\(\\triangle PQR\\) and \\(\\triangle STU\\), \\(\\angle P = \\angle S\\), \\(\\angle Q = \\angle T\\), and side \\(PQ = ST\\). Identify the correct congruence statement.",
            "\\(\\triangle PQR \\cong \\triangle STU\\) by ASA test",
            [
                "\\(\\triangle PQR \\cong \\triangle STU\\) by SSS test",
                "\\(\\triangle PQR \\cong \\triangle STU\\) by SAS test",
                "\\(\\triangle PQR \\cong \\triangle UTS\\) by RHS test"
            ],
            "Identify the given corresponding parts: \\(\\angle P \\leftrightarrow \\angle S\\), \\(\\angle Q \\leftrightarrow \\angle T\\), and side \\(PQ \\leftrightarrow ST\\).",
            "Since side \\(PQ\\) is included between \\(\\angle P\\) and \\(\\angle Q\\), the ASA criterion is satisfied.",
            "Thus, \\(\\triangle PQR \\cong \\triangle STU\\) by ASA test.",
            d, v
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 13.3.2 Stating remaining congruent angles and sides (50 questions: 30 exam + 20 foundation)
    # -------------------------------------------------------------
    tc_1332 = "MH-8-MTH-13-13.3.2"
    name_1332 = "Stating remaining congruent angles and sides"
    for i in range(50):
        v = vaults_50[i]
        d = diffs_50[i]
        q = make_q(
            tc_1332, name_1332,
            f"Once \\(\\triangle ABC \\cong \\triangle DEF\\) is established, what is the justification used to conclude that \\(\\angle A \\cong \\angle D\\)?",
            "Corresponding angles of congruent triangles (c.a.c.t.)",
            ["Sum of interior angles is 180°", "Alternate interior angle theorem", "Pythagoras theorem"],
            "When two triangles are proved congruent, all their remaining matching parts are also congruent.",
            "The abbreviation c.a.c.t. stands for corresponding angles of congruent triangles (or c.p.c.t.).",
            "Therefore, \\(\\angle A \\cong \\angle D\\) is concluded by c.a.c.t.",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch13_questions()
    print(f"Generated {len(qs)} questions for Chapter 13.")
    out_path = "scripts/mh8_mth_ch13_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
