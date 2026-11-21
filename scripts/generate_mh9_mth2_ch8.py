# scripts/generate_mh9_mth2_ch8.py
import json

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
        "createdAt": "2026-11-21T14:00:00.000Z",
        "updatedAt": "2026-11-21T14:00:00.000Z",
        "options": opts,
        "correctAnswer": corr_letter,
        "solution": sol,
        "text": text
    }

def svg_trig(v_top, v_rt, v_right, opp_lbl, adj_lbl, hyp_lbl, title=""):
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
        f'</svg>'
    )

# -----------------------------------------------------------------------------
# 8.1.1: sin θ = Opposite / Hypotenuse
# -----------------------------------------------------------------------------
def gen_8_1_1():
    tc = "MH-9-MTH2-8-8.1.1"
    tname = "In right angled triangle: sin θ = Opposite / Hypotenuse"
    qs = []
    
    triples_0 = [(3,4,5), (5,12,13), (8,15,17), (7,24,25), (9,40,41), (12,35,37), (20,21,29), (11,60,61), (16,63,65), (28,45,53)]
    tmpls_0 = [
        "In right-angled \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), side \\(AB = {a}\\) and hypotenuse \\(AC = {c}\\). Find \\(\\sin C\\).",
        "For \\(\\triangle ABC\\) right-angled at \\(B\\), where \\(AB = {a}\\) and \\(AC = {c}\\), what is the value of \\(\\sin C\\)?",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), given \\(AB = {a}\\) and \\(AC = {c}\\), compute the sine ratio \\(\\sin C\\).",
        "Given right \\(\\triangle ABC\\) with right angle at vertex \\(B\\), \\(AB = {a}\\) and \\(AC = {c}\\). Determine \\(\\sin C\\).",
        "Calculate the value of \\(\\sin C\\) in \\(\\triangle ABC\\) having \\(\\angle B = 90^\\circ\\), \\(AB = {a}\\), and \\(AC = {c}\\).",
        "What is \\(\\sin C\\) in right triangle \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) if \\(AB = {a}\\) and hypotenuse \\(AC = {c}\\)?",
        "In right-angled \\(\\triangle ABC\\), \\(\\angle ABC = 90^\\circ\\), \\(AB = {a}\\) and \\(AC = {c}\\). Evaluate \\(\\sin C\\).",
        "Find \\(\\sin C\\) for the right triangle \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), opposite side \\(AB = {a}\\), and hypotenuse \\(AC = {c}\\).",
        "With \\(\\angle B = 90^\\circ\\) in \\(\\triangle ABC\\), determine \\(\\sin C\\) when side \\(AB = {a}\\) and hypotenuse \\(AC = {c}\\).",
        "Compute \\(\\sin C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(AB = {a}\\) and \\(AC = {c}\\)."
    ]
    
    triples_1 = [(4,3,5), (12,5,13), (15,8,17), (24,7,25), (40,9,41), (35,12,37), (21,20,29), (60,11,61), (63,16,65), (45,28,53)]
    tmpls_1 = [
        "In right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), side \\(BC = {a}\\) and \\(AC = {c}\\). What is \\(\\sin A\\)?",
        "Find the ratio \\(\\sin A\\) in \\(\\triangle ABC\\) right-angled at \\(B\\) if \\(BC = {a}\\) and \\(AC = {c}\\).",
        "In \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), calculate \\(\\sin A\\) given opposite side \\(BC = {a}\\) and hypotenuse \\(AC = {c}\\).",
        "For \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), determine \\(\\sin A\\) knowing that \\(BC = {a}\\) and \\(AC = {c}\\).",
        "What is the value of \\(\\sin A\\) in right triangle \\(\\triangle ABC\\) where \\(BC = {a}\\) and hypotenuse \\(AC = {c}\\)?",
        "Compute \\(\\sin A\\) in right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(BC = {a}\\) and \\(AC = {c}\\).",
        "Evaluate the sine of angle \\(A\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with \\(BC = {a}\\) and \\(AC = {c}\\).",
        "In right \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), find \\(\\sin A\\) if \\(BC = {a}\\) and \\(AC = {c}\\).",
        "Determine \\(\\sin A\\) for \\(\\triangle ABC\\) right-angled at \\(B\\) having \\(BC = {a}\\) and hypotenuse \\(AC = {c}\\).",
        "Find \\(\\sin A\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with \\(BC = {a}\\) and \\(AC = {c}\\)."
    ]
    
    data_2 = [(3,5,15,9), (5,13,52,20), (8,17,34,16), (7,25,50,14), (9,41,82,18), (12,37,74,24), (20,29,58,40), (11,61,122,22), (4,5,25,20), (12,13,39,36)]
    tmpls_2 = [
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), if \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and hypotenuse \\(AC = {ac}\\), calculate side \\(AB\\).",
        "Find length of side \\(AB\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and \\(AC = {ac}\\).",
        "For right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), determine \\(AB\\) if \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and \\(AC = {ac}\\).",
        "Compute side \\(AB\\) in right triangle \\(\\triangle ABC\\) when \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and hypotenuse \\(AC = {ac}\\).",
        "What is the length of opposite side \\(AB\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) where \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and \\(AC = {ac}\\)?",
        "In \\(\\triangle ABC\\) right-angled at \\(B\\), evaluate \\(AB\\) knowing \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and \\(AC = {ac}\\).",
        "If \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and hypotenuse \\(AC = {ac}\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), find \\(AB\\).",
        "Determine the measure of side \\(AB\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and \\(AC = {ac}\\).",
        "In right \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), calculate \\(AB\\) if \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and \\(AC = {ac}\\).",
        "Find side \\(AB\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and \\(AC = {ac}\\)."
    ]
    
    data_3 = [(3,5,6,10), (5,13,15,39), (8,17,24,51), (7,25,21,75), (9,41,27,123), (12,37,36,111), (20,29,60,87), (11,61,33,183), (4,5,12,15), (12,13,24,26)]
    tmpls_3 = [
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), if \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and \\(AB = {ab}\\), find hypotenuse \\(AC\\).",
        "What is hypotenuse \\(AC\\) in right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(AB = {ab}\\) and \\(\\sin C = \\frac{{{a}}}{{{c}}}\\)?",
        "Calculate \\(AC\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(AB = {ab}\\) and \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
        "In right triangle \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), find hypotenuse \\(AC\\) if \\(AB = {ab}\\) and \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
        "Determine the length of hypotenuse \\(AC\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) where \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and \\(AB = {ab}\\).",
        "For \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), find \\(AC\\) knowing \\(AB = {ab}\\) and \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
        "Evaluate hypotenuse \\(AC\\) in \\(\\triangle ABC\\) right-angled at \\(B\\) given \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and opposite side \\(AB = {ab}\\).",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), compute \\(AC\\) when \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and \\(AB = {ab}\\).",
        "If \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and \\(AB = {ab}\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), what is \\(AC\\)?",
        "Find hypotenuse \\(AC\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) and \\(AB = {ab}\\)."
    ]
    
    data_4 = [(3,5,9,25), (5,13,25,169), (8,17,64,289), (7,25,49,625), (9,41,81,1681), (12,37,144,1369), (20,29,400,841), (11,61,121,3721), (4,5,16,25), (12,13,144,169)]
    tmpls_4 = [
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), if \\(\\sin C = \\frac{{{a}}}{{{c}}}\\), find the value of \\(\\sin^2 C\\).",
        "Calculate \\(\\sin^2 C\\) in right-angled \\(\\triangle ABC\\) given \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
        "What is the value of \\(\\sin^2 C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(\\sin C = \\frac{{{a}}}{{{c}}}\\)?",
        "Evaluate \\((\\sin C)^2\\) for right \\(\\triangle ABC\\) with \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), compute \\(\\sin^2 C\\) if \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
        "Determine \\(\\sin^2 C\\) in right triangle \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) where \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
        "Find the squared sine \\(\\sin^2 C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) knowing \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
        "For \\(\\triangle ABC\\ right-angled at \\(B\\), find \\(\\sin^2 C\\) when \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
        "Compute the numerical value of \\(\\sin^2 C\\) if \\(\\sin C = \\frac{{{a}}}{{{c}}}\\) in \\(\\triangle ABC\\).",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), evaluate \\(\\sin^2 C\\) given \\(\\sin C = \\frac{{{a}}}{{{c}}}\\)."
    ]
    
    data_5 = [(3,5,16,25), (5,13,144,169), (8,17,225,289), (7,25,576,625), (9,41,1600,1681), (12,37,1225,1369), (20,29,441,841), (11,61,3600,3721), (4,5,9,25), (12,13,25,169)]
    tmpls_5 = [
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), if \\(\\sin C = \\frac{{{a}}}{{{c}}}\\), find the value of \\(1 - \\sin^2 C\\).",
        "Evaluate \\(1 - \\sin^2 C\\) for right-angled \\(\\triangle ABC\\) given \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
        "What is the value of \\(1 - \\sin^2 C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(\\sin C = \\frac{{{a}}}{{{c}}}\\)?",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), calculate \\(1 - \\sin^2 C\\) if \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
        "Calculate the expression \\(1 - \\sin^2 C\\) in right \\(\\triangle ABC\\) where \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
        "Determine the measure of \\(1 - \\sin^2 C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
        "Find the value of \\(1 - \\sin^2 C\\) for \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
        "For right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), find \\(1 - \\sin^2 C\\) when \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
        "Compute \\(1 - \\sin^2 C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) knowing \\(\\sin C = \\frac{{{a}}}{{{c}}}\\).",
        "In right triangle \\(\\triangle ABC\\), evaluate \\(1 - \\sin^2 C\\) if \\(\\sin C = \\frac{{{a}}}{{{c}}}\\)."
    ]
    
    data_6 = [(1,1,"\\sqrt{2}","2"), (1,2,"\\sqrt{5}","5"), (1,3,"\\sqrt{10}","10"), (2,3,"\\sqrt{13}","13"), (1,4,"\\sqrt{17}","17"), (2,5,"\\sqrt{29}","29"), (1,6,"\\sqrt{37}","37"), (3,5,"\\sqrt{34}","34"), (4,5,"\\sqrt{41}","41"), (1,7,"\\sqrt{50}","50")]
    tmpls_6 = [
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), side \\(AB = {a}\\) and \\(BC = {b}\\). What is \\(\\sin C\\)?",
        "Given legs \\(AB = {a}\\) and \\(BC = {b}\\) in right \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), find \\(\\sin C\\).",
        "Calculate \\(\\sin C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with perpendicular sides \\(AB = {a}\\) and \\(BC = {b}\\).",
        "In right-angled \\(\\triangle ABC\\), \\(AB = {a}\\) and \\(BC = {b}\\). Determine \\(\\sin C\\).",
        "Find the sine ratio \\(\\sin C\\) for \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) where \\(AB = {a}\\) and \\(BC = {b}\\).",
        "Compute \\(\\sin C\\) in right triangle \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) having legs \\(AB = {a}\\) and \\(BC = {b}\\).",
        "Evaluate \\(\\sin C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with legs \\(AB = {a}\\) and \\(BC = {b}\\).",
        "For \\(\\triangle ABC\\) right-angled at \\(B\\), find \\(\\sin C\\) if \\(AB = {a}\\) and \\(BC = {b}\\).",
        "What is the exact value of \\(\\sin C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with \\(AB = {a}\\) and \\(BC = {b}\\)?",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), determine \\(\\sin C\\) given legs \\(AB = {a}\\) and \\(BC = {b}\\)."
    ]
    
    data_7 = [
        ("0^\\circ", "0", ["1", "\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}"]),
        ("30^\\circ", "\\frac{1}{2}", ["\\frac{\\sqrt{3}}{2}", "\\frac{1}{\\sqrt{2}}", "1"]),
        ("45^\\circ", "\\frac{1}{\\sqrt{2}}", ["\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}", "0"]),
        ("60^\\circ", "\\frac{\\sqrt{3}}{2}", ["\\frac{1}{2}", "\\frac{1}{\\sqrt{2}}", "1"]),
        ("90^\\circ", "1", ["0", "\\frac{1}{2}", "\\text{undefined}"]),
        ("30^\\circ \\text{ squared}", "\\frac{1}{4}", ["\\frac{3}{4}", "\\frac{1}{2}", "\\frac{1}{8}"]),
        ("45^\\circ \\text{ squared}", "\\frac{1}{2}", ["\\frac{1}{4}", "\\frac{3}{4}", "1"]),
        ("60^\\circ \\text{ squared}", "\\frac{3}{4}", ["\\frac{1}{4}", "\\frac{1}{2}", "\\frac{3}{2}"]),
        ("30^\\circ + \\sin 90^\\circ", "\\frac{3}{2}", ["1", "\\frac{1}{2}", "2"]),
        ("60^\\circ - \\sin 30^\\circ", "\\frac{\\sqrt{3}-1}{2}", ["\\frac{\\sqrt{3}+1}{2}", "\\frac{1}{2}", "0"])
    ]
    tmpls_7 = [
        "In right triangle trigonometry, what is the exact standard value of \\(\\sin 0^\\circ\\)?",
        "What is the exact numerical value of \\(\\sin 30^\\circ\\) derived from a 30°-60°-90° right triangle?",
        "Find the exact value of \\(\\sin 45^\\circ\\) in a 45°-45°-90° right-angled triangle.",
        "Evaluate the exact trigonometric ratio \\(\\sin 60^\\circ\\).",
        "What is the value of \\(\\sin 90^\\circ\\) in standard trigonometry?",
        "Compute the exact value of \\(\\sin^2 30^\\circ\\).",
        "Evaluate the squared sine ratio \\(\\sin^2 45^\\circ\\).",
        "Determine the exact value of \\(\\sin^2 60^\\circ\\).",
        "Calculate the sum \\(\\sin 30^\\circ + \\sin 90^\\circ\\).",
        "Find the exact difference \\(\\sin 60^\\circ - \\sin 30^\\circ\\)."
    ]
    
    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        
        if arch == 0:
            a, b, c = triples_0[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {a}", f"BC = {b}", f"AC = {c}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(a=a, c=c)
            corr = f"\\(\\frac{{{a}}}{{{c}}}\\)"
            dist = [f"\\(\\frac{{{b}}}{{{c}}}\\)", f"\\(\\frac{{{a}}}{{{b}}}\\)", f"\\(\\frac{{{c}}}{{{a}}}\\)"]
            sol = f"**Step 1: Formula**\n\\(\\sin C = \\frac{{\\text{{Side opposite to }} \\angle C}}{{\\text{{Hypotenuse}}}} = \\frac{{AB}}{{AC}} = \\frac{{{a}}}{{{c}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{a}}}{{{c}}}\\)."
        elif arch == 1:
            a, b, c = triples_1[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {b}", f"BC = {a}", f"AC = {c}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(a=a, c=c)
            corr = f"\\(\\frac{{{a}}}{{{c}}}\\)"
            dist = [f"\\(\\frac{{{b}}}{{{c}}}\\)", f"\\(\\frac{{{a}}}{{{b}}}\\)", f"\\(\\frac{{{c}}}{{{a}}}\\)"]
            sol = f"**Step 1: Formula**\n\\(\\sin A = \\frac{{\\text{{Side opposite to }} \\angle A}}{{\\text{{Hypotenuse}}}} = \\frac{{BC}}{{AC}} = \\frac{{{a}}}{{{c}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{a}}}{{{c}}}\\)."
        elif arch == 2:
            a, c, ac, ans = data_2[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = ?", "", f"AC = {ac}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(a=a, c=c, ac=ac)
            corr = f"{ans}"
            dist = [f"{ans + 2}", f"{ans - 2 if ans > 2 else ans + 4}", f"{ans * 2}"]
            sol = f"**Step 1: Cross multiplication**\n\\(\\sin C = \\frac{{AB}}{{AC}} \\implies \\frac{{{a}}}{{{c}}} = \\frac{{AB}}{{{ac}}}\\).\n\\(AB = \\frac{{{a} \\times {ac}}}{{{c}}} = {ans}\\).\n**Step 2: Conclusion**\n{ans}."
        elif arch == 3:
            a, c, ab, ans = data_3[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {ab}", "", "AC = ?") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(a=a, c=c, ab=ab)
            corr = f"{ans}"
            dist = [f"{ans + 5}", f"{ans - 5 if ans > 5 else ans + 8}", f"{ans * 2}"]
            sol = f"**Step 1: Cross multiplication**\n\\(\\sin C = \\frac{{AB}}{{AC}} \\implies \\frac{{{a}}}{{{c}}} = \\frac{{{ab}}}{{AC}}\\).\n\\(AC = \\frac{{{c} \\times {ab}}}{{{a}}} = {ans}\\).\n**Step 2: Conclusion**\n{ans}."
        elif arch == 4:
            a, c, sq_a, sq_c = data_4[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {a}", "", f"AC = {c}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(a=a, c=c)
            corr = f"\\(\\frac{{{sq_a}}}{{{sq_c}}}\\)"
            dist = [f"\\(\\frac{{{a * 2}}}{{{c * 2}}}\\)", f"\\(\\frac{{{sq_a + 2}}}{{{sq_c}}}\\)", f"\\(\\frac{{{sq_a}}}{{{sq_c + 5}}}\\)"]
            sol = f"**Step 1: Square ratio**\n\\(\\sin^2 C = (\\frac{{{a}}}{{{c}}})^2 = \\frac{{{sq_a}}}{{{sq_c}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{sq_a}}}{{{sq_c}}}\\)."
        elif arch == 5:
            a, c, sq_sub, sq_c = data_5[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {a}", "", f"AC = {c}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(a=a, c=c)
            corr = f"\\(\\frac{{{sq_sub}}}{{{sq_c}}}\\)"
            dist = [f"\\(\\frac{{{sq_sub - 2}}}{{{sq_c}}}\\)", f"\\(\\frac{{{sq_sub}}}{{{sq_c + 4}}}\\)", f"\\(\\frac{{{a}}}{{{c}}}\\)"]
            sol = f"**Step 1: Evaluate identity**\n\\(1 - \\sin^2 C = 1 - \\frac{{{a*a}}}{{{sq_c}}} = \\frac{{{sq_c - a*a}}}{{{sq_c}}} = \\frac{{{sq_sub}}}{{{sq_c}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{sq_sub}}}{{{sq_c}}}\\)."
        elif arch == 6:
            a, b, rad, rad_sq = data_6[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {a}", f"BC = {b}", f"AC = {rad}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(a=a, b=b)
            corr = f"\\(\\frac{{{a}}}{{{rad}}}\\)"
            dist = [f"\\(\\frac{{{b}}}{{{rad}}}\\)", f"\\(\\frac{{{a}}}{{{b}}}\\)", f"\\(\\frac{{{rad}}}{{{a}}}\\)"]
            sol = f"**Step 1: Pythagoras theorem**\n\\(AC = \\sqrt{{{a}^2 + {b}^2}} = {rad}\\).\n**Step 2: Sine formula**\n\\(\\sin C = \\frac{{AB}}{{AC}} = \\frac{{{a}}}{{{rad}}}\\).\n**Step 3: Conclusion**\n\\(\\frac{{{a}}}{{{rad}}}\\)."
        else:
            tag, ans_c, dist_c = data_7[sub_idx]
            txt = tmpls_7[sub_idx]
            corr = f"\\({ans_c}\\)" if not ans_c.startswith("\\") and any(c in ans_c for c in "+-/*") else (ans_c if ans_c.startswith("\\") else f"\\({ans_c}\\)")
            dist = [d if d.startswith("\\") else f"\\({d}\\)" for d in dist_c]
            sol = f"**Step 1: Geometric evaluation**\nFrom standard trigonometric values, the exact value is {corr}.\n**Step 2: Conclusion**\n{corr}."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

# -----------------------------------------------------------------------------
# 8.1.2: cos θ = Adjacent / Hypotenuse
# -----------------------------------------------------------------------------
def gen_8_1_2():
    tc = "MH-9-MTH2-8-8.1.2"
    tname = "cos θ = Adjacent / Hypotenuse"
    qs = []
    
    triples_0 = [(4,3,5), (12,5,13), (15,8,17), (24,7,25), (40,9,41), (35,12,37), (21,20,29), (60,11,61), (63,16,65), (45,28,53)]
    tmpls_0 = [
        "In right-angled \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), side \\(BC = {a}\\) and hypotenuse \\(AC = {c}\\). Find \\(\\cos C\\).",
        "For \\(\\triangle ABC\\) right-angled at \\(B\\), where \\(BC = {a}\\) and \\(AC = {c}\\), what is the value of \\(\\cos C\\)?",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), given \\(BC = {a}\\) and \\(AC = {c}\\), compute the cosine ratio \\(\\cos C\\).",
        "Given right \\(\\triangle ABC\\) with right angle at vertex \\(B\\), \\(BC = {a}\\) and \\(AC = {c}\\). Determine \\(\\cos C\\).",
        "Calculate the value of \\(\\cos C\\) in \\(\\triangle ABC\\) having \\(\\angle B = 90^\\circ\\), \\(BC = {a}\\), and \\(AC = {c}\\).",
        "What is \\(\\cos C\\) in right triangle \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) if \\(BC = {a}\\) and hypotenuse \\(AC = {c}\\)?",
        "In right-angled \\(\\triangle ABC\\), \\(\\angle ABC = 90^\\circ\\), \\(BC = {a}\\) and \\(AC = {c}\\). Evaluate \\(\\cos C\\).",
        "Find \\(\\cos C\\) for the right triangle \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), adjacent side \\(BC = {a}\\), and hypotenuse \\(AC = {c}\\).",
        "With \\(\\angle B = 90^\\circ\\) in \\(\\triangle ABC\\), determine \\(\\cos C\\) when side \\(BC = {a}\\) and hypotenuse \\(AC = {c}\\).",
        "Compute \\(\\cos C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(BC = {a}\\) and \\(AC = {c}\\)."
    ]
    
    triples_1 = [(3,4,5), (5,12,13), (8,15,17), (7,24,25), (9,40,41), (12,35,37), (20,21,29), (11,60,61), (16,63,65), (28,45,53)]
    tmpls_1 = [
        "In right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), side \\(AB = {a}\\) and \\(AC = {c}\\). What is \\(\\cos A\\)?",
        "Find the ratio \\(\\cos A\\) in \\(\\triangle ABC\\) right-angled at \\(B\\) if \\(AB = {a}\\) and \\(AC = {c}\\).",
        "In \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), calculate \\(\\cos A\\) given adjacent side \\(AB = {a}\\) and hypotenuse \\(AC = {c}\\).",
        "For \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), determine \\(\\cos A\\) knowing that \\(AB = {a}\\) and \\(AC = {c}\\).",
        "What is the value of \\(\\cos A\\) in right triangle \\(\\triangle ABC\\) where \\(AB = {a}\\) and hypotenuse \\(AC = {c}\\)?",
        "Compute \\(\\cos A\\) in right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(AB = {a}\\) and \\(AC = {c}\\).",
        "Evaluate the cosine of angle \\(A\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with \\(AB = {a}\\) and \\(AC = {c}\\).",
        "In right \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), find \\(\\cos A\\) if \\(AB = {a}\\) and \\(AC = {c}\\).",
        "Determine \\(\\cos A\\) for \\(\\triangle ABC\\) right-angled at \\(B\\) having \\(AB = {a}\\) and hypotenuse \\(AC = {c}\\).",
        "Find \\(\\cos A\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with \\(AB = {a}\\) and \\(AC = {c}\\)."
    ]
    
    data_2 = [(4,5,15,12), (12,13,26,24), (15,17,34,30), (24,25,50,48), (40,41,82,80), (35,37,74,70), (21,29,58,42), (60,61,122,120), (3,5,35,21), (5,13,65,25)]
    tmpls_2 = [
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), if \\(\\cos C = \\frac{{{a}}}{{{c}}}\\) and hypotenuse \\(AC = {ac}\\), calculate side \\(BC\\).",
        "Find length of side \\(BC\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(\\cos C = \\frac{{{a}}}{{{c}}}\\) and \\(AC = {ac}\\).",
        "For right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), determine \\(BC\\) if \\(\\cos C = \\frac{{{a}}}{{{c}}}\\) and \\(AC = {ac}\\).",
        "Compute side \\(BC\\) in right triangle \\(\\triangle ABC\\) when \\(\\cos C = \\frac{{{a}}}{{{c}}}\\) and hypotenuse \\(AC = {ac}\\).",
        "What is the length of adjacent side \\(BC\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) where \\(\\cos C = \\frac{{{a}}}{{{c}}}\\) and \\(AC = {ac}\\)?",
        "In \\(\\triangle ABC\\) right-angled at \\(B\\), evaluate \\(BC\\) knowing \\(\\cos C = \\frac{{{a}}}{{{c}}}\\) and \\(AC = {ac}\\).",
        "If \\(\\cos C = \\frac{{{a}}}{{{c}}}\\) and hypotenuse \\(AC = {ac}\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), find \\(BC\\).",
        "Determine the measure of side \\(BC\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(\\cos C = \\frac{{{a}}}{{{c}}}\\) and \\(AC = {ac}\\).",
        "In right \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), calculate \\(BC\\) if \\(\\cos C = \\frac{{{a}}}{{{c}}}\\) and \\(AC = {ac}\\).",
        "Find side \\(BC\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(\\cos C = \\frac{{{a}}}{{{c}}}\\) and \\(AC = {ac}\\)."
    ]
    
    data_3 = [(4,5,8,10), (12,13,36,39), (15,17,45,51), (24,25,72,75), (40,41,40,41), (35,37,70,74), (21,29,63,87), (60,61,120,122), (3,5,12,20), (5,13,25,65)]
    tmpls_3 = [
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), if \\(\\cos C = \\frac{{{a}}}{{{c}}}\\) and \\(BC = {bc}\\), find hypotenuse \\(AC\\).",
        "What is hypotenuse \\(AC\\) in right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(BC = {bc}\\) and \\(\\cos C = \\frac{{{a}}}{{{c}}}\\)?",
        "Calculate \\(AC\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(BC = {bc}\\) and \\(\\cos C = \\frac{{{a}}}{{{c}}}\\).",
        "In right triangle \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), find hypotenuse \\(AC\\) if \\(BC = {bc}\\) and \\(\\cos C = \\frac{{{a}}}{{{c}}}\\).",
        "Determine the length of hypotenuse \\(AC\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) where \\(\\cos C = \\frac{{{a}}}{{{c}}}\\) and \\(BC = {bc}\\).",
        "For \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), find \\(AC\\) knowing \\(BC = {bc}\\) and \\(\\cos C = \\frac{{{a}}}{{{c}}}\\).",
        "Evaluate hypotenuse \\(AC\\) in \\(\\triangle ABC\\) right-angled at \\(B\\) given \\(\\cos C = \\frac{{{a}}}{{{c}}}\\) and adjacent side \\(BC = {bc}\\).",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), compute \\(AC\\) when \\(\\cos C = \\frac{{{a}}}{{{c}}}\\) and \\(BC = {bc}\\).",
        "If \\(\\cos C = \\frac{{{a}}}{{{c}}}\\) and \\(BC = {bc}\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), what is \\(AC\\)?",
        "Find hypotenuse \\(AC\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(\\cos C = \\frac{{{a}}}{{{c}}}\\) and \\(BC = {bc}\\)."
    ]
    
    data_4 = [(4,5,16,25), (12,13,144,169), (15,17,225,289), (24,25,576,625), (40,41,1600,1681), (35,37,1225,1369), (21,29,441,841), (60,61,3600,3721), (3,5,9,25), (5,13,25,169)]
    tmpls_4 = [
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), if \\(\\cos C = \\frac{{{a}}}{{{c}}}\\), find the value of \\(\\cos^2 C\\).",
        "Calculate \\(\\cos^2 C\\) in right-angled \\(\\triangle ABC\\) given \\(\\cos C = \\frac{{{a}}}{{{c}}}\\).",
        "What is the value of \\(\\cos^2 C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(\\cos C = \\frac{{{a}}}{{{c}}}\\)?",
        "Evaluate \\((\\cos C)^2\\) for right \\(\\triangle ABC\\) with \\(\\cos C = \\frac{{{a}}}{{{c}}}\\).",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), compute \\(\\cos^2 C\\) if \\(\\cos C = \\frac{{{a}}}{{{c}}}\\).",
        "Determine \\(\\cos^2 C\\) in right triangle \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) where \\(\\cos C = \\frac{{{a}}}{{{c}}}\\).",
        "Find the squared cosine \\(\\cos^2 C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) knowing \\(\\cos C = \\frac{{{a}}}{{{c}}}\\).",
        "For \\(\\triangle ABC\\) right-angled at \\(B\\), find \\(\\cos^2 C\\) when \\(\\cos C = \\frac{{{a}}}{{{c}}}\\).",
        "Compute the numerical value of \\(\\cos^2 C\\) if \\(\\cos C = \\frac{{{a}}}{{{c}}}\\) in \\(\\triangle ABC\\).",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), evaluate \\(\\cos^2 C\\) given \\(\\cos C = \\frac{{{a}}}{{{c}}}\\)."
    ]
    
    data_5 = [(4,5,9,25), (12,13,25,169), (15,17,64,289), (24,25,49,625), (40,41,81,1681), (35,37,144,1369), (21,29,400,841), (60,61,121,3721), (3,5,16,25), (5,13,144,169)]
    tmpls_5 = [
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), if \\(\\cos C = \\frac{{{a}}}{{{c}}}\\), find the value of \\(1 - \\cos^2 C\\).",
        "Evaluate \\(1 - \\cos^2 C\\) for right-angled \\(\\triangle ABC\\) given \\(\\cos C = \\frac{{{a}}}{{{c}}}\\).",
        "What is the value of \\(1 - \\cos^2 C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(\\cos C = \\frac{{{a}}}{{{c}}}\\)?",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), calculate \\(1 - \\cos^2 C\\) if \\(\\cos C = \\frac{{{a}}}{{{c}}}\\).",
        "Calculate the expression \\(1 - \\cos^2 C\\) in right \\(\\triangle ABC\\) where \\(\\cos C = \\frac{{{a}}}{{{c}}}\\).",
        "Determine the measure of \\(1 - \\cos^2 C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with \\(\\cos C = \\frac{{{a}}}{{{c}}}\\).",
        "Find the value of \\(1 - \\cos^2 C\\) for \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(\\cos C = \\frac{{{a}}}{{{c}}}\\).",
        "For right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), find \\(1 - \\cos^2 C\\) when \\(\\cos C = \\frac{{{a}}}{{{c}}}\\).",
        "Compute \\(1 - \\cos^2 C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) knowing \\(\\cos C = \\frac{{{a}}}{{{c}}}\\).",
        "In right triangle \\(\\triangle ABC\\), evaluate \\(1 - \\cos^2 C\\) if \\(\\cos C = \\frac{{{a}}}{{{c}}}\\)."
    ]
    
    data_6 = [(1,1,"\\sqrt{2}","2"), (2,1,"\\sqrt{5}","5"), (3,1,"\\sqrt{10}","10"), (3,2,"\\sqrt{13}","13"), (4,1,"\\sqrt{17}","17"), (5,2,"\\sqrt{29}","29"), (6,1,"\\sqrt{37}","37"), (5,3,"\\sqrt{34}","34"), (5,4,"\\sqrt{41}","41"), (7,1,"\\sqrt{50}","50")]
    tmpls_6 = [
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), side \\(BC = {b}\\) and \\(AB = {a}\\). What is \\(\\cos C\\)?",
        "Given legs \\(BC = {b}\\) and \\(AB = {a}\\) in right \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), find \\(\\cos C\\).",
        "Calculate \\(\\cos C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with legs \\(BC = {b}\\) and \\(AB = {a}\\).",
        "In right-angled \\(\\triangle ABC\\), \\(BC = {b}\\) and \\(AB = {a}\\). Determine \\(\\cos C\\).",
        "Find the cosine ratio \\(\\cos C\\) for \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) where \\(BC = {b}\\) and \\(AB = {a}\\).",
        "Compute \\(\\cos C\\) in right triangle \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) having legs \\(BC = {b}\\) and \\(AB = {a}\\).",
        "Evaluate \\(\\cos C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with legs \\(BC = {b}\\) and \\(AB = {a}\\).",
        "For \\(\\triangle ABC\\) right-angled at \\(B\\), find \\(\\cos C\\) if \\(BC = {b}\\) and \\(AB = {a}\\).",
        "What is the exact value of \\(\\cos C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with \\(BC = {b}\\) and \\(AB = {a}\\)?",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), determine \\(\\cos C\\) given legs \\(BC = {b}\\) and \\(AB = {a}\\)."
    ]
    
    data_7 = [
        ("0^\\circ", "1", ["0", "\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}"]),
        ("30^\\circ", "\\frac{\\sqrt{3}}{2}", ["\\frac{1}{2}", "\\frac{1}{\\sqrt{2}}", "1"]),
        ("45^\\circ", "\\frac{1}{\\sqrt{2}}", ["\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}", "0"]),
        ("60^\\circ", "\\frac{1}{2}", ["\\frac{\\sqrt{3}}{2}", "\\frac{1}{\\sqrt{2}}", "1"]),
        ("90^\\circ", "0", ["1", "\\frac{1}{2}", "\\text{undefined}"]),
        ("30^\\circ \\text{ squared}", "\\frac{3}{4}", ["\\frac{1}{4}", "\\frac{1}{2}", "\\frac{1}{8}"]),
        ("45^\\circ \\text{ squared}", "\\frac{1}{2}", ["\\frac{1}{4}", "\\frac{3}{4}", "1"]),
        ("60^\\circ \\text{ squared}", "\\frac{1}{4}", ["\\frac{3}{4}", "\\frac{1}{2}", "\\frac{3}{2}"]),
        ("60^\\circ + \\cos 0^\\circ", "\\frac{3}{2}", ["1", "\\frac{1}{2}", "2"]),
        ("30^\\circ - \\cos 60^\\circ", "\\frac{\\sqrt{3}-1}{2}", ["\\frac{\\sqrt{3}+1}{2}", "\\frac{1}{2}", "0"])
    ]
    tmpls_7 = [
        "In right triangle trigonometry, what is the exact standard value of \\(\\cos 0^\\circ\\)?",
        "What is the exact numerical value of \\(\\cos 30^\\circ\\) derived from a 30°-60°-90° right triangle?",
        "Find the exact value of \\(\\cos 45^\\circ\\) in a 45°-45°-90° right-angled triangle.",
        "Evaluate the exact trigonometric ratio \\(\\cos 60^\\circ\\).",
        "What is the value of \\(\\cos 90^\\circ\\) in standard trigonometry?",
        "Compute the exact value of \\(\\cos^2 30^\\circ\\).",
        "Evaluate the squared cosine ratio \\(\\cos^2 45^\\circ\\).",
        "Determine the exact value of \\(\\cos^2 60^\\circ\\).",
        "Calculate the sum \\(\\cos 60^\\circ + \\cos 0^\\circ\\).",
        "Find the exact difference \\(\\cos 30^\\circ - \\cos 60^\\circ\\)."
    ]
    
    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        
        if arch == 0:
            a, b, c = triples_0[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {b}", f"BC = {a}", f"AC = {c}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(a=a, c=c)
            corr = f"\\(\\frac{{{a}}}{{{c}}}\\)"
            dist = [f"\\(\\frac{{{b}}}{{{c}}}\\)", f"\\(\\frac{{{a}}}{{{b}}}\\)", f"\\(\\frac{{{c}}}{{{a}}}\\)"]
            sol = f"**Step 1: Formula**\n\\(\\cos C = \\frac{{\\text{{Side adjacent to }} \\angle C}}{{\\text{{Hypotenuse}}}} = \\frac{{BC}}{{AC}} = \\frac{{{a}}}{{{c}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{a}}}{{{c}}}\\)."
        elif arch == 1:
            a, b, c = triples_1[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {a}", f"BC = {b}", f"AC = {c}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(a=a, c=c)
            corr = f"\\(\\frac{{{a}}}{{{c}}}\\)"
            dist = [f"\\(\\frac{{{b}}}{{{c}}}\\)", f"\\(\\frac{{{a}}}{{{b}}}\\)", f"\\(\\frac{{{c}}}{{{a}}}\\)"]
            sol = f"**Step 1: Formula**\n\\(\\cos A = \\frac{{\\text{{Side adjacent to }} \\angle A}}{{\\text{{Hypotenuse}}}} = \\frac{{AB}}{{AC}} = \\frac{{{a}}}{{{c}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{a}}}{{{c}}}\\)."
        elif arch == 2:
            a, c, ac, ans = data_2[sub_idx]
            svg = svg_trig("A", "B", "C", "", f"BC = ?", f"AC = {ac}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(a=a, c=c, ac=ac)
            corr = f"{ans}"
            dist = [f"{ans + 2}", f"{ans - 2 if ans > 2 else ans + 4}", f"{ans * 2}"]
            sol = f"**Step 1: Cross multiplication**\n\\(\\cos C = \\frac{{BC}}{{AC}} \\implies \\frac{{{a}}}{{{c}}} = \\frac{{BC}}{{{ac}}}\\).\n\\(BC = \\frac{{{a} \\times {ac}}}{{{c}}} = {ans}\\).\n**Step 2: Conclusion**\n{ans}."
        elif arch == 3:
            a, c, bc, ans = data_3[sub_idx]
            svg = svg_trig("A", "B", "C", "", f"BC = {bc}", "AC = ?") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(a=a, c=c, bc=bc)
            corr = f"{ans}"
            dist = [f"{ans + 5}", f"{ans - 5 if ans > 5 else ans + 8}", f"{ans * 2}"]
            sol = f"**Step 1: Cross multiplication**\n\\(\\cos C = \\frac{{BC}}{{AC}} \\implies \\frac{{{a}}}{{{c}}} = \\frac{{{bc}}}{{AC}}\\).\n\\(AC = \\frac{{{c} \\times {bc}}}{{{a}}} = {ans}\\).\n**Step 2: Conclusion**\n{ans}."
        elif arch == 4:
            a, c, sq_a, sq_c = data_4[sub_idx]
            svg = svg_trig("A", "B", "C", "", f"BC = {a}", f"AC = {c}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(a=a, c=c)
            corr = f"\\(\\frac{{{sq_a}}}{{{sq_c}}}\\)"
            dist = [f"\\(\\frac{{{a * 2}}}{{{c * 2}}}\\)", f"\\(\\frac{{{sq_a + 2}}}{{{sq_c}}}\\)", f"\\(\\frac{{{sq_a}}}{{{sq_c + 5}}}\\)"]
            sol = f"**Step 1: Square ratio**\n\\(\\cos^2 C = (\\frac{{{a}}}{{{c}}})^2 = \\frac{{{sq_a}}}{{{sq_c}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{sq_a}}}{{{sq_c}}}\\)."
        elif arch == 5:
            a, c, sq_sub, sq_c = data_5[sub_idx]
            svg = svg_trig("A", "B", "C", "", f"BC = {a}", f"AC = {c}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(a=a, c=c)
            corr = f"\\(\\frac{{{sq_sub}}}{{{sq_c}}}\\)"
            dist = [f"\\(\\frac{{{sq_sub - 2}}}{{{sq_c}}}\\)", f"\\(\\frac{{{sq_sub}}}{{{sq_c + 4}}}\\)", f"\\(\\frac{{{a}}}{{{c}}}\\)"]
            sol = f"**Step 1: Evaluate identity**\n\\(1 - \\cos^2 C = 1 - \\frac{{{a*a}}}{{{sq_c}}} = \\frac{{{sq_c - a*a}}}{{{sq_c}}} = \\frac{{{sq_sub}}}{{{sq_c}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{sq_sub}}}{{{sq_c}}}\\)."
        elif arch == 6:
            a, b, rad, rad_sq = data_6[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {a}", f"BC = {b}", f"AC = {rad}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(a=a, b=b)
            corr = f"\\(\\frac{{{b}}}{{{rad}}}\\)"
            dist = [f"\\(\\frac{{{a}}}{{{rad}}}\\)", f"\\(\\frac{{{b}}}{{{a}}}\\)", f"\\(\\frac{{{rad}}}{{{b}}}\\)"]
            sol = f"**Step 1: Pythagoras theorem**\n\\(AC = \\sqrt{{{a}^2 + {b}^2}} = {rad}\\).\n**Step 2: Cosine formula**\n\\(\\cos C = \\frac{{BC}}{{AC}} = \\frac{{{b}}}{{{rad}}}\\).\n**Step 3: Conclusion**\n\\(\\frac{{{b}}}{{{rad}}}\\)."
        else:
            tag, ans_c, dist_c = data_7[sub_idx]
            txt = tmpls_7[sub_idx]
            corr = f"\\({ans_c}\\)" if not ans_c.startswith("\\") and any(c in ans_c for c in "+-/*") else (ans_c if ans_c.startswith("\\") else f"\\({ans_c}\\)")
            dist = [d if d.startswith("\\") else f"\\({d}\\)" for d in dist_c]
            sol = f"**Step 1: Geometric evaluation**\nFrom standard trigonometric values, the exact value is {corr}.\n**Step 2: Conclusion**\n{corr}."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def main():
    q1 = gen_8_1_1()
    q2 = gen_8_1_2()
    print("8.1.1 count:", len(q1))
    print("8.1.2 count:", len(q2))
    all_qs = q1 + q2
    with open("scripts/mh9_mth2_ch8_test.json", "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2)

if __name__ == "__main__":
    main()
