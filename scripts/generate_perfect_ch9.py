# scripts/generate_perfect_ch9.py
# High-entropy, 100% distinct question generator for Chapter 9 (Surface Area and Volume)
# 9 subtopics * 80 questions = 720 questions.
# Meets Rule 2T (80Q pack: 40 Exam, 20 Practice, 20 Foundation)
# Passes validateBatchDistinctness with 0 duplicate pairs.

import json
import math

def make_opts(corr_text, distractors):
    dist_set = []
    for d in distractors:
        sd = str(d).strip()
        sc = str(corr_text).strip()
        if sd != sc and sd not in dist_set:
            dist_set.append(sd)
        if len(dist_set) == 3:
            break
    while len(dist_set) < 3:
        cand = f"{corr_text} + {len(dist_set) + 1}"
        if cand not in dist_set:
            dist_set.append(cand)

    all_four = [str(corr_text).strip()] + dist_set[:3]
    all_four.sort(key=lambda s: (len(s), s))

    letters = ['A', 'B', 'C', 'D']
    options = []
    for idx, opt_text in enumerate(all_four):
        options.append({
            "id": letters[idx],
            "text": opt_text,
            "isCorrect": (opt_text == str(corr_text).strip())
        })
    return options

def svg_cone(r_str, h_str, l_str, title="Right Circular Cone"):
    return f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 340 180" style="max-width: 340px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="170" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>
  <line x1="170" y1="35" x2="105" y2="140" stroke="#38bdf8" stroke-width="2.2"/>
  <line x1="170" y1="35" x2="235" y2="140" stroke="#38bdf8" stroke-width="2.2"/>
  <ellipse cx="170" cy="140" rx="65" ry="18" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <line x1="170" y1="35" x2="170" y2="140" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="3,3"/>
  <line x1="170" y1="140" x2="235" y2="140" stroke="#f8fafc" stroke-width="2"/>
  <circle cx="170" cy="140" r="3.5" fill="#f59e0b"/>
  <circle cx="170" cy="35" r="3.5" fill="#f8fafc"/>
  <text x="178" y="90" fill="#f59e0b" font-size="11" font-weight="600" font-family="sans-serif">{h_str}</text>
  <text x="202" y="156" fill="#f8fafc" font-size="11" font-weight="600" font-family="sans-serif">{r_str}</text>
  <text x="215" y="80" fill="#38bdf8" font-size="11" font-weight="600" font-family="sans-serif">{l_str}</text>
</svg>
</div>"""

def svg_sphere(r_str, title="Solid Sphere"):
    return f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 340 180" style="max-width: 340px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="170" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>
  <circle cx="170" cy="100" r="60" fill="#1e293b" stroke="#38bdf8" stroke-width="2.2"/>
  <ellipse cx="170" cy="100" rx="60" ry="16" fill="none" stroke="#64748b" stroke-width="1.2" stroke-dasharray="4,4"/>
  <line x1="170" y1="100" x2="230" y2="100" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="170" cy="100" r="3.5" fill="#f59e0b"/>
  <circle cx="230" cy="100" r="3" fill="#38bdf8"/>
  <text x="200" y="92" fill="#f59e0b" font-size="11" font-weight="600" font-family="sans-serif">{r_str}</text>
</svg>
</div>"""

def svg_hemi(r_str, title="Solid Hemisphere"):
    return f"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 340 180" style="max-width: 340px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="170" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>
  <ellipse cx="170" cy="80" rx="65" ry="18" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <path d="M 105 80 A 65 65 0 0 0 235 80 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <line x1="170" y1="80" x2="235" y2="80" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="170" cy="80" r="3.5" fill="#f59e0b"/>
  <text x="202" y="72" fill="#f59e0b" font-size="11" font-weight="600" font-family="sans-serif">{r_str}</text>
</svg>
</div>"""

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
        "chapterNumber": 9,
        "chapter": "Surface Area and Volume",
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

TRIPLETS_80 = []
base_triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (9, 40, 41), (12, 35, 37), (20, 21, 29), (11, 60, 61)]
for mult in range(1, 15):
    for r0, h0, l0 in base_triples:
        TRIPLETS_80.append((r0 * mult, h0 * mult, l0 * mult))
        if len(TRIPLETS_80) >= 80:
            break
    if len(TRIPLETS_80) >= 80:
        break

OBJECTS_80 = [
    ("party conical hat", "party hat"), ("circus marquee tent", "tent"), ("grain storage funnel", "funnel"),
    ("traffic safety cone", "cone"), ("conical church steeple", "steeple"), ("spinning top toy", "toy"),
    ("conical water reservoir", "reservoir"), ("ice cream wafer cone", "wafer cone"), ("decorative paper lantern", "lantern"),
    ("sand pile conical heap", "sand heap"), ("laboratory conical filter", "filter"), ("metal conical hopper", "hopper"),
    ("conical loudspeaker horn", "horn"), ("wooden plumb bob", "plumb bob"), ("conical volcanic peak model", "volcano model"),
    ("conical drilling head", "drill head"), ("decorative table lampshade", "lampshade"), ("conical exhaust hood", "exhaust hood"),
    ("pastry chef icing cone", "icing cone"), ("miniature glass cone", "glass cone"),
    ("grain silo hopper", "hopper"), ("conical chemical retort", "retort"), ("radar antenna reflector", "reflector"),
    ("oil transfer funnel", "funnel"), ("conical roof turret", "turret"), ("campers teepee shelter", "teepee"),
    ("highway delineation cone", "pylon"), ("conical buoy marker", "buoy"), ("decorative pinecone ornament", "ornament"),
    ("conical glass flask", "flask"), ("conical speaker diaphragm", "diaphragm"), ("brass plumb line weight", "plumb bob"),
    ("conical grain collector", "collector"), ("sugar loaf cone", "sugar cone"), ("conical acoustic dampener", "dampener"),
    ("conical drill tip", "drill bit"), ("conical spinning bobbin", "bobbin"), ("rotary cyclone separator", "cyclone"),
    ("conical oil dispenser", "dispenser"), ("conical ceramic pot", "pot"),
    ("canvas canopy cone", "canopy"), ("conical cement silo", "silo"), ("conical wine strainer", "strainer"),
    ("conical copper kettle lid", "lid"), ("conical party noisemaker", "noisemaker"), ("conical steel rivet head", "rivet head"),
    ("conical fountain nozzle", "nozzle"), ("aerodynamic missile nosecone", "nosecone"), ("conical feed dispenser", "feed bin"),
    ("conical measuring cup", "measuring cup"), ("conical seed planter", "planter"), ("conical acoustic horn", "horn"),
    ("conical exhaust diffuser", "diffuser"), ("conical spotlight casing", "spotlight"), ("conical chimney cap", "chimney cap"),
    ("conical water filter cartridge", "filter"), ("conical bronze bell core", "bell core"), ("conical centrifuge tube", "tube"),
    ("conical rocket exhaust nozzle", "nozzle"), ("conical spice container", "spice container"),
    ("conical lamp diffuser", "diffuser"), ("conical satellite antenna", "antenna"), ("conical tea infuser", "infuser"),
    ("conical surveyor marker", "marker"), ("conical pendulum bob", "pendulum"), ("conical oil filter element", "filter"),
    ("conical water dropper", "dropper"), ("conical mortar pestle tip", "pestle"), ("conical blast nozzle", "nozzle"),
    ("conical air intake cowl", "cowl"), ("conical grain scoop", "scoop"), ("conical concrete hopper", "hopper"),
    ("conical steel cone anchor", "anchor"), ("conical flour sifter", "sifter"), ("conical laser lens hood", "lens hood"),
    ("conical copper still head", "still head"), ("conical brewing funnel", "funnel"), ("conical smoke baffle", "baffle"),
    ("conical sandglass funnel", "funnel"), ("conical paper coffee dripper", "dripper")
]

SEQS_80 = [101 + i for i in range(40)] + [201 + i for i in range(20)] + [301 + i for i in range(20)]

def generate_9_1_1():
    # Slant height l = √(r² + h²)
    tc = "MH-9-MTH2-9-9.1.1"
    tname = "Slant height l = √(r² + h²)"
    qs = []
    for idx, seq in enumerate(SEQS_80):
        r, h, l = TRIPLETS_80[idx]
        obj_name, obj_short = OBJECTS_80[idx]
        has_fig = (idx % 5 != 0)
        svg = svg_cone(f"r = {r} cm", f"h = {h} cm", f"l = {l} cm", f"{obj_name.title()} #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        if archetype == 0:
            txt = prefix + f"A {obj_name} has a base radius of \\(r = {r}\\text{{ cm}}\\) and vertical height \\(h = {h}\\text{{ cm}}\\). Calculate its slant height \\(l\\)."
            corr = f"\\({l}\\text{{ cm}}\\)"
            dist = [f"\\({h + 2}\\text{{ cm}}\\)", f"\\({r + h}\\text{{ cm}}\\)", f"\\({l + 4}\\text{{ cm}}\\)", f"\\({l - 2}\\text{{ cm}}\\)" if l > 2 else f"\\({l + 3}\\text{{ cm}}\\)"]
            sol = f"**Step 1: Formula**\n\\(l = \\sqrt{{r^2 + h^2}} = \\sqrt{{{r}^2 + {h}^2}} = \\sqrt{{{r*r} + {h*h}}} = \\sqrt{{{l*l}}} = {l}\\text{{ cm}}\\).\n**Step 2: Conclusion**\nSlant height \\(l = {l}\\text{{ cm}}\\)."
        elif archetype == 1:
            txt = prefix + f"For the {obj_name} depicted above with vertical height \\(h = {h}\\text{{ cm}}\\) and slant height \\(l = {l}\\text{{ cm}}\\), what is its base radius \\(r\\)?"
            corr = f"\\({r}\\text{{ cm}}\\)"
            dist = [f"\\({l - h}\\text{{ cm}}\\)", f"\\({r + 3}\\text{{ cm}}\\)", f"\\({(r + 2)}\\text{{ cm}}\\)", f"\\({l + 1}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Formula**\n\\(r = \\sqrt{{l^2 - h^2}} = \\sqrt{{{l}^2 - {h}^2}} = \\sqrt{{{l*l - h*h}}} = {r}\\text{{ cm}}\\).\n**Step 2: Conclusion**\nRadius \\(r = {r}\\text{{ cm}}\\)."
        elif archetype == 2:
            txt = prefix + f"A craftsman manufactures a {obj_name} with base radius \\({r}\\text{{ cm}}\\) and slant height \\({l}\\text{{ cm}}\\). Determine its perpendicular vertical height \\(h\\)."
            corr = f"\\({h}\\text{{ cm}}\\)"
            dist = [f"\\({l - r}\\text{{ cm}}\\)", f"\\({h + 2}\\text{{ cm}}\\)", f"\\({h - 2}\\text{{ cm}}\\)" if h > 2 else f"\\({h + 5}\\text{{ cm}}\\)", f"\\({l + r}\\text{{ cm}}\\)"]
            sol = f"**Step 1: Formula**\n\\(h = \\sqrt{{l^2 - r^2}} = \\sqrt{{{l*l} - {r*r}}} = \\sqrt{{{h*h}}} = {h}\\text{{ cm}}\\).\n**Step 2: Conclusion**\nVertical height \\(h = {h}\\text{{ cm}}\\)."
        elif archetype == 3:
            txt = prefix + f"In the geometry of a right circular {obj_short}, the radius is \\({r}\\text{{ m}}\\) and the vertical altitude is \\({h}\\text{{ m}}\\). Find the length of the generator (slant height) in meters."
            corr = f"\\({l}\\text{{ m}}\\)"
            dist = [f"\\({l + 1}\\text{{ m}}\\)", f"\\({h + r}\\text{{ m}}\\)", f"\\({l - 1}\\text{{ m}}\\)", f"\\({l + 5}\\text{{ m}}\\)" ]
            sol = f"**Step 1: Slant Height Relation**\n\\(l = \\sqrt{{{r}^2 + {h}^2}} = \\sqrt{{{r*r + h*h}}} = {l}\\text{{ m}}\\).\n**Step 2: Conclusion**\nSlant height is \\({l}\\text{{ m}}\\)."
        elif archetype == 4:
            txt = prefix + f"A civil engineer inspects a {obj_name}. If the base diameter is \\({2 * r}\\text{{ cm}}\\) and the altitude is \\({h}\\text{{ cm}}\\), what is its slant height?"
            corr = f"\\({l}\\text{{ cm}}\\)"
            dist = [f"\\({2 * l}\\text{{ cm}}\\)", f"\\({l + 2}\\text{{ cm}}\\)", f"\\({2 * r + h}\\text{{ cm}}\\)", f"\\({l - 3}\\text{{ cm}}\\)"]
            sol = f"**Step 1: Radius Calculation**\nRadius \\(r = \\frac{{{2 * r}}}{{2}} = {r}\\text{{ cm}}\\).\n**Step 2: Slant Height**\n\\(l = \\sqrt{{{r}^2 + {h}^2}} = \\sqrt{{{r*r + h*h}}} = {l}\\text{{ cm}}\\).\n**Step 3: Conclusion**\n\\({l}\\text{{ cm}}\\)."
        elif archetype == 5:
            txt = prefix + f"If the slant height of a {obj_name} is \\({l}\\text{{ cm}}\\) and its base diameter is \\({2 * r}\\text{{ cm}}\\), find its perpendicular vertical height."
            corr = f"\\({h}\\text{{ cm}}\\)"
            dist = [f"\\({h + 3}\\text{{ cm}}\\)", f"\\({l - r}\\text{{ cm}}\\)", f"\\({h - 1}\\text{{ cm}}\\)", f"\\({2 * h}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Radius**\n\\(r = \\frac{{{2*r}}}{{2}} = {r}\\text{{ cm}}\\).\n**Step 2: Vertical Height**\n\\(h = \\sqrt{{l^2 - r^2}} = \\sqrt{{{l*l - r*r}}} = {h}\\text{{ cm}}\\).\n**Step 3: Conclusion**\n\\({h}\\text{{ cm}}\\)."
        elif archetype == 6:
            txt = prefix + f"Verify the Pythagorean relation for a {obj_short} having radius \\(r = {r}\\text{{ cm}}\\) and height \\(h = {h}\\text{{ cm}}\\). What is the value of \\(l^2\\)?"
            l2 = l * l
            corr = f"\\({l2}\\text{{ cm}}^2\\)"
            dist = [f"\\({l2 + 10}\\text{{ cm}}^2\\)", f"\\({(r + h)**2}\\text{{ cm}}^2\\)", f"\\({l2 - 15}\\text{{ cm}}^2\\)", f"\\({2 * l2}\\text{{ cm}}^2\\)" ]
            sol = f"**Step 1: Calculation**\n\\(l^2 = r^2 + h^2 = {r}^2 + {h}^2 = {r*r} + {h*h} = {l2}\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\(l^2 = {l2}\\text{{ cm}}^2\\)."
        else:
            txt = prefix + f"A party decorator prepares a {obj_name} where \\(h = {h}\\text{{ cm}}\\) and \\(l = {l}\\text{{ cm}}\\). What is the diameter of its circular base?"
            d_val = 2 * r
            corr = f"\\({d_val}\\text{{ cm}}\\)"
            dist = [f"\\({r}\\text{{ cm}}\\)", f"\\({d_val + 2}\\text{{ cm}}\\)", f"\\({l + h}\\text{{ cm}}\\)", f"\\({d_val - 2}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Radius**\n\\(r = \\sqrt{{l^2 - h^2}} = \\sqrt{{{l*l - h*h}}} = {r}\\text{{ cm}}\\).\n**Step 2: Diameter**\nDiameter \\(= 2r = 2 \\times {r} = {d_val}\\text{{ cm}}\\).\n**Step 3: Conclusion**\n\\({d_val}\\text{{ cm}}\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def generate_9_1_2():
    # Curved Surface Area = πrl
    tc = "MH-9-MTH2-9-9.1.2"
    tname = "Curved Surface Area = πrl"
    qs = []
    for idx, seq in enumerate(SEQS_80):
        r, h, l = TRIPLETS_80[idx]
        obj_name, obj_short = OBJECTS_80[idx]
        csa_val = r * l
        has_fig = (idx % 5 != 0)
        svg = svg_cone(f"r = {r} cm", f"h = {h} cm", f"l = {l} cm", f"{obj_name.title()} CSA #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        if archetype == 0:
            txt = prefix + f"Determine the curved surface area of a {obj_name} with base radius \\(r = {r}\\text{{ cm}}\\) and slant height \\(l = {l}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
            corr = f"\\({csa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({csa_val * 2}\\pi\\text{{ cm}}^2\\)", f"\\({(r * h)}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val + 10}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val - 8}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Formula**\n\\(\\text{{CSA}} = \\pi r l = \\pi \\times {r} \\times {l} = {csa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\nCurved surface area is \\({csa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 1:
            txt = prefix + f"A craftsman requires canvas to cover the lateral surface of a {obj_name}. If \\(r = {r}\\text{{ m}}\\) and vertical height \\(h = {h}\\text{{ m}}\\), find the canvas area needed in terms of \\(\\pi\\)."
            corr = f"\\({csa_val}\\pi\\text{{ m}}^2\\)"
            dist = [f"\\({r * h}\\pi\\text{{ m}}^2\\)", f"\\({csa_val + 12}\\pi\\text{{ m}}^2\\)", f"\\({2 * csa_val}\\pi\\text{{ m}}^2\\)", f"\\({csa_val - 15}\\pi\\text{{ m}}^2\\)"]
            sol = f"**Step 1: Slant Height**\n\\(l = \\sqrt{{{r}^2 + {h}^2}} = {l}\\text{{ m}}\\).\n**Step 2: Lateral Area**\n\\(\\text{{CSA}} = \\pi r l = \\pi \\times {r} \\times {l} = {csa_val}\\pi\\text{{ m}}^2\\).\n**Step 3: Conclusion**\n\\({csa_val}\\pi\\text{{ m}}^2\\)."
        elif archetype == 2:
            txt = prefix + f"The curved surface area of a {obj_name} is \\({csa_val}\\pi\\text{{ cm}}^2\\). If its slant height is \\({l}\\text{{ cm}}\\), what is its base radius?"
            corr = f"\\({r}\\text{{ cm}}\\)"
            dist = [f"\\({r + 2}\\text{{ cm}}\\)", f"\\({l - r}\\text{{ cm}}\\)", f"\\({r - 1}\\text{{ cm}}\\)" if r > 1 else f"\\({r + 4}\\text{{ cm}}\\)", f"\\({2 * r}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Inverse Calculation**\n\\(\\text{{CSA}} = \\pi r l \\implies {csa_val}\\pi = \\pi \\times r \\times {l}\\).\n\\(r = \\frac{{{csa_val}}}{{{l}}} = {r}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\(r = {r}\\text{{ cm}}\\)."
        elif archetype == 3:
            txt = prefix + f"The lateral surface area of a {obj_short} is \\({csa_val}\\pi\\text{{ cm}}^2\\) and its base radius is \\({r}\\text{{ cm}}\\). Calculate its slant height."
            corr = f"\\({l}\\text{{ cm}}\\)"
            dist = [f"\\({l + 3}\\text{{ cm}}\\)", f"\\({l - 2}\\text{{ cm}}\\)", f"\\({h}\\text{{ cm}}\\)", f"\\({l * 2}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Formula**\n\\(l = \\frac{{\\text{{CSA}}}}{{\\pi r}} = \\frac{{{csa_val}\\pi}}{{\\pi \\times {r}}} = {l}\\text{{ cm}}\\).\n**Step 2: Conclusion**\nSlant height is \\({l}\\text{{ cm}}\\)."
        elif archetype == 4:
            rate = 5 + (idx % 12) * 2
            total_cost = csa_val * rate
            txt = prefix + f"A painter coats the outside curved surface of a {obj_name} with \\(r = {r}\\text{{ m}}\\) and \\(l = {l}\\text{{ m}}\\). At ₹{rate} per \\(\\pi\\text{{ m}}^2\\), find the total painting cost."
            corr = f"₹{total_cost}"
            dist = [f"₹{total_cost + 50}", f"₹{total_cost - 40}", f"₹{total_cost * 2}", f"₹{total_cost + 100}"]
            sol = f"**Step 1: CSA**\n\\(\\text{{CSA}} = \\pi r l = {csa_val}\\pi\\text{{ m}}^2\\).\n**Step 2: Cost Calculation**\n\\(\\text{{Cost}} = {csa_val} \\times {rate} = ₹{total_cost}\\).\n**Step 3: Conclusion**\nTotal cost is ₹{total_cost}."
        elif archetype == 5:
            txt = prefix + f"What is the curved surface area of a right circular {obj_short} having base diameter \\({2 * r}\\text{{ cm}}\\) and slant height \\({l}\\text{{ cm}}\\)?"
            corr = f"\\({csa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({2 * csa_val}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val // 2}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val + 20}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val - 10}\\pi\\text{{ cm}}^2\\)" ]
            sol = f"**Step 1: Radius**\n\\(r = \\frac{{{2 * r}}}{{2}} = {r}\\text{{ cm}}\\).\n**Step 2: CSA**\n\\(\\text{{CSA}} = \\pi r l = \\pi \\times {r} \\times {l} = {csa_val}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\n\\({csa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 6:
            txt = prefix + f"If the base radius of a {obj_name} is \\({r}\\text{{ cm}}\\) and its vertical height is \\({h}\\text{{ cm}}\\), what is its curved surface area in terms of \\(\\pi\\)?"
            corr = f"\\({csa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({r * h}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val + 15}\\pi\\text{{ cm}}^2\\)", f"\\({2 * csa_val}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val - 12}\\pi\\text{{ cm}}^2\\)" ]
            sol = f"**Step 1: Slant Height**\n\\(l = \\sqrt{{{r}^2 + {h}^2}} = {l}\\text{{ cm}}\\).\n**Step 2: CSA**\n\\(\\text{{CSA}} = \\pi r l = {csa_val}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\n\\({csa_val}\\pi\\text{{ cm}}^2\\)."
        else:
            material = ["metal sheet", "copper foil", "tin sheet", "plastic wrap", "fabric lining", "cardboard cover", "canvas cloth", "tarpaulin cover"][idx % 8]
            txt = prefix + f"A roll of {material} is shaped into an open {obj_name} of radius \\({r}\\text{{ cm}}\\) and slant height \\({l}\\text{{ cm}}\\). What surface area of material was consumed (ignoring base)?"
            corr = f"\\({csa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({(r + l)**2}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val + 25}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val * 3}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val - 18}\\pi\\text{{ cm}}^2\\)" ]
            sol = f"**Step 1: Concept**\nOpen cone lateral area equals \\(\\pi r l\\).\n**Step 2: Calculation**\n\\(\\text{{Area}} = \\pi \\times {r} \\times {l} = {csa_val}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\n\\({csa_val}\\pi\\text{{ cm}}^2\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def generate_9_1_3():
    # Total Surface Area = πr(r + l)
    tc = "MH-9-MTH2-9-9.1.3"
    tname = "Total Surface Area = πr(r + l)"
    qs = []
    for idx, seq in enumerate(SEQS_80):
        r, h, l = TRIPLETS_80[idx]
        obj_name, obj_short = OBJECTS_80[idx]
        tsa_val = r * (r + l)
        has_fig = (idx % 5 != 0)
        svg = svg_cone(f"r = {r} cm", f"h = {h} cm", f"l = {l} cm", f"{obj_name.title()} TSA #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        if archetype == 0:
            txt = prefix + f"Find the total surface area of a solid {obj_name} with base radius \\(r = {r}\\text{{ cm}}\\) and slant height \\(l = {l}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
            corr = f"\\({tsa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({r * l}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val + 20}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val * 2}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val - 14}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Formula**\n\\(\\text{{TSA}} = \\pi r(r + l) = \\pi \\times {r} \\times ({r} + {l}) = \\pi \\times {r} \\times {r + l} = {tsa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({tsa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 1:
            txt = prefix + f"A closed {obj_name} has radius \\(r = {r}\\text{{ m}}\\) and height \\(h = {h}\\text{{ m}}\\). Determine the total surface area to be painted in terms of \\(\\pi\\)."
            corr = f"\\({tsa_val}\\pi\\text{{ m}}^2\\)"
            dist = [f"\\({r * l}\\pi\\text{{ m}}^2\\)", f"\\({tsa_val + 16}\\pi\\text{{ m}}^2\\)", f"\\({tsa_val - 12}\\pi\\text{{ m}}^2\\)", f"\\({2 * tsa_val}\\pi\\text{{ m}}^2\\)" ]
            sol = f"**Step 1: Slant Height**\n\\(l = \\sqrt{{{r}^2 + {h}^2}} = {l}\\text{{ m}}\\).\n**Step 2: TSA**\n\\(\\text{{TSA}} = \\pi r(r + l) = \\pi \\times {r} \\times ({r} + {l}) = {tsa_val}\\pi\\text{{ m}}^2\\).\n**Step 3: Conclusion**\n\\({tsa_val}\\pi\\text{{ m}}^2\\)."
        elif archetype == 2:
            base_area = r * r
            csa_val = r * l
            txt = prefix + f"For a solid {obj_short}, the base area is \\({base_area}\\pi\\text{{ cm}}^2\\) and the curved surface area is \\({csa_val}\\pi\\text{{ cm}}^2\\). Calculate its total surface area."
            corr = f"\\({tsa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({csa_val}\\pi\\text{{ cm}}^2\\)", f"\\({base_area}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val + 10}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val * 2}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Concept**\n\\(\\text{{TSA}} = \\text{{Base Area}} + \\text{{CSA}} = {base_area}\\pi + {csa_val}\\pi = {tsa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({tsa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 3:
            txt = prefix + f"The total surface area of a solid right circular {obj_short} is \\({tsa_val}\\pi\\text{{ cm}}^2\\). If its base radius is \\({r}\\text{{ cm}}\\), what is its slant height?"
            corr = f"\\({l}\\text{{ cm}}\\)"
            dist = [f"\\({l + 2}\\text{{ cm}}\\)", f"\\({l - 2}\\text{{ cm}}\\)", f"\\({h}\\text{{ cm}}\\)", f"\\({r + 1}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Formula**\n\\(\\pi r(r + l) = {tsa_val}\\pi \\implies {r}({r} + l) = {tsa_val}\\).\n\\({r} + l = \\frac{{{tsa_val}}}{{{r}}} = {r + l} \\implies l = {l}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\({l}\\text{{ cm}}\\)."
        elif archetype == 4:
            txt = prefix + f"A solid wooden {obj_name} has diameter \\({2 * r}\\text{{ cm}}\\) and slant height \\({l}\\text{{ cm}}\\). What is its total surface area in terms of \\(\\pi\\)?"
            corr = f"\\({tsa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({2 * tsa_val}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val + 25}\\pi\\text{{ cm}}^2\\)", f"\\({r * l}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val - 18}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Radius**\n\\(r = \\frac{{{2 * r}}}{{2}} = {r}\\text{{ cm}}\\).\n**Step 2: TSA**\n\\(\\text{{TSA}} = \\pi r(r + l) = \\pi \\times {r} \\times ({r + l}) = {tsa_val}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\n\\({tsa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 5:
            diff_area = tsa_val - (r * l)
            txt = prefix + f"What is the difference between the total surface area and curved surface area of a solid {obj_short} of radius \\(r = {r}\\text{{ cm}}\\) and slant height \\(l = {l}\\text{{ cm}}\\)?"
            corr = f"\\({diff_area}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({2 * diff_area}\\pi\\text{{ cm}}^2\\)", f"\\({r}\\pi\\text{{ cm}}^2\\)", f"\\({diff_area + 5}\\pi\\text{{ cm}}^2\\)", f"\\({l * r}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Concept**\n\\(\\text{{TSA}} - \\text{{CSA}} = \\text{{Base Area}} = \\pi r^2 = \\pi \\times {r}^2 = {diff_area}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({diff_area}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 6:
            cost_rate = 3 + (idx % 10) * 2
            total_cost = tsa_val * cost_rate
            txt = prefix + f"Polishing a solid metallic {obj_name} of radius \\({r}\\text{{ cm}}\\) and slant height \\({l}\\text{{ cm}}\\) costs ₹{cost_rate} per \\(\\pi\\text{{ cm}}^2\\). Calculate the total polishing cost."
            corr = f"₹{total_cost}"
            dist = [f"₹{total_cost + 30}", f"₹{total_cost - 25}", f"₹{total_cost * 2}", f"₹{total_cost + 60}"]
            sol = f"**Step 1: Total Surface Area**\n\\(\\text{{TSA}} = \\pi r(r + l) = {tsa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Cost**\n\\(\\text{{Cost}} = {tsa_val} \\times {cost_rate} = ₹{total_cost}\\).\n**Step 3: Conclusion**\n₹{total_cost}."
        else:
            finish_type = ["electroplated", "powder coated", "lacquered", "enameled", "anodized", "ceramic coated", "varnished", "wax polished"][idx % 8]
            txt = prefix + f"A solid decorative {obj_name} is assembled with radius \\({r}\\text{{ cm}}\\) and altitude \\({h}\\text{{ cm}}\\). What total surface area must be {finish_type} in terms of \\(\\pi\\)?"
            corr = f"\\({tsa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({tsa_val + 35}\\pi\\text{{ cm}}^2\\)", f"\\({(r*h)}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val - 20}\\pi\\text{{ cm}}^2\\)", f"\\({2 * tsa_val}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Slant Height**\n\\(l = \\sqrt{{{r}^2 + {h}^2}} = {l}\\text{{ cm}}\\).\n**Step 2: TSA**\n\\(\\text{{TSA}} = \\pi r(r + l) = {tsa_val}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\n\\({tsa_val}\\pi\\text{{ cm}}^2\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def generate_9_1_4():
    # Volume = 1/3 * πr²h
    tc = "MH-9-MTH2-9-9.1.4"
    tname = "Volume = 1/3 * πr²h"
    qs = []
    ratio_pairs = [
        ((1, 2), (2, 1), "1:2"), ((2, 3), (3, 2), "2:3"), ((3, 4), (4, 3), "3:4"),
        ((1, 3), (3, 1), "1:3"), ((2, 1), (1, 2), "2:1"), ((3, 2), (2, 3), "3:2"),
        ((4, 3), (3, 4), "4:3"), ((3, 1), (1, 3), "3:1"), ((1, 4), (4, 1), "1:4"),
        ((4, 1), (1, 4), "4:1")
    ]
    for idx, seq in enumerate(SEQS_80):
        r_orig, h_orig, l_orig = TRIPLETS_80[idx]
        h = h_orig if (r_orig * r_orig * h_orig) % 3 == 0 else (h_orig * 3)
        r = r_orig
        vol_val = (r * r * h) // 3
        obj_name, obj_short = OBJECTS_80[idx]
        has_fig = (idx % 5 != 0)
        svg = svg_cone(f"r = {r} cm", f"h = {h} cm", f"Volume #{seq}", f"{obj_name.title()} Vol") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        if archetype == 0:
            txt = prefix + f"Determine the volume of a right circular {obj_name} having radius \\(r = {r}\\text{{ cm}}\\) and vertical height \\(h = {h}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({vol_val * 3}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 24}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val // 2}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 18}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Formula**\n\\(V = \\frac{{1}}{{3}}\\pi r^2 h = \\frac{{1}}{{3}}\\pi \\times {r}^2 \\times {h} = \\frac{{1}}{{3}}\\pi \\times {r*r} \\times {h} = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\nVolume is \\({vol_val}\\pi\\text{{ cm}}^3\\)."
        elif archetype == 1:
            txt = prefix + f"A storage container shaped like a {obj_name} has base diameter \\({2 * r}\\text{{ cm}}\\) and depth \\({h}\\text{{ cm}}\\). What is its maximum holding capacity in terms of \\(\\pi\\)?"
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({4 * vol_val}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 15}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val * 3}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 10}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Radius**\n\\(r = \\frac{{{2 * r}}}{{2}} = {r}\\text{{ cm}}\\).\n**Step 2: Volume**\n\\(V = \\frac{{1}}{{3}}\\pi r^2 h = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 3: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."
        elif archetype == 2:
            txt = prefix + f"The volume of a {obj_short} is \\({vol_val}\\pi\\text{{ cm}}^3\\) and its base radius is \\({r}\\text{{ cm}}\\). Calculate its perpendicular vertical height."
            corr = f"\\({h}\\text{{ cm}}\\)"
            dist = [f"\\({h + 3}\\text{{ cm}}\\)", f"\\({h - 2}\\text{{ cm}}\\)", f"\\({2 * h}\\text{{ cm}}\\)", f"\\({h // 2}\\text{{ cm}}\\)"]
            sol = f"**Step 1: Height Formula**\n\\(h = \\frac{{3V}}{{\\pi r^2}} = \\frac{{3 \\times {vol_val}\\pi}}{{\\pi \\times {r*r}}} = {h}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\(h = {h}\\text{{ cm}}\\)."
        elif archetype == 3:
            txt = prefix + f"A {obj_short} has volume \\({vol_val}\\pi\\text{{ cm}}^3\\) and altitude \\({h}\\text{{ cm}}\\). Find the radius of its circular base."
            corr = f"\\({r}\\text{{ cm}}\\)"
            dist = [f"\\({r + 2}\\text{{ cm}}\\)", f"\\({r - 1}\\text{{ cm}}\\)", f"\\({2 * r}\\text{{ cm}}\\)", f"\\({r + 4}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Radius Formula**\n\\(r^2 = \\frac{{3V}}{{\\pi h}} = \\frac{{3 \\times {vol_val}\\pi}}{{\\pi \\times {h}}} = {r*r}\\implies r = {r}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\(r = {r}\\text{{ cm}}\\)."
        elif archetype == 4:
            pair_idx = (idx // 8) % len(ratio_pairs)
            (r1, r2), (h1, h2), ans_str = ratio_pairs[pair_idx]
            txt = prefix + f"Two conical funnels have their base radii in the ratio \\({r1}:{r2}\\) and their vertical heights in the ratio \\({h1}:{h2}\\). What is the ratio of their volumes?"
            corr = f"\\({ans_str}\\)"
            dist = ["\\(1:4\\)" if ans_str != "1:4" else "\\(2:5\\)", "\\(3:5\\)", "\\(1:1\\)", "\\(4:9\\)"]
            sol = f"**Step 1: Ratio**\n\\(\\frac{{V_1}}{{V_2}} = \\frac{{\\frac{{1}}{{3}}\\pi r_1^2 h_1}}{{\\frac{{1}}{{3}}\\pi r_2^2 h_2}} = \\left(\\frac{{{r1}}}{{{r2}}}\\right)^2 \\times \\frac{{{h1}}}{{{h2}}} = \\frac{{{r1*r1*h1}}}{{{r2*r2*h2}}} = {ans_str}\\).\n**Step 2: Conclusion**\n\\({ans_str}\\)."
        elif archetype == 5:
            base_area = r * r
            txt = prefix + f"For a {obj_short}, the area of the circular base is \\({base_area}\\pi\\text{{ cm}}^2\\) and the vertical height is \\({h}\\text{{ cm}}\\). Find its volume in terms of \\(\\pi\\)."
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({base_area * h}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 30}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val * 2}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 20}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Formula**\n\\(V = \\frac{{1}}{{3}} \\times \\text{{Base Area}} \\times h = \\frac{{1}}{{3}} \\times {base_area}\\pi \\times {h} = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."
        elif archetype == 6:
            txt = prefix + f"A heap of grain forms a {obj_name} with radius \\({r}\\text{{ m}}\\) and height \\({h}\\text{{ m}}\\). If 1 cubic meter of grain weighs 0.8 tonnes, what is the exact volume in terms of \\(\\pi\\)?"
            corr = f"\\({vol_val}\\pi\\text{{ m}}^3\\)"
            dist = [f"\\({vol_val * 3}\\pi\\text{{ m}}^3\\)", f"\\({vol_val + 12}\\pi\\text{{ m}}^3\\)", f"\\({vol_val - 8}\\pi\\text{{ m}}^3\\)", f"\\({2 * vol_val}\\pi\\text{{ m}}^3\\)"]
            sol = f"**Step 1: Volume Calculation**\n\\(V = \\frac{{1}}{{3}}\\pi r^2 h = \\frac{{1}}{{3}}\\pi \\times {r}^2 \\times {h} = {vol_val}\\pi\\text{{ m}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ m}}^3\\)."
        else:
            txt = prefix + f"A molten metal cylinder of base radius \\({r}\\text{{ cm}}\\) and height \\({h}\\text{{ cm}}\\) is recast into 3 identical {obj_short}s of the same radius. What is the volume of each cone in terms of \\(\\pi\\)?"
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({vol_val * 3}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val // 3}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 18}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 15}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Cylinder Volume**\n\\(V_{{\\text{{cyl}}}} = \\pi r^2 h = {3 * vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Cone Volume**\n\\(V_{{\\text{{cone}}}} = \\frac{{V_{{\\text{{cyl}}}}}}{{3}} = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 3: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

RADII_80 = [i + 1 for i in range(80)]

SPHERE_OBJECTS_80 = [
    ("cricket leather ball", "ball"), ("solid steel bearing sphere", "bearing"), ("crystal glass globe", "globe"),
    ("metallic cannonball", "cannonball"), ("decorative spherical bauble", "bauble"), ("rubber bouncy ball", "ball"),
    ("solid copper spherical pellet", "pellet"), ("spherical water droplet", "droplet"), ("spherical astronomical planetarium model", "planet model"),
    ("spherical soap bubble", "bubble"), ("spherical lead shot", "lead shot"), ("marble spherical toy", "marble"),
    ("spherical bronze statue head", "bronze sphere"), ("spherical helium balloon", "balloon"), ("spherical float valve", "float"),
    ("spherical gas storage tank", "storage tank"), ("spherical bowling ball", "bowling ball"), ("spherical billiard cue ball", "billiard ball"),
    ("spherical wooden croquet ball", "croquet ball"), ("spherical golf practice ball", "golf ball"),
    ("spherical radar radome", "radome"), ("spherical decorative garden orb", "orb"), ("spherical pearl bead", "pearl"),
    ("spherical brass door knob", "knob"), ("spherical silver pendant", "pendant"), ("spherical table tennis ball", "ping pong ball"),
    ("spherical gold nugget bead", "gold bead"), ("spherical bath bomb", "bath bomb"), ("spherical ceramic grinding ball", "grinding ball"),
    ("spherical tungsten carbide ball", "carbide ball"), ("spherical acrylic lens sphere", "acrylic ball"), ("spherical steel counterweight", "counterweight"),
    ("spherical compass housing", "compass sphere"), ("spherical plasma globe", "plasma ball"), ("spherical gyroscope rotor", "gyro sphere"),
    ("spherical bathysphere diving capsule", "diving sphere"), ("spherical meteoroid specimen", "meteorite"), ("spherical quartz crystal ball", "crystal ball"),
    ("spherical sonar transducer", "sonar sphere"), ("spherical pressure hull", "hull"),
    ("spherical satellite beacon", "satellite"), ("spherical foam training ball", "foam ball"), ("spherical glass marble", "marble"),
    ("spherical cast iron kettlebell", "kettlebell"), ("spherical granite ball", "granite sphere"), ("spherical aluminum float", "float"),
    ("spherical pendulum weight", "pendulum"), ("spherical target buoy", "buoy"), ("spherical camera dome", "camera dome"),
    ("spherical glass paperweight", "paperweight"), ("spherical ballcock float", "float valve"), ("spherical silver chime ball", "chime"),
    ("spherical steel ball valve", "ball valve"), ("spherical lead fishing sinker", "sinker"), ("spherical wooden bead", "wooden bead"),
    ("spherical chocolate truffle", "truffle"), ("spherical plastic ball pit sphere", "pit ball"), ("spherical ceramic kiln ball", "kiln ball"),
    ("spherical brass finial", "finial"), ("spherical lava rock sphere", "lava sphere"),
    ("spherical disco mirror ball", "mirror ball"), ("spherical navigational buoy", "buoy"), ("spherical titanium pressure tank", "tank"),
    ("spherical bronze gong chime", "chime"), ("spherical clay seed ball", "seed ball"), ("spherical glass float", "float"),
    ("spherical copper grounding ball", "ground ball"), ("spherical stone architectural ball", "finial"), ("spherical zinc anode ball", "anode"),
    ("spherical obsidian meditation sphere", "obsidian sphere"), ("spherical cork float", "cork float"), ("spherical iron meteor replica", "replica"),
    ("spherical stainless steel whisk ball", "whisk ball"), ("spherical amber resin bead", "amber bead"), ("spherical ivory game sphere", "game ball"),
    ("spherical crystal gazing ball", "gazing ball"), ("spherical brass navigational globe", "globe"), ("spherical aluminum fishing float", "float"),
    ("spherical decorative silver bauble", "bauble"), ("spherical hollow steel ball", "steel sphere")
]

def generate_9_2_1():
    # Surface Area of Sphere = 4πr²
    tc = "MH-9-MTH2-9-9.2.1"
    tname = "Surface Area of Sphere = 4πr²"
    qs = []
    for idx, seq in enumerate(SEQS_80):
        r = RADII_80[idx]
        obj_name, obj_short = SPHERE_OBJECTS_80[idx]
        sa_val = 4 * r * r
        has_fig = (idx % 5 != 0)
        svg = svg_sphere(f"r = {r} cm", f"{obj_name.title()} #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        if archetype == 0:
            txt = prefix + f"Calculate the total surface area of a {obj_name} having radius \\(r = {r}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
            corr = f"\\({sa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({sa_val // 2}\\pi\\text{{ cm}}^2\\)", f"\\({sa_val * 2}\\pi\\text{{ cm}}^2\\)", f"\\({sa_val + 20}\\pi\\text{{ cm}}^2\\)", f"\\({sa_val - 16}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Formula**\n\\(A = 4\\pi r^2 = 4\\pi \\times {r}^2 = 4\\pi \\times {r*r} = {sa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\nSurface area is \\({sa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 1:
            txt = prefix + f"A solid spherical {obj_short} has diameter \\({2 * r}\\text{{ cm}}\\). What is its surface area in terms of \\(\\pi\\)?"
            corr = f"\\({sa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({4 * sa_val}\\pi\\text{{ cm}}^2\\)", f"\\({sa_val // 4}\\pi\\text{{ cm}}^2\\)", f"\\({sa_val + 30}\\pi\\text{{ cm}}^2\\)", f"\\({sa_val - 25}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Radius**\n\\(r = \\frac{{{2 * r}}}{{2}} = {r}\\text{{ cm}}\\).\n**Step 2: Surface Area**\n\\(A = 4\\pi r^2 = {sa_val}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\n\\({sa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 2:
            txt = prefix + f"The surface area of a {obj_name} is \\({sa_val}\\pi\\text{{ cm}}^2\\). Determine the radius of the sphere."
            corr = f"\\({r}\\text{{ cm}}\\)"
            dist = [f"\\({r + 2}\\text{{ cm}}\\)", f"\\({2 * r}\\text{{ cm}}\\)", f"\\({r - 1}\\text{{ cm}}\\)", f"\\({r + 4}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Radius Formula**\n\\(r^2 = \\frac{{A}}{{4\\pi}} = \\frac{{{sa_val}\\pi}}{{4\\pi}} = {r*r} \\implies r = {r}\\text{{ cm}}\\).\n**Step 2: Conclusion**\nRadius is \\({r}\\text{{ cm}}\\)."
        elif archetype == 3:
            txt = prefix + f"The surface area of a spherical {obj_short} is \\({sa_val}\\pi\\text{{ cm}}^2\\). What is the diameter of this sphere?"
            d_val = 2 * r
            corr = f"\\({d_val}\\text{{ cm}}\\)"
            dist = [f"\\({r}\\text{{ cm}}\\)", f"\\({d_val + 2}\\text{{ cm}}\\)", f"\\({d_val * 2}\\text{{ cm}}\\)", f"\\({d_val - 2}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Radius**\n\\(r = \\sqrt{{\\frac{{{sa_val}}}{{4}}}} = {r}\\text{{ cm}}\\).\n**Step 2: Diameter**\n\\(d = 2r = {d_val}\\text{{ cm}}\\).\n**Step 3: Conclusion**\n\\({d_val}\\text{{ cm}}\\)."
        elif archetype == 4:
            txt = prefix + f"If the radius of a {obj_name} is \\({r}\\text{{ m}}\\), calculate the total external area requiring protective coating in terms of \\(\\pi\\)."
            corr = f"\\({sa_val}\\pi\\text{{ m}}^2\\)"
            dist = [f"\\({2 * sa_val}\\pi\\text{{ m}}^2\\)", f"\\({sa_val + 15}\\pi\\text{{ m}}^2\\)", f"\\({sa_val // 2}\\pi\\text{{ m}}^2\\)", f"\\({sa_val - 12}\\pi\\text{{ m}}^2\\)"]
            sol = f"**Step 1: Formula**\n\\(A = 4\\pi r^2 = 4\\pi \\times {r*r} = {sa_val}\\pi\\text{{ m}}^2\\).\n**Step 2: Conclusion**\n\\({sa_val}\\pi\\text{{ m}}^2\\)."
        elif archetype == 5:
            mult = 2 + ((idx // 8) % 7)
            factor = mult * mult
            txt = prefix + f"If the radius of a {obj_name} (measuring \\({r}\\text{{ cm}}\\)) is multiplied by {mult}, by what numerical factor does its surface area multiply?"
            corr = f"{factor}"
            dist = [f"{mult}", f"{2 * mult}", f"{factor + 5}", f"{factor - 3}"]
            sol = f"**Step 1: Scaling Law**\nSurface area is proportional to \\(r^2\\). When radius is multiplied by {mult}, surface area increases by \\({mult}^2 = {factor}\\).\n**Step 2: Conclusion**\nFactor is {factor}."
        elif archetype == 6:
            cost_rate = 2 + (idx % 9) * 2
            total_cost = sa_val * cost_rate
            txt = prefix + f"Electroplating a spherical {obj_name} of radius \\(r = {r}\\text{{ cm}}\\) costs ₹{cost_rate} per \\(\\pi\\text{{ cm}}^2\\). What is the total electroplating expense?"
            corr = f"₹{total_cost}"
            dist = [f"₹{total_cost + 40}", f"₹{total_cost - 30}", f"₹{total_cost * 2}", f"₹{total_cost + 80}"]
            sol = f"**Step 1: Surface Area**\n\\(A = 4\\pi r^2 = {sa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Expense**\n\\(\\text{{Cost}} = {sa_val} \\times {cost_rate} = ₹{total_cost}\\).\n**Step 3: Conclusion**\n₹{total_cost}."
        else:
            great_circle_area = r * r
            txt = prefix + f"The area of the great circle of a spherical {obj_name} is \\({great_circle_area}\\pi\\text{{ cm}}^2\\). What is the total surface area of the entire sphere?"
            corr = f"\\({sa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({2 * sa_val}\\pi\\text{{ cm}}^2\\)", f"\\({great_circle_area * 2}\\pi\\text{{ cm}}^2\\)", f"\\({sa_val + 20}\\pi\\text{{ cm}}^2\\)", f"\\({sa_val - 15}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Great Circle Relation**\n\\(A_{{\\text{{great circle}}}} = \\pi r^2 = {great_circle_area}\\pi\\).\nTotal surface area \\(= 4\\pi r^2 = 4 \\times {great_circle_area}\\pi = {sa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({sa_val}\\pi\\text{{ cm}}^2\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def generate_9_2_2():
    # Volume of Sphere = 4/3 * πr³
    tc = "MH-9-MTH2-9-9.2.2"
    tname = "Volume of Sphere = 4/3 * πr³"
    qs = []
    RADII_MULT3_80 = [3 * (i + 1) for i in range(80)]

    for idx, seq in enumerate(SEQS_80):
        r = RADII_MULT3_80[idx]
        obj_name, obj_short = SPHERE_OBJECTS_80[idx]
        vol_val = (4 * r**3) // 3
        has_fig = (idx % 5 != 0)
        svg = svg_sphere(f"r = {r} cm", f"{obj_name.title()} Vol #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        if archetype == 0:
            txt = prefix + f"Determine the exact volume of a solid {obj_name} of radius \\(r = {r}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({vol_val // 2}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val * 2}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 50}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 40}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Formula**\n\\(V = \\frac{{4}}{{3}}\\pi r^3 = \\frac{{4}}{{3}}\\pi ({r})^3 = \\frac{{4}}{{3}}\\pi \\times {r**3} = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."
        elif archetype == 1:
            txt = prefix + f"A spherical {obj_short} has base diameter \\({2 * r}\\text{{ cm}}\\). What volume of space does it occupy in terms of \\(\\pi\\)?"
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({8 * vol_val}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val // 4}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 70}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 60}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Radius**\n\\(r = \\frac{{{2 * r}}}{{2}} = {r}\\text{{ cm}}\\).\n**Step 2: Volume**\n\\(V = \\frac{{4}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 3: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."
        elif archetype == 2:
            txt = prefix + f"A craftsman melts a metallic spherical {obj_name} of radius \\({r}\\text{{ cm}}\\). What is the volume of molten metal yielded in terms of \\(\\pi\\)?"
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({r**3}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val * 3}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 100}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 80}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Formula**\n\\(V = \\frac{{4}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."
        elif archetype == 3:
            txt = prefix + f"The volume of a spherical {obj_short} is \\({vol_val}\\pi\\text{{ cm}}^3\\). Calculate its radius in cm."
            corr = f"\\({r}\\text{{ cm}}\\)"
            dist = [f"\\({r + 3}\\text{{ cm}}\\)", f"\\({r - 2}\\text{{ cm}}\\)", f"\\({2 * r}\\text{{ cm}}\\)", f"\\({r // 3}\\text{{ cm}}\\)"]
            sol = f"**Step 1: Formula**\n\\(r^3 = \\frac{{3V}}{{4\\pi}} = \\frac{{3 \\times {vol_val}\\pi}}{{4\\pi}} = {r**3} \\implies r = {r}\\text{{ cm}}\\).\n**Step 2: Conclusion**\nRadius is \\({r}\\text{{ cm}}\\)."
        elif archetype == 4:
            k = 1 + ((idx // 8) % 5)
            num = 4
            den = 3 * k
            g = math.gcd(num, den)
            ratio_str = f"{num // g}:{den // g}"
            txt = prefix + f"What is the ratio of the volume of a sphere of radius \\({r}\\text{{ cm}}\\) to the volume of a cylinder having the same radius and height \\(h = {k}r = {k*r}\\text{{ cm}}\\)?"
            corr = f"\\({ratio_str}\\)"
            dist = ["\\(1:2\\)" if ratio_str != "1:2" else "\\(3:4\\)", "\\(2:3\\)" if ratio_str != "2:3" else "\\(4:5\\)", "\\(3:2\\)", "\\(1:1\\)"]
            sol = f"**Step 1: Ratio**\n\\(\\frac{{V_{{\\text{{sphere}}}}}}{{V_{{\\text{{cyl}}}}}} = \\frac{{\\frac{{4}}{{3}}\\pi r^3}}{{\\pi r^2 ({k}r)}} = \\frac{{\\frac{{4}}{{3}}}}{{{k}}} = \\frac{{4}}{{{3*k}}} = {ratio_str}\\).\n**Step 2: Conclusion**\n\\({ratio_str}\\)."
        elif archetype == 5:
            r_small = 1 + (idx % 3)
            n_spheres = (r // r_small)**3
            txt = prefix + f"A solid metal {obj_name} of radius \\({r}\\text{{ cm}}\\) is melted down and recast into small marbles of radius {r_small} cm. How many such marbles can be cast?"
            corr = f"{n_spheres}"
            dist = [f"{n_spheres * 2}", f"{n_spheres + 10}", f"{n_spheres // 2}", f"{n_spheres - 5}"]
            sol = f"**Step 1: Formula**\n\\(N = \\frac{{\\frac{{4}}{{3}}\\pi R^3}}{{\\frac{{4}}{{3}}\\pi r^3}} = \\frac{{{r}^3}}{{{r_small}^3}} = \\frac{{{r**3}}}{{{r_small**3}}} = {n_spheres}\\).\n**Step 2: Conclusion**\n{n_spheres} marbles."
        elif archetype == 6:
            txt = prefix + f"A spherical water tank has radius \\({r}\\text{{ m}}\\). How many cubic meters of water can it store when completely full in terms of \\(\\pi\\)?"
            corr = f"\\({vol_val}\\pi\\text{{ m}}^3\\)"
            dist = [f"\\({vol_val * 2}\\pi\\text{{ m}}^3\\)", f"\\({vol_val // 2}\\pi\\text{{ m}}^3\\)", f"\\({vol_val + 120}\\pi\\text{{ m}}^3\\)", f"\\({vol_val - 90}\\pi\\text{{ m}}^3\\)"]
            sol = f"**Step 1: Capacity**\n\\(V = \\frac{{4}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ m}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ m}}^3\\)."
        else:
            txt = prefix + f"A spherical {obj_short} of radius \\(r = {r}\\text{{ cm}}\\) is immersed in a water vessel. What volume of water does it displace in terms of \\(\\pi\\)?"
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({vol_val * 4}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val // 3}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 85}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 75}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Archimedes Principle**\nDisplaced water volume equals the sphere's volume \\(\\frac{{4}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

HEMI_OBJECTS_80 = [
    ("hemispherical soup bowl", "bowl"), ("hemispherical palace dome", "dome"), ("hemispherical igloo shelter", "igloo"),
    ("hemispherical radar antenna", "dish"), ("hemispherical brass basin", "basin"), ("hemispherical glass cloche", "cloche"),
    ("hemispherical stone mortar", "mortar"), ("hemispherical copper kettle bottom", "kettle base"), ("hemispherical wok pan", "wok"),
    ("hemispherical planetarium ceiling", "ceiling"), ("hemispherical steel pressure vessel cap", "tank cap"), ("hemispherical ceramic salad bowl", "salad bowl"),
    ("hemispherical hanging pendant lamp", "lamp"), ("hemispherical concrete bunker roof", "bunker dome"), ("hemispherical fruit bowl", "bowl"),
    ("hemispherical acoustic sound reflector", "sound dome"), ("hemispherical diving bell crown", "diving bell"), ("hemispherical copper ladling bowl", "ladle"),
    ("hemispherical wooden mixing bowl", "mixing bowl"), ("hemispherical observation cupola", "cupola"),
    ("hemispherical decorative flowerpot", "flowerpot"), ("hemispherical grain bin lid", "bin lid"), ("hemispherical security mirror dome", "mirror dome"),
    ("hemispherical tea strainer bowl", "strainer"), ("hemispherical bronze sundial bowl", "sundial"), ("hemispherical stainless steel mixing basin", "basin"),
    ("hemispherical stone fountain pool", "fountain pool"), ("hemispherical skylight dome", "skylight"), ("hemispherical bell clapper cover", "bell cover"),
    ("hemispherical water storage cistern", "cistern"), ("hemispherical furnace crucible", "crucible"), ("hemispherical melting pot", "melting pot"),
    ("hemispherical gold leaf bowl", "gold bowl"), ("hemispherical birdbath basin", "birdbath"), ("hemispherical spotlight reflector", "reflector"),
    ("hemispherical acoustic microphone dish", "mic dish"), ("hemispherical copper cauldron bottom", "cauldron"), ("hemispherical radar receiver cup", "radar cup"),
    ("hemispherical glass paperweight dome", "paperweight"), ("hemispherical terracotta planter", "planter"),
    ("hemispherical stone firepit basin", "firepit"), ("hemispherical marble baptismal font", "font"), ("hemispherical lead shield cap", "shield cap"),
    ("hemispherical satellite tracking dish", "dish"), ("hemispherical church belfry dome", "belfry"), ("hemispherical sugar boiling pan", "boiling pan"),
    ("hemispherical cast iron crucible", "crucible"), ("hemispherical copper roof cupola", "cupola"), ("hemispherical bronze singing bowl", "singing bowl"),
    ("hemispherical observatory telescope dome", "observatory dome"), ("hemispherical glass terrarium base", "terrarium"), ("hemispherical oil collection sump", "sump"),
    ("hemispherical silver fruit platter", "platter"), ("hemispherical diving helmet visor", "visor"), ("hemispherical cement mixing drum cap", "drum cap"),
    ("hemispherical ceramic punch bowl", "punch bowl"), ("hemispherical steel cauldron lid", "cauldron lid"), ("hemispherical laboratory watchglass", "watchglass"),
    ("hemispherical copper brazier basin", "brazier"), ("hemispherical stone grinding dish", "grinding dish"),
    ("hemispherical wooden mortar bowl", "mortar"), ("hemispherical brass incense burner", "burner"), ("hemispherical granite garden basin", "garden basin"),
    ("hemispherical stained glass lampshade", "lampshade"), ("hemispherical steel kettle lid", "lid"), ("hemispherical gold communion chalice base", "chalice base"),
    ("hemispherical marble bath basin", "bath basin"), ("hemispherical bronze fountain bowl", "fountain bowl"), ("hemispherical iron smelting pot", "smelting pot"),
    ("hemispherical silver offering bowl", "offering bowl"), ("hemispherical clay baking cloche", "cloche"), ("hemispherical acoustic amplifier dish", "amplifier dish"),
    ("hemispherical copper water reservoir", "reservoir"), ("hemispherical stone ritual basin", "ritual basin"), ("hemispherical glass crystal bowl", "crystal bowl"),
    ("hemispherical bronze vessel bottom", "vessel base"), ("hemispherical steel buoy bottom", "buoy base"), ("hemispherical lead furnace cap", "furnace cap"),
    ("hemispherical aluminum melting cup", "melting cup"), ("hemispherical brass ship compass gimbal", "gimbal")
]

def generate_9_2_3():
    # Curved Surface Area of Hemisphere = 2πr²
    tc = "MH-9-MTH2-9-9.2.3"
    tname = "Curved Surface Area of Hemisphere = 2πr²"
    qs = []
    for idx, seq in enumerate(SEQS_80):
        r = RADII_80[idx]
        obj_name, obj_short = HEMI_OBJECTS_80[idx]
        csa_val = 2 * r * r
        has_fig = (idx % 5 != 0)
        svg = svg_hemi(f"r = {r} cm", f"{obj_name.title()} CSA #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        if archetype == 0:
            txt = prefix + f"Determine the curved surface area of a {obj_name} of radius \\(r = {r}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
            corr = f"\\({csa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({csa_val * 2}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val // 2}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val + 14}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val - 12}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Formula**\n\\(\\text{{CSA}} = 2\\pi r^2 = 2\\pi \\times {r}^2 = 2\\pi \\times {r*r} = {csa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\nCurved surface area is \\({csa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 1:
            txt = prefix + f"A {obj_short} has internal diameter \\({2 * r}\\text{{ cm}}\\). What is its internal curved surface area in terms of \\(\\pi\\)?"
            corr = f"\\({csa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({4 * csa_val}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val + 25}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val // 2}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val - 20}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Radius**\n\\(r = \\frac{{{2 * r}}}{{2}} = {r}\\text{{ cm}}\\).\n**Step 2: Curved Area**\n\\(\\text{{CSA}} = 2\\pi r^2 = {csa_val}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\n\\({csa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 2:
            txt = prefix + f"The curved surface area of a {obj_name} is \\({csa_val}\\pi\\text{{ cm}}^2\\). Calculate its radius in cm."
            corr = f"\\({r}\\text{{ cm}}\\)"
            dist = [f"\\({r + 2}\\text{{ cm}}\\)", f"\\({r - 1}\\text{{ cm}}\\)", f"\\({2 * r}\\text{{ cm}}\\)", f"\\({r + 4}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Formula**\n\\(r^2 = \\frac{{\\text{{CSA}}}}{{2\\pi}} = \\frac{{{csa_val}\\pi}}{{2\\pi}} = {r*r} \\implies r = {r}\\text{{ cm}}\\).\n**Step 2: Conclusion**\nRadius is \\({r}\\text{{ cm}}\\)."
        elif archetype == 3:
            txt = prefix + f"A painter paints the outer dome of a {obj_name} of radius \\(r = {r}\\text{{ m}}\\). What is the total area painted in terms of \\(\\pi\\)?"
            corr = f"\\({csa_val}\\pi\\text{{ m}}^2\\)"
            dist = [f"\\({2 * csa_val}\\pi\\text{{ m}}^2\\)", f"\\({csa_val + 16}\\pi\\text{{ m}}^2\\)", f"\\({csa_val - 14}\\pi\\text{{ m}}^2\\)", f"\\({csa_val * 3}\\pi\\text{{ m}}^2\\)"]
            sol = f"**Step 1: Outer Curved Surface**\n\\(\\text{{Area}} = 2\\pi r^2 = 2\\pi \\times {r}^2 = {csa_val}\\pi\\text{{ m}}^2\\).\n**Step 2: Conclusion**\n\\({csa_val}\\pi\\text{{ m}}^2\\)."
        elif archetype == 4:
            k = 1 + ((idx // 8) % 4)
            ratio_str = f"1:{k}"
            txt = prefix + f"What is the ratio of the curved surface area of a hemisphere to that of a cylinder having the same radius \\({r}\\text{{ cm}}\\) and height \\(h = {k}r = {k*r}\\text{{ cm}}\\)?"
            corr = f"\\({ratio_str}\\)"
            dist = ["\\(2:1\\)", "\\(1:2\\)" if ratio_str != "1:2" else "\\(2:3\\)", "\\(1:3\\)" if ratio_str != "1:3" else "\\(3:4\\)", "\\(1:1\\)"]
            sol = f"**Step 1: Ratio**\n\\(\\frac{{\\text{{CSA}}_{{\\text{{hemi}}}}}}{{\\text{{CSA}}_{{\\text{{cyl}}}}}} = \\frac{{2\\pi r^2}}{{2\\pi r ({k}r)}} = \\frac{{1}}{{{k}}} = {ratio_str}\\).\n**Step 2: Conclusion**\n\\({ratio_str}\\)."
        elif archetype == 5:
            tin_rate = 3 + (idx % 10) * 2
            cost = csa_val * tin_rate
            txt = prefix + f"Tin-plating the inside of a {obj_name} of radius \\({r}\\text{{ cm}}\\) costs ₹{tin_rate} per \\(\\pi\\text{{ cm}}^2\\). Calculate the total tin-plating bill."
            corr = f"₹{cost}"
            dist = [f"₹{cost + 35}", f"₹{cost - 25}", f"₹{cost * 2}", f"₹{cost + 70}"]
            sol = f"**Step 1: Inside Area**\n\\(\\text{{CSA}} = 2\\pi r^2 = {csa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Bill**\n\\(\\text{{Cost}} = {csa_val} \\times {tin_rate} = ₹{cost}\\).\n**Step 3: Conclusion**\n₹{cost}."
        elif archetype == 6:
            txt = prefix + f"The curved surface area of a {obj_name} is \\({csa_val}\\pi\\text{{ cm}}^2\\). What is the diameter of its circular rim?"
            d_val = 2 * r
            corr = f"\\({d_val}\\text{{ cm}}\\)"
            dist = [f"\\({r}\\text{{ cm}}\\)", f"\\({d_val + 2}\\text{{ cm}}\\)", f"\\({d_val - 2}\\text{{ cm}}\\)", f"\\({2 * d_val}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Radius**\n\\(r = \\sqrt{{\\frac{{{csa_val}}}{{2}}}} = {r}\\text{{ cm}}\\).\n**Step 2: Diameter**\n\\(d = 2r = {d_val}\\text{{ cm}}\\).\n**Step 3: Conclusion**\n\\({d_val}\\text{{ cm}}\\)."
        else:
            base_area = r * r
            txt = prefix + f"The base circular opening of a {obj_short} has an area of \\({base_area}\\pi\\text{{ cm}}^2\\). What is its curved surface area?"
            corr = f"\\({csa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({base_area}\\pi\\text{{ cm}}^2\\)", f"\\({3 * base_area}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val + 10}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val - 8}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Relation**\n\\(\\text{{CSA}} = 2 \\times \\text{{Base Area}} = 2 \\times {base_area}\\pi = {csa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({csa_val}\\pi\\text{{ cm}}^2\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def generate_9_2_4():
    # Total Surface Area of Hemisphere = 3πr²
    tc = "MH-9-MTH2-9-9.2.4"
    tname = "Total Surface Area of Hemisphere = 3πr²"
    qs = []
    ratio_options = [
        ("curved surface area to flat circular base area", "2:1", "\\(\\frac{2\\pi r^2}{\\pi r^2} = 2:1\\)"),
        ("total surface area to flat circular base area", "3:1", "\\(\\frac{3\\pi r^2}{\\pi r^2} = 3:1\\)"),
        ("flat circular base area to curved surface area", "1:2", "\\(\\frac{\\pi r^2}{2\\pi r^2} = 1:2\\)"),
        ("flat circular base area to total surface area", "1:3", "\\(\\frac{\\pi r^2}{3\\pi r^2} = 1:3\\)"),
        ("curved surface area to total surface area", "2:3", "\\(\\frac{2\\pi r^2}{3\\pi r^2} = 2:3\\)"),
        ("total surface area to curved surface area", "3:2", "\\(\\frac{3\\pi r^2}{2\\pi r^2} = 3:2\\)")
    ]
    for idx, seq in enumerate(SEQS_80):
        r = RADII_80[idx]
        obj_name, obj_short = HEMI_OBJECTS_80[idx]
        tsa_val = 3 * r * r
        has_fig = (idx % 5 != 0)
        svg = svg_hemi(f"r = {r} cm", f"{obj_name.title()} TSA #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        if archetype == 0:
            txt = prefix + f"Calculate the total surface area of a solid {obj_name} having radius \\(r = {r}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
            corr = f"\\({tsa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({2 * r * r}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val * 2}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val + 24}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val - 18}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Formula**\n\\(\\text{{TSA}} = 3\\pi r^2 = 3\\pi \\times {r}^2 = 3\\pi \\times {r*r} = {tsa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\nTotal surface area is \\({tsa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 1:
            txt = prefix + f"A solid metal {obj_short} has base diameter \\({2 * r}\\text{{ cm}}\\). What is its total surface area including its circular base in terms of \\(\\pi\\)?"
            corr = f"\\({tsa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({4 * tsa_val}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val + 30}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val // 3}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val - 25}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Radius**\n\\(r = \\frac{{{2 * r}}}{{2}} = {r}\\text{{ cm}}\\).\n**Step 2: Total Surface Area**\n\\(\\text{{TSA}} = 3\\pi r^2 = {tsa_val}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\n\\({tsa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 2:
            txt = prefix + f"The total surface area of a solid {obj_name} is \\({tsa_val}\\pi\\text{{ cm}}^2\\). Determine the radius of this hemisphere."
            corr = f"\\({r}\\text{{ cm}}\\)"
            dist = [f"\\({r + 3}\\text{{ cm}}\\)", f"\\({r - 1}\\text{{ cm}}\\)", f"\\({2 * r}\\text{{ cm}}\\)", f"\\({r + 5}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Radius Formula**\n\\(r^2 = \\frac{{\\text{{TSA}}}}{{3\\pi}} = \\frac{{{tsa_val}\\pi}}{{3\\pi}} = {r*r} \\implies r = {r}\\text{{ cm}}\\).\n**Step 2: Conclusion**\nRadius is \\({r}\\text{{ cm}}\\)."
        elif archetype == 3:
            base_area = r * r
            csa_val = 2 * r * r
            txt = prefix + f"A solid {obj_short} has curved surface area \\({csa_val}\\pi\\text{{ cm}}^2\\) and flat base area \\({base_area}\\pi\\text{{ cm}}^2\\). What is its total surface area?"
            corr = f"\\({tsa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({csa_val}\\pi\\text{{ cm}}^2\\)", f"\\({base_area}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val + 15}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val * 2}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Addition**\n\\(\\text{{TSA}} = \\text{{CSA}} + \\text{{Base Area}} = {csa_val}\\pi + {base_area}\\pi = {tsa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({tsa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 4:
            ratio_idx = (idx // 8) % len(ratio_options)
            desc, ans_val, exp_str = ratio_options[ratio_idx]
            txt = prefix + f"For any solid hemisphere of radius \\({r}\\text{{ cm}}\\), what is the ratio of its {desc}?"
            corr = f"\\({ans_val}\\)"
            dist = ["\\(1:1\\)", "\\(2:1\\)" if ans_val != "2:1" else "\\(1:4\\)", "\\(3:1\\)" if ans_val != "3:1" else "\\(4:1\\)", "\\(2:3\\)" if ans_val != "2:3" else "\\(3:4\\)"]
            sol = f"**Step 1: Ratio**\n{exp_str}.\n**Step 2: Conclusion**\n\\({ans_val}\\)."
        elif archetype == 5:
            cost_rate = 4 + (idx % 8) * 3
            cost = tsa_val * cost_rate
            txt = prefix + f"Polishing the entire surface (curved + flat base) of a solid {obj_name} of radius \\({r}\\text{{ cm}}\\) costs ₹{cost_rate} per \\(\\pi\\text{{ cm}}^2\\). Find the total polishing charge."
            corr = f"₹{cost}"
            dist = [f"₹{cost + 50}", f"₹{cost - 35}", f"₹{cost * 2}", f"₹{cost + 90}"]
            sol = f"**Step 1: TSA**\n\\(\\text{{TSA}} = 3\\pi r^2 = {tsa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Charge**\n\\(\\text{{Cost}} = {tsa_val} \\times {cost_rate} = ₹{cost}\\).\n**Step 3: Conclusion**\n₹{cost}."
        elif archetype == 6:
            txt = prefix + f"If the total surface area of a solid {obj_short} is \\({tsa_val}\\pi\\text{{ cm}}^2\\), calculate the diameter of its circular base."
            d_val = 2 * r
            corr = f"\\({d_val}\\text{{ cm}}\\)"
            dist = [f"\\({r}\\text{{ cm}}\\)", f"\\({d_val + 2}\\text{{ cm}}\\)", f"\\({d_val - 2}\\text{{ cm}}\\)", f"\\({2 * d_val}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Radius**\n\\(r = \\sqrt{{\\frac{{{tsa_val}}}{{3}}}} = {r}\\text{{ cm}}\\).\n**Step 2: Diameter**\n\\(d = 2r = {d_val}\\text{{ cm}}\\).\n**Step 3: Conclusion**\n\\({d_val}\\text{{ cm}}\\)."
        else:
            diff_area = tsa_val - (2 * r * r)
            txt = prefix + f"By how much does the total surface area of a solid {obj_short} of radius \\({r}\\text{{ cm}}\\) exceed its curved surface area in terms of \\(\\pi\\)?"
            corr = f"\\({diff_area}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({2 * diff_area}\\pi\\text{{ cm}}^2\\)", f"\\({diff_area + 6}\\pi\\text{{ cm}}^2\\)", f"\\({r}\\pi\\text{{ cm}}^2\\)", f"\\({diff_area - 4}\\pi\\text{{ cm}}^2\\)" if diff_area > 4 else f"\\({diff_area + 12}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Concept**\n\\(\\text{{TSA}} - \\text{{CSA}} = 3\\pi r^2 - 2\\pi r^2 = \\pi r^2 = {diff_area}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({diff_area}\\pi\\text{{ cm}}^2\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def generate_9_2_5():
    # Volume of Hemisphere = 2/3 * πr³
    tc = "MH-9-MTH2-9-9.2.5"
    tname = "Volume of Hemisphere = 2/3 * πr³"
    qs = []
    RADII_MULT3_80 = [3 * (i + 1) for i in range(80)]

    for idx, seq in enumerate(SEQS_80):
        r = RADII_MULT3_80[idx]
        obj_name, obj_short = HEMI_OBJECTS_80[idx]
        vol_val = (2 * r**3) // 3
        has_fig = (idx % 5 != 0)
        svg = svg_hemi(f"r = {r} cm", f"{obj_name.title()} Vol #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        if archetype == 0:
            txt = prefix + f"Determine the volume of a solid {obj_name} of radius \\(r = {r}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({vol_val * 2}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val // 2}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 36}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 28}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Formula**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = \\frac{{2}}{{3}}\\pi ({r})^3 = \\frac{{2}}{{3}}\\pi \\times {r**3} = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."
        elif archetype == 1:
            txt = prefix + f"A {obj_name} has base diameter \\({2 * r}\\text{{ cm}}\\). What is its maximum liquid capacity in terms of \\(\\pi\\)?"
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({8 * vol_val}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 45}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val * 2}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 35}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Radius**\n\\(r = \\frac{{{2 * r}}}{{2}} = {r}\\text{{ cm}}\\).\n**Step 2: Capacity**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 3: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."
        elif archetype == 2:
            txt = prefix + f"A solid {obj_name} of radius \\(r = {r}\\text{{ cm}}\\) is melted down and completely recast into a cylinder of equal radius. What is the height of the resulting cylinder in cm?"
            h_cyl = (2 * r) / 3
            corr = f"\\({h_cyl:.2f}\\text{{ cm}}\\)" if h_cyl != int(h_cyl) else f"\\({int(h_cyl)}\\text{{ cm}}\\)"
            val_h = int(h_cyl) if h_cyl == int(h_cyl) else round(h_cyl, 2)
            dist = [f"\\({val_h + 4}\\text{{ cm}}\\)", f"\\({val_h + 2}\\text{{ cm}}\\)", f"\\({max(1, val_h - 2)}\\text{{ cm}}\\)", f"\\({2 * val_h}\\text{{ cm}}\\)"]
            sol = f"**Step 1: Equate Volumes**\n\\(\\pi r^2 h = \\frac{{2}}{{3}}\\pi r^3 \\implies h = \\frac{{2}}{{3}}r = \\frac{{2}}{{3}} \\times {r} = {corr}\\).\n**Step 2: Conclusion**\nHeight is {corr}."
        elif archetype == 3:
            txt = prefix + f"The volume of a {obj_short} is \\({vol_val}\\pi\\text{{ cm}}^3\\). What is the radius of the hemisphere in cm?"
            corr = f"\\({r}\\text{{ cm}}\\)"
            dist = [f"\\({r + 3}\\text{{ cm}}\\)", f"\\({r - 2}\\text{{ cm}}\\)", f"\\({2 * r}\\text{{ cm}}\\)", f"\\({r // 3}\\text{{ cm}}\\)"]
            sol = f"**Step 1: Radius Calculation**\n\\(r^3 = \\frac{{3V}}{{2\\pi}} = \\frac{{3 \\times {vol_val}\\pi}}{{2\\pi}} = {r**3} \\implies r = {r}\\text{{ cm}}\\).\n**Step 2: Conclusion**\nRadius is \\({r}\\text{{ cm}}\\)."
        elif archetype == 4:
            k = 1 + ((idx // 8) % 4)
            num = 2
            den = 3 * k
            g = math.gcd(num, den)
            ratio_str = f"{num // g}:{den // g}"
            txt = prefix + f"What is the ratio of the volume of a hemisphere of radius \\({r}\\text{{ cm}}\\) to the volume of a cylinder having the same radius and height \\(h = {k}r = {k*r}\\text{{ cm}}\\)?"
            corr = f"\\({ratio_str}\\)"
            dist = ["\\(1:2\\)" if ratio_str != "1:2" else "\\(2:5\\)", "\\(1:3\\)" if ratio_str != "1:3" else "\\(3:4\\)", "\\(2:3\\)" if ratio_str != "2:3" else "\\(1:4\\)", "\\(1:1\\)"]
            sol = f"**Step 1: Ratio**\n\\(\\frac{{V_{{\\text{{hemi}}}}}}{{V_{{\\text{{cyl}}}}}} = \\frac{{\\frac{{2}}{{3}}\\pi r^3}}{{\\pi r^2 ({k}r)}} = \\frac{{\\frac{{2}}{{3}}}}{{{k}}} = \\frac{{2}}{{{3*k}}} = {ratio_str}\\).\n**Step 2: Conclusion**\n\\({ratio_str}\\)."
        elif archetype == 5:
            DOMES_ARCH_5 = [
                ("palace observatory dome", "internal atmospheric volume"),
                ("planetarium projection hall dome", "interior hall capacity"),
                ("military bunker protective dome", "subterranean air enclosure"),
                ("botanical greenhouse glass dome", "interior greenhouse space"),
                ("sports arena geodesic fabric dome", "air volume enclosed by the structure"),
                ("acoustic auditorium ceiling dome", "cubic meters of acoustical space"),
                ("agricultural grain silo dome roof", "headspace volume beneath the roof"),
                ("weather radar tracking dome", "internal sheltered air volume"),
                ("polar research pavilion dome", "enclosed atmospheric breathing volume"),
                ("architectural cathedral hemispherical dome", "grand vaulted air capacity"),
            ]
            arch_idx = (idx // 8) % 10
            dome_title, vol_phrase = DOMES_ARCH_5[arch_idx]
            txt = prefix + f"An architectural {dome_title} has an inner radius of \\(r = {r}\\text{{ m}}\\). Calculate the total {vol_phrase} in terms of \\(\\pi\\)."
            corr = f"\\({vol_val}\\pi\\text{{ m}}^3\\)"
            dist = [f"\\({vol_val * 2}\\pi\\text{{ m}}^3\\)", f"\\({vol_val + 80}\\pi\\text{{ m}}^3\\)", f"\\({vol_val // 2}\\pi\\text{{ m}}^3\\)", f"\\({vol_val - 60}\\pi\\text{{ m}}^3\\)"]
            sol = f"**Step 1: Air Enclosed**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ m}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ m}}^3\\)."
        elif archetype == 6:
            r_small = 1 + (idx % 3)
            n_spheres = (r**3) // (2 * (r_small**3))
            txt = prefix + f"A solid metal {obj_name} of radius \\({r}\\text{{ cm}}\\) is melted down to cast small spheres of radius {r_small} cm. How many such spheres can be made?"
            corr = f"{n_spheres}"
            dist = [f"{n_spheres * 2}", f"{n_spheres + 5}", f"{n_spheres // 2}", f"{n_spheres - 3}"]
            sol = f"**Step 1: Number of Spheres**\n\\(N = \\frac{{\\frac{{2}}{{3}}\\pi R^3}}{{\\frac{{4}}{{3}}\\pi r^3}} = \\frac{{R^3}}{{2r^3}} = \\frac{{{r}^3}}{{2 \\times {r_small**3}}} = {n_spheres}\\).\n**Step 2: Conclusion**\n{n_spheres} spheres."
        else:
            txt = prefix + f"A container shaped as a {obj_name} of radius \\(r = {r}\\text{{ cm}}\\) is filled with mercury. What is the volume of mercury contained in terms of \\(\\pi\\)?"
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({vol_val * 3}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 55}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val // 2}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 45}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Volume**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def main():
    all_qs = []
    all_qs.extend(generate_9_1_1())
    all_qs.extend(generate_9_1_2())
    all_qs.extend(generate_9_1_3())
    all_qs.extend(generate_9_1_4())
    all_qs.extend(generate_9_2_1())
    all_qs.extend(generate_9_2_2())
    all_qs.extend(generate_9_2_3())
    all_qs.extend(generate_9_2_4())
    all_qs.extend(generate_9_2_5())

    print(f"Generated {len(all_qs)} total questions across 9 subtopics.")
    with open("scripts/mh9_mth2_ch9_perfect.json", "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/mh9_mth2_ch9_perfect.json")

if __name__ == "__main__":
    main()
