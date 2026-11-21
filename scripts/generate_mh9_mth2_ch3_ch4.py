# scripts/generate_mh9_mth2_ch3_ch4.py
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
        "createdAt": "2026-11-21T13:40:00.000Z",
        "updatedAt": "2026-11-21T13:40:00.000Z"
    }

questions_ch3_ch4 = []

def generate_subtopic_pack(ch_num, ch_name, t_code, t_name, n_exam, n_pr, n_fo, concept_builder):
    for i in range(1, n_exam + 1):
        txt, corr, raw_dist, sol = concept_builder(i, "exam")
        opts = make_unique_opts(corr, raw_dist)
        shift = i % 4
        opts = opts[shift:] + opts[:shift]
        code = f"{t_code}-OSC-{100 + i:03d}"
        questions_ch3_ch4.append(make_q(code, txt, opts, sol, ch_num, ch_name, t_code, t_name, "exam", "medium" if i % 2 == 0 else "hard"))

    for i in range(1, n_pr + 1):
        txt, corr, raw_dist, sol = concept_builder(i, "practice")
        opts = make_unique_opts(corr, raw_dist)
        shift = i % 4
        opts = opts[shift:] + opts[:shift]
        code = f"{t_code}-OSC-{200 + i:03d}"
        questions_ch3_ch4.append(make_q(code, txt, opts, sol, ch_num, ch_name, t_code, t_name, "practice", "medium"))

    for i in range(1, n_fo + 1):
        txt, corr, raw_dist, sol = concept_builder(i, "foundation")
        opts = make_unique_opts(corr, raw_dist)
        shift = i % 4
        opts = opts[shift:] + opts[:shift]
        code = f"{t_code}-OSC-{150 + i:03d}"
        questions_ch3_ch4.append(make_q(code, txt, opts, sol, ch_num, ch_name, t_code, t_name, "foundation", "easy"))

# ==========================================
# CHAPTER 3: Triangles
# ==========================================
ch3_num = 3
ch3_name = "Triangles"

# 3.1.1: Remote interior angles theorem (40 Ex, 20 Pr, 20 Fo)
def builder_311(i, mode):
    a = 30 + (i % 6) * 10
    b = 40 + (i % 5) * 10
    ext = a + b
    txt = f"An exterior angle of \\(\\triangle ABC\\) has measure \\({ext}^\\circ\\). If one of its remote interior angles is \\({a}^\\circ\\), what is the measure of the other remote interior angle?"
    corr = f"\\({b}^\\circ\\)"
    raw_dist = [
        f"\\({b + 10}^\\circ\\)",
        f"\\({b - 10}^\\circ\\)",
        f"\\({180 - ext}^\\circ\\)"
    ]
    sol = (
        f"Step 1: By the Remote Interior Angles Theorem, \\(\\text{{Exterior Angle}} = \\text{{Sum of Remote Interior Angles}}\\).\n"
        f"Step 2: \\({ext}^\\circ = {a}^\\circ + \\angle B \\implies \\angle B = {ext}^\\circ - {a}^\\circ\\).\n"
        f"Step 3: \\(\\angle B = {b}^\\circ\\)."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch3_num, ch3_name, "MH-9-MTH2-3-3.1.1", "Measure of exterior angle = sum of its remote interior angles", 40, 20, 20, builder_311)

# 3.2.1: Rigorous geometric proofs (tests for congruence) (40 Ex, 20 Pr, 20 Fo)
def builder_321(i, mode):
    tests = ["SAS test", "ASA test", "SSS test", "Hypotenuse-Side test", "AAS test"]
    test = tests[i % len(tests)]
    txt = f"Which criterion proves two right-angled triangles congruent if the hypotenuse and one side of one triangle are congruent to the hypotenuse and corresponding side of the other?"
    corr = "Hypotenuse-Side test"
    raw_dist = [
        "SSS test",
        "AAA test",
        "SAS test"
    ]
    if i % 3 == 0:
        txt = "Why is 'AAA' (Angle-Angle-Angle) not a valid test for congruence of triangles?"
        corr = "Triangles with equal angles can have different side lengths (they are similar, not necessarily congruent)"
        raw_dist = [
            "Because angles cannot be measured accurately",
            "Because the angle sum is not 180°",
            "Because three angles cannot specify a triangle"
        ]
    sol = (
        "Step 1: Congruence requires identity in both shape and size.\n"
        "Step 2: Equal corresponding angles guarantee same shape, but side scale factor may vary.\n"
        f"Step 3: Correct answer: {corr}."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch3_num, ch3_name, "MH-9-MTH2-3-3.2.1", "Rigorous two-column geometric proofs", 40, 20, 20, builder_321)

# 3.2.2: c.a.c.t. & c.s.c.t. (40 Ex, 20 Pr, 20 Fo)
def builder_322(i, mode):
    txt = "What does the abbreviation 'c.s.c.t.' stand for in geometric triangle proofs?"
    corr = "Corresponding sides of congruent triangles"
    raw_dist = [
        "Corresponding sides of similar triangles",
        "Central segments of congruent triangles",
        "Common sides of cyclic triangles"
    ]
    if i % 2 == 0:
        txt = "What does the abbreviation 'c.a.c.t.' stand for in geometric triangle proofs?"
        corr = "Corresponding angles of congruent triangles"
        raw_dist = [
            "Corresponding angles of cyclic triangles",
            "Central angles of congruent triangles",
            "Consecutive angles of congruent trapeziums"
        ]
    sol = (
        "Step 1: When two triangles are proved congruent, their corresponding parts are congruent.\n"
        "Step 2: 'c.s.c.t.' = corresponding sides of congruent triangles; 'c.a.c.t.' = corresponding angles of congruent triangles.\n"
        f"Step 3: Correct expansion is {corr}."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch3_num, ch3_name, "MH-9-MTH2-3-3.2.2", "Corresponding angles/sides of congruent triangles (c.a.c.t. & c.s.c.t.)", 40, 20, 20, builder_322)

# 3.3.1: Isosceles triangle theorem (40 Ex, 20 Pr, 20 Fo)
def builder_331(i, mode):
    vert = 40 + (i % 7) * 10
    base_ang = (180 - vert) // 2
    txt = f"In an isosceles triangle \\(\\triangle PQR\\), \\(PQ = PR\\). If the vertex angle \\(\\angle P = {vert}^\\circ\\), find the measure of base angle \\(\\angle Q\\)."
    corr = f"\\({base_ang}^\\circ\\)"
    raw_dist = [
        f"\\({vert}^\\circ\\)",
        f"\\({base_ang + 10}^\\circ\\)",
        f"\\({180 - vert}^\\circ\\)"
    ]
    sol = (
        f"Step 1: By the Isosceles Triangle Theorem, angles opposite to equal sides are equal: \\(\\angle Q = \\angle R\\).\n"
        f"Step 2: Sum of angles = \\(180^\\circ \\implies {vert}^\\circ + 2\\angle Q = 180^\\circ\\).\n"
        f"Step 3: \\(2\\angle Q = 180^\\circ - {vert}^\\circ = {180 - vert}^\\circ \\implies \\angle Q = {base_ang}^\\circ\\)."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch3_num, ch3_name, "MH-9-MTH2-3-3.3.1", "Isosceles triangle theorem and converse", 40, 20, 20, builder_331)

# 3.3.2: 30°-60°-90° theorem (40 Ex, 20 Pr, 20 Fo)
def builder_332(i, mode):
    hyp = (i % 8 + 3) * 2 # 6, 8, 10, ...
    opp30 = hyp // 2
    txt = f"In a \\(30^\\circ-60^\\circ-90^\\circ\\) right-angled triangle, the hypotenuse is \\({hyp}\\) cm. What is the length of the side opposite to the \\(30^\\circ\\) angle?"
    corr = f"\\({opp30}\\) cm"
    raw_dist = [
        f"\\({hyp}\\) cm",
        f"\\({opp30}\\sqrt{{3}}\\) cm",
        f"\\({opp30 + 2}\\) cm"
    ]
    sol = (
        f"Step 1: By the \\(30^\\circ-60^\\circ-90^\\circ\\) Theorem, the side opposite to \\(30^\\circ\\) is half of the hypotenuse: \\(\\text{{Side}} = \\frac{{1}}{{2}} \\times \\text{{Hypotenuse}}\\).\n"
        f"Step 2: \\(\\text{{Side}} = \\frac{{1}}{{2}} \\times {hyp}\\).\n"
        f"Step 3: Length = \\({opp30}\\) cm."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch3_num, ch3_name, "MH-9-MTH2-3-3.3.2", "30°-60°-90° theorem", 40, 20, 20, builder_332)

# 3.3.3: 45°-45°-90° theorem (40 Ex, 20 Pr, 20 Fo)
def builder_333(i, mode):
    s = (i % 6) + 4
    txt = f"In a \\(45^\\circ-45^\\circ-90^\\circ\\) triangle, each perpendicular side has length \\({s}\\) cm. What is the length of the hypotenuse?"
    corr = f"\\({s}\\sqrt{{2}}\\) cm"
    raw_dist = [
        f"\\({2*s}\\) cm",
        f"\\({s}\\sqrt{{3}}\\) cm",
        f"\\({s // 2}\\sqrt{{2}}\\) cm"
    ]
    sol = (
        f"Step 1: By the \\(45^\\circ-45^\\circ-90^\\circ\\) Theorem, \\(\\text{{Side}} = \\frac{{1}}{{\\sqrt{{2}}}} \\times \\text{{Hypotenuse}}\\).\n"
        f"Step 2: Therefore, \\(\\text{{Hypotenuse}} = \\sqrt{{2}} \\times \\text{{Side}}\\).\n"
        f"Step 3: \\(\\text{{Hypotenuse}} = {s}\\sqrt{{2}}\\) cm."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch3_num, ch3_name, "MH-9-MTH2-3-3.3.3", "45°-45°-90° theorem: Perpendicular sides are 1/√2 hyp", 40, 20, 20, builder_333)

# 3.4.1: Length of median to hypotenuse = 1/2 hypotenuse (40 Ex, 20 Pr, 20 Fo)
def builder_341(i, mode):
    hyp = (i % 7 + 4) * 2 # 8, 10, ...
    med = hyp // 2
    txt = f"In right-angled \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), hypotenuse \\(AC = {hyp}\\) cm. What is the length of the median drawn from vertex \\(B\\) to the hypotenuse?"
    corr = f"\\({med}\\) cm"
    raw_dist = [
        f"\\({hyp}\\) cm",
        f"\\({med + 2}\\) cm",
        f"\\({med}\\sqrt{{2}}\\) cm"
    ]
    sol = (
        f"Step 1: Theorem: In a right-angled triangle, the length of the median to the hypotenuse is half the length of the hypotenuse.\n"
        f"Step 2: \\(\\text{{Median}} = \\frac{{1}}{{2}} \\times AC = \\frac{{1}}{{2}} \\times {hyp}\\).\n"
        f"Step 3: Length of median is \\({med}\\) cm."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch3_num, ch3_name, "MH-9-MTH2-3-3.4.1", "Length of median to hypotenuse = 1/2 hypotenuse", 40, 20, 20, builder_341)

# 3.4.2: Perpendicular bisector theorem (40 Ex, 20 Pr, 20 Fo)
def builder_342(i, mode):
    d = (i % 6) + 5
    txt = f"Point \\(P\\) lies on the perpendicular bisector of segment \\(AB\\). If \\(PA = {d}\\) cm, what is the length of segment \\(PB\\)?"
    corr = f"\\({d}\\) cm"
    raw_dist = [
        f"\\({2*d}\\) cm",
        f"\\({d // 2}\\) cm",
        f"\\({d + 2}\\) cm"
    ]
    sol = (
        f"Step 1: By the Perpendicular Bisector Theorem, every point on the perpendicular bisector of a segment is equidistant from its endpoints.\n"
        f"Step 2: Since point \\(P\\) lies on the perpendicular bisector of \\(AB\\), \\(PA = PB\\).\n"
        f"Step 3: Given \\(PA = {d}\\) cm, therefore \\(PB = {d}\\) cm."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch3_num, ch3_name, "MH-9-MTH2-3-3.4.2", "Perpendicular bisector theorem", 40, 20, 20, builder_342)

# 3.5.1: Angle bisector theorem (40 Ex, 20 Pr, 20 Fo)
def builder_351(i, mode):
    dist = (i % 5) + 3
    txt = f"Point \\(M\\) lies on the ray bisecting \\(\\angle ABC\\). If the perpendicular distance from \\(M\\) to arm \\(BA\\) is \\({dist}\\) cm, what is the perpendicular distance from \\(M\\) to arm \\(BC\\)?"
    corr = f"\\({dist}\\) cm"
    raw_dist = [
        f"\\({2*dist}\\) cm",
        f"\\({dist + 1}\\) cm",
        f"\\({dist // 2}\\) cm"
    ]
    sol = (
        f"Step 1: By the Angle Bisector Theorem, every point on the bisector of an angle is equidistant from the arms of the angle.\n"
        f"Step 2: Since \\(M\\) is on the angle bisector, perpendicular distance to arm \\(BA\\) equals perpendicular distance to arm \\(BC\\).\n"
        f"Step 3: The distance is \\({dist}\\) cm."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch3_num, ch3_name, "MH-9-MTH2-3-3.5.1", "Every point on angle bisector is equidistant from arms of angle", 40, 20, 20, builder_351)

# 3.5.2: Similar triangles: ratio of sides equal (40 Ex, 20 Pr, 20 Fo)
def builder_352(i, mode):
    k = (i % 3) + 2 # scale factor 2, 3, 4
    ab = 4
    pq = ab * k
    bc = 6
    qr = bc * k
    txt = f"If \\(\\triangle ABC \\sim \\triangle PQR\\) and \\(\\frac{{AB}}{{PQ}} = \\frac{{1}}{{{k}}}\\), what is \\(QR\\) if \\(BC = {bc}\\) cm?"
    corr = f"\\({qr}\\) cm"
    raw_dist = [
        f"\\({bc}\\) cm",
        f"\\({qr + 2}\\) cm",
        f"\\({bc // k}\\) cm"
    ]
    sol = (
        f"Step 1: Corresponding sides of similar triangles are in proportion: \\(\\frac{{AB}}{{PQ}} = \\frac{{BC}}{{QR}}\\).\n"
        f"Step 2: \\(\\frac{{1}}{{{k}}} = \\frac{{{bc}}}{{QR}} \\implies QR = {bc} \\times {k}\\).\n"
        f"Step 3: \\(QR = {qr}\\) cm."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch3_num, ch3_name, "MH-9-MTH2-3-3.5.2", "Similar triangles: ratio of corresponding sides equal", 40, 20, 20, builder_352)

# ==========================================
# CHAPTER 4: Constructions of Triangles
# ==========================================
ch4_num = 4
ch4_name = "Constructions of Triangles"

# 4.1.1: Given base, base angle & sum of sides (40 Ex, 20 Pr, 20 Fo)
def builder_411(i, mode):
    txt = "In constructing \\(\\triangle ABC\\) given base \\(BC\\), \\(\\angle B\\), and sum of sides \\(AB + AC\\), what geometric line is drawn to locate vertex \\(A\\) on ray \\(BD\\)?"
    corr = "Perpendicular bisector of segment \\(CD\\)"
    raw_dist = [
        "Angle bisector of \\(\\angle B\\)",
        "Median to segment \\(BC\\)",
        "Altitude from \\(D\\) to \\(BC\\)"
    ]
    sol = (
        "Step 1: Point \\(D\\) is marked on ray \\(BD\\) such that \\(BD = AB + AC\\).\n"
        "Step 2: Since \\(AD = AC\\), point \\(A\\) is equidistant from \\(C\\) and \\(D\\).\n"
        "Step 3: By the perpendicular bisector theorem, \\(A\\) lies on the perpendicular bisector of \\(\\text{seg } CD\\)."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch4_num, ch4_name, "MH-9-MTH2-4-4.1.1", "Compass and ruler step-by-step construction", 40, 20, 20, builder_411)

# 4.2.1: Difference of sides: AB > AC (40 Ex, 20 Pr, 20 Fo)
def builder_421(i, mode):
    txt = "When constructing \\(\\triangle ABC\\) given base \\(BC\\), \\(\\angle B\\), and difference \\(AB - AC\\) (where \\(AB > AC\\)), where is point \\(D\\) marked such that \\(BD = AB - AC\\)?"
    corr = "On ray \\(BD\\) in the direction of \\(A\\)"
    raw_dist = [
        "On the opposite ray of ray \\(BD\\)",
        "On the segment \\(BC\\)",
        "At the circumcentre"
    ]
    sol = (
        "Step 1: When \\(AB > AC\\), \\(B-D-A\\) holds, so \\(D\\) lies on the ray \\(BA\\).\n"
        "Step 2: \\(BD = AB - AD = AB - AC\\).\n"
        "Step 3: Point \\(D\\) is marked on ray \\(BD\\) in the direction of \\(A\\)."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch4_num, ch4_name, "MH-9-MTH2-4-4.2.1", "Case 1: AB > AC", 40, 20, 20, builder_421)

# 4.2.2: Difference of sides: AC > AB (40 Ex, 20 Pr, 20 Fo)
def builder_422(i, mode):
    txt = "When constructing \\(\\triangle ABC\\) given base \\(BC\\), \\(\\angle B\\), and \\(AC - AB\\) (where \\(AC > AB\\)), where is point \\(D\\) marked such that \\(BD = AC - AB\\)?"
    corr = "On the opposite ray of ray \\(BA\\)"
    raw_dist = [
        "On the ray \\(BA\\) itself",
        "On ray \\(BC\\)",
        "At the midpoint of \\(AC\\)"
    ]
    sol = (
        "Step 1: When \\(AC > AB\\), betweenness is \\(D-B-A\\).\n"
        "Step 2: Thus, point \\(D\\) must be extended on the opposite ray of ray \\(BA\\).\n"
        "Step 3: \\(BD = AC - AB\\) is measured along the opposite ray."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch4_num, ch4_name, "MH-9-MTH2-4-4.2.2", "Case 2: AC > AB", 40, 20, 20, builder_422)

# 4.3.1: Given perimeter and two base angles (40 Ex, 20 Pr, 20 Fo)
def builder_431(i, mode):
    b1 = 60
    b2 = 80
    txt = "In constructing \\(\\triangle ABC\\) given its perimeter and base angles \\(\\angle B = 60^\\circ\\) and \\(\\angle C = 80^\\circ\\), what base angles are constructed on the perimeter line segment \\(XY\\)?"
    corr = "\\(30^\\circ\\) and \\(40^\\circ\\) (half of the given base angles)"
    raw_dist = [
        "\\(60^\\circ\\) and \\(80^\\circ\\)",
        "\\(120^\\circ\\) and \\(160^\\circ\\)",
        "\\(45^\\circ\\) and \\(45^\\circ\\)"
    ]
    sol = (
        "Step 1: In perimeter construction, temporary baseline \\(XY = AB + BC + CA\\).\n"
        "Step 2: The angles at endpoints \\(X\\) and \\(Y\\) are drawn equal to half of \\(\\angle B\\) and half of \\(\\angle C\\).\n"
        "Step 3: Hence, the angles constructed are \\(\\frac{60^\\circ}{2} = 30^\\circ\\) and \\(\\frac{80^\\circ}{2} = 40^\\circ\\)."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch4_num, ch4_name, "MH-9-MTH2-4-4.3.1", "Dividing baseline and drawing perpendicular bisectors", 40, 20, 20, builder_431)

print(f"Generated Chapters 3 & 4: {len(questions_ch3_ch4)} questions")

with open("scripts/mh9_mth2_ch3_ch4_generated.json", "w", encoding="utf-8") as f:
    json.dump(questions_ch3_ch4, f, indent=2)
