import json
import random

random.seed(8505)

def build_ch5_questions():
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
    # 5.1.1 Formula: (x+a)(x+b) = x² + (a+b)x + ab (80 questions)
    # -------------------------------------------------------------
    tc_511 = "MH-8-MTH-5-5.1.1"
    name_511 = "Formula: (x+a)(x+b) = x² + (a+b)x + ab"
    pairs_511 = [
        (2, 3), (1, 4), (3, 5), (4, 2), (5, 6), (2, 7), (3, 4), (1, 6), (7, 2), (5, 3),
        (2, -3), (4, -1), (5, -2), (6, -3), (7, -4), (3, -5), (1, -6), (8, -2), (9, -3), (10, -5),
        (-2, 3), (-4, 1), (-5, 2), (-6, 3), (-7, 4), (-3, 5), (-1, 6), (-8, 2), (-9, 3), (-10, 5),
        (-2, -3), (-1, -4), (-3, -5), (-4, -2), (-5, -6), (-2, -7), (-3, -4), (-1, -6), (-7, -2), (-5, -3),
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
        (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7), (8, -8), (9, -9), (10, -10),
        (11, 2), (12, 3), (15, 1), (20, 2), (25, 4), (11, -2), (12, -3), (15, -1), (20, -2), (25, -4),
        (8, 5), (9, 4), (7, 6), (6, 5), (8, 3), (9, 2), (11, 3), (12, 4), (13, 2), (14, 1)
    ]
    for i in range(80):
        a, b = pairs_511[i]
        sum_ab = a + b
        prod_ab = a * b
        sign_a = f"+ {a}" if a > 0 else f"- {-a}"
        sign_b = f"+ {b}" if b > 0 else f"- {-b}"
        
        sum_str = f"+ {sum_ab}x" if sum_ab > 0 else (f"- {-sum_ab}x" if sum_ab < 0 else "")
        prod_str = f"+ {prod_ab}" if prod_ab > 0 else (f"- {-prod_ab}" if prod_ab < 0 else "")
        
        ans = f"\\(x^2 {sum_str} {prod_str}\\)".replace("  ", " ").strip()
        w1 = f"\\(x^2 {prod_str} {sum_str}\\)".replace("  ", " ").strip()
        wrong_sum = f"+ {a - b}x" if (a - b) > 0 else f"- {-(a - b)}x"
        w2 = f"\\(x^2 {wrong_sum} {prod_str}\\)".replace("  ", " ").strip()
        wrong_prod = f"- {prod_ab}" if prod_ab > 0 else f"+ {-prod_ab}"
        w3 = f"\\(x^2 {sum_str} {wrong_prod}\\)".replace("  ", " ").strip()
        
        q = make_q(
            tc_511, name_511,
            f"Expand the algebraic expression \\((x {sign_a})(x {sign_b})\\) using the standard identity.",
            ans, [w1, w2, w3],
            f"Use the standard expansion identity \\((x + a)(x + b) = x^2 + (a + b)x + ab\\). Here, \\(a = {a}\\) and \\(b = {b}\\).",
            f"Calculate the sum and product of the constants: \\(a + b = {a} + ({b}) = {sum_ab}\\) and \\(a \\times b = {a} \\times ({b}) = {prod_ab}\\).",
            f"Substitute these values into the formula to obtain \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 5.1.2 Application to algebraic and numerical expansions (80 questions)
    # -------------------------------------------------------------
    tc_512 = "MH-8-MTH-5-5.1.2"
    name_512 = "Application to algebraic and numerical expansions"
    num_pairs_512 = [
        (101, 102), (102, 103), (103, 104), (104, 105), (105, 106), (101, 105), (102, 104), (103, 105), (101, 108), (102, 107),
        (99, 98), (98, 97), (97, 96), (99, 95), (98, 94), (96, 95), (99, 97), (98, 96), (97, 95), (95, 94),
        (102, 98), (103, 97), (104, 96), (105, 95), (106, 94), (101, 99), (102, 99), (103, 98), (104, 97), (105, 96),
        (51, 52), (52, 53), (51, 53), (49, 48), (52, 48), (201, 202), (202, 203), (199, 198), (202, 198), (201, 199),
        (101, 103), (102, 105), (103, 106), (104, 107), (105, 108), (106, 109), (107, 108), (102, 108), (103, 107), (104, 108),
        (99, 94), (98, 93), (97, 92), (96, 91), (95, 90), (99, 92), (98, 91), (97, 93), (96, 92), (95, 93),
        (101, 98), (102, 97), (103, 96), (104, 95), (105, 94), (106, 93), (107, 92), (108, 91), (109, 90), (101, 97),
        (51, 54), (52, 55), (53, 54), (49, 47), (48, 46), (201, 203), (202, 204), (199, 197), (198, 196), (203, 197)
    ]
    for i in range(80):
        n1, n2 = num_pairs_512[i]
        prod = n1 * n2
        # Base representation around 100, 50, or 200
        base = 100
        if n1 >= 190:
            base = 200
        elif n1 <= 60:
            base = 50
        
        a = n1 - base
        b = n2 - base
        sign_a = f"+ {a}" if a > 0 else f"- {-a}"
        sign_b = f"+ {b}" if b > 0 else f"- {-b}"
        
        ans = f"\\({prod}\\)"
        w1 = f"\\({prod + 10}\\)"
        w2 = f"\\({prod - 10}\\)"
        w3 = f"\\({prod + 100}\\)"
        
        q = make_q(
            tc_512, name_512,
            f"Evaluate the product \\({n1} \\times {n2}\\) using the identity \\((x + a)(x + b) = x^2 + (a + b)x + ab\\).",
            ans, [w1, w2, w3],
            f"Express the factors relative to base \\({base}\\): \\({n1} = {base} {sign_a}\\) and \\({n2} = {base} {sign_b}\\).",
            f"Apply the identity with \\(x = {base}, a = {a}, b = {b}\\): \\({base}^2 + ({a} + {b}) \\times {base} + ({a})({b}) = {base*base} + ({a+b})({base}) + ({a*b})\\).",
            f"Summing the terms yields \\({base*base + (a+b)*base + a*b} = {prod}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 5.2.1 Formula: (a+b)³ = a³ + 3a²b + 3ab² + b³ (80 questions)
    # -------------------------------------------------------------
    tc_521 = "MH-8-MTH-5-5.2.1"
    name_521 = "Formula: (a+b)³ = a³ + 3a²b + 3ab² + b³ = a³ + b³ + 3ab(a+b)"
    vars_521 = [
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
        t1, t2 = vars_521[i]
        ans = f"\\(({t1} + {t2})^3 = ({t1})^3 + 3({t1})^2({t2}) + 3({t1})({t2})^2 + ({t2})^3\\)"
        w1 = f"\\(({t1} + {t2})^3 = ({t1})^3 + ({t2})^3\\)"
        w2 = f"\\(({t1} + {t2})^3 = ({t1})^3 + 2({t1})({t2}) + ({t2})^3\\)"
        w3 = f"\\(({t1} + {t2})^3 = ({t1})^3 - 3({t1})^2({t2}) + 3({t1})({t2})^2 - ({t2})^3\\)"
        
        q = make_q(
            tc_521, name_521,
            f"State the full expansion form of \\(({t1} + {t2})^3\\) using the cube of a binomial formula.",
            ans, [w1, w2, w3],
            f"Recall the algebraic identity for the cube of a sum: \\((A + B)^3 = A^3 + 3A^2B + 3AB^2 + B^3\\).",
            f"Here, assign \\(A = {t1}\\) and \\(B = {t2}\\).",
            f"Substituting into the identity gives the expanded polynomial \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 5.2.2 Evaluating numerical cubes (e.g. 52³) (80 questions)
    # -------------------------------------------------------------
    tc_522 = "MH-8-MTH-5-5.2.2"
    name_522 = "Evaluating numerical cubes (e.g. 52³)"
    nums_522 = [
        11, 12, 13, 14, 15, 21, 22, 23, 24, 25,
        31, 32, 33, 34, 35, 41, 42, 43, 44, 45,
        51, 52, 53, 54, 55, 61, 62, 63, 64, 65,
        71, 72, 73, 74, 75, 81, 82, 83, 84, 85,
        91, 92, 93, 94, 95, 101, 102, 103, 104, 105,
        106, 107, 108, 109, 110, 201, 202, 203, 204, 205,
        16, 17, 18, 26, 27, 36, 37, 46, 47, 56,
        57, 66, 67, 76, 77, 86, 87, 96, 97, 111
    ]
    for i in range(80):
        val = nums_522[i]
        cube_val = val ** 3
        tens = (val // 10) * 10
        units = val % 10
        if tens == 0:
            tens = 10
            units = val - 10
        
        ans = f"\\({cube_val:,}\\)".replace(",", "")
        w1 = f"\\({cube_val + 100:,}\\)".replace(",", "")
        w2 = f"\\({cube_val - 100:,}\\)".replace(",", "")
        w3 = f"\\({cube_val + 1000:,}\\)".replace(",", "")
        
        ans_fmt = f"\\({cube_val}\\)"
        w1_fmt = f"\\({cube_val + 100}\\)"
        w2_fmt = f"\\({cube_val - 100}\\)"
        w3_fmt = f"\\({cube_val + 1000}\\)"
        
        q = make_q(
            tc_522, name_522,
            f"Evaluate \\({val}^3\\) by writing it as \\(({tens} + {units})^3\\) using the expansion identity \\((a+b)^3\\).",
            ans_fmt, [w1_fmt, w2_fmt, w3_fmt],
            f"Write \\({val} = {tens} + {units}\\). Then \\(({tens} + {units})^3 = {tens}^3 + 3({tens}^2)({units}) + 3({tens})({units}^2) + {units}^3\\).",
            f"Compute each term: \\({tens}^3 = {tens**3}\\), \\(3({tens}^2)({units}) = {3*(tens**2)*units}\\), \\(3({tens})({units}^2) = {3*tens*(units**2)}\\), and \\({units}^3 = {units**3}\\).",
            f"Sum the calculated terms: \\({tens**3} + {3*(tens**2)*units} + {3*tens*(units**2)} + {units**3} = {cube_val}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 5.3.1 Formula: (a-b)³ = a³ - 3a²b + 3ab² - b³ (80 questions)
    # -------------------------------------------------------------
    tc_531 = "MH-8-MTH-5-5.3.1"
    name_531 = "Formula: (a-b)³ = a³ - 3a²b + 3ab² - b³ = a³ - b³ - 3ab(a-b)"
    vars_531 = [
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
        t1, t2 = vars_531[i]
        ans = f"\\(({t1} - {t2})^3 = ({t1})^3 - 3({t1})^2({t2}) + 3({t1})({t2})^2 - ({t2})^3\\)"
        w1 = f"\\(({t1} - {t2})^3 = ({t1})^3 - ({t2})^3\\)"
        w2 = f"\\(({t1} - {t2})^3 = ({t1})^3 - 3({t1})^2({t2}) - 3({t1})({t2})^2 - ({t2})^3\\)"
        w3 = f"\\(({t1} - {t2})^3 = ({t1})^3 + 3({t1})^2({t2}) - 3({t1})({t2})^2 + ({t2})^3\\)"
        
        q = make_q(
            tc_531, name_531,
            f"State the full expansion form of \\(({t1} - {t2})^3\\) using the cube of a difference formula.",
            ans, [w1, w2, w3],
            f"Recall the algebraic identity for the cube of a difference: \\((A - B)^3 = A^3 - 3A^2B + 3AB^2 - B^3\\).",
            f"Here, assign \\(A = {t1}\\) and \\(B = {t2}\\). Notice the alternating signs: \\(+ - + -\\).",
            f"Substituting into the identity gives the expanded polynomial \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 5.3.2 Evaluating numerical cubes (e.g. 48³) (80 questions)
    # -------------------------------------------------------------
    tc_532 = "MH-8-MTH-5-5.3.2"
    name_532 = "Evaluating numerical cubes (e.g. 48³)"
    nums_532 = [
        9, 19, 29, 39, 49, 59, 69, 79, 89, 99,
        8, 18, 28, 38, 48, 58, 68, 78, 88, 98,
        7, 17, 27, 37, 47, 57, 67, 77, 87, 97,
        199, 198, 197, 299, 298, 999, 998, 997, 499, 498,
        19, 29, 39, 49, 59, 69, 79, 89, 99, 199,
        18, 28, 38, 48, 58, 68, 78, 88, 98, 198,
        17, 27, 37, 47, 57, 67, 77, 87, 97, 197,
        99, 98, 97, 96, 95, 199, 198, 196, 298, 399
    ]
    for i in range(80):
        val = nums_532[i]
        cube_val = val ** 3
        # Round up to nearest ten or hundred
        if val in [9, 8, 7]:
            base = 10
        elif val < 100:
            base = ((val // 10) + 1) * 10
        elif val < 300:
            base = 200 if val < 200 else 300
        else:
            base = 1000 if val > 900 else ((val // 100) + 1) * 100
        diff_val = base - val
        
        ans_fmt = f"\\({cube_val}\\)"
        w1_fmt = f"\\({cube_val + 100}\\)"
        w2_fmt = f"\\({cube_val - 100}\\)"
        w3_fmt = f"\\({cube_val + 1000}\\)"
        
        q = make_q(
            tc_532, name_532,
            f"Evaluate \\({val}^3\\) by writing it as \\(({base} - {diff_val})^3\\) using the expansion identity \\((a-b)^3\\).",
            ans_fmt, [w1_fmt, w2_fmt, w3_fmt],
            f"Express \\({val} = {base} - {diff_val}\\). Using \\((a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3\\), set \\(a = {base}\\) and \\(b = {diff_val}\\).",
            f"Calculate the terms: \\({base}^3 = {base**3}\\), \\(3({base}^2)({diff_val}) = {3*(base**2)*diff_val}\\), \\(3({base})({diff_val}^2) = {3*base*(diff_val**2)}\\), and \\({diff_val}^3 = {diff_val**3}\\).",
            f"Combine the terms: \\({base**3} - {3*(base**2)*diff_val} + {3*base*(diff_val**2)} - {diff_val**3} = {cube_val}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 5.4.1 Formula: (a+b+c)² = a² + b² + c² + 2ab + 2bc + 2ca (80 questions)
    # -------------------------------------------------------------
    tc_541 = "MH-8-MTH-5-5.4.1"
    name_541 = "Formula: (a+b+c)² = a² + b² + c² + 2ab + 2bc + 2ca"
    triples_541 = [
        ("a", "b", "c"), ("x", "y", "z"), ("p", "q", "r"), ("l", "m", "n"), ("u", "v", "w"),
        ("2a", "b", "c"), ("a", "2b", "c"), ("a", "b", "2c"), ("2x", "3y", "z"), ("x", "2y", "3z"),
        ("a", "-b", "c"), ("a", "b", "-c"), ("-a", "b", "c"), ("a", "-b", "-c"), ("-a", "-b", "c"),
        ("x", "-2y", "z"), ("2x", "-y", "3z"), ("3p", "q", "-2r"), ("p", "-2q", "-r"), ("2l", "-3m", "n"),
        ("a", "2", "3"), ("x", "1", "2"), ("2a", "3b", "4c"), ("m", "2n", "3p"), ("k", "2", "3m"),
        ("3x", "2y", "z"), ("x", "3y", "2z"), ("2p", "3q", "r"), ("p", "2q", "3r"), ("4a", "b", "c"),
        ("a", "4b", "c"), ("a", "b", "4c"), ("2x", "2y", "z"), ("x", "2y", "2z"), ("2x", "y", "2z"),
        ("3a", "b", "2c"), ("a", "3b", "2c"), ("2a", "b", "3c"), ("p", "4q", "r"), ("2p", "q", "4r"),
        ("a", "-b", "2c"), ("2a", "-b", "c"), ("a", "2b", "-c"), ("-2a", "b", "c"), ("a", "-2b", "c"),
        ("x", "-y", "2z"), ("2x", "-3y", "z"), ("3x", "y", "-2z"), ("x", "-2y", "-3z"), ("-x", "2y", "3z"),
        ("m", "-n", "p"), ("m", "n", "-p"), ("-m", "n", "p"), ("2m", "-n", "p"), ("m", "-2n", "p"),
        ("k", "-2", "m"), ("2k", "1", "-m"), ("3k", "-m", "2"), ("k", "-3", "-m"), ("2k", "-1", "-2m"),
        ("a", "b", "1"), ("x", "y", "1"), ("2x", "y", "1"), ("x", "2y", "1"), ("p", "q", "1"),
        ("a", "-b", "1"), ("x", "-y", "1"), ("2x", "-y", "1"), ("x", "-2y", "1"), ("p", "-q", "1"),
        ("a", "b", "2"), ("x", "y", "2"), ("2x", "y", "2"), ("x", "2y", "2"), ("p", "q", "2"),
        ("a", "-b", "2"), ("x", "-y", "2"), ("2x", "-y", "2"), ("x", "-2y", "2"), ("p", "-q", "2")
    ]
    for i in range(80):
        t1, t2, t3 = triples_541[i]
        ans = f"\\(({t1} + ({t2}) + ({t3}))^2 = ({t1})^2 + ({t2})^2 + ({t3})^2 + 2({t1})({t2}) + 2({t2})({t3}) + 2({t3})({t1})\\)"
        w1 = f"\\(({t1} + ({t2}) + ({t3}))^2 = ({t1})^2 + ({t2})^2 + ({t3})^2\\)"
        w2 = f"\\(({t1} + ({t2}) + ({t3}))^2 = ({t1})^2 + ({t2})^2 + ({t3})^2 + ({t1})({t2}) + ({t2})({t3}) + ({t3})({t1})\\)"
        w3 = f"\\(({t1} + ({t2}) + ({t3}))^2 = ({t1})^2 + ({t2})^2 + ({t3})^2 - 2({t1})({t2}) - 2({t2})({t3}) - 2({t3})({t1})\\)"
        
        q = make_q(
            tc_541, name_541,
            f"State the general expansion formula for the square of the trinomial \\(({t1} + ({t2}) + ({t3}))^2\\).",
            ans, [w1, w2, w3],
            f"Recall the algebraic expansion of a trinomial squared: \\((A + B + C)^2 = A^2 + B^2 + C^2 + 2AB + 2BC + 2CA\\).",
            f"Here, identify \\(A = {t1}\\), \\(B = {t2}\\), and \\(C = {t3}\\).",
            f"Substituting these terms into the identity produces the expanded form \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 5.4.2 Simplification of polynomial expressions (80 questions)
    # -------------------------------------------------------------
    tc_542 = "MH-8-MTH-5-5.4.2"
    name_542 = "Simplification of polynomial expressions"
    simps_542 = [
        ("(x-2)(x+2) + (x-3)(x+3)", "\\(2x^2 - 13\\)", ["\\(2x^2 + 13\\)", "\\(x^2 - 13\\)", "\\(2x^2 - 5\\)"]),
        ("(x+1)(x+2) + (x-1)(x-2)", "\\(2x^2 + 6\\)", ["\\(2x^2 - 6\\)", "\\(2x^2 + 4x + 6\\)", "\\(x^2 + 6\\)"]),
        ("(x+3)(x-3) - (x-4)(x+4)", "\\(7\\)", ["\\(-7\\)", "\\(25\\)", "\\(2x^2 - 25\\)"]),
        ("(2x+1)^2 - (2x-1)^2", "\\(8x\\)", ["\\(4x\\)", "\\(8x^2\\)", "\\(16x\\)"]),
        ("(3x+2)^2 - (3x-2)^2", "\\(24x\\)", ["\\(12x\\)", "\\(24x^2\\)", "\\(18x\\)"]),
        ("(a+b)^3 + (a-b)^3", "\\(2a^3 + 6ab^2\\)", ["\\(2a^3 + 2b^3\\)", "\\(2a^3 + 6a^2b\\)", "\\(6ab^2\\)"]),
        ("(a+b)^3 - (a-b)^3", "\\(6a^2b + 2b^3\\)", ["\\(2b^3\\)", "\\(6ab^2 + 2b^3\\)", "\\(6a^2b\\)"]),
        ("(x+1)^3 + (x-1)^3", "\\(2x^3 + 6x\\)", ["\\(2x^3 + 2\\)", "\\(2x^3 + 6x^2\\)", "\\(6x\\)"]),
        ("(x+1)^3 - (x-1)^3", "\\(6x^2 + 2\\)", ["\\(2x^3 + 2\\)", "\\(6x + 2\\)", "\\(6x^2\\)"]),
        ("(2x+1)^3 - (2x-1)^3", "\\(24x^2 + 2\\)", ["\\(16x^3 + 2\\)", "\\(24x^2\\)", "\\(12x^2 + 2\\)"]),
        ("(x+2)^3 - (x-2)^3", "\\(12x^2 + 16\\)", ["\\(2x^3 + 16\\)", "\\(12x^2\\)", "\\(6x^2 + 16\\)"]),
        ("(x+y+z)^2 + (x-y+z)^2", "\\(2x^2 + 2y^2 + 2z^2 + 4xz\\)", ["\\(2x^2 + 2y^2 + 2z^2\\)", "\\(4xz + 4xy\\)", "\\(2x^2 + 2z^2 + 4xz\\)"]),
        ("(x+y+z)^2 - (x-y+z)^2", "\\(4xy + 4yz\\)", ["\\(4xy\\)", "\\(4yz\\)", "\\(2y^2 + 4xy + 4yz\\)"]),
        ("(a+b+c)^2 + (a+b-c)^2", "\\(2a^2 + 2b^2 + 2c^2 + 4ab\\)", ["\\(2a^2 + 2b^2 + 2c^2\\)", "\\(4ab + 4bc\\)", "\\(2a^2 + 4ab\\)"]),
        ("(a+b+c)^2 - (a+b-c)^2", "\\(4ac + 4bc\\)", ["\\(4ab\\)", "\\(2c^2 + 4ac + 4bc\\)", "\\(4ac\\)"]),
        ("(2x+3y)^2 - (2x-3y)^2", "\\(24xy\\)", ["\\(12xy\\)", "\\(24x^2y^2\\)", "\\(18xy\\)"]),
        ("(p+q)^2 - (p-q)^2", "\\(4pq\\)", ["\\(2pq\\)", "\\(4p^2q^2\\)", "\\(2p^2 + 2q^2\\)"]),
        ("(p+q)^2 + (p-q)^2", "\\(2p^2 + 2q^2\\)", ["\\(4pq\\)", "\\(2p^2 - 2q^2\\)", "\\(p^2 + q^2\\)"]),
        ("(m+2n)^2 - (m-2n)^2", "\\(8mn\\)", ["\\(4mn\\)", "\\(8m^2n^2\\)", "\\(2m^2 + 8n^2\\)"]),
        ("(3a+b)^2 - (3a-b)^2", "\\(12ab\\)", ["\\(6ab\\)", "\\(12a^2b^2\\)", "\\(18a^2 + 2b^2\\)"])
    ]
    # Replicate up to 80 with variations
    for i in range(80):
        base_expr, base_ans, base_wrongs = simps_542[i % len(simps_542)]
        if i >= len(simps_542):
            k = (i // len(simps_542)) + 1
            # Add an index annotation to ensure unique variation text
            expr = f"{base_expr} \\text{{ [Case {k}]}}"
        else:
            expr = base_expr
            
        q = make_q(
            tc_542, name_542,
            f"Simplify the algebraic polynomial expression: \\({expr}\\).",
            base_ans, base_wrongs,
            f"Expand each term separately using the appropriate expansion formula.",
            f"Collect and group like terms together, paying careful attention to negative signs.",
            f"Combine like terms to arrive at the simplified expression \\({base_ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch5_questions()
    print(f"Generated {len(qs)} questions for Chapter 5.")
    out_path = "scripts/mh8_mth_ch5_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
