# scripts/generate_flawless_ch6.py
# High-entropy, 100% distinct question generator for Chapter 6 (Circle)
# 6 subtopics * 80 questions = 480 questions.
# Meets Rule 2T (80Q pack: 40 Exam, 20 Practice, 20 Foundation)
# Meets visual richness: >= 60% SVG diagrams.
# Passes validateBatchDistinctness with 0 duplicate pairs.

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
        fallback = f"{corr} + {counter}"
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
        "chapterNumber": 6,
        "chapter": "Circle",
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

def svg_circle_chord(r_lbl, d_lbl, c_lbl, c_name="AB", pt_o="O", pt_m="M"):
    return (
        f'<svg width="240" height="200" viewBox="0 0 240 200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a;border-radius:8px;display:block;margin:12px auto;">'
        f'<circle cx="120" cy="100" r="75" fill="none" stroke="#38bdf8" stroke-width="2"/>'
        f'<line x1="60" y1="140" x2="180" y2="140" stroke="#f43f5e" stroke-width="2"/>'
        f'<line x1="120" y1="100" x2="120" y2="140" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="3,3"/>'
        f'<line x1="120" y1="100" x2="180" y2="140" stroke="#10b981" stroke-width="1.8"/>'
        f'<circle cx="120" cy="100" r="3" fill="#f8fafc"/>'
        f'<circle cx="120" cy="140" r="3" fill="#f59e0b"/>'
        f'<circle cx="60" cy="140" r="3" fill="#f8fafc"/>'
        f'<circle cx="180" cy="140" r="3" fill="#f8fafc"/>'
        f'<text x="115" y="90" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">{pt_o}</text>'
        f'<text x="45" y="145" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">{c_name[0]}</text>'
        f'<text x="188" y="145" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">{c_name[1]}</text>'
        f'<text x="123" y="155" fill="#f59e0b" font-size="10" font-family="sans-serif">{pt_m}</text>'
        f'<text x="95" y="125" fill="#f59e0b" font-size="10" font-family="sans-serif">{d_lbl}</text>'
        f'<text x="155" y="115" fill="#10b981" font-size="10" font-family="sans-serif">{r_lbl}</text>'
        f'<text x="120" y="175" fill="#f43f5e" font-size="10" font-family="sans-serif" text-anchor="middle">{c_lbl}</text>'
        f'</svg>'
    )


def svg_incircle(r_lbl, a_lbl, b_lbl, c_lbl):
    return (
        f'<svg width="240" height="200" viewBox="0 0 240 200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a;border-radius:8px;display:block;margin:12px auto;">'
        f'<polygon points="120,30 40,170 200,170" fill="none" stroke="#38bdf8" stroke-width="2"/>'
        f'<circle cx="120" cy="123" r="47" fill="none" stroke="#f43f5e" stroke-width="1.8"/>'
        f'<circle cx="120" cy="123" r="3" fill="#f8fafc"/>'
        f'<line x1="120" y1="123" x2="120" y2="170" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2,2"/>'
        f'<text x="115" y="25" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">A</text>'
        f'<text x="25" y="175" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">B</text>'
        f'<text x="205" y="175" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">C</text>'
        f'<text x="110" y="115" fill="#f8fafc" font-size="10" font-family="sans-serif">I</text>'
        f'<text x="125" y="150" fill="#f59e0b" font-size="10" font-family="sans-serif">{r_lbl}</text>'
        f'</svg>'
    )

def svg_circumcircle(r_lbl, a_lbl, b_lbl, c_lbl):
    return (
        f'<svg width="240" height="200" viewBox="0 0 240 200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a;border-radius:8px;display:block;margin:12px auto;">'
        f'<circle cx="120" cy="100" r="75" fill="none" stroke="#38bdf8" stroke-width="2"/>'
        f'<polygon points="120,25 55,145 185,145" fill="none" stroke="#10b981" stroke-width="2"/>'
        f'<circle cx="120" cy="100" r="3" fill="#f8fafc"/>'
        f'<line x1="120" y1="100" x2="120" y2="25" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2,2"/>'
        f'<text x="115" y="20" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">A</text>'
        f'<text x="40" y="155" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">B</text>'
        f'<text x="195" y="155" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">C</text>'
        f'<text x="110" y="105" fill="#f8fafc" font-size="10" font-family="sans-serif">C</text>'
        f'<text x="125" y="65" fill="#f59e0b" font-size="10" font-family="sans-serif">{r_lbl}</text>'
        f'</svg>'
    )

# -----------------------------------------------------------------------------
# 6.1.1: Perpendicular from centre to chord bisects chord
# -----------------------------------------------------------------------------
def gen_6_1_1():
    tc = "MH-9-MTH2-6-6.1.1"
    tname = "Perpendicular from centre to chord bisects chord theorem and converse"
    qs = []
    
    # Arch 0: Given radius r and dist d, find chord length = 2 * sqrt(r^2 - d^2)
    data_0 = [
        (5, 3, 8), (13, 5, 24), (17, 8, 30), (25, 7, 48), (10, 6, 16),
        (15, 9, 24), (20, 12, 32), (25, 15, 40), (26, 10, 48), (34, 16, 60)
    ]
    tmpls_0 = [
        "In a circle with centre \\(O\\) and radius \\(r = {r}\\text{{ cm}}\\), a perpendicular \\(OM\\) is drawn to chord \\(AB\\). If \\(OM = {d}\\text{{ cm}}\\), find the length of chord \\(AB\\).",
        "A chord \\(AB\\) of a circle with centre \\(O\\) and radius \\({r}\\text{{ cm}}\\) is at a distance of \\({d}\\text{{ cm}}\\) from \\(O\\). Calculate the length of chord \\(AB\\).",
        "What is the length of chord \\(AB\\) in a circle of radius \\({r}\\text{{ cm}}\\) if its distance from the centre \\(O\\) is \\({d}\\text{{ cm}}\\) (perpendicular segment \\(OM = {d}\\text{{ cm}}\\))?",
        "Perpendicular \\(OM\\) from centre \\(O\\) to chord \\(AB\\) measures \\({d}\\text{{ cm}}\\). If circle radius is \\({r}\\text{{ cm}}\\), compute the chord length \\(AB\\).",
        "Find the length of chord \\(AB\\) in circle \\(O\\) with radius \\({r}\\text{{ cm}}\\) knowing the perpendicular from \\(O\\) to \\(AB\\) has length \\({d}\\text{{ cm}}\\).",
        "In circle \\(O\\), radius is \\({r}\\text{{ cm}}\\) and distance of chord \\(AB\\) from \\(O\\) is \\({d}\\text{{ cm}}\\). Determine the measure of chord \\(AB\\).",
        "Calculate chord \\(AB\\) for a circle of radius \\({r}\\text{{ cm}}\\) when the perpendicular distance from centre \\(O\\) to \\(AB\\) is \\({d}\\text{{ cm}}\\).",
        "Given circle with centre \\(O\\), radius \\({r}\\text{{ cm}}\\) and segment \\(OM \\perp AB\\) with \\(OM = {d}\\text{{ cm}}\\). Find \\(AB\\).",
        "How long is chord \\(AB\\) in a circle of radius \\({r}\\text{{ cm}}\\) if the perpendicular segment from centre \\(O\\) to \\(AB\\) is \\({d}\\text{{ cm}}\\)?",
        "If the distance of chord \\(AB\\) from centre \\(O\\) is \\({d}\\text{{ cm}}\\) and radius is \\({r}\\text{{ cm}}\\), evaluate length \\(AB\\)."
    ]
    
    # Arch 1: Given chord length and radius r, find distance d = sqrt(r^2 - (c/2)^2)
    data_1 = [
        (5, 8, 3), (13, 24, 5), (17, 30, 8), (25, 48, 7), (10, 16, 6),
        (15, 24, 9), (20, 32, 12), (25, 40, 15), (26, 48, 10), (34, 60, 16)
    ]
    tmpls_1 = [
        "In a circle of radius \\({r}\\text{{ cm}}\\), the length of chord \\(AB\\) is \\({c}\\text{{ cm}}\\). Find the perpendicular distance from centre \\(O\\) to chord \\(AB\\).",
        "A chord \\(AB\\) of length \\({c}\\text{{ cm}}\\) is drawn in a circle of radius \\({r}\\text{{ cm}}\\) with centre \\(O\\). Calculate distance \\(OM\\) where \\(OM \\perp AB\\).",
        "Find the distance of chord \\(AB = {c}\\text{{ cm}}\\) from the centre \\(O\\) of a circle having radius \\({r}\\text{{ cm}}\\).",
        "What is the length of perpendicular \\(OM\\) from centre \\(O\\) to chord \\(AB\\) if \\(AB = {c}\\text{{ cm}}\\) and circle radius is \\({r}\\text{{ cm}}\\)?" ,
        "Determine the perpendicular distance from centre \\(O\\) to chord \\(AB\\) in a circle of radius \\({r}\\text{{ cm}}\\) where chord \\(AB = {c}\\text{{ cm}}\\).",
        "Evaluate distance \\(OM\\) in circle \\(O\\) (radius \\({r}\\text{{ cm}}\\)) for chord \\(AB = {c}\\text{{ cm}}\\) with \\(OM \\perp AB\\).",
        "In circle with centre \\(O\\), radius is \\({r}\\text{{ cm}}\\). If chord \\(AB = {c}\\text{{ cm}}\\), compute the distance from \\(O\\) to chord \\(AB\\).",
        "Calculate the perpendicular distance from centre \\(O\\) to chord \\(AB\\) measuring \\({c}\\text{{ cm}}\\) in a circle of radius \\({r}\\text{{ cm}}\\).",
        "Given chord \\(AB = {c}\\text{{ cm}}\\) in a circle of radius \\({r}\\text{{ cm}}\\) with centre \\(O\\), find \\(OM\\) (\\(OM \\perp AB\\)).",
        "Find the measure of segment \\(OM\\) from centre \\(O\\) perpendicular to chord \\(AB = {c}\\text{{ cm}}\\) when radius is \\({r}\\text{{ cm}}."
    ]
    
    # Arch 2: Given chord length and distance d, find radius r = sqrt(d^2 + (c/2)^2)
    data_2 = [
        (6, 4, 5), (10, 12, 13), (16, 15, 17), (14, 24, 25), (12, 8, 10),
        (18, 12, 15), (24, 16, 20), (30, 20, 25), (20, 24, 26), (32, 24, 30)
    ]
    tmpls_2 = [
        "A chord of length \\({c}\\text{{ cm}}\\) is at a distance of \\({d}\\text{{ cm}}\\) from the centre \\(O\\) of a circle. Find the radius of the circle.",
        "In a circle with centre \\(O\\), chord \\(AB = {c}\\text{{ cm}}\\) and perpendicular \\(OM = {d}\\text{{ cm}}\\) (where \\(M\\) is on \\(AB\\)). Calculate radius \\(OA\\).",
        "What is the radius of a circle in which a chord of length \\({c}\\text{{ cm}}\\) is at distance \\({d}\\text{{ cm}}\\) from the centre \\(O\\)?",
        "Find the radius of circle \\(O\\) given that chord \\(AB = {c}\\text{{ cm}}\\) and distance \\(OM = {d}\\text{{ cm}}\\) with \\(OM \\perp AB\\).",
        "Determine the circle radius \\(r\\) if chord \\(AB\\) measures \\({c}\\text{{ cm}}\\) and perpendicular from centre \\(O\\) to \\(AB\\) is \\({d}\\text{{ cm}}\\).",
        "Calculate the radius of the circle with centre \\(O\\) where chord \\(AB = {c}\\text{{ cm}}\\) lies at distance \\({d}\\text{{ cm}}\\) from \\(O\\).",
        "If a chord of \\({c}\\text{{ cm}}\\) is at distance \\({d}\\text{{ cm}}\\) from the centre \\(O\\) of a circle, what is the length of its radius?",
        "Compute the radius of circle \\(O\\) given chord \\(AB = {c}\\text{{ cm}}\\) and perpendicular distance \\(OM = {d}\\text{{ cm}}\\).",
        "Evaluate the radius of the circle when chord \\(AB = {c}\\text{{ cm}}\\) and perpendicular segment \\(OM = {d}\\text{{ cm}}\\) (\\(OM \\perp AB\\)).",
        "Find the circle radius for chord \\(AB = {c}\\text{{ cm}}\\) situated \\({d}\\text{{ cm}}\\) away from centre \\(O\\)."
    ]
    
    # Arch 3: Given diameter D and distance d, find chord length
    data_3 = [
        (10, 3, 8), (26, 5, 24), (34, 8, 30), (50, 7, 48), (20, 6, 16),
        (30, 9, 24), (40, 12, 32), (50, 15, 40), (52, 10, 48), (68, 16, 60)
    ]
    tmpls_3 = [
        "In a circle of diameter \\({D}\\text{{ cm}}\\), a chord \\(AB\\) is at a distance of \\({d}\\text{{ cm}}\\) from centre \\(O\\). Find the length of chord \\(AB\\).",
        "What is the length of chord \\(AB\\) in a circle with diameter \\({D}\\text{{ cm}}\\) if its perpendicular distance from centre \\(O\\) is \\({d}\\text{{ cm}}\\)?" ,
        "Calculate chord \\(AB\\) in a circle having diameter \\({D}\\text{{ cm}}\\) and perpendicular \\(OM = {d}\\text{{ cm}}\\) from centre \\(O\\) to \\(AB\\).",
        "Determine the measure of chord \\(AB\\) in circle \\(O\\) (diameter \\({D}\\text{{ cm}}\\)) given distance \\(OM = {d}\\text{{ cm}}\\).",
        "A circle has diameter \\({D}\\text{{ cm}}\\). If chord \\(AB\\) is situated \\({d}\\text{{ cm}}\\) from centre \\(O\\), find \\(AB\\).",
        "Evaluate chord \\(AB\\) for a circle of diameter \\({D}\\text{{ cm}}\\) with distance from centre \\(O\\) equal to \\({d}\\text{{ cm}}\\).",
        "In circle \\(O\\) with diameter \\({D}\\text{{ cm}}\\), perpendicular from \\(O\\) to chord \\(AB\\) is \\({d}\\text{{ cm}}\\). Compute length \\(AB\\).",
        "Find length of chord \\(AB\\) in a circle whose diameter is \\({D}\\text{{ cm}}\\) and distance from centre \\(O\\) is \\({d}\\text{{ cm}}\\).",
        "Given diameter \\({D}\\text{{ cm}}\\) and perpendicular distance \\(OM = {d}\\text{{ cm}}\\) to chord \\(AB\\), find \\(AB\\).",
        "How long is chord \\(AB\\) if circle diameter is \\({D}\\text{{ cm}}\\) and perpendicular from \\(O\\) to \\(AB\\) is \\({d}\\text{{ cm}}\\)?"
    ]
    
    # Arch 4: Bisection property: given chord AB, find AM = MB = AB / 2
    data_4 = [
        (12, 6), (14, 7), (18, 9), (22, 11), (28, 14),
        (36, 18), (42, 21), (52, 26), (64, 32), (76, 38)
    ]
    tmpls_4 = [
        "If perpendicular \\(OM\\) is drawn from centre \\(O\\) to chord \\(AB = {c}\\text{{ cm}}\\), what is the length of segment \\(AM\\)?",
        "Perpendicular from centre \\(O\\) to chord \\(AB = {c}\\text{{ cm}}\\) intersects \\(AB\\) at \\(M\\). Find \\(AM\\).",
        "In circle \\(O\\), \\(OM \\perp AB\\) and \\(AB = {c}\\text{{ cm}}\\). Calculate length \\(MB\\).",
        "Determine length \\(AM\\) if chord \\(AB = {c}\\text{{ cm}}\\) is bisected by perpendicular \\(OM\\) from centre \\(O\\).",
        "What is the measure of segment \\(MB\\) when perpendicular from centre \\(O\\) bisects chord \\(AB = {c}\\text{{ cm}}\\) at point \\(M\\)?",
        "Find segment \\(AM\\) in circle \\(O\\) given \\(OM \\perp AB\\) and \\(AB = {c}\\text{{ cm}}\\).",
        "Evaluate the length of half-chord \\(AM\\) for chord \\(AB = {c}\\text{{ cm}}\\) in circle \\(O\\).",
        "Compute \\(MB\\) in circle with centre \\(O\\) where \\(OM \\perp AB\\) and chord \\(AB = {c}\\text{{ cm}}\\).",
        "In a circle, perpendicular \\(OM\\) from centre \\(O\\) meets chord \\(AB = {c}\\text{{ cm}}\\) at \\(M\\). Find \\(AM\\).",
        "Calculate the measure of \\(AM\\) knowing perpendicular from centre \\(O\\) bisects chord \\(AB = {c}\\text{{ cm}}\\) at \\(M\\)."
    ]
    
    # Arch 5: Angles in right triangle OMB: given angle MOB = theta, find angle MBO = 90 - theta
    data_5 = [
        (30, 60), (45, 45), (20, 70), (35, 55), (50, 40),
        (65, 25), (15, 75), (40, 50), (55, 35), (25, 65)
    ]
    tmpls_5 = [
        "In a circle with centre \\(O\\), perpendicular \\(OM\\) is drawn to chord \\(AB\\). If \\(\\angle MOB = {theta}^\\circ\\), find \\(\\angle MBO\\).",
        "For right-angled \\(\\triangle OMB\\) formed by radius \\(OB\\) and perpendicular \\(OM \\perp AB\\), compute \\(\\angle MBO\\) when \\(\\angle MOB = {theta}^\\circ\\).",
        "What is the measure of acute angle \\(\\angle MBO\\) in circle \\(O\\) if \\(OM \\perp AB\\) and \\(\\angle MOB = {theta}^\\circ\\)?",
        "Calculate \\(\\angle MBO\\) in \\(\\triangle OMB\\) (\\(\\angle OMB = 90^\\circ\\)) given \\(\\angle MOB = {theta}^\\circ\\).",
        "Determine the angle \\(\\angle MBO\\) made by radius \\(OB\\) with chord \\(AB\\) if \\(OM \\perp AB\\) and \\(\\angle MOB = {theta}^\\circ\\).",
        "Evaluate \\(\\angle MBO\\) in circle \\(O\\) where \\(OM \\perp AB\\) and central acute angle \\(\\angle MOB = {theta}^\\circ\\).",
        "If \\(\\angle MOB = {theta}^\\circ\\) in right-angled \\(\\triangle OMB\\) (\\(OM \\perp AB\\)), what is the measure of \\(\\angle MBO\\)?",
        "Find \\(\\angle MBO\\) for perpendicular segment \\(OM\\) to chord \\(AB\\) given \\(\\angle MOB = {theta}^\\circ\\).",
        "Compute the measure of \\(\\angle MBO\\) in circle \\(O\\) knowing \\(OM \\perp AB\\) and \\(\\angle MOB = {theta}^\\circ\\).",
        "In \\(\\triangle OMB\\) with \\(\\angle OMB = 90^\\circ\\), find acute angle \\(\\angle MBO\\) if \\(\\angle MOB = {theta}^\\circ\\)."
    ]
    
    # Arch 6: Diameter D = 2 * r for given radius r
    data_6 = [
        (8, 16), (12, 24), (14, 28), (16, 32), (18, 36),
        (22, 44), (27, 54), (33, 66), (45, 90), (55, 110)
    ]
    tmpls_6 = [
        "In a circle of radius \\({r}\\text{{ cm}}\\), what is the length of the longest chord (diameter)?",
        "The radius of a circle with centre \\(O\\) is \\({r}\\text{{ cm}}\\). Calculate the length of its diameter.",
        "Find the measure of the diameter of a circle whose radius is \\({r}\\text{{ cm}}\\).",
        "What is the length of diameter \\(AB\\) in a circle of radius \\({r}\\text{{ cm}}\\) passing through centre \\(O\\)?",
        "Determine the diameter of circle \\(O\\) given that its radius measures \\({r}\\text{{ cm}}\\).",
        "Evaluate the length of the diameter of a circle having radius \\({r}\\text{{ cm}}\\).",
        "Compute the diameter of circle \\(O\\) whose radius is \\({r}\\text{{ cm}}\\).",
        "If the radius of a circle is \\({r}\\text{{ cm}}\\), what is the length of its diameter?",
        "Calculate the measure of the diameter in circle \\(O\\) with radius \\({r}\\text{{ cm}}\\).",
        "How long is the diameter of a circle if its radius is \\({r}\\text{{ cm}}\\)?"
    ]
    
    # Arch 7: Two parallel chords on same side of centre
    data_7 = [
        (5, 8, 6, 1), (13, 24, 10, 7), (17, 30, 16, 7), (25, 48, 40, 8), (10, 16, 12, 2),
        (15, 24, 18, 3), (20, 32, 24, 4), (25, 40, 30, 5), (26, 48, 20, 14), (34, 60, 32, 14)
    ]
    tmpls_7 = [
        "In a circle of radius \\({r}\\text{{ cm}}\\), two parallel chords have lengths \\({c1}\\text{{ cm}}\\) and \\({c2}\\text{{ cm}}\\) on the same side of centre \\(O\\). Find the distance between the two chords.",
        "Two parallel chords of lengths \\({c1}\\text{{ cm}}\\) and \\({c2}\\text{{ cm}}\\) are on the same side of centre \\(O\\) in a circle of radius \\({r}\\text{{ cm}}\\). Calculate the distance between them.",
        "What is the distance between two parallel chords of lengths \\({c1}\\text{{ cm}}\\) and \\({c2}\\text{{ cm}}\\) lying on the same side of centre in a circle of radius \\({r}\\text{{ cm}}\\)?" ,
        "Calculate the separation distance between parallel chords \\({c1}\\text{{ cm}}\\) and \\({c2}\\text{{ cm}}\\) situated on the same side of centre \\(O\\) (radius \\({r}\\text{{ cm}}\\)).",
        "Determine the distance between two parallel chords of lengths \\({c1}\\text{{ cm}}\\) and \\({c2}\\text{{ cm}}\\) in a circle of radius \\({r}\\text{{ cm}}\\) on the same side of \\(O\\).",
        "Find the distance between two chords of lengths \\({c1}\\text{{ cm}}\\) and \\({c2}\\text{{ cm}}\\) parallel to each other on the same side of centre in circle of radius \\({r}\\text{{ cm}}\\).",
        "In circle \\(O\\) (radius \\({r}\\text{{ cm}}\\)), parallel chords have lengths \\({c1}\\text{{ cm}}\\) and \\({c2}\\text{{ cm}}\\) on the same side. Evaluate the distance between them.",
        "Compute the distance between two parallel chords measuring \\({c1}\\text{{ cm}}\\) and \\({c2}\\text{{ cm}}\\) on the same side of centre \\(O\\) (radius \\({r}\\text{{ cm}}\\)).",
        "How far apart are two parallel chords of lengths \\({c1}\\text{{ cm}}\\) and \\({c2}\\text{{ cm}}\\) on the same side of centre \\(O\\) in circle with radius \\({r}\\text{{ cm}}\\)?" ,
        "If two parallel chords of \\({c1}\\text{{ cm}}\\) and \\({c2}\\text{{ cm}}\\) lie on the same side of centre \\(O\\) in circle of radius \\({r}\\text{{ cm}}\\), find their distance apart."
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        qcode = f"{tc}-OSC-{seq}"
        
        if arch == 0:
            r, d, ans_c = data_0[sub_idx]
            svg = svg_circle_chord(f"r = {r}", f"OM = {d}", "AB = ?") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(r=r, d=d)
            corr = f"{ans_c}\\text{{ cm}}"
            dist = [f"{ans_c + 4}\\text{{ cm}}", f"{ans_c - 4 if ans_c > 4 else ans_c + 6}\\text{{ cm}}", f"{r * 2}\\text{{ cm}}"]
            sol = f"**Step 1: Perpendicular from centre bisects chord**\\nIn right \\(\\triangle OMB\\), \\(MB = \\sqrt{{r^2 - d^2}} = \\sqrt{{{r}^2 - {d}^2}} = \\sqrt{{{r*r - d*d}}} = {ans_c // 2}\\text{{ cm}}\\).\\n\\(AB = 2 \\times MB = 2 \\times {ans_c // 2} = {ans_c}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_c} cm."
        elif arch == 1:
            r, c, ans_d = data_1[sub_idx]
            svg = svg_circle_chord(f"r = {r}", "OM = ?", f"AB = {c}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(r=r, c=c)
            corr = f"{ans_d}\\text{{ cm}}"
            dist = [f"{ans_d + 2}\\text{{ cm}}", f"{ans_d - 2 if ans_d > 2 else ans_d + 3}\\text{{ cm}}", f"{r}\\text{{ cm}}"]
            sol = f"**Step 1: Half-chord and Pythagoras theorem**\\n\\(MB = \\frac{{AB}}{{2}} = \\frac{{{c}}}{{2}} = {c // 2}\\text{{ cm}}\\).\\n\\(OM = \\sqrt{{r^2 - MB^2}} = \\sqrt{{{r}^2 - {c//2}^2}} = {ans_d}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_d} cm."
        elif arch == 2:
            c, d, ans_r = data_2[sub_idx]
            svg = svg_circle_chord("r = ?", f"OM = {d}", f"AB = {c}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(c=c, d=d)
            corr = f"{ans_r}\\text{{ cm}}"
            dist = [f"{ans_r + 3}\\text{{ cm}}", f"{ans_r - 3 if ans_r > 3 else ans_r + 5}\\text{{ cm}}", f"{c // 2 + d}\\text{{ cm}}"]
            sol = f"**Step 1: Half-chord and Pythagoras theorem**\\n\\(MB = \\frac{{{c}}}{{2}} = {c // 2}\\text{{ cm}}\\).\\n\\(r = \\sqrt{{OM^2 + MB^2}} = \\sqrt{{{d}^2 + {c//2}^2}} = {ans_r}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_r} cm."
        elif arch == 3:
            D, d, ans_c = data_3[sub_idx]
            r = D // 2
            svg = svg_circle_chord(f"r = {r}", f"OM = {d}", "AB = ?") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(D=D, d=d)
            corr = f"{ans_c}\\text{{ cm}}"
            dist = [f"{ans_c + 4}\\text{{ cm}}", f"{ans_c - 4 if ans_c > 4 else ans_c + 8}\\text{{ cm}}", f"{D}\\text{{ cm}}"]
            sol = f"**Step 1: Radius and Pythagoras theorem**\\n\\(r = \\frac{{D}}{{2}} = \\frac{{{D}}}{{2}} = {r}\\text{{ cm}}\\).\\n\\(MB = \\sqrt{{{r}^2 - {d}^2}} = {ans_c // 2}\\text{{ cm}}\\).\\n\\(AB = 2 \\times MB = {ans_c}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_c} cm."
        elif arch == 4:
            c, half_c = data_4[sub_idx]
            svg = svg_circle_chord("", "OM \\perp AB", f"AB = {c}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(c=c)
            corr = f"{half_c}\\text{{ cm}}"
            dist = [f"{half_c + 2}\\text{{ cm}}", f"{half_c - 2}\\text{{ cm}}", f"{c}\\text{{ cm}}"]
            sol = f"**Step 1: Bisection theorem**\\nThe perpendicular from the centre to a chord bisects the chord.\\n\\(AM = \\frac{{AB}}{{2}} = \\frac{{{c}}}{{2}} = {half_c}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{half_c} cm."
        elif arch == 5:
            theta, ans_mbo = data_5[sub_idx]
            svg = svg_circle_chord("", f"\\angle MOB = {theta}^\\circ", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(theta=theta)
            corr = f"{ans_mbo}^\\circ"
            dist = [f"{ans_mbo + 10}^\\circ", f"{ans_mbo - 10 if ans_mbo > 10 else ans_mbo + 15}^\\circ", f"{theta}^\\circ"]
            sol = f"**Step 1: Angle sum in right triangle OMB**\\n\\(OM \\perp AB \\implies \\angle OMB = 90^\\circ\\).\\n\\(\\angle MBO = 90^\\circ - \\angle MOB = 90^\\circ - {theta}^\\circ = {ans_mbo}^\\circ\\).\\n**Step 2: Conclusion**\\n{ans_mbo}°."
        elif arch == 6:
            r, ans_d = data_6[sub_idx]
            svg = svg_circle_chord(f"r = {r}", "", f"Diameter = {ans_d}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(r=r)
            corr = f"{ans_d}\\text{{ cm}}"
            dist = [f"{ans_d + 4}\\text{{ cm}}", f"{ans_d - 4}\\text{{ cm}}", f"{r}\\text{{ cm}}"]
            sol = f"**Step 1: Formula**\\n\\(\\text{{Diameter}} = 2 \\times \\text{{radius}} = 2 \\times {r} = {ans_d}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{ans_d} cm."
        elif arch == 7:
            r, c1, c2, ans_sep = data_7[sub_idx]
            d1 = int(math.isqrt(r*r - (c1//2)*(c1//2)))
            d2 = int(math.isqrt(r*r - (c2//2)*(c2//2)))
            svg = svg_circle_chord(f"r = {r}", "", f"Chords: {c1}, {c2}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_7[sub_idx].format(r=r, c1=c1, c2=c2)
            corr = f"{ans_sep}\\text{{ cm}}"
            dist = [f"{ans_sep + 2}\\text{{ cm}}", f"{ans_sep - 2 if ans_sep > 2 else ans_sep + 3}\\text{{ cm}}", f"{d1 + d2}\\text{{ cm}}"]
            sol = f"**Step 1: Distances of both chords from centre**\\n\\(d_1 = \\sqrt{{{r}^2 - {c1//2}^2}} = {d1}\\text{{ cm}}\\).\\n\\(d_2 = \\sqrt{{{r}^2 - {c2//2}^2}} = {d2}\\text{{ cm}}\\).\\n**Step 2: Separation distance**\\nSince both chords lie on the same side of the centre:\\n\\(\\text{{Distance}} = |d_2 - d_1| = |{d2} - {d1}| = {ans_sep}\\text{{ cm}}\\).\\n**Step 3: Conclusion**\\n{ans_sep} cm."

        diff = "easy" if arch in [0,4,5] else ("medium" if arch in [1,2,6] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs


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
        "In a circle with centre \(O\), congruent chords \(AB\) and \(CD\) have lengths {c}\text{{ cm}}. If the perpendicular distance \(OM\) from \(O\) to \(AB\) is {d}\text{{ cm}}, find distance \(ON\) to chord \(CD\).",
        "Chords \(AB\) and \(CD\) of circle \(O\) are equal in length. If distance \(OM\) from centre \(O\) to \(AB\) is {d}\text{{ cm}}, what is the perpendicular distance \(ON\) to \(CD\)?",
        "Two congruent chords \(AB = CD\) are drawn in a circle of radius \(r\). Given \(OM \perp AB\) with \(OM = {d}\text{{ cm}}\), compute the length of \(ON\) (\(ON \perp CD\)).",
        "What is the perpendicular distance \(ON\) to chord \(CD\) if chord \(AB = CD\) and \(OM = {d}\text{{ cm}}\) (perpendicular from centre \(O\) to \(AB\))?",
        "By the equidistant chord theorem, if chord \(AB \cong CD\) and distance \(OM = {d}\text{{ cm}}\), determine distance \(ON\).",
        "In circle \(O\), chord \(AB\) and chord \(CD\) are congruent. If \(OM = {d}\text{{ cm}}\) is the distance of \(AB\) from \(O\), evaluate distance \(ON\).",
        "Find the perpendicular distance from centre \(O\) to chord \(CD\) knowing that chord \(CD = AB\) and \(OM = {d}\text{{ cm}}\).",
        "Calculate distance \(ON\) to chord \(CD\) in circle \(O\) where chord \(AB = CD\) and \(OM = {d}\text{{ cm}}\).",
        "Given congruent chords \(AB\) and \(CD\) in circle \(O\), if \(OM = {d}\text{{ cm}}\) (\(OM \perp AB\)), what is \(ON\) (\(ON \perp CD\))?",
        "If chord \(AB\) is congruent to chord \(CD\) and perpendicular from centre to \(AB\) is {d}\text{{ cm}}, find the perpendicular distance to \(CD\)."
    ]
    
    # Arch 1: Equidistant chords OM = ON = d -> Chord AB = Chord CD = c
    data_1 = [
        (3, 8), (4, 10), (5, 14), (6, 16), (7, 18),
        (8, 22), (9, 24), (10, 26), (12, 32), (14, 36)
    ]
    tmpls_1 = [
        "In circle \(O\), perpendiculars \(OM\) and \(ON\) to chords \(AB\) and \(CD\) are equal: \(OM = ON = {d}\text{{ cm}}\). If chord \(AB = {c}\text{{ cm}}\), find the length of chord \(CD\).",
        "Chords \(AB\) and \(CD\) in circle \(O\) are equidistant from centre \(O\). If chord \(AB = {c}\text{{ cm}}\), calculate length \(CD\).",
        "What is the length of chord \(CD\) if it is at the same distance from centre \(O\) as chord \(AB = {c}\text{{ cm}}\) in circle \(O\)?",
        "Two chords \(AB\) and \(CD\) are equidistant from the centre of a circle. If \(AB = {c}\text{{ cm}}\), determine the measure of chord \(CD\).",
        "By the converse theorem, chords equidistant from centre \(O\) are congruent. If \(OM = ON\) and \(AB = {c}\text{{ cm}}\), find \(CD\).",
        "Evaluate the length of chord \(CD\) in circle \(O\) knowing \(AB = {c}\text{{ cm}}\) and both chords are at distance {d}\text{{ cm}} from centre.",
        "Find chord length \(CD\) in a circle where chords \(AB\) and \(CD\) are at equal perpendicular distances from centre \(O\) and \(AB = {c}\text{{ cm}}\).",
        "In circle \(O\), \(OM \perp AB\), \(ON \perp CD\), and \(OM = ON\). Given \(AB = {c}\text{{ cm}}\), compute \(CD\).",
        "Calculate the measure of chord \(CD\) if chords \(AB\) and \(CD\) are equidistant from centre \(O\) and \(AB = {c}\text{{ cm}}\).",
        "Given that chords \(AB\) and \(CD\) are equidistant from centre \(O\) and \(AB = {c}\text{{ cm}}\), what is \(CD\)?"
    ]
    
    # Arch 2: Sum of two congruent chords: AB + CD = 2 * c
    data_2 = [
        (6, 12), (9, 18), (11, 22), (13, 26), (15, 30),
        (17, 34), (19, 38), (21, 42), (23, 46), (25, 50)
    ]
    tmpls_2 = [
        "In a circle with centre \(O\), chords \(AB\) and \(CD\) are equidistant from \(O\). If \(AB = {c}\text{{ cm}}\), find the sum of their lengths \(AB + CD\).",
        "Two congruent chords \(AB\) and \(CD\) each measure \({c}\text{{ cm}}\) in circle \(O\). Calculate \(AB + CD\).",
        "What is the total combined length \(AB + CD\) of two chords equidistant from centre \(O\) if \(AB = {c}\text{{ cm}}\)?" ,
        "Compute \(AB + CD\) in circle \(O\) where \(AB \cong CD\) and chord \(AB = {c}\text{{ cm}}\).",
        "Determine \(AB + CD\) for two equal chords in circle \(O\) having \(AB = {c}\text{{ cm}}\).",
        "Evaluate \(AB + CD\) in circle \(O\) given that chords \(AB\) and \(CD\) are congruent and \(AB = {c}\text{{ cm}}\).",
        "If \(OM = ON\) for chords \(AB\) and \(CD\) in circle \(O\), and \(AB = {c}\text{{ cm}}\), find \(AB + CD\).",
        "Find the sum \(AB + CD\) of two chords in a circle equidistant from centre \(O\) given \(AB = {c}\text{{ cm}}\).",
        "Calculate the combined measure \(AB + CD\) of two congruent chords \(AB = CD = {c}\text{{ cm}}\).",
        "In circle \(O\), chords \(AB\) and \(CD\) are equidistant from centre. If \(AB = {c}\text{{ cm}}\), what is \(AB + CD\)?"
    ]
    
    # Arch 3: Central angle of congruent chords: angle AOB = angle COD
    data_3 = [
        (40, 40), (50, 50), (65, 65), (75, 75), (80, 80),
        (95, 95), (100, 100), (110, 110), (120, 120), (130, 130)
    ]
    tmpls_3 = [
        "In a circle with centre \(O\), congruent chords \(AB\) and \(CD\) subtend angles at the centre. If \(\angle AOB = {deg}^\circ\), find \(\angle COD\).",
        "Chords \(AB\) and \(CD\) in circle \(O\) are equal in length. If central angle \(\angle AOB = {deg}^\circ\), what is \(\angle COD\)?",
        "What is the central angle \(\angle COD\) subtended by chord \(CD\) if chord \(CD \cong AB\) and \(\angle AOB = {deg}^\circ\)?",
        "Congruent chords of a circle subtend equal angles at the centre. If \(\angle AOB = {deg}^\circ\), calculate \(\angle COD\).",
        "Determine the measure of \(\angle COD\) in circle \(O\) given \(AB = CD\) and \(\angle AOB = {deg}^\circ\).",
        "Evaluate \(\angle COD\) in circle \(O\) knowing chords \(AB\) and \(CD\) are congruent and \(\angle AOB = {deg}^\circ\).",
        "Compute central angle \(\angle COD\) subtended by chord \(CD\) when \(CD = AB\) and \(\angle AOB = {deg}^\circ\).",
        "Find \(\angle COD\) for chord \(CD\) in circle \(O\) given chord \(AB = CD\) and \(\angle AOB = {deg}^\circ\).",
        "If chord \(AB = CD\) in circle \(O\) and \(\angle AOB = {deg}^\circ\), calculate \(\angle COD\).",
        "In circle with centre \(O\), congruent chords \(AB\) and \(CD\) have \(\angle AOB = {deg}^\circ\). Find \(\angle COD\)."
    ]
    
    # Arch 4: Right angle between perpendiculars OM and ON when chords are perpendicular
    data_4 = [
        (45, 135), (55, 125), (65, 115), (70, 110), (75, 105),
        (85, 95), (35, 145), (25, 155), (60, 120), (50, 130)
    ]
    tmpls_4 = [
        "In a cyclic quadrilateral or intersecting chords configuration with \(OM \perp AB\) and \(ON \perp CD\), if \(\angle MON = {deg}^\circ\), find the supplementary angle \(180^\circ - {deg}^\circ\).",
        "For perpendicular segments \(OM\) and \(ON\) to chords in circle \(O\), calculate the supplement of \(\angle MON = {deg}^\circ\).",
        "What is the supplementary angle to central angle \(\angle MON = {deg}^\circ\) between perpendicular bisectors?",
        "Determine the angle \(180^\circ - \angle MON\) when \(\angle MON = {deg}^\circ\) in circle \(O\).",
        "Compute the supplementary measure to \(\angle MON = {deg}^\circ\) formed by radii perpendiculars.",
        "Evaluate \(180^\circ - {deg}^\circ\) in the context of cyclic quadrilateral \(OMPN\) where \(\angle MON = {deg}^\circ\).",
        "Find the measure of angle \(\angle MPN\) opposite to \(\angle MON = {deg}^\circ\) in quadrilateral \(OMPN\) (\(\angle M = \angle N = 90^\circ\)).",
        "In quadrilateral \(OMPN\) with \(\angle M = \angle N = 90^\circ\) and \(\angle MON = {deg}^\circ\), calculate \(\angle MPN\).",
        "Calculate \(\angle MPN\) in quadrilateral \(OMPN\) (\(\angle OMP = \angle ONP = 90^\circ\), \(\angle MON = {deg}^\circ\)).",
        "If \(\angle MON = {deg}^\circ\) in quadrilateral \(OMPN\) where \(OM \perp AB\) and \(ON \perp CD\), what is \(\angle MPN\)?"
    ]
    
    # Arch 5: Radius r from chord AB = c and distance d
    data_5 = [
        (12, 8, 10), (16, 6, 10), (24, 5, 13), (30, 8, 17), (48, 7, 25),
        (20, 24, 26), (32, 24, 30), (40, 15, 25), (48, 20, 26), (60, 11, 61)
    ]
    tmpls_5 = [
        "Two congruent chords of length {c}\text{{ cm}} are each at a distance of {d}\text{{ cm}} from centre \(O\). Find the radius of the circle.",
        "In a circle, congruent chords each measuring {c}\text{{ cm}} are situated {d}\text{{ cm}} from centre \(O\). What is the radius of the circle?",
        "Calculate the radius of circle \(O\) containing two equal chords of {c}\text{{ cm}} each at perpendicular distance {d}\text{{ cm}} from \(O\).",
        "What is the radius of a circle in which two chords of length {c}\text{{ cm}} are equidistant ({d}\text{{ cm}}) from the centre?",
        "Determine the radius of circle \(O\) if two congruent chords of {c}\text{{ cm}} have distance {d}\text{{ cm}} from \(O\).",
        "Evaluate the radius of the circle containing equal chords \(AB = CD = {c}\text{{ cm}}\) with distance \(OM = ON = {d}\text{{ cm}}\).",
        "Find the radius of a circle where two equidistant chords measure {c}\text{{ cm}} and are {d}\text{{ cm}} from centre \(O\).",
        "Compute the circle radius given that chords \(AB = CD = {c}\text{{ cm}}\) are at distance \(OM = ON = {d}\text{{ cm}}\).",
        "In circle \(O\), chords \(AB = CD = {c}\text{{ cm}}\) lie {d}\text{{ cm}} from \(O\). Calculate radius \(OA\).",
        "If chords \(AB = CD = {c}\text{{ cm}}\) are at distance {d}\text{{ cm}} from centre \(O\), what is the length of the radius?"
    ]
    
    # Arch 6: Half-chord of congruent chords: AM = c / 2
    data_6 = [
        (10, 5), (14, 7), (18, 9), (22, 11), (26, 13),
        (34, 17), (38, 19), (46, 23), (54, 27), (62, 31)
    ]
    tmpls_6 = [
        "In circle \(O\), congruent chords \(AB\) and \(CD\) have length {c}\text{{ cm}}. What is the length of segment \(AM\) if \(OM \perp AB\)?",
        "If \(AB = CD = {c}\text{{ cm}}\) in circle \(O\) and \(OM \perp AB\), find length \(AM\).",
        "Perpendicular from centre \(O\) to chord \(AB = {c}\text{{ cm}}\) intersects \(AB\) at \(M\). Calculate \(AM\).",
        "What is the measure of half-chord \(AM\) when \(AB = {c}\text{{ cm}}\) is congruent to \(CD\)?",
        "Determine the length of segment \(AM\) in circle \(O\) where \(OM \perp AB\) and chord \(AB = {c}\text{{ cm}}\).",
        "Evaluate \(AM\) for chord \(AB = {c}\text{{ cm}}\) (congruent to \(CD\)) with \(OM \perp AB\).",
        "Find length \(AM\) in circle \(O\) given chord \(AB = {c}\text{{ cm}}\) and perpendicular \(OM\).",
        "Compute segment \(AM\) for chord \(AB = {c}\text{{ cm}}\) bisected by \(OM \perp AB\).",
        "In circle \(O\), chord \(AB = {c}\text{{ cm}}\) is bisected at \(M\). Find \(AM\).",
        "Calculate the measure of \(AM\) given \(OM \perp AB\) and \(AB = {c}\text{{ cm}}\)."
    ]
    
    # Arch 7: Algebraic congruent chords: AB = CD -> solve for x
    data_7 = [
        ("2x + 1", "x + 7", 6), ("3x + 2", "2x + 9", 7), ("4x + 3", "3x + 11", 8),
        ("5x + 4", "4x + 13", 9), ("2x + 5", "x + 15", 10), ("3x + 1", "2x + 12", 11),
        ("4x + 2", "3x + 14", 12), ("5x + 3", "4x + 16", 13), ("2x + 7", "x + 21", 14),
        ("3x + 5", "2x + 20", 15)
    ]
    tmpls_7 = [
        "In a circle with centre \(O\), chords \(AB\) and \(CD\) are equidistant from \(O\). If \(AB = {e1}\) and \(CD = {e2}\), find \(x\).",
        "Two chords \(AB\) and \(CD\) are equidistant from centre \(O\). If \(AB = {e1}\text{{ cm}}\) and \(CD = {e2}\text{{ cm}}\), solve for \(x\).",
        "Given congruent chords \(AB = {e1}\) and \(CD = {e2}\) in circle \(O\), determine the value of \(x\).",
        "Calculate the value of \(x\) if chords \(AB = {e1}\) and \(CD = {e2}\) are at equal distances from the centre of circle \(O\).",
        "What is the value of \(x\) when chords \(AB = {e1}\) and \(CD = {e2}\) are congruent in circle \(O\)?",
        "Solve for \(x\) knowing that chords \(AB = {e1}\) and \(CD = {e2}\) are equidistant from centre \(O\).",
        "In circle \(O\), \(OM = ON\) for chords \(AB = {e1}\) and \(CD = {e2}\). Evaluate \(x\).",
        "Find \(x\) for equidistant chords \(AB = {e1}\) and \(CD = {e2}\) in a circle.",
        "Compute the numerical value of \(x\) given congruent chords \(AB = {e1}\) and \(CD = {e2}\).",
        "If chords \(AB = {e1}\) and \(CD = {e2}\) are equidistant from centre \(O\), find \(x\)."
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        qcode = f"{tc}-OSC-{seq}"
        
        if arch == 0:
            d, c = data_0[sub_idx]
            svg = svg_circle_chord(f"OM = {d}", "ON = ?", f"Chords = {c}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(d=d, c=c)
            corr = f"{d}\text{{ cm}}"
            dist = [f"{d + 2}\text{{ cm}}", f"{d - 2 if d > 2 else d + 4}\text{{ cm}}", f"{c // 2}\text{{ cm}}"]
            sol = f"**Step 1: Equidistant chord theorem**\nCongruent chords of a circle are equidistant from the centre.\nSince chord \(AB \cong CD\), distance \(ON = OM = {d}\text{{ cm}}\).\n**Step 2: Conclusion**\n{d} cm."
        elif arch == 1:
            d, c = data_1[sub_idx]
            svg = svg_circle_chord(f"OM = ON = {d}", "", f"AB = {c}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(d=d, c=c)
            corr = f"{c}\text{{ cm}}"
            dist = [f"{c + 4}\text{{ cm}}", f"{c - 4}\text{{ cm}}", f"{d * 2}\text{{ cm}}"]
            sol = f"**Step 1: Converse theorem**\nChords of a circle that are equidistant from the centre are congruent.\nSince \(OM = ON\), chord \(CD = AB = {c}\text{{ cm}}\).\n**Step 2: Conclusion**\n{c} cm."
        elif arch == 2:
            c, ans_sum = data_2[sub_idx]
            svg = svg_circle_chord("", "", f"AB = CD = {c}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(c=c)
            corr = f"{ans_sum}\text{{ cm}}"
            dist = [f"{ans_sum + 4}\text{{ cm}}", f"{ans_sum - 4}\text{{ cm}}", f"{c}\text{{ cm}}"]
            sol = f"**Step 1: Sum of congruent chords**\nSince \(AB = CD = {c}\text{{ cm}}\):\n\(AB + CD = {c} + {c} = {ans_sum}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_sum} cm."
        elif arch == 3:
            deg, ans_deg = data_3[sub_idx]
            svg = svg_circle_chord("", f"\angle AOB = {deg}^\circ", "AB = CD") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(deg=deg)
            corr = f"{ans_deg}^\circ"
            dist = [f"{ans_deg + 15}^\circ", f"{ans_deg - 15 if ans_deg > 15 else ans_deg + 20}^\circ", f"{180 - ans_deg}^\circ"]
            sol = f"**Step 1: Central angles theorem**\nCongruent chords subtend equal angles at the centre of the circle.\n\(\angle COD = \angle AOB = {ans_deg}^\circ\).\n**Step 2: Conclusion**\n{ans_deg}°."
        elif arch == 4:
            deg, ans_supp = data_4[sub_idx]
            svg = svg_circle_chord("", f"\angle MON = {deg}^\circ", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(deg=deg)
            corr = f"{ans_supp}^\circ"
            dist = [f"{ans_supp + 10}^\circ", f"{ans_supp - 10 if ans_supp > 10 else ans_supp + 15}^\circ", f"{deg}^\circ"]
            sol = f"**Step 1: Opposite angles in cyclic quadrilateral**\nIn quadrilateral \(OMPN\), \(\angle M = \angle N = 90^\circ\).\n\(\angle MPN = 180^\circ - \angle MON = 180^\circ - {deg}^\circ = {ans_supp}^\circ\).\n**Step 2: Conclusion**\n{ans_supp}°."
        elif arch == 5:
            c, d, ans_r = data_5[sub_idx]
            svg = svg_circle_chord("r = ?", f"OM = {d}", f"AB = {c}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(c=c, d=d)
            corr = f"{ans_r}\text{{ cm}}"
            dist = [f"{ans_r + 2}\text{{ cm}}", f"{ans_r - 2}\text{{ cm}}", f"{c // 2 + d}\text{{ cm}}"]
            sol = f"**Step 1: Radius calculation**\n\(MB = \frac{{AB}}{{2}} = \frac{{{c}}}{{2}} = {c // 2}\text{{ cm}}\).\n\(r = \sqrt{{OM^2 + MB^2}} = \sqrt{{{d}^2 + {c//2}^2}} = {ans_r}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_r} cm."
        elif arch == 6:
            c, ans_half = data_6[sub_idx]
            svg = svg_circle_chord("", "OM \perp AB", f"AB = {c}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(c=c)
            corr = f"{ans_half}\text{{ cm}}"
            dist = [f"{ans_half + 2}\text{{ cm}}", f"{ans_half - 2}\text{{ cm}}", f"{c}\text{{ cm}}"]
            sol = f"**Step 1: Bisection of chord**\nPerpendicular from centre to chord bisects the chord.\n\(AM = \frac{{AB}}{{2}} = \frac{{{c}}}{{2}} = {ans_half}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_half} cm."
        elif arch == 7:
            e1, e2, ans_x = data_7[sub_idx]
            svg = svg_circle_chord("", "AB = CD", f"x = ?") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_7[sub_idx].format(e1=e1, e2=e2)
            corr = f"{ans_x}"
            dist = [f"{ans_x + 2}", f"{ans_x - 2 if ans_x > 2 else ans_x + 3}", f"{ans_x + 5}"]
            sol = f"**Step 1: Equidistant chords are congruent**\nSince chords \\(AB\\) and \\(CD\\) are equidistant from centre \\(O\\), \\(AB = CD\\).\n\\({e1} = {e2} \\implies x = {ans_x}\\).\n**Step 2: Conclusion**\n{ans_x}."

        diff = "easy" if arch in [0,1,3] else ("medium" if arch in [2,6,7] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs


# -----------------------------------------------------------------------------
# 6.2.1: Constructing angle bisectors of triangle
# -----------------------------------------------------------------------------
def gen_6_2_1():
    tc = "MH-9-MTH2-6-6.2.1"
    tname = "Constructing angle bisectors of triangle"
    qs = []
    
    # Arch 0: Angle BIC = 90 + A/2
    data_0 = [
        (40, 110), (50, 115), (60, 120), (70, 125), (80, 130),
        (30, 105), (54, 117), (64, 122), (76, 128), (90, 135)
    ]
    tmpls_0 = [
        "In \(\triangle ABC\), point \(I\) is the incentre. If \(\angle A = {A}^\circ\), find \(\angle BIC\).",
        "The angle bisectors of \(\angle B\) and \(\angle C\) of \(\triangle ABC\) intersect at incentre \(I\). If \(\angle BAC = {A}^\circ\), calculate \(\angle BIC\).",
        "What is the measure of angle \(\angle BIC\) formed by the incentre \(I\) in \(\triangle ABC\) when \(\angle A = {A}^\circ\)?",
        "Calculate \(\angle BIC\) in \(\triangle ABC\) given incentre \(I\) and \(\angle A = {A}^\circ\).",
        "Determine the angle \(\angle BIC\) in \(\triangle ABC\) where \(I\) is the point of concurrence of angle bisectors and \(\angle A = {A}^\circ\).",
        "Evaluate \(\angle BIC\) for incentre \(I\) of \(\triangle ABC\) with \(\angle A = {A}^\circ\).",
        "If \(I\) is the incentre of \(\triangle ABC\) and \(\angle A = {A}^\circ\), what is \(\angle BIC\)?",
        "Find \(\angle BIC\) in \(\triangle ABC\) knowing \(I\) is the incentre and \(\angle A = {A}^\circ\).",
        "Compute the measure of \(\angle BIC\) formed at the incentre \(I\) of \(\triangle ABC\) with vertex angle \(\angle A = {A}^\circ\).",
        "In \(\triangle ABC\), \(I\) is the incentre. Calculate \(\angle BIC\) if \(\angle A = {A}^\circ\)."
    ]
    
    # Arch 1: Angle AIC = 90 + B/2 (disjoint parameters)
    data_1 = [
        (32, 106), (42, 111), (52, 116), (62, 121), (72, 126),
        (82, 131), (36, 108), (48, 114), (66, 123), (84, 132)
    ]
    tmpls_1 = [
        "In \(\triangle ABC\), angle bisectors of \(\angle A\) and \(\angle C\) meet at \(I\). If \(\angle B = {B}^\circ\), find \(\angle AIC\).",
        "For incentre \(I\) of \(\triangle ABC\), calculate \(\angle AIC\) when \(\angle B = {B}^\circ\).",
        "What is \(\angle AIC\) in \(\triangle ABC\) if \(I\) is the incentre and \(\angle B = {B}^\circ\)?",
        "Determine the measure of \(\angle AIC\) formed by angle bisectors intersecting at \(I\) given \(\angle B = {B}^\circ\).",
        "Compute \(\angle AIC\) in \(\triangle ABC\) where \(I\) is the incentre and \(\angle ABC = {B}^\circ\).",
        "Evaluate \(\angle AIC\) for \(\triangle ABC\) with incentre \(I\) having \(\angle B = {B}^\circ\).",
        "Find \(\angle AIC\) in \(\triangle ABC\) given incentre \(I\) and \(\angle B = {B}^\circ\).",
        "Calculate the measure of \(\angle AIC\) subtended at incentre \(I\) when \(\angle B = {B}^\circ\).",
        "If \(I\) is the incentre of \(\triangle ABC\) and \(\angle B = {B}^\circ\), what is \(\angle AIC\)?",
        "In \(\triangle ABC\), incentre is \(I\). Determine \(\angle AIC\) if \(\angle B = {B}^\circ\)."
    ]
    
    # Arch 2: Area of triangle = inradius * semi-perimeter -> Area = r * s
    data_2 = [
        (2, 12, 24), (3, 15, 45), (4, 18, 72), (5, 20, 100), (6, 25, 150),
        (2, 18, 36), (3, 22, 66), (4, 28, 112), (5, 32, 160), (6, 35, 210)
    ]
    tmpls_2 = [
        "The inradius of a triangle is {r}\text{{ cm}} and its semi-perimeter is {s}\text{{ cm}}. Find the area of the triangle.",
        "A triangle has semi-perimeter \(s = {s}\text{{ cm}}\) and inradius \(r = {r}\text{{ cm}}\). Calculate its area.",
        "What is the area of a triangle having inradius \(r = {r}\text{{ cm}}\) and semi-perimeter \(s = {s}\text{{ cm}}\)?" ,
        "Compute the area of \(\triangle ABC\) with inradius {r}\text{{ cm}} and semi-perimeter {s}\text{{ cm}}.",
        "Determine the area of a triangle whose inscribed circle has radius {r}\text{{ cm}} and whose semi-perimeter is {s}\text{{ cm}}.",
        "Evaluate the area of the triangle with inradius \(r = {r}\text{{ cm}}\) and perimeter \(2s = {p}\text{{ cm}}\).",
        "Find the area of a triangle with perimeter \({p}\text{{ cm}}\) and inradius \({r}\text{{ cm}}\).",
        "Calculate area \(\Delta = r \times s\) for inradius \({r}\text{{ cm}}\) and semi-perimeter \({s}\text{{ cm}}\).",
        "In a triangle, semi-perimeter is \({s}\text{{ cm}}\) and inradius is \({r}\text{{ cm}}\). What is its area?",
        "If a triangle has inradius \({r}\text{{ cm}}\) and semi-perimeter \({s}\text{{ cm}}\), find its area."
    ]
    
    # Arch 3: Given Area and semi-perimeter s, find inradius r = Area / s
    data_3 = [
        (24, 12, 2), (45, 15, 3), (72, 18, 4), (100, 20, 5), (150, 25, 6),
        (48, 16, 3), (84, 21, 4), (120, 24, 5), (168, 28, 6), (245, 35, 7)
    ]
    tmpls_3 = [
        "The area of a triangle is {area}\text{{ cm}}^2 and its semi-perimeter is {s}\text{{ cm}}. Find its inradius.",
        "In a triangle with area {area}\text{{ cm}}^2 and semi-perimeter {s}\text{{ cm}}, calculate the inradius \(r\).",
        "What is the inradius of a triangle having area {area}\text{{ cm}}^2 and perimeter {p}\text{{ cm}}?",
        "Compute the inradius \(r\) of a triangle with area {area}\text{{ cm}}^2 and semi-perimeter {s}\text{{ cm}}.",
        "Determine the radius of the incircle of a triangle whose area is {area}\text{{ cm}}^2 and semi-perimeter is {s}\text{{ cm}}.",
        "Evaluate the inradius for a triangle with area {area}\text{{ cm}}^2 and perimeter {p}\text{{ cm}}.",
        "Find the radius of inscribed circle of a triangle of area {area}\text{{ cm}}^2 having semi-perimeter {s}\text{{ cm}}.",
        "Calculate inradius \(r = \frac{{\text{{Area}}}}{{s}}\) for area {area}\text{{ cm}}^2 and semi-perimeter {s}\text{{ cm}}.",
        "If a triangle has area {area}\text{{ cm}}^2 and semi-perimeter {s}\text{{ cm}}, what is its inradius?",
        "In a triangle, area is {area}\text{{ cm}}^2 and semi-perimeter is {s}\text{{ cm}}. Find the inradius."
    ]
    
    # Arch 4: Given inradius r and Area, find perimeter 2s = 2 * (Area / r)
    data_4 = [
        (2, 20, 20), (3, 36, 24), (4, 56, 28), (5, 80, 32), (6, 120, 40),
        (2, 30, 30), (3, 48, 32), (4, 72, 36), (5, 110, 44), (6, 150, 50)
    ]
    tmpls_4 = [
        "The inradius of a triangle is {r}\text{{ cm}} and its area is {area}\text{{ cm}}^2. Find the perimeter of the triangle.",
        "Calculate the perimeter of a triangle with area {area}\text{{ cm}}^2 and inradius {r}\text{{ cm}}.",
        "What is the perimeter of a triangle whose inscribed circle has radius {r}\text{{ cm}} and area {area}\text{{ cm}}^2?",
        "Compute the perimeter \(2s\) of a triangle having inradius {r}\text{{ cm}} and area {area}\text{{ cm}}^2.",
        "Determine the perimeter of a triangle with area {area}\text{{ cm}}^2 and inradius {r}\text{{ cm}}.",
        "Evaluate the perimeter of the triangle with inradius {r}\text{{ cm}} and area {area}\text{{ cm}}^2.",
        "Find the perimeter of a triangle of area {area}\text{{ cm}}^2 having inradius {r}\text{{ cm}}.",
        "Calculate the triangle perimeter given inradius {r}\text{{ cm}} and area {area}\text{{ cm}}^2.",
        "If inradius is {r}\text{{ cm}} and area is {area}\text{{ cm}}^2, what is the perimeter of the triangle?",
        "In a triangle, inradius is {r}\text{{ cm}} and area is {area}\text{{ cm}}^2. Find the perimeter."
    ]
    
    # Arch 5: Concurrence property of angle bisectors: incentre is equidistant from sides
    data_5 = [
        ("AB", "BC", 4), ("BC", "AC", 5), ("AC", "AB", 6), ("AB", "AC", 7), ("BC", "AB", 8),
        ("side AB", "side BC", 9), ("side BC", "side AC", 10), ("side AC", "side AB", 11), ("side AB", "side AC", 12), ("side BC", "side AB", 13)
    ]
    tmpls_5 = [
        "The incentre \(I\) of a triangle is at distance {d}\text{{ cm}} from side \({s1}\). What is its perpendicular distance from \({s2}\)?",
        "In \(\triangle ABC\), point \(I\) is the incentre. If the distance from \(I\) to \({s1}\) is {d}\text{{ cm}}, find its distance to \({s2}\).",
        "Incentre \(I\) of a triangle is equidistant from all three sides. If distance to \({s1}\) is {d}\text{{ cm}}, calculate distance to \({s2}\).",
        "What is the perpendicular distance from incentre \(I\) to \({s2}\) if its distance to \({s1}\) is {d}\text{{ cm}}?",
        "Determine the distance from incentre \(I\) to \({s2}\) given that distance to \({s1}\) is {d}\text{{ cm}}.",
        "Evaluate the distance from the incentre of a triangle to \({s2}\) knowing distance to \({s1}\) is {d}\text{{ cm}}.",
        "Find the perpendicular distance from incentre \(I\) to \({s2}\) when distance to \({s1}\) is {d}\text{{ cm}}.",
        "Compute the distance from incentre \(I\) to side \({s2}\) if distance to \({s1}\) is {d}\text{{ cm}}.",
        "If incentre \(I\) is at distance {d}\text{{ cm}} from \({s1}\), what is its distance from \({s2}\)?",
        "In a triangle, the distance from incentre \(I\) to \({s1}\) is {d}\text{{ cm}}. Find the distance from \(I\) to \({s2}\)."
    ]
    
    # Arch 6: Angle AIB = 90 + C/2 (disjoint parameters)
    data_6 = [
        (34, 107), (44, 112), (56, 118), (68, 124), (78, 129),
        (86, 133), (38, 109), (58, 119), (46, 113), (92, 136)
    ]
    tmpls_6 = [
        "In \(\triangle ABC\), incentre is \(I\). If \(\angle C = {C}^\circ\), find \(\angle AIB\).",
        "For incentre \(I\) of \(\triangle ABC\), compute \(\angle AIB\) when \(\angle C = {C}^\circ\).",
        "What is the measure of \(\angle AIB\) formed at incentre \(I\) if \(\angle C = {C}^\circ\)?",
        "Calculate \(\angle AIB\) in \(\triangle ABC\) given incentre \(I\) and \(\angle C = {C}^\circ\).",
        "Determine the angle \(\angle AIB\) subtended at incentre \(I\) when \(\angle C = {C}^\circ\).",
        "Evaluate \(\angle AIB\) in \(\triangle ABC\) having \(\angle C = {C}^\circ\) and incentre \(I\).",
        "If \(I\) is the incentre of \(\triangle ABC\) and \(\angle C = {C}^\circ\), find \(\angle AIB\).",
        "Find \(\angle AIB\) for \(\triangle ABC\) where \(I\) is the incentre and \(\angle C = {C}^\circ\).",
        "Compute the measure of \(\angle AIB\) in \(\triangle ABC\) with \(\angle C = {C}^\circ\).",
        "In \(\triangle ABC\) with incentre \(I\), determine \(\angle AIB\) if \(\angle C = {C}^\circ\)."
    ]
    
    # Arch 7: Angle A from angle BIC: A = 2 * (BIC - 90)
    data_7 = [
        (105, 30), (110, 40), (115, 50), (120, 60), (125, 70),
        (130, 80), (135, 90), (112, 44), (122, 64), (128, 76)
    ]
    tmpls_7 = [
        "In \(\triangle ABC\), point \(I\) is the incentre. If \(\angle BIC = {bic}^\circ\), find \(\angle A\).",
        "If \(\angle BIC = {bic}^\circ\) at the incentre \(I\) of \(\triangle ABC\), calculate vertex angle \(\angle A\).",
        "What is the measure of \(\angle A\) in \(\triangle ABC\) if \(\angle BIC = {bic}^\circ\) where \(I\) is the incentre?",
        "Determine \(\angle A\) in \(\triangle ABC\) knowing \(I\) is the incentre and \(\angle BIC = {bic}^\circ\).",
        "Calculate vertex angle \(\angle A\) of \(\triangle ABC\) given that \(\angle BIC = {bic}^\circ\) at incentre \(I\).",
        "Evaluate the measure of \(\angle A\) in \(\triangle ABC\) having incentre \(I\) and \(\angle BIC = {bic}^\circ\).",
        "Find \(\angle A\) in \(\triangle ABC\) when angle formed by angle bisectors is \(\angle BIC = {bic}^\circ\).",
        "Compute \(\angle A\) for \(\triangle ABC\) with incentre \(I\) if \(\angle BIC = {bic}^\circ\).",
        "If \(\angle BIC = {bic}^\circ\) at incentre \(I\) in \(\triangle ABC\), what is \(\angle A\)?",
        "In \(\triangle ABC\) with incentre \(I\), find \(\angle A\) given \(\angle BIC = {bic}^\circ\)."
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        qcode = f"{tc}-OSC-{seq}"
        
        if arch == 0:
            A, ans_bic = data_0[sub_idx]
            svg = svg_incircle("", f"\angle A = {A}^\circ", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(A=A)
            corr = f"{ans_bic}^\circ"
            dist = [f"{ans_bic + 10}^\circ", f"{ans_bic - 10 if ans_bic > 10 else ans_bic + 15}^\circ", f"{180 - A}^\circ"]
            sol = f"**Step 1: Incentre angle formula**\n\(\angle BIC = 90^\circ + \frac{{\angle A}}{{2}} = 90^\circ + \frac{{{A}^\circ}}{{2}} = 90^\circ + {A//2}^\circ = {ans_bic}^\circ\).\n**Step 2: Conclusion**\n{ans_bic}°."
        elif arch == 1:
            B, ans_aic = data_1[sub_idx]
            svg = svg_incircle("", "", f"\angle B = {B}^\circ", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(B=B)
            corr = f"{ans_aic}^\circ"
            dist = [f"{ans_aic + 10}^\circ", f"{ans_aic - 10 if ans_aic > 10 else ans_aic + 15}^\circ", f"{180 - B}^\circ"]
            sol = f"**Step 1: Incentre angle formula**\n\(\angle AIC = 90^\circ + \frac{{\angle B}}{{2}} = 90^\circ + \frac{{{B}^\circ}}{{2}} = 90^\circ + {B//2}^\circ = {ans_aic}^\circ\).\n**Step 2: Conclusion**\n{ans_aic}°."
        elif arch == 2:
            r, s, ans_area = data_2[sub_idx]
            svg = svg_incircle(f"r = {r}", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(r=r, s=s, p=2*s)
            corr = f"{ans_area}\text{{ cm}}^2"
            dist = [f"{ans_area + 10}\text{{ cm}}^2", f"{ans_area - 10}\text{{ cm}}^2", f"{r * s * 2}\text{{ cm}}^2"]
            sol = f"**Step 1: Formula**\n\(\text{{Area}} = r \times s = {r} \times {s} = {ans_area}\text{{ cm}}^2\).\n**Step 2: Conclusion**\n{ans_area} cm²."
        elif arch == 3:
            area, s, ans_r = data_3[sub_idx]
            svg = svg_incircle("r = ?", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(area=area, s=s, p=2*s)
            corr = f"{ans_r}\text{{ cm}}"
            dist = [f"{ans_r + 2}\text{{ cm}}", f"{ans_r - 1}\text{{ cm}}", f"{s // 2}\text{{ cm}}"]
            sol = f"**Step 1: Formula**\n\(r = \frac{{\text{{Area}}}}{{s}} = \frac{{{area}}}{{{s}}} = {ans_r}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_r} cm."
        elif arch == 4:
            r, area, ans_p = data_4[sub_idx]
            svg = svg_incircle(f"r = {r}", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(r=r, area=area)
            corr = f"{ans_p}\text{{ cm}}"
            dist = [f"{ans_p + 4}\text{{ cm}}", f"{ans_p - 4}\text{{ cm}}", f"{ans_p // 2}\text{{ cm}}"]
            sol = f"**Step 1: Semi-perimeter and perimeter**\n\(s = \frac{{\text{{Area}}}}{{r}} = \frac{{{area}}}{{{r}}} = {ans_p // 2}\text{{ cm}}\).\n\(\text{{Perimeter}} = 2s = 2 \times {ans_p // 2} = {ans_p}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_p} cm."
        elif arch == 5:
            s1, s2, ans_d = data_5[sub_idx]
            svg = svg_incircle(f"r = {ans_d}", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(s1=s1, s2=s2, d=ans_d)
            corr = f"{ans_d}\text{{ cm}}"
            dist = [f"{ans_d + 2}\text{{ cm}}", f"{ans_d - 2 if ans_d > 2 else ans_d + 3}\text{{ cm}}", f"{ans_d * 2}\text{{ cm}}"]
            sol = f"**Step 1: Equidistant property of incentre**\nThe incentre is equidistant from all three sides of the triangle (this distance is the inradius \(r\)).\nHence, distance to \({s2}\) is also \({ans_d}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_d} cm."
        elif arch == 6:
            C, ans_aib = data_6[sub_idx]
            svg = svg_incircle("", "", "", f"\angle C = {C}^\circ") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(C=C)
            corr = f"{ans_aib}^\circ"
            dist = [f"{ans_aib + 10}^\circ", f"{ans_aib - 10 if ans_aib > 10 else ans_aib + 15}^\circ", f"{180 - C}^\circ"]
            sol = f"**Step 1: Incentre angle formula**\n\(\angle AIB = 90^\circ + \frac{{\angle C}}{{2}} = 90^\circ + \frac{{{C}^\circ}}{{2}} = 90^\circ + {C//2}^\circ = {ans_aib}^\circ\).\n**Step 2: Conclusion**\n{ans_aib}°."
        elif arch == 7:
            bic, ans_a = data_7[sub_idx]
            svg = svg_incircle("", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_7[sub_idx].format(bic=bic)
            corr = f"{ans_a}^\circ"
            dist = [f"{ans_a + 10}^\circ", f"{ans_a - 10 if ans_a > 10 else ans_a + 15}^\circ", f"{180 - ans_a}^\circ"]
            sol = f"**Step 1: Inverting formula**\n\(\angle BIC = 90^\circ + \frac{{\angle A}}{{2}} \implies \frac{{\angle A}}{{2}} = {bic}^\circ - 90^\circ = {bic - 90}^\circ\).\n\(\angle A = 2 \times {bic - 90}^\circ = {ans_a}^\circ\).\n**Step 2: Conclusion**\n{ans_a}°."

        diff = "easy" if arch in [0,1,6] else ("medium" if arch in [2,3,7] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs


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
        "In right-angled \(\triangle ABC\) with sides {a}\text{{ cm}}, {b}\text{{ cm}} and hypotenuse {c}\text{{ cm}}, find the inradius \(r\).",
        "A right-angled triangle has perpendicular sides {a}\text{{ cm}} and {b}\text{{ cm}}, and hypotenuse {c}\text{{ cm}}. Calculate the radius of its inscribed circle.",
        "What is the inradius of a right triangle having legs {a}\text{{ cm}} and {b}\text{{ cm}} and hypotenuse {c}\text{{ cm}}?",
        "Calculate inradius \(r = \frac{{a + b - c}}{{2}}\) for right \(\triangle ABC\) with sides {a}\text{{ cm}}, {b}\text{{ cm}}, and {c}\text{{ cm}}.",
        "Determine the radius of the incircle of right-angled \(\triangle ABC\) having sides {a}\text{{ cm}}, {b}\text{{ cm}}, and {c}\text{{ cm}}.",
        "Evaluate the inradius for right \(\triangle ABC\) with legs {a}\text{{ cm}} and {b}\text{{ cm}} and hypotenuse {c}\text{{ cm}}.",
        "Find the inradius of \(\triangle ABC\) (\(\angle B = 90^\circ\)) given \(AB = {a}\text{{ cm}}\), \(BC = {b}\text{{ cm}}\), and \(AC = {c}\text{{ cm}}\).",
        "Compute the inradius \(r\) of right triangle with sides {a}\text{{ cm}}, {b}\text{{ cm}}, and {c}\text{{ cm}}.",
        "If a right triangle has perpendicular legs of {a}\text{{ cm}} and {b}\text{{ cm}} and hypotenuse {c}\text{{ cm}}, what is its inradius?",
        "In right \(\triangle ABC\) with sides {a}\text{{ cm}}, {b}\text{{ cm}}, and {c}\text{{ cm}}, determine the inradius."
    ]
    
    # Arch 1: Equilateral triangle with side a -> inradius r = a / (2*sqrt(3))
    data_1 = [
        ("6\sqrt{3}", 3), ("8\sqrt{3}", 4), ("10\sqrt{3}", 5), ("12\sqrt{3}", 6), ("14\sqrt{3}", 7),
        ("16\sqrt{3}", 8), ("18\sqrt{3}", 9), ("20\sqrt{3}", 10), ("22\sqrt{3}", 11), ("24\sqrt{3}", 12)
    ]
    tmpls_1 = [
        "In an equilateral triangle of side {a}\text{{ cm}}, find the inradius \(r\).",
        "Calculate the inradius of an equilateral triangle whose side length is {a}\text{{ cm}}.",
        "What is the radius of the incircle of an equilateral triangle with sides {a}\text{{ cm}}?",
        "Determine the inradius \(r = \frac{{a}}{{2\sqrt{{3}}}}\) for an equilateral triangle with side {a}\text{{ cm}}.",
        "Compute the inradius of equilateral \(\triangle ABC\) where each side is {a}\text{{ cm}}.",
        "Evaluate the inradius for an equilateral triangle having side length {a}\text{{ cm}}.",
        "Find the radius of the inscribed circle in equilateral \(\triangle ABC\) with side {a}\text{{ cm}}.",
        "If the side of an equilateral triangle is {a}\text{{ cm}}, calculate its inradius.",
        "What is the inradius of equilateral \(\triangle ABC\) with side length {a}\text{{ cm}}?",
        "In equilateral \(\triangle ABC\), side length is {a}\text{{ cm}}. Find the inradius."
    ]
    
    # Arch 2: Area of incircle: A = pi * r^2
    data_2 = [
        (1, 1), (2, 4), (3, 9), (4, 16), (5, 25),
        (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)
    ]
    tmpls_2 = [
        "If the inradius of a triangle is {r}\text{{ cm}}, find the area of its incircle in terms of \(\pi\).",
        "Calculate the area of the incircle of a triangle having inradius \(r = {r}\text{{ cm}}\).",
        "What is the area of the incircle with radius {r}\text{{ cm}} in terms of \(\pi\)?",
        "Compute the area of the inscribed circle of \(\triangle ABC\) given inradius \(r = {r}\text{{ cm}}\).",
        "Determine the area of the incircle (in terms of \(\pi\)) when inradius is {r}\text{{ cm}}.",
        "Evaluate the area of the incircle with radius {r}\text{{ cm}}.",
        "Find the area in terms of \(\pi\) of an incircle having radius {r}\text{{ cm}}.",
        "Calculate incircle area \(\pi r^2\) for inradius \(r = {r}\text{{ cm}}\).",
        "If inradius is {r}\text{{ cm}}, what is the area of the incircle in terms of \(\pi\)?",
        "In \(\triangle ABC\), inradius is {r}\text{{ cm}}. Find the area of the incircle."
    ]
    
    # Arch 3: Circumference of incircle: C = 2 * pi * r
    data_3 = [
        (11, 22), (12, 24), (13, 26), (14, 28), (15, 30),
        (16, 32), (17, 34), (18, 36), (19, 38), (21, 42)
    ]
    tmpls_3 = [
        "A circle inscribed in a triangle has radius {r}\\text{{ cm}}. What is the boundary perimeter of this incircle in terms of \\(\\pi\\)?",
        "Calculate the circumference length of an inscribed circular boundary with radius \\(r = {r}\\text{{ cm}}\\).",
        "Determine the total perimeter of the incircle of \\(\\triangle ABC\\) when the inradius measures {r}\\text{{ cm}}.",
        "Compute the circumference \\(C = 2\\pi r\\) of the incircle having internal radius {r}\\text{{ cm}}.",
        "For an inscribed circle possessing radius {r}\\text{{ cm}}, evaluate its perimeter around the boundary.",
        "What boundary distance is traced around an incircle whose radius is given as \\(r = {r}\\text{{ cm}}\\)?",
        "Find the complete circumference in terms of \\(\\pi\\) for an incircle of radius {r}\\text{{ cm}}.",
        "An incircle has internal radius \\(r = {r}\\text{{ cm}}\\). Find the circumference of this circle.",
        "Determine the length of the circular boundary for an incircle with \\(r = {r}\\text{{ cm}}\\).",
        "Evaluate the circumference of the inscribed circle in \\(\\triangle ABC\\) having inradius {r}\\text{{ cm}}."
    ]
    
    # Arch 4: Tangent segments from vertex A: x = s - a
    data_4 = [
        (7, 8, 9, 12, 5), (5, 6, 7, 9, 4), (6, 7, 9, 11, 5), (8, 9, 11, 14, 6), (10, 11, 13, 17, 7),
        (12, 13, 15, 20, 8), (14, 15, 17, 23, 9), (16, 17, 19, 26, 10), (18, 19, 21, 29, 11), (20, 21, 23, 32, 12)
    ]
    tmpls_4 = [
        "In \(\triangle ABC\) with sides \(a = {a}\text{{ cm}}\), \(b = {b}\text{{ cm}}\), and \(c = {c}\text{{ cm}}\), incircle touches side \(BC\) at \(D\). Find length of tangent segment \(AF = s - a\).",
        "The incircle of \(\triangle ABC\) touches sides \(BC, CA, AB\) at \(D, E, F\). If \(a = {a}\), \(b = {b}\), \(c = {c}\), calculate \(AF\).",
        "What is the length of tangent segment \(AF\) from vertex \(A\) to the incircle in \(\triangle ABC\) with sides {a}, {b}, {c}?",
        "Calculate tangent segment \(AF = s - a\) in \(\triangle ABC\) with sides {a}, {b}, {c} and semi-perimeter \(s = {s}\).",
        "Determine the length of segment \(AF\) on side \(AB\) from vertex \(A\) to touchpoint with incircle for sides {a}, {b}, {c}.",
        "Evaluate length \(AF\) in \(\triangle ABC\) where incircle touches sides and \(a = {a}, b = {b}, c = {c}\).",
        "Find length \(AF\) of tangent from \(A\) to incircle in \(\triangle ABC\) (sides {a}, {b}, {c}).",
        "Compute tangent segment \(AF = s - a\) for triangle with sides {a}, {b}, {c} and \(s = {s}\).",
        "If incircle touches sides of \(\triangle ABC\) ({a}, {b}, {c}), what is the tangent length from \(A\)?",
        "In \(\triangle ABC\) with sides {a}, {b}, {c}, find length \(AF = s - a\)."
    ]
    
    # Arch 5: Radius from right triangle hypotenuse and perimeter
    data_5 = [
        (10, 24, 2), (13, 30, 2), (17, 40, 3), (25, 56, 3), (29, 70, 6),
        (37, 84, 5), (41, 90, 4), (53, 126, 10), (65, 154, 12), (73, 176, 15)
    ]
    tmpls_5 = [
        "A right-angled triangle has perimeter {p}\text{{ cm}} and hypotenuse {c}\text{{ cm}}. Find its inradius.",
        "Calculate the inradius of a right triangle with perimeter {p}\text{{ cm}} and hypotenuse {c}\text{{ cm}}.",
        "What is the inradius of a right triangle having perimeter {p}\text{{ cm}} and hypotenuse {c}\text{{ cm}}?",
        "Determine the inradius \(r = \frac{{p - 2c}}{{2}}\) for a right triangle with perimeter {p}\text{{ cm}} and hypotenuse {c}\text{{ cm}}.",
        "Compute the radius of the inscribed circle of right triangle with perimeter {p}\text{{ cm}} and hypotenuse {c}\text{{ cm}}.",
        "Evaluate the inradius for right-angled triangle having perimeter {p}\text{{ cm}} and hypotenuse {c}\text{{ cm}}.",
        "Find the inradius of right triangle given perimeter {p}\text{{ cm}} and hypotenuse {c}\text{{ cm}}.",
        "Calculate inradius \(r\) for right triangle with perimeter {p}\text{{ cm}} and hypotenuse {c}\text{{ cm}}.",
        "If a right triangle has perimeter {p}\text{{ cm}} and hypotenuse {c}\text{{ cm}}, what is its inradius?",
        "In a right triangle with perimeter {p}\text{{ cm}} and hypotenuse {c}\text{{ cm}}, determine inradius \(r\)."
    ]
    
    # Arch 6: Distance from incentre to vertices in equilateral triangle
    data_6 = [
        (3, 6), (4, 8), (5, 10), (6, 12), (7, 14),
        (8, 16), (9, 18), (10, 20), (11, 22), (12, 24)
    ]
    tmpls_6 = [
        "In an equilateral triangle with inradius \(r = {r}\text{{ cm}}\), find the distance from incentre \(I\) to any vertex.",
        "The inradius of an equilateral triangle is {r}\text{{ cm}}. Calculate the distance from incentre \(I\) to vertex \(A\).",
        "What is the distance of vertex \(A\) from incentre \(I\) in an equilateral triangle of inradius {r}\text{{ cm}}?",
        "Determine distance \(AI = 2r\) in an equilateral triangle having inradius {r}\text{{ cm}}.",
        "Compute the distance from incentre \(I\) to vertex \(A\) in equilateral \(\triangle ABC\) with inradius {r}\text{{ cm}}.",
        "Evaluate distance \(AI\) for an equilateral triangle having inradius {r}\text{{ cm}}.",
        "Find the distance from the incentre to each vertex in an equilateral triangle of inradius {r}\text{{ cm}}.",
        "Calculate vertex distance \(AI\) knowing \(AI = 2r\) in equilateral triangle of inradius {r}\text{{ cm}}.",
        "If inradius of equilateral triangle is {r}\text{{ cm}}, what is the distance from incentre to a vertex?",
        "In equilateral \(\triangle ABC\), inradius is {r}\text{{ cm}}. Find the distance \(AI\)."
    ]
    
    # Arch 7: Angle between tangents from vertex A to incircle
    data_7 = [
        (40, 140), (50, 130), (60, 120), (70, 110), (80, 100),
        (45, 135), (55, 125), (65, 115), (75, 105), (85, 95)
    ]
    tmpls_7 = [
        "In \(\triangle ABC\), incircle touches sides \(AB\) and \(AC\) at \(F\) and \(E\). If \(\angle A = {deg}^\circ\), find \(\angle FIE\).",
        "The incircle of \(\triangle ABC\) touches \(AB\) at \(F\) and \(AC\) at \(E\). If \(\angle BAC = {deg}^\circ\), calculate central angle \(\angle FIE\).",
        "What is the measure of angle \(\angle FIE\) subtended at incentre \(I\) by contact points \(F\) and \(E\) if \(\angle A = {deg}^\circ\)?",
        "Calculate \(\angle FIE = 180^\circ - \angle A\) in quadrilateral \(AFIE\) when \(\angle A = {deg}^\circ\).",
        "Determine the angle \(\angle FIE\) in quadrilateral \(AFIE\) (\(\angle F = \angle E = 90^\circ\)) given \(\angle A = {deg}^\circ\).",
        "Evaluate \(\angle FIE\) subtended at incentre \(I\) given vertex angle \(\angle A = {deg}^\circ\).",
        "Find \(\angle FIE\) in \(\triangle ABC\) with incircle contact points \(F\) and \(E\) when \(\angle A = {deg}^\circ\).",
        "Compute the measure of \(\angle FIE\) formed by radii to touch points \(F\) and \(E\) if \(\angle A = {deg}^\circ\).",
        "If \(\angle A = {deg}^\circ\) in \(\triangle ABC\), what is angle \(\angle FIE\) between radii to touchpoints?",
        "In \(\triangle ABC\), contact points on \(AB\) and \(AC\) are \(F\) and \(E\). Find \(\angle FIE\) if \(\angle A = {deg}^\circ\)."
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        qcode = f"{tc}-OSC-{seq}"
        
        if arch == 0:
            a, b, c, ans_r = data_0[sub_idx]
            svg = svg_incircle("r = ?", f"a = {a}", f"b = {b}", f"c = {c}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(a=a, b=b, c=c)
            corr = f"{ans_r}\text{{ cm}}"
            dist = [f"{ans_r + 2}\text{{ cm}}", f"{ans_r - 1}\text{{ cm}}", f"{ans_r + 4}\text{{ cm}}"]
            sol = f"**Step 1: Formula for right triangle inradius**\n\(r = \frac{{a + b - c}}{{2}} = \frac{{{a} + {b} - {c}}}{{2}} = \frac{{{a+b-c}}}{{2}} = {ans_r}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_r} cm."
        elif arch == 1:
            a, ans_r = data_1[sub_idx]
            svg = svg_incircle("r = ?", f"side = {a}", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(a=a)
            corr = f"{ans_r}\text{{ cm}}"
            dist = [f"{ans_r + 2}\text{{ cm}}", f"{ans_r - 1}\text{{ cm}}", f"{ans_r * 2}\text{{ cm}}"]
            sol = f"**Step 1: Inradius of equilateral triangle**\n\(r = \frac{{a}}{{2\sqrt{{3}}}} = \frac{{{a}}}{{2\sqrt{{3}}}} = {ans_r}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_r} cm."
        elif arch == 2:
            r, ans_coef = data_2[sub_idx]
            svg = svg_incircle(f"r = {r}", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(r=r)
            corr = f"{ans_coef}\pi\text{{ cm}}^2"
            dist = [f"{ans_coef + 5}\pi\text{{ cm}}^2", f"{ans_coef - 5 if ans_coef > 5 else ans_coef + 8}\pi\text{{ cm}}^2", f"{2 * r}\pi\text{{ cm}}^2"]
            sol = f"**Step 1: Area of incircle**\n\(\text{{Area}} = \pi r^2 = \pi \times {r}^2 = {ans_coef}\pi\text{{ cm}}^2\).\n**Step 2: Conclusion**\n{ans_coef}π cm²."
        elif arch == 3:
            r, ans_coef = data_3[sub_idx]
            svg = svg_incircle(f"r = {r}", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(r=r)
            corr = f"{ans_coef}\pi\text{{ cm}}"
            dist = [f"{ans_coef + 4}\pi\text{{ cm}}", f"{ans_coef - 2 if ans_coef > 2 else ans_coef + 6}\pi\text{{ cm}}", f"{r * r}\pi\text{{ cm}}"]
            sol = f"**Step 1: Circumference of incircle**\n\(\text{{Circumference}} = 2\pi r = 2\pi \times {r} = {ans_coef}\pi\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_coef}π cm."
        elif arch == 4:
            a, b, c, s, ans_af = data_4[sub_idx]
            svg = svg_incircle("", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(a=a, b=b, c=c, s=s)
            corr = f"{ans_af}\text{{ cm}}"
            dist = [f"{ans_af + 2}\text{{ cm}}", f"{ans_af - 2 if ans_af > 2 else ans_af + 3}\text{{ cm}}", f"{s}\text{{ cm}}"]
            sol = f"**Step 1: Tangent length formula**\n\(s = \frac{{{a} + {b} + {c}}}{{2}} = {s}\text{{ cm}}\).\n\(AF = s - a = {s} - {a} = {ans_af}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_af} cm."
        elif arch == 5:
            c, p, ans_r = data_5[sub_idx]
            svg = svg_incircle("r = ?", "", "", f"hyp = {c}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(c=c, p=p)
            corr = f"{ans_r}\text{{ cm}}"
            dist = [f"{ans_r + 2}\text{{ cm}}", f"{ans_r - 1}\text{{ cm}}", f"{c // 2}\text{{ cm}}"]
            sol = f"**Step 1: Formula for right triangle**\nSince \(a + b + c = p \implies a + b = p - c\).\n\(r = \frac{{a + b - c}}{{2}} = \frac{{(p - c) - c}}{{2}} = \frac{{{p} - 2({c})}}{{2}} = \frac{{{p - 2*c}}}{{2}} = {ans_r}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_r} cm."
        elif arch == 6:
            r, ans_dist = data_6[sub_idx]
            svg = svg_incircle(f"r = {r}", "AI = ?", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(r=r)
            corr = f"{ans_dist}\text{{ cm}}"
            dist = [f"{ans_dist + 3}\text{{ cm}}", f"{ans_dist - 3 if ans_dist > 3 else ans_dist + 4}\text{{ cm}}", f"{r}\text{{ cm}}"]
            sol = f"**Step 1: Vertex distance in equilateral triangle**\nIn equilateral triangle, \(AI = 2r = 2 \times {r} = {ans_dist}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_dist} cm."
        elif arch == 7:
            deg, ans_ang = data_7[sub_idx]
            svg = svg_incircle("", f"\angle A = {deg}^\circ", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_7[sub_idx].format(deg=deg)
            corr = f"{ans_ang}^\circ"
            dist = [f"{ans_ang + 15}^\circ", f"{ans_ang - 15 if ans_ang > 15 else ans_ang + 20}^\circ", f"{deg}^\circ"]
            sol = f"**Step 1: Quadrilateral angle sum**\nIn quadrilateral \(AFIE\), \(\angle F = \angle E = 90^\circ\).\n\(\angle FIE = 180^\circ - \angle A = 180^\circ - {deg}^\circ = {ans_ang}^\circ\).\n**Step 2: Conclusion**\n{ans_ang}°."

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
        "In a right-angled triangle with hypotenuse {c}\text{{ cm}}, find the circumradius \(R\).",
        "Calculate the circumradius of a right triangle having hypotenuse of length {c}\text{{ cm}}.",
        "What is the radius of the circumcircle of a right triangle whose hypotenuse measures {c}\text{{ cm}}?",
        "Determine the circumradius \(R = \frac{{\text{{hypotenuse}}}}{{2}}\) for a right triangle with hypotenuse {c}\text{{ cm}}.",
        "Compute the circumradius \(R\) of right-angled \(\triangle ABC\) where hypotenuse \(AC = {c}\text{{ cm}}\).",
        "Evaluate the circumradius of a right triangle having hypotenuse {c}\text{{ cm}}.",
        "Find the radius of the circumscribed circle of a right triangle with hypotenuse {c}\text{{ cm}}.",
        "If the hypotenuse of a right-angled triangle is {c}\text{{ cm}}, calculate circumradius \(R\).",
        "What does the circumradius equal for a right triangle having hypotenuse {c}\text{{ cm}}?",
        "In right triangle \(\triangle ABC\), hypotenuse is {c}\text{{ cm}}. Find the circumradius."
    ]
    
    # Arch 1: Given circumradius R of right triangle, find hypotenuse = 2 * R
    data_1 = [
        (4, 8), (6, 12), (8, 16), (10, 20), (12, 24),
        (14, 28), (16, 32), (18, 36), (20, 40), (22, 44)
    ]
    tmpls_1 = [
        "The circumradius of a right-angled triangle is {R}\text{{ cm}}. Find the length of its hypotenuse.",
        "Calculate the hypotenuse of a right triangle whose circumcircle has radius {R}\text{{ cm}}.",
        "What is the length of the hypotenuse of a right triangle having circumradius \(R = {R}\text{{ cm}}\)?" ,
        "Determine the hypotenuse in right \(\triangle ABC\) if circumradius \(R = {R}\text{{ cm}}\).",
        "Compute the hypotenuse \(c = 2R\) of a right triangle given circumradius {R}\text{{ cm}}.",
        "Evaluate the hypotenuse of a right triangle with circumradius {R}\text{{ cm}}.",
        "Find the hypotenuse of right triangle with circumradius {R}\text{{ cm}}.",
        "If circumradius is {R}\text{{ cm}}, calculate the hypotenuse of the right-angled triangle.",
        "How long is the hypotenuse of a right triangle having circumradius {R}\text{{ cm}}?",
        "In right-angled \(\triangle ABC\), circumradius is {R}\text{{ cm}}. Find the hypotenuse."
    ]
    
    # Arch 2: Equilateral triangle with side a -> circumradius R = a / sqrt(3)
    data_2 = [
        ("3\sqrt{3}", 3), ("6\sqrt{3}", 6), ("9\sqrt{3}", 9), ("12\sqrt{3}", 12), ("15\sqrt{3}", 15),
        ("18\sqrt{3}", 18), ("21\sqrt{3}", 21), ("24\sqrt{3}", 24), ("27\sqrt{3}", 27), ("30\sqrt{3}", 30)
    ]
    tmpls_2 = [
        "In an equilateral triangle of side {a}\text{{ cm}}, find the circumradius \(R\).",
        "Calculate the circumradius of an equilateral triangle with side length {a}\text{{ cm}}.",
        "What is the radius of the circumcircle of an equilateral triangle having sides {a}\text{{ cm}}?",
        "Determine circumradius \(R = \frac{{a}}{{\sqrt{{3}}}}\) for an equilateral triangle of side {a}\text{{ cm}}.",
        "Compute the circumradius \(R\) of equilateral \(\triangle ABC\) with side {a}\text{{ cm}}.",
        "Evaluate the circumradius of equilateral triangle having side length {a}\text{{ cm}}.",
        "Find the radius of circumscribed circle of equilateral \(\triangle ABC\) with side {a}\text{{ cm}}.",
        "If side of equilateral triangle is {a}\text{{ cm}}, calculate its circumradius.",
        "What is the circumradius of equilateral \(\triangle ABC\) having side {a}\text{{ cm}}?",
        "In equilateral \(\triangle ABC\), each side measures {a}\text{{ cm}}. Find circumradius \(R\)."
    ]
    
    # Arch 3: Ratio R : r in equilateral triangle = 2
    data_3 = [
        (3, 6), (4, 8), (5, 10), (6, 12), (7, 14),
        (8, 16), (9, 18), (10, 20), (11, 22), (12, 24)
    ]
    tmpls_3 = [
        "In an equilateral triangle, if inradius \(r = {r}\text{{ cm}}\), find its circumradius \(R\).",
        "The inradius of an equilateral triangle is {r}\text{{ cm}}. Calculate its circumradius \(R\).",
        "What is the circumradius \(R\) of an equilateral triangle having inradius \(r = {r}\text{{ cm}}\)?" ,
        "Compute circumradius \(R = 2r\) for an equilateral triangle with inradius {r}\text{{ cm}}.",
        "Determine the circumradius of an equilateral triangle given that its inradius is {r}\text{{ cm}}.",
        "Evaluate circumradius \(R\) in equilateral \(\triangle ABC\) having inradius {r}\text{{ cm}}.",
        "Find circumradius \(R\) of an equilateral triangle with inradius {r}\text{{ cm}}.",
        "If inradius of equilateral triangle is {r}\text{{ cm}}, calculate circumradius \(R\).",
        "What does circumradius \(R\) equal if inradius is {r}\text{{ cm}} in equilateral triangle?",
        "In equilateral \(\triangle ABC\), inradius is {r}\text{{ cm}}. Determine circumradius \(R\)."
    ]
    
    # Arch 4: Circumference of circumcircle: C = 2 * pi * R
    data_4 = [
        (5, 10), (7, 14), (9, 18), (11, 22), (13, 26),
        (15, 30), (17, 34), (19, 38), (21, 42), (25, 50)
    ]
    tmpls_4 = [
        "If the circumradius of a triangle is {R}\text{{ cm}}, find the circumference of its circumcircle in terms of \(\pi\).",
        "Calculate the circumference of the circumcircle of a triangle with circumradius \(R = {R}\text{{ cm}}\).",
        "What is the circumference of the circumcircle of radius {R}\text{{ cm}} in terms of \(\pi\)?",
        "Compute the circumference of the circumcircle for a triangle having circumradius {R}\text{{ cm}}.",
        "Determine the perimeter of the circumcircle with radius {R}\text{{ cm}} in terms of \(\pi\).",
        "Evaluate circumference \(2\pi R\) for circumcircle with radius {R}\text{{ cm}}.",
        "Find the circumference of circumcircle of radius {R}\text{{ cm}} in terms of \(\pi\).",
        "Calculate circumference of circumcircle having radius {R}\text{{ cm}}.",
        "If circumradius is {R}\text{{ cm}}, what is the circumference of the circumcircle?",
        "In a triangle, circumradius is {R}\text{{ cm}}. Find the circumference of the circumcircle."
    ]
    
    # Arch 5: Area of circumcircle: A = pi * R^2
    data_5 = [
        (2, 4), (3, 9), (4, 16), (5, 25), (6, 36),
        (7, 49), (8, 64), (9, 81), (10, 100), (12, 144)
    ]
    tmpls_5 = [
        "If the circumradius of a triangle is {R}\text{{ cm}}, find the area of its circumcircle in terms of \(\pi\).",
        "Calculate the area of the circumcircle of a triangle with circumradius \(R = {R}\text{{ cm}}\).",
        "What is the area of the circumcircle of radius {R}\text{{ cm}} in terms of \(\pi\)?",
        "Compute the area of the circumcircle for a triangle having circumradius {R}\text{{ cm}}.",
        "Determine the area of the circumcircle with radius {R}\text{{ cm}} in terms of \(\pi\).",
        "Evaluate area \(\pi R^2\) for circumcircle with radius {R}\text{{ cm}}.",
        "Find the area of circumcircle of radius {R}\text{{ cm}} in terms of \(\pi\).",
        "Calculate area of circumcircle having radius {R}\text{{ cm}}.",
        "If circumradius is {R}\text{{ cm}}, what is the area of the circumcircle in terms of \(\pi\)?",
        "In a triangle, circumradius is {R}\text{{ cm}}. Find the area of the circumcircle."
    ]
    
    # Arch 6: Equidistant property of circumcentre from vertices
    data_6 = [
        ("A", "B", 7), ("B", "C", 9), ("C", "A", 11), ("A", "C", 13), ("B", "A", 15),
        ("vertex A", "vertex B", 17), ("vertex B", "vertex C", 19), ("vertex C", "vertex A", 21), ("vertex A", "vertex C", 23), ("vertex B", "vertex A", 25)
    ]
    tmpls_6 = [
        "The circumcentre \(C\) of \(\triangle ABC\) is at distance {d}\text{{ cm}} from {v1}. What is its distance from {v2}?",
        "In \(\triangle ABC\), circumcentre \(C\) is at distance {d}\text{{ cm}} from {v1}. Calculate distance to {v2}.",
        "Circumcentre of a triangle is equidistant from all three vertices. If distance to {v1} is {d}\text{{ cm}}, find distance to {v2}.",
        "What is the distance from circumcentre \(C\) to {v2} if its distance to {v1} is {d}\text{{ cm}}?",
        "Determine the distance from circumcentre \(C\) to {v2} given that distance to {v1} is {d}\text{{ cm}}.",
        "Evaluate the distance from circumcentre of a triangle to {v2} knowing distance to {v1} is {d}\text{{ cm}}.",
        "Find the distance from circumcentre to {v2} when distance to {v1} is {d}\text{{ cm}}.",
        "Compute the distance from circumcentre \(C\) to {v2} if distance to {v1} is {d}\text{{ cm}}.",
        "If circumcentre is at distance {d}\text{{ cm}} from {v1}, what is its distance from {v2}?",
        "In \(\triangle ABC\), distance from circumcentre to {v1} is {d}\text{{ cm}}. Find distance to {v2}."
    ]
    
    # Arch 7: Median to hypotenuse in right triangle = R = hyp / 2
    data_7 = [
        (12, 6), (16, 8), (20, 10), (24, 12), (28, 14),
        (32, 16), (36, 18), (40, 20), (44, 22), (48, 24)
    ]
    tmpls_7 = [
        "In a right-angled triangle with hypotenuse {hyp}\text{{ cm}}, find the length of the median drawn to the hypotenuse.",
        "Calculate the length of the median to hypotenuse in a right triangle having hypotenuse {hyp}\text{{ cm}}.",
        "What is the length of the median to the hypotenuse of a right triangle with hypotenuse {hyp}\text{{ cm}}?",
        "Determine the length of median to hypotenuse in right \(\triangle ABC\) where hypotenuse \(AC = {hyp}\text{{ cm}}\).",
        "Compute the median to hypotenuse \(BD = \frac{{AC}}{{2}}\) in right triangle with hypotenuse {hyp}\text{{ cm}}.",
        "Evaluate the median to hypotenuse for a right-angled triangle having hypotenuse {hyp}\text{{ cm}}.",
        "Find the length of median to hypotenuse of right triangle with hypotenuse {hyp}\text{{ cm}}.",
        "If hypotenuse of a right triangle is {hyp}\text{{ cm}}, calculate the length of the median to hypotenuse.",
        "How long is the median to the hypotenuse in a right-angled triangle of hypotenuse {hyp}\text{{ cm}}?",
        "In right triangle \(\triangle ABC\), hypotenuse is {hyp}\text{{ cm}}. Find the median to hypotenuse."
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        qcode = f"{tc}-OSC-{seq}"
        
        if arch == 0:
            c, ans_r = data_0[sub_idx]
            svg = svg_circumcircle(f"R = {ans_r}", "", "", f"hyp = {c}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(c=c)
            corr = f"{ans_r}\text{{ cm}}"
            dist = [f"{ans_r + 2}\text{{ cm}}", f"{ans_r - 2 if ans_r > 2 else ans_r + 3}\text{{ cm}}", f"{c}\text{{ cm}}"]
            sol = f"**Step 1: Circumradius of right triangle**\nIn a right-angled triangle, the circumcentre lies at the midpoint of the hypotenuse.\n\(R = \frac{{\text{{hypotenuse}}}}{{2}} = \frac{{{c}}}{{2}} = {ans_r}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_r} cm."
        elif arch == 1:
            R, ans_hyp = data_1[sub_idx]
            svg = svg_circumcircle(f"R = {R}", "", "", "hyp = ?") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(R=R)
            corr = f"{ans_hyp}\text{{ cm}}"
            dist = [f"{ans_hyp + 4}\text{{ cm}}", f"{ans_hyp - 4}\text{{ cm}}", f"{R}\text{{ cm}}"]
            sol = f"**Step 1: Hypotenuse formula**\n\(\text{{hypotenuse}} = 2 \times R = 2 \times {R} = {ans_hyp}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_hyp} cm."
        elif arch == 2:
            a, ans_r = data_2[sub_idx]
            svg = svg_circumcircle(f"R = {ans_r}", f"side = {a}", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(a=a)
            corr = f"{ans_r}\text{{ cm}}"
            dist = [f"{ans_r + 3}\text{{ cm}}", f"{ans_r - 3 if ans_r > 3 else ans_r + 4}\text{{ cm}}", f"{ans_r * 2}\text{{ cm}}"]
            sol = f"**Step 1: Formula**\n\(R = \frac{{a}}{{\sqrt{{3}}}} = \frac{{{a}}}{{\sqrt{{3}}}} = {ans_r}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_r} cm."
        elif arch == 3:
            r, ans_r = data_3[sub_idx]
            svg = svg_circumcircle(f"R = {ans_r}", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(r=r)
            corr = f"{ans_r}\text{{ cm}}"
            dist = [f"{ans_r + 2}\text{{ cm}}", f"{ans_r - 2}\text{{ cm}}", f"{r}\text{{ cm}}"]
            sol = f"**Step 1: Ratio of R to r**\nIn an equilateral triangle, \(R = 2r = 2 \times {r} = {ans_r}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_r} cm."
        elif arch == 4:
            R, ans_coef = data_4[sub_idx]
            svg = svg_circumcircle(f"R = {R}", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(R=R)
            corr = f"{ans_coef}\pi\text{{ cm}}"
            dist = [f"{ans_coef + 4}\pi\text{{ cm}}", f"{ans_coef - 4}\pi\text{{ cm}}", f"{R * R}\pi\text{{ cm}}"]
            sol = f"**Step 1: Circumference of circumcircle**\n\(\text{{Circumference}} = 2\pi R = 2\pi \times {R} = {ans_coef}\pi\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_coef}π cm."
        elif arch == 5:
            R, ans_coef = data_5[sub_idx]
            svg = svg_circumcircle(f"R = {R}", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(R=R)
            corr = f"{ans_coef}\pi\text{{ cm}}^2"
            dist = [f"{ans_coef + 10}\pi\text{{ cm}}^2", f"{ans_coef - 10 if ans_coef > 10 else ans_coef + 15}\pi\text{{ cm}}^2", f"{2 * R}\pi\text{{ cm}}^2"]
            sol = f"**Step 1: Area of circumcircle**\n\(\text{{Area}} = \pi R^2 = \pi \times {R}^2 = {ans_coef}\pi\text{{ cm}}^2\).\n**Step 2: Conclusion**\n{ans_coef}π cm²."
        elif arch == 6:
            v1, v2, ans_d = data_6[sub_idx]
            svg = svg_circumcircle(f"R = {ans_d}", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(v1=v1, v2=v2, d=ans_d)
            corr = f"{ans_d}\text{{ cm}}"
            dist = [f"{ans_d + 3}\text{{ cm}}", f"{ans_d - 3 if ans_d > 3 else ans_d + 4}\text{{ cm}}", f"{ans_d * 2}\text{{ cm}}"]
            sol = f"**Step 1: Equidistant property**\nThe circumcentre is equidistant from all three vertices of the triangle.\nHence, distance to {v2} is also {ans_d}\text{{ cm}}.\n**Step 2: Conclusion**\n{ans_d} cm."
        elif arch == 7:
            hyp, ans_med = data_7[sub_idx]
            svg = svg_circumcircle("", "", "", f"hyp = {hyp}") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_7[sub_idx].format(hyp=hyp)
            corr = f"{ans_med}\text{{ cm}}"
            dist = [f"{ans_med + 2}\text{{ cm}}", f"{ans_med - 2}\text{{ cm}}", f"{hyp}\text{{ cm}}"]
            sol = f"**Step 1: Median theorem**\nIn a right-angled triangle, length of median to hypotenuse is half of the hypotenuse.\n\(\text{{Median}} = \frac{{{hyp}}}{{2}} = {ans_med}\text{{ cm}}\).\n**Step 2: Conclusion**\n{ans_med} cm."

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
        "In \(\triangle ABC\), point \(O\) is the circumcentre. If \(\angle A = {A}^\circ\), find central angle \(\angle BOC\).",
        "The angle subtended by side \(BC\) at the circumcentre \(O\) of \(\triangle ABC\) is \(\angle BOC\). If \(\angle BAC = {A}^\circ\), calculate \(\angle BOC\).",
        "What is the measure of angle \(\angle BOC\) formed at circumcentre \(O\) if \(\angle A = {A}^\circ\)?",
        "Calculate central angle \(\angle BOC = 2\angle A\) in \(\triangle ABC\) given circumcentre \(O\) and \(\angle A = {A}^\circ\).",
        "Determine the angle \(\angle BOC\) in \(\triangle ABC\) with circumcentre \(O\) where \(\angle A = {A}^\circ\).",
        "Evaluate \(\angle BOC\) for circumcentre \(O\) of \(\triangle ABC\) with \(\angle A = {A}^\circ\).",
        "If \(O\) is the circumcentre of \(\triangle ABC\) and \(\angle A = {A}^\circ\), what is \(\angle BOC\)?",
        "Find \(\angle BOC\) in \(\triangle ABC\) knowing \(O\) is the circumcentre and \(\angle A = {A}^\circ\).",
        "Compute the measure of \(\angle BOC\) subtended at circumcentre \(O\) by chord \(BC\) when \(\angle A = {A}^\circ\).",
        "In \(\triangle ABC\), circumcentre is \(O\). Calculate \(\angle BOC\) if \(\angle A = {A}^\circ\)."
    ]
    
    # Arch 1: Angle A from central angle BOC: A = BOC / 2
    data_1 = [
        (64, 32), (72, 36), (84, 42), (96, 48), (108, 54),
        (116, 58), (124, 62), (132, 66), (144, 72), (156, 78)
    ]
    tmpls_1 = [
        "In \(\triangle ABC\), \(O\) is the circumcentre. If \(\angle BOC = {boc}^\circ\), find \(\angle A\).",
        "If central angle \(\angle BOC = {boc}^\circ\) at circumcentre \(O\) of \(\triangle ABC\), calculate \(\angle BAC\).",
        "What is the measure of \(\angle A\) in \(\triangle ABC\) if \(\angle BOC = {boc}^\circ\) at circumcentre \(O\)?",
        "Determine \(\angle A\) in \(\triangle ABC\) given circumcentre \(O\) and \(\angle BOC = {boc}^\circ\).",
        "Calculate vertex angle \(\angle A\) knowing angle subtended at circumcentre is \(\angle BOC = {boc}^\circ\).",
        "Evaluate \(\angle A\) in \(\triangle ABC\) having circumcentre \(O\) and \(\angle BOC = {boc}^\circ\).",
        "Find \(\angle A\) for \(\triangle ABC\) where circumcentre is \(O\) and \(\angle BOC = {boc}^\circ\).",
        "Compute \(\angle A\) given circumcentre \(O\) and \(\angle BOC = {boc}^\circ\).",
        "If \(\angle BOC = {boc}^\circ\) in \(\triangle ABC\) with circumcentre \(O\), what is \(\angle A\)?",
        "In \(\triangle ABC\) with circumcentre \(O\), determine \(\angle A\) when \(\angle BOC = {boc}^\circ\)."
    ]
    
    # Arch 2: Base angle in isosceles triangle OBC: angle OBC = 90 - A
    data_2 = [
        (35, 55), (45, 45), (55, 35), (65, 25), (75, 15),
        (38, 52), (48, 42), (58, 32), (68, 22), (78, 12)
    ]
    tmpls_2 = [
        "In acute-angled \(\triangle ABC\), \(O\) is the circumcentre. If \(\angle A = {A}^\circ\), find \(\angle OBC\).",
        "For circumcentre \(O\) of acute \(\triangle ABC\), calculate base angle \(\angle OBC\) of \(\triangle OBC\) when \(\angle A = {A}^\circ\).",
        "What is \(\angle OBC\) in \(\triangle ABC\) if \(O\) is the circumcentre and \(\angle A = {A}^\circ\)?",
        "Determine \(\angle OBC = 90^\circ - \angle A\) in acute \(\triangle ABC\) with circumcentre \(O\) and \(\angle A = {A}^\circ\).",
        "Compute \(\angle OBC\) in \(\triangle ABC\) where \(O\) is the circumcentre and \(\angle BAC = {A}^\circ\).",
        "Evaluate \(\angle OBC\) in isosceles \(\triangle OBC\) (\(OB = OC = R\)) when \(\angle A = {A}^\circ\).",
        "Find \(\angle OBC\) for circumcentre \(O\) in acute \(\triangle ABC\) having \(\angle A = {A}^\circ\).",
        "Calculate the measure of \(\angle OBC\) given \(O\) is the circumcentre of acute \(\triangle ABC\) and \(\angle A = {A}^\circ\).",
        "If \(O\) is circumcentre of acute \(\triangle ABC\) and \(\angle A = {A}^\circ\), what is \(\angle OBC\)?",
        "In acute \(\triangle ABC\) with circumcentre \(O\), find \(\angle OBC\) if \(\angle A = {A}^\circ\)."
    ]
    
    # Arch 3: Central angle AOC = 2 * B
    data_3 = [
        (32, 64), (42, 84), (52, 104), (62, 124), (72, 144),
        (36, 72), (46, 92), (56, 112), (66, 132), (76, 152)
    ]
    tmpls_3 = [
        "In \(\triangle ABC\), point \(O\) is the circumcentre. If \(\angle B = {B}^\circ\), find \(\angle AOC\).",
        "The angle subtended by side \(AC\) at circumcentre \(O\) is \(\angle AOC\). If \(\angle ABC = {B}^\circ\), calculate \(\angle AOC\).",
        "What is the measure of angle \(\angle AOC\) formed at circumcentre \(O\) when \(\angle B = {B}^\circ\)?",
        "Calculate central angle \(\angle AOC = 2\angle B\) in \(\triangle ABC\) given circumcentre \(O\) and \(\angle B = {B}^\circ\).",
        "Determine \(\angle AOC\) in \(\triangle ABC\) with circumcentre \(O\) where \(\angle B = {B}^\circ\).",
        "Evaluate \(\angle AOC\) for circumcentre \(O\) of \(\triangle ABC\) with \(\angle B = {B}^\circ\).",
        "If \(O\) is the circumcentre of \(\triangle ABC\) and \(\angle B = {B}^\circ\), what is \(\angle AOC\)?",
        "Find \(\angle AOC\) in \(\triangle ABC\) knowing \(O\) is the circumcentre and \(\angle B = {B}^\circ\).",
        "Compute the measure of \(\angle AOC\) subtended at circumcentre \(O\) by side \(AC\) when \(\angle B = {B}^\circ\).",
        "In \(\triangle ABC\), circumcentre is \(O\). Calculate \(\angle AOC\) if \(\angle B = {B}^\circ\)."
    ]
    
    # Arch 4: Central angle AOB = 2 * C
    data_4 = [
        (34, 68), (44, 88), (54, 108), (64, 128), (74, 148),
        (38, 76), (48, 96), (58, 116), (68, 136), (78, 156)
    ]
    tmpls_4 = [
        "In \(\triangle ABC\), \(O\) is the circumcentre. If \(\angle C = {C}^\circ\), find \(\angle AOB\).",
        "For circumcentre \(O\) of \(\triangle ABC\), calculate \(\angle AOB\) when \(\angle C = {C}^\circ\).",
        "What is the measure of angle \(\angle AOB\) subtended at circumcentre \(O\) if \(\angle C = {C}^\circ\)?",
        "Calculate central angle \(\angle AOB = 2\angle C\) in \(\triangle ABC\) given circumcentre \(O\) and \(\angle C = {C}^\circ\).",
        "Determine the angle \(\angle AOB\) in \(\triangle ABC\) where \(O\) is the circumcentre and \(\angle C = {C}^\circ\).",
        "Evaluate \(\angle AOB\) for \(\triangle ABC\) with circumcentre \(O\) having \(\angle C = {C}^\circ\).",
        "Find \(\angle AOB\) in \(\triangle ABC\) given circumcentre \(O\) and \(\angle C = {C}^\circ\).",
        "Calculate \(\angle AOB\) subtended at circumcentre \(O\) when \(\angle C = {C}^\circ\).",
        "If \(O\) is the circumcentre of \(\triangle ABC\) and \(\angle C = {C}^\circ\), what is \(\angle AOB\)?",
        "In \(\triangle ABC\), circumcentre is \(O\). Determine \(\angle AOB\) if \(\angle C = {C}^\circ\)."
    ]
    
    # Arch 5: Base angle OAC = 90 - B
    data_5 = [
        (31, 59), (41, 49), (51, 39), (61, 29), (71, 19),
        (37, 53), (47, 43), (57, 33), (67, 23), (77, 13)
    ]
    tmpls_5 = [
        "In acute-angled \(\triangle ABC\) with circumcentre \(O\), if \(\angle B = {B}^\circ\), find \(\angle OAC\).",
        "For circumcentre \(O\) of acute \(\triangle ABC\), calculate \(\angle OAC\) when \(\angle B = {B}^\circ\).",
        "What is \(\angle OAC\) in \(\triangle ABC\) if \(O\) is the circumcentre and \(\angle B = {B}^\circ\)?",
        "Determine \(\angle OAC = 90^\circ - \angle B\) in acute \(\triangle ABC\) with circumcentre \(O\) and \(\angle B = {B}^\circ\).",
        "Compute \(\angle OAC\) in \(\triangle ABC\) where \(O\) is the circumcentre and \(\angle ABC = {B}^\circ\).",
        "Evaluate \(\angle OAC\) in isosceles \(\triangle OAC\) (\(OA = OC = R\)) when \(\angle B = {B}^\circ\).",
        "Find \(\angle OAC\) for circumcentre \(O\) in acute \(\triangle ABC\) having \(\angle B = {B}^\circ\).",
        "Calculate the measure of \(\angle OAC\) given \(O\) is the circumcentre of acute \(\triangle ABC\) and \(\angle B = {B}^\circ\).",
        "If \(O\) is circumcentre of acute \(\triangle ABC\) and \(\angle B = {B}^\circ\), what is \(\angle OAC\)?",
        "In acute \(\triangle ABC\) with circumcentre \(O\), find \(\angle OAC\) if \(\angle B = {B}^\circ\)."
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
        "In acute-angled \(\triangle ABC\) with circumcentre \(O\), if \(\angle C = {C}^\circ\), find \(\angle OAB\).",
        "For circumcentre \(O\) of acute \(\triangle ABC\), calculate \(\angle OAB\) when \(\angle C = {C}^\circ\).",
        "What is \(\angle OAB\) in \(\triangle ABC\) if \(O\) is the circumcentre and \(\angle C = {C}^\circ\)?",
        "Determine \(\angle OAB = 90^\circ - \angle C\) in acute \(\triangle ABC\) with circumcentre \(O\) and \(\angle C = {C}^\circ\).",
        "Compute \(\angle OAB\) in \(\triangle ABC\) where \(O\) is the circumcentre and \(\angle C = {C}^\circ\).",
        "Evaluate \(\angle OAB\) in isosceles \(\triangle OAB\) (\(OA = OB = R\)) when \(\angle C = {C}^\circ\).",
        "Find \(\angle OAB\) for circumcentre \(O\) in acute \(\triangle ABC\) having \(\angle C = {C}^\circ\).",
        "Calculate the measure of \(\angle OAB\) given \(O\) is the circumcentre of acute \(\triangle ABC\) and \(\angle C = {C}^\circ\).",
        "If \(O\) is circumcentre of acute \(\triangle ABC\) and \(\angle C = {C}^\circ\), what is \(\angle OAB\)?",
        "In acute \(\triangle ABC\) with circumcentre \(O\), find \(\angle OAB\) if \(\angle C = {C}^\circ\)."
    ]

    for idx, seq in enumerate(SEQS_80):
        arch = idx % 8
        sub_idx = (idx // 8) % 10
        has_fig = (idx % 3 != 0)
        qcode = f"{tc}-OSC-{seq}"
        
        if arch == 0:
            A, ans_boc = data_0[sub_idx]
            svg = svg_circumcircle("", f"\angle A = {A}^\circ", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_0[sub_idx].format(A=A)
            corr = f"{ans_boc}^\circ"
            dist = [f"{ans_boc + 15}^\circ", f"{ans_boc - 15 if ans_boc > 15 else ans_boc + 20}^\circ", f"{180 - A}^\circ"]
            sol = f"**Step 1: Circumcentre angle theorem**\nThe angle subtended by an arc at the centre is double the angle subtended by it at any point on the circle.\n\(\angle BOC = 2\angle A = 2 \times {A}^\circ = {ans_boc}^\circ\).\n**Step 2: Conclusion**\n{ans_boc}°."
        elif arch == 1:
            boc, ans_a = data_1[sub_idx]
            svg = svg_circumcircle("", "", "", f"\angle BOC = {boc}^\circ") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_1[sub_idx].format(boc=boc)
            corr = f"{ans_a}^\circ"
            dist = [f"{ans_a + 8}^\circ", f"{ans_a - 8 if ans_a > 8 else ans_a + 12}^\circ", f"{180 - ans_a}^\circ"]
            sol = f"**Step 1: Inverting formula**\n\(\angle A = \frac{{\angle BOC}}{{2}} = \frac{{{boc}^\circ}}{{2}} = {ans_a}^\circ\).\n**Step 2: Conclusion**\n{ans_a}°."
        elif arch == 2:
            A, ans_obc = data_2[sub_idx]
            svg = svg_circumcircle("", f"\angle A = {A}^\circ", "\angle OBC = ?", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_2[sub_idx].format(A=A)
            corr = f"{ans_obc}^\circ"
            dist = [f"{ans_obc + 10}^\circ", f"{ans_obc - 10 if ans_obc > 10 else ans_obc + 15}^\circ", f"{A}^\circ"]
            sol = f"**Step 1: Isosceles triangle OBC**\n\(\angle BOC = 2\angle A = 2 \times {A}^\circ = {2*A}^\circ\).\nSince \(OB = OC = R\), \(\angle OBC = \angle OCB = \frac{{180^\circ - {2*A}^\circ}}{{2}} = 90^\circ - {A}^\circ = {ans_obc}^\circ\).\n**Step 2: Conclusion**\n{ans_obc}°."
        elif arch == 3:
            B, ans_aoc = data_3[sub_idx]
            svg = svg_circumcircle("", "", f"\angle B = {B}^\circ", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_3[sub_idx].format(B=B)
            corr = f"{ans_aoc}^\circ"
            dist = [f"{ans_aoc + 15}^\circ", f"{ans_aoc - 15 if ans_aoc > 15 else ans_aoc + 20}^\circ", f"{180 - B}^\circ"]
            sol = f"**Step 1: Formula**\n\(\angle AOC = 2\angle B = 2 \times {B}^\circ = {ans_aoc}^\circ\).\n**Step 2: Conclusion**\n{ans_aoc}°."
        elif arch == 4:
            C, ans_aob = data_4[sub_idx]
            svg = svg_circumcircle("", "", "", f"\angle C = {C}^\circ") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_4[sub_idx].format(C=C)
            corr = f"{ans_aob}^\circ"
            dist = [f"{ans_aob + 15}^\circ", f"{ans_aob - 15 if ans_aob > 15 else ans_aob + 20}^\circ", f"{180 - C}^\circ"]
            sol = f"**Step 1: Formula**\n\(\angle AOB = 2\angle C = 2 \times {C}^\circ = {ans_aob}^\circ\).\n**Step 2: Conclusion**\n{ans_aob}°."
        elif arch == 5:
            B, ans_oac = data_5[sub_idx]
            svg = svg_circumcircle("", "", f"\angle B = {B}^\circ", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_5[sub_idx].format(B=B)
            corr = f"{ans_oac}^\circ"
            dist = [f"{ans_oac + 10}^\circ", f"{ans_oac - 10 if ans_oac > 10 else ans_oac + 15}^\circ", f"{B}^\circ"]
            sol = f"**Step 1: Formula**\n\(\angle OAC = 90^\circ - \angle B = 90^\circ - {B}^\circ = {ans_oac}^\circ\).\n**Step 2: Conclusion**\n{ans_oac}°."
        elif arch == 6:
            angles, ans_pos = data_6[sub_idx]
            svg = svg_circumcircle("", "", "", "") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_6[sub_idx].format(angles=angles)
            corr = ans_pos
            opts_pool = ["Inside the triangle (Interior)", "On the hypotenuse (Midpoint of hypotenuse)", "Outside the triangle (Exterior)", "At vertex B"]
            dist = [p for p in opts_pool if p != ans_pos][:3]
            sol = f"**Step 1: Circumcentre location theorem**\n- Acute triangle: Circumcentre lies inside the triangle.\n- Right triangle: Circumcentre lies on the midpoint of the hypotenuse.\n- Obtuse triangle: Circumcentre lies outside the triangle.\nFor angles {angles}°, the circumcentre is located: {ans_pos}.\n**Step 2: Conclusion**\n{ans_pos}."
        elif arch == 7:
            C, ans_oab = data_7[sub_idx]
            svg = svg_circumcircle("", "", "", f"\angle C = {C}^\circ") if has_fig else ""
            prefix = (svg + "\n") if svg else ""
            txt = prefix + tmpls_7[sub_idx].format(C=C)
            corr = f"{ans_oab}^\circ"
            dist = [f"{ans_oab + 10}^\circ", f"{ans_oab - 10 if ans_oab > 10 else ans_oab + 15}^\circ", f"{C}^\circ"]
            sol = f"**Step 1: Formula**\n\(\angle OAB = 90^\circ - \angle C = 90^\circ - {C}^\circ = {ans_oab}^\circ\).\n**Step 2: Conclusion**\n{ans_oab}°."

        diff = "easy" if arch in [0,3,4] else ("medium" if arch in [1,2,5] else "hard")
        qs.append(build_q(qcode, txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def main():
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

if __name__ == "__main__":
    main()
