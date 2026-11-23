import json


def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        'Uncontrolled biological variation',
        'Non-cellular spontaneous crystallization',
        'Artifact of optical distortion'
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
                "boardCode": "CBSE",
                "class": "9",
                "subjectCode": "SCIE",
                "chapterNumber": 2,
                "vault": vault,
                "type": "OSC"
            })
            q_seq += 1

    return questions


# ==============================================================================
# SUBTOPIC 2.1.1: Robert Hooke cork cells (1665)
# Topic Code: CBSE-9-SCIE-2-2.1.1
# ==============================================================================
def gen_2_1_1():
    # Arch 1: Historical Discovery by Robert Hooke (1665)
    arch1 = {
        'data': [
            ("1665", "Robert Hooke", "Thin slice of bottle cork (bark of Quercus suber)", "Honeycomb-like structure consisting of empty box-like compartments"),
            ("Micrographia", "Robert Hooke", "First published scientific treatise illustrating microscopic observations in 1665", "Coined the biological term 'cell' from the Latin 'cellula' (little room)"),
            ("Self-designed primitive compound microscope", "Robert Hooke", "Used an oil lamp and water flask as a light condenser to illuminate opaque cork slices", "Observed dead plant cell walls enclosing air spaces"),
            ("Cellulae (Little Rooms)", "Latin word 'cellula' meaning a small monastery chamber or room", "Applied by Hooke to the polygonal pores seen in cork", "Hooke actually saw empty dead plant cell walls without cytoplasm"),
            ("Spanish oak / Cork oak (Quercus suber)", "Tree bark from which commercial bottle cork is derived", "Dead protective secondary tissue (phellem)", "Cells are dead at maturity, suberized, and filled with air"),
            ("Biological significance of Hooke's 1665 observation", "First demonstration that living matter is divided into distinct discrete structural units", "Marked the beginning of cytology and cellular biology", "Limited because Hooke only observed non-living cell walls without living protoplasm"),
            ("Physical appearance of cork under Hooke's microscope", "Network of tiny, empty hexagonal or polygonal compartments resembling a honeycomb", "Perforated with tiny pores surrounded by thick cellulose-suberin walls", "Contained no living fluid, nucleus, or organelles"),
            ("Illumination technique used by Robert Hooke", "Oil lamp flame focused through a spherical glass water reservoir", "Functioned as a makeshift optical condensing lens to concentrate light on the opaque specimen", "Allowed reflection-based viewing before modern substage condensers were invented"),
            ("Year of publication of Hooke's landmark work 'Micrographia'", "1665", "Published under the auspices of the Royal Society of London", "Contained exquisite copperplate engravings of insects and cork cells"),
            ("Nature of cells observed in cork", "Dead plant cells consisting purely of rigid cell walls enclosing empty spaces", "Lacked cytoplasm, plasma membrane, and nucleus", "Formed as part of bark to provide insulation and water impermeability to trees")
        ],
        'templates': [
            "In the history of cell biology, '{0}' refers to: {1}. Which of the following is the accurate scientific fact?:",
            "What historical milestone is associated with '{0}' in the study of cell discovery?:",
            "Regarding Robert Hooke's 1665 discovery: '{0}'. The correct biological description is:",
            "How did Robert Hooke in '{0}' contribute fundamentally to the foundation of cytology?:",
            "Which statement accurately explains the observation of '{0}' made by Robert Hooke?:",
            "In '{0}', Robert Hooke examined cork and concluded that:",
            "What did Robert Hooke actually visualize when studying '{0}' in 1665?:",
            "Identify the accurate historical and biological detail regarding '{0}':",
            "Hooke's classic 1665 experiment with '{0}' is scientifically significant because:",
            "In 1665, Robert Hooke observed '{0}'. What was the structural reality of what he saw?:"
        ],
        'calc': lambda item: (
            item[3],
            [
                "Hooke observed living amoebae swimming inside fresh spring water",
                "Hooke observed animal cells undergoing active mitotic cell division",
                "Hooke discovered the cell nucleus and named chromatin fibers"
            ],
            f"**Step 1: Understand Robert Hooke's 1665 landmark discovery.**\nIn 1665, British natural philosopher Robert Hooke examined a thin slice of bottle cork under his self-designed compound microscope and published his observations in *Micrographia*.\n\n**Step 2: Nature of the specimen.**\nCork is the dead outer bark of the cork oak (*Quercus suber*). Hooke saw empty hexagonal compartments ({item[3]}).\n\n**Step 3: Etymology:**\nHe named them **cells** from the Latin *cellula* ('little rooms')."
        ),
        'diff': 'easy'
    }

    # Arch 2: Nature of Cork Cells - Suberization and Dead Protective Tissue
    arch2 = {
        'data': [
            ("Chemical substance deposited in the walls of mature cork cells", "Suberin", "A complex waxy waterproof lipid polymer that makes cork walls impermeable to water and gases", "Lignin, Pectin, Chitin"),
            ("State of living matter inside mature cork cells", "Dead at maturity, lacking protoplasm and nucleus", "The protoplasm degenerates during maturation, leaving hollow air-filled compartments", "Actively dividing with dense cytoplasm, Highly photosynthetic with chloroplasts, Amoeboid and motile"),
            ("Primary physiological function of cork (phellem) in woody plants", "Protection against mechanical injury, desiccation (water loss), and infection by pathogens", "Forms a tough outer insulating layer around mature stems and roots", "Food conduction and phloem translocation, Water absorption from the soil, Rapid vegetative multiplication"),
            ("Gaseous exchange pores present across cork bark layers", "Lenticels", "Loosely arranged non-suberized complementary cells allowing gas diffusion across impermeable phellem", "Stomata, Hydathodes, Plasmodesmata"),
            ("Meristematic tissue responsible for producing cork cells in dicot stems", "Cork cambium (Phellogen)", "A lateral secondary meristem that divides to form phellem (cork) externally and phelloderm internally", "Apical meristem, Vascular cambium, Intercalary meristem"),
            ("Why cork is highly buoyant and a superior thermal insulator", "Because mature cork cells are hollow, tightly packed, and filled with trapped air", "Low density combined with suberin-lined waterproof walls", "Because cork contains large amounts of heavy metallic crystals, Because cork cells are filled with liquid sap, Because cork absorbs huge amounts of nitrogen gas"),
            ("Arrangement of cork cells in plant bark", "Compactly arranged in radial rows without intercellular spaces", "Creates an unbroken protective seal preventing moisture leakage", "Loosely scattered with large air gaps, Arranged in concentric fluid rings, Spiral coils with flagella"),
            ("Why Robert Hooke did NOT observe cytoplasm or nucleus in cork", "Because cork cells are dead plant structures whose living contents have vanished, leaving only cell walls", "Living components had decomposed before commercial cork harvesting", "Because the microscope was not plugged into electricity, Because plant cells never contain cytoplasm, Because Hooke used a blue light filter"),
            ("Periderm structure in woody plants", "Collective name for Phellogen (cork cambium), Phellem (cork), and Phelloderm (secondary cortex)", "Replaces the ruptured epidermis during secondary growth in stems and roots", "Epidermis, Cuticle, and Stomata; Xylem, Phloem, and Cambium; Cortex, Endodermis, and Pericycle"),
            ("Industrial property of cork derived from cell wall suberin", "Elasticity, compressibility, and complete impermeability to liquids and gases", "Makes it an ideal material for wine bottle stoppers, gasket seals, and bulletin boards", "High electrical conductivity, Extreme water solubility, Rapid chemical combustibility in water")
        ],
        'templates': [
            "In plant histology and cell biology: '{0}'. What is the correct scientific fact?:",
            "Regarding the structure and chemistry of cork cells: '{0}' is characterized as:",
            "What biological feature explains: '{0}'?:",
            "In studying Hooke's cork cells: '{0}' refers to:",
            "Which of the following is the accurate botanical explanation for: '{0}'?:",
            "Why is '{0}' significant in understanding the properties of cork tissue?:",
            "Identify the correct biological mechanism or component for: '{0}':",
            "In plant secondary growth: '{0}' is accurately described as:",
            "A biology practical examines cork tissue: '{0}'. The student must state that:",
            "Which statement correctly accounts for: '{0}'?:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand the botanical properties of cork.**\nCork (phellem) is formed by the cork cambium (phellogen) during secondary growth.\n\n**Step 2: Key traits of mature cork.**\n- Dead at maturity (no living protoplast).\n- Cell walls impregnated with **{item[1]}** ({item[2]}).\n\n**Step 3: Functional role:**\nProvides an impermeable, protective, and insulating barrier for woody plants."
        ),
        'diff': 'medium'
    }

    # Arch 3: Comparison of Hooke's Compound Microscope vs Modern Light Microscope
    arch3 = {
        'data': [
            ("Magnification power of Robert Hooke's primitive compound microscope", "Approximately 30x to 50x magnification", "Sufficient to resolve the 20-30 μm outlines of cork cell walls but unable to resolve subcellular organelles", "1000x to 2000x magnification, 50,000x magnification, Exactly 5x magnification"),
            ("Major optical defect present in Robert Hooke's early lenses", "Severe chromatic aberration and spherical aberration", "Single glass lenses bent different light wavelengths differently, producing blurred rainbow-colored halos around objects", "Total internal reflection failure, Zero light transmission, High electron scattering"),
            ("Illumination source utilized in Hooke's compound microscope", "An oil lamp flame focused through a spherical glass flask filled with water", "Concentrated light onto the opaque specimen from above (incident / epi-illumination)", "Substage electric LED lamp with iris diaphragm, Laser diode beam, Reflected moonlight"),
            ("Modern compound light microscope magnification limit", "Approximately 1000x to 1500x magnification with a resolution limit of ~0.2 micrometres (200 nm)", "Limited by the wave nature (diffraction limit) of visible light wavelengths (~400-700 nm)", "100,000x magnification, Unlimited resolution capable of visualizing individual atoms, 50x magnification"),
            ("Definition of 'Resolution' in microscopy", "The minimum distance between two distinct points at which they can still be distinguished as separate entities", "Determines image sharpness and clarity; higher resolution reveals finer microscopic detail", "The degree by which an object appears enlarged, The brightness of the light source, The size of the glass stage"),
            ("Difference between Magnification and Resolution", "Magnification makes an object appear larger; Resolution resolves fine detail and separates adjacent points", "High magnification without sufficient resolution produces an empty, blurred image ('empty magnification')", "Magnification and resolution are identical synonyms, Magnification refers to color while resolution refers to size, Resolution is only used in digital screens"),
            ("Role of the condenser lens in a modern compound microscope", "Gathers and focuses light rays from the illuminator uniformly onto the specimen on the stage", "Ensures optimal contrast, resolution, and illumination across the field of view", "Magnifies the image formed by the objective lens, Inverts the image upside down, Blocks ultraviolet light"),
            ("Standard objective lenses on a modern secondary school microscope", "Scanning (4x), Low power (10x), High dry power (40x), and Oil immersion (100x)", "Total magnification = Eyepiece magnification (typically 10x) multiplied by Objective magnification", "1x, 2x, 3x, and 4x lenses; 100x, 200x, 300x lenses; Only a single fixed 10x lens"),
            ("Why immersion oil is used with the 100x high-power objective lens", "Immersion oil has the same refractive index as glass (n ≈ 1.515), preventing light refraction and loss at glass-air interfaces", "Increases numerical aperture (NA) and maximizes resolution of fine bacterial and cellular structures", "It lubricates the lens to slide across the slide, It stains the cells blue instantly, It acts as a disinfectant against viruses"),
            ("Electron Microscope resolution advantage over Light Microscope", "Electron beams have wavelengths ~100,000 times shorter than visible light photons (de Broglie wavelength)", "Achieves resolutions down to 0.1 to 0.2 nanometres, revealing ultrastructure of membranes, ribosomes, and DNA", "Electrons are cheaper than light, Electron microscopes can view live swimming organisms in air, Light microscopes can only view dead metal objects")
        ],
        'templates': [
            "In optical physics and microscopy: '{0}'. What is the correct scientific description?:",
            "How does the historical microscope of Robert Hooke compare with modern systems regarding: '{0}'?:",
            "What is the optical significance of '{0}' in microscopy?:",
            "A student examines a microscope and learns about '{0}'. The accurate principle is:",
            "Explain the physical and optical basis of: '{0}':",
            "In practical cell biology, '{0}' is characterized by:",
            "Which statement correctly defines and evaluates: '{0}'?:",
            "Regarding microscope performance: '{0}' refers to:",
            "Why is '{0}' critical in modern cellular observations?:",
            "Analyze the microscopy concept: '{0}'. The scientifically valid explanation is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand microscope optical principles.**\n- **Hooke's microscope:** Compound optical system with ~30x–50x magnification, plagued by chromatic aberration.\n- **Modern light microscope:** Resolves up to 200 nm (1500x).\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Temporary Mount Preparation: Onion Peel Epidermal Cells Practical
    arch4 = {
        'data': [
            ("Stain commonly used to mount onion peel epidermal cells in school laboratories", "Safranin solution (or Dilute Iodine solution)", "Stains nuclei deep red/pink and cell walls distinctly for clear contrast under brightfield illumination", "Methylene blue, Crystal violet, Leishman stain"),
            ("Mounting medium used when placing the coverslip over the stained onion peel", "Glycerine (Glycerol)", "Prevents the biological specimen from drying out, provides optical clearing, and has a refractive index close to glass", "Concentrated sulfuric acid, Absolute alcohol, Boiling water"),
            ("Correct technique for lowering a glass coverslip onto the slide", "Hold coverslip at a 45° angle with a needle and lower it gently to prevent trapping air bubbles", "Trapped air bubbles appear as circular dark rings with thick black borders that obstruct viewing", "Drop it vertically from 10 cm height, Press it down hard with a thumb, Slide it rapidly back and forth"),
            ("Appearance of air bubbles under a light microscope compared to cells", "Perfect circles with thick, dark black borders and bright centers that move when pressed", "Do not possess cell walls, nuclei, or biological texture", "Hexagonal cells with prominent red nuclei, Granular green chloroplasts, Thread-like chromosomes"),
            ("Why an onion epidermal peel is ideal for studying plant cell architecture", "It is a single, transparent, monolayer sheet of cells that requires no difficult section-cutting", "Allows light to transmit directly through without overlapping cell layers", "Because onion cells are completely spherical, Because onion cells have no cell walls, Because onion cells lack nuclei"),
            ("Visible structures under low and high power in stained onion peel cells", "Cell wall, plasma membrane, large central vacuole, cytoplasm, and prominent nucleus located peripherally", "Chloroplasts are absent because onion bulb scales are underground non-photosynthetic storage leaves", "Centrioles and lysosomes; Chloroplasts and pseudopodia; Flagella and cilia"),
            ("Why onion peel cells lack chloroplasts", "Onion bulbs grow underground in the dark and function as modified food storage leaves (tunic)", "Chloroplast development requires light exposure; underground scale leaves contain colorless amyloplasts/leucoplasts", "Because monocot plants never possess chloroplasts, Because cell walls destroy chloroplasts, Because safranin dissolves chlorophyll"),
            ("Function of blotting paper during temporary mount slide preparation", "Absorbs excess stain and glycerine seeping out from under the edges of the coverslip", "Keeps the top of the coverslip clean and prevents liquid from dirtying microscope objective lenses", "Stains the specimen brown, Glues the coverslip permanently, Dissolves air bubbles chemically"),
            ("Shape and arrangement of onion peel epidermal cells", "Elongated, rectangular cells packed compactly end-to-end like bricks in a wall without intercellular spaces", "Provides mechanical protection and containment for underlying fleshy storage tissues", "Round loose cells with large gaps, Star-shaped cells with long dendrites, Spindle-shaped motile cells"),
            ("Position of the nucleus in mature plant cells such as onion epidermis", "Pushed to the peripheral parietal cytoplasm against the cell wall due to the huge central vacuole", "The large central vacuolar sap space occupies >80-90% of the interior cell volume", "Located precisely at the geometric dead center, Floating freely inside the vacuolar sap, Suspended outside the cell wall")
        ],
        'templates': [
            "In the class practical 'Preparation of temporary stained mount of onion peel': '{0}'. What is the correct scientific rationale or technique?:",
            "When preparing an onion epidermal mount in the laboratory: '{0}' is used because:",
            "A student prepares an onion peel slide: '{0}'. The accurate laboratory observation or rule is:",
            "What is the procedural standard regarding '{0}' during plant cell mount preparation?:",
            "Why is the following step critical when preparing an onion peel mount: '{0}'?:",
            "In examining onion epidermal cells under a compound microscope: '{0}' signifies:",
            "Identify the correct technique or explanation for: '{0}':",
            "During a biology practical test on onion peel cells: '{0}' is correctly described as:",
            "What observation or protocol applies to: '{0}'?:",
            "A student observes onion peel cells under 400x magnification: '{0}'. The correct fact is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Review the onion peel temporary mount protocol.**\n- **Specimen:** Inner concave epidermis of onion bulb scale leaf.\n- **Stain:** Safranin / dilute iodine (highlights nucleus and cell walls).\n- **Mountant:** Glycerine (prevents dehydration and optical distortion).\n- **Coverslip:** Lowered at 45° with a mounting needle to avoid trapped air bubbles.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Robert Hooke's Contemporaries: Marcello Malpighi and Nehemiah Grew
    arch5 = {
        'data': [
            ("Marcello Malpighi (1628-1694)", "Father of microscopic anatomy and plant histology; discovered blood capillaries in 1661", "Confirmed that plant tissues are composed of microscopic utricles / vesicles analogous to cells", "Invented the electron microscope, Discovered DNA double helix, Proposed the neuron doctrine"),
            ("Nehemiah Grew (1641-1712)", "English plant anatomist who published 'The Anatomy of Plants' in 1682", "Described plant tissues as composed of bladders and fibers, comparing them to woven lace or fabric", "Discovered bacteria in human mouth, Coined the term chromosome, First cloned a sheep"),
            ("Concept of plant tissue architecture in 17th-century microscopy", "Tissues were viewed as continuous masses containing chambers ('utricles' or 'vesicles') rather than autonomous living units", "Paved the conceptual pathway toward the unified Cell Theory 150 years later", "Viewed as solid non-porous stone, Believed to be made of miniature adult animals, Thought to be single giant multinucleate cells"),
            ("Why Hooke's discovery remained dormant for over a century", "Early microscopes had poor resolution (chromatic aberration) and observers lacked cell theory framework to recognize living significance", "Most naturalists viewed cell walls as mere fibrous framing around fluids rather than living functional units", "Because microscopes were banned by international law, Because all cork trees became extinct, Because Hooke hid his drawings"),
            ("Discovery of blood capillaries by Marcello Malpighi (1661)", "Provided the missing physical link in William Harvey's circulatory theory connecting arteries to veins", "Demonstrated blood cells circulating through microscopic capillary networks in frog lungs", "Proved that blood is generated fresh inside bones every minute, Proved blood flows in one direction only in worms, First visualized white blood cells eating bacteria"),
            ("Comparison of cork cells to honeycomb by Hooke", "Noted that cork was partitioned into distinct regular cavities separated by porous diaphragms", "Used the term 'pores' and 'cells' interchangeably in Micrographia", "Claimed cork was made of live bees, Believed cork was manufactured from spider silk, Thought cork was a dried mineral sponge"),
            ("Anton van Leeuwenhoek's relationship with Robert Hooke and the Royal Society", "Leeuwenhoek sent letters with microscopic drawings of 'animalcules' to Hooke and the Royal Society for verification", "Hooke replicated Leeuwenhoek's single-lens microscopes to confirm the existence of living microorganisms", "Hooke sued Leeuwenhoek for copyright violation, Leeuwenhoek was Hooke's university professor, They never communicated during their lifetimes"),
            ("Hooke's other scientific contributions beyond cytology", "Formulated Hooke's Law of Elasticity (F = -kx), designed the balance spring watch, and surveyed London after the 1666 Great Fire", "Was an extraordinary polymath and Curator of Experiments at the Royal Society", "Discovered gravity before Newton and proved planetary orbits are circles, Invented vaccination against smallpox, Discovered atomic fission"),
            ("Primary limitation of Hooke's definition of a cell", "Defined the cell based solely on the rigid outer boundary (cell wall) rather than the living internal contents (protoplasm)", "Hooke believed the hollow cavities were simply channels for conducting nutritive juices", "Hooke thought cells were large macroscopic fruit, Hooke claimed cells were formed of pure gold, Hooke thought cells could fly in air"),
            ("The shift from 'cell wall' focus to 'protoplasm' focus in biology", "Transition from 17th-century structural wall observation to 19th-century realization that the living cytoplasm/nucleus is the seat of life", "Led by Dujardin (sarcode), Purkinje (protoplasm), and Max Schultze (protoplasm theory)", "Reverted back to viewing cell walls as the only living part, Concluded that cytoplasm is waste water, Proved that cells have no internal structure")
        ],
        'templates': [
            "In the history of science and early microscopy: '{0}'. Identify the correct historical and biological fact:",
            "Regarding early microscopic investigators: '{0}' is recognized for:",
            "What contribution or concept is associated with '{0}'?:",
            "Analyze the historical context of early cytology: '{0}' refers to:",
            "Which statement accurately explains: '{0}'?:",
            "How did scientific understanding develop through '{0}'?:",
            "In evaluating 17th-century cell discoveries: '{0}' represents:",
            "What was the scientific significance of: '{0}'?:",
            "Historical cytology records that '{0}' led to:",
            "Which description accurately characterizes: '{0}'?:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand early microscopic discoveries.**\nFollowing Hooke's 1665 observation of cork, Marcello Malpighi and Nehemiah Grew extended microscopic anatomy to plant and animal tissues.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Historical significance:**\n{item[2]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Cork Anatomy, Lenticels, and Secondary Protective Systems
    arch6 = {
        'data': [
            ("Phellogen (Cork Cambium)", "Lateral meristem originating from cortical or pericyclic parenchyma cells during secondary growth", "Divides tangentially to produce phellem (cork) towards the exterior and phelloderm towards the interior", "Apical meristem producing leaves, Intercalary meristem elongating grass internodes, Endodermis forming Casparian strips"),
            ("Phellem (Cork)", "Dead, suberized cells arranged in radial compact rows with no intercellular spaces", "Forms the outer protective bark resistant to fire, water loss, pests, and mechanical shearing", "Living storage parenchyma with abundant starch, Sieve tubes with companion cells, Water-conducting tracheids with scalariform pits"),
            ("Phelloderm (Secondary Cortex)", "Living parenchymatous tissue cut off by the cork cambium on its inner side", "Contains chloroplasts in young green stems and stores nutrients", "Dead sclerenchyma fibers with thick lignin, Xylem vessels with bordered pits, Cuticle layer containing wax"),
            ("Lenticels in woody bark", "Lens-shaped raised openings formed by loose non-suberized complementary cells allowing gas exchange", "Enables oxygen and carbon dioxide diffusion for respiration in underlying living bark and cambium tissues", "Absorbs liquid water from raindrops, Secretes sweet nectar to attract ants, Forms thorns to deter herbivores"),
            ("Bark in botanical terminology", "All tissues lying external to the vascular cambium (includes secondary phloem and periderm)", "Protects the vascular cylinder and transports organic solutes via phloem", "Consists purely of dead xylem wood, Refers exclusively to the dead cuticle, Includes the pith and primary xylem"),
            ("Why peeling a complete ring of bark from a tree trunk (girdling) kills the tree", "Removes the phloem, halting translocation of photosynthesized sugars from leaves to roots; roots starve and die", "Water transport via inner xylem continues temporarily, but roots die from energy depletion, eventually killing the entire tree", "Water transport in xylem stops immediately within 5 seconds, The tree bleeds to death from losing sap instantly, Leaves lose all nitrogen immediately"),
            ("Commercial harvesting of cork from cork oak without killing the tree", "Only the outer phellem (cork) layer is stripped, leaving the living phellogen, phloem, and vascular cambium unharmed", "The phellogen regenerates a fresh layer of commercial cork over a 9 to 10 year cycle", "The entire tree trunk is cut down into circular planks, The xylem wood is extracted from the center of the tree, Cork is extracted by boiling the leaves"),
            ("Suberin chemical structure and properties", "Glycerol-derived cross-linked polyester polymer rich in long-chain hydroxy fatty acids and phenolics", "Imparts hydrophobicity, elasticity, thermal insulation, and resistance to enzymatic degradation", "Pure carbohydrate composed of glucose monomers, Protein polymer made of 20 essential amino acids, Inorganic silica crystalline matrix"),
            ("Tyloses in secondary xylem compared to cork suberin", "Balloon-like parenchymatous outgrowths blocking xylem vessels in non-functional heartwood", "Prevents fungal spread and water leakage in heartwood, while suberin acts as a dermal bark barrier", "Tyloses transport food, while cork transports water; Both are living actively dividing meristems; Both are leaf stomata structures"),
            ("Distinction between Epidermis and Periderm", "Epidermis is the primary outer monolayer of young stems/leaves; Periderm is the secondary multi-layered protective bark replacing epidermis in woody stems", "Epidermis has cuticle and stomata; Periderm has suberized cork and lenticels", "Epidermis is made of dead cork cells, while periderm is made of living dividing cells; They are identical names for the same single layer; Epidermis only exists in roots")
        ],
        'templates': [
            "In structural botany and secondary plant tissue development: '{0}'. Identify the true statement:",
            "What physiological or structural feature describes: '{0}'?:",
            "Regarding the tissue system: '{0}', which of the following is scientifically accurate?:",
            "Analyze the anatomical structure: '{0}'. The correct botanical description is:",
            "How does '{0}' function in plant biology?:",
            "In plant histology, '{0}' is defined by:",
            "Which statement correctly accounts for the biology of: '{0}'?:",
            "What is the botanical significance of: '{0}'?:",
            "Consider the tissue organization: '{0}'. The accurate characterization is:",
            "A question on secondary bark anatomy asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand periderm and bark anatomy.**\nDuring secondary growth in woody dicots, the epidermis breaks and is replaced by the **periderm**:\n1. Phellogen (cork cambium)\n2. Phellem (cork, suberized dead cells)\n3. Phelloderm (secondary cortex)\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Cell Wall Structure and Chemistry in Plants, Fungi, and Bacteria
    arch7 = {
        'data': [
            ("Primary structural polysaccharide of plant cell walls", "Cellulose", "Linear polymer of β-D-glucose units joined by β-(1→4)-glycosidic bonds forming high-tensile microfibrils", "Chitin, Peptidoglycan, Glycogen"),
            ("Primary chemical constituent of fungal cell walls", "Chitin", "Nitrogen-containing structural polysaccharide composed of N-acetylglucosamine units joined by β-(1→4) bonds", "Cellulose, Peptidoglycan, Pectin"),
            ("Primary chemical constituent of bacterial cell walls (Eubacteria)", "Peptidoglycan (Murein)", "Polymer consisting of alternating NAM and NAG glycan chains cross-linked by short amino acid peptide bridges", "Cellulose, Chitin, Keratin"),
            ("Chemical constituent of the plant middle lamella cementing adjacent cells together", "Calcium and magnesium pectates", "Amorphous jelly-like cementing layer; dissolves during fruit ripening causing softening", "Cellulose microfibrils, Chitin crystals, Suberin wax"),
            ("Complex polymer deposited in secondary cell walls of plant sclerenchyma and xylem vessels", "Lignin", "Complex cross-linked aromatic polymer of phenylpropanoid alcohols providing rigid compressive strength and decay resistance", "Pectin, Suberin, Starch"),
            ("Cutin and Wax on aerial plant epidermal cell walls", "Form an external hydrophobic cuticle layer that drastically reduces non-stomatal transpiration and defends against pathogens", "Lipid-based waterproofing envelope covering leaves, herbaceous stems, and fruit", "Attracts harmful bacteria, Dissolves plant cell walls during rain, Generates ATP from sunlight directly"),
            ("Gram-positive vs Gram-negative bacterial cell wall difference", "Gram-positive walls have a thick multilayered peptidoglycan layer with teichoic acids; Gram-negative walls have a thin peptidoglycan layer enclosed by an outer lipopolysaccharide (LPS) membrane", "Reflected in Gram stain retention (purple vs pink)", "Gram-positive bacteria lack cell walls, Gram-negative bacteria have cellulose walls, Both have identical thick chitin walls"),
            ("Plasmodesmata traversing plant cell walls", "Microscopic membrane-lined cytoplasmic channels connecting adjacent plant cells across middle lamella and primary walls", "Enables symplastic transport of water, ions, small metabolites, and signaling molecules", "Open holes where nuclei travel between cells, Gas vents allowing air to escape from roots, Dead suberin tubes for food storage"),
            ("Why animal cells lack a cell wall", "Animals require structural flexibility, active locomotion, rapid cell shape change, and tissue remodeling", "Structural support is provided internally by the cytoskeleton and externally by extracellular matrix and skeletons", "Because animal cells have no plasma membrane, Because cell walls prevent cells from having DNA, Because animals consume all their cell walls as food"),
            ("Turgor pressure and the role of plant cell walls", "The rigid cell wall exerts an equal and opposite wall pressure against the expanding turgid vacuole, preventing hypotonic osmotic lysis", "Allows herbaceous plant shoots to remain erect and crisp without a bony skeleton", "Causes the cell to burst instantly when placed in pure water, Prevents water from ever entering the plant cell, Melts the plasma membrane during rain")
        ],
        'templates': [
            "In comparative cytology: '{0}'. Identify the correct structural or chemical fact:",
            "What is the chemical composition or biological function of: '{0}'?:",
            "Regarding cell wall diversity across biological kingdoms: '{0}' is characterized by:",
            "Analyze the cellular wall component: '{0}'. The accurate scientific fact is:",
            "Which statement correctly describes: '{0}'?:",
            "In cell wall biochemistry, '{0}' refers to:",
            "What is the cellular role and structure of: '{0}'?:",
            "Identify the correct chemical constituent or mechanism for: '{0}':",
            "In studying cellular boundaries: '{0}' is properly explained as:",
            "A cytology question examines cell wall evolution: '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Compare cell wall composition across kingdoms.**\n- **Plants:** Cellulose microfibrils in a hemicellulose/pectin matrix; middle lamella of calcium pectate.\n- **Fungi:** Chitin (polymer of N-acetylglucosamine).\n- **Bacteria:** Peptidoglycan (murein).\n- **Animals:** No cell wall.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 8: Chronology of Cytological Discoveries Leading to Cell Theory
    arch8 = {
        'data': [
            (1665, "Robert Hooke", "Discovered cork cells and coined the term 'cell' in Micrographia", "Dead plant cell wall compartments"),
            (1674, "Anton van Leeuwenhoek", "First observed and described living, free-moving microscopic cells ('animalcules')", "Bacteria, protozoa (Vorticella), spirogyra, red blood cells, and sperm"),
            (1831, "Robert Brown", "Discovered and named the 'nucleus' as a constant spherical organelle in orchid root cells", "Recognized it as an essential fundamental component of plant cells"),
            (1838, "Matthias Schleiden", "German botanist who concluded that all plant tissues are composed of cells", "Asserted that the cell is the fundamental unit of plant structure"),
            (1839, "Theodor Schwann", "German zoologist who concluded that all animal tissues are composed of cells and unified Cell Theory", "Formulated the foundational Cell Theory: 'All living organisms are composed of cells and their products'"),
            (1839, "Jan Evangelista Purkinje", "Coined the scientific term 'protoplasm' for the fluid living substance of the cell", "Shifted cytological focus from the non-living outer cell wall to the living internal contents"),
            (1855, "Rudolf Virchow", "Expanded Cell Theory with the aphorism 'Omnis cellula-e-cellula' (All cells arise from pre-existing cells)", "Refuted spontaneous generation / de novo crystallization of cells from free cytoblastema"),
            (1866, "Ernst Haeckel", "Proposed that the nucleus is responsible for the storage and transmission of hereditary characters", "Identified the genetic role of the nucleus before chromosomes were fully characterized"),
            (1931, "Ernst Ruska and Max Knoll", "Invented the Transmission Electron Microscope (TEM)", "Overcame light diffraction limits, achieving sub-nanometre resolution to discover cell ultrastructure"),
            (1898, "Camillo Golgi", "Discovered the reticular internal reticular apparatus (Golgi complex/body) using silver nitrate staining", "Visualized the cellular packaging and secretory organelle in owl nerve cells")
        ],
        'templates': [
            "In cytological chronology, which scientist made the milestone discovery in {0}: '{2}'?:",
            "Identify the scientist associated with the landmark biological discovery in {0} ({2}):",
            "In {0}, {1} contributed fundamentally to cytology by: '{2}'. What did this establish?:",
            "Which milestone discovery occurred in {0} by {1}?:",
            "Match the year and scientist: in {0}, {1} discovered:",
            "The historical breakthrough '{2}' was achieved in {0} by:",
            "Who was the pioneering cytologist responsible for '{2}' in {0}?:",
            "In the timeline of cell biology: in {0}, {1} demonstrated that:",
            "Which of the following achievements is credited to {1} in {0}?:",
            "The cytological discovery '{2}' occurred in {0} under the leadership of:"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Louis Pasteur",
                "Gregor Mendel",
                "Charles Darwin"
            ],
            f"**Step 1: Review cytological discovery timeline.**\n- **{item[0]}:** **{item[1]}** accomplished: *{item[2]}*.\n\n**Step 2: Structural and biological meaning:**\n{item[3]}.\n\n**Step 3: Correct attribution:** **{item[1]}**."
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-2-2.1.1", "Robert Hooke cork cells (1665)", archs)


# ==============================================================================
# SUBTOPIC 2.1.2: Anton van Leeuwenhoek free living cells
# Topic Code: CBSE-9-SCIE-2-2.1.2
# ==============================================================================
def gen_2_1_2():
    # Arch 1: Anton van Leeuwenhoek's Single-Lens Microscope and Craftsmanship
    arch1 = {
        'data': [
            ("Optical construction of Leeuwenhoek's microscopes", "A single, tiny, high-quality biconvex glass bead lens mounted between two riveted brass plates with a specimen-positioning screw pin", "Achieved remarkable magnification up to 275x to 300x with exceptional numerical aperture and minimal aberration", "Two large ocular lenses mounted in a long cardboard cylinder, Electron beam focusing magnets, A hollow water sphere condenser"),
            ("Magnification power achieved by Leeuwenhoek's finest single lens", "Approximately 250x to 300x magnification", "Had a focal length of only ~1 mm, allowing resolution down to ~1.4 micrometres, resolving bacteria", "Only 5x magnification, 50,000x magnification, Exactly 10x magnification"),
            ("Why Leeuwenhoek's single-lens microscopes outperformed contemporary compound microscopes", "Single small high-curvature bead lenses avoided the compounding chromatic and spherical aberrations of multi-lens systems of the 1670s", "Provided a bright, sharp, aberration-reduced image when held extremely close to the observer's eye", "Because Leeuwenhoek used magical diamond lenses, Because compound microscopes did not use light, Because Leeuwenhoek observed in total darkness"),
            ("Leeuwenhoek's profession and training in Delft, Netherlands", "Draper / fabric merchant and city chamberlain with no formal university academic degree", "Initially used magnifying glasses to inspect the weave and thread count of linen fabrics before teaching himself advanced glass blowing", "University professor of medicine at Leiden, Court physician to the King of England, Master glassmaker for astronomical telescopes"),
            ("Technique used by Leeuwenhoek to manufacture his high-power lens beads", "Melting fine glass filaments in a hot flame to form tiny, perfectly spherical molten glass beads through surface tension", "Ground and polished microscopic glass globules with extraordinary manual dexterity", "Pouring molten lead into cold water, Carving rock crystal with a diamond chisel, Casting plastic polymers in molds"),
            ("Method of viewing through Leeuwenhoek's microscope", "Holding the tiny instrument directly against the eye socket while facing a bright window or candle flame", "Adjusting focus by turning fine threaded thumbscrews that moved the specimen pin toward or away from the lens", "Projecting the image onto a large classroom wall screen, Looking downward onto a wide glass mirror stage, Viewing through electronic digital binoculars"),
            ("Secrecy surrounding Leeuwenhoek's lens-grinding methods", "Leeuwenhoek kept his precise lens-making techniques strictly secret, never revealing his proprietary methods to visitors", "Refused to publish his manufacturing protocols, leaving only his observational letters to the Royal Society", "Destroyed all his microscopes upon his death, Claimed his lenses were made by angels, Published 50 detailed instruction textbooks"),
            ("Material of the mounting plates in Leeuwenhoek's surviving instruments", "Brass or silver metal plates riveted together", "Clamped the tiny spherical lens securely between small aligned pinholes", "Wooden blocks tied with twine, Clay ceramics baked in an oven, Hollow bamboo tubes"),
            ("How many microscopes Leeuwenhoek constructed over his lifetime", "Over 500 optical devices and lenses", "Left a collection of silver and brass instruments bequeathed to the Royal Society of London upon his death", "Exactly 2 instruments, Over 100,000 factory-made devices, Only 1 single lifetime instrument"),
            ("Leeuwenhoek's communication channel with the international scientific community", "Sent hundreds of informal letters written in Dutch to the Royal Society of London over 50 years", "Translated and read aloud by Henry Oldenburg and verified by Robert Hooke before publication in Philosophical Transactions", "Wrote thick academic Latin textbooks, Traveled worldwide giving lecture tours, Broadcasted radio announcements")
        ],
        'templates': [
            "In the history of cytology and optical science: '{0}'. Identify the true scientific statement:",
            "Regarding Anton van Leeuwenhoek's microscope technology: '{0}' is characterized by:",
            "What optical or historical reality explains: '{0}'?:",
            "Analyze Leeuwenhoek's scientific craftsmanship: '{0}' refers to:",
            "Which statement accurately explains '{0}' in Leeuwenhoek's career?:",
            "Why was '{0}' significant in enabling the discovery of microscopic life?:",
            "In early microscopy, '{0}' is correctly described as:",
            "What is the historical and technological reality behind: '{0}'?:",
            "Consider the optical design of early microscopes: '{0}' demonstrates that:",
            "A biology history question asks about '{0}'. The accurate fact is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Leeuwenhoek's microscopy breakthrough.**\nAnton van Leeuwenhoek (1632–1723) crafted single-lens handheld microscopes with minute biconvex lenses.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 2: Discovery of Living Microorganisms - Animalcules
    arch2 = {
        'data': [
            ("Discovery of free-living freshwater protozoa in pond water (1674)", "First visualization of motile microscopic unicellular organisms, including \\(\\textit{Vorticella}\\), \\(\\textit{Euglena}\\), and green filamentous algae (\\(\\textit{Spirogyra}\\))", "Proved that water contains teeming communities of autonomous living microscopic life", "Claimed pond water was completely sterile mineral fluid, Believed green filaments were insect hairs, Thought protozoa were miniature mermaids"),
            ("Coining of the term 'Animalcules' (Little Animals)", "Leeuwenhoek's term for the microscopic swimming organisms he discovered in rainwater, pond water, and infusions", "Deduced they were living animals because of their active, purposeful self-directed swimming motility and behavioral responses", "Used the Latin word 'bacteria' in 1674, Called them viral crystals, Classified them as non-living minerals"),
            ("Discovery of bacteria in dental plaque (1676-1683)", "Scraped plaque from his own teeth and elderly non-brushing individuals, observing motile rods (bacilli), spheres (cocci), and spiral forms (spirochaetes)", "First scientific observation and documentation of bacteria in human history", "Discovered dental cavities are caused by radioactive decay, Claimed teeth were made of living insects, Proved human mouths are completely sterile"),
            ("Observation of human red blood cells (1674)", "Accurately measured erythrocytes as ~7.5 micrometres in diameter and described their biconcave disc shape circulating through capillaries", "Confirmed Marcello Malpighi's earlier observations and demonstrated their role in blood circulation", "Claimed blood cells are square crystalline cubes, Stated red blood cells are alive and swim with flagella, Thought blood color is due to dissolved copper"),
            ("Observation of spermatozoa in semen of animals and humans (1677)", "Discovered motile flagellated gametes ('spermatic animalcules')", "Overthrew the Aristotelian theory that semen was a coagulating non-cellular fluid and initiated embryological cytology", "Claimed semen was composed of tiny complete adult humans (homunculi) with folded arms, Believed sperm were parasitic worms harming reproduction, Thought eggs are fertilised by spiritual vapor"),
            ("Observation of the vacuole and spiral chloroplasts in green algae (Spirogyra)", "Observed green ribbon-like spiral bands within translucent green pond filaments in 1674", "One of the earliest descriptions of algal intracellular organelles before modern organelle terminology existed", "Believed green filaments were poisonous snakes, Thought algae were crystals of copper, Claimed algae had no cell boundaries"),
            ("Discovery of Giardia lamblia in human diarrheal feces (1681)", "Identified the flagellated protozoan parasite \\(\\textit{Giardia}\\), describing its tumbling crab-like motility under the microscope", "First microscopic diagnosis of an intestinal parasitic pathogen in human history", "Claimed feces was pure sterile carbon, Believed diarrhea was caused by evil spirits, Discovered penicillin mold in feces"),
            ("Leeuwenhoek's pepper-water infusion experiments (1676)", "Soaked black peppercorns in water to discover why pepper is hot; observed explosive growth of millions of tiny swimming bacteria", "Demonstrated microbial proliferation and population growth in organic nutrient broths", "Proved that pepper heat is caused by tiny biting insects with sharp teeth, Concluded that pepper is made of pure acid crystals, Proved water evaporates into bacteria"),
            ("Verification of Leeuwenhoek's findings by the Royal Society (1677)", "The Royal Society requested Robert Hooke and Nehemiah Grew to replicate the observations; Hooke successfully confirmed living animalcules", "Led to Leeuwenhoek's election as a full Fellow of the Royal Society of London in 1680", "The Royal Society banned Leeuwenhoek from science, Hooke declared Leeuwenhoek a fraud, The King confiscated Leeuwenhoek's microscopes"),
            ("Core contrast between Hooke's (1665) and Leeuwenhoek's (1674) discoveries", "Hooke discovered dead structural cell walls in cork; Leeuwenhoek discovered the first living, moving, functional individual cells", "Shifted science from viewing cells as passive static structural compartments to recognizing cells as autonomous living units of life", "Hooke observed living bacteria while Leeuwenhoek observed dead cork; Both discovered identical plant tissues in oak trees; Hooke discovered animal cells while Leeuwenhoek discovered plant cells")
        ],
        'templates': [
            "In the history of microbiology: '{0}'. What is the accurate scientific fact?:",
            "What major discovery is represented by: '{0}'?:",
            "Regarding Anton van Leeuwenhoek's biological findings: '{0}' is characterized as:",
            "How did '{0}' revolutionize contemporary understanding of life?:",
            "Which statement correctly details: '{0}'?:",
            "Analyze the historical experiment: '{0}'. The scientific reality is:",
            "What did Leeuwenhoek observe and conclude in: '{0}'?:",
            "In assessing Leeuwenhoek's contributions: '{0}' established:",
            "Which discovery by Leeuwenhoek is accurately described by: '{0}'?:",
            "A biology question compares early discoveries: '{0}'. The correct evaluation is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Leeuwenhoek's living cell discoveries.**\nAnton van Leeuwenhoek was the first human to observe **free-living living cells** in 1674.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Impact:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Bacterial Morphology Discovered by Leeuwenhoek
    arch3 = {
        'data': [
            ("Coccus (plural: Cocci)", "Spherical or oval-shaped bacteria", "Occur as single cells, pairs (diplococci), chains (streptococci), or clusters (staphylococci); e.g. \\(\\textit{Streptococcus pneumoniae}\\)", "Rod-shaped straight cylinders, Spiral corkscrews with flagella, Comma-shaped curved vibrios"),
            ("Bacillus (plural: Bacilli)", "Cylindrical or rod-shaped bacteria", "May occur singly, in pairs (diplobacilli), or in filamentous chains (streptobacilli); e.g. \\(\\textit{Bacillus anthracis}\\), \\(\\textit{Lactobacillus}\\)", "Spherical balls, Rigid helical corkscrews, Branched fungal hyphae"),
            ("Spirillum (plural: Spirilla)", "Rigid, helical or corkscrew-shaped bacteria", "Possess external flagella and rigid wavy cell walls; e.g. \\(\\textit{Spirillum volutans}\\)", "Spherical chains, Flat rectangular sheets, Comma-shaped bend"),
            ("Vibrio (plural: Vibrios)", "Curved, comma-shaped cylindrical bacteria", "Characterized by a single rigid curved bend resembling a punctuation comma; e.g. \\(\\textit{Vibrio cholerae}\\)", "Perfect spheres, Multi-segmented cubes, Branching filaments"),
            ("Spirochaete", "Flexible, thin, undulating spiral-shaped bacteria", "Possess internal axial filaments (endoflagella) within periplasmic space producing corkscrew motility; e.g. \\(\\textit{Treponema pallidum}\\)", "Rigid straight rods, Spherical clusters, Square flat tiles"),
            ("Typical size range of most bacterial cells", "0.5 to 5.0 micrometres (μm) in length/diameter", "Approximately 10 times smaller than typical eukaryotic animal/plant cells (10-100 μm)", "1 to 2 millimetres (visible to naked eye), 0.001 nanometres (smaller than protons), 10 to 50 centimetres"),
            ("Bacterial flagella structure and motility mechanism", "Rigid helical filament composed of flagellin protein driven by a rotary motor powered by proton motive force (\\(\\text{H}^+\\) gradient)", "Rotates like a boat propeller to drive rapid swimming motility (up to 50 body lengths per second)", "Bends like a whip with 9+2 microtubule dynein sliding, Contracts like actin-myosin muscle fibers, Glides by dissolving the water chemically"),
            ("Capsule / Glycocalyx in bacterial cells", "Gelatinous polysaccharide or polypeptide coat external to the peptidoglycan cell wall", "Protects bacteria from phagocytosis by host white blood cells and prevents desiccation", "Generates ATP through cellular respiration, Synthesizes proteins for secretion, Duplicates the bacterial chromosome"),
            ("Gram-negative outer membrane composition", "Asymmetric bilayer containing lipopolysaccharide (LPS / endotoxin) on outer leaflet and phospholipids on inner leaflet", "Provides an impermeable barrier against toxic detergents, bile salts, and certain antibiotics (e.g. penicillin)", "Composed purely of solid cellulose wax, Made of bone hydroxyapatite, Contains active chloroplast pigments"),
            ("Plasmids in bacterial cytoplasm", "Small, circular, double-stranded extrachromosomal DNA molecules capable of autonomous self-replication", "Carry accessory genes providing antibiotic resistance (R-factors), toxin production, or conjugation pili", "Store reserve starch for winter dormancy, Serve as the primary nuclear genome of bacteria, Form the physical structure of the bacterial cell wall")
        ],
        'templates': [
            "In microbiology and cytology: '{0}'. Identify the correct structural definition or fact:",
            "What morphological form or feature is represented by: '{0}'?:",
            "Regarding bacterial diversity: '{0}' is characterized as:",
            "A student identifies '{0}'. The correct biological description is:",
            "Which statement accurately describes the bacterial structure: '{0}'?:",
            "In classifying bacterial shapes: '{0}' corresponds to:",
            "What is the functional or morphological reality of: '{0}'?:",
            "Identify the correct anatomical description for: '{0}':",
            "In bacteriology, '{0}' refers to:",
            "Analyze the microbial feature: '{0}'. The accurate scientific fact is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand bacterial morphology.**\nBacteria exhibit four classic morphological types:\n- **Coccus:** Spherical.\n- **Bacillus:** Rod-shaped.\n- **Spirillum / Spirochaete:** Spiral/helical.\n- **Vibrio:** Comma-shaped.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Leeuwenhoek's Impact on the Theory of Spontaneous Generation
    arch4 = {
        'data': [
            ("Theory of Spontaneous Generation (Abiogenesis)", "The ancient belief that living organisms can arise spontaneously from non-living matter (e.g. maggots from rotting meat, mice from sweaty shirts)", "Prevalent since Aristotle; challenged by experimental evidence from Redi, Spallanzani, and Pasteur", "The theory that all living organisms evolved from fish, The concept that cells reproduce by binary fission, The law that energy cannot be created or destroyed"),
            ("Leeuwenhoek's stance on spontaneous generation of animalcules", "Leeuwenhoek firmly opposed spontaneous generation, asserting that even tiny animalcules arise from airborne reproductive 'seeds' or parents", "Observed reproduction and copulation in microscopic creatures and argued that God created life through reproduction, not spontaneous dirt", "Leeuwenhoek claimed dirt spontaneously creates bacteria, Leeuwenhoek proved that rotting water creates animals from nothing, Leeuwenhoek had no opinion on spontaneous generation"),
            ("Francesco Redi's experiment (1668)", "Placed meat in unsealed jars, sealed jars, and gauze-covered jars, proving maggots develop only from fly eggs, not from decomposing meat", "First controlled biological experiment disproving spontaneous generation for macroscopic organisms", "Proved that air contains bacteria, Discovered that boiling kills mold, Invented refrigeration to prevent meat decay"),
            ("Lazzaro Spallanzani's infusion experiment (1768)", "Boiled nutrient broth in sealed glass flasks for an hour, showing the broth remained clear with zero microbial growth indefinitely", "Demonstrated that heating kills microorganisms and that microbes enter from airborne contamination", "Proved that air is poisonous to bacteria, Discovered that glass attracts spontaneous generation, Claimed boiling destroys the nutritional value of broth"),
            ("John Needham's counter-experiment (1745)", "Briefly boiled mutton gravy in flasks and sealed them with corks; observed microbial growth and claimed spontaneous generation was real", "Flawed experiment: insufficient boiling failed to kill bacterial endospores and unsterile porous corks allowed air leaks", "Proved bacteria cannot survive heat, Discovered modern autoclave sterilization, Proved spontaneous generation was a universal law"),
            ("Louis Pasteur's Swan-Neck Flask experiment (1862)", "Used swan-neck S-shaped curved flasks allowing air entry while gravity trapped airborne dust and microbes in the bend; broth stayed sterile indefinitely", "Conclusively defeated the doctrine of spontaneous generation and earned the French Academy of Sciences Alhumbert Prize", "Showed that air destroys broth chemically, Proved that swan-neck flasks generate oxygen, Demonstrated that bacteria are created by glass"),
            ("What happened when Pasteur snapped the curved neck off the swan-neck flask", "Airborne dust particles carrying bacterial spores fell directly into the broth, which became turbid with microbial growth within 48 hours", "Proved that living microbes in broth originate exclusively from pre-existing airborne microbes, not spontaneous generation", "The broth exploded due to atmospheric pressure, The broth froze instantly into solid ice, The broth turned into pure distilled water"),
            ("Biogenesis Principle ('Omne vivum ex vivo')", "Fundamental biological law stating that all living organisms arise exclusively from pre-existing living organisms through reproduction", "Direct logical corollary of Rudolf Virchow's cellular aphorism 'Omnis cellula-e-cellula'", "Claims that life is continuously created from mud, Asserts that non-living chemicals can turn into living mice overnight, States that living organisms do not need parents"),
            ("John Tyndall's discovery of heat-resistant bacterial endospores (1876)", "Discovered that certain bacteria (e.g. \\(\\textit{Bacillus}\\), \\(\\textit{Clostridium}\\)) form endospores resistant to 100°C boiling", "Developed 'Tyndallization' (discontinuous fractional sterilization over 3 successive days) to kill germinating spores", "Proved that spontaneous generation occurs in hay, Claimed bacteria are created by boiling water, Proved that heat causes bacteria to reproduce faster"),
            ("Modern understanding of the Origin of Life (Abiogenesis vs Biogenesis)", "Biogenesis governs all modern biology today (life comes from pre-existing life); chemical abiogenesis occurred once ~3.8 billion years ago on early Earth", "Miller-Urey experiment (1953) demonstrated abiotic synthesis of amino acids from primitive reducing atmospheric gases", "Spontaneous generation occurs daily in modern puddles, Living bacteria fall from the sun every morning, Life has no chemical foundation")
        ],
        'templates': [
            "In the history of science: '{0}'. What is the accurate scientific fact?:",
            "How did experimental evidence resolve the debate over '{0}'?:",
            "Regarding the dispute over '{0}': which statement is historically and scientifically true?:",
            "Analyze the landmark investigation: '{0}' established that:",
            "What is the biological reality demonstrated by: '{0}'?:",
            "In experimental microbiology, '{0}' proved that:",
            "Identify the correct outcome and significance of: '{0}':",
            "Which description accurately characterizes: '{0}'?:",
            "A biology question tests historical debates: '{0}'. The correct answer is:",
            "What fundamental biological law emerged from resolving: '{0}'?:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand the debate over spontaneous generation.**\n- **Spontaneous Generation (Abiogenesis):** Non-living matter produces living organisms.\n- **Biogenesis:** Life arises only from pre-existing life.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Landmark resolution:**\n{item[2]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Free-Living Unicellular Organisms Discovered in Freshwater
    arch5 = {
        'data': [
            ("Amoeba proteus", "Free-living freshwater protozoan exhibiting amorphous changing shape and locomotion via pseudopodia (false feet)", "Feeds by phagocytosis and regulates osmotic water balance via a contractile vacuole", "Possesses a rigid cellulose cell wall, Moves using two long whip-like flagella, Autotrophic with red chloroplasts"),
            ("Paramecium caudatum", "Ciliated, slipper-shaped freshwater protozoan with coordinated beating of thousands of cilia", "Possesses dual nuclei (macronucleus and micronucleus), oral groove, cytostome, and two radial contractile vacuoles", "Lacks a plasma membrane, Moves by amoeboid pseudopodia, Contains multicellular tissues"),
            ("Euglena viridis", "Unicellular flagellated protist exhibiting mixotrophic nutrition (photosynthetic in light, heterotrophic in dark)", "Possesses a photoreceptive eyespot (stigma), green chloroplasts, proteinaceous pellicle, and a single anterior whip-like flagellum", "Has a rigid wooden cell wall, Completely non-motile like a stone, Parasite living exclusively inside human bone cells"),
            ("Chlamydomonas", "Unicellular biflagellated green alga found in freshwater pools and damp soils", "Possesses a cup-shaped chloroplast, pyrenoid for starch synthesis, eyespot, and two equal apical flagella", "Heterotrophic animal with no chlorophyll, Multicellular marine giant kelp, Non-motile bacterium lacking flagella"),
            ("Vorticella", "Bell-shaped, stalked, sessile ciliated protozoan found anchored to freshwater pond weeds", "Possesses an inverted bell body with a ciliated oral wreath and a retractile spring-like helical stalk containing spasmoneme fibers", "Free-swimming giant bacterium, Photosynthetic plant with true roots, Multicellular worm living in marine sand"),
            ("Contractile Vacuole in freshwater unicellular protists", "Osmoregulatory organelle that periodically collects excess cytosolic water and pumps it out through the plasma membrane", "Prevents hypotonic osmotic swelling and lysis in freshwater habitats where interior cytoplasm is hypertonic to pond water", "Digests solid food particles by secreting acid, Synthesizes proteins for cellular growth, Stores genetic information like a nucleus"),
            ("Pellicle in Paramecium and Euglena", "Flexible proteinaceous sub-membrane skeletal layer providing structural shape while allowing cell flexibility", "Replaces the rigid cell wall in these motile protists, maintaining characteristic organism morphology", "A thick layer of dead cork suberin, An impermeable metal shield protecting against sunlight, A layer of green photosynthetic wax"),
            ("Food Vacuole (Phagosome) in Amoeba", "Temporary intracellular digestive compartment formed by pseudopodial engulfment of food particles", "Fuses with lysosomes containing hydrolytic digestive enzymes to break down prey into absorbable nutrients", "Pumps water out of the cell to prevent bursting, Transports oxygen from air into mitochondria, Duplicates the cell's genetic chromosomes"),
            ("Pseudopodia mechanism in Amoeba (Sol-Gel Theory)", "Reversible cytoplasmic transformation between fluid central plasmasol and viscous peripheral plasmagel", "Drives protoplasmic streaming and amoeboid creeping motion toward food or away from noxious stimuli", "Propelled by microscopic rocket jets of boiling water, Driven by spinning flagellar wheels, Glides on magnetic currents in the soil"),
            ("Binary fission in Amoeba and Paramecium", "Asexual reproduction where the parent cell duplicates its genetic material and divides into two identical daughter cells", "In Amoeba, division occurs across any plane; in Paramecium, transverse binary fission occurs perpendicular to the long axis", "Involves fusion of male and female multicellular gametes, Occurs exclusively by forming dry airborne seeds, Results in complete death of all daughter cells")
        ],
        'templates': [
            "In the study of unicellular living microorganisms: '{0}'. Identify the correct biological fact:",
            "What cellular feature or organism is described as: '{0}'?:",
            "Regarding free-living freshwater protists: '{0}' is characterized by:",
            "A student observes pond water under a microscope: '{0}'. The accurate identification is:",
            "Analyze the unicellular structure: '{0}'. The correct biological description is:",
            "How does '{0}' function in unicellular organism physiology?:",
            "Which statement correctly explains the morphology or behavior of: '{0}'?:",
            "In protozoology, '{0}' refers to:",
            "What is the scientific reality regarding: '{0}'?:",
            "A biology practical examines living pond organisms: '{0}'. The correct conclusion is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand unicellular freshwater protist diversity.**\nLeeuwenhoek discovered free-living unicellular protists (Amoeba, Paramecium, Euglena, Vorticella, Chlamydomonas) in freshwater pond samples.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Human Microscopic Cells Observed by Leeuwenhoek
    arch6 = {
        'data': [
            ("Human Red Blood Cells (Erythrocytes)", "Enucleated, biconcave circular discs of diameter ~7.2 to 7.8 μm containing hemoglobin", "Biconcave shape maximizes surface-area-to-volume ratio for rapid oxygen diffusion; lack of nucleus accommodates more hemoglobin", "Spherical nucleated cells with pseudopodia, Spindle-shaped multinucleated fibers, Long branched nerve cells with synapses"),
            ("Human Spermatozoa (Sperm cells)", "Motile male gametes consisting of head (with haploid nucleus and acrosome), middle piece (with spiral mitochondria), and flagellar tail", "Tail exhibits whip-like undulations powered by ATP from middle-piece mitochondria to swim toward the ovum", "Non-motile spherical eggs filled with yolk, Multicellular worms with digestive tracts, Ciliated epithelial sheets lining lungs"),
            ("Epithelial cheek cells (Squamous epithelium)", "Thin, flat, polygonal plate-like cells with distinct centrally placed nuclei and irregular keratinized borders", "Form a smooth protective lining inside the buccal cavity that continuously sloughs off and regenerates", "Elongated striated muscle fibers with sarcomeres, Branching dendrites with myelin sheaths, Hollow dead tubes impregnated with suberin"),
            ("Why mature mammalian red blood cells lack a nucleus and organelles", "Maximizes internal cytoplasmic space to pack ~270 million hemoglobin molecules per cell for maximum oxygen transport", "Erythrocytes lose their nucleus, mitochondria, and ER during terminal maturation in the bone marrow", "Because red blood cells are dead cells like cork, Because the nucleus dissolves in acidic blood plasma, Because red blood cells are manufactured from plant chloroplasts"),
            ("Why human red blood cells burst when placed in pure distilled water", "Lacking a rigid protective cell wall, water rushes into the hypertonic cell via endosmosis until the plasma membrane ruptures (hemolysis)", "Plant cells do not burst in water because their rigid cellulose cell wall exerts opposing wall pressure (turgor)", "The distilled water dissolves hemoglobin chemically, Red blood cells are made of pure water-soluble sugar, Red blood cells contract until they pop"),
            ("Acrosome function in human sperm cells", "Modified lysosomal cap over the anterior nucleus containing hydrolytic enzymes (hyaluronidase and acrosin)", "Digests through the protective corona radiata and zona pellucida of the ovum to enable fertilization", "Powers the swimming motion of the flagellum, Stores glycogen for sperm nutrition, Synthesizes testosterone hormone"),
            ("Methylene blue staining of human cheek epithelial cells", "Basic cationic stain that binds specifically to acidic polyanions (DNA/RNA) in the nucleus, staining nuclei deep blue", "Provides strong optical contrast between the pale blue cytoplasm and the dark blue spherical nucleus", "Dissolves the cheek cells instantly, Stains only cell walls red, Turns cheek cells into bacterial colonies"),
            ("White Blood Cells (Leukocytes) in human blood", "Nucleated immune defense cells capable of amoeboid movement and diapedesis across capillary walls", "Engulf pathogens by phagocytosis (neutrophils/macrophages) or produce antibodies (lymphocytes)", "Lack nuclei and transport carbon dioxide, Are dead crystalline platelets, Form the structural bones of the skull"),
            ("Platelets (Thrombocytes) in human blood", "Small, enucleated cytoplasmic fragments derived from megakaryocytes in bone marrow (2-4 μm diameter)", "Initiate blood clotting by releasing thromboplastin and forming a platelet plug at wound sites", "Transport glucose to muscles, Fight virus infections with antibodies, Produce red blood cells in the liver"),
            ("Comparative size order of human cellular components", "Ovum (100 μm) > Cheek cell (50 μm) > White blood cell (12-15 μm) > Red blood cell (7.5 μm) > Platelet (2-4 μm) > Sperm head (3-5 μm)", "The human unfertilized ovum is the largest single human cell, barely visible to the naked human eye", "Sperm cell > Ovum > Cheek cell > Platelet, Red blood cell is the largest cell in human body, All human cells are exactly identical in diameter")
        ],
        'templates': [
            "In human histology and microscopic cytology: '{0}'. What is the correct scientific fact?:",
            "What physiological or structural feature describes: '{0}'?:",
            "Regarding human cell diversity: '{0}' is characterized by:",
            "Analyze the cellular component: '{0}'. The accurate biological description is:",
            "Why is '{0}' significant in human physiology?:",
            "In studying human microscopic tissues, '{0}' refers to:",
            "Which statement correctly accounts for the structure and function of: '{0}'?:",
            "What is the biological reality regarding: '{0}'?:",
            "A practical exam tests human cell preparation: '{0}'. The correct answer is:",
            "How does cellular architecture relate to function in: '{0}'?:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand human cell morphology and function.**\nHuman tissues contain specialized cells with diverse structures tailored to their physiological roles.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Measurement of Microscopic Specimens: Micrometry and Scale Calculation
    arch7 = {
        'data': [
            ("Convert 0.05 millimetres (mm) to micrometres (μm)", 50.0, "0.05 mm * 1000 = 50 μm", "5.0 μm, 500 μm, 0.0005 μm"),
            ("Convert 750 nanometres (nm) to micrometres (μm)", 0.75, "750 nm / 1000 = 0.75 μm", "7.5 μm, 75 μm, 0.075 μm"),
            ("Convert 2.5 micrometres (μm) to nanometres (nm)", 2500.0, "2.5 μm * 1000 = 2500 nm", "250 nm, 25000 nm, 0.0025 nm"),
            ("An image of a cell measures 30 mm across. The actual cell size is 60 μm. Calculate the magnification of the image", 500.0, "Magnification = Image size / Actual size = 30 mm / 0.06 mm = 500x", "50x, 5000x, 2x"),
            ("A microscopic organism is viewed under 400x magnification and appears 16 mm long. Calculate its actual length in micrometres (μm)", 40.0, "Actual size = Image size / Magnification = 16 mm / 400 = 0.04 mm = 40 μm", "4.0 μm, 400 μm, 0.4 μm"),
            ("The field of view of a microscope under 100x magnification is 2.0 mm. Exactly 10 onion cells fit end-to-end across the diameter. What is the average length of one onion cell?", 200.0, "Average length = 2.0 mm / 10 = 0.2 mm = 200 μm", "20 μm, 2000 μm, 50 μm"),
            ("If the field of view diameter under 100x magnification is 2.0 mm, what will be the field of view diameter under 400x magnification?", 0.5, "Field diameter decreases inversely with magnification: 2.0 mm * (100 / 400) = 0.5 mm = 500 μm", "8.0 mm, 0.25 mm, 1.0 mm"),
            ("A bacterium of actual length 2.0 μm is photographed under an electron microscope with a scale bar where 1 cm represents 0.5 μm. How long does the bacterium appear in the photograph?", 4.0, "Image length = Actual size * Scale = 2.0 μm * (1 cm / 0.5 μm) = 4.0 cm", "1.0 cm, 8.0 cm, 0.5 cm"),
            ("Calculate total magnification when using a 15x ocular eyepiece and a 40x high-power objective lens", 600.0, "Total magnification = Eyepiece magnification * Objective magnification = 15 * 40 = 600x", "55x, 400x, 6000x"),
            ("A red blood cell has a diameter of 7.5 μm. How many red blood cells placed side-by-side in a straight row would span a length of 1.5 cm?", 2000.0, "Number of cells = Total length / Cell diameter = 15000 μm / 7.5 μm = 2000 cells", "200 cells, 20000 cells, 750 cells")
        ],
        'templates': [
            "In microscopic calculations: '{0}'. Determine the correct numerical result:",
            "Solve the microscopy measurement problem: '{0}':",
            "Calculate the required parameter: '{0}':",
            "A student performs cell micrometry: '{0}'. The correct calculated answer is:",
            "In optical magnification calculations: '{0}'. The result equals:",
            "Determine the actual size, magnification, or dimension from: '{0}':",
            "Evaluate the microscopy problem: '{0}':",
            "From the practical microscopy data: '{0}'. Calculate the answer:",
            "Solve the dimensional micrometry task: '{0}':",
            "A biology exam asks: '{0}'. The accurate numerical solution is:"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\)" if isinstance(item[1], (int, float)) else str(item[1]),
            split_options(item[3]),
            f"**Step 1: State the micrometry formula.**\n\\(\\text{{Magnification}} = \\frac{{\\text{{Image Size}}}}{{\\text{{Actual Size}}}}\\), \\(\\text{{Actual Size}} = \\frac{{\\text{{Image Size}}}}{{\\text{{Magnification}}}}\\).\nEnsure all units are converted to the same metric scale (\\(1\\text{{ mm}} = 1000\\, \\mu\\text{{m}} = 10^6\\text{{ nm}}\\)).\n\n**Step 2: Substitute and compute.**\n{item[2]}.\n\n**Step 3: Result:** **{item[1]}**."
        ),
        'diff': 'medium'
    }

    # Arch 8: Scientific Methodology of Early Microscopy: Rigor and Reproducibility
    arch8 = {
        'data': [
            ("Why the Royal Society of London sent a delegation to Delft to inspect Leeuwenhoek's experiments", "Scientific peer review and empirical verification: claims of microscopic living creatures in water were so astonishing that independent replication was mandatory", "Required confirmation by reputable natural philosophers before publication in Philosophical Transactions", "To arrest Leeuwenhoek for heresy, To buy all his microscopes for the King's army, To teach Leeuwenhoek how to speak English"),
            ("Role of Robert Hooke in validating Leeuwenhoek's discoveries", "Hooke constructed specialized single-lens microscopes and successfully replicated the observation of swimming bacteria and protozoa in pepper infusions", "Hooke's confirmation established Leeuwenhoek's global scientific credibility within the Royal Society", "Hooke declared Leeuwenhoek's drawings were imaginary cartoons, Hooke took credit for Leeuwenhoek's discovery, Hooke sued the Royal Society"),
            ("Significance of Leeuwenhoek's precise quantitative measurements using hair breadths and grains of sand", "Leeuwenhoek calibrated specimen sizes against known comparative physical references (e.g. diameter of a coarse sand grain ~1 mm, human hair ~100 μm)", "Pioneered quantitative biological scaling long before international standard metric micrometre grids existed", "Used arbitrary imaginary numbers with no reference, Refused to estimate sizes of organisms, Claimed all animalcules were 1 metre long"),
            ("Why Leeuwenhoek did NOT propose a unified Cell Theory in the 17th century", "He viewed animalcules as autonomous whole animal organisms rather than universal modular building blocks of all tissues", "Lack of comparative histology across diverse plant and animal tissues delayed the generalization for 160 years", "Because his religious beliefs banned theories, Because he lost all his notebooks in a fire, Because he thought plants were not alive"),
            ("Importance of detailed botanical and biological illustrations in early cytology", "Exquisite copperplate engravings in Micrographia and Leeuwenhoek's letters allowed scientists worldwide to visually examine and verify discoveries", "Visual evidence was vital when very few individuals owned functional high-power microscopes", "Illustrations were used only to decorate the book for sale, Drawings replaced the need for conducting experiments, All early drawings were deliberately distorted"),
            ("Concept of 'Animalcule' vs modern taxonomic domains", "Leeuwenhoek's 'animalcules' lumped together distinct domains of life: Bacteria (prokaryotes) and Protista (eukaryotes)", "Modern taxonomy classifies them into Bacteria, Archaea, and Eukarya based on rRNA sequencing and cellular ultrastructure", "Animalcules are all classified as chordate animals today, Animalcules are non-living minerals, Animalcules are exclusively RNA viruses"),
            ("The shift from Aristotelian qualitative teleology to empirical microscopic observation", "17th-century microscopists replaced scholastic philosophical debate with direct instrumental observation and repeatable testing", "Formed the cornerstone of the modern scientific method championed by the Royal Society's motto 'Nullius in verba' (Take nobody's word for it)", "Replaced experimental evidence with ancient Greek myths, Banned all laboratory instruments, Claimed human eyes can see everything without tools"),
            ("Legacy of Anton van Leeuwenhoek in modern science", "Universally acknowledged as the 'Father of Microbiology' and pioneer of microscopic cytology", "Opened an entire previously invisible microscopic universe containing the vast majority of Earth's biological biodiversity", "Remembered only as a linen cloth merchant, Discredited for discovering non-existent creatures, Named the Father of Quantum Mechanics"),
            ("Reproducibility as a core tenet of the scientific method demonstrated in early cytology", "A scientific observation is valid only if independent researchers in different laboratories can replicate the result under identical conditions", "Demonstrated when Hooke and British investigators independently verified Leeuwenhoek's pepper-infusion animalcules", "Scientific truth is determined by who has the most money, A single unrepeated observation is accepted as absolute universal dogma, Replication is considered an insult to the original discoverer"),
            ("Difference between Hooke's compound microscope and Leeuwenhoek's simple microscope", "Hooke's microscope was a compound system (two lenses: objective and eyepiece); Leeuwenhoek's microscope was a simple system (single high-power biconvex bead lens)", "Compound system suffered from multi-lens aberrations, while the simple bead lens achieved higher resolution and magnification in the 1670s", "Hooke used an electron beam while Leeuwenhoek used sunlight, Hooke's microscope was simple while Leeuwenhoek's was compound, Both were identical factory-built instruments")
        ],
        'templates': [
            "In the philosophy and history of scientific discovery: '{0}'. What is the correct scientific insight?:",
            "Regarding the methodology of early cytology: '{0}' demonstrates that:",
            "What scientific principle is illustrated by: '{0}'?:",
            "Analyze the historical context of early microbiology: '{0}' shows that:",
            "Which statement accurately explains the significance of: '{0}'?:",
            "How did '{0}' advance the foundational standards of the scientific method?:",
            "In evaluating scientific rigor in 17th-century microscopy: '{0}' represents:",
            "What is the historical reality and scientific importance of: '{0}'?:",
            "A science history seminar examines early cytology: '{0}'. The accurate conclusion is:",
            "Which of the following correctly characterizes: '{0}'?:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand early scientific methodology.**\nEarly cytological discoveries established modern peer review, replication, comparative quantification, and empirical validation.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-2-2.1.2", "Anton van Leeuwenhoek free living cells", archs)


# ==============================================================================
# SUBTOPIC 2.1.3: Cell Theory: Schleiden, Schwann, Virchow (Omnis cellula-e-cellula)
# Topic Code: CBSE-9-SCIE-2-2.1.3
# ==============================================================================
def gen_2_1_3():
    # Arch 1: Formulation of Classical Cell Theory by Schleiden and Schwann
    arch1 = {
        'data': [
            ("Matthias Schleiden (1838)", "German botanist who examined thousands of plant specimens and concluded that all plants are composed of cells", "Asserted that cells are the fundamental structural units of all plant tissues", "English physicist who discovered universal gravitation, French chemist who invented rabies vaccination, Austrian monk who discovered genetics"),
            ("Theodor Schwann (1839)", "German zoologist who studied diverse animal tissues and concluded that all animals are composed of cells and cell products", "Identified the delicate outer plasma membrane of animal cells and noted that plant cells possess a unique outer cell wall", "Italian physician who discovered malaria parasites, Scottish botanist who discovered plant nuclei, German physicist who discovered X-rays"),
            ("Unification of Classical Cell Theory (1839)", "Joint formulation by Schleiden and Schwann stating: (1) All living organisms are composed of one or more cells; (2) The cell is the basic structural unit of life", "First universal biological generalization uniting the plant and animal kingdoms under a common architectural principle", "Claimed that cells are created by spontaneous combustion, Stated that all cells are square and lack membranes, Declared that animals are made of cells but plants are made of rocks"),
            ("Major flaw or limitation in Schleiden and Schwann's original 1839 Cell Theory", "They failed to explain how new cells actually arise, mistakenly proposing 'de novo' crystallization from a free cellular fluid ('cytoblastema')", "Schleiden believed that new cells crystallize around the nucleus inside older cells, similar to inorganic crystals growing in solution", "They denied that cells contain nuclei, They claimed animal cells have thick wooden cell walls, They stated that humans are not composed of cells"),
            ("Schwann's comparative observation of plant vs animal cells (1839)", "Observed that animal cells are bounded only by a delicate outer membrane, whereas plant cells possess a distinct thick outer rigid cell wall", "Recognized that the presence of a cell wall is a distinguishing unique feature of plant tissues", "Claimed animal cells have no membranes, Stated plant cells have no cytoplasm, Claimed both are completely identical with no differences"),
            ("Robert Brown's discovery of the Nucleus (1831) as a precursor to Cell Theory", "Scottish botanist who observed and named the 'nucleus' as a constant spherical organelle in orchid epidermal cells", "Convinced Schleiden and Schwann that cells possess an organized, universal internal anatomy", "Discovered the cell wall in cork, Discovered bacteria in milk, Invented the electron microscope"),
            ("Jan Evangelista Purkinje (1839) coining of 'Protoplasm'", "Coined the term 'protoplasm' for the fluid living colloidal substance of the cell (cytoplasm + nucleus)", "Shifted biological focus from the non-living outer cell wall to the living dynamic interior", "Coined the term chromosome, Discovered mitochondria, Invented tissue culture"),
            ("Felix Dujardin (1835) and the discovery of 'Sarcode'", "French biologist who observed the living jelly-like substance inside protozoa and named it 'sarcode'", "Demonstrated that living matter possesses contractile, viscous properties distinct from non-living fluids", "Discovered that protozoa are made of mineral glass, Claimed single cells have human-like brains, Discovered blood capillaries"),
            ("Max Schultze (1861) and the 'Protoplasm Theory'", "Defined the cell as 'a lump of nucleated protoplasm with or without a cell wall'", "Firmly established that protoplasm is the physical basis of life (Thomas Huxley's phrase: 'physical basis of life')", "Claimed that protoplasm is an inert mineral oil, Stated that nuclei are parasitic invaders, Concluded that cell walls are the only living part"),
            ("Modern Classical Cell Theory core postulates", "(1) All living organisms are composed of one or more cells; (2) The cell is the structural and functional unit of life; (3) All cells arise from pre-existing cells", "Forms the unifying foundational cornerstone of all modern biological sciences", "All cells can transform into viruses spontaneously; Cells are generated by dirt and water; Only plants are made of cells, animals are made of fluid")
        ],
        'templates': [
            "In the history and formulation of Cell Theory: '{0}'. Identify the true statement:",
            "What contribution or concept is associated with: '{0}'?:",
            "Regarding the foundational postulates of Cell Theory: '{0}' is characterized as:",
            "A student learns about the history of cytology: '{0}'. The accurate biological fact is:",
            "Which statement correctly describes the scientific milestone: '{0}'?:",
            "Analyze the historical cytological development: '{0}' established:",
            "What was the critical significance of: '{0}'?:",
            "In classical cell biology, '{0}' refers to:",
            "How did '{0}' advance the unification of biological sciences?:",
            "A biology question tests Cell Theory origins: '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand the formulation of Cell Theory.**\n- **1838:** Matthias Schleiden (plants are made of cells).\n- **1839:** Theodor Schwann (animals are made of cells; cell wall distinguishes plants).\n- **Combined:** All living things are composed of cells; the cell is the unit of life.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Rudolf Virchow and 'Omnis cellula-e-cellula' (1855)
    arch2 = {
        'data': [
            ("Rudolf Virchow (1855)", "German pathologist who modified Cell Theory by proposing the principle 'Omnis cellula-e-cellula'", "Asserted that all new cells arise exclusively from the division of pre-existing cells through binary fission or mitosis", "Discovered that cells crystallize from chemical soups, Claimed that cancer is caused by angry spirits, Discovered DNA polymerase"),
            ("Meaning of the Latin aphorism 'Omnis cellula-e-cellula'", "'All cells arise from pre-existing cells'", "Overthrew the erroneous belief of de novo cell crystallization from cytoblastema and finally completed the unified Cell Theory", "All cells are square; All cells have cell walls; Cells are immortal and never divide"),
            ("Virchow's contribution to Cellular Pathology (1858)", "Demonstrated that diseases (such as cancer and inflammation) originate at the cellular level ('diseased cells arise from normal cells')", "Established modern clinical pathology by connecting anatomical symptoms to cellular abnormalities", "Claimed diseases are caused by an imbalance of four humors (blood, phlegm, black bile, yellow bile), Stated that bacteria do not exist, Asserted that organs are independent of cells"),
            ("Robert Remak's prior discovery (1852) of cell division", "Polish-German embryologist who first observed cell division in red blood cells and frog eggs, demonstrating that cells multiply by splitting", "Virchow popularized Remak's observation into the universal biological doctrine 'Omnis cellula-e-cellula'", "Invented the compound microscope, Discovered that cells do not divide, Claimed eggs are formed by spontaneous generation"),
            ("How Virchow's postulate refuted spontaneous generation at the cellular level", "By demonstrating that living cells never emerge from inorganic broths or non-cellular cytoblastema, but only via cellular replication", "Aligned cytological theory with Louis Pasteur's subsequent swan-neck flask experiments on biogenesis", "Proved that bacteria generate spontaneously in blood, Claimed that rocks turn into cells when heated, Stated that viruses are created by dirt"),
            ("Cytological mechanism underlying 'Omnis cellula-e-cellula' in eukaryotes", "Mitosis and Meiosis: precise nuclear division ensuring equal distribution of replicated chromosomes to daughter cells", "Guarantees genetic continuity and transmission of hereditary DNA from generation to generation", "Crystallization of proteins around a nucleolus, Spontaneous explosion of the mother cell, Direct absorption of surrounding food into new cells"),
            ("Cytological mechanism underlying 'Omnis cellula-e-cellula' in prokaryotes", "Binary fission: circular chromosome replication, cell elongation, and septum formation yielding two clonal daughter cells", "Enables rapid exponential population growth in bacteria under favorable nutrient conditions", "Meiotic crossing over, Spontaneous de novo synthesis from agar, Budding of multicellular larvae"),
            ("The continuity of life from the first primordial cell to modern organisms", "Every living cell on Earth today represents an unbroken, continuous lineage of cell divisions extending back ~3.8 billion years to LUCA (Last Universal Common Ancestor)", "Underpins the evolutionary unity and genetic homology shared across all living kingdoms", "Cells are freshly created every day from rainwater, Each human generation starts from newly crystallized chemical mud, Plant cells have no evolutionary relationship to animal cells"),
            ("Virchow's rejection of 'blastema' and 'free-cell formation'", "Categorically rejected Schleiden's idea that cells precipitate out of an unorganized organic soup like sugar crystals", "Demonstrated that every cell boundary and nucleus traces its parentage directly to a preceding cell", "Asserted that blastema is the only way cells reproduce, Claimed cell division is impossible, Believed cells are formed inside mitochondria"),
            ("Modern three-part definition of Cell Theory (Unified)", "(1) All living organisms are composed of one or more cells; (2) The cell is the fundamental structural and functional unit of life; (3) All cells arise from pre-existing cells by division", "Universally taught as the primary foundation of biological sciences", "Cells are created from energy and light; Viruses are the ancestors of all humans; Only multicellular organisms have cells")
        ],
        'templates': [
            "In cytology and evolutionary biology: '{0}'. Identify the correct scientific statement:",
            "What landmark contribution is represented by: '{0}'?:",
            "Regarding Rudolf Virchow's role in Cell Theory: '{0}' is characterized as:",
            "A biology student learns about '{0}'. The accurate scientific fact is:",
            "Which statement correctly explains: '{0}'?:",
            "Analyze the historical doctrine: '{0}' established that:",
            "Why was '{0}' critical in finalizing modern Cell Theory?:",
            "In cellular pathology and biology, '{0}' refers to:",
            "How did '{0}' revolutionize contemporary understanding of life?:",
            "A question on Cell Theory postulates asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Rudolf Virchow's 1855 contribution.**\nRudolf Virchow completed the classical Cell Theory by adding the third postulate:\n**'Omnis cellula-e-cellula'** ({item[1]}).\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Biological meaning:**\n{item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 3: Exceptions and Edge Cases to the Classical Cell Theory
    arch3 = {
        'data': [
            ("Viruses as an exception to Cell Theory", "Acellular entities lacking cytoplasm, organelles, and metabolic machinery; composed only of a nucleic acid genome (DNA or RNA) enclosed in a protein capsid", "Obligate intracellular parasites that exhibit living traits (replication, mutation) only inside a host cell, but remain inert crystals outside", "Viruses are multicellular fungi, Viruses have thick cellulose cell walls, Viruses reproduce by binary fission in pond water"),
            ("Viroids as an exception to Cell Theory", "Infectious sub-viral agents consisting exclusively of a tiny, circular, single-stranded non-coding RNA molecule lacking any protein coat", "Cause devastating agricultural plant diseases (e.g. potato spindle tuber viroid) without cellular structure", "Viroids are giant eukaryotic cells, Viroids have nuclei and chloroplasts, Viroids are motile protozoans"),
            ("Prions as an exception to Cell Theory", "Infectious misfolded proteins that contain zero genetic material (no DNA or RNA) and propagate by inducing normal cellular proteins to misfold", "Cause fatal neurodegenerative transmissible spongiform encephalopathies (e.g. BSE / Mad Cow Disease, CJD in humans)", "Prions are multicellular bacteria, Prions have lipid bilayer membranes, Prions reproduce by meiosis"),
            ("Coenocytic (Aseptate) Fungi (e.g. Rhizopus, Mucor)", "Multinucleate continuous cytoplasmic tubes lacking dividing transverse cross-walls (septa)", "A single continuous filamentous hypha contains thousands of nuclei without discrete cellular boundaries, challenging the 'one cell = one nucleus' concept", "Composed of discrete single cells with separate cell walls, Unicellular flagellated algae, Acellular viral particles"),
            ("Siphonaceous green algae (e.g. Vaucheria, Caulerpa)", "Giant macroscopic multinucleate organisms formed of a single continuous coenocytic siphon up to a metre long without internal septa", "Demonstrates that complex macroscopic morphology can develop without partitioning into individual cellular compartments", "Multicellular flowering plants, Microscopic bacteria, Colonial animals with bones"),
            ("Mature mammalian red blood cells (Erythrocytes)", "Lack a nucleus, mitochondria, and endoplasmic reticulum at functional maturity", "Can survive and transport oxygen for ~120 days but cannot synthesize proteins, repair damage, or divide", "Divide rapidly by mitosis in bloodstream, Have 5 nuclei per cell, Are multicellular tissue fragments"),
            ("Mature plant phloem sieve tube elements", "Lack a nucleus, vacuole, and ribosomes at maturity, yet remain alive and transport phloem sap", "Survive dependent upon adjacent nucleated companion cells connected via specialized plasmodesmatal pore complexes", "Dead hollow tubes like xylem vessels, Completely independent autotrophic cells, Giant multinucleate amoebae"),
            ("Slime molds (Plasmodial Myxomycetes, e.g. Physarum)", "A giant, acellular, multinucleate mass of protoplasm (plasmodium) that streams and creeps amoeboid-style over rotting wood", "Contains millions of nuclei suspended in a common shared cytoplasm bounded by a single outer membrane", "Multicellular insects, Colonies of photosynthetic algae, Pure non-living mineral crystals"),
            ("Why viruses are called a 'biological puzzle' or borderline between living and non-living", "Non-living traits: acellular, can be crystallized (Wendell Stanley, 1935), zero metabolic respiration outside host; Living traits: possess genetic material, replicate, mutate, and evolve inside living cells", "Demonstrates that life's properties exist along a continuum rather than a rigid binary divide", "Because viruses are made of pure gold, Because viruses can fly like birds, Because viruses are living plants in air"),
            ("How modern cell biologists view the 'Cell Theory exceptions'", "The cell remains the universal fundamental operational unit of all free-living autonomous life; viruses, prions, and syncytia are specialized sub-cellular or supra-cellular evolutionary adaptations", "Exceptions do not invalidate Cell Theory but refine its scope to autonomous metabolizing living systems", "Exceptions prove Cell Theory is completely false and must be discarded, Modern science has abandoned cells, All living organisms are now classified as viruses")
        ],
        'templates': [
            "In analyzing exceptions to the classical Cell Theory: '{0}'. What is the accurate scientific fact?:",
            "Why is '{0}' considered a major exception or edge-case to classical Cell Theory?:",
            "Regarding biological entities that challenge traditional Cell Theory: '{0}' is characterized by:",
            "A biology student studies non-cellular life: '{0}'. The correct biological explanation is:",
            "Which statement accurately explains why '{0}' represents a limitation of Cell Theory?:",
            "Analyze the biological structure: '{0}'. Its relationship to Cell Theory is:",
            "What structural reality explains why '{0}' does not fit standard cellular definitions?:",
            "In modern cytology, '{0}' is understood as:",
            "How does contemporary biology classify and account for: '{0}'?:",
            "A question on Cell Theory limitations asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Identify exceptions to the classical Cell Theory.**\n- **Acellular entities (Viruses, Viroids, Prions):** Lack cytoplasm, membranes, and independent metabolism.\n- **Coenocytic/Syncytial organisms (Rhizopus, Vaucheria, Slime molds):** Continuous multinucleate protoplasm without discrete cross-walls.\n- **Aneuploid/Enucleated living units:** Mature mammalian RBCs and sieve tube elements.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Modern Cell Theory (Cell Principle / Cell Doctrine)
    arch4 = {
        'data': [
            ("First tenet of Modern Cell Theory", "All known living organisms are composed of one or more cells and their products", "Applies universally across Monera, Protista, Fungi, Plantae, and Animalia", "All organisms are composed of inorganic minerals, Living organisms have no structural units, Only plants are made of cells"),
            ("Second tenet of Modern Cell Theory", "The cell is the basic structural, physiological, and functional unit of all living organisms", "Every vital metabolic reaction (glycolysis, respiration, protein synthesis) takes place within the cellular boundary", "The organ is the smallest functional unit of life, Life only functions at the macroscopic level, Molecules function without cells"),
            ("Third tenet of Modern Cell Theory", "All cells arise exclusively from pre-existing cells through cellular division (mitosis, meiosis, or binary fission)", "Continuous cellular lineage linking modern organisms back to the origin of life on Earth", "Cells are created de novo from non-living chemicals daily, Cells crystallize from air, Cells are formed inside volcanic rocks"),
            ("Fourth tenet of Modern Cell Theory (Genetic continuity)", "Cells contain hereditary genetic material (DNA) that is replicated and passed from parent cell to daughter cells during division", "Encodes instructions for cellular structure, enzymatic functions, and physiological regulation", "Cells pass their memories through spiritual telepathy, Hereditary information is carried in cell walls, Genetic material changes randomly every second"),
            ("Fifth tenet of Modern Cell Theory (Chemical and biochemical unity)", "All cells share fundamentally similar chemical composition, genetic code (universal triplet codons), and metabolic pathways (e.g. ATP currency, glycolysis)", "Demonstrates that all life on Earth evolved from a common universal ancestral ancestor (LUCA)", "Every species has a completely different genetic code, Plant cells use silicon while animal cells use carbon, Energy in cells is stored as pure electricity"),
            ("Sixth tenet of Modern Cell Theory (Energy flow and metabolism)", "All energy transformations (metabolism, cellular respiration, photosynthesis) of life occur within cells", "Cells maintain a dynamic steady state (homeostasis) far from thermodynamic equilibrium by consuming free energy", "Cells do not require energy to live, Energy flows only between whole organisms, Cells produce energy out of nothing"),
            ("Activity of an organism depends on total cellular activities", "The collective physiological behavior of a multicellular organism is the sum of the coordinated activities, communications, and interactions of its constituent cells", "Emergent properties arise at tissue and organ levels from specialized cellular cooperation", "An organism's life is independent of its cells, Cells in an organism operate as enemies competing to kill each other, Organs function even if all their cells die"),
            ("Definition of Homeostasis at the cellular level", "The maintenance of a stable, constant internal physiological and chemical environment (pH, ion concentrations, osmotic balance, temperature) within the cell", "Regulated by selective membrane transport, enzyme kinetics, and feedback signaling loops", "Complete equilibrium with the outside environment where inside equals outside, The state of cell death, Uncontrolled rapid fluctuation of cell contents"),
            ("Why the cell is considered the 'Unit of Life'", "Because no component smaller than a complete, membrane-enclosed, metabolizing cell is capable of independent autonomous life", "Isolated organelles (mitochondria, nucleus, ribosomes) cannot survive or replicate independently outside the cellular environment", "Because cells are large enough to be seen with magnifying glasses, Because atoms cannot combine without magic, Because cells are eternal and never perish"),
            ("Unicellular vs Multicellular organism organization in Modern Cell Theory", "In unicellular organisms, all vital life functions (nutrition, respiration, excretion, reproduction) are performed by a single autonomous cell; in multicellular organisms, division of labor assigns specialized functions to distinct cell types", "Cell specialization enables complex tissue, organ, and system-level physiological efficiency", "Unicellular organisms are not alive, Multicellular organisms have only one giant cell, In multicellular organisms every cell performs identical functions")
        ],
        'templates': [
            "In modern cell biology, what is: '{0}'?:",
            "According to the tenets of Modern Cell Theory (Cell Doctrine): '{0}' states that:",
            "Which statement accurately expresses the modern biological principle: '{0}'?:",
            "Analyze the foundational biological concept: '{0}'. The accurate statement is:",
            "How does Modern Cell Theory define and explain: '{0}'?:",
            "In advanced cytology, '{0}' is characterized as:",
            "What is the significance of the cell doctrine postulate: '{0}'?:",
            "Identify the scientifically rigorous explanation for: '{0}':",
            "Which of the following aligns with the core tenet: '{0}'?:",
            "A biology examination tests the modern cell doctrine: '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Modern Cell Theory (Cell Doctrine).**\nExpands classical theory by incorporating biochemistry, genetics, and thermodynamics:\n1. All organisms are composed of cells.\n2. Cell is the unit of structure and function.\n3. Cells arise from pre-existing cells.\n4. Energy flows within cells (metabolism).\n5. DNA passes from cell to cell.\n6. All cells share basic chemical composition.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 5: Levels of Structural Organization: Organelles to Organism
    arch5 = {
        'data': [
            ("Correct hierarchical sequence of biological structural organization in multicellular organisms", "Organelles \\(\\rightarrow\\) Cells \\(\\rightarrow\\) Tissues \\(\\rightarrow\\) Organs \\(\\rightarrow\\) Organ Systems \\(\\rightarrow\\) Organism", "Each ascending level exhibits novel emergent properties that cannot be predicted from lower levels alone", "Cells \\(\\rightarrow\\) Organs \\(\\rightarrow\\) Tissues \\(\\rightarrow\\) Organ Systems; Organelles \\(\\rightarrow\\) Organisms \\(\\rightarrow\\) Tissues; Tissues \\(\\rightarrow\\) Cells \\(\\rightarrow\\) Organelles"),
            ("Definition of a 'Tissue' in multicellular biology", "A cooperative group of structurally similar cells, along with their extracellular matrix, performing a specific shared physiological function (e.g. muscular tissue, vascular xylem)", "Possesses specialized biochemical and morphological adaptations tailored to its function", "A collection of unrelated organs, A group of different whole organisms living together, A single giant multi-membrane organelle"),
            ("Definition of an 'Organ' in biology", "A distinct anatomical structure composed of two or more different tissue types working together to perform complex physiological activities (e.g. stomach, leaf, heart)", "Combines multiple tissues (e.g. stomach contains epithelial, muscular, connective, and nervous tissues)", "A single isolated cell floating in blood, An individual organelle inside a cell, A population of organisms of the same species"),
            ("Definition of an 'Organ System'", "A group of interconnected organs that coordinate collectively to execute a vital life function (e.g. digestive system, circulatory system, plant vascular system)", "Ensures systemic integration across the whole organism", "A single tissue layer covering the body, A subcellular protein machine, An ecological community in a forest"),
            ("Concept of 'Emergent Properties' in biological hierarchy", "Novel, complex properties that arise at higher levels of organization that were not present in the individual lower-level components alone (e.g. consciousness emerges from brain circuits, not single neurons)", "The whole is greater than the simple arithmetic sum of its individual parts", "Properties that disappear as organisms grow larger, The spontaneous generation of new chemical elements, The decay of living matter into pure entropy"),
            ("Division of Labor in multicellular organisms", "Specialization of different cell types and tissues to execute specific dedicated functions, maximizing whole-organism efficiency", "E.g. muscle cells contract, red blood cells carry oxygen, nerve cells transmit impulses, xylem vessels conduct water", "Every cell trying to perform all life processes simultaneously, Cells fighting for food until only one survives, Tissues shutting down to save energy"),
            ("Division of Labor within a single unicellular cell (Intracellular division of labor)", "Partitioning of specific metabolic pathways into membrane-bound organelles (e.g. ATP production in mitochondria, protein synthesis in rough ER/ribosomes, photosynthesis in chloroplasts)", "Allows incompatible biochemical reactions (e.g. protein synthesis vs protein degradation in lysosomes) to occur simultaneously in separate compartments", "The cell splitting into multiple separate animals, Organelles consuming each other for food, The nucleus taking over all cytoplasm functions"),
            ("Plant vs Animal organ system integration", "Animals possess specialized nervous and endocrine systems for rapid coordination and sensory integration; Plants coordinate organs via hormone signaling (phytohormones) and plasmodesmatal transport", "Reflects the motile heterotrophic lifestyle of animals versus the sessile autotrophic lifestyle of plants", "Plants have human-like nervous systems with brains, Animals lack organ systems and have only tissues, Neither plants nor animals have internal communication"),
            ("Tissue level organization in simple multicellular animals (e.g. Cnidaria / Hydra)", "Possesses distinct epithelial and nerve net tissues, but lacks true specialized organs and organ systems", "Represents an intermediate evolutionary stage between colonial protists and triploblastic organ-grade animals", "Has complete digestive and respiratory organ systems with lungs, Possesses a bony skeleton and brain, Is a unicellular bacterium"),
            ("Cellular autonomy vs organismic interdependence", "An isolated muscle cell in culture can contract independently, but in the body its survival depends entirely on the circulatory, respiratory, and nervous systems", "Multicellularity trades complete cellular self-sufficiency for collective physiological prowess and longevity", "Cells inside an organism are completely independent and do not need blood or food, Cells die instantly the moment a tissue is formed, Organisms have no cellular foundation")
        ],
        'templates': [
            "In hierarchical biological organization: '{0}'. Identify the correct scientific fact:",
            "What biological principle or level is defined as: '{0}'?:",
            "Regarding structural complexity in multicellular organisms: '{0}' is characterized by:",
            "A student examines the hierarchy from molecules to ecosystems: '{0}'. The accurate concept is:",
            "Which statement correctly describes: '{0}'?:",
            "Analyze the organizational biological principle: '{0}' demonstrates that:",
            "What is the functional significance of: '{0}'?:",
            "In comparative anatomy and physiology, '{0}' refers to:",
            "How does contemporary biology explain: '{0}'?:",
            "A question on biological hierarchy asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand biological hierarchy.**\nOrganelles \\(\\rightarrow\\) Cells \\(\\rightarrow\\) Tissues \\(\\rightarrow\\) Organs \\(\\rightarrow\\) Organ Systems \\(\\rightarrow\\) Organism.\n\n**Step 2: Key concept:**\nAt each ascending level, **emergent properties** arise from coordinated interactions and division of labor.\n\n**Step 3: Evaluate '{item[0]}'.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Cell Size, Shape Diversity, and Surface-Area-to-Volume Ratio
    arch6 = {
        'data': [
            ("Smallest known free-living cellular organism", "Mycoplasma (PPLO - Pleuropneumonia-like organisms)", "Approximately 0.1 to 0.3 micrometres (μm) in diameter; lacks a cell wall and has the smallest genome", "Ostrich egg, Human cheek cell, Amoeba proteus"),
            ("Largest single isolated cell in the biological world", "Ostrich egg (unfertilized)", "Measures approximately 15 to 18 cm across; the massive size is largely non-living yolk (nutrient reserve) surrounding a microscopic blastodisc", "Human ovum, Acetabularia, Whale neuron"),
            ("Longest cells in the human body", "Neurons (Nerve cells)", "Can reach lengths over 1 metre (e.g. sciatic nerve axons running from the base of the spinal cord to the tips of the toes)", "Erythrocytes, Skeletal muscle myocytes, Skin epidermal cells"),
            ("Smallest cell in the human body", "Human sperm cell (or cerebellar granule cell neuron)", "Sperm head measures only ~3 to 5 μm long and 2 to 3 μm wide, with minimal cytoplasm", "Human ovum, Liver hepatocyte, Cardiac muscle cell"),
            ("Largest cell in the human body", "Human ovum (unfertilized egg cell)", "Measures approximately 100 to 120 micrometres (0.1 mm) in diameter; visible to the naked eye as a tiny speck", "Red blood cell, Human sperm, Platelet"),
            ("Relationship between cell size and Surface-Area-to-Volume (SA/V) ratio", "As a cell grows larger in volume (\\(V \\propto r^3\\)), its surface area increases much more slowly (\\(\\text{SA} \\propto r^2\\)), causing the SA/V ratio to decrease drastically (\\(\\text{SA/V} \\propto 1/r\\))", "A low SA/V ratio critically limits the rate of nutrient diffusion, gas exchange, and waste removal across the plasma membrane", "As a cell grows larger its SA/V ratio increases to infinity, Cell size has zero mathematical relationship to surface area, Larger cells absorb nutrients much faster per unit volume"),
            ("Why cells divide upon reaching a critical size threshold (Nucleo-cytoplasmic ratio / Kernplasma ratio)", "To restore an optimal high Surface-Area-to-Volume ratio and ensure the single nucleus can effectively control metabolic processes across the cytoplasm", "When cell volume outgrows the transcriptional and diffusion capacity of the nucleus, division is triggered", "Because cells get tired of being large, To destroy excess DNA, Because cell walls melt when volume increases"),
            ("Cellular shape adaptations to maximize Surface-Area-to-Volume ratio", "Flattened cells (squamous epithelium), thin elongated cylinders (neurons, root hairs), and surface microvilli folds (intestinal brush border)", "Drastically elevates surface area for rapid absorption or transmission without expanding intracellular volume", "Transforming into giant spherical spheres, Eliminating the plasma membrane, Filling with heavy mineral crystals"),
            ("Shape diversity in human cells matched to specialized functions", "Biconcave RBCs (flexible passage through capillaries), Branched neurons (transmitting signals across distances), Spindle smooth muscle (contractile force), Ciliated columnar (sweeping mucus)", "Form strictly follows function (morphological adaptation)", "All human cells are identical perfect spheres, Shape is completely random and has no relationship to function, Cells change their shape to mimic insects"),
            ("Unicellular giant alga Acetabularia (Mermaid's wineglass)", "A giant single-celled green marine alga reaching 5 to 10 cm in height with distinct rhizoid, stalk, and cap, controlled by a single nucleus in the rhizoid", "Used by Joachim Hämmerling in grafting experiments (1930s-1940s) to prove that the nucleus controls morphogenesis and cellular heredity", "A multicellular flowering tree, A colonial animal with bones, A microscopic bacterium")
        ],
        'templates': [
            "In comparative cytology and cellular biophysics: '{0}'. Identify the correct scientific fact:",
            "What biological reality explains: '{0}'?:",
            "Regarding cell size and morphology: '{0}' is characterized by:",
            "A biology student calculates dimensions: '{0}'. The accurate physical principle is:",
            "Which statement correctly accounts for: '{0}'?:",
            "Analyze the relationship between geometry and cellular function: '{0}' demonstrates:",
            "What is the mathematical or physiological reason for: '{0}'?:",
            "In cell biology, '{0}' refers to:",
            "Why is '{0}' significant in cellular physiology?:",
            "A question on cell size limits asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand cell size limits and geometry.**\n- Surface area \\(\\propto r^2\\); Volume \\(\\propto r^3\\).\n- \\(\\frac{{\\text{{SA}}}}{{\\text{{V}}}} \\propto \\frac{{1}}{{r}}\\).\n- Smaller cells have higher SA/V ratios, enabling rapid nutrient and gas diffusion.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Joachim Hämmerling's Acetabularia Experiments: Nucleus Governs Cellular Form
    arch7 = {
        'data': [
            ("Joachim Hämmerling's experimental organism (1930s-1940s)", "Acetabularia (Mermaid's wineglass)", "A giant single-celled marine alga consisting of three parts: rhizoid (containing single nucleus), stalk, and apical cap", "Amoeba proteus, Onion root tip, Drosophila melanogaster"),
            ("Two distinct species of Acetabularia used by Hämmerling", "Acetabularia mediterranea (smooth umbrella-like cap) and Acetabularia crenulata (branched finger-like cap)", "Easily distinguished by their distinct inherited cap morphologies", "Homo sapiens and Pan troglodytes, Pisum sativum and Zea mays, Escherichia coli and Salmonella"),
            ("Hämmerling's cap amputation experiment", "When the cap of Acetabularia was cut off, the remaining stalk and nucleated rhizoid regenerated a new, perfect cap of the original species", "Demonstrated that the cell possesses regenerative capacity directed by the nucleated base", "The entire cell disintegrated and died within 1 second, The cut stalk grew into a giant fish, The cap regenerated into 10 separate rhizoids"),
            ("Hämmerling's stalk-transplantation (grafting) experiment", "A stalk from A. crenulata was grafted onto an enucleated rhizoid containing the nucleus of A. mediterranea", "The first regenerated intermediate cap was influenced by stored mRNA in the stalk, but when cut again, the second cap was 100% Mediterranean type", "The hybrid cell developed a sunflower, The cell immediately lost all its genetic material, The nucleus turned into a chloroplast"),
            ("Core conclusion established by Hämmerling's Acetabularia experiments", "The nucleus contains and transmits the genetic instructions that determine the morphological structure and phenotypic traits of the cell", "Proved experimentally that genetic information resides in the cell nucleus long before the molecular structure of DNA was resolved", "Proved that the cell wall controls heredity, Concluded that the cytoplasm has no enzymes, Demonstrated that cap shape is determined by ocean salt"),
            ("Why the first regenerated cap in grafted stalks was intermediate or mixed", "Stored morphogenetic substances (messenger RNA / transcripts) from the donor stalk influenced the initial cap formation before decaying", "Once donor transcripts degraded, the host nucleus transcribed its own mRNAs, asserting complete genetic control over subsequent regeneration", "Because the graft mutated into a new species, Because seawater dissolved the nucleus, Because the stalk had an independent brain"),
            ("Reciprocal cross-transplantation of nuclei in Acetabularia", "Transferring an isolated nucleus from A. mediterranea into an enucleated rhizoid of A. crenulata resulted in regeneration of an A. mediterranea cap", "Proved conclusively that the nucleus, and not the rhizoid cytoplasm or cell wall, dictates species-specific morphology", "Produced a completely random non-biological cap, The cell died without dividing, Concluded that the nucleus has no function"),
            ("Cellular structure of Acetabularia making it uniquely suited for nuclear grafting", "It is an immense single cell (up to 5-10 cm tall) with only ONE single nucleus located conveniently in the basal rhizoid", "Allowed microsurgical amputation, stalk grafting, and nuclear transplantation without destroying the cell", "It has no cell membrane, It reproduces by laying hard-shelled eggs, It contains 5000 nuclei scattered throughout the stalk"),
            ("Historical connection between Hämmerling's work and modern genetics", "Provided direct cellular-level proof for Ernst Haeckel's 1866 hypothesis that the nucleus is the physical seat of heredity", "Laid the conceptual experimental foundation for subsequent nuclear transfer and cloning technologies (e.g. Briggs and King, Gurdon, Dolly the sheep)", "Disproved that DNA has any role in heredity, Proved that spontaneous generation creates new caps, Established that proteins are genetic material"),
            ("Cytoplasmic vs Nuclear inheritance in the Acetabularia model", "Cytoplasm can harbor temporary morphogenetic messages (stored mRNAs), but enduring, heritable, long-term cellular architecture is governed exclusively by nuclear genes", "Demonstrates the cooperative functional interplay between nuclear transcription and cytoplasmic translation", "Cytoplasm is the sole master of heredity while nucleus is waste storage, Nuclear genes are destroyed by the cytoplasm, Genetic information flows from cell wall to nucleus")
        ],
        'templates': [
            "In experimental cytology and the genetic control of cell form: '{0}'. Identify the correct scientific fact:",
            "What landmark conclusion was established by: '{0}'?:",
            "Regarding Joachim Hämmerling's classic experiments: '{0}' is characterized as:",
            "A biology student analyzes Hämmerling's Acetabularia study: '{0}'. The accurate fact is:",
            "Which statement correctly explains: '{0}'?:",
            "Analyze the experimental methodology: '{0}' conclusively proved that:",
            "What was the critical significance of: '{0}'?:",
            "In developmental cell biology, '{0}' refers to:",
            "How did '{0}' advance the proof that the nucleus directs cellular morphogenesis?:",
            "A question on nuclear determination asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Hämmerling's Acetabularia experiments (1930s-1940s).**\nUsing the giant single-celled alga *Acetabularia* (*A. mediterranea* vs *A. crenulata*), Hämmerling transplanted stalks and nucleated rhizoids.\n\n**Step 2: Conclusion:**\nThe **nucleus** contains the genetic instructions that dictate cellular morphology and species-specific architecture.\n\n**Step 3: Evaluate '{item[0]}'.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 8: Modern Molecular and Biophysical Insights into the Cell Theory
    arch8 = {
        'data': [
            ("Universal Genetic Code shared by all cellular life", "A sequence of three nucleotide bases (codon) in mRNA specifies the exact same amino acid across bacteria, protists, fungi, plants, and humans", "Proves that all living organisms share a singular evolutionary origin and inherited their genetic machinery from LUCA", "Every species has a completely unique genetic language, Plant codons code for sugars while animal codons code for lipids, Codons are read backwards in bacteria"),
            ("ATP (Adenosine Triphosphate) as universal cellular energy currency", "High-energy phosphoanhydride bonds store and release free energy (\\(\\sim 30.5\\text{ kJ/mol}\\)) to drive cellular mechanical work, active transport, and biosynthesis across all cells", "Universal biochemical energy mediator coupling catabolic exergonic reactions to anabolic endergonic processes", "Cells generate energy using nuclear fusion, Only animal cells use ATP while plant cells use glucose directly, ATP is a non-cellular mineral salt"),
            ("Central Dogma of Molecular Biology (Francis Crick, 1958)", "The directional flow of genetic information: DNA \\(\\xrightarrow{\\text{Transcription}}\\) RNA \\(\\xrightarrow{\\text{Translation}}\\) Protein", "Explains how the static linear code of nuclear DNA is expressed into dynamic functional cellular enzymes and structural proteins", "Protein \\(\\rightarrow\\) RNA \\(\\rightarrow\\) DNA, Lipids \\(\\rightarrow\\) Carbohydrates \\(\\rightarrow\\) Proteins, Genetic information flows backwards from cell wall to nucleus"),
            ("Reverse Transcription (Howard Temin and David Baltimore, 1970)", "Synthesis of DNA from an RNA template catalyzed by reverse transcriptase in retroviruses (e.g. HIV) and retrotransposons", "Represents an exception/extension to the canonical Central Dogma (RNA \\(\\rightarrow\\) DNA)", "DNA is converted directly into lipids, Proteins are converted into amino acid sugars, All viruses lack genetic material"),
            ("Endosymbiotic Theory (Lynn Margulis, 1967)", "Mitochondria and chloroplasts originated as free-living prokaryotes (aerobic proteobacteria and photosynthetic cyanobacteria) engulfed by ancestral host cells", "Supported by evidence: circular 70S ribosomes, circular naked DNA genomes, binary fission-like division, and double membrane architecture", "Mitochondria originated from volcanic ash, Chloroplasts are crystallized sugar grains, Eukaryotes evolved directly from viruses"),
            ("LUCA (Last Universal Common Ancestor)", "The hypothetical ancestral cellular organism from which all current three domains of life (Bacteria, Archaea, Eukarya) descended ~3.8 billion years ago", "Possessed a lipid bilayer, DNA genome, RNA intermediates, 20 amino acid genetic code, ribosome translation, and ATP synthase", "LUCA was a multicellular mammal, LUCA was a silicon-based crystal, LUCA lived in modern household refrigerators"),
            ("Ribosomes as universal ribonucleoprotein translation engines", "Composed of ribosomal RNA (rRNA) and proteins; 70S in prokaryotes, 80S in eukaryotic cytoplasm", "Catalyze peptidyl transferase peptide bond formation during mRNA translation across all living kingdoms", "Ribosomes duplicate the nuclear chromosome, Ribosomes pump water out of the cell, Ribosomes are covered by a thick double lipid membrane"),
            ("Cellular compartmentalization advantage in eukaryotes", "Internal membrane systems (ER, Golgi, lysosomes, peroxisomes) segregate conflicting biochemical reactions into optimized micro-environments", "Increases local enzyme and substrate concentrations, boosting metabolic efficiency and protecting the cell from hydrolytic self-digestion", "Slows down cellular metabolism to zero, Causes cells to burst from internal pressure, Prevents cells from synthesizing proteins"),
            ("Synthetic Biology and minimal synthetic cells (Craig Venter Institute, JCVI-syn3.0)", "Creation of a synthetic viable bacterial cell with a chemically synthesized minimal genome of only 473 essential genes", "Demonstrates that the minimal blueprint of cellular life requires a coherent set of genes for replication, transcription, translation, and membrane synthesis", "Proves that cells do not need DNA to survive, Proved that spontaneous generation creates new species, Synthetic cells are made without any cell membrane"),
            ("Why Cell Theory remains the bedrock of modern biology and biotechnology", "Every advancement in gene editing (CRISPR), stem cell therapeutics, cancer biology, cloning, and tissue engineering relies on the principle that the cell is the living, dividing, functional unit of biology", "Validates Virchow's timeless maxim: all biology and medicine is cellular biology and medicine", "Cell theory has been replaced by astrology, Modern biology ignores cells and studies only macroscopic ghosts, Biotechnology has abandoned cells in favor of non-living plastic")
        ],
        'templates': [
            "In modern molecular cytology and evolutionary biology: '{0}'. Identify the correct scientific fact:",
            "What fundamental biological insight is provided by: '{0}'?:",
            "Regarding the molecular foundations of Cell Theory: '{0}' is characterized as:",
            "A student explores the frontiers of cell biology: '{0}'. The accurate scientific fact is:",
            "Which statement correctly explains: '{0}'?:",
            "Analyze the molecular cytological concept: '{0}'. It demonstrates that:",
            "What is the evolutionary and cellular significance of: '{0}'?:",
            "In modern biochemistry, '{0}' refers to:",
            "How does contemporary biology integrate Cell Theory with: '{0}'?:",
            "A biology question tests modern extensions of Cell Theory: '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand modern molecular extensions of Cell Theory.**\nIntegrates the universal genetic code, ATP energetics, Central Dogma, and Endosymbiosis.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-2-2.1.3", "Cell Theory: Schleiden, Schwann, Virchow (Omnis cellula-e-cellula)", archs)


if __name__ == "__main__":
    q1 = gen_2_1_1()
    q2 = gen_2_1_2()
    q3 = gen_2_1_3()
    print(f"gen_2_1_1: {len(q1)} questions")
    print(f"gen_2_1_2: {len(q2)} questions")
    print(f"gen_2_1_3: {len(q3)} questions")
    print(f"Total Part 1 questions: {len(q1) + len(q2) + len(q3)}")
