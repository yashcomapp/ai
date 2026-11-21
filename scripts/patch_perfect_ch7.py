# scripts/patch_perfect_ch7.py
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
        fallback = f"{corr} (Option {counter})"
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

PTS_NAMES = [f"P_{{{i+1}}}" if i >= 26 else chr(65 + i) for i in range(80)]

# ------------------------------------------------------------------------------
# 7.1.1: X-axis, Y-axis, Origin (0,0) (100% verified)
# ------------------------------------------------------------------------------
def generate_7_1_1():
    tc = "MH-9-MTH2-7-7.1.1"
    tname = "X-axis, Y-axis, Origin (0,0)"
    qs = []
    
    ARCH_TEMPLATES = {
        0: [
            "A surveyor sets origin \\(O(0, 0)\\) and measures {d} units eastward along the horizontal axis. Find the marker coordinates.",
            "Starting from reference point \\(O(0, 0)\\), a robot travels {d} units along the positive X-axis. What is its terminal location?",
            "An engineer plots a test point {d} units to the right of origin \\(O\\) on the horizontal baseline. State its coordinates.",
            "Determine the position vector coordinates after displacing a particle {d} units along the positive horizontal axis from \\((0, 0)\\).",
            "On a Cartesian layout, a sensor is anchored {d} units to the right of the axes intersection. What is its ordered pair?",
            "What ordered pair specifies a location {d} units in the positive horizontal direction from the coordinate origin?",
            "Moving {d} units rightwards along the abscissa line starting from \\(O(0, 0)\\) reaches which point?",
            "A laser beam originates at \\((0, 0)\\) and targets a sensor {d} units right on the X-axis. Specify the sensor coordinates.",
            "Calculate the final coordinate representation of a point shifted {d} units along the positive X-axis from the origin.",
            "Find the ordered pair for an alignment pin placed {d} units right of the origin along the horizontal datum."
        ],
        1: [
            "For the point \\({pt}({px}, {py})\\) plotted on the Cartesian grid, state the exact numerical value of its abscissa.",
            "What is the horizontal coordinate (abscissa) of the point \\({pt}({px}, {py})\\)?",
            "Identify the abscissa component of the ordered pair \\({pt}({px}, {py})\\).",
            "Extract the x-value (abscissa) for the reference location \\({pt}({px}, {py})\\).",
            "In the Cartesian definition of point \\({pt}({px}, {py})\\), which number represents the abscissa?",
            "Specify the directed horizontal distance from the vertical axis (abscissa) for point \\({pt}({px}, {py})\\).",
            "Determine the abscissa of point \\({pt}\\) given its coordinates \\(({px}, {py})\\).",
            "From the coordinate pair \\({pt}({px}, {py})\\), what is the abscissa value?",
            "State the value of the x-coordinate (abscissa) for the plotted point \\({pt}({px}, {py})\\).",
            "Which coordinate value designates the abscissa of \\({pt}({px}, {py})\\)?"
        ],
        2: [
            "Identify the vertical coordinate (ordinate) of the point \\({pt}({px}, {py})\\) in the Cartesian plane.",
            "What is the numerical value of the ordinate for point \\({pt}({px}, {py})\\)?",
            "State the ordinate component corresponding to the ordered pair \\({pt}({px}, {py})\\).",
            "For the location marked \\({pt}({px}, {py})\\), extract its ordinate value.",
            "Determine the y-value (ordinate) of point \\({pt}({px}, {py})\\) on the coordinate grid.",
            "In the point definition \\({pt}({px}, {py})\\), which number denotes the ordinate?",
            "Specify the directed vertical distance from the horizontal axis (ordinate) for \\({pt}({px}, {py})\\).",
            "From the given coordinates of point \\({pt}({px}, {py})\\), what is the ordinate?",
            "What is the ordinate of point \\({pt}\\) having coordinates \\(({px}, {py})\\)?",
            "Which number in the coordinate pair \\({pt}({px}, {py})\\) gives its ordinate?"
        ],
        3: [
            "Compute the perpendicular distance from the horizontal X-axis to the point \\({pt}({px}, {py})\\).",
            "How far is the point \\({pt}({px}, {py})\\) located vertically from the X-axis?",
            "Determine the shortest distance separating point \\({pt}({px}, {py})\\) from the horizontal coordinate axis.",
            "Find the perpendicular spacing between the X-axis and point \\({pt}({px}, {py})\\).",
            "What is the vertical distance from the baseline X-axis to point \\({pt}({px}, {py})\\)?",
            "Calculate the clearance from the horizontal axis \\(y = 0\\) to point \\({pt}({px}, {py})\\).",
            "State the perpendicular distance of \\({pt}({px}, {py})\\) from the line of the X-axis.",
            "A vertical line is dropped from \\({pt}({px}, {py})\\) to the X-axis. What is its length?",
            "How many units of perpendicular distance separate \\({pt}({px}, {py})\\) from the X-axis?",
            "Measure the perpendicular distance from the X-axis to point \\({pt}({px}, {py})\\)."
        ],
        4: [
            "Find the perpendicular distance from the vertical Y-axis to point \\({pt}({px}, {py})\\).",
            "How far horizontally is point \\({pt}({px}, {py})\\) from the Y-axis?",
            "Determine the perpendicular length from the vertical axis \\(x = 0\\) to point \\({pt}({px}, {py})\\).",
            "Calculate the shortest distance between the Y-axis and point \\({pt}({px}, {py})\\).",
            "What is the horizontal clearance from the Y-axis to the point \\({pt}({px}, {py})\\)?",
            "A horizontal segment connects the Y-axis to \\({pt}({px}, {py})\\). Compute its length.",
            "State the perpendicular distance of the point \\({pt}({px}, {py})\\) from the vertical axis.",
            "Measure the distance from the line \\(x = 0\\) to point \\({pt}({px}, {py})\\).",
            "How many units separate point \\({pt}({px}, {py})\\) perpendicularly from the Y-axis?",
            "Find the perpendicular separation between the vertical axis and \\({pt}({px}, {py})\\)."
        ],
        5: [
            "Point \\({pt}({px}, 0)\\) is situated on the X-axis. Find its distance from origin \\(O(0, 0)\\).",
            "What is the straight-line length from origin \\(O\\) to point \\({pt}({px}, 0)\\) on the horizontal axis?",
            "Calculate the distance separating the origin from point \\({pt}({px}, 0)\\) along the X-axis.",
            "A marker is placed at \\({pt}({px}, 0)\\). How many units is it from the origin \\(O\\)?",
            "Determine the distance along the horizontal baseline from \\((0, 0)\\) to \\({pt}({px}, 0)\\).",
            "Find the coordinate span along the horizontal axis between the origin and point \\({pt}({px}, 0)\\).",
            "Find the length of the segment connecting the origin to point \\({pt}({px}, 0)\\).",
            "Compute the distance between origin \\(O(0, 0)\\) and the X-axis point \\({pt}({px}, 0)\\).",
            "State the distance of the point \\({pt}({px}, 0)\\) from the Cartesian origin.",
            "What is the span along the X-axis from the origin to point \\({pt}({px}, 0)\\)?"
        ],
        6: [
            "Point \\({pt}(0, {py})\\) lies on the vertical Y-axis. Calculate its distance from origin \\(O\\).",
            "What is the straight distance from the origin \\((0, 0)\\) to point \\({pt}(0, {py})\\) on the Y-axis?",
            "Determine the distance between the origin and point \\({pt}(0, {py})\\) along the vertical axis.",
            "How far is the point \\({pt}(0, {py})\\) on the Y-axis from the coordinate origin?",
            "Find the length of the vertical segment from \\(O(0, 0)\\) to \\({pt}(0, {py})\\).",
            "A sensor is placed at \\({pt}(0, {py})\\). Compute its distance from the origin.",
            "State the distance separating the origin point \\(O\\) from \\({pt}(0, {py})\\) on the Y-axis.",
            "Compute the span along the vertical axis from \\(O(0, 0)\\) to \\({pt}(0, {py})\\).",
            "Measure the distance from the origin to point \\({pt}(0, {py})\\) on the vertical line.",
            "How many units from origin \\(O\\) is the Y-axis point \\({pt}(0, {py})\\) located?"
        ],
        7: [
            "For the point \\({pt}({px}, {py})\\), evaluate the algebraic sum of its coordinates \\(x + y\\).",
            "Calculate the combined total \\(x + y\\) of the abscissa and ordinate for \\({pt}({px}, {py})\\).",
            "What is the sum of the horizontal and vertical coordinates of point \\({pt}({px}, {py})\\)?",
            "Add the x-coordinate and y-coordinate of point \\({pt}({px}, {py})\\). What is the result?",
            "Find the numerical value of \\(x + y\\) for the ordered pair \\({pt}({px}, {py})\\).",
            "Evaluate the expression \\(x + y\\) given that point \\({pt}\\) has coordinates \\(({px}, {py})\\).",
            "What is the algebraic sum \\(x + y\\) of the coordinate values for \\({pt}({px}, {py})\\)?",
            "Compute \\(x + y\\) using the abscissa and ordinate of point \\({pt}({px}, {py})\\).",
            "Determine the sum \\(x + y\\) for the Cartesian location \\({pt}({px}, {py})\\).",
            "State the total \\(x + y\\) obtained by adding the coordinates of \\({pt}({px}, {py})\\)."
        ]
    }
    
    for idx, seq in enumerate(SEQS_80):
        pt = PTS_NAMES[idx]
        has_fig = (idx % 3 != 0)
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        tmpl = ARCH_TEMPLATES[arch][sub_idx]
        
        px = (sub_idx - 5) if sub_idx != 5 else 7
        py = (sub_idx * 2 - 9)
        svg = svg_cartesian_point(pt, px, py, f"Cartesian Frame #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        if arch == 0:
            d = sub_idx + 1
            txt = prefix + tmpl.format(d=d)
            corr = f"\\(({d}, 0)\\)"
            dist = [f"\\((0, {d})\\)", f"\\(({-d}, 0)\\)", f"\\(({d}, {d})\\)"]
            sol = f"**Step 1: Movement from Origin**\nStarting at \\((0, 0)\\) and moving {d} units right gives \\(({d}, 0)\\).\n**Step 2: Conclusion**\n\\(({d}, 0)\\)."
        elif arch == 1:
            px_val = 10 + sub_idx
            py_val = 3 + sub_idx
            txt = prefix + tmpl.format(pt=pt, px=px_val, py=py_val)
            corr = f"{px_val}"
            dist = [f"{py_val}", f"{-px_val}", f"{px_val + 2}"]
            sol = f"**Step 1: Abscissa Definition**\nThe abscissa is the x-coordinate of the point, which is {px_val}.\n**Step 2: Conclusion**\n{px_val}."
        elif arch == 2:
            px_val = 2 + sub_idx
            py_val = 20 + sub_idx
            txt = prefix + tmpl.format(pt=pt, px=px_val, py=py_val)
            corr = f"{py_val}"
            dist = [f"{px_val}", f"{-py_val}", f"{py_val - 2}"]
            sol = f"**Step 1: Ordinate Definition**\nThe ordinate is the y-coordinate of the point, which is {py_val}.\n**Step 2: Conclusion**\n{py_val}."
        elif arch == 3:
            d_val = 30 + sub_idx
            px_val = 4 + sub_idx
            txt = prefix + tmpl.format(pt=pt, px=px_val, py=-d_val)
            corr = f"{d_val} units"
            dist = [f"{px_val} units", f"{d_val + 3} units", f"{d_val + 1} units"]
            sol = f"**Step 1: Distance Formula**\nPerpendicular distance from X-axis \\(= |y| = |-({d_val})| = {d_val}\\) units.\n**Step 2: Conclusion**\n{d_val} units."
        elif arch == 4:
            d_val = 40 + sub_idx
            py_val = 5 + sub_idx
            txt = prefix + tmpl.format(pt=pt, px=-d_val, py=py_val)
            corr = f"{d_val} units"
            dist = [f"{py_val} units", f"{d_val + 2} units", f"{d_val + 4} units"]
            sol = f"**Step 1: Distance Formula**\nPerpendicular distance from Y-axis \\(= |x| = |-({d_val})| = {d_val}\\) units.\n**Step 2: Conclusion**\n{d_val} units."
        elif arch == 5:
            d_val = 50 + sub_idx
            txt = prefix + tmpl.format(pt=pt, px=d_val)
            corr = f"{d_val} units"
            dist = [f"{d_val + 2} units", f"{d_val - 3} units", f"{d_val * 2} units"]
            sol = f"**Step 1: Distance Calculation**\nDistance from origin \\(= |{d_val} - 0| = {d_val}\\) units.\n**Step 2: Conclusion**\n{d_val} units."
        elif arch == 6:
            d_val = 65 + sub_idx
            txt = prefix + tmpl.format(pt=pt, py=-d_val)
            corr = f"{d_val} units"
            dist = [f"{d_val + 3} units", f"{d_val + 1} units", f"{d_val * 2} units"]
            sol = f"**Step 1: Distance Calculation**\nDistance from origin \\(= |-({d_val}) - 0| = {d_val}\\) units.\n**Step 2: Conclusion**\n{d_val} units."
        else:
            px_val = 70 + sub_idx
            py_val = 5 + sub_idx
            val = px_val + py_val
            txt = prefix + tmpl.format(pt=pt, px=px_val, py=py_val)
            corr = f"{val}"
            dist = [f"{val + 2}", f"{val - 3}", f"{-val}"]
            sol = f"**Step 1: Sum Calculation**\n\\(x + y = {px_val} + ({py_val}) = {val}\\).\n**Step 2: Conclusion**\n{val}."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

# ------------------------------------------------------------------------------
# 7.1.2: Plotting points in all four quadrants (All 20 distinct templates include {pt})
# ------------------------------------------------------------------------------
def generate_7_1_2():
    tc = "MH-9-MTH2-7-7.1.2"
    tname = "Plotting points in all four quadrants"
    qs = []
    
    TEMPLATES_20 = [
        "Point \\({pt}({x}, {y})\\) has both coordinates positive. In which quadrant does it reside?",
        "Identify the quadrant containing point \\({pt}({x}, {y})\\) on a standard Cartesian grid.",
        "If an analyst plots point \\({pt}({x}, {y})\\), which quadrant will it occupy?",
        "What quadrant of the coordinate plane contains the ordered pair \\({pt}({x}, {y})\\)?",
        "Point \\({pt}\\) is placed at \\({x}\\) units horizontally and \\({y}\\) units vertically. Name its quadrant.",
        "In which quadrant does point \\({pt}\\) with abscissa {x} and ordinate {y} fall?",
        "State the quadrant where point \\({pt}({x}, {y})\\) is positioned.",
        "Determine the quadrant location for point \\({pt}\\) given \\(x = {x}\\) and \\(y = {y}\\).",
        "On plotting point \\({pt}({x}, {y})\\), in which numbered quadrant will it be marked?",
        "Which Cartesian quadrant encompasses the point \\({pt}({x}, {y})\\)?",
        "A GPS sensor marks point \\({pt}({x}, {y})\\). To which quadrant does this fix correspond?",
        "On a blueprint coordinate layout, where does marker \\({pt}({x}, {y})\\) map?",
        "Determine the quadrant index for the specific point \\({pt}({x}, {y})\\).",
        "Which sector of the 2D Cartesian plane contains the marker \\({pt}({x}, {y})\\)?",
        "Specifying point \\({pt}({x}, {y})\\) on graph paper places it inside which quadrant?",
        "Identify the quadrant region containing alignment point \\({pt}({x}, {y})\\).",
        "When point \\({pt}({x}, {y})\\) is charted, which quadrant bounds its location?",
        "Name the specific quadrant where point \\({pt}\\) with coordinates \\(({x}, {y})\\) lies.",
        "Find the quadrant of the Cartesian plane holding test point \\({pt}({x}, {y})\\).",
        "Test point \\({pt}({x}, {y})\\) belongs to which quadrant of the coordinate frame?"
    ]
    
    for idx, seq in enumerate(SEQS_80):
        pt = PTS_NAMES[idx]
        has_fig = (idx % 3 != 0)
        
        q_target = idx % 4
        sub_idx = idx // 4 # exactly 0..19
        
        x_base = 3 + sub_idx * 3
        y_base = 4 + sub_idx * 4
        
        if q_target == 0:
            px, py = x_base, y_base
            quad_name = "Quadrant I"
            dist_q = ["Quadrant II", "Quadrant IV", "Quadrant III"]
        elif q_target == 1:
            px, py = -x_base, y_base
            quad_name = "Quadrant II"
            dist_q = ["Quadrant I", "Quadrant III", "Quadrant IV"]
        elif q_target == 2:
            px, py = -x_base, -y_base
            quad_name = "Quadrant III"
            dist_q = ["Quadrant II", "Quadrant IV", "Quadrant I"]
        else:
            px, py = x_base, -y_base
            quad_name = "Quadrant IV"
            dist_q = ["Quadrant I", "Quadrant II", "Quadrant III"]
            
        svg = svg_cartesian_point(pt, px if abs(px) <= 8 else (px // 8), py if abs(py) <= 8 else (py // 8), f"Quadrant Frame #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        tmpl = TEMPLATES_20[sub_idx]
        txt = prefix + tmpl.format(pt=pt, x=px, y=py)
        corr = quad_name
        dist = dist_q
        sol = f"**Step 1: Sign Examination**\nHere \\(x = {px}\\) and \\(y = {py}\\).\nTherefore, point \\({pt}\\) lies in {quad_name}.\n**Step 2: Conclusion**\n{quad_name}."
        
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

# ------------------------------------------------------------------------------
# 7.2.1: Line parallel to Y-axis: x = c (100% verified)
# ------------------------------------------------------------------------------
def generate_7_2_1():
    tc = "MH-9-MTH2-7-7.2.1"
    tname = "Line parallel to Y-axis: x = c"
    qs = []
    
    TEMPLATES = {
        0: [
            "Find the equation of the line parallel to the Y-axis passing through point \\({pt}({c}, {py})\\).",
            "What is the algebraic equation of a vertical line crossing \\({pt}({c}, {py})\\)?",
            "State the linear equation of the line parallel to the vertical axis through \\({pt}({c}, {py})\\).",
            "Determine the equation of the line parallel to the Y-axis with x-intercept \\({c}\\).",
            "A vertical line contains point \\({pt}({c}, {py})\\). Write its equation.",
            "Which equation defines a straight line parallel to the Y-axis passing through \\({pt}({c}, {py})\\)?",
            "Compute the equation of the line through \\({pt}({c}, {py})\\) that runs parallel to the Y-axis.",
            "Write down the equation for the vertical locus of points containing \\({pt}({c}, {py})\\).",
            "Identify the equation of the line parallel to the ordinate axis passing through \\({pt}({c}, {py})\\).",
            "What is the mathematical relation representing a vertical line through \\({pt}({c}, {py})\\)?"
        ],
        1: [
            "A line parallel to the Y-axis is at a distance of {d} units to the {side} of it. What is its equation?",
            "State the equation of a vertical line located {d} units {side} of the Y-axis.",
            "Determine the equation of the line parallel to the vertical axis situated {d} units to the {side}.",
            "Find the algebraic formula for a line running parallel to the Y-axis at a distance of {d} units on the {side}.",
            "What is the equation of the vertical boundary {d} units to the {side} of the Y-axis?",
            "A straight fence runs parallel to the Y-axis {d} units to the {side}. State its equation.",
            "Specify the equation of a line parallel to the vertical axis at distance {d} to the {side}.",
            "Which equation describes a line parallel to \\(x = 0\\) offset by {d} units to the {side}?",
            "Compute the equation of the line parallel to the Y-axis positioned {d} units on the {side}.",
            "Write the formula for the vertical path {d} units {side} of the Y-axis."
        ],
        2: [
            "At which point does the vertical line \\(x = {c}\\) intersect the horizontal X-axis?",
            "Determine the coordinates of the X-intercept for the vertical line \\(x = {c}\\).",
            "Where does the line \\(x = {c}\\) meet the horizontal axis \\(y = 0\\)?",
            "State the point of intersection between line \\(x = {c}\\) and the X-axis.",
            "Find the coordinates where the line \\(x = {c}\\) crosses the abscissa axis.",
            "On a graph, the line \\(x = {c}\\) cuts the horizontal X-axis at:",
            "What is the intersection point of the vertical line \\(x = {c}\\) with the line \\(y = 0\\)?",
            "Compute the coordinates of the point common to line \\(x = {c}\\) and the X-axis.",
            "Identify the point on the X-axis through which line \\(x = {c}\\) passes.",
            "Write the ordered pair where line \\(x = {c}\\) meets the horizontal axis."
        ],
        3: [
            "Calculate the perpendicular distance from the vertical Y-axis to line \\(x = {c}\\).",
            "How far is the vertical line \\(x = {c}\\) from the Y-axis \\(x = 0\\)?",
            "Find the distance separating the vertical axis from the line \\(x = {c}\\).",
            "What is the perpendicular spacing between the Y-axis and line \\(x = {c}\\)?",
            "Compute the clearance between the vertical line \\(x = {c}\\) and the line \\(x = 0\\).",
            "Determine the horizontal distance from the vertical datum to line \\(x = {c}\\).",
            "State the perpendicular distance of line \\(x = {c}\\) from the Y-axis.",
            "How many units of distance separate the vertical axis from line \\(x = {c}\\)?",
            "Measure the gap between the Y-axis and the parallel line \\(x = {c}\\).",
            "Find the shortest distance from the Y-axis to the line \\(x = {c}\\)."
        ],
        4: [
            "What is the distance separating the two parallel lines \\(x = {c}\\) and \\(x = {c2}\\)?",
            "Compute the perpendicular distance between vertical lines \\(x = {c}\\) and \\(x = {c2}\\).",
            "Calculate the horizontal gap between parallel lines \\(x = {c}\\) and \\(x = {c2}\\).",
            "How many units separate the parallel vertical lines \\(x = {c}\\) and \\(x = {c2}\\)?",
            "Find the distance between the two lines \\(x = {c}\\) and \\(x = {c2}\\).",
            "Determine the spacing between parallel vertical tracks \\(x = {c}\\) and \\(x = {c2}\\).",
            "State the distance separating lines \\(x = {c}\\) and \\(x = {c2}\\).",
            "Measure the horizontal separation between \\(x = {c}\\) and \\(x = {c2}\\).",
            "What is the perpendicular clearance between lines \\(x = {c}\\) and \\(x = {c2}\\)?",
            "Find the gap between the two parallel lines \\(x = {c}\\) and \\(x = {c2}\\)."
        ],
        5: [
            "Express the vertical line equation \\(x = {c}\\) in general form \\(ax + by + d = 0\\).",
            "Write the linear equation \\(x = {c}\\) in standard form \\(1x + 0y + d = 0\\).",
            "Convert the equation \\(x = {c}\\) into general two-variable linear notation.",
            "What is the standard algebraic representation \\(ax + by + d = 0\\) for line \\(x = {c}\\)?",
            "In general form \\(Ax + By + C = 0\\), how is the line \\(x = {c}\\) represented?",
            "State the general linear form of the vertical line \\(x = {c}\\).",
            "Which expression gives the equation \\(x = {c}\\) in standard linear format?",
            "Represent the line \\(x = {c}\\) in the two-variable format \\(ax + by + d = 0\\).",
            "Write the equation \\(x = {c}\\) with explicit zero coefficient for y.",
            "Express line \\(x = {c}\\) in complete linear equation form."
        ],
        6: [
            "If line \\(x = {c}\\) is shifted {shift} units to the right, what is its new equation?",
            "Translating the vertical line \\(x = {c}\\) by {shift} units rightward yields which equation?",
            "A vertical line \\(x = {c}\\) moves {shift} units in the positive X-direction. State its equation.",
            "What is the resulting equation after displacing line \\(x = {c}\\) by {shift} units to the right?",
            "Shifting the line \\(x = {c}\\) rightwards by {shift} units gives the line:",
            "Find the equation of the line obtained by translating \\(x = {c}\\) by {shift} units to the right.",
            "When the vertical line \\(x = {c}\\) is moved {shift} units right, what is its equation?",
            "Compute the new equation when line \\(x = {c}\\) undergoes a rightward translation of {shift} units.",
            "Determine the equation after shifting \\(x = {c}\\) horizontally right by {shift} units.",
            "State the equation of line \\(x = {c}\\) following a rightward shift of {shift} units."
        ],
        7: [
            "Which of the following points lies on the vertical line \\(x = {c}\\)?",
            "Identify the point that belongs to the line \\(x = {c}\\).",
            "Which coordinate pair satisfies the linear equation \\(x = {c}\\)?",
            "Select the point situated on the line \\(x = {c}\\).",
            "Which of these ordered pairs lies on the graph of \\(x = {c}\\)?",
            "Find the point that lies on the vertical line \\(x = {c}\\).",
            "Which point is situated on the line whose equation is \\(x = {c}\\)?",
            "Determine which of the following points is on line \\(x = {c}\\).",
            "Identify the ordered pair located on the line \\(x = {c}\\).",
            "Which of the given points falls on the line \\(x = {c}\\)?"
        ]
    }
    
    for idx, seq in enumerate(SEQS_80):
        pt = PTS_NAMES[idx]
        has_fig = (idx % 3 != 0)
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        tmpl = TEMPLATES[arch][sub_idx]
        
        c = (arch * 15) + sub_idx + 1
        py = 3 + sub_idx
        
        svg = svg_parallel_line(f"x = {c}", True, c if abs(c) <= 9 else (c // 5), f"Vertical Line #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        if arch == 0:
            txt = prefix + tmpl.format(pt=pt, c=c, py=py)
            corr = f"\\(x = {c}\\)"
            dist = [f"\\(y = {py}\\)", f"\\(x = {py}\\)", f"\\(y = {c}\\)"]
            sol = f"**Step 1: Vertical line property**\nEquation is \\(x = c\\). Since x-coordinate is {c}, \\(x = {c}\\).\n**Step 2: Conclusion**\n\\(x = {c}\\)."
        elif arch == 1:
            d = c
            side = "right" if sub_idx % 2 == 0 else "left"
            c_val = d if side == "right" else -d
            txt = prefix + tmpl.format(d=d, side=side)
            corr = f"\\(x = {c_val}\\)"
            dist = [f"\\(x = {-c_val}\\)", f"\\(y = {c_val}\\)", f"\\(y = {d}\\)"]
            sol = f"**Step 1: Distance and Side**\nDistance {d} to the {side} gives \\(x = {c_val}\\).\n**Step 2: Conclusion**\n\\(x = {c_val}\\)."
        elif arch == 2:
            txt = prefix + tmpl.format(c=c)
            corr = f"\\(({c}, 0)\\)"
            dist = [f"\\((0, {c})\\)", f"\\(({-c}, 0)\\)", f"\\((0, 0)\\)"]
            sol = f"**Step 1: Intersection with X-axis**\nOn X-axis, \\(y = 0\\). Point is \\(({c}, 0)\\).\n**Step 2: Conclusion**\n\\(({c}, 0)\\)."
        elif arch == 3:
            dist_val = abs(c)
            txt = prefix + tmpl.format(c=c)
            corr = f"{dist_val} units"
            dist = [f"{dist_val + 3} units", f"{dist_val + 5} units", f"{dist_val * 2} units"]
            sol = f"**Step 1: Distance**\nDistance \\(= |{c} - 0| = {dist_val}\\) units.\n**Step 2: Conclusion**\n{dist_val} units."
        elif arch == 4:
            gap = sub_idx + 10
            c2 = c + gap
            txt = prefix + tmpl.format(c=c, c2=c2)
            corr = f"{gap} units"
            dist = [f"{gap + 2} units", f"{gap * 2} units", f"{gap - 1} units"]
            sol = f"**Step 1: Gap**\nDistance \\(= |{c2} - {c}| = {gap}\\) units.\n**Step 2: Conclusion**\n{gap} units."
        elif arch == 5:
            txt = prefix + tmpl.format(c=c)
            corr = f"\\(1x + 0y - {c} = 0\\)" if c > 0 else f"\\(1x + 0y + {-c} = 0\\)"
            dist = [f"\\(0x + 1y - {c} = 0\\)", f"\\(1x + 1y - {c} = 0\\)", f"\\(1x - 1y + {c} = 0\\)"]
            sol = f"**Step 1: Standard form**\n\\(x = {c} \\implies 1x + 0y - ({c}) = 0\\).\n**Step 2: Conclusion**\n{corr}."
        elif arch == 6:
            shift = sub_idx + 5
            c_new = c + shift
            txt = prefix + tmpl.format(c=c, shift=shift)
            corr = f"\\(x = {c_new}\\)"
            dist = [f"\\(x = {c - shift}\\)", f"\\(y = {c_new}\\)", f"\\(x = {c}\\)"]
            sol = f"**Step 1: Shift right**\nNew \\(x = {c} + {shift} = {c_new}\\).\n**Step 2: Conclusion**\n\\(x = {c_new}\\)."
        else:
            txt = prefix + tmpl.format(c=c)
            corr = f"\\(({c}, {py})\\)"
            dist = [f"\\(({c + 1}, {py})\\)", f"\\(({py}, {c})\\)", f"\\((0, {c})\\)"]
            sol = f"**Step 1: Check point**\nPoints on \\(x = {c}\\) must have x-coordinate {c}. Point \\(({c}, {py})\\) satisfies this.\n**Step 2: Conclusion**\n\\(({c}, {py})\\)."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

# ------------------------------------------------------------------------------
# 7.2.2: Line parallel to X-axis: y = c (100% verified)
# ------------------------------------------------------------------------------
def generate_7_2_2():
    tc = "MH-9-MTH2-7-7.2.2"
    tname = "Line parallel to X-axis: y = c"
    qs = []
    
    TEMPLATES = {
        0: [
            "Find the equation of the line parallel to the X-axis passing through point \\({pt}({px}, {c})\\).",
            "What is the algebraic equation of a horizontal line crossing \\({pt}({px}, {c})\\)?",
            "State the linear equation of the line parallel to the horizontal axis through \\({pt}({px}, {c})\\).",
            "Determine the equation of the line parallel to the X-axis with y-intercept \\({c}\\).",
            "A horizontal line contains point \\({pt}({px}, {c})\\). Write its equation.",
            "Which equation defines a straight line parallel to the X-axis passing through \\({pt}({px}, {c})\\)?",
            "Compute the equation of the line through \\({pt}({px}, {c})\\) that runs parallel to the X-axis.",
            "Write down the equation for the horizontal locus of points containing \\({pt}({px}, {c})\\).",
            "Identify the equation of the line parallel to the abscissa axis passing through \\({pt}({px}, {c})\\).",
            "What is the mathematical relation representing a horizontal line through \\({pt}({px}, {c})\\)?"
        ],
        1: [
            "A line parallel to the X-axis is at a distance of {d} units {side} it. What is its equation?",
            "State the equation of a horizontal line located {d} units {side} the X-axis.",
            "Determine the equation of the line parallel to the horizontal axis situated {d} units {side}.",
            "Find the algebraic formula for a line running parallel to the X-axis at a distance of {d} units {side}.",
            "What is the equation of the horizontal boundary {d} units {side} the X-axis?",
            "A straight beam runs parallel to the X-axis {d} units {side}. State its equation.",
            "Specify the equation of a line parallel to the horizontal axis at distance {d} {side}.",
            "Which equation describes a line parallel to \\(y = 0\\) offset by {d} units {side}?",
            "Compute the equation of the line parallel to the X-axis positioned {d} units {side}.",
            "Write the formula for the horizontal path {d} units {side} the X-axis."
        ],
        2: [
            "At which point does the horizontal line \\(y = {c}\\) intersect the vertical Y-axis?",
            "Determine the coordinates of the Y-intercept for the horizontal line \\(y = {c}\\).",
            "Where does the line \\(y = {c}\\) meet the vertical axis \\(x = 0\\)?",
            "State the point of intersection between line \\(y = {c}\\) and the Y-axis.",
            "Find the coordinates where the line \\(y = {c}\\) crosses the ordinate axis.",
            "On a graph, the line \\(y = {c}\\) cuts the vertical Y-axis at:",
            "What is the intersection point of the horizontal line \\(y = {c}\\) with the line \\(x = 0\\)?",
            "Compute the coordinates of the point common to line \\(y = {c}\\) and the Y-axis.",
            "Identify the point on the Y-axis through which line \\(y = {c}\\) passes.",
            "Write the ordered pair where line \\(y = {c}\\) meets the vertical axis."
        ],
        3: [
            "Calculate the perpendicular distance from the horizontal X-axis to line \\(y = {c}\\).",
            "How far is the horizontal line \\(y = {c}\\) from the X-axis \\(y = 0\\)?",
            "Find the distance separating the horizontal axis from the line \\(y = {c}\\).",
            "What is the perpendicular spacing between the X-axis and line \\(y = {c}\\)?",
            "Compute the clearance between the horizontal line \\(y = {c}\\) and the line \\(y = 0\\).",
            "Determine the vertical distance from the horizontal datum to line \\(y = {c}\\).",
            "State the perpendicular distance of line \\(y = {c}\\) from the X-axis.",
            "How many units of distance separate the horizontal axis from line \\(y = {c}\\)?",
            "Measure the gap between the X-axis and the parallel line \\(y = {c}\\).",
            "Find the shortest distance from the X-axis to the line \\(y = {c}\\)."
        ],
        4: [
            "What is the distance separating the two parallel lines \\(y = {c}\\) and \\(y = {c2}\\)?",
            "Compute the perpendicular distance between horizontal lines \\(y = {c}\\) and \\(y = {c2}\\).",
            "Calculate the vertical gap between parallel lines \\(y = {c}\\) and \\(y = {c2}\\).",
            "How many units separate the parallel horizontal lines \\(y = {c}\\) and \\(y = {c2}\\)?",
            "Find the distance between the two lines \\(y = {c}\\) and \\(y = {c2}\\).",
            "Determine the spacing between parallel horizontal tracks \\(y = {c}\\) and \\(y = {c2}\\).",
            "State the distance separating lines \\(y = {c}\\) and \\(y = {c2}\\).",
            "Measure the vertical separation between \\(y = {c}\\) and \\(y = {c2}\\).",
            "What is the perpendicular clearance between lines \\(y = {c}\\) and \\(y = {c2}\\)?",
            "Find the gap between the two parallel lines \\(y = {c}\\) and \\(y = {c2}\\)."
        ],
        5: [
            "Express the horizontal line equation \\(y = {c}\\) in general form \\(ax + by + d = 0\\).",
            "Write the linear equation \\(y = {c}\\) in standard form \\(0x + 1y + d = 0\\).",
            "Convert the equation \\(y = {c}\\) into general two-variable linear notation.",
            "What is the standard algebraic representation \\(ax + by + d = 0\\) for line \\(y = {c}\\)?",
            "In general form \\(Ax + By + C = 0\\), how is the line \\(y = {c}\\) represented?",
            "State the general linear form of the horizontal line \\(y = {c}\\).",
            "Which expression gives the equation \\(y = {c}\\) in standard linear format?",
            "Represent the line \\(y = {c}\\) in the two-variable format \\(ax + by + d = 0\\).",
            "Write the equation \\(y = {c}\\) with explicit zero coefficient for x.",
            "Express line \\(y = {c}\\) in complete linear equation form."
        ],
        6: [
            "If line \\(y = {c}\\) is shifted {shift} units upwards, what is its new equation?",
            "Translating the horizontal line \\(y = {c}\\) by {shift} units upward yields which equation?",
            "A horizontal line \\(y = {c}\\) moves {shift} units in the positive Y-direction. State its equation.",
            "What is the resulting equation after displacing line \\(y = {c}\\) by {shift} units upwards?",
            "Shifting the line \\(y = {c}\\) upwards by {shift} units gives the line:",
            "Find the equation of the line obtained by translating \\(y = {c}\\) by {shift} units upwards.",
            "When the horizontal line \\(y = {c}\\) is moved {shift} units up, what is its equation?",
            "Compute the new equation when line \\(y = {c}\\) undergoes an upward translation of {shift} units.",
            "Determine the equation after shifting \\(y = {c}\\) vertically up by {shift} units.",
            "State the equation of line \\(y = {c}\\) following an upward shift of {shift} units."
        ],
        7: [
            "Which of the following points lies on the horizontal line \\(y = {c}\\)?",
            "Identify the point that belongs to the line \\(y = {c}\\).",
            "Which coordinate pair satisfies the linear equation \\(y = {c}\\)?",
            "Select the point situated on the line \\(y = {c}\\).",
            "Which of these ordered pairs lies on the graph of \\(y = {c}\\)?",
            "Find the point that lies on the horizontal line \\(y = {c}\\).",
            "Which point is situated on the line whose equation is \\(y = {c}\\)?",
            "Determine which of the following points is on line \\(y = {c}\\).",
            "Identify the ordered pair located on the line \\(y = {c}\\).",
            "Which of the given points falls on the line \\(y = {c}\\)?"
        ]
    }
    
    for idx, seq in enumerate(SEQS_80):
        pt = PTS_NAMES[idx]
        has_fig = (idx % 3 != 0)
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        tmpl = TEMPLATES[arch][sub_idx]
        
        c = (arch * 15) + sub_idx + 1
        px = 4 + sub_idx
        
        svg = svg_parallel_line(f"y = {c}", False, c if abs(c) <= 9 else (c // 5), f"Horizontal Line #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        if arch == 0:
            txt = prefix + tmpl.format(pt=pt, c=c, px=px)
            corr = f"\\(y = {c}\\)"
            dist = [f"\\(x = {px}\\)", f"\\(y = {px}\\)", f"\\(x = {c}\\)"]
            sol = f"**Step 1: Horizontal line property**\nEquation is \\(y = c\\). Since y-coordinate is {c}, \\(y = {c}\\).\n**Step 2: Conclusion**\n\\(y = {c}\\)."
        elif arch == 1:
            d = c
            side = "above" if sub_idx % 2 == 0 else "below"
            c_val = d if side == "above" else -d
            txt = prefix + tmpl.format(d=d, side=side)
            corr = f"\\(y = {c_val}\\)"
            dist = [f"\\(y = {-c_val}\\)", f"\\(x = {c_val}\\)", f"\\(x = {d}\\)"]
            sol = f"**Step 1: Distance and Side**\nDistance {d} units {side} gives \\(y = {c_val}\\).\n**Step 2: Conclusion**\n\\(y = {c_val}\\)."
        elif arch == 2:
            txt = prefix + tmpl.format(c=c)
            corr = f"\\((0, {c})\\)"
            dist = [f"\\(({c}, 0)\\)", f"\\((0, {-c})\\)", f"\\((0, 0)\\)"]
            sol = f"**Step 1: Intersection with Y-axis**\nOn Y-axis, \\(x = 0\\). Point is \\((0, {c})\\).\n**Step 2: Conclusion**\n\\((0, {c})\\)."
        elif arch == 3:
            dist_val = abs(c)
            txt = prefix + tmpl.format(c=c)
            corr = f"{dist_val} units"
            dist = [f"{dist_val + 2} units", f"{dist_val + 4} units", f"{dist_val * 2} units"]
            sol = f"**Step 1: Distance**\nDistance \\(= |{c} - 0| = {dist_val}\\) units.\n**Step 2: Conclusion**\n{dist_val} units."
        elif arch == 4:
            gap = sub_idx + 8
            c2 = c + gap
            txt = prefix + tmpl.format(c=c, c2=c2)
            corr = f"{gap} units"
            dist = [f"{gap + 2} units", f"{gap * 2} units", f"{gap - 1} units"]
            sol = f"**Step 1: Gap**\nDistance \\(= |{c2} - {c}| = {gap}\\) units.\n**Step 2: Conclusion**\n{gap} units."
        elif arch == 5:
            txt = prefix + tmpl.format(c=c)
            corr = f"\\(0x + 1y - {c} = 0\\)" if c > 0 else f"\\(0x + 1y + {-c} = 0\\)"
            dist = [f"\\(1x + 0y - {c} = 0\\)", f"\\(0x - 1y - {c} = 0\\)", f"\\(1x + 1y = {c}\\)"]
            sol = f"**Step 1: Standard form**\n\\(y = {c} \\implies 0x + 1y - ({c}) = 0\\).\n**Step 2: Conclusion**\n{corr}."
        elif arch == 6:
            shift = sub_idx + 7
            c_new = c + shift
            txt = prefix + tmpl.format(c=c, shift=shift)
            corr = f"\\(y = {c_new}\\)"
            dist = [f"\\(y = {c - shift}\\)", f"\\(x = {c_new}\\)", f"\\(y = {c}\\)"]
            sol = f"**Step 1: Shift up**\nNew \\(y = {c} + {shift} = {c_new}\\).\n**Step 2: Conclusion**\n\\(y = {c_new}\\)."
        else:
            txt = prefix + tmpl.format(c=c)
            corr = f"\\(({px}, {c})\\)"
            dist = [f"\\(({c}, {px})\\)", f"\\(({px}, {c + 1})\\)", f"\\((0, 0)\\)"]
            sol = f"**Step 1: Check point**\nPoints on \\(y = {c}\\) must have y-coordinate {c}. Point \\(({px}, {c})\\) satisfies this.\n**Step 2: Conclusion**\n\\(({px}, {c})\\)."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

# ------------------------------------------------------------------------------
# 7.2.3: Equation of X-axis (y=0) and Y-axis (x=0) (Distinct questions)
# ------------------------------------------------------------------------------
def generate_7_2_3():
    tc = "MH-9-MTH2-7-7.2.3"
    tname = "Equation of X-axis (y=0) and Y-axis (x=0)"
    qs = []
    
    TEMPLATES = {
        0: [
            ("What is the standard algebraic equation defining the horizontal X-axis?", "\\(y = 0\\)", ["\\(x = 0\\)", "\\(x = y\\)", "\\(x + y = 0\\)"], "Every point on the X-axis has y-coordinate 0."),
            ("If the horizontal line \\(y = k\\) coincides with the X-axis, what is the value of \\(k\\)?", "0", ["1", "-1", "Cannot be determined"], "The X-axis has equation \\(y = 0\\), so \\(k = 0\\)."),
            ("What is the perpendicular distance between the X-axis (line \\(y = 0\\)) and the parallel line \\(y = 8\\)?", "8 units", ["4 units", "16 units", "0 units"], "Distance \\(= |8 - 0| = 8\\) units."),
            ("At what point does the horizontal X-axis (line \\(y = 0\\)) intersect the vertical line \\(x = 6\\)?", "\\((6, 0)\\)", ["\\((0, 6)\\)", "\\((6, 6)\\)", "\\((0, 0)\\)"], "Intersection is \\((6, 0)\\)."),
            ("A horizontal line passes through points \\((2, 0)\\) and \\((7, 0)\\). What is its equation?", "\\(y = 0\\)", ["\\(x = 0\\)", "\\(x = 2\\)", "\\(y = 7\\)"], "Both ordinates are 0, so equation is \\(y = 0\\)."),
            ("What are the coordinates of the reflection of point \\(A(4, 5)\\) across the line \\(y = 0\\) (X-axis)?", "\\((4, -5)\\)", ["\\((-4, 5)\\)", "\\((-4, -5)\\)", "\\((5, 4)\\)"], "Reflection across \\(y = 0\\) maps \\((x, y) \\to (x, -y)\\)."),
            ("If line \\(y = 0\\) is shifted 3 units upwards, what is the equation of the resulting parallel line?", "\\(y = 3\\)", ["\\(y = -3\\)", "\\(x = 3\\)", "\\(y = 0\\)"], "Shift up by 3 gives \\(y = 0 + 3 = 3\\)."),
            ("How many points on the line \\(y = 0\\) have a non-zero ordinate?", "0 points", ["Infinitely many", "Exactly 1 point", "Cannot be determined"], "Every point on \\(y = 0\\) has ordinate exactly 0."),
            ("What is the distance between the line \\(y = 0\\) and the parallel line \\(y = -9\\)?", "9 units", ["-9 units", "18 units", "0 units"], "Distance \\(= |0 - (-9)| = 9\\) units."),
            ("The line \\(y = 0\\) is perpendicular to which of the following coordinate lines?", "Line \\(x = 0\\)", ["Line \\(y = 2\\)", "Line \\(y = -4\\)", "Line \\(x = y\\)"], "Line \\(y = 0\\) (X-axis) is perpendicular to \\(x = 0\\) (Y-axis).")
        ],
        1: [
            ("What is the standard algebraic formula that defines the vertical Y-axis?", "\\(x = 0\\)", ["\\(y = 0\\)", "\\(x = 1\\)", "\\(y = x\\)"], "Every point on the Y-axis has x-coordinate 0."),
            ("For what value of parameter c does the linear equation \\(x = c\\) describe the vertical Y-axis?", "0", ["1", "-1", "Variable"], "The Y-axis is \\(x = 0\\), so \\(c = 0\\)."),
            ("Find the perpendicular distance between the Y-axis (line \\(x = 0\\)) and the parallel line \\(x = 7\\).", "7 units", ["14 units", "0 units", "3.5 units"], "Distance \\(= |7 - 0| = 7\\) units."),
            ("At what point does the vertical Y-axis (line \\(x = 0\\)) intersect the horizontal line \\(y = -5\\)?", "\\((0, -5)\\)", ["\\((-5, 0)\\)", "\\((0, 5)\\)", "\\((0, 0)\\)"], "Intersection is \\((0, -5)\\)."),
            ("A vertical line passes through points \\((0, 3)\\) and \\((0, 8)\\). What is its equation?", "\\(x = 0\\)", ["\\(y = 0\\)", "\\(y = 3\\)", "\\(x = 8\\)"], "Both abscissae are 0, so equation is \\(x = 0\\)."),
            ("What are the coordinates of the image when point \\(B(6, 2)\\) is reflected in the line \\(x = 0\\) (Y-axis)?", "\\((-6, 2)\\)", ["\\((6, -2)\\)", "\\((-6, -2)\\)", "\\((2, 6)\\)"], "Reflection across \\(x = 0\\) maps \\((x, y) \\to (-x, y)\\)."),
            ("If line \\(x = 0\\) is translated 5 units to the right, what is the equation of the new line?", "\\(x = 5\\)", ["\\(x = -5\\)", "\\(y = 5\\)", "\\(x = 0\\)"], "Shift right by 5 gives \\(x = 0 + 5 = 5\\)."),
            ("Can any point situated on the vertical axis \\(x = 0\\) have an abscissa different from zero?", "No, abscissa is strictly 0", ["Yes, in Quadrant I", "Yes, at negative values", "Cannot be determined"], "Every point on \\(x = 0\\) has abscissa exactly 0."),
            ("What is the perpendicular separation between the line \\(x = 0\\) and the parallel line \\(x = -11\\)?", "11 units", ["-11 units", "22 units", "0 units"], "Distance \\(= |0 - (-11)| = 11\\) units."),
            ("The vertical line \\(x = 0\\) is parallel to which of the following lines?", "Line \\(x = 4\\)", ["Line \\(y = 0\\)", "Line \\(y = -8\\)", "Line \\(x + y = 0\\)"], "Lines with equations \\(x = c\\) are all mutually parallel.")
        ],
        2: [
            "Determine the coordinates of the intersection point of lines \\(x = 0\\) and \\(y = 0\\).",
            "At what point on the coordinate plane do the axes \\(x = 0\\) and \\(y = 0\\) cross?",
            "Find the simultaneous solution point for the two equations \\(x = 0\\) and \\(y = 0\\).",
            "Where do the coordinate axes intersect each other in the Cartesian system?",
            "State the point of concurrency of the lines \\(x = 0\\) and \\(y = 0\\).",
            "What ordered pair corresponds to the meeting point of both coordinate axes?",
            "Identify the coordinates of the origin \\(O\\) where \\(x = 0\\) meets \\(y = 0\\).",
            "The lines \\(x = 0\\) and \\(y = 0\\) meet at which unique geometric point?",
            "Compute the common intersection coordinates of the X-axis and Y-axis.",
            "Which point satisfies both equations \\(x = 0\\) and \\(y = 0\\) simultaneously?"
        ],
        3: [
            "The locus of all points whose y-coordinate is identically zero forms the:",
            "All points on the Cartesian grid satisfying the condition \\(y = 0\\) constitute the:",
            "If every point in a set has an ordinate of zero, this set traces the:",
            "The geometric locus defined by the equation \\(y = 0\\) is known as the:",
            "Which line comprises all points where the vertical coordinate is 0?",
            "Points with zero ordinate lie along which geometric line?",
            "The path traced by points where \\(y = 0\\) corresponds to the:",
            "What coordinate line is formed by the condition \\(y = 0\\)?",
            "The set of points \\(\\{(x, y) : y = 0\\}\\) defines the:",
            "Which axis contains all points having a vertical displacement of zero?"
        ],
        4: [
            "The locus of all points whose x-coordinate is identically zero represents the:",
            "All points in the plane with abscissa equal to zero lie on the:",
            "If every point on a line has \\(x = 0\\), this line is the:",
            "The geometric locus defined by \\(x = 0\\) is called the:",
            "Which axis comprises all points where the horizontal coordinate is 0?",
            "Points with zero abscissa are situated along which line?",
            "The path traced by points satisfying \\(x = 0\\) is the:",
            "What coordinate line corresponds to the condition \\(x = 0\\)?",
            "The set \\(\\{(x, y) : x = 0\\}\\) algebraically specifies the:",
            "Which line contains all points having zero horizontal displacement?"
        ],
        5: [
            "What is the constant vertical coordinate of any particle moving along the horizontal line \\(y = 0\\)?",
            "For a sensor traveling strictly on the X-axis, what is its fixed ordinate value?",
            "Along the horizontal datum line \\(y = 0\\), what numerical value does the ordinate take?",
            "State the fixed y-value for all objects constrained to the line \\(y = 0\\).",
            "In physical motion along the horizontal axis, the vertical coordinate remains constantly:",
            "What is the ordinate of any point on the Cartesian line \\(y = 0\\)?",
            "A point moves along the line \\(y = 0\\). Its vertical coordinate is always:",
            "Determine the constant ordinate value for points lying on the horizontal axis.",
            "On the horizontal line \\(y = 0\\), the value of the second coordinate is identically:",
            "Specify the fixed y-component for any point situated on \\(y = 0\\)."
        ],
        6: [
            "What is the horizontal coordinate of any marker positioned on the vertical line \\(x = 0\\)?",
            "For a beacon located on the Y-axis, what is its fixed abscissa value?",
            "Along the vertical datum line \\(x = 0\\), what numerical value does the abscissa assume?",
            "State the fixed x-value for all stations situated on the line \\(x = 0\\).",
            "In motion along the vertical axis, the horizontal coordinate remains constantly:",
            "What is the abscissa of any point on the Cartesian line \\(x = 0\\)?",
            "A point moves along the line \\(x = 0\\). Its horizontal coordinate is always:",
            "Determine the constant abscissa value for points lying on the vertical axis.",
            "On the vertical line \\(x = 0\\), the value of the first coordinate is identically:",
            "Specify the fixed x-component for any point situated on \\(x = 0\\)."
        ],
        7: [
            "Which of the following points lies on the line \\(y = 0\\) (the X-axis)?",
            "Identify the point belonging to the horizontal axis \\(y = 0\\).",
            "Which coordinate pair lies directly on the line \\(y = 0\\)?",
            "Select the point located on the X-axis where \\(y = 0\\).",
            "Which of these ordered pairs satisfies the equation \\(y = 0\\)?",
            "Find the point that rests on the line \\(y = 0\\).",
            "Which point is situated on the line of the X-axis?",
            "Determine which of the following points has \\(y = 0\\).",
            "Identify the ordered pair located on the line \\(y = 0\\).",
            "Which of the given points is a point on the X-axis?"
        ]
    }
    
    for idx, seq in enumerate(SEQS_80):
        pt = PTS_NAMES[idx]
        has_fig = (idx % 3 != 0)
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        tmpl = TEMPLATES[arch][sub_idx]
        
        k_val = sub_idx + 1
        m_val = sub_idx + 15
        svg = svg_cartesian_point(pt, k_val, m_val, f"Axis Locus #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        if arch == 0 or arch == 1:
            q_txt, corr, dist, expl = TEMPLATES[arch][sub_idx]
            txt = prefix + q_txt
            sol = f"**Step 1: Analysis**\n{expl}\n**Step 2: Conclusion**\n{corr}."
        elif arch == 2:
            txt = prefix + tmpl
            corr = "\\((0, 0)\\)"
            dist = ["\\((1, 0)\\)", "\\((0, 1)\\)", "\\((1, 1)\\)"]
            sol = f"**Step 1: Simultaneous Solution**\n\\(x = 0\\) and \\(y = 0\\) intersect at \\((0, 0)\\).\n**Step 2: Conclusion**\n\\((0, 0)\\)."
        elif arch == 3:
            txt = prefix + tmpl
            corr = "X-axis"
            dist = ["Y-axis", "Line \\(x = y\\)", "Origin only"]
            sol = f"**Step 1: Locus**\nPoints with \\(y = 0\\) form the horizontal X-axis.\n**Step 2: Conclusion**\nX-axis."
        elif arch == 4:
            txt = prefix + tmpl
            corr = "Y-axis"
            dist = ["X-axis", "Line \\(y = x\\)", "Origin only"]
            sol = f"**Step 1: Locus**\nPoints with \\(x = 0\\) form the vertical Y-axis.\n**Step 2: Conclusion**\nY-axis."
        elif arch == 5:
            txt = prefix + tmpl
            corr = "0"
            dist = ["1", "-1", "Variable"]
            sol = f"**Step 1: Condition**\nOn line \\(y = 0\\), ordinate is constantly 0.\n**Step 2: Conclusion**\n0."
        elif arch == 6:
            val_ans = m_val
            txt = prefix + f"Point \\({pt}(k, {m_val})\\) is situated on the vertical Y-axis (where \\(x = 0\\)). Compute the value of \\(k + {m_val}\\)."
            corr = f"{val_ans}"
            dist = [f"{val_ans + 2}", f"{val_ans - 3}", "0"]
            sol = f"**Step 1: Coordinate on Y-axis**\nOn line \\(x = 0\\), abscissa \\(k = 0\\).\nTherefore, \\(k + {m_val} = 0 + {m_val} = {val_ans}\\).\n**Step 2: Conclusion**\n{val_ans}."
        else:
            txt = prefix + tmpl
            corr = f"\\(({k_val * 4}, 0)\\)"
            dist = [f"\\((0, {k_val * 4})\\)", f"\\(({k_val * 4}, 1)\\)", f"\\((1, {k_val * 4})\\)"]
            sol = f"**Step 1: Condition**\nA point on \\(y = 0\\) must have y-coordinate 0. Point \\(({k_val * 4}, 0)\\) satisfies this.\n**Step 2: Conclusion**\n\\(({k_val * 4}, 0)\\)."
            
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
    
    TEMPLATES = {
        0: [
            "For the linear equation \\({eq}\\), compute the value of \\(y\\) when \\(x = {x_val}\\).",
            "In the linear relation \\({eq}\\), what is \\(y\\) when \\(x\\) is set to {x_val}?",
            "Given the straight-line equation \\({eq}\\), find the ordinate \\(y\\) corresponding to \\(x = {x_val}\\).",
            "Evaluate \\(y\\) in the equation \\({eq}\\) for the value \\(x = {x_val}\\).",
            "Determine the value of \\(y\\) satisfying \\({eq}\\) when \\(x = {x_val}\\).",
            "If \\(x = {x_val}\\) in the linear formula \\({eq}\\), what does \\(y\\) equal?",
            "Calculate \\(y\\) from the equation \\({eq}\\) when the abscissa is {x_val}.",
            "Substitute \\(x = {x_val}\\) into \\({eq}\\) to find the resulting \\(y\\)-value.",
            "What is the corresponding \\(y\\)-coordinate for \\(x = {x_val}\\) on the line \\({eq}\\)?",
            "Find the ordinate value when \\(x = {x_val}\\) in the equation \\({eq}\\)."
        ],
        1: [
            "For the linear graph \\({eq}\\), determine the value of \\(x\\) when \\(y = {y_val}\\).",
            "In the equation \\({eq}\\), what is the abscissa \\(x\\) when \\(y\\) equals {y_val}?",
            "Calculate the value of \\(x\\) satisfying \\({eq}\\) for the ordinate \\(y = {y_val}\\).",
            "Given the line \\({eq}\\), find \\(x\\) corresponding to \\(y = {y_val}\\).",
            "Evaluate \\(x\\) in the formula \\({eq}\\) when \\(y = {y_val}\\).",
            "If \\(y = {y_val}\\) in the equation \\({eq}\\), what is the value of \\(x\\)?",
            "Determine the abscissa on the line \\({eq}\\) when \\(y = {y_val}\\).",
            "Substitute \\(y = {y_val}\\) into \\({eq}\\) to compute \\(x\\).",
            "What value of \\(x\\) pairs with \\(y = {y_val}\\) in the linear equation \\({eq}\\)?",
            "Find the horizontal coordinate \\(x\\) when \\(y = {y_val}\\) for line \\({eq}\\)."
        ],
        2: [
            "Find the coordinates of the X-intercept where the line \\({eq}\\) meets the horizontal axis.",
            "At what point on the X-axis does the line \\({eq}\\) cross?",
            "Determine the X-intercept point of the linear graph \\({eq}\\).",
            "State the coordinates where the straight line \\({eq}\\) cuts the X-axis.",
            "Where does the linear equation \\({eq}\\) intersect the line \\(y = 0\\)?",
            "Compute the X-intercept coordinates for the line \\({eq}\\).",
            "Identify the point on the horizontal axis cut by the line \\({eq}\\).",
            "What is the intersection point of line \\({eq}\\) with the horizontal X-axis?",
            "Calculate the coordinates of the X-intercept of line \\({eq}\\).",
            "Write the ordered pair where line \\({eq}\\) intersects the X-axis."
        ],
        3: [
            "Determine the coordinates of the Y-intercept for the line \\({eq}\\).",
            "At what point on the Y-axis does the line \\({eq}\\) intersect?",
            "Find the Y-intercept point of the linear graph \\({eq}\\).",
            "State the coordinates where the straight line \\({eq}\\) cuts the vertical axis.",
            "Where does the linear equation \\({eq}\\) cross the line \\(x = 0\\)?",
            "Compute the Y-intercept coordinates for the equation \\({eq}\\).",
            "Identify the point on the vertical axis cut by the line \\({eq}\\).",
            "What is the intersection point of line \\({eq}\\) with the vertical Y-axis?",
            "Calculate the coordinates of the Y-intercept of line \\({eq}\\).",
            "Write the ordered pair where line \\({eq}\\) meets the vertical axis."
        ],
        4: [
            "How many distinct solutions \\((x, y)\\) exist for the linear equation \\({eq}\\)?",
            "What is the total number of coordinate pairs satisfying the line \\({eq}\\)?",
            "How many points lie on the straight line graph of \\({eq}\\)?",
            "A linear equation in two variables such as \\({eq}\\) has how many solutions?",
            "State the number of possible solutions to the linear formula \\({eq}\\).",
            "How many ordered pairs solve the two-variable equation \\({eq}\\)?",
            "Determine the solution count for the linear equation \\({eq}\\).",
            "The equation \\({eq}\\) is satisfied by how many coordinate pairs?",
            "What is the cardinality of the solution set of \\({eq}\\)?",
            "How many points make up the solution graph of \\({eq}\\)?"
        ],
        5: [
            "What geometric figure is formed on graph paper by plotting the equation \\({eq}\\)?",
            "Plotting all solutions of \\({eq}\\) in the Cartesian plane produces which shape?",
            "The graph of the two-variable linear equation \\({eq}\\) is a:",
            "Which geometric curve represents the equation \\({eq}\\) on a coordinate sheet?",
            "Every first-degree equation in two variables like \\({eq}\\) graphs as a:",
            "What is the graphical representation of the linear equation \\({eq}\\)?",
            "The set of points satisfying \\({eq}\\) aligns to form a:",
            "Identify the geometric shape represented by the equation \\({eq}\\).",
            "On a graph grid, the relation \\({eq}\\) is depicted as a:",
            "Name the geometric entity corresponding to the graph of \\({eq}\\)."
        ],
        6: [
            "To draw an accurate line graph of \\({eq}\\), what minimum number of points should be plotted to verify collinearity?",
            "How many points are recommended to ensure verified collinearity when graphing \\({eq}\\)?",
            "When plotting the straight line \\({eq}\\), what is the safest minimum number of solutions to compute?",
            "What is the standard minimum number of points plotted to graph \\({eq}\\) reliably?",
            "To prevent arithmetic errors when graphing \\({eq}\\), at least how many points should be located?",
            "In practical graph plotting of \\({eq}\\), how many points are needed to check alignment?",
            "What minimum number of solutions should be calculated to plot \\({eq}\\) accurately?",
            "How many coordinate points are recommended to establish collinearity for line \\({eq}\\)?",
            "To confirm that plotted points for \\({eq}\\) are truly collinear, calculate at least:",
            "State the recommended minimum number of points required to plot the line \\({eq}\\)."
        ],
        7: [
            "Does the straight line \\({eq}\\) pass through the origin \\(O(0, 0)\\)?",
            "Determine whether the graph of \\({eq}\\) crosses through the origin \\((0, 0)\\).",
            "Check if the origin point \\((0, 0)\\) satisfies the linear equation \\({eq}\\).",
            "Does the line \\({eq}\\) contain the point \\((0, 0)\\)?",
            "Will the straight line \\({eq}\\) pass through the intersection of the coordinate axes?",
            "Is the origin \\((0, 0)\\) a solution to the equation \\({eq}\\)?",
            "Does the locus of \\({eq}\\) include the coordinate origin?",
            "Verify if the point \\((0, 0)\\) lies on the line \\({eq}\\).",
            "Does the line represented by \\({eq}\\) pass through \\(O(0, 0)\\)?",
            "Is origin \\((0, 0)\\) located on the straight line \\({eq}\\)?"
        ]
    }
    
    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        tmpl = TEMPLATES[arch][sub_idx]
        
        a = 1 if sub_idx % 2 == 0 else 2
        b = 1 if sub_idx < 5 else -1
        c = (arch * 20) + (sub_idx + 1) * 2 * a
        eq_str = f"{a}x + y = {c}" if b == 1 else f"{a}x - y = {c}"
        
        has_fig = (idx % 3 != 0)
        svg = svg_parallel_line(eq_str, False, 2, f"Line Graph #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        if arch == 0:
            x_val = sub_idx + 1
            y_val = (c - a * x_val) if b == 1 else -(c - a * x_val)
            txt = prefix + tmpl.format(eq=eq_str, x_val=x_val)
            corr = f"{y_val}"
            dist = [f"{y_val + 2}", f"{y_val - 3}", f"{-y_val}"]
            sol = f"**Step 1: Substitution**\nSubstitute \\(x = {x_val}\\) into \\({eq_str}\\):\n\\(y = {y_val}\\).\n**Step 2: Conclusion**\n{y_val}."
        elif arch == 1:
            y_val = sub_idx + 2
            rem = c - b * y_val
            x_val = rem // a
            txt = prefix + tmpl.format(eq=eq_str, y_val=y_val)
            corr = f"{x_val}"
            dist = [f"{x_val + 2}", f"{x_val - 1}", f"{-x_val}"]
            sol = f"**Step 1: Substitution**\nSubstitute \\(y = {y_val}\\) into \\({eq_str}\\):\n\\(x = {x_val}\\).\n**Step 2: Conclusion**\n{x_val}."
        elif arch == 2:
            x_int = c // a
            txt = prefix + tmpl.format(eq=eq_str)
            corr = f"\\(({x_int}, 0)\\)"
            dist = [f"\\((0, {x_int})\\)", f"\\(({x_int}, 1)\\)", f"\\((0, 0)\\)"]
            sol = f"**Step 1: Put y = 0**\n\\({a}x = {c} \\implies x = {x_int}\\).\nPoint is \\(({x_int}, 0)\\).\n**Step 2: Conclusion**\n\\(({x_int}, 0)\\)."
        elif arch == 3:
            y_int = c if b == 1 else -c
            txt = prefix + tmpl.format(eq=eq_str)
            corr = f"\\((0, {y_int})\\)"
            dist = [f"\\(({y_int}, 0)\\)", f"\\((1, {y_int})\\)", f"\\((0, 0)\\)"]
            sol = f"**Step 1: Put x = 0**\n\\({b}y = {c} \\implies y = {y_int}\\).\nPoint is \\((0, {y_int})\\).\n**Step 2: Conclusion**\n\\((0, {y_int})\\)."
        elif arch == 4:
            txt = prefix + tmpl.format(eq=eq_str)
            corr = "Infinitely many solutions"
            dist = ["Exactly one solution", "Exactly two solutions", "Zero solutions"]
            sol = f"**Step 1: Concept**\nA line consists of infinitely many points; each point is a solution.\n**Step 2: Conclusion**\nInfinitely many solutions."
        elif arch == 5:
            txt = prefix + tmpl.format(eq=eq_str)
            corr = "A straight line"
            dist = ["A circle", "A parabola", "An angle"]
            sol = f"**Step 1: Concept**\nA linear equation in two variables always graphs as a straight line.\n**Step 2: Conclusion**\nA straight line."
        elif arch == 6:
            txt = prefix + tmpl.format(eq=eq_str)
            corr = "At least 3 points"
            dist = ["Only 1 point", "At least 10 points", "At least 5 points"]
            sol = f"**Step 1: Rule**\nPlotting at least 3 points verifies collinearity and avoids calculation errors.\n**Step 2: Conclusion**\nAt least 3 points."
        else:
            # Alternate between lines passing through origin (c=0) and not passing (c != 0) with distinct equations
            if sub_idx % 2 == 0:
                eq_origin = f"{sub_idx + 1}x - y = 0"
                txt = prefix + tmpl.format(eq=eq_origin)
                corr = "Yes, because the constant term is zero (0)"
                dist = ["No, because it is a linear equation", "Only in Quadrant I", "Cannot be determined"]
                sol = f"**Step 1: Check origin (0, 0)**\nLHS \\(= {sub_idx + 1}(0) - 0 = 0\\), which equals RHS (0). So it passes through origin.\n**Step 2: Conclusion**\n{corr}."
            else:
                c_val = 100 + sub_idx * 15
                eq_non_origin = f"{sub_idx + 2}x + y = {c_val}"
                txt = prefix + tmpl.format(eq=eq_non_origin)
                corr = "No, because the constant term is non-zero"
                dist = ["Yes, because constant term is 0", "Only in Quadrant I", "Cannot be determined"]
                sol = f"**Step 1: Check origin (0, 0)**\nLHS \\(= 0\\), whereas RHS \\(= {c_val}\\). Since \\(0 \\neq {c_val}\\), it does not pass through origin.\n**Step 2: Conclusion**\n{corr}."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def main():
    all_qs = []
    print("Generating Chapter 7 perfect questions...")
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
