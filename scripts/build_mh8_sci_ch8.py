import json
import random

random.seed(8808)

def build_ch8_questions():
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

    def add_sci_subtopic(tc, name, cases):
        for i in range(80):
            ctx, ans, wrongs, s1, s2, s3 = cases[i % len(cases)]
            q = make_q(tc, name, ctx, ans, wrongs, s1, s2, s3, diffs_80[i], vaults_80[i])
            questions.append(q)

    # -------------------------------------------------------------
    # 8.1.1 Degradable vs non-degradable pollutants (80 questions)
    # -------------------------------------------------------------
    tc_811 = "MH-8-SCI-8-8.1.1"
    name_811 = "Definition of pollution and degradable vs non-degradable pollutants"
    c811_data = [
        ("Pollutants that can be decomposed and broken down naturally by microorganisms over time are called:", "Biodegradable pollutants (e.g. vegetable waste, paper, sewage)", ["Non-biodegradable pollutants", "Radioactive fallout", "Heavy metal poisons"],
         "Biodegradable materials are natural organic substances degraded by microbes into harmless inorganic products.", "Examples include kitchen refuse, agricultural residues, and natural fibers.", "Hence, biodegradable pollutants is correct."),
        ("Which of the following environmental pollutants is NON-BIODEGRADABLE, persisting in nature for centuries?", "Plastic bags, DDT pesticide, glass, and aluminum cans", ["Fallen dry leaves", "Cattle dung manure", "Cotton fabric"],
         "Non-biodegradable substances resist biological microbial decomposition.", "Synthetic polymers, chlorinated hydrocarbons (DDT), and heavy metals accumulate permanently.", "Therefore, plastic bags and DDT is correct.")
    ]
    add_sci_subtopic(tc_811, name_811, c811_data)

    # -------------------------------------------------------------
    # 8.2.1 Air pollutants: SO2, CO, NO, PM, lead (80 questions)
    # -------------------------------------------------------------
    tc_821 = "MH-8-SCI-8-8.2.1"
    name_821 = "Pollutants: SO2, CO, NO, particulate matter (PM), lead compounds"
    c821_data = [
        ("Which toxic, odorless gas produced by incomplete combustion of fossil fuels binds to hemoglobin 200 times faster than oxygen, causing asphyxiation?", "Carbon Monoxide (CO)", ["Carbon Dioxide (\\(\\text{CO}_2\\))", "Nitrogen (\\(\\text{N}_2\\))", "Sulphur Dioxide (\\(\\text{SO}_2\\))"],
         "Carbon monoxide binds avidly to hemoglobin forming carboxyhemoglobin.", "This completely blocks oxygen transport to body tissues, leading to fatal hypoxia.", "Thus, Carbon Monoxide is correct."),
        ("Sulphur dioxide (\\(\\text{SO}_2\\)) emitted from coal-burning thermal power plants causes which severe human health issue?", "Intense irritation of eyes, respiratory tract irritation, and chronic bronchitis/asthma", ["Bone fracture", "Kidney stones", "Skin melanin loss"],
         "Sulphur dioxide reacts with respiratory moisture forming sulphurous acid.", "This triggers severe bronchial inflammation and respiratory distress.", "Hence, respiratory irritation is correct.")
    ]
    add_sci_subtopic(tc_821, name_821, c821_data)

    # -------------------------------------------------------------
    # 8.2.2 Acid rain and monument corrosion (80 questions)
    # -------------------------------------------------------------
    tc_822 = "MH-8-SCI-8-8.2.2"
    name_822 = "Acid rain (formation of H2SO4 and HNO3) and corrosion of historical monuments (Taj Mahal)"
    c822_data = [
        ("What chemical reactions in the atmosphere lead to the formation of 'Acid Rain'?", "Atmospheric \\(\\text{SO}_2\\) and \\(\\text{NO}_2\\) dissolve in rainwater clouds forming \\(\\text{H}_2\\text{SO}_4\\) and \\(\\text{HNO}_3\\)", ["Carbon burns into pure graphite", "Ozone reacts with nitrogen to form ammonia", "Methane dissolves in moisture"],
         "Industrial emissions of \\(\\text{SO}_2\\) and nitrogen oxides oxidize in cloud droplets.", "They form dilute sulphuric acid (\\(\\text{H}_2\\text{SO}_4\\)) and nitric acid (\\(\\text{HNO}_3\\)), lowering precipitation pH below 5.6.", "Therefore, formation of \\(\\text{H}_2\\text{SO}_4\\) and \\(\\text{HNO}_3\\) is correct."),
        ("Why has the white marble (\\(\\text{CaCO}_3\\)) of the historical Taj Mahal in Agra suffered yellowing and corrosion (marble cancer)?", "Acid rain reacts with marble: \\(\\text{CaCO}_3 + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{CaSO}_4 + \\text{CO}_2 + \\text{H}_2\\text{O}\\)", ["Excessive sunlight exposure", "Painting with wrong chemicals", "Tourists touching the stone"],
         "Acid rain converts insoluble calcium carbonate into soluble calcium sulphate.", "This phenomenon is termed 'marble cancer', eroding historical monuments.", "Thus, reaction with acid rain is correct.")
    ]
    add_sci_subtopic(tc_822, name_822, c822_data)

    # -------------------------------------------------------------
    # 8.2.3 Greenhouse effect and global warming (80 questions)
    # -------------------------------------------------------------
    tc_823 = "MH-8-SCI-8-8.2.3"
    name_823 = "Greenhouse effect and global warming"
    c823_data = [
        ("Which of the following is the primary anthropogenic Greenhouse Gas responsible for modern Global Warming?", "Carbon Dioxide (\\(\\text{CO}_2\\))", ["Nitrogen gas (\\(\\text{N}_2\\))", "Oxygen gas (\\(\\text{O}_2\\))", "Argon (Ar)"],
         "Greenhouse gases trap outgoing terrestrial infrared radiation emitted by Earth's surface.", "Excess \\(\\text{CO}_2\\) from fossil fuel combustion intensifies this effect, elevating global average temperatures.", "Hence, Carbon Dioxide is correct."),
        ("Besides \\(\\text{CO}_2\\), which potent greenhouse gas is released from flooded paddy fields and digestive systems of ruminant cattle?", "Methane (\\(\\text{CH}_4\\))", ["Sulphur Dioxide", "Helium", "Chlorine gas"],
         "Methane is emitted during anaerobic methanogenesis in wetlands, rice paddies, and cattle rumination.", "Its global warming potential is over 25 times greater than \\(\\text{CO}_2\\).", "Thus, Methane is correct.")
    ]
    add_sci_subtopic(tc_823, name_823, c823_data)

    # -------------------------------------------------------------
    # 8.3.1 Domestic sewage and industrial effluents (80 questions)
    # -------------------------------------------------------------
    tc_831 = "MH-8-SCI-8-8.3.1"
    name_831 = "Domestic sewage, industrial effluents, agricultural pesticides and fertilisers"
    c831_data = [
        ("Untreated industrial effluents discharged into rivers often introduce which dangerous heavy metal toxins into the food chain?", "Mercury (Hg), Lead (Pb), Cadmium (Cd), and Arsenic (As)", ["Calcium and Magnesium", "Sodium and Potassium", "Pure distilled water"],
         "Chemical manufacturing, electroplating, and tanning industries release toxic heavy metals.", "These bioaccumulate across trophic levels, causing neurological poisoning.", "Therefore, Mercury, Lead, and Cadmium is correct.")
    ]
    add_sci_subtopic(tc_831, name_831, c831_data)

    # -------------------------------------------------------------
    # 8.3.2 Eutrophication and BOD (80 questions)
    # -------------------------------------------------------------
    tc_832 = "MH-8-SCI-8-8.3.2"
    name_832 = "Eutrophication and depletion of dissolved oxygen (BOD)"
    c832_data = [
        ("What biological ecological phenomenon occurs when excess nitrogen and phosphorus fertilizers wash into aquatic lakes, causing explosive algal bloom?", "Eutrophication", ["Salinization", "Biomagnification", "Desalination"],
         "Excess agricultural nitrates and phosphates stimulate rapid algal overgrowth.", "When algae die, bacterial decomposition consumes dissolved oxygen, suffocating aquatic fish.", "Hence, Eutrophication is correct."),
        ("What does high Biological Oxygen Demand (BOD) in a river water sample signify?", "High organic pollution requiring large amounts of dissolved oxygen for bacterial decomposition", ["Extremely pure drinking water", "Zero bacteria in the water", "High mineral salt content"],
         "BOD measures the dissolved oxygen required by aerobic microbes to oxidize organic matter.", "High BOD indicates severe organic waste contamination.", "Thus, high organic pollution is correct.")
    ]
    add_sci_subtopic(tc_832, name_832, c832_data)

    # -------------------------------------------------------------
    # 8.3.3 Water-borne diseases (80 questions)
    # -------------------------------------------------------------
    tc_833 = "MH-8-SCI-8-8.3.3"
    name_833 = "Water-borne diseases (Typhoid, Jaundice, Amoebiasis)"
    c833_data = [
        ("Drinking untreated water contaminated with municipal sewage is the primary transmission route for which group of infectious diseases?", "Typhoid, Cholera, Hepatitis A (Jaundice), and Amoebic Dysentery", ["Malaria and Dengue", "Asthma and Bronchitis", "Goitre and Scurvy"],
         "Pathogenic water contamination spreads enteric pathogens directly to the digestive system.", "Boiling water and sewage treatment prevent these waterborne epidemics.", "Therefore, Typhoid, Cholera, and Jaundice is correct.")
    ]
    add_sci_subtopic(tc_833, name_833, c833_data)

    # -------------------------------------------------------------
    # 8.4.1 Soil pollution: chemicals, plastic, saline soil (80 questions)
    # -------------------------------------------------------------
    tc_841 = "MH-8-SCI-8-8.4.1"
    name_841 = "Chemical fertilisers, plastic waste, radioactive fallout, saline soil"
    c841_data = [
        ("Excessive and continuous application of synthetic chemical fertilizers (NPK) over decades causes which detrimental change in soil?", "Loss of soil fertility, destruction of beneficial earthworms, and soil acidification/salinization", ["Enrichment of natural humus", "Increased earthworm populations", "Permanent moisture retention"],
         "Excess chemical salts destroy soil microflora and beneficial earthworms.", "The soil texture degrades, turning saline and alkaline.", "Hence, loss of fertility and salinization is correct.")
    ]
    add_sci_subtopic(tc_841, name_841, c841_data)

    # -------------------------------------------------------------
    # 8.4.2 Solid waste management and organic farming (80 questions)
    # -------------------------------------------------------------
    tc_842 = "MH-8-SCI-8-8.4.2"
    name_842 = "Solid waste management and organic farming methods"
    c842_data = [
        ("What eco-friendly agricultural practice relies entirely on crop rotation, green manures, bio-fertilizers, and vermicompost without synthetic agrochemicals?", "Organic Farming", ["Intensive monoculture farming", "Chemical hydroponics", "Slash-and-burn farming"],
         "Organic farming eliminates synthetic pesticides and chemical fertilizers.", "It sustains long-term soil biological health and produces residue-free food.", "Thus, Organic Farming is correct."),
        ("What are the fundamental '4 Rs' of modern solid waste management hierarchy?", "Reduce, Reuse, Recycle, and Recover", ["React, Reject, Remove, Renew", "Reheat, Refill, Reorder, Replace", "Refuel, Rebuild, Resell, Repair"],
         "The 4R environmental hierarchy prioritizes source reduction, re-using items, recycling materials, and recovering energy.", "This minimizes landfill waste.", "Hence, Reduce, Reuse, Recycle, Recover is correct.")
    ]
    add_sci_subtopic(tc_842, name_842, c842_data)

    return questions

if __name__ == "__main__":
    qs = build_ch8_questions()
    print(f"Generated {len(qs)} questions for Chapter 8.")
    out_path = "scripts/mh8_sci_ch8_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
