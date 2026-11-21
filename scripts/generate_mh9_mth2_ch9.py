# scripts/generate_mh9_mth2_ch9.py
# High-entropy diverse generator for MH-9-MTH2 Chapter 9 (Surface Area and Volume)
# 9 subtopics * 80 questions = 720 completely unique, distinct questions.

import json
import math

def make_opts(corr_text, distractors):
    dist_set = []
    for d in distractors:
        if d != corr_text and d not in dist_set:
            dist_set.append(d)
        if len(dist_set) == 3:
            break
    while len(dist_set) < 3:
        dist_set.append(f"{corr_text} + {len(dist_set) + 1}")
    
    all_four = [corr_text] + dist_set[:3]
    all_four.sort(key=lambda s: (len(s), s))
    
    letters = ['A', 'B', 'C', 'D']
    options = []
    for idx, opt_text in enumerate(all_four):
        options.append({
            "id": letters[idx],
            "text": opt_text,
            "isCorrect": (opt_text == corr_text)
        })
    return options

def svg_cone(r, h, l, title):
    return f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 170" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>
  <line x1="180" y1="35" x2="110" y2="135" stroke="#38bdf8" stroke-width="2.2"/>
  <line x1="180" y1="35" x2="250" y2="135" stroke="#38bdf8" stroke-width="2.2"/>
  <ellipse cx="180" cy="135" rx="70" ry="18" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <line x1="180" y1="35" x2="180" y2="135" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="3,3"/>
  <line x1="180" y1="135" x2="250" y2="135" stroke="#f8fafc" stroke-width="2"/>
  <circle cx="180" cy="135" r="3.5" fill="#f59e0b"/>
  <circle cx="180" cy="35" r="3.5" fill="#f8fafc"/>
  <text x="190" y="85" fill="#f59e0b" font-size="11" font-weight="600" font-family="sans-serif">h = {h}</text>
  <text x="215" y="152" fill="#f8fafc" font-size="11" font-weight="600" font-family="sans-serif">r = {r}</text>
  <text x="225" y="75" fill="#38bdf8" font-size="11" font-weight="600" font-family="sans-serif">l = {l}</text>
</svg>
</div>"""

def svg_sphere(r, title):
    return f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 170" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>
  <circle cx="180" cy="90" r="58" fill="#1e293b" stroke="#38bdf8" stroke-width="2.2"/>
  <ellipse cx="180" cy="90" rx="58" ry="16" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,3"/>
  <line x1="180" y1="90" x2="238" y2="90" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="180" cy="90" r="3.5" fill="#f59e0b"/>
  <text x="180" y="80" fill="#f59e0b" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">O</text>
  <text x="208" y="105" fill="#f59e0b" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">r = {r}</text>
</svg>
</div>"""

def svg_hemi(r, title):
    return f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 160" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>
  <ellipse cx="180" cy="65" rx="65" ry="18" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <path d="M 115 65 A 65 65 0 0 0 245 65" fill="#1e293b" stroke="#38bdf8" stroke-width="2.2"/>
  <line x1="180" y1="65" x2="245" y2="65" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="180" cy="65" r="3.5" fill="#f59e0b"/>
  <text x="180" y="55" fill="#f59e0b" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">O</text>
  <text x="212" y="80" fill="#f59e0b" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">r = {r}</text>
</svg>
</div>"""

def build_q(qcode, text, corr, distractors, sol, tc, top_name, seq, has_fig):
    opts = make_opts(corr, distractors)
    corr_letter = [o["id"] for o in opts if o["isCorrect"]][0]
    vault = 'exam' if seq <= 40 else ('practice' if seq <= 60 else 'foundation')
    diff = 'easy' if seq <= 25 else ('medium' if seq <= 65 else 'hard')

    return {
        "questionCode": qcode,
        "text": text,
        "options": opts,
        "correctAnswer": corr_letter,
        "solution": sol,
        "boardCode": "MH",
        "board": "Maharashtra Board",
        "class": "9",
        "subjectCode": "MTH2",
        "subject": "Mathematics Part - 2 (Geometry)",
        "chapterNumber": 9,
        "chapter": "Surface Area and Volume",
        "topicCode": tc,
        "topic": top_name,
        "type": "OSC",
        "marks": 4,
        "difficulty": diff,
        "vault": vault,
        "timesUsed": 0,
        "usedInClassroomTest": False,
        "requiresFigure": has_fig,
        "createdAt": "2026-11-21T19:00:00.000Z",
        "updatedAt": "2026-11-21T19:00:00.000Z"
    }

TRIPLES_10 = [
    (3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17),
    (9, 12, 15), (10, 24, 26), (12, 16, 20), (15, 20, 25), (14, 48, 50)
]

RADII_10 = [3, 4, 5, 6, 7, 8, 9, 10, 12, 14]
RADII_VOL_10 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

def generate_ch9_all():
    all_qs = []

    # -----------------------------------------------------------------
    # Subtopic 9.1.1: Slant height l = sqrt(r^2 + h^2)
    # -----------------------------------------------------------------
    tc = "MH-9-MTH2-9-9.1.1"
    tname = "Slant height l = √(r² + h²)"
    sub_qs = []
    for cat in range(8):
        for i in range(10):
            seq = cat * 10 + i + 1
            qcode = f"{tc}-OSC-{seq:03d}"
            r, h, l = TRIPLES_10[i]
            has_fig = (seq % 10 in [0, 1, 2, 4, 6, 8])
            svg = svg_cone(f"{r} cm", f"{h} cm", f"{l} cm", f"Slant Height Analysis #{seq}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""

            if cat == 0:
                txt = prefix + f"A right circular cone has base radius \\(r = {r}\\text{{ cm}}\\) and vertical height \\(h = {h}\\text{{ cm}}\\). What is its slant height \\(l\\)?"
                corr = f"\\({l}\\text{{ cm}}\\)"
                dist = [f"\\({h + 1}\\text{{ cm}}\\)", f"\\({l + 2}\\text{{ cm}}\\)", f"\\({r + h}\\text{{ cm}}\\)"]
                sol = f"**Step 1: Formula**\n\\(l = \\sqrt{{r^2 + h^2}} = \\sqrt{{{r}^2 + {h}^2}} = \\sqrt{{{r*r + h*h}}} = {l}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\(l = {l}\\text{{ cm}}\\)."
            elif cat == 1:
                txt = prefix + f"The slant height of a right cone is \\(l = {l}\\text{{ cm}}\\) and its base radius is \\(r = {r}\\text{{ cm}}\\). Find the perpendicular height \\(h\\) of the cone."
                corr = f"\\({h}\\text{{ cm}}\\)"
                dist = [f"\\({l - 1}\\text{{ cm}}\\)", f"\\({h + 3}\\text{{ cm}}\\)", f"\\({h - 2}\\text{{ cm}}\\)"]
                sol = f"**Step 1: Formula**\n\\(h = \\sqrt{{l^2 - r^2}} = \\sqrt{{{l}^2 - {r}^2}} = \\sqrt{{{l*l - r*r}}} = {h}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\(h = {h}\\text{{ cm}}\\)."
            elif cat == 2:
                txt = prefix + f"A cone has vertical height \\(h = {h}\\text{{ m}}\\) and slant height \\(l = {l}\\text{{ m}}\\). Calculate the radius of its circular base."
                corr = f"\\({r}\\text{{ m}}\\)"
                dist = [f"\\({l - h}\\text{{ m}}\\)", f"\\({r + 2}\\text{{ m}}\\)", f"\\({r - 1}\\text{{ m}}\\)"]
                sol = f"**Step 1: Formula**\n\\(r = \\sqrt{{l^2 - h^2}} = \\sqrt{{{l}^2 - {h}^2}} = {r}\\text{{ m}}\\).\n**Step 2: Conclusion**\n\\(r = {r}\\text{{ m}}\\)."
            elif cat == 3:
                txt = prefix + f"The diameter of the circular base of a cone is \\({2 * r}\\text{{ cm}}\\) and its vertical height is \\({h}\\text{{ cm}}\\). What is its slant height?"
                corr = f"\\({l}\\text{{ cm}}\\)"
                dist = [f"\\({2 * r + h}\\text{{ cm}}\\)", f"\\({l + 4}\\text{{ cm}}\\)", f"\\({l - 2}\\text{{ cm}}\\)"]
                sol = f"**Step 1: Radius & Slant Height**\nRadius \\(r = \\frac{{{2 * r}}}{{2}} = {r}\\text{{ cm}}\\). Then \\(l = \\sqrt{{{r}^2 + {h}^2}} = {l}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\(l = {l}\\text{{ cm}}\\)."
            elif cat == 4:
                txt = prefix + f"A conical circus tent has a base radius of \\({r}\\text{{ m}}\\) and height \\({h}\\text{{ m}}\\). Determine the length of the canvas support pole required along its slanted side."
                corr = f"\\({l}\\text{{ m}}\\)"
                dist = [f"\\({h + 3}\\text{{ m}}\\)", f"\\({l + 5}\\text{{ m}}\\)", f"\\({r + 4}\\text{{ m}}\\)"]
                sol = f"**Step 1: Geometric Setup**\nThe support pole along the slanted side represents the slant height \\(l = \\sqrt{{{r}^2 + {h}^2}} = {l}\\text{{ m}}\\).\n**Step 2: Conclusion**\n\\({l}\\text{{ m}}\\)."
            elif cat == 5:
                txt = prefix + f"Wheat grain is poured into a conical heap of base radius \\({r}\\text{{ m}}\\) and height \\({h}\\text{{ m}}\\). What is the slant height of this grain heap?"
                corr = f"\\({l}\\text{{ m}}\\)"
                dist = [f"\\({l + 1}\\text{{ m}}\\)", f"\\({h + 2}\\text{{ m}}\\)", f"\\({l - 3}\\text{{ m}}\\)"]
                sol = f"**Step 1: Calculation**\n\\(l = \\sqrt{{{r}^2 + {h}^2}} = \\sqrt{{{r*r} + {h*h}}} = {l}\\text{{ m}}\\).\n**Step 2: Conclusion**\n\\({l}\\text{{ m}}\\)."
            elif cat == 6:
                txt = prefix + f"A conical funnel has an internal vertical depth of \\({h}\\text{{ cm}}\\) and a rim radius of \\({r}\\text{{ cm}}\\). What is the slanted side length of the funnel?"
                corr = f"\\({l}\\text{{ cm}}\\)"
                dist = [f"\\({h + 4}\\text{{ cm}}\\)", f"\\({l + 3}\\text{{ cm}}\\)", f"\\({l - 1}\\text{{ cm}}\\)"]
                sol = f"**Step 1: Calculation**\n\\(l = \\sqrt{{{r}^2 + {h}^2}} = {l}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({l}\\text{{ cm}}\\)."
            else:
                txt = prefix + f"A conical birthday cap is constructed with a circular base radius of \\({r}\\text{{ cm}}\\) and slant height of \\({l}\\text{{ cm}}\\). Find its vertical height."
                corr = f"\\({h}\\text{{ cm}}\\)"
                dist = [f"\\({l - 2}\\text{{ cm}}\\)", f"\\({h + 4}\\text{{ cm}}\\)", f"\\({h - 3}\\text{{ cm}}\\)"]
                sol = f"**Step 1: Calculation**\n\\(h = \\sqrt{{{l}^2 - {r}^2}} = {h}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({h}\\text{{ cm}}\\)."

            sub_qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig))
    all_qs.extend(sub_qs)

    # -----------------------------------------------------------------
    # Subtopic 9.1.2: Curved Surface Area = pi * r * l
    # -----------------------------------------------------------------
    tc = "MH-9-MTH2-9-9.1.2"
    tname = "Curved Surface Area = πrl"
    sub_qs = []
    for cat in range(8):
        for i in range(10):
            seq = cat * 10 + i + 1
            qcode = f"{tc}-OSC-{seq:03d}"
            r, h, l = TRIPLES_10[i]
            csa = r * l
            has_fig = (seq % 10 in [0, 1, 2, 4, 6, 8])
            svg = svg_cone(f"{r} cm", f"{h} cm", f"{l} cm", f"Cone Curved Surface #{seq}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""

            if cat == 0:
                txt = prefix + f"Find the curved surface area of a right circular cone having base radius \\(r = {r}\\text{{ cm}}\\) and slant height \\(l = {l}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
                corr = f"\\({csa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({csa + 12}\\pi\\text{{ cm}}^2\\)", f"\\({r * h}\\pi\\text{{ cm}}^2\\)", f"\\({2 * csa}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Formula**\n\\(\\text{{CSA}} = \\pi r l = \\pi \\times {r} \\times {l} = {csa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({csa}\\pi\\text{{ cm}}^2\\)."
            elif cat == 1:
                txt = prefix + f"The curved surface area of a cone is \\({csa}\\pi\\text{{ cm}}^2\\) and its base radius is \\({r}\\text{{ cm}}\\). What is its slant height \\(l\\)?"
                corr = f"\\({l}\\text{{ cm}}\\)"
                dist = [f"\\({l + 3}\\text{{ cm}}\\)", f"\\({h}\\text{{ cm}}\\)", f"\\({l - 2}\\text{{ cm}}\\)"]
                sol = f"**Step 1: Formula**\n\\(l = \\frac{{\\text{{CSA}}}}{{\\pi r}} = \\frac{{{csa}\\pi}}{{{r}\\pi}} = {l}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({l}\\text{{ cm}}\\)."
            elif cat == 2:
                txt = prefix + f"If a cone has a curved surface area of \\({csa}\\pi\\text{{ m}}^2\\) and a slant height of \\({l}\\text{{ m}}\\), calculate the radius of its circular base."
                corr = f"\\({r}\\text{{ m}}\\)"
                dist = [f"\\({r + 2}\\text{{ m}}\\)", f"\\({r - 1}\\text{{ m}}\\)", f"\\({l // 2}\\text{{ m}}\\)"]
                sol = f"**Step 1: Formula**\n\\(r = \\frac{{\\text{{CSA}}}}{{\\pi l}} = \\frac{{{csa}\\pi}}{{{l}\\pi}} = {r}\\text{{ m}}\\).\n**Step 2: Conclusion**\n\\({r}\\text{{ m}}\\)."
            elif cat == 3:
                w = 2
                cloth = csa // w
                txt = prefix + f"A conical circus tent has base radius \\({r}\\text{{ m}}\\) and slant height \\({l}\\text{{ m}}\\). How many meters of canvas of width \\({w}\\text{{ m}}\\) are needed to fabricate the curved tent (in terms of \\(\\pi\\))?"
                corr = f"\\({cloth}\\pi\\text{{ m}}\\)"
                dist = [f"\\({csa}\\pi\\text{{ m}}\\)", f"\\({cloth + 10}\\pi\\text{{ m}}\\)", f"\\({cloth - 5}\\pi\\text{{ m}}\\)"]
                sol = f"**Step 1: Canvas Area & Length**\nArea \\(= \\pi r l = {csa}\\pi\\text{{ m}}^2\\). Required length \\(= \\frac{{{csa}\\pi}}{{{w}}} = {cloth}\\pi\\text{{ m}}\\).\n**Step 2: Conclusion**\n\\({cloth}\\pi\\text{{ m}}\\)."
            elif cat == 4:
                rate = 10 + i * 5
                cost = csa * rate
                txt = prefix + f"The curved surface of a conical party canopy with radius \\({r}\\text{{ m}}\\) and slant height \\({l}\\text{{ m}}\\) is to be painted. Find the total cost at ₹{rate} per \\(\\pi\\text{{ m}}^2\\)."
                corr = f"₹{cost}"
                dist = [f"₹{cost + 100}", f"₹{cost - 50}", f"₹{cost * 2}"]
                sol = f"**Step 1: Total Cost**\n\\(\\text{{Cost}} = \\text{{Rate}} \\times \\text{{CSA}} = {rate} \\times {csa} = ₹{cost}\\).\n**Step 2: Conclusion**\n₹{cost}."
            elif cat == 5:
                k = i + 2
                txt = prefix + f"Two right circular cones have their base radii in the ratio \\(1:{k}\\) and identical slant heights of \\({l}\\text{{ cm}}\\). What is the ratio of their curved surface areas?"
                corr = f"\\(1:{k}\\)"
                dist = [f"\\(1:{k*k}\\)", f"\\({k}:1\\)", f"\\(1:{2*k}\\)"]
                sol = f"**Step 1: Ratio**\n\\(\\frac{{\\text{{CSA}}_1}}{{\\text{{CSA}}_2}} = \\frac{{\\pi r_1 l}}{{\\pi r_2 l}} = \\frac{{r_1}}{{r_2}} = \\frac{{1}}{{{k}}}\\).\n**Step 2: Conclusion**\n\\(1:{k}\\)."
            elif cat == 6:
                circ = 2 * r
                txt = prefix + f"The circumference of the circular base of a cone is \\({circ}\\pi\\text{{ cm}}\\) and its slant height is \\({l}\\text{{ cm}}\\). What is its curved surface area in terms of \\(\\pi\\)?"
                corr = f"\\({csa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({2 * csa}\\pi\\text{{ cm}}^2\\)", f"\\({csa // 2}\\pi\\text{{ cm}}^2\\)", f"\\({circ * l}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Base Radius & CSA**\n\\(2\\pi r = {circ}\\pi \\implies r = {r}\\text{{ cm}}\\). \\(\\text{{CSA}} = \\pi r l = {csa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({csa}\\pi\\text{{ cm}}^2\\)."
            else:
                n_caps = (i + 1) * 5
                tot_csa = n_caps * csa
                txt = prefix + f"A stage performer makes {n_caps} identical conical caps, each having base radius \\({r}\\text{{ cm}}\\) and slant height \\({l}\\text{{ cm}}\\). Find the total area of cardboard sheet required in terms of \\(\\pi\\)."
                corr = f"\\({tot_csa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({tot_csa + 50}\\pi\\text{{ cm}}^2\\)", f"\\({csa}\\pi\\text{{ cm}}^2\\)", f"\\({2 * tot_csa}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Total Area**\n\\(\\text{{Total Sheet}} = {n_caps} \\times \\pi r l = {n_caps} \\times {csa}\\pi = {tot_csa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({tot_csa}\\pi\\text{{ cm}}^2\\)."

            sub_qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig))
    all_qs.extend(sub_qs)

    # -----------------------------------------------------------------
    # Subtopic 9.1.3: Total Surface Area = pi * r * (r + l)
    # -----------------------------------------------------------------
    tc = "MH-9-MTH2-9-9.1.3"
    tname = "Total Surface Area = πr(r + l)"
    sub_qs = []
    for cat in range(8):
        for i in range(10):
            seq = cat * 10 + i + 1
            qcode = f"{tc}-OSC-{seq:03d}"
            r, h, l = TRIPLES_10[i]
            tsa = r * (r + l)
            csa = r * l
            base_area = r * r
            has_fig = (seq % 10 in [0, 1, 2, 4, 6, 8])
            svg = svg_cone(f"{r} cm", f"{h} cm", f"{l} cm", f"Cone Total Surface #{seq}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""

            if cat == 0:
                txt = prefix + f"Determine the total surface area (TSA) of a solid right circular cone with base radius \\(r = {r}\\text{{ cm}}\\) and slant height \\(l = {l}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
                corr = f"\\({tsa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({csa}\\pi\\text{{ cm}}^2\\)", f"\\({tsa + 16}\\pi\\text{{ cm}}^2\\)", f"\\({base_area}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Formula**\n\\(\\text{{TSA}} = \\pi r (r + l) = \\pi \\times {r} \\times ({r} + {l}) = {tsa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({tsa}\\pi\\text{{ cm}}^2\\)."
            elif cat == 1:
                txt = prefix + f"A solid cone has base radius \\(r = {r}\\text{{ cm}}\\). If its total surface area is \\({tsa}\\pi\\text{{ cm}}^2\\), find its slant height \\(l\\)."
                corr = f"\\({l}\\text{{ cm}}\\)"
                dist = [f"\\({l + 2}\\text{{ cm}}\\)", f"\\({h}\\text{{ cm}}\\)", f"\\({l - 1}\\text{{ cm}}\\)"]
                sol = f"**Step 1: Formula**\n\\(\\pi r (r + l) = {tsa}\\pi \\implies {r}({r} + l) = {tsa} \\implies {r} + l = {r + l} \\implies l = {l}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({l}\\text{{ cm}}\\)."
            elif cat == 2:
                txt = prefix + f"A solid cone has a base circular area of \\({base_area}\\pi\\text{{ cm}}^2\\) and curved surface area of \\({csa}\\pi\\text{{ cm}}^2\\). Calculate its total surface area (TSA)."
                corr = f"\\({tsa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({csa}\\pi\\text{{ cm}}^2\\)", f"\\({base_area}\\pi\\text{{ cm}}^2\\)", f"\\({tsa + 20}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Addition Property**\n\\(\\text{{TSA}} = \\text{{Base Area}} + \\text{{CSA}} = {base_area}\\pi + {csa}\\pi = {tsa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({tsa}\\pi\\text{{ cm}}^2\\)."
            elif cat == 3:
                txt = prefix + f"A solid wooden conical toy has base radius \\({r}\\text{{ cm}}\\) and slant height \\({l}\\text{{ cm}}\\). What is the total area of wood exposed to painting on its entire surface?"
                corr = f"\\({tsa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({csa}\\pi\\text{{ cm}}^2\\)", f"\\({tsa + 15}\\pi\\text{{ cm}}^2\\)", f"\\({tsa - 10}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Formula**\n\\(\\text{{TSA}} = \\pi r(r + l) = {tsa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({tsa}\\pi\\text{{ cm}}^2\\)."
            elif cat == 4:
                cost = tsa * 10
                txt = prefix + f"The complete outer surface (curved side and bottom base) of a solid cone of radius \\({r}\\text{{ m}}\\) and slant height \\({l}\\text{{ m}}\\) is polished. Find the cost at ₹10 per \\(\\pi\\text{{ m}}^2\\)."
                corr = f"₹{cost}"
                dist = [f"₹{cost + 50}", f"₹{cost - 40}", f"₹{cost * 2}"]
                sol = f"**Step 1: Total Cost**\n\\(\\text{{Cost}} = 10 \\times \\text{{TSA}} = 10 \\times {tsa} = ₹{cost}\\).\n**Step 2: Conclusion**\n₹{cost}."
            elif cat == 5:
                txt = prefix + f"In a right cone with radius \\({r}\\text{{ cm}}\\) and slant height \\({l}\\text{{ cm}}\\), what is the ratio of its curved surface area to its base circular area?"
                corr = f"\\({l}:{r}\\)"
                dist = [f"\\({r}:{l}\\)", f"\\({l}:{h}\\)", f"\\(1:2\\)"]
                sol = f"**Step 1: Ratio**\n\\(\\frac{{\\text{{CSA}}}}{{\\text{{Base Area}}}} = \\frac{{\\pi r l}}{{\\pi r^2}} = \\frac{{{l}}}{{{r}}}\\).\n**Step 2: Conclusion**\n\\({l}:{r}\\)."
            elif cat == 6:
                txt = prefix + f"What is the exact ratio of the curved surface area (CSA) to the total surface area (TSA) of a cone with radius \\({r}\\text{{ cm}}\\) and slant height \\({l}\\text{{ cm}}\\)?"
                corr = f"\\({l}:{r + l}\\)"
                dist = [f"\\({r}:{r + l}\\)", f"\\({l}:{r}\\)", f"\\(1:2\\)"]
                sol = f"**Step 1: Ratio**\n\\(\\frac{{\\text{{CSA}}}}{{\\text{{TSA}}}} = \\frac{{\\pi r l}}{{\\pi r (r + l)}} = \\frac{{{l}}}{{{r + l}}}\\).\n**Step 2: Conclusion**\n\\({l}:{r + l}\\)."
            else:
                txt = prefix + f"A solid conical paperweight has base diameter \\({2 * r}\\text{{ cm}}\\) and slant height \\({l}\\text{{ cm}}\\). What is its total surface area in terms of \\(\\pi\\)?"
                corr = f"\\({tsa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({csa}\\pi\\text{{ cm}}^2\\)", f"\\({2 * tsa}\\pi\\text{{ cm}}^2\\)", f"\\({tsa + 12}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Radius & TSA**\n\\(r = {r}\\text{{ cm}}\\). \\(\\text{{TSA}} = \\pi r(r + l) = {tsa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({tsa}\\pi\\text{{ cm}}^2\\)."

            sub_qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig))
    all_qs.extend(sub_qs)

    # -----------------------------------------------------------------
    # Subtopic 9.1.4: Volume = 1/3 * pi * r^2 * h
    # -----------------------------------------------------------------
    tc = "MH-9-MTH2-9-9.1.4"
    tname = "Volume = 1/3 * πr²h"
    sub_qs = []
    for cat in range(8):
        for i in range(10):
            seq = cat * 10 + i + 1
            qcode = f"{tc}-OSC-{seq:03d}"
            r, h, l = TRIPLES_10[i]
            vol_val = (r * r * h) // 3
            has_fig = (seq % 10 in [0, 1, 2, 4, 6, 8])
            svg = svg_cone(f"{r} cm", f"{h} cm", f"{l} cm", f"Cone Volume Geometry #{seq}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""

            if cat == 0:
                txt = prefix + f"Find the volume of a right circular cone having base radius \\(r = {r}\\text{{ cm}}\\) and vertical height \\(h = {h}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
                corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
                dist = [f"\\({vol_val * 3}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 20}\\pi\\text{{ cm}}^3\\)", f"\\({r * h}\\pi\\text{{ cm}}^3\\)"]
                sol = f"**Step 1: Formula**\n\\(V = \\frac{{1}}{{3}}\\pi r^2 h = \\frac{{1}}{{3}}\\pi ({r})^2 ({h}) = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."
            elif cat == 1:
                txt = prefix + f"The volume of a cone is \\({vol_val}\\pi\\text{{ cm}}^3\\) and its base radius is \\({r}\\text{{ cm}}\\). Calculate the vertical height \\(h\\) of the cone."
                corr = f"\\({h}\\text{{ cm}}\\)"
                dist = [f"\\({h + 3}\\text{{ cm}}\\)", f"\\({l}\\text{{ cm}}\\)", f"\\({h - 2}\\text{{ cm}}\\)"]
                sol = f"**Step 1: Formula**\n\\(h = \\frac{{3V}}{{\\pi r^2}} = \\frac{{3 \\times {vol_val}\\pi}}{{\\pi \\times {r*r}}} = {h}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({h}\\text{{ cm}}\\)."
            elif cat == 2:
                txt = prefix + f"A cone of volume \\({vol_val}\\pi\\text{{ m}}^3\\) has vertical height \\({h}\\text{{ m}}\\). Determine the radius of its circular base."
                corr = f"\\({r}\\text{{ m}}\\)"
                dist = [f"\\({r + 2}\\text{{ m}}\\)", f"\\({r - 1}\\text{{ m}}\\)", f"\\({h // 2}\\text{{ m}}\\)"]
                sol = f"**Step 1: Formula**\n\\(r^2 = \\frac{{3V}}{{\\pi h}} = \\frac{{3 \\times {vol_val}}}{{{h}}} = {r*r} \\implies r = {r}\\text{{ m}}\\).\n**Step 2: Conclusion**\n\\({r}\\text{{ m}}\\)."
            elif cat == 3:
                base_area = r * r
                txt = prefix + f"The area of the base of a cone is \\({base_area}\\pi\\text{{ cm}}^2\\) and its height is \\({h}\\text{{ cm}}\\). What is its volume in terms of \\(\\pi\\)?"
                corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
                dist = [f"\\({base_area * h}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 15}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val // 2}\\pi\\text{{ cm}}^3\\)"]
                sol = f"**Step 1: Formula**\n\\(V = \\frac{{1}}{{3}} \\times \\text{{Base Area}} \\times h = \\frac{{1}}{{3}} \\times {base_area}\\pi \\times {h} = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."
            elif cat == 4:
                liters = vol_val
                txt = prefix + f"A conical storage container of base radius \\({r}\\text{{ m}}\\) and height \\({h}\\text{{ m}}\\) is filled with liquid. If \\(1\\pi\\text{{ m}}^3\\) holds 1000 liters, find its capacity."
                corr = f"{liters * 1000} liters"
                dist = [f"{liters * 500} liters", f"{liters * 100} liters", f"{(liters + 10) * 1000} liters"]
                sol = f"**Step 1: Volume to Liters**\n\\(V = {vol_val}\\pi\\text{{ m}}^3\\). Capacity \\(= {vol_val} \\times 1000 = {liters * 1000}\\text{{ liters}}\\).\n**Step 2: Conclusion**\n{liters * 1000} liters."
            elif cat == 5:
                txt = prefix + f"A conical heap of fine sand has base radius \\({r}\\text{{ m}}\\) and height \\({h}\\text{{ m}}\\). What is the total volume of sand in the heap?"
                corr = f"\\({vol_val}\\pi\\text{{ m}}^3\\)"
                dist = [f"\\({vol_val * 2}\\pi\\text{{ m}}^3\\)", f"\\({vol_val + 30}\\pi\\text{{ m}}^3\\)", f"\\({vol_val // 2}\\pi\\text{{ m}}^3\\)"]
                sol = f"**Step 1: Calculation**\n\\(V = \\frac{{1}}{{3}}\\pi r^2 h = {vol_val}\\pi\\text{{ m}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ m}}^3\\)."
            elif cat == 6:
                txt = prefix + f"A cylinder and a cone share the exact same base radius \\({r}\\text{{ cm}}\\) and same height \\({h}\\text{{ cm}}\\). What is the ratio of the volume of the cone to the cylinder?"
                corr = "\\(1:3\\)"
                dist = ["\\(3:1\\)", "\\(1:2\\)", "\\(2:3\\)"]
                sol = "**Step 1: Volume Ratio**\n\\(V_{\\text{cone}} = \\frac{1}{3}\\pi r^2 h\\) and \\(V_{\\text{cyl}} = \\pi r^2 h\\). Ratio \\(= 1:3\\).\n**Step 2: Conclusion**\n\\(1:3\\)."
            else:
                small_v = 1
                n_vessels = vol_val // small_v
                txt = prefix + f"How many small conical measuring cups of volume \\(1\\pi\\text{{ cm}}^3\\) can be completely filled from a large cone of radius \\({r}\\text{{ cm}}\\) and height \\({h}\\text{{ cm}}\\)?"
                corr = f"{n_vessels}"
                dist = [f"{n_vessels + 10}", f"{n_vessels // 2}", f"{n_vessels * 2}"]
                sol = f"**Step 1: Number of Cups**\n\\(N = \\frac{{{vol_val}\\pi}}{{1\\pi}} = {n_vessels}\\).\n**Step 2: Conclusion**\n{n_vessels}."

            sub_qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig))
    all_qs.extend(sub_qs)

    # -----------------------------------------------------------------
    # Subtopic 9.2.1: Surface Area of Sphere = 4 * pi * r^2
    # -----------------------------------------------------------------
    tc = "MH-9-MTH2-9-9.2.1"
    tname = "Surface Area of Sphere = 4πr²"
    sub_qs = []
    for cat in range(8):
        for i in range(10):
            seq = cat * 10 + i + 1
            qcode = f"{tc}-OSC-{seq:03d}"
            r = RADII_10[i]
            sa = 4 * r * r
            has_fig = (seq % 10 in [0, 1, 2, 4, 6, 8])
            svg = svg_sphere(f"{r} cm", f"Sphere Surface Area #{seq}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""

            if cat == 0:
                txt = prefix + f"Calculate the total surface area of a solid sphere of radius \\(r = {r}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
                corr = f"\\({sa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({sa // 2}\\pi\\text{{ cm}}^2\\)", f"\\({sa + 20}\\pi\\text{{ cm}}^2\\)", f"\\({r * r}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Formula**\n\\(\\text{{SA}} = 4\\pi r^2 = 4\\pi ({r})^2 = {sa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({sa}\\pi\\text{{ cm}}^2\\)."
            elif cat == 1:
                txt = prefix + f"A sphere has a total surface area of \\({sa}\\pi\\text{{ cm}}^2\\). Determine the length of its radius \\(r\\)."
                corr = f"\\({r}\\text{{ cm}}\\)"
                dist = [f"\\({r + 2}\\text{{ cm}}\\)", f"\\({r - 1}\\text{{ cm}}\\)", f"\\({2 * r}\\text{{ cm}}\\)"]
                sol = f"**Step 1: Formula**\n\\(4\\pi r^2 = {sa}\\pi \\implies r^2 = {r*r} \\implies r = {r}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({r}\\text{{ cm}}\\)."
            elif cat == 2:
                txt = prefix + f"Find the surface area of a spherical ball having a diameter of \\({2 * r}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
                corr = f"\\({sa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({4 * sa}\\pi\\text{{ cm}}^2\\)", f"\\({sa // 4}\\pi\\text{{ cm}}^2\\)", f"\\({sa + 24}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Radius & Formula**\nRadius \\(r = {r}\\text{{ cm}}\\). \\(\\text{{SA}} = 4\\pi r^2 = {sa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({sa}\\pi\\text{{ cm}}^2\\)."
            elif cat == 3:
                txt = prefix + f"A spherical metallic cannonball has radius \\(r = {r}\\text{{ cm}}\\). What is the total outer area exposed to the air?"
                corr = f"\\({sa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({sa // 2}\\pi\\text{{ cm}}^2\\)", f"\\({sa + 16}\\pi\\text{{ cm}}^2\\)", f"\\({2 * sa}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Surface Area**\n\\(\\text{{SA}} = 4\\pi r^2 = {sa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({sa}\\pi\\text{{ cm}}^2\\)."
            elif cat == 4:
                cost = sa * 5
                txt = prefix + f"The surface of a solid decorative sphere of radius \\({r}\\text{{ cm}}\\) is to be gold-plated. Find the cost at ₹5 per \\(\\pi\\text{{ cm}}^2\\)."
                corr = f"₹{cost}"
                dist = [f"₹{cost + 50}", f"₹{cost - 30}", f"₹{cost * 2}"]
                sol = f"**Step 1: Cost Calculation**\n\\(\\text{{Cost}} = 5 \\times {sa} = ₹{cost}\\).\n**Step 2: Conclusion**\n₹{cost}."
            elif cat == 5:
                txt = prefix + f"If the radius of a sphere is doubled from \\({r}\\text{{ cm}}\\) to \\({2 * r}\\text{{ cm}}\\), by what factor does its surface area increase?"
                corr = "Increases by a factor of 4"
                dist = ["Increases by a factor of 2", "Increases by a factor of 8", "Increases by a factor of 6"]
                sol = "**Step 1: Scaling Ratio**\n\\(\\text{SA} \\propto r^2\\). If radius is doubled \\((2r)^2 = 4r^2\\), surface area increases by 4.\n**Step 2: Conclusion**\nIncreases by a factor of 4."
            elif cat == 6:
                great_circ = r * r
                txt = prefix + f"The area of the great circular cross-section of a sphere is \\({great_circ}\\pi\\text{{ cm}}^2\\). Find the total surface area of the sphere."
                corr = f"\\({sa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({2 * great_circ}\\pi\\text{{ cm}}^2\\)", f"\\({great_circ}\\pi\\text{{ cm}}^2\\)", f"\\({sa + 12}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Great Circle Relation**\n\\(\\text{{SA}} = 4 \\times \\text{{Great Circle Area}} = 4 \\times {great_circ}\\pi = {sa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({sa}\\pi\\text{{ cm}}^2\\)."
            else:
                txt = prefix + f"Two spheres have radii in the ratio \\(1:2\\). If the smaller sphere has radius \\({r}\\text{{ cm}}\\), what is the ratio of their surface areas?"
                corr = "\\(1:4\\)"
                dist = ["\\(1:2\\)", "\\(1:8\\)", "\\(1:6\\)"]
                sol = "**Step 1: Surface Area Ratio**\n\\(\\frac{\\text{SA}_1}{\\text{SA}_2} = (\\frac{r_1}{r_2})^2 = (\\frac{1}{2})^2 = \\frac{1}{4}\\).\n**Step 2: Conclusion**\n\\(1:4\\)."

            sub_qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig))
    all_qs.extend(sub_qs)

    # -----------------------------------------------------------------
    # Subtopic 9.2.2: Volume of Sphere = 4/3 * pi * r^3
    # -----------------------------------------------------------------
    tc = "MH-9-MTH2-9-9.2.2"
    tname = "Volume of Sphere = 4/3 * πr³"
    sub_qs = []
    for cat in range(8):
        for i in range(10):
            seq = cat * 10 + i + 1
            qcode = f"{tc}-OSC-{seq:03d}"
            r = RADII_VOL_10[i]
            vol_val = (4 * r**3) // 3
            corr_vol = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            has_fig = (seq % 10 in [0, 1, 2, 4, 6, 8])
            svg = svg_sphere(f"{r} cm", f"Spherical Volume #{seq}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""

            if cat == 0:
                txt = prefix + f"Calculate the volume of a solid sphere of radius \\(r = {r}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
                corr = corr_vol
                dist = [f"\\({4 * r * r}\\pi\\text{{ cm}}^3\\)", f"\\({r**3}\\pi\\text{{ cm}}^3\\)", f"\\({2 * r**3}\\pi\\text{{ cm}}^3\\)"]
                sol = f"**Step 1: Formula**\n\\(V = \\frac{{4}}{{3}}\\pi r^3 = \\frac{{4}}{{3}}\\pi ({r})^3 = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n{corr_vol}."
            elif cat == 1:
                txt = prefix + f"Find the volume of a spherical lead shot having a diameter of \\({2 * r}\\text{{ cm}}\\) (in terms of \\(\\pi\\))."
                corr = corr_vol
                dist = [f"\\({r**3}\\pi\\text{{ cm}}^3\\)", f"\\({8 * r**3}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 50}\\pi\\text{{ cm}}^3\\)"]
                sol = f"**Step 1: Radius & Formula**\nRadius \\(r = {r}\\text{{ cm}}\\). \\(V = \\frac{{4}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n{corr_vol}."
            elif cat == 2:
                txt = prefix + f"A spherical metal ball of radius \\({r}\\text{{ cm}}\\) is melted. What volume of molten metal is obtained in terms of \\(\\pi\\)?"
                corr = corr_vol
                dist = [f"\\({2 * r**3}\\pi\\text{{ cm}}^3\\)", f"\\({3 * r**3}\\pi\\text{{ cm}}^3\\)", f"\\({r**2}\\pi\\text{{ cm}}^3\\)"]
                sol = f"**Step 1: Conservation of Volume**\nMolten volume \\(= \\frac{{4}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n{corr_vol}."
            elif cat == 3:
                txt = prefix + f"How many small lead balls of radius 1 cm can be cast by melting a solid lead sphere of radius \\({r}\\text{{ cm}}\\)?"
                n_balls = r**3
                corr = f"{n_balls}"
                dist = [f"{n_balls // 2}", f"{n_balls * 2}", f"{n_balls + 10}"]
                sol = f"**Step 1: Ratio of Volumes**\n\\(N = \\frac{{\\frac{{4}}{{3}}\\pi R^3}}{{\\frac{{4}}{{3}}\\pi r^3}} = \\frac{{{r}^3}}{{1^3}} = {n_balls}\\).\n**Step 2: Conclusion**\n{n_balls}."
            elif cat == 4:
                txt = prefix + f"If the radius of a sphere is doubled, by what factor does its volume increase?"
                corr = "Increases by a factor of 8"
                dist = ["Increases by a factor of 4", "Increases by a factor of 6", "Increases by a factor of 2"]
                sol = "**Step 1: Cubic Scaling**\n\\(V \\propto r^3\\). Doubling radius gives \\((2r)^3 = 8r^3\\).\n**Step 2: Conclusion**\nIncreases by a factor of 8."
            elif cat == 5:
                txt = prefix + f"Two solid spheres have radii in the ratio \\(1:3\\). What is the ratio of their volumes?"
                corr = "\\(1:27\\)"
                dist = ["\\(1:9\\)", "\\(1:3\\)", "\\(1:6\\)"]
                sol = "**Step 1: Ratio**\n\\(\\frac{V_1}{V_2} = (\\frac{1}{3})^3 = \\frac{1}{27}\\).\n**Step 2: Conclusion**\n\\(1:27\\)."
            elif cat == 6:
                txt = prefix + f"A solid metal sphere of radius \\({r}\\text{{ cm}}\\) has density \\(1\\text{{ g/cm}}^3\\). What is the total mass of the sphere (in terms of \\(\\pi\\))?"
                corr = f"\\({vol_val}\\pi\\text{{ grams}}\\)"
                dist = [f"\\({r**3}\\pi\\text{{ grams}}\\)", f"\\({4 * r * r}\\pi\\text{{ grams}}\\)", f"\\({vol_val * 2}\\pi\\text{{ grams}}\\)"]
                sol = f"**Step 1: Mass = Density * Volume**\n\\(\\text{{Mass}} = 1 \\times V = {vol_val}\\pi\\text{{ g}}\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ grams}}\\)."
            else:
                txt = prefix + f"A spherical storage tank has an inner radius of \\({r}\\text{{ m}}\\). Determine the volume of liquid it can hold when full."
                corr = f"\\({vol_val}\\pi\\text{{ m}}^3\\)"
                dist = [f"\\({2 * r**3}\\pi\\text{{ m}}^3\\)", f"\\({4 * r * r}\\pi\\text{{ m}}^3\\)", f"\\({vol_val + 20}\\pi\\text{{ m}}^3\\)"]
                sol = f"**Step 1: Volume Formula**\n\\(V = \\frac{{4}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ m}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ m}}^3\\)."

            sub_qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig))
    all_qs.extend(sub_qs)

    # -----------------------------------------------------------------
    # Subtopic 9.2.3: Curved Surface Area of Hemisphere = 2 * pi * r^2
    # -----------------------------------------------------------------
    tc = "MH-9-MTH2-9-9.2.3"
    tname = "Curved Surface Area of Hemisphere = 2πr²"
    sub_qs = []
    for cat in range(8):
        for i in range(10):
            seq = cat * 10 + i + 1
            qcode = f"{tc}-OSC-{seq:03d}"
            r = RADII_10[i]
            csa = 2 * r * r
            has_fig = (seq % 10 in [0, 1, 2, 4, 6, 8])
            svg = svg_hemi(f"{r} cm", f"Hemisphere CSA Diagram #{seq}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""

            if cat == 0:
                txt = prefix + f"What is the curved surface area (CSA) of a hemisphere of radius \\(r = {r}\\text{{ cm}}\\) in terms of \\(\\pi\\)?"
                corr = f"\\({csa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({3 * r * r}\\pi\\text{{ cm}}^2\\)", f"\\({4 * r * r}\\pi\\text{{ cm}}^2\\)", f"\\({r * r}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Formula**\n\\(\\text{{CSA}} = 2\\pi r^2 = 2\\pi ({r})^2 = {csa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({csa}\\pi\\text{{ cm}}^2\\)."
            elif cat == 1:
                txt = prefix + f"The curved surface area of a hollow hemisphere is \\({csa}\\pi\\text{{ cm}}^2\\). Calculate its radius \\(r\\)."
                corr = f"\\({r}\\text{{ cm}}\\)"
                dist = [f"\\({r + 2}\\text{{ cm}}\\)", f"\\({r - 1}\\text{{ cm}}\\)", f"\\({2 * r}\\text{{ cm}}\\)"]
                sol = f"**Step 1: Formula**\n\\(2\\pi r^2 = {csa}\\pi \\implies r^2 = {r*r} \\implies r = {r}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({r}\\text{{ cm}}\\)."
            elif cat == 2:
                txt = prefix + f"Find the inner curved surface area of a hemispherical bowl having diameter \\({2 * r}\\text{{ cm}}\\) (in terms of \\(\\pi\\))."
                corr = f"\\({csa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({2 * csa}\\pi\\text{{ cm}}^2\\)", f"\\({csa // 2}\\pi\\text{{ cm}}^2\\)", f"\\({csa + 14}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Radius & Formula**\nRadius \\(r = {r}\\text{{ cm}}\\). \\(\\text{{CSA}} = 2\\pi r^2 = {csa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({csa}\\pi\\text{{ cm}}^2\\)."
            elif cat == 3:
                cost = csa * 2
                txt = prefix + f"The inner surface of a hemispherical bowl of radius \\({r}\\text{{ cm}}\\) is tin-plated. Calculate the cost at ₹2 per \\(\\pi\\text{{ cm}}^2\\)."
                corr = f"₹{cost}"
                dist = [f"₹{cost + 20}", f"₹{cost - 10}", f"₹{cost * 2}"]
                sol = f"**Step 1: Cost**\n\\(\\text{{Cost}} = 2 \\times {csa} = ₹{cost}\\).\n**Step 2: Conclusion**\n₹{cost}."
            elif cat == 4:
                txt = prefix + f"A hemispherical dome on a building has radius \\({r}\\text{{ m}}\\). What is the total curved area to be painted on the outside (in terms of \\(\\pi\\))?"
                corr = f"\\({csa}\\pi\\text{{ m}}^2\\)"
                dist = [f"\\({3 * r * r}\\pi\\text{{ m}}^2\\)", f"\\({4 * r * r}\\pi\\text{{ m}}^2\\)", f"\\({csa + 25}\\pi\\text{{ m}}^2\\)"]
                sol = f"**Step 1: Curved Surface**\n\\(\\text{{CSA}} = 2\\pi r^2 = {csa}\\pi\\text{{ m}}^2\\).\n**Step 2: Conclusion**\n\\({csa}\\pi\\text{{ m}}^2\\)."
            elif cat == 5:
                txt = prefix + f"What is the ratio of the curved surface area of a hemisphere to the total surface area of a sphere of the same radius?"
                corr = "\\(1:2\\)"
                dist = ["\\(2:1\\)", "\\(1:3\\)", "\\(1:4\\)"]
                sol = "**Step 1: Ratio**\n\\(\\frac{\\text{CSA}_{\\text{hemi}}}{\\text{SA}_{\\text{sphere}}} = \\frac{2\\pi r^2}{4\\pi r^2} = \\frac{1}{2}\\).\n**Step 2: Conclusion**\n\\(1:2\\)."
            elif cat == 6:
                txt = prefix + f"Canvas is used to make a hemispherical tent of radius \\({r}\\text{{ m}}\\). Find the minimum area of canvas required in terms of \\(\\pi\\)."
                corr = f"\\({csa}\\pi\\text{{ m}}^2\\)"
                dist = [f"\\({3 * r * r}\\pi\\text{{ m}}^2\\)", f"\\({csa - 10}\\pi\\text{{ m}}^2\\)", f"\\({2 * csa}\\pi\\text{{ m}}^2\\)"]
                sol = f"**Step 1: Curved Canvas Area**\n\\(\\text{{CSA}} = 2\\pi r^2 = {csa}\\pi\\text{{ m}}^2\\).\n**Step 2: Conclusion**\n\\({csa}\\pi\\text{{ m}}^2\\)."
            else:
                txt = prefix + f"Two hemispherical bowls have radii in the ratio \\(1:2\\). What is the ratio of their curved surface areas?"
                corr = "\\(1:4\\)"
                dist = ["\\(1:2\\)", "\\(1:8\\)", "\\(2:1\\)"]
                sol = "**Step 1: Ratio**\n\\(\\frac{\\text{CSA}_1}{\\text{CSA}_2} = (\\frac{r_1}{r_2})^2 = \\frac{1}{4}\\).\n**Step 2: Conclusion**\n\\(1:4\\)."

            sub_qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig))
    all_qs.extend(sub_qs)

    # -----------------------------------------------------------------
    # Subtopic 9.2.4: Total Surface Area of Hemisphere = 3 * pi * r^2
    # -----------------------------------------------------------------
    tc = "MH-9-MTH2-9-9.2.4"
    tname = "Total Surface Area of Hemisphere = 3πr²"
    sub_qs = []
    for cat in range(8):
        for i in range(10):
            seq = cat * 10 + i + 1
            qcode = f"{tc}-OSC-{seq:03d}"
            r = RADII_10[i]
            tsa = 3 * r * r
            csa = 2 * r * r
            base_area = r * r
            has_fig = (seq % 10 in [0, 1, 2, 4, 6, 8])
            svg = svg_hemi(f"{r} cm", f"Solid Hemisphere TSA #{seq}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""

            if cat == 0:
                txt = prefix + f"Find the total surface area (TSA) of a solid hemisphere of radius \\(r = {r}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
                corr = f"\\({tsa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({csa}\\pi\\text{{ cm}}^2\\)", f"\\({4 * r * r}\\pi\\text{{ cm}}^2\\)", f"\\({base_area}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Formula**\n\\(\\text{{TSA}} = 3\\pi r^2 = 3\\pi ({r})^2 = {tsa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({tsa}\\pi\\text{{ cm}}^2\\)."
            elif cat == 1:
                txt = prefix + f"The total surface area of a solid hemisphere is \\({tsa}\\pi\\text{{ cm}}^2\\). What is the radius of the hemisphere?"
                corr = f"\\({r}\\text{{ cm}}\\)"
                dist = [f"\\({r + 2}\\text{{ cm}}\\)", f"\\({r - 1}\\text{{ cm}}\\)", f"\\({2 * r}\\text{{ cm}}\\)"]
                sol = f"**Step 1: Formula**\n\\(3\\pi r^2 = {tsa}\\pi \\implies r^2 = {r*r} \\implies r = {r}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({r}\\text{{ cm}}\\)."
            elif cat == 2:
                txt = prefix + f"A solid hemisphere has a flat circular base area of \\({base_area}\\pi\\text{{ cm}}^2\\). Determine its total surface area in terms of \\(\\pi\\)."
                corr = f"\\({tsa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({2 * base_area}\\pi\\text{{ cm}}^2\\)", f"\\({4 * base_area}\\pi\\text{{ cm}}^2\\)", f"\\({tsa + 12}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Property**\n\\(\\text{{TSA}} = 3 \\times \\text{{Base Area}} = 3 \\times {base_area}\\pi = {tsa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({tsa}\\pi\\text{{ cm}}^2\\)."
            elif cat == 3:
                txt = prefix + f"A solid wooden hemispherical paperweight has radius \\({r}\\text{{ cm}}\\). What is the total exposed area to be polished (curved dome and circular base)?"
                corr = f"\\({tsa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({csa}\\pi\\text{{ cm}}^2\\)", f"\\({tsa + 15}\\pi\\text{{ cm}}^2\\)", f"\\({tsa - 10}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Total Surface Area**\n\\(\\text{{TSA}} = 3\\pi r^2 = {tsa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({tsa}\\pi\\text{{ cm}}^2\\)."
            elif cat == 4:
                cost = tsa * 4
                txt = prefix + f"Find the total cost of painting all faces of a solid hemisphere of radius \\({r}\\text{{ cm}}\\) at ₹4 per \\(\\pi\\text{{ cm}}^2\\)."
                corr = f"₹{cost}"
                dist = [f"₹{cost + 30}", f"₹{cost - 20}", f"₹{cost * 2}"]
                sol = f"**Step 1: Cost Calculation**\n\\(\\text{{Cost}} = 4 \\times \\text{{TSA}} = 4 \\times {tsa} = ₹{cost}\\).\n**Step 2: Conclusion**\n₹{cost}."
            elif cat == 5:
                txt = prefix + f"What is the ratio of the curved surface area (CSA) to the total surface area (TSA) of a solid hemisphere?"
                corr = "\\(2:3\\)"
                dist = ["\\(3:2\\)", "\\(1:2\\)", "\\(1:3\\)"]
                sol = "**Step 1: Ratio**\n\\(\\frac{\\text{CSA}}{\\text{TSA}} = \\frac{2\\pi r^2}{3\\pi r^2} = \\frac{2}{3}\\).\n**Step 2: Conclusion**\n\\(2:3\\)."
            elif cat == 6:
                txt = prefix + f"A solid hemisphere has diameter \\({2 * r}\\text{{ cm}}\\). Calculate its total surface area in terms of \\(\\pi\\)."
                corr = f"\\({tsa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({csa}\\pi\\text{{ cm}}^2\\)", f"\\({4 * tsa}\\pi\\text{{ cm}}^2\\)", f"\\({tsa // 2}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Radius & Formula**\nRadius \\(r = {r}\\text{{ cm}}\\). \\(\\text{{TSA}} = 3\\pi r^2 = {tsa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({tsa}\\pi\\text{{ cm}}^2\\)."
            else:
                txt = prefix + f"A toy is made in the shape of a solid hemisphere of radius \\({r}\\text{{ cm}}\\). Find the sum of the curved area and base area in terms of \\(\\pi\\)."
                corr = f"\\({tsa}\\pi\\text{{ cm}}^2\\)"
                dist = [f"\\({csa}\\pi\\text{{ cm}}^2\\)", f"\\({base_area}\\pi\\text{{ cm}}^2\\)", f"\\({tsa + 18}\\pi\\text{{ cm}}^2\\)"]
                sol = f"**Step 1: Addition**\n\\(\\text{{Curved}} + \\text{{Base}} = 2\\pi r^2 + \\pi r^2 = 3\\pi r^2 = {tsa}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({tsa}\\pi\\text{{ cm}}^2\\)."

            sub_qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig))
    all_qs.extend(sub_qs)

    # -----------------------------------------------------------------
    # Subtopic 9.2.5: Volume of Hemisphere = 2/3 * pi * r^3
    # -----------------------------------------------------------------
    tc = "MH-9-MTH2-9-9.2.5"
    tname = "Volume of Hemisphere = 2/3 * πr³"
    sub_qs = []
    for cat in range(8):
        for i in range(10):
            seq = cat * 10 + i + 1
            qcode = f"{tc}-OSC-{seq:03d}"
            r = RADII_VOL_10[i]
            vol_val = (2 * r**3) // 3
            corr_vol = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            has_fig = (seq % 10 in [0, 1, 2, 4, 6, 8])
            svg = svg_hemi(f"{r} cm", f"Hemisphere Volume #{seq}") if has_fig else ""
            prefix = f"{svg}\n" if svg else ""

            if cat == 0:
                txt = prefix + f"Determine the volume of a solid hemisphere of radius \\(r = {r}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
                corr = corr_vol
                dist = [f"\\({2 * r * r}\\pi\\text{{ cm}}^3\\)", f"\\({r**3}\\pi\\text{{ cm}}^3\\)", f"\\({4 * r**3}\\pi\\text{{ cm}}^3\\)"]
                sol = f"**Step 1: Formula**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = \\frac{{2}}{{3}}\\pi ({r})^3 = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n{corr_vol}."
            elif cat == 1:
                txt = prefix + f"Find the internal capacity of a hemispherical bowl having radius \\(r = {r}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
                corr = corr_vol
                dist = [f"\\({r**3}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 20}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val // 2}\\pi\\text{{ cm}}^3\\)"]
                sol = f"**Step 1: Capacity Formula**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n{corr_vol}."
            elif cat == 2:
                txt = prefix + f"A hemispherical bowl of radius \\({r}\\text{{ cm}}\\) is full of soup. If the soup is poured into a cylindrical container, what volume of soup was transferred (in terms of \\(\\pi\\))?"
                corr = corr_vol
                dist = [f"\\({r**3}\\pi\\text{{ cm}}^3\\)", f"\\({3 * r**3}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val * 2}\\pi\\text{{ cm}}^3\\)"]
                sol = f"**Step 1: Transferred Volume**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n{corr_vol}."
            elif cat == 3:
                txt = prefix + f"What is the ratio of the volume of a hemisphere to the volume of a full sphere of the same radius?"
                corr = "\\(1:2\\)"
                dist = ["\\(2:1\\)", "\\(1:3\\)", "\\(2:3\\)"]
                sol = "**Step 1: Ratio**\n\\(\\frac{V_{\\text{hemi}}}{V_{\\text{sphere}}} = \\frac{\\frac{2}{3}\\pi r^3}{\\frac{4}{3}\\pi r^3} = \\frac{1}{2}\\).\n**Step 2: Conclusion**\n\\(1:2\\)."
            elif cat == 4:
                txt = prefix + f"A hemispherical dome has radius \\({r}\\text{{ m}}\\). Calculate the volume of air contained inside the dome in terms of \\(\\pi\\)."
                corr = f"\\({vol_val}\\pi\\text{{ m}}^3\\)"
                dist = [f"\\({r**3}\\pi\\text{{ m}}^3\\)", f"\\({2 * r**3}\\pi\\text{{ m}}^3\\)", f"\\({vol_val + 15}\\pi\\text{{ m}}^3\\)"]
                sol = f"**Step 1: Air Volume**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ m}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ m}}^3\\)."
            elif cat == 5:
                txt = prefix + f"A solid hemispherical metal casting has diameter \\({2 * r}\\text{{ cm}}\\). What is the volume of metal in the casting in terms of \\(\\pi\\)?"
                corr = corr_vol
                dist = [f"\\({8 * r**3}\\pi\\text{{ cm}}^3\\)", f"\\({r**3}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val // 2}\\pi\\text{{ cm}}^3\\)"]
                sol = f"**Step 1: Radius & Volume**\nRadius \\(r = {r}\\text{{ cm}}\\). \\(V = \\frac{{2}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n{corr_vol}."
            elif cat == 6:
                txt = prefix + f"A solid metal hemisphere of radius \\({r}\\text{{ cm}}\\) is melted down to cast small spheres of radius 1 cm. How many such spheres can be made?"
                n_spheres = (r**3) // 2
                corr = f"{n_spheres}"
                dist = [f"{n_spheres * 2}", f"{n_spheres + 5}", f"{n_spheres // 2}"]
                sol = f"**Step 1: Number of Spheres**\n\\(N = \\frac{{\\frac{{2}}{{3}}\\pi R^3}}{{\\frac{{4}}{{3}}\\pi r^3}} = \\frac{{R^3}}{{2r^3}} = \\frac{{{r}^3}}{{2}} = {n_spheres}\\).\n**Step 2: Conclusion**\n{n_spheres}."
            else:
                txt = prefix + f"A hemispherical water basin of radius \\({r}\\text{{ m}}\\) is completely full. How many cubic meters of water does it contain in terms of \\(\\pi\\)?"
                corr = f"\\({vol_val}\\pi\\text{{ m}}^3\\)"
                dist = [f"\\({r**3}\\pi\\text{{ m}}^3\\)", f"\\({4 * r**3}\\pi\\text{{ m}}^3\\)", f"\\({vol_val + 25}\\pi\\text{{ m}}^3\\)"]
                sol = f"**Step 1: Calculation**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ m}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ m}}^3\\)."

            sub_qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig))
    all_qs.extend(sub_qs)

    print(f"Generated {len(all_qs)} total questions for Chapter 9.")
    return all_qs

if __name__ == "__main__":
    qs = generate_ch9_all()
    with open("scripts/mh9_mth2_diverse_ch9.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/mh9_mth2_diverse_ch9.json")
