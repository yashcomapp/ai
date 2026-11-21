# scripts/append_ch6_final.py
import re

code_final = '''
# -----------------------------------------------------------------------------
# 6.2.2: Incentre (I) and inradius
# -----------------------------------------------------------------------------
def gen_6_2_2():
    tc = "MH-9-MTH2-6-6.2.2"
    tname = "Incentre (I) and inradius"
    qs = []
    
    # Arch 0: Right triangle legs a, b, hyp c -> inradius r = (a + b - c)/2
    data_0 = [
        (6, 8, 10, 2), (8, 15, 17, 3), (9, 40, 41, 4), (12, 35, 37, 5), (20, 21, 29, 6),
        (16, 63, 65, 7), (28, 45, 53, 10), (33, 56, 65, 12), (48, 55, 73, 15), (65, 72, 97, 20)
    ]
    tmpls_0 = [
        "In right-angled \\(\\triangle ABC\\) with sides {a}\\text{{ cm}}, {b}\\text{{ cm}} and hypotenuse {c}\\text{{ cm}}, find the inradius \\(r\\).",
        "A right-angled triangle has perpendicular sides {a}\\text{{ cm}} and {b}\\text{{ cm}}, and hypotenuse {c}\\text{{ cm}}. Calculate the radius of its inscribed circle.",
        "What is the inradius of a right triangle having legs {a}\\text{{ cm}} and {b}\\text{{ cm}} and hypotenuse {c}\\text{{ cm}}?",
        "Calculate inradius \\(r = \\frac{{a + b - c}}{{2}}\\) for right \\(\\triangle ABC\\) with sides {a}\\text{{ cm}}, {b}\\text{{ cm}}, and {c}\\text{{ cm}}.",
        "Determine the radius of the incircle of right-angled \\(\\triangle ABC\\) having sides {a}\\text{{ cm}}, {b}\\text{{ cm}}, and {c}\\text{{ cm}}.",
        "Evaluate the inradius for right \\(\\triangle ABC\\) with legs {a}\\text{{ cm}} and {b}\\text{{ cm}} and hypotenuse {c}\\text{{ cm}}.",
        "Find the inradius of \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(AB = {a}\\text{{ cm}}\\), \\(BC = {b}\\text{{ cm}}\\), and \\(AC = {c}\\text{{ cm}}\\).",
        "Compute the inradius \\(r\\) of right triangle with sides {a}\\text{{ cm}}, {b}\\text{{ cm}}, and {c}\\text{{ cm}}.",
        "If a right triangle has perpendicular legs of {a}\\text{{ cm}} and {b}\\text{{ cm}} and hypotenuse {c}\\text{{ cm}}, what is its inradius?",
        "In right \\(\\triangle ABC\\) with sides {a}\\text{{ cm}}, {b}\\text{{ cm}}, and {c}\\text{{ cm}}, determine the inradius."
    ]
    
    # Arch 1: Equilateral triangle with side a -> inradius r = a / (2*sqrt(3))
    data_1 = [
        ("6\\sqrt{3}", 3), ("8\\sqrt{3}", 4), ("10\\sqrt{3}", 5), ("12\\sqrt{3}", 6), ("14\\sqrt{3}", 7),
        ("16\\sqrt{3}", 8), ("18\\sqrt{3}", 9), ("20\\sqrt{3}", 10), ("22\\sqrt{3}", 11), ("24\\sqrt{3}", 12)
    ]
    tmpls_1 = [
        "In an equilateral triangle of side {a}\\text{{ cm}}, find the inradius \\(r\\).",
        "Calculate the inradius of an equilateral triangle whose side length is {a}\\text{{ cm}}.",
        "What is the radius of the incircle of an equilateral triangle with sides {a}\\text{{ cm}}?",
        "Determine the inradius \\(r = \\frac{{a}}{{2\\sqrt{{3}}}}\\) for an equilateral triangle with side {a}\\text{{ cm}}.",
        "Compute the inradius of equilateral \\(\\triangle ABC\\) where each side is {a}\\text{{ cm}}.",
        "Evaluate the inradius for an equilateral triangle having side length {a}\\text{{ cm}}.",
        "Find the radius of the inscribed circle in equilateral \\(\\triangle ABC\\) with side {a}\\text{{ cm}}.",
        "If the side of an equilateral triangle is {a}\\text{{ cm}}, calculate its inradius.",
        "What is the inradius of equilateral \\(\\triangle ABC\\) with side length {a}\\text{{ cm}}?",
        "In equilateral \\(\\triangle ABC\\), side length is {a}\\text{{ cm}}. Find the inradius."
    ]
    
    # Arch 2: Area of incircle: A = pi * r^2
    data_2 = [
        (1, 1), (2, 4), (3, 9), (4, 16), (5, 25),
        (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)
    ]
    tmpls_2 = [
        "If the inradius of a triangle is {r}\\text{{ cm}}, find the area of its incircle in terms of \\(\\pi\\).",
        "Calculate the area of the incircle of a triangle having inradius \\(r = {r}\\text{{ cm}}\\).",
        "What is the area of the incircle with radius {r}\\text{{ cm}} in terms of \\(\\pi\\)?",
        "Compute the area of the inscribed circle of \\(\\triangle ABC\\) given inradius \\(r = {r}\\text{{ cm}}\\).",
        "Determine the area of the incircle (in terms of \\(\\pi\\)) when inradius is {r}\\text{{ cm}}.",
        "Evaluate the area of the incircle with radius {r}\\text{{ cm}}.",
        "Find the area in terms of \\(\\pi\\) of an incircle having radius {r}\\text{{ cm}}.",
        "Calculate incircle area \\(\\pi r^2\\) for inradius \\(r = {r}\\text{{ cm}}\\).",
        "If inradius is {r}\\text{{ cm}}, what is the area of the incircle in terms of \\(\\pi\\)?",
        "In \\(\\triangle ABC\\), inradius is {r}\\text{{ cm}}. Find the area of the incircle."
    ]
    
    # Arch 3: Circumference of incircle: C = 2 * pi * r
    data_3 = [
        (1, 2), (2, 4), (3, 6), (4, 8), (5, 10),
        (6, 12), (7, 14), (8, 16), (9, 18), (10, 20)
    ]
    tmpls_3 = [
        "If the inradius of a triangle is {r}\\text{{ cm}}, find the circumference of its incircle in terms of \\(\\pi\\).",
        "Calculate the circumference of the incircle of a triangle having inradius \\(r = {r}\\text{{ cm}}\\).",
        "What is the circumference of the inscribed circle of \\(\\triangle ABC\\) with inradius {r}\\text{{ cm}}?",
        "Compute the circumference of the incircle in terms of \\(\\pi\\) for inradius {r}\\text{{ cm}}.",
        "Determine the perimeter of the incircle having radius {r}\\text{{ cm}} in terms of \\(\\pi\\).",
        "Evaluate the circumference of the incircle with inradius \\(r = {r}\\text{{ cm}}\\).",
        "Find the circumference of an incircle of radius {r}\\text{{ cm}}.",
        "Calculate circumference \\(2\\pi r\\) of the incircle with inradius {r}\\text{{ cm}}.",
        "If the inradius is {r}\\text{{ cm}}, what is the circumference of the incircle?",
        "In a triangle, inradius is {r}\\text{{ cm}}. Find the circumference of its incircle."
    ]
    
    # Arch 4: Tangent segments from vertex A: x = s - a
    data_4 = [
        (7, 8, 9, 12, 5), (5, 6, 7, 9, 4), (6, 7, 9, 11, 5), (8, 9, 11, 14, 6), (10, 11, 13, 17, 7),
        (12, 13, 15, 20, 8), (14, 15, 17, 23, 9), (16, 17, 19, 26, 10), (18, 19, 21, 29, 11), (20, 21, 23, 32, 12)
    ]
    tmpls_4 = [
        "In \\(\\triangle ABC\\) with sides \\(a = {a}\\text{{ cm}}\\), \\(b = {b}\\text{{ cm}}\\), and \\(c = {c}\\text{{ cm}}\\), incircle touches side \\(BC\\) at \\(D\\). Find length of tangent segment \\(AF = s - a\\).",
        "The incircle of \\(\\triangle ABC\\) touches sides \\(BC, CA, AB\\) at \\(D, E, F\\). If \\(a = {a}\\), \\(b = {b}\\), \\(c = {c}\\), calculate \\(AF\\).",
        "What is the length of tangent segment \\(AF\\) from vertex \\(A\\) to the incircle in \\(\\triangle ABC\\) with sides {a}, {b}, {c}?",
        "Calculate tangent segment \\(AF = s - a\\) in \\(\\triangle ABC\\) with sides {a}, {b}, {c} and semi-perimeter \\(s = {s}\\).",
        "Determine the length of segment \\(AF\\) on side \\(AB\\) from vertex \\(A\\) to touchpoint with incircle for sides {a}, {b}, {c}.",
        "Evaluate length \\(AF\\) in \\(\\triangle ABC\\) where incircle touches sides and \\(a = {a}, b = {b}, c = {c}\\).",
        "Find length \\(AF\\) of tangent from \\(A\\) to incircle in \\(\\triangle ABC\\) (sides {a}, {b}, {c}).",
        "Compute tangent segment \\(AF = s - a\\) for triangle with sides {a}, {b}, {c} and \\(s = {s}\\).",
        "If incircle touches sides of \\(\\triangle ABC\\) ({a}, {b}, {c}), what is the tangent length from \\(A\\)?",
        "In \\(\\triangle ABC\\) with sides {a}, {b}, {c}, find length \\(AF = s - a\\)."
    ]
    
    # Arch 5: Radius from right triangle hypotenuse and perimeter
    data_5 = [
        (10, 24, 2), (13, 30, 2), (17, 40, 3), (25, 56, 3), (29, 70, 6),
        (37, 84, 5), (41, 90, 4), (53, 126, 10), (65, 154, 12), (73, 176, 15)
    ]
    tmpls_5 = [
        "A right-angled triangle has perimeter {p}\\text{{ cm}} and hypotenuse {c}\\text{{ cm}}. Find its inradius.",
        "Calculate the inradius of a right triangle with perimeter {p}\\text{{ cm}} and hypotenuse {c}\\text{{ cm}}.",
        "What is the inradius of a right triangle having perimeter {p}\\text{{ cm}} and hypotenuse {c}\\text{{ cm}}?",
        "Determine the inradius \\(r = \\frac{{p - 2c}}{{2}}\\) for a right triangle with perimeter {p}\\text{{ cm}} and hypotenuse {c}\\text{{ cm}}.",
        "Compute the radius of the inscribed circle of right triangle with perimeter {p}\\text{{ cm}} and hypotenuse {c}\\text{{ cm}}.",
        "Evaluate the inradius for right-angled triangle having perimeter {p}\\text{{ cm}} and hypotenuse {c}\\text{{ cm}}.",
        "Find the inradius of right triangle given perimeter {p}\\text{{ cm}} and hypotenuse {c}\\text{{ cm}}.",
        "Calculate inradius \\(r\\) for right triangle with perimeter {p}\\text{{ cm}} and hypotenuse {c}\\text{{ cm}}.",
        "If a right triangle has perimeter {p}\\text{{ cm}} and hypotenuse {c}\\text{{ cm}}, what is its inradius?",
        "In a right triangle with perimeter {p}\\text{{ cm}} and hypotenuse {c}\\text{{ cm}}, determine inradius \\(r\\)."
    ]
    
    # Arch 6: Distance from incentre to vertices in equilateral triangle
    data_6 = [
        (3, 6), (4, 8), (5, 10), (6, 12), (7, 14),
        (8, 16), (9, 18), (10, 20), (11, 22), (12, 24)
    ]
    tmpls_6 = [
        "In an equilateral triangle with inradius \\(r = {r}\\text{{ cm}}\\), find the distance from incentre \\(I\\) to any vertex.",
        "The inradius of an equilateral triangle is {r}\\text{{ cm}}. Calculate the distance from incentre \\(I\\) to vertex \\(A\\).",
        "What is the distance of vertex \\(A\\) from incentre \\(I\\) in an equilateral triangle of inradius {r}\\text{{ cm}}?",
        "Determine distance \\(AI = 2r\\) in an equilateral triangle having inradius {r}\\text{{ cm}}.",
        "Compute the distance from incentre \\(I\\) to vertex \\(A\\) in equilateral \\(\\triangle ABC\\) with inradius {r}\\text{{ cm}}.",
        "Evaluate distance \\(AI\\) for an equilateral triangle having inradius {r}\\text{{ cm}}.",
        "Find the distance from the incentre to each vertex in an equilateral triangle of inradius {r}\\text{{ cm}}.",
        "Calculate vertex distance \\(AI\\) knowing \\(AI = 2r\\) in equilateral triangle of inradius {r}\\text{{ cm}}.",
        "If inradius of equilateral triangle is {r}\\text{{ cm}}, what is the distance from incentre to a vertex?",
        "In equilateral \\(\\triangle ABC\\), inradius is {r}\\text{{ cm}}. Find the distance \\(AI\\)."
    ]
    
    # Arch 7: Angle between tangents from vertex A to incircle
    data_7 = [
        (40, 140), (50, 130), (60, 120), (70, 110), (80, 100),
        (45, 135), (55, 125), (65, 115), (75, 105), (85, 95)
    ]
    tmpls_7 = [
        "In \\(\\triangle ABC\\), incircle touches sides \\(AB\\) and \\(AC\\) at \\(F\\) and \\(E\\). If \\(\\angle A = {deg}^\\circ\\), find \\(\\angle FIE\\).",
        "The incircle of \\(\\triangle ABC\\) touches \\(AB\\) at \\(F\\) and \\(AC\\) at \\(E\\). If \\(\\angle BAC = {deg}^\\circ\\), calculate central angle \\(\\angle FIE\\).",
        "What is the measure of angle \\(\\angle FIE\\) subtended at incentre \\(I\\) by contact points \\(F\\) and \\(E\\) if \\(\\angle A = {deg}^\\circ\\)?",
        "Calculate \\(\\angle FIE = 180^\\circ - \\angle A\\) in quadrilateral \\(AFIE\\) when \\(\\angle A = {deg}^\\circ\\).",
        "Determine the angle \\(\\angle FIE\\) in quadrilateral \\(AFIE\\) (\\(\\angle F = \\angle E = 90^\\circ\\)) given \\(\\angle A = {deg}^\\circ\\).",
        "Evaluate \\(\\angle FIE\\) subtended at incentre \\(I\\) given vertex angle \\(\\angle A = {deg}^\\circ\\).",
        "Find \\(\\angle FIE\\) in \\(\\triangle ABC\\) with incircle contact points \\(F\\) and \\(E\\) when \\(\\angle A = {deg}^\\circ\\).",
        "Compute the measure of \\(\\angle FIE\\) formed by radii to touch points \\(F\\) and \\(E\\) if \\(\\angle A = {deg}^\\circ\\).",
        "If \\(\\angle A = {deg}^\\circ\\) in \\(\\triangle ABC\\), what is angle \\(\\angle FIE\\) between radii to touchpoints?",
        "In \\(\\triangle ABC\\), contact points on \\(AB\\) and \\(AC\\) are \\(F\\) and \\(E\\). Find \\(\\angle FIE\\) if \\(\\angle A = {deg}^\\circ\\)."
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        qcode = f"{tc}-OSC-{seq}"
        
        if arch == 0:
            a, b, c, ans_r = data_0[sub_idx]
            svg = svg_incircle("r = ?", f"a = {a}", f"b = {b}", f"c = {c}") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(a=a, b=b, c=c)
            corr = f"{ans_r}\\text{{ cm}}"
            dist = [f"{ans_r + 2}\\text{{ cm}}", f"{ans_r - 1}\\text{{ cm}}", f"{ans_r + 4}\\text{{ cm}}"]
            sol = f"**Step 1: Formula for right triangle inradius**\\n\\(r = \\frac{{a + b - c}}{{2}} = \\frac{{{a} + {b} - {c}}}{{2}} = \\frac{{{a+b-c}}}{{2}} = {ans_r}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_r} cm."
        elif arch == 1:
            a, ans_r = data_1[sub_idx]
            svg = svg_incircle("r = ?", f"side = {a}", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(a=a)
            corr = f"{ans_r}\\text{{ cm}}"
            dist = [f"{ans_r + 2}\\text{{ cm}}", f"{ans_r - 1}\\text{{ cm}}", f"{ans_r * 2}\\text{{ cm}}"]
            sol = f"**Step 1: Inradius of equilateral triangle**\\n\\(r = \\frac{{a}}{{2\\sqrt{{3}}}} = \\frac{{{a}}}{{2\\sqrt{{3}}}} = {ans_r}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_r} cm."
        elif arch == 2:
            r, ans_coef = data_2[sub_idx]
            svg = svg_incircle(f"r = {r}", "", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(r=r)
            corr = f"{ans_coef}\\pi\\text{{ cm}}^2"
            dist = [f"{ans_coef + 5}\\pi\\text{{ cm}}^2", f"{ans_coef - 5 if ans_coef > 5 else ans_coef + 8}\\pi\\text{{ cm}}^2", f"{2 * r}\\pi\\text{{ cm}}^2"]
            sol = f"**Step 1: Area of incircle**\\n\\(\\text{{Area}} = \\pi r^2 = \\pi \\times {r}^2 = {ans_coef}\\pi\\text{{ cm}}^2\\).\\n**Step 2: Conclusion**\\n{ans_coef}π cm²."
        elif arch == 3:
            r, ans_coef = data_3[sub_idx]
            svg = svg_incircle(f"r = {r}", "", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(r=r)
            corr = f"{ans_coef}\\pi\\text{{ cm}}"
            dist = [f"{ans_coef + 4}\\pi\\text{{ cm}}", f"{ans_coef - 2 if ans_coef > 2 else ans_coef + 6}\\pi\\text{{ cm}}", f"{r * r}\\pi\\text{{ cm}}"]
            sol = f"**Step 1: Circumference of incircle**\\n\\(\\text{{Circumference}} = 2\\pi r = 2\\pi \\times {r} = {ans_coef}\\pi\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_coef}π cm."
        elif arch == 4:
            a, b, c, s, ans_af = data_4[sub_idx]
            svg = svg_incircle("", "", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(a=a, b=b, c=c, s=s)
            corr = f"{ans_af}\\text{{ cm}}"
            dist = [f"{ans_af + 2}\\text{{ cm}}", f"{ans_af - 2 if ans_af > 2 else ans_af + 3}\\text{{ cm}}", f"{s}\\text{{ cm}}"]
            sol = f"**Step 1: Tangent length formula**\\n\\(s = \\frac{{{a} + {b} + {c}}}{{2}} = {s}\\text{{ cm}}\\).\\n\\(AF = s - a = {s} - {a} = {ans_af}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_af} cm."
        elif arch == 5:
            c, p, ans_r = data_5[sub_idx]
            svg = svg_incircle("r = ?", "", "", f"hyp = {c}") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(c=c, p=p)
            corr = f"{ans_r}\\text{{ cm}}"
            dist = [f"{ans_r + 2}\\text{{ cm}}", f"{ans_r - 1}\\text{{ cm}}", f"{c // 2}\\text{{ cm}}"]
            sol = f"**Step 1: Formula for right triangle**\\nSince \\(a + b + c = p \\implies a + b = p - c\\).\\n\\(r = \\frac{{a + b - c}}{{2}} = \\frac{{(p - c) - c}}{{2}} = \\frac{{{p} - 2({c})}}{{2}} = \\frac{{{p - 2*c}}}{{2}} = {ans_r}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_r} cm."
        elif arch == 6:
            r, ans_dist = data_6[sub_idx]
            svg = svg_incircle(f"r = {r}", "AI = ?", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(r=r)
            corr = f"{ans_dist}\\text{{ cm}}"
            dist = [f"{ans_dist + 3}\\text{{ cm}}", f"{ans_dist - 3 if ans_dist > 3 else ans_dist + 4}\\text{{ cm}}", f"{r}\\text{{ cm}}"]
            sol = f"**Step 1: Vertex distance in equilateral triangle**\\nIn equilateral triangle, \\(AI = 2r = 2 \\times {r} = {ans_dist}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_dist} cm."
        elif arch == 7:
            deg, ans_ang = data_7[sub_idx]
            svg = svg_incircle("", f"\\angle A = {deg}^\\circ", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_7[sub_idx].format(deg=deg)
            corr = f"{ans_ang}^\\circ"
            dist = [f"{ans_ang + 15}^\\circ", f"{ans_ang - 15 if ans_ang > 15 else ans_ang + 20}^\\circ", f"{deg}^\\circ"]
            sol = f"**Step 1: Quadrilateral angle sum**\\nIn quadrilateral \\(AFIE\\), \\(\\angle F = \\angle E = 90^\\circ\\).\\n\\(\\angle FIE = 180^\\circ - \\angle A = 180^\\circ - {deg}^\\circ = {ans_ang}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_ang}°."

        diff = "easy" if arch in [0,2,3] else ("medium" if arch in [1,4,5] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

# -----------------------------------------------------------------------------
# 6.3.1: Constructing perpendicular bisectors of sides of triangle
# -----------------------------------------------------------------------------
def gen_6_3_1():
    tc = "MH-9-MTH2-6-6.3.1"
    tname = "Constructing perpendicular bisectors of sides of triangle"
    qs = []
    
    # Arch 0: Right triangle hypotenuse c -> Circumradius R = c / 2
    data_0 = [
        (10, 5), (14, 7), (18, 9), (22, 11), (26, 13),
        (30, 15), (34, 17), (38, 19), (42, 21), (50, 25)
    ]
    tmpls_0 = [
        "In a right-angled triangle with hypotenuse {c}\\text{{ cm}}, find the circumradius \\(R\\).",
        "Calculate the circumradius of a right triangle having hypotenuse of length {c}\\text{{ cm}}.",
        "What is the radius of the circumcircle of a right triangle whose hypotenuse measures {c}\\text{{ cm}}?",
        "Determine the circumradius \\(R = \\frac{{\\text{{hypotenuse}}}}{{2}}\\) for a right triangle with hypotenuse {c}\\text{{ cm}}.",
        "Compute the circumradius \\(R\\) of right-angled \\(\\triangle ABC\\) where hypotenuse \\(AC = {c}\\text{{ cm}}\\).",
        "Evaluate the circumradius of a right triangle having hypotenuse {c}\\text{{ cm}}.",
        "Find the radius of the circumscribed circle of a right triangle with hypotenuse {c}\\text{{ cm}}.",
        "If the hypotenuse of a right-angled triangle is {c}\\text{{ cm}}, calculate circumradius \\(R\\).",
        "What does the circumradius equal for a right triangle having hypotenuse {c}\\text{{ cm}}?",
        "In right triangle \\(\\triangle ABC\\), hypotenuse is {c}\\text{{ cm}}. Find the circumradius."
    ]
    
    # Arch 1: Given circumradius R of right triangle, find hypotenuse = 2 * R
    data_1 = [
        (4, 8), (6, 12), (8, 16), (10, 20), (12, 24),
        (14, 28), (16, 32), (18, 36), (20, 40), (22, 44)
    ]
    tmpls_1 = [
        "The circumradius of a right-angled triangle is {R}\\text{{ cm}}. Find the length of its hypotenuse.",
        "Calculate the hypotenuse of a right triangle whose circumcircle has radius {R}\\text{{ cm}}.",
        "What is the length of the hypotenuse of a right triangle having circumradius \\(R = {R}\\text{{ cm}}\\)?" ,
        "Determine the hypotenuse in right \\(\\triangle ABC\\) if circumradius \\(R = {R}\\text{{ cm}}\\).",
        "Compute the hypotenuse \\(c = 2R\\) of a right triangle given circumradius {R}\\text{{ cm}}.",
        "Evaluate the hypotenuse of a right triangle with circumradius {R}\\text{{ cm}}.",
        "Find the hypotenuse of right triangle with circumradius {R}\\text{{ cm}}.",
        "If circumradius is {R}\\text{{ cm}}, calculate the hypotenuse of the right-angled triangle.",
        "How long is the hypotenuse of a right triangle having circumradius {R}\\text{{ cm}}?",
        "In right-angled \\(\\triangle ABC\\), circumradius is {R}\\text{{ cm}}. Find the hypotenuse."
    ]
    
    # Arch 2: Equilateral triangle with side a -> circumradius R = a / sqrt(3)
    data_2 = [
        ("3\\sqrt{3}", 3), ("6\\sqrt{3}", 6), ("9\\sqrt{3}", 9), ("12\\sqrt{3}", 12), ("15\\sqrt{3}", 15),
        ("18\\sqrt{3}", 18), ("21\\sqrt{3}", 21), ("24\\sqrt{3}", 24), ("27\\sqrt{3}", 27), ("30\\sqrt{3}", 30)
    ]
    tmpls_2 = [
        "In an equilateral triangle of side {a}\\text{{ cm}}, find the circumradius \\(R\\).",
        "Calculate the circumradius of an equilateral triangle with side length {a}\\text{{ cm}}.",
        "What is the radius of the circumcircle of an equilateral triangle having sides {a}\\text{{ cm}}?",
        "Determine circumradius \\(R = \\frac{{a}}{{\\sqrt{{3}}}}\\) for an equilateral triangle of side {a}\\text{{ cm}}.",
        "Compute the circumradius \\(R\\) of equilateral \\(\\triangle ABC\\) with side {a}\\text{{ cm}}.",
        "Evaluate the circumradius of equilateral triangle having side length {a}\\text{{ cm}}.",
        "Find the radius of circumscribed circle of equilateral \\(\\triangle ABC\\) with side {a}\\text{{ cm}}.",
        "If side of equilateral triangle is {a}\\text{{ cm}}, calculate its circumradius.",
        "What is the circumradius of equilateral \\(\\triangle ABC\\) having side {a}\\text{{ cm}}?",
        "In equilateral \\(\\triangle ABC\\), each side measures {a}\\text{{ cm}}. Find circumradius \\(R\\)."
    ]
    
    # Arch 3: Ratio R : r in equilateral triangle = 2
    data_3 = [
        (3, 6), (4, 8), (5, 10), (6, 12), (7, 14),
        (8, 16), (9, 18), (10, 20), (11, 22), (12, 24)
    ]
    tmpls_3 = [
        "In an equilateral triangle, if inradius \\(r = {r}\\text{{ cm}}\\), find its circumradius \\(R\\).",
        "The inradius of an equilateral triangle is {r}\\text{{ cm}}. Calculate its circumradius \\(R\\).",
        "What is the circumradius \\(R\\) of an equilateral triangle having inradius \\(r = {r}\\text{{ cm}}\\)?" ,
        "Compute circumradius \\(R = 2r\\) for an equilateral triangle with inradius {r}\\text{{ cm}}.",
        "Determine the circumradius of an equilateral triangle given that its inradius is {r}\\text{{ cm}}.",
        "Evaluate circumradius \\(R\\) in equilateral \\(\\triangle ABC\\) having inradius {r}\\text{{ cm}}.",
        "Find circumradius \\(R\\) of an equilateral triangle with inradius {r}\\text{{ cm}}.",
        "If inradius of equilateral triangle is {r}\\text{{ cm}}, calculate circumradius \\(R\\).",
        "What does circumradius \\(R\\) equal if inradius is {r}\\text{{ cm}} in equilateral triangle?",
        "In equilateral \\(\\triangle ABC\\), inradius is {r}\\text{{ cm}}. Determine circumradius \\(R\\)."
    ]
    
    # Arch 4: Circumference of circumcircle: C = 2 * pi * R
    data_4 = [
        (5, 10), (7, 14), (9, 18), (11, 22), (13, 26),
        (15, 30), (17, 34), (19, 38), (21, 42), (25, 50)
    ]
    tmpls_4 = [
        "If the circumradius of a triangle is {R}\\text{{ cm}}, find the circumference of its circumcircle in terms of \\(\\pi\\).",
        "Calculate the circumference of the circumcircle of a triangle with circumradius \\(R = {R}\\text{{ cm}}\\).",
        "What is the circumference of the circumcircle of radius {R}\\text{{ cm}} in terms of \\(\\pi\\)?",
        "Compute the circumference of the circumcircle for a triangle having circumradius {R}\\text{{ cm}}.",
        "Determine the perimeter of the circumcircle with radius {R}\\text{{ cm}} in terms of \\(\\pi\\).",
        "Evaluate circumference \\(2\\pi R\\) for circumcircle with radius {R}\\text{{ cm}}.",
        "Find the circumference of circumcircle of radius {R}\\text{{ cm}} in terms of \\(\\pi\\).",
        "Calculate circumference of circumcircle having radius {R}\\text{{ cm}}.",
        "If circumradius is {R}\\text{{ cm}}, what is the circumference of the circumcircle?",
        "In a triangle, circumradius is {R}\\text{{ cm}}. Find the circumference of the circumcircle."
    ]
    
    # Arch 5: Area of circumcircle: A = pi * R^2
    data_5 = [
        (2, 4), (3, 9), (4, 16), (5, 25), (6, 36),
        (7, 49), (8, 64), (9, 81), (10, 100), (12, 144)
    ]
    tmpls_5 = [
        "If the circumradius of a triangle is {R}\\text{{ cm}}, find the area of its circumcircle in terms of \\(\\pi\\).",
        "Calculate the area of the circumcircle of a triangle with circumradius \\(R = {R}\\text{{ cm}}\\).",
        "What is the area of the circumcircle of radius {R}\\text{{ cm}} in terms of \\(\\pi\\)?",
        "Compute the area of the circumcircle for a triangle having circumradius {R}\\text{{ cm}}.",
        "Determine the area of the circumcircle with radius {R}\\text{{ cm}} in terms of \\(\\pi\\).",
        "Evaluate area \\(\\pi R^2\\) for circumcircle with radius {R}\\text{{ cm}}.",
        "Find the area of circumcircle of radius {R}\\text{{ cm}} in terms of \\(\\pi\\).",
        "Calculate area of circumcircle having radius {R}\\text{{ cm}}.",
        "If circumradius is {R}\\text{{ cm}}, what is the area of the circumcircle in terms of \\(\\pi\\)?",
        "In a triangle, circumradius is {R}\\text{{ cm}}. Find the area of the circumcircle."
    ]
    
    # Arch 6: Equidistant property of circumcentre from vertices
    data_6 = [
        ("A", "B", 7), ("B", "C", 9), ("C", "A", 11), ("A", "C", 13), ("B", "A", 15),
        ("vertex A", "vertex B", 17), ("vertex B", "vertex C", 19), ("vertex C", "vertex A", 21), ("vertex A", "vertex C", 23), ("vertex B", "vertex A", 25)
    ]
    tmpls_6 = [
        "The circumcentre \\(C\\) of \\(\\triangle ABC\\) is at distance {d}\\text{{ cm}} from {v1}. What is its distance from {v2}?",
        "In \\(\\triangle ABC\\), circumcentre \\(C\\) is at distance {d}\\text{{ cm}} from {v1}. Calculate distance to {v2}.",
        "Circumcentre of a triangle is equidistant from all three vertices. If distance to {v1} is {d}\\text{{ cm}}, find distance to {v2}.",
        "What is the distance from circumcentre \\(C\\) to {v2} if its distance to {v1} is {d}\\text{{ cm}}?",
        "Determine the distance from circumcentre \\(C\\) to {v2} given that distance to {v1} is {d}\\text{{ cm}}.",
        "Evaluate the distance from circumcentre of a triangle to {v2} knowing distance to {v1} is {d}\\text{{ cm}}.",
        "Find the distance from circumcentre to {v2} when distance to {v1} is {d}\\text{{ cm}}.",
        "Compute the distance from circumcentre \\(C\\) to {v2} if distance to {v1} is {d}\\text{{ cm}}.",
        "If circumcentre is at distance {d}\\text{{ cm}} from {v1}, what is its distance from {v2}?",
        "In \\(\\triangle ABC\\), distance from circumcentre to {v1} is {d}\\text{{ cm}}. Find distance to {v2}."
    ]
    
    # Arch 7: Median to hypotenuse in right triangle = R = hyp / 2
    data_7 = [
        (12, 6), (16, 8), (20, 10), (24, 12), (28, 14),
        (32, 16), (36, 18), (40, 20), (44, 22), (48, 24)
    ]
    tmpls_7 = [
        "In a right-angled triangle with hypotenuse {hyp}\\text{{ cm}}, find the length of the median drawn to the hypotenuse.",
        "Calculate the length of the median to hypotenuse in a right triangle having hypotenuse {hyp}\\text{{ cm}}.",
        "What is the length of the median to the hypotenuse of a right triangle with hypotenuse {hyp}\\text{{ cm}}?",
        "Determine the length of median to hypotenuse in right \\(\\triangle ABC\\) where hypotenuse \\(AC = {hyp}\\text{{ cm}}\\).",
        "Compute the median to hypotenuse \\(BD = \\frac{{AC}}{{2}}\\) in right triangle with hypotenuse {hyp}\\text{{ cm}}.",
        "Evaluate the median to hypotenuse for a right-angled triangle having hypotenuse {hyp}\\text{{ cm}}.",
        "Find the length of median to hypotenuse of right triangle with hypotenuse {hyp}\\text{{ cm}}.",
        "If hypotenuse of a right triangle is {hyp}\\text{{ cm}}, calculate the length of the median to hypotenuse.",
        "How long is the median to the hypotenuse in a right-angled triangle of hypotenuse {hyp}\\text{{ cm}}?",
        "In right triangle \\(\\triangle ABC\\), hypotenuse is {hyp}\\text{{ cm}}. Find the median to hypotenuse."
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        qcode = f"{tc}-OSC-{seq}"
        
        if arch == 0:
            c, ans_r = data_0[sub_idx]
            svg = svg_circumcircle(f"R = {ans_r}", "", "", f"hyp = {c}") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(c=c)
            corr = f"{ans_r}\\text{{ cm}}"
            dist = [f"{ans_r + 2}\\text{{ cm}}", f"{ans_r - 2 if ans_r > 2 else ans_r + 3}\\text{{ cm}}", f"{c}\\text{{ cm}}"]
            sol = f"**Step 1: Circumradius of right triangle**\\nIn a right-angled triangle, the circumcentre lies at the midpoint of the hypotenuse.\\n\\(R = \\frac{{\\text{{hypotenuse}}}}{{2}} = \\frac{{{c}}}{{2}} = {ans_r}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_r} cm."
        elif arch == 1:
            R, ans_hyp = data_1[sub_idx]
            svg = svg_circumcircle(f"R = {R}", "", "", "hyp = ?") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(R=R)
            corr = f"{ans_hyp}\\text{{ cm}}"
            dist = [f"{ans_hyp + 4}\\text{{ cm}}", f"{ans_hyp - 4}\\text{{ cm}}", f"{R}\\text{{ cm}}"]
            sol = f"**Step 1: Hypotenuse formula**\\n\\(\\text{{hypotenuse}} = 2 \\times R = 2 \\times {R} = {ans_hyp}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_hyp} cm."
        elif arch == 2:
            a, ans_r = data_2[sub_idx]
            svg = svg_circumcircle(f"R = {ans_r}", f"side = {a}", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(a=a)
            corr = f"{ans_r}\\text{{ cm}}"
            dist = [f"{ans_r + 3}\\text{{ cm}}", f"{ans_r - 3 if ans_r > 3 else ans_r + 4}\\text{{ cm}}", f"{ans_r * 2}\\text{{ cm}}"]
            sol = f"**Step 1: Formula**\\n\\(R = \\frac{{a}}{{\\sqrt{{3}}}} = \\frac{{{a}}}{{\\sqrt{{3}}}} = {ans_r}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_r} cm."
        elif arch == 3:
            r, ans_r = data_3[sub_idx]
            svg = svg_circumcircle(f"R = {ans_r}", "", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(r=r)
            corr = f"{ans_r}\\text{{ cm}}"
            dist = [f"{ans_r + 2}\\text{{ cm}}", f"{ans_r - 2}\\text{{ cm}}", f"{r}\\text{{ cm}}"]
            sol = f"**Step 1: Ratio of R to r**\\nIn an equilateral triangle, \\(R = 2r = 2 \\times {r} = {ans_r}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_r} cm."
        elif arch == 4:
            R, ans_coef = data_4[sub_idx]
            svg = svg_circumcircle(f"R = {R}", "", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(R=R)
            corr = f"{ans_coef}\\pi\\text{{ cm}}"
            dist = [f"{ans_coef + 4}\\pi\\text{{ cm}}", f"{ans_coef - 4}\\pi\\text{{ cm}}", f"{R * R}\\pi\\text{{ cm}}"]
            sol = f"**Step 1: Circumference of circumcircle**\\n\\(\\text{{Circumference}} = 2\\pi R = 2\\pi \\times {R} = {ans_coef}\\pi\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_coef}π cm."
        elif arch == 5:
            R, ans_coef = data_5[sub_idx]
            svg = svg_circumcircle(f"R = {R}", "", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(R=R)
            corr = f"{ans_coef}\\pi\\text{{ cm}}^2"
            dist = [f"{ans_coef + 10}\\pi\\text{{ cm}}^2", f"{ans_coef - 10 if ans_coef > 10 else ans_coef + 15}\\pi\\text{{ cm}}^2", f"{2 * R}\\pi\\text{{ cm}}^2"]
            sol = f"**Step 1: Area of circumcircle**\\n\\(\\text{{Area}} = \\pi R^2 = \\pi \\times {R}^2 = {ans_coef}\\pi\\text{{ cm}}^2\\).\\n**Step 2: Conclusion**\\n{ans_coef}π cm²."
        elif arch == 6:
            v1, v2, ans_d = data_6[sub_idx]
            svg = svg_circumcircle(f"R = {ans_d}", "", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(v1=v1, v2=v2, d=ans_d)
            corr = f"{ans_d}\\text{{ cm}}"
            dist = [f"{ans_d + 3}\\text{{ cm}}", f"{ans_d - 3 if ans_d > 3 else ans_d + 4}\\text{{ cm}}", f"{ans_d * 2}\\text{{ cm}}"]
            sol = f"**Step 1: Equidistant property**\\nThe circumcentre is equidistant from all three vertices of the triangle.\\nHence, distance to {v2} is also {ans_d}\\text{{ cm}}.\\n**Step 2: Conclusion**\\n{ans_d} cm."
        elif arch == 7:
            hyp, ans_med = data_7[sub_idx]
            svg = svg_circumcircle("", "", "", f"hyp = {hyp}") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_7[sub_idx].format(hyp=hyp)
            corr = f"{ans_med}\\text{{ cm}}"
            dist = [f"{ans_med + 2}\\text{{ cm}}", f"{ans_med - 2}\\text{{ cm}}", f"{hyp}\\text{{ cm}}"]
            sol = f"**Step 1: Median theorem**\\nIn a right-angled triangle, length of median to hypotenuse is half of the hypotenuse.\\n\\(\\text{{Median}} = \\frac{{{hyp}}}{{2}} = {ans_med}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_med} cm."

        diff = "easy" if arch in [0,1,7] else ("medium" if arch in [2,3,6] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

# -----------------------------------------------------------------------------
# 6.3.2: Circumcentre location in acute, right, and obtuse triangles
# -----------------------------------------------------------------------------
def gen_6_3_2():
    tc = "MH-9-MTH2-6-6.3.2"
    tname = "Circumcentre (C) location in acute, right, and obtuse triangles"
    qs = []
    
    # Arch 0: Central angle BOC = 2 * A
    data_0 = [
        (35, 70), (45, 90), (55, 110), (65, 130), (75, 150),
        (30, 60), (40, 80), (50, 100), (60, 120), (70, 140)
    ]
    tmpls_0 = [
        "In \\(\\triangle ABC\\), point \\(O\\) is the circumcentre. If \\(\\angle A = {A}^\\circ\\), find central angle \\(\\angle BOC\\).",
        "The angle subtended by side \\(BC\\) at the circumcentre \\(O\\) of \\(\\triangle ABC\\) is \\(\\angle BOC\\). If \\(\\angle BAC = {A}^\\circ\\), calculate \\(\\angle BOC\\).",
        "What is the measure of angle \\(\\angle BOC\\) formed at circumcentre \\(O\\) if \\(\\angle A = {A}^\\circ\\)?",
        "Calculate central angle \\(\\angle BOC = 2\\angle A\\) in \\(\\triangle ABC\\) given circumcentre \\(O\\) and \\(\\angle A = {A}^\\circ\\).",
        "Determine the angle \\(\\angle BOC\\) in \\(\\triangle ABC\\) with circumcentre \\(O\\) where \\(\\angle A = {A}^\\circ\\).",
        "Evaluate \\(\\angle BOC\\) for circumcentre \\(O\\) of \\(\\triangle ABC\\) with \\(\\angle A = {A}^\\circ\\).",
        "If \\(O\\) is the circumcentre of \\(\\triangle ABC\\) and \\(\\angle A = {A}^\\circ\\), what is \\(\\angle BOC\\)?",
        "Find \\(\\angle BOC\\) in \\(\\triangle ABC\\) knowing \\(O\\) is the circumcentre and \\(\\angle A = {A}^\\circ\\).",
        "Compute the measure of \\(\\angle BOC\\) subtended at circumcentre \\(O\\) by chord \\(BC\\) when \\(\\angle A = {A}^\\circ\\).",
        "In \\(\\triangle ABC\\), circumcentre is \\(O\\). Calculate \\(\\angle BOC\\) if \\(\\angle A = {A}^\\circ\\)."
    ]
    
    # Arch 1: Angle A from central angle BOC: A = BOC / 2
    data_1 = [
        (64, 32), (72, 36), (84, 42), (96, 48), (108, 54),
        (116, 58), (124, 62), (132, 66), (144, 72), (156, 78)
    ]
    tmpls_1 = [
        "In \\(\\triangle ABC\\), \\(O\\) is the circumcentre. If \\(\\angle BOC = {boc}^\\circ\\), find \\(\\angle A\\).",
        "If central angle \\(\\angle BOC = {boc}^\\circ\\) at circumcentre \\(O\\) of \\(\\triangle ABC\\), calculate \\(\\angle BAC\\).",
        "What is the measure of \\(\\angle A\\) in \\(\\triangle ABC\\) if \\(\\angle BOC = {boc}^\\circ\\) at circumcentre \\(O\\)?",
        "Determine \\(\\angle A\\) in \\(\\triangle ABC\\) given circumcentre \\(O\\) and \\(\\angle BOC = {boc}^\\circ\\).",
        "Calculate vertex angle \\(\\angle A\\) knowing angle subtended at circumcentre is \\(\\angle BOC = {boc}^\\circ\\).",
        "Evaluate \\(\\angle A\\) in \\(\\triangle ABC\\) having circumcentre \\(O\\) and \\(\\angle BOC = {boc}^\\circ\\).",
        "Find \\(\\angle A\\) for \\(\\triangle ABC\\) where circumcentre is \\(O\\) and \\(\\angle BOC = {boc}^\\circ\\).",
        "Compute \\(\\angle A\\) given circumcentre \\(O\\) and \\(\\angle BOC = {boc}^\\circ\\).",
        "If \\(\\angle BOC = {boc}^\\circ\\) in \\(\\triangle ABC\\) with circumcentre \\(O\\), what is \\(\\angle A\\)?",
        "In \\(\\triangle ABC\\) with circumcentre \\(O\\), determine \\(\\angle A\\) when \\(\\angle BOC = {boc}^\\circ\\)."
    ]
    
    # Arch 2: Base angle in isosceles triangle OBC: angle OBC = 90 - A
    data_2 = [
        (35, 55), (45, 45), (55, 35), (65, 25), (75, 15),
        (38, 52), (48, 42), (58, 32), (68, 22), (78, 12)
    ]
    tmpls_2 = [
        "In acute-angled \\(\\triangle ABC\\), \\(O\\) is the circumcentre. If \\(\\angle A = {A}^\\circ\\), find \\(\\angle OBC\\).",
        "For circumcentre \\(O\\) of acute \\(\\triangle ABC\\), calculate base angle \\(\\angle OBC\\) of \\(\\triangle OBC\\) when \\(\\angle A = {A}^\\circ\\).",
        "What is \\(\\angle OBC\\) in \\(\\triangle ABC\\) if \\(O\\) is the circumcentre and \\(\\angle A = {A}^\\circ\\)?",
        "Determine \\(\\angle OBC = 90^\\circ - \\angle A\\) in acute \\(\\triangle ABC\\) with circumcentre \\(O\\) and \\(\\angle A = {A}^\\circ\\).",
        "Compute \\(\\angle OBC\\) in \\(\\triangle ABC\\) where \\(O\\) is the circumcentre and \\(\\angle BAC = {A}^\\circ\\).",
        "Evaluate \\(\\angle OBC\\) in isosceles \\(\\triangle OBC\\) (\\(OB = OC = R\\)) when \\(\\angle A = {A}^\\circ\\).",
        "Find \\(\\angle OBC\\) for circumcentre \\(O\\) in acute \\(\\triangle ABC\\) having \\(\\angle A = {A}^\\circ\\).",
        "Calculate the measure of \\(\\angle OBC\\) given \\(O\\) is the circumcentre of acute \\(\\triangle ABC\\) and \\(\\angle A = {A}^\\circ\\).",
        "If \\(O\\) is circumcentre of acute \\(\\triangle ABC\\) and \\(\\angle A = {A}^\\circ\\), what is \\(\\angle OBC\\)?",
        "In acute \\(\\triangle ABC\\) with circumcentre \\(O\\), find \\(\\angle OBC\\) if \\(\\angle A = {A}^\\circ\\)."
    ]
    
    # Arch 3: Central angle AOC = 2 * B
    data_3 = [
        (32, 64), (42, 84), (52, 104), (62, 124), (72, 144),
        (36, 72), (46, 92), (56, 112), (66, 132), (76, 152)
    ]
    tmpls_3 = [
        "In \\(\\triangle ABC\\), point \\(O\\) is the circumcentre. If \\(\\angle B = {B}^\\circ\\), find \\(\\angle AOC\\).",
        "The angle subtended by side \\(AC\\) at circumcentre \\(O\\) is \\(\\angle AOC\\). If \\(\\angle ABC = {B}^\\circ\\), calculate \\(\\angle AOC\\).",
        "What is the measure of angle \\(\\angle AOC\\) formed at circumcentre \\(O\\) when \\(\\angle B = {B}^\\circ\\)?",
        "Calculate central angle \\(\\angle AOC = 2\\angle B\\) in \\(\\triangle ABC\\) given circumcentre \\(O\\) and \\(\\angle B = {B}^\\circ\\).",
        "Determine \\(\\angle AOC\\) in \\(\\triangle ABC\\) with circumcentre \\(O\\) where \\(\\angle B = {B}^\\circ\\).",
        "Evaluate \\(\\angle AOC\\) for circumcentre \\(O\\) of \\(\\triangle ABC\\) with \\(\\angle B = {B}^\\circ\\).",
        "If \\(O\\) is the circumcentre of \\(\\triangle ABC\\) and \\(\\angle B = {B}^\\circ\\), what is \\(\\angle AOC\\)?",
        "Find \\(\\angle AOC\\) in \\(\\triangle ABC\\) knowing \\(O\\) is the circumcentre and \\(\\angle B = {B}^\\circ\\).",
        "Compute the measure of \\(\\angle AOC\\) subtended at circumcentre \\(O\\) by side \\(AC\\) when \\(\\angle B = {B}^\\circ\\).",
        "In \\(\\triangle ABC\\), circumcentre is \\(O\\). Calculate \\(\\angle AOC\\) if \\(\\angle B = {B}^\\circ\\)."
    ]
    
    # Arch 4: Central angle AOB = 2 * C
    data_4 = [
        (34, 68), (44, 88), (54, 108), (64, 128), (74, 148),
        (38, 76), (48, 96), (58, 116), (68, 136), (78, 156)
    ]
    tmpls_4 = [
        "In \\(\\triangle ABC\\), \\(O\\) is the circumcentre. If \\(\\angle C = {C}^\\circ\\), find \\(\\angle AOB\\).",
        "For circumcentre \\(O\\) of \\(\\triangle ABC\\), calculate \\(\\angle AOB\\) when \\(\\angle C = {C}^\\circ\\).",
        "What is the measure of angle \\(\\angle AOB\\) subtended at circumcentre \\(O\\) if \\(\\angle C = {C}^\\circ\\)?",
        "Calculate central angle \\(\\angle AOB = 2\\angle C\\) in \\(\\triangle ABC\\) given circumcentre \\(O\\) and \\(\\angle C = {C}^\\circ\\).",
        "Determine the angle \\(\\angle AOB\\) in \\(\\triangle ABC\\) where \\(O\\) is the circumcentre and \\(\\angle C = {C}^\\circ\\).",
        "Evaluate \\(\\angle AOB\\) for \\(\\triangle ABC\\) with circumcentre \\(O\\) having \\(\\angle C = {C}^\\circ\\).",
        "Find \\(\\angle AOB\\) in \\(\\triangle ABC\\) given circumcentre \\(O\\) and \\(\\angle C = {C}^\\circ\\).",
        "Calculate \\(\\angle AOB\\) subtended at circumcentre \\(O\\) when \\(\\angle C = {C}^\\circ\\).",
        "If \\(O\\) is the circumcentre of \\(\\triangle ABC\\) and \\(\\angle C = {C}^\\circ\\), what is \\(\\angle AOB\\)?",
        "In \\(\\triangle ABC\\), circumcentre is \\(O\\). Determine \\(\\angle AOB\\) if \\(\\angle C = {C}^\\circ\\)."
    ]
    
    # Arch 5: Base angle OAC = 90 - B
    data_5 = [
        (31, 59), (41, 49), (51, 39), (61, 29), (71, 19),
        (37, 53), (47, 43), (57, 33), (67, 23), (77, 13)
    ]
    tmpls_5 = [
        "In acute-angled \\(\\triangle ABC\\) with circumcentre \\(O\\), if \\(\\angle B = {B}^\\circ\\), find \\(\\angle OAC\\).",
        "For circumcentre \\(O\\) of acute \\(\\triangle ABC\\), calculate \\(\\angle OAC\\) when \\(\\angle B = {B}^\\circ\\).",
        "What is \\(\\angle OAC\\) in \\(\\triangle ABC\\) if \\(O\\) is the circumcentre and \\(\\angle B = {B}^\\circ\\)?",
        "Determine \\(\\angle OAC = 90^\\circ - \\angle B\\) in acute \\(\\triangle ABC\\) with circumcentre \\(O\\) and \\(\\angle B = {B}^\\circ\\).",
        "Compute \\(\\angle OAC\\) in \\(\\triangle ABC\\) where \\(O\\) is the circumcentre and \\(\\angle ABC = {B}^\\circ\\).",
        "Evaluate \\(\\angle OAC\\) in isosceles \\(\\triangle OAC\\) (\\(OA = OC = R\\)) when \\(\\angle B = {B}^\\circ\\).",
        "Find \\(\\angle OAC\\) for circumcentre \\(O\\) in acute \\(\\triangle ABC\\) having \\(\\angle B = {B}^\\circ\\).",
        "Calculate the measure of \\(\\angle OAC\\) given \\(O\\) is the circumcentre of acute \\(\\triangle ABC\\) and \\(\\angle B = {B}^\\circ\\).",
        "If \\(O\\) is circumcentre of acute \\(\\triangle ABC\\) and \\(\\angle B = {B}^\\circ\\), what is \\(\\angle OAC\\)?",
        "In acute \\(\\triangle ABC\\) with circumcentre \\(O\\), find \\(\\angle OAC\\) if \\(\\angle B = {B}^\\circ\\)."
    ]
    
    # Arch 6: Location classification: acute -> inside, right -> on hypotenuse, obtuse -> outside
    data_6 = [
        ("40, 60, 80", "Inside the triangle (Interior)"),
        ("30, 60, 90", "On the hypotenuse (Midpoint of hypotenuse)"),
        ("20, 50, 110", "Outside the triangle (Exterior)"),
        ("50, 60, 70", "Inside the triangle (Interior)"),
        ("45, 45, 90", "On the hypotenuse (Midpoint of hypotenuse)"),
        ("25, 35, 120", "Outside the triangle (Exterior)"),
        ("55, 60, 65", "Inside the triangle (Interior)"),
        ("35, 55, 90", "On the hypotenuse (Midpoint of hypotenuse)"),
        ("15, 30, 135", "Outside the triangle (Exterior)"),
        ("48, 52, 80", "Inside the triangle (Interior)")
    ]
    tmpls_6 = [
        "In a triangle whose angles are {angles}^\circ, where is the circumcentre located?",
        "A triangle has angle measures {angles}^\circ. Determine the position of its circumcentre.",
        "What is the location of the circumcentre of a triangle with angles {angles}^\circ?",
        "Where does the circumcentre lie for a triangle having angles {angles}^\circ?",
        "Find the position of the circumcentre of a triangle with angles {angles}^\circ relative to the triangle.",
        "For a triangle with angle measures {angles}^\circ, identify where its circumcentre is located.",
        "In geometry, where is the circumcentre situated for a triangle having angles {angles}^\circ?",
        "Determine whether the circumcentre lies inside, on, or outside the triangle with angles {angles}^\circ.",
        "If the three angles of a triangle are {angles}^\circ, what is the location of its circumcentre?",
        "Evaluate the position of the circumcentre for a triangle with angle measures {angles}^\circ."
    ]
    
    # Arch 7: Base angle OAB = 90 - C
    data_7 = [
        (33, 57), (43, 47), (53, 37), (63, 27), (73, 17),
        (39, 51), (49, 41), (59, 31), (69, 21), (79, 11)
    ]
    tmpls_7 = [
        "In acute-angled \\(\\triangle ABC\\) with circumcentre \\(O\\), if \\(\\angle C = {C}^\\circ\\), find \\(\\angle OAB\\).",
        "For circumcentre \\(O\\) of acute \\(\\triangle ABC\\), calculate \\(\\angle OAB\\) when \\(\\angle C = {C}^\\circ\\).",
        "What is \\(\\angle OAB\\) in \\(\\triangle ABC\\) if \\(O\\) is the circumcentre and \\(\\angle C = {C}^\\circ\\)?",
        "Determine \\(\\angle OAB = 90^\\circ - \\angle C\\) in acute \\(\\triangle ABC\\) with circumcentre \\(O\\) and \\(\\angle C = {C}^\\circ\\).",
        "Compute \\(\\angle OAB\\) in \\(\\triangle ABC\\) where \\(O\\) is the circumcentre and \\(\\angle C = {C}^\\circ\\).",
        "Evaluate \\(\\angle OAB\\) in isosceles \\(\\triangle OAB\\) (\\(OA = OB = R\\)) when \\(\\angle C = {C}^\\circ\\).",
        "Find \\(\\angle OAB\\) for circumcentre \\(O\\) in acute \\(\\triangle ABC\\) having \\(\\angle C = {C}^\\circ\\).",
        "Calculate the measure of \\(\\angle OAB\\) given \\(O\\) is the circumcentre of acute \\(\\triangle ABC\\) and \\(\\angle C = {C}^\\circ\\).",
        "If \\(O\\) is circumcentre of acute \\(\\triangle ABC\\) and \\(\\angle C = {C}^\\circ\\), what is \\(\\angle OAB\\)?",
        "In acute \\(\\triangle ABC\\) with circumcentre \\(O\\), find \\(\\angle OAB\\) if \\(\\angle C = {C}^\\circ\\)."
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        qcode = f"{tc}-OSC-{seq}"
        
        if arch == 0:
            A, ans_boc = data_0[sub_idx]
            svg = svg_circumcircle("", f"\\angle A = {A}^\\circ", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(A=A)
            corr = f"{ans_boc}^\\circ"
            dist = [f"{ans_boc + 15}^\\circ", f"{ans_boc - 15 if ans_boc > 15 else ans_boc + 20}^\\circ", f"{180 - A}^\\circ"]
            sol = f"**Step 1: Circumcentre angle theorem**\\nThe angle subtended by an arc at the centre is double the angle subtended by it at any point on the circle.\\n\\(\\angle BOC = 2\\angle A = 2 \\times {A}^\\circ = {ans_boc}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_boc}°."
        elif arch == 1:
            boc, ans_a = data_1[sub_idx]
            svg = svg_circumcircle("", "", "", f"\\angle BOC = {boc}^\\circ") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(boc=boc)
            corr = f"{ans_a}^\\circ"
            dist = [f"{ans_a + 8}^\\circ", f"{ans_a - 8 if ans_a > 8 else ans_a + 12}^\\circ", f"{180 - ans_a}^\\circ"]
            sol = f"**Step 1: Inverting formula**\\n\\(\\angle A = \\frac{{\\angle BOC}}{{2}} = \\frac{{{boc}^\\circ}}{{2}} = {ans_a}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_a}°."
        elif arch == 2:
            A, ans_obc = data_2[sub_idx]
            svg = svg_circumcircle("", f"\\angle A = {A}^\\circ", "\\angle OBC = ?", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(A=A)
            corr = f"{ans_obc}^\\circ"
            dist = [f"{ans_obc + 10}^\\circ", f"{ans_obc - 10 if ans_obc > 10 else ans_obc + 15}^\\circ", f"{A}^\\circ"]
            sol = f"**Step 1: Isosceles triangle OBC**\\n\\(\\angle BOC = 2\\angle A = 2 \\times {A}^\\circ = {2*A}^\\circ\\).\\nSince \\(OB = OC = R\\), \\(\\angle OBC = \\angle OCB = \\frac{{180^\\circ - {2*A}^\\circ}}{{2}} = 90^\\circ - {A}^\\circ = {ans_obc}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_obc}°."
        elif arch == 3:
            B, ans_aoc = data_3[sub_idx]
            svg = svg_circumcircle("", "", f"\\angle B = {B}^\\circ", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(B=B)
            corr = f"{ans_aoc}^\\circ"
            dist = [f"{ans_aoc + 15}^\\circ", f"{ans_aoc - 15 if ans_aoc > 15 else ans_aoc + 20}^\\circ", f"{180 - B}^\\circ"]
            sol = f"**Step 1: Formula**\\n\\(\\angle AOC = 2\\angle B = 2 \\times {B}^\\circ = {ans_aoc}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_aoc}°."
        elif arch == 4:
            C, ans_aob = data_4[sub_idx]
            svg = svg_circumcircle("", "", "", f"\\angle C = {C}^\\circ") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(C=C)
            corr = f"{ans_aob}^\\circ"
            dist = [f"{ans_aob + 15}^\\circ", f"{ans_aob - 15 if ans_aob > 15 else ans_aob + 20}^\\circ", f"{180 - C}^\\circ"]
            sol = f"**Step 1: Formula**\\n\\(\\angle AOB = 2\\angle C = 2 \\times {C}^\\circ = {ans_aob}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_aob}°."
        elif arch == 5:
            B, ans_oac = data_5[sub_idx]
            svg = svg_circumcircle("", "", f"\\angle B = {B}^\\circ", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(B=B)
            corr = f"{ans_oac}^\\circ"
            dist = [f"{ans_oac + 10}^\\circ", f"{ans_oac - 10 if ans_oac > 10 else ans_oac + 15}^\\circ", f"{B}^\\circ"]
            sol = f"**Step 1: Formula**\\n\\(\\angle OAC = 90^\\circ - \\angle B = 90^\\circ - {B}^\\circ = {ans_oac}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_oac}°."
        elif arch == 6:
            angles, ans_pos = data_6[sub_idx]
            svg = svg_circumcircle("", "", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(angles=angles)
            corr = ans_pos
            opts_pool = ["Inside the triangle (Interior)", "On the hypotenuse (Midpoint of hypotenuse)", "Outside the triangle (Exterior)", "At vertex B"]
            dist = [p for p in opts_pool if p != ans_pos][:3]
            sol = f"**Step 1: Circumcentre location theorem**\\n- Acute triangle: Circumcentre lies inside the triangle.\\n- Right triangle: Circumcentre lies on the midpoint of the hypotenuse.\\n- Obtuse triangle: Circumcentre lies outside the triangle.\\nFor angles {angles}°, the circumcentre is located: {ans_pos}.\\n**Step 2: Conclusion**\\n{ans_pos}."
        elif arch == 7:
            C, ans_oab = data_7[sub_idx]
            svg = svg_circumcircle("", "", "", f"\\angle C = {C}^\\circ") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_7[sub_idx].format(C=C)
            corr = f"{ans_oab}^\\circ"
            dist = [f"{ans_oab + 10}^\\circ", f"{ans_oab - 10 if ans_oab > 10 else ans_oab + 15}^\\circ", f"{C}^\\circ"]
            sol = f"**Step 1: Formula**\\n\\(\\angle OAB = 90^\\circ - \\angle C = 90^\\circ - {C}^\\circ = {ans_oab}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_oab}°."

        diff = "easy" if arch in [0,3,4] else ("medium" if arch in [1,2,5] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs
'''

with open("scripts/generate_flawless_ch6.py", "r", encoding="utf-8") as f:
    orig = f.read()

# Insert before def main():
idx = orig.find("def main():")
new_content = orig[:idx] + code_final + "\n" + orig[idx:]

# Update main
main_code = '''def main():
    qs = []
    print("Generating Chapter 6: Subtopic 6.1.1...")
    q1 = gen_6_1_1()
    print(f"Generated 6.1.1: {len(q1)} questions")
    qs.extend(q1)
    print("Generating 6.1.2...")
    q2 = gen_6_1_2()
    print(f"Generated 6.1.2: {len(q2)} questions")
    qs.extend(q2)
    print("Generating 6.2.1...")
    q3 = gen_6_2_1()
    print(f"Generated 6.2.1: {len(q3)} questions")
    qs.extend(q3)
    print("Generating 6.2.2...")
    q4 = gen_6_2_2()
    print(f"Generated 6.2.2: {len(q4)} questions")
    qs.extend(q4)
    print("Generating 6.3.1...")
    q5 = gen_6_3_1()
    print(f"Generated 6.3.1: {len(q5)} questions")
    qs.extend(q5)
    print("Generating 6.3.2...")
    q6 = gen_6_3_2()
    print(f"Generated 6.3.2: {len(q6)} questions")
    qs.extend(q6)

    with open("scripts/mh9_mth2_ch6_perfect.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print("Saved all 480 questions to scripts/mh9_mth2_ch6_perfect.json!")
'''

new_content = re.sub(r'def main\(\):[\s\S]*', main_code, new_content)

with open("scripts/generate_flawless_ch6.py", "w", encoding="utf-8") as f:
    f.write(new_content)
print("Complete Chapter 6 generator updated!")
