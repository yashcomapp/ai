import json
import random
import math

random.seed(8101)

def build_ch1_questions():
    questions = []
    start_seq = 300

    def make_q(topic_code, subtopic_name, text, correct, wrongs, step1, step2, step3, diff="medium", vault="exam"):
        nonlocal start_seq
        # Ensure strictly 4 unique options
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

    # 1.1.1 Ending digits of square numbers (need 19)
    tc = "CBSE-8-MGP1-1-1.1.1"
    name = "Ending digits of square numbers"
    numbers = [23, 47, 88, 102, 125, 236, 349, 414, 551, 672, 783, 897, 918, 1024, 1239, 1455, 1686, 1781, 1990]
    for i, num in enumerate(numbers[:19]):
        unit = num % 10
        sq_unit = (unit * unit) % 10
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"What is the units digit of the square of the number \\({num}\\)?",
            f"\\({sq_unit}\\)",
            [f"\\({(sq_unit + 2) % 10}\\)", f"\\({(sq_unit + 5) % 10}\\)", f"\\({(sq_unit + 7) % 10}\\)"],
            f"The units digit of \\({num}\\) is \\({unit}\\).",
            f"Squaring the units digit gives \\({unit}^2 = {unit*unit}\\), which ends in \\({sq_unit}\\).",
            f"Therefore, the units digit of \\({num}^2\\) is \\({sq_unit}\\).",
            d, v
        )
        questions.append(q)

    # 1.1.2 Zeros at the end of squares (need 71)
    tc = "CBSE-8-MGP1-1-1.1.2"
    name = "Zeros at the end of squares"
    for i in range(71):
        k = (i % 5) + 1
        base = random.randint(2, 15) * (10 ** k)
        zeros = k
        sq_zeros = 2 * k
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"How many trailing zeros are there in the square of \\({base}\\)?",
            f"\\({sq_zeros}\\)",
            [f"\\({zeros}\\)", f"\\({sq_zeros + 1}\\)", f"\\({sq_zeros - 1}\\)"],
            f"The number \\({base}\\) has \\({zeros}\\) trailing zero(s).",
            f"When any integer with \\(k\\) trailing zeros is squared, the square has \\(2k\\) trailing zeros: \\(2 \\times {zeros} = {sq_zeros}\\).",
            f"Thus, the square contains exactly \\({sq_zeros}\\) trailing zeros.",
            d, v
        )
        questions.append(q)

    # 1.1.3 Squares of even and odd numbers (need 68)
    tc = "CBSE-8-MGP1-1-1.1.3"
    name = "Squares of even and odd numbers"
    for i in range(68):
        val = 13 + i * 4 + (i % 2)
        is_even = (val % 2 == 0)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        parity = "even" if is_even else "odd"
        opp_parity = "odd" if is_even else "even"
        q = make_q(
            tc, name,
            f"Determine whether the square of \\({val}\\) is an even number or an odd number, and identify the fundamental reason.",
            f"The square is {parity}, because the square of an {parity} number is always {parity}.",
            [
                f"The square is {opp_parity}, because squaring flips parity.",
                f"The square is {opp_parity}, because all squares ending in {val%10} are {opp_parity}.",
                f"The parity depends on whether \\({val}\\) is prime."
            ],
            f"The given number is \\({val}\\), which is an {parity} integer.",
            f"By algebraic definition, the square of any {parity} integer \\((2k{' ' if is_even else '+1'})^2\\) produces an {parity} integer.",
            f"Hence, \\({val}^2\\) is {parity}.",
            d, v
        )
        questions.append(q)

    # 1.2.1 Sum of consecutive odd numbers (need 51)
    tc = "CBSE-8-MGP1-1-1.2.1"
    name = "Sum of consecutive odd numbers"
    for i in range(51):
        n = 4 + (i % 25)
        sum_odd = n * n
        odds_str = " + ".join(str(2 * k + 1) for k in range(min(n, 5)))
        if n > 5:
            odds_str += f" + \\dots + {2*n - 1}"
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"What is the sum of the first \\({n}\\) consecutive odd natural numbers: \\({odds_str}\\)?",
            f"\\({sum_odd}\\)",
            [f"\\({sum_odd - 2*n}\\)", f"\\({sum_odd + 2*n}\\)", f"\\({n * (n + 1)}\\)"],
            f"Recall the theorem: the sum of the first \\(n\\) consecutive odd natural numbers is given by \\(n^2\\).",
            f"Here, \\(n = {n}\\). Therefore, the sum is \\({n}^2 = {sum_odd}\\).",
            f"Hence, the value of the given summation is \\({sum_odd}\\).",
            d, v
        )
        questions.append(q)

    # 1.2.2 Non-square numbers between consecutive squares (need 49)
    tc = "CBSE-8-MGP1-1-1.2.2"
    name = "Non-square numbers between consecutive squares"
    for i in range(49):
        n = 10 + i
        non_sq = 2 * n
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"How many non-perfect square natural numbers lie strictly between \\({n}^2\\) and \\(({n+1})^2\\)?",
            f"\\({non_sq}\\)",
            [f"\\({non_sq + 1}\\)", f"\\({non_sq - 1}\\)", f"\\({2 * n + 2}\\)"],
            f"Between consecutive squares \\(n^2\\) and \\((n+1)^2\\), the count of non-square integers is \\(2n\\).",
            f"Here \\(n = {n}\\). Thus, the count is \\(2 \\times {n} = {non_sq}\\).",
            f"Hence, there are exactly \\({non_sq}\\) non-square numbers between \\({n}^2\\) and \\(({n+1})^2\\).",
            d, v
        )
        questions.append(q)

    # 1.2.3 Pythagorean triplets formula (2m, m²-1, m²+1) (need 58)
    tc = "CBSE-8-MGP1-1-1.2.3"
    name = "Pythagorean triplets formula (2m, m²-1, m²+1)"
    for i in range(58):
        m = 3 + (i % 20)
        a = 2 * m
        b = m * m - 1
        c = m * m + 1
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Using the Pythagorean triplet formula \\((2m, m^2-1, m^2+1)\\), find the other two members of the triplet if the smallest member is \\({a}\\).",
            f"\\({b}\\) and \\({c}\\)",
            [f"\\({b-2}\\) and \\({c+1}\\)", f"\\({b+2}\\) and \\({c+3}\\)", f"\\({m^2}\\) and \\({m^2+2}\\)"],
            f"Given the smallest member is \\(2m = {a}\\), we solve for \\(m\\): \\(m = {m}\\).",
            f"Calculate the second member: \\(m^2 - 1 = {m}^2 - 1 = {b}\\). Calculate the third member: \\(m^2 + 1 = {m}^2 + 1 = {c}\\).",
            f"Thus, the complete Pythagorean triplet is \\(({a}, {b}, {c})\\).",
            d, v
        )
        questions.append(q)

    # 1.3.1 Square root as inverse of squaring (need 48)
    tc = "CBSE-8-MGP1-1-1.3.1"
    name = "Square root as inverse of squaring"
    for i in range(48):
        root = 12 + i
        sq = root * root
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"If \\({root}^2 = {sq}\\), what is the value of \\(\\sqrt{{{sq}}}\\)?",
            f"\\({root}\\)",
            [f"\\({root + 2}\\)", f"\\({root - 2}\\)", f"\\({sq // 2}\\)"],
            f"Squaring an integer \\(x\\) yields \\(x^2\\). The square root operation \\(\\sqrt{{x}}\\) is the inverse operation of squaring.",
            f"Since \\({root}^2 = {sq}\\), taking the principal square root gives \\(\\sqrt{{{sq}}} = {root}\\).",
            f"Therefore, \\(\\sqrt{{{sq}}} = {root}\\).",
            d, v
        )
        questions.append(q)

    # 1.3.2 Prime factor pairing (need 60)
    tc = "CBSE-8-MGP1-1-1.3.2"
    name = "Prime factor pairing"
    for i in range(60):
        p1 = [2, 3, 5, 7][i % 4]
        p2 = [3, 5, 7, 11][(i + 1) % 4]
        if p1 == p2:
            p2 = 13
        root = p1 * p2
        sq = root * root
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find the square root of \\({sq}\\) by prime factorisation.",
            f"\\({root}\\)",
            [f"\\({root + p1}\\)", f"\\({root - p1}\\)", f"\\({p1 * p2 * 2}\\)"],
            f"Express \\({sq}\\) as a product of prime factors: \\({sq} = {p1}^2 \\times {p2}^2\\).",
            f"Pair the prime factors: \\(({p1} \\times {p1}) \\times ({p2} \\times {p2})\\). Take one factor from each pair: \\({p1} \\times {p2} = {root}\\).",
            f"Therefore, \\(\\sqrt{{{sq}}} = {root}\\).",
            d, v
        )
        questions.append(q)

    # 1.3.3 Smallest multiplier or divisor to get perfect square (need 50)
    tc = "CBSE-8-MGP1-1-1.3.3"
    name = "Smallest multiplier or divisor to get perfect square"
    for i in range(50):
        mult = [2, 3, 5, 7][i % 4]
        base = 6 + (i % 10)
        num = (base * base) * mult
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find the smallest natural number by which \\({num}\\) must be multiplied so that the product becomes a perfect square.",
            f"\\({mult}\\)",
            [f"\\({mult + 1}\\)", f"\\({mult + 2}\\)", f"\\({mult * 2}\\)"],
            f"Determine the prime factorisation of \\({num}\\): it contains an un-paired factor of \\({mult}\\).",
            f"To make all prime factors form complete pairs, we must multiply by \\({mult}\\).",
            f"Hence, the smallest required multiplier is \\({mult}\\).",
            d, v
        )
        questions.append(q)

    # 1.4.1 Long division algorithm (need 64)
    tc = "CBSE-8-MGP1-1-1.4.1"
    name = "Long division algorithm"
    for i in range(64):
        val = 25 + i
        sq = val * val
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find the square root of \\({sq}\\) using the long division method.",
            f"\\({val}\\)",
            [f"\\({val + 2}\\)", f"\\({val - 2}\\)", f"\\({val + 10}\\)"],
            f"Group the digits of \\({sq}\\) in pairs from right to left.",
            f"Execute the division algorithm: find the largest integer whose square is less than or equal to the leftmost period, double the quotient for subsequent trial divisors.",
            f"The quotient obtained without any remainder is \\({val}\\). Hence, \\(\\sqrt{{{sq}}} = {val}\\).",
            d, v
        )
        questions.append(q)

    # 1.4.2 Square roots of decimals (need 26)
    tc = "CBSE-8-MGP1-1-1.4.2"
    name = "Square roots of decimals"
    for i in range(26):
        int_root = 12 + i
        root_dec = int_root / 10.0
        sq_dec = round(root_dec * root_dec, 2)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Evaluate the square root of the decimal number \\({sq_dec}\\).",
            f"\\({root_dec}\\)",
            [f"\\({round(root_dec + 0.2, 2)}\\)", f"\\({round(root_dec - 0.2, 2)}\\)", f"\\({round(root_dec * 10, 2)}\\)"],
            f"Convert the decimal to a vulgar fraction: \\({sq_dec} = \\frac{{{int_root**2}}}{{100}}\\).",
            f"Apply the quotient rule of radicals: \\(\\sqrt{{\\frac{{{int_root**2}}}{{100}}}} = \\frac{{\\sqrt{{{int_root**2}}}}}{{\\sqrt{{100}}}} = \\frac{{{int_root}}}{{10}} = {root_dec}\\).",
            f"Therefore, \\(\\sqrt{{{sq_dec}}} = {root_dec}\\).",
            d, v
        )
        questions.append(q)

    # 1.4.3 Estimating square roots in word problems (need 68)
    tc = "CBSE-8-MGP1-1-1.4.3"
    name = "Estimating square roots in word problems"
    for i in range(68):
        root = 15 + (i % 25)
        area = root * root
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"A square field has an area of \\({area}\\text{{ m}}^2\\). A gardener wants to plant a fence along one complete side. What is the side length of the field?",
            f"\\({root}\\text{{ m}}\\)",
            [f"\\({root + 4}\\text{{ m}}\\)", f"\\({root - 4}\\text{{ m}}\\)", f"\\({area // 2}\\text{{ m}}\\)"],
            f"The area of a square is given by \\(\\text{{Area}} = \\text{{side}}^2\\). Here \\(\\text{{side}}^2 = {area}\\).",
            f"Take the square root of both sides: \\(\\text{{side}} = \\sqrt{{{area}}} = {root}\\text{{ m}}\\).",
            f"Therefore, the side length of the field is \\({root}\\text{{ m}}\\).",
            d, v
        )
        questions.append(q)

    # 1.5.1 Cube numbers definition (need 25)
    tc = "CBSE-8-MGP1-1-1.5.1"
    name = "Cube numbers definition"
    for i in range(25):
        n = 3 + i
        cube = n ** 3
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"What is the cube of \\({n}\\)?",
            f"\\({cube}\\)",
            [f"\\({cube + 3*n}\\)", f"\\({cube - 3*n}\\)", f"\\({n * 3}\\)"],
            f"A cube of a number \\(n\\) is obtained by multiplying the number by itself three times: \\(n^3 = n \\times n \\times n\\).",
            f"Substitute \\(n = {n}\\): \\({n}^3 = {n} \\times {n} \\times {n} = {cube}\\).",
            f"Therefore, \\({n}^3 = {cube}\\).",
            d, v
        )
        questions.append(q)

    # 1.5.2 Adding consecutive odd numbers for cubes (need 66)
    tc = "CBSE-8-MGP1-1-1.5.2"
    name = "Adding consecutive odd numbers for cubes"
    for i in range(66):
        n = 2 + (i % 12)
        cube = n ** 3
        first_odd = n * (n - 1) + 1
        last_odd = first_odd + 2 * (n - 1)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"To express \\({n}^3\\) as the sum of \\({n}\\) consecutive odd numbers, what is the starting (first) odd number in the sequence?",
            f"\\({first_odd}\\)",
            [f"\\({first_odd + 2}\\)", f"\\({first_odd - 2}\\)", f"\\({2 * n + 1}\\)"],
            f"The \\(n\\) consecutive odd numbers whose sum is \\(n^3\\) start at \\(n(n-1) + 1\\).",
            f"Substituting \\(n = {n}\\): \\({n}({n}-1) + 1 = {n}({n-1}) + 1 = {first_odd}\\).",
            f"Thus, the first odd number in the sequence is \\({first_odd}\\).",
            d, v
        )
        questions.append(q)

    # 1.5.3 Prime factorisation of cubes (need 67)
    tc = "CBSE-8-MGP1-1-1.5.3"
    name = "Prime factorisation of cubes"
    for i in range(67):
        p = [2, 3, 5][i % 3]
        mult = 2 + (i % 6)
        cube_base = p * mult
        cube = cube_base ** 3
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"In the prime factorisation of a perfect cube \\({cube}\\), each distinct prime factor must appear in groups of:",
            "triplets (groups of 3)",
            ["pairs (groups of 2)", "quadruplets (groups of 4)", "any multiple of 5"],
            f"By the Fundamental Theorem of Arithmetic, if a number is a perfect cube \\(N = k^3\\), every prime exponent in its prime factorisation must be a multiple of 3.",
            f"Hence, all prime factors must group into exact triplets.",
            f"Therefore, each prime factor appears in triplets (groups of 3).",
            d, v
        )
        questions.append(q)

    # 1.6.1 Cube root symbol and definition (need 29)
    tc = "CBSE-8-MGP1-1-1.6.1"
    name = "Cube root symbol and definition"
    for i in range(29):
        root = 4 + i
        cube = root ** 3
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Evaluate the cube root expression: \\(\\sqrt[3]{{{cube}}}\\).",
            f"\\({root}\\)",
            [f"\\({root + 2}\\)", f"\\({root - 2}\\)", f"\\({cube // 3}\\)"],
            f"The symbol \\(\\sqrt[3]{{x}}\\) denotes the principal cube root of \\(x\\).",
            f"Since \\({root}^3 = {cube}\\), it follows directly that \\(\\sqrt[3]{{{cube}}} = {root}\\).",
            f"Therefore, \\(\\sqrt[3]{{{cube}}} = {root}\\).",
            d, v
        )
        questions.append(q)

    # 1.6.2 Triplets of prime factors (need 64)
    tc = "CBSE-8-MGP1-1-1.6.2"
    name = "Triplets of prime factors"
    for i in range(64):
        p1 = [2, 3, 5][i % 3]
        p2 = [3, 5, 7][(i + 1) % 3]
        if p1 == p2:
            p2 = 11
        root = p1 * p2
        cube = root ** 3
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find the cube root of \\({cube}\\) by prime factorisation.",
            f"\\({root}\\)",
            [f"\\({root + p1}\\)", f"\\({root - p1}\\)", f"\\({root * 2}\\)"],
            f"Write the prime factorisation of \\({cube}\\): \\({cube} = {p1}^3 \\times {p2}^3\\).",
            f"Form triplets of equal factors: \\(({p1} \\times {p1} \\times {p1}) \\times ({p2} \\times {p2} \\times {p2})\\). Take one prime from each triplet: \\({p1} \\times {p2} = {root}\\).",
            f"Thus, \\(\\sqrt[3]{{{cube}}} = {root}\\).",
            d, v
        )
        questions.append(q)

    # 1.6.3 Estimation method for cube roots (need 65)
    tc = "CBSE-8-MGP1-1-1.6.3"
    name = "Estimation method for cube roots"
    for i in range(65):
        ten_digit = 1 + (i % 6)
        unit_digit = [1, 2, 3, 4, 5, 6, 7, 8, 9][(i * 3) % 9]
        root = ten_digit * 10 + unit_digit
        cube = root ** 3
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Using the estimation method (grouping by 3 digits from right), find the cube root of \\({cube}\\).",
            f"\\({root}\\)",
            [f"\\({root + 2}\\)", f"\\({root - 2}\\)", f"\\({root + 10}\\)"],
            f"Divide \\({cube}\\) into two groups from right to left: units group and remaining thousands group.",
            f"The units digit of \\({cube}\\) determines the units digit of the cube root (\\({unit_digit}\\)). The remaining group falls between \\({ten_digit}^3\\) and \\({ten_digit+1}^3\\), giving tens digit \\({ten_digit}\\).",
            f"Combining both digits gives the cube root: \\({root}\\).",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch1_questions()
    print(f"Generated {len(qs)} questions for Chapter 1.")
    with open("scripts/cbse8_mgp1_ch1_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/cbse8_mgp1_ch1_topup.json")
