# scripts/build_ch4_5.py
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

def build_q(qcode, text, corr, dist, sol, ch_num, ch_name, tc, tname, seq, has_fig, diff="medium"):
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
        "chapterNumber": ch_num,
        "chapter": ch_name,
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
        "questionText": text,
        "text": text,
        "options": opts,
        "correctAnswer": corr_letter,
        "solution": sol,
        "explanation": sol,
        "hasFigure": has_fig,
        "isVerified": True
    }

# SVGs
def svg_parallelogram(lbl_a="A", lbl_b="B", lbl_c="C", lbl_d="D", extra_text=""):
    t_tag = f'<text x="120" y="115" fill="#f59e0b" font-size="10" font-family="sans-serif">{extra_text}</text>' if extra_text else ""
    return (
        '<svg width="240" height="200" viewBox="0 0 240 200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a;border-radius:8px;display:block;margin:12px auto;">'
        '<polygon points="40,150 160,150 200,60 80,60" fill="none" stroke="#38bdf8" stroke-width="2"/>'
        f'<text x="25" y="155" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">{lbl_a}</text>'
        f'<text x="165" y="155" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">{lbl_b}</text>'
        f'<text x="205" y="55" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">{lbl_c}</text>'
        f'<text x="70" y="55" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">{lbl_d}</text>'
        f'{t_tag}'
        '</svg>'
    )

def svg_parallelogram_diagonals(extra_text=""):
    t_tag = f'<text x="120" y="140" fill="#f59e0b" font-size="10" font-family="sans-serif">{extra_text}</text>' if extra_text else ""
    return (
        '<svg width="240" height="200" viewBox="0 0 240 200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a;border-radius:8px;display:block;margin:12px auto;">'
        '<polygon points="40,150 160,150 200,60 80,60" fill="none" stroke="#38bdf8" stroke-width="2"/>'
        '<line x1="40" y1="150" x2="200" y2="60" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,3"/>'
        '<line x1="160" y1="150" x2="80" y2="60" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,3"/>'
        '<circle cx="120" cy="105" r="3" fill="#f8fafc"/>'
        '<text x="25" y="155" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">A</text>'
        '<text x="165" y="155" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">B</text>'
        '<text x="205" y="55" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">C</text>'
        '<text x="70" y="55" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">D</text>'
        '<text x="125" y="100" fill="#f8fafc" font-size="10" font-family="sans-serif">O</text>'
        f'{t_tag}'
        '</svg>'
    )

def svg_rectangle(lbl_a="A", lbl_b="B", lbl_c="C", lbl_d="D", extra_text=""):
    t_tag = f'<text x="120" y="115" fill="#f59e0b" font-size="10" font-family="sans-serif">{extra_text}</text>' if extra_text else ""
    return (
        '<svg width="240" height="200" viewBox="0 0 240 200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a;border-radius:8px;display:block;margin:12px auto;">'
        '<rect x="40" y="60" width="160" height="100" fill="none" stroke="#38bdf8" stroke-width="2"/>'
        '<line x1="40" y1="160" x2="200" y2="60" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,3"/>'
        '<line x1="200" y1="160" x2="40" y2="60" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,3"/>'
        '<circle cx="120" cy="110" r="3" fill="#f8fafc"/>'
        f'<text x="25" y="165" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">{lbl_a}</text>'
        f'<text x="205" y="165" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">{lbl_b}</text>'
        f'<text x="205" y="55" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">{lbl_c}</text>'
        f'<text x="25" y="55" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">{lbl_d}</text>'
        '<text x="125" y="105" fill="#f8fafc" font-size="10" font-family="sans-serif">O</text>'
        f'{t_tag}'
        '</svg>'
    )

def svg_rhombus(lbl_a="A", lbl_b="B", lbl_c="C", lbl_d="D", extra_text=""):
    t_tag = f'<text x="120" y="145" fill="#f59e0b" font-size="10" font-family="sans-serif">{extra_text}</text>' if extra_text else ""
    return (
        '<svg width="240" height="200" viewBox="0 0 240 200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a;border-radius:8px;display:block;margin:12px auto;">'
        '<polygon points="120,40 200,105 120,170 40,105" fill="none" stroke="#38bdf8" stroke-width="2"/>'
        '<line x1="120" y1="40" x2="120" y2="170" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,3"/>'
        '<line x1="40" y1="105" x2="200" y2="105" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,3"/>'
        '<circle cx="120" cy="105" r="3" fill="#f8fafc"/>'
        f'<text x="115" y="30" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">{lbl_a}</text>'
        f'<text x="205" y="110" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">{lbl_b}</text>'
        f'<text x="115" y="185" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">{lbl_c}</text>'
        f'<text x="25" y="110" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">{lbl_d}</text>'
        '<text x="125" y="98" fill="#f8fafc" font-size="10" font-family="sans-serif">O</text>'
        f'{t_tag}'
        '</svg>'
    )

def svg_square(extra_text=""):
    t_tag = f'<text x="120" y="145" fill="#f59e0b" font-size="10" font-family="sans-serif">{extra_text}</text>' if extra_text else ""
    return (
        '<svg width="240" height="200" viewBox="0 0 240 200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a;border-radius:8px;display:block;margin:12px auto;">'
        '<rect x="60" y="45" width="120" height="120" fill="none" stroke="#38bdf8" stroke-width="2"/>'
        '<line x1="60" y1="165" x2="180" y2="45" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,3"/>'
        '<line x1="180" y1="165" x2="60" y2="45" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,3"/>'
        '<text x="45" y="170" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">A</text>'
        '<text x="185" y="170" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">B</text>'
        '<text x="185" y="40" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">C</text>'
        '<text x="45" y="40" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">D</text>'
        f'{t_tag}'
        '</svg>'
    )

def svg_midpoint(extra_text=""):
    t_tag = f'<text x="120" y="130" fill="#f59e0b" font-size="10" font-family="sans-serif">{extra_text}</text>' if extra_text else ""
    return (
        '<svg width="240" height="200" viewBox="0 0 240 200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a;border-radius:8px;display:block;margin:12px auto;">'
        '<polygon points="120,35 40,165 200,165" fill="none" stroke="#38bdf8" stroke-width="2"/>'
        '<line x1="80" y1="100" x2="160" y2="100" stroke="#f43f5e" stroke-width="2"/>'
        '<circle cx="80" cy="100" r="3" fill="#f8fafc"/>'
        '<circle cx="160" cy="100" r="3" fill="#f8fafc"/>'
        '<text x="115" y="25" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">A</text>'
        '<text x="25" y="170" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">B</text>'
        '<text x="205" y="170" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">C</text>'
        '<text x="65" y="98" fill="#f8fafc" font-size="10" font-family="sans-serif">D</text>'
        '<text x="165" y="98" fill="#f8fafc" font-size="10" font-family="sans-serif">E</text>'
        f'{t_tag}'
        '</svg>'
    )

def svg_construction(extra_text=""):
    t_tag = f'<text x="120" y="115" fill="#f59e0b" font-size="10" font-family="sans-serif">{extra_text}</text>' if extra_text else ""
    return (
        '<svg width="240" height="200" viewBox="0 0 240 200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a;border-radius:8px;display:block;margin:12px auto;">'
        '<line x1="40" y1="160" x2="200" y2="160" stroke="#38bdf8" stroke-width="2"/>'
        '<line x1="40" y1="160" x2="130" y2="40" stroke="#38bdf8" stroke-width="1.5"/>'
        '<line x1="130" y1="40" x2="200" y2="160" stroke="#f43f5e" stroke-width="1.5"/>'
        '<line x1="90" y1="95" x2="200" y2="160" stroke="#a855f7" stroke-width="1.2" stroke-dasharray="3,3"/>'
        '<circle cx="90" cy="95" r="3" fill="#f8fafc"/>'
        '<text x="25" y="165" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">B</text>'
        '<text x="205" y="165" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">C</text>'
        '<text x="135" y="35" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">A</text>'
        '<text x="75" y="95" fill="#f8fafc" font-size="10" font-family="sans-serif">D</text>'
        f'{t_tag}'
        '</svg>'
    )

print("SVGs loaded.")
