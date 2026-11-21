# scripts/generate_flawless_mth2_ch7.py
import json
import math

SEQS_80 = [101 + i for i in range(40)] + [201 + i for i in range(20)] + [301 + i for i in range(20)]

def make_opts(corr, dist):
    opts = [{"id": "A", "text": corr, "isCorrect": True}]
    letters = ["B", "C", "D"]
    seen = {corr}
    clean_dist = []
    for d in dist:
        if d not in seen and len(clean_dist) < 3:
            seen.add(d)
            clean_dist.append(d)
    
    counter = 1
    while len(clean_dist) < 3:
        fallback = f"{corr} (Alt {counter})"
        if fallback not in seen:
            seen.add(fallback)
            clean_dist.append(fallback)
        counter += 1
        
    for idx, d in enumerate(clean_dist):
        opts.append({"id": letters[idx], "text": d, "isCorrect": False})
        
    # Deterministic rotation based on length
    shift = len(corr) % 4
    rotated = opts[shift:] + opts[:shift]
    for idx, o in enumerate(rotated):
        o["id"] = ["A", "B", "C", "D"][idx]
    return rotated

def build_q(qcode, text, corr, dist, sol, tc, tname, seq, has_fig, diff="medium"):
    vault = 'exam' if 101 <= seq <= 140 else ('practice' if 201 <= seq <= 220 else 'foundation')
    marks = 4 if vault in ['exam', 'practice'] else 2
    opts = make_opts(corr, dist)
    corr_letter = next(o['id'] for o in opts if o['isCorrect'])

    return {
        "questionCode": qcode,
        "boardCode": "MH",
        "board": "Maharashtra Board",
        "class": "9",
        "subjectCode": "MTH2",
        "subject": "Mathematics Part - 2 (Geometry)",
        "chapterNumber": 7,
        "chapter": "Coordinate Geometry",
        "topicCode": tc,
        "topic": tname,
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
        "requiresFigure": has_fig,
        "createdAt": "2026-11-21T13:48:00.000Z",
        "updatedAt": "2026-11-21T13:48:00.000Z",
        "options": opts,
        "correctAnswer": corr_letter,
        "solution": sol,
        "text": text
    }

def svg_cartesian_point(pt, x, y, title):
    # Map (-8..8, -8..8) to SVG viewbox 0..240
    cx = 120 + x * 12
    cy = 120 - y * 12
    return (
        f'<svg width="240" height="240" viewBox="0 0 240 240" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a;border-radius:8px;display:block;margin:12px auto;">'
        f'<defs><pattern id="grid_{pt}_{x}_{y}" width="12" height="12" patternUnits="userSpaceOnUse">'
        f'<path d="M 12 0 L 0 0 0 12" fill="none" stroke="#1e293b" stroke-width="0.5"/>'
        f'</pattern></defs>'
        f'<rect width="240" height="240" fill="url(#grid_{pt}_{x}_{y})"/>'
        f'<line x1="0" y1="120" x2="240" y2="120" stroke="#64748b" stroke-width="1.5"/>'
        f'<line x1="120" y1="0" x2="120" y2="240" stroke="#64748b" stroke-width="1.5"/>'
        f'<text x="230" y="115" fill="#94a3b8" font-size="10" font-family="sans-serif">X</text>'
        f'<text x="125" y="15" fill="#94a3b8" font-size="10" font-family="sans-serif">Y</text>'
        f'<text x="123" y="133" fill="#94a3b8" font-size="9" font-family="sans-serif">O</text>'
        f'<line x1="{cx}" y1="120" x2="{cx}" y2="{cy}" stroke="#38bdf8" stroke-dasharray="2,2" stroke-width="1"/>'
        f'<line x1="120" y1="{cy}" x2="{cx}" y2="{cy}" stroke="#38bdf8" stroke-dasharray="2,2" stroke-width="1"/>'
        f'<circle cx="{cx}" cy="{cy}" r="4" fill="#f59e0b"/>'
        f'<text x="{cx + 6}" y="{cy - 6}" fill="#f59e0b" font-size="11" font-weight="bold" font-family="sans-serif">{pt}({x}, {y})</text>'
        f'<text x="10" y="230" fill="#38bdf8" font-size="10" font-family="sans-serif">{title}</text>'
        f'</svg>'
    )

def svg_parallel_line(eq, is_vertical, val, title):
    coord = 120 + val * 12 if is_vertical else 120 - val * 12
    line_svg = (
        f'<line x1="{coord}" y1="10" x2="{coord}" y2="230" stroke="#f43f5e" stroke-width="2"/>'
        if is_vertical else
        f'<line x1="10" y1="{coord}" x2="230" y2="{coord}" stroke="#f43f5e" stroke-width="2"/>'
    )
    lbl_x = coord + 4 if is_vertical else 15
    lbl_y = 25 if is_vertical else coord - 5
    return (
        f'<svg width="240" height="240" viewBox="0 0 240 240" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a;border-radius:8px;display:block;margin:12px auto;">'
        f'<line x1="0" y1="120" x2="240" y2="120" stroke="#64748b" stroke-width="1.5"/>'
        f'<line x1="120" y1="0" x2="120" y2="240" stroke="#64748b" stroke-width="1.5"/>'
        f'{line_svg}'
        f'<text x="{lbl_x}" y="{lbl_y}" fill="#f43f5e" font-size="11" font-weight="bold" font-family="sans-serif">{eq}</text>'
        f'<text x="10" y="230" fill="#38bdf8" font-size="10" font-family="sans-serif">{title}</text>'
        f'</svg>'
    )

COORDS_80 = []
for x in [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for y in [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7]:
        COORDS_80.append((x, y))
        if len(COORDS_80) >= 80:
            break
    if len(COORDS_80) >= 80:
        break

PTS_80 = [f"P_{{{i+1}}}" if i >= 26 else chr(65 + i) for i in range(80)]

# ------------------------------------------------------------------------------
# 7.1.1: X-axis, Y-axis, Origin (0,0)
# ------------------------------------------------------------------------------
def generate_7_1_1():
    tc = "MH-9-MTH2-7-7.1.1"
    tname = "X-axis, Y-axis, Origin (0,0)"
    qs = []
    
    for idx, seq in enumerate(SEQS_80):
        px, py = COORDS_80[idx]
        pt = PTS_80[idx]
        has_fig = (idx % 4 != 0)
        svg = svg_cartesian_point(pt, px, py, f"Point {pt}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        mode = idx % 8
        if mode == 0:
            # Origin variations
            variants = [
                ("What are the coordinates of the origin where the coordinate axes cross each other?", "\\((0, 0)\\)", ["\\((1, 1)\\)", "\\((0, 1)\\)", "\\((1, 0)\\)"]),
                ("If origin \\(O\\) has coordinates \\((a, b)\\), compute the value of \\(a^2 + b^2\\).", "0", ["1", "2", "-1"]),
                ("In a 2D coordinate system, what is the distance of the origin from the horizontal axis?", "0 units", ["1 unit", "2 units", "Undefined"]),
                ("What is the product of the x-coordinate and y-coordinate of the origin \\(O\\)?", "0", ["1", "-1", "Cannot be determined"]),
                ("The reference point from which all coordinate measurements originate is termed the:", "Origin", ["Y-intercept", "X-intercept", "Abscissa"]),
                ("If a point lies at the intersection of lines \\(x = 0\\) and \\(y = 0\\), its coordinates are:", "\\((0, 0)\\)", ["\\((0, 1)\\)", "\\((1, 0)\\)", "\\((-1, -1)\\)"]),
                ("A particle located at origin \\(O\\) is shifted 0 units horizontally and 0 units vertically. Its new position is:", "\\((0, 0)\\)", ["\\((1, 0)\\)", "\\((0, 1)\\)", "\\((0, -1)\\)"]),
                ("What is the sum of abscissa and ordinate for the point of origin?", "0", ["1", "2", "-2"]),
                ("Which ordered pair designates the zero reference point on graph paper?", "\\((0, 0)\\)", ["\\((0, 2)\\)", "\\((2, 0)\\)", "\\((1, -1)\\)"]),
                ("The abscissa of the origin point on the Cartesian plane is equal to:", "0", ["1", "-1", "Infinity"])
            ]
            q_txt, corr, dist = variants[(idx // 8) % len(variants)]
            txt = prefix + q_txt
            sol = f"**Step 1: Concept**\nThe origin \\(O\\) is defined as \\((0, 0)\\) where both coordinate axes intersect.\n**Step 2: Conclusion**\n{corr}."
        elif mode == 1:
            # Point on X-axis (px, 0)
            txt = prefix + f"Point \\({pt}({px}, k)\\) lies on the X-axis. Find the exact numerical value of \\(k\\)."
            corr = "0"
            dist = [f"{px}", f"{-px}", "1"]
            sol = f"**Step 1: Property of X-axis**\nEvery point on the X-axis has a y-coordinate equal to 0.\nTherefore, \\(k = 0\\).\n**Step 2: Conclusion**\n0."
        elif mode == 2:
            # Point on Y-axis (0, py)
            txt = prefix + f"Point \\({pt}(m, {py})\\) is situated on the vertical Y-axis. What must be the value of \\(m\\)?"
            corr = "0"
            dist = [f"{py}", f"{-py}", "1"]
            sol = f"**Step 1: Property of Y-axis**\nEvery point lying on the Y-axis has an x-coordinate of 0.\nHence, \\(m = 0\\).\n**Step 2: Conclusion**\n0."
        elif mode == 3:
            # Abscissa of (px, py)
            txt = prefix + f"State the abscissa of the point \\({pt}({px}, {py})\\) plotted in the Cartesian plane."
            corr = f"{px}"
            dist = [f"{py}", f"{-px}", f"{px + 1}"]
            sol = f"**Step 1: Definition**\nThe abscissa of a point is its x-coordinate.\nFor \\({pt}({px}, {py})\\), the x-coordinate is {px}.\n**Step 2: Conclusion**\n{px}."
        elif mode == 4:
            # Ordinate of (px, py)
            txt = prefix + f"What is the ordinate of the ordered pair representing point \\({pt}({px}, {py})\\)?"
            corr = f"{py}"
            dist = [f"{px}", f"{-py}", f"{py - 1}"]
            sol = f"**Step 1: Definition**\nThe ordinate of a point is its y-coordinate.\nFor \\({pt}({px}, {py})\\), the y-coordinate is {py}.\n**Step 2: Conclusion**\n{py}."
        elif mode == 5:
            # Perpendicular distance from X-axis
            d_x = abs(py)
            txt = prefix + f"Calculate the perpendicular distance of the point \\({pt}({px}, {py})\\) from the horizontal X-axis."
            corr = f"{d_x} units"
            dist = [f"{abs(px)} units", f"{d_x + 2} units", f"{d_x + 1} units"]
            sol = f"**Step 1: Distance Formula**\nPerpendicular distance from X-axis \\(= |y| = |{py}| = {d_x}\\) units.\n**Step 2: Conclusion**\n{d_x} units."
        elif mode == 6:
            # Perpendicular distance from Y-axis
            d_y = abs(px)
            txt = prefix + f"Find the perpendicular distance from the vertical Y-axis to the point \\({pt}({px}, {py})\\)."
            corr = f"{d_y} units"
            dist = [f"{abs(py)} units", f"{d_y + 3} units", f"{d_y + 1} units"]
            sol = f"**Step 1: Distance Formula**\nPerpendicular distance from Y-axis \\(= |x| = |{px}| = {d_y}\\) units.\n**Step 2: Conclusion**\n{d_y} units."
        else:
            # Distance from origin
            d_sq = px*px + py*py
            is_perf = math.isqrt(d_sq)**2 == d_sq
            dist_str = f"{math.isqrt(d_sq)}" if is_perf else f"\\sqrt{{{d_sq}}}"
            txt = prefix + f"Determine the straight-line distance of the point \\({pt}({px}, {py})\\) from the origin \\(O(0, 0)\\)."
            corr = f"{dist_str} units"
            dist = [f"{abs(px) + abs(py)} units", f"\\sqrt{{{d_sq + 5}}} units", f"{abs(px)} units"]
            sol = f"**Step 1: Distance from Origin**\n\\(d = \\sqrt{{x^2 + y^2}} = \\sqrt{{{px}^2 + ({py})^2}} = \\sqrt{{{px*px} + {py*py}}} = {dist_str}\\) units.\n**Step 2: Conclusion**\n{dist_str} units."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

# ------------------------------------------------------------------------------
# 7.1.2: Plotting points in all four quadrants
# ------------------------------------------------------------------------------
def generate_7_1_2():
    tc = "MH-9-MTH2-7-7.1.2"
    tname = "Plotting points in all four quadrants"
    qs = []
    
    for idx, seq in enumerate(SEQS_80):
        raw_x, raw_y = COORDS_80[idx]
        pt = PTS_80[idx]
        has_fig = (idx % 4 != 0)
        
        # Determine quadrant target: 0 -> Q1, 1 -> Q2, 2 -> Q3, 3 -> Q4
        quad_target = idx % 4
        if quad_target == 0:
            px, py = abs(raw_x), abs(raw_y)
            quad_name = "Quadrant I"
            signs = "(+, +)"
            desc = "both x and y are positive"
            dist_quads = ["Quadrant II", "Quadrant IV", "Quadrant III"]
        elif quad_target == 1:
            px, py = -abs(raw_x), abs(raw_y)
            quad_name = "Quadrant II"
            signs = "(-, +)"
            desc = "x is negative and y is positive"
            dist_quads = ["Quadrant I", "Quadrant III", "Quadrant IV"]
        elif quad_target == 2:
            px, py = -abs(raw_x), -abs(raw_y)
            quad_name = "Quadrant III"
            signs = "(-, -)"
            desc = "both x and y are negative"
            dist_quads = ["Quadrant II", "Quadrant IV", "Quadrant I"]
        else:
            px, py = abs(raw_x), -abs(raw_y)
            quad_name = "Quadrant IV"
            signs = "(+, -)"
            desc = "x is positive and y is negative"
            dist_quads = ["Quadrant I", "Quadrant II", "Quadrant III"]
            
        svg = svg_cartesian_point(pt, px, py, f"Quadrant Analysis #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        archetype = (idx // 4) % 10
        if archetype == 0:
            txt = prefix + f"In which quadrant of the Cartesian plane does the point \\({pt}({px}, {py})\\) lie?"
            corr = quad_name
            dist = dist_quads
            sol = f"**Step 1: Sign Examination**\nHere \\(x = {px}\\) and \\(y = {py}\\). Since {desc}, the point lies in {quad_name}.\n**Step 2: Conclusion**\n{quad_name}."
        elif archetype == 1:
            txt = prefix + f"If a point \\({pt}\\) has coordinates with signs \\({signs}\\), identify its quadrant."
            corr = quad_name
            dist = dist_quads
            sol = f"**Step 1: Quadrant Signs**\nThe sign combination \\({signs}\\) uniquely corresponds to {quad_name}.\n**Step 2: Conclusion**\n{quad_name}."
        elif archetype == 2:
            txt = prefix + f"Point \\({pt}({px}, {py})\\) is plotted by moving {abs(px)} units along the horizontal axis and {abs(py)} units along the vertical axis. Which quadrant contains \\({pt}\\)?"
            corr = quad_name
            dist = dist_quads
            sol = f"**Step 1: Coordinate Signs**\n\\(x = {px}\\) and \\(y = {py}\\), which means {desc}.\n**Step 2: Conclusion**\n{quad_name}."
        elif archetype == 3:
            txt = prefix + f"What is the sign configuration of any point situated in {quad_name}?"
            corr = signs
            all_signs = ["(+, +)", "(-, +)", "(-, -)", "(+, -)"]
            dist = [s for s in all_signs if s != signs][:3]
            sol = f"**Step 1: Definition**\nIn {quad_name}, {desc}, so signs are \\({signs}\\).\n**Step 2: Conclusion**\n\\({signs}\\)."
        elif archetype == 4:
            txt = prefix + f"For point \\({pt}({px}, {py})\\), what is the sign of the product of its abscissa and ordinate \\(xy\\)?"
            prod = px * py
            corr = "Positive \\(> 0\\)" if prod > 0 else "Negative \\(< 0\\)"
            dist = ["Negative \\(< 0\\)" if prod > 0 else "Positive \\(> 0\\)", "Zero", "Undefined"]
            sol = f"**Step 1: Product Calculation**\n\\(xy = ({px}) \\times ({py}) = {prod}\\).\n**Step 2: Conclusion**\n{corr}."
        elif archetype == 5:
            # Reflection across X-axis
            ref_y = -py
            txt = prefix + f"If point \\({pt}({px}, {py})\\) is reflected across the X-axis, what are the coordinates of its reflection \\({pt}'\\)?"
            corr = f"\\(({px}, {ref_y})\\)"
            dist = [f"\\(({-px}, {py})\\)", f"\\(({-px}, {ref_y})\\)", f"\\(({py}, {px})\\)"]
            sol = f"**Step 1: Reflection Rule**\nReflection across X-axis maps \\((x, y) \\to (x, -y)\\).\nThus \\(({px}, {py}) \\to ({px}, {ref_y})\\).\n**Step 2: Conclusion**\n\\(({px}, {ref_y})\\)."
        elif archetype == 6:
            # Reflection across Y-axis
            ref_x = -px
            txt = prefix + f"Determine the coordinates of the image point when \\({pt}({px}, {py})\\) is reflected across the Y-axis."
            corr = f"\\(({ref_x}, {py})\\)"
            dist = [f"\\(({px}, {-py})\\)", f"\\(({ref_x}, {-py})\\)", f"\\(({-py}, {-px})\\)"]
            sol = f"**Step 1: Reflection Rule**\nReflection across Y-axis maps \\((x, y) \\to (-x, y)\\).\nThus \\(({px}, {py}) \\to ({ref_x}, {py})\\).\n**Step 2: Conclusion**\n\\(({ref_x}, {py})\\)."
        elif archetype == 7:
            # Quadrant of reflected point across origin
            opp_quad = {"Quadrant I": "Quadrant III", "Quadrant II": "Quadrant IV", "Quadrant III": "Quadrant I", "Quadrant IV": "Quadrant II"}[quad_name]
            txt = prefix + f"When point \\({pt}({px}, {py})\\) in {quad_name} is reflected through the origin \\(O\\), which quadrant will its image occupy?"
            corr = opp_quad
            dist = [q for q in ["Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV"] if q != opp_quad][:3]
            sol = f"**Step 1: Reflection in Origin**\nReflection through origin changes signs of both coordinates \\((x, y) \\to (-x, -y)\\).\nThis maps {quad_name} directly to {opp_quad}.\n**Step 2: Conclusion**\n{opp_quad}."
        elif archetype == 8:
            txt = prefix + f"In which quadrant does a point reside if its abscissa is {px} and its ordinate is {py}?"
            corr = quad_name
            dist = dist_quads
            sol = f"**Step 1: Signs**\nAbscissa \\(x = {px}\\) and ordinate \\(y = {py}\\).\nSince {desc}, it lies in {quad_name}.\n**Step 2: Conclusion**\n{quad_name}."
        else:
            txt = prefix + f"A surveyor plots a boundary marker at \\(({px}, {py})\\) on a site map. Identify the quadrant of this marker."
            corr = quad_name
            dist = dist_quads
            sol = f"**Step 1: Signs**\nMarker coordinates \\(({px}, {py})\\) satisfy {desc}.\n**Step 2: Conclusion**\n{quad_name}."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

# ------------------------------------------------------------------------------
# 7.2.1: Line parallel to Y-axis: x = c
# ------------------------------------------------------------------------------
def generate_7_2_1():
    tc = "MH-9-MTH2-7-7.2.1"
    tname = "Line parallel to Y-axis: x = c"
    qs = []
    
    CONSTANTS = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for idx, seq in enumerate(SEQS_80):
        c = CONSTANTS[idx % len(CONSTANTS)]
        # Add offset for diversity
        if idx >= 36:
            c = c + (1 if c >= 0 else -1)
        pt = PTS_80[idx]
        py = (idx % 11) - 5
        has_fig = (idx % 4 != 0)
        svg = svg_parallel_line(f"x = {c}", True, c, f"Line Parallel to Y-axis #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        mode = idx % 8
        if mode == 0:
            txt = prefix + f"What is the equation of a line parallel to the Y-axis and passing through the point \\({pt}({c}, {py})\\)?"
            corr = f"\\(x = {c}\\)"
            dist = [f"\\(y = {py}\\)", f"\\(x = {py}\\)", f"\\(y = {c}\\)"]
            sol = f"**Step 1: Property**\nEvery line parallel to the Y-axis has the equation \\(x = c\\).\nSince it passes through \\(({c}, {py})\\), \\(x = {c}\\).\n**Step 2: Conclusion**\n\\(x = {c}\\)."
        elif mode == 1:
            side = "right" if c > 0 else "left"
            dist_val = abs(c)
            txt = prefix + f"Find the equation of a line parallel to the Y-axis at a distance of {dist_val} units to the {side} of the Y-axis."
            corr = f"\\(x = {c}\\)"
            dist = [f"\\(x = {-c}\\)", f"\\(y = {c}\\)", f"\\(y = {dist_val}\\)"]
            sol = f"**Step 1: Position relative to Y-axis**\nA line parallel to Y-axis at distance {dist_val} to the {side} has equation \\(x = {c}\\).\n**Step 2: Conclusion**\n\\(x = {c}\\)."
        elif mode == 2:
            txt = prefix + f"The graph of the equation \\(x = {c}\\) is a line that is:"
            corr = "Parallel to the Y-axis"
            dist = ["Parallel to the X-axis", "Passing through the origin", "Coincident with the X-axis"]
            sol = f"**Step 1: Equation Form**\nThe equation \\(x = c\\) represents a straight line parallel to the Y-axis.\n**Step 2: Conclusion**\nParallel to the Y-axis."
        elif mode == 3:
            txt = prefix + f"Does the point \\({pt}({c}, {py})\\) lie on the line \\(x = {c}\\)?"
            corr = "Yes, because its x-coordinate is \\({c}\\)"
            dist = ["No, because its y-coordinate is not 0", "Only if \\(y > 0\\)", "Cannot be determined"]
            sol = f"**Step 1: Check coordinates**\nThe line \\(x = {c}\\) contains all points with x-coordinate {c}.\nSince \\({pt}\\) has x-coordinate {c}, it lies on this line.\n**Step 2: Conclusion**\nYes."
        elif mode == 4:
            txt = prefix + f"At what point does the vertical line \\(x = {c}\\) intersect the horizontal X-axis?"
            corr = f"\\(({c}, 0)\\)"
            dist = [f"\\((0, {c})\\)", f"\\(({-c}, 0)\\)", f"\\((0, 0)\\)"]
            sol = f"**Step 1: Intersection with X-axis**\nOn the X-axis, \\(y = 0\\). Substituting into \\(x = {c}\\) gives point \\(({c}, 0)\\).\n**Step 2: Conclusion**\n\\(({c}, 0)\\)."
        elif mode == 5:
            dist_val = abs(c)
            txt = prefix + f"What is the distance between the line \\(x = {c}\\) and the vertical Y-axis?"
            corr = f"{dist_val} units"
            dist = [f"{dist_val + 2} units", f"{c} units" if c < 0 else f"{c + 4} units", f"{dist_val * 2} units"]
            sol = f"**Step 1: Distance Calculation**\nThe Y-axis has equation \\(x = 0\\). Distance between \\(x = {c}\\) and \\(x = 0\\) is \\(|{c} - 0| = {dist_val}\\) units.\n**Step 2: Conclusion**\n{dist_val} units."
        elif mode == 6:
            c2 = -c
            dist_between = abs(c - c2)
            txt = prefix + f"Compute the perpendicular distance between two parallel lines \\(x = {c}\\) and \\(x = {c2}\\)."
            corr = f"{dist_between} units"
            dist = [f"{abs(c)} units", f"{dist_between + 2} units", "0 units"]
            sol = f"**Step 1: Distance Between Parallel Lines**\nDistance \\(= |{c} - ({c2})| = {dist_between}\\) units.\n**Step 2: Conclusion**\n{dist_between} units."
        else:
            txt = prefix + f"If line \\(x = {c}\\) is shifted 3 units to the right, what is the equation of the new line?"
            c_new = c + 3
            corr = f"\\(x = {c_new}\\)"
            dist = [f"\\(x = {c - 3}\\)", f"\\(y = {c_new}\\)", f"\\(x = {c}\\)"]
            sol = f"**Step 1: Shift right**\nShifting right by 3 units adds 3 to the x-value: \\(x = {c} + 3 = {c_new}\\).\n**Step 2: Conclusion**\n\\(x = {c_new}\\)."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

# ------------------------------------------------------------------------------
# 7.2.2: Line parallel to X-axis: y = c
# ------------------------------------------------------------------------------
def generate_7_2_2():
    tc = "MH-9-MTH2-7-7.2.2"
    tname = "Line parallel to X-axis: y = c"
    qs = []
    
    CONSTANTS = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for idx, seq in enumerate(SEQS_80):
        c = CONSTANTS[idx % len(CONSTANTS)]
        if idx >= 36:
            c = c + (1 if c >= 0 else -1)
        pt = PTS_80[idx]
        px = (idx % 13) - 6
        has_fig = (idx % 4 != 0)
        svg = svg_parallel_line(f"y = {c}", False, c, f"Line Parallel to X-axis #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        mode = idx % 8
        if mode == 0:
            txt = prefix + f"Determine the equation of the line parallel to the X-axis passing through \\({pt}({px}, {c})\\)."
            corr = f"\\(y = {c}\\)"
            dist = [f"\\(x = {px}\\)", f"\\(y = {px}\\)", f"\\(x = {c}\\)"]
            sol = f"**Step 1: Property**\nEvery line parallel to the X-axis has equation \\(y = c\\).\nSince it passes through \\(({px}, {c})\\), \\(y = {c}\\).\n**Step 2: Conclusion**\n\\(y = {c}\\)."
        elif mode == 1:
            side = "above" if c > 0 else "below"
            dist_val = abs(c)
            txt = prefix + f"What is the equation of a straight line parallel to the X-axis at a distance of {dist_val} units {side} the X-axis?"
            corr = f"\\(y = {c}\\)"
            dist = [f"\\(y = {-c}\\)", f"\\(x = {c}\\)", f"\\(x = {dist_val}\\)"]
            sol = f"**Step 1: Position relative to X-axis**\nA line parallel to X-axis at distance {dist_val} {side} has equation \\(y = {c}\\).\n**Step 2: Conclusion**\n\\(y = {c}\\)."
        elif mode == 2:
            txt = prefix + f"The graph of the linear equation \\(y = {c}\\) represents a line that is:"
            corr = "Parallel to the X-axis"
            dist = ["Parallel to the Y-axis", "Passing through origin", "Perpendicular to the X-axis"]
            sol = f"**Step 1: Equation Form**\n\\(y = c\\) is a horizontal line parallel to the X-axis.\n**Step 2: Conclusion**\nParallel to the X-axis."
        elif mode == 3:
            txt = prefix + f"At which point does the horizontal line \\(y = {c}\\) intersect the vertical Y-axis?"
            corr = f"\\((0, {c})\\)"
            dist = [f"\\(({c}, 0)\\)", f"\\((0, {-c})\\)", f"\\((0, 0)\\)"]
            sol = f"**Step 1: Intersection with Y-axis**\nOn the Y-axis, \\(x = 0\\). Hence intersection point is \\((0, {c})\\).\n**Step 2: Conclusion**\n\\((0, {c})\\)."
        elif mode == 4:
            dist_val = abs(c)
            txt = prefix + f"Calculate the perpendicular distance from the X-axis to the line \\(y = {c}\\)."
            corr = f"{dist_val} units"
            dist = [f"{dist_val + 2} units", f"{dist_val + 4} units", f"{dist_val * 2} units"]
            sol = f"**Step 1: Distance**\nDistance \\(= |{c} - 0| = {dist_val}\\) units.\n**Step 2: Conclusion**\n{dist_val} units."
        elif mode == 5:
            c2 = -c
            dist_between = abs(c - c2)
            txt = prefix + f"Find the vertical distance between the two horizontal lines \\(y = {c}\\) and \\(y = {c2}\\)."
            corr = f"{dist_between} units"
            dist = [f"{abs(c)} units", f"{dist_between + 3} units", "0 units"]
            sol = f"**Step 1: Distance Between Lines**\nDistance \\(= |{c} - ({c2})| = {dist_between}\\) units.\n**Step 2: Conclusion**\n{dist_between} units."
        elif mode == 6:
            txt = prefix + f"If the horizontal line \\(y = {c}\\) is translated 4 units upwards, what is the resulting equation?"
            c_new = c + 4
            corr = f"\\(y = {c_new}\\)"
            dist = [f"\\(y = {c - 4}\\)", f"\\(x = {c_new}\\)", f"\\(y = {c}\\)"]
            sol = f"**Step 1: Upward translation**\nTranslating up by 4 units yields \\(y = {c} + 4 = {c_new}\\).\n**Step 2: Conclusion**\n\\(y = {c_new}\\)."
        else:
            txt = prefix + f"Does point \\({pt}({px}, {c})\\) satisfy the linear equation \\(y = {c}\\)?"
            corr = f"Yes, because its ordinate is {c}"
            dist = ["No, because its abscissa is not 0", "Only when x is positive", "Cannot be determined"]
            sol = f"**Step 1: Verification**\nThe ordinate of \\({pt}\\) is {c}, which satisfies \\(y = {c}\\).\n**Step 2: Conclusion**\nYes."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

# ------------------------------------------------------------------------------
# 7.2.3: Equation of X-axis (y=0) and Y-axis (x=0)
# ------------------------------------------------------------------------------
def generate_7_2_3():
    tc = "MH-9-MTH2-7-7.2.3"
    tname = "Equation of X-axis (y=0) and Y-axis (x=0)"
    qs = []
    
    for idx, seq in enumerate(SEQS_80):
        px, py = COORDS_80[idx]
        pt = PTS_80[idx]
        has_fig = (idx % 4 != 0)
        svg = svg_cartesian_point(pt, px, py, f"Axes Analysis #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        mode = idx % 8
        if mode == 0:
            txt = prefix + f"What is the standard algebraic equation of the horizontal X-axis in the Cartesian plane?"
            corr = "\\(y = 0\\)"
            dist = ["\\(x = 0\\)", "\\(x = y\\)", "\\(x + y = 0\\)"]
            sol = f"**Step 1: Property of X-axis**\nEvery point on the X-axis has y-coordinate 0. Hence its equation is \\(y = 0\\).\n**Step 2: Conclusion**\n\\(y = 0\\)."
        elif mode == 1:
            txt = prefix + f"Identify the correct algebraic equation representing the vertical Y-axis."
            corr = "\\(x = 0\\)"
            dist = ["\\(y = 0\\)", "\\(x = 1\\)", "\\(y = 1\\)"]
            sol = f"**Step 1: Property of Y-axis**\nEvery point on the Y-axis has x-coordinate 0. Hence its equation is \\(x = 0\\).\n**Step 2: Conclusion**\n\\(x = 0\\)."
        elif mode == 2:
            txt = prefix + f"At what point do the lines \\(y = 0\\) (X-axis) and \\(x = 0\\) (Y-axis) intersect?"
            corr = "\\((0, 0)\\)"
            dist = ["\\((1, 0)\\)", "\\((0, 1)\\)", "\\((1, 1)\\)"]
            sol = f"**Step 1: Simultaneous Solution**\n\\(x = 0\\) and \\(y = 0\\) intersect at the origin \\((0, 0)\\).\n**Step 2: Conclusion**\n\\((0, 0)\\)."
        elif mode == 3:
            txt = prefix + f"The locus of all points whose y-coordinate is identically zero defines the:"
            corr = "X-axis"
            dist = ["Y-axis", "Origin", "Line \\(x = y\\)"]
            sol = f"**Step 1: Locus definition**\nPoints with \\(y = 0\\) form the horizontal X-axis.\n**Step 2: Conclusion**\nX-axis."
        elif mode == 4:
            txt = prefix + f"The locus of all points whose x-coordinate is identically zero represents the:"
            corr = "Y-axis"
            dist = ["X-axis", "Line \\(y = x\\)", "Quadrant I"]
            sol = f"**Step 1: Locus definition**\nPoints with \\(x = 0\\) form the vertical Y-axis.\n**Step 2: Conclusion**\nY-axis."
        elif mode == 5:
            txt = prefix + f"For the point \\({pt}({px}, 0)\\), what is its perpendicular distance from the line \\(y = 0\\)?"
            corr = "0 units"
            dist = [f"{abs(px)} units", "1 unit", "Cannot be determined"]
            sol = f"**Step 1: Distance Calculation**\nSince the y-coordinate is 0, the point lies on \\(y = 0\\), so distance is 0 units.\n**Step 2: Conclusion**\n0 units."
        elif mode == 6:
            txt = prefix + f"For the point \\({pt}(0, {py})\\), what is its distance from the line \\(x = 0\\)?"
            corr = "0 units"
            dist = [f"{abs(py)} units", "1 unit", f"{py} units"]
            sol = f"**Step 1: Distance Calculation**\nPoint \\({pt}(0, {py})\\) lies directly on the line \\(x = 0\\), so distance is 0.\n**Step 2: Conclusion**\n0 units."
        else:
            txt = prefix + f"Which of the following points lies on the line \\(y = 0\\)?"
            corr = f"\\(({px}, 0)\\)"
            dist = [f"\\((0, {px})\\)", f"\\(({px}, 1)\\)", f"\\((1, {px})\\)"]
            sol = f"**Step 1: Condition**\nA point on \\(y = 0\\) must have y-coordinate 0. Point \\(({px}, 0)\\) satisfies this.\n**Step 2: Conclusion**\n\\(({px}, 0)\\)."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

# ------------------------------------------------------------------------------
# 7.3.1: Finding solutions table and plotting straight lines on graph paper
# ------------------------------------------------------------------------------
def generate_7_3_1():
    tc = "MH-9-MTH2-7-7.3.1"
    tname = "Finding solutions table and plotting straight lines on graph paper"
    qs = []
    
    EQUATIONS = [
        ("x + y = 6", 1, 1, 6),
        ("x - y = 2", 1, -1, 2),
        ("2x + y = 8", 2, 1, 8),
        ("x + 2y = 10", 1, 2, 10),
        ("2x - y = 4", 2, -1, 4),
        ("3x + y = 9", 3, 1, 9),
        ("x - 2y = 0", 1, -2, 0),
        ("2x + 3y = 12", 2, 3, 12)
    ]
    
    for idx, seq in enumerate(SEQS_80):
        eq_str, a, b, c = EQUATIONS[idx % len(EQUATIONS)]
        pt = PTS_80[idx]
        has_fig = (idx % 4 != 0)
        svg = svg_parallel_line(eq_str, False, 2, f"Linear Equation Graph #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        mode = idx % 8
        if mode == 0:
            # Find y when x is given
            x_val = (idx % 5) + 1
            # a*x + b*y = c => b*y = c - a*x => y = (c - a*x)/b
            y_val = (c - a * x_val) // b if b != 0 and (c - a * x_val) % b == 0 else c - a * x_val
            txt = prefix + f"For the linear equation \\({eq_str}\\), find the value of \\(y\\) when \\(x = {x_val}\\)."
            corr = f"{y_val}"
            dist = [f"{y_val + 2}", f"{y_val - 1}", f"{-y_val}"]
            sol = f"**Step 1: Substitution**\nSubstitute \\(x = {x_val}\\) into \\({eq_str}\\):\n\\({a}({x_val}) + {b}y = {c} \\implies {a * x_val} + {b}y = {c}\\).\n\\({b}y = {c - a * x_val} \\implies y = {y_val}\\).\n**Step 2: Conclusion**\n{y_val}."
        elif mode == 1:
            # Find x when y is given
            y_val = (idx % 5)
            x_val = (c - b * y_val) // a if a != 0 and (c - b * y_val) % a == 0 else c - b * y_val
            txt = prefix + f"In the linear equation \\({eq_str}\\), determine the value of \\(x\\) when \\(y = {y_val}\\)."
            corr = f"{x_val}"
            dist = [f"{x_val + 3}", f"{x_val - 2}", f"{-x_val}"]
            sol = f"**Step 1: Substitution**\nSubstitute \\(y = {y_val}\\) into \\({eq_str}\\):\n\\({a}x + {b}({y_val}) = {c} \\implies {a}x + {b * y_val} = {c}\\).\n\\({a}x = {c - b * y_val} \\implies x = {x_val}\\).\n**Step 2: Conclusion**\n{x_val}."
        elif mode == 2:
            # X-intercept (y=0)
            x_int = c // a if a != 0 and c % a == 0 else f"\\frac{{{c}}}{{{a}}}"
            txt = prefix + f"Find the coordinates of the point where the line \\({eq_str}\\) intersects the X-axis."
            corr = f"\\(({x_int}, 0)\\)"
            dist = [f"\\((0, {x_int})\\)", f"\\(({x_int}, 1)\\)", f"\\((0, 0)\\)"]
            sol = f"**Step 1: Set y = 0**\nOn the X-axis, \\(y = 0\\).\n\\({a}x + {b}(0) = {c} \\implies {a}x = {c} \\implies x = {x_int}\\).\nPoint is \\(({x_int}, 0)\\).\n**Step 2: Conclusion**\n\\(({x_int}, 0)\\)."
        elif mode == 3:
            # Y-intercept (x=0)
            y_int = c // b if b != 0 and c % b == 0 else f"\\frac{{{c}}}{{{b}}}"
            txt = prefix + f"Determine the Y-intercept coordinates of the line with equation \\({eq_str}\\)."
            corr = f"\\((0, {y_int})\\)"
            dist = [f"\\(({y_int}, 0)\\)", f"\\((1, {y_int})\\)", f"\\((0, 0)\\)"]
            sol = f"**Step 1: Set x = 0**\nOn the Y-axis, \\(x = 0\\).\n\\({a}(0) + {b}y = {c} \\implies {b}y = {c} \\implies y = {y_int}\\).\nPoint is \\((0, {y_int})\\).\n**Step 2: Conclusion**\n\\((0, {y_int})\\)."
        elif mode == 4:
            txt = prefix + f"How many distinct solutions (ordered pairs \\((x, y)\\)) does the linear equation \\({eq_str}\\) possess?"
            corr = "Infinitely many"
            dist = ["Exactly one", "Exactly two", "Zero"]
            sol = f"**Step 1: Theory**\nA linear equation in two variables represents a straight line consisting of infinitely many points, each being a solution.\n**Step 2: Conclusion**\nInfinitely many."
        elif mode == 5:
            # Verify if point satisfies equation
            x_test = 2
            y_test = (c - a * x_test) // b if b != 0 and (c - a * x_test) % b == 0 else 1
            is_sol = (a * x_test + b * y_test == c)
            txt = prefix + f"Does the ordered pair \\(({x_test}, {y_test})\\) satisfy the equation \\({eq_str}\\)?"
            corr = "Yes, it is a valid solution" if is_sol else "No, it does not satisfy the equation"
            dist = ["No, it does not satisfy the equation" if is_sol else "Yes, it is a valid solution", "Only if both variables are negative", "Cannot be determined"]
            sol = f"**Step 1: Check LHS**\n\\(\\text{{LHS}} = {a}({x_test}) + {b}({y_test}) = {a * x_test + b * y_test}\\).\n\\(\\text{{RHS}} = {c}\\).\n**Step 2: Conclusion**\n{corr}."
        elif mode == 6:
            txt = prefix + f"To plot a straight line graph of \\({eq_str}\\) accurately, what is the minimum number of points recommended to establish collinearity?"
            corr = "At least 3 points"
            dist = ["Only 1 point", "At least 10 points", "At least 5 points"]
            sol = f"**Step 1: Plotting Rule**\nTwo points determine a line, but a 3rd point is necessary to verify accuracy and ensure no calculation error occurred.\n**Step 2: Conclusion**\nAt least 3 points."
        else:
            txt = prefix + f"What geometric figure is represented on a graph paper by the equation \\({eq_str}\\)?"
            corr = "Straight line"
            dist = ["Parabola", "Circle", "Pair of intersecting rays"]
            sol = f"**Step 1: Concept**\nEvery linear equation of degree 1 in two variables \\(ax + by + c = 0\\) represents a straight line on graph paper.\n**Step 2: Conclusion**\nStraight line."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def main():
    all_qs = []
    print("Generating Chapter 7 questions...")
    q1 = generate_7_1_1()
    print(f"  7.1.1: {len(q1)} Qs")
    all_qs.extend(q1)
    
    q2 = generate_7_1_2()
    print(f"  7.1.2: {len(q2)} Qs")
    all_qs.extend(q2)
    
    q3 = generate_7_2_1()
    print(f"  7.2.1: {len(q3)} Qs")
    all_qs.extend(q3)
    
    q4 = generate_7_2_2()
    print(f"  7.2.2: {len(q4)} Qs")
    all_qs.extend(q4)
    
    q5 = generate_7_2_3()
    print(f"  7.2.3: {len(q5)} Qs")
    all_qs.extend(q5)
    
    q6 = generate_7_3_1()
    print(f"  7.3.1: {len(q6)} Qs")
    all_qs.extend(q6)
    
    out_file = "scripts/mh9_mth2_ch7_perfect.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
        
    print(f"Total Chapter 7 generated: {len(all_qs)} questions written to {out_file}")

if __name__ == "__main__":
    main()
