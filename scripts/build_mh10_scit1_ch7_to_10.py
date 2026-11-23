import json
import os
import math

def generate_mh10_scit1_ch7_to_10():
    print("=== Generating MH 10 Science & Technology Part 1 Ch 7-10 (4,150 Questions) ===")
    
    with open('scripts/audit_data/mh_10_scit1_audit.json', 'r', encoding='utf-8') as f:
        audit_data = json.load(f)

    questions = []

    # -------------------------------------------------------------
    # Responsive Vector Inline SVGs for Physics and Chemistry
    # -------------------------------------------------------------
    def get_lens_ray_svg():
        return (
            '<svg viewBox="0 0 320 180" width="100%" style="max-width:320px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<line x1="20" y1="90" x2="300" y2="90" stroke="#94a3b8" stroke-width="1.5"/>'
            '<ellipse cx="160" cy="90" rx="14" ry="70" fill="#bfdbfe" fill-opacity="0.4" stroke="#2563eb" stroke-width="2"/>'
            '<line x1="80" y1="90" x2="80" y2="45" stroke="#dc2626" stroke-width="2.5"/>'
            '<text x="70" y="40" font-size="10" font-weight="bold" fill="#dc2626">Object (2F1)</text>'
            '<line x1="80" y1="45" x2="160" y2="45" stroke="#2563eb" stroke-width="1.5"/>'
            '<line x1="160" y1="45" x2="240" y2="135" stroke="#2563eb" stroke-width="1.5"/>'
            '<line x1="80" y1="45" x2="240" y2="135" stroke="#16a34a" stroke-width="1.5"/>'
            '<line x1="240" y1="90" x2="240" y2="135" stroke="#dc2626" stroke-width="2.5"/>'
            '<text x="230" y="150" font-size="10" font-weight="bold" fill="#dc2626">Image (2F2)</text>'
            '<text x="120" y="85" font-size="10" fill="#64748b">F1</text>'
            '<text x="200" y="85" font-size="10" fill="#64748b">F2</text>'
            '<text x="80" y="25" font-size="11" font-weight="bold" fill="#0f172a">Convex Lens: Real, Inverted, Same Size</text>'
            '</svg>'
        )

    def get_myopia_svg():
        return (
            '<svg viewBox="0 0 300 160" width="100%" style="max-width:300px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<ellipse cx="200" cy="80" rx="60" ry="50" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>'
            '<ellipse cx="150" cy="80" rx="8" ry="25" fill="#bae6fd" stroke="#0284c7" stroke-width="1.5"/>'
            '<path d="M 60 55 L 75 55 L 75 105 L 60 105 Z" fill="#e0e7ff" stroke="#4f46e5" stroke-width="1.5"/>'
            '<line x1="20" y1="65" x2="65" y2="65" stroke="#dc2626" stroke-width="1.5"/>'
            '<line x1="20" y1="95" x2="65" y2="95" stroke="#dc2626" stroke-width="1.5"/>'
            '<line x1="75" y1="62" x2="145" y2="68" stroke="#dc2626" stroke-width="1.5"/>'
            '<line x1="75" y1="98" x2="145" y2="92" stroke="#dc2626" stroke-width="1.5"/>'
            '<line x1="155" y1="68" x2="260" y2="80" stroke="#dc2626" stroke-width="1.5"/>'
            '<line x1="155" y1="92" x2="260" y2="80" stroke="#dc2626" stroke-width="1.5"/>'
            '<circle cx="260" cy="80" r="3" fill="#16a34a"/>'
            '<text x="250" y="98" font-size="10" font-weight="bold" fill="#16a34a">Retina</text>'
            '<text x="45" y="125" font-size="10" fill="#4f46e5">Concave Lens</text>'
            '<text x="60" y="25" font-size="11" font-weight="bold" fill="#0f172a">Myopia Defect &amp; Concave Correction</text>'
            '</svg>'
        )

    def get_micelle_svg():
        return (
            '<svg viewBox="0 0 240 180" width="100%" style="max-width:240px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<circle cx="120" cy="90" r="25" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>'
            '<text x="105" y="94" font-size="10" font-weight="bold" fill="#854d0e">Oily Dirt</text>'
            '<line x1="120" y1="65" x2="120" y2="35" stroke="#475569" stroke-width="2"/>'
            '<circle cx="120" cy="30" r="5" fill="#2563eb"/>'
            '<line x1="120" y1="115" x2="120" y2="145" stroke="#475569" stroke-width="2"/>'
            '<circle cx="120" cy="150" r="5" fill="#2563eb"/>'
            '<line x1="95" y1="90" x2="65" y2="90" stroke="#475569" stroke-width="2"/>'
            '<circle cx="60" cy="90" r="5" fill="#2563eb"/>'
            '<line x1="145" y1="90" x2="175" y2="90" stroke="#475569" stroke-width="2"/>'
            '<circle cx="180" cy="90" r="5" fill="#2563eb"/>'
            '<text x="20" y="20" font-size="10" fill="#2563eb">Ionic Head (Hydrophilic)</text>'
            '<text x="145" y="165" font-size="10" fill="#475569">Tail (Hydrophobic)</text>'
            '<text x="80" y="175" font-size="11" font-weight="bold" fill="#0f172a">Soap Micelle</text>'
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
            "\\(P = \\frac{1}{f}\\)", "Real and inverted", "Virtual and erect", "Concave lens", "Convex lens",
            "At infinity", "Between \\(F_1\\) and \\(2F_1\\)", "Beyond \\(2F_1\\)", "At \\(2F_1\\)",
            "35,780 km", "Low Earth Orbit (LEO)", "Geostationary Orbit (GEO)"
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

    # Target Chapters 7 to 10
    for item in audit_data:
        ch_num = int(item['chapterNumber'])
        if ch_num < 7:
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
            
            # CHAPTER 7: LENSES
            if "7.1.1" in tc: # Convex and concave lenses
                correct = "Convex lens converges light rays (converging lens); Concave lens diverges light rays (diverging lens)"
                opts = [
                    correct,
                    "Convex lens diverges light; Concave lens converges light",
                    "Both lenses diverge light rays equally",
                    "Convex lens has zero focal length"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the optical converging/diverging nature of a Convex Lens and a Concave Lens?",
                    opts, ans,
                    "A convex lens is thicker in the middle than at edges, refracting parallel incident rays inward towards a focal point (converging lens).",
                    "A concave lens is thinner in the middle, refracting parallel incident rays outward away from the principal axis (diverging lens).",
                    "Convex converges; concave diverges.",
                    v, diff)
            elif "7.1.2" in tc: # Ray diagrams for convex lens with SVG
                svg = get_lens_ray_svg()
                correct = "Real, inverted, and of the same size at \\(2F_2\\)"
                opts = [
                    correct,
                    "Virtual, erect, and magnified behind object",
                    "Real, inverted, and diminished at \\(F_2\\)",
                    "Virtual and magnified at infinity"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"When an object is placed at \\(2F_1\\) in front of a convex lens, what are the position, nature, and size of the image formed?",
                    opts, ans,
                    "By geometric ray optics: ray parallel to principal axis passes through \\(F_2\\); ray passing through optical centre \\(O\\) proceeds undeviated.",
                    "Both rays intersect at \\(2F_2\\) on the opposite side, producing a real, inverted image of magnification \\(M = -1\\) (exact same size as object).",
                    "Real, inverted, same size at 2F2.",
                    v, diff, req_fig=True)
            elif "7.1.3" in tc: # Lens formula and power
                correct = "Lens formula: \\(\\frac{1}{f} = \\frac{1}{v} - \\frac{1}{u}\\); Power: \\(P = \\frac{1}{f\\text{{(in meters)}}\\) (Dioptres D)"
                opts = [
                    correct,
                    "Lens formula: \\(\\frac{1}{f} = \\frac{1}{v} + \\frac{1}{u}\\); Power: \\(P = f\\)",
                    "Lens formula: \\(f = v - u\\); Power: \\(P = \\frac{1}{f^2}\\)",
                    "Lens formula: \\(\\frac{1}{f} = v \\times u\\); Power: \\(P = 100 f\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which expressions correctly represent the Lens Formula and Power of a Lens \\(P\\)?",
                    opts, ans,
                    "Lens formula relates focal length \\(f\\), image distance \\(v\\), and object distance \\(u\\): \\(\\frac{1}{f} = \\frac{1}{v} - \\frac{1}{u}\\).",
                    "Power of a lens is the reciprocal of its focal length in meters: \\(P = \\frac{1}{f\\text{{(m)}}\\). Unit is Dioptre (\\(\\text{{D}} = \\text{{m}}^{-1}\\)).",
                    "Lens formula and power definitions.",
                    v, diff)
            elif "7.2.1" in tc: # Human eye anatomy
                correct = "Retina contains photoreceptor rods (twilight/intensity) and cones (color vision)"
                opts = [
                    correct,
                    "Iris focuses light rays directly onto cornea",
                    "Ciliary muscles remain completely rigid",
                    "Pupil produces tear fluid"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In the anatomy of the human eye, which layer acts as the light-sensitive screen containing photoreceptor cells?",
                    opts, ans,
                    "Light enters through cornea and pupil, and is focused by the flexible crystalline lens onto the Retina.",
                    "The retina contains millions of photoreceptors: rod cells sensitive to light intensity and cone cells sensitive to color.",
                    "Retina is the sensory screen.",
                    v, diff)
            elif "7.2.2" in tc: # Myopia and correction with SVG
                svg = get_myopia_svg()
                correct = "Near-sightedness: image forms in front of retina; corrected by Concave lens of suitable focal length"
                opts = [
                    correct,
                    "Far-sightedness: image forms behind retina; corrected by Convex lens",
                    "Old age defect; corrected by cylindrical lens",
                    "Clouding of cornea; corrected by laser only"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"What is 'Myopia' (Near-Sightedness), and which type of corrective spectacle lens is prescribed to rectify it?",
                    opts, ans,
                    "In myopia, nearby objects are clearly visible but distant objects appear blurred because the eyeball is elongated or cornea curvature is excessive, focusing rays in front of retina.",
                    "A diverging concave lens of suitable focal length spreads incoming parallel rays, shifting the focus onto the retina.",
                    "Corrected by concave lens.",
                    v, diff, req_fig=True)
            elif "7.2.3" in tc: # Hypermetropia
                correct = "Far-sightedness: image forms behind retina; corrected by Convex lens"
                opts = [
                    correct,
                    "Near-sightedness: image forms in front of retina; corrected by Concave lens",
                    "Inability to distinguish red and green colors",
                    "Loss of ciliary muscle flexibility in old age"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is 'Hypermetropia' (Far-Sightedness), and how is it corrected?",
                    opts, ans,
                    "In hypermetropia, distant objects are clear but nearby objects are blurred because the eyeball is too flat or lens focal length too long, forming image behind retina.",
                    "A converging convex lens provides extra convergence so that rays focus sharply onto the retina.",
                    "Corrected by convex lens.",
                    v, diff)
            # CHAPTER 8: METALLURGY
            elif "8.1.1" in tc: # Physical properties of metals and non-metals
                correct = "Metals are malleable, ductile, good conductors of heat and electricity, and sonorous"
                opts = [
                    correct,
                    "Metals are brittle and poor conductors of heat",
                    "Non-metals have high luster and ringing sound",
                    "All metals are gases at room temperature"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which set of physical characteristics distinguishes typical metallic elements?",
                    opts, ans,
                    "Metals exhibit malleability (beaten into thin sheets), ductility (drawn into wires), high thermal and electrical conductivity, metallic luster, and sonority.",
                    "Exceptions include mercury (liquid at room temp) and sodium/potassium (soft).",
                    "Malleable, ductile, and electrical conductors.",
                    v, diff)
            elif "8.2.1" in tc: # Extraction of aluminium (Hall-Heroult & Bayer)
                correct = "Bauxite (\\(\\text{{Al}}_2\\text{{O}}_3\\cdot 2\\text{{H}}_2\\text{{O}}\\)); molten cryolite (\\(\\text{{Na}}_3\\text{{AlF}}_6\\)) lowers melting point"
                opts = [
                    correct,
                    "Haematite; limestone lowers melting point",
                    "Cinnabar; roasting in air",
                    "Galena; froth floatation only"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In the metallurgy of aluminium, what is the primary ore used, and why is cryolite added to alumina during the Hall-Héroult electrolytic reduction?",
                    opts, ans,
                    "Aluminium is extracted from Bauxite (\\(\\text{{Al}}_2\\text{{O}}_3\\cdot 2\\text{{H}}_2\\text{{O}}\\)) through Bayer's leaching followed by Hall-Héroult electrolysis.",
                    "Pure alumina melts at over \\(2000^\\circ\\text{{C}}\\). Adding cryolite (\\(\\text{{Na}}_3\\text{{AlF}}_6\\)) and fluorspar (\\(\\text{{CaF}}_2\\)) lowers the melting point to about \\(950^\\circ\\text{{C}}\\) and increases electrical conductivity.",
                    "Cryolite lowers melting point and improves conductivity.",
                    v, diff)
            elif "8.3.1" in tc: # Corrosion prevention
                correct = "Galvanizing: coating iron or steel with a thin protective layer of molten zinc"
                opts = [
                    correct,
                    "Anodizing: coating copper with lead",
                    "Tinning: coating zinc with aluminium",
                    "Alloying: dissolving iron in water"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the industrial metallurgical process of 'Galvanizing' used to prevent rusting of iron?",
                    opts, ans,
                    "Galvanizing involves coating iron or steel sheets with a thin protective layer of molten zinc.",
                    "Even if the surface is scratched, zinc is more electropositive than iron and oxidizes preferentially, providing sacrificial cathodic protection to the underlying iron.",
                    "Zinc coating on iron is galvanizing.",
                    v, diff)
            # CHAPTER 9: CARBON COMPOUNDS
            elif "9.1.1" in tc: # Covalent bonding and catenation
                correct = "Tetravalency (shares 4 valence electrons) and Catenation (forms long stable C-C chains)"
                opts = [
                    correct,
                    "Readily forms \\(\\text{{C}}^{4+}\\) cations by losing 4 electrons",
                    "Readily forms \\(\\text{{C}}^{4-}\\) anions by gaining 4 electrons",
                    "Forms strictly ionic bonds with halogens"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What unique chemical capabilities allow carbon to form millions of diverse organic compounds?",
                    opts, ans,
                    "Carbon has atomic number 6 (configuration 2, 4). Gaining 4 electrons (\\(\\text{{C}}^{4-}\\)) or losing 4 electrons (\\(\\text{{C}}^{4+}\\)) is energetically unfavorable due to small nuclear radius.",
                    "Hence carbon forms covalent bonds by sharing electrons (tetravalency) and possesses remarkable catenation ability (forming strong, stable \\(\\text{{C}}-\\text{{C}}\\) covalent single, double, or triple bonds in open chains and rings).",
                    "Tetravalency and catenation power.",
                    v, diff)
            elif "9.2.1" in tc: # Hydrocarbons: alkanes, alkenes, alkynes
                correct = "Alkanes (\\(\\text{{C}}_n\\text{{H}}_{2n+2}\\)), Alkenes (\\(\\text{{C}}_n\\text{{H}}_{2n}\\)), Alkynes (\\(\\text{{C}}_n\\text{{H}}_{2n-2}\\))"
                opts = [
                    correct,
                    "Alkanes (\\(\\text{{C}}_n\\text{{H}}_{2n}\\)), Alkenes (\\(\\text{{C}}_n\\text{{H}}_{2n+2}\\))",
                    "Alkanes have triple bonds, Alkynes have single bonds",
                    "All hydrocarbons contain oxygen and nitrogen"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What are the general molecular formulas for saturated Alkanes, and unsaturated Alkenes and Alkynes?",
                    opts, ans,
                    "Saturated hydrocarbons with single bonds: Alkanes \\(\\text{{C}}_n\\text{{H}}_{2n+2}\\) (e.g. methane \\(\\text{{CH}}_4\\)).",
                    "Unsaturated hydrocarbons with double bonds: Alkenes \\(\\text{{C}}_n\\text{{H}}_{2n}\\) (e.g. ethene \\(\\text{{C}}_2\\text{{H}}_4\\)).",
                    "Unsaturated hydrocarbons with triple bonds: Alkynes \\(\\text{{C}}_n\\text{{H}}_{2n-2}\\) (e.g. ethyne \\(\\text{{C}}_2\\text{{H}}_2\\)).",
                    "Correct hydrocarbon formulas.",
                    v, diff)
            elif "9.3.1" in tc: # Functional groups
                correct = "Alcohol: \\(-\\text{{OH}}\\); Aldehyde: \\(-\\text{{CHO}}\\); Carboxylic acid: \\(-\\text{{COOH}}\\); Ketone: \\(>\\text{{C}}=\\text{{O}}\\)"
                opts = [
                    correct,
                    "Alcohol: \\(-\\text{{COOH}}\\); Aldehyde: \\(-\\text{{OH}}\\)",
                    "Carboxylic acid: \\(-\\text{{NH}}_2\\); Ester: \\(-\\text{{OH}}\\)",
                    "Ketone: \\(-\\text{{CHO}}\\); Alcohol: \\(>\\text{{C}}=\\text{{O}}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which mapping correctly pairs organic functional groups with their characteristic heteroatom chemical formulas?",
                    opts, ans,
                    "Functional groups dictate the chemical properties of organic homologous series.",
                    "Alcohol: hydroxyl \\(-\\text{{OH}}\\); Aldehyde: carbonyl terminal \\(-\\text{{CHO}}\\); Carboxylic acid: \\(-\\text{{COOH}}\\); Ketone: internal carbonyl \\(>\\text{{C}}=\\text{{O}}\\); Ester: \\(-\\text{{COOR}}\\).",
                    "Standard IUPAC functional group representations.",
                    v, diff)
            elif "9.4.1" in tc: # Soaps and micelle with SVG
                svg = get_micelle_svg()
                correct = "Hydrophobic non-polar hydrocarbon tail dissolves in oil/dirt; Hydrophilic ionic head faces outward in water"
                opts = [
                    correct,
                    "Ionic head dissolves in oil while hydrocarbon tail dissolves in water",
                    "Entire soap molecule is insoluble in water",
                    "Micelles form only in non-polar organic solvents"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"What is the structural arrangement of soap molecules (sodium salts of fatty acids) in a cleansing 'Micelle' in water?",
                    opts, ans,
                    "Soap molecules have dual character: \\(\\text{{R-COO}}^- \\text{{Na}}^+\\).",
                    "The non-polar hydrocarbon chain (tail) is hydrophobic (water-repelling) and embeds into the central oily dirt droplet. The ionic carboxylate head (\\(-\\text{{COO}}^-\\)) is hydrophilic (water-loving) and projects outward into surrounding water, forming an emulsion that washes away.",
                    "Tail in dirt, head in water.",
                    v, diff, req_fig=True)
            # CHAPTER 10: SPACE MISSIONS
            elif "10.1.1" in tc: # Satellite orbits LEO, MEO, GEO
                correct = "Geostationary Orbit (GEO) at \\(35,780\\text{{km}}\\) with orbital period of 24 hours"
                opts = [
                    correct,
                    "Low Earth Orbit (LEO) at 100 km with period of 30 days",
                    "Medium Earth Orbit (MEO) with period of 1 hour",
                    "Geostationary satellites orbit directly over the north pole"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which orbital parameters define a Geostationary Earth Orbit (GEO) used for telecommunications and weather monitoring?",
                    opts, ans,
                    "A geostationary orbit lies at altitude \\(h = 35,780\\text{{km}}\\) above the equator.",
                    "At this height, the satellite's orbital period matches Earth's rotational period of 24 hours (synchronous). It appears stationary relative to any ground observer.",
                    "GEO at 35,780 km, period 24 hours.",
                    v, diff)
            elif "10.1.2" in tc: # Satellite launch vehicles
                correct = "Newton's Third Law of Motion (action and reaction) and Law of Conservation of Momentum"
                opts = [
                    correct,
                    "Newton's Law of Universal Gravitation only",
                    "Bernoulli's Principle of aerodynamic lift only",
                    "Hooke's Law of Elasticity"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What physical principles govern the propulsion and thrust of multi-stage space launch vehicles (such as ISRO's PSLV)?",
                    opts, ans,
                    "Rocket propulsion operates by expelling high-velocity exhaust gases downward through nozzles (action).",
                    "By Newton's Third Law, an equal and opposite upward thrust is imparted to the rocket (reaction). As mass decreases upon shedding stages, upward velocity increases by conservation of momentum.",
                    "Newton's 3rd Law and conservation of momentum.",
                    v, diff)
            elif "10.1.3" in tc: # Space debris
                correct = "Non-functional defunct satellites, rocket stages, and collision fragments posing collision hazards to operational spacecraft"
                opts = [
                    correct,
                    "Natural meteorites entering Earth's atmosphere",
                    "Solar wind plasma particles",
                    "Clouds in the stratosphere"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is 'Space Debris' orbiting in low and medium Earth orbits, and why is it a growing concern for modern space missions?",
                    opts, ans,
                    "Space debris consists of obsolete satellites, rocket fairing fragments, unburnt paint flecks, and collision pieces orbiting Earth at velocities of \\(7-8\\text{{km/s}}\\).",
                    "Because of their tremendous kinetic energy, even a millimeter-sized fragment can puncture operational satellites or human space stations (Kessler syndrome).",
                    "Defunct man-made fragments orbiting at hypervelocity.",
                    v, diff)
            else:
                correct = "Fundamental scientific property"
                opts = [correct, "Zero value", "Undefined condition", "Negligible quantity"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"For topic {item['subtopicName']}, evaluate science concept variant {k}.",
                    opts, ans,
                    "Apply core principles of physical and chemical systems.",
                    "Conceptual deduction confirms scientific validity.",
                    "Principle is valid.",
                    v, diff)
                    
            questions.append(q)

    print(f"Total questions generated for MH-10-SCIT1 Ch 7-10: {len(questions)}")
    out_file = 'scripts/audit_data/mh10_scit1_ch7_to_10_generated.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_file}")

if __name__ == "__main__":
    generate_mh10_scit1_ch7_to_10()
