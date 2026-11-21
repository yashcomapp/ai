# scripts/patch_perfect_ch8.py
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
        fallback = f"{corr} (Alt {counter})"
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
        "chapterNumber": 8,
        "chapter": "Trigonometry",
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

def svg_trig_triangle(v_top, v_rt, v_right, opp_lbl, adj_lbl, hyp_lbl, title):
    return (
        f'<svg width="240" height="200" viewBox="0 0 240 200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a;border-radius:8px;display:block;margin:12px auto;">'
        f'<polygon points="40,160 200,160 40,40" fill="none" stroke="#38bdf8" stroke-width="2"/>'
        f'<rect x="40" y="145" width="15" height="15" fill="none" stroke="#f43f5e" stroke-width="1.5"/>'
        f'<text x="25" y="40" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">{v_top}</text>'
        f'<text x="25" y="170" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">{v_rt}</text>'
        f'<text x="205" y="170" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">{v_right}</text>'
        f'<text x="15" y="105" fill="#f59e0b" font-size="10" font-family="sans-serif">{opp_lbl}</text>'
        f'<text x="110" y="180" fill="#f59e0b" font-size="10" font-family="sans-serif">{adj_lbl}</text>'
        f'<text x="130" y="95" fill="#10b981" font-size="10" font-family="sans-serif">{hyp_lbl}</text>'
        f'<text x="10" y="195" fill="#94a3b8" font-size="9" font-family="sans-serif">{title}</text>'
        f'</svg>'
    )

TRIPLES = [
    (3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (9, 40, 41),
    (12, 35, 37), (20, 21, 29), (11, 60, 61), (16, 63, 65), (28, 45, 53)
]

# ------------------------------------------------------------------------------
# 8.1.1: In right angled triangle: sin θ = Opposite / Hypotenuse
# ------------------------------------------------------------------------------
def generate_8_1_1():
    tc = "MH-9-MTH2-8-8.1.1"
    tname = "In right angled triangle: sin θ = Opposite / Hypotenuse"
    qs = []
    
    TEMPLATES = {
        0: [
            "In right-angled triangle \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), side \\(AB = {a}\\) and hypotenuse \\(AC = {c}\\). Find \\(\\sin C\\).",
            "For \\(\\triangle ABC\\) right-angled at \\(B\\), the side opposite to \\(\\angle C\\) is \\(AB = {a}\\) and hypotenuse \\(AC = {c}\\). What is \\(\\sin C\\)?",
            "Calculate \\(\\sin C\\) in \\(\\triangle ABC\\) where \\(\\angle B = 90^\\circ\\), \\(AB = {a}\\) and \\(AC = {c}\\).",
            "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), given \\(AB = {a}\\) and \\(AC = {c}\\), evaluate the ratio \\(\\sin C\\).",
            "Determine the sine ratio of acute angle \\(C\\) in \\(\\triangle ABC\\) where \\(\\angle B = 90^\\circ\\), \\(AB = {a}\\), and \\(AC = {c}\\).",
            "State the value of \\(\\sin C\\) in right-angled \\(\\triangle ABC\\) with perpendicular \\(AB = {a}\\) and hypotenuse \\(AC = {c}\\).",
            "In right triangle \\(\\triangle ABC\\) with right angle at \\(B\\), side \\(AB = {a}\\) and \\(AC = {c}\\). What is \\(\\sin C\\)?",
            "Find the ratio \\(\\sin C = \\frac{{\\text{{Opposite}}}}{{\\text{{Hypotenuse}}}}\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with \\(AB = {a}\\) and \\(AC = {c}\\).",
            "For the right-angled triangle \\(\\triangle ABC\\) having \\(\\angle B = 90^\\circ\\), \\(AB = {a}\\), and \\(AC = {c}\\), find \\(\\sin C\\).",
            "Compute the exact trigonometric value of \\(\\sin C\\) for \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\), \\(AB = {a}\\), \\(AC = {c}\\))."
        ],
        1: [
            "In right-angled \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), side \\(BC = {b}\\) and hypotenuse \\(AC = {c}\\). Find \\(\\sin A\\).",
            "What is \\(\\sin A\\) in \\(\\triangle ABC\\) right-angled at \\(B\\), where \\(BC = {b}\\) and \\(AC = {c}\\)?",
            "Calculate the sine of angle \\(A\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(BC = {b}\\) and \\(AC = {c}\\).",
            "Determine \\(\\sin A\\) for right-angled \\(\\triangle ABC\\) having \\(\\angle B = 90^\\circ\\), \\(BC = {b}\\), and \\(AC = {c}\\).",
            "In right triangle \\(\\triangle ABC\\) with right angle at \\(B\\), \\(BC = {b}\\) and \\(AC = {c}\\). What is \\(\\sin A\\)?",
            "Find the ratio representing \\(\\sin A\\) in \\(\\triangle ABC\\) where \\(\\angle B = 90^\\circ\\), \\(BC = {b}\\), and \\(AC = {c}\\).",
            "Evaluate \\(\\sin A\\) in right \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), given \\(BC = {b}\\) and \\(AC = {c}\\).",
            "State the value of \\(\\sin A\\) in \\(\\triangle ABC\\) where \\(\\angle B = 90^\\circ\\), \\(BC = {b}\\), and \\(AC = {c}\\).",
            "For right-angled triangle \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), given \\(BC = {b}\\) and \\(AC = {c}\\), find \\(\\sin A\\).",
            "Compute \\(\\sin A = \\frac{{BC}}{{AC}}\\) for \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), \\(BC = {b}\\), and \\(AC = {c}\\)."
        ],
        2: [
            "In a right-angled triangle, how is the sine ratio \\(\\sin \\theta\\) of an acute angle defined?",
            "State the standard formula defining \\(\\sin \\theta\\) in any right triangle.",
            "The trigonometric ratio \\(\\sin \\theta\\) in a right-angled triangle equals:",
            "Which side ratio defines \\(\\sin \\theta\\) with respect to an acute angle \\(\\theta\\)?",
            "By definition, the sine of an acute angle \\(\\theta\\) in a right triangle is:",
            "What is the mathematical ratio representing \\(\\sin \\theta\\) in a right-angled triangle?",
            "In terms of triangle sides, \\(\\sin \\theta\\) is expressed as:",
            "Identify the correct formula for \\(\\sin \\theta\\) in right triangle trigonometry.",
            "Which quotient represents \\(\\sin \\theta\\) for an acute angle \\(\\theta\\)?",
            "State the quotient defining \\(\\sin \\theta\\) in right-angled geometry."
        ],
        3: [
            "In \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), if \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and hypotenuse \\(AC = {c_mult}\\), find length \\(AB\\).",
            "Given \\(\\sin C = \\frac{{{a}}}{{{c}}}\ enter in right \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with \\(AC = {c_mult}\\), compute side \\(AB\\).",
            "Find the length of opposite side \\(AB\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(\\sin C = \\frac{{{a}}}{{{c}}}\) and \\(AC = {c_mult}\\).",
            "In right triangle \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), \\(AC = {c_mult}\\) and \\(\\sin C = \\frac{{{a}}}{{{c}}}\\). What is \\(AB\\)?",
            "Calculate side \\(AB\\) in \\(\\triangle ABC\\) right-angled at \\(B\\) if \\(\\sin C = \\frac{{{a}}}{{{c}}}\) and hypotenuse \\(AC = {c_mult}\\).",
            "Determine side \\(AB\\) opposite to angle \\(C\\) when \\(\\sin C = \\frac{{{a}}}{{{c}}}\) and \\(AC = {c_mult}\\) in \\(\\triangle ABC\\).",
            "Evaluate side length \\(AB\\) in right \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), \\(\\sin C = \\frac{{{a}}}{{{c}}}\\), and \\(AC = {c_mult}\\).",
            "What is the length of side \\(AB\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) if \\(\\sin C = \\frac{{{a}}}{{{c}}}\) and \\(AC = {c_mult}\\)?",
            "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), compute side \\(AB\\) given \\(\\sin C = \\frac{{{a}}}{{{c}}}\) and hypotenuse \\(AC = {c_mult}\\).",
            "For \\(\\triangle ABC\\) right-angled at \\(B\\), find \\(AB\\) when \\(\\sin C = \\frac{{{a}}}{{{c}}}\) and \\(AC = {c_mult}\\)."
        ],
        4: [
            "In \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), if \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and \\(AB = {a_mult}\\), find hypotenuse \\(AC\\).",
            "What is the hypotenuse \\(AC\\) in right-angled \\(\\triangle ABC\\) if \\(AB = {a_mult}\\) and \\(\\sin C = \\frac{{{a}}}{{{c}}}\\)?",
            "Calculate hypotenuse \\(AC\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(AB = {a_mult}\\) and \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
            "In right \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), \\(AB = {a_mult}\\) and \\(\\sin C = \\frac{{{a}}}{{{c}}}\\). Determine \\(AC\\).",
            "Find length \\(AC\\) in \\(\\triangle ABC\\) right-angled at \\(B\\) if \\(\\sin C = \\frac{{{a}}}{{{c}}}\) and \\(AB = {a_mult}\\).",
            "Determine the hypotenuse of \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(AB = {a_mult}\\) and \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
            "Evaluate the hypotenuse \\(AC\\) for right \\(\\triangle ABC\\) where \\(AB = {a_mult}\\) and \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
            "In right triangle \\(\\triangle ABC\\), find hypotenuse \\(AC\\) knowing \\(AB = {a_mult}\\) and \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
            "Compute hypotenuse \\(AC\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(\\sin C = \\frac{{{a}}}{{{c}}}\) and \\(AB = {a_mult}\\).",
            "What is hypotenuse \\(AC\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) if \\(\\sin C = \\frac{{{a}}}{{{c}}}\) and \\(AB = {a_mult}\\)?"
        ],
        5: [
            "Can the sine ratio of an acute angle in a right-angled triangle ever exceed 1?",
            "For any acute angle \\(\\theta\\) in a right triangle, is it possible for \\(\\sin \\theta > 1\\)?",
            "What is the maximum theoretical value that \\(\\sin \\theta\\) can attain for an acute angle \\(\\theta\\)?",
            "Why is \\(\\sin \\theta < 1\\) for every acute angle in a right-angled triangle?",
            "In a right triangle, since hypotenuse is the longest side, the ratio \\(\\sin \\theta = \\frac{{\\text{{Opposite}}}}{{\\text{{Hypotenuse}}}}\\) is always:",
            "Which inequality correctly bounds the value of \\(\\sin \\theta\\) for an acute angle \\(0^\\circ < \\theta < 90^\\circ\\)?",
            "State whether \\(\\sin \\theta\\) can be equal to 1.5 for any acute angle \\(\\theta\\).",
            "For any acute angle \\(\\theta\\), which statement regarding \\(\\sin \\theta\\) is mathematically true?",
            "In any right-angled triangle, the ratio of opposite side to hypotenuse is always:",
            "What is the upper bound for the sine of an acute angle in a right triangle?"
        ],
        6: [
            "In \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), side \\(AB = {a}\\) and \\(BC = {b}\\). Use Pythagoras theorem to find \\(\\sin C\\).",
            "Given perpendicular sides \\(AB = {a}\\) and \\(BC = {b}\\) in right \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), compute \\(\\sin C\\).",
            "Find \\(\\sin C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when legs are \\(AB = {a}\\) and \\(BC = {b}\\).",
            "In right-angled \\(\\triangle ABC\\) with legs \\(AB = {a}\\) and \\(BC = {b}\\), evaluate \\(\\sin C\\).",
            "Calculate \\(\\sin C\\) for \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with legs \\(AB = {a}\\) and \\(BC = {b}\\).",
            "Determine \\(\\sin C\\) in \\(\\triangle ABC\\) right-angled at \\(B\\) if \\(AB = {a}\\) and \\(BC = {b}\\).",
            "For \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with sides \\(AB = {a}\\) and \\(BC = {b}\\), find \\(\\sin C\\).",
            "Evaluate \\(\\sin C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given legs \\(AB = {a}\\) and \\(BC = {b}\\).",
            "State \\(\\sin C\\) for right \\(\\triangle ABC\\) having legs \\(AB = {a}\\) and \\(BC = {b}\\).",
            "Compute \\(\\sin C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with leg lengths \\(AB = {a}\\) and \\(BC = {b}\\)."
        ],
        7: [
            "In \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), if \\(\\sin C = \\frac{{{a}}}{{{c}}}\\), what is the value of \\(\\sin^2 C\\)?",
            "Compute \\(\\sin^2 C\\) in right-angled \\(\\triangle ABC\\) given \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
            "If \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), find \\((\\sin C)^2\\).",
            "What is \\(\\sin^2 C\\) for \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(\\sin C = \\frac{{{a}}}{{{c}}}\\)?",
            "Evaluate the squared sine ratio \\(\\sin^2 C\\) if \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) in \\(\\triangle ABC\\).",
            "Calculate \\(\\sin^2 C\\) in right \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) where \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
            "Determine \\(\\sin^2 C\\) given \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) in right-angled \\(\\triangle ABC\\).",
            "Find the value of \\(\\sin^2 C\\) for right-angled \\(\\triangle ABC\\) with \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
            "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), find \\(\\sin^2 C\\) knowing \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
            "Compute \\((\\sin C)^2\\) for \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\) where \\(\\sin C = \\frac{{{a}}}{{{c}}}\\)."
        ]
    }
    
    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        tmpl = TEMPLATES[arch][sub_idx]
        
        a, b, c = TRIPLES[sub_idx]
        has_fig = (idx % 3 != 0)
        svg = svg_trig_triangle("A", "B", "C", f"AB = {a}", f"BC = {b}", f"AC = {c}", f"Right Triangle #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""
        
        if arch == 0:
            txt = prefix + tmpl.format(a=a, c=c)
            corr = f"\\(\\frac{{{a}}}{{{c}}}\\)"
            dist = [f"\\(\\frac{{{b}}}{{{c}}}\\)", f"\\(\\frac{{{a}}}{{{b}}}\\)", f"\\(\\frac{{{c}}}{{{a}}}\\)"]
            sol = f"**Step 1: Formula**\n\\(\\sin C = \\frac{{\\text{{Side opposite to }} \\angle C}}{{\\text{{Hypotenuse}}}} = \\frac{{AB}}{{AC}} = \\frac{{{a}}}{{{c}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{a}}}{{{c}}}\\)."
        elif arch == 1:
            txt = prefix + tmpl.format(b=b, c=c)
            corr = f"\\(\\frac{{{b}}}{{{c}}}\\)"
            dist = [f"\\(\\frac{{{a}}}{{{c}}}\\)", f"\\(\\frac{{{b}}}{{{a}}}\\)", f"\\(\\frac{{{c}}}{{{b}}}\\)"]
            sol = f"**Step 1: Formula**\n\\(\\sin A = \\frac{{\\text{{Side opposite to }} \\angle A}}{{\\text{{Hypotenuse}}}} = \\frac{{BC}}{{AC}} = \\frac{{{b}}}{{{c}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{b}}}{{{c}}}\\)."
        elif arch == 2:
            txt = prefix + tmpl
            corr = "\\(\\frac{\\text{Opposite side}}{\\text{Hypotenuse}}\\)"
            dist = ["\\(\\frac{\\text{Adjacent side}}{\\text{Hypotenuse}}\\)", "\\(\\frac{\\text{Opposite side}}{\\text{Adjacent side}}\\)", "\\(\\frac{\\text{Hypotenuse}}{\\text{Opposite side}}\\)" ]
            sol = f"**Step 1: Definition**\nIn a right triangle, \\(\\sin \\theta = \\frac{{\\text{{Opposite side}}}}{{\\text{{Hypotenuse}}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{\\text{{Opposite side}}}}{{\\text{{Hypotenuse}}}}\\)."
        elif arch == 3:
            c_mult = c * 2
            a_ans = a * 2
            txt = prefix + tmpl.format(a=a, c=c, c_mult=c_mult)
            corr = f"{a_ans}"
            dist = [f"{a}", f"{a_ans + 2}", f"{b * 2}"]
            sol = f"**Step 1: Cross-multiplication**\n\\(\\sin C = \\frac{{AB}}{{AC}} \\implies \\frac{{{a}}}{{{c}}} = \\frac{{AB}}{{{c_mult}}}\\).\n\\(AB = \\frac{{{a} \\times {c_mult}}}{{{c}}} = {a_ans}\\).\n**Step 2: Conclusion**\n{a_ans}."
        elif arch == 4:
            a_mult = a * 3
            c_ans = c * 3
            txt = prefix + tmpl.format(a=a, c=c, a_mult=a_mult)
            corr = f"{c_ans}"
            dist = [f"{c}", f"{c_ans + 5}", f"{b * 3}"]
            sol = f"**Step 1: Cross-multiplication**\n\\(\\sin C = \\frac{{AB}}{{AC}} \\implies \\frac{{{a}}}{{{c}}} = \\frac{{{a_mult}}}{{AC}}\\).\n\\(AC = \\frac{{{c} \\times {a_mult}}}{{{a}}} = {c_ans}\\).\n**Step 2: Conclusion**\n{c_ans}."
        elif arch == 5:
            txt = prefix + tmpl
            corr = "No, because hypotenuse is strictly greater than the opposite side"
            dist = ["Yes, for large acute angles", "Yes, when hypotenuse is small", "Cannot be determined"]
            sol = f"**Step 1: Geometric inequality**\nIn any right-angled triangle, hypotenuse > opposite side, so \\(\\sin \\theta = \\frac{{\\text{{opposite}}}}{{\\text{{hypotenuse}}}} < 1\\).\n**Step 2: Conclusion**\nNo."
        elif arch == 6:
            txt = prefix + tmpl.format(a=a, b=b)
            corr = f"\\(\\frac{{{a}}}{{{c}}}\\)"
            dist = [f"\\(\\frac{{{b}}}{{{c}}}\\)", f"\\(\\frac{{{a}}}{{{b}}}\\)", f"\\(\\frac{{{b}}}{{{a}}}\\)"]
            sol = f"**Step 1: Hypotenuse by Pythagoras**\n\\(AC = \\sqrt{{{a}^2 + {b}^2}} = \\sqrt{{{a*a + b*b}}} = {c}\\).\n**Step 2: Sine Ratio**\n\\(\\sin C = \\frac{{AB}}{{AC}} = \\frac{{{a}}}{{{c}}}\\).\n**Step 3: Conclusion**\n\\(\\frac{{{a}}}{{{c}}}\\)."
        else:
            sq_a = a * a
            sq_c = c * c
            txt = prefix + tmpl.format(a=a, c=c)
            corr = f"\\(\\frac{{{sq_a}}}{{{sq_c}}}\\)"
            dist = [f"\\(\\frac{{{a * 2}}}{{{c * 2}}}\\)", f"\\(\\frac{{{b * b}}}{{{sq_c}}}\\)", f"\\(\\frac{{{sq_a + 1}}}{{{sq_c}}}\\)"]
            sol = f"**Step 1: Square ratio**\n\\(\\sin^2 C = (\\frac{{{a}}}{{{c}}})^2 = \\frac{{{sq_a}}}{{{sq_c}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{sq_a}}}{{{sq_c}}}\\)."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def main():
    q1 = generate_8_1_1()
    print("8.1.1 count:", len(q1))
    with open("scripts/mh9_mth2_8_1_1_test.json", "w", encoding="utf-8") as f:
        json.dump(q1, f, indent=2)

if __name__ == "__main__":
    main()
