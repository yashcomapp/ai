# scripts/generate_ch2_part2_js.py
# Generates scripts/mh9_mth1_ch2_part2_data.js containing 226 validated questions for Chapter 2 (Topics 2.4, 2.5, 2.6)
import json

questions = []

def make_q(qcode, tcode, parent_tcode, tnum, tname, parent_tname, vault, difficulty, bloom, tag, text, correct, wrongs, sol):
    opts = [{"text": correct, "isCorrect": True}]
    for w in wrongs:
        opts.append({"text": w, "isCorrect": False})
    
    # Deterministic rotation based on hash to distribute A, B, C, D
    h = sum(ord(c) for c in qcode) % 4
    rotated_opts = opts[h:] + opts[:h]
    letters = ['A', 'B', 'C', 'D']
    c_idx = next(i for i, o in enumerate(rotated_opts) if o["isCorrect"])
    
    return {
        "questionCode": qcode,
        "topicCode": tcode,
        "parentTopicCode": parent_tcode,
        "topicNumber": tnum,
        "topic": tname,
        "topicName": tname,
        "parentTopicName": parent_tname,
        "boardCode": "MH",
        "board": "Maharashtra Board",
        "class": "9",
        "subjectCode": "MTH1",
        "subject": "Mathematics Part - 1 (Algebra)",
        "chapterNumber": 2,
        "chapter": "Real Numbers",
        "vault": vault,
        "examCategory": "foundation" if vault == "foundation" else "standard",
        "type": "OSC",
        "marks": 4,
        "difficulty": difficulty,
        "bloomLevel": bloom,
        "conceptTag": tag,
        "text": text,
        "options": rotated_opts,
        "correctAnswer": letters[c_idx],
        "solution": sol,
        "timesUsed": 0,
        "usedInClassroomTest": False,
        "requiresFigure": False
    }

# =========================================================================
# TOPIC 2.4: Operations & Comparison of Surds (75 Qs)
# Subtopics: 2.4.1 (38 Qs), 2.4.2 (37 Qs)
# =========================================================================

# 2.4.1: Arithmetic operations (19 Exam, 9 Practice, 10 Foundation = 38 Qs)
s241_vaults = ['exam']*19 + ['practice']*9 + ['foundation']*10
add_sub_cases = [
    # (a, b, c, rad, res_coeff) => a\sqrt{rad} + b\sqrt{rad} - c\sqrt{rad} = res_coeff\sqrt{rad}
    (5, 7, 3, 3, 9),
    (4, 8, 5, 2, 7),
    (6, 9, 4, 5, 11),
    (8, 3, 6, 7, 5),
    (7, 5, 4, 11, 8),
    (9, 6, 5, 3, 10),
    (3, 11, 4, 2, 10),
    (12, 4, 7, 5, 9),
    (10, 5, 8, 7, 7),
    (15, 6, 9, 6, 12),
    (4, 9, 3, 10, 10),
    (7, 8, 6, 3, 9),
    (11, 5, 7, 2, 9),
    (8, 7, 5, 5, 10),
    (13, 4, 8, 7, 9),
    (9, 9, 6, 11, 12),
    (6, 12, 7, 3, 11),
    (14, 5, 9, 2, 10),
    (7, 10, 8, 5, 9),
    (11, 8, 7, 6, 12),
    (5, 13, 6, 7, 12),
    (16, 4, 9, 3, 11),
    (8, 11, 7, 2, 12),
    (10, 7, 8, 5, 9),
    (12, 6, 9, 11, 9),
    (9, 8, 7, 3, 10),
    (15, 3, 8, 2, 10),
    (7, 11, 6, 5, 12),
    (13, 5, 7, 7, 11),
    (10, 9, 8, 6, 11),
    (6, 14, 9, 3, 11),
    (12, 7, 8, 2, 11),
    (8, 10, 7, 5, 11),
    (14, 4, 9, 7, 9),
    (11, 9, 8, 11, 12),
    (7, 12, 8, 3, 11),
    (13, 6, 9, 2, 10),
    (9, 11, 8, 5, 12)
]

for i, v in enumerate(s241_vaults):
    seq = f"{i+4:03d}"
    v_prefix = 'E' if v == 'exam' else ('P' if v == 'practice' else 'F')
    qc = f"MH-9-MTH1-2-2.4.1-OSC-{v_prefix}{seq}"
    c1, c2, c3, rad, ans_coeff = add_sub_cases[i]
    
    questions.append(make_q(
        qc, "MH-9-MTH1-2-2.4.1", "MH-9-MTH1-2-2.4", "2.4.1",
        "Addition, subtraction, multiplication, division of surds", "Operations on Surds & Comparison of Surds",
        v, "medium" if i % 2 == 0 else "easy", "Apply", f"Combine Like Surds {rad}",
        f"Simplify: \\({c1}\\sqrt{{{rad}}} + {c2}\\sqrt{{{rad}}} - {c3}\\sqrt{{{rad}}}\\)",
        f"\\({ans_coeff}\\sqrt{{{rad}}}\\)",
        [
            f"\\({ans_coeff + 2}\\sqrt{{{rad}}}\\)",
            f"\\({ans_coeff - 2}\\sqrt{{{rad}}}\\)",
            f"\\({c1 + c2 + c3}\\sqrt{{{rad}}}\\)"
        ],
        f"1. Since all terms are like surds with common radical factor \\(\\sqrt{{{rad}}}\\), combine their rational coefficients:\n   \\(({c1} + {c2} - {c3})\\sqrt{{{rad}}}\\).\n2. \\({c1} + {c2} - {c3} = {ans_coeff}\\).\n3. Result: \\({ans_coeff}\\sqrt{{{rad}}}\\)."
    ))

# 2.4.2: Comparing pure and mixed surds (18 Exam, 9 Practice, 10 Foundation = 37 Qs)
s242_vaults = ['exam']*18 + ['practice']*9 + ['foundation']*10
compare_cases = [
    # (a, r1, b, r2) => a\sqrt{r1} = \sqrt{a^2*r1} vs b\sqrt{r2} = \sqrt{b^2*r2}
    (4, 3, 3, 5),   # 48 vs 45 -> >
    (5, 2, 3, 6),   # 50 vs 54 -> <
    (6, 2, 5, 3),   # 72 vs 75 -> <
    (7, 3, 6, 4),   # 147 vs 144 -> >
    (4, 5, 5, 3),   # 80 vs 75 -> >
    (3, 7, 4, 4),   # 63 vs 64 -> <
    (5, 5, 6, 3),   # 125 vs 108 -> >
    (8, 2, 5, 5),   # 128 vs 125 -> >
    (7, 2, 4, 6),   # 98 vs 96 -> >
    (6, 3, 4, 7),   # 108 vs 112 -> <
    (9, 2, 7, 3),   # 162 vs 147 -> >
    (5, 6, 7, 3),   # 150 vs 147 -> >
    (4, 8, 6, 3),   # 128 vs 108 -> >
    (3, 10, 5, 4),  # 90 vs 100 -> <
    (7, 5, 8, 4),   # 245 vs 256 -> <
    (6, 5, 8, 3),   # 180 vs 192 -> <
    (9, 3, 11, 2),  # 243 vs 242 -> >
    (5, 7, 6, 5),   # 175 vs 180 -> <
    (8, 3, 7, 4),   # 192 vs 196 -> <
    (10, 2, 6, 6),  # 200 vs 216 -> <
    (7, 6, 8, 5),   # 294 vs 320 -> <
    (9, 4, 12, 2),  # 324 vs 288 -> >
    (6, 7, 8, 4),   # 252 vs 256 -> <
    (5, 11, 7, 6),  # 275 vs 294 -> <
    (11, 3, 9, 5),  # 363 vs 405 -> <
    (8, 5, 10, 3),  # 320 vs 300 -> >
    (7, 7, 9, 4),   # 343 vs 324 -> >
    (12, 2, 7, 6),  # 288 vs 294 -> <
    (6, 8, 7, 6),   # 288 vs 294 -> <
    (10, 3, 8, 5),  # 300 vs 320 -> <
    (9, 5, 11, 3),  # 405 vs 363 -> >
    (7, 8, 9, 5),   # 392 vs 405 -> <
    (12, 3, 10, 4), # 432 vs 400 -> >
    (8, 6, 9, 5),   # 384 vs 405 -> <
    (11, 4, 13, 3), # 484 vs 507 -> <
    (10, 5, 12, 3), # 500 vs 432 -> >
    (9, 6, 11, 4)   # 486 vs 484 -> >
]

for i, v in enumerate(s242_vaults):
    seq = f"{i+3:03d}"
    v_prefix = 'E' if v == 'exam' else ('P' if v == 'practice' else 'F')
    qc = f"MH-9-MTH1-2-2.4.2-OSC-{v_prefix}{seq}"
    a, r1, b, r2 = compare_cases[i]
    val1 = (a**2) * r1
    val2 = (b**2) * r2
    rel_symbol = ">" if val1 > val2 else "<"
    inv_symbol = "<" if val1 > val2 else ">"
    
    questions.append(make_q(
        qc, "MH-9-MTH1-2-2.4.2", "MH-9-MTH1-2-2.4", "2.4.2",
        "Comparing pure and mixed surds", "Operations on Surds & Comparison of Surds",
        v, "medium", "Apply", f"Compare Surds {a}sqrt({r1}) and {b}sqrt({r2})",
        f"Compare the two surds \\({a}\\sqrt{{{r1}}}\\) and \\({b}\\sqrt{{{r2}}}\\):",
        f"\\({a}\\sqrt{{{r1}}} {rel_symbol} {b}\\sqrt{{{r2}}}\\) because \\(\\sqrt{{{val1}}} {rel_symbol} \\sqrt{{{val2}}}\\)",
        [
            f"\\({a}\\sqrt{{{r1}}} {inv_symbol} {b}\\sqrt{{{r2}}}\\)",
            f"\\({a}\\sqrt{{{r1}}} = {b}\\sqrt{{{r2}}}\\)",
            "They cannot be compared because their orders differ"
        ],
        f"1. Convert both mixed surds into pure surds:\n   - \\({a}\\sqrt{{{r1}}} = \\sqrt{{{a}^2 \\times {r1}}} = \\sqrt{{{val1}}}\\)\n   - \\({b}\\sqrt{{{r2}}} = \\sqrt{{{b}^2 \\times {r2}}} = \\sqrt{{{val2}}}\\)\n2. Comparing radicands: \\({val1} {rel_symbol} {val2}\\).\n3. Therefore, \\({a}\\sqrt{{{r1}}} {rel_symbol} {b}\\sqrt{{{r2}}}\\)."
    ))

# =========================================================================
# TOPIC 2.5: Rationalisation of Surds & Conjugate Pairs (76 Qs)
# Subtopics: 2.5.1 (39 Qs), 2.5.2 (37 Qs)
# =========================================================================

# 2.5.1: Rationalising factor (19 Exam, 10 Practice, 10 Foundation = 39 Qs)
s251_vaults = ['exam']*19 + ['practice']*10 + ['foundation']*10
monomial_surds = [
    (2, 2, 2),
    (3, 3, 3),
    (5, 5, 5),
    (7, 7, 7),
    (6, 6, 6),
    (8, 2, "2\\sqrt{2} \\times \\sqrt{2} = 4"),
    (11, 11, 11),
    (12, 3, "2\\sqrt{3} \\times \\sqrt{3} = 6"),
    (13, 13, 13),
    (15, 15, 15),
    (18, 2, "3\\sqrt{2} \\times \\sqrt{2} = 6"),
    (20, 5, "2\\sqrt{5} \\times \\sqrt{5} = 10"),
    (21, 21, 21),
    (24, 6, "2\\sqrt{6} \\times \\sqrt{6} = 12"),
    (27, 3, "3\\sqrt{3} \\times \\sqrt{3} = 9"),
    (28, 7, "2\\sqrt{7} \\times \\sqrt{7} = 14"),
    (32, 2, "4\\sqrt{2} \\times \\sqrt{2} = 8"),
    (35, 35, 35),
    (40, 10, "2\\sqrt{10} \\times \\sqrt{10} = 20"),
    (45, 5, "3\\sqrt{5} \\times \\sqrt{5} = 15"),
    (48, 3, "4\\sqrt{3} \\times \\sqrt{3} = 12"),
    (50, 2, "5\\sqrt{2} \\times \\sqrt{2} = 10"),
    (54, 6, "3\\sqrt{6} \\times \\sqrt{6} = 18"),
    (63, 7, "3\\sqrt{7} \\times \\sqrt{7} = 21"),
    (72, 2, "6\\sqrt{2} \\times \\sqrt{2} = 12"),
    (75, 3, "5\\sqrt{3} \\times \\sqrt{3} = 15"),
    (80, 5, "4\\sqrt{5} \\times \\sqrt{5} = 20"),
    (98, 2, "7\\sqrt{2} \\times \\sqrt{2} = 14"),
    (108, 3, "6\\sqrt{3} \\times \\sqrt{3} = 18"),
    (125, 5, "5\\sqrt{5} \\times \\sqrt{5} = 25"),
    (147, 3, "7\\sqrt{3} \\times \\sqrt{3} = 21"),
    (162, 2, "9\\sqrt{2} \\times \\sqrt{2} = 18"),
    (180, 5, "6\\sqrt{5} \\times \\sqrt{5} = 30"),
    (192, 3, "8\\sqrt{3} \\times \\sqrt{3} = 24"),
    (200, 2, "10\\sqrt{2} \\times \\sqrt{2} = 20"),
    (245, 5, "7\\sqrt{5} \\times \\sqrt{5} = 35"),
    (288, 2, "12\\sqrt{2} \\times \\sqrt{2} = 24"),
    (300, 3, "10\\sqrt{3} \\times \\sqrt{3} = 30"),
    (320, 5, "8\\sqrt{5} \\times \\sqrt{5} = 40")
]

for i, v in enumerate(s251_vaults):
    seq = f"{i+3:03d}"
    v_prefix = 'E' if v == 'exam' else ('P' if v == 'practice' else 'F')
    qc = f"MH-9-MTH1-2-2.5.1-OSC-{v_prefix}{seq}"
    raw_rad, rf_rad, mult_exp = monomial_surds[i]
    
    questions.append(make_q(
        qc, "MH-9-MTH1-2-2.5.1", "MH-9-MTH1-2-2.5", "2.5.1",
        "Rationalising factor definition", "Rationalisation of Surds & Conjugate Pairs",
        v, "medium" if i % 2 == 0 else "easy", "Apply", f"RF of sqrt({raw_rad})",
        f"What is the simplest rationalising factor of the surd \\(\\sqrt{{{raw_rad}}}\\)?",
        f"\\(\\sqrt{{{rf_rad}}}\\)",
        [
            f"\\({rf_rad}\\)",
            f"\\(\\sqrt{{{raw_rad + 2}}}\\)",
            "\\(1\\)"
        ],
        f"1. A surd is called a rationalising factor if multiplying it by the given surd yields a rational number.\n2. In simplest form, \\(\\sqrt{{{raw_rad}}}\\) has radical component \\(\\sqrt{{{rf_rad}}}\\).\n3. Multiplying by \\(\\sqrt{{{rf_rad}}}\\) produces a rational number."
    ))

# 2.5.2: Conjugate pairs (18 Exam, 9 Practice, 10 Foundation = 37 Qs)
s252_vaults = ['exam']*18 + ['practice']*9 + ['foundation']*10
conjugate_cases = [
    # (term1, term2, conjugate_str, product_val) => (t1 + t2)(t1 - t2) = t1^2 - t2^2
    ("\\sqrt{5}", "\\sqrt{3}", "\\sqrt{5} - \\sqrt{3}", "5 - 3 = 2"),
    ("\\sqrt{7}", "\\sqrt{2}", "\\sqrt{7} - \\sqrt{2}", "7 - 2 = 5"),
    ("\\sqrt{11}", "\\sqrt{5}", "\\sqrt{11} - \\sqrt{5}", "11 - 5 = 6"),
    ("3", "\\sqrt{2}", "3 - \\sqrt{2}", "9 - 2 = 7"),
    ("5", "\\sqrt{3}", "5 - \\sqrt{3}", "25 - 3 = 22"),
    ("\\sqrt{13}", "\\sqrt{7}", "\\sqrt{13} - \\sqrt{7}", "13 - 7 = 6"),
    ("2\\sqrt{3}", "\\sqrt{5}", "2\\sqrt{3} - \\sqrt{5}", "12 - 5 = 7"),
    ("4", "\\sqrt{7}", "4 - \\sqrt{7}", "16 - 7 = 9"),
    ("\\sqrt{10}", "\\sqrt{3}", "\\sqrt{10} - \\sqrt{3}", "10 - 3 = 7"),
    ("3\\sqrt{2}", "2\\sqrt{3}", "3\\sqrt{2} - 2\\sqrt{3}", "18 - 12 = 6"),
    ("\\sqrt{15}", "\\sqrt{6}", "\\sqrt{15} - \\sqrt{6}", "15 - 6 = 9"),
    ("6", "\\sqrt{5}", "6 - \\sqrt{5}", "36 - 5 = 31"),
    ("\\sqrt{17}", "\\sqrt{3}", "\\sqrt{17} - \\sqrt{3}", "17 - 3 = 14"),
    ("4\\sqrt{2}", "\\sqrt{11}", "4\\sqrt{2} - \\sqrt{11}", "32 - 11 = 21"),
    ("\\sqrt{19}", "\\sqrt{10}", "\\sqrt{19} - \\sqrt{10}", "19 - 10 = 9"),
    ("5", "2\\sqrt{6}", "5 - 2\\sqrt{6}", "25 - 24 = 1"),
    ("3\\sqrt{5}", "4\\sqrt{2}", "3\\sqrt{5} - 4\\sqrt{2}", "45 - 32 = 13"),
    ("\\sqrt{21}", "\\sqrt{14}", "\\sqrt{21} - \\sqrt{14}", "21 - 14 = 7"),
    ("7", "3\\sqrt{5}", "7 - 3\\sqrt{5}", "49 - 45 = 4"),
    ("\\sqrt{23}", "\\sqrt{7}", "\\sqrt{23} - \\sqrt{7}", "23 - 7 = 16"),
    ("4\\sqrt{3}", "3\\sqrt{5}", "4\\sqrt{3} - 3\\sqrt{5}", "48 - 45 = 3"),
    ("8", "\\sqrt{15}", "8 - \\sqrt{15}", "64 - 15 = 49"),
    ("\\sqrt{26}", "\\sqrt{10}", "\\sqrt{26} - \\sqrt{10}", "26 - 10 = 16"),
    ("5\\sqrt{2}", "4\\sqrt{3}", "5\\sqrt{2} - 4\\sqrt{3}", "50 - 48 = 2"),
    ("9", "2\\sqrt{19}", "9 - 2\\sqrt{19}", "81 - 76 = 5"),
    ("\\sqrt{29}", "\\sqrt{13}", "\\sqrt{29} - \\sqrt{13}", "29 - 13 = 16"),
    ("6\\sqrt{2}", "5\\sqrt{2}", "6\\sqrt{2} - 5\\sqrt{2}", "72 - 50 = 22"),
    ("7\\sqrt{2}", "6\\sqrt{2}", "7\\sqrt{2} - 6\\sqrt{2}", "98 - 72 = 26"),
    ("10", "\\sqrt{19}", "10 - \\sqrt{19}", "100 - 19 = 81"),
    ("\\sqrt{31}", "\\sqrt{15}", "\\sqrt{31} - \\sqrt{15}", "31 - 15 = 16"),
    ("6\\sqrt{3}", "5\\sqrt{4}", "6\\sqrt{3} - 5\\sqrt{4}", "108 - 100 = 8"),
    ("8\\sqrt{2}", "7\\sqrt{2}", "8\\sqrt{2} - 7\\sqrt{2}", "128 - 98 = 30"),
    ("11", "3\\sqrt{11}", "11 - 3\\sqrt{11}", "121 - 99 = 22"),
    ("\\sqrt{33}", "\\sqrt{17}", "\\sqrt{33} - \\sqrt{17}", "33 - 17 = 16"),
    ("7\\sqrt{3}", "6\\sqrt{4}", "7\\sqrt{3} - 6\\sqrt{4}", "147 - 144 = 3"),
    ("9\\sqrt{2}", "8\\sqrt{2}", "9\\sqrt{2} - 8\\sqrt{2}", "162 - 128 = 34"),
    ("12", "5\\sqrt{5}", "12 - 5\\sqrt{5}", "144 - 125 = 19")
]

for i, v in enumerate(s252_vaults):
    seq = f"{i+3:03d}"
    v_prefix = 'E' if v == 'exam' else ('P' if v == 'practice' else 'F')
    qc = f"MH-9-MTH1-2-2.5.2-OSC-{v_prefix}{seq}"
    t1, t2, conj, prod_calc = conjugate_cases[i]
    
    questions.append(make_q(
        qc, "MH-9-MTH1-2-2.5.2", "MH-9-MTH1-2-2.5", "2.5.2",
        "Conjugate pair of binomial surd (√a + √b)(√a - √b)", "Rationalisation of Surds & Conjugate Pairs",
        v, "medium", "Apply", f"Conjugate of {t1} + {t2}",
        f"What is the conjugate pair of the binomial surd \\(({t1} + {t2})\\)?",
        f"\\(({conj})\\)",
        [
            f"\\(-({t1} + {t2})\\)",
            f"\\(({t1} + 2{t2})\\)",
            f"\\(1 / ({t1} + {t2})\\)"
        ],
        f"1. The conjugate pair of a binomial surd \\((x + y)\\) is \\((x - y)\\).\n2. For \\(({t1} + {t2})\\), the conjugate pair is \\(({conj})\\).\n3. Their product uses identity \\((x+y)(x-y) = x^2 - y^2 = {prod_calc}\\), which is completely rational."
    ))

# =========================================================================
# TOPIC 2.6: Absolute Value / Modulus of Real Numbers (75 Qs)
# Subtopics: 2.6.1 (38 Qs), 2.6.2 (37 Qs)
# =========================================================================

# 2.6.1: Definition of |x| (19 Exam, 9 Practice, 10 Foundation = 38 Qs)
s261_vaults = ['exam']*19 + ['practice']*9 + ['foundation']*10
mod_evals = [
    # (expr, ans, step)
    ("|15 - 28|", "13", "|-13| = 13"),
    ("|8 - 19|", "11", "|-11| = 11"),
    ("|23 - 45|", "22", "|-22| = 22"),
    ("|7 \\times (-4)|", "28", "|-28| = 28"),
    ("|(-9) \\times 6|", "54", "|-54| = 54"),
    ("|35 - 50|", "15", "|-15| = 15"),
    ("|12 - 31|", "19", "|-19| = 19"),
    ("|(-14) \\times (-5)|", "70", "|70| = 70"),
    ("|42 - 60|", "18", "|-18| = 18"),
    ("|18 - 41|", "23", "|-23| = 23"),
    ("|(-25) \\times 4|", "100", "|-100| = 100"),
    ("|16 - 39|", "23", "|-23| = 23"),
    ("|55 - 72|", "17", "|-17| = 17"),
    ("|(-8) \\times (-9)|", "72", "|72| = 72"),
    ("|29 - 53|", "24", "|-24| = 24"),
    ("|34 - 61|", "27", "|-27| = 27"),
    ("|(-15) \\times 6|", "90", "|-90| = 90"),
    ("|48 - 75|", "27", "|-27| = 27"),
    ("|21 - 49|", "28", "|-28| = 28"),
    ("|(-12) \\times 8|", "96", "|-96| = 96"),
    ("|33 - 64|", "31", "|-31| = 31"),
    ("|27 - 58|", "31", "|-31| = 31"),
    ("|(-18) \\times 5|", "90", "|-90| = 90"),
    ("|38 - 69|", "31", "|-31| = 31"),
    ("|26 - 59|", "33", "|-33| = 33"),
    ("|(-16) \\times 7|", "112", "|-112| = 112"),
    ("|44 - 78|", "34", "|-34| = 34"),
    ("|32 - 67|", "35", "|-35| = 35"),
    ("|(-20) \\times 6|", "120", "|-120| = 120"),
    ("|41 - 77|", "36", "|-36| = 36"),
    ("|36 - 73|", "37", "|-37| = 37"),
    ("|(-14) \\times 9|", "126", "|-126| = 126"),
    ("|47 - 85|", "38", "|-38| = 38"),
    ("|39 - 78|", "39", "|-39| = 39"),
    ("|(-22) \\times 5|", "110", "|-110| = 110"),
    ("|52 - 93|", "41", "|-41| = 41"),
    ("|43 - 85|", "42", "|-42| = 42"),
    ("|(-15) \\times 8|", "120", "|-120| = 120")
]

for i, v in enumerate(s261_vaults):
    seq = f"{i+3:03d}"
    v_prefix = 'E' if v == 'exam' else ('P' if v == 'practice' else 'F')
    qc = f"MH-9-MTH1-2-2.6.1-OSC-{v_prefix}{seq}"
    mod_expr, ans_str, step_str = mod_evals[i]
    ans_int = int(ans_str)
    
    questions.append(make_q(
        qc, "MH-9-MTH1-2-2.6.1", "MH-9-MTH1-2-2.6", "2.6.1",
        "Definition |x|", "Absolute Value / Modulus of Real Numbers",
        v, "easy", "Apply", f"Evaluate Absolute Value {mod_expr}",
        f"Find the value of \\({mod_expr}\\):",
        f"\\({ans_str}\\)",
        [
            f"\\(-{ans_str}\\)",
            f"\\({ans_int + 2}\\)",
            f"\\({ans_int - 2}\\)"
        ],
        f"1. Absolute value is defined as: \\(|x| = x\\) if \\(x \\ge 0\\), and \\(|x| = -x\\) if \\(x < 0\\).\n2. Inside the bars: \\({step_str}\\).\n3. Result is \\({ans_str}\\)."
    ))

# 2.6.2: Solving modulus equations (18 Exam, 10 Practice, 9 Foundation = 37 Qs)
s262_vaults = ['exam']*18 + ['practice']*10 + ['foundation']*9
mod_eqs = [
    # (a, b, c, sol1, sol2) => |ax - b| = c
    (1, 4, 7, 11, -3),
    (1, 5, 8, 13, -3),
    (2, 3, 9, 6, -3),
    (3, 1, 8, 3, -7/3),
    (2, 5, 7, 6, -1),
    (1, 6, 10, 16, -4),
    (3, 2, 13, 5, -11/3),
    (2, 7, 11, 9, -2),
    (1, 8, 12, 20, -4),
    (4, 3, 9, 3, -1.5),
    (2, 9, 15, 12, -3),
    (1, 7, 14, 21, -7),
    (3, 4, 14, 6, -10/3),
    (2, 1, 13, 7, -6),
    (1, 9, 16, 25, -7),
    (5, 2, 18, 4, -3.2),
    (2, 11, 17, 14, -3),
    (1, 10, 15, 25, -5),
    (3, 5, 16, 7, -11/3),
    (2, 3, 15, 9, -6),
    (1, 12, 18, 30, -6),
    (4, 1, 15, 4, -3.5),
    (2, 13, 19, 16, -3),
    (1, 11, 20, 31, -9),
    (3, 7, 20, 9, -13/3),
    (2, 5, 17, 11, -6),
    (1, 13, 22, 35, -9),
    (5, 4, 21, 5, -3.4),
    (2, 15, 21, 18, -3),
    (1, 14, 24, 38, -10),
    (3, 8, 22, 10, -14/3),
    (2, 7, 19, 13, -6),
    (1, 15, 25, 40, -10),
    (4, 3, 21, 6, -4.5),
    (2, 17, 23, 20, -3),
    (1, 16, 26, 42, -10),
    (3, 10, 26, 12, -16/3)
]

for i, v in enumerate(s262_vaults):
    seq = f"{i+4:03d}"
    v_prefix = 'E' if v == 'exam' else ('P' if v == 'practice' else 'F')
    qc = f"MH-9-MTH1-2-2.6.2-OSC-{v_prefix}{seq}"
    coeff_a, const_b, rhs_c, r1, r2 = mod_eqs[i]
    
    a_str = f"{coeff_a}" if coeff_a > 1 else ""
    r1_fmt = f"{int(r1)}" if isinstance(r1, int) or r1.is_integer() else f"{r1:.1f}"
    r2_fmt = f"{int(r2)}" if isinstance(r2, int) or r2.is_integer() else f"{r2:.2f}"
    
    questions.append(make_q(
        qc, "MH-9-MTH1-2-2.6.2", "MH-9-MTH1-2-2.6", "2.6.2",
        "Solving modulus equations |x - a| = b", "Absolute Value / Modulus of Real Numbers",
        v, "medium" if i % 2 == 0 else "hard", "Apply", f"Solve Mod Equation |{a_str}x - {const_b}| = {rhs_c}",
        f"Solve the modulus equation: \\(|{a_str}x - {const_b}| = {rhs_c}\\). The solution set is:",
        f"\\(x = {r1_fmt}\\) or \\(x = {r2_fmt}\\)",
        [
            f"\\(x = {r1_fmt}\\) only",
            f"\\(x = -{r1_fmt}\\) or \\(x = -{r2_fmt}\\)",
            "\\(\\emptyset\\) (No solution)"
        ],
        f"1. \\(|{a_str}x - {const_b}| = {rhs_c} \\implies {a_str}x - {const_b} = {rhs_c}\\) or \\({a_str}x - {const_b} = -{rhs_c}\\).\n2. Case 1: \\({a_str}x = {rhs_c + const_b} \\implies x = {r1_fmt}\\).\n3. Case 2: \\({a_str}x = {-rhs_c + const_b} \\implies x = {r2_fmt}\\).\n4. Solution set: \\(\\{{{r1_fmt}, {r2_fmt}\\}}\\)."
    ))

print(f"Generated {len(questions)} questions for Chapter 2 Part 2.")

# Write to JS module
js_code = "// scripts/mh9_mth1_ch2_part2_data.js\n"
js_code += f"// Generated {len(questions)} questions for Chapter 2 Topics 2.4, 2.5, 2.6\n\n"
js_code += "const ch2Part2Questions = " + json.dumps(questions, indent=2) + ";\n\n"
js_code += "module.exports = { ch2Part2Questions };\n"

with open("scripts/mh9_mth1_ch2_part2_data.js", "w", encoding="utf-8") as f:
    f.write(js_code)
print("Successfully written scripts/mh9_mth1_ch2_part2_data.js")
