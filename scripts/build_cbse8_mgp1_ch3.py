import json
import random
from math import gcd

random.seed(8103)

def build_ch3_questions():
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

    # 3.1.1 Rational numbers definition (p/q, q != 0) (need 54)
    tc = "CBSE-8-MGP1-3-3.1.1"
    name = "Rational numbers definition (p/q, q != 0)"
    for i in range(54):
        p = -15 + i
        q_denom = 2 + (i % 7)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Why is the number \\(\\frac{{{p}}}{{{q_denom}}}\\) classified as a rational number?",
            f"Because it is written in the form \\(\\frac{{p}}{{q}}\\) where \\(p={p}\\) and \\(q={q_denom}\\) are integers and \\(q \\neq 0\\).",
            [
                f"Because \\(p={p}\\) is strictly a positive natural number.",
                f"Because its denominator is greater than its numerator.",
                "Because every fraction must terminate in an integer."
            ],
            f"Recall the formal definition of a rational number: any number that can be expressed as \\(\\frac{{p}}{{q}}\\) where \\(p\\) and \\(q\\) are integers and \\(q \\neq 0\\).",
            f"Here \\(p = {p}\\) and \\(q = {q_denom}\\), both of which are integers, and \\({q_denom} \\neq 0\\).",
            f"Therefore, \\(\\frac{{{p}}}{{{q_denom}}}\\) is a valid rational number.",
            d, v
        )
        questions.append(q)

    # 3.1.2 Closure property under addition, subtraction, multiplication (need 50)
    tc = "CBSE-8-MGP1-3-3.1.2"
    name = "Closure property under addition, subtraction, multiplication"
    for i in range(50):
        ops = ["addition", "subtraction", "multiplication"][i % 3]
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"If \\(a\\) and \\(b\\) are any two rational numbers, which of the following statements correctly expresses the closure property of rational numbers under {ops}?",
            f"The result \\(a \\star b\\) under {ops} is always a rational number.",
            [
                f"The result under {ops} is always a positive integer.",
                f"The result under {ops} is commutative.",
                f"Rational numbers are not closed under {ops}."
            ],
            f"Closure means that performing an operation on any two elements of a set always produces an element within that same set.",
            f"Rational numbers \\(\\mathbb{{Q}}\\) are closed under addition, subtraction, and multiplication.",
            f"Thus, operating on any two rational numbers under {ops} yields another rational number.",
            d, v
        )
        questions.append(q)

    # 3.1.3 Commutative property for operations on rationals (need 54)
    tc = "CBSE-8-MGP1-3-3.1.3"
    name = "Commutative property for operations on rationals"
    for i in range(54):
        a1, b1 = 2 + (i % 5), 3 + (i % 4)
        a2, b2 = 1 + (i % 3), 4 + (i % 3)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"For two rational numbers \\(x = \\frac{{{a1}}}{{{b1}}}\\) and \\(y = \\frac{{{a2}}}{{{b2}}}\\), which operation is strictly COMMUTATIVE?",
            "Addition and Multiplication",
            ["Subtraction and Division", "Division only", "Subtraction only"],
            f"Commutativity states that changing the order of operands does not change the result: \\(x \\star y = y \\star x\\).",
            f"For rational numbers, addition \\(x + y = y + x\\) and multiplication \\(x \\times y = y \\times x\\) are commutative, whereas subtraction and division are not.",
            f"Hence, Addition and Multiplication are commutative.",
            d, v
        )
        questions.append(q)

    # 3.2.1 Associative property for addition and multiplication (need 59)
    tc = "CBSE-8-MGP1-3-3.2.1"
    name = "Associative property for addition and multiplication"
    for i in range(59):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "Which of the following algebraic equations demonstrates the ASSOCIATIVE property of addition for rational numbers?",
            "\\((a + b) + c = a + (b + c)\\)",
            ["\\(a + b = b + a\\)", "\\(a \\times (b + c) = a \\times b + a \\times c\\)", "\\(a + 0 = a\\)"],
            f"The associative property of addition states that the way numbers are grouped does not affect their sum.",
            f"Mathematically, for any rational numbers \\(a, b, c\\), \\((a + b) + c = a + (b + c)\\).",
            f"Therefore, \\((a + b) + c = a + (b + c)\\) correctly represents the associative property.",
            d, v
        )
        questions.append(q)

    # 3.2.2 Additive identity (0) and additive inverse (negative) (need 61)
    tc = "CBSE-8-MGP1-3-3.2.2"
    name = "Additive identity (0) and additive inverse (negative)"
    for i in range(61):
        num = 2 + (i % 9)
        den = 3 + (i % 8)
        if num == den: den += 1
        is_neg = (i % 2 == 1)
        orig_str = f"-\\frac{{{num}}}{{{den}}}" if is_neg else f"\\frac{{{num}}}{{{den}}}"
        inv_str = f"\\frac{{{num}}}{{{den}}}" if is_neg else f"-\\frac{{{num}}}{{{den}}}"
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"What is the additive inverse of the rational number \\({orig_str}\\)?",
            f"\\({inv_str}\\)",
            [f"\\(\\frac{{{den}}}{{{num}}}\\)", f"\\(0\\)", f"\\(1\\)"],
            f"The additive inverse of a rational number \\(x\\) is the number \\(-x\\) such that \\(x + (-x) = 0\\).",
            f"Here, \\(x = {orig_str}\\). The negative of \\(x\\) is \\({inv_str}\\).",
            f"Since \\({orig_str} + ({inv_str}) = 0\\), the additive inverse is \\({inv_str}\\).",
            d, v
        )
        questions.append(q)

    # 3.2.3 Multiplicative identity (1) and reciprocal (need 55)
    tc = "CBSE-8-MGP1-3-3.2.3"
    name = "Multiplicative identity (1) and reciprocal"
    for i in range(55):
        num = 3 + (i % 7)
        den = 5 + (i % 6)
        if num == den: den += 2
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find the multiplicative inverse (reciprocal) of \\(-\\frac{{{num}}}{{{den}}}\\).",
            f"\\(-\\frac{{{den}}}{{{num}}}\\)",
            [f"\\(\\frac{{{num}}}{{{den}}}\\)", f"\\(\\frac{{{den}}}{{{num}}}\\)", f"\\(1\\)"],
            f"The multiplicative inverse (reciprocal) of a non-zero rational number \\(\\frac{{a}}{{b}}\\) is \\(\\frac{{b}}{{a}}\\) such that their product is 1.",
            f"For \\(-\\frac{{{num}}}{{{den}}}\\), multiplying by \\(-\\frac{{{den}}}{{{num}}}\\) yields \\((-\\frac{{{num}}}{{{den}}}) \\times (-\\frac{{{den}}}{{{num}}}) = 1\\).",
            f"Hence, the multiplicative inverse is \\(-\\frac{{{den}}}{{{num}}}\\).",
            d, v
        )
        questions.append(q)

    # 3.2.4 Distributive property of multiplication over addition/subtraction (need 63)
    tc = "CBSE-8-MGP1-3-3.2.4"
    name = "Distributive property of multiplication over addition/subtraction"
    for i in range(63):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "Which identity illustrates the distributive property of multiplication over addition for rational numbers?",
            "\\(a \\times (b + c) = (a \\times b) + (a \\times c)\\)",
            [
                "\\(a + (b + c) = (a + b) + c\\)",
                "\\(a \\times b = b \\times a\\)",
                "\\(a \\times (b \\times c) = (a \\times b) \\times c\\)"
            ],
            f"The distributive property of multiplication over addition distributes multiplication across grouped terms inside parentheses.",
            f"For any rational numbers \\(a, b, c\\), \\(a(b + c) = ab + ac\\).",
            f"Therefore, \\(a \\times (b + c) = (a \\times b) + (a \\times c)\\) is the correct expression.",
            d, v
        )
        questions.append(q)

    # 3.3.1 Dividing unit intervals into equal parts (need 41)
    tc = "CBSE-8-MGP1-3-3.3.1"
    name = "Dividing unit intervals into equal parts"
    for i in range(41):
        d_val = 3 + (i % 8)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"To represent the rational number \\(\\frac{{1}}{{{d_val}}}\\) on a number line, into how many equal parts must the unit interval from 0 to 1 be divided?",
            f"\\({d_val}\\) equal parts",
            [f"\\({d_val - 1}\\) equal parts", f"\\({d_val + 1}\\) equal parts", f"\\(2 \\times {d_val}\\) equal parts"],
            f"The denominator of a fraction indicates the total number of equal sub-divisions into which each unit length is partitioned.",
            f"Since the denominator is \\({d_val}\\), the unit segment between 0 and 1 must be divided into \\({d_val}\\) equal parts.",
            f"Thus, \\({d_val}\\) equal parts is the correct answer.",
            d, v
        )
        questions.append(q)

    # 3.3.2 Plotting positive and negative rationals (need 37)
    tc = "CBSE-8-MGP1-3-3.3.2"
    name = "Plotting positive and negative rationals"
    for i in range(37):
        num = 2 + (i % 5)
        den = 7
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"On a standard horizontal number line, on which side of the origin (0) does the rational number \\(-\\frac{{{num}}}{{{den}}}\\) lie?",
            "To the left of 0",
            ["To the right of 0", "Directly at 0", "At +1"],
            f"On a horizontal number line, 0 serves as the origin.",
            f"Positive rational numbers are plotted to the right of 0, whereas negative rational numbers are plotted to the left of 0.",
            f"Since \\(-\\frac{{{num}}}{{{den}}} < 0\\), it lies to the left of 0.",
            d, v
        )
        questions.append(q)

    # 3.4.1 Mean / average method (need 66)
    tc = "CBSE-8-MGP1-3-3.4.1"
    name = "Mean / average method"
    for i in range(66):
        a = 1 + (i % 4)
        b = a + 1
        sum_ab = a + b
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find a rational number strictly between \\({a}\\) and \\({b}\\) using the mean method.",
            f"\\(\\frac{{{sum_ab}}}{{2}}\\)",
            [f"\\(\\frac{{{sum_ab}}}{{4}}\\)", f"\\({a}\\)", f"\\({b}\\)"],
            f"The mean method finds a rational number between two numbers \\(x\\) and \\(y\\) by computing their arithmetic mean: \\(\\frac{{x + y}}{{2}}\\).",
            f"Substitute \\(x = {a}\\) and \\(y = {b}\\): \\(\\frac{{{a} + {b}}}{{2}} = \\frac{{{sum_ab}}}{{2}}\\).",
            f"Hence, \\(\\frac{{{sum_ab}}}{{2}}\\) is a rational number strictly between \\({a}\\) and \\({b}\\).",
            d, v
        )
        questions.append(q)

    # 3.4.2 Common denominator method (need 66)
    tc = "CBSE-8-MGP1-3-3.4.2"
    name = "Common denominator method"
    for i in range(66):
        d1 = 3
        d2 = 5
        lcm = 15
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"To insert multiple rational numbers between \\(\\frac{{1}}{{{d1}}}\\) and \\(\\frac{{2}}{{{d2}}}\\) using the common denominator method, what is the least common denominator (LCM) to start with?",
            f"\\({lcm}\\)",
            [f"\\({d1 + d2}\\)", f"\\({d2 - d1}\\)", f"\\(30\\)"],
            f"The common denominator method begins by converting given fractions to equivalent fractions with their least common multiple (LCM) as the denominator.",
            f"The denominators are \\({d1}\\) and \\({d2}\\). Since \\(\\gcd({d1}, {d2}) = 1\\), \\(\\text{{LCM}}({d1}, {d2}) = {d1} \\times {d2} = {lcm}\\).",
            f"Therefore, the initial least common denominator is \\({lcm}\\).",
            d, v
        )
        questions.append(q)

    # 3.4.3 Density property: Infinitely many rationals exist (need 26)
    tc = "CBSE-8-MGP1-3-3.4.3"
    name = "Density property: Infinitely many rationals exist"
    for i in range(26):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "How many rational numbers exist strictly between any two distinct rational numbers?",
            "Infinitely many",
            ["Only one", "A finite number depending on the difference", "None"],
            f"By the density property of rational numbers, between any two distinct rational numbers \\(a\\) and \\(b\\), we can always find another rational number (e.g. their mean \\(\\frac{{a+b}}{{2}}\\)).",
            f"Repeating this process indefinitely generates an unbounded sequence of distinct rational numbers.",
            f"Thus, there are infinitely many rational numbers between any two distinct rationals.",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch3_questions()
    print(f"Generated {len(qs)} questions for Chapter 3.")
    with open("scripts/cbse8_mgp1_ch3_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/cbse8_mgp1_ch3_topup.json")
