import json
import random

random.seed(8101)

def build_ch1_questions():
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
    # 1.1.1 Criteria for classification (36 exam questions)
    # -------------------------------------------------------------
    tc_111 = "MH-8-SCI-1-1.1.1"
    name_111 = "Criteria for classification: complexity of cell, body organization, mode of nutrition, life style, phylogenetic relationship"
    diffs_36 = ["easy"] * 12 + ["medium"] * 14 + ["hard"] * 10
    c111_cases = [
        ("Which of the following is NOT one of Robert Whittaker's five fundamental criteria for biological classification?", "Color and atmospheric habitat", ["Complexity of cell structure (prokaryotic vs eukaryotic)", "Mode of nutrition (autotrophic vs heterotrophic)", "Phylogenetic relationship (evolutionary history)"]),
        ("Under Whittaker's classification criteria, 'Complexity of Cell Structure' divides all living organisms into:", "Prokaryotic and Eukaryotic", ["Unicellular and Multicellular", "Autotrophic and Heterotrophic", "Plants and Animals"]),
        ("Under Whittaker's criteria, 'Body Organization' classifies organisms into which two broad groups?", "Unicellular and Multicellular", ["Prokaryotic and Eukaryotic", "Producers and Consumers", "Aerobic and Anaerobic"]),
        ("What does 'Phylogenetic Relationship' in Whittaker's biological classification refer to?", "Evolutionary progression from prokaryotic to eukaryotic and unicellular to multicellular", ["Geographical distribution across continents", "Lifespan and reproduction rate", "Ecological footprint in urban areas"]),
        ("How are Fungi classified according to their mode of nutrition in Whittaker's five-kingdom system?", "Heterotrophic and saprophytic (absorption from decaying organic matter)", ["Autotrophic (photosynthetic)", "Heterotrophic and ingestive (holozoic)", "Chemosynthetic autotrophs"]),
        ("In Whittaker's classification, which lifestyle role do green plants occupy in an ecosystem?", "Producers", ["Consumers", "Decomposers", "Parasites"]),
        ("In Whittaker's ecological lifestyle criterion, which role is performed by animals?", "Consumers", ["Producers", "Decomposers", "Pioneers"]),
        ("In Whittaker's ecological lifestyle criterion, which role is performed by fungi?", "Decomposers", ["Producers", "Primary consumers", "Secondary consumers"])
    ]
    for i in range(36):
        ctx, ans, wrongs = c111_cases[i % len(c111_cases)]
        q = make_q(
            tc_111, name_111,
            f"Whittaker's Classification System: {ctx}",
            ans, wrongs,
            "Robert H. Whittaker proposed the Five Kingdom classification in 1969 based on five primary criteria.",
            "These criteria are: 1. Complexity of cell structure, 2. Complexity of organism, 3. Mode of nutrition, 4. Lifestyle, and 5. Phylogenetic relationship.",
            f"Therefore, the correct assessment is '{ans}'.",
            diffs_36[i], "exam"
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 1.1.2 Kingdom Monera, Protista, Fungi, Plantae, Animalia (37 exam questions)
    # -------------------------------------------------------------
    tc_112 = "MH-8-SCI-1-1.1.2"
    name_112 = "Kingdom Monera, Protista, Fungi, Plantae, Animalia"
    diffs_37 = ["easy"] * 12 + ["medium"] * 15 + ["hard"] * 10
    c112_cases = [
        ("Which kingdom in Whittaker's five kingdom system encompasses ALL unicellular prokaryotic organisms?", "Kingdom Monera", ["Kingdom Protista", "Kingdom Fungi", "Kingdom Plantae"]),
        ("Which kingdom includes unicellular eukaryotic organisms such as Amoeba, Paramoecium, and Euglena?", "Kingdom Protista", ["Kingdom Monera", "Kingdom Fungi", "Kingdom Animalia"]),
        ("Organisms in Kingdom Fungi are characterized by which type of cellular cell wall?", "A tough, complex sugar cell wall made of chitin", ["A rigid cellulose cell wall", "A peptidoglycan cell wall", "Absence of any cell wall"]),
        ("Which kingdom consists of multicellular eukaryotic organisms capable of photosynthesis?", "Kingdom Plantae", ["Kingdom Animalia", "Kingdom Monera", "Kingdom Fungi"]),
        ("Which kingdom is characterized by multicellular eukaryotes that lack cell walls and ingest food?", "Kingdom Animalia", ["Kingdom Plantae", "Kingdom Fungi", "Kingdom Protista"]),
        ("Which of the following organisms belongs to Kingdom Monera?", "Clostridium tetani / Streptococcus pneumoniae", ["Amoeba proteus", "Saccharomyces cerevisiae (Yeast)", "Spirogyra"]),
        ("In which kingdom do we place Euglena, an organism that possesses chloroplasts and flagella but is unicellular?", "Kingdom Protista", ["Kingdom Plantae", "Kingdom Monera", "Kingdom Animalia"]),
        ("Bread mould (Rhizopus) and mushrooms belong to which kingdom?", "Kingdom Fungi", ["Kingdom Plantae", "Kingdom Protista", "Kingdom Monera"])
    ]
    for i in range(37):
        ctx, ans, wrongs = c112_cases[i % len(c112_cases)]
        q = make_q(
            tc_112, name_112,
            f"Five Kingdoms of Life: {ctx}",
            ans, wrongs,
            "Whittaker categorized all living forms into 5 kingdoms: Monera, Protista, Fungi, Plantae, and Animalia.",
            "Each kingdom has distinct diagnostic cellular structures, cell wall compositions, and nutritional modes.",
            f"Hence, '{ans}' is the correct classification.",
            diffs_37[i], "exam"
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 1.2.1 Monera: unicellular prokaryotes (80 questions)
    # -------------------------------------------------------------
    tc_121 = "MH-8-SCI-1-1.2.1"
    name_121 = "Monera: unicellular prokaryotes (Streptococcus, Clostridium)"
    monera_q = [
        ("What is the defining cellular characteristic of organisms belonging to Kingdom Monera?", "They lack a distinct membrane-bound nucleus and membrane-bound organelles", ["They have multiple nuclei per cell", "They possess large chloroplasts and mitochondria", "They are strictly multicellular"]),
        ("Which of the following bacteria is responsible for causing curdling of milk by fermenting lactose into lactic acid?", "Lactobacillus", ["Clostridium tetani", "Streptococcus pneumoniae", "Salmonella typhi"]),
        ("What morphological shape does Streptococcus bacteria exhibit under a microscope?", "Spherical / round cells clustered in chains", ["Rod-shaped elongated cells", "Spiral comma-shaped filaments", "Irregular amoeboid shape"]),
        ("Clostridium tetani is an obligate anaerobic bacterium that causes which disease in humans?", "Tetanus (lockjaw)", ["Cholera", "Tuberculosis", "Typhoid"]),
        ("How do organisms of Kingdom Monera reproduce under favorable environmental conditions?", "Asexual binary fission (simple cell division)", ["Sexual reproduction by gamete fusion", "Spore formation via meiosis", "Seed germination"]),
        ("Which bacterium causes Asiatic cholera and has a comma-shaped (vibrio) morphology?", "Vibrio cholerae", ["Treponema pallidum", "Streptococcus", "Rhizobium"]),
        ("Why are Monerans described as prokaryotic?", "Because 'pro' means primitive/before and 'karyon' means nucleus (no true nuclear envelope)", ["Because they have true nuclei", "Because they cannot move", "Because they live only in soil"]),
        ("Can bacteria belonging to Monera live in extreme conditions such as hot springs and deep ocean vents?", "Yes, many archaebacteria and extremophiles thrive in extreme environments", ["No, bacteria only survive between 20°C and 30°C", "No, oxygen is strictly mandatory for all bacteria", "No, they only survive inside human intestines"])
    ]
    for i in range(80):
        ctx, ans, wrongs = monera_q[i % len(monera_q)]
        q = make_q(
            tc_121, name_121,
            f"Kingdom Monera Biology: {ctx}",
            ans, wrongs,
            "Kingdom Monera encompasses all bacteria and blue-green algae (cyanobacteria).",
            "They are unicellular prokaryotes lacking a well-defined nucleus and membrane-bound cell organelles.",
            f"Therefore, '{ans}' is the correct statement.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 1.2.2 Protista: unicellular eukaryotes (80 questions)
    # -------------------------------------------------------------
    tc_122 = "MH-8-SCI-1-1.2.2"
    name_122 = "Protista: unicellular eukaryotes with pseudopodia/cilia (Amoeba, Euglena)"
    protista_q = [
        ("What locomotory organelle is utilized by Amoeba for locomotion and capturing food particles?", "Pseudopodia (false feet)", ["Cilia", "Flagella", "Tentacles"]),
        ("Which organelle is used by Paramoecium for swimming through aquatic media?", "Cilia (hair-like projections covering the entire cell surface)", ["Pseudopodia", "A single whip-like flagellum", "Muscular foot"]),
        ("Euglena is unique among unicellular protists because it contains which organelle?", "Chloroplasts (for autotrophic photosynthesis in light)", ["Chitin cell wall", "Peptidoglycan capsule", "True roots and leaves"]),
        ("What is the locomotory organelle found in Euglena?", "A long whip-like flagellum", ["Pseudopodia", "Rows of thousands of cilia", "Slime gliding layer"]),
        ("Under which kingdom are unicellular protozoans with well-defined nuclear membranes classified?", "Kingdom Protista", ["Kingdom Monera", "Kingdom Fungi", "Kingdom Plantae"]),
        ("Entamoeba histolytica is a parasitic protist that causes which intestinal ailment?", "Amoebic dysentery (amoebiasis)", ["Malaria", "Sleeping sickness", "Tetanus"]),
        ("Plasmodium vivax, which causes malaria in humans, belongs to which biological group?", "Protozoan protists", ["Kingdom Monera (bacteria)", "Fungi", "Viruses"]),
        ("How does Amoeba engulf food particles during phagocytosis?", "By extending pseudopodia around the food particle to form a food vacuole", ["By filtering through gills", "By photosynthesizing glucose", "By absorbing nutrients via roots"])
    ]
    for i in range(80):
        ctx, ans, wrongs = protista_q[i % len(protista_q)]
        q = make_q(
            tc_122, name_122,
            f"Kingdom Protista Biology: {ctx}",
            ans, wrongs,
            "Kingdom Protista includes single-celled eukaryotic organisms possessing a well-defined nucleus enveloped by a nuclear membrane.",
            "They possess distinct locomotory organelles like pseudopodia, cilia, or flagella.",
            f"Hence, '{ans}' is the accurate fact.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 1.2.3 Fungi: saprophytic eukaryotes (80 questions)
    # -------------------------------------------------------------
    tc_123 = "MH-8-SCI-1-1.2.3"
    name_123 = "Fungi: saprophytic eukaryotes with chitin cell wall (Aspergillus, Penicillium, Yeast)"
    fungi_q = [
        ("The cell wall of fungi is composed of which complex and tough nitrogenous polysaccharide?", "Chitin", ["Cellulose", "Peptidoglycan", "Pectin"]),
        ("What is the primary mode of nutrition demonstrated by fungi like Aspergillus and mushrooms?", "Saprophytic (absorbing nutrients from dead, decaying organic matter)", ["Autotrophic photosynthesis", "Holozoic animal-like ingestion", "Chemosynthetic oxidation"]),
        ("Which of the following is a UNICELLULAR fungus widely used in bread making and alcohol fermentation?", "Yeast (Saccharomyces cerevisiae)", ["Aspergillus", "Penicillium", "Agaricus (Mushroom)"]),
        ("From which fungus was the first modern life-saving antibiotic, penicillin, extracted by Sir Alexander Fleming?", "Penicillium notatum", ["Aspergillus niger", "Rhizopus stolonifer", "Yeast"]),
        ("The thread-like, branched vegetative filaments that constitute the body of a multicellular fungus are called:", "Hyphae (collectively called mycelium)", ["Pseudopodia", "Flagella", "Rhizoids of mosses"]),
        ("Black fungus or mould growing on stale bread or pickles is scientifically identified as:", "Rhizopus / Mucor", ["Euglena", "Lactobacillus", "Paramoecium"]),
        ("Why are fungi unable to manufacture their own food through photosynthesis?", "They lack chlorophyll pigments completely", ["Their cell wall blocks all sunlight", "They lack cell nuclei", "They are strictly anaerobic"]),
        ("Which fungus is commercially cultivated worldwide as an edible, protein-rich culinary delicacy?", "Agaricus (Button Mushroom)", ["Aspergillus", "Penicillium", "Clostridium"])
    ]
    for i in range(80):
        ctx, ans, wrongs = fungi_q[i % len(fungi_q)]
        q = make_q(
            tc_123, name_123,
            f"Kingdom Fungi Biology: {ctx}",
            ans, wrongs,
            "Fungi are non-green, eukaryotic, heterotrophic organisms that feed saprophytically on decaying matter.",
            "Their cell walls are made of a tough nitrogenous polymer called chitin.",
            f"Thus, '{ans}' is the correct answer.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 1.3.1 Size hierarchy in micrometres and nanometres (80 questions)
    # -------------------------------------------------------------
    tc_131 = "MH-8-SCI-1-1.3.1"
    name_131 = "Size hierarchy in micrometres and nanometres"
    sizes_q = [
        ("How many micrometres (\\(\\mu\\text{m}\\)) are in 1 metre (\\(1\\text{ m}\\))?", "\\(10^6\\,\\mu\\text{m}\\) (one million micrometres)", ["\\(10^3\\,\\mu\\text{m}\\)", "\\(10^9\\,\\mu\\text{m}\\)", "\\(10^{12}\\,\\mu\\text{m}\\)"]),
        ("How many nanometres (\\(\\text{nm}\\)) are in 1 metre (\\(1\\text{ m}\\))?", "\\(10^9\\text{ nm}\\) (one billion nanometres)", ["\\(10^6\\text{ nm}\\)", "\\(10^{12}\\text{ nm}\\)", "\\(10^3\\text{ nm}\\)"]),
        ("How many nanometres (\\(\\text{nm}\\)) are equal to 1 micrometre (\\(1\\,\\mu\\text{m}\\))?", "\\(1000\\text{ nm}\\)", ["\\(100\\text{ nm}\\)", "\\(10\\text{ nm}\\)", "\\(10000\\text{ nm}\\)"]),
        ("What is the typical average size range of bacteria in biological microscopy?", "1 to 10 micrometres (\\(1\\text{ to } 10\\,\\mu\\text{m}\\))", ["10 to 100 nanometres", "1 to 10 millimetres", "100 to 500 micrometres"]),
        ("What is the typical size range of viruses, making them visible only under an electron microscope?", "10 to 100 nanometres (\\(10\\text{ to } 100\\text{ nm}\\))", ["1 to 10 micrometres", "10 to 50 micrometres", "1 to 2 millimetres"]),
        ("What is the typical approximate size range of single-celled protozoa like Amoeba?", "Around 200 micrometres (\\(200\\,\\mu\\text{m}\\))", ["10 nanometres", "100 nanometres", "1 metre"]),
        ("Which microscopic tool is essential to resolve and photograph internal structures of viruses at nanometre scale?", "Electron microscope", ["Compound light microscope", "Simple magnifying hand lens", "Dissecting stereo microscope"]),
        ("In the microscopic size hierarchy, which organism is significantly SMALLER than bacteria?", "Viruses (10–100 nm vs bacteria 1–10 μm)", ["Protozoa (200 μm)", "Unicellular fungi (yeast 10–100 μm)", "Microscopic algae (10–100 μm)"])
    ]
    for i in range(80):
        ctx, ans, wrongs = sizes_q[i % len(sizes_q)]
        q = make_q(
            tc_131, name_131,
            f"Microbial Metrology: {ctx}",
            ans, wrongs,
            "Microscopic organisms are measured using micrometres (μm) and nanometres (nm).",
            "1 metre = 10⁶ μm = 10⁹ nm; hence 1 μm = 1000 nm. Viruses (10–100 nm) are 10 to 100 times smaller than bacteria (1–10 μm).",
            f"Therefore, '{ans}' is the precise measurement value.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 1.3.2 Bacteria shapes (coccus, bacillus, spirillum) (80 questions)
    # -------------------------------------------------------------
    tc_132 = "MH-8-SCI-1-1.3.2"
    name_132 = "Bacteria shapes (coccus, bacillus, spirillum)"
    shapes_q = [
        ("What is the spherical or round shaped bacterium called in biological nomenclature?", "Coccus", ["Bacillus", "Spirillum", "Vibrio"]),
        ("What is the rod-shaped bacterium called in microbiological classification?", "Bacillus", ["Coccus", "Spirillum", "Vibrio"]),
        ("What is the comma-shaped bacterium called in bacterial taxonomy?", "Vibrio (e.g., Vibrio cholerae)", ["Bacillus", "Coccus", "Spirillum"]),
        ("What is the spiral or corkscrew-shaped bacterium called?", "Spirillum", ["Coccus", "Bacillus", "Vibrio"]),
        ("Lactobacillus, found in yogurt and curd, belongs to which morphological shape of bacteria?", "Bacillus (rod-shaped)", ["Coccus (spherical)", "Vibrio (comma-shaped)", "Spirillum (spiral)"]),
        ("Bacteria appearing as spherical cells joined together in pairs are designated as:", "Diplococcus", ["Streptobacillus", "Spirillum", "Vibrio"]),
        ("Which bacterial shape does Salmonella typhi (the causative agent of typhoid) exhibit?", "Bacillus (rod-shaped)", ["Coccus", "Vibrio", "Spirillum"]),
        ("Treponema pallidum, a bacterium with a wavy coiled helical form, is an example of:", "Spirillum", ["Coccus", "Bacillus", "Vibrio"])
    ]
    for i in range(80):
        ctx, ans, wrongs = shapes_q[i % len(shapes_q)]
        q = make_q(
            tc_132, name_132,
            f"Bacterial Morphology: {ctx}",
            ans, wrongs,
            "Bacteria are classified morphologically into four fundamental shapes: Coccus (spherical), Bacillus (rod-shaped), Vibrio (comma-shaped), and Spirillum (spiral).",
            "These structural forms are determined by rigid peptidoglycan cell walls.",
            f"Therefore, the correct identification is '{ans}'.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 1.3.3 Protozoa free living and parasitic (80 questions)
    # -------------------------------------------------------------
    tc_133 = "MH-8-SCI-1-1.3.3"
    name_133 = "Protozoa free living and parasitic (Plasmodium, Entamoeba)"
    proto_q = [
        ("Where are free-living protozoans like Amoeba and Paramoecium commonly found?", "Fresh water, dirty pond water, and moist soil", ["Exclusively in volcanic vents", "Only inside human blood cells", "Exclusively on dry desert sand"]),
        ("Which parasitic protozoan is the pathogen causing malaria in humans?", "Plasmodium vivax", ["Entamoeba histolytica", "Amoeba proteus", "Paramoecium caudatum"]),
        ("Which insect vector transmits the protozoan parasite Plasmodium vivax between human hosts?", "Female Anopheles mosquito", ["Male Anopheles mosquito", "Female Aedes mosquito", "Housefly (Musca domestica)"]),
        ("Entamoeba histolytica inhabits which organ of the human body as an endoparasite?", "Large intestine", ["Lungs", "Red blood cells", "Kidneys"]),
        ("What is the primary symptom of amoebic dysentery caused by Entamoeba histolytica?", "Frequent severe diarrhoea with mucus and blood in stools", ["High body fever with respiratory cough", "Muscle paralysis of legs", "Joint swelling"]),
        ("How does the slipper-shaped Paramoecium obtain its microscopic food particles?", "Through an oral groove (cytostome) lined with beating cilia", ["Through photosynthesis using chloroplasts", "By absorbing minerals from dry rocks", "By parasitic suction of blood"]),
        ("Why are protozoa described as eukaryotic rather than prokaryotic?", "Because they possess a true nucleus bounded by a nuclear envelope", ["Because they lack DNA", "Because they have no cytoplasm", "Because they reproduce only sexually"]),
        ("In the life cycle of Plasmodium, in which cells of the human host does the parasite first multiply?", "Liver cells (hepatocytes), followed by red blood cells (erythrocytes)", ["Neurons in the brain", "Bone marrow only", "Stomach epithelial cells"])
    ]
    for i in range(80):
        ctx, ans, wrongs = proto_q[i % len(proto_q)]
        q = make_q(
            tc_133, name_133,
            f"Protozoan Biology: {ctx}",
            ans, wrongs,
            "Protozoa are single-celled eukaryotic microorganisms that can be free-living in aquatic environments or parasitic in hosts.",
            "Parasitic forms like Plasmodium (malaria) and Entamoeba (amoebic dysentery) cause major infectious diseases.",
            f"Thus, the correct fact is '{ans}'.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 1.3.4 Algae autotrophs with chloroplast (80 questions)
    # -------------------------------------------------------------
    tc_134 = "MH-8-SCI-1-1.3.4"
    name_134 = "Algae autotrophs with chloroplast (Chlorella)"
    algae_q = [
        ("Which green pigment enables algae like Chlorella to perform photosynthesis?", "Chlorophyll", ["Haemoglobin", "Melanin", "Anthocyanin"]),
        ("Which of the following is a UNICELLULAR green alga rich in proteins and studied for space nutrition?", "Chlorella", ["Spirogyra", "Ulva", "Sargassum"]),
        ("In which habitat do the vast majority of microscopic and macroscopic algae reside?", "Aquatic habitats (fresh water and marine oceans)", ["Deep underground mines", "Human digestive tract", "Dry sand dunes"]),
        ("Algae are ecologically vital to life on Earth because they produce huge quantities of:", "Oxygen (via photosynthetic carbon assimilation)", ["Carbon monoxide", "Methane gas", "Ammonia gas"]),
        ("Which filamentous multicellular green alga is famous for having ribbon-like spiral chloroplasts?", "Spirogyra", ["Chlamydomonas", "Chlorella", "Amoeba"]),
        ("Unlike land plants, microscopic algae lack which specialized structural organs?", "True roots, stems, leaves, and vascular tissues (xylem and phloem)", ["Cell walls and nuclei", "Chloroplasts", "Cytoplasm and cell membranes"]),
        ("What is the stored food reserve synthesized by green algae through photosynthesis?", "Starch", ["Glycogen", "Chitin", "Keratin"]),
        ("Under Whittaker's classification, where are unicellular microscopic algae like Chlamydomonas and Chlorella placed?", "Kingdom Protista", ["Kingdom Monera", "Kingdom Fungi", "Kingdom Animalia"])
    ]
    for i in range(80):
        ctx, ans, wrongs = algae_q[i % len(algae_q)]
        q = make_q(
            tc_134, name_134,
            f"Algal Biology: {ctx}",
            ans, wrongs,
            "Algae are aquatic, eukaryotic autotrophs that carry out photosynthesis using chloroplasts.",
            "Unicellular algae like Chlorella synthesize organic nutrients and release dissolved oxygen into ecosystems.",
            f"Hence, '{ans}' is the correct statement.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 1.4.1 Submicroscopic size (10 to 100 nm) (80 questions)
    # -------------------------------------------------------------
    tc_141 = "MH-8-SCI-1-1.4.1"
    name_141 = "Submicroscopic size (10 to 100 nm)"
    vir_size_q = [
        ("Why are viruses termed 'submicroscopic' entities in biology?", "Because their minute size (10–100 nm) is below the resolving power of compound optical microscopes", ["Because they live underwater only", "Because they can be seen with naked human eyes", "Because they are larger than plant cells"]),
        ("What is the approximate size range of typical virus particles?", "10 to 100 nanometres (\\(10\\text{ to } 100\\text{ nm}\\))", ["1 to 10 micrometres", "100 to 500 micrometres", "1 to 5 millimetres"]),
        ("Why can viruses pass through bacterial proof filters (Chamberland filters)?", "Because viruses are 10 to 100 times smaller than bacteria", ["Because viruses dissolve the filter", "Because bacterial filters have giant holes", "Because viruses are gaseous"]),
        ("Which advanced scientific instrument was invented in the 1930s that first allowed direct imaging of virus particles?", "Transmission Electron Microscope (TEM)", ["Galilean telescope", "Standard classroom compound light microscope", "Magnifying prism"]),
        ("How many times smaller is a 10 nm virus compared to a 1 μm bacterium?", "100 times smaller (\\(1000\\text{ nm} \\div 10\\text{ nm} = 100\\))", ["10 times smaller", "2 times smaller", "1000 times smaller"]),
        ("Are viruses classified under any of Robert Whittaker's five kingdoms of living organisms?", "No, because they are non-cellular borderline entities lacking cellular metabolic machinery", ["Yes, in Kingdom Monera", "Yes, in Kingdom Protista", "Yes, in Kingdom Fungi"]),
        ("Outside a living host cell, in what state do virus particles exist?", "Inert crystalline non-living macromolecules (virions)", ["Active reproducing bacteria", "Swimming flagellated cells", "Photosynthesizing spores"]),
        ("Why do antibiotics (such as penicillin) fail completely against viral infections like influenza or common cold?", "Because antibiotics target bacterial cell walls/metabolism, which viruses do not have", ["Because viral particles are too large", "Because viruses consume antibiotics as food", "Because antibiotics only work on human blood"])
    ]
    for i in range(80):
        ctx, ans, wrongs = vir_size_q[i % len(vir_size_q)]
        q = make_q(
            tc_141, name_141,
            f"Viral Metrology & Nature: {ctx}",
            ans, wrongs,
            "Viruses are submicroscopic obligate parasites ranging from 10 to 100 nm in diameter.",
            "They are acellular entities on the threshold of the living and non-living, requiring host cellular machinery to replicate.",
            f"Therefore, '{ans}' is the correct answer.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 1.4.2 DNA or RNA genome surrounded by protein coat (80 questions)
    # -------------------------------------------------------------
    tc_142 = "MH-8-SCI-1-1.4.2"
    name_142 = "DNA or RNA genome surrounded by protein coat"
    vir_struct_q = [
        ("What is the protective protein shell that encapsulates the viral genetic material called?", "Capsid", ["Cell wall", "Capsule", "Cytoplasmic membrane"]),
        ("What genetic material is contained inside a virus particle?", "Either DNA or RNA (never both together in the same virus)", ["Both DNA and RNA simultaneously in equal amounts", "Only proteins without nucleic acid", "Neither DNA nor RNA"]),
        ("The individual protein subunits that assemble to form the viral capsid are known as:", "Capsomeres", ["Peptidoglycans", "Chitin molecules", "Phospholipids"]),
        ("HIV (Human Immunodeficiency Virus) and SARS-CoV-2 contain which type of genetic material?", "Single-stranded RNA", ["Double-stranded DNA only", "Triple-stranded protein", "Cellulose"]),
        ("Once a virus attaches to a host cell and injects its nucleic acid, what happens next?", "The viral genome hijacks the host cell's machinery to synthesize viral components", ["The host cell digests the virus as nutrient", "The virus creates a bacterial spore", "The virus photosynthesizes glucose"]),
        ("What happens to the host cell when numerous newly assembled viruses burst out at the end of the lytic cycle?", "The host cell undergoes lysis (ruptures and dies)", ["The host cell divides by binary fission", "The host cell grows larger indefinitely", "The host cell turns into a plant"]),
        ("Why are viruses referred to as 'obligate intracellular parasites'?", "Because they cannot reproduce or metabolize outside a living host cell", ["Because they live only in soil", "Because they can survive on artificial nutrient agar", "Because they eat human food"]),
        ("Smallpox virus and Hepatitis B virus are examples of viruses containing which genetic core?", "DNA genome", ["RNA only", "Cellulose fibers", "Lipid bilayer only"])
    ]
    for i in range(80):
        ctx, ans, wrongs = vir_struct_q[i % len(vir_struct_q)]
        q = make_q(
            tc_142, name_142,
            f"Viral Structure: {ctx}",
            ans, wrongs,
            "A virus is composed of a core genome (either DNA or RNA, never both) enclosed in a protective protein coat called a capsid.",
            "Lacking ribosomes and metabolic enzymes, it relies entirely on host machinery for replication.",
            f"Hence, '{ans}' is the scientifically accurate fact.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 1.4.3 Bacteriophage and plant/animal viruses (80 questions)
    # -------------------------------------------------------------
    tc_143 = "MH-8-SCI-1-1.4.3"
    name_143 = "Bacteriophage and plant/animal viruses"
    phage_q = [
        ("What is a virus that specifically infects and destroys bacteria called?", "Bacteriophage", ["Viroid", "Prion", "Mycophage"]),
        ("Which structural part of a bacteriophage attaches to the bacterial cell wall during infection?", "Tail fibers / base plate", ["Icosahedral head only", "Nuclear membrane", "Cilia"]),
        ("Tobacco Mosaic Virus (TMV) is an example of a virus that infects:", "Plants (causing mottled discoloration of leaves)", ["Human lungs", "Bacterial cells", "Cattle and livestock"]),
        ("Foot-and-Mouth Disease (FMD) is a contagious viral illness affecting which category of hosts?", "Animals (cattle, buffaloes, swine, and sheep)", ["Cereal crops like wheat", "Aquatic algae", "Soil bacteria"]),
        ("Which virus causes acute respiratory syndrome, influenza, and the common cold in humans?", "Human respiratory viruses (e.g. Influenza virus, Rhinovirus)", ["Bacteriophage T4", "Tobacco Mosaic Virus", "Potato virus X"]),
        ("Polio virus and Hepatitis virus are human pathogens categorized under:", "Animal / Human viruses", ["Bacteriophages", "Plant viruses", "Beneficial bacterial symbionts"]),
        ("Why were bacteriophages historically called 'bacteria-eaters'?", "Because they lyse (dissolve and kill) bacterial colonies rapidly", ["Because they are large bacteria", "Because they eat food inside human stomach", "Because they live in soil"]),
        ("Tomato spotted wilt virus and Papaya ring spot virus cause severe economic damage to which sector?", "Agriculture and horticulture (plant farming)", ["Automobile manufacturing", "Dairy processing", "Textile spinning"])
    ]
    for i in range(80):
        ctx, ans, wrongs = phage_q[i % len(phage_q)]
        q = make_q(
            tc_143, name_143,
            f"Viral Host Specificity: {ctx}",
            ans, wrongs,
            "Viruses exhibit high host specificity: bacteriophages infect bacteria, plant viruses infect plant tissues, and animal viruses infect animal/human hosts.",
            "Bacteriophages like T4 infect bacterial cells by injecting their genetic material.",
            f"Therefore, '{ans}' is the correct response.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch1_questions()
    print(f"Generated {len(qs)} questions for Chapter 1.")
    out_path = "scripts/mh8_sci_ch1_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
