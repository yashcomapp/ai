import json
import re

def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        "Uncontrolled biological differentiation",
        "Non-vascular lignified parenchyma",
        "Passive artifact of cell shrinkage"
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
                "subtopic": subtopic_name,
                "chapterNumber": 3,
                "subjectCode": "SCIE",
                "class": "9",
                "boardCode": "CBSE",
                "type": "OSC",
                "vault": vault,
                "marks": 4
            })
            q_seq += 1

    return questions


# ==========================================
# 3.1.1: Apical, intercalary, lateral meristems (cambium)
# ==========================================
def gen_3_1_1():
    # Arch 1: General Characteristics of Meristematic Cells
    arch1 = {
        'templates': [
            "What distinct cytological feature defines: '{0}'?:",
            "In plant histology, meristematic tissue is recognized by: '{0}', which exhibits:",
            "Consider meristematic cytology: '{0}' is characterized by:",
            "Which statement precisely describes the anatomical nature of: '{0}'?:",
            "A botanist examines dividing plant tissue: '{0}'. What is true?:",
            "Identify the accurate histological fact regarding: '{0}':",
            "How does '{0}' enable continuous cell division in plant growth zones?:",
            "Evaluate the cellular attribute: '{0}'. Its functional significance is:",
            "Why is '{0}' indispensable for perpetual plant morphogenesis?:",
            "What cellular structure corresponds to: '{0}'?:"
        ],
        'data': [
            ("Meristematic cell cytoplasm", "Dense, granular cytoplasm rich in active organelles, ribosomes, and mitochondria", "Supports high metabolic rates and rapid ATP generation required for continuous mitotic cycles", "Watery, highly vacuolated sap with low protein content, Devoid of mitochondria and ribosomes, Completely crystalized storage fluid"),
            ("Meristematic cell vacuoles", "Vacuoles are either completely absent or extremely small and rudimentary", "Prevents structural hindrance to rapid karyokinesis and maintains compact protoplasm", "Giant central sap vacuole occupying 90% of cell volume, Multiple contractile vacuoles for osmoregulation, Air-filled gas vacuoles for floating"),
            ("Meristematic primary cell wall", "Thin, flexible, extensible wall composed solely of primary cellulose and pectin, lacking secondary lignin", "Allows cell expansion, stretching, and rapid cleavage during cytokinesis", "Thick, heavily lignified secondary wall impermeable to water, Peptidoglycan wall with teichoic acid, Chitinous shell with calcium carbonate"),
            ("Meristematic nucleus", "Prominent, centrally located, large nucleus with high nuclear-to-cytoplasmic (N:C) ratio and distinct nucleoli", "Coordinates intense transcriptional activity and frequent DNA replication cycles", "Tiny, pyknotic, peripheral nucleus pushed against cell wall, Enucleated state with complete loss of chromosomes, Multiple fragmented micronuclei"),
            ("Intercellular spaces in meristems", "Completely absent; cells are compactly arranged without any intercellular spaces", "Ensures rigid structural cohesion and seamless symplastic communication via plasmodesmata", "Massive air-filled cavities facilitating gas floatation, Broad intercellular spaces filled with resin, Wide canals lined with epithelial cells"),
            ("Plastids in meristematic cells", "Present only as undifferentiated, non-pigmented proplastids", "Differentiate into functional chloroplasts, chromoplasts, or leucoplasts only upon tissue maturation", "Mature fully stacked chloroplasts with active grana, Pigment-rich chromoplasts containing lycopene, Starch-storing amyloplasts"),
            ("Cell division mode in meristems", "Divide exclusively by standard equational division (mitosis) followed by cell plate cytokinesis", "Produces two identical daughter cells: one remains meristematic, while the other differentiates into permanent tissue", "Divide by reductional meiosis with crossing over, Divide by amitotic budding, Undergo nuclear division without cytokinesis"),
            ("Metabolic activity and respiration", "Exhibits exceptionally high rates of aerobic respiration and nutrient consumption", "Required to sustain continuous protein synthesis, spindle formation, and chromatin duplication", "Completely dormant anaerobic metabolism, Zero oxygen consumption, Passive state with no ATP turnover"),
            ("Ergastic substances in meristems", "Lacks stored ergastic substances (starch grains, fat droplets, calcium oxalate crystals)", "All synthesized metabolites are immediately utilized for cellular growth and replication", "Densely packed with large starch grains and aleurone layers, Loaded with calcium oxalate raphide crystals, Filled with rubber latex droplets"),
            ("Totipotency of meristematic cells", "Each meristematic cell retains the complete genetic capacity to regenerate an entire intact plant (cellular totipotency)", "Exploited extensively in plant tissue culture and micropropagation techniques", "Permanently committed and incapable of forming other tissues, Capable only of dying by apoptosis, Non-viable when isolated from stems")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Meristematic Tissue Characteristics.**\n- Meristematic cells are perpetually dividing, undifferentiated embryonic cells.\n- Features: Dense cytoplasm, thin cellulose walls, prominent nuclei, no/tiny vacuoles, no intercellular spaces, proplastids, high metabolic rate.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Functional / Cytological Context:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 2: Apical Meristem (SAM and RAM, Primary Growth)
    arch2 = {
        'templates': [
            "What is the anatomical location and primary role of: '{0}'?:",
            "In primary plant organogenesis: '{0}' is characterized by:",
            "Consider the shoot/root apical growth zone: '{0}' functions to:",
            "Which statement precisely describes the biology of: '{0}'?:",
            "A plant morphologist traces primary growth: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' drive elongation of the plant body?:",
            "Evaluate the histological feature: '{0}':",
            "Why is '{0}' vital for vertical axis extension in tracheophytes?:",
            "What developmental feature corresponds to: '{0}'?:"
        ],
        'data': [
            ("Shoot Apical Meristem (SAM)", "Located at the growing tips of stems and branches, responsible for primary elongation of shoots and leaf primordia initiation", "Dome-shaped meristematic zone giving rise to protoderm, ground meristem, and procambium", "Located at the base of internodes in monocots, Responsible for stem thickness in woody trees, Found exclusively inside mature seeds"),
            ("Root Apical Meristem (RAM)", "Sub-apical meristem located just behind the protective root cap (calyptra), responsible for primary longitudinal root growth", "Protected from abrasive soil particles as the root penetrates downward", "Located at the extreme tip without any protective cap, Responsible for radial bark formation, Found only in aquatic floating leaves"),
            ("Root Cap (Calyptra)", "Thimble-like protective parenchymatous cap covering the fragile RAM, secreting mucilage (mucigel)", "Lubricates root passage through soil and contains statoliths for gravitropism; absent in hydrophytes", "Actively divides to produce root xylem, Site of rapid nutrient absorption with root hairs, Meristematic tissue producing secondary bark"),
            ("Quiescent Centre (QC) in RAM", "Inverted cup-shaped region of cells in the root apex with exceptionally low mitotic activity, discovered by Clowes (1956)", "Acts as an inactive reservoir of stem cells that replenishes damaged initial cells of the meristem", "Hyperactive zone dividing every 10 minutes, Zone of rapid elongation and differentiation, Dead tissue protecting root hairs"),
            ("Tunica-Corpus Theory (Schmidt 1924)", "In SAM, Tunica consists of outer cell layers dividing anticlinally to form epidermis; Corpus consists of inner mass dividing in all planes to form cortex and vascular bundle", "Explains the organization of angiosperm shoot apices", "Applies to secondary root cambium, States that cells divide only tangentially, Describes stomatal guard cell movement"),
            ("Histogen Theory (Hanstein 1868)", "Proposes three distinct meristematic zones at root/shoot apices: Dermatogen (forms epidermis), Periblem (forms cortex), and Plerome (forms central stele/vascular cylinder)", "Useful framework for understanding root apical tissue derivation", "Describes cork cambium and phelloderm, Explains pollen tube growth, Describes chloroplast replication"),
            ("Protoderm, Ground Meristem, and Procambium", "Three primary meristems derived from apical meristems: Protoderm \\(\\rightarrow\\) Epidermis; Ground Meristem \\(\\rightarrow\\) Cortex, Endodermis, Pith; Procambium \\(\\rightarrow\\) Primary Xylem and Phloem", "Establish the primary tissue framework of the entire plant axis", "Protoderm forms wood; Ground meristem forms root cap; Procambium forms cuticle, All three differentiate into dead cork cells, Derived exclusively from secondary lateral cambium"),
            ("Axillary Buds (Lateral buds)", "Clusters of meristematic cells left behind from SAM during shoot elongation, positioned in the axils of leaves", "Capable of developing into vegetative branches or reproductive flowers upon release from apical dominance", "Formed by dedifferentiation of mature xylem, Permanently non-dividing storage cells, Meristematic cells that produce root hairs"),
            ("Apical Dominance and Auxin", "The apical bud inhibits the outgrowth of lateral axillary buds via polar basipetal transport of auxin (IAA)", "Decapitation (pruning/hedging) removes the auxin source, promoting vigorous lateral branching", "Cytokinins from shoot apex inhibit root growth, Gibberellins cause immediate leaf shedding, Ethylene promotes elongation of main stem"),
            ("Zone of Elongation in roots", "Region situated just proximal to the meristematic zone where newly formed cells undergo rapid vacuolation and longitudinal expansion", "Responsible for the actual physical lengthening of the root pushing through the soil", "Region where mature root hairs absorb minerals, Zone where lateral roots emerge from pericycle, Zone covered by protective suberized cork")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Apical Meristem Biology.**\n- Located at terminal growing apices (SAM at shoot tip, RAM sub-apical behind root cap).\n- Responsible for Primary Growth: vertical elongation and primary tissue framework (Protoderm, Ground Meristem, Procambium).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Developmental Context:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 3: Intercalary Meristem (Location, Grass Regrowth, Internodal Elongation)
    arch3 = {
        'templates': [
            "What is the evolutionary adaptation and function of: '{0}'?:",
            "In monocotyledonous stems and grasses: '{0}' is characterized by:",
            "Consider intercalary meristematic activity: '{0}' plays an essential role in:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A botanist studies grass regeneration after grazing: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' facilitate rapid internodal elongation?:",
            "Evaluate the anatomical feature: '{0}':",
            "Why is '{0}' vital for herbivore resistance in grasslands?:",
            "What physiological property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Intercalary Meristem Definition", "Meristematic tissue derived from the apical meristem that becomes separated and sandwiched between permanent mature tissues", "Located at the base of internodes (e.g., grasses, bamboo) or at leaf bases (e.g., Pinus)", "Lateral meristem increasing trunk girth, Primary meristem located inside root tips, Secondary tissue produced by cork cambium"),
            ("Rapid regrowth of grazed grasses", "When grazing herbivores (cows, goats) or lawnmowers consume terminal shoot tips, intercalary meristems at the base of nodes rapidly regenerate lost leaves and stems", "Key evolutionary adaptation allowing grasses to dominate global savannas and prairies", "Grasses regenerate entirely from deep tap roots, Grazing triggers immediate flower blooming, Shoots regrow by rapid lateral cambium division"),
            ("Bamboo rapid culm elongation", "Intercalary meristems situated at the base of every individual node divide simultaneously, allowing bamboo stems to grow up to \\(1\\text{ meter/day}\\)", "Parallel elongation across multiple internodes drives unmatched vertical growth rates in Poaceae", "Due entirely to cell expansion without any new cell divisions, Powered by secondary vascular cambium, Occurs only inside underground rhizomes"),
            ("Internodal elongation in monocot stems", "Adds new cells at the base of each internode, pushing older tissues upward and increasing stem length", "Active during vegetative growth and bolting", "Expands stem width by producing secondary phloem, Replaces broken root caps, Synthesizes secondary lignin in bark"),
            ("Base of leaf sheath in grasses", "Intercalary meristematic zones located at the junction of leaf blade and sheath allow leaves to continue growing even after clipping", "Enables turfgrass to withstand repetitive mowing in lawns and golf courses", "Lacks living cells and contains only dead fibres, Forms protective cork bark over leaves, Site of active seed germination"),
            ("Ephemerality of intercalary meristem", "Unlike indeterminate apical meristems, intercalary meristems are short-lived and eventually differentiate completely into permanent tissues", "Activity terminates once internodal elongation ceases", "Remains active for hundreds of years like tree cambium, Never differentiates into permanent cells, Continues dividing after the plant dies"),
            ("Straightening of lodged cereal stems (Negative gravitropism)", "When wind or rain knocks down wheat/rice stems (lodging), intercalary meristems on the lower side of nodes become active and divide more rapidly", "Curvatures at the nodes bend the stem upward toward light, restoring upright growth", "Stems straighten due to water loss by guttation, Lodged stems cannot recover and always rot, The entire plant uproots and flips over"),
            ("Intercalary meristem in Equisetum (Horsetails)", "Located at the base of each ribbed internode, surrounded by a sheath of fused microphylls", "Permits modular jointed stem growth characteristic of pteridophytes", "Produces secondary rings of bark, Found inside the sporangium only, Absorbs soil moisture directly"),
            ("Intercalary meristem in Pinus (Gymnosperm needles)", "Located at the base of the needle leaves, permitting basal growth while the tip matures", "Allows longevity and continuous expansion of evergreen needles", "Forms annual growth rings in wood, Located at the root cap apex, Disappears in seedlings"),
            ("Origin from apical meristem", "Intercalary meristem is of primary origin, representing detached portions of apical meristem left behind as the apex moves upward", "Shares the primary thin-walled, densely protoplasmic nature of apical cells", "Derived by secondary dedifferentiation of permanent sclerenchyma, Synthesized de novo from phloem sieve tubes, Formed by fusion of vascular cambium rings")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Intercalary Meristem Biology.**\n- Primary meristem derived from apical meristem, localized between permanent tissues (bases of internodes/nodes/leaves in grasses).\n- Short-lived; drives rapid internodal elongation and regrowth after herbivore grazing/lawnmowing.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Evolutionary / Ecological Context:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Lateral Meristems (Vascular Cambium & Cork Cambium, Secondary Growth)
    arch4 = {
        'templates': [
            "What is the anatomical role and developmental fate of: '{0}'?:",
            "In secondary plant growth (girth expansion): '{0}' is characterized by:",
            "Consider the lateral meristems: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A wood anatomist examines tree trunk thickening: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' contribute to secondary thickening in dicots and gymnosperms?:",
            "Evaluate the histological feature: '{0}':",
            "Why is '{0}' absent in typical monocotyledonous stems?:",
            "What structural tissue derives directly from: '{0}'?:"
        ],
        'data': [
            ("Lateral Meristem Definition", "Meristems arranged parallel to the longitudinal lateral axis of stems and roots, dividing periclinally to increase diameter (girth)", "Responsible for Secondary Growth in dicotyledonous angiosperms and gymnosperms", "Meristems located at root and shoot tips increasing length, Ephemeral tissues at internodes, Embryonic cells inside pollen grains"),
            ("Vascular Cambium (Fascicular + Interfascicular)", "Cylindrical sheath of meristematic cells between xylem and phloem; intra-fascicular cambium unites with interfascicular cambium to form a complete ring", "Divides periclinally to produce Secondary Xylem (wood) towards the inside and Secondary Phloem (inner bark) towards the outside", "Produces epidermis and cuticle towards the outside, Produces pith towards the inside, Forms root hairs on stems"),
            ("Cork Cambium (Phellogen)", "Secondary lateral meristem that arises in the outer cortical or epidermal region to replace ruptured epidermis", "Divides to produce Phellem (cork) towards the outside and Phelloderm (secondary cortex) towards the inside", "Produces primary vascular bundles, Produces secretory resin canals only, Formed exclusively inside the central pith"),
            ("Periderm Architecture", "Protective secondary tissue consisting of three layers: Phellem (outer dead suberized cork), Phellogen (cork cambium), and Phelloderm (inner living cortex)", "Acts as an impermeable barrier against desiccation, mechanical injury, and pathogens", "Consists of primary epidermis, stomata, and cuticle; Made of xylem vessels, tracheids, and wood fibres; Composed of living collenchyma and sclereids"),
            ("Bark (Botanical definition)", "All tissues lying external to the vascular cambium, including secondary phloem, cortex, and periderm", "Divided into outer bark (dead tissues external to innermost phellogen) and inner bark (living secondary phloem)", "Composed purely of dead secondary xylem, Consists only of primary epidermis and cuticle, Strictly identical to wood"),
            ("Wood (Secondary Xylem)", "The extensive tissue formed on the inner face of the vascular cambium, constituting the bulk of a woody tree trunk", "Composed of vessels, tracheids, xylem fibres, and xylem rays; provides mechanical support and water conduction", "The outer living tissue carrying sugars, Composed purely of suberized dead cells, Derived exclusively from phellogen"),
            ("Fusiform initials vs Ray initials", "Fusiform initials are vertically elongated cells producing axial secondary xylem and phloem; Ray initials are isodiametric cells producing horizontal parenchyma vascular rays", "Vascular rays conduct water and nutrients radially and store nutrients across the trunk", "Fusiform initials form cork, Ray initials form stomata, Both produce primary epidermal hairs"),
            ("Annual Rings (Growth Rings)", "Concentric growth rings consisting of Early Wood (Spring wood: wide vessels with thin walls) and Late Wood (Autumn wood: narrow vessels with thick walls)", "Formed due to seasonal activity fluctuations of vascular cambium in temperate climates; used to estimate tree age (Dendrochronology)", "Formed by seasonal peeling of cork bark, Caused by daily opening and closing of stomata, Direct result of lunar gravitational cycles"),
            ("Heartwood (Duramen) vs Sapwood (Alburnum)", "Heartwood is the non-functional, dark, central secondary xylem filled with tannins/resins/tyloses (provides durability); Sapwood is the outer, lighter, functional secondary xylem conducting water", "Heartwood is highly resistant to fungal decay and insect attack, making it prized commercial timber", "Heartwood conducts water actively while sapwood is dead, Sapwood is outer dead bark while heartwood is living phloem, Both conduct identical volumes of sap"),
            ("Absence of lateral cambium in Monocots", "Monocot stems possess closed, scattered vascular bundles lacking a vascular cambium, hence generally lack typical secondary growth", "Monocots (e.g., palms) attain thick trunks through primary thickening meristems or anomalous growth, not bifacial cambial rings", "Monocots have three concentric cambial rings, Monocots lack all meristems entirely, Monocots produce wood five times faster than dicots")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Lateral Meristem Biology.**\n- Cylindrical meristems parallel to organ axis (Vascular Cambium and Cork Cambium / Phellogen).\n- Responsible for Secondary Growth: radial expansion / girth increase (Secondary Xylem/Wood inside, Secondary Phloem outside; Phellem/Cork outside, Phelloderm inside).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Anatomical & Economic Significance:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 5: Comparative Classification & Diagnostic Matrix of Meristems
    arch5 = {
        'templates': [
            "Which category or property correctly classifies: '{0}'?:",
            "In comparative plant anatomy: '{0}' is categorized under:",
            "Consider meristem classification criteria: '{0}' is defined by:",
            "Which statement presents a 100% accurate classification of: '{0}'?:",
            "A botany examination question compares meristems: '{0}'. The correct answer is:",
            "Identify the accurate comparative feature: '{0}':",
            "How does '{0}' differ from other meristematic categories?:",
            "Evaluate the meristematic type: '{0}':",
            "Why is '{0}' placed in this specific anatomical division?:",
            "What definitive property distinguishes: '{0}'?:"
        ],
        'data': [
            ("Classification by position (Apical vs Intercalary vs Lateral)", "Apical at organ tips (length); Intercalary between mature tissues (internodal length); Lateral parallel to sides (girth/diameter)", "Based on topographical location within the plant body", "Based on whether cells divide by meiosis or mitosis, Based on the color of plastids, Based on presence or absence of DNA"),
            ("Classification by origin (Promeristem vs Primary vs Secondary)", "Promeristem: embryonic initial cells; Primary: derived from promeristem (apical/intercalary); Secondary: derived from permanent cells by dedifferentiation (cork cambium, interfascicular cambium)", "Reflects evolutionary ontogeny and developmental timing", "Based purely on cell size under light microscopy, Based on water content of the stem, Based on whether plants are herbaceous or woody"),
            ("Classification by plane of division (Rib vs Plate vs Mass meristem)", "Rib (file) meristem: divides in one plane (forms cortex/pith files); Plate meristem: divides in two planes (forms leaf lamina); Mass meristem: divides in all planes (forms endosperm/cortex mass)", "Determines the resulting three-dimensional organ geometry", "Governs the thickness of secondary cell walls, Controls whether chromosomes pair up, Dictates whether cells produce lignin"),
            ("Classification by function (Protoderm, Procambium, Ground Meristem)", "Baberlandt's functional classification: Protoderm (dermal system); Procambium (vascular system); Ground meristem (fundamental ground tissue system)", "Maps early embryonic lineages to adult functional tissue systems", "Divides cells based on photosynthetic rate, Separates tissues by secondary metabolite storage, Classifies based on pollen tube formation"),
            ("Dedifferentiation vs Redifferentiation", "Dedifferentiation: mature permanent living cells regain dividing capacity to form secondary meristem (e.g., parenchyma forming cork cambium); Redifferentiation: cells produced by secondary meristem mature into permanent tissues (e.g., secondary xylem/cork)", "Central biological principle underpinning plant grafting, wound repair, and secondary growth", "Dedifferentiation occurs only in dead cells, Redifferentiation leads back to embryonic zygote, Both terms describe cell death during necrosis"),
            ("Indeterminate vs Determinate growth in meristems", "Apical meristems exhibit indeterminate growth (perpetual vegetative production); Floral meristems exhibit determinate growth (cease dividing after producing sepals, petals, stamens, carpels)", "WUSCHEL and CLAVATA signaling circuits regulate the transition from indeterminate to determinate meristem fate", "All plant meristems stop dividing after one week, Floral meristems divide indefinitely forming infinite leaves, Roots show determinate growth while shoots are always indeterminate"),
            ("Primary meristem vs Secondary meristem", "Primary meristem originates directly from embryonic promeristem and builds the primary plant body; Secondary meristem originates from living permanent cells and builds secondary protective and vascular tissues", "Interfascicular cambium and cork cambium are classic secondary meristems", "Primary meristem has thick lignified walls, Secondary meristem is found only in algae, Both meristems produce identical primary epidermis"),
            ("Fascicular cambium vs Interfascicular cambium", "Fascicular cambium is primary in origin (present within vascular bundles from procambium); Interfascicular cambium is secondary in origin (formed by dedifferentiation of medullary ray parenchyma between bundles)", "Their continuous ring fusion creates the unified vascular cambial cylinder", "Fascicular cambium produces bark, Interfascicular cambium produces root hairs, Both arise exclusively from the epidermis"),
            ("Shoot apex zonation (CzA, PzA, RzA)", "Central Zone (CzA): slowly dividing stem cell pool; Peripheral Zone (PzA): rapidly dividing cells giving rise to leaf primordia; Rib Zone (RzA): gives rise to internal stem tissues (pith)", "Molecular feedback loop between WUSCHEL (WUS) in organizing center and CLAVATA3 (CLV3) maintains stem cell homeostasis", "Shoot apex has no zonation and consists of completely random cells, Zonation exists only in roots, Shoot zonation is an artifact of chemical fixation"),
            ("Meristem maintenance and stem cell niche", "The organizing center provides continuous non-cell-autonomous signals that maintain overlying cells in an undifferentiated stem cell state", "Loss of WUS leads to premature consumption and arrest of the shoot apical meristem", "Stem cells are maintained by massive suberin deposits, Stem cell niches are present only in animal bone marrow, Cells remain undifferentiated due to total absence of genes")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Meristem Classification Schemes.**\n- By Location: Apical (tips/length), Intercalary (internodes/regrowth), Lateral (sides/girth).\n- By Origin: Promeristem, Primary, Secondary (dedifferentiation of permanent cells).\n- By Plane: Rib (1 plane), Plate (2 planes), Mass (all planes).\n\n**Step 2: Classify '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Diagnostic / Anatomical Criterion:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 6: Quantitative & Analytical Problems in Meristematic Growth
    arch6 = {
        'templates': [
            "{0}:",
            "Calculate the plant growth or anatomical parameter: {0}:",
            "A quantitative plant histology calculation: {0}:",
            "Analytical meristem growth problem: {0}:",
            "Solve the quantitative botany calculation: {0}:",
            "Analyze the numerical meristematic cell division problem: {0}:",
            "Determine the correct calculated rate or value: {0}:",
            "An analytical plant morphogenesis question: {0}:",
            "Find the correct quantitative result: {0}:",
            "Compute the following growth metric: {0}:"
        ],
        'data': [
            ("A shoot apical meristem produces \\(120\\text{ new cells}\\) per cell cycle. If the cell cycle duration is 12 hours, how many cells are produced by this meristem in 4 days (assuming exponential doubling of active initials starting with 10 initial cells)?", "2,560 cells", "Number of 12-h cycles in 4 days (96 hours) \\(= 96 / 12 = 8\\) generations. Total cells \\(= 10 \\times 2^8 = 10 \\times 256 = 2,560\\)", "1,280 cells, 5,120 cells, 1,024 cells"),
            ("A grass culm has 8 internodes, each with an intercalary meristem at its base elongating at a rate of \\(1.5\\text{ mm/day}\\). What is the total longitudinal extension of the entire grass culm in 5 days?", "\\(60\\text{ mm}\\) (\\(6.0\\text{ cm}\\))", "\\(\\text{Elongation per day} = 8 \\times 1.5\\text{ mm} = 12\\text{ mm/day}\\). In 5 days: \\(12 \\times 5 = 60\\text{ mm} = 6.0\\text{ cm}\\)", "12 mm (1.2 cm), 120 mm (12.0 cm), 30 mm (3.0 cm)"),
            ("A tree trunk has radius \\(r_1 = 10\\text{ cm}\\). Over 5 years, the vascular cambium adds \\(2\\text{ mm}\\) of secondary xylem (wood) each year. What is the new circumference of the tree trunk (taking \\(\\pi = 3.14\\))?", "\\(69.08\\text{ cm}\\)", "Total radial growth \\(= 5 \\times 0.2\\text{ cm} = 1.0\\text{ cm}\\). New radius \\(r_2 = 10 + 1.0 = 11.0\\text{ cm}\\). New circumference \\(C = 2\\pi r = 2 \\times 3.14 \\times 11.0 = 69.08\\text{ cm}\\)", "62.80 cm, 75.36 cm, 65.94 cm"),
            ("A root tip was marked with Indian ink dots at \\(1\\text{ mm}\\) intervals starting from the root cap (Dots 0, 1, 2, 3, 4, 5). After 24 hours, the distance between Dots 1 and 2 increased from \\(1\\text{ mm}\\) to \\(6\\text{ mm}\\), while the distance between Dots 4 and 5 remained \\(1\\text{ mm}\\). Which developmental zone is represented between Dots 1 and 2?", "Zone of Elongation", "Rapid longitudinal expansion of newly divided cells occurs uniquely in the zone of elongation (just behind the meristem), whereas the mature zone (Dots 4-5) shows no elongation", "Root Cap zone, Zone of Secondary Growth, Quiescent Centre"),
            ("In an experiment, a nail was driven into the trunk of a 2-meter tall tree at a height of \\(1.0\\text{ meter}\\) from the ground. If the tree grows in height at a rate of \\(0.5\\text{ meters per year}\\), at what height from the ground will the nail be located after 6 years?", "\\(1.0\\text{ meter}\\) (the exact same height)", "Longitudinal growth occurs exclusively by apical meristems at the shoot apex; lateral meristems add girth, but cannot displace the height of previously formed mature trunk tissues", "4.0 meters, 3.0 meters, 0.5 meters"),
            ("If a vascular cambium ring has diameter \\(20\\text{ cm}\\), and each fusiform initial is \\(20\\text{ }\mu\\text{m}\\) wide tangentially, approximately how many fusiform initials form the perimeter of the cambial ring (\\(\\pi = 3.14\\))?", "\\(31,400\\text{ fusiform initials}\\)", "Circumference \\(= \\pi D = 3.14 \\times 20\\text{ cm} = 62.8\\text{ cm} = 628,000\\text{ }\mu\\text{m}\\). Number of cells \\(= 628,000 / 20 = 31,400\\)", "3,140 initials, 314,000 initials, 15,700 initials"),
            ("A bamboo shoot grows \\(90\\text{ cm}\\) in 24 hours. What is its average elongation rate in micrometers per second (\\(\\mu\\text{m/s}\\))?", "\\(10.42\\text{ }\mu\\text{m/s}\\)", "\\(90\\text{ cm} = 900,000\\text{ }\mu\\text{m}\\). Seconds in 24 hours \\(= 24 \\times 3,600 = 86,400\\text{ s}\\). Rate \\(= 900,000 / 86,400 \\approx 10.42\\text{ }\mu\\text{m/s}\\)", "1.04 μm/s, 104.2 μm/s, 5.21 μm/s"),
            ("A cross-section of a gymnosperm stem reveals 45 distinct annual growth rings. What is the estimated age of this tree stem, and what discipline studies this?", "45 years (Dendrochronology)", "Each annual ring represents one year's seasonal cycle of early (spring) and late (autumn) wood production; analyzed via dendrochronology", "90 years (Palynology), 22.5 years (Histochemistry), 450 years (Dendrology)"),
            ("The mitotic index of an onion root apical meristem is \\(8.5\\%\\). If 2,000 cells are examined across multiple fields under microscopy, how many cells are actively undergoing mitotic division?", "170 dividing cells", "\\(\\text{Dividing cells} = 2,000 \\times 0.085 = 170\\)", "85 cells, 340 cells, 17 cells"),
            ("If an apical meristem cell has \\(2n = 14\\) chromosomes and a DNA content of \\(4\\text{ pg}\\) in G1 phase, what will be the chromosome number and DNA content of each daughter cell immediately after completing cytokinesis?", "14 chromosomes and 4 pg DNA", "Equational mitotic division maintains constant diploid chromosome number (\\(2n = 14\\)) and identical DNA content (4 pg) in both daughter cells", "7 chromosomes and 2 pg DNA, 14 chromosomes and 8 pg DNA, 28 chromosomes and 4 pg DNA")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Identify given physical and biological quantities.**\n" + item[0] + "\n\n**Step 2: Apply the governing anatomical/mathematical formula.**\n" + item[2] + ".\n\n**Step 3: Conclude.**\nResult is " + item[1] + "."
        ),
        'diff': 'hard'
    }

    # Arch 7: Experimental Techniques and Historical Discoveries in Meristem Biology
    arch7 = {
        'templates': [
            "Which historical discovery, staining technique, or experiment relates to: '{0}'?:",
            "In botanical research and plant histology: '{0}' was demonstrated by:",
            "What experimental protocol is used to study: '{0}'?:",
            "How did plant anatomists historically elucidate: '{0}'?:",
            "A student performs an onion root tip squash: '{0}'. What is observed?:",
            "Which histochemical stain is specific for: '{0}'?:",
            "In agricultural biotechnology, '{0}' is utilized to:",
            "What laboratory observation confirms: '{0}'?:",
            "Evaluate the scientific protocol used for: '{0}':",
            "Identify the landmark botanical contribution regarding: '{0}':"
        ],
        'data': [
            ("Onion root tip squash with Acetocarmine", "Root tips are fixed in Carnoy's fluid (acetic acid : ethanol 1:3), hydrolyzed in dilute HCl to soften pectin middle lamella, and stained with acetocarmine", "Standard educational protocol for visualizing all stages of mitosis (prophase, metaphase, anaphase, telophase)", "Stains cell wall lignin green, Dissolves chromosomes leaving only empty cells, Stains vacuolar anthocyanins red"),
            ("Colchicine treatment of apical meristems", "Alkaloid from Colchicum autumnale that binds tubulin and arrests spindle assembly at metaphase, inducing polyploidy (e.g., doubling chromosome number from 2n to 4n)", "Widely used in plant breeding to create larger, higher-yielding tetraploid and octoploid crop varieties", "Accelerates cytokinesis by 500%, Destroys cell membrane lipids, Stimulates instant floral blooming"),
            ("Meristem culture for virus-free plant production", "Excising apical meristem dome (\\(0.1\\text{ to }0.3\\text{ mm}\\)) free of vascular tissues and culturing in vitro produces 100% virus-free clones", "Viruses cannot keep pace with rapid meristematic division and lack vascular pathways (xylem/phloem) in the apex", "Viruses are destroyed by adding high doses of penicillin, Meristems contain viral antibodies, Meristem cells have impenetrable chitin walls"),
            ("Sachs' landmark demonstration of growing zones (1873)", "Marked germinating radicles at uniform millimeter intervals to discover that growth is restricted strictly to a discrete sub-apical zone", "Established the modern concept of spatial zonation (Meristematic \\(\\rightarrow\\) Elongation \\(\\rightarrow\\) Maturation)", "Proved that roots grow from the base, Disproved existence of cell division in plants, Claimed roots absorb carbon dioxide from air"),
            ("Phloroglucinol-HCl staining of secondary tissues", "Stains lignified cell walls of secondary xylem, sclerenchyma, and mature vessels bright cherry red (reacts with coniferyl aldehyde units in lignin)", "Differentiates lignified secondary permanent tissues from non-lignified primary meristematic cells", "Stains starch grains deep blue-black, Stains living cytoplasm yellow, Selectively bleaches all cellulose"),
            ("Dendrochronology and Cross-Dating (A.E. Douglass)", "Analyzing matching patterns of narrow (drought) and wide (favorable) annual rings in living trees and historical timbers", "Enables precise calendar-year dating of wooden archaeological artifacts and climate reconstruction across millennia", "Dating based on carbon-14 decay in live leaves, Counting leaf veins under electron microscopy, Measuring soil moisture fluctuations"),
            ("Skoog and Miller's Auxin-Cytokinin hormonal ratio experiment (1957)", "Demonstrated that high auxin : low cytokinin ratio induces root regeneration; high cytokinin : low auxin ratio induces shoot bud initiation; balanced ratio maintains undifferentiated callus meristem", "Cornerstone principle of plant tissue culture and organogenesis", "Proved gibberellins degrade chromosomes, Demonstrated ethylene dissolves cell walls, Showed abscisic acid stimulates mitosis"),
            ("Thymidine labeling of Quiescent Centre (Clowes)", "Pulse-labeling with tritiated thymidine revealed zero or minimal incorporation into DNA of the central hemispherical cell cluster in the root apex", "Conclusive autoradiographic proof of a low-mitotic 'quiescent centre' acting as a stem cell reserve", "Showed all root cells divide at identical speeds, Proved root caps divide faster than apical cells, Showed roots lack DNA"),
            ("Scanning Electron Microscopy (SEM) of SAM", "Reveals the pristine 3D geometric dome of the vegetative apex surrounded by spirally arranged leaf primordia following Fibonacci phyllotaxis", "Visualizes cellular arrangements and organ initiation with sub-micrometer depth of field", "Resolves internal nuclear pore complexes, Stains chloroplast thylakoids, Measures cellular ATP levels directly"),
            ("Wounding and Callus Meristem Formation", "Injury to living parenchyma cells triggers dedifferentiation into an unorganized, rapidly proliferating meristematic mass termed callus", "Produces protective wound periderm and serves as the starting material for genetic transformation via Agrobacterium", "Causes immediate permanent cell death of the entire plant, Converts stems into reproductive roots, Stimulates immediate shedding of all bark")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Historical and Experimental Meristem Biology.**\n- Classical experiments (Sachs, Clowes, Skoog & Miller) established spatial zonation, the quiescent center, and hormonal control of meristem differentiation.\n- Techniques include root tip squashes, colchicine-induced polyploidy, and virus-free meristem tip culture.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Laboratory / Agricultural Significance:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    # Arch 8: Plant Morphogenesis, Hormonal Control & Developmental Anomalies
    arch8 = {
        'templates': [
            "Which developmental signaling mechanism or hormonal pathway controls: '{0}'?:",
            "In plant physiological morphogenesis: '{0}' is characterized by:",
            "What physiological consequence results from: '{0}'?:",
            "How does the plant hormone system coordinate: '{0}'?:",
            "A plant physiologist investigates meristem fate: '{0}'. What is true?:",
            "Which molecular or environmental factor regulates: '{0}'?:",
            "What is the developmental significance of: '{0}'?:",
            "Why is '{0}' critical for vegetative-to-reproductive transition?:",
            "What abnormal phenotype occurs upon disruption of: '{0}'?:",
            "Evaluate the plant developmental concept: '{0}':"
        ],
        'data': [
            ("CLAVATA-WUSCHEL (CLV-WUS) feedback loop in SAM", "WUS transcription factor in organizing center promotes stem cell identity; overlying stem cells secrete CLV3 peptide which activates CLV1/CLV2 receptors to repress WUS", "Maintains constant, stable stem cell population preventing meristem overproliferation or exhaustion", "Triggers immediate apoptosis of the entire shoot, Causes roots to form at the stem apex, Inactivates all photosynthetic genes"),
            ("Polar Auxin Transport (PAT) and PIN proteins", "Asymmetric localization of PIN-FORMED (PIN) efflux carriers drives directional auxin flow toward shoot apex tips and root columella", "Creates local auxin maxima that trigger initiation of new leaf primordia and lateral root founder cells", "Transports sugars symmetrically through phloem, Degrades plant hormones in vacuoles, Pumps water across root cap cells"),
            ("Cytokinin signaling and shoot meristem proliferation", "Cytokinins (e.g., zeatin, isopentenyladenine) act through histidine kinase receptors to stimulate cell division and expand SAM size", "Antagonistic to auxin: high cytokinin promotes shoot vegetative branching and inhibits root elongation", "Induces dormancy and leaf shedding, Inhibits DNA replication in meristems, Dissolves plant cell walls"),
            ("Florigen (FT protein) and Floral Meristem Transition", "FLOWERING LOCUS T (FT) protein produced in leaves under inductive photoperiods moves via phloem to SAM, transforming it into a floral meristem", "Converts indeterminate vegetative apex into determinate flower-bearing inflorescence", "Destroys the apical dome causing stem dieback, Converts flowers into vegetative leaves, Stops all nutrient transport"),
            ("Abscisic Acid (ABA) and Meristem Dormancy", "High ABA levels induce bud scale formation and arrest mitotic activity in apical and lateral meristems during winter cold or drought", "Protects fragile embryonic tissues inside dormant terminal winter buds until spring warmer temperatures return", "Stimulates rapid stem elongation, Causes explosive cell division in bark, Promotes water absorption through bark"),
            ("Gibberellins (GA) and Bolting in Rosette Plants", "Application of gibberellic acid triggers dramatic internodal intercalary meristem division and elongation in rosette plants (e.g., cabbage)", "Causes rapid vertical shooting and premature flowering without changing environmental daylength", "Permanently shrinks the plant into dwarf form, Inhibits all stem elongation, Destroys flower buds"),
            ("Fasciation (Crested growth anomaly)", "Abnormal expansion or flattening of the shoot apical meristem from a single focal point into a broad ribbon-like line", "Results in flattened, ribbon-like, or crested stems, flowers, and fruits (e.g., cockscomb Celosia, beefsteak tomato)", "Shrinks stems into needle-thin threads, Complete loss of all lateral branches, Inability to produce chlorophyll"),
            ("Girdling / Ringing experiment (Malpighi 1675)", "Removing a complete ring of bark (periderm, cortex, and phloem) down to the vascular cambium causes swelling above the girdle and root death", "Proves that organic nutrients (sugars) are translocated downwards exclusively through the phloem bark", "Proves water ascends through bark, Has zero effect on plant survival, Causes immediate wilting of upper leaves"),
            ("Agrobacterium tumefaciens and Crown Gall disease", "Transfers T-DNA carrying auxin (iaaM, iaaH) and cytokinin (ipt) biosynthetic genes into host plant genome, driving uncontrolled meristematic division", "Results in massive disorganized neoplastic tumor (gall) growth on plant stems and crowns", "Kills the plant within 10 seconds by poison, Degrades all plant cellulose, Inhibits all plant cell division"),
            ("Witches' broom symptom (Phytoplasma infection)", "Bacterial phytoplasmas secrete effector proteins (e.g., SAP11) that disrupt TCP transcription factors, completely abolishing apical dominance", "Triggers explosive, uncontrolled proliferation of hundreds of clustered dwarf lateral branches resembling a broom", "Causes all branches to drop off leaving bare trunk, Doubles trunk girth within one day, Converts all leaves into thick bark")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Plant Morphogenesis & Meristem Regulation.**\n- Meristem activity is tightly coordinated by hormonal balances (Auxin, Cytokinin, Gibberellin, ABA) and gene regulatory networks (CLV-WUS feedback).\n- Disruptions produce profound developmental alterations (fasciation, crown gall, witches' broom, bolting).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Morphogenetic Consequence:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-3-3.1.1", "Apical, intercalary, lateral meristems (cambium)", archs)


# ==========================================
# 3.1.2: Parenchyma (storage, aerenchyma, chlorenchyma)
# ==========================================
def gen_3_1_2():
    # Arch 1: General Histology and Structure of Parenchyma
    arch1 = {
        'templates': [
            "What distinct anatomical and cytological feature defines: '{0}'?:",
            "In plant ground tissues: '{0}' is characterized by:",
            "Consider parenchyma tissue histology: '{0}' exhibits:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A botanist examines living ground tissue: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' maintain living metabolic function in permanent plant tissues?:",
            "Evaluate the cellular attribute: '{0}'. Its biological role is:",
            "Why is '{0}' considered the fundamental ground tissue of all tracheophytes?:",
            "What structural property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Parenchyma cell shape (Isodiametric)", "Typically isodiametric, oval, spherical, rounded, or polygonal with equal diameters in all directions", "Uniform shape allows flexible packaging in pith, cortex, and mesophyll", "Highly elongated spindle-shaped fibers, Hollow dead cylinders with spiral rings, Rigid star-shaped sclereids"),
            ("Parenchyma cell wall composition", "Thin, flexible primary cell wall made of cellulose, hemicellulose, and pectin, strictly lacking secondary lignin", "Allows cell expansion, osmosis, turgor adjustments, and chemical permeability", "Thick, heavily lignified secondary wall with bordered pits, Suberized waterproof wall, Peptidoglycan cell wall"),
            ("Living state and protoplasm in parenchyma", "Living at functional maturity, possessing active cytoplasm, prominent nucleus, and a large central vacuole", "Capable of sustained metabolic processes (respiration, secretion, biosynthesis) and dedifferentiation", "Dead at maturity lacking all living contents, Enucleated cell lacking cytoplasm, Spore-like dehydrated cell"),
            ("Intercellular spaces in parenchyma", "Prominent, small to large intercellular air spaces present between cell corners", "Facilitates internal gaseous diffusion (\\(\\text{CO}_2, \\text{O}_2\\)) throughout ground tissues", "Completely absent with tight interlocking walls, Filled with solid secondary lignin, Sealed with waterproof suberin"),
            ("Vacuolation and turgidity in parenchyma", "Contains a large central sap vacuole that maintains hydrostatic turgor pressure", "Provides mechanical support and firmness to non-woody, herbaceous plant organs (e.g., leaves, young stems)", "Lacks vacuoles entirely to maximize cell division, Filled with air bubbles for flight, Vacuole contains pure lipid crystals"),
            ("Pith and Cortex composition", "Pith (medulla) and cortex of dicot stems and roots consist predominantly of loosely arranged parenchyma cells", "Serves as the structural matrix and storage reservoir of the plant axis", "Composed entirely of dead lignified sclerenchyma fibres, Composed of dead xylem vessels, Formed exclusively by cork"),
            ("Plasmodesmatal connectivity", "Parenchyma cells are interconnected by numerous plasmodesmata spanning primary pit fields", "Enables continuous symplastic transport of sugars, amino acids, and signaling molecules", "Isolated completely with zero intercellular transport, Connected only by gap junctions, Fused into a continuous syncytium"),
            ("Capacity for dedifferentiation", "Under appropriate hormonal or wounding cues, mature living parenchyma cells can dedifferentiate into meristematic cells", "Forms secondary cambial rings (interfascicular cambium, phellogen) and wound callus", "Permanently committed and incapable of dividing, Can only undergo apoptosis, Transforms directly into dead xylem"),
            ("Origin from ground meristem", "Derived from the primary ground meristem of the shoot and root apical meristems", "Forms the fundamental ground tissue system of the primary plant body", "Derived from secondary lateral cambium only, Synthesized from dead cork, Formed by epidermal hair division"),
            ("Distribution across plant organs", "Universally distributed across roots, stems, leaves, flowers, fruits, and seeds", "Forms the continuous packaging ground tissue embedding all specialized vascular and dermal tissues", "Restricted strictly to the outer bark of woody trees, Found only inside pollen grains, Present only in aquatic plants")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Parenchyma Histology.**\n- Most abundant, fundamental, living ground tissue in plants.\n- Features: Isodiametric, thin primary cellulose walls, living protoplasm, large central vacuole, intercellular spaces, capable of dedifferentiation.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Cytological / Anatomical Detail:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 2: Chlorenchyma (Photosynthesis, Palisade & Spongy Mesophyll)
    arch2 = {
        'templates': [
            "What is the specialized function and anatomical structure of: '{0}'?:",
            "In photosynthetic foliar tissues: '{0}' is characterized by:",
            "Consider chlorenchyma adaptation: '{0}' functions to:",
            "Which statement precisely describes: '{0}'?:",
            "A plant physiologist examines leaf mesophyll: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' optimize light capture and gas exchange?:",
            "Evaluate the histological feature: '{0}':",
            "Why is '{0}' vital for autotrophic solar energy conversion?:",
            "What anatomical property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Chlorenchyma Definition", "Specialized parenchyma cells containing abundant functional chloroplasts, dedicated to photosynthesis", "Found primarily in the mesophyll of leaves, young green stems, and phylloclades", "Parenchyma modified to store large volumes of air in water plants, Dead cells with thick lignified walls, Food conducting tissue in phloem"),
            ("Palisade mesophyll in dorsiventral leaves", "Vertically elongated, columnar chlorenchyma cells arranged compactly in one or two layers perpendicular to the upper adaxial epidermis", "Contains \\(\\approx 80\\%\\) of foliar chloroplasts; optimized to capture direct sunlight entering the leaf surface", "Loosely arranged spherical cells with huge air cavities, Dead protective cells on the leaf surface, Vascular tissue conducting sap"),
            ("Spongy mesophyll in dorsiventral leaves", "Loosely arranged, irregularly shaped or lobed chlorenchyma cells with expansive intercellular air cavities facing the lower abaxial epidermis", "Maximizes internal surface area for rapid diffusion of \\(\\text{CO}_2\\) from stomata to photosynthesizing cells", "Compact columnar cells without air spaces, Highly lignified structural tissue, Clear cells lacking all chloroplasts"),
            ("Isobilateral leaf mesophyll (Monocots e.g., Grasses)", "Mesophyll is not differentiated into distinct palisade and spongy layers; consists of uniform chlorenchyma cells throughout", "Adapted to vertical leaf orientation where both surfaces receive equal sunlight", "Contains only dead sclerenchyma fibres, Completely lacks chloroplasts, Divided into four distinct palisade zones"),
            ("Chloroplast orientation (Photorelocation)", "Chloroplasts inside chlorenchyma cells move dynamically along actin filaments: accumulate along periclinal walls under low light (accumulation) and move to anticlinal walls under excessive light (avoidance)", "Protects photosynthetic machinery from photo-inhibition and light-induced oxidative stress", "Chloroplasts are cemented permanently to cell corners, Move into vacuoles during night, Expelled into intercellular spaces"),
            ("Stomatal substomatal cavity", "Large respiratory cavity directly beneath each stoma in the spongy mesophyll layer", "Acts as the immediate mixing chamber for gaseous exchange (\\(\\text{CO}_2\\) uptake and \\(\\text{H}_2\\text{O}\\) vapor transpiration)", "Water storage reservoir for drought survival, Site where pollen grains germinate, Digestive cavity for trapping insects"),
            ("Chlorenchyma in herbaceous stems (Cortex chlorenchyma)", "Outer cortical layers of young green stems contain chlorenchyma capable of photosynthesis", "Contributes significantly to total carbon fixation before secondary woody bark forms", "Synthesizes secondary lignin to kill the stem, Absorbs water directly from atmospheric air, Stores heavy metals"),
            ("Phylloclade / Cladode chlorenchyma (e.g., Opuntia, Ruscus)", "In xerophytic succulents where leaves are reduced to protective spines, modified green stems contain extensive chlorenchyma", "Takes over 100% of the plant's photosynthetic responsibilities while minimizing transpiration", "Stores toxic salt crystals, Produces root hairs above ground, Made entirely of dead cork"),
            ("Kranz anatomy in C4 plants (e.g., Maize, Sugarcane)", "Specialized concentric arrangement where bundle sheath chlorenchyma with agranal chloroplasts surrounds vascular bundles, ringed by mesophyll chlorenchyma", "Operates the \\(\\text{C}_4\\) dicarboxylic acid pathway, eliminating photorespiration and concentrating \\(\\text{CO}_2\\) at RuBisCO", "Composed of non-chloroplastic dead sclerenchyma, Found only in aquatic floating ferns, Prevents water transport in veins"),
            ("Chloroplast count per chlorenchyma cell", "A single mature palisade chlorenchyma cell typically contains \\(30\\text{ to }70\\text{ chloroplasts}\\)", "Provides immense membrane surface area for light-harvesting pigment complexes", "Contains exactly 1 chloroplast like Chlamydomonas, Contains 1,000,000 chloroplasts, Lacks chloroplasts entirely")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Chlorenchyma Structure & Function.**\n- Chlorenchyma is parenchyma containing abundant functional chloroplasts.\n- Primary site of photosynthesis (Palisade mesophyll: columnar, light capture; Spongy mesophyll: loose, gas exchange).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Physiological Details:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 3: Aerenchyma (Aquatic Adaptations, Buoyancy & Gas Diffusion)
    arch3 = {
        'templates': [
            "What is the ecological adaptation and structural feature of: '{0}'?:",
            "In hydrophytes and wetland plants: '{0}' is characterized by:",
            "Consider aerenchyma tissue biology: '{0}' functions to:",
            "Which statement precisely describes: '{0}'?:",
            "A freshwater ecologist examines aquatic plants: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' prevent root anoxia in waterlogged anaerobic soils?:",
            "Evaluate the anatomical feature: '{0}':",
            "Why is '{0}' vital for buoyancy and floatation in hydrophytes?:",
            "What histological property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Aerenchyma Definition", "Specialized parenchyma tissue enclosing exceptionally large, continuous air chambers (lacunae) separated by thin cellular septa", "Provides mechanical buoyancy allowing aquatic plants to float, and creates internal channels for longitudinal gas diffusion", "Densely packed cells storing concentrated starch, Heavily lignified dead tissue providing rigid trunk support, Tissue conducting water"),
            ("Buoyancy in floating hydrophytes (e.g., Eichhornia / Water Hyacinth)", "Swollen spongy petioles of water hyacinth are packed with aerenchyma containing trapped air", "Enables the plant body to stay buoyant on the water surface and access atmospheric light and air", "Plants float due to oil droplets stored in seeds, Heavy calcium crystals keep the plant floating, Floats due to gas produced by bacteria"),
            ("Lysigenous aerenchyma formation", "Formed by programmed cell death (PCD) and autolytic dissolution of entire cortical cell files (e.g., in waterlogged maize and rice roots)", "Triggered by ethylene gas accumulation in submerged, hypoxic root tissues", "Formed by rapid division of lateral cambium, Created by cell wall suberization, Formed by drying and desiccation"),
            ("Schizogenous aerenchyma formation", "Formed by coordinated cell separation along the middle lamella during development without cell lysis (e.g., in many natural wetland monocots)", "Creates geometrically precise, unbroken longitudinal air tubes extending from leaves to root tips", "Formed by mechanical crushing of cells, Produced by fungal infection, Formed by calcium carbonate deposition"),
            ("Internal oxygen transport to waterlogged roots", "Continuous internal aerenchyma channels allow atmospheric oxygen to diffuse longitudinally from aerial shoots down to submerged roots", "Prevents lethal root anoxia and maintains aerobic cellular respiration in oxygen-depleted anaerobic muds", "Transports water upward from soil to leaves, Transports toxic methane into leaves for storage, Absorbs nitrogen gas directly"),
            ("Radial Oxygen Loss (ROL) and Rhizosphere Oxidation", "Excess oxygen diffusing through root aerenchyma leaks out into the surrounding toxic, reduced soil (rhizosphere)", "Oxidizes toxic ferrous iron (\\(\\text{Fe}^{2+}\\)) to harmless ferric iron (\\(\\text{Fe}^{3+}\\)), creating protective iron plaques around roots", "Deoxygenates the soil to kill competitor plants, Emits carbon monoxide to attract bacteria, Dissolves soil minerals"),
            ("Stellate parenchyma in Juncus (Rushes)", "Aerenchyma cells with radiating star-like arms (stellate cells) connected at their arm tips", "Creates a mechanically resilient, crush-resistant honeycomb framework surrounding enormous air cavities", "Dense hexagonal packing preventing all air diffusion, Spindle-shaped cells producing silk fibres, Dead cells with helical lignified bands"),
            ("Petiolar aerenchyma in Lotus and Water Lily (Nymphaea)", "Long, hollow, flexible petioles contain multiple large longitudinal air canals lined with aerenchyma and internal sclereid astrosclereids", "Facilitates gas exchange between surface floating leaves and deep mud-anchored rhizomes", "Conducts soil sand to floating leaves, Rigid wooden cylinder preventing any bending, Transports dissolved sugar directly to fish"),
            ("Pneumatophore aerenchyma in Mangroves (e.g., Rhizophora, Avicennia)", "Negatively gravitropic vertical breathing roots (pneumatophores) possess lenticels connected to extensive internal cortical aerenchyma", "Allows oxygen intake during low tide to sustain buried subterranean root systems in saline, waterlogged muds", "Absorbs ocean salt to sweeten the fruit, Photosynthesizes underwater, Functions exclusively as reproductive flowers"),
            ("Methane emissions and aerenchyma conduit", "Aerenchyma in wetland plants (especially paddy rice fields) acts as an open chimney, facilitating passive upward venting of soil methane (\\(\\text{CH}_4\\))", "Significant contributor to global biogenic greenhouse gas emissions from flooded agricultural soils", "Converts methane into glucose in chloroplasts, Traps methane inside permanently, Emits pure ozone into atmosphere")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Aerenchyma Biology.**\n- Specialized parenchyma with large, continuous intercellular air cavities (lacunae).\n- Functions: Buoyancy (floatation in aquatic plants like Eichhornia, Nymphaea) and internal longitudinal gas conduits (delivering \\(\\text{O}_2\\) to waterlogged roots in rice/mangroves).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Ecological / Environmental Detail:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Storage Parenchyma, Idioblasts & Succulent Water Storage
    arch4 = {
        'templates': [
            "What physiological storage role or anatomical adaptation defines: '{0}'?:",
            "In plant reserve storage and xerophytic survival: '{0}' is characterized by:",
            "Consider storage parenchyma specialization: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A botanist analyzes plant storage organs: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' support drought resistance or nutrient dormancy?:",
            "Evaluate the cellular specialization: '{0}':",
            "Why is '{0}' vital for perennation and economic crop yield?:",
            "What biochemical reserve corresponds to: '{0}'?:"
        ],
        'data': [
            ("Amyloplast storage parenchyma in Potato tubers (Solanum tuberosum)", "Parenchyma cells densely packed with starch grains showing concentric or eccentric growth rings around a hilum", "Acts as the primary carbohydrate reserve ensuring survival through unfavorable seasons (perennation)", "Stores pure protein crystals in vacuole, Stores lipid droplets in cell wall, Contains chlorophyll for photosynthesis"),
            ("Water-storage parenchyma in succulents (e.g., Aloe, Agave, Cacti)", "Massive, thin-walled parenchyma cells containing large central vacuoles filled with mucilage and hydrophilic polysaccharides", "Retains huge volumes of water during prolonged droughts, conferring extreme desiccation tolerance", "Stores air for floatation, Filled with crystalline toxic calcium, Generates heat by non-shivering thermogenesis"),
            ("Aleurone layer in cereal grains (e.g., Wheat, Maize)", "Specialized peripheral endosperm parenchyma layer densely packed with aleurone protein grains", "Synthesizes hydrolytic enzymes (alpha-amylase) in response to gibberellin during seed germination", "Photosynthetic tissue producing sucrose, Dead tissue forming the husk, Water storage tissue preventing seed drying"),
            ("Cotyledonary storage parenchyma in legumes (e.g., Pea, Bean)", "Stores abundant protein (legumin, vicilin) and starch reserves to nourish the developing embryo during germination", "Provides the primary dietary protein source for humans and herbivores", "Contains only water and mineral salts, Consists of dead lignified fibers, Made of active meristematic initials"),
            ("Endosperm storage parenchyma in Castor (Ricinus communis)", "Rich in lipid droplets (triacylglycerols in oleosomes/oil bodies) and protein aleurone grains", "Lipids undergo beta-oxidation and glyoxylate cycle conversion into sugars during seedling establishment", "Stores calcium carbonate crystals, Completely filled with cellulose walls, Lacks living contents"),
            ("Idioblasts (Specialized solitary parenchyma cells)", "Individual parenchyma cells markedly differing in shape, size, or content from surrounding ground tissue cells", "Store specialized defensive compounds: tannins, essential oils, mucilage, gums, or calcium oxalate crystals", "Undifferentiated meristematic cells dividing rapidly, Dead cells forming hollow xylem vessels, Stomatal guard cells"),
            ("Raphides and Druses (Calcium oxalate idioblasts)", "Raphides (needle-like crystal bundles) and Druses (spherical star-like crystal clusters) stored in specialized vacuolar idioblasts", "Serve as physical and chemical deterrents against herbivory (cause intense irritation to mucosal tissues e.g., Colocasia/Arum)", "Nutritional reserves metabolized into ATP, Structural pillars preventing cell collapse, Pigments giving flowers blue color"),
            ("Cystoliths and Lithocysts (e.g., Ficus elastica leaf)", "Lithocysts are enlarged epidermal/parenchymal cells containing cystoliths: grape-like internal deposits of calcium carbonate (\\(\\text{CaCO}_3\\)) on a cellulose stalk", "Excretory waste sink and light-scattering optical device inside leaves", "Starch storage vesicle, Site of nitrogen fixation, Water absorption hair"),
            ("Prosenchyma (Elongated parenchyma)", "Parenchyma cells with tapered, pointed ends whose walls may become slightly thickened", "Provides both metabolic living functions and minor tensile support in herbaceous stems and vascular bundles", "Isodiametric round storage cells, Completely dead hollow tubes, Cells containing only air"),
            ("Pavement parenchyma in fleshy fruits (e.g., Watermelon, Apple)", "Massive, highly vacuolated, thin-walled parenchyma cells filled with sweet sugary cell sap (fructose, glucose, organic acids)", "Attracts frugivorous animals to consume the fruit and disperse mature seeds across wide geographic ranges", "Tough lignified fibres protecting seeds, Toxic defensive tissue preventing seed consumption, Air-filled tissue making fruit float")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Storage Parenchyma & Idioblasts.**\n- Specialized parenchyma stores vital reserve materials (starch in potato tubers, water/mucilage in succulents, proteins/lipids in seeds).\n- Idioblasts contain specialized defensive metabolites (raphides, druses, cystoliths, tannins).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Physiological / Adaptive Significance:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 5: Comparative Matrix & Diagnostic Distinctions of Parenchyma Types
    arch5 = {
        'templates': [
            "Which row in the table correctly characterizes: '{0}'?:",
            "In comparative ground tissue histology: '{0}' is distinguished by:",
            "Consider parenchyma functional diversity: '{0}' is classified as:",
            "Which statement presents a 100% accurate contrast: '{0}'?:",
            "A botanical summary table features: '{0}'. The accurate entry is:",
            "Compare parenchyma modifications: '{0}' is accurately stated as:",
            "Which histological fact holds true for: '{0}'?:",
            "Select the correct pairing for: '{0}':",
            "In an analytical examination question: '{0}' is correctly described by:",
            "Evaluate the ground tissue specialization: '{0}':"
        ],
        'data': [
            ("Parenchyma vs Chlorenchyma vs Aerenchyma", "Parenchyma: generalized living ground tissue; Chlorenchyma: chloroplast-rich photosynthetic parenchyma; Aerenchyma: large air lacunae for buoyancy/gas transport", "All three share thin primary cellulose walls and living protoplasm", "Parenchyma is dead, Chlorenchyma has lignin, Aerenchyma lacks cytoplasm; All three possess thick secondary walls; Aerenchyma is found only in desert plants"),
            ("Primary wall chemistry across parenchyma", "Contains \\(\\approx 30\\%\\) cellulose, \\(\\approx 30\\%\\) hemicellulose, and \\(\\approx 35\\%\\) pectin, with zero secondary lignin", "High pectin content allows flexibility, hydration, and middle lamella adhesion", "Contains 90% secondary lignin, Made of chitin identical to fungi, Bounded by a peptidoglycan layer"),
            ("Metabolic versatility of parenchyma", "Can perform photosynthesis, storage, secretion, wound repair, solute transport, and dedifferentiation into meristems", "Acts as the metabolic powerhouse and developmental reservoir of the plant body", "Performs only water conduction like dead xylem, Dedicated solely to mechanical support like bone, Completely inactive metabolic state"),
            ("Location of chlorenchyma vs aerenchyma", "Chlorenchyma is abundant in leaf mesophyll and green stems; Aerenchyma is abundant in submerged roots, floating petioles, and wetland stems", "Reflects evolutionary adaptation to light capture versus aquatic hypoxia/buoyancy", "Chlorenchyma is found inside roots underground, Aerenchyma is found on dry cactus spines, Both are restricted to bark"),
            ("Presence of secondary cell walls in parenchyma", "Normal parenchyma strictly lacks secondary cell walls; certain specialized storage parenchyma (e.g., date palm endosperm) develop thick hemicellulose walls", "Hemicellulose in date palm endosperm serves as a mobilized nutrient reserve during germination", "All parenchyma cells have thick lignified secondary walls, Secondary walls are made of suberin only, Never occurs in any plant species"),
            ("Parenchyma in vascular tissues (Xylem & Phloem parenchyma)", "Living parenchyma cells embedded within vascular bundles: Xylem parenchyma stores starch/fat and assists radial conduction; Phloem parenchyma stores food and resins", "Xylem parenchyma is the ONLY living element in mature gymnosperm/angiosperm xylem", "Vascular parenchyma is dead and hollow, Performs rapid transpirational pull, Lacks protoplasm and nucleus"),
            ("Turgor-driven mechanical support", "When well-watered, osmotic inflow of water into parenchyma vacuoles generates internal hydrostatic pressure (turgor) pressing against cell walls", "Provides sufficient rigidity to keep herbaceous non-woody plants completely upright; loss of turgor causes wilting", "Turgor pressure causes cell walls to burst immediately, Operates only in dead woody trunks, Driven by gas pressure inside aerenchyma"),
            ("Symplastic vs Apoplastic pathways across parenchyma", "Symplastic movement proceeds through living protoplasm and plasmodesmata; Apoplastic movement proceeds through non-living cell walls and intercellular spaces", "Parenchyma facilitates both pathways until water reaches the impermeable Casparian strip in the endodermis", "Symplast passes through air chambers only, Apoplast requires ATP expenditure, Both pathways are identical"),
            ("Regeneration and grafting union formation", "When two plant stems are grafted together, living parenchyma cells from both stock and scion divide vigorously to form a connecting callus bridge", "Subsequently redifferentiates into continuous vascular cambium, xylem, and phloem, establishing vascular union", "Grafting succeeds through fusion of dead bark fibres, Successful grafting requires total absence of living cells, Dependent exclusively on root hairs"),
            ("Parenchyma role in tyloses formation", "Xylem parenchyma cells balloon through pit apertures into the lumens of inactive or damaged xylem vessels, forming plugs termed tyloses", "Blocks water flow and seals vessels against systemic spread of fungal pathogens and air embolisms", "Produces new secondary xylem vessels, Synthesizes chlorophyll inside heartwood, Dissolves tree trunks")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Parenchyma Modifications & Functional Roles.**\n- Generalized parenchyma (pith, cortex) \\(\\rightarrow\\) Chlorenchyma (mesophyll/photosynthesis) \\(\\rightarrow\\) Aerenchyma (lacunae/buoyancy/\\(\\text{O}_2\\)) \\(\\rightarrow\\) Storage parenchyma (starch, water, reserves).\n- Vascular parenchyma (Xylem parenchyma: only living xylem element; Phloem parenchyma: stores organic sap).\n\n**Step 2: Contrast '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Physiological Details:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 6: Quantitative & Biophysical Calculations on Parenchyma
    arch6 = {
        'templates': [
            "{0}:",
            "Calculate the parenchyma tissue cellular metric: {0}:",
            "A biophysical plant histology calculation: {0}:",
            "Quantitative ground tissue problem: {0}:",
            "Solve the quantitative parenchyma calculation: {0}:",
            "Analyze the numerical turgor and gas-volume calculation: {0}:",
            "Determine the correct calculated parameter: {0}:",
            "An analytical plant biophysics question: {0}:",
            "Find the accurate quantity for: {0}:",
            "Compute the following physiological quantity: {0}:"
        ],
        'data': [
            ("A spherical parenchyma cell has diameter \\(50\\text{ }\mu\\text{m}\\) (radius \\(r = 25\\text{ }\mu\\text{m}\\)). If its central vacuole occupies \\(80\\%\\) of the cell volume, what is the volume of the living cytoplasm and nucleus?", "\\(13,090\\text{ }\mu\\text{m}^3\\)", "Total cell volume \\(V = \\frac{4}{3}\\pi r^3 = \\frac{4}{3}\\pi (25)^3 \\approx 65,450\\text{ }\mu\\text{m}^3\\). Cytoplasm \\(= 20\\% \\times 65,450 = 13,090\\text{ }\mu\\text{m}^3\\)", "\\(52,360\\text{ }\mu\\text{m}^3\\), \\(6,545\\text{ }\mu\\text{m}^3\\), \\(26,180\\text{ }\mu\\text{m}^3\\)"),
            ("A floating leaf petiole of Eichhornia has total volume \\(12\\text{ cm}^3\\). If aerenchyma air lacunae make up \\(65\\%\\) of the petiole volume, what is the total volume of trapped air in this single petiole?", "\\(7.8\\text{ cm}^3\\)", "\\(\\text{Air volume} = 0.65 \\times 12\\text{ cm}^3 = 7.8\\text{ cm}^3\\)", "4.2 cm^3, 6.5 cm^3, 8.4 cm^3"),
            ("Given water density is \\(1.0\\text{ g/cm}^3\\), a plant tissue fragment with mass \\(4.0\\text{ g}\\) and volume \\(8.0\\text{ cm}^3\\) (containing extensive aerenchyma) has what average buoyant density, and will it float?", "Density \\(= 0.5\\text{ g/cm}^3\\); it will float vigorously", "\\(\\text{Density} = \\text{Mass} / \\text{Volume} = 4.0\\text{ g} / 8.0\\text{ cm}^3 = 0.5\\text{ g/cm}^3 < 1.0\\text{ g/cm}^3\\)", "Density = 2.0 g/cm^3; it will sink, Density = 1.0 g/cm^3; neutral buoyancy, Density = 0.8 g/cm^3; it will sink"),
            ("In a potato tuber, storage parenchyma cells contain \\(20\\%\\) starch by fresh weight. If starch density is \\(1.5\\text{ g/cm}^3\\), how much starch is present in a \\(250\\text{ g}\\) potato tuber?", "\\(50\\text{ g}\\) of starch", "\\(\\text{Starch mass} = 0.20 \\times 250\\text{ g} = 50\\text{ g}\\)", "25 g of starch, 100 g of starch, 75 g of starch"),
            ("A palisade chlorenchyma cell contains 50 chloroplasts. If each chloroplast fixes \\(2.0 \\times 10^{-14}\\text{ moles of }\\text{CO}_2\\) per hour under full sunlight, how many moles of \\(\\text{CO}_2\\) are fixed by \\(1.0 \\times 10^6\\) palisade cells in a leaf in 1 hour?", "\\(1.0 \\times 10^{-6}\\text{ moles of }\\text{CO}_2\\)", "\\(\\text{CO}_2\\text{ fixed} = 10^6 \\times 50 \\times (2.0 \\times 10^{-14}) = 1.0 \\times 10^{-6}\\text{ moles}\\)", "\\(1.0 \\times 10^{-5}\\text{ moles}\\), \\(5.0 \\times 10^{-7}\\text{ moles}\\), \\(2.0 \\times 10^{-6}\\text{ moles}\\)"),
            ("The water potential equation is \\(\\Psi_w = \\Psi_s + \\Psi_p\\). If a turgid parenchyma cell has an osmotic solute potential \\(\\Psi_s = -0.9\\text{ MPa}\\) and a turgor pressure potential \\(\\Psi_p = +0.7\\text{ MPa}\\), what is its net water potential \\(\\Psi_w\\)?", "\\(-0.2\\text{ MPa}\\)", "\\(\\Psi_w = -0.9\\text{ MPa} + 0.7\\text{ MPa} = -0.2\\text{ MPa}\\)", "+0.2 MPa, -1.6 MPa, 0.0 MPa"),
            ("When a parenchyma cell is fully turgid at equilibrium in pure water (\\(\\Psi_w = 0\\)), if its solute potential \\(\\Psi_s = -1.2\\text{ MPa}\\), what must be its turgor pressure potential \\(\\Psi_p\\)?", "\\(+1.2\\text{ MPa}\\)", "\\(\\Psi_w = 0 \\implies \\Psi_p = -\\Psi_s = -(-1.2) = +1.2\\text{ MPa}\\)", "-1.2 MPa, 0.0 MPa, +2.4 MPa"),
            ("A wetland root of length \\(20\\text{ cm}\\) has longitudinal aerenchyma channels with total cross-sectional area \\(0.05\\text{ cm}^2\\). What is the total volume of these continuous gas conduits?", "\\(1.0\\text{ cm}^3\\) (\\(1,000\\text{ mm}^3\\))", "\\(V = A \\times L = 0.05\\text{ cm}^2 \\times 20\\text{ cm} = 1.0\\text{ cm}^3 = 1,000\\text{ mm}^3\\)", "0.5 cm^3, 2.0 cm^3, 0.1 cm^3"),
            ("If a cubic block of cortex parenchyma measures \\(2\\text{ mm} \\times 2\\text{ mm} \\times 2\\text{ mm}\\) (volume \\(8\\text{ mm}^3\\)) and individual isodiametric parenchyma cells have diameter \\(50\\text{ }\mu\\text{m}\\) (volume \\(\\approx 6.54 \\times 10^{-5}\\text{ mm}^3\\)), approximately how many parenchyma cells are packed in this block (assuming 75% volume packing efficiency)?", "\\(\\approx 91,743\\text{ parenchyma cells}\\)", "\\(\\text{Effective volume} = 0.75 \\times 8\\text{ mm}^3 = 6.0\\text{ mm}^3\\). Cells \\(= 6.0 / (6.54 \\times 10^{-5}) \\approx 91,743\\)", "\\(\\approx 9,174\\), \\(\\approx 917,430\\), \\(\\approx 50,000\\)"),
            ("In an experiment, an apple flesh parenchyma cylinder lost \\(15\\%\\) of its weight when immersed in a \\(0.5\\text{ M}\\) sucrose solution. What physiological process caused this weight loss?", "Exosmosis of water from cell vacuoles due to hypertonic medium", "Water moves out down its chemical potential gradient from higher vacuolar potential to lower external potential, shrinking cell turgor", "Endosmosis of sucrose into cytoplasm, Active secretion of cell wall pectin, Decomposition of starch into gas")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Identify given physical and physiological values.**\n" + item[0] + "\n\n**Step 2: Apply the governing biophysical/water potential formula.**\n" + item[2] + ".\n\n**Step 3: Conclude.**\nResult is " + item[1] + "."
        ),
        'diff': 'hard'
    }

    # Arch 7: Experimental Protocols, Histochemistry, and Tissue Preparation
    arch7 = {
        'templates': [
            "Which laboratory staining procedure or microtechnique identifies: '{0}'?:",
            "In plant histology and pharmacognosy: '{0}' is detected using:",
            "What experimental protocol is used to demonstrate: '{0}'?:",
            "How do plant anatomists visualize: '{0}'?:",
            "A student prepares a temporary slide of leaf epidermis and mesophyll: '{0}'. What is observed?:",
            "Which microchemical reagent specifically stains: '{0}'?:",
            "In laboratory food testing and botany, '{0}' is confirmed by:",
            "What microscopic feature identifies: '{0}'?:",
            "Evaluate the laboratory protocol for: '{0}':",
            "Identify the standard histological stain utilized for: '{0}':"
        ],
        'data': [
            ("Iodine (IKI) test for starch in storage parenchyma", "Potassium iodide-iodine reagent reacts with helical amylose coils to produce an intense dark blue-black complex", "Standard microchemical test for amyloplasts in potato, banana, and cereal endosperm", "Stains lipids bright scarlet red, Dissolves starch into clear gas, Turns cellulose bright green"),
            ("Sudan III / Sudan IV staining of lipid droplets", "Lipophilic lysochrome diazo dyes that dissolve preferentially in intracellular oil bodies (oleosomes), staining fats bright orange/red", "Used to detect oil storage parenchyma in castor, peanut, and sunflower seeds", "Stains protein aleurone grains deep blue, Bleaches all lipid molecules, Stains nucleic acids purple"),
            ("Fast Green / Safranin differential staining", "Fast Green stains cellulose primary cell walls of parenchyma bright green; Safranin stains lignified secondary walls of xylem/sclerenchyma brilliant red", "Classic double-staining technique enabling instant visual differentiation between living parenchyma and dead mechanical tissues", "Stains all cells identical black, Dissolves parenchyma completely, Stains vacuolar sap yellow"),
            ("Polarized Light Microscopy of starch grains", "Shows a brilliant birefringent 'Maltese Cross' pattern centered on the hilum under crossed polars (polarisers at 90 degrees)", "Diagnostic for radial semicrystalline arrangement of amylopectin lamellae in ungelatinized starch", "Proves starch is completely amorphous, Visualizes chlorophyll autofluorescence, Shows cell walls are made of metal"),
            ("Maceration technique (Schultze's or Jeffrey's method)", "Treating plant tissue with nitric acid and potassium chlorate (or chromic/nitric acid mixture) to dissolve middle lamella pectin", "Separates individual intact parenchyma and fiber cells without tearing cell walls", "Fuses all cells into solid stone, Stains DNA with fluorescent dye, Burns all organic matter to ash"),
            ("Freehand sectioning with a pith / potato carrot support", "Sandwiching delicate herbaceous stems or leaves inside split elderberry pith or carrot cylinder to slice ultra-thin uniform cross-sections with a razor", "Crucial laboratory skill for preparing distortion-free temporary mounts of plant ground tissues", "Method for extracting plant DNA, Process for boiling roots in acid, Method for drying wood in ovens"),
            ("Ruthenium Red staining of pectin", "Cationic inorganic complex that selectively stains acidic pectins in the middle lamella and primary walls of parenchyma pink/red", "Differentiates pectin-rich collenchyma and parenchyma from non-pectin tissues", "Stains starch blue-black, Stains lignin cherry red, Bleaches plant pigments"),
            ("Plasmolysis observation in Rhoeo discolor leaf epidermal peel", "Mounting purple Rhoeo lower epidermis in 10% sucrose solution reveals shrinking of pink vacuolar sap away from primary cell wall", "Classic pedagogical experiment demonstrating living semi-permeable tonoplast membrane and exosmosis", "Cells explode violently due to turgor, Purple pigment turns bright yellow, Cell wall dissolves instantly"),
            ("Microscopic detection of calcium oxalate raphides", "Clearing leaf tissue in 5% KOH or chloral hydrate and examining under polarized light reveals bright, glowing needle clusters in idioblasts", "Used in pharmacognostical quality control to detect adulteration in herbal drugs", "Identifies bacterial contamination, Measures leaf chlorophyll concentration, Confirms presence of starch"),
            ("Fluorescence microscopy of chlorenchyma chlorophyll", "Under blue or ultraviolet excitation light (\\(\\approx 450\\text{ nm}\\)), chlorophyll pigments emit intense, deep autofluorescent red light (\\(\\approx 680\\text{ nm}\\))", "Allows precise spatial mapping of functional photosynthetic chloroplasts without any exogenous chemical dyes", "Emits green light like GFP, Absorbs all UV light without emission, Emits yellow light only in dead cells")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Histochemical & Microscopic Techniques.**\n- Selective stains reveal specific chemical constituents: Iodine (blue-black starch), Sudan III (red lipids), Fast Green (green cellulose), Safranin (red lignin), Ruthenium Red (pink pectin).\n- Rhoeo plasmolysis proves semi-permeability; polarized light reveals Maltese crosses on starch.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Laboratory / Analytical Principle:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 8: Economic Botany, Biotechnology & Agricultural Significance
    arch8 = {
        'templates': [
            "Which commercial product, crop trait, or industrial process relates to: '{0}'?:",
            "In agricultural biotechnology and economic botany: '{0}' is characterized by:",
            "What economic or industrial significance is associated with: '{0}'?:",
            "How does agriculture exploit: '{0}' for food production or post-harvest preservation?:",
            "A food scientist examines crop storage physiology: '{0}'. What is true?:",
            "Which agricultural trait is governed by: '{0}'?:",
            "What is the commercial value of: '{0}'?:",
            "Why is '{0}' critical in post-harvest biology and plant breeding?:",
            "What technological advancement utilizes: '{0}'?:",
            "Evaluate the agro-economic concept: '{0}':"
        ],
        'data': [
            ("Potato tuber dormancy and sprout inhibition", "Endogenous ABA and storage parenchyma quiescence maintain commercial potato dormancy; Chlorpropham (CIPC) or ethylene gas prevents sprouting in cold storage", "Prevents conversion of valuable storage starch into reducing sugars (cold sweetening) that cause brown acrylamide formation during frying", "Stimulates immediate rot by fungi, Causes instant germination into green leaves, Increases water content to 99%"),
            ("Pectin extraction from citrus peel parenchyma", "Citrus fruit albedo (white spongy mesocarp parenchyma) is the commercial industrial source of pectin used as a gelling agent in jams, jellies, and pharmaceuticals", "Exploits the exceptionally high galacturonic acid pectin content of parenchymal middle lamellae", "Commercial source of diesel fuel, Source of natural rubber latex, Used to manufacture synthetic plastics"),
            ("Crispness and texture in fruits and vegetables", "Crunchy crispness (in apples, celery, carrots) depends entirely on hydrostatic turgor pressure stretching primary parenchyma walls and middle lamella adhesion", "Post-harvest water loss or pectinase enzyme breakdown of middle lamellae causes softening, mealy texture, and wilting", "Determined by heavy deposits of silica in cells, Caused by air bubbles trapped in aerenchyma, Controlled by wood lignin content"),
            ("Sugarcane stem parenchyma (Saccharum officinarum)", "Massive ground tissue parenchyma cells in sugarcane stems store up to \\(15\\text{ to }20\\%\\) sucrose in their vacuolar sap", "Primary source of refined sucrose sugar, molasses, and bioethanol worldwide", "Stores starch grains in amyloplasts, Contains toxic tannins preventing extraction, Composed of dead lignified fibers"),
            ("Plant Tissue Culture Callus (Totipotency in action)", "Explanted storage or ground parenchyma dedifferentiates into rapidly dividing totipotent callus on nutrient agar containing 2,4-D and kinetin", "Enables micropropagation of millions of disease-free orchids, bananas, and oil palms from microscopic tissue samples", "Requires whole intact mature trees, Callus cells cannot regenerate organs, Process limited to dead wood"),
            ("Ethylene-induced ripening of fleshy fruits (Climacteric fruits)", "Ethylene triggers expression of polygalacturonase and cellulase, which hydrolyze middle lamellae between parenchyma cells, softening the fruit", "Coupled with enzymatic breakdown of storage starch into sweet sucrose and fructose (e.g., in bananas, mangoes, tomatoes)", "Causes fruit to become rock-hard like wood, Completely stops all cellular respiration, Prevents fruit from changing color"),
            ("Aloe vera gel parenchymal parenchyma", "Clear, viscous inner leaf parenchyma stores acetylated glucomannans (acemannan), vitamins, and glycoproteins", "Extensively utilized in dermatology, cosmetics, and wound-healing ointments for its soothing and anti-inflammatory properties", "Source of industrial motor oil, Toxic poison causing severe necrosis, Pure crystalline starch paste"),
            ("Sweet potato storage root (Ipomoea batatas)", "Modified adventitious storage root whose parenchyma stores massive quantities of starch and beta-carotene (provitamin A)", "Critical staple biofortified food crop combating childhood blindness (xerophthalmia) in developing nations", "Stem tuber derived from shoot apex, Storage organ composed entirely of cork, Non-edible toxic weed"),
            ("Delayed softening in 'Flavr Savr' tomato", "First genetically engineered commercial crop (1994), engineered with antisense RNA against polygalacturonase to prevent pectin degradation in fruit parenchyma", "Prolonged vine-ripened flavor and shelf-life without premature rotting or soft collapse during shipping", "Produced tomatoes with blue skin, Eliminated all seeds from fruit, Made tomato plants resistant to drought"),
            ("Controlled Atmosphere (CA) Storage for Apples", "Storing apples in \\(1\\text{ to }2\\%\\text{ }\\text{O}_2\\), \\(1\\text{ to }3\\%\\text{ }\\text{CO}_2\\), and \\(0\\text{ to }4^\\circ\\text{C}\\) slows respiration in flesh parenchyma by 80%", "Extends marketability and crisp turgidity of harvested apples for up to 12 months without chemical preservatives", "Causes immediate fermentation and spoilage, Freezes apples into solid ice crystals, Depletes all sugars from fruit")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Agricultural & Economic Applications of Parenchyma.**\n- Food reserves: Potato (starch), Sugarcane (sucrose), Legumes (protein), Citrus peel (pectin).\n- Texture & post-harvest: Turgor drives crispness; pectinase/polygalacturonase degrades middle lamella during ripening.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Commercial / Biotechnological Impact:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-3-3.1.2", "Parenchyma (storage, aerenchyma, chlorenchyma)", archs)


# ==========================================
# 3.1.3: Collenchyma (flexibility), Sclerenchyma (lignified walls)
# ==========================================
def gen_3_1_3():
    # Arch 1: Collenchyma Histology, Wall Pectins & Plastic Flexibility
    arch1 = {
        'templates': [
            "What distinct histological and mechanical property defines: '{0}'?:",
            "In living mechanical tissues: '{0}' is characterized by:",
            "Consider collenchyma tissue architecture: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A plant anatomist examines sub-epidermal mechanical support: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' impart tensile strength without restricting organ growth?:",
            "Evaluate the cellular feature: '{0}'. Its biological role is:",
            "Why is '{0}' termed the 'living mechanical tissue' of growing plant organs?:",
            "What structural property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Collenchyma living state and protoplasm", "Living at maturity, containing active cytoplasm, nucleus, vacuole, and often functional chloroplasts", "Provides mechanical support while retaining metabolic activity, osmotic responsiveness, and growth capacity", "Dead at maturity lacking all protoplasm, Non-living empty tubes filled with air, Enucleated cells lined with suberin"),
            ("Collenchyma cell wall composition", "Unevenly thickened primary cell wall composed of cellulose, hemicellulose, and exceptionally high pectin content (\\(\\approx 45\\%\\)), strictly lacking lignin", "High hydration and pectin content confer tensile strength combined with high plastic flexibility", "Uniformly thickened secondary wall impregnated with heavy lignin, Thin wall made of peptidoglycan, Wall made of suberin and wax"),
            ("Uneven wall thickenings at cell corners", "Localized thickening occurs predominantly at cell junctions (corners) where three or more cells meet", "Reinforces the tissue against tensile mechanical stress while leaving thin areas for transport", "Thickened uniformly like a concentric cylinder, Thickened only on the inner periclinal face, Thickenings are made of silica crystals"),
            ("Sub-epidermal hypodermal distribution in dicot stems", "Occurs in continuous cylinders or discrete longitudinal ribs directly beneath the epidermis in young dicotyledonous stems and petioles", "Forms peripheral reinforcing girders maximizing resistance to bending forces caused by wind", "Located in the deepest core of the central pith, Found exclusively on root tips, Forms the inner lining of seed coats"),
            ("Tensile strength and bending flexibility", "Imparts remarkable tensile strength, allowing slender stems and petioles to bend vigorously in strong winds without snapping", "Acts like flexible mechanical cables supporting growing organs", "Makes stems brittle causing them to shatter in wind, Prevents any bending making stems rock-hard, Causes stems to collapse under their own weight"),
            ("Absence of collenchyma in roots and monocots", "Completely absent in almost all roots (underground organs do not experience wind bending) and typically absent in monocot stems", "Monocots rely instead on early-differentiating sclerenchyma fiber girders for mechanical support", "Present as thick layers in all root tips, Abundant in monocot pith, Replaces all xylem in desert roots"),
            ("Collenchyma in leaf petioles (e.g., Celery / Apium)", "The prominent, stringy, ribbed strands running along celery petioles consist of dense collenchyma bundles", "Classic dietary and anatomical example of living tensile collenchyma strands", "Strands of pure dead xylem wood, Strands of stinging hair idioblasts, Bundles of fungal hyphae"),
            ("Elongation capacity during organ growth", "Because collenchyma cell walls are unlignified and plastic, they can stretch and expand longitudinally as the young organ continues to grow", "Unlike rigid lignified sclerenchyma, collenchyma does not arrest organ elongation", "Permanently freezes stem length upon formation, Shrinks the stem as it ages, Causes premature organ shedding"),
            ("Chloroplast presence in collenchyma", "Cells frequently contain chloroplasts and can perform secondary photosynthesis in young stems and petioles", "Visible as green hypodermal ribs in angular herbaceous stems (e.g., Cucurbita)", "Completely devoid of plastids, Contains only dark brown tannin crystals, Filled with starch amyloplasts only"),
            ("Hydration and wall water content", "Collenchyma cell walls possess extremely high water content (over \\(60\\%\\) of fresh wall weight) due to hydrophilic pectins", "Water acts as a structural plasticizer, imparting flexibility and high fracture toughness", "Walls are completely dry and anhydrous, Hydrophobic walls repelling all moisture, Water is replaced by liquid resin")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Collenchyma Tissue Biology.**\n- Living mechanical tissue of young, growing organs (petioles, young dicot stems, leaf veins).\n- Unevenly thickened primary cellulose + pectin walls (no lignin); plastic flexibility allows bending without snapping and does not impede elongation.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Mechanical / Anatomical Detail:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 2: Collenchyma Morphological Types (Angular, Lacunar, Lamellar)
    arch2 = {
        'templates': [
            "Which anatomical description and representative example matches: '{0}'?:",
            "In the histological classification of collenchyma: '{0}' is characterized by:",
            "Consider collenchyma wall thickening patterns: '{0}' exhibits:",
            "Which statement precisely describes the structure of: '{0}'?:",
            "A botanist examines a stem cross-section under microscopy: '{0}'. What is seen?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' distribute mechanical reinforcement across the hypodermis?:",
            "Evaluate the specialized collenchyma subtype: '{0}':",
            "Why is '{0}' classified under this specific morphological category?:",
            "What architectural feature defines: '{0}'?:"
        ],
        'data': [
            ("Angular Collenchyma", "Thickenings localized heavily at the cell angles/corners where three or more cells meet; intercellular spaces are completely absent", "Most common collenchyma type; found in stems of Cucurbita (pumpkin), Solanum tuberosum (potato), and Datura", "Thickenings on tangential walls only, Large intercellular spaces with thickenings on cavity walls, Thickened uniformly with bordered pits"),
            ("Lamellar (Plate / Tangential) Collenchyma", "Thickenings localized predominantly on the tangential (inner and outer) cell walls, while radial walls remain thin", "Cells appear arranged in regular horizontal plates or bands; found in stems of Sambucus (elderberry), Helianthus (sunflower), and Eupatorium", "Thickenings restricted strictly to cell corners, Intercellular cavities filled with air, Spiral lignified bands on inner walls"),
            ("Lacunar (Lacunate) Collenchyma", "Thickenings localized specifically on the cell wall surfaces bordering prominent intercellular spaces", "Possesses distinct intercellular spaces (lacunae); found in petioles of Petasites, stems of Malva, and aerial roots of Ficus", "Lacks intercellular spaces completely, Thickened only at outer tangential faces, Cells are dead and hollow"),
            ("Annular Collenchyma", "Cell wall thickenings are uniformly deposited around the entire perimeter, giving the cell lumen a circular or oval outline in cross-section", "Derived by progressive thickening from angular collenchyma; found in petioles of Nerium and Viscum", "Thickenings shaped like sharp needle crystals, Walls thickened only on radial faces, Walls contain thick rings of lignin"),
            ("Hypodermis of Cucurbita stem", "Angular collenchyma forms prominent sub-epidermal ridges/girders corresponding to the five external stem ribs", "Provides exceptional resistance against twisting (torsional) and bending mechanical forces", "Composed of dead lignified stone cells, Composed of water-storing aerenchyma, Formed by multi-layered suberized cork"),
            ("Collenchyma in Apium graveolens (Celery)", "Forms massive discrete longitudinal strands of angular collenchyma beneath the petiole ridges", "Classic demonstration material where peeled strands show extreme elastic extension and tensile recovery", "Strands of pure secondary xylem vessels, Solid cords of dead sclereids, Formed by aerenchyma lacunae"),
            ("Collenchyma in Helianthus (Sunflower) stem", "Lamellar collenchyma forms a continuous 3 to 5 layer hypodermal band beneath the stem epidermis", "Strengthens young expanding sunflower stems before secondary woody growth initiates", "Contains massive dead stone cells, Lacks cell walls and forms a syncytium, Consists of single-celled hairs"),
            ("Distinction between Collenchyma and Sclerenchyma in polarization", "Collenchyma walls display distinct optical birefringence under polarized light due to alternating lamellae of cellulose and pectin, but remain living", "Sclerenchyma displays intense secondary wall birefringence and lacks living protoplasm", "Collenchyma is completely isotropic and non-birefringent, Sclerenchyma does not polarize light, Both tissues are chemically identical"),
            ("Collenchyma response to mechanical stress (Thigmomorphogenesis)", "Wind exposure or mechanical flexing induces rapid upregulation of cell wall synthesis, increasing collenchyma wall thickness and organ girth", "Classic adaptive thigmomorphogenetic response ensuring survival in exposed environments", "Wind induces immediate cell lysis and death, Causes leaves to drop off within 10 seconds, Inhibits all cellulose synthesis"),
            ("Transitional nature of collenchyma", "In certain mature perennial organs, collenchyma cells can undergo secondary lignification and transform into permanent sclerenchyma", "Demonstrates the developmental plasticity between primary living ground tissues and secondary mechanical tissues", "Transforms into photosynthetic chlorenchyma only, Converts directly into sieve tube elements, Dissolves into empty air chambers")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Collenchyma Morphological Types.**\n- Angular: Corner thickenings, no intercellular spaces (Cucurbita, Solanum).\n- Lamellar: Tangential wall thickenings, plate-like (Sambucus, Helianthus).\n- Lacunar: Thickenings bordering intercellular spaces (Petasites, Malva).\n- Annular: Uniformly thickened circular lumen (Nerium).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Histological / Diagnostic Feature:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 3: Sclerenchyma Fibres (Structure, Lignification, Pits, Commercial Bast Fibres)
    arch3 = {
        'templates': [
            "What distinct anatomical and physical feature defines: '{0}'?:",
            "In dead plant mechanical tissues: '{0}' is characterized by:",
            "Consider sclerenchyma fiber architecture: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A textile botanist analyzes commercial plant fibers: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' impart rigid structural support to mature plant axes?:",
            "Evaluate the cellular feature: '{0}'. Its economic or biological role is:",
            "Why is '{0}' dead at maturity with narrow lumen?:",
            "What structural property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Sclerenchyma Fibres Definition", "Long, slender, narrow, spindle-shaped cells with pointed tapering ends and thick, heavily lignified secondary cell walls", "Dead at maturity, lacking protoplasm and nucleus; possesses an extremely narrow central lumen", "Living isodiametric cells with thin cellulose walls, Short spherical cells containing starch, Unlignified cells storing water"),
            ("Lignin deposition and dead state at maturity", "Secondary cell walls are impregnated with hydrophobic polyphenol lignin polymers, cutting off water and metabolite diffusion", "Protoplasm degenerates completely, leaving an empty hollow lumen dedicated entirely to rigid mechanical support", "Lignin synthesis keeps the cell living for 500 years, Cells divide rapidly by mitosis, Lignin dissolves in water during rain"),
            ("Pit architecture in sclerenchyma fibres", "Possess simple, oblique, slit-like pits or small circular pits traversing the thick secondary cell walls", "Remnants of primary pit fields through which plasmodesmata once connected living sister cells", "Large bordered pits with toruses like conifer tracheids, Open perforations devoid of pit membranes, Pits filled with living cytoplasm"),
            ("Bast fibres (Phloem / Cortical fibres)", "Extraxylary sclerenchyma fibres located in the phloem or pericycle of dicot stems (e.g., Jute, Flax, Hemp)", "Highly prized commercially for spinning into burlap, linen cloth, ropes, and twine", "Fibres found inside root caps, Fibres lining the interior of fruits, Xylem vessels conducting mineral sap"),
            ("Flax fibres (Linum usitatissimum / Linen)", "Bast fibres with exceptionally thick walls, narrow lumen, and low lignin content (predominantly crystalline cellulose)", "Possess immense tensile strength and softness, used for manufacturing fine linen textiles and archival paper", "Extremely brittle fibres that cannot be woven, Coarse rough fibres used only for stuffing mattresses, Highly lignified rough wood fibres"),
            ("Jute fibres (Corchorus capsularis)", "Commercial bast fibres obtained from secondary phloem, moderately lignified, coarse, and golden-brown", "Used globally for manufacturing gunny sacks, hessian bags, ropes, and carpet backings", "Softest white fiber used for surgical cotton, Pure protein fibers like silk, Fibres obtained from leaf epidermal hairs"),
            ("Hemp (Cannabis sativa) and Ramie (Boehmeria nivea) fibres", "Hemp provides rugged, rot-resistant bast fibres for marine ropes; Ramie provides the longest (up to \\(55\\text{ cm}\\)) and strongest known plant fibres", "Exceptional resistance to microbial decay and saltwater degradation", "Shortest microscopic fibres in plants, Dissolve instantly in water, Fibres obtained from fruit pulp"),
            ("Surface fibres (e.g., Cotton - Gossypium)", "Cotton fibres are NOT true sclerenchyma fibres; they are unicellular epidermal seed coat hairs composed of pure (\\(\\approx 90\\%\\)) unlignified cellulose", "Unlike dead lignified bast fibres, cotton fibers are soft, absorbent, and unlignified", "Heavily lignified dead bast fibres from phloem, Multicellular branched sclereids, Derived from secondary wood"),
            ("Coir fibres (Cocos nucifera / Coconut husk)", "Coarse, highly lignified sclerenchyma fibres obtained from the fibrous mesocarp of the coconut fruit", "Possess exceptional elasticity, water-resistance, and buoyancy; used for ropes, mats, brushes, and soil-less potting medium", "Pectocellulosic collenchyma from coconut leaves, Endosperm storage tissue, Soft cotton-like seed hairs"),
            ("Tensile strength comparison of sclerenchyma", "High-grade sclerenchyma fibres exhibit tensile strength comparable to steel wire (up to \\(100\\text{ kg/mm}^2\\)) combined with low density", "Enables tall tree canopies and slender bamboo culms to withstand hurricane-force winds without buckling", "Ten times weaker than gelatin, Brittle like glass shattering under light pressure, Loses all strength when dry")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Sclerenchyma Fibre Anatomy.**\n- Dead mechanical tissue with heavily lignified secondary cell walls, narrow lumen, and tapering ends.\n- Extraxylary bast fibres (Jute, Flax, Hemp) provide massive tensile strength and commercial textile utility.\n- Note: Cotton is unicellular epidermal seed hair (cellulose), NOT a lignified sclerenchyma fibre.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Commercial / Mechanical Detail:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Sclerenchyma Sclereids (Stone Cells, Types, Fruit Grittiness)
    arch4 = {
        'templates': [
            "What morphological shape and anatomical role defines: '{0}'?:",
            "In plant mechanical tissues and seed protection: '{0}' is characterized by:",
            "Consider sclereid architecture: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A food scientist analyzes the grittiness of pears: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' protect plant seeds or stiffen leaf laminas?:",
            "Evaluate the cellular feature: '{0}'. Its biological role is:",
            "Why is '{0}' categorized as a sclerenchymatous stone cell?:",
            "What structural property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Sclereids (Stone Cells) Definition", "Short, isodiametric, spherical, or irregular cells with extremely thick, heavily lignified secondary walls and branched canal-like pits", "Dead at maturity with an obliterated or tiny central lumen; provide rigid protective hardness", "Long spindle-shaped cells with living nuclei, Living cells containing chloroplasts, Thin-walled storage cells"),
            ("Brachysclereids (Stone cells in Pear & Guava)", "Short, roughly isodiametric sclereids with thick secondary walls and radiating branched pit canals", "Responsible for the characteristic gritty crunch when eating ripe pears (Pyrus), guavas (Psidium), and sapota", "Soft gelatinous cells full of sugar, Air-filled floating cells, Fibres used for spinning yarn"),
            ("Macrosclereids (Rod cells in legume seed coats)", "Columnar, rod-like elongated sclereids arranged in a palisade-like layer in legume seed coats (e.g., Pea, Bean)", "Imparts mechanical toughness and water impermeability to the protective testa (seed coat)", "Star-shaped cells in water lilies, Spherical cells in pear pulp, Living cells in root tips"),
            ("Osteosclereids (Bone cells / Prop cells)", "Bone-shaped or dumbbell-shaped sclereids with enlarged, lobed, or knobbed ends", "Found in seed coats of Pisum (pea) and leaves of Hakea, providing compressive resistance", "Columnar cells with smooth ends, Needle-shaped crystal cells, Hair-like branched trichomes"),
            ("Astrosclereids (Star-shaped sclereids)", "Deeply lobed, star-shaped sclereids with radiating pointed arms protruding into intercellular air spaces", "Stiffens leaf blades and petioles of floating water plants (e.g., Nymphaea / Water Lily) and Tea (Camellia sinensis)", "Isodiametric round cells in potato, Rod-like cells in wood, Cells producing essential oils"),
            ("Trichosclereids (Internal hair-like sclereids)", "Extremely elongated, hair-like or needle-like branched sclereids projecting into intercellular spaces", "Found in aerial roots of Monstera and leaves of olive (Olea), providing internal mechanical bracing against collapse", "External glandular hairs secreting nectar, Soft cotton fibers on seeds, Root hairs absorbing soil water"),
            ("Seed coat hardness in nuts (e.g., Walnut, Coconut, Almond)", "The impenetrable, rock-hard endocarp shells of walnuts, coconuts, peach stones, and hazelnuts consist of solid sheets of interlocking sclereids", "Protects the delicate embryonic seed from predatory herbivores, insects, and physical crushing", "Made of frozen water crystals, Composed of living suberized cork, Formed by fibrous phloem cells"),
            ("Branched pit canals (Ramiform pits) in sclereids", "Deep, canal-like pit cavities that branch repeatedly as they traverse the immensely thick secondary wall", "Formed because the inner wall layers have much smaller surface area than outer layers during progressive wall deposition", "Channels through which cytoplasm actively circulates, Pores that secrete digestive enzymes, Holes drilled by parasitic fungi"),
            ("Sclereids in Tea leaves (Camellia sinensis)", "Astrosclereids and osteosclereids scattered throughout the mesophyll stiffen the leaf lamina", "Used in pharmacognosy as diagnostic microscopic markers to detect adulteration in commercial tea powders", "Produce caffeine in their lumen, Absorb water vapor from fog, Convert sunlight into starch"),
            ("Secondary wall lignification chemistry", "Lignin is an irregular, three-dimensional, cross-linked aromatic polymer of monolignols (coniferyl, sinapyl, p-coumaryl alcohols)", "Covalently cross-links cellulose microfibrils, creating an impenetrable composite material resistant to enzymatic degradation", "Simple linear sugar polymer like starch, Soluble protein chain synthesized in ribosomes, Liquid fatty acid layer")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Sclerenchyma Sclereid (Stone Cell) Anatomy.**\n- Short, isodiametric or branched dead cells with immensely thick lignified walls and branched pit canals (ramiform pits).\n- Types: Brachysclereids (gritty stone cells in pear/guava), Macrosclereids (rod cells in legume testa), Osteosclereids (bone-shaped in pea seeds), Astrosclereids (star-shaped in Nymphaea/Tea), Trichosclereids (internal hair-like in Monstera).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Diagnostic / Protective Detail:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 5: Comparative Matrix: Parenchyma vs Collenchyma vs Sclerenchyma
    arch5 = {
        'templates': [
            "Which row in the comparative table correctly contrasts: '{0}'?:",
            "In comparing the three simple permanent plant tissues: '{0}' is characterized by:",
            "Consider mechanical tissue differences: '{0}' demonstrates that:",
            "Which statement presents a 100% accurate contrast: '{0}'?:",
            "A botanical summary matrix features: '{0}'. The accurate entry is:",
            "Compare Collenchyma and Sclerenchyma: '{0}' is accurately stated as:",
            "Which comparative histological fact holds true for: '{0}'?:",
            "Select the correct pairing for: '{0}':",
            "In an analytical examination question: '{0}' is correctly described by:",
            "Evaluate the simple permanent tissue criteria: '{0}':"
        ],
        'data': [
            ("Living state at functional maturity", "Parenchyma: Living; Collenchyma: Living; Sclerenchyma: Dead (lacks protoplasm at maturity)", "Parenchyma and collenchyma retain active metabolic cytoplasm, whereas sclerenchyma is purely mechanical corpse", "All three tissues are dead at maturity, Parenchyma is dead while sclerenchyma is living, Collenchyma is dead while parenchyma is living"),
            ("Cell wall chemical composition", "Parenchyma: Thin primary cellulose + pectin; Collenchyma: Uneven primary cellulose + high pectin (no lignin); Sclerenchyma: Thick secondary wall heavily lignified", "Lignin presence is the definitive diagnostic boundary separating sclerenchyma from collenchyma and parenchyma", "All three tissues contain heavy secondary lignin, Collenchyma contains chitin while sclerenchyma contains suberin, Parenchyma wall is made of peptidoglycan"),
            ("Mechanical support mechanism", "Parenchyma: Hydrostatic turgor pressure; Collenchyma: Plastic tensile flexibility (bending); Sclerenchyma: Rigid compressive and tensile strength (wood/fibres)", "Matches the developmental requirements of unexpanded vs expanding vs fully mature plant organs", "Parenchyma provides rigid wooden support, Collenchyma causes brittleness, Sclerenchyma provides hydrostatic support"),
            ("Intercellular spaces", "Parenchyma: Present (often large); Collenchyma: Absent or small (angular lacks spaces); Sclerenchyma: Completely absent", "Dense packing in collenchyma and sclerenchyma maximizes mechanical girder efficiency", "Parenchyma has no spaces, Sclerenchyma has giant air chambers, Collenchyma has open water canals"),
            ("Lumen diameter and cell shape", "Parenchyma: Large lumen, isodiametric; Collenchyma: Medium lumen, elongated prismatic; Sclerenchyma: Obliterated or very narrow lumen, spindle fibres or stone cells", "Progressive centripetal wall deposition in sclerenchyma almost obliterates the cell cavity", "Sclerenchyma has the widest lumen in plants, Parenchyma has no lumen, Collenchyma has star-shaped lumens only"),
            ("Location across the plant body", "Parenchyma: Ubiquitous ground tissue (cortex, pith, mesophyll); Collenchyma: Sub-epidermal hypodermis of dicot stems/petioles (absent in roots/monocots); Sclerenchyma: Vascular bundles, pericycle, seed coats, nutshells", "Reflects external wind bending forces on stems versus internal structural bracing of vascular cylinders", "Collenchyma is found only in roots, Sclerenchyma is found only in flowers, Parenchyma is restricted to wood"),
            ("Elasticity vs Plasticity", "Collenchyma exhibits Plastic deformation (stretches permanently during growth); Sclerenchyma exhibits Elastic deformation (rebounds after bending, snaps if limit exceeded)", "Plasticity of collenchyma allows organs to elongate without tearing mechanical supports", "Collenchyma shatters immediately like glass, Sclerenchyma stretches indefinitely, Both are completely rigid and non-deformable"),
            ("Pits and Pit canals", "Parenchyma: Simple primary pit fields; Collenchyma: Simple thin areas; Sclerenchyma: Narrow slit-like pits or deeply branched ramiform pit canals", "Branching pit canals in sclereids result from thick secondary wall deposition", "Parenchyma has bordered pits with toruses, Sclerenchyma lacks pits entirely, Collenchyma has open holes"),
            ("Response to growth hormones (Auxin / Gibberellin)", "Parenchyma and collenchyma respond to auxin and expand; Mature sclerenchyma cannot respond because cells are dead and walls are rigid", "Enables ongoing developmental plasticity in living primary tissues", "Sclerenchyma doubles in size every day with auxin, Collenchyma is killed by auxin, Parenchyma shrinks in response to gibberellins"),
            ("Taxonomic distribution", "Parenchyma: All plant groups (bryophytes to angiosperms); Collenchyma: Predominantly dicotyledons (rare in monocots/gymnosperms); Sclerenchyma: All vascular plants (pteridophytes, gymnosperms, angiosperms)", "Collenchyma is an evolutionary specialization of fast-growing herbaceous dicot shoots", "Collenchyma is found only in conifers, Sclerenchyma is found only in algae, Parenchyma occurs only in flowering plants")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Definitive Comparative Histology.**\n- Parenchyma: Living, thin primary wall (cellulose/pectin), turgor support, storage/photosynthesis.\n- Collenchyma: Living, uneven primary wall (cellulose/high pectin, NO lignin), plastic tensile flexibility, sub-epidermal hypodermis.\n- Sclerenchyma: Dead at maturity, thick secondary wall (heavily lignified), narrow lumen, rigid elastic strength (fibres & sclereids).\n\n**Step 2: Contrast '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Diagnostic / Evolutionary Criterion:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 6: Quantitative & Mechanical Problems in Plant Biomechanics
    arch6 = {
        'templates': [
            "{0}:",
            "Calculate the mechanical or anatomical parameter: {0}:",
            "A biomechanical plant histology calculation: {0}:",
            "Quantitative plant mechanics problem: {0}:",
            "Solve the quantitative mechanical tissue calculation: {0}:",
            "Analyze the numerical fiber tensile strength problem: {0}:",
            "Determine the correct calculated mechanical quantity: {0}:",
            "An analytical plant biophysics calculation: {0}:",
            "Find the correct quantitative result: {0}:",
            "Compute the following structural parameter: {0}:"
        ],
        'data': [
            ("A single sclerenchyma bast fiber bundle has a cross-sectional area of \\(0.2\\text{ mm}^2\\). If the ultimate tensile strength of the fiber is \\(600\\text{ MPa}\\) (\\(600\\text{ N/mm}^2\\)), what is the maximum tensile force this bundle can support before breaking?", "\\(120\\text{ N}\\) (equivalent to \\(\\approx 12.2\\text{ kg}\\) hanging mass)", "\\(F = \\text{Stress} \\times \\text{Area} = 600\\text{ N/mm}^2 \\times 0.2\\text{ mm}^2 = 120\\text{ N}\\). Mass \\(= 120 / 9.8 \\approx 12.2\\text{ kg}\\)", "1,200 N, 12 N, 60 N"),
            ("A cylindrical sclerenchyma fiber has an outer radius \\(R = 10\\text{ }\mu\\text{m}\\) and an inner lumen radius \\(r = 2\\text{ }\mu\\text{m}\\). What percentage of the fiber's cross-sectional area is occupied by the thick lignified secondary cell wall?", "\\(96\\%\\)", "Wall area \\(= \\pi (R^2 - r^2) = \\pi (100 - 4) = 96\\pi\\). Total area \\(= \\pi R^2 = 100\\pi\\). Percentage \\(= (96\\pi / 100\\pi) \\times 100 = 96\\%\\)", "80%, 90%, 99%"),
            ("A hollow circular collenchyma cell has outer diameter \\(30\\text{ }\mu\\text{m}\\) and lumen diameter \\(20\\text{ }\mu\\text{m}\\). What is the ratio of wall area to lumen area?", "\\(1.25\\)", "Wall area \\(= \\pi (15^2 - 10^2) = \\pi (225 - 100) = 125\\pi\\). Lumen area \\(= \\pi (10^2) = 100\\pi\\). Ratio \\(= 125 / 100 = 1.25\\)", "0.80, 2.25, 1.50"),
            ("A hemp rope made of twisted sclerenchyma bast fibers has a cross-sectional fiber area of \\(15\\text{ mm}^2\\). Given a safety working load factor of 4 and ultimate tensile strength of \\(800\\text{ N/mm}^2\\), what is the maximum safe working load in Newtons?", "\\(3,000\\text{ N}\\)", "\\(\\text{Ultimate Load} = 15 \\times 800 = 12,000\\text{ N}\\). Safe working load \\(= 12,000 / 4 = 3,000\\text{ N}\\)", "12,000 N, 6,000 N, 1,500 N"),
            ("In an angular collenchyma tissue, cell corners have a wall thickness of \\(8.0\\text{ }\mu\\text{m}\\), while the mid-region of the walls has a thickness of \\(1.6\\text{ }\mu\\text{m}\\). What is the ratio of corner thickening to mid-wall thickness?", "\\(5.0\\)", "\\(\\text{Ratio} = 8.0 / 1.6 = 5.0\\)", "2.5, 4.0, 10.0"),
            ("A microscopic field reveals 240 cells in a stem hypodermal layer. If 180 cells are collenchyma and 60 cells are parenchyma, what percentage of the hypodermis consists of collenchyma?", "\\(75\\%\\)", "\\(\\text{Percentage} = (180 / 240) \\times 100 = 75\\%\\)", "60%, 80%, 50%"),
            ("A ramie sclerenchyma fiber reaches a length of \\(500\\text{ mm}\\) (\\(50\\text{ cm}\\)) and a diameter of \\(50\\text{ }\mu\\text{m}\\) (\\(0.05\\text{ mm}\\)). What is the aspect ratio (length-to-diameter ratio) of this fiber?", "\\(10,000 : 1\\)", "\\(\\text{Aspect ratio} = 500\\text{ mm} / 0.05\\text{ mm} = 10,000\\)", "1,000 : 1, 100,000 : 1, 5,000 : 1"),
            ("Young's modulus (stiffness) of dry sclerenchyma fiber is \\(E_1 = 30\\text{ GPa}\\), whereas Young's modulus of turgid collenchyma is \\(E_2 = 2\\text{ GPa}\\). How many times stiffer is the lignified sclerenchyma fiber compared to the living collenchyma tissue?", "\\(15\\text{ times stiffer}\\)", "\\(\\text{Ratio} = E_1 / E_2 = 30 / 2 = 15\\)", "60 times, 150 times, 5 times"),
            ("If a microscopic stone cell (brachysclereid) has spherical diameter \\(40\\text{ }\mu\\text{m}\\) and its hollow central lumen has diameter \\(4\\text{ }\mu\\text{m}\\), what fraction of the total cell volume is occupied by the thick lignified secondary wall?", "\\(99.9\\%\\) (\\(999/1000\\))", "Total volume \\(\\propto 40^3 = 64,000\\). Lumen volume \\(\\propto 4^3 = 64\\). Wall volume \\(\\propto 64,000 - 64 = 63,936\\). Fraction \\(= 63,936 / 64,000 = 0.999 = 99.9\\%\\)", "90.0%, 95.0%, 99.0%"),
            ("A stem experiences a bending moment \\(M = 0.5\\text{ N}\\cdot\\text{m}\\). If peripheral collenchyma bands increase the second moment of area \\(I\\) of the stem by \\(400\\%\\) (5-fold), by what factor is the maximum bending stress reduced?", "Reduced to \\(1/5\\) (by \\(80\\%\\))", "Bending stress \\(\\sigma = My / I\\). If \\(I\\) increases by 5-fold, stress \\(\\sigma\\) decreases to \\(1/5\\) (an 80% reduction in stress)", "Reduced to 1/2, Reduced to 1/10, Stress increases 5-fold")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Identify given physical and geometrical variables.**\n" + item[0] + "\n\n**Step 2: Apply the governing mechanical/geometric formulation.**\n" + item[2] + ".\n\n**Step 3: Conclude.**\nResult is " + item[1] + "."
        ),
        'diff': 'hard'
    }

    # Arch 7: Histochemical Staining, Maceration & Textile Diagnostics
    arch7 = {
        'templates': [
            "Which histochemical reagent or microchemical test identifies: '{0}'?:",
            "In textile fiber forensics and pharmacognosy: '{0}' is confirmed by:",
            "What experimental protocol is used to distinguish: '{0}'?:",
            "How do plant histologists differentiate between: '{0}'?:",
            "A forensic analyst examines an unknown commercial plant fiber: '{0}'. What is observed?:",
            "Which staining reaction specifically characterizes: '{0}'?:",
            "In laboratory microtechnique, '{0}' is isolated or prepared by:",
            "What microscopic reaction confirms: '{0}'?:",
            "Evaluate the diagnostic staining protocol for: '{0}':",
            "Identify the standard microchemical test utilized for: '{0}':"
        ],
        'data': [
            ("Phloroglucinol-HCl (Wiesner test) for lignin in sclerenchyma", "Phloroglucinol in concentrated HCl reacts specifically with coniferyl aldehyde groups in lignin, turning sclerenchyma bright cherry-red / magenta", "Collenchyma and parenchyma remain unstained (green/colorless), providing foolproof diagnostic differentiation", "Turns cellulose bright blue, Stains living cytoplasm yellow, Bleaches lignin to pure white"),
            ("Chlor-zinc-iodine (Schulze reagent) reaction", "Stains pure cellulose walls of collenchyma and cotton deep blue-violet; stains lignified sclerenchyma walls yellow-brown", "Standard forensic test for evaluating lignin content in paper pulp and textile fibers", "Turns all plant cells pitch black, Dissolves sclerenchyma instantly, Stains pectin bright green"),
            ("Toluidine Blue O metachromatic staining", "Polychromatic basic dye that stains lignified sclerenchyma secondary walls bright blue/green, and pectin-rich collenchyma walls pink/purple", "Enables simultaneous identification of multiple cell wall types on a single histological section", "Stains all cells identical red, Bleaches cell walls, Stains only dead nuclei"),
            ("Jeffrey's maceration method for isolating sclerenchyma fibres", "Boiling woody or fibrous stems in an equal mixture of 10% chromic acid and 10% nitric acid to dissolve the middle lamella", "Releases individual intact sclerenchyma fibers and sclereids for micrometer measurements without fragmenting walls", "Dissolves secondary walls leaving only living protoplasts, Fuses fibers into solid plastic, Converts fibers into sugar"),
            ("Polarized light birefringence in collenchyma vs sclerenchyma", "Collenchyma exhibits alternating lamellar extinction due to differing microfibril angles in pectin/cellulose; Sclerenchyma exhibits uniform high-order birefringence", "Differentiates primary plastic collenchyma from secondary elastic sclerenchyma under petrographic microscopy", "Collenchyma shows zero birefringence, Sclerenchyma appears completely dark, Both appear identical to air"),
            ("Fluorescence microscopy of lignin (Autofluorescence)", "Under ultraviolet excitation (\\(\\approx 365\\text{ nm}\\)), lignified sclerenchyma walls emit intense natural blue-green autofluorescence without adding any chemical dyes", "Collenchyma walls show no autofluorescence, enabling pristine optical contrast", "Collenchyma emits bright red light, Sclerenchyma absorbs all UV without emission, Emits yellow light only when heated"),
            ("Schweizer's reagent (Cuoxam / Ammoniacal copper hydroxide)", "Completely dissolves pure cellulose fibers (cotton, young collenchyma), but leaves heavily lignified sclerenchyma fibers undissolved", "Used in textile quality laboratories to test the purity and chemical processing of bast fibers", "Dissolves only lignin while preserving cellulose, Fuses fibers into copper wire, Stains starch blue-black"),
            ("Methylene Blue staining of collenchyma", "Basic cationic dye that binds strongly to acidic carboxylate groups (\\(\\text{COO}^-\\)) of pectins, staining collenchyma deep blue", "Highlight corner thickenings in celery and pumpkin stems under brightfield microscopy", "Stains secondary lignin red, Selectively bleaches pectin, Stains only dead air bubbles"),
            ("Microscopic detection of stone cells in adulterated spices", "Powdered cinnamon, pepper, or clove adulterated with ground olive stones or nutshells reveals dense clusters of brachysclereids with ramiform pits", "Critical pharmacognostical purity test under the Food Safety and Standards Authority (FSSAI)", "Detects starch adulteration via iodine, Measures moisture content via heating, Tests for artificial food coloring"),
            ("Burning test for fiber identification (Cotton vs Linen vs Jute)", "Cotton and unlignified linen burn rapidly with a yellow flame, smelling like burning paper with light gray ash; heavily lignified jute burns leaving dark, gritty, charred ash", "Standard field textile test distinguishing cellulosic seed hairs from lignified bast fibers", "Linen melts like plastic forming hard beads, Jute smells like burning hair due to sulfur, Cotton does not burn")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Diagnostic Histochemistry of Mechanical Tissues.**\n- Phloroglucinol-HCl (Wiesner test): Lignin stains bright cherry-red / magenta (sclerenchyma positive, collenchyma negative).\n- Chlor-zinc-iodine: Cellulose blue-violet (collenchyma), lignin yellow-brown (sclerenchyma).\n- Toluidine Blue: Metachromatic (lignin blue/green, pectin pink/purple).\n- Autofluorescence: Lignified walls emit bright blue-green under UV.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Laboratory / Forensic Significance:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 8: Plant Biomechanics, Wind Adaptation & Industrial Fiber Technology
    arch8 = {
        'templates': [
            "Which industrial application, biological adaptation, or engineering principle relates to: '{0}'?:",
            "In plant biomechanics and biomimetic engineering: '{0}' is characterized by:",
            "What functional consequence or technological advantage arises from: '{0}'?:",
            "How does plant mechanical architecture optimize: '{0}'?:",
            "A materials scientist investigates bio-composite materials: '{0}'. What is true?:",
            "Which evolutionary selective pressure produced: '{0}'?:",
            "What is the engineering significance of: '{0}'?:",
            "Why is '{0}' critical for terrestrial plant architecture?:",
            "What industrial advancement utilizes: '{0}'?:",
            "Evaluate the plant biomechanics concept: '{0}':"
        ],
        'data': [
            ("I-Beam structural engineering in plant stems", "Peripheral sclerenchyma or collenchyma fiber girders act like the flanges of an engineering I-beam or hollow structural tube", "Maximizes resistance to bending moments (\\(M = \sigma I / y\\)) with minimum material cost and low weight", "Plants are solid cast-iron rods without internal cavities, Centers of stems carry all the bending load, Peripheral tissues carry zero load"),
            ("Water retting of bast fibers (Microbial pectinolysis)", "Submerging harvested jute or flax stems in slow-moving water allows anaerobic bacteria (Clostridium) to produce pectinases that digest parenchymal middle lamellae", "Releases the intact, tough sclerenchyma bast fiber ribbons cleanly from the stem core without damaging fibers", "Chemical process using boiling sulfuric acid, Burns the plant stems to ash, High-pressure steam explosion destroying all fibers"),
            ("Bio-composites and automotive lightweighting", "Flax and hemp sclerenchyma fibers are embedded in polypropylene or epoxy matrices to manufacture lightweight, crash-resistant automotive interior door panels", "Replaces heavy, energy-intensive glass fibers with biodegradable, renewable, carbon-neutral natural composites", "Used to manufacture steel car engines, Used exclusively as car fuel, Replaces rubber in car tires"),
            ("Lignocellulosic biomass recalcitrance in biofuels", "The complex, crystalline cross-linking between lignin, hemicellulose, and cellulose in secondary walls resists enzymatic hydrolysis", "Major technological hurdle in producing cellulosic bioethanol from agricultural residues (corn stover, switchgrass)", "Lignin converts into ethanol instantly without enzymes, Plant walls dissolve completely in cold water, Recalcitrance occurs only in algae"),
            ("Wind-induced lodging resistance in cereals", "Wheat and rice varieties bred with thick sclerenchyma hypodermal rings and lignin-rich culm walls resist stem breakage (lodging) during monsoon storms", "Guarantees crop yield protection and enables automated mechanical combine harvesting", "Tall weak-stemmed varieties are more lodging resistant, Lodging is prevented by removing all leaves, Sclerenchyma makes stems fall over"),
            ("Biomimetic impact absorption (Macadamia / Walnut shell mimicry)", "Interlocking geometric sclereid suture architectures in nut endocarps distribute impact energy circumferentially, preventing crack propagation", "Inspires biomimetic crack-resistant helmets, armor plating, and protective aerospace casings", "Walnut shells shatter easily under zero load, Shells absorb impact by melting, Inspires soft sponge mattresses"),
            ("Tension wood in angiosperms (Gelatinous G-fibers)", "When a dicot tree branch is tilted, tension wood develops on the UPPER side containing specialized sclerenchyma fibres with a thick, unlignified gelatinous (G) layer", "Shrinks axially upon drying, exerting immense tensile pulling forces that pull the branch back upward toward horizontal", "Develops on the lower side pushing the branch up, Causes the branch to break off immediately, Made of pure cork"),
            ("Compression wood in gymnosperms", "In conifer trees, compression wood forms on the LOWER side of leaning trunks, possessing heavily lignified, rounded tracheids", "Expands axially, exerting compressive pushing forces that push the leaning trunk back into vertical orientation", "Develops on the upper side pulling the trunk, Formed purely by living collenchyma, Has zero lignin content"),
            ("Geomembrane and geotextile engineering with coir", "Coir sclerenchyma mesh mats are laid over steep slopes and riverbanks to prevent soil erosion while vegetation establishes", "High lignin content (\\(\\approx 45\\%\\)) gives coir an exceptionally slow degradation rate (lasts 3 to 5 years in wet soil)", "Coir degrades within two days in water, Dissolves into toxic acids killing all grass, Replaces concrete foundations in skyscrapers"),
            ("Safety glass laminate inspired by plant cell wall composites", "Modern laminated safety glass (alternating rigid glass sheets with flexible PVB polymer interlayers) mimics the alternating microfibril angles of sclerenchyma walls", "Arrests crack propagation by dissipating mechanical fracture energy along flexible interfaces", "Mimics the single crystal structure of quartz, Replicates the hollow lumen of dead cells, Based on the fluid lipid bilayer")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Plant Biomechanics & Industrial Technologies.**\n- I-beam engineering: Peripheral collenchyma/sclerenchyma girders resist bending with minimal mass.\n- Retting: Microbial pectinases release intact bast fibers (jute/flax).\n- Bio-composites: Natural fibers replace fiberglass in automotive panels; nut endocarp sclereids inspire crack-resistant materials.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Biomechanical / Industrial Principle:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-3-3.1.3", "Collenchyma (flexibility), Sclerenchyma (lignified walls)", archs)


if __name__ == "__main__":
    q1 = gen_3_1_1()
    q2 = gen_3_1_2()
    q3 = gen_3_1_3()
    print(f"gen_3_1_1: {len(q1)} questions")
    print(f"gen_3_1_2: {len(q2)} questions")
    print(f"gen_3_1_3: {len(q3)} questions")
    print(f"Total Part 1 questions: {len(q1) + len(q2) + len(q3)}")
