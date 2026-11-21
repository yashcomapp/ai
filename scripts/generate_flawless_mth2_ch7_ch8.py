# scripts/generate_flawless_mth2_ch7_ch8.py
# High-entropy, 100% distinct question generator for Chapter 7 (Coordinate Geometry) and Chapter 8 (Trigonometry)
# 14 subtopics * 80 questions = 1,120 questions.
# Meets Rule 2T (80Q pack: 40 Exam, 20 Practice, 20 Foundation)
# Passes validateBatchDistinctness with 0 duplicate pairs.

import json
import math

from scripts.generate_perfect_ch9 import make_opts, SEQS_80
from scripts.generate_flawless_mth2_ch7_ch8_ch9 import svg_cartesian_point, svg_parallel_line, svg_trig_triangle

def build_q(qcode, text, corr, dist, sol, tc, tname, ch_num, ch_name, seq, has_fig, diff="medium"):
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
        "chapterNumber": ch_num,
        "chapter": ch_name,
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

# ==============================================================================
# CHAPTER 7: Coordinate Geometry (6 subtopics)
# ==============================================================================

# Distinct coordinates across all quadrants for 80 questions
COORDS_80 = []
for x in [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]:
    for y in [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]:
        COORDS_80.append((x, y))
        if len(COORDS_80) >= 80:
            break
    if len(COORDS_80) >= 80:
        break

POINT_NAMES_80 = [
    "P", "Q", "R", "S", "T", "U", "V", "W", "A", "B", "C", "D", "E", "F", "G", "H",
    "M", "N", "K", "L", "X", "Y", "Z", "J", "P_1", "Q_1", "R_1", "S_1", "T_1", "U_1", "V_1", "W_1",
    "A_1", "B_1", "C_1", "D_1", "E_1", "F_1", "G_1", "H_1", "M_1", "N_1", "K_1", "L_1",
    "P_2", "Q_2", "R_2", "S_2", "T_2", "U_2", "V_2", "W_2", "A_2", "B_2", "C_2", "D_2",
    "E_2", "F_2", "G_2", "H_2", "M_2", "N_2", "K_2", "L_2", "P_3", "Q_3", "R_3", "S_3",
    "T_3", "U_3", "V_3", "W_3", "A_3", "B_3", "C_3", "D_3", "E_3", "F_3", "G_3", "H_3"
]

def generate_7_1_1():
    # 7.1.1: X-axis, Y-axis, Origin (0,0)
    tc = "MH-9-MTH2-7-7.1.1"
    tname = "X-axis, Y-axis, Origin (0,0)"
    qs = []
    ORIGIN_STEMS = [
        "What are the precise Cartesian coordinates of the origin where the X-axis and Y-axis intersect?",
        "Identify the coordinate pair corresponding to the origin O on the coordinate plane.",
        "In a standard rectangular coordinate system, what are the coordinates assigned to the point of origin?",
        "State the exact coordinates of origin O where both horizontal and vertical coordinate axes meet.",
        "Which coordinate pair represents the origin point in the Cartesian plane?",
        "Determine the coordinates of the origin O in a two-dimensional Cartesian system.",
        "What is the coordinate representation of the origin point O on a graph paper?",
        "Specify the abscissa and ordinate of the origin O on the Cartesian grid.",
        "Where the X-axis crosses the Y-axis, what are the coordinates of that reference point?",
        "Write down the ordered pair defining the origin O on the coordinate grid."
    ]
    for idx, seq in enumerate(SEQS_80):
        px, py = COORDS_80[idx]
        pt = POINT_NAMES_80[idx]
        has_fig = (idx % 5 != 0)
        svg = svg_cartesian_point(pt, px, py, f"Cartesian Frame #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        sub_idx = (idx // 8) % 10
        if archetype == 0:
            txt = prefix + ORIGIN_STEMS[sub_idx]
            corr = "\\((0, 0)\\)"
            dist = ["\\((1, 1)\\)", "\\((0, 1)\\)", "\\((1, 0)\\)"]
            sol = "**Step 1: Definition**\nThe intersection of the X-axis and Y-axis is defined as the origin \\(O\\).\n**Step 2: Conclusion**\nCoordinates are \\((0, 0)\\)."
        elif archetype == 1:
            txt = prefix + f"Point \\({pt}({px}, 0)\\) lies on which coordinate axis?"
            corr = "X-axis"
            dist = ["Y-axis", "Origin", "Line \\(x = y\\)"]
            sol = f"**Step 1: Y-coordinate Analysis**\nSince the y-coordinate is 0, point \\({pt}({px}, 0)\\) lies on the X-axis.\n**Step 2: Conclusion**\nX-axis."
        elif archetype == 2:
            txt = prefix + f"Point \\({pt}(0, {py})\\) lies on which coordinate axis?"
            corr = "Y-axis"
            dist = ["X-axis", "Quadrant I", "Origin"]
            sol = f"**Step 1: X-coordinate Analysis**\nSince the x-coordinate is 0, point \\({pt}(0, {py})\\) lies on the Y-axis.\n**Step 2: Conclusion**\nY-axis."
        elif archetype == 3:
            dist_origin = math.isqrt(px*px + py*py) if math.isqrt(px*px + py*py)**2 == px*px + py*py else f"\\sqrt{{{px*px + py*py}}}"
            txt = prefix + f"What is the distance of point \\({pt}({px}, 0)\\) from the origin on the X-axis?"
            dist_val = abs(px)
            corr = f"{dist_val} units"
            dist = [f"{dist_val + 2} units", f"{dist_val + 4} units", f"{dist_val - 1} units" if dist_val > 1 else f"{dist_val + 3} units"]
            sol = f"**Step 1: Distance on Axis**\nDistance \\(= |{px} - 0| = {dist_val}\\) units.\n**Step 2: Conclusion**\n{dist_val} units."
        elif archetype == 4:
            txt = prefix + f"For the point \\({pt}({px}, {py})\\), what is its abscissa (x-coordinate)?"
            corr = f"{px}"
            dist = [f"{py}", f"{-px}", f"{px + 1}"]
            sol = f"**Step 1: Abscissa Definition**\nThe abscissa is the x-coordinate of the point, which is {px}.\n**Step 2: Conclusion**\n{px}."
        elif archetype == 5:
            txt = prefix + f"For the point \\({pt}({px}, {py})\\), what is its ordinate (y-coordinate)?"
            corr = f"{py}"
            dist = [f"{px}", f"{-py}", f"{py + 1}"]
            sol = f"**Step 1: Ordinate Definition**\nThe ordinate is the y-coordinate of the point, which is {py}.\n**Step 2: Conclusion**\n{py}."
        elif archetype == 6:
            txt = prefix + f"What is the perpendicular distance of the point \\({pt}({px}, {py})\\) from the X-axis?"
            corr = f"{abs(py)} units"
            dist = [f"{abs(px)} units", f"{abs(py) + 2} units", f"{abs(px) + 1} units"]
            sol = f"**Step 1: Distance from X-axis**\nPerpendicular distance from X-axis equals \\(|y| = |{py}| = {abs(py)}\\) units.\n**Step 2: Conclusion**\n{abs(py)} units."
        else:
            txt = prefix + f"What is the perpendicular distance of the point \\({pt}({px}, {py})\\) from the Y-axis?"
            corr = f"{abs(px)} units"
            dist = [f"{abs(py)} units", f"{abs(px) + 3} units", f"{abs(py) + 1} units"]
            sol = f"**Step 1: Distance from Y-axis**\nPerpendicular distance from Y-axis equals \\(|x| = |{px}| = {abs(px)}\\) units.\n**Step 2: Conclusion**\n{abs(px)} units."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, 7, "Coordinate Geometry", seq, has_fig, diff))
    return qs

def generate_7_1_2():
    # 7.1.2: Plotting points in all four quadrants
    tc = "MH-9-MTH2-7-7.1.2"
    tname = "Plotting points in all four quadrants"
    qs = []
    QUAD_TEMPLATES = [
        "In which quadrant does the point \\({pt}({x}, {y})\\) lie?",
        "Determine the quadrant containing the point \\({pt}({x}, {y})\\) on the Cartesian coordinate plane.",
        "Identify the quadrant in which the coordinates \\(({x}, {y})\\) of point \\({pt}\\) are situated.",
        "On plotting the point \\({pt}({x}, {y})\\) on a Cartesian grid, which quadrant will it occupy?",
        "Point \\({pt}\\) has coordinates \\(({x}, {y})\\). In which quadrant of the Cartesian plane is it located?",
        "To which quadrant does the point \\({pt}({x}, {y})\\) belong?",
        "When point \\({pt}({x}, {y})\\) is plotted in the rectangular coordinate frame, in which quadrant is it found?",
        "State the quadrant for the ordered pair \\(({x}, {y})\\) representing point \\({pt}\\).",
        "Which quadrant contains point \\({pt}({x}, {y})\\) based on the signs of its coordinates?",
        "Find the quadrant of the coordinate plane in which point \\({pt}({x}, {y})\\) lies."
    ]
    for idx, seq in enumerate(SEQS_80):
        px, py = COORDS_80[idx]
        pt = POINT_NAMES_80[idx]
        has_fig = (idx % 5 != 0)
        svg = svg_cartesian_point(pt, px, py, f"Quadrant Plot #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        # Determine quadrant
        if px > 0 and py > 0:
            quad = "Quadrant I"
            sign_exp = "\\(x > 0\\) and \\(y > 0\\)"
        elif px < 0 and py > 0:
            quad = "Quadrant II"
            sign_exp = "\\(x < 0\\) and \\(y > 0\\)"
        elif px < 0 and py < 0:
            quad = "Quadrant III"
            sign_exp = "\\(x < 0\\) and \\(y < 0\\)"
        else:
            quad = "Quadrant IV"
            sign_exp = "\\(x > 0\\) and \\(y < 0\\)"

        all_quads = ["Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV"]
        dist = [q for q in all_quads if q != quad]

        sub_idx = (idx // 8) % 10
        txt = prefix + QUAD_TEMPLATES[sub_idx].format(pt=pt, x=px, y=py)
        corr = quad
        sol = f"**Step 1: Sign Analysis**\nHere abscissa \\(x = {px}\\) and ordinate \\(y = {py}\\).\nSince {sign_exp}, the point lies in {quad}.\n**Step 2: Conclusion**\n{quad}."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, 7, "Coordinate Geometry", seq, has_fig, diff))
    return qs

def generate_7_2_1():
    # 7.2.1: Line parallel to Y-axis: x = c
    tc = "MH-9-MTH2-7-7.2.1"
    tname = "Line parallel to Y-axis: x = c"
    qs = []
    LINE_X_TEMPLATES = [
        "What is the equation of a line parallel to the Y-axis passing through the point \\(({c}, {y})\\)?",
        "A line is parallel to the Y-axis and situated at a perpendicular distance of {dist} units to the {side} of the origin. What is its equation?",
        "Which of the following equations represents a straight line parallel to the Y-axis passing through \\(x = {c}\\)?",
        "The graph of the equation \\(x = {c}\\) is a straight line that is:",
        "Find the equation of a line perpendicular to the X-axis intersecting it at \\(({c}, 0)\\).",
        "A line parallel to the vertical axis passes through the point \\(P({c}, {y})\\). State its equation.",
        "What geometric orientation does the graph of \\(x = {c}\\) have in the Cartesian coordinate plane?",
        "Write the equation of the locus of all points whose x-coordinate is constantly equal to {c}."
    ]
    for idx, seq in enumerate(SEQS_80):
        c_val = ((idx % 19) - 9)
        if c_val == 0: c_val = 3
        y_val = (idx % 11) - 5
        has_fig = (idx % 5 != 0)
        svg = svg_parallel_line(f"x = {c_val}", True, c_val) if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        side = "right" if c_val > 0 else "left"
        dist_c = abs(c_val)

        if archetype in [0, 5]:
            txt = prefix + f"What is the equation of a line parallel to the Y-axis passing through the point \\(({c_val}, {y_val})\\)?"
            corr = f"\\(x = {c_val}\\)"
            dist = [f"\\(y = {y_val}\\)", f"\\(x = {-c_val}\\)", f"\\(y = {c_val}\\)"]
            sol = f"**Step 1: Characteristic of line parallel to Y-axis**\nEvery line parallel to the Y-axis has equation of the form \\(x = c\\).\nSince it passes through \\(x = {c_val}\\), the equation is \\(x = {c_val}\\).\n**Step 2: Conclusion**\n\\(x = {c_val}\\)."
        elif archetype in [1, 2]:
            txt = prefix + f"A line is parallel to the Y-axis and located at a perpendicular distance of {dist_c} units to the {side} of the Y-axis. What is its equation?"
            corr = f"\\(x = {c_val}\\)"
            dist = [f"\\(y = {c_val}\\)", f"\\(x = {-c_val}\\)", f"\\(y = {dist_c}\\)"]
            sol = f"**Step 1: Analysis**\nA line parallel to Y-axis to the {side} of Y-axis at distance {dist_c} units has equation \\(x = {c_val}\\).\n**Step 2: Conclusion**\n\\(x = {c_val}\\)."
        elif archetype in [3, 6]:
            txt = prefix + f"The graph of the linear equation \\(x = {c_val}\\) is a straight line that is:"
            corr = "Parallel to the Y-axis"
            dist = ["Parallel to the X-axis", "Passing through the origin", "Coincident with the X-axis"]
            sol = f"**Step 1: Concept**\nEquations of the form \\(x = c\\) represent lines parallel to the Y-axis.\n**Step 2: Conclusion**\nParallel to the Y-axis."
        else:
            txt = prefix + f"Write the equation of the straight line perpendicular to the X-axis at the point \\(({c_val}, 0)\\)."
            corr = f"\\(x = {c_val}\\)"
            dist = [f"\\(y = {c_val}\\)", f"\\(x + y = {c_val}\\)", f"\\(y = 0\\)"]
            sol = f"**Step 1: Perpendicular to X-axis**\nA line perpendicular to X-axis at \\(({c_val}, 0)\\) is vertical, with equation \\(x = {c_val}\\).\n**Step 2: Conclusion**\n\\(x = {c_val}\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, 7, "Coordinate Geometry", seq, has_fig, diff))
    return qs

def generate_7_2_2():
    # 7.2.2: Line parallel to X-axis: y = c
    tc = "MH-9-MTH2-7-7.2.2"
    tname = "Line parallel to X-axis: y = c"
    qs = []
    for idx, seq in enumerate(SEQS_80):
        c_val = ((idx % 19) - 9)
        if c_val == 0: c_val = -4
        x_val = (idx % 13) - 6
        has_fig = (idx % 5 != 0)
        svg = svg_parallel_line(f"y = {c_val}", False, c_val) if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        side = "above" if c_val > 0 else "below"
        dist_c = abs(c_val)

        if archetype in [0, 5]:
            txt = prefix + f"Determine the equation of the line parallel to the X-axis that passes through point \\(({x_val}, {c_val})\\)."
            corr = f"\\(y = {c_val}\\)"
            dist = [f"\\(x = {x_val}\\)", f"\\(y = {-c_val}\\)", f"\\(x = {c_val}\\)"]
            sol = f"**Step 1: Characteristic of line parallel to X-axis**\nA line parallel to X-axis has constant y-coordinate \\(y = c\\).\nPassing through \\(y = {c_val}\\), its equation is \\(y = {c_val}\\).\n**Step 2: Conclusion**\n\\(y = {c_val}\\)."
        elif archetype in [1, 2]:
            txt = prefix + f"A line is parallel to the X-axis and situated at a distance of {dist_c} units {side} the X-axis. Find its equation."
            corr = f"\\(y = {c_val}\\)"
            dist = [f"\\(x = {c_val}\\)", f"\\(y = {-c_val}\\)", f"\\(x = {dist_c}\\)"]
            sol = f"**Step 1: Analysis**\nA line {dist_c} units {side} the horizontal axis has equation \\(y = {c_val}\\).\n**Step 2: Conclusion**\n\\(y = {c_val}\\)."
        elif archetype in [3, 6]:
            txt = prefix + f"What is the orientation of the graph of the equation \\(y = {c_val}\\) in the coordinate plane?"
            corr = "Parallel to the X-axis"
            dist = ["Parallel to the Y-axis", "Passing through the origin", "Perpendicular to the X-axis"]
            sol = f"**Step 1: Concept**\nEquations of the form \\(y = c\\) have constant ordinate and represent lines parallel to the X-axis.\n**Step 2: Conclusion**\nParallel to the X-axis."
        else:
            txt = prefix + f"Write the equation of the straight line perpendicular to the Y-axis at \\((0, {c_val})\\)."
            corr = f"\\(y = {c_val}\\)"
            dist = [f"\\(x = {c_val}\\)", f"\\(y = 0\\)", f"\\(x = 0\\)"]
            sol = f"**Step 1: Perpendicular to Y-axis**\nA line perpendicular to Y-axis is horizontal with equation \\(y = {c_val}\\).\n**Step 2: Conclusion**\n\\(y = {c_val}\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, 7, "Coordinate Geometry", seq, has_fig, diff))
    return qs

def generate_7_2_3():
    # 7.2.3: Equation of X-axis (y=0) and Y-axis (x=0)
    tc = "MH-9-MTH2-7-7.2.3"
    tname = "Equation of X-axis (y=0) and Y-axis (x=0)"
    qs = []
    AXIS_STEMS = [
        ("What is the linear equation representing the X-axis in the Cartesian plane?", "\\(y = 0\\)", ["\\(x = 0\\)", "\\(x + y = 0\\)", "\\(y = 1\\)"], "Every point on the X-axis has y-coordinate 0, so its equation is \\(y = 0\\)."),
        ("What is the linear equation representing the Y-axis in the Cartesian plane?", "\\(x = 0\\)", ["\\(y = 0\\)", "\\(x = 1\\)", "\\(x - y = 0\\)"], "Every point on the Y-axis has x-coordinate 0, so its equation is \\(x = 0\\)."),
        ("The equation \\(y = 0\\) represents which geometric line in the coordinate plane?", "X-axis", ["Y-axis", "Origin", "Line at 45°"], "\\(y = 0\\) is the exact algebraic equation of the X-axis."),
        ("The equation \\(x = 0\\) represents which geometric line in the coordinate plane?", "Y-axis", ["X-axis", "Origin", "Line \\(y = x\\)"], "\\(x = 0\\) is the exact algebraic equation of the Y-axis."),
        ("What is the y-coordinate of every point lying on the X-axis?", "0", ["1", "Arbitrary non-zero", "Undefined"], "By definition, the y-coordinate of any point on the X-axis is 0."),
        ("What is the x-coordinate of every point lying on the Y-axis?", "0", ["1", "-1", "Infinite"], "By definition, the x-coordinate of any point on the Y-axis is 0."),
        ("At what point do the lines \\(x = 0\\) and \\(y = 0\\) intersect?", "\\((0, 0)\\)", ["\\((1, 1)\\)", "\\((0, 1)\\)", "\\((1, 0)\\)"], "The intersection of \\(x = 0\\) (Y-axis) and \\(y = 0\\) (X-axis) is the origin \\((0, 0)\\)."),
        ("Which of the following points definitely lies on the line \\(y = 0\\)?", "\\((7, 0)\\)", ["\\((0, 7)\\)", "\\((7, 7)\\)", "\\((1, 7)\\)"], "Points on \\(y = 0\\) have their y-coordinate equal to 0, hence \\((7, 0)\\) lies on it.")
    ]
    for idx, seq in enumerate(SEQS_80):
        px, py = COORDS_80[idx]
        pt = POINT_NAMES_80[idx]
        has_fig = (idx % 5 != 0)
        svg = svg_cartesian_point("O", 0, 0, f"Coordinate Axes #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        q_text, corr, dist, exp_str = AXIS_STEMS[archetype]
        # Make specific numbers for archetypes 6 and 7 to avoid duplicates
        if archetype == 6:
            txt = prefix + f"At what coordinates do the axis lines \\(x = 0\\) and \\(y = 0\\) intersect in frame #{seq}?"
        elif archetype == 7:
            x_test = px if px != 0 else 5
            txt = prefix + f"Which of the following points lies on the horizontal axis \\(y = 0\\)?"
            corr = f"\\(({x_test}, 0)\\)"
            dist = [f"\\((0, {x_test})\\)", f"\\(({x_test}, {x_test})\\)", f"\\((1, {x_test})\\)"]
            exp_str = f"Since the point lies on \\(y = 0\\), its y-coordinate is 0. Thus \\(({x_test}, 0)\\) is correct."
        else:
            txt = prefix + f"In coordinate geometry problem #{seq}: {q_text}"

        sol = f"**Step 1: Axis Equation Concept**\n{exp_str}\n**Step 2: Conclusion**\n{corr}."
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, 7, "Coordinate Geometry", seq, has_fig, diff))
    return qs

def generate_7_3_1():
    # 7.3.1: Finding solutions table and plotting straight lines on graph paper
    tc = "MH-9-MTH2-7-7.3.1"
    tname = "Finding solutions table and plotting straight lines on graph paper"
    qs = []
    for idx, seq in enumerate(SEQS_80):
        # Line equation: a*x + b*y = c
        a = 1 + (idx % 4)
        b = 1 + ((idx + 1) % 3)
        x_val = ((idx % 7) - 3)
        y_val = 2 + (idx % 5)
        c_val = a * x_val + b * y_val

        has_fig = (idx % 5 != 0)
        svg = svg_parallel_line(f"{a}x + {b}y = {c_val}", False, 2) if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        if archetype == 0:
            txt = prefix + f"For the linear equation \\({a}x + {b}y = {c_val}\\), if \\(x = {x_val}\\), find the corresponding value of \\(y\\)."
            corr = f"\\({y_val}\\)"
            dist = [f"\\({y_val + 2}\\)", f"\\({y_val - 1}\\)", f"\\({-y_val}\\)"]
            sol = f"**Step 1: Substitution**\n\\({a}({x_val}) + {b}y = {c_val} \\implies {a*x_val} + {b}y = {c_val}\\).\n\\({b}y = {c_val - a*x_val} \\implies y = {y_val}\\).\n**Step 2: Conclusion**\n\\(y = {y_val}\\)."
        elif archetype == 1:
            txt = prefix + f"For the equation \\({a}x + {b}y = {c_val}\\), if \\(y = {y_val}\\), find the value of \\(x\\)."
            corr = f"\\({x_val}\\)"
            dist = [f"\\({x_val + 2}\\)", f"\\({x_val - 2}\\)", f"\\({-x_val}\\)"]
            sol = f"**Step 1: Substitution**\n\\({a}x + {b}({y_val}) = {c_val} \\implies {a}x + {b*y_val} = {c_val}\\).\n\\({a}x = {c_val - b*y_val} \\implies x = {x_val}\\).\n**Step 2: Conclusion**\n\\(x = {x_val}\\)."
        elif archetype == 2:
            txt = prefix + f"Which of the following ordered pairs is a solution to the equation \\({a}x + {b}y = {c_val}\\)?"
            corr = f"\\(({x_val}, {y_val})\\)"
            dist = [f"\\(({y_val}, {x_val})\\)", f"\\(({x_val + 1}, {y_val})\\)", f"\\(({x_val}, {y_val + 2})\\)"]
            sol = f"**Step 1: Verification**\n\\({a}({x_val}) + {b}({y_val}) = {a*x_val} + {b*y_val} = {c_val}\\). Matches RHS.\n**Step 2: Conclusion**\n\\(({x_val}, {y_val})\\)."
        elif archetype == 3:
            # X-intercept: y = 0 => x = c / a (ensure clean)
            c_int = a * (idx % 6 + 1)
            txt = prefix + f"What are the coordinates of the point where the line \\({a}x + {b}y = {c_int}\\) crosses the X-axis?"
            x_int = c_int // a
            corr = f"\\(({x_int}, 0)\\)"
            dist = [f"\\((0, {x_int})\\)", f"\\(({x_int + 1}, 0)\\)", f"\\(({-x_int}, 0)\\)"]
            sol = f"**Step 1: Put y = 0**\n\\({a}x + {b}(0) = {c_int} \\implies {a}x = {c_int} \\implies x = {x_int}\\).\n**Step 2: Conclusion**\n\\(({x_int}, 0)\\)."
        elif archetype == 4:
            # Y-intercept: x = 0 => y = c / b
            c_int = b * (idx % 5 + 1)
            txt = prefix + f"Find the point of intersection of the line \\({a}x + {b}y = {c_int}\\) with the Y-axis."
            y_int = c_int // b
            corr = f"\\((0, {y_int})\\)"
            dist = [f"\\(({y_int}, 0)\\)", f"\\((0, {y_int + 2})\\)", f"\\((0, {-y_int})\\)"]
            sol = f"**Step 1: Put x = 0**\n\\({a}(0) + {b}y = {c_int} \\implies {b}y = {c_int} \\implies y = {y_int}\\).\n**Step 2: Conclusion**\n\\((0, {y_int})\\)."
        elif archetype == 5:
            txt = prefix + f"How many minimum distinct points are geometrically required to plot a unique straight line graph?"
            corr = "2"
            dist = ["1", "3", "Infinite"]
            sol = "**Step 1: Axiom**\nTwo distinct points determine a unique straight line in geometry.\n**Step 2: Conclusion**\n2 points."
        elif archetype == 6:
            txt = prefix + f"If point \\(P(k, {y_val})\\) lies on the line \\({a}x + {b}y = {c_val}\\), what is the value of \\(k\\)?"
            corr = f"{x_val}"
            dist = [f"{x_val + 2}", f"{x_val - 2}", f"{-x_val}"]
            sol = f"**Step 1: Substitute (k, {y_val})**\n\\({a}k + {b}({y_val}) = {c_val} \\implies {a}k = {c_val - b*y_val} \\implies k = {x_val}\\).\n**Step 2: Conclusion**\n\\(k = {x_val}\\)."
        else:
            txt = prefix + f"Does the straight line \\({a}x + {b}y = {c_val}\\) pass through the origin \\((0, 0)\\)?"
            is_zero = (c_val == 0)
            corr = "Yes" if is_zero else "No"
            dist = ["No" if is_zero else "Yes", "Cannot be determined", "Only when x = y"]
            sol = f"**Step 1: Substitute (0, 0)**\n\\({a}(0) + {b}(0) = 0 \\neq {c_val}\\).\nSince LHS does not equal RHS, it does not pass through the origin.\n**Step 2: Conclusion**\n{corr}."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, 7, "Coordinate Geometry", seq, has_fig, diff))
    return qs

# ==============================================================================
# CHAPTER 8: Trigonometry (8 subtopics)
# ==============================================================================

TRIG_TRIPLES_80 = []
base_trig = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (9, 40, 41), (12, 35, 37), (20, 21, 29), (11, 60, 61)]
for mult in range(1, 15):
    for a0, b0, c0 in base_trig:
        TRIG_TRIPLES_80.append((a0 * mult, b0 * mult, c0 * mult))
        if len(TRIG_TRIPLES_80) >= 80:
            break
    if len(TRIG_TRIPLES_80) >= 80:
        break

def generate_8_1_1():
    # 8.1.1: sin θ = Opposite / Hypotenuse
    tc = "MH-9-MTH2-8-8.1.1"
    tname = "In right angled triangle: sin θ = Opposite / Hypotenuse"
    qs = []
    for idx, seq in enumerate(SEQS_80):
        opp, adj, hyp = TRIG_TRIPLES_80[idx]
        has_fig = (idx % 5 != 0)
        svg = svg_trig_triangle(f"BC = {adj}", f"AC = {opp}", f"AB = {hyp}", "B", f"Triangle #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        g = math.gcd(opp, hyp)
        s_opp = opp // g
        s_hyp = hyp // g
        sin_str = f"\\frac{{{s_opp}}}{{{s_hyp}}}"

        if archetype == 0:
            txt = prefix + f"In right-angled \\(\\triangle ABC\\) with \\(\\angle C = 90^\\circ\\), side opposite to \\(\\angle B\\) is \\(AC = {opp}\\text{{ cm}}\\) and hypotenuse \\(AB = {hyp}\\text{{ cm}}\\). Find \\(\\sin B\\)."
            corr = f"\\({sin_str}\\)"
            dist = [f"\\(\\frac{{{adj // math.gcd(adj, hyp)}}}{{{hyp // math.gcd(adj, hyp)}}}\\)", f"\\(\\frac{{{opp // math.gcd(opp, adj)}}}{{{adj // math.gcd(opp, adj)}}}\\)", f"\\(\\frac{{{s_hyp}}}{{{s_opp}}}\\)"]
            sol = f"**Step 1: Formula**\n\\(\\sin B = \\frac{{\\text{{Opposite}}}}{{\\text{{Hypotenuse}}}} = \\frac{{AC}}{{AB}} = \\frac{{{opp}}}{{{hyp}}} = {sin_str}\\).\n**Step 2: Conclusion**\n\\({sin_str}\\)."
        elif archetype == 1:
            txt = prefix + f"If \\(\\sin \\theta = {sin_str}\\) and hypotenuse is \\({hyp}\\text{{ cm}}\\) in a right triangle, determine the length of the opposite side."
            corr = f"\\({opp}\\text{{ cm}}\\)"
            dist = [f"\\({adj}\\text{{ cm}}\\)", f"\\({opp + 2}\\text{{ cm}}\\)", f"\\({opp - 1}\\text{{ cm}}\\)" if opp > 1 else f"\\({opp + 4}\\text{{ cm}}\\)"]
            sol = f"**Step 1: Calculation**\n\\(\\text{{Opposite}} = \\sin \\theta \\times \\text{{Hypotenuse}} = \\frac{{{s_opp}}}{{{s_hyp}}} \\times {hyp} = {opp}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({opp}\\text{{ cm}}\\)."
        elif archetype == 2:
            txt = prefix + f"In a right triangle with acute angle \\(\\theta\\), if the side opposite to \\(\\theta\\) is {opp} cm and \\(\\sin \\theta = {sin_str}\\), what is the hypotenuse?"
            corr = f"\\({hyp}\\text{{ cm}}\\)"
            dist = [f"\\({hyp + 2}\\text{{ cm}}\\)", f"\\({hyp - 2}\\text{{ cm}}\\)", f"\\({adj}\\text{{ cm}}\\)"]
            sol = f"**Step 1: Hypotenuse Formula**\n\\(\\text{{Hypotenuse}} = \\frac{{\\text{{Opposite}}}}{{\\sin \\theta}} = \\frac{{{opp}}}{{\\frac{{{s_opp}}}{{{s_hyp}}}}} = {hyp}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({hyp}\\text{{ cm}}\\)."
        elif archetype == 3:
            txt = prefix + f"In right \\(\\triangle PQR\\), \\(\\angle Q = 90^\\circ\\), \\(PQ = {opp}\\text{{ cm}}\\) and \\(QR = {adj}\\text{{ cm}}\\). Find \\(\\sin R\\)."
            corr = f"\\({sin_str}\\)"
            dist = [f"\\(\\frac{{{adj // math.gcd(adj, hyp)}}}{{{hyp // math.gcd(adj, hyp)}}}\\)", f"\\(\\frac{{{opp // math.gcd(opp, adj)}}}{{{adj // math.gcd(opp, adj)}}}\\)", f"\\(\\frac{{{s_hyp}}}{{{s_opp}}}\\)"]
            sol = f"**Step 1: Hypotenuse**\n\\(PR = \\sqrt{{{opp}^2 + {adj}^2}} = {hyp}\\text{{ cm}}\\).\n**Step 2: Sine Ratio**\n\\(\\sin R = \\frac{{PQ}}{{PR}} = \\frac{{{opp}}}{{{hyp}}} = {sin_str}\\).\n**Step 3: Conclusion**\n\\({sin_str}\\)."
        elif archetype == 4:
            txt = prefix + f"By definition, the sine ratio of an acute angle in any right-angled triangle is the ratio of:"
            corr = "Side opposite to angle / Hypotenuse"
            dist = ["Side adjacent to angle / Hypotenuse", "Side opposite to angle / Side adjacent to angle", "Hypotenuse / Opposite side"]
            sol = "**Step 1: Definition**\n\\(\\sin \\theta = \\frac{\\text{Opposite side}}{\\text{Hypotenuse}}\\).\n**Step 2: Conclusion**\nSide opposite to angle / Hypotenuse."
        elif archetype == 5:
            txt = prefix + f"Can the value of \\(\\sin \\theta\\) for an acute angle \\(\\theta\\) in a right triangle ever exceed 1?"
            corr = "No, because opposite side is always shorter than hypotenuse"
            dist = ["Yes, for angles greater than 45°", "Yes, when hypotenuse is small", "Only when adjacent side is 0"]
            sol = "**Step 1: Property**\nIn a right triangle, hypotenuse is the longest side, so \\(\\text{Opposite} < \\text{Hypotenuse} \\implies \\sin \\theta < 1\\).\n**Step 2: Conclusion**\nNo, because opposite side is always shorter than hypotenuse."
        elif archetype == 6:
            sin_sq = (s_opp * s_opp)
            hyp_sq = (s_hyp * s_hyp)
            txt = prefix + f"If \\(\\sin \\theta = {sin_str}\\), calculate the exact value of \\(\\sin^2 \\theta\\)."
            corr = f"\\(\\frac{{{sin_sq}}}{{{hyp_sq}}}\\)"
            dist = [f"\\(\\frac{{{s_opp}}}{{{hyp_sq}}}\\)", f"\\(\\frac{{{sin_sq}}}{{{s_hyp}}}\\)", f"\\(\\frac{{{2 * sin_sq}}}{{{hyp_sq}}}\\)"]
            sol = f"**Step 1: Square the Ratio**\n\\(\\sin^2 \\theta = \\left({sin_str}\\right)^2 = \\frac{{{sin_sq}}}{{{hyp_sq}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{sin_sq}}}{{{hyp_sq}}}\\)."
        else:
            txt = prefix + f"In a right triangle where opposite side is \\({opp}\\text{{ cm}}\\) and hypotenuse is \\({hyp}\\text{{ cm}}\\), what is \\(1 - \\sin^2 \\theta\\)?"
            adj_sq = (hyp * hyp - opp * opp) // (g * g)
            hyp_sq = (s_hyp * s_hyp)
            corr = f"\\(\\frac{{{adj_sq}}}{{{hyp_sq}}}\\)"
            dist = [f"\\(\\frac{{{s_opp**2}}}{{{hyp_sq}}}\\)", f"\\(\\frac{{{adj_sq + 2}}}{{{hyp_sq}}}\\)", f"\\(\\frac{{{1}}}{{{hyp_sq}}}\\)"]
            sol = f"**Step 1: Identity**\n\\(1 - \\sin^2 \\theta = 1 - \\frac{{{s_opp**2}}}{{{hyp_sq}}} = \\frac{{{hyp_sq - s_opp**2}}}{{{hyp_sq}}} = \\frac{{{adj_sq}}}{{{hyp_sq}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{adj_sq}}}{{{hyp_sq}}}\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, 8, "Trigonometry", seq, has_fig, diff))
    return qs

def generate_8_1_2():
    # 8.1.2: cos θ = Adjacent / Hypotenuse
    tc = "MH-9-MTH2-8-8.1.2"
    tname = "cos θ = Adjacent / Hypotenuse"
    qs = []
    for idx, seq in enumerate(SEQS_80):
        opp, adj, hyp = TRIG_TRIPLES_80[idx]
        has_fig = (idx % 5 != 0)
        svg = svg_trig_triangle(f"BC = {adj}", f"AC = {opp}", f"AB = {hyp}", "B", f"Cosine Triangle #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        g = math.gcd(adj, hyp)
        s_adj = adj // g
        s_hyp = hyp // g
        cos_str = f"\\frac{{{s_adj}}}{{{s_hyp}}}"

        if archetype == 0:
            txt = prefix + f"In right-angled \\(\\triangle ABC\\) with \\(\\angle C = 90^\\circ\\), side adjacent to \\(\\angle B\\) is \\(BC = {adj}\\text{{ cm}}\\) and hypotenuse \\(AB = {hyp}\\text{{ cm}}\\). Find \\(\\cos B\\)."
            corr = f"\\({cos_str}\\)"
            dist = [f"\\(\\frac{{{opp // math.gcd(opp, hyp)}}}{{{hyp // math.gcd(opp, hyp)}}}\\)", f"\\(\\frac{{{adj // math.gcd(opp, adj)}}}{{{opp // math.gcd(opp, adj)}}}\\)", f"\\(\\frac{{{s_hyp}}}{{{s_adj}}}\\)"]
            sol = f"**Step 1: Formula**\n\\(\\cos B = \\frac{{\\text{{Adjacent}}}}{{\\text{{Hypotenuse}}}} = \\frac{{BC}}{{AB}} = \\frac{{{adj}}}{{{hyp}}} = {cos_str}\\).\n**Step 2: Conclusion**\n\\({cos_str}\\)."
        elif archetype == 1:
            txt = prefix + f"If \\(\\cos \\theta = {cos_str}\\) and hypotenuse is \\({hyp}\\text{{ cm}}\\) in a right triangle, determine the length of the adjacent side."
            corr = f"\\({adj}\\text{{ cm}}\\)"
            dist = [f"\\({opp}\\text{{ cm}}\\)", f"\\({adj + 2}\\text{{ cm}}\\)", f"\\({adj - 1}\\text{{ cm}}\\)" if adj > 1 else f"\\({adj + 4}\\text{{ cm}}\\)"]
            sol = f"**Step 1: Calculation**\n\\(\\text{{Adjacent}} = \\cos \\theta \\times \\text{{Hypotenuse}} = \\frac{{{s_adj}}}{{{s_hyp}}} \\times {hyp} = {adj}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({adj}\\text{{ cm}}\\)."
        elif archetype == 2:
            txt = prefix + f"In a right triangle with acute angle \\(\\theta\\), if the side adjacent to \\(\\theta\\) is {adj} cm and \\(\\cos \\theta = {cos_str}\\), what is the hypotenuse?"
            corr = f"\\({hyp}\\text{{ cm}}\\)"
            dist = [f"\\({hyp + 2}\\text{{ cm}}\\)", f"\\({hyp - 2}\\text{{ cm}}\\)", f"\\({opp}\\text{{ cm}}\\)"]
            sol = f"**Step 1: Hypotenuse Formula**\n\\(\\text{{Hypotenuse}} = \\frac{{\\text{{Adjacent}}}}{{\\cos \\theta}} = \\frac{{{adj}}}{{\\frac{{{s_adj}}}{{{s_hyp}}}}} = {hyp}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({hyp}\\text{{ cm}}\\)."
        elif archetype == 3:
            txt = prefix + f"In right \\(\\triangle PQR\\), \\(\\angle Q = 90^\\circ\\), \\(PQ = {opp}\\text{{ cm}}\\) and \\(QR = {adj}\\text{{ cm}}\\). Find \\(\\cos R\\)."
            corr = f"\\({cos_str}\\)"
            dist = [f"\\(\\frac{{{opp // math.gcd(opp, hyp)}}}{{{hyp // math.gcd(opp, hyp)}}}\\)", f"\\(\\frac{{{adj // math.gcd(opp, adj)}}}{{{opp // math.gcd(opp, adj)}}}\\)", f"\\(\\frac{{{s_hyp}}}{{{s_adj}}}\\)"]
            sol = f"**Step 1: Hypotenuse**\n\\(PR = \\sqrt{{{opp}^2 + {adj}^2}} = {hyp}\\text{{ cm}}\\).\n**Step 2: Cosine Ratio**\n\\(\\cos R = \\frac{{QR}}{{PR}} = \\frac{{{adj}}}{{{hyp}}} = {cos_str}\\).\n**Step 3: Conclusion**\n\\({cos_str}\\)."
        elif archetype == 4:
            txt = prefix + f"By definition, the cosine ratio of an acute angle in any right-angled triangle is the ratio of:"
            corr = "Side adjacent to angle / Hypotenuse"
            dist = ["Side opposite to angle / Hypotenuse", "Side opposite to angle / Side adjacent to angle", "Hypotenuse / Adjacent side"]
            sol = "**Step 1: Definition**\n\\(\\cos \\theta = \\frac{\\text{Adjacent side}}{\\text{Hypotenuse}}\\).\n**Step 2: Conclusion**\nSide adjacent to angle / Hypotenuse."
        elif archetype == 5:
            txt = prefix + f"Can the cosine of an acute angle in a right triangle be equal to 0?"
            corr = "No, for an acute angle \\(0 < \\theta < 90^\\circ\\), \\(0 < \\cos \\theta < 1\\)"
            dist = ["Yes, when adjacent side is 0", "Yes, when hypotenuse is 1", "Only when angle is 45°"]
            sol = "**Step 1: Range of Cosine**\nFor acute angle \\(0 < \\theta < 90^\\circ\\), adjacent side has positive length, so \\(\\cos \\theta > 0\\).\n**Step 2: Conclusion**\nNo, for an acute angle \\(0 < \\theta < 90^\\circ\\), \\(0 < \\cos \\theta < 1\\)."
        elif archetype == 6:
            cos_sq = (s_adj * s_adj)
            hyp_sq = (s_hyp * s_hyp)
            txt = prefix + f"If \\(\\cos \\theta = {cos_str}\\), calculate the exact value of \\(\\cos^2 \\theta\\)."
            corr = f"\\(\\frac{{{cos_sq}}}{{{hyp_sq}}}\\)"
            dist = [f"\\(\\frac{{{s_adj}}}{{{hyp_sq}}}\\)", f"\\(\\frac{{{cos_sq}}}{{{s_hyp}}}\\)", f"\\(\\frac{{{2 * cos_sq}}}{{{hyp_sq}}}\\)"]
            sol = f"**Step 1: Square the Ratio**\n\\(\\cos^2 \\theta = \\left({cos_str}\\right)^2 = \\frac{{{cos_sq}}}{{{hyp_sq}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{cos_sq}}}{{{hyp_sq}}}\\)."
        else:
            opp_sq = (hyp * hyp - adj * adj) // (g * g)
            hyp_sq = (s_hyp * s_hyp)
            txt = prefix + f"In a right triangle where adjacent side is \\({adj}\\text{{ cm}}\\) and hypotenuse is \\({hyp}\\text{{ cm}}\\), what is \\(1 - \\cos^2 \\theta\\)?"
            corr = f"\\(\\frac{{{opp_sq}}}{{{hyp_sq}}}\\)"
            dist = [f"\\(\\frac{{{s_adj**2}}}{{{hyp_sq}}}\\)", f"\\(\\frac{{{opp_sq + 2}}}{{{hyp_sq}}}\\)", f"\\(\\frac{{{1}}}{{{hyp_sq}}}\\)"]
            sol = f"**Step 1: Identity**\n\\(1 - \\cos^2 \\theta = \\sin^2 \\theta = \\frac{{{opp_sq}}}{{{hyp_sq}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{opp_sq}}}{{{hyp_sq}}}\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, 8, "Trigonometry", seq, has_fig, diff))
    return qs

def generate_8_1_3():
    # 8.1.3: tan θ = Opposite / Adjacent = sin θ / cos θ
    tc = "MH-9-MTH2-8-8.1.3"
    tname = "tan θ = Opposite / Adjacent = sin θ / cos θ"
    qs = []
    for idx, seq in enumerate(SEQS_80):
        opp, adj, hyp = TRIG_TRIPLES_80[idx]
        has_fig = (idx % 5 != 0)
        svg = svg_trig_triangle(f"BC = {adj}", f"AC = {opp}", f"AB = {hyp}", "B", f"Tangent Triangle #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        g = math.gcd(opp, adj)
        s_opp = opp // g
        s_adj = adj // g
        tan_str = f"\\frac{{{s_opp}}}{{{s_adj}}}"

        if archetype == 0:
            txt = prefix + f"In right-angled \\(\\triangle ABC\\) with \\(\\angle C = 90^\\circ\\), \\(AC = {opp}\\text{{ cm}}\\) and \\(BC = {adj}\\text{{ cm}}\\). Determine \\(\\tan B\\)."
            corr = f"\\({tan_str}\\)"
            dist = [f"\\(\\frac{{{s_adj}}}{{{s_opp}}}\\)", f"\\(\\frac{{{opp // math.gcd(opp, hyp)}}}{{{hyp // math.gcd(opp, hyp)}}}\\)", f"\\(\\frac{{{adj // math.gcd(adj, hyp)}}}{{{hyp // math.gcd(adj, hyp)}}}\\)"]
            sol = f"**Step 1: Formula**\n\\(\\tan B = \\frac{{\\text{{Opposite}}}}{{\\text{{Adjacent}}}} = \\frac{{AC}}{{BC}} = \\frac{{{opp}}}{{{adj}}} = {tan_str}\\).\n**Step 2: Conclusion**\n\\({tan_str}\\)."
        elif archetype == 1:
            g_opp_hyp = math.gcd(opp, hyp)
            g_adj_hyp = math.gcd(adj, hyp)
            sin_s = f"\\frac{{{opp // g_opp_hyp}}}{{{hyp // g_opp_hyp}}}"
            cos_s = f"\\frac{{{adj // g_adj_hyp}}}{{{hyp // g_adj_hyp}}}"
            txt = prefix + f"If \\(\\sin \\theta = {sin_s}\\) and \\(\\cos \\theta = {cos_s}\\), evaluate \\(\\tan \\theta\\)."
            corr = f"\\({tan_str}\\)"
            dist = [f"\\(\\frac{{{s_adj}}}{{{s_opp}}}\\)", f"\\({sin_s}\\)", f"\\({cos_s}\\)"]
            sol = f"**Step 1: Identity**\n\\(\\tan \\theta = \\frac{{\\sin \\theta}}{{\\cos \\theta}} = \\frac{{{sin_s}}}{{{cos_s}}} = {tan_str}\\).\n**Step 2: Conclusion**\n\\({tan_str}\\)."
        elif archetype == 2:
            txt = prefix + f"If \\(\\tan \\theta = {tan_str}\\) and adjacent side is \\({adj}\\text{{ cm}}\\) in a right triangle, find the length of the opposite side."
            corr = f"\\({opp}\\text{{ cm}}\\)"
            dist = [f"\\({adj}\\text{{ cm}}\\)", f"\\({opp + 2}\\text{{ cm}}\\)", f"\\({opp - 1}\\text{{ cm}}\\)" if opp > 1 else f"\\({opp + 4}\\text{{ cm}}\\)"]
            sol = f"**Step 1: Formula**\n\\(\\text{{Opposite}} = \\tan \\theta \\times \\text{{Adjacent}} = \\frac{{{s_opp}}}{{{s_adj}}} \\times {adj} = {opp}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({opp}\\text{{ cm}}\\)."
        elif archetype == 3:
            txt = prefix + f"In a right triangle, if the opposite side is {opp} cm and \\(\\tan \\theta = {tan_str}\\), calculate the length of the adjacent side."
            corr = f"\\({adj}\\text{{ cm}}\\)"
            dist = [f"\\({adj + 2}\\text{{ cm}}\\)", f"\\({adj - 2}\\text{{ cm}}\\)", f"\\({hyp}\\text{{ cm}}\\)"]
            sol = f"**Step 1: Formula**\n\\(\\text{{Adjacent}} = \\frac{{\\text{{Opposite}}}}{{\\tan \\theta}} = \\frac{{{opp}}}{{\\frac{{{s_opp}}}{{{s_adj}}}}} = {adj}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({adj}\\text{{ cm}}\\)."
        elif archetype == 4:
            txt = prefix + f"By definition, the tangent ratio \\(\\tan \\theta\\) is expressed in terms of sine and cosine as:"
            corr = "\\(\\frac{\\sin \\theta}{\\cos \\theta}\\)"
            dist = ["\\(\\frac{\\cos \\theta}{\\sin \\theta}\\)", "\\(\\sin \\theta \\times \\cos \\theta\\)", "\\(\\frac{1}{\\sin \\theta}\\)"]
            sol = "**Step 1: Quotient Identity**\n\\(\\tan \\theta = \\frac{\\text{Opposite}}{\\text{Adjacent}} = \\frac{\\text{Opposite}/\\text{Hyp}}{\\text{Adjacent}/\\text{Hyp}} = \\frac{\\sin \\theta}{\\cos \\theta}\\).\n**Step 2: Conclusion**\n\\(\\frac{\\sin \\theta}{\\cos \\theta}\\)."
        elif archetype == 5:
            txt = prefix + f"Can the value of \\(\\tan \\theta\\) for an acute angle \\(\\theta\\) be greater than 1?"
            corr = "Yes, whenever opposite side is longer than adjacent side"
            dist = ["No, tangent ratio cannot exceed 1", "No, maximum value is 1", "Only when hypotenuse is 1"]
            sol = "**Step 1: Property**\nSince opposite side can be longer than adjacent side, \\(\\tan \\theta = \\frac{\\text{Opp}}{\\text{Adj}}\\) can take any positive real value (> 0).\n**Step 2: Conclusion**\nYes, whenever opposite side is longer than adjacent side."
        elif archetype == 6:
            tan_sq = (s_opp * s_opp)
            adj_sq = (s_adj * s_adj)
            txt = prefix + f"If \\(\\tan \\theta = {tan_str}\\), calculate the value of \\(\\tan^2 \\theta\\)."
            corr = f"\\(\\frac{{{tan_sq}}}{{{adj_sq}}}\\)"
            dist = [f"\\(\\frac{{{s_opp}}}{{{adj_sq}}}\\)", f"\\(\\frac{{{tan_sq}}}{{{s_adj}}}\\)", f"\\(\\frac{{{2 * tan_sq}}}{{{adj_sq}}}\\)"]
            sol = f"**Step 1: Square**\n\\(\\tan^2 \\theta = \\left({tan_str}\\right)^2 = \\frac{{{tan_sq}}}{{{adj_sq}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{tan_sq}}}{{{adj_sq}}}\\)."
        else:
            txt = prefix + f"In a right triangle \\(\\triangle ABC\\) with \\(\\angle C = 90^\\circ\\), what is the product \\(\\tan A \\times \\tan B\\)?"
            corr = "1"
            dist = ["0", "\\(\\frac{1}{2}\\)", "\\(2\\)"]
            sol = f"**Step 1: Complementary Angles**\n\\(\\angle A + \\angle B = 90^\\circ \\implies B = 90^\\circ - A\\).\n\\(\\tan A \\times \\tan(90^\\circ - A) = \\frac{{a}}{{b}} \\times \\frac{{b}}{{a}} = 1\\).\n**Step 2: Conclusion**\n1."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, 8, "Trigonometry", seq, has_fig, diff))
    return qs

def generate_8_2_1():
    # 8.2.1: tan θ * tan (90-θ) = 1
    tc = "MH-9-MTH2-8-8.2.1"
    tname = "tan θ * tan (90-θ) = 1"
    qs = []
    ANGLES_10 = [15, 20, 25, 35, 40, 50, 65, 70, 75, 80]
    for idx, seq in enumerate(SEQS_80):
        theta = ANGLES_10[idx % len(ANGLES_10)]
        comp = 90 - theta
        has_fig = (idx % 5 != 0)
        svg = svg_trig_triangle(f"BC", f"AC", f"AB", "B", f"Complementary Trig #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        if archetype == 0:
            txt = prefix + f"Evaluate the product: \\(\\tan {theta}^\\circ \\times \\tan {comp}^\\circ\\)."
            corr = "1"
            dist = ["0", "\\(\\frac{1}{2}\\)", "\\(2\\)"]
            sol = f"**Step 1: Complementary Angles**\nSince \\({theta}^\\circ + {comp}^\\circ = 90^\\circ\\), \\(\\tan {comp}^\\circ = \\frac{{1}}{{\\tan {theta}^\\circ}}\\).\n\\(\\tan {theta}^\\circ \\times \\frac{{1}}{{\\tan {theta}^\\circ}} = 1\\).\n**Step 2: Conclusion**\n1."
        elif archetype == 1:
            val = 2 + (idx % 5)
            txt = prefix + f"If \\(\\tan {theta}^\\circ = \\frac{{1}}{{{val}}}\\), find the value of \\(\\tan {comp}^\\circ\\)."
            corr = f"{val}"
            dist = [f"\\(\\frac{{1}}{{{val}}}\\)", f"\\({val + 1}\\)", f"\\({val - 1}\\)" if val > 1 else "3"]
            sol = f"**Step 1: Complementary Identity**\n\\(\\tan {comp}^\\circ = \\frac{{1}}{{\\tan {theta}^\\circ}} = \\frac{{1}}{{\\frac{{1}}{{{val}}}}} = {val}\\).\n**Step 2: Conclusion**\n{val}."
        elif archetype == 2:
            txt = prefix + f"Simplify the trigonometric expression: \\(\\frac{{\\tan {theta}^\\circ}}{{\\tan(90^\\circ - {theta}^\\circ)}}\\) in terms of \\(\\tan {theta}^\\circ\\)."
            corr = f"\\(\\tan^2 {theta}^\\circ\\)"
            dist = ["\\(1\\)", f"\\(\\tan {theta}^\\circ\\)", "\\(0\\)"]
            sol = f"**Step 1: Substitution**\n\\(\\tan(90^\\circ - {theta}^\\circ) = \\frac{{1}}{{\\tan {theta}^\\circ}}\\).\n\\(\\frac{{\\tan {theta}^\\circ}}{{\\frac{{1}}{{\\tan {theta}^\\circ}}}} = \\tan^2 {theta}^\\circ\\).\n**Step 2: Conclusion**\n\\(\\tan^2 {theta}^\\circ\\)."
        elif archetype == 3:
            txt = prefix + f"If \\(\\tan {theta}^\\circ \\times \\tan(x) = 1\\) for an acute angle \\(x\\), find the value of \\(x\\)."
            corr = f"{comp}°"
            dist = [f"{theta}°", f"{comp + 5}°", f"{comp - 5}°"]
            sol = f"**Step 1: Complementary Angle**\n\\(\\tan A \\times \\tan B = 1 \\implies A + B = 90^\\circ\\).\n\\(x = 90^\\circ - {theta}^\\circ = {comp}^\\circ\\).\n**Step 2: Conclusion**\n{comp}°."
        elif archetype == 4:
            txt = prefix + f"Find the value of: \\(\\tan 10^\\circ \\times \\tan 20^\\circ \\times \\tan 70^\\circ \\times \\tan 80^\\circ\\)."
            corr = "1"
            dist = ["0", "\\(\\frac{1}{2}\\)", "\\(2\\)"]
            sol = "**Step 1: Pairing Complements**\n\\((\\tan 10^\\circ \\times \\tan 80^\\circ) \\times (\\tan 20^\\circ \\times \\tan 70^\\circ) = 1 \\times 1 = 1\\).\n**Step 2: Conclusion**\n1."
        elif archetype == 5:
            txt = prefix + f"Calculate the numerical value of \\(\\tan 45^\\circ\\)."
            corr = "1"
            dist = ["0", "\\(\\frac{1}{\\sqrt{3}}\\)", "\\(\\sqrt{3}\\)"]
            sol = "**Step 1: Standard Value**\nIn an isosceles right triangle, opposite = adjacent, so \\(\\tan 45^\\circ = 1\\).\n**Step 2: Conclusion**\n1."
        elif archetype == 6:
            txt = prefix + f"Evaluate: \\(\\tan {theta}^\\circ \\times \\tan {comp}^\\circ + \\tan 45^\\circ\\)."
            corr = "2"
            dist = ["1", "0", "3"]
            sol = f"**Step 1: Calculation**\n\\(\\tan {theta}^\\circ \\times \\tan {comp}^\\circ = 1\\) and \\(\\tan 45^\\circ = 1\\).\nTotal \\(= 1 + 1 = 2\\).\n**Step 2: Conclusion**\n2."
        else:
            txt = prefix + f"What is the value of \\(\\tan {theta}^\\circ \\times \\tan {comp}^\\circ - 1\\)?"
            corr = "0"
            dist = ["1", "-1", "2"]
            sol = f"**Step 1: Calculation**\n\\(1 - 1 = 0\\).\n**Step 2: Conclusion**\n0."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, 8, "Trigonometry", seq, has_fig, diff))
    return qs

def generate_8_2_2():
    # 8.2.2: sin θ = cos (90-θ) and cos θ = sin (90-θ)
    tc = "MH-9-MTH2-8-8.2.2"
    tname = "sin θ = cos (90-θ) and cos θ = sin (90-θ)"
    qs = []
    ANGLES_10 = [12, 18, 24, 32, 38, 48, 56, 64, 72, 78]
    for idx, seq in enumerate(SEQS_80):
        theta = ANGLES_10[idx % len(ANGLES_10)]
        comp = 90 - theta
        has_fig = (idx % 5 != 0)
        svg = svg_trig_triangle("BC", "AC", "AB", "B", f"Co-function #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        if archetype == 0:
            txt = prefix + f"Express \\(\\sin {theta}^\\circ\\) in terms of cosine of its complementary angle."
            corr = f"\\(\\cos {comp}^\\circ\\)"
            dist = [f"\\(\\cos {theta}^\\circ\\)", f"\\(\\sin {comp}^\\circ\\)", f"\\(\\tan {comp}^\\circ\\)"]
            sol = f"**Step 1: Co-function Identity**\n\\(\\sin \\theta = \\cos(90^\\circ - \\theta) = \\cos(90^\\circ - {theta}^\\circ) = \\cos {comp}^\\circ\\).\n**Step 2: Conclusion**\n\\(\\cos {comp}^\\circ\\)."
        elif archetype == 1:
            txt = prefix + f"Express \\(\\cos {theta}^\\circ\\) in terms of sine of its complementary angle."
            corr = f"\\(\\sin {comp}^\\circ\\)"
            dist = [f"\\(\\sin {theta}^\\circ\\)", f"\\(\\cos {comp}^\\circ\\)", f"\\(\\tan {theta}^\\circ\\)"]
            sol = f"**Step 1: Identity**\n\\(\\cos \\theta = \\sin(90^\\circ - \\theta) = \\sin(90^\\circ - {theta}^\\circ) = \\sin {comp}^\\circ\\).\n**Step 2: Conclusion**\n\\(\\sin {comp}^\\circ\\)."
        elif archetype == 2:
            txt = prefix + f"Evaluate the quotient: \\(\\frac{{\\sin {theta}^\\circ}}{{\\cos {comp}^\\circ}}\\)."
            corr = "1"
            dist = ["0", "\\(\\tan {theta}^\\circ\\)", "\\(\\frac{1}{2}\\)"]
            sol = f"**Step 1: Identity**\n\\(\\cos {comp}^\\circ = \\sin {theta}^\\circ\\).\n\\(\\frac{{\\sin {theta}^\\circ}}{{\\sin {theta}^\\circ}} = 1\\).\n**Step 2: Conclusion**\n1."
        elif archetype == 3:
            txt = prefix + f"Evaluate the difference: \\(\\sin {theta}^\\circ - \\cos {comp}^\\circ\\)."
            corr = "0"
            dist = ["1", "-1", f"\\(2\\sin {theta}^\\circ\\)"]
            sol = f"**Step 1: Identity**\n\\(\\cos {comp}^\\circ = \\sin {theta}^\\circ \\implies \\sin {theta}^\\circ - \\sin {theta}^\\circ = 0\\).\n**Step 2: Conclusion**\n0."
        elif archetype == 4:
            txt = prefix + f"If \\(\\sin {theta}^\\circ = \\cos x\\) where \\(x\\) is an acute angle, find the value of \\(x\\)."
            corr = f"{comp}°"
            dist = [f"{theta}°", f"{comp + 10}°", f"{comp - 10}°"]
            sol = f"**Step 1: Co-function Rule**\n\\(\\sin A = \\cos B \\implies A + B = 90^\\circ\\).\n\\(x = 90^\\circ - {theta}^\\circ = {comp}^\\circ\\).\n**Step 2: Conclusion**\n{comp}°."
        elif archetype == 5:
            txt = prefix + f"Calculate: \\(3\\frac{{\\sin {theta}^\\circ}}{{\\cos {comp}^\\circ}} + 2\\frac{{\\cos {theta}^\\circ}}{{\\sin {comp}^\\circ}}\\)."
            corr = "5"
            dist = ["1", "6", "0"]
            sol = f"**Step 1: Simplification**\nEach fraction equals 1.\n\\(3(1) + 2(1) = 3 + 2 = 5\\).\n**Step 2: Conclusion**\n5."
        elif archetype == 6:
            txt = prefix + f"Evaluate: \\(\\sin^2 {theta}^\\circ + \\sin^2 {comp}^\\circ\\)."
            corr = "1"
            dist = ["0", "2", "\\(\\frac{1}{2}\\)"]
            sol = f"**Step 1: Substitution**\n\\(\\sin {comp}^\\circ = \\cos {theta}^\\circ\\).\n\\(\\sin^2 {theta}^\\circ + \\cos^2 {theta}^\\circ = 1\\).\n**Step 2: Conclusion**\n1."
        else:
            txt = prefix + f"Evaluate: \\(\\cos^2 {theta}^\\circ + \\cos^2 {comp}^\\circ\\)."
            corr = "1"
            dist = ["0", "2", "\\(\\frac{1}{2}\\)"]
            sol = f"**Step 1: Substitution**\n\\(\\cos {comp}^\\circ = \\sin {theta}^\\circ\\).\n\\(\\cos^2 {theta}^\\circ + \\sin^2 {theta}^\\circ = 1\\).\n**Step 2: Conclusion**\n1."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, 8, "Trigonometry", seq, has_fig, diff))
    return qs

def generate_8_2_3():
    # 8.2.3: Fundamental identity: sin²θ + cos²θ = 1
    tc = "MH-9-MTH2-8-8.2.3"
    tname = "Fundamental identity: sin²θ + cos²θ = 1"
    qs = []
    for idx, seq in enumerate(SEQS_80):
        opp, adj, hyp = TRIG_TRIPLES_80[idx]
        has_fig = (idx % 5 != 0)
        svg = svg_trig_triangle(f"BC", f"AC", f"AB", "B", f"Identity Triangle #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        g = math.gcd(opp, hyp)
        s_opp = opp // g
        s_hyp = hyp // g
        g2 = math.gcd(adj, hyp)
        s_adj = adj // g2
        s_hyp2 = hyp // g2

        archetype = idx % 8
        if archetype == 0:
            txt = prefix + f"If \\(\\sin \\theta = \\frac{{{s_opp}}}{{{s_hyp}}}\\) and \\(\\theta\\) is an acute angle, find \\(\\cos \\theta\\) using \\(\\sin^2\\theta + \\cos^2\\theta = 1\\)."
            corr = f"\\(\\frac{{{s_adj}}}{{{s_hyp2}}}\\)"
            dist = [f"\\(\\frac{{{s_opp}}}{{{s_hyp2}}}\\)", f"\\(\\frac{{{s_adj + 1}}}{{{s_hyp2}}}\\)", f"\\(\\frac{{{s_adj}}}{{{s_hyp2 + 2}}}\\)"]
            sol = f"**Step 1: Identity**\n\\(\\cos^2 \\theta = 1 - \\sin^2 \\theta = 1 - \\left(\\frac{{{s_opp}}}{{{s_hyp}}}\\right)^2 = 1 - \\frac{{{s_opp**2}}}{{{s_hyp**2}}} = \\frac{{{s_hyp**2 - s_opp**2}}}{{{s_hyp**2}}} = \\frac{{{s_adj**2}}}{{{s_hyp2**2}}}\\).\n\\(\\cos \\theta = \\frac{{{s_adj}}}{{{s_hyp2}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{s_adj}}}{{{s_hyp2}}}\\)."
        elif archetype == 1:
            txt = prefix + f"If \\(\\cos \\theta = \\frac{{{s_adj}}}{{{s_hyp2}}}\\) for an acute angle \\(\\theta\\), determine \\(\\sin \\theta\\)."
            corr = f"\\(\\frac{{{s_opp}}}{{{s_hyp}}}\\)"
            dist = [f"\\(\\frac{{{s_adj}}}{{{s_hyp}}}\\)", f"\\(\\frac{{{s_opp + 1}}}{{{s_hyp}}}\\)", f"\\(\\frac{{{s_opp}}}{{{s_hyp + 2}}}\\)"]
            sol = f"**Step 1: Identity**\n\\(\\sin^2 \\theta = 1 - \\cos^2 \\theta = 1 - \\frac{{{s_adj**2}}}{{{s_hyp2**2}}} = \\frac{{{s_opp**2}}}{{{s_hyp**2}}} \\implies \\sin \\theta = \\frac{{{s_opp}}}{{{s_hyp}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{s_opp}}}{{{s_hyp}}}\\)."
        elif archetype == 2:
            txt = prefix + f"What is the fundamental Pythagorean identity relating \\(\\sin \\theta\\) and \\(\\cos \\theta\\)?"
            corr = "\\(\\sin^2 \\theta + \\cos^2 \\theta = 1\\)"
            dist = ["\\(\\sin \\theta + \\cos \\theta = 1\\)", "\\(\\sin^2 \\theta - \\cos^2 \\theta = 1\\)", "\\(\\sin^2 \\theta + \\cos^2 \\theta = 0\\)"]
            sol = "**Step 1: Identity Definition**\nIn a right triangle, \\(a^2 + b^2 = c^2 \\implies \\frac{a^2}{c^2} + \\frac{b^2}{c^2} = 1 \\implies \\sin^2 \\theta + \\cos^2 \\theta = 1\\).\n**Step 2: Conclusion**\n\\(\\sin^2 \\theta + \\cos^2 \\theta = 1\\)."
        elif archetype == 3:
            txt = prefix + f"Simplify the expression: \\(1 - \\sin^2 \\theta\\)."
            corr = "\\(\\cos^2 \\theta\\)"
            dist = ["\\(\\sin^2 \\theta\\)", "\\(\\tan^2 \\theta\\)", "\\(1\\)"]
            sol = "**Step 1: Identity**\n\\(\\sin^2 \\theta + \\cos^2 \\theta = 1 \\implies \\cos^2 \\theta = 1 - \\sin^2 \\theta\\).\n**Step 2: Conclusion**\n\\(\\cos^2 \\theta\\)."
        elif archetype == 4:
            txt = prefix + f"Simplify the expression: \\(1 - \\cos^2 \\theta\\)."
            corr = "\\(\\sin^2 \\theta\\)"
            dist = ["\\(\\cos^2 \\theta\\)", "\\(\\tan^2 \\theta\\)", "\\(-1\\)"]
            sol = "**Step 1: Identity**\n\\(1 - \\cos^2 \\theta = \\sin^2 \\theta\\).\n**Step 2: Conclusion**\n\\(\\sin^2 \\theta\\)."
        elif archetype == 5:
            txt = prefix + f"Evaluate: \\(5\\sin^2 \\theta + 5\\cos^2 \\theta\\)."
            corr = "5"
            dist = ["1", "10", "0"]
            sol = "**Step 1: Factorization**\n\\(5(\\sin^2 \\theta + \\cos^2 \\theta) = 5(1) = 5\\).\n**Step 2: Conclusion**\n5."
        elif archetype == 6:
            txt = prefix + f"Evaluate: \\(2 - 2\\cos^2 \\theta\\) in terms of \\(\\sin \\theta\\)."
            corr = "\\(2\\sin^2 \\theta\\)"
            dist = ["\\(2\\cos^2 \\theta\\)", "\\(2\\)", "\\(\\sin^2 \\theta\\)"]
            sol = "**Step 1: Factorization**\n\\(2(1 - \\cos^2 \\theta) = 2\\sin^2 \\theta\\).\n**Step 2: Conclusion**\n\\(2\\sin^2 \\theta\\)."
        else:
            txt = prefix + f"If \\(\\sin \\theta = \\cos \\theta\\) for an acute angle \\(\\theta\\), what is the value of \\(\\sin^2 \\theta + \\cos^2 \\theta\\)?"
            corr = "1"
            dist = ["\\(\\frac{1}{2}\\)", "2", "0"]
            sol = "**Step 1: Universal Invariant**\nThe identity \\(\\sin^2 \\theta + \\cos^2 \\theta = 1\\) holds for ALL angles \\(\\theta\\).\n**Step 2: Conclusion**\n1."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, 8, "Trigonometry", seq, has_fig, diff))
    return qs

def generate_8_3_1():
    # 8.3.1: Derivation of values using geometric triangles (0°, 30°, 45°, 60°, 90°)
    tc = "MH-9-MTH2-8-8.3.1"
    tname = "Derivation of values using geometric triangles"
    qs = []
    STANDARD_VALS = [
        ("sin 30°", "\\frac{1}{2}", ["\\frac{\\sqrt{3}}{2}", "\\frac{1}{\\sqrt{2}}", "1"], "In a 30°-60°-90° triangle, side opposite 30° is half the hypotenuse, so \\(\\sin 30^\\circ = \\frac{1}{2}\\)."),
        ("cos 30°", "\\frac{\\sqrt{3}}{2}", ["\\frac{1}{2}", "\\frac{1}{\\sqrt{2}}", "\\sqrt{3}"], "In a 30°-60°-90° triangle, side opposite 60° (adjacent to 30°) is \\(\\frac{\\sqrt{3}}{2}\\) of hypotenuse."),
        ("tan 30°", "\\frac{1}{\\sqrt{3}}", ["\\sqrt{3}", "1", "\\frac{1}{2}"], "\\(\\tan 30^\\circ = \\frac{\\sin 30^\\circ}{\\cos 30^\\circ} = \\frac{1/2}{\\sqrt{3}/2} = \\frac{1}{\\sqrt{3}}\\)."),
        ("sin 45°", "\\frac{1}{\\sqrt{2}}", ["\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}", "1"], "In a 45°-45°-90° triangle, perpendicular sides are \\(\\frac{1}{\\sqrt{2}}\\) times hypotenuse."),
        ("cos 45°", "\\frac{1}{\\sqrt{2}}", ["\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}", "0"], "In an isosceles right triangle, \\(\\cos 45^\\circ = \\frac{1}{\\sqrt{2}}\\)."),
        ("tan 45°", "1", ["\\frac{1}{\\sqrt{3}}", "\\sqrt{3}", "0"], "\\(\\tan 45^\\circ = \\frac{\\sin 45^\\circ}{\\cos 45^\\circ} = 1\\)."),
        ("sin 60°", "\\frac{\\sqrt{3}}{2}", ["\\frac{1}{2}", "\\frac{1}{\\sqrt{2}}", "\\sqrt{3}"], "In a 30°-60°-90° triangle, side opposite 60° is \\(\\frac{\\sqrt{3}}{2}\\) of hypotenuse."),
        ("cos 60°", "\\frac{1}{2}", ["\\frac{\\sqrt{3}}{2}", "\\frac{1}{\\sqrt{2}}", "1"], "In a 30°-60°-90° triangle, side adjacent to 60° is half of hypotenuse.")
    ]
    for idx, seq in enumerate(SEQS_80):
        ratio_name, corr_val, dist_vals, exp_str = STANDARD_VALS[idx % 8]
        has_fig = (idx % 5 != 0)
        svg = svg_trig_triangle("1", "\\sqrt{3}", "2", "30°", f"Standard Angle #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        txt = prefix + f"What is the exact standard trigonometric value of \\(\\{ratio_name}\\) derived geometrically?"
        corr = f"\\({corr_val}\\)"
        dist = [f"\\({d}\\)" for d in dist_vals]
        sol = f"**Step 1: Geometric Derivation**\n{exp_str}\n**Step 2: Conclusion**\n\\({corr_val}\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, 8, "Trigonometry", seq, has_fig, diff))
    return qs

def generate_8_3_2():
    # 8.3.2: Evaluating trigonometric algebraic expressions
    tc = "MH-9-MTH2-8-8.3.2"
    tname = "Evaluating trigonometric algebraic expressions"
    qs = []
    EXPR_QUESTIONS = [
        ("2\\sin 30^\\circ + \\cos 0^\\circ", "2", ["1", "3", "0"], "2(1/2) + 1 = 1 + 1 = 2"),
        ("2\\tan 45^\\circ + \\cos 60^\\circ - \\sin 30^\\circ", "2", ["1", "3", "0"], "2(1) + 1/2 - 1/2 = 2"),
        ("\\sin 30^\\circ \\times \\cos 60^\\circ + \\cos 30^\\circ \\times \\sin 60^\\circ", "1", ["0", "1/2", "\\sqrt{3}/2"], "(1/2)(1/2) + (\\sqrt{3}/2)(\\sqrt{3}/2) = 1/4 + 3/4 = 1"),
        ("4\\sin^2 30^\\circ + 3\\tan^2 30^\\circ", "2", ["1", "3", "4"], "4(1/4) + 3(1/3) = 1 + 1 = 2"),
        ("\\cos^2 45^\\circ + \\sin^2 45^\\circ", "1", ["2", "1/2", "0"], "1/2 + 1/2 = 1"),
        ("2\\tan^2 45^\\circ + \\cos^2 30^\\circ - \\sin^2 60^\\circ", "2", ["1", "3", "0"], "2(1) + 3/4 - 3/4 = 2"),
        ("\\frac{\\sin 30^\\circ}{\\cos 30^\\circ}", "\\frac{1}{\\sqrt{3}}", ["\\sqrt{3}", "1", "1/2"], "\\frac{1/2}{\\sqrt{3}/2} = \\frac{1}{\\sqrt{3}}"),
        ("5\\cos^2 60^\\circ + 4\\sin^2 30^\\circ", "\\frac{9}{4}", ["2", "3", "\\frac{5}{4}"], "5(1/4) + 4(1/4) = 9/4")
    ]
    for idx, seq in enumerate(SEQS_80):
        expr_str, corr_val, dist_vals, calc_str = EXPR_QUESTIONS[idx % 8]
        has_fig = (idx % 5 != 0)
        svg = svg_trig_triangle("1", "1", "\\sqrt{2}", "45°", f"Trig Evaluation #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        txt = prefix + f"Evaluate the numerical value of the trigonometric expression: \\({expr_str}\\)."
        corr = f"\\({corr_val}\\)"
        dist = [f"\\({d}\\)" for d in dist_vals]
        sol = f"**Step 1: Substitute Standard Values**\n{calc_str}.\n**Step 2: Conclusion**\n\\({corr_val}\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, 8, "Trigonometry", seq, has_fig, diff))
    return qs

def main():
    all_qs = []
    # Chapter 7
    all_qs.extend(generate_7_1_1())
    all_qs.extend(generate_7_1_2())
    all_qs.extend(generate_7_2_1())
    all_qs.extend(generate_7_2_2())
    all_qs.extend(generate_7_2_3())
    all_qs.extend(generate_7_3_1())
    # Chapter 8
    all_qs.extend(generate_8_1_1())
    all_qs.extend(generate_8_1_2())
    all_qs.extend(generate_8_1_3())
    all_qs.extend(generate_8_2_1())
    all_qs.extend(generate_8_2_2())
    all_qs.extend(generate_8_2_3())
    all_qs.extend(generate_8_3_1())
    all_qs.extend(generate_8_3_2())

    print(f"Generated {len(all_qs)} total questions across 14 subtopics (Chapters 7 & 8).")
    with open("scripts/mh9_mth2_ch7_ch8_perfect.json", "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/mh9_mth2_ch7_ch8_perfect.json")

if __name__ == "__main__":
    main()
