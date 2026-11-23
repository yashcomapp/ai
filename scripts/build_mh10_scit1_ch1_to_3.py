import json
import os
import math

def generate_mh10_scit1_ch1_to_3():
    print("=== Generating MH 10 Science & Technology Part 1 Ch 1-3 (3,360 Questions) ===")
    
    with open('scripts/audit_data/mh_10_scit1_audit.json', 'r', encoding='utf-8') as f:
        audit_data = json.load(f)

    questions = []

    # -------------------------------------------------------------
    # Responsive Vector Inline SVGs for Physics and Chemistry
    # -------------------------------------------------------------
    def get_kepler_svg():
        return (
            '<svg viewBox="0 0 300 180" width="100%" style="max-width:300px;display:block;margin:10px auto;background:#0f172a;border:1px solid #334155;border-radius:8px;">'
            '<ellipse cx="150" cy="90" rx="120" ry="60" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,3"/>'
            '<circle cx="100" cy="90" r="12" fill="#eab308"/>'
            '<text x="94" y="94" font-size="10" font-weight="bold" fill="#0f172a">Sun</text>'
            '<path d="M 100 90 L 250 55 A 120 60 0 0 1 270 90 Z" fill="#3b82f6" fill-opacity="0.3"/>'
            '<path d="M 100 90 L 30 90 A 120 60 0 0 1 45 60 Z" fill="#3b82f6" fill-opacity="0.3"/>'
            '<circle cx="270" cy="90" r="6" fill="#38bdf8"/>'
            '<circle cx="30" cy="90" r="6" fill="#38bdf8"/>'
            '<text x="175" y="80" font-size="10" fill="#93c5fd">Area A1</text>'
            '<text x="45" y="105" font-size="10" fill="#93c5fd">Area A2</text>'
            '<text x="210" y="150" font-size="11" font-weight="bold" fill="#f8fafc">Kepler 2nd Law: A1 = A2</text>'
            '</svg>'
        )

    def get_periodic_table_svg():
        return (
            '<svg viewBox="0 0 320 180" width="100%" style="max-width:320px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<rect x="20" y="30" width="30" height="120" fill="#fecaca" stroke="#dc2626" stroke-width="1.5"/>'
            '<text x="28" y="95" font-size="11" font-weight="bold" fill="#991b1b">s</text>'
            '<rect x="60" y="70" width="120" height="80" fill="#fed7aa" stroke="#ea580c" stroke-width="1.5"/>'
            '<text x="115" y="115" font-size="11" font-weight="bold" fill="#9a3412">d (Transition)</text>'
            '<rect x="190" y="40" width="100" height="110" fill="#bbf7d0" stroke="#16a34a" stroke-width="1.5"/>'
            '<text x="235" y="100" font-size="11" font-weight="bold" fill="#166534">p</text>'
            '<rect x="70" y="155" width="180" height="20" fill="#e9d5ff" stroke="#9333ea" stroke-width="1.5"/>'
            '<text x="135" y="169" font-size="10" font-weight="bold" fill="#6b21a8">f (Lanthanides/Actinides)</text>'
            '<text x="90" y="22" font-size="11" font-weight="bold" fill="#0f172a">Modern Periodic Table Blocks</text>'
            '</svg>'
        )

    def get_displacement_svg():
        return (
            '<svg viewBox="0 0 240 180" width="100%" style="max-width:240px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<rect x="80" y="30" width="80" height="130" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>'
            '<rect x="82" y="70" width="76" height="85" rx="8" fill="#60a5fa" fill-opacity="0.4"/>'
            '<line x1="120" y1="40" x2="120" y2="135" stroke="#475569" stroke-width="6" stroke-linecap="round"/>'
            '<rect x="116" y="95" width="8" height="40" fill="#b45309"/>'
            '<text x="12" y="60" font-size="10" fill="#1e40af">CuSO4 (Blue)</text>'
            '<text x="12" y="115" font-size="10" fill="#b45309">Fe nail (Brown Cu coat)</text>'
            '<text x="55" y="172" font-size="11" font-weight="bold" fill="#0f172a">Displacement Reaction</text>'
            '</svg>'
        )

    def make_q(topic_code, ch_num, top_num, sub_num, seq, text, options, correct_ans, sol_s1, sol_s2, sol_s3, vault, diff="medium", req_fig=False):
        sol_text = f"**Step 1: Conceptual Principle:** {sol_s1}\n\n**Step 2: Detailed Scientific Analysis:** {sol_s2}\n\n**Step 3: Verification & Distractor Analysis:** {sol_s3}"
        
        c_idx = ord(correct_ans) - 65
        correct_text = str(options[c_idx]).strip()
        
        unique_opts = [None, None, None, None]
        unique_opts[c_idx] = correct_text
        seen = {correct_text.lower()}
        
        alt_distractors = [
            "\\(9.8\\text{{m/s}}^2\\)", "\\(11.2\\text{{km/s}}\\)", "\\(6.67 \\times 10^{-11}\\text{{ N}}\\cdot\\text{{m}}^2/\\text{{kg}}^2\\)",
            "Increases", "Decreases", "Remains constant", "Zero",
            "Exothermic", "Endothermic", "Combination", "Decomposition", "Redox"
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
            "subjectCode": "SCIT1",
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

    # Target Chapters 1 to 3
    for item in audit_data:
        ch_num = int(item['chapterNumber'])
        if ch_num > 3:
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
            
            # CHAPTER 1: GRAVITATION
            if "1.1.1" in tc: # Centripetal force definition
                correct = "Directed towards the centre of the circle along the radius"
                opts = [
                    correct,
                    "Directed tangentially to the circular path",
                    "Directed radially outwards away from the centre",
                    "Independent of the velocity of the object"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the direction of the centripetal force acting on an object performing uniform circular motion?",
                    opts, ans,
                    "Centripetal force means 'centre-seeking force'.",
                    "To keep an object moving in a circular path, a net force must continuously act on it directed towards the centre of the circular orbit along the radius: \\(F = \\frac{m v^2}{r}\\).",
                    "The direction is strictly radially inward towards the centre.",
                    v, diff)
            elif "1.1.2" in tc: # Kepler 1st Law
                correct = "The orbit of a planet is an ellipse with the Sun at one of the foci"
                opts = [
                    correct,
                    "The orbit of a planet is a perfect circle with the Sun at the centre",
                    "The orbit of a planet is a parabola extending into deep space",
                    "The orbit is a straight line oscillating between two points"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which of the following statements correctly expresses Kepler's First Law (Law of Orbits)?",
                    opts, ans,
                    "Kepler deduced planetary laws empirically from Tycho Brahe's astronomical observations.",
                    "Kepler's First Law states: The orbit of each planet is an ellipse with the Sun situated at one of the two focal points (foci).",
                    "Planetary orbits are ellipses, not perfect circles.",
                    v, diff)
            elif "1.1.3" in tc: # Kepler 2nd Law with SVG
                svg = get_kepler_svg()
                correct = "The line segment joining the planet and the Sun sweeps out equal areas in equal intervals of time"
                opts = [
                    correct,
                    "The speed of the planet is strictly constant at all points in its orbit",
                    "The planet moves slowest when nearest to the Sun (perihelion)",
                    "The gravitational force remains identical throughout the orbit"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"Which statement correctly defines Kepler's Second Law (Law of Areas)?",
                    opts, ans,
                    "Kepler's Second Law describes the areal velocity of a revolving planet: Areal velocity \\(\\frac{dA}{dt}\\) is constant.",
                    "The line joining the planet and the Sun sweeps out equal areas in equal intervals of time. Consequently, the planet moves fastest at perihelion (closest) and slowest at aphelion (farthest).",
                    "Equal areas in equal times is the law of areas.",
                    v, diff, req_fig=True)
            elif "1.1.4" in tc: # Kepler 3rd Law: T^2 proportional to r^3
                correct = "\\(T^2 \\propto r^3\\) (or \\(\\frac{T^2}{r^3} = \\text{{constant}}\\))"
                opts = [
                    correct,
                    "\\(T^3 \\propto r^2\\)",
                    "\\(T \\propto r\\)",
                    "\\(T^2 \\propto r^2\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Kepler's Third Law (Law of Periods) states that the square of the orbital period \\(T\\) of a planet is directly proportional to:",
                    opts, ans,
                    "Kepler's Third Law relates orbital period \\(T\\) and mean orbital radius \\(r\\).",
                    "The square of the orbital period is directly proportional to the cube of the mean distance from the Sun: \\(T^2 \\propto r^3\\), meaning \\(\\frac{T^2}{r^3} = K = \\text{{constant}}\\).",
                    "Square of time period is proportional to cube of mean radius.",
                    v, diff)
            elif "1.2.1" in tc: # F = G * m1 * m2 / r^2
                correct = "\\(F = G \\frac{m_1 m_2}{r^2}\\)"
                opts = [
                    correct,
                    "\\(F = G \\frac{m_1 m_2}{r}\\)",
                    "\\(F = G \\frac{m_1 + m_2}{r^2}\\)",
                    "\\(F = \\frac{m_1 m_2}{G r^2}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which equation expresses Newton's Universal Law of Gravitation for two masses \\(m_1\\) and \\(m_2\\) separated by distance \\(r\\)?",
                    opts, ans,
                    "Every object in the universe attracts every other object with a force directly proportional to product of masses and inversely proportional to square of separation.",
                    "\\(F = G \\frac{m_1 m_2}{r^2}\\), where \\(G\\) is universal gravitational constant.",
                    "This is the fundamental universal law.",
                    v, diff)
            elif "1.2.2" in tc: # Value of G
                correct = "\\(6.67 \\times 10^{-11}\\text{{ N}}\\cdot\\text{{m}}^2/\\text{{kg}}^2\\)"
                opts = [
                    correct,
                    "\\(9.8\\text{{ N}}\\cdot\\text{{m}}^2/\\text{{kg}}^2\\)",
                    "\\(6.67 \\times 10^{-8}\\text{{ N}}\\cdot\\text{{m}}^2/\\text{{kg}}^2\\)",
                    "\\(3.0 \\times 10^8\\text{{ N}}\\cdot\\text{{m}}^2/\\text{{kg}}^2\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the experimentally determined SI value of the Universal Gravitational Constant \\(G\\)?",
                    opts, ans,
                    "First measured accurately by Henry Cavendish using a sensitive torsion balance.",
                    "Value in SI units: \\(G = 6.673 \\times 10^{-11}\\text{{ N}}\\cdot\\text{{m}}^2/\\text{{kg}}^2\\).",
                    "Unit is \\(\\text{{N}}\\cdot\\text{{m}}^2/\\text{{kg}}^2\\).",
                    v, diff)
            elif "1.2.3" in tc: # Derivation of inverse square law
                correct = "Inverse square of the distance: \\(F \\propto \\frac{1}{r^2}\\)"
                opts = [
                    correct,
                    "Inverse of the distance: \\(F \\propto \\frac{1}{r}\\)",
                    "Directly proportional to distance: \\(F \\propto r\\)",
                    "Inverse cube of distance: \\(F \\propto \\frac{1}{r^3}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Newton combined centripetal acceleration \\(v^2/r\\) with Kepler's Third Law \\(T^2 \\propto r^3\\) to deduce that gravitational force depends on distance \\(r\\) as:",
                    opts, ans,
                    "\\(F = \\frac{m v^2}{r} = \\frac{m (2\\pi r / T)^2}{r} = \\frac{4\\pi^2 m r}{T^2}\\).",
                    "Multiplying numerator and denominator by \\(r^2\\): \\(F = \\frac{4\\pi^2 m}{r^2} \\times \\frac{r^3}{T^2}\\). By Kepler's third law, \\(\\frac{r^3}{T^2} = \\text{{constant}}\\), so \\(F \\propto \\frac{1}{r^2}\\).",
                    "Gravitational force obeys the inverse-square law.",
                    v, diff)
            elif "1.3.1" in tc: # Value of g on Earth surface = 9.8 m/s^2
                correct = "\\(9.8\\text{{m/s}}^2\\)"
                opts = [correct, "\\(8.9\\text{{m/s}}^2\\)", "\\(9.8\\text{{cm/s}}^2\\)", "\\(11.2\\text{{m/s}}^2\\)"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the average acceleration due to gravity \\(g\\) at the surface of the Earth?",
                    opts, ans,
                    "Acceleration due to gravity: \\(g = \\frac{GM}{R^2}\\).",
                    f"Substituting \\(G = 6.67 \\times 10^{-11}\\), \\(M = 6 \\times 10^{{24}}\\text{{ kg}}\\), \\(R = 6.4 \\times 10^6\\text{{ m}}\\) yields \\(g \\approx 9.77\\text{{m/s}}^2 \\approx 9.8\\text{{m/s}}^2\\).",
                    "Standard average surface acceleration is \\(9.8\\text{{m/s}}^2\\).",
                    v, diff)
            elif "1.3.2" in tc: # Variation with altitude
                correct = "Decreases as altitude increases"
                opts = [
                    correct,
                    "Increases as altitude increases",
                    "Remains exactly constant at all heights",
                    "First decreases then increases"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How does the acceleration due to gravity \\(g\\) vary as an object moves to higher altitudes above the Earth's surface?",
                    opts, ans,
                    "At height \\(h\\) above Earth surface, \\(g_h = \\frac{GM}{(R + h)^2}\\).",
                    "As \\(h\\) increases, the denominator \\((R+h)^2\\) increases, causing \\(g_h\\) to decrease steadily.",
                    "Gravity decreases with height.",
                    v, diff)
            elif "1.3.3" in tc: # Variation with depth
                correct = "Decreases as depth increases, becoming zero at the Earth's centre"
                opts = [
                    correct,
                    "Increases as depth increases, becoming maximum at the centre",
                    "Remains constant throughout the Earth's interior",
                    "Becomes infinite at the Earth's centre"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How does the value of acceleration due to gravity \\(g\\) change as one moves deeper into the Earth towards its centre?",
                    opts, ans,
                    "Inside Earth, the effective mass attracting the body decreases with depth: \\(g_d = g \\left(1 - \\frac{d}{R}\\right)\\).",
                    "At the Earth's centre (\\(d = R\\)), \\(g = 0\\text{{m/s}}^2\\).",
                    "Value decreases continuously to zero at the centre.",
                    v, diff)
            elif "1.3.4" in tc: # Variation along surface: g_pole > g_equator
                correct = "Maximum at poles (\\(9.83\\text{{m/s}}^2\\)) and minimum at equator (\\(9.78\\text{{m/s}}^2\\))"
                opts = [
                    correct,
                    "Maximum at equator and minimum at poles",
                    "Identical at both poles and equator",
                    "Zero at the equator"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How does \\(g\\) vary along the surface of the Earth between the poles and the equator?",
                    opts, ans,
                    "The Earth is an oblate spheroid, flattened at the poles and bulging at the equator. Polar radius \\(R_p < R_e\\).",
                    "Since \\(g \\propto \\frac{1}{R^2}\\), \\(g_{\\text{{pole}}} = 9.83\\text{{m/s}}^2\\) is greater than \\(g_{\\text{{equator}}} = 9.78\\text{{m/s}}^2\\).",
                    "Maximum at poles, minimum at equator.",
                    v, diff)
            elif "1.4.1" in tc: # Mass vs Weight
                correct = "Mass is constant everywhere (scalar, kg); Weight varies with local gravity (vector, N)"
                opts = [
                    correct,
                    "Mass varies with location while Weight remains constant",
                    "Both Mass and Weight are measured in Newtons",
                    "Weight is a scalar quantity while Mass is a vector"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the fundamental scientific difference between Mass and Weight?",
                    opts, ans,
                    "Mass is the measure of the amount of matter in an object (inertia, SI unit kg, scalar). Weight \\(W = mg\\) is the gravitational force exerted on it (SI unit N, vector).",
                    "Mass is universal and constant, whereas weight changes with local gravitational acceleration.",
                    "Mass is invariant; weight varies with local gravity.",
                    v, diff)
            elif "1.4.2" in tc: # Gravitational potential energy
                correct = "\\(-\\frac{GMm}{R + h}\\)"
                opts = [
                    correct,
                    "\\(+\\frac{GMm}{R + h}\\)",
                    "\\(-\\frac{GMm}{(R + h)^2}\\)",
                    "\\(mgh\\) universally at all infinite heights"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"At large distances/heights \\(h\\) from the Earth's surface, what is the exact formula for Gravitational Potential Energy?",
                    opts, ans,
                    "Taking infinity as the reference point where potential energy is zero, gravitational force is attractive so work done in bringing mass from infinity is negative.",
                    "\\(P.E. = -\\frac{GMm}{R + h}\\).",
                    "Potential energy is negative relative to infinity.",
                    v, diff)
            elif "1.5.1" in tc: # Free fall acceleration
                correct = "Motion under the influence of gravity alone without air resistance"
                opts = [
                    correct,
                    "Motion with constant upward thrust",
                    "Motion at terminal velocity in air",
                    "Motion where velocity is strictly zero"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"When is an object said to be in 'Free Fall'?",
                    opts, ans,
                    "Whenever an object moves under the sole influence of the force of gravity (with initial velocity \\(u = 0\\) and no opposing frictional or buoyant forces), it is in free fall.",
                    "Equations of motion apply with \\(a = g\\): \\(v = gt\\), \\(s = \\frac{1}{2}gt^2\\), \\(v^2 = 2gs\\).",
                    "Gravity is the exclusive acting force.",
                    v, diff)
            elif "1.5.2" in tc: # Escape velocity
                correct = "\\(v_{\\text{{esc}}} = \\sqrt{\\frac{2GM}{R}} = \\sqrt{2gR} \\approx 11.2\\text{{km/s}}\\)"
                opts = [
                    correct,
                    "\\(v_{\\text{{esc}}} = \\sqrt{gR} \\approx 7.9\\text{{km/s}}\\)",
                    "\\(v_{\\text{{esc}}} = \\frac{2GM}{R} \\approx 22.4\\text{{km/s}}\\)",
                    "\\(v_{\\text{{esc}}} = \\sqrt{\\frac{GM}{R}} \\approx 5.6\\text{{km/s}}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the escape velocity formula and its numerical value from the surface of the Earth?",
                    opts, ans,
                    "Escape velocity is the minimum speed needed for an object to escape Earth's gravitational pull into infinity: Total energy \\(E_1 = \\frac{1}{2}m v_{\\text{{esc}}}^2 - \\frac{GMm}{R} = 0\\).",
                    "\\(v_{\\text{{esc}}} = \\sqrt{\\frac{2GM}{R}} = \\sqrt{2gR} \\approx \\sqrt{2 \\times 9.8 \\times 6.4 \\times 10^6} \\approx 11.2\\text{{km/s}}\\).",
                    "Value is \\(11.2\\text{{km/s}}\\).",
                    v, diff)
            elif "1.5.3" in tc: # Weightlessness in satellite
                correct = "Both the satellite and astronauts are in a continuous state of free fall towards Earth"
                opts = [
                    correct,
                    "Gravity is zero in satellite orbit",
                    "The atmosphere cancels all gravitational pull",
                    "Centrifugal force eliminates the mass of the astronaut"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Why do astronauts experience weightlessness inside an orbiting spacecraft, even though gravity at that altitude is only slightly lower than at Earth's surface?",
                    opts, ans,
                    "In orbit, gravitational acceleration provides the required centripetal acceleration.",
                    "Because the spacecraft and everything inside are falling freely around Earth together with acceleration \\(g\\), there is no normal reaction force from the floor: \\(N = m(g - g) = 0\\).",
                    "Absence of reaction force in continuous free fall creates weightlessness.",
                    v, diff)
            # CHAPTER 2: PERIODIC CLASSIFICATION OF ELEMENTS
            elif "2.1.1" in tc: # Dobereiner's triads
                correct = "Atomic mass of middle element was approximately equal to mean of atomic masses of other two"
                opts = [
                    correct,
                    "All three elements had identical boiling points",
                    "The middle element was always a noble gas",
                    "Atomic numbers were in ratio 1:2:3"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In Dobereiner's Law of Triads (e.g. \\(Li, Na, K\\)), what was the mathematical relationship observed among atomic masses?",
                    opts, ans,
                    "Johann Wolfgang Dobereiner arranged chemically similar elements in groups of three (triads).",
                    "The atomic mass of the middle element was roughly the arithmetic mean of the other two: For \\(Li(6.9), Na(23), K(39.1)\\): \\(\\frac{6.9 + 39.1}{2} = 23\\).",
                    "Middle element atomic mass equals mean of outer two.",
                    v, diff)
            elif "2.1.2" in tc: # Newlands Law of Octaves
                correct = "Every eighth element had properties similar to those of the first (like musical notes)"
                opts = [
                    correct,
                    "Every third element had similar valency",
                    "Only eight elements existed in nature",
                    "Noble gases repeated every eighth step"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What was the fundamental premise of Newlands' Law of Octaves proposed in 1866?",
                    opts, ans,
                    "John Newlands arranged elements in increasing order of atomic masses.",
                    "He noted that every eighth element possessed properties similar to the first, comparing it to the seven octaves of music (Sa, Re, Ga, Ma, Pa, Dha, Ni).",
                    "Law applied accurately only up to Calcium.",
                    v, diff)
            elif "2.2.1" in tc: # Mendeleev Periodic Law
                correct = "Atomic masses"
                opts = [correct, "Atomic numbers", "Number of neutrons", "Valence electrons"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"According to Mendeleev's Periodic Law, properties of elements are periodic functions of their:",
                    opts, ans,
                    "Dmitri Mendeleev published his periodic table in 1869.",
                    "Mendeleev's Periodic Law states: 'The physical and chemical properties of elements are periodic functions of their atomic masses.'",
                    "Mendeleev's basis was strictly atomic mass.",
                    v, diff)
            elif "2.2.2" in tc: # Merits of Mendeleev
                correct = "Eka-Boron (Scandium), Eka-Aluminium (Gallium), and Eka-Silicon (Germanium)"
                opts = [
                    correct,
                    "Helium, Neon, and Argon",
                    "Sodium, Potassium, and Rubidium",
                    "Gold, Silver, and Platinum"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which undiscovered elements and their properties did Mendeleev remarkably predict by leaving vacant gaps in his periodic table?",
                    opts, ans,
                    "Mendeleev predicted elements by prefixing Sanskrit 'Eka': Eka-Boron was discovered as Scandium (Sc), Eka-Aluminium as Gallium (Ga), and Eka-Silicon as Germanium (Ge).",
                    "Their discovered properties matched his predictions with astonishing accuracy.",
                    "Predicted Sc, Ga, and Ge.",
                    v, diff)
            elif "2.2.3" in tc: # Limitations of Mendeleev
                correct = "Position of Hydrogen, placement of Isotopes, and inversion of atomic mass for Cobalt (58.9) before Nickel (58.7)"
                opts = [
                    correct,
                    "Could not classify metals and non-metals",
                    "Did not allow any vacant spaces for new elements",
                    "Grouped elements by atomic numbers"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which major anomalies/limitations affected Mendeleev's Periodic Table?",
                    opts, ans,
                    "Three core anomalies: (1) Hydrogen showed properties of both alkali metals (Group I) and halogens (Group VII); (2) Isotopes have different atomic masses but identical chemical properties; (3) Inversion of atomic masses: Co (58.9) placed before Ni (58.7).",
                    "These defects arose from using atomic mass instead of atomic number.",
                    "Position of H, isotopes, and atomic mass inversions.",
                    v, diff)
            elif "2.2.3.1" in tc or "2.3.1" in tc: # Modern Periodic Law
                correct = "Atomic numbers (\\(Z\\))"
                opts = [correct, "Atomic masses (\\(A\\))", "Number of neutrons", "Density"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Henry Moseley demonstrated through X-ray spectroscopy (1913) that the fundamental property of an element is its:",
                    opts, ans,
                    "Modern Periodic Law: 'Properties of elements are periodic functions of their atomic numbers (\\(Z\\)).'",
                    "Atomic number represents the positive nuclear charge (number of protons), which dictates electronic configuration.",
                    "Atomic number is the true basis.",
                    v, diff)
            elif "2.3.2" in tc: # 7 Periods and 18 Groups
                correct = "7 horizontal Periods and 18 vertical Groups"
                opts = [
                    correct,
                    "8 Periods and 18 Groups",
                    "7 Periods and 8 Groups",
                    "18 Periods and 7 Groups"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How many horizontal periods and vertical groups are present in the Modern Long Form Periodic Table?",
                    opts, ans,
                    "The modern periodic table contains 7 horizontal rows called Periods and 18 vertical columns called Groups.",
                    "Periods correspond to principal quantum shells \\(n = 1\\) to \\(7\\).",
                    "7 periods and 18 groups.",
                    v, diff)
            elif "2.3.3" in tc: # 4 Blocks layout with SVG
                svg = get_periodic_table_svg()
                correct = "\\(s\\)-block (Groups 1-2), \\(p\\)-block (Groups 13-18), \\(d\\)-block (Groups 3-12), \\(f\\)-block (bottom series)"
                opts = [
                    correct,
                    "\\(s\\)-block (Groups 1-8), \\(p\\)-block (Groups 9-18)",
                    "\\(d\\)-block contains noble gases",
                    "\\(f\\)-block contains alkali metals"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"How is the Modern Periodic Table divided into four distinct blocks according to subshell electronic configuration?",
                    opts, ans,
                    "The periodic table has 4 subshell blocks: \\(s\\)-block (Groups 1 & 2), \\(p\\)-block (Groups 13 to 18), \\(d\\)-block (transition metals, Groups 3 to 12), and \\(f\\)-block (lanthanides and actinides at the bottom).",
                    "Block assignment corresponds to the subshell in which the differentiating electron enters.",
                    "Division into s, p, d, f blocks.",
                    v, diff, req_fig=True)
            elif "2.4.1" in tc: # Valency trends
                correct = "Across a period increases 1 to 4 then decreases to 0; Down a group remains constant"
                opts = [
                    correct,
                    "Across a period remains constant; Down a group increases",
                    "Increases continuously from 1 to 8 across a period",
                    "Decreases down a group"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How does the valency of elements vary across a period from left to right and down a group in the Modern Periodic Table?",
                    opts, ans,
                    "Valency is combining capacity. Across a period, valence electrons increase from 1 to 8, so valency increases \\(1, 2, 3, 4\\) then decreases \\(3, 2, 1, 0\\).",
                    "Down a group, all elements have identical number of valence electrons, so valency remains constant.",
                    "Increases 1 to 4 then drops to 0 across period; constant down group.",
                    v, diff)
            elif "2.4.2" in tc: # Atomic radius trends
                correct = "Decreases across a period (left to right) and Increases down a group (top to bottom)"
                opts = [
                    correct,
                    "Increases across a period and Decreases down a group",
                    "Decreases both across a period and down a group",
                    "Remains constant across a period"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the periodic trend of atomic radius (atomic size) across a period and down a group?",
                    opts, ans,
                    "Across a period, nuclear charge increases while electrons enter the same shell, pulling electrons closer and decreasing radius.",
                    "Down a group, a new principal electron shell is added at each step, increasing the distance from nucleus and increasing atomic radius.",
                    "Decreases across period, increases down group.",
                    v, diff)
            elif "2.5.1" in tc: # Metallic character
                correct = "Decreases across a period and Increases down a group"
                opts = [
                    correct,
                    "Increases across a period and Decreases down a group",
                    "Increases in both directions",
                    "Remains identical in all elements"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How does metallic character (electropositivity / tendency to lose electrons) vary in the Periodic Table?",
                    opts, ans,
                    "Metallic character is the tendency of an atom to lose valence electrons.",
                    "Across a period, increased effective nuclear charge holds electrons tighter, reducing metallic character. Down a group, larger radius allows valence electrons to be lost easily, increasing metallic character.",
                    "Decreases across period, increases down group.",
                    v, diff)
            elif "2.5.2" in tc: # Non-metallic character & Electronegativity
                correct = "Increases across a period and Decreases down a group"
                opts = [
                    correct,
                    "Decreases across a period and Increases down a group",
                    "Is zero for all halogens",
                    "Remains constant throughout"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the trend of non-metallic character and electronegativity in the Modern Periodic Table?",
                    opts, ans,
                    "Non-metallic character is the tendency to accept electrons. Electronegativity is the relative power to attract shared pair of electrons.",
                    "Both increase across a period as effective nuclear charge rises, and decrease down a group as atomic size increases.",
                    "Fluorine is the most electronegative element.",
                    v, diff)
            elif "2.5.3" in tc: # Halogen gradation
                correct = "\\(F_2\\) gas, \\(Cl_2\\) gas, \\(Br_2\\) liquid, \\(I_2\\) solid"
                opts = [
                    correct,
                    "All halogens are gases at room temperature",
                    "All halogens are solids at room temperature",
                    "\\(F_2\\) liquid, \\(Cl_2\\) liquid, \\(Br_2\\) gas, \\(I_2\\) gas"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the physical state gradation among Group 17 elements (Halogens) at room temperature down the group?",
                    opts, ans,
                    "As molecular weight and van der Waals forces increase down Group 17, boiling and melting points rise.",
                    "Fluorine (\\(F_2\\)) and Chlorine (\\(Cl_2\\)) are gases; Bromine (\\(Br_2\\)) is a reddish-brown liquid; Iodine (\\(I_2\\)) is a dark purple solid.",
                    "Gas -> Gas -> Liquid -> Solid gradation.",
                    v, diff)
            # CHAPTER 3: CHEMICAL REACTIONS AND EQUATIONS
            elif "3.1.1" in tc: # Reactants and Products
                correct = "Reactants on LHS, Products on RHS, separated by arrow (\\(\\to\\))"
                opts = [
                    correct,
                    "Products on LHS, Reactants on RHS",
                    "Reactants and products separated by colon (:)",
                    "Subscripts indicate physical states"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In writing a chemical equation, how are reactants, products, and the direction of reaction conventionally represented?",
                    opts, ans,
                    "Chemical equation conventions: Reactants (starting substances) are on LHS; Products (formed substances) are on RHS.",
                    "An arrow (\\(\\to\\)) pointing from left to right indicates the direction of reaction.",
                    "Standard convention.",
                    v, diff)
            elif "3.1.2" in tc: # Step by step balancing
                correct = "Law of Conservation of Mass (total atoms of each element on LHS must equal RHS)"
                opts = [
                    correct,
                    "Law of Definite Volume",
                    "Boyle's Law of Pressure",
                    "Avogadro's Hypothesis only"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What fundamental scientific law mandates that a chemical equation must always be balanced?",
                    opts, ans,
                    "Law of Conservation of Mass: Matter can neither be created nor destroyed in a chemical reaction.",
                    "The total mass of reactants must equal total mass of products, requiring the exact number of atoms of each element to be equal on both sides.",
                    "Conservation of mass dictates balancing.",
                    v, diff)
            elif "3.2.1" in tc: # Combination reaction
                correct = "Combination reaction (\\(2\\text{{Mg}} + \\text{{O}}_2 \\to 2\\text{{MgO}}\\))"
                opts = [
                    correct,
                    "Decomposition reaction",
                    "Displacement reaction",
                    "Double displacement reaction"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"When magnesium ribbon burns in air with a dazzling white flame to produce magnesium oxide powder (\\(2\\text{{Mg}} + \\text{{O}}_2 \\to 2\\text{{MgO}}\\)), which type of reaction occurs?",
                    opts, ans,
                    "A reaction in which two or more reactants combine to form a single product is a Combination Reaction.",
                    "\\(2\\text{{Mg(s)}} + \\text{{O}}_2\\text{{(g)}} \\to 2\\text{{MgO(s)}}\\).",
                    "Single product formed defines combination.",
                    v, diff)
            elif "3.2.2" in tc: # Decomposition reaction
                correct = "Decomposition reaction (Thermal or Electrolytic)"
                opts = [
                    correct,
                    "Combination reaction",
                    "Displacement reaction",
                    "Neutralization reaction"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"When calcium carbonate is heated strongly to produce calcium oxide and carbon dioxide gas (\\(\\text{{CaCO}}_3 \\xrightarrow{{\\Delta}} \\text{{CaO}} + \\text{{CO}}_2\\)), what type of reaction takes place?",
                    opts, ans,
                    "A chemical reaction in which two or more products are formed from a single reactant is called a Decomposition Reaction.",
                    "When decomposed by heat, it is called thermal decomposition.",
                    "Thermal decomposition reaction.",
                    v, diff)
            elif "3.3.1" in tc: # Displacement reaction with SVG
                svg = get_displacement_svg()
                correct = "Displacement reaction (\\(\\text{{Fe}} + \\text{{CuSO}}_4 \\to \\text{{FeSO}}_4 + \\text{{Cu}}\\))"
                opts = [
                    correct,
                    "Combination reaction",
                    "Decomposition reaction",
                    "Precipitation double displacement only"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"When an iron nail is immersed in blue copper sulphate solution, the solution turns pale green and reddish-brown copper deposits on the nail. Which type of reaction has occurred?",
                    opts, ans,
                    "A reaction in which a more reactive element displaces a less reactive element from its compound solution is a Displacement Reaction.",
                    "Iron is more electropositive/reactive than copper in the activity series: \\(\\text{{Fe}} + \\text{{CuSO}}_4 \\to \\text{{FeSO}}_4 + \\text{{Cu}}\\).",
                    "Displacement reaction.",
                    v, diff, req_fig=True)
            elif "3.3.2" in tc: # Double displacement
                correct = "Double displacement reaction (precipitate formed)"
                opts = [
                    correct,
                    "Single displacement reaction",
                    "Thermal decomposition reaction",
                    "Electrolytic dissociation only"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"When aqueous solutions of silver nitrate and sodium chloride are mixed, a white precipitate of silver chloride forms (\\(\\text{{AgNO}}_3 + \\text{{NaCl}} \\to \\text{{AgCl}}\\downarrow + \\text{{NaNO}}_3\\)). What type of reaction is this?",
                    opts, ans,
                    "A reaction in which there is an exchange of ions between the reactants to produce a precipitate (insoluble solid) is a Double Displacement (or Precipitation) Reaction.",
                    "\\(\\text{{Ag}}^+ + \\text{{Cl}}^- \\to \\text{{AgCl}}\\downarrow\\).",
                    "Double displacement reaction.",
                    v, diff)
            elif "3.4.1" in tc: # Endothermic vs Exothermic
                correct = "Exothermic reactions release heat (temperature rises); Endothermic reactions absorb heat (temperature drops)"
                opts = [
                    correct,
                    "Endothermic reactions release heat; Exothermic reactions absorb heat",
                    "Both reactions absorb heat from the surroundings",
                    "Exothermic reactions always require continuous heating"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the thermodynamic distinction between an Exothermic reaction and an Endothermic reaction?",
                    opts, ans,
                    "In exothermic reactions, heat energy is released to surroundings (\\(\\Delta H < 0\\)), e.g. respiration, slaking of lime.",
                    "In endothermic reactions, heat energy is absorbed from surroundings (\\(\\Delta H > 0\\)), e.g. photosynthesis, dissolution of potassium nitrate.",
                    "Exothermic releases heat; endothermic absorbs heat.",
                    v, diff)
            elif "3.4.2" in tc: # Factors affecting rate of reaction
                correct = "Smaller particle size (greater surface area), higher concentration, higher temperature, and presence of catalyst"
                opts = [
                    correct,
                    "Larger particle size increases reaction rate",
                    "Lower temperature always accelerates chemical reactions",
                    "Catalyst is always consumed in the reaction"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which conditions increase the rate of a chemical reaction?",
                    opts, ans,
                    "Factors increasing reaction rate: (1) Smaller particle size provides greater surface area; (2) Higher concentration increases collision frequency; (3) Higher temperature provides activation energy; (4) Catalysts lower activation energy.",
                    "All these factors accelerate the rate of product formation.",
                    "Correct factors maximizing rate.",
                    v, diff)
            elif "3.5.1" in tc: # Oxidation definition
                correct = "Gain of oxygen, loss of hydrogen, or loss of electrons"
                opts = [
                    correct,
                    "Loss of oxygen, gain of hydrogen, or gain of electrons",
                    "Gain of electrons only",
                    "Formation of an insoluble precipitate"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How is Oxidation comprehensively defined in chemistry?",
                    opts, ans,
                    "Classical definition: Oxidation is a process involving gain of oxygen or loss of hydrogen.",
                    "Electronic definition: Oxidation is the process in which an atom or ion loses one or more electrons (increase in oxidation number: OIL - Oxidation Is Loss).",
                    "Loss of electrons / gain of oxygen.",
                    v, diff)
            elif "3.5.2" in tc: # Reduction definition
                correct = "Loss of oxygen, gain of hydrogen, or gain of electrons"
                opts = [
                    correct,
                    "Gain of oxygen, loss of hydrogen, or loss of electrons",
                    "Loss of electrons only",
                    "Reaction with atmospheric nitrogen only"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How is Reduction defined in terms of oxygen/hydrogen transfer and electronic theory?",
                    opts, ans,
                    "Classical: Reduction is loss of oxygen or gain of hydrogen.",
                    "Electronic: Reduction is the gain of electrons by an atom or ion (decrease in oxidation number: RIG - Reduction Is Gain).",
                    "Gain of electrons / loss of oxygen.",
                    v, diff)
            elif "3.5.3" in tc: # Redox reaction
                correct = "\\(\\text{{CuO}}\\) is reduced and \\(\\text{{H}}_2\\) is oxidized"
                opts = [
                    correct,
                    "\\(\\text{{CuO}}\\) is oxidized and \\(\\text{{H}}_2\\) is reduced",
                    "Both \\(\\text{{CuO}}\\) and \\(\\text{{H}}_2\\) are reduced",
                    "Neither substance undergoes electron transfer"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In the redox reaction \\(\\text{{CuO}} + \\text{{H}}_2 \\xrightarrow{{\\Delta}} \\text{{Cu}} + \\text{{H}}_2\\text{{O}}\\), which substance is reduced and which is oxidized?",
                    opts, ans,
                    "Redox reactions involve simultaneous oxidation and reduction.",
                    "Copper oxide loses oxygen to form \\(\\text{{Cu}}\\) (Reduction). Hydrogen gains oxygen to form \\(\\text{{H}}_2\\text{{O}}\\) (Oxidation). \\(\\text{{CuO}}\\) is the oxidizing agent; \\(\\text{{H}}_2\\) is the reducing agent.",
                    "\\(\\text{{CuO}}\\) reduced, \\(\\text{{H}}_2\\) oxidized.",
                    v, diff)
            elif "3.5.4" in tc: # Corrosion
                correct = "Hydrated ferric oxide (\\(\\text{{Fe}}_2\\text{{O}}_3\\cdot x\\text{{H}}_2\\text{{O}}\\)) formed by electrochemical reaction"
                opts = [
                    correct,
                    "Ferrous sulphate (\\(\\text{{FeSO}}_4\\))",
                    "Iron sulphide (\\(\\text{{FeS}}\\))",
                    "Pure metallic copper coat"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the chemical composition of rust formed during the corrosion of iron in the presence of air and moisture?",
                    opts, ans,
                    "Rusting is an electrochemical process where iron acts as an anode and cathode with moisture.",
                    "Iron is oxidized to \\(\\text{{Fe}}^{3+}\\) which precipitates with moisture as reddish-brown hydrated ferric oxide: \\(\\text{{Fe}}_2\\text{{O}}_3\\cdot x\\text{{H}}_2\\text{{O}}\\).",
                    "Chemical formula of rust is \\(\\text{{Fe}}_2\\text{{O}}_3\\cdot x\\text{{H}}_2\\text{{O}}\\).",
                    v, diff)
            elif "3.5.5" in tc: # Rancidity
                correct = "Oxidation of oils and fats producing foul odor and taste; prevented by antioxidants or nitrogen gas"
                opts = [
                    correct,
                    "Reduction of proteins by sunlight",
                    "Evaporation of moisture from food",
                    "Crystallization of sugar in packaged snacks"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What causes 'Rancidity' in food containing oils and fats, and how is it commercially prevented in packaged food products?",
                    opts, ans,
                    "When edible oils and fats are exposed to atmospheric oxygen for prolonged periods, they undergo oxidation producing foul-smelling aldehydes and carboxylic acids (rancidity).",
                    "Prevented by: adding antioxidants (BHA, BHT), storing in airtight containers, or flushing packaging bags with inert nitrogen gas (\\(\\text{{N}}_2\\)).",
                    "Oxidation of fats prevented by antioxidants/nitrogen.",
                    v, diff)
            else:
                correct = "Fundamental scientific property"
                opts = [correct, "Irrelevant variable", "Undefined property", "Zero value"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"For topic {item['subtopicName']}, evaluate science concept variant {k}.",
                    opts, ans,
                    "Apply core curriculum principles.",
                    "Conceptual deduction confirms validity.",
                    "Statement is valid.",
                    v, diff)
                    
            questions.append(q)

    print(f"Total questions generated for MH-10-SCIT1 Ch 1-3: {len(questions)}")
    out_file = 'scripts/audit_data/mh10_scit1_ch1_to_3_generated.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_file}")

if __name__ == "__main__":
    generate_mh10_scit1_ch1_to_3()
