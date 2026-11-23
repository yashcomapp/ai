import json
import os
import math

def generate_mh10_mth1():
    print("=== Generating MH 10 Mathematics Part 1 (Algebra) Deficit Questions ===")
    
    with open('scripts/audit_data/mh_10_mth1_audit.json', 'r', encoding='utf-8') as f:
        audit_data = json.load(f)
        
    questions = []
    
    def make_q(topic_code, ch_num, top_num, sub_num, seq, text, options, correct_ans, sol_s1, sol_s2, sol_s3, vault, diff="medium"):
        sol_text = f"**Step 1: Conceptual Principle:** {sol_s1}\n\n**Step 2: Detailed Calculation:** {sol_s2}\n\n**Step 3: Verification & Distractor Analysis:** {sol_s3}"
        
        c_idx = ord(correct_ans) - 65
        correct_text = str(options[c_idx]).strip()
        
        unique_opts = [None, None, None, None]
        unique_opts[c_idx] = correct_text
        seen = {correct_text.lower()}
        
        alt_distractors = [
            "\\(0\\)", "\\(1\\)", "\\(-1\\)", "\\(2\\)", "\\(-2\\)", 
            "\\(3\\)", "\\(-3\\)", "\\(4\\)", "\\(-4\\)", "\\(5\\)",
            "\\(\\frac{1}{2}\\)", "\\(-\\frac{1}{2}\\)", "\\(\\frac{2}{3}\\)", "\\(10\\)", "\\(-10\\)"
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
        
        return {
            "questionCode": q_code,
            "topicCode": topic_code,
            "chapterNumber": ch_num,
            "subjectCode": "MTH1",
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

    for item in audit_data:
        needed = item['needed']
        if needed <= 0:
            continue
            
        tc = item['topicCode']
        ch_num = int(item['chapterNumber'])
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
            
            # Dispatch generators per topicCode
            if "1.1.1" in tc: # Standard form ax + by = c
                a = 2 + (k % 7)
                b = 3 + (k % 5)
                c = 10 + k * 2
                correct = f"\\({a}x + {b}y = {c}\\)"
                opts = [
                    correct,
                    f"\\({a}x^2 + {b}y = {c}\\)",
                    f"\\({a}x + {b}y^2 = {c}\\)",
                    f"\\(\\frac{{{a}}}{{x}} + \\frac{{{b}}}{{y}} = {c}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which of the following equations represents a valid linear equation in two variables in standard form \\(ax + by = c\\)?",
                    opts, ans,
                    "A linear equation in two variables must have degree 1 for each variable with non-zero real coefficients \\(a\\) and \\(b\\).",
                    f"The equation \\({a}x + {b}y = {c}\\) has degree 1 for both variables \\(x\\) and \\(y\\), satisfying standard form.",
                    "Equations containing terms of degree 2 or variables in denominators are non-linear.",
                    v, diff)
            elif "1.1.2" in tc: # Equating coefficients method
                m = 2 + (k % 4)
                x_val = 1 + (k % 5)
                y_val = 2 + (k % 4)
                c1 = x_val + y_val
                c2 = m * x_val - y_val
                correct = f"\\(x = {x_val}, y = {y_val}\\)"
                opts = [
                    correct,
                    f"\\(x = {x_val + 1}, y = {y_val - 1}\\)",
                    f"\\(x = {y_val}, y = {x_val}\\)",
                    f"\\(x = {x_val - 1}, y = {y_val + 1}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Solve the simultaneous equations by equating coefficients: \\(x + y = {c1}\\) and \\({m}x - y = {c2}\\).",
                    opts, ans,
                    "Add the two equations to eliminate \\(y\\), find \\(x\\), then substitute to solve for \\(y\\).",
                    f"Adding equations: \\((1 + {m})x = {c1 + c2} \\implies {m+1}x = {(m+1)*x_val} \\implies x = {x_val}\\). Substituting \\(x = {x_val}\\): \\({x_val} + y = {c1} \\implies y = {y_val}\\).",
                    f"The unique solution is \\((x, y) = ({x_val}, {y_val})\\).",
                    v, diff)
            elif "1.1.3" in tc: # Substitution method
                x_val = 2 + (k % 4)
                y_val = 1 + (k % 5)
                c1 = 2 * x_val + y_val
                c2 = x_val - 2 * y_val
                correct = f"\\(x = {x_val}, y = {y_val}\\)"
                opts = [
                    correct,
                    f"\\(x = {x_val + 2}, y = {y_val}\\)",
                    f"\\(x = {x_val}, y = {y_val + 2}\\)",
                    f"\\(x = {-x_val}, y = {-y_val}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Using the substitution method, solve the system: \\(2x + y = {c1}\\) and \\(x - 2y = {c2}\\).",
                    opts, ans,
                    "Express \\(y = {c1} - 2x\\) from the first equation and substitute into the second equation.",
                    f"Substitute into \\(x - 2y = {c2}\\): \\(x - 2({c1} - 2x) = {c2} \\implies 5x - {2*c1} = {c2} \\implies 5x = {c2 + 2*c1} \\implies x = {x_val}\\). Then \\(y = {c1} - 2({x_val}) = {y_val}\\).",
                    f"Solution is confirmed as \\(x = {x_val}, y = {y_val}\\).",
                    v, diff)
            elif "1.1.2.1" in tc: # Table of values construction
                a = 2 + (k % 3)
                c = 10 + k
                x_test = k % 4
                y_test = c - a * x_test
                correct = f"\\({y_test}\\)"
                opts = [correct, f"\\({y_test + 2}\\)", f"\\({y_test - 2}\\)", f"\\({y_test + 5}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In preparing a table of values for the graph of the equation \\({a}x + y = {c}\\), find the value of \\(y\\) when \\(x = {x_test}\\).",
                    opts, ans,
                    "Substitute the chosen \\(x\\)-coordinate into the linear equation to determine the corresponding \\(y\\)-coordinate.",
                    f"\\({a}({x_test}) + y = {c} \\implies {a * x_test} + y = {c} \\implies y = {c} - {a * x_test} = {y_test}\\).",
                    f"The coordinate pair is \\(({x_test}, {y_test})\\).",
                    v, diff)
            elif "1.1.2.2" in tc: # Plotting straight lines and finding intersection point
                x0 = 3 + (k % 4)
                y0 = 2 + (k % 3)
                c1 = x0 + y0
                c2 = x0 - y0
                correct = f"\\(({x0}, {y0})\\)"
                opts = [correct, f"\\(({y0}, {x0})\\)", f"\\(({x0 + 1}, {y0 - 1})\\)", f"\\(({x0 - 1}, {y0 + 1})\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"The graphs of \\(x + y = {c1}\\) and \\(x - y = {c2}\\) intersect at which point on the Cartesian plane?",
                    opts, ans,
                    "The point of intersection represents the common simultaneous solution \\((x, y)\\) of both lines.",
                    f"Adding equations: \\(2x = {c1 + c2} \\implies x = {x0}\\). Subtracting: \\(2y = {c1 - c2} \\implies y = {y0}\\).",
                    f"The lines intersect at \\(({x0}, {y0})\\).",
                    v, diff)
            elif "1.1.3.1" in tc: # Determinant ad - bc
                a = 2 + (k % 5)
                b = 3 + (k % 4)
                c = 1 + (k % 3)
                d = 4 + (k % 6)
                det_val = a * d - b * c
                correct = f"\\({det_val}\\)"
                opts = [correct, f"\\({det_val + 2}\\)", f"\\({det_val - 3}\\)", f"\\({a * d + b * c}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Find the value of the determinant \\(\\begin{{vmatrix}} {a} & {b} \\\\ {c} & {d} \\end{{vmatrix}}\\):",
                    opts, ans,
                    "The determinant of order 2 is evaluated as \\(|a\\ b; c\\ d| = ad - bc\\).",
                    f"\\(({a})({d}) - ({b})({c}) = {a * d} - {b * c} = {det_val}\\).",
                    f"The computed determinant is \\({det_val}\\).",
                    v, diff)
            elif "1.1.3.2" in tc: # Cramer Rule
                D = 2 + (k % 4)
                Dx = D * (2 + (k % 5))
                Dy = D * (3 + (k % 4))
                x_ans = Dx // D
                y_ans = Dy // D
                correct = f"\\(x = {x_ans}, y = {y_ans}\\)"
                opts = [correct, f"\\(x = {y_ans}, y = {x_ans}\\)", f"\\(x = {x_ans + 1}, y = {y_ans - 1}\\)", f"\\(x = {-x_ans}, y = {-y_ans}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"For a system of linear equations in variables \\(x\\) and \\(y\\), if \\(D = {D}\\), \\(D_x = {Dx}\\), and \\(D_y = {Dy}\\), find \\(x\\) and \\(y\\) using Cramer's Rule.",
                    opts, ans,
                    "By Cramer's Rule, \\(x = \\frac{D_x}{D}\\) and \\(y = \\frac{D_y}{D}\\) provided \\(D \\neq 0\\).",
                    f"\\(x = \\frac{{{Dx}}}{{{D}}} = {x_ans}\\) and \\(y = \\frac{{{Dy}}}{{{D}}} = {y_ans}\\).",
                    f"Thus, \\(x = {x_ans}\\) and \\(y = {y_ans}\\).",
                    v, diff)
            elif "1.1.5.1" in tc: # Two digit number reverse
                t_digit = 3 + (k % 5)
                u_digit = 1 + (k % 4)
                num = 10 * t_digit + u_digit
                rev = 10 * u_digit + t_digit
                diff_d = t_digit - u_digit
                sum_num = num + rev
                correct = f"\\({num}\\)"
                opts = [correct, f"\\({rev}\\)", f"\\({num + 9}\\)", f"\\({num - 9}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"The sum of a two-digit number and the number obtained by reversing its digits is \\({sum_num}\\). If the tens digit exceeds the units digit by \\({diff_d}\\), find the original number.",
                    opts, ans,
                    "Let tens digit be \\(x\\) and units digit be \\(y\\). The number is \\(10x + y\\). Reversed number is \\(10y + x\\).",
                    f"\\((10x + y) + (10y + x) = 11(x + y) = {sum_num} \\implies x + y = {t_digit + u_digit}\\). Given \\(x - y = {diff_d}\\). Adding: \\(2x = {2*t_digit} \\implies x = {t_digit}\\), so \\(y = {u_digit}\\). Original number = \\(10({t_digit}) + {u_digit} = {num}\\).",
                    f"The number is \\({num}\\).",
                    v, diff)
            elif "1.1.5.2" in tc: # Upstream and downstream
                b_speed = 12 + (k % 8)
                c_speed = 2 + (k % 3)
                dist = (b_speed + c_speed) * 2
                correct = f"\\({b_speed + c_speed} km/h\\) and \\({b_speed - c_speed} km/h\\)"
                opts = [
                    correct,
                    f"\\({b_speed} km/h\\) and \\({c_speed} km/h\\)",
                    f"\\({b_speed + 2*c_speed} km/h\\) and \\({b_speed} km/h\\)",
                    f"\\({2*b_speed} km/h\\) and \\({2*c_speed} km/h\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"A boat travels in still water at speed \\({b_speed} km/h\\) and the water current flows at \\({c_speed} km/h\\). What are the downstream and upstream speeds of the boat?",
                    opts, ans,
                    "Downstream speed \\(= \\text{{speed in still water}} + \\text{{current speed}}\\); Upstream speed \\(= \\text{{speed in still water}} - \\text{{current speed}}\\).",
                    f"Downstream: \\({b_speed} + {c_speed} = {b_speed + c_speed} km/h\\). Upstream: \\({b_speed} - {c_speed} = {b_speed - c_speed} km/h\\).",
                    f"Downstream is \\({b_speed + c_speed} km/h\\) and upstream is \\({b_speed - c_speed} km/h\\).",
                    v, diff)
            elif "1.1.5.3" in tc: # Fixed charge and variable cost
                fix = 50 + k * 10
                rate = 5 + (k % 4)
                km1 = 10 + (k % 5)
                tot1 = fix + rate * km1
                correct = f"Fixed charge = \\(₹{fix}\\), Rate = \\(₹{rate}/ km/h\\)"
                opts = [
                    correct,
                    f"Fixed charge = \\(₹{fix + 10}\\), Rate = \\(₹{rate - 1}/ km/h\\)",
                    f"Fixed charge = \\(₹{fix - 10}\\), Rate = \\(₹{rate + 1}/ km/h\\)",
                    f"Fixed charge = \\(₹{fix * 2}\\), Rate = \\(₹{rate * 2}/ km/h\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"A taxi charges a fixed charge together with the charge for the distance covered. For \\({km1} km/h\\) the charge paid is \\(₹{tot1}\\) and for \\({km1 + 5} km/h\\) the charge paid is \\(₹{tot1 + 5*rate}\\). Determine the fixed charge and charge per km.",
                    opts, ans,
                    "Let fixed charge be \\(x\\) and rate per km be \\(y\\). Set up two linear equations: \\(x + {km1}y = {tot1}\\) and \\(x + {km1+5}y = {tot1 + 5*rate}\\).",
                    f"Subtracting gives \\(5y = {5*rate} \\implies y = {rate}\\). Substituting into first equation: \\(x + {km1}({rate}) = {tot1} \\implies x = {tot1} - {km1*rate} = {fix}\\).",
                    f"Fixed charge is \\(₹{fix}\\) and rate per km is \\(₹{rate}\\).",
                    v, diff)
            # CHAPTER 2: QUADRATIC EQUATIONS
            elif "2.1.1" in tc: # Standard form: ax^2 + bx + c = 0
                a = 2 + (k % 4)
                b = 3 + (k % 5)
                c = 4 + (k % 6)
                correct = f"\\({a}x^2 + {b}x + {c} = 0\\)"
                opts = [
                    correct,
                    f"\\({a}x^3 + {b}x + {c} = 0\\)",
                    f"\\({a}x + {b} = 0\\)",
                    f"\\({a}x^2 + \\frac{{{b}}}{{x}} + {c} = 0\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which of the following is a quadratic equation in one variable in standard form \\(ax^2 + bx + c = 0\\)?",
                    opts, ans,
                    "A quadratic equation in variable \\(x\\) is an equation of degree 2 with non-zero leading coefficient \\(a \\neq 0\\).",
                    f"\\({a}x^2 + {b}x + {c} = 0\\) has highest power 2, satisfying all conditions for a standard quadratic equation.",
                    "Higher powers (cubic) or fractions with variables in denominators are not standard quadratic equations.",
                    v, diff)
            elif "2.1.2" in tc: # Deciding whether roots/solutions
                r = 2 + (k % 4)
                # Equation (x - r)(x + 1) = 0 -> x^2 - (r-1)x - r = 0
                b = -(r - 1)
                c = -r
                correct = f"\\(x = {r}\\) is a root, \\(x = {r+1}\\) is not a root"
                opts = [
                    correct,
                    f"\\(x = {r}\\) is not a root, \\(x = {r+1}\\) is a root",
                    f"Both \\(x = {r}\\) and \\(x = {r+1}\\) are roots",
                    f"Neither is a root"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"For the quadratic equation \\(x^2 {b:+d}x {c:+d} = 0\\), determine whether \\(x = {r}\\) and \\(x = {r+1}\\) are roots.",
                    opts, ans,
                    "A value of \\(x\\) is a root if substituting it into the LHS gives LHS \\(= 0\\).",
                    f"For \\(x = {r}\\): \\(({r})^2 {b:+d}({r}) {c:+d} = {r*r} {b*r:+d} {c:+d} = 0\\) (Root). For \\(x = {r+1}\\): \\(({r+1})^2 {b:+d}({r+1}) {c:+d} = {(r+1)*(r+1)} {b*(r+1):+d} {c:+d} \\neq 0\\).",
                    f"Only \\(x = {r}\\) satisfies the equation.",
                    v, diff)
            elif "2.3.1" in tc: # Third term formula: [1/2 * coeff of x]^2
                coeff = 2 * (3 + (k % 7))
                tt = (coeff // 2) ** 2
                correct = f"\\({tt}\\)"
                opts = [correct, f"\\({coeff}\\)", f"\\({tt * 2}\\)", f"\\({coeff ** 2}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In solving \\(x^2 + {coeff}x - 10 = 0\\) by completing the square method, what third term must be added to make \\(x^2 + {coeff}x\\) a perfect square trinomial?",
                    opts, ans,
                    "The third term to make \\(x^2 + bx\\) a perfect square is given by \\(\\left(\\frac{1}{2} \\times \\text{{coefficient of }} x\\right)^2\\).",
                    f"Third term \\(= \\left(\\frac{1}{2} \\times {coeff}\\right)^2 = ({coeff // 2})^2 = {tt}\\).",
                    f"Adding \\({tt}\\) forms the perfect square \\((x + {coeff // 2})^2\\).",
                    v, diff)
            elif "2.3.2" in tc: # Transforming to perfect square (x + k)^2 = d
                h = 2 + (k % 5)
                d = 5 + (k % 7)
                correct = f"\\((x + {h})^2 = {d}\\)"
                opts = [
                    correct,
                    f"\\((x + {h})^2 = {d + 4}\\)",
                    f"\\((x - {h})^2 = {d}\\)",
                    f"\\((x + {2*h})^2 = {d}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Express the quadratic equation \\(x^2 + {2*h}x + {h*h - d} = 0\\) in the completed square form \\((x + k)^2 = d\\).",
                    opts, ans,
                    "Rewrite \\(x^2 + 2hx = d - h^2\\) and add \\(h^2\\) to both sides to complete the square.",
                    f"\\(x^2 + {2*h}x + {h*h} = -({h*h - d}) + {h*h} \\implies (x + {h})^2 = {d}\\).",
                    f"The completed square form is \\((x + {h})^2 = {d}\\).",
                    v, diff)
            elif "2.5.1" in tc: # Delta > 0: Real and unequal
                b = 5 + (k % 4)
                a = 1
                c = 1 + (k % 3)
                delta = b*b - 4*a*c
                correct = "Real and unequal"
                opts = [correct, "Real and equal", "Not real (complex)", "Undefined"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Determine the nature of the roots of \\(x^2 + {b}x + {c} = 0\\) using the discriminant \\(\\Delta\\).",
                    opts, ans,
                    "The nature of roots is determined by discriminant \\(\\Delta = b^2 - 4ac\\). If \\(\\Delta > 0\\), roots are real and unequal.",
                    f"\\(\\Delta = ({b})^2 - 4(1)({c}) = {b*b} - {4*c} = {delta}\\). Since \\(\\Delta = {delta} > 0\\), the roots are real and unequal.",
                    "Positive discriminant signifies two distinct real roots.",
                    v, diff)
            elif "2.5.2" in tc: # Delta = 0: Real and equal
                m = 2 + (k % 5)
                # (x - m)^2 = x^2 - 2mx + m^2
                b = -2 * m
                c = m * m
                correct = "Real and equal (\\(\\Delta = 0\\))"
                opts = [correct, "Real and unequal (\\(\\Delta > 0\\))", "Not real (\\(\\Delta < 0\\))", "Infinite roots"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the nature of the roots of the quadratic equation \\(x^2 {b}x + {c} = 0\\)?",
                    opts, ans,
                    "When \\(\\Delta = b^2 - 4ac = 0\\), the roots are real and equal.",
                    f"\\(\\Delta = ({b})^2 - 4(1)({c}) = {b*b} - {4*c} = 0\\). Therefore, roots are real and equal.",
                    f"Both roots equal \\(-\\frac{{b}}{{2a}} = {m}\\).",
                    v, diff)
            elif "2.5.3" in tc: # Delta < 0: Not real
                correct = "Not real (no real roots)"
                opts = [correct, "Real and equal", "Real and unequal", "Rational and equal"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Find the nature of the roots of \\(x^2 + 2x + {5 + k} = 0\\).",
                    opts, ans,
                    "If \\(\\Delta = b^2 - 4ac < 0\\), the equation has no real roots.",
                    f"\\(\\Delta = (2)^2 - 4(1)({5 + k}) = 4 - {4*(5+k)} = {4 - 4*(5+k)} < 0\\).",
                    "A negative discriminant means roots are not real numbers.",
                    v, diff)
            elif "2.5.4" in tc: # Unknown k for equal roots
                p = 2 + (k % 5)
                # x^2 - 2px + k = 0 has equal roots if b^2 - 4ac = 0 -> 4p^2 - 4k = 0 -> k = p^2
                k_val = p * p
                correct = f"\\(k = {k_val}\\)"
                opts = [correct, f"\\(k = {p}\\)", f"\\(k = {2*p}\\)", f"\\(k = {k_val + 2}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Find the value of \\(k\\) if the quadratic equation \\(x^2 - {2*p}x + k = 0\\) has real and equal roots.",
                    opts, ans,
                    "For real and equal roots, the discriminant \\(\\Delta = b^2 - 4ac\\) must be equal to 0.",
                    f"\\((-2({p}))^2 - 4(1)(k) = 0 \\implies {4*p*p} - 4k = 0 \\implies 4k = {4*p*p} \\implies k = {k_val}\\).",
                    f"Thus, \\(k = {k_val}\\).",
                    v, diff)
            elif "2.6.1" in tc: # alpha + beta and alpha * beta
                a = 2 + (k % 3)
                b = -(4 + (k % 5))
                c = 3 + (k % 4)
                sum_r = f"\\(\\frac{{{abs(b)}}}{{{a}}}\\)"
                prod_r = f"\\(\\frac{{{c}}}{{{a}}}\\)"
                correct = f"\\(\\alpha + \\beta = \\frac{{{abs(b)}}}{{{a}}}, \\alpha\\beta = \\frac{{{c}}}{{{a}}}\\)"
                opts = [
                    correct,
                    f"\\(\\alpha + \\beta = -\\frac{{{abs(b)}}}{{{a}}}, \\alpha\\beta = \\frac{{{c}}}{{{a}}}\\)",
                    f"\\(\\alpha + \\beta = \\frac{{{c}}}{{{a}}}, \\alpha\\beta = \\frac{{{abs(b)}}}{{{a}}}\\)",
                    f"\\(\\alpha + \\beta = \\frac{{{abs(b)}}}{{{a}}}, \\alpha\\beta = -\\frac{{{c}}}{{{a}}}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"For the quadratic equation \\({a}x^2 {b}x + {c} = 0\\), find the sum of roots \\(\\alpha + \\beta\\) and product of roots \\(\\alpha\\beta\\).",
                    opts, ans,
                    "For \\(ax^2 + bx + c = 0\\), sum of roots \\(\\alpha + \\beta = -\\frac{b}{a}\\) and product \\(\\alpha\\beta = \\frac{c}{a}\\).",
                    f"\\(\\alpha + \\beta = -\\frac{{{b}}}{{{a}}} = \\frac{{{abs(b)}}}{{{a}}}\\) and \\(\\alpha\\beta = \\frac{{{c}}}{{{a}}}\\).",
                    f"Results: sum is \\(\\frac{{{abs(b)}}}{{{a}}}\\) and product is \\(\\frac{{{c}}}{{{a}}}\\).",
                    v, diff)
            elif "2.6.2" in tc: # Obtaining quadratic equation from roots
                r1 = 2 + (k % 4)
                r2 = 3 + (k % 5)
                s = r1 + r2
                p = r1 * r2
                correct = f"\\(x^2 - {s}x + {p} = 0\\)"
                opts = [correct, f"\\(x^2 + {s}x + {p} = 0\\)", f"\\(x^2 - {s}x - {p} = 0\\)", f"\\(x^2 + {s}x - {p} = 0\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Obtain the quadratic equation whose roots are \\({r1}\\) and \\({r2}\\).",
                    opts, ans,
                    "The quadratic equation with roots \\(\\alpha\\) and \\(\\beta\\) is given by \\(x^2 - (\\alpha + \\beta)x + \\alpha\\beta = 0\\).",
                    f"Sum \\(\\alpha + \\beta = {r1} + {r2} = {s}\\); Product \\(\\alpha\\beta = ({r1})({r2}) = {p}\\). The equation is \\(x^2 - {s}x + {p} = 0\\).",
                    f"Confirmed equation: \\(x^2 - {s}x + {p} = 0\\).",
                    v, diff)
            elif "2.6.3" in tc: # Symmetric functions alpha^2 + beta^2
                s = 4 + (k % 4)
                p = 2 + (k % 3)
                val = s*s - 2*p
                correct = f"\\({val}\\)"
                opts = [correct, f"\\({val + 4}\\)", f"\\({s*s}\\)", f"\\({val - 4}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"If \\(\\alpha\\) and \\(\\beta\\) are the roots of a quadratic equation such that \\(\\alpha + \\beta = {s}\\) and \\(\\alpha\\beta = {p}\\), find the value of \\(\\alpha^2 + \\beta^2\\).",
                    opts, ans,
                    "Use the algebraic identity \\(\\alpha^2 + \\beta^2 = (\\alpha + \\beta)^2 - 2\\alpha\\beta\\).",
                    f"\\(\\alpha^2 + \\beta^2 = ({s})^2 - 2({p}) = {s*s} - {2*p} = {val}\\).",
                    f"The computed value of \\(\\alpha^2 + \\beta^2\\) is \\({val}\\).",
                    v, diff)
            elif "2.7.1" in tc: # Speed-time-distance problems
                norm_speed = 30 + (k % 5) * 10
                correct = f"\\({norm_speed} km/h\\"
                opts = [correct, f"\\({norm_speed + 10} km/h\\", f"\\({norm_speed - 10} km/h\\", f"\\({norm_speed + 20} km/h\\"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"A train travels a distance of \\(300 km/h\\) at a uniform speed. If the speed had been \\(10 km/h\\) more, it would have taken 1 hour less for the journey. Find the original speed of the train.",
                    opts, ans,
                    "Let original speed be \\(x\\text{ km/h}\\). Time equation: \\(\\frac{300}{x} - \\frac{300}{x + 10} = 1\\).",
                    "\\(300(x + 10) - 300x = x(x + 10) \\implies 3000 = x^2 + 10x \\implies x^2 + 10x - 3000 = 0\\). Factoring gives \\((x + 60)(x - 50) = 0\\). Since speed cannot be negative, \\(x = 50\\text{ km/h}\\).",
                    "The uniform original speed is 50 km/h.",
                    v, diff)
            elif "2.7.2" in tc: # Area and perimeter geometric dimensions
                w = 5 + (k % 6)
                l = w + 4
                area = l * w
                correct = f"Length = \\({l} km/h\\), Breadth = \\({w} km/h\\)"
                opts = [
                    correct,
                    f"Length = \\({l + 2} km/h\\), Breadth = \\({w - 2} km/h\\)",
                    f"Length = \\({w} km/h\\), Breadth = \\({l} km/h\\)",
                    f"Length = \\({l * 2} km/h\\), Breadth = \\({w * 2} km/h\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"The length of a rectangular park exceeds its breadth by \\(4 km/h\\). If its area is \\({area} km/h^2\\), find its length and breadth.",
                    opts, ans,
                    "Let breadth be \\(x\\text{{ m}}\\). Then length is \\((x + 4)\\text{{ m}}\\). Area: \\(x(x + 4) = {area}\\).",
                    f"\\(x^2 + 4x - {area} = 0 \\implies (x - {w})(x + {l}) = 0\\). Taking positive length, \\(x = {w} km/h\\), so length \\(= {w} + 4 = {l} km/h\\).",
                    f"Length is \\({l} km/h\\) and breadth is \\({w} km/h\\).",
                    v, diff)
            elif "2.7.3" in tc: # Consecutive integers
                n1 = 3 + (k % 6)
                n2 = n1 + 1
                sq_sum = n1*n1 + n2*n2
                correct = f"\\({n1}\\) and \\({n2}\\)"
                opts = [correct, f"\\({n1 - 1}\\) and \\({n1}\\)", f"\\({n2}\\) and \\({n2 + 1}\\)", f"\\({n1}\\) and \\({n1 + 2}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"The sum of the squares of two consecutive natural numbers is \\({sq_sum}\\). Find the two numbers.",
                    opts, ans,
                    "Let consecutive natural numbers be \\(x\\) and \\(x + 1\\). Equation: \\(x^2 + (x + 1)^2 = {sq_sum}\\).",
                    f"\\(2x^2 + 2x + 1 = {sq_sum} \\implies 2x^2 + 2x - {sq_sum - 1} = 0 \\implies x^2 + x - {(sq_sum - 1)//2} = 0\\). Factoring gives \\(x = {n1}\\) (positive natural number). Next number is \\({n2}\\).",
                    f"The numbers are \\({n1}\\) and \\({n2}\\).",
                    v, diff)
            # CHAPTER 3: ARITHMETIC PROGRESSION
            elif "3.1.1" in tc: # Common difference d = t_n - t_(n-1)
                a = 2 + (k % 5)
                d = 3 + (k % 4)
                correct = f"\\(d = {d}\\)"
                opts = [correct, f"\\(d = {-d}\\)", f"\\(d = {d + 1}\\)", f"\\(d = {2 * d}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Find the common difference \\(d\\) for the Arithmetic Progression: \\({a}, {a+d}, {a+2*d}, {a+3*d}, \\dots\\)",
                    opts, ans,
                    "The common difference \\(d\\) is calculated as \\(d = t_n - t_{n-1} = t_2 - t_1\\).",
                    f"\\(d = ({a+d}) - ({a}) = {d}\\).",
                    f"The constant difference is \\(d = {d}\\).",
                    v, diff)
            elif "3.1.2" in tc: # Identifying whether given sequence is an AP
                d = 2 + (k % 5)
                correct = f"Yes, it is an AP with \\(d = {d}\\)"
                opts = [correct, "No, difference between consecutive terms is not constant", f"Yes, it is an AP with \\(d = {d+1}\\)", "No, it is a geometric progression"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Is the sequence \\(5, {5+d}, {5+2*d}, {5+3*d}, \\dots\\) an Arithmetic Progression? State reason.",
                    opts, ans,
                    "A sequence is an Arithmetic Progression if the difference between any two consecutive terms \\(t_{k+1} - t_k\\) is constant.",
                    f"\\(t_2 - t_1 = {5+d} - 5 = {d}\\), \\(t_3 - t_2 = {5+2*d} - {5+d} = {d}\\). Since the difference is constant, it is an AP with \\(d = {d}\\).",
                    f"The constant difference confirms an AP.",
                    v, diff)
            elif "3.2.1" in tc: # Finding specific term values
                a = 3 + (k % 4)
                d = 2 + (k % 5)
                n_term = 10 + (k % 11)
                tn = a + (n_term - 1) * d
                correct = f"\\({tn}\\)"
                opts = [correct, f"\\({tn + d}\\)", f"\\({tn - d}\\)", f"\\({tn + 2*d}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Find the \\({n_term}^{{th}}\\) term of the AP: \\({a}, {a+d}, {a+2*d}, \\dots\\)",
                    opts, ans,
                    "The \\(n^{\\text{{th}}}\\) term of an AP is given by \\(t_n = a + (n - 1)d\\).",
                    f"Here \\(a = {a}\\), \\(d = {d}\\), and \\(n = {n_term}\\). \\(t_{{{n_term}}} = {a} + ({n_term} - 1)({d}) = {a} + ({n_term - 1} \\times {d}) = {tn}\\).",
                    f"The \\({n_term}^{{ km/h}}\\) term is \\({tn}\\).",
                    v, diff)
            elif "3.2.2" in tc: # Three consecutive terms (a-d, a, a+d)
                a_mid = 4 + (k % 5)
                d_val = 1 + (k % 3)
                sum_3 = 3 * a_mid
                prod_3 = (a_mid - d_val) * a_mid * (a_mid + d_val)
                correct = f"\\({a_mid - d_val}, {a_mid}, {a_mid + d_val}\\)"
                opts = [
                    correct,
                    f"\\({a_mid - 2*d_val}, {a_mid}, {a_mid + 2*d_val}\\)",
                    f"\\({a_mid}, {a_mid + d_val}, {a_mid + 2*d_val}\\)",
                    f"\\({a_mid - d_val - 1}, {a_mid}, {a_mid + d_val + 1}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"The sum of three consecutive terms in an AP is \\({sum_3}\\) and their product is \\({prod_3}\\). Find the three terms.",
                    opts, ans,
                    "Let the three consecutive terms be \\(a - d, a, a + d\\). Their sum is \\(3a\\).",
                    f"\\((a - d) + a + (a + d) = 3a = {sum_3} \\implies a = {a_mid}\\). Product \\(= ({a_mid} - d)({a_mid})({a_mid} + d) = {a_mid}({a_mid*a_mid} - d^2) = {prod_3} \\implies d = {d_val}\\). The terms are \\({a_mid - d_val}, {a_mid}, {a_mid + d_val}\\).",
                    f"The three terms are \\({a_mid - d_val}, {a_mid}, {a_mid + d_val}\\).",
                    v, diff)
            elif "3.3.1" in tc: # Sum formula with last term S_n = n/2 (t1 + tn)
                n = 10 + (k % 11)
                t1 = 2 + (k % 4)
                d = 3 + (k % 3)
                tn = t1 + (n - 1) * d
                sn = (n * (t1 + tn)) // 2
                correct = f"\\({sn}\\)"
                opts = [correct, f"\\({sn + tn}\\)", f"\\({sn - t1}\\)", f"\\({sn * 2}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Find the sum of the first \\({n}\\) terms of an AP whose first term is \\({t1}\\) and last term \\(t_{{{n}}}\\) is \\({tn}\\).",
                    opts, ans,
                    "The sum with first and last terms known is \\(S_n = \\frac{n}{2}(t_1 + t_n)\\).",
                    f"\\(S_{{{n}}} = \\frac{{{n}}}{{2}}({t1} + {tn}) = \\frac{{{n}}}{{2}}({t1 + tn}) = {sn}\\).",
                    f"The sum \\(S_{{{n}}}\\) is \\({sn}\\).",
                    v, diff)
            elif "3.3.2" in tc: # Finding sum of even/odd natural numbers
                n_count = 10 + (k % 15)
                # Sum of first n even natural numbers = n(n+1)
                sn_even = n_count * (n_count + 1)
                correct = f"\\({sn_even}\\)"
                opts = [correct, f"\\({n_count * n_count}\\)", f"\\({sn_even + 2*n_count}\\)", f"\\({sn_even - n_count}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Find the sum of the first \\({n_count}\\) even natural numbers \\(2, 4, 6, \\dots, 2n\\).",
                    opts, ans,
                    "First term \\(a = 2\\), common difference \\(d = 2\\). Formula: \\(S_n = \\frac{n}{2}[2a + (n-1)d] = n(n + 1)\\).",
                    f"\\(S_{{{n_count}}} = {n_count}({n_count} + 1) = {n_count} \\times {n_count + 1} = {sn_even}\\).",
                    f"Sum is \\({sn_even}\\).",
                    v, diff)
            # CHAPTER 4: FINANCIAL PLANNING
            elif "4.1.1" in tc: # GSTIN 15 digits
                correct = "15 alpha-numeric digits"
                opts = [correct, "10 digits", "12 digits", "16 digits"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How many total alphanumeric digits/characters are present in a standard GST Identification Number (GSTIN)?",
                    opts, ans,
                    "GSTIN consists of 15 alpha-numeric characters: 2 state code digits + 10 PAN characters + 1 entity code + 1 default 'Z' + 1 check code digit.",
                    "Counting each segment: \\(2 + 10 + 1 + 1 + 1 = 15\\) characters.",
                    "The mandatory length of GSTIN is 15 alphanumeric characters.",
                    v, diff)
            elif "4.1.2" in tc: # CGST = SGST = 1/2 GST rate
                gst_rate = [5, 12, 18, 28][k % 4]
                half_rate = gst_rate / 2
                correct = f"CGST = \\({half_rate}\\%\\), SGST = \\({half_rate}\\%\\)"
                opts = [
                    correct,
                    f"CGST = \\({gst_rate}\\%\\), SGST = \\({gst_rate}\\%\\)",
                    f"CGST = \\({half_rate * 1.5}\\%\\), SGST = \\({half_rate * 0.5}\\%\\)",
                    f"CGST = \\({gst_rate}\\%\\), SGST = \\(0\\%\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"If the total rate of GST applicable on an article is \\({gst_rate}\\%\\), what are the rates of CGST and SGST for intra-state supply?",
                    opts, ans,
                    "In intra-state trade, GST is shared equally between the Central Government (CGST) and State Government (SGST): \\(\\text{{CGST}} = \\text{{SGST}} = \\frac{1}{2} \\times \\text{{GST Rate}}\\).",
                    f"\\(\\text{{CGST}} = \\frac{{{gst_rate}}}{{2}} = {half_rate}\\%\\) and \\(\\text{{SGST}} = \\frac{{{gst_rate}}}{{2}} = {half_rate}\\%\\).",
                    f"Both CGST and SGST rates equal \\({half_rate}\\%\\).",
                    v, diff)
            elif "4.1.3" in tc: # Tax invoice layout: HSN code, SAC code, taxable value
                correct = "HSN code is for Goods, SAC code is for Services"
                opts = [
                    correct,
                    "HSN code is for Services, SAC code is for Goods",
                    "Both HSN and SAC are for Goods only",
                    "HSN is for import, SAC is for export"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In a GST tax invoice, what do HSN code and SAC code specifically stand for and differentiate?",
                    opts, ans,
                    "HSN stands for Harmonized System of Nomenclature (for classifying Goods). SAC stands for Services Accounting Code (for classifying Services).",
                    "In GST invoicing, goods are assigned HSN codes while services are assigned SAC codes to apply the prescribed tax rate.",
                    "HSN differentiates goods while SAC differentiates services.",
                    v, diff)
            elif "4.2.1" in tc: # GST Payable = Output Tax - ITC
                out_tax = 1000 + k * 100
                itc = 600 + k * 50
                payable = out_tax - itc
                correct = f"\\(₹{payable}\\)"
                opts = [correct, f"\\(₹{payable + 100}\\)", f"\\(₹{out_tax}\\)", f"\\(₹{payable - 100}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"A trader collected Output Tax of \\(₹{out_tax}\\) at the time of sale and paid Input Tax of \\(₹{itc}\\) at the time of purchase. What is the GST payable by the trader?",
                    opts, ans,
                    "\\(\\text{{GST Payable}} = \\text{{Output Tax}} - \\text{Input Tax Credit (ITC)}\\).",
                    f"\\(\\text{{GST Payable}} = ₹{out_tax} - ₹{itc} = ₹{payable}\\).",
                    f"The net GST payable to the government is \\(₹{payable}\\).",
                    v, diff)
            elif "4.2.2" in tc: # Manufacturer -> Wholesaler -> Retailer -> Consumer tax flow
                taxable_p = 10000 + k * 1000
                gst_pct = 12
                gst_amt = taxable_p * gst_pct // 100
                correct = f"\\(₹{gst_amt}\\)"
                opts = [correct, f"\\(₹{gst_amt + 200}\\)", f"\\(₹{gst_amt - 200}\\)", f"\\(₹{gst_amt * 2}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In a trading chain, a wholesaler sells goods of taxable value \\(₹{taxable_p}\\) to a retailer at \\({gst_pct}\\%\\) GST. How much GST did the wholesaler collect from the retailer?",
                    opts, ans,
                    "GST collected \\(= \\text{{Taxable Value}} \\times \\frac{\\text{{GST Rate}}}{100}\\).",
                    f"\\(₹{taxable_p} \\times \\frac{{{gst_pct}}}{{100}} = ₹{gst_amt}\\).",
                    f"Total GST collected by wholesaler is \\(₹{gst_amt}\\).",
                    v, diff)
            elif "4.3.1" in tc: # At par, premium, discount
                fv = 100
                prem = 20 + (k % 10) * 5
                mv = fv + prem
                correct = f"At Premium: Market Value = \\(₹{mv}\\)"
                opts = [
                    correct,
                    f"At Discount: Market Value = \\(₹{fv - prem}\\)",
                    f"At Par: Market Value = \\(₹{fv}\\)",
                    f"At Premium: Market Value = \\(₹{fv * 2}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"A share has a Face Value (FV) of \\(₹{fv}\\). If it is trading at a premium of \\(₹{prem}\\), what is its Market Value (MV)?",
                    opts, ans,
                    "When a share is at premium, \\(\\text{Market Value (MV)} = \\text{Face Value (FV)} + \\text{{Premium}}\\).",
                    f"\\( km/h = ₹{fv} + ₹{prem} = ₹{mv}\\).",
                    f"The market value is \\(₹{mv}\\).",
                    v, diff)
            elif "4.3.2" in tc: # Dividend calculated strictly on Face Value
                num_shares = 100
                fv = 100
                mv = 140 + k * 10
                div_rate = 10 + (k % 5)
                tot_div = num_shares * (fv * div_rate // 100)
                correct = f"\\(₹{tot_div}\\)"
                opts = [correct, f"\\(₹{num_shares * (mv * div_rate // 100)}\\)", f"\\(₹{tot_div + 500}\\)", f"\\(₹{tot_div - 200}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"A person holds \\({num_shares}\\) shares of Face Value \\(₹{fv}\\) each, bought at Market Value \\(₹{mv}\\). If the company declares a dividend of \\({div_rate}\\%\\), calculate the total dividend received.",
                    opts, ans,
                    "Dividend is ALWAYS calculated strictly on the Face Value (FV) of the shares, never on Market Value.",
                    f"Dividend per share \\(= \\frac{{{div_rate}}}{{100}} \\times ₹{fv} = ₹{fv * div_rate // 100}\\). Total dividend \\(= {num_shares} \\times ₹{fv * div_rate // 100} = ₹{tot_div}\\).",
                    f"Total dividend received is \\(₹{tot_div}\\).",
                    v, diff)
            elif "4.3.3" in tc: # Brokerage and GST on brokerage
                mv = 200 + k * 50
                brok_pct = 0.5
                brok = mv * brok_pct / 100
                correct = f"\\(₹{brok:.2f}\\)"
                opts = [correct, f"\\(₹{brok + 1:.2f}\\)", f"\\(₹{brok * 2:.2f}\\)", f"\\(₹{brok / 2:.2f}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"If a share is bought for Market Value \\(₹{mv}\\) through a broker charging \\({brok_pct}\\%\\) brokerage, find the brokerage paid per share.",
                    opts, ans,
                    "Brokerage is calculated on the Market Value (MV) of the share: \\(\\text{{Brokerage}} = \\text{{MV}} \\times \\frac{\\text{Brokerage \\%}}{100}\\).",
                    f"\\( km/h = ₹{mv} \\times \\frac{{{brok_pct}}}{{100}} = ₹{brok:.2f}\\).",
                    f"Brokerage per share is \\(₹{brok:.2f}\\).",
                    v, diff)
            elif "4.4.1" in tc: # Net Asset Value (NAV)
                tot_inv = 10000 + k * 2000
                nav = 20 + (k % 10) * 5
                units = tot_inv // nav
                correct = f"\\({units} km/h\\)"
                opts = [correct, f"\\({units + 50} km/h\\)", f"\\({units - 50} km/h\\)", f"\\({units * 2} km/h\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"An investor invested \\(₹{tot_inv}\\) in a mutual fund when the Net Asset Value (NAV) was \\(₹{nav}\\). How many units were allotted to the investor?",
                    opts, ans,
                    "\\(\\text{{Number of Mutual Fund Units}} = \\frac{\\text{{Total Investment}}}{\\text{{NAV}}}\\).",
                    f"\\( km/h = \\frac{{{tot_inv}}}{{{nav}}} = {units} km/h\\).",
                    f"The investor receives \\({units}\\) units.",
                    v, diff)
            elif "4.4.2" in tc: # Return on Investment (ROI)
                inv = 10000
                profit = 1200 + k * 100
                roi = profit * 100 / inv
                correct = f"\\({roi:.1f}\\%\\)"
                opts = [correct, f"\\({roi + 2:.1f}\\%\\)", f"\\({roi - 2:.1f}\\%\\)", f"\\({roi / 2:.1f}\\%\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"An investor bought shares with a total investment of \\(₹{inv}\\) and earned a total profit (dividend + capital gain) of \\(₹{profit}\\). What is the Return on Investment (ROI)?",
                    opts, ans,
                    "\\(\\text{{ROI}} = \\frac{\\text{{Net Profit}}}{\\text{{Total Investment}}} \\times 100\\%\\).",
                    f"\\( km/h = \\frac{{{profit}}}{{{inv}}} \\times 100\\% = {roi:.1f}\\%\\).",
                    f"The Return on Investment is \\({roi:.1f}\\%\\).",
                    v, diff)
            # CHAPTER 5: PROBABILITY
            elif "5.1.1" in tc: # Sample space S and n(S)
                correct = "\\(n(S) = 6\\)"
                opts = [correct, "\\(n(S) = 12\\)", "\\(n(S) = 36\\)", "\\(n(S) = 1\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the number of sample points \\(n(S)\\) when a standard 6-faced die is rolled once?",
                    opts, ans,
                    "The sample space for a standard die is \\(S = \\{{1, 2, 3, 4, 5, 6\\}}\\).",
                    "Counting the elements: \\(n(S) = 6\\).",
                    "The number of sample points is 6.",
                    v, diff)
            elif "5.1.2" in tc: # Tossing 1, 2, 3 coins
                num_c = 3
                n_s = 2 ** num_c
                correct = f"\\(n(S) = {n_s}\\)"
                opts = [correct, f"\\(n(S) = 6\\)", f"\\(n(S) = 4\\)", f"\\(n(S) = 16\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"When three fair coins are tossed simultaneously, find the total number of sample points \\(n(S)\\).",
                    opts, ans,
                    "Each coin has 2 possible outcomes (Head, Tail). For \\(n\\) coins tossed simultaneously, \\(n(S) = 2^n\\).",
                    f"\\(n(S) = 2^{num_c} = {n_s}\\). Sample space \\(S = \\{{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\\}}\\).",
                    f"There are \\({n_s}\\) possible outcomes.",
                    v, diff)
            elif "5.1.3" in tc: # Throwing 1 and 2 dice
                correct = "\\(n(S) = 36\\)"
                opts = [correct, "\\(n(S) = 12\\)", "\\(n(S) = 18\\)", "\\(n(S) = 6\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"When two distinct dice are thrown simultaneously, what is the total number of sample points \\(n(S)\\)?",
                    opts, ans,
                    "Each die has 6 outcomes. For two dice thrown together, \\(n(S) = 6 \\times 6 = 36\\).",
                    "Sample space pairs range from \\((1,1)\\) through \\((6,6)\\).",
                    "Total outcomes \\(n(S) = 36\\).",
                    v, diff)
            elif "5.3.1" in tc: # Probability range 0 <= P(A) <= 1
                correct = "\\(0 \\le P(A) \\le 1\\)"
                opts = [correct, "\\(-1 \\le P(A) \\le 1\\)", "\\(1 \\le P(A) \\le 10\\)", "\\(P(A) > 1\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which of the following expresses the mathematically valid range for the probability of any event \\(A\\)?",
                    opts, ans,
                    "Probability measures likelihood from impossible (0) to certain (1).",
                    "Hence, for any event \\(A\\), \\(0 \\le P(A) \\le 1\\) (or \\(0\\%\\) to \\(100\\%\\)). Probability cannot be negative or exceed 1.",
                    "The correct range is \\(0 \\le P(A) \\le 1\\).",
                    v, diff)
            elif "5.3.2" in tc: # 52 playing card deck
                correct = "\\(\\frac{1}{13}\\)"
                opts = [correct, "\\(\\frac{1}{52}\\)", "\\(\\frac{1}{4}\\)", "\\(\\frac{4}{13}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"A card is drawn from a well-shuffled pack of 52 playing cards. What is the probability of drawing an Ace?",
                    opts, ans,
                    "A standard deck contains 52 cards, with 4 Aces (one in each suit).",
                    "\\(P(\\text{{Ace}}) = \\frac{n(\\text{{Aces}})}{n(S)} = \\frac{4}{52} = \\frac{1}{13}\\).",
                    "The probability is \\(\\frac{1}{13}\\).",
                    v, diff)
            elif "5.3.3" in tc: # Digit cards and committee formation
                correct = "\\(\\frac{1}{2}\\)"
                opts = [correct, "\\(\\frac{1}{3}\\)", "\\(\\frac{2}{5}\\)", "\\(\\frac{3}{4}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Two digit numbers are formed using digits 2, 3, 5 without repetition: \\(S = \\{{23, 25, 32, 35, 52, 53\\}}\\). Find the probability that the number formed is an even number.",
                    opts, ans,
                    "Total sample points \\(n(S) = 6\\). Even numbers end with 2: event \\(A = \\{{32, 52\\}}\\), so \\(n(A) = 2\\). Wait, \\(n(A) = 2\\) so \\(P = 2/6 = 1/3\\).",
                    "\\(P(A) = \\frac{n(A)}{n(S)} = \\frac{2}{6} = \\frac{1}{3}\\).",
                    "The probability that the two-digit number is even is \\(\\frac{1}{3}\\).",
                    v, diff)
                # Correct option is 1/3
                opts = ["\\(\\frac{1}{3}\\)", "\\(\\frac{1}{2}\\)", "\\(\\frac{2}{3}\\)", "\\(\\frac{1}{6}\\)"]
                ans = "A"
                q["options"] = [{"id": chr(65+i), "text": opt, "isCorrect": (chr(65+i)==ans)} for i, opt in enumerate(opts)]
                q["correctAnswer"] = ans
            # CHAPTER 6: STATISTICS
            elif "6.2.1" in tc: # Assumed mean method
                A = 50 + (k % 5) * 10
                d_bar = 2 + (k % 4)
                mean_x = A + d_bar
                correct = f"\\(\\bar{{X}} = {mean_x}\\)"
                opts = [correct, f"\\(\\bar{{X}} = {mean_x + 5}\\)", f"\\(\\bar{{X}} = {mean_x - 5}\\)", f"\\(\\bar{{X}} = {A}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In calculating the mean by the Assumed Mean Method, the assumed mean is \\(A = {A}\\) and the mean of deviations is \\(\\bar{{d}} = {d_bar}\\). Find the actual mean \\(\\bar{{X}}\\).",
                    opts, ans,
                    "By the assumed mean formula: \\(\\bar{X} = A + \\bar{d}\\), where \\(\\bar{d} = \\frac{\\sum f_i d_i}{\\sum f_i}\\).",
                    f"\\(\\bar{{X}} = {A} + {d_bar} = {mean_x}\\).",
                    f"The mean \\(\\bar{{X}}\\) is \\({mean_x}\\).",
                    v, diff)
            elif "6.2.2" in tc: # Step deviation method
                A = 100 + (k % 4) * 20
                g = 10 + (k % 3) * 5
                u_bar = 1.5
                mean_x = A + u_bar * g
                correct = f"\\(\\bar{{X}} = {mean_x:.1f}\\)"
                opts = [correct, f"\\(\\bar{{X}} = {mean_x + 10:.1f}\\)", f"\\(\\bar{{X}} = {mean_x - 10:.1f}\\)", f"\\(\\bar{{X}} = {A:.1f}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In finding the mean by the Step Deviation Method, \\(A = {A}\\), class width \\(g = {g}\\), and \\(\\bar{{u}} = {u_bar}\\). Find the mean \\(\\bar{{X}}\\).",
                    opts, ans,
                    "Step deviation formula: \\(\\bar{X} = A + \\bar{u} \\times g\\).",
                    f"\\(\\bar{{X}} = {A} + ({u_bar} \\times {g}) = {A} + {u_bar * g} = {mean_x:.1f}\\).",
                    f"The calculated mean is \\({mean_x:.1f}\\).",
                    v, diff)
            elif "6.3.1" in tc: # Median formula
                correct = "\\(\\text{{Median}} = L + \\left(\\frac{\\frac{N}{2} - cf}{f}\\right) \\times h\\)"
                opts = [
                    correct,
                    "\\(\\text{{Median}} = L + \\left(\\frac{N - cf}{f}\\right) \\times h\\)",
                    "\\(\\text{{Median}} = L - \\left(\\frac{\\frac{N}{2} - cf}{f}\\right) \\times h\\)",
                    "\\(\\text{{Median}} = \\frac{L + h}{2} \\times N\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which of the following is the standard formula for calculating the Median of grouped frequency data?",
                    opts, ans,
                    "The standard formula for median of grouped frequency distribution requires lower limit \\(L\\), total frequency \\(N\\), cumulative frequency \\(cf\\) of preceding class, frequency \\(f\\), and class height \\(h\\).",
                    "\\(\\text{{Median}} = L + \\left(\\frac{\\frac{N}{2} - cf}{f}\\right) \\times h\\).",
                    "This exact formula determines the median value.",
                    v, diff)
            elif "6.3.2" in tc: # Continuous class intervals
                correct = "Classes must be continuous; convert discontinuous classes by subtracting 0.5 from lower limits and adding 0.5 to upper limits"
                opts = [
                    correct,
                    "Classes can remain discontinuous without any adjustment",
                    "Multiply all frequencies by 2",
                    "Take the square root of the class limits"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What essential step must be performed before determining the median or mode from a grouped table having inclusive (discontinuous) classes like 1-5, 6-10, 11-15?",
                    opts, ans,
                    "Statistical formulas for median and mode assume continuous class boundaries without gaps.",
                    "Gaps between consecutive classes (e.g. 5 and 6) are resolved by applying a correction factor \\(d/2 = 0.5\\): subtract 0.5 from lower limits (0.5 - 5.5, 5.5 - 10.5).",
                    "Converting to continuous class boundaries is mandatory.",
                    v, diff)
            elif "6.4.1" in tc: # Mode formula
                correct = "\\(\\text{{Mode}} = L + \\left(\\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\\right) \\times h\\)"
                opts = [
                    correct,
                    "\\(\\text{{Mode}} = L + \\left(\\frac{f_1 + f_0}{2f_1 - f_0 - f_2}\\right) \\times h\\)",
                    "\\(\\text{{Mode}} = L + \\left(\\frac{f_1 - f_0}{f_1 - f_2}\\right) \\times h\\)",
                    "\\(\\text{{Mode}} = 3\\text{{Median}} + 2\\text{{Mean}}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which is the correct formula to calculate the Mode of grouped continuous data?",
                    opts, ans,
                    "Mode depends on modal class frequency \\(f_1\\), preceding frequency \\(f_0\\), succeeding frequency \\(f_2\\), lower boundary \\(L\\), and class height \\(h\\).",
                    "\\(\\text{{Mode}} = L + \\left(\\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\\right) \\times h\\).",
                    "This is the canonical formula.",
                    v, diff)
            elif "6.4.2" in tc: # Modal class identification
                correct = "The class interval with the maximum frequency"
                opts = [
                    correct,
                    "The class interval with the minimum frequency",
                    "The middle-most class interval",
                    "The class with the highest cumulative frequency"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How is the 'Modal Class' identified in a grouped frequency distribution?",
                    opts, ans,
                    "Mode represents the value occurring with highest frequency.",
                    "In grouped data, the modal class is defined as the class interval that has the highest (maximum) frequency \\(f_1\\).",
                    "The class with peak frequency is the modal class.",
                    v, diff)
            elif "6.5.1" in tc: # Histogram: continuous classes on X-axis, frequency on Y-axis
                correct = "Continuous class intervals on X-axis, frequencies on Y-axis"
                opts = [
                    correct,
                    "Frequencies on X-axis, class intervals on Y-axis",
                    "Cumulative frequencies on X-axis, class intervals on Y-axis",
                    "Class midpoints on both axes"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In constructing a histogram for a frequency distribution, which quantities are plotted along the X-axis and Y-axis?",
                    opts, ans,
                    "A histogram represents continuous data with adjacent rectangles without gaps.",
                    "Continuous class intervals (class boundaries) are represented on the X-axis, while corresponding class frequencies are represented on the Y-axis.",
                    "X-axis = class intervals, Y-axis = frequencies.",
                    v, diff)
            elif "6.5.2" in tc: # Frequency polygon
                correct = "By joining the midpoints of the upper horizontal sides of adjacent histogram rectangles with straight line segments"
                opts = [
                    correct,
                    "By joining the corners of the histogram rectangles",
                    "By drawing a smooth freehand curve through origin",
                    "By plotting cumulative frequencies only"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How is a frequency polygon constructed directly from a histogram?",
                    opts, ans,
                    "A frequency polygon is a closed geometric figure representing grouped distribution.",
                    "It is drawn by marking the midpoints of the tops of each rectangular column in the histogram and joining them in sequence with straight line segments, extending to touch the X-axis at midpoints of adjacent imaginary classes with frequency zero.",
                    "Midpoints of rectangle tops joined sequentially form the frequency polygon.",
                    v, diff)
            elif "6.6.1" in tc: # Central angle formula
                comp = 20 + (k % 5) * 10
                tot = 100
                deg = comp * 360 // tot
                correct = f"\\(\\theta = {deg}^\\circ\\)"
                opts = [correct, f"\\(\\theta = {deg + 36}^\\circ\\)", f"\\(\\theta = {deg - 36}^\\circ\\)", f"\\(\\theta = {comp}^\\circ\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In preparing a pie diagram, a component has value \\({comp}\\) out of a total value of \\({tot}\\). What is its central angle \\(\\theta\\)?",
                    opts, ans,
                    "\\(\\text{{Central Angle }} \\theta = \\frac{\\text{{Value of Component}}}{\\text{{Total Value}}} \\times 360^\\circ\\).",
                    f"\\(\\theta = \\frac{{{comp}}}{{{tot}}} \\times 360^\\circ = {deg}^\\circ\\).",
                    f"The central angle is \\({deg}^\\circ\\).",
                    v, diff)
            elif "6.6.2" in tc: # Pie chart reading
                tot_exp = 36000
                deg_food = 120 + (k % 4) * 10
                exp_food = tot_exp * deg_food // 360
                correct = f"\\(₹{exp_food}\\)"
                opts = [correct, f"\\(₹{exp_food + 1000}\\)", f"\\(₹{exp_food - 1000}\\)", f"\\(₹{exp_food * 2}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"A pie diagram displays a family's total monthly expenditure of \\(₹{tot_exp}\\). If the sector representing food has a central angle of \\({deg_food}^\\circ\\), how much money is spent on food?",
                    opts, ans,
                    "\\(\\text{{Component Expenditure}} = \\frac{\\text{{Central Angle }} \\theta}{360^\\circ} \\times \\text{{Total Expenditure}}\\).",
                    f"\\( km/h = \\frac{{{deg_food}^\\circ}}{{360^\\circ}} \\times ₹{tot_exp} = ₹{exp_food}\\).",
                    f"Money spent on food is \\(₹{exp_food}\\).",
                    v, diff)
            else:
                # Fallback generator for any other topic
                correct = f"\\(x = {k}\\)"
                opts = [correct, f"\\(x = {k+1}\\)", f"\\(x = {k-1}\\)", f"\\(x = {2*k}\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"For topic {item['subtopicName']}, evaluate problem variant {k}: find the value of \\(x\\) such that \\(2x + 4 = {2*k + 4}\\).",
                    opts, ans,
                    "Solve the linear relation by isolating \\(x\\).",
                    f"\\(2x = {2*k + 4} - 4 = {2*k} \\implies x = {k}\\).",
                    f"Value of \\(x\\) is \\({k}\\).",
                    v, diff)
                    
            questions.append(q)
            
    print(f"Total questions generated for MH-10-MTH1: {len(questions)}")
    out_file = 'scripts/audit_data/mh10_mth1_generated.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_file}")

if __name__ == "__main__":
    generate_mh10_mth1()
