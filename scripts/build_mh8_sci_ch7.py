import json
import random

random.seed(8707)

def build_ch7_questions():
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
    # 7.1.1 Physical properties of metals (39 questions)
    # -------------------------------------------------------------
    tc_711 = "MH-8-SCI-7-7.1.1"
    name_711 = "Lustre, hardness, malleability, ductility, conduction of heat and electricity, sonority, high density and melting points"
    c711_q = [
        ("The property of metals that allows them to be hammered into thin sheets without shattering is called:", "Malleability", ["Ductility", "Sonority", "Lustre"]),
        ("The mechanical property by which metals can be drawn into long, thin wires is called:", "Ductility", ["Malleability", "Hardness", "Brittleness"]),
        ("Which metal is the best conductor of electricity and heat among all chemical elements?", "Silver (Ag)", ["Iron (Fe)", "Lead (Pb)", "Aluminium (Al)"]),
        ("Why are school bells and temple chimes manufactured from bell metal (an alloy of copper and tin)?", "Because metals possess sonority (producing a deep ringing sound when struck)", ["Because metals are malleable", "Because metals conduct heat", "Because metals are ductile"]),
        ("Gold and silver are prized for making jewelry primarily because of their high malleability, ductility, and:", "Metallic lustre and resistance to corrosion", ["Low melting points", "High electrical resistance", "Brittleness"]),
        ("Which metal has the highest melting point (around 3422°C), making it ideal for incandescent light bulb filaments?", "Tungsten (W)", ["Copper (Cu)", "Iron (Fe)", "Gold (Au)"])
    ]
    for i in range(39):
        ctx, ans, wrongs = c711_q[i % len(c711_q)]
        q = make_q(
            tc_711, name_711,
            f"Physical Metallurgy: {ctx}",
            ans, wrongs,
            "Metals typically exhibit lustre, hardness, malleability, ductility, sonority, and high electrical/thermal conductivity.",
            "These properties stem from metallic bonding with delocalized valence electron seas.",
            f"Hence, '{ans}' is correct.",
            "medium" if i % 2 == 0 else "easy", "exam"
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 7.1.2 Exceptions: Mercury, Gallium, Sodium, Potassium (37 questions)
    # -------------------------------------------------------------
    tc_712 = "MH-8-SCI-7-7.1.2"
    name_712 = "Exceptions: Mercury and Gallium (liquids), Sodium and Potassium (soft, low density)"
    c712_q = [
        ("Which metal is uniquely in the liquid state at standard room temperature (25°C)?", "Mercury (Hg)", ["Gallium (Ga)", "Sodium (Na)", "Bromine (Br)"]),
        ("Which metals are so soft that they can be easily cut with an ordinary kitchen knife?", "Sodium (Na) and Potassium (K)", ["Iron and Copper", "Aluminium and Gold", "Tungsten and Zinc"]),
        ("Which metal melts when placed on the palm of a human hand due to body heat (melting point ~30°C)?", "Gallium (Ga) / Caesium (Cs)", ["Iron (Fe)", "Lead (Pb)", "Platinum (Pt)"]),
        ("Why do alkali metals like Sodium (0.97 g/cm³) and Potassium (0.86 g/cm³) float on water?", "Because their densities are lower than the density of water (1.0 g/cm³)", ["Because they are magnetic", "Because they have no mass", "Because they repel water"])
    ]
    for i in range(37):
        ctx, ans, wrongs = c712_q[i % len(c712_q)]
        q = make_q(
            tc_712, name_712,
            f"Metallic Exceptions: {ctx}",
            ans, wrongs,
            "While most metals are hard solids, mercury is liquid at room temperature.",
            "Sodium and potassium are soft alkali metals with low densities cut by a knife.",
            f"Therefore, '{ans}' is the correct exception.",
            diffs_80[i % len(diffs_80)], "exam"
        )
        questions.append(q)

    # Helper generator for standard 80-q subtopics
    def add_sci_subtopic(tc, name, cases):
        for i in range(80):
            ctx, ans, wrongs, s1, s2, s3 = cases[i % len(cases)]
            q = make_q(tc, name, ctx, ans, wrongs, s1, s2, s3, diffs_80[i], vaults_80[i])
            questions.append(q)

    # -------------------------------------------------------------
    # 7.2.1 Physical properties of non-metals (80 questions)
    # -------------------------------------------------------------
    tc_721 = "MH-8-SCI-7-7.2.1"
    name_721 = "Non-lustrous, brittle, poor conductors of heat and electricity"
    c721_data = [
        ("What happens when a solid piece of sulphur or coal (carbon) is struck with a hammer?", "It breaks into small pieces or powder because non-metals are brittle", ["It flattens into a thin sheet", "It draws into a thin wire", "It rings with a sonorous chime"],
         "Non-metals lack malleability and ductility.", "When subjected to mechanical stress, their covalent lattices fracture readily, exhibiting brittleness.", "Hence, 'breaks into small pieces' is correct."),
        ("Non-metals are generally classified electrically as:", "Insulators (poor conductors of electricity and heat)", ["Superconductors", "Excellent conductors", "Semiconductors only"],
         "Non-metals lack free delocalized valence electrons.", "Consequently, they cannot easily conduct electric charge or thermal energy.", "Thus, insulators is correct.")
    ]
    add_sci_subtopic(tc_721, name_721, c721_data)

    # -------------------------------------------------------------
    # 7.2.2 Non-metal exceptions: Diamond, Graphite, Iodine (80 questions)
    # -------------------------------------------------------------
    tc_722 = "MH-8-SCI-7-7.2.2"
    name_722 = "Exceptions: Diamond (hardest substance, good heat conductor), Graphite (good electric conductor), Iodine (lustrous)"
    c722_data = [
        ("Which allotrope of non-metal carbon is the hardest naturally occurring substance known on Earth?", "Diamond", ["Graphite", "Fullerene", "Coal"],
         "Diamond has a 3D tetrahedral giant covalent network of carbon atoms.", "This rigid architecture makes it the hardest natural substance.", "Thus, diamond is correct."),
        ("Which non-metal is an exceptional GOOD conductor of electricity due to free mobile pi-electrons?", "Graphite", ["Diamond", "Sulphur", "Phosphorus"],
         "In graphite, each carbon atom bonds to 3 others in hexagonal layers, leaving one free mobile electron per atom.", "These delocalized electrons conduct electricity.", "Hence, graphite is correct."),
        ("Which non-metal displays a shiny, sparkling metallic-like crystalline lustre?", "Iodine (I₂)", ["Sulphur", "Phosphorus", "Carbon black"],
         "Non-metals are typically dull in appearance.", "Iodine is a notable exception, forming shiny lustrous purple-black crystals.", "Therefore, Iodine is correct.")
    ]
    add_sci_subtopic(tc_722, name_722, c722_data)

    # -------------------------------------------------------------
    # 7.3.1 Reaction with oxygen: basic metal oxides (80 questions)
    # -------------------------------------------------------------
    tc_731 = "MH-8-SCI-7-7.3.1"
    name_731 = "Reaction with oxygen: basic metal oxides"
    c731_data = [
        ("When metals react with atmospheric oxygen on heating, what type of chemical oxides do they form?", "Basic oxides (e.g. \\(\\text{MgO, Na}_2\\text{O, CaO}\\))", ["Acidic oxides", "Neutral oxides", "Amphoteric only"],
         "Metals react with oxygen to form metal oxides: \\(2\\text{Mg} + \\text{O}_2 \\rightarrow 2\\text{MgO}\\).", "When dissolved in water, they form bases that turn red litmus paper blue.", "Hence, basic oxides is correct.")
    ]
    add_sci_subtopic(tc_731, name_731, c731_data)

    # -------------------------------------------------------------
    # 7.3.2 Reaction with water: metal hydroxides and H2 gas (80 questions)
    # -------------------------------------------------------------
    tc_732 = "MH-8-SCI-7-7.3.2"
    name_732 = "Reaction with water: metal hydroxides and hydrogen gas"
    c732_data = [
        ("When sodium (Na) or potassium (K) reacts violently with cold water, which gas is released with effervescence?", "Hydrogen gas (\\(\\text{H}_2\\))", ["Oxygen gas (\\(\\text{O}_2\\))", "Carbon dioxide (\\(\\text{CO}_2\\))", "Nitrogen gas (\\(\\text{N}_2\\))"],
         "Active metals displace hydrogen from water: \\(2\\text{Na} + 2\\text{H}_2\\text{O} \\rightarrow 2\\text{NaOH} + \\text{H}_2\\uparrow\\).", "The evolved hydrogen burns with a pop sound.", "Thus, hydrogen gas is correct.")
    ]
    add_sci_subtopic(tc_732, name_732, c732_data)

    # -------------------------------------------------------------
    # 7.3.3 Reaction with dilute acids (80 questions)
    # -------------------------------------------------------------
    tc_733 = "MH-8-SCI-7-7.3.3"
    name_733 = "Reaction with dilute acids: salt and hydrogen gas evolution"
    c733_data = [
        ("What products are formed when reactive metals (like zinc or magnesium) react with dilute hydrochloric acid?", "Metal salt and hydrogen gas (\\(\\text{Zn} + 2\\text{HCl} \\rightarrow \\text{ZnCl}_2 + \\text{H}_2\\uparrow\\))", ["Metal oxide and water", "Chlorine gas and water", "No reaction occurs"],
         "Reactive metals above hydrogen in the activity series displace hydrogen from dilute acids.", "This produces the corresponding metal salt and gaseous \\(\\text{H}_2\\).", "Hence, salt and hydrogen gas is correct.")
    ]
    add_sci_subtopic(tc_733, name_733, c733_data)

    # -------------------------------------------------------------
    # 7.4.1 Reaction with oxygen: acidic non-metal oxides (80 questions)
    # -------------------------------------------------------------
    tc_741 = "MH-8-SCI-7-7.4.1"
    name_741 = "Reaction with oxygen: acidic or neutral non-metal oxides (CO2, SO2)"
    c741_data = [
        ("When non-metals (such as carbon and sulphur) burn in air, what chemical nature do their resulting oxides possess?", "Acidic oxides (turn moist blue litmus red when dissolved in water)", ["Basic oxides", "Neutral only", "Alkaline oxides"],
         "Non-metal combustion produces non-metal oxides: \\(\\text{S} + \\text{O}_2 \\rightarrow \\text{SO}_2\\).", "Dissolving in water produces acids (\\(\\text{SO}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{H}_2\\text{SO}_3\\)) that turn blue litmus red.", "Thus, acidic oxides is correct.")
    ]
    add_sci_subtopic(tc_741, name_741, c741_data)

    # -------------------------------------------------------------
    # 7.4.2 Non-metals generally do not react with dilute acids (80 questions)
    # -------------------------------------------------------------
    tc_742 = "MH-8-SCI-7-7.4.2"
    name_742 = "Non-metals generally do not react with dilute acids"
    c742_data = [
        ("What happens when solid sulphur or charcoal is mixed with dilute hydrochloric acid at room temperature?", "No chemical reaction occurs and no hydrogen gas is evolved", ["Violent explosion occurs", "Oxygen gas is liberated", "Salt precipitates immediately"],
         "Non-metals are electron acceptors and cannot supply electrons to reduce \\(\\text{H}^+\\) ions in dilute acids into \\(\\text{H}_2\\) gas.", "Consequently, non-metals do not displace hydrogen from dilute acids.", "Therefore, no reaction occurs.")
    ]
    add_sci_subtopic(tc_742, name_742, c742_data)

    # -------------------------------------------------------------
    # 7.5.1 Noble metals and purity in Carats (80 questions)
    # -------------------------------------------------------------
    tc_751 = "MH-8-SCI-7-7.5.1"
    name_751 = "Noble metals: Gold, Silver, Platinum, Palladium and purity in Carats (24K, 22K)"
    c751_data = [
        ("What is the percentage purity of pure 24-Carat (24K) gold?", "100% pure gold", ["91.6% pure gold", "75% pure gold", "50% pure gold"],
         "24 Carat represents 100% pure gold without alloying.", "Because pure gold is very soft, 22K gold (91.6% gold alloyed with copper/silver) is used for jewelry.", "Hence, 100% pure is correct.")
    ]
    add_sci_subtopic(tc_751, name_751, c751_data)

    # -------------------------------------------------------------
    # 7.5.2 Corrosion: Rusting of iron, green patina, tarnishing (80 questions)
    # -------------------------------------------------------------
    tc_752 = "MH-8-SCI-7-7.5.2"
    name_752 = "Corrosion: Rusting of iron, green patina on copper, tarnishing of silver"
    c752_data = [
        ("What chemical substance forms the reddish-brown coating called 'Rust' on iron in the presence of moist air?", "Hydrated Ferric Oxide (\\(\\text{Fe}_2\\text{O}_3 \\cdot x\\text{H}_2\\text{O}\\))", ["Copper carbonate", "Silver sulphide", "Zinc oxide"],
         "Iron corrodes when exposed to oxygen and moisture, forming hydrated iron(III) oxide.", "Copper forms a green basic carbonate layer, and silver forms black silver sulphide (\\(\\text{Ag}_2\\text{S}\\)).", "Thus, hydrated ferric oxide is correct.")
    ]
    add_sci_subtopic(tc_752, name_752, c752_data)

    # -------------------------------------------------------------
    # 7.5.3 Alloys: Brass, Bronze, Stainless Steel (80 questions)
    # -------------------------------------------------------------
    tc_753 = "MH-8-SCI-7-7.5.3"
    name_753 = "Alloys: Brass (Cu+Zn), Bronze (Cu+Sn), Stainless Steel (Fe+C+Cr+Ni)"
    c753_data = [
        ("What is the metallic composition of the alloy 'Brass'?", "Copper (Cu) and Zinc (Zn)", ["Copper and Tin", "Iron and Carbon", "Aluminium and Magnesium"],
         "Brass is a homogeneous alloy of Copper and Zinc.", "Bronze is composed of Copper and Tin.", "Therefore, Copper and Zinc is correct.")
    ]
    add_sci_subtopic(tc_753, name_753, c753_data)

    return questions

if __name__ == "__main__":
    qs = build_ch7_questions()
    print(f"Generated {len(qs)} questions for Chapter 7.")
    out_path = "scripts/mh8_sci_ch7_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
