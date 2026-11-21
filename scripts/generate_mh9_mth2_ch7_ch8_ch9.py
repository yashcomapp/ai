# scripts/generate_mh9_mth2_ch7_ch8_ch9.py
# Generates high-quality questions for MH-9-MTH2 Chapters 7, 8 & 9
# Strict 80Q standard pack (40 Exam, 20 Practice, 20 Foundation) per subtopic.
# Total subtopics: 23 (6 in Ch 7, 8 in Ch 8, 9 in Ch 9) -> 1,840 questions.

import json
import random
import math

random.seed(42)

def make_unique_opts(corr_text, raw_distractors):
    seen = set()
    seen.add(str(corr_text).strip())
    opts = [str(corr_text).strip()]
    for d in raw_distractors:
        sd = str(d).strip()
        if sd not in seen and len(opts) < 4:
            seen.add(sd)
            opts.append(sd)
    
    # Fallback padding if needed
    counter = 1
    while len(opts) < 4:
        cand = f"{corr_text} (alt {counter})"
        if cand not in seen:
            seen.add(cand)
            opts.append(cand)
        counter += 1
        
    random.shuffle(opts)
    letters = ['A', 'B', 'C', 'D']
    return [{'id': l, 'text': opt, 'isCorrect': (opt == str(corr_text).strip())} for l, opt in zip(letters, opts)]

def build_q(qcode, topic_code, ch_num, ch_name, t_name, qtext, corr_text, distractors, solution_text, vault, seq, diff="medium"):
    marks = 4 if vault in ['exam', 'practice'] else 2
    opts = make_unique_opts(corr_text, distractors)
    letters = ['A', 'B', 'C', 'D']
    corr_idx = -1
    for idx, o in enumerate(opts):
        if o["isCorrect"]:
            corr_idx = idx
            break
    corr_letter = letters[corr_idx] if corr_idx != -1 else 'A'
    
    return {
        "questionCode": qcode,
        "text": qtext,
        "options": opts,
        "correctAnswer": corr_letter,
        "solution": solution_text,
        "boardCode": "MH",
        "board": "Maharashtra Board",
        "class": "9",
        "subjectCode": "MTH2",
        "subject": "Mathematics Part - 2 (Geometry)",
        "chapterNumber": ch_num,
        "chapter": ch_name,
        "topicCode": topic_code,
        "topic": t_name,
        "type": "OSC",
        "typeCode": "OSC",
        "source": vault,
        "vault": vault,
        "marks": marks,
        "negativeMarks": 0,
        "difficulty": diff,
        "status": "active",
        "timesUsed": 0,
        "usedInClassroomTest": False,
        "requiresFigure": False,
        "createdAt": "2026-11-21T13:48:00.000Z",
        "updatedAt": "2026-11-21T13:48:00.000Z"
    }

questions = []

def generate_subtopic_pack(topic_code, ch_num, ch_name, t_name, q_generators):
    # Generates 80 questions: 40 Exam (101-140), 20 Practice (201-220), 20 Foundation (301-320)
    n_gen = len(q_generators)
    
    # 40 Exam (101 to 140)
    for i in range(40):
        seq = 101 + i
        qcode = f"{topic_code}-OSC-{seq}"
        gen_fn = q_generators[i % n_gen]
        qtext, corr_text, distractors, solution_text, diff = gen_fn(i, 'exam')
        questions.append(build_q(qcode, topic_code, ch_num, ch_name, t_name, qtext, corr_text, distractors, solution_text, 'exam', seq, diff))
        
    # 20 Practice (201 to 220)
    for i in range(20):
        seq = 201 + i
        qcode = f"{topic_code}-OSC-{seq}"
        gen_fn = q_generators[(i + 5) % n_gen]
        qtext, corr_text, distractors, solution_text, diff = gen_fn(i, 'practice')
        questions.append(build_q(qcode, topic_code, ch_num, ch_name, t_name, qtext, corr_text, distractors, solution_text, 'practice', seq, diff))
        
    # 20 Foundation (301 to 320)
    for i in range(20):
        seq = 301 + i
        qcode = f"{topic_code}-OSC-{seq}"
        gen_fn = q_generators[(i + 10) % n_gen]
        qtext, corr_text, distractors, solution_text, diff = gen_fn(i, 'foundation')
        questions.append(build_q(qcode, topic_code, ch_num, ch_name, t_name, qtext, corr_text, distractors, solution_text, 'foundation', seq, 'easy'))

# ==============================================================================
# CHAPTER 7: Coordinate Geometry (6 subtopics)
# ==============================================================================

# --- Subtopic 7.1.1: X-axis, Y-axis, Origin (0,0) ---
def gen_7_1_1(idx, source):
    types = idx % 5
    if types == 0:
        return (
            "What are the coordinates of the origin where the X-axis and Y-axis intersect?",
            "\\((0, 0)\\)",
            ["\\((1, 1)\\)", "\\((0, 1)\\)", "\\((1, 0)\\)"],
            "**Step 1: Concept**\nThe point of intersection of the coordinate axes is called the origin.\n**Step 2: Coordinate Definition**\nBoth its x-coordinate (abscissa) and y-coordinate (ordinate) are zero.\n**Step 3: Conclusion**\nCoordinates of origin are \\((0, 0)\\).",
            "easy"
        )
    elif types == 1:
        x_val = (idx * 3 % 17) + 2
        return (
            f"If a point lies on the X-axis at a distance of \\({x_val}\\) units to the right of the Y-axis, what are its coordinates?",
            f"\\(({x_val}, 0)\\)",
            [f"\\((0, {x_val})\\)", f"\\((-{x_val}, 0)\\)", f"\\(({x_val}, {x_val})\\)"],
            f"**Step 1: Formula**\nAny point lying on the X-axis has y-coordinate equal to 0.\n**Step 2: Abscissa value**\nDistance to the right means \\(x = +{x_val}\\).\n**Step 3: Conclusion**\nThe coordinates are \\(({x_val}, 0)\\).",
            "easy"
        )
    elif types == 2:
        y_val = (idx * 4 % 19) + 3
        return (
            f"If a point \\(P\\) lies on the Y-axis at a distance of \\({y_val}\\) units below the X-axis, what are the coordinates of \\(P\\)?",
            f"\\((0, -{y_val})\\)",
            [f"\\((-{y_val}, 0)\\)", f"\\((0, {y_val})\\)", f"\\(({y_val}, 0)\\)"],
            f"**Step 1: Concept**\nAny point on the Y-axis has x-coordinate equal to 0.\n**Step 2: Ordinate calculation**\nSince it lies below the X-axis, its y-coordinate is negative: \\(y = -{y_val}\\).\n**Step 3: Final Answer**\nThe coordinates are \\((0, -{y_val})\\).",
            "medium"
        )
    elif types == 3:
        x_val = -((idx * 2 % 13) + 1)
        return (
            f"What is the ordinate of the point \\(({x_val}, 0)\\)?",
            "\\(0\\)",
            [f"\\({x_val}\\)", f"\\({-x_val}\\)", "\\(1\\)"],
            f"**Step 1: Definition**\nIn an ordered pair \\((x, y)\\), \\(x\\) is the abscissa and \\(y\\) is the ordinate.\n**Step 2: Identification**\nHere, \\(x = {x_val}\\) and \\(y = 0\\).\n**Step 3: Conclusion**\nThe ordinate is \\(0\\).",
            "easy"
        )
    else:
        y_val = (idx * 5 % 15) + 2
        return (
            f"What is the abscissa of the point \\((0, {y_val})\\)?",
            "\\(0\\)",
            [f"\\({y_val}\\)", f"\\(-{y_val}\\)", "\\(1\\)"],
            f"**Step 1: Definition**\nThe abscissa of a point is its x-coordinate.\n**Step 2: Identification**\nFor point \\((0, {y_val})\\), the x-coordinate is 0.\n**Step 3: Conclusion**\nThe abscissa is \\(0\\).",
            "easy"
        )

# --- Subtopic 7.1.2: Plotting points in all four quadrants ---
def gen_7_1_2(idx, source):
    x = (idx * 3 % 11) + 2
    y = (idx * 4 % 13) + 3
    q_case = idx % 4
    if q_case == 0:
        return (
            f"In which quadrant does the point \\(A({x}, {y})\\) lie?",
            "Quadrant I",
            ["Quadrant II", "Quadrant III", "Quadrant IV"],
            f"**Step 1: Rule of signs**\nFor any point \\((x, y)\\):\nQuadrant I: \\(x > 0, y > 0\\).\n**Step 2: Test coordinates**\nHere \\(x = {x} > 0\\) and \\(y = {y} > 0\\).\n**Step 3: Conclusion**\nPoint \\(A\\) lies in Quadrant I.",
            "easy"
        )
    elif q_case == 1:
        return (
            f"In which quadrant does the point \\(B(-{x}, {y})\\) lie?",
            "Quadrant II",
            ["Quadrant I", "Quadrant III", "Quadrant IV"],
            f"**Step 1: Rule of signs**\nQuadrant II has \\(x < 0\\) and \\(y > 0\\).\n**Step 2: Test coordinates**\nHere \\(x = -{x} < 0\\) and \\(y = {y} > 0\\).\n**Step 3: Conclusion**\nPoint \\(B\\) lies in Quadrant II.",
            "easy"
        )
    elif q_case == 2:
        return (
            f"In which quadrant does the point \\(C(-{x}, -{y})\\) lie?",
            "Quadrant III",
            ["Quadrant I", "Quadrant II", "Quadrant IV"],
            f"**Step 1: Rule of signs**\nQuadrant III has \\(x < 0\\) and \\(y < 0\\).\n**Step 2: Test coordinates**\nHere \\(x = -{x} < 0\\) and \\(y = -{y} < 0\\).\n**Step 3: Conclusion**\nPoint \\(C\\) lies in Quadrant III.",
            "easy"
        )
    else:
        return (
            f"In which quadrant does the point \\(D({x}, -{y})\\) lie?",
            "Quadrant IV",
            ["Quadrant I", "Quadrant II", "Quadrant III"],
            f"**Step 1: Rule of signs**\nQuadrant IV has \\(x > 0\\) and \\(y < 0\\).\n**Step 2: Test coordinates**\nHere \\(x = {x} > 0\\) and \\(y = -{y} < 0\\).\n**Step 3: Conclusion**\nPoint \\(D\\) lies in Quadrant IV.",
            "easy"
        )

# --- Subtopic 7.2.1: Line parallel to Y-axis: x = c ---
def gen_7_2_1(idx, source):
    c = (idx * 2 % 15) - 7
    if c == 0:
        c = 5
    if idx % 2 == 0:
        return (
            f"What is the equation of the line parallel to the Y-axis and passing through the point \\(({c}, 9)\\)?",
            f"\\(x = {c}\\)",
            [f"\\(y = {c}\\)", f"\\(x = 9\\)", f"\\(y = 9\\)"],
            f"**Step 1: Concept**\nAny line parallel to the Y-axis has an equation of the form \\(x = c\\), where every point on the line has the same x-coordinate.\n**Step 2: Value of c**\nSince it passes through \\(({c}, 9)\\), \\(x = {c}\\).\n**Step 3: Conclusion**\nThe equation of the line is \\(x = {c}\\).",
            "medium"
        )
    else:
        dist = abs(c)
        side = "right" if c > 0 else "left"
        return (
            f"A line is parallel to the Y-axis at a distance of \\({dist}\\) units to the {side} of it. What is its equation?",
            f"\\(x = {c}\\)",
            [f"\\(x = {-c}\\)", f"\\(y = {c}\\)", f"\\(y = {-c}\\)"],
            f"**Step 1: Concept**\nA line parallel to the Y-axis has equation \\(x = a\\).\n**Step 2: Determine sign**\nDistance to the {side} of Y-axis implies \\(x = {c}\\).\n**Step 3: Conclusion**\nThe equation is \\(x = {c}\\).",
            "medium"
        )

# --- Subtopic 7.2.2: Line parallel to X-axis: y = c ---
def gen_7_2_2(idx, source):
    c = (idx * 3 % 17) - 8
    if c == 0:
        c = 4
    if idx % 2 == 0:
        return (
            f"What is the equation of the line parallel to the X-axis and passing through the point \\((-4, {c})\\)?",
            f"\\(y = {c}\\)",
            [f"\\(x = {c}\\)", f"\\(x = -4\\)", f"\\(y = -4\\)"],
            f"**Step 1: Concept**\nAny line parallel to the X-axis has an equation of the form \\(y = c\\).\n**Step 2: Coordinate value**\nSince the point \\((-4, {c})\\) lies on this line, \\(y = {c}\\).\n**Step 3: Conclusion**\nThe equation is \\(y = {c}\\).",
            "medium"
        )
    else:
        dist = abs(c)
        pos = "above" if c > 0 else "below"
        return (
            f"What is the equation of the line parallel to the X-axis and at a distance of \\({dist}\\) units {pos} the X-axis?",
            f"\\(y = {c}\\)",
            [f"\\(y = {-c}\\)", f"\\(x = {c}\\)", f"\\(x = {-c}\\)"],
            f"**Step 1: Concept**\nA line parallel to the X-axis has the equation \\(y = b\\).\n**Step 2: Determine constant**\nDistance \\({dist}\\) units {pos} the X-axis means \\(y = {c}\\).\n**Step 3: Final Answer**\nThe equation is \\(y = {c}\\).",
            "medium"
        )

# --- Subtopic 7.2.3: Equation of X-axis (y=0) and Y-axis (x=0) ---
def gen_7_2_3(idx, source):
    types = idx % 4
    if types == 0:
        return (
            "What is the equation of the X-axis?",
            "\\(y = 0\\)",
            ["\\(x = 0\\)", "\\(x = y\\)", "\\(x + y = 0\\)"],
            "**Step 1: Definition**\nFor every point on the X-axis, the y-coordinate (ordinate) is zero.\n**Step 2: Mathematical Form**\nTherefore, the equation of the X-axis is \\(y = 0\\).\n**Step 3: Conclusion**\nCorrect option is \\(y = 0\\).",
            "easy"
        )
    elif types == 1:
        return (
            "What is the equation of the Y-axis?",
            "\\(x = 0\\)",
            ["\\(y = 0\\)", "\\(x = 1\\)", "\\(y = 1\\)"],
            "**Step 1: Definition**\nFor every point on the Y-axis, the x-coordinate (abscissa) is zero.\n**Step 2: Form**\nHence, the equation of the Y-axis is \\(x = 0\\).\n**Step 3: Conclusion**\nCorrect option is \\(x = 0\\).",
            "easy"
        )
    elif types == 2:
        return (
            "The graph of the equation \\(y = 0\\) represents:",
            "The X-axis",
            ["The Y-axis", "A line through \\((1, 1)\\)", "A circle"],
            "**Step 1: Concept**\nEvery point with \\(y = 0\\) lies directly on the horizontal axis.\n**Step 2: Interpretation**\nThis horizontal axis is the X-axis.\n**Step 3: Conclusion**\nIt represents the X-axis.",
            "easy"
        )
    else:
        return (
            "The graph of the equation \\(x = 0\\) represents:",
            "The Y-axis",
            ["The X-axis", "The origin only", "A line parallel to the X-axis"],
            "**Step 1: Concept**\nEvery point whose x-coordinate is 0 lies directly on the vertical coordinate axis.\n**Step 2: Identification**\nThis axis is defined as the Y-axis.\n**Step 3: Conclusion**\nIt represents the Y-axis.",
            "easy"
        )

# --- Subtopic 7.3.1: Finding solutions table and plotting straight lines on graph paper ---
def gen_7_3_1(idx, source):
    m = (idx % 4) + 1
    c = (idx * 2 % 7) + 1
    x_val = (idx % 5) + 1
    y_val = m * x_val + c
    if idx % 2 == 0:
        return (
            f"If \\(x = {x_val}\\) in the linear equation \\(y = {m}x + {c}\\), what is the corresponding value of \\(y\\)?",
            f"\\({y_val}\\)",
            [f"\\({y_val + 2}\\)", f"\\({y_val - 2}\\)", f"\\({m * x_val}\\)"],
            f"**Step 1: Given equation**\n\\(y = {m}x + {c}\\).\n**Step 2: Substitution**\nSubstitute \\(x = {x_val}\\):\n\\(y = {m}({x_val}) + {c} = {m * x_val} + {c} = {y_val}\\).\n**Step 3: Conclusion**\nThe value of \\(y\\) is \\({y_val}\\).",
            "medium"
        )
    else:
        wrong_y = y_val + 3
        return (
            f"Which of the following points lies on the line given by \\(y = {m}x + {c}\\)?",
            f"\\(({x_val}, {y_val})\\)",
            [f"\\(({x_val}, {wrong_y})\\)", f"\\((0, {c + 2})\\)", f"\\((1, {m + c + 1})\\)"],
            f"**Step 1: Condition**\nA point \\((x, y)\\) lies on the line if it satisfies the equation \\(y = {m}x + {c}\\).\n**Step 2: Verification**\nFor \\(({x_val}, {y_val})\\): LHS \\(= {y_val}\\), RHS \\(= {m}({x_val}) + {c} = {y_val}\\). LHS = RHS.\n**Step 3: Conclusion**\nPoint \\(({x_val}, {y_val})\\) lies on the line.",
            "medium"
        )

# ==============================================================================
# CHAPTER 8: Trigonometry (8 subtopics)
# ==============================================================================

triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (9, 40, 41)]

# --- Subtopic 8.1.1: In right angled triangle: sin θ = Opposite / Hypotenuse ---
def gen_8_1_1(idx, source):
    opp, adj, hyp = triples[idx % len(triples)]
    mult = (idx % 3) + 1
    opp *= mult
    adj *= mult
    hyp *= mult
    return (
        f"In a right-angled triangle \\(\\triangle ABC\\) where \\(\\angle B = 90^\\circ\\), the side opposite to angle \\(\\theta\\) is {opp} cm and the hypotenuse is {hyp} cm. What is \\(\\sin \\theta\\)?",
        f"\\(\\frac{{{opp}}}{{{hyp}}}\\)",
        [f"\\(\\frac{{{adj}}}{{{hyp}}}\\)", f"\\(\\frac{{{opp}}}{{{adj}}}\\)", f"\\(\\frac{{{hyp}}}{{{opp}}}\\)"],
        f"**Step 1: Formula**\n\\(\\sin \\theta = \\frac{{\\text{{Opposite side}}}}{{\\text{{Hypotenuse}}}}\\).\n**Step 2: Substitution**\nOpposite side = {opp}, Hypotenuse = {hyp}.\n\\(\\sin \\theta = \\frac{{{opp}}}{{{hyp}}}\\).\n**Step 3: Conclusion**\n\\(\\sin \\theta = \\frac{{{opp}}}{{{hyp}}}\\).",
        "medium"
    )

# --- Subtopic 8.1.2: cos θ = Adjacent / Hypotenuse ---
def gen_8_1_2(idx, source):
    opp, adj, hyp = triples[idx % len(triples)]
    mult = (idx % 3) + 1
    opp *= mult
    adj *= mult
    hyp *= mult
    return (
        f"In right-angled triangle \\(\\triangle PQR\\) with \\(\\angle Q = 90^\\circ\\), side adjacent to angle \\(\\theta\\) is {adj} cm and hypotenuse is {hyp} cm. What is \\(\\cos \\theta\\)?",
        f"\\(\\frac{{{adj}}}{{{hyp}}}\\)",
        [f"\\(\\frac{{{opp}}}{{{hyp}}}\\)", f"\\(\\frac{{{adj}}}{{{opp}}}\\)", f"\\(\\frac{{{hyp}}}{{{adj}}}\\)"],
        f"**Step 1: Definition**\n\\(\\cos \\theta = \\frac{{\\text{{Adjacent side}}}}{{\\text{{Hypotenuse}}}}\\).\n**Step 2: Substitution**\nAdjacent side = {adj}, Hypotenuse = {hyp}.\n\\(\\cos \\theta = \\frac{{{adj}}}{{{hyp}}}\\).\n**Step 3: Conclusion**\n\\(\\cos \\theta = \\frac{{{adj}}}{{{hyp}}}\\).",
        "medium"
    )

# --- Subtopic 8.1.3: tan θ = Opposite / Adjacent = sin θ / cos θ ---
def gen_8_1_3(idx, source):
    opp, adj, hyp = triples[idx % len(triples)]
    return (
        f"In a right-angled triangle, if opposite side = {opp} cm and adjacent side = {adj} cm, what is \\(\\tan \\theta\\)?",
        f"\\(\\frac{{{opp}}}{{{adj}}}\\)",
        [f"\\(\\frac{{{adj}}}{{{opp}}}\\)", f"\\(\\frac{{{opp}}}{{{hyp}}}\\)", f"\\(\\frac{{{adj}}}{{{hyp}}}\\)"],
        f"**Step 1: Formula**\n\\(\\tan \\theta = \\frac{{\\text{{Opposite side}}}}{{\\text{{Adjacent side}}}}\\).\n**Step 2: Substitution**\nOpposite = {opp}, Adjacent = {adj}.\n\\(\\tan \\theta = \\frac{{{opp}}}{{{adj}}}\\).\n**Step 3: Conclusion**\n\\(\\tan \\theta = \\frac{{{opp}}}{{{adj}}}\\).",
        "medium"
    )

# --- Subtopic 8.2.1: tan θ * tan (90-θ) = 1 ---
def gen_8_2_1(idx, source):
    theta = 15 + (idx * 5 % 65)
    comp = 90 - theta
    if idx % 2 == 0:
        return (
            f"What is the value of \\(\\tan {theta}^\\circ \\times \\tan {comp}^\\circ\\)?",
            "\\(1\\)",
            ["\\(0\\)", "\\(2\\)", "\\(\\frac{1}{2}\\)"],
            f"**Step 1: Complementary Angle Relation**\nSince \\(\\tan(90^\\circ - \\theta) = \\frac{{1}}{{\\tan \\theta}}\\), we have \\(\\tan \\theta \\times \\tan(90^\\circ - \\theta) = 1\\).\n**Step 2: Calculation**\nHere \\({theta}^\\circ + {comp}^\\circ = 90^\\circ\\), so \\(\\tan {comp}^\\circ = \\frac{{1}}{{\\tan {theta}^\\circ}}\\).\n\\(\\tan {theta}^\\circ \\times \\frac{{1}}{{\\tan {theta}^\\circ}} = 1\\).\n**Step 3: Conclusion**\nThe value is \\(1\\).",
            "medium"
        )
    else:
        return (
            f"If \\(\\tan {theta}^\\circ = k\\), then what is \\(\\tan {comp}^\\circ\\) in terms of \\(k\\)?",
            "\\(\\frac{1}{k}\\)",
            ["\\(k\\)", "\\(1 - k\\)", "\\(-k\\)"],
            f"**Step 1: Relation**\n\\(\\tan(90^\\circ - \\theta) = \\cot \\theta = \\frac{{1}}{{\\tan \\theta}}\\).\n**Step 2: Substitution**\n\\(\\tan {comp}^\\circ = \\tan(90^\\circ - {theta}^\\circ) = \\frac{{1}}{{k}}\\).\n**Step 3: Conclusion**\nCorrect value is \\(\\frac{{1}}{{k}}\\).",
            "medium"
        )

# --- Subtopic 8.2.2: sin θ = cos (90-θ) and cos θ = sin (90-θ) ---
def gen_8_2_2(idx, source):
    angle = 10 + (idx * 7 % 70)
    comp = 90 - angle
    if idx % 2 == 0:
        return (
            f"Express \\(\\sin {angle}^\\circ\\) in terms of cosine of its complementary angle.",
            f"\\(\\cos {comp}^\\circ\\)",
            [f"\\(\\cos {angle}^\\circ\\)", f"\\(\\sin {comp}^\\circ\\)", f"\\(\\tan {comp}^\\circ\\)"],
            f"**Step 1: Complementary formula**\n\\(\\sin \\theta = \\cos(90^\\circ - \\theta)\\).\n**Step 2: Substitution**\nFor \\(\\theta = {angle}^\\circ\\):\n\\(\\sin {angle}^\\circ = \\cos(90^\\circ - {angle}^\\circ) = \\cos {comp}^\\circ\\).\n**Step 3: Conclusion**\n\\(\\sin {angle}^\\circ = \\cos {comp}^\\circ\\).",
            "medium"
        )
    else:
        return (
            f"What is the value of \\(\\frac{{\\cos {comp}^\\circ}}{{\\sin {angle}^\\circ}}\\)?",
            "\\(1\\)",
            ["\\(0\\)", "\\(\\tan {angle}^\\circ\\)", "\\(\\cot {angle}^\\circ\\)"],
            f"**Step 1: Complementary relationship**\n\\(\\cos {comp}^\\circ = \\cos(90^\\circ - {angle}^\\circ) = \\sin {angle}^\\circ\\).\n**Step 2: Division**\n\\(\\frac{{\\cos {comp}^\\circ}}{{\\sin {angle}^\\circ}} = \\frac{{\\sin {angle}^\\circ}}{{\\sin {angle}^\\circ}} = 1\\).\n**Step 3: Conclusion**\nThe value is \\(1\\).",
            "medium"
        )

# --- Subtopic 8.2.3: Fundamental identity: sin²θ + cos²θ = 1 ---
def gen_8_2_3(idx, source):
    opp, adj, hyp = triples[idx % len(triples)]
    if idx % 2 == 0:
        return (
            f"If \\(\\sin \\theta = \\frac{{{opp}}}{{{hyp}}}\\), find \\(\\cos \\theta\\) for acute angle \\(\\theta\\).",
            f"\\(\\frac{{{adj}}}{{{hyp}}}\\)",
            [f"\\(\\frac{{{opp}}}{{{hyp}}}\\)", f"\\(\\frac{{{adj}}}{{{opp}}}\\)", f"\\(1\\)"],
            f"**Step 1: Identity**\n\\(\\sin^2\\theta + \\cos^2\\theta = 1 \\implies \\cos \\theta = \\sqrt{{1 - \\sin^2\\theta}}\\).\n**Step 2: Calculation**\n\\(\\cos \\theta = \\sqrt{{1 - \\left(\\frac{{{opp}}}{{{hyp}}}\\right)^2}} = \\sqrt{{\\frac{{{hyp**2 - opp**2}}}{{{hyp**2}}}}} = \\frac{{{adj}}}{{{hyp}}}\\).\n**Step 3: Conclusion**\n\\(\\cos \\theta = \\frac{{{adj}}}{{{hyp}}}\\).",
            "hard"
        )
    else:
        angle = 20 + (idx * 3 % 50)
        return (
            f"What is the value of \\(\\sin^2 {angle}^\\circ + \\cos^2 {angle}^\\circ\\)?",
            "\\(1\\)",
            ["\\(0\\)", "\\(2\\)", "\\(\\frac{1}{2}\\)"],
            f"**Step 1: Trigonometric Identity**\nFor any angle \\(\\theta\\), \\(\\sin^2\\theta + \\cos^2\\theta = 1\\).\n**Step 2: Application**\nHere \\(\\theta = {angle}^\\circ\\), so \\(\\sin^2 {angle}^\\circ + \\cos^2 {angle}^\\circ = 1\\).\n**Step 3: Conclusion**\nThe value is \\(1\\).",
            "easy"
        )

# --- Subtopic 8.3.1: Derivation of values using geometric triangles (30°, 45°, 60°) ---
def gen_8_3_1(idx, source):
    table = [
        ("sin 30^\\circ", "\\frac{1}{2}", ["\\frac{\\sqrt{3}}{2}", "\\frac{1}{\\sqrt{2}}", "1"]),
        ("cos 60^\\circ", "\\frac{1}{2}", ["\\frac{\\sqrt{3}}{2}", "\\frac{1}{\\sqrt{2}}", "0"]),
        ("sin 60^\\circ", "\\frac{\\sqrt{3}}{2}", ["\\frac{1}{2}", "\\frac{1}{\\sqrt{2}}", "1"]),
        ("cos 30^\\circ", "\\frac{\\sqrt{3}}{2}", ["\\frac{1}{2}", "\\frac{1}{\\sqrt{2}}", "\\sqrt{3}"]),
        ("tan 45^\\circ", "1", ["\\frac{1}{\\sqrt{3}}", "\\sqrt{3}", "0"]),
        ("sin 45^\\circ", "\\frac{1}{\\sqrt{2}}", ["\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}", "1"]),
        ("cos 45^\\circ", "\\frac{1}{\\sqrt{2}}", ["\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}", "0"]),
        ("tan 30^\\circ", "\\frac{1}{\\sqrt{3}}", ["\\sqrt{3}", "1", "\\frac{1}{2}"]),
        ("tan 60^\\circ", "\\sqrt{3}", ["\\frac{1}{\\sqrt{3}}", "1", "2"])
    ]
    item = table[idx % len(table)]
    ratio, corr, dist = item
    return (
        f"What is the exact value of \\(\\{ratio}\\)?",
        f"\\({corr}\\)",
        [f"\\({d}\\)" for d in dist],
        f"**Step 1: Standard Table Reference**\nBy standard equilateral triangle (30°-60°-90°) or isosceles right triangle (45°-45°-90°).\n**Step 2: Evaluation**\nThe value of \\(\\{ratio}\\) is \\({corr}\\).\n**Step 3: Conclusion**\nCorrect value is \\({corr}\\).",
        "easy"
    )

# --- Subtopic 8.3.2: Evaluating trigonometric algebraic expressions ---
def gen_8_3_2(idx, source):
    types = idx % 3
    if types == 0:
        return (
            "Evaluate: \\(2\\sin 30^\\circ + \\cos 0^\\circ\\)",
            "\\(2\\)",
            ["\\(1\\)", "\\(3\\)", "\\(\\frac{3}{2}\\)"],
            "**Step 1: Substitute values**\n\\(\\sin 30^\\circ = \\frac{1}{2}\\), \\(\\cos 0^\\circ = 1\\).\n**Step 2: Compute**\n\\(2\\left(\\frac{1}{2}\\right) + 1 = 1 + 1 = 2\\).\n**Step 3: Conclusion**\nThe result is \\(2\\).",
            "medium"
        )
    elif types == 1:
        return (
            "Evaluate: \\(\\tan^2 45^\\circ + \\sin^2 90^\\circ\\)",
            "\\(2\\)",
            ["\\(1\\)", "\\(0\\)", "\\(\\sqrt{2}\\)"],
            "**Step 1: Values**\n\\(\\tan 45^\\circ = 1\\), \\(\\sin 90^\\circ = 1\\).\n**Step 2: Compute**\n\\(1^2 + 1^2 = 1 + 1 = 2\\).\n**Step 3: Conclusion**\nValue is \\(2\\).",
            "medium"
        )
    else:
        return (
            "Evaluate: \\(4\\cos^2 60^\\circ + 3\\tan^2 30^\\circ\\)",
            "\\(2\\)",
            ["\\(1\\)", "\\(3\\)", "\\(\\frac{7}{4}\\)"],
            "**Step 1: Values**\n\\(\\cos 60^\\circ = \\frac{1}{2}\\), \\(\\tan 30^\\circ = \\frac{1}{\\sqrt{3}}\\).\n**Step 2: Substitution & Calculation**\n\\(4\\left(\\frac{1}{2}\\right)^2 + 3\\left(\\frac{1}{\\sqrt{3}}\\right)^2 = 4\\left(\\frac{1}{4}\\right) + 3\\left(\\frac{1}{3}\\right) = 1 + 1 = 2\\).\n**Step 3: Conclusion**\nThe result is \\(2\\).",
            "hard"
        )

# ==============================================================================
# CHAPTER 9: Surface Area and Volume (9 subtopics)
# ==============================================================================

cone_triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (7, 24, 25), (8, 15, 17)]

# --- Subtopic 9.1.1: Slant height l = √(r² + h²) ---
def gen_9_1_1(idx, source):
    r, h, l = cone_triples[idx % len(cone_triples)]
    return (
        f"Find the slant height \\(l\\) of a right circular cone whose base radius is {r} cm and height is {h} cm.",
        f"{l} cm",
        [f"{l + 2} cm", f"{r + h} cm", f"{l - 1} cm"],
        f"**Step 1: Formula**\nSlant height \\(l = \\sqrt{{r^2 + h^2}}\\).\n**Step 2: Calculation**\n\\(l = \\sqrt{{{r}^2 + {h}^2}} = \\sqrt{{{r**2} + {h**2}}} = \\sqrt{{{l**2}}} = {l}\\text{{ cm}}\\).\n**Step 3: Conclusion**\nThe slant height is {l} cm.",
        "easy"
    )

# --- Subtopic 9.1.2: Curved Surface Area = πrl ---
def gen_9_1_2(idx, source):
    r, h, l = cone_triples[idx % len(cone_triples)]
    csa_pi = r * l
    return (
        f"A right circular cone has radius \\(r = {r}\\text{{ cm}}\\) and slant height \\(l = {l}\\text{{ cm}}\\). What is its curved surface area in terms of \\(\\pi\\)?",
        f"\\({csa_pi}\\pi\\text{{ cm}}^2\\)",
        [f"\\({csa_pi + 10}\\pi\\text{{ cm}}^2\\)", f"\\({r * h}\\pi\\text{{ cm}}^2\\)", f"\\({2 * csa_pi}\\pi\\text{{ cm}}^2\\)"],
        f"**Step 1: Formula**\nCurved Surface Area of cone \\(= \\pi r l\\).\n**Step 2: Substitution**\n\\(\\text{{CSA}} = \\pi \\times {r} \\times {l} = {csa_pi}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\nCurved surface area is \\({csa_pi}\\pi\\text{{ cm}}^2\\).",
        "medium"
    )

# --- Subtopic 9.1.3: Total Surface Area = πr(r + l) ---
def gen_9_1_3(idx, source):
    r, h, l = cone_triples[idx % len(cone_triples)]
    tsa_pi = r * (r + l)
    return (
        f"Calculate the total surface area of a cone having radius {r} cm and slant height {l} cm (in terms of \\(\\pi\\)).",
        f"\\({tsa_pi}\\pi\\text{{ cm}}^2\\)",
        [f"\\({tsa_pi + 12}\\pi\\text{{ cm}}^2\\)", f"\\({r * l}\\pi\\text{{ cm}}^2\\)", f"\\({2 * tsa_pi}\\pi\\text{{ cm}}^2\\)"],
        f"**Step 1: Formula**\nTotal Surface Area of cone \\(= \\pi r (r + l)\\).\n**Step 2: Calculation**\n\\(\\text{{TSA}} = \\pi \\times {r} \\times ({r} + {l}) = \\pi \\times {r} \\times {r + l} = {tsa_pi}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\nTotal surface area is \\({tsa_pi}\\pi\\text{{ cm}}^2\\).",
        "medium"
    )

# --- Subtopic 9.1.4: Volume = 1/3 * πr²h ---
def gen_9_1_4(idx, source):
    r, h, l = cone_triples[idx % len(cone_triples)]
    vol_pi = (r * r * h) // 3
    if (r * r * h) % 3 != 0:
        vol_str = f"\\frac{{{r * r * h}}}{{3}}\\pi\\text{{ cm}}^3"
        dist = [f"\\frac{{{r * r * h + 3}}}{{3}}\\pi\\text{{ cm}}^3", f"{r * h}\\pi\\text{{ cm}}^3", f"{r * r * h}\\pi\\text{{ cm}}^3"]
    else:
        vol_str = f"{vol_pi}\\pi\\text{{ cm}}^3"
        dist = [f"{vol_pi + 15}\\pi\\text{{ cm}}^3", f"{vol_pi * 3}\\pi\\text{{ cm}}^3", f"{vol_pi - 10}\\pi\\text{{ cm}}^3"]
    return (
        f"Find the volume of a cone with radius {r} cm and vertical height {h} cm.",
        f"\\({vol_str}\\)",
        [f"\\({d}\\)" for d in dist],
        f"**Step 1: Formula**\nVolume of cone \\(= \\frac{{1}}{{3}}\\pi r^2 h\\).\n**Step 2: Substitution**\n\\(V = \\frac{{1}}{{3}}\\pi \\times {r}^2 \\times {h} = \\frac{{1}}{{3}}\\pi \\times {r * r} \\times {h} = {vol_str}\\).\n**Step 3: Conclusion**\nVolume is \\({vol_str}\\).",
        "hard"
    )

# --- Subtopic 9.2.1: Surface Area of Sphere = 4πr² ---
def gen_9_2_1(idx, source):
    r = (idx % 7) + 2
    sa_pi = 4 * r * r
    return (
        f"Find the surface area of a solid sphere of radius {r} cm in terms of \\(\\pi\\).",
        f"\\({sa_pi}\\pi\\text{{ cm}}^2\\)",
        [f"\\({sa_pi // 2}\\pi\\text{{ cm}}^2\\)", f"\\({sa_pi + 16}\\pi\\text{{ cm}}^2\\)", f"\\({2 * r * r}\\pi\\text{{ cm}}^2\\)"],
        f"**Step 1: Formula**\nSurface area of sphere \\(= 4\\pi r^2\\).\n**Step 2: Calculation**\n\\(\\text{{SA}} = 4\\pi \\times {r}^2 = 4\\pi \\times {r * r} = {sa_pi}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\nSurface area is \\({sa_pi}\\pi\\text{{ cm}}^2\\).",
        "easy"
    )

# --- Subtopic 9.2.2: Volume of Sphere = 4/3 * πr³ ---
def gen_9_2_2(idx, source):
    r = (idx % 6) + 3
    num = 4 * (r ** 3)
    if num % 3 == 0:
        vol_str = f"{num // 3}\\pi\\text{{ cm}}^3"
        dist = [f"{(num // 3) + 20}\\pi\\text{{ cm}}^3", f"{(num // 3) // 2}\\pi\\text{{ cm}}^3", f"{num}\\pi\\text{{ cm}}^3"]
    else:
        vol_str = f"\\frac{{{num}}}{{3}}\\pi\\text{{ cm}}^3"
        dist = [f"\\frac{{{num + 6}}}{{3}}\\pi\\text{{ cm}}^3", f"{4 * r * r}\\pi\\text{{ cm}}^3", f"\\frac{{{num // 2}}}{{3}}\\pi\\text{{ cm}}^3"]
    return (
        f"What is the volume of a sphere of radius {r} cm?",
        f"\\({vol_str}\\)",
        [f"\\({d}\\)" for d in dist],
        f"**Step 1: Formula**\nVolume of sphere \\(= \\frac{{4}}{{3}}\\pi r^3\\).\n**Step 2: Calculation**\n\\(V = \\frac{{4}}{{3}}\\pi \\times {r}^3 = \\frac{{4}}{{3}}\\pi \\times {r**3} = {vol_str}\\).\n**Step 3: Conclusion**\nThe volume is \\({vol_str}\\).",
        "medium"
    )

# --- Subtopic 9.2.3: Curved Surface Area of Hemisphere = 2πr² ---
def gen_9_2_3(idx, source):
    r = (idx % 8) + 2
    csa_pi = 2 * r * r
    return (
        f"Find the curved surface area (CSA) of a hemisphere of radius {r} cm in terms of \\(\\pi\\).",
        f"\\({csa_pi}\\pi\\text{{ cm}}^2\\)",
        [f"\\({3 * r * r}\\pi\\text{{ cm}}^2\\)", f"\\({4 * r * r}\\pi\\text{{ cm}}^2\\)", f"\\({r * r}\\pi\\text{{ cm}}^2\\)"],
        f"**Step 1: Formula**\nCurved surface area of hemisphere \\(= 2\\pi r^2\\).\n**Step 2: Calculation**\n\\(\\text{{CSA}} = 2\\pi \\times {r}^2 = 2\\pi \\times {r * r} = {csa_pi}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\nCurved surface area is \\({csa_pi}\\pi\\text{{ cm}}^2\\).",
        "easy"
    )

# --- Subtopic 9.2.4: Total Surface Area of Hemisphere = 3πr² ---
def gen_9_2_4(idx, source):
    r = (idx % 7) + 2
    tsa_pi = 3 * r * r
    return (
        f"Find the total surface area (TSA) of a solid hemisphere of radius {r} cm in terms of \\(\\pi\\).",
        f"\\({tsa_pi}\\pi\\text{{ cm}}^2\\)",
        [f"\\({2 * r * r}\\pi\\text{{ cm}}^2\\)", f"\\({4 * r * r}\\pi\\text{{ cm}}^2\\)", f"\\({(3 * r * r) + 10}\\pi\\text{{ cm}}^2\\)"],
        f"**Step 1: Formula**\nTotal surface area of solid hemisphere \\(= 3\\pi r^2\\) (curved surface \\(2\\pi r^2\\) + circular flat base \\(\\pi r^2\\)).\n**Step 2: Calculation**\n\\(\\text{{TSA}} = 3\\pi \\times {r}^2 = 3\\pi \\times {r * r} = {tsa_pi}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\nTotal surface area is \\({tsa_pi}\\pi\\text{{ cm}}^2\\).",
        "medium"
    )

# --- Subtopic 9.2.5: Volume of Hemisphere = 2/3 * πr³ ---
def gen_9_2_5(idx, source):
    r = (idx % 6) + 3
    num = 2 * (r ** 3)
    if num % 3 == 0:
        vol_str = f"{num // 3}\\pi\\text{{ cm}}^3"
        dist = [f"{(num // 3) + 12}\\pi\\text{{ cm}}^3", f"{(num // 3) * 2}\\pi\\text{{ cm}}^3", f"{num}\\pi\\text{{ cm}}^3"]
    else:
        vol_str = f"\\frac{{{num}}}{{3}}\\pi\\text{{ cm}}^3"
        dist = [f"\\frac{{{num + 4}}}{{3}}\\pi\\text{{ cm}}^3", f"{2 * r * r}\\pi\\text{{ cm}}^3", f"\\frac{{{num * 2}}}{{3}}\\pi\\text{{ cm}}^3"]
    return (
        f"Find the volume of a solid hemisphere having radius {r} cm.",
        f"\\({vol_str}\\)",
        [f"\\({d}\\)" for d in dist],
        f"**Step 1: Formula**\nVolume of hemisphere \\(= \\frac{{2}}{{3}}\\pi r^3\\).\n**Step 2: Calculation**\n\\(V = \\frac{{2}}{{3}}\\pi \\times {r}^3 = \\frac{{2}}{{3}}\\pi \\times {r**3} = {vol_str}\\).\n**Step 3: Conclusion**\nThe volume is \\({vol_str}\\).",
        "medium"
    )

# ==============================================================================
# MAIN EXECUTION: Populate all 23 subtopics
# ==============================================================================

print("Generating Questions for Chapter 7 (Coordinate Geometry)...")
ch7_name = "Coordinate Geometry"
generate_subtopic_pack("MH-9-MTH2-7-7.1.1", 7, ch7_name, "X-axis, Y-axis, Origin (0,0)", [gen_7_1_1])
generate_subtopic_pack("MH-9-MTH2-7-7.1.2", 7, ch7_name, "Plotting points in all four quadrants", [gen_7_1_2])
generate_subtopic_pack("MH-9-MTH2-7-7.2.1", 7, ch7_name, "Line parallel to Y-axis: x = c", [gen_7_2_1])
generate_subtopic_pack("MH-9-MTH2-7-7.2.2", 7, ch7_name, "Line parallel to X-axis: y = c", [gen_7_2_2])
generate_subtopic_pack("MH-9-MTH2-7-7.2.3", 7, ch7_name, "Equation of X-axis (y=0) and Y-axis (x=0)", [gen_7_2_3])
generate_subtopic_pack("MH-9-MTH2-7-7.3.1", 7, ch7_name, "Finding solutions table and plotting straight lines on graph paper", [gen_7_3_1])

print("Generating Questions for Chapter 8 (Trigonometry)...")
ch8_name = "Trigonometry"
generate_subtopic_pack("MH-9-MTH2-8-8.1.1", 8, ch8_name, "In right angled triangle: sin θ = Opposite / Hypotenuse", [gen_8_1_1])
generate_subtopic_pack("MH-9-MTH2-8-8.1.2", 8, ch8_name, "cos θ = Adjacent / Hypotenuse", [gen_8_1_2])
generate_subtopic_pack("MH-9-MTH2-8-8.1.3", 8, ch8_name, "tan θ = Opposite / Adjacent = sin θ / cos θ", [gen_8_1_3])
generate_subtopic_pack("MH-9-MTH2-8-8.2.1", 8, ch8_name, "tan θ * tan (90-θ) = 1", [gen_8_2_1])
generate_subtopic_pack("MH-9-MTH2-8-8.2.2", 8, ch8_name, "sin θ = cos (90-θ) and cos θ = sin (90-θ)", [gen_8_2_2])
generate_subtopic_pack("MH-9-MTH2-8-8.2.3", 8, ch8_name, "Fundamental identity: sin²θ + cos²θ = 1", [gen_8_2_3])
generate_subtopic_pack("MH-9-MTH2-8-8.3.1", 8, ch8_name, "Derivation of values using geometric triangles", [gen_8_3_1])
generate_subtopic_pack("MH-9-MTH2-8-8.3.2", 8, ch8_name, "Evaluating trigonometric algebraic expressions", [gen_8_3_2])

print("Generating Questions for Chapter 9 (Surface Area and Volume)...")
ch9_name = "Surface Area and Volume"
generate_subtopic_pack("MH-9-MTH2-9-9.1.1", 9, ch9_name, "Slant height l = √(r² + h²)", [gen_9_1_1])
generate_subtopic_pack("MH-9-MTH2-9-9.1.2", 9, ch9_name, "Curved Surface Area = πrl", [gen_9_1_2])
generate_subtopic_pack("MH-9-MTH2-9-9.1.3", 9, ch9_name, "Total Surface Area = πr(r + l)", [gen_9_1_3])
generate_subtopic_pack("MH-9-MTH2-9-9.1.4", 9, ch9_name, "Volume = 1/3 * πr²h", [gen_9_1_4])
generate_subtopic_pack("MH-9-MTH2-9-9.2.1", 9, ch9_name, "Surface Area of Sphere = 4πr²", [gen_9_2_1])
generate_subtopic_pack("MH-9-MTH2-9-9.2.2", 9, ch9_name, "Volume of Sphere = 4/3 * πr³", [gen_9_2_2])
generate_subtopic_pack("MH-9-MTH2-9-9.2.3", 9, ch9_name, "Curved Surface Area of Hemisphere = 2πr²", [gen_9_2_3])
generate_subtopic_pack("MH-9-MTH2-9-9.2.4", 9, ch9_name, "Total Surface Area of Hemisphere = 3πr²", [gen_9_2_4])
generate_subtopic_pack("MH-9-MTH2-9-9.2.5", 9, ch9_name, "Volume of Hemisphere = 2/3 * πr³", [gen_9_2_5])

print(f"Total questions generated across Ch 7, 8, 9: {len(questions)}")

output_path = "scripts/mh9_mth2_ch7_ch8_ch9_generated.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
