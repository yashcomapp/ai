import json
import math

def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        "Unbalanced gametic recombination",
        "Passive thermodynamic stagnation",
        "Spontaneous non-mitotic dissociation"
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
                "chapterNumber": 11,
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
# SUBTOPIC 11.1.1: Binary and multiple fission (Amoeba, Plasmodium)
# ==============================================================================
def gen_11_1_1():
    archs = []

    # Arch 1: Binary fission in Amoeba
    archs.append({
        'templates': [
            "How does the unicellular protozoan Amoeba reproduce under favorable environmental conditions?",
            "During binary fission in Amoeba, which event occurs FIRST before the cell cleaves into two?",
            "In Amoeba, the division of the nucleus (karyokinesis) is followed by which process to complete binary fission?",
            "Binary fission in Amoeba can take place along which plane of cell division?"
        ],
        'data': [
            ("By binary fission, where the single parent cell divides into two genetically identical daughter cells", "By budding, forming colonial clusters; By sexual syngamy with spore release; By fragmentation of pseudopodia"),
            ("Elongation and nuclear division (karyokinesis)", "Cytokinesis; Formation of a thick cyst wall; Shedding of pseudopodia permanently"),
            ("Division of the cytoplasm (cytokinesis) through constriction of the cell membrane", "Spore formation; Gametogenesis; Nuclear disintegration"),
            ("Any plane (it has no fixed plane of division due to its irregular, non-rigid shape)", "Only longitudinal plane; Only transverse plane; Strictly equatorial plane")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In Amoeba, reproduction takes place by simple binary fission.\\n\\n**Step 2:** First, the single nucleus elongates and divides into two daughter nuclei by mitosis (karyokinesis).\\n\\n**Step 3:** This is followed by constriction of the cytoplasm (cytokinesis), forming two separate, identical daughter Amoebae. Because Amoeba is irregular in shape, division can take place in any plane. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Binary fission in Leishmania (causes Kala-azar)
    archs.append({
        'templates': [
            "How does binary fission in Leishmania (the protozoan parasite causing Kala-azar) differ from that in Amoeba?",
            "Leishmania reproduces by binary fission that occurs in which specific plane relative to its whip-like flagellum?",
            "Which disease is caused by the flagellated protozoan Leishmania, which reproduces by oriented binary fission?",
            "In Leishmania, the division of the cell body occurs in a definite longitudinal orientation because:"
        ],
        'data': [
            ("It occurs in a definite longitudinal orientation relative to the whip-like flagellum at one end", "It can occur in any random plane; It always occurs transversely; It involves multiple fission only"),
            ("Longitudinal plane (along the length of the organism)", "Transverse plane; Oblique plane; Random unoriented plane"),
            ("Kala-azar (Black fever or visceral leishmaniasis)", "Malaria; Sleeping sickness; Amoebic dysentery"),
            ("the organism has a definite cellular organization with a whip-like flagellum structure at one end", "it has a rigid cellulose cell wall; it is multicellular; it lacks a true nucleus")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Unlike Amoeba, some unicellular organisms show more complex cellular organization.\\n\\n**Step 2:** Leishmania has a whip-like flagellum structure at one end.\\n\\n**Step 3:** In Leishmania, binary fission occurs in a definite orientation (longitudinally) in relation to these structures. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 3: Multiple fission in Plasmodium (Malarial parasite)
    archs.append({
        'templates': [
            "How does Plasmodium (the malarial parasite) reproduce inside the host red blood cells and liver cells?",
            "What defines multiple fission as observed in Plasmodium?",
            "During multiple fission in Plasmodium, what protective structure forms around the dividing cell?",
            "What happens when the protective cyst of Plasmodium matures and ruptures?"
        ],
        'data': [
            ("By multiple fission, where a single parent cell divides simultaneously into many daughter cells", "By binary fission into two daughter cells; By budding from outer surface; By sexual conjugation"),
            ("A form of asexual reproduction in which a single parent cell divides to produce many daughter cells simultaneously", "A process forming exactly two identical cells; Regeneration of lost appendages; Meiotic spore formation"),
            ("A protective, resistant cyst wall", "A cellulose capsid; A chitinous cuticle; A calcareous shell"),
            ("The cyst bursts open, releasing numerous daughter cells (merozoites) simultaneously into the blood", "The entire cell dies; Exactly two cells emerge; Spores dry up permanently")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Plasmodium reproduces by multiple fission.\\n\\n**Step 2:** Under adverse conditions, the parasite rounds up and secretes a protective cyst around itself. Within the cyst, the nucleus undergoes repeated divisions to produce many daughter nuclei.\\n\\n**Step 3:** Each nucleus becomes surrounded by cytoplasm, forming numerous daughter cells simultaneously. When the cyst bursts, all daughter cells are liberated. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 4: Multiple fission in Amoeba during unfavorable conditions (Encystment)
    archs.append({
        'templates': [
            "Under adverse or unfavorable conditions (such as drought or scarcity of food), how does Amoeba survive and reproduce?",
            "What is the process called when Amoeba withdraws its pseudopodia and secretes a three-layered protective wall around itself?",
            "When favorable conditions return, what happens inside the encysted Amoeba?",
            "The minute, amoeba-like daughter cells produced by multiple fission within an Amoeba cyst are called:"
        ],
        'data': [
            ("It withdraws pseudopodia, secretes a protective 3-layered cyst (encystment), and divides by multiple fission (sporulation)", "It dies immediately; It reproduces sexually with another Amoeba; It moves into the air as a gas"),
            ("Encystment", "Excystation; Sporogenesis; Budding"),
            ("The nucleus divides repeatedly by multiple fission to produce many pseudopodiospores, and the cyst wall ruptures in water", "It undergoes meiosis to produce gametes; It remains permanently dormant; It dissolves completely"),
            ("Pseudopodiospores (or minute amoebulae)", "Zoospores; Conidia; Gemmules")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** During unfavorable conditions, Amoeba withdraws its pseudopodia and secretes a tough three-layered cyst around itself (encystment).\\n\\n**Step 2:** Within the cyst, it divides repeatedly by multiple fission to form many tiny pseudopodiospores.\\n\\n**Step 3:** When favorable moisture conditions return, the cyst wall bursts, releasing these pseudopodiospores to grow into independent Amoebae. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 5: Asexual vs Sexual reproduction comparison
    archs.append({
        'templates': [
            "Which of the following is a fundamental characteristic of ASEXUAL reproduction?",
            "Why are offspring produced by asexual reproduction referred to as 'clones'?",
            "What is the primary evolutionary advantage of SEXUAL reproduction over asexual reproduction?",
            "Which statement comparing asexual and sexual reproduction is FALSE?"
        ],
        'data': [
            ("Only a single parent is involved, and reproduction occurs without the formation or fusion of gametes", "Two parents of opposite sexes are mandatory; Offspring always have half the parental chromosome number; Genetic recombination is high"),
            ("Because they are genetically identical and exact morphological copies of the single parent organism", "Because they have different DNA; Because they reproduce faster; Because they are sterile"),
            ("Sexual reproduction creates new combinations of genes and introduces genetic variation, aiding species adaptation and survival", "Sexual reproduction requires less energy; Sexual reproduction produces exact clones; Sexual reproduction is much faster"),
            ("Asexual reproduction produces genetically diverse offspring with novel traits", "Asexual reproduction involves only mitosis; Sexual reproduction involves meiosis and fertilization; Clones are produced in asexual reproduction")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Asexual reproduction involves a single individual producing offspring without the involvement of gamete formation or fertilization.\\n\\n**Step 2:** Because the genetic material is copied faithfully by mitosis, the offspring are morphologically and genetically identical to the parent and are called clones.\\n\\n**Step 3:** Sexual reproduction combines DNA from two parents, generating genetic variations essential for natural selection. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 6: Chronological sequence of binary fission stages
    archs.append({
        'templates': [
            "Which of the following represents the correct chronological sequence of events during binary fission in Amoeba?",
            "Identify the correct chronological order of stages in Amoeba reproduction:",
            "What is the final stage of binary fission in a unicellular organism?",
            "During cell division in binary fission, cytokinesis occurs:"
        ],
        'data': [
            ("Nuclear elongation → Nuclear constriction and division (Karyokinesis) → Cytoplasmic constriction → Separation into two daughter Amoebae (Cytokinesis)", "Cytokinesis → Karyokinesis → DNA replication; Separation of cells → Nuclear division → Growth; Cyst formation → Binary split → Gametogenesis"),
            ("Replication of genetic material → Division of nucleus → Division of cytoplasm → Formation of two independent cells", "Division of cytoplasm → Division of nucleus → DNA replication; Formation of 4 cells → Nuclear merge; Meiotic division"),
            ("Cleavage of the cytoplasm (cytokinesis) and separation of the two daughter cells", "Elongation of the nucleus; Replication of DNA; Disappearance of pseudopodia"),
            ("after the complete division and segregation of the two daughter nuclei (karyokinesis)", "before the nucleus starts dividing; simultaneously with DNA replication; only in the absence of water")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Binary fission begins with the duplication of DNA.\\n\\n**Step 2:** The nucleus then elongates, constricts in the middle, and divides into two nuclei (karyokinesis).\\n\\n**Step 3:** Cytoplasm then constricts centrally and pinches off into two daughter cells (cytokinesis). Correct sequence is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 7: Binary fission in Paramecium (transverse division)
    archs.append({
        'templates': [
            "In the ciliated protozoan Paramecium, binary fission occurs along which plane of the organism?",
            "How does Paramecium divide during asexual reproduction?",
            "Paramecium exhibits {} binary fission, while Euglena exhibits {} binary fission:",
            "Which protozoan divides transversely across its slippers-shaped body?"
        ],
        'data': [
            ("Transverse plane (perpendicular to its longitudinal axis)", "Longitudinal plane; Oblique plane; Random unoriented plane"),
            ("By transverse binary fission into two daughter cells", "By longitudinal fission; By multiple fission; By budding"),
            ("Transverse binary fission", "Longitudinal binary fission", "Transverse; Longitudinal", "Longitudinal; Transverse; Random; Oblique"),
            ("Paramecium", "Euglena; Leishmania; Amoeba")
        ],
        'calc': lambda item: (
            item[0] if len(item) == 2 else ("Transverse; Longitudinal" if len(item) == 4 else item[0]),
            split_options(item[1] if len(item) == 2 else ("Longitudinal; Transverse; Random; Oblique" if len(item) == 4 else item[1])),
            f"**Step 1:** In Paramecium (a ciliate), the plane of cell division is transverse (across the width of the cell).\\n\\n**Step 2:** In flagellates like Euglena and Leishmania, binary fission is longitudinal (along the length of the cell).\\n\\n**Step 3:** In Amoeba, fission is simple and occurs in any plane. Correct answer is '{item[0] if len(item) == 2 else item[2]}'."
        ),
        'diff': 'medium'
    })

    # Arch 8: Population doubling calculations in binary fission
    archs.append({
        'templates': [
            "A bacterium divides by binary fission every 20 minutes. Starting from a single bacterium, how many bacteria will be present after {} hour(s)?",
            "In an ideal culture medium, a single cell dividing by binary fission every 30 minutes will produce how many cells in {} hours?",
            "How many generations of binary fission are required to produce 64 cells from a single parent cell?",
            "If a protozoan population doubles through binary fission every generation, how many cells are produced from 1 cell after {} generations?"
        ],
        'data': [
            (1.0, "8 bacteria (since 3 divisions: 2³ = 8)", "4; 6; 16"),
            (2.0, "64 bacteria (since 6 divisions: 2⁶ = 64)", "32; 128; 256"),
            (3.0, "512 bacteria (since 9 divisions: 2⁹ = 512)", "256; 1024; 128"),
            (64, "6 generations (since 2⁶ = 64)", "4 generations; 5 generations; 8 generations"),
            (4, "16 cells (2⁴ = 16)", "8; 12; 32"),
            (5, "32 cells (2⁵ = 32)", "16; 64; 10"),
            (0.5, "4 bacteria (since 2 divisions: 2² = 4)", "2; 8; 16"),
            (1.5, "32 bacteria (since 5 divisions: 2⁵ = 32)", "16; 64; 8")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1:** In binary fission, the population doubles with each division generation according to the formula \\(N = N_0 \\times 2^n\\), where n is the number of division cycles.\\n\\n**Step 2:** Calculate total generations \\(n = \\frac{{\\text{{Total time}}}}{{\\text{{Generation time}}}}\\).\\n\\n**Step 3:** Substitute into \\(2^n\\) to obtain the final count. Correct answer is '{item[1]}'."
        ),
        'diff': 'hard'
    })

    return generate_vault_questions('CBSE-9-SCIE-11-11.1.1', 'Binary and multiple fission (Amoeba, Plasmodium)', archs)

# ==============================================================================
# SUBTOPIC 11.1.2: Budding, spore formation, fragmentation
# ==============================================================================
def gen_11_1_2():
    archs = []

    # Arch 1: Budding in Yeast
    archs.append({
        'templates': [
            "How does the unicellular fungus Yeast reproduce asexually?",
            "What is a 'bud' in yeast reproduction?",
            "During rapid asexual budding in a sugar solution, yeast cells often form:",
            "Which of the following organisms reproduces by budding as a single-celled eukaryote?"
        ],
        'data': [
            ("By budding, where a small protuberance appears on the parent cell, receives a daughter nucleus, and separates", "By binary fission into two equal halves; By producing motile zoospores; By fragmentation of hyphae"),
            ("A small bulb-like projection or outgrowth formed on the body of the parent yeast cell", "A spore with a thick wall; A root-like rhizoid; A male gamete"),
            ("long chains of interconnected buds that remain attached to one another", "thick-walled resting cysts; multicellular filaments called hyphae; sexual zygospores"),
            ("Yeast", "Amoeba; Spirogyra; Planaria")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Yeast (a unicellular fungus) reproduces asexually by budding.\\n\\n**Step 2:** A small bulb-like projection called a bud develops on the parent body; the nucleus divides by mitosis and one daughter nucleus moves into the bud.\\n\\n**Step 3:** The bud grows, pinches off, or forms long chains of buds in nutrient-rich sugar solutions. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Budding in Hydra
    archs.append({
        'templates': [
            "How does the multicellular animal Hydra reproduce asexually?",
            "Which type of cells does Hydra utilize for asexual reproduction by budding?",
            "In Hydra, a bud develops as an outgrowth due to repeated cell division at:",
            "What happens when the bud of a Hydra matures?"
        ],
        'data': [
            ("By budding, where an outgrowth develops on the body wall, grows into a miniature individual with mouth and tentacles, and detaches", "By multiple fission inside a cyst; By breaking into microscopic spores; By laying unfertilized eggs"),
            ("Regenerative cells", "Nerve cells; Gametic cells; Epithelial muscle cells only"),
            ("one specific site on the parent body wall", "all parts of the body simultaneously; the tentacles only; the basal disc only"),
            ("It detaches from the parent body and becomes an independent, free-living organism", "It remains attached permanently to form a coral reef; It is absorbed back into the parent; It dies immediately")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Hydra reproduces asexually by budding using its regenerative cells.\\n\\n**Step 2:** Repeated cell division at one specific site causes an outgrowth (bud) to develop.\\n\\n**Step 3:** The bud develops a tiny body, mouth, and tentacles. When fully mature, it separates from the parent to live independently. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Fragmentation in Spirogyra
    archs.append({
        'templates': [
            "What method of asexual reproduction is observed in the green filamentous alga Spirogyra?",
            "How does fragmentation occur in Spirogyra?",
            "Why can Spirogyra reproduce by simple fragmentation, whereas complex multicellular animals like birds or mammals cannot?",
            "In Spirogyra, when the filament breaks into smaller pieces upon reaching maturity:"
        ],
        'data': [
            ("Fragmentation", "Budding; Spore formation; Binary fission"),
            ("The mature multicellular filament breaks up into smaller fragments, and each fragment grows into a new individual by mitotic cell division", "The organism dissolves into single spores; The cell secretes a cyst and splits; The filament produces seeds"),
            ("Because Spirogyra has a simple body organization where all cells are similar, unlike complex animals with specialized tissues and organs", "Because Spirogyra has no DNA; Because Spirogyra is a plant; Because animals cannot undergo cell division"),
            ("each fragment grows into a complete new Spirogyra filament", "the fragments die; they merge into a single sphere; they produce flowers")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Spirogyra is a multicellular filamentous green alga with a simple cellular organization.\\n\\n**Step 2:** Upon maturation, the filament simply breaks into two or more smaller pieces (fragments).\\n\\n**Step 3:** Each fragment continues to divide by mitosis and grows into a full new filament. This process is called fragmentation. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 4: Regeneration in Planaria and Hydra
    archs.append({
        'templates': [
            "If a flatworm Planaria is cut into two or three pieces, what will happen to each piece?",
            "What is the biological process called when an organism regrows a complete body from a cut or detached body part?",
            "Why is regeneration NOT considered identical to reproduction?",
            "Which specialized cells carry out the process of regeneration in Planaria?"
        ],
        'data': [
            ("Each cut piece grows and regenerates into a complete, independent Planaria", "All pieces die immediately; Only the head piece survives; The pieces fuse back together"),
            ("Regeneration", "Fragmentation; Budding; Fission"),
            ("Because organisms do not normally depend on being cut or broken into pieces to reproduce; it is an ability to repair and replace lost tissues", "Because regeneration requires two parents; Because regeneration produces seeds; Because regeneration only occurs in plants"),
            ("Specialized regenerative cells (stem-like neoblasts) that proliferate and differentiate into diverse tissue types", "Mature muscle cells; Nerve fibers only; Red blood cells")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** If organisms like Planaria or Hydra are cut into pieces, each cut portion can grow into a complete organism through regeneration.\\n\\n**Step 2:** Regeneration is carried out by specialized cells that proliferate into large masses of cells and differentiate into various cell types.\\n\\n**Step 3:** However, regeneration is primarily a developmental and repair mechanism, not a normal reproductive strategy. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 5: Spore formation in Rhizopus (Bread mould)
    archs.append({
        'templates': [
            "What method of asexual reproduction is typical of the bread mould fungus Rhizopus?",
            "In Rhizopus, what are the tiny bulb-like structures borne atop upright reproductive hyphae called?",
            "What is contained inside the sporangia of Rhizopus?",
            "How do spores of Rhizopus survive adverse conditions such as desiccation and heat?"
        ],
        'data': [
            ("Spore formation", "Binary fission; Fragmentation; Vegetative propagation"),
            ("Sporangia (singular: sporangium)", "Conidiophores; Rhizoids; Stolon buds"),
            ("Numerous microscopic reproductive cells called spores", "Seeds; Gametes; Pollen grains"),
            ("They are covered by thick, resistant protective walls that preserve them until they contact moist bread", "They burrow underground; They form magnetic shields; They enter a liquid state")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Rhizopus (common bread mould) reproduces asexually by spore formation.\\n\\n**Step 2:** Upright hyphae develop swollen terminal structures called sporangia.\\n\\n**Step 3:** Each sporangium contains hundreds of tiny spores protected by thick walls. When mature, the sporangium bursts, liberating airborne spores that germinate on moist organic substrates. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 6: Spores in non-flowering plants (Ferns and Mosses)
    archs.append({
        'templates': [
            "In non-flowering plants like ferns and mosses, asexual reproduction is accomplished through the production of:",
            "Where are the spore-producing capsules located on the undersurface of a mature fern leaf?",
            "Why are spores dispersed by wind advantageous for terrestrial non-flowering plants?",
            "What happens when a fern or moss spore lands on cool, moist soil?"
        ],
        'data': [
            ("Spores produced in sporangia", "Seeds enclosed in fruit; Flowers with nectar; Underground tubers"),
            ("In clusters of sporangia called sori (singular: sorus)", "Inside the root cortex; Within flower petals; Inside wood rings"),
            ("Lightweight microscopic spores can be carried by wind over vast distances to colonize new damp habitats", "Spores attract birds for pollination; Spores generate heat; Spores repel all fungi"),
            ("It germinates to produce a small green photosynthetic gametophyte stage", "It instantly becomes a flowering tree; It dies immediately; It forms a seed")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Non-flowering plants such as mosses and ferns reproduce via spores.\\n\\n**Step 2:** In ferns, spores are produced inside sporangia organized in clusters called sori on the underside of fronds.\\n\\n**Step 3:** The lightweight spores are dispersed by wind and germinate in damp soil to continue the life cycle. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 7: Distinguishing Fragmentation vs Regeneration vs Fission
    archs.append({
        'templates': [
            "Which of the following correctly pairs an organism with its primary mode of asexual reproduction?",
            "Fragmentation is the normal reproductive method for which of the following organisms?",
            "Regeneration of complete organisms from cut body pieces is prominently seen in:",
            "Which organism reproduces asexually by budding?"
        ],
        'data': [
            ("Spirogyra - Fragmentation; Hydra - Budding; Amoeba - Binary fission; Rhizopus - Spore formation", "Spirogyra - Budding; Hydra - Spore formation; Amoeba - Fragmentation; Rhizopus - Binary fission; All pair randomly"),
            ("Spirogyra (filamentous alga)", "Hydra; Amoeba; Paramecium"),
            ("Planaria (flatworm)", "Earthworm; Cockroach; Frog"),
            ("Hydra and Yeast", "Amoeba and Plasmodium; Spirogyra and Rhizopus; Fern and Moss")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Different organisms use specific asexual methods adapted to their structural organization.\\n\\n**Step 2:** Unicellular organisms: Amoeba (binary fission), Plasmodium (multiple fission), Yeast (budding).\\n\\n**Step 3:** Simple multicellular organisms: Spirogyra (fragmentation), Hydra (budding and regeneration), Planaria (regeneration), Rhizopus (spore formation). Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 8: Adaptations and ecological significance of asexual mechanisms
    archs.append({
        'templates': [
            "Why is spore formation one of the most successful survival adaptations for fungi and lower plants?",
            "Under which environmental circumstances is asexual reproduction most advantageous for an organism?",
            "A major limitation of relying exclusively on asexual reproduction across multiple generations is:",
            "Which of the following asexual structures can survive desiccation, extreme cold, and heat?"
        ],
        'data': [
            ("Because the thick protective spore wall resists adverse conditions like drought, heat, and lack of food until favorable moist conditions arrive", "Because spores are warm; Because spores consume no water; Because spores can fly into space"),
            ("In stable, favorable environmental conditions with abundant resources, allowing rapid population expansion without finding a mate", "During catastrophic environmental changes; When disease strikes the population; In dry deserts only"),
            ("The complete lack of genetic diversity, making the entire population vulnerable to sudden environmental changes or epidemics", "Offspring grow too slowly; Reproduction requires two parents; Excess energy is wasted on flowers"),
            ("Thick-walled fungal spores (e.g. Rhizopus spores) and encysted protozoans", "Yeast buds; Spirogyra fragments; Planaria cut pieces")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Spores are specialized dormant reproductive units surrounded by a thick, resilient wall.\\n\\n**Step 2:** They protect the organism during drought, cold, or food scarcity, germinating only upon encountering moisture and nutrients.\\n\\n**Step 3:** Asexual reproduction is rapid and efficient in stable environments, but its lack of genetic variation leaves populations vulnerable to changing conditions. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-11-11.1.2', 'Budding (Hydra, Yeast), spore formation, fragmentation', archs)

# ==============================================================================
# SUBTOPIC 11.1.3: Vegetative propagation in plants
# ==============================================================================
def gen_11_1_3():
    archs = []

    # Arch 1: Definition of vegetative propagation
    archs.append({
        'templates': [
            "What is vegetative propagation in plants?",
            "In vegetative propagation, new plantlets are produced from which parts of the parent plant?",
            "Why is vegetative propagation classified as a form of ASEXUAL reproduction?",
            "Which of the following is NOT a vegetative part of a plant?"
        ],
        'data': [
            ("A form of asexual reproduction in which new plants develop from vegetative parts like roots, stems, or leaves, without seeds", "Reproduction involving flowers and pollination; Production of plants from spores; Chemical synthesis of plant tissues"),
            ("Vegetative parts such as roots, stems, and leaves", "Flowers and seeds; Fruits and ovules; Pollen grains only"),
            ("Because only one parent plant is involved and there is no formation or fusion of gametes", "Because it requires soil; Because flowers are needed; Because it produces different varieties"),
            ("Flower (it is the sexual reproductive organ)", "Root; Stem; Leaf")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Vegetative propagation is an asexual mode of reproduction in plants.\\n\\n**Step 2:** New individuals arise from vegetative parts of the plant body (root, stem, or leaf) rather than from seeds or spores.\\n\\n**Step 3:** The offspring are genetically identical to the single parent plant. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Vegetative propagation by leaves (Bryophyllum)
    archs.append({
        'templates': [
            "Which plant is famous for natural vegetative propagation through adventitious buds developed on the margins of its leaves?",
            "In Bryophyllum, where do the vegetative buds develop on the leaf?",
            "What happens when a detached leaf of Bryophyllum falls onto moist soil?",
            "Besides Bryophyllum, which other plant reproduces vegetatively through adventitious foliar buds on its leaves?"
        ],
        'data': [
            ("Bryophyllum", "Rose; Mango; Hibiscus"),
            ("Along the notches in the margins of the leaf", "At the tip of the petiole; On the primary vein; On the flower stalk"),
            ("The adventitious buds at the leaf notches sprout roots and shoot to grow into independent new plants", "The leaf decays with no offspring; The leaf produces flowers; The leaf forms seeds"),
            ("Begonia", "Potato; Ginger; Onion")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Bryophyllum (sprout leaf plant) possesses specialized adventitious buds in the notches along the margins of its fleshy leaves.\\n\\n**Step 2:** When the leaf falls onto damp soil or touches the ground, these buds develop adventitious roots and shoots.\\n\\n**Step 3:** Each bud can separate and develop into a complete, independent plant. Begonia also reproduces similarly. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Vegetative propagation by underground modified stems
    archs.append({
        'templates': [
            "A potato tuber develops new plants from specialized depressions on its surface. What are these structures called?",
            "How does ginger (Zingiber officinale) propagate vegetatively under the soil?",
            "Onion and garlic propagate vegetatively through which modified stem structure?",
            "Grass, strawberry, and mint spread horizontally over the ground and root at nodes using:"
        ],
        'data': [
            ("Eyes (which are vegetative nodes bearing scale leaves and dormant buds)", "Roots; Flowers; Stomas"),
            ("Through underground modified stems called rhizomes bearing buds", "Through taproots; Through true seeds; Through leaf spores"),
            ("Bulbs (fleshy underground modified stems)", "Tubers; Runners; Tendrils"),
            ("Runners or stolons (subaerial creeping stems)", "Tap roots; Spines; Aerial climbers")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Many plants store food in modified underground stems capable of vegetative propagation.\\n\\n**Step 2:** Potato: tuber with 'eyes' (buds in leaf axils). Ginger and turmeric: underground rhizomes. Onion and garlic: modified bulbs.\\n\\n**Step 3:** Grass and mint spread via subaerial creeping stems called runners. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 4: Vegetative propagation by roots
    archs.append({
        'templates': [
            "Which of the following plants reproduces vegetatively through adventitious buds developed on its swollen ROOTS?",
            "Sweet potato (Ipomoea batatas) is a modified {} that can produce new plantlets vegetatively:",
            "Which pair of plants propagates vegetatively through swollen root tubers bearing buds?",
            "How does a sweet potato tuber differ botanically from a normal potato tuber?"
        ],
        'data': [
            ("Sweet potato (and Dahlia)", "Potato; Ginger; Onion"),
            ("root (root tuber)", "stem; leaf; flower"),
            ("Sweet potato and Dahlia", "Potato and Ginger; Onion and Garlic; Rose and Jasmine"),
            ("Sweet potato is a modified root, whereas ordinary potato is a modified underground stem (stem tuber)", "Both are modified leaves; Sweet potato is a fruit; Potato is an aerial seed")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** While ordinary potato is an underground stem tuber (with nodes, internodes, and eyes), sweet potato and Dahlia have swollen root tubers.\\n\\n**Step 2:** These fleshy roots develop adventitious buds that sprout into new plants when planted in moist soil.\\n\\n**Step 3:** Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 5: Artificial vegetative propagation: Cutting, Layering, Grafting
    archs.append({
        'templates': [
            "Which artificial propagation method involves cutting a piece of stem with a node and planting it in moist soil to root (e.g. in Rose, Sugarcane)?",
            "In which artificial method is a lower branch of a plant bent down into the soil, buried at a node, and detached after rooting (e.g. in Jasmine)?",
            "What is the artificial propagation method where a branch (scion) of a superior quality plant is grafted onto the root system (stock) of a hardy plant?",
            "In grafting, the rooted lower plant portion is called the {}, while the attached superior stem portion is called the {}:"
        ],
        'data': [
            ("Stem cutting", "Layering; Grafting; Tissue culture"),
            ("Layering", "Cutting; Grafting; Pollination"),
            ("Grafting", "Layering; Cutting; Micropropagation"),
            ("stock", "scion", "Stock; Scion", "Scion; Stock; Callus; Explant")
        ],
        'calc': lambda item: (
            item[0] if len(item) == 2 else ("Stock (root portion); Scion (grafted shoot)" if len(item) == 4 else item[0]),
            split_options(item[1] if len(item) == 2 else ("Scion; Stock; Callus; Bud" if len(item) == 4 else item[1])),
            f"**Step 1:** Cutting: a piece of stem with a node is planted in soil (rose, sugarcane, money plant).\\n\\n**Step 2:** Layering: a flexible branch is pegged into soil to induce adventitious roots before cutting off (jasmine, bougainvillea).\\n\\n**Step 3:** Grafting: joining the stem of a desirable variety (scion) onto a rooted stem (stock) so their vascular cambiums merge (apple, mango, rose). Correct answer is '{item[0] if len(item) == 2 else item[2]}'."
        ),
        'diff': 'medium'
    })

    # Arch 6: Plant tissue culture (Micropropagation)
    archs.append({
        'templates': [
            "What is the modern biotechnological technique of producing new plants from a small tissue sample grown in an artificial nutrient medium under sterile conditions?",
            "In plant tissue culture, what is the unorganized, rapidly dividing mass of cells formed from the explant called?",
            "What chemical substances are added to the tissue culture nutrient medium to stimulate root and shoot differentiation from the callus?",
            "Why is tissue culture widely utilized in commercial horticulture for propagating orchids, ornamental plants, and carnations?"
        ],
        'data': [
            ("Tissue culture (or Micropropagation)", "Hydroponics; Grafting; Layering"),
            ("Callus", "Embryo; Seedling; Sporangium"),
            ("Plant growth hormones (such as auxins and cytokinins)", "Antibiotics only; Mineral acids; Animal enzymes"),
            ("Because it enables the rapid production of thousands of disease-free (virus-free) plantlets from a single parent in a short time", "Because it requires no sterile conditions; Because plants produce no roots; Because plants grow without sunlight")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Tissue culture (micropropagation) involves isolating a small piece of plant tissue (explant) from the growing tip and placing it in a sterile nutrient medium.\\n\\n**Step 2:** The cells divide rapidly to form an undifferentiated cellular mass called a callus.\\n\\n**Step 3:** The callus is transferred to media containing hormones (auxins/cytokinins) to induce differentiation into plantlets. It produces thousands of identical, disease-free plants rapidly. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 7: Advantages of vegetative propagation
    archs.append({
        'templates': [
            "Which of the following is a major agricultural ADVANTAGE of vegetative propagation?",
            "Why is vegetative propagation the ONLY viable method for cultivating crops like banana, seedless orange, jasmine, and rose?",
            "How do plants raised by vegetative propagation compare to plants grown from seeds regarding time to flowering and fruiting?",
            "All plants produced by vegetative propagation are genetically identical to the parent plant. This property ensures:"
        ],
        'data': [
            ("Plants raised by vegetative propagation bear flowers and fruits much earlier than those grown from seeds", "Plants require no sunlight; Plants have high genetic diversity; Plants are immune to all diseases"),
            ("Because these cultivated varieties have lost the capacity to produce viable seeds", "Because their seeds are poisonous; Because their pollen is radioactive; Because seeds cannot germinate in soil"),
            ("Vegetatively propagated plants flower and fruit much earlier than seed-raised plants", "They take twice as long to flower; They never bear fruit; They flower at the exact same age"),
            ("strict preservation and uniformity of desirable parental traits across the entire crop", "continuous evolutionary variation; spontaneous mutations; elimination of all pests")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Vegetative propagation offers distinct horticultural advantages: (1) Plants flower and bear fruit earlier than seed-grown plants, (2) It is the sole method for propagating seedless varieties (banana, seedless grapes, rose), (3) Exact desirable characteristics of the parent are preserved uniformly.\\n\\n**Step 2:** Offspring are genetic clones of the high-yielding parent plant.\\n\\n**Step 3:** Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 8: Disadvantages of vegetative propagation
    archs.append({
        'templates': [
            "What is a significant biological DISADVANTAGE of relying solely on vegetative propagation for crops?",
            "Why are vegetatively propagated monoculture crops (like Cavendish bananas or clone potatoes) especially vulnerable to devastating epidemics?",
            "Why does continuous vegetative propagation without sexual reproduction fail to produce new crop varieties?",
            "Overcrowding and severe competition for light, water, and nutrients occur in vegetative propagation because:"
        ],
        'data': [
            ("The complete absence of genetic variation means the entire crop has identical susceptibility to diseases or environmental stress", "Plants produce toxic fruits; Plants take decades to grow; Plants require excessive fertilizer"),
            ("Because all plants share identical genetic susceptibility, so a single pathogen can wipe out the entire plantation (e.g. Panama disease)", "Because cloned plants have no cell walls; Because cloned plants attract locusts; Because cloned plants lack roots"),
            ("Because asexual reproduction involves only mitosis, producing no new genetic combinations or variations", "Because vegetative parts have no chromosomes; Because hormones suppress DNA; Because soil destroys mutations"),
            ("daughter plantlets develop in close proximity around the parent plant without wide seed dispersal mechanisms", "plantlets repel each other; roots grow upwards into air; plants absorb all oxygen")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The major drawbacks of vegetative propagation stem from the lack of genetic variation.\\n\\n**Step 2:** Because all individuals are clones, an outbreak of a fungal or viral disease can decimate the entire population simultaneously (as seen in historical potato blight and Panama disease in bananas).\\n\\n**Step 3:** Furthermore, offspring cluster near the parent, leading to overcrowding and competition. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-11-11.1.3', 'Vegetative propagation in plants (cuttings, runners, layering)', archs)

# ==============================================================================
# SUBTOPIC 11.2.1: Structure of a flower
# ==============================================================================
def gen_11_2_1():
    archs = []

    # Arch 1: Flower as the reproductive organ and floral whorls
    archs.append({
        'templates': [
            "In angiosperms (flowering plants), what is the primary biological function of a flower?",
            "What are the four concentric floral whorls of a complete flower arranged from outermost to innermost?",
            "Which two floral whorls are directly involved in reproduction and are termed ESSENTIAL whorls?",
            "Which two floral whorls are protective or attractive and termed ACCESSORY (non-essential) whorls?"
        ],
        'data': [
            ("It is the reproductive organ of the plant, specialized for sexual reproduction through gamete production and seed formation", "It performs 90% of photosynthesis; It absorbs mineral water from air; It anchors the plant in the soil"),
            ("Calyx (sepals) → Corolla (petals) → Androecium (stamens) → Gynoecium (carpel/pistil)", "Corolla → Calyx → Gynoecium → Androecium; Androecium → Gynoecium → Corolla → Calyx; Calyx → Androecium → Corolla → Gynoecium"),
            ("Stamens (male reproductive organ) and Carpel/Pistil (female reproductive organ)", "Sepals and Petals; Petals and Stamens; Sepals and Carpel"),
            ("Calyx (sepals) and Corolla (petals)", "Stamens and Carpels; Anther and Stigma; Filament and Style")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The flower is the specialized sexual reproductive shoot of angiosperms.\\n\\n**Step 2:** A typical flower consists of four whorls attached to the swollen receptacle: Calyx (sepals), Corolla (petals), Androecium (stamens), and Gynoecium (carpels).\\n\\n**Step 3:** Stamens and carpels are the essential reproductive whorls; sepals and petals are accessory whorls. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Calyx (Sepals) and Corolla (Petals)
    archs.append({
        'templates': [
            "What is the outermost whorl of a flower composed of sepals called, and what is its primary function?",
            "What is the second whorl of a flower composed of petals called, and what is its primary biological role?",
            "Why are the petals of insect-pollinated flowers brightly colored and scented?",
            "When the sepals and petals of a flower are not clearly differentiated and fused into a single whorl, it is called a:"
        ],
        'data': [
            ("Calyx; it protects the inner delicate reproductive whorls during the unopened bud stage", "Corolla; it attracts pollinators; Androecium; it produces pollen; Gynoecium; it forms fruit"),
            ("Corolla; its vibrant colors and scent attract pollinating insects and birds", "Calyx; it protects seeds; Androecium; it receives pollen; Thalamus; it stores sugar"),
            ("To visually attract insect pollinators (like bees and butterflies) to facilitate pollen transfer", "To scare away birds; To absorb green light; To prevent water loss"),
            ("Perianth (composed of tepals)", "Pistil; Pedicel; Bract")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The calyx consists of green sepals that enclose and protect the flower when it is in the bud stage.\\n\\n**Step 2:** The corolla consists of petals, which are usually brightly colored, scented, and equipped with nectaries to attract animal pollinators for pollination.\\n\\n**Step 3:** Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Male reproductive organ: Stamen (Anther and Filament)
    archs.append({
        'templates': [
            "What is the male reproductive unit of a flower, and what are its two structural components?",
            "What is the slender stalk that supports the anther in a stamen called?",
            "What is the swollen, bilobed terminal portion of a stamen that produces pollen grains called?",
            "What do pollen grains produced inside the anther contain?"
        ],
        'data': [
            ("Stamen (Androecium); composed of a slender filament and a terminal bilobed anther", "Carpel; composed of stigma and style; Petal; composed of blade and claw; Sepal; composed of bud sheath"),
            ("Filament", "Style; Pedicel; Petiole"),
            ("Anther", "Stigma; Ovary; Receptacle"),
            ("The male gametes (sperm cells) of the flowering plant", "Female egg cells; Miniature seeds; Chloroplasts only")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The stamen is the male reproductive organ of the flower.\\n\\n**Step 2:** It consists of a long, slender stalk called the filament and a terminal, bilobed sac called the anther.\\n\\n**Step 3:** The anther produces thousands of powdery yellow pollen grains, each enclosing the male gametes. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 4: Female reproductive organ: Carpel/Pistil (Stigma, Style, Ovary)
    archs.append({
        'templates': [
            "What is the female reproductive organ situated at the center of a flower called, and what are its three parts?",
            "What is the sticky terminal landing platform of the carpel designed to capture pollen grains called?",
            "What is the elongated middle tube through which the pollen tube grows down to reach the ovary called?",
            "What is the swollen basal portion of the carpel that encloses the ovules called?"
        ],
        'data': [
            ("Carpel or Pistil; composed of the terminal stigma, middle elongated style, and basal swollen ovary", "Stamen; composed of anther and filament; Calyx; composed of sepals; Receptacle; composed of nodes"),
            ("Stigma", "Style; Anther; Ovary"),
            ("Style", "Filament; Stigma; Pedicel"),
            ("Ovary", "Anther; Receptacle; Thalamus")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The female reproductive organ is the carpel (or pistil), which occupies the central whorl (gynoecium).\\n\\n**Step 2:** It consists of three distinct regions: (1) Stigma (sticky upper surface that traps pollen), (2) Style (slender neck tube connecting stigma to ovary), and (3) Ovary (swollen base holding ovules).\\n\\n**Step 3:** Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 5: Ovule and female gamete (egg cell)
    archs.append({
        'templates': [
            "What structures are contained inside the swollen ovary of a flower?",
            "Where is the female gamete (egg cell or ovum) located in a flowering plant?",
            "Following successful fertilization, what does the ovule develop into, and what does the surrounding ovary become?",
            "A single ovary can contain one or multiple ovules. An ovary containing a SINGLE ovule will produce a fruit with:"
        ],
        'data': [
            ("Ovules", "Pollen grains; Filaments; Sepals"),
            ("Inside the embryo sac enclosed within an ovule", "Inside the anther; On the stigma surface; In the petals"),
            ("The ovule becomes the SEED, and the ovary ripens into the FRUIT", "The ovule becomes the fruit, and ovary becomes seed; Both become petals; The ovule disintegrates"),
            ("a single seed (e.g. Mango, Peach)", "hundreds of seeds; no seeds; multiple fruits")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The ovary contains one or more rounded ovules attached to the placenta.\\n\\n**Step 2:** Inside each ovule lies the female embryo sac containing the egg cell (female gamete).\\n\\n**Step 3:** After fertilization, each fertilized ovule develops into a seed, and the ovary ripens into the protective fruit wall (pericarp). Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 6: Unisexual vs Bisexual flowers
    archs.append({
        'templates': [
            "What is a flower termed if it contains BOTH stamens and carpels?",
            "What is a flower termed if it contains EITHER stamens OR carpels, but not both?",
            "Which of the following plants produces UNISEXUAL flowers?",
            "Which of the following plants produces BISEXUAL (hermaphrodite) flowers?"
        ],
        'data': [
            ("Bisexual flower (or hermaphrodite flower)", "Unisexual flower; Apetalous flower; Sterile flower"),
            ("Unisexual flower (either staminate/male or pistillate/female)", "Bisexual flower; Complete flower; Hermaphrodite flower"),
            ("Papaya and Watermelon (also cucumber, corn)", "Hibiscus and Mustard; Rose and Pea; Petunia and Lily"),
            ("Hibiscus and Mustard (also pea, rose)", "Papaya and Watermelon; Cucumber and Palm; Corn and Willow")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** A bisexual flower contains both male reproductive organs (stamens) and female reproductive organs (carpels) within the same blossom (e.g., Hibiscus, mustard, pea, rose).\\n\\n**Step 2:** A unisexual flower contains only stamens (staminate / male) or only carpels (pistillate / female), such as in papaya, watermelon, and cucumber.\\n\\n**Step 3:** Correct classification is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 7: Receptacle / Thalamus and Pedicel
    archs.append({
        'templates': [
            "What is the swollen or expanded tip of the flower stalk to which all four floral whorls are attached called?",
            "What is the stalk of an individual flower called?",
            "In an apple, the edible fleshy fruit portion is derived not from the ovary, but from which floral structure?",
            "A flower lacking a pedicel that is attached directly to the stem is described as:"
        ],
        'data': [
            ("Receptacle (or Thalamus)", "Pedicel; Petiole; Node"),
            ("Pedicel", "Petiole; Tendril; Rachis"),
            ("The swollen thalamus / receptacle (making apple a 'false fruit' or pome)", "The calyx; The style; The anther"),
            ("Sessile", "Pedicellate; Petiolate; Cauliflory")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The stalk that supports a flower is the pedicel.\\n\\n**Step 2:** The swollen top of the pedicel upon which the sepals, petals, stamens, and carpels are inserted is called the receptacle or thalamus.\\n\\n**Step 3:** In some fruits like apples and pears, the thalamus becomes fleshy and edible (false fruits). Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 8: Complete vs Incomplete flowers and floral diagrams
    archs.append({
        'templates': [
            "What is a flower called if it possesses all four concentric floral whorls (sepals, petals, stamens, and carpels)?",
            "A flower that lacks one or more of the four whorls is termed:",
            "Can a unisexual flower ever be a complete flower?",
            "Which of the following statements about floral morphology is correct?"
        ],
        'data': [
            ("A complete flower", "An incomplete flower; A unisexual flower; A sterile flower"),
            ("An incomplete flower", "A complete flower; A bisexual flower; A perfect flower"),
            ("No, because a unisexual flower by definition lacks either the stamen or carpel whorl", "Yes, if it has sepals and petals; Yes, if it is large; Yes, in aquatic plants"),
            ("All complete flowers are bisexual, but not all bisexual flowers are necessarily complete", "All unisexual flowers are complete; Sepals produce female gametes; The style forms the seed coat")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** A complete flower possesses all four whorls: calyx, corolla, androecium, and gynoecium.\\n\\n**Step 2:** If any one or more of these whorls is missing, the flower is incomplete.\\n\\n**Step 3:** Every unisexual flower is necessarily incomplete because it lacks one reproductive whorl. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-11-11.2.1', 'Structure of a flower: Sepals, petals, stamens, carpel', archs)

def main():
    all_questions = []

    print("Generating 11.1.1...")
    q1 = gen_11_1_1()
    print(f"11.1.1 generated {len(q1)} questions")
    all_questions.extend(q1)

    print("Generating 11.1.2...")
    q2 = gen_11_1_2()
    print(f"11.1.2 generated {len(q2)} questions")
    all_questions.extend(q2)

    print("Generating 11.1.3...")
    q3 = gen_11_1_3()
    print(f"11.1.3 generated {len(q3)} questions")
    all_questions.extend(q3)

    print("Generating 11.2.1...")
    q4 = gen_11_2_1()
    print(f"11.2.1 generated {len(q4)} questions")
    all_questions.extend(q4)

    out_file = 'scripts/cbse9_scie_ch11_part_a.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved {len(all_questions)} questions to {out_file}")

if __name__ == '__main__':
    main()
