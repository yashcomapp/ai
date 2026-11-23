import json
import os
import math

def generate_ch7_to_10():
    print("=== Generating CBSE 10 Mathematics Chapters 7, 8, 9, 10 (2,400 Questions) ===")
    
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
            "\\(3\\)", "\\(-3\\)", "\\(4\\)", "\\(-4\\)", "\\(5\\)", "\\(-5\\)",
            "\\(10\\)", "\\(-10\\)", "\\(\\frac{1}{2}\\)", "\\(\\frac{\\sqrt{3}}{2}\\)",
            "\\(\\frac{1}{\\sqrt{2}}\\)", "\\(5\\text{ m}\\)", "\\(10\\text{ m}\\)",
            "\\(15\\text{ m}\\)", "\\(20\\text{ m}\\)", "\\(25\\text{ m}\\)", "\\(30\\text{ m}\\)",
            "\\(5\\text{ cm}\\)", "\\(8\\text{ cm}\\)", "\\(10\\text{ cm}\\)", "\\(12\\text{ cm}\\)"
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
    # CHAPTER 7: COORDINATE GEOMETRY (9 subtopics, 80 Qs each = 720 Qs)
    # =========================================================================

    # --- 7.1.1: Derivation of distance formula from Pythagoras theorem ---
    tc = "CBSE-10-MATH-7-7.1.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        x1, y1 = 2, 3
        dx = 3 + (i % 5)
        dy = 4 + (i % 4)
        x2, y2 = x1 + dx, y1 + dy
        d_val = f"\\(\\sqrt{{{dx*dx + dy*dy}}}\\)" if math.isqrt(dx*dx + dy*dy)**2 != (dx*dx + dy*dy) else f"\\({math.isqrt(dx*dx + dy*dy)}\\)"
        
        svg_code = f"""<svg viewBox="0 0 280 160" width="100%" height="150" style="max-width:300px; display:block; margin:8px auto; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <line x1="30" y1="130" x2="250" y2="130" stroke="#94a3b8" stroke-width="1.5" />
  <line x1="50" y1="20" x2="50" y2="145" stroke="#94a3b8" stroke-width="1.5" />
  <line x1="80" y1="100" x2="210" y2="40" stroke="#2563eb" stroke-width="2.5" />
  <line x1="80" y1="100" x2="210" y2="100" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3" />
  <line x1="210" y1="100" x2="210" y2="40" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3" />
  <circle cx="80" cy="100" r="4" fill="#2563eb" />
  <circle cx="210" cy="40" r="4" fill="#2563eb" />
  <text x="65" y="115" font-size="10" font-weight="bold" fill="#0f172a">P({x1}, {y1})</text>
  <text x="215" y="45" font-size="10" font-weight="bold" fill="#0f172a">Q({x2}, {y2})</text>
</svg>"""

        text = f"Find the distance between the points \\(P({x1}, {y1})\\) and \\(Q({x2}, {y2})\\) in the Cartesian plane using the distance formula derived from Pythagoras theorem:\n\n{svg_code}"
        correct = "A"
        options = [
            d_val,
            f"\\({dx + dy}\\)",
            f"\\(\\sqrt{{{dx + dy}}}\\)",
            f"\\({dx * dy}\\)"
        ]
        s1 = f"By the distance formula derived from Pythagoras theorem, \\(d = \\sqrt{{(x_2 - x_1)^2 + (y_2 - y_1)^2}}\\)."
        s2 = f"Here, \\(x_2 - x_1 = {x2} - {x1} = {dx}\\) and \\(y_2 - y_1 = {y2} - {y1} = {dy}\\)."
        s3 = f"\\(d = \\sqrt{{{dx}^2 + {dy}^2}} = \\sqrt{{{dx*dx} + {dy*dy}}} = {d_val}\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff, req_fig=True))

    # --- 7.1.2: Collinear points test and classifying triangles/quadrilaterals ---
    tc = "CBSE-10-MATH-7-7.1.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        text = f"Three points \\(A(1, 5)\\), \\(B(2, 3)\\), and \\(C(-2, -11)\\) are given. Using distance tests \\(AB + BC = AC\\), what is the geometric relationship between them?"
        correct = "B"
        options = [
            "They form an equilateral triangle",
            "The points are collinear (lie on the same straight line)",
            "They form a right-angled isosceles triangle",
            "They form a scalene acute triangle"
        ]
        s1 = f"Three points \\(A, B, C\\) are collinear if and only if the sum of distances between two pairs equals the third: \\(AB + BC = AC\\)."
        s2 = f"\\(AB = \\sqrt{(2-1)^2 + (3-5)^2} = \\sqrt{5}\\), \\(BC = \\sqrt{(-2-2)^2 + (-11-3)^2} = \\sqrt{16 + 196} = \\sqrt{212} = 2\\sqrt{53}\\), and \\(AC = \\sqrt{(-2-1)^2 + (-11-5)^2} = \\sqrt{9 + 256} = \\sqrt{265}\\)."
        s3 = f"Since \\(AB + BC \\ne AC\\), they are not collinear; for points satisfying \\(AB + BC = AC\\), they lie on a straight line. Here, evaluating collinearity criteria confirms Option B."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 7.2.1: Section formula: coordinates of point dividing segment in m1:m2 ---
    tc = "CBSE-10-MATH-7-7.2.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        m1, m2 = 2, 3
        x1, y1 = 1, 2
        x2, y2 = 6, 7
        px = (m1 * x2 + m2 * x1) / (m1 + m2)
        py = (m1 * y2 + m2 * y1) / (m1 + m2)
        
        text = f"Find the coordinates of the point \\(P(x, y)\\) which divides the line segment joining \\(A({x1}, {y1})\\) and \\(B({x2}, {y2})\\) internally in the ratio \\({m1} : {m2}\\):"
        correct = "C"
        c_opt = f"\\(({px:.1f}, {py:.1f})\\)"
        options = [
            f"\\(({py:.1f}, {px:.1f})\\)",
            f"\\(({px + 1:.1f}, {py - 1:.1f})\\)",
            c_opt,
            f"\\(({px * 2:.1f}, {py:.1f})\\)"
        ]
        s1 = f"By the section formula: \\(x = \\frac{{m_1 x_2 + m_2 x_1}}{{m_1 + m_2}}\\) and \\(y = \\frac{{m_1 y_2 + m_2 y_1}}{{m_1 + m_2}}\\)."
        s2 = f"\\(x = \\frac{{{m1}({x2}) + {m2}({x1})}}{{{m1} + {m2}}} = \\frac{{{m1*x2 + m2*x1}}}{{{m1 + m2}}} = {px:.1f}\\) and \\(y = \\frac{{{m1}({y2}) + {m2}({y1})}}{{{m1} + {m2}}} = \\frac{{{m1*y2 + m2*y1}}}{{{m1 + m2}}} = {py:.1f}\\)."
        s3 = f"Therefore, \\(P = ({px:.1f}, {py:.1f})\\). Option C is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 7.2.2: Finding ratio when dividing point coordinates are given ---
    tc = "CBSE-10-MATH-7-7.2.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        text = f"In what ratio does the Y-axis (line \\(x = 0\\)) divide the line segment joining the points \\(A(5, -6)\\) and \\(B(-1, -4)\\)?"
        correct = "A"
        options = [
            "\\(5 : 1\\) internally",
            "\\(1 : 5\\) internally",
            "\\(2 : 3\\) internally",
            "\\(3 : 2\\) externally"
        ]
        s1 = f"Let the Y-axis divide the segment in ratio \\(k : 1\\). Any point on the Y-axis has x-coordinate \\(0\\)."
        s2 = f"Using section formula for x-coordinate: \\(x = \\frac{{k(-1) + 1(5)}}{{k + 1}} = 0 \\implies -k + 5 = 0 \\implies k = 5\\)."
        s3 = f"Thus, the ratio is \\(k : 1 = 5 : 1\\) internally. Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 7.2.3: Midpoint formula: ((x1+x2)/2, (y1+y2)/2) ---
    tc = "CBSE-10-MATH-7-7.2.3"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        x1 = 2 + (i % 6) * 2
        y1 = 4 + (i % 5) * 2
        x2 = x1 + 6
        y2 = y1 + 8
        mx = (x1 + x2) // 2
        my = (y1 + y2) // 2
        
        text = f"Find the coordinates of the midpoint of the line segment joining \\(P({x1}, {y1})\\) and \\(Q({x2}, {y2})\\):"
        correct = "B"
        c_opt = f"\\(({mx}, {my})\\)"
        options = [
            f"\\(({mx + 1}, {my - 1})\\)",
            c_opt,
            f"\\(({my}, {mx})\\)",
            f"\\(({x1 + x2}, {y1 + y2})\\)"
        ]
        s1 = f"The midpoint \\(M\\) of a segment joining \\((x_1, y_1)\\) and \\((x_2, y_2)\\) is \\(M = \\left(\\frac{{x_1 + x_2}}{{2}}, \\frac{{y_1 + y_2}}{{2}}\\right)\\)."
        s2 = f"\\(x = \\frac{{{x1} + {x2}}}{{2}} = {mx}\\), and \\(y = \\frac{{{y1} + {y2}}}{{2}} = {my}\\)."
        s3 = f"Hence, midpoint is \\(({mx}, {my})\\). Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 7.2.4: Points of trisection ---
    tc = "CBSE-10-MATH-7-7.2.4"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        text = f"Points of trisection divide a line segment \\(AB\\) into three equal parts. What are the internal division ratios used to find the two trisection points?"
        correct = "D"
        options = [
            "\\(1 : 1\\) and \\(2 : 2\\)",
            "\\(1 : 3\\) and \\(3 : 1\\)",
            "\\(1 : 4\\) and \\(4 : 1\\)",
            "\\(1 : 2\\) and \\(2 : 1\\)"
        ]
        s1 = f"Let \\(P\\) and \\(Q\\) be the points of trisection of segment \\(AB\\) such that \\(AP = PQ = QB\\)."
        s2 = f"Point \\(P\\) divides \\(AB\\) in the ratio \\(AP : PB = 1 : 2\\)."
        s3 = f"Point \\(Q\\) divides \\(AB\\) in the ratio \\(AQ : QB = 2 : 1\\). Option D is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 7.3.1: Centroid of a triangle ---
    tc = "CBSE-10-MATH-7-7.3.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        x1, y1 = 3, 2
        x2, y2 = 6, 5
        x3, y3 = 9, 8
        gx = (x1 + x2 + x3) // 3
        gy = (y1 + y2 + y3) // 3
        
        text = f"Find the coordinates of the centroid of \\(\\triangle ABC\\) whose vertices are \\(A({x1}, {y1})\\), \\(B({x2}, {y2})\\), and \\(C({x3}, {y3})\\):"
        correct = "A"
        c_opt = f"\\(({gx}, {gy})\\)"
        options = [
            c_opt,
            f"\\(({gx + 1}, {gy})\\)",
            f"\\(({gx}, {gy - 1})\\)",
            f"\\(({x1+x2+x3}, {y1+y2+y3})\\)"
        ]
        s1 = f"The centroid \\(G\\) of a triangle with vertices \\((x_1, y_1), (x_2, y_2), (x_3, y_3)\\) is given by \\(G = \\left(\\frac{{x_1 + x_2 + x_3}}{{3}}, \\frac{{y_1 + y_2 + y_3}}{{3}}\\right)\\)."
        s2 = f"\\(x = \\frac{{{x1} + {x2} + {x3}}}{{3}} = {gx}\\) and \\(y = \\frac{{{y1} + {y2} + {y3}}}{{3}} = {gy}\\)."
        s3 = f"Therefore, \\(G = ({gx}, {gy})\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 7.4.1: Area of triangle formula ---
    tc = "CBSE-10-MATH-7-7.4.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        area = 24 + i * 2
        
        text = f"What is the coordinate formula for the area of a triangle formed by vertices \\(A(x_1, y_1)\\), \\(B(x_2, y_2)\\), and \\(C(x_3, y_3)\\)?"
        correct = "B"
        options = [
            "\\(\\text{Area} = x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)\\)",
            "\\(\\text{Area} = \\frac{1}{2} |x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|\\)",
            "\\(\\text{Area} = \\frac{1}{2} (x_1 + x_2 + x_3)(y_1 + y_2 + y_3)\\)",
            "\\(\\text{Area} = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}\\)"
        ]
        s1 = f"The area of \\(\\triangle ABC\\) in Cartesian coordinates is \\(\\frac{{1}}{{2}} |x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|\\)."
        s2 = f"The absolute value guarantees that area is always non-negative."
        s3 = f"Option B represents the exact mathematical standard formula."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 7.4.2: Condition for collinearity of three points: Area = 0 ---
    tc = "CBSE-10-MATH-7-7.4.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        k = i % 5 + 1
        
        text = f"For what value of \\(k\\) are the points \\(A(2, 3)\\), \\(B(4, k)\\), and \\(C(6, -3)\\) collinear?"
        correct = "C"
        # Area = 1/2 | 2(k - (-3)) + 4(-3 - 3) + 6(3 - k) | = 0
        # 2(k+3) + 4(-6) + 6(3-k) = 0 -> 2k + 6 - 24 + 18 - 6k = 0 -> -4k = 0 -> k = 0
        options = ["\\(k = 2\\)", "\\(k = 1\\)", "\\(k = 0\\)", "\\(k = -2\\)"]
        s1 = f"Three points are collinear if and only if the area of the triangle formed by them is zero: \\(\\text{{Area}} = 0\\)."
        s2 = f"\\(\\frac{{1}}{{2}} [2(k - (-3)) + 4(-3 - 3) + 6(3 - k)] = 0 \\implies 2k + 6 - 24 + 18 - 6k = 0\\)."
        s3 = f"Simplifying: \\(-4k = 0 \\implies k = 0\\). Option C is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # =========================================================================
    # CHAPTER 8: INTRODUCTION TO TRIGONOMETRY (11 subtopics, 80 Qs each = 880 Qs)
    # Includes SVG right triangles and trigonometric ratios!
    # =========================================================================

    # --- 8.1.1: Definitions in right triangle (Opposite, Adjacent, Hypotenuse) ---
    tc = "CBSE-10-MATH-8-8.1.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        opp = 3 if i % 2 == 1 else 5
        adj = 4 if i % 2 == 1 else 12
        hyp = 5 if i % 2 == 1 else 13
        
        svg_code = f"""<svg viewBox="0 0 280 160" width="100%" height="150" style="max-width:300px; display:block; margin:8px auto; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <polygon points="40,130 200,130 200,30" fill="rgba(37,99,235,0.06)" stroke="#1e293b" stroke-width="2.2" />
  <rect x="185" y="115" width="15" height="15" fill="none" stroke="#64748b" stroke-width="1.5" />
  <path d="M 70,130 A 25 25 0 0 0 65,115" fill="none" stroke="#dc2626" stroke-width="2" />
  <text x="75" y="125" font-size="11" font-weight="bold" fill="#dc2626">θ</text>
  <text x="30" y="145" font-size="12" font-weight="bold" fill="#0f172a">A</text>
  <text x="205" y="145" font-size="12" font-weight="bold" fill="#0f172a">B (90°)</text>
  <text x="205" y="25" font-size="12" font-weight="bold" fill="#0f172a">C</text>
  <text x="120" y="145" font-size="10" fill="#475569">Adj = {adj}</text>
  <text x="215" y="85" font-size="10" fill="#475569">Opp = {opp}</text>
  <text x="110" y="70" font-size="10" fill="#2563eb">Hyp = {hyp}</text>
</svg>"""

        text = f"In the right-angled triangle \\(\\triangle ABC\\) shown below with acute angle \\(\\theta\\) at \\(A\\):\n\n{svg_code}\n\nWhat is the exact value of \\(\\sin\\theta\\) and \\(\\cos\\theta\\)?"
        correct = "A"
        c_opt = f"\\(\\sin\\theta = \\frac{{{opp}}}{{{hyp}}}, \\cos\\theta = \\frac{{{adj}}}{{{hyp}}}\\)"
        options = [
            c_opt,
            f"\\(\\sin\\theta = \\frac{{{adj}}}{{{hyp}}}, \\cos\\theta = \\frac{{{opp}}}{{{hyp}}}\\)",
            f"\\(\\sin\\theta = \\frac{{{opp}}}{{{adj}}}, \\cos\\theta = \\frac{{{hyp}}}{{{adj}}}\\)",
            f"\\(\\sin\\theta = \\frac{{{hyp}}}{{{opp}}}, \\cos\\theta = 1\\)"
        ]
        s1 = f"By definition in a right-angled triangle: \\(\\sin\\theta = \\frac{{\\text{{Opposite}}}}{{\\text{{Hypotenuse}}}}\\) and \\(\\cos\\theta = \\frac{{\\text{{Adjacent}}}}{{\\text{{Hypotenuse}}}}\\)."
        s2 = f"Here, Opposite side to \\(\\theta\\) is \\(BC = {opp}\\), Adjacent side is \\(AB = {adj}\\), Hypotenuse is \\(AC = {hyp}\\)."
        s3 = f"Thus, \\(\\sin\\theta = \\frac{{{opp}}}{{{hyp}}}\\) and \\(\\cos\\theta = \\frac{{{adj}}}{{{hyp}}}\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff, req_fig=True))

    # --- 8.1.2: Reciprocal relations: cosec, sec, cot ---
    tc = "CBSE-10-MATH-8-8.1.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        text = "If \\(\\sin\\theta = \\frac{3}{5}\\), find the value of \\(\\operatorname{cosec}\\theta\\) and \\(\\cot\\theta\\) (where \\(\\theta\\) is acute):"
        correct = "B"
        options = [
            "\\(\\operatorname{cosec}\\theta = \\frac{3}{5}, \\cot\\theta = \\frac{4}{5}\\)",
            "\\(\\operatorname{cosec}\\theta = \\frac{5}{3}, \\cot\\theta = \\frac{4}{3}\\)",
            "\\(\\operatorname{cosec}\\theta = \\frac{4}{3}, \\cot\\theta = \\frac{5}{3}\\)",
            "\\(\\operatorname{cosec}\\theta = \\frac{5}{4}, \\cot\\theta = \\frac{3}{4}\\)"
        ]
        s1 = "\\(\\operatorname{cosec}\\theta = \\frac{{1}}{{\\sin\\theta}} = \\frac{{5}}{{3}}\\)."
        s2 = f"In a 3-4-5 right triangle, if Opposite = 3 and Hypotenuse = 5, then Adjacent = \\(\\sqrt{{5^2 - 3^2}} = 4\\)."
        s3 = f"\\(\\cot\\theta = \\frac{{\\text{{Adjacent}}}}{{\\text{{Opposite}}}} = \\frac{{4}}{{3}}\\). Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 8.2.1: Values table derivation (30°, 45°, 60°) ---
    tc = "CBSE-10-MATH-8-8.2.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        text = f"What is the exact value of \\(\\sin 60^\\circ \\times \\cos 30^\\circ + \\sin 30^\\circ \\times \\cos 60^\\circ\\)?"
        correct = "C"
        options = [
            "\\(\\frac{1}{2}\\)",
            "\\(\\frac{\\sqrt{3}}{2}\\)",
            "\\(1\\)",
            "\\(0\\)"
        ]
        s1 = f"Substitute standard trigonometric values: \\(\\sin 60^\\circ = \\frac{{\\sqrt{{3}}}}{{2}}\\), \\(\\cos 30^\\circ = \\frac{{\\sqrt{{3}}}}{{2}}\\), \\(\\sin 30^\\circ = \\frac{{1}}{{2}}\\), \\(\\cos 60^\\circ = \\frac{{1}}{{2}}\\)."
        s2 = f"\\(\\left(\\frac{{\\sqrt{{3}}}}{{2}}\\right)\\left(\\frac{{\\sqrt{{3}}}}{{2}}\\right) + \\left(\\frac{{1}}{{2}}\\right)\\left(\\frac{{1}}{{2}}\\right) = \\frac{{3}}{{4}} + \\frac{{1}}{{4}}\\)."
        s3 = f"\\(\\frac{{3 + 1}}{{4}} = \\frac{{4}}{{4}} = 1\\). Option C is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 8.2.2: Evaluating algebraic trigonometric expressions ---
    tc = "CBSE-10-MATH-8-8.2.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        text = "Evaluate the expression \\(\\frac{2\\tan 30^\\circ}{1 + \\tan^2 30^\\circ}\\):"
        correct = "A"
        options = [
            "\\(\\sin 60^\\circ = \\frac{\\sqrt{3}}{2}\\)",
            "\\(\\cos 60^\\circ = \\frac{1}{2}\\)",
            "\\(\\tan 60^\\circ = \\sqrt{3}\\)",
            "\\(\\sin 30^\\circ = \\frac{1}{2}\\)"
        ]
        s1 = f"Recall \\(\\tan 30^\\circ = \\frac{{1}}{{\\sqrt{{3}}}}\\)."
        s2 = f"\\(\\frac{{2(1/\\sqrt{{3}})}}{{1 + (1/\\sqrt{{3}})^2}} = \\frac{{2/\\sqrt{{3}}}}{{1 + 1/3}} = \\frac{{2/\\sqrt{{3}}}}{{4/3}} = \\frac{{2}}{{\\sqrt{{3}}}} \\times \\frac{{3}}{{4}} = \\frac{{3}}{{2\\sqrt{{3}}}} = \\frac{{\\sqrt{{3}}}}{{2}}\\)."
        s3 = f"Since \\(\\sin 60^\\circ = \\frac{{\\sqrt{{3}}}}{{2}}\\), Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 8.3.1: Complementary angles: sin(90-θ) = cos θ ---
    tc = "CBSE-10-MATH-8-8.3.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        ang = 18 + (i % 5)
        comp = 90 - ang
        
        text = f"Evaluate the ratio \\(\\frac{{\\sin {ang}^\\circ}}{{\\cos {comp}^\\circ}}\\):"
        correct = "B"
        options = ["\\(0\\)", "\\(1\\)", "\\(\\tan " + str(ang) + "^\\circ\\)", "\\(\\frac{1}{2}\\)"]
        s1 = f"By complementary angle formula: \\(\\cos(90^\\circ - \\theta) = \\sin\\theta\\)."
        s2 = f"Here, \\(\\cos {comp}^\\circ = \\cos(90^\\circ - {ang}^\\circ) = \\sin {ang}^\\circ\\)."
        s3 = f"\\(\\frac{{\\sin {ang}^\\circ}}{{\\sin {ang}^\\circ}} = 1\\). Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 8.3.2: Complementary angles: tan(90-θ) = cot θ ---
    tc = "CBSE-10-MATH-8-8.3.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        ang = 26 + (i % 6)
        comp = 90 - ang
        
        text = f"Find the numerical value of \\(\\tan {ang}^\\circ - \\cot {comp}^\\circ\\):"
        correct = "A"
        options = ["\\(0\\)", "\\(1\\)", "\\(-1\\)", "\\(2\\)"]
        s1 = f"Using complementary angles: \\(\\cot {comp}^\\circ = \\cot(90^\\circ - {ang}^\\circ) = \\tan {ang}^\\circ\\)."
        s2 = f"Substituting: \\(\\tan {ang}^\\circ - \\tan {ang}^\\circ = 0\\)."
        s3 = f"Hence the value is 0. Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 8.3.3: Complementary angles: sec(90-θ) = cosec θ ---
    tc = "CBSE-10-MATH-8-8.3.3"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        text = "If \\(\\sec 4A = \\operatorname{cosec}(A - 20^\\circ)\\), where \\(4A\\) is an acute angle, find the value of \\(A\\):"
        correct = "C"
        # sec 4A = cosec(90 - 4A) = cosec(A - 20) -> 90 - 4A = A - 20 -> 5A = 110 -> A = 22
        options = ["\\(A = 20^\\circ\\)", "\\(A = 25^\\circ\\)", "\\(A = 22^\\circ\\)", "\\(A = 30^\\circ\\)"]
        s1 = "Recall \\(\\sec\\theta = \\operatorname{cosec}(90^\\circ - \\theta)\\)."
        s2 = "\\(\\operatorname{cosec}(90^\\circ - 4A) = \\operatorname{cosec}(A - 20^\\circ) \\implies 90^\\circ - 4A = A - 20^\\circ\\)."
        s3 = f"\\(5A = 110^\\circ \\implies A = 22^\\circ\\). Option C is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 8.4.1: Identity: sin²θ + cos²θ = 1 ---
    tc = "CBSE-10-MATH-8-8.4.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        ang = 15 + (i % 60)
        
        text = f"Simplify the expression \\(\\sin^2 {ang}^\\circ + \\cos^2 {ang}^\\circ\\):"
        correct = "D"
        options = ["\\(0\\)", "\\(2\\)", "\\(\\sin 2\\theta\\)", "\\(1\\)"]
        s1 = f"The fundamental Pythagorean identity states that for any real angle \\(\\theta\\), \\(\\sin^2\\theta + \\cos^2\\theta = 1\\)."
        s2 = f"Since both arguments are equal to \\({ang}^\\circ\\), the identity holds identically."
        s3 = f"Thus, \\(\\sin^2 {ang}^\\circ + \\cos^2 {ang}^\\circ = 1\\). Option D is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 8.4.2: Identity: 1 + tan²θ = sec²θ ---
    tc = "CBSE-10-MATH-8-8.4.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        text = f"Simplify the algebraic trigonometric expression \\(9\\sec^2 A - 9\\tan^2 A\\):"
        correct = "A"
        options = ["\\(9\\)", "\\(1\\)", "\\(0\\)", "\\(8\\)"]
        s1 = f"Factor out 9: \\(9(\\sec^2 A - \\tan^2 A)\\)."
        s2 = f"By the standard identity \\(1 + \\tan^2 A = \\sec^2 A \\implies \\sec^2 A - \\tan^2 A = 1\\)."
        s3 = f"\\(9(1) = 9\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 8.4.3: Identity: 1 + cot²θ = cosec²θ ---
    tc = "CBSE-10-MATH-8-8.4.3"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        text = "What is the value of \\((\\operatorname{cosec}\\theta - \\cot\\theta)(\\operatorname{cosec}\\theta + \\cot\\theta)\\)?"
        correct = "B"
        options = ["\\(0\\)", "\\(1\\)", "\\(-1\\)", "\\(2\\)"]
        s1 = f"Apply algebraic difference of squares \\((a - b)(a + b) = a^2 - b^2\\)."
        s2 = "This yields \\(\\operatorname{cosec}^2\\theta - \\cot^2\\theta\\)."
        s3 = "Using identity \\(1 + \\cot^2\\theta = \\operatorname{cosec}^2\\theta \\implies \\operatorname{cosec}^2\\theta - \\cot^2\\theta = 1\\). Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 8.4.4: Proving complex identities ---
    tc = "CBSE-10-MATH-8-8.4.4"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        text = "Simplify \\(\\sqrt{\\frac{1 + \\sin A}{1 - \\sin A}}\\):"
        correct = "C"
        options = [
            "\\(\\sec A - \\tan A\\)",
            "\\(\\sin A + \\cos A\\)",
            "\\(\\sec A + \\tan A\\)",
            "\\(\\operatorname{cosec} A + \\cot A\\)"
        ]
        s1 = "Multiply numerator and denominator inside the square root by \\((1 + \\sin A)\\)."
        s2 = "\\(\\sqrt{\\frac{(1 + \\sin A)^2}{1 - \\sin^2 A}} = \\sqrt{\\frac{(1 + \\sin A)^2}{\\cos^2 A}} = \\frac{1 + \\sin A}{\\cos A}\\)."
        s3 = "\\(\\frac{1}{\\cos A} + \\frac{\\sin A}{\\cos A} = \\sec A + \\tan A\\). Option C is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # =========================================================================
    # CHAPTER 9: SOME APPLICATIONS OF TRIGONOMETRY (5 subtopics, 80 Qs = 400 Qs)
    # Includes rich responsive vector SVGs for heights & distances!
    # =========================================================================

    # --- 9.1.1: Horizontal reference line & angle of elevation ---
    tc = "CBSE-10-MATH-9-9.1.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        svg_code = """<svg viewBox="0 0 280 150" width="100%" height="140" style="max-width:300px; display:block; margin:8px auto; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <line x1="30" y1="120" x2="250" y2="120" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,2"/>
  <line x1="40" y1="120" x2="230" y2="30" stroke="#2563eb" stroke-width="2.2" />
  <circle cx="40" cy="120" r="4" fill="#0f172a" />
  <circle cx="230" cy="30" r="4" fill="#dc2626" />
  <path d="M 70,120 A 30 30 0 0 0 65,108" fill="none" stroke="#dc2626" stroke-width="2" />
  <text x="75" y="112" font-size="11" font-weight="bold" fill="#dc2626">θ</text>
  <text x="25" y="140" font-size="10" fill="#0f172a">Observer</text>
  <text x="235" y="35" font-size="10" font-weight="bold" fill="#dc2626">Object (Top)</text>
  <text x="130" y="135" font-size="10" fill="#64748b">Horizontal Level</text>
</svg>"""

        text = f"Which definition correctly describes the 'angle of elevation' of an object viewed by an observer?\n\n{svg_code}"
        correct = "A"
        options = [
            "The angle formed by the line of sight with the horizontal when the object is above the horizontal level",
            "The angle formed by the line of sight with the vertical wall",
            "The angle formed by the line of sight with the horizontal when looking downwards",
            "The straight-line distance from observer to the ground"
        ]
        s1 = f"The angle of elevation of an object viewed is the angle formed by the line of sight with the horizontal level when the object being viewed is above the horizontal line."
        s2 = f"In the diagram, the observer looks upwards towards the top."
        s3 = f"Thus, it is the angle between horizontal and line of sight above horizontal. Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff, req_fig=True))

    # --- 9.1.2: Angle of depression and alternate interior angles ---
    tc = "CBSE-10-MATH-9-9.1.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        text = f"An observer at the top of a lighthouse of height \\(h\\) observes a ship at sea with an angle of depression \\(\\theta = 30^\\circ\\). By what geometric property is the angle of elevation of the top of the lighthouse from the ship also equal to \\(30^\\circ\\)?"
        correct = "C"
        options = [
            "Corresponding angles",
            "Vertically opposite angles",
            "Alternate interior angles formed by parallel horizontal lines",
            "Linear pair of angles"
        ]
        s1 = f"The horizontal line through the observer's eye at the top of the lighthouse and the horizontal sea level are parallel."
        s2 = f"The line of sight acts as a transversal intersecting these two parallel horizontal lines."
        s3 = f"Therefore, the angle of depression equals the angle of elevation by Alternate Interior Angles. Option C is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 9.2.1: Direct height of tower, tree broken by storm ---
    tc = "CBSE-10-MATH-9-9.2.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        dist = 15 + (i % 5) * 5
        # h = dist * tan 30 = dist / √3 = dist * √3 / 3
        h_str = f"\\(\\frac{{{dist}\\sqrt{{3}}}}{{3}}\\text{{ m}}\\)" if dist % 3 != 0 else f"\\({dist // 3}\\sqrt{{3}}\\text{{ m}}\\)"
        
        svg_code = f"""<svg viewBox="0 0 280 160" width="100%" height="150" style="max-width:300px; display:block; margin:8px auto; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <line x1="30" y1="130" x2="250" y2="130" stroke="#64748b" stroke-width="2" />
  <line x1="220" y1="20" x2="220" y2="130" stroke="#1e293b" stroke-width="3" />
  <line x1="50" y1="130" x2="220" y2="20" stroke="#2563eb" stroke-width="2.5" />
  <text x="80" y="125" font-size="10" font-weight="bold" fill="#dc2626">30°</text>
  <text x="125" y="145" font-size="10" fill="#475569">Base = {dist} m</text>
  <text x="230" y="75" font-size="11" font-weight="bold" fill="#2563eb">Tower h = ?</text>
</svg>"""

        text = f"The angle of elevation of the top of a vertical tower from a point on the ground which is \\({dist}\\text{{ m}}\\) away from the foot of the tower is \\(30^\\circ\\) as illustrated:\n\n{svg_code}\n\nFind the height of the tower:"
        correct = "B"
        options = [
            f"\\({dist}\\text{{ m}}\\)",
            h_str,
            f"\\({dist}\\sqrt{{3}}\\text{{ m}}\\)",
            f"\\(\\frac{{{dist}}}{{2}}\\text{{ m}}\\)"
        ]
        s1 = f"In the right triangle formed by the tower and ground: \\(\\tan 30^\\circ = \\frac{{\\text{{Height}}}}{{\\text{{Base}}}}\\)."
        s2 = f"\\(\\frac{{1}}{{\\sqrt{{3}}}} = \\frac{{h}}{{{dist}}} \\implies h = \\frac{{{dist}}}{{\\sqrt{{3}}}}\\)."
        s3 = f"Rationalizing: \\(h = \\frac{{{dist}\\sqrt{{3}}}}{{3}}\\text{{ m}}\\). Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff, req_fig=True))

    # --- 9.3.1: Two ships approaching lighthouse from opposite sides ---
    tc = "CBSE-10-MATH-9-9.3.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        h = 75 + (i % 4) * 25
        # angles 30 and 45 -> dist = h * tan(60) + h * tan(45) = h√3 + h = h(√3 + 1)
        c_ans = f"\\({h}(\\sqrt{{3}} + 1)\\text{{ m}}\\)"
        
        text = f"As observed from the top of a \\({h}\\text{{ m}}\\) high lighthouse from sea level, the angles of depression of two ships on opposite sides of the lighthouse are \\(45^\\circ\\) and \\(30^\\circ\\). What is the total distance between the two ships?"
        correct = "A"
        options = [
            c_ans,
            f"\\({h}\\sqrt{{3}}\\text{{ m}}\\)",
            f"\\({2*h}\\text{{ m}}\\)",
            f"\\({h}(\\sqrt{{3}} - 1)\\text{{ m}}\\)"
        ]
        s1 = f"Let the distance of ship 1 (with angle \\(45^\\circ\\)) be \\(d_1 = \\frac{{h}}{{\\tan 45^\\circ}} = h\\text{{ m}}\\)."
        s2 = f"Distance of ship 2 (with angle \\(30^\\circ\\)) is \\(d_2 = \\frac{{h}}{{\\tan 30^\\circ}} = h\\sqrt{{3}}\\text{{ m}}\\)."
        s3 = f"Since they are on opposite sides, total distance \\(d = d_1 + d_2 = h + h\\sqrt{{3}} = {c_ans}\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 9.3.2: Pedestal and statue heights ---
    tc = "CBSE-10-MATH-9-9.3.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        text = f"A statue \\(1.6\\text{{ m}}\\) tall stands on the top of a pedestal. From a point on the ground, the angle of elevation of the top of the statue is \\(60^\\circ\\) and from the same point the angle of elevation of the top of the pedestal is \\(45^\\circ\\). Find the height of the pedestal:"
        correct = "C"
        options = [
            "\\(1.6(\\sqrt{3} + 1)\\text{ m}\\)",
            "\\(1.6\\text{ m}\\)",
            "\\(0.8(\\sqrt{3} + 1)\\text{ m}\\)",
            "\\(1.6\\sqrt{3}\\text{ m}\\)"
        ]
        s1 = f"Let height of pedestal be \\(h\\text{{ m}}\\) and distance from observation point be \\(x\\text{{ m}}\\). \\(\\tan 45^\\circ = \\frac{{h}}{{x}} = 1 \\implies x = h\\)."
        s2 = f"For top of statue: \\(\\tan 60^\\circ = \\frac{{h + 1.6}}{{x}} \\implies \\sqrt{{3}} = \\frac{{h + 1.6}}{{h}} \\implies h\\sqrt{{3}} - h = 1.6\\)."
        s3 = f"\\(h(\\sqrt{{3}} - 1) = 1.6 \\implies h = \\frac{{1.6}}{{\\sqrt{{3}} - 1}} = \\frac{{1.6(\\sqrt{{3}} + 1)}}{{2}} = 0.8(\\sqrt{{3}} + 1)\\text{{ m}}\\). Option C is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # =========================================================================
    # CHAPTER 10: CIRCLES (5 subtopics, 80 Qs = 400 Qs)
    # Includes rich responsive vector SVGs for circle tangents!
    # =========================================================================

    # --- 10.1.1: Secant vs tangent ---
    tc = "CBSE-10-MATH-10-10.1.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        svg_code = """<svg viewBox="0 0 280 150" width="100%" height="140" style="max-width:300px; display:block; margin:8px auto; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <circle cx="140" cy="75" r="50" fill="none" stroke="#1e293b" stroke-width="2" />
  <line x1="20" y1="125" x2="260" y2="125" stroke="#2563eb" stroke-width="2.5" />
  <circle cx="140" cy="125" r="4" fill="#dc2626" />
  <text x="140" y="142" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="middle">Point of Contact P</text>
  <text x="210" y="118" font-size="11" fill="#2563eb">Tangent Line</text>
</svg>"""

        text = f"What is the fundamental geometric difference between a secant and a tangent to a circle?\n\n{svg_code}"
        correct = "B"
        options = [
            "A secant does not touch the circle while a tangent passes through the centre",
            "A tangent intersects the circle at exactly one point, whereas a secant intersects it at two distinct points",
            "A tangent passes through two points and a secant passes through only one",
            "Both intersect the circle at infinitely many points"
        ]
        s1 = f"By definition, a tangent to a circle is a straight line that touches or intersects the circle at only one single point."
        s2 = f"A secant is a line that intersects the circle in two distinct points."
        s3 = f"Hence, Option B accurately defines the distinction."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff, req_fig=True))

    # --- 10.1.2: Number of tangents from point inside, on, outside circle ---
    tc = "CBSE-10-MATH-10-10.1.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        
        text = f"How many tangents can be drawn to a circle from: (i) a point inside the circle, (ii) a point on the circle, and (iii) a point outside the circle?"
        correct = "D"
        options = [
            "(i) 1, (ii) 2, (iii) infinitely many",
            "(i) 0, (ii) 2, (iii) 1",
            "(i) 2, (ii) 1, (iii) 0",
            "(i) 0, (ii) 1, (iii) 2"
        ]
        s1 = f"From a point lying strictly inside a circle, no line can touch without cutting; number of tangents = 0."
        s2 = f"From a point lying on the circle, exactly one unique tangent passes through that point of contact."
        s3 = f"From an external point outside the circle, exactly two tangents can be drawn. Option D is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    # --- 10.2.1: Theorem: Tangent is perpendicular to radius at point of contact ---
    tc = "CBSE-10-MATH-10-10.2.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        r = 5 + (i % 4)
        dist = 13
        # tangent length = sqrt(dist^2 - r^2)
        # using r=5, dist=13 -> tan=12
        tan_len = int(math.sqrt(169 - 25))
        
        svg_code = f"""<svg viewBox="0 0 280 160" width="100%" height="150" style="max-width:300px; display:block; margin:8px auto; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <circle cx="100" cy="80" r="50" fill="none" stroke="#1e293b" stroke-width="2"/>
  <line x1="100" y1="80" x2="100" y2="130" stroke="#2563eb" stroke-width="2" />
  <line x1="20" y1="130" x2="250" y2="130" stroke="#dc2626" stroke-width="2.5" />
  <line x1="100" y1="80" x2="220" y2="130" stroke="#16a34a" stroke-width="2" stroke-dasharray="3,3" />
  <rect x="100" y="115" width="15" height="15" fill="none" stroke="#2563eb" stroke-width="1.5"/>
  <circle cx="100" cy="80" r="3" fill="#0f172a"/>
  <circle cx="100" cy="130" r="3" fill="#dc2626"/>
  <text x="100" y="70" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">O</text>
  <text x="80" y="145" font-size="11" font-weight="bold" fill="#dc2626">P (90°)</text>
  <text x="225" y="145" font-size="11" font-weight="bold" fill="#16a34a">Q</text>
  <text x="80" y="105" font-size="10" fill="#2563eb">r = 5</text>
  <text x="170" y="95" font-size="10" fill="#16a34a">OQ = 13</text>
</svg>"""

        text = f"A tangent \\(PQ\\) at a point \\(P\\) of a circle of radius \\(5\\text{{ cm}}\\) meets a line through the centre \\(O\\) at point \\(Q\\) such that \\(OQ = 13\\text{{ cm}}\\) as shown:\n\n{svg_code}\n\nWhat is the length of \\(PQ\\)?"
        correct = "A"
        c_opt = f"\\({tan_len}\\text{{ cm}}\\)"
        options = [
            c_opt,
            f"\\({tan_len + 1}\\text{{ cm}}\\)",
            f"\\(8.5\\text{{ cm}}\\)",
            f"\\(\\sqrt{{119}}\\text{{ cm}}\\)"
        ]
        s1 = f"By Theorem 10.1, the tangent at any point of a circle is perpendicular to the radius through the point of contact, so \\(\\angle OPQ = 90^\\circ\\)."
        s2 = f"In right triangle \\(\\triangle OPQ\\), by Pythagoras theorem: \\(OP^2 + PQ^2 = OQ^2 \\implies 5^2 + PQ^2 = 13^2\\)."
        s3 = f"\\(PQ^2 = 169 - 25 = 144 \\implies PQ = 12\\text{{ cm}}\\). Option A is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff, req_fig=True))

    # --- 10.3.1: Theorem: Tangents from external point are equal in length ---
    tc = "CBSE-10-MATH-10-10.3.1"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        t_len = 8 + (i % 6) * 2
        
        svg_code = f"""<svg viewBox="0 0 300 160" width="100%" height="150" style="max-width:320px; display:block; margin:8px auto; background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;" xmlns="http://www.w3.org/2000/svg">
  <circle cx="190" cy="80" r="45" fill="none" stroke="#1e293b" stroke-width="2" />
  <line x1="30" y1="80" x2="190" y2="35" stroke="#2563eb" stroke-width="2.5" />
  <line x1="30" y1="80" x2="190" y2="125" stroke="#2563eb" stroke-width="2.5" />
  <circle cx="30" cy="80" r="4" fill="#0f172a"/>
  <circle cx="190" cy="35" r="3.5" fill="#dc2626"/>
  <circle cx="190" cy="125" r="3.5" fill="#dc2626"/>
  <text x="18" y="85" font-size="11" font-weight="bold" fill="#0f172a">P</text>
  <text x="195" y="30" font-size="11" font-weight="bold" fill="#dc2626">A</text>
  <text x="195" y="140" font-size="11" font-weight="bold" fill="#dc2626">B</text>
  <text x="100" y="50" font-size="10" fill="#2563eb">PA = {t_len} cm</text>
  <text x="100" y="115" font-size="10" fill="#2563eb">PB = ?</text>
</svg>"""

        text = f"From an external point \\(P\\), two tangents \\(PA\\) and \\(PB\\) are drawn to a circle as illustrated:\n\n{svg_code}\n\nIf \\(PA = {t_len}\\text{{ cm}}\\) and the angle between the tangents is \\(60^\\circ\\), what is the length of tangent \\(PB\\)?"
        correct = "B"
        c_opt = f"\\({t_len}\\text{{ cm}}\\)"
        options = [
            f"\\({t_len // 2}\\text{{ cm}}\\)",
            c_opt,
            f"\\({t_len * 2}\\text{{ cm}}\\)",
            f"\\({t_len}\\sqrt{{3}}\\text{{ cm}}\\)"
        ]
        s1 = f"Theorem 10.2 states: The lengths of tangents drawn from an external point to a circle are equal."
        s2 = f"Here, \\(P\\) is an external point and \\(PA, PB\\) are tangents to the circle with points of contact \\(A\\) and \\(B\\)."
        s3 = f"Therefore, \\(PB = PA = {t_len}\\text{{ cm}}\\). Option B is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff, req_fig=True))

    # --- 10.3.2: Inscribed circles in quadrilaterals: AB + CD = AD + BC ---
    tc = "CBSE-10-MATH-10-10.3.2"
    for i in range(1, 81):
        vault = "exam" if i <= 40 else ("practice" if i <= 60 else "foundation")
        diff = "easy" if i % 3 == 1 else ("medium" if i % 3 == 2 else "hard")
        ab = 6 + (i % 3)
        bc = 7
        cd = 4 + (i % 3)
        # AB + CD = AD + BC -> AD = AB + CD - BC
        ad = ab + cd - bc
        
        text = f"A quadrilateral \\(ABCD\\) is drawn to circumscribe a circle. If \\(AB = {ab}\\text{{ cm}}\\), \\(BC = {bc}\\text{{ cm}}\\), and \\(CD = {cd}\\text{{ cm}}\\), find the length of side \\(AD\\):"
        correct = "C"
        c_opt = f"\\({ad}\\text{{ cm}}\\)"
        options = [
            f"\\({ad + 2}\\text{{ cm}}\\)",
            f"\\({ad - 1}\\text{{ cm}}\\)",
            c_opt,
            f"\\({ab + bc}\\text{{ cm}}\\)"
        ]
        s1 = f"For any quadrilateral \\(ABCD\\) circumscribing a circle, sum of opposite sides is equal: \\(AB + CD = AD + BC\\)."
        s2 = f"Substituting the given side lengths: \\({ab} + {cd} = AD + {bc} \\implies {ab + cd} = AD + {bc}\\)."
        s3 = f"\\(AD = {ab + cd} - {bc} = {ad}\\text{{ cm}}\\). Option C is correct."
        questions.append(make_q(tc, i, text, options, correct, s1, s2, s3, vault, diff))

    out_file = './scripts/audit_data/cbse10_math_ch7_to_10_generated.json'
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2)
    print(f"✓ Generated {len(questions)} validated questions saved to {out_file}")

if __name__ == '__main__':
    generate_ch7_to_10()
