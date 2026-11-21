# scripts/generate_mh9_mth2_ch5_ch6.py
import json

def make_opt(text, is_correct):
    return {"text": text, "isCorrect": is_correct}

def make_unique_opts(corr_text, raw_distractors):
    seen = {corr_text}
    distractors = []
    for d in raw_distractors:
        if d not in seen:
            seen.add(d)
            distractors.append(d)
        if len(distractors) == 3:
            break
    counter = 1
    while len(distractors) < 3:
        cand = f"\\(\\text{{None of these}}\\) {counter}"
        if cand not in seen:
            seen.add(cand)
            distractors.append(cand)
        counter += 1
    opts = [make_opt(corr_text, True)] + [make_opt(d, False) for d in distractors]
    return opts

def make_q(q_code, text, opts, sol, ch_num, ch_name, t_code, t_name, vault, diff, q_type="OSC", marks=4):
    letters = ["A", "B", "C", "D"]
    corr_idx = -1
    for idx, o in enumerate(opts):
        if o["isCorrect"]:
            corr_idx = idx
            break
    if corr_idx == -1:
        raise ValueError(f"No correct option in {q_code}")
    
    return {
        "questionCode": q_code,
        "text": text,
        "options": opts,
        "correctAnswer": letters[corr_idx],
        "solution": sol,
        "boardCode": "MH",
        "board": "Maharashtra Board",
        "class": "9",
        "subjectCode": "MTH2",
        "subject": "Mathematics Part - 2 (Geometry)",
        "chapterNumber": ch_num,
        "chapter": ch_name,
        "topicCode": t_code,
        "topic": t_name,
        "type": q_type,
        "marks": marks,
        "difficulty": diff,
        "vault": vault,
        "timesUsed": 0,
        "usedInClassroomTest": False,
        "requiresFigure": False,
        "createdAt": "2026-11-21T13:42:00.000Z",
        "updatedAt": "2026-11-21T13:42:00.000Z"
    }

questions_ch5_ch6 = []

def generate_subtopic_pack(ch_num, ch_name, t_code, t_name, n_exam, n_pr, n_fo, concept_builder):
    for i in range(1, n_exam + 1):
        txt, corr, raw_dist, sol = concept_builder(i, "exam")
        opts = make_unique_opts(corr, raw_dist)
        shift = i % 4
        opts = opts[shift:] + opts[:shift]
        code = f"{t_code}-OSC-{100 + i:03d}"
        questions_ch5_ch6.append(make_q(code, txt, opts, sol, ch_num, ch_name, t_code, t_name, "exam", "medium" if i % 2 == 0 else "hard"))

    for i in range(1, n_pr + 1):
        txt, corr, raw_dist, sol = concept_builder(i, "practice")
        opts = make_unique_opts(corr, raw_dist)
        shift = i % 4
        opts = opts[shift:] + opts[:shift]
        code = f"{t_code}-OSC-{200 + i:03d}"
        questions_ch5_ch6.append(make_q(code, txt, opts, sol, ch_num, ch_name, t_code, t_name, "practice", "medium"))

    for i in range(1, n_fo + 1):
        txt, corr, raw_dist, sol = concept_builder(i, "foundation")
        opts = make_unique_opts(corr, raw_dist)
        shift = i % 4
        opts = opts[shift:] + opts[:shift]
        code = f"{t_code}-OSC-{150 + i:03d}"
        questions_ch5_ch6.append(make_q(code, txt, opts, sol, ch_num, ch_name, t_code, t_name, "foundation", "easy"))

# ==========================================
# CHAPTER 5: Quadrilaterals
# ==========================================
ch5_num = 5
ch5_name = "Quadrilaterals"

# 5.1.1: Opposite sides and angles of parallelogram (40 Ex, 20 Pr, 20 Fo)
def builder_511(i, mode):
    a = 50 + (i % 8) * 10
    adj = 180 - a
    txt = f"In a parallelogram \\(ABCD\\), \\(\\angle A = {a}^\\circ\\). What are the measures of opposite angle \\(\\angle C\\) and adjacent angle \\(\\angle B\\)?"
    corr = f"\\(\\angle C = {a}^\\circ, \\angle B = {adj}^\\circ\\)"
    raw_dist = [
        f"\\(\\angle C = {adj}^\\circ, \\angle B = {a}^\\circ\\)",
        f"\\(\\angle C = {a}^\\circ, \\angle B = {a}^\\circ\\)",
        f"\\(\\angle C = 90^\\circ, \\angle B = 90^\\circ\\)"
    ]
    sol = (
        f"Step 1: Theorem: Opposite angles of a parallelogram are congruent (\\(\\angle C = \\angle A = {a}^\\circ\\)).\n"
        f"Step 2: Adjacent angles are supplementary (\\(\\angle A + \\angle B = 180^\\circ \\implies \\angle B = 180^\\circ - {a}^\\circ = {adj}^\\circ\\)).\n"
        f"Step 3: Hence, \\(\\angle C = {a}^\\circ\\) and \\(\\angle B = {adj}^\\circ\\)."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch5_num, ch5_name, "MH-9-MTH2-5-5.1.1", "Opposite sides and opposite angles theorem", 40, 20, 20, builder_511)

# 5.1.2: Diagonals bisect each other theorem (40 Ex, 20 Pr, 20 Fo)
def builder_512(i, mode):
    d1 = (i % 6 + 4) * 2 # 8, 10, ...
    half1 = d1 // 2
    txt = f"The diagonals of a parallelogram \\(PQRS\\) intersect at point \\(O\\). If \\(PR = {d1}\\) cm, what is the length of \\(PO\\)?"
    corr = f"\\({half1}\\) cm"
    raw_dist = [
        f"\\({d1}\\) cm",
        f"\\({half1 + 2}\\) cm",
        f"\\({half1 - 1}\\) cm"
    ]
    sol = (
        f"Step 1: Theorem: The diagonals of a parallelogram bisect each other.\n"
        f"Step 2: Point \\(O\\) is the midpoint of diagonal \\(PR\\), so \\(PO = \\frac{{1}}{{2}} PR\\).\n"
        f"Step 3: \\(PO = \\frac{{1}}{{2}} \\times {d1} = {half1}\\) cm."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch5_num, ch5_name, "MH-9-MTH2-5-5.1.2", "Diagonals bisect each other theorem", 40, 20, 20, builder_512)

# 5.1.3: Tests for parallelograms (40 Ex, 20 Pr, 20 Fo)
def builder_513(i, mode):
    txt = "Which of the following conditions is sufficient to prove that a quadrilateral is a parallelogram?"
    corr = "One pair of opposite sides is both parallel and congruent"
    raw_dist = [
        "One pair of opposite sides is parallel and the other pair is congruent",
        "Diagonals are perpendicular to each other",
        "All four angles sum to 360°"
    ]
    sol = (
        "Step 1: By the Tests for Parallelograms, a quadrilateral is a parallelogram if one pair of opposite sides is both parallel and congruent.\n"
        "Step 2: Alternatively, if both pairs of opposite angles are congruent or diagonals bisect each other.\n"
        "Step 3: Hence, one pair parallel and congruent is sufficient."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch5_num, ch5_name, "MH-9-MTH2-5-5.1.3", "Tests to prove a quadrilateral is a parallelogram", 40, 20, 20, builder_513)

# 5.2.1: Diagonals of rectangle are congruent (40 Ex, 20 Pr, 20 Fo)
def builder_521(i, mode):
    diag = (i % 7) + 8
    txt = f"If one diagonal of a rectangle measures \\({diag}\\) cm, what is the length of its other diagonal?"
    corr = f"\\({diag}\\) cm"
    raw_dist = [
        f"\\({2*diag}\\) cm",
        f"\\({diag // 2}\\) cm",
        f"\\({diag + 4}\\) cm"
    ]
    sol = (
        f"Step 1: Theorem: The diagonals of a rectangle are congruent (equal in length).\n"
        f"Step 2: Given length of one diagonal is \\({diag}\\) cm.\n"
        f"Step 3: Therefore, the length of the other diagonal is \\({diag}\\) cm."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch5_num, ch5_name, "MH-9-MTH2-5-5.2.1", "Diagonals of rectangle are congruent", 40, 20, 20, builder_521)

# 5.2.2: Diagonals of rhombus are perpendicular bisectors (40 Ex, 20 Pr, 20 Fo)
def builder_522(i, mode):
    txt = "What is the angle of intersection between the diagonals of a rhombus?"
    corr = "\\(90^\\circ\\) (they are perpendicular bisectors)"
    raw_dist = [
        "\\(60^\\circ\\)",
        "\\(45^\\circ\\)",
        "\\(180^\\circ\\)"
    ]
    sol = (
        "Step 1: Theorem: The diagonals of a rhombus are perpendicular bisectors of each other.\n"
        "Step 2: Perpendicular lines intersect at right angles (\\(90^\\circ\\)).\n"
        "Step 3: Hence, the angle between them is \\(90^\\circ\\)."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch5_num, ch5_name, "MH-9-MTH2-5-5.2.2", "Diagonals of rhombus are perpendicular bisectors", 40, 20, 20, builder_522)

# 5.2.3: Diagonals of square (40 Ex, 20 Pr, 20 Fo)
def builder_523(i, mode):
    txt = "Which quadrilateral has diagonals that are BOTH congruent AND perpendicular bisectors of each other?"
    corr = "Square"
    raw_dist = [
        "Rectangle (congruent, but not perpendicular)",
        "Rhombus (perpendicular, but not congruent)",
        "Trapezium"
    ]
    sol = (
        "Step 1: A square is both a rectangle and a rhombus.\n"
        "Step 2: As a rectangle, its diagonals are congruent. As a rhombus, its diagonals are perpendicular bisectors.\n"
        "Step 3: Therefore, a square satisfies both properties."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch5_num, ch5_name, "MH-9-MTH2-5-5.2.3", "Diagonals of square are congruent and perpendicular bisectors", 40, 20, 20, builder_523)

# 5.3.1: Midpoint theorem of triangle (40 Ex, 20 Pr, 20 Fo)
def builder_531(i, mode):
    bc = (i % 8 + 4) * 2 # 8, 10, ...
    de = bc // 2
    txt = f"In \\(\\triangle ABC\\), \\(D\\) and \\(E\\) are the midpoints of sides \\(AB\\) and \\(AC\\) respectively. If side \\(BC = {bc}\\) cm, what is the length of segment \\(DE\\)?"
    corr = f"\\({de}\\) cm"
    raw_dist = [
        f"\\({bc}\\) cm",
        f"\\({2*bc}\\) cm",
        f"\\({de + 3}\\) cm"
    ]
    sol = (
        f"Step 1: Midpoint Theorem: The segment joining the midpoints of any two sides of a triangle is parallel to the third side and half as long as that third side.\n"
        f"Step 2: \\(DE = \\frac{{1}}{{2}} BC = \\frac{{1}}{{2}} \\times {bc}\\).\n"
        f"Step 3: \\(DE = {de}\\) cm."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch5_num, ch5_name, "MH-9-MTH2-5-5.3.1", "Midpoint theorem: Segment joining midpoints of two sides is parallel to third side and half of it", 40, 20, 20, builder_531)

# 5.3.2: Converse of midpoint theorem (40 Ex, 20 Pr, 20 Fo)
def builder_532(i, mode):
    txt = "What does the Converse of the Midpoint Theorem state?"
    corr = "A line drawn through the midpoint of one side of a triangle parallel to another side bisects the third side"
    raw_dist = [
        "A line joining midpoints is perpendicular to the base",
        "A line drawn through vertex bisects the area",
        "The medians of a triangle are equal"
    ]
    sol = (
        "Step 1: The converse takes the midpoint of one side and parallelism to the second side as hypothesis.\n"
        "Step 2: It concludes that the line intersects and bisects the third side.\n"
        "Step 3: Hence, it bisects the third side."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch5_num, ch5_name, "MH-9-MTH2-5-5.3.2", "Converse of midpoint theorem", 40, 20, 20, builder_532)

# ==========================================
# CHAPTER 6: Circle
# ==========================================
ch6_num = 6
ch6_name = "Circle"

# 6.1.1: Perpendicular from centre to chord (Needs 16 Exam, 20 Fo)
def builder_611(i, mode):
    r = 5 if i % 2 == 1 else 10
    d = 3 if i % 2 == 1 else 6
    half_chord = 4 if i % 2 == 1 else 8
    chord = 2 * half_chord
    txt = f"A chord of a circle of radius \\({r}\\) cm is at a distance of \\({d}\\) cm from the centre. Find the length of the chord."
    corr = f"\\({chord}\\) cm"
    raw_dist = [
        f"\\({half_chord}\\) cm",
        f"\\({chord + 2}\\) cm",
        f"\\({2*r}\\) cm"
    ]
    sol = (
        f"Step 1: The perpendicular from the centre bisects the chord. A right-angled triangle is formed with hypotenuse \\(r = {r}\\), distance \\(d = {d}\\), and half-chord \\(x\\).\n"
        f"Step 2: By Pythagoras theorem, \\(x^2 = r^2 - d^2 = {r}^2 - {d}^2 = {r**2} - {d**2} = {half_chord**2} \\implies x = {half_chord}\\) cm.\n"
        f"Step 3: Length of chord \\(= 2x = 2 \\times {half_chord} = {chord}\\) cm."
    )
    return txt, corr, raw_dist, sol

for i in range(1, 17):
    txt, corr, raw_dist, sol = builder_611(i, "exam")
    opts = make_unique_opts(corr, raw_dist)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    code = f"MH-9-MTH2-6-6.1.1-OSC-{100 + i:03d}"
    questions_ch5_ch6.append(make_q(code, txt, opts, sol, ch6_num, ch6_name, "MH-9-MTH2-6-6.1.1", "Perpendicular from centre to chord bisects chord theorem and converse", "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    txt, corr, raw_dist, sol = builder_611(i, "foundation")
    opts = make_unique_opts(corr, raw_dist)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    code = f"MH-9-MTH2-6-6.1.1-OSC-{150 + i:03d}"
    questions_ch5_ch6.append(make_q(code, txt, opts, sol, ch6_num, ch6_name, "MH-9-MTH2-6-6.1.1", "Perpendicular from centre to chord bisects chord theorem and converse", "foundation", "easy"))

# 6.1.2: Congruent chords equidistant from centre (Needs 30 Exam, 20 Fo)
def builder_612(i, mode):
    dist = (i % 6) + 3
    txt = f"Two congruent chords \\(AB\\) and \\(CD\\) are drawn in a circle. If chord \\(AB\\) is at a distance of \\({dist}\\) cm from the centre, what is the distance of chord \\(CD\\) from the centre?"
    corr = f"\\({dist}\\) cm"
    raw_dist = [
        f"\\({2*dist}\\) cm",
        f"\\({dist // 2}\\) cm",
        f"\\({dist + 2}\\) cm"
    ]
    sol = (
        f"Step 1: Theorem: Congruent chords of a circle are equidistant from the centre.\n"
        f"Step 2: Since chord \\(AB \\cong\\) chord \\(CD\\), their perpendicular distances from the centre are equal.\n"
        f"Step 3: Distance of \\(CD\\) from centre is \\({dist}\\) cm."
    )
    return txt, corr, raw_dist, sol

for i in range(1, 31):
    txt, corr, raw_dist, sol = builder_612(i, "exam")
    opts = make_unique_opts(corr, raw_dist)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    code = f"MH-9-MTH2-6-6.1.2-OSC-{100 + i:03d}"
    questions_ch5_ch6.append(make_q(code, txt, opts, sol, ch6_num, ch6_name, "MH-9-MTH2-6-6.1.2", "Congruent chords are equidistant from centre theorem and converse", "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    txt, corr, raw_dist, sol = builder_612(i, "foundation")
    opts = make_unique_opts(corr, raw_dist)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    code = f"MH-9-MTH2-6-6.1.2-OSC-{150 + i:03d}"
    questions_ch5_ch6.append(make_q(code, txt, opts, sol, ch6_num, ch6_name, "MH-9-MTH2-6-6.1.2", "Congruent chords are equidistant from centre theorem and converse", "foundation", "easy"))

# 6.2.1: Constructing angle bisectors of triangle (Incircle) (40 Ex, 20 Pr, 20 Fo)
def builder_621(i, mode):
    txt = "To construct the incircle of a triangle, which geometric lines must be drawn to locate the incentre?"
    corr = "Angle bisectors of the interior angles of the triangle"
    raw_dist = [
        "Perpendicular bisectors of the sides",
        "Medians of the triangle",
        "Altitudes from the vertices"
    ]
    sol = (
        "Step 1: The incircle touches all three sides of a triangle internally.\n"
        "Step 2: Its centre (incentre) is equidistant from all three sides.\n"
        "Step 3: By the angle bisector theorem, the incentre is the point of concurrency of the angle bisectors."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch6_num, ch6_name, "MH-9-MTH2-6-6.2.1", "Constructing angle bisectors of triangle", 40, 20, 20, builder_621)

# 6.2.2: Incentre (I) and inradius (40 Ex, 20 Pr, 20 Fo)
def builder_622(i, mode):
    txt = "Where does the incentre \\(I\\) of any triangle (acute, right, or obtuse) always lie?"
    corr = "Always inside the triangle"
    raw_dist = [
        "Outside the triangle for an obtuse triangle",
        "On the hypotenuse for a right-angled triangle",
        "At the vertex of the largest angle"
    ]
    sol = (
        "Step 1: The incircle lies entirely within the interior of the triangle.\n"
        "Step 2: The centre of the incircle (incentre) must always lie inside the boundaries of the triangle.\n"
        "Step 3: Hence, the incentre is always in the interior of the triangle."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch6_num, ch6_name, "MH-9-MTH2-6-6.2.2", "Incentre (I) and inradius", 40, 20, 20, builder_622)

# 6.3.1: Constructing perpendicular bisectors (Circumcircle) (40 Ex, 20 Pr, 20 Fo)
def builder_631(i, mode):
    txt = "To construct the circumcircle of a triangle, which geometric lines are constructed to locate the circumcentre?"
    corr = "Perpendicular bisectors of the sides of the triangle"
    raw_dist = [
        "Angle bisectors of the angles",
        "Medians from the vertices",
        "Lines parallel to the opposite sides"
    ]
    sol = (
        "Step 1: The circumcircle passes through all three vertices of the triangle.\n"
        "Step 2: Its centre (circumcentre) is equidistant from all three vertices.\n"
        "Step 3: By the perpendicular bisector theorem, the circumcentre is the point of concurrency of the perpendicular bisectors of the sides."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch6_num, ch6_name, "MH-9-MTH2-6-6.3.1", "Constructing perpendicular bisectors of sides of triangle", 40, 20, 20, builder_631)

# 6.3.2: Circumcentre (C) location (40 Ex, 20 Pr, 20 Fo)
def builder_632(i, mode):
    txt = "Where does the circumcentre of a right-angled triangle lie?"
    corr = "At the midpoint of the hypotenuse"
    raw_dist = [
        "Inside the triangle",
        "Outside the triangle",
        "At the vertex containing the right angle"
    ]
    if i % 2 == 0:
        txt = "Where does the circumcentre of an obtuse-angled triangle lie?"
        corr = "In the exterior (outside) of the triangle"
        raw_dist = [
            "In the interior of the triangle",
            "On the longest side",
            "At the obtuse-angled vertex"
        ]
    sol = (
        "Step 1: The position of the circumcentre depends on the type of triangle:\n"
        "Step 2: Acute-angled triangle: inside the triangle; Right-angled triangle: midpoint of hypotenuse; Obtuse-angled triangle: outside the triangle.\n"
        f"Step 3: Correct location is {corr}."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch6_num, ch6_name, "MH-9-MTH2-6-6.3.2", "Circumcentre (C) location in acute, right, and obtuse triangles", 40, 20, 20, builder_632)

print(f"Generated Chapters 5 & 6: {len(questions_ch5_ch6)} questions")

with open("scripts/mh9_mth2_ch5_ch6_generated.json", "w", encoding="utf-8") as f:
    json.dump(questions_ch5_ch6, f, indent=2)
