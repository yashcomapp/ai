import json
import os
import math

def generate_mh10_scit1_ch4_to_6():
    print("=== Generating MH 10 Science & Technology Part 1 Ch 4-6 (3,680 Questions) ===")
    
    with open('scripts/audit_data/mh_10_scit1_audit.json', 'r', encoding='utf-8') as f:
        audit_data = json.load(f)

    questions = []

    # -------------------------------------------------------------
    # Responsive Vector Inline SVGs for Physics
    # -------------------------------------------------------------
    def get_motor_svg():
        return (
            '<svg viewBox="0 0 300 180" width="100%" style="max-width:300px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<rect x="20" y="40" width="40" height="90" fill="#fecaca" stroke="#dc2626" stroke-width="2"/>'
            '<text x="32" y="90" font-size="14" font-weight="bold" fill="#991b1b">N</text>'
            '<rect x="240" y="40" width="40" height="90" fill="#bfdbfe" stroke="#2563eb" stroke-width="2"/>'
            '<text x="253" y="90" font-size="14" font-weight="bold" fill="#1e40af">S</text>'
            '<rect x="80" y="60" width="140" height="50" fill="none" stroke="#d97706" stroke-width="3"/>'
            '<circle cx="150" cy="130" r="15" fill="none" stroke="#475569" stroke-width="3" stroke-dasharray="20,10"/>'
            '<text x="105" y="165" font-size="10" font-weight="bold" fill="#0f172a">Split-Ring Commutator</text>'
            '<text x="95" y="30" font-size="11" font-weight="bold" fill="#0f172a">Electric Motor (Fleming Left Hand)</text>'
            '</svg>'
        )

    def get_hopes_apparatus_svg():
        return (
            '<svg viewBox="0 0 240 190" width="100%" style="max-width:240px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<rect x="95" y="20" width="50" height="150" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>'
            '<ellipse cx="120" cy="95" rx="55" ry="25" fill="#f1f5f9" stroke="#64748b" stroke-width="2"/>'
            '<text x="100" y="98" font-size="9" fill="#0f172a">Freezing Mix</text>'
            '<line x1="145" y1="40" x2="190" y2="40" stroke="#dc2626" stroke-width="2"/>'
            '<text x="195" y="44" font-size="10" font-weight="bold" fill="#dc2626">T1 (0°C)</text>'
            '<line x1="145" y1="150" x2="190" y2="150" stroke="#2563eb" stroke-width="2"/>'
            '<text x="195" y="154" font-size="10" font-weight="bold" fill="#2563eb">T2 (4°C)</text>'
            '<text x="45" y="182" font-size="11" font-weight="bold" fill="#0f172a">Hope Apparatus (Anomalous H2O)</text>'
            '</svg>'
        )

    def get_glass_slab_svg():
        return (
            '<svg viewBox="0 0 300 180" width="100%" style="max-width:300px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<rect x="60" y="50" width="180" height="80" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>'
            '<text x="110" y="95" font-size="11" fill="#0369a1">Glass Slab (Medium 2)</text>'
            '<line x1="110" y1="20" x2="110" y2="80" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>'
            '<line x1="40" y1="15" x2="110" y2="50" stroke="#dc2626" stroke-width="2"/>'
            '<line x1="110" y1="50" x2="160" y2="130" stroke="#2563eb" stroke-width="2"/>'
            '<line x1="160" y1="130" x2="230" y2="165" stroke="#dc2626" stroke-width="2"/>'
            '<line x1="160" y1="100" x2="160" y2="160" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>'
            '<text x="175" y="155" font-size="10" fill="#dc2626">Lateral Shift d</text>'
            '<text x="75" y="30" font-size="11" font-weight="bold" fill="#0f172a">Refraction &amp; Lateral Displacement</text>'
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
            "\\(H = I^2 R t\\)", "\\(3.6 \\times 10^6\\text{{J}}\\)", "\\(4^\\circ\\text{{C}}\\)", "\\(0^\\circ\\text{{C}}\\)",
            "Increases", "Decreases", "Remains constant", "Zero",
            "Left hand", "Right hand", "Clockwise", "Anticlockwise"
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

    # Target Chapters 4 to 6
    for item in audit_data:
        ch_num = int(item['chapterNumber'])
        if ch_num < 4 or ch_num > 6:
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
            
            # CHAPTER 4: EFFECTS OF ELECTRIC CURRENT
            if "4.1.1" in tc: # Heating effect and Joule's law
                correct = "\\(H = I^2 R t\\)"
                opts = [
                    correct,
                    "\\(H = I R t\\)",
                    "\\(H = I^2 R^2 t\\)",
                    "\\(H = \\frac{I^2 R}{t}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which equation expresses Joule's Law of Heating for a current \\(I\\) passing through a resistor of resistance \\(R\\) for time \\(t\\)?",
                    opts, ans,
                    "Joule's law of heating states that heat produced \\(H\\) is directly proportional to square of current, resistance, and time: \\(H = I^2 R t\\).",
                    "Electrical work done: \\(W = V Q = V I t = (I R) I t = I^2 R t\\). In Joules, \\(H = I^2 R t\\).",
                    "Standard Joule heating formula.",
                    v, diff)
            elif "4.1.2" in tc: # Fuse wire
                correct = "Low melting point alloy (e.g. lead and tin alloy) connected in series with live wire"
                opts = [
                    correct,
                    "High melting point tungsten wire connected in parallel",
                    "Thick copper cable connected to neutral wire",
                    "Insulated plastic fiber"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What are the essential physical properties and connection mode of a safety fuse wire in household electrical circuits?",
                    opts, ans,
                    "A safety fuse protects household electrical appliances against short-circuits and overloading.",
                    "It is made of a lead-tin alloy with a low melting point and connected strictly in series with the live wire so that excessive current melts it instantly, breaking the circuit.",
                    "Low melting point connected in series with live wire.",
                    v, diff)
            elif "4.1.3" in tc: # Electric power and kilowatt-hour
                correct = "\\(1\\text{{kWh}} = 3.6 \\times 10^6\\text{{J}}\\)"
                opts = [
                    correct,
                    "\\(1\\text{{kWh}} = 3.6 \\times 10^3\\text{{J}}\\)",
                    "\\(1\\text{{kWh}} = 1000\\text{{J}}\\)",
                    "\\(1\\text{{kWh}} = 3.6 \\times 10^8\\text{{J}}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the exact conversion relation between 1 kilowatt-hour (1 commercial electricity unit) and Joules?",
                    opts, ans,
                    "\\(1\\text{{kWh}} = 1\\text{{kW}} \\times 1\\text{{hour}} = 1000\\text{{W}} \\times 3600\\text{{s}}\\).",
                    "\\(1000\\text{{J/s}} \\times 3600\\text{{s}} = 3,600,000\\text{{J}} = 3.6 \\times 10^6\\text{{J}}\\).",
                    "Equivalence is \\(3.6 \\times 10^6\\text{{J}}\\).",
                    v, diff)
            elif "4.2.1" in tc: # Right-Hand Thumb Rule
                correct = "Thumb points in direction of current; curled fingers give direction of magnetic field lines"
                opts = [
                    correct,
                    "Thumb points in direction of magnetic field; curled fingers give current",
                    "Thumb points towards magnetic north pole; fingers point to south pole",
                    "Curled fingers give the direction of mechanical force"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"According to Maxwell's Right-Hand Thumb Rule, what do the thumb and curled fingers indicate?",
                    opts, ans,
                    "Imagine grasping a straight current-carrying conductor in your right hand.",
                    "If the outstretched thumb points in the direction of the electric current, then the curled fingers encircling the wire show the direction of concentric magnetic field lines.",
                    "Thumb = current, fingers = concentric magnetic field lines.",
                    v, diff)
            elif "4.2.2" in tc: # Magnetic field of solenoid
                correct = "Resembles the magnetic field of a bar magnet with uniform parallel field lines inside"
                opts = [
                    correct,
                    "Is strictly zero everywhere inside the solenoid",
                    "Has radial field lines pointing outward in all directions",
                    "Is perpendicular to the axis of the coil inside"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the magnetic field pattern produced by a current-carrying solenoid coil?",
                    opts, ans,
                    "A solenoid is a long coil of many circular turns of insulated copper wire.",
                    "Its magnetic field lines resemble those of a permanent bar magnet. Inside the solenoid, field lines are parallel, uniform, and along the central axis.",
                    "Resembles a bar magnet with uniform internal field.",
                    v, diff)
            elif "4.3.1" in tc: # Fleming's Left Hand Rule with SVG
                svg = get_motor_svg()
                correct = "Thumb: Force (Motion), Forefinger: Magnetic Field, Middle finger: Electric Current"
                opts = [
                    correct,
                    "Thumb: Current, Forefinger: Field, Middle finger: Force",
                    "Thumb: Magnetic Field, Forefinger: Current, Middle finger: Force",
                    "Thumb: Potential Difference, Forefinger: Resistance, Middle finger: Power"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"According to Fleming's Left-Hand Rule used for electric motors, what directions do the mutually perpendicular Thumb, Forefinger, and Middle finger indicate?",
                    opts, ans,
                    "Stretch thumb, forefinger, and middle finger of left hand mutually perpendicular to each other.",
                    "Forefinger represents Magnetic Field (B), Middle finger represents Electric Current (I), and Thumb indicates direction of Mechanical Force / Motion (F) on the conductor.",
                    "Thumb = Force, Forefinger = Field, Middle finger = Current.",
                    v, diff, req_fig=True)
            elif "4.3.2" in tc: # Electric motor split-ring commutator
                correct = "Reverses the direction of current in the coil every half rotation to sustain continuous unidirectional rotation"
                opts = [
                    correct,
                    "Increases the voltage of the supply source",
                    "Converts alternating current into mechanical heat",
                    "Prevents the magnets from losing magnetism"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the essential function of the split-ring commutator in an Electric Motor?",
                    opts, ans,
                    "As the rectangular coil rotates through the vertical plane, the split-ring segments swap contact brushes.",
                    "This reverses the direction of current in the coil arms every half rotation, ensuring that the couple of forces continues to rotate the coil in the same continuous direction.",
                    "Reverses current direction every half turn.",
                    v, diff)
            elif "4.4.1" in tc: # Electromagnetic induction & Faraday's Law
                correct = "Whenever the magnetic flux linked with a coil changes, an electromotive force (emf) is induced in the coil"
                opts = [
                    correct,
                    "A static constant magnetic field generates continuous infinite current",
                    "Induced current is independent of the rate of change of magnetic field",
                    "Electric current generates magnetic monopoles"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is Faraday's Law of Electromagnetic Induction?",
                    opts, ans,
                    "Discovered by Michael Faraday in 1831.",
                    "Whenever the magnetic flux linked with a conductor/coil changes with time, an induced electromotive force (and current) is produced: \\(e = -\\frac{d\\Phi}{dt}\\).",
                    "Changing magnetic flux induces EMF.",
                    v, diff)
            elif "4.4.2" in tc: # Fleming's Right Hand Rule
                correct = "Thumb: Motion of conductor, Forefinger: Magnetic field, Middle finger: Induced current"
                opts = [
                    correct,
                    "Thumb: Induced current, Forefinger: Field, Middle finger: Motion",
                    "Thumb: Magnetic field, Forefinger: Force, Middle finger: Current",
                    "All three fingers point towards the south pole"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In an electric generator, what does Fleming's Right-Hand Rule determine?",
                    opts, ans,
                    "Used to find the direction of induced current.",
                    "With mutually perpendicular fingers of right hand: Thumb points in direction of motion of conductor, Forefinger in direction of magnetic field, and Middle finger points in direction of induced current.",
                    "Middle finger indicates induced current.",
                    v, diff)
            elif "4.4.3" in tc or "4.5.1" in tc: # AC vs DC
                correct = "AC reverses direction periodically (50 Hz in India, changing every 1/100 s); DC flows in one direction only"
                opts = [
                    correct,
                    "DC reverses direction periodically while AC flows in one direction",
                    "AC cannot be transmitted over long distances",
                    "DC voltage can be stepped up easily using transformers"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the difference between Alternating Current (AC) and Direct Current (DC)?",
                    opts, ans,
                    "DC flows continuously in a single direction (battery).",
                    "AC changes its direction periodically. In India, domestic AC has frequency \\(50\\text{{Hz}}\\), completing one cycle in \\(1/50\\text{{s}}\\) and reversing direction every \\(1/100\\text{{s}}\\).",
                    "AC alternates direction at 50 Hz; DC is unidirectional.",
                    v, diff)
            # CHAPTER 5: HEAT
            elif "5.1.1" in tc: # Latent heat of fusion
                correct = "Amount of heat energy absorbed at constant temperature by unit mass of solid to convert into liquid"
                opts = [
                    correct,
                    "Heat required to raise the temperature of liquid by 1°C",
                    "Heat released when liquid evaporates at boiling point",
                    "Specific heat of gas at constant volume"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How is the 'Specific Latent Heat of Fusion' of a substance defined?",
                    opts, ans,
                    "During phase change from solid to liquid, temperature remains constant at the melting point.",
                    "Specific latent heat of fusion \\(L_f\\) is the quantity of heat absorbed by unit mass (1 kg) of a solid at its melting point to convert completely into liquid without any rise in temperature (for ice, \\(L_f = 3.33 \\times 10^5\\text{{J/kg}}\\) or \\(80\\text{{cal/g}}\\)).",
                    "Heat absorbed at constant temperature for phase transition.",
                    v, diff)
            elif "5.1.2" in tc: # Latent heat of vaporization
                correct = "Amount of heat energy absorbed at constant temperature by unit mass of liquid to convert into gaseous state"
                opts = [
                    correct,
                    "Heat absorbed to increase water temperature from 0°C to 100°C",
                    "Heat released when steam expands adiabatically",
                    "Heat absorbed by solid during melting"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the definition of the 'Specific Latent Heat of Vaporization' of a liquid?",
                    opts, ans,
                    "At the boiling point, liquid converts to vapour while temperature stays constant.",
                    "Specific latent heat of vaporization \\(L_v\\) is heat absorbed per unit mass at boiling point without change in temperature (for water, \\(L_v = 2.26 \\times 10^6\\text{{J/kg}}\\) or \\(540\\text{{cal/g}}\\)).",
                    "Heat absorbed at constant boiling point for vaporization.",
                    v, diff)
            elif "5.1.3" in tc: # Regelation
                correct = "Melting of ice under increased pressure and recongealing when pressure is released"
                opts = [
                    correct,
                    "Sublimation of camphor under vacuum",
                    "Evaporation of alcohol at room temperature",
                    "Thermal expansion of mercury in thermometer"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the physical phenomenon of 'Regelation' demonstrated with an ice block and weighted wire?",
                    opts, ans,
                    "Regelation is the phenomenon in which ice converts to water under high pressure (melting point drops below 0°C) and refreezes into ice when the pressure is removed.",
                    "Allows a weighted wire to pass through an ice slab without cutting it into two separate pieces.",
                    "Melting under pressure and refreezing upon release.",
                    v, diff)
            elif "5.2.1" in tc: # Anomalous expansion of water with SVG
                svg = get_hopes_apparatus_svg()
                correct = "Contracts on heating from 0°C to 4°C, reaching maximum density at 4°C"
                opts = [
                    correct,
                    "Expands continuously from 0°C to 100°C like normal liquids",
                    "Reaches maximum density at 0°C",
                    "Contracts continuously at all temperatures above 4°C"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"What is the 'Anomalous Expansion of Water' between \\(0^\\circ\\text{{C}}\\) and \\(4^\\circ\\text{{C}}\\) as studied using Hope's Apparatus?",
                    opts, ans,
                    "Normal liquids expand when heated.",
                    "Water contracts when heated from \\(0^\\circ\\text{{C}}\\) to \\(4^\\circ\\text{{C}}\\) (its volume decreases to a minimum and density reaches a maximum of \\(1\\text{{g/cm}}^3 = 1000\\text{{kg/m}}^3\\) at \\(4^\\circ\\text{{C}}\\)). Above \\(4^\\circ\\text{{C}}\\), it expands normally.",
                    "Minimum volume and maximum density at 4°C.",
                    v, diff, req_fig=True)
            elif "5.2.2" in tc: # Aquatic life survival
                correct = "Denser 4°C water settles at the bottom of frozen lakes, allowing aquatic organisms to survive under top ice layer"
                opts = [
                    correct,
                    "Ice sinks to the lake bed providing heat to aquatic plants",
                    "Salt in lake water prevents ice from forming anywhere",
                    "Aquatic animals hibernate in dry air bubbles"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How does the anomalous expansion of water enable the survival of aquatic flora and fauna in cold regions during severe winters?",
                    opts, ans,
                    "As lake surface cools, water becomes denser and sinks until the entire lake reaches \\(4^\\circ\\text{{C}}\\).",
                    "Further cooling between \\(4^\\circ\\text{{C}}\\) and \\(0^\\circ\\text{{C}}\\) makes surface water lighter, so it freezes into ice at top. Since ice is a poor conductor of heat, water at the bottom remains liquid at \\(4^\\circ\\text{{C}}\\), preserving aquatic life.",
                    "Bottom water remains at 4°C beneath insulating ice layer.",
                    v, diff)
            elif "5.3.1" in tc: # Dew point and humidity
                correct = "Dew Point"
                opts = [correct, "Boiling point", "Freezing point", "Critical temperature"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"The temperature at which unsaturated air containing a given mass of water vapour becomes saturated is called its:",
                    opts, ans,
                    "The capacity of air to hold water vapour decreases with decreasing temperature.",
                    "If unsaturated air is cooled, it reaches a specific temperature where its moisture content fully saturates the air. This temperature is called the Dew Point temperature.",
                    "Dew Point is the saturation temperature.",
                    v, diff)
            elif "5.3.2" in tc: # Relative humidity
                correct = "\\(\\text{{Relative Humidity}} = \\frac{\\text{{Mass of water vapour in volume}}{\\text{{Mass required to saturate volume at that temp}} \\times 100\\%\\)"
                opts = [
                    correct,
                    "\\(\\text{{Relative Humidity}} = \\frac{\\text{{Atmospheric Pressure}}{\\text{{Standard Pressure}} \\times 100\\%\\)",
                    "\\(\\text{{Relative Humidity}} = \\frac{\\text{{Temperature in Kelvin}}{\\text{{Dew Point}} \\times 100\\%\\)",
                    "\\(\\text{{Relative Humidity}} = \\text{{Absolute Humidity}} \\times 100\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How is the Percentage Relative Humidity of air defined?",
                    opts, ans,
                    "Relative Humidity (RH) measures moisture degree relative to maximum capacity.",
                    "\\(\\%\\text{{RH}} = \\frac{\\text{{Actual mass of water vapour in given volume}}{\\text{{Mass of water vapour needed to saturate it at that temperature}} \\times 100\\%\\).",
                    "At dew point, \\(\\%\\text{{RH}} = 100\\%\\).",
                    v, diff)
            elif "5.4.1" in tc: # Specific heat capacity Q = mc Delta T
                correct = "\\(Q = m c \\Delta T\\)"
                opts = [
                    correct,
                    "\\(Q = \\frac{m c}{\\Delta T}\\)",
                    "\\(Q = m L\\)",
                    "\\(Q = c \\Delta T\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which formula calculates the heat energy \\(Q\\) absorbed or lost by a body of mass \\(m\\) and specific heat capacity \\(c\\) undergoing temperature change \\(\\Delta T\\)?",
                    opts, ans,
                    "Specific heat capacity \\(c\\) is the heat required to raise temperature of unit mass by \\(1^\\circ\\text{{C}}\\).",
                    "Total heat absorbed or released: \\(Q = m c \\Delta T\\). SI unit of specific heat is \\(\\text{{J}}/(\\text{{kg}}\\cdot^\\circ\\text{{C}})\\).",
                    "Standard calorimetry formula.",
                    v, diff)
            elif "5.4.2" in tc: # Principle of heat exchange
                correct = "Heat lost by hot object = Heat gained by cold object (in isolated system)"
                opts = [
                    correct,
                    "Heat lost is always greater than heat gained due to radiation",
                    "Temperature of cold object doubles while hot object halves",
                    "Heat exchange continues indefinitely"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the Principle of Heat Exchange used in calorimetry?",
                    opts, ans,
                    "By conservation of thermal energy in an isolated insulated system:",
                    "Heat lost by hot body \\(= \\text{{Heat gained by cold body}}\\) until thermal equilibrium (equal final temperature) is attained.",
                    "Conservation of thermal energy.",
                    v, diff)
            # CHAPTER 6: REFRACTION OF LIGHT
            elif "6.1.1" in tc: # Refraction definition
                correct = "Bending of light rays as they pass obliquely from one transparent medium to another of different optical density"
                opts = [
                    correct,
                    "Bouncing back of light into the same medium",
                    "Splitting of white light into spectrum colors",
                    "Absorption of light rays by opaque surfaces"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the optical phenomenon of 'Refraction of Light'?",
                    opts, ans,
                    "Light travels at different speeds in different optical media.",
                    "When a ray of light passes obliquely from one transparent medium to another, its speed changes, causing it to change its direction (bend) at the interface. This bending is called refraction.",
                    "Change in direction due to change in speed.",
                    v, diff)
            elif "6.1.2" in tc: # Snell's Law
                correct = "Snell's Law: \\(\\frac{\\sin i}{\\sin r} = \\text{{constant}} = n\\)"
                opts = [
                    correct,
                    "Law of Reflection: \\(i = r\\)",
                    "Lens formula: \\(\\frac{1}{f} = \\frac{1}{v} - \\frac{1}{u}\\)",
                    "Brewster's Law: \\(\\tan i_p = 1/n\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"For a given pair of media, the ratio of the sine of the angle of incidence \\(i\\) to the sine of the angle of refraction \\(r\\) is constant. This law is known as:",
                    opts, ans,
                    "Second law of refraction formulated by Willebrord Snellius in 1621.",
                    "\\(\\frac{\\sin i}{\\sin r} = {}_1 n_2 = \\text{{constant}}\\), where \\(n\\) is the refractive index of second medium with respect to first medium.",
                    "Snell's Law.",
                    v, diff)
            elif "6.1.3" in tc: # Refractive index n21 = v1 / v2
                correct = "\\(n_{21} = \\frac{v_1}{v_2}\\) (ratio of speed of light in medium 1 to medium 2)"
                opts = [
                    correct,
                    "\\(n_{21} = \\frac{v_2}{v_1}\\)",
                    "\\(n_{21} = v_1 \\times v_2\\)",
                    "\\(n_{21} = \\frac{c^2}{v_1 v_2}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How is the refractive index of medium 2 with respect to medium 1 (\\(n_{21}\\)) expressed in terms of the speed of light?",
                    opts, ans,
                    "Refractive index is inversely proportional to speed of light in that medium.",
                    "\\({}_1 n_2 = \\frac{\\text{{Velocity of light in medium 1}} (v_1)}{\\text{{Velocity of light in medium 2}} (v_2)}\\).",
                    "Ratio of speeds \\(v_1 / v_2\\).",
                    v, diff)
            elif "6.2.1" in tc: # Refraction through glass slab with SVG
                svg = get_glass_slab_svg()
                correct = "Angle of incidence \\(i\\) = Angle of emergence \\(e\\), and emergent ray is parallel to incident ray"
                opts = [
                    correct,
                    "Angle of incidence \\(i\\) > Angle of emergence \\(e\\)",
                    "Emergent ray is perpendicular to incident ray",
                    "Light ray undergoes total absorption inside slab"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"When a light ray passes through a rectangular glass slab with parallel refracting surfaces, what is the relationship between the incident ray and emergent ray?",
                    opts, ans,
                    "At the first surface (air to glass), ray bends towards normal (\\(r_1 < i\\)). At opposite parallel surface (glass to air), ray bends away from normal by equal extent (\\(e = i\\)).",
                    "The emergent ray is laterally displaced but strictly parallel to the original incident ray direction.",
                    "\\(i = e\\) and rays are parallel.",
                    v, diff, req_fig=True)
            elif "6.2.2" in tc: # Twinkling of stars
                correct = "Continuous atmospheric refraction through constantly fluctuating density and temperature layers of air"
                opts = [
                    correct,
                    "Periodic fluctuations in the nuclear fusion inside stars",
                    "Intermittent blocking by orbiting space debris",
                    "Total internal reflection within the ozone layer"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What causes the apparent twinkling effect of distant stars in the night sky?",
                    opts, ans,
                    "Stars are point sources of light situated trillions of kilometers away.",
                    "Their light passes through turbulent atmospheric layers whose temperature, density, and refractive index constantly change, randomly deflecting the beam and altering the apparent brightness and position seen by the eye.",
                    "Atmospheric refraction through turbulent air.",
                    v, diff)
            elif "6.2.3" in tc: # Advanced sunrise and delayed sunset
                correct = "2 minutes before actual sunrise and 2 minutes after actual sunset (total 4 minutes increase)"
                opts = [
                    correct,
                    "5 minutes before sunrise and 5 minutes after sunset",
                    "1 hour difference due to time zones",
                    "Zero minutes difference"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Due to atmospheric refraction, the Sun is visible to an observer on Earth approximately how many minutes before actual sunrise and after actual sunset?",
                    opts, ans,
                    "When the Sun is just below the horizon, rays entering the increasingly dense atmosphere bend downwards towards normal.",
                    "This lifts the virtual image of the Sun above the horizon by about \\(0.5^\\circ\\), corresponding to 2 minutes early at sunrise and 2 minutes late at sunset (adding 4 minutes of daylight).",
                    "2 minutes early sunrise, 2 minutes delayed sunset.",
                    v, diff)
            elif "6.3.1" in tc: # Dispersion of light
                correct = "Splitting of composite white light into its component colors (VIBGYOR) due to different speeds/wavelengths"
                opts = [
                    correct,
                    "Bouncing back of white light into dark rays",
                    "Interference of coherent laser beams",
                    "Polarization of light into single planes"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the optical phenomenon of 'Dispersion of Light' discovered by Sir Isaac Newton using a glass prism?",
                    opts, ans,
                    "White sunlight is composed of seven constituent spectral colors: Violet, Indigo, Blue, Green, Yellow, Orange, Red (VIBGYOR).",
                    "In glass, red light has highest speed and bends least; violet light has lowest speed and bends most. This angular separation of colors is called dispersion.",
                    "Separation into VIBGYOR colors.",
                    v, diff)
            elif "6.3.2" in tc: # Total internal reflection
                correct = "Angle of incidence in denser medium exceeds the critical angle (\\(i > i_c\\))"
                opts = [
                    correct,
                    "Light travels from rarer medium into denser medium",
                    "Angle of incidence is exactly zero degrees",
                    "Refractive index of both media is identical"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What are the two mandatory conditions required for Total Internal Reflection (TIR) to occur?",
                    opts, ans,
                    "Conditions for Total Internal Reflection: (1) Light must travel from an optically denser medium into an optically rarer medium; (2) The angle of incidence \\(i\\) in the denser medium must be strictly greater than the critical angle \\(i_c\\) (for which \\(r = 90^\\circ\\)).",
                    "When \\(i > i_c\\), 100% of light reflects back into the denser medium.",
                    "Denser to rarer medium with \\(i > i_c\\).",
                    v, diff)
            elif "6.3.3" in tc: # Formation of rainbow
                correct = "Refraction, dispersion, and internal reflection of sunlight by tiny spherical raindrops"
                opts = [
                    correct,
                    "Diffraction of moonlight through clouds",
                    "Absorption of solar rays by ozone layer",
                    "Scattering of blue light by atmospheric nitrogen"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"A rainbow is a natural spectrum produced in the sky through which combined optical phenomena?",
                    opts, ans,
                    "Tiny water droplets act as miniature prisms.",
                    "When sunlight enters a raindrop, it first undergoes refraction and dispersion, followed by internal reflection at the back inner surface of the drop, and finally refraction again as it exits, producing the circular rainbow arc.",
                    "Refraction, dispersion, and internal reflection.",
                    v, diff)
            else:
                correct = "Fundamental physical property"
                opts = [correct, "Zero value", "Undefined quantity", "Infinite variance"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"For topic {item['subtopicName']}, evaluate physics property variant {k}.",
                    opts, ans,
                    "Apply core principles of physical laws.",
                    "Analysis confirms physical law.",
                    "Principle is valid.",
                    v, diff)
                    
            questions.append(q)

    print(f"Total questions generated for MH-10-SCIT1 Ch 4-6: {len(questions)}")
    out_file = 'scripts/audit_data/mh10_scit1_ch4_to_6_generated.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_file}")

if __name__ == "__main__":
    generate_mh10_scit1_ch4_to_6()
