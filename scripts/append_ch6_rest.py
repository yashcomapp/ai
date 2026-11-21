# scripts/append_ch6_rest.py
import re

code_rest = '''
# -----------------------------------------------------------------------------
# 6.1.2: Congruent chords are equidistant from centre
# -----------------------------------------------------------------------------
def gen_6_1_2():
    tc = "MH-9-MTH2-6-6.1.2"
    tname = "Congruent chords are equidistant from centre theorem and converse"
    qs = []
    
    # Arch 0: Chord AB = Chord CD, dist OM = d -> dist ON = d
    data_0 = [
        (4, 10), (5, 12), (6, 14), (7, 16), (8, 18),
        (9, 20), (10, 24), (11, 26), (12, 28), (15, 30)
    ]
    tmpls_0 = [
        "In a circle with centre \\(O\\), congruent chords \\(AB\\) and \\(CD\\) have lengths {c}\\text{{ cm}}. If the perpendicular distance \\(OM\\) from \\(O\\) to \\(AB\\) is {d}\\text{{ cm}}, find distance \\(ON\\) to chord \\(CD\\).",
        "Chords \\(AB\\) and \\(CD\\) of circle \\(O\\) are equal in length. If distance \\(OM\\) from centre \\(O\\) to \\(AB\\) is {d}\\text{{ cm}}, what is the perpendicular distance \\(ON\\) to \\(CD\\)?",
        "Two congruent chords \\(AB = CD\\) are drawn in a circle of radius \\(r\\). Given \\(OM \\perp AB\\) with \\(OM = {d}\\text{{ cm}}\\), compute the length of \\(ON\\) (\\(ON \\perp CD\\)).",
        "What is the perpendicular distance \\(ON\\) to chord \\(CD\\) if chord \\(AB = CD\\) and \\(OM = {d}\\text{{ cm}}\\) (perpendicular from centre \\(O\\) to \\(AB\\))?",
        "By the equidistant chord theorem, if chord \\(AB \\cong CD\\) and distance \\(OM = {d}\\text{{ cm}}\\), determine distance \\(ON\\).",
        "In circle \\(O\\), chord \\(AB\\) and chord \\(CD\\) are congruent. If \\(OM = {d}\\text{{ cm}}\\) is the distance of \\(AB\\) from \\(O\\), evaluate distance \\(ON\\).",
        "Find the perpendicular distance from centre \\(O\\) to chord \\(CD\\) knowing that chord \\(CD = AB\\) and \\(OM = {d}\\text{{ cm}}\\).",
        "Calculate distance \\(ON\\) to chord \\(CD\\) in circle \\(O\\) where chord \\(AB = CD\\) and \\(OM = {d}\\text{{ cm}}\\).",
        "Given congruent chords \\(AB\\) and \\(CD\\) in circle \\(O\\), if \\(OM = {d}\\text{{ cm}}\\) (\\(OM \\perp AB\\)), what is \\(ON\\) (\\(ON \\perp CD\\))?",
        "If chord \\(AB\\) is congruent to chord \\(CD\\) and perpendicular from centre to \\(AB\\) is {d}\\text{{ cm}}, find the perpendicular distance to \\(CD\\)."
    ]
    
    # Arch 1: Equidistant chords OM = ON = d -> Chord AB = Chord CD = c
    data_1 = [
        (3, 8), (4, 10), (5, 14), (6, 16), (7, 18),
        (8, 22), (9, 24), (10, 26), (12, 32), (14, 36)
    ]
    tmpls_1 = [
        "In circle \\(O\\), perpendiculars \\(OM\\) and \\(ON\\) to chords \\(AB\\) and \\(CD\\) are equal: \\(OM = ON = {d}\\text{{ cm}}\\). If chord \\(AB = {c}\\text{{ cm}}\\), find the length of chord \\(CD\\).",
        "Chords \\(AB\\) and \\(CD\\) in circle \\(O\\) are equidistant from centre \\(O\\). If chord \\(AB = {c}\\text{{ cm}}\\), calculate length \\(CD\\).",
        "What is the length of chord \\(CD\\) if it is at the same distance from centre \\(O\\) as chord \\(AB = {c}\\text{{ cm}}\\) in circle \\(O\\)?",
        "Two chords \\(AB\\) and \\(CD\\) are equidistant from the centre of a circle. If \\(AB = {c}\\text{{ cm}}\\), determine the measure of chord \\(CD\\).",
        "By the converse theorem, chords equidistant from centre \\(O\\) are congruent. If \\(OM = ON\\) and \\(AB = {c}\\text{{ cm}}\\), find \\(CD\\).",
        "Evaluate the length of chord \\(CD\\) in circle \\(O\\) knowing \\(AB = {c}\\text{{ cm}}\\) and both chords are at distance {d}\\text{{ cm}} from centre.",
        "Find chord length \\(CD\\) in a circle where chords \\(AB\\) and \\(CD\\) are at equal perpendicular distances from centre \\(O\\) and \\(AB = {c}\\text{{ cm}}\\).",
        "In circle \\(O\\), \\(OM \\perp AB\\), \\(ON \\perp CD\\), and \\(OM = ON\\). Given \\(AB = {c}\\text{{ cm}}\\), compute \\(CD\\).",
        "Calculate the measure of chord \\(CD\\) if chords \\(AB\\) and \\(CD\\) are equidistant from centre \\(O\\) and \\(AB = {c}\\text{{ cm}}\\).",
        "Given that chords \\(AB\\) and \\(CD\\) are equidistant from centre \\(O\\) and \\(AB = {c}\\text{{ cm}}\\), what is \\(CD\\)?"
    ]
    
    # Arch 2: Sum of two congruent chords: AB + CD = 2 * c
    data_2 = [
        (6, 12), (9, 18), (11, 22), (13, 26), (15, 30),
        (17, 34), (19, 38), (21, 42), (23, 46), (25, 50)
    ]
    tmpls_2 = [
        "In a circle with centre \\(O\\), chords \\(AB\\) and \\(CD\\) are equidistant from \\(O\\). If \\(AB = {c}\\text{{ cm}}\\), find the sum of their lengths \\(AB + CD\\).",
        "Two congruent chords \\(AB\\) and \\(CD\\) each measure \\({c}\\text{{ cm}}\\) in circle \\(O\\). Calculate \\(AB + CD\\).",
        "What is the total combined length \\(AB + CD\\) of two chords equidistant from centre \\(O\\) if \\(AB = {c}\\text{{ cm}}\\)?" ,
        "Compute \\(AB + CD\\) in circle \\(O\\) where \\(AB \\cong CD\\) and chord \\(AB = {c}\\text{{ cm}}\\).",
        "Determine \\(AB + CD\\) for two equal chords in circle \\(O\\) having \\(AB = {c}\\text{{ cm}}\\).",
        "Evaluate \\(AB + CD\\) in circle \\(O\\) given that chords \\(AB\\) and \\(CD\\) are congruent and \\(AB = {c}\\text{{ cm}}\\).",
        "If \\(OM = ON\\) for chords \\(AB\\) and \\(CD\\) in circle \\(O\\), and \\(AB = {c}\\text{{ cm}}\\), find \\(AB + CD\\).",
        "Find the sum \\(AB + CD\\) of two chords in a circle equidistant from centre \\(O\\) given \\(AB = {c}\\text{{ cm}}\\).",
        "Calculate the combined measure \\(AB + CD\\) of two congruent chords \\(AB = CD = {c}\\text{{ cm}}\\).",
        "In circle \\(O\\), chords \\(AB\\) and \\(CD\\) are equidistant from centre. If \\(AB = {c}\\text{{ cm}}\\), what is \\(AB + CD\\)?"
    ]
    
    # Arch 3: Central angle of congruent chords: angle AOB = angle COD
    data_3 = [
        (40, 40), (50, 50), (65, 65), (75, 75), (80, 80),
        (95, 95), (100, 100), (110, 110), (120, 120), (130, 130)
    ]
    tmpls_3 = [
        "In a circle with centre \\(O\\), congruent chords \\(AB\\) and \\(CD\\) subtend angles at the centre. If \\(\\angle AOB = {deg}^\\circ\\), find \\(\\angle COD\\).",
        "Chords \\(AB\\) and \\(CD\\) in circle \\(O\\) are equal in length. If central angle \\(\\angle AOB = {deg}^\\circ\\), what is \\(\\angle COD\\)?",
        "What is the central angle \\(\\angle COD\\) subtended by chord \\(CD\\) if chord \\(CD \\cong AB\\) and \\(\\angle AOB = {deg}^\\circ\\)?",
        "Congruent chords of a circle subtend equal angles at the centre. If \\(\\angle AOB = {deg}^\\circ\\), calculate \\(\\angle COD\\).",
        "Determine the measure of \\(\\angle COD\\) in circle \\(O\\) given \\(AB = CD\\) and \\(\\angle AOB = {deg}^\\circ\\).",
        "Evaluate \\(\\angle COD\\) in circle \\(O\\) knowing chords \\(AB\\) and \\(CD\\) are congruent and \\(\\angle AOB = {deg}^\\circ\\).",
        "Compute central angle \\(\\angle COD\\) subtended by chord \\(CD\\) when \\(CD = AB\\) and \\(\\angle AOB = {deg}^\\circ\\).",
        "Find \\(\\angle COD\\) for chord \\(CD\\) in circle \\(O\\) given chord \\(AB = CD\\) and \\(\\angle AOB = {deg}^\\circ\\).",
        "If chord \\(AB = CD\\) in circle \\(O\\) and \\(\\angle AOB = {deg}^\\circ\\), calculate \\(\\angle COD\\).",
        "In circle with centre \\(O\\), congruent chords \\(AB\\) and \\(CD\\) have \\(\\angle AOB = {deg}^\\circ\\). Find \\(\\angle COD\\)."
    ]
    
    # Arch 4: Right angle between perpendiculars OM and ON when chords are perpendicular
    data_4 = [
        (45, 135), (55, 125), (65, 115), (70, 110), (75, 105),
        (85, 95), (35, 145), (25, 155), (60, 120), (50, 130)
    ]
    tmpls_4 = [
        "In a cyclic quadrilateral or intersecting chords configuration with \\(OM \\perp AB\\) and \\(ON \\perp CD\\), if \\(\\angle MON = {deg}^\\circ\\), find the supplementary angle \\(180^\\circ - {deg}^\\circ\\).",
        "For perpendicular segments \\(OM\\) and \\(ON\\) to chords in circle \\(O\\), calculate the supplement of \\(\\angle MON = {deg}^\\circ\\).",
        "What is the supplementary angle to central angle \\(\\angle MON = {deg}^\\circ\\) between perpendicular bisectors?",
        "Determine the angle \\(180^\\circ - \\angle MON\\) when \\(\\angle MON = {deg}^\\circ\\) in circle \\(O\\).",
        "Compute the supplementary measure to \\(\\angle MON = {deg}^\\circ\\) formed by radii perpendiculars.",
        "Evaluate \\(180^\\circ - {deg}^\\circ\\) in the context of cyclic quadrilateral \\(OMPN\\) where \\(\\angle MON = {deg}^\\circ\\).",
        "Find the measure of angle \\(\\angle MPN\\) opposite to \\(\\angle MON = {deg}^\\circ\\) in quadrilateral \\(OMPN\\) (\\(\\angle M = \\angle N = 90^\\circ\\)).",
        "In quadrilateral \\(OMPN\\) with \\(\\angle M = \\angle N = 90^\\circ\\) and \\(\\angle MON = {deg}^\\circ\\), calculate \\(\\angle MPN\\).",
        "Calculate \\(\\angle MPN\\) in quadrilateral \\(OMPN\\) (\\(\\angle OMP = \\angle ONP = 90^\\circ\\), \\(\\angle MON = {deg}^\\circ\\)).",
        "If \\(\\angle MON = {deg}^\\circ\\) in quadrilateral \\(OMPN\\) where \\(OM \\perp AB\\) and \\(ON \\perp CD\\), what is \\(\\angle MPN\\)?"
    ]
    
    # Arch 5: Radius r from chord AB = c and distance d
    data_5 = [
        (12, 8, 10), (16, 6, 10), (24, 5, 13), (30, 8, 17), (48, 7, 25),
        (20, 24, 26), (32, 24, 30), (40, 15, 25), (48, 20, 26), (60, 11, 61)
    ]
    tmpls_5 = [
        "Two congruent chords of length {c}\\text{{ cm}} are each at a distance of {d}\\text{{ cm}} from centre \\(O\\). Find the radius of the circle.",
        "In a circle, congruent chords each measuring {c}\\text{{ cm}} are situated {d}\\text{{ cm}} from centre \\(O\\). What is the radius of the circle?",
        "Calculate the radius of circle \\(O\\) containing two equal chords of {c}\\text{{ cm}} each at perpendicular distance {d}\\text{{ cm}} from \\(O\\).",
        "What is the radius of a circle in which two chords of length {c}\\text{{ cm}} are equidistant ({d}\\text{{ cm}}) from the centre?",
        "Determine the radius of circle \\(O\\) if two congruent chords of {c}\\text{{ cm}} have distance {d}\\text{{ cm}} from \\(O\\).",
        "Evaluate the radius of the circle containing equal chords \\(AB = CD = {c}\\text{{ cm}}\\) with distance \\(OM = ON = {d}\\text{{ cm}}\\).",
        "Find the radius of a circle where two equidistant chords measure {c}\\text{{ cm}} and are {d}\\text{{ cm}} from centre \\(O\\).",
        "Compute the circle radius given that chords \\(AB = CD = {c}\\text{{ cm}}\\) are at distance \\(OM = ON = {d}\\text{{ cm}}\\).",
        "In circle \\(O\\), chords \\(AB = CD = {c}\\text{{ cm}}\\) lie {d}\\text{{ cm}} from \\(O\\). Calculate radius \\(OA\\).",
        "If chords \\(AB = CD = {c}\\text{{ cm}}\\) are at distance {d}\\text{{ cm}} from centre \\(O\\), what is the length of the radius?"
    ]
    
    # Arch 6: Half-chord of congruent chords: AM = c / 2
    data_6 = [
        (10, 5), (14, 7), (18, 9), (22, 11), (26, 13),
        (34, 17), (38, 19), (46, 23), (54, 27), (62, 31)
    ]
    tmpls_6 = [
        "In circle \\(O\\), congruent chords \\(AB\\) and \\(CD\\) have length {c}\\text{{ cm}}. What is the length of segment \\(AM\\) if \\(OM \\perp AB\\)?",
        "If \\(AB = CD = {c}\\text{{ cm}}\\) in circle \\(O\\) and \\(OM \\perp AB\\), find length \\(AM\\).",
        "Perpendicular from centre \\(O\\) to chord \\(AB = {c}\\text{{ cm}}\\) intersects \\(AB\\) at \\(M\\). Calculate \\(AM\\).",
        "What is the measure of half-chord \\(AM\\) when \\(AB = {c}\\text{{ cm}}\\) is congruent to \\(CD\\)?",
        "Determine the length of segment \\(AM\\) in circle \\(O\\) where \\(OM \\perp AB\\) and chord \\(AB = {c}\\text{{ cm}}\\).",
        "Evaluate \\(AM\\) for chord \\(AB = {c}\\text{{ cm}}\\) (congruent to \\(CD\\)) with \\(OM \\perp AB\\).",
        "Find length \\(AM\\) in circle \\(O\\) given chord \\(AB = {c}\\text{{ cm}}\\) and perpendicular \\(OM\\).",
        "Compute segment \\(AM\\) for chord \\(AB = {c}\\text{{ cm}}\\) bisected by \\(OM \\perp AB\\).",
        "In circle \\(O\\), chord \\(AB = {c}\\text{{ cm}}\\) is bisected at \\(M\\). Find \\(AM\\).",
        "Calculate the measure of \\(AM\\) given \\(OM \\perp AB\\) and \\(AB = {c}\\text{{ cm}}\\)."
    ]
    
    # Arch 7: Distance ratio OM : ON for congruent chords = 1
    data_7 = [
        (15, 1), (25, 1), (35, 1), (45, 1), (55, 1),
        (65, 1), (75, 1), (85, 1), (95, 1), (105, 1)
    ]
    tmpls_7 = [
        "If chords \\(AB\\) and \\(CD\\) in circle \\(O\\) are congruent, what is the ratio of their perpendicular distances \\(\\frac{{OM}}{{ON}}\\)?",
        "For congruent chords \\(AB \\cong CD\\) in circle \\(O\\), find the numerical ratio \\(\\frac{{OM}}{{ON}}\\).",
        "What is the value of the ratio \\(OM : ON\\) of perpendicular distances from centre to two congruent chords \\(AB\\) and \\(CD\\)?",
        "Calculate the ratio \\(\\frac{{OM}}{{ON}}\\) where \\(OM\\) and \\(ON\\) are distances of congruent chords \\(AB\\) and \\(CD\\) from centre \\(O\\).",
        "Determine the ratio of distances from centre \\(O\\) to two equal chords in a circle.",
        "In circle \\(O\\), if chord \\(AB = CD\\), evaluate the ratio \\(\\frac{{OM}}{{ON}}\\).",
        "Find the ratio of distances \\(OM\\) to \\(ON\\) for two congruent chords in circle \\(O\\).",
        "What does the ratio \\(\\frac{{OM}}{{ON}}\\) equal if chords \\(AB\\) and \\(CD\\) are equal?",
        "Compute the ratio \\(OM : ON\\) for two chords \\(AB\\) and \\(CD\\) of equal length in circle \\(O\\).",
        "If chord \\(AB\\) equals chord \\(CD\\) in a circle, what is the quotient \\(\\frac{{OM}}{{ON}}\\)?"
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        qcode = f"{tc}-OSC-{seq}"
        
        if arch == 0:
            d, c = data_0[sub_idx]
            svg = svg_circle_chord(f"OM = {d}", "ON = ?", f"Chords = {c}") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(d=d, c=c)
            corr = f"{d}\\text{{ cm}}"
            dist = [f"{d + 2}\\text{{ cm}}", f"{d - 2 if d > 2 else d + 4}\\text{{ cm}}", f"{c // 2}\\text{{ cm}}"]
            sol = f"**Step 1: Equidistant chord theorem**\\nCongruent chords of a circle are equidistant from the centre.\\nSince chord \\(AB \\cong CD\\), distance \\(ON = OM = {d}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{d} cm."
        elif arch == 1:
            d, c = data_1[sub_idx]
            svg = svg_circle_chord(f"OM = ON = {d}", "", f"AB = {c}") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(d=d, c=c)
            corr = f"{c}\\text{{ cm}}"
            dist = [f"{c + 4}\\text{{ cm}}", f"{c - 4}\\text{{ cm}}", f"{d * 2}\\text{{ cm}}"]
            sol = f"**Step 1: Converse theorem**\\nChords of a circle that are equidistant from the centre are congruent.\\nSince \\(OM = ON\\), chord \\(CD = AB = {c}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{c} cm."
        elif arch == 2:
            c, ans_sum = data_2[sub_idx]
            svg = svg_circle_chord("", "", f"AB = CD = {c}") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(c=c)
            corr = f"{ans_sum}\\text{{ cm}}"
            dist = [f"{ans_sum + 4}\\text{{ cm}}", f"{ans_sum - 4}\\text{{ cm}}", f"{c}\\text{{ cm}}"]
            sol = f"**Step 1: Sum of congruent chords**\\nSince \\(AB = CD = {c}\\text{{ cm}}\\):\\n\\(AB + CD = {c} + {c} = {ans_sum}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_sum} cm."
        elif arch == 3:
            deg, ans_deg = data_3[sub_idx]
            svg = svg_circle_chord("", f"\\angle AOB = {deg}^\\circ", "AB = CD") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(deg=deg)
            corr = f"{ans_deg}^\\circ"
            dist = [f"{ans_deg + 15}^\\circ", f"{ans_deg - 15 if ans_deg > 15 else ans_deg + 20}^\\circ", f"{180 - ans_deg}^\\circ"]
            sol = f"**Step 1: Central angles theorem**\\nCongruent chords subtend equal angles at the centre of the circle.\\n\\(\\angle COD = \\angle AOB = {ans_deg}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_deg}°."
        elif arch == 4:
            deg, ans_supp = data_4[sub_idx]
            svg = svg_circle_chord("", f"\\angle MON = {deg}^\\circ", "") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(deg=deg)
            corr = f"{ans_supp}^\\circ"
            dist = [f"{ans_supp + 10}^\\circ", f"{ans_supp - 10 if ans_supp > 10 else ans_supp + 15}^\\circ", f"{deg}^\\circ"]
            sol = f"**Step 1: Opposite angles in cyclic quadrilateral**\\nIn quadrilateral \\(OMPN\\), \\(\\angle M = \\angle N = 90^\\circ\\).\\n\\(\\angle MPN = 180^\\circ - \\angle MON = 180^\\circ - {deg}^\\circ = {ans_supp}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_supp}°."
        elif arch == 5:
            c, d, ans_r = data_5[sub_idx]
            svg = svg_circle_chord("r = ?", f"OM = {d}", f"AB = {c}") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(c=c, d=d)
            corr = f"{ans_r}\\text{{ cm}}"
            dist = [f"{ans_r + 2}\\text{{ cm}}", f"{ans_r - 2}\\text{{ cm}}", f"{c // 2 + d}\\text{{ cm}}"]
            sol = f"**Step 1: Radius calculation**\\n\\(MB = \\frac{{AB}}{{2}} = \\frac{{{c}}}{{2}} = {c // 2}\\text{{ cm}}\\).\\n\\(r = \\sqrt{{OM^2 + MB^2}} = \\sqrt{{{d}^2 + {c//2}^2}} = {ans_r}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_r} cm."
        elif arch == 6:
            c, ans_half = data_6[sub_idx]
            svg = svg_circle_chord("", "OM \\perp AB", f"AB = {c}") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(c=c)
            corr = f"{ans_half}\\text{{ cm}}"
            dist = [f"{ans_half + 2}\\text{{ cm}}", f"{ans_half - 2}\\text{{ cm}}", f"{c}\\text{{ cm}}"]
            sol = f"**Step 1: Bisection of chord**\\nPerpendicular from centre to chord bisects the chord.\\n\\(AM = \\frac{{AB}}{{2}} = \\frac{{{c}}}{{2}} = {ans_half}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_half} cm."
        elif arch == 7:
            k, ans_ratio = data_7[sub_idx]
            svg = svg_circle_chord("", "", "AB \\cong CD") if has_fig else ""
            prefix = (svg + "\\n") if svg else ""
            txt = prefix + tmpls_7[sub_idx].format()
            corr = "1"
            dist = ["2", "\\frac{1}{2}", "0"]
            sol = f"**Step 1: Distance ratio**\\nSince congruent chords are equidistant from the centre, \\(OM = ON\\).\\nTherefore, \\(\\frac{{OM}}{{ON}} = 1\\).\\n**Step 2: Conclusion**\\n1."

        diff = "easy" if arch in [0,1,3] else ("medium" if arch in [2,6,7] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs
'''

with open("scripts/generate_flawless_ch6.py", "r", encoding="utf-8") as f:
    orig = f.read()

# Insert gen_6_1_2 before main
idx = orig.find("def main():")
new_content = orig[:idx] + code_rest + "\n" + orig[idx:]

# Update main to include gen_6_1_2
new_content = new_content.replace(
    '    qs.extend(q1)',
    '    qs.extend(q1)\n    print("Generating 6.1.2...")\n    q2 = gen_6_1_2()\n    print(f"Generated 6.1.2: {len(q2)} questions")\n    qs.extend(q2)'
)

with open("scripts/generate_flawless_ch6.py", "w", encoding="utf-8") as f:
    f.write(new_content)
print("Updated generate_flawless_ch6.py with 6.1.2!")
