# scripts/generate_flawless_mth2_ch7_v2.py
import json
import math

SEQS_80 = [101 + i for i in range(40)] + [201 + i for i in range(20)] + [301 + i for i in range(20)]

def make_opts(corr, dist):
    opts = [{"id": "A", "text": str(corr), "isCorrect": True}]
    letters = ["B", "C", "D"]
    seen = {str(corr)}
    clean_dist = []
    for d in dist:
        sd = str(d)
        if sd not in seen and len(clean_dist) < 3:
            seen.add(sd)
            clean_dist.append(sd)
    
    counter = 1
    while len(clean_dist) < 3:
        fallback = f"{corr} + {counter}"
        if fallback not in seen:
            seen.add(fallback)
            clean_dist.append(fallback)
        counter += 1
        
    for idx, d in enumerate(clean_dist):
        opts.append({"id": letters[idx], "text": d, "isCorrect": False})
        
    shift = len(str(corr)) % 4
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
    cx = 120 + x * 10
    cy = 120 - y * 10
    return (
        f'<svg width="240" height="240" viewBox="0 0 240 240" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a;border-radius:8px;display:block;margin:12px auto;">'
        f'<defs><pattern id="g_{pt}_{x}_{y}" width="10" height="10" patternUnits="userSpaceOnUse">'
        f'<path d="M 10 0 L 0 0 0 10" fill="none" stroke="#1e293b" stroke-width="0.5"/>'
        f'</pattern></defs>'
        f'<rect width="240" height="240" fill="url(#g_{pt}_{x}_{y})"/>'
        f'<line x1="0" y1="120" x2="240" y2="120" stroke="#64748b" stroke-width="1.5"/>'
        f'<line x1="120" y1="0" x2="120" y2="240" stroke="#64748b" stroke-width="1.5"/>'
        f'<text x="228" y="115" fill="#94a3b8" font-size="10" font-family="sans-serif">X</text>'
        f'<text x="125" y="15" fill="#94a3b8" font-size="10" font-family="sans-serif">Y</text>'
        f'<line x1="{cx}" y1="120" x2="{cx}" y2="{cy}" stroke="#38bdf8" stroke-dasharray="2,2" stroke-width="1"/>'
        f'<line x1="120" y1="{cy}" x2="{cx}" y2="{cy}" stroke="#38bdf8" stroke-dasharray="2,2" stroke-width="1"/>'
        f'<circle cx="{cx}" cy="{cy}" r="4" fill="#f59e0b"/>'
        f'<text x="{cx + 6}" y="{cy - 6}" fill="#f59e0b" font-size="11" font-weight="bold" font-family="sans-serif">{pt}({x}, {y})</text>'
        f'<text x="10" y="230" fill="#38bdf8" font-size="10" font-family="sans-serif">{title}</text>'
        f'</svg>'
    )

def svg_parallel_line(eq, is_vertical, val, title):
    coord = 120 + val * 10 if is_vertical else 120 - val * 10
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

# 80 distinct coordinates
POINTS_DATA = []
for x in [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for y in [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]:
        POINTS_DATA.append((x, y))
        if len(POINTS_DATA) >= 80:
            break
    if len(POINTS_DATA) >= 80:
        break

PTS_NAMES = [f"P_{{{i+1}}}" if i >= 26 else chr(65 + i) for i in range(80)]

# ------------------------------------------------------------------------------
# Subtopic 7.1.1
# ------------------------------------------------------------------------------
def generate_7_1_1():
    tc = "MH-9-MTH2-7-7.1.1"
    tname = "X-axis, Y-axis, Origin (0,0)"
    qs = []
    
    for idx, seq in enumerate(SEQS_80):
        px, py = POINTS_DATA[idx]
        pt = PTS_NAMES[idx]
        has_fig = (idx % 3 != 0)
        svg = svg_cartesian_point(pt, px, py, f"Cartesian Geometry #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        # 10 completely distinct archetypes per 8 questions (8 archetypes x 10 unique questions)
        arch = idx % 8
        k = idx // 8
        
        if arch == 0:
            # Questions about the origin with unique parameters
            offset = k + 1
            txt = prefix + f"A point starts at the origin \\(O(0, 0)\\) and moves {offset} units along the positive X-axis. What are its final coordinates?"
            corr = f"\\(({offset}, 0)\\)"
            dist = [f"\\((0, {offset})\\)", f"\\(({-offset}, 0)\\)", f"\\(({offset}, {offset})\\)"]
            sol = f"**Step 1: Movement**\nStarting at \\((0, 0)\\) and moving {offset} units right gives \\(({offset}, 0)\\).\n**Step 2: Conclusion**\n\\(({offset}, 0)\\)."
        elif arch == 1:
            # Abscissa of distinct points
            txt = prefix + f"For the point \\({pt}({px}, {py})\\) shown in the Cartesian plane, state the value of its abscissa."
            corr = f"{px}"
            dist = [f"{py}", f"{-px}", f"{px + 2}"]
            sol = f"**Step 1: Definition**\nThe abscissa of a point is its horizontal x-coordinate.\nHere \\(x = {px}\\).\n**Step 2: Conclusion**\n{px}."
        elif arch == 2:
            # Ordinate of distinct points
            txt = prefix + f"Identify the ordinate of point \\({pt}({px}, {py})\\) in the two-dimensional coordinate system."
            corr = f"{py}"
            dist = [f"{px}", f"{-py}", f"{py - 2}"]
            sol = f"**Step 1: Definition**\nThe ordinate of a point is its vertical y-coordinate.\nHere \\(y = {py}\\).\n**Step 2: Conclusion**\n{py}."
        elif arch == 3:
            # Distance from X-axis
            d = abs(py)
            txt = prefix + f"Calculate the perpendicular distance from the horizontal X-axis to the point \\({pt}({px}, {py})\\)."
            corr = f"{d} units"
            dist = [f"{abs(px)} units", f"{d + 3} units", f"{d + 1} units"]
            sol = f"**Step 1: Distance formula**\nPerpendicular distance from X-axis equals \\(|y| = |{py}| = {d}\\) units.\n**Step 2: Conclusion**\n{d} units."
        elif arch == 4:
            # Distance from Y-axis
            d = abs(px)
            txt = prefix + f"Determine the perpendicular distance from the vertical Y-axis to the point \\({pt}({px}, {py})\\)."
            corr = f"{d} units"
            dist = [f"{abs(py)} units", f"{d + 2} units", f"{d + 4} units"]
            sol = f"**Step 1: Distance formula**\nPerpendicular distance from Y-axis equals \\(|x| = |{px}| = {d}\\) units.\n**Step 2: Conclusion**\n{d} units."
        elif arch == 5:
            # Point on X-axis: distance from origin
            dist_val = abs(px)
            txt = prefix + f"Point \\({pt}({px}, 0)\\) lies on the X-axis. What is its distance from the origin \\(O(0, 0)\\)?"
            corr = f"{dist_val} units"
            dist = [f"{dist_val + 2} units", f"{px} units" if px < 0 else f"{px + 3} units", f"{dist_val * 2} units"]
            sol = f"**Step 1: Distance on Axis**\nDistance from origin \\(= |{px} - 0| = {dist_val}\\) units.\n**Step 2: Conclusion**\n{dist_val} units."
        elif arch == 6:
            # Point on Y-axis: distance from origin
            dist_val = abs(py)
            txt = prefix + f"Point \\({pt}(0, {py})\\) is located on the Y-axis. Compute its straight-line distance from the origin."
            corr = f"{dist_val} units"
            dist = [f"{dist_val + 3} units", f"{py} units" if py < 0 else f"{py + 1} units", f"{dist_val * 2} units"]
            sol = f"**Step 1: Distance on Axis**\nDistance \\(= |{py} - 0| = {dist_val}\\) units.\n**Step 2: Conclusion**\n{dist_val} units."
        else:
            # Sum or product of coordinates
            val = px + py
            txt = prefix + f"For the point \\({pt}({px}, {py})\\), evaluate the algebraic sum of its abscissa and ordinate \\(x + y\\)."
            corr = f"{val}"
            dist = [f"{val + 2}", f"{val - 3}", f"{-val}"]
            sol = f"**Step 1: Sum**\n\\(x + y = {px} + ({py}) = {val}\\).\n**Step 2: Conclusion**\n{val}."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

# ------------------------------------------------------------------------------
# Subtopic 7.1.2: Plotting points in all four quadrants
# ------------------------------------------------------------------------------
def generate_7_1_2():
    tc = "MH-9-MTH2-7-7.1.2"
    tname = "Plotting points in all four quadrants"
    qs = []
    
    for idx, seq in enumerate(SEQS_80):
        raw_x, raw_y = POINTS_DATA[idx]
        pt = PTS_NAMES[idx]
        has_fig = (idx % 3 != 0)
        
        # Balance quadrants across the 80 questions:
        q_idx = idx % 4
        if q_idx == 0:
            px, py = abs(raw_x), abs(raw_y)
            q_name = "Quadrant I"
            sign_str = "(+, +)"
            dist_q = ["Quadrant II", "Quadrant IV", "Quadrant III"]
        elif q_idx == 1:
            px, py = -abs(raw_x), abs(raw_y)
            q_name = "Quadrant II"
            sign_str = "(-, +)"
            dist_q = ["Quadrant I", "Quadrant III", "Quadrant IV"]
        elif q_idx == 2:
            px, py = -abs(raw_x), -abs(raw_y)
            q_name = "Quadrant III"
            sign_str = "(-, -)"
            dist_q = ["Quadrant II", "Quadrant IV", "Quadrant I"]
        else:
            px, py = abs(raw_x), -abs(raw_y)
            q_name = "Quadrant IV"
            sign_str = "(+, -)"
            dist_q = ["Quadrant I", "Quadrant II", "Quadrant III"]
            
        svg = svg_cartesian_point(pt, px, py, f"Quadrant Identification #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        # 8 distinct question styles
        style = (idx // 4) % 10
        if style == 0:
            txt = prefix + f"In which quadrant of the coordinate plane is the point \\({pt}({px}, {py})\\) situated?"
            corr = q_name
            dist = dist_q
            sol = f"**Step 1: Sign check**\n\\(x = {px}\\) and \\(y = {py}\\), which matches {sign_str}.\n**Step 2: Conclusion**\n{q_name}."
        elif style == 1:
            txt = prefix + f"Point \\({pt}\\) has abscissa {px} and ordinate {py}. Determine its location on the Cartesian grid."
            corr = q_name
            dist = dist_q
            sol = f"**Step 1: Coordinates**\nPoint coordinates are \\(({px}, {py})\\), located in {q_name}.\n**Step 2: Conclusion**\n{q_name}."
        elif style == 2:
            ref_y = -py
            txt = prefix + f"If point \\({pt}({px}, {py})\\) is reflected across the X-axis, what are the coordinates of the reflected point?"
            corr = f"\\(({px}, {ref_y})\\)"
            dist = [f"\\(({-px}, {py})\\)", f"\\(({-px}, {ref_y})\\)", f"\\(({py}, {px})\\)"]
            sol = f"**Step 1: Reflection across X-axis**\n\\((x, y) \\to (x, -y)\\), so \\(({px}, {py}) \\to ({px}, {ref_y})\\).\n**Step 2: Conclusion**\n\\(({px}, {ref_y})\\)."
        elif style == 3:
            ref_x = -px
            txt = prefix + f"What is the image of point \\({pt}({px}, {py})\\) when reflected across the vertical Y-axis?"
            corr = f"\\(({ref_x}, {py})\\)"
            dist = [f"\\(({px}, {-py})\\)", f"\\(({ref_x}, {-py})\\)", f"\\(({-py}, {-px})\\)"]
            sol = f"**Step 1: Reflection across Y-axis**\n\\((x, y) \\to (-x, y)\\), so \\(({px}, {py}) \\to ({ref_x}, {py})\\).\n**Step 2: Conclusion**\n\\(({ref_x}, {py})\\)."
        elif style == 4:
            txt = prefix + f"For the point \\({pt}({px}, {py})\\), what is the sign of the product \\(x \\times y\\)?"
            prod = px * py
            corr = f"Positive ({prod})" if prod > 0 else f"Negative ({prod})"
            dist = [f"Negative ({prod})" if prod > 0 else f"Positive ({prod})", "Zero (0)", "Undefined"]
            sol = f"**Step 1: Product**\n\\({px} \\times ({py}) = {prod}\\).\n**Step 2: Conclusion**\n{corr}."
        elif style == 5:
            # Midpoint to origin
            mx, my = px / 2, py / 2
            txt = prefix + f"Find the coordinates of the midpoint between origin \\(O(0, 0)\\) and point \\({pt}({px}, {py})\\)."
            corr = f"\\(({mx}, {my})\\)"
            dist = [f"\\(({px}, {py})\\)", f"\\(({-mx}, {my})\\)", f"\\(({mx}, {-my})\\)"]
            sol = f"**Step 1: Midpoint Formula**\n\\((\\frac{{0 + {px}}}{{2}}, \\frac{{0 + {py}}}{{2}}) = ({mx}, {my})\\).\n**Step 2: Conclusion**\n\\(({mx}, {my})\\)."
        elif style == 6:
            txt = prefix + f"Which quadrant contains all points with the sign signature \\({sign_str}\\)?"
            corr = q_name
            dist = dist_q
            sol = f"**Step 1: Definition**\nThe sign pattern \\({sign_str}\\) uniquely belongs to {q_name}.\n**Step 2: Conclusion**\n{q_name}."
        elif style == 7:
            # Shift point
            sx = px + 1
            sy = py + 2
            txt = prefix + f"If point \\({pt}({px}, {py})\\) is shifted 1 unit right and 2 units up, what are its new coordinates?"
            corr = f"\\(({sx}, {sy})\\)"
            dist = [f"\\(({px - 1}, {py + 2})\\)", f"\\(({sx}, {py - 2})\\)", f"\\(({px}, {py})\\)"]
            sol = f"**Step 1: Translation**\nNew \\(x = {px} + 1 = {sx}\\), New \\(y = {py} + 2 = {sy}\\).\n**Step 2: Conclusion**\n\\(({sx}, {sy})\\)."
        elif style == 8:
            dist_sq = px*px + py*py
            txt = prefix + f"Compute the squared distance \\(OP^2\\) from origin \\(O(0,0)\\) to point \\({pt}({px}, {py})\\)."
            corr = f"{dist_sq}"
            dist = [f"{dist_sq + 5}", f"{dist_sq - 4}", f"{abs(px) + abs(py)}"]
            sol = f"**Step 1: Distance Squared**\n\\(OP^2 = x^2 + y^2 = {px}^2 + ({py})^2 = {dist_sq}\\).\n**Step 2: Conclusion**\n{dist_sq}."
        else:
            txt = prefix + f"A point is plotted {abs(px)} units {'right' if px > 0 else 'left'} of the Y-axis and {abs(py)} units {'above' if py > 0 else 'below'} the X-axis. Name its quadrant."
            corr = q_name
            dist = dist_q
            sol = f"**Step 1: Position**\nCoordinates are \\(({px}, {py})\\), which is in {q_name}.\n**Step 2: Conclusion**\n{q_name}."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

# ------------------------------------------------------------------------------
# Subtopic 7.2.1: Line parallel to Y-axis: x = c
# ------------------------------------------------------------------------------
def generate_7_2_1():
    tc = "MH-9-MTH2-7-7.2.1"
    tname = "Line parallel to Y-axis: x = c"
    qs = []
    
    # 80 distinct constant values for lines x = c
    C_VALS = [i for i in range(-40, 41) if i != 0][:80]
    
    for idx, seq in enumerate(SEQS_80):
        c = C_VALS[idx]
        pt = PTS_NAMES[idx]
        py = (idx % 15) - 7
        has_fig = (idx % 3 != 0)
        svg = svg_parallel_line(f"x = {c}", True, c if abs(c) <= 9 else (c // 5), f"Vertical Line x = {c} #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        mode = idx % 8
        if mode == 0:
            txt = prefix + f"What is the equation of the line parallel to the Y-axis passing through the point \\({pt}({c}, {py})\\)?"
            corr = f"\\(x = {c}\\)"
            dist = [f"\\(y = {py}\\)", f"\\(x = {py}\\)", f"\\(y = {c}\\)"]
            sol = f"**Step 1: Line Parallel to Y-axis**\nEquation is \\(x = c\\). Since x-coordinate is {c}, \\(x = {c}\\).\n**Step 2: Conclusion**\n\\(x = {c}\\)."
        elif mode == 1:
            side = "right" if c > 0 else "left"
            dist_val = abs(c)
            txt = prefix + f"A line is parallel to the Y-axis and situated {dist_val} units to the {side} of it. State its algebraic equation."
            corr = f"\\(x = {c}\\)"
            dist = [f"\\(x = {-c}\\)", f"\\(y = {c}\\)", f"\\(y = {dist_val}\\)"]
            sol = f"**Step 1: Distance and Side**\nDistance is {dist_val} to the {side}, so equation is \\(x = {c}\\).\n**Step 2: Conclusion**\n\\(x = {c}\\)."
        elif mode == 2:
            txt = prefix + f"At what point does the vertical line \\(x = {c}\\) cross the horizontal X-axis?"
            corr = f"\\(({c}, 0)\\)"
            dist = [f"\\((0, {c})\\)", f"\\(({-c}, 0)\\)", f"\\((0, 0)\\)"]
            sol = f"**Step 1: Intersect X-axis**\nOn X-axis, \\(y = 0\\). Thus intersection point is \\(({c}, 0)\\).\n**Step 2: Conclusion**\n\\(({c}, 0)\\)."
        elif mode == 3:
            dist_val = abs(c)
            txt = prefix + f"What is the perpendicular distance between the vertical Y-axis and the line \\(x = {c}\\)?"
            corr = f"{dist_val} units"
            dist = [f"{dist_val + 3} units", f"{dist_val + 5} units", f"{dist_val * 2} units"]
            sol = f"**Step 1: Distance**\nDistance \\(= |{c} - 0| = {dist_val}\\) units.\n**Step 2: Conclusion**\n{dist_val} units."
        elif mode == 4:
            c2 = c + 5
            txt = prefix + f"Calculate the horizontal distance separating two parallel lines \\(x = {c}\\) and \\(x = {c2}\\)."
            corr = "5 units"
            dist = ["10 units", f"{abs(c)} units", "2 units"]
            sol = f"**Step 1: Distance between lines**\nDistance \\(= |{c2} - {c}| = 5\\) units.\n**Step 2: Conclusion**\n5 units."
        elif mode == 5:
            # Linear form ax + b = 0
            # x = c => x - c = 0
            txt = prefix + f"Express the equation of the line \\(x = {c}\\) in the standard linear form \\(ax + by + d = 0\\)."
            corr = f"\\(1x + 0y - {c} = 0\\)" if c > 0 else f"\\(1x + 0y + {-c} = 0\\)"
            dist = [f"\\(0x + 1y - {c} = 0\\)", f"\\(1x + 1y - {c} = 0\\)", f"\\(1x - 1y + {c} = 0\\)"]
            sol = f"**Step 1: Standard form**\n\\(x = {c} \\implies 1x + 0y - ({c}) = 0\\).\n**Step 2: Conclusion**\n{corr}."
        elif mode == 6:
            c_shift = c + 4
            txt = prefix + f"If the line \\(x = {c}\\) is shifted 4 units to the right, what is the equation of the resulting line?"
            corr = f"\\(x = {c_shift}\\)"
            dist = [f"\\(x = {c - 4}\\)", f"\\(y = {c_shift}\\)", f"\\(x = {c}\\)"]
            sol = f"**Step 1: Shift right**\nNew \\(x = {c} + 4 = {c_shift}\\).\n**Step 2: Conclusion**\n\\(x = {c_shift}\\)."
        else:
            txt = prefix + f"Which of the following points lies on the line \\(x = {c}\\)?"
            corr = f"\\(({c}, {py})\\)"
            dist = [f"\\(({c + 1}, {py})\\)", f"\\(({py}, {c})\\)", f"\\((0, {c})\\)"]
            sol = f"**Step 1: Verification**\nPoints on \\(x = {c}\\) must have x-coordinate equal to {c}. Point \\(({c}, {py})\\) satisfies this.\n**Step 2: Conclusion**\n\\(({c}, {py})\\)."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

# ------------------------------------------------------------------------------
# Subtopic 7.2.2: Line parallel to X-axis: y = c
# ------------------------------------------------------------------------------
def generate_7_2_2():
    tc = "MH-9-MTH2-7-7.2.2"
    tname = "Line parallel to X-axis: y = c"
    qs = []
    
    C_VALS = [i for i in range(-40, 41) if i != 0][:80]
    
    for idx, seq in enumerate(SEQS_80):
        c = C_VALS[idx]
        pt = PTS_NAMES[idx]
        px = (idx % 17) - 8
        has_fig = (idx % 3 != 0)
        svg = svg_parallel_line(f"y = {c}", False, c if abs(c) <= 9 else (c // 5), f"Horizontal Line y = {c} #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        mode = idx % 8
        if mode == 0:
            txt = prefix + f"Determine the algebraic equation of the line parallel to the X-axis passing through \\({pt}({px}, {c})\\)."
            corr = f"\\(y = {c}\\)"
            dist = [f"\\(x = {px}\\)", f"\\(y = {px}\\)", f"\\(x = {c}\\)"]
            sol = f"**Step 1: Line Parallel to X-axis**\nEquation is \\(y = c\\). Since y-coordinate is {c}, \\(y = {c}\\).\n**Step 2: Conclusion**\n\\(y = {c}\\)."
        elif mode == 1:
            side = "above" if c > 0 else "below"
            dist_val = abs(c)
            txt = prefix + f"What is the equation of a straight line parallel to the X-axis at a distance of {dist_val} units {side} it?"
            corr = f"\\(y = {c}\\)"
            dist = [f"\\(y = {-c}\\)", f"\\(x = {c}\\)", f"\\(x = {dist_val}\\)"]
            sol = f"**Step 1: Distance and Position**\nDistance {dist_val} units {side} X-axis gives \\(y = {c}\\).\n**Step 2: Conclusion**\n\\(y = {c}\\)."
        elif mode == 2:
            txt = prefix + f"At which point does the horizontal line \\(y = {c}\\) intersect the vertical Y-axis?"
            corr = f"\\((0, {c})\\)"
            dist = [f"\\(({c}, 0)\\)", f"\\((0, {-c})\\)", f"\\((0, 0)\\)"]
            sol = f"**Step 1: Intersect Y-axis**\nOn Y-axis, \\(x = 0\\). Point of intersection is \\((0, {c})\\).\n**Step 2: Conclusion**\n\\((0, {c})\\)."
        elif mode == 3:
            dist_val = abs(c)
            txt = prefix + f"Find the perpendicular distance from the line \\(y = {c}\\) to the horizontal X-axis."
            corr = f"{dist_val} units"
            dist = [f"{dist_val + 2} units", f"{dist_val + 4} units", f"{dist_val * 2} units"]
            sol = f"**Step 1: Distance**\nDistance \\(= |{c} - 0| = {dist_val}\\) units.\n**Step 2: Conclusion**\n{dist_val} units."
        elif mode == 4:
            c2 = c + 6
            txt = prefix + f"What is the vertical distance separating the two parallel lines \\(y = {c}\\) and \\(y = {c2}\\)?"
            corr = "6 units"
            dist = ["12 units", f"{abs(c)} units", "3 units"]
            sol = f"**Step 1: Vertical Distance**\nDistance \\(= |{c2} - {c}| = 6\\) units.\n**Step 2: Conclusion**\n6 units."
        elif mode == 5:
            txt = prefix + f"Express the horizontal line equation \\(y = {c}\\) in standard form \\(ax + by + d = 0\\)."
            corr = f"\\(0x + 1y - {c} = 0\\)" if c > 0 else f"\\(0x + 1y + {-c} = 0\\)"
            dist = [f"\\(1x + 0y - {c} = 0\\)", f"\\(0x - 1y - {c} = 0\\)", f"\\(1x + 1y = {c}\\)"]
            sol = f"**Step 1: Standard form**\n\\(y = {c} \\implies 0x + 1y - ({c}) = 0\\).\n**Step 2: Conclusion**\n{corr}."
        elif mode == 6:
            c_shift = c + 3
            txt = prefix + f"When the horizontal line \\(y = {c}\\) is shifted 3 units upward, what is its new equation?"
            corr = f"\\(y = {c_shift}\\)"
            dist = [f"\\(y = {c - 3}\\)", f"\\(x = {c_shift}\\)", f"\\(y = {c}\\)"]
            sol = f"**Step 1: Upward shift**\nNew \\(y = {c} + 3 = {c_shift}\\).\n**Step 2: Conclusion**\n\\(y = {c_shift}\\)."
        else:
            txt = prefix + f"Which ordered pair represents a point on the line \\(y = {c}\\)?"
            corr = f"\\(({px}, {c})\\)"
            dist = [f"\\(({c}, {px})\\)", f"\\(({px}, {c + 1})\\)", f"\\((0, 0)\\)"]
            sol = f"**Step 1: Verification**\nPoints on \\(y = {c}\\) must have y-coordinate equal to {c}. Point \\(({px}, {c})\\) satisfies this.\n**Step 2: Conclusion**\n\\(({px}, {c})\\)."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

# ------------------------------------------------------------------------------
# Subtopic 7.2.3: Equation of X-axis (y=0) and Y-axis (x=0)
# ------------------------------------------------------------------------------
def generate_7_2_3():
    tc = "MH-9-MTH2-7-7.2.3"
    tname = "Equation of X-axis (y=0) and Y-axis (x=0)"
    qs = []
    
    for idx, seq in enumerate(SEQS_80):
        px, py = POINTS_DATA[idx]
        pt = PTS_NAMES[idx]
        has_fig = (idx % 3 != 0)
        svg = svg_cartesian_point(pt, px, py, f"Axes Locus Analysis #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        mode = idx % 8
        if mode == 0:
            txt = prefix + f"State the standard algebraic equation defining the horizontal X-axis."
            corr = "\\(y = 0\\)"
            dist = ["\\(x = 0\\)", "\\(x = y\\)", "\\(x + y = 0\\)"]
            sol = f"**Step 1: Definition**\nEvery point on the X-axis has y-coordinate 0. Hence \\(y = 0\\).\n**Step 2: Conclusion**\n\\(y = 0\\)."
        elif mode == 1:
            txt = prefix + f"What is the mathematical equation that defines the vertical Y-axis?"
            corr = "\\(x = 0\\)"
            dist = ["\\(y = 0\\)", "\\(x = 1\\)", "\\(y = x\\)"]
            sol = f"**Step 1: Definition**\nEvery point on the Y-axis has x-coordinate 0. Hence \\(x = 0\\).\n**Step 2: Conclusion**\n\\(x = 0\\)."
        elif mode == 2:
            txt = prefix + f"What are the coordinates of the common intersection point of lines \\(x = 0\\) and \\(y = 0\\)?"
            corr = "\\((0, 0)\\)"
            dist = ["\\((1, 0)\\)", "\\((0, 1)\\)", "\\((1, 1)\\)"]
            sol = f"**Step 1: Intersection**\nSimultaneous solution of \\(x = 0\\) and \\(y = 0\\) is the origin \\((0, 0)\\).\n**Step 2: Conclusion**\n\\((0, 0)\\)."
        elif mode == 3:
            txt = prefix + f"The locus of all points whose ordinate is zero represents which geometric entity?"
            corr = "X-axis"
            dist = ["Y-axis", "Line \\(x = y\\)", "Origin only"]
            sol = f"**Step 1: Locus**\nOrdinate is y. Points with \\(y = 0\\) form the X-axis.\n**Step 2: Conclusion**\nX-axis."
        elif mode == 4:
            txt = prefix + f"The geometric locus of all points having an abscissa equal to zero is called the:"
            corr = "Y-axis"
            dist = ["X-axis", "Line \\(y = x\\)", "Origin only"]
            sol = f"**Step 1: Locus**\nAbscissa is x. Points with \\(x = 0\\) constitute the Y-axis.\n**Step 2: Conclusion**\nY-axis."
        elif mode == 5:
            txt = prefix + f"If point \\({pt}({px}, k)\\) lies directly on the line \\(y = 0\\), determine \\(k\\)."
            corr = "0"
            dist = [f"{px}", f"{-px}", "1"]
            sol = f"**Step 1: Condition**\nOn line \\(y = 0\\), y-coordinate is 0. So \\(k = 0\\).\n**Step 2: Conclusion**\n0."
        elif mode == 6:
            txt = prefix + f"Point \\({pt}(m, {py})\\) is located on the line \\(x = 0\\). What is the exact value of \\(m\\)?"
            corr = "0"
            dist = [f"{py}", f"{-py}", "1"]
            sol = f"**Step 1: Condition**\nOn line \\(x = 0\\), x-coordinate is 0. So \\(m = 0\\).\n**Step 2: Conclusion**\n0."
        else:
            txt = prefix + f"Which of the following points belongs to the line \\(y = 0\\) (the X-axis)?"
            corr = f"\\(({px}, 0)\\)"
            dist = [f"\\((0, {px})\\)", f"\\(({px}, 1)\\)", f"\\((1, {px})\\)"]
            sol = f"**Step 1: Verification**\nPoints on \\(y = 0\\) must have ordinate 0. \\(({px}, 0)\\) satisfies this.\n**Step 2: Conclusion**\n\\(({px}, 0)\\)."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

# ------------------------------------------------------------------------------
# Subtopic 7.3.1: Finding solutions table and plotting straight lines on graph paper
# ------------------------------------------------------------------------------
def generate_7_3_1():
    tc = "MH-9-MTH2-7-7.3.1"
    tname = "Finding solutions table and plotting straight lines on graph paper"
    qs = []
    
    # 80 distinct linear equations with integer solutions
    EQUATIONS_80 = []
    for a in [1, 2, 3, 4]:
        for b in [1, -1, 2, -2]:
            for c in range(1, 15):
                eq_label = f"{a}x + {b}y = {c}" if b > 0 else f"{a}x - {abs(b)}y = {c}"
                EQUATIONS_80.append((eq_label, a, b, c))
                if len(EQUATIONS_80) >= 80:
                    break
            if len(EQUATIONS_80) >= 80:
                break
        if len(EQUATIONS_80) >= 80:
            break
            
    for idx, seq in enumerate(SEQS_80):
        eq_str, a, b, c = EQUATIONS_80[idx]
        pt = PTS_NAMES[idx]
        has_fig = (idx % 3 != 0)
        svg = svg_parallel_line(eq_str, False, 2, f"Linear Graph #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        mode = idx % 8
        if mode == 0:
            # Given x, find y
            x_val = (idx % 4) + 1
            # a*x + b*y = c => b*y = c - a*x
            rem = c - a * x_val
            y_val = rem // b if rem % b == 0 else f"\\frac{{{rem}}}{{{b}}}"
            txt = prefix + f"In the linear equation \\({eq_str}\\), calculate the corresponding value of \\(y\\) when \\(x = {x_val}\\)."
            corr = f"{y_val}"
            dist = [f"{y_val + 2}" if isinstance(y_val, int) else f"\\frac{{{rem + 1}}}{{{b}}}", 
                    f"{y_val - 1}" if isinstance(y_val, int) else f"\\frac{{{rem - 2}}}{{{b}}}", 
                    f"{-y_val}" if isinstance(y_val, int) else "0"]
            sol = f"**Step 1: Substitute x**\n\\({a}({x_val}) + ({b})y = {c} \\implies {a * x_val} + ({b})y = {c}\\).\n\\({b}y = {rem} \\implies y = {y_val}\\).\n**Step 2: Conclusion**\n{y_val}."
        elif mode == 1:
            # Given y, find x
            y_val = (idx % 3)
            rem = c - b * y_val
            x_val = rem // a if rem % a == 0 else f"\\frac{{{rem}}}{{{a}}}"
            txt = prefix + f"For the graph of \\({eq_str}\\), determine the value of \\(x\\) when \\(y = {y_val}\\)."
            corr = f"{x_val}"
            dist = [f"{x_val + 3}" if isinstance(x_val, int) else f"\\frac{{{rem + 2}}}{{{a}}}", 
                    f"{x_val - 2}" if isinstance(x_val, int) else f"\\frac{{{rem - 1}}}{{{a}}}", 
                    f"{-x_val}" if isinstance(x_val, int) else "1"]
            sol = f"**Step 1: Substitute y**\n\\({a}x + ({b})({y_val}) = {c} \\implies {a}x + {b * y_val} = {c}\\).\n\\({a}x = {rem} \\implies x = {x_val}\\).\n**Step 2: Conclusion**\n{x_val}."
        elif mode == 2:
            # X-intercept
            x_int = c // a if c % a == 0 else f"\\frac{{{c}}}{{{a}}}"
            txt = prefix + f"Find the X-intercept coordinates where the line \\({eq_str}\\) meets the horizontal axis."
            corr = f"\\(({x_int}, 0)\\)"
            dist = [f"\\((0, {x_int})\\)", f"\\(({x_int}, 1)\\)", f"\\((0, 0)\\)"]
            sol = f"**Step 1: Put y = 0**\n\\({a}x + 0 = {c} \\implies x = {x_int}\\).\nPoint is \\(({x_int}, 0)\\).\n**Step 2: Conclusion**\n\\(({x_int}, 0)\\)."
        elif mode == 3:
            # Y-intercept
            y_int = c // b if c % b == 0 else f"\\frac{{{c}}}{{{b}}}"
            txt = prefix + f"Determine the Y-intercept coordinates of the linear graph \\({eq_str}\\)."
            corr = f"\\((0, {y_int})\\)"
            dist = [f"\\(({y_int}, 0)\\)", f"\\((1, {y_int})\\)", f"\\((0, 0)\\)"]
            sol = f"**Step 1: Put x = 0**\n\\(0 + ({b})y = {c} \\implies y = {y_int}\\).\nPoint is \\((0, {y_int})\\).\n**Step 2: Conclusion**\n\\((0, {y_int})\\)."
        elif mode == 4:
            txt = prefix + f"How many distinct coordinate pairs \\((x, y)\\) satisfy the linear equation \\({eq_str}\\)?"
            corr = "Infinitely many pairs"
            dist = ["Only one pair", "Exactly two pairs", "Zero pairs"]
            sol = f"**Step 1: Concept**\nA line consists of infinitely many points; each point on the line is a solution.\n**Step 2: Conclusion**\nInfinitely many pairs."
        elif mode == 5:
            txt = prefix + f"What geometric curve is formed by plotting all solutions of \\({eq_str}\\) on a graph sheet?"
            corr = "A straight line"
            dist = ["A circle", "A parabola", "An angle"]
            sol = f"**Step 1: Degree of equation**\nA first-degree equation in two variables \\(ax + by = c\\) always graphs as a straight line.\n**Step 2: Conclusion**\nA straight line."
        elif mode == 6:
            txt = prefix + f"To plot the line \\({eq_str}\\) with verified collinearity, what is the minimum recommended number of points to calculate?"
            corr = "At least 3 points"
            dist = ["Only 1 point", "At least 10 points", "At least 5 points"]
            sol = f"**Step 1: Practical plotting rule**\nWhile two points define a line, a third point verifies collinearity and avoids calculation errors.\n**Step 2: Conclusion**\nAt least 3 points."
        else:
            # Check origin
            passes_origin = (c == 0)
            txt = prefix + f"Does the straight line \\({eq_str}\\) pass through the origin \\(O(0, 0)\\)?"
            corr = "No, because the constant term \\(c \\neq 0\\)" if not passes_origin else "Yes, because constant term is 0"
            dist = ["Yes, because constant term is 0" if not passes_origin else "No, because the constant term \\(c \\neq 0\\)", "Only in Quadrant I", "Cannot be determined"]
            sol = f"**Step 1: Check origin (0, 0)**\nLHS \\(= {a}(0) + {b}(0) = 0\\), whereas RHS \\(= {c}\\). Since \\(0 \\neq {c}\\), it does not pass through origin.\n**Step 2: Conclusion**\n{corr}."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def main():
    all_qs = []
    print("Generating Chapter 7 flawless questions...")
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
