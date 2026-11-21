# scripts/append_ch6_circles_incircle.py
import re

svg_funcs = '''
def svg_incircle(r_lbl, a_lbl, b_lbl, c_lbl):
    return (
        f'<svg width="240" height="200" viewBox="0 0 240 200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a;border-radius:8px;display:block;margin:12px auto;">'
        f'<polygon points="120,30 40,170 200,170" fill="none" stroke="#38bdf8" stroke-width="2"/>'
        f'<circle cx="120" cy="123" r="47" fill="none" stroke="#f43f5e" stroke-width="1.8"/>'
        f'<circle cx="120" cy="123" r="3" fill="#f8fafc"/>'
        f'<line x1="120" y1="123" x2="120" y2="170" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2,2"/>'
        f'<text x="115" y="25" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">A</text>'
        f'<text x="25" y="175" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">B</text>'
        f'<text x="205" y="175" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">C</text>'
        f'<text x="110" y="115" fill="#f8fafc" font-size="10" font-family="sans-serif">I</text>'
        f'<text x="125" y="150" fill="#f59e0b" font-size="10" font-family="sans-serif">{r_lbl}</text>'
        f'</svg>'
    )

def svg_circumcircle(r_lbl, a_lbl, b_lbl, c_lbl):
    return (
        f'<svg width="240" height="200" viewBox="0 0 240 200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a;border-radius:8px;display:block;margin:12px auto;">'
        f'<circle cx="120" cy="100" r="75" fill="none" stroke="#38bdf8" stroke-width="2"/>'
        f'<polygon points="120,25 55,145 185,145" fill="none" stroke="#10b981" stroke-width="2"/>'
        f'<circle cx="120" cy="100" r="3" fill="#f8fafc"/>'
        f'<line x1="120" y1="100" x2="120" y2="25" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2,2"/>'
        f'<text x="115" y="20" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">A</text>'
        f'<text x="40" y="155" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">B</text>'
        f'<text x="195" y="155" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">C</text>'
        f'<text x="110" y="105" fill="#f8fafc" font-size="10" font-family="sans-serif">C</text>'
        f'<text x="125" y="65" fill="#f59e0b" font-size="10" font-family="sans-serif">{r_lbl}</text>'
        f'</svg>'
    )
'''

generators_code = '''
# -----------------------------------------------------------------------------
# 6.2.1: Constructing angle bisectors of triangle
# -----------------------------------------------------------------------------
def gen_6_2_1():
    tc = "MH-9-MTH2-6-6.2.1"
    tname = "Constructing angle bisectors of triangle"
    qs = []
    
    # Arch 0: Angle BIC = 90 + A/2
    data_0 = [
        (40, 110), (50, 115), (60, 120), (70, 125), (80, 130),
        (30, 105), (54, 117), (64, 122), (76, 128), (90, 135)
    ]
    tmpls_0 = [
        "In \\(\\triangle ABC\\), point \\(I\\) is the incentre. If \\(\\angle A = {A}^\\circ\\), find \\(\\angle BIC\\).",
        "The angle bisectors of \\(\\angle B\\) and \\(\\angle C\\) of \\(\\triangle ABC\\) intersect at incentre \\(I\\). If \\(\\angle BAC = {A}^\\circ\\), calculate \\(\\angle BIC\\).",
        "What is the measure of angle \\(\\angle BIC\\) formed by the incentre \\(I\\) in \\(\\triangle ABC\\) when \\(\\angle A = {A}^\\circ\\)?",
        "Calculate \\(\\angle BIC\\) in \\(\\triangle ABC\\) given incentre \\(I\\) and \\(\\angle A = {A}^\\circ\\).",
        "Determine the angle \\(\\angle BIC\\) in \\(\\triangle ABC\\) where \\(I\\) is the point of concurrence of angle bisectors and \\(\\angle A = {A}^\\circ\\).",
        "Evaluate \\(\\angle BIC\\) for incentre \\(I\\) of \\(\\triangle ABC\\) with \\(\\angle A = {A}^\\circ\\).",
        "If \\(I\\) is the incentre of \\(\\triangle ABC\\) and \\(\\angle A = {A}^\\circ\\), what is \\(\\angle BIC\\)?",
        "Find \\(\\angle BIC\\) in \\(\\triangle ABC\\) knowing \\(I\\) is the incentre and \\(\\angle A = {A}^\\circ\\).",
        "Compute the measure of \\(\\angle BIC\\) formed at the incentre \\(I\\) of \\(\\triangle ABC\\) with vertex angle \\(\\angle A = {A}^\\circ\\).",
        "In \\(\\triangle ABC\\), \\(I\\) is the incentre. Calculate \\(\\angle BIC\\) if \\(\\angle A = {A}^\\circ\\)."
    ]
    
    # Arch 1: Angle AIC = 90 + B/2
    data_1 = [
        (40, 110), (50, 115), (60, 120), (70, 125), (80, 130),
        (36, 108), (48, 114), (66, 123), (74, 127), (84, 132)
    ]
    tmpls_1 = [
        "In \\(\\triangle ABC\\), angle bisectors of \\(\\angle A\\) and \\(\\angle C\\) meet at \\(I\\). If \\(\\angle B = {B}^\\circ\\), find \\(\\angle AIC\\).",
        "For incentre \\(I\\) of \\(\\triangle ABC\\), calculate \\(\\angle AIC\\) when \\(\\angle B = {B}^\\circ\\).",
        "What is \\(\\angle AIC\\) in \\(\\triangle ABC\\) if \\(I\\) is the incentre and \\(\\angle B = {B}^\\circ\\)?",
        "Determine the measure of \\(\\angle AIC\\) formed by angle bisectors intersecting at \\(I\\) given \\(\\angle B = {B}^\\circ\\).",
        "Compute \\(\\angle AIC\\) in \\(\\triangle ABC\\) where \\(I\\) is the incentre and \\(\\angle ABC = {B}^\\circ\\).",
        "Evaluate \\(\\angle AIC\\) for \\(\\triangle ABC\\) with incentre \\(I\\) having \\(\\angle B = {B}^\\circ\\).",
        "Find \\(\\angle AIC\\) in \\(\\triangle ABC\\) given incentre \\(I\\) and \\(\\angle B = {B}^\\circ\\).",
        "Calculate the measure of \\(\\angle AIC\\) subtended at incentre \\(I\\) when \\(\\angle B = {B}^\\circ\\).",
        "If \\(I\\) is the incentre of \\(\\triangle ABC\\) and \\(\\angle B = {B}^\\circ\\), what is \\(\\angle AIC\\)?",
        "In \\(\\triangle ABC\\), incentre is \\(I\\). Determine \\(\\angle AIC\\) if \\(\\angle B = {B}^\\circ\\)."
    ]
    
    # Arch 2: Area of triangle = inradius * semi-perimeter -> Area = r * s
    data_2 = [
        (2, 12, 24), (3, 15, 45), (4, 18, 72), (5, 20, 100), (6, 25, 150),
        (2, 18, 36), (3, 22, 66), (4, 28, 112), (5, 32, 160), (6, 35, 210)
    ]
    tmpls_2 = [
        "The inradius of a triangle is {r}\\text{{ cm}} and its semi-perimeter is {s}\\text{{ cm}}. Find the area of the triangle.",
        "A triangle has semi-perimeter \\(s = {s}\\text{{ cm}}\\) and inradius \\(r = {r}\\text{{ cm}}\\). Calculate its area.",
        "What is the area of a triangle having inradius \\(r = {r}\\text{{ cm}}\\) and semi-perimeter \\(s = {s}\\text{{ cm}}\\)?" ,
        "Compute the area of \\(\\triangle ABC\\) with inradius {r}\\text{{ cm}} and semi-perimeter {s}\\text{{ cm}}.",
        "Determine the area of a triangle whose inscribed circle has radius {r}\\text{{ cm}} and whose semi-perimeter is {s}\\text{{ cm}}.",
        "Evaluate the area of the triangle with inradius \\(r = {r}\\text{{ cm}}\\) and perimeter \\(2s = {2*s}\\text{{ cm}}\\).",
        "Find the area of a triangle with perimeter \\({2*s}\\text{{ cm}}\\) and inradius \\({r}\\text{{ cm}}\\).",
        "Calculate area \\(\\Delta = r \\times s\\) for inradius \\({r}\\text{{ cm}}\\) and semi-perimeter \\({s}\\text{{ cm}}\\).",
        "In a triangle, semi-perimeter is \\({s}\\text{{ cm}}\\) and inradius is \\({r}\\text{{ cm}}\\). What is its area?",
        "If a triangle has inradius \\({r}\\text{{ cm}}\\) and semi-perimeter \\({s}\\text{{ cm}}\\), find its area."
    ]
    
    # Arch 3: Given Area and semi-perimeter s, find inradius r = Area / s
    data_3 = [
        (24, 12, 2), (45, 15, 3), (72, 18, 4), (100, 20, 5), (150, 25, 6),
        (48, 16, 3), (84, 21, 4), (120, 24, 5), (168, 28, 6), (216, 36, 6)
    ]
    tmpls_3 = [
        "The area of a triangle is {area}\\text{{ cm}}^2 and its semi-perimeter is {s}\\text{{ cm}}. Find its inradius.",
        "In a triangle with area {area}\\text{{ cm}}^2 and semi-perimeter {s}\\text{{ cm}}, calculate the inradius \\(r\\).",
        "What is the inradius of a triangle having area {area}\\text{{ cm}}^2 and perimeter {2*s}\\text{{ cm}}?",
        "Compute the inradius \\(r\\) of a triangle with area {area}\\text{{ cm}}^2 and semi-perimeter {s}\\text{{ cm}}.",
        "Determine the radius of the incircle of a triangle whose area is {area}\\text{{ cm}}^2 and semi-perimeter is {s}\\text{{ cm}}.",
        "Evaluate the inradius for a triangle with area {area}\\text{{ cm}}^2 and perimeter {2*s}\\text{{ cm}}.",
        "Find the radius of inscribed circle of a triangle of area {area}\\text{{ cm}}^2 having semi-perimeter {s}\\text{{ cm}}.",
        "Calculate inradius \\(r = \\frac{{\\text{{Area}}}}{{s}}\\) for area {area}\\text{{ cm}}^2 and semi-perimeter {s}\\text{{ cm}}.",
        "If a triangle has area {area}\\text{{ cm}}^2 and semi-perimeter {s}\\text{{ cm}}, what is its inradius?",
        "In a triangle, area is {area}\\text{{ cm}}^2 and semi-perimeter is {s}\\text{{ cm}}. Find the inradius."
    ]
    
    # Arch 4: Given inradius r and Area, find perimeter 2s = 2 * (Area / r)
    data_4 = [
        (2, 20, 20), (3, 36, 24), (4, 56, 28), (5, 80, 32), (6, 120, 40),
        (2, 30, 30), (3, 48, 32), (4, 72, 36), (5, 110, 44), (6, 150, 50)
    ]
    tmpls_4 = [
        "The inradius of a triangle is {r}\\text{{ cm}} and its area is {area}\\text{{ cm}}^2. Find the perimeter of the triangle.",
        "Calculate the perimeter of a triangle with area {area}\\text{{ cm}}^2 and inradius {r}\\text{{ cm}}.",
        "What is the perimeter of a triangle whose inscribed circle has radius {r}\\text{{ cm}} and area {area}\\text{{ cm}}^2?",
        "Compute the perimeter \\(2s\\) of a triangle having inradius {r}\\text{{ cm}} and area {area}\\text{{ cm}}^2.",
        "Determine the perimeter of a triangle with area {area}\\text{{ cm}}^2 and inradius {r}\\text{{ cm}}.",
        "Evaluate the perimeter of the triangle with inradius {r}\\text{{ cm}} and area {area}\\text{{ cm}}^2.",
        "Find the perimeter of a triangle of area {area}\\text{{ cm}}^2 having inradius {r}\\text{{ cm}}.",
        "Calculate the triangle perimeter given inradius {r}\\text{{ cm}} and area {area}\\text{{ cm}}^2.",
        "If inradius is {r}\\text{{ cm}} and area is {area}\\text{{ cm}}^2, what is the perimeter of the triangle?",
        "In a triangle, inradius is {r}\\text{{ cm}} and area is {area}\\text{{ cm}}^2. Find the perimeter."
    ]
    
    # Arch 5: Concurrence property of angle bisectors: incentre is equidistant from sides
    data_5 = [
        ("AB", "BC", 4), ("BC", "AC", 5), ("AC", "AB", 6), ("AB", "AC", 7), ("BC", "AB", 8),
        ("side AB", "side BC", 9), ("side BC", "side AC", 10), ("side AC", "side AB", 11), ("side AB", "side AC", 12), ("side BC", "side AB", 13)
    ]
    tmpls_5 = [
        "The incentre \\(I\\) of a triangle is at distance {d}\\text{{ cm}} from side \\({s1}\\). What is its perpendicular distance from \\({s2}\\)?",
        "In \\(\\triangle ABC\\), point \\(I\\) is the incentre. If the distance from \\(I\\) to \\({s1}\\) is {d}\\text{{ cm}}, find its distance to \\({s2}\\).",
        "Incentre \\(I\\) of a triangle is equidistant from all three sides. If distance to \\({s1}\\) is {d}\\text{{ cm}}, calculate distance to \\({s2}\\).",
        "What is the perpendicular distance from incentre \\(I\\) to \\({s2}\\) if its distance to \\({s1}\\) is {d}\\text{{ cm}}?",
        "Determine the distance from incentre \\(I\\) to \\({s2}\\) given that distance to \\({s1}\\) is {d}\\text{{ cm}}.",
        "Evaluate the distance from the incentre of a triangle to \\({s2}\\) knowing distance to \\({s1}\\) is {d}\\text{{ cm}}.",
        "Find the perpendicular distance from incentre \\(I\\) to \\({s2}\\) when distance to \\({s1}\\) is {d}\\text{{ cm}}.",
        "Compute the distance from incentre \\(I\\) to side \\({s2}\\) if distance to \\({s1}\\) is {d}\\text{{ cm}}.",
        "If incentre \\(I\\) is at distance {d}\\text{{ cm}} from \\({s1}\\), what is its distance from \\({s2}\\)?",
        "In a triangle, the distance from incentre \\(I\\) to \\({s1}\\) is {d}\\text{{ cm}}. Find the distance from \\(I\\) to \\({s2}\\)."
    ]
    
    # Arch 6: Angle AIB = 90 + C/2
    data_6 = [
        (40, 110), (50, 115), (60, 120), (70, 125), (80, 130),
        (32, 106), (44, 112), (68, 124), (72, 126), (86, 133)
    ]
    tmpls_6 = [
        "In \\(\\triangle ABC\\), incentre is \\(I\\). If \\(\\angle C = {C}^\\circ\\), find \\(\\angle AIB\\).",
        "For incentre \\(I\\) of \\(\\triangle ABC\\), compute \\(\\angle AIB\\) when \\(\\angle C = {C}^\\circ\\).",
        "What is the measure of \\(\\angle AIB\\) formed at incentre \\(I\\) if \\(\\angle C = {C}^\\circ\\)?",
        "Calculate \\(\\angle AIB\\) in \\(\\triangle ABC\\) given incentre \\(I\\) and \\(\\angle C = {C}^\\circ\\).",
        "Determine the angle \\(\\angle AIB\\) subtended at incentre \\(I\\) when \\(\\angle C = {C}^\\circ\\).",
        "Evaluate \\(\\angle AIB\\) in \\(\\triangle ABC\\) having \\(\\angle C = {C}^\\circ\\) and incentre \\(I\\).",
        "If \\(I\\) is the incentre of \\(\\triangle ABC\\) and \\(\\angle C = {C}^\\circ\\), find \\(\\angle AIB\\).",
        "Find \\(\\angle AIB\\) for \\(\\triangle ABC\\) where \\(I\\) is the incentre and \\(\\angle C = {C}^\\circ\\).",
        "Compute the measure of \\(\\angle AIB\\) in \\(\\triangle ABC\\) with \\(\\angle C = {C}^\\circ\\).",
        "In \\(\\triangle ABC\\) with incentre \\(I\\), determine \\(\\angle AIB\\) if \\(\\angle C = {C}^\\circ\\)."
    ]
    
    # Arch 7: Angle A from angle BIC: A = 2 * (BIC - 90)
    data_7 = [
        (105, 30), (110, 40), (115, 50), (120, 60), (125, 70),
        (130, 80), (135, 90), (112, 44), (122, 64), (128, 76)
    ]
    tmpls_7 = [
        "In \\(\\triangle ABC\\), point \\(I\\) is the incentre. If \\(\\angle BIC = {bic}^\\circ\\), find \\(\\angle A\\).",
        "If \\(\\angle BIC = {bic}^\\circ\\) at the incentre \\(I\\) of \\(\\triangle ABC\\), calculate vertex angle \\(\\angle A\\).",
        "What is the measure of \\(\\angle A\\) in \\(\\triangle ABC\\) if \\(\\angle BIC = {bic}^\\circ\\) where \\(I\\) is the incentre?",
        "Determine \\(\\angle A\\) in \\(\\triangle ABC\\) knowing \\(I\\) is the incentre and \\(\\angle BIC = {bic}^\\circ\\).",
        "Calculate vertex angle \\(\\angle A\\) of \\(\\triangle ABC\\) given that \\(\\angle BIC = {bic}^\\circ\\) at incentre \\(I\\).",
        "Evaluate the measure of \\(\\angle A\\) in \\(\\triangle ABC\\) having incentre \\(I\\) and \\(\\angle BIC = {bic}^\\circ\\).",
        "Find \\(\\angle A\\) in \\(\\triangle ABC\\) when angle formed by angle bisectors is \\(\\angle BIC = {bic}^\\circ\\).",
        "Compute \\(\\angle A\\) for \\(\\triangle ABC\\) with incentre \\(I\\) if \\(\\angle BIC = {bic}^\\circ\\).",
        "If \\(\\angle BIC = {bic}^\\circ\\) at incentre \\(I\\) in \\(\\triangle ABC\\), what is \\(\\angle A\\)?",
        "In \\(\\triangle ABC\\) with incentre \\(I\\), find \\(\\angle A\\) given \\(\\angle BIC = {bic}^\\circ\\)."
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        qcode = f"{tc}-OSC-{seq}"
        
        if arch == 0:
            A, ans_bic = data_0[sub_idx]
            svg = svg_incircle("", f"\\angle A = {A}^\\circ", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(A=A)
            corr = f"{ans_bic}^\\circ"
            dist = [f"{ans_bic + 10}^\\circ", f"{ans_bic - 10 if ans_bic > 10 else ans_bic + 15}^\\circ", f"{180 - A}^\\circ"]
            sol = f"**Step 1: Incentre angle formula**\\n\\(\\angle BIC = 90^\\circ + \\frac{{\\angle A}}{{2}} = 90^\\circ + \\frac{{{A}^\\circ}}{{2}} = 90^\\circ + {A//2}^\\circ = {ans_bic}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_bic}°."
        elif arch == 1:
            B, ans_aic = data_1[sub_idx]
            svg = svg_incircle("", "", f"\\angle B = {B}^\\circ", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(B=B)
            corr = f"{ans_aic}^\\circ"
            dist = [f"{ans_aic + 10}^\\circ", f"{ans_aic - 10 if ans_aic > 10 else ans_aic + 15}^\\circ", f"{180 - B}^\\circ"]
            sol = f"**Step 1: Incentre angle formula**\\n\\(\\angle AIC = 90^\\circ + \\frac{{\\angle B}}{{2}} = 90^\\circ + \\frac{{{B}^\\circ}}{{2}} = 90^\\circ + {B//2}^\\circ = {ans_aic}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_aic}°."
        elif arch == 2:
            r, s, ans_area = data_2[sub_idx]
            svg = svg_incircle(f"r = {r}", "", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(r=r, s=s)
            corr = f"{ans_area}\\text{{ cm}}^2"
            dist = [f"{ans_area + 10}\\text{{ cm}}^2", f"{ans_area - 10}\\text{{ cm}}^2", f"{r * s * 2}\\text{{ cm}}^2"]
            sol = f"**Step 1: Formula**\\n\\(\\text{{Area}} = r \\times s = {r} \\times {s} = {ans_area}\\text{{ cm}}^2\\).\\n**Step 2: Conclusion**\\n{ans_area} cm²."
        elif arch == 3:
            area, s, ans_r = data_3[sub_idx]
            svg = svg_incircle("r = ?", "", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(area=area, s=s)
            corr = f"{ans_r}\\text{{ cm}}"
            dist = [f"{ans_r + 2}\\text{{ cm}}", f"{ans_r - 1}\\text{{ cm}}", f"{s // 2}\\text{{ cm}}"]
            sol = f"**Step 1: Formula**\\n\\(r = \\frac{{\\text{{Area}}}}{{s}} = \\frac{{{area}}}{{{s}}} = {ans_r}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_r} cm."
        elif arch == 4:
            r, area, ans_p = data_4[sub_idx]
            svg = svg_incircle(f"r = {r}", "", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(r=r, area=area)
            corr = f"{ans_p}\\text{{ cm}}"
            dist = [f"{ans_p + 4}\\text{{ cm}}", f"{ans_p - 4}\\text{{ cm}}", f"{ans_p // 2}\\text{{ cm}}"]
            sol = f"**Step 1: Semi-perimeter and perimeter**\\n\\(s = \\frac{{\\text{{Area}}}}{{r}} = \\frac{{{area}}}{{{r}}} = {ans_p // 2}\\text{{ cm}}\\).\\n\\(\\text{{Perimeter}} = 2s = 2 \\times {ans_p // 2} = {ans_p}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_p} cm."
        elif arch == 5:
            s1, s2, ans_d = data_5[sub_idx]
            svg = svg_incircle(f"r = {ans_d}", "", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(s1=s1, s2=s2, d=ans_d)
            corr = f"{ans_d}\\text{{ cm}}"
            dist = [f"{ans_d + 2}\\text{{ cm}}", f"{ans_d - 2 if ans_d > 2 else ans_d + 3}\\text{{ cm}}", f"{ans_d * 2}\\text{{ cm}}"]
            sol = f"**Step 1: Equidistant property of incentre**\\nThe incentre is equidistant from all three sides of the triangle (this distance is the inradius \\(r\\)).\\nHence, distance to \\({s2}\\) is also \\({ans_d}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_d} cm."
        elif arch == 6:
            C, ans_aib = data_6[sub_idx]
            svg = svg_incircle("", "", "", f"\\angle C = {C}^\\circ") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(C=C)
            corr = f"{ans_aib}^\\circ"
            dist = [f"{ans_aib + 10}^\\circ", f"{ans_aib - 10 if ans_aib > 10 else ans_aib + 15}^\\circ", f"{180 - C}^\\circ"]
            sol = f"**Step 1: Incentre angle formula**\\n\\(\\angle AIB = 90^\\circ + \\frac{{\\angle C}}{{2}} = 90^\\circ + \\frac{{{C}^\\circ}}{{2}} = 90^\\circ + {C//2}^\\circ = {ans_aib}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_aib}°."
        elif arch == 7:
            bic, ans_a = data_7[sub_idx]
            svg = svg_incircle("", "", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_7[sub_idx].format(bic=bic)
            corr = f"{ans_a}^\\circ"
            dist = [f"{ans_a + 10}^\\circ", f"{ans_a - 10 if ans_a > 10 else ans_a + 15}^\\circ", f"{180 - ans_a}^\\circ"]
            sol = f"**Step 1: Inverting formula**\\n\\(\\angle BIC = 90^\\circ + \\frac{{\\angle A}}{{2}} \\implies \\frac{{\\angle A}}{{2}} = {bic}^\\circ - 90^\\circ = {bic - 90}^\\circ\\).\\n\\(\\angle A = 2 \\times {bic - 90}^\\circ = {ans_a}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_a}°."

        diff = "easy" if arch in [0,1,6] else ("medium" if arch in [2,3,7] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs
'''

with open("scripts/generate_flawless_ch6.py", "r", encoding="utf-8") as f:
    orig = f.read()

# Add SVG functions near top (after svg_circle_chord)
idx_svg = orig.find("def svg_circle_chord")
idx_svg_end = orig.find("# -----------------------------------------------------------------------------", idx_svg)
orig = orig[:idx_svg_end] + svg_funcs + "\n" + orig[idx_svg_end:]

# Insert gen_6_2_1 before main
idx = orig.find("def main():")
new_content = orig[:idx] + generators_code + "\n" + orig[idx:]

# Update main
new_content = new_content.replace(
    '    qs.extend(q2)',
    '    qs.extend(q2)\n    print("Generating 6.2.1...")\n    q3 = gen_6_2_1()\n    print(f"Generated 6.2.1: {len(q3)} questions")\n    qs.extend(q3)'
)

with open("scripts/generate_flawless_ch6.py", "w", encoding="utf-8") as f:
    f.write(new_content)
print("Added 6.2.1 and SVG functions to generate_flawless_ch6.py!")
