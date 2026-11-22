import json
import math

def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        "Unbalanced phylogenetic divergence",
        "Passive taxonomic stagnation",
        "Spontaneous non-cladistic dissociation"
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
                "chapterNumber": 12,
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
# SUBTOPIC 12.1.1: Need for classification & hierarchy of taxonomic categories
# ==============================================================================
def gen_12_1_1():
    archs = []

    # Arch 1: Need for classification and systematic study
    archs.append({
        'templates': [
            "Why is the biological classification of living organisms essential in science?",
            "What is the primary scientific purpose of classifying the millions of diverse organisms on Earth?",
            "How does biological classification aid our understanding of the living world?",
            "Taxonomy is defined as the scientific discipline that deals with:"
        ],
        'data': [
            ("Because millions of diverse species exist on Earth, and classification groups them systematically based on similarities, making their study feasible and tracing evolutionary lineages", "To create unique commercial trade names; To count the total number of trees; To synthesize new animals in laboratories"),
            ("To organize diverse life forms into hierarchical groups based on shared characteristics, revealing evolutionary relationships", "To prove that all organisms have identical DNA; To separate edible and non-edible species only; To eliminate non-useful species"),
            ("It enables systematic study of a vast array of organisms by studying representative types of each group and establishes phylogenetic relationships", "It changes organisms into new forms; It replaces the need for ecology; It predicts weather patterns"),
            ("the identification, nomenclature, and systematic classification of organisms based on shared characteristics and evolutionary relationships", "the study of mineral rocks; the breeding of racehorses; the chemical synthesis of drugs")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Millions of diverse organisms inhabit the Earth. It is impossible to study every single species individually.\\n\\n**Step 2:** Biological classification groups organisms based on fundamental similarities and differences in cellular structure, body design, and evolutionary history.\\n\\n**Step 3:** By studying a few representative types from each group, we can understand the key features of the entire group and trace evolutionary lineages (phylogeny). Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Fundamental criteria for biological classification
    archs.append({
        'templates': [
            "Which of the following represents the most fundamental primary criterion used in classifying living organisms into major kingdoms?",
            "In modern biological taxonomy, what are the primary criteria used by Robert Whittaker for classifying organisms into five kingdoms?",
            "Why is the presence of a well-defined nucleus (Eukaryotic vs Prokaryotic) the most fundamental distinction in classification?",
            "What is the distinction between unicellular and multicellular body organization in classification?"
        ],
        'data': [
            ("Cellular complexity: whether cells are Prokaryotic (lacking membrane-bound nucleus) or Eukaryotic (having membrane-bound nucleus and organelles)", "Habitat: whether organisms live on land or water; Color of the organism; Size of the organism"),
            ("1. Cell structure (prokaryotic/eukaryotic), 2. Body organization (unicellular/multicellular), 3. Mode of nutrition (autotrophic/heterotrophic), and 4. Cell wall presence", "1. Number of legs, 2. Swimming ability, 3. Blood color; 1. Body weight, 2. Lifespan, 3. Skin color; 1. Geographical location alone"),
            ("Because eukaryotic cellular compartmentalization allows diverse specialized biochemical processes to occur simultaneously and independently", "Because prokaryotes have no DNA; Because eukaryotes have no cell walls; Because prokaryotes live only in fire"),
            ("Unicellular organisms perform all life functions within a single independent cell, while multicellular organisms show cellular division of labor with specialized tissues", "Multicellular organisms have no cell membranes; Unicellular organisms cannot divide; Both have identical tissue systems")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The primary division in life forms is based on cellular complexity: Prokaryotic cells (lacking a membrane-enclosed nucleus and organelles, e.g. Monera) versus Eukaryotic cells.\\n\\n**Step 2:** Further subdivisions depend on whether the organism is unicellular or multicellular, whether cells have a cell wall, and the mode of nutrition (photosynthetic autotroph vs absorptive or ingestive heterotroph).\\n\\n**Step 3:** Correct criterion is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 3: Five Kingdom classification (Whittaker, 1969) and Woese modification
    archs.append({
        'templates': [
            "Who proposed the widely accepted Five-Kingdom classification system in 1969?",
            "What are the five kingdoms proposed by Robert H. Whittaker in 1969?",
            "How did Carl Woese (1977) further modify the Five-Kingdom classification system?",
            "In which kingdom did Whittaker place unicellular eukaryotic organisms like Amoeba and Paramecium?"
        ],
        'data': [
            ("Robert H. Whittaker", "Carolus Linnaeus; Charles Darwin; Ernst Haeckel"),
            ("Monera, Protista, Fungi, Plantae, and Animalia", "Algae, Fungi, Bryophytes, Pteridophytes, and Angiosperms; Invertebrates, Vertebrates, Plants, Bacteria, and Viruses; Mammals, Birds, Reptiles, Amphibians, and Fishes"),
            ("By dividing Kingdom Monera into two distinct domains: Archaebacteria (ancient bacteria) and Eubacteria (true bacteria)", "By merging Fungi and Plants; By creating a kingdom for viruses; By eliminating Kingdom Protista"),
            ("Kingdom Protista", "Kingdom Monera; Kingdom Fungi; Kingdom Animalia")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In 1969, American ecologist Robert H. Whittaker proposed the Five-Kingdom classification: Monera, Protista, Fungi, Plantae, and Animalia.\\n\\n**Step 2:** Unicellular prokaryotes belong to Monera; unicellular eukaryotes belong to Protista.\\n\\n**Step 3:** In 1977, Carl Woese subdivided Monera into Archaebacteria and Eubacteria based on 16S ribosomal RNA differences. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 4: Taxonomic hierarchy order (Kingdom to Species)
    archs.append({
        'templates': [
            "What is the correct descending order of the taxonomic categories in the biological hierarchy of classification?",
            "Which of the following sequences represents the correct ascending order of taxonomic categories (from lowest to highest)?",
            "In plant taxonomy, the category equivalent to 'Phylum' in animal taxonomy is:",
            "Which category in the taxonomic hierarchy lies between Class and Family?"
        ],
        'data': [
            ("Kingdom → Phylum (or Division) → Class → Order → Family → Genus → Species", "Kingdom → Class → Order → Phylum → Family → Genus → Species; Species → Genus → Family → Order → Class → Phylum → Kingdom; Kingdom → Order → Class → Family → Genus → Species"),
            ("Species → Genus → Family → Order → Class → Phylum (or Division) → Kingdom", "Kingdom → Phylum → Class → Order → Family → Genus → Species; Species → Order → Family → Class → Kingdom; Genus → Species → Family → Order → Kingdom"),
            ("Division", "Cohort; Tribe; Section"),
            ("Order", "Phylum; Genus; Species")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The biological hierarchy of taxonomic ranks from highest to lowest is: Kingdom, Phylum (in animals) or Division (in plants), Class, Order, Family, Genus, and Species.\\n\\n**Step 2:** A helpful mnemonic is: 'King Philip Came Over For Good Soup'.\\n\\n**Step 3:** Correct order is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 5: Basic fundamental unit of classification (Species)
    archs.append({
        'templates': [
            "What is the basic, fundamental, and lowest unit of biological classification?",
            "How is a biological 'species' defined in modern biology?",
            "As we proceed from Species to Kingdom in the taxonomic hierarchy, how does the number of common characteristics shared by organisms change?",
            "Which taxonomic rank contains organisms sharing the HIGHEST degree of common anatomical and physiological characteristics?"
        ],
        'data': [
            ("Species", "Genus; Family; Kingdom"),
            ("A group of closely related individuals that are morphologically similar and capable of interbreeding freely in nature to produce fertile offspring", "A group of animals living in the same forest; A population of plants with same flower color; Organisms that eat the same diet"),
            ("The number of common characteristics decreases progressively, while general dissimilarities increase", "The number of common characteristics increases; Common characteristics remain identical; All differences disappear"),
            ("Species", "Family; Order; Kingdom")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Species is the lowest, most specific and fundamental unit of classification.\\n\\n**Step 2:** A species comprises a group of individuals sharing maximum morphological, physiological, and genetic similarities and capable of interbreeding in nature to yield fertile offspring.\\n\\n**Step 3:** As we move upward from species to kingdom, the degree of shared characteristics decreases. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 6: Taxonomic classification of Humans (Homo sapiens)
    archs.append({
        'templates': [
            "What is the complete taxonomic hierarchy for modern humans (Homo sapiens)?",
            "To which biological Class do human beings belong in the animal kingdom?",
            "What is the Order to which humans, monkeys, and apes belong?",
            "What is the Family to which human beings belong?"
        ],
        'data': [
            ("Kingdom: Animalia, Phylum: Chordata, Class: Mammalia, Order: Primates, Family: Hominidae, Genus: Homo, Species: sapiens", "Kingdom: Plantae, Phylum: Arthropoda, Class: Aves; Kingdom: Animalia, Phylum: Annelida, Class: Insecta; Kingdom: Animalia, Phylum: Mollusca, Class: Reptilia"),
            ("Class Mammalia (mammals, possessing mammary glands, body hair, and three ear ossicles)", "Class Aves; Class Reptilia; Class Amphibia"),
            ("Order Primates", "Order Carnivora; Order Rodentia; Order Cetacea"),
            ("Family Hominidae", "Family Felidae; Family Canidae; Family Bovidae")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Complete taxonomy of humans:\\n- Kingdom: Animalia\\n- Phylum: Chordata (presence of notochord/backbone)\\n- Class: Mammalia (mammary glands, hair)\\n- Order: Primates (stereoscopic vision, grasping hands)\\n- Family: Hominidae\\n- Genus: Homo\\n- Species: sapiens.\\n\\n**Step 2:** Examine the relevant taxonomic and evolutionary criteria.\\n\\n**Step 3:** Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 7: Evolution and Classification (Charles Darwin)
    archs.append({
        'templates': [
            "In which landmark book published in 1859 did Charles Darwin introduce the idea of biological evolution by natural selection?",
            "How are biological classification and organic evolution interconnected?",
            "What is meant by 'primitive' (lower) and 'advanced' (higher) organisms in evolutionary classification?",
            "Classification of organisms based on their shared evolutionary ancestry and genealogical descent is called:"
        ],
        'data': [
            ("The Origin of Species (On the Origin of Species by Means of Natural Selection)", "Systema Naturae; Philosophia Botanica; Micrographia"),
            ("Classification of organisms is a reflection of their evolutionary relationships (phylogeny); more closely related organisms share more recent common ancestors", "Classification disproves evolution; Evolution occurs without classification; Classification is independent of genetics"),
            ("Primitive organisms have ancient, simpler body designs that have changed little, while advanced organisms have acquired more complex, specialized body structures more recently", "Primitive organisms are extinct; Advanced organisms have no cells; Primitive organisms live in space"),
            ("Phylogenetic classification (or Cladistics)", "Artificial classification; Empirical taxonomy; Numerical taxonomy")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In 1859, Charles Darwin published 'The Origin of Species', establishing that all living species evolved from ancestral forms through natural selection.\\n\\n**Step 2:** Classification is directly linked to evolution: organisms with similar body designs share a more recent common ancestor.\\n\\n**Step 3:** Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 8: Genus concept and comparison of related species
    archs.append({
        'templates': [
            "What is a 'Genus' in the taxonomic hierarchy of classification?",
            "Consider the lion (Panthera leo), tiger (Panthera tigris), and leopard (Panthera pardus). Why are they grouped into the same genus Panthera?",
            "Potato (Solanum tuberosum) and Brinjal/Eggplant (Solanum melongena) belong to the same:",
            "Two organisms belong to the same Class. Must they also belong to the same Phylum and Kingdom?"
        ],
        'data': [
            ("A taxonomic category comprising a group of closely related species that share several common structural features", "A single isolated organism; A group of unrelated families; The highest taxonomic rank"),
            ("Because they share many common anatomical and predatory characteristics, though they are distinct inter-sterile species", "Because they can mate and produce fertile cubs; Because they have identical coat colors; Because they live in the same forest"),
            ("Genus (Solanum)", "Species; Variety; Subspecies"),
            ("YES, because organisms sharing a lower taxonomic rank (Class) must automatically share all higher ranks (Phylum and Kingdom)", "NO, they can belong to different Kingdoms; NO, they can belong to different Phyla; Only if they live in water")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** A Genus is an assemblage of related species having more characters in common with one another than with species of other genera.\\n\\n**Step 2:** For example, lion (*Panthera leo*), tiger (*Panthera tigris*), and leopard (*Panthera pardus*) share key anatomical features and are placed in the genus *Panthera*.\\n\\n**Step 3:** Any two organisms sharing a Class necessarily share the same Phylum and Kingdom. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-12-12.1.1', 'Need for classification and hierarchy of taxonomic categories', archs)

# ==============================================================================
# SUBTOPIC 12.1.2: Binomial nomenclature system (Linnaeus)
# ==============================================================================
def gen_12_1_2():
    archs = []

    # Arch 1: Carolus Linnaeus and binomial nomenclature
    archs.append({
        'templates': [
            "Which 18th-century Swedish naturalist introduced the system of Binomial Nomenclature and is revered as the 'Father of Taxonomy'?",
            "What does the term 'Binomial Nomenclature' literally mean?",
            "In which landmark botanical work published in 1753 did Carolus Linnaeus first establish binomial nomenclature for plants?",
            "Why was the binomial nomenclature system universally adopted by scientists worldwide?"
        ],
        'data': [
            ("Carolus Linnaeus (Carl von Linné)", "Charles Darwin; Robert Hooke; Gregor Mendel"),
            ("A scientific naming system in which every organism is given a two-word Latin name consisting of Genus and Species", "A system using three numbers; A naming system based on country of origin; Naming animals after scientists only"),
            ("Species Plantarum (1753)", "Philosophie Zoologique; Systema Naturae (10th edition for animals, 1758); The Origin of Species"),
            ("It provides a single, universally accepted, standardized scientific name for each organism, eliminating the confusion caused by local vernacular names", "It makes names easier to pronounce in English; It allows anyone to change animal names; It translates names into all languages")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Carolus Linnaeus (1707–1778), the Father of Taxonomy, introduced the Binomial Nomenclature system in 'Species Plantarum' (1753).\\n\\n**Step 2:** Under this system, each species has a unique, universally accepted two-word Latin name.\\n\\n**Step 3:** This eliminates the confusion caused by numerous regional and vernacular names across different languages. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Four international rules of writing scientific names
    archs.append({
        'templates': [
            "What are the official international rules for writing a scientific name under the Binomial Nomenclature system?",
            "In the scientific name Mangifera indica, what does the first word 'Mangifera' represent, and how must it be written?",
            "In the scientific name Homo sapiens, what does the second word 'sapiens' represent, and how must it be written?",
            "When scientific names are HANDWRITTEN in notebooks, what is the mandatory typographical rule?"
        ],
        'data': [
            ("1. Names are in Latin and italicized when printed. 2. First word is Genus (starts with Capital), second is Species (lowercase). 3. When handwritten, both words are underlined separately", "Names must be in English; Both words must start with capitals; Names are never underlined; Species is written first followed by Genus"),
            ("It represents the GENUS (generic name) and must always begin with an UPPERCASE (capital) letter", "It represents the species and starts with lowercase; It represents the family; It is an adjective"),
            ("It represents the SPECIES (specific epithet) and must always begin with a LOWERCASE (small) letter", "It represents the genus and starts with capital; It represents the kingdom; It is the author name"),
            ("Both the genus name and the species name must be UNDERLINED SEPARATELY", "Both words must be underlined with one continuous line; No underlining is allowed; Written in capital letters only")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Universal rules of binomial nomenclature:\\n1. Biological names are derived from Latin and printed in italics.\\n2. The first word is the Genus (begins with a capital letter); the second word is the Species (begins with a lowercase letter).\\n3. When handwritten, both words must be underlined separately to indicate their Latin origin.\\n\\n**Step 2:** Examine the relevant taxonomic and evolutionary criteria.\\n\\n**Step 3:** Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Scientific names of common plants
    archs.append({
        'templates': [
            "What is the correct scientific name of the national fruit of India, MANGO?",
            "What is the scientific name of garden PEA, utilized by Gregor Mendel in his genetics experiments?",
            "What is the scientific name of WHEAT?",
            "What is the scientific name of the holy BANYAN tree (national tree of India)?"
        ],
        'data': [
            ("Mangifera indica", "Pisum sativum; Triticum aestivum; Ficus benghalensis"),
            ("Pisum sativum", "Mangifera indica; Triticum aestivum; Oryza sativa"),
            ("Triticum aestivum", "Oryza sativa; Zea mays; Solanum tuberosum"),
            ("Ficus benghalensis", "Ficus religiosa; Azadirachta indica; Mangifera indica")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Common plant scientific names:\\n- Mango: *Mangifera indica*\\n- Garden pea: *Pisum sativum*\\n- Wheat: *Triticum aestivum*\\n- Banyan tree: *Ficus benghalensis*\\n\\n**Step 2:** Examine the relevant taxonomic and evolutionary criteria.\\n\\n**Step 3:** Note that the genus begins with a capital letter and species with a lowercase letter, printed in italics. Correct name is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 4: Scientific names of common animals
    archs.append({
        'templates': [
            "What is the correct scientific name of modern HUMAN beings?",
            "What is the scientific name of the national animal of India, the TIGER?",
            "What is the scientific name of the common Indian bullfrog?",
            "What is the scientific name of the domestic housefly?"
        ],
        'data': [
            ("Homo sapiens", "Panthera tigris; Rana tigrina; Musca domestica"),
            ("Panthera tigris", "Panthera leo; Canis familiaris; Felis catus"),
            ("Rana tigrina (Hoplobatrachus tigerinus)", "Bufo melanostictus; Rana temporaria; Hyla versicolor"),
            ("Musca domestica", "Periplaneta americana; Apis mellifera; Anopheles stephensi")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Common animal scientific names:\\n- Human: *Homo sapiens*\\n- Tiger: *Panthera tigris*\\n- Lion: *Panthera leo*\\n- Frog: *Rana tigrina*\\n- Housefly: *Musca domestica*\\n\\n**Step 2:** Examine the relevant taxonomic and evolutionary criteria.\\n\\n**Step 3:** Correct name is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 5: Author citation in binomial nomenclature
    archs.append({
        'templates': [
            "In the botanical name Mangifera indica Linn., what does the abbreviation 'Linn.' signify?",
            "Where and how is the author's name cited in a complete scientific binomial?",
            "Why is the author's citation (e.g. 'Linn.') NOT printed in italics like the genus and species?",
            "Who first named the species when written as Homo sapiens L.?"
        ],
        'data': [
            ("It indicates that the species was first described and published by Carolus Linnaeus", "It means the plant was discovered in London; It means the plant is linear in shape; It denotes Latin language"),
            ("At the end of the biological name after the specific epithet, written in roman (upright) script without italics (e.g. Mangifera indica Linn.)", "Before the genus name; In parentheses between genus and species; As a footnote only"),
            ("Because it is the proper name of the describing author, not a Latin descriptive word forming part of the biological name itself", "Because printers had no italic font for names; Because Linnaeus forbade italics; Because authors are not Latin"),
            ("Carolus Linnaeus (L. stands for Linnaeus)", "Charles Darwin; Louis Pasteur; Antonie van Leeuwenhoek")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In taxonomic literature, the name of the author who first published a valid description of the species is appended at the end of the binomial name.\\n\\n**Step 2:** For example, *Mangifera indica* Linn. indicates that this species was originally named by Linnaeus.\\n\\n**Step 3:** The author's name is abbreviated and printed in regular roman type, not in italics. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 6: Why common names are inadequate
    archs.append({
        'templates': [
            "Why can vernacular (common local) names NOT be used for precise global scientific communication?",
            "Which of the following common names creates biological confusion by implying the organism is a true fish when it is actually an invertebrate?",
            "The Spanish name, Hindi name, and English name for onion are cebolla, pyaz, and onion respectively. Binomial nomenclature resolves this confusion by designating it as:",
            "Which animal is falsely called a 'fish' based on common vernacular naming?"
        ],
        'data': [
            ("Because common names vary from region to region, language to language, and often convey misleading biological relationships", "Because common names are in Latin; Because common names are too long; Because scientists cannot speak English"),
            ("Jellyfish (cnidarian), Starfish (echinoderm), and Cuttlefish (mollusc)", "Rohu; Catla; Shark"),
            ("Allium cepa", "Allium sativum; Solanum melongena; Brassica oleracea"),
            ("Starfish (it is an echinoderm, not a true vertebrate fish)", "Rohu (Labeo rohita); Salmon; Tuna")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Common names cause immense confusion because: (1) They vary across regions and languages (e.g. onion is called pyaaz, kanda, ulli, cebolla), (2) The same name may denote different organisms in different countries, (3) Misleading names exist (e.g. jellyfish, starfish, silverfish are not true fishes).\\n\\n**Step 2:** Examine the relevant taxonomic and evolutionary criteria.\\n\\n**Step 3:** Binomial nomenclature provides a unique, universal name across all countries. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 7: Tautonyms in zoological vs botanical nomenclature
    archs.append({
        'templates': [
            "What is a tautonym in biological nomenclature?",
            "Which of the following is a valid zoological tautonym?",
            "Are tautonyms (e.g. Malus malus) PERMITTED under the International Code of Botanical Nomenclature (ICBN)?",
            "Under the International Code of Zoological Nomenclature (ICZN), which animal has the valid tautonym Rattus rattus?"
        ],
        'data': [
            ("A scientific name in which the generic name and specific epithet are identical in spelling (e.g. Naja naja)", "A name with three words; A name named after two scientists; A name that has no meaning"),
            ("Naja naja (Indian cobra)", "Mangifera indica; Homo sapiens; Pisum sativum"),
            ("NO, tautonyms are strictly prohibited in plant nomenclature under ICBN, although allowed in animal nomenclature under ICZN", "YES, tautonyms are mandatory for all plants; YES, for all trees; Only for fungi"),
            ("The black rat (roof rat)", "The house mouse; The rabbit; The guinea pig")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** A tautonym is a scientific name where the genus and species names are identical (e.g. *Naja naja* for Indian cobra, *Rattus rattus* for house rat, *Catla catla* for Indian carp).\\n\\n**Step 2:** Tautonyms are valid in zoological nomenclature (ICZN).\\n\\n**Step 3:** However, they are strictly rejected in botanical nomenclature (ICBN). Correct answer is '{item[0]}'."
        ),
        'diff': 'hard'
    })

    # Arch 8: Identifying typographical errors in scientific names
    archs.append({
        'templates': [
            "A student writes the scientific name of human beings as 'homo Sapiens'. What two errors are present in this representation?",
            "Identify the SCIENTIFICALLY CORRECT representation of the botanical name of potato:",
            "Which of the following scientific names is formatted in STRICT COMPLIANCE with the rules of binomial nomenclature?",
            "Why is the representation 'panthera Leo' incorrect?"
        ],
        'data': [
            ("The genus name must start with a capital letter (Homo) and species name must start with lowercase (sapiens): Homo sapiens", "Both genus and species names must start with uppercase capital letters; The name should be written in French with accent marks; The generic name must be hyphenated with the specific epithet"),
            ("Solanum tuberosum (printed in italics, genus capitalized, species lowercase)", "Solanum Tuberosum (both genus and species capitalized); solanum tuberosum (both written in lowercase without capital); Solanum-tuberosum (words joined by an invalid hyphen)"),
            ("Panthera leo (capital P, lowercase l, printed in italics)", "panthera Leo (lowercase p, capital L); Panthera Leo (capital P, capital L); panthera leo (all lowercase letters without capital)"),
            ("Because the genus name 'Panthera' must begin with a capital letter and species name 'leo' must begin with a lowercase letter", "Because Leo should be Greek rather than Latin; Because lions are not classified within Kingdom Animalia; Because specific epithets require three capital letters")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Rules of binomial formatting:\\n- Genus starts with a CAPITAL letter.\\n- Species starts with a LOWERCASE letter.\\n- Italicized in print or underlined separately when handwritten.\\n\\n**Step 2:** Examine the relevant taxonomic and evolutionary criteria.\\n\\n**Step 3:** Therefore, *Panthera leo* and *Solanum tuberosum* are strictly correct. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-12-12.1.2', 'Binomial nomenclature system (Linnaeus)', archs)

# ==============================================================================
# SUBTOPIC 12.2.1: Kingdom Monera, Protista, Fungi, Plantae, Animalia
# ==============================================================================
def gen_12_2_1():
    archs = []

    # Arch 1: Kingdom Monera characteristics
    archs.append({
        'templates': [
            "What are the defining cellular characteristics of organisms belonging to Kingdom Monera?",
            "Which of the following organisms belongs to Kingdom Monera?",
            "In Monera, what type of nuclear organization is present?",
            "Cyanobacteria (blue-green algae like Anabaena and Nostoc) belong to Kingdom Monera because they are:"
        ],
        'data': [
            ("Unicellular PROKARYOTES lacking a membrane-bound nucleus and membrane-bound organelles", "Unicellular eukaryotes with a nucleus; Multicellular photosynthetic plants; Multicellular heterotrophic fungi"),
            ("Bacteria and Cyanobacteria (Blue-green algae)", "Amoeba and Paramecium; Yeast and Mushroom; Spirogyra and Ferns"),
            ("An incipient nucleus or nucleoid consisting of naked circular DNA without a nuclear membrane", "A true membrane-bound nucleus with nucleolus; Multiple nuclei with chromatin fibers; No DNA whatsoever"),
            ("prokaryotic photosynthetic organisms with peptidoglycan cell walls", "eukaryotic plants with flowers; multicellular algae; parasitic fungi")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Kingdom Monera encompasses all prokaryotic organisms (bacteria, cyanobacteria, mycoplasma).\\n\\n**Step 2:** They lack an organized membrane-bound nucleus; their genetic material is naked circular DNA (nucleoid).\\n\\n**Step 3:** They do not possess membrane-bound organelles (like mitochondria, chloroplasts, Golgi bodies). Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Kingdom Protista characteristics
    archs.append({
        'templates': [
            "What are the defining characteristics of organisms classified under Kingdom Protista?",
            "Which of the following organisms belongs to Kingdom Protista?",
            "How do diverse protists like Amoeba, Euglena, and Paramecium achieve locomotion?",
            "Why is Euglena considered a unique mixotrophic organism in Kingdom Protista?"
        ],
        'data': [
            ("Unicellular EUKARYOTIC organisms possessing a well-defined membrane-bound nucleus and organelles", "Unicellular prokaryotes without a nucleus; Multicellular photosynthetic trees; Filamentous saprophytic fungi"),
            ("Amoeba, Paramecium, Euglena, and Diatoms", "Bacteria and Cyanobacteria; Rhizopus and Agaricus; Moss and Ferns"),
            ("Amoeba moves using pseudopodia, Euglena uses a whip-like flagellum, and Paramecium uses thousands of hair-like cilia", "All move using muscular legs; All drift passively with zero movement; All fly using chitin wings"),
            ("Because it has chloroplasts to photosynthesize in sunlight (autotroph), but behaves as a heterotroph feeding on smaller organisms in the dark", "Because it has no nucleus; Because it lives in fire; Because it is half animal and half fungus")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Kingdom Protista includes all unicellular eukaryotic organisms.\\n\\n**Step 2:** They have a membrane-bound nucleus, mitochondria, and other organelles.\\n\\n**Step 3:** Locomotion occurs via pseudopodia (Amoeba), flagella (Euglena), or cilia (Paramecium). Euglena exhibits mixotrophic nutrition. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Kingdom Fungi characteristics and Chitin cell wall
    archs.append({
        'templates': [
            "What is the chemical composition of the rigid cell wall in organisms belonging to Kingdom Fungi?",
            "What is the predominant mode of nutrition in Kingdom Fungi?",
            "Which of the following is a UNICELLULAR fungus?",
            "The body of a typical multicellular fungus like Rhizopus or Mushroom consists of a network of thread-like filaments called:"
        ],
        'data': [
            ("Chitin (a tough, complex nitrogenous polysaccharide)", "Cellulose; Peptidoglycan; Silica"),
            ("Saprophytic (absorptive heterotrophs feeding on dead, decaying organic matter)", "Holozoic ingestion; Photosynthetic autotrophy; Chemosynthetic autotrophy"),
            ("Yeast (Saccharomyces)", "Agaricus (Mushroom); Rhizopus (Bread mould); Penicillium"),
            ("Hyphae (collectively forming the mycelium)", "Rhizoids; Pseudopodia; Flagella")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Fungi are eukaryotic, mostly multicellular (except unicellular yeast) heterotrophs.\\n\\n**Step 2:** Their cell wall is made of chitin (a tough complex nitrogen-containing polysaccharide), not cellulose.\\n\\n**Step 3:** They obtain nutrition saprophytically by secreting digestive enzymes onto decaying organic matter and absorbing soluble nutrients. The filamentous body network is called mycelium (composed of hyphae). Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 4: Lichens and Symbiotic association
    archs.append({
        'templates': [
            "What is a Lichen in biological terms?",
            "In the symbiotic relationship of a lichen, what role is played by the ALGAL component (phycobiont) and FUNGAL component (mycobiont) respectively?",
            "Why are lichens widely recognized as highly sensitive bio-indicators of atmospheric pollution?",
            "Which of the following organisms live in a mutually beneficial symbiotic relationship to form a lichen?"
        ],
        'data': [
            ("A mutually beneficial symbiotic association between an autotrophic alga (or cyanobacterium) and a heterotrophic fungus", "A parasitic infection of trees by moss; A single primitive plant species; A hybrid created by cross-pollination"),
            ("The alga synthesizes food by photosynthesis, while the fungus provides structural shelter, anchorage, and absorption of water and minerals", "The fungus makes food while alga produces seeds; Both eat dead animals; Alga consumes the fungus"),
            ("Because lichens are extremely sensitive to air pollution (especially sulfur dioxide, SO2) and cannot survive in polluted industrial air", "Because lichens emit smoke; Because lichens change color with humidity; Because lichens attract smog"),
            ("An alga and a fungus", "A bacterium and a virus; A plant and an insect; A protozoan and a worm")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Lichens are classic examples of mutualistic symbiosis between an alga/cyanobacterium (phycobiont) and a fungus (mycobiont).\\n\\n**Step 2:** The photosynthetic partner prepares carbohydrates, while the fungal partner provides shelter and absorbs water and mineral nutrients.\\n\\n**Step 3:** Lichens do not grow in polluted areas containing sulfur dioxide (\\(\\text{{SO}}_2\\)), making them natural bio-indicators of air quality. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 5: Kingdom Plantae characteristics
    archs.append({
        'templates': [
            "What are the defining characteristics of organisms classified under Kingdom Plantae?",
            "What is the chemical substance constituting the rigid cell wall of plant cells?",
            "Which photosynthetic pigment present in chloroplasts enables green plants to synthesize their own food?",
            "Plants store reserve carbohydrates primarily in the form of:"
        ],
        'data': [
            ("Multicellular EUKARYOTES with cellulose cell walls and chlorophyll-bearing plastids for autotrophic photosynthesis", "Unicellular prokaryotes without cell walls; Multicellular ingestive heterotrophs; Chitin-walled saprophytes"),
            ("Cellulose", "Chitin; Peptidoglycan; Keratin"),
            ("Chlorophyll", "Hemoglobin; Bilirubin; Melanin"),
            ("Starch", "Glycogen; Chitin; Glucose monomers only")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Kingdom Plantae includes all multicellular eukaryotic autotrophs.\\n\\n**Step 2:** They have rigid cell walls made of cellulose and carry photosynthetic pigments (chlorophyll) inside plastids to produce organic food from solar energy.\\n\\n**Step 3:** Excess carbohydrates are stored as starch. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 6: Kingdom Animalia characteristics
    archs.append({
        'templates': [
            "What are the defining characteristics of organisms belonging to Kingdom Animalia?",
            "Which cellular structure present in plant cells is completely ABSENT in all animal cells?",
            "Animals store reserve carbohydrates primarily in the form of:",
            "Most animals exhibit which predominant mode of nutrition?"
        ],
        'data': [
            ("Multicellular EUKARYOTES lacking cell walls and plastids, exhibiting holozoic ingestive heterotrophy", "Multicellular autotrophs with cellulose walls; Unicellular prokaryotes; Saprophytes with chitin walls"),
            ("Cell wall (and chloroplasts)", "Cell membrane; Nucleus; Mitochondria"),
            ("Glycogen (and fat)", "Starch; Cellulose; Chitin"),
            ("Holozoic nutrition (ingesting complex solid food internally, followed by digestion and absorption)", "Saprophytic absorption; Autotrophic photosynthesis; Parasitic absorption only")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Kingdom Animalia comprises multicellular eukaryotic organisms that lack cell walls and chloroplasts.\\n\\n**Step 2:** They exhibit holozoic ingestive heterotrophy (taking in food and digesting it internally).\\n\\n**Step 3:** Reserve food is stored as glycogen and fat. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 7: Whittaker's Five Kingdom summary matrix
    archs.append({
        'templates': [
            "An organism is eukaryotic, multicellular, has a cell wall made of chitin, and is heterotrophic. To which kingdom does it belong?",
            "An organism is unicellular, prokaryotic, and lacks a nuclear membrane. To which kingdom does it belong?",
            "An organism is eukaryotic, unicellular, and possesses a flagellum for movement. To which kingdom does it belong?",
            "An organism is multicellular, eukaryotic, lacks cell walls, and exhibits sensory locomotion. To which kingdom does it belong?"
        ],
        'data': [
            ("Kingdom Fungi", "Kingdom Plantae; Kingdom Monera; Kingdom Protista"),
            ("Kingdom Monera", "Kingdom Protista; Kingdom Fungi; Kingdom Animalia"),
            ("Kingdom Protista", "Kingdom Monera; Kingdom Plantae; Kingdom Fungi"),
            ("Kingdom Animalia", "Kingdom Plantae; Kingdom Fungi; Kingdom Protista")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Identify the combination of cell type, cell wall, and nutrition:\\n- Prokaryotic unicellular → Monera\\n- Eukaryotic unicellular → Protista\\n- Eukaryotic multicellular with chitin cell wall + heterotrophic → Fungi\\n- Eukaryotic multicellular with cellulose wall + autotrophic → Plantae\\n- Eukaryotic multicellular with NO cell wall + ingestive heterotrophic → Animalia.\\n\\n**Step 2:** Examine the relevant taxonomic and evolutionary criteria.\\n\\n**Step 3:** Correct kingdom is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 8: Mycoplasma (smallest cell without cell wall)
    archs.append({
        'templates': [
            "Which organism in Kingdom Monera is renowned as the smallest known free-living cell and completely lacks a cell wall?",
            "Why are Mycoplasma (PPLO - Pleuropneumonia-like organisms) completely immune to penicillin antibiotics?",
            "Which group of Monera live in extreme, hostile environments like boiling sulfur hot springs and salt pans?",
            "Methanogens, which produce methane gas (biogas) in the gut of ruminants like cows, are classified under:"
        ],
        'data': [
            ("Mycoplasma (PPLO)", "Cyanobacteria; Rhizobium; Bacillus"),
            ("Because penicillin acts by disrupting bacterial cell wall synthesis, and Mycoplasma naturally lacks a cell wall", "Because Mycoplasma has no DNA; Because Mycoplasma produces penicillin; Because Mycoplasma is a virus"),
            ("Archaebacteria (ancient bacteria: halophiles and thermoacidophiles)", "Eubacteria; Cyanobacteria; Fungi"),
            ("Archaebacteria", "Eubacteria; Protista; Fungi")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Mycoplasma (PPLO) are the smallest known living cells (~0.1 to 0.3 µm) and are unique among Monerans in lacking a cell wall completely.\\n\\n**Step 2:** Because they lack a peptidoglycan wall, cell-wall targeting antibiotics like penicillin are ineffective against them.\\n\\n**Step 3:** Archaebacteria possess distinct cell membranes allowing them to survive in extreme habitats. Correct answer is '{item[0]}'."
        ),
        'diff': 'hard'
    })

    return generate_vault_questions('CBSE-9-SCIE-12-12.2.1', 'Kingdom Monera, Protista, Fungi, Plantae, Animalia characteristics', archs)

# ==============================================================================
# SUBTOPIC 12.2.2: Plant kingdom divisions
# ==============================================================================
def gen_12_2_2():
    archs = []

    # Arch 1: Division Thallophyta (Algae)
    archs.append({
        'templates': [
            "What is the defining characteristic of plants belonging to Division Thallophyta (commonly called Algae)?",
            "Which of the following plants belongs to Division Thallophyta?",
            "Do plants of Division Thallophyta possess specialized vascular tissues (xylem and phloem) for water and food transport?",
            "Spirogyra, Ulothrix, Cladophora, and Chara are classified under which division of the plant kingdom?"
        ],
        'data': [
            ("Their body is NOT differentiated into true roots, stems, or leaves; it is a simple undifferentiated thallus", "They bear naked seeds in cones; They have taproots and flowers; They are terrestrial trees with wood"),
            ("Spirogyra and Ulothrix (also Chara, Cladophora, Ulva)", "Funaria and Marchantia; Ferns and Marsilea; Pinus and Cycas"),
            ("NO, Thallophytes lack specialized vascular tissues completely", "YES, they have advanced xylem vessels; YES, they have phloem companion cells; Only when growing on land"),
            ("Thallophyta (Algae)", "Bryophyta; Pteridophyta; Gymnosperms")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Division Thallophyta comprises primitive plants whose body design is not differentiated into roots, stems, and leaves.\\n\\n**Step 2:** The plant body is termed a thallus, and they are predominantly aquatic (freshwater or marine).\\n\\n**Step 3:** They lack vascular tissues (xylem and phloem). Examples: *Spirogyra*, *Ulothrix*, *Cladophora*, *Chara*, *Ulva*. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Division Bryophyta ('Amphibians of the plant kingdom')
    archs.append({
        'templates': [
            "Why are Bryophytes (mosses and liverworts) commonly referred to as the 'Amphibians of the plant kingdom'?",
            "What is the morphological structure of a typical bryophyte body?",
            "Which root-like thread structures anchor bryophytes to the soil and absorb water?",
            "Which of the following plants is a BRYOPHYTE?"
        ],
        'data': [
            ("Because they live on land (damp soil) but strictly depend on water for sexual reproduction (flagellated male gametes swim through water to reach the female organ)", "Because they can turn into frogs; Because they have gills; Because they photosynthesize only in lakes"),
            ("The body is differentiated to form stem and leaf-like structures, but lacks true vascular tissues and true roots", "It consists of massive woody trunks; It produces flowers and fruits; It is a single cell without a nucleus"),
            ("Rhizoids (hair-like anchoring structures)", "Taproots; Fibrous roots; Prop roots"),
            ("Funaria (moss), Marchantia, and Riccia", "Spirogyra; Marsilea; Pinus")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Bryophytes are terrestrial plants that inhabit damp, shady environments.\\n\\n**Step 2:** They are called 'amphibians of the plant kingdom' because while they live on soil, they require an external film of water for flagellated antherozoids (male gametes) to swim to the archegonium (female organ) for fertilization.\\n\\n**Step 3:** They have stem-like and leaf-like parts anchored by rhizoids, but lack true vascular tissues. Examples: *Funaria*, *Marchantia*, *Riccia*. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Division Pteridophyta (First vascular cryptogams)
    archs.append({
        'templates': [
            "What major evolutionary breakthrough distinguishes Pteridophytes (ferns) from Bryophytes and Thallophytes?",
            "The plant body of a Pteridophyte is differentiated into:",
            "Which of the following plants is classified under Division Pteridophyta?",
            "How do Pteridophytes reproduce, given that they do not produce flowers or seeds?"
        ],
        'data': [
            ("They possess specialized VASCULAR tissues (xylem and phloem) for the conduction of water and nutrients", "They produce edible fruits; They develop flowers with petals; They have naked seeds in cones"),
            ("True roots, stems, and leaves", "A thallus only; Stem and rhizoids without true roots; Wood and cones only"),
            ("Marsilea, Ferns (Dryopteris, Pteris), and Horsetails (Equisetum)", "Funaria and Riccia; Spirogyra and Chara; Apple and Mango"),
            ("Asexually via microscopic spores produced inside sporangia on the leaves", "By producing true seeds; By flowering; By budding only")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Pteridophytes are the first terrestrial plants to evolve specialized vascular tissues (xylem and phloem).\\n\\n**Step 2:** Their plant body is differentiated into true roots, stems, and leaves.\\n\\n**Step 3:** Like bryophytes and thallophytes, they reproduce via spores and do not produce seeds. Examples: *Marsilea*, ferns (*Dryopteris*, *Pteris*), horsetails (*Equisetum*). Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 4: Cryptogams vs Phanerogams
    archs.append({
        'templates': [
            "Plants belonging to Thallophyta, Bryophyta, and Pteridophyta are collectively called CRYPTOGAMS because:",
            "What are PHANEROGAMS in plant classification?",
            "Which plant divisions belong to Phanerogams (seed-bearing plants)?",
            "Which of the following plant groups is a CRYPTOGAM?"
        ],
        'data': [
            ("They have inconspicuous or hidden reproductive organs and reproduce by spores without producing seeds or flowers", "They produce naked seeds in cones; They produce enclosed seeds in fruits; They live only in dark caves"),
            ("Plants with well-differentiated, conspicuous reproductive tissues that produce SEEDS after fertilization", "Plants that reproduce only by fragmentation; Algae that float on water; Plants without vascular tissue"),
            ("Gymnosperms and Angiosperms", "Thallophyta and Bryophyta; Bryophyta and Pteridophyta; Algae and Fungi"),
            ("Ferns, Mosses, and Algae (Pteridophyta, Bryophyta, Thallophyta)", "Pine; Cycas; Sunflower")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Plant kingdom is broadly divided into two major super-groups:\\n\\n**Step 2:** Cryptogams ('hidden marriage'): Thallophyta, Bryophyta, and Pteridophyta, having hidden reproductive organs and producing spores without seeds.\\n\\n**Step 3:** Phanerogams ('visible marriage'): Gymnosperms and Angiosperms, possessing well-developed reproductive organs and producing seeds. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 5: Division Gymnosperms (Naked seeds)
    archs.append({
        'templates': [
            "What does the term 'Gymnosperm' literally mean in Greek botanical terms?",
            "What is the defining characteristic of seeds in Division Gymnospermae?",
            "What are the general vegetative characteristics of gymnosperm plants?",
            "Which of the following plants is a GYMNOSPERM?"
        ],
        'data': [
            ("Gymnos = naked, sperma = seed (Naked seeded plants)", "Covered seeds; Flowering trees; Single-celled plants"),
            ("The seeds are NAKED, meaning they develop exposed on scales of cones and are NOT enclosed within a fruit wall (ovary)", "Seeds are enclosed within a fleshy ovary; Seeds have no embryos; Seeds develop inside flowers"),
            ("Perennial, evergreen, and woody trees or shrubs", "Annual herbaceous weeds; Aquatic thallophytes; Soft non-vascular mosses"),
            ("Pinus (Pine) and Cycas (also Deodar - Cedrus)", "Pea and Gram; Mango and Apple; Rose and Jasmine")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Gymnosperms (from Greek *gymnos* = naked, *sperma* = seed) are seed-bearing plants where the ovules and seeds are not enclosed inside an ovary/fruit.\\n\\n**Step 2:** They bear seeds exposed on modified leaves forming reproductive cones (strobili).\\n\\n**Step 3:** They are typically perennial, evergreen, and woody trees. Examples: *Pinus* (pine), *Cycas*, *Cedrus* (deodar). Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 6: Division Angiosperms (Covered seeds / Flowering plants)
    archs.append({
        'templates': [
            "What does the term 'Angiosperm' literally mean in Greek botanical terms?",
            "What is the defining reproductive feature that distinguishes Angiosperms from Gymnosperms?",
            "In Angiosperms, seeds develop enclosed inside which organ that later ripens into a fruit?",
            "Which group represents the most highly evolved, diverse, and dominant plants on Earth today?"
        ],
        'data': [
            ("Angio = covered, sperma = seed (Covered-seeded plants)", "Naked seeds; Non-vascular plants; Spore-producing plants"),
            ("Seeds develop enclosed inside an ovary that ripens into a FRUIT, and flowers are present as reproductive organs", "Seeds are exposed on woody cones; Plants lack xylem vessels; Fertilization requires swimming sperms"),
            ("The Ovary", "The Thalamus; The Cone scale; The Petiole"),
            ("Angiosperms (Flowering plants)", "Gymnosperms; Pteridophytes; Bryophytes")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Angiosperms (from Greek *angio* = covered, *sperma* = seed) are flowering plants whose seeds develop enclosed inside an ovary.\\n\\n**Step 2:** The ovary ripens into a protective fruit enclosing the seeds.\\n\\n**Step 3:** They represent the most advanced and dominant plant group on Earth today. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 7: Monocotyledons vs Dicotyledons in Angiosperms
    archs.append({
        'templates': [
            "How do Monocots and Dicots differ with respect to cotyledons, leaf venation, and root system?",
            "Which of the following suites of characters is characteristic of a MONOCOT plant?",
            "Which of the following suites of characters is characteristic of a DICOT plant?",
            "Gram, Pea, Mustard, and Mango are examples of:"
        ],
        'data': [
            ("Monocots have 1 cotyledon, parallel leaf venation, and fibrous roots; Dicots have 2 cotyledons, reticulate (netted) venation, and taproots", "Monocots have taproots and reticulate venation; Dicots have 1 cotyledon and parallel venation; Both are identical"),
            ("Single cotyledon, parallel venation in leaves, fibrous root system, trimerous flowers (e.g. Maize, Grass, Wheat)", "Two cotyledons, reticulate venation, taproot system; Naked seeds in cones; Thalloid body"),
            ("Two cotyledons, reticulate (netted) venation in leaves, taproot system, tetramerous/pentamerous flowers (e.g. Pea, Gram, Mango)", "Single cotyledon, parallel venation, fibrous roots; Spores instead of seeds; Lack of xylem"),
            ("Dicotyledonous plants (Dicots)", "Monocotyledonous plants (Monocots); Gymnosperms; Pteridophytes")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Angiosperms are subdivided into two classes:\\n\\n**Step 2:** Monocotyledons (Monocots): 1 seed leaf (cotyledon), parallel leaf venation, and fibrous adventitious roots (e.g. maize, wheat, rice, grasses).\\n\\n**Step 3:** Dicotyledons (Dicots): 2 seed leaves (cotyledons), reticulate (webbed) leaf venation, and a primary taproot system (e.g. pea, gram, mustard, sunflower). Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 8: Plant Kingdom evolutionary dichotomous key
    archs.append({
        'templates': [
            "According to the plant classification flowchart, which plant group has differentiated body, vascular tissues, produces seeds, but has NAKED seeds without fruit enclosure?",
            "Which plant division has a thalloid body with no differentiation into roots, stems, or leaves?",
            "Which plant group is vascular, has true roots and leaves, but does NOT produce seeds?",
            "Trace the evolutionary sequence of major plant groups from primitive to advanced:"
        ],
        'data': [
            ("Gymnosperms", "Angiosperms; Pteridophyta; Bryophyta"),
            ("Thallophyta (Algae)", "Bryophyta; Pteridophyta; Gymnosperms"),
            ("Pteridophyta (Ferns)", "Gymnosperms; Angiosperms; Bryophyta"),
            ("Thallophyta → Bryophyta → Pteridophyta → Gymnosperms → Angiosperms", "Angiosperms → Gymnosperms → Pteridophyta → Bryophyta → Thallophyta; Bryophyta → Thallophyta → Gymnosperms → Pteridophyta → Angiosperms; Thallophyta → Gymnosperms → Bryophyta → Angiosperms")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Evolutionary sequence of the Plant Kingdom:\\n1. Thallophyta: non-differentiated body, non-vascular, aquatic spores.\\n2. Bryophyta: differentiated body, non-vascular, amphibious spores.\\n3. Pteridophyta: differentiated, vascular, non-seed spores.\\n4. Gymnosperms: differentiated, vascular, naked seeds in cones.\\n5. Angiosperms: differentiated, vascular, covered seeds in fruits with flowers.\\n\\n**Step 2:** Examine the relevant taxonomic and evolutionary criteria.\\n\\n**Step 3:** Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-12-12.2.2', 'Plant kingdom divisions', archs)

def main():
    all_questions = []

    print("Generating 12.1.1...")
    q1 = gen_12_1_1()
    print(f"12.1.1 generated {len(q1)} questions")
    all_questions.extend(q1)

    print("Generating 12.1.2...")
    q2 = gen_12_1_2()
    print(f"12.1.2 generated {len(q2)} questions")
    all_questions.extend(q2)

    print("Generating 12.2.1...")
    q3 = gen_12_2_1()
    print(f"12.2.1 generated {len(q3)} questions")
    all_questions.extend(q3)

    print("Generating 12.2.2...")
    q4 = gen_12_2_2()
    print(f"12.2.2 generated {len(q4)} questions")
    all_questions.extend(q4)

    out_file = 'scripts/cbse9_scie_ch12_part_a.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved {len(all_questions)} questions to {out_file}")

if __name__ == '__main__':
    main()
