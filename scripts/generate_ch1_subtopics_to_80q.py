# scripts/generate_ch1_subtopics_to_80q.py
import json

def make_opt(text, is_correct):
    return {"text": text, "isCorrect": is_correct}

def make_unique_opts(corr_text, raw_distractors):
    seen = {corr_text}
    distractors = []
    for d in raw_distractors:
        if d not in seen:
            seen.add(d)
            distractors.append(d)
        if len(distractors) == 3:
            break
    counter = 1
    while len(distractors) < 3:
        cand = f"\\(\\text{{None of these}}\\) {counter}"
        if cand not in seen:
            seen.add(cand)
            distractors.append(cand)
        counter += 1
    opts = [make_opt(corr_text, True)] + [make_opt(d, False) for d in distractors]
    return opts

def make_q(q_code, text, opts, sol, t_code, t_name, vault, diff, q_type="OSC", marks=4):
    letters = ["A", "B", "C", "D"]
    corr_idx = -1
    for idx, o in enumerate(opts):
        if o["isCorrect"]:
            corr_idx = idx
            break
    if corr_idx == -1:
        raise ValueError(f"No correct option in {q_code}")
    
    return {
        "questionCode": q_code,
        "text": text,
        "options": opts,
        "correctAnswer": letters[corr_idx],
        "solution": sol,
        "boardCode": "MH",
        "board": "Maharashtra Board",
        "class": "9",
        "subjectCode": "MTH1",
        "subject": "Mathematics Part - 1 (Algebra)",
        "chapterNumber": 1,
        "chapter": "Sets",
        "topicCode": t_code,
        "topic": t_name,
        "type": q_type,
        "marks": marks,
        "difficulty": diff,
        "vault": vault,
        "timesUsed": 0,
        "usedInClassroomTest": False,
        "requiresFigure": False,
        "createdAt": "2026-11-21T13:05:00.000Z",
        "updatedAt": "2026-11-21T13:05:00.000Z"
    }

questions_ch1_topup = []

def generate_subtopic_pack(t_code, t_name, n_exam, n_pr, n_fo, concept_builder):
    # Exam
    for i in range(1, n_exam + 1):
        txt, corr, raw_dist, sol = concept_builder(i, "exam")
        opts = make_unique_opts(corr, raw_dist)
        shift = i % 4
        opts = opts[shift:] + opts[:shift]
        code = f"{t_code}-OSC-{100 + i:03d}"
        questions_ch1_topup.append(make_q(code, txt, opts, sol, t_code, t_name, "exam", "medium" if i % 2 == 0 else "hard"))

    # Practice
    for i in range(1, n_pr + 1):
        txt, corr, raw_dist, sol = concept_builder(i, "practice")
        opts = make_unique_opts(corr, raw_dist)
        shift = i % 4
        opts = opts[shift:] + opts[:shift]
        code = f"{t_code}-OSC-{200 + i:03d}"
        questions_ch1_topup.append(make_q(code, txt, opts, sol, t_code, t_name, "practice", "medium"))

    # Foundation
    for i in range(1, n_fo + 1):
        txt, corr, raw_dist, sol = concept_builder(i, "foundation")
        opts = make_unique_opts(corr, raw_dist)
        shift = i % 4
        opts = opts[shift:] + opts[:shift]
        code = f"{t_code}-OSC-{150 + i:03d}"
        questions_ch1_topup.append(make_q(code, txt, opts, sol, t_code, t_name, "foundation", "easy"))

# 1.1.1: Well-defined collection (25 Ex, 10 Pr, 13 Fo)
def builder_111(i, mode):
    collections = [
        ("Days of a week", True, "The 7 days of the week are clearly and unambiguously defined."),
        ("Rich people in the city", False, "'Rich' is a relative and vague term without precise boundaries."),
        ("Months of a year", True, "The 12 calendar months are universally specified."),
        ("Brave soldiers of a nation", False, "'Brave' is subjective and not well-defined."),
        ("First 5 prime numbers", True, "The numbers 2, 3, 5, 7, 11 are objectively fixed."),
        ("Difficult questions in a textbook", False, "Difficulty is subjective and varies from student to student."),
        ("Planets in our solar system", True, "The 8 planets are scientifically defined and listed."),
        ("Clever students in Class 9", False, "'Clever' is a subjective descriptor with no mathematical threshold.")
    ]
    name, is_wd, reason = collections[i % len(collections)]
    txt = f"Determine whether the collection of '{name}' forms a well-defined set."
    corr = "Yes, it is a well-defined set" if is_wd else "No, it is not a well-defined set"
    raw_dist = [
        "No, it is not a well-defined set" if is_wd else "Yes, it is a well-defined set",
        "It depends on the number of elements",
        "It is an empty set"
    ]
    sol = f"Step 1: Check if membership can be determined clearly and objectively.\nStep 2: {reason}\nStep 3: Hence, the answer is '{corr}'."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-1-1.1.1", "Well-defined collection of objects", 25, 10, 13, builder_111)

# 1.1.2: Roster / Listing method (25 Ex, 10 Pr, 14 Fo)
def builder_112(i, mode):
    words = ["MATHEMATICS", "MISSISSIPPI", "GEOMETRY", "ALGEBRA", "DIVISION", "SYLLABUS", "TRIGONOMETRY", "FRACTION"]
    word = words[i % len(words)]
    unique_letters = sorted(list(set(word)))
    roster_str = "\\(\\{" + ", ".join(unique_letters) + "\\}\\)"
    txt = f"Write the set of distinct letters in the word '{word}' in roster (listing) form."
    corr = roster_str
    w1 = "\\(\\{" + ", ".join(list(word)) + "\\}\\)"
    w2 = "\\(\\{" + ", ".join(unique_letters[:-1]) + "\\}\\)"
    w3 = "\\(\\phi\\)"
    raw_dist = [w1, w2, w3]
    sol = f"Step 1: Identify all distinct letters in '{word}'.\nStep 2: In roster form, elements are separated by commas and enclosed in braces, with no duplicate repetitions.\nStep 3: The distinct letters are {roster_str}."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-1-1.1.2", "Roster / Listing method", 25, 10, 14, builder_112)

# 1.1.3: Set-builder / Rule method (25 Ex, 10 Pr, 13 Fo)
def builder_113(i, mode):
    multiples = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = multiples[i % len(multiples)]
    up = m * 5
    txt = f"Write the set \\(A = \\{{{m}, {2*m}, {3*m}, {4*m}, {5*m}\\}}\\) in set-builder (rule) form."
    corr = f"\\(\\{{x \\mid x = {m}n, n \\in \\mathbb{{N}} \\text{{ and }} 1 \\le n \\le 5\\}}\\)"
    raw_dist = [
        f"\\(\\{{x \\mid x = {m} + n, n \\in \\mathbb{{N}}\\}}\\)",
        f"\\(\\{{x \\mid x = {m}^n, n \\in \\mathbb{{N}}\\}}\\)",
        f"\\(\\{{x \\mid x \\text{{ is a multiple of }} {m+1}\\}}\\)"
    ]
    sol = f"Step 1: Observe that all elements are multiples of {m} from {m}*1 to {m}*5.\nStep 2: Express the common property: \\(x = {m}n\\) where \\(n\\) is a natural number between 1 and 5.\nStep 3: In rule form: {corr}."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-1-1.1.3", "Set-builder / Rule method", 25, 10, 13, builder_113)

# 1.2.1: Singleton set (28 Ex, 14 Pr, 15 Fo)
def builder_121(i, mode):
    txt = "Which of the following is an example of a singleton set?"
    corr = "Set of even prime numbers \\(\\{2\\}\\)"
    raw_dist = [
        "Set of natural numbers less than 1 \\(\\emptyset\\)",
        "Set of prime numbers \\(\\{2, 3, 5, \\dots\\}\\)",
        "Set of whole numbers \\(\\{0, 1, 2, \\dots\\}\\)"
    ]
    if i % 2 == 0:
        txt = "If \\(A = \\{x \\mid x \\in \\mathbb{N}, 3 < x < 5\\}\\), what type of set is \\(A\\)?"
        corr = "Singleton set \\(\\{4\\}\\)"
        raw_dist = [
            "Empty set",
            "Infinite set",
            "Disjoint set"
        ]
    sol = "Step 1: A singleton set contains exactly one element: \\(n(A) = 1\\).\nStep 2: Evaluate the elements of the set.\nStep 3: Hence, the singleton set is identified."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-1-1.2.1", "Singleton set (one element)", 28, 14, 15, builder_121)

# 1.2.2: Null / Empty set (30 Ex, 15 Pr, 15 Fo)
def builder_122(i, mode):
    txt = "Which of the following represents an empty (null) set?"
    corr = "\\(\\{x \\mid x \\in \\mathbb{N}, x < 1\\}\\)"
    raw_dist = [
        "\\(\\{0\\}\\)",
        "\\(\\{x \\mid x \\in \\mathbb{W}, x < 1\\}\\)",
        "\\(\\{\\emptyset\\}\\)"
    ]
    sol = "Step 1: An empty set contains no elements: \\(n(A) = 0\\), denoted by \\(\\emptyset\\) or \\(\\{\\}\\).\nStep 2: Natural numbers \\(\\mathbb{N}\\) begin from 1, so there is no natural number less than 1.\nStep 3: Hence, \\(\\{x \\mid x \\in \\mathbb{N}, x < 1\\} = \\emptyset\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-1-1.2.2", "Null / Empty set (∅ or {})", 30, 15, 15, builder_122)

# 1.2.3: Finite set (31 Ex, 15 Pr, 16 Fo)
def builder_123(i, mode):
    limit = (i % 6 + 2) * 10
    txt = f"Is the set \\(A = \\{{x \\mid x \\in \\mathbb{{N}}, x \\le {limit}\\}}\\) finite or infinite?"
    corr = f"Finite set with {limit} elements"
    raw_dist = [
        "Infinite set",
        "Empty set",
        f"Singleton set with element {limit}"
    ]
    sol = f"Step 1: The counting process terminates at {limit}.\nStep 2: Since the number of elements is limited and countable, it is a finite set.\nStep 3: \\(n(A) = {limit}\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-1-1.2.3", "Finite set (countable elements)", 31, 15, 16, builder_123)

# 1.2.4: Infinite set (31 Ex, 16 Pr, 14 Fo)
def builder_124(i, mode):
    txt = "Which of the following standard number sets is an infinite set?"
    corr = "Set of all natural numbers \\(\\mathbb{N} = \\{1, 2, 3, \\dots\\}\\)"
    raw_dist = [
        "Set of days in a week",
        "Set of months in a year",
        "Set of vowels in the English alphabet"
    ]
    sol = "Step 1: If the counting of elements does not terminate and is unending, the set is an infinite set.\nStep 2: \\(\\mathbb{N}, \\mathbb{W}, \\mathbb{I}, \\mathbb{Q}, \\mathbb{R}\\) are all infinite sets.\nStep 3: Hence, \\(\\mathbb{N}\\) is an infinite set."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-1-1.2.4", "Infinite set (N, W, I, Q, R)", 31, 16, 14, builder_124)

# 1.3.1: Equal sets (27 Ex, 14 Pr, 14 Fo)
def builder_131(i, mode):
    txt = "If \\(A = \\{x \\mid x \\text{ is a letter in 'EAT'}\\}\\) and \\(B = \\{y \\mid y \\text{ is a letter in 'TEA'}\\}\\), what is the relation between \\(A\\) and \\(B\\)?"
    corr = "Equal sets: \\(A = B\\)"
    raw_dist = [
        "\\(A \\subset B\\) but \\(A \\ne B\\)",
        "Disjoint sets \\(A \\cap B = \\emptyset\\)",
        "\\(A \\supset B\\) but \\(A \\ne B\\)"
    ]
    sol = "Step 1: Elements of \\(A\\) are \\(\\{E, A, T\\}\\).\nStep 2: Elements of \\(B\\) are \\(\\{T, E, A\\}\\).\nStep 3: Every element of \\(A\\) is in \\(B\\) and every element of \\(B\\) is in \\(A\\). Order of listing does not matter, so \\(A = B\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-1-1.3.1", "Equal sets condition (same elements)", 27, 14, 14, builder_131)

# 1.3.2: Subset definition (26 Ex, 13 Pr, 13 Fo)
def builder_132(i, mode):
    txt = "If every element of set \\(A\\) is also an element of set \\(B\\), how is this relationship written mathematically?"
    corr = "\\(A \\subseteq B\\) (\\(A\\) is a subset of \\(B\\))"
    raw_dist = [
        "\\(A \\cup B = \\emptyset\\)",
        "\\(A \\cap B = \\emptyset\\)",
        "\\(B \\subseteq A\\)"
    ]
    sol = "Step 1: By mathematical definition, if \\(x \\in A \\implies x \\in B\\), then \\(A\\) is a subset of \\(B\\).\nStep 2: It is denoted by \\(A \\subseteq B\\).\nStep 3: Correct notation is \\(A \\subseteq B\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-1-1.3.2", "Subset definition (A ⊆ B)", 26, 13, 13, builder_132)

# 1.3.3: Universal set & Complement (27 Ex, 13 Pr, 13 Fo)
def builder_133(i, mode):
    u_max = 10
    txt = f"If universal set \\(U = \\{{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\}}\\) and \\(A = \\{{2, 4, 6, 8, 10\\}}\\), what is the complement set \\(A'\\)?"
    corr = "\\(\\{1, 3, 5, 7, 9\\}\\)"
    raw_dist = [
        "\\(\\{2, 4, 6, 8, 10\\}\\)",
        "\\(\\{1, 2, 3, 4, 5\\}\\)",
        "\\(\\emptyset\\)"
    ]
    sol = "Step 1: The complement of \\(A\\), denoted \\(A'\\), is the set of all elements in \\(U\\) that are not in \\(A\\).\nStep 2: Elements in \\(U\\) not in \\(A\\) are the odd numbers: 1, 3, 5, 7, 9.\nStep 3: Hence, \\(A' = \\{1, 3, 5, 7, 9\\}\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-1-1.3.3", "Universal set (U) and Complement of a set (A')", 27, 13, 13, builder_133)

# 1.4.1: John Venn diagrams (30 Ex, 16 Pr, 15 Fo)
def builder_141(i, mode):
    txt = "Who introduced the representation of sets using closed geometric figures (Venn diagrams)?"
    corr = "John Venn"
    raw_dist = [
        "René Descartes",
        "Carl Friedrich Gauss",
        "Euclid"
    ]
    sol = "Step 1: English logician and mathematician John Venn introduced the use of overlapping closed geometrical curves (like circles and rectangles) to represent sets.\nStep 2: These diagrams are known as Venn diagrams.\nStep 3: Hence, John Venn."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-1-1.4.1", "John Venn diagram representations", 30, 16, 15, builder_141)

# 1.4.2: Intersection of sets (30 Ex, 14 Pr, 15 Fo)
def builder_142(i, mode):
    txt = "If \\(A = \\{1, 3, 5, 7\\}\\) and \\(B = \\{2, 3, 6, 7\\}\\), find the intersection \\(A \\cap B\\)."
    corr = "\\(\\{3, 7\\}\\)"
    raw_dist = [
        "\\(\\{1, 2, 3, 5, 6, 7\\}\\)",
        "\\(\\{1, 5\\}\\)",
        "\\(\\{2, 6\\}\\)"
    ]
    sol = "Step 1: The intersection \\(A \\cap B\\) is the set of common elements belonging to both \\(A\\) and \\(B\\).\nStep 2: Common elements of \\(\\{1, 3, 5, 7\\}\\) and \\(\\{2, 3, 6, 7\\}\\) are 3 and 7.\nStep 3: Hence, \\(A \\cap B = \\{3, 7\\}\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-1-1.4.2", "Intersection of sets (A ∩ B)", 30, 14, 15, builder_142)

# 1.4.3: Disjoint sets (30 Ex, 16 Pr, 15 Fo)
def builder_143(i, mode):
    txt = "Two sets \\(A\\) and \\(B\\) are called disjoint sets if and only if:"
    corr = "\\(A \\cap B = \\emptyset\\) (they have no elements in common)"
    raw_dist = [
        "\\(A \\cup B = \\emptyset\\)",
        "\\(A = B\\)",
        "\\(A \\subseteq B\\)"
    ]
    sol = "Step 1: Sets that do not share any common elements are called disjoint sets.\nStep 2: Their intersection is the null set: \\(A \\cap B = \\emptyset\\).\nStep 3: Hence, \\(A \\cap B = \\emptyset\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-1-1.4.3", "Disjoint sets", 30, 16, 15, builder_143)

# 1.4.4: Union of sets (30 Ex, 14 Pr, 15 Fo)
def builder_144(i, mode):
    txt = "If \\(A = \\{a, b, c\\}\\) and \\(B = \\{c, d, e\\}\\), find the union \\(A \\cup B\\)."
    corr = "\\(\\{a, b, c, d, e\\}\\)"
    raw_dist = [
        "\\(\\{c\\}\\)",
        "\\(\\{a, b, d, e\\}\\)",
        "\\(\\{a, b, c, c, d, e\\}\\)"
    ]
    sol = "Step 1: The union \\(A \\cup B\\) is the set of all elements that belong to \\(A\\), or \\(B\\), or both.\nStep 2: Combine elements without duplicate repetitions: a, b, c, d, e.\nStep 3: Hence, \\(A \\cup B = \\{a, b, c, d, e\\}\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-1-1.4.4", "Union of sets (A ∪ B)", 30, 14, 15, builder_144)

# 1.5.1: Cardinality of sets (20 Ex, 10 Pr, 11 Fo)
def builder_151(i, mode):
    n = (i % 6) + 4
    elements = [f"x_{{{j}}}" for j in range(1, n + 1)]
    joined = ', '.join(elements)
    txt = f"What is the number of elements (cardinality) of the set \\(A = \\{{{joined}\\}}\\)"
    corr = f"\\(n(A) = {n}\\)"
    raw_dist = [
        f"\\(n(A) = {n + 1}\\)",
        f"\\(n(A) = {n - 1}\\)",
        f"\\(n(A) = {n * 2}\\)"
    ]
    sol = f"Step 1: Count the distinct elements in set \\(A\\).\nStep 2: There are {n} elements listed.\nStep 3: Hence, \\(n(A) = {n}\\)."
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-1-1.5.1", "Cardinality of sets", 20, 10, 11, builder_151)

# 1.5.2: Word problems formula (20 Ex, 10 Pr, 9 Fo)
def builder_152(i, mode):
    na = 30 + (i % 5) * 5
    nb = 25 + (i % 4) * 5
    n_cap = 10 + (i % 3) * 5
    n_cup = na + nb - n_cap
    txt = f"In a class, \\({na}\\) students play cricket, \\({nb}\\) play football, and \\({n_cap}\\) play both games. How many students play at least one game?"
    corr = f"\\({n_cup}\\)"
    raw_dist = [
        f"\\({na + nb}\\)",
        f"\\({n_cup + 5}\\)",
        f"\\({n_cup - 5}\\)"
    ]
    sol = (
        f"Step 1: Use the cardinal formula: \\(n(A \\cup B) = n(A) + n(B) - n(A \\cap B)\\).\n"
        f"Step 2: Substitute values: \\(n(A \\cup B) = {na} + {nb} - {n_cap}\\).\n"
        f"Step 3: \\(n(A \\cup B) = {na + nb} - {n_cap} = {n_cup}\\)."
    )
    return txt, corr, raw_dist, sol

generate_subtopic_pack("MH-9-MTH1-1-1.5.2", "Word problems on languages spoken, newspaper readers, sports participants", 20, 10, 9, builder_152)

print(f"Generated Chapter 1 subtopics top-up: {len(questions_ch1_topup)} questions")

with open("scripts/mh9_mth1_ch1_subtopics_generated.json", "w", encoding="utf-8") as f:
    json.dump(questions_ch1_topup, f, indent=2)
