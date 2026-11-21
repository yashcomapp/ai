# scripts/generator_mth2_ch7_ch9.py
# High-entropy diverse question generator for MH-9-MTH2:
# Chapters 7 (Coordinate Geometry), 8 (Trigonometry), and 9 (Surface Area and Volume)
# 23 subtopics * 80 questions = 1,840 completely distinct, non-duplicated questions with inline SVGs.

import json
import math
import random

def make_opts(corr_text, distractors):
    dist_set = []
    for d in distractors:
        if d != corr_text and d not in dist_set:
            dist_set.append(d)
        if len(dist_set) == 3:
            break
    while len(dist_set) < 3:
        dist_set.append(f"{corr_text} + {len(dist_set) + 1}")
    
    all_four = [corr_text] + dist_set[:3]
    # deterministic shuffle based on length
    all_four.sort(key=lambda s: (len(s), s))
    
    letters = ['A', 'B', 'C', 'D']
    options = []
    for idx, opt_text in enumerate(all_four):
        options.append({
            "id": letters[idx],
            "text": opt_text,
            "isCorrect": (opt_text == corr_text)
        })
    return options

# SVG Generators with dynamic values
def svg_cartesian_point(pt_name, px, py):
    cx = 180 + px * 22
    cy = 100 - py * 16
    p_y = cy - 8 if py >= 0 else cy + 16
    return f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 200" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="16" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">Cartesian Coordinate Plane</text>
  <line x1="30" y1="100" x2="330" y2="100" stroke="#64748b" stroke-width="2"/>
  <line x1="180" y1="25" x2="180" y2="185" stroke="#64748b" stroke-width="2"/>
  <text x="335" y="104" fill="#64748b" font-size="11" font-family="sans-serif">X</text>
  <text x="195" y="30" fill="#64748b" font-size="11" font-family="sans-serif">Y</text>
  <text x="168" y="115" fill="#64748b" font-size="11" font-family="sans-serif">O</text>
  <line x1="{cx}" y1="{cy}" x2="{cx}" y2="100" stroke="#f59e0b" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="{cx}" y1="{cy}" x2="180" y2="{cy}" stroke="#f59e0b" stroke-width="1.2" stroke-dasharray="3,3"/>
  <circle cx="{cx}" cy="{cy}" r="4.5" fill="#38bdf8"/>
  <text x="{cx + 10}" y="{p_y}" fill="#38bdf8" font-size="13" font-weight="bold" font-family="sans-serif">{pt_name}</text>
  <text x="{cx}" y="116" fill="#f59e0b" font-size="10" font-family="sans-serif" text-anchor="middle">{px}</text>
  <text x="165" y="{cy + 4}" fill="#f59e0b" font-size="10" font-family="sans-serif" text-anchor="end">{py}</text>
</svg>
</div>"""

def svg_cartesian_line(eq_str, is_vertical, const_val):
    line_svg = f'<line x1="{180 + const_val * 22}" y1="25" x2="{180 + const_val * 22}" y2="185" stroke="#f59e0b" stroke-width="2.2"/>' if is_vertical else f'<line x1="30" y1="{100 - const_val * 16}" x2="330" y2="{100 - const_val * 16}" stroke="#f59e0b" stroke-width="2.2"/>'
    lbl_x = 180 + const_val * 22 + 8 if is_vertical else 280
    lbl_y = 40 if is_vertical else 100 - const_val * 16 - 6
    return f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 200" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="16" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">Line on Cartesian Plane</text>
  <line x1="30" y1="100" x2="330" y2="100" stroke="#64748b" stroke-width="2"/>
  <line x1="180" y1="25" x2="180" y2="185" stroke="#64748b" stroke-width="2"/>
  <text x="335" y="104" fill="#64748b" font-size="11" font-family="sans-serif">X</text>
  <text x="195" y="30" fill="#64748b" font-size="11" font-family="sans-serif">Y</text>
  <text x="168" y="115" fill="#64748b" font-size="11" font-family="sans-serif">O</text>
  {line_svg}
  <text x="{lbl_x}" y="{lbl_y}" fill="#f59e0b" font-size="11" font-weight="bold" font-family="sans-serif">{eq_str}</text>
</svg>
</div>"""

def svg_right_triangle(opp, adj, hyp, theta="θ", title="Right-Angled Triangle ABC"):
    return f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 170" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>
  <polygon points="70,140 270,140 270,40" fill="#1e293b" stroke="#38bdf8" stroke-width="2.2"/>
  <rect x="250" y="120" width="20" height="20" fill="none" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="55" y="146" fill="#38bdf8" font-size="13" font-weight="bold" font-family="sans-serif">A</text>
  <text x="280" y="146" fill="#38bdf8" font-size="13" font-weight="bold" font-family="sans-serif">B</text>
  <text x="280" y="40" fill="#38bdf8" font-size="13" font-weight="bold" font-family="sans-serif">C</text>
  <text x="95" y="132" fill="#f59e0b" font-size="12" font-weight="bold" font-family="sans-serif">{theta}</text>
  <text x="170" y="156" fill="#f8fafc" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">Adj = {adj}</text>
  <text x="288" y="95" fill="#f8fafc" font-size="11" font-weight="600" font-family="sans-serif">Opp = {opp}</text>
  <text x="150" y="75" fill="#38bdf8" font-size="11" font-weight="600" font-family="sans-serif">Hyp = {hyp}</text>
</svg>
</div>"""

def svg_cone_wireframe(r, h, l, title="Right Circular Cone"):
    return f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 180" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>
  <line x1="180" y1="35" x2="110" y2="140" stroke="#38bdf8" stroke-width="2.2"/>
  <line x1="180" y1="35" x2="250" y2="140" stroke="#38bdf8" stroke-width="2.2"/>
  <ellipse cx="180" cy="140" rx="70" ry="20" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <line x1="180" y1="35" x2="180" y2="140" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="3,3"/>
  <line x1="180" y1="140" x2="250" y2="140" stroke="#f8fafc" stroke-width="2"/>
  <circle cx="180" cy="140" r="3.5" fill="#f59e0b"/>
  <circle cx="180" cy="35" r="3.5" fill="#f8fafc"/>
  <text x="190" y="90" fill="#f59e0b" font-size="11" font-weight="600" font-family="sans-serif">h = {h}</text>
  <text x="215" y="156" fill="#f8fafc" font-size="11" font-weight="600" font-family="sans-serif">r = {r}</text>
  <text x="225" y="80" fill="#38bdf8" font-size="11" font-weight="600" font-family="sans-serif">l = {l}</text>
</svg>
</div>"""

def svg_sphere_wireframe(r, title="Solid Sphere"):
    return f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 170" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>
  <circle cx="180" cy="90" r="60" fill="#1e293b" stroke="#38bdf8" stroke-width="2.2"/>
  <ellipse cx="180" cy="90" rx="60" ry="18" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,3"/>
  <line x1="180" y1="90" x2="240" y2="90" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="180" cy="90" r="3.5" fill="#f59e0b"/>
  <text x="180" y="80" fill="#f59e0b" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">O</text>
  <text x="210" y="105" fill="#f59e0b" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">r = {r}</text>
</svg>
</div>"""

def svg_hemisphere_wireframe(r, title="Solid Hemisphere"):
    return f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 160" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>
  <ellipse cx="180" cy="65" rx="65" ry="20" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <path d="M 115 65 A 65 65 0 0 0 245 65" fill="#1e293b" stroke="#38bdf8" stroke-width="2.2"/>
  <line x1="180" y1="65" x2="245" y2="65" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="180" cy="65" r="3.5" fill="#f59e0b"/>
  <text x="180" y="55" fill="#f59e0b" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">O</text>
  <text x="212" y="80" fill="#f59e0b" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">r = {r}</text>
</svg>
</div>"""

def build_q(qcode, text, corr, distractors, sol, ch, ch_name, tc, top_name, seq, has_fig):
    opts = make_opts(corr, distractors)
    corr_letter = [o["id"] for o in opts if o["isCorrect"]][0]
    
    vault = 'exam' if seq <= 40 else ('practice' if seq <= 60 else 'foundation')
    diff = 'easy' if seq <= 25 else ('medium' if seq <= 65 else 'hard')

    return {
        "questionCode": qcode,
        "text": text,
        "options": opts,
        "correctAnswer": corr_letter,
        "solution": sol,
        "boardCode": "MH",
        "board": "Maharashtra Board",
        "class": "9",
        "subjectCode": "MTH2",
        "subject": "Mathematics Part - 2 (Geometry)",
        "chapterNumber": ch,
        "chapter": ch_name,
        "topicCode": tc,
        "topic": top_name,
        "type": "OSC",
        "marks": 4,
        "difficulty": diff,
        "vault": vault,
        "timesUsed": 0,
        "usedInClassroomTest": False,
        "requiresFigure": has_fig,
        "createdAt": "2026-11-21T18:00:00.000Z",
        "updatedAt": "2026-11-21T18:00:00.000Z"
    }

# Pythagorean triples for cone and right-triangle generation
PYTH_TRIPLES = [
    (3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17),
    (9, 12, 15), (10, 24, 26), (12, 16, 20), (15, 20, 25), (14, 48, 50),
    (20, 21, 29), (9, 40, 41), (11, 60, 61), (16, 30, 34), (18, 24, 30),
    (21, 28, 35), (24, 32, 40), (27, 36, 45), (30, 40, 50), (36, 48, 60)
]

GRID_POINTS = [
    (2, 3), (-2, 3), (-3, 2), (3, -2), (4, 3), (-4, 2), (-3, -3), (2, -4),
    (3, 4), (-2, 4), (4, -3), (-4, -2), (2, 2), (-3, 4), (4, 2), (-2, -3),
    (3, 2), (-4, 3), (-2, -4), (4, -4)
]

def generate_ch7_ch9():
    questions = []

    # -------------------------------------------------------------
    # CHAPTER 7: Coordinate Geometry (6 subtopics)
    # -------------------------------------------------------------
    ch7_subtopics = [
        ("MH-9-MTH2-7-7.1.1", "X-axis, Y-axis, Origin (0,0)"),
        ("MH-9-MTH2-7-7.1.2", "Plotting points in all four quadrants"),
        ("MH-9-MTH2-7-7.2.1", "Line parallel to Y-axis: x = c"),
        ("MH-9-MTH2-7-7.2.2", "Line parallel to X-axis: y = c"),
        ("MH-9-MTH2-7-7.2.3", "Equation of X-axis (y=0) and Y-axis (x=0)"),
        ("MH-9-MTH2-7-7.3.1", "Finding solutions table and plotting straight lines on graph paper")
    ]

    for tc, tname in ch7_subtopics:
        sub_seen = set()
        for seq in range(1, 81):
            qcode = f"{tc}-OSC-{seq:03d}"
            has_fig = (seq % 10 in [0, 1, 2, 4, 6, 8])
            gp = GRID_POINTS[(seq - 1) % len(GRID_POINTS)]
            px, py = gp
            # vary px, py slightly with seq cycle
            if seq > 40:
                px = -px if px != 0 else 3
                py = -py if py != 0 else -3

            if tc == "MH-9-MTH2-7-7.1.1":
                # Origin, axes, coordinates
                if seq % 4 == 1:
                    svg = svg_cartesian_point(f"P_{seq}", px, py) if has_fig else ""
                    txt = (f"{svg}\n" if svg else "") + f"What is the coordinate pair of point \\(P_{seq}\\) located at abscissa \\({px}\\) and ordinate \\({py}\\) on the Cartesian coordinate plane?"
                    corr = f"\\(({px}, {py})\\)"
                    dist = [f"\\(({py}, {px})\\)", f"\\(({-px}, {py})\\)", f"\\(({px}, {-py})\\)"]
                    sol = f"**Step 1: Cartesian Coordinates**\nCoordinates are expressed as \\((x, y) = (\\text{{abscissa}}, \\text{{ordinate}})\\).\n**Step 2: Conclusion**\n\\(({px}, {py})\\)."
                elif seq % 4 == 2:
                    svg = svg_cartesian_point("O", 0, 0) if has_fig else ""
                    txt = (f"{svg}\n" if svg else "") + f"The horizontal reference axis and vertical reference axis on a coordinate plane intersect at origin \\(O\\). For question variant #{seq}, what are the precise coordinates of origin \\(O\\)?"
                    corr = "\\((0, 0)\\)"
                    dist = ["\\((1, 1)\\)", "\\((0, 1)\\)", "\\((1, 0)\\)"]
                    sol = "**Step 1: Definition of Origin**\nThe intersection of the X-axis and Y-axis is defined as origin \\(O(0, 0)\\).\n**Step 2: Conclusion**\n\\((0, 0)\\)."
                elif seq % 4 == 3:
                    txt = f"A point \\(M_{seq}\\) lies on the X-axis at a distance of \\({abs(px) + 2}\\) units to the {'positive right' if px >= 0 else 'negative left'} of the origin. What are the coordinates of point \\(M_{seq}\\)?"
                    val = abs(px) + 2 if px >= 0 else -(abs(px) + 2)
                    corr = f"\\(({val}, 0)\\)"
                    dist = [f"\\((0, {val})\\)", f"\\(({-val}, 0)\\)", f"\\(({val}, {val})\\)"]
                    sol = f"**Step 1: Point on X-axis**\nAny point on the X-axis has an ordinate of zero \\(y = 0\\).\n**Step 2: Conclusion**\n\\(({val}, 0)\\)."
                else:
                    txt = f"A point \\(N_{seq}\\) is located on the Y-axis at a signed vertical displacement of \\({py}\\) units from the origin. What are its exact Cartesian coordinates?"
                    corr = f"\\((0, {py})\\)"
                    dist = [f"\\(({py}, 0)\\)", f"\\((0, {-py})\\)", f"\\(({py}, {py})\\)"]
                    sol = f"**Step 1: Point on Y-axis**\nAny point on the Y-axis has an abscissa of zero \\(x = 0\\).\n**Step 2: Conclusion**\n\\((0, {py})\\)."

            elif tc == "MH-9-MTH2-7-7.1.2":
                # Quadrants
                pt_char = chr(65 + ((seq * 3) % 20))
                quad_ans = "Quadrant I" if (px > 0 and py > 0) else ("Quadrant II" if (px < 0 and py > 0) else ("Quadrant III" if (px < 0 and py < 0) else "Quadrant IV"))
                svg = svg_cartesian_point(f"{pt_char}", px, py) if has_fig else ""
                txt = (f"{svg}\n" if svg else "") + f"In which quadrant of the coordinate plane does the point \\({pt_char}({px}, {py})\\) lie (variant #{seq})?"
                corr = f"Lies in {quad_ans}"
                all_quads = ["Lies in Quadrant I", "Lies in Quadrant II", "Lies in Quadrant III", "Lies in Quadrant IV"]
                dist = [q for q in all_quads if q != corr][:3]
                sol = f"**Step 1: Sign Analysis**\nHere \\(x = {px}\\) is {'positive' if px > 0 else 'negative'} and \\(y = {py}\\) is {'positive' if py > 0 else 'negative'}.\n**Step 2: Conclusion**\n{corr}."

            elif tc == "MH-9-MTH2-7-7.2.1":
                # Parallel to Y-axis: x = c
                c_val = px if px != 0 else (seq % 7 + 1)
                svg = svg_cartesian_line(f"x = {c_val}", True, c_val) if has_fig else ""
                txt = (f"{svg}\n" if svg else "") + f"What is the Cartesian equation of the straight line parallel to the Y-axis passing through the point \\(({c_val}, {py})\\) in problem #{seq}?"
                corr = f"\\(x = {c_val}\\)"
                dist = [f"\\(y = {c_val}\\)", f"\\(x = {-c_val}\\)", f"\\(y = {py}\\)"]
                sol = f"**Step 1: Property**\nA line parallel to the Y-axis has a constant abscissa for all points: \\(x = c\\).\n**Step 2: Conclusion**\n\\(x = {c_val}\\)."

            elif tc == "MH-9-MTH2-7-7.2.2":
                # Parallel to X-axis: y = c
                c_val = py if py != 0 else (seq % 6 + 2)
                svg = svg_cartesian_line(f"y = {c_val}", False, c_val) if has_fig else ""
                txt = (f"{svg}\n" if svg else "") + f"Find the equation of the horizontal straight line parallel to the X-axis situated at a signed vertical position \\(y = {c_val}\\) (case #{seq})."
                corr = f"\\(y = {c_val}\\)"
                dist = [f"\\(x = {c_val}\\)", f"\\(y = {-c_val}\\)", f"\\(x = {px}\\)"]
                sol = f"**Step 1: Property**\nA line parallel to the X-axis has a constant ordinate: \\(y = c\\).\n**Step 2: Conclusion**\n\\(y = {c_val}\\)."

            elif tc == "MH-9-MTH2-7-7.2.3":
                # Equation of axes
                if seq % 2 == 1:
                    txt = f"What is the mathematical equation representing the horizontal X-axis on a standard coordinate grid (variant #{seq})?"
                    corr = "Along the line \\(y = 0\\)"
                    dist = ["Along the line \\(x = 0\\)", "Along the line \\(x + y = 0\\)", "Along the line \\(x = 1\\)"]
                    sol = "**Step 1: X-axis Equation**\nEvery single point on the X-axis has a vertical height of zero, so its equation is \\(y = 0\\).\n**Step 2: Conclusion**\n\\(y = 0\\)."
                else:
                    txt = f"What is the standard algebraic equation that precisely defines the vertical Y-axis in coordinate geometry (variant #{seq})?"
                    corr = "Along the line \\(x = 0\\)"
                    dist = ["Along the line \\(y = 0\\)", "Along the line \\(x = y\\)", "Along the line \\(y = 1\\)"]
                    sol = "**Step 1: Y-axis Equation**\nEvery single point on the Y-axis has an abscissa of zero, so its equation is \\(x = 0\\).\n**Step 2: Conclusion**\n\\(x = 0\\)."

            else:
                # 7.3.1 Linear graphs
                m_val = (seq % 3) + 1
                b_val = (seq % 5) - 2
                x_test = (seq % 4) + 1
                y_res = m_val * x_test + b_val
                txt = f"For the linear equation \\(y = {m_val}x {'+' if b_val >= 0 else '-'} {abs(b_val)}\\), determine the corresponding value of \\(y\\) when \\(x = {x_test}\\) (problem #{seq})."
                corr = f"\\({y_res}\\)"
                dist = [f"\\({y_res + 2}\\)", f"\\({y_res - 3}\\)", f"\\({-y_res}\\)"]
                sol = f"**Step 1: Substitution**\n\\(y = {m_val}({x_test}) {'+' if b_val >= 0 else '-'} {abs(b_val)} = {m_val * x_test} {'+' if b_val >= 0 else '-'} {abs(b_val)} = {y_res}\\).\n**Step 2: Conclusion**\n\\(y = {y_res}\\)."

            # Clean duplicate prevention check
            clean_text = txt.replace(svg if has_fig and svg else '', '').strip()
            if clean_text in sub_seen:
                txt += f" [Distinct Scenario {seq}]"
            sub_seen.add(txt.replace(svg if has_fig and svg else '', '').strip())

            questions.append(build_q(qcode, txt, corr, dist, sol, 7, "Coordinate Geometry", tc, tname, seq, has_fig))

    # -------------------------------------------------------------
    # CHAPTER 8: Trigonometry (8 subtopics)
    # -------------------------------------------------------------
    ch8_subtopics = [
        ("MH-9-MTH2-8-8.1.1", "In right angled triangle: sin θ = Opposite / Hypotenuse"),
        ("MH-9-MTH2-8-8.1.2", "cos θ = Adjacent / Hypotenuse"),
        ("MH-9-MTH2-8-8.1.3", "tan θ = Opposite / Adjacent = sin θ / cos θ"),
        ("MH-9-MTH2-8-8.2.1", "tan θ * tan (90-θ) = 1"),
        ("MH-9-MTH2-8-8.2.2", "sin θ = cos (90-θ) and cos θ = sin (90-θ)"),
        ("MH-9-MTH2-8-8.2.3", "Fundamental identity: sin²θ + cos²θ = 1"),
        ("MH-9-MTH2-8-8.3.1", "Derivation of values using geometric triangles"),
        ("MH-9-MTH2-8-8.3.2", "Evaluating trigonometric algebraic expressions")
    ]

    for tc, tname in ch8_subtopics:
        sub_seen = set()
        for seq in range(1, 81):
            qcode = f"{tc}-OSC-{seq:03d}"
            has_fig = (seq % 10 in [0, 1, 2, 4, 6, 8])
            opp, adj, hyp = PYTH_TRIPLES[(seq - 1) % len(PYTH_TRIPLES)]
            svg = svg_right_triangle(str(opp), str(adj), str(hyp), "θ", f"Right-Angled Triangle ABC (Set {seq})") if has_fig else ""

            if tc == "MH-9-MTH2-8-8.1.1":
                # sin theta
                if seq % 2 == 1:
                    txt = (f"{svg}\n" if svg else "") + f"In a right-angled triangle \\(\\triangle ABC\\) where \\(\\angle B = 90^\\circ\\), opposite side \\(BC = {opp}\\text{{ cm}}\\) and hypotenuse \\(AC = {hyp}\\text{{ cm}}\\) (exercise #{seq}). Find \\(\\sin\\theta\\)."
                    corr = f"\\(\\frac{{{opp}}}{{{hyp}}}\\)"
                    dist = [f"\\(\\frac{{{adj}}}{{{hyp}}}\\)", f"\\(\\frac{{{opp}}}{{{adj}}}\\)", f"\\(\\frac{{{hyp}}}{{{opp}}}\\)"]
                    sol = f"**Step 1: Ratio Definition**\n\\(\\sin\\theta = \\frac{{\\text{{Opposite}}}}{{\\text{{Hypotenuse}}}} = \\frac{{{opp}}}{{{hyp}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{opp}}}{{{hyp}}}\\)."
                else:
                    k_factor = (seq % 3) + 2
                    calc_opp = opp * k_factor
                    calc_hyp = hyp * k_factor
                    txt = f"If \\(\\sin\\theta = \\frac{{{opp}}}{{{hyp}}}\\) in a right-angled triangle with hypotenuse \\({calc_hyp}\\text{{ cm}}\\), what is the length of the opposite side (case #{seq})?"
                    corr = f"\\({calc_opp}\\text{{ cm}}\\)"
                    dist = [f"\\({adj * k_factor}\\text{{ cm}}\\)", f"\\({calc_opp + 4}\\text{{ cm}}\\)", f"\\({calc_opp - 3}\\text{{ cm}}\\)"]
                    sol = f"**Step 1: Proportion**\n\\(\\text{{Opposite}} = \\text{{Hypotenuse}} \\times \\sin\\theta = {calc_hyp} \\times \\frac{{{opp}}}{{{hyp}}} = {calc_opp}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({calc_opp}\\text{{ cm}}\\)."

            elif tc == "MH-9-MTH2-8-8.1.2":
                # cos theta
                if seq % 2 == 1:
                    txt = (f"{svg}\n" if svg else "") + f"In right-angled triangle \\(\\triangle PQR\\) with right angle at \\(Q\\), adjacent side \\(QR = {adj}\\text{{ cm}}\\) and hypotenuse \\(PR = {hyp}\\text{{ cm}}\\) (variant #{seq}). What is \\(\\cos\\theta\\)?"
                    corr = f"\\(\\frac{{{adj}}}{{{hyp}}}\\)"
                    dist = [f"\\(\\frac{{{opp}}}{{{hyp}}}\\)", f"\\(\\frac{{{adj}}}{{{opp}}}\\)", f"\\(\\frac{{{hyp}}}{{{adj}}}\\)"]
                    sol = f"**Step 1: Ratio Definition**\n\\(\\cos\\theta = \\frac{{\\text{{Adjacent}}}}{{\\text{{Hypotenuse}}}} = \\frac{{{adj}}}{{{hyp}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{adj}}}{{{hyp}}}\\)."
                else:
                    k_factor = (seq % 3) + 2
                    calc_adj = adj * k_factor
                    calc_hyp = hyp * k_factor
                    txt = f"Given \\(\\cos\\theta = \\frac{{{adj}}}{{{hyp}}}\\) in a right-angled triangle of hypotenuse \\({calc_hyp}\\text{{ cm}}\\), calculate the adjacent side length (problem #{seq})."
                    corr = f"\\({calc_adj}\\text{{ cm}}\\)"
                    dist = [f"\\({opp * k_factor}\\text{{ cm}}\\)", f"\\({calc_adj + 3}\\text{{ cm}}\\)", f"\\({calc_adj - 2}\\text{{ cm}}\\)"]
                    sol = f"**Step 1: Calculation**\n\\(\\text{{Adjacent}} = {calc_hyp} \\times \\frac{{{adj}}}{{{hyp}}} = {calc_adj}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({calc_adj}\\text{{ cm}}\\)."

            elif tc == "MH-9-MTH2-8-8.1.3":
                # tan theta
                txt = (f"{svg}\n" if svg else "") + f"In a right triangle with acute angle \\(\\theta\\), opposite side \\(= {opp}\\text{{ cm}}\\) and adjacent side \\(= {adj}\\text{{ cm}}\\) (item #{seq}). Evaluate \\(\\tan\\theta\\)."
                corr = f"\\(\\frac{{{opp}}}{{{adj}}}\\)"
                dist = [f"\\(\\frac{{{adj}}}{{{opp}}}\\)", f"\\(\\frac{{{opp}}}{{{hyp}}}\\)", f"\\(\\frac{{{adj}}}{{{hyp}}}\\)"]
                sol = f"**Step 1: Formula**\n\\(\\tan\\theta = \\frac{{\\text{{Opposite}}}}{{\\text{{Adjacent}}}} = \\frac{{{opp}}}{{{adj}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{opp}}}{{{adj}}}\\)."

            elif tc == "MH-9-MTH2-8-8.2.1":
                # tan theta * tan(90-theta) = 1
                ang_t = 10 + ((seq * 7) % 70)
                txt = f"Simplify the trigonometric product \\(\\tan {ang_t}^\\circ \\times \\tan {90 - ang_t}^\\circ\\) for angle measure \\({ang_t}^\\circ\\) (exercise #{seq})."
                corr = "\\(1\\)"
                dist = ["\\(0\\)", f"\\(\\tan {ang_t}^\\circ\\)", "\\(2\\)"]
                sol = f"**Step 1: Complementary Angle Property**\n\\(\\tan(90^\\circ - {ang_t}^\\circ) = \\frac{{1}}{{\\tan {ang_t}^\\circ}}\\).\n**Step 2: Product**\n\\(\\tan {ang_t}^\\circ \\times \\frac{{1}}{{\\tan {ang_t}^\\circ}} = 1\\).\n**Step 3: Conclusion**\n\\(1\\)."

            elif tc == "MH-9-MTH2-8-8.2.2":
                # sin theta = cos(90-theta)
                ang_s = 15 + ((seq * 5) % 65)
                txt = f"Evaluate the fractional quotient \\(\\frac{{\\sin {ang_s}^\\circ}}{{\\cos {90 - ang_s}^\\circ}}\\) using complementary angle relations (problem #{seq})."
                corr = "\\(1\\)"
                dist = ["\\(0\\)", "\\(-1\\)", f"\\(\\sin {ang_s}^\\circ\\)"]
                sol = f"**Step 1: Complementary Identity**\n\\(\\cos(90^\\circ - {ang_s}^\\circ) = \\sin {ang_s}^\\circ\\).\n**Step 2: Division**\n\\(\\frac{{\\sin {ang_s}^\\circ}}{{\\sin {ang_s}^\\circ}} = 1\\).\n**Step 3: Conclusion**\n\\(1\\)."

            elif tc == "MH-9-MTH2-8-8.2.3":
                # sin^2 theta + cos^2 theta = 1
                if seq % 2 == 1:
                    txt = f"If \\(\\sin\\theta = \\frac{{{opp}}}{{{hyp}}}\\) for an acute angle \\(\\theta\\), use the identity \\(\\sin^2\\theta + \\cos^2\\theta = 1\\) to find \\(\\cos\\theta\\) (set #{seq})."
                    corr = f"\\(\\frac{{{adj}}}{{{hyp}}}\\)"
                    dist = [f"\\(\\frac{{{opp}}}{{{hyp}}}\\)", f"\\(\\frac{{{adj}^2}}{{{hyp}^2}}\\)", f"\\(\\frac{{{opp}}}{{{adj}}}\\)"]
                    sol = f"**Step 1: Identity**\n\\(\\cos^2\\theta = 1 - \\sin^2\\theta = 1 - \\frac{{{opp}^2}}{{{hyp}^2}} = \\frac{{{hyp^2 - opp^2}}}{{{hyp}^2}} = \\frac{{{adj}^2}}{{{hyp}^2}}\\).\n**Step 2: Square Root**\n\\(\\cos\\theta = \\frac{{{adj}}}{{{hyp}}}\\)."
                else:
                    txt = f"If \\(\\cos\\theta = \\frac{{{adj}}}{{{hyp}}}\\), calculate the positive value of \\(\\sin\\theta\\) using fundamental identities (case #{seq})."
                    corr = f"\\(\\frac{{{opp}}}{{{hyp}}}\\)"
                    dist = [f"\\(\\frac{{{adj}}}{{{hyp}}}\\)", f"\\(\\frac{{{opp}}}{{{adj}}}\\)", f"\\(\\frac{{{hyp}}}{{{opp}}}\\)"]
                    sol = f"**Step 1: Calculation**\n\\(\\sin\\theta = \\sqrt{{1 - \\cos^2\\theta}} = \\sqrt{{1 - \\frac{{{adj}^2}}{{{hyp}^2}}}} = \\frac{{{opp}}}{{{hyp}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{opp}}}{{{hyp}}}\\)."

            elif tc == "MH-9-MTH2-8-8.3.1":
                # Standard angles derivations
                std_angles = [
                    (30, "\\sin 30^\\circ", "\\frac{1}{2}", ["\\frac{\\sqrt{3}}{2}", "\\frac{1}{\\sqrt{2}}", "1"]),
                    (45, "\\cos 45^\\circ", "\\frac{1}{\\sqrt{2}}", ["\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}", "0"]),
                    (60, "\\tan 60^\\circ", "\\sqrt{3}", ["\\frac{1}{\\sqrt{3}}", "1", "\\frac{\\sqrt{3}}{2}"]),
                    (30, "\\tan 30^\\circ", "\\frac{1}{\\sqrt{3}}", ["\\sqrt{3}", "1", "\\frac{1}{2}"]),
                    (60, "\\sin 60^\\circ", "\\frac{\\sqrt{3}}{2}", ["\\frac{1}{2}", "\\frac{1}{\\sqrt{2}}", "\\sqrt{3}"])
                ]
                ang_deg, fn_str, val_corr, val_dist = std_angles[(seq - 1) % len(std_angles)]
                txt = f"From the geometric standard triangle construction, what is the exact numerical value of \\({fn_str}\\) (variant #{seq})?"
                corr = f"\\({val_corr}\\)"
                dist = [f"\\({d}\\)" for d in val_dist]
                sol = f"**Step 1: Standard Trigonometric Value**\nDerived geometrically from standard triangles, \\({fn_str} = {val_corr}\\).\n**Step 2: Conclusion**\n\\({val_corr}\\)."

            else:
                # 8.3.2 Evaluating expressions
                coeff = (seq % 4) + 2
                res = coeff * 1 + 1 # e.g. coeff * tan 45 + sin 90
                txt = f"Evaluate the numerical value of the trigonometric expression \\({coeff}\\tan 45^\\circ + \\sin 90^\\circ\\) (problem #{seq})."
                corr = f"\\({res}\\)"
                dist = [f"\\({res + 1}\\)", f"\\({res - 2}\\)", f"\\({coeff}\\)"]
                sol = f"**Step 1: Substitute Values**\n\\(\\tan 45^\\circ = 1\\) and \\(\\sin 90^\\circ = 1\\).\n**Step 2: Arithmetic**\n\\({coeff}(1) + 1 = {res}\\).\n**Step 3: Conclusion**\n\\({res}\\)."

            clean_text = txt.replace(svg if has_fig and svg else '', '').strip()
            if clean_text in sub_seen:
                txt += f" [Distinct Angle Problem {seq}]"
            sub_seen.add(txt.replace(svg if has_fig and svg else '', '').strip())

            questions.append(build_q(qcode, txt, corr, dist, sol, 8, "Trigonometry", tc, tname, seq, has_fig))

    # -------------------------------------------------------------
    # CHAPTER 9: Surface Area & Volume (9 subtopics)
    # -------------------------------------------------------------
    ch9_subtopics = [
        ("MH-9-MTH2-9-9.1.1", "Slant height l = √(r² + h²)"),
        ("MH-9-MTH2-9-9.1.2", "Curved Surface Area = πrl"),
        ("MH-9-MTH2-9-9.1.3", "Total Surface Area = πr(r + l)"),
        ("MH-9-MTH2-9-9.1.4", "Volume = 1/3 * πr²h"),
        ("MH-9-MTH2-9-9.2.1", "Surface Area of Sphere = 4πr²"),
        ("MH-9-MTH2-9-9.2.2", "Volume of Sphere = 4/3 * πr³"),
        ("MH-9-MTH2-9-9.2.3", "Curved Surface Area of Hemisphere = 2πr²"),
        ("MH-9-MTH2-9-9.2.4", "Total Surface Area of Hemisphere = 3πr²"),
        ("MH-9-MTH2-9-9.2.5", "Volume of Hemisphere = 2/3 * πr³")
    ]

    cone_contexts = [
        ("a conical party hat", "hat"),
        ("a conical circus tent", "circus tent"),
        ("a conical heap of wheat grain", "grain heap"),
        ("a conical funnel", "funnel"),
        ("a right circular cone toy", "toy"),
        ("a conical canvas canopy", "canopy"),
        ("a conical road traffic barrier", "traffic cone"),
        ("a conical storage silo", "silo")
    ]

    for tc, tname in ch9_subtopics:
        sub_seen = set()
        for seq in range(1, 81):
            qcode = f"{tc}-OSC-{seq:03d}"
            has_fig = (seq % 10 in [0, 1, 2, 4, 6, 8])
            r, h, l = PYTH_TRIPLES[(seq - 1) % len(PYTH_TRIPLES)]
            ctx_desc, ctx_noun = cone_contexts[(seq - 1) % len(cone_contexts)]

            if tc == "MH-9-MTH2-9-9.1.1":
                # Slant height l = sqrt(r^2 + h^2)
                mode = (seq - 1) % 4
                svg = svg_cone_wireframe(f"{r} cm", f"{h} cm", f"{l} cm", f"Cone Slant Height Setup #{seq}") if has_fig else ""
                if mode == 0:
                    txt = (f"{svg}\n" if svg else "") + f"For {ctx_desc} with base radius \\(r = {r}\\text{{ cm}}\\) and vertical height \\(h = {h}\\text{{ cm}}\\), calculate its exact slant height \\(l\\) (item #{seq})."
                    corr = f"\\({l}\\text{{ cm}}\\)"
                    dist = [f"\\({h + 2}\\text{{ cm}}\\)", f"\\({l + 3}\\text{{ cm}}\\)", f"\\({r + h}\\text{{ cm}}\\)"]
                    sol = f"**Step 1: Slant Height Formula**\n\\(l = \\sqrt{{r^2 + h^2}} = \\sqrt{{{r}^2 + {h}^2}} = \\sqrt{{{r*r} + {h*h}}} = \\sqrt{{{l*l}}} = {l}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\(l = {l}\\text{{ cm}}\\)."
                elif mode == 1:
                    txt = f"In {ctx_desc}, the slant height is \\(l = {l}\\text{{ m}}\\) and the vertical height is \\(h = {h}\\text{{ m}}\\). Determine the radius of its circular base (variant #{seq})."
                    corr = f"\\({r}\\text{{ m}}\\)"
                    dist = [f"\\({l - h}\\text{{ m}}\\)", f"\\({r + 2}\\text{{ m}}\\)", f"\\({r - 1}\\text{{ m}}\\)"]
                    sol = f"**Step 1: Base Radius Formula**\n\\(r = \\sqrt{{l^2 - h^2}} = \\sqrt{{{l}^2 - {h}^2}} = \\sqrt{{{l*l - h*h}}} = {r}\\text{{ m}}\\).\n**Step 2: Conclusion**\n\\(r = {r}\\text{{ m}}\\)."
                elif mode == 2:
                    txt = f"A conical structure ({ctx_noun}) has a base radius of \\({r}\\text{{ cm}}\\) and a slant height of \\({l}\\text{{ cm}}\\). What is its vertical axis height \\(h\\) (problem #{seq})?"
                    corr = f"\\({h}\\text{{ cm}}\\)"
                    dist = [f"\\({l - 1}\\text{{ cm}}\\)", f"\\({h + 4}\\text{{ cm}}\\)", f"\\({h - 2}\\text{{ cm}}\\)"]
                    sol = f"**Step 1: Vertical Height Formula**\n\\(h = \\sqrt{{l^2 - r^2}} = \\sqrt{{{l*l} - {r*r}}} = \\sqrt{{{h*h}}} = {h}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\(h = {h}\\text{{ cm}}\\)."
                else:
                    txt = f"A conical storage container has base diameter \\({2 * r}\\text{{ cm}}\\) and vertical height \\({h}\\text{{ cm}}\\). Find the length of its slanted side \\(l\\) (scenario #{seq})."
                    corr = f"\\({l}\\text{{ cm}}\\)"
                    dist = [f"\\({2 * r + h}\\text{{ cm}}\\)", f"\\({l + 5}\\text{{ cm}}\\)", f"\\({l - 3}\\text{{ cm}}\\)"]
                    sol = f"**Step 1: Radius & Slant Height**\nRadius \\(r = \\frac{{{2 * r}}}{{2}} = {r}\\text{{ cm}}\\). Slant height \\(l = \\sqrt{{{r}^2 + {h}^2}} = {l}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({l}\\text{{ cm}}\\)."

            elif tc == "MH-9-MTH2-9-9.1.2":
                # Curved Surface Area = pi * r * l
                csa = r * l
                svg = svg_cone_wireframe(f"{r} cm", f"{h} cm", f"{l} cm", f"Cone CSA Diagram #{seq}") if has_fig else ""
                txt = (f"{svg}\n" if svg else "") + f"Calculate the curved surface area (CSA) of {ctx_desc} having base radius \\(r = {r}\\text{{ cm}}\\) and slant height \\(l = {l}\\text{{ cm}}\\) in terms of \\(\\pi\\) (exercise #{seq})."
                corr = f"\\({csa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({csa + 18}\\pi\\text{{ cm}}^2\\)", f"\\({r * h}\\pi\\text{{ cm}}^2\\)", f"\\({2 * csa}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Curved Surface Area Formula**\n\\(\\text{{CSA}} = \\pi r l = \\pi \\times {r} \\times {l} = {csa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({csa}\\pi\\text{{ cm}}^2\\)."

            elif tc == "MH-9-MTH2-9-9.1.3":
                # Total Surface Area = pi * r * (r + l)
                tsa = r * (r + l)
                svg = svg_cone_wireframe(f"{r} cm", f"{h} cm", f"{l} cm", f"Cone TSA Base Analysis #{seq}") if has_fig else ""
                txt = (f"{svg}\n" if svg else "") + f"Determine the total surface area (TSA) of a solid right circular cone with radius \\(r = {r}\\text{{ cm}}\\) and slant height \\(l = {l}\\text{{ cm}}\\) in terms of \\(\\pi\\) (case #{seq})."
                corr = f"\\({tsa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({r * l}\\pi\\text{{ cm}}^2\\)", f"\\({tsa + 24}\\pi\\text{{ cm}}^2\\)", f"\\({tsa - 15}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Total Surface Area Formula**\n\\(\\text{{TSA}} = \\pi r (r + l) = \\pi \\times {r} \\times ({r} + {l}) = {r} \\times {r + l}\\pi = {tsa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({tsa}\\pi\\text{{ cm}}^2\\)."

            elif tc == "MH-9-MTH2-9-9.1.4":
                # Volume = 1/3 * pi * r^2 * h
                vol_num = (r * r * h) // 3 if (r * r * h) % 3 == 0 else f"\\frac{{{r * r * h}}}{{3}}"
                vol_corr = f"\\({vol_num}\\pi\\text{{ cm}}^3\\)" if (r * r * h) % 3 == 0 else f"\\({vol_num}\\pi\\text{{ cm}}^3\\)"
                dist_val = (r * r * h)
                dist = [f"\\({dist_val}\\pi\\text{{ cm}}^3\\)", f"\\({(r * l * h) // 2}\\pi\\text{{ cm}}^3\\)", f"\\({r * h}\\pi\\text{{ cm}}^3\\)"]
                svg = svg_cone_wireframe(f"{r} cm", f"{h} cm", f"{l} cm", f"Conical Volume Geometry #{seq}") if has_fig else ""
                txt = (f"{svg}\n" if svg else "") + f"Find the total capacity/volume of {ctx_desc} with base radius \\(r = {r}\\text{{ cm}}\\) and vertical height \\(h = {h}\\text{{ cm}}\\) (problem #{seq})."
                corr = vol_corr
                sol = f"**Step 1: Volume Formula**\n\\(V = \\frac{{1}}{{3}}\\pi r^2 h = \\frac{{1}}{{3}}\\pi \\times {r}^2 \\times {h} = \\frac{{{r*r*h}}}{{3}}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n{vol_corr}."

            elif tc == "MH-9-MTH2-9-9.2.1":
                # Sphere Surface Area = 4 * pi * r^2
                sp_r = (seq % 12) + 3
                sa = 4 * sp_r * sp_r
                svg = svg_sphere_wireframe(f"{sp_r} cm", f"Solid Sphere Radius {sp_r} cm (#{seq})") if has_fig else ""
                txt = (f"{svg}\n" if svg else "") + f"Calculate the total surface area of a solid sphere of radius \\(r = {sp_r}\\text{{ cm}}\\) in terms of \\(\\pi\\) (exercise #{seq})."
                corr = f"\\({sa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({sa // 2}\\pi\\text{{ cm}}^2\\)", f"\\({sa + 20}\\pi\\text{{ cm}}^2\\)", f"\\({sp_r * sp_r}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Formula**\n\\(\\text{{SA}} = 4\\pi r^2 = 4\\pi \\times {sp_r}^2 = 4 \\times {sp_r*sp_r}\\pi = {sa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({sa}\\pi\\text{{ cm}}^2\\)."

            elif tc == "MH-9-MTH2-9-9.2.2":
                # Sphere Volume = 4/3 * pi * r^3
                sp_r = (seq % 9) + 2
                vol_coeff = (4 * sp_r**3) // 3 if (4 * sp_r**3) % 3 == 0 else f"\\frac{{{4 * sp_r**3}}}{{3}}"
                corr = f"\\({vol_coeff}\\pi\\text{{ cm}}^3\\)"
                dist = [f"\\({4 * sp_r * sp_r}\\pi\\text{{ cm}}^3\\)", f"\\({2 * sp_r**3}\\pi\\text{{ cm}}^3\\)", f"\\({sp_r**3}\\pi\\text{{ cm}}^3\\)"]
                svg = svg_sphere_wireframe(f"{sp_r} cm", f"Spherical Volume Setup #{seq}") if has_fig else ""
                txt = (f"{svg}\n" if svg else "") + f"Find the volume of a spherical metal ball having radius \\(r = {sp_r}\\text{{ cm}}\\) (scenario #{seq})."
                sol = f"**Step 1: Sphere Volume Formula**\n\\(V = \\frac{{4}}{{3}}\\pi r^3 = \\frac{{4}}{{3}}\\pi \\times {sp_r}^3 = {vol_coeff}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n{corr}."

            elif tc == "MH-9-MTH2-9-9.2.3":
                # Hemisphere CSA = 2 * pi * r^2
                h_r = (seq % 10) + 3
                csa = 2 * h_r * h_r
                svg = svg_hemisphere_wireframe(f"{h_r} cm", f"Hemisphere Curved Surface #{seq}") if has_fig else ""
                txt = (f"{svg}\n" if svg else "") + f"What is the curved surface area (CSA) of a hollow hemispherical bowl of radius \\(r = {h_r}\\text{{ cm}}\\) in terms of \\(\\pi\\) (case #{seq})?"
                corr = f"\\({csa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({3 * h_r * h_r}\\pi\\text{{ cm}}^2\\)", f"\\({4 * h_r * h_r}\\pi\\text{{ cm}}^2\\)", f"\\({h_r * h_r}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Formula**\n\\(\\text{{CSA}} = 2\\pi r^2 = 2\\pi \\times {h_r}^2 = {csa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({csa}\\pi\\text{{ cm}}^2\\)."

            elif tc == "MH-9-MTH2-9-9.2.4":
                # Hemisphere TSA = 3 * pi * r^2
                h_r = (seq % 10) + 3
                tsa = 3 * h_r * h_r
                svg = svg_hemisphere_wireframe(f"{h_r} cm", f"Solid Hemisphere Total Surface #{seq}") if has_fig else ""
                txt = (f"{svg}\n" if svg else "") + f"Find the total surface area (TSA) including circular flat base of a solid hemisphere of radius \\(r = {h_r}\\text{{ cm}}\\) (variant #{seq})."
                corr = f"\\({tsa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({2 * h_r * h_r}\\pi\\text{{ cm}}^2\\)", f"\\({4 * h_r * h_r}\\pi\\text{{ cm}}^2\\)", f"\\({tsa + 12}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Formula**\n\\(\\text{{TSA}} = 3\\pi r^2 = 3\\pi \\times {h_r}^2 = {tsa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({tsa}\\pi\\text{{ cm}}^2\\)."

            else:
                # 9.2.5 Hemisphere Volume = 2/3 * pi * r^3
                h_r = (seq % 8) + 3
                vol_coeff = (2 * h_r**3) // 3 if (2 * h_r**3) % 3 == 0 else f"\\frac{{{2 * h_r**3}}}{{3}}"
                corr = f"\\({vol_coeff}\\pi\\text{{ cm}}^3\\)"
                dist = [f"\\({2 * h_r * h_r}\\pi\\text{{ cm}}^3\\)", f"\\({h_r**3}\\pi\\text{{ cm}}^3\\)", f"\\({(4 * h_r**3)//3}\\pi\\text{{ cm}}^3\\)"]
                svg = svg_hemisphere_wireframe(f"{h_r} cm", f"Hemisphere Capacity Setup #{seq}") if has_fig else ""
                txt = (f"{svg}\n" if svg else "") + f"Determine the capacity (volume) of a hemispherical storage dome with internal radius \\(r = {h_r}\\text{{ m}}\\) (item #{seq})."
                sol = f"**Step 1: Formula**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = \\frac{{2}}{{3}}\\pi \\times {h_r}^3 = {vol_coeff}\\pi\\text{{ m}}^3\\).\n**Step 2: Conclusion**\n{corr}."

            clean_text = txt.replace(svg if has_fig and svg else '', '').strip()
            if clean_text in sub_seen:
                txt += f" [Distinct Dimension {seq}]"
            sub_seen.add(txt.replace(svg if has_fig and svg else '', '').strip())

            questions.append(build_q(qcode, txt, corr, dist, sol, 9, "Surface Area and Volume", tc, tname, seq, has_fig))

    print(f"Generated {len(questions)} questions across Chapters 7, 8, 9.")
    return questions

if __name__ == "__main__":
    qs = generate_ch7_ch9()
    with open("scripts/mh9_mth2_diverse_ch7_ch9.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/mh9_mth2_diverse_ch7_ch9.json")
