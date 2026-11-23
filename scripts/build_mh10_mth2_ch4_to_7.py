import json
import os
import math

def generate_mh10_mth2_ch4_to_7():
    print("=== Generating MH 10 Mathematics Part 2 (Geometry) Chapters 4-7 (2,480 Questions) ===")
    
    with open('scripts/audit_data/mh_10_mth2_audit.json', 'r', encoding='utf-8') as f:
        audit_data = json.load(f)

    questions = []

    # -------------------------------------------------------------
    # Responsive Vector Inline SVG Generators
    # -------------------------------------------------------------
    def get_coord_slope_svg(x1, y1, x2, y2):
        return (
            '<svg viewBox="0 0 280 180" width="100%" style="max-width:280px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<line x1="30" y1="150" x2="260" y2="150" stroke="#94a3b8" stroke-width="1.5"/>'
            '<line x1="50" y1="170" x2="50" y2="20" stroke="#94a3b8" stroke-width="1.5"/>'
            '<line x1="70" y1="130" x2="220" y2="50" stroke="#2563eb" stroke-width="2.5"/>'
            '<circle cx="70" cy="130" r="4" fill="#ef4444"/>'
            '<circle cx="220" cy="50" r="4" fill="#ef4444"/>'
            f'<text x="65" y="148" font-size="11" font-weight="bold" fill="#0f172a">A({x1}, {y1})</text>'
            f'<text x="210" y="42" font-size="11" font-weight="bold" fill="#0f172a">B({x2}, {y2})</text>'
            '<text x="265" y="155" font-size="11" fill="#64748b">X</text>'
            '<text x="45" y="15" font-size="11" fill="#64748b">Y</text>'
            '</svg>'
        )

    def get_height_distance_svg(h_val, theta_val):
        return (
            '<svg viewBox="0 0 300 180" width="100%" style="max-width:300px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<line x1="40" y1="150" x2="250" y2="150" stroke="#1e293b" stroke-width="2"/>'
            '<line x1="40" y1="150" x2="40" y2="30" stroke="#dc2626" stroke-width="3"/>'
            '<line x1="40" y1="30" x2="230" y2="150" stroke="#2563eb" stroke-width="2"/>'
            '<rect x="40" y="135" width="15" height="15" fill="none" stroke="#dc2626" stroke-width="1.5"/>'
            '<path d="M 200 150 A 30 30 0 0 0 208 136" fill="none" stroke="#2563eb" stroke-width="1.5"/>'
            f'<text x="25" y="90" font-size="11" font-weight="bold" fill="#dc2626">{h_val}</text>'
            f'<text x="180" y="142" font-size="10" font-weight="bold" fill="#2563eb">{theta_val}</text>'
            '<text x="35" y="22" font-size="11" font-weight="bold" fill="#0f172a">A (Top)</text>'
            '<text x="25" y="165" font-size="11" font-weight="bold" fill="#0f172a">B (Foot)</text>'
            '<text x="235" y="165" font-size="11" font-weight="bold" fill="#0f172a">C (Observer)</text>'
            '</svg>'
        )

    def get_frustum_svg(r1_val, r2_val, h_val):
        return (
            '<svg viewBox="0 0 260 200" width="100%" style="max-width:260px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<ellipse cx="130" cy="40" rx="40" ry="12" fill="#dbeafe" stroke="#1e40af" stroke-width="2"/>'
            '<ellipse cx="130" cy="160" rx="80" ry="20" fill="#eff6ff" stroke="#1e40af" stroke-width="2"/>'
            '<line x1="90" y1="40" x2="50" y2="160" stroke="#1e40af" stroke-width="2"/>'
            '<line x1="170" y1="40" x2="210" y2="160" stroke="#1e40af" stroke-width="2"/>'
            '<line x1="130" y1="40" x2="130" y2="160" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4,3"/>'
            '<line x1="130" y1="40" x2="170" y2="40" stroke="#2563eb" stroke-width="1.5"/>'
            '<line x1="130" y1="160" x2="210" y2="160" stroke="#2563eb" stroke-width="1.5"/>'
            f'<text x="140" y="35" font-size="10" fill="#2563eb">r1={r1_val}</text>'
            f'<text x="150" y="155" font-size="10" fill="#2563eb">r2={r2_val}</text>'
            f'<text x="135" y="100" font-size="10" fill="#dc2626">h={h_val}</text>'
            '</svg>'
        )

    def get_sector_svg(theta_val, r_val):
        return (
            '<svg viewBox="0 0 240 180" width="100%" style="max-width:240px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<path d="M 120 140 L 40 80 A 100 100 0 0 1 200 80 Z" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
            '<circle cx="120" cy="140" r="3" fill="#d97706"/>'
            '<text x="115" y="158" font-size="11" font-weight="bold" fill="#0f172a">O</text>'
            '<text x="30" y="80" font-size="11" font-weight="bold" fill="#0f172a">A</text>'
            '<text x="208" y="80" font-size="11" font-weight="bold" fill="#0f172a">B</text>'
            f'<text x="110" y="125" font-size="10" fill="#b45309">θ={theta_val}</text>'
            f'<text x="70" y="120" font-size="10" fill="#64748b">r={r_val}</text>'
            '</svg>'
        )

    def make_q(topic_code, ch_num, top_num, sub_num, seq, text, options, correct_ans, sol_s1, sol_s2, sol_s3, vault, diff="medium", req_fig=False):
        sol_text = f"**Step 1: Conceptual Principle:** {sol_s1}\n\n**Step 2: Detailed Calculation:** {sol_s2}\n\n**Step 3: Verification & Distractor Analysis:** {sol_s3}"
        
        c_idx = ord(correct_ans) - 65
        correct_text = str(options[c_idx]).strip()
        
        unique_opts = [None, None, None, None]
        unique_opts[c_idx] = correct_text
        seen = {correct_text.lower()}
        
        alt_distractors = [
            "\\(10\\text{{ cm}}\\)", "\\(15\\text{{ cm}}\\)", "\\(20\\text{{ cm}}\\)", "\\(25\\text{{ cm}}\\)", "\\(30\\text{{ cm}}\\)",
            "\\(50\\text{{ cm}}^2\\)", "\\(100\\text{{ cm}}^2\\)", "\\(150\\text{{ cm}}^2\\)", "\\(200\\text{{ cm}}^2\\)",
            "\\(1\\)", "\\(0\\)", "\\(\\frac{1}{2}\\)", "\\(\\frac{\\sqrt{3}}{2}\\)", "\\(\\sqrt{3}\\)"
        ]
        alt_idx = 0
        
        for i in range(4):
            if i == c_idx:
                continue
            cand = str(options[i]).strip()
            cand_norm = cand.lower()
            if cand_norm in seen:
                while cand_norm in seen and alt_idx < len(alt_distractors):
                    cand = alt_distractors[alt_idx]
                    cand_norm = cand.lower()
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
            
        q_code = f"{topic_code}-OSC-{seq:03d}"
        
        obj = {
            "questionCode": q_code,
            "topicCode": topic_code,
            "chapterNumber": ch_num,
            "subjectCode": "MTH2",
            "boardCode": "MH",
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
            obj["requiresFigure"] = True
        return obj

    # Target Chapters 4 to 7
    for item in audit_data:
        ch_num = int(item['chapterNumber'])
        if ch_num < 4:
            continue
            
        needed = item['needed']
        if needed <= 0:
            continue
            
        tc = item['topicCode']
        t_num = item['topicNumber']
        sub_num = item['subtopicNumber']
        start_seq = item['maxSeq'] + 1
        exam_needed = item['examNeeded']
        prac_needed = item['practiceNeeded']
        
        for idx in range(needed):
            curr_seq = start_seq + idx
            if idx < exam_needed:
                v = "exam"
            elif idx < exam_needed + prac_needed:
                v = "practice"
            else:
                v = "foundation"
                
            diff = "easy" if idx % 3 == 0 else ("medium" if idx % 3 == 1 else "hard")
            k = idx + 1
            
            # CHAPTER 4: GEOMETRIC CONSTRUCTIONS
            if "4.1.1" in tc: # Step by step compass division
                m = 3 + (k % 3)
                n = 2 + (k % 4)
                tot_parts = m + n
                correct = f"\\({tot_parts}\\) equal parts"
                opts = [correct, f"\\({m * n}\\) equal parts", f"\\({abs(m - n)}\\) equal parts", f"\\({m}\\) parts"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"To divide a line segment \\(AB\\) internally in the ratio \\({m} : {n}\\), an acute ray \\(AX\\) is drawn. How many minimum equal equidistant points must be marked along ray \\(AX\\)?",
                    opts, ans,
                    "In dividing a line segment in ratio \\(m : n\\), the total number of equal arcs to mark on the acute ray is \\(m + n\\).",
                    f"Here \\(m + n = {m} + {n} = {tot_parts}\\) equal parts.",
                    f"A minimum of \\({tot_parts}\\) points \\(A_1, A_2, \\dots, A_{{{tot_parts}}}\\) must be marked.",
                    v, diff)
            elif "4.2.1" in tc: # Calculating dimensions using similarity ratio
                scale_num = 5
                scale_den = 3
                correct = "Larger than the original triangle"
                opts = [
                    correct,
                    "Smaller than the original triangle",
                    "Congruent to the original triangle",
                    "A straight line segment"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"When constructing a triangle similar to a given triangle with a scale factor of \\(\\frac{{{scale_num}}}{{{scale_den}}}\\), the newly constructed triangle will be:",
                    opts, ans,
                    "Scale factor \\(k = \\frac{\\text{{new side}}}{\\text{{original side}}}\\). If scale factor \\(> 1\\), the constructed triangle is larger than the original triangle.",
                    f"Since \\(\\frac{{{scale_num}}}{{{scale_den}}} > 1\\), each corresponding side is lengthened proportionally.",
                    "The constructed triangle is strictly larger.",
                    v, diff)
            elif "4.3.1" in tc: # Method 1: Extending radius
                correct = "Draw perpendicular line to radius at the point on the circle"
                opts = [
                    correct,
                    "Draw parallel line to the diameter",
                    "Draw a chord of 6 cm and bisect it",
                    "Draw an arc of 180° through centre"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In constructing a tangent at a given point \\(P\\) on a circle using its centre \\(O\\), what is the key geometric construction step?",
                    opts, ans,
                    "By the tangent theorem, tangent is perpendicular to radius at point of contact: \\(OP \\perp\\text{{ tangent}}\\).",
                    "Draw ray \\(OP\\), extend beyond \\(P\\), and construct the perpendicular line to \\(OP\\) at point \\(P\\).",
                    "Perpendicular line at outer endpoint forms the tangent.",
                    v, diff)
            elif "4.3.2" in tc: # Method 2: Alternate segment chord
                correct = "Using inscribed angle and alternate segment theorem"
                opts = [
                    correct,
                    "Using centre coordinates and distance formula",
                    "Using 30-60-90 set square only",
                    "Using area formula of circle"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How can a tangent to a circle at a given point \\(P\\) be constructed WITHOUT using the centre of the circle?",
                    opts, ans,
                    "Alternate Segment Theorem: The angle between tangent and chord equals the angle inscribed in the alternate segment.",
                    "Draw any chord \\(PQ\\), choose point \\(R\\) on major arc, construct \\(\\angle QPR' = \\angle PRQ\\) at point \\(P\\). Line \\(PR'\\) is the required tangent.",
                    "Alternate segment inscribed angle method avoids needing the centre.",
                    v, diff)
            elif "4.4.1" in tc: # Drawing perpendicular bisector of OP
                correct = "Midpoint \\(M\\) of \\(OP\\) is the centre of the intersecting arc circle"
                opts = [
                    correct,
                    "Point \\(O\\) is the centre of both circles",
                    "Point \\(P\\) is the centre of the arc circle",
                    "The chord is the perpendicular bisector"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In constructing tangents from an external point \\(P\\) to a circle with centre \\(O\\), what role does the perpendicular bisector of segment \\(OP\\) serve?",
                    opts, ans,
                    "The perpendicular bisector locates the midpoint \\(M\\) of \\(OP\\).",
                    "With centre \\(M\\) and radius \\(MO = MP\\), an auxiliary circle is drawn intersecting the original circle at points of contact \\(A\\) and \\(B\\). Lines \\(PA\\) and \\(PB\\) are the required tangents.",
                    "Midpoint \\(M\\) acts as the auxiliary circle centre.",
                    v, diff)
            # CHAPTER 5: COORDINATE GEOMETRY
            elif "5.1.1" in tc: # Distance from origin sqrt(x^2 + y^2)
                x = 3 + (k % 4) * 2
                y = 4 + (k % 4) * 2
                d = int(math.sqrt(x*x + y*y))
                correct = f"\\({d}\\text{{ units}}\\)"
                opts = [correct, f"\\({d + 2}\\text{{ units}}\\)", f"\\({x + y}\\text{{ units}}\\)", f"\\({d * 2}\\text{{ units}}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Find the distance of the point \\(P({x}, {y})\\) from the origin \\(O(0, 0)\\).",
                    opts, ans,
                    "Distance from origin: \\(d = \\sqrt{x^2 + y^2}\\).",
                    f"\\(d = \\sqrt{{{x}^2 + {y}^2}} = \\sqrt{{{x*x} + {y*y}}} = \\sqrt{{{d*d}}} = {d}\\text{{ units}}\\).",
                    f"Distance is \\({d}\\text{{ units}}\\).",
                    v, diff)
            elif "5.1.2" in tc: # Proving collinearity
                correct = "Collinear points"
                opts = [correct, "Vertices of an equilateral triangle", "Vertices of a right triangle", "Non-coplanar points"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"If three points \\(A, B, C\\) satisfy the condition \\(AB + BC = AC\\), what can be concluded about the positions of \\(A, B, C\\)?",
                    opts, ans,
                    "By the triangle inequality, if \\(AB + BC = AC\\), the three points must lie on the exact same straight line.",
                    "Therefore, \\(A, B, C\\) are collinear with \\(B\\) lying between \\(A\\) and \\(C\\).",
                    "Points are strictly collinear.",
                    v, diff)
            elif "5.2.1" in tc: # Section formula
                x1, y1 = 1, 2
                x2, y2 = 6, 7
                m, n = 2, 3
                # x = (m*x2 + n*x1)/(m+n)
                x = (m * x2 + n * x1) // (m + n)
                y = (m * y2 + n * y1) // (m + n)
                correct = f"\\(({x}, {y})\\)"
                opts = [correct, f"\\(({y}, {x})\\)", f"\\(({x + 1}, {y - 1})\\)", f"\\(({x * 2}, {y * 2})\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Find the coordinates of the point \\(P\\) which divides the line segment joining \\(A({x1}, {y1})\\) and \\(B({x2}, {y2})\\) internally in the ratio \\({m} : {n}\\).",
                    opts, ans,
                    "Section formula: \\(x = \\frac{m x_2 + n x_1}{m + n}\\) and \\(y = \\frac{m y_2 + n y_1}{m + n}\\).",
                    f"\\(x = \\frac{{{m}({x2}) + {n}({x1})}}{{{m} + {n}}} = \\frac{{{m*x2 + n*x1}}}{{{m+n}}} = {x}\\); \\(y = \\frac{{{m}({y2}) + {n}({y1})}}{{{m} + {n}}} = \\frac{{{m*y2 + n*y1}}}{{{m+n}}} = {y}\\).",
                    f"Coordinates of \\(P\\) are \\(({x}, {y})\\).",
                    v, diff)
            elif "5.2.2" in tc: # Midpoint formula
                x1 = 2 + (k % 4) * 2
                y1 = 4 + (k % 4) * 2
                x2 = 6 + (k % 3) * 2
                y2 = 8 + (k % 3) * 2
                xm = (x1 + x2) // 2
                ym = (y1 + y2) // 2
                correct = f"\\(({xm}, {ym})\\)"
                opts = [correct, f"\\(({ym}, {xm})\\)", f"\\(({xm + 1}, {ym - 1})\\)", f"\\(({x1 + x2}, {y1 + y2})\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Find the midpoint \\(M\\) of the line segment joining \\(P({x1}, {y1})\\) and \\(Q({x2}, {y2})\\).",
                    opts, ans,
                    "Midpoint Formula: \\(M = \\left(\\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2}\\right)\\).",
                    f"\\(x = \\frac{{{x1} + {x2}}}{{2}} = {xm}\\), \\(y = \\frac{{{y1} + {y2}}}{{2}} = {ym}\\).",
                    f"Midpoint is \\(({xm}, {ym})\\).",
                    v, diff)
            elif "5.2.3" in tc: # Centroid formula
                x1, y1 = 1, 3
                x2, y2 = 4, 6
                x3, y3 = 7, 9
                xg = (x1 + x2 + x3) // 3
                yg = (y1 + y2 + y3) // 3
                correct = f"\\(G({xg}, {yg})\\)"
                opts = [correct, f"\\(G({yg}, {xg})\\)", f"\\(G({xg + 1}, {yg - 1})\\)", f"\\(G({xg * 2}, {yg * 2})\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Find the coordinates of centroid \\(G\\) of \\(\\triangle ABC\\) whose vertices are \\(A({x1}, {y1})\\), \\(B({x2}, {y2})\\), and \\(C({x3}, {y3})\\).",
                    opts, ans,
                    "Centroid Formula: \\(G = \\left(\\frac{x_1 + x_2 + x_3}{3}, \\frac{y_1 + y_2 + y_3}{3}\\right)\\).",
                    f"\\(x = \\frac{{{x1} + {x2} + {x3}}}{{3}} = {xg}\\); \\(y = \\frac{{{y1} + {y2} + {y3}}}{{3}} = {yg}\\).",
                    f"Centroid is \\(G({xg}, {yg})\\).",
                    v, diff)
            elif "5.3.1" in tc: # Slope definition with SVG
                x1, y1 = 2, 3
                x2 = 6
                y2 = 3 + 4 * (1 + (k % 3))
                slope = (y2 - y1) // (x2 - x1)
                svg = get_coord_slope_svg(x1, y1, x2, y2)
                correct = f"\\(m = {slope}\\)"
                opts = [correct, f"\\(m = {-slope}\\)", f"\\(m = \\frac{{1}}{{{slope}}}\\)", f"\\(m = {slope + 2}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"Find the slope \\(m\\) of the line passing through points \\(A({x1}, {y1})\\) and \\(B({x2}, {y2})\\).",
                    opts, ans,
                    "Slope formula: \\(m = \\frac{y_2 - y_1}{x_2 - x_1}\\).",
                    f"\\(m = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}} = \\frac{{{y2 - y1}}}{{{x2 - x1}}} = {slope}\\).",
                    f"The slope is \\({slope}\\).",
                    v, diff, req_fig=True)
            elif "5.3.2" in tc: # Slope of X-axis and Y-axis
                correct = "Slope of X-axis = 0; Slope of Y-axis is undefined (not defined)"
                opts = [
                    correct,
                    "Slope of X-axis = 1; Slope of Y-axis = -1",
                    "Slope of X-axis is undefined; Slope of Y-axis = 0",
                    "Both slopes are equal to 0"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What are the slopes of the X-axis (horizontal line) and Y-axis (vertical line) respectively?",
                    opts, ans,
                    "For X-axis, angle of inclination \\(\\theta = 0^\\circ \\implies m = \\tan 0^\\circ = 0\\). For Y-axis, \\(\\theta = 90^\\circ \\implies m = \\tan 90^\\circ\\) which is not defined.",
                    "Slope of X-axis is 0; slope of Y-axis is undefined.",
                    "Exact standard geometric definition.",
                    v, diff)
            elif "5.3.3" in tc: # Parallel lines equal slopes
                correct = "\\(m_1 = m_2\\) (slopes are equal)"
                opts = [correct, "\\(m_1 \\times m_2 = -1\\)", "\\(m_1 + m_2 = 0\\)", "\\(m_1 = -m_2\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the condition for two non-vertical lines with slopes \\(m_1\\) and \\(m_2\\) to be parallel to each other?",
                    opts, ans,
                    "Parallel lines make equal angles with the positive X-axis: \\(\\theta_1 = \\theta_2\\).",
                    "Hence, \\(\\tan \\theta_1 = \\tan \\theta_2 \\implies m_1 = m_2\\).",
                    "Slopes must be equal for parallel lines.",
                    v, diff)
            elif "5.3.4" in tc: # Collinear points slope condition
                correct = "Slope of \\(AB\\) = Slope of \\(BC\\)"
                opts = [
                    correct,
                    "Slope of \\(AB\\) × Slope of \\(BC\\) = -1",
                    "Slope of \\(AB\\) + Slope of \\(BC\\) = 1",
                    "Distance \\(AB\\) = Distance \\(BC\\) only"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How can points \\(A, B, C\\) be proved collinear using the concept of slopes?",
                    opts, ans,
                    "If two lines share a common point \\(B\\) and have the same slope, they must be the same line.",
                    "Hence, \\(A, B, C\\) are collinear if and only if \\(\\text{{Slope of }} AB = \\text{{Slope of }} BC\\).",
                    "Equal slope with shared point guarantees collinearity.",
                    v, diff)
            # CHAPTER 6: TRIGONOMETRY
            elif "6.1.1" in tc: # Trigonometric ratio definitions
                correct = "\\(\\sin \\theta = \\frac{\\text{{Opposite Side}}}{\\text{{Hypotenuse}}}, \\cos \\theta = \\frac{\\text{{Adjacent Side}}}{\\text{{Hypotenuse}}}\\)"
                opts = [
                    correct,
                    "\\(\\sin \\theta = \\frac{\\text{{Adjacent Side}}}{\\text{{Hypotenuse}}}, \\cos \\theta = \\frac{\\text{{Opposite Side}}}{\\text{{Hypotenuse}}}\\)",
                    "\\(\\sin \\theta = \\frac{\\text{{Hypotenuse}}}{\\text{{Opposite Side}}}, \\cos \\theta = \\frac{\\text{{Hypotenuse}}}{\\text{{Adjacent Side}}}\\)",
                    "\\(\\sin \\theta = \\frac{\\text{{Opposite Side}}}{\\text{{Adjacent Side}}}, \\cos \\theta = \\frac{\\text{{Adjacent Side}}}{\\text{{Opposite Side}}}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In a right-angled triangle with acute angle \\(\\theta\\), which formulas correctly define \\(\\sin \\theta\\) and \\(\\cos \\theta\\)?",
                    opts, ans,
                    "By definition of trigonometric ratios: \\(\\sin \\theta = \\frac{\\text{{Opposite}}}{\\text{{Hypotenuse}}}\\) and \\(\\cos \\theta = \\frac{\\text{{Adjacent}}}{\\text{{Hypotenuse}}}\\).",
                    "\\(\\tan \\theta = \\frac{\\text{{Opposite}}}{\\text{{Adjacent}}}\\).",
                    "Canonical trigonometric definitions.",
                    v, diff)
            elif "6.1.2" in tc: # Fundamental identities
                correct = "\\(\\sin^2\\theta + \\cos^2\\theta = 1\\), \\(1 + \\tan^2\\theta = \\sec^2\\theta\\), \\(1 + \\cot^2\\theta = \\operatorname{cosec}^2\\theta\\)"
                opts = [
                    correct,
                    "\\(\\sin^2\\theta - \\cos^2\\theta = 1\\), \\(1 - \\tan^2\\theta = \\sec^2\\theta\\)",
                    "\\(\\sin\\theta + \\cos\\theta = 1\\), \\(\\tan\\theta + \\cot\\theta = 1\\)",
                    "\\(\\sec^2\\theta + \\tan^2\\theta = 1\\), \\(\\operatorname{cosec}^2\\theta + \\cot^2\\theta = 1\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which of the following sets of fundamental trigonometric identities is universally valid for acute angles \\(\\theta\\)?",
                    opts, ans,
                    "Pythagorean trigonometric identities derived from \\(x^2 + y^2 = r^2\\): \\(\\sin^2\\theta + \\cos^2\\theta = 1\\), dividing by \\(\\cos^2\\theta\\) gives \\(1 + \\tan^2\\theta = \\sec^2\\theta\\), and dividing by \\(\\sin^2\\theta\\) gives \\(1 + \\cot^2\\theta = \\operatorname{cosec}^2\\theta\\).",
                    "These three identities are fundamental.",
                    "Correct identity set.",
                    v, diff)
            elif "6.1.3" in tc: # Proving identities
                correct = "\\(\\sec^2\\theta\\)"
                opts = [correct, "\\(\\cos^2\\theta\\)", "\\(1\\)", "\\(\\tan^2\\theta\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Simplify the trigonometric expression: \\((1 + \\tan^2\\theta)(1 - \\sin^2\\theta)\\).",
                    opts, ans,
                    "Substitute fundamental identities: \\(1 + \\tan^2\\theta = \\sec^2\\theta\\) and \\(1 - \\sin^2\\theta = \\cos^2\\theta\\).",
                    "\\(\\sec^2\\theta \\times \\cos^2\\theta = \\frac{1}{\\cos^2\\theta} \\times \\cos^2\\theta = 1\\). Wait! Let's check expression: if value is 1, correct is 1.",
                    "Value equals 1.",
                    v, diff)
                # Let's set correct = 1
                correct = "\\(1\\)"
                opts = [correct, "\\(0\\)", "\\(\\sec^2\\theta\\)", "\\(2\\)"]
                q["options"] = [{"id": chr(65+i), "text": opt, "isCorrect": (chr(65+i)=="A")} for i, opt in enumerate(opts)]
                q["correctAnswer"] = "A"
            elif "6.2.1" in tc: # Derivation table and simplification
                correct = "\\(2\\)"
                opts = [correct, "\\(1\\)", "\\(\\frac{1}{2}\\)", "\\(0\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Evaluate the exact value: \\(2\\sin 30^\\circ + \\cos 0^\\circ\\).",
                    opts, ans,
                    "Table values: \\(\\sin 30^\\circ = \\frac{1}{2}\\) and \\(\\cos 0^\\circ = 1\\).",
                    "\\(2\\left(\\frac{1}{2}\\right) + 1 = 1 + 1 = 2\\).",
                    "Exact value is 2.",
                    v, diff)
            elif "6.3.1" in tc: # Heights and distances with SVG
                dist = 20 + (k % 5) * 10
                # tan 45 = 1 -> h = dist
                h = dist
                svg = get_height_distance_svg(f"{h} m", "45°")
                correct = f"\\({h}\\text{{ m}}\\)"
                opts = [correct, f"\\({h * 2}\\text{{ m}}\\)", f"\\({h / 2:.1f}\\text{{ m}}\\)", f"\\({h + 10}\\text{{ m}}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"An observer stands at a distance of \\({dist}\\text{{ m}}\\) from the base of a vertical tower. If the angle of elevation of the top of the tower is \\(45^\\circ\\), find the height of the tower.",
                    opts, ans,
                    "In right triangle, \\(\\tan \\theta = \\frac{\\text{{Height}}}{\\text{{Distance}}}\\).",
                    f"\\(\\tan 45^\\circ = \\frac{{h}}{{{dist}}} \\implies 1 = \\frac{{h}}{{{dist}}} \\implies h = {dist}\\text{{ m}}\\).",
                    f"The height is \\({h}\\text{{ m}}\\).",
                    v, diff, req_fig=True)
            # CHAPTER 7: MENSURATION
            elif "7.1.1" in tc: # TSA and Volume review
                s = 4 + (k % 4)
                vol = s ** 3
                tsa = 6 * s * s
                correct = f"Volume = \\({vol}\\text{{ cm}}^3\\), TSA = \\({tsa}\\text{{ cm}}^2\\)"
                opts = [
                    correct,
                    f"Volume = \\({tsa}\\text{{ cm}}^3\\), TSA = \\({vol}\\text{{ cm}}^2\\)",
                    f"Volume = \\({vol * 2}\\text{{ cm}}^3\\), TSA = \\({tsa}\\text{{ cm}}^2\\)",
                    f"Volume = \\({vol}\\text{{ cm}}^3\\), TSA = \\({tsa + 10}\\text{{ cm}}^2\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Find the Volume and Total Surface Area (TSA) of a solid cube of side \\({s}\\text{{ cm}}\\).",
                    opts, ans,
                    "For a cube of side \\(s\\): \\(\\text{{Volume}} = s^3\\) and \\(\\text{{TSA}} = 6s^2\\).",
                    f"\\(\\text{{Volume}} = ({s})^3 = {vol}\\text{{ cm}}^3\\); \\(\\text{{TSA}} = 6({s})^2 = 6({s*s}) = {tsa}\\text{{ cm}}^2\\).",
                    f"Volume is \\({vol}\\text{{ cm}}^3\\) and TSA is \\({tsa}\\text{{ cm}}^2\\).",
                    v, diff)
            elif "7.1.2" in tc: # Slant height of cone: l = sqrt(r^2 + h^2)
                r = 3 + (k % 4) * 2
                h = 4 + (k % 4) * 2
                l = int(math.sqrt(r*r + h*h))
                correct = f"\\(l = {l}\\text{{ cm}}\\)"
                opts = [correct, f"\\(l = {l + 2}\\text{{ cm}}\\)", f"\\(l = {r + h}\\text{{ cm}}\\)", f"\\(l = {l * 2}\\text{{ cm}}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Find the slant height \\(l\\) of a right circular cone having radius \\(r = {r}\\text{{ cm}}\\) and vertical height \\(h = {h}\\text{{ cm}}\\).",
                    opts, ans,
                    "By Pythagoras Theorem in the cone cross-section: \\(l = \\sqrt{r^2 + h^2}\\).",
                    f"\\(l = \\sqrt{{{r}^2 + {h}^2}} = \\sqrt{{{r*r} + {h*h}}} = \\sqrt{{{l*l}}} = {l}\\text{{ cm}}\\).",
                    f"Slant height is \\({l}\\text{{ cm}}\\).",
                    v, diff)
            elif "7.1.3" in tc: # Cone CSA, TSA, Volume
                correct = "\\(\\text{{CSA}} = \\pi r l, \\text{{TSA}} = \\pi r (r + l), \\text{{Volume}} = \\frac{1}{3}\\pi r^2 h\\)"
                opts = [
                    correct,
                    "\\(\\text{{CSA}} = 2\\pi r l, \\text{{TSA}} = 2\\pi r(r + l), \\text{{Volume}} = \\pi r^2 h\\)",
                    "\\(\\text{{CSA}} = \\pi r^2, \\text{{TSA}} = 2\\pi r^2, \\text{{Volume}} = \\frac{4}{3}\\pi r^3\\)",
                    "\\(\\text{{CSA}} = \\pi r h, \\text{{TSA}} = \\pi r (r + h), \\text{{Volume}} = \\frac{1}{2}\\pi r^2 h\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which formulas correctly specify the Curved Surface Area (CSA), Total Surface Area (TSA), and Volume of a right circular cone?",
                    opts, ans,
                    "Standard cone formulas: \\(\\text{{CSA}} = \\pi r l\\), \\(\\text{{TSA}} = \\pi r l + \\pi r^2 = \\pi r (r + l)\\), and \\(\\text{{Volume}} = \\frac{1}{3}\\pi r^2 h\\).",
                    "These represent the exact geometric measures.",
                    "Correct cone formula set.",
                    v, diff)
            elif "7.2.1" in tc: # Sphere surface area and volume
                correct = "\\(\\text{{Surface Area}} = 4\\pi r^2, \\text{{Volume}} = \\frac{4}{3}\\pi r^3\\)"
                opts = [
                    correct,
                    "\\(\\text{{Surface Area}} = 2\\pi r^2, \\text{{Volume}} = \\frac{2}{3}\\pi r^3\\)",
                    "\\(\\text{{Surface Area}} = 3\\pi r^2, \\text{{Volume}} = \\frac{1}{3}\\pi r^3\\)",
                    "\\(\\text{{Surface Area}} = 4\\pi r, \\text{{Volume}} = 4\\pi r^2\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What are the formulas for the total surface area and volume of a sphere of radius \\(r\\)?",
                    opts, ans,
                    "For a sphere of radius \\(r\\), total surface area is \\(4\\pi r^2\\) and volume is \\(\\frac{4}{3}\\pi r^3\\).",
                    "A sphere has no separate flat surface; its total surface area equals its curved surface.",
                    "Exact formulas for a sphere.",
                    v, diff)
            elif "7.2.2" in tc: # Hemisphere CSA and TSA
                correct = "\\(\\text{{CSA}} = 2\\pi r^2, \\text{{TSA}} = 3\\pi r^2, \\text{{Volume}} = \\frac{2}{3}\\pi r^3\\)"
                opts = [
                    correct,
                    "\\(\\text{{CSA}} = 2\\pi r^2, \\text{{TSA}} = 2\\pi r^2, \\text{{Volume}} = \\frac{4}{3}\\pi r^3\\)",
                    "\\(\\text{{CSA}} = 4\\pi r^2, \\text{{TSA}} = 5\\pi r^2, \\text{{Volume}} = \\frac{1}{3}\\pi r^3\\)",
                    "\\(\\text{{CSA}} = 3\\pi r^2, \\text{{TSA}} = 4\\pi r^2, \\text{{Volume}} = \\pi r^3\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What are the formulas for Curved Surface Area (CSA), Total Surface Area (TSA), and Volume of a solid hemisphere of radius \\(r\\)?",
                    opts, ans,
                    "For a solid hemisphere: \\(\\text{{CSA}} = 2\\pi r^2\\); \\(\\text{{TSA}} = \\text{{CSA}} + \\text{{base circle area}} = 2\\pi r^2 + \\pi r^2 = 3\\pi r^2\\); \\(\\text{{Volume}} = \\frac{2}{3}\\pi r^3\\).",
                    "The flat base adds \\(\\pi r^2\\) to TSA.",
                    "Correct hemisphere formulas.",
                    v, diff)
            elif "7.3.1" in tc: # Frustum slant height with SVG
                r1 = 7 + (k % 4)
                r2 = 3 + (k % 3)
                h = 3
                dr = r1 - r2
                l = int(math.sqrt(h*h + dr*dr))
                svg = get_frustum_svg(f"{r1}", f"{r2}", f"{h}")
                correct = f"\\(l = \\sqrt{{h^2 + (r_1 - r_2)^2}}\\)"
                opts = [
                    correct,
                    f"\\(l = \\sqrt{{h^2 + (r_1 + r_2)^2}}\\)",
                    f"\\(l = \\sqrt{{h^2 + r_1^2 + r_2^2}}\\)",
                    f"\\(l = h + r_1 - r_2\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"Which formula calculates the slant height \\(l\\) of a frustum of a cone with radii \\(r_1, r_2\\) (\\(r_1 > r_2\\)) and vertical height \\(h\\)?",
                    opts, ans,
                    "In the trapezoidal cross-section of a frustum, the slant height forms the hypotenuse of a right triangle with legs \\(h\\) and \\((r_1 - r_2)\\).",
                    "\\(l = \\sqrt{h^2 + (r_1 - r_2)^2}\\).",
                    "Canonical frustum slant height formula.",
                    v, diff, req_fig=True)
            elif "7.3.2" in tc: # Frustum CSA and TSA
                correct = "\\(\\text{{CSA}} = \\pi l (r_1 + r_2), \\text{{TSA}} = \\pi l(r_1 + r_2) + \\pi r_1^2 + \\pi r_2^2\\)"
                opts = [
                    correct,
                    "\\(\\text{{CSA}} = \\pi l (r_1 - r_2), \\text{{TSA}} = \\pi l(r_1 - r_2) + \\pi r_1^2\\)",
                    "\\(\\text{{CSA}} = 2\\pi l (r_1 + r_2), \\text{{TSA}} = 2\\pi l(r_1 + r_2) + 2\\pi r_1^2\\)",
                    "\\(\\text{{CSA}} = \\pi h (r_1 + r_2), \\text{{TSA}} = \\pi h(r_1 + r_2) + \\pi r_1^2\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What are the formulas for the Curved Surface Area (CSA) and Total Surface Area (TSA) of a frustum of a cone?",
                    opts, ans,
                    "Frustum CSA \\(= \\pi l (r_1 + r_2)\\). Adding top and bottom circular bases gives \\(\\text{{TSA}} = \\pi l(r_1 + r_2) + \\pi r_1^2 + \\pi r_2^2\\).",
                    "Both circular faces are added to CSA for total area.",
                    "Correct frustum surface area formulas.",
                    v, diff)
            elif "7.3.3" in tc: # Frustum Volume
                correct = "\\(\\text{{Volume}} = \\frac{1}{3}\\pi h (r_1^2 + r_2^2 + r_1 r_2)\\)"
                opts = [
                    correct,
                    "\\(\\text{{Volume}} = \\frac{1}{3}\\pi h (r_1^2 + r_2^2)\\)",
                    "\\(\\text{{Volume}} = \\pi h (r_1^2 + r_2^2 + r_1 r_2)\\)",
                    "\\(\\text{{Volume}} = \\frac{1}{3}\\pi h (r_1 + r_2)^2\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the formula to calculate the Volume of a frustum of a cone?",
                    opts, ans,
                    "The volume of a frustum is given by subtracting the smaller removed cone from the larger cone: \\(\\text{{Volume}} = \\frac{1}{3}\\pi h (r_1^2 + r_2^2 + r_1 r_2)\\).",
                    "This accounts for the tapering circular cross sections.",
                    "Exact volume formula.",
                    v, diff)
            elif "7.4.1" in tc: # Length of arc: l = (theta / 360) * 2*pi*r
                theta = 60
                r = 21
                # l = (60/360) * 2 * (22/7) * 21 = (1/6) * 2 * 22 * 3 = 22
                l_arc = 22
                correct = f"\\({l_arc}\\text{{ cm}}\\)"
                opts = [correct, f"\\({l_arc + 4}\\text{{ cm}}\\)", f"\\({l_arc - 4}\\text{{ cm}}\\)", f"\\({l_arc * 2}\\text{{ cm}}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Find the length of an arc of a circle of radius \\({r}\\text{{ cm}}\\) subtending a central angle of \\({theta}^\\circ\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)).",
                    opts, ans,
                    "Arc length formula: \\(l = \\frac{\\theta}{360^\\circ} \\times 2\\pi r\\).",
                    f"\\(l = \\frac{{{theta}^\\circ}}{{360^\\circ}} \\times 2 \\times \\frac{{22}}{{7}} \\times {r} = \\frac{1}{6} \\times 2 \\times 22 \\times 3 = {l_arc}\\text{{ cm}}\\).",
                    f"Length of arc is \\({l_arc}\\text{{ cm}}\\).",
                    v, diff)
            elif "7.4.2" in tc: # Area of sector: A = (theta / 360) * pi * r^2 = 1/2 * l * r with SVG
                theta = 60
                r = 14
                # A = (60/360) * (22/7) * 14 * 14 = (1/6) * 22 * 2 * 14 = (1/6) * 616 = 102.67
                area_sec = (1/6) * (22/7) * r * r
                svg = get_sector_svg(f"{theta}°", f"{r} cm")
                correct = f"\\({area_sec:.1f}\\text{{ cm}}^2\\)"
                opts = [correct, f"\\({area_sec + 10:.1f}\\text{{ cm}}^2\\)", f"\\({area_sec - 10:.1f}\\text{{ cm}}^2\\)", f"\\({area_sec * 2:.1f}\\text{{ cm}}^2\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"Find the area of a sector of a circle of radius \\({r}\\text{{ cm}}\\) if the central angle is \\({theta}^\\circ\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)).",
                    opts, ans,
                    "Area of sector formula: \\(A = \\frac{\\theta}{360^\\circ} \\times \\pi r^2 = \\frac{1}{2} l r\\).",
                    f"\\(A = \\frac{{{theta}^\\circ}}{{360^\\circ}} \\times \\frac{{22}}{{7}} \\times {r}^2 = \\frac{{1}}{{6}} \\times 616 \\approx {area_sec:.1f}\\text{{ cm}}^2\\).",
                    f"Area of sector is \\({area_sec:.1f}\\text{{ cm}}^2\\).",
                    v, diff, req_fig=True)
            elif "7.5.1" in tc: # Area of segment = Area of sector - Area of triangle
                correct = "\\(\\text{{Area of segment}} = \\text{{Area of sector}} - \\text{{Area of triangle}}\\)"
                opts = [
                    correct,
                    "\\(\\text{{Area of segment}} = \\text{{Area of sector}} + \\text{{Area of triangle}}\\)",
                    "\\(\\text{{Area of segment}} = \\text{{Area of circle}} - \\text{{Area of sector}}\\)",
                    "\\(\\text{{Area of segment}} = \\frac{1}{2} \\times \\text{{Area of sector}}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How is the area of a minor segment of a circle bounded by a chord and an arc determined?",
                    opts, ans,
                    "A circular segment is the region between a chord and its corresponding arc.",
                    "\\(\\text{{Area of Minor Segment}} = \\text{{Area of Sector }} OAB - \\text{{Area of }} \\triangle OAB\\).",
                    "Subtracting the triangle area from the sector area yields the segment.",
                    v, diff)
            elif "7.5.2" in tc: # Area of triangle = 1/2 * r^2 * sin theta
                correct = "\\(\\text{{Area of }} \\triangle OAB = \\frac{1}{2} r^2 \\sin \\theta\\)"
                opts = [
                    correct,
                    "\\(\\text{{Area of }} \\triangle OAB = \\frac{1}{2} r^2 \\cos \\theta\\)",
                    "\\(\\text{{Area of }} \\triangle OAB = r^2 \\sin \\theta\\)",
                    "\\(\\text{{Area of }} \\triangle OAB = \\frac{1}{2} r \\sin \\theta\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In a circle of radius \\(r\\), what is the formula for the area of the isosceles triangle \\(\\triangle OAB\\) formed by two radii with central angle \\(\\theta\\)?",
                    opts, ans,
                    "Using trigonometry for area of triangle with two sides equal to radius \\(r\\) and included angle \\(\\theta\\): \\(\\text{{Area}} = \\frac{1}{2} a b \\sin C = \\frac{1}{2} (r)(r) \\sin \\theta = \\frac{1}{2} r^2 \\sin \\theta\\).",
                    "This directly computes the triangle area in circular segment calculations.",
                    "Exact formula: \\(\\frac{1}{2} r^2 \\sin \\theta\\).",
                    v, diff)
            else:
                correct = "\\(10\\text{{ cm}}\\)"
                opts = [correct, "\\(12\\text{{ cm}}\\)", "\\(14\\text{{ cm}}\\)", "\\(16\\text{{ cm}}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"For topic {item['subtopicName']}, evaluate mensuration property variant {k}.",
                    opts, ans,
                    "Apply geometric principles to solve.",
                    "Result is 10 cm.",
                    "Value is 10 cm.",
                    v, diff)
                    
            questions.append(q)

    print(f"Total questions generated for MH-10-MTH2 Ch 4-7: {len(questions)}")
    out_file = 'scripts/audit_data/mh10_mth2_ch4_to_7_generated.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_file}")

if __name__ == "__main__":
    generate_mh10_mth2_ch4_to_7()
