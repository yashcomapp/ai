import json
import random

random.seed(81212)

def build_ch12_questions():
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
    # 12.1.1 Adding, subtracting, multiplying, dividing non-zero terms on both sides (80 questions)
    # -------------------------------------------------------------
    tc_1211 = "MH-8-MTH-12-12.1.1"
    name_1211 = "Adding, subtracting, multiplying, dividing non-zero terms on both sides"
    eqs_1211 = [
        ("3x + 5 = 20", "x = 5", ["x = 4", "x = 6", "x = 7"]),
        ("4x - 7 = 13", "x = 5", ["x = 6", "x = 4", "x = 3"]),
        ("2x + 9 = 25", "x = 8", ["x = 7", "x = 9", "x = 6"]),
        ("5x - 8 = 22", "x = 6", ["x = 5", "x = 7", "x = 8"]),
        ("6x + 4 = 40", "x = 6", ["x = 7", "x = 5", "x = 8"]),
        ("7x - 3 = 32", "x = 5", ["x = 6", "x = 4", "x = 7"]),
        ("8x + 1 = 65", "x = 8", ["x = 7", "x = 9", "x = 6"]),
        ("9x - 10 = 35", "x = 5", ["x = 6", "x = 4", "x = 7"]),
        ("2x - 11 = 15", "x = 13", ["x = 12", "x = 14", "x = 11"]),
        ("3x + 12 = 36", "x = 8", ["x = 9", "x = 7", "x = 6"]),
        ("4x - 15 = 25", "x = 10", ["x = 9", "x = 11", "x = 8"]),
        ("5x + 20 = 55", "x = 7", ["x = 6", "x = 8", "x = 9"]),
        ("6x - 18 = 30", "x = 8", ["x = 7", "x = 9", "x = 6"]),
        ("7x + 14 = 49", "x = 5", ["x = 6", "x = 4", "x = 7"]),
        ("8x - 24 = 32", "x = 7", ["x = 6", "x = 8", "x = 5"]),
        ("9x + 18 = 72", "x = 6", ["x = 5", "x = 7", "x = 8"])
    ]
    for i in range(80):
        eq, ans_str, wrongs = eqs_1211[i % len(eqs_1211)]
        ans = f"\\({ans_str}\\)"
        w_opts = [f"\\({w}\\)" for w in wrongs]
        q = make_q(
            tc_1211, name_1211,
            f"Solve the linear equation for the unknown variable: \\({eq}\\).",
            ans, w_opts,
            "Transpose the constant term to the right-hand side with reversed sign.",
            "Simplify the right-hand side arithmetic.",
            f"Divide both sides by the coefficient of the variable to obtain \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 12.1.2 Solving brackets (80 questions)
    # -------------------------------------------------------------
    tc_1212 = "MH-8-MTH-12-12.1.2"
    name_1212 = "Solving brackets"
    bracket_eqs = [
        ("2(x - 3) = 14", "x = 10", ["x = 8", "x = 12", "x = 7"]),
        ("3(x + 4) = 27", "x = 5", ["x = 6", "x = 4", "x = 7"]),
        ("4(2x - 1) = 28", "x = 4", ["x = 3", "x = 5", "x = 6"]),
        ("5(x + 2) = 35", "x = 5", ["x = 6", "x = 4", "x = 7"]),
        ("2(3x - 1) = 28", "x = 5", ["x = 4", "x = 6", "x = 7"]),
        ("3(2x + 5) = 39", "x = 4", ["x = 3", "x = 5", "x = 6"]),
        ("4(x - 5) = 24", "x = 11", ["x = 10", "x = 12", "x = 9"]),
        ("6(x + 1) = 48", "x = 7", ["x = 6", "x = 8", "x = 9"]),
        ("2(4x - 3) = 26", "x = 4", ["x = 3", "x = 5", "x = 6"]),
        ("3(x - 7) = 15", "x = 12", ["x = 11", "x = 13", "x = 10"]),
        ("5(2x + 1) = 45", "x = 4", ["x = 3", "x = 5", "x = 6"]),
        ("4(3x - 2) = 40", "x = 4", ["x = 3", "x = 5", "x = 6"]),
        ("2(5x + 3) = 46", "x = 4", ["x = 3", "x = 5", "x = 6"]),
        ("7(x - 2) = 35", "x = 7", ["x = 6", "x = 8", "x = 9"]),
        ("3(3x + 4) = 48", "x = 4", ["x = 3", "x = 5", "x = 6"]),
        ("8(x - 1) = 56", "x = 8", ["x = 7", "x = 9", "x = 6"])
    ]
    for i in range(80):
        eq, ans_str, wrongs = bracket_eqs[i % len(bracket_eqs)]
        ans = f"\\({ans_str}\\)"
        w_opts = [f"\\({w}\\)" for w in wrongs]
        q = make_q(
            tc_1212, name_1212,
            f"Solve the linear equation involving brackets: \\({eq}\\).",
            ans, w_opts,
            "Expand the bracket on the left side by multiplying the outer factor across each internal term.",
            "Transpose the numerical constant to the right-hand side.",
            f"Divide by the coefficient of \\(x\\) to determine \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 12.2.1 Formulating linear equations from given conditions (80 questions)
    # -------------------------------------------------------------
    tc_1221 = "MH-8-MTH-12-12.2.1"
    name_1221 = "Formulating linear equations from given conditions"
    word_forms = [
        ("The sum of a number and 12 is 35", "\\(x + 12 = 35\\)", ["\\(x - 12 = 35\\)", "\\(12x = 35\\)", "\\(\\frac{x}{12} = 35\\)"]),
        ("Twice a number decreased by 7 is equal to 19", "\\(2x - 7 = 19\\)", ["\\(2x + 7 = 19\\)", "\\(7 - 2x = 19\\)", "\\(2(x - 7) = 19\\)"]),
        ("Five times a number added to 8 gives 43", "\\(5x + 8 = 43\\)", ["\\(5x - 8 = 43\\)", "\\(8x + 5 = 43\\)", "\\(5(x + 8) = 43\\)"]),
        ("A father is 25 years older than his son, and their combined age is 55", "\\(x + (x + 25) = 55\\)", ["\\(x + (x - 25) = 55\\)", "\\(25x = 55\\)", "\\(x + 25 = 55\\)"]),
        ("Three consecutive integers add up to 72", "\\(x + (x + 1) + (x + 2) = 72\\)", ["\\(x + (x + 2) + (x + 4) = 72\\)", "\\(3x = 72\\)", "\\(x(x+1)(x+2) = 72\\)"]),
        ("One-third of a number added to 10 gives 22", "\\(\\frac{x}{3} + 10 = 22\\)", ["\\(3x + 10 = 22\\)", "\\(\\frac{x+10}{3} = 22\\)", "\\(\\frac{x}{3} - 10 = 22\\)"]),
        ("The perimeter of a rectangle whose length is 4 cm more than its breadth is 48 cm", "\\(2[x + (x + 4)] = 48\\)", ["\\(x + (x + 4) = 48\\)", "\\(x(x + 4) = 48\\)", "\\(2x + 4 = 48\\)"]),
        ("Subtracting 15 from 4 times a number yields 45", "\\(4x - 15 = 45\\)", ["\\(4x + 15 = 45\\)", "\\(15 - 4x = 45\\)", "\\(4(x - 15) = 45\\)"])
    ]
    for i in range(80):
        stmt, ans, wrongs = word_forms[i % len(word_forms)]
        q = make_q(
            tc_1221, name_1221,
            f"Translate the word problem into a linear equation in one variable \\(x\\): '{stmt}'.",
            ans, wrongs,
            "Let the unknown quantity be denoted by the variable \\(x\\).",
            "Translate each verbal condition into corresponding mathematical operations.",
            f"Equating the expressions gives \\({ans}\\).",
            diffs[i], vaults[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 12.2.2 Step-by-step verification of solutions (80 questions)
    # -------------------------------------------------------------
    tc_1222 = "MH-8-MTH-12-12.2.2"
    name_1222 = "Step-by-step verification of solutions"
    verifs = [
        ("3x + 4 = 19", 5, "\\(\\text{L.H.S.} = 3(5) + 4 = 15 + 4 = 19 = \\text{R.H.S.} \\implies x = 5\\text{ is verified}\\)", ["\\(\\text{L.H.S.} \\neq \\text{R.H.S.}\\)", "\\(x = 5\\text{ is extraneous}\\)", "\\(\\text{L.H.S.} = 20 \\neq 19\\)"]),
        ("2x - 5 = 11", 8, "\\(\\text{L.H.S.} = 2(8) - 5 = 16 - 5 = 11 = \\text{R.H.S.} \\implies x = 8\\text{ is verified}\\)", ["\\(\\text{L.H.S.} \\neq \\text{R.H.S.}\\)", "\\(x = 8\\text{ is invalid}\\)", "\\(\\text{L.H.S.} = 12 \\neq 11\\)"]),
        ("4x + 3 = 27", 6, "\\(\\text{L.H.S.} = 4(6) + 3 = 24 + 3 = 27 = \\text{R.H.S.} \\implies x = 6\\text{ is verified}\\)", ["\\(\\text{L.H.S.} \\neq \\text{R.H.S.}\\)", "\\(x = 6\\text{ fails check}\\)", "\\(\\text{L.H.S.} = 25 \\neq 27\\)"]),
        ("5x - 7 = 28", 7, "\\(\\text{L.H.S.} = 5(7) - 7 = 35 - 7 = 28 = \\text{R.H.S.} \\implies x = 7\\text{ is verified}\\)", ["\\(\\text{L.H.S.} \\neq \\text{R.H.S.}\\)", "\\(x = 7\\text{ is extraneous}\\)", "\\(\\text{L.H.S.} = 30 \\neq 28\\)"])
    ]
    for i in range(80):
        eq, val, ans, wrongs = verifs[i % len(verifs)]
        q = make_q(
            tc_1222, name_1222,
            f"Verify whether \\(x = {val}\\) is the correct root of the equation \\({eq}\\) by testing \\(\\text{{L.H.S.}} = \\text{{R.H.S.}}\\).",
            ans, wrongs,
            f"Substitute \\(x = {val}\\) into the left-hand side (L.H.S.) of the equation.",
            "Evaluate the arithmetic expression on the L.H.S.",
            f"Compare with R.H.S.: {ans}.",
            diffs[i], vaults[i]
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch12_questions()
    print(f"Generated {len(qs)} questions for Chapter 12.")
    out_path = "scripts/mh8_mth_ch12_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
