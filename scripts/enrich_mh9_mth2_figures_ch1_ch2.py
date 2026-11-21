# scripts/enrich_mh9_mth2_figures_ch1_ch2.py
# Systematically enriches MH-9-MTH2 Chapters 1 & 2 with ~900+ inline SVG figure questions.
# Updates questions in-place by questionCode, strictly preserving Rule 2T 80Q standard packs.

import json
import random

random.seed(42)

def make_unique_opts(corr_text, raw_distractors):
    seen = {str(corr_text).strip()}
    opts = [str(corr_text).strip()]
    for d in raw_distractors:
        sd = str(d).strip()
        if sd not in seen and len(opts) < 4:
            seen.add(sd)
            opts.append(sd)
    
    counter = 1
    while len(opts) < 4:
        cand = f"{corr_text} (var {counter})"
        if cand not in seen:
            seen.add(cand)
            opts.append(cand)
        counter += 1
        
    random.shuffle(opts)
    letters = ['A', 'B', 'C', 'D']
    return [{'id': l, 'text': opt, 'isCorrect': (opt == str(corr_text).strip())} for l, opt in zip(letters, opts)]

def build_q(qcode, topic_code, ch_num, ch_name, t_name, svg_markup, stem_text, corr_text, distractors, solution_text, vault, diff="medium", marks=4):
    opts = make_unique_opts(corr_text, distractors)
    letters = ['A', 'B', 'C', 'D']
    corr_idx = -1
    for idx, o in enumerate(opts):
        if o["isCorrect"]:
            corr_idx = idx
            break
    corr_letter = letters[corr_idx] if corr_idx != -1 else 'A'
    
    full_text = f'{svg_markup}\n{stem_text}' if svg_markup else stem_text
    has_fig = bool(svg_markup)
    
    return {
        "questionCode": qcode,
        "text": full_text,
        "options": opts,
        "correctAnswer": corr_letter,
        "solution": solution_text,
        "boardCode": "MH",
        "board": "Maharashtra Board",
        "class": "9",
        "subjectCode": "MTH2",
        "subject": "Mathematics Part - 2 (Geometry)",
        "chapterNumber": ch_num,
        "chapter": ch_name,
        "topicCode": topic_code,
        "topic": t_name,
        "type": "OSC",
        "typeCode": "OSC",
        "source": vault,
        "vault": vault,
        "marks": marks,
        "negativeMarks": 0,
        "difficulty": diff,
        "status": "active",
        "requiresFigure": has_fig,
        "timesUsed": 0,
        "usedInClassroomTest": False,
        "createdAt": "2026-11-21T15:00:00.000Z",
        "updatedAt": "2026-11-21T15:00:00.000Z"
    }

# ==============================================================================
# SVG BUILDERS FOR CHAPTER 1
# ==============================================================================

def make_number_line_svg(points_dict, title="Coordinate Number Line"):
    # points_dict: { 'A': -4, 'B': 2, ... }
    # Mapping -7 to 7 on 360 width: cx = 180 + val * 22
    svg = [
        '<div style="display: flex; justify-content: center; margin: 12px 0;">',
        '<svg width="100%" height="auto" viewBox="0 0 360 135" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">',
        f'  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>',
        '  <line x1="20" y1="65" x2="340" y2="65" stroke="#64748b" stroke-width="2"/>',
        '  <polygon points="15,65 24,60 24,70" fill="#64748b"/>',
        '  <polygon points="345,65 336,60 336,70" fill="#64748b"/>'
    ]
    # Draw tick marks
    for val in range(-6, 7):
        cx = 180 + val * 22
        svg.append(f'  <line x1="{cx}" y1="60" x2="{cx}" y2="70" stroke="#475569" stroke-width="1.2"/>')
        svg.append(f'  <text x="{cx}" y="86" fill="#64748b" font-size="9" font-family="sans-serif" text-anchor="middle">{val}</text>')
        
    for p_name, val in points_dict.items():
        cx = 180 + val * 22
        svg.append(f'  <circle cx="{cx}" cy="65" r="4.5" fill="#38bdf8"/>')
        svg.append(f'  <text x="{cx}" y="46" fill="#38bdf8" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{p_name}</text>')
        
    svg.append('</svg>\n</div>')
    return '\n'.join(svg)

def make_collinear_svg(p1, p2, p3, len1_str, len2_str, title="Collinear Points"):
    svg = f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 120" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>
  <line x1="40" y1="60" x2="320" y2="60" stroke="#38bdf8" stroke-width="2.5"/>
  <circle cx="50" cy="60" r="4.5" fill="#f8fafc"/>
  <circle cx="170" cy="60" r="4.5" fill="#f59e0b"/>
  <circle cx="310" cy="60" r="4.5" fill="#f8fafc"/>
  <text x="50" y="44" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{p1}</text>
  <text x="170" y="44" fill="#f59e0b" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{p2}</text>
  <text x="310" y="44" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{p3}</text>
  <text x="110" y="85" fill="#38bdf8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{len1_str}</text>
  <text x="240" y="85" fill="#38bdf8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{len2_str}</text>
</svg>
</div>"""
    return svg

def make_midpoint_svg(p1, mid, p2, len_str, title="Midpoint of Segment"):
    svg = f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 120" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>
  <line x1="50" y1="60" x2="310" y2="60" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Congruence ticks on halves -->
  <line x1="112" y1="53" x2="118" y2="67" stroke="#f59e0b" stroke-width="2"/>
  <line x1="242" y1="53" x2="248" y2="67" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="50" cy="60" r="4.5" fill="#f8fafc"/>
  <circle cx="180" cy="60" r="4.5" fill="#f59e0b"/>
  <circle cx="310" cy="60" r="4.5" fill="#f8fafc"/>
  <text x="50" y="44" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{p1}</text>
  <text x="180" y="44" fill="#f59e0b" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{mid}</text>
  <text x="310" y="44" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{p2}</text>
  <text x="180" y="90" fill="#38bdf8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{len_str}</text>
</svg>
</div>"""
    return svg

def make_opposite_rays_svg(p_left, orig, p_right, title="Opposite Rays"):
    svg = f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 120" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>
  <line x1="30" y1="60" x2="330" y2="60" stroke="#38bdf8" stroke-width="2.5"/>
  <polygon points="20,60 32,55 32,65" fill="#38bdf8"/>
  <polygon points="340,60 328,55 328,65" fill="#38bdf8"/>
  <circle cx="90" cy="60" r="4" fill="#f8fafc"/>
  <circle cx="180" cy="60" r="4.5" fill="#f59e0b"/>
  <circle cx="270" cy="60" r="4" fill="#f8fafc"/>
  <text x="90" y="44" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{p_left}</text>
  <text x="180" y="44" fill="#f59e0b" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{orig}</text>
  <text x="270" y="44" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{p_right}</text>
  <text x="180" y="90" fill="#94a3b8" font-size="11" font-family="sans-serif" text-anchor="middle">Ray {orig}{p_left} and Ray {orig}{p_right} are opposite rays</text>
</svg>
</div>"""
    return svg

# ==============================================================================
# SVG BUILDERS FOR CHAPTER 2 (Parallel Lines)
# ==============================================================================

def make_parallel_transversal_svg(ang1_str, ang2_str, mode="alternate", title="Parallel Lines cut by Transversal"):
    # Two horizontal lines at y=55 and y=115
    # Transversal from (80, 20) to (280, 150)
    # Intersections: (130, 55) and (215.7, 115)
    if mode == "alternate":
        # Angle 1 top-right at (155, 75), Angle 2 bot-left at (190, 105)
        pos1 = (155, 75)
        pos2 = (190, 105)
    elif mode == "corresponding":
        # Angle 1 top-right at (155, 50), Angle 2 bot-right at (240, 110)
        pos1 = (155, 50)
        pos2 = (240, 110)
    else: # interior same side
        # Angle 1 top-right at (155, 75), Angle 2 bot-right at (235, 105)
        pos1 = (155, 75)
        pos2 = (235, 105)

    svg = f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 170" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="18" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>
  <line x1="30" y1="55" x2="330" y2="55" stroke="#38bdf8" stroke-width="2.2"/>
  <text x="340" y="59" fill="#38bdf8" font-size="12" font-style="italic" font-family="sans-serif">l</text>
  <line x1="30" y1="115" x2="330" y2="115" stroke="#38bdf8" stroke-width="2.2"/>
  <text x="340" y="119" fill="#38bdf8" font-size="12" font-style="italic" font-family="sans-serif">m</text>
  <line x1="80" y1="20" x2="280" y2="150" stroke="#f59e0b" stroke-width="2.2"/>
  <text x="290" y="155" fill="#f59e0b" font-size="12" font-style="italic" font-family="sans-serif">t</text>
  <circle cx="133.8" cy="55" r="3.5" fill="#f8fafc"/>
  <circle cx="226.2" cy="115" r="3.5" fill="#f8fafc"/>
  <text x="{pos1[0]}" y="{pos1[1]}" fill="#f59e0b" font-size="12" font-weight="bold" font-family="sans-serif">{ang1_str}</text>
  <text x="{pos2[0]}" y="{pos2[1]}" fill="#38bdf8" font-size="12" font-weight="bold" font-family="sans-serif">{ang2_str}</text>
  <text x="60" y="150" fill="#94a3b8" font-size="11" font-family="sans-serif">line l ∥ line m</text>
</svg>
</div>"""
    return svg

def make_perpendicular_parallel_svg():
    svg = """<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 360 170" style="max-width: 360px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="180" y="18" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">Perpendicular to Parallel Lines</text>
  <line x1="40" y1="55" x2="320" y2="55" stroke="#38bdf8" stroke-width="2.2"/>
  <text x="330" y="59" fill="#38bdf8" font-size="12" font-style="italic" font-family="sans-serif">l</text>
  <line x1="40" y1="115" x2="320" y2="115" stroke="#38bdf8" stroke-width="2.2"/>
  <text x="330" y="119" fill="#38bdf8" font-size="12" font-style="italic" font-family="sans-serif">m</text>
  <!-- Perpendicular line p at x=180 -->
  <line x1="180" y1="20" x2="180" y2="150" stroke="#f59e0b" stroke-width="2.2"/>
  <text x="185" y="30" fill="#f59e0b" font-size="12" font-style="italic" font-family="sans-serif">p</text>
  <!-- Right angle symbols -->
  <rect x="180" y="45" width="10" height="10" fill="none" stroke="#f8fafc" stroke-width="1.2"/>
  <rect x="180" y="105" width="10" height="10" fill="none" stroke="#f8fafc" stroke-width="1.2"/>
  <circle cx="180" cy="55" r="3.5" fill="#f8fafc"/>
  <circle cx="180" cy="115" r="3.5" fill="#f8fafc"/>
  <text x="140" y="150" fill="#94a3b8" font-size="11" font-family="sans-serif">line p ⊥ line l, line l ∥ line m ⇒ line p ⊥ line m</text>
</svg>
</div>"""
    return svg

# ==============================================================================
# BATCH GENERATION & IN-PLACE MERGE
# ==============================================================================

enriched_questions = []

print("Enriching Chapter 1 & 2 Questions with Inline SVGs...")

# Load existing ch1_ch2 questions
with open('scripts/mh9_mth2_ch1_ch2_generated.json', 'r', encoding='utf-8') as f:
    ch1_ch2_base = json.load(f)

print(f"Loaded {len(ch1_ch2_base)} base questions for Chapters 1 & 2.")

# Process each question and enrich with SVG based on subtopic
ch1_subtopics = [
    "MH-9-MTH2-1-1.1.1", "MH-9-MTH2-1-1.1.2", "MH-9-MTH2-1-1.2.1", "MH-9-MTH2-1-1.2.2",
    "MH-9-MTH2-1-1.3.1", "MH-9-MTH2-1-1.3.2", "MH-9-MTH2-1-1.3.3", "MH-9-MTH2-1-1.3.4",
    "MH-9-MTH2-1-1.4.1", "MH-9-MTH2-1-1.4.2"
]

ch2_subtopics = [
    "MH-9-MTH2-2-2.1.1", "MH-9-MTH2-2-2.1.2", "MH-9-MTH2-2-2.1.3",
    "MH-9-MTH2-2-2.2.1", "MH-9-MTH2-2-2.2.2", "MH-9-MTH2-2-2.2.3", "MH-9-MTH2-2-2.2.4"
]

fig_count = 0

for q in ch1_ch2_base:
    tc = q["topicCode"]
    seq = int(q["questionCode"].split('-')[-1])
    # Decide whether this question gets a figure (e.g. 70% of questions in visual subtopics)
    should_have_fig = (seq % 10 < 7) # 7 out of every 10 questions = 70%
    
    if not should_have_fig:
        enriched_questions.append(q)
        continue

    svg = None
    # Chapter 1 Subtopics
    if tc == "MH-9-MTH2-1-1.1.1":
        # Coordinates of point on number line
        val = ((seq * 3) % 11) - 5
        pt = chr(65 + (seq % 6))
        svg = make_number_line_svg({pt: val}, f"Number Line: Point {pt}")
        q["text"] = f'{svg}\nIn the number line diagram above, what is the coordinate of point \\({pt}\\)?'
        q["options"] = make_unique_opts(f"\\({val}\\)", [f"\\({val + 2}\\)", f"\\({-val}\\)", f"\\({val - 3}\\)"])
        corr_letter = [o["id"] for o in q["options"] if o["isCorrect"]][0]
        q["correctAnswer"] = corr_letter
        q["solution"] = f"**Step 1: Read Coordinate**\nFrom the number line, point \\({pt}\\) is marked at coordinate \\({val}\\).\n**Step 2: Conclusion**\nCoordinate of \\({pt}\\) is \\({val}\\)."
        q["requiresFigure"] = True
        fig_count += 1

    elif tc == "MH-9-MTH2-1-1.1.2":
        # Distance on number line d(A, B)
        c1 = ((seq * 2) % 6) - 5
        c2 = c1 + ((seq % 5) + 2)
        p1, p2 = "P", "Q"
        d_val = c2 - c1
        svg = make_number_line_svg({p1: c1, p2: c2}, f"Distance d({p1}, {p2}) on Number Line")
        q["text"] = f'{svg}\nRefer to the number line above with points \\({p1}\\) and \\({p2}\\). What is the distance \\(d({p1}, {p2})\\)?'
        q["options"] = make_unique_opts(f"\\({d_val}\\)", [f"\\({d_val + 2}\\)", f"\\({d_val - 1}\\)", f"\\({-d_val}\\)"])
        corr_letter = [o["id"] for o in q["options"] if o["isCorrect"]][0]
        q["correctAnswer"] = corr_letter
        q["solution"] = f"**Step 1: Coordinates**\nCoordinate of \\({p1} = {c1}\\), coordinate of \\({p2} = {c2}\\).\n**Step 2: Formula & Calculation**\n\\(d({p1}, {p2}) = {c2} - ({c1}) = {d_val}\\).\n**Step 3: Conclusion**\n\\(d({p1}, {p2}) = {d_val}\\)."
        q["requiresFigure"] = True
        fig_count += 1

    elif tc == "MH-9-MTH2-1-1.2.1":
        # Betweenness P-Q-R
        l1 = (seq % 7) + 4
        l2 = (seq % 6) + 5
        total = l1 + l2
        svg = make_collinear_svg("P", "Q", "R", f"{l1} cm", f"{l2} cm", "Collinear Points P-Q-R")
        q["text"] = f'{svg}\nAs shown in the collinear points diagram above, \\(P-Q-R\\) with \\(d(P, Q) = {l1}\\text{{ cm}}\\) and \\(d(Q, R) = {l2}\\text{{ cm}}\\). What is \\(d(P, R)\\)?'
        q["options"] = make_unique_opts(f"\\({total}\\text{{ cm}}\\)", [f"\\({total + 3}\\text{{ cm}}\\)", f"\\({total - 2}\\text{{ cm}}\\)", f"\\({abs(l1 - l2)}\\text{{ cm}}\\)"])
        corr_letter = [o["id"] for o in q["options"] if o["isCorrect"]][0]
        q["correctAnswer"] = corr_letter
        q["solution"] = f"**Step 1: Property**\nFor \\(P-Q-R\\), \\(d(P, R) = d(P, Q) + d(Q, R)\\).\n**Step 2: Calculation**\n\\(d(P, R) = {l1} + {l2} = {total}\\text{{ cm}}\\).\n**Step 3: Conclusion**\n\\(d(P, R) = {total}\\text{{ cm}}\\)."
        q["requiresFigure"] = True
        fig_count += 1

    elif tc == "MH-9-MTH2-1-1.3.4":
        # Midpoint of segment
        half_l = (seq % 8) + 4
        tot_l = 2 * half_l
        svg = make_midpoint_svg("A", "M", "B", f"AB = {tot_l} cm", "Midpoint M of Segment AB")
        q["text"] = f'{svg}\nIn the figure above, point \\(M\\) is the midpoint of segment \\(AB\\). If \\(AB = {tot_l}\\text{{ cm}}\\), what is the length of \\(AM\\)?'
        q["options"] = make_unique_opts(f"\\({half_l}\\text{{ cm}}\\)", [f"\\({tot_l}\\text{{ cm}}\\)", f"\\({half_l + 2}\\text{{ cm}}\\)", f"\\({half_l - 1}\\text{{ cm}}\\)"])
        corr_letter = [o["id"] for o in q["options"] if o["isCorrect"]][0]
        q["correctAnswer"] = corr_letter
        q["solution"] = f"**Step 1: Midpoint Definition**\nSince \\(M\\) is the midpoint of \\(AB\\), \\(AM = \\frac{{1}}{{2}} AB\\).\n**Step 2: Calculation**\n\\(AM = \\frac{{{tot_l}}}{{2}} = {half_l}\\text{{ cm}}\\).\n**Step 3: Conclusion**\n\\(AM = {half_l}\\text{{ cm}}\\)."
        q["requiresFigure"] = True
        fig_count += 1

    elif tc == "MH-9-MTH2-1-1.3.2":
        # Opposite rays
        svg = make_opposite_rays_svg("A", "O", "B")
        q["text"] = f'{svg}\nIn the diagram above, what can be stated about ray \\(OA\\) and ray \\(OB\\)?'
        q["options"] = make_unique_opts("They are opposite rays forming a straight line", [
            "They are intersecting rays at 90 degrees",
            "They are coincident rays with same direction",
            "They are parallel non-collinear rays"
        ])
        corr_letter = [o["id"] for o in q["options"] if o["isCorrect"]][0]
        q["correctAnswer"] = corr_letter
        q["solution"] = "**Step 1: Definition of Opposite Rays**\nTwo rays having a common origin and forming a straight line are defined as opposite rays.\n**Step 2: Identification**\nRay \\(OA\\) and Ray \\(OB\\) share origin \\(O\\) and lie on opposite sides of \\(O\\) along line \\(AB\\).\n**Step 3: Conclusion**\nThey are opposite rays forming a straight line."
        q["requiresFigure"] = True
        fig_count += 1

    # Chapter 2 Subtopics (Parallel lines)
    elif tc == "MH-9-MTH2-2-2.1.1":
        # Alternate interior angles
        ang = 50 + (seq * 5 % 65)
        svg = make_parallel_transversal_svg(f"{ang}°", "x", "alternate", "Alternate Interior Angles (l ∥ m)")
        q["text"] = f'{svg}\nIn the figure above, line \\(l \\parallel m\\) and line \\(t\\) is a transversal. What is the value of alternate interior angle \\(x\\)?'
        q["options"] = make_unique_opts(f"\\({ang}^\\circ\\)", [f"\\({180 - ang}^\\circ\\)", f"\\({ang + 15}^\\circ\\)", f"\\({ang - 10}^\\circ\\)"])
        corr_letter = [o["id"] for o in q["options"] if o["isCorrect"]][0]
        q["correctAnswer"] = corr_letter
        q["solution"] = f"**Step 1: Theorem**\nAlternate interior angles formed by parallel lines and a transversal are equal.\n**Step 2: Calculation**\n\\(x = {ang}^\\circ\\).\n**Step 3: Conclusion**\n\\(x = {ang}^\\circ\\)."
        q["requiresFigure"] = True
        fig_count += 1

    elif tc == "MH-9-MTH2-2-2.1.2":
        # Corresponding angles
        ang = 60 + (seq * 7 % 55)
        svg = make_parallel_transversal_svg(f"{ang}°", "y", "corresponding", "Corresponding Angles (l ∥ m)")
        q["text"] = f'{svg}\nRefer to the parallel lines figure above with \\(l \\parallel m\\). Find the measure of corresponding angle \\(y\\).'
        q["options"] = make_unique_opts(f"\\({ang}^\\circ\\)", [f"\\({180 - ang}^\\circ\\)", f"\\({ang + 20}^\\circ\\)", f"\\({ang - 15}^\\circ\\)"])
        corr_letter = [o["id"] for o in q["options"] if o["isCorrect"]][0]
        q["correctAnswer"] = corr_letter
        q["solution"] = f"**Step 1: Axiom**\nCorresponding angles are equal for parallel lines intersected by a transversal.\n**Step 2: Conclusion**\n\\(y = {ang}^\\circ\\)."
        q["requiresFigure"] = True
        fig_count += 1

    elif tc == "MH-9-MTH2-2-2.1.3":
        # Interior angles on same side
        ang1 = 65 + (seq * 5 % 50)
        ang2 = 180 - ang1
        svg = make_parallel_transversal_svg(f"{ang1}°", "z", "interior", "Consecutive Interior Angles (l ∥ m)")
        q["text"] = f'{svg}\nIn the figure above with line \\(l \\parallel m\\), what is the value of interior angle \\(z\\) on the same side of transversal \\(t\\)?'
        q["options"] = make_unique_opts(f"\\({ang2}^\\circ\\)", [f"\\({ang1}^\\circ\\)", f"\\({ang2 + 10}^\\circ\\)", f"\\({ang2 - 15}^\\circ\\)"])
        corr_letter = [o["id"] for o in q["options"] if o["isCorrect"]][0]
        q["correctAnswer"] = corr_letter
        q["solution"] = f"**Step 1: Theorem**\nInterior angles on the same side of a transversal are supplementary (sum = \\(180^\\circ\\)).\n**Step 2: Calculation**\n\\(z = 180^\\circ - {ang1}^\\circ = {ang2}^\\circ\\).\n**Step 3: Conclusion**\n\\(z = {ang2}^\\circ\\)."
        q["requiresFigure"] = True
        fig_count += 1

    elif tc == "MH-9-MTH2-2-2.2.4":
        # Perpendicular to parallel lines
        svg = make_perpendicular_parallel_svg()
        q["text"] = f'{svg}\nIn the figure above, line \\(l \\parallel m\\) and line \\(p \\perp l\\). What is the relation between line \\(p\\) and line \\(m\\)?'
        q["options"] = make_unique_opts("Line p is perpendicular to line m", [
            "Line p is parallel to line m",
            "Line p intersects line m at 45 degrees",
            "Line p does not intersect line m"
        ])
        corr_letter = [o["id"] for o in q["options"] if o["isCorrect"]][0]
        q["correctAnswer"] = corr_letter
        q["solution"] = "**Step 1: Geometric Theorem**\nIf a line is perpendicular to one of two parallel lines, it is also perpendicular to the other parallel line.\n**Step 2: Conclusion**\nLine \\(p \\perp m\\)."
        q["requiresFigure"] = True
        fig_count += 1

    enriched_questions.append(q)

print(f"Total Questions Processed: {len(enriched_questions)}")
print(f"Total Questions with Figures in Ch 1 & 2: {fig_count} ({fig_count / len(enriched_questions) * 100:.1f}%)")

output_path = "scripts/mh9_mth2_ch1_ch2_figures_generated.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(enriched_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
