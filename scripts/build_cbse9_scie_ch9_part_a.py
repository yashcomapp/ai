import json
import math

def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        "Unbalanced chemical stoichiometry",
        "Passive thermodynamic stagnation",
        "Spontaneous non-stoichiometric dissociation"
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
            q_doc = {
                "questionCode": q_code,
                "text": q_text,
                "options": final_options,
                "correctAnswer": correct_letter,
                "difficulty": diff,
                "marks": 4,
                "negativeMarks": 1,
                "vault": vault,
                "topicCode": topic_code,
                "subtopic": topic_code,
                "chapterNumber": 9,
                "class": "9",
                "subjectCode": "SCIE",
                "boardCode": "CBSE",
                "type": "OSC",
                "solution": solution,
                "status": "approved"
            }
            questions.append(q_doc)
            q_seq += 1

    return questions

# ==============================================================================
# SUBTOPIC 9.1.1: Law of Conservation of Mass (Lavoisier)
# ==============================================================================
def gen_9_1_1():
    archs = []

    # Arch 1: Historical formulation & definition of Law of Conservation of Mass
    archs.append({
        'templates': [
            "Who established the Law of Conservation of Mass through meticulous quantitative chemical experiments in 1774?",
            "What fundamental statement defines the Law of Conservation of Mass?",
            "According to the Law of Conservation of Mass, during any physical or chemical change:",
            "Which of the following statements precisely reflects the Law of Conservation of Mass established by Antoine Lavoisier?"
        ],
        'data': [
            ("Antoine Lavoisier", "Mass can neither be created nor destroyed in a chemical reaction", "John Dalton; Joseph Proust; J.J. Thomson"),
            ("Antoine Lavoisier", "Total mass of reactants equals total mass of products in a closed system", "Robert Boyle; Amedeo Avogadro; Ernest Rutherford"),
            ("Antoine Lavoisier", "The mass of a closed system must remain constant over time", "Dmitri Mendeleev; Niels Bohr; James Chadwick"),
            ("Antoine Lavoisier", "In any chemical reaction, total initial mass of reactants is strictly conserved", "Henry Moseley; Louis Pasteur; Michael Faraday")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1:** The Law of Conservation of Mass was established by French chemist Antoine Laurent Lavoisier in 1774.\\n\\n**Step 2:** The law states that mass can neither be created nor destroyed in a chemical reaction.\\n\\n**Step 3:** This means that the total mass of the products formed in a chemical reaction must be strictly equal to the total mass of the reactants consumed. Correct answer is '{item[1]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Numerical calculations: Reactant A + Reactant B -> Product C + Product D
    archs.append({
        'templates': [
            "In a chemical reaction, {} g of sodium carbonate reacts completely with {} g of ethanoic acid to produce {} g of carbon dioxide, {} g of water, and x g of sodium ethanoate. What is the value of x according to the Law of Conservation of Mass?",
            "When {} g of substance A reacts with {} g of substance B, {} g of product C and y g of product D are formed. Calculate y:",
            "According to the Law of Conservation of Mass, if {} g of X reacts with {} g of Y to form {} g of Z and a gaseous byproduct W, what is the mass of W?",
            "During a chemical reaction between {} g of calcium carbonate and {} g of hydrochloric acid, {} g of calcium chloride and {} g of water are produced along with carbon dioxide. Find the mass of carbon dioxide released:"
        ],
        'data': [
            (5.3, 6.0, 2.2, 0.9, 8.2),
            (10.0, 15.0, 12.5, 0.0, 12.5),
            (4.2, 10.0, 8.4, 0.0, 5.8),
            (12.0, 18.0, 15.0, 0.0, 15.0),
            (5.0, 8.0, 6.5, 0.0, 6.5),
            (7.5, 12.5, 11.0, 0.0, 9.0),
            (20.0, 30.0, 26.0, 0.0, 24.0),
            (15.0, 25.0, 22.0, 0.0, 18.0)
        ],
        'calc': lambda item: (
            f"{item[4]} g",
            split_options(f"{round(item[4] * 1.5, 1)} g; {round(item[4] * 0.5, 1)} g; {round(item[4] + 4.0, 1)} g"),
            f"**Step 1:** According to the Law of Conservation of Mass: \\(\\text{{Total mass of reactants}} = \\text{{Total mass of products}}\\).\\n\\n**Step 2:** Sum of reactants = \\({item[0]} + {item[1]} = {round(item[0] + item[1], 1)}\\text{{ g}}\\).\\n\\n**Step 3:** Sum of known products = \\({item[2]} + {item[3]} = {round(item[2] + item[3], 1)}\\text{{ g}}\\). Unknown mass = \\({round(item[0] + item[1], 1)} - {round(item[2] + item[3], 1)} = {item[4]}\\text{{ g}}\\). Correct answer is {item[4]} g."
        ),
        'diff': 'medium'
    })

    # Arch 3: Precipitation reaction in conical flask (Barium Chloride + Sodium Sulfate)
    archs.append({
        'templates': [
            "In an experiment to verify the Law of Conservation of Mass, an ignition tube containing barium chloride solution is suspended in a conical flask containing sodium sulfate solution. Why is the flask tightly corked before and after mixing?",
            "What happens to the total mass of the system when barium chloride solution is mixed with sodium sulfate solution in a sealed conical flask?",
            "A white precipitate of barium sulfate is formed when solutions of barium chloride and sodium sulfate are mixed. The mass of the flask and contents before mixing was 152.4 g. What will be the mass after mixing?",
            "When sodium sulfate reacts with barium chloride in a sealed container to form insoluble barium sulfate and sodium chloride solution, the balance reading:"
        ],
        'data': [
            ("To prevent any exchange of matter (gases/vapors) between the flask and surroundings", "To increase atmospheric pressure inside the flask; To accelerate the formation of white precipitate; To prevent light from entering the flask"),
            ("Total mass remains completely unchanged", "Total mass increases due to formation of solid precipitate; Total mass decreases because of heat generation; Mass becomes zero"),
            ("152.4 g", "150.0 g; 155.0 g; 160.2 g"),
            ("remains exactly the same", "increases by 10%; decreases due to precipitation; fluctuates randomly")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In a chemical reaction taking place in a closed container, matter cannot enter or leave the system.\\n\\n**Step 2:** In the reaction \\(\\text{{BaCl}}_2\\text{{(aq)}} + \\text{{Na}}_2\\text{{SO}}_4\\text{{(aq)}} \\to \\text{{BaSO}}_4\\text{{(s)}} + 2\\text{{NaCl(aq)}}\\), precipitation occurs but no atoms are lost.\\n\\n**Step 3:** The total mass before mixing is strictly equal to the total mass after mixing. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 4: Thermal decomposition of Calcium Carbonate
    archs.append({
        'templates': [
            "When {} g of calcium carbonate is heated strongly in a closed container, it decomposes completely into calcium oxide and carbon dioxide. If {} g of calcium oxide is obtained, what is the mass of carbon dioxide produced?",
            "On heating {} g of CaCO3, {} g of quicklime (CaO) is formed. Calculate the mass of CO2 gas released according to the conservation of mass:",
            "In a closed vessel, {} g of calcium carbonate decomposes into quicklime and carbon dioxide. If {} g of carbon dioxide is generated, find the mass of calcium oxide:",
            "Strong heating of {} g of limestone produces {} g of solid residue. What mass of gaseous carbon dioxide escaped?"
        ],
        'data': [
            (100.0, 56.0, 44.0),
            (50.0, 28.0, 22.0),
            (25.0, 14.0, 11.0),
            (200.0, 112.0, 88.0),
            (10.0, 5.6, 4.4),
            (75.0, 42.0, 33.0),
            (150.0, 84.0, 66.0),
            (20.0, 11.2, 8.8)
        ],
        'calc': lambda item: (
            f"{item[2]} g",
            split_options(f"{round(item[2] * 1.5, 1)} g; {round(item[2] * 0.5, 1)} g; {round(item[2] + 10.0, 1)} g"),
            f"**Step 1:** Chemical equation: \\(\\text{{CaCO}}_3 \\to \\text{{CaO}} + \\text{{CO}}_2\\).\\n\\n**Step 2:** According to the Law of Conservation of Mass: \\(\\text{{Mass of CaCO}}_3 = \\text{{Mass of CaO}} + \\text{{Mass of CO}}_2\\).\\n\\n**Step 3:** \\(\\text{{Mass of CO}}_2 = {item[0]} - {item[1]} = {item[2]}\\text{{ g}}\\). Correct answer is {item[2]} g."
        ),
        'diff': 'medium'
    })

    # Arch 5: Combustion in open vs closed containers
    archs.append({
        'templates': [
            "When a piece of magnesium ribbon is burnt in an open crucible, the mass of the white ash (magnesium oxide) formed is greater than the initial mass of the magnesium. Why does this NOT violate the Law of Conservation of Mass?",
            "Burning a candle in an open container shows an apparent decrease in mass. How is the Law of Conservation of Mass verified in this case?",
            "When wood burns in an open fireplace, only light ash remains. Why does the mass of ash appear much smaller than the original wood?",
            "An apparent increase or decrease in mass during a chemical reaction conducted in an OPEN vessel occurs because:"
        ],
        'data': [
            ("Because oxygen from atmospheric air combined with magnesium; when the mass of oxygen is included, total mass is conserved", "Because magnesium gains neutrons from the flame; Because the crucible absorbs heat mass; Because energy converts into mass"),
            ("By carrying out the combustion in a closed container and weighing the carbon dioxide and water vapor produced", "By cooling the candle to absolute zero; By subtracting the weight of melted wax; By ignoring the gaseous products"),
            ("Because gaseous products (carbon dioxide and water vapor) escape into the atmosphere unnoticed", "Because matter is destroyed into heat energy; Because wood contains zero mass initially; Because carbon atoms vanish upon heating"),
            ("gaseous reactants are absorbed from, or gaseous products escape into, the surroundings", "the Law of Conservation of Mass fails for combustion; mass is destroyed into light photons; gravity fluctuates during heating")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In open vessels, gaseous reactants (like atmospheric oxygen) may enter the reaction, or gaseous products (like \\(\\text{{CO}}_2\\) and steam) may escape into the atmosphere.\\n\\n**Step 2:** When all reactants (including atmospheric oxygen) and all products (including gases) are weighed in a closed system, total mass before reaction equals total mass after reaction.\\n\\n**Step 3:** Correct scientific explanation is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 6: Physical changes and mass conservation
    archs.append({
        'templates': [
            "If {} g of ice cubes at 0 °C melt completely into liquid water in a closed container, what is the mass of the water formed?",
            "When {} g of sucrose (sugar) is completely dissolved in {} g of pure water in a beaker, what is the total mass of the resulting sugar solution?",
            "During the physical dissolution of {} g of common salt (NaCl) in {} g of water, the mass of the brine solution formed is:",
            "A sealed flask containing {} g of liquid water is frozen into solid ice. What is the mass of the ice formed?"
        ],
        'data': [
            (50.0, 50.0, "50.0 g", "45.0 g; 55.0 g; 48.0 g"),
            (15.0, 100.0, "115.0 g", "100.0 g; 85.0 g; 120.0 g"),
            (25.0, 150.0, "175.0 g", "150.0 g; 125.0 g; 180.0 g"),
            (100.0, 100.0, "100.0 g", "90.0 g; 110.0 g; 95.0 g"),
            (20.0, 80.0, "100.0 g", "80.0 g; 60.0 g; 120.0 g"),
            (10.0, 90.0, "100.0 g", "90.0 g; 80.0 g; 110.0 g"),
            (30.0, 200.0, "230.0 g", "200.0 g; 170.0 g; 240.0 g"),
            (40.0, 160.0, "200.0 g", "160.0 g; 120.0 g; 210.0 g")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1:** The Law of Conservation of Mass applies to both chemical reactions and physical changes.\\n\\n**Step 2:** In dissolution: \\(\\text{{Mass of solution}} = \\text{{Mass of solute}} + \\text{{Mass of solvent}}\\). In phase changes: mass does not change upon melting or freezing.\\n\\n**Step 3:** The resulting mass is {item[2]}."
        ),
        'diff': 'easy'
    })

    # Arch 7: Atomic-level basis of conservation of mass (Dalton connection)
    archs.append({
        'templates': [
            "How did John Dalton explain the Law of Conservation of Mass in terms of his atomic theory?",
            "Which postulate of Dalton's atomic theory provides the theoretical foundation for the Law of Conservation of Mass?",
            "At the atomic level, why does the total mass of matter remain unchanged during a chemical reaction?",
            "A chemical reaction involves only the rearrangement of atoms. What does this imply about the conservation of mass?"
        ],
        'data': [
            ("Atoms are indivisible particles that cannot be created or destroyed in a chemical reaction", "Atoms expand in size during a reaction; Atoms lose mass to create energy; Electrons combine to form new protons"),
            ("Atoms are indivisible particles, which cannot be created or destroyed in a chemical reaction", "All atoms of a given element have identical mass; Atoms combine in the ratio of small whole numbers; Elements consist of tiny particles called atoms"),
            ("Because the number and types of atoms remain identical before and after the reaction; only their bonds rearrange", "Because atoms transform into lighter isotopes; Because chemical bonds have infinite mass; Because nuclear forces double in strength"),
            ("Since no atoms are created or lost, the total mass must remain strictly conserved", "Mass changes depending on reaction speed; Mass is lost as light energy; Reactant atoms are converted into pure energy")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Dalton's atomic theory provided the scientific rationale for the empirical laws of chemical combination.\\n\\n**Step 2:** Dalton postulated that atoms are indivisible particles that cannot be created or destroyed in a chemical reaction.\\n\\n**Step 3:** During a reaction, atoms merely dissociate from reactant molecules and recombine to form product molecules; since the number and identities of atoms are unchanged, total mass is conserved. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 8: Advanced conservation calculation with unreacted excess
    archs.append({
        'templates': [
            "In a reaction, {} g of reactant A is mixed with {} g of reactant B. If {} g of product C is formed and {} g of reactant B remains unreacted, does this data verify the Law of Conservation of Mass?",
            "A mixture of {} g of hydrogen and {} g of oxygen is ignited. If {} g of water is formed and {} g of oxygen remains unreacted, what is the total mass of the system after the reaction?",
            "When {} g of solid reactant decomposes to give {} g of product X and {} g of product Y, what is the percentage recovery of mass?",
            "Heating {} g of a substance yields {} g of solid residue and {} g of gas. What is the total mass of products?"
        ],
        'data': [
            (10.0, 20.0, 25.0, 5.0, "Yes, because mass of reacted substances (10 g + 15 g) equals product mass (25 g)", "No, because product mass is 25 g instead of 30 g; No, because reactant B disappeared; Yes, but only in vacuum"),
            (4.0, 40.0, 36.0, 8.0, "44.0 g (36 g water + 8 g unreacted oxygen = 44 g total)", "36.0 g; 40.0 g; 48.0 g"),
            (50.0, 28.0, 22.0, 0.0, "100% (50 g products from 50 g reactant)", "90%; 85%; 95%"),
            (80.0, 52.0, 28.0, 0.0, "80.0 g (52 g + 28 g = 80 g)", "75.0 g; 85.0 g; 70.0 g")
        ],
        'calc': lambda item: (
            item[4],
            split_options(item[5]),
            f"**Step 1:** In any reaction system: \\(\\text{{Initial Mass}} = \\text{{Final Mass}}\\).\\n\\n**Step 2:** Final mass includes the mass of products formed plus any unreacted excess reactants.\\n\\n**Step 3:** \\(\\text{{Total final mass}} = \\text{{Products}} + \\text{{Unreacted reactant}}\\). This strictly conforms to the Law of Conservation of Mass. Correct answer is '{item[4]}'."
        ),
        'diff': 'hard'
    })

    return generate_vault_questions('CBSE-9-SCIE-9-9.1.1', 'Law of Conservation of Mass (Lavoisier)', archs)

# ==============================================================================
# SUBTOPIC 9.1.2: Law of Constant Proportions (Proust)
# ==============================================================================
def gen_9_1_2():
    archs = []

    # Arch 1: Historical formulation & definition of Law of Constant Proportions
    archs.append({
        'templates': [
            "Who formulated the Law of Constant Proportions (also known as the Law of Definite Proportions) in 1799?",
            "What is the definition of the Law of Constant Proportions?",
            "According to the Law of Definite Proportions, in a chemical compound:",
            "Which statement correctly expresses the Law of Constant Proportions stated by Joseph Proust?"
        ],
        'data': [
            ("Joseph Proust", "In a chemical substance, the elements are always present in definite proportions by mass", "Antoine Lavoisier; John Dalton; J.J. Thomson"),
            ("Joseph Proust", "A pure chemical compound always contains exactly the same proportion of elements by mass regardless of its source", "Dmitri Mendeleev; Robert Boyle; Amedeo Avogadro"),
            ("Joseph Proust", "The ratio of elements by mass is fixed and independent of the method of preparation", "Henry Moseley; Ernest Rutherford; Niels Bohr"),
            ("Joseph Proust", "In any pure compound, constituent elements are combined in a constant ratio by mass", "James Chadwick; Michael Faraday; Louis Pasteur")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1:** The Law of Constant Proportions was stated by French chemist Joseph Louis Proust in 1799.\\n\\n**Step 2:** The law states: 'In a chemical substance, the elements are always present in definite proportions by mass.'\\n\\n**Step 3:** This means that regardless of where a pure compound is obtained from or how it is prepared, its constituent elements always exist in the same fixed proportion by mass. Correct statement is '{item[1]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Water (H2O) ratio 1:8 calculations
    archs.append({
        'templates': [
            "In pure water (H2O), hydrogen and oxygen are always present in the ratio of {} by mass. What mass of oxygen gas is required to react completely with {} g of hydrogen gas?",
            "According to the 1:8 mass ratio in water, if {} g of hydrogen is combined with excess oxygen, what mass of water is formed?",
            "How much oxygen will react completely with {} g of hydrogen to produce pure water?",
            "To form pure water, {} g of hydrogen requires what mass of oxygen according to the Law of Definite Proportions?"
        ],
        'data': [
            ("1:8", 1.0, 8.0, 9.0),
            ("1:8", 2.0, 16.0, 18.0),
            ("1:8", 3.0, 24.0, 27.0),
            ("1:8", 4.0, 32.0, 36.0),
            ("1:8", 5.0, 40.0, 45.0),
            ("1:8", 6.0, 48.0, 54.0),
            ("1:8", 8.0, 64.0, 72.0),
            ("1:8", 10.0, 80.0, 90.0)
        ],
        'calc': lambda item: (
            f"{item[2]} g of oxygen",
            split_options(f"{round(item[2] * 1.5, 1)} g of oxygen; {round(item[2] * 0.5, 1)} g of oxygen; {round(item[2] + 6.0, 1)} g of oxygen"),
            f"**Step 1:** In water (\\(\\text{{H}}_2\\text{{O}}\\)), the mass ratio of Hydrogen to Oxygen is \\(2 \\times 1 : 16 = 2:16 = 1:8\\).\\n\\n**Step 2:** For every 1 g of Hydrogen, exactly 8 g of Oxygen is required.\\n\\n**Step 3:** For {item[1]} g of Hydrogen: \\(\\text{{Mass of oxygen}} = {item[1]} \\times 8 = {item[2]}\\text{{ g}}\\). Total mass of water formed = \\({item[1]} + {item[2]} = {item[3]}\\text{{ g}}\\). Correct answer is {item[2]} g of oxygen."
        ),
        'diff': 'easy'
    })

    # Arch 3: Ammonia (NH3) ratio 14:3 calculations
    archs.append({
        'templates': [
            "In ammonia (NH3), nitrogen and hydrogen are always present in the ratio of {} by mass. What mass of hydrogen is needed to react completely with {} g of nitrogen?",
            "According to the Law of Constant Proportions, what mass of ammonia is produced when {} g of nitrogen reacts with sufficient hydrogen?",
            "Given that ammonia has a nitrogen:hydrogen mass ratio of 14:3, calculate the mass of nitrogen required to combine with {} g of hydrogen:",
            "How many grams of ammonia will be formed when {} g of nitrogen reacts completely with {} g of hydrogen?"
        ],
        'data': [
            ("14:3", 14.0, 3.0, 17.0),
            ("14:3", 28.0, 6.0, 34.0),
            ("14:3", 42.0, 9.0, 51.0),
            ("14:3", 56.0, 12.0, 68.0),
            ("14:3", 70.0, 15.0, 85.0),
            ("14:3", 84.0, 18.0, 102.0)
        ],
        'calc': lambda item: (
            f"{item[2]} g of hydrogen",
            split_options(f"{round(item[2] * 2.0, 1)} g of hydrogen; {round(item[2] * 0.5, 1)} g of hydrogen; {round(item[2] + 4.0, 1)} g of hydrogen"),
            f"**Step 1:** In ammonia (\\(\\text{{NH}}_3\\)), the mass ratio of Nitrogen to Hydrogen is \\(14 : 3 \\times 1 = 14:3\\).\\n\\n**Step 2:** For {item[1]} g of Nitrogen: \\(\\text{{Hydrogen mass}} = {item[1]} \\times \\frac{{3}}{{14}} = {item[2]}\\text{{ g}}\\).\\n\\n**Step 3:** Total mass of ammonia produced = \\({item[1]} + {item[2]} = {item[3]}\\text{{ g}}\\). Correct answer is {item[2]} g of hydrogen."
        ),
        'diff': 'medium'
    })

    # Arch 4: Carbon Dioxide (CO2) ratio 3:8 with limiting reagent
    archs.append({
        'templates': [
            "In carbon dioxide (CO2), carbon and oxygen combine in the fixed ratio of {} by mass. When {} g of carbon is burnt in {} g of oxygen, what mass of CO2 is produced, and what mass of oxygen remains unreacted?",
            "If {} g of carbon is heated with {} g of oxygen, how much carbon dioxide will be formed according to the Law of Definite Proportions?",
            "What mass of carbon dioxide is formed when {} g of carbon is burnt in {} g of oxygen?",
            "When {} g of carbon is reacted with {} g of oxygen in a closed vessel, the mass of CO2 formed is:"
        ],
        'data': [
            ("3:8", 3.0, 50.0, 11.0, 42.0),
            ("3:8", 6.0, 50.0, 22.0, 34.0),
            ("3:8", 9.0, 50.0, 33.0, 26.0),
            ("3:8", 12.0, 50.0, 44.0, 18.0),
            ("3:8", 3.0, 8.0, 11.0, 0.0),
            ("3:8", 6.0, 16.0, 22.0, 0.0)
        ],
        'calc': lambda item: (
            f"{item[3]} g of CO2",
            split_options(f"{round(item[3] * 1.5, 1)} g of CO2; {round(item[3] * 0.5, 1)} g of CO2; {round(item[3] + 8.0, 1)} g of CO2"),
            f"**Step 1:** In \\(\\text{{CO}}_2\\), the mass ratio of Carbon to Oxygen is \\(12 : 2 \\times 16 = 12:32 = 3:8\\).\\n\\n**Step 2:** 3 g of carbon reacts with exactly 8 g of oxygen to produce 11 g of \\(\\text{{CO}}_2\\).\\n\\n**Step 3:** For {item[1]} g of carbon, the oxygen required is \\({item[1]} \\times \\frac{{8}}{{3}} = {round(item[1] * 8 / 3, 1)}\\text{{ g}}\\). The mass of \\(\\text{{CO}}_2\\) formed is {item[3]} g (with {item[4]} g oxygen remaining unreacted). Correct answer is {item[3]} g of CO2."
        ),
        'diff': 'hard'
    })

    # Arch 5: Copper Oxide samples prepared by different methods (Proust's classic experiment)
    archs.append({
        'templates': [
            "In one experiment, 1.375 g of copper oxide yielded 1.098 g of copper on reduction. In another experiment, 1.178 g of copper produced 1.476 g of copper oxide. Which chemical law is illustrated by these results?",
            "Two different samples of cupric oxide were analyzed: Sample A contained 79.9% copper and 20.1% oxygen; Sample B contained 79.9% copper and 20.1% oxygen. This data confirms:",
            "Whether copper carbonate is decomposed thermally or copper is reacted directly with nitric acid and ignited, the resulting copper oxide always contains copper and oxygen in the same ratio. This demonstrates:",
            "A compound analyzed from synthetic and natural sources showed identical percentage composition of constituent elements. This proves:"
        ],
        'data': [
            ("Law of Constant Proportions (Law of Definite Proportions)", "Law of Conservation of Mass; Law of Multiple Proportions; Law of Reciprocal Proportions"),
            ("Law of Definite Proportions", "Law of Conservation of Energy; Dalton's Law of Partial Pressures; Gay-Lussac's Law of Gaseous Volumes"),
            ("Law of Constant Proportions", "Avogadro's Hypothesis; Graham's Law of Diffusion; Boyle's Law"),
            ("Law of Constant Proportions", "Law of Mass Action; Le Chatelier's Principle; Hess's Law")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In Proust's classic experiment with synthetic and natural cupric carbonate (and copper oxide), the percentage by mass of copper and oxygen was found to be identical in both samples (~79.9% Cu and 20.1% O).\\n\\n**Step 2:** This established that regardless of source or method of preparation, the ratio by mass of constituent elements in a chemical compound is always fixed.\\n\\n**Step 3:** This confirms the Law of Constant Proportions. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 6: Calcium Oxide (CaO) ratio 5:2 calculations
    archs.append({
        'templates': [
            "In calcium oxide (CaO), calcium and oxygen combine in the ratio of {} by mass. What mass of oxygen will react completely with {} g of calcium?",
            "According to the 5:2 mass ratio in quicklime (CaO), what mass of calcium oxide is formed when {} g of calcium reacts with sufficient oxygen?",
            "What mass of calcium is required to combine with {} g of oxygen to form calcium oxide?",
            "When {} g of calcium reacts with {} g of oxygen, what is the mass of CaO formed?"
        ],
        'data': [
            ("5:2", 20.0, 8.0, 28.0),
            ("5:2", 10.0, 4.0, 14.0),
            ("5:2", 25.0, 10.0, 35.0),
            ("5:2", 40.0, 16.0, 56.0),
            ("5:2", 50.0, 20.0, 70.0),
            ("5:2", 5.0, 2.0, 7.0)
        ],
        'calc': lambda item: (
            f"{item[2]} g of oxygen",
            split_options(f"{round(item[2] * 2.0, 1)} g of oxygen; {round(item[2] * 0.5, 1)} g of oxygen; {round(item[2] + 5.0, 1)} g of oxygen"),
            f"**Step 1:** In \\(\\text{{CaO}}\\), atomic mass of Ca = 40 u and O = 16 u. Ratio by mass = \\(40 : 16 = 5:2\\).\\n\\n**Step 2:** For {item[1]} g of calcium: \\(\\text{{Mass of oxygen}} = {item[1]} \\times \\frac{{2}}{{5}} = {item[2]}\\text{{ g}}\\).\\n\\n**Step 3:** Total mass of \\(\\text{{CaO}}\\) formed = \\({item[1]} + {item[2]} = {item[3]}\\text{{ g}}\\). Correct answer is {item[2]} g of oxygen."
        ),
        'diff': 'medium'
    })

    # Arch 7: Sulfur Dioxide (SO2) ratio 1:1 calculations
    archs.append({
        'templates': [
            "In sulfur dioxide (SO2), sulfur and oxygen combine in the ratio of {} by mass. What mass of oxygen is required to react completely with {} g of sulfur?",
            "Given that sulfur and oxygen combine in a 1:1 mass ratio in SO2, what mass of sulfur dioxide is formed from {} g of sulfur?",
            "If {} g of sulfur is burnt in {} g of oxygen, what is the mass of SO2 produced?",
            "To produce SO2, {} g of sulfur requires what mass of oxygen according to the Law of Definite Proportions?"
        ],
        'data': [
            ("1:1", 16.0, 16.0, 32.0),
            ("1:1", 32.0, 32.0, 64.0),
            ("1:1", 8.0, 8.0, 16.0),
            ("1:1", 64.0, 64.0, 128.0),
            ("1:1", 4.0, 4.0, 8.0),
            ("1:1", 20.0, 20.0, 40.0)
        ],
        'calc': lambda item: (
            f"{item[2]} g of oxygen",
            split_options(f"{round(item[2] * 1.5, 1)} g of oxygen; {round(item[2] * 0.5, 1)} g of oxygen; {round(item[2] + 6.0, 1)} g of oxygen"),
            f"**Step 1:** In \\(\\text{{SO}}_2\\), atomic mass of S = 32 u and 2 O = 32 u. The mass ratio is \\(32 : 32 = 1:1\\).\\n\\n**Step 2:** For {item[1]} g of sulfur, exactly {item[2]} g of oxygen is required.\\n\\n**Step 3:** Total mass of \\(\\text{{SO}}_2\\) formed = \\({item[1]} + {item[2]} = {item[3]}\\text{{ g}}\\). Correct answer is {item[2]} g of oxygen."
        ),
        'diff': 'easy'
    })

    # Arch 8: Dalton's explanation of Proust's Law
    archs.append({
        'templates': [
            "Which postulate of Dalton's atomic theory provides the theoretical foundation for the Law of Constant Proportions?",
            "How does Dalton's atomic theory explain why a compound always contains elements in a fixed ratio by mass?",
            "The fact that a given compound always contains the same elements in a fixed ratio of small whole numbers of atoms directly explains:",
            "Dalton's postulate stating that 'the relative number and kinds of atoms are constant in a given compound' explains:"
        ],
        'data': [
            ("The relative number and kinds of atoms are constant in a given compound", "Atoms are indivisible particles that cannot be created or destroyed; Atoms of the same element have identical mass; Atoms of different elements have different masses"),
            ("Because atoms of different elements have fixed characteristic masses and combine in fixed whole-number ratios to form compound molecules", "Because electrons have negligible mass compared to nucleons; Because chemical bonds have constant length; Because all elements have identical valencies"),
            ("The Law of Constant Proportions", "The Law of Conservation of Energy; Avogadro's Hypothesis; Boyle's Law"),
            ("The Law of Constant Proportions (Law of Definite Proportions)", "The Law of Conservation of Mass; The Law of Multiple Proportions; The Periodic Law")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Dalton postulated that in any given compound, the relative number and kinds of atoms are strictly constant.\\n\\n**Step 2:** Since each type of atom possesses a characteristic, fixed atomic mass, a fixed numerical ratio of atoms in a molecule inevitably produces a constant ratio of elements by mass.\\n\\n**Step 3:** This postulate successfully explained Proust's Law of Constant Proportions. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-9-9.1.2', 'Law of Constant Proportions (Proust)', archs)

# ==============================================================================
# SUBTOPIC 9.2.1: Postulates of Dalton atomic theory
# ==============================================================================
def gen_9_2_1():
    archs = []

    # Arch 1: Postulates of Dalton's atomic theory
    archs.append({
        'templates': [
            "Which of the following is a core postulate of John Dalton's atomic theory published in 1808?",
            "According to Dalton's atomic theory, what is matter composed of?",
            "Which statement represents an authentic postulate of Dalton's atomic theory?",
            "What did John Dalton propose regarding atoms of a given chemical element?"
        ],
        'data': [
            ("All matter is made of very tiny particles called atoms, which participate in chemical reactions", "Atoms consist of a central positive nucleus surrounded by orbiting electrons; Atoms can be split into subatomic particles by chemical means; Atoms of the same element can have different masses"),
            ("Atoms are indivisible particles, which cannot be created or destroyed in a chemical reaction", "Atoms are hollow spheres containing free protons; Atoms constantly radiate energy; All atoms are identical regardless of the element"),
            ("Atoms of a given element are identical in mass and chemical properties", "Atoms combine in continuously variable proportions; Compounds contain fractional numbers of atoms; Elements are formed by fusion of hydrogen atoms"),
            ("Atoms combine in the ratio of small whole numbers to form compounds", "Atoms disintegrate spontaneously during chemical bonding; Mass of an atom is concentrated in electron orbitals; Valency is independent of atomic structure")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In 1808, British chemist John Dalton presented his atomic theory in 'A New System of Chemical Philosophy'.\\n\\n**Step 2:** Key postulates include: (1) Matter consists of indivisible atoms, (2) Atoms cannot be created or destroyed, (3) Atoms of an element are identical in mass and properties, (4) Atoms of different elements differ in mass and properties, (5) Atoms combine in small whole numbers to form compounds, (6) Relative number and kinds of atoms are constant in a compound.\\n\\n**Step 3:** Correct postulate is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Modern modifications / limitations of Dalton's theory
    archs.append({
        'templates': [
            "Which discovery in modern physics disproved Dalton's postulate that atoms are indivisible?",
            "Dalton's postulate that 'atoms of the same element are identical in all respects, including mass' was modified following the discovery of:",
            "The discovery of which phenomenon proved that atoms of different elements CAN have the same mass number, contrary to Dalton's theory?",
            "Which modern discovery showed that Dalton's assumption of indivisibility of the atom is incorrect?"
        ],
        'data': [
            ("The discovery of subatomic particles (electrons, protons, and neutrons)", "The discovery of noble gases; The discovery of electrolysis; The invention of the electron microscope"),
            ("Isotopes (atoms of the same element having different mass numbers, e.g., ³⁵Cl and ³⁷Cl)", "Isobars; Allotropes; Polyatomic ions"),
            ("Isobars (atoms of different elements having the same mass number, e.g., ⁴⁰Ar and ⁴⁰Ca)", "Isotopes; Isomers; Radioactivity"),
            ("The discovery of electrons, protons, and neutrons demonstrating atomic divisibility", "The discovery of chemical valency; The synthesis of synthetic dyes; The discovery of Avogadro's constant")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Dalton considered atoms to be indivisible and indestructible.\\n\\n**Step 2:** Modern discoveries revealed that: (1) Atoms are divisible into subatomic particles (p, e, n), (2) Isotopes exist (atoms of same element with different masses), and (3) Isobars exist (atoms of different elements with same mass).\\n\\n**Step 3:** Correct modification is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 3: Ancient Indian and Greek philosophical concepts of atom
    archs.append({
        'templates': [
            "Which ancient Indian philosopher postulated around 500 BC that if we go on dividing matter (Padarth), we shall get smaller particles, and ultimately a stage will come when we shall come across the smallest particles that cannot be divided further, which he named 'Parmanu'?",
            "Which Indian philosopher elaborated on Maharishi Kanad's concepts and stated that these indivisible particles (Parmanu) normally exist in a combined form which gives us various forms of matter?",
            "Around the same era, which ancient Greek philosophers suggested that if we go on dividing matter, a stage will come when particles obtained cannot be divided further and called these indivisible particles 'atoms' (meaning indivisible)?",
            "What did the ancient Greek term 'atomos' coined by Democritus literally mean?"
        ],
        'data': [
            ("Maharishi Kanad", "Aryabhata; Charaka; Sushruta"),
            ("Pakudha Katyayama", "Varahamihira; Brahmagupta; Nagarjuna"),
            ("Democritus and Leucippus", "Aristotle and Plato; Socrates and Pythagoras; Archimedes and Euclid"),
            ("Indivisible or uncuttable", "Invisible; Infinitesimal; Inactive")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Around 500 BC, Indian philosopher Maharishi Kanad postulated that dividing matter (Padarth) leads to the smallest indivisible particle, which he termed 'Parmanu'.\\n\\n**Step 2:** Another Indian philosopher, Pakudha Katyayama, explained that Parmanu normally exist in combined states (molecules) giving diverse forms of matter.\\n\\n**Step 3:** Greek philosophers Democritus and Leucippus called them 'atomos', meaning uncuttable or indivisible. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 4: Atomic size and scale of atomic radius (nanometres)
    archs.append({
        'templates': [
            "Atomic radius is measured in which SI unit of length?",
            "How many metres are in one nanometre (1 nm)?",
            "What is the approximate order of magnitude of the radius of a hydrogen atom?",
            "Which of the following correctly pairs an entity with its approximate size (radius in metres)?"
        ],
        'data': [
            ("Nanometres (nm)", "Picometres only; Micrometres; Millimetres"),
            ("10⁻⁹ m (1 nm = 10⁻⁹ m)", "10⁻⁶ m; 10⁻¹² m; 10⁻¹⁵ m"),
            ("10⁻¹⁰ m (0.1 nm)", "10⁻⁶ m; 10⁻¹⁵ m; 10⁻³ m"),
            ("Molecule of water: ~10⁻⁹ m (1 nm)", "Atom of hydrogen: 10⁻³ m; Molecule of hemoglobin: 10⁻² m; Grain of sand: 10⁻¹² m")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Atoms are exceedingly small; their radii are measured on the nanoscale in nanometres (nm).\\n\\n**Step 2:** \\(1\\text{{ nm}} = 10^{{-9}}\\text{{ m}}\\), or \\(1\\text{{ m}} = 10^9\\text{{ nm}}\\).\\n\\n**Step 3:** The radius of a hydrogen atom (the smallest atom) is \\(\\approx 10^{{-10}}\\text{{ m}}\\), and a water molecule is \\(\\approx 10^{{-9}}\\text{{ m}}\\). Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 5: IUPAC symbols of elements (Berzelius convention)
    archs.append({
        'templates': [
            "Which scientist proposed that the symbols of elements should be made from one or two letters of the name of the element?",
            "What is the IUPAC rule for writing the symbol of an element consisting of two letters?",
            "What is the Latin name from which the chemical symbol for {} ({}) is derived?",
            "Match the chemical symbol of the element with its Latin name:"
        ],
        'data': [
            ("J.J. Berzelius", "Antoine Lavoisier; John Dalton; Robert Boyle"),
            ("The first letter is always capitalized (uppercase) and the second letter is always lowercase", "Both letters are capitalized; Both letters are lowercase; The first is lowercase and the second is uppercase"),
            ("Sodium", "Na", "Natrium", "Stibium; Kalium; Ferrum"),
            ("Potassium", "K", "Kalium", "Natrium; Plumbum; Cuprum"),
            ("Iron", "Fe", "Ferrum", "Argentum; Aurum; Stannum"),
            ("Copper", "Cu", "Cuprum", "Hydrargyrum; Kalium; Wolfram"),
            ("Gold", "Au", "Aurum", "Argentum; Plumbum; Ferrum"),
            ("Silver", "Ag", "Argentum", "Aurum; Stannum; Natrium"),
            ("Lead", "Pb", "Plumbum", "Plutonium; Phosphorus; Potassium")
        ],
        'calc': lambda item: (
            item[2] if len(item) == 4 else item[0],
            split_options(item[3] if len(item) == 4 else item[1]),
            f"**Step 1:** J.J. Berzelius suggested that symbols of elements be derived from one or two letters of their English, Latin, German, or Greek names.\\n\\n**Step 2:** The first letter is always capitalized, and the second letter (if present) is always lowercase (e.g., Cobalt is Co, not CO which is carbon monoxide).\\n\\n**Step 3:** Correct answer is '{item[2] if len(item) == 4 else item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 6: Definition and standard of unified atomic mass unit (u)
    archs.append({
        'templates': [
            "In 1961, which isotope was internationally chosen as the standard reference for measuring atomic masses?",
            "How is one unified atomic mass unit (1 u) precisely defined?",
            "Before adopting carbon-12 in 1961, which element was initially used as the reference standard (1/16 of its atom) for atomic mass?",
            "One unified atomic mass unit (1 u) is equivalent to:"
        ],
        'data': [
            ("Carbon-12 isotope (¹²C)", "Carbon-14; Oxygen-16; Hydrogen-1"),
            ("Exactly 1/12th of the mass of one atom of carbon-12", "The mass of one hydrogen atom; 1/16th the mass of oxygen-16; The mass of one proton"),
            ("Oxygen (natural oxygen, 1/16th of its atomic mass)", "Nitrogen; Helium; Chlorine"),
            ("1/12 the mass of a single carbon-12 atom (approximately 1.6605 × 10⁻²⁷ kg)", "The mass of 1 mole of carbon atoms; The mass of 12 carbon atoms; Exactly 1 gram")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In 1961, the International Union of Pure and Applied Chemistry (IUPAC) adopted the carbon-12 isotope as the universally accepted atomic mass standard.\\n\\n**Step 2:** One unified atomic mass unit (symbol 'u', formerly 'amu') is defined as a mass unit equal to exactly \\(\\frac{{1}}{{12}}\\text{{th}}\\) of the mass of one atom of carbon-12.\\n\\n**Step 3:** The relative atomic mass of all elements is determined with respect to this standard. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 7: Atomic mass values of common elements
    archs.append({
        'templates': [
            "What is the atomic mass of {} (in unified atomic mass units, u)?",
            "According to the IUPAC scale, the atomic mass of {} is:",
            "An atom of {} has an atomic mass of:",
            "Which of the following correctly states the atomic mass of {}?"
        ],
        'data': [
            ("Hydrogen", "1 u", "2 u; 4 u; 12 u"),
            ("Carbon", "12 u", "6 u; 14 u; 24 u"),
            ("Nitrogen", "14 u", "7 u; 16 u; 28 u"),
            ("Oxygen", "16 u", "8 u; 12 u; 32 u"),
            ("Sodium", "23 u", "11 u; 24 u; 46 u"),
            ("Magnesium", "24 u", "12 u; 23 u; 48 u"),
            ("Sulfur", "32 u", "16 u; 28 u; 64 u"),
            ("Chlorine", "35.5 u", "17 u; 35 u; 37 u"),
            ("Calcium", "40 u", "20 u; 39 u; 42 u")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1:** Relative atomic mass is the average mass of an atom of the element relative to \\(\\frac{{1}}{{12}}\\text{{th}}\\) the mass of one carbon-12 atom.\\n\\n**Step 2:** For {item[0]}, the accepted relative atomic mass on the periodic scale is {item[1]}.\\n\\n**Step 3:** Correct atomic mass is {item[1]}."
        ),
        'diff': 'easy'
    })

    # Arch 8: Dalton's symbols of elements
    archs.append({
        'templates': [
            "How did John Dalton originally represent different chemical elements before Berzelius's alphabetical notation was adopted?",
            "What was the distinctive feature of Dalton's symbolic notation for elements?",
            "Why was Dalton's geometric pictorial notation replaced by Berzelius's letter-based system?",
            "In Dalton's system of chemical symbols, each symbol represented:"
        ],
        'data': [
            ("He used specific geometric circle drawings with internal dots, crosses, or shadings", "He used Roman numerals; He used Chinese logograms; He used Latin letters"),
            ("Each symbol was a circle with unique internal markings representing one atom of the element", "Symbols were three-dimensional models; Symbols were based on atomic weights; Symbols were color-coded liquid drops"),
            ("Because geometric pictorial symbols were difficult to draw, print, and memorize for complex chemical formulas", "Because Dalton's symbols were copyrighted; Because circles could not represent gases; Because symbols were scientifically incorrect"),
            ("not only the element but also definite one atom of that element", "one mole of gas; the volume of the element; the density of the compound")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** John Dalton was the first scientist to use specific symbols for elements; his symbols were circles containing dots (Hydrogen), a cross (Sulfur), shading (Carbon), etc.\\n\\n**Step 2:** When Dalton used a symbol, it signified not only the element but also exactly one atom of that element.\\n\\n**Step 3:** Because drawing these pictorial symbols was cumbersome, J.J. Berzelius introduced the modern letter-based system. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-9-9.2.1', 'Postulates of Dalton atomic theory', archs)

# ==============================================================================
# SUBTOPIC 9.2.2: Molecules of elements and compounds
# ==============================================================================
def gen_9_2_2():
    archs = []

    # Arch 1: Definition of a molecule
    archs.append({
        'templates': [
            "What is the definition of a molecule?",
            "How does a molecule differ fundamentally from an individual isolated atom?",
            "Which statement correctly characterizes a molecule?",
            "A molecule is defined as:"
        ],
        'data': [
            ("The smallest particle of an element or compound capable of independent existence and showing all properties of that substance", "A particle with net electric charge; A nucleus without electrons; An indivisible fundamental particle like a quark"),
            ("A molecule can exist independently under ordinary conditions, whereas single atoms of most elements cannot", "A molecule always carries an electric charge; A molecule has no mass; A molecule cannot be broken down by chemical means"),
            ("A group of two or more atoms chemically bonded together by attractive forces", "A mixture of physically stirred elements; An unstable cluster of protons; A collection of electrons orbiting empty space"),
            ("the smallest particle of a substance that retains its chemical properties and can exist freely", "the largest unit of matter visible to the naked eye; a single proton; a state of matter formed at absolute zero")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** A molecule is in general a group of two or more atoms that are chemically bonded together by attractive forces.\\n\\n**Step 2:** It can be defined as the smallest particle of an element or a compound that is capable of an independent existence and shows all the properties of that substance.\\n\\n**Step 3:** Atoms of most elements are reactive and cannot exist independently; they combine to form molecules or ions. Correct statement is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Atomicity of elements (monoatomic, diatomic, triatomic, polyatomic)
    archs.append({
        'templates': [
            "What is meant by the atomicity of an element?",
            "What is the atomicity of the noble gas {} ({})?",
            "What is the atomicity of {} ({})?",
            "Which of the following elements is {}?"
        ],
        'data': [
            ("The number of atoms constituting a molecule of an element", "The total number of protons in an atom; The valency of the element; The mass of one molecule in grams"),
            ("Helium", "He", "Monoatomic (atomicity = 1)", "Diatomic; Triatomic; Polyatomic"),
            ("Argon", "Ar", "Monoatomic (atomicity = 1)", "Diatomic; Tetra-atomic; Polyatomic"),
            ("Oxygen", "O2", "Diatomic (atomicity = 2)", "Monoatomic; Triatomic; Polyatomic"),
            ("Nitrogen", "N2", "Diatomic (atomicity = 2)", "Monoatomic; Triatomic; Tetra-atomic"),
            ("Hydrogen", "H2", "Diatomic (atomicity = 2)", "Monoatomic; Triatomic; Polyatomic"),
            ("Chlorine", "Cl2", "Diatomic (atomicity = 2)", "Monoatomic; Triatomic; Tetra-atomic"),
            ("Ozone", "O3", "Triatomic (atomicity = 3)", "Monoatomic; Diatomic; Polyatomic"),
            ("Phosphorus", "P4", "Tetra-atomic (atomicity = 4)", "Monoatomic; Diatomic; Triatomic"),
            ("Sulfur", "S8", "Polyatomic (octa-atomic, atomicity = 8)", "Monoatomic; Diatomic; Triatomic")
        ],
        'calc': lambda item: (
            item[2] if len(item) == 4 else item[0],
            split_options(item[3] if len(item) == 4 else item[1]),
            f"**Step 1:** Atomicity is defined as the number of atoms constituting a single molecule of an element.\\n\\n**Step 2:** Noble gases (He, Ne, Ar) consist of single atoms: monoatomic (1). Gases like \\(\\text{{H}}_2, \\text{{O}}_2, \\text{{N}}_2, \\text{{Cl}}_2\\) are diatomic (2). Ozone (\\(\\text{{O}}_3\\)) is triatomic (3). Phosphorus (\\(\\text{{P}}_4\\)) is tetra-atomic (4), and sulfur (\\(\\text{{S}}_8\\)) is polyatomic (8).\\n\\n**Step 3:** Correct atomicity is '{item[2] if len(item) == 4 else item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Molecules of elements vs molecules of compounds (homoatomic vs heteroatomic)
    archs.append({
        'templates': [
            "Molecules of elements are termed homoatomic while molecules of compounds are heteroatomic. Which of the following is a heteroatomic molecule?",
            "Which of the following represents a molecule of an ELEMENT rather than a compound?",
            "What is the fundamental structural difference between a molecule of an element and a molecule of a compound?",
            "Classify the following species: Cl2, CO2, P4, NH3. Which pair represents molecules of compounds?"
        ],
        'data': [
            ("Methane (CH4)", "Oxygen (O2); Ozone (O3); Phosphorus (P4)"),
            ("Water (H2O)", "Nitrogen (N2); Chlorine (Cl2); Sulfur (S8)"),
            ("Carbon dioxide (CO2)", "Hydrogen (H2); Argon (Ar); Ozone (O3)"),
            ("Sulfur (S8)", "Sulfur dioxide (SO2); Water (H2O); Ammonia (NH3)"),
            ("A molecule of an element contains only one kind of atom, whereas a molecule of a compound contains two or more different kinds of atoms", "Molecules of elements are always gases while compounds are always solids; Molecules of elements have no mass; Molecules of compounds have electric charges"),
            ("CO2 and NH3", "Cl2 and P4; Cl2 and CO2; P4 and NH3")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Molecules of elements consist of identical atoms of the same chemical element chemically bonded together (homoatomic, e.g. \\(\\text{{O}}_2, \\text{{P}}_4, \\text{{S}}_8\\)).\\n\\n**Step 2:** Molecules of compounds consist of atoms of two or more different elements combined chemically in a fixed proportion (heteroatomic, e.g. \\(\\text{{H}}_2\\text{{O}}, \\text{{CO}}_2, \\text{{CH}}_4\\)).\\n\\n**Step 3:** Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 4: Ratio by mass and ratio by number of atoms in common compounds
    archs.append({
        'templates': [
            "In water (H2O), the ratio by mass of combining elements is 1:8 (H:O). What is the ratio by NUMBER of atoms (H:O)?",
            "In ammonia (NH3), the ratio by mass is 14:3 (N:H). What is the ratio by NUMBER of atoms (N:H)?",
            "In carbon dioxide (CO2), the ratio by mass is 3:8 (C:O). What is the ratio by NUMBER of atoms (C:O)?",
            "In carbon monoxide (CO), what are the ratio by mass and ratio by number of atoms (C:O) respectively?"
        ],
        'data': [
            ("2:1", "1:2; 1:8; 8:1"),
            ("1:3", "3:1; 14:3; 3:14"),
            ("1:2", "2:1; 3:8; 8:3"),
            ("3:4 by mass and 1:1 by number of atoms", "3:8 by mass and 1:2 by number; 1:1 by mass and 3:4 by number; 12:16 by mass and 2:1 by number")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The chemical formula gives the exact number of atoms of each element in a molecule.\\n\\n**Step 2:** For example, in \\(\\text{{H}}_2\\text{{O}}\\), there are 2 atoms of Hydrogen and 1 atom of Oxygen, giving an atomic ratio of 2:1.\\n\\n**Step 3:** Mass ratio is obtained by multiplying atomic ratio by relative atomic masses: \\(2 \\times 1 : 1 \\times 16 = 2:16 = 1:8\\). Correct ratio by number of atoms is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 5: Simple ions (cations vs anions)
    archs.append({
        'templates': [
            "What is an ion, and what are negatively and positively charged ions termed respectively?",
            "Which of the following is a CATION?",
            "Which of the following is an ANION?",
            "When a neutral sodium atom (Na) loses one electron to achieve an octet, what species does it form?"
        ],
        'data': [
            ("An ion is a charged atom or group of atoms; negatively charged is an anion, positively charged is a cation", "Negatively charged is cation, positively charged is anion; Ions are always neutral; Ions have zero mass"),
            ("Sodium ion (Na⁺)", "Chloride ion (Cl⁻); Oxide ion (O²⁻); Sulfide ion (S²⁻)"),
            ("Magnesium ion (Mg²⁺)", "Nitride ion (N³⁻); Fluoride ion (F⁻); Bromide ion (Br⁻)"),
            ("Chloride ion (Cl⁻)", "Calcium ion (Ca²⁺); Aluminium ion (Al³⁺); Potassium ion (K⁺)"),
            ("A sodium cation with +1 charge (Na⁺)", "A sodium anion with -1 charge; A sodium molecule (Na2); A neutron")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** An ion is an atom or group of atoms that carries a net electric charge.\\n\\n**Step 2:** A positively charged ion is called a cation (formed by the loss of one or more electrons). A negatively charged ion is called an anion (formed by the gain of one or more electrons).\\n\\n**Step 3:** Correct classification is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 6: Determining atomic ratio from mass ratio and atomic mass
    archs.append({
        'templates': [
            "A compound contains elements X (atomic mass = {} u) and Y (atomic mass = {} u) combined in a mass ratio of {}:{}. What is the simplest atomic ratio of X to Y?",
            "Given that hydrogen (atomic mass 1 u) and oxygen (atomic mass 16 u) combine in water in a 1:8 mass ratio, what is the calculated atomic ratio?",
            "In ammonia, nitrogen (atomic mass 14 u) and hydrogen (atomic mass 1 u) combine in a 14:3 mass ratio. Calculate the atomic ratio (N:H):",
            "In sulfur dioxide, sulfur (atomic mass 32 u) and oxygen (atomic mass 16 u) combine in 1:1 mass ratio. Find the atomic ratio (S:O):"
        ],
        'data': [
            (1, 16, 1, 8, "2:1 (H2O)", "1:8; 1:2; 8:1"),
            (14, 1, 14, 3, "1:3 (NH3)", "3:1; 14:3; 1:1"),
            (12, 16, 3, 8, "1:2 (CO2)", "2:1; 3:8; 1:1"),
            (32, 16, 1, 1, "1:2 (SO2)", "2:1; 1:1; 1:3"),
            (40, 16, 5, 2, "1:1 (CaO)", "5:2; 2:5; 2:1"),
            (24, 16, 3, 2, "1:1 (MgO)", "3:2; 2:3; 1:2")
        ],
        'calc': lambda item: (
            item[4],
            split_options(item[5]),
            f"**Step 1:** To find the atomic ratio, divide the mass ratio of each element by its respective atomic mass: \\(\\text{{Atomic ratio}} = \\frac{{\\text{{Mass ratio of X}}}}{{\\text{{Atomic mass of X}}}} : \\frac{{\\text{{Mass ratio of Y}}}}{{\\text{{Atomic mass of Y}}}}\\).\\n\\n**Step 2:** For X: \\(\\frac{{{item[2]}}}{{{item[0]}}}\\); For Y: \\(\\frac{{{item[3]}}}{{{item[1]}}}\\).\\n\\n**Step 3:** Simplifying to the simplest whole-number ratio yields {item[4]}."
        ),
        'diff': 'hard'
    })

    # Arch 7: Distinguishing between atoms, molecules, and formula units
    archs.append({
        'templates': [
            "Why is the formula of sodium chloride written as NaCl rather than as a discrete molecule?",
            "In sodium chloride crystal, each sodium ion is surrounded by how many chloride ions, and vice versa?",
            "Which of the following compounds consists of a 3D ionic lattice rather than individual discrete molecules?",
            "The term 'Formula Unit' is specifically used for:"
        ],
        'data': [
            ("Because sodium chloride exists as a three-dimensional crystal lattice of alternating Na⁺ and Cl⁻ ions, not as discrete neutral molecules", "Because sodium and chlorine do not form chemical bonds; Because NaCl evaporates at room temperature; Because chlorine is monoatomic"),
            ("6 chloride ions (octahedral coordination)", "2 chloride ions; 4 chloride ions; 8 chloride ions"),
            ("Sodium chloride (NaCl)", "Water (H2O); Carbon dioxide (CO2); Methane (CH4)"),
            ("ionic compounds whose constituent particles are ions arranged in an extended network", "gaseous molecular elements; noble gases; covalent organic liquids")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Ionic compounds (like \\(\\text{{NaCl}}, \\text{{CaO}}, \\text{{MgCl}}_2\\)) do not consist of discrete molecules.\\n\\n**Step 2:** Instead, they form a vast three-dimensional crystalline lattice in which oppositely charged ions are held together by electrostatic forces in regular geometric coordination.\\n\\n**Step 3:** The chemical formula representing the simplest ratio of ions in the lattice is called a 'formula unit'. Correct explanation is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 8: Allotropes and diverse molecular forms of elements
    archs.append({
        'templates': [
            "Oxygen exists in the Earth's atmosphere as two distinct allotropic molecular forms: diatomic oxygen (O2) and triatomic ozone (O3). How do they differ in atomicity?",
            "What is the atomicity of Buckminsterfullerene (C60), a spherical molecular allotrope of carbon?",
            "Which molecular form of an element shields life on Earth from harmful solar ultraviolet (UV) radiation?",
            "Solid rhombic sulfur exists as puckered ring molecules with which molecular formula and atomicity?"
        ],
        'data': [
            ("Oxygen gas is diatomic (atomicity = 2), while ozone is triatomic (atomicity = 3)", "Both have atomicity = 1; Oxygen is monoatomic and ozone is diatomic; Oxygen is triatomic and ozone is tetra-atomic"),
            ("60 (atomicity = 60)", "12; 24; 100"),
            ("Ozone (O3, triatomic molecule of oxygen)", "Diatomic oxygen (O2); Carbon dioxide (CO2); Nitrogen (N2)"),
            ("S8 (octa-atomic puckered ring, atomicity = 8)", "S2; S4; S16")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Allotropes are different molecular or physical forms of the same chemical element in the same physical state.\\n\\n**Step 2:** Diatomic oxygen (\\(\\text{{O}}_2\\)) has atomicity 2, while ozone (\\(\\text{{O}}_3\\)) has atomicity 3 and absorbs UV radiation in the stratosphere. Sulfur exists as \\(\\text{{S}}_8\\) crown-shaped rings with atomicity 8. Fullerene (\\(\\text{{C}}_{{60}}\\)) contains 60 carbon atoms in a soccer-ball cage.\\n\\n**Step 3:** Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-9-9.2.2', 'Molecules of elements and compounds', archs)

def main():
    all_questions = []

    print("Generating 9.1.1...")
    q_9_1_1 = gen_9_1_1()
    print(f"9.1.1 generated {len(q_9_1_1)} questions")
    all_questions.extend(q_9_1_1)

    print("Generating 9.1.2...")
    q_9_1_2 = gen_9_1_2()
    print(f"9.1.2 generated {len(q_9_1_2)} questions")
    all_questions.extend(q_9_1_2)

    print("Generating 9.2.1...")
    q_9_2_1 = gen_9_2_1()
    print(f"9.2.1 generated {len(q_9_2_1)} questions")
    all_questions.extend(q_9_2_1)

    print("Generating 9.2.2...")
    q_9_2_2 = gen_9_2_2()
    print(f"9.2.2 generated {len(q_9_2_2)} questions")
    all_questions.extend(q_9_2_2)

    out_file = 'scripts/cbse9_scie_ch9_part_a.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved {len(all_questions)} questions to {out_file}")

if __name__ == '__main__':
    main()
