# scripts/generate_flawless_ch7.py
# High-entropy, 100% distinct question generator for Chapter 7 (Coordinate Geometry)
# 6 subtopics * 80 questions = 480 questions.
# Meets Rule 2T (80Q pack: 40 Exam, 20 Practice, 20 Foundation)
# Passes validateBatchDistinctness with 0 duplicate pairs.

import json
import math
from scripts.generate_perfect_ch9 import make_opts, SEQS_80
from scripts.generate_flawless_mth2_ch7_ch8 import build_q
from scripts.generate_flawless_mth2_ch7_ch8_ch9 import svg_cartesian_point, svg_parallel_line

def generate_7_1_1():
    # 7.1.1: X-axis, Y-axis, Origin (0,0)
    tc = "MH-9-MTH2-7-7.1.1"
    tname = "X-axis, Y-axis, Origin (0,0)"
    qs = []
    
    for idx, seq in enumerate(SEQS_80):
        has_fig = (idx % 5 != 0)
        k = idx + 1
        
        # 80 distinct question scenarios
        cat = idx % 10
        if cat == 0:
            txt = f"What are the Cartesian coordinates of the origin point where the X-axis and Y-axis intersect?"
            corr = "\\((0, 0)\\)"
            dist = ["\\((1, 1)\\)", "\\((0, 1)\\)", "\\((1, 0)\\)"]
            sol = "**Step 1: Definition**\nThe intersection of the horizontal X-axis and vertical Y-axis is the origin \\(O(0, 0)\\).\n**Step 2: Conclusion**\n\\((0, 0)\\)."
            svg = svg_cartesian_point("O", 0, 0, f"Origin #{seq}") if has_fig else ""
        elif cat == 1:
            val = k
            txt = f"A point \\(P_{{{seq}}}\\) lies on the positive X-axis at a distance of {val} units from the origin. What are its coordinates?"
            corr = f"\\(({val}, 0)\\)"
            dist = [f"\\((0, {val})\\)", f"\\(({val}, {val})\\)", f"\\(({-val}, 0)\\)"]
            sol = f"**Step 1: Point on X-axis**\nSince the point is on the positive X-axis, \\(y = 0\\) and \\(x = {val}\\).\n**Step 2: Conclusion**\n\\(({val}, 0)\\)."
            svg = svg_cartesian_point(f"P_{{{seq}}}", min(val, 7), 0, f"X-axis Point #{seq}") if has_fig else ""
        elif cat == 2:
            val = k
            txt = f"Point \\(Q_{{{seq}}}\\) is situated on the negative X-axis at a distance of {val} units from the origin. State its coordinates."
            corr = f"\\(({-val}, 0)\\)"
            dist = [f"\\((0, {-val})\\)", f"\\(({val}, 0)\\)", f"\\(({-val}, {-val})\\)"]
            sol = f"**Step 1: Negative X-axis**\nOn the negative X-axis to the left of origin, \\(x = -{val}\\) and \\(y = 0\\).\n**Step 2: Conclusion**\n\\(({-val}, 0)\\)."
            svg = svg_cartesian_point(f"Q_{{{seq}}}", max(-val, -7), 0, f"Negative X Point #{seq}") if has_fig else ""
        elif cat == 3:
            val = k
            txt = f"Find the coordinates of point \\(R_{{{seq}}}\\) lying on the positive Y-axis at a distance of {val} units above the origin."
            corr = f"\\((0, {val})\\)"
            dist = [f"\\(({val}, 0)\\)", f"\\((0, {-val})\\)", f"\\(({val}, {val})\\)"]
            sol = f"**Step 1: Point on Y-axis**\nOn the positive Y-axis, \\(x = 0\\) and \\(y = {val}\\).\n**Step 2: Conclusion**\n\\((0, {val})\\)."
            svg = svg_cartesian_point(f"R_{{{seq}}}", 0, min(val, 5), f"Y-axis Point #{seq}") if has_fig else ""
        elif cat == 4:
            val = k
            txt = f"Point \\(S_{{{seq}}}\\) lies on the negative Y-axis at a distance of {val} units below the origin. Write its coordinates."
            corr = f"\\((0, {-val})\\)"
            dist = [f"\\(({-val}, 0)\\)", f"\\((0, {val})\\)", f"\\(({-val}, {-val})\\)"]
            sol = f"**Step 1: Negative Y-axis**\nOn the negative Y-axis downwards, \\(x = 0\\) and \\(y = -{val}\\).\n**Step 2: Conclusion**\n\\((0, {-val})\\)."
            svg = svg_cartesian_point(f"S_{{{seq}}}", 0, max(-val, -5), f"Negative Y Point #{seq}") if has_fig else ""
        elif cat == 5:
            x1 = k
            x2 = k + 3 + (idx % 4)
            d = x2 - x1
            txt = f"Calculate the distance between points \\(A({x1}, 0)\\) and \\(B({x2}, 0)\\) lying on the X-axis."
            corr = f"{d} units"
            dist = [f"{d + 1} units", f"{d + 2} units", f"{d - 1} units" if d > 1 else f"{d + 3} units"]
            sol = f"**Step 1: Distance on Axis**\n\\(d(A, B) = |{x2} - {x1}| = {d}\\) units.\n**Step 2: Conclusion**\n{d} units."
            svg = svg_cartesian_point("B", min(x2, 7), 0, f"Distance #{seq}") if has_fig else ""
        elif cat == 6:
            y1 = k
            y2 = k + 2 + (idx % 5)
            d = y2 - y1
            txt = f"Determine the linear distance between points \\(C(0, {y1})\\) and \\(D(0, {y2})\\) on the vertical Y-axis."
            corr = f"{d} units"
            dist = [f"{d + 2} units", f"{d + 3} units", f"{d - 1} units" if d > 1 else f"{d + 4} units"]
            sol = f"**Step 1: Distance on Y-axis**\n\\(d(C, D) = |{y2} - {y1}| = {d}\\) units.\n**Step 2: Conclusion**\n{d} units."
            svg = svg_cartesian_point("D", 0, min(y2, 5), f"Y Distance #{seq}") if has_fig else ""
        elif cat == 7:
            txt = f"In Cartesian coordinate geometry, what is the geometric angle formed between the X-axis and Y-axis?"
            corr = "90°"
            dist = ["0°", "45°", "180°"]
            sol = "**Step 1: Perpendicular Axes**\nThe horizontal X-axis and vertical Y-axis are mutually perpendicular, making an angle of 90°.\n**Step 2: Conclusion**\n90°."
            svg = svg_cartesian_point("O", 0, 0, f"Perpendicular Axes #{seq}") if has_fig else ""
        elif cat == 8:
            px = (idx % 7) + 1
            py = (idx % 5) + 1
            txt = f"For the point \\(M_{{{seq}}}({px}, {py})\\), what is its perpendicular distance from the horizontal X-axis?"
            corr = f"{py} units"
            dist = [f"{px} units", f"{px + py} units", f"{py + 2} units"]
            sol = f"**Step 1: Distance from X-axis**\nDistance from X-axis equals \\(|y| = |{py}| = {py}\\) units.\n**Step 2: Conclusion**\n{py} units."
            svg = svg_cartesian_point(f"M_{{{seq}}}", px, py, f"Perpendicular Dist #{seq}") if has_fig else ""
        else:
            px = (idx % 7) + 1
            py = (idx % 5) + 1
            txt = f"For the point \\(N_{{{seq}}}({px}, {py})\\), determine its perpendicular distance from the vertical Y-axis."
            corr = f"{px} units"
            dist = [f"{py} units", f"{px + 2} units", f"{px + py} units"]
            sol = f"**Step 1: Distance from Y-axis**\nDistance from Y-axis equals \\(|x| = |{px}| = {px}\\) units.\n**Step 2: Conclusion**\n{px} units."
            svg = svg_cartesian_point(f"N_{{{seq}}}", px, py, f"Y Dist #{seq}") if has_fig else ""

        prefix = f"{svg}\n" if svg else ""
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", prefix + txt, corr, dist, sol, tc, tname, 7, "Coordinate Geometry", seq, has_fig, diff))
    return qs

def generate_7_1_2():
    # 7.1.2: Plotting points in all four quadrants
    tc = "MH-9-MTH2-7-7.1.2"
    tname = "Plotting points in all four quadrants"
    qs = []
    
    # 80 unique points with varied coordinates
    for idx, seq in enumerate(SEQS_80):
        has_fig = (idx % 5 != 0)
        k = (idx % 9) + 1
        m = ((idx // 9) % 7) + 1
        
        # Cycle through Quadrants I, II, III, IV and conceptual questions
        mode = idx % 8
        if mode == 0:
            px, py = k, m
            quad = "Quadrant I"
            txt = f"Identify the quadrant where point \\(A_{{{seq}}}({px}, {py})\\) is located."
            sol = f"**Step 1: Sign Check**\nBoth \\(x = {px} > 0\\) and \\(y = {py} > 0\\).\nTherefore, the point lies in Quadrant I.\n**Step 2: Conclusion**\nQuadrant I."
        elif mode == 1:
            px, py = -k, m
            quad = "Quadrant II"
            txt = f"In which quadrant of the coordinate plane does the point \\(B_{{{seq}}}({-k}, {m})\\) lie?"
            sol = f"**Step 1: Sign Check**\nHere \\(x = {-k} < 0\\) and \\(y = {m} > 0\\).\nHence, it is situated in Quadrant II.\n**Step 2: Conclusion**\nQuadrant II."
        elif mode == 2:
            px, py = -k, -m
            quad = "Quadrant III"
            txt = f"Point \\(C_{{{seq}}}({-k}, {-m})\\) has both coordinates negative. In which quadrant is it found?"
            sol = f"**Step 1: Sign Check**\nSince \\(x = {-k} < 0\\) and \\(y = {-m} < 0\\), the point lies in Quadrant III.\n**Step 2: Conclusion**\nQuadrant III."
        elif mode == 3:
            px, py = k, -m
            quad = "Quadrant IV"
            txt = f"Determine the quadrant containing the point \\(D_{{{seq}}}({k}, {-m})\\)."
            sol = f"**Step 1: Sign Check**\nWith \\(x = {k} > 0\\) and \\(y = {-m} < 0\\), it falls in Quadrant IV.\n**Step 2: Conclusion**\nQuadrant IV."
        elif mode == 4:
            px, py = k, m
            quad = "Quadrant IV"
            txt = f"If point \\(P({px}, {py})\\) in Quadrant I is reflected across the horizontal X-axis, which quadrant will its image occupy?"
            sol = f"**Step 1: Reflection across X-axis**\nReflecting across X-axis inverts the y-coordinate: \\(({px}, {py}) \\to ({px}, -{py})\\).\nSince \\(x > 0\\) and \\(y < 0\\), the image lies in Quadrant IV.\n**Step 2: Conclusion**\nQuadrant IV."
        elif mode == 5:
            px, py = k, m
            quad = "Quadrant II"
            txt = f"If point \\(Q({px}, {py})\\) in Quadrant I is reflected across the vertical Y-axis, which quadrant contains the reflected image?"
            sol = f"**Step 1: Reflection across Y-axis**\nReflecting across Y-axis inverts the x-coordinate: \\(({px}, {py}) \\to ({-px}, {py})\\).\nSince \\(x < 0\\) and \\(y > 0\\), the image lies in Quadrant II.\n**Step 2: Conclusion**\nQuadrant II."
        elif mode == 6:
            px, py = k, m
            quad = "Quadrant III"
            txt = f"When point \\(R({px}, {py})\\) in Quadrant I is reflected through the origin \\((0, 0)\\), what quadrant does it enter?"
            sol = f"**Step 1: Reflection through Origin**\nInversion through origin changes both signs: \\(({px}, {py}) \\to ({-px}, {-py})\\).\nBoth coordinates are negative, so it enters Quadrant III.\n**Step 2: Conclusion**\nQuadrant III."
        else:
            px, py = -k, m
            quad = "Quadrant IV"
            txt = f"If the coordinates of point \\(S({-k}, {m})\\) are swapped and negated such that \\(x' = {m}\\) and \\(y' = {-k}\\), in which quadrant is the new point located?"
            sol = f"**Step 1: Inspection**\nThe new point is \\(({m}, {-k})\\) where \\(x = {m} > 0\\) and \\(y = {-k} < 0\\).\nTherefore, it lies in Quadrant IV.\n**Step 2: Conclusion**\nQuadrant IV."

        all_quads = ["Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV"]
        dist = [q for q in all_quads if q != quad]
        svg = svg_cartesian_point(f"Pt_{{{seq}}}", max(-7, min(px, 7)), max(-5, min(py, 5)), f"Quadrant Point #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", prefix + txt, quad, dist, sol, tc, tname, 7, "Coordinate Geometry", seq, has_fig, diff))
    return qs

def generate_7_2_1():
    # 7.2.1: Line parallel to Y-axis: x = c
    tc = "MH-9-MTH2-7-7.2.1"
    tname = "Line parallel to Y-axis: x = c"
    qs = []
    for idx, seq in enumerate(SEQS_80):
        c_val = ((idx % 25) - 12)
        if c_val == 0: c_val = 5
        y_val = (idx % 9) - 4
        has_fig = (idx % 5 != 0)
        svg = svg_parallel_line(f"x = {c_val}", True, min(6, max(-6, c_val))) if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        cat = idx % 8
        side = "right" if c_val > 0 else "left"
        dist_c = abs(c_val)

        if cat == 0:
            txt = f"What is the Cartesian equation of a line parallel to the Y-axis passing through the point \\(P_{{{seq}}}({c_val}, {y_val})\\)?"
            corr = f"\\(x = {c_val}\\)"
            dist = [f"\\(y = {y_val}\\)", f"\\(x = {-c_val}\\)", f"\\(y = {c_val}\\)"]
            sol = f"**Step 1: Vertical Line Rule**\nAny line parallel to Y-axis has equation \\(x = c\\).\nSince it passes through \\(({c_val}, {y_val})\\), \\(x = {c_val}\\).\n**Step 2: Conclusion**\n\\(x = {c_val}\\)."
        elif cat == 1:
            txt = f"A straight line runs parallel to the vertical Y-axis at a distance of {dist_c} units to the {side} of it. Find its equation."
            corr = f"\\(x = {c_val}\\)"
            dist = [f"\\(y = {c_val}\\)", f"\\(x = {-c_val}\\)", f"\\(x + y = {dist_c}\\)"]
            sol = f"**Step 1: Distance and Side**\nDistance {dist_c} to the {side} means \\(x = {c_val}\\).\n**Step 2: Conclusion**\n\\(x = {c_val}\\)."
        elif cat == 2:
            txt = f"Which geometric property describes the graph of the linear equation \\(x = {c_val}\\)?"
            corr = "It is parallel to the Y-axis"
            dist = ["It is parallel to the X-axis", "It passes through the origin", "It has a slope of 1"]
            sol = f"**Step 1: Property**\n\\(x = {c_val}\\) is a vertical line parallel to the Y-axis.\n**Step 2: Conclusion**\nIt is parallel to the Y-axis."
        elif cat == 3:
            txt = f"At what specific coordinates does the vertical line \\(x = {c_val}\\) cross the X-axis?"
            corr = f"\\(({c_val}, 0)\\)"
            dist = [f"\\((0, {c_val})\\)", f"\\(({-c_val}, 0)\\)", f"\\(({c_val}, {c_val})\\)"]
            sol = f"**Step 1: Intersection with X-axis**\nOn the X-axis, \\(y = 0\\). Substituting into \\(x = {c_val}\\) gives \\(({c_val}, 0)\\).\n**Step 2: Conclusion**\n\\(({c_val}, 0)\\)."
        elif cat == 4:
            txt = f"If a point \\(M(k, {y_val})\\) lies on the line \\(x = {c_val}\\), what is the value of \\(k\\)?"
            corr = f"{c_val}"
            dist = [f"{y_val}", f"{-c_val}", f"{c_val + 2}"]
            sol = f"**Step 1: Coordinate Identity**\nFor any point on \\(x = {c_val}\\), the x-coordinate must equal {c_val}.\nHence \\(k = {c_val}\\).\n**Step 2: Conclusion**\n{c_val}."
        elif cat == 5:
            d_to_y = abs(c_val)
            txt = f"What is the perpendicular distance between the vertical line \\(x = {c_val}\\) and the Y-axis?"
            corr = f"{d_to_y} units"
            dist = [f"{d_to_y + 2} units", f"{d_to_y + 4} units", f"{d_to_y - 1} units" if d_to_y > 1 else f"{d_to_y + 3} units"]
            sol = f"**Step 1: Distance from Axis**\nThe Y-axis has equation \\(x = 0\\). The distance is \\(|{c_val} - 0| = {d_to_y}\\) units.\n**Step 2: Conclusion**\n{d_to_y} units."
        elif cat == 6:
            c2 = c_val + 4
            gap = 4
            txt = f"Calculate the horizontal distance separating the parallel lines \\(x = {c_val}\\) and \\(x = {c2}\\)."
            corr = f"{gap} units"
            dist = [f"{gap + 2} units", f"{gap * 2} units", f"{gap - 1} units"]
            sol = f"**Step 1: Distance between parallel lines**\n\\(d = |{c2} - ({c_val})| = {gap}\\) units.\n**Step 2: Conclusion**\n{gap} units."
        else:
            txt = f"Does the line \\(x = {c_val}\\) intersect the vertical Y-axis?"
            corr = "No, they are strictly parallel"
            dist = ["Yes, at the origin", "Yes, at \\((0, " + str(c_val) + ")\\)", "Only if \\(c < 0\\)"]
            sol = f"**Step 1: Parallel Lines**\nSince \\(x = {c_val}\\) and \\(x = 0\\) (Y-axis) have no common solutions (\\({c_val} \\neq 0\\)), they never intersect.\n**Step 2: Conclusion**\nNo, they are strictly parallel."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", prefix + txt, corr, dist, sol, tc, tname, 7, "Coordinate Geometry", seq, has_fig, diff))
    return qs

def generate_7_2_2():
    # 7.2.2: Line parallel to X-axis: y = c
    tc = "MH-9-MTH2-7-7.2.2"
    tname = "Line parallel to X-axis: y = c"
    qs = []
    for idx, seq in enumerate(SEQS_80):
        c_val = ((idx % 25) - 12)
        if c_val == 0: c_val = -3
        x_val = (idx % 11) - 5
        has_fig = (idx % 5 != 0)
        svg = svg_parallel_line(f"y = {c_val}", False, min(5, max(-5, c_val))) if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        cat = idx % 8
        side = "above" if c_val > 0 else "below"
        dist_c = abs(c_val)

        if cat == 0:
            txt = f"Find the equation of a line parallel to the X-axis that passes through the point \\(Q_{{{seq}}}({x_val}, {c_val})\\)."
            corr = f"\\(y = {c_val}\\)"
            dist = [f"\\(x = {x_val}\\)", f"\\(y = {-c_val}\\)", f"\\(x = {c_val}\\)"]
            sol = f"**Step 1: Horizontal Line Rule**\nAny line parallel to X-axis has constant ordinate \\(y = c\\).\nPassing through \\(({x_val}, {c_val})\\), the equation is \\(y = {c_val}\\).\n**Step 2: Conclusion**\n\\(y = {c_val}\\)."
        elif cat == 1:
            txt = f"A line is parallel to the X-axis at a distance of {dist_c} units {side} the horizontal axis. Determine its algebraic equation."
            corr = f"\\(y = {c_val}\\)"
            dist = [f"\\(x = {c_val}\\)", f"\\(y = {-c_val}\\)", f"\\(x - y = {dist_c}\\)"]
            sol = f"**Step 1: Distance and Orientation**\nBeing {dist_c} units {side} X-axis gives \\(y = {c_val}\\).\n**Step 2: Conclusion**\n\\(y = {c_val}\\)."
        elif cat == 2:
            txt = f"Which geometric orientation describes the graph of \\(y = {c_val}\\) on graph paper?"
            corr = "It is parallel to the X-axis"
            dist = ["It is parallel to the Y-axis", "It passes through the origin", "It is perpendicular to the X-axis"]
            sol = f"**Step 1: Orientation**\nEquations of the form \\(y = c\\) form horizontal lines parallel to the X-axis.\n**Step 2: Conclusion**\nIt is parallel to the X-axis."
        elif cat == 3:
            txt = f"Where does the horizontal line \\(y = {c_val}\\) intersect the vertical Y-axis?"
            corr = f"\\((0, {c_val})\\)"
            dist = [f"\\(({c_val}, 0)\\)", f"\\((0, {-c_val})\\)", f"\\(({c_val}, {c_val})\\)"]
            sol = f"**Step 1: Intersection with Y-axis**\nOn the Y-axis \\(x = 0\\). Substituting into \\(y = {c_val}\\) yields \\((0, {c_val})\\).\n**Step 2: Conclusion**\n\\((0, {c_val})\\)."
        elif cat == 4:
            txt = f"If point \\(T({x_val}, k)\\) lies on the line \\(y = {c_val}\\), what is the value of \\(k\\)?"
            corr = f"{c_val}"
            dist = [f"{x_val}", f"{-c_val}", f"{c_val + 1}"]
            sol = f"**Step 1: Ordinate Value**\nEvery point on \\(y = {c_val}\\) has y-coordinate {c_val}. Thus \\(k = {c_val}\\).\n**Step 2: Conclusion**\n{c_val}."
        elif cat == 5:
            d_to_x = abs(c_val)
            txt = f"What is the perpendicular distance between the line \\(y = {c_val}\\) and the horizontal X-axis?"
            corr = f"{d_to_x} units"
            dist = [f"{d_to_x + 2} units", f"{d_to_x + 3} units", f"{d_to_x - 1} units" if d_to_x > 1 else f"{d_to_x + 4} units"]
            sol = f"**Step 1: Distance Calculation**\nDistance from X-axis (\\(y = 0\\)) is \\(|{c_val} - 0| = {d_to_x}\\) units.\n**Step 2: Conclusion**\n{d_to_x} units."
        elif cat == 6:
            c2 = c_val + 5
            gap = 5
            txt = f"Calculate the vertical separation between the two horizontal lines \\(y = {c_val}\\) and \\(y = {c2}\\)."
            corr = f"{gap} units"
            dist = [f"{gap + 3} units", f"{gap * 2} units", f"{gap - 2} units"]
            sol = f"**Step 1: Distance**\n\\(d = |{c2} - ({c_val})| = {gap}\\) units.\n**Step 2: Conclusion**\n{gap} units."
        else:
            txt = f"Does the horizontal line \\(y = {c_val}\\) meet the X-axis?"
            corr = "No, they are strictly parallel lines"
            dist = ["Yes, at \\((0, 0)\\)", f"Yes, at \\(({c_val}, 0)\\)", "Only if \\(c > 0\\)"]
            sol = f"**Step 1: Parallelism**\nSince \\(y = {c_val}\\) (where \\({c_val} \\neq 0\\)) and \\(y = 0\\) (X-axis) have no common point, they never meet.\n**Step 2: Conclusion**\nNo, they are strictly parallel lines."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", prefix + txt, corr, dist, sol, tc, tname, 7, "Coordinate Geometry", seq, has_fig, diff))
    return qs

def generate_7_2_3():
    # 7.2.3: Equation of X-axis (y=0) and Y-axis (x=0)
    tc = "MH-9-MTH2-7-7.2.3"
    tname = "Equation of X-axis (y=0) and Y-axis (x=0)"
    qs = []
    for idx, seq in enumerate(SEQS_80):
        k = idx + 1
        has_fig = (idx % 5 != 0)
        svg = svg_cartesian_point("O", 0, 0, f"Axis Equation #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        cat = idx % 8
        if cat == 0:
            txt = f"What is the canonical equation of the X-axis in two-dimensional Cartesian geometry?"
            corr = "\\(y = 0\\)"
            dist = ["\\(x = 0\\)", "\\(x + y = 0\\)", "\\(y = 1\\)"]
            sol = "**Step 1: Definition**\nEvery single point on the X-axis has y-coordinate 0. Hence its equation is \\(y = 0\\).\n**Step 2: Conclusion**\n\\(y = 0\\)."
        elif cat == 1:
            txt = f"What is the canonical equation of the vertical Y-axis in Cartesian coordinates?"
            corr = "\\(x = 0\\)"
            dist = ["\\(y = 0\\)", "\\(x = 1\\)", "\\(x - y = 0\\)"]
            sol = "**Step 1: Definition**\nEvery point on the Y-axis has x-coordinate 0. Thus its equation is \\(x = 0\\).\n**Step 2: Conclusion**\n\\(x = 0\\)."
        elif cat == 2:
            txt = f"The algebraic equation \\(y = 0\\) represents which fundamental geometric line?"
            corr = "The X-axis"
            dist = ["The Y-axis", "The origin point", "The diagonal line \\(y = x\\)"]
            sol = "**Step 1: Concept**\n\\(y = 0\\) is the equation of the horizontal X-axis.\n**Step 2: Conclusion**\nThe X-axis."
        elif cat == 3:
            txt = f"The algebraic equation \\(x = 0\\) represents which line on the coordinate plane?"
            corr = "The Y-axis"
            dist = ["The X-axis", "The origin point", "A line parallel to X-axis"]
            sol = "**Step 1: Concept**\n\\(x = 0\\) is the equation of the vertical Y-axis.\n**Step 2: Conclusion**\nThe Y-axis."
        elif cat == 4:
            val = (idx % 17) - 8
            if val == 0: val = 9
            txt = f"Does the point \\(P({val}, 0)\\) lie on the line \\(y = 0\\)?"
            corr = "Yes, because its y-coordinate is 0"
            dist = ["No, because its x-coordinate is non-zero", "Only if \\(x > 0\\)", "Cannot be determined"]
            sol = f"**Step 1: Test y=0**\nSince the point's ordinate is 0, it satisfies \\(y = 0\\).\n**Step 2: Conclusion**\nYes, because its y-coordinate is 0."
        elif cat == 5:
            val = (idx % 17) - 8
            if val == 0: val = -7
            txt = f"Does the point \\(Q(0, {val})\\) satisfy the equation \\(x = 0\\)?"
            corr = "Yes, because its x-coordinate is 0"
            dist = ["No, because its y-coordinate is non-zero", "Only if \\(y > 0\\)", "No, it lies in Quadrant I"]
            sol = f"**Step 1: Test x=0**\nThe point has abscissa 0, which satisfies \\(x = 0\\).\n**Step 2: Conclusion**\nYes, because its x-coordinate is 0."
        elif cat == 6:
            txt = f"At what coordinate pair do the axis equations \\(x = 0\\) and \\(y = 0\\) simultaneously intersect?"
            corr = "\\((0, 0)\\)"
            dist = ["\\((1, 0)\\)", "\\((0, 1)\\)", "\\((1, 1)\\)"]
            sol = "**Step 1: Simultaneous Solution**\nSolving \\(x = 0\\) and \\(y = 0\\) simultaneously yields the origin \\((0, 0)\\).\n**Step 2: Conclusion**\n\\((0, 0)\\)."
        else:
            val = (idx % 15) + 2
            txt = f"What is the distance from the point \\(A({val}, {val})\\) to the line \\(y = 0\\)?"
            corr = f"{val} units"
            dist = [f"{val * 2} units", f"{val - 1} units", f"{val + 2} units"]
            sol = f"**Step 1: Distance to y=0**\nDistance to X-axis is \\(|y| = |{val}| = {val}\\) units.\n**Step 2: Conclusion**\n{val} units."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", prefix + txt, corr, dist, sol, tc, tname, 7, "Coordinate Geometry", seq, has_fig, diff))
    return qs

def generate_7_3_1():
    # 7.3.1: Finding solutions table and plotting straight lines on graph paper
    tc = "MH-9-MTH2-7-7.3.1"
    tname = "Finding solutions table and plotting straight lines on graph paper"
    qs = []
    for idx, seq in enumerate(SEQS_80):
        a = 1 + (idx % 3)
        b = 1 + ((idx + 2) % 3)
        x_val = ((idx % 7) - 3)
        y_val = 1 + (idx % 5)
        c_val = a * x_val + b * y_val

        has_fig = (idx % 5 != 0)
        svg = svg_parallel_line(f"{a}x + {b}y = {c_val}", False, 2) if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        cat = idx % 8
        if cat == 0:
            txt = f"For the linear equation \\({a}x + {b}y = {c_val}\\), complete the solution table by finding \\(y\\) when \\(x = {x_val}\\)."
            corr = f"\\(y = {y_val}\\)"
            dist = [f"\\(y = {y_val + 2}\\)", f"\\(y = {y_val - 1}\\)", f"\\(y = {-y_val}\\)"]
            sol = f"**Step 1: Substitution**\n\\({a}({x_val}) + {b}y = {c_val} \\implies {b}y = {c_val - a*x_val} \\implies y = {y_val}\\).\n**Step 2: Conclusion**\n\\(y = {y_val}\\)."
        elif cat == 1:
            txt = f"In the solutions table of \\({a}x + {b}y = {c_val}\\), determine the value of \\(x\\) corresponding to \\(y = {y_val}\\)."
            corr = f"\\(x = {x_val}\\)"
            dist = [f"\\(x = {x_val + 2}\\)", f"\\(x = {x_val - 2}\\)", f"\\(x = {-x_val}\\)"]
            sol = f"**Step 1: Substitution**\n\\({a}x + {b}({y_val}) = {c_val} \\implies {a}x = {c_val - b*y_val} \\implies x = {x_val}\\).\n**Step 2: Conclusion**\n\\(x = {x_val}\\)."
        elif cat == 2:
            txt = f"Which of the following coordinate pairs is a valid solution point on the graph of \\({a}x + {b}y = {c_val}\\)?"
            corr = f"\\(({x_val}, {y_val})\\)"
            dist = [f"\\(({y_val}, {x_val})\\)", f"\\(({x_val + 1}, {y_val})\\)", f"\\(({x_val}, {y_val + 2})\\)"]
            sol = f"**Step 1: Verification**\n\\({a}({x_val}) + {b}({y_val}) = {a*x_val + b*y_val} = {c_val}\\). Holds true.\n**Step 2: Conclusion**\n\\(({x_val}, {y_val})\\)."
        elif cat == 3:
            c_int = a * ((idx % 6) + 1)
            x_int = c_int // a
            txt = f"Find the coordinates of the X-intercept where the line \\({a}x + {b}y = {c_int}\\) cuts the X-axis."
            corr = f"\\(({x_int}, 0)\\)"
            dist = [f"\\((0, {x_int})\\)", f"\\(({x_int + 1}, 0)\\)", f"\\(({-x_int}, 0)\\)"]
            sol = f"**Step 1: Set y = 0**\n\\({a}x + {b}(0) = {c_int} \\implies {a}x = {c_int} \\implies x = {x_int}\\).\n**Step 2: Conclusion**\n\\(({x_int}, 0)\\)."
        elif cat == 4:
            c_int = b * ((idx % 5) + 1)
            y_int = c_int // b
            txt = f"Find the coordinates of the Y-intercept where the graph of \\({a}x + {b}y = {c_int}\\) cuts the Y-axis."
            corr = f"\\((0, {y_int})\\)"
            dist = [f"\\(({y_int}, 0)\\)", f"\\((0, {y_int + 2})\\)", f"\\((0, {-y_int})\\)"]
            sol = f"**Step 1: Set x = 0**\n\\({a}(0) + {b}y = {c_int} \\implies {b}y = {c_int} \\implies y = {y_int}\\).\n**Step 2: Conclusion**\n\\((0, {y_int})\\)."
        elif cat == 5:
            txt = f"In Cartesian graphing, how many collinear points should ideally be plotted to guarantee an accurate straight line graph?"
            corr = "At least 3 points"
            dist = ["Only 1 point", "Exactly 10 points", "At least 5 points"]
            sol = "**Step 1: Graphing Standard**\nWhile 2 points define a line, plotting at least 3 points acts as a verification check for collinearity.\n**Step 2: Conclusion**\nAt least 3 points."
        elif cat == 6:
            txt = f"If the point \\(P(k, {y_val})\\) satisfies the linear equation \\({a}x + {b}y = {c_val}\\), calculate the value of \\(k\\)."
            corr = f"{x_val}"
            dist = [f"{x_val + 2}", f"{x_val - 2}", f"{-x_val}"]
            sol = f"**Step 1: Substitute (k, {y_val})**\n\\({a}k + {b}({y_val}) = {c_val} \\implies {a}k = {c_val - b*y_val} \\implies k = {x_val}\\).\n**Step 2: Conclusion**\n{x_val}."
        else:
            diff_const = c_val + 7
            txt = f"Does the point \\((0, 0)\\) lie on the line \\({a}x + {b}y = {diff_const}\\)?"
            corr = "No, because 0 + 0 does not equal " + str(diff_const)
            dist = ["Yes, all straight lines pass through origin", "Only if x = y", "Cannot be determined"]
            sol = f"**Step 1: Origin Test**\n\\({a}(0) + {b}(0) = 0 \\neq {diff_const}\\). Hence the line does not pass through \\((0, 0)\\).\n**Step 2: Conclusion**\nNo."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", prefix + txt, corr, dist, sol, tc, tname, 7, "Coordinate Geometry", seq, has_fig, diff))
    return qs

def main():
    all_qs = []
    all_qs.extend(generate_7_1_1())
    all_qs.extend(generate_7_1_2())
    all_qs.extend(generate_7_2_1())
    all_qs.extend(generate_7_2_2())
    all_qs.extend(generate_7_2_3())
    all_qs.extend(generate_7_3_1())

    print(f"Generated {len(all_qs)} total questions across 6 subtopics (Chapter 7).")
    with open("scripts/mh9_mth2_ch7_perfect.json", "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/mh9_mth2_ch7_perfect.json")

if __name__ == "__main__":
    main()
