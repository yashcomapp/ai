import json
import random

random.seed(8301)

def build_ch1_questions():
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

    # 1.1.1 Definition of rational numbers m/n (need 80)
    tc = "MH-8-MTH-1-1.1.1"
    name = "Definition of rational numbers m/n"
    for i in range(80):
        m = -10 + i
        n = 3 + (i % 7)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"According to the Maharashtra State Board curriculum, why is \\(\\frac{{{m}}}{{{n}}}\\) classified as a rational number?",
            f"Because it is written in the form \\(\\frac{{m}}{{n}}\\) where \\(m={m}\\) and \\(n={n}\\) are integers and \\(n \\neq 0\\)",
            [
                f"Because \\(m={m}\\) must be strictly positive",
                f"Because \\(n={n}\\) is a multiple of 10",
                "Because every fraction must be less than 1"
            ],
            f"In the Balbharti mathematics syllabus, the numbers of the form \\(\\frac{{m}}{{n}}\\) are called rational numbers.",
            f"Here \\(m\\) and \\(n\\) are integers and \\(n\\) is a non-zero integer (\\(n \\neq 0\\)).",
            f"Since \\({m}\\) and \\({n}\\) are integers and \\({n} \\neq 0\\), \\(\\frac{{{m}}}{{{n}}}\\) is a rational number.",
            d, v
        )
        questions.append(q)

    # 1.1.2 Plotting fractions and negative rational numbers on number line (need 80)
    tc = "MH-8-MTH-1-1.1.2"
    name = "Plotting fractions and negative rational numbers on number line"
    for i in range(80):
        val = 2 + (i % 7)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"A point \\(P\\) on the number line represents \\(-\\frac{{{val}}}{{5}}\\). In which direction and at what distance from the origin (0) does \\(P\\) lie?",
            f"To the left of 0, at a distance of \\({val}\\) sub-units of length \\(\\frac{{1}}{{5}}\\)",
            [
                f"To the right of 0, at a distance of \\({val}\\) sub-units",
                "Directly at integer -1",
                "To the right of +1"
            ],
            f"Negative numbers are plotted to the left of the origin 0.",
            f"Each sub-unit on this scale has length \\(\\frac{{1}}{{5}}\\).",
            f"Hence, \\(-\\frac{{{val}}}{{5}}\\) lies \\({val}\\) units of \\(\\frac{{1}}{{5}}\\) to the left of 0.",
            d, v
        )
        questions.append(q)

    # 1.1.3 Equivalent fractions (need 80)
    tc = "MH-8-MTH-1-1.1.3"
    name = "Equivalent fractions"
    for i in range(80):
        num = 2 + (i % 6)
        den = 3 + (i % 5)
        if num == den: den += 1
        k = 2 + (i % 5)
        eq_num = num * k
        eq_den = den * k
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Which of the following is an equivalent fraction of \\(\\frac{{{num}}}{{{den}}}\\)?",
            f"\\(\\frac{{{eq_num}}}{{{eq_den}}}\\)",
            [f"\\(\\frac{{{eq_num + 1}}}{{{eq_den}}}\\)", f"\\(\\frac{{{eq_num}}}{{{eq_den + 1}}}\\)", f"\\(\\frac{{{num + k}}}{{{den + k}}}\\)"],
            f"An equivalent fraction is obtained by multiplying both numerator and denominator by the same non-zero integer \\(k\\).",
            f"Multiply \\(\\frac{{{num}}}{{{den}}}\\) by \\(\\frac{{{k}}}{{{k}}}\\): \\(\\frac{{{num} \\times {k}}}{{{den} \\times {k}}} = \\frac{{{eq_num}}}{{{eq_den}}}\\).",
            f"Therefore, \\(\\frac{{{eq_num}}}{{{eq_den}}}\\) is an equivalent fraction.",
            d, v
        )
        questions.append(q)

    # 1.2.1 Cross multiplication rule (a/b vs c/d) (need 80)
    tc = "MH-8-MTH-1-1.2.1"
    name = "Cross multiplication rule (a/b vs c/d)"
    for i in range(80):
        a, b = 2 + (i % 4), 3 + (i % 3)
        c, d_val = 3 + (i % 3), 4 + (i % 3)
        ad = a * d_val
        bc = b * c
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        if ad > bc:
            rel = ">"
            ans = f"\\(\\frac{{{a}}}{{{b}}} > \\frac{{{c}}}{{{d_val}}}\\) because \\({a} \\times {d_val} = {ad} > {b} \\times {c} = {bc}\\)"
            wrongs = [
                f"\\(\\frac{{{a}}}{{{b}}} < \\frac{{{c}}}{{{d_val}}}\\)",
                f"\\(\\frac{{{a}}}{{{b}}} = \\frac{{{c}}}{{{d_val}}}\\)",
                "Cannot be determined without a decimal"
            ]
        elif ad < bc:
            rel = "<"
            ans = f"\\(\\frac{{{a}}}{{{b}}} < \\frac{{{c}}}{{{d_val}}}\\) because \\({a} \\times {d_val} = {ad} < {b} \\times {c} = {bc}\\)"
            wrongs = [
                f"\\(\\frac{{{a}}}{{{b}}} > \\frac{{{c}}}{{{d_val}}}\\)",
                f"\\(\\frac{{{a}}}{{{b}}} = \\frac{{{c}}}{{{d_val}}}\\)",
                "Cannot be determined without a decimal"
            ]
        else:
            rel = "="
            ans = f"\\(\\frac{{{a}}}{{{b}}} = \\frac{{{c}}}{{{d_val}}}\\) because \\({a} \\times {d_val} = {b} \\times {c} = {ad}\\)"
            wrongs = [
                f"\\(\\frac{{{a}}}{{{b}}} > \\frac{{{c}}}{{{d_val}}}\\)",
                f"\\(\\frac{{{a}}}{{{b}}} < \\frac{{{c}}}{{{d_val}}}\\)",
                "Cannot be determined without a decimal"
            ]
        q = make_q(
            tc, name,
            f"Compare the rational numbers \\(\\frac{{{a}}}{{{b}}}\\) and \\(\\frac{{{c}}}{{{d_val}}}\\) using the cross-multiplication rule.",
            ans, wrongs,
            f"For positive denominators \\(b > 0, d > 0\\), compare the cross products \\(a \\times d\\) and \\(b \\times c\\).",
            f"Calculate \\(a \\times d = {a} \\times {d_val} = {ad}\\) and \\(b \\times c = {b} \\times {c} = {bc}\\).",
            f"Since \\({ad} {rel} {bc}\\), it follows that \\(\\frac{{{a}}}{{{b}}} {rel} \\frac{{{c}}}{{{d_val}}}\\).",
            d, v
        )
        questions.append(q)

    # 1.2.2 Comparing positive and negative rational numbers (need 80)
    tc = "MH-8-MTH-1-1.2.2"
    name = "Comparing positive and negative rational numbers"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "If two rational numbers have negative numerators: \\(-\\frac{5}{7}\\) and \\(-\\frac{3}{7}\\), which number is greater?",
            "\\(-\\frac{3}{7}\\) is greater, because \\(-3 > -5\\) on the number line",
            [
                "\\(-\\frac{5}{7}\\) is greater, because 5 is greater than 3",
                "Both numbers are equal",
                "Negative rational numbers cannot be compared"
            ],
            f"When denominators are identical and positive (here, 7), the comparison depends solely on the numerators.",
            f"Comparing the numerators: \\(-3 > -5\\) (since \\(-3\\) lies to the right of \\(-5\\) on the number line).",
            f"Therefore, \\(-\\frac{3}{7} > -\\frac{5}{7}\\).",
            d, v
        )
        questions.append(q)

    # 1.3.1 Terminating decimal form (need 80)
    tc = "MH-8-MTH-1-1.3.1"
    name = "Terminating decimal form"
    for i in range(80):
        den = [2, 4, 5, 8, 10, 16, 20, 25, 40, 50][i % 10]
        num = 1 + (i % 7)
        dec_val = num / den
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Convert \\(\\frac{{{num}}}{{{den}}}\\) into its decimal form and identify whether it is terminating or non-terminating.",
            f"\\({dec_val}\\) (Terminating)",
            [f"\\({dec_val}\\) (Non-terminating recurring)", f"\\({dec_val + 0.1}\\) (Irrational)", "\\(0.333\\dots\\) (Terminating)"],
            f"Divide the numerator \\({num}\\) by the denominator \\({den}\\).",
            f"Notice that the prime factors of denominator \\({den}\\) consist exclusively of 2s and/or 5s.",
            f"Therefore, the division terminates completely with remainder 0, giving the terminating decimal \\({dec_val}\\).",
            d, v
        )
        questions.append(q)

    # 1.3.2 Non-terminating recurring decimal form (dot/bar notation) (need 80)
    tc = "MH-8-MTH-1-1.3.2"
    name = "Non-terminating recurring decimal form (dot/bar notation)"
    for i in range(80):
        den = [3, 6, 7, 9, 11][i % 5]
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"What type of decimal representation does the rational number \\(\\frac{{1}}{{{den}}}\\) possess in Balbharti mathematics?",
            "Non-terminating recurring decimal form (represented by a dot or horizontal bar)",
            ["Terminating decimal form", "Non-terminating non-recurring decimal form", "Whole integer form"],
            f"Examine the prime factorisation of denominator \\({den}\\): it contains a prime factor other than 2 and 5.",
            f"When dividing 1 by \\({den}\\), a digit or group of digits recurs endlessly.",
            f"In Maharashtra State Board convention, a dot is placed over a single recurring digit or a horizontal bar over a recurring block of digits.",
            d, v
        )
        questions.append(q)

    # 1.4.1 Definition of irrational numbers (non-terminating non-recurring) (need 80)
    tc = "MH-8-MTH-1-1.4.1"
    name = "Definition of irrational numbers (non-terminating non-recurring)"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "Which of the following defines an IRRATIONAL number in Maharashtra Board mathematics?",
            "A number whose decimal form is non-terminating and non-recurring (cannot be written as m/n)",
            [
                "A number that has a repeating block of decimals",
                "Any negative rational number",
                "A fraction with denominator 0"
            ],
            f"Numbers that cannot be expressed in the form \\(\\frac{{m}}{{n}}\\) (where \\(m, n\\) are integers and \\(n \\neq 0\\)) are irrational numbers.",
            f"Their decimal representation is both non-terminating and non-recurring.",
            f"Numbers like \\(\\sqrt{2}, \\sqrt{3}, \\pi\\) are classic examples of irrational numbers.",
            d, v
        )
        questions.append(q)

    # 1.4.2 Geometric construction of √2 and √3 on number line using Pythagoras (need 80)
    tc = "MH-8-MTH-1-1.4.2"
    name = "Geometric construction of √2 and √3 on number line using Pythagoras"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "How is the irrational number \\(\\sqrt{2}\\) geometrically constructed on a number line using Pythagoras' theorem?",
            "By constructing a right triangle with base 1 unit and perpendicular height 1 unit at 1, giving hypotenuse \\(\\sqrt{1^2 + 1^2} = \\sqrt{2}\\)",
            [
                "By dividing the segment between 1 and 2 into two equal parts",
                "By squaring 2 and dividing by 4",
                "By drawing a circle of radius 2 units"
            ],
            f"Draw a unit segment \\(OA = 1\\) on the number line. At point \\(A(1)\\), erect a perpendicular line segment \\(AB = 1\\).",
            f"Join \\(OB\\). By the Pythagoras theorem in \\(\\triangle OAB\\), \\(OB^2 = OA^2 + AB^2 = 1^2 + 1^2 = 2 \\implies OB = \\sqrt{2}\\).",
            f"Using a compass with center \\(O\\) and radius \\(OB\\), draw an arc cutting the number line at coordinate \\(\\sqrt{2}\\).",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch1_questions()
    print(f"Generated {len(qs)} questions for Chapter 1.")
    with open("scripts/mh8_mth_ch1_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/mh8_mth_ch1_topup.json")
