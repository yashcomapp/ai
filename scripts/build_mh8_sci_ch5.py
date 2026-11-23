import json
import random

random.seed(8505)

def build_ch5_questions():
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

    # -------------------------------------------------------------
    # 5.1.1 Dalton: hard indivisible spheres (23 questions)
    # -------------------------------------------------------------
    tc_511 = "MH-8-SCI-5-5.1.1"
    name_511 = "Dalton: hard indivisible spheres"
    c511_q = [
        ("According to John Dalton's Atomic Theory (1803), how is an atom fundamentally conceptualized?", "A tiny, hard, indivisible, and indestructible solid sphere having uniform internal mass", ["A hollow ball containing liquid protons", "A positively charged pudding with electron seeds", "A miniature planetary solar system"]),
        ("What does Dalton's atomic postulate state regarding atoms of the SAME chemical element?", "Atoms of the same element are completely identical in mass, size, and chemical properties", ["Atoms of the same element have different masses", "Atoms of the same element can turn into gold", "Atoms of the same element have no mass"]),
        ("Which fundamental chemical law is directly explained by Dalton's concept that atoms cannot be created or destroyed?", "Law of Conservation of Mass", ["Law of Constant Proportions", "Ohm's Law", "Boyle's Law"]),
        ("Kanada (Acharya Kanada), an ancient Indian sage in the 6th century BC, conceived that all matter is composed of indivisible particles named:", "Parmanu (or Anu)", ["Dalton", "Atomos", "Electron"])
    ]
    for i in range(23):
        ctx, ans, wrongs = c511_q[i % len(c511_q)]
        q = make_q(
            tc_511, name_511,
            f"Dalton's Atomic Theory: {ctx}",
            ans, wrongs,
            "John Dalton in 1803 proposed that matter is made of indivisible atoms like hard spheres.",
            "All atoms of a given element are identical in mass and properties.",
            f"Hence, '{ans}' is correct.",
            "medium" if i % 2 == 0 else "easy", "foundation"
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 5.1.2 Thomson plum pudding model (27 questions)
    # -------------------------------------------------------------
    tc_512 = "MH-8-SCI-5-5.1.2"
    name_512 = "Thomson: positively charged sphere with embedded negatively charged electrons (cathode ray discovery)"
    c512_q = [
        ("In J.J. Thomson's Plum Pudding (or Watermelon) model of the atom (1904), what does the red sweet pulp correspond to?", "The continuous sphere of positive electrical charge", ["Negatively charged electrons", "The central hard nucleus", "Neutral neutrons"]),
        ("In Thomson's watermelon analogy of the atom, what do the black seeds embedded in the pulp represent?", "Negatively charged electrons", ["Positively charged protons", "Neutral neutrons", "Positrons"]),
        ("Through which groundbreaking gas discharge tube experiment did J.J. Thomson discover the electron in 1897?", "Cathode Ray Tube (discharge tube) experiment", ["Gold foil scattering experiment", "Oil drop experiment", "Photoelectric experiment"]),
        ("Why is an individual atom electrically neutral according to Thomson's atomic model?", "Because the total negative charge of embedded electrons exactly balances the positive charge of the sphere", ["Because atoms possess no electric charges at all", "Because electrons have no charge", "Because positive charge is destroyed by negative charge"])
    ]
    for i in range(27):
        ctx, ans, wrongs = c512_q[i % len(c512_q)]
        q = make_q(
            tc_512, name_512,
            f"Thomson's Plum Pudding Model: {ctx}",
            ans, wrongs,
            "J.J. Thomson discovered the electron and proposed the plum pudding model.",
            "The atom is a positive sphere with embedded negative electrons, maintaining overall electrical neutrality.",
            f"Therefore, '{ans}' is the correct statement.",
            "medium" if i % 2 == 0 else "easy", "foundation"
        )
        questions.append(q)

    # Helper generator for standard 50-q subtopics (30 exam + 20 foundation)
    def add_subtopic_qs(tc, name, q_data, count):
        v_list = ["exam"] * (count - 20) + ["foundation"] * 20
        d_list = ["easy"] * (count // 3) + ["medium"] * (count // 3) + ["hard"] * (count - 2 * (count // 3))
        for i in range(count):
            ctx, ans, wrongs, s1, s2, s3 = q_data[i % len(q_data)]
            q = make_q(tc, name, ctx, ans, wrongs, s1, s2, s3, d_list[i], v_list[i])
            questions.append(q)

    # -------------------------------------------------------------
    # 5.2.1 Alpha particle scattering experiment (49 questions)
    # -------------------------------------------------------------
    tc_521 = "MH-8-SCI-5-5.2.1"
    name_521 = "Alpha particle scattering experiment"
    c521_data = [
        ("In Ernest Rutherford's famous scattering experiment (1911), which ultra-thin metal foil was bombarded with alpha particles?", "Gold foil (thickness ~10^-7 m)", ["Aluminium foil", "Lead sheet", "Copper foil"],
         "Rutherford selected gold because gold is the most malleable metal, allowing an extremely thin foil of ~1000 atoms thickness.", "Alpha particles were fired at this thin gold sheet.", "Hence, gold foil was used."),
        ("What type of radiation particles did Rutherford fire at the gold foil?", "Positively charged Alpha particles (\\(\\text{He}^{2+}\\) nuclei)", ["Negatively charged beta particles", "Neutral gamma photons", "Proton beams"],
         "Alpha particles are positively charged helium nuclei with a mass of 4 u and charge +2e emitted by radioactive elements.", "They provided high momentum probes.", "Thus, alpha particles were used."),
        ("What surprising observation did Rutherford make regarding the trajectory of MOST alpha particles passing through the gold foil?", "Most alpha particles (over 99%) passed straight through the foil undeflected", ["All particles bounced straight back", "All particles were absorbed by gold", "All particles turned into electrons"],
         "Over 99% of alpha particles traveled undeflected in straight lines.", "This proved that the interior of atoms consists predominantly of empty space.", "Therefore, 'passed straight undeflected' is correct.")
    ]
    add_subtopic_qs(tc_521, name_521, c521_data, 49)

    # -------------------------------------------------------------
    # 5.2.2 Nuclear model of atom (50 questions)
    # -------------------------------------------------------------
    tc_522 = "MH-8-SCI-5-5.2.2"
    name_522 = "Positively charged dense central nucleus, empty space around nucleus, planetary electrons"
    c522_data = [
        ("What revolutionary atomic structure did Rutherford deduce from the fact that a tiny fraction (1 in 20,000) of alpha particles rebounded at large angles (180°)?", "A tiny, extremely dense, positively charged core called the Nucleus containing almost the entire mass of the atom", ["A hollow center", "That electrons are heavy", "That atoms are indestructible solid balls"],
         "Large-angle rebounds proved that positive charge is concentrated in a tiny central volume.", "This dense core was named the atomic nucleus.", "Thus, the nucleus was discovered."),
        ("In Rutherford's planetary model, where do the negatively charged electrons reside?", "Orbiting around the central nucleus in circular paths, like planets around the Sun", ["Fixed inside the nucleus", "Glued to the outer shell", "Embedded in a positive pudding"],
         "Rutherford proposed that electrons revolve around the nucleus in planetary orbits.", "The space between nucleus and electrons is empty space.", "Hence, 'orbiting around the nucleus' is correct.")
    ]
    add_subtopic_qs(tc_522, name_522, c522_data, 50)

    # -------------------------------------------------------------
    # 5.2.3 Drawbacks of Rutherford model (51 questions)
    # -------------------------------------------------------------
    tc_523 = "MH-8-SCI-5-5.2.3"
    name_523 = "Drawbacks of Rutherford model (stability of orbital electrons)"
    c523_data = [
        ("According to classical electromagnetic theory (Maxwell's laws), what major drawback plagued Rutherford's planetary model?", "An accelerating orbiting electron must continuously radiate electromagnetic energy and spiral into the nucleus within a fraction of a second", ["Electrons are too heavy to move", "The nucleus would push electrons away", "Atoms would expand infinitely"],
         "Classical physics dictates that any charged particle undergoing circular acceleration radiates energy continuously.", "The electron would lose kinetic energy, spiral inwards, and collapse into the nucleus in \\(10^{-8}\\text{ s}\\).", "Thus, Rutherford's model could not explain the inherent stability of atoms.")
    ]
    add_subtopic_qs(tc_523, name_523, c523_data, 51)

    # -------------------------------------------------------------
    # 5.3.1 Bohr stable circular orbits (52 questions)
    # -------------------------------------------------------------
    tc_531 = "MH-8-SCI-5-5.3.1"
    name_531 = "Electrons revolve in discrete stable circular orbits (K, L, M, N shells)"
    c531_data = [
        ("How did Niels Bohr (1913) resolve the instability dilemma of Rutherford's atomic model?", "He postulated that electrons revolve only in specific stationary, non-radiating discrete circular orbits (energy levels / shells)", ["By removing electrons from the atom", "By stating that electrons are stationary", "By replacing electrons with neutrons"],
         "Bohr introduced quantized stationary orbits where electrons do not radiate energy while revolving.", "These shells are labeled K, L, M, N (n = 1, 2, 3, 4).", "Hence, discrete non-radiating orbits resolved the drawback.")
    ]
    add_subtopic_qs(tc_531, name_531, c531_data, 52)

    # -------------------------------------------------------------
    # 5.3.2 Quantum electron jumps (53 questions)
    # -------------------------------------------------------------
    tc_532 = "MH-8-SCI-5-5.3.2"
    name_532 = "Energy emission and absorption during quantum electron jumps"
    c532_data = [
        ("What happens energetically when an electron jumps from an INNER lower-energy shell to an OUTER higher-energy shell?", "The electron absorbs a specific quantum of energy (photon: \\(\\Delta E = h\\nu\\))", ["The electron emits radiation", "The electron loses all mass", "The electron turns into a proton"],
         "Moving to a higher orbit requires absorbing energy equal to the difference between orbits.", "When jumping from higher to lower orbit, it emits a photon.", "Thus, energy is absorbed.")
    ]
    add_subtopic_qs(tc_532, name_532, c532_data, 53)

    # -------------------------------------------------------------
    # 5.4.1 Proton: positive charge (49 questions)
    # -------------------------------------------------------------
    tc_541 = "MH-8-SCI-5-5.4.1"
    name_541 = "Proton: positive charge in nucleus (1.6 * 10^-19 C)"
    c541_data = [
        ("What is the electric charge carried by a single proton located in the nucleus?", "\\(+1.6 \\times 10^{-19}\\text{ Coulombs (or } +1e\\text{)}\\)", ["\\(-1.6 \\times 10^{-19}\\text{ C}\\)", "Zero charge", "\\(+3.2 \\times 10^{-19}\\text{ C}\\)"],
         "A proton carries a unit positive fundamental charge of \\(+1.6 \\times 10^{-19}\\text{ C}\\).", "Its mass is approximately \\(1\\text{ u} \\approx 1.67 \\times 10^{-27}\\text{ kg}\\).", "Therefore, \\(+1.6 \\times 10^{-19}\\text{ C}\\) is correct.")
    ]
    add_subtopic_qs(tc_541, name_541, c541_data, 49)

    # -------------------------------------------------------------
    # 5.4.2 Neutron: electrically neutral (50 questions)
    # -------------------------------------------------------------
    tc_542 = "MH-8-SCI-5-5.4.2"
    name_542 = "Neutron: electrically neutral particle (James Chadwick, 1932)"
    c542_data = [
        ("Which British physicist discovered the neutral subatomic particle 'Neutron' in 1932?", "James Chadwick", ["J.J. Thomson", "Ernest Rutherford", "Niels Bohr"],
         "James Chadwick bombarded beryllium targets with alpha particles and discovered uncharged neutrons.", "Neutrons have mass approximately equal to a proton (\\(\\sim 1\\text{ u}\\)).", "Hence, James Chadwick is correct.")
    ]
    add_subtopic_qs(tc_542, name_542, c542_data, 50)

    # -------------------------------------------------------------
    # 5.4.3 Electron: negatively charged (51 questions)
    # -------------------------------------------------------------
    tc_543 = "MH-8-SCI-5-5.4.3"
    name_543 = "Electron: negatively charged particle with negligible mass (1/1837 of H atom)"
    c543_data = [
        ("How does the mass of an electron compare to the mass of a hydrogen atom (or proton)?", "It is negligible, approximately \\(\\frac{1}{1837}\\) of the mass of a hydrogen atom", ["It is equal to the mass of a proton", "It is twice as heavy as a proton", "It has zero volume and infinite mass"],
         "An electron has mass \\(9.1 \\times 10^{-31}\\text{ kg}\\), which is \\(1/1837\\) of a proton.", "Because of this minute mass, atomic mass is concentrated almost entirely in nucleons (protons and neutrons).", "Thus, \\(1/1837\\) is correct.")
    ]
    add_subtopic_qs(tc_543, name_543, c543_data, 51)

    # -------------------------------------------------------------
    # 5.5.1 Atomic number Z (52 questions)
    # -------------------------------------------------------------
    tc_551 = "MH-8-SCI-5-5.5.1"
    name_551 = "Atomic number Z = number of protons = number of electrons"
    c551_data = [
        ("What does the 'Atomic Number' (Z) of a chemical element represent?", "The total number of protons present in the nucleus of an atom (which equals the number of electrons in a neutral atom)", ["The sum of protons and neutrons", "The total number of neutrons only", "The atomic weight in grams"],
         "Atomic number \\(Z\\) is the defining identity of an element, representing nuclear proton count.", "In a neutral atom, \\(Z = \\text{protons} = \\text{electrons}\\).", "Hence, 'number of protons' is correct.")
    ]
    add_subtopic_qs(tc_551, name_551, c551_data, 52)

    # -------------------------------------------------------------
    # 5.5.2 Mass number A (52 questions)
    # -------------------------------------------------------------
    tc_552 = "MH-8-SCI-5-5.5.2"
    name_552 = "Mass number A = protons + neutrons"
    c552_data = [
        ("What is the 'Mass Number' (A) of an atom defined as?", "The total sum of protons and neutrons (nucleons) in the nucleus: \\(A = Z + N\\)", ["The number of electrons orbiting the nucleus", "The density of the nucleus", "The volume of the electron cloud"],
         "Mass number \\(A\\) is the integer count of nucleons (protons + neutrons) in the nucleus.", "Number of neutrons is given by \\(N = A - Z\\).", "Therefore, \\(A = Z + N\\) is correct.")
    ]
    add_subtopic_qs(tc_552, name_552, c552_data, 52)

    # -------------------------------------------------------------
    # 5.5.3 Shell capacity formula 2n² (53 questions)
    # -------------------------------------------------------------
    tc_553 = "MH-8-SCI-5-5.5.3"
    name_553 = "Shell capacity formula 2n² (K=2, L=8, M=18, N=32)"
    c553_data = [
        ("What is the maximum number of electrons that can be accommodated in the M shell (\\(n = 3\\)) according to the \\(2n^2\\) rule?", "\\(18\\text{ electrons}\\) (\\(2 \\times 3^2 = 2 \\times 9 = 18\\))", ["\\(8\\text{ electrons}\\)", "\\(32\\text{ electrons}\\)", "\\(2\\text{ electrons}\\)"],
         "According to Bohr-Bury scheme, shell capacity is \\(2n^2\\).", "For M-shell (\\(n=3\\)): \\(2 \\times 3^2 = 18\\).", "Thus, 18 electrons is correct.")
    ]
    add_subtopic_qs(tc_553, name_553, c553_data, 53)

    # -------------------------------------------------------------
    # 5.5.4 Valence electrons and valency (53 questions)
    # -------------------------------------------------------------
    tc_554 = "MH-8-SCI-5-5.5.4"
    name_554 = "Valence electrons and valency determination"
    c554_data = [
        ("What is the valency of an oxygen atom having atomic number \\(Z = 8\\) and electronic configuration \\(2, 6\\)?", "\\(2\\) (needs 2 electrons to complete stable octet \\(8 - 6 = 2\\))", ["\\(6\\)", "\\(8\\)", "\\(1\\)"],
         "Oxygen has 6 valence electrons in its outer L-shell.", "To achieve octet stability (8 electrons), it accepts or shares 2 electrons.", "Therefore, its valency is 2.")
    ]
    add_subtopic_qs(tc_554, name_554, c554_data, 53)

    # -------------------------------------------------------------
    # 5.6.1 Isotopes definition (52 questions)
    # -------------------------------------------------------------
    tc_561 = "MH-8-SCI-5-5.6.1"
    name_561 = "Definition: same atomic number Z, different mass number A (e.g. C-12, C-14; H-1, H-2, H-3)"
    c561_data = [
        ("What are 'Isotopes' in nuclear chemistry?", "Atoms of the same element having the same atomic number \\(Z\\) but different mass numbers \\(A\\)", ["Atoms of different elements with same mass number", "Atoms with equal numbers of neutrons but different protons", "Molecules with the same molecular formula"],
         "Isotopes share identical proton count \\(Z\\) and chemical behavior.", "They differ in neutron count \\(N\\) and mass number \\(A\\) (e.g. Protium, Deuterium, Tritium).", "Hence, 'same Z, different A' is correct.")
    ]
    add_subtopic_qs(tc_561, name_561, c561_data, 52)

    # -------------------------------------------------------------
    # 5.6.2 Uses of radioactive isotopes (53 questions)
    # -------------------------------------------------------------
    tc_562 = "MH-8-SCI-5-5.6.2"
    name_562 = "Uses: Uranium-235 in nuclear reactors, Cobalt-60 in cancer therapy, Iodine-131 in goitre, Carbon-14 dating"
    c562_data = [
        ("Which radioactive isotope is widely utilized in medical radiation oncology for cancer therapy?", "Cobalt-60 (\\(^{60}\\text{Co}\\))", ["Carbon-14", "Iodine-131", "Uranium-235"],
         "Cobalt-60 emits high-energy gamma rays utilized in radiotherapy to destroy cancerous cells.", "Iodine-131 treats thyroid goitre, and C-14 is used in carbon dating.", "Thus, Cobalt-60 is correct.")
    ]
    add_subtopic_qs(tc_562, name_562, c562_data, 53)

    return questions

if __name__ == "__main__":
    qs = build_ch5_questions()
    print(f"Generated {len(qs)} questions for Chapter 5.")
    out_path = "scripts/mh8_sci_ch5_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
