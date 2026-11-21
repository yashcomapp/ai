# scripts/generate_mh9_mth2_ch1_ch2.py
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
        "createdAt": "2026-11-21T13:38:00.000Z",
        "updatedAt": "2026-11-21T13:38:00.000Z"
    }

questions_ch1_ch2 = []

def generate_subtopic_pack(ch_num, ch_name, t_code, t_name, n_exam, n_pr, n_fo, concept_builder):
    for i in range(1, n_exam + 1):
        txt, corr, raw_dist, sol = concept_builder(i, "exam")
        opts = make_unique_opts(corr, raw_dist)
        shift = i % 4
        opts = opts[shift:] + opts[:shift]
        code = f"{t_code}-OSC-{100 + i:03d}"
        questions_ch1_ch2.append(make_q(code, txt, opts, sol, ch_num, ch_name, t_code, t_name, "exam", "medium" if i % 2 == 0 else "hard"))

    for i in range(1, n_pr + 1):
        txt, corr, raw_dist, sol = concept_builder(i, "practice")
        opts = make_unique_opts(corr, raw_dist)
        shift = i % 4
        opts = opts[shift:] + opts[:shift]
        code = f"{t_code}-OSC-{200 + i:03d}"
        questions_ch1_ch2.append(make_q(code, txt, opts, sol, ch_num, ch_name, t_code, t_name, "practice", "medium"))

    for i in range(1, n_fo + 1):
        txt, corr, raw_dist, sol = concept_builder(i, "foundation")
        opts = make_unique_opts(corr, raw_dist)
        shift = i % 4
        opts = opts[shift:] + opts[:shift]
        code = f"{t_code}-OSC-{150 + i:03d}"
        questions_ch1_ch2.append(make_q(code, txt, opts, sol, ch_num, ch_name, t_code, t_name, "foundation", "easy"))

# ==========================================
# CHAPTER 1: Basic Concepts in Geometry
# ==========================================
ch1_num = 1
ch1_name = "Basic Concepts in Geometry"

# 1.1.1: Coordinates on number line (40 Ex, 20 Pr, 20 Fo)
def builder_111(i, mode):
    coord = -8 + (i % 17) # -8 to 8
    pt = chr(65 + (i % 26))
    txt = f"On a number line, point \\({pt}\\) denotes the number \\({coord}\\). What is the coordinate of point \\({pt}\\)?"
    corr = f"\\({coord}\\)"
    raw_dist = [
        f"\\({-coord}\\)" if coord != 0 else "\\(1\\)",
        f"\\({coord + 2}\\)",
        f"\\({coord - 3}\\)"
    ]
    sol = (
        f"Step 1: The real number associated with a point on a number line is called the coordinate of that point.\n"
        f"Step 2: Here, point \\({pt}\\) corresponds to the number \\({coord}\\).\n"
        f"Step 3: Hence, the coordinate of point \\({pt}\\) is \\({coord}\\)."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch1_num, ch1_name, "MH-9-MTH2-1-1.1.1", "Coordinates on number line", 40, 20, 20, builder_111)

# 1.1.2: Distance formula: Greater - Smaller (40 Ex, 20 Pr, 20 Fo)
def builder_112(i, mode):
    c1 = (i % 7) + 2 # greater: 2 to 8
    c2 = -((i % 6) + 1) # smaller: -1 to -6
    dist = c1 - c2
    txt = f"The coordinates of points \\(A\\) and \\(B\\) on a number line are \\({c1}\\) and \\({c2}\\) respectively. Find the distance \\(d(A, B)\\)."
    corr = f"\\({dist}\\)"
    raw_dist = [
        f"\\({c1 + c2}\\)",
        f"\\({-dist}\\)",
        f"\\({dist + 2}\\)"
    ]
    sol = (
        f"Step 1: On a number line, distance between two points is given by \\(d(A, B) = \\text{{Greater coordinate}} - \\text{{Smaller coordinate}}\\).\n"
        f"Step 2: Compare coordinates: \\({c1} > {c2}\\).\n"
        f"Step 3: \\(d(A, B) = {c1} - ({c2}) = {c1} + {abs(c2)} = {dist}\\)."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch1_num, ch1_name, "MH-9-MTH2-1-1.1.2", "Distance formula: d(A, B) = Greater coordinate - Smaller coordinate", 40, 20, 20, builder_112)

# 1.2.1: Condition: d(A, B) + d(B, C) = d(A, C) (40 Ex, 20 Pr, 20 Fo)
def builder_121(i, mode):
    d_ab = (i % 5) + 3
    d_bc = (i % 4) + 4
    d_ac = d_ab + d_bc
    txt = f"Points \\(P, Q, R\\) lie on a line such that \\(d(P, Q) = {d_ab}\\), \\(d(Q, R) = {d_bc}\\), and \\(d(P, R) = {d_ac}\\). Which point lies between the other two?"
    corr = "Point \\(Q\\) (betweenness \\(P-Q-R\\))"
    raw_dist = [
        "Point \\(P\\) (betweenness \\(Q-P-R\\))",
        "Point \\(R\\) (betweenness \\(P-R-Q\\))",
        "The points are non-collinear"
    ]
    sol = (
        f"Step 1: Check the betweenness condition: if \\(d(P, Q) + d(Q, R) = d(P, R)\\), then point \\(Q\\) lies between \\(P\\) and \\(R\\).\n"
        f"Step 2: Here, \\({d_ab} + {d_bc} = {d_ac} = d(P, R)\\).\n"
        f"Step 3: Therefore, point \\(Q\\) lies between \\(P\\) and \\(R\\), written as \\(P-Q-R\\)."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch1_num, ch1_name, "MH-9-MTH2-1-1.2.1", "Condition: d(A, B) + d(B, C) = d(A, C)", 40, 20, 20, builder_121)

# 1.2.2: Collinear vs non-collinear test (40 Ex, 20 Pr, 20 Fo)
def builder_122(i, mode):
    is_coll = (i % 2 == 1)
    a = (i % 4) + 3
    b = (i % 5) + 4
    c = a + b if is_coll else a + b + 2
    txt = f"Three points \\(X, Y, Z\\) have distances \\(d(X, Y) = {a}\\), \\(d(Y, Z) = {b}\\), and \\(d(X, Z) = {c}\\). Are the points collinear?"
    if is_coll:
        corr = f"Yes, collinear because \\({a} + {b} = {c}\\)"
        raw_dist = [
            f"No, non-collinear because \\({a} + {b} \\ne {c}\\)",
            "Cannot be decided without coordinates",
            "They form an equilateral triangle"
        ]
    else:
        corr = f"No, non-collinear because \\({a} + {b} = {a+b} \\ne {c}\\)"
        raw_dist = [
            f"Yes, collinear with \\(Y\\) between \\(X\\) and \\(Z\\)",
            "Yes, collinear with \\(X\\) between \\(Y\\) and \\(Z\\)",
            "They lie on the same ray"
        ]
    sol = (
        f"Step 1: Points are collinear if the sum of the two smaller distances equals the greatest distance.\n"
        f"Step 2: Compare sum \\({a} + {b} = {a + b}\\) with greatest distance \\({c}\\).\n"
        f"Step 3: {corr}."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch1_num, ch1_name, "MH-9-MTH2-1-1.2.2", "Collinear vs non-collinear test", 40, 20, 20, builder_122)

# 1.3.1: Segment definition and length (40 Ex, 20 Pr, 20 Fo)
def builder_131(i, mode):
    txt = "What is the union of point \\(A\\), point \\(B\\), and all points between \\(A\\) and \\(B\\) called?"
    corr = "Segment \\(AB\\) (\\(\\text{seg } AB\\))"
    raw_dist = [
        "Ray \\(AB\\)",
        "Line \\(AB\\)",
        "Plane \\(AB\\)"
    ]
    sol = (
        "Step 1: By geometric definition, the set containing endpoints \\(A\\) and \\(B\\) and all points between \\(A\\) and \\(B\\) is a line segment.\n"
        "Step 2: It is denoted by \\(\\text{seg } AB\\) or \\(\\text{seg } BA\\).\n"
        "Step 3: Hence, it is Segment \\(AB\\)."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch1_num, ch1_name, "MH-9-MTH2-1-1.3.1", "Segment definition and length", 40, 20, 20, builder_131)

# 1.3.2: Opposite rays (40 Ex, 20 Pr, 20 Fo)
def builder_132(i, mode):
    txt = "Two rays \\(\\text{ray } BA\\) and \\(\\text{ray } BC\\) are said to be opposite rays if:"
    corr = "They have a common origin \\(B\\) and their union is a straight line (\\(A-B-C\\))"
    raw_dist = [
        "They are perpendicular to each other",
        "They have different endpoints and do not intersect",
        "They point in the same direction"
    ]
    sol = (
        "Step 1: Two rays having the same origin (starting point) and forming a single straight line are opposite rays.\n"
        "Step 2: Their union \\(\\text{ray } BA \\cup \\text{ray } BC = \\text{line } AC\\).\n"
        "Step 3: Hence, they have common origin \\(B\\) and form a straight line with betweenness \\(A-B-C\\)."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch1_num, ch1_name, "MH-9-MTH2-1-1.3.2", "Opposite rays", 40, 20, 20, builder_132)

# 1.3.3: Midpoint: AM = MB = 1/2 AB (40 Ex, 20 Pr, 20 Fo)
def builder_133(i, mode):
    ab = (i % 8 + 3) * 2 # 6, 8, 10, ...
    am = ab // 2
    txt = f"Point \\(M\\) is the midpoint of segment \\(AB\\). If \\(l(AB) = {ab}\\) cm, find the length of \\(l(AM)\\)."
    corr = f"\\({am}\\) cm"
    raw_dist = [
        f"\\({ab}\\) cm",
        f"\\({am + 2}\\) cm",
        f"\\({am - 1}\\) cm"
    ]
    sol = (
        f"Step 1: By definition of midpoint, \\(M\\) divides \\(\\text{{seg }} AB\\) into two equal parts: \\(l(AM) = l(MB) = \\frac{{1}}{{2}} l(AB)\\).\n"
        f"Step 2: \\(l(AM) = \\frac{{1}}{{2}} \\times {ab}\\).\n"
        f"Step 3: \\(l(AM) = {am}\\) cm."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch1_num, ch1_name, "MH-9-MTH2-1-1.3.3", "Midpoint: AM = MB = 1/2 AB", 40, 20, 20, builder_133)

# 1.4.1: Antecedent vs Consequent (40 Ex, 20 Pr, 20 Fo)
def builder_141(i, mode):
    txt = "In the conditional statement 'If a quadrilateral is a rhombus, then its diagonals are perpendicular bisectors of each other', identify the antecedent (hypothesis)."
    corr = "A quadrilateral is a rhombus"
    raw_dist = [
        "Its diagonals are perpendicular bisectors of each other",
        "The quadrilateral is a square",
        "The diagonals are congruent"
    ]
    sol = (
        "Step 1: A conditional statement is written in 'If... then...' form.\n"
        "Step 2: The part following 'If' is the antecedent (hypothesis), and the part following 'then' is the consequent (conclusion).\n"
        "Step 3: Antecedent is 'A quadrilateral is a rhombus'."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch1_num, ch1_name, "MH-9-MTH2-1-1.4.1", "Antecedent (If part) vs Consequent (Then part)", 40, 20, 20, builder_141)

# 1.4.2: Converse formulation (40 Ex, 20 Pr, 20 Fo)
def builder_142(i, mode):
    txt = "What is the converse of the statement: 'If two angles are vertically opposite angles, then they are congruent'?"
    corr = "If two angles are congruent, then they are vertically opposite angles"
    raw_dist = [
        "If two angles are not congruent, then they are not vertically opposite",
        "If two angles are complementary, then they are congruent",
        "Two angles are vertically opposite if and only if they are supplementary"
    ]
    sol = (
        "Step 1: The converse of a conditional statement 'If P, then Q' is obtained by interchanging the antecedent and consequent: 'If Q, then P'.\n"
        "Step 2: Here P is 'two angles are vertically opposite' and Q is 'they are congruent'.\n"
        "Step 3: Converse: 'If two angles are congruent, then they are vertically opposite angles'."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch1_num, ch1_name, "MH-9-MTH2-1-1.4.2", "Converse formulation", 40, 20, 20, builder_142)

# 1.4.3: Direct and indirect proof methods (40 Ex, 20 Pr, 20 Fo)
def builder_143(i, mode):
    txt = "In an indirect proof, how does the argument begin?"
    corr = "By assuming that the conclusion (consequent) is false"
    raw_dist = [
        "By assuming that the hypothesis (antecedent) is false",
        "By drawing a circle of arbitrary radius",
        "By proving the converse directly"
    ]
    sol = (
        "Step 1: Indirect proof (reductio ad absurdum) starts by assuming the negation of what is to be proved.\n"
        "Step 2: Logical deduction from this false assumption leads to a contradiction with known postulates or given data.\n"
        "Step 3: Hence, the proof begins by assuming the conclusion is false."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch1_num, ch1_name, "MH-9-MTH2-1-1.4.3", "Direct and indirect proof methods", 40, 20, 20, builder_143)

# ==========================================
# CHAPTER 2: Parallel Lines
# ==========================================
ch2_num = 2
ch2_name = "Parallel Lines"

# 2.1.1: Interior angles on same side sum = 180° (40 Ex, 20 Pr, 20 Fo)
def builder_211_ch2(i, mode):
    ang1 = 50 + (i % 8) * 10 # 50, 60, ... 120
    ang2 = 180 - ang1
    txt = f"Two parallel lines are intersected by a transversal. If one interior angle on one side of the transversal is \\({ang1}^\\circ\\), what is the measure of the other interior angle on the same side?"
    corr = f"\\({ang2}^\\circ\\)"
    raw_dist = [
        f"\\({ang1}^\\circ\\)",
        f"\\({ang2 + 10}^\\circ\\)",
        f"\\({ang2 - 10}^\\circ\\)"
    ]
    sol = (
        f"Step 1: The Interior Angles Theorem states that interior angles on the same side of a transversal are supplementary (sum = \\(180^\\circ\\)).\n"
        f"Step 2: \\(\\text{{Angle}}_1 + \\text{{Angle}}_2 = 180^\\circ \\implies {ang1}^\\circ + \\text{{Angle}}_2 = 180^\\circ\\).\n"
        f"Step 3: \\(\\text{{Angle}}_2 = 180^\\circ - {ang1}^\\circ = {ang2}^\\circ\\)."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch2_num, ch2_name, "MH-9-MTH2-2-2.1.1", "Sum of interior angles on same side of transversal is 180° theorem", 40, 20, 20, builder_211_ch2)

# 2.1.2: Indirect proof method for parallel lines (40 Ex, 20 Pr, 20 Fo)
def builder_212_ch2(i, mode):
    txt = "To prove by indirect method that two coplanar lines \\(l\\) and \\(m\\) intersected by a transversal are parallel, what contradiction is reached?"
    corr = "A triangle would be formed whose angle sum exceeds 180°, contradicting Euclid's postulate"
    raw_dist = [
        "The lines would become perpendicular",
        "The transversal would cease to exist",
        "The angles would become zero"
    ]
    sol = (
        "Step 1: In the indirect proof of the interior angles theorem, we assume lines \\(l\\) and \\(m\\) are not parallel, so they intersect at a point \\(P\\).\n"
        "Step 2: Then triangle \\(\\triangle ABP\\) is formed with angle sum \\(180^\\circ + \\angle P > 180^\\circ\\).\n"
        "Step 3: This contradicts the triangle angle sum theorem (sum = 180°), proving the lines must be parallel."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch2_num, ch2_name, "MH-9-MTH2-2-2.1.2", "Indirect proof method", 40, 20, 20, builder_212_ch2)

# 2.2.1: Alternate angles theorem proof (40 Ex, 20 Pr, 20 Fo)
def builder_221_ch2(i, mode):
    ang = 45 + (i % 9) * 10
    txt = f"Line \\(l \\parallel m\\) and line \\(n\\) is a transversal. If an alternate interior angle is \\({ang}^\\circ\\), what is the measure of its corresponding alternate angle?"
    corr = f"\\({ang}^\\circ\\)"
    raw_dist = [
        f"\\({180 - ang}^\\circ\\)",
        f"\\({ang + 15}^\\circ\\)",
        f"\\({90}^\\circ\\)"
    ]
    sol = (
        f"Step 1: The Alternate Angles Theorem states that alternate interior angles formed by a transversal of two parallel lines are congruent (equal in measure).\n"
        f"Step 2: Since the given angle is \\({ang}^\\circ\\), its alternate interior angle must have the exact same measure.\n"
        f"Step 3: Measure is \\({ang}^\\circ\\)."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch2_num, ch2_name, "MH-9-MTH2-2-2.2.1", "Alternate angles theorem proof", 40, 20, 20, builder_221_ch2)

# 2.2.2: Corresponding angles theorem proof (40 Ex, 20 Pr, 20 Fo)
def builder_222_ch2(i, mode):
    ang = 40 + (i % 10) * 8
    txt = f"If two parallel lines are cut by a transversal, what is the relation between each pair of corresponding angles?"
    corr = "They are congruent (equal in measure)"
    raw_dist = [
        "They are supplementary (sum = 180°)",
        "They are complementary (sum = 90°)",
        "Their ratio is always 1:2"
    ]
    sol = (
        "Step 1: The Corresponding Angles Theorem states that corresponding angles formed by a transversal of parallel lines are equal.\n"
        "Step 2: Using the interior angles theorem and linear pair axiom, corresponding angles are proved congruent.\n"
        "Step 3: Hence, they are congruent."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch2_num, ch2_name, "MH-9-MTH2-2-2.2.2", "Corresponding angles theorem proof", 40, 20, 20, builder_222_ch2)

# 2.3.1: Proving two lines parallel using angle criteria (40 Ex, 20 Pr, 20 Fo)
def builder_231_ch2(i, mode):
    txt = "If a pair of alternate interior angles formed by a transversal of two lines is equal, what can be concluded about the two lines?"
    corr = "The two lines are parallel (by Alternate Angle Test)"
    raw_dist = [
        "The two lines are perpendicular",
        "The two lines are coincident",
        "No conclusion can be drawn"
    ]
    sol = (
        "Step 1: By the Alternate Angles Test for parallel lines, if alternate angles formed by a transversal are equal, then the lines are parallel.\n"
        "Step 2: This is the converse of the alternate angles theorem.\n"
        "Step 3: Hence, the lines are parallel."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch2_num, ch2_name, "MH-9-MTH2-2-2.3.1", "Proving two lines parallel using angle criteria", 40, 20, 20, builder_231_ch2)

# 2.4.1: Sum of angles of triangle = 180° (40 Ex, 20 Pr, 20 Fo)
def builder_241_ch2(i, mode):
    a1 = 30 + (i % 6) * 10
    a2 = 40 + (i % 5) * 10
    a3 = 180 - (a1 + a2)
    txt = f"In \\(\\triangle ABC\\), \\(\\angle A = {a1}^\\circ\\) and \\(\\angle B = {a2}^\\circ\\). What is the measure of \\(\\angle C\\)?"
    corr = f"\\({a3}^\\circ\\)"
    raw_dist = [
        f"\\({a3 + 10}^\\circ\\)",
        f"\\({a3 - 10}^\\circ\\)",
        f"\\({a1 + a2}^\\circ\\)"
    ]
    sol = (
        f"Step 1: The sum of all three angles of a triangle is \\(180^\\circ\\): \\(\\angle A + \\angle B + \\angle C = 180^\\circ\\).\n"
        f"Step 2: \\({a1}^\\circ + {a2}^\\circ + \\angle C = 180^\\circ \\implies {a1 + a2}^\\circ + \\angle C = 180^\\circ\\).\n"
        f"Step 3: \\(\\angle C = 180^\\circ - {a1 + a2}^\\circ = {a3}^\\circ\\)."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch2_num, ch2_name, "MH-9-MTH2-2-2.4.1", "Theorem: Sum of all three angles of a triangle is 180°", 40, 20, 20, builder_241_ch2)

# 2.4.2: Exterior angle theorem applications (40 Ex, 20 Pr, 20 Fo)
def builder_242_ch2(i, mode):
    r1 = 35 + (i % 5) * 10
    r2 = 45 + (i % 4) * 10
    ext = r1 + r2
    txt = f"The remote interior angles of a triangle are \\({r1}^\\circ\\) and \\({r2}^\\circ\\). Find the measure of the exterior angle."
    corr = f"\\({ext}^\\circ\\)"
    raw_dist = [
        f"\\({180 - ext}^\\circ\\)",
        f"\\({ext + 15}^\\circ\\)",
        f"\\({abs(r1 - r2)}^\\circ\\)"
    ]
    sol = (
        f"Step 1: By the Remote Interior Angles Theorem, the measure of an exterior angle of a triangle equals the sum of its two remote interior angles.\n"
        f"Step 2: \\(\\text{{Exterior angle}} = {r1}^\\circ + {r2}^\\circ\\).\n"
        f"Step 3: \\(\\text{{Exterior angle}} = {ext}^\\circ\\)."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack(ch2_num, ch2_name, "MH-9-MTH2-2-2.4.2", "Exterior angle theorem applications", 40, 20, 20, builder_242_ch2)

print(f"Generated Chapters 1 & 2: {len(questions_ch1_ch2)} questions")

with open("scripts/mh9_mth2_ch1_ch2_generated.json", "w", encoding="utf-8") as f:
    json.dump(questions_ch1_ch2, f, indent=2)
