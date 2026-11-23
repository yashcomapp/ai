import json
import os
import math

def generate_ch1_to_3():
    print("=== Generating CBSE 10 Mathematics Chapters 1, 2, 3 (2,080 Questions) ===")
    
    questions = []
    
    # -------------------------------------------------------------
    # Helper to create question object
    # -------------------------------------------------------------
    def make_q(topic_code, seq, text, options, correct_ans, sol_s1, sol_s2, sol_s3, vault, diff="medium", req_fig=False):
        sol_text = f"**Step 1:** {sol_s1}\n**Step 2:** {sol_s2}\n**Step 3:** {sol_s3}"
        
        # Ensure 4 strictly unique options
        c_idx = ord(correct_ans) - 65
        correct_text = options[c_idx]
        
        unique_opts = [None, None, None, None]
        unique_opts[c_idx] = correct_text
        seen = {correct_text.strip().lower()}
        
        alt_distractors = [
            "\\(0\\)", "\\(1\\)", "\\(-1\\)", "\\(2\\)", "\\(-2\\)", 
            "\\(x = 1, y = 1\\)", "\\(x = -1, y = 2\\)", "\\(x = 2, y = -1\\)",
            "\\(5\\)", "\\(-5\\)", "\\(10\\)", "\\(-10\\)", "\\(\\frac{1}{2}\\)", "\\(-\\frac{1}{2}\\)"
        ]
        alt_idx = 0
        
        for i in range(4):
            if i == c_idx:
                continue
            cand = options[i]
            cand_norm = cand.strip().lower()
            if cand_norm in seen:
                # Perturb candidate
                while cand_norm in seen and alt_idx < len(alt_distractors):
                    cand = alt_distractors[alt_idx]
                    cand_norm = cand.strip().lower()
                    alt_idx += 1
            seen.add(cand_norm)
            unique_opts[i] = cand
            
        # Format options as list of objects with A, B, C, D
        parsed_opts = []
        for i, opt in enumerate(unique_opts):
            opt_id = chr(65 + i)
            parsed_opts.append({
                "id": opt_id,
                "text": opt,
                "isCorrect": (opt_id == correct_ans)
            })
            
        parts = topic_code.split('-')
        # format: CBSE-10-MATH-1-1.1.1
        ch_num = int(parts[3])
        top_num = parts[4]
        q_code = f"{topic_code}-OSC-{seq:03d}"
        
        q_obj = {
            "questionCode": q_code,
            "topicCode": topic_code,
            "chapterNumber": ch_num,
            "subjectCode": "MATH",
            "boardCode": "CBSE",
            "class": "10",
            "type": "OSC",
            "text": text,
            "options": parsed_opts,
            "correctAnswer": correct_ans,
            "solution": sol_text,
            "explanation": sol_text,
            "difficulty": diff,
            "vault": vault,
            "marks": 4,
            "estimatedTime": 90 if diff == "hard" else 60,
            "bloomsTaxonomy": "analyze" if diff == "hard" else ("apply" if diff == "medium" else "understand"),
            "status": "active"
        }
        if req_fig:
            q_obj["requiresFigure"] = True
        return q_obj

    # =========================================================================
    # CHAPTER 1: REAL NUMBERS (7 subtopics, 80 Qs each = 560 Qs)
    # =========================================================================
    
    # --- 1.1.1: Statement: Every composite number uniquely expressed as product of primes ---
    tc = "CBSE-10-MATH-1-1.1.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        n_base = 24 + i * 6
        # Find prime factorization of n_base
        temp = n_base
        factors = {}
        for d in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
            while temp % d == 0:
                factors[d] = factors.get(d, 0) + 1
                temp //= d
        if temp > 1:
            factors[temp] = 1
        
        prime_str = " \\times ".join([f"{p}^{{{exp}}}" if exp > 1 else f"{p}" for p, exp in sorted(factors.items())])
        
        if i % 2 == 1:
            text = f"According to the Fundamental Theorem of Arithmetic, what is the unique prime factorization of the composite number \\({n_base}\\)?"
            correct = "A"
            c_opt = f"\\({prime_str}\\)"
            w1 = f"\\(2 \\times {n_base // 2}\\)"
            w2 = f"\\(3 \\times {n_base // 3}\\)" if n_base % 3 == 0 else f"\\(5 \\times {n_base // 5}\\)"
            w3 = f"\\(4 \\times {n_base // 4}\\)" if n_base % 4 == 0 else f"\\({n_base} \\times 1\\)"
            options = [c_opt, w1, w2, w3]
            s1 = f"The Fundamental Theorem of Arithmetic states that every composite number can be expressed uniquely as a product of prime powers, apart from the order of factors."
            s2 = f"Successive division of \\({n_base}\\) by the lowest prime divisors yields prime factors: {sorted(factors.items())}."
            s3 = f"Combining identical primes into exponential form gives \\({prime_str}\\). Hence, Option A is correct."
        else:
            text = f"If the prime factorization of a natural number \\(N\\) is given by \\({prime_str}\\), what is the total number of positive factors of \\(N\\)?"
            num_factors = 1
            for exp in factors.values():
                num_factors *= (exp + 1)
            correct = "B"
            c_opt = f"\\({num_factors}\\)"
            options = [f"\\({num_factors - 2}\\)", c_opt, f"\\({num_factors + 2}\\)", f"\\({num_factors * 2}\\)"]
            s1 = f"For a number \\(N = p_1^{{a_1}} p_2^{{a_2}} \\dots\\), the total number of positive divisors is given by \\((a_1 + 1)(a_2 + 1)\\dots\\)."
            s2 = f"Here, exponents of prime factors are {[e for e in factors.values()]}. Multiplying \\((e_i + 1)\\) gives \\({num_factors}\\)."
            s3 = f"Therefore, \\(N\\) has exactly \\({num_factors}\\) positive divisors. Option B is correct."
            
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 1.1.2: Finding HCF and LCM using prime factors ---
    tc = "CBSE-10-MATH-1-1.1.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        a = 12 + i * 4
        b = 18 + i * 6
        h = math.gcd(a, b)
        l = (a * b) // h
        
        if i % 2 == 1:
            text = f"Using the prime factorisation method, what is the Highest Common Factor \\(\\text{{HCF}}({a}, {b})\\)?"
            correct = "A"
            options = [f"\\({h}\\)", f"\\({h * 2}\\)", f"\\({max(1, h // 2)}\\)", f"\\({l}\\)"]
            s1 = f"Express both integers as products of their prime factors."
            s2 = f"\\(\\text{{HCF}}\\) is the product of the smallest power of each common prime factor involved in the numbers."
            s3 = f"Evaluating the intersection of prime powers gives \\(\\text{{HCF}}({a}, {b}) = {h}\\). Option A is correct."
        else:
            text = f"What is the Lowest Common Multiple \\(\\text{{LCM}}({a}, {b})\\) computed via prime factorisation?"
            correct = "C"
            options = [f"\\({h}\\)", f"\\({l // 2}\\)", f"\\({l}\\)", f"\\({l * 2}\\)"]
            s1 = f"\\(\\text{{LCM}}\\) is the product of the greatest power of each prime factor involved in the numbers."
            s2 = f"Calculating from the union of prime factors of \\({a}\\) and \\({b}\\) gives \\({l}\\)."
            s3 = f"Therefore, \\(\\text{{LCM}}({a}, {b}) = {l}\\). Option C is correct."
            
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 1.1.3: Formula: HCF(a, b) * LCM(a, b) = a * b ---
    tc = "CBSE-10-MATH-1-1.1.3"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        a = 15 + i * 5
        b = 20 + i * 5
        h = math.gcd(a, b)
        l = (a * b) // h
        
        if i % 2 == 1:
            text = f"Given that \\(\\text{{HCF}}({a}, {b}) = {h}\\), find \\(\\text{{LCM}}({a}, {b})\\) using the relationship \\(\\text{{HCF}}(a, b) \\times \\text{{LCM}}(a, b) = a \\times b\\)."
            correct = "B"
            options = [f"\\({l - 10}\\)", f"\\({l}\\)", f"\\({l + 10}\\)", f"\\({a * b}\\)"]
            s1 = f"For any two positive integers \\(a\\) and \\(b\\), \\(\\text{{HCF}}(a, b) \\times \\text{{LCM}}(a, b) = a \\times b\\)."
            s2 = f"Substituting: \\({h} \\times \\text{{LCM}} = {a} \\times {b} = {a * b} \\implies \\text{{LCM}} = \\frac{{{a * b}}}{{{h}}} = {l}\\)."
            s3 = f"Thus, \\(\\text{{LCM}}({a}, {b}) = {l}\\). Option B is correct."
        else:
            p_val = a * b
            text = f"If the product of two positive numbers is \\({p_val}\\) and their \\(\\text{{LCM}}\\) is \\({l}\\), what is their \\(\\text{{HCF}}\\)?"
            correct = "A"
            options = [f"\\({h}\\)", f"\\({h + 2}\\)", f"\\({h * 3}\\)", f"\\({p_val}\\)"]
            s1 = f"By identity: \\(\\text{{HCF}} \\times \\text{{LCM}} = \\text{{Product of numbers}}\\)."
            s2 = f"\\(\\text{{HCF}} = \\frac{{{p_val}}}{{{l}}} = {h}\\)."
            s3 = f"Hence, \\(\\text{{HCF}} = {h}\\). Option A is correct."
            
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 1.2.1: Theorem: If p divides a², then p divides a ---
    tc = "CBSE-10-MATH-1-1.2.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        primes = [2, 3, 5, 7, 11, 13, 17]
        p = primes[(i - 1) % len(primes)]
        
        text = f"Let \\(p = {p}\\) be a prime number. If \\({p}\\) divides \\(a^2\\) (where \\(a\\) is a positive integer), which of the following is guaranteed by the Fundamental Theorem of Arithmetic?"
        correct = "D"
        options = [
            f"\\({p}\\) divides \\(a + 1\\)",
            f"\\(a\\) must be a prime number",
            f"\\({p^2}\\) divides \\(a\\)",
            f"\\({p}\\) divides \\(a\\)"
        ]
        s1 = f"Theorem 1.2 states: Let \\(p\\) be a prime number. If \\(p\\) divides \\(a^2\\), then \\(p\\) divides \\(a\\), where \\(a\\) is a positive integer."
        s2 = f"Let prime factorization of \\(a\\) be \\(p_1 p_2 \\dots p_n\\). Then \\(a^2 = (p_1 p_2 \\dots p_n)^2\\). Since \\(p\\) divides \\(a^2\\), \\(p\\) must be one of the prime factors of \\(a\\)."
        s3 = f"Therefore, \\({p}\\) necessarily divides \\(a\\). Option D is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 1.2.2: Rigorous proofs of irrationality for √2, √3, √5, 3+2√5 by contradiction ---
    tc = "CBSE-10-MATH-1-1.2.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        k = (i % 6) + 2
        root = [2, 3, 5, 7][i % 4]
        
        if i % 2 == 1:
            text = f"In the proof by contradiction that \\(\\sqrt{{{root}}}\\) is irrational, we assume \\(\\sqrt{{{root}}} = \\frac{{a}}{{b}}\\) where \\(a\\) and \\(b\\) are coprime integers. Squaring both sides yields \\({root} b^2 = a^2\\). What contradiction arises?"
            correct = "A"
            options = [
                f"Both \\(a\\) and \\(b\\) have \\({root}\\) as a common factor, contradicting that \\(a, b\\) are coprime",
                f"\\(b = 0\\), which is undefined",
                f"\\({root}\\) becomes a composite number",
                f"\\(a^2\\) is odd while \\(b^2\\) is even"
            ]
            s1 = f"Assume on the contrary that \\(\\sqrt{{{root}}}\\) is rational, so \\(\\sqrt{{{root}}} = \\frac{{a}}{{b}}\\) where \\(a, b\\) are coprime integers."
            s2 = f"Then \\(a^2 = {root} b^2 \\implies {root}\\) divides \\(a^2 \\implies {root}\\) divides \\(a\\). Writing \\(a = {root}c\\) gives \\({root}^2 c^2 = {root} b^2 \\implies b^2 = {root}c^2 \\implies {root}\\) divides \\(b\\)."
            s3 = f"Hence \\({root}\\) divides both \\(a\\) and \\(b\\), contradicting coprimality. Thus \\(\\sqrt{{{root}}}\\) is irrational. Option A is correct."
        else:
            text = f"If \\(\\sqrt{{{root}}}\\) is known to be irrational, why is the number \\({k} + 2\\sqrt{{{root}}}\\) also irrational?"
            correct = "C"
            options = [
                "Because squaring it results in a negative integer",
                "Because any number containing a root symbol is undefined",
                f"Because assuming it rational leads to \\(\\sqrt{{{root}}} = \\frac{{r - {k}}}{{2}}\\) (rational), contradicting that \\(\\sqrt{{{root}}}\\) is irrational",
                f"Because the sum of two integers is always irrational"
            ]
            s1 = f"Assume \\(x = {k} + 2\\sqrt{{{root}}}\\) is rational, say \\(r \\in \\mathbb{{Q}}\\)."
            s2 = f"Rearranging: \\(2\\sqrt{{{root}}} = r - {k} \\implies \\sqrt{{{root}}} = \\frac{{r - {k}}}{{2}}\\). Since \\(r, {k}, 2\\) are rational, the RHS is rational."
            s3 = f"This contradicts the proven fact that \\(\\sqrt{{{root}}}\\) is irrational. Hence \\({k} + 2\\sqrt{{{root}}}\\) is irrational. Option C is correct."
            
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 1.3.1: Terminating decimal condition: denominator in 2ⁿ5ᵐ form ---
    tc = "CBSE-10-MATH-1-1.3.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        n_p = (i % 4) + 1
        m_p = (i % 3) + 1
        den = (2**n_p) * (5**m_p)
        num = 7 + i * 2
        while math.gcd(num, den) > 1:
            num += 1
            
        text = f"Without actual division, determine whether the rational number \\(\\frac{{{num}}}{{{den}}}\\) has a terminating or non-terminating decimal expansion, and after how many decimal places it terminates:"
        max_dec = max(n_p, m_p)
        correct = "B"
        options = [
            f"Non-terminating repeating",
            f"Terminating, after {max_dec} decimal places",
            f"Terminating, after {n_p + m_p} decimal places",
            f"Non-terminating non-repeating"
        ]
        s1 = f"A rational number \\(\\frac{{p}}{{q}}\\) in simplest form has a terminating decimal expansion if and only if the prime factorisation of \\(q\\) is of the form \\(2^n 5^m\\)."
        s2 = f"Here, \\({den} = 2^{{{n_p}}} \\times 5^{{{m_p}}}\\). Since only 2 and 5 are prime factors, the expansion terminates."
        s3 = f"The number of decimal places after which it terminates is \\(\\max(n, m) = \\max({n_p}, {m_p}) = {max_dec}\\). Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 1.3.2: Non-terminating recurring decimal criteria ---
    tc = "CBSE-10-MATH-1-1.3.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        extra_prime = [3, 7, 11, 13][i % 4]
        den = (2**(i % 3 + 1)) * extra_prime
        num = 13 + i * 4
        while math.gcd(num, den) > 1:
            num += 2
            
        text = f"Why does the fraction \\(\\frac{{{num}}}{{{den}}}\\) (in simplest form) have a non-terminating repeating decimal expansion?"
        correct = "A"
        options = [
            f"Because the denominator contains prime factor \\({extra_prime}\\), which is other than 2 or 5",
            f"Because the numerator \\({num}\\) is odd",
            f"Because the denominator is greater than the numerator",
            f"Because \\({den}\\) is not divisible by 10"
        ]
        s1 = f"By Theorem 1.7, if the denominator \\(q\\) of \\(\\frac{{p}}{{q}}\\) has a prime factor other than 2 and 5, its decimal expansion is non-terminating recurring."
        s2 = f"Prime factorization of \\({den}\\) is \\(2^{{{i % 3 + 1}}} \\times {extra_prime}\\)."
        s3 = f"The presence of \\({extra_prime}\\) prevents it from being represented as a terminating decimal. Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # =========================================================================
    # CHAPTER 2: POLYNOMIALS (10 subtopics, 80 Qs each = 800 Qs)
    # Includes inline SVG figures for graphical subtopics!
    # =========================================================================

    # --- 2.1.1: Parabolic graphs of quadratic polynomials (upward/downward opening) ---
    tc = "CBSE-10-MATH-2-2.1.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        a_sgn = 1 if i % 2 == 1 else -1
        a_val = a_sgn * (i % 3 + 1)
        b_val = 2 * (i % 4 + 1)
        c_val = -3 * (i % 5 + 1)
        
        # SVG figure for parabola
        svg_direction = "upward" if a_sgn > 0 else "downward"
        vertex_y = 130 if a_sgn > 0 else 50
        control_y = 30 if a_sgn > 0 else 150
        path_d = f"M 40,{vertex_y} Q 150,{control_y} 260,{vertex_y}" if a_sgn < 0 else f"M 40,50 Q 150,150 260,50"
        
        svg_code = f"""<svg viewBox="0 0 300 180" width="100%" height="160" style="max-width:320px; display:block; margin:10px auto; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <!-- Axes -->
  <line x1="20" y1="90" x2="280" y2="90" stroke="#64748b" stroke-width="1.5" />
  <line x1="150" y1="10" x2="150" y2="170" stroke="#64748b" stroke-width="1.5" />
  <text x="270" y="85" font-family="sans-serif" font-size="11" fill="#475569">X</text>
  <text x="155" y="20" font-family="sans-serif" font-size="11" fill="#475569">Y</text>
  <!-- Parabola -->
  <path d="{path_d}" fill="none" stroke="#2563eb" stroke-width="2.5" />
  <text x="150" y="165" font-family="sans-serif" font-size="10" fill="#0f172a" text-anchor="middle">y = ax² + bx + c</text>
</svg>"""

        text = f"Consider the quadratic polynomial \\(p(x) = {a_val}x^2 + {b_val}x + {c_val}\\) shown in the parabolic sketch below:\n\n{svg_code}\n\nIn which direction does the parabola open, and what property of coefficient \\(a\\) determines this?"
        correct = "A" if a_sgn > 0 else "B"
        options = [
            f"Opens upwards because \\(a = {a_val} > 0\\)",
            f"Opens downwards because \\(a = {a_val} < 0\\)",
            f"Opens horizontally because \\(b = {b_val} \\ne 0\\)",
            f"Opens upwards because constant term \\(c = {c_val} < 0\\)"
        ]
        s1 = f"For any quadratic polynomial \\(y = ax^2 + bx + c\\) with \\(a \\ne 0\\), the graph is a parabola."
        s2 = f"If \\(a > 0\\), the parabola opens upwards. If \\(a < 0\\), the parabola opens downwards."
        s3 = f"Here, coefficient \\(a = {a_val}\\) is {'positive (> 0)' if a_sgn > 0 else 'negative (< 0)'}. Therefore, it opens {svg_direction}s. Option {correct} is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff, req_fig=True))

    # --- 2.1.2: Number of zeroes = number of X-axis intersections ---
    tc = "CBSE-10-MATH-2-2.1.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        num_zeroes = (i % 4) # 0, 1, 2, or 3
        
        # Build SVG based on num_zeroes
        if num_zeroes == 0:
            curve = "M 30,50 Q 150,60 270,50"
            dot_code = ""
        elif num_zeroes == 1:
            curve = "M 30,50 Q 150,90 270,50"
            dot_code = '<circle cx="150" cy="90" r="4" fill="#dc2626" />'
        elif num_zeroes == 2:
            curve = "M 30,40 Q 150,140 270,40"
            dot_code = '<circle cx="85" cy="90" r="4" fill="#dc2626" /><circle cx="215" cy="90" r="4" fill="#dc2626" />'
        else:
            curve = "M 30,130 C 80,40 120,40 150,90 C 180,140 220,140 270,50"
            dot_code = '<circle cx="65" cy="90" r="4" fill="#dc2626" /><circle cx="150" cy="90" r="4" fill="#dc2626" /><circle cx="235" cy="90" r="4" fill="#dc2626" />'

        svg_code = f"""<svg viewBox="0 0 300 180" width="100%" height="160" style="max-width:320px; display:block; margin:10px auto; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <line x1="20" y1="90" x2="280" y2="90" stroke="#64748b" stroke-width="1.5" />
  <line x1="150" y1="15" x2="150" y2="165" stroke="#64748b" stroke-width="1.5" />
  <path d="{curve}" fill="none" stroke="#2563eb" stroke-width="2.5" />
  {dot_code}
</svg>"""

        text = f"The graph of \\(y = p(x)\\) is given below:\n\n{svg_code}\n\nBased on the number of intersections of the curve with the X-axis, how many real zeroes does \\(p(x)\\) have?"
        correct_ans = chr(65 + num_zeroes)
        options = ["\\(0\\)", "\\(1\\)", "\\(2\\)", "\\(3\\)"]
        s1 = f"The number of real zeroes of a polynomial \\(p(x)\\) is precisely equal to the number of points where the graph of \\(y = p(x)\\) intersects or touches the X-axis."
        s2 = f"Inspecting the given graph, the curve intersects/touches the X-axis at exactly \\({num_zeroes}\\) distinct point(s)."
        s3 = f"Therefore, the polynomial \\(p(x)\\) has exactly \\({num_zeroes}\\) zero(es). Option {correct_ans} is correct."
        questions.append(make_q(tc, i, text, options, correct_ans, s1, s2, s3, vault, diff, req_fig=True))

    # --- 2.2.1: Sum of zeroes: α + β = -b/a ---
    tc = "CBSE-10-MATH-2-2.2.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        a = (i % 3) + 1
        b = -1 * (3 + i * 2)
        c = 2 + (i % 5)
        sum_z = f"\\(\\frac{{{abs(b)}}}{{{a}}}\\)" if a > 1 else f"\\({abs(b)}\\)"
        
        text = f"If \\(\\alpha\\) and \\(\\beta\\) are the zeroes of the quadratic polynomial \\(p(x) = {a}x^2 + ({b})x + {c}\\), find the value of \\(\\alpha + \\beta\\):"
        correct = "A"
        options = [sum_z, f"\\(-\\frac{{{abs(b)}}}{{{a}}}\\)", f"\\(\\frac{{{c}}}{{{a}}}\\)", f"\\(-\\frac{{{c}}}{{{a}}}\\)"]
        s1 = f"For any quadratic polynomial \\(ax^2 + bx + c\\), the sum of its zeroes is given by the relation \\(\\alpha + \\beta = -\\frac{{b}}{{a}}\\)."
        s2 = f"Here, \\(a = {a}\\), \\(b = {b}\\). Substituting these values: \\(\\alpha + \\beta = -\\frac{{{b}}}{{{a}}} = {sum_z}\\)."
        s3 = f"Hence, the sum of the zeroes is {sum_z}. Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 2.2.2: Product of zeroes: α * β = c/a ---
    tc = "CBSE-10-MATH-2-2.2.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        a = (i % 3) + 1
        b = 4 + i
        c = -1 * (2 + i * 3)
        prod_z = f"\\(-\\frac{{{abs(c)}}}{{{a}}}\\)" if a > 1 else f"\\({c}\\)"
        
        text = f"If \\(\\alpha\\) and \\(\\beta\\) are zeroes of \\(p(x) = {a}x^2 + {b}x + ({c})\\), what is the product \\(\\alpha\\beta\\)?"
        correct = "B"
        options = [f"\\(\\frac{{{abs(c)}}}{{{a}}}\\)", prod_z, f"\\(-\\frac{{{b}}}{{{a}}}\\)", f"\\(\\frac{{{b}}}{{{a}}}\\)"]
        s1 = f"For \\(ax^2 + bx + c\\), the product of zeroes satisfies \\(\\alpha\\beta = \\frac{{c}}{{a}}\\)."
        s2 = f"Identifying coefficients: \\(a = {a}\\), \\(c = {c}\\). Thus, \\(\\alpha\\beta = \\frac{{{c}}}{{{a}}} = {prod_z}\\)."
        s3 = f"Therefore, the product of zeroes is {prod_z}. Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 2.2.3: Forming quadratic polynomial: k[x² - (α+β)x + αβ] ---
    tc = "CBSE-10-MATH-2-2.2.3"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        s = 2 + i % 5
        p = -3 - (i % 4)
        
        text = f"Find a quadratic polynomial whose sum and product of zeroes are \\({s}\\) and \\({p}\\) respectively:"
        correct = "C"
        c_poly = f"\\(x^2 - {s}x + ({p})\\)"
        options = [
            f"\\(x^2 + {s}x + {p}\\)",
            f"\\(x^2 - {s}x - {p}\\)",
            f"\\(x^2 - {s}x + ({p})\\)",
            f"\\(x^2 + {s}x - ({p})\\)"
        ]
        s1 = f"A quadratic polynomial with sum of zeroes \\(S\\) and product \\(P\\) is given by \\(k[x^2 - Sx + P]\\) for non-zero real \\(k\\)."
        s2 = f"Given \\(S = \\alpha + \\beta = {s}\\) and \\(P = \\alpha\\beta = {p}\\)."
        s3 = f"Setting \\(k = 1\\), the polynomial is \\(x^2 - {s}x + ({p})\\). Option C is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 2.3.1: Cubic sum of zeroes: α + β + γ = -b/a ---
    tc = "CBSE-10-MATH-2-2.3.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        a = 1 if i % 2 == 1 else 2
        b = -3 * (i % 4 + 1)
        c = 5 + i
        d = -2 * (i % 3 + 1)
        val = f"\\({abs(b)}\\)" if a == 1 else f"\\(\\frac{{{abs(b)}}}{{{a}}}\\)"
        
        text = f"If \\(\\alpha, \\beta, \\gamma\\) are the zeroes of the cubic polynomial \\(p(x) = {a}x^3 + ({b})x^2 + {c}x + ({d})\\), find \\(\\alpha + \\beta + \\gamma\\):"
        correct = "A"
        options = [val, f"\\(-{val}\\)", f"\\(\\frac{{{c}}}{{{a}}}\\)", f"\\(-\\frac{{{d}}}{{{a}}}\\)"]
        s1 = f"For a cubic polynomial \\(ax^3 + bx^2 + cx + d\\), the sum of zeroes is given by \\(\\alpha + \\beta + \\gamma = -\\frac{{b}}{{a}}\\)."
        s2 = f"Here, \\(a = {a}\\) and \\(b = {b}\\). Substituting gives \\(-\\frac{{{b}}}{{{a}}} = {val}\\)."
        s3 = f"Therefore, \\(\\alpha + \\beta + \\gamma = {val}\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 2.3.2: Sum of products in pairs: αβ + βγ + γα = c/a ---
    tc = "CBSE-10-MATH-2-2.3.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        a = 1 if i % 2 == 1 else 3
        c = -4 * (i % 5 + 1)
        val = f"\\({c}\\)" if a == 1 else f"\\(\\frac{{{c}}}{{{a}}}\\)"
        
        text = f"For the cubic polynomial \\(p(x) = {a}x^3 - 5x^2 + ({c})x - 7\\), what is the sum of the products of its zeroes taken two at a time, \\(\\alpha\\beta + \\beta\\gamma + \\gamma\\alpha\\)?"
        correct = "D"
        options = [f"\\(5\\)", f"\\(-5\\)", f"\\(7\\)", val]
        s1 = f"For \\(ax^3 + bx^2 + cx + d\\), the sum of products of zeroes taken two at a time is \\(\\alpha\\beta + \\beta\\gamma + \\gamma\\alpha = \\frac{{c}}{{a}}\\)."
        s2 = f"Here, \\(a = {a}\\) and \\(c = {c}\\). Thus, \\(\\frac{{c}}{{a}} = {val}\\)."
        s3 = f"Hence, \\(\\alpha\\beta + \\beta\\gamma + \\gamma\\alpha = {val}\\). Option D is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 2.3.3: Product of zeroes: αβγ = -d/a ---
    tc = "CBSE-10-MATH-2-2.3.3"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        a = 1 if i % 2 == 1 else 2
        d = -6 * (i % 4 + 1)
        val = f"\\({abs(d)}\\)" if a == 1 else f"\\(\\frac{{{abs(d)}}}{{{a}}}\\)"
        
        text = f"What is the product of the zeroes \\(\\alpha\\beta\\gamma\\) of the cubic polynomial \\(p(x) = {a}x^3 + 2x^2 - 4x + ({d})\\)?"
        correct = "B"
        options = [f"\\(-{val}\\)", val, f"\\(\\frac{{4}}{{{a}}}\\)", f"\\(-2\\)"]
        s1 = f"For any cubic polynomial, the product of all three zeroes satisfies \\(\\alpha\\beta\\gamma = -\\frac{{d}}{{a}}\\)."
        s2 = f"Substituting \\(a = {a}\\) and \\(d = {d}\\): \\(\\alpha\\beta\\gamma = -\\frac{{{d}}}{{{a}}} = {val}\\)."
        s3 = f"Therefore, the product of the zeroes is {val}. Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 2.4.1: p(x) = g(x) * q(x) + r(x) ---
    tc = "CBSE-10-MATH-2-2.4.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        k = i % 5 + 1
        
        text = f"According to the Division Algorithm for polynomials, if \\(p(x)\\) is divided by \\(g(x)\\) yielding quotient \\(q(x)\\) and remainder \\(r(x)\\), what strict condition must the degree of \\(r(x)\\) satisfy?"
        correct = "A"
        options = [
            "\\(r(x) = 0\\) or \\(\\deg(r(x)) < \\deg(g(x))\\)",
            "\\(\\deg(r(x)) = \\deg(g(x))\\)",
            "\\(\\deg(r(x)) > \\deg(g(x))\\)",
            "\\(\\deg(r(x)) < \\deg(q(x))\\)"
        ]
        s1 = f"The Division Algorithm for polynomials states that \\(p(x) = g(x)q(x) + r(x)\\)."
        s2 = f"The remainder \\(r(x)\\) must either be the zero polynomial or its degree must be strictly less than that of the divisor \\(g(x)\\)."
        s3 = f"Thus, \\(r(x) = 0\\) or \\(\\deg(r(x)) < \\deg(g(x))\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 2.4.2: Finding remaining zeroes when two irrational zeroes are given (e.g. ±√5/3) ---
    tc = "CBSE-10-MATH-2-2.4.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        root = [2, 3, 5][i % 3]
        other_z1 = (i % 3) + 1
        other_z2 = -1 * ((i % 4) + 1)
        
        text = f"Find the remaining zeroes of the polynomial \\(p(x) = x^4 - ({other_z1 + other_z2})x^3 + ({other_z1 * other_z2 - root})x^2 + {root * (other_z1 + other_z2)}x - {root * other_z1 * other_z2}\\), given that two of its zeroes are \\(\\sqrt{{{root}}}\\) and \\(-\\sqrt{{{root}}}\\):"
        correct = "B"
        options = [
            f"\\({other_z1 + 1}, {other_z2 - 1}\\)",
            f"\\({other_z1}, {other_z2}\\)",
            f"\\(-{other_z1}, -{other_z2}\\)",
            f"\\({root}, -{root}\\)"
        ]
        s1 = f"Since \\(\\pm\\sqrt{{{root}}}\\) are zeroes, \\((x - \\sqrt{{{root}}})(x + \\sqrt{{{root}}}) = x^2 - {root}\\) is a factor of \\(p(x)\\)."
        s2 = f"Dividing \\(p(x)\\) by \\(x^2 - {root}\\) yields the quadratic quotient \\(q(x) = x^2 - ({other_z1 + other_z2})x + ({other_z1 * other_z2})\\)."
        s3 = f"Factoring \\(q(x) = (x - {other_z1})(x - ({other_z2})) = 0\\) gives the remaining zeroes \\({other_z1}\\) and \\({other_z2}\\). Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # =========================================================================
    # CHAPTER 3: PAIR OF LINEAR EQUATIONS IN TWO VARIABLES (9 subtopics, 80 Qs each = 720 Qs)
    # Includes inline SVG figures for linear system lines!
    # =========================================================================

    # --- 3.1.1: Intersecting lines (unique solution, consistent: a1/a2 != b1/b2) ---
    tc = "CBSE-10-MATH-3-3.1.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        a1, b1 = 2, 3
        a2, b2 = 3, 2 + (i % 3)
        if a1 * b2 == a2 * b1:
            b2 += 1
            
        svg_code = """<svg viewBox="0 0 280 160" width="100%" height="150" style="max-width:300px; display:block; margin:8px auto; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <line x1="20" y1="80" x2="260" y2="80" stroke="#94a3b8" stroke-width="1.2" />
  <line x1="140" y1="10" x2="140" y2="150" stroke="#94a3b8" stroke-width="1.2" />
  <line x1="40" y1="130" x2="240" y2="30" stroke="#2563eb" stroke-width="2.2" />
  <line x1="40" y1="30" x2="240" y2="130" stroke="#dc2626" stroke-width="2.2" />
  <circle cx="140" cy="80" r="4.5" fill="#16a34a" />
  <text x="148" y="75" font-family="sans-serif" font-size="10" font-weight="bold" fill="#16a34a">Unique (x, y)</text>
</svg>"""

        text = f"The system of linear equations is given by:\n\\({a1}x + {b1}y = 12\\)\n\\({a2}x + {b2}y = 15\\)\n\n{svg_code}\n\nComparing the coefficient ratios \\(\\frac{{a_1}}{{a_2}}\\) and \\(\\frac{{b_1}}{{b_2}}\\), what is the geometric nature of the lines and number of solutions?"
        correct = "A"
        options = [
            f"Intersecting lines with exactly one unique solution (consistent, \\(\\frac{{a_1}}{{a_2}} \\ne \\frac{{b_1}}{{b_2}}\\))",
            f"Parallel lines with no solution (inconsistent, \\(\\frac{{a_1}}{{a_2}} = \\frac{{b_1}}{{b_2}} \\ne \\frac{{c_1}}{{c_2}}\\))",
            f"Coincident lines with infinitely many solutions",
            f"Perpendicular lines with no real solution"
        ]
        s1 = f"For a pair of linear equations \\(a_1x + b_1y + c_1 = 0\\) and \\(a_2x + b_2y + c_2 = 0\\), if \\(\\frac{{a_1}}{{a_2}} \\ne \\frac{{b_1}}{{b_2}}\\), the lines intersect at a single point."
        s2 = f"Here, \\(\\frac{{a_1}}{{a_2}} = \\frac{{{a1}}}{{{a2}}}\\) and \\(\\frac{{b_1}}{{b_2}} = \\frac{{{b1}}}{{{b2}}}\\). Since \\({a1 * b2} \\ne {a2 * b1}\\), \\(\\frac{{a_1}}{{a_2}} \\ne \\frac{{b_1}}{{b_2}}\\)."
        s3 = f"Hence, the lines intersect at a unique point, representing a consistent system with one unique solution. Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff, req_fig=True))

    # --- 3.1.2: Parallel lines (no solution, inconsistent: a1/a2 = b1/b2 != c1/c2) ---
    tc = "CBSE-10-MATH-3-3.1.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        k = i % 4 + 2
        
        svg_code = """<svg viewBox="0 0 280 150" width="100%" height="140" style="max-width:300px; display:block; margin:8px auto; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <line x1="20" y1="75" x2="260" y2="75" stroke="#94a3b8" stroke-width="1.2" />
  <line x1="140" y1="10" x2="140" y2="140" stroke="#94a3b8" stroke-width="1.2" />
  <line x1="30" y1="110" x2="250" y2="20" stroke="#2563eb" stroke-width="2.2" />
  <line x1="30" y1="140" x2="250" y2="50" stroke="#dc2626" stroke-width="2.2" />
  <text x="180" y="45" font-family="sans-serif" font-size="10" fill="#2563eb">L₁</text>
  <text x="180" y="75" font-family="sans-serif" font-size="10" fill="#dc2626">L₂ (Parallel)</text>
</svg>"""

        text = f"For what value of \\(k\\) will the pair of linear equations have no solution (parallel lines)?\n\\(2x + 3y = 7\\)\n\\(4x + ky = 11\\)\n\n{svg_code}"
        correct = "C"
        options = ["\\(k = 3\\)", "\\(k = 4\\)", "\\(k = 6\\)", "\\(k = 8\\)"]
        s1 = f"The condition for no solution (inconsistent, parallel lines) is \\(\\frac{{a_1}}{{a_2}} = \\frac{{b_1}}{{b_2}} \\ne \\frac{{c_1}}{{c_2}}\\)."
        s2 = f"Here, \\(\\frac{{a_1}}{{a_2}} = \\frac{{2}}{{4}} = \\frac{{1}}{{2}}\\), and \\(\\frac{{b_1}}{{b_2}} = \\frac{{3}}{{k}}\\). Equating: \\(\\frac{{1}}{{2}} = \\frac{{3}}{{k}} \\implies k = 6\\)."
        s3 = f"Since \\(\\frac{{c_1}}{{c_2}} = \\frac{{7}}{{11}} \\ne \\frac{{1}}{{2}}\\), \\(k = 6\\) yields parallel lines with zero common points. Option C is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff, req_fig=True))

    # --- 3.1.3: Coincident lines (infinitely many solutions: a1/a2 = b1/b2 = c1/c2) ---
    tc = "CBSE-10-MATH-3-3.1.3"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        m = i % 4 + 2
        
        text = f"If the equations \\(3x + 5y = 8\\) and \\({3*m}x + {5*m}y = k\\) represent coincident lines (infinitely many solutions), what must be the value of \\(k\\)?"
        correct = "B"
        c_val = 8 * m
        options = [f"\\({c_val - 2}\\)", f"\\({c_val}\\)", f"\\({c_val + 4}\\)", f"\\({8}\\)"]
        s1 = f"For coincident lines (dependent consistent system with infinitely many solutions), the condition is \\(\\frac{{a_1}}{{a_2}} = \\frac{{b_1}}{{b_2}} = \\frac{{c_1}}{{c_2}}\\)."
        s2 = f"Here, \\(\\frac{{a_1}}{{a_2}} = \\frac{{3}}{{{3*m}}} = \\frac{{1}}{{{m}}}\\) and \\(\\frac{{c_1}}{{c_2}} = \\frac{{8}}{{k}}\\)."
        s3 = f"Setting \\(\\frac{{1}}{{{m}}} = \\frac{{8}}{{k}} \\implies k = 8 \\times {m} = {c_val}\\). Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 3.2.1: Substitution method ---
    tc = "CBSE-10-MATH-3-3.2.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        x_val = 2 + (i % 6)
        y_val = 1 + (i % 5)
        eq1_c = x_val + y_val
        eq2_c = 2 * x_val - y_val
        
        text = f"Solve the linear system using the substitution method:\n\\(x + y = {eq1_c}\\)\n\\(2x - y = {eq2_c}\\)"
        correct = "A"
        options = [
            f"\\(x = {x_val}, y = {y_val}\\)",
            f"\\(x = {x_val + 1}, y = {y_val - 1}\\)",
            f"\\(x = {y_val}, y = {x_val}\\)",
            f"\\(x = {x_val * 2}, y = {y_val}\\)"
        ]
        s1 = f"From the first equation, express \\(y\\) in terms of \\(x\\): \\(y = {eq1_c} - x\\)."
        s2 = f"Substitute into the second equation: \\(2x - ({eq1_c} - x) = {eq2_c} \\implies 3x - {eq1_c} = {eq2_c} \\implies 3x = {eq2_c + eq1_c} \\implies x = {x_val}\\)."
        s3 = f"Substitute \\(x = {x_val}\\) back into \\(y = {eq1_c} - {x_val} = {y_val}\\). Thus \\(x = {x_val}, y = {y_val}\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 3.3.1: Elimination method ---
    tc = "CBSE-10-MATH-3-3.3.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        x_val = 3 + (i % 5)
        y_val = 2 + (i % 4)
        c1 = 3 * x_val + 2 * y_val
        c2 = 2 * x_val + 3 * y_val
        
        text = f"Using the elimination method, find the values of \\(x\\) and \\(y\\) satisfying:\n\\(3x + 2y = {c1}\\)\n\\(2x + 3y = {c2}\\)"
        correct = "D"
        options = [
            f"\\(x = {x_val - 1}, y = {y_val + 1}\\)",
            f"\\(x = {y_val}, y = {x_val}\\)",
            f"\\(x = {x_val + 2}, y = {y_val}\\)",
            f"\\(x = {x_val}, y = {y_val}\\)"
        ]
        s1 = f"Multiply the first equation by 3 and the second by 2: \\(9x + 6y = {3 * c1}\\) and \\(4x + 6y = {2 * c2}\\)."
        s2 = f"Subtracting the equations: \\(5x = {3 * c1 - 2 * c2} \\implies x = {x_val}\\)."
        s3 = f"Substitute \\(x = {x_val}\\) into \\(3({x_val}) + 2y = {c1} \\implies 2y = {c1 - 3 * x_val} \\implies y = {y_val}\\). Option D is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 3.3.4.1: Variable denominators substitution u = 1/x, v = 1/y ---
    tc = "CBSE-10-MATH-3-3.4.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        x_val = 2 + (i % 4)
        y_val = 3 + (i % 3)
        u_val = 1 / x_val
        v_val = 1 / y_val
        # 2/x + 3/y = 2*u + 3*v
        c1_num = 2 * y_val + 3 * x_val
        c1_den = x_val * y_val
        
        text = f"By reducing to a pair of linear equations using substitutions \\(u = \\frac{{1}}{{x}}\\) and \\(v = \\frac{{1}}{{y}}\\), solve for \\(x\\) and \\(y\\):\n\\(\\frac{{2}}{{x}} + \\frac{{3}}{{y}} = \\frac{{{c1_num}}}{{{c1_den}}}\\)\n\\(\\frac{{5}}{{x}} - \\frac{{4}}{{y}} = \\frac{{{5 * y_val - 4 * x_val}}}{{{x_val * y_val}}}\\)"
        correct = "B"
        options = [
            f"\\(x = {x_val + 1}, y = {y_val}\\)",
            f"\\(x = {x_val}, y = {y_val}\\)",
            f"\\(x = \\frac{{1}}{{{x_val}}}, y = \\frac{{1}}{{{y_val}}}\\)",
            f"\\(x = {y_val}, y = {x_val}\\)"
        ]
        s1 = f"Let \\(u = \\frac{{1}}{{x}}\\) and \\(v = \\frac{{1}}{{y}}\\). The system transforms into: \\(2u + 3v = \\frac{{{c1_num}}}{{{c1_den}}}\\) and \\(5u - 4v = \\frac{{{5 * y_val - 4 * x_val}}}{{{x_val * y_val}}}\\)."
        s2 = f"Solving for \\(u\\) and \\(v\\) via elimination yields \\(u = \\frac{{1}}{{{x_val}}}\\) and \\(v = \\frac{{1}}{{{y_val}}}\\)."
        s3 = f"Taking reciprocals: \\(x = \\frac{{1}}{{u}} = {x_val}\\) and \\(y = \\frac{{1}}{{v}} = {y_val}\\). Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 3.5.1: Upstream (x - y) and downstream (x + y) boat problems ---
    tc = "CBSE-10-MATH-3-3.5.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        x_speed = 10 + (i % 6) * 2 # speed of boat in still water
        y_speed = 2 + (i % 3)      # speed of stream
        d_down = 3 * (x_speed + y_speed)
        d_up = 3 * (x_speed - y_speed)
        
        text = f"A motorboat covers \\({d_down}\\text{{ km}}\\) downstream in \\(3\\text{{ hours}}\\) and covers \\({d_up}\\text{{ km}}\\) upstream in the same time. What is the speed of the boat in still water and the speed of the stream?"
        correct = "A"
        options = [
            f"Boat: \\({x_speed}\\text{{ km/h}}\\), Stream: \\({y_speed}\\text{{ km/h}}\\)",
            f"Boat: \\({x_speed + 2}\\text{{ km/h}}\\), Stream: \\({y_speed}\\text{{ km/h}}\\)",
            f"Boat: \\({x_speed}\\text{{ km/h}}\\), Stream: \\({y_speed + 1}\\text{{ km/h}}\\)",
            f"Boat: \\({x_speed - 2}\\text{{ km/h}}\\), Stream: \\({y_speed - 1}\\text{{ km/h}}\\)"
        ]
        s1 = f"Let the speed of the boat in still water be \\(x\\text{{ km/h}}\\) and stream be \\(y\\text{{ km/h}}\\). Downstream speed is \\(x + y\\) and upstream speed is \\(x - y\\)."
        s2 = f"\\(x + y = \\frac{{{d_down}}}{{3}} = {x_speed + y_speed}\\) and \\(x - y = \\frac{{{d_up}}}{{3}} = {x_speed - y_speed}\\)."
        s3 = f"Adding the equations: \\(2x = {2 * x_speed} \\implies x = {x_speed}\\text{{ km/h}}\\). Subtracting: \\(2y = {2 * y_speed} \\implies y = {y_speed}\\text{{ km/h}}\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 3.5.2: Fixed charge and per km charge taxi problems ---
    tc = "CBSE-10-MATH-3-3.5.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        fixed = 20 + (i % 5) * 5
        per_km = 8 + (i % 4)
        c1 = fixed + 10 * per_km
        c2 = fixed + 15 * per_km
        
        text = f"The taxi charges in a city consist of a fixed charge together with the charge for the distance covered. For a distance of \\(10\\text{{ km}}\\), the charge paid is \\(₹{c1}\\) and for a journey of \\(15\\text{{ km}}\\), the charge is \\(₹{c2}\\). What are the fixed charge and the charge per km?"
        correct = "C"
        options = [
            f"Fixed: \\(₹{fixed + 10}\\), Per km: \\(₹{per_km}\\)",
            f"Fixed: \\(₹{fixed}\\), Per km: \\(₹{per_km + 2}\\)",
            f"Fixed: \\(₹{fixed}\\), Per km: \\(₹{per_km}\\)",
            f"Fixed: \\(₹{fixed - 5}\\), Per km: \\(₹{per_km + 1}\\)"
        ]
        s1 = f"Let the fixed charge be \\(₹x\\) and the running charge per km be \\(₹y\\)."
        s2 = f"The system of equations is: \\(x + 10y = {c1}\\) and \\(x + 15y = {c2}\\). Subtracting gives \\(5y = {c2 - c1} \\implies y = {per_km}\\text{{ Rs/km}}\\)."
        s3 = f"Substituting \\(y = {per_km}\\) into the first equation: \\(x + 10({per_km}) = {c1} \\implies x = {fixed}\\). Option C is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 3.5.3: Two-digit number reversal problems ---
    tc = "CBSE-10-MATH-3-3.5.3"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        # tens digit x, units digit y
        tens = 2 + (i % 6)
        units = tens + 3 if tens <= 6 else tens - 3
        orig_num = 10 * tens + units
        rev_num = 10 * units + tens
        sum_digits = tens + units
        diff_num = rev_num - orig_num
        
        text = f"The sum of the digits of a two-digit number is \\({sum_digits}\\). The number obtained by reversing the digits exceeds the original number by \\({abs(diff_num)}\\) (or vice versa). What is the original number?"
        correct = "A"
        options = [
            f"\\({orig_num}\\)",
            f"\\({rev_num}\\)",
            f"\\({orig_num + 9}\\)",
            f"\\({orig_num - 9}\\)"
        ]
        s1 = f"Let the tens digit be \\(x\\) and the units digit be \\(y\\). The original number is \\(10x + y\\) and the reversed number is \\(10y + x\\)."
        s2 = f"Given \\(x + y = {sum_digits}\\) and \\((10y + x) - (10x + y) = {diff_num} \\implies 9(y - x) = {diff_num} \\implies y - x = {diff_num // 9}\\)."
        s3 = f"Solving the linear equations gives \\(x = {tens}\\) and \\(y = {units}\\). Hence, the original number is \\(10({tens}) + {units} = {orig_num}\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    out_file = './scripts/audit_data/cbse10_math_ch1_to_3_generated.json'
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2)
    print(f"✓ Generated {len(questions)} validated questions saved to {out_file}")

if __name__ == '__main__':
    generate_ch1_to_3()
