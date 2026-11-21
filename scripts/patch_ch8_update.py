# scripts/patch_ch8_update.py
with open('scripts/generate_mh9_mth2_ch8_all.py', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('def gen_8_2_2():')
base = c[:pos]

fixed_code = '''def gen_8_2_2():
    tc = "MH-9-MTH2-8-8.2.2"
    tname = "sin θ = cos (90-θ) and cos θ = sin (90-θ)"
    qs = []
    
    data_0 = [(12,78), (18,72), (24,66), (32,58), (38,52), (44,46), (52,38), (64,26), (72,18), (78,12)]
    data_1 = [(14,76), (22,68), (28,62), (36,54), (42,48), (48,42), (56,34), (62,28), (74,16), (82,8)]
    data_2 = [(10,2), (20,3), (30,4), (40,5), (50,6), (60,7), (70,9), (80,11), (15,13), (25,15)]
    data_3 = [(11,21), (21,23), (31,27), (41,29), (51,31), (61,33), (71,35), (81,37), (33,39), (43,41)]
    data_4 = [
        (4, 18, "\\\\sin(4\\\\theta) = \\\\cos(\\\\theta)"),
        (5, 15, "\\\\sin(5\\\\theta) = \\\\cos(\\\\theta)"),
        (2, 30, "\\\\sin(2\\\\theta) = \\\\cos(\\\\theta)"),
        (10, 40, "\\\\sin(\\\\theta + 10^\\\\circ) = \\\\cos(\\\\theta)"),
        (20, 35, "\\\\sin(\\\\theta + 20^\\\\circ) = \\\\cos(\\\\theta)"),
        (40, 25, "\\\\sin(\\\\theta + 40^\\\\circ) = \\\\cos(\\\\theta)"),
        (50, 20, "\\\\sin(\\\\theta + 50^\\\\circ) = \\\\cos(\\\\theta)"),
        (14, 38, "\\\\sin(\\\\theta + 14^\\\\circ) = \\\\cos(\\\\theta)"),
        (46, 22, "\\\\sin(\\\\theta + 46^\\\\circ) = \\\\cos(\\\\theta)"),
        (70, 10, "\\\\sin(\\\\theta + 70^\\\\circ) = \\\\cos(\\\\theta)")
    ]
    data_5 = [
        (10,"\\\\frac{2}{5}"), (20,"\\\\frac{3}{7}"), (30,"\\\\frac{4}{9}"), (40,"\\\\frac{5}{11}"), (50,"\\\\frac{6}{13}"),
        (60,"\\\\frac{7}{15}"), (70,"\\\\frac{8}{17}"), (80,"\\\\frac{9}{19}"), (15,"\\\\frac{1}{3}"), (25,"\\\\frac{5}{8}")
    ]
    data_6 = [
        (12,78, "In right-angled \\\\(\\\\triangle ABC\\\\) with \\\\(\\\\angle B = 90^\\\\circ\\\\) and \\\\(\\\\angle C = 12^\\\\circ\\\\), \\\\(\\\\cos C\\\\) equals which ratio of angle \\\\(A\\\\)?"),
        (22,68, "For right \\\\(\\\\triangle ABC\\\\) with \\\\(\\\\angle B = 90^\\\\circ\\\\), if \\\\(\\\\angle C = 22^\\\\circ\\\\), express \\\\(\\\\cos C\\\\) in terms of angle \\\\(A\\\\)."),
        (32,58, "If \\\\(\\\\angle C = 32^\\\\circ\\\\) in right \\\\(\\\\triangle ABC\\\\) (\\\\(\\\\angle B = 90^\\\\circ\\\\)), what is \\\\(\\\\cos C\\\\) written as a function of \\\\(\\\\angle A\\\\)?"),
        (42,48, "Calculate the equivalent trigonometric ratio of angle \\\\(A\\\\) for \\\\(\\\\cos 42^\\\\circ\\\\) in right \\\\(\\\\triangle ABC\\\\)."),
        (52,38, "In \\\\(\\\\triangle ABC\\\\) right-angled at \\\\(B\\\\), \\\\(\\\\cos 52^\\\\circ\\\\) is identical to which trigonometric ratio of angle \\\\(A\\\\)?"),
        (62,28, "Determine the trigonometric expression for \\\\(\\\\cos C\\\\) in terms of angle \\\\(A\\\\) when \\\\(\\\\angle C = 62^\\\\circ\\\\) and \\\\(\\\\angle B = 90^\\\\circ\\\\)."),
        (72,18, "What is the value of \\\\(\\\\cos 72^\\\\circ\\\\) expressed as a sine of angle \\\\(A\\\\) in right \\\\(\\\\triangle ABC\\\\)?"),
        (16,74, "In right triangle \\\\(\\\\triangle ABC\\\\) where \\\\(\\\\angle C = 16^\\\\circ\\\\), write \\\\(\\\\cos C\\\\) using the acute angle \\\\(A\\\\)."),
        (26,64, "Express \\\\(\\\\cos 26^\\\\circ\\\\) using angle \\\\(A\\\\) in right-angled \\\\(\\\\triangle ABC\\\\) (\\\\(\\\\angle B = 90^\\\\circ\\\\))."),
        (36,54, "For \\\\(\\\\triangle ABC\\\\) with \\\\(\\\\angle B = 90^\\\\circ\\\\) and \\\\(\\\\angle C = 36^\\\\circ\\\\), convert \\\\(\\\\cos C\\\\) to a ratio of angle \\\\(A\\\\).")
    ]
    data_7 = [
        (15,75, "State the complementary identity relating \\\\(\\\\sin 15^\\\\circ\\\\) and cosine of an acute angle."),
        (25,65, "What angle \\\\(x\\\\) satisfies \\\\(\\\\sin 25^\\\\circ = \\\\cos x\\\\) in standard trigonometry?"),
        (35,55, "Which equation correctly reflects the complementary sine-cosine identity for angle 35°?"),
        (45,45, "In complementary trigonometry, \\\\(\\\\sin 45^\\\\circ\\\\) equals the cosine of what angle?"),
        (55,35, "Determine the angle whose cosine equals \\\\(\\\\sin 55^\\\\circ\\\\)."),
        (65,25, "Identify the correct acute complementary relation for \\\\(\\\\sin 65^\\\\circ\\\\)."),
        (75,15, "Convert \\\\(\\\\sin 75^\\\\circ\\\\) into a cosine expression using complementary angle relations."),
        (85,5, "What is \\\\(\\\\sin 85^\\\\circ\\\\) expressed as the cosine of its complementary angle?"),
        (5,85, "Write \\\\(\\\\sin 5^\\\\circ\\\\) in terms of the cosine of an acute angle."),
        (60,30, "According to complementary ratio relations, \\\\(\\\\sin 60^\\\\circ\\\\) is identical to:")
    ]
    
    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        
        if arch == 0:
            d, comp = data_0[sub_idx]
            svg = svg_trig("A", "B", "C", f"\\\\angle C = {comp}^\\\\circ", f"\\\\angle A = {d}^\\\\circ", "") if has_fig else ""
            prefix = f"{svg}\\n" if svg else ""
            txt = prefix + f"If \\\\(\\\\sin \\\\theta = \\\\cos {d}^\\\\circ\\\\) for an acute angle \\\\(\\\\theta\\\\), find \\\\(\\\\theta\\\\)."
            corr = f"{comp}^\\\\circ"
            dist = [f"{d}^\\\\circ", f"{comp + 10}^\\\\circ", f"{comp - 10}^\\\\circ"]
            sol = f"**Step 1: Complementary identity**\\n\\\\(\\\\cos {d}^\\\\circ = \\\\sin(90^\\\\circ - {d}^\\\\circ) = \\\\sin {comp}^\\\\circ \\\\implies \\\\theta = {comp}^\\\\circ\\\\).\\n**Step 2: Conclusion**\\n{comp}°."
        elif arch == 1:
            d, comp = data_1[sub_idx]
            svg = svg_trig("A", "B", "C", f"\\\\angle C = {comp}^\\\\circ", f"\\\\angle A = {d}^\\\\circ", "") if has_fig else ""
            prefix = f"{svg}\\n" if svg else ""
            txt = prefix + f"Determine the acute angle \\\\(\\\\theta\\\\) such that \\\\(\\\\cos \\\\theta = \\\\sin {d}^\\\\circ\\\\)."
            corr = f"{comp}^\\\\circ"
            dist = [f"{d}^\\\\circ", f"{comp + 5}^\\\\circ", f"{comp - 5}^\\\\circ"]
            sol = f"**Step 1: Identity**\\n\\\\(\\\\sin {d}^\\\\circ = \\\\cos(90^\\\\circ - {d}^\\\\circ) = \\\\cos {comp}^\\\\circ \\\\implies \\\\theta = {comp}^\\\\circ\\\\).\\n**Step 2: Conclusion**\\n{comp}°."
        elif arch == 2:
            d, k = data_2[sub_idx]
            comp = 90 - d
            svg = svg_trig("A", "B", "C", f"\\\\angle C = {d}^\\\\circ", f"\\\\angle A = {comp}^\\\\circ", "") if has_fig else ""
            prefix = f"{svg}\\n" if svg else ""
            txt = prefix + f"Evaluate \\\\({k} \\\\cdot \\\\frac{{\\\\sin {d}^\\\\circ}}{{\\\\cos {comp}^\\\\circ}}\\\\)."
            corr = f"{k}"
            dist = [f"{k + 2}", f"{k - 1 if k > 1 else k + 3}", f"{k * 2}"]
            sol = f"**Step 1: Ratio simplification**\\nSince \\\\(\\\\cos {comp}^\\\\circ = \\\\sin {d}^\\\\circ\\\\), \\\\(\\\\frac{{\\\\sin {d}^\\\\circ}}{{\\\\cos {comp}^\\\\circ}} = 1\\\\).\\n\\\\({k} \\\\times 1 = {k}\\\\).\\n**Step 2: Conclusion**\\n{k}."
        elif arch == 3:
            d, k = data_3[sub_idx]
            comp = 90 - d
            svg = svg_trig("A", "B", "C", f"\\\\angle C = {d}^\\\\circ", f"\\\\angle A = {comp}^\\\\circ", "") if has_fig else ""
            prefix = f"{svg}\\n" if svg else ""
            txt = prefix + f"Calculate the value of \\\\((\\\\sin {d}^\\\\circ - \\\\cos {comp}^\\\\circ) + {k}\\\\)."
            corr = f"{k}"
            dist = [f"{k + 1}", f"{k - 1}", f"{k * 2}"]
            sol = f"**Step 1: Simplify**\\n\\\\(\\\\sin {d}^\\\\circ - \\\\cos {comp}^\\\\circ = 0\\\\).\\n\\\\(0 + {k} = {k}\\\\).\\n**Step 2: Conclusion**\\n{k}."
        elif arch == 4:
            p, ans_theta, eq_str = data_4[sub_idx]
            svg = svg_trig("A", "B", "C", "", "", "") if has_fig else ""
            prefix = f"{svg}\\n" if svg else ""
            txt = prefix + f"Find the acute angle \\\\(\\\\theta\\\\) if \\\\({eq_str}\\\\)."
            corr = f"{ans_theta}^\\\\circ"
            dist = [f"{ans_theta + 10}^\\\\circ", f"{ans_theta - 5 if ans_theta > 5 else ans_theta + 15}^\\\\circ", f"{90 - ans_theta}^\\\\circ"]
            sol = f"**Step 1: Solve equation**\\nEquating sum of acute angles to 90° yields \\\\(\\\\theta = {ans_theta}^\\\\circ\\\\).\\n**Step 2: Conclusion**\\n{ans_theta}°."
        elif arch == 5:
            d, val_str = data_5[sub_idx]
            comp = 90 - d
            txt = f"If \\\\(\\\\sin {d}^\\\\circ = {val_str}\\\\), what is the exact value of \\\\(\\\\cos {comp}^\\\\circ\\\\)?"
            corr = f"\\\\({val_str}\\\\)"
            dist = ["\\\\(\\frac{1}{2}\\\\)", "\\\\(1\\\\)", "\\\\(0\\\\)"]
            sol = f"**Step 1: Complementary identity**\\n\\\\(\\\\cos {comp}^\\\\circ = \\\\cos(90^\\\\circ - {d}^\\\\circ) = \\\\sin {d}^\\\\circ = {val_str}\\\\).\\n**Step 2: Conclusion**\\n\\\\({val_str}\\\\)."
        elif arch == 6:
            c_ang, a_ang, txt_stem = data_6[sub_idx]
            svg = svg_trig("A", "B", "C", f"\\\\angle C = {c_ang}^\\\\circ", f"\\\\angle A = {a_ang}^\\\\circ", "") if has_fig else ""
            prefix = f"{svg}\\n" if svg else ""
            txt = prefix + txt_stem
            corr = f"\\\\(\\\\sin {a_ang}^\\\\circ\\\\)"
            dist = [f"\\\\(\\\\cos {a_ang}^\\\\circ\\\\)", f"\\\\(\\\\tan {a_ang}^\\\\circ\\\\)", f"\\\\(\\\\sin {c_ang}^\\\\circ\\\\)"]
            sol = f"**Step 1: Acute angles in right triangle**\\n\\\\(\\\\angle A = 90^\\\\circ - {c_ang}^\\\\circ = {a_ang}^\\\\circ\\\\).\\n\\\\(\\\\cos C = \\\\sin A = \\\\sin {a_ang}^\\\\circ\\\\).\\n**Step 2: Conclusion**\\n\\\\(\\\\sin {a_ang}^\\\\circ\\\\)."
        else:
            ang, comp, txt_stem = data_7[sub_idx]
            txt = txt_stem
            corr = f"\\\\(\\\\sin {ang}^\\\\circ = \\\\cos {comp}^\\\\circ\\\\)"
            dist = [f"\\\\(\\\\sin {ang}^\\\\circ + \\\\cos {comp}^\\\\circ = 1\\\\)", f"\\\\(\\\\cos {ang}^\\\\circ = \\\\sin {ang}^\\\\circ\\\\)", f"\\\\(\\\\tan {ang}^\\\\circ = 1\\\\)"]
            sol = f"**Step 1: Formula**\\n\\\\(\\\\sin \\\\theta = \\\\cos(90^\\\\circ - \\\\theta)\\\\).\\nFor \\\\(\\\\theta = {ang}^\\\\circ\\\\), \\\\(\\\\sin {ang}^\\\\circ = \\\\cos {comp}^\\\\circ\\\\).\\n**Step 2: Conclusion**\\n\\\\(\\\\sin {ang}^\\\\circ = \\\\cos {comp}^\\\\circ\\\\)."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def gen_8_2_3():
    tc = "MH-9-MTH2-8-8.2.3"
    tname = "Fundamental identity: sin²θ + cos²θ = 1"
    qs = []
    
    triples_0 = [(3,4,5), (5,12,13), (8,15,17), (7,24,25), (9,40,41), (12,35,37), (20,21,29), (11,60,61), (16,63,65), (28,45,53)]
    triples_1 = [(4,3,5), (12,5,13), (15,8,17), (24,7,25), (40,9,41), (35,12,37), (21,20,29), (60,11,61), (63,16,65), (45,28,53)]
    data_2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
    data_3 = [(1,4,3,4), (1,9,8,9), (4,9,5,9), (1,16,15,16), (9,16,7,16), (1,25,24,25), (4,25,21,25), (9,25,16,25), (16,25,9,25), (1,36,35,36)]
    data_4 = [(3,4,1,4), (8,9,1,9), (5,9,4,9), (15,16,1,16), (7,16,9,16), (24,25,1,25), (21,25,4,25), (16,25,9,25), (9,25,16,25), (35,36,1,36)]
    data_5 = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    data_6 = [(2,1), (3,2), (4,3), (5,4), (6,5), (7,6), (8,7), (10,9), (13,12), (17,16)]
    data_7 = [(10,11), (20,21), (30,31), (40,41), (50,51), (60,61), (70,71), (80,81), (90,91), (100,101)]
    
    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        
        if arch == 0:
            a, b, c = triples_0[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {a}", f"BC = {b}", f"AC = {c}") if has_fig else ""
            prefix = f"{svg}\\n" if svg else ""
            txt = prefix + f"If \\\\(\\\\sin \\\\theta = \\\\frac{{{a}}}{{{c}}}\\\\) for an acute angle \\\\(\\\\theta\\\\), find \\\\(\\\\cos \\\\theta\\\\) using \\\\(\\\\sin^2 \\\\theta + \\\\cos^2 \\\\theta = 1\\\\)."
            corr = f"\\\\(\\\\frac{{{b}}}{{{c}}}\\\\)"
            dist = [f"\\\\(\\\\frac{{{a}}}{{{c}}}\\\\)", f"\\\\(\\\\frac{{{b}}}{{{a}}}\\\\)", f"\\\\(\\\\frac{{{a}}}{{{b}}}\\\\)"]
            sol = f"**Step 1: Fundamental identity**\\n\\\\(\\\\cos^2 \\\\theta = 1 - \\\\sin^2 \\\\theta = \\\\frac{{{b*b}}}{{{c*c}}}\\\\).\\n\\\\(\\\\cos \\\\theta = \\\\frac{{{b}}}{{{c}}}\\\\).\\n**Step 2: Conclusion**\\n\\\\(\\\\frac{{{b}}}{{{c}}}\\\\)."
        elif arch == 1:
            a, b, c = triples_1[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {b}", f"BC = {a}", f"AC = {c}") if has_fig else ""
            prefix = f"{svg}\\n" if svg else ""
            txt = prefix + f"If \\\\(\\\\cos \\\\theta = \\\\frac{{{a}}}{{{c}}}\\\\) for an acute angle \\\\(\\\\theta\\\\), determine \\\\(\\\\sin \\\\theta\\\\)."
            corr = f"\\\\(\\\\frac{{{b}}}{{{c}}}\\\\)"
            dist = [f"\\\\(\\\\frac{{{a}}}{{{c}}}\\\\)", f"\\\\(\\\\frac{{{b}}}{{{a}}}\\\\)", f"\\\\(\\\\frac{{{a}}}{{{b}}}\\\\)"]
            sol = f"**Step 1: Fundamental identity**\\n\\\\(\\\\sin^2 \\\\theta = 1 - \\\\cos^2 \\\\theta = \\\\frac{{{b*b}}}{{{c*c}}}\\\\).\\n\\\\(\\\\sin \\\\theta = \\\\frac{{{b}}}{{{c}}}\\\\).\\n**Step 2: Conclusion**\\n\\\\(\\\\frac{{{b}}}{{{c}}}\\\\)."
        elif arch == 2:
            k = data_2[sub_idx]
            svg = svg_trig("A", "B", "C", "", "", "") if has_fig else ""
            prefix = f"{svg}\\n" if svg else ""
            txt = prefix + f"Evaluate the expression \\\\({k}(\\\\sin^2 \\\\theta + \\\\cos^2 \\\\theta)\\\\) for any acute angle \\\\(\\\\theta\\\\)."
            corr = f"{k}"
            dist = [f"{k + 1}", f"{k - 1}", f"{k * 2}"]
            sol = f"**Step 1: Identity substitution**\\n\\\\(\\\\sin^2 \\\\theta + \\\\cos^2 \\\\theta = 1\\\\).\\n\\\\({k} \\\\times 1 = {k}\\\\).\\n**Step 2: Conclusion**\\n{k}."
        elif arch == 3:
            num, den, c_num, c_den = data_3[sub_idx]
            txt = f"If \\\\(\\\\sin^2 \\\\theta = \\\\frac{{{num}}}{{{den}}}\\\\), what is the value of \\\\(\\\\cos^2 \\\\theta\\\\)?"
            corr = f"\\\\(\\\\frac{{{c_num}}}{{{c_den}}}\\\\)"
            dist = [f"\\\\(\\\\frac{{{num}}}{{{den}}}\\\\)", f"\\\\(\\frac{{{c_num}}}{{{c_den + 2}}}\\\\)", "\\\\(1\\\\)"]
            sol = f"**Step 1: Identity**\\n\\\\(\\\\cos^2 \\\\theta = 1 - \\\\sin^2 \\\\theta = 1 - \\\\frac{{{num}}}{{{den}}} = \\\\frac{{{c_num}}}{{{c_den}}}\\\\).\\n**Step 2: Conclusion**\\n\\\\(\\\\frac{{{c_num}}}{{{c_den}}}\\\\)."
        elif arch == 4:
            num, den, c_num, c_den = data_4[sub_idx]
            txt = f"If \\\\(\\\\cos^2 \\\\theta = \\\\frac{{{num}}}{{{den}}}\\\\), find the value of \\\\(\\\\sin^2 \\\\theta\\\\)."
            corr = f"\\\\(\\\\frac{{{c_num}}}{{{c_den}}}\\\\)"
            dist = [f"\\\\(\\\\frac{{{num}}}{{{den}}}\\\\)", f"\\\\(\\frac{{{c_num}}}{{{c_den + 2}}}\\\\)", "\\\\(0\\\\)"]
            sol = f"**Step 1: Identity**\\n\\\\(\\\\sin^2 \\\\theta = 1 - \\\\cos^2 \\\\theta = 1 - \\\\frac{{{num}}}{{{den}}} = \\\\frac{{{c_num}}}{{{c_den}}}\\\\).\\n**Step 2: Conclusion**\\n\\\\(\\\\frac{{{c_num}}}{{{c_den}}}\\\\)."
        elif arch == 5:
            k = data_5[sub_idx]
            ans_val = k - 1
            txt = f"Calculate the value of \\\\({k} - (\\\\sin^2 \\\\theta + \\\\cos^2 \\\\theta)\\\\)."
            corr = f"{ans_val}"
            dist = [f"{k}", f"{k + 1}", f"{ans_val - 2}"]
            sol = f"**Step 1: Evaluate**\\n\\\\(\\\\sin^2 \\\\theta + \\\\cos^2 \\\\theta = 1\\\\).\\n\\\\({k} - 1 = {ans_val}\\\\).\\n**Step 2: Conclusion**\\n{ans_val}."
        elif arch == 6:
            k_val, diff_val = data_6[sub_idx]
            txt = f"If \\\\(\\\\sin \\\\theta = \\\\frac{{1}}{{\\\\sqrt{{{k_val}}}}}\\\\), what is \\\\(\\\\cos \\\\theta\\\\)?"
            corr = f"\\\\(\\\\sqrt{{\\\\frac{{{diff_val}}}{{{k_val}}}}}\\\\)" if diff_val != 1 else f"\\\\(\\\\frac{{1}}{{\\\\sqrt{{{k_val}}}}}\\\\)"
            dist = ["\\\\(\\frac{1}{2}\\\\)", "\\\\(1\\\\)", f"\\\\(\\frac{{{k_val}}}{{2}}\\\\)" ]
            sol = f"**Step 1: Identity**\\n\\\\(\\\\cos^2 \\\\theta = 1 - \\\\frac{{1}}{{{k_val}}} = \\\\frac{{{diff_val}}}{{{k_val}}}\\\\).\\n**Step 2: Conclusion**\\n{corr}."
        else:
            k, ans_k = data_7[sub_idx]
            txt = f"Evaluate \\\\({k} + \\\\sin^2 35^\\\\circ + \\\\cos^2 35^\\\\circ\\\\)."
            corr = f"{ans_k}"
            dist = [f"{k}", f"{ans_k + 2}", f"{ans_k - 2}"]
            sol = f"**Step 1: Identity**\\n\\\\(\\\\sin^2 35^\\\\circ + \\\\cos^2 35^\\\\circ = 1\\\\).\\n\\\\({k} + 1 = {ans_k}\\\\).\\n**Step 2: Conclusion**\\n{ans_k}."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def gen_8_3_1():
    tc = "MH-9-MTH2-8-8.3.1"
    tname = "Derivation of values using geometric triangles"
    qs = []
    
    data_0 = [
        (6,3, "In \\\\(\\\\triangle ABC\\\\) with \\\\(\\\\angle B = 90^\\\\circ\\\\), \\\\(\\\\angle C = 30^\\\\circ\\\\), and hypotenuse \\\\(AC = 6\\\\), find length \\\\(AB\\\\)."),
        (10,5, "For right-angled \\\\(\\\\triangle ABC\\\\) (\\\\(\\\\angle B = 90^\\\\circ\\\\), \\\\(\\\\angle C = 30^\\\\circ\\\\)), compute side \\\\(AB\\\\) when \\\\(AC = 10\\\\)."),
        (14,7, "What is the length of side \\\\(AB\\\\) opposite to 30° in \\\\(\\\\triangle ABC\\\\) (\\\\(\\\\angle B = 90^\\\\circ\\\\)) if hypotenuse \\\\(AC = 14\\\\)?"),
        (18,9, "Calculate opposite side \\\\(AB\\\\) in right triangle \\\\(\\\\triangle ABC\\\\) with \\\\(\\\\angle C = 30^\\\\circ\\\\) and \\\\(AC = 18\\\\)."),
        (22,11, "Determine side \\\\(AB\\\\) in \\\\(\\\\triangle ABC\\\\) (\\\\(\\\\angle B = 90^\\\\circ\\\\), \\\\(\\\\angle C = 30^\\\\circ\\\\)) having hypotenuse \\\\(AC = 22\\\\)."),
        (26,13, "Evaluate the length of \\\\(AB\\\\) in \\\\(\\\\triangle ABC\\\\) right-angled at \\\\(B\\\\) given \\\\(\\\\angle C = 30^\\\\circ\\\\) and \\\\(AC = 26\\\\)."),
        (30,15, "Find the opposite leg \\\\(AB\\\\) in 30°-60°-90° right \\\\(\\\\triangle ABC\\\\) if hypotenuse \\\\(AC = 30\\\\)."),
        (34,17, "In right triangle \\\\(\\\\triangle ABC\\\\), hypotenuse \\\\(AC = 34\\\\) and \\\\(\\\\angle C = 30^\\\\circ\\\\). Find \\\\(AB\\\\)."),
        (38,19, "Compute the measure of side \\\\(AB\\\\) in \\\\(\\\\triangle ABC\\\\) (\\\\(\\\\angle B = 90^\\\\circ\\\\), \\\\(\\\\angle C = 30^\\\\circ\\\\), \\\\(AC = 38\\\\))."),
        (42,21, "If \\\\(\\\\angle C = 30^\\\\circ\\\\) and \\\\(AC = 42\\\\) in right \\\\(\\\\triangle ABC\\\\) (\\\\(\\\\angle B = 90^\\\\circ\\\\)), what is \\\\(AB\\\\)?")
    ]
    data_1 = [(2,"\\\\sqrt{3}"), (4,"2\\\\sqrt{3}"), (6,"3\\\\sqrt{3}"), (8,"4\\\\sqrt{3}"), (10,"5\\\\sqrt{3}"), (12,"6\\\\sqrt{3}"), (14,"7\\\\sqrt{3}"), (16,"8\\\\sqrt{3}"), (18,"9\\\\sqrt{3}"), (20,"10\\\\sqrt{3}")]
    data_2 = [(3,"3\\\\sqrt{2}"), (5,"5\\\\sqrt{2}"), (7,"7\\\\sqrt{2}"), (9,"9\\\\sqrt{2}"), (11,"11\\\\sqrt{2}"), (13,"13\\\\sqrt{2}"), (15,"15\\\\sqrt{2}"), (17,"17\\\\sqrt{2}"), (19,"19\\\\sqrt{2}"), (21,"21\\\\sqrt{2}")]
    data_3 = [(2,"2\\\\sqrt{2}",2), (4,"4\\\\sqrt{2}",4), (6,"6\\\\sqrt{2}",6), (8,"8\\\\sqrt{2}",8), (10,"10\\\\sqrt{2}",10), (12,"12\\\\sqrt{2}",12), (14,"14\\\\sqrt{2}",14), (16,"16\\\\sqrt{2}",16), (18,"18\\\\sqrt{2}",18), (20,"20\\\\sqrt{2}",20)]
    data_4 = [(12,6), (16,8), (20,10), (24,12), (28,14), (32,16), (36,18), (40,20), (44,22), (48,24)]
    data_5 = [(3,6), (5,10), (7,14), (9,18), (11,22), (13,26), (15,30), (17,34), (19,38), (21,42)]
    data_6 = [(2,4), (3,6), (4,8), (5,10), (6,12), (7,14), (8,16), (9,18), (10,20), (11,22)]
    data_7 = [15, 25, 35, 45, 55, 65, 75, 85, 20, 40]
    
    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        
        if arch == 0:
            hyp, opp, txt_stem = data_0[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = ?", "", f"AC = {hyp}") if has_fig else ""
            prefix = f"{svg}\\n" if svg else ""
            txt = prefix + txt_stem
            corr = f"{opp}"
            dist = [f"{opp + 2}", f"{opp - 2 if opp > 2 else opp + 4}", f"{opp * 2}"]
            sol = f"**Step 1: 30°-60°-90° theorem**\\n\\\\(AB = \\\\frac{{1}}{{2}} \\\\times AC = \\\\frac{{1}}{{2}} \\\\times {hyp} = {opp}\\\\).\\n**Step 2: Conclusion**\\n{opp}."
        elif arch == 1:
            hyp, opp_str = data_1[sub_idx]
            svg = svg_trig("A", "B", "C", "", f"BC = ?", f"AC = {hyp}") if has_fig else ""
            prefix = f"{svg}\\n" if svg else ""
            txt = prefix + f"In \\\\(\\\\triangle ABC\\\\) (\\\\(\\\\angle B = 90^\\\\circ\\\\), \\\\(\\\\angle A = 30^\\\\circ\\\\), \\\\(AC = {hyp}\\\\)), find side \\\\(BC\\\\) opposite to 30°."
            half_hyp = hyp // 2
            corr = f"{half_hyp}"
            dist = [f"{half_hyp + 2}", f"{half_hyp - 1}", f"{hyp}"]
            sol = f"**Step 1: 30°-60°-90° theorem**\\nSide opposite 30° is \\\\(\\frac{{1}}{{2}} \\\\times {hyp} = {half_hyp}\\\\).\\n**Step 2: Conclusion**\\n{half_hyp}."
        elif arch == 2:
            s, hyp_str = data_2[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {s}", f"BC = {s}", "AC = ?") if has_fig else ""
            prefix = f"{svg}\\n" if svg else ""
            txt = prefix + f"In an isosceles right triangle \\\\(\\\\triangle ABC\\\\) (\\\\(\\\\angle B = 90^\\\\circ\\\\)), if legs \\\\(AB = BC = {s}\\\\), find hypotenuse \\\\(AC\\\\)."
            corr = f"\\\\({hyp_str}\\\\)"
            dist = [f"\\\\({s}\\\\)", f"\\\\({s * 2}\\\\)", f"\\\\({s}\\\\sqrt{{3}}\\\\)" ]
            sol = f"**Step 1: 45°-45°-90° theorem**\\n\\\\(AC = \\\\sqrt{{2}} \\\\times \\\\text{{leg}} = {hyp_str}\\\\).\\n**Step 2: Conclusion**\\n\\\\({hyp_str}\\\\)."
        elif arch == 3:
            s, hyp_str, leg = data_3[sub_idx]
            svg = svg_trig("A", "B", "C", "AB = ?", "BC = ?", f"AC = {hyp_str}") if has_fig else ""
            prefix = f"{svg}\\n" if svg else ""
            txt = prefix + f"In 45°-45°-90° \\\\(\\\\triangle ABC\\\\) (\\\\(\\\\angle B = 90^\\\\circ\\\\)), if hypotenuse \\\\(AC = {hyp_str}\\\\), find the length of each perpendicular side."
            corr = f"{leg}"
            dist = [f"{leg + 2}", f"{leg - 2 if leg > 2 else leg + 3}", f"{leg * 2}"]
            sol = f"**Step 1: 45°-45°-90° theorem**\\n\\\\(\\\\text{{leg}} = \\\\frac{{AC}}{{\\\\sqrt{{2}}}} = {leg}\\\\).\\n**Step 2: Conclusion**\\n{leg}."
        elif arch == 4:
            hyp_val, opp_val = data_4[sub_idx]
            txt = f"In a 30°-60°-90° right triangle with hypotenuse \\\\({hyp_val}\\\\), find the length of the side opposite to 30°."
            corr = f"{opp_val}"
            dist = [f"{opp_val + 2}", f"{opp_val - 2}", f"{hyp_val}"]
            sol = f"**Step 1: Formula**\\n\\\\(\\text{{opposite 30°}} = \\\\frac{{1}}{{2}} \\\\times {hyp_val} = {opp_val}\\\\).\\n**Step 2: Conclusion**\\n{opp_val}."
        elif arch == 5:
            s_val, hyp_ans = data_5[sub_idx]
            txt = f"In a 30°-60°-90° right triangle, the side opposite to 60° is \\\\({s_val}\\\\sqrt{{3}}\\\\). What is the hypotenuse?"
            corr = f"{hyp_ans}"
            dist = [f"{s_val * 3}", f"{hyp_ans + 4}", f"{hyp_ans - 4}"]
            sol = f"**Step 1: Formula**\\n\\\\(\\text{{opposite 60°}} = \\\\frac{{\\\\sqrt{{3}}}}{{2}} \\\\times \\\\text{{hyp}} \\\\implies \\\\text{{hyp}} = 2 \\\\times {s_val} = {hyp_ans}\\\\).\\n**Step 2: Conclusion**\\n{hyp_ans}."
        elif arch == 6:
            opp, hyp = data_6[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {opp}", "", "AC = ?") if has_fig else ""
            prefix = f"{svg}\\n" if svg else ""
            txt = prefix + f"In \\\\(\\\\triangle ABC\\\\) (\\\\(\\\\angle B = 90^\\\\circ\\\\), \\\\(\\\\angle C = 30^\\\\circ\\\\)), if side \\\\(AB = {opp}\\\\), what is hypotenuse \\\\(AC\\\\)?\"
            corr = f"{hyp}"
            dist = [f"{opp}", f"{hyp + 4}", f"{opp * 3}"]
            sol = f"**Step 1: 30°-60°-90° theorem**\\n\\\\(AC = 2 \\\\times AB = 2 \\\\times {opp} = {hyp}\\\\).\\n**Step 2: Conclusion**\\n{hyp}."
        else:
            ang = data_7[sub_idx]
            txt = f"In a right triangle with acute angle \\\\({ang}^\\\\circ\\\\), what is the other acute angle?"
            comp = 90 - ang
            corr = f"{comp}^\\\\circ"
            dist = [f"{comp + 10}^\\\\circ", f"{comp - 10}^\\\\circ", f"{ang}^\\\\circ"]
            sol = f"**Step 1: Angle sum**\\n\\\\(90^\\\\circ - {ang}^\\\\circ = {comp}^\\\\circ\\\\).\\n**Step 2: Conclusion**\\n{comp}°."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def gen_8_3_2():
    tc = "MH-9-MTH2-8-8.3.2"
    tname = "Evaluating trigonometric algebraic expressions"
    qs = []
    
    data_0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data_1 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    data_2 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    data_3 = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
    data_4 = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    data_5 = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
    data_6 = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
    data_7 = [
        (30, "2\\\\sin x = 1", "Find acute angle \\\\(x\\\\) satisfying \\\\(2\\\\sin x = 1\\\\)."),
        (60, "2\\\\cos x = 1", "Calculate the acute angle \\\\(x\\\\) when \\\\(2\\\\cos x = 1\\\\)."),
        (45, "\\\\tan x = 1", "Determine acute angle \\\\(x\\\\) given \\\\(\\\\tan x = 1\\\\)."),
        (40, "\\\\sin(x - 10^\\\\circ) = \\\\frac{1}{2}", "What is the acute angle \\\\(x\\\\) if \\\\(\\\\sin(x - 10^\\\\circ) = \\\\frac{1}{2}\\\\)?"),
        (50, "\\\\cos(x + 10^\\\\circ) = \\\\frac{1}{2}", "Evaluate acute angle \\\\(x\\\\) if \\\\(\\\\cos(x + 10^\\\\circ) = \\\\frac{1}{2}\\\\)."),
        (70, "\\\\tan(x - 25^\\\\circ) = 1", "Find the value of acute angle \\\\(x\\\\) for which \\\\(\\\\tan(x - 25^\\\\circ) = 1\\\\)."),
        (80, "\\\\sin(x + 10^\\\\circ) = 1", "Solve the trigonometric equation \\\\(\\\\sin(x + 10^\\\\circ) = 1\\\\) for acute angle \\\\(x\\\\)."),
        (10, "\\\\cos(x - 10^\\\\circ) = 1", "Determine \\\\(x\\\\) in \\\\(0^\\\\circ < x < 90^\\\\circ\\\\) where \\\\(\\\\cos(x - 10^\\\\circ) = 1\\\\)."),
        (35, "\\\\tan(x + 25^\\\\circ) = \\\\sqrt{3}", "Compute acute angle \\\\(x\\\\) when \\\\(\\\\tan(x + 25^\\\\circ) = \\\\sqrt{3}\\\\)."),
        (15, "\\\\sin(2x) = \\\\frac{1}{2}", "For what acute angle \\\\(x\\\\) does \\\\(\\\\sin(2x) = \\\\frac{1}{2}\\\\)?")
    ]
    
    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = False
        
        if arch == 0:
            k = data_0[sub_idx]
            ans_val = 2 + k
            txt = f"Evaluate the expression \\\\(2\\\\sin 30^\\\\circ + \\\\cos 0^\\\\circ + {k}\\\\)."
            corr = f"{ans_val}"
            dist = [f"{ans_val + 2}", f"{ans_val - 2}", f"{k}"]
            sol = f"**Step 1: Substitute values**\\n\\\\(2(\\\\frac{{1}}{{2}}) + 1 + {k} = {ans_val}\\\\).\\n**Step 2: Conclusion**\\n{ans_val}."
        elif arch == 1:
            k = data_1[sub_idx]
            ans_val = 4 + k
            txt = f"Evaluate the expression \\\\(4\\\\cos 60^\\\\circ + 2\\\\tan 45^\\\\circ + {k}\\\\)."
            corr = f"{ans_val}"
            dist = [f"{ans_val + 2}", f"{ans_val - 2}", f"{k}"]
            sol = f"**Step 1: Substitute values**\\n\\\\(4(\\\\frac{{1}}{{2}}) + 2(1) + {k} = {ans_val}\\\\).\\n**Step 2: Conclusion**\\n{ans_val}."
        elif arch == 2:
            k = data_2[sub_idx]
            ans_val = 4 + k
            txt = f"Calculate the numerical value of \\\\(\\\\tan^2 60^\\\\circ + \\\\sin^2 90^\\\\circ + {k}\\\\)."
            corr = f"{ans_val}"
            dist = [f"{ans_val + 3}", f"{ans_val - 3}", f"{k}"]
            sol = f"**Step 1: Substitute values**\\n\\\\((\\\\sqrt{{3}})^2 + (1)^2 + {k} = {ans_val}\\\\).\\n**Step 2: Conclusion**\\n{ans_val}."
        elif arch == 3:
            k = data_3[sub_idx]
            ans_val = 1 + k
            txt = f"Evaluate the expression \\\\(3\\\\tan^2 30^\\\\circ + {k}\\\\)."
            corr = f"{ans_val}"
            dist = [f"{ans_val + 2}", f"{ans_val - 2}", f"{k}"]
            sol = f"**Step 1: Substitute values**\\n\\\\(3(\\\\frac{{1}}{{\\\\sqrt{{3}}}})^2 + {k} = {ans_val}\\\\).\\n**Step 2: Conclusion**\\n{ans_val}."
        elif arch == 4:
            k = data_4[sub_idx]
            ans_val = 1 + k
            txt = f"Calculate the value of \\\\(2\\\\cos^2 45^\\\\circ + {k}\\\\)."
            corr = f"{ans_val}"
            dist = [f"{ans_val + 2}", f"{ans_val - 2}", f"{k}"]
            sol = f"**Step 1: Substitute values**\\n\\\\(2(\\\\frac{{1}}{{\\\\sqrt{{2}}}})^2 + {k} = {ans_val}\\\\).\\n**Step 2: Conclusion**\\n{ans_val}."
        elif arch == 5:
            k = data_5[sub_idx]
            ans_val = 1 + k
            txt = f"Evaluate \\\\(4\\\\sin^2 30^\\\\circ + {k}\\\\)."
            corr = f"{ans_val}"
            dist = [f"{ans_val + 2}", f"{ans_val - 2}", f"{k}"]
            sol = f"**Step 1: Substitute values**\\n\\\\(4(\\\\frac{{1}}{{2}})^2 + {k} = {ans_val}\\\\).\\n**Step 2: Conclusion**\\n{ans_val}."
        elif arch == 6:
            k = data_6[sub_idx]
            ans_val = 3 + k
            txt = f"Evaluate \\\\(\\\\sqrt{{3}}\\\\tan 60^\\\\circ + {k}\\\\)."
            corr = f"{ans_val}"
            dist = [f"{ans_val + 3}", f"{ans_val - 3}", f"{k}"]
            sol = f"**Step 1: Substitute values**\\n\\\\(\\\\sqrt{{3}}(\\\\sqrt{{3}}) + {k} = {ans_val}\\\\).\\n**Step 2: Conclusion**\\n{ans_val}."
        else:
            ang, eq_str, txt_stem = data_7[sub_idx]
            txt = txt_stem
            corr = f"{ang}^\\\\circ"
            dist = [f"{ang + 15}^\\\\circ", f"{90 - ang}^\\\\circ", f"{ang - 15 if ang > 15 else ang + 30}^\\\\circ"]
            sol = f"**Step 1: Standard ratio**\\n\\\\(x = {ang}^\\\\circ\\\\).\\n**Step 2: Conclusion**\\n{ang}°."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def main():
    q1 = gen_8_1_1()
    q2 = gen_8_1_2()
    q3 = gen_8_1_3()
    q4 = gen_8_2_1()
    q5 = gen_8_2_2()
    q6 = gen_8_2_3()
    q7 = gen_8_3_1()
    q8 = gen_8_3_2()
    all_qs = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8
    print('Total Chapter 8 questions:', len(all_qs))
    with open('scripts/mh9_mth2_ch8_perfect.json', 'w', encoding='utf-8') as f:
        json.dump(all_qs, f, indent=2)

if __name__ == '__main__':
    main()
'''

with open('scripts/generate_mh9_mth2_ch8_all.py', 'w', encoding='utf-8') as f:
    f.write(base + fixed_code)
print('Successfully patched generate_mh9_mth2_ch8_all.py!')
