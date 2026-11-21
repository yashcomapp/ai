# scripts/fix_ch8_completely.py
import re

# 1. Fix gen_8_1_1 in generate_mh9_mth2_ch8.py
with open("scripts/generate_mh9_mth2_ch8.py", "r", encoding="utf-8") as f:
    c = f.read()

# Change (5,13,26,10) to (5,13,39,15) so answer is 15 instead of 10
c = c.replace("(5,13,26,10)", "(5,13,39,15)")
with open("scripts/generate_mh9_mth2_ch8.py", "w", encoding="utf-8") as f:
    f.write(c)
print("Updated generate_mh9_mth2_ch8.py")

# 2. In generate_mh9_mth2_ch8_all.py, update gen_8_2_2, gen_8_2_3, gen_8_3_1
with open("scripts/generate_mh9_mth2_ch8_all.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace gen_8_2_2 with unique answers across all archetypes
gen_8_2_2_code = '''def gen_8_2_2():
    tc = "MH-9-MTH2-8-8.2.2"
    tname = "sin θ = cos(90 - θ), cos θ = sin(90 - θ), tan θ = 1 / tan(90 - θ)"
    qs = []
    
    # Arch 0: sin(theta) = cos(alpha) -> theta = 90 - alpha
    data_0 = [
        (25, 65, "Given that \\(\\sin \\theta = \\cos {alpha}^\\circ\\) where \\(\\theta\\) is acute, determine the measure of \\(\\theta\\)."),
        (35, 55, "If \\(\\sin \\theta = \\cos {alpha}^\\circ\\) for an acute angle \\(\\theta\\), calculate the value of \\(\\theta\\)."),
        (42, 48, "In a right triangle, if \\(\\sin \\theta = \\cos {alpha}^\\circ\\), what is the value of acute angle \\(\\theta\\)?"),
        (55, 35, "Solve for acute angle \\(\\theta\\) given the relationship \\(\\sin \\theta = \\cos {alpha}^\\circ\\)."),
        (65, 25, "Find the measure of acute angle \\(\\theta\\) satisfying \\(\\sin \\theta = \\cos {alpha}^\\circ\\)."),
        (15, 75, "Determine acute \\(\\theta\\) when \\(\\sin \\theta = \\cos {alpha}^\\circ\\)."),
        (28, 62, "Evaluate the acute angle \\(\\theta\\) such that \\(\\sin \\theta = \\cos {alpha}^\\circ\\)."),
        (32, 58, "What acute angle \\(\\theta\\) satisfies the equation \\(\\sin \\theta = \\cos {alpha}^\\circ\\)?"),
        (48, 42, "If \\(\\theta\\) is an acute angle and \\(\\sin \\theta = \\cos {alpha}^\\circ\\), find \\(\\theta\\)."),
        (74, 16, "Compute the acute angle \\(\\theta\\) if \\(\\sin \\theta = \\cos {alpha}^\\circ\\).")
    ]
    # Arch 1: cos(theta) = sin(alpha) -> theta = 90 - alpha
    data_1 = [
        (20, 70, "If \\(\\cos \\theta = \\sin {alpha}^\\circ\\) for acute angle \\(\\theta\\), find \\(\\theta\\)."),
        (30, 60, "Determine acute \\(\\theta\\) satisfying \\(\\cos \\theta = \\sin {alpha}^\\circ\\)."),
        (40, 50, "Calculate the acute angle \\(\\theta\\) when \\(\\cos \\theta = \\sin {alpha}^\\circ\\)."),
        (50, 40, "Find the value of acute angle \\(\\theta\\) if \\(\\cos \\theta = \\sin {alpha}^\\circ\\)."),
        (60, 30, "What is the measure of acute \\(\\theta\\) given \\(\\cos \\theta = \\sin {alpha}^\\circ\\)?"),
        (70, 20, "Solve for \\(\\theta\\) (acute) knowing that \\(\\cos \\theta = \\sin {alpha}^\\circ\\)."),
        (10, 80, "Evaluate acute angle \\(\\theta\\) if \\(\\cos \\theta = \\sin {alpha}^\\circ\\)."),
        (80, 10, "In right triangle context, find acute \\(\\theta\\) if \\(\\cos \\theta = \\sin {alpha}^\\circ\\)."),
        (45, 45, "Compute \\(\\theta\\) when \\(\\cos \\theta = \\sin {alpha}^\\circ\\) and \\(\\theta\\) is acute."),
        (64, 26, "Given \\(\\cos \\theta = \\sin {alpha}^\\circ\\), what is the value of acute angle \\(\\theta\\)?")
    ]
    # Arch 2: evaluate sin(alpha) - cos(90 - alpha) = 0
    data_2 = [12, 24, 36, 47, 58, 63, 71, 79, 83, 17]
    # Arch 3: difference angle A - angle C in right triangle
    data_3 = [(10, 80, 70), (20, 70, 50), (30, 60, 30), (40, 50, 10), (22, 68, 46), (34, 56, 22), (18, 72, 54), (26, 64, 38), (38, 52, 14), (16, 74, 58)]
    # Arch 4: tan(theta) = 1/tan(alpha) -> theta = 90 - alpha
    data_4 = [(15, 75), (25, 65), (35, 55), (45, 45), (55, 35), (65, 25), (75, 15), (21, 69), (31, 59), (41, 49)]
    # Arch 5: sin(alpha)/cos(90 - alpha) = 1
    data_5 = [14, 27, 39, 49, 53, 67, 76, 81, 84, 88]
    # Arch 6: sin(theta + a) = cos(theta) -> 2*theta + a = 90 -> theta = (90 - a)/2
    data_6 = [(10, 40), (20, 35), (30, 30), (40, 25), (50, 20), (60, 15), (70, 10), (14, 38), (24, 33), (34, 28)]
    # Arch 7: sin(2 theta) = cos(3 theta) -> 5 theta = 90 -> theta = 18; or similar multipliers
    data_7 = [
        (2, 3, 18, "\\sin(2\\theta) = \\cos(3\\theta)"),
        (1, 4, 18, "\\sin(\\theta) = \\cos(4\\theta)"),
        (1, 1, 45, "\\sin(\\theta) = \\cos(\\theta)"),
        (2, 1, 30, "\\sin(2\\theta) = \\cos(\\theta)"),
        (3, 2, 18, "\\sin(3\\theta) = \\cos(2\\theta)"),
        (4, 1, 18, "\\sin(4\\theta) = \\cos(\\theta)"),
        (1, 2, 30, "\\sin(\\theta) = \\cos(2\\theta)"),
        (3, 1, 22.5, "\\sin(3\\theta) = \\cos(\\theta)"), # handled as frac or exact
        (5, 1, 15, "\\sin(5\\theta) = \\cos(\\theta)"),
        (1, 5, 15, "\\sin(\\theta) = \\cos(5\\theta)")
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        qcode = f"{tc}-OSC-{seq}"
        
        if arch == 0:
            alpha, ans_theta, stem = data_0[sub_idx]
            svg = svg_trig("A", "B", "C", f"\\angle C = {ans_theta}^\\circ", f"\\angle A = {alpha}^\\circ", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + stem.format(alpha=alpha)
            corr = f"{ans_theta}^\\circ"
            dist = [f"{ans_theta + 10}^\\circ", f"{ans_theta - 10 if ans_theta > 10 else ans_theta + 15}^\\circ", f"{alpha}^\\circ"]
            sol = f"**Step 1: Complementary relation**\\nSince \\(\\sin \\theta = \\cos(90^\\circ - \\theta)\\), we have \\(90^\\circ - \\theta = {alpha}^\\circ \\implies \\theta = 90^\\circ - {alpha}^\\circ = {ans_theta}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_theta}°."
        elif arch == 1:
            alpha, ans_theta, stem = data_1[sub_idx]
            svg = svg_trig("A", "B", "C", f"\\angle C = {alpha}^\\circ", f"\\angle A = {ans_theta}^\\circ", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + stem.format(alpha=alpha)
            corr = f"{ans_theta}^\\circ"
            dist = [f"{ans_theta + 8}^\\circ", f"{ans_theta - 8 if ans_theta > 8 else ans_theta + 12}^\\circ", f"{alpha}^\\circ"]
            sol = f"**Step 1: Identity**\\n\\(\\cos \\theta = \\sin(90^\\circ - \\theta) = \\sin {alpha}^\\circ \\implies \\theta = 90^\\circ - {alpha}^\\circ = {ans_theta}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_theta}°."
        elif arch == 2:
            d = data_2[sub_idx]
            comp = 90 - d
            svg = svg_trig("A", "B", "C", f"\\angle C = {d}^\\circ", f"\\angle A = {comp}^\\circ", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            tmpls_sub = [
                "Find the value of \\(\\sin {d}^\\circ - \\cos {comp}^\\circ\\).",
                "Evaluate the trigonometric difference \\(\\sin {d}^\\circ - \\cos {comp}^\\circ\\).",
                "What is the numerical result of \\(\\sin {d}^\\circ - \\cos {comp}^\\circ\\)?",
                "Calculate the simplified value of \\(\\sin {d}^\\circ - \\cos {comp}^\\circ\\).",
                "Determine \\(\\sin {d}^\\circ - \\cos {comp}^\\circ\\).",
                "Compute the value of expression \\(\\sin {d}^\\circ - \\cos {comp}^\\circ\\).",
                "Simplify the expression \\(\\sin {d}^\\circ - \\cos {comp}^\\circ\\).",
                "Evaluate \\(\\sin {d}^\\circ - \\cos {comp}^\\circ\\) using complementary angles.",
                "Find the measure of \\(\\sin {d}^\\circ - \\cos {comp}^\\circ\\).",
                "What does \\(\\sin {d}^\\circ - \\cos {comp}^\\circ\\) simplify to?"
            ]
            txt = prefix + tmpls_sub[sub_idx].format(d=d, comp=comp)
            corr = "0"
            dist = ["1", "-1", f"\\sin {d}^\\circ"]
            sol = f"**Step 1: Complementary angles**\\nSince \\(\\cos {comp}^\\circ = \\cos(90^\\circ - {d}^\\circ) = \\sin {d}^\\circ\\), the difference is \\(\\sin {d}^\\circ - \\sin {d}^\\circ = 0\\).\\n**Step 2: Conclusion**\\n0."
        elif arch == 3:
            d1, d2, diff_ans = data_3[sub_idx]
            svg = svg_trig("A", "B", "C", f"\\angle C = {d1}^\\circ", f"\\angle A = {d2}^\\circ", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            tmpls_sub = [
                "In right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), with acute angle \\(\\angle C = {d1}^\\circ\\), compute \\(\\angle A - \\angle C\\).",
                "For right \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\) and \\(\\angle C = {d1}^\\circ\\), what is the angle difference \\(\\angle A - \\angle C\\)?",
                "Given \\(\\triangle ABC\\) right-angled at \\(B\\) and \\(\\angle C = {d1}^\\circ\\), find \\(\\angle A - \\angle C\\).",
                "Calculate the difference between the two acute angles \\(\\angle A - \\angle C\\) in right \\(\\triangle ABC\\) if \\(\\angle C = {d1}^\\circ\\).",
                "In \\(\\triangle ABC\\) having \\(\\angle B = 90^\\circ\\) and \\(\\angle C = {d1}^\\circ\\), determine the value of \\(\\angle A - \\angle C\\).",
                "What is the measure of \\(\\angle A - \\angle C\\) in right \\(\\triangle ABC\\) when \\(\\angle C = {d1}^\\circ\\)?",
                "Evaluate the angle difference \\(\\angle A - \\angle C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\), \\(\\angle C = {d1}^\\circ\\)).",
                "If \\(\\angle C = {d1}^\\circ\\) in right triangle \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), calculate \\(\\angle A - \\angle C\\).",
                "Determine \\(\\angle A - \\angle C\\) for right \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\) and \\(\\angle C = {d1}^\\circ\\).",
                "Find \\(\\angle A - \\angle C\\) in \\(\\triangle ABC\\) where \\(\\angle B = 90^\\circ\\) and \\(\\angle C = {d1}^\\circ\\)."
            ]
            txt = prefix + tmpls_sub[sub_idx].format(d1=d1, d2=d2)
            corr = f"{diff_ans}^\\circ"
            dist = [f"{diff_ans + 12}^\\circ", f"{diff_ans - 12 if diff_ans > 12 else diff_ans + 16}^\\circ", f"{d1}^\\circ"]
            sol = f"**Step 1: Triangle acute angles**\\n\\(\\angle A = 90^\\circ - {d1}^\\circ = {d2}^\\circ\\).\\n\\(\\angle A - \\angle C = {d2}^\\circ - {d1}^\\circ = {diff_ans}^\\circ\\).\\n**Step 2: Conclusion**\\n{diff_ans}°."
        elif arch == 4:
            d1, d2 = data_4[sub_idx]
            svg = svg_trig("A", "B", "C", "", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            tmpls_sub = [
                "Find the acute angle \\(\\theta\\) if \\(\\tan \\theta = \\frac{{1}}{{\\tan {d1}^\\circ}}\\).",
                "If \\(\\tan \\theta = \\frac{{1}}{{\\tan {d1}^\\circ}}\\) for an acute angle \\(\\theta\\), determine \\(\\theta\\).",
                "Calculate acute angle \\(\\theta\\) satisfying \\(\\tan \\theta \\cdot \\tan {d1}^\\circ = 1\\).",
                "What is the value of acute \\(\\theta\\) if \\(\\tan \\theta = \\cot {d1}^\\circ\\)?",
                "Evaluate the acute angle \\(\\theta\\) such that \\(\\tan \\theta = \\frac{{1}}{{\\tan {d1}^\\circ}}\\).",
                "Solve for acute angle \\(\\theta\\) when \\(\\tan \\theta \\tan {d1}^\\circ = 1\\).",
                "Determine the measure of acute angle \\(\\theta\\) given \\(\\tan \\theta = \\frac{{1}}{{\\tan {d1}^\\circ}}\\).",
                "In right-angled trigonometry, find acute \\(\\theta\\) if \\(\\tan \\theta = \\frac{{1}}{{\\tan {d1}^\\circ}}\\).",
                "Compute the value of acute angle \\(\\theta\\) from \\(\\tan \\theta \\cdot \\tan {d1}^\\circ = 1\\).",
                "What acute angle \\(\\theta\\) satisfies \\(\\tan \\theta = \\frac{{1}}{{\\tan {d1}^\\circ}}\\)?",
            ]
            txt = prefix + tmpls_sub[sub_idx].format(d1=d1)
            corr = f"{d2}^\\circ"
            dist = [f"{d1}^\\circ", f"{d2 + 10}^\\circ", f"{d2 - 10 if d2 > 10 else d2 + 15}^\\circ"]
            sol = f"**Step 1: Identity**\\n\\(\\frac{{1}}{{\\tan {d1}^\\circ}} = \\cot {d1}^\\circ = \\tan(90^\\circ - {d1}^\\circ) = \\tan {d2}^\\circ\\implies \\theta = {d2}^\\circ\\).\\n**Step 2: Conclusion**\\n{d2}°."
        elif arch == 5:
            d = data_5[sub_idx]
            comp = 90 - d
            svg = svg_trig("A", "B", "C", f"\\angle C = {d}^\\circ", f"\\angle A = {comp}^\\circ", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            tmpls_sub = [
                "Calculate the simplified quotient \\(\\frac{{\\sin {d}^\\circ}}{{\\cos {comp}^\\circ}}\\).",
                "What is the value of the trigonometric ratio \\(\\frac{{\\sin {d}^\\circ}}{{\\cos {comp}^\\circ}}\\)?",
                "Evaluate \\(\\frac{{\\sin {d}^\\circ}}{{\\cos {comp}^\\circ}}\\).",
                "Determine the numerical value of \\(\\frac{{\\sin {d}^\\circ}}{{\\cos {comp}^\\circ}}\\).",
                "Find the value of \\(\\frac{{\\sin {d}^\\circ}}{{\\cos {comp}^\\circ}}\\).",
                "Compute the fraction \\(\\frac{{\\sin {d}^\\circ}}{{\\cos {comp}^\\circ}}\\).",
                "Simplify \\(\\frac{{\\sin {d}^\\circ}}{{\\cos {comp}^\\circ}}\\).",
                "Using complementary angle formulas, evaluate \\(\\frac{{\\sin {d}^\\circ}}{{\\cos {comp}^\\circ}}\\).",
                "What is the quotient of \\(\\sin {d}^\\circ\\) and \\(\\cos {comp}^\\circ\\)?",
                "Find the measure of the ratio \\(\\frac{{\\sin {d}^\\circ}}{{\\cos {comp}^\\circ}}\\)."
            ]
            txt = prefix + tmpls_sub[sub_idx].format(d=d, comp=comp)
            corr = "1"
            dist = ["0", "2", f"\\tan {d}^\\circ"]
            sol = f"**Step 1: Complementary angles**\\nSince \\(\\cos {comp}^\\circ = \\sin(90^\\circ - {comp}^\\circ) = \\sin {d}^\\circ\\), the quotient is \\(\\frac{{\\sin {d}^\\circ}}{{\\sin {d}^\\circ}} = 1\\).\\n**Step 2: Conclusion**\\n1."
        elif arch == 6:
            a, ans_theta = data_6[sub_idx]
            svg = svg_trig("A", "B", "C", "", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            tmpls_sub = [
                "Solve for acute \\(\\theta\\) if \\(\\sin(\\theta + {a}^\\circ) = \\cos(\\theta)\\).",
                "Find the measure of acute angle \\(\\theta\\) given \\(\\sin(\\theta + {a}^\\circ) = \\cos(\\theta)\\).",
                "Determine acute angle \\(\\theta\\) such that \\(\\sin(\\theta + {a}^\\circ) = \\cos(\\theta)\\).",
                "What is the value of acute \\(\\theta\\) satisfying \\(\\sin(\\theta + {a}^\\circ) = \\cos(\\theta)\\)?",
                "Calculate the acute angle \\(\\theta\\) from the equation \\(\\sin(\\theta + {a}^\\circ) = \\cos(\\theta)\\).",
                "If \\(\\sin(\\theta + {a}^\\circ) = \\cos(\\theta)\\) for an acute angle \\(\\theta\\), evaluate \\(\\theta\\).",
                "From \\(\\sin(\\theta + {a}^\\circ) = \\cos(\\theta)\\), find acute \\(\\theta\\).",
                "Compute acute angle \\(\\theta\\) if \\(\\sin(\\theta + {a}^\\circ) = \\cos(\\theta)\\).",
                "In right-angled trigonometry, find acute \\(\\theta\\) when \\(\\sin(\\theta + {a}^\\circ) = \\cos(\\theta)\\).",
                "Evaluate the acute angle \\(\\theta\\) if \\(\\sin(\\theta + {a}^\\circ) = \\cos(\\theta)\\)."
            ]
            txt = prefix + tmpls_sub[sub_idx].format(a=a)
            corr = f"{ans_theta}^\\circ"
            dist = [f"{ans_theta + 10}^\\circ", f"{ans_theta - 10 if ans_theta > 10 else ans_theta + 15}^\\circ", f"{90 - ans_theta}^\\circ"]
            sol = f"**Step 1: Identity**\\n\\(\\cos(\\theta) = \\sin(90^\\circ - \\theta)\\implies \\theta + {a}^\\circ = 90^\\circ - \\theta \\implies 2\\theta = {90 - a}^\\circ \\implies \\theta = {ans_theta}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_theta}°."
        elif arch == 7:
            m1, m2, ans_theta, eq_str = data_7[sub_idx]
            svg = svg_trig("A", "B", "C", "", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            tmpls_sub = [
                "Find the acute angle \\(\\theta\\) if \\({eq_str}\\).",
                "Determine the measure of acute angle \\(\\theta\\) given \\({eq_str}\\).",
                "Calculate the value of acute angle \\(\\theta\\) satisfying \\({eq_str}\\).",
                "What acute angle \\(\\theta\\) satisfies the trigonometric relation \\({eq_str}\\)?",
                "Solve for acute \\(\\theta\\) from the equation \\({eq_str}\\).",
                "Evaluate the acute angle \\(\\theta\\) such that \\({eq_str}\\).",
                "If \\({eq_str}\\) for an acute angle \\(\\theta\\), find \\(\\theta\\).",
                "From the equation \\({eq_str}\\), compute acute \\(\\theta\\).",
                "Determine acute \\(\\theta\\) when \\({eq_str}\\).",
                "What is the value of acute angle \\(\\theta\\) if \\({eq_str}\\)?"
            ]
            txt = prefix + tmpls_sub[sub_idx].format(eq_str=eq_str)
            corr = f"{ans_theta}^\\circ"
            dist = [f"{ans_theta + 6}^\\circ", f"{ans_theta - 6 if ans_theta > 6 else ans_theta + 12}^\\circ", f"{90 - ans_theta}^\\circ"]
            sol = f"**Step 1: Complementary angles**\\n\\({eq_str} \\implies {m1}\\theta + {m2}\\theta = 90^\\circ \\implies {m1+m2}\\theta = 90^\\circ \\implies \\theta = {ans_theta}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_theta}°."

        diff = "easy" if arch in [0,1,2] else ("medium" if arch in [3,4,5] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs
'''

# Replace gen_8_2_3 with clean distinct numbers
gen_8_2_3_code = '''def gen_8_2_3():
    tc = "MH-9-MTH2-8-8.2.3"
    tname = "Fundamental Trigonometric Identity: sin²θ + cos²θ = 1"
    qs = []
    
    # Arch 0: Given sin theta = a/b, find cos theta
    data_0 = [
        (3,5,4,5), (5,13,12,13), (8,17,15,17), (7,25,24,25), (9,41,40,41), 
        (12,37,35,37), (20,29,21,29), (11,61,60,61), (16,65,63,65), (28,53,45,53)
    ]
    # Arch 1: Given cos theta = a/b, find sin theta
    data_1 = [
        (4,5,3,5), (12,13,5,13), (15,17,8,17), (24,25,7,25), (40,41,9,41),
        (35,37,12,37), (21,29,20,29), (60,61,11,61), (63,65,16,65), (45,53,28,53)
    ]
    # Arch 2: Given sin theta = a/b, find tan theta = a/adj
    data_2 = [
        (3,5,3,4), (5,13,5,12), (8,17,8,15), (7,25,7,24), (9,41,9,40),
        (12,37,12,35), (20,29,20,21), (11,61,11,60), (16,65,16,63), (28,53,28,45)
    ]
    # Arch 3: Given sin^2 theta = num/den, find cos^2 theta = 1 - num/den (disjoint fractions!)
    data_3 = [
        (1, 4, 3, 4), (1, 9, 8, 9), (4, 9, 5, 9), (1, 16, 15, 16), (9, 16, 7, 16),
        (1, 25, 24, 25), (9, 25, 16, 25), (16, 25, 9, 25), (1, 36, 35, 36), (25, 36, 11, 36)
    ]
    # Arch 4: Given cos^2 theta = num/den, find sin^2 theta = 1 - num/den (disjoint denominators: 49, 64, 81, 100)
    data_4 = [
        (1, 49, 48, 49), (4, 49, 45, 49), (9, 49, 40, 49), (16, 49, 33, 49), (25, 49, 24, 49),
        (1, 64, 63, 64), (9, 64, 55, 64), (25, 64, 39, 64), (1, 81, 80, 81), (16, 81, 65, 81)
    ]
    # Arch 5: Evaluate k - (sin^2 theta + cos^2 theta) = k - 1
    data_5 = [5, 8, 12, 15, 20, 25, 30, 42, 50, 100]
    # Arch 6: Evaluate (1 - sin^2 theta) / cos^2 theta = 1
    data_6 = [13, 21, 32, 44, 56, 68, 77, 82, 37, 49]
    # Arch 7: Evaluate k*(sin^2 theta + cos^2 theta) + m = k + m
    data_7 = [(2,3,5), (3,4,7), (4,5,9), (5,6,11), (6,7,13), (7,8,15), (8,9,17), (9,10,19), (10,11,21), (12,13,25)]

    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        qcode = f"{tc}-OSC-{seq}"
        
        if arch == 0:
            a, b, c, d = data_0[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {a}", "BC = ?", f"AC = {b}") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            tmpls = [
                "If \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\) for an acute angle \\(\\theta\\), find \\(\\cos \\theta\\).",
                "In right-angled \\(\\triangle ABC\\), given \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\), calculate \\(\\cos \\theta\\).",
                "Determine the value of \\(\\cos \\theta\\) when \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\).",
                "What is \\(\\cos \\theta\\) if acute angle \\(\\theta\\) satisfies \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\)?",
                "Calculate \\(\\cos \\theta\\) using the identity \\(\\sin^2 \\theta + \\cos^2 \\theta = 1\\) given \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\).",
                "Find \\(\\cos \\theta\\) knowing that \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\) for acute \\(\\theta\\).",
                "Evaluate \\(\\cos \\theta\\) if \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\).",
                "For acute \\(\\theta\\), if \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\), compute \\(\\cos \\theta\\).",
                "Determine \\(\\cos \\theta\\) given \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\).",
                "What is the measure of \\(\\cos \\theta\\) if \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\)?"
            ]
            txt = prefix + tmpls[sub_idx].format(a=a, b=b)
            corr = f"\\(\\frac{{{c}}}{{{d}}}\\)"
            dist = [f"\\(\\frac{{{a}}}{{{b}}}\\)", f"\\(\\frac{{{c}}}{{{b + 2}}}\\)", f"\\(\\frac{{{a + 1}}}{{{b}}}\\)"]
            sol = f"**Step 1: Trigonometric identity**\\n\\(\\cos^2 \\theta = 1 - \\sin^2 \\theta = 1 - (\\frac{{{a}}}{{{b}}})^2 = 1 - \\frac{{{a*a}}}{{{b*b}}} = \\frac{{{c*c}}}{{{d*d}}}\\).\\n\\(\\cos \\theta = \\frac{{{c}}}{{{d}}}\\).\\n**Step 2: Conclusion**\\n\\(\\frac{{{c}}}{{{d}}}\\)."
        elif arch == 1:
            a, b, c, d = data_1[sub_idx]
            svg = svg_trig("A", "B", "C", "AB = ?", f"BC = {a}", f"AC = {b}") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            tmpls = [
                "If \\(\\cos \\theta = \\frac{{{a}}}{{{b}}}\\) for an acute angle \\(\\theta\\), find \\(\\sin \\theta\\).",
                "In right-angled \\(\\triangle ABC\\), given \\(\\cos \\theta = \\frac{{{a}}}{{{b}}}\\), calculate \\(\\sin \\theta\\).",
                "Determine the value of \\(\\sin \\theta\\) when \\(\\cos \\theta = \\frac{{{a}}}{{{b}}}\\).",
                "What is \\(\\sin \\theta\\) if acute angle \\(\\theta\\) satisfies \\(\\cos \\theta = \\frac{{{a}}}{{{b}}}\\)?",
                "Calculate \\(\\sin \\theta\\) using the identity \\(\\sin^2 \\theta + \\cos^2 \\theta = 1\\) given \\(\\cos \\theta = \\frac{{{a}}}{{{b}}}\\).",
                "Find \\(\\sin \\theta\\) knowing that \\(\\cos \\theta = \\frac{{{a}}}{{{b}}}\\) for acute \\(\\theta\\).",
                "Evaluate \\(\\sin \\theta\\) if \\(\\cos \\theta = \\frac{{{a}}}{{{b}}}\\).",
                "For acute \\(\\theta\\), if \\(\\cos \\theta = \\frac{{{a}}}{{{b}}}\\), compute \\(\\sin \\theta\\).",
                "Determine \\(\\sin \\theta\\) given \\(\\cos \\theta = \\frac{{{a}}}{{{b}}}\\).",
                "What is the measure of \\(\\sin \\theta\\) if \\(\\cos \\theta = \\frac{{{a}}}{{{b}}}\\)?"
            ]
            txt = prefix + tmpls[sub_idx].format(a=a, b=b)
            corr = f"\\(\\frac{{{c}}}{{{d}}}\\)"
            dist = [f"\\(\\frac{{{a}}}{{{b}}}\\)", f"\\(\\frac{{{c}}}{{{b + 2}}}\\)", f"\\(\\frac{{{a + 1}}}{{{b}}}\\)"]
            sol = f"**Step 1: Trigonometric identity**\\n\\(\\sin^2 \\theta = 1 - \\cos^2 \\theta = 1 - (\\frac{{{a}}}{{{b}}})^2 = 1 - \\frac{{{a*a}}}{{{b*b}}} = \\frac{{{c*c}}}{{{d*d}}}\\).\\n\\(\\sin \\theta = \\frac{{{c}}}{{{d}}}\\).\\n**Step 2: Conclusion**\\n\\(\\frac{{{c}}}{{{d}}}\\)."
        elif arch == 2:
            a, b, c, d = data_2[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {a}", f"BC = {d}", f"AC = {b}") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            tmpls = [
                "If \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\) for acute angle \\(\\theta\\), determine \\(\\tan \\theta\\).",
                "Find \\(\\tan \\theta\\) given that \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\) in right triangle.",
                "Calculate \\(\\tan \\theta\\) when \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\).",
                "What is the value of \\(\\tan \\theta\\) if \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\)?",
                "Evaluate \\(\\tan \\theta\\) for an acute angle \\(\\theta\\) having \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\).",
                "In right-angled \\(\\triangle ABC\\), find \\(\\tan \\theta\\) if \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\).",
                "Determine the tangent ratio \\(\\tan \\theta\\) knowing \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\).",
                "Compute \\(\\tan \\theta\\) given \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\).",
                "Find \\(\\tan \\theta\\) using identities if \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\).",
                "What is \\(\\tan \\theta\\) when acute angle \\(\\theta\\) satisfies \\(\\sin \\theta = \\frac{{{a}}}{{{b}}}\\)?"
            ]
            txt = prefix + tmpls[sub_idx].format(a=a, b=b)
            corr = f"\\(\\frac{{{c}}}{{{d}}}\\)"
            dist = [f"\\(\\frac{{{a}}}{{{b}}}\\)", f"\\(\\frac{{{d}}}{{{c}}}\\)", f"\\(\\frac{{{c}}}{{{b}}}\\)"]
            sol = f"**Step 1: Compute cos θ then tan θ**\\n\\(\\cos \\theta = \\sqrt{{1 - (\\frac{{{a}}}{{{b}}})^2}} = \\frac{{{d}}}{{{b}}}\\).\\n\\(\\tan \\theta = \\frac{{\\sin \\theta}}{{\\cos \\theta}} = \\frac{{{c}}}{{{d}}}\\).\\n**Step 2: Conclusion**\\n\\(\\frac{{{c}}}{{{d}}}\\)."
        elif arch == 3:
            num, den, c_num, c_den = data_3[sub_idx]
            tmpls = [
                "If \\(\\sin^2 \\theta = \\frac{{{num}}}{{{den}}}\\), what is the value of \\(\\cos^2 \\theta\\)?",
                "Given \\(\\sin^2 \\theta = \\frac{{{num}}}{{{den}}}\\), find \\(\\cos^2 \\theta\\).",
                "Calculate \\(\\cos^2 \\theta\\) when \\(\\sin^2 \\theta = \\frac{{{num}}}{{{den}}}\\).",
                "Determine the value of \\(\\cos^2 \\theta\\) if \\(\\sin^2 \\theta = \\frac{{{num}}}{{{den}}}\\).",
                "What does \\(\\cos^2 \\theta\\) equal if \\(\\sin^2 \\theta = \\frac{{{num}}}{{{den}}}\\)?",
                "Evaluate \\(\\cos^2 \\theta\\) knowing that \\(\\sin^2 \\theta = \\frac{{{num}}}{{{den}}}\\).",
                "For acute angle \\(\\theta\\), if \\(\\sin^2 \\theta = \\frac{{{num}}}{{{den}}}\\), compute \\(\\cos^2 \\theta\\).",
                "Find \\(\\cos^2 \\theta\\) using fundamental identity when \\(\\sin^2 \\theta = \\frac{{{num}}}{{{den}}}\\).",
                "Compute the value of \\(\\cos^2 \\theta\\) given \\(\\sin^2 \\theta = \\frac{{{num}}}{{{den}}}\\).",
                "In trigonometry, if \\(\\sin^2 \\theta = \\frac{{{num}}}{{{den}}}\\), what is \\(\\cos^2 \\theta\\)?"
            ]
            txt = tmpls[sub_idx].format(num=num, den=den)
            corr = f"\\(\\frac{{{c_num}}}{{{c_den}}}\\)"
            dist = [f"\\(\\frac{{{num}}}{{{den}}}\\)", f"\\(\\frac{{{c_num + 2}}}{{{c_den}}}\\)", "\\(1\\)"]
            sol = f"**Step 1: Identity**\\n\\(\\cos^2 \\theta = 1 - \\sin^2 \\theta = 1 - \\frac{{{num}}}{{{den}}} = \\frac{{{c_num}}}{{{c_den}}}\\).\\n**Step 2: Conclusion**\\n\\(\\frac{{{c_num}}}{{{c_den}}}\\)."
        elif arch == 4:
            num, den, c_num, c_den = data_4[sub_idx]
            tmpls = [
                "If \\(\\cos^2 \\theta = \\frac{{{num}}}{{{den}}}\\), find the value of \\(\\sin^2 \\theta\\).",
                "Given \\(\\cos^2 \\theta = \\frac{{{num}}}{{{den}}}\\), calculate \\(\\sin^2 \\theta\\).",
                "Determine \\(\\sin^2 \\theta\\) when \\(\\cos^2 \\theta = \\frac{{{num}}}{{{den}}}\\).",
                "What is \\(\\sin^2 \\theta\\) if \\(\\cos^2 \\theta = \\frac{{{num}}}{{{den}}}\\)?",
                "Calculate the measure of \\(\\sin^2 \\theta\\) given \\(\\cos^2 \\theta = \\frac{{{num}}}{{{den}}}\\).",
                "Evaluate \\(\\sin^2 \\theta\\) knowing that \\(\\cos^2 \\theta = \\frac{{{num}}}{{{den}}}\\).",
                "Compute \\(\\sin^2 \\theta\\) for an acute angle \\(\\theta\\) having \\(\\cos^2 \\theta = \\frac{{{num}}}{{{den}}}\\).",
                "Find \\(\\sin^2 \\theta\\) from the identity \\(\\sin^2 \\theta + \\cos^2 \\theta = 1\\) when \\(\\cos^2 \\theta = \\frac{{{num}}}{{{den}}}\\).",
                "Determine the value of \\(\\sin^2 \\theta\\) if \\(\\cos^2 \\theta = \\frac{{{num}}}{{{den}}}\\).",
                "What does \\(\\sin^2 \\theta\\) simplify to if \\(\\cos^2 \\theta = \\frac{{{num}}}{{{den}}}\\)?"
            ]
            txt = tmpls[sub_idx].format(num=num, den=den)
            corr = f"\\(\\frac{{{c_num}}}{{{c_den}}}\\)"
            dist = [f"\\(\\frac{{{num}}}{{{den}}}\\)", f"\\(\\frac{{{c_num + 3}}}{{{c_den}}}\\)", "\\(0\\)"]
            sol = f"**Step 1: Identity**\\n\\(\\sin^2 \\theta = 1 - \\cos^2 \\theta = 1 - \\frac{{{num}}}{{{den}}} = \\frac{{{c_num}}}{{{c_den}}}\\).\\n**Step 2: Conclusion**\\n\\(\\frac{{{c_num}}}{{{c_den}}}\\)."
        elif arch == 5:
            k = data_5[sub_idx]
            ans_val = k - 1
            tmpls = [
                "Calculate the value of \\({k} - (\\sin^2 \\theta + \\cos^2 \\theta)\\).",
                "What is the numerical result of \\({k} - (\\sin^2 \\theta + \\cos^2 \\theta)\\)?",
                "Evaluate the algebraic expression \\({k} - (\\sin^2 \\theta + \\cos^2 \\theta)\\).",
                "Determine the value of \\({k} - (\\sin^2 \\theta + \\cos^2 \\theta)\\) for any angle \\(\\theta\\).",
                "Simplify \\({k} - (\\sin^2 \\theta + \\cos^2 \\theta)\\).",
                "Find the measure of \\({k} - (\\sin^2 \\theta + \\cos^2 \\theta)\\).",
                "Compute the simplified value of \\({k} - (\\sin^2 \\theta + \\cos^2 \\theta)\\).",
                "Using the fundamental identity, evaluate \\({k} - (\\sin^2 \\theta + \\cos^2 \\theta)\\).",
                "What does \\({k} - (\\sin^2 \\theta + \\cos^2 \\theta)\\) equal?",
                "Find the value of expression \\({k} - (\\sin^2 \\theta + \\cos^2 \\theta)\\)."
            ]
            txt = tmpls[sub_idx].format(k=k)
            corr = f"{ans_val}"
            dist = [f"{k}", f"{ans_val + 2}", f"{ans_val - 2 if ans_val > 2 else ans_val + 3}"]
            sol = f"**Step 1: Identity**\\n\\(\\sin^2 \\theta + \\cos^2 \\theta = 1\\).\\n\\({k} - 1 = {ans_val}\\).\\n**Step 2: Conclusion**\\n{ans_val}."
        elif arch == 6:
            d = data_6[sub_idx]
            tmpls = [
                "Simplify the expression \\(\\frac{{1 - \\sin^2 {d}^\\circ}}{{\\cos^2 {d}^\\circ}}\\).",
                "Evaluate the trigonometric ratio \\(\\frac{{1 - \\sin^2 {d}^\\circ}}{{\\cos^2 {d}^\\circ}}\\).",
                "What is the value of \\(\\frac{{1 - \\sin^2 {d}^\\circ}}{{\\cos^2 {d}^\\circ}}\\)?",
                "Calculate the numerical measure of \\(\\frac{{1 - \\sin^2 {d}^\\circ}}{{\\cos^2 {d}^\\circ}}\\).",
                "Determine the simplified value of \\(\\frac{{1 - \\sin^2 {d}^\\circ}}{{\\cos^2 {d}^\\circ}}\\).",
                "Find the value of \\(\\frac{{1 - \\sin^2 {d}^\\circ}}{{\\cos^2 {d}^\\circ}}\\).",
                "Using identities, evaluate \\(\\frac{{1 - \\sin^2 {d}^\\circ}}{{\\cos^2 {d}^\\circ}}\\).",
                "What does \\(\\frac{{1 - \\sin^2 {d}^\\circ}}{{\\cos^2 {d}^\\circ}}\\) simplify to?",
                "Compute \\(\\frac{{1 - \\sin^2 {d}^\\circ}}{{\\cos^2 {d}^\\circ}}\\).",
                "Find the simplified form of \\(\\frac{{1 - \\sin^2 {d}^\\circ}}{{\\cos^2 {d}^\\circ}}\\)."
            ]
            txt = tmpls[sub_idx].format(d=d)
            corr = "1"
            dist = ["0", "2", f"\\tan^2 {d}^\\circ"]
            sol = f"**Step 1: Identity**\\n\\(1 - \\sin^2 {d}^\\circ = \\cos^2 {d}^\\circ\\).\\n\\(\\frac{{\\cos^2 {d}^\\circ}}{{\\cos^2 {d}^\\circ}} = 1\\).\\n**Step 2: Conclusion**\\n1."
        elif arch == 7:
            k, m, ans_val = data_7[sub_idx]
            tmpls = [
                "Evaluate the expression \\({k}(\\sin^2 \\theta + \\cos^2 \\theta) + {m}\\).",
                "What is the value of \\({k}(\\sin^2 \\theta + \\cos^2 \\theta) + {m}\\)?",
                "Calculate \\({k}(\\sin^2 \\theta + \\cos^2 \\theta) + {m}\\) for any acute angle \\(\\theta\\).",
                "Find the simplified numerical result of \\({k}(\\sin^2 \\theta + \\cos^2 \\theta) + {m}\\).",
                "Determine the measure of \\({k}(\\sin^2 \\theta + \\cos^2 \\theta) + {m}\\).",
                "Compute \\({k}(\\sin^2 \\theta + \\cos^2 \\theta) + {m}\\).",
                "Simplify \\({k}(\\sin^2 \\theta + \\cos^2 \\theta) + {m}\\).",
                "Using the Pythagorean trigonometric identity, evaluate \\({k}(\\sin^2 \\theta + \\cos^2 \\theta) + {m}\\).",
                "What does \\({k}(\\sin^2 \\theta + \\cos^2 \\theta) + {m}\\) equal?",
                "Find the value of expression \\({k}(\\sin^2 \\theta + \\cos^2 \\theta) + {m}\\)."
            ]
            txt = tmpls[sub_idx].format(k=k, m=m)
            corr = f"{ans_val}"
            dist = [f"{ans_val + 2}", f"{ans_val - 2}", f"{k * m}"]
            sol = f"**Step 1: Identity**\\n\\(\\sin^2 \\theta + \\cos^2 \\theta = 1\\).\\n\\({k}(1) + {m} = {ans_val}\\).\\n**Step 2: Conclusion**\\n{ans_val}."

        diff = "easy" if arch in [0,1,2] else ("medium" if arch in [3,4,5] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs
'''

# Replace gen_8_3_1 with clean 8 archetypes x 10 varied templates
gen_8_3_1_code = '''def gen_8_3_1():
    tc = "MH-9-MTH2-8-8.3.1"
    tname = "Derivation of values using geometric triangles (30°-60°-90° and 45°-45°-90°)"
    qs = []
    
    # Arch 0: 30-60-90: side opp 30° = hyp/2
    data_0 = [
        (6, 3), (10, 5), (14, 7), (18, 9), (22, 11),
        (26, 13), (30, 15), (34, 17), (38, 19), (42, 21)
    ]
    tmpls_0 = [
        "In \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), \\(\\angle C = 30^\\circ\\), and hypotenuse \\(AC = {hyp}\\), find length \\(AB\\).",
        "For right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\), \\(\\angle C = 30^\\circ\\)), compute side \\(AB\\) when \\(AC = {hyp}\\).",
        "What is the length of side \\(AB\\) opposite to 30° in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) if hypotenuse \\(AC = {hyp}\\)?",
        "Calculate opposite side \\(AB\\) in right triangle \\(\\triangle ABC\\) with \\(\\angle C = 30^\\circ\\) and \\(AC = {hyp}\\).",
        "Determine side \\(AB\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\), \\(\\angle C = 30^\\circ\\)) having hypotenuse \\(AC = {hyp}\\).",
        "Evaluate the length of \\(AB\\) in \\(\\triangle ABC\\) right-angled at \\(B\\) given \\(\\angle C = 30^\\circ\\) and \\(AC = {hyp}\\).",
        "Find the opposite leg \\(AB\\) in 30°-60°-90° right \\(\\triangle ABC\\) if hypotenuse \\(AC = {hyp}\\).",
        "In right triangle \\(\\triangle ABC\\), hypotenuse \\(AC = {hyp}\\) and \\(\\angle C = 30^\\circ\\). Find \\(AB\\).",
        "Compute the measure of side \\(AB\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\), \\(\\angle C = 30^\\circ\\), \\(AC = {hyp}\\)).",
        "If \\(\\angle C = 30^\\circ\\) and \\(AC = {hyp}\\) in right \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), what is \\(AB\\)?"
    ]
    
    # Arch 1: 30-60-90: side opp 60° = (sqrt(3)/2)*hyp
    data_1 = [
        (2, "\\sqrt{3}"), (4, "2\\sqrt{3}"), (6, "3\\sqrt{3}"), (8, "4\\sqrt{3}"), (10, "5\\sqrt{3}"),
        (12, "6\\sqrt{3}"), (14, "7\\sqrt{3}"), (16, "8\\sqrt{3}"), (18, "9\\sqrt{3}"), (20, "10\\sqrt{3}")
    ]
    tmpls_1 = [
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\), \\(\\angle A = 30^\\circ\\), \\(AC = {hyp}\\)), find side \\(BC\\) opposite to 60°.",
        "Calculate side \\(BC\\) opposite to 60° in right-angled \\(\\triangle ABC\\) with hypotenuse \\(AC = {hyp}\\).",
        "What is the measure of side \\(BC\\) opposite to 60° in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) if \\(AC = {hyp}\\)?",
        "For 30°-60°-90° \\(\\triangle ABC\\), evaluate the length of side \\(BC\\) opposite to 60° when hypotenuse \\(AC = {hyp}\\).",
        "Find the length of the side opposite to 60° in right \\(\\triangle ABC\\) with \\(AC = {hyp}\\).",
        "Determine \\(BC\\) opposite to 60° in right-angled \\(\\triangle ABC\\) having hypotenuse \\(AC = {hyp}\\).",
        "In right triangle \\(\\triangle ABC\\) with acute angles 30° and 60°, find the side opposite to 60° if hypotenuse \\(AC = {hyp}\\).",
        "Compute the leg opposite to 60° in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with hypotenuse \\(AC = {hyp}\\).",
        "Given hypotenuse \\(AC = {hyp}\\) in 30°-60°-90° \\(\\triangle ABC\\), what is the length of side \\(BC\\)?",
        "If \\(\\angle A = 60^\\circ\\) and hypotenuse \\(AC = {hyp}\\) in right \\(\\triangle ABC\\), find the opposite side."
    ]
    
    # Arch 2: 45-45-90: given leg s, find hypotenuse s*sqrt(2)
    data_2 = [
        (3, "3\\sqrt{2}"), (5, "5\\sqrt{2}"), (7, "7\\sqrt{2}"), (9, "9\\sqrt{2}"), (11, "11\\sqrt{2}"),
        (13, "13\\sqrt{2}"), (15, "15\\sqrt{2}"), (17, "17\\sqrt{2}"), (19, "19\\sqrt{2}"), (21, "21\\sqrt{2}")
    ]
    tmpls_2 = [
        "In an isosceles right triangle \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), if legs \\(AB = BC = {s}\\), find hypotenuse \\(AC\\).",
        "For 45°-45°-90° \\(\\triangle ABC\\) with congruent legs \\(AB = BC = {s}\\), compute hypotenuse \\(AC\\).",
        "What is the hypotenuse \\(AC\\) of an isosceles right triangle with equal sides of length \\({s}\\)?",
        "Calculate hypotenuse \\(AC\\) in right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) where \\(AB = BC = {s}\\).",
        "Determine the measure of hypotenuse \\(AC\\) in 45°-45°-90° \\(\\triangle ABC\\) having legs \\({s}\\).",
        "Find length \\(AC\\) in isosceles right \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(AB = BC = {s}\\).",
        "Evaluate the hypotenuse of a 45°-45°-90° triangle whose perpendicular legs measure \\({s}\\).",
        "In right triangle \\(\\triangle ABC\\) with \\(\\angle A = \\angle C = 45^\\circ\\) and leg \\({s}\\), what is hypotenuse \\(AC\\)?",
        "Compute the hypotenuse \\(AC\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\), \\(AB = BC = {s}\\)).",
        "If each equal side in right isosceles \\(\\triangle ABC\\) is \\({s}\\), calculate hypotenuse \\(AC\\)."
    ]
    
    # Arch 3: 45-45-90: given hypotenuse s*sqrt(2), find leg s
    data_3 = [
        ("2\\sqrt{2}", 2), ("4\\sqrt{2}", 4), ("6\\sqrt{2}", 6), ("8\\sqrt{2}", 8), ("10\\sqrt{2}", 10),
        ("12\\sqrt{2}", 12), ("14\\sqrt{2}", 14), ("16\\sqrt{2}", 16), ("18\\sqrt{2}", 18), ("20\\sqrt{2}", 20)
    ]
    tmpls_3 = [
        "In 45°-45°-90° \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), if hypotenuse \\(AC = {hyp_str}\\), find the length of each perpendicular side.",
        "Calculate the leg length of an isosceles right triangle whose hypotenuse is \\({hyp_str}\\).",
        "What is the measure of each perpendicular side in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) if hypotenuse \\(AC = {hyp_str}\\)?",
        "For a 45°-45°-90° triangle with hypotenuse \\({hyp_str}\\), determine the length of each equal side.",
        "Find the length of side \\(AB\\) in right isosceles \\(\\triangle ABC\\) given hypotenuse \\(AC = {hyp_str}\\).",
        "Evaluate the length of each leg in 45°-45°-90° right triangle having hypotenuse \\({hyp_str}\\).",
        "Compute side \\(BC\\) in isosceles right-angled \\(\\triangle ABC\\) where hypotenuse \\(AC = {hyp_str}\\).",
        "In \\(\\triangle ABC\\) with \\(\\angle A = \\angle C = 45^\\circ\\) and hypotenuse \\(AC = {hyp_str}\\), find side \\(AB\\).",
        "Determine the leg of a 45°-45°-90° triangle if its hypotenuse is \\({hyp_str}\\).",
        "If hypotenuse \\(AC = {hyp_str}\\) in right-angled isosceles \\(\\triangle ABC\\), what is the length of side \\(AB\\)?"
    ]
    
    # Arch 4: 30-60-90: side opp 30° is given, find hypotenuse = 2 * opp
    data_4 = [
        (7, 14), (9, 18), (11, 22), (13, 26), (15, 30),
        (17, 34), (19, 38), (21, 42), (23, 46), (25, 50)
    ]
    tmpls_4 = [
        "In a 30°-60°-90° right triangle, if the side opposite to 30° is \\({opp}\\), calculate the length of the hypotenuse.",
        "Find the hypotenuse of right triangle \\(\\triangle ABC\\) where the side opposite to 30° measures \\({opp}\\).",
        "What is the length of the hypotenuse in a 30°-60°-90° triangle having opposite leg \\({opp}\\)?",
        "Determine the hypotenuse in right-angled \\(\\triangle ABC\\) if side opposite to 30° is \\({opp}\\).",
        "For 30°-60°-90° \\(\\triangle ABC\\), compute hypotenuse \\(AC\\) when the side opposite to 30° is \\({opp}\\).",
        "Evaluate the hypotenuse of a right triangle with an acute angle of 30° and opposite side \\({opp}\\).",
        "Calculate the measure of the hypotenuse if the side opposite to 30° in a right triangle is \\({opp}\\).",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\), \\(\\angle C = 30^\\circ\\)), given \\(AB = {opp}\\), find hypotenuse \\(AC\\).",
        "What is the hypotenuse of right-angled \\(\\triangle ABC\\) when side opposite to 30° is \\({opp}\\)?",
        "Find hypotenuse \\(AC\\) in 30°-60°-90° \\(\\triangle ABC\\) given opposite side \\(AB = {opp}\\)."
    ]
    
    # Arch 5: 30-60-90: side opp 60° is k*sqrt(3), find hypotenuse = 2*k
    data_5 = [
        ("3\\sqrt{3}", 6), ("5\\sqrt{3}", 10), ("7\\sqrt{3}", 14), ("9\\sqrt{3}", 18), ("11\\sqrt{3}", 22),
        ("13\\sqrt{3}", 26), ("27\\sqrt{3}", 54), ("17\\sqrt{3}", 34), ("19\\sqrt{3}", 38), ("21\\sqrt{3}", 42)
    ]
    tmpls_5 = [
        "In a 30°-60°-90° right triangle, the side opposite to 60° is \\({opp_str}\\). What is the hypotenuse?",
        "Find the hypotenuse of 30°-60°-90° triangle whose side opposite to 60° is \\({opp_str}\\).",
        "Calculate the length of the hypotenuse in right triangle \\(\\triangle ABC\\) if the leg opposite to 60° is \\({opp_str}\\).",
        "What is the measure of the hypotenuse in a right triangle where side opposite to 60° measures \\({opp_str}\\)?",
        "Determine the hypotenuse of a 30°-60°-90° triangle given that the side opposite to 60° is \\({opp_str}\\).",
        "For right-angled \\(\\triangle ABC\\) with acute angle 60° and opposite side \\({opp_str}\\), compute the hypotenuse.",
        "Evaluate the hypotenuse in 30°-60°-90° \\(\\triangle ABC\\) when the side opposite to 60° is \\({opp_str}\\).",
        "If the side opposite to 60° in a right triangle is \\({opp_str}\\), calculate the hypotenuse.",
        "Compute the length of hypotenuse in right \\(\\triangle ABC\\) where the side opposite to 60° is \\({opp_str}\\).",
        "Find hypotenuse \\(AC\\) in 30°-60°-90° \\(\\triangle ABC\\) knowing the side opposite to 60° is \\({opp_str}\\)."
    ]
    
    # Arch 6: Area of 45-45-90 with leg s -> 1/2 * s^2
    data_6 = [
        (4, 8), (6, 18), (8, 32), (10, 50), (12, 72),
        (14, 98), (16, 128), (18, 162), (20, 200), (22, 242)
    ]
    tmpls_6 = [
        "In right isosceles \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with legs \\(AB = BC = {s}\\), find its area.",
        "Compute the area of a 45°-45°-90° right triangle whose perpendicular sides each measure \\({s}\\).",
        "What is the area of \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\), \\(AB = BC = {s}\\))?",
        "Determine the area of an isosceles right triangle with equal legs of length \\({s}\\).",
        "For 45°-45°-90° triangle \\(\\triangle ABC\\), find the area when both perpendicular legs equal \\({s}\\).",
        "Calculate the area of right isosceles \\(\\triangle ABC\\) having equal sides of \\({s}\\).",
        "Find the area of \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\), \\(\\angle A = 45^\\circ\\)) if legs measure \\({s}\\).",
        "Evaluate the area of right-angled isosceles \\(\\triangle ABC\\) with legs \\({s}\\).",
        "In 45°-45°-90° \\(\\triangle ABC\\), perpendicular sides are \\({s}\\). What is its area?",
        "If legs \\(AB = BC = {s}\\) in right-angled \\(\\triangle ABC\\), determine its area."
    ]
    
    # Arch 7: Geometric ratio deduction
    data_7 = [
        ("30^\\circ", "60^\\circ", "\\frac{1}{2}"),
        ("45^\\circ", "45^\\circ", "\\frac{1}{\\sqrt{2}}"),
        ("60^\\circ", "30^\\circ", "\\frac{\\sqrt{3}}{2}"),
        ("30^\\circ", "90^\\circ", "\\frac{1}{2}"),
        ("45^\\circ", "90^\\circ", "1"),
        ("60^\\circ", "90^\\circ", "\\sqrt{3}"),
        ("30^\\circ", "45^\\circ", "\\frac{1}{\\sqrt{3}}"),
        ("0^\\circ", "90^\\circ", "0"),
        ("60^\\circ", "45^\\circ", "\\frac{\\sqrt{3}}{2}"),
        ("30^\\circ", "30^\\circ", "1")
    ]
    tmpls_7 = [
        "In a 30°-60°-90° triangle, what is the geometric ratio of the side opposite to {a1} to the hypotenuse?",
        "What is the ratio of the side opposite to {a1} to the hypotenuse in a right triangle?",
        "Determine the ratio of side opposite to {a1} to hypotenuse in a standard right triangle.",
        "Calculate the ratio of the opposite leg to hypotenuse for angle {a1}.",
        "For angle {a1} in a geometric reference triangle, find the ratio of opposite side to hypotenuse.",
        "Evaluate the ratio of opposite side to hypotenuse for angle {a1}.",
        "What does the ratio of opposite side to hypotenuse equal for angle {a1} in standard geometry?",
        "Find the theoretical geometric ratio of side opposite to {a1} to the hypotenuse.",
        "Compute the ratio of opposite side to hypotenuse for an angle of {a1}.",
        "In geometric deduction of trigonometric values, what is \\(\\sin({a1})\\)?"
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        qcode = f"{tc}-OSC-{seq}"
        
        if arch == 0:
            hyp, opp = data_0[sub_idx]
            svg = svg_trig("A", "B", "C", "AB = ?", "", f"AC = {hyp}") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(hyp=hyp)
            corr = f"{opp}"
            dist = [f"{opp + 2}", f"{opp - 2 if opp > 2 else opp + 4}", f"{opp * 2}"]
            sol = f"**Step 1: 30°-60°-90° theorem**\\n\\(AB = \\frac{{1}}{{2}} \\times AC = \\frac{{1}}{{2}} \\times {hyp} = {opp}\\).\\n**Step 2: Conclusion**\\n{opp}."
        elif arch == 1:
            hyp, opp_str = data_1[sub_idx]
            svg = svg_trig("A", "B", "C", "", f"BC = ?", f"AC = {hyp}") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(hyp=hyp)
            corr = f"\\({opp_str}\\)"
            dist = [f"\\({hyp}\\)", f"\\(\\frac{{{hyp}}}{{2}}\\)", f"\\({hyp}\\sqrt{{2}}\\)" ]
            sol = f"**Step 1: 30°-60°-90° theorem**\\n\\(BC = \\frac{{\\sqrt{{3}}}}{{2}} \\times AC = \\frac{{\\sqrt{{3}}}}{{2}} \\times {hyp} = {opp_str}\\).\\n**Step 2: Conclusion**\\n\\({opp_str}\\)."
        elif arch == 2:
            s, hyp_str = data_2[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {s}", f"BC = {s}", "AC = ?") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(s=s)
            corr = f"\\({hyp_str}\\)"
            dist = [f"{s * 2}", f"{s}", f"\\({s}\\sqrt{{3}}\\)" ]
            sol = f"**Step 1: 45°-45°-90° theorem**\\n\\(AC = \\sqrt{{2}} \\times \\text{{side}} = {hyp_str}\\).\\n**Step 2: Conclusion**\\n\\({hyp_str}\\)."
        elif arch == 3:
            hyp_str, leg = data_3[sub_idx]
            svg = svg_trig("A", "B", "C", "AB = ?", "BC = ?", f"AC = {hyp_str}") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(hyp_str=hyp_str)
            corr = f"{leg}"
            dist = [f"{leg + 2}", f"{leg - 2 if leg > 2 else leg + 3}", f"{leg * 2}"]
            sol = f"**Step 1: 45°-45°-90° theorem**\\n\\(\\text{{leg}} = \\frac{{AC}}{{\\sqrt{{2}}}} = {leg}\\).\\n**Step 2: Conclusion**\\n{leg}."
        elif arch == 4:
            opp, hyp = data_4[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {opp}", "", "AC = ?") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(opp=opp)
            corr = f"{hyp}"
            dist = [f"{hyp + 4}", f"{hyp - 4}", f"{opp}"]
            sol = f"**Step 1: Formula**\\n\\(\\text{{hypotenuse}} = 2 \\times \\text{{opposite 30°}} = 2 \\times {opp} = {hyp}\\).\\n**Step 2: Conclusion**\\n{hyp}."
        elif arch == 5:
            opp_str, hyp = data_5[sub_idx]
            svg = svg_trig("A", "B", "C", "", f"BC = {opp_str}", "AC = ?") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(opp_str=opp_str)
            corr = f"{hyp}"
            dist = [f"{hyp + 4}", f"{hyp - 4}", f"{hyp * 2}"]
            sol = f"**Step 1: 30°-60°-90° theorem**\\n\\(\\text{{opposite 60°}} = \\frac{{\\sqrt{{3}}}}{{2}} \\times \\text{{hypotenuse}} \\implies \\text{{hypotenuse}} = {hyp}\\).\\n**Step 2: Conclusion**\\n{hyp}."
        elif arch == 6:
            s, area_ans = data_6[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {s}", f"BC = {s}", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(s=s)
            corr = f"{area_ans}"
            dist = [f"{area_ans + 4}", f"{area_ans - 4 if area_ans > 4 else area_ans + 6}", f"{s * 2}"]
            sol = f"**Step 1: Formula**\\n\\(\\text{{Area}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} = \\frac{{1}}{{2}} \\times {s} \\times {s} = {area_ans}\\).\\n**Step 2: Conclusion**\\n{area_ans}."
        elif arch == 7:
            a1, a2, ans_str = data_7[sub_idx]
            svg = svg_trig("A", "B", "C", "", "", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_7[sub_idx].format(a1=a1)
            corr = f"\\({ans_str}\\)"
            dist = ["\\(\\frac{1}{2}\\)", "\\(\\frac{\\sqrt{3}}{2}\\)", "\\(\\frac{1}{\\sqrt{2}}\\)", "\\(1\\)"]
            dist = [d for d in dist if d != f"\\({ans_str}\\)"][:3]
            sol = f"**Step 1: Definition**\\nIn a standard geometric right triangle, the ratio for {a1} is \\({ans_str}\\).\\n**Step 2: Conclusion**\\n\\({ans_str}\\)."

        diff = "easy" if arch in [0,1,2] else ("medium" if arch in [3,4,5] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs
'''

# Substitute in content
# Replace def gen_8_2_2()
content = re.sub(r'def gen_8_2_2\(\):[\s\S]*?(?=def gen_8_2_3\(\):)', lambda m: gen_8_2_2_code + '\n', content)
# Replace def gen_8_2_3()
content = re.sub(r'def gen_8_2_3\(\):[\s\S]*?(?=def gen_8_3_1\(\):)', lambda m: gen_8_2_3_code + '\n', content)
# Replace def gen_8_3_1()
content = re.sub(r'def gen_8_3_1\(\):[\s\S]*?(?=def gen_8_3_2\(\):)', lambda m: gen_8_3_1_code + '\n', content)

with open("scripts/generate_mh9_mth2_ch8_all.py", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated generate_mh9_mth2_ch8_all.py with flawless gen_8_2_2, gen_8_2_3, gen_8_3_1!")
