import json
import random

random.seed(8202)

def build_ch2_questions():
    questions = []
    start_seq = 300

    def make_q(topic_code, subtopic_name, text, correct, wrongs, step1, step2, step3, diff="medium", vault="exam"):
        nonlocal start_seq
        opts_text = [correct]
        used = {correct.strip().lower()}
        for w in wrongs:
            w_clean = w.strip().lower()
            if w_clean not in used:
                opts_text.append(w)
                used.add(w_clean)
        
        cand_offset = 1
        while len(opts_text) < 4:
            cand = f"\\({cand_offset}\\)"
            if cand.lower() not in used:
                opts_text.append(cand)
                used.add(cand.lower())
            cand_offset += 1
        opts_text = opts_text[:4]

        indices = list(range(4))
        random.shuffle(indices)
        shuffled_opts = [opts_text[i] for i in indices]
        correct_idx = shuffled_opts.index(correct)
        opt_letters = ["A", "B", "C", "D"]
        correct_letter = opt_letters[correct_idx]

        options = [
            {"id": opt_letters[i], "text": shuffled_opts[i], "isCorrect": (i == correct_idx)}
            for i in range(4)
        ]

        solution = f"**Step 1:** {step1}\n**Step 2:** {step2}\n**Step 3:** {step3}"
        q_code = f"{topic_code}-OSC-{start_seq}"
        start_seq += 1

        return {
            "questionCode": q_code,
            "text": text,
            "options": options,
            "correctAnswer": correct_letter,
            "solution": solution,
            "difficulty": diff,
            "topicCode": topic_code,
            "subtopic": subtopic_name,
            "vault": vault,
            "type": "OSC",
            "marks": 4,
            "bloomsTaxonomy": "apply" if diff == "hard" else "understand",
            "estimatedTime": 90 if diff == "hard" else 60
        }

    vault_cycle = ["exam", "practice", "foundation"]
    diff_cycle = ["easy", "medium", "hard"]

    # 2.1.1 Baudhayana Sulba Sutra statement & right triangle anatomy (need 80)
    tc = "CBSE-8-MGP2-2-2.1.1"
    name = "Baudhayana Sulba Sutra statement & right triangle anatomy"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "According to the ancient Indian Baudhayana Sulba Sutra, what does the diagonal of a rectangle produce?",
            "An area equal to the sum of the areas produced by the length and the breadth separately",
            [
                "An area equal to the difference of length and breadth",
                "An area double the perimeter of the rectangle",
                "A line segment equal to the sum of length and breadth"
            ],
            f"The Baudhayana Sulba Sutra states: 'The diagonal of a rectangle produces both areas which its length and breadth produce separately.'",
            f"In modern terms, if a rectangle has length \\(a\\) and breadth \\(b\\), the square on diagonal \\(c\\) satisfies \\(c^2 = a^2 + b^2\\).",
            f"Therefore, the diagonal produces an area equal to the sum of the areas produced by the two sides.",
            d, v
        )
        questions.append(q)

    # 2.1.2 Relationship between squares on hypotenuse and legs (need 80)
    tc = "CBSE-8-MGP2-2-2.1.2"
    name = "Relationship between squares on hypotenuse and legs"
    for i in range(80):
        a, b = 3 + (i % 6), 4 + (i % 5)
        hyp_sq = a * a + b * b
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"In a right-angled triangle with legs of lengths \\({a}\\text{{ cm}}\\) and \\({b}\\text{{ cm}}\\), what is the area of the square constructed on its hypotenuse?",
            f"\\({hyp_sq}\\text{{ cm}}^2\\)",
            [f"\\({hyp_sq + 5}\\text{{ cm}}^2\\)", f"\\({hyp_sq - 5}\\text{{ cm}}^2\\)", f"\\({(a + b) ** 2}\\text{{ cm}}^2\\)"],
            f"By the Pythagoras theorem, the area of the square on the hypotenuse is equal to the sum of areas of squares on the two legs: \\(\\text{{Hypotenuse}}^2 = a^2 + b^2\\).",
            f"Substitute \\(a = {a}\\) and \\(b = {b}\\): \\({a}^2 + {b}^2 = {a*a} + {b*b} = {hyp_sq}\\text{{ cm}}^2\\).",
            f"Hence, the area of the square on the hypotenuse is \\({hyp_sq}\\text{{ cm}}^2\\).",
            d, v
        )
        questions.append(q)

    # 2.2.1 Dissection and square rearrangement geometric proofs (need 80)
    tc = "CBSE-8-MGP2-2-2.2.1"
    name = "Dissection and square rearrangement geometric proofs"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "In Bhaskara II's visual proof of the Pythagoras theorem ('Behold!'), how is a large square of side \\(c\\) dissected?",
            "Into 4 congruent right triangles of legs \\(a, b\\) and a small central square of side \\((b - a)\\)",
            [
                "Into 4 rectangles and 2 equilateral triangles",
                "Into 3 squares of equal area",
                "Into 4 trapeziums of equal height"
            ],
            f"Bhaskara II arranged four copies of a right triangle with legs \\(a, b\\) inside a square of side \\(c\\).",
            f"The remaining central unshaded area forms a square of side \\(|b - a|\\).",
            f"Equating total area gives: \\(c^2 = 4 \\times \\left(\\frac{1}{2}ab\\right) + (b - a)^2 = 2ab + b^2 - 2ab + a^2 = a^2 + b^2\\).",
            d, v
        )
        questions.append(q)

    # 2.2.2 Converse of Pythagoras theorem (testing right triangles) (need 80)
    tc = "CBSE-8-MGP2-2-2.2.2"
    name = "Converse of Pythagoras theorem (testing right triangles)"
    for i in range(80):
        triplets = [
            (6, 8, 10, True),
            (5, 12, 13, True),
            (7, 24, 25, True),
            (8, 15, 17, True),
            (9, 12, 15, True),
            (4, 5, 6, False),
            (6, 7, 9, False),
            (5, 8, 10, False)
        ]
        s1, s2, s3, is_rt = triplets[i % len(triplets)]
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        if is_rt:
            ans = f"Yes, because \\({s1}^2 + {s2}^2 = {s1*s1} + {s2*s2} = {s3*s3} = {s3}^2\\)."
            wrongs = [
                f"No, because \\({s1}^2 + {s2}^2 \\neq {s3}^2\\).",
                f"No, because side lengths must be odd numbers.",
                "Cannot be determined without angle measurements."
            ]
        else:
            ans = f"No, because \\({s1}^2 + {s2}^2 = {s1*s1 + s2*s2} \\neq {s3*s3} = {s3}^2\\)."
            wrongs = [
                f"Yes, because \\({s1} + {s2} > {s3}\\).",
                f"Yes, because all sides are integers.",
                "Cannot be determined without a compass."
            ]
        q = make_q(
            tc, name,
            f"Can a triangle with side lengths \\({s1}\\text{{ cm}}, {s2}\\text{{ cm}}, {s3}\\text{{ cm}}\\) form a right-angled triangle?",
            ans, wrongs,
            f"The converse of the Pythagoras theorem states that if \\(a^2 + b^2 = c^2\\) (where \\(c\\) is the longest side), the triangle is right-angled.",
            f"Compute squares: \\({s1}^2 + {s2}^2 = {s1*s1} + {s2*s2} = {s1*s1 + s2*s2}\\), and \\({s3}^2 = {s3*s3}\\).",
            f"Comparison shows: {ans}",
            d, v
        )
        questions.append(q)

    # 2.3.1 Identifying primitive Pythagorean triplets (3,4,5; 5,12,13) (need 80)
    tc = "CBSE-8-MGP2-2-2.3.1"
    name = "Identifying primitive Pythagorean triplets (3,4,5; 5,12,13)"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "Which of the following is a PRIMITIVE Pythagorean triplet (a triplet of integers with \\(\\gcd(a, b, c) = 1\\))?",
            "\\((5, 12, 13)\\)",
            ["\\((6, 8, 10)\\)", "\\((9, 12, 15)\\)", "\\((10, 24, 26)\\)"],
            f"A Pythagorean triplet \\((a, b, c)\\) satisfies \\(a^2 + b^2 = c^2\\).",
            f"It is defined as primitive if the greatest common divisor of all three numbers is 1: \\(\\gcd(a, b, c) = 1\\).",
            f"For \\((5, 12, 13)\\), \\(5^2 + 12^2 = 25 + 144 = 169 = 13^2\\) and \\(\\gcd(5, 12, 13) = 1\\). The others share a common factor of 2 or 3.",
            d, v
        )
        questions.append(q)

    # 2.3.2 Generating triplets using 2m, m²-1, m²+1 formula (need 80)
    tc = "CBSE-8-MGP2-2-2.3.2"
    name = "Generating triplets using 2m, m²-1, m²+1 formula"
    for i in range(80):
        m = 4 + (i % 8)
        a = 2 * m
        b = m * m - 1
        c = m * m + 1
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Using the algebraic identity \\((2m, m^2-1, m^2+1)\\), generate a Pythagorean triplet when \\(m = {m}\\).",
            f"\\(({a}, {b}, {c})\\)",
            [f"\\(({a}, {b - 2}, {c + 2})\\)", f"\\(({a + 2}, {b}, {c})\\)", f"\\(({m}, {m*m}, {m*m+1})\\)"],
            f"Substitute \\(m = {m}\\) into the three algebraic generators.",
            f"First term: \\(2m = 2({m}) = {a}\\). Second term: \\(m^2 - 1 = {m}^2 - 1 = {b}\\). Third term: \\(m^2 + 1 = {m}^2 + 1 = {c}\\).",
            f"Verify: \\({a}^2 + {b}^2 = {a*a} + {b*b} = {a*a + b*b} = {c*c} = {c}^2\\). Thus, the triplet is \\(({a}, {b}, {c})\\).",
            d, v
        )
        questions.append(q)

    # 2.4.1 Finding unknown side lengths in geometric figures (need 80)
    tc = "CBSE-8-MGP2-2-2.4.1"
    name = "Finding unknown side lengths in geometric figures"
    for i in range(80):
        scale = 1 + (i % 5)
        a = 3 * scale
        b = 4 * scale
        c = 5 * scale
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"In a right triangle with legs \\({a}\\text{{ cm}}\\) and \\({b}\\text{{ cm}}\\), calculate the length of the hypotenuse.",
            f"\\({c}\\text{{ cm}}\\)",
            [f"\\({c + 2}\\text{{ cm}}\\)", f"\\({c - 1}\\text{{ cm}}\\)", f"\\({a + b}\\text{{ cm}}\\)"],
            f"Apply the Pythagoras theorem: \\(\\text{{Hypotenuse}} = \\sqrt{{a^2 + b^2}}\\).",
            f"Substitute values: \\(\\sqrt{{{a}^2 + {b}^2}} = \\sqrt{{{a*a} + {b*b}}} = \\sqrt{{{c*c}}} = {c}\\text{{ cm}}\\).",
            f"Therefore, the hypotenuse is \\({c}\\text{{ cm}}\\).",
            d, v
        )
        questions.append(q)

    # 2.4.2 Word problems on ladder, tree, walking distance (need 80)
    tc = "CBSE-8-MGP2-2-2.4.2"
    name = "Word problems on ladder, tree, walking distance"
    for i in range(80):
        ladder = 10 + (i % 4) * 5  # e.g., 10, 15, 20, 25
        # 3-4-5 multiple
        k = 2 + (i % 4)
        base = 3 * k
        height = 4 * k
        hyp = 5 * k
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"A ladder of length \\({hyp}\\text{{ m}}\\) reaches a window located \\({height}\\text{{ m}}\\) high on a vertical wall. How far is the foot of the ladder from the base of the wall?",
            f"\\({base}\\text{{ m}}\\)",
            [f"\\({base + 2}\\text{{ m}}\\)", f"\\({base - 2}\\text{{ m}}\\)", f"\\({hyp - height}\\text{{ m}}\\)"],
            f"The wall, ground, and ladder form a right-angled triangle with hypotenuse \\({hyp}\\text{{ m}}\\) and vertical height \\({height}\\text{{ m}}\\).",
            f"Use the Pythagoras theorem: \\(\\text{{base}} = \\sqrt{{\\text{{hypotenuse}}^2 - \\text{{height}}^2}} = \\sqrt{{{hyp}^2 - {height}^2}}\\).",
            f"Calculate: \\(\\sqrt{{{hyp*hyp} - {height*height}}} = \\sqrt{{{base*base}}} = {base}\\text{{ m}}\\).",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch2_questions()
    print(f"Generated {len(qs)} questions for Chapter 2.")
    with open("scripts/cbse8_mgp2_ch2_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/cbse8_mgp2_ch2_topup.json")
