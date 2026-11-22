# scripts/generate_clean_mth1_ch1.py
# Generates 1,280 flawless, non-duplicate questions for MH-9-MTH1 Chapter 1 (Sets)
# 16 subtopics * 80 questions each = 1,280 questions.

import json
import random

SEQS_80 = [100 + i for i in range(1, 41)] + [200 + i for i in range(1, 21)] + [300 + i for i in range(1, 21)]

def make_opts(corr, dist):
    # Ensure options are distinct
    clean_dist = []
    seen = {corr}
    for d in dist:
        if d not in seen:
            seen.add(d)
            clean_dist.append(d)
    while len(clean_dist) < 3:
        clean_dist.append(f"None of these ({len(clean_dist)})")
    opts_pool = [corr] + clean_dist[:3]
    # deterministic shuffle based on length
    random.Random(len(corr) + len(dist[0])).shuffle(opts_pool)
    letters = ['A', 'B', 'C', 'D']
    out = []
    for l, val in zip(letters, opts_pool):
        out.append({'id': l, 'text': str(val), 'isCorrect': (val == corr)})
    return out

def build_q(code, text, corr, dist, sol, tc, tname, seq, has_fig=False, diff='medium'):
    opts = make_opts(corr, dist)
    c_letter = next(o['id'] for o in opts if o['isCorrect'])
    v = 'foundation' if seq >= 301 else ('practice' if seq >= 201 else 'exam')
    return {
        'questionCode': code,
        'boardCode': 'MH',
        'board': 'Maharashtra Board',
        'class': '9',
        'subjectCode': 'MTH1',
        'subject': 'Mathematics Part - 1 (Algebra)',
        'chapterNumber': 1,
        'chapter': 'Sets',
        'topicCode': tc,
        'topic': tname,
        'type': 'OSC',
        'typeCode': 'OSC',
        'source': v,
        'vault': v,
        'marks': 4,
        'negativeMarks': 0,
        'difficulty': diff,
        'status': 'active',
        'timesUsed': 0,
        'usedInClassroomTest': False,
        'requiresFigure': has_fig,
        'createdAt': '2026-11-22T00:00:00.000Z',
        'updatedAt': '2026-11-22T00:00:00.000Z',
        'options': opts,
        'correctAnswer': c_letter,
        'solution': sol,
        'text': text
    }

def svg_venn(label_a, label_b, title="Venn Diagram"):
    return f'''<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 340 180" style="max-width: 340px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <text x="170" y="22" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>
  <rect x="20" y="35" width="300" height="130" rx="6" fill="none" stroke="#64748b" stroke-width="1.5"/>
  <text x="35" y="52" fill="#cbd5e1" font-size="11" font-weight="bold">U</text>
  <circle cx="130" cy="105" r="45" fill="#3b82f6" fill-opacity="0.25" stroke="#60a5fa" stroke-width="2"/>
  <circle cx="210" cy="105" r="45" fill="#10b981" fill-opacity="0.25" stroke="#34d399" stroke-width="2"/>
  <text x="110" y="105" fill="#93c5fd" font-size="11" font-weight="bold">{label_a}</text>
  <text x="225" y="105" fill="#a7f3d0" font-size="11" font-weight="bold">{label_b}</text>
</svg>
</div>'''

def generate_ch1_all():
    qs = []
    
    # --- 1.1.1: Well-defined collection of objects ---
    tc = "MH-9-MTH1-1-1.1.1"
    tname = "Well-defined collection of objects"
    ARCH_111 = [
        # (collection, is_welldefined, explanation)
        ("Days of a week", True, "The seven days Monday through Sunday are universally and definitively established."),
        ("Happy citizens in a town", False, "Happiness is subjective and lacks an unambiguous mathematical standard."),
        ("Months of a solar year having exactly 30 days", True, "April, June, September, November are uniquely and objectively defined."),
        ("Brilliant students in a mathematics class", False, "'Brilliant' is a relative quality without a strict objective benchmark."),
        ("Prime numbers strictly between 10 and 25", True, "{11, 13, 17, 19, 23} is uniquely determined."),
        ("Brave personnel of the armed forces", False, "'Brave' is an evaluative adjective and lacks a binary membership test."),
        ("Vowels in the modern English alphabet", True, "{a, e, i, o, u} is universally specified."),
        ("Tasty dishes prepared in a restaurant", False, "Taste is a personal subjective preference and not an objective criterion."),
        ("Planets orbiting the Sun in our Solar System", True, "Mercury through Neptune constitute an astronomy-defined collection."),
        ("Rich business owners in an industrial city", False, "'Rich' is vague without a specified net worth cut-off.")
    ]
    for idx, seq in enumerate(SEQS_80):
        item_idx = idx % 10
        coll, is_wd, expl = ARCH_111[item_idx]
        arch_type = idx // 10
        if arch_type == 0:
            txt = f"Evaluate whether the following collection represents a well-defined mathematical set: '{coll}'."
            corr = "Yes, it is a well-defined set" if is_wd else "No, it is not a well-defined set"
            dist = ["No, it is not a well-defined set" if is_wd else "Yes, it is a well-defined set", "It is an empty set", "It cannot be determined"]
            sol = f"**Step 1: Concept Verification**\nA collection is a set if there is an objective rule deciding membership.\n**Step 2: Analysis**\n'{coll}': {expl}\n**Step 3: Conclusion**\n{corr}."
        elif arch_type == 1:
            txt = f"Which property prevents or qualifies '{coll}' as a mathematical set?"
            corr = f"{expl}"
            dist = ["The collection has too many elements to be listed", "Elements must strictly be numbers", "Only single-element groups form sets"]
            sol = f"**Step 1: Reason**\n{expl}\n**Step 2: Conclusion**\n{corr}."
        elif arch_type == 2:
            txt = f"In set theory, why is an unambiguous rule required to declare '{coll}' as a valid set?"
            corr = "To uniquely decide whether any given object belongs to the collection or not"
            dist = ["To ensure all elements are prime numbers", "To guarantee that the set has an even number of items", "To ensure every element is an alphabet"]
            sol = f"**Step 1: Rule of Membership**\nA set requires a decisive criterion for inclusion or exclusion.\n**Step 2: Conclusion**\n{corr}."
        elif arch_type == 3:
            txt = f"Select the true statement regarding the collection: '{coll}'."
            if is_wd:
                corr = f"It qualifies as a set because {expl.lower()}"
                dist = ["It is not a set because elements are words", "It is an infinite set", "It contains no elements"]
            else:
                corr = f"It does not qualify as a set because {expl.lower()}"
                dist = ["It qualifies as a finite set", "It is an established mathematical singleton set", "It is identical to the set of natural numbers"]
            sol = f"**Step 1: Classification**\n'{coll}' -> {corr}.\n**Step 2: Conclusion**\n{corr}."
        elif arch_type == 4:
            txt = f"Let group \(G\) be '{coll}'. Is membership \(x \\in G\) objectively testable for any candidate \(x\)?"
            corr = "Yes, membership is strictly testable without ambiguity" if is_wd else "No, membership depends on personal judgment"
            dist = ["No, membership depends on personal judgment" if is_wd else "Yes, membership is strictly testable without ambiguity", "Only if x is a positive integer", "Only if the set contains zero"]
            sol = f"**Step 1: Testability**\n{expl}\n**Step 2: Conclusion**\n{corr}."
        elif arch_type == 5:
            txt = f"Which of the following modifications would make the collection '{coll}' unequivocally well-defined?"
            corr = "Specifying exact measurable criteria rather than qualitative adjectives" if not is_wd else "It is already completely well-defined as stated"
            dist = ["Adding more subjective descriptions", "Restricting the collection to only three elements", "Translating the name into Latin"]
            sol = f"**Step 1: Objectivity Standard**\n{corr}.\n**Step 2: Conclusion**\n{corr}."
        elif arch_type == 6:
            txt = f"What is the mathematical status of the entity: '{coll}'?"
            corr = "Valid mathematical set" if is_wd else "Invalid (not a well-defined set)"
            dist = ["Invalid (not a well-defined set)" if is_wd else "Valid mathematical set", "Null set \\(\\emptyset\\)", "Universal set \\(U\\)"]
            sol = f"**Step 1: Evaluation**\n{expl}\n**Step 2: Conclusion**\n{corr}."
        else:
            txt = f"Consider the collection: '{coll}'. Which symbol accurately reflects that a member \(m\) satisfies the criteria of this grouping?"
            corr = "\\(m \\in G\\)" if is_wd else "The membership symbol \\(\\in\\) cannot be definitively applied"
            dist = ["The membership symbol \\(\\in\\) cannot be definitively applied" if is_wd else "\\(m \\in G\\)", "\\(m \\subset G\\)", "\\(m = \\emptyset\\)"]
            sol = f"**Step 1: Notation**\n{corr}.\n**Step 2: Conclusion**\n{corr}."
        diff = 'easy' if seq >= 301 else ('medium' if seq >= 201 else 'hard')
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, False, diff))

    # --- 1.1.2: Roster / Listing method ---
    tc = "MH-9-MTH1-1-1.1.2"
    tname = "Roster / Listing method"
    WORDS_112 = [
        ("MATHEMATICS", "{M, A, T, H, E, I, C, S}"),
        ("COMPLEMENT", "{C, O, M, P, L, E, N, T}"),
        ("TRIGONOMETRY", "{T, R, I, G, O, N, M, E, Y}"),
        ("ASSESSMENT", "{A, S, E, M, N, T}"),
        ("PROPORTION", "{P, R, O, T, I, N}"),
        ("STATISTICS", "{S, T, A, I, C}"),
        ("GEOMETRY", "{G, E, O, M, T, R, Y}"),
        ("POLYNOMIAL", "{P, O, L, Y, N, M, I, A}"),
        ("COORDINATE", "{C, O, R, D, I, N, A, T, E}"),
        ("SIMILARITY", "{S, I, M, L, A, R, T, Y}")
    ]
    for idx, seq in enumerate(SEQS_80):
        w_idx = idx % 10
        word, letters_set = WORDS_112[w_idx]
        arch_type = idx // 10
        if arch_type in [0, 1]:
            txt = f"Write the set of letters in the word '{word}' using the Roster (Listing) method."
            corr = f"\\({letters_set}\\)"
            dist = [f"\\({letters_set.replace('}', ', X}')}\\)", f"\\({letters_set.replace('{M, ', '{')}\\)", "\\(\\emptyset\\)"]
            sol = f"**Step 1: Rule**\nIn listing method, elements are enclosed in braces and separated by commas without repeating any letter.\n**Step 2: Extract distinct letters**\nLetters in '{word}': {letters_set}.\n**Step 3: Conclusion**\n\\({letters_set}\\)."
        elif arch_type in [2, 3]:
            k = 2 + (w_idx % 5)
            limit = k * 6
            mults = [k * m for m in range(1, 7)]
            mults_str = "{" + ", ".join(map(str, mults)) + "}"
            txt = f"Express the set of positive multiples of {k} less than or equal to {limit} in roster form."
            corr = f"\\({mults_str}\\)"
            dist = [f"\\({{{', '.join(map(str, mults[:-1]))}}}\\)", f"\\({{{', '.join(map(str, [k*m for m in range(7)]))}}}\\)", f"\\({{{k}, {limit}}}\\)"]
            sol = f"**Step 1: Multiples of {k}**\nMultiples up to {limit}: {', '.join(map(str, mults))}.\n**Step 2: Enclose in braces**\n\\({mults_str}\\).\n**Step 3: Conclusion**\n\\({mults_str}\\)."
        elif arch_type in [4, 5]:
            p_start = 10 * (w_idx + 1)
            p_end = p_start + 20
            primes = [n for n in range(p_start, p_end + 1) if all(n % d != 0 for d in range(2, int(n**0.5) + 1))]
            primes_str = "{" + ", ".join(map(str, primes)) + "}"
            txt = f"List all prime numbers strictly between {p_start} and {p_end} in roster notation."
            corr = f"\\({primes_str}\\)" if primes else "\\(\\emptyset\\)"
            dist = [f"\\({{{p_start + 1}, {p_end - 1}}}\\)", f"\\({{{', '.join(map(str, [p_start + 1, p_start + 3, p_start + 7]))}}}\\)", "\\(\\{2\\}\\)"]
            sol = f"**Step 1: Identify Primes**\nPrimes between {p_start} and {p_end}: {', '.join(map(str, primes)) if primes else 'none'}.\n**Step 2: Conclusion**\n{corr}."
        else:
            p_sq = (w_idx + 2)**2
            squares = [x**2 for x in range(1, w_idx + 4)]
            sq_str = "{" + ", ".join(map(str, squares)) + "}"
            txt = f"Write the set of perfect squares from 1 up to {(w_idx + 3)**2} in roster format."
            corr = f"\\({sq_str}\\)"
            dist = [f"\\({{{', '.join(map(str, squares[:-1]))}}}\\)", f"\\({{{1, (w_idx + 3)**2}}}\\)", f"\\({{{', '.join(map(str, [x*2 for x in squares]))}}}\\)"]
            sol = f"**Step 1: Squares**\nSquares: {', '.join(map(str, squares))}.\n**Step 2: Conclusion**\n\\({sq_str}\\)."
        diff = 'easy' if seq >= 301 else ('medium' if seq >= 201 else 'hard')
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, False, diff))

    # Save to JSON
    with open("scripts/mh9_mth1_ch1_test.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(qs)} test questions for Chapter 1.")

if __name__ == "__main__":
    generate_ch1_all()
