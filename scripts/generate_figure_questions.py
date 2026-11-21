# scripts/generate_figure_questions.py
# Generates 60 high-quality figure-based geometry questions with embedded inline SVGs
# for MH-9-MTH2 across Chapters 1, 2, 3, 5, 6, and 7.
# Complies 100% with Rule 2T, Rule 2K, and SVG validation rules.

import json
import random

random.seed(99)

def make_unique_opts(corr_text, raw_distractors):
    seen = set()
    seen.add(str(corr_text).strip())
    opts = [str(corr_text).strip()]
    for d in raw_distractors:
        sd = str(d).strip()
        if sd not in seen and len(opts) < 4:
            seen.add(sd)
            opts.append(sd)
    
    counter = 1
    while len(opts) < 4:
        cand = f"{corr_text} (var {counter})"
        if cand not in seen:
            seen.add(cand)
            opts.append(cand)
        counter += 1
        
    random.shuffle(opts)
    letters = ['A', 'B', 'C', 'D']
    return [{'id': l, 'text': opt, 'isCorrect': (opt == str(corr_text).strip())} for l, opt in zip(letters, opts)]

def build_fig_q(qcode, topic_code, ch_num, ch_name, t_name, svg_markup, stem_text, corr_text, distractors, solution_text, vault="exam", marks=4, diff="medium"):
    opts = make_unique_opts(corr_text, distractors)
    letters = ['A', 'B', 'C', 'D']
    corr_idx = -1
    for idx, o in enumerate(opts):
        if o["isCorrect"]:
            corr_idx = idx
            break
    corr_letter = letters[corr_idx] if corr_idx != -1 else 'A'
    
    full_text = f'{svg_markup}\n{stem_text}'
    
    return {
        "questionCode": qcode,
        "text": full_text,
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
        "requiresFigure": True,
        "timesUsed": 0,
        "usedInClassroomTest": False,
        "createdAt": "2026-11-21T14:20:00.000Z",
        "updatedAt": "2026-11-21T14:20:00.000Z"
    }

figure_questions = []

# ==============================================================================
# CHAPTER 1: BASIC CONCEPTS IN GEOMETRY (10 questions)
# ==============================================================================
ch1_name = "Basic Concepts in Geometry"

# --- 1.1.1: Number line coordinates and distance d(A, B) (5 questions) ---
# SVG Number Line with points A(-3), B(-1), C(0), D(2), E(5)
def get_number_line_svg(p_coords, active_pts=None, title="Coordinate Number Line"):
    # p_coords: dict of { 'A': -3, 'B': -1, 'C': 0, 'D': 2, 'E': 5 }
    # Map -6 to +6 on 360 width: x = 180 + val * 26
    svg = [
        '<div style="display: flex; justify-content: center; margin: 12px 0;">',
        '<svg width="100%" height="auto" viewBox="0 0 360 140" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">',
        f'  <text x="180" y="22" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>',
        '  <!-- Main line with arrows -->',
        '  <line x1="20" y1="70" x2="340" y2="70" stroke="#64748b" stroke-width="2"/>',
        '  <polygon points="15,70 25,65 25,75" fill="#64748b"/>',
        '  <polygon points="345,70 335,65 335,75" fill="#64748b"/>'
    ]
    # Draw ticks from -6 to 6
    for val in range(-6, 7):
        cx = 180 + val * 24
        svg.append(f'  <line x1="{cx}" y1="65" x2="{cx}" y2="75" stroke="#475569" stroke-width="1.2"/>')
        svg.append(f'  <text x="{cx}" y="92" fill="#64748b" font-size="9" font-family="sans-serif" text-anchor="middle">{val}</text>')
        
    for p_name, val in p_coords.items():
        cx = 180 + val * 24
        is_highlight = active_pts and (p_name in active_pts)
        c_fill = "#38bdf8" if is_highlight else "#f8fafc"
        svg.append(f'  <circle cx="{cx}" cy="70" r="4.5" fill="{c_fill}"/>')
        # Ensure point label Y is spaced away from tick label Y (y=50 vs y=92)
        svg.append(f'  <text x="{cx}" y="50" fill="{c_fill}" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{p_name}</text>')
        
    svg.append('</svg>\n</div>')
    return '\n'.join(svg)

nl1 = {'A': -3, 'B': -1, 'C': 0, 'D': 2, 'E': 5}
# Q1: d(A, D) = 2 - (-3) = 5
q1_svg = get_number_line_svg(nl1, ['A', 'D'], "Number Line with Points A, B, C, D, E")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-1-1.1.1-OSC-101", "MH-9-MTH2-1-1.1.1", 1, ch1_name, "Coordinates of Points & Distance on Number Line",
    q1_svg,
    "Refer to the number line shown above with points \\(A, B, C, D, E\\). What is the distance \\(d(A, D)\\)?",
    "\\(5\\)", ["\\(1\\)", "\\(-5\\)", "\\(6\\)"],
    "**Step 1: Given Coordinates**\nFrom the number line diagram, the coordinate of \\(A\\) is \\(-3\\) and the coordinate of \\(D\\) is \\(2\\).\n**Step 2: Formula & Calculation**\nDistance is greater coordinate minus smaller coordinate:\n\\(d(A, D) = 2 - (-3) = 2 + 3 = 5\\).\n**Step 3: Conclusion**\n\\(d(A, D) = 5\\).",
    "exam", 4, "easy"
))

# Q2: d(B, E) = 5 - (-1) = 6
q2_svg = get_number_line_svg(nl1, ['B', 'E'], "Number Line with Points A, B, C, D, E")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-1-1.1.1-OSC-102", "MH-9-MTH2-1-1.1.1", 1, ch1_name, "Coordinates of Points & Distance on Number Line",
    q2_svg,
    "In the given number line above, points \\(B\\) and \\(E\\) have coordinates \\(-1\\) and \\(5\\) respectively. Find \\(d(B, E)\\).",
    "\\(6\\)", ["\\(4\\)", "\\(5\\)", "\\(7\\)"],
    "**Step 1: Coordinates**\nCoordinate of \\(B = -1\\) and coordinate of \\(E = 5\\).\n**Step 2: Calculation**\n\\(d(B, E) = 5 - (-1) = 5 + 1 = 6\\).\n**Step 3: Conclusion**\n\\(d(B, E) = 6\\).",
    "exam", 4, "easy"
))

# Q3: d(A, E) = 5 - (-3) = 8
q3_svg = get_number_line_svg(nl1, ['A', 'E'], "Number Line with Points A, B, C, D, E")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-1-1.1.1-OSC-103", "MH-9-MTH2-1-1.1.1", 1, ch1_name, "Coordinates of Points & Distance on Number Line",
    q3_svg,
    "Based on the given number line above, calculate the total distance \\(d(A, E)\\).",
    "\\(8\\)", ["\\(2\\)", "\\(7\\)", "\\(9\\)"],
    "**Step 1: Identify Coordinates**\nCoordinate of \\(A = -3\\), coordinate of \\(E = 5\\).\n**Step 2: Distance Computation**\n\\(d(A, E) = 5 - (-3) = 8\\).\n**Step 3: Conclusion**\nThe distance \\(d(A, E)\\) is \\(8\\).",
    "exam", 4, "easy"
))

# Q4: Midpoint coordinate of A(-3) and D(2) = (-3 + 2)/2 = -0.5 or d(A, B) = 2
q4_svg = get_number_line_svg(nl1, ['A', 'B'], "Number Line with Points A, B, C, D, E")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-1-1.1.1-OSC-104", "MH-9-MTH2-1-1.1.1", 1, ch1_name, "Coordinates of Points & Distance on Number Line",
    q4_svg,
    "Refer to the number line above. What is the distance \\(d(A, B)\\) between point \\(A(-3)\\) and point \\(B(-1)\\)?",
    "\\(2\\)", ["\\(-2\\)", "\\(4\\)", "\\(3\\)"],
    "**Step 1: Coordinates**\nCoordinate of \\(A = -3\\), coordinate of \\(B = -1\\).\nSince \\(-1 > -3\\), \\(-1\\) is the greater coordinate.\n**Step 2: Distance**\n\\(d(A, B) = -1 - (-3) = -1 + 3 = 2\\).\n**Step 3: Conclusion**\n\\(d(A, B) = 2\\).",
    "exam", 4, "easy"
))

# Q5: d(C, D) = 2 - 0 = 2
q5_svg = get_number_line_svg(nl1, ['C', 'D'], "Number Line with Points A, B, C, D, E")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-1-1.1.1-OSC-105", "MH-9-MTH2-1-1.1.1", 1, ch1_name, "Coordinates of Points & Distance on Number Line",
    q5_svg,
    "In the diagram above, point \\(C\\) represents the origin \\(0\\) and point \\(D\\) is at coordinate \\(2\\). Find \\(d(C, D)\\).",
    "\\(2\\)", ["\\(0\\)", "\\(1\\)", "\\(3\\)"],
    "**Step 1: Coordinates**\nCoordinate of \\(C = 0\\), coordinate of \\(D = 2\\).\n**Step 2: Distance**\n\\(d(C, D) = 2 - 0 = 2\\).\n**Step 3: Conclusion**\n\\(d(C, D) = 2\\).",
    "exam", 4, "easy"
))

# --- 1.2.1: Betweenness of Points (5 questions) ---
def get_betweenness_svg(p1, p2, p3, l12, l23, title="Collinear Points & Betweenness"):
    svg = f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 130" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="22" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>
  <line x1="40" y1="65" x2="320" y2="65" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="50" cy="65" r="5" fill="#f8fafc"/>
  <circle cx="170" cy="65" r="5" fill="#f59e0b"/>
  <circle cx="310" cy="65" r="5" fill="#f8fafc"/>
  <text x="50" y="48" fill="#f8fafc" font-size="14" font-weight="bold" font-family="sans-serif" text-anchor="middle">{p1}</text>
  <text x="170" y="48" fill="#f59e0b" font-size="14" font-weight="bold" font-family="sans-serif" text-anchor="middle">{p2}</text>
  <text x="310" y="48" fill="#f8fafc" font-size="14" font-weight="bold" font-family="sans-serif" text-anchor="middle">{p3}</text>
  <!-- Length labels below line -->
  <text x="110" y="95" fill="#38bdf8" font-size="12" font-weight="600" font-family="sans-serif" text-anchor="middle">{l12}</text>
  <text x="240" y="95" fill="#38bdf8" font-size="12" font-weight="600" font-family="sans-serif" text-anchor="middle">{l23}</text>
</svg>
</div>"""
    return svg

# Q6: P-Q-R with PQ = 6, QR = 9 -> PR = 15
q6_svg = get_betweenness_svg('P', 'Q', 'R', "6 cm", "9 cm")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-1-1.2.1-OSC-101", "MH-9-MTH2-1-1.2.1", 1, ch1_name, "Betweenness of Points (A-B-C) & Collinear Points",
    q6_svg,
    "As shown in the collinear segment diagram above, point \\(Q\\) lies between \\(P\\) and \\(R\\) (\\(P-Q-R\\)). If \\(d(P, Q) = 6\\text{ cm}\\) and \\(d(Q, R) = 9\\text{ cm}\\), find \\(d(P, R)\\).",
    "\\(15\\text{ cm}\\)", ["\\(12\\text{ cm}\\)", "\\(3\\text{ cm}\\)", "\\(18\\text{ cm}\\)"],
    "**Step 1: Betweenness Property**\nFor collinear points \\(P-Q-R\\):\n\\(d(P, R) = d(P, Q) + d(Q, R)\\).\n**Step 2: Substitution**\n\\(d(P, R) = 6 + 9 = 15\\text{ cm}\\).\n**Step 3: Conclusion**\n\\(d(P, R) = 15\\text{ cm}\\).",
    "exam", 4, "easy"
))

# Q7: A-B-C with AC = 18, BC = 7 -> AB = 11
q7_svg = get_betweenness_svg('A', 'B', 'C', "?", "7 cm", "Betweenness A-B-C with Total AC = 18 cm")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-1-1.2.1-OSC-102", "MH-9-MTH2-1-1.2.1", 1, ch1_name, "Betweenness of Points (A-B-C) & Collinear Points",
    q7_svg,
    "In the diagram above, points \\(A, B, C\\) are collinear with \\(A-B-C\\). If total length \\(d(A, C) = 18\\text{ cm}\\) and \\(d(B, C) = 7\\text{ cm}\\), what is \\(d(A, B)\\)?",
    "\\(11\\text{ cm}\\)", ["\\(10\\text{ cm}\\)", "\\(12\\text{ cm}\\)", "\\(25\\text{ cm}\\)"],
    "**Step 1: Formula**\n\\(d(A, C) = d(A, B) + d(B, C) \\implies d(A, B) = d(A, C) - d(B, C)\\).\n**Step 2: Calculation**\n\\(d(A, B) = 18 - 7 = 11\\text{ cm}\\).\n**Step 3: Conclusion**\n\\(d(A, B) = 11\\text{ cm}\\).",
    "exam", 4, "medium"
))

# Q8: X-Y-Z with XY = 12, YZ = 16 -> XZ = 28
q8_svg = get_betweenness_svg('X', 'Y', 'Z', "12 cm", "16 cm", "Collinear Points X-Y-Z")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-1-1.2.1-OSC-103", "MH-9-MTH2-1-1.2.1", 1, ch1_name, "Betweenness of Points (A-B-C) & Collinear Points",
    q8_svg,
    "In the collinear points figure above, \\(Y\\) lies between \\(X\\) and \\(Z\\). If \\(XY = 12\\text{ cm}\\) and \\(YZ = 16\\text{ cm}\\), what is the total length of \\(XZ\\)?",
    "\\(28\\text{ cm}\\)", ["\\(24\\text{ cm}\\)", "\\(4\\text{ cm}\\)", "\\(30\\text{ cm}\\)"],
    "**Step 1: Formula**\n\\(XZ = XY + YZ\\).\n**Step 2: Calculation**\n\\(XZ = 12 + 16 = 28\\text{ cm}\\).\n**Step 3: Conclusion**\nTotal length \\(XZ = 28\\text{ cm}\\).",
    "exam", 4, "easy"
))

# Q9: L-M-N with LN = 30, LM = 13 -> MN = 17
q9_svg = get_betweenness_svg('L', 'M', 'N', "13 cm", "?", "Betweenness L-M-N with Total LN = 30 cm")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-1-1.2.1-OSC-104", "MH-9-MTH2-1-1.2.1", 1, ch1_name, "Betweenness of Points (A-B-C) & Collinear Points",
    q9_svg,
    "Referring to the collinear points diagram above, \\(L-M-N\\) with \\(LN = 30\\text{ cm}\\) and \\(LM = 13\\text{ cm}\\). Find the length of \\(MN\\).",
    "\\(17\\text{ cm}\\)", ["\\(15\\text{ cm}\\)", "\\(16\\text{ cm}\\)", "\\(43\\text{ cm}\\)"],
    "**Step 1: Relationship**\n\\(LN = LM + MN \\implies MN = LN - LM\\).\n**Step 2: Calculation**\n\\(MN = 30 - 13 = 17\\text{ cm}\\).\n**Step 3: Conclusion**\n\\(MN = 17\\text{ cm}\\).",
    "exam", 4, "medium"
))

# Q10: A-B-C where B is midpoint of AC, AC = 24 -> AB = 12
q10_svg = get_betweenness_svg('A', 'B', 'C', "x", "x", "Point B is Midpoint of AC (AC = 24 cm)")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-1-1.2.1-OSC-105", "MH-9-MTH2-1-1.2.1", 1, ch1_name, "Betweenness of Points (A-B-C) & Collinear Points",
    q10_svg,
    "In the diagram above, \\(B\\) is the midpoint of segment \\(AC\\) such that \\(AB = BC\\). If \\(AC = 24\\text{ cm}\\), find the length of \\(AB\\).",
    "\\(12\\text{ cm}\\)", ["\\(6\\text{ cm}\\)", "\\(10\\text{ cm}\\)", "\\(14\\text{ cm}\\)"],
    "**Step 1: Midpoint Definition**\nA point \\(B\\) on \\(AC\\) with \\(AB = BC\\) divides \\(AC\\) into two equal halves.\n**Step 2: Calculation**\n\\(AB = \\frac{1}{2} AC = \\frac{24}{2} = 12\\text{ cm}\\).\n**Step 3: Conclusion**\n\\(AB = 12\\text{ cm}\\).",
    "exam", 4, "easy"
))


# ==============================================================================
# CHAPTER 2: PARALLEL LINES (10 questions)
# ==============================================================================
ch2_name = "Parallel Lines"

# Transversal cutting parallel lines l and m
def get_parallel_lines_svg(angle_top_str, angle_bot_str, angle_type_label, is_alternate=True):
    # Two horizontal lines l and m with transversal t slanted
    svg = f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 190" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">Parallel Lines cut by Transversal</text>
  <!-- Line l (top) -->
  <line x1="30" y1="65" x2="330" y2="65" stroke="#38bdf8" stroke-width="2.2"/>
  <text x="340" y="69" fill="#38bdf8" font-size="12" font-style="italic" font-family="sans-serif">l</text>
  <!-- Line m (bottom) -->
  <line x1="30" y1="135" x2="330" y2="135" stroke="#38bdf8" stroke-width="2.2"/>
  <text x="340" y="139" fill="#38bdf8" font-size="12" font-style="italic" font-family="sans-serif">m</text>
  <!-- Transversal t -->
  <line x1="80" y1="25" x2="280" y2="175" stroke="#f59e0b" stroke-width="2.2"/>
  <text x="290" y="180" fill="#f59e0b" font-size="12" font-style="italic" font-family="sans-serif">t</text>
  <!-- Intersection points: (133, 65) and (227, 135) -->
  <circle cx="133.3" cy="65" r="4" fill="#f8fafc"/>
  <circle cx="226.7" cy="135" r="4" fill="#f8fafc"/>
  <!-- Angle arcs & text labels -->
  <!-- Top angle label -->
  <text x="155" y="86" fill="#f59e0b" font-size="12" font-weight="bold" font-family="sans-serif">{angle_top_str}</text>
  <!-- Bottom angle label -->
  <text x="195" y="125" fill="#38bdf8" font-size="12" font-weight="bold" font-family="sans-serif">{angle_bot_str}</text>
  <!-- Parallel note -->
  <text x="60" y="170" fill="#94a3b8" font-size="11" font-family="sans-serif">{angle_type_label}</text>
</svg>
</div>"""
    return svg

# Q11: Alternate interior angle: top = 70°, bot = x -> x = 70°
q11_svg = get_parallel_lines_svg("70°", "x", "line l ∥ line m", True)
figure_questions.append(build_fig_q(
    "MH-9-MTH2-2-2.1.1-OSC-101", "MH-9-MTH2-2-2.1.1", 2, ch2_name, "Corresponding Angles & Alternate Angles Theorem",
    q11_svg,
    "In the figure above, line \\(l \\parallel m\\) and line \\(t\\) is a transversal. What is the value of the alternate interior angle \\(x\\)?",
    "\\(70^\\circ\\)", ["\\(110^\\circ\\)", "\\(60^\\circ\\)", "\\(80^\\circ\\)"],
    "**Step 1: Theorem**\nWhen two parallel lines are cut by a transversal, alternate interior angles are congruent (equal).\n**Step 2: Equating Angles**\nHere, the angle measuring \\(70^\\circ\\) and angle \\(x\\) form a pair of alternate interior angles.\n\\(x = 70^\\circ\\).\n**Step 3: Conclusion**\n\\(x = 70^\\circ\\).",
    "exam", 4, "easy"
))

# Q12: Alternate interior angle: top = 115°, bot = x -> x = 115°
q12_svg = get_parallel_lines_svg("115°", "x", "line l ∥ line m", True)
figure_questions.append(build_fig_q(
    "MH-9-MTH2-2-2.1.1-OSC-102", "MH-9-MTH2-2-2.1.1", 2, ch2_name, "Corresponding Angles & Alternate Angles Theorem",
    q12_svg,
    "In the parallel lines figure above with line \\(l \\parallel m\\), find the value of angle \\(x\\) if its alternate interior angle measures \\(115^\\circ\\).",
    "\\(115^\\circ\\)", ["\\(65^\\circ\\)", "\\(105^\\circ\\)", "\\(125^\\circ\\)"],
    "**Step 1: Geometric Property**\nAlternate interior angles formed by a transversal intersecting parallel lines are equal in measure.\n**Step 2: Conclusion**\n\\(x = 115^\\circ\\).",
    "exam", 4, "easy"
))

# Q13: Corresponding angles: angle = 80°, corresponding angle = x -> x = 80°
q13_svg = get_parallel_lines_svg("80°", "x", "Corresponding Angles (l ∥ m)")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-2-2.1.1-OSC-103", "MH-9-MTH2-2-2.1.1", 2, ch2_name, "Corresponding Angles & Alternate Angles Theorem",
    q13_svg,
    "Refer to the figure above showing line \\(l \\parallel m\\) intersected by transversal \\(t\\). What is the value of the angle \\(x\\) if it corresponds to an angle of \\(80^\\circ\\)?",
    "\\(80^\\circ\\)", ["\\(100^\\circ\\)", "\\(90^\\circ\\)", "\\(70^\\circ\\)"],
    "**Step 1: Corresponding Angles Axiom**\nIf two parallel lines are intersected by a transversal, each pair of corresponding angles has equal measure.\n**Step 2: Calculation**\n\\(x = 80^\\circ\\).\n**Step 3: Conclusion**\n\\(x = 80^\\circ\\).",
    "exam", 4, "easy"
))

# Q14: Alternate angles: 3x and 75° -> x = 25°
q14_svg = get_parallel_lines_svg("75°", "3x", "line l ∥ line m")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-2-2.1.1-OSC-104", "MH-9-MTH2-2-2.1.1", 2, ch2_name, "Corresponding Angles & Alternate Angles Theorem",
    q14_svg,
    "In the diagram above, line \\(l \\parallel m\\) and transversal \\(t\\) forms alternate interior angles measuring \\(75^\\circ\\) and \\(3x\\). What is the value of \\(x\\)?",
    "\\(25^\\circ\\)", ["\\(15^\\circ\\)", "\\(35^\\circ\\)", "\\(20^\\circ\\)"],
    "**Step 1: Alternate Angles Equality**\n\\(3x = 75^\\circ\\).\n**Step 2: Solve for x**\n\\(x = \\frac{75^\\circ}{3} = 25^\\circ\\).\n**Step 3: Conclusion**\n\\(x = 25^\\circ\\).",
    "exam", 4, "medium"
))

# Q15: Corresponding angles: 2x + 10° and 70° -> 2x = 60° -> x = 30°
q15_svg = get_parallel_lines_svg("70°", "2x + 10°", "line l ∥ line m")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-2-2.1.1-OSC-105", "MH-9-MTH2-2-2.1.1", 2, ch2_name, "Corresponding Angles & Alternate Angles Theorem",
    q15_svg,
    "In the figure above with \\(l \\parallel m\\), the marked corresponding angles are \\(70^\\circ\\) and \\(2x + 10^\\circ\\). What is the value of \\(x\\)?",
    "\\(30^\\circ\\)", ["\\(40^\\circ\\)", "\\(35^\\circ\\)", "\\(25^\\circ\\)"],
    "**Step 1: Set up Equation**\nCorresponding angles are equal: \\(2x + 10^\\circ = 70^\\circ\\).\n**Step 2: Solve**\n\\(2x = 70^\\circ - 10^\\circ = 60^\\circ \\implies x = 30^\\circ\\).\n**Step 3: Conclusion**\n\\(x = 30^\\circ\\).",
    "exam", 4, "medium"
))

# Consecutive Interior Angles on the same side: sum to 180°
def get_interior_angles_svg(ang1, ang2):
    svg = f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 190" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">Interior Angles on Same Side of Transversal</text>
  <line x1="30" y1="65" x2="330" y2="65" stroke="#38bdf8" stroke-width="2.2"/>
  <text x="340" y="69" fill="#38bdf8" font-size="12" font-style="italic" font-family="sans-serif">l</text>
  <line x1="30" y1="135" x2="330" y2="135" stroke="#38bdf8" stroke-width="2.2"/>
  <text x="340" y="139" fill="#38bdf8" font-size="12" font-style="italic" font-family="sans-serif">m</text>
  <line x1="80" y1="25" x2="280" y2="175" stroke="#f59e0b" stroke-width="2.2"/>
  <text x="290" y="180" fill="#f59e0b" font-size="12" font-style="italic" font-family="sans-serif">t</text>
  <!-- Interior on same side (right side between lines): top-right and bot-right -->
  <text x="155" y="86" fill="#f59e0b" font-size="12" font-weight="bold" font-family="sans-serif">{ang1}</text>
  <text x="245" y="125" fill="#38bdf8" font-size="12" font-weight="bold" font-family="sans-serif">{ang2}</text>
  <text x="60" y="170" fill="#94a3b8" font-size="11" font-family="sans-serif">line l ∥ line m</text>
</svg>
</div>"""
    return svg

# Q16: Interior angles on same side: 120° and x -> x = 60°
q16_svg = get_interior_angles_svg("120°", "x")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-2-2.2.1-OSC-101", "MH-9-MTH2-2-2.2.1", 2, ch2_name, "Interior Angles Theorem & Supplementary Angles",
    q16_svg,
    "In the figure above, line \\(l \\parallel m\\) and line \\(t\\) is the transversal. If one interior angle on the right side is \\(120^\\circ\\), what is the value of the consecutive interior angle \\(x\\)?",
    "\\(60^\\circ\\)", ["\\(120^\\circ\\)", "\\(70^\\circ\\)", "\\(50^\\circ\\)"],
    "**Step 1: Theorem**\nInterior angles on the same side of a transversal intersecting two parallel lines are supplementary (sum to \\(180^\\circ\\)).\n**Step 2: Calculation**\n\\(120^\\circ + x = 180^\\circ \\implies x = 180^\\circ - 120^\\circ = 60^\\circ\\).\n**Step 3: Conclusion**\n\\(x = 60^\\circ\\).",
    "exam", 4, "easy"
))

# Q17: Interior angles: 2x and 3x -> 5x = 180° -> x = 36°
q17_svg = get_interior_angles_svg("2x", "3x")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-2-2.2.1-OSC-102", "MH-9-MTH2-2-2.2.1", 2, ch2_name, "Interior Angles Theorem & Supplementary Angles",
    q17_svg,
    "As shown in the figure above, the two interior angles on the same side of transversal \\(t\\) are \\(2x\\) and \\(3x\\). Find the value of \\(x\\).",
    "\\(36^\\circ\\)", ["\\(30^\\circ\\)", "\\(40^\\circ\\)", "\\(45^\\circ\\)"],
    "**Step 1: Supplementary Condition**\n\\(2x + 3x = 180^\\circ\\).\n**Step 2: Solve**\n\\(5x = 180^\\circ \\implies x = 36^\\circ\\).\n**Step 3: Conclusion**\n\\(x = 36^\\circ\\).",
    "exam", 4, "medium"
))

# Q18: Interior angles: x + 20° and x -> 2x + 20 = 180 -> x = 80°
q18_svg = get_interior_angles_svg("x + 20°", "x")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-2-2.2.1-OSC-103", "MH-9-MTH2-2-2.2.1", 2, ch2_name, "Interior Angles Theorem & Supplementary Angles",
    q18_svg,
    "In the given figure with \\(l \\parallel m\\), the interior angles on the same side are marked as \\(x + 20^\\circ\\) and \\(x\\). What is the value of \\(x\\)?",
    "\\(80^\\circ\\)", ["\\(100^\\circ\\)", "\\(70^\\circ\\)", "\\(60^\\circ\\)"],
    "**Step 1: Form Equation**\n\\((x + 20^\\circ) + x = 180^\\circ\\).\n**Step 2: Solve**\n\\(2x + 20^\\circ = 180^\\circ \\implies 2x = 160^\\circ \\implies x = 80^\\circ\\).\n**Step 3: Conclusion**\n\\(x = 80^\\circ\\).",
    "exam", 4, "medium"
))

# Q19: Interior angles: 105° and y -> y = 75°
q19_svg = get_interior_angles_svg("105°", "y")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-2-2.2.1-OSC-104", "MH-9-MTH2-2-2.2.1", 2, ch2_name, "Interior Angles Theorem & Supplementary Angles",
    q19_svg,
    "In the parallel lines figure above, what is the measure of angle \\(y\\) if its consecutive interior angle is \\(105^\\circ\\)?",
    "\\(75^\\circ\\)", ["\\(105^\\circ\\)", "\\(85^\\circ\\)", "\\(65^\\circ\\)"],
    "**Step 1: Formula**\nInterior angles on the same side add up to \\(180^\\circ\\).\n\\(y = 180^\\circ - 105^\\circ = 75^\\circ\\).\n**Step 2: Conclusion**\n\\(y = 75^\\circ\\).",
    "exam", 4, "easy"
))

# Q20: Interior angles: 4x and x -> 5x = 180 -> x = 36°, larger angle = 4x = 144°
q20_svg = get_interior_angles_svg("4x", "x")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-2-2.2.1-OSC-105", "MH-9-MTH2-2-2.2.1", 2, ch2_name, "Interior Angles Theorem & Supplementary Angles",
    q20_svg,
    "In the figure above, the consecutive interior angles are in the ratio \\(4:1\\) (represented by \\(4x\\) and \\(x\\)). What is the measure of the larger interior angle \\(4x\\)?",
    "\\(144^\\circ\\)", ["\\(36^\\circ\\)", "\\(120^\\circ\\)", "\\(150^\\circ\\)"],
    "**Step 1: Equation**\n\\(4x + x = 180^\\circ \\implies 5x = 180^\\circ \\implies x = 36^\\circ\\).\n**Step 2: Compute larger angle**\nLarger angle \\(= 4x = 4 \\times 36^\\circ = 144^\\circ\\).\n**Step 3: Conclusion**\nThe larger angle is \\(144^\\circ\\).",
    "exam", 4, "medium"
))


# ==============================================================================
# CHAPTER 3: TRIANGLES (12 questions)
# ==============================================================================
ch3_name = "Triangles"

# --- 3.1.1: Congruence Tests (4 questions) ---
# Congruence SVG comparing two triangles ABC and PQR
def get_congruent_triangles_svg(crit_label):
    svg = f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 170" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">Triangle Congruence Inspection</text>
  <!-- Triangle ABC on left -->
  <polygon points="80,45 25,135 135,135" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="80" cy="45" r="3.5" fill="#f8fafc"/>
  <circle cx="25" cy="135" r="3.5" fill="#f8fafc"/>
  <circle cx="135" cy="135" r="3.5" fill="#f8fafc"/>
  <text x="80" y="36" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">A</text>
  <text x="14" y="142" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">B</text>
  <text x="142" y="142" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">C</text>
  
  <!-- Triangle PQR on right -->
  <polygon points="280,45 225,135 335,135" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="280" cy="45" r="3.5" fill="#f8fafc"/>
  <circle cx="225" cy="135" r="3.5" fill="#f8fafc"/>
  <circle cx="335" cy="135" r="3.5" fill="#f8fafc"/>
  <text x="280" y="36" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">P</text>
  <text x="214" y="142" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">Q</text>
  <text x="342" y="142" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">R</text>
  
  <!-- Congruence test tag -->
  <text x="180" y="158" fill="#38bdf8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{crit_label}</text>
</svg>
</div>"""
    return svg

# Q21: SAS test
q21_svg = get_congruent_triangles_svg("AB = PQ, BC = QR, ∠B = ∠Q (SAS)")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-3-3.1.1-OSC-101", "MH-9-MTH2-3-3.1.1", 3, ch3_name, "Congruence of Triangles (SAS, SSS, ASA, AAS, RHS)",
    q21_svg,
    "In the figure above, for \\(\\triangle ABC\\) and \\(\\triangle PQR\\), \\(AB = PQ\\), \\(BC = QR\\), and the included angle \\(\\angle B = \\angle Q\\). By which criterion are the two triangles congruent?",
    "Side-Angle-Side (SAS) test", ["Side-Side-Side (SSS) test", "Angle-Side-Angle (ASA) test", "Hypotenuse-Side (RHS) test"],
    "**Step 1: Identify Given Elements**\nTwo pairs of corresponding sides are equal (\\(AB = PQ\\) and \\(BC = QR\\)) and their included angle is equal (\\(\\angle B = \\angle Q\\)).\n**Step 2: Congruence Criterion**\nBy the Side-Angle-Side (SAS) congruence test, \\(\\triangle ABC \\cong \\triangle PQR\\).\n**Step 3: Conclusion**\nSide-Angle-Side (SAS) test.",
    "exam", 4, "easy"
))

# Q22: SSS test
q22_svg = get_congruent_triangles_svg("AB = PQ, BC = QR, AC = PR (SSS)")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-3-3.1.1-OSC-102", "MH-9-MTH2-3-3.1.1", 3, ch3_name, "Congruence of Triangles (SAS, SSS, ASA, AAS, RHS)",
    q22_svg,
    "As shown in the diagram above, all three corresponding sides of \\(\\triangle ABC\\) and \\(\\triangle PQR\\) are equal: \\(AB = PQ\\), \\(BC = QR\\), and \\(AC = PR\\). Which congruence test applies?",
    "Side-Side-Side (SSS) test", ["Side-Angle-Side (SAS) test", "Angle-Side-Angle (ASA) test", "Hypotenuse-Side (RHS) test"],
    "**Step 1: Test Identification**\nWhen all three pairs of corresponding sides are congruent, the triangles are congruent by the Side-Side-Side (SSS) test.\n**Step 2: Conclusion**\nSide-Side-Side (SSS) test.",
    "exam", 4, "easy"
))

# Q23: ASA test
q23_svg = get_congruent_triangles_svg("∠B = ∠Q, ∠C = ∠R, BC = QR (ASA)")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-3-3.1.1-OSC-103", "MH-9-MTH2-3-3.1.1", 3, ch3_name, "Congruence of Triangles (SAS, SSS, ASA, AAS, RHS)",
    q23_svg,
    "In the diagram above, \\(\\angle B = \\angle Q\\), \\(\\angle C = \\angle R\\), and the included side \\(BC = QR\\). Which test proves \\(\\triangle ABC \\cong \\triangle PQR\\)?",
    "Angle-Side-Angle (ASA) test", ["Side-Angle-Side (SAS) test", "Side-Side-Side (SSS) test", "Hypotenuse-Side (RHS) test"],
    "**Step 1: Analysis**\nTwo angles and the included side of \\(\\triangle ABC\\) are equal to two angles and the included side of \\(\\triangle PQR\\).\n**Step 2: Conclusion**\nAngle-Side-Angle (ASA) test.",
    "exam", 4, "easy"
))

# Q24: RHS test
q24_svg = get_congruent_triangles_svg("∠B = ∠Q = 90°, AC = PR, AB = PQ (RHS)")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-3-3.1.1-OSC-104", "MH-9-MTH2-3-3.1.1", 3, ch3_name, "Congruence of Triangles (SAS, SSS, ASA, AAS, RHS)",
    q24_svg,
    "In two right triangles \\(\\triangle ABC\\) and \\(\\triangle PQR\\) (with \\(\\angle B = \\angle Q = 90^\\circ\\)), the hypotenuses \\(AC = PR\\) and one pair of legs \\(AB = PQ\\) are equal. By which test are they congruent?",
    "Hypotenuse-Side (RHS) test", ["Side-Angle-Side (SAS) test", "Side-Side-Side (SSS) test", "Angle-Side-Angle (ASA) test"],
    "**Step 1: Principle**\nIn two right-angled triangles, if the hypotenuse and one side of one triangle are congruent to the hypotenuse and corresponding side of the other, they are congruent by the Hypotenuse-Side (RHS) test.\n**Step 2: Conclusion**\nHypotenuse-Side (RHS) test.",
    "exam", 4, "easy"
))

# --- 3.2.1: Isosceles Triangle Theorem (4 questions) ---
def get_isosceles_triangle_svg(top_label, left_lbl, right_lbl, base_ang_lbl, vertex_ang_lbl):
    svg = f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 180" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">Isosceles Triangle Inspection</text>
  <!-- Triangle ABC -->
  <polygon points="180,45 80,145 280,145" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Tick marks for AB = AC -->
  <line x1="124" y1="92" x2="134" y2="98" stroke="#f59e0b" stroke-width="2.2"/>
  <line x1="226" y1="98" x2="236" y2="92" stroke="#f59e0b" stroke-width="2.2"/>
  <!-- Vertices -->
  <circle cx="180" cy="45" r="4" fill="#f8fafc"/>
  <circle cx="80" cy="145" r="4" fill="#f8fafc"/>
  <circle cx="280" cy="145" r="4" fill="#f8fafc"/>
  <text x="180" y="34" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{top_label}</text>
  <text x="65" y="152" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">{left_lbl}</text>
  <text x="290" y="152" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">{right_lbl}</text>
  <!-- Angle labels -->
  <text x="180" y="68" fill="#f59e0b" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">{vertex_ang_lbl}</text>
  <text x="105" y="138" fill="#38bdf8" font-size="12" font-weight="bold" font-family="sans-serif">{base_ang_lbl}</text>
</svg>
</div>"""
    return svg

# Q25: Isosceles triangle ABC: AB = AC, angle A = 50° -> angle B = (180 - 50)/2 = 65°
q25_svg = get_isosceles_triangle_svg("A", "B", "C", "∠B = ?", "50°")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-3-3.2.1-OSC-101", "MH-9-MTH2-3-3.2.1", 3, ch3_name, "Isosceles Triangle Theorem & Converse (30°-60°-90°, 45°-45°-90°)",
    q25_svg,
    "In the isosceles triangle \\(\\triangle ABC\\) shown above, side \\(AB = AC\\) and vertex angle \\(\\angle A = 50^\\circ\\). What is the measure of the base angle \\(\\angle B\\)?",
    "\\(65^\\circ\\)", ["\\(50^\\circ\\)", "\\(60^\\circ\\)", "\\(70^\\circ\\)"],
    "**Step 1: Isosceles Triangle Theorem**\nAngles opposite to equal sides are equal: \\(\\angle B = \\angle C\\).\n**Step 2: Angle Sum Property**\n\\(\\angle A + \\angle B + \\angle C = 180^\\circ\\).\n\\(50^\\circ + 2\\angle B = 180^\\circ \\implies 2\\angle B = 130^\\circ \\implies \\angle B = 65^\\circ\\).\n**Step 3: Conclusion**\n\\(\\angle B = 65^\\circ\\).",
    "exam", 4, "easy"
))

# Q26: Isosceles triangle PQR: PQ = PR, base angle Q = 70° -> vertex angle P = 180 - 140 = 40°
q26_svg = get_isosceles_triangle_svg("P", "Q", "R", "70°", "∠P = ?")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-3-3.2.1-OSC-102", "MH-9-MTH2-3-3.2.1", 3, ch3_name, "Isosceles Triangle Theorem & Converse (30°-60°-90°, 45°-45°-90°)",
    q26_svg,
    "In \\(\\triangle PQR\\) shown above with \\(PQ = PR\\), the base angle \\(\\angle Q = 70^\\circ\\). What is the measure of the vertex angle \\(\\angle P\\)?",
    "\\(40^\\circ\\)", ["\\(50^\\circ\\)", "\\(55^\\circ\\)", "\\(70^\\circ\\)"],
    "**Step 1: Base Angles**\nSince \\(PQ = PR\\), \\(\\angle R = \\angle Q = 70^\\circ\\).\n**Step 2: Angle Sum Property**\n\\(\\angle P = 180^\\circ - (70^\\circ + 70^\\circ) = 180^\\circ - 140^\\circ = 40^\\circ\\).\n**Step 3: Conclusion**\n\\(\\angle P = 40^\\circ\\).",
    "exam", 4, "easy"
))

# Q27: Isosceles triangle ABC: AB = AC, vertex angle A = 90° -> base angle B = 45°
q27_svg = get_isosceles_triangle_svg("A", "B", "C", "∠B = ?", "90°")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-3-3.2.1-OSC-103", "MH-9-MTH2-3-3.2.1", 3, ch3_name, "Isosceles Triangle Theorem & Converse (30°-60°-90°, 45°-45°-90°)",
    q27_svg,
    "In the right isosceles triangle \\(\\triangle ABC\\) above, \\(AB = AC\\) and \\(\\angle A = 90^\\circ\\). What is the measure of base angle \\(\\angle B\\)?",
    "\\(45^\\circ\\)", ["\\(30^\\circ\\)", "\\(60^\\circ\\)", "\\(90^\\circ\\)"],
    "**Step 1: Calculation**\n\\(\\angle B = \\angle C = \\frac{180^\\circ - 90^\\circ}{2} = \\frac{90^\\circ}{2} = 45^\\circ\\).\n**Step 2: Conclusion**\n\\(\\angle B = 45^\\circ\\).",
    "exam", 4, "easy"
))

# Q28: Isosceles triangle XYZ: XY = XZ, vertex angle X = 40° -> base angle = 70°
q28_svg = get_isosceles_triangle_svg("X", "Y", "Z", "∠Y = ?", "40°")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-3-3.2.1-OSC-104", "MH-9-MTH2-3-3.2.1", 3, ch3_name, "Isosceles Triangle Theorem & Converse (30°-60°-90°, 45°-45°-90°)",
    q28_svg,
    "In \\(\\triangle XYZ\\) shown above, \\(XY = XZ\\) and \\(\\angle X = 40^\\circ\\). Find \\(\\angle Y\\).",
    "\\(70^\\circ\\)", ["\\(60^\\circ\\)", "\\(75^\\circ\\)", "\\(80^\\circ\\)"],
    "**Step 1: Formula**\n\\(\\angle Y = \\frac{180^\\circ - 40^\\circ}{2} = \\frac{140^\\circ}{2} = 70^\\circ\\).\n**Step 2: Conclusion**\n\\(\\angle Y = 70^\\circ\\).",
    "exam", 4, "easy"
))

# --- 3.3.1: Exterior Angle Theorem (4 questions) ---
def get_exterior_angle_svg(top_ang, bot_left_ang, ext_ang_lbl):
    svg = f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 170" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">Theorem of Remote Interior Angles</text>
  <!-- Extended base line B-C-D -->
  <line x1="40" y1="130" x2="330" y2="130" stroke="#64748b" stroke-width="2"/>
  <!-- Triangle ABC -->
  <polygon points="150,45 60,130 240,130" fill="#1e293b" stroke="#38bdf8" stroke-width="2.2"/>
  <!-- Vertices -->
  <circle cx="150" cy="45" r="4" fill="#f8fafc"/>
  <circle cx="60" cy="130" r="4" fill="#f8fafc"/>
  <circle cx="240" cy="130" r="4" fill="#f8fafc"/>
  <circle cx="320" cy="130" r="3" fill="#f59e0b"/>
  <text x="150" y="34" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">A</text>
  <text x="45" y="135" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">B</text>
  <text x="235" y="148" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">C</text>
  <text x="325" y="148" fill="#f59e0b" font-size="13" font-weight="bold" font-family="sans-serif">D</text>
  <!-- Remote Interior Angles -->
  <text x="150" y="68" fill="#38bdf8" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">{top_ang}</text>
  <text x="85" y="122" fill="#38bdf8" font-size="12" font-weight="bold" font-family="sans-serif">{bot_left_ang}</text>
  <!-- Exterior Angle ACD -->
  <text x="260" y="120" fill="#f59e0b" font-size="12" font-weight="bold" font-family="sans-serif">{ext_ang_lbl}</text>
</svg>
</div>"""
    return svg

# Q29: Ext angle ACD = 60° + 50° = 110°
q29_svg = get_exterior_angle_svg("60°", "50°", "x = ?")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-3-3.3.1-OSC-101", "MH-9-MTH2-3-3.3.1", 3, ch3_name, "Theorem of Remote Interior Angles of a Triangle",
    q29_svg,
    "In the diagram above, side \\(BC\\) of \\(\\triangle ABC\\) is extended to \\(D\\). The remote interior angles are \\(\\angle A = 60^\\circ\\) and \\(\\angle B = 50^\\circ\\). What is the measure of the exterior angle \\(\\angle ACD\\)?",
    "\\(110^\\circ\\)", ["\\(70^\\circ\\)", "\\(120^\\circ\\)", "\\(100^\\circ\\)"],
    "**Step 1: Theorem of Remote Interior Angles**\nThe measure of an exterior angle of a triangle is equal to the sum of its remote interior angles.\n\\(\\angle ACD = \\angle A + \\angle B\\).\n**Step 2: Calculation**\n\\(\\angle ACD = 60^\\circ + 50^\\circ = 110^\\circ\\).\n**Step 3: Conclusion**\n\\(\\angle ACD = 110^\\circ\\).",
    "exam", 4, "easy"
))

# Q30: Ext angle = 125°, remote angle A = 70° -> angle B = 125° - 70° = 55°
q30_svg = get_exterior_angle_svg("70°", "∠B = ?", "125°")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-3-3.3.1-OSC-102", "MH-9-MTH2-3-3.3.1", 3, ch3_name, "Theorem of Remote Interior Angles of a Triangle",
    q30_svg,
    "In the figure above, exterior angle \\(\\angle ACD = 125^\\circ\\) and remote interior angle \\(\\angle A = 70^\\circ\\). What is the measure of angle \\(\\angle B\\)?",
    "\\(55^\\circ\\)", ["\\(65^\\circ\\)", "\\(50^\\circ\\)", "\\(60^\\circ\\)"],
    "**Step 1: Formula**\n\\(\\angle ACD = \\angle A + \\angle B \\implies \\angle B = \\angle ACD - \\angle A\\).\n**Step 2: Calculation**\n\\(\\angle B = 125^\\circ - 70^\\circ = 55^\\circ\\).\n**Step 3: Conclusion**\n\\(\\angle B = 55^\\circ\\).",
    "exam", 4, "medium"
))

# Q31: Ext angle = 130°, remote interior angles are x and x (equal) -> x = 65°
q31_svg = get_exterior_angle_svg("x", "x", "130°")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-3-3.3.1-OSC-103", "MH-9-MTH2-3-3.3.1", 3, ch3_name, "Theorem of Remote Interior Angles of a Triangle",
    q31_svg,
    "As shown above, the exterior angle \\(\\angle ACD\\) is \\(130^\\circ\\) and the remote interior angles \\(\\angle A\\) and \\(\\angle B\\) are equal (both measure \\(x\\)). Find \\(x\\).",
    "\\(65^\\circ\\)", ["\\(60^\\circ\\)", "\\(70^\\circ\\)", "\\(50^\\circ\\)"],
    "**Step 1: Formula**\n\\(x + x = 130^\\circ \\implies 2x = 130^\\circ\\).\n**Step 2: Solve**\n\\(x = 65^\\circ\\).\n**Step 3: Conclusion**\n\\(x = 65^\\circ\\).",
    "exam", 4, "easy"
))

# Q32: Ext angle = 140°, remote angles 3x and 4x -> 7x = 140 -> x = 20°
q32_svg = get_exterior_angle_svg("4x", "3x", "140°")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-3-3.3.1-OSC-104", "MH-9-MTH2-3-3.3.1", 3, ch3_name, "Theorem of Remote Interior Angles of a Triangle",
    q32_svg,
    "In the diagram above, the remote interior angles of \\(\\triangle ABC\\) are in the ratio \\(4:3\\) (given as \\(4x\\) and \\(3x\\)). The exterior angle \\(\\angle ACD = 140^\\circ\\). Find \\(x\\).",
    "\\(20^\\circ\\)", ["\\(15^\\circ\\)", "\\(25^\\circ\\)", "\\(30^\\circ\\)"],
    "**Step 1: Equation**\n\\(4x + 3x = 140^\\circ \\implies 7x = 140^\\circ\\).\n**Step 2: Solve**\n\\(x = 20^\\circ\\).\n**Step 3: Conclusion**\n\\(x = 20^\\circ\\).",
    "exam", 4, "medium"
))


# ==============================================================================
# CHAPTER 5: QUADRILATERALS (10 questions)
# ==============================================================================
ch5_name = "Quadrilaterals"

# Parallelogram ABCD
def get_parallelogram_svg(a_lbl, b_lbl, c_lbl, d_lbl, title="Parallelogram ABCD"):
    svg = f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 170" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>
  <!-- Parallelogram: A(100,50), B(280,50), C(240,130), D(60,130) -->
  <polygon points="100,50 280,50 240,130 60,130" fill="#1e293b" stroke="#38bdf8" stroke-width="2.2"/>
  <!-- Vertices -->
  <circle cx="100" cy="50" r="4" fill="#f8fafc"/>
  <circle cx="280" cy="50" r="4" fill="#f8fafc"/>
  <circle cx="240" cy="130" r="4" fill="#f8fafc"/>
  <circle cx="60" cy="130" r="4" fill="#f8fafc"/>
  <text x="95" y="38" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">A</text>
  <text x="288" y="48" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">B</text>
  <text x="250" y="142" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">C</text>
  <text x="42" y="142" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">D</text>
  <!-- Labels -->
  <text x="100" y="72" fill="#f59e0b" font-size="11" font-weight="600" font-family="sans-serif">{a_lbl}</text>
  <text x="250" y="72" fill="#38bdf8" font-size="11" font-weight="600" font-family="sans-serif">{b_lbl}</text>
  <text x="215" y="122" fill="#f59e0b" font-size="11" font-weight="600" font-family="sans-serif">{c_lbl}</text>
  <text x="80" y="122" fill="#38bdf8" font-size="11" font-weight="600" font-family="sans-serif">{d_lbl}</text>
</svg>
</div>"""
    return svg

# Q33: Parallelogram ABCD with angle A = 70° -> opposite angle C = 70°
q33_svg = get_parallelogram_svg("70°", "", "∠C = ?", "")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-5-5.1.1-OSC-101", "MH-9-MTH2-5-5.1.1", 5, ch5_name, "Parallelogram: Properties of Sides, Angles & Diagonals",
    q33_svg,
    "In the parallelogram \\(ABCD\\) shown above, \\(\\angle A = 70^\\circ\\). What is the measure of the opposite angle \\(\\angle C\\)?",
    "\\(70^\\circ\\)", ["\\(110^\\circ\\)", "\\(140^\\circ\\)", "\\(90^\\circ\\)"],
    "**Step 1: Property of Parallelogram**\nOpposite angles of a parallelogram are congruent (equal in measure): \\(\\angle C = \\angle A\\).\n**Step 2: Conclusion**\n\\(\\angle C = 70^\\circ\\).",
    "exam", 4, "easy"
))

# Q34: Parallelogram ABCD with angle A = 70° -> adjacent angle B = 180° - 70° = 110°
q34_svg = get_parallelogram_svg("70°", "∠B = ?", "", "")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-5-5.1.1-OSC-102", "MH-9-MTH2-5-5.1.1", 5, ch5_name, "Parallelogram: Properties of Sides, Angles & Diagonals",
    q34_svg,
    "Refer to parallelogram \\(ABCD\\) above. If \\(\\angle A = 70^\\circ\\), what is the measure of the adjacent angle \\(\\angle B\\)?",
    "\\(110^\\circ\\)", ["\\(70^\\circ\\)", "\\(120^\\circ\\)", "\\(100^\\circ\\)"],
    "**Step 1: Adjacent Angles Property**\nAdjacent angles of a parallelogram are supplementary (sum to \\(180^\\circ\\)).\n\\(\\angle A + \\angle B = 180^\\circ\\).\n**Step 2: Calculation**\n\\(\\angle B = 180^\\circ - 70^\\circ = 110^\\circ\\).\n**Step 3: Conclusion**\n\\(\\angle B = 110^\\circ\\).",
    "exam", 4, "easy"
))

# Q35: Parallelogram opposite sides: AB = 3x - 2, CD = 16 -> 3x = 18 -> x = 6
q35_svg = get_parallelogram_svg("3x - 2", "", "16 cm", "", "Opposite Sides AB and CD")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-5-5.1.1-OSC-103", "MH-9-MTH2-5-5.1.1", 5, ch5_name, "Parallelogram: Properties of Sides, Angles & Diagonals",
    q35_svg,
    "In parallelogram \\(ABCD\\) shown above, opposite sides \\(AB\\) and \\(CD\\) measure \\(3x - 2\\) and \\(16\\text{ cm}\\) respectively. What is the value of \\(x\\)?",
    "\\(6\\)", ["\\(5\\)", "\\(7\\)", "\\(8\\)"],
    "**Step 1: Property**\nOpposite sides of a parallelogram are equal: \\(AB = CD\\).\n**Step 2: Solve**\n\\(3x - 2 = 16 \\implies 3x = 18 \\implies x = 6\\).\n**Step 3: Conclusion**\n\\(x = 6\\).",
    "exam", 4, "medium"
))

# Q36: Parallelogram opposite angles: 2x + 10° and 3x - 20° -> x = 30°
q36_svg = get_parallelogram_svg("2x + 10°", "", "3x - 20°", "", "Opposite Angles A and C")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-5-5.1.1-OSC-104", "MH-9-MTH2-5-5.1.1", 5, ch5_name, "Parallelogram: Properties of Sides, Angles & Diagonals",
    q36_svg,
    "In the parallelogram \\(ABCD\\) above, opposite angles \\(\\angle A = 2x + 10^\\circ\\) and \\(\\angle C = 3x - 20^\\circ\\). Find \\(x\\).",
    "\\(30^\\circ\\)", ["\\(25^\\circ\\)", "\\(35^\\circ\\)", "\\(20^\\circ\\)"],
    "**Step 1: Equate Opposite Angles**\n\\(3x - 20^\\circ = 2x + 10^\\circ\\).\n**Step 2: Solve**\n\\(3x - 2x = 10^\\circ + 20^\\circ \\implies x = 30^\\circ\\).\n**Step 3: Conclusion**\n\\(x = 30^\\circ\\).",
    "exam", 4, "medium"
))

# Q37: Diagonals of parallelogram ABCD bisect each other at M. If AM = 5 cm, AC = 10 cm
def get_parallelogram_diagonals_svg():
    svg = """<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 170" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">Diagonals Bisect Each Other at Point M</text>
  <polygon points="100,50 280,50 240,130 60,130" fill="#1e293b" stroke="#38bdf8" stroke-width="2.2"/>
  <!-- Diagonals AC and BD -->
  <line x1="100" y1="50" x2="240" y2="130" stroke="#f59e0b" stroke-width="1.8"/>
  <line x1="60" y1="130" x2="280" y2="50" stroke="#f59e0b" stroke-width="1.8"/>
  <!-- Point M at intersection (170, 90) -->
  <circle cx="170" cy="90" r="4" fill="#f8fafc"/>
  <text x="175" y="84" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">M</text>
  <text x="95" y="42" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">A</text>
  <text x="286" y="48" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">B</text>
  <text x="248" y="140" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">C</text>
  <text x="44" y="140" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">D</text>
  <text x="125" y="70" fill="#f59e0b" font-size="11" font-family="sans-serif">5 cm</text>
</svg>
</div>"""
    return svg

q37_svg = get_parallelogram_diagonals_svg()
figure_questions.append(build_fig_q(
    "MH-9-MTH2-5-5.1.1-OSC-105", "MH-9-MTH2-5-5.1.1", 5, ch5_name, "Parallelogram: Properties of Sides, Angles & Diagonals",
    q37_svg,
    "In the diagram above, diagonals \\(AC\\) and \\(BD\\) of parallelogram \\(ABCD\\) intersect at \\(M\\). If \\(AM = 5\\text{ cm}\\), what is the full length of diagonal \\(AC\\)?",
    "\\(10\\text{ cm}\\)", ["\\(5\\text{ cm}\\)", "\\(15\\text{ cm}\\)", "\\(2.5\\text{ cm}\\)"],
    "**Step 1: Property of Diagonals**\nThe diagonals of a parallelogram bisect each other. Therefore, \\(M\\) is the midpoint of diagonal \\(AC\\).\n**Step 2: Calculation**\n\\(AC = 2 \\times AM = 2 \\times 5 = 10\\text{ cm}\\).\n**Step 3: Conclusion**\n\\(AC = 10\\text{ cm}\\).",
    "exam", 4, "easy"
))

# --- 5.3.1: Midpoint Theorem (5 questions) ---
def get_midpoint_theorem_svg(bc_val, pq_val):
    svg = f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 170" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">Midpoint Theorem in Triangle ABC</text>
  <polygon points="180,40 60,140 300,140" fill="#1e293b" stroke="#38bdf8" stroke-width="2.2"/>
  <!-- Midpoints P(120, 90) on AB and Q(240, 90) on AC -->
  <line x1="120" y1="90" x2="240" y2="90" stroke="#f59e0b" stroke-width="2.2"/>
  <circle cx="180" cy="40" r="3.5" fill="#f8fafc"/>
  <circle cx="60" cy="140" r="3.5" fill="#f8fafc"/>
  <circle cx="300" cy="140" r="3.5" fill="#f8fafc"/>
  <circle cx="120" cy="90" r="4" fill="#f59e0b"/>
  <circle cx="240" cy="90" r="4" fill="#f59e0b"/>
  <text x="180" y="32" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">A</text>
  <text x="45" y="148" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">B</text>
  <text x="310" y="148" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">C</text>
  <text x="105" y="88" fill="#f59e0b" font-size="12" font-weight="bold" font-family="sans-serif">P</text>
  <text x="250" y="88" fill="#f59e0b" font-size="12" font-weight="bold" font-family="sans-serif">Q</text>
  <!-- Length labels -->
  <text x="180" y="82" fill="#f59e0b" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{pq_val}</text>
  <text x="180" y="158" fill="#38bdf8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{bc_val}</text>
</svg>
</div>"""
    return svg

# Q38: BC = 14 cm, PQ = 7 cm
q38_svg = get_midpoint_theorem_svg("BC = 14 cm", "PQ = ?")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-5-5.3.1-OSC-101", "MH-9-MTH2-5-5.3.1", 5, ch5_name, "Midpoint Theorem of Triangle & Converse",
    q38_svg,
    "In \\(\\triangle ABC\\) shown above, \\(P\\) is the midpoint of \\(AB\\) and \\(Q\\) is the midpoint of \\(AC\\). If \\(BC = 14\\text{ cm}\\), what is the length of segment \\(PQ\\)?",
    "\\(7\\text{ cm}\\)", ["\\(14\\text{ cm}\\)", "\\(28\\text{ cm}\\)", "\\(3.5\\text{ cm}\\)"],
    "**Step 1: Midpoint Theorem**\nThe segment joining the midpoints of any two sides of a triangle is parallel to the third side and half as long as that third side: \\(PQ = \\frac{1}{2} BC\\).\n**Step 2: Calculation**\n\\(PQ = \\frac{14}{2} = 7\\text{ cm}\\).\n**Step 3: Conclusion**\n\\(PQ = 7\\text{ cm}\\).",
    "exam", 4, "easy"
))

# Q39: PQ = 6 cm -> BC = 12 cm
q39_svg = get_midpoint_theorem_svg("BC = ?", "PQ = 6 cm")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-5-5.3.1-OSC-102", "MH-9-MTH2-5-5.3.1", 5, ch5_name, "Midpoint Theorem of Triangle & Converse",
    q39_svg,
    "In the diagram above, segment \\(PQ\\) joins the midpoints of sides \\(AB\\) and \\(AC\\) of \\(\\triangle ABC\\). If \\(PQ = 6\\text{ cm}\\), find the length of base \\(BC\\).",
    "\\(12\\text{ cm}\\)", ["\\(6\\text{ cm}\\)", "\\(3\\text{ cm}\\)", "\\(18\\text{ cm}\\)"],
    "**Step 1: Formula**\nBy the Midpoint Theorem, \\(BC = 2 \\times PQ\\).\n**Step 2: Calculation**\n\\(BC = 2 \\times 6 = 12\\text{ cm}\\).\n**Step 3: Conclusion**\n\\(BC = 12\\text{ cm}\\).",
    "exam", 4, "easy"
))

# Q40: BC = 20 cm -> PQ = 10 cm
q40_svg = get_midpoint_theorem_svg("BC = 20 cm", "PQ = ?")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-5-5.3.1-OSC-103", "MH-9-MTH2-5-5.3.1", 5, ch5_name, "Midpoint Theorem of Triangle & Converse",
    q40_svg,
    "Refer to \\(\\triangle ABC\\) above with midpoints \\(P\\) and \\(Q\\). If \\(BC = 20\\text{ cm}\\), what is \\(PQ\\)?",
    "\\(10\\text{ cm}\\)", ["\\(15\\text{ cm}\\)", "\\(5\\text{ cm}\\)", "\\(40\\text{ cm}\\)"],
    "**Step 1: Midpoint Theorem**\n\\(PQ = \\frac{1}{2} BC = \\frac{20}{2} = 10\\text{ cm}\\).\n**Step 2: Conclusion**\n\\(PQ = 10\\text{ cm}\\).",
    "exam", 4, "easy"
))

# Q41: PQ = 8.5 cm -> BC = 17 cm
q41_svg = get_midpoint_theorem_svg("BC = ?", "PQ = 8.5 cm")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-5-5.3.1-OSC-104", "MH-9-MTH2-5-5.3.1", 5, ch5_name, "Midpoint Theorem of Triangle & Converse",
    q41_svg,
    "In \\(\\triangle ABC\\) above, segment \\(PQ\\) connects midpoints \\(P\\) and \\(Q\\). If \\(PQ = 8.5\\text{ cm}\\), what is \\(BC\\)?",
    "\\(17\\text{ cm}\\)", ["\\(16\\text{ cm}\\)", "\\(18\\text{ cm}\\)", "\\(4.25\\text{ cm}\\)"],
    "**Step 1: Calculation**\n\\(BC = 2 \\times 8.5 = 17\\text{ cm}\\).\n**Step 2: Conclusion**\n\\(BC = 17\\text{ cm}\\).",
    "exam", 4, "easy"
))

# Q42: Perimeter of triangle APQ compared to ABC
q42_svg = get_midpoint_theorem_svg("Base BC", "Midsegment PQ")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-5-5.3.1-OSC-105", "MH-9-MTH2-5-5.3.1", 5, ch5_name, "Midpoint Theorem of Triangle & Converse",
    q42_svg,
    "In \\(\\triangle ABC\\) above, \\(P\\) and \\(Q\\) are midpoints of \\(AB\\) and \\(AC\\). If the perimeter of \\(\\triangle ABC\\) is \\(36\\text{ cm}\\), what is the perimeter of \\(\\triangle APQ\\)?",
    "\\(18\\text{ cm}\\)", ["\\(12\\text{ cm}\\)", "\\(9\\text{ cm}\\)", "\\(24\\text{ cm}\\)"],
    "**Step 1: Ratio of Sides**\nEach side of \\(\\triangle APQ\\) is exactly half of the corresponding side of \\(\\triangle ABC\\) (\\(AP = \\frac{1}{2}AB\\), \\(AQ = \\frac{1}{2}AC\\), \\(PQ = \\frac{1}{2}BC\\)).\n**Step 2: Perimeter**\n\\(\\text{Perimeter}(\\triangle APQ) = \\frac{1}{2} \\times \\text{Perimeter}(\\triangle ABC) = \\frac{36}{2} = 18\\text{ cm}\\).\n**Step 3: Conclusion**\n\\(18\\text{ cm}\\).",
    "exam", 4, "medium"
))


# ==============================================================================
# CHAPTER 6: CIRCLE (10 questions)
# ==============================================================================
ch6_name = "Circle"

# Circle with center O, chord AB, perpendicular OM
def get_circle_chord_svg(r_val, d_val, c_val):
    svg = f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 190" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">Perpendicular from Center to Chord</text>
  <!-- Main circle: center (180, 100), radius 65 -->
  <circle cx="180" cy="100" r="65" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <!-- Chord AB: horizontal at y = 135 -->
  <!-- dx = sqrt(65^2 - 35^2) = sqrt(4225 - 1225) = sqrt(3000) approx 54.7 -->
  <line x1="125" y1="135" x2="235" y2="135" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Perpendicular OM -->
  <line x1="180" y1="100" x2="180" y2="135" stroke="#f59e0b" stroke-width="2"/>
  <!-- Radius OA -->
  <line x1="180" y1="100" x2="125" y2="135" stroke="#f8fafc" stroke-width="1.6" stroke-dasharray="3,3"/>
  <!-- Points -->
  <circle cx="180" cy="100" r="3.5" fill="#f59e0b"/>
  <circle cx="125" cy="135" r="3.5" fill="#f8fafc"/>
  <circle cx="235" cy="135" r="3.5" fill="#f8fafc"/>
  <circle cx="180" cy="135" r="3" fill="#f59e0b"/>
  <text x="180" y="92" fill="#f59e0b" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">O</text>
  <text x="110" y="142" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">A</text>
  <text x="245" y="142" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">B</text>
  <text x="180" y="152" fill="#f59e0b" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">M</text>
  <!-- Dimension labels -->
  <text x="145" y="112" fill="#f8fafc" font-size="10" font-family="sans-serif">{r_val}</text>
  <text x="190" y="120" fill="#f59e0b" font-size="10" font-family="sans-serif">{d_val}</text>
  <text x="180" y="172" fill="#38bdf8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{c_val}</text>
</svg>
</div>"""
    return svg

# Q43: r = 10, OM = 6 -> AM = 8 -> AB = 16
q43_svg = get_circle_chord_svg("r = 10", "OM = 6", "Chord AB = ?")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-6-6.1.1-OSC-101", "MH-9-MTH2-6-6.1.1", 6, ch6_name, "Perpendicular from Centre of a Circle to a Chord Bisects Chord",
    q43_svg,
    "In the circle with center \\(O\\) shown above, radius \\(OA = 10\\text{ cm}\\) and perpendicular distance to chord \\(AB\\) is \\(OM = 6\\text{ cm}\\). What is the length of chord \\(AB\\)?",
    "\\(16\\text{ cm}\\)", ["\\(8\\text{ cm}\\)", "\\(12\\text{ cm}\\)", "\\(20\\text{ cm}\\)"],
    "**Step 1: Right Triangle OMA**\nIn right-angled triangle \\(\\triangle OMA\\), \\(AM^2 + OM^2 = OA^2\\).\n\\(AM = \\sqrt{OA^2 - OM^2} = \\sqrt{10^2 - 6^2} = \\sqrt{100 - 36} = \\sqrt{64} = 8\\text{ cm}\\).\n**Step 2: Chord Bisection Theorem**\nThe perpendicular from the center to a chord bisects the chord: \\(AB = 2 \\times AM = 2 \\times 8 = 16\\text{ cm}\\).\n**Step 3: Conclusion**\n\\(AB = 16\\text{ cm}\\).",
    "exam", 4, "medium"
))

# Q44: AB = 16 cm -> AM = 8 cm, OM = 6 cm -> radius OA = 10 cm
q44_svg = get_circle_chord_svg("r = ?", "OM = 6", "Chord AB = 16 cm")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-6-6.1.1-OSC-102", "MH-9-MTH2-6-6.1.1", 6, ch6_name, "Perpendicular from Centre of a Circle to a Chord Bisects Chord",
    q44_svg,
    "In the circle above, chord \\(AB = 16\\text{ cm}\\) and its perpendicular distance from center \\(O\\) is \\(OM = 6\\text{ cm}\\). What is the radius of the circle?",
    "\\(10\\text{ cm}\\)", ["\\(8\\text{ cm}\\)", "\\(12\\text{ cm}\\)", "\\(14\\text{ cm}\\)"],
    "**Step 1: Half Chord Length**\n\\(AM = \\frac{1}{2} AB = \\frac{16}{2} = 8\\text{ cm}\\).\n**Step 2: Pythagoras Theorem**\nRadius \\(OA = \\sqrt{OM^2 + AM^2} = \\sqrt{6^2 + 8^2} = \\sqrt{36 + 64} = \\sqrt{100} = 10\\text{ cm}\\).\n**Step 3: Conclusion**\nRadius is \\(10\\text{ cm}\\).",
    "exam", 4, "medium"
))

# Q45: r = 13 cm, OM = 5 cm -> AM = 12 cm -> AB = 24 cm
q45_svg = get_circle_chord_svg("r = 13", "OM = 5", "Chord AB = ?")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-6-6.1.1-OSC-103", "MH-9-MTH2-6-6.1.1", 6, ch6_name, "Perpendicular from Centre of a Circle to a Chord Bisects Chord",
    q45_svg,
    "In the diagram above, radius \\(OA = 13\\text{ cm}\\) and distance \\(OM = 5\\text{ cm}\\). Find the length of chord \\(AB\\).",
    "\\(24\\text{ cm}\\)", ["\\(12\\text{ cm}\\)", "\\(18\\text{ cm}\\)", "\\(26\\text{ cm}\\)"],
    "**Step 1: Calculate AM**\n\\(AM = \\sqrt{13^2 - 5^2} = \\sqrt{169 - 25} = \\sqrt{144} = 12\\text{ cm}\\).\n**Step 2: Chord Length**\n\\(AB = 2 \\times 12 = 24\\text{ cm}\\).\n**Step 3: Conclusion**\n\\(AB = 24\\text{ cm}\\).",
    "exam", 4, "medium"
))

# Q46: r = 17 cm, AB = 30 cm -> AM = 15 cm -> OM = 8 cm
q46_svg = get_circle_chord_svg("r = 17", "OM = ?", "Chord AB = 30 cm")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-6-6.1.1-OSC-104", "MH-9-MTH2-6-6.1.1", 6, ch6_name, "Perpendicular from Centre of a Circle to a Chord Bisects Chord",
    q46_svg,
    "As shown in the figure above, chord \\(AB = 30\\text{ cm}\\) in a circle of radius \\(17\\text{ cm}\\). What is the perpendicular distance \\(OM\\) from the center to chord \\(AB\\)?",
    "\\(8\\text{ cm}\\)", ["\\(15\\text{ cm}\\)", "\\(6\\text{ cm}\\)", "\\(10\\text{ cm}\\)"],
    "**Step 1: Half Chord**\n\\(AM = \\frac{30}{2} = 15\\text{ cm}\\).\n**Step 2: Compute OM**\n\\(OM = \\sqrt{OA^2 - AM^2} = \\sqrt{17^2 - 15^2} = \\sqrt{289 - 225} = \\sqrt{64} = 8\\text{ cm}\\).\n**Step 3: Conclusion**\n\\(OM = 8\\text{ cm}\\).",
    "exam", 4, "medium"
))

# Q47: r = 25 cm, OM = 7 cm -> AM = 24 cm -> AB = 48 cm
q47_svg = get_circle_chord_svg("r = 25", "OM = 7", "Chord AB = ?")
figure_questions.append(build_fig_q(
    "MH-9-MTH2-6-6.1.1-OSC-105", "MH-9-MTH2-6-6.1.1", 6, ch6_name, "Perpendicular from Centre of a Circle to a Chord Bisects Chord",
    q47_svg,
    "In the circle above, a chord is at a distance of \\(7\\text{ cm}\\) from center \\(O\\). If radius is \\(25\\text{ cm}\\), what is the length of chord \\(AB\\)?",
    "\\(48\\text{ cm}\\)", ["\\(24\\text{ cm}\\)", "\\(36\\text{ cm}\\)", "\\(50\\text{ cm}\\)"],
    "**Step 1: Half Chord**\n\\(AM = \\sqrt{25^2 - 7^2} = \\sqrt{625 - 49} = \\sqrt{576} = 24\\text{ cm}\\).\n**Step 2: Full Chord**\n\\(AB = 2 \\times 24 = 48\\text{ cm}\\).\n**Step 3: Conclusion**\n\\(AB = 48\\text{ cm}\\).",
    "exam", 4, "medium"
))

# Congruent Chords Equidistant from Center
def get_equidistant_chords_svg():
    svg = """<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 190" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">Congruent Chords Equidistant from Center</text>
  <circle cx="180" cy="100" r="65" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <!-- Top Chord AB at y = 65 -->
  <line x1="125" y1="65" x2="235" y2="65" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Bottom Chord CD at y = 135 -->
  <line x1="125" y1="135" x2="235" y2="135" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Perpendiculars OM and ON -->
  <line x1="180" y1="100" x2="180" y2="65" stroke="#f59e0b" stroke-width="2"/>
  <line x1="180" y1="100" x2="180" y2="135" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="180" cy="100" r="3.5" fill="#f59e0b"/>
  <circle cx="180" cy="65" r="3" fill="#f59e0b"/>
  <circle cx="180" cy="135" r="3" fill="#f59e0b"/>
  <text x="188" y="104" fill="#f59e0b" font-size="12" font-weight="bold" font-family="sans-serif">O</text>
  <text x="110" y="68" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">A</text>
  <text x="245" y="68" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">B</text>
  <text x="110" y="142" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">C</text>
  <text x="245" y="142" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">D</text>
  <text x="180" y="52" fill="#f59e0b" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">M</text>
  <text x="180" y="152" fill="#f59e0b" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">N</text>
</svg>
</div>"""
    return svg

# Q48: AB = CD = 16 cm, OM = 6 cm -> ON = 6 cm
q48_svg = get_equidistant_chords_svg()
figure_questions.append(build_fig_q(
    "MH-9-MTH2-6-6.2.1-OSC-101", "MH-9-MTH2-6-6.2.1", 6, ch6_name, "Congruent Chords of a Circle are Equidistant from Centre",
    q48_svg,
    "In the circle with center \\(O\\) shown above, chords \\(AB\\) and \\(CD\\) are congruent (\\(AB = CD = 16\\text{ cm}\\)). If the distance \\(OM = 6\\text{ cm}\\), what is the distance \\(ON\\)?",
    "\\(6\\text{ cm}\\)", ["\\(8\\text{ cm}\\)", "\\(12\\text{ cm}\\)", "\\(16\\text{ cm}\\)"],
    "**Step 1: Equidistant Chords Theorem**\nCongruent chords of a circle are equidistant from the center of the circle.\n**Step 2: Conclusion**\nSince \\(AB = CD\\), \\(ON = OM = 6\\text{ cm}\\).",
    "exam", 4, "easy"
))

# Q49: OM = ON = 5 cm, AB = 18 cm -> CD = 18 cm
figure_questions.append(build_fig_q(
    "MH-9-MTH2-6-6.2.1-OSC-102", "MH-9-MTH2-6-6.2.1", 6, ch6_name, "Congruent Chords of a Circle are Equidistant from Centre",
    q48_svg,
    "Refer to the figure above where chords \\(AB\\) and \\(CD\\) are equidistant from center \\(O\\) (\\(OM = ON = 5\\text{ cm}\\)). If \\(AB = 18\\text{ cm}\\), what is the length of chord \\(CD\\)?",
    "\\(18\\text{ cm}\\)", ["\\(9\\text{ cm}\\)", "\\(10\\text{ cm}\\)", "\\(36\\text{ cm}\\)"],
    "**Step 1: Converse Theorem**\nChords that are equidistant from the center of a circle are congruent (equal in length).\n**Step 2: Conclusion**\n\\(CD = AB = 18\\text{ cm}\\).",
    "exam", 4, "easy"
))

# Q50: Congruent chords equidistant: OM = 2x - 1, ON = x + 4 -> x = 5 -> OM = 9 cm
figure_questions.append(build_fig_q(
    "MH-9-MTH2-6-6.2.1-OSC-103", "MH-9-MTH2-6-6.2.1", 6, ch6_name, "Congruent Chords of a Circle are Equidistant from Centre",
    q48_svg,
    "In the circle above, congruent chords \\(AB\\) and \\(CD\\) have distances \\(OM = 2x - 1\\text{ cm}\\) and \\(ON = x + 4\\text{ cm}\\). What is the value of \\(x\\)?",
    "\\(5\\)", ["\\(4\\)", "\\(6\\)", "\\(3\\)"],
    "**Step 1: Equate Distances**\nCongruent chords are equidistant from center: \\(OM = ON\\).\n\\(2x - 1 = x + 4 \\implies 2x - x = 4 + 1 \\implies x = 5\\).\n**Step 2: Conclusion**\n\\(x = 5\\).",
    "exam", 4, "medium"
))

# Q51: Concentric circles with chord AB of outer circle intersecting inner at C and D -> AC = DB
def get_concentric_circles_svg():
    svg = """<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 190" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">Concentric Circles with Secant Line</text>
  <circle cx="180" cy="100" r="70" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="180" cy="100" r="42" fill="none" stroke="#f59e0b" stroke-width="2"/>
  <line x1="90" y1="100" x2="270" y2="100" stroke="#f8fafc" stroke-width="2.2"/>
  <!-- Points A, C, D, B from left to right -->
  <circle cx="110" cy="100" r="3.5" fill="#38bdf8"/>
  <circle cx="138" cy="100" r="3.5" fill="#f59e0b"/>
  <circle cx="222" cy="100" r="3.5" fill="#f59e0b"/>
  <circle cx="250" cy="100" r="3.5" fill="#38bdf8"/>
  <text x="105" y="122" fill="#38bdf8" font-size="12" font-weight="bold" font-family="sans-serif">A</text>
  <text x="135" y="122" fill="#f59e0b" font-size="12" font-weight="bold" font-family="sans-serif">C</text>
  <text x="220" y="122" fill="#f59e0b" font-size="12" font-weight="bold" font-family="sans-serif">D</text>
  <text x="255" y="122" fill="#38bdf8" font-size="12" font-weight="bold" font-family="sans-serif">B</text>
  <circle cx="180" cy="100" r="3.5" fill="#f8fafc"/>
  <text x="180" y="88" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">O</text>
</svg>
</div>"""
    return svg

q51_svg = get_concentric_circles_svg()
figure_questions.append(build_fig_q(
    "MH-9-MTH2-6-6.2.1-OSC-104", "MH-9-MTH2-6-6.2.1", 6, ch6_name, "Congruent Chords of a Circle are Equidistant from Centre",
    q51_svg,
    "In the concentric circles figure above with common center \\(O\\), a straight line intersects the outer circle at \\(A, B\\) and the inner circle at \\(C, D\\). Which relation is always true?",
    "\\(AC = DB\\)", ["\\(AC = 2DB\\)", "\\(AC + DB = AB\\)", "\\(AC = \\frac{1}{2}CD\\)"],
    "**Step 1: Perpendicular from Center**\nDraw perpendicular \\(OM\\) to line \\(AB\\). \\(OM\\) bisects chord \\(AB\\) (\\(AM = MB\\)) and also bisects chord \\(CD\\) (\\(CM = MD\\)).\n**Step 2: Subtracting**\n\\(AM - CM = MB - MD \\implies AC = DB\\).\n**Step 3: Conclusion**\n\\(AC = DB\\).",
    "exam", 4, "medium"
))

# Q52: Chords AB = 10 cm, CD = 10 cm. Radius = 13 cm. Distance = 12 cm.
figure_questions.append(build_fig_q(
    "MH-9-MTH2-6-6.2.1-OSC-105", "MH-9-MTH2-6-6.2.1", 6, ch6_name, "Congruent Chords of a Circle are Equidistant from Centre",
    q48_svg,
    "In a circle of radius \\(13\\text{ cm}\\), two congruent chords \\(AB\\) and \\(CD\\) each have length \\(10\\text{ cm}\\). What is the distance of each chord from the center \\(O\\)?",
    "\\(12\\text{ cm}\\)", ["\\(10\\text{ cm}\\)", "\\(8\\text{ cm}\\)", "\\(5\\text{ cm}\\)"],
    "**Step 1: Half Chord**\n\\(AM = \\frac{10}{2} = 5\\text{ cm}\\).\n**Step 2: Distance from Center**\n\\(d = \\sqrt{r^2 - AM^2} = \\sqrt{13^2 - 5^2} = \\sqrt{169 - 25} = \\sqrt{144} = 12\\text{ cm}\\).\n**Step 3: Conclusion**\nDistance is \\(12\\text{ cm}\\).",
    "exam", 4, "medium"
))


# ==============================================================================
# CHAPTER 7: COORDINATE GEOMETRY (8 questions)
# ==============================================================================
ch7_name = "Coordinate Geometry"

# Plotted Points in 4 Quadrants
def get_cartesian_plot_svg(pt_name, px, py):
    # Origin at (180, 100), scale 1 unit = 20 px
    cx = 180 + px * 20
    cy = 100 - py * 20
    svg = f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 200" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">Cartesian Coordinate Plane</text>
  <!-- Grid lines -->
  <line x1="30" y1="100" x2="330" y2="100" stroke="#64748b" stroke-width="2"/>
  <line x1="180" y1="25" x2="180" y2="185" stroke="#64748b" stroke-width="2"/>
  <text x="335" y="104" fill="#64748b" font-size="11" font-family="sans-serif">X</text>
  <text x="195" y="32" fill="#64748b" font-size="11" font-family="sans-serif">Y</text>
  <text x="168" y="115" fill="#64748b" font-size="11" font-family="sans-serif">O</text>
  <!-- Drop lines from point to axes -->
  <line x1="{cx}" y1="{cy}" x2="{cx}" y2="100" stroke="#f59e0b" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="{cx}" y1="{cy}" x2="180" y2="{cy}" stroke="#f59e0b" stroke-width="1.2" stroke-dasharray="3,3"/>
  <!-- Point dot & Label -->
  <circle cx="{cx}" cy="{cy}" r="4.5" fill="#38bdf8"/>
  <text x="{cx + 10}" y="{cy - 6}" fill="#38bdf8" font-size="13" font-weight="bold" font-family="sans-serif">{pt_name}</text>
  <!-- Axis tick marks & values -->
  <text x="{cx}" y="116" fill="#f59e0b" font-size="10" font-family="sans-serif" text-anchor="middle">{px}</text>
  <text x="165" y="{cy + 4}" fill="#f59e0b" font-size="10" font-family="sans-serif" text-anchor="end">{py}</text>
</svg>
</div>"""
    return svg

# Q53: Point A(3, 4) in Quadrant I
q53_svg = get_cartesian_plot_svg("A", 3, 4)
figure_questions.append(build_fig_q(
    "MH-9-MTH2-7-7.1.2-OSC-101", "MH-9-MTH2-7-7.1.2", 7, ch7_name, "Plotting points in all four quadrants",
    q53_svg,
    "Refer to the Cartesian coordinate plane above. What are the coordinates of the plotted point \\(A\\)?",
    "\\((3, 4)\\)", ["\\((4, 3)\\)", "\\((-3, 4)\\)", "\\((3, -4)\\)"],
    "**Step 1: Abscissa (x-coordinate)**\nTracing vertically to the X-axis gives \\(x = 3\\).\n**Step 2: Ordinate (y-coordinate)**\nTracing horizontally to the Y-axis gives \\(y = 4\\).\n**Step 3: Conclusion**\nCoordinates of \\(A\\) are \\((3, 4)\\).",
    "exam", 4, "easy"
))

# Q54: Point B(-4, 2) in Quadrant II
q54_svg = get_cartesian_plot_svg("B", -4, 2)
figure_questions.append(build_fig_q(
    "MH-9-MTH2-7-7.1.2-OSC-102", "MH-9-MTH2-7-7.1.2", 7, ch7_name, "Plotting points in all four quadrants",
    q54_svg,
    "In the coordinate plane above, identify the coordinates of point \\(B\\) lying in Quadrant II.",
    "\\((-4, 2)\\)", ["\\((4, -2)\\)", "\\((2, -4)\\)", "\\((-4, -2)\\)"],
    "**Step 1: Read Coordinates**\nProjection on X-axis is \\(-4\\), projection on Y-axis is \\(2\\).\n**Step 2: Conclusion**\nCoordinates of \\(B\\) are \\((-4, 2)\\).",
    "exam", 4, "easy"
))

# Q55: Point C(-3, -3) in Quadrant III
q55_svg = get_cartesian_plot_svg("C", -3, -3)
figure_questions.append(build_fig_q(
    "MH-9-MTH2-7-7.1.2-OSC-103", "MH-9-MTH2-7-7.1.2", 7, ch7_name, "Plotting points in all four quadrants",
    q55_svg,
    "What are the coordinates of point \\(C\\) plotted in Quadrant III in the diagram above?",
    "\\((-3, -3)\\)", ["\\((3, 3)\\)", "\\((-3, 3)\\)", "\\((3, -3)\\)"],
    "**Step 1: Quadrant III Signs**\nBoth x and y are negative: \\(x = -3\\), \\(y = -3\\).\n**Step 2: Conclusion**\nCoordinates are \\((-3, -3)\\).",
    "exam", 4, "easy"
))

# Q56: Point D(4, -2) in Quadrant IV
q56_svg = get_cartesian_plot_svg("D", 4, -2)
figure_questions.append(build_fig_q(
    "MH-9-MTH2-7-7.1.2-OSC-104", "MH-9-MTH2-7-7.1.2", 7, ch7_name, "Plotting points in all four quadrants",
    q56_svg,
    "In the coordinate graph above, determine the coordinates of point \\(D\\).",
    "\\((4, -2)\\)", ["\\((-2, 4)\\)", "\\((-4, -2)\\)", "\\((4, 2)\\)"],
    "**Step 1: Coordinates**\n\\(x = 4\\), \\(y = -2\\).\n**Step 2: Conclusion**\nCoordinates are \\((4, -2)\\).",
    "exam", 4, "easy"
))

# Line parallel to Y-axis or X-axis
def get_parallel_line_graph_svg(is_vertical, val):
    # Origin (180, 100), 1 unit = 20 px
    svg = [
        '<div style="display: flex; justify-content: center; margin: 12px 0;">',
        '<svg width="100%" height="auto" viewBox="0 0 360 200" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">',
        '  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">Line on Cartesian Plane</text>',
        '  <line x1="30" y1="100" x2="330" y2="100" stroke="#64748b" stroke-width="2"/>',
        '  <line x1="180" y1="25" x2="180" y2="185" stroke="#64748b" stroke-width="2"/>',
        '  <text x="335" y="104" fill="#64748b" font-size="11" font-family="sans-serif">X</text>',
        '  <text x="210" y="32" fill="#64748b" font-size="11" font-family="sans-serif">Y</text>'
    ]
    if is_vertical:
        lx = 180 + val * 20
        svg.append(f'  <line x1="{lx}" y1="25" x2="{lx}" y2="185" stroke="#38bdf8" stroke-width="2.5"/>')
        svg.append(f'  <circle cx="{lx}" cy="100" r="4" fill="#f59e0b"/>')
        svg.append(f'  <text x="{lx}" y="118" fill="#f59e0b" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">{val}</text>')
    else:
        ly = 100 - val * 20
        svg.append(f'  <line x1="30" y1="{ly}" x2="330" y2="{ly}" stroke="#38bdf8" stroke-width="2.5"/>')
        svg.append(f'  <circle cx="180" cy="{ly}" r="4" fill="#f59e0b"/>')
        svg.append(f'  <text x="160" y="{ly + 4}" fill="#f59e0b" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="end">{val}</text>')
        
    svg.append('</svg>\n</div>')
    return '\n'.join(svg)

# Q57: Vertical line x = 3
q57_svg = get_parallel_line_graph_svg(True, 3)
figure_questions.append(build_fig_q(
    "MH-9-MTH2-7-7.2.1-OSC-101", "MH-9-MTH2-7-7.2.1", 7, ch7_name, "Line parallel to Y-axis: x = c",
    q57_svg,
    "The blue line in the Cartesian plane above is parallel to the Y-axis and passes through \\((3, 0)\\). What is its equation?",
    "\\(x = 3\\)", ["\\(y = 5\\)", "\\(x + y = 0\\)", "\\(2x + y = 6\\)"],
    "**Step 1: Property**\nEvery point on a line parallel to the Y-axis has a constant x-coordinate.\n**Step 2: Equation**\nSince it passes through \\((3, 0)\\), \\(x = 3\\).\n**Step 3: Conclusion**\nEquation is \\(x = 3\\).",
    "exam", 4, "easy"
))

# Q58: Vertical line x = -2
q58_svg = get_parallel_line_graph_svg(True, -2)
figure_questions.append(build_fig_q(
    "MH-9-MTH2-7-7.2.1-OSC-102", "MH-9-MTH2-7-7.2.1", 7, ch7_name, "Line parallel to Y-axis: x = c",
    q58_svg,
    "In the diagram above, what is the equation of the line parallel to the Y-axis at a distance of \\(2\\) units to the left of the Y-axis?",
    "\\(x = -2\\)", ["\\(y = 4\\)", "\\(x - y = 0\\)", "\\(3x + 2y = 1\\)"],
    "**Step 1: Formula**\nA vertical line \\(2\\) units to the left of the Y-axis has equation \\(x = -2\\).\n**Step 2: Conclusion**\n\\(x = -2\\).",
    "exam", 4, "easy"
))

# Q59: Horizontal line y = 4
q59_svg = get_parallel_line_graph_svg(False, 4)
figure_questions.append(build_fig_q(
    "MH-9-MTH2-7-7.2.1-OSC-103", "MH-9-MTH2-7-7.2.1", 7, ch7_name, "Line parallel to Y-axis: x = c",
    q59_svg,
    "The graph above shows a horizontal line parallel to the X-axis passing through \\((0, 4)\\). What is its equation?",
    "\\(y = 4\\)", ["\\(x = 2\\)", "\\(x + y = 0\\)", "\\(2x - y = 5\\)"],
    "**Step 1: Property**\nA line parallel to the X-axis has constant y-coordinate: \\(y = c\\).\n**Step 2: Conclusion**\nSince it crosses the Y-axis at \\(4\\), the equation is \\(y = 4\\).",
    "exam", 4, "easy"
))

# Q60: Horizontal line y = -3
q60_svg = get_parallel_line_graph_svg(False, -3)
figure_questions.append(build_fig_q(
    "MH-9-MTH2-7-7.2.1-OSC-104", "MH-9-MTH2-7-7.2.1", 7, ch7_name, "Line parallel to Y-axis: x = c",
    q60_svg,
    "What is the equation of the line shown above that is parallel to the X-axis and \\(3\\) units below it?",
    "\\(y = -3\\)", ["\\(x = 5\\)", "\\(x - y = 0\\)", "\\(3x + y = 2\\)"],
    "**Step 1: Concept**\nDistance \\(3\\) units below X-axis means \\(y = -3\\).\n**Step 2: Conclusion**\n\\(y = -3\\).",
    "exam", 4, "easy"
))

print(f"Total Figure Questions Generated: {len(figure_questions)}")

output_file = "scripts/mh9_mth2_figure_questions.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(figure_questions, f, indent=2, ensure_ascii=False)

print(f"Saved {len(figure_questions)} figure questions to {output_file}")
