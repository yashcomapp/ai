import json
import random

random.seed(81717)

def build_ch17_questions():
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
    # 17.1.1 Perpendicular drawn from centre to chord bisects chord (80 questions)
    # -------------------------------------------------------------
    tc_1711 = "MH-8-MTH-17-17.1.1"
    name_1711 = "Perpendicular drawn from centre to chord bisects chord"
    chord_data = [
        (10, 6, 8, 16), (13, 5, 12, 24), (17, 8, 15, 30), (25, 7, 24, 48),
        (5, 3, 4, 8), (15, 9, 12, 24), (20, 12, 16, 32), (25, 15, 20, 40),
        (26, 10, 24, 48), (30, 18, 24, 48), (10, 8, 6, 12), (17, 15, 8, 16),
        (25, 20, 15, 30), (26, 24, 10, 20), (34, 16, 30, 60), (39, 15, 36, 72)
    ]
    for i in range(80):
        r, d, half_c, chord = chord_data[i % len(chord_data)]
        ans = f"\\({chord}\\text{{ cm}}\\)"
        w1 = f"\\({half_c}\\text{{ cm}}\\)"
        w2 = f"\\({chord + 4}\\text{{ cm}}\\)"
        w3 = f"\\({max(4, chord - 4)}\\text{{ cm}}\\)"
        
        q = make_q(
            tc_1711, name_1711,
            f"In a circle of radius \\(r = {r}\\text{{ cm}}\\), a perpendicular is drawn from the centre to a chord at a distance of \\({d}\\text{{ cm}}\\). What is the total length of the chord?",
            ans, [w1, w2, w3],
            f"The perpendicular drawn from the centre of a circle to a chord bisects the chord.",
            f"Using Pythagoras theorem in the right triangle formed by radius, perpendicular distance, and half-chord: \\(\\text{{half-chord}} = \\sqrt{{{r}^2 - {d}^2}} = \\sqrt{{{r**2} - {d**2}}} = {half_c}\\text{{ cm}}\\).",
            f"The total chord length is \\(2 \\times {half_c} = {ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 17.1.2 Segment joining centre and midpoint of chord is perpendicular to chord (80 questions)
    # -------------------------------------------------------------
    tc_1712 = "MH-8-MTH-17-17.1.2"
    name_1712 = "Segment joining centre and midpoint of chord is perpendicular to chord"
    for i in range(80):
        r, d, half_c, chord = chord_data[i % len(chord_data)]
        ans = f"\\({d}\\text{{ cm}}\\)"
        w1 = f"\\({d + 2}\\text{{ cm}}\\)"
        w2 = f"\\({max(1, d - 2)}\\text{{ cm}}\\)"
        w3 = f"\\({d * 2}\\text{{ cm}}\\)"
        
        q = make_q(
            tc_1712, name_1712,
            f"The radius of a circle is \\({r}\\text{{ cm}}\\) and a chord measures \\({chord}\\text{{ cm}}\\). Find the distance of the chord from the centre.",
            ans, [w1, w2, w3],
            f"The segment joining the centre to the midpoint of a chord is perpendicular to the chord, dividing it into half: \\(\\frac{{{chord}}}{{2}} = {half_c}\\text{{ cm}}\\).",
            f"Apply the Pythagoras theorem: \\(d = \\sqrt{{{r}^2 - {half_c}^2}} = \\sqrt{{{r**2} - {half_c**2}}} = \\sqrt{{{d**2}}}\\).",
            f"The perpendicular distance from the centre is \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 17.2.1 Minor arc, Major arc, and Semicircular arc (80 questions)
    # -------------------------------------------------------------
    tc_1721 = "MH-8-MTH-17-17.2.1"
    name_1721 = "Minor arc, Major arc, and Semicircular arc"
    arc_types = [
        ("An arc of a circle whose measure is strictly less than 180° is called:", "Minor arc", ["Major arc", "Semicircular arc", "Sector"]),
        ("An arc of a circle whose measure is strictly greater than 180° is called:", "Major arc", ["Minor arc", "Semicircular arc", "Segment"]),
        ("An arc of a circle whose measure is exactly equal to 180° is called:", "Semicircular arc", ["Minor arc", "Major arc", "Quadrant arc"]),
        ("The endpoints of a semicircular arc coincide with the endpoints of which line segment?", "A diameter of the circle", ["Any non-diameter chord", "A tangent line", "A secant line"])
    ]
    for i in range(80):
        ctx, ans, wrongs = arc_types[i % len(arc_types)]
        q = make_q(
            tc_1721, name_1721,
            f"Circle arc definitions: {ctx}",
            ans, wrongs,
            "Recall standard circle arc nomenclature based on angular measure.",
            "An arc smaller than a semicircle (< 180°) is a minor arc; greater than 180° is a major arc; exactly 180° is a semicircular arc.",
            f"Thus, the correct term is '{ans}'.",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 17.2.2 Central angle and measure of minor arc (80 questions)
    # -------------------------------------------------------------
    tc_1722 = "MH-8-MTH-17-17.2.2"
    name_1722 = "Central angle and measure of minor arc"
    angles_1722 = [40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 45, 65, 75, 85, 95, 105]
    for i in range(80):
        ang = angles_1722[i % len(angles_1722)]
        ans = f"\\({ang}^\\circ\\)"
        w1 = f"\\({180 - ang}^\\circ\\)"
        w2 = f"\\({360 - ang}^\\circ\\)"
        w3 = f"\\({ang // 2}^\\circ\\)"
        
        q = make_q(
            tc_1722, name_1722,
            f"In a circle with centre \\(O\\), the central angle \\(\\angle AOB\\) subtended by minor arc \\(AB\\) measures \\({ang}^\\circ\\). What is the measure of minor arc \\(AB\\)?",
            ans, [w1, w2, w3],
            "By definition, the measure of a minor arc is equal to the measure of its corresponding central angle.",
            f"Here, central angle \\(\\angle AOB = {ang}^\\circ\\).",
            f"Therefore, \\(m(\\text{{arc }} AB) = {ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 17.2.3 Measure of major arc = 360° - measure of minor arc (80 questions)
    # -------------------------------------------------------------
    tc_1723 = "MH-8-MTH-17-17.2.3"
    name_1723 = "Measure of major arc = 360° - measure of minor arc"
    for i in range(80):
        minor_ang = angles_1722[i % len(angles_1722)]
        major_ang = 360 - minor_ang
        ans = f"\\({major_ang}^\\circ\\)"
        w1 = f"\\({180 - minor_ang}^\\circ\\)"
        w2 = f"\\({minor_ang}^\\circ\\)"
        w3 = f"\\({major_ang - 20}^\\circ\\)"
        
        q = make_q(
            tc_1723, name_1723,
            f"The measure of a minor arc in a circle is \\({minor_ang}^\\circ\\). Find the measure of its corresponding major arc.",
            ans, [w1, w2, w3],
            f"The total angular measure of a complete circle is \\(360^\\circ\\).",
            f"The measure of a major arc is given by \\(m(\\text{{major arc}}) = 360^\\circ - m(\\text{{minor arc}})\\).",
            f"Calculate: \\(360^\\circ - {minor_ang}^\\circ = {ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 17.3.1 Arcs having equal measures and same radius are congruent (80 questions)
    # -------------------------------------------------------------
    tc_1731 = "MH-8-MTH-17-17.3.1"
    name_1731 = "Arcs having equal measures and same radius are congruent"
    arc_cong_q = [
        ("Two arcs of the same circle (or congruent circles) are congruent if and only if:", "Their measures (central angles) are equal", ["Their chords have different lengths", "One is major and the other is minor", "Their radii are unequal"]),
        ("If arc \\(AB\\) and arc \\(CD\\) in a circle of radius 6 cm both have measure 75°, then:", "\\(\\text{arc } AB \\cong \\text{arc } CD\\)", ["\\(\\text{arc } AB\\) is longer than \\(\\text{arc } CD\\)", "\\(\\text{arc } CD\\) is longer than \\(\\text{arc } AB\\)", "They cannot be compared"]),
        ("What two conditions are required for two circular arcs to be strictly congruent?", "Equal radii and equal angular measures", ["Equal radii only", "Equal angular measures in circles of any size", "Equal perimeter of enclosing circles only"]),
        ("In congruent circles with radius 8 cm, \\(m(\\text{arc } P) = 110^\\circ\\) and \\(m(\\text{arc } Q) = 110^\\circ\\). Are the arcs congruent?", "Yes, because both radius and measure are identical", ["No, because they are in separate circles", "No, because 110° is obtuse", "Only if their orientations match"])
    ]
    for i in range(80):
        ctx, ans, wrongs = arc_cong_q[i % len(arc_cong_q)]
        q = make_q(
            tc_1731, name_1731,
            f"Congruence of arcs: {ctx}",
            ans, wrongs,
            "Recall the geometric definition of congruent arcs.",
            "Two arcs are congruent if they have the same radius and identical angular measures.",
            f"Therefore, '{ans}' is the correct statement.",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 17.3.2 Chords corresponding to congruent arcs are congruent (80 questions)
    # -------------------------------------------------------------
    tc_1732 = "MH-8-MTH-17-17.3.2"
    name_1732 = "Chords corresponding to congruent arcs are congruent"
    chord_lens = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    for i in range(80):
        cl = chord_lens[i % len(chord_lens)]
        ans = f"\\({cl}\\text{{ cm}}\\)"
        w1 = f"\\({cl // 2}\\text{{ cm}}\\)"
        w2 = f"\\({cl * 2}\\text{{ cm}}\\)"
        w3 = f"\\({cl + 5}\\text{{ cm}}\\)"
        
        q = make_q(
            tc_1732, name_1732,
            f"In a circle, arc \\(AB \\cong\\) arc \\(CD\\). If chord \\(AB = {cl}\\text{{ cm}}\\), what is the length of chord \\(CD\\)?",
            ans, [w1, w2, w3],
            "A fundamental circle theorem states that chords corresponding to congruent arcs of a circle are congruent.",
            f"Since arc \\(AB \\cong\\) arc \\(CD\\), chord \\(AB \\cong\\) chord \\(CD\\).",
            f"Therefore, chord \\(CD = chord AB = {ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch17_questions()
    print(f"Generated {len(qs)} questions for Chapter 17.")
    out_path = "scripts/mh8_mth_ch17_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
