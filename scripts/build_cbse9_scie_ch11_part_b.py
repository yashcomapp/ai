import json
import math

def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        "Unbalanced hormonal perturbation",
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
# SUBTOPIC 11.2.2: Pollination (self vs cross) and fertilization process
# ==============================================================================
def gen_11_2_2():
    archs = []

    # Arch 1: Definition of pollination
    archs.append({
        'templates': [
            "What is the biological definition of pollination in flowering plants?",
            "The transfer of pollen grains from the anther to the stigma of a flower is known as:",
            "What is the ultimate purpose of the pollination process in angiosperms?",
            "Which of the following processes must occur BEFORE fertilization can take place in a flower?"
        ],
        'data': [
            ("The transfer of pollen grains from the anther to the receptive stigma of a flower", "The fusion of male and female gametes; The germination of seeds in soil; The ripening of the ovary into a fruit"),
            ("Pollination", "Fertilization; Germination; Transpiration"),
            ("To deliver the male gametes enclosed in pollen grains to the female reproductive organ for fertilization", "To produce nectar for insects; To disperse seeds; To provide color to petals"),
            ("Pollination (transfer of pollen from anther to stigma)", "Seed germination; Fruit ripening; Leaf shedding")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Pollination is defined as the process of transfer of pollen grains from the anther of a stamen to the receptive stigma of a carpel.\\n\\n**Step 2:** Pollen grains enclose the non-motile male gametes.\\n\\n**Step 3:** Pollination brings the male gametes to the female reproductive structure, enabling fertilization to occur. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Self-pollination vs Cross-pollination
    archs.append({
        'templates': [
            "What is self-pollination (autogamy)?",
            "What is cross-pollination (allogamy)?",
            "How does cross-pollination benefit the evolutionary fitness of a plant species compared to self-pollination?",
            "A major disadvantage of continuous self-pollination over multiple generations is:"
        ],
        'data': [
            ("The transfer of pollen grains from the anther to the stigma of the same flower or another flower of the same plant", "The transfer of pollen to a flower of a different species; Pollination by wind only; Fertilization without pollen"),
            ("The transfer of pollen grains from the anther of a flower to the stigma of a flower on a different plant of the same species", "Pollination occurring within a single closed bud; Transfer of ovules by wind; Fusion of two identical cells"),
            ("It introduces genetic variations by combining traits from two distinct parent plants, enhancing vigor and disease resistance", "It requires no external agents; It takes less time; It eliminates the need for petals"),
            ("Inbreeding depression: loss of genetic vigor, accumulation of harmful recessive traits, and reduced adaptability", "Complete loss of flowers; Flowers becoming poisonous; Seeds becoming too heavy to disperse")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Self-pollination occurs when pollen transfer is confined to the same flower or flowers on the same individual plant.\\n\\n**Step 2:** Cross-pollination involves pollen transfer between flowers on genetically distinct plants of the same species, mediated by external agents (wind, water, insects).\\n\\n**Step 3:** Cross-pollination produces new genetic combinations and variations, whereas continuous self-pollination leads to inbreeding depression. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Agents of pollination (Wind, Water, Insects)
    archs.append({
        'templates': [
            "Flowers pollinated by the wind (anemophilous flowers, e.g. corn, wheat, grasses) typically possess which characteristic floral adaptations?",
            "Flowers pollinated by insects (entomophilous flowers, e.g. rose, sunflower, jasmine) exhibit which adaptations?",
            "Water-pollinated flowers (hydrophilous flowers, e.g. Vallisneria, Hydrilla) produce pollen grains that are:",
            "Which of the following plants is adapted for WIND pollination?"
        ],
        'data': [
            ("Lightweight, smooth, non-sticky pollen produced in vast quantities, well-exposed stamens, and large, feathery stigmas", "Bright colorful petals with sweet nectar; Heavy, sticky, scented pollen; Tubular petals hiding stigmas"),
            ("Brightly colored petals, fragrant scent, sweet nectar, and sticky pollen with a rough outer coat", "Feathery stigmas without petals; Colorless, odorless blossoms; Inaudible sound emitters"),
            ("protected by a mucilaginous covering that prevents them from getting wet", "heavier than stones; brightly colored like rainbow; covered in thick wax spines"),
            ("Maize / Corn and Grasses", "Hibiscus; Rose; Orchid")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Wind-pollinated plants produce small, inconspicuous, scentless flowers with enormous quantities of dry, lightweight pollen and feathery protruding stigmas to trap airborne pollen.\\n\\n**Step 2:** Insect-pollinated flowers have large, brightly colored petals, nectar glands, and sticky pollen that adheres to insect bodies.\\n\\n**Step 3:** Water-pollinated plants have mucilage-coated pollen to resist wetting. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 4: Pollen germination and pollen tube formation
    archs.append({
        'templates': [
            "After a compatible pollen grain lands on the sticky surface of the stigma, what happens next?",
            "What stimulates the pollen grain to germinate and produce a pollen tube on the stigma?",
            "Through which part of the carpel does the pollen tube grow down to carry male gametes to the ovary?",
            "The growth of the pollen tube through the style towards the ovary is an example of which plant movement?"
        ],
        'data': [
            ("It absorbs sugary nutrient secretions from the stigma, germinates, and produces a slender pollen tube", "It immediately falls off; It forms a seed on the stigma; It divides into spores"),
            ("Sugary and nutrient-rich secretions produced on the surface of the mature receptive stigma", "Bright sunlight only; Wind pressure; Earth's magnetic field"),
            ("The style", "The anther; The filament; The sepal"),
            ("Chemotropism (directional growth response to chemical attractants released by the ovule)", "Phototropism; Geotropism; Hydrotropism")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** On landing on a compatible stigma, the pollen grain absorbs moisture and sugary nutrients.\\n\\n**Step 2:** The intine emerges through a germ pore to form a pollen tube carrying two male gametes.\\n\\n**Step 3:** The pollen tube grows through the tissues of the style directed by chemical attractants (chemotropism) towards the ovary. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 5: Path of pollen tube into ovule (Micropyle)
    archs.append({
        'templates': [
            "Through which microscopic opening in the integuments of the ovule does the pollen tube normally enter the embryo sac?",
            "What is the micropyle in plant reproductive anatomy?",
            "What does the tip of the pollen tube release upon rupturing inside the embryo sac?",
            "How many male gametes are carried down to the ovule by a single pollen tube?"
        ],
        'data': [
            ("The micropyle", "The hilum; The chalaza; The funicle"),
            ("A tiny pore or aperture in the protective integuments of the ovule through which the pollen tube enters", "The stalk of the seed; The landing platform of the carpel; The wall of the fruit"),
            ("Two male gametes (sperm nuclei)", "Hundreds of spores; One ovum; Female polar nuclei"),
            ("Two male gametes", "One male gamete; Four male gametes; Eight male gametes")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The ovule is surrounded by protective coats (integuments) with a small pore at one end called the micropyle.\\n\\n**Step 2:** The pollen tube enters the ovule through the micropyle into the embryo sac.\\n\\n**Step 3:** The tip of the pollen tube bursts, releasing two male gametes into the embryo sac. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 6: Fertilization and Syngamy in angiosperms
    archs.append({
        'templates': [
            "What is fertilization in flowering plants?",
            "In angiosperms, what is the fusion of one male gamete with the female egg cell (ovum) called?",
            "What cell is formed by the successful fusion of the haploid male gamete with the haploid female egg cell?",
            "The zygote formed after syngamy has what ploidy level?"
        ],
        'data': [
            ("The fusion of the male gamete with the female gamete to form a diploid zygote", "The transfer of pollen from anther to stigma; The ripening of the ovary; The shedding of petals"),
            ("Syngamy (true fertilization)", "Triple fusion; Parthenogenesis; Budding"),
            ("A diploid zygote", "A triploid endosperm; A haploid spore; A seed coat"),
            ("Diploid (2n)", "Haploid (n); Triploid (3n); Tetraploid (4n)")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Fertilization is the fusion of the haploid male gamete (n) with the haploid female gamete / egg cell (n).\\n\\n**Step 2:** This fusion is specifically called syngamy.\\n\\n**Step 3:** Syngamy produces a single-celled diploid zygote (2n), which later develops into the plant embryo. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 7: Triple fusion and Double fertilization concept
    archs.append({
        'templates': [
            "Angiosperms exhibit a unique phenomenon known as 'Double Fertilization'. What two fusion events constitute double fertilization?",
            "What is 'triple fusion' in angiosperm reproduction?",
            "What tissue does the primary endosperm nucleus (PEN) develop into, and what is its biological function?",
            "Why is double fertilization unique to angiosperms (flowering plants)?"
        ],
        'data': [
            ("Syngamy (fusion of 1st male gamete with egg cell) AND Triple Fusion (fusion of 2nd male gamete with 2 polar nuclei)", "Fertilization of two different flowers; Two pollen tubes entering one ovule; Fusion of two egg cells with one sperm"),
            ("The fusion of the second haploid male gamete with two haploid polar nuclei (or diploid secondary nucleus) to form a triploid primary endosperm nucleus (3n)", "The division of the zygote into three cells; The fusion of three pollen grains; The formation of three cotyledons"),
            ("It develops into the triploid endosperm, which stores nutrients to nourish the developing embryo", "It forms the tough seed coat; It ripens into the fruit skin; It forms the taproot"),
            ("Because two separate fertilization events occur simultaneously within the same embryo sac involving two male gametes", "Because angiosperms have two ovaries; Because flowers bloom twice a year; Because seeds have two embryos always")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In angiosperms, one male gamete fuses with the egg cell to form a diploid zygote (syngamy, 2n).\\n\\n**Step 2:** The second male gamete fuses with the two polar nuclei in the central cell to form a triploid primary endosperm nucleus (triple fusion, 3n).\\n\\n**Step 3:** Because two distinct fusions take place in the embryo sac, the phenomenon is called double fertilization. The endosperm provides nourishment to the developing embryo. Correct answer is '{item[0]}'."
        ),
        'diff': 'hard'
    })

    # Arch 8: Adaptations promoting cross-pollination
    archs.append({
        'templates': [
            "Which of the following floral adaptations effectively PREVENTS self-pollination and promotes cross-pollination?",
            "What is dichogamy in plant reproductive biology?",
            "What is self-incompatibility in flowering plants?",
            "Which condition ensures that a plant CANNOT undergo self-pollination under any circumstances?"
        ],
        'data': [
            ("Dichogamy (anthers and stigmas mature at different times) and self-incompatibility", "Bisexuality of flowers; Equal height of anther and stigma; Closing of petals before opening"),
            ("A condition where the male and female organs of a bisexual flower mature at different times (either protandry or protogyny)", "The production of two kinds of seeds; The failure of seeds to germinate; The fusion of petals"),
            ("A genetic mechanism that prevents self-pollen from fertilizing the ovules by inhibiting pollen germination or pollen tube growth on the stigma", "Physical damage to flowers; Lack of water in soil; Absence of bees"),
            ("Dioecious condition (unisexual male and female flowers borne on separate individual plants, e.g. Papaya)", "Bisexual flowers; Hermaphrodite flowers; Flowers with both stamens and carpels")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Flowering plants have evolved mechanisms called outbreeding devices to prevent self-pollination: (1) Unisexuality (dioecy, e.g. papaya), (2) Dichogamy (anther and stigma mature at different times), (3) Self-incompatibility (genetic inhibition of self-pollen).\\n\\n**Step 2:** These ensure genetic outcrossing and hybrid vigor.\\n\\n**Step 3:** Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-11-11.2.2', 'Pollination (self vs cross) and fertilization process', archs)

# ==============================================================================
# SUBTOPIC 11.2.3: Seed and fruit formation
# ==============================================================================
def gen_11_2_3():
    archs = []

    # Arch 1: Post-fertilization floral transformations
    archs.append({
        'templates': [
            "Following successful fertilization in a flower, what happens to the ovule and the ovary respectively?",
            "After fertilization, the petals, sepals, stamens, style, and stigma of the flower typically:",
            "What does the ovary wall (pericarp) transform into after fertilization?",
            "Which floral part ripens to form the SEED?"
        ],
        'data': [
            ("The ovule develops into a SEED, and the ovary ripens into a FRUIT", "The ovule becomes a petal, and ovary becomes root; The ovule forms nectar, and ovary dries into ash; Both become seeds"),
            ("wither, dry up, and fall off (or degenerate)", "turn into leaves; grow into new flowers; form the seed coat"),
            ("The fruit wall (pericarp, which may be fleshy like mango or dry like pea pod)", "The seed coat; The embryo; The cotyledon"),
            ("The fertilized ovule", "The ovary; The thalamus; The style")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** After fertilization, major structural changes take place in the flower.\\n\\n**Step 2:** The zygote divides repeatedly to form an embryo, and the ovule develops a tough protective coat to become a seed.\\n\\n**Step 3:** The ovary grows rapidly and ripens into a fruit. The remaining floral parts (sepals, petals, stamens, style) wither and fall off. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Structure of a typical seed
    archs.append({
        'templates': [
            "What are the three main structural parts of a mature angiosperm seed?",
            "What is the outer protective covering of a seed called, and what are its two layers?",
            "In a seed embryo, which part develops into the future ROOT system of the plant?",
            "In a seed embryo, which part develops into the future SHOOT (stem and leaves) of the plant?"
        ],
        'data': [
            ("Seed coat, cotyledon(s) storing food, and the embryo", "Ovary, style, and stigma; Pollen tube, nectar, and petal; Calyx, corolla, and stamen"),
            ("Seed coat (consisting of the outer tough testa and inner thin tegmen)", "Pericarp; Endocarp; Cuticle"),
            ("The radicle", "The plumule; The cotyledon; The micropyle"),
            ("The plumule", "The radicle; The endosperm; The hilum")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** A seed consists of an outer protective seed coat (testa and tegmen) and an embryo.\\n\\n**Step 2:** The embryo contains an embryonic axis with two distinct growing points: the radicle (which gives rise to the primary root) and the plumule (which gives rise to the shoot).\\n\\n**Step 3:** The cotyledons store reserve nutrients for the germinating embryo. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Monocotyledonous vs Dicotyledonous seeds
    archs.append({
        'templates': [
            "How do monocotyledonous (monocot) seeds differ structurally from dicotyledonous (dicot) seeds?",
            "Which of the following plants produces DICOT seeds with two fleshy cotyledons?",
            "Which of the following plants produces MONOCOT seeds with a single cotyledon (scutellum)?",
            "In cereal grains like maize and wheat, what is the single cotyledon specialized for nutrient absorption called?"
        ],
        'data': [
            ("Monocot seeds possess a single cotyledon, whereas dicot seeds possess two cotyledons", "Monocot seeds have no embryo; Dicot seeds have no seed coat; Monocot seeds never germinate"),
            ("Gram (chana), Pea, and Bean", "Maize; Wheat; Rice"),
            ("Maize, Wheat, Rice, and Grasses", "Gram; Pea; Groundnut"),
            ("Scutellum", "Coleoptile; Coleorhiza; Aleurone")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Angiosperms are classified based on the number of embryonic leaves (cotyledons) in the seed.\\n\\n**Step 2:** Dicots have two cotyledons that store food reserves (e.g. gram, pea, bean, groundnut).\\n\\n**Step 3:** Monocots have a single cotyledon, called the scutellum in grasses and cereals (e.g. maize, wheat, rice). Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 4: Conditions required for seed germination
    archs.append({
        'templates': [
            "What are the three essential environmental conditions required for dormant seeds to successfully germinate?",
            "Why is WATER (moisture) absolutely necessary to initiate seed germination?",
            "Why is OXYGEN (air) indispensable for germinating seeds?",
            "Why do seeds kept in an airtight container or submerged in boiled, cooled water covered with oil fail to germinate?"
        ],
        'data': [
            ("Water (moisture), Oxygen (air), and suitable Temperature (warmth)", "Direct sunlight, fertilizer, and carbon dioxide; Darkness, ice, and nitrogen; Soil, sugar, and vacuum"),
            ("Water softens the tough seed coat, hydrates dormant tissues, and activates hydrolytic enzymes to break down stored food", "Water generates heat by friction; Water acts as a fertilizer; Water provides carbon for photosynthesis"),
            ("Oxygen is required for aerobic cellular respiration to generate ATP energy needed for rapid embryonic cell division and growth", "Oxygen converts starch to cellulose; Oxygen cools down the embryo; Oxygen prevents bacterial decay"),
            ("Because of the complete lack of dissolved oxygen required for cellular respiration", "Because water is too cold; Because oil is acidic; Because seeds need light to germinate")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Seed germination requires three primary external factors: moisture (water), oxygen, and an optimum temperature (25-35 °C).\\n\\n**Step 2:** Water softens the seed coat and activates digestive enzymes to mobilize stored carbohydrates and proteins.\\n\\n**Step 3:** Oxygen is vital for aerobic respiration to supply metabolic energy (ATP) for embryonic cell growth. Light is generally not required for germination of most seeds. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 5: Epigeal vs Hypogeal germination
    archs.append({
        'templates': [
            "In which type of germination do the cotyledons get pushed ABOVE the ground into the air (e.g. in Castor, Bean)?",
            "In which type of germination do the cotyledons remain BELOW the soil surface (e.g. in Gram, Pea, Maize)?",
            "In epigeal germination, what causes the cotyledons to emerge above the soil?",
            "In hypogeal germination, the cotyledons remain underground because of the rapid elongation of which embryonic region?"
        ],
        'data': [
            ("Epigeal germination", "Hypogeal germination; Viviparous germination; Parthenocarpic germination"),
            ("Hypogeal germination", "Epigeal germination; Epiphytic germination; Aerial germination"),
            ("Rapid elongation and arching of the hypocotyl (the region below the cotyledons)", "Rapid elongation of the epicotyl; Deep burrowing of the radicle; Decay of the plumule"),
            ("The epicotyl (the region above the cotyledons elongates, pushing the plumule upward while cotyledons stay buried)", "The hypocotyl; The root cap; The seed coat")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In epigeal germination (castor, bean, tamarind), the hypocotyl elongates rapidly, curving and pulling the cotyledons above the ground, where they turn green and photosynthetic.\\n\\n**Step 2:** In hypogeal germination (gram, pea, maize), the epicotyl elongates rapidly while the hypocotyl remains short, leaving the cotyledons buried underground.\\n\\n**Step 3:** Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 6: True fruits vs False fruits
    archs.append({
        'templates': [
            "What is a TRUE fruit in botany?",
            "Why is an apple or strawberry classified as a FALSE fruit (pseudo-carp)?",
            "In an apple, which part of the flower swells and becomes the edible, juicy flesh?",
            "Which of the following is a TRUE fruit developing strictly from the fertilized ovary?"
        ],
        'data': [
            ("A fruit that develops exclusively from the mature, ripened ovary of a flower without participation of other floral parts", "A fruit produced synthetically in a laboratory; A fruit without seeds; A fruit that never ripens"),
            ("Because other floral parts (specifically the swollen thalamus/receptacle) contribute to the edible fruit flesh along with the ovary", "Because it contains no seeds; Because it grows underground; Because it is produced asexually"),
            ("The thalamus (receptacle)", "The calyx; The style; The pedicel"),
            ("Mango and Tomato (also pea, grape)", "Apple; Pear; Strawberry")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** A true fruit develops exclusively from the ripened ovary of a flower after fertilization (e.g., mango, tomato, pea).\\n\\n**Step 2:** A false fruit (pseudocarp) is one where other floral parts—chiefly the receptacle or thalamus—become enlarged and fleshy alongside the ovary (e.g., apple, pear, strawberry, cashew).\\n\\n**Step 3:** Correct explanation is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 7: Seed dispersal adaptations
    archs.append({
        'templates': [
            "Why is seed dispersal essential for the survival and propagation of plant species?",
            "Dandelion and drumstick seeds possess wings or tufts of fine parachute hairs. What is their mode of dispersal?",
            "Coconut fruits possess a fibrous, buoyant mesocarp. How are they adapted for dispersal?",
            "Seeds of Xanthium (cocklebur) and Urena possess hooks, spines, or sticky barbs. How are they dispersed?"
        ],
        'data': [
            ("It prevents overcrowding and intense competition for sunlight, water, and minerals near the parent plant, facilitating colonization of new habitats", "It ensures all seeds land in the same spot; It converts seeds into spores; It protects plants from herbivores"),
            ("Dispersal by wind (anemochory)", "Dispersal by water; Dispersal by animals; Explosive mechanism"),
            ("Dispersal by water (hydrochory), allowing them to float over ocean currents for thousands of kilometres", "Dispersal by wind; Dispersal by birds; Dispersal by explosive dehiscence"),
            ("Dispersal by animals (epizoochory), by hooking onto the fur of passing animals or clothing of humans", "Dispersal by wind; Dispersal by water; Dispersal by rain")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Seed dispersal prevents localized overcrowding, competition for light and nutrients, and inbreeding depression around the parent plant.\\n\\n**Step 2:** Adaptations: Wind (wings in maple, parachute hairs in dandelion); Water (fibrous fibrous husk in coconut); Animals (spines/hooks in Xanthium, succulent pulp in berries); Explosive burst (balsam, pea).\\n\\n**Step 3:** Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 8: Parthenocarpy (Seedless fruit development)
    archs.append({
        'templates': [
            "What is the development of a fruit without fertilization of the ovules called, resulting in seedless fruits?",
            "Which commercial crop naturally produces seedless fruits via natural parthenocarpy?",
            "How can parthenocarpy be induced artificially in crops like tomatoes, watermelons, and grapes?",
            "Seedless fruits produced by parthenocarpy are advantageous to consumers because they:"
        ],
        'data': [
            ("Parthenocarpy", "Parthenogenesis; Syngamy; Apomixis"),
            ("Banana", "Apple; Mango; Pomegranate"),
            ("By spraying unpollinated flowers with synthetic plant hormones (auxins and gibberellins)", "By boiling flowers; By keeping flowers in the dark; By freezing pollen grains"),
            ("contain high-quality edible flesh without hard, inedible seeds", "grow twice as fast; require no water; can be stored for 100 years")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Parthenocarpy is the formation and development of fruits without prior fertilization of ovules.\\n\\n**Step 2:** Because fertilization does not take place, seeds are not formed, producing seedless fruits (naturally in cultivated bananas and pineapples).\\n\\n**Step 3:** It can be artificially induced by applying auxin and gibberellin hormone sprays on unfertilized ovaries. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-11-11.2.3', 'Seed and fruit formation', archs)

# ==============================================================================
# SUBTOPIC 11.3.1: Male and female reproductive anatomy overview
# ==============================================================================
def gen_11_3_1():
    archs = []

    # Arch 1: Scrotum and temperature regulation of Testes
    archs.append({
        'templates': [
            "Why are the human male testes located outside the abdominal cavity in a pouch-like sac called the scrotum?",
            "What is the temperature maintained inside the scrotal sac compared to normal core body temperature?",
            "What is the primary function of the testes in the human male reproductive system?",
            "Failure of the testes to descend into the scrotum during fetal development (cryptorchidism) results in:"
        ],
        'data': [
            ("Because spermatogenesis (sperm production) requires a temperature 2 to 2.5 °C lower than normal core body temperature", "To prevent physical compression by intestines; To increase blood pressure in kidneys; To keep sperm warm in cold weather"),
            ("2 to 2.5 °C lower than internal core body temperature (approx. 34.5 to 35 °C)", "5 °C higher than body temperature; Identical to body temperature; 10 °C lower than body temperature"),
            ("Production of male gametes (sperms) and secretion of the male sex hormone testosterone", "Filtration of blood; Synthesis of bile; Storage of urine"),
            ("Infertility (sterility) due to failure of spermatogenesis at normal higher body temperature", "Immunity to all infections; Excessive sperm production; Gigantism")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In human males, the primary sex organs are the paired testes situated outside the pelvic abdominal cavity in the scrotum.\\n\\n**Step 2:** The scrotum acts as a thermoregulator, maintaining a scrotal temperature 2-2.5 °C below normal core body temperature (37 °C).\\n\\n**Step 3:** This lower temperature is strictly required for the viable production and maturation of sperms (spermatogenesis). Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Vas deferens and sperm pathway
    archs.append({
        'templates': [
            "What is the muscular duct that carries mature sperm from the testes/epididymis up into the abdominal cavity called?",
            "Which duct in the human male serves as a COMMON passage for both urine from the bladder and semen from reproductive organs?",
            "What is the function of the epididymis located on the posterior surface of each testis?",
            "Trace the correct anatomical pathway of sperm movement from their site of origin to exit:"
        ],
        'data': [
            ("Vas deferens (sperm duct)", "Ureter; Fallopian tube; Urethra"),
            ("The urethra", "The ureter; The vas deferens; The ejaculatory duct"),
            ("Temporary storage, physiological maturation, and motility development of sperms", "Production of testosterone; Filtration of urine; Synthesis of enzymes"),
            ("Testes (seminiferous tubules) → Epididymis → Vas deferens → Ejaculatory duct → Urethra", "Testes → Ureter → Bladder → Urethra; Epididymis → Testes → Ureter → Penis; Urethra → Vas deferens → Testes")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Sperms produced in the testes pass into the coiled epididymis for temporary storage and maturation.\\n\\n**Step 2:** They travel through the muscular vas deferens, which loops over the urinary bladder.\\n\\n**Step 3:** The vas deferens unites with ducts from seminal vesicles to form the ejaculatory duct, joining the urethra. The male urethra serves as a common conduit for urine and semen. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Accessory sex glands (Seminal vesicles and Prostate gland)
    archs.append({
        'templates': [
            "What secretions do the accessory sex glands (seminal vesicles and prostate gland) add to the sperms?",
            "What is semen composed of?",
            "What is the functional advantage of the alkaline seminal fluid added to sperms by accessory glands?",
            "Which single gland surrounds the upper part of the urethra just below the urinary bladder in males?"
        ],
        'data': [
            ("A fluid containing fructose, alkaline buffers, and prostaglandins that nourishes sperms and enhances their motility", "Pure water with mineral salt; Acidic gastric juice; Concentrated urea"),
            ("A mixture of sperms and the collective nutrient-rich, lubricating secretions of seminal vesicles, prostate, and bulbourethral glands", "Pure sperms with no liquid; Blood plasma only; Urine and white blood cells"),
            ("It neutralizes the acidic environment of the male urethra and female vagina, protecting sperms and facilitating motility", "It converts sperms into eggs; It destroys all bacteria; It solidifies semen into bone"),
            ("The prostate gland", "The seminal vesicle; The thyroid gland; The adrenal gland")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The accessory male reproductive glands include paired seminal vesicles, a single prostate gland, and bulbourethral (Cowper's) glands.\\n\\n**Step 2:** They secrete an alkaline seminal fluid containing fructose (energy source), enzymes, and mucus.\\n\\n**Step 3:** This fluid neutralizes urethral and vaginal acidity, activates sperm motility, and provides nutrition. Semen = sperms + seminal plasma. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 4: Female reproductive system: Ovaries
    archs.append({
        'templates': [
            "What are the two primary biological functions of the ovaries in the human female?",
            "Where are the ovaries situated in the human female body?",
            "How often does a mature human female ovary typically release a mature ovum (egg cell)?",
            "Which female sex hormones are synthesized and secreted by the ovaries?"
        ],
        'data': [
            ("1. Production and release of female gametes (ova/eggs), and 2. Secretion of female sex hormones (estrogen and progesterone)", "Filtration of maternal blood and production of bile; Implantation of embryo; Digestion of nutrients"),
            ("In the lower abdominal cavity (pelvic cavity), on either side of the uterus", "Inside the thoracic cavity; Underneath the diaphragm; Within the scrotal sac"),
            ("One mature ovum is released alternately by one of the ovaries approximately every 28 days (ovulation)", "Ten ova are released every week; One ovum every 365 days; Hundreds of ova every hour"),
            ("Estrogen and Progesterone", "Testosterone and Androsterone; Insulin and Glucagon; Thyroxine and Adrenaline")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The primary female sex organs are the paired ovaries located in the lower abdomen on either side of the uterus.\\n\\n**Step 2:** Ovaries produce the female gametes (ova/eggs) and secrete the steroid hormones estrogen (responsible for secondary sexual traits) and progesterone (supports pregnancy).\\n\\n**Step 3:** Typically, one egg is released every ~28 days in a process called ovulation. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 5: Fallopian tubes (Oviducts) and site of fertilization
    archs.append({
        'templates': [
            "In the human female reproductive tract, where does the fertilization of an ovum by a sperm normally take place?",
            "What are the slender tubes that connect each ovary to the uterus called?",
            "What structures at the funnel-shaped ovarian end of the fallopian tube help capture the ovum released during ovulation?",
            "How is the non-motile ovum propelled along the fallopian tube towards the uterus?"
        ],
        'data': [
            ("In the Fallopian tube (Oviduct, specifically the ampullary region)", "Inside the uterus; In the vagina; Inside the ovary"),
            ("Fallopian tubes (or Oviducts)", "Vas deferens; Ureters; Cervical canals"),
            ("Finger-like projections called fimbriae", "Flagella; Cilia only; Muscular sphincters"),
            ("By rhythmic contractions of the muscular wall and coordinated beating of the ciliated epithelial lining of the oviduct", "By gravity alone; By blood circulation; By swimming active tail motion")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The fallopian tubes (oviducts) extend from the vicinity of each ovary to the uterus.\\n\\n**Step 2:** The funnel-shaped opening has finger-like fimbriae that collect the ovum after ovulation.\\n\\n**Step 3:** Fertilization (fusion of sperm and ovum) normally occurs in the fallopian tube (oviduct). Ciliary action and peristalsis move the ovum/zygote towards the uterus. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 6: Uterus (Womb), Cervix, and Vagina
    archs.append({
        'templates': [
            "What is the inverted pear-shaped, highly muscular organ where the fertilized embryo implants and develops called?",
            "What is the lower narrow neck region of the uterus that opens into the vagina called?",
            "What is the canal through which the baby is expelled during childbirth called?",
            "What is the innermost glandular lining of the uterus that thickens monthly to receive an embryo called?"
        ],
        'data': [
            ("The Uterus (Womb)", "The Ovary; The Bladder; The Oviduct"),
            ("The Cervix", "The Vulva; The Clitoris; The Hymen"),
            ("The Vagina (birth canal, together with the cervix)", "The Urethra; The Fallopian tube; The Ureter"),
            ("Endometrium", "Myometrium; Perimetrium; Epimetrium")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The uterus (womb) is a hollow, pear-shaped muscular organ in the female pelvis designed to nourish and shelter the developing fetus.\\n\\n**Step 2:** The inner lining is the vascular endometrium, which prepares monthly for implantation.\\n\\n**Step 3:** The uterus opens via a narrow cervix into the muscular canal called the vagina (birth canal). Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 7: Placenta structure and function
    archs.append({
        'templates': [
            "What is the specialized disc-shaped vascular organ embedded in the uterine wall that connects the developing embryo to the mother?",
            "What is the primary biological function of the placenta during human pregnancy?",
            "How are oxygen and nutrients transferred from the maternal blood to the fetal blood across the placenta?",
            "How are carbon dioxide and metabolic waste products generated by the fetus removed?"
        ],
        'data': [
            ("The Placenta", "The Amnion; The Umbilical cord only; The Corpus luteum"),
            ("It provides a large surface area for diffusion of glucose and oxygen from maternal blood to embryo, and removal of embryo wastes into maternal blood", "It produces red blood cells for the mother; It filters amniotic fluid; It anchors the fetus to maternal intestines"),
            ("By diffusion across the extensive microvilli of the placenta without direct mixing of maternal and fetal blood", "By direct massive blood transfusion; By active pumping through the stomach; By air inhalation"),
            ("They diffuse across the placental barrier into the mother's bloodstream to be excreted by maternal kidneys and lungs", "They are stored permanently in the fetus; They evaporate through fetal skin; They are digested in the placenta")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The placenta is a specialized disc-like organ that develops embedded in the uterine wall during pregnancy.\\n\\n**Step 2:** It has finger-like villi on the embryo side surrounded by maternal blood spaces, providing a huge surface area for exchange.\\n\\n**Step 3:** Nutrients and \\(\\text{{O}}_2\\) diffuse from maternal blood to the fetus via the umbilical cord, while \\(\\text{{CO}}_2\\) and urea diffuse into maternal circulation for excretion. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 8: Gestation period and Parturition
    archs.append({
        'templates': [
            "What is the average gestation period (duration of pregnancy from conception to birth) in humans?",
            "What is the process of giving birth to a baby at the end of pregnancy called?",
            "Strong, rhythmic contractions of which uterine layer induce the birth of the baby during labor?",
            "What is the flexible cord containing blood vessels that connects the fetus's navel to the placenta called?"
        ],
        'data': [
            ("Approximately 9 months (around 280 days or 40 weeks)", "6 months (180 days); 12 months (365 days); 3 months (90 days)"),
            ("Parturition (Childbirth)", "Gestation; Implantation; Ovulation"),
            ("The muscular wall of the uterus (Myometrium)", "The endometrium; The peritoneal membrane; The abdominal skin"),
            ("The Umbilical cord", "The Fallopian tube; The Vas deferens; The Amniotic stalk")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The period of embryonic and fetal development from fertilization to birth is called the gestation period.\\n\\n**Step 2:** In humans, the average gestation period is about 9 months (approximately 280 days from the last menstrual period, or ~38-40 weeks).\\n\\n**Step 3:** The process of delivery of the fully formed fetus is called parturition, driven by forceful contractions of the myometrium. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    return generate_vault_questions('CBSE-9-SCIE-11-11.3.1', 'Male and female reproductive anatomy overview', archs)

# ==============================================================================
# SUBTOPIC 11.3.2: Puberty, hormonal changes, gamete production
# ==============================================================================
def gen_11_3_2():
    archs = []

    # Arch 1: Concept and age of puberty
    archs.append({
        'templates': [
            "What is puberty in human biological development?",
            "Around what age range does puberty typically begin in human girls and boys respectively?",
            "Which endocrine gland located at the base of the brain initiates puberty by releasing gonadotropic hormones (LH and FSH)?",
            "The physical and physiological changes during puberty are primarily driven by:"
        ],
        'data': [
            ("The developmental period during adolescence when reproductive organs become mature and capable of reproduction", "The period of rapid infancy growth; The attainment of maximum height in old age; The onset of menopause"),
            ("Girls: 10 to 12 years; Boys: 12 to 14 years (typically begins 1-2 years earlier in girls)", "Girls: 5 years, Boys: 6 years; Girls: 18 years, Boys: 20 years; Both at exactly 16 years"),
            ("The Pituitary gland (master gland)", "The Thyroid gland; The Pancreas; The Adrenal gland"),
            ("increased secretion of sex hormones stimulated by pituitary gonadotropins", "changes in dietary habits alone; atmospheric humidity; genetic mutations during puberty")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Puberty is the phase of adolescence during which sexual maturity is attained and individuals become biologically capable of sexual reproduction.\\n\\n**Step 2:** In girls, it typically begins between ages 10-12, and in boys between 12-14.\\n\\n**Step 3:** It is triggered when the pituitary gland secretes LH and FSH, which stimulate the testes to produce testosterone and ovaries to produce estrogen. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Male secondary sexual characteristics and testosterone
    archs.append({
        'templates': [
            "Which major male sex hormone is responsible for triggering secondary sexual characteristics in adolescent boys?",
            "Which of the following is a characteristic secondary sexual change observed in boys during puberty?",
            "Why does the voice of adolescent boys often crack and deepen noticeably during puberty?",
            "Where in the testes is the male hormone testosterone synthesized?"
        ],
        'data': [
            ("Testosterone", "Estrogen; Progesterone; Insulin"),
            ("Deepening of voice, enlargement of the larynx (Adam's apple), growth of facial/body hair, and broadening of shoulders", "Broadening of pelvic girdle; Development of mammary glands; High-pitched shrill voice"),
            ("Because the larynx (voice box) grows larger and protrudes visibly as the 'Adam's apple', causing vocal cords to thicken", "Because lungs shrink; Because vocal cords disappear; Because mouth muscles relax"),
            ("By the Leydig cells (interstitial cells) located between seminiferous tubules", "Inside the prostate gland; In the scrotal skin; Inside the urinary bladder")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In males, puberty is regulated by testosterone, produced by the interstitial (Leydig) cells of the testes.\\n\\n**Step 2:** Testosterone stimulates spermatogenesis and induces secondary sexual characters: enlargement of the penis and scrotum, facial/body hair, enlargement of the larynx (Adam's apple), deepening of the voice, and muscular development.\\n\\n**Step 3:** Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Female secondary sexual characteristics and estrogen
    archs.append({
        'templates': [
            "Which female sex hormone is primarily responsible for the development of secondary sexual characteristics in adolescent girls?",
            "Which of the following is a secondary sexual characteristic that develops in girls during puberty?",
            "What physiological event marks the attainment of reproductive capability in adolescent females?",
            "What is the hormone that prepares and maintains the uterine endometrium for pregnancy?"
        ],
        'data': [
            ("Estrogen", "Testosterone; Adrenaline; Glucagon"),
            ("Enlargement of breasts (mammary glands), broadening of hips/pelvis, and initiation of the menstrual cycle", "Deepening of voice with Adam's apple; Growth of heavy facial beard; Narrowing of hips"),
            ("Menarche (the onset of the first menstrual cycle)", "Menopause; Ovulation cessation; Implantation"),
            ("Progesterone (pregnancy hormone)", "Insulin; Melatonin; Thyroxine")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In females, puberty is driven primarily by estrogen produced by maturing ovarian follicles.\\n\\n**Step 2:** Estrogen stimulates breast enlargement, widening of the pelvic girdle, subcutaneous fat deposition, growth of pubic hair, and onset of menstruation.\\n\\n**Step 3:** Progesterone, secreted by the corpus luteum, supports the uterine lining for pregnancy. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 4: Male gamete structure (Sperm)
    archs.append({
        'templates': [
            "What are the three distinct morphological regions of a mature human sperm?",
            "What essential organelle is present in large numbers in the middle piece of a human sperm?",
            "What is the cap-like structure at the anterior tip of the sperm head containing hydrolytic enzymes to penetrate the egg called?",
            "What is the function of the long tail (flagellum) of a sperm?"
        ],
        'data': [
            ("Head, Middle piece, and Tail (flagellum)", "Nucleus, Cytoplasm, and Pseudopodia; Capsule, Cell wall, and Cilia; Stalk, Blade, and Root"),
            ("Mitochondria (arranged in a spiral to provide ATP energy for vigorous motility)", "Ribosomes only; Chloroplasts; Vacuoles"),
            ("Acrosome", "Centrosome; Ribosome; Peroxisome"),
            ("It provides vigorous whiplash motility enabling the sperm to swim through the female reproductive tract towards the ovum", "It absorbs nutrients from air; It anchors the sperm to blood; It stores genetic information")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** A human sperm is a microscopic, motile haploid cell consisting of head, neck, middle piece, and tail.\\n\\n**Step 2:** The head contains an elongated haploid nucleus capped by the acrosome, which carries digestive enzymes to penetrate the ovum membrane.\\n\\n**Step 3:** The middle piece contains spiral mitochondria producing ATP energy to power the flagellar tail for swimming. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 5: Female gamete (Ovum/Egg) and Ovulation
    archs.append({
        'templates': [
            "How does a human ovum (egg cell) compare in size and motility to a human sperm?",
            "What is the release of a mature ovum from an ovarian follicle into the fallopian tube called?",
            "On approximately which day of a typical 28-day human menstrual cycle does ovulation occur?",
            "How long does an unfertilized ovum remain viable for fertilization after ovulation?"
        ],
        'data': [
            ("The ovum is much larger than a sperm, non-motile, and contains nutrient-rich cytoplasm", "The ovum is smaller than a sperm and swims rapidly; Both are identical in size and shape; The ovum has a flagellar tail"),
            ("Ovulation", "Menstruation; Implantation; Fertilization"),
            ("Around Day 14 (mid-cycle)", "Day 1; Day 28; Day 5"),
            ("Approximately 24 hours (1 day)", "10 days; 1 hour; 1 month")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The ovum is a large, non-motile spherical cell containing abundant cytoplasm to nourish early embryonic cell divisions.\\n\\n**Step 2:** The release of the ovum from the mature Graafian follicle is called ovulation, triggered by an LH surge at approximately mid-cycle (around day 14 of a 28-day cycle).\\n\\n**Step 3:** An unfertilized ovum survives for only about 24 hours in the fallopian tube before degenerating. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 6: Menstrual cycle phases
    archs.append({
        'templates': [
            "What is the human menstrual cycle?",
            "What happens to the uterine lining (endometrium) if the released ovum is NOT fertilized by a sperm?",
            "During menstruation (bleeding phase), what is discharged through the vagina?",
            "How long does the menstrual flow (bleeding) typically last in a healthy adolescent female?"
        ],
        'data': [
            ("A periodic rhythmic cycle of physiological changes (~28 days) in the ovaries and uterine lining preparing the body for pregnancy", "A disease of the digestive system; A daily hormonal surge; An infection of the urinary tract"),
            ("The thickened endometrium along with its blood vessels breaks down and sloughs off as menstrual bleeding", "The endometrium turns into bone; The endometrium remains permanent; The uterus shrinks to half size"),
            ("The disintegrated uterine endometrial tissue, mucus, and blood, along with the degenerated unfertilized egg", "Pure clear water; Solid bone fragments; White blood cells only"),
            ("Approximately 3 to 5 days (up to 7 days)", "15 to 20 days; Exactly 1 hour; 28 days continuously")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The menstrual cycle is a repeating ~28-day cycle that prepares the female reproductive tract for potential pregnancy.\\n\\n**Step 2:** Each month, the endometrium thickens and becomes richly vascularized.\\n\\n**Step 3:** If fertilization does not occur, progesterone levels plummet, causing the endometrium to break down and shed through the vagina as menstrual flow lasting 3-5 days. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 7: Menarche and Menopause
    archs.append({
        'templates': [
            "What is the onset of the first menstrual period in an adolescent female at puberty termed?",
            "What is the permanent cessation of menstrual cycles and reproductive capability in women called?",
            "Around what age does menopause naturally occur in human females?",
            "Why does menopause occur in women, whereas men continue producing sperm into old age?"
        ],
        'data': [
            ("Menarche", "Menopause; Gestation; Ovulation"),
            ("Menopause", "Menarche; Puberty; Parturition"),
            ("Between 45 and 50 years of age", "Between 20 and 25 years; At 12 years; At 80 years"),
            ("Because females are born with a finite pool of primary follicles in the ovaries which become depleted, causing estrogen levels to drop", "Because the uterus disappears; Because blood production stops; Because women run out of hormones completely")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Menarche is the first occurrence of menstruation, marking the onset of puberty in females (around 10-12 years).\\n\\n**Step 2:** Menopause is the permanent cessation of menstruation and ovulation, typically occurring between 45 and 50 years of age.\\n\\n**Step 3:** While spermatogenesis continues throughout male adulthood, female ovarian follicles become depleted around mid-life. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 8: Pituitary and gonadal hormonal feedback
    archs.append({
        'templates': [
            "Which two pituitary hormones stimulate the development of gametes and secretion of sex steroids in both males and females?",
            "In males, what does Luteinizing Hormone (LH) specifically stimulate?",
            "In females, what does Follicle Stimulating Hormone (FSH) stimulate in the ovaries?",
            "What event triggers ovulation (release of ovum) around day 14 of the menstrual cycle?"
        ],
        'data': [
            ("LH (Luteinizing Hormone) and FSH (Follicle Stimulating Hormone)", "Insulin and Glucagon; Thyroxine and Calcitonin; Growth Hormone and Oxytocin"),
            ("Leydig cells in the testes to synthesize and secrete testosterone", "The prostate gland to produce mucus; The penis to grow; The kidneys to filter urine"),
            ("Growth and maturation of ovarian follicles enclosing the developing ovum", "Shedding of the uterine lining; Contraction of the cervix; Production of milk"),
            ("A sharp mid-cycle surge in Luteinizing Hormone (LH surge)", "A sudden drop in body temperature; A spike in adrenaline; The onset of menstruation")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Puberty and gametogenesis are orchestrated by the hypothalamic-pituitary-gonadal axis.\\n\\n**Step 2:** The anterior pituitary secretes FSH (stimulates follicle growth in females and spermatogenesis in males) and LH (stimulates testosterone in males and triggers ovulation in females).\\n\\n**Step 3:** The mid-cycle LH surge ruptures the mature follicle, causing ovulation on day 14. Correct answer is '{item[0]}'."
        ),
        'diff': 'hard'
    })

    return generate_vault_questions('CBSE-9-SCIE-11-11.3.2', 'Puberty, hormonal changes, gamete production', archs)

# ==============================================================================
# SUBTOPIC 11.3.3: Reproductive hygiene and health awareness
# ==============================================================================
def gen_11_3_3():
    archs = []

    # Arch 1: Definition of Reproductive Health (WHO)
    archs.append({
        'templates': [
            "According to the World Health Organization (WHO), what is the comprehensive definition of reproductive health?",
            "A society in which people have physically and functionally normal reproductive organs and normal emotional and behavioral interactions in sex-related matters is termed:",
            "Which of the following is a key objective of reproductive health education programs in schools?",
            "Why is awareness about reproductive health and bodily changes crucial for adolescents?"
        ],
        'data': [
            ("A state of complete physical, mental, emotional, and social well-being in all matters relating to the reproductive system and its functions", "Merely the absence of reproductive disease or infirmity; The ability to produce maximum children; Having large families"),
            ("Reproductively healthy society", "Technologically advanced society; Industrially developed society; Conservative society"),
            ("To provide scientifically accurate information about puberty, safe sex, contraception, and prevention of STIs to prevent myths and misconceptions", "To encourage child marriage; To eliminate sports from school; To promote unverified traditional remedies"),
            ("To help adolescents navigate emotional, hormonal, and physical changes safely without falling prey to peer pressure or risky behaviors", "To stop physical growth; To decrease life expectancy; To avoid doctor visits")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The WHO defines reproductive health as total well-being in all aspects of reproduction: physical, emotional, behavioral, and social.\\n\\n**Step 2:** It encompasses not merely the absence of disease, but responsible, safe, and fulfilling reproductive capability.\\n\\n**Step 3:** Correct definition is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Sexually Transmitted Infections (STIs / STDs)
    archs.append({
        'templates': [
            "What are Sexually Transmitted Infections (STIs, also known as STDs)?",
            "Which of the following STIs is caused by a BACTERIAL infection?",
            "Which of the following STIs is caused by a VIRAL infection?",
            "Which fatal viral STI attacks the human immune system (specifically CD4+ T helper cells) leading to immune deficiency?"
        ],
        'data': [
            ("Infections that are transmitted from an infected person to an uninfected person through sexual contact", "Diseases transmitted by airborne droplets; Nutritional deficiency disorders; Genetic chromosomal mutations"),
            ("Gonorrhea and Syphilis", "HIV-AIDS; Genital Warts; Genital Herpes"),
            ("HIV-AIDS, Genital Warts, and Genital Herpes", "Gonorrhea; Syphilis; Cholera"),
            ("HIV-AIDS (Human Immunodeficiency Virus / Acquired Immunodeficiency Syndrome)", "Gonorrhea; Syphilis; Tuberculosis")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** STIs are infectious diseases spread primarily through sexual contact.\\n\\n**Step 2:** Bacterial STIs include Gonorrhea (Neisseria gonorrhoeae) and Syphilis (Treponema pallidum), which can be cured with antibiotics if treated early.\\n\\n**Step 3:** Viral STIs include Genital Warts, Genital Herpes, and HIV-AIDS. HIV specifically attacks helper T-lymphocytes, destroying immune defense. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Prevention of STIs (Barrier methods)
    archs.append({
        'templates': [
            "Which contraceptive method is unique in providing DUAL protection: preventing unwanted pregnancy AND protecting against sexually transmitted infections (STIs/HIV)?",
            "How does the use of condoms prevent the transmission of sexually transmitted pathogens?",
            "Which of the following contraceptive methods does NOT provide any protection against STIs?",
            "The most effective practice for preventing the transmission of STIs is:"
        ],
        'data': [
            ("Barrier methods like condoms (male or female condoms)", "Oral contraceptive pills; Copper-T (IUD); Surgical vasectomy"),
            ("By creating a physical mechanical barrier that prevents direct skin-to-skin contact and exchange of body fluids (semen and vaginal secretions)", "By killing viruses with antibiotics; By changing body hormones; By altering blood groups"),
            ("Oral hormonal pills, Copper-T (IUD), and surgical sterilization", "Male condoms; Female condoms; Latex barriers"),
            ("using barrier methods (condoms) consistently and avoiding unprotected sexual contact with multiple partners", "taking vitamin C; taking painkillers; washing with hot water after intercourse")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Condoms are barrier contraceptives made of thin latex sheath.\\n\\n**Step 2:** They cover the penis in males or line the vagina in females, physically blocking the exchange of seminal and vaginal fluids during intercourse.\\n\\n**Step 3:** Condoms are the only contraceptive method that provides dual protection against both pregnancy and STIs (including HIV and Syphilis). Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 4: Contraceptive methods classification: Barrier, Chemical, IUD, Surgical
    archs.append({
        'templates': [
            "Contraceptive methods are divided into categories. Which of the following is a BARRIER method of contraception?",
            "Which of the following is an INTRAUTERINE DEVICE (IUD) used for contraception?",
            "How do oral contraceptive pills (chemical hormonal methods) prevent pregnancy?",
            "What is a potential disadvantage or side effect of oral hormonal contraceptive pills?"
        ],
        'data': [
            ("Condoms, Diaphragms, and Cervical Caps", "Oral pills; Copper-T; Vasectomy"),
            ("Copper-T (or Loop)", "Diaphragm; Condom; Birth control patch"),
            ("They alter the hormonal balance of the body to prevent ovulation and thicken cervical mucus to block sperm entry", "They destroy all eggs permanently; They surgically block fallopian tubes; They kill sperms by freezing"),
            ("Because they alter delicate hormonal balances, they can cause side effects like nausea, irregular bleeding, weight gain, and headaches", "They cause immediate tooth decay; They eliminate hearing; They cause paralysis")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Contraceptive methods are grouped as: (1) Barrier (condoms, diaphragms), (2) Chemical/Hormonal (oral pills like 'Saheli', injections), (3) IUDs (Copper-T, LNG-20), (4) Surgical (vasectomy, tubectomy).\\n\\n**Step 2:** Oral pills contain synthetic estrogen/progesterone combinations that suppress ovulation.\\n\\n**Step 3:** Correct classification is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 5: Intrauterine Device (Copper-T) mechanism
    archs.append({
        'templates': [
            "Where is a Copper-T contraceptive device placed in the female body by a trained healthcare professional?",
            "How does a Copper-T (IUD) prevent pregnancy?",
            "What is a major advantage of Intrauterine Devices (IUDs) like Copper-T for family planning?",
            "Can a Copper-T prevent the transmission of sexually transmitted infections like HIV?"
        ],
        'data': [
            ("Inside the cavity of the Uterus", "Inside the Fallopian tube; Inside the ovary; Inside the urinary bladder"),
            ("It releases copper ions that suppress sperm motility and fertilizing capacity, and induces an inflammatory response preventing implantation", "It permanently removes the ovaries; It destroys the vagina; It stops menstruation permanently"),
            ("It is a long-term, highly effective, reversible contraceptive that requires no daily pill intake", "It increases body height; It cures diabetes; It provides immunity against flu"),
            ("No, Copper-T provides zero protection against STIs; it only prevents pregnancy", "Yes, it destroys all viruses; Yes, copper sterilizes the bloodstream; Yes, completely")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Copper-T is an intrauterine device inserted into the uterine cavity by a doctor.\\n\\n**Step 2:** The copper ions released reduce sperm motility and survival, while the device alters the endometrial lining to prevent implantation of the blastocyst.\\n\\n**Step 3:** However, IUDs do not prevent STIs. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 6: Surgical methods (Vasectomy and Tubectomy)
    archs.append({
        'templates': [
            "What is the permanent surgical contraceptive procedure performed in males called, where the vas deferens is cut and tied?",
            "What is the surgical sterilization procedure in females called, where a small portion of the fallopian tubes is cut and tied?",
            "After a successful vasectomy in a man, how is the ejaculate affected?",
            "Why are surgical methods (vasectomy and tubectomy) termed 'terminal' or 'sterilization' methods?"
        ],
        'data': [
            ("Vasectomy", "Tubectomy; Appendectomy; Mastectomy"),
            ("Tubectomy", "Vasectomy; Hysterectomy; Episiotomy"),
            ("Semen is still ejaculated normally with secretions from seminal vesicles and prostate, but it contains NO sperms", "No fluid is ejaculated; Semen turns yellow; Testosterone drops to zero"),
            ("Because they provide permanent contraception with extremely poor and difficult reversibility", "Because they are performed at birth; Because they kill the patient; Because they take 20 years to work")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Surgical methods are permanent sterilization techniques.\\n\\n**Step 2:** In males, vasectomy involves cutting and ligating the vas deferens, preventing sperms from reaching the urethra. In females, tubectomy involves cutting and tying the fallopian tubes, preventing the ovum from meeting sperm.\\n\\n**Step 3:** In vasectomy, ejaculation occurs normally (seminal plasma is produced) but without sperms. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 7: Menstrual hygiene management
    archs.append({
        'templates': [
            "Why is maintaining strict menstrual hygiene essential for adolescent girls and women during menstruation?",
            "How often should a sanitary napkin or absorbent pad be changed during menstruation for optimal hygiene?",
            "Why should old unwashed or damp cloth NEVER be reused as menstrual absorbents?",
            "What is the hygienic method for disposing of used sanitary napkins?"
        ],
        'data': [
            ("To prevent bacterial and fungal infections of the reproductive and urinary tracts (RTI / UTI) and long-term pelvic inflammatory diseases", "To stop bleeding faster; To reduce body temperature; To prevent hair loss"),
            ("Every 4 to 6 hours (or more frequently on heavy flow days)", "Once every 24 hours; Once every 48 hours; Once a week"),
            ("Because unhygienic, damp cloth harbors pathogenic bacteria and fungi that cause severe vaginal and pelvic infections", "Because cloth absorbs too much blood; Because cloth changes blood color; Because cloth is heavier than cotton"),
            ("Wrapping it securely in waste paper and disposing of it in a designated sanitary waste bin or incinerator", "Flushing it down the toilet; Throwing it into open drains; Burying it in gardens")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Menstrual hygiene is vital to prevent reproductive tract infections (RTIs) and pelvic inflammatory diseases.\\n\\n**Step 2:** Sanitary pads should be changed every 4-6 hours to prevent bacterial proliferation.\\n\\n**Step 3:** Reusing unsterilized damp cloth causes serious fungal and bacterial infections. Used pads should be wrapped and disposed of in sanitary bins, never flushed down toilets (which causes severe clogs). Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 8: Adolescent health and gender equity
    archs.append({
        'templates': [
            "Why is female foeticide (prenatal sex determination and aborting female fetuses) illegal and severely punishable under Indian law (PCPNDT Act)?",
            "What is a critical social consequence of widespread female foeticide and declining child sex ratio?",
            "What is the legal minimum age for marriage in India designed to ensure physical and mental reproductive maturity?",
            "Why is adolescent pregnancy (teenage pregnancy) medically hazardous for the young mother and child?"
        ],
        'data': [
            ("Because it causes severe demographic distortion, violates human rights, and skews the child sex ratio dangerously", "Because ultrasound machines are expensive; Because female fetuses have higher body mass; Because hospitals have no space"),
            ("A severe imbalance in the sex ratio leading to social instability, violence against women, and demographic crisis", "Overpopulation of girls; Shortage of food; Collapse of schools"),
            ("18 years for females and 21 years for males", "14 years for both; 10 years for females, 12 for males; 25 years for both"),
            ("Because an adolescent girl's body and pelvis are not fully developed, leading to high maternal mortality, severe anemia, and low-birth-weight babies", "Because teenage mothers produce twins always; Because infants born to teens have no bones; Because teens cannot feed babies")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The Pre-Conception and Pre-Natal Diagnostic Techniques (PCPNDT) Act strictly bans sex selection and prenatal gender determination to curb female foeticide.\\n\\n**Step 2:** Skewed child sex ratios cause severe demographic and social problems.\\n\\n**Step 3:** The legal marriage age (18 for women, 21 for men) ensures physiological and emotional maturity, protecting young women from the severe health hazards of early teenage pregnancy. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-11-11.3.3', 'Reproductive hygiene and health awareness', archs)

def main():
    all_questions = []

    print("Generating 11.2.2...")
    q1 = gen_11_2_2()
    print(f"11.2.2 generated {len(q1)} questions")
    all_questions.extend(q1)

    print("Generating 11.2.3...")
    q2 = gen_11_2_3()
    print(f"11.2.3 generated {len(q2)} questions")
    all_questions.extend(q2)

    print("Generating 11.3.1...")
    q3 = gen_11_3_1()
    print(f"11.3.1 generated {len(q3)} questions")
    all_questions.extend(q3)

    print("Generating 11.3.2...")
    q4 = gen_11_3_2()
    print(f"11.3.2 generated {len(q4)} questions")
    all_questions.extend(q4)

    print("Generating 11.3.3...")
    q5 = gen_11_3_3()
    print(f"11.3.3 generated {len(q5)} questions")
    all_questions.extend(q5)

    out_file = 'scripts/cbse9_scie_ch11_part_b.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved {len(all_questions)} questions to {out_file}")

if __name__ == '__main__':
    main()
