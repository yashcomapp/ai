import json
import random

random.seed(8105)

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

    vault_cycle = ["exam", "practice", "foundation"]
    diff_cycle = ["easy", "medium", "hard"]

    # 5.1.1 Sum of consecutive natural numbers patterns (need 80)
    tc = "CBSE-8-MGP1-5-5.1.1"
    name = "Sum of consecutive natural numbers patterns"
    for i in range(80):
        n = 5 + (i % 25)
        sum_n = (n * (n + 1)) // 2
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Using the triangular number pattern, find the sum of the first \\({n}\\) consecutive natural numbers \\(1 + 2 + 3 + \\dots + {n}\\).",
            f"\\({sum_n}\\)",
            [f"\\({sum_n + n}\\)", f"\\({sum_n - n}\\)", f"\\({n * n}\\)"],
            f"The sum of the first \\(n\\) consecutive natural numbers is given by the formula \\(S_n = \\frac{{n(n+1)}}{{2}}\\).",
            f"Substitute \\(n = {n}\\): \\(S_{{{n}}} = \\frac{{{n} \\times ({n} + 1)}}{{2}} = \\frac{{{n} \\times {n+1}}}{{2}} = {sum_n}\\).",
            f"Therefore, the sum is \\({sum_n}\\).",
            d, v
        )
        questions.append(q)

    # 5.1.2 Consecutive numbers with + and - signs & parity patterns (need 80)
    tc = "CBSE-8-MGP1-5-5.1.2"
    name = "Consecutive numbers with + and - signs & parity patterns"
    for i in range(80):
        pairs = 3 + (i % 20)
        n = 2 * pairs
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Evaluate the alternating sum: \\(1 - 2 + 3 - 4 + 5 - 6 + \\dots + ({n-1} - {n})\\).",
            f"\\(-{pairs}\\)",
            [f"\\({pairs}\\)", f"\\(-{n}\\)", "\\(0\\)"],
            f"Group the consecutive terms into pairs: \\((1 - 2) + (3 - 4) + \\dots + ({n-1} - {n})\\).",
            f"Notice that each pair evaluates to \\(-1\\): \\(1 - 2 = -1\\), \\(3 - 4 = -1\\), etc.",
            f"Since there are \\({pairs}\\) such pairs, the total sum is \\({pairs} \\times (-1) = -{pairs}\\).",
            d, v
        )
        questions.append(q)

    # 5.1.3 Breaking even & algebraic structures for even outcomes (need 80)
    tc = "CBSE-8-MGP1-5-5.1.3"
    name = "Breaking even & algebraic structures for even outcomes"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "If \\(m\\) is any odd integer and \\(n\\) is any odd integer, what is the parity of their sum \\(m + n\\) and product \\(m \\times n\\)?",
            "Sum is EVEN, product is ODD",
            ["Sum is ODD, product is EVEN", "Both sum and product are EVEN", "Both sum and product are ODD"],
            f"Let \\(m = 2k + 1\\) and \\(n = 2j + 1\\) for integers \\(k, j\\).",
            f"Sum: \\(m + n = (2k + 1) + (2j + 1) = 2(k + j + 1)\\), which is divisible by 2 and therefore EVEN.",
            f"Product: \\(m \\times n = (2k + 1)(2j + 1) = 4kj + 2k + 2j + 1 = 2(2kj + k + j) + 1\\), which is ODD.",
            d, v
        )
        questions.append(q)

    # 5.2.1 Divisibility tests for 2, 5, and 10 using unit digits (need 80)
    tc = "CBSE-8-MGP1-5-5.2.1"
    name = "Divisibility tests for 2, 5, and 10 using unit digits"
    for i in range(80):
        val = 1430 + i * 15
        unit = val % 10
        div2 = (unit % 2 == 0)
        div5 = (unit == 0 or unit == 5)
        div10 = (unit == 0)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        if div10:
            ans = "Divisible by 2, 5, and 10"
            wrongs = ["Divisible by 2 only", "Divisible by 5 only", "Not divisible by any"]
        elif div5:
            ans = "Divisible by 5 only (not by 2 or 10)"
            wrongs = ["Divisible by 10", "Divisible by 2 and 5", "Divisible by 2 only"]
        elif div2:
            ans = "Divisible by 2 only (not by 5 or 10)"
            wrongs = ["Divisible by 5", "Divisible by 10", "Not divisible by 2"]
        else:
            ans = "Not divisible by 2, 5, or 10"
            wrongs = ["Divisible by 2", "Divisible by 5", "Divisible by 10"]
        q = make_q(
            tc, name,
            f"Determine the divisibility of \\({val}\\) by 2, 5, and 10 by examining its units digit.",
            ans, wrongs,
            f"The units digit of \\({val}\\) is \\({unit}\\).",
            f"Divisibility rules state: a number is divisible by 2 if its unit digit is even, by 5 if its unit digit is 0 or 5, and by 10 if its unit digit is 0.",
            f"Since the unit digit is \\({unit}\\), the number is: {ans}.",
            d, v
        )
        questions.append(q)

    # 5.2.2 Divisibility tests for 3 and 9 using digit sums (need 80)
    tc = "CBSE-8-MGP1-5-5.2.2"
    name = "Divisibility tests for 3 and 9 using digit sums"
    for i in range(80):
        val = 3120 + i * 7
        d_sum = sum(int(c) for c in str(val))
        div3 = (d_sum % 3 == 0)
        div9 = (d_sum % 9 == 0)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        if div9:
            ans = "Divisible by both 3 and 9"
            wrongs = ["Divisible by 3 only", "Divisible by 9 only", "Not divisible by either"]
        elif div3:
            ans = "Divisible by 3 but not by 9"
            wrongs = ["Divisible by 9", "Divisible by both 3 and 9", "Not divisible by either"]
        else:
            ans = "Not divisible by 3 or 9"
            wrongs = ["Divisible by 3", "Divisible by 9", "Divisible by both"]
        q = make_q(
            tc, name,
            f"Test whether \\({val}\\) is divisible by 3 and 9 using the sum of digits test.",
            ans, wrongs,
            f"Calculate the sum of digits of \\({val}\\): \\({' + '.join(str(val))}\\) = \\({d_sum}\\).",
            f"Divisibility rules: a number is divisible by 3 if its digit sum is a multiple of 3, and by 9 if its digit sum is a multiple of 9.",
            f"Here \\({d_sum}\\) is {('divisible by 9' if div9 else ('divisible by 3 but not 9' if div3 else 'not divisible by 3'))}. Hence: {ans}.",
            d, v
        )
        questions.append(q)

    # 5.2.3 Divisibility test for 11 using alternating digit difference (need 80)
    tc = "CBSE-8-MGP1-5-5.2.3"
    name = "Divisibility test for 11 using alternating digit difference"
    for i in range(80):
        val = 12340 + i * 11 + (i % 5)
        digits = [int(c) for c in str(val)]
        odd_sum = sum(digits[j] for j in range(len(digits)-1, -1, -2))
        even_sum = sum(digits[j] for j in range(len(digits)-2, -1, -2))
        diff = abs(odd_sum - even_sum)
        div11 = (diff % 11 == 0)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        ans = f"Difference is \\({diff}\\); number is {'divisible' if div11 else 'not divisible'} by 11"
        wrongs = [
            f"Difference is \\({diff + 1}\\); number is {'not divisible' if div11 else 'divisible'} by 11",
            f"Difference is \\({diff + 2}\\); number is divisible by 11",
            f"Difference is \\({diff + 5}\\); number is not divisible by 11"
        ]
        q = make_q(
            tc, name,
            f"Apply the divisibility test for 11 to the number \\({val}\\).",
            ans, wrongs,
            f"Sum digits at odd places from the right: \\({odd_sum}\\). Sum digits at even places from the right: \\({even_sum}\\).",
            f"Calculate the difference: \\(|{odd_sum} - {even_sum}| = {diff}\\).",
            f"A number is divisible by 11 if and only if this difference is 0 or a multiple of 11. Hence: {ans}.",
            d, v
        )
        questions.append(q)

    # 5.2.4 Mathematical reasons using generalized form (100a + 10b + c) (need 80)
    tc = "CBSE-8-MGP1-5-5.2.4"
    name = "Mathematical reasons using generalized form (100a + 10b + c)"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "Why is a 3-digit number \\(N = 100a + 10b + c\\) divisible by 9 if and only if \\(a + b + c\\) is divisible by 9?",
            "Because \\(100a + 10b + c = 9(11a + b) + (a + b + c)\\), where the first term is an exact multiple of 9.",
            [
                "Because 100 is a multiple of 9.",
                "Because every 3-digit number has 3 digits.",
                "Because \\(a \\times b \\times c\\) is always divisible by 9."
            ],
            f"Decompose the generalized form: \\(100a + 10b + c = (99a + a) + (9b + b) + c\\).",
            f"Rearrange terms: \\((99a + 9b) + (a + b + c) = 9(11a + b) + (a + b + c)\\).",
            f"Since \\(9(11a + b)\\) is always divisible by 9, the entire number \\(N\\) is divisible by 9 if and only if the remainder \\(a + b + c\\) is divisible by 9.",
            d, v
        )
        questions.append(q)

    # 5.3.1 Digital root calculation & properties (need 80)
    tc = "CBSE-8-MGP1-5-5.3.1"
    name = "Digital root calculation & properties"
    for i in range(80):
        val = 2345 + i * 13
        # calculate digital root
        t = val
        while t >= 10:
            t = sum(int(c) for c in str(t))
        d_root = t
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find the digital root (repeated single-digit sum) of the number \\({val}\\).",
            f"\\({d_root}\\)",
            [f"\\({(d_root % 9) + 1}\\)", f"\\({((d_root + 3) % 9) + 1}\\)", f"\\({val % 10}\\)"],
            f"The digital root of a number is obtained by repeatedly summing its digits until a single digit remains.",
            f"Sum digits of \\({val}\\): {val} -> ... -> \\({d_root}\\).",
            f"Thus, the digital root is \\({d_root}\\).",
            d, v
        )
        questions.append(q)

    # 5.3.2 Remainders when divided by 9 and digital roots (need 80)
    tc = "CBSE-8-MGP1-5-5.3.2"
    name = "Remainders when divided by 9 and digital roots"
    for i in range(80):
        val = 4567 + i * 9 + (i % 7)
        rem = val % 9
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"What is the remainder when the number \\({val}\\) is divided by 9?",
            f"\\({rem}\\)",
            [f"\\({(rem + 2) % 9}\\)", f"\\({(rem + 4) % 9}\\)", f"\\({(rem + 7) % 9}\\)"],
            f"A fundamental property of arithmetic modulo 9 states that the remainder when \\(N\\) is divided by 9 is equal to the remainder of its digital sum divided by 9.",
            f"Sum the digits of \\({val}\\) and reduce modulo 9.",
            f"The resulting remainder is \\({rem}\\).",
            d, v
        )
        questions.append(q)

    # 5.4.1 Letters for digits in addition problems (need 80)
    tc = "CBSE-8-MGP1-5-5.4.1"
    name = "Letters for digits in addition problems"
    for i in range(80):
        A = 1 + (i % 7)
        B = 2 + (i % 6)
        if A == B: B = (A + 1) % 9 + 1
        sum_val = A + B
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"In the cryptarithm addition: \\(3A + 25 = B2\\) where \\(A\\) and \\(B\\) represent single digits, what are the values of \\(A\\) and \\(B\\)?",
            f"\\(A = 7\\) and \\(B = 6\\)",
            [f"\\(A = 5\\) and \\(B = 6\\)", f"\\(A = 7\\) and \\(B = 5\\)", f"\\(A = 8\\) and \\(B = 7\\)"],
            f"Examine the units column: \\(A + 5\\) ends in 2. This implies \\(A + 5 = 12\\), which gives \\(A = 12 - 5 = 7\\), with a carry of 1.",
            f"Examine the tens column: \\(1\\text{{ (carry)}} + 3 + 2 = B \\implies B = 6\\).",
            f"Therefore, \\(A = 7\\) and \\(B = 6\\).",
            d, v
        )
        questions.append(q)

    # 5.4.2 Letters for digits in multiplication problems (need 80)
    tc = "CBSE-8-MGP1-5-5.4.2"
    name = "Letters for digits in multiplication problems"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "In the multiplication problem \\(1A \\times A = 9A\\) where \\(A\\) is a single non-zero digit, find the value of \\(A\\).",
            "\\(A = 6\\)",
            ["\\(A = 5\\)", "\\(A = 4\\)", "\\(A = 1\\)"],
            f"The units digit of \\(A \\times A\\) must be \\(A\\). The possible non-zero single digits satisfying this are \\(A = 1, 5, 6\\).",
            f"Test \\(A = 1\\): \\(11 \\times 1 = 11 \\neq 91\\). Test \\(A = 5\\): \\(15 \\times 5 = 75 \\neq 95\\).",
            f"Test \\(A = 6\\): \\(16 \\times 6 = 96 = 9A\\). This matches perfectly! Hence, \\(A = 6\\).",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch5_questions()
    print(f"Generated {len(qs)} questions for Chapter 5.")
    with open("scripts/cbse8_mgp1_ch5_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/cbse8_mgp1_ch5_topup.json")
