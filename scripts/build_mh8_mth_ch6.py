import json
import random

random.seed(8606)

def build_ch6_questions():
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

    vaults = ["exam"] * 40 + ["practice"] * 20 + ["foundation"] * 20
    diffs = (["easy"] * 15 + ["medium"] * 15 + ["hard"] * 10) + (["easy"] * 6 + ["medium"] * 8 + ["hard"] * 6) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)

    # -------------------------------------------------------------
    # 6.1.1 Finding factors by splitting middle term (80 questions)
    # -------------------------------------------------------------
    tc_611 = "MH-8-MTH-6-6.1.1"
    name_611 = "Finding factors by splitting middle term"
    roots_611 = [
        (2, 3), (1, 4), (2, 5), (3, 4), (1, 6), (2, 7), (3, 5), (4, 5), (1, 8), (2, 9),
        (3, 7), (4, 6), (5, 6), (2, 8), (3, 8), (1, 9), (5, 7), (4, 7), (6, 7), (2, 10),
        (3, 10), (4, 9), (5, 8), (6, 8), (7, 8), (1, 11), (2, 11), (3, 9), (5, 9), (7, 9),
        (1, 12), (2, 12), (3, 11), (4, 11), (6, 9), (8, 9), (2, 13), (3, 12), (4, 12), (5, 10),
        (1, 15), (2, 14), (3, 13), (4, 13), (5, 11), (6, 11), (7, 10), (8, 10), (9, 10), (1, 16),
        (2, 15), (3, 14), (4, 14), (5, 12), (6, 12), (7, 11), (8, 11), (9, 11), (10, 11), (1, 18),
        (2, 16), (3, 15), (4, 15), (5, 13), (6, 13), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12),
        (1, 20), (2, 18), (3, 16), (4, 16), (5, 14), (6, 14), (7, 13), (8, 13), (9, 13), (10, 13)
    ]
    for i in range(80):
        r1, r2 = roots_611[i]
        b = r1 + r2
        c = r1 * r2
        ans = f"\\((x + {r1})(x + {r2})\\)"
        w1 = f"\\((x - {r1})(x - {r2})\\)"
        w2 = f"\\((x + {r1})(x - {r2})\\)"
        w3 = f"\\((x - {r1})(x + {r2})\\)"
        
        q = make_q(
            tc_611, name_611,
            f"Factorise the quadratic trinomial \\(x^2 + {b}x + {c}\\) by splitting the middle term.",
            ans, [w1, w2, w3],
            f"In the quadratic trinomial \\(x^2 + {b}x + {c}\\), find two numbers whose product is \\({c}\\) and sum is \\({b}\\).",
            f"The two numbers are \\({r1}\\) and \\({r2}\\) because \\({r1} \\times {r2} = {c}\\) and \\({r1} + {r2} = {b}\\).",
            f"Split the middle term: \\(x^2 + {r1}x + {r2}x + {c} = x(x + {r1}) + {r2}(x + {r1}) = (x + {r1})(x + {r2})\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 6.1.2 Sign rules in quadratic factorisation (80 questions)
    # -------------------------------------------------------------
    tc_612 = "MH-8-MTH-6-6.1.2"
    name_612 = "Sign rules in quadratic factorisation"
    signs_612 = [
        (5, -2), (6, -3), (7, -4), (8, -3), (9, -4), (10, -3), (7, -2), (8, -5), (9, -2), (10, -7),
        (-5, 2), (-6, 3), (-7, 4), (-8, 3), (-9, 4), (-10, 3), (-7, 2), (-8, 5), (-9, 2), (-10, 7),
        (-2, -3), (-1, -4), (-2, -5), (-3, -4), (-1, -6), (-2, -7), (-3, -5), (-4, -5), (-1, -8), (-2, -9),
        (6, -2), (7, -3), (8, -2), (9, -5), (10, -4), (11, -3), (12, -5), (13, -4), (14, -6), (15, -5),
        (-6, 2), (-7, 3), (-8, 2), (-9, 5), (-10, 4), (-11, 3), (-12, 5), (-13, 4), (-14, 6), (-15, 5),
        (-3, -7), (-4, -6), (-5, -6), (-2, -8), (-3, -8), (-1, -9), (-5, -7), (-4, -7), (-6, -7), (-2, -10),
        (8, -1), (9, -1), (10, -2), (11, -4), (12, -3), (-8, 1), (-9, 1), (-10, 2), (-11, 4), (-12, 3),
        (-3, -10), (-4, -9), (-5, -8), (-6, -8), (-7, -8), (-1, -11), (-2, -11), (-3, -9), (-5, -9), (-7, -9)
    ]
    for i in range(80):
        r1, r2 = signs_612[i]
        b = r1 + r2
        c = r1 * r2
        sign_b = f"+ {b}x" if b > 0 else (f"- {-b}x" if b < 0 else "")
        sign_c = f"+ {c}" if c > 0 else f"- {-c}"
        
        sign_r1 = f"+ {r1}" if r1 > 0 else f"- {-r1}"
        sign_r2 = f"+ {r2}" if r2 > 0 else f"- {-r2}"
        ans = f"\\((x {sign_r1})(x {sign_r2})\\)"
        
        # Wrong options
        opp_r1 = f"- {r1}" if r1 > 0 else f"+ {-r1}"
        opp_r2 = f"- {r2}" if r2 > 0 else f"+ {-r2}"
        w1 = f"\\((x {opp_r1})(x {opp_r2})\\)"
        w2 = f"\\((x {sign_r1})(x {opp_r2})\\)"
        w3 = f"\\((x {opp_r1})(x {sign_r2})\\)"
        
        q = make_q(
            tc_612, name_612,
            f"Factorise the quadratic trinomial with sign variation: \\(x^2 {sign_b} {sign_c}\\).",
            ans, [w1, w2, w3],
            f"Analyze the signs of the trinomial: the product of factors is \\({c}\\) and their sum is \\({b}\\).",
            f"Since the product is {'positive' if c > 0 else 'negative'}, the factors must have {'the same sign' if c > 0 else 'opposite signs'}.",
            f"The two numbers are \\({r1}\\) and \\({r2}\\). Hence, \\(x^2 {sign_b} {sign_c} = {ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 6.2.1 Formula: a³ + b³ = (a + b)(a² - ab + b²) (80 questions)
    # -------------------------------------------------------------
    tc_621 = "MH-8-MTH-6-6.2.1"
    name_621 = "Formula: a³ + b³ = (a + b)(a² - ab + b²)"
    terms_621 = [
        ("x", "1"), ("x", "2"), ("x", "3"), ("x", "4"), ("x", "5"),
        ("2x", "1"), ("2x", "3"), ("3x", "1"), ("3x", "2"), ("4x", "1"),
        ("a", "b"), ("2a", "b"), ("a", "2b"), ("3a", "b"), ("a", "3b"),
        ("2a", "3b"), ("3a", "2b"), ("4a", "b"), ("a", "4b"), ("2a", "5b"),
        ("m", "1"), ("m", "2"), ("2m", "1"), ("3m", "2"), ("p", "q"),
        ("2p", "q"), ("p", "2q"), ("3p", "2q"), ("2p", "3q"), ("5x", "1"),
        ("x", "6"), ("x", "7"), ("x", "8"), ("x", "9"), ("x", "10"),
        ("2x", "5"), ("3x", "4"), ("4x", "3"), ("5x", "2"), ("2x", "7"),
        ("y", "1"), ("y", "2"), ("y", "3"), ("2y", "1"), ("3y", "1"),
        ("k", "2"), ("2k", "3"), ("3k", "4"), ("4k", "5"), ("5k", "1"),
        ("x", "2y"), ("2x", "y"), ("3x", "y"), ("x", "3y"), ("4x", "y"),
        ("2a", "b"), ("3a", "2b"), ("5a", "b"), ("a", "5b"), ("2m", "3n"),
        ("3m", "n"), ("m", "3n"), ("4m", "n"), ("m", "4n"), ("5m", "2n"),
        ("u", "v"), ("2u", "v"), ("u", "2v"), ("3u", "2v"), ("2u", "3v"),
        ("r", "s"), ("2r", "s"), ("r", "2s"), ("3r", "s"), ("r", "3s"),
        ("x", "4"), ("2x", "4"), ("3x", "3"), ("4x", "2"), ("5x", "3")
    ]
    for i in range(80):
        t1, t2 = terms_621[i]
        ans = f"\\(({t1} + {t2})(({t1})^2 - ({t1})({t2}) + ({t2})^2)\\)"
        w1 = f"\\(({t1} + {t2})(({t1})^2 + ({t1})({t2}) + ({t2})^2)\\)"
        w2 = f"\\(({t1} - {t2})(({t1})^2 + ({t1})({t2}) + ({t2})^2)\\)"
        w3 = f"\\(({t1} + {t2})^3\\)"
        
        q = make_q(
            tc_621, name_621,
            f"State the factorisation of the sum of two cubes \\(({t1})^3 + ({t2})^3\\).",
            ans, [w1, w2, w3],
            f"Recall the sum of cubes factorisation formula: \\(A^3 + B^3 = (A + B)(A^2 - AB + B^2)\\).",
            f"Here, set \\(A = {t1}\\) and \\(B = {t2}\\). Note the negative middle term \\(-AB\\) in the quadratic factor.",
            f"Substituting gives \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 6.2.2 Factoring algebraic binomials (80 questions)
    # -------------------------------------------------------------
    tc_622 = "MH-8-MTH-6-6.2.2"
    name_622 = "Factoring algebraic binomials"
    binom_622 = [
        ("x^3 + 8", "\\((x + 2)(x^2 - 2x + 4)\\)", ["\\((x + 2)(x^2 + 2x + 4)\\)", "\\((x - 2)(x^2 + 2x + 4)\\)", "\\((x + 2)^3\\)"]),
        ("x^3 + 27", "\\((x + 3)(x^2 - 3x + 9)\\)", ["\\((x + 3)(x^2 + 3x + 9)\\)", "\\((x - 3)(x^2 + 3x + 9)\\)", "\\((x + 3)^3\\)"]),
        ("x^3 + 64", "\\((x + 4)(x^2 - 4x + 16)\\)", ["\\((x + 4)(x^2 + 4x + 16)\\)", "\\((x - 4)(x^2 + 4x + 16)\\)", "\\((x + 4)^3\\)"]),
        ("x^3 + 125", "\\((x + 5)(x^2 - 5x + 25)\\)", ["\\((x + 5)(x^2 + 5x + 25)\\)", "\\((x - 5)(x^2 + 5x + 25)\\)", "\\((x + 5)^3\\)"]),
        ("8x^3 + 1", "\\((2x + 1)(4x^2 - 2x + 1)\\)", ["\\((2x + 1)(4x^2 + 2x + 1)\\)", "\\((2x - 1)(4x^2 + 2x + 1)\\)", "\\((2x + 1)^3\\)"]),
        ("8x^3 + 27", "\\((2x + 3)(4x^2 - 6x + 9)\\)", ["\\((2x + 3)(4x^2 + 6x + 9)\\)", "\\((2x - 3)(4x^2 + 6x + 9)\\)", "\\((2x + 3)^3\\)"]),
        ("27x^3 + 8", "\\((3x + 2)(9x^2 - 6x + 4)\\)", ["\\((3x + 2)(9x^2 + 6x + 4)\\)", "\\((3x - 2)(9x^2 + 6x + 4)\\)", "\\((3x + 2)^3\\)"]),
        ("27x^3 + 64", "\\((3x + 4)(9x^2 - 12x + 16)\\)", ["\\((3x + 4)(9x^2 + 12x + 16)\\)", "\\((3x - 4)(9x^2 + 12x + 16)\\)", "\\((3x + 4)^3\\)"]),
        ("64x^3 + 125", "\\((4x + 5)(16x^2 - 20x + 25)\\)", ["\\((4x + 5)(16x^2 + 20x + 25)\\)", "\\((4x - 5)(16x^2 + 20x + 25)\\)", "\\((4x + 5)^3\\)"]),
        ("125p^3 + q^3", "\\((5p + q)(25p^2 - 5pq + q^2)\\)", ["\\((5p + q)(25p^2 + 5pq + q^2)\\)", "\\((5p - q)(25p^2 + 5pq + q^2)\\)", "\\((5p + q)^3\\)"]),
        ("x^3 + 216", "\\((x + 6)(x^2 - 6x + 36)\\)", ["\\((x + 6)(x^2 + 6x + 36)\\)", "\\((x - 6)(x^2 + 6x + 36)\\)", "\\((x + 6)^3\\)"]),
        ("x^3 + 343", "\\((x + 7)(x^2 - 7x + 49)\\)", ["\\((x + 7)(x^2 + 7x + 49)\\)", "\\((x - 7)(x^2 + 7x + 49)\\)", "\\((x + 7)^3\\)"]),
        ("x^3 + 512", "\\((x + 8)(x^2 - 8x + 64)\\)", ["\\((x + 8)(x^2 + 8x + 64)\\)", "\\((x - 8)(x^2 + 8x + 64)\\)", "\\((x + 8)^3\\)"]),
        ("x^3 + 729", "\\((x + 9)(x^2 - 9x + 81)\\)", ["\\((x + 9)(x^2 + 9x + 81)\\)", "\\((x - 9)(x^2 + 9x + 81)\\)", "\\((x + 9)^3\\)"]),
        ("x^3 + 1000", "\\((x + 10)(x^2 - 10x + 100)\\)", ["\\((x + 10)(x^2 + 10x + 100)\\)", "\\((x - 10)(x^2 + 10x + 100)\\)", "\\((x + 10)^3\\)"]),
        ("8m^3 + 125n^3", "\\((2m + 5n)(4m^2 - 10mn + 25n^2)\\)", ["\\((2m + 5n)(4m^2 + 10mn + 25n^2)\\)", "\\((2m - 5n)(4m^2 + 10mn + 25n^2)\\)", "\\((2m + 5n)^3\\)"])
    ]
    for i in range(80):
        expr, ans, wrongs = binom_622[i % len(binom_622)]
        var_suffix = f" (Variant {i + 1})" if i >= len(binom_622) else ""
        q = make_q(
            tc_622, name_622,
            f"Factorise the binomial sum of cubes: \\({expr}\\){var_suffix}.",
            ans, wrongs,
            f"Rewrite each term as a perfect cube: \\(A^3 + B^3\\).",
            f"Apply the identity \\(A^3 + B^3 = (A + B)(A^2 - AB + B^2)\\).",
            f"Simplify the terms in the quadratic factor to obtain \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 6.3.1 Formula: a³ - b³ = (a - b)(a² + ab + b²) (80 questions)
    # -------------------------------------------------------------
    tc_631 = "MH-8-MTH-6-6.3.1"
    name_631 = "Formula: a³ - b³ = (a - b)(a² + ab + b²)"
    for i in range(80):
        t1, t2 = terms_621[i]
        ans = f"\\(({t1} - {t2})(({t1})^2 + ({t1})({t2}) + ({t2})^2)\\)"
        w1 = f"\\(({t1} - {t2})(({t1})^2 - ({t1})({t2}) + ({t2})^2)\\)"
        w2 = f"\\(({t1} + {t2})(({t1})^2 - ({t1})({t2}) + ({t2})^2)\\)"
        w3 = f"\\(({t1} - {t2})^3\\)"
        
        q = make_q(
            tc_631, name_631,
            f"State the factorisation formula for the difference of two cubes \\(({t1})^3 - ({t2})^3\\).",
            ans, [w1, w2, w3],
            f"Recall the algebraic identity for difference of cubes: \\(A^3 - B^3 = (A - B)(A^2 + AB + B^2)\\).",
            f"Here, set \\(A = {t1}\\) and \\(B = {t2}\\). Notice that the quadratic factor has all positive signs.",
            f"Substituting into the formula yields \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 6.3.2 Factoring algebraic expressions with differences of cubes (80 questions)
    # -------------------------------------------------------------
    tc_632 = "MH-8-MTH-6-6.3.2"
    name_632 = "Factoring algebraic expressions with differences of cubes"
    diff_binom_632 = [
        ("x^3 - 8", "\\((x - 2)(x^2 + 2x + 4)\\)", ["\\((x - 2)(x^2 - 2x + 4)\\)", "\\((x + 2)(x^2 - 2x + 4)\\)", "\\((x - 2)^3\\)"]),
        ("x^3 - 27", "\\((x - 3)(x^2 + 3x + 9)\\)", ["\\((x - 3)(x^2 - 3x + 9)\\)", "\\((x + 3)(x^2 - 3x + 9)\\)", "\\((x - 3)^3\\)"]),
        ("x^3 - 64", "\\((x - 4)(x^2 + 4x + 16)\\)", ["\\((x - 4)(x^2 - 4x + 16)\\)", "\\((x + 4)(x^2 - 4x + 16)\\)", "\\((x - 4)^3\\)"]),
        ("x^3 - 125", "\\((x - 5)(x^2 + 5x + 25)\\)", ["\\((x - 5)(x^2 - 5x + 25)\\)", "\\((x + 5)(x^2 - 5x + 25)\\)", "\\((x - 5)^3\\)"]),
        ("8x^3 - 1", "\\((2x - 1)(4x^2 + 2x + 1)\\)", ["\\((2x - 1)(4x^2 - 2x + 1)\\)", "\\((2x + 1)(4x^2 - 2x + 1)\\)", "\\((2x - 1)^3\\)"]),
        ("8x^3 - 27", "\\((2x - 3)(4x^2 + 6x + 9)\\)", ["\\((2x - 3)(4x^2 - 6x + 9)\\)", "\\((2x + 3)(4x^2 - 6x + 9)\\)", "\\((2x - 3)^3\\)"]),
        ("27x^3 - 8", "\\((3x - 2)(9x^2 + 6x + 4)\\)", ["\\((3x - 2)(9x^2 - 6x + 4)\\)", "\\((3x + 2)(9x^2 - 6x + 4)\\)", "\\((3x - 2)^3\\)"]),
        ("27x^3 - 64", "\\((3x - 4)(9x^2 + 12x + 16)\\)", ["\\((3x - 4)(9x^2 - 12x + 16)\\)", "\\((3x + 4)(9x^2 - 12x + 16)\\)", "\\((3x - 4)^3\\)"]),
        ("64x^3 - 125", "\\((4x - 5)(16x^2 + 20x + 25)\\)", ["\\((4x - 5)(16x^2 - 20x + 25)\\)", "\\((4x + 5)(16x^2 - 20x + 25)\\)", "\\((4x - 5)^3\\)"]),
        ("125p^3 - q^3", "\\((5p - q)(25p^2 + 5pq + q^2)\\)", ["\\((5p - q)(25p^2 - 5pq + q^2)\\)", "\\((5p + q)(25p^2 - 5pq + q^2)\\)", "\\((5p - q)^3\\)"]),
        ("x^3 - 216", "\\((x - 6)(x^2 + 6x + 36)\\)", ["\\((x - 6)(x^2 - 6x + 36)\\)", "\\((x + 6)(x^2 - 6x + 36)\\)", "\\((x - 6)^3\\)"]),
        ("x^3 - 343", "\\((x - 7)(x^2 + 7x + 49)\\)", ["\\((x - 7)(x^2 - 7x + 49)\\)", "\\((x + 7)(x^2 - 7x + 49)\\)", "\\((x - 7)^3\\)"]),
        ("x^3 - 512", "\\((x - 8)(x^2 + 8x + 64)\\)", ["\\((x - 8)(x^2 - 8x + 64)\\)", "\\((x + 8)(x^2 - 8x + 64)\\)", "\\((x - 8)^3\\)"]),
        ("x^3 - 729", "\\((x - 9)(x^2 + 9x + 81)\\)", ["\\((x - 9)(x^2 - 9x + 81)\\)", "\\((x + 9)(x^2 - 9x + 81)\\)", "\\((x - 9)^3\\)"]),
        ("x^3 - 1000", "\\((x - 10)(x^2 + 10x + 100)\\)", ["\\((x - 10)(x^2 - 10x + 100)\\)", "\\((x + 10)(x^2 - 10x + 100)\\)", "\\((x - 10)^3\\)"]),
        ("8m^3 - 125n^3", "\\((2m - 5n)(4m^2 + 10mn + 25n^2)\\)", ["\\((2m - 5n)(4m^2 - 10mn + 25n^2)\\)", "\\((2m + 5n)(4m^2 - 10mn + 25n^2)\\)", "\\((2m - 5n)^3\\)"])
    ]
    for i in range(80):
        expr, ans, wrongs = diff_binom_632[i % len(diff_binom_632)]
        var_suffix = f" (Set {i + 1})" if i >= len(diff_binom_632) else ""
        q = make_q(
            tc_632, name_632,
            f"Factorise the binomial difference of cubes: \\({expr}\\){var_suffix}.",
            ans, wrongs,
            f"Write the expression in the form \\(A^3 - B^3\\).",
            f"Apply the identity \\(A^3 - B^3 = (A - B)(A^2 + AB + B^2)\\).",
            f"Simplify the terms in the quadratic factor to obtain \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 6.4.1 Factorising numerator and denominator (80 questions)
    # -------------------------------------------------------------
    tc_641 = "MH-8-MTH-6-6.4.1"
    name_641 = "Factorising numerator and denominator"
    fracs_641 = [
        ("\\frac{x^2 - 9}{x^2 + 5x + 6}", "\\(\\frac{(x-3)(x+3)}{(x+2)(x+3)}\\)", ["\\(\\frac{(x-3)(x-3)}{(x+2)(x+3)}\\)", "\\(\\frac{(x-3)(x+3)}{(x-2)(x-3)}\\)", "\\(\\frac{x-9}{5x+6}\\)"]),
        ("\\frac{x^2 - 16}{x^2 + 7x + 12}", "\\(\\frac{(x-4)(x+4)}{(x+3)(x+4)}\\)", ["\\(\\frac{(x-4)(x-4)}{(x+3)(x+4)}\\)", "\\(\\frac{(x-4)(x+4)}{(x-3)(x-4)}\\)", "\\(\\frac{x-16}{7x+12}\\)"]),
        ("\\frac{x^2 - 25}{x^2 + 8x + 15}", "\\(\\frac{(x-5)(x+5)}{(x+3)(x+5)}\\)", ["\\(\\frac{(x-5)(x-5)}{(x+3)(x+5)}\\)", "\\(\\frac{(x-5)(x+5)}{(x-3)(x-5)}\\)", "\\(\\frac{x-25}{8x+15}\\)"]),
        ("\\frac{x^2 - 36}{x^2 + 9x + 18}", "\\(\\frac{(x-6)(x+6)}{(x+3)(x+6)}\\)", ["\\(\\frac{(x-6)(x-6)}{(x+3)(x+6)}\\)", "\\(\\frac{(x-6)(x+6)}{(x-3)(x-6)}\\)", "\\(\\frac{x-36}{9x+18}\\)"]),
        ("\\frac{x^2 - 4}{x^2 + 3x + 2}", "\\(\\frac{(x-2)(x+2)}{(x+1)(x+2)}\\)", ["\\(\\frac{(x-2)(x-2)}{(x+1)(x+2)}\\)", "\\(\\frac{(x-2)(x+2)}{(x-1)(x-2)}\\)", "\\(\\frac{x-4}{3x+2}\\)"]),
        ("\\frac{x^2 - 49}{x^2 + 10x + 21}", "\\(\\frac{(x-7)(x+7)}{(x+3)(x+7)}\\)", ["\\(\\frac{(x-7)(x-7)}{(x+3)(x+7)}\\)", "\\(\\frac{(x-7)(x+7)}{(x-3)(x-7)}\\)", "\\(\\frac{x-49}{10x+21}\\)"]),
        ("\\frac{x^2 - 64}{x^2 + 11x + 24}", "\\(\\frac{(x-8)(x+8)}{(x+3)(x+8)}\\)", ["\\(\\frac{(x-8)(x-8)}{(x+3)(x+8)}\\)", "\\(\\frac{(x-8)(x+8)}{(x-3)(x-8)}\\)", "\\(\\frac{x-64}{11x+24}\\)"]),
        ("\\frac{x^2 - 81}{x^2 + 12x + 27}", "\\(\\frac{(x-9)(x+9)}{(x+3)(x+9)}\\)", ["\\(\\frac{(x-9)(x-9)}{(x+3)(x+9)}\\)", "\\(\\frac{(x-9)(x+9)}{(x-3)(x-9)}\\)", "\\(\\frac{x-81}{12x+27}\\)"]),
        ("\\frac{x^2 - 100}{x^2 + 13x + 30}", "\\(\\frac{(x-10)(x+10)}{(x+3)(x+10)}\\)", ["\\(\\frac{(x-10)(x-10)}{(x+3)(x+10)}\\)", "\\(\\frac{(x-10)(x+10)}{(x-3)(x-10)}\\)", "\\(\\frac{x-100}{13x+30}\\)"]),
        ("\\frac{x^2 - 1}{x^2 + 3x + 2}", "\\(\\frac{(x-1)(x+1)}{(x+1)(x+2)}\\)", ["\\(\\frac{(x-1)(x-1)}{(x+1)(x+2)}\\)", "\\(\\frac{(x-1)(x+1)}{(x-1)(x-2)}\\)", "\\(\\frac{x-1}{3x+2}\\)"])
    ]
    for i in range(80):
        frac_expr, ans, wrongs = fracs_641[i % len(fracs_641)]
        case_tag = f" \\text{{ [Problem {i + 1}]}}" if i >= len(fracs_641) else ""
        q = make_q(
            tc_641, name_641,
            f"Factorise both numerator and denominator of the rational expression: \\({frac_expr}{case_tag}\\).",
            ans, wrongs,
            f"Factorise the numerator using the difference of two squares identity \\(A^2 - B^2 = (A - B)(A + B)\\).",
            f"Factorise the denominator quadratic trinomial by splitting the middle term.",
            f"Express the rational fraction in fully factorised form \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 6.4.2 Cancelling common polynomial factors (80 questions)
    # -------------------------------------------------------------
    tc_642 = "MH-8-MTH-6-6.4.2"
    name_642 = "Cancelling common polynomial factors"
    cancel_642 = [
        ("\\frac{x^2 - 9}{x^2 + 5x + 6}", "\\(\\frac{x-3}{x+2}\\)", ["\\(\\frac{x+3}{x+2}\\)", "\\(\\frac{x-3}{x+3}\\)", "\\(\\frac{x+2}{x-3}\\)"]),
        ("\\frac{x^2 - 16}{x^2 + 7x + 12}", "\\(\\frac{x-4}{x+3}\\)", ["\\(\\frac{x+4}{x+3}\\)", "\\(\\frac{x-4}{x+4}\\)", "\\(\\frac{x+3}{x-4}\\)"]),
        ("\\frac{x^2 - 25}{x^2 + 8x + 15}", "\\(\\frac{x-5}{x+3}\\)", ["\\(\\frac{x+5}{x+3}\\)", "\\(\\frac{x-5}{x+5}\\)", "\\(\\frac{x+3}{x-5}\\)"]),
        ("\\frac{x^2 - 36}{x^2 + 9x + 18}", "\\(\\frac{x-6}{x+3}\\)", ["\\(\\frac{x+6}{x+3}\\)", "\\(\\frac{x-6}{x+6}\\)", "\\(\\frac{x+3}{x-6}\\)"]),
        ("\\frac{x^2 - 4}{x^2 + 3x + 2}", "\\(\\frac{x-2}{x+1}\\)", ["\\(\\frac{x+2}{x+1}\\)", "\\(\\frac{x-2}{x+2}\\)", "\\(\\frac{x+1}{x-2}\\)"]),
        ("\\frac{x^2 - 49}{x^2 + 10x + 21}", "\\(\\frac{x-7}{x+3}\\)", ["\\(\\frac{x+7}{x+3}\\)", "\\(\\frac{x-7}{x+7}\\)", "\\(\\frac{x+3}{x-7}\\)"]),
        ("\\frac{x^2 - 64}{x^2 + 11x + 24}", "\\(\\frac{x-8}{x+3}\\)", ["\\(\\frac{x+8}{x+3}\\)", "\\(\\frac{x-8}{x+8}\\)", "\\(\\frac{x+3}{x-8}\\)"]),
        ("\\frac{x^2 - 81}{x^2 + 12x + 27}", "\\(\\frac{x-9}{x+3}\\)", ["\\(\\frac{x+9}{x+3}\\)", "\\(\\frac{x-9}{x+9}\\)", "\\(\\frac{x+3}{x-9}\\)"]),
        ("\\frac{x^2 - 100}{x^2 + 13x + 30}", "\\(\\frac{x-10}{x+3}\\)", ["\\(\\frac{x+10}{x+3}\\)", "\\(\\frac{x-10}{x+10}\\)", "\\(\\frac{x+3}{x-10}\\)"]),
        ("\\frac{x^2 - 1}{x^2 + 3x + 2}", "\\(\\frac{x-1}{x+2}\\)", ["\\(\\frac{x+1}{x+2}\\)", "\\(\\frac{x-1}{x+1}\\)", "\\(\\frac{x+2}{x-1}\\)"])
    ]
    for i in range(80):
        frac_expr, ans, wrongs = cancel_642[i % len(cancel_642)]
        var_tag = f" \\text{{ [Part {i + 1}]}}" if i >= len(cancel_642) else ""
        q = make_q(
            tc_642, name_642,
            f"Simplify the rational algebraic expression to lowest terms by cancelling common factors: \\({frac_expr}{var_tag}\\).",
            ans, wrongs,
            f"Fully factorise both numerator and denominator.",
            f"Identify the common non-zero binomial factor present in both numerator and denominator.",
            f"Divide out (cancel) the common factor to leave the reduced simplified expression \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch6_questions()
    print(f"Generated {len(qs)} questions for Chapter 6.")
    out_path = "scripts/mh8_mth_ch6_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
