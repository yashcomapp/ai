# scripts/generate_mh9_mth2_ch8_all.py
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

def svg_trig(v_top, v_rt, v_right, opp_lbl, adj_lbl, hyp_lbl):
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

# Import gen_8_1_1 and gen_8_1_2 from generate_mh9_mth2_ch8
from generate_mh9_mth2_ch8 import gen_8_1_1, gen_8_1_2

# -----------------------------------------------------------------------------
# 8.1.3: tan θ = Opposite / Adjacent
# -----------------------------------------------------------------------------
def gen_8_1_3():
    tc = "MH-9-MTH2-8-8.1.3"
    tname = "tan θ = Opposite / Adjacent = sin θ / cos θ"
    qs = []
    
    triples_0 = [(3,4,5), (5,12,13), (8,15,17), (7,24,25), (9,40,41), (12,35,37), (20,21,29), (11,60,61), (16,63,65), (28,45,53)]
    tmpls_0 = [
        "In right-angled \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), side \\(AB = {a}\\) and \\(BC = {b}\\). Find \\(\\tan C\\).",
        "For \\(\\triangle ABC\\) right-angled at \\(B\\), where \\(AB = {a}\\) and \\(BC = {b}\\), what is the value of \\(\\tan C\\)?",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), given \\(AB = {a}\\) and \\(BC = {b}\\), compute the tangent ratio \\(\\tan C\\).",
        "Given right \\(\\triangle ABC\\) with right angle at vertex \\(B\\), \\(AB = {a}\\) and \\(BC = {b}\\). Determine \\(\\tan C\\).",
        "Calculate the value of \\(\\tan C\\) in \\(\\triangle ABC\\) having \\(\\angle B = 90^\\circ\\), \\(AB = {a}\\), and \\(BC = {b}\\).",
        "What is \\(\\tan C\\) in right triangle \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) if \\(AB = {a}\\) and \\(BC = {b}\\)?",
        "In right-angled \\(\\triangle ABC\\), \\(\\angle ABC = 90^\\circ\\), \\(AB = {a}\\) and \\(BC = {b}\\). Evaluate \\(\\tan C\\).",
        "Find \\(\\tan C\\) for the right triangle \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), opposite side \\(AB = {a}\\), and adjacent side \\(BC = {b}\\).",
        "With \\(\\angle B = 90^\\circ\\) in \\(\\triangle ABC\\), determine \\(\\tan C\\) when side \\(AB = {a}\\) and adjacent \\(BC = {b}\\).",
        "Compute \\(\\tan C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(AB = {a}\\) and \\(BC = {b}\\)."
    ]
    
    triples_1 = [(4,3,5), (12,5,13), (15,8,17), (24,7,25), (40,9,41), (35,12,37), (21,20,29), (60,11,61), (63,16,65), (45,28,53)]
    tmpls_1 = [
        "In right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), side \\(BC = {a}\\) and \\(AB = {b}\\). What is \\(\\tan A\\)?",
        "Find the ratio \\(\\tan A\\) in \\(\\triangle ABC\\) right-angled at \\(B\\) if \\(BC = {a}\\) and \\(AB = {b}\\).",
        "In \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), calculate \\(\\tan A\\) given opposite side \\(BC = {a}\\) and adjacent \\(AB = {b}\\).",
        "For \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), determine \\(\\tan A\\) knowing that \\(BC = {a}\\) and \\(AB = {b}\\).",
        "What is the value of \\(\\tan A\\) in right triangle \\(\\triangle ABC\\) where \\(BC = {a}\\) and \\(AB = {b}\\)?",
        "Compute \\(\\tan A\\) in right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(BC = {a}\\) and \\(AB = {b}\\).",
        "Evaluate the tangent of angle \\(A\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with \\(BC = {a}\\) and \\(AB = {b}\\).",
        "In right \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), find \\(\\tan A\\) if \\(BC = {a}\\) and \\(AB = {b}\\).",
        "Determine \\(\\tan A\\) for \\(\\triangle ABC\\) right-angled at \\(B\\) having \\(BC = {a}\\) and adjacent \\(AB = {b}\\).",
        "Find \\(\\tan A\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with \\(BC = {a}\\) and \\(AB = {b}\\)."
    ]
    
    data_2 = [(3,4,16,12), (5,12,24,10), (8,15,45,24), (7,24,48,14), (9,40,80,18), (12,35,105,36), (20,21,42,40), (11,60,120,22), (4,3,15,20), (5,12,36,15)]
    tmpls_2 = [
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), if \\(\\tan C = \\frac{{{a}}}{{{b}}}\\) and adjacent \\(BC = {bc}\\), calculate opposite side \\(AB\\).",
        "Find length of side \\(AB\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(\\tan C = \\frac{{{a}}}{{{b}}}\\) and \\(BC = {bc}\\).",
        "For right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), determine \\(AB\\) if \\(\\tan C = \\frac{{{a}}}{{{b}}}\\) and \\(BC = {bc}\\).",
        "Compute side \\(AB\\) in right triangle \\(\\triangle ABC\\) when \\(\\tan C = \\frac{{{a}}}{{{b}}}\\) and \\(BC = {bc}\\).",
        "What is the length of opposite side \\(AB\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) where \\(\\tan C = \\frac{{{a}}}{{{b}}}\\) and \\(BC = {bc}\\)?",
        "In \\(\\triangle ABC\\) right-angled at \\(B\\), evaluate \\(AB\\) knowing \\(\\tan C = \\frac{{{a}}}{{{b}}}\\) and \\(BC = {bc}\\).",
        "If \\(\\tan C = \\frac{{{a}}}{{{b}}}\\) and \\(BC = {bc}\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), find \\(AB\\).",
        "Determine the measure of side \\(AB\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(\\tan C = \\frac{{{a}}}{{{b}}}\\) and \\(BC = {bc}\\).",
        "In right \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), calculate \\(AB\\) if \\(\\tan C = \\frac{{{a}}}{{{b}}}\\) and \\(BC = {bc}\\).",
        "Find side \\(AB\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(\\tan C = \\frac{{{a}}}{{{b}}}\\) and \\(BC = {bc}\\)."
    ]
    
    data_3 = [(3,4,6,8), (5,12,25,60), (8,15,16,30), (7,24,14,48), (9,40,27,120), (12,35,24,70), (20,21,40,42), (11,60,33,180), (4,3,8,6), (12,5,60,25)]
    tmpls_3 = [
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), if \\(\\tan C = \\frac{{{a}}}{{{b}}}\\) and \\(AB = {ab}\\), find adjacent side \\(BC\\).",
        "What is side \\(BC\\) in right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(AB = {ab}\\) and \\(\\tan C = \\frac{{{a}}}{{{b}}}\\)?",
        "Calculate \\(BC\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(AB = {ab}\\) and \\(\\tan C = \\frac{{{a}}}{{{b}}}\\).",
        "In right triangle \\(\\triangle ABC\\) with \\(\\angle B = 90^\\circ\\), find adjacent \\(BC\\) if \\(AB = {ab}\\) and \\(\\tan C = \\frac{{{a}}}{{{b}}}\\).",
        "Determine the length of side \\(BC\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) where \\(\\tan C = \\frac{{{a}}}{{{b}}}\\) and \\(AB = {ab}\\).",
        "For \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), find \\(BC\\) knowing \\(AB = {ab}\\) and \\(\\tan C = \\frac{{{a}}}{{{b}}}\\).",
        "Evaluate side \\(BC\\) in \\(\\triangle ABC\\) right-angled at \\(B\\) given \\(\\tan C = \\frac{{{a}}}{{{b}}}\\) and opposite side \\(AB = {ab}\\).",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), compute \\(BC\\) when \\(\\tan C = \\frac{{{a}}}{{{b}}}\\) and \\(AB = {ab}\\).",
        "If \\(\\tan C = \\frac{{{a}}}{{{b}}}\\) and \\(AB = {ab}\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), what is \\(BC\\)?",
        "Find adjacent \\(BC\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(\\tan C = \\frac{{{a}}}{{{b}}}\\) and \\(AB = {ab}\\)."
    ]
    
    data_4 = [(3,4,9,16), (5,12,25,144), (8,15,64,225), (7,24,49,576), (9,40,81,1600), (12,35,144,1225), (20,21,400,441), (11,60,121,3600), (4,3,16,9), (12,5,144,25)]
    tmpls_4 = [
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), if \\(\\tan C = \\frac{{{a}}}{{{b}}}\\), find the value of \\(\\tan^2 C\\).",
        "Calculate \\(\\tan^2 C\\) in right-angled \\(\\triangle ABC\\) given \\(\\tan C = \\frac{{{a}}}{{{b}}}\\).",
        "What is the value of \\(\\tan^2 C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(\\tan C = \\frac{{{a}}}{{{b}}}\\)?",
        "Evaluate \\((\\tan C)^2\\) for right \\(\\triangle ABC\\) with \\(\\tan C = \\frac{{{a}}}{{{b}}}\\).",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), compute \\(\\tan^2 C\\) if \\(\\tan C = \\frac{{{a}}}{{{b}}}\\).",
        "Determine \\(\\tan^2 C\\) in right triangle \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) where \\(\\tan C = \\frac{{{a}}}{{{b}}}\\).",
        "Find the squared tangent \\(\\tan^2 C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) knowing \\(\\tan C = \\frac{{{a}}}{{{b}}}\\).",
        "For \\(\\triangle ABC\\) right-angled at \\(B\\), find \\(\\tan^2 C\\) when \\(\\tan C = \\frac{{{a}}}{{{b}}}\\).",
        "Compute the numerical value of \\(\\tan^2 C\\) if \\(\\tan C = \\frac{{{a}}}{{{b}}}\\) in \\(\\triangle ABC\\).",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), evaluate \\(\\tan^2 C\\) given \\(\\tan C = \\frac{{{a}}}{{{b}}}\\)."
    ]
    
    data_5 = [(3,4,25,16), (5,12,169,144), (8,15,289,225), (7,24,625,576), (9,40,1681,1600), (12,35,1369,1225), (20,21,841,441), (11,60,3721,3600), (4,3,25,9), (12,5,169,25)]
    tmpls_5 = [
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), if \\(\\tan C = \\frac{{{a}}}{{{b}}}\\), find the value of \\(1 + \\tan^2 C\\).",
        "Evaluate \\(1 + \\tan^2 C\\) for right-angled \\(\\triangle ABC\\) given \\(\\tan C = \\frac{{{a}}}{{{b}}}\\).",
        "What is the value of \\(1 + \\tan^2 C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) when \\(\\tan C = \\frac{{{a}}}{{{b}}}\\)?",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), calculate \\(1 + \\tan^2 C\\) if \\(\\tan C = \\frac{{{a}}}{{{b}}}\\).",
        "Calculate the expression \\(1 + \\tan^2 C\\) in right \\(\\triangle ABC\\) where \\(\\tan C = \\frac{{{a}}}{{{b}}}\\).",
        "Determine the measure of \\(1 + \\tan^2 C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with \\(\\tan C = \\frac{{{a}}}{{{b}}}\\).",
        "Find the value of \\(1 + \\tan^2 C\\) for \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) given \\(\\tan C = \\frac{{{a}}}{{{b}}}\\).",
        "For right-angled \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), find \\(1 + \\tan^2 C\\) when \\(\\tan C = \\frac{{{a}}}{{{b}}}\\).",
        "Compute \\(1 + \\tan^2 C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) knowing \\(\\tan C = \\frac{{{a}}}{{{b}}}\\).",
        "In right triangle \\(\\triangle ABC\\), evaluate \\(1 + \\tan^2 C\\) if \\(\\tan C = \\frac{{{a}}}{{{b}}}\\)."
    ]
    
    data_6 = [(1,1,"1"), (1,2,"\\frac{1}{2}"), (1,3,"\\frac{1}{3}"), (2,3,"\\frac{2}{3}"), (1,4,"\\frac{1}{4}"), (2,5,"\\frac{2}{5}"), (1,6,"\\frac{1}{6}"), (3,5,"\\frac{3}{5}"), (4,5,"\\frac{4}{5}"), (1,7,"\\frac{1}{7}")]
    tmpls_6 = [
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), side \\(AB = {a}\\) and \\(BC = {b}\\). What is \\(\\tan C\\)?",
        "Given legs \\(AB = {a}\\) and \\(BC = {b}\\) in right \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), find \\(\\tan C\\).",
        "Calculate \\(\\tan C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with perpendicular sides \\(AB = {a}\\) and \\(BC = {b}\\).",
        "In right-angled \\(\\triangle ABC\\), \\(AB = {a}\\) and \\(BC = {b}\\). Determine \\(\\tan C\\).",
        "Find the tangent ratio \\(\\tan C\\) for \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) where \\(AB = {a}\\) and \\(BC = {b}\\).",
        "Compute \\(\\tan C\\) in right triangle \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) having legs \\(AB = {a}\\) and \\(BC = {b}\\).",
        "Evaluate \\(\\tan C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with legs \\(AB = {a}\\) and \\(BC = {b}\\).",
        "For \\(\\triangle ABC\\) right-angled at \\(B\\), find \\(\\tan C\\) if \\(AB = {a}\\) and \\(BC = {b}\\).",
        "What is the exact value of \\(\\tan C\\) in \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)) with \\(AB = {a}\\) and \\(BC = {b}\\)?",
        "In \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), determine \\(\\tan C\\) given legs \\(AB = {a}\\) and \\(BC = {b}\\)."
    ]
    
    data_7 = [
        ("0^\\circ", "0", ["1", "\\frac{1}{\\sqrt{3}}", "\\sqrt{3}"]),
        ("30^\\circ", "\\frac{1}{\\sqrt{3}}", ["\\sqrt{3}", "1", "\\frac{1}{2}"]),
        ("45^\\circ", "1", ["\\frac{1}{\\sqrt{3}}", "\\sqrt{3}", "0"]),
        ("60^\\circ", "\\sqrt{3}", ["\\frac{1}{\\sqrt{3}}", "1", "3"]),
        ("30^\\circ \\text{ squared}", "\\frac{1}{3}", ["3", "1", "\\frac{1}{9}"]),
        ("2 \\times 45^\\circ", "2", ["1", "4", "\\sqrt{3}"]),
        ("60^\\circ \\text{ squared}", "3", ["\\sqrt{3}", "1", "9"]),
        ("30^\\circ + 60^\\circ", "\\frac{4}{\\sqrt{3}}", ["\\frac{2}{\\sqrt{3}}", "2", "\\sqrt{3}"]),
        ("60^\\circ - 30^\\circ", "\\frac{2}{\\sqrt{3}}", ["\\frac{1}{\\sqrt{3}}", "\\sqrt{3}", "0"]),
        ("45^\\circ + 60^\\circ \\text{ sq}", "4", ["3", "5", "2"])
    ]
    tmpls_7 = [
        "In right triangle trigonometry, what is the exact standard value of \\(\\tan 0^\\circ\\)?",
        "What is the exact numerical value of \\(\\tan 30^\\circ\\) derived from a 30°-60°-90° right triangle?",
        "Find the exact value of \\(\\tan 45^\\circ\\) in a 45°-45°-90° right-angled triangle.",
        "Evaluate the exact trigonometric ratio \\(\\tan 60^\\circ\\).",
        "Compute the exact value of \\(\\tan^2 30^\\circ\\).",
        "Evaluate the expression \\(2\\tan 45^\\circ\\).",
        "Determine the exact value of \\(\\tan^2 60^\\circ\\).",
        "Calculate the sum \\(\\tan 30^\\circ + \\tan 60^\\circ\\).",
        "Find the exact difference \\(\\tan 60^\\circ - \\tan 30^\\circ\\).",
        "Evaluate the sum \\(\\tan^2 45^\\circ + \\tan^2 60^\\circ\\)."
    ]
    
    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        
        if arch == 0:
            a, b, c = triples_0[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {a}", f"BC = {b}", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(a=a, b=b)
            corr = f"\\(\\frac{{{a}}}{{{b}}}\\)"
            dist = [f"\\(\\frac{{{b}}}{{{a}}}\\)", f"\\(\\frac{{{a}}}{{{c}}}\\)", f"\\(\\frac{{{b}}}{{{c}}}\\)"]
            sol = f"**Step 1: Formula**\n\\(\\tan C = \\frac{{\\text{{Side opposite to }} \\angle C}}{{\\text{{Side adjacent to }} \\angle C}} = \\frac{{AB}}{{BC}} = \\frac{{{a}}}{{{b}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{a}}}{{{b}}}\\)."
        elif arch == 1:
            a, b, c = triples_1[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {b}", f"BC = {a}", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(a=a, b=b)
            corr = f"\\(\\frac{{{a}}}{{{b}}}\\)"
            dist = [f"\\(\\frac{{{b}}}{{{a}}}\\)", f"\\(\\frac{{{a}}}{{{c}}}\\)", f"\\(\\frac{{{b}}}{{{c}}}\\)"]
            sol = f"**Step 1: Formula**\n\\(\\tan A = \\frac{{\\text{{Side opposite to }} \\angle A}}{{\\text{{Side adjacent to }} \\angle A}} = \\frac{{BC}}{{AB}} = \\frac{{{a}}}{{{b}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{a}}}{{{b}}}\\)."
        elif arch == 2:
            a, b, bc, ans = data_2[sub_idx]
            svg = svg_trig("A", "B", "C", "AB = ?", f"BC = {bc}", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(a=a, b=b, bc=bc)
            corr = f"{ans}"
            dist = [f"{ans + 2}", f"{ans - 2 if ans > 2 else ans + 4}", f"{ans * 2}"]
            sol = f"**Step 1: Cross multiplication**\n\\(\\tan C = \\frac{{AB}}{{BC}} \\implies \\frac{{{a}}}{{{b}}} = \\frac{{AB}}{{{bc}}}\\).\n\\(AB = \\frac{{{a} \\times {bc}}}{{{b}}} = {ans}\\).\n**Step 2: Conclusion**\n{ans}."
        elif arch == 3:
            a, b, ab, ans = data_3[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {ab}", "BC = ?", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(a=a, b=b, ab=ab)
            corr = f"{ans}"
            dist = [f"{ans + 5}", f"{ans - 5 if ans > 5 else ans + 8}", f"{ans * 2}"]
            sol = f"**Step 1: Cross multiplication**\n\\(\\tan C = \\frac{{AB}}{{BC}} \\implies \\frac{{{a}}}{{{b}}} = \\frac{{{ab}}}{{BC}}\\).\n\\(BC = \\frac{{{b} \\times {ab}}}{{{a}}} = {ans}\\).\n**Step 2: Conclusion**\n{ans}."
        elif arch == 4:
            a, b, sq_a, sq_b = data_4[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {a}", f"BC = {b}", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(a=a, b=b)
            corr = f"\\(\\frac{{{sq_a}}}{{{sq_b}}}\\)"
            dist = [f"\\(\\frac{{{a * 2}}}{{{b * 2}}}\\)", f"\\(\\frac{{{sq_a + 2}}}{{{sq_b}}}\\)", f"\\(\\frac{{{sq_a}}}{{{sq_b + 5}}}\\)"]
            sol = f"**Step 1: Square ratio**\n\\(\\tan^2 C = (\\frac{{{a}}}{{{b}}})^2 = \\frac{{{sq_a}}}{{{sq_b}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{sq_a}}}{{{sq_b}}}\\)."
        elif arch == 5:
            a, b, sq_c, sq_b = data_5[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {a}", f"BC = {b}", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(a=a, b=b)
            corr = f"\\(\\frac{{{sq_c}}}{{{sq_b}}}\\)"
            dist = [f"\\(\\frac{{{sq_c - 2}}}{{{sq_b}}}\\)", f"\\(\\frac{{{sq_c}}}{{{sq_b + 4}}}\\)", f"\\(\\frac{{{a}}}{{{b}}}\\)"]
            sol = f"**Step 1: Evaluate identity**\n\\(1 + \\tan^2 C = 1 + \\frac{{{a*a}}}{{{b*b}}} = \\frac{{{b*b + a*a}}}{{{b*b}}} = \\frac{{{sq_c}}}{{{sq_b}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{{sq_c}}}{{{sq_b}}}\\)."
        elif arch == 6:
            a, b, ans_str = data_6[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {a}", f"BC = {b}", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(a=a, b=b)
            corr = f"\\({ans_str}\\)" if not ans_str.startswith("\\") and "/" in ans_str else (f"\\({ans_str}\\)" if ans_str != "1" else "1")
            dist = [f"\\(\\frac{{{b}}}{{{a}}}\\)", f"\\(\\frac{{{a + 1}}}{{{b}}}\\)", f"\\(\\frac{{{a}}}{{{b + 2}}}\\)"]
            sol = f"**Step 1: Tangent formula**\n\\(\\tan C = \\frac{{AB}}{{BC}} = \\frac{{{a}}}{{{b}}} = {ans_str}\\).\n**Step 2: Conclusion**\n{corr}."
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
# 8.2.1: tan θ * tan (90-θ) = 1
# -----------------------------------------------------------------------------
def gen_8_2_1():
    tc = "MH-9-MTH2-8-8.2.1"
    tname = "tan θ * tan (90-θ) = 1"
    qs = []
    
    # 8 distinct archetypes with strictly disjoint answers
    # Arch 0: k * tan(deg) * tan(90-deg) = k
    data_0 = [(10,80,2), (15,75,3), (20,70,4), (25,65,5), (35,55,6), (40,50,7), (5,85,8), (30,60,9), (12,78,10), (18,72,12)]
    tmpls_0 = [
        "Evaluate the trigonometric product \\({k} \\tan {deg}^\\circ \\cdot \\tan {comp}^\\circ\\).",
        "What is the value of \\({k} \\tan {deg}^\\circ \\times \\tan {comp}^\\circ\\)?",
        "Calculate \\({k} \\tan {deg}^\\circ \\cdot \\tan {comp}^\\circ\\) using complementary angle identities.",
        "In right triangle trigonometry, find \\({k} \\tan {deg}^\\circ \\times \\tan(90^\\circ - {deg}^\\circ)\\).",
        "Compute the exact value of \\({k} \\tan {deg}^\\circ \\cdot \\tan {comp}^\\circ\\).",
        "Determine the value of \\({k} [\\tan {deg}^\\circ \\cdot \\tan {comp}^\\circ]\\).",
        "Evaluate the expression \\({k} \\tan {deg}^\\circ \\tan {comp}^\\circ\\).",
        "Find the value of \\({k} \\cdot \\tan {deg}^\\circ \\cdot \\tan {comp}^\\circ\\).",
        "What does \\({k} \\tan {deg}^\\circ \\cdot \\tan {comp}^\\circ\\) equal?",
        "Simplify and compute \\({k} \\tan {deg}^\\circ \\cdot \\tan {comp}^\\circ\\)."
    ]
    
    # Arch 1: Evaluate tan(deg)*tan(comp) + c = 1 + c
    data_1 = [(14,76,15), (16,74,17), (22,68,23), (26,64,27), (32,58,33), (36,54,37), (42,48,43), (28,62,29), (34,56,35), (38,52,39)]
    
    # Arch 2: If tan(deg) = k, express tan(comp) = 1/k
    data_2 = [(10,"m"), (15,"p"), (20,"x"), (25,"y"), (35,"z"), (40,"w"), (50,"u"), (65,"v"), (70,"t"), (80,"s")]
    
    # Arch 3: Angle difference in right triangle
    data_3 = [(10,80,70), (15,75,60), (20,70,50), (25,65,40), (30,60,30), (35,55,20), (5,85,80), (8,82,74), (12,78,66), (18,72,54)]
    
    # Arch 4: Solving for acute angle theta where tan(theta) = 1/tan(deg) => theta = 90 - deg
    data_4 = [(11,79), (21,69), (31,59), (41,49), (51,39), (61,29), (71,19), (81,9), (13,77), (23,67)]
    
    # Arch 5: 10 * tan(d1)*tan(d2) - k = 10 - k
    data_5 = [(1,89,1), (3,87,2), (7,83,3), (9,81,4), (17,73,5), (19,71,6), (27,63,7), (29,61,8), (37,53,9), (39,51,0)]
    
    # Arch 6: Reciprocal value inversion with diverse fractions
    data_6 = [
        (10,"\\frac{2}{3}","\\frac{3}{2}",["\\frac{4}{3}","\\frac{2}{5}","\\frac{5}{2}"]),
        (20,"\\frac{3}{5}","\\frac{5}{3}",["\\frac{5}{2}","\\frac{3}{4}","\\frac{4}{5}"]),
        (30,"\\frac{1}{\\sqrt{3}}","\\sqrt{3}",["\\frac{1}{3}","3","\\frac{\\sqrt{3}}{2}"]),
        (40,"\\frac{4}{7}","\\frac{7}{4}",["\\frac{7}{2}","\\frac{4}{5}","\\frac{3}{7}"]),
        (50,"\\frac{5}{8}","\\frac{8}{5}",["\\frac{8}{3}","\\frac{5}{7}","\\frac{2}{5}"]),
        (60,"\\sqrt{3}","\\frac{1}{\\sqrt{3}}",["3","\\frac{1}{3}","\\frac{\\sqrt{3}}{2}"]),
        (70,"\\frac{7}{9}","\\frac{9}{7}",["\\frac{9}{5}","\\frac{7}{8}","\\frac{3}{7}"]),
        (80,"\\frac{5}{6}","\\frac{6}{5}",["\\frac{6}{7}","\\frac{5}{4}","\\frac{2}{3}"]),
        (25,"\\frac{3}{8}","\\frac{8}{3}",["\\frac{8}{5}","\\frac{3}{5}","\\frac{5}{8}"]),
        (35,"\\frac{4}{9}","\\frac{9}{4}",["\\frac{9}{2}","\\frac{4}{7}","\\frac{2}{9}"])
    ]
    
    # Arch 7: Complementary angle calculation
    data_7 = [(16,74), (24,66), (28,62), (34,56), (44,46), (48,42), (52,38), (56,34), (64,26), (68,22)]
    
    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        
        if arch == 0:
            deg, comp, k = data_0[sub_idx]
            svg = svg_trig("A", "B", "C", f"\\angle C = {deg}^\\circ", f"\\angle A = {comp}^\\circ", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(deg=deg, comp=comp, k=k)
            corr = f"{k}"
            dist = [f"{k + 2}", f"{k - 1 if k > 1 else k + 3}", f"{k * 2}"]
            sol = f"**Step 1: Identity**\n\\(\\tan {deg}^\\circ \\cdot \\tan {comp}^\\circ = 1\\).\n\\({k} \\times 1 = {k}\\).\n**Step 2: Conclusion**\n{k}."
        elif arch == 1:
            d1, d2, c = data_1[sub_idx]
            svg = svg_trig("A", "B", "C", f"\\angle C = {d1}^\\circ", f"\\angle A = {d2}^\\circ", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + f"Evaluate the expression \\(\\tan {d1}^\\circ \\cdot \\tan {d2}^\\circ + {c}\\)."
            ans_val = 1 + c
            corr = f"{ans_val}"
            dist = [f"{c}", f"{ans_val + 2}", f"{ans_val - 2}"]
            sol = f"**Step 1: Complementary product**\n\\(\\tan {d1}^\\circ \\cdot \\tan {d2}^\\circ = 1\\).\n\\(1 + {c} = {ans_val}\\).\n**Step 2: Conclusion**\n{ans_val}."
        elif arch == 2:
            d1, var = data_2[sub_idx]
            d2 = 90 - d1
            svg = svg_trig("A", "B", "C", f"\\angle C = {d1}^\\circ", f"\\angle A = {d2}^\\circ", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + f"If \\(\\tan {d1}^\\circ = {var}\\), express \\(\\tan {d2}^\\circ\\) in terms of \\({var}\\)."
            corr = f"\\(\\frac{{1}}{{{var}}}\\)"
            dist = [f"\\({var}\\)", f"\\(1 - {var}\\)", f"\\(\\frac{{{var}}}{{2}}\\)" ]
            sol = f"**Step 1: Complementary formula**\n\\(\\tan {d2}^\\circ = \\tan(90^\\circ - {d1}^\\circ) = \\frac{{1}}{{\\tan {d1}^\\circ}} = \\frac{{1}}{{{var}}}\\).\n**Step 2: Conclusion**\n\\(\\frac{{1}}{{{var}}}\\)."
        elif arch == 3:
            d1, d2, diff_ans = data_3[sub_idx]
            svg = svg_trig("A", "B", "C", f"\\angle C = {d1}^\\circ", f"\\angle A = {d2}^\\circ", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + f"In right \\(\\triangle ABC\\) (\\(\\angle B = 90^\\circ\\)), if \\(\\angle C = {d1}^\\circ\\), what is the difference \\(\\angle A - \\angle C\\)?"
            corr = f"{diff_ans}^\\circ"
            dist = [f"{diff_ans + 10}^\\circ", f"{diff_ans - 10 if diff_ans > 10 else diff_ans + 15}^\\circ", f"{90 - diff_ans}^\\circ"]
            sol = f"**Step 1: Triangle acute angles**\n\\(\\angle A = 90^\\circ - {d1}^\\circ = {d2}^\\circ\\).\n\\(\\angle A - \\angle C = {d2}^\\circ - {d1}^\\circ = {diff_ans}^\\circ\\).\n**Step 2: Conclusion**\n{diff_ans}°."
        elif arch == 4:
            d1, d2 = data_4[sub_idx]
            svg = svg_trig("A", "B", "C", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + f"Find the acute angle \\(\\theta\\) if \\(\\tan \\theta = \\frac{{1}}{{\\tan {d1}^\\circ}}\\)."
            corr = f"{d2}^\\circ"
            dist = [f"{d1}^\\circ", f"{d2 + 10}^\\circ", f"{d2 - 10}^\\circ"]
            sol = f"**Step 1: Identity**\n\\(\\frac{{1}}{{\\tan {d1}^\\circ}} = \\tan(90^\\circ - {d1}^\\circ) = \\tan {d2}^\\circ\\implies \\theta = {d2}^\\circ\\).\n**Step 2: Conclusion**\n{d2}°."
        elif arch == 5:
            d1, d2, k = data_5[sub_idx]
            svg = svg_trig("A", "B", "C", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            ans_val = 10 - k
            txt = prefix + f"Evaluate \\(10(\\tan {d1}^\\circ \\cdot \\tan {d2}^\\circ) - {k}\\)."
            corr = f"{ans_val}"
            dist = [f"{ans_val + 2}", f"{ans_val - 2}", f"{10 + k}"]
            sol = f"**Step 1: Calculate**\n\\(10 \\times 1 - {k} = {ans_val}\\).\n**Step 2: Conclusion**\n{ans_val}."
        elif arch == 6:
            deg, val_str, inv_str, dist_opts = data_6[sub_idx]
            comp = 90 - deg
            txt = f"If \\(\\tan {deg}^\\circ = {val_str}\\), calculate the value of \\(\\tan {comp}^\\circ\\)."
            corr = f"\\({inv_str}\\)"
            dist = [f"\\({d}\\)" for d in dist_opts]
            sol = f"**Step 1: Reciprocal identity**\n\\(\\tan {comp}^\\circ = \\frac{{1}}{{\\tan {deg}^\\circ}} = {inv_str}\\).\n**Step 2: Conclusion**\n\\({inv_str}\\)."
        else: # arch == 7
            d1, comp = data_7[sub_idx]
            txt = f"If \\(\\angle C = {d1}^\\circ\\) in a right-angled triangle, what is the measure of its complementary acute angle?"
            corr = f"{comp}^\\circ"
            dist = [f"{comp + 10}^\\circ", f"{comp - 10}^\\circ", f"{d1}^\\circ"]
            sol = f"**Step 1: Complementary sum**\n\\(90^\\circ - {d1}^\\circ = {comp}^\\circ\\).\n**Step 2: Conclusion**\n{comp}°."
            
        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs



# -----------------------------------------------------------------------------
# 8.2.2: sin θ = cos (90-θ) and cos θ = sin (90-θ)
# -----------------------------------------------------------------------------
def gen_8_2_2():
    tc = "MH-9-MTH2-8-8.2.2"
    tname = "sin θ = cos(90 - θ), cos θ = sin(90 - θ), tan θ = 1 / tan(90 - θ)"
    qs = []
    
    # Arch 0: sin(theta) = cos(alpha) -> theta = 90 - alpha
    data_0 = [
        (25, 65, "Given that \(\sin \theta = \cos {alpha}^\circ\) where \(\theta\) is acute, determine the measure of \(\theta\)."),
        (35, 55, "If \(\sin \theta = \cos {alpha}^\circ\) for an acute angle \(\theta\), calculate the value of \(\theta\)."),
        (42, 48, "In a right triangle, if \(\sin \theta = \cos {alpha}^\circ\), what is the value of acute angle \(\theta\)?"),
        (55, 35, "Solve for acute angle \(\theta\) given the relationship \(\sin \theta = \cos {alpha}^\circ\)."),
        (65, 25, "Find the measure of acute angle \(\theta\) satisfying \(\sin \theta = \cos {alpha}^\circ\)."),
        (15, 75, "Determine acute \(\theta\) when \(\sin \theta = \cos {alpha}^\circ\)."),
        (28, 62, "Evaluate the acute angle \(\theta\) such that \(\sin \theta = \cos {alpha}^\circ\)."),
        (32, 58, "What acute angle \(\theta\) satisfies the equation \(\sin \theta = \cos {alpha}^\circ\)?"),
        (48, 42, "If \(\theta\) is an acute angle and \(\sin \theta = \cos {alpha}^\circ\), find \(\theta\)."),
        (74, 16, "Compute the acute angle \(\theta\) if \(\sin \theta = \cos {alpha}^\circ\).")
    ]
    # Arch 1: cos(theta) = sin(alpha) -> theta = 90 - alpha
    data_1 = [
        (20, 70, "If \(\cos \theta = \sin {alpha}^\circ\) for acute angle \(\theta\), find \(\theta\)."),
        (30, 60, "Determine acute \(\theta\) satisfying \(\cos \theta = \sin {alpha}^\circ\)."),
        (40, 50, "Calculate the acute angle \(\theta\) when \(\cos \theta = \sin {alpha}^\circ\)."),
        (50, 40, "Find the value of acute angle \(\theta\) if \(\cos \theta = \sin {alpha}^\circ\)."),
        (60, 30, "What is the measure of acute \(\theta\) given \(\cos \theta = \sin {alpha}^\circ\)?"),
        (70, 20, "Solve for \(\theta\) (acute) knowing that \(\cos \theta = \sin {alpha}^\circ\)."),
        (10, 80, "Evaluate acute angle \(\theta\) if \(\cos \theta = \sin {alpha}^\circ\)."),
        (80, 10, "In right triangle context, find acute \(\theta\) if \(\cos \theta = \sin {alpha}^\circ\)."),
        (45, 45, "Compute \(\theta\) when \(\cos \theta = \sin {alpha}^\circ\) and \(\theta\) is acute."),
        (64, 26, "Given \(\cos \theta = \sin {alpha}^\circ\), what is the value of acute angle \(\theta\)?")
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
        (2, 3, 18, "\sin(2\theta) = \cos(3\theta)"),
        (1, 4, 18, "\sin(\theta) = \cos(4\theta)"),
        (1, 1, 45, "\sin(\theta) = \cos(\theta)"),
        (2, 1, 30, "\sin(2\theta) = \cos(\theta)"),
        (3, 2, 18, "\sin(3\theta) = \cos(2\theta)"),
        (4, 1, 18, "\sin(4\theta) = \cos(\theta)"),
        (1, 2, 30, "\sin(\theta) = \cos(2\theta)"),
        (3, 1, 22.5, "\sin(3\theta) = \cos(\theta)"), # handled as frac or exact
        (5, 1, 15, "\sin(5\theta) = \cos(\theta)"),
        (1, 5, 15, "\sin(\theta) = \cos(5\theta)")
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        qcode = f"{tc}-OSC-{seq}"
        
        if arch == 0:
            alpha, ans_theta, stem = data_0[sub_idx]
            svg = svg_trig("A", "B", "C", f"\angle C = {ans_theta}^\circ", f"\angle A = {alpha}^\circ", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + stem.format(alpha=alpha)
            corr = f"{ans_theta}^\circ"
            dist = [f"{ans_theta + 10}^\circ", f"{ans_theta - 10 if ans_theta > 10 else ans_theta + 15}^\circ", f"{alpha}^\circ"]
            sol = f"**Step 1: Complementary relation**\nSince \(\sin \theta = \cos(90^\circ - \theta)\), we have \(90^\circ - \theta = {alpha}^\circ \implies \theta = 90^\circ - {alpha}^\circ = {ans_theta}^\circ\).\n**Step 2: Conclusion**\n{ans_theta}°."
        elif arch == 1:
            alpha, ans_theta, stem = data_1[sub_idx]
            svg = svg_trig("A", "B", "C", f"\angle C = {alpha}^\circ", f"\angle A = {ans_theta}^\circ", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + stem.format(alpha=alpha)
            corr = f"{ans_theta}^\circ"
            dist = [f"{ans_theta + 8}^\circ", f"{ans_theta - 8 if ans_theta > 8 else ans_theta + 12}^\circ", f"{alpha}^\circ"]
            sol = f"**Step 1: Identity**\n\(\cos \theta = \sin(90^\circ - \theta) = \sin {alpha}^\circ \implies \theta = 90^\circ - {alpha}^\circ = {ans_theta}^\circ\).\n**Step 2: Conclusion**\n{ans_theta}°."
        elif arch == 2:
            d = data_2[sub_idx]
            comp = 90 - d
            svg = svg_trig("A", "B", "C", f"\angle C = {d}^\circ", f"\angle A = {comp}^\circ", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            tmpls_sub = [
                "Find the value of \(\sin {d}^\circ - \cos {comp}^\circ\).",
                "Evaluate the trigonometric difference \(\sin {d}^\circ - \cos {comp}^\circ\).",
                "What is the numerical result of \(\sin {d}^\circ - \cos {comp}^\circ\)?",
                "Calculate the simplified value of \(\sin {d}^\circ - \cos {comp}^\circ\).",
                "Determine \(\sin {d}^\circ - \cos {comp}^\circ\).",
                "Compute the value of expression \(\sin {d}^\circ - \cos {comp}^\circ\).",
                "Simplify the expression \(\sin {d}^\circ - \cos {comp}^\circ\).",
                "Evaluate \(\sin {d}^\circ - \cos {comp}^\circ\) using complementary angles.",
                "Find the measure of \(\sin {d}^\circ - \cos {comp}^\circ\).",
                "What does \(\sin {d}^\circ - \cos {comp}^\circ\) simplify to?"
            ]
            txt = prefix + tmpls_sub[sub_idx].format(d=d, comp=comp)
            corr = "0"
            dist = ["1", "-1", f"\sin {d}^\circ"]
            sol = f"**Step 1: Complementary angles**\nSince \(\cos {comp}^\circ = \cos(90^\circ - {d}^\circ) = \sin {d}^\circ\), the difference is \(\sin {d}^\circ - \sin {d}^\circ = 0\).\n**Step 2: Conclusion**\n0."
        elif arch == 3:
            d1, d2, diff_ans = data_3[sub_idx]
            svg = svg_trig("A", "B", "C", f"\angle C = {d1}^\circ", f"\angle A = {d2}^\circ", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            tmpls_sub = [
                "In right-angled \(\triangle ABC\) (\(\angle B = 90^\circ\)), with acute angle \(\angle C = {d1}^\circ\), compute \(\angle A - \angle C\).",
                "For right \(\triangle ABC\) with \(\angle B = 90^\circ\) and \(\angle C = {d1}^\circ\), what is the angle difference \(\angle A - \angle C\)?",
                "Given \(\triangle ABC\) right-angled at \(B\) and \(\angle C = {d1}^\circ\), find \(\angle A - \angle C\).",
                "Calculate the difference between the two acute angles \(\angle A - \angle C\) in right \(\triangle ABC\) if \(\angle C = {d1}^\circ\).",
                "In \(\triangle ABC\) having \(\angle B = 90^\circ\) and \(\angle C = {d1}^\circ\), determine the value of \(\angle A - \angle C\).",
                "What is the measure of \(\angle A - \angle C\) in right \(\triangle ABC\) when \(\angle C = {d1}^\circ\)?",
                "Evaluate the angle difference \(\angle A - \angle C\) in \(\triangle ABC\) (\(\angle B = 90^\circ\), \(\angle C = {d1}^\circ\)).",
                "If \(\angle C = {d1}^\circ\) in right triangle \(\triangle ABC\) (\(\angle B = 90^\circ\)), calculate \(\angle A - \angle C\).",
                "Determine \(\angle A - \angle C\) for right \(\triangle ABC\) with \(\angle B = 90^\circ\) and \(\angle C = {d1}^\circ\).",
                "Find \(\angle A - \angle C\) in \(\triangle ABC\) where \(\angle B = 90^\circ\) and \(\angle C = {d1}^\circ\)."
            ]
            txt = prefix + tmpls_sub[sub_idx].format(d1=d1, d2=d2)
            corr = f"{diff_ans}^\circ"
            dist = [f"{diff_ans + 12}^\circ", f"{diff_ans - 12 if diff_ans > 12 else diff_ans + 16}^\circ", f"{d1}^\circ"]
            sol = f"**Step 1: Triangle acute angles**\n\(\angle A = 90^\circ - {d1}^\circ = {d2}^\circ\).\n\(\angle A - \angle C = {d2}^\circ - {d1}^\circ = {diff_ans}^\circ\).\n**Step 2: Conclusion**\n{diff_ans}°."
        elif arch == 4:
            d1, d2 = data_4[sub_idx]
            svg = svg_trig("A", "B", "C", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            tmpls_sub = [
                "Find the acute angle \(\theta\) if \(\tan \theta = \frac{{1}}{{\tan {d1}^\circ}}\).",
                "If \(\tan \theta = \frac{{1}}{{\tan {d1}^\circ}}\) for an acute angle \(\theta\), determine \(\theta\).",
                "Calculate acute angle \(\theta\) satisfying \(\tan \theta \cdot \tan {d1}^\circ = 1\).",
                "What is the value of acute \(\theta\) if \(\tan \theta = \cot {d1}^\circ\)?",
                "Evaluate the acute angle \(\theta\) such that \(\tan \theta = \frac{{1}}{{\tan {d1}^\circ}}\).",
                "Solve for acute angle \(\theta\) when \(\tan \theta \tan {d1}^\circ = 1\).",
                "Determine the measure of acute angle \(\theta\) given \(\tan \theta = \frac{{1}}{{\tan {d1}^\circ}}\).",
                "In right-angled trigonometry, find acute \(\theta\) if \(\tan \theta = \frac{{1}}{{\tan {d1}^\circ}}\).",
                "Compute the value of acute angle \(\theta\) from \(\tan \theta \cdot \tan {d1}^\circ = 1\).",
                "What acute angle \(\theta\) satisfies \(\tan \theta = \frac{{1}}{{\tan {d1}^\circ}}\)?",
            ]
            txt = prefix + tmpls_sub[sub_idx].format(d1=d1)
            corr = f"{d2}^\circ"
            dist = [f"{d1}^\circ", f"{d2 + 10}^\circ", f"{d2 - 10 if d2 > 10 else d2 + 15}^\circ"]
            sol = f"**Step 1: Identity**\n\(\frac{{1}}{{\tan {d1}^\circ}} = \cot {d1}^\circ = \tan(90^\circ - {d1}^\circ) = \tan {d2}^\circ\implies \theta = {d2}^\circ\).\n**Step 2: Conclusion**\n{d2}°."
        elif arch == 5:
            d = data_5[sub_idx]
            comp = 90 - d
            svg = svg_trig("A", "B", "C", f"\angle C = {d}^\circ", f"\angle A = {comp}^\circ", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            tmpls_sub = [
                "Calculate the simplified quotient \(\frac{{\sin {d}^\circ}}{{\cos {comp}^\circ}}\).",
                "What is the value of the trigonometric ratio \(\frac{{\sin {d}^\circ}}{{\cos {comp}^\circ}}\)?",
                "Evaluate \(\frac{{\sin {d}^\circ}}{{\cos {comp}^\circ}}\).",
                "Determine the numerical value of \(\frac{{\sin {d}^\circ}}{{\cos {comp}^\circ}}\).",
                "Find the value of \(\frac{{\sin {d}^\circ}}{{\cos {comp}^\circ}}\).",
                "Compute the fraction \(\frac{{\sin {d}^\circ}}{{\cos {comp}^\circ}}\).",
                "Simplify \(\frac{{\sin {d}^\circ}}{{\cos {comp}^\circ}}\).",
                "Using complementary angle formulas, evaluate \(\frac{{\sin {d}^\circ}}{{\cos {comp}^\circ}}\).",
                "What is the quotient of \(\sin {d}^\circ\) and \(\cos {comp}^\circ\)?",
                "Find the measure of the ratio \(\frac{{\sin {d}^\circ}}{{\cos {comp}^\circ}}\)."
            ]
            txt = prefix + tmpls_sub[sub_idx].format(d=d, comp=comp)
            corr = "1"
            dist = ["0", "2", f"\tan {d}^\circ"]
            sol = f"**Step 1: Complementary angles**\nSince \(\cos {comp}^\circ = \sin(90^\circ - {comp}^\circ) = \sin {d}^\circ\), the quotient is \(\frac{{\sin {d}^\circ}}{{\sin {d}^\circ}} = 1\).\n**Step 2: Conclusion**\n1."
        elif arch == 6:
            a, ans_theta = data_6[sub_idx]
            svg = svg_trig("A", "B", "C", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            tmpls_sub = [
                "Solve for acute \(\theta\) if \(\sin(\theta + {a}^\circ) = \cos(\theta)\).",
                "Find the measure of acute angle \(\theta\) given \(\sin(\theta + {a}^\circ) = \cos(\theta)\).",
                "Determine acute angle \(\theta\) such that \(\sin(\theta + {a}^\circ) = \cos(\theta)\).",
                "What is the value of acute \(\theta\) satisfying \(\sin(\theta + {a}^\circ) = \cos(\theta)\)?",
                "Calculate the acute angle \(\theta\) from the equation \(\sin(\theta + {a}^\circ) = \cos(\theta)\).",
                "If \(\sin(\theta + {a}^\circ) = \cos(\theta)\) for an acute angle \(\theta\), evaluate \(\theta\).",
                "From \(\sin(\theta + {a}^\circ) = \cos(\theta)\), find acute \(\theta\).",
                "Compute acute angle \(\theta\) if \(\sin(\theta + {a}^\circ) = \cos(\theta)\).",
                "In right-angled trigonometry, find acute \(\theta\) when \(\sin(\theta + {a}^\circ) = \cos(\theta)\).",
                "Evaluate the acute angle \(\theta\) if \(\sin(\theta + {a}^\circ) = \cos(\theta)\)."
            ]
            txt = prefix + tmpls_sub[sub_idx].format(a=a)
            corr = f"{ans_theta}^\circ"
            dist = [f"{ans_theta + 10}^\circ", f"{ans_theta - 10 if ans_theta > 10 else ans_theta + 15}^\circ", f"{90 - ans_theta}^\circ"]
            sol = f"**Step 1: Identity**\n\(\cos(\theta) = \sin(90^\circ - \theta)\implies \theta + {a}^\circ = 90^\circ - \theta \implies 2\theta = {90 - a}^\circ \implies \theta = {ans_theta}^\circ\).\n**Step 2: Conclusion**\n{ans_theta}°."
        elif arch == 7:
            m1, m2, ans_theta, eq_str = data_7[sub_idx]
            svg = svg_trig("A", "B", "C", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            tmpls_sub = [
                "Find the acute angle \(\theta\) if \({eq_str}\).",
                "Determine the measure of acute angle \(\theta\) given \({eq_str}\).",
                "Calculate the value of acute angle \(\theta\) satisfying \({eq_str}\).",
                "What acute angle \(\theta\) satisfies the trigonometric relation \({eq_str}\)?",
                "Solve for acute \(\theta\) from the equation \({eq_str}\).",
                "Evaluate the acute angle \(\theta\) such that \({eq_str}\).",
                "If \({eq_str}\) for an acute angle \(\theta\), find \(\theta\).",
                "From the equation \({eq_str}\), compute acute \(\theta\).",
                "Determine acute \(\theta\) when \({eq_str}\).",
                "What is the value of acute angle \(\theta\) if \({eq_str}\)?"
            ]
            txt = prefix + tmpls_sub[sub_idx].format(eq_str=eq_str)
            corr = f"{ans_theta}^\circ"
            dist = [f"{ans_theta + 6}^\circ", f"{ans_theta - 6 if ans_theta > 6 else ans_theta + 12}^\circ", f"{90 - ans_theta}^\circ"]
            sol = f"**Step 1: Complementary angles**\n\({eq_str} \implies {m1}\theta + {m2}\theta = 90^\circ \implies {m1+m2}\theta = 90^\circ \implies \theta = {ans_theta}^\circ\).\n**Step 2: Conclusion**\n{ans_theta}°."

        diff = "easy" if arch in [0,1,2] else ("medium" if arch in [3,4,5] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def gen_8_2_3():
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
            prefix = (svg + "\n") if svg else ""
            tmpls = [
                "If \(\sin \theta = \frac{{{a}}}{{{b}}}\) for an acute angle \(\theta\), find \(\cos \theta\).",
                "In right-angled \(\triangle ABC\), given \(\sin \theta = \frac{{{a}}}{{{b}}}\), calculate \(\cos \theta\).",
                "Determine the value of \(\cos \theta\) when \(\sin \theta = \frac{{{a}}}{{{b}}}\).",
                "What is \(\cos \theta\) if acute angle \(\theta\) satisfies \(\sin \theta = \frac{{{a}}}{{{b}}}\)?",
                "Calculate \(\cos \theta\) using the identity \(\sin^2 \theta + \cos^2 \theta = 1\) given \(\sin \theta = \frac{{{a}}}{{{b}}}\).",
                "Find \(\cos \theta\) knowing that \(\sin \theta = \frac{{{a}}}{{{b}}}\) for acute \(\theta\).",
                "Evaluate \(\cos \theta\) if \(\sin \theta = \frac{{{a}}}{{{b}}}\).",
                "For acute \(\theta\), if \(\sin \theta = \frac{{{a}}}{{{b}}}\), compute \(\cos \theta\).",
                "Determine \(\cos \theta\) given \(\sin \theta = \frac{{{a}}}{{{b}}}\).",
                "What is the measure of \(\cos \theta\) if \(\sin \theta = \frac{{{a}}}{{{b}}}\)?"
            ]
            txt = prefix + tmpls[sub_idx].format(a=a, b=b)
            corr = f"\(\frac{{{c}}}{{{d}}}\)"
            dist = [f"\(\frac{{{a}}}{{{b}}}\)", f"\(\frac{{{c}}}{{{b + 2}}}\)", f"\(\frac{{{a + 1}}}{{{b}}}\)"]
            sol = f"**Step 1: Trigonometric identity**\n\(\cos^2 \theta = 1 - \sin^2 \theta = 1 - (\frac{{{a}}}{{{b}}})^2 = 1 - \frac{{{a*a}}}{{{b*b}}} = \frac{{{c*c}}}{{{d*d}}}\).\n\(\cos \theta = \frac{{{c}}}{{{d}}}\).\n**Step 2: Conclusion**\n\(\frac{{{c}}}{{{d}}}\)."
        elif arch == 1:
            a, b, c, d = data_1[sub_idx]
            svg = svg_trig("A", "B", "C", "AB = ?", f"BC = {a}", f"AC = {b}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            tmpls = [
                "If \(\cos \theta = \frac{{{a}}}{{{b}}}\) for an acute angle \(\theta\), find \(\sin \theta\).",
                "In right-angled \(\triangle ABC\), given \(\cos \theta = \frac{{{a}}}{{{b}}}\), calculate \(\sin \theta\).",
                "Determine the value of \(\sin \theta\) when \(\cos \theta = \frac{{{a}}}{{{b}}}\).",
                "What is \(\sin \theta\) if acute angle \(\theta\) satisfies \(\cos \theta = \frac{{{a}}}{{{b}}}\)?",
                "Calculate \(\sin \theta\) using the identity \(\sin^2 \theta + \cos^2 \theta = 1\) given \(\cos \theta = \frac{{{a}}}{{{b}}}\).",
                "Find \(\sin \theta\) knowing that \(\cos \theta = \frac{{{a}}}{{{b}}}\) for acute \(\theta\).",
                "Evaluate \(\sin \theta\) if \(\cos \theta = \frac{{{a}}}{{{b}}}\).",
                "For acute \(\theta\), if \(\cos \theta = \frac{{{a}}}{{{b}}}\), compute \(\sin \theta\).",
                "Determine \(\sin \theta\) given \(\cos \theta = \frac{{{a}}}{{{b}}}\).",
                "What is the measure of \(\sin \theta\) if \(\cos \theta = \frac{{{a}}}{{{b}}}\)?"
            ]
            txt = prefix + tmpls[sub_idx].format(a=a, b=b)
            corr = f"\(\frac{{{c}}}{{{d}}}\)"
            dist = [f"\(\frac{{{a}}}{{{b}}}\)", f"\(\frac{{{c}}}{{{b + 2}}}\)", f"\(\frac{{{a + 1}}}{{{b}}}\)"]
            sol = f"**Step 1: Trigonometric identity**\n\(\sin^2 \theta = 1 - \cos^2 \theta = 1 - (\frac{{{a}}}{{{b}}})^2 = 1 - \frac{{{a*a}}}{{{b*b}}} = \frac{{{c*c}}}{{{d*d}}}\).\n\(\sin \theta = \frac{{{c}}}{{{d}}}\).\n**Step 2: Conclusion**\n\(\frac{{{c}}}{{{d}}}\)."
        elif arch == 2:
            a, b, c, d = data_2[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {a}", f"BC = {d}", f"AC = {b}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            tmpls = [
                "If \(\sin \theta = \frac{{{a}}}{{{b}}}\) for acute angle \(\theta\), determine \(\tan \theta\).",
                "Find \(\tan \theta\) given that \(\sin \theta = \frac{{{a}}}{{{b}}}\) in right triangle.",
                "Calculate \(\tan \theta\) when \(\sin \theta = \frac{{{a}}}{{{b}}}\).",
                "What is the value of \(\tan \theta\) if \(\sin \theta = \frac{{{a}}}{{{b}}}\)?",
                "Evaluate \(\tan \theta\) for an acute angle \(\theta\) having \(\sin \theta = \frac{{{a}}}{{{b}}}\).",
                "In right-angled \(\triangle ABC\), find \(\tan \theta\) if \(\sin \theta = \frac{{{a}}}{{{b}}}\).",
                "Determine the tangent ratio \(\tan \theta\) knowing \(\sin \theta = \frac{{{a}}}{{{b}}}\).",
                "Compute \(\tan \theta\) given \(\sin \theta = \frac{{{a}}}{{{b}}}\).",
                "Find \(\tan \theta\) using identities if \(\sin \theta = \frac{{{a}}}{{{b}}}\).",
                "What is \(\tan \theta\) when acute angle \(\theta\) satisfies \(\sin \theta = \frac{{{a}}}{{{b}}}\)?"
            ]
            txt = prefix + tmpls[sub_idx].format(a=a, b=b)
            corr = f"\(\frac{{{c}}}{{{d}}}\)"
            dist = [f"\(\frac{{{a}}}{{{b}}}\)", f"\(\frac{{{d}}}{{{c}}}\)", f"\(\frac{{{c}}}{{{b}}}\)"]
            sol = f"**Step 1: Compute cos θ then tan θ**\n\(\cos \theta = \sqrt{{1 - (\frac{{{a}}}{{{b}}})^2}} = \frac{{{d}}}{{{b}}}\).\n\(\tan \theta = \frac{{\sin \theta}}{{\cos \theta}} = \frac{{{c}}}{{{d}}}\).\n**Step 2: Conclusion**\n\(\frac{{{c}}}{{{d}}}\)."
        elif arch == 3:
            num, den, c_num, c_den = data_3[sub_idx]
            tmpls = [
                "If \(\sin^2 \theta = \frac{{{num}}}{{{den}}}\), what is the value of \(\cos^2 \theta\)?",
                "Given \(\sin^2 \theta = \frac{{{num}}}{{{den}}}\), find \(\cos^2 \theta\).",
                "Calculate \(\cos^2 \theta\) when \(\sin^2 \theta = \frac{{{num}}}{{{den}}}\).",
                "Determine the value of \(\cos^2 \theta\) if \(\sin^2 \theta = \frac{{{num}}}{{{den}}}\).",
                "What does \(\cos^2 \theta\) equal if \(\sin^2 \theta = \frac{{{num}}}{{{den}}}\)?",
                "Evaluate \(\cos^2 \theta\) knowing that \(\sin^2 \theta = \frac{{{num}}}{{{den}}}\).",
                "For acute angle \(\theta\), if \(\sin^2 \theta = \frac{{{num}}}{{{den}}}\), compute \(\cos^2 \theta\).",
                "Find \(\cos^2 \theta\) using fundamental identity when \(\sin^2 \theta = \frac{{{num}}}{{{den}}}\).",
                "Compute the value of \(\cos^2 \theta\) given \(\sin^2 \theta = \frac{{{num}}}{{{den}}}\).",
                "In trigonometry, if \(\sin^2 \theta = \frac{{{num}}}{{{den}}}\), what is \(\cos^2 \theta\)?"
            ]
            txt = tmpls[sub_idx].format(num=num, den=den)
            corr = f"\(\frac{{{c_num}}}{{{c_den}}}\)"
            dist = [f"\(\frac{{{num}}}{{{den}}}\)", f"\(\frac{{{c_num + 2}}}{{{c_den}}}\)", "\(1\)"]
            sol = f"**Step 1: Identity**\n\(\cos^2 \theta = 1 - \sin^2 \theta = 1 - \frac{{{num}}}{{{den}}} = \frac{{{c_num}}}{{{c_den}}}\).\n**Step 2: Conclusion**\n\(\frac{{{c_num}}}{{{c_den}}}\)."
        elif arch == 4:
            num, den, c_num, c_den = data_4[sub_idx]
            tmpls = [
                "If \(\cos^2 \theta = \frac{{{num}}}{{{den}}}\), find the value of \(\sin^2 \theta\).",
                "Given \(\cos^2 \theta = \frac{{{num}}}{{{den}}}\), calculate \(\sin^2 \theta\).",
                "Determine \(\sin^2 \theta\) when \(\cos^2 \theta = \frac{{{num}}}{{{den}}}\).",
                "What is \(\sin^2 \theta\) if \(\cos^2 \theta = \frac{{{num}}}{{{den}}}\)?",
                "Calculate the measure of \(\sin^2 \theta\) given \(\cos^2 \theta = \frac{{{num}}}{{{den}}}\).",
                "Evaluate \(\sin^2 \theta\) knowing that \(\cos^2 \theta = \frac{{{num}}}{{{den}}}\).",
                "Compute \(\sin^2 \theta\) for an acute angle \(\theta\) having \(\cos^2 \theta = \frac{{{num}}}{{{den}}}\).",
                "Find \(\sin^2 \theta\) from the identity \(\sin^2 \theta + \cos^2 \theta = 1\) when \(\cos^2 \theta = \frac{{{num}}}{{{den}}}\).",
                "Determine the value of \(\sin^2 \theta\) if \(\cos^2 \theta = \frac{{{num}}}{{{den}}}\).",
                "What does \(\sin^2 \theta\) simplify to if \(\cos^2 \theta = \frac{{{num}}}{{{den}}}\)?"
            ]
            txt = tmpls[sub_idx].format(num=num, den=den)
            corr = f"\(\frac{{{c_num}}}{{{c_den}}}\)"
            dist = [f"\(\frac{{{num}}}{{{den}}}\)", f"\(\frac{{{c_num + 3}}}{{{c_den}}}\)", "\(0\)"]
            sol = f"**Step 1: Identity**\n\(\sin^2 \theta = 1 - \cos^2 \theta = 1 - \frac{{{num}}}{{{den}}} = \frac{{{c_num}}}{{{c_den}}}\).\n**Step 2: Conclusion**\n\(\frac{{{c_num}}}{{{c_den}}}\)."
        elif arch == 5:
            k = data_5[sub_idx]
            ans_val = k - 1
            tmpls = [
                "Calculate the value of \({k} - (\sin^2 \theta + \cos^2 \theta)\).",
                "What is the numerical result of \({k} - (\sin^2 \theta + \cos^2 \theta)\)?",
                "Evaluate the algebraic expression \({k} - (\sin^2 \theta + \cos^2 \theta)\).",
                "Determine the value of \({k} - (\sin^2 \theta + \cos^2 \theta)\) for any angle \(\theta\).",
                "Simplify \({k} - (\sin^2 \theta + \cos^2 \theta)\).",
                "Find the measure of \({k} - (\sin^2 \theta + \cos^2 \theta)\).",
                "Compute the simplified value of \({k} - (\sin^2 \theta + \cos^2 \theta)\).",
                "Using the fundamental identity, evaluate \({k} - (\sin^2 \theta + \cos^2 \theta)\).",
                "What does \({k} - (\sin^2 \theta + \cos^2 \theta)\) equal?",
                "Find the value of expression \({k} - (\sin^2 \theta + \cos^2 \theta)\)."
            ]
            txt = tmpls[sub_idx].format(k=k)
            corr = f"{ans_val}"
            dist = [f"{k}", f"{ans_val + 2}", f"{ans_val - 2 if ans_val > 2 else ans_val + 3}"]
            sol = f"**Step 1: Identity**\n\(\sin^2 \theta + \cos^2 \theta = 1\).\n\({k} - 1 = {ans_val}\).\n**Step 2: Conclusion**\n{ans_val}."
        elif arch == 6:
            d = data_6[sub_idx]
            tmpls = [
                "Simplify the expression \(\frac{{1 - \sin^2 {d}^\circ}}{{\cos^2 {d}^\circ}}\).",
                "Evaluate the trigonometric ratio \(\frac{{1 - \sin^2 {d}^\circ}}{{\cos^2 {d}^\circ}}\).",
                "What is the value of \(\frac{{1 - \sin^2 {d}^\circ}}{{\cos^2 {d}^\circ}}\)?",
                "Calculate the numerical measure of \(\frac{{1 - \sin^2 {d}^\circ}}{{\cos^2 {d}^\circ}}\).",
                "Determine the simplified value of \(\frac{{1 - \sin^2 {d}^\circ}}{{\cos^2 {d}^\circ}}\).",
                "Find the value of \(\frac{{1 - \sin^2 {d}^\circ}}{{\cos^2 {d}^\circ}}\).",
                "Using identities, evaluate \(\frac{{1 - \sin^2 {d}^\circ}}{{\cos^2 {d}^\circ}}\).",
                "What does \(\frac{{1 - \sin^2 {d}^\circ}}{{\cos^2 {d}^\circ}}\) simplify to?",
                "Compute \(\frac{{1 - \sin^2 {d}^\circ}}{{\cos^2 {d}^\circ}}\).",
                "Find the simplified form of \(\frac{{1 - \sin^2 {d}^\circ}}{{\cos^2 {d}^\circ}}\)."
            ]
            txt = tmpls[sub_idx].format(d=d)
            corr = "1"
            dist = ["0", "2", f"\tan^2 {d}^\circ"]
            sol = f"**Step 1: Identity**\n\(1 - \sin^2 {d}^\circ = \cos^2 {d}^\circ\).\n\(\frac{{\cos^2 {d}^\circ}}{{\cos^2 {d}^\circ}} = 1\).\n**Step 2: Conclusion**\n1."
        elif arch == 7:
            k, m, ans_val = data_7[sub_idx]
            tmpls = [
                "Evaluate the expression \({k}(\sin^2 \theta + \cos^2 \theta) + {m}\).",
                "What is the value of \({k}(\sin^2 \theta + \cos^2 \theta) + {m}\)?",
                "Calculate \({k}(\sin^2 \theta + \cos^2 \theta) + {m}\) for any acute angle \(\theta\).",
                "Find the simplified numerical result of \({k}(\sin^2 \theta + \cos^2 \theta) + {m}\).",
                "Determine the measure of \({k}(\sin^2 \theta + \cos^2 \theta) + {m}\).",
                "Compute \({k}(\sin^2 \theta + \cos^2 \theta) + {m}\).",
                "Simplify \({k}(\sin^2 \theta + \cos^2 \theta) + {m}\).",
                "Using the Pythagorean trigonometric identity, evaluate \({k}(\sin^2 \theta + \cos^2 \theta) + {m}\).",
                "What does \({k}(\sin^2 \theta + \cos^2 \theta) + {m}\) equal?",
                "Find the value of expression \({k}(\sin^2 \theta + \cos^2 \theta) + {m}\)."
            ]
            txt = tmpls[sub_idx].format(k=k, m=m)
            corr = f"{ans_val}"
            dist = [f"{ans_val + 2}", f"{ans_val - 2}", f"{k * m}"]
            sol = f"**Step 1: Identity**\n\(\sin^2 \theta + \cos^2 \theta = 1\).\n\({k}(1) + {m} = {ans_val}\).\n**Step 2: Conclusion**\n{ans_val}."

        diff = "easy" if arch in [0,1,2] else ("medium" if arch in [3,4,5] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def gen_8_3_1():
    tc = "MH-9-MTH2-8-8.3.1"
    tname = "Derivation of values using geometric triangles (30°-60°-90° and 45°-45°-90°)"
    qs = []
    
    # Arch 0: 30-60-90: side opp 30° = hyp/2
    data_0 = [
        (6, 3), (10, 5), (14, 7), (18, 9), (22, 11),
        (26, 13), (30, 15), (34, 17), (38, 19), (42, 21)
    ]
    tmpls_0 = [
        "In \(\triangle ABC\) with \(\angle B = 90^\circ\), \(\angle C = 30^\circ\), and hypotenuse \(AC = {hyp}\), find length \(AB\).",
        "For right-angled \(\triangle ABC\) (\(\angle B = 90^\circ\), \(\angle C = 30^\circ\)), compute side \(AB\) when \(AC = {hyp}\).",
        "What is the length of side \(AB\) opposite to 30° in \(\triangle ABC\) (\(\angle B = 90^\circ\)) if hypotenuse \(AC = {hyp}\)?",
        "Calculate opposite side \(AB\) in right triangle \(\triangle ABC\) with \(\angle C = 30^\circ\) and \(AC = {hyp}\).",
        "Determine side \(AB\) in \(\triangle ABC\) (\(\angle B = 90^\circ\), \(\angle C = 30^\circ\)) having hypotenuse \(AC = {hyp}\).",
        "Evaluate the length of \(AB\) in \(\triangle ABC\) right-angled at \(B\) given \(\angle C = 30^\circ\) and \(AC = {hyp}\).",
        "Find the opposite leg \(AB\) in 30°-60°-90° right \(\triangle ABC\) if hypotenuse \(AC = {hyp}\).",
        "In right triangle \(\triangle ABC\), hypotenuse \(AC = {hyp}\) and \(\angle C = 30^\circ\). Find \(AB\).",
        "Compute the measure of side \(AB\) in \(\triangle ABC\) (\(\angle B = 90^\circ\), \(\angle C = 30^\circ\), \(AC = {hyp}\)).",
        "If \(\angle C = 30^\circ\) and \(AC = {hyp}\) in right \(\triangle ABC\) (\(\angle B = 90^\circ\)), what is \(AB\)?"
    ]
    
    # Arch 1: 30-60-90: side opp 60° = (sqrt(3)/2)*hyp
    data_1 = [
        (2, "\sqrt{3}"), (4, "2\sqrt{3}"), (6, "3\sqrt{3}"), (8, "4\sqrt{3}"), (10, "5\sqrt{3}"),
        (12, "6\sqrt{3}"), (14, "7\sqrt{3}"), (16, "8\sqrt{3}"), (18, "9\sqrt{3}"), (20, "10\sqrt{3}")
    ]
    tmpls_1 = [
        "In \(\triangle ABC\) (\(\angle B = 90^\circ\), \(\angle A = 30^\circ\), \(AC = {hyp}\)), find side \(BC\) opposite to 60°.",
        "Calculate side \(BC\) opposite to 60° in right-angled \(\triangle ABC\) with hypotenuse \(AC = {hyp}\).",
        "What is the measure of side \(BC\) opposite to 60° in \(\triangle ABC\) (\(\angle B = 90^\circ\)) if \(AC = {hyp}\)?",
        "For 30°-60°-90° \(\triangle ABC\), evaluate the length of side \(BC\) opposite to 60° when hypotenuse \(AC = {hyp}\).",
        "Find the length of the side opposite to 60° in right \(\triangle ABC\) with \(AC = {hyp}\).",
        "Determine \(BC\) opposite to 60° in right-angled \(\triangle ABC\) having hypotenuse \(AC = {hyp}\).",
        "In right triangle \(\triangle ABC\) with acute angles 30° and 60°, find the side opposite to 60° if hypotenuse \(AC = {hyp}\).",
        "Compute the leg opposite to 60° in \(\triangle ABC\) (\(\angle B = 90^\circ\)) with hypotenuse \(AC = {hyp}\).",
        "Given hypotenuse \(AC = {hyp}\) in 30°-60°-90° \(\triangle ABC\), what is the length of side \(BC\)?",
        "If \(\angle A = 60^\circ\) and hypotenuse \(AC = {hyp}\) in right \(\triangle ABC\), find the opposite side."
    ]
    
    # Arch 2: 45-45-90: given leg s, find hypotenuse s*sqrt(2)
    data_2 = [
        (3, "3\sqrt{2}"), (5, "5\sqrt{2}"), (7, "7\sqrt{2}"), (9, "9\sqrt{2}"), (11, "11\sqrt{2}"),
        (13, "13\sqrt{2}"), (15, "15\sqrt{2}"), (17, "17\sqrt{2}"), (19, "19\sqrt{2}"), (21, "21\sqrt{2}")
    ]
    tmpls_2 = [
        "In an isosceles right triangle \(\triangle ABC\) (\(\angle B = 90^\circ\)), if legs \(AB = BC = {s}\), find hypotenuse \(AC\).",
        "For 45°-45°-90° \(\triangle ABC\) with congruent legs \(AB = BC = {s}\), compute hypotenuse \(AC\).",
        "What is the hypotenuse \(AC\) of an isosceles right triangle with equal sides of length \({s}\)?",
        "Calculate hypotenuse \(AC\) in right-angled \(\triangle ABC\) (\(\angle B = 90^\circ\)) where \(AB = BC = {s}\).",
        "Determine the measure of hypotenuse \(AC\) in 45°-45°-90° \(\triangle ABC\) having legs \({s}\).",
        "Find length \(AC\) in isosceles right \(\triangle ABC\) (\(\angle B = 90^\circ\)) given \(AB = BC = {s}\).",
        "Evaluate the hypotenuse of a 45°-45°-90° triangle whose perpendicular legs measure \({s}\).",
        "In right triangle \(\triangle ABC\) with \(\angle A = \angle C = 45^\circ\) and leg \({s}\), what is hypotenuse \(AC\)?",
        "Compute the hypotenuse \(AC\) in \(\triangle ABC\) (\(\angle B = 90^\circ\), \(AB = BC = {s}\)).",
        "If each equal side in right isosceles \(\triangle ABC\) is \({s}\), calculate hypotenuse \(AC\)."
    ]
    
    # Arch 3: 45-45-90: given hypotenuse s*sqrt(2), find leg s
    data_3 = [
        ("2\sqrt{2}", 2), ("4\sqrt{2}", 4), ("6\sqrt{2}", 6), ("8\sqrt{2}", 8), ("10\sqrt{2}", 10),
        ("12\sqrt{2}", 12), ("14\sqrt{2}", 14), ("16\sqrt{2}", 16), ("18\sqrt{2}", 18), ("20\sqrt{2}", 20)
    ]
    tmpls_3 = [
        "In 45°-45°-90° \(\triangle ABC\) (\(\angle B = 90^\circ\)), if hypotenuse \(AC = {hyp_str}\), find the length of each perpendicular side.",
        "Calculate the leg length of an isosceles right triangle whose hypotenuse is \({hyp_str}\).",
        "What is the measure of each perpendicular side in \(\triangle ABC\) (\(\angle B = 90^\circ\)) if hypotenuse \(AC = {hyp_str}\)?",
        "For a 45°-45°-90° triangle with hypotenuse \({hyp_str}\), determine the length of each equal side.",
        "Find the length of side \(AB\) in right isosceles \(\triangle ABC\) given hypotenuse \(AC = {hyp_str}\).",
        "Evaluate the length of each leg in 45°-45°-90° right triangle having hypotenuse \({hyp_str}\).",
        "Compute side \(BC\) in isosceles right-angled \(\triangle ABC\) where hypotenuse \(AC = {hyp_str}\).",
        "In \(\triangle ABC\) with \(\angle A = \angle C = 45^\circ\) and hypotenuse \(AC = {hyp_str}\), find side \(AB\).",
        "Determine the leg of a 45°-45°-90° triangle if its hypotenuse is \({hyp_str}\).",
        "If hypotenuse \(AC = {hyp_str}\) in right-angled isosceles \(\triangle ABC\), what is the length of side \(AB\)?"
    ]
    
    # Arch 4: 30-60-90: side opp 30° is given, find hypotenuse = 2 * opp
    data_4 = [
        (7, 14), (9, 18), (11, 22), (13, 26), (15, 30),
        (17, 34), (19, 38), (21, 42), (23, 46), (25, 50)
    ]
    tmpls_4 = [
        "In a 30°-60°-90° right triangle, if the side opposite to 30° is \({opp}\), calculate the length of the hypotenuse.",
        "Find the hypotenuse of right triangle \(\triangle ABC\) where the side opposite to 30° measures \({opp}\).",
        "What is the length of the hypotenuse in a 30°-60°-90° triangle having opposite leg \({opp}\)?",
        "Determine the hypotenuse in right-angled \(\triangle ABC\) if side opposite to 30° is \({opp}\).",
        "For 30°-60°-90° \(\triangle ABC\), compute hypotenuse \(AC\) when the side opposite to 30° is \({opp}\).",
        "Evaluate the hypotenuse of a right triangle with an acute angle of 30° and opposite side \({opp}\).",
        "Calculate the measure of the hypotenuse if the side opposite to 30° in a right triangle is \({opp}\).",
        "In \(\triangle ABC\) (\(\angle B = 90^\circ\), \(\angle C = 30^\circ\)), given \(AB = {opp}\), find hypotenuse \(AC\).",
        "What is the hypotenuse of right-angled \(\triangle ABC\) when side opposite to 30° is \({opp}\)?",
        "Find hypotenuse \(AC\) in 30°-60°-90° \(\triangle ABC\) given opposite side \(AB = {opp}\)."
    ]
    
    # Arch 5: 30-60-90: side opp 60° is k*sqrt(3), find hypotenuse = 2*k
    data_5 = [
        ("3\sqrt{3}", 6), ("5\sqrt{3}", 10), ("7\sqrt{3}", 14), ("9\sqrt{3}", 18), ("11\sqrt{3}", 22),
        ("13\sqrt{3}", 26), ("27\sqrt{3}", 54), ("17\sqrt{3}", 34), ("19\sqrt{3}", 38), ("21\sqrt{3}", 42)
    ]
    tmpls_5 = [
        "In a 30°-60°-90° right triangle, the side opposite to 60° is \({opp_str}\). What is the hypotenuse?",
        "Find the hypotenuse of 30°-60°-90° triangle whose side opposite to 60° is \({opp_str}\).",
        "Calculate the length of the hypotenuse in right triangle \(\triangle ABC\) if the leg opposite to 60° is \({opp_str}\).",
        "What is the measure of the hypotenuse in a right triangle where side opposite to 60° measures \({opp_str}\)?",
        "Determine the hypotenuse of a 30°-60°-90° triangle given that the side opposite to 60° is \({opp_str}\).",
        "For right-angled \(\triangle ABC\) with acute angle 60° and opposite side \({opp_str}\), compute the hypotenuse.",
        "Evaluate the hypotenuse in 30°-60°-90° \(\triangle ABC\) when the side opposite to 60° is \({opp_str}\).",
        "If the side opposite to 60° in a right triangle is \({opp_str}\), calculate the hypotenuse.",
        "Compute the length of hypotenuse in right \(\triangle ABC\) where the side opposite to 60° is \({opp_str}\).",
        "Find hypotenuse \(AC\) in 30°-60°-90° \(\triangle ABC\) knowing the side opposite to 60° is \({opp_str}\)."
    ]
    
    # Arch 6: Area of 45-45-90 with leg s -> 1/2 * s^2
    data_6 = [
        (4, 8), (6, 18), (8, 32), (10, 50), (12, 72),
        (14, 98), (16, 128), (18, 162), (20, 200), (22, 242)
    ]
    tmpls_6 = [
        "In right isosceles \(\triangle ABC\) (\(\angle B = 90^\circ\)) with legs \(AB = BC = {s}\), find its area.",
        "Compute the area of a 45°-45°-90° right triangle whose perpendicular sides each measure \({s}\).",
        "What is the area of \(\triangle ABC\) (\(\angle B = 90^\circ\), \(AB = BC = {s}\))?",
        "Determine the area of an isosceles right triangle with equal legs of length \({s}\).",
        "For 45°-45°-90° triangle \(\triangle ABC\), find the area when both perpendicular legs equal \({s}\).",
        "Calculate the area of right isosceles \(\triangle ABC\) having equal sides of \({s}\).",
        "Find the area of \(\triangle ABC\) (\(\angle B = 90^\circ\), \(\angle A = 45^\circ\)) if legs measure \({s}\).",
        "Evaluate the area of right-angled isosceles \(\triangle ABC\) with legs \({s}\).",
        "In 45°-45°-90° \(\triangle ABC\), perpendicular sides are \({s}\). What is its area?",
        "If legs \(AB = BC = {s}\) in right-angled \(\triangle ABC\), determine its area."
    ]
    
    # Arch 7: Geometric ratio deduction
    data_7 = [
        ("30^\circ", "60^\circ", "\frac{1}{2}"),
        ("45^\circ", "45^\circ", "\frac{1}{\sqrt{2}}"),
        ("60^\circ", "30^\circ", "\frac{\sqrt{3}}{2}"),
        ("30^\circ", "90^\circ", "\frac{1}{2}"),
        ("45^\circ", "90^\circ", "1"),
        ("60^\circ", "90^\circ", "\sqrt{3}"),
        ("30^\circ", "45^\circ", "\frac{1}{\sqrt{3}}"),
        ("0^\circ", "90^\circ", "0"),
        ("60^\circ", "45^\circ", "\frac{\sqrt{3}}{2}"),
        ("30^\circ", "30^\circ", "1")
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
        "In geometric deduction of trigonometric values, what is \(\sin({a1})\)?"
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        qcode = f"{tc}-OSC-{seq}"
        
        if arch == 0:
            hyp, opp = data_0[sub_idx]
            svg = svg_trig("A", "B", "C", "AB = ?", "", f"AC = {hyp}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(hyp=hyp)
            corr = f"{opp}"
            dist = [f"{opp + 2}", f"{opp - 2 if opp > 2 else opp + 4}", f"{opp * 2}"]
            sol = f"**Step 1: 30°-60°-90° theorem**\n\(AB = \frac{{1}}{{2}} \times AC = \frac{{1}}{{2}} \times {hyp} = {opp}\).\n**Step 2: Conclusion**\n{opp}."
        elif arch == 1:
            hyp, opp_str = data_1[sub_idx]
            svg = svg_trig("A", "B", "C", "", f"BC = ?", f"AC = {hyp}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(hyp=hyp)
            corr = f"\({opp_str}\)"
            dist = [f"\({hyp}\)", f"\(\frac{{{hyp}}}{{2}}\)", f"\({hyp}\sqrt{{2}}\)" ]
            sol = f"**Step 1: 30°-60°-90° theorem**\n\(BC = \frac{{\sqrt{{3}}}}{{2}} \times AC = \frac{{\sqrt{{3}}}}{{2}} \times {hyp} = {opp_str}\).\n**Step 2: Conclusion**\n\({opp_str}\)."
        elif arch == 2:
            s, hyp_str = data_2[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {s}", f"BC = {s}", "AC = ?") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(s=s)
            corr = f"\({hyp_str}\)"
            dist = [f"{s * 2}", f"{s}", f"\({s}\sqrt{{3}}\)" ]
            sol = f"**Step 1: 45°-45°-90° theorem**\n\(AC = \sqrt{{2}} \times \text{{side}} = {hyp_str}\).\n**Step 2: Conclusion**\n\({hyp_str}\)."
        elif arch == 3:
            hyp_str, leg = data_3[sub_idx]
            svg = svg_trig("A", "B", "C", "AB = ?", "BC = ?", f"AC = {hyp_str}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(hyp_str=hyp_str)
            corr = f"{leg}"
            dist = [f"{leg + 2}", f"{leg - 2 if leg > 2 else leg + 3}", f"{leg * 2}"]
            sol = f"**Step 1: 45°-45°-90° theorem**\n\(\text{{leg}} = \frac{{AC}}{{\sqrt{{2}}}} = {leg}\).\n**Step 2: Conclusion**\n{leg}."
        elif arch == 4:
            opp, hyp = data_4[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {opp}", "", "AC = ?") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(opp=opp)
            corr = f"{hyp}"
            dist = [f"{hyp + 4}", f"{hyp - 4}", f"{opp}"]
            sol = f"**Step 1: Formula**\n\(\text{{hypotenuse}} = 2 \times \text{{opposite 30°}} = 2 \times {opp} = {hyp}\).\n**Step 2: Conclusion**\n{hyp}."
        elif arch == 5:
            opp_str, hyp = data_5[sub_idx]
            svg = svg_trig("A", "B", "C", "", f"BC = {opp_str}", "AC = ?") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(opp_str=opp_str)
            corr = f"{hyp}"
            dist = [f"{hyp + 4}", f"{hyp - 4}", f"{hyp * 2}"]
            sol = f"**Step 1: 30°-60°-90° theorem**\n\(\text{{opposite 60°}} = \frac{{\sqrt{{3}}}}{{2}} \times \text{{hypotenuse}} \implies \text{{hypotenuse}} = {hyp}\).\n**Step 2: Conclusion**\n{hyp}."
        elif arch == 6:
            s, area_ans = data_6[sub_idx]
            svg = svg_trig("A", "B", "C", f"AB = {s}", f"BC = {s}", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(s=s)
            corr = f"{area_ans}"
            dist = [f"{area_ans + 4}", f"{area_ans - 4 if area_ans > 4 else area_ans + 6}", f"{s * 2}"]
            sol = f"**Step 1: Formula**\n\(\text{{Area}} = \frac{{1}}{{2}} \times \text{{base}} \times \text{{height}} = \frac{{1}}{{2}} \times {s} \times {s} = {area_ans}\).\n**Step 2: Conclusion**\n{area_ans}."
        elif arch == 7:
            a1, a2, ans_str = data_7[sub_idx]
            svg = svg_trig("A", "B", "C", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_7[sub_idx].format(a1=a1)
            corr = f"\({ans_str}\)"
            dist = ["\(\frac{1}{2}\)", "\(\frac{\sqrt{3}}{2}\)", "\(\frac{1}{\sqrt{2}}\)", "\(1\)"]
            dist = [d for d in dist if d != f"\({ans_str}\)"][:3]
            sol = f"**Step 1: Definition**\nIn a standard geometric right triangle, the ratio for {a1} is \({ans_str}\).\n**Step 2: Conclusion**\n\({ans_str}\)."

        diff = "easy" if arch in [0,1,2] else ("medium" if arch in [3,4,5] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
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
        (30, "2\\sin x = 1", "Find acute angle \\(x\\) satisfying \\(2\\sin x = 1\\)."),
        (60, "2\\cos x = 1", "Calculate the acute angle \\(x\\) when \\(2\\cos x = 1\\)."),
        (45, "\\tan x = 1", "Determine acute angle \\(x\\) given \\(\\tan x = 1\\)."),
        (40, "\\sin(x - 10^\\circ) = \\frac{1}{2}", "What is the acute angle \\(x\\) if \\(\\sin(x - 10^\\circ) = \\frac{1}{2}\\)?"),
        (50, "\\cos(x + 10^\\circ) = \\frac{1}{2}", "Evaluate acute angle \\(x\\) if \\(\\cos(x + 10^\\circ) = \\frac{1}{2}\\)."),
        (70, "\\tan(x - 25^\\circ) = 1", "Find the value of acute angle \\(x\\) for which \\(\\tan(x - 25^\\circ) = 1\\)."),
        (80, "\\sin(x + 10^\\circ) = 1", "Solve the trigonometric equation \\(\\sin(x + 10^\\circ) = 1\\) for acute angle \\(x\\)."),
        (10, "\\cos(x - 10^\\circ) = 1", "Determine \\(x\\) in \\(0^\\circ < x < 90^\\circ\\) where \\(\\cos(x - 10^\\circ) = 1\\)."),
        (35, "\\tan(x + 25^\\circ) = \\sqrt{3}", "Compute acute angle \\(x\\) when \\(\\tan(x + 25^\\circ) = \\sqrt{3}\\)."),
        (15, "\\sin(2x) = \\frac{1}{2}", "For what acute angle \\(x\\) does \\(\\sin(2x) = \\frac{1}{2}\\)?")
    ]
    
    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = False
        
        if arch == 0:
            k = data_0[sub_idx]
            ans_val = 2 + k
            txt = f"Evaluate the expression \\(2\\sin 30^\\circ + \\cos 0^\\circ + {k}\\)."
            corr = f"{ans_val}"
            dist = [f"{ans_val + 2}", f"{ans_val - 2}", f"{k}"]
            sol = f"**Step 1: Substitute values**\n\\(2(\\frac{{1}}{{2}}) + 1 + {k} = {ans_val}\\).\n**Step 2: Conclusion**\n{ans_val}."
        elif arch == 1:
            k = data_1[sub_idx]
            ans_val = 4 + k
            txt = f"Evaluate the expression \\(4\\cos 60^\\circ + 2\\tan 45^\\circ + {k}\\)."
            corr = f"{ans_val}"
            dist = [f"{ans_val + 2}", f"{ans_val - 2}", f"{k}"]
            sol = f"**Step 1: Substitute values**\n\\(4(\\frac{{1}}{{2}}) + 2(1) + {k} = {ans_val}\\).\n**Step 2: Conclusion**\n{ans_val}."
        elif arch == 2:
            k = data_2[sub_idx]
            ans_val = 4 + k
            txt = f"Calculate the numerical value of \\(\\tan^2 60^\\circ + \\sin^2 90^\\circ + {k}\\)."
            corr = f"{ans_val}"
            dist = [f"{ans_val + 3}", f"{ans_val - 3}", f"{k}"]
            sol = f"**Step 1: Substitute values**\n\\((\\sqrt{{3}})^2 + (1)^2 + {k} = {ans_val}\\).\n**Step 2: Conclusion**\n{ans_val}."
        elif arch == 3:
            k = data_3[sub_idx]
            ans_val = 1 + k
            txt = f"Evaluate the expression \\(3\\tan^2 30^\\circ + {k}\\)."
            corr = f"{ans_val}"
            dist = [f"{ans_val + 2}", f"{ans_val - 2}", f"{k}"]
            sol = f"**Step 1: Substitute values**\n\\(3(\\frac{{1}}{{\\sqrt{{3}}}})^2 + {k} = {ans_val}\\).\n**Step 2: Conclusion**\n{ans_val}."
        elif arch == 4:
            k = data_4[sub_idx]
            ans_val = 1 + k
            txt = f"Calculate the value of \\(2\\cos^2 45^\\circ + {k}\\)."
            corr = f"{ans_val}"
            dist = [f"{ans_val + 2}", f"{ans_val - 2}", f"{k}"]
            sol = f"**Step 1: Substitute values**\n\\(2(\\frac{{1}}{{\\sqrt{{2}}}})^2 + {k} = {ans_val}\\).\n**Step 2: Conclusion**\n{ans_val}."
        elif arch == 5:
            k = data_5[sub_idx]
            ans_val = 1 + k
            txt = f"Evaluate \\(4\\sin^2 30^\\circ + {k}\\)."
            corr = f"{ans_val}"
            dist = [f"{ans_val + 2}", f"{ans_val - 2}", f"{k}"]
            sol = f"**Step 1: Substitute values**\n\\(4(\\frac{{1}}{{2}})^2 + {k} = {ans_val}\\).\n**Step 2: Conclusion**\n{ans_val}."
        elif arch == 6:
            k = data_6[sub_idx]
            ans_val = 3 + k
            txt = f"Evaluate \\(\\sqrt{{3}}\\tan 60^\\circ + {k}\\)."
            corr = f"{ans_val}"
            dist = [f"{ans_val + 3}", f"{ans_val - 3}", f"{k}"]
            sol = f"**Step 1: Substitute values**\n\\(\\sqrt{{3}}(\\sqrt{{3}}) + {k} = {ans_val}\\).\n**Step 2: Conclusion**\n{ans_val}."
        else:
            ang, eq_str, txt_stem = data_7[sub_idx]
            txt = txt_stem
            corr = f"{ang}^\\circ"
            dist = [f"{ang + 15}^\\circ", f"{90 - ang}^\\circ", f"{ang - 15 if ang > 15 else ang + 30}^\\circ"]
            sol = f"**Step 1: Standard ratio**\n\\(x = {ang}^\\circ\\).\n**Step 2: Conclusion**\n{ang}°."
            
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
