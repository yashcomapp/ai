# scripts/generate_ch5_all.py
import json
from scripts.build_ch4_5 import (
    SEQS_80, build_q, svg_parallelogram, svg_parallelogram_diagonals,
    svg_rectangle, svg_rhombus, svg_square, svg_midpoint
)

CH_NUM = 5
CH_NAME = "Quadrilaterals"

# -----------------------------------------------------------------------------
# 5.1.1: Opposite sides and opposite angles theorem
# -----------------------------------------------------------------------------
def gen_5_1_1():
    tc = "MH-9-MTH2-5-5.1.1"
    tname = "Opposite sides and opposite angles theorem"
    qs = []

    # Arch 0: Opposite sides equal: AB = CD => a*x + b = (a-1)*x + c => x = c - b
    data_0 = [
        (3, 4, 2, 9, 5, 19), (4, 1, 3, 7, 6, 25), (5, -3, 4, 4, 7, 32),
        (2, 8, 1, 16, 8, 24), (6, -5, 5, 4, 9, 49), (3, 12, 2, 22, 10, 42),
        (4, -6, 3, 5, 11, 38), (5, 2, 4, 14, 12, 62), (2, 15, 1, 28, 13, 41),
        (3, -1, 2, 13, 14, 45)
    ]
    tmpls_0 = [
        "In parallelogram \(ABCD\), opposite sides have lengths \(AB = ({a}x {b_sign} {abs_b})\text{{ cm}}\) and \(CD = ({c}x + {d})\text{{ cm}}\). Find the length of \(AB\).",
        "Given parallelogram \(ABCD\) with opposite sides \(AB = {a}x {b_sign} {abs_b}\) and \(CD = {c}x + {d}\), calculate the measure of side \(AB\).",
        "Opposite sides of parallelogram \(ABCD\) are \(AB = {a}x {b_sign} {abs_b}\) and \(CD = {c}x + {d}\). Determine the length \(AB\).",
        "In a parallelogram \(ABCD\), \(AB = ({a}x {b_sign} {abs_b})\text{{ cm}}\) and \(CD = ({c}x + {d})\text{{ cm}}\). Evaluate length \(AB\).",
        "For parallelogram \(ABCD\), opposite side lengths satisfy \(AB = {a}x {b_sign} {abs_b}\) and \(CD = {c}x + {d}\). What is \(AB\)?",
        "If \(ABCD\) is a parallelogram with \(AB = {a}x {b_sign} {abs_b}\) and \(CD = {c}x + {d}\), compute \(AB\).",
        "Find the length of side \(AB\) of parallelogram \(ABCD\) where \(AB = ({a}x {b_sign} {abs_b})\text{{ cm}}\) and \(CD = ({c}x + {d})\text{{ cm}}\).",
        "Calculate the measure of \(AB\) in parallelogram \(ABCD\) given \(AB = {a}x {b_sign} {abs_b}\) and \(CD = {c}x + {d}\).",
        "In quadrilateral \(ABCD\) (a parallelogram), \(AB = {a}x {b_sign} {abs_b}\) and \(CD = {c}x + {d}\). Find \(AB\).",
        "Determine \(AB\) in parallelogram \(ABCD\) with opposite sides \(AB = ({a}x {b_sign} {abs_b})\text{{ cm}}\) and \(CD = ({c}x + {d})\text{{ cm}}\)."
    ]

    # Arch 1: Adjacent angles supplementary: \angle A + \angle B = 180^\circ
    data_1 = [
        (50, 130), (55, 125), (65, 115), (70, 110), (75, 105),
        (80, 100), (85, 95), (60, 120), (45, 135), (40, 140)
    ]
    tmpls_1 = [
        "In parallelogram \(ABCD\), angle \(\angle A = {ang_a}^\circ\). What is the measure of adjacent angle \(\angle B\)?",
        "If one angle of parallelogram \(ABCD\) is \(\angle A = {ang_a}^\circ\), find the measure of consecutive angle \(\angle B\).",
        "Calculate \(\angle B\) in parallelogram \(ABCD\) given that \(\angle A = {ang_a}^\circ\).",
        "In a parallelogram \(ABCD\), adjacent angle to \(\angle A = {ang_a}^\circ\) is \(\angle B\). Determine \(\angle B\).",
        "For parallelogram \(ABCD\) where \(\angle A = {ang_a}^\circ\), evaluate the degree measure of \(\angle B\).",
        "Find adjacent interior angle \(\angle B\) of parallelogram \(ABCD\) when \(\angle A = {ang_a}^\circ\).",
        "What is the value of consecutive angle \(\angle B\) in parallelogram \(ABCD\) with \(\angle A = {ang_a}^\circ\)?",
        "Determine the angle \(\angle B\) adjacent to \(\angle A = {ang_a}^\circ\) in parallelogram \(ABCD\).",
        "In parallelogram \(ABCD\), the measure of \(\angle A\) is {ang_a}°. Compute the measure of \(\angle B\).",
        "Evaluate consecutive angle \(\angle B\) in parallelogram \(ABCD\) if \(\angle A = {ang_a}^\circ\)."
    ]

    # Arch 2: Adjacent angles algebraic: (a*x + b) + (c*x + d) = 180 => x
    data_2 = [
        (2, 10, 3, 20, 30), (1, 25, 2, 35, 40), (3, -10, 2, 40, 30), (4, 10, 1, 20, 30),
        (2, 14, 3, 16, 30), (1, 15, 2, 45, 40), (3, 5, 2, 25, 30), (4, 20, 1, 10, 30),
        (2, 22, 3, 8, 30), (1, 30, 2, 30, 40)
    ]
    # To ensure distinct answers x, let's vary x:
    # 5x = 180 - b - d
    data_2 = [
        (2, 10, 3, 20, 30), (2, 5, 3, 25, 30), # wait, let's ensure distinct answers:
        (1, 20, 1, 40, 60), (2, 10, 1, 20, 50), (1, 10, 3, 10, 40),
        (2, 20, 2, 40, 30), (3, 15, 2, 15, 30), # distinct:
    ]
    # Let's make data_2 explicitly distinct answers x = 15, 18, 20, 22, 24, 25, 26, 28, 32, 35:
    # 2x + a + 3x + b = 180 => 5x = 180 - (a+b) => a+b = 180 - 5x
    data_2 = [
        (2, 50, 3, 55, 15), (2, 40, 3, 50, 18), (2, 35, 3, 45, 20), (2, 30, 3, 40, 22), (2, 25, 3, 35, 24),
        (2, 20, 3, 35, 25), (2, 20, 3, 30, 26), (2, 15, 3, 25, 28), (2, 5, 3, 15, 32), (2, 2, 3, 3, 35)
    ]
    tmpls_2 = [
        "In parallelogram \(ABCD\), two adjacent angles are \(\angle A = ({a}x + {b})^\circ\) and \(\angle B = ({c}x + {d})^\circ\). Find the value of \(x\).",
        "Two consecutive angles of parallelogram \(ABCD\) measure \(({a}x + {b})^\circ\) and \(({c}x + {d})^\circ\). Calculate \(x\).",
        "Determine the value of variable \(x\) if adjacent angles of parallelogram \(ABCD\) are \(({a}x + {b})^\circ\) and \(({c}x + {d})^\circ\).",
        "In a parallelogram \(ABCD\), \(\angle A = ({a}x + {b})^\circ\) and \(\angle B = ({c}x + {d})^\circ\). Evaluate \(x\).",
        "Calculate \(x\) given that adjacent angles of parallelogram \(ABCD\) are represented as \(({a}x + {b})^\circ\) and \(({c}x + {d})^\circ\).",
        "Consecutive angles in parallelogram \(ABCD\) are given by \(({a}x + {b})^\circ\) and \(({c}x + {d})^\circ\). What is \(x\)?",
        "Find \(x\) for parallelogram \(ABCD\) where \(\angle A = ({a}x + {b})^\circ\) and \(\angle B = ({c}x + {d})^\circ\).",
        "Adjacent angles in parallelogram \(ABCD\) satisfy \(\angle A = ({a}x + {b})^\circ\) and \(\angle B = ({c}x + {d})^\circ\). Compute \(x\).",
        "Evaluate \(x\) in parallelogram \(ABCD\) with consecutive interior angles \(({a}x + {b})^\circ\) and \(({c}x + {d})^\circ\).",
        "If \(\angle A = ({a}x + {b})^\circ\) and \(\angle B = ({c}x + {d})^\circ\) are adjacent in parallelogram \(ABCD\), find \(x\)."
    ]

    # Arch 3: Opposite angles equal: \angle A = \angle C => 3x - a = 2x + b => x = a + b
    data_3 = [
        (3, 10, 2, 2, 12), (3, 12, 2, 2, 14), (3, 14, 2, 2, 16), (3, 15, 2, 2, 17), (3, 17, 2, 2, 19),
        (3, 19, 2, 2, 21), (3, 21, 2, 2, 23), (3, 25, 2, 2, 27), (3, 27, 2, 2, 29), (3, 29, 2, 2, 31)
    ]
    tmpls_3 = [
        "In parallelogram \(ABCD\), opposite angles are \(\angle A = ({a}x - {b})^\circ\) and \(\angle C = ({c}x + {d})^\circ\). Find \(x\).",
        "Opposite angles of parallelogram \(ABCD\) measure \(({a}x - {b})^\circ\) and \(({c}x + {d})^\circ\). Calculate the value of \(x\).",
        "Calculate \(x\) if \(\angle A = ({a}x - {b})^\circ\) and \(\angle C = ({c}x + {d})^\circ\) in parallelogram \(ABCD\).",
        "Determine \(x\) in parallelogram \(ABCD\) given opposite angles \(\angle A = ({a}x - {b})^\circ\) and \(\angle C = ({c}x + {d})^\circ\).",
        "For parallelogram \(ABCD\), opposite angles satisfy \({a}x - {b} = {c}x + {d}\). What is \(x\)?",
        "Find the value of \(x\) from opposite angles \(\angle A = ({a}x - {b})^\circ\) and \(\angle C = ({c}x + {d})^\circ\) of parallelogram \(ABCD\).",
        "Evaluate \(x\) given that opposite angles in parallelogram \(ABCD\) are \(({a}x - {b})^\circ\) and \(({c}x + {d})^\circ\).",
        "Compute \(x\) for parallelogram \(ABCD\) with opposite angles \(\angle A = ({a}x - {b})^\circ\) and \(\angle C = ({c}x + {d})^\circ\).",
        "If \(\angle A = ({a}x - {b})^\circ\) and \(\angle C = ({c}x + {d})^\circ\) are opposite in parallelogram \(ABCD\), find \(x\).",
        "In quadrilateral \(ABCD\) (parallelogram), opposite angles are \(({a}x - {b})^\circ\) and \(({c}x + {d})^\circ\). Find \(x\)."
    ]

    # Arch 4: Perimeter of parallelogram: P = 2*(a + b)
    data_4 = [
        (5, 7, 24), (6, 9, 30), (7, 11, 36), (8, 13, 42), (9, 15, 48),
        (10, 17, 54), (11, 19, 60), (12, 21, 66), (13, 23, 72), (14, 25, 78)
    ]
    tmpls_4 = [
        "Adjacent sides of parallelogram \(ABCD\) are {a}\text{{ cm}} and {b}\text{{ cm}}. What is its perimeter?",
        "Find the perimeter of parallelogram \(ABCD\) having adjacent sides measuring {a}\text{{ cm}} and {b}\text{{ cm}}.",
        "Calculate the perimeter of a parallelogram whose two adjacent side lengths are {a}\text{{ cm}} and {b}\text{{ cm}}.",
        "In parallelogram \(ABCD\), \(AB = {a}\text{{ cm}}\) and \(BC = {b}\text{{ cm}}\). Determine the total perimeter.",
        "Determine the perimeter of parallelogram \(ABCD\) with adjacent sides {a}\text{{ cm}} and {b}\text{{ cm}}.",
        "Compute the perimeter of parallelogram \(ABCD\) when adjacent sides are {a}\text{{ cm}} and {b}\text{{ cm}}.",
        "What is the total boundary perimeter of parallelogram \(ABCD\) having sides of lengths {a}\text{{ cm}} and {b}\text{{ cm}}?",
        "Evaluate the perimeter of parallelogram \(ABCD\) given \(AB = {a}\text{{ cm}}\) and \(BC = {b}\text{{ cm}}\).",
        "A parallelogram has side lengths {a}\text{{ cm}} and {b}\text{{ cm}}. Calculate its perimeter.",
        "For parallelogram \(ABCD\) with adjacent sides {a}\text{{ cm}} and {b}\text{{ cm}}, find perimeter \(P = 2(a + b)\)."
    ]

    # Arch 5: Given perimeter P and side a, find adjacent side b = P/2 - a
    data_5 = [
        (26, 6, 7), (28, 6, 8), (32, 7, 9), (34, 7, 10), (38, 8, 11),
        (40, 8, 12), (44, 9, 13), (46, 9, 14), (50, 10, 15), (52, 10, 16)
    ]
    tmpls_5 = [
        "The perimeter of parallelogram \(ABCD\) is {p}\text{{ cm}} and one side is {a}\text{{ cm}}. Find the length of its adjacent side.",
        "In parallelogram \(ABCD\), perimeter is {p}\text{{ cm}}. If \(AB = {a}\text{{ cm}}\), calculate adjacent side \(BC\).",
        "What is the length of adjacent side in parallelogram \(ABCD\) with perimeter {p}\text{{ cm}} and one side {a}\text{{ cm}}?",
        "Determine the adjacent side length of parallelogram \(ABCD\) whose perimeter measures {p}\text{{ cm}} and one side is {a}\text{{ cm}}.",
        "Calculate the adjacent side of parallelogram \(ABCD\) given perimeter = {p}\text{{ cm}} and side = {a}\text{{ cm}}.",
        "If a parallelogram has perimeter {p}\text{{ cm}} and one side of length {a}\text{{ cm}}, compute the length of its other side.",
        "Find the length of side \(BC\) in parallelogram \(ABCD\) having perimeter {p}\text{{ cm}} and \(AB = {a}\text{{ cm}}\).",
        "Evaluate the adjacent side of parallelogram \(ABCD\) when its perimeter is {p}\text{{ cm}} and one side measures {a}\text{{ cm}}.",
        "A parallelogram with perimeter {p}\text{{ cm}} has one side measuring {a}\text{{ cm}}. Determine the other side.",
        "In parallelogram \(ABCD\) with perimeter {p}\text{{ cm}} and side {a}\text{{ cm}}, find adjacent side \(b\)."
    ]

    # Arch 6: Consecutive angle ratio a:b => smaller angle
    data_6 = [
        (1, 2, 60), (1, 3, 45), (2, 3, 72), (4, 5, 80), (1, 5, 30),
        (3, 7, 54), (7, 11, 70), (1, 4, 36), (5, 7, 75), (5, 13, 50)
    ]
    tmpls_6 = [
        "Adjacent angles of parallelogram \(ABCD\) are in the ratio {r1}:{r2}. Find the measure of the smaller angle.",
        "Two consecutive angles of parallelogram \(ABCD\) are in the proportion {r1}:{r2}. Calculate the smaller angle.",
        "What is the measure of the smaller angle in parallelogram \(ABCD\) if its adjacent angles are in ratio {r1}:{r2}?",
        "Determine the smaller interior angle of parallelogram \(ABCD\) given that adjacent angles are in ratio {r1}:{r2}.",
        "Calculate the measure of the smaller consecutive angle of parallelogram \(ABCD\) having angle ratio {r1}:{r2}.",
        "In parallelogram \(ABCD\), ratio of two adjacent angles is {r1}:{r2}. Evaluate the smaller angle.",
        "Find the smaller angle in degrees for parallelogram \(ABCD\) with adjacent angles in ratio {r1}:{r2}.",
        "If adjacent angles of parallelogram \(ABCD\) are in ratio {r1}:{r2}, compute the smaller angle.",
        "Evaluate the measure of the smaller angle of parallelogram \(ABCD\) whose consecutive angles have ratio {r1}:{r2}.",
        "The adjacent angles of a parallelogram are in the ratio {r1}:{r2}. Find the smaller angle."
    ]

    # Arch 7: Angle bisector of adjacent angle: \angle PAB = \angle A / 2
    data_7 = [
        (64, 32), (68, 34), (72, 36), (76, 38), (82, 41),
        (86, 43), (92, 46), (96, 48), (104, 52), (112, 56)
    ]
    tmpls_7 = [
        "In parallelogram \(ABCD\), ray \(AP\) bisects \(\angle A\). If \(\angle A = {ang}^\circ\), find \(\angle PAB\).",
        "The bisector of angle \(\angle A = {ang}^\circ\) in parallelogram \(ABCD\) is drawn. What is the measure of \(\angle PAB\)?",
        "Calculate \(\angle PAB\) in parallelogram \(ABCD\) where ray \(AP\) is the angle bisector of \(\angle A = {ang}^\circ\).",
        "In a parallelogram \(ABCD\), \(\angle A = {ang}^\circ\) is bisected by segment \(AP\). Determine \(\angle PAB\).",
        "Determine the measure of \(\angle PAB\) if \(AP\) bisects angle \(\angle A = {ang}^\circ\) of parallelogram \(ABCD\).",
        "Find \(\angle PAB\) in parallelogram \(ABCD\) given that \(\angle A = {ang}^\circ\) and ray \(AP\) bisects \(\angle A\).",
        "What is the angle \(\angle PAB\) formed by the angle bisector of \(\angle A = {ang}^\circ\) in parallelogram \(ABCD\)?",
        "Evaluate \(\angle PAB\) for parallelogram \(ABCD\) with angle bisector \(AP\) of \(\angle A = {ang}^\circ\).",
        "Compute the measure of \(\angle PAB\) when \(\angle A = {ang}^\circ\) in parallelogram \(ABCD\) is bisected by \(AP\).",
        "If ray \(AP\) bisects \(\angle A = {ang}^\circ\) in parallelogram \(ABCD\), find \(\angle PAB\)."
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx // 10
        sub_idx = idx % 10
        qcode = f"{tc}-OSC-{seq}"
        has_fig = (sub_idx in [0, 1, 2, 3, 4, 5, 6]) # 70% figures

        if arch == 0:
            a, b, c, d, x_ans, ab_ans = data_0[sub_idx]
            b_sign = "+" if b >= 0 else "-"
            abs_b = abs(b)
            svg = svg_parallelogram("A", "B", "C", "D", f"AB = {ab_ans} cm") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(a=a, b=b, c=c, d=d, b_sign=b_sign, abs_b=abs_b)
            corr = f"{ab_ans} cm"
            dist = [f"{ab_ans + 4} cm", f"{ab_ans - 4 if ab_ans > 4 else ab_ans + 8} cm", f"{ab_ans + 10} cm"]
            sol = f"**Step 1: Equating opposite sides**\nIn a parallelogram, opposite sides are equal: \(AB = CD\).\n\({a}x {b_sign} {abs_b} = {c}x + {d} \implies {a-c}x = {d-b} \implies x = {x_ans}\).\n**Step 2: Calculating side AB**\n\(AB = {a}({x_ans}) {b_sign} {abs_b} = {ab_ans}\text{{ cm}}\).\n**Step 3: Conclusion**\n{ab_ans} cm."
        elif arch == 1:
            ang_a, ang_b = data_1[sub_idx]
            svg = svg_parallelogram("A", "B", "C", "D", f"\angle A = {ang_a}^\circ") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(ang_a=ang_a)
            corr = f"{ang_b}^\circ"
            dist = [f"{ang_b + 10}^\circ", f"{ang_b - 10}^\circ", f"{ang_a}^\circ"]
            sol = f"**Step 1: Formula**\nAdjacent angles of a parallelogram are supplementary: \(\angle A + \angle B = 180^\circ\).\n\(\angle B = 180^\circ - {ang_a}^\circ = {ang_b}^\circ\).\n**Step 2: Conclusion**\n{ang_b}°."
        elif arch == 2:
            a, b, c, d, x_ans = data_2[sub_idx]
            svg = svg_parallelogram("A", "B", "C", "D") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(a=a, b=b, c=c, d=d)
            corr = f"{x_ans}"
            dist = [f"{x_ans + 4}", f"{x_ans - 4 if x_ans > 4 else x_ans + 8}", f"{x_ans + 10}"]
            sol = f"**Step 1: Supplementary equation**\n\(\angle A + \angle B = 180^\circ \implies ({a}x + {b}) + ({c}x + {d}) = 180\).\n\({a+c}x + {b+d} = 180 \implies {a+c}x = {180 - b - d} \implies x = {x_ans}\).\n**Step 2: Conclusion**\n{x_ans}."
        elif arch == 3:
            a, b, c, d, x_ans = data_3[sub_idx]
            svg = svg_parallelogram("A", "B", "C", "D") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(a=a, b=b, c=c, d=d)
            corr = f"{x_ans}"
            dist = [f"{x_ans + 3}", f"{x_ans - 3 if x_ans > 3 else x_ans + 6}", f"{x_ans + 8}"]
            sol = f"**Step 1: Opposite angles are equal**\n\(\angle A = \angle C \implies {a}x - {b} = {c}x + {d}\).\n\({a-c}x = {b+d} \implies x = {x_ans}\).\n**Step 2: Conclusion**\n{x_ans}."
        elif arch == 4:
            a, b, p_ans = data_4[sub_idx]
            svg = svg_parallelogram("A", "B", "C", "D", f"a={a}, b={b}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(a=a, b=b)
            corr = f"{p_ans} cm"
            dist = [f"{p_ans + 6} cm", f"{p_ans - 6 if p_ans > 6 else p_ans + 12} cm", f"{a + b} cm"]
            sol = f"**Step 1: Formula**\nPerimeter of parallelogram \(P = 2(a + b) = 2({a} + {b}) = 2({a+b}) = {p_ans}\text{{ cm}}\).\n**Step 2: Conclusion**\n{p_ans} cm."
        elif arch == 5:
            p, a, b_ans = data_5[sub_idx]
            svg = svg_parallelogram("A", "B", "C", "D", f"P={p} cm") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(p=p, a=a)
            corr = f"{b_ans} cm"
            dist = [f"{b_ans + 2} cm", f"{b_ans - 2 if b_ans > 2 else b_ans + 4} cm", f"{b_ans + 5} cm"]
            sol = f"**Step 1: Formula**\n\(P = 2(a + b) \implies \frac{{P}}{{2}} = a + b \implies b = \frac{{{p}}}{{2}} - {a} = {p//2} - {a} = {b_ans}\text{{ cm}}\).\n**Step 2: Conclusion**\n{b_ans} cm."
        elif arch == 6:
            r1, r2, ang_ans = data_6[sub_idx]
            svg = svg_parallelogram("A", "B", "C", "D", f"{r1}:{r2}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(r1=r1, r2=r2)
            corr = f"{ang_ans}^\circ"
            dist = [f"{ang_ans + 15}^\circ", f"{ang_ans - 15 if ang_ans > 15 else ang_ans + 25}^\circ", f"{180 - ang_ans}^\circ"]
            sol = f"**Step 1: Ratio calculation**\nLet adjacent angles be \({r1}x\) and \({r2}x\).\n\({r1}x + {r2}x = 180^\circ \implies {r1+r2}x = 180^\circ \implies x = {180 // (r1+r2)}^\circ\).\nSmaller angle = \({r1} \times {180 // (r1+r2)}^\circ = {ang_ans}^\circ\).\n**Step 2: Conclusion**\n{ang_ans}°."
        elif arch == 7:
            ang, half_ang = data_7[sub_idx]
            svg = svg_parallelogram("A", "B", "C", "D") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_7[sub_idx].format(ang=ang)
            corr = f"{half_ang}^\circ"
            dist = [f"{half_ang + 5}^\circ", f"{half_ang - 5 if half_ang > 5 else half_ang + 10}^\circ", f"{ang}^\circ"]
            sol = f"**Step 1: Bisector formula**\n\(\angle PAB = \frac{{\angle A}}{{2}} = \frac{{{ang}^\circ}}{{2}} = {half_ang}^\circ\).\n**Step 2: Conclusion**\n{half_ang}°."

        diff = "easy" if arch in [1, 4, 7] else ("medium" if arch in [0, 5, 6] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, CH_NUM, CH_NAME, tc, tname, seq, has_fig, diff))

    return qs

print("gen_5_1_1 defined.")

# -----------------------------------------------------------------------------
# 5.1.2: Diagonals bisect each other theorem
# -----------------------------------------------------------------------------
def gen_5_1_2():
    tc = "MH-9-MTH2-5-5.1.2"
    tname = "Diagonals bisect each other theorem"
    qs = []

    # Arch 0: Semi-diagonal OA given, find full AC = 2 * OA
    data_0 = [
        (3.5, 7), (4.5, 9), (5.5, 11), (6.5, 13), (7.5, 15),
        (8.5, 17), (9.5, 19), (10.5, 21), (11.5, 23), (12.5, 25)
    ]
    tmpls_0 = [
        "In parallelogram \(ABCD\), diagonals intersect at \(O\). If \(OA = {oa}\text{{ cm}}\), find the length of diagonal \(AC\).",
        "Diagonals of parallelogram \(ABCD\) bisect each other at \(O\). Given \(OA = {oa}\text{{ cm}}\), calculate \(AC\).",
        "What is the length of diagonal \(AC\) in parallelogram \(ABCD\) if semi-diagonal \(OA = {oa}\text{{ cm}}\)?",
        "Determine the measure of diagonal \(AC\) in parallelogram \(ABCD\) knowing that \(O\) is the intersection of diagonals and \(OA = {oa}\text{{ cm}}\).",
        "Calculate diagonal \(AC = 2 \times OA\) in parallelogram \(ABCD\) where \(OA = {oa}\text{{ cm}}\).",
        "In a parallelogram \(ABCD\), diagonals meet at \(O\). If \(OA = {oa}\text{{ cm}}\), evaluate \(AC\).",
        "Find the full length of diagonal \(AC\) of parallelogram \(ABCD\) given \(OA = {oa}\text{{ cm}}\).",
        "Compute diagonal length \(AC\) for parallelogram \(ABCD\) with center \(O\) and \(OA = {oa}\text{{ cm}}\).",
        "Evaluate \(AC\) in parallelogram \(ABCD\) given that diagonals bisect at \(O\) and \(OA = {oa}\text{{ cm}}\).",
        "For parallelogram \(ABCD\) with diagonal midpoint \(O\), if \(OA = {oa}\text{{ cm}}\), what is \(AC\)?"
    ]

    # Arch 1: Full diagonal BD given, find semi-diagonal OB = BD / 2
    data_1 = [
        (16, 8), (20, 10), (24, 12), (28, 14), (32, 16),
        (36, 18), (40, 20), (44, 22), (48, 24), (52, 26)
    ]
    tmpls_1 = [
        "In parallelogram \(ABCD\), diagonals meet at \(O\). If diagonal \(BD = {bd}\text{{ cm}}\), find \(OB\).",
        "Diagonals of parallelogram \(ABCD\) intersect at \(O\). Given \(BD = {bd}\text{{ cm}}\), calculate semi-diagonal \(OB\).",
        "Calculate the measure of \(OB\) in parallelogram \(ABCD\) if diagonal \(BD = {bd}\text{{ cm}}\).",
        "What is the length of segment \(OB\) in parallelogram \(ABCD\) where diagonal \(BD\) measures {bd}\text{{ cm}}?",
        "Determine \(OB\) in parallelogram \(ABCD\) given that diagonal \(BD = {bd}\text{{ cm}}\).",
        "Compute length \(OB\) for parallelogram \(ABCD\) having diagonal \(BD = {bd}\text{{ cm}}\).",
        "Find \(OB = \frac{{BD}}{{2}}\) in parallelogram \(ABCD\) with diagonal \(BD = {bd}\text{{ cm}}\).",
        "In a parallelogram \(ABCD\), diagonals bisect at \(O\). If \(BD = {bd}\text{{ cm}}\), evaluate \(OB\).",
        "Evaluate semi-diagonal \(OB\) of parallelogram \(ABCD\) when \(BD = {bd}\text{{ cm}}\).",
        "Given parallelogram \(ABCD\) with diagonals meeting at \(O\), if \(BD = {bd}\text{{ cm}}\), find \(OB\)."
    ]

    # Arch 2: Algebraic bisection OA = OC => 2x + a = x + b => x = b - a
    data_2 = [
        (2, 3, 1, 6, 3), (2, 4, 1, 8, 4), (2, 5, 1, 10, 5), (2, 6, 1, 12, 6), (2, 7, 1, 14, 7),
        (2, 8, 1, 16, 8), (2, 9, 1, 18, 9), (2, 10, 1, 20, 10), (2, 11, 1, 22, 11), (2, 12, 1, 24, 12)
    ]
    tmpls_2 = [
        "In parallelogram \(ABCD\), diagonals bisect at \(O\). If \(OA = ({a}x + {b})\text{{ cm}}\) and \(OC = (x + {d})\text{{ cm}}\), find \(x\).",
        "Diagonals of parallelogram \(ABCD\) intersect at \(O\). Given \(OA = {a}x + {b}\) and \(OC = x + {d}\), calculate \(x\).",
        "Calculate \(x\) if \(OA = {a}x + {b}\) and \(OC = x + {d}\) in parallelogram \(ABCD\) with diagonal intersection \(O\).",
        "Determine the value of \(x\) from \(OA = ({a}x + {b})\text{{ cm}}\) and \(OC = (x + {d})\text{{ cm}}\) in parallelogram \(ABCD\).",
        "What is the value of \(x\) in parallelogram \(ABCD\) given \(OA = {a}x + {b}\) and \(OC = x + {d}\)?",
        "Find \(x\) for parallelogram \(ABCD\) where diagonals bisect at \(O\) with \(OA = {a}x + {b}\) and \(OC = x + {d}\).",
        "Evaluate \(x\) in parallelogram \(ABCD\) satisfying \(OA = ({a}x + {b})\text{{ cm}}\) and \(OC = (x + {d})\text{{ cm}}\).",
        "Compute \(x\) given that diagonals of parallelogram \(ABCD\) bisect each other and \(OA = {a}x + {b}, OC = x + {d}\).",
        "For parallelogram \(ABCD\) with diagonal midpoint \(O\), if \(OA = {a}x + {b}\) and \(OC = x + {d}\), find \(x\).",
        "If \(OA = {a}x + {b}\) and \(OC = x + {d}\) represent bisected diagonal segments of parallelogram \(ABCD\), find \(x\)."
    ]

    # Arch 3: Algebraic bisection OB = OD => 3y - c = 2y + d => y = c + d, find OD
    data_3 = [
        (3, 10, 2, 7, 17, 41), (3, 11, 2, 8, 19, 46), (3, 12, 2, 9, 21, 51), (3, 13, 2, 10, 23, 56), (3, 15, 2, 12, 27, 66),
        (3, 16, 2, 13, 29, 71), (3, 17, 2, 14, 31, 76), (3, 18, 2, 15, 33, 81), (3, 19, 2, 16, 35, 86), (3, 20, 2, 17, 37, 91)
    ]
    tmpls_3 = [
        "In parallelogram \(ABCD\), diagonals meet at \(O\). If \(OB = ({a}y - {c})\text{{ cm}}\) and \(OD = ({b}y + {d})\text{{ cm}}\), find \(OD\).",
        "Diagonals of parallelogram \(ABCD\) bisect at \(O\). Given \(OB = {a}y - {c}\) and \(OD = {b}y + {d}\), calculate length \(OD\).",
        "Calculate the measure of \(OD\) in parallelogram \(ABCD\) where \(OB = {a}y - {c}\) and \(OD = {b}y + {d}\).",
        "Determine length \(OD\) in parallelogram \(ABCD\) given that diagonals bisect each other and \(OB = {a}y - {c}, OD = {b}y + {d}\).",
        "What is \(OD\) in parallelogram \(ABCD\) with diagonal intersection \(O\) and \(OB = {a}y - {c}, OD = {b}y + {d}\)?",
        "Find the length of \(OD\) for parallelogram \(ABCD\) where \(OB = ({a}y - {c})\text{{ cm}}\) and \(OD = ({b}y + {d})\text{{ cm}}\).",
        "Evaluate segment \(OD\) in parallelogram \(ABCD\) given \(OB = {a}y - {c}\) and \(OD = {b}y + {d}\).",
        "Compute \(OD\) in parallelogram \(ABCD\) with center \(O\), given \(OB = ({a}y - {c})\text{{ cm}}\) and \(OD = ({b}y + {d})\text{{ cm}}\).",
        "For parallelogram \(ABCD\) with bisecting diagonals at \(O\), if \(OB = {a}y - {c}\) and \(OD = {b}y + {d}\), find \(OD\).",
        "If diagonals of parallelogram \(ABCD\) meet at \(O\) with \(OB = {a}y - {c}\) and \(OD = {b}y + {d}\), determine \(OD\)."
    ]

    # Arch 4: Perimeter of \triangle AOB = AB + OA + OB
    data_4 = [
        (6, 4, 5, 15), (7, 5, 6, 18), (8, 6, 7, 21), (9, 7, 8, 24), (10, 8, 9, 27),
        (11, 9, 10, 30), (12, 10, 11, 33), (13, 11, 12, 36), (14, 12, 13, 39), (15, 13, 14, 42)
    ]
    tmpls_4 = [
        "In parallelogram \(ABCD\), diagonals intersect at \(O\). If \(AB = {ab}\text{{ cm}}\), \(OA = {oa}\text{{ cm}}\), and \(OB = {ob}\text{{ cm}}\), find the perimeter of \(\triangle AOB\).",
        "Diagonals of parallelogram \(ABCD\) meet at \(O\). If \(AB = {ab}\text{{ cm}}\), \(OA = {oa}\text{{ cm}}\), \(OB = {ob}\text{{ cm}}\), calculate the perimeter of \(\triangle AOB\).",
        "Calculate the perimeter of \(\triangle AOB\) in parallelogram \(ABCD\) with \(AB = {ab}\text{{ cm}}, OA = {oa}\text{{ cm}}, OB = {ob}\text{{ cm}}\).",
        "What is the perimeter of \(\triangle AOB\) formed by side \(AB = {ab}\text{{ cm}}\) and semi-diagonals \(OA = {oa}\text{{ cm}}, OB = {ob}\text{{ cm}}\) of parallelogram \(ABCD\)?",
        "Determine the perimeter of \(\triangle AOB\) in parallelogram \(ABCD\) given \(AB = {ab}\text{{ cm}}, OA = {oa}\text{{ cm}}\), and \(OB = {ob}\text{{ cm}}\).",
        "Find the perimeter of \(\triangle AOB\) for parallelogram \(ABCD\) having \(AB = {ab}\text{{ cm}}, OA = {oa}\text{{ cm}}, OB = {ob}\text{{ cm}}\).",
        "Compute perimeter of \(\triangle AOB\) in parallelogram \(ABCD\) where diagonals meet at \(O\) and \(AB = {ab}, OA = {oa}, OB = {ob}\).",
        "Evaluate the perimeter of \(\triangle AOB\) given side \(AB = {ab}\text{{ cm}}\) and half-diagonals \(OA = {oa}\text{{ cm}}, OB = {ob}\text{{ cm}}\) in parallelogram \(ABCD\).",
        "In parallelogram \(ABCD\) with diagonal intersection \(O\), find the perimeter of \(\triangle AOB\) for \(AB = {ab}\text{{ cm}}, OA = {oa}\text{{ cm}}, OB = {ob}\text{{ cm}}\).",
        "For parallelogram \(ABCD\), if \(AB = {ab}\text{{ cm}}, OA = {oa}\text{{ cm}}, OB = {ob}\text{{ cm}}\), find the perimeter of \(\triangle AOB\)."
    ]

    # Arch 5: Sum OA + OB = (d1 + d2)/2
    data_5 = [
        (13, 16, 14.5), (15, 18, 16.5), (17, 20, 18.5), (19, 22, 20.5), (21, 24, 22.5),
        (23, 26, 24.5), (25, 28, 26.5), (27, 30, 28.5), (29, 32, 30.5), (31, 34, 32.5)
    ]
    tmpls_5 = [
        "In parallelogram \(ABCD\), diagonals are \(AC = {d1}\text{{ cm}}\) and \(BD = {d2}\text{{ cm}}\). Find \(OA + OB\).",
        "Diagonals of parallelogram \(ABCD\) measure \(AC = {d1}\text{{ cm}}\) and \(BD = {d2}\text{{ cm}}\) intersecting at \(O\). Calculate \(OA + OB\).",
        "Calculate the sum \(OA + OB\) in parallelogram \(ABCD\) with diagonals \(AC = {d1}\text{{ cm}}\) and \(BD = {d2}\text{{ cm}}\).",
        "What is the sum of semi-diagonals \(OA + OB\) in parallelogram \(ABCD\) having diagonals \(AC = {d1}\text{{ cm}}\) and \(BD = {d2}\text{{ cm}}\)?",
        "Determine \(OA + OB\) in parallelogram \(ABCD\) given diagonals \(AC = {d1}\text{{ cm}}\) and \(BD = {d2}\text{{ cm}}\).",
        "Compute \(OA + OB\) for parallelogram \(ABCD\) whose diagonals are {d1}\text{{ cm}} and {d2}\text{{ cm}}.",
        "Find the value of \(OA + OB\) in parallelogram \(ABCD\) with diagonal lengths \(AC = {d1}\text{{ cm}}\) and \(BD = {d2}\text{{ cm}}\).",
        "Evaluate \(OA + OB\) in parallelogram \(ABCD\) where diagonals intersect at \(O\) with \(AC = {d1}\text{{ cm}}, BD = {d2}\text{{ cm}}\).",
        "If diagonals of parallelogram \(ABCD\) are \(AC = {d1}\text{{ cm}}\) and \(BD = {d2}\text{{ cm}}\), find \(OA + OB\).",
        "For parallelogram \(ABCD\) with diagonals meeting at \(O\), calculate \(OA + OB\) given \(AC = {d1}\text{{ cm}}\) and \(BD = {d2}\text{{ cm}}\)."
    ]

    # Arch 6: Perimeter of \triangle AOD = P1 and AD = s => OA + OD = P1 - s
    data_6 = [
        (21, 8, 13), (23, 8, 15), (26, 9, 17), (30, 10, 20), (33, 11, 22),
        (37, 12, 25), (41, 13, 28), (45, 14, 31), (49, 15, 34), (54, 16, 38)
    ]
    tmpls_6 = [
        "In parallelogram \(ABCD\), diagonals meet at \(O\). If the perimeter of \(\triangle AOD\) is {p}\text{{ cm}} and \(AD = {s}\text{{ cm}}\), find \(OA + OD\).",
        "Perimeter of \(\triangle AOD\) in parallelogram \(ABCD\) is {p}\text{{ cm}}. Given side \(AD = {s}\text{{ cm}}\), calculate \(OA + OD\).",
        "Calculate \(OA + OD\) in parallelogram \(ABCD\) where diagonals intersect at \(O\), \(\triangle AOD\) has perimeter {p}\text{{ cm}}, and \(AD = {s}\text{{ cm}}\).",
        "What is the sum \(OA + OD\) if the perimeter of \(\triangle AOD\) is {p}\text{{ cm}} and \(AD = {s}\text{{ cm}}\) in parallelogram \(ABCD\)?",
        "Determine \(OA + OD\) in parallelogram \(ABCD\) knowing that \(\triangle AOD\) has perimeter {p}\text{{ cm}} and side \(AD = {s}\text{{ cm}}\).",
        "Find \(OA + OD\) for parallelogram \(ABCD\) having \(\triangle AOD\) perimeter = {p}\text{{ cm}} and \(AD = {s}\text{{ cm}}\).",
        "Compute \(OA + OD\) in parallelogram \(ABCD\) given perimeter of \(\triangle AOD\) is {p}\text{{ cm}} and \(AD = {s}\text{{ cm}}\).",
        "Evaluate \(OA + OD\) when \(\triangle AOD\) in parallelogram \(ABCD\) has perimeter {p}\text{{ cm}} and side \(AD = {s}\text{{ cm}}\).",
        "In parallelogram \(ABCD\) with diagonal intersection \(O\), if \(\text{{Perimeter}}(\triangle AOD) = {p}\text{{ cm}}\) and \(AD = {s}\text{{ cm}}\), find \(OA + OD\).",
        "If perimeter of \(\triangle AOD\) is {p}\text{{ cm}} and \(AD = {s}\text{{ cm}}\) in parallelogram \(ABCD\), find \(OA + OD\)."
    ]

    # Arch 7: Angle in \triangle AOB: \angle AOB = 180 - (alpha + beta)
    data_7 = [
        (45, 70, 65), (40, 65, 75), (35, 60, 85), (30, 55, 95), (25, 50, 105),
        (20, 45, 115), (15, 40, 125), (40, 70, 70), (35, 65, 80), (25, 45, 110)
    ]
    tmpls_7 = [
        "In parallelogram \(ABCD\), diagonals intersect at \(O\). If \(\angle OAB = {a}^\circ\) and \(\angle OBA = {b}^\circ\), find \(\angle AOB\).",
        "Diagonals of parallelogram \(ABCD\) meet at \(O\). Given \(\angle OAB = {a}^\circ\) and \(\angle OBA = {b}^\circ\), calculate \(\angle AOB\).",
        "Calculate the angle between diagonals \(\angle AOB\) in parallelogram \(ABCD\) if \(\angle OAB = {a}^\circ\) and \(\angle OBA = {b}^\circ\).",
        "What is the measure of \(\angle AOB\) in parallelogram \(ABCD\) where \(\angle OAB = {a}^\circ\) and \(\angle OBA = {b}^\circ\)?",
        "Determine \(\angle AOB\) in parallelogram \(ABCD\) given that \(\angle OAB = {a}^\circ\) and \(\angle OBA = {b}^\circ\).",
        "Find \(\angle AOB\) in parallelogram \(ABCD\) with diagonal intersection \(O\) knowing \(\angle OAB = {a}^\circ\) and \(\angle OBA = {b}^\circ\).",
        "Compute \(\angle AOB\) for parallelogram \(ABCD\) when \(\angle OAB = {a}^\circ\) and \(\angle OBA = {b}^\circ\).",
        "Evaluate \(\angle AOB\) in parallelogram \(ABCD\) having \(\angle OAB = {a}^\circ\) and \(\angle OBA = {b}^\circ\).",
        "In parallelogram \(ABCD\) with diagonals meeting at \(O\), if \(\angle OAB = {a}^\circ\) and \(\angle OBA = {b}^\circ\), find \(\angle AOB\).",
        "For parallelogram \(ABCD\), given \(\angle OAB = {a}^\circ\) and \(\angle OBA = {b}^\circ\), find \(\angle AOB\)."
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx // 10
        sub_idx = idx % 10
        qcode = f"{tc}-OSC-{seq}"
        has_fig = (sub_idx in [0, 1, 2, 3, 4, 5, 6]) # 70% figures

        if arch == 0:
            oa, ac = data_0[sub_idx]
            svg = svg_parallelogram_diagonals(f"OA = {oa} cm") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(oa=oa)
            corr = f"{ac} cm"
            dist = [f"{ac + 2} cm", f"{ac - 2 if ac > 2 else ac + 4} cm", f"{oa} cm"]
            sol = f"**Step 1: Formula**\nDiagonals of a parallelogram bisect each other: \(AC = 2 \times OA\).\n\(AC = 2 \times {oa} = {ac}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ac} cm."
        elif arch == 1:
            bd, ob = data_1[sub_idx]
            svg = svg_parallelogram_diagonals(f"BD = {bd} cm") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(bd=bd)
            corr = f"{ob} cm"
            dist = [f"{ob + 3} cm", f"{ob - 3 if ob > 3 else ob + 6} cm", f"{bd} cm"]
            sol = f"**Step 1: Formula**\nDiagonals of a parallelogram bisect each other: \(OB = \frac{{BD}}{{2}}\).\n\(OB = \frac{{{bd}}}{{2}} = {ob}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ob} cm."
        elif arch == 2:
            a, b, c, d, x_ans = data_2[sub_idx]
            svg = svg_parallelogram_diagonals() if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(a=a, b=b, d=d)
            corr = f"{x_ans}"
            dist = [f"{x_ans + 2}", f"{x_ans - 2 if x_ans > 2 else x_ans + 4}", f"{x_ans + 5}"]
            sol = f"**Step 1: Diagonals bisect each other**\n\(OA = OC \implies {a}x + {b} = x + {d}\).\n\({a-1}x = {d-b} \implies x = {x_ans}\).\n**Step 2: Conclusion**\n{x_ans}."
        elif arch == 3:
            a, c, b, d, y_ans, od_ans = data_3[sub_idx]
            svg = svg_parallelogram_diagonals() if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(a=a, c=c, b=b, d=d)
            corr = f"{od_ans} cm"
            dist = [f"{od_ans + 5} cm", f"{od_ans - 5 if od_ans > 5 else od_ans + 10} cm", f"{y_ans} cm"]
            sol = f"**Step 1: Equating semi-diagonals**\n\(OB = OD \implies {a}y - {c} = {b}y + {d}\).\n\({a-b}y = {c+d} \implies y = {y_ans}\).\n**Step 2: Calculating OD**\n\(OD = {b}({y_ans}) + {d} = {od_ans}\text{{ cm}}\).\n**Step 3: Conclusion**\n{od_ans} cm."
        elif arch == 4:
            ab, oa, ob, p = data_4[sub_idx]
            svg = svg_parallelogram_diagonals() if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(ab=ab, oa=oa, ob=ob)
            corr = f"{p} cm"
            dist = [f"{p + 4} cm", f"{p - 4 if p > 4 else p + 8} cm", f"{ab + oa} cm"]
            sol = f"**Step 1: Formula**\nPerimeter of \(\triangle AOB = AB + OA + OB = {ab} + {oa} + {ob} = {p}\text{{ cm}}\).\n**Step 2: Conclusion**\n{p} cm."
        elif arch == 5:
            d1, d2, sum_ans = data_5[sub_idx]
            svg = svg_parallelogram_diagonals(f"AC={d1}, BD={d2}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(d1=d1, d2=d2)
            corr = f"{sum_ans} cm"
            dist = [f"{sum_ans + 2} cm", f"{sum_ans - 2 if sum_ans > 2 else sum_ans + 4} cm", f"{d1 + d2} cm"]
            sol = f"**Step 1: Formula**\n\(OA = \frac{{AC}}{{2}} = \frac{{{d1}}}{{2}} = {d1/2}\text{{ cm}}\).\n\(OB = \frac{{BD}}{{2}} = \frac{{{d2}}}{{2}} = {d2/2}\text{{ cm}}\).\n\(OA + OB = {d1/2} + {d2/2} = {sum_ans}\text{{ cm}}\).\n**Step 2: Conclusion**\n{sum_ans} cm."
        elif arch == 6:
            p, s, sum_ans = data_6[sub_idx]
            svg = svg_parallelogram_diagonals(f"P={p} cm") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(p=p, s=s)
            corr = f"{sum_ans} cm"
            dist = [f"{sum_ans + 3} cm", f"{sum_ans - 3 if sum_ans > 3 else sum_ans + 6} cm", f"{p} cm"]
            sol = f"**Step 1: Perimeter formula**\n\(\text{{Perimeter}}(\triangle AOD) = OA + OD + AD\).\n\(OA + OD = \text{{Perimeter}} - AD = {p} - {s} = {sum_ans}\text{{ cm}}\).\n**Step 2: Conclusion**\n{sum_ans} cm."
        elif arch == 7:
            a, b, aob = data_7[sub_idx]
            svg = svg_parallelogram_diagonals() if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_7[sub_idx].format(a=a, b=b)
            corr = f"{aob}^\circ"
            dist = [f"{aob + 10}^\circ", f"{aob - 10}^\circ", f"{180 - aob}^\circ"]
            sol = f"**Step 1: Angle sum in \(\triangle AOB\)**\n\(\angle AOB = 180^\circ - (\angle OAB + \angle OBA) = 180^\circ - ({a}^\circ + {b}^\circ) = 180^\circ - {a+b}^\circ = {aob}^\circ\).\n**Step 2: Conclusion**\n{aob}°."

        diff = "easy" if arch in [0, 1, 4] else ("medium" if arch in [2, 5, 7] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, CH_NUM, CH_NAME, tc, tname, seq, has_fig, diff))

    return qs

print("gen_5_1_2 defined.")

# -----------------------------------------------------------------------------
# 5.1.3: Tests to prove a quadrilateral is a parallelogram
# -----------------------------------------------------------------------------
def gen_5_1_3():
    tc = "MH-9-MTH2-5-5.1.3"
    tname = "Tests to prove a quadrilateral is a parallelogram"
    qs = []

    # Arch 0: Opposite angles test: x + a = 2x - b => x = a + b
    data_0 = [
        (1, 20, 2, 5, 25), (1, 25, 2, 10, 35), (1, 30, 2, 10, 40), (1, 35, 2, 10, 45), (1, 40, 2, 10, 50),
        (1, 45, 2, 10, 55), (1, 50, 2, 10, 60), (1, 55, 2, 10, 65), (1, 60, 2, 10, 70), (1, 65, 2, 10, 75)
    ]
    tmpls_0 = [
        "In quadrilateral \(ABCD\), opposite angles are \(\angle A = (x + {a})^\circ\) and \(\angle C = (2x - {b})^\circ\). Find \(x\) such that \(ABCD\) is a parallelogram.",
        "For quadrilateral \(ABCD\) to be a parallelogram by opposite angles test, if \(\angle A = (x + {a})^\circ\) and \(\angle C = (2x - {b})^\circ\), calculate \(x\).",
        "Calculate \(x\) for quadrilateral \(ABCD\) to be a parallelogram, given \(\angle A = (x + {a})^\circ\) and \(\angle C = (2x - {b})^\circ\).",
        "Determine the value of \(x\) so that opposite angles \(\angle A = (x + {a})^\circ\) and \(\angle C = (2x - {b})^\circ\) make \(ABCD\) a parallelogram.",
        "What value of \(x\) ensures that opposite angles \(\angle A = (x + {a})^\circ\) and \(\angle C = (2x - {b})^\circ\) satisfy the parallelogram test?",
        "Find \(x\) in quadrilateral \(ABCD\) where opposite angles measure \((x + {a})^\circ\) and \((2x - {b})^\circ\) for it to be a parallelogram.",
        "Evaluate \(x\) such that quadrilateral \(ABCD\) with \(\angle A = (x + {a})^\circ\) and \(\angle C = (2x - {b})^\circ\) is a parallelogram.",
        "Compute \(x\) for which quadrilateral \(ABCD\) has congruent opposite angles \(\angle A = (x + {a})^\circ\) and \(\angle C = (2x - {b})^\circ\).",
        "If quadrilateral \(ABCD\) is a parallelogram with \(\angle A = (x + {a})^\circ\) and \(\angle C = (2x - {b})^\circ\), find \(x\).",
        "In quadrilateral \(ABCD\), opposite angles are \((x + {a})^\circ\) and \((2x - {b})^\circ\). Determine \(x\) for parallelogram test."
    ]

    # Arch 1: Opposite sides test: 3x - a = 2x + b => x = a + b
    data_1 = [
        (3, 5, 2, 3, 8), (3, 6, 2, 3, 9), (3, 7, 2, 3, 10), (3, 8, 2, 3, 11), (3, 9, 2, 3, 12),
        (3, 10, 2, 3, 13), (3, 11, 2, 3, 14), (3, 12, 2, 3, 15), (3, 13, 2, 3, 16), (3, 14, 2, 3, 17)
    ]
    tmpls_1 = [
        "In quadrilateral \(ABCD\), opposite sides are \(AB = ({a}x - {b})\text{{ cm}}\) and \(CD = ({c}x + {d})\text{{ cm}}\). Find \(x\) for \(ABCD\) to be a parallelogram.",
        "Opposite sides test: For quadrilateral \(ABCD\) to be a parallelogram, \(AB = {a}x - {b}\) and \(CD = {c}x + {d}\). Calculate \(x\).",
        "Calculate \(x\) such that \(AB = ({a}x - {b})\text{{ cm}}\) and \(CD = ({c}x + {d})\text{{ cm}}\) are congruent opposite sides of parallelogram \(ABCD\).",
        "What value of \(x\) makes opposite sides \(AB = {a}x - {b}\) and \(CD = {c}x + {d}\) equal in quadrilateral \(ABCD\)?",
        "Determine \(x\) so that quadrilateral \(ABCD\) with \(AB = {a}x - {b}\) and \(CD = {c}x + {d}\) satisfies the parallelogram condition.",
        "Find \(x\) for which quadrilateral \(ABCD\) with sides \(AB = ({a}x - {b})\text{{ cm}}\) and \(CD = ({c}x + {d})\text{{ cm}}\) is a parallelogram.",
        "Evaluate \(x\) in quadrilateral \(ABCD\) where \(AB = {a}x - {b}\) and \(CD = {c}x + {d}\) are opposite sides.",
        "Compute \(x\) such that opposite sides \(AB = {a}x - {b}\) and \(CD = {c}x + {d}\) prove quadrilateral \(ABCD\) is a parallelogram.",
        "In quadrilateral \(ABCD\), if \(AB = {a}x - {b}\) and \(CD = {c}x + {d}\) are equal, find \(x\).",
        "Determine the value of \(x\) for which opposite sides \(AB = {a}x - {b}\) and \(CD = {c}x + {d}\) are equal."
    ]

    # Arch 2: One pair of opposite sides parallel and equal: AB || CD and AB = 4y - a, CD = 3y + b => y = a + b
    data_2 = [
        (4, 3, 3, 2, 5), (4, 4, 3, 2, 6), (4, 5, 3, 2, 7), (4, 6, 3, 2, 8), (4, 7, 3, 2, 9),
        (4, 8, 3, 2, 10), (4, 9, 3, 2, 11), (4, 10, 3, 2, 12), (4, 11, 3, 2, 13), (4, 12, 3, 2, 14)
    ]
    tmpls_2 = [
        "In quadrilateral \(ABCD\), \(AB \parallel CD\). If \(AB = ({a}y - {b})\text{{ cm}}\) and \(CD = ({c}y + {d})\text{{ cm}}\), find \(y\) for \(ABCD\) to be a parallelogram.",
        "Given \(AB \parallel CD\) in quadrilateral \(ABCD\), find \(y\) such that \(AB = {a}y - {b}\) equals \(CD = {c}y + {d}\).",
        "A quadrilateral \(ABCD\) has \(AB \parallel CD\). What value of \(y\) makes \(AB = ({a}y - {b})\text{{ cm}}\) equal to \(CD = ({c}y + {d})\text{{ cm}}\)?",
        "Calculate \(y\) in quadrilateral \(ABCD\) with \(AB \parallel CD\) where \(AB = {a}y - {b}\) and \(CD = {c}y + {d}\).",
        "Determine \(y\) so that one pair of opposite sides \(AB \parallel CD\) with \(AB = {a}y - {b}\) and \(CD = {c}y + {d}\) proves \(ABCD\) is a parallelogram.",
        "Find \(y\) for quadrilateral \(ABCD\) where \(AB \parallel CD\) and \(AB = ({a}y - {b})\text{{ cm}}, CD = ({c}y + {d})\text{{ cm}}\).",
        "Compute \(y\) such that \(AB = CD\) when \(AB = {a}y - {b}, CD = {c}y + {d}\), and \(AB \parallel CD\).",
        "Evaluate \(y\) in quadrilateral \(ABCD\) given \(AB \parallel CD\), \(AB = {a}y - {b}\), and \(CD = {c}y + {d}\).",
        "If \(AB \parallel CD\) in quadrilateral \(ABCD\) with \(AB = {a}y - {b}\) and \(CD = {c}y + {d}\), find \(y\).",
        "For quadrilateral \(ABCD\), \(AB \parallel CD\). Find \(y\) given \(AB = ({a}y - {b})\text{{ cm}}\) and \(CD = ({c}y + {d})\text{{ cm}}\)."
    ]

    # Arch 3: Diagonals bisect test: OA = 2z + a, OC = z + b => z = b - a
    data_3 = [
        (2, 3, 1, 7, 4), (2, 3, 1, 9, 6), (2, 3, 1, 11, 8), (2, 3, 1, 13, 10), (2, 3, 1, 15, 12),
        (2, 3, 1, 17, 14), (2, 3, 1, 19, 16), (2, 3, 1, 21, 18), (2, 3, 1, 23, 20), (2, 3, 1, 25, 22)
    ]
    tmpls_3 = [
        "Diagonals of quadrilateral \(ABCD\) meet at \(O\). If \(OA = ({a}z + {b})\text{{ cm}}\) and \(OC = (z + {d})\text{{ cm}}\), find \(z\) for diagonals to bisect.",
        "In quadrilateral \(ABCD\), diagonals meet at \(O\). Find \(z\) so that \(OA = {a}z + {b}\) equals \(OC = z + {d}\).",
        "Calculate \(z\) such that \(OA = ({a}z + {b})\text{{ cm}}\) and \(OC = (z + {d})\text{{ cm}}\) are equal in quadrilateral \(ABCD\).",
        "What value of \(z\) ensures \(OA = {a}z + {b}\) and \(OC = z + {d}\) bisect diagonal \(AC\) at \(O\)?",
        "Determine \(z\) in quadrilateral \(ABCD\) with diagonal intersection \(O\) where \(OA = {a}z + {b}\) and \(OC = z + {d}\).",
        "Find \(z\) for which \(OA = ({a}z + {b})\text{{ cm}}\) equals \(OC = (z + {d})\text{{ cm}}\) in quadrilateral \(ABCD\).",
        "Evaluate \(z\) such that diagonal \(AC\) is bisected at \(O\) with \(OA = {a}z + {b}\) and \(OC = z + {d}\).",
        "Compute \(z\) given \(OA = {a}z + {b}\) and \(OC = z + {d}\) for parallelogram diagonal test in \(ABCD\).",
        "If diagonals of quadrilateral \(ABCD\) bisect at \(O\) with \(OA = {a}z + {b}\) and \(OC = z + {d}\), find \(z\).",
        "In quadrilateral \(ABCD\), \(O\) is the midpoint of \(AC\). Find \(z\) if \(OA = {a}z + {b}\) and \(OC = z + {d}\)."
    ]

    # Arch 4: Varignon parallelogram perimeter: P = d1 + d2
    data_4 = [
        (8, 10, 18), (10, 12, 22), (12, 14, 26), (14, 16, 30), (16, 18, 34),
        (18, 20, 38), (20, 22, 42), (22, 24, 46), (24, 26, 50), (26, 28, 54)
    ]
    tmpls_4 = [
        "In quadrilateral \(ABCD\), diagonals are \(AC = {d1}\text{{ cm}}\) and \(BD = {d2}\text{{ cm}}\). Find the perimeter of the parallelogram formed by joining the midpoints of its sides.",
        "The midpoints of sides of quadrilateral \(ABCD\) form a parallelogram. If diagonals \(AC = {d1}\text{{ cm}}\) and \(BD = {d2}\text{{ cm}}\), calculate its perimeter.",
        "Calculate the perimeter of Varignon's parallelogram in quadrilateral \(ABCD\) with diagonals \(AC = {d1}\text{{ cm}}\) and \(BD = {d2}\text{{ cm}}\).",
        "What is the perimeter of the parallelogram obtained by joining midpoints of sides of quadrilateral \(ABCD\) having diagonals {d1}\text{{ cm}} and {d2}\text{{ cm}}?",
        "Determine the perimeter of the midpoint parallelogram of quadrilateral \(ABCD\) given \(AC = {d1}\text{{ cm}}\) and \(BD = {d2}\text{{ cm}}\).",
        "Find the perimeter of the quadrilateral formed by midpoints of sides of \(ABCD\) where diagonals measure {d1}\text{{ cm}} and {d2}\text{{ cm}}.",
        "Compute the perimeter of the parallelogram connecting midpoints of sides of quadrilateral \(ABCD\) with diagonals {d1}\text{{ cm}} and {d2}\text{{ cm}}.",
        "Evaluate the perimeter of the medial parallelogram of quadrilateral \(ABCD\) having diagonals \(AC = {d1}\text{{ cm}}\) and \(BD = {d2}\text{{ cm}}\).",
        "If diagonals of quadrilateral \(ABCD\) are {d1}\text{{ cm}} and {d2}\text{{ cm}}, find the perimeter of the parallelogram formed by joining its midpoints.",
        "For quadrilateral \(ABCD\) with diagonals \(AC = {d1}\text{{ cm}}\) and \(BD = {d2}\text{{ cm}}\), find the perimeter of the midpoint parallelogram."
    ]

    # Arch 5: Angle required for parallelogram: \angle C must equal \angle A
    data_5 = [
        (48, 48), (52, 52), (56, 56), (64, 64), (72, 72),
        (78, 78), (84, 84), (96, 96), (108, 108), (114, 114)
    ]
    tmpls_5 = [
        "In quadrilateral \(ABCD\), \(\angle A = {ang}^\circ\) and \(\angle B = {supp}^\circ\). For \(ABCD\) to be a parallelogram, what must be the measure of \(\angle C\)?",
        "Given \(\angle A = {ang}^\circ\) in quadrilateral \(ABCD\) where adjacent \(\angle B = {supp}^\circ\), what measure of \(\angle C\) makes \(ABCD\) a parallelogram?",
        "What value must opposite angle \(\angle C\) have so that quadrilateral \(ABCD\) with \(\angle A = {ang}^\circ\) is a parallelogram?",
        "Determine the measure of \(\angle C\) required for quadrilateral \(ABCD\) to be a parallelogram given \(\angle A = {ang}^\circ\).",
        "Calculate the degree measure of \(\angle C\) in quadrilateral \(ABCD\) if \(\angle A = {ang}^\circ\) and opposite angles must be equal.",
        "For quadrilateral \(ABCD\) to satisfy the opposite angles test with \(\angle A = {ang}^\circ\), find \(\angle C\).",
        "Find the required measure of angle \(\angle C\) so that quadrilateral \(ABCD\) with \(\angle A = {ang}^\circ\) is a parallelogram.",
        "Compute \(\angle C\) in quadrilateral \(ABCD\) where \(\angle A = {ang}^\circ\) and consecutive angle is {supp}°.",
        "If quadrilateral \(ABCD\) is to be a parallelogram and \(\angle A = {ang}^\circ\), what must \(\angle C\) measure?",
        "Evaluate the necessary measure of \(\angle C\) in quadrilateral \(ABCD\) with \(\angle A = {ang}^\circ\) for it to be a parallelogram."
    ]

    # Arch 6: Fourth angle of quadrilateral: d = 360 - (a + b + c)
    data_6 = [
        (85, 110, 120, 45), (75, 105, 125, 55), (80, 100, 115, 65), (70, 95, 120, 75), (65, 90, 120, 85),
        (60, 85, 120, 95), (55, 80, 120, 105), (50, 75, 120, 115), (45, 70, 120, 125), (40, 65, 120, 135)
    ]
    tmpls_6 = [
        "Three angles of quadrilateral \(ABCD\) are {a}^\circ, {b}^\circ, and {c}^\circ. Find the fourth angle \(\angle D\).",
        "In quadrilateral \(ABCD\), \(\angle A = {a}^\circ\), \(\angle B = {b}^\circ\), and \(\angle C = {c}^\circ\). Calculate \(\angle D\).",
        "Calculate the fourth angle of quadrilateral \(ABCD\) if three angles measure {a}^\circ, {b}^\circ, and {c}^\circ.",
        "What is the measure of the fourth angle in quadrilateral \(ABCD\) with angles {a}^\circ, {b}^\circ, and {c}^\circ?",
        "Determine \(\angle D\) in quadrilateral \(ABCD\) given \(\angle A = {a}^\circ\), \(\angle B = {b}^\circ\), and \(\angle C = {c}^\circ\).",
        "Find \(\angle D\) for quadrilateral \(ABCD\) having three interior angles {a}^\circ, {b}^\circ, and {c}^\circ.",
        "Compute the fourth interior angle of quadrilateral \(ABCD\) with angles {a}^\circ, {b}^\circ, and {c}^\circ.",
        "Evaluate \(\angle D\) in quadrilateral \(ABCD\) where three angles are {a}^\circ, {b}^\circ, and {c}^\circ.",
        "If three angles of quadrilateral \(ABCD\) measure {a}^\circ, {b}^\circ, and {c}^\circ, find \(\angle D\).",
        "For quadrilateral \(ABCD\), given \(\angle A = {a}^\circ, \angle B = {b}^\circ, \angle C = {c}^\circ\), find \(\angle D\)."
    ]

    # Arch 7: Angle required for consecutive interior angle test: \angle B = 180 - \angle A
    data_7 = [
        (54, 126), (58, 122), (62, 118), (66, 114), (74, 106),
        (78, 102), (82, 98), (86, 94), (94, 86), (102, 78)
    ]
    tmpls_7 = [
        "In quadrilateral \(ABCD\), \(\angle A = {ang}^\circ\). For line \(AD \parallel BC\), what must be the measure of consecutive angle \(\angle B\)?",
        "For lines \(AD\) and \(BC\) of quadrilateral \(ABCD\) to be parallel, if \(\angle A = {ang}^\circ\), calculate \(\angle B\).",
        "What measure of \(\angle B\) makes interior angles on the same side supplementary with \(\angle A = {ang}^\circ\) in quadrilateral \(ABCD\)?",
        "Determine consecutive interior angle \(\angle B\) so that \(AD \parallel BC\) given \(\angle A = {ang}^\circ\) in quadrilateral \(ABCD\).",
        "Calculate the angle \(\angle B\) required to make \(AD \parallel BC\) in quadrilateral \(ABCD\) when \(\angle A = {ang}^\circ\).",
        "Find \(\angle B\) in quadrilateral \(ABCD\) such that consecutive interior angles with \(\angle A = {ang}^\circ\) sum to 180°.",
        "Evaluate \(\angle B\) for which \(AD \parallel BC\) in quadrilateral \(ABCD\) with \(\angle A = {ang}^\circ\).",
        "Compute \(\angle B\) in quadrilateral \(ABCD\) so that \(AD \parallel BC\) given \(\angle A = {ang}^\circ\).",
        "If \(AD \parallel BC\) in quadrilateral \(ABCD\) and \(\angle A = {ang}^\circ\), what must \(\angle B\) be?",
        "In quadrilateral \(ABCD\), find \(\angle B\) such that \(\angle A + \angle B = 180^\circ\) given \(\angle A = {ang}^\circ\)."
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx // 10
        sub_idx = idx % 10
        qcode = f"{tc}-OSC-{seq}"
        has_fig = (sub_idx in [0, 1, 2, 3, 4, 5, 6]) # 70% figures

        if arch == 0:
            c1, a, c2, b, x_ans = data_0[sub_idx]
            svg = svg_parallelogram("A", "B", "C", "D") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(a=a, b=b)
            corr = f"{x_ans}"
            dist = [f"{x_ans + 5}", f"{x_ans - 5 if x_ans > 5 else x_ans + 10}", f"{x_ans + 15}"]
            sol = f"**Step 1: Parallelogram opposite angles test**\nA quadrilateral is a parallelogram if opposite angles are equal: \(\angle A = \angle C\).\n\(x + {a} = 2x - {b} \implies 2x - x = {a} + {b} \implies x = {x_ans}\).\n**Step 2: Conclusion**\n{x_ans}."
        elif arch == 1:
            a, b, c, d, x_ans = data_1[sub_idx]
            svg = svg_parallelogram("A", "B", "C", "D") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(a=a, b=b, c=c, d=d)
            corr = f"{x_ans}"
            dist = [f"{x_ans + 2}", f"{x_ans - 2 if x_ans > 2 else x_ans + 4}", f"{x_ans + 6}"]
            sol = f"**Step 1: Parallelogram opposite sides test**\n\(AB = CD \implies {a}x - {b} = {c}x + {d} \implies {a-c}x = {b+d} \implies x = {x_ans}\).\n**Step 2: Conclusion**\n{x_ans}."
        elif arch == 2:
            a, b, c, d, y_ans = data_2[sub_idx]
            svg = svg_parallelogram("A", "B", "C", "D", "AB || CD") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(a=a, b=b, c=c, d=d)
            corr = f"{y_ans}"
            dist = [f"{y_ans + 2}", f"{y_ans - 2 if y_ans > 2 else y_ans + 4}", f"{y_ans + 5}"]
            sol = f"**Step 1: Parallelogram test**\nA quadrilateral is a parallelogram if one pair of opposite sides is both parallel and equal: \(AB = CD\).\n\({a}y - {b} = {c}y + {d} \implies {a-c}y = {b+d} \implies y = {y_ans}\).\n**Step 2: Conclusion**\n{y_ans}."
        elif arch == 3:
            a, b, c, d, z_ans = data_3[sub_idx]
            svg = svg_parallelogram_diagonals() if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(a=a, b=b, d=d)
            corr = f"{z_ans}"
            dist = [f"{z_ans + 3}", f"{z_ans - 3 if z_ans > 3 else z_ans + 6}", f"{z_ans + 8}"]
            sol = f"**Step 1: Diagonal bisection test**\n\(OA = OC \implies {a}z + {b} = z + {d} \implies {a-1}z = {d-b} \implies z = {z_ans}\).\n**Step 2: Conclusion**\n{z_ans}."
        elif arch == 4:
            d1, d2, p_ans = data_4[sub_idx]
            svg = svg_parallelogram("A", "B", "C", "D") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(d1=d1, d2=d2)
            corr = f"{p_ans} cm"
            dist = [f"{p_ans + 4} cm", f"{p_ans - 4 if p_ans > 4 else p_ans + 8} cm", f"{d1 + d2 + 6} cm"]
            sol = f"**Step 1: Varignon's Theorem**\nThe perimeter of the parallelogram formed by joining the midpoints of sides of a quadrilateral is equal to the sum of its diagonals: \(P = AC + BD\).\n\(P = {d1} + {d2} = {p_ans}\text{{ cm}}\).\n**Step 2: Conclusion**\n{p_ans} cm."
        elif arch == 5:
            ang, ans_c = data_5[sub_idx]
            supp = 180 - ang
            svg = svg_parallelogram("A", "B", "C", "D") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(ang=ang, supp=supp)
            corr = f"{ans_c}^\circ"
            dist = [f"{ans_c + 10}^\circ", f"{ans_c - 10}^\circ", f"{supp}^\circ"]
            sol = f"**Step 1: Opposite angles property**\nIn a parallelogram, opposite angles are equal: \(\angle C = \angle A = {ang}^\circ\).\n**Step 2: Conclusion**\n{ans_c}°."
        elif arch == 6:
            a, b, c, d_ans = data_6[sub_idx]
            svg = svg_parallelogram("A", "B", "C", "D") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(a=a, b=b, c=c)
            corr = f"{d_ans}^\circ"
            dist = [f"{d_ans + 10}^\circ", f"{d_ans - 10}^\circ", f"{360 - d_ans}^\circ"]
            sol = f"**Step 1: Angle sum of quadrilateral**\n\(\angle A + \angle B + \angle C + \angle D = 360^\circ\).\n\(\angle D = 360^\circ - ({a}^\circ + {b}^\circ + {c}^\circ) = 360^\circ - {a+b+c}^\circ = {d_ans}^\circ\).\n**Step 2: Conclusion**\n{d_ans}°."
        elif arch == 7:
            ang, b_ans = data_7[sub_idx]
            svg = svg_parallelogram("A", "B", "C", "D") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_7[sub_idx].format(ang=ang)
            corr = f"{b_ans}^\circ"
            dist = [f"{b_ans + 10}^\circ", f"{b_ans - 10}^\circ", f"{ang}^\circ"]
            sol = f"**Step 1: Interior angles test**\nFor \(AD \parallel BC\), consecutive interior angles must sum to 180°: \(\angle A + \angle B = 180^\circ\).\n\(\angle B = 180^\circ - {ang}^\circ = {b_ans}^\circ\).\n**Step 2: Conclusion**\n{b_ans}°."

        diff = "easy" if arch in [1, 5, 7] else ("medium" if arch in [0, 2, 6] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, CH_NUM, CH_NAME, tc, tname, seq, has_fig, diff))

    return qs

print("gen_5_1_3 defined.")
