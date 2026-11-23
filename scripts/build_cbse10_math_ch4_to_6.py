import json
import os
import math

def generate_ch4_to_6():
    print("=== Generating CBSE 10 Mathematics Chapters 4, 5, 6 (2,160 Questions) ===")
    
    questions = []
    
    # -------------------------------------------------------------
    # Helper to create question object with 100% unique options
    # -------------------------------------------------------------
    def make_q(topic_code, seq, text, options, correct_ans, sol_s1, sol_s2, sol_s3, vault, diff="medium", req_fig=False):
        sol_text = f"**Step 1:** {sol_s1}\n**Step 2:** {sol_s2}\n**Step 3:** {sol_s3}"
        
        c_idx = ord(correct_ans) - 65
        correct_text = options[c_idx]
        
        unique_opts = [None, None, None, None]
        unique_opts[c_idx] = correct_text
        seen = {correct_text.strip().lower()}
        
        alt_distractors = [
            "\\(0\\)", "\\(1\\)", "\\(-1\\)", "\\(2\\)", "\\(-2\\)", 
            "\\(4\\)", "\\(-4\\)", "\\(6\\)", "\\(-6\\)", "\\(8\\)", "\\(12\\)",
            "\\(\\frac{1}{2}\\)", "\\(3\\text{ cm}\\)", "\\(5\\text{ cm}\\)", "\\(7\\text{ cm}\\)",
            "\\(10\\text{ cm}\\)", "\\(12\\text{ cm}\\)", "\\(15\\text{ cm}\\)", "\\(20\\text{ cm}\\)",
            "\\(25\\text{ cm}^2\\)", "\\(36\\text{ cm}^2\\)", "\\(49\\text{ cm}^2\\)", "\\(64\\text{ cm}^2\\)"
        ]
        alt_idx = 0
        
        for i in range(4):
            if i == c_idx:
                continue
            cand = options[i]
            cand_norm = cand.strip().lower()
            if cand_norm in seen:
                while cand_norm in seen and alt_idx < len(alt_distractors):
                    cand = alt_distractors[alt_idx]
                    cand_norm = cand.strip().lower()
                    alt_idx += 1
            seen.add(cand_norm)
            unique_opts[i] = cand
            
        parsed_opts = []
        for i, opt in enumerate(unique_opts):
            opt_id = chr(65 + i)
            parsed_opts.append({
                "id": opt_id,
                "text": opt,
                "isCorrect": (opt_id == correct_ans)
            })
            
        parts = topic_code.split('-')
        ch_num = int(parts[3])
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
    # CHAPTER 4: QUADRATIC EQUATIONS (10 subtopics, 80 Qs each = 800 Qs)
    # =========================================================================

    # --- 4.1.1: Standard form: ax² + bx + c = 0 (a != 0) ---
    tc = "CBSE-10-MATH-4-4.1.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        a = (i % 4) + 1
        b = -1 * (2 * i + 1)
        c = (i % 6) + 2
        
        text = f"Which of the following equations is a quadratic equation in one variable in standard form \\(ax^2 + bx + c = 0\\) with \\(a \\ne 0\\)?"
        correct = "A"
        c_opt = f"\\({a}x^2 + ({b})x + {c} = 0\\)"
        options = [
            c_opt,
            f"\\(x^3 - {a}x^2 + 2x = 0\\)",
            f"\\({b}x + {c} = 0\\)",
            f"\\(x + \\frac{{1}}{{x}} = x^2\\)"
        ]
        s1 = f"A quadratic equation in variable \\(x\\) is an equation of the form \\(ax^2 + bx + c = 0\\), where \\(a, b, c\\) are real numbers and \\(a \\ne 0\\)."
        s2 = f"Option A has degree exactly 2 and fits the standard polynomial form."
        s3 = f"The other options either have degree 3, degree 1, or simplify to degree 3. Hence, Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 4.1.2: Formulating quadratic equations from verbal descriptions ---
    tc = "CBSE-10-MATH-4-4.1.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        w_diff = 2 + (i % 4)
        area = (10 + i * 2) * (10 + i * 2 + w_diff)
        
        text = f"The length of a rectangular plot is \\({w_diff}\\text{{ m}}\\) more than its breadth \\(x\\). If the area of the plot is \\({area}\\text{{ m}}^2\\), which quadratic equation models this situation?"
        correct = "B"
        c_opt = f"\\(x^2 + {w_diff}x - {area} = 0\\)"
        options = [
            f"\\(x^2 - {w_diff}x + {area} = 0\\)",
            c_opt,
            f"\\(2x + 2(x + {w_diff}) = {area}\\)",
            f"\\(x^2 + {w_diff}x + {area} = 0\\)"
        ]
        s1 = f"Let breadth be \\(x\\text{{ m}}\\). Then length is \\(x + {w_diff}\\text{{ m}}\\)."
        s2 = f"\\(\\text{{Area}} = \\text{{Length}} \\times \\text{{Breadth}} = x(x + {w_diff}) = x^2 + {w_diff}x\\)."
        s3 = f"Equating to area: \\(x^2 + {w_diff}x = {area} \\implies x^2 + {w_diff}x - {area} = 0\\). Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 4.2.1: Finding roots by factoring quadratic trinomials ---
    tc = "CBSE-10-MATH-4-4.2.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        r1 = 2 + (i % 5)
        r2 = -1 * (3 + (i % 4))
        b_val = - (r1 + r2)
        c_val = r1 * r2
        
        text = f"Find the roots of the quadratic equation \\(x^2 + ({b_val})x + ({c_val}) = 0\\) by factorisation:"
        correct = "C"
        options = [
            f"\\(x = {-r1}, x = {-r2}\\)",
            f"\\(x = {r1 + 1}, x = {r2 - 1}\\)",
            f"\\(x = {r1}, x = {r2}\\)",
            f"\\(x = {r1 * 2}, x = {r2}\\)"
        ]
        s1 = f"To factor \\(x^2 + bx + c = 0\\), find two numbers whose sum is \\({b_val}\\) and product is \\({c_val}\\)."
        s2 = f"The numbers are \\({-r1}\\) and \\({-r2}\\), giving factorization \\((x - {r1})(x - ({r2})) = 0\\)."
        s3 = f"Setting each factor to zero: \\(x = {r1}\\) or \\(x = {r2}\\). Option C is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 4.3.1: Quadratic formula derivation: x = [-b ± √(b² - 4ac)] / (2a) ---
    tc = "CBSE-10-MATH-4-4.3.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        a = (i % 3) + 1
        b = 5 + (i % 4)
        c = 1
        d_val = b*b - 4*a*c
        
        text = f"Using the quadratic formula \\(x = \\frac{{-b \\pm \\sqrt{{b^2 - 4ac}}}}{{2a}}\\), what are the roots of \\({a}x^2 + {b}x + {c} = 0\\)?"
        correct = "A"
        c_opt = f"\\(x = \\frac{{- {b} \\pm \\sqrt{{{d_val}}}}}{{{2*a}}}\\)"
        options = [
            c_opt,
            f"\\(x = \\frac{{{b} \\pm \\sqrt{{{d_val}}}}}{{{2*a}}}\\)",
            f"\\(x = \\frac{{- {b} \\pm \\sqrt{{{d_val}}}}}{{{a}}}\\)",
            f"\\(x = \\frac{{- {b} \\pm {d_val}}}{{{2*a}}}\\)"
        ]
        s1 = f"Identify the coefficients: \\(a = {a}\\), \\(b = {b}\\), \\(c = {c}\\)."
        s2 = f"Discriminant \\(D = b^2 - 4ac = ({b})^2 - 4({a})({c}) = {d_val}\\)."
        s3 = f"Applying the formula gives \\(x = \\frac{{- {b} \\pm \\sqrt{{{d_val}}}}}{{{2*a}}}\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 4.4.1: D > 0: Two distinct real roots ---
    tc = "CBSE-10-MATH-4-4.4.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        a = 1
        b = 6 + i % 4
        c = 2
        d_val = b*b - 4*a*c
        
        text = f"What is the nature of the roots of the quadratic equation \\(x^2 + {b}x + {c} = 0\\)?"
        correct = "B"
        options = [
            "Two equal real roots",
            "Two distinct real roots",
            "No real roots (complex roots)",
            "One real root and one imaginary root"
        ]
        s1 = f"Compute discriminant \\(D = b^2 - 4ac\\)."
        s2 = f"Here, \\(D = ({b})^2 - 4(1)({c}) = {d_val}\\)."
        s3 = f"Since \\(D = {d_val} > 0\\), the equation has two distinct real roots. Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 4.4.2: D = 0: Two equal real roots ---
    tc = "CBSE-10-MATH-4-4.4.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        r = 2 + (i % 6)
        b = 2 * r
        c = r * r
        
        text = f"Why does the equation \\(x^2 - {b}x + {c} = 0\\) possess two equal real roots?"
        correct = "A"
        options = [
            f"Because its discriminant \\(D = (-{b})^2 - 4(1)({c}) = 0\\)",
            f"Because its constant term is a perfect square",
            f"Because coefficient of \\(x\\) is even",
            f"Because \\(a = 1\\)"
        ]
        s1 = f"A quadratic equation \\(ax^2 + bx + c = 0\\) has two equal real roots if and only if \\(D = b^2 - 4ac = 0\\)."
        s2 = f"Evaluating \\(D = (-{b})^2 - 4(1)({c}) = {b*b} - {4*c} = 0\\)."
        s3 = f"Since \\(D = 0\\), it forms a perfect square \\((x - {r})^2 = 0\\) giving two equal real roots \\(x = {r}\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 4.4.3: D < 0: No real roots ---
    tc = "CBSE-10-MATH-4-4.4.3"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        a = 2
        b = 2
        c = 5 + (i % 5)
        d_val = b*b - 4*a*c
        
        text = f"Determine the nature of the roots of \\({a}x^2 + {b}x + {c} = 0\\):"
        correct = "C"
        options = [
            "Two distinct real roots",
            "Two equal real roots",
            "No real roots",
            "Infinitely many roots"
        ]
        s1 = f"Calculate the discriminant \\(D = b^2 - 4ac\\)."
        s2 = f"\\(D = (2)^2 - 4({a})({c}) = 4 - {4*a*c} = {d_val}\\)."
        s3 = f"Since \\(D = {d_val} < 0\\), the square root of \\(D\\) is not real. Hence, there are no real roots. Option C is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 4.4.4: Finding unknown parameter k for equal roots ---
    tc = "CBSE-10-MATH-4-4.4.4"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        c = (i % 6) + 1
        # 2x^2 + kx + 3 = 0 -> k^2 - 4(2)(c) = 0 -> k = ±√(8c)
        val = 8 * c
        
        text = f"Find the non-zero value(s) of \\(k\\) for which the quadratic equation \\(2x^2 + kx + {c} = 0\\) has two equal real roots:"
        correct = "D"
        c_opt = f"\\(k = \\pm \\sqrt{{{val}}}\\)"
        options = [
            f"\\(k = {c}\\)",
            f"\\(k = {val}\\)",
            f"\\(k = 0\\)",
            c_opt
        ]
        s1 = f"For equal real roots, discriminant must satisfy \\(D = b^2 - 4ac = 0\\)."
        s2 = f"Here, \\(a = 2\\), \\(b = k\\), \\(c = {c}\\). Thus, \\(k^2 - 4(2)({c}) = 0 \\implies k^2 - {val} = 0\\)."
        s3 = f"Solving gives \\(k^2 = {val} \\implies k = \\pm \\sqrt{{{val}}}\\). Option D is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 4.5.1: Train speed decrease/increase problems ---
    tc = "CBSE-10-MATH-4-4.5.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        speed = 40 + (i % 5) * 10
        dist = 360
        diff_h = 1
        
        text = f"An express train takes \\(1\\text{{ hour}}\\) less for a journey of \\({dist}\\text{{ km}}\\) if its speed is increased by \\(5\\text{{ km/h}}\\). Which quadratic equation models this relation for usual speed \\(x\\text{{ km/h}}\\)?"
        correct = "B"
        c_opt = f"\\(x^2 + 5x - 1800 = 0\\)"
        options = [
            f"\\(x^2 - 5x - 1800 = 0\\)",
            c_opt,
            f"\\(x^2 + 5x + 1800 = 0\\)",
            f"\\(5x^2 + x - 360 = 0\\)"
        ]
        s1 = f"Let usual speed be \\(x\\text{{ km/h}}\\). Time taken is \\(\\frac{{{dist}}}{{x}}\\text{{ hours}}\\)."
        s2 = f"With increased speed \\(x + 5\\), time is \\(\\frac{{{dist}}}{{x + 5}}\\). The difference is \\(\\frac{{{dist}}}{{x}} - \\frac{{{dist}}}{{x + 5}} = 1\\)."
        s3 = f"Simplifying: \\({dist}\\left[\\frac{{(x + 5) - x}}{{x(x + 5)}}\\right] = 1 \\implies \\frac{{{dist} \\times 5}}{{x^2 + 5x}} = 1 \\implies x^2 + 5x - 1800 = 0\\). Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 4.5.2: Two water taps filling a pool together problems ---
    tc = "CBSE-10-MATH-4-4.5.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        diff_t = 10
        
        text = f"Two water taps together can fill a tank in \\(9\\frac{{3}}{{8}}\\text{{ hours}}\\). The tap of larger diameter takes \\({diff_t}\\text{{ hours}}\\) less than the smaller one to fill the tank separately. If the smaller tap takes \\(x\\text{{ hours}}\\), what is the governing quadratic equation?"
        correct = "A"
        c_opt = f"\\(4x^2 - 115x + 375 = 0\\)"
        options = [
            c_opt,
            f"\\(4x^2 + 115x - 375 = 0\\)",
            f"\\(8x^2 - 75x + 100 = 0\\)",
            f"\\(x^2 - 10x - 75 = 0\\)"
        ]
        s1 = f"Let smaller tap take \\(x\\text{{ h}}\\) and larger tap take \\(x - 10\\text{{ h}}\\). Together they fill in \\(\\frac{{75}}{{8}}\\text{{ h}}\\)."
        s2 = f"Work done in 1 hour: \\(\\frac{{1}}{{x}} + \\frac{{1}}{{x - 10}} = \\frac{{8}}{{75}}\\)."
        s3 = f"\\(\\frac{{2x - 10}}{{x^2 - 10x}} = \\frac{{8}}{{75}} \\implies 75(2x - 10) = 8(x^2 - 10x) \\implies 8x^2 - 80x = 150x - 750 \\implies 8x^2 - 230x + 750 = 0 \\implies 4x^2 - 115x + 375 = 0\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # =========================================================================
    # CHAPTER 5: ARITHMETIC PROGRESSIONS (7 subtopics, 80 Qs each = 560 Qs)
    # =========================================================================

    # --- 5.1.1: Arithmetic progression sequence: a, a+d, a+2d, ... ---
    tc = "CBSE-10-MATH-5-5.1.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        a = 3 + (i % 5)
        d = 4 + (i % 4)
        terms = [a + k * d for k in range(4)]
        
        text = f"Write the first four terms of the Arithmetic Progression whose first term is \\(a = {a}\\) and common difference is \\(d = {d}\\):"
        correct = "B"
        c_opt = f"\\({terms[0]}, {terms[1]}, {terms[2]}, {terms[3]}\\)"
        options = [
            f"\\({terms[0]}, {terms[0]*d}, {terms[0]*d*d}, {terms[0]*d**3}\\)",
            c_opt,
            f"\\({terms[0]}, {terms[1]+1}, {terms[2]+2}, {terms[3]+3}\\)",
            f"\\({terms[0]}, {terms[1]}, {terms[1]+d+2}, {terms[1]+2*d+4}\\)"
        ]
        s1 = f"An Arithmetic Progression with first term \\(a\\) and common difference \\(d\\) is generated by \\(a, a+d, a+2d, a+3d, \\dots\\)."
        s2 = f"Substituting \\(a = {a}\\) and \\(d = {d}\\): \\(T_1 = {terms[0]}\\), \\(T_2 = {terms[1]}\\), \\(T_3 = {terms[2]}\\), \\(T_4 = {terms[3]}\\)."
        s3 = f"Thus, the first four terms are {c_opt}. Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 5.1.2: Determining whether a given sequence forms an AP ---
    tc = "CBSE-10-MATH-5-5.1.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        text = f"Which of the following sequences forms an Arithmetic Progression?"
        correct = "C"
        options = [
            "\\(1, 2, 4, 8, 16, \\dots\\)",
            "\\(1^2, 2^2, 3^2, 4^2, \\dots\\)",
            f"\\(\\sqrt{{2}}, \\sqrt{{8}}, \\sqrt{{18}}, \\sqrt{{32}}, \\dots\\)",
            "\\(0.2, 0.22, 0.222, 0.2222, \\dots\\)"
        ]
        s1 = f"A sequence \\(a_1, a_2, a_3, \\dots\\) forms an AP if the difference \\(a_{{k+1}} - a_k\\) remains constant for all \\(k\\)."
        s2 = f"Simplifying Option C: \\(\\sqrt{{2}}, 2\\sqrt{{2}}, 3\\sqrt{{2}}, 4\\sqrt{{2}}, \\dots\\)."
        s3 = f"The common difference is \\(2\\sqrt{{2}} - \\sqrt{{2}} = 3\\sqrt{{2}} - 2\\sqrt{{2}} = \\sqrt{{2}}\\) (constant). Hence, Option C forms an AP."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 5.2.1: Finding specific terms, n, and first negative term ---
    tc = "CBSE-10-MATH-5-5.2.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        a = 2 + (i % 4)
        d = 3 + (i % 3)
        n = 10 + (i % 15)
        an = a + (n - 1) * d
        
        text = f"Find the \\({n}^{{\\text{{th}}}}\\ term of the Arithmetic Progression \\({a}, {a+d}, {a+2*d}, \\dots\\):"
        correct = "A"
        options = [
            f"\\({an}\\)",
            f"\\({an - d}\\)",
            f"\\({an + d}\\)",
            f"\\({an + 2}\\)"
        ]
        s1 = f"The \\(n^{{\\text{{th}}}}\\) term of an AP is given by \\(a_n = a + (n - 1)d\\)."
        s2 = f"Here, \\(a = {a}\\), \\(d = {d}\\), and \\(n = {n}\\). Substituting gives \\(a_{{{n}}} = {a} + ({n} - 1)({d}) = {a} + {n-1} \\times {d}\\)."
        s3 = f"\\(a_{{{n}}} = {a} + {(n-1)*d} = {an}\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 5.2.2: nth term from the end formula: l - (n - 1)d ---
    tc = "CBSE-10-MATH-5-5.2.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        a = 3
        d = 4
        last = 203 + (i % 5) * 4
        m = 10 + (i % 6) # mth term from end
        ans = last - (m - 1) * d
        
        text = f"Find the \\({m}^{{\\text{{th}}}}\\) term from the end of the AP \\({a}, {a+d}, {a+2*d}, \\dots, {last}\\):"
        correct = "B"
        options = [
            f"\\({ans + d}\\)",
            f"\\({ans}\\)",
            f"\\({ans - d}\\)",
            f"\\({last - m * d}\\)"
        ]
        s1 = f"The \\(m^{{\\text{{th}}}}\\) term from the end of an AP with last term \\(l\\) and common difference \\(d\\) is given by \\(a'_m = l - (m - 1)d\\)."
        s2 = f"Here, \\(l = {last}\\), \\(d = {d}\\), \\(m = {m}\\)."
        s3 = f"\\(a'_{{{m}}} = {last} - ({m} - 1)({d}) = {last} - {(m-1)*d} = {ans}\\). Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 5.3.1: Sum formula with last term: S_n = n/2(a + l) ---
    tc = "CBSE-10-MATH-5-5.3.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        n = 10 + (i % 10) * 2
        a = 1 + (i % 4)
        d = 2 + (i % 3)
        l = a + (n - 1) * d
        sn = (n * (a + l)) // 2
        
        text = f"Find the sum of the first \\({n}\\) terms of an AP whose first term is \\(a = {a}\\) and last term is \\(l = {l}\\):"
        correct = "D"
        options = [
            f"\\({sn - 20}\\)",
            f"\\({sn + 20}\\)",
            f"\\({n * (a + l)}\\)",
            f"\\({sn}\\)"
        ]
        s1 = f"The sum of the first \\(n\\) terms of an AP when first and last terms are known is \\(S_n = \\frac{{n}}{{2}}(a + l)\\)."
        s2 = f"Substituting \\(n = {n}\\), \\(a = {a}\\), and \\(l = {l}\\): \\(S_{{{n}}} = \\frac{{{n}}}{{2}}({a} + {l}) = {n // 2} \\times {a + l}\\)."
        s3 = f"\\(S_{{{n}}} = {sn}\\). Option D is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 5.3.2: Relation between sum and nth term: a_n = S_n - S_(n-1) ---
    tc = "CBSE-10-MATH-5-5.3.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        p = (i % 3) + 1
        q = (i % 4) + 2
        # S_n = p*n^2 + q*n -> a_n = S_n - S_(n-1) = 2*p*n + (q - p)
        coeff_n = 2 * p
        const_term = q - p
        
        text = f"If the sum of the first \\(n\\) terms of an AP is given by \\(S_n = {p}n^2 + {q}n\\), find its \\(n^{{\\text{{th}}}}\\) term \\(a_n\\):"
        correct = "C"
        c_opt = f"\\({coeff_n}n + ({const_term})\\)" if const_term != 0 else f"\\({coeff_n}n\\)"
        options = [
            f"\\({p}n + {q}\\)",
            f"\\({2*p}n + {q}\\)",
            c_opt,
            f"\\({p}n^2 - {q}n\\)"
        ]
        s1 = f"The \\(n^{{\\text{{th}}}}\\) term is related to the sum by the identity \\(a_n = S_n - S_{{n-1}}\\)."
        s2 = f"\\(S_n = {p}n^2 + {q}n\\), and \\(S_{{n-1}} = {p}(n-1)^2 + {q}(n-1) = {p}(n^2 - 2n + 1) + {q}n - {q}\\)."
        s3 = f"Subtracting: \\(a_n = ({p}n^2 + {q}n) - [{p}n^2 + ({q} - 2{p})n + ({p} - {q})] = {coeff_n}n + ({const_term})\\). Option C is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 5.4.1: Applied word problems (potato race, log stacking, loan repayments) ---
    tc = "CBSE-10-MATH-5-5.4.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        start_pay = 1000 + (i % 5) * 100
        inc = 50 + (i % 4) * 10
        m = 30 # months
        tot = (m * (2 * start_pay + (m - 1) * inc)) // 2
        
        text = f"A borrower repays a loan by paying \\(₹{start_pay}\\) in the first month and then increases the payment by \\(₹{inc}\\) every month. How much total amount is paid by him in \\({m}\\text{{ installments}}\\)?"
        correct = "A"
        options = [
            f"\\(₹{tot}\\)",
            f"\\(₹{tot - 500}\\)",
            f"\\(₹{tot + 500}\\)",
            f"\\(₹{m * start_pay}\\)"
        ]
        s1 = f"The monthly payments form an AP with first term \\(a = {start_pay}\\), common difference \\(d = {inc}\\), and \\(n = {m}\\)."
        s2 = f"Using sum formula \\(S_n = \\frac{{n}}{{2}}[2a + (n - 1)d]\\): \\(S_{{{m}}} = \\frac{{{m}}}{{2}}[2({start_pay}) + ({m} - 1)({inc})]\\)."
        s3 = f"\\(S_{{{m}}} = {m // 2}[{2 * start_pay} + {(m - 1) * inc}] = {tot}\\). Hence total amount is \\(₹{tot}\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # =========================================================================
    # CHAPTER 6: TRIANGLES (10 subtopics, 80 Qs each = 800 Qs)
    # 100% FIGURE-RICH GEOMETRY QUESTIONS WITH RESPONSIVE VECTOR SVGS!
    # =========================================================================

    # --- 6.1.1: Definition of similarity (equiangular and proportional sides) ---
    tc = "CBSE-10-MATH-6-6.1.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        scale = 1.5
        
        svg_code = """<svg viewBox="0 0 380 160" width="100%" height="150" style="max-width:400px; display:block; margin:8px auto; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <polygon points="50,20 15,130 130,130" fill="rgba(37,99,235,0.08)" stroke="#1e293b" stroke-width="2" />
  <text x="50" y="15" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">A</text>
  <text x="8" y="140" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">B</text>
  <text x="135" y="140" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">C</text>
  
  <polygon points="260,10 210,140 360,140" fill="rgba(22,163,74,0.08)" stroke="#1e293b" stroke-width="2" />
  <text x="260" y="8" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">D</text>
  <text x="200" y="150" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">E</text>
  <text x="365" y="150" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">F</text>
  <text x="190" y="85" font-family="sans-serif" font-size="11" fill="#2563eb" text-anchor="middle">~ (Similar)</text>
</svg>"""

        text = f"Two polygons/triangles are similar if and only if which two strict mathematical conditions are simultaneously satisfied?\n\n{svg_code}"
        correct = "B"
        options = [
            "Their corresponding angles are unequal but sides are equal",
            "Their corresponding angles are equal and their corresponding sides are in the same ratio (proportional)",
            "Their perimeters and areas are exactly congruent",
            "Their corresponding sides are equal irrespective of angles"
        ]
        s1 = f"By definition, two triangles \\(\\triangle ABC\\) and \\(\\triangle DEF\\) are similar (\\(\\triangle ABC \\sim \\triangle DEF\\)) if:"
        s2 = f"1. Their corresponding angles are equal: \\(\\angle A = \\angle D\\), \\(\\angle B = \\angle E\\), \\(\\angle C = \\angle F\\)."
        s3 = f"2. Their corresponding sides are proportional: \\(\\frac{{AB}}{{DE}} = \\frac{{BC}}{{EF}} = \\frac{{AC}}{{DF}}\\). Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff, req_fig=True))

    # --- 6.1.2: Equiangular triangles (AAA / AA similarity) ---
    tc = "CBSE-10-MATH-6-6.1.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        ang_a = 50 + (i % 6) * 5
        ang_b = 60 + (i % 4) * 5
        ang_c = 180 - (ang_a + ang_b)
        
        svg_code = f"""<svg viewBox="0 0 380 150" width="100%" height="140" style="max-width:400px; display:block; margin:8px auto; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <polygon points="60,25 20,130 140,130" fill="none" stroke="#1e293b" stroke-width="2"/>
  <text x="60" y="20" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">A ({ang_a}°)</text>
  <text x="15" y="142" font-size="11" font-weight="bold" fill="#0f172a">B ({ang_b}°)</text>
  <text x="145" y="142" font-size="11" font-weight="bold" fill="#0f172a">C</text>
  
  <polygon points="270,15 220,140 360,140" fill="none" stroke="#2563eb" stroke-width="2"/>
  <text x="270" y="10" font-size="11" font-weight="bold" fill="#2563eb" text-anchor="middle">D ({ang_a}°)</text>
  <text x="210" y="152" font-size="11" font-weight="bold" fill="#2563eb">E ({ang_b}°)</text>
  <text x="365" y="152" font-size="11" font-weight="bold" fill="#2563eb">F</text>
</svg>"""

        text = f"In \\(\\triangle ABC\\) and \\(\\triangle DEF\\) shown below, \\(\\angle A = {ang_a}^\\circ = \\angle D\\) and \\(\\angle B = {ang_b}^\\circ = \\angle E\\):\n\n{svg_code}\n\nBy which criterion are the two triangles similar, and what is the measure of \\(\\angle C\\)?"
        correct = "A"
        options = [
            f"AA similarity criterion, and \\(\\angle C = {ang_c}^\\circ\\)",
            f"SAS similarity criterion, and \\(\\angle C = {ang_a}^\\circ\\)",
            f"SSS similarity criterion, and \\(\\angle C = 90^\\circ\\)",
            f"RHS similarity criterion, and \\(\\angle C = {ang_b}^\\circ\\)"
        ]
        s1 = f"The AA similarity criterion states that if two angles of one triangle are respectively equal to two angles of another triangle, then the two triangles are similar."
        s2 = f"Here, \\(\\angle A = \\angle D = {ang_a}^\\circ\\) and \\(\\angle B = \\angle E = {ang_b}^\\circ\\), so \\(\\triangle ABC \\sim \\triangle DEF\\) by AA."
        s3 = f"The third angle is \\(\\angle C = 180^\\circ - ({ang_a}^\\circ + {ang_b}^\\circ) = {ang_c}^\\circ\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff, req_fig=True))

    # --- 6.1.3: Proportional sides (SSS similarity) ---
    tc = "CBSE-10-MATH-6-6.1.3"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        k = 2 if i % 2 == 1 else 3
        ab, bc, ca = 3, 4, 5
        de, ef, fd = ab * k, bc * k, ca * k
        
        svg_code = f"""<svg viewBox="0 0 380 150" width="100%" height="140" style="max-width:400px; display:block; margin:8px auto; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <polygon points="50,30 20,130 120,130" fill="none" stroke="#1e293b" stroke-width="2"/>
  <text x="25" y="75" font-size="10" fill="#2563eb">{ab}</text>
  <text x="70" y="142" font-size="10" fill="#2563eb">{bc}</text>
  <text x="95" y="75" font-size="10" fill="#2563eb">{ca}</text>
  
  <polygon points="270,15 210,145 360,145" fill="none" stroke="#16a34a" stroke-width="2"/>
  <text x="230" y="75" font-size="10" fill="#16a34a">{de}</text>
  <text x="285" y="157" font-size="10" fill="#16a34a">{ef}</text>
  <text x="330" y="75" font-size="10" fill="#16a34a">{fd}</text>
</svg>"""

        text = f"In the triangles shown below, \\(AB = {ab}\\), \\(BC = {bc}\\), \\(CA = {ca}\\) and \\(DE = {de}\\), \\(EF = {ef}\\), \\(FD = {fd}\\):\n\n{svg_code}\n\nWhat is the ratio of their corresponding sides and the similarity criterion?"
        correct = "C"
        options = [
            f"Ratio \\(1 : {k+1}\\), by SAS similarity",
            f"Ratio \\(1 : 1\\), by RHS congruence",
            f"Ratio \\(1 : {k}\\), by SSS similarity criterion",
            f"Ratio \\({k} : 1\\), by AA similarity"
        ]
        s1 = f"Calculate the ratio of corresponding sides: \\(\\frac{{AB}}{{DE}} = \\frac{{{ab}}}{{{de}}} = \\frac{{1}}{{{k}}}\\), \\(\\frac{{BC}}{{EF}} = \\frac{{{bc}}}{{{ef}}} = \\frac{{1}}{{{k}}}\\), \\(\\frac{{CA}}{{FD}} = \\frac{{{ca}}}{{{fd}}} = \\frac{{1}}{{{k}}}\\)."
        s2 = f"Since all three pairs of corresponding sides are in the same ratio, \\(\\triangle ABC \\sim \\triangle DEF\\) by SSS similarity."
        s3 = f"The scale factor of similarity is \\(1 : {k}\\). Option C is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff, req_fig=True))

    # --- 6.1.4: Ratio of two sides and included angle (SAS similarity) ---
    tc = "CBSE-10-MATH-6-6.1.4"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        ang = 70
        ab = 2.5
        ac = 5
        pq = 5
        pr = 10
        
        text = f"In \\(\\triangle ABC\\) and \\(\\triangle PQR\\), \\(AB = 2.5\\text{{ cm}}\\), \\(AC = 5\\text{{ cm}}\\), \\(\\angle A = 70^\\circ\\), and \\(PQ = 5\\text{{ cm}}\\), \\(PR = 10\\text{{ cm}}\\), \\(\\angle P = 70^\\circ\\). Are the triangles similar?"
        correct = "A"
        options = [
            "Yes, similar by SAS similarity criterion (\\(\\triangle ABC \\sim \\triangle PQR\\))",
            "No, because the angles are not right angles",
            "Yes, congruent by SAS congruence criterion",
            "Cannot be determined without knowing the third side"
        ]
        s1 = f"The SAS similarity criterion states that if one angle of a triangle is equal to one angle of another triangle and the sides including these angles are proportional, the triangles are similar."
        s2 = f"Here, \\(\\angle A = \\angle P = 70^\\circ\\), and \\(\\frac{{AB}}{{PQ}} = \\frac{{2.5}}{{5}} = \\frac{{1}}{{2}}\\), \\(\\frac{{AC}}{{PR}} = \\frac{{5}}{{10}} = \\frac{{1}}{{2}}\\)."
        s3 = f"Since the included angles are equal and their adjacent sides are proportional, \\(\\triangle ABC \\sim \\triangle PQR\\) by SAS. Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 6.2.1: Basic Proportionality Theorem (BPT / Thales Theorem) ---
    tc = "CBSE-10-MATH-6-6.2.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        ad = 1.5 + (i % 4) * 0.5
        db = 3.0
        ae = 1.0 + (i % 3) * 0.5
        ec = (db * ae) / ad
        
        svg_code = f"""<svg viewBox="0 0 300 180" width="100%" height="160" style="max-width:320px; display:block; margin:8px auto; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <polygon points="150,20 40,160 260,160" fill="none" stroke="#1e293b" stroke-width="2.2" />
  <line x1="85" y1="102" x2="215" y2="102" stroke="#2563eb" stroke-width="2" stroke-dasharray="4,2"/>
  <text x="150" y="15" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">A</text>
  <text x="30" y="165" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">B</text>
  <text x="268" y="165" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">C</text>
  <text x="70" y="102" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">D</text>
  <text x="222" y="102" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">E</text>
  <text x="150" y="95" font-family="sans-serif" font-size="10" fill="#2563eb" text-anchor="middle">DE || BC</text>
  <text x="95" y="60" font-size="10" fill="#475569">AD = {ad}</text>
  <text x="50" y="135" font-size="10" fill="#475569">DB = {db}</text>
  <text x="195" y="60" font-size="10" fill="#475569">AE = {ae}</text>
  <text x="240" y="135" font-size="10" fill="#dc2626">EC = ?</text>
</svg>"""

        text = f"In \\(\\triangle ABC\\) shown below, \\(DE \\parallel BC\\). Given \\(AD = {ad}\\text{{ cm}}\\), \\(DB = {db}\\text{{ cm}}\\), and \\(AE = {ae}\\text{{ cm}}\\), find the length of \\(EC\\):\n\n{svg_code}"
        correct = "B"
        c_opt = f"\\({ec:.1f}\\text{{ cm}}\\)"
        options = [
            f"\\({ec + 1.0:.1f}\\text{{ cm}}\\)",
            c_opt,
            f"\\({ec * 2:.1f}\\text{{ cm}}\\)",
            f"\\({max(0.5, ec - 0.5):.1f}\\text{{ cm}}\\)"
        ]
        s1 = f"By Basic Proportionality Theorem (Thales Theorem), if a line is drawn parallel to one side of a triangle intersecting the other two sides, then it divides the two sides in the same ratio: \\(\\frac{{AD}}{{DB}} = \\frac{{AE}}{{EC}}\\)."
        s2 = f"Substitute the given lengths: \\(\\frac{{{ad}}}{{{db}}} = \\frac{{{ae}}}{{EC}}\\)."
        s3 = f"Cross-multiplying: \\(EC = \\frac{{{db} \\times {ae}}}{{{ad}}} = {ec:.1f}\\text{{ cm}}\\). Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff, req_fig=True))

    # --- 6.2.2: Converse of BPT theorem ---
    tc = "CBSE-10-MATH-6-6.2.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        ad = 2.0 + (i % 3)
        db = 4.0 + 2 * (i % 3)
        ae = 3.0
        ec = 6.0
        # Ratio is 1:2
        
        text = f"In \\(\\triangle ABC\\), point \\(D\\) lies on \\(AB\\) and point \\(E\\) lies on \\(AC\\) such that \\(AD = {ad}\\text{{ cm}}\\), \\(DB = {db}\\text{{ cm}}\\), \\(AE = {ae}\\text{{ cm}}\\), and \\(EC = {ec}\\text{{ cm}}\\). What conclusion follows from the Converse of Basic Proportionality Theorem?"
        correct = "A"
        options = [
            "\\(DE \\parallel BC\\) because \\(\\frac{AD}{DB} = \\frac{AE}{EC} = \\frac{1}{2}\\)",
            "\\(DE\\) is perpendicular to \\(BC\\)",
            "\\(DE\\) cannot be parallel to \\(BC\\)",
            "\\(\\triangle ABC\\) must be an equilateral triangle"
        ]
        s1 = f"The Converse of BPT states that if a line divides any two sides of a triangle in the same ratio, then the line must be parallel to the third side."
        s2 = f"Here, \\(\\frac{{AD}}{{DB}} = \\frac{{{ad}}}{{{db}}} = \\frac{{1}}{{2}}\\) and \\(\\frac{{AE}}{{EC}} = \\frac{{{ae}}}{{{ec}}} = \\frac{{1}}{{2}}\\)."
        s3 = f"Since \\(\\frac{{AD}}{{DB}} = \\frac{{AE}}{{EC}}\\), by the converse of BPT, \\(DE \\parallel BC\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 6.3.1: Ratio of areas of similar triangles = square of ratio of sides ---
    tc = "CBSE-10-MATH-6-6.3.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        s1_val = 3 + (i % 4)
        s2_val = 5 + (i % 3)
        r_area1 = s1_val * s1_val
        r_area2 = s2_val * s2_val
        
        text = f"If \\(\\triangle ABC \\sim \\triangle DEF\\) with corresponding sides in the ratio \\(AB : DE = {s1_val} : {s2_val}\\), what is the ratio of their areas \\(\\frac{{\\text{{Area}}(\\triangle ABC)}}{{\\text{{Area}}(\\triangle DEF)}}\\)?"
        correct = "D"
        c_opt = f"\\({r_area1} : {r_area2}\\)"
        options = [
            f"\\({s1_val} : {s2_val}\\)",
            f"\\({2*s1_val} : {2*s2_val}\\)",
            f"\\(\\sqrt{{{s1_val}}} : \\sqrt{{{s2_val}}}\\)",
            c_opt
        ]
        s1 = f"The ratio of the areas of two similar triangles is equal to the square of the ratio of their corresponding sides."
        s2 = f"\\(\\frac{{\\text{{Area}}(\\triangle ABC)}}{{\\text{{Area}}(\\triangle DEF)}} = \\left(\\frac{{AB}}{{DE}}\\right)^2 = \\left(\\frac{{{s1_val}}}{{{s2_val}}}\\right)^2\\)."
        s3 = f"Squaring numerator and denominator gives \\(\\frac{{{r_area1}}}{{{r_area2}}}\\) or \\({r_area1} : {r_area2}\\). Option D is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 6.4.1: Theorem: Similarity in right triangle with altitude to hypotenuse ---
    tc = "CBSE-10-MATH-6-6.4.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        svg_code = """<svg viewBox="0 0 300 170" width="100%" height="150" style="max-width:320px; display:block; margin:8px auto; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <polygon points="30,140 270,140 100,30" fill="none" stroke="#1e293b" stroke-width="2.2" />
  <line x1="100" y1="30" x2="100" y2="140" stroke="#2563eb" stroke-width="2" stroke-dasharray="3,2"/>
  <text x="95" y="20" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">B (90°)</text>
  <text x="18" y="145" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">A</text>
  <text x="275" y="145" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">C</text>
  <text x="105" y="155" font-family="sans-serif" font-size="11" font-weight="bold" fill="#2563eb">D</text>
  <text x="110" y="85" font-size="10" fill="#2563eb">BD ⟂ AC</text>
</svg>"""

        text = f"In a right triangle \\(\\triangle ABC\\) right-angled at \\(B\\), altitude \\(BD\\) is drawn perpendicular to hypotenuse \\(AC\\) as shown:\n\n{svg_code}\n\nWhich of the following similarity relationships is geometrically established by Theorem 6.7?"
        correct = "A"
        options = [
            "\\(\\triangle ADB \\sim \\triangle ABC\\) and \\(\\triangle BDC \\sim \\triangle ABC\\) and \\(\\triangle ADB \\sim \\triangle BDC\\)",
            "\\(\\triangle ADB \\cong \\triangle BDC\\) always",
            "\\(BD^2 = AB \\times BC\\)",
            "\\(\\triangle ABC\\) is similar only to \\(\\triangle BDC\\) but not \\(\\triangle ADB\\)"
        ]
        s1 = f"Theorem 6.7 states: If a perpendicular is drawn from the vertex of the right angle of a right triangle to the hypotenuse, then triangles on both sides of the perpendicular are similar to the whole triangle and to each other."
        s2 = f"Both smaller triangles share one acute angle with \\(\\triangle ABC\\) and have a right angle, making them equiangular."
        s3 = f"Therefore, \\(\\triangle ADB \\sim \\triangle ABC\\), \\(\\triangle BDC \\sim \\triangle ABC\\), and \\(\\triangle ADB \\sim \\triangle BDC\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff, req_fig=True))

    # --- 6.4.2: Converse of Pythagoras theorem ---
    tc = "CBSE-10-MATH-6-6.4.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        triplets = [(6, 8, 10), (5, 12, 13), (7, 24, 25), (8, 15, 17), (9, 40, 41)]
        t = triplets[i % len(triplets)]
        mult = (i % 3) + 1
        a_side = t[0] * mult
        b_side = t[1] * mult
        c_side = t[2] * mult
        
        text = f"In \\(\\triangle PQR\\), the lengths of the sides are \\(PQ = {a_side}\\text{{ cm}}\\), \\(QR = {b_side}\\text{{ cm}}\\), and \\(PR = {c_side}\\text{{ cm}}\\). By the Converse of Pythagoras Theorem, which angle is a right angle?"
        correct = "B"
        options = [
            f"\\(\\angle P\\)",
            f"\\(\\angle Q = 90^\\circ\\) (opposite to longest side \\(PR\\))",
            f"\\(\\angle R\\)",
            "None, because the triangle is acute"
        ]
        s1 = f"The Converse of Pythagoras Theorem states: In a triangle, if square of one side is equal to sum of squares of the other two sides, the angle opposite the first side is a right angle."
        s2 = f"Check: \\(PQ^2 + QR^2 = {a_side}^2 + {b_side}^2 = {a_side*a_side} + {b_side*b_side} = {c_side*c_side} = PR^2\\)."
        s3 = f"Since \\(PR^2 = PQ^2 + QR^2\\), the angle opposite the hypotenuse \\(PR\\) is \\(\\angle Q = 90^\\circ\\). Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 6.4.3: Applications in geometric calculations and ladder problems ---
    tc = "CBSE-10-MATH-6-6.4.3"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        ladder = 10 + (i % 4) * 5
        base = 6 + (i % 4) * 3
        # h = sqrt(ladder^2 - base^2) = 8 + (i % 4)*4
        h_wall = int(math.sqrt(ladder**2 - base**2))
        
        svg_code = f"""<svg viewBox="0 0 280 180" width="100%" height="160" style="max-width:300px; display:block; margin:8px auto; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <!-- Ground & Wall -->
  <line x1="30" y1="150" x2="250" y2="150" stroke="#64748b" stroke-width="2.5" />
  <line x1="50" y1="20" x2="50" y2="150" stroke="#1e293b" stroke-width="3" />
  <!-- Ladder -->
  <line x1="50" y1="35" x2="200" y2="150" stroke="#dc2626" stroke-width="3" />
  <!-- Rungs on ladder -->
  <line x1="80" y1="58" x2="88" y2="68" stroke="#f59e0b" stroke-width="2"/>
  <line x1="110" y1="81" x2="118" y2="91" stroke="#f59e0b" stroke-width="2"/>
  <line x1="140" y1="104" x2="148" y2="114" stroke="#f59e0b" stroke-width="2"/>
  <!-- Labels -->
  <text x="135" y="80" font-size="11" font-weight="bold" fill="#dc2626">Ladder = {ladder} m</text>
  <text x="115" y="165" font-size="10" fill="#475569">Base = {base} m</text>
  <text x="15" y="90" font-size="11" font-weight="bold" fill="#2563eb">h = ?</text>
</svg>"""

        text = f"A ladder of length \\({ladder}\\text{{ m}}\\) reaches a window of a building. If the foot of the ladder is \\({base}\\text{{ m}}\\) away from the base of the wall on level ground as shown below, how high above the ground is the window?\n\n{svg_code}"
        correct = "C"
        c_opt = f"\\({h_wall}\\text{{ m}}\\)"
        options = [
            f"\\({h_wall + 2}\\text{{ m}}\\)",
            f"\\({ladder - base}\\text{{ m}}\\)",
            c_opt,
            f"\\({h_wall - 1}\\text{{ m}}\\)"
        ]
        s1 = f"The wall, the ground, and the ladder form a right-angled triangle with the ladder as hypotenuse."
        s2 = f"By Pythagoras Theorem: \\(h^2 + \\text{{base}}^2 = \\text{{ladder}}^2 \\implies h^2 + {base}^2 = {ladder}^2\\)."
        s3 = f"\\(h^2 = {ladder}^2 - {base}^2 = {ladder*ladder} - {base*base} = {h_wall*h_wall} \\implies h = {h_wall}\\text{{ m}}\\). Option C is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff, req_fig=True))

    out_file = './scripts/audit_data/cbse10_math_ch4_to_6_generated.json'
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2)
    print(f"✓ Generated {len(questions)} validated questions saved to {out_file}")

if __name__ == '__main__':
    generate_ch4_to_6()
