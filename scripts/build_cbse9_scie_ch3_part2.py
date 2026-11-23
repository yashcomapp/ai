import json
import re

def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        "Passive artifact of tissue collapse",
        "Non-vascular carbohydrate crystal",
        "Uncontrolled metabolic leakage"
    ]
    for d in default_distractors:
        if len(parts) >= 3:
            break
        if d not in parts:
            parts.append(d)
    return parts[:3]

def generate_vault_questions(topic_code, subtopic_name, archs):
    questions = []
    q_seq = 1

    for arch_idx, arch in enumerate(archs):
        templates = arch['templates']
        data_list = arch['data']
        calc_fn = arch['calc']
        diff = arch['diff']

        for i in range(10):
            template = templates[i % len(templates)]
            item = data_list[i % len(data_list)]

            correct_ans, wrong_choices, solution = calc_fn(item)
            q_text = template.format(*item)

            if q_seq <= 40:
                vault = 'exam'
            elif q_seq <= 60:
                vault = 'practice'
            else:
                vault = 'foundation'

            options_list = [
                {"id": "A", "text": correct_ans, "isCorrect": True},
                {"id": "B", "text": wrong_choices[0], "isCorrect": False},
                {"id": "C", "text": wrong_choices[1], "isCorrect": False},
                {"id": "D", "text": wrong_choices[2], "isCorrect": False}
            ]

            rot = (q_seq - 1) % 4
            shuffled_options = options_list[rot:] + options_list[:rot]
            labels = ["A", "B", "C", "D"]
            correct_letter = "A"
            final_options = []
            for idx, opt in enumerate(shuffled_options):
                lbl = labels[idx]
                is_corr = opt["isCorrect"]
                if is_corr:
                    correct_letter = lbl
                final_options.append({
                    "id": lbl,
                    "text": opt["text"],
                    "isCorrect": is_corr
                })

            q_code = f"{topic_code}-OSC-{q_seq:03d}"
            questions.append({
                "code": q_code,
                "questionCode": q_code,
                "text": q_text,
                "options": final_options,
                "correctAnswer": correct_letter,
                "solution": solution,
                "difficulty": diff,
                "topicCode": topic_code,
                "subtopic": subtopic_name,
                "chapterNumber": 3,
                "subjectCode": "SCIE",
                "class": "9",
                "boardCode": "CBSE",
                "type": "OSC",
                "vault": vault,
                "marks": 4
            })
            q_seq += 1

    return questions


# ==========================================
# 3.2.1: Xylem: Tracheids, vessels, xylem parenchyma, fibres (water transport)
# ==========================================
def gen_3_2_1():
    # Arch 1: General Complex Tissue Definition and the Four Elements of Xylem
    arch1 = {
        'templates': [
            "What distinct anatomical and physiological feature defines: '{0}'?:",
            "In plant vascular histology: '{0}' is characterized by:",
            "Consider complex vascular tissues: '{0}' is defined as:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A plant anatomist examines water-conducting tissue: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' contribute to the unidirectional ascent of sap in vascular plants?:",
            "Evaluate the cellular element: '{0}'. Its biological role is:",
            "Why is '{0}' considered a complex permanent tissue?:",
            "What structural property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Complex Permanent Tissue Definition", "Composed of more than one type of cell working together as a coordinated functional unit (e.g., Xylem, Phloem)", "Contrasts with simple tissues (parenchyma, collenchyma, sclerenchyma) which consist of only a single cell type", "Composed of identical cells dividing continuously, Tissue found exclusively in animal organs, Tissue composed of dead cells only"),
            ("The Four Elements of Angiosperm Xylem", "Tracheids, Vessels (tracheae), Xylem Parenchyma, and Xylem Fibres", "Only Xylem Parenchyma is living; Tracheids, Vessels, and Fibres are dead at functional maturity", "Sieve tubes, companion cells, phloem fibers, and xylem parenchyma; Collenchyma, sclereids, parenchyma, and vessels; Tracheids, sieve cells, albuminous cells, and cork"),
            ("Xylem Parenchyma (The ONLY living xylem element)", "Living, thin-walled parenchyma cells that store food reserves (starch, fats) and assist in lateral/radial water conduction via xylem rays", "Essential for maintaining hydraulic continuity, refilling embolized vessels, and synthesizing defensive tyloses", "Dead hollow tubes conducting sap vertically, Thick lignified fibers providing tensile strength, Sieve elements transporting sugars"),
            ("Xylem Fibres (Wood fibres)", "Highly elongated sclerenchymatous cells with pointed ends, extremely thick lignified walls, and narrow or obliterated lumen", "Dead at maturity; provide immense rigid mechanical strength to the xylem cylinder and wood", "Living cells storing starch, Wide open pipes conducting transpirational stream, Cells that divide to form bark"),
            ("Unidirectional Ascent of Sap", "Xylem sap (water + dissolved mineral ions) moves strictly unidirectionally upwards from roots to leaves driven by transpirational pull and root pressure", "Contrasts with bidirectional or multidirectional translocation of organic solutes in the phloem", "Water moves bidirectionally between leaves and roots, Water is pumped downwards into soil, Sap flows only horizontally across bark"),
            ("Protoxylem vs Metaxylem", "Protoxylem is the first-formed primary xylem with narrow lumen and annular/spiral thickenings; Metaxylem matures later with wider lumen and reticulate/pitted thickenings", "Allows early water conduction while organ is still elongating, followed by high-capacity conduction upon full organ expansion", "Protoxylem is living while metaxylem is dead, Protoxylem conducts food while metaxylem conducts water, Both are identical secondary tissues"),
            ("Endarch xylem in Dicot Stems", "Protoxylem lies towards the center (pith/inside) and Metaxylem lies towards the periphery (outside) — centrifugal development", "Characteristic anatomical hallmark of all angiosperm stems", "Protoxylem lies towards outside and metaxylem inside, Protoxylem and metaxylem are randomly scattered, Xylem is arranged in radial plates alternating with phloem"),
            ("Exarch xylem in Roots", "Protoxylem lies towards the periphery (outside) and Metaxylem lies towards the center (inside) — centripetal development", "Characteristic anatomical hallmark of all dicot and monocot roots", "Protoxylem lies towards the center and metaxylem outside, Xylem vessels lack secondary walls, Development occurs centrifugally"),
            ("Primary Xylem vs Secondary Xylem", "Primary xylem differentiates from embryonic procambium; Secondary xylem (wood) is produced by the bifacial lateral vascular cambium during secondary growth", "Secondary xylem constitutes the structural timber of mature trees and shrubs", "Primary xylem forms tree rings while secondary xylem forms leaves, Both are produced by cork cambium, Primary xylem is found only in bark"),
            ("Xylem sap chemical composition", "Dilute aqueous solution (\\(> 99\\%\\text{ water}\\)) containing inorganic mineral ions (\\(\\text{K}^+, \\text{NO}_3^-, \\text{Ca}^{2+}, \\text{SO}_4^{2-}\\)), amino acids, and trace hormones (cytokinins, ABA)", "Transports soil-absorbed nutrients to aerial foliar photosynthetic factories", "Concentrated 20% sucrose solution, Dense lipid emulsion storing energy, Pure distilled water with zero solutes")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Xylem Organization as a Complex Tissue.**\n- Composed of 4 elements: Tracheids (dead), Vessels (dead), Xylem Fibres (dead), and Xylem Parenchyma (the ONLY living element).\n- Conducts water and minerals unidirectionally upwards (roots \\(\\rightarrow\\) leaves); Endarch in stems (protoxylem inside), Exarch in roots (protoxylem outside).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Anatomical / Physiological Significance:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 2: Tracheids vs Vessels (Evolution, Perforations, Bordered Pits)
    arch2 = {
        'templates': [
            "What is the structural and evolutionary distinction between: '{0}'?:",
            "In comparative wood anatomy: '{0}' is characterized by:",
            "Consider tracheary element architecture: '{0}' exhibits:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A plant phylogenist compares gymnosperm and angiosperm wood: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' optimize hydraulic conductance while protecting against cavitation?:",
            "Evaluate the tracheary structural feature: '{0}':",
            "Why is '{0}' considered an evolutionary advancement of angiosperms?:",
            "What histological property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Tracheids", "Elongated, tube-like cells with tapering, chisel-like overlapping ends and heavily lignified pitted walls, lacking perforation plates", "Water moves from tracheid to tracheid through lateral bordered pits across pit membranes; present in pteridophytes, gymnosperms, and angiosperms", "Short wide open barrels with perforated end walls, Living cells containing chloroplasts, Unlignified cells with sieve plates"),
            ("Vessels (Tracheae)", "Long, continuous multi-cellular pipelines formed by the end-to-end fusion of individual vessel elements with completely or partially dissolved end walls (perforation plates)", "Major water-conducting channels characteristic of angiosperms, absent in most gymnosperms (except Gnetales)", "Single unicellular fibers with closed tapering ends, Living cells with active nuclei, Food conducting tubes in phloem"),
            ("Perforation Plates in Vessels", "The open end walls between adjacent vessel elements where primary walls and middle lamellae have been enzymatically dissolved during programmed cell death", "Can be simple (a single large open hole) or scalariform (ladder-like bars); provides unmatched low-resistance hydraulic conductance", "Closed pit membranes with toruses, Walls containing sieve pores and callose, Solid lignified caps preventing water flow"),
            ("Bordered Pits with Torus-Margo in Gymnosperm Tracheids", "Specialized pits where secondary wall arches over the pit cavity; pit membrane has a dense central impermeable torus suspended by a permeable fibrillar margo", "Acts as a safety valve: when cavitation occurs, the torus seals against the pit border, preventing air embolisms from spreading to adjacent tracheids", "Simple open holes without membranes, Pits found only in collenchyma, Pits through which living cytoplasm circulates"),
            ("Non-porous wood (Gymnosperms / Softwoods) vs Porous wood (Angiosperms / Hardwoods)", "Gymnosperm wood (Pinus, Cedrus) consists almost entirely (\\(> 90\\%\\)) of tracheids and lacks vessels (non-porous); Angiosperm wood possesses large open vessels (pores) appearing as distinct holes in cross-section (porous)", "Angiosperm vessels enable far higher hydraulic capacity, supporting massive leaf canopy transpiration", "Softwoods contain vessels while hardwoods have only tracheids, Hardwoods lack all fibers, Both have identical vessel diameters"),
            ("Secondary wall thickening patterns in tracheary elements", "Deposition of lignin follows developmental progression: Annular (rings) \\(\\rightarrow\\) Spiral (helices) \\(\\rightarrow\\) Scalariform (ladder) \\(\\rightarrow\\) Reticulate (net) \\(\\rightarrow\\) Pitted (bordered pits)", "Annular and spiral thickenings allow longitudinal stretching during early stem elongation; pitted walls provide rigid non-deformable support in mature organs", "Begins with pitted and ends with annular, Secondary walls are deposited on the outside of epidermis, Thickenings are made of pectin"),
            ("Evolutionary origin of vessel elements from tracheids", "Vessel elements evolved from tracheid ancestors through shortening, widening, transverse flattening of end walls, and loss of end-wall pit membranes (perforation formation)", "Bailey and Tupper (1918) established this classic evolutionary sequence in plant comparative anatomy", "Tracheids evolved from vessels by closing end walls, Vessels evolved directly from phloem sieve tubes, Vessels originated from epidermal hairs"),
            ("Gnetales: The vessel-bearing gymnosperms", "Advanced gymnosperm group (Gnetum, Ephedra, Welwitschia) possessing true xylem vessels, demonstrating convergent evolution with angiosperms", "Represents a classic evolutionary bridge between gymnosperm and angiosperm wood morphology", "Gnetales lack xylem entirely, Gnetales have collenchyma vessels, Gnetales are extinct pteridophytes"),
            ("Hydraulic conductance vs Cavitation vulnerability trade-off", "Wide vessels offer minimal resistance to water flow (volume flow \\(\\propto r^4\\) by Hagen-Poiseuille law) but are far more vulnerable to freezing- and drought-induced air cavitation than narrow tracheids", "Explains why northern boreal forests are dominated by tracheid-bearing conifers (pines, spruces) that survive severe freeze-thaw cycles", "Wide vessels are completely immune to cavitation, Narrow tracheids carry 1000-fold more water than vessels, Freezing has no effect on xylem sap"),
            ("Tyloses (Balloon-like vessel blockages)", "Protrusions of living xylem parenchyma or ray cells that push through pit cavities into adjacent vessel lumens when vessels become non-functional or injured", "Fills and seals old vessels with resins, gums, and tannins, transforming sapwood into decay-resistant heartwood", "Tyloses are parasitic fungi that destroy trees, Tyloses are air bubbles produced by boiling sap, Structures that pump water"),
            ("Ring-porous vs Diffuse-porous wood", "Ring-porous wood (e.g., Oak, Ash) produces huge wide vessels in spring and very narrow vessels in autumn; Diffuse-porous wood (e.g., Birch, Maple) produces uniform-diameter vessels throughout the growing season", "Ring-porous trees achieve rapid early-spring canopy hydration before full latewood development", "Ring-porous wood lacks vessels entirely, Diffuse-porous wood produces wood only during winter, Both have identical vessel distributions")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Tracheary Element Architecture.**\n- Tracheids: Unicellular, elongated, tapering closed ends, bordered pits (pteridophytes, gymnosperms, angiosperms).\n- Vessels: Multicellular pipelines, open perforation plates, wide lumen, high hydraulic efficiency (predominantly angiosperms).\n- Gymnosperm wood is non-porous (tracheids only); Angiosperm wood is porous (vessels + tracheids).\n\n**Step 2: Contrast '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Evolutionary / Biomechanical Significance:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 3: Mechanism of Water Transport: Transpiration Pull, Cohesion-Tension & Root Pressure
    arch3 = {
        'templates': [
            "What physical force and biophysical principle explains: '{0}'?:",
            "In the physiology of xylem sap ascent: '{0}' is characterized by:",
            "Consider the Cohesion-Tension mechanism: '{0}' functions to:",
            "Which statement precisely describes the physics of: '{0}'?:",
            "A plant biophysicist investigates the ascent of sap: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' pull water to the tops of 100-meter tall redwood trees?:",
            "Evaluate the physiological phenomenon: '{0}':",
            "Why is '{0}' essential for sustaining the transpirational stream?:",
            "What physical property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Cohesion-Tension Theory (Dixon and Joly 1894)", "Transpiration from leaves creates negative hydrostatic pressure (suction/tension); transmitted through continuous, unbroken water columns maintained by hydrogen-bonded cohesion of water molecules", "Universally accepted physical explanation for sap ascent to the summits of the tallest trees (e.g., Sequoia sempervirens, \\(> 115\\text{ m}\\))", "Water is pushed up by powerful mechanical pumps in roots, Water ascends by electrical repulsion of ions, Sap rises by cellular cytoplasmic streaming"),
            ("Cohesion of water molecules", "Mutual electrostatic attraction between polar water molecules mediated by extensive hydrogen bonding (\\(\\delta^+ \\text{H}\\) to \\(\\delta^- \\text{O}\\))", "Confers exceptionally high tensile strength to water (up to \\(-30\\text{ MPa}\\)), preventing water column breakage under massive pulling tensions", "Repulsion between water molecules forcing them apart, Attraction between water and lipid membranes, Tendency of water to evaporate in vacuum"),
            ("Adhesion of water to hydrophilic tracheary walls", "Attraction between polar water molecules and the hydrophilic cellulose/lignin surfaces of xylem vessel and tracheid walls", "Helps support the weight of the vertical water column and prevents meniscus detachment under negative pressure", "Adhesion to air bubbles inside vessels, Attraction between water and hydrophobic waxes, Friction stopping all sap ascent"),
            ("Transpiration Pull (Negative pressure / Tension)", "Evaporation of water from mesophyll cell walls into substomatal cavities lowers the water potential (\\(\\Psi_w\\)) and creates steep concave menisci with high capillary tension", "Pulls water out of leaf vein xylem endings, generating negative pressure that propagates down the entire stem to root tips", "Positive pressure pushing water out of leaf tips, Atmospheric air pressure pushing sap down to roots, Gravitational force pulling water upward"),
            ("Root Pressure and Guttation", "Positive hydrostatic pressure (\\(\\approx 0.1\\text{ to }0.2\\text{ MPa}\\)) generated in root xylem by active mineral ion accumulation into the stele across the endodermis", "Forces water droplets out of specialized hydathodes at leaf margins (guttation) during humid nights when transpiration is minimal; cannot lift water above a few meters", "Massive suction pulling water down into soil, Pressure that lifts water 100 meters high, Caused by photosynthesis in roots"),
            ("Cavitation and Embolism in Xylem", "Breakage of the continuous water column under excessive negative tension, causing dissolved gases to come out of solution and form an air-filled vapor bubble (embolism)", "Blocks sap flow through that vessel; adjacent vessels bypass the blockage via lateral bordered pits", "Instantaneous freezing of sap into ice, Bursting of vessels due to positive pressure, Dissolution of cell wall lignin"),
            ("Embolism repair / Refilling mechanisms", "Positive nocturnal root pressure and active solute secretion by living xylem parenchyma cells into embolized vessels draw water in by osmosis, dissolving the air bubble", "Restores hydraulic continuity before the next day's transpiration demand begins", "Leaves drop off and are replaced every night, Xylem vessels divide mitotically to produce new cells, Air bubbles are consumed by mitochondria"),
            ("Endodermal Casparian Strip role in Root Pressure", "Suberin and lignin band in radial and transverse walls of the endodermis blocking apoplastic water flow, forcing water and minerals through living symplasm", "Prevents back-leakage of concentrated mineral ions from root xylem into the soil, creating the osmotic engine for root pressure", "Conducts water faster than xylem vessels, Absorbs water directly from air, Synthesizes cellulose for root hairs"),
            ("Hagen-Poiseuille Law of Hydraulic Flow (\\(Q \\propto r^4\\))", "Volume flow rate \\(Q\\) through a cylindrical vessel is proportional to the fourth power of its inner radius: \\(Q = (\\pi r^4 \\Delta P) / (8\\eta L)\\)", "A 2-fold increase in vessel radius results in a \\(2^4 = 16\\text{-fold}\\) increase in water transport capacity", "Flow is directly proportional to vessel length, Flow decreases when radius increases, Flow is independent of vessel radius"),
            ("Hydathodes (Epithem tissue)", "Specialized water-exudation pores located at the vein endings of leaf margins (e.g., strawberry, tomato, grasses)", "Pores lack guard cell regulation (permanently open) and exude liquid xylem sap under high root pressure (guttation)", "Stomata that absorb water vapor from clouds, Glands that secrete nectar to attract bees, Hair-like structures catching dust")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Mechanisms of Water Transport.**\n- Transpiration Pull & Cohesion-Tension Theory (Dixon & Joly): Evaporation creates negative tension \\(\\rightarrow\\) pulled by cohesive H-bonds and wall adhesion (unbroken water column up to 115m).\n- Root Pressure: Positive osmotic pressure (0.1-0.2 MPa) causing nocturnal Guttation via hydathodes.\n- Hagen-Poiseuille: Volume flow scales with \\(r^4\\).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Biophysical Principle:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    # Arch 4: Quantitative & Physical Problems in Xylem Hydraulics
    arch4 = {
        'templates': [
            "{0}:",
            "Calculate the xylem hydraulic or biophysical parameter: {0}:",
            "A biophysical plant water relations problem: {0}:",
            "Quantitative xylem sap transport calculation: {0}:",
            "Solve the quantitative xylem physics problem: {0}:",
            "Analyze the numerical Hagen-Poiseuille and tension calculation: {0}:",
            "Determine the correct calculated physical parameter: {0}:",
            "An analytical plant hydraulics problem: {0}:",
            "Find the accurate quantity for: {0}:",
            "Compute the following physiological rate: {0}:"
        ],
        'data': [
            ("A giant California redwood tree is \\(110\\text{ meters}\\) tall. Given that the hydrostatic gravitational pressure gradient is \\(0.01\\text{ MPa/m}\\) and frictional flow resistance through xylem vessels adds \\(0.01\\text{ MPa/m}\\), what is the minimum negative pressure (tension) required at the leaf surface to pull water to the top?", "\\(-2.2\\text{ MPa}\\)", "\\(\\text{Total tension} = 110\\text{ m} \\times (0.01 + 0.01)\\text{ MPa/m} = 110 \\times 0.02 = 2.2\\text{ MPa}\\). As tension (negative pressure), \\(P = -2.2\\text{ MPa}\\)", "-1.1 MPa, -4.4 MPa, -0.22 MPa"),
            ("Vessel A has radius \\(r_A = 20\\text{ }\mu\\text{m}\\) and Vessel B has radius \\(r_B = 60\\text{ }\mu\\text{m}\\). According to the Hagen-Poiseuille law (\\(Q \\propto r^4\\)), how many times greater is the hydraulic volume flow rate through Vessel B compared to Vessel A under the same pressure gradient?", "\\(81\\text{ times greater}\\)", "\\(Q_B / Q_A = (r_B / r_A)^4 = (60 / 20)^4 = 3^4 = 81\\)", "3 times, 9 times, 27 times"),
            ("A mature sunflower plant transpires \\(1.2\\text{ liters}\\) of water during a 10-hour sunny day. If this transpirational flow is conducted through \\(2,000\\) parallel xylem vessels, what is the average volume of water conducted per individual vessel in 1 hour?", "\\(0.06\\text{ mL/hr}\\) (\\(60\\text{ }\mu\\text{L/hr}\\))", "\\(\\text{Total flow/hr} = 1,200\\text{ mL} / 10 = 120\\text{ mL/hr}\\). Per vessel \\(= 120 / 2,000 = 0.06\\text{ mL/hr} = 60\\text{ }\mu\\text{L/hr}\\)", "0.6 mL/hr, 6.0 mL/hr, 0.006 mL/hr"),
            ("Sap velocity through an oak vessel is measured at \\(40\\text{ meters/hour}\\) (\\(1.11\\text{ cm/s}\\)). How long will it take a water molecule to travel from a root tip to a leaf at a height of \\(20\\text{ meters}\\)?", "\\(0.5\\text{ hours}\\) (\\(30\\text{ minutes}\\))", "\\(\\text{Time} = \\text{Distance} / \\text{Velocity} = 20\\text{ m} / 40\\text{ m/hr} = 0.5\\text{ hr} = 30\\text{ min}\\)", "1.0 hour, 2.0 hours, 15 minutes"),
            ("The Young-Laplace equation for capillary meniscus tension is \\(\\Delta P = (2\gamma \\cos\theta) / r\\). If water surface tension \\(\\gamma = 0.072\\text{ N/m}\\), contact angle \\(\\theta = 0^\\circ\\), and cell wall pore radius \\(r = 5.0\\text{ nm}\\) (\\(5.0 \\times 10^{-9}\\text{ m}\\)), calculate the maximum capillary tension generated across this meniscus", "\\(-28.8\\text{ MPa}\\)", "\\(\\Delta P = (2 \\times 0.072 \\times 1) / (5.0 \\times 10^{-9}) = 0.144 / 5.0 \\times 10^{-9} = 2.88 \\times 10^7\\text{ Pa} = 28.8\\text{ MPa}\\). As negative tension: \\(-28.8\\text{ MPa}\\)", "-2.88 MPa, -14.4 MPa, -57.6 MPa"),
            ("A potted tomato plant undergoes guttation at night. If root pressure generates \\(+0.15\\text{ MPa}\\) at the root stele, what is the maximum theoretical height \\(h\\) this positive pressure alone could push a static water column (\\(P = \rho g h\\), \\(\rho = 1000\\text{ kg/m}^3\\), \\(g = 9.8\\text{ m/s}^2\\))?", "\\(\\approx 15.3\\text{ meters}\\)", "\\(h = P / (\\rho g) = 150,000\\text{ Pa} / (1,000 \\times 9.8) \\approx 15.3\\text{ m}\\). (In real plants, resistance reduces this to \\(< 2\\text{--}3\\text{ m}\\))", "\\(\\approx 1.5\\text{ m}\\), \\(\\approx 153\\text{ m}\\), \\(\\approx 5.0\\text{ m}\\)"),
            ("A cylindrical xylem vessel has internal diameter \\(50\\text{ }\mu\\text{m}\\) (radius \\(25\\text{ }\mu\\text{m}\\)) and length \\(10\\text{ cm}\\) (\\(100,000\\text{ }\mu\\text{m}\\)). What is the internal volume of this single vessel in microliters (\\(\\mu\\text{L}\\))?", "\\(0.196\\text{ }\mu\\text{L}\\)", "\\(V = \\pi r^2 L = 3.1416 \\times (25)^2 \\times 100,000 = 196,350,000\\text{ }\mu\\text{m}^3\\). Since \\(1\\text{ }\mu\\text{L} = 10^9\\text{ }\mu\\text{m}^3\\), \\(V = 0.196\\text{ }\mu\\text{L}\\)", "1.96 μL, 0.0196 μL, 19.6 μL"),
            ("If \\(30\\%\\) of the xylem vessels in a birch branch become embolized following a late spring freeze, and total initial conductance was \\(120\\text{ mmol}\\cdot\\text{m}^{-1}\\cdot\\text{s}^{-1}\\cdot\\text{MPa}^{-1}\\), what is the new hydraulic conductance of the branch?", "\\(84\\text{ mmol}\\cdot\\text{m}^{-1}\\cdot\\text{s}^{-1}\\cdot\\text{MPa}^{-1}\\)", "\\(\\text{Remaining conductance} = 120 \\times (1 - 0.30) = 120 \\times 0.70 = 84\\)", "36, 96, 60"),
            ("In an experiment using the pressure bomb (Scholander pressure chamber), an excised leaf requires a balancing pressure of \\(+1.4\\text{ MPa}\\) to bring the xylem sap meniscus back to the cut stem surface. What was the original xylem water potential (\\(\\Psi_w\\)) of the leaf?", "\\(-1.4\\text{ MPa}\\)", "The applied balancing pressure equals the magnitude of the negative xylem tension in the intact leaf: \\(\\Psi_w = -P_{\\text{balance}} = -1.4\\text{ MPa}\\)", "+1.4 MPa, 0.0 MPa, -2.8 MPa"),
            ("A tree stem has 10,000 functioning xylem vessels, each transporting sap at an average velocity of \\(2\\text{ mm/s}\\). If each vessel cross-sectional area is \\(1.25 \\times 10^{-3}\\text{ mm}^2\\), what is the total volume flow rate of sap ascending the trunk in milliliters per minute (\\(\\text{mL/min}\\))?", "\\(1.5\\text{ mL/min}\\)", "Total area \\(= 10,000 \\times (1.25 \\times 10^{-3}) = 12.5\\text{ mm}^2\\). Flow \\(= 12.5\\text{ mm}^2 \\times 2\\text{ mm/s} = 25\\text{ mm}^3/\\text{s} = 0.025\\text{ mL/s}\\). Per min \\(= 0.025 \\times 60 = 1.5\\text{ mL/min}\\)", "15 mL/min, 0.15 mL/min, 150 mL/min")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Identify given physical and biophysical quantities.**\n" + item[0] + "\n\n**Step 2: Apply the governing hydraulic/physical formula.**\n" + item[2] + ".\n\n**Step 3: Conclude.**\nResult is " + item[1] + "."
        ),
        'diff': 'hard'
    }

    # Arch 5: Pathophysiology, Vascular Wilt Diseases, Cavitation and Embolisms
    arch5 = {
        'templates': [
            "Which plant pathology or physiological disorder relates to: '{0}'?:",
            "In plant vascular pathology: '{0}' is characterized by:",
            "What clinical or ecological symptom results from: '{0}'?:",
            "How does vascular wilt pathogen infection cause: '{0}'?:",
            "A forest pathologist investigates tree mortality: '{0}'. What is true?:",
            "Which disease mechanism explains: '{0}'?:",
            "What is the physiological consequence of: '{0}'?:",
            "Why is '{0}' catastrophic for tree water transport?:",
            "What diagnostic feature identifies: '{0}'?:",
            "Evaluate the plant disease concept: '{0}':"
        ],
        'data': [
            ("Vascular Wilt Diseases (Fusarium / Verticillium wilt)", "Soil-borne fungal hyphae invade root xylem vessels and secrete polysaccharides, enzymes, and toxins, triggering host tyloses and gum production", "Completely clogs vessel lumens, blocking the transpirational stream and causing irreversible foliar wilting and death", "Enhances water conduction by 200%, Converts xylem into living phloem, Causes stems to double in thickness"),
            ("Dutch Elm Disease (Ophiostoma ulmi)", "Ascomycete fungus spread by elm bark beetles that grows within xylem vessels, triggering massive immune tyloses and vascular plugging", "Decimated tens of millions of mature American and European elm trees across the 20th century", "Infects only the flowers preventing pollination, Destroys roots by rotting tubers, Makes trees immune to drought"),
            ("Pierce's Disease in Grapevines (Xylella fastidiosa)", "Xylem-limited Gram-negative bacterium transmitted by sharpshooter leafhoppers that forms dense biofilms and extracellular gums inside grape vessels", "Causes severe leaf scorch, fruit shriveling ('raisining'), and systemic vine decline, devastating commercial vineyards", "Destroys phloem preventing sugar transport, Infects chloroplasts turning leaves white, Causes vines to produce blue wine"),
            ("Drought-induced Runaway Cavitation", "Severe soil water deficit forces xylem tension to exceed the cavitation threshold of bordered pit membranes, causing widespread air seeding", "Triggers cascading embolisms across vessel networks, leading to catastrophic hydraulic failure and tree dieback", "Accelerates water absorption from deep aquifers, Causes tree roots to explode, Stimulates rapid leaf expansion"),
            ("Freeze-Thaw Cavitation in Temperate Trees", "During winter freezing, air bubbles come out of solution because gases are insoluble in ice; upon thawing under tension, bubbles expand to embolize wide vessels", "Restricts wide-vessel ring-porous trees from colonizing high alpine and subarctic zones", "Freezing permanently seals all stomata, Freezing converts xylem into wood fibers, Sap turns into sweet syrup"),
            ("Tyloses as a defense mechanism against pathogens", "Living parenchyma cells balloon into infected vessels to wall off and compartmentalize fungal or bacterial pathogens", "Prevents systemic upward spread of the pathogen, though excessive tylosis induces self-inflicted drought wilt", "Produces antibodies identical to human IgG, Dissolves fungal cell walls with stomach acid, Expels the fungus through stomata"),
            ("Heartwood formation as natural durability", "Aging inner sapwood undergoes programmed shutdown of parenchyma: vessels are plugged by tyloses and impregnated with polyphenols, tannins, and quinones", "Converts light sapwood into dense, dark, rot-resistant heartwood (duramen) that resists termite and fungal decay", "Heartwood continues conducting active transpirational sap, Heartwood is living while sapwood is dead, Formed purely by bark division"),
            ("Ultrasonic Acoustic Emissions (UAE) of cavitation", "When a water column under tension snaps during cavitation, the sudden release of energy produces a micro-acoustic pop in the ultrasonic frequency range (\\(100\\text{--}300\\text{ kHz}\\))", "Monitored non-destructively with acoustic sensors to quantify real-time drought stress and embolism rates in living plants", "Emits visible light flashes inside stems, Produces audible hums heard by human ears, Causes stems to vibrate like guitar strings"),
            ("Apoplastic tracer dyes (Eosin / Acid Fuchsin / Safranin)", "Placing cut plant stems in red eosin dye solution reveals that only xylem vessels and tracheids stain red as water ascends to leaf veins", "Definitive classic experimental proof that water conduction is restricted exclusively to the dead lumens of xylem", "Stains living phloem sieve tubes only, Dyes collenchyma cells leaving xylem white, Confirms that water travels through bark"),
            ("Vessel refilling under negative pressure (Novel paradigm)", "Recent biophysical evidence demonstrates that living xylem ray parenchyma cells actively pump solutes and water into embolized vessels to dissolve bubbles even while bulk xylem remains under tension", "Requires metabolic ATP and intact membrane aquaporins in living parenchyma surrounding vessels", "Vessels refill by absorbing raindrops through bark, Air bubbles are squeezed out through stomata, Embolized vessels are discarded and regrown daily")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Xylem Pathology & Cavitation.**\n- Vascular wilts (Fusarium, Verticillium, Xylella, Ophiostoma): Pathogen biofilms and host defensive tyloses plug vessels \\(\\rightarrow\\) hydraulic failure & wilting.\n- Cavitation: Tension exceeds threshold \\(\\rightarrow\\) air seeding creates embolism; freeze-thaw cycles cause gas bubble expansion.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Pathological / Diagnostic Detail:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    # Arch 6: Primary vs Secondary Xylem & Wood Anatomy
    arch6 = {
        'templates': [
            "Which anatomical distinction or structural feature characterizes: '{0}'?:",
            "In comparative wood anatomy: '{0}' is defined by:",
            "Consider secondary xylem architecture: '{0}' exhibits:",
            "Which statement precisely describes: '{0}'?:",
            "A wood anatomist analyzes tree trunk histology: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' organize the structural matrix of secondary wood?:",
            "Evaluate the histological feature: '{0}':",
            "Why is '{0}' vital for timber classification and mechanical durability?:",
            "What structural component corresponds to: '{0}'?:"
        ],
        'data': [
            ("Axial system vs Radial system in secondary xylem", "Axial system (derived from fusiform initials) comprises vertically oriented vessels, tracheids, fibres, and axial parenchyma; Radial system (derived from ray initials) comprises horizontal ray parenchyma", "Enables bidirectional fluid transport: vertical conduction of water up the trunk and radial transport of nutrients and water across trunk rings", "Axial system conducts food while radial system conducts air, Both systems consist purely of dead cork cells, Radial system forms the outer bark"),
            ("Uniseriate vs Multiseriate xylem rays", "Uniseriate rays are a single cell wide in tangential section (characteristic of conifer softwoods e.g., Pinus); Multiseriate rays are multiple cells wide (characteristic of angiosperm hardwoods e.g., Quercus / Oak)", "Key diagnostic feature used in forensic wood anatomy and timber species identification", "Uniseriate rays contain vessels while multiseriate contain fibres, Multiseriate rays are found only in mosses, Neither contains living cells"),
            ("Early wood (Spring wood)", "Formed during spring when cambium is highly active: possesses wide vessels with thin walls and broad lumens", "Optimized to conduct large volumes of water to supply rapidly expanding spring foliage", "Narrow vessels with very thick walls, Highly dark in color, Lacks vessels completely"),
            ("Late wood (Autumn wood)", "Formed during late summer/autumn when cambial activity wanes: possesses narrow vessels with heavily thickened lignified walls and small lumens", "Provides dense mechanical support as seasonal growth terminates", "Wide vessels with thin walls, Pure white color, Consists of living cork cells"),
            ("Reaction Wood (Tension wood vs Compression wood)", "Tension wood develops on the upper side of leaning dicot branches (possesses gelatinous G-fibres); Compression wood develops on the lower side of leaning conifer trunks (possesses heavily lignified tracheids)", "Mechanically realigns displaced branches and stems back towards optimal light orientation", "Reaction wood dissolves the branch, Formed by fungal infection, Contains only living collenchyma"),
            ("Bordered pits in Conifer Tracheids (Bars of Sanio)", "Conifer tracheids display large circular bordered pits on their radial walls; Bars of Sanio (crassulae) are horizontal cellulose thickenings between pit pairs", "Provides reinforcement preventing tracheid wall collapse under extreme winter freeze tensions", "Spirally arranged thorns on bark, Open holes without membranes, Stomata on conifer wood"),
            ("Resin Canals in Gymnosperm Xylem (e.g., Pinus)", "Schizogenous tubular intercellular canals lined with living secretory epithelial cells that synthesize and secrete terpene-rich oleoresin", "Protects trees by physically trapping and chemically poisoning wood-boring bark beetles and inhibiting fungal hyphae", "Conducts transpirational sap, Stores starch reserves, Discharges water vapor into air"),
            ("Hardwood vs Softwood botanical definitions", "Hardwood is secondary xylem derived from angiosperm dicotyledonous trees (possesses vessels and wood fibres); Softwood is secondary xylem derived from gymnosperm conifers (composed of tracheids, lacking vessels)", "Botanical distinction based on presence of vessels, not on physical hardness (e.g., balsa wood is botanically a hardwood despite being extremely soft)", "Softwood is always soft to the touch while hardwood is hard, Softwood comes from ferns, Hardwood lacks cell walls"),
            ("Dendrochronology and Climate Reconstruction", "Measuring width variations in annual growth rings across centuries: wide rings indicate warm, moist, favorable years; narrow rings reflect severe drought or frost", "Used by climatologists to reconstruct past climate variations over thousands of years (paleoclimatology)", "Measures tree height by radar, Counts leaves on branches, Analyzes soil acidity"),
            ("Vascular Cambium cell types: Fusiform vs Ray Initials", "Fusiform initials are elongated, tapering cells that divide periclinally to produce axial secondary xylem and phloem; Ray initials are small isodiametric cells that produce horizontal vascular rays", "Unified bifacial cambial ring maintains constant radial thickness through anticlinal divisions", "Fusiform initials form cork, Ray initials form leaves, Both are dead at maturity")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Secondary Xylem & Wood Histology.**\n- Axial system (fusiform initials): Vertical vessels, tracheids, fibres, axial parenchyma.\n- Radial system (ray initials): Horizontal ray parenchyma for radial transport.\n- Annual rings: Early wood (wide spring vessels) + Late wood (narrow autumn vessels).\n- Hardwoods (angiosperms: vessels present) vs Softwoods (gymnosperms: tracheids only).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Anatomical Detail:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 7: Experimental Protocols, Staining, and Demonstrations in Xylem Physiology
    arch7 = {
        'templates': [
            "Which laboratory experiment, staining technique, or apparatus demonstrates: '{0}'?:",
            "In plant physiological experimentation: '{0}' was verified by:",
            "What experimental protocol is used to study: '{0}'?:",
            "How do plant physiologists experimentally prove: '{0}'?:",
            "A student performs a potometer experiment: '{0}'. What is observed?:",
            "Which microchemical reagent specifically stains: '{0}'?:",
            "In laboratory botany, '{0}' is demonstrated using:",
            "What physical observation confirms: '{0}'?:",
            "Evaluate the laboratory demonstration of: '{0}':",
            "Identify the landmark botanical contribution regarding: '{0}':"
        ],
        'data': [
            ("Ganong's Potometer", "Measures the rate of water absorption by a leafy shoot by tracking the movement of an air bubble in a graduated capillary tube", "Demonstrates that rate of water absorption nearly equals the rate of transpiration under steady-state conditions", "Measures the rate of photosynthesis by collecting oxygen, Weighs root tubers, Measures sugar translocation in phloem"),
            ("Balsam plant stem in Eosin solution (Path of Water Ascent)", "Placing a translucent cut Impatiens (balsam) plant in red eosin dye reveals that after 30 minutes, red coloration is confined exclusively to the xylem vascular bundles and leaf veins", "Definitive visual demonstration that water ascends through xylem, not phloem or cortex", "Red dye accumulates in the bark, Red dye stains only the epidermal hairs, Proves water travels through pith parenchyma"),
            ("Cobalt Chloride (\\(\\text{CoCl}_2\\)) Paper method", "Dry blue anhydrous \\(\\text{CoCl}_2\\) paper turns pink upon absorbing water vapor transpired from leaf surfaces", "Comparing upper vs lower surfaces of dorsiventral leaves proves the lower surface transpires much faster due to higher stomatal density", "Turns black in presence of starch, Turns bright yellow in sunlight, Measures oxygen emission"),
            ("Scholander Pressure Chamber (Pressure bomb)", "An excised leafy twig is sealed in a steel chamber with its cut stem protruding; nitrogen gas pressure is increased until sap just appears at the cut surface", "Directly measures negative xylem tension (water potential \\(\\Psi_w\\)) in intact plant branches", "Pumps water into the plant to force growth, Extracts chloroplasts for DNA sequencing, Measures root pressure"),
            ("Ringing / Girdling experiment and Xylem Continuity", "Removing a complete ring of outer bark (phloem, cortex, periderm) down to the vascular cambium leaves xylem intact; the upper canopy stays healthy and fully turgid for weeks", "Proves that upward water conduction is completely unaffected by phloem removal and proceeds exclusively through xylem", "Causes upper leaves to wilt instantly within 10 seconds, Stops all transpiration immediately, Kills the upper canopy within 5 minutes"),
            ("Strasburger's poisonous ascent experiment (1891)", "Eduard Strasburger placed cut tree trunks in lethal picric acid and copper sulfate solutions; solutions ascended to tree tops and killed all living cells, yet water ascent continued", "Proved conclusively that the ascent of sap is a purely physical process and does not require living cells in the water conduit", "Proved water is pumped by living cells in xylem, Proved that poison stimulates root growth, Showed that trees cannot absorb copper"),
            ("Phloroglucinol-HCl staining of xylem vessels", "Treating stem cross-sections with phloroglucinol and concentrated hydrochloric acid turns all xylem tracheids and vessels intense cherry-red", "Specific histochemical reaction with coniferyl aldehyde units in cell wall lignin", "Stains living sieve tubes bright blue, Turns starch granules blue-black, Bleaches all cell walls"),
            ("Manometer measurement of Root Pressure", "Attaching a glass manometer with mercury or water to the decapitated stump of a well-watered herbaceous plant (e.g., tomato, maize)", "Directly measures positive hydrostatic root pressure pushing a liquid column upward against gravity", "Measures negative tension in leaves, Counts number of stomata, Measures rate of chlorophyll breakdown"),
            ("Bell Jar / Polythene bag demonstration of Transpiration", "Enclosing a potted plant (with pot soil covered in rubber sheeting) inside a dry glass bell jar produces visible condensed water droplets on the inner glass walls", "Simple, elegant proof that aerial plant shoots transpire water vapor into the surrounding air", "Proves that plants emit carbon monoxide, Shows that roots absorb air, Measures soil evaporation"),
            ("Darwin's Porometer", "Measures the rate of air flow drawn through a leaf under constant pressure to determine stomatal opening and resistance", "Used in stomatal physiology to correlate transpiration rate with stomatal aperture", "Measures water conduction through wood, Measures root hair surface area, Weighs seeds")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Classical Experimental Botany.**\n- Path of water: Eosin dye & Girdling prove ascent occurs through xylem.\n- Transpiration: Ganong's potometer (absorption rate), \\(\\text{CoCl}_2\\) paper (transpiration rate), Bell jar (condensation).\n- Physical nature: Strasburger's poison experiment proved living cells are not required for sap ascent; Scholander pressure bomb measures xylem tension.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Laboratory / Historical Significance:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 8: Economic Botany, Timber Technology & Forestry Applications
    arch8 = {
        'templates': [
            "Which commercial timber product, forestry practice, or industrial application relates to: '{0}'?:",
            "In timber technology and forest utilization: '{0}' is characterized by:",
            "What technological significance or wood quality feature defines: '{0}'?:",
            "How does wood anatomy dictate: '{0}'?:",
            "A materials engineer examines commercial wood properties: '{0}'. What is true?:",
            "Which botanical attribute governs: '{0}'?:",
            "What is the commercial or forestry value of: '{0}'?:",
            "Why is '{0}' prized in furniture, construction, and pulp industries?:",
            "What wood preservation process addresses: '{0}'?:",
            "Evaluate the forest science concept: '{0}':"
        ],
        'data': [
            ("Teak wood (Tectona grandis)", "High-density angiosperm hardwood whose secondary xylem is rich in natural preservative oils, silica, and tectoquinones", "World's premier timber for marine decking, shipbuilding, and luxury outdoor furniture due to unmatched termite and rot resistance", "Softwood that rots within one week in rain, Cheap wood used only for paper pulp, Extremely brittle wood that cannot be sawed"),
            ("Balsa wood (Ochroma pyramidale)", "Angiosperm hardwood with exceptionally low density (\\(\\approx 0.16\\text{ g/cm}^3\\)) due to huge, thin-walled, air-filled parenchyma and large vessels", "Lightest commercial timber; used for model aircraft, wind turbine blade cores, and thermal/acoustic insulation", "Heaviest wood on Earth sinking like iron, Dense conifer wood full of resin, Brittle stone-like wood"),
            ("Pulp and Papermaking from Softwoods (e.g., Pinus radiata)", "Conifer softwoods have long tracheids (\\(3\\text{ to }5\\text{ mm}\\)) compared to short hardwood fibers (\\(1\\text{ mm}\\)), providing superior paper tear strength and tensile web cohesion", "Kraft pulping chemically dissolves lignin with sodium hydroxide and sodium sulfide, separating intact cellulose fibers", "Pulp is made by grinding bark, Paper requires 100% lignin, Paper is made from leaves"),
            ("Wood seasoning (Kiln drying vs Air drying)", "Controlled removal of free water from vessel lumens followed by bound water from cell walls down to equilibrium moisture content (\\(\\approx 12\\%\\))", "Prevents subsequent warping, twisting, checking, splitting, and fungal decay in manufactured timber products", "Process of soaking wood in water for 50 years, Burning wood to create charcoal, Adding suberin to wood"),
            ("Creosote and CCA (Chromated Copper Arsenate) treatment", "Pressure-impregnating commercial wood (railway ties, utility poles) with coal-tar creosote or copper-arsenic salts under vacuum", "Poisons wood-decay fungi and termites, extending exterior timber service life from 5 years to over 40 years", "Bleaches wood to pure white, Makes wood transparent like glass, Softens wood for carving"),
            ("Quarter-sawn vs Flat-sawn lumber", "Quarter-sawn wood is cut radially across annual rings: produces dimensionally stable boards that resist cupping and reveal dramatic ray fleck figures (e.g., in oak)", "Flat-sawn wood is cut tangentially: faster and cheaper to produce but prone to warping and shrinking", "Quarter-sawn wood contains no grain, Flat-sawn wood is made of compressed leaves, Both have identical warping rates"),
            ("Lignin as a renewable industrial feedstock (Lignosulfonates)", "Byproduct of chemical paper pulping: used as concrete plasticizers, oil-well drilling mud dispersants, and precursors for bio-vanillin and carbon fibers", "Transforms paper mill waste into high-value green industrial chemicals", "Burned as toxic waste with zero uses, Added to baby milk as protein, Used to manufacture synthetic rubber"),
            ("Plywood and Veneer manufacturing", "Rotating high-grade logs against a sharp lathe knife to peel a continuous thin wooden sheet (veneer); veneers are glued with alternating grain at 90 degrees", "Cross-lamination equalizes tensile strength in all directions and prevents wood from splitting along the grain", "Plywood is made of compressed sawdust, Made of pure cellulose pulp, Consists of pressed tree bark"),
            ("Dendrochronological dating of Stradivarius violins", "Tree-ring analysis of spruce wood in the soundboards of antique Antonio Stradivari violins reveals they were carved from slow-growing alpine trees during the 'Maunder Minimum' (Little Ice Age)", "Uniform narrow growth rings provided optimal acoustic resonance and vibrational damping properties", "Violins were carved from tropical balsa wood, Soundboards are made of pressed coir fibers, Wood was dated via radioactive uranium"),
            ("Charcoal production by Pyrolysis", "Heating dense hardwood billets in the absence of oxygen (pyrolysis) drives off water and volatile organic tars, leaving pure (\\(\\approx 85\\%\\)) porous carbon", "Produces smokeless, high-calorific fuel used for cooking, metallurgy, and industrial activated carbon filters", "Wood is boiled in water, Complete combustion producing white ash, Biological fermentation by yeast")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Wood Technology & Economic Forestry.**\n- Hardwoods (angiosperms e.g., Teak, Oak, Balsa) vs Softwoods (gymnosperms e.g., Pine, Spruce: long tracheids for paper pulp).\n- Wood seasoning: Drying to \\(\\approx 12\\%\\) moisture prevents warping; Cross-lamination (plywood) equalizes tensile strength.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Commercial / Industrial Significance:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-3-3.2.1", "Xylem: Tracheids, vessels, xylem parenchyma, fibres (water transport)", archs)


# ==========================================
# 3.2.2: Phloem: Sieve tubes, companion cells, phloem parenchyma, fibres (food translocation)
# ==========================================
def gen_3_2_2():
    # Arch 1: General Complex Phloem Organization and the Four Elements
    arch1 = {
        'templates': [
            "What distinct histological and physiological feature defines: '{0}'?:",
            "In plant vascular translocation: '{0}' is characterized by:",
            "Consider phloem tissue architecture: '{0}' is defined as:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A plant physiologist traces photoassimilate transport: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' contribute to source-to-sink organic nutrient translocation?:",
            "Evaluate the cellular component: '{0}'. Its biological role is:",
            "Why is '{0}' considered an indispensable element of the phloem complex?:",
            "What structural property corresponds to: '{0}'?:"
        ],
        'data': [
            ("The Four Elements of Angiosperm Phloem", "Sieve tube elements, Companion cells, Phloem parenchyma, and Phloem fibres (bast fibres)", "Sieve tubes, companion cells, and phloem parenchyma are living; only phloem fibres are dead at functional maturity", "Vessels, tracheids, xylem parenchyma, and phloem fibers; Sieve cells, albuminous cells, cork, and collenchyma; Sclereids, vessels, companion cells, and tracheids"),
            ("Living state of Phloem vs Dead state of Xylem", "Phloem is predominantly a living conducting tissue (3 of 4 elements are living), whereas xylem is predominantly a dead tissue (3 of 4 elements are dead)", "Reflects the metabolic ATP energy requirement for active phloem loading and maintaining cellular osmotic gradients", "Phloem is entirely dead while xylem is entirely living, Both tissues are 100% dead at maturity, Both tissues lack cell walls"),
            ("Bidirectional / Multidirectional Translocation in Phloem", "Phloem sap translocates multidirectionally from sources (photosynthesizing leaves or storage tubers) to sinks (roots, fruits, growing buds, shoot tips)", "Direction shifts seasonally depending on developmental metabolic demand (e.g., upward in spring from storage roots to buds; downward in summer to roots)", "Translocates strictly unidirectionally from roots to leaves, Translocates only downward into soil, Flow is random and unregulated"),
            ("Phloem Fibres (Bast fibres - The ONLY dead phloem element)", "Highly elongated, thick-walled, lignified sclerenchyma fibres that provide mechanical support to the vascular bundle", "Dead at maturity; commercial source of jute, flax, and hemp fibers", "Living cells actively pumping sucrose, Enucleated cells conducting sugar sap, Cells containing chloroplasts for photosynthesis"),
            ("Phloem Parenchyma", "Living, elongated parenchyma cells with thin cellulose walls that store organic nutrients (starch, fats, resins, latex) and assist lateral transport", "Absent in most monocotyledonous stems (e.g., grasses, maize), present in dicotyledons and gymnosperms", "Dead hollow tubes conducting sap, Highly lignified cells without cytoplasm, Cells that produce pollen grains"),
            ("Protophloem vs Metaphloem", "Protophloem is the first-formed primary phloem with narrow, indistinct sieve tubes that rapidly get crushed during organ elongation; Metaphloem matures later with wider, prominent sieve elements", "Ensures early nutrient conduction before the final adult vascular cylinder is established", "Protophloem has lignified walls while metaphloem is living, Protophloem conducts water while metaphloem conducts sugar, Both are secondary tissues"),
            ("Primary Phloem vs Secondary Phloem", "Primary phloem differentiates from embryonic procambium; Secondary phloem (inner bark) is produced towards the outside by the lateral vascular cambium during secondary growth", "Secondary phloem accumulates over years, providing seasonal sugar conduction before outer layers become bark", "Primary phloem is found only in roots while secondary is in leaves, Primary phloem forms wood while secondary forms roots, Both arise from cork cambium"),
            ("Phloem sap chemical composition", "Concentrated alkaline solution (pH 7.5 to 8.5) containing \\(10\\text{ to }25\\%\\) sucrose, along with amino acids, organic acids, potassium (\\(\\text{K}^+\\)), mRNA, and signaling hormones", "Non-reducing disaccharide sucrose is the transport sugar because it is chemically unreactive and osmoprotective", "Pure water with zero dissolved solids, 90% glucose and starch, Highly acidic solution of pH 2.0"),
            ("P-Protein (Phloem-specific Protein / Slime)", "Specialized filamentous structural protein unique to sieve tube elements of dicotyledonous angiosperms", "Aggregates instantly over sieve plate pores upon physical injury or insect feeding, plugging the sieve pores to prevent catastrophic loss of phloem sap", "Enzyme that synthesizes starch in leaves, Structural protein of the spindle apparatus, Receptor for light in chloroplasts"),
            ("Callose and Wound Callose (\\(\\beta\\)-1,3-glucan)", "A glucose polymer synthesized by callose synthase in plasma membrane: forms callose collars around sieve pores and rapidly seals sieve plates upon injury or winter dormancy", "Enzymatically dissolved by beta-1,3-glucanase in spring to reopen sieve pores for seasonal sap resumption", "Protein that digests cell walls, Lipid that makes bark waterproof, Mineral crystal storing calcium")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Phloem Organization as a Complex Tissue.**\n- Composed of 4 elements: Sieve tube elements (living, enucleated), Companion cells (living, nucleated), Phloem parenchyma (living, absent in monocots), Phloem fibres (the ONLY dead phloem element).\n- Conducts organic nutrients (sucrose) bidirectionally from Source \\(\\rightarrow\\) Sink.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Physiological / Anatomical Significance:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 2: Sieve Tube Elements vs Sieve Cells & Companion Cells vs Albuminous Cells
    arch2 = {
        'templates': [
            "What distinct anatomical and evolutionary feature distinguishes: '{0}'?:",
            "In comparative phloem cytology: '{0}' is characterized by:",
            "Consider sieve element architecture: '{0}' exhibits:",
            "Which statement precisely describes the structural relationship between: '{0}'?:",
            "A plant anatomist examines angiosperm vs gymnosperm phloem: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' maintain living metabolic viability despite lacking a nucleus?:",
            "Evaluate the cellular specialization: '{0}':",
            "Why is '{0}' considered a unique cytological entity in plant biology?:",
            "What ultrastructural property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Enucleated living state of mature Sieve Tube Elements", "At maturity, the nucleus, vacuolar membrane (tonoplast), ribosomes, and Golgi apparatus degenerate, leaving a peripheral thin layer of living cytoplasm and mitochondria", "Eliminates internal cellular obstructions, creating a low-resistance lumen for high-volume hydrostatic sap flow while remaining living", "Dead empty tube lacking all membranes like xylem vessels, Possesses a giant hyperactive nucleus, Filled with solid crystalline starch"),
            ("Companion Cells (Sister cells of Sieve Tube Elements)", "Specialized parenchymatous cells derived from the exact same mother initial cell as the adjacent sieve tube element by an asymmetric longitudinal division", "Contains dense cytoplasm, numerous mitochondria, and a prominent nucleus that metabolically directs and sustains the enucleated sieve tube", "Dead sclerenchyma fibers providing tensile support, Cells derived from xylem cambium, Non-living vesicles storing sap"),
            ("Plasmodesmatal / Pore-Plasmodesma units", "Sieve tube elements and companion cells are interconnected by dense, branched pore-plasmodesma units spanning their common longitudinal walls", "Allows rapid symplastic movement of ATP, proteins, mRNAs, and sucrose from companion cell into the sieve tube lumen", "Completely impermeable wall with zero connections, Connected only by large open hole perforations, Separated by a thick suberin layer"),
            ("Sieve Plates and Sieve Pores", "Transverse or oblique end walls between adjacent sieve tube elements perforated by numerous enlarged sieve pores lined with callose", "Allows continuous, low-resistance longitudinal bulk flow of concentrated phloem sap between consecutive sieve elements", "Solid impermeable lignified end walls, Open perforations lacking any membrane or lining, Thick plates made of calcium carbonate"),
            ("Sieve Cells vs Sieve Tube Elements (Evolution)", "Sieve cells are primitive, elongated, unspecialized cells with narrow sieve areas on lateral walls and closed tapering ends (found in pteridophytes and gymnosperms); Sieve tube elements are specialized, wide, end-to-end barrels forming continuous tubes with distinct sieve plates (angiosperms)", "Represents the evolutionary advancement of phloem parallel to tracheid-to-vessel evolution in xylem", "Sieve cells are found only in flowering plants, Sclereids evolved from sieve cells, Both possess identical simple sieve plates"),
            ("Albuminous Cells (Strasburger cells) in Gymnosperms", "Specialized ray or axial phloem parenchyma cells in gymnosperms that perform the metabolic companion role for sieve cells", "Unlike angiosperm companion cells, albuminous cells do NOT arise from the same mother cell as the sieve cell", "Dead sclerenchyma fibers protecting conifer bark, Cells that store albumen protein in seeds, Cells producing resin"),
            ("Simple vs Compound Sieve Plates", "Simple sieve plates consist of a single sieve area occupying the entire end wall (e.g., Cucurbita); Compound sieve plates consist of multiple distinct sieve areas arranged in scalariform or reticulate patterns (e.g., Betula / Birch)", "Compound sieve plates represent a more primitive ancestral state than simple transverse sieve plates", "Simple plates have zero pores, Compound plates are made of wood, Simple plates are found only in gymnosperms"),
            ("Companion cell subtypes: Ordinary, Transfer, and Intermediary cells", "Ordinary companion cells have smooth walls; Transfer cells develop extensive invaginated wall ingrowths to maximize apoplastic sucrose uptake; Intermediary cells possess thousands of branched plasmodesmata for symplastic polymer trapping", "Reflects the specific mechanistic mode of phloem loading (apoplastic vs symplastic) operating in that plant species", "Ordinary cells are dead, Transfer cells produce pollen, Intermediary cells produce secondary wood"),
            ("Absence of companion cells in non-angiosperms", "Pteridophytes (ferns) and Gymnosperms strictly lack companion cells; they possess albuminous cells instead", "True companion cells are an exclusive evolutionary diagnostic synapomorphy of angiosperms", "Angiosperms lack companion cells, Companion cells are present in all living plants including algae, Gymnosperms possess 10 companion cells per tube"),
            ("Life span of sieve tube elements", "In most herbaceous plants and deciduous trees, sieve tubes function for only a single growing season before being crushed by secondary growth; in monocots (palms), individual sieve tubes function for over \\(100\\text{ years}\\)", "Shows that enucleated sieve tube elements can survive for a century if supported by living companion cells", "Die within 2 minutes of formation, Function indefinitely across 500 years in all plants, Replaced every 24 hours")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Sieve Element & Companion Cell Cytology.**\n- Sieve tube element: Living, enucleated at maturity (no nucleus, tonoplast, or ribosomes) to minimize resistance to flow.\n- Companion cell: Living, nucleated, sister cell (same parent initial), rich in mitochondria, directs sieve tube metabolism via branched pore-plasmodesmata.\n- Gymnosperms: Sieve cells + Albuminous (Strasburger) cells (lack sieve plates and companion cells).\n\n**Step 2: Contrast '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Evolutionary / Cytological Detail:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 3: Pressure-Flow Hypothesis (Münch 1930) & Phloem Loading/Unloading
    arch3 = {
        'templates': [
            "What physiological mechanism and biophysical principle explains: '{0}'?:",
            "In the Münch Pressure-Flow hypothesis: '{0}' is characterized by:",
            "Consider phloem source-sink mechanics: '{0}' functions to:",
            "Which statement precisely describes the physics of: '{0}'?:",
            "A plant physiologist traces assimilate partition: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' drive bulk mass flow of sucrose through sieve tubes?:",
            "Evaluate the physiological process: '{0}':",
            "Why is '{0}' indispensable for long-distance organic solute transport?:",
            "What thermodynamic principle corresponds to: '{0}'?:"
        ],
        'data': [
            ("Münch Pressure-Flow Hypothesis (1930)", "Active loading of sucrose at source lowers water potential, causing osmotic water inflow from xylem and generating high turgor pressure; at sink, sucrose is unloaded, water leaves by osmosis, lowering turgor pressure; the resulting hydrostatic pressure gradient drives bulk mass flow", "Universally accepted mechanistic framework explaining long-distance phloem translocation", "Sucrose flows by simple diffusion down its concentration gradient, Phloem sap is pulled by transpiration suction, Sap is driven by peristaltic waves of muscle fibers"),
            ("Source vs Sink definition", "Source: organ producing excess photoassimilates beyond its own needs (mature leaves, germinating cotyledons, storage tubers in spring); Sink: organ consuming or storing assimilates (roots, young expanding leaves, fruits, seeds, tubers in autumn)", "Source and sink identities are dynamic and can reverse depending on the developmental stage and season", "Roots are always sources and leaves are always sinks, Sinks produce sucrose while sources consume it, Only flowers can act as sources"),
            ("Apoplastic Phloem Loading (\\(\\text{Sucrose/H}^+\\) Symport)", "\\(\\text{H}^+\\)-ATPase pumps protons out into cell wall (apoplast); the proton-motive force drives active uptake of sucrose into companion cells against a concentration gradient via SUT/SUC symporters", "Requires metabolic ATP; sensitive to uncouplers (DNP) and metabolic inhibitors (cyanide)", "Sucrose diffuses passively without any proteins, Driven by sodium-potassium pumps, Occurs through open water channels only"),
            ("Symplastic Phloem Loading (Polymer Trapping Model)", "Sucrose diffuses through plasmodesmata into intermediary companion cells, where galactosyltransferases synthesize larger raffinose and stachyose oligosaccharides", "Larger oligosaccharides cannot diffuse backward through narrow plasmodesmata into mesophyll, forcing directional flow forward into the sieve tube", "Proteins are digested into amino acids, Sucrose is converted into insoluble starch grains, Operates only in dead tissues"),
            ("Turgor pressure gradient (\\(\\Delta P\\)) along sieve tubes", "Turgor pressure is high at the source (\\(\\approx 0.6\\text{ to }1.5\\text{ MPa}\\)) and significantly lower at the sink (\\(\\approx 0.1\\text{ to }0.3\\text{ MPa}\\))", "The physical hydrostatic pressure gradient (\\(\\Delta P = P_{\\text{source}} - P_{\\text{sink}}\\)) drives bulk mass flow through sieve pores without requiring metabolic ATP along the transport conduit", "Turgor pressure is identical throughout the entire plant, Turgor pressure is negative like xylem tension, Pressure is high at the sink and low at the source"),
            ("Phloem Unloading at Sinks (Symplastic vs Apoplastic)", "In growing vegetative sinks (root tips), unloading is predominantly symplastic via plasmodesmata; In storage organs (seeds, fruits), unloading involves an apoplastic step mediated by invertases and SWEET transporters", "Apoplastic step allows strict developmental and hormonal regulation of reserve accumulation", "Unloading requires boiling of sap, Unloading occurs only by cell death, Unloading is identical in all organs"),
            ("Aphid Stylet Technique (Mothes & Romeike / Kennedy & Mittler)", "Aphids insert needle-like mouthparts (stylets) precisely into a single living sieve tube element without provoking wound callose or P-protein plugging", "Cutting the aphid body from its stylet yields pure, flowing phloem sap for hours under positive turgor pressure, verifying the pressure-flow model", "Proves phloem sap is under extreme negative tension, Proves phloem conducts pure water, Used to inject viral DNA into roots"),
            ("Radioactive Tracer Studies (\\(^{14}\\text{CO}_2\\) and Autoradiography)", "Exposing a single leaf to \\(^{14}\\text{CO}_2\\) produces radioactive \\(^{14}\\text{C}\\)-sucrose, which can be tracked moving simultaneously upward to shoot tips and downward to roots via phloem", "Conclusively demonstrated the bidirectional, multi-sink routing of organic photoassimilates", "Proved that carbon moves through xylem vessels, Showed that carbon is expelled through root hairs, Showed that leaves absorb sugar from rain"),
            ("Phloem sap velocity and mass transfer rate", "Phloem sap travels at linear velocities of \\(30\\text{ to }100\\text{ cm/hour}\\), moving up to \\(1\\text{ to }5\\text{ grams of sucrose}\\) per hour per \\(\\text{cm}^2\\) of phloem cross-section", "Orders of magnitude faster than possible by passive diffusion (which would take 32 years to diffuse 1 meter)", "Travels at the speed of light, Moves at 1 micrometer per week, Flow rate is zero in live plants"),
            ("Water recycling between Xylem and Phloem", "Water that enters the phloem at sources by osmosis and travels to sinks is unloaded and recycled back into adjacent xylem vessels to re-enter the transpirational stream", "Creates a closed, continuous circulatory hydraulic loop linking xylem and phloem transport systems", "Water leaves phloem by leaking out of bark into air, Water is consumed permanently in sieve tubes, Phloem water converts into oil")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Phloem Translocation Mechanics.**\n- Münch Pressure-Flow Hypothesis: Sucrose loading at source (low \\(\\Psi_w\\)) draws water from xylem \\(\\rightarrow\\) high turgor pressure \\(\\rightarrow\\) bulk flow \\(\\rightarrow\\) unloading at sink (water exits) \\(\\rightarrow\\) low turgor pressure.\n- Driven by hydrostatic gradient (\\(\\Delta P\\)); verified by Aphid stylet technique and \\(^{14}\\text{C}\\) tracer autoradiography.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Biophysical Detail:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    # Arch 4: Quantitative & Biophysical Calculations in Phloem Transport
    arch4 = {
        'templates': [
            "{0}:",
            "Calculate the phloem translocation parameter: {0}:",
            "A biophysical phloem transport problem: {0}:",
            "Quantitative source-sink physiology calculation: {0}:",
            "Solve the quantitative phloem calculation: {0}:",
            "Analyze the numerical sucrose mass-transfer question: {0}:",
            "Determine the correct calculated physiological quantity: {0}:",
            "An analytical plant translocation problem: {0}:",
            "Find the accurate quantity for: {0}:",
            "Compute the following transport metric: {0}:"
        ],
        'data': [
            ("A potato plant translocates \\(15\\text{ grams of sucrose}\\) per day into its developing underground tubers. If the total functional cross-sectional area of phloem in the stolon is \\(0.02\\text{ cm}^2\\), what is the specific mass transfer rate (SMTR) in grams per hour per square centimeter (\\(\\text{g}\\cdot\\text{hr}^{-1}\\cdot\\text{cm}^{-2}\\))?", "\\(31.25\\text{ g}\\cdot\\text{hr}^{-1}\\cdot\\text{cm}^{-2}\\)", "\\(\\text{Sucrose/hr} = 15\\text{ g} / 24\\text{ hr} = 0.625\\text{ g/hr}\\). \\(\\text{SMTR} = 0.625\\text{ g/hr} / 0.02\\text{ cm}^2 = 31.25\\text{ g}\\cdot\\text{hr}^{-1}\\cdot\\text{cm}^{-2}\\)", "3.125, 62.5, 15.6"),
            ("A severed aphid stylet exudes phloem sap at a steady rate of \\(3.0\\text{ }\mu\\text{L/hour}\\). If the sucrose concentration of the sap is \\(0.6\\text{ M}\\) (MW \\(= 342.3\\text{ g/mol}\\)), how many milligrams of sucrose are exuded in 8 hours?", "\\(4.93\\text{ mg}\\) of sucrose", "Volume in 8 hr \\(= 3.0 \\times 8 = 24\\text{ }\mu\\text{L} = 24 \\times 10^{-6}\\text{ L}\\). Moles \\(= 0.6 \\times (24 \\times 10^{-6}) = 1.44 \\times 10^{-5}\\text{ mol}\\). Mass \\(= 1.44 \\times 10^{-5} \\times 342.3 = 4.93 \\times 10^{-3}\\text{ g} = 4.93\\text{ mg}\\)", "49.3 mg, 0.49 mg, 9.86 mg"),
            ("At a leaf source, sieve tube sap has solute potential \\(\\Psi_s = -1.8\\text{ MPa}\\) and total water potential \\(\\Psi_w = -0.6\\text{ MPa}\\). What is the hydrostatic turgor pressure \\(P_{\\text{source}}\\) in the sieve tube (\\(\\Psi_w = \\Psi_s + P\\))?", "\\(+1.2\\text{ MPa}\\)", "\\(P = \\Psi_w - \\Psi_s = -0.6 - (-1.8) = -0.6 + 1.8 = +1.2\\text{ MPa}\\)", "-1.2 MPa, +2.4 MPa, +0.6 MPa"),
            ("At a root sink, sieve tube sap has solute potential \\(\\Psi_s = -0.7\\text{ MPa}\\) and total water potential \\(\\Psi_w = -0.4\\text{ MPa}\\). What is the hydrostatic turgor pressure \\(P_{\\text{sink}}\\) at this sink?", "\\(+0.3\\text{ MPa}\\)", "\\(P = \\Psi_w - \\Psi_s = -0.4 - (-0.7) = -0.4 + 0.7 = +0.3\\text{ MPa}\\)", "-0.3 MPa, +1.1 MPa, 0.0 MPa"),
            ("Given \\(P_{\\text{source}} = 1.2\\text{ MPa}\\) and \\(P_{\\text{sink}} = 0.3\\text{ MPa}\\) in a \\(1.5\\text{-meter}\\) tall plant, what is the hydrostatic pressure gradient (\\(\\Delta P / L\\)) driving bulk phloem flow along the stem?", "\\(0.60\\text{ MPa/m}\\)", "\\(\\Delta P = 1.2 - 0.3 = 0.9\\text{ MPa}\\). Gradient \\(= 0.9\\text{ MPa} / 1.5\\text{ m} = 0.60\\text{ MPa/m}\\)", "0.90 MPa/m, 0.30 MPa/m, 1.20 MPa/m"),
            ("Phloem sap travels through a sieve tube at a linear velocity of \\(60\\text{ cm/hour}\\). How long will it take a radioactive \\(^{14}\\text{C}\\)-sucrose molecule to travel from a mature leaf to a root tip located \\(90\\text{ cm}\\) below?", "\\(1.5\\text{ hours}\\) (\\(90\\text{ minutes}\\))", "\\(\\text{Time} = \\text{Distance} / \\text{Velocity} = 90\\text{ cm} / 60\\text{ cm/hr} = 1.5\\text{ hours} = 90\\text{ min}\\)", "3.0 hours, 0.75 hours, 45 minutes"),
            ("A circular sieve plate has radius \\(R = 15\\text{ }\mu\\text{m}\\) (area \\(= 706.86\\text{ }\mu\\text{m}^2\\)). If it contains 100 identical circular sieve pores, each of radius \\(r = 0.6\\text{ }\mu\\text{m}\\), what percentage of the total sieve plate area is open for sap flow?", "\\(16.0\\%\\)", "Total pore area \\(= 100 \\times \\pi (0.6)^2 = 100 \\times 1.131 \\approx 113.1\\text{ }\mu\\text{m}^2\\). Percentage \\(= (113.1 / 706.86) \\times 100 \\approx 16.0\\%\\)", "32.0%, 8.0%, 25.0%"),
            ("If passive diffusion of sucrose across \\(1\\text{ meter}\\) in water takes approximately 32 years, and bulk phloem flow covers \\(1\\text{ meter}\\) in \\(1.25\\text{ hours}\\), how many times faster is phloem mass flow than molecular diffusion?", "\\(\\approx 224,256\\text{ times faster}\\)", "\\(32\\text{ years} = 32 \\times 365.25 \\times 24 = 280,320\\text{ hours}\\). Ratio \\(= 280,320 / 1.25 \\approx 224,256\\)", "\\(\\approx 2,242\\), \\(\\approx 22,425\\), \\(\\approx 1,000,000\\)"),
            ("A mature pumpkin (Cucurbita) fruit gains \\(5.4\\text{ kg}\\) fresh weight over 30 days. If the dry matter is \\(10\\%\\) and consists of \\(90\\%\\) translocated sucrose, what was the average mass of sucrose imported per day?", "\\(16.2\\text{ grams/day}\\)", "Total dry matter \\(= 0.10 \\times 5,400\\text{ g} = 540\\text{ g}\\). Sucrose \\(= 0.90 \\times 540 = 486\\text{ g}\\). Per day \\(= 486 / 30 = 16.2\\text{ g/day}\\)", "32.4 g/day, 8.1 g/day, 54.0 g/day"),
            ("In an aphid feeding assay, severed stylets discharge sap with osmolarity \\(800\\text{ mOsm/L}\\). At \\(20^\\circ\\text{C}\\) (\\(293\\text{ K}\\)), what is the osmotic potential (\\(\\Psi_s\\)) of this sap (\\(\\Psi_s = -MiRT\\), \\(R = 0.008314\\text{ L}\\cdot\\text{MPa}\\cdot\\text{mol}^{-1}\\cdot\\text{K}^{-1}\\))?", "\\(-1.95\\text{ MPa}\\)", "\\(\\Psi_s = -0.800\\text{ mol/L} \\times 0.008314 \\times 293 \\approx -1.948\\text{ MPa} \\approx -1.95\\text{ MPa}\\)", "-0.98 MPa, -3.90 MPa, -1.25 MPa")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Identify given physical and biochemical variables.**\n" + item[0] + "\n\n**Step 2: Apply the governing phloem biophysical formula.**\n" + item[2] + ".\n\n**Step 3: Conclude.**\nResult is " + item[1] + "."
        ),
        'diff': 'hard'
    }

    # Arch 5: Comparative Matrix: Xylem vs Phloem
    arch5 = {
        'templates': [
            "Which row in the comparative matrix correctly contrasts: '{0}'?:",
            "In comparing the two complex vascular tissues: '{0}' is characterized by:",
            "Consider xylem vs phloem functional biology: '{0}' demonstrates that:",
            "Which statement presents a 100% accurate contrast: '{0}'?:",
            "A botanical summary matrix features: '{0}'. The accurate entry is:",
            "Compare Xylem and Phloem: '{0}' is accurately stated as:",
            "Which comparative vascular fact holds true for: '{0}'?:",
            "Select the correct pairing for: '{0}':",
            "In an analytical examination question: '{0}' is correctly described by:",
            "Evaluate the vascular tissue comparison: '{0}':"
        ],
        'data': [
            ("Primary physiological function", "Xylem: Conduction of water and dissolved mineral ions; Phloem: Translocation of organic nutrients (sucrose, amino acids)", "Xylem hydrates and supplies inorganic minerals; Phloem nourishes growing and storage tissues with carbohydrates", "Xylem transports sugars while phloem transports water, Both tissues conduct identical mineral solutions, Xylem stores food while phloem absorbs water"),
            ("Direction of sap flow", "Xylem: Strictly unidirectional (upwards from roots to leaves); Phloem: Multidirectional / Bidirectional (from sources to sinks)", "Xylem flow is driven by leaf transpiration; Phloem flow routes dynamically to where metabolic demand is highest", "Xylem is multidirectional while phloem is unidirectional, Both flow only downwards into soil, Both flow exclusively sideways"),
            ("Living vs Dead cellular state", "Xylem: Dead conducting elements (vessels, tracheids, fibres are dead; only parenchyma is living); Phloem: Living conducting elements (sieve tubes, companion cells, parenchyma are living; only fibres are dead)", "Reflects physical pull (xylem) versus active osmotic hydrostatic pumping (phloem)", "Both tissues are 100% dead at maturity, Xylem is 100% living while phloem is dead, Sieve tubes are dead like vessels"),
            ("Driving physical mechanism", "Xylem: Transpirational pull & negative hydrostatic tension (Cohesion-Tension); Phloem: Positive hydrostatic turgor pressure gradient (Münch Pressure-Flow)", "Xylem sap is pulled under tension; Phloem sap is pushed under positive turgor pressure", "Both are driven by negative suction, Both are driven by root pressure only, Phloem is driven by gravity alone"),
            ("Wall chemical composition", "Xylem: Thick, heavily lignified secondary walls in vessels, tracheids, and fibers; Phloem: Thin primary cellulose walls in sieve tubes and companion cells (only fibers have lignin)", "Lignin in xylem prevents conduit collapse under immense negative pressure", "Phloem has heavily lignified walls while xylem lacks lignin, Both have thin unlignified walls, Phloem walls are made of suberin"),
            ("Position in Dicot Stem Vascular Bundles", "Xylem lies towards the inside (endarch / facing pith); Phloem lies towards the outside (facing cortex), separated by vascular cambium", "Arrangement maintains wood production inside and bark production outside", "Phloem lies towards the center and xylem towards the outside, Both tissues are randomly mixed together, Phloem is restricted to the pith"),
            ("Conduit structural units", "Xylem: Vessels (open perforation plates) and Tracheids (bordered pits); Phloem: Sieve tube elements (sieve plates with callose pores) and Companion cells", "Reflects open pipe hydraulics vs living enucleated symplastic channels", "Both conduits have open perforation plates, Sieve tubes have bordered pits, Xylem vessels contain companion cells"),
            ("Commercial fiber source", "Xylem provides Wood timber, paper pulp, and firewood; Phloem provides Bast textile fibers (Jute, Flax, Hemp)", "Timber derives from secondary xylem; commercial ropes and burlap derive from secondary phloem bast fibers", "Commercial ropes are made of xylem vessels, Paper is made of phloem companion cells, Timber is pure phloem"),
            ("Pathological reaction to injury", "Xylem: Cavitation/embolism formation and vessel sealing by tyloses; Phloem: Rapid sealing of sieve pores by P-protein plugs and wound callose synthesis", "Prevents catastrophic leakage of pressurized phloem sap and seals vascular conduits against systemic pathogens", "Xylem leaks all sap until the plant dies, Phloem cannot seal its pores, Both tissues explode upon injury"),
            ("Effect of Girdling / Ringing experiment", "Removing phloem bark leaves xylem intact: upper canopy remains fully turgid and photosynthetic, but roots starve and die after several weeks due to lack of downward sugar transport", "Proves conclusively that water ascends through xylem while food descends through phloem", "Tree dies instantly within 10 seconds, Roots grow 10 times larger, Leaves wilt within 5 minutes due to drought")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Definitive Comparative Vascular Biology.**\n- Xylem: Water/minerals, Unidirectional (upwards), Dead conducting cells (vessels/tracheids), Negative tension (Cohesion-Tension), Thick lignified walls, Positioned inside.\n- Phloem: Organic solutes (sucrose), Multidirectional (Source \\(\\rightarrow\\) Sink), Living conducting cells (sieve tubes/companion cells), Positive turgor (Pressure-Flow), Thin cellulose walls, Positioned outside.\n\n**Step 2: Contrast '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Diagnostic / Evolutionary Criterion:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 6: Phloem Pathology, Insect Vectors, Viruses and Parasitic Plants
    arch6 = {
        'templates': [
            "Which plant disease, pest interaction, or agricultural phenomenon relates to: '{0}'?:",
            "In phloem pathology and agricultural entomology: '{0}' is characterized by:",
            "What physiological impact or agricultural damage results from: '{0}'?:",
            "How do phloem-feeding insects exploit: '{0}'?:",
            "An agricultural extension officer investigates crop failure: '{0}'. What is true?:",
            "Which vector-pathogen relationship explains: '{0}'?:",
            "What is the pathological consequence of: '{0}'?:",
            "Why is '{0}' devastating to crop yields?:",
            "What diagnostic symptom identifies: '{0}'?:",
            "Evaluate the plant-insect pathology concept: '{0}':"
        ],
        'data': [
            ("Aphids and Phloem sap feeding (Honeydew excretion)", "Aphids (Aphidoidea) tap stylets directly into pressurized sieve tubes; positive pressure forces sugary sap through the insect gut without active sucking", "Aphids excrete excess unabsorbed sucrose solution ('honeydew'), which coats leaves and fosters black sooty mold fungi, reducing host photosynthesis", "Aphids inject lethal stomach acid that dissolves roots, Aphids feed on dead xylem fibers, Aphids absorb all water causing instant wilting"),
            ("Citrus Greening Disease (Huanglongbing / HLB)", "Candidatus Liberibacter asiaticus, a fastidious phloem-limited bacterium transmitted by the Asian citrus psyllid (Diaphorina citri)", "Induces massive phloem necrosis and callose blockage, leading to blotchy mottle leaf chlorosis, bitter misshapen green fruit, and tree death", "Fungus that rots citrus flowers, Virus that infects xylem vessels causing wilt, Nutrient deficiency of iron"),
            ("Systemic Viral Transport via Phloem", "Plant viruses (e.g., Tobacco Mosaic Virus - TMV, Potato Virus Y) move short distances through plasmodesmata and enter sieve tubes for rapid long-distance systemic spread to all sinks", "Exploits the plant's own high-velocity phloem assimilate translocation network to infect whole crops within days", "Viruses travel through dead xylem vessels only, Viruses fly through air spaces in aerenchyma, Viruses move by swimming with flagella"),
            ("Dodder (Cuscuta) parasitic angiosperm", "Obligate stem holoparasite lacking roots and chlorophyll that coils around host stems and sends specialized invasive haustoria into host vascular bundles", "Haustoria form direct symplastic and vascular connections to host phloem and xylem, siphoning off water, minerals, and sucrose", "Autotrophic plant that fixes nitrogen for crops, Mutualistic legume providing fertilizer, Epiphyte absorbing moisture from fog"),
            ("Phloem necrosis in Potato Leafroll Virus (PLRV)", "PLRV infection causes severe degeneration and necrosis of primary and secondary phloem sieve tubes in potato stems and tubers", "Causes carbohydrate accumulation in leaves (thick, leathery, rolled upward leaves) and internal net necrosis in potato tubers, ruining marketability", "Causes roots to turn green, Converts potato tubers into hollow wood, Prevents potato leaves from absorbing water"),
            ("Whiteflies (Bemisia tabaci) as phloem virus vectors", "Sap-sucking hemipterans that transmit over 100 devastating plant geminiviruses (e.g., Tomato Yellow Leaf Curl Virus - TYLCV, Cotton Leaf Curl)", "Major global agricultural pest causing billions of dollars in crop losses in tropical and subtropical regions", "Predatory beetles that eat leaves, Caterpillars that bore into wood, Parasitic fungi invading stomata"),
            ("Phytoplasma diseases (Aster Yellows / Coconut Lethal Yellowing)", "Wall-less bacteria (Mollicutes) that inhabit phloem sieve tube elements, disrupting hormone balance and assimilate partition", "Causes severe stunting, floral virescence (petals turn green and leaf-like), witches' brooms, and rapid lethal wilt", "Spore-forming fungi destroying xylem, Viruses living in cuticle wax, Bacterial infection of chloroplasts"),
            ("Sweet secretion (Guttation) vs Honeydew", "Guttation is pure, dilute xylem water exuded by the plant itself through hydathodes under root pressure; Honeydew is sticky, concentrated sucrose-rich insect excrement discharged by phloem-feeding aphids and whiteflies", "Honeydew attracts ants which establish mutualistic herds protecting aphids from ladybird beetle predators", "Both fluids are identical xylem sap, Guttation is produced by bees, Honeydew is secreted by root hairs"),
            ("Girdling by Rodents and Herbivores (e.g., Beavers, Porcupines)", "Animals gnawing off a continuous ring of outer bark and phloem around the base of a tree trunk during winter starvation", "Kills mature trees by cutting off downward sugar translocation to root systems, causing root death by spring", "Kills trees by stopping water from reaching leaves, Stimulates trees to produce triple wood, Has zero effect on tree health"),
            ("Sieve element plugging response to insect puncture", "Mechanical puncture activates rapid \\(\\text{Ca}^{2+}\\) influx, triggering instantaneous dispersion of P-protein bodies and callose synthesis over sieve pores", "Evolved as a mechanical and biochemical defense to arrest phloem sap leakage into feeding insect stylets", "Triggers explosive release of toxic gas, Dissolves the cell wall completely, Causes immediate cell division")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Phloem Pathology & Insect Interactions.**\n- Phloem-feeding insects (Aphids, Psyllids, Whiteflies): Tap stylets into pressurized sieve tubes \\(\\rightarrow\\) excrete honeydew \\(\\rightarrow\\) sooty mold; transmit lethal pathogens (HLB, TYLCV, PLRV).\n- Parasitic plants (Cuscuta / Dodder): Haustoria penetrate host phloem to steal sucrose.\n- Girdling by herbivores kills roots by blocking downward sugar transport.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Pathological / Ecological Significance:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    # Arch 7: Histochemistry, Microtechnique & Visualization of Phloem
    arch7 = {
        'templates': [
            "Which histochemical stain, microscopic technique, or fluorescent probe visualizes: '{0}'?:",
            "In botanical microtechnique and phloem cytology: '{0}' is detected using:",
            "What experimental protocol is used to demonstrate: '{0}'?:",
            "How do plant anatomists visualize and differentiate: '{0}'?:",
            "A student prepares a transverse section of Cucurbita stem: '{0}'. What is observed?:",
            "Which staining reagent specifically identifies: '{0}'?:",
            "In laboratory plant histology, '{0}' is confirmed by:",
            "What microscopic feature identifies: '{0}'?:",
            "Evaluate the diagnostic staining protocol for: '{0}':",
            "Identify the standard microchemical test utilized for: '{0}':"
        ],
        'data': [
            ("Aniline Blue fluorescence staining of Callose", "Aniline blue (fluorochrome) binds specifically to beta-1,3-glucan (callose) at sieve plates, emitting intense yellow-gold fluorescence under UV light", "Gold standard diagnostic technique for locating sieve plates and quantifying wound callose in plant sections", "Stains cellulose blue-black, Stains secondary lignin cherry red, Bleaches all plant cell walls"),
            ("Resorcin Blue (Lacmoid) staining of sieve plates", "Reacts with callose collars lining sieve pores, staining sieve plates bright blue to cobalt blue under brightfield light microscopy", "Classic histological stain for identifying functional sieve tube elements in Cucurbita and Vitis stems", "Stains starch grains deep purple, Stains xylem vessels bright red, Bleaches cytoplasm"),
            ("Cucurbita stem cross-section for phloem study", "Cucurbita (pumpkin) stems possess massive bicollateral vascular bundles (phloem present on BOTH outer and inner sides of xylem) with huge sieve plates", "Ideal demonstration specimen where sieve plates, companion cells, and callose plugs are clearly visible under standard light microscopy", "Possesses radial vascular bundles like roots, Completely lacks phloem, Vascular bundles lack xylem"),
            ("Transmission Electron Microscopy (TEM) of Sieve Elements", "Reveals complete absence of nucleus, tonoplast, and ribosomes, but confirms presence of functional mitochondria, plastids, and P-protein filaments along the parietal layer", "Conclusive ultrastructural proof of the living, enucleated, low-resistance state of functional sieve tubes", "Shows sieve tubes are completely dead hollow tubes like vessels, Shows a giant hyperactive nucleus, Shows cell wall is made of peptidoglycan"),
            ("Fluorescein (CFDA) tracer dye loading", "Carboxyfluorescein diacetate (CFDA) is loaded into leaf mesophyll; cleavage by cytoplasmic esterases releases membrane-impermeant fluorescent CF, which translocates exclusively through phloem", "Used in real-time confocal laser scanning microscopy to map symplastic phloem loading and transport pathways in living plants", "Stains dead xylem vessels red, Evaporates out through stomata like water vapor, Kills the plant cells instantly"),
            ("Fehling's / Benedict's test on Phloem sap vs Leaf extract", "Intact phloem sap tests NEGATIVE for reducing sugars (gives no red \\(\\text{Cu}_2\\text{O}\\) precipitate) because transport sugar is non-reducing sucrose; hydrolyzing sap with dilute HCl yields positive red test (glucose + fructose)", "Proves that non-reducing sucrose (not glucose) is the dedicated translocation sugar in phloem", "Proves sap is 100% starch, Proves phloem carries only mineral salts, Shows sap contains protein only"),
            ("Lugol's Iodine test on Sieve Tube Plastids", "Plastids in sieve tube elements (S-type plastids) contain specialized branched amylopectin starch grains that stain reddish-brown (not blue-black) with iodine", "Used in plant systematic anatomy to classify families (S-type vs P-type protein plastids)", "Stains all sieve elements pitch black, Dissolves sieve tubes completely, Stains callose green"),
            ("Double staining with Safranin and Fast Green for Vascular Bundles", "Safranin stains lignified xylem vessels, fibers, and sclerenchyma bright red; Fast Green stains non-lignified cellulosic walls of phloem sieve tubes, companion cells, and parenchyma brilliant green", "Provides unmistakable, high-contrast visual separation between xylem (red) and phloem (green)", "Stains both tissues identical red, Stains phloem red and xylem green, Dissolves phloem completely"),
            ("Freeze-substitution and cryo-SEM of phloem", "Rapid plunge-freezing in liquid propane followed by cryo-scanning electron microscopy preserves sieve tube contents in their native state without surging artifacts", "Proves that P-protein filaments are evenly distributed along parietal cytoplasm, not aggregated at sieve plates in uninjured living cells", "Melts the plant tissue into liquid, Proves that sieve tubes are completely empty, Destroys all cell walls"),
            ("Radioactive carbon (\\(^{14}\\text{C}\\)) tissue printing", "Pressing freshly cut stem cross-sections against photographic X-ray film reveals blackened silver grains localized strictly over phloem bundles", "Direct visual demonstration of radioactive photoassimilate localization in the phloem of intact plants", "Visualizes water movement in xylem, Measures cell wall thickness, Detects plant DNA")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Phloem Microtechnique & Diagnostic Stains.**\n- Callose at sieve plates: Aniline blue (yellow-gold fluorescence under UV), Resorcin blue (bright blue).\n- Bicollateral bundles in Cucurbita: Phloem on both sides of xylem with giant sieve plates.\n- Safranin/Fast Green: Xylem stains red (lignin), Phloem stains green (cellulose).\n- Sap chemistry: Sucrose is non-reducing (negative Benedict's until acid hydrolysis).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Laboratory / Analytical Principle:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 8: Agricultural Biotechnology, Crop Yield & Sink-Source Optimization
    arch8 = {
        'templates': [
            "Which agricultural biotechnology strategy, crop yield enhancement, or physiological trait relates to: '{0}'?:",
            "In crop physiology and agronomic enhancement: '{0}' is characterized by:",
            "What agronomic advantage or harvest index improvement arises from: '{0}'?:",
            "How does genetic manipulation of assimilate partitioning optimize: '{0}'?:",
            "A crop physiologist examines source-sink optimization: '{0}'. What is true?:",
            "Which molecular transporter or enzyme governs: '{0}'?:",
            "What is the agricultural value of: '{0}'?:",
            "Why is '{0}' critical for maximizing grain yield in staple cereals?:",
            "What technological advancement addresses: '{0}'?:",
            "Evaluate the crop science concept: '{0}':"
        ],
        'data': [
            ("SWEET Transporters (Sugars Will Eventually be Exported Transporters)", "Plasma membrane uniporters that mediate energy-independent facilitated diffusion of sucrose from phloem parenchyma into the apoplast", "Targeted by plant breeders to boost sugar loading into cereal grains; also targeted by bacterial pathogens (Xanthomonas) to steal sugar", "Pumps that move water into xylem, Enzymes that synthesize cell wall lignin, Transporters of toxic heavy metals"),
            ("Harvest Index (HI) and Assimilate Partitioning", "The ratio of harvested economic yield (grain, fruit, tuber) to total above-ground biological biomass: \\(\\text{HI} = \\text{Economic Yield} / \\text{Biological Yield}\\)", "The Green Revolution's dwarf wheat and rice varieties achieved \\(\\text{HI} \\approx 0.5\\) by redirecting photosynthates from tall straw stems to grain sinks", "Measures total water consumed by crop, Ratio of leaf area to root length, Measures soil fertilizer concentration"),
            ("Source-Sink Manipulation by Pruning and Fruit Thinning", "Selectively removing excess vegetative shoots (pruning) or thinning immature fruit clusters concentrates phloem photoassimilate flow into remaining fruits", "Produces significantly larger, sweeter, higher-grade commercial fruits (e.g., in apples, grapes, peaches)", "Causes remaining fruits to shrink, Kills the root system, Prevents all photosynthesis"),
            ("Cell Wall Invertase (CWIN) in reproductive sinks", "Hydrolyzes sucrose in the apoplast into glucose and fructose, maintaining a steep downhill concentration gradient that drives continuous phloem unloading into developing seeds", "Overexpression of CWIN in maize kernels significantly increases grain filling rate and final kernel weight", "Degrades starch in leaves, Converts glucose into toxic alcohol, Prevents flower pollination"),
            ("Heat stress damage to phloem loading during grain filling", "High temperatures (\\(> 35^\\circ\\text{C}\\)) inhibit sucrose transporters (SUTs) and invertases, disrupting phloem assimilate transport to developing cereal heads", "Results in unfilled, chalky, shriveled grains and massive agricultural yield losses under global warming", "Stimulates trees to double grain size, Accelerates photosynthesis by 500%, Causes leaves to turn into roots"),
            ("Girdling / Cincturing in Horticulture (e.g., Citrus, Avocado)", "Scoring or removing a shallow strip of phloem bark on a fruiting branch arrests downward sugar export, trapping all photoassimilates in that branch", "Triggers profuse flowering, increases fruit set, and accelerates fruit sizing and ripening for early market harvest", "Causes the tree trunk to rot instantly, Kills all the fruit within one day, Prevents leaves from transpiring"),
            ("Nitrogen fertilization and Sink-Source balance", "Excessive nitrogen fertilizer promotes runaway vegetative source growth (massive leafy canopy) at the expense of reproductive sink filling (delayed flowering and low grain yield)", "Agronomic nutrient management balances nitrogen to synchronize source capacity with sink demand", "Nitrogen stops all photosynthesis, Excess nitrogen converts crops into wood, Nitrogen destroys phloem fibers"),
            ("Stay-Green trait in Sorghum and Maize", "Genetic trait where leaves retain functional green chlorenchyma and active photosynthetic capacity throughout the grain filling stage without premature senescence", "Sustains prolonged phloem sucrose loading, increasing drought tolerance, grain weight, and forage quality", "Leaves drop off before flowering, Causes plants to stop absorbing water, Converts grain heads into leaves"),
            ("Foliar fertilizer application and Phloem Mobility", "Applying soluble nutrients (e.g., nitrogen as urea, potassium) directly to leaves: nutrients are absorbed and loaded into phloem for rapid distribution to sinks", "Essential agricultural rescue practice when root nutrient uptake is paralyzed by cold or waterlogged soils", "Leaves cannot absorb any nutrients, Foliar fertilizers travel through xylem only, Kills leaves immediately"),
            ("Metabolic Engineering of Sucrose Transporters (SUT/SUC)", "Upregulating companion cell sucrose-proton symporters (e.g., SUT1) enhances phloem loading efficiency, accelerating biomass accumulation and tuber yield in potatoes", "Promising biotechnological frontier for climate-resilient high-yield bioenergy crops", "Inhibits all sugar movement in stems, Causes plants to stop producing starch, Converts crops into weeds")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Agricultural Biotechnology & Sink-Source Optimization.**\n- Harvest Index (HI): Partitioning of photoassimilates to economic sinks (grain/tubers); enhanced by dwarf varieties and CWIN/SWEET transporters.\n- Horticultural practices: Pruning, thinning, and girdling concentrate phloem sap into commercial fruits.\n- Climate resilience: Heat stress impairs phloem loading; 'Stay-green' sustains prolonged grain filling.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Agronomic / Economic Significance:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-3-3.2.2", "Phloem: Sieve tubes, companion cells, phloem parenchyma, fibres (food translocation)", archs)


if __name__ == "__main__":
    q1 = gen_3_2_1()
    q2 = gen_3_2_2()
    print(f"gen_3_2_1: {len(q1)} questions")
    print(f"gen_3_2_2: {len(q2)} questions")
    print(f"Total Part 2 questions: {len(q1) + len(q2)}")
