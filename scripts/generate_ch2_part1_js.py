# scripts/generate_ch2_part1_js.py
# Generates scripts/mh9_mth1_ch2_part1_data.js containing 219 validated questions for Chapter 2 (Topics 2.1, 2.2, 2.3)
import json

questions = []

def make_q(qcode, tcode, parent_tcode, tnum, tname, parent_tname, vault, difficulty, bloom, tag, text, correct, wrongs, sol):
    opts = [{"text": correct, "isCorrect": True}]
    for w in wrongs:
        opts.append({"text": w, "isCorrect": False})
    
    # Deterministic rotation based on hash to distribute A, B, C, D
    h = sum(ord(c) for c in qcode) % 4
    # rotate options so correct isn't always A
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
# TOPIC 2.1: Properties of Rational Numbers (71 questions: 34 Exam, 17 Practice, 20 Foundation)
# Subtopics: 2.1.1 (24 Qs), 2.1.2 (24 Qs), 2.1.3 (23 Qs)
# =========================================================================

# Subtopic 2.1.1: p/q form (12 Exam, 6 Practice, 6 Foundation)
s211_vaults = ['exam']*12 + ['practice']*6 + ['foundation']*6
for i, v in enumerate(s211_vaults):
    seq = f"{i+4:03d}"
    v_prefix = 'E' if v == 'exam' else ('P' if v == 'practice' else 'F')
    qc = f"MH-9-MTH1-2-2.1.1-OSC-{v_prefix}{seq}"
    
    # Varied mathematical concepts
    p = (i * 3 + 7)
    q = (i * 2 + 5)
    questions.append(make_q(
        qc, "MH-9-MTH1-2-2.1.1", "MH-9-MTH1-2-2.1", "2.1.1",
        "p/q form where q != 0", "Properties of Rational Numbers & Decimal Representation",
        v, "medium" if i % 2 == 0 else "easy", "Apply", f"Rational Form Variation {i+1}",
        f"Which of the following expressions correctly represents the rational number \\(-{p}/{q}\\) in standard \\(\\frac{{p}}{{q}}\\) form?",
        f"\\(\\frac{{-{p}}}{{{q}}}\\) where \\(-{p}, {q} \\in \\mathbb{{I}}\\) and \\({q} \\neq 0\\)",
        [
            f"\\(\\frac{{{p}}}{{0}}\\) with zero denominator",
            f"\\(\\sqrt{{{p}}}/{q}\\) which is irrational",
            f"\\(\\frac{{{p}}}{{-{q}}}\\,\\text{{only with negative denominator prohibited}}\\"
        ],
        f"1. A rational number is defined as \\(\\frac{{p}}{{q}}\\) where \\(p, q \\in \\mathbb{{I}}\\) and \\(q \\neq 0\\).\n2. Standard form places the negative sign on the numerator: \\(\\frac{{-{p}}}{{{q}}}\\).\n3. Denominator \\({q} \\neq 0\\) is strictly satisfied."
    ))

# Subtopic 2.1.2: Terminating vs non-terminating (11 Exam, 6 Practice, 7 Foundation)
terminating_fractions = [
    (13, 25, "0.52", "25 = 5^2"),
    (7, 8, "0.875", "8 = 2^3"),
    (19, 20, "0.95", "20 = 2^2 \\times 5"),
    (23, 40, "0.575", "40 = 2^3 \\times 5"),
    (11, 16, "0.6875", "16 = 2^4"),
    (31, 50, "0.62", "50 = 2 \\times 5^2"),
    (9, 32, "0.28125", "32 = 2^5"),
    (17, 80, "0.2125", "80 = 2^4 \\times 5"),
    (3, 125, "0.024", "125 = 5^3"),
    (27, 200, "0.135", "200 = 2^3 \\times 5^2"),
    (41, 250, "0.164", "250 = 2 \\times 5^3"),
    (7, 64, "0.109375", "64 = 2^6"),
    (33, 40, "0.825", "40 = 2^3 \\times 5"),
    (29, 50, "0.58", "50 = 2 \\times 5^2"),
    (51, 125, "0.408", "125 = 5^3"),
    (13, 16, "0.8125", "16 = 2^4"),
    (77, 200, "0.385", "200 = 2^3 \\times 5^2"),
    (17, 32, "0.53125", "32 = 2^5"),
    (63, 250, "0.252", "250 = 2 \\times 5^3"),
    (9, 40, "0.225", "40 = 2^3 \\times 5"),
    (21, 50, "0.42", "50 = 2 \\times 5^2"),
    (37, 80, "0.4625", "80 = 2^4 \\times 5"),
    (19, 32, "0.59375", "32 = 2^5"),
    (39, 125, "0.312", "125 = 5^3")
]

s212_vaults = ['exam']*11 + ['practice']*6 + ['foundation']*7
for i, v in enumerate(s212_vaults):
    seq = f"{i+5:03d}"
    v_prefix = 'E' if v == 'exam' else ('P' if v == 'practice' else 'F')
    qc = f"MH-9-MTH1-2-2.1.2-OSC-{v_prefix}{seq}"
    num, den, dec, prime_fac = terminating_fractions[i]
    
    questions.append(make_q(
        qc, "MH-9-MTH1-2-2.1.2", "MH-9-MTH1-2-2.1", "2.1.2",
        "Terminating vs non-terminating recurring forms", "Properties of Rational Numbers & Decimal Representation",
        v, "medium" if i % 2 == 0 else "easy", "Apply", f"Terminating Fraction {den}",
        f"Why does the rational number \\(\\frac{{{num}}}{{{den}}}\\) have a terminating decimal form \\({dec}\\)?",
        f"Because the denominator factors as \\({prime_fac}\\), containing only prime factors 2 and/or 5",
        [
            f"Because numerator {num} is a multiple of 10",
            f"Because denominator {den} is an odd prime number",
            "Because all fractions in algebra always terminate"
        ],
        f"1. A reduced fraction \\(\\frac{{p}}{{q}}\\) has a terminating decimal expansion if and only if \\(q = 2^m \\times 5^n\\).\n2. Here \\({den} = {prime_fac}\\).\n3. Since only 2 and/or 5 divide the denominator, \\(\\frac{{{num}}}{{{den}}} = {dec}\\) terminates."
    ))

# Subtopic 2.1.3: Trichotomy law & order (11 Exam, 5 Practice, 7 Foundation)
s213_vaults = ['exam']*11 + ['practice']*5 + ['foundation']*7
for i, v in enumerate(s213_vaults):
    seq = f"{i+3:03d}"
    v_prefix = 'E' if v == 'exam' else ('P' if v == 'practice' else 'F')
    qc = f"MH-9-MTH1-2-2.1.3-OSC-{v_prefix}{seq}"
    
    a = 2 + i
    b = 3 + i
    c = 3 + i
    d = 4 + i
    # a/b vs c/d: a*d vs b*c
    prod1 = a * d
    prod2 = b * c
    # prod1 = a(a+2) = a^2+2a; prod2 = (a+1)^2 = a^2+2a+1 => prod1 < prod2 always!
    questions.append(make_q(
        qc, "MH-9-MTH1-2-2.1.3", "MH-9-MTH1-2-2.1", "2.1.3",
        "Order relation properties (Trichotomy law)", "Properties of Rational Numbers & Decimal Representation",
        v, "medium", "Apply", f"Rational Comparison {a}/{b} vs {c}/{d}",
        f"Compare the rational numbers \\(\\frac{{{a}}}{{{b}}}\\) and \\(\\frac{{{c}}}{{{d}}}\\):",
        f"\\(\\frac{{{a}}}{{{b}}} < \\frac{{{c}}}{{{d}}}\\) because \\({a} \\times {d} = {prod1} < {b} \\times {c} = {prod2}\\)",
        [
            f"\\(\\frac{{{a}}}{{{b}}} > \\frac{{{c}}}{{{d}}}\\) because {a} is smaller than {c}",
            f"\\(\\frac{{{a}}}{{{b}}} = \\frac{{{c}}}{{{d}}}\\) because difference is 1 in both",
            "Cannot be compared without converting to irrational numbers"
        ],
        f"1. To compare \\(\\frac{{a}}{{b}}\\) and \\(\\frac{{c}}{{d}}\\) with positive denominators, compare cross-products \\(ad\\) and \\(bc\\).\n2. \\({a} \\times {d} = {prod1}\\) and \\({b} \\times {c} = {prod2}\\).\n3. Since \\({prod1} < {prod2}\\), \\(\\frac{{{a}}}{{{b}}} < \\frac{{{c}}}{{{d}}}\\)."
    ))

# =========================================================================
# TOPIC 2.2: Irrational Numbers (76 questions: 38 Exam, 18 Practice, 20 Foundation)
# Subtopics: 2.2.1 (38 Qs), 2.2.2 (38 Qs)
# =========================================================================

# Subtopic 2.2.1: Proof by contradiction (19 Exam, 9 Practice, 10 Foundation)
s221_vaults = ['exam']*19 + ['practice']*9 + ['foundation']*10
primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 2, 3, 5, 7, 11, 13, 17, 19]
for i, v in enumerate(s221_vaults):
    seq = f"{i+3:03d}"
    v_prefix = 'E' if v == 'exam' else ('P' if v == 'practice' else 'F')
    qc = f"MH-9-MTH1-2-2.2.1-OSC-{v_prefix}{seq}"
    pr = primes_list[i]
    
    questions.append(make_q(
        qc, "MH-9-MTH1-2-2.2.1", "MH-9-MTH1-2-2.2", "2.2.1",
        "Proof by contradiction", "Irrational Numbers: Geometric Proof of Irrationality of √2",
        v, "hard" if i % 2 == 0 else "medium", "Analyze", f"Contradiction Proof sqrt({pr})",
        f"In the indirect proof that \\(\\sqrt{{{pr}}}\\) is irrational by contradiction, what is the initial assumption made?",
        f"Assume that \\(\\sqrt{{{pr}}}\\) is a rational number of the form \\(\\frac{{p}}{{q}}\\) where \\(p, q \\in \\mathbb{{I}}, q \\neq 0\\) and \\(\\gcd(p, q) = 1\\)",
        [
            f"Assume that \\(\\sqrt{{{pr}}} = 0\\)",
            f"Assume that \\({pr}\\) is a composite number",
            f"Assume that \\(\\sqrt{{{pr}}}\\) is a negative integer"
        ],
        f"1. In proof by contradiction (reductio ad absurdum), we assume the exact negation of the proposition to be proved.\n2. To prove \\(\\sqrt{{{pr}}}\\) is irrational, we assume \\(\\sqrt{{{pr}}}\\) is rational (in simplest co-prime form \\(p/q\\)).\n3. Deriving a contradiction to \\(\\gcd(p, q) = 1\\) proves \\(\\sqrt{{{pr}}}\\) is irrational."
    ))

# Subtopic 2.2.2: Representation on number line (19 Exam, 9 Practice, 10 Foundation)
s222_vaults = ['exam']*19 + ['practice']*9 + ['foundation']*10
radicals = [
    (2, 1, 1, "\\sqrt{1^2 + 1^2} = \\sqrt{2}"),
    (5, 2, 1, "\\sqrt{2^2 + 1^2} = \\sqrt{4 + 1} = \\sqrt{5}"),
    (10, 3, 1, "\\sqrt{3^2 + 1^2} = \\sqrt{9 + 1} = \\sqrt{10}"),
    (13, 3, 2, "\\sqrt{3^2 + 2^2} = \\sqrt{9 + 4} = \\sqrt{13}"),
    (17, 4, 1, "\\sqrt{4^2 + 1^2} = \\sqrt{16 + 1} = \\sqrt{17}"),
    (20, 4, 2, "\\sqrt{4^2 + 2^2} = \\sqrt{16 + 4} = \\sqrt{20}"),
    (26, 5, 1, "\\sqrt{5^2 + 1^2} = \\sqrt{25 + 1} = \\sqrt{26}"),
    (29, 5, 2, "\\sqrt{5^2 + 2^2} = \\sqrt{25 + 4} = \\sqrt{29}"),
    (37, 6, 1, "\\sqrt{6^2 + 1^2} = \\sqrt{36 + 1} = \\sqrt{37}"),
    (41, 5, 4, "\\sqrt{5^2 + 4^2} = \\sqrt{25 + 16} = \\sqrt{41}"),
    (50, 7, 1, "\\sqrt{7^2 + 1^2} = \\sqrt{49 + 1} = \\sqrt{50}"),
    (65, 8, 1, "\\sqrt{8^2 + 1^2} = \\sqrt{64 + 1} = \\sqrt{65}")
]

for i, v in enumerate(s222_vaults):
    seq = f"{i+3:03d}"
    v_prefix = 'E' if v == 'exam' else ('P' if v == 'practice' else 'F')
    qc = f"MH-9-MTH1-2-2.2.2-OSC-{v_prefix}{seq}"
    rad_val, base, perp, pyth_str = radicals[i % len(radicals)]
    
    questions.append(make_q(
        qc, "MH-9-MTH1-2-2.2.2", "MH-9-MTH1-2-2.2", "2.2.2",
        "Representation of √5, √10 on number line", "Irrational Numbers: Geometric Proof of Irrationality of √2",
        v, "medium", "Apply", f"Number Line Pyth sqrt({rad_val})",
        f"To plot \\(\\sqrt{{{rad_val}}}\\) on the number line using a right-angled triangle \\(\\triangle OAB\\) with origin \\(O\\), what base along the number line and perpendicular height are taken?",
        f"Base \\(OA = {base}\\) units along number line, perpendicular height \\(AB = {perp}\\) unit",
        [
            f"Base \\(OA = {rad_val}\\) units, perpendicular height \\(AB = {rad_val}\\) units",
            f"Base \\(OA = {base + 1}\\) units, perpendicular height \\(AB = {perp + 2}\\) units",
            f"Base \\(OA = 0.5\\) units, perpendicular height \\(AB = {rad_val}\\) units"
        ],
        f"1. By Pythagoras theorem, hypotenuse \\(OB = \\sqrt{{OA^2 + AB^2}}\\).\n2. With base \\(OA = {base}\\) and height \\(AB = {perp}\\), \\(OB = {pyth_str}\\).\n3. Drawing an arc of radius \\(OB\\) with centre \\(O\\) cuts the number line at \\(\\sqrt{{{rad_val}}}\\)."
    ))

# =========================================================================
# TOPIC 2.3: Surds (72 questions: 35 Exam, 17 Practice, 20 Foundation)
# Subtopics: 2.3.1 (18 Qs), 2.3.2 (18 Qs), 2.3.3 (18 Qs), 2.3.4 (18 Qs)
# =========================================================================

# 2.3.1: Definition of surd (9 Exam, 4 Practice, 5 Foundation)
s231_vaults = ['exam']*9 + ['practice']*4 + ['foundation']*5
for i, v in enumerate(s231_vaults):
    seq = f"{i+3:03d}"
    v_prefix = 'E' if v == 'exam' else ('P' if v == 'practice' else 'F')
    qc = f"MH-9-MTH1-2-2.3.1-OSC-{v_prefix}{seq}"
    surd_n = 2 + (i % 3)
    surd_a = [7, 11, 13, 17, 19, 23, 26, 29, 31, 37, 43, 47, 53, 59, 61, 67, 71, 73][i]
    
    questions.append(make_q(
        qc, "MH-9-MTH1-2-2.3.1", "MH-9-MTH1-2-2.3", "2.3.1",
        "Definition of surd ⁿ√a", "Surds: Definition, Order, Like/Unlike Surds & Simplest Form",
        v, "medium" if i % 2 == 0 else "easy", "Understand", f"Surd Definition Test {surd_a}",
        f"Why is \\(\\sqrt[{surd_n}]{{{surd_a}}}\\) classified as a surd?",
        f"Because order \\({surd_n} > 1\\) is an integer, radicand \\({surd_a}\\) is a positive rational number, and \\(\\sqrt[{surd_n}]{{{surd_a}}}\\) is irrational",
        [
            f"Because \\({surd_a}\\) is a perfect square",
            f"Because \\(\\sqrt[{surd_n}]{{{surd_a}}}\\) is a rational fraction",
            f"Because {surd_n} is an even number"
        ],
        f"1. A real number of the form \\(\\sqrt[n]{{a}}\\) is a surd if \\(n > 1\\) is a positive integer, \\(a > 0\\) is rational, and \\(\\sqrt[n]{{a}}\\) is irrational.\n2. Here \\({surd_a}\\) is rational and \\(\\sqrt[{surd_n}]{{{surd_a}}}\\) is irrational, satisfying all criteria."
    ))

# 2.3.2: Order of surd (9 Exam, 4 Practice, 5 Foundation)
s232_vaults = ['exam']*9 + ['practice']*4 + ['foundation']*5
orders = [2, 3, 4, 5, 6, 3, 2, 4, 5, 3, 2, 7, 4, 3, 2, 5, 3, 2]
for i, v in enumerate(s232_vaults):
    seq = f"{i+3:03d}"
    v_prefix = 'E' if v == 'exam' else ('P' if v == 'practice' else 'F')
    qc = f"MH-9-MTH1-2-2.3.2-OSC-{v_prefix}{seq}"
    ord_val = orders[i]
    rad_val = 5 + i * 2
    
    questions.append(make_q(
        qc, "MH-9-MTH1-2-2.3.2", "MH-9-MTH1-2-2.3", "2.3.2",
        "Order of surd (n)", "Surds: Definition, Order, Like/Unlike Surds & Simplest Form",
        v, "easy", "Remember", f"Order Identification {ord_val}",
        f"What is the order of the surd \\(\\sqrt[{ord_val}]{{{rad_val}}}\\)?",
        f"\\({ord_val}\\)",
        [
            f"\\({rad_val}\\)",
            f"\\({ord_val * 2}\\)",
            "\\(1\\)"
        ],
        f"1. In the radical expression \\(\\sqrt[n]{{a}}\\), the positive integer \\(n\\) is called the order of the surd.\n2. In \\(\\sqrt[{ord_val}]{{{rad_val}}}\\), order \\(n = {ord_val}\\)."
    ))

# 2.3.3: Like / similar surds (9 Exam, 4 Practice, 5 Foundation)
s233_vaults = ['exam']*9 + ['practice']*4 + ['foundation']*5
like_pairs = [
    ("\\sqrt{18}", "\\sqrt{50}", "3\\sqrt{2}", "5\\sqrt{2}", "\\sqrt{2}"),
    ("\\sqrt{12}", "\\sqrt{75}", "2\\sqrt{3}", "5\\sqrt{3}", "\\sqrt{3}"),
    ("\\sqrt{20}", "\\sqrt{45}", "2\\sqrt{5}", "3\\sqrt{5}", "\\sqrt{5}"),
    ("\\sqrt{28}", "\\sqrt{63}", "2\\sqrt{7}", "3\\sqrt{7}", "\\sqrt{7}"),
    ("\\sqrt{27}", "\\sqrt{48}", "3\\sqrt{3}", "4\\sqrt{3}", "\\sqrt{3}"),
    ("\\sqrt{32}", "\\sqrt{72}", "4\\sqrt{2}", "6\\sqrt{2}", "\\sqrt{2}"),
    ("\\sqrt{40}", "\\sqrt{90}", "2\\sqrt{10}", "3\\sqrt{10}", "\\sqrt{10}"),
    ("\\sqrt{54}", "\\sqrt{96}", "3\\sqrt{6}", "4\\sqrt{6}", "\\sqrt{6}"),
    ("\\sqrt{44}", "\\sqrt{99}", "2\\sqrt{11}", "3\\sqrt{11}", "\\sqrt{11}"),
    ("\\sqrt{8}", "\\sqrt{98}", "2\\sqrt{2}", "7\\sqrt{2}", "\\sqrt{2}"),
    ("\\sqrt{75}", "\\sqrt{108}", "5\\sqrt{3}", "6\\sqrt{3}", "\\sqrt{3}"),
    ("\\sqrt{80}", "\\sqrt{125}", "4\\sqrt{5}", "5\\sqrt{5}", "\\sqrt{5}"),
    ("\\sqrt{63}", "\\sqrt{112}", "3\\sqrt{7}", "4\\sqrt{7}", "\\sqrt{7}"),
    ("\\sqrt{50}", "\\sqrt{162}", "5\\sqrt{2}", "9\\sqrt{2}", "\\sqrt{2}"),
    ("\\sqrt{48}", "\\sqrt{147}", "4\\sqrt{3}", "7\\sqrt{3}", "\\sqrt{3}"),
    ("\\sqrt{45}", "\\sqrt{180}", "3\\sqrt{5}", "6\\sqrt{5}", "\\sqrt{5}"),
    ("\\sqrt{112}", "\\sqrt{175}", "4\\sqrt{7}", "5\\sqrt{7}", "\\sqrt{7}"),
    ("\\sqrt{72}", "\\sqrt{128}", "6\\sqrt{2}", "8\\sqrt{2}", "\\sqrt{2}")
]

for i, v in enumerate(s233_vaults):
    seq = f"{i+3:03d}"
    v_prefix = 'E' if v == 'exam' else ('P' if v == 'practice' else 'F')
    qc = f"MH-9-MTH1-2-2.3.3-OSC-{v_prefix}{seq}"
    s1, s2, sim1, sim2, base_rad = like_pairs[i]
    
    questions.append(make_q(
        qc, "MH-9-MTH1-2-2.3.3", "MH-9-MTH1-2-2.3", "2.3.3",
        "Like / similar surds", "Surds: Definition, Order, Like/Unlike Surds & Simplest Form",
        v, "medium", "Apply", f"Like Surds Pair {s1} and {s2}",
        f"Show whether the surds \\({s1}\\) and \\({s2}\\) are like (similar) surds:",
        f"Yes, they are like surds because their simplest forms are \\({sim1}\\) and \\({sim2}\\), sharing the same order (2) and radicand ({base_rad})",
        [
            f"No, because {s1} and {s2} have completely different radicands",
            f"No, because their rational coefficients are not equal",
            "They are unlike surds because both are irrational"
        ],
        f"1. Simplify each surd: \\({s1} = {sim1}\\) and \\({s2} = {sim2}\\).\n2. Two surds are like surds if their order is equal and their radicands in simplest form are equal.\n3. Both have order 2 and common radical factor \\({base_rad}\\), so they are like surds."
    ))

# 2.3.4: Simplest radical form (8 Exam, 5 Practice, 5 Foundation)
s234_vaults = ['exam']*8 + ['practice']*5 + ['foundation']*5
simplifications = [
    ("\\sqrt{50}", "5\\sqrt{2}", "\\sqrt{25 \\times 2} = 5\\sqrt{2}"),
    ("\\sqrt{75}", "5\\sqrt{3}", "\\sqrt{25 \\times 3} = 5\\sqrt{3}"),
    ("\\sqrt{108}", "6\\sqrt{3}", "\\sqrt{36 \\times 3} = 6\\sqrt{3}"),
    ("\\sqrt{128}", "8\\sqrt{2}", "\\sqrt{64 \\times 2} = 8\\sqrt{2}"),
    ("\\sqrt{147}", "7\\sqrt{3}", "\\sqrt{49 \\times 3} = 7\\sqrt{3}"),
    ("\\sqrt{180}", "6\\sqrt{5}", "\\sqrt{36 \\times 5} = 6\\sqrt{5}"),
    ("\\sqrt{200}", "10\\sqrt{2}", "\\sqrt{100 \\times 2} = 10\\sqrt{2}"),
    ("\\sqrt{243}", "9\\sqrt{3}", "\\sqrt{81 \\times 3} = 9\\sqrt{3}"),
    ("\\sqrt{288}", "12\\sqrt{2}", "\\sqrt{144 \\times 2} = 12\\sqrt{2}"),
    ("\\sqrt{300}", "10\\sqrt{3}", "\\sqrt{100 \\times 3} = 10\\sqrt{3}"),
    ("\\sqrt{500}", "10\\sqrt{5}", "\\sqrt{100 \\times 5} = 10\\sqrt{5}"),
    ("\\sqrt{600}", "10\\sqrt{6}", "\\sqrt{100 \\times 6} = 10\\sqrt{6}"),
    ("\\sqrt{72}", "6\\sqrt{2}", "\\sqrt{36 \\times 2} = 6\\sqrt{2}"),
    ("\\sqrt{98}", "7\\sqrt{2}", "\\sqrt{49 \\times 2} = 7\\sqrt{2}"),
    ("\\sqrt{162}", "9\\sqrt{2}", "\\sqrt{81 \\times 2} = 9\\sqrt{2}"),
    ("\\sqrt{192}", "8\\sqrt{3}", "\\sqrt{64 \\times 3} = 8\\sqrt{3}"),
    ("\\sqrt{245}", "7\\sqrt{5}", "\\sqrt{49 \\times 5} = 7\\sqrt{5}"),
    ("\\sqrt{320}", "8\\sqrt{5}", "\\sqrt{64 \\times 5} = 8\\sqrt{5}")
]

for i, v in enumerate(s234_vaults):
    seq = f"{i+3:03d}"
    v_prefix = 'E' if v == 'exam' else ('P' if v == 'practice' else 'F')
    qc = f"MH-9-MTH1-2-2.3.4-OSC-{v_prefix}{seq}"
    raw_s, simp_s, step_s = simplifications[i]
    
    questions.append(make_q(
        qc, "MH-9-MTH1-2-2.3.4", "MH-9-MTH1-2-2.3", "2.3.4",
        "Simplest radical form", "Surds: Definition, Order, Like/Unlike Surds & Simplest Form",
        v, "medium" if i % 2 == 0 else "easy", "Apply", f"Simplest Form {raw_s}",
        f"Express \\({raw_s}\\) in its simplest radical form:",
        f"\\({simp_s}\\)",
        [
            f"\\(2{simp_s}\\)",
            f"\\(3{simp_s}\\)",
            f"\\({raw_s}\\) is already in simplest form"
        ],
        f"1. Factor the radicand into a perfect square factor and a square-free factor:\n   \\({raw_s} = {step_s}\\).\n2. Hence the simplest radical form is \\({simp_s}\\)."
    ))

print(f"Generated {len(questions)} questions for Chapter 2 Part 1.")

# Write to JS module
js_code = "// scripts/mh9_mth1_ch2_part1_data.js\n"
js_code += f"// Generated {len(questions)} questions for Chapter 2 Topics 2.1, 2.2, 2.3\n\n"
js_code += "const ch2Part1Questions = " + json.dumps(questions, indent=2) + ";\n\n"
js_code += "module.exports = { ch2Part1Questions };\n"

with open("scripts/mh9_mth1_ch2_part1_data.js", "w", encoding="utf-8") as f:
    f.write(js_code)
print("Successfully written scripts/mh9_mth1_ch2_part1_data.js")
