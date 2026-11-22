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

            rot = (q_seq + arch_idx) % 4
            rotated_options = options_list[rot:] + options_list[:rot]
            labels = ["A", "B", "C", "D"]
            correct_letter = "A"
            final_options = []
            for idx, opt in enumerate(rotated_options):
                lbl = labels[idx]
                if opt["isCorrect"]:
                    correct_letter = lbl
                final_options.append({
                    "id": lbl,
                    "text": opt["text"],
                    "isCorrect": opt["isCorrect"]
                })

            opt_texts = [o["text"].strip().lower() for o in final_options]
            if len(set(opt_texts)) != 4:
                raise ValueError(f"Duplicate options detected in {topic_code} seq {q_seq}: {opt_texts}")

            q_code = f"{topic_code}-OSC-{q_seq:03d}"
            questions.append({
                "questionCode": q_code,
                "text": q_text,
                "options": final_options,
                "correctAnswer": correct_letter,
                "solution": solution,
                "difficulty": diff,
                "topicCode": topic_code,
                "subtopic": subtopic_name,
                "vault": vault,
                "type": "OSC",
                "marks": 4,
                "bloomsTaxonomy": "understand" if diff == "easy" else ("apply" if diff == "medium" else "analyze"),
                "estimatedTime": 60 if diff == "easy" else (90 if diff == "medium" else 120)
            })

            q_seq += 1

    return questions

# -------------------------------------------------------------
# SUBTOPIC 12.2.3: Animal kingdom non-chordates and chordates introduction
# -------------------------------------------------------------
def gen_12_2_3():
    archs = []

    # Arch 1: Levels of organization & body symmetry
    archs.append({
        'diff': 'easy',
        'templates': [
            "Which primary body symmetry and cellular organization is characteristically observed in {0}?",
            "Identify the fundamental body organization and symmetry exhibited by the organism {0}:",
            "In animal taxonomy, {0} is classified under which organizational grade and symmetry pattern?",
            "What level of organization and plane of symmetry define the anatomical body plan of {0}?"
        ],
        'data': [
            ("Sponges (Porifera)", "Cellular level with asymmetrical body symmetry", "Tissue level with bilateral symmetry; Organ system with pentamerous radial symmetry; Organ level with bilateral symmetry"),
            ("Hydra (Cnidaria)", "Tissue level of organization with radial symmetry", "Cellular level with bilateral symmetry; Organ system with bilateral symmetry; Organ level with asymmetry"),
            ("Planaria (Platyhelminthes)", "Organ level of organization with bilateral symmetry", "Tissue level with radial symmetry; Cellular level with spherical symmetry; Organ system with asymmetry"),
            ("Earthworm (Annelida)", "Organ system level of organization with bilateral symmetry", "Cellular level with radial symmetry; Tissue level with asymmetry; Organ level with pentaradial symmetry"),
            ("Cockroach (Arthropoda)", "Organ system level of organization with bilateral symmetry", "Tissue level with radial symmetry; Cellular level with bilateral symmetry; Organ level with asymmetry"),
            ("Pila (Mollusca)", "Organ system level of organization with bilateral symmetry (in larva/adult prior to torsion)", "Cellular level with radial symmetry; Tissue level with radial symmetry; Cellular grade with spherical symmetry"),
            ("Adult Starfish (Echinodermata)", "Organ system level with pentamerous radial symmetry", "Cellular level with bilateral symmetry; Tissue level with asymmetry; Organ grade with unilateral asymmetry"),
            ("Starfish larva", "Bilateral symmetry in larval development transitioning to radial symmetry in adult", "Pentaradial symmetry in larva transitioning to asymmetry; Cellular grade without symmetry; Spherical symmetry in both stages"),
            ("Jellyfish (Aurelia)", "Tissue level of organization with radial symmetry", "Organ system level with bilateral symmetry; Cellular level with bilateral symmetry; Organ grade with asymmetry"),
            ("Ascaris (Roundworm)", "Organ system level of organization with bilateral symmetry", "Tissue level with radial symmetry; Cellular level with spherical symmetry; Organ level with asymmetry")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand body plan classification.** Organisms are classified by level of organization (cellular, tissue, organ, organ system) and symmetry (asymmetrical, radial, bilateral).\n**Step 2: Examine {item[0]}.** {item[0]} displays {item[1]}.\n**Step 3: Conclusion.** Hence, the correct diagnostic feature is {item[1]}."
        )
    })

    # Arch 2: Coelom types (acoelomate, pseudocoelomate, eucoelomate)
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which category of body cavity (coelom) is strictly characteristic of the phylum {0}?",
            "Organisms belonging to the phylum {0} possess which diagnostic coelomic body plan?",
            "How is the body cavity structurally classified in the taxonomic group {0}?",
            "What type of coelomic architecture is identified in representatives of phylum {0}?"
        ],
        'data': [
            ("Platyhelminthes (Flatworms)", "Acoelomate (solid body without a coelom between digestive tract and body wall)", "Pseudocoelomate with scattered mesodermal pouches; Eucoelomate with true mesodermal lining; Enterocoelomate with secondary pouching"),
            ("Aschelminthes / Nematoda (Roundworms)", "Pseudocoelomate (body cavity not lined completely by mesoderm, present as scattered pouches)", "True coelomate with peritoneal lining; Acoelomate with solid mesenchyme; Schizocoelomate with haemocoel"),
            ("Annelida (Segmented worms)", "Eucoelomate (true coelom lined by mesodermal epithelium)", "Pseudocoelomate with unlined blastocoel; Acoelomate without cavity; Non-coelomic cellular parenchymal cavity"),
            ("Arthropoda", "Eucoelomate with a reduced true coelom forming a haemocoel filled with haemolymph", "Acoelomate with solid mesenchyme; Pseudocoelomate with persistent blastocoel; Enterocoelomate with closed capillaries"),
            ("Mollusca", "Eucoelomate with coelom restricted mainly to pericardial cavity and gonocoel", "Pseudocoelomate throughout visceral mass; Acoelomate without any internal fluid space; Non-triploblastic blastocoel"),
            ("Echinodermata", "Enterocoelomate (true coelom lined by mesoderm arising from archenteron pouches)", "Pseudocoelomate with blastocoelic origin; Acoelomate with parenchymal packing; Haemocoelomic without mesoderm"),
            ("Chordata", "Eucoelomate (true enterocoelous or schizocoelous body cavity fully lined by mesoderm)", "Pseudocoelomate with false cavity; Acoelomate lacking body lining; Haemocoelomate without epithelial peritoneum"),
            ("Porifera", "Spongocoel (paragastric cavity lined by choanocytes, not a true coelomic body cavity)", "True mesodermal coelom; Pseudocoelom lined by endoderm; Schizocoel lined by ectoderm"),
            ("Cnidaria", "Gastrovascular cavity (coelenteron serving both digestion and circulation, not a coelom)", "Peritoneal true coelom; Pseudocoelom with mesodermal pouches; Haemocoel containing haemocyanin"),
            ("Ctenophora", "Acoelomate with solid mesenchymal jelly without a true body cavity", "Pseudocoelomate with mesodermal lining; Eucoelomate with schizocoel; Haemocoel with open circulation")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Define coelomic categories.** A true coelom (eucoelom) is lined by mesoderm. A pseudocoelom retains the blastocoel with scattered mesoderm pouches. Acoelomates lack any body cavity.\n**Step 2: Analyze {item[0]}.** The group {item[0]} exhibits {item[1]}.\n**Step 3: Match options.** Therefore, {item[1]} is the correct classification."
        )
    })

    # Arch 3: Phylum Porifera & Cnidaria
    archs.append({
        'diff': 'easy',
        'templates': [
            "Which specialized cell or diagnostic feature is exclusively found in {0}?",
            "Identify the unique structural or functional adaptation characteristic of {0}:",
            "What distinctive cellular element enables defense, food capture, or water circulation in {0}?",
            "In aquatic invertebrates, which morphological feature defines {0}?"
        ],
        'data': [
            ("Phylum Porifera (Sponges)", "Choanocytes (collar cells) lining the internal canal system for water filtration", "Cnidoblasts with nematocysts; Flame cells for excretion; Statocysts for equilibrium"),
            ("Phylum Cnidaria (Coelenterata)", "Cnidocytes containing stinging nematocysts used for anchorage, defense, and prey capture", "Choanocytes lining spongocoel; Nephridia for nitrogenous waste; Malpighian tubules for excretion"),
            ("Sycon / Spongilla", "Ostia for water entry and a large osculum for water exit driven by flagella", "Tentacles with nematocytes; Radula with chitinous teeth; Parapodia with chaetae"),
            ("Hydra", "Gastrovascular cavity with a single opening acting as mouth and anus", "Complete alimentary canal with separate anus; Canal system with dermal pores; Tracheal system with spiracles"),
            ("Physalia (Portuguese man-of-war)", "Polymorphism exhibiting distinct zooids for feeding, reproduction, and defense", "Monomorphic cellular aggregation; Segmented metamerism; Water vascular canal system"),
            ("Corals (Cnidaria)", "Calcium carbonate exoskeleton secreted by colonial polyps", "Siliceous spicules of spongin fibers; Chitinous segmented cuticle; Shell of mantle origin with radula"),
            ("Spongin fibers and spicules", "Skeletal framework supporting the soft body structure of diverse sponges", "Muscular foot providing locomotion; Jointed exoskeleton of chitin; Cartilaginous vertebral rod"),
            ("Metagenesis in Obelia", "Alternation of generations between asexual sessile polyp and sexual free-swimming medusa", "Complete metamorphosis from caterpillar to imago; Asexual regeneration without gametes; Parthenogenetic alternation of males"),
            ("Sea anemone (Adamsia)", "Symbiotic sessile polyp association with hermit crab providing protection and mobility", "Parasitic attachment via scolex hooks; Free-swimming solitary medusa; Colonial freshwater spongin network"),
            ("Aurelia (Moon jelly)", "Medusa dominant form characterized by a umbrella-shaped gelatinous bell", "Sessile polyp form secreting calcareous reefs; Cellular poriferous encrustation; Bilateral segmented vermiform body")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Identify taxon characteristics.** Sponges possess choanocytes and a water canal system. Cnidarians possess stinging cnidoblasts/nematocysts and a gastrovascular cavity.\n**Step 2: Relate to {item[0]}.** The hallmark diagnostic feature for {item[0]} is {item[1]}.\n**Step 3: Deduce option.** Thus, the correct answer is {item[1]}."
        )
    })

    # Arch 4: Platyhelminthes & Nematoda
    archs.append({
        'diff': 'medium',
        'templates': [
            "What distinguishes the parasitic flatworm or roundworm {0} from other helminthes?",
            "Which physiological or structural specialization is correctly attributed to {0}?",
            "Identify the excretory or morphological hallmark of the helminth {0}:",
            "In invertebrate zoology, {0} is characterized by which anatomical trait?"
        ],
        'data': [
            ("Planaria (Turbellaria)", "High regeneration capacity and specialized flame cells (protonephridia) for osmoregulation", "Pseudocoelom with tubular gut; Metameric segmentation with setae; Jointed appendages with antennae"),
            ("Taenia solium (Tapeworm)", "Scolex with hooks and suckers, absence of digestive tract, and nutrient absorption through tegument", "Well-developed muscular pharynx and anus; Radula with horny teeth; Ciliated epidermis with gastrovascular cavity"),
            ("Fasciola hepatica (Liver fluke)", "Bifurcated incomplete gut, oral and ventral suckers, and hermaphroditic reproduction", "Pseudocoelomic fluid hydrostatic skeleton; Chitinous exoskeleton with moulting; Complete gut with terminal anus"),
            ("Ascaris lumbricoides (Roundworm)", "Unsegmented cylindrical body, complete alimentary canal with muscular pharynx, and sexual dimorphism", "Acoelomate flat dorsoventrally compressed body; Hermaphroditic monoecious anatomy; Flame cell excretory network"),
            ("Wuchereria bancrofti (Filarial worm)", "Parasitic nematode causing lymphatic filariasis (elephantiasis) transmitted by Culex mosquito", "Flatworm causing cysticercosis via pork; Free-living turbellarian in ponds; Annelid causing skin irritation"),
            ("Ancylostoma (Hookworm)", "Oral cutting plates for latching onto intestinal mucosa and sucking blood", "Flame cell tubules without mouth; Calcareous shell with operculum; Ctenidia for branchial respiration"),
            ("Flame cells (Protonephridia)", "Specialized excretory and osmoregulatory cells operating in Platyhelminthes", "Excretory Malpighian tubules in insects; Nephridial funnel tubules in annelids; Green antennal glands in crustaceans"),
            ("Pseudocoelom in nematodes", "Hydrostatic skeleton providing internal turgor pressure for undulating movement", "Open circulatory sinuses for oxygen delivery; Calcareous internal skeletal rod; Chitinous endoskeleton for muscle levers"),
            ("Sexual dimorphism in Ascaris", "Female is distinctly longer and thicker than the male which has a curved posterior tail", "Male is much larger with brooding pouches; Both sexes are structurally indistinguishable; Hermaphroditic self-fertilizing organs"),
            ("Syncytial epidermis of Ascaris", "Multinucleated cytoplasmic layer without cell boundaries covered by thick resistant cuticle", "Single layered ciliated cellular epithelium; Calcareous crystalline mantle; Metameric septated hypodermis")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Contrast Platyhelminthes and Nematoda.** Platyhelminthes are dorsoventrally flattened acoelomates with flame cells; Nematodes are cylindrical pseudocoelomates with a complete gut and thick cuticle.\n**Step 2: Evaluate {item[0]}.** Its defining characteristic is {item[1]}.\n**Step 3: Match the correct choice.** The correct statement is {item[1]}."
        )
    })

    # Arch 5: Annelida & Arthropoda
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which anatomical specialization is fundamentally unique to {0}?",
            "Identify the diagnostic physiological or structural adaptation of {0}:",
            "In comparative invertebrate biology, what key feature distinguishes {0}?",
            "How is locomotion, excretion, or circulation organized in {0}?"
        ],
        'data': [
            ("Earthworm (Pheretima)", "True metameric segmentation, closed circulatory system, and nephridia for excretion", "Open haemocoel with Malpighian tubules; Pseudocoelomic cavity with flame cells; Unsegmented body with mantle"),
            ("Leech (Hirudinaria)", "Suckers at anterior and posterior ends, anticoagulant hirudin secretion, and sanguivorous diet", "Jointed walking legs with chitinous carapace; Flame cells with paired tentacles; Radula with calcareous shell"),
            ("Phylum Arthropoda", "Jointed appendages, chitinous exoskeleton, open circulatory system with haemocoel", "Closed blood vessels with haemoglobin; Unsegmented body with ciliated mantle; Paragastric canal system with ostia"),
            ("Cockroach (Periplaneta)", "Tracheal system with spiracles for respiration and Malpighian tubules for uric acid excretion", "Gills with nephridia; Book lungs with flame cells; Ctenidia with green glands"),
            ("Prawn (Palaemon)", "Green glands (antennal glands) for excretion and gills enclosed in branchial chambers for respiration", "Malpighian tubules with tracheal tubes; Nephridia with skin respiration; Flame cells with book gills"),
            ("Scorpion / Spider (Arachnida)", "Book lungs for aerial respiration and cephalothorax without antennae", "Tracheal system with three pairs of antennae; Branchial gills with compound eyes; Ciliated skin with muscular foot"),
            ("Centipede (Chilopoda)", "Flattened body with one pair of legs per segment and venomous maxillipeds (poison claws)", "Two pairs of legs per segment and chewing herbivorous mouthparts; Unsegmented body with suckers; Jointed chelae with swim bladders"),
            ("Millipede (Diplopoda)", "Cylindrical body with two pairs of legs per visible diplosegment and herbivorous habit", "One pair of legs per segment with poison fangs; Solid acoelomate body with flame cells; Calcareous shell with muscular foot"),
            ("Compound eyes in Arthropods", "Visual organs composed of thousands of independent ommatidia providing mosaic vision", "Single biconvex lens providing monocular vision; Statocysts providing light direction only; Simple photoreceptive eye spots"),
            ("Chitinous exoskeleton", "Protective cuticular layer preventing desiccation and serving as muscle attachment points", "Fluid hydrostatic chamber lined by peritoneum; Siliceous spicule grid without joints; Internal bony column of vertebrae")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Analyze taxonomic characters.** Annelids exhibit metameric segmentation, true coelom, and closed circulation. Arthropods have jointed appendages, chitinous exoskeleton, and open haemocoel.\n**Step 2: Inspect {item[0]}.** {item[0]} is specifically identified by {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 6: Mollusca & Echinodermata
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which unique organ or developmental feature defines {0}?",
            "What physiological mechanism or body component is characteristic of {0}?",
            "In marine and freshwater invertebrates, {0} is uniquely identified by which structure?",
            "Identify the defining morphological or anatomical marker for {0}:"
        ],
        'data': [
            ("Phylum Mollusca", "Soft unsegmented body covered by a calcareous shell secreted by the mantle, with a muscular foot", "Jointed appendages with chitinous cuticle; Radially symmetrical spiny skin with water vascular system; Segmented body with setae"),
            ("Radula in Mollusca", "File-like rasping organ with transverse rows of chitinous teeth used for feeding", "Filter-feeding choanocyte collar; Piercing stylet of nematode; Chewing mandible of arthropod"),
            ("Water vascular (ambulacral) system", "Hydraulic canal system driving locomotion, food capture, and respiration via tube feet in Echinoderms", "Open blood vascular system in insects; Closed double circulation in vertebrates; Hydrostatic pseudocoelom in roundworms"),
            ("Adult vs larval Echinoderms", "Bilateral symmetry in free-swimming larva and pentamerous radial symmetry in adult", "Radial symmetry in larva and bilateral symmetry in adult; Asymmetry in both larval and adult stages; Spherical symmetry throughout life"),
            ("Starfish (Asterias)", "Oral-aboral axis, ambulacral grooves with tube feet, and high capacity for arm autotomy/regeneration", "Distinct head with antennae and compound eyes; Mantle cavity with ctenidia; Segmented trunk with parapodia"),
            ("Pila (Apple snail)", "Asymmetric coiled shell, unsegmented visceral hump, and dual respiration via ctenidium and pulmonary sac", "Bilateral bivalve shell with siphon; Segmented body with setae; Tube feet with madreporite"),
            ("Octopus (Cephalopoda)", "Large brain, well-developed image-forming eyes, eight arms with suckers, and ink sac for defense", "External bivalve shell with rasping radula; Jointed legs with exoskeleton; Calcareous spines with pedicellariae"),
            ("Echinus (Sea urchin)", "Globular shell (test) of fused calcareous plates bearing movable spines and Aristotle's lantern", "Soft body with internal pen; Metameric segments with setae; Parasitic scolex with hooks"),
            ("Madreporite in Echinoderms", "Perforated sieve plate regulating the entry of seawater into the water vascular system", "Excretory pore discharging nitrogenous urea; Sensory organ detecting light direction; Muscular siphon for jet propulsion"),
            ("Mantle cavity in Molluscs", "Space between mantle and visceral hump housing ctenidia (gills) for respiration and excretion", "Coelomic blastocoel filled with haemolymph; Enteron cavity lined by digestive cells; Spongocoel lined by flagellated cells")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand Mollusca and Echinodermata characteristics.** Molluscs have soft bodies, mantle, muscular foot, and radula. Echinoderms possess a spiny skin, endoskeleton of calcareous ossicles, and a unique water vascular system.\n**Step 2: Examine {item[0]}.** The correct trait for {item[0]} is {item[1]}.\n**Step 3: Conclusion.** Hence, {item[1]} is the correct option."
        )
    })

    # Arch 7: Chordata fundamental features & subphyla
    archs.append({
        'diff': 'hard',
        'templates': [
            "Which primary anatomical hallmark fundamentally separates chordates from non-chordates in {0}?",
            "What critical diagnostic structure is universally present at some stage of life in {0}?",
            "In chordate comparative anatomy, which statement accurately characterizes {0}?",
            "How does {0} demonstrate the foundational architecture of the phylum Chordata?"
        ],
        'data': [
            ("Fundamental Chordate characteristics", "Notochord, dorsal tubular nerve cord, paired pharyngeal gill slits, and post-anal tail", "Ventral solid nerve cord, heart located dorsally, and absence of pharyngeal slits; Open haemocoel, chitinous rod, and absence of coelom; Invertebrate ciliated canal system with ventral heart"),
            ("Notochord function", "Flexible solid rod-like structure lying dorsal to gut and ventral to nerve cord serving as primary skeletal support", "Hollow fluid tube transmitting neural action potentials; Muscular valve regulating blood pressure; Digestive diverticulum secreting digestive enzymes"),
            ("Dorsal hollow nerve cord", "Ectodermal tubular neural tube situated above the notochord developing into brain and spinal cord", "Solid double ventral nerve cord with paired segmental ganglia; Diffuse epidermal nerve net without centralization; Ventral muscular nerve strand"),
            ("Urochordata (Protochordates)", "Notochord present only in the free-swimming larval tail, lost during retrogressive metamorphosis in adult (e.g., Herdmania, Ascidia)", "Notochord persistent throughout life extending from head to tail; Vertebral column replacing notochord in embryo; Complete absence of notochord in all life stages"),
            ("Cephalochordata (Protochordates)", "Notochord extends from head to tail (rostrum to posterior) and persists throughout entire life (e.g., Branchiostoma / Amphioxus)", "Notochord confined to proboscis region only; Notochord present only in embryonic tail; Bony vertebrae replacing notochord in adult"),
            ("Subphylum Vertebrata", "Embryonic notochord replaced by a cartilaginous or bony vertebral column in the adult", "Notochord remains unsegmented and flexible throughout life; Absence of endoskeleton and cranium; Ventral solid nerve cord without brain"),
            ("Nerve cord position: Chordates vs Non-chordates", "Dorsal, single, and hollow in chordates; Ventral, double, and solid with ganglia in non-chordates", "Ventral and hollow in chordates; Dorsal and solid in non-chordates; Lateral and paired in chordates; Centralized diffuse in non-chordates"),
            ("Heart position: Chordates vs Non-chordates", "Ventrally positioned in chordates; Dorsally positioned (if present) in non-chordates", "Dorsal in chordates; Ventral in non-chordates; Lateral in chordates; Terminal in non-chordates"),
            ("Pharyngeal gill slits", "Paired lateral openings in the pharynx used for filter-feeding or respiration during development", "Tracheal invaginations opening along the abdomen; Dermal branchiae arising from calcareous plates; Modified mantle cavities with radula"),
            ("Post-anal tail", "Muscular extension of the body projecting beyond the anus used for locomotion and balance", "Anterior cephalic prolongation before the mouth; Pre-anal fleshy lobe containing the gut; Segmented pygidium bearing the terminal anus")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Recall fundamental chordate hallmarks.** Chordates have a dorsal hollow nerve cord, notochord, paired pharyngeal gill slits, and a post-anal tail.\n**Step 2: Differentiate chordate subphyla and non-chordates.** Non-chordates have a ventral solid nerve cord and dorsal heart. In vertebrates, the notochord is replaced by a vertebral column.\n**Step 3: Analyze {item[0]}.** The correct concept is {item[1]}."
        )
    })

    # Arch 8: Vertebrata Classes
    archs.append({
        'diff': 'hard',
        'templates': [
            "Which combination of circulatory, thermal, and integumentary traits defines the vertebrate class {0}?",
            "Identify the key anatomical and physiological adaptations characteristic of {0}:",
            "In vertebrate classification, what diagnostic set of traits distinguishes {0} from other classes?",
            "How are cardiac structure, respiration, and thermoregulation organized in {0}?"
        ],
        'data': [
            ("Class Pisces (Fishes)", "2-chambered heart (one atrium, one ventricle), single venous circulation, poikilothermic (cold-blooded), gills for respiration", "3-chambered heart, double circulation, homeothermic, lung respiration; 4-chambered heart, single circulation, cold-blooded, skin respiration; 3-chambered heart, pulmonary respiration, warm-blooded, epidermal scales"),
            ("Class Amphibia (Frogs, Salamanders)", "3-chambered heart (two atria, one ventricle), poikilothermic, moist glandular scale-less skin, dual respiration (gills in larva, skin/lungs/buccopharynx in adult)", "2-chambered heart, warm-blooded, dry cornified scaly skin, gill respiration; 4-chambered heart, cold-blooded, feathered body, air sacs; 3-chambered heart, homeothermic, thick hair, external ear pinna"),
            ("Class Reptilia (Lizards, Snakes, Turtles)", "3-chambered heart with incomplete ventricular septum (4-chambered in crocodiles), poikilothermic, dry cornified skin with epidermal scales, pulmonary respiration", "2-chambered heart, homeothermic, moist skin, branchial respiration; 4-chambered heart, poikilothermic, feathers, external ear opening; 3-chambered heart, warm-blooded, smooth skin, cutaneous respiration"),
            ("Class Aves (Birds)", "4-chambered heart, homeothermic (warm-blooded), forelimbs modified into wings, pneumatic (hollow) bones, lungs with air sacs", "3-chambered heart, cold-blooded, solid heavy bones, gills with operculum; 4-chambered heart, poikilothermic, mammary glands, epidermal scales; 2-chambered heart, warm-blooded, cutaneous respiration, claws"),
            ("Class Mammalia", "4-chambered heart, homeothermic, presence of mammary glands, skin with hair and sweat/sebaceous glands, external pinna, enucleated RBCs", "3-chambered heart, cold-blooded, crop and gizzard, pneumatic bones, nucleated RBCs; 4-chambered heart, poikilothermic, dry epidermal scales, oviparous cleidoic eggs; 2-chambered heart, homeothermic, operculum, placoid scales"),
            ("Heart structure in Crocodiles", "4-chambered heart with complete ventricular separation, exceptional among reptiles", "2-chambered heart with single atrium; 3-chambered heart without any septum; 5-chambered heart with accessory sinuses"),
            ("Pneumatic bones in Aves", "Hollow air-filled bones reducing body weight as an aerodynamic flight adaptation", "Dense mineralized bones providing heavy ballast for diving; Cartilaginous fibrous bones lacking marrow cavity; Flexible uncalcified collagenous rods"),
            ("Mammary glands in Mammals", "Specialized exocrine glands producing milk for nourishing neonates, unique to mammals", "Secretory oil glands preening plumage; Venom glands in cephalic palps; Endocrine glands controlling ecdysis"),
            ("Homeothermic vs Poikilothermic vertebrates", "Aves and Mammalia regulate constant body temperature; Pisces, Amphibia, and Reptilia depend on environmental temperature", "Mammals and Reptiles are homeothermic; Birds and Fishes are poikilothermic; Amphibians and Birds maintain constant heat; All vertebrates are homeothermic"),
            ("Placoid vs Cycloid/Ctenoid scales", "Placoid scales with backward denticles in cartilaginous fishes (Chondrichthyes); Cycloid/Ctenoid dermal scales in bony fishes (Osteichthyes)", "Placoid scales in bony fishes; Cycloid scales in reptiles; Horny epidermal scutes in amphibians; Pneumatic dermal plates in birds")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand vertebrate classification.** Pisces have 2 chambers; Amphibians have 3 chambers; Reptiles have 3 chambers (crocodiles have 4); Birds and Mammals have 4 chambers and are homeothermic.\n**Step 2: Inspect {item[0]}.** The correct combination of features is {item[1]}.\n**Step 3: Deduce option.** Therefore, the correct answer is {item[1]}."
        )
    })

    return generate_vault_questions('CBSE-9-SCIE-12-12.2.3', 'Animal kingdom non-chordates and chordates introduction', archs)

# -------------------------------------------------------------
# SUBTOPIC 12.3.1: Significance of biodiversity in ecosystems
# -------------------------------------------------------------
def gen_12_3_1():
    archs = []

    # Arch 1: Levels of biodiversity
    archs.append({
        'diff': 'easy',
        'templates': [
            "Which fundamental level of biological diversity is exemplified by {0}?",
            "How is the biological variation in {0} categorized within biodiversity levels?",
            "Identify the specific tier of biodiversity described by {0}:",
            "In ecology, {0} represents which level of biodiversity?"
        ],
        'data': [
            ("Over 50,000 genetically different strains of rice and 1,000 varieties of mango in India", "Genetic diversity (variation of genes within a single species)", "Species diversity; Ecosystem diversity; Biome-level diversity"),
            ("Greater amphibian species richness in the Western Ghats compared to the Eastern Ghats", "Species diversity (richness and variety of distinct species within a region)", "Genetic diversity; Biome diversity; Genetic polymorphism"),
            ("Presence of deserts, rain forests, mangroves, coral reefs, wetlands, and alpine meadows in India", "Ecosystem / Ecological diversity (variety of habitats and ecological processes)", "Species diversity; Genetic diversity; Allelic diversity"),
            ("Difference in concentration and potency of the active chemical reserpine in Rauwolfia vomitoria", "Genetic diversity within a plant species across different Himalayan ranges", "Ecosystem diversity across biomes; Interspecific taxonomic divergence; Trophic level diversification"),
            ("Alpha diversity (local species richness)", "Diversity of species within a single uniform community or local habitat", "Diversity across a whole landscape; Regional species turnover; Allele frequency distribution"),
            ("Beta diversity (species turnover)", "Rate of change in species composition along an environmental or geographic gradient between habitats", "Total regional diversity of a continent; Allelic variation within one population; Trophic biomass pyramid"),
            ("Gamma diversity (regional diversity)", "Overall species diversity across all habitats within a broad geographic region or landscape", "Local within-habitat species count; Intra-individual gene expression; Microhabitat bacterial variation"),
            ("Allelic variation in crop pest resistance genes", "Genetic diversity vital for crop breeding and resilience against pathogens", "Ecosystem-level biome stratification; Inter-phylum taxonomic richness; Biogeographic faunal interchange"),
            ("Coexistence of herbivores, carnivores, and decomposers in a coral reef", "Species and ecosystem diversity sustaining complex food webs", "Intra-clonal genetic uniformity; Mono-specific habitat dominance; Unidirectional succession"),
            ("High diversity of cichlid fish species in Lake Victoria", "Species diversity arising from adaptive radiation within an aquatic ecosystem", "Ecosystem-wide biome replacement; Genetic cloning without mutation; Artificial human monoculture")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Distinguish biodiversity levels.** Biodiversity is structured into: Genetic diversity (within species), Species diversity (among species), and Ecological/Ecosystem diversity (among habitats and biomes).\n**Step 2: Analyze {item[0]}.** This manifests {item[1]}.\n**Step 3: Conclusion.** Hence, {item[1]} is correct."
        )
    })

    # Arch 2: Provisioning ecosystem services
    archs.append({
        'diff': 'easy',
        'templates': [
            "Which provisioning ecosystem service directly supplied by biodiversity is represented by {0}?",
            "What direct material benefit or provisioning service of biodiversity is illustrated in {0}?",
            "Identify the economic or survival resource categorized under provisioning services in {0}:",
            "How does biodiversity act as a direct provider of human needs in {0}?"
        ],
        'data': [
            ("Quinine derived from Cinchona bark and Taxol from Yew tree", "Medicinal drugs and pharmaceuticals obtained directly from natural plant biodiversity", "Climate regulation through evapotranspiration; Soil formation via humification; Nutrient cycling through mycorrhizae"),
            ("Cereal crops, pulses, fruits, and livestock breeds", "Food and nutritional sustenance harvested from domestic and wild biodiversity", "Carbon sequestration by peat bogs; Coastal defense by barrier reefs; Flood moderation by wetlands"),
            ("Timber, bamboo, thatch, and firewood", "Structural materials and biomass energy derived from forest ecosystems", "Hydrological cycle stabilization; Pollination of orchards; Genetic preservation in permafrost"),
            ("Natural fibers such as cotton, jute, silk, and wool", "Raw textile materials obtained from agricultural plants and domesticated animals", "Atmospheric oxygen regeneration; Geological weathering of parent rock; Soil mycorrhizal bio-filtration"),
            ("Fresh water yield filtered through forested watersheds", "Provisioning of clean potable water through natural forested catchments", "Decomposition of organic matter; Pollination by solitary bees; Aesthetic inspiration for arts"),
            ("Industrial biochemicals, tannins, resins, and gums", "Natural biochemical feedstocks and adhesives extracted from diverse plant taxa", "Trophic cascade moderation; Global temperature buffering; Wave energy dissipation"),
            ("Genetic pool from wild relatives of wheat and rice", "Genes conferring drought and pest resistance for breeding resilient high-yield crops", "Direct aesthetic recreational income; Primary bedrock weathering; Denitrification in wetlands"),
            ("Marine fish catches, crustaceans, and edible molluscs", "Protein source and economic livelihoods from wild aquatic fisheries", "Tide generation through celestial forces; Ocean acidification mitigation; Oceanic trench formation"),
            ("Natural rubber harvested from Hevea brasiliensis", "Essential industrial elastomer supplied by biodiverse rainforest species", "Precipitation regulation by jet streams; Deep mantle magma recycling; Magnetic field stabilization"),
            ("Essential oils and aromatic compounds from lavender and sandalwood", "Fragrances, cosmetic ingredients, and antimicrobial extracts from plant species", "Runoff sediment retention; Ozone layer formation in stratosphere; Geothermal heating of aquifers")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand ecosystem service categories.** Provisioning services are the direct, tangible material outputs obtained from ecosystems (food, medicine, timber, fresh water, genetic resources).\n**Step 2: Connect to {item[0]}.** It represents {item[1]}.\n**Step 3: Match options.** The correct choice is {item[1]}."
        )
    })

    # Arch 3: Regulating & supporting ecosystem services
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which regulating or supporting ecological service is primarily performed by {0}?",
            "How does biodiversity maintain biosphere balance through the process in {0}?",
            "Identify the supporting or regulatory role of ecosystems demonstrated in {0}:",
            "What ecological stabilizing mechanism is illustrated by {0}?"
        ],
        'data': [
            ("Pollination by honeybees, bumblebees, bats, and butterflies", "Regulating service facilitating angiosperm fertilization and production of 75% of global food crops", "Provisioning service providing commercial plastic; Cultural service of mining minerals; Abiotic physical evaporation"),
            ("Photosynthesis in the Amazon rainforest and marine phytoplankton", "Supporting service generating atmospheric oxygen and sequestering massive amounts of carbon dioxide", "Extraction of fossil fuels; Industrial carbon mineralization; Mechanical filtration of salt"),
            ("Mangrove forests along tropical coastlines", "Regulating service buffering shores against storm surges, tsunamis, and soil erosion while trapping sediments", "Primary production of desert sand; Commercial deep-sea gravel extraction; Desalination by reverse osmosis"),
            ("Soil formation and nutrient cycling by earthworms and mycorrhizae", "Supporting service decomposing organic matter and recycling nitrogen, phosphorus, and carbon into bioavailable forms", "Rapid atmospheric nitrogen fixation by storms; Mechanical crushing of topsoil; Chemical synthesis of synthetic urea"),
            ("Wetlands and riparian reed beds", "Regulating service filtering toxic pollutants, trapping heavy metals, and purifying surface runoff", "Generation of nuclear radiation; Industrial production of chlorine; Acceleration of flash floods"),
            ("Forested catchment basins and hill vegetation", "Regulating service moderating microclimate, inducing precipitation, and preventing catastrophic landslides", "Direct manufacture of chemical fertilizers; Extraction of petroleum lubricants; Artificial cooling via refrigerants"),
            ("Biological pest control by ladybird beetles and insectivorous birds", "Regulating service suppressing pest populations naturally without synthetic chemical pesticides", "Synthetic organophosphate distribution; Soil sterilization with steam; Genetic cloning of insect monocultures"),
            ("Decomposition of leaf litter by saprophytic fungi and actinomycetes", "Supporting service mineralizing humus and maintaining continuous terrestrial soil fertility", "Direct extraction of mineral ores; Abiotic wind ablation of sand dunes; Mechanical compacting of clays"),
            ("Carbon sequestration by peatlands and oceanic blue carbon ecosystems", "Regulating service sequestering gigatons of carbon to mitigate greenhouse warming and climate change", "Industrial scrubbing with limestone; Subsurface coal combustion; Solar thermal steam generation"),
            ("Water cycle maintenance through forest evapotranspiration", "Regulating service recycling continental moisture and driving inland cloud formation and rainfall", "Mechanical cloud seeding with silver iodide; Groundwater depletion through tube wells; River dredging for barges")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Define regulating and supporting services.** Regulating services moderate natural processes (climate regulation, flood control, pollination). Supporting services maintain fundamental conditions (nutrient cycling, primary production, soil formation).\n**Step 2: Evaluate {item[0]}.** It executes {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is the correct answer."
        )
    })

    # Arch 4: Ecosystem stability, resilience, and Tilman's experiments
    archs.append({
        'diff': 'medium',
        'templates': [
            "How does species richness contribute to ecosystem stability as demonstrated in {0}?",
            "Which ecological principle explaining biodiversity and community stability relates to {0}?",
            "What conclusion regarding ecosystem resilience is drawn from {0}?",
            "In ecosystem ecology, how does {0} explain the relationship between diversity and productivity?"
        ],
        'data': [
            ("David Tilman's long-term outdoor prairie plot experiments", "Plots with greater species richness showed less year-to-year variation in total biomass and higher overall productivity", "Monoculture plots produced higher stability during severe drought; Species richness caused rapid biomass oscillations; Fewer species yielded higher nutrient retention"),
            ("Ecological resilience (buffering capacity)", "Ability of a biodiverse ecosystem to absorb environmental shocks, disturbances, and bounce back to equilibrium", "Fragility of diverse webs leading to catastrophic collapse; Resistance to any evolutionary change; Inability of communities to tolerate invasive species"),
            ("Complex multi-branched food webs vs simple linear chains", "Alternative feeding pathways prevent entire community collapse if one prey species suffers a population decline", "Strict dependence on single prey makes predators highly vulnerable; Simple linear chains survive disease outbreaks better; Elimination of top carnivore enhances overall chain stability"),
            ("Niche complementarity hypothesis", "Diverse coexisting species exploit distinct resources efficiently, minimizing interspecific competition and maximizing total resource utilization", "Complete competitive exclusion forces all competitors to extinction; Species share identical niches leading to resource depletion; Diverse species abandon their niches completely"),
            ("The 'Insurance Hypothesis' of biodiversity", "High biodiversity provides a functional buffer because redundant species can replace the ecological functions of lost species", "All species in an ecosystem perform completely identical functions simultaneously; A single dominant species is sufficient to guarantee long-term survival; Ecosystems with high diversity suffer catastrophic insurance failure"),
            ("Response to epidemic plant pathogens in polycultures", "High species diversity slows pathogen transmission because non-host plants physically block the spread of disease vectors", "Pathogens reproduce exponentially faster across mixed plant stands; Uniform genetic monocultures prevent pathogen evolution; Polycultures are universally infected by single strain viruses"),
            ("Drought resistance in diverse grassland communities", "Species with varying rooting depths and water-use strategies maintain canopy cover and reduce soil drying during dry spells", "Shallow-rooted single grasses conserve moisture better than deep roots; Dense species mixtures consume all water causing instant desertification; Only desert succulents survive in diverse temperate meadows"),
            ("Productivity-Diversity positive correlation", "Communities with higher plant species richness capture more sunlight and soil nutrients, achieving greater total primary productivity", "Monocultures consistently achieve higher net primary production than rainforests; Species richness leads to massive nutrient leakage and soil death; Diversity is inversely proportional to net photosynthetic output"),
            ("Ecosystem homeostasis", "Self-regulating dynamic equilibrium maintained through complex feedback loops among diverse biological populations", "External human intervention is strictly required to prevent food web collapse; Random demographic stochasticity without balance; Fixed non-dynamic biomass that never undergoes turnover"),
            ("Functional redundancy in decomposer communities", "Multiple bacterial and fungal species can perform cellulose breakdown, ensuring continuous nutrient cycling even if some species decline", "Only one unique bacterium on Earth can decompose organic matter; Loss of any microbe halts all global carbon decomposition; Decomposers do not contribute to ecosystem nutrient turnover")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand diversity-stability relationships.** Greater diversity generally enhances community stability, productivity, and resilience against disturbances (as shown by Tilman and the Insurance Hypothesis).\n**Step 2: Relate to {item[0]}.** The correct ecological understanding is {item[1]}.\n**Step 3: Select option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 5: Keystone species & trophic cascades
    archs.append({
        'diff': 'hard',
        'templates': [
            "What critical ecological role defines a keystone species as illustrated by {0}?",
            "How does the organism in {0} exert disproportionate influence on community structure?",
            "Identify the trophic mechanism or consequence of removing {0} from its ecosystem:",
            "In community ecology, which observation regarding {0} confirms its status as a keystone regulator?"
        ],
        'data': [
            ("Sea otters in North American Pacific kelp forest ecosystems", "Preying on herbivorous sea urchins prevents overgrazing, thereby sustaining giant kelp forests and hundreds of associated marine species", "Grazing directly on kelp fronds causing massive underwater deforestation; Filtering plankton without influencing benthic herbivore density; Acting as secondary decomposers on sandy marine beaches"),
            ("Robert Paine's Pisaster ochraceus (starfish) removal experiment", "Removal of the predatory starfish led to competitive dominance by mussels (Mytilus) and extinction of over 10 other invertebrate species", "Starfish removal resulted in a dramatic increase in overall benthic species diversity; Mussels completely disappeared due to lack of predation; Barnacles and algae expanded into a permanent climax forest"),
            ("Apex predators like Bengal Tigers in Indian forest ecosystems", "Regulating populations of large herbivores (deer, boar) prevents overgrazing and preserves forest regeneration and watershed hydrology", "Consuming primary canopy leaves to stimulate tree sprouting; Competing with herbivores for ground grasses; Eliminating all forest decomposers and insects"),
            ("Fig trees (Ficus species) in tropical rainforests", "Acting as a keystone resource during seasonal fruit scarcity by sustaining frugivorous birds, bats, and primates", "Poisoning understory vegetation to ensure sole canopy dominance; Suppressing fruit-eating bird populations through toxic latex; Flowering only once every century without ecological impact"),
            ("Beavers (Castor fiber) as ecosystem engineers", "Building dams that transform streams into wetlands, creating diverse habitats for fish, amphibians, waterbirds, and aquatic plants", "Preying on aquatic fish causing local freshwater extinctions; Deforesting entire landscapes without creating aquatic habitats; Digging underground burrows that desiccate river beds"),
            ("Definition of a Keystone Species", "A species whose impact on its community or ecosystem structure is disproportionately large relative to its modest abundance or biomass", "The most abundant species that constitutes the majority of total ecosystem biomass; Any invasive non-native species that disrupts an established food chain; A microscopic organism that cannot be observed without electron microscopy"),
            ("Trophic cascade triggered by wolf reintroduction in Yellowstone", "Predation and fear of wolves altered elk browsing behavior, enabling recovery of willows and asps, which revitalized beavers, songbirds, and stabilized riverbanks", "Elk populations multiplied exponentially causing complete riverbank erosion; Wolves eradicated all herbivore populations leading to park desertification; Vegetation died due to wolf territorial scent marking"),
            ("African elephants in savanna woodland ecosystems", "Knocking down mature acacia trees and creating pathways maintains open grassland mosaic preventing forest encroachment", "Overeating grass roots causing immediate barren sand dunes; Eliminating termite mounds and bird nesting cavities; Preventing savanna fires by consuming all combustible twigs"),
            ("Pollinating fruit bats (flying foxes) on oceanic islands", "Primary pollinators and seed dispersers for over 70% of island canopy trees, essential for island forest regeneration", "Herbivores consuming seeds preventing any seedling survival; Vectoring viral diseases that wipe out all island flora; Restricting tree reproduction to asexual cloning"),
            ("Loss of top sharks in coral reef ecosystems", "Release of meso-predators leads to depletion of herbivorous parrotfish, causing macroalgae to overgrow and kill living coral reefs", "Parrotfish populations explode and clear all ocean algae; Corals grow twice as fast in the complete absence of apex sharks; Reef water clarity improves due to absence of predatory swimming")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Define keystone species.** A keystone species exerts an impact disproportionately large relative to its abundance; its loss triggers a trophic cascade that destabilizes community diversity.\n**Step 2: Analyze {item[0]}.** The correct ecological outcome is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 6: Bioindicators and environmental sentinels
    archs.append({
        'diff': 'medium',
        'templates': [
            "Why is {0} classified as a sensitive bioindicator of environmental quality?",
            "Which environmental change or pollutant is uniquely signaled by {0}?",
            "How does monitoring {0} provide diagnostic data on ecosystem health?",
            "In ecotoxicology and environmental science, {0} serves as a sentinel for what condition?"
        ],
        'data': [
            ("Lichens (symbiosis of fungus and alga/cyanobacterium)", "Extreme sensitivity to sulfur dioxide (SO₂) air pollution; absent in polluted industrial urban areas", "High tolerance to heavy metal smog; flourishing exclusively in coal power plant fumes; resistance to acid rain"),
            ("Benthic macroinvertebrates (mayfly, stonefly, and caddisfly larvae)", "High oxygen requirement and low tolerance to organic pollution, indicating clean, well-oxygenated streams", "Flourishing in hypoxic sewage sludge; indicating high chemical pesticide runoff; feeding exclusively on microplastics"),
            ("Tubifex worms and Chironomus (bloodworm) larvae", "Tolerance to extremely low dissolved oxygen and organic enrichment, indicating severe sewage pollution in water bodies", "Intolerance to organic matter; requiring ultra-pure oligotrophic mountain springs; indicating absence of bacteria"),
            ("Amphibians (frogs, toads, and salamanders)", "Permeable skin and dual aquatic-terrestrial life cycle making them vulnerable to water pollutants, UV radiation, and chytrid fungus", "Thick impermeable keratinous scales shielding them from all chemical contaminants; Independent aquatic stage immune to acidic water; Exclusively terrestrial lifestyle unaffected by water toxicity"),
            ("Canary birds historically used in coal mines", "Higher metabolic rate and respiratory sensitivity to odorless carbon monoxide (CO) and toxic methane gases", "Immunity to all underground poisonous vapours; Ability to neutralize toxic coal dust in lungs; High tolerance to subterranean methane"),
            ("Coliform bacteria (Escherichia coli) in drinking water", "Indicator of fecal contamination and potential presence of pathogenic waterborne enteric microorganisms", "Proof of industrial heavy metal contamination; Indicator of high dissolved oxygen in mineral springs; Non-biological indicator of radioactive isotopes"),
            ("Corals and zooxanthellae symbiosis", "Bleaching response to elevated sea surface temperatures and marine heatwaves, indicating oceanic thermal stress", "Thriving under high water temperatures; indicating industrial oil tanker spillage; blooming during severe ocean acidification"),
            ("Diatoms (siliceous microalgae) in lake sediments", "Specific species assemblages indicate precise pH, salinity, and nutrient (eutrophication) status across ecological history", "Uniform growth regardless of water chemistry; Indicator strictly limited to thermal thermal volcanic springs; Incapable of fossilizing in lake beds"),
            ("House sparrows and insectivorous passerine birds", "Decline in urban populations indicates loss of insect food, excessive pesticide use, and habitat homogenization", "Booming populations in response to intense pesticide spraying; Immunity to electromagnetic radiation and food loss; Direct indicators of subterranean groundwater depletion"),
            ("Vultures (Gyps species) in South Asia", "Catastrophic population crash alerted scientists to lethal veterinary diclofenac residues in livestock carcasses", "Indicator of expanding tropical scrub forests; Direct consumer of live domestic cattle; Resistant to all synthetic anti-inflammatory drugs")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand bioindicators.** Bioindicators are species whose presence, absence, abundance, or physiological state reflects the environmental health or level of specific pollutants in an ecosystem.\n**Step 2: Inspect {item[0]}.** It functions as {item[1]}.\n**Step 3: Match options.** Hence, {item[1]} is the correct answer."
        )
    })

    # Arch 7: Agricultural biodiversity & genetic erosion
    archs.append({
        'diff': 'hard',
        'templates': [
            "What significant ecological risk or agricultural consequence is associated with {0}?",
            "How does {0} demonstrate the vital importance of preserving agricultural genetic diversity?",
            "Identify the agricultural danger or genetic vulnerability highlighted by {0}:",
            "In agronomy and conservation genetics, what principle is established by {0}?"
        ],
        'data': [
            ("The Irish Potato Famine of 1845–1852", "Extreme vulnerability of widespread genetic monoculture (Lumper potato clone) to a single pathogen (Phytophthora infestans)", "Benefits of high polyculture diversity resisting blights; Demonstration that cloning guarantees permanent crop health; Failure of wild Andean potato varieties to resist blight"),
            ("Widespread adoption of high-yielding monocultures during the Green Revolution", "Narrowing of the genetic base (genetic erosion) replacing thousands of resilient traditional landraces with uniform cultivars", "Permanent eradication of all crop pests and diseases; Preservation of all ancient ancestral cereal landraces; Complete stabilization of wild crop relatives"),
            ("Preservation of Crop Wild Relatives (CWRs)", "Providing ancestral gene pools containing natural alleles for drought tolerance, disease resistance, and pest immunity", "Replacing commercial high-yield seeds with low-nutrition wild weeds; Eliminating the necessity of agricultural seed banks; Breeding non-edible crops for urban lawns"),
            ("Southern Corn Leaf Blight epidemic in the USA (1970)", "Over 85% of US maize carried the identical Texas male-sterile (Tms) cytoplasm, making entire national yields susceptible to Helminthosporium maydis", "Demonstration that cytoplasmic male sterility prevents fungal infections; Proof that diverse hybrid varieties fail in warm climates; Total immunity of monoculture corn to all leaf blights"),
            ("The Svalbard Global Seed Vault ('Doomsday Vault')", "Secure underground gene bank preserving duplicate backups of crop seeds from around the world against catastrophic loss", "Commercial trading warehouse for genetically modified corporate seeds; Facility designed to grow fresh vegetables for Arctic research; Nuclear disposal site for irradiated plant tissue"),
            ("Traditional intercropping / polyculture farming", "Planting diverse crop species together disrupts pest migration, enhances soil nutrient utilization, and ensures harvest stability", "Guarantees complete soil nutrient exhaustion within one season; Increases vulnerability to fungal leaf rusts; Decreases overall land equivalent ratio below monocultures"),
            ("Genetic vulnerability in Cavendish banana clone", "Global commercial reliance on a single sterile seedless clone makes production vulnerable to Tropical Race 4 (TR4) Panama disease", "Natural immunity of Cavendish bananas to all fungal Fusarium wilt strains; High genetic diversity generated through sexual seed breeding; Demonstration that clonal propagation enhances pathogen resistance"),
            ("Wild rice species Oryza nivara", "Supplied a critical gene for resistance against the grassy stunt virus to modern commercial cultivated rice (Oryza sativa)", "Wiped out Asian rice paddies as an aggressive agricultural weed; Caused sterility in hybrid rice crosses; Lacked any functional agricultural resistance genes"),
            ("Bioprospecting in indigenous medicinal plants", "Systematic exploration of wild biological resources for commercially valuable genetic traits and biochemical compounds", "Unregulated mass deforestation of ancient forests; Replacing modern pharmaceuticals with toxic crude extracts; Banning scientific patenting of all synthesized molecules"),
            ("In-situ conservation of agro-biodiversity by traditional farmers", "Active on-farm cultivation and dynamic selection of heirloom landraces under evolving local climate pressures", "Freezing seed germplasm in liquid nitrogen for centuries; Irradiating seeds with gamma rays to induce lethal mutations; Complete prohibition of planting traditional local varieties")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand agricultural biodiversity.** Genetic diversity within crops and wild relatives protects food security against epidemics and climate extremes. Monocultures are genetically vulnerable.\n**Step 2: Relate to {item[0]}.** The correct insight is {item[1]}.\n**Step 3: Select option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 8: Economic, cultural, and intrinsic values
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which category of biodiversity value is represented by {0}?",
            "How is the importance of biodiversity expressed through {0}?",
            "Identify the valuation framework that accounts for the benefits of {0}:",
            "In conservation ethics and environmental economics, {0} exemplifies what value?"
        ],
        'data': [
            ("Sacred Groves (e.g., in Khasi and Jaintia Hills, Western Ghats, Aravalli Hills)", "Cultural, religious, and traditional ethical conservation preserving pristine climax biodiversity from human exploitation", "Pure commercial timber logging concessions; Industrial agro-forestry monocultures; Urban botanical entertainment parks"),
            ("Ecotourism in national parks like Kaziranga and Jim Corbett", "Non-consumptive economic value generating revenue and local livelihoods through wildlife observation and recreation", "Consumptive harvesting of endangered species parts; Commercial clear-cutting of protected forests; Heavy mineral open-cast mining inside reserves"),
            ("Intrinsic value of species", "Ethical perspective asserting that every species has an inherent right to exist regardless of its economic utility to humans", "Market price of an organism's pelt or meat; Replacement cost of an engineered ecosystem service; Financial penalty imposed for illegal poaching"),
            ("Option value of biodiversity", "Economic potential and future unforeseen benefits of unknown species for medicine, agriculture, or industry", "Immediate scrap value of deforested timber; Direct revenue earned from tourist park entry tickets; Insurance compensation paid for wildfire damages"),
            ("Existence value of biodiversity", "Satisfaction and moral contentment humans derive from knowing that remote wilderness and wild species continue to exist", "Direct commercial yield from marine fish landings; Cost savings achieved through natural wetland water filtration; Profit generated from bioprospecting patents"),
            ("Paul Ehrlich's 'Rivet Popper Hypothesis'", "Analogy comparing an ecosystem to an airplane: losing a few rivets (minor species) may seem harmless, but losing critical rivets (keystone species) leads to catastrophic crash", "Demonstration that all species can be removed without affecting ecosystem flight; Proof that ecosystems are completely indestructible regardless of extinctions; Argument that only cockpit pilots (humans) matter in an aircraft"),
            ("Traditional ecological knowledge (TEK) of indigenous communities", "Generational understanding of local species, seasonal phenology, and sustainable harvesting practices passed through cultural traditions", "Modern laboratory gene-editing algorithms; Commercial marketing strategies for multinational agribusiness; Synthetic pesticide spraying schedules"),
            ("Biophilia hypothesis (E. O. Wilson)", "Innate human tendency and psychological affinity to connect with nature, other living organisms, and biodiverse landscapes", "Aversion and fear of wild natural wilderness; Human economic motivation to pave over all green areas; Preference for sterile concrete urban architecture"),
            ("Consumptive use value", "Direct value of biodiversity products harvested and consumed locally without passing through commercial retail markets (e.g., wild firewood, bushmeat, wild herbs)", "Corporate revenue from multinational patent licensing; Entrance fees collected at municipal zoological parks; International bond trading on carbon credits"),
            ("Productive use value", "Commercial value of biological resources that are harvested, industrially processed, and sold in national and global trade markets (e.g., pulp paper, leather, pharmaceuticals)", "Subsistence gathering of medicinal leaves by a forest dweller; Moral joy of reading wildlife poetry; Pure aesthetic appreciation of sunset over a wetland")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand biodiversity values.** Biodiversity holds direct economic (consumptive/productive), indirect ecological (services, option, existence), cultural, and intrinsic values.\n**Step 2: Examine {item[0]}.** It represents {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    return generate_vault_questions('CBSE-9-SCIE-12-12.3.1', 'Significance of biodiversity in ecosystems', archs)

# -------------------------------------------------------------
# SUBTOPIC 12.3.2: Threats to biodiversity and national/global conservation measures
# -------------------------------------------------------------
def gen_12_3_2():
    archs = []

    # Arch 1: The "Evil Quartet" (Primary threats)
    archs.append({
        'diff': 'easy',
        'templates': [
            "Which primary driver of species extinction among the 'Evil Quartet' is illustrated in {0}?",
            "Identify the major threat to biodiversity responsible for the situation described in {0}:",
            "According to conservation biology, {0} is a direct consequence of which component of the 'Evil Quartet'?",
            "In anthropogenic biodiversity loss, {0} represents which extinction driver?"
        ],
        'data': [
            ("Clearing of tropical rainforests in the Amazon for soybean cultivation and cattle ranching", "Habitat loss and fragmentation (the single most important cause of species extinction)", "Overexploitation by trophy hunters; Co-extinction with specialized pollinators; Colonization by extraterrestrial predators"),
            ("Extinction of the Passenger Pigeon and Dodo due to excessive human hunting and harvesting", "Overexploitation (when human resource need turns to greed, outstripping natural replenishment)", "Natural background speciation; Habitat fragmentation by geological faulting; Co-extinction caused by plant viruses"),
            ("Devastating spread of Water Hyacinth (Eichhornia crassipes) choking Indian freshwater wetlands", "Alien (invasive) species invasion (exotic species multiplying uncontrollably and outcompeting native taxa)", "Habitat creation through silviculture; Co-extinction of benthic molluscs; Overharvesting of weed leaves"),
            ("Extinction of a specialized parasite when its obligate host fish species goes extinct", "Co-extinction (when the extinction of one species inevitably leads to the demise of associated dependent species)", "Overexploitation of parasitic worms; Direct habitat deforestation; Introduction of predatory terrestrial mammals"),
            ("Fragmentation of contiguous forests into small isolated patches by highway and railway corridors", "Habitat fragmentation causing edge effects and isolating populations of large mammals with wide home ranges", "Overexploitation by sport fishing; Co-extinction of deep-sea corals; Alien invasion of oceanic islands"),
            ("Introduction of the Nile perch into Lake Victoria causing extinction of over 200 endemic cichlid fish species", "Alien (invasive) species invasion decimating native fauna through aggressive predation and competition", "Overexploitation of phytoplankton; Habitat destruction by continental drift; Co-extinction of mangrove forests"),
            ("Extinction of Stellar's Sea Cow within 27 years of discovery due to relentless hunting for meat and fur", "Overexploitation driven by excessive human commercial hunting", "Loss of freshwater wetlands; Co-extinction with arctic mosses; Invasive alien weed smothering shores"),
            ("Obligate mutualism between Yucca moth and Yucca plant where loss of one leads to extinction of the other", "Co-extinction in mutualistic interactions where neither partner can complete its life cycle alone", "Invasive weed overgrowth; Direct habitat burning; Overexploitation for commercial textile silk"),
            ("Replacement of native forest undergrowth by Parthenium (carrot grass) and Lantana camara in India", "Alien (invasive) species invasion suppressing native flora through allelopathy and aggressive colonization", "Overexploitation of native wildflowers; Co-extinction with cave-dwelling bats; Creation of deep river canyons"),
            ("Conversion of pristine mangrove wetlands into commercial shrimp aquaculture farms", "Habitat destruction and degradation leading to catastrophic loss of nursery grounds for marine species", "Overexploitation by scientific specimen collection; Co-extinction of freshwater carps; Natural succession toward alpine tundra")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Identify the 'Evil Quartet'.** The four major drivers of biodiversity loss are: (1) Habitat loss and fragmentation, (2) Overexploitation, (3) Alien species invasion, and (4) Co-extinction.\n**Step 2: Evaluate {item[0]}.** The applicable threat is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 2: Habitat loss, fragmentation & edge effects
    archs.append({
        'diff': 'medium',
        'templates': [
            "What ecological impact or population consequence directly arises from {0}?",
            "How does {0} accelerate local extinction and biodiversity decline?",
            "In landscape ecology, what problem is specifically caused by {0}?",
            "Identify the structural consequence of habitat alteration demonstrated in {0}:"
        ],
        'data': [
            ("Division of continuous wildlife habitats by linear infrastructure (roads, railways, power lines)", "Population fragmentation, disruption of migratory routes, elevated mortality from vehicle collisions, and genetic isolation", "Immediate doubling of genetic diversity; Rapid evolution of giant body size; Expansion of core wilderness zones"),
            ("Increased edge-to-interior ratio in forest fragments (Edge Effect)", "Exposure of interior species to altered microclimate (higher winds, temperature fluctuations) and invasion by edge predators and weeds", "Complete stabilization of interior moisture; Protection of forest interior from all external predators; Eradication of all surrounding invasive weeds"),
            ("Reduction of Amazon rainforest cover from 14% to less than 6% of Earth's land surface", "Loss of global 'lungs of the planet', release of stored carbon, and extinction of thousands of undiscovered endemic species", "Permanent global cooling and ice sheet expansion; Complete elimination of all worldwide wildfires; Massive increase in global terrestrial biodiversity"),
            ("Isolation of small isolated tiger populations in fragmented forest reserves", "Loss of gene flow leading to severe inbreeding depression, reduced fertility, and elevated vulnerability to stochastic disease outbreaks", "Explosive increase in reproductive fitness; Immunity to viral feline distemper; Emergence of new distinct sub-species within months"),
            ("Destruction of tropical coral reefs by destructive dynamite fishing and bottom trawling", "Physical obliteration of 3D architectural habitat complexity, eliminating breeding and feeding grounds for thousands of marine species", "Rapid natural regeneration of massive coral colonies; Expansion of commercial pelagic tuna breeding; Immediate purification of ocean seawater"),
            ("Establishment of biological corridors connecting isolated protected areas", "Mitigation of fragmentation by facilitating animal movement, gene flow, and seasonal migration between sub-populations", "Permanent isolation of animal populations; Promotion of edge effect across the entire core area; Complete blockage of mammalian dispersal"),
            ("Forest fire and subsequent cattle grazing in tropical seasonal forests", "Destruction of seed banks in leaf litter, soil compaction, and prevention of natural tree regeneration", "Immediate acceleration of primary succession; Enrichment of diverse indigenous understory shrubs; Eradication of grass fires for centuries"),
            ("Draining of natural wetlands for real estate development", "Loss of natural flood detention basins, decline of migratory waterfowl, and destruction of groundwater recharge mechanisms", "Dramatic reduction in urban flood risks; Immediate elevation of regional water tables; Proliferation of rare migratory pelicans"),
            ("Clear-cutting of mangroves along coastal delta areas", "Loss of coastal storm protection, accelerated tidal erosion, and collapse of coastal estuarine nurseries for fish and prawns", "Stabilization of river delta mudflats; Formation of protective barrier dunes; Complete prevention of hurricane damage"),
            ("Urban sprawl encroaching on peripheral wildlife habitats", "Escalation of human-wildlife conflict, roadkills, garbage foraging, and transmission of zoonotic pathogens to domestic pets", "Peaceful integration of wild carnivores into cities; Total elimination of human-animal competition; Natural expansion of apex predator home ranges")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand habitat loss and fragmentation.** Breaking large habitats into small fragments increases edge effects, disrupts migration, isolates populations, and accelerates extinction.\n**Step 2: Inspect {item[0]}.** The correct impact is {item[1]}.\n**Step 3: Match options.** Thus, {item[1]} is correct."
        )
    })

    # Arch 3: Invasive alien species
    archs.append({
        'diff': 'medium',
        'templates': [
            "Why is the introduced species {0} considered a destructive invasive alien threat?",
            "Which ecological disruption is directly caused by the invasion of {0}?",
            "How has the introduction of {0} impacted indigenous biodiversity?",
            "In invasion biology, what threat is specifically attributed to {0}?"
        ],
        'data': [
            ("Water Hyacinth (Eichhornia crassipes / 'Terror of Bengal')", "Forms dense impenetrable mats over water surfaces, blocking sunlight and depleting dissolved oxygen, suffocating native aquatic flora and fauna", "Acts as an oxygen generator restoring degraded water bodies; Provides ideal food for indigenous herbivorous fishes; Enhances commercial inland boat navigation"),
            ("Parthenium hysterophorus (Carrot grass / Congress grass)", "Aggressive agricultural weed producing allelopathic toxins that inhibit crop growth and pollen that causes severe respiratory allergies in humans", "Provides rich protein fodder for dairy cattle; Restores nitrogen in degraded drylands naturally; Attracts beneficial honeybees without allergic effects"),
            ("Lantana camara", "Forms dense prickly impenetrable thickets in forest understories, preventing tree regeneration and poisoning grazing cattle with triterpenoid toxins", "Nourishes native deer herds with edible foliage; Encourages growth of native saplings under its canopy; Disappears naturally after one growing season"),
            ("Nile Perch (Lates niloticus) in Lake Victoria", "Massive apex predatory fish that decimated more than 200 endemic cichlid fish species through relentless predation", "Formed peaceful shoals with endemic haplochromine cichlids; Fed exclusively on floating lake weeds; Restored historical cichlid species diversity"),
            ("African Catfish (Clarias gariepinus) introduced for aquaculture", "Aggressively predatory invasive catfish that escaped into Indian rivers, threatening indigenous catfish species with extinction", "Feeds strictly on green algae sparing all native fauna; Incapable of surviving in natural river currents; Displaces only non-native aquaculture carps"),
            ("Brown Tree Snake (Boiga irregularis) introduced to Guam", "Accidentally introduced snake that eradicated virtually all native forest bird and fruit bat species on the island", "Controlled rodent pests without harming any native birds; Flourished only in captive zoos; Failed to establish breeding populations in the wild"),
            ("Prosopis juliflora (Mesquite / Vilayati Kikar)", "Deep tap roots exhaust groundwater and prolific thorns and seed pods suppress native arid and semi-arid vegetation in India", "Enriches shallow water tables through transpiration; Nurtures endemic desert acacia saplings; Loses all seeds to granivorous desert birds"),
            ("Domestic and feral cats introduced to oceanic islands", "Predation on ground-nesting birds, reptiles, and small mammals unadapted to mammalian carnivores, causing numerous island extinctions", "Protecting ground-nesting seabirds from rodent predation; Consuming only marine fish washed onto beaches; Exhibiting peaceful mutualism with flightless rails"),
            ("Cane Toad (Rhinella marina) introduced to Australia", "Poisonous parotoid glands kill native predatory monitors, snakes, and quolls that attempt to consume it, while outcompeting native amphibians", "Successfully eradicated sugarcane beetle grubs without ecological damage; Provided safe non-toxic prey for native marsupials; Died out quickly due to arid Australian climate"),
            ("Zebra Mussel (Dreissena polymorpha) in North American Great Lakes", "Fouls underwater water intake pipes and encrusts native unionid mussels, filtering phytoplankton so intensely that food webs collapse", "Cleans lake water without impacting any native food chain; Serves as an ideal host for native freshwater pearls; Dissolves toxic industrial chemicals completely")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand biological invasions.** Alien species, when introduced intentionally or accidentally, can turn invasive, outcompeting, predating, or poisoning native species and collapsing food webs.\n**Step 2: Relate to {item[0]}.** The correct impact is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 4: Biomagnification, pollution & climate threats
    archs.append({
        'diff': 'hard',
        'templates': [
            "Which ecotoxicological mechanism or climate threat is correctly described in {0}?",
            "How does the environmental factor in {0} induce severe biodiversity decline?",
            "Identify the biochemical or physiological hazard detailed in {0}:",
            "In global change biology, what phenomenon is demonstrated by {0}?"
        ],
        'data': [
            ("Biomagnification of DDT in aquatic food chains", "Concentration of non-biodegradable fat-soluble DDT increases at each successive trophic level, causing eggshell thinning and population crashes in raptorial birds", "DDT rapidly degrades into harmless water-soluble sugars in algae; Apex fish-eating birds excrete DDT completely without accumulation; DDT strengthens calcium deposition in avian eggshells"),
            ("Eutrophication of lakes and water bodies", "Excessive nutrient enrichment (nitrates and phosphates from fertilizers/sewage) triggers algal blooms, whose decomposition by bacteria exhausts dissolved oxygen, causing massive fish kills", "High dissolved oxygen levels leading to proliferation of deep-water fishes; Algae consume all toxic chemicals and clarify water; Enrichment permanently purifies drinking water aquifers"),
            ("Ocean acidification due to rising atmospheric CO₂", "Dissolution of CO₂ forms carbonic acid, lowering ocean pH and reducing carbonate ion availability, which impairs shell and skeleton formation in corals and calcifying molluscs", "Carbonic acid strengthens calcium carbonate shells; Acidification increases coral reef growth rates worldwide; Elevated pH makes ocean waters more alkaline"),
            ("Coral bleaching induced by marine heatwaves", "Prolonged elevated sea temperatures cause corals to expel their symbiotic photosynthetic zooxanthellae, resulting in starvation, white skeleton exposure, and mass coral death", "Warmer waters stimulate zooxanthellae to produce triple the nutrient output; Bleached corals develop immunity to disease and grow faster; Corals absorb excess heat and convert it into bioluminescence"),
            ("Bioaccumulation of methylmercury in aquatic carnivores", "Inorganic mercury is methylated by anaerobic bacteria and bioaccumulates in apex predatory fishes (tuna, swordfish, sharks), posing neurotoxic hazards to wildlife and humans", "Mercury evaporates harmlessly into the atmosphere from fish gills; Anaerobic microbes neutralize all heavy metals into nutrients; Methylmercury is degraded into harmless sodium chloride in blood"),
            ("Veterinary diclofenac toxicity in Indian vultures", "Vultures consuming cattle carcasses treated with the non-steroidal anti-inflammatory drug diclofenac suffered acute renal failure, visceral gout, and 99% population decline", "Diclofenac acted as a beneficial vitamin boosting vulture reproductive rates; Vultures developed genetic resistance and flourished around feedlots; The drug was completely metabolized without entering avian kidneys"),
            ("Plastic and microplastic pollution in marine environments", "Ingestion of microplastics by marine organisms causes physical gut blockages, pseudo-satiation, starvation, and exposure to toxic chemical plasticizers", "Microplastics serve as nutritious high-calorie food for baleen whales; Marine animals completely digest synthetic polymers with specialized enzymes; Plastics dissolve into harmless mineral salts within weeks"),
            ("Thermal pollution from industrial and power plant cooling water", "Discharge of heated water reduces the solubility of dissolved oxygen and induces thermal shock, altering enzyme function and breeding cycles of aquatic species", "Elevated water temperatures drastically increase dissolved oxygen solubility; Warm water prevents any fungal or bacterial disease in fishes; Fishes thrive with unlimited stamina in boiling cooling canals"),
            ("Acid rain (deposition of sulfuric and nitric acids)", "Leaches toxic aluminum from soils into waterways and directly damages leaf cuticles, causing forest dieback and the acidification of lakes beyond aquatic organism tolerance", "Neutralizes soil alkalinity and promotes vigorous tree root growth; Enriches lake ecosystems with bioavailable plant nutrients; Protects marble monuments and aquatic life from degradation"),
            ("Phenological mismatch caused by climate change", "Warming temperatures cause insect emergence to advance in spring while migratory insectivorous birds arrive on unchanged photoperiod schedules, starving chicks of peak food", "Migratory birds and insect prey maintain perfectly synchronized shifts across all seasons; Insects delay emergence until birds complete their migration; Warming halts all animal reproductive and nesting cycles")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand ecotoxicology and climate impacts.** Pollutants like DDT and heavy metals biomagnify up food chains. Climate change triggers ocean acidification, coral bleaching, and phenological mismatch.\n**Step 2: Inspect {item[0]}.** The correct explanation is {item[1]}.\n**Step 3: Select option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 5: IUCN Red List categories & criteria
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which definition or criterion precisely corresponds to the IUCN Red List status {0}?",
            "How does the International Union for Conservation of Nature (IUCN) classify a species under {0}?",
            "Identify the official threat level or criteria representing {0} in the IUCN Red Data Book:",
            "In conservation assessment, what does the designation {0} signify?"
        ],
        'data': [
            ("Extinct (EX)", "No reasonable doubt that the last individual of the species has died anywhere on Earth (e.g., Dodo, Passenger Pigeon)", "Species survives only in captivity or cultivation; Population reduced by 10% over fifty years; Species recorded in low numbers in remote habitats"),
            ("Extinct in the Wild (EW)", "Survives only in cultivation, in captivity, or as a naturalized population well outside the past range (e.g., Alagoas Curassow)", "Completely eliminated from both wild habitats and all global zoological collections; Widely distributed in pristine wilderness but declining in cities; Abundant in local private gardens without documentation"),
            ("Critically Endangered (CR)", "Facing an extremely high risk of extinction in the wild in the immediate future based on catastrophic population reduction or tiny range (e.g., Great Indian Bustard, Gharial)", "Moderately declining population with no immediate risk of extinction; Common species facing seasonal habitat shifts; Species not evaluated due to data deficiency"),
            ("Endangered (EN)", "Facing a very high risk of extinction in the wild in the near future (e.g., Bengal Tiger, Asian Elephant, Snow Leopard)", "Fully secure species that has achieved maximum carrying capacity; Species extinct everywhere on Earth; Captive-bred population released into gardens"),
            ("Vulnerable (VU)", "Facing a high risk of extinction in the wild in the medium-term future (e.g., One-horned Rhinoceros, Olive Ridley Sea Turtle)", "Species with zero population decline over centuries; Ubiquitous weed widespread across all continents; Taxon evaluated and found completely immune to threats"),
            ("Near Threatened (NT)", "Does not currently qualify for Critically Endangered, Endangered, or Vulnerable, but is close to qualifying or likely to qualify in the near future", "Species facing immediate global extinction tomorrow; Fully domesticated farm animal; Unstudied marine microorganism"),
            ("Least Concern (LC)", "Widespread and abundant taxon evaluated and determined not to qualify for any threat category (e.g., House Crow, Common Myna)", "Highest priority species facing imminent total extinction; Confined to a single mountaintop with under 5 individuals; Species surviving solely in deep-freeze seed banks"),
            ("Data Deficient (DD)", "Inadequate information to make a direct or indirect assessment of extinction risk based on distribution or population status", "Official confirmation that the species is definitely extinct; Complete genome sequenced confirming safety; Status indicating infinite wild abundance"),
            ("IUCN Red Data Book", "Comprehensive international catalogue documenting the global conservation status, extinction risk, and threats to biological species", "Trade register recording prices of commercial wildlife pelts; Legal manual listing permitted hunting quotas; Botanical book cataloguing synthetic crop pesticides"),
            ("Endemic Species", "A species naturally restricted and confined exclusively to a particular geographic region or locality and found nowhere else on Earth", "A cosmopolitan weed thriving equally across all continents; An introduced invasive organism displacing native fauna; A cultivated hybrid cereal grown in commercial farms")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand IUCN Red List Categories.** IUCN categorizes taxa into: Extinct (EX), Extinct in the Wild (EW), Critically Endangered (CR), Endangered (EN), Vulnerable (VU), Near Threatened (NT), and Least Concern (LC).\n**Step 2: Relate to {item[0]}.** The correct definition is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 6: In-situ conservation (National Parks, Sanctuaries, Biosphere Reserves)
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which characteristic, legal regulation, or zonation feature defines {0}?",
            "How is biodiversity managed and protected within {0}?",
            "Identify the distinctive regulatory framework or design of {0}:",
            "In in-situ conservation biology, what distinguishes {0} from other protected area models?"
        ],
        'data': [
            ("In-situ conservation (On-site conservation)", "Protecting endangered plants and animals in their natural, native habitats and ecosystems (e.g., National Parks, Biosphere Reserves)", "Removing species from their wild habitats to breed them in human enclosures; Preserving frozen germplasm in liquid nitrogen tanks; Cultivating single clonal varieties in greenhouse labs"),
            ("National Park (e.g., Jim Corbett, Kaziranga, Ranthambore)", "Strictly protected area dedicated to wildlife conservation where human settlements, private ownership, and grazing are strictly prohibited by law", "Multiple human villages allowed to extract timber freely; Commercial open-pit mining encouraged; Reserved exclusively for commercial agriculture"),
            ("Wildlife Sanctuary (e.g., Bharatpur / Keoladeo, Periyar)", "Protected area focused on conserving specific animal species where regulated human activities like minor forest produce gathering and grazing may be permitted", "Total prohibition of any scientific research; Open unhindered commercial clear-cutting; Exclusive government-run zoo with cages"),
            ("Biosphere Reserve - Core Zone", "Legally protected inviolate pristine sanctuary zone where no human activity or exploitation is permitted", "Zone where urban cities and industries are developed; Area reserved for commercial timber logging; Public tourist amusement zone with rollercoasters"),
            ("Biosphere Reserve - Buffer Zone", "Area surrounding the core zone where managed, non-destructive research, education, and limited tourism activities are accommodated", "Inviolate zone where even researchers cannot enter; Heavy industrial zone with chemical refineries; Open commercial deforestation belt"),
            ("Biosphere Reserve - Transition Zone (Manipulation Zone)", "Outermost zone where local communities, conservation managers, and economic activities cooperate for sustainable resource use", "Strictly barred to all human beings; Radioactive waste disposal region; Subsurface deep geological mining zone"),
            ("Man and the Biosphere (MAB) Programme", "UNESCO intergovernmental scientific programme launched in 1971 to promote sustainable balance between conservation and development", "Commercial global trade agreement for shipping wild animals; Military treaty protecting naval border coasts; Chemical initiative developing synthetic pesticides"),
            ("Biodiversity Hotspots (Norman Myers)", "Regions characterized by exceptionally high levels of species richness, high endemism, and under severe threat of habitat loss (at least 70% primary habitat lost)", "Pristine uninhabited polar ice sheets with zero human impact; Degraded agricultural zones with no native species; Urban metropolitan landscapes with high human population"),
            ("Indian Biodiversity Hotspots", "Himalaya, Western Ghats & Sri Lanka, Indo-Burma, and Sundaland (Nicobar Islands)", "Thar Desert, Indo-Gangetic Plains, and Deccan Plateau; Rann of Kutch, Central India, and Eastern Ghats; Siachen Glacier and Delhi Ridge"),
            ("Sacred Groves of India", "Pristine forest patches communally protected by indigenous tribes through religious customs and taboos, acting as evolutionary refugia", "Government-owned commercial eucalyptus plantations; City botanical gardens with entry tickets; Deforested hill slopes managed for terraced rice farming")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand In-situ conservation.** In-situ protects organisms in their natural habitat. National parks allow no human exploitation; Wildlife sanctuaries allow limited regulated activities; Biosphere Reserves have Core, Buffer, and Transition zones.\n**Step 2: Inspect {item[0]}.** The correct statement is {item[1]}.\n**Step 3: Deduce option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 7: Ex-situ conservation (Botanical gardens, Zoos, Cryopreservation)
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which technique or institution exemplifies {0}?",
            "How does {0} contribute to the preservation of endangered species?",
            "Identify the scientific protocol or facility characteristic of {0}:",
            "In biodiversity management, what defines the approach in {0}?"
        ],
        'data': [
            ("Ex-situ conservation (Off-site conservation)", "Protecting and maintaining endangered species outside their natural habitats in human-managed facilities (e.g., Zoos, Botanical Gardens, Seed Banks)", "Declaring an entire pristine rainforest as a national park; Establishing community sacred groves around shrines; Protecting marine coral barriers in open oceans"),
            ("Zoological Parks (Modern Zoos)", "Facilities where endangered animals are kept under professional care for scientific research, public education, and coordinated captive breeding programmes", "Commercial hunting ranches where tourists shoot game; Circuses training wild animals for entertainment; Wholesale livestock slaughterhouses"),
            ("Botanical Gardens (e.g., Kew, Indian Botanical Garden Shibpur)", "Maintained living collections of diverse, rare, and economically important plant species for research, taxonomy, and germplasm preservation", "Agricultural fields growing hybrid wheat crops; Indoor hydroponic commercial lettuce greenhouses; Timber processing lumber yards"),
            ("Cryopreservation of gametes and embryos", "Preservation of viable living biological tissues, gametes, and embryos at ultra-low temperatures (-196 °C in liquid nitrogen) for indefinite storage", "Drying seeds in direct sunlight at 40 °C; Storing roots in formalin at room temperature; Preserving herbarium sheets in wooden cabinets"),
            ("Seed Banks (e.g., Millennium Seed Bank, Svalbard)", "Facilities where seeds of diverse plant species and wild crop relatives are dried and stored at -20 °C under low humidity to preserve genetic viability", "Commercial grain silos storing wheat flour for grocery stores; Garden nurseries selling hybrid seedlings; Fertilizer blending manufacturing units"),
            ("In-vitro tissue culture (Micropropagation)", "Aseptic clonal propagation of endangered plant species from tiny shoot tips or explants on nutrient media in laboratory culture vessels", "Growing seeds directly in natural unsterilized forest soil; Planting broad-acre open timber cuttings; Grafting fruit trees in outdoor orchards"),
            ("Captive Breeding and Reintroduction (e.g., California Condor, Pygmy Hog)", "Breeding severely endangered wild species in secure facilities followed by reintroduction into restored native wild habitats", "Breeding animals permanently for pet trade sales; Domesticating wild animals into draft livestock; Keeping animals isolated without ever releasing them into the wild"),
            ("Pollen Banks", "Storage of viable pollen grains under low temperature and desiccated conditions for assisted pollination and plant breeding programmes", "Atmospheric monitoring stations tracking allergy pollen; Honeybee hives collecting raw beeswax; Commercial perfume extraction refineries"),
            ("Gene Banks / Germplasm Banks", "Comprehensive biorepositories storing genetic material (seeds, cuttings, DNA, frozen semen) across thousands of cultivars and wild relatives", "Offices issuing intellectual property patents; Financial banks investing in corporate agribusiness; Municipal water reservoirs"),
            ("Wildlife Safaris / Safari Parks", "Spacious open-air enclosures where wild animals roam in semi-natural conditions while human visitors traverse along protected vehicle tracks", "Traditional Victorian iron cages measuring two square meters; Indoor concrete basements without natural sunlight; Deep ocean trawler nets")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand Ex-situ conservation.** Ex-situ involves preserving threatened species outside their natural habitats (zoos, botanical gardens, cryopreservation in liquid nitrogen at -196 °C, seed banks).\n**Step 2: Evaluate {item[0]}.** The correct concept is {item[1]}.\n**Step 3: Match options.** Hence, {item[1]} is correct."
        )
    })

    # Arch 8: Legal frameworks, conventions & national projects
    archs.append({
        'diff': 'hard',
        'templates': [
            "Which mandate, founding year, or operational objective belongs to {0}?",
            "What significant conservation achievement or legal provision was established by {0}?",
            "Identify the key international convention or Indian legal statute described in {0}:",
            "In environmental policy and conservation history, {0} is recognized for which outcome?"
        ],
        'data': [
            ("Wildlife (Protection) Act, 1972 (India)", "Landmark national legislation providing legal protection to wild animals, birds, and plants, establishing national parks, and outlawing hunting", "Act facilitating commercial export of tiger pelts; Statute promoting deforestation for railway construction; Law legalizing blast fishing along marine coasts"),
            ("Project Tiger (launched in 1973 in India)", "Centrally sponsored flagship conservation initiative launched at Jim Corbett to secure viable wild tiger populations in designated tiger reserves", "Programme to domesticate tigers as working animals; Plan to export wild tigers to overseas circus parks; Agricultural initiative to clear tiger habitat for crops"),
            ("Convention on Biological Diversity (CBD) / Earth Summit (Rio de Janeiro, 1992)", "Historic international treaty with three core objectives: conservation of biological diversity, sustainable use of components, and fair and equitable sharing of benefits", "Treaty legalizing biopiracy by multinational corporations; Economic agreement to eliminate all national parks; Protocol banning all scientific biodiversity research"),
            ("Convention on International Trade in Endangered Species (CITES, 1975)", "International agreement ensuring that international commercial trade in specimens of wild animals and plants does not threaten their survival", "Treaty setting minimum wholesale prices for elephant ivory; Agreement legalizing unrestricted trade in rhino horns; Protocol dismantling all customs border inspections"),
            ("Ramsar Convention on Wetlands (1971, Iran)", "Intergovernmental treaty establishing global framework for national action and international cooperation for the conservation and wise use of wetlands", "Treaty advocating the complete drainage of all global marshes; Protocol promoting industrial chemical discharge into lakes; Agreement to convert wetlands into commercial ports"),
            ("Biological Diversity Act, 2002 (India)", "National law enacted to fulfill CBD commitments, regulating access to biological resources and associated traditional knowledge through a 3-tier structure (NBA, SBB, BMC)", "Act privatizing all national biological resources to foreign corporations; Law abolishing patent benefit-sharing for local tribes; Statute repealing all previous forestry protection codes"),
            ("Project Elephant (launched in 1992 in India)", "Centrally sponsored initiative to protect elephant populations, secure elephant corridors, and mitigate human-elephant conflict", "Programme to capture all wild elephants for temple ceremonies; Commercial ivory extraction project; Project to build walls blocking all elephant migratory paths"),
            ("World Summit on Sustainable Development (Johannesburg, 2002)", "Global summit where 190 countries pledged to achieve a significant reduction in the current rate of biodiversity loss by 2010", "Conference declaring that biodiversity extinction is an unavoidable economic cost; Treaty repealing all international climate agreements; Summit legalizing whaling in Antarctic waters"),
            ("National Biodiversity Authority (NBA) of India", "Statutory autonomous body established in 2003 at Chennai to implement the Biological Diversity Act, approving access and ensuring equitable benefit-sharing", "Commercial logging corporation harvesting Andaman timber; Judicial court sentencing illegal poachers to prison; Private company distributing hybrid GMO seeds"),
            ("Red Panda Conservation and Project Snow Leopard (2009)", "Targeted high-altitude landscape conservation initiatives launched in India to protect fragile Himalayan ecosystems and alpine apex predators", "Eradication plan for high-altitude snow carnivores; Scheme to build highways through high alpine meadows; Project to clear Himalayan oak forests for tea plantations")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand conservation laws and conventions.** Key frameworks include the Wildlife Protection Act 1972, Project Tiger (1973), CITES, CBD / Earth Summit (1992), and the Biological Diversity Act (2002).\n**Step 2: Inspect {item[0]}.** The corresponding hallmark is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    return generate_vault_questions('CBSE-9-SCIE-12-12.3.2', 'Threats to biodiversity and national/global conservation measures', archs)

def main():
    all_questions = []

    print("Generating 12.2.3...")
    q1 = gen_12_2_3()
    print(f"12.2.3 generated {len(q1)} questions")
    all_questions.extend(q1)

    print("Generating 12.3.1...")
    q2 = gen_12_3_1()
    print(f"12.3.1 generated {len(q2)} questions")
    all_questions.extend(q2)

    print("Generating 12.3.2...")
    q3 = gen_12_3_2()
    print(f"12.3.2 generated {len(q3)} questions")
    all_questions.extend(q3)

    out_file = 'scripts/cbse9_scie_ch12_part_b.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved {len(all_questions)} questions to {out_file}")

if __name__ == '__main__':
    main()
