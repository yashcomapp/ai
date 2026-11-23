import json
import random

random.seed(8606)

def build_ch6_questions():
    questions = []
    start_seq = 300

    def make_q(topic_code, subtopic_name, text, correct, wrongs, step1, step2, step3, diff="medium", vault="exam"):
        nonlocal start_seq
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

    vaults_80 = ["exam"] * 40 + ["practice"] * 20 + ["foundation"] * 20
    diffs_80 = (["easy"] * 15 + ["medium"] * 15 + ["hard"] * 10) + (["easy"] * 6 + ["medium"] * 8 + ["hard"] * 6) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)

    # -------------------------------------------------------------
    # 6.1.1 Intermolecular forces and spacing (13 questions)
    # -------------------------------------------------------------
    tc_611 = "MH-8-SCI-6-6.1.1"
    name_611 = "Intermolecular forces of attraction and particle spacing"
    c611_q = [
        ("In which physical state of matter are intermolecular forces of attraction MAXIMUM and intermolecular spaces MINIMUM?", "Solid state", ["Liquid state", "Gaseous state", "Plasma state"]),
        ("Why do particles in a gas move freely in all directions with very high kinetic velocity?", "Because intermolecular forces between gas particles are negligible (extremely weak)", ["Because gas particles are magnetic", "Because gas particles have zero mass", "Because temperature is zero"]),
        ("How does the intermolecular distance between particles change during the phase change from liquid to gas?", "Intermolecular distance increases dramatically by a factor of 10 to 100", ["It decreases to zero", "It remains completely unchanged", "Particles fuse together"]),
        ("In liquids, how strong are the intermolecular forces compared to solids?", "Moderately strong—sufficient to keep particles together in a fixed volume, but not enough to hold them in fixed positions", ["Much stronger than in solids", "Zero force", "Infinite force"])
    ]
    for i in range(13):
        ctx, ans, wrongs = c611_q[i % len(c611_q)]
        q = make_q(
            tc_611, name_611,
            f"Intermolecular Forces in Matter: {ctx}",
            ans, wrongs,
            "The physical state of matter depends on the balance between intermolecular attraction and thermal particle motion.",
            "Solids have maximum attraction and minimum spacing; gases have negligible attraction and large spacing.",
            f"Hence, '{ans}' is correct.",
            "medium" if i % 2 == 0 else "easy", "exam"
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 6.1.2 Rigidity, fluidity, compressibility (13 questions)
    # -------------------------------------------------------------
    tc_612 = "MH-8-SCI-6-6.1.2"
    name_612 = "Definite shape, volume, rigidity, fluidity, compressibility comparison"
    c612_q = [
        ("Which state of matter possesses a definite volume and high fluidity, but acquires the shape of its container?", "Liquid state", ["Solid state", "Gaseous state", "Plasma"]),
        ("Why are gases highly compressible compared to solids and liquids?", "Because of the vast empty intermolecular spaces between gas molecules", ["Because gas particles can shrink in size", "Because gas molecules are hollow", "Because gases have no mass"]),
        ("The property of solids to maintain their fixed shape when subjected to external force is called:", "Rigidity", ["Fluidity", "Compressibility", "Diffusion"]),
        ("Both liquids and gases are classified as 'Fluids' because:", "Their constituent particles can slide or flow past one another", ["They have definite shapes", "They are completely incompressible", "They conduct electricity"])
    ]
    for i in range(13):
        ctx, ans, wrongs = c612_q[i % len(c612_q)]
        q = make_q(
            tc_612, name_612,
            f"Macroscopic Properties of Matter: {ctx}",
            ans, wrongs,
            "Solids possess rigidity, definite shape, and volume.",
            "Liquids flow and take container shape with fixed volume; gases possess maximum compressibility and fill any volume.",
            f"Therefore, '{ans}' is correct.",
            "medium" if i % 2 == 0 else "easy", "exam"
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 6.2.1 Element definition (80 questions)
    # -------------------------------------------------------------
    tc_621 = "MH-8-SCI-6-6.2.1"
    name_621 = "Element: purest substance consisting of single type of atom"
    elem_q = [
        ("What is the definition of a chemical 'Element'?", "A pure substance whose molecules consist of only one single type of atom and cannot be broken down by ordinary chemical means", ["A mixture of two or more liquids", "A substance made of different atoms chemically combined", "A homogeneous solution in water"]),
        ("Which of the following substances is a pure chemical ELEMENT?", "Gold (Au) / Iron (Fe) / Oxygen (O₂)", ["Water (H₂O)", "Common salt (NaCl)", "Carbon dioxide (CO₂)"]),
        ("Can an element be decomposed into simpler distinct chemical substances through ordinary physical or chemical reactions?", "No, elements represent the fundamental chemical building blocks of matter", ["Yes, by heating in an oven", "Yes, by dissolving in water", "Yes, by filtering through paper"]),
        ("The smallest fundamental representative particle of an element that retains its chemical identity is:", "An atom", ["A compound", "A colloid", "A suspension"]),
        ("How many known chemical elements have been identified and organized on the Modern Periodic Table to date?", "118 elements", ["92 elements", "150 elements", "200 elements"]),
        ("An oxygen molecule (\\(\\text{O}_2\\)) is categorized as an element because:", "It is composed entirely of identical oxygen atoms bonded together", ["It is a gas", "It supports combustion", "It has mass"]),
        ("Which element is a lustrous liquid metal at room temperature?", "Mercury (Hg)", ["Bromine (Br)", "Sodium (Na)", "Lead (Pb)"]),
        ("Which element is a dark reddish-brown liquid non-metal at standard room temperature?", "Bromine (Br)", ["Chlorine (Cl)", "Iodine (I)", "Phosphorus (P)"])
    ]
    for i in range(80):
        ctx, ans, wrongs = elem_q[i % len(elem_q)]
        q = make_q(
            tc_621, name_621,
            f"Chemical Elements: {ctx}",
            ans, wrongs,
            "An element is a pure substance composed of only one kind of atom.",
            "It cannot be chemically split into simpler substances by ordinary reactions.",
            f"Thus, '{ans}' is the correct response.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 6.2.2 Compound definition (80 questions)
    # -------------------------------------------------------------
    tc_622 = "MH-8-SCI-6-6.2.2"
    name_622 = "Compound: chemical combination of elements in fixed proportion by weight"
    comp_q = [
        ("What is a chemical 'Compound'?", "A pure substance formed by the chemical combination of two or more elements in a fixed proportion by mass", ["A physical blend of substances in any arbitrary ratio", "A single type of atom", "An impure solution"]),
        ("In pure water (\\(\\text{H}_2\\text{O}\\)), what is the fixed ratio by mass of Hydrogen to Oxygen according to the Law of Constant Proportions?", "1 : 8 (\\(2\\text{ g H} : 16\\text{ g O}\\))", ["2 : 1", "1 : 16", "1 : 2"]),
        ("How do the chemical and physical properties of a compound compare to those of its constituent elements?", "The properties of a compound are entirely new and completely different from its constituent elements", ["The compound retains all properties of both elements", "The compound has properties identical to the heavier element", "The compound is always a gas"]),
        ("Hydrogen is highly inflammable and oxygen supports combustion; yet their compound water (\\(\\text{H}_2\\text{O}\\)) acts as:", "A fire extinguisher (completely extinguishing combustion)", ["A powerful explosive", "A combustible fuel", "A toxic oxidant"]),
        ("Can the constituent elements of a chemical compound be separated by simple physical methods (like filtration or magnets)?", "No, they can only be separated through chemical or electrochemical reactions (such as electrolysis)", ["Yes, by using a hand magnet", "Yes, by filtering through paper", "Yes, by letting it stand"]),
        ("Which of the following common household substances is a pure chemical COMPOUND?", "Common salt (Sodium Chloride, NaCl)", ["Air", "Milk", "Lemonade"]),
        ("In Carbon Dioxide (\\(\\text{CO}_2\\)), what is the fixed proportion by weight of Carbon to Oxygen?", "3 : 8 (\\(12\\text{ g C} : 32\\text{ g O}\\))", ["1 : 2", "3 : 4", "1 : 1"]),
        ("The smallest representative unit of a chemical compound that exhibits its complete properties is:", "A molecule", ["An atom", "A nucleon", "An isotope"])
    ]
    for i in range(80):
        ctx, ans, wrongs = comp_q[i % len(comp_q)]
        q = make_q(
            tc_622, name_622,
            f"Chemical Compounds: {ctx}",
            ans, wrongs,
            "A compound is formed when elements combine chemically in fixed mass proportions.",
            "Its properties differ fundamentally from the constituent elements, requiring chemical reactions for separation.",
            f"Therefore, '{ans}' is correct.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 6.2.3 Mixture definition (80 questions)
    # -------------------------------------------------------------
    tc_623 = "MH-8-SCI-6-6.2.3"
    name_623 = "Mixture: physical combination of substances in any proportion"
    mix_q = [
        ("What is a 'Mixture' in chemistry?", "A physical combination of two or more substances in any arbitrary proportion without any chemical reaction", ["A pure substance with fixed chemical formula", "A single element bonded to itself", "A crystal lattice"]),
        ("Do the constituent components of a mixture retain their individual original physical and chemical properties?", "Yes, each constituent retains its individual properties", ["No, completely new chemical properties are formed", "Only in the dark", "Only when boiled"]),
        ("Can the components of an iron filings and sulphur powder mixture be separated by simple physical means?", "Yes, rolling a magnet over the mixture readily attracts and separates the iron filings", ["No, they must be electrolyzed", "No, they cannot be separated", "Only by nuclear fission"]),
        ("Why is atmospheric air classified as a mixture rather than a compound?", "Because its constituent gases (nitrogen, oxygen, argon, CO₂) retain their individual properties and exist in variable proportions without chemical bonds", ["Because air is invisible", "Because air has weight", "Because air has uniform temperature"]),
        ("Is heat or light energy mandatorily absorbed or evolved when a simple physical mixture is prepared?", "No, there is generally no chemical energy exchange or reaction during mechanical mixing", ["Yes, an explosion always occurs", "Yes, mass increases by 50%", "Yes, it creates a new element"]),
        ("Which of the following is a classic example of a solid-liquid mixture?", "Salt dissolved in water / muddy water", ["Pure distilled water", "Carbon dioxide gas", "Metallic copper wire"]),
        ("Does a mixture have a sharp, fixed, definite melting or boiling point?", "No, mixtures melt and boil over a range of temperatures depending on their variable composition", ["Yes, always at 100°C", "Yes, always at 0°C", "Yes, identical to water"]),
        ("Brass (an alloy of copper and zinc) is classified as:", "A solid homogeneous metallic mixture (alloy)", ["A chemical compound with covalent bonds", "A pure chemical element", "A suspension"])
    ]
    for i in range(80):
        ctx, ans, wrongs = mix_q[i % len(mix_q)]
        q = make_q(
            tc_623, name_623,
            f"Chemical Mixtures: {ctx}",
            ans, wrongs,
            "A mixture is a physical combination of substances in variable proportions.",
            "Components retain their individual properties and can be separated by physical techniques.",
            f"Hence, '{ans}' is correct.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 6.3.1 Homogeneous mixture (80 questions)
    # -------------------------------------------------------------
    tc_631 = "MH-8-SCI-6-6.3.1"
    name_631 = "Homogeneous mixture: uniform composition throughout (solutions)"
    homo_q = [
        ("A mixture that possesses a completely uniform composition and identical properties throughout all its parts is called:", "A homogeneous mixture", ["A heterogeneous mixture", "A coarse suspension", "An aerosol"]),
        ("Which of the following is an example of a HOMOGENEOUS mixture?", "Salt dissolved completely in water (salt solution)", ["Chalk powder stirred in water", "Oil floating on water", "Iron filings mixed with sand"]),
        ("How many distinct physical phases are observable in a completely homogeneous mixture?", "Only one single uniform phase", ["Two distinct visible phases", "Three separate layers", "Infinite phases"]),
        ("Why is a filtered sugar syrup solution classified as homogeneous?", "Because sugar molecules are uniformly dispersed among water molecules, with identical sweetness in every drop", ["Because sugar settles at the bottom", "Because you can see sugar crystals floating", "Because it is opaque"]),
        ("Clean filtered air, clear sea water, and bronze metal alloy are all examples of:", "Homogeneous mixtures", ["Heterogeneous suspensions", "Pure elements", "Chemical compounds"]),
        ("Can the individual dissolved particles in a true homogeneous solution be separated by ordinary filter paper?", "No, solute particles pass freely through filter pores because they are molecularly dispersed", ["Yes, filter paper catches all dissolved salt", "Yes, sugar stays on the paper", "Only if filtered twice"]),
        ("In a homogeneous liquid solution, does the dissolved solute settle out when left undisturbed for hours?", "No, the solution is completely stable and solute particles remain permanently dispersed", ["Yes, solute settles within 10 minutes", "Yes, solute floats to the surface", "Yes, it turns into gas"]),
        ("A true solution of alcohol in water represents which type of homogeneous mixture?", "Liquid-in-liquid homogeneous solution", ["Solid-in-solid suspension", "Gas-in-liquid colloid", "Coarse heterogeneous mixture"])
    ]
    for i in range(80):
        ctx, ans, wrongs = homo_q[i % len(homo_q)]
        q = make_q(
            tc_631, name_631,
            f"Homogeneous Mixtures: {ctx}",
            ans, wrongs,
            "Homogeneous mixtures have uniform composition and single-phase appearance throughout.",
            "True solutions like saline water do not settle and cannot be separated by filtration.",
            f"Thus, '{ans}' is correct.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 6.3.2 Heterogeneous mixture (80 questions)
    # -------------------------------------------------------------
    tc_632 = "MH-8-SCI-6-6.3.2"
    name_632 = "Heterogeneous mixture: non-uniform composition (suspensions, colloids)"
    hetero_q = [
        ("A mixture in which the components are not uniformly distributed and distinct phase boundaries exist is termed:", "A heterogeneous mixture", ["A homogeneous solution", "A pure substance", "An element"]),
        ("Which of the following mixtures is HETEROGENEOUS?", "A mixture of oil and water / muddy water", ["Salt dissolved in water", "Pure vinegar", "Clean atmospheric air"]),
        ("When sand is stirred in water, two distinct physical layers are clearly visible. This exemplifies:", "A heterogeneous solid-liquid mixture", ["A homogeneous true solution", "A chemical compound", "An element"]),
        ("Why does shaking a mixture of kerosene and water result in a heterogeneous system?", "Kerosene and water are immiscible liquids that separate into two distinct layers upon standing", ["Kerosene reacts chemically with water to form gas", "Water dissolves kerosene completely", "They form a true solution"]),
        ("Soil collected from a garden is categorized as:", "A complex heterogeneous mixture containing minerals, decaying organic matter, and microbes", ["A pure compound", "A homogeneous true solution", "A single element"]),
        ("Blood, milk, and paints are classified as heterogeneous mixtures because:", "Under high microscopic magnification, distinct suspended particles/droplets are dispersed in a liquid medium", ["They are transparent", "They contain only one type of atom", "They have fixed chemical formulas"]),
        ("Can the dispersed solid particles in a heterogeneous muddy water mixture be separated by filtration?", "Yes, the solid particles are trapped on filter paper as residue", ["No, they pass through like water", "Only by chemical titration", "Only by magnetic attraction"]),
        ("A mixture of iron filings and sand is:", "A solid-solid heterogeneous mixture", ["A homogeneous solution", "A chemical compound", "An alloy"])
    ]
    for i in range(80):
        ctx, ans, wrongs = hetero_q[i % len(hetero_q)]
        q = make_q(
            tc_632, name_632,
            f"Heterogeneous Mixtures: {ctx}",
            ans, wrongs,
            "Heterogeneous mixtures have non-uniform distribution of constituent parts and visible phase boundaries.",
            "Examples include oil-water emulsions and muddy suspensions.",
            f"Therefore, '{ans}' is the correct response.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 6.4.1 Solutions: solute and solvent (80 questions)
    # -------------------------------------------------------------
    tc_641 = "MH-8-SCI-6-6.4.1"
    name_641 = "Solution: solute and solvent, true solution particle size < 1 nm"
    soln_q = [
        ("In a sugar solution prepared by dissolving sugar in water, which component is the 'Solvent'?", "Water (the component present in larger quantity that dissolves the solute)", ["Sugar", "The glass container", "Air bubbles"]),
        ("In an aqueous solution of common salt, the salt is designated as the:", "Solute (the component present in lesser quantity that gets dissolved)", ["Solvent", "Precipitate", "Emulsifier"]),
        ("What is the typical diameter of solute particles in a True Solution?", "Less than 1 nanometre (\\(< 1\\text{ nm} = 10^{-9}\\text{ m}\\))", ["Between 10 and 100 micrometres", "Greater than 1000 nanometres", "1 millimetre"]),
        ("Why does a true solution (like salt water) appear completely clear and transparent without scattering a beam of light?", "Because the solute particles are so tiny (< 1 nm) that they cannot scatter light rays", ["Because water absorbs all light", "Because salt reflects all light", "Because the solution is in the dark"]),
        ("A solution in which water acts as the solvent is universally called:", "An aqueous solution", ["A non-aqueous solution", "A tincture", "An amalgam"]),
        ("Tincture of iodine is a medical antiseptic solution in which iodine solute is dissolved in which solvent?", "Alcohol", ["Water", "Kerosene", "Ether"]),
        ("Carbonated soft drinks (soda water) represent which type of solution?", "Gas dissolved in a liquid (\\(\\text{CO}_2\\) in water)", ["Liquid in gas", "Solid in solid", "Gas in gas"]),
        ("A solution that contains the maximum possible amount of dissolved solute at a given temperature is called:", "A saturated solution", ["An unsaturated solution", "A dilute solution", "A suspension"])
    ]
    for i in range(80):
        ctx, ans, wrongs = soln_q[i % len(soln_q)]
        q = make_q(
            tc_641, name_641,
            f"True Solutions & Solubility: {ctx}",
            ans, wrongs,
            "A solution is a homogeneous mixture of solute and solvent.",
            "In true solutions, solute particles are smaller than 1 nm, remaining transparent and stable.",
            f"Hence, '{ans}' is correct.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 6.4.2 Suspension: particle size > 1000 nm (80 questions)
    # -------------------------------------------------------------
    tc_642 = "MH-8-SCI-6-6.4.2"
    name_642 = "Suspension: heterogeneous mixture particle size > 1000 nm, settles on standing"
    susp_q = [
        ("What is a 'Suspension' in chemistry?", "A heterogeneous mixture in which insoluble solid particles (> 1000 nm) remain suspended in a liquid and settle on standing", ["A homogeneous clear solution", "A pure chemical compound", "A mixture of two gases"]),
        ("What is the typical diameter of dispersed particles in a suspension?", "Greater than 1000 nanometres (\\(> 1000\\text{ nm} = 1\\,\\mu\\text{m}\\))", ["Less than 1 nm", "Between 1 and 10 nm", "0.1 nm"]),
        ("What happens when an opaque suspension of chalk powder in water is left undisturbed on a table?", "The chalk particles gradually settle down at the bottom due to gravity (sedimentation)", ["The chalk dissolves into a clear liquid", "The chalk evaporates into the air", "The water boils"]),
        ("Can the suspended particles in a suspension be separated from the liquid by ordinary filter paper?", "Yes, the particles are larger than the filter pores and are retained as residue", ["No, they pass freely through filter pores", "Only by boiling", "Only by centrifugal magnets"]),
        ("Why does a freshly shaken suspension of flour in water scatter a beam of light?", "Because the large suspended particles obstruct and scatter the light beam", ["Because flour glows in the dark", "Because water is transparent", "Because the particles absorb all light"]),
        ("Which of the following is a classic example of a suspension?", "Chalk powder in water / sand in water", ["Salt in water", "Sugar in water", "Alcohol in water"]),
        ("Are the dispersed particles in a suspension visible to the naked human eye or under a simple microscope?", "Yes, because their particle diameter exceeds 1000 nm", ["No, they require an electron microscope", "No, they have zero volume", "Only in ultraviolet light"]),
        ("Why do medical prescription suspensions (like antacid syrups) carry the instruction 'SHAKE WELL BEFORE USE'?", "To re-disperse the settled drug particles uniformly throughout the liquid before dosing", ["To cool the medicine", "To generate gas", "To dissolve the bottle"])
    ]
    for i in range(80):
        ctx, ans, wrongs = susp_q[i % len(susp_q)]
        q = make_q(
            tc_642, name_642,
            f"Suspension Chemistry: {ctx}",
            ans, wrongs,
            "A suspension is a heterogeneous mixture with particles larger than 1000 nm.",
            "These particles settle under gravity upon standing and can be separated by filtration.",
            f"Thus, '{ans}' is the correct response.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 6.4.3 Colloid and Tyndall effect (80 questions)
    # -------------------------------------------------------------
    tc_643 = "MH-8-SCI-6-6.4.3"
    name_643 = "Colloid: particle size 1 to 1000 nm, Tyndall scattering of light (milk, ink, smoke)"
    colloid_q = [
        ("What is the size range of dispersed particles in a 'Colloid' (colloidal solution)?", "Between 1 nanometre and 1000 nanometres (\\(1\\text{ to } 1000\\text{ nm}\\))", ["Less than 0.1 nm", "Greater than 100,000 nm", "Over 1 centimetre"]),
        ("What is the phenomenon of scattering of a visible light beam by colloidal particles called?", "Tyndall Effect", ["Raman Effect", "Doppler Effect", "Photoelectric Effect"]),
        ("Why does a beam of sunlight streaming through a small hole into a dusty room become visibly illuminated?", "Because airborne dust particles act as a colloid and scatter the light beam (Tyndall effect)", ["Because sunlight is magnetic", "Because dust generates its own light", "Because the air is heated"]),
        ("Which of the following everyday substances is classified as a COLLOID?", "Milk / Fog / Smoke / Ink", ["Salt water solution", "Clear tap water", "Pure carbon dioxide gas"]),
        ("Do colloidal particles (such as butterfat droplets in milk) settle down at the bottom when left standing undisturbed?", "No, colloidal particles remain suspended indefinitely due to Brownian motion", ["Yes, they settle within seconds", "Yes, they precipitate immediately", "Yes, like heavy stones"]),
        ("Can colloidal particles be separated from the liquid medium using standard filter paper?", "No, colloidal particles are small enough to pass through standard filter paper pores", ["Yes, filter paper captures all milk particles", "Yes, like sand", "Only with metal filters"]),
        ("Fog and clouds in the atmosphere represent which type of colloidal system?", "Liquid droplets dispersed in a gas (Aerosol)", ["Solid in liquid (Sol)", "Gas in liquid (Foam)", "Liquid in solid (Gel)"]),
        ("Why does milk appear translucent or opaque white instead of transparent?", "Because colloidal fat and protein particles scatter light in all directions", ["Because it contains chalk", "Because water is white", "Because it absorbs all light"])
    ]
    for i in range(80):
        ctx, ans, wrongs = colloid_q[i % len(colloid_q)]
        q = make_q(
            tc_643, name_643,
            f"Colloidal Systems & Tyndall Effect: {ctx}",
            ans, wrongs,
            "Colloids have particle sizes between 1 and 1000 nm.",
            "They scatter light beams (Tyndall effect), do not settle upon standing, and pass through filter paper.",
            f"Therefore, '{ans}' is correct.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 6.5.1 Chemical formulae cross-over technique (80 questions)
    # -------------------------------------------------------------
    tc_651 = "MH-8-SCI-6-6.5.1"
    name_651 = "Writing chemical formulae using constituent elements and valency cross-over technique"
    formula_pairs = [
        ("Sodium (valency 1) and Chlorine (valency 1)", "\\(\\text{NaCl}\\)", ["\\(\\text{Na}_2\\text{Cl}\\)", "\\(\\text{NaCl}_2\\)", "\\(\\text{Na}_2\\text{Cl}_2\\)"]),
        ("Magnesium (valency 2) and Chlorine (valency 1)", "\\(\\text{MgCl}_2\\)", ["\\(\\text{MgCl}\\)", "\\(\\text{Mg}_2\\text{Cl}\\)", "\\(\\text{Mg}_2\\text{Cl}_3\\)"]),
        ("Aluminium (valency 3) and Oxygen (valency 2)", "\\(\\text{Al}_2\\text{O}_3\\)", ["\\(\\text{AlO}\\)", "\\(\\text{Al}_3\\text{O}_2\\)", "\\(\\text{AlO}_2\\)"]),
        ("Calcium (valency 2) and Oxygen (valency 2)", "\\(\\text{CaO}\\)", ["\\(\\text{Ca}_2\\text{O}_2\\)", "\\(\\text{CaO}_2\\)", "\\(\\text{Ca}_2\\text{O}\\)"]),
        ("Carbon (valency 4) and Oxygen (valency 2)", "\\(\\text{CO}_2\\)", ["\\(\\text{C}_2\\text{O}_4\\)", "\\(\\text{CO}\\)", "\\(\\text{C}_4\\text{O}_2\\)"]),
        ("Hydrogen (valency 1) and Sulphur (valency 2)", "\\(\\text{H}_2\\text{S}\\)", ["\\(\\text{HS}\\)", "\\(\\text{HS}_2\\)", "\\(\\text{H}_2\\text{S}_2\\)"]),
        ("Carbon (valency 4) and Hydrogen (valency 1)", "\\(\\text{CH}_4\\)", ["\\(\\text{CH}\\)", "\\(\\text{C}_4\\text{H}\\)", "\\(\\text{C}_2\\text{H}_4\\)"]),
        ("Iron(III) (valency 3) and Oxygen (valency 2)", "\\(\\text{Fe}_2\\text{O}_3\\)", ["\\(\\text{FeO}\\)", "\\(\\text{Fe}_3\\text{O}_2\\)", "\\(\\text{FeO}_2\\)"])
    ]
    for i in range(80):
        pair_desc, ans, wrongs = formula_pairs[i % len(formula_pairs)]
        q = make_q(
            tc_651, name_651,
            f"Determine the correct molecular formula using the valency cross-over method for: {pair_desc}.",
            ans, wrongs,
            "Write the chemical symbols of the constituent elements side-by-side.",
            "Write their respective valencies below the symbols and cross-multiply (criss-cross) them.",
            f"Simplify the subscripts to the lowest whole-number ratio to arrive at \\({ans}\\).",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch6_questions()
    print(f"Generated {len(qs)} questions for Chapter 6.")
    out_path = "scripts/mh8_sci_ch6_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
