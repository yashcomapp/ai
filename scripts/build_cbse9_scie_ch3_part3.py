import json
import re

def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        "Uncontrolled somatic mutation",
        "Non-functional connective stroma",
        "Passive artifact of fixation"
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
# 3.3.1: Epithelial tissues: Squamous, cuboidal, columnar, ciliated
# ==========================================
def gen_3_3_1():
    # Arch 1: General Features of Epithelial Tissue & Basement Membrane
    arch1 = {
        'templates': [
            "What distinct histological and anatomical characteristic defines: '{0}'?:",
            "In human histology: '{0}' is recognized by:",
            "Consider epithelial tissue architecture: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A pathologist examines epithelial histology: '{0}'. What is true?:",
            "Identify the accurate histological fact regarding: '{0}':",
            "How does '{0}' protect underlying tissues while regulating exchange?:",
            "Evaluate the cellular feature: '{0}'. Its biological role is:",
            "Why is '{0}' considered a fundamental barrier tissue in animals?:",
            "What structural property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Epithelial tissue general definition", "Continuous sheets of tightly packed cells covering external body surfaces and lining internal cavities and lumens, with minimal intercellular matrix", "Possesses an exposed free apical surface and a resting basal surface anchored to a basement membrane", "Loose meshwork of fibers with abundant extracellular fluid, Contractile syncytium generating voluntary movement, Electrically excitable network transmitting action potentials"),
            ("Basement Membrane (Basal Lamina + Reticular Lamina)", "Non-cellular, protein-polysaccharide fibrous sheet (collagen IV, laminin, entactin, heparan sulfate proteoglycan) beneath epithelial cells", "Anchors epithelium to underlying connective tissue, provides physical support, and acts as a selective molecular filter", "Living cellular layer dividing by mitosis, Thick lignified dead wall, Phospholipid bilayer membrane enclosing individual cells"),
            ("Avascularity of Epithelia", "Epithelial tissues strictly lack direct blood vessels (capillaries)", "Oxygen, nutrients, and waste products diffuse across the semi-permeable basement membrane from capillaries in underlying connective tissue (lamina propria)", "Directly penetrated by large muscular arteries, Lacks all nutrient exchange, Possesses internal lymphatic conduits"),
            ("High regenerative capacity", "Exhibits exceptional mitotic turnover, rapidly replacing cells shed due to physical friction or chemical wear (e.g., skin epidermis, intestinal lining)", "Sustained by adult stem cells residing in the basal germinative layer", "Incapable of cell division after embryogenesis, Permanent post-mitotic tissue like neurons, Heals only by scar fibrosis"),
            ("Cell junctions (Tight junctions / Zonula occludens)", "Continuous belt of claudin and occludin proteins sealing adjacent plasma membranes near the apical border", "Prevents paracellular leakage of fluids and solutes across epithelial sheets (e.g., blood-brain barrier, stomach lining)", "Channels that allow free cytoplasmic diffusion, Mechanical rivets anchoring intermediate filaments, Open pores for water bulk flow"),
            ("Adherens junctions (Zonula adherens) and Desmosomes (Macula adherens)", "Adherens junctions link cadherins to actin microfilaments; Desmosomes link desmogleins/desmocollins to intermediate keratin filaments (tonofilaments)", "Provide immense mechanical tensile strength, preventing tissue tearing under mechanical shearing (e.g., skin, cervix, cardiac muscle)", "Pores allowing electrical ion flow, Tight water barriers, Sites of cellular endocytosis"),
            ("Gap junctions (Nexus / Connexons)", "Transmembrane hexameric protein cylinders (connexons) forming hydrophilic aqueous channels (\\(1.5\\text{ nm}\\)) between adjacent cells", "Allows rapid electrical coupling and metabolic communication by passing small molecules (ions, cAMP, ATP) up to \\(1,000\\text{ Da}\\)", "Impermeable barriers blocking all diffusion, Anchoring plaques for heavy collagen bundles, Non-functional lipid inclusions"),
            ("Microvilli on apical membrane", "Dense, non-motile, cylindrical finger-like cytoplasmic projections supported by an actin core, forming a 'brush border'", "Dramatically expands apical surface area up to 20- to 30-fold to maximize absorption (e.g., small intestine enterocytes, renal PCT)", "Motile whip-like organelles sweeping mucus, Sensory antennae receiving sound waves, Thick keratin scales"),
            ("Cilia on apical membrane", "Motile, hair-like projections containing a 9+2 axoneme of tubulin microtubules powered by ATP-driven dynein motor arms", "Beat synchronously in metachronal waves to propel mucus, trapped dirt, or oocytes along luminal surfaces", "Non-motile projections expanding absorptive area, Dense keratin dead scales, Storage vesicles for enzymes"),
            ("Simple vs Stratified classification", "Simple epithelia consist of a single cell layer (specialized for absorption, filtration, and secretion); Stratified epithelia consist of multiple cell layers (specialized for physical/chemical protection against wear and tear)", "Classification based on the number of cell layers and the shape of the surface layer", "Based on whether cells contain hemoglobin, Based on presence of DNA, Based on electrical conductivity")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand General Epithelial Tissue Biology.**\n- Tightly packed cells, minimal matrix, avascular (nourishment via diffusion across basement membrane).\n- Polarity: Apical surface (microvilli/cilia) + Basal surface on Basement Membrane (Basal lamina + Reticular lamina).\n- Specialized junctions: Tight (occluding/barrier), Desmosomes (anchoring/tensile), Gap (communicating/connexons).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Functional / Clinical Detail:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 2: Simple Epithelia (Squamous, Cuboidal, Columnar, Ciliated)
    arch2 = {
        'templates': [
            "What is the morphological shape, anatomical location, and function of: '{0}'?:",
            "In human histology: '{0}' is characterized by:",
            "Consider simple epithelial types: '{0}' specializes in:",
            "Which statement precisely describes: '{0}'?:",
            "A medical student examines an organ biopsy: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' optimize diffusion, secretion, or mechanical transport?:",
            "Evaluate the epithelial subtype: '{0}':",
            "Why is '{0}' found in this specific physiological site?:",
            "What histological property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Simple Squamous Epithelium (Pavement epithelium)", "Single layer of extremely flat, thin, scale-like polygonal cells with wavy margins and a centrally bulging, flattened disc-like nucleus", "Specialized for rapid passive diffusion, osmosis, and filtration; lines lung alveoli, Bowman's capsule of nephrons, and blood vessel endothelium", "Tall columnar cells specialized for mucus secretion, Multi-layered protective barrier on dry skin, Cube-shaped cells lining salivary ducts"),
            ("Endothelium and Mesothelium", "Endothelium: simple squamous lining the internal lumen of blood vessels, heart chambers, and lymphatics; Mesothelium: simple squamous lining major body serous cavities (pleura, peritoneum, pericardium)", "Reduces friction for circulating blood and secretes lubricating serous fluid in coelomic cavities", "Stratified keratinized skin layer, Glandular epithelium secreting stomach acid, Ciliated lining of trachea"),
            ("Simple Cuboidal Epithelium", "Single layer of cube-like cells with roughly equal height and width, possessing a prominent, centrally located spherical nucleus", "Specialized for secretion and selective absorption; lines thyroid follicles, renal collecting tubules, and salivary/pancreatic ducts", "Flat pancake-like cells lining lung alveoli, Tall column-like cells with basal nuclei, Multi-layered lining of the esophagus"),
            ("Brush-bordered Simple Cuboidal Epithelium in PCT", "Cuboidal cells whose apical surface is densely packed with microvilli (brush border), exponentially expanding absorptive surface area", "Lines the Proximal Convoluted Tubule (PCT) of the nephron, reabsorbing \\(\\approx 70\\%\\) of glomerular filtrate (water, glucose, amino acids, ions)", "Lines the alveoli facilitating gas diffusion, Lines the urinary bladder allowing distension, Found in skin epidermis"),
            ("Simple Columnar Epithelium", "Single layer of tall, pillar-like, vertically elongated cells with oval nuclei situated in the basal third of the cell", "Specialized for active nutrient absorption and heavy secretion of digestive enzymes and mucus; lines stomach, small intestine, and gallbladder", "Flat thin cells with central nuclei, Multi-layered tissue with keratin, Cube-shaped cells lining thyroid"),
            ("Brush-bordered Simple Columnar with Goblet Cells in Intestine", "Columnar enterocytes with apical microvilli interspersed with unicellular mucus-secreting Goblet cells", "Lines the mucosa of the small intestine (duodenum, jejunum, ileum); microvilli form the intestinal brush border for terminal digestion and absorption", "Lines the dry external epidermis, Lines the heart ventricles, Forms the outer cornea of the eye"),
            ("Ciliated Simple Columnar Epithelium in Fallopian Tubes (Oviducts)", "Columnar cells equipped with motile apical cilia beating synchronously towards the uterus", "Creates unidirectional fluid currents that propel the ovulated secondary oocyte (and early embryo) along the fallopian tube to the uterine cavity", "Lines the stomach digesting food with acid, Lines blood vessels reducing friction, Found in kidney glomerulus"),
            ("Ciliated Simple Cuboidal / Columnar in Ventricles (Ependyma)", "Lines the ventricles of the brain and central canal of the spinal cord (ependymal cells)", "Cilia beat to circulate cerebrospinal fluid (CSF) throughout the central nervous system", "Absorbs nutrients in small intestine, Forms thick protective skin scales, Secretes hydrochloric acid"),
            ("Unicellular Goblet Cells", "Modified columnar epithelial cells specialized to synthesize, package, and secrete mucin glycoproteins by exocytosis", "Mucin hydrates to form viscous protective mucus, lubricating luminal surfaces and protecting stomach/intestinal mucosa from self-digestion by acid and enzymes", "Dead keratinized cells protecting skin, Phagocytic white blood cells, Cells that transmit electrical impulses"),
            ("Glandular Epithelium (Endocrine vs Exocrine)", "Exocrine glands discharge secretions through ducts onto epithelial surfaces (e.g., salivary, sweat, mammary, digestive glands); Endocrine glands lack ducts and secrete hormones directly into surrounding interstitial fluid and blood (e.g., thyroid, pituitary, adrenal)", "Derived by invagination of surface epithelial sheets during embryonic development", "Exocrine glands secrete hormones into blood, Endocrine glands possess long branching ducts, Both are derived from muscle tissue")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Simple Epithelial Subtypes.**\n- Simple Squamous: Thin flat tiles, central nucleus, diffusion/filtration (alveoli, endothelium, Bowman's capsule).\n- Simple Cuboidal: Cube-shaped, central spherical nucleus, secretion/absorption (thyroid, renal tubules, PCT brush border).\n- Simple Columnar: Tall pillars, basal oval nucleus, absorption/secretion (stomach, intestine brush border + goblet cells).\n- Ciliated: Motile 9+2 cilia (fallopian tubes \\(\\rightarrow\\) egg movement; ventricles \\(\\rightarrow\\) CSF circulation).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Histological Location & Significance:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 3: Pseudostratified & Stratified Epithelia (Keratinized, Non-keratinized, Transitional)
    arch3 = {
        'templates': [
            "What distinct architectural feature and physiological protection defines: '{0}'?:",
            "In protective epithelial histology: '{0}' is characterized by:",
            "Consider complex epithelial stratification: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A histopathologist analyzes a mucosal biopsy: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' prevent mechanical abrasion, desiccation, or chemical toxicity?:",
            "Evaluate the stratified epithelial tissue: '{0}':",
            "Why is '{0}' indispensable for organ lining subjected to extreme friction or distension?:",
            "What structural property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Pseudostratified Ciliated Columnar Epithelium (Respiratory epithelium)", "Single layer of cells of varying heights all resting on the basement membrane, but nuclei appear at multiple levels giving a false (pseudo) impression of stratification", "Equipped with motile apical cilia and interspersed goblet cells; lines the trachea, bronchi, and nasal cavity (mucociliary escalator)", "True multi-layered stratified epithelium lining skin, Simple squamous epithelium lining alveoli, Cube-shaped cells lining thyroid"),
            ("Mucociliary Escalator in Respiratory Tract", "Goblet cells secrete sticky mucus to trap inhaled dust, bacteria, and particulate pollutants; synchronous ciliary beating sweeps the mucus upward toward the pharynx to be swallowed", "Paralyzed and destroyed by cigarette smoke and chronic bronchitis, leading to 'smoker's cough' and frequent respiratory infections", "Propels food bolus downward into stomach, Circulates blood through lung capillaries, Pushes air into pleural cavity"),
            ("Stratified Squamous Keratinized Epithelium (Epidermis)", "Multi-layered epithelium whose basal cells divide actively, migrate upward, flatten, and die as they fill with dense insoluble keratin protein (stratum corneum)", "Forms dry, tough, waterproof, pathogen-impermeable external barrier of mammalian skin", "Moist non-keratinized lining of mouth, Single layer of cells lining stomach, Elastic tissue lining urinary bladder"),
            ("Stratified Squamous Non-Keratinized Epithelium", "Multi-layered epithelium whose surface squamous cells remain living, nucleated, and moist, lacking the dry dead keratinized scale layer", "Covers moist surfaces subjected to heavy mechanical wear and tear: oral cavity, pharynx, esophagus, vagina, and cornea", "Dry waterproof skin covering body, Single layer of cells in lungs, Columnar lining of intestine"),
            ("Transitional Epithelium (Urothelium)", "Specialized stratified epithelium whose surface umbrella cells (facet cells) can reversibly alter shape from dome-shaped/plump (when relaxed) to flattened (when stretched)", "Lines the renal pelvis, ureters, and urinary bladder; permits dramatic reversible organ distension while preventing toxic urine resorption", "Rigid keratinized layer preventing all stretching, Ciliated epithelium beating mucus, Simple squamous lining of blood vessels"),
            ("Umbrella cells (Facet cells) and Urothelial Plaques", "Large, often binucleated superficial cells possessing apical asymmetric unit membranes (AUM) composed of crystalline uroplakin plaques", "Forms an impermeable transcellular barrier against highly hypertonic, acidic, and toxic waste solutes (urea, ammonia) in urine", "Cells that absorb water from urine to dehydrate body, Cells that secrete digestive acid, Ciliated cells sweeping urine to urethra"),
            ("Stratified Cuboidal and Stratified Columnar Epithelia", "Rare multi-layered epithelia (typically 2 to 3 layers) providing moderate structural reinforcement and secretory conduit integrity", "Lines the largest ducts of sweat glands, mammary glands, salivary glands, and portions of the male urethra", "Covers the entire skin surface, Lines the small intestine lumen, Lines the alveoli of lungs"),
            ("Metaplasia in respiratory epithelium (Smoker's lung)", "Chronic exposure to toxic cigarette smoke causes pseudostratified ciliated columnar epithelium to transform into tough stratified squamous epithelium (squamous metaplasia)", "Provides resistance against chemical irritation, but eliminates the mucociliary escalator and represents a pre-malignant lesion", "Converts epithelium into bone, Causes immediate shrinkage of lung size, Reverses all cellular aging"),
            ("Cervical Transformation Zone (Squamous Metaplasia & HPV)", "Junction where simple columnar epithelium of the endocervix meets stratified squamous epithelium of the ectocervix", "High cellular turnover makes this squamocolumnar junction highly vulnerable to oncogenic Human Papillomavirus (HPV 16, 18) infection and cervical carcinoma (screened by Pap smear)", "Site where urine is filtered, Region where fertilization occurs, Completely non-dividing dead scar tissue"),
            ("Pemphigus vulgaris (Desmosome autoimmunity)", "Autoimmune blistering disease where IgG autoantibodies attack desmoglein-3 in epithelial desmosomes, causing loss of intercellular adhesion (acantholysis)", "Results in widespread, painful intraepidermal blisters and severe mucosal erosion in the skin and oral cavity", "Bacterial infection destroying basement membrane, Genetic defect in cilia motor dynein, Nutritional deficiency of vitamin C")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Stratified & Pseudostratified Epithelial Types.**\n- Pseudostratified: Single layer, nuclei at varied heights (respiratory tract: ciliated + goblet cells \\(\\rightarrow\\) mucociliary escalator).\n- Stratified Squamous Keratinized: Multi-layered, dead enucleated keratin scales, waterproof/abrasion-resistant (skin epidermis).\n- Stratified Squamous Non-Keratinized: Multi-layered, living nucleated moist surface (mouth, esophagus, vagina).\n- Transitional (Urothelium): Stretchable umbrella cells + uroplakin plaques (urinary bladder).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Histological / Clinical Significance:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Clinical and Pathological Aspects of Epithelia
    arch4 = {
        'templates': [
            "Which clinical condition, syndrome, or oncology hallmark relates to: '{0}'?:",
            "In clinical pathology and medicine: '{0}' is characterized by:",
            "What clinical insight or diagnostic finding is derived from: '{0}'?:",
            "How does pathophysiology disrupt: '{0}'?:",
            "A physician evaluates a patient biopsy: '{0}'. What is true?:",
            "Which disease mechanism explains: '{0}'?:",
            "What is the medical significance of: '{0}'?:",
            "Why is '{0}' critical in clinical oncology and cytology?:",
            "What pathological consequence results from: '{0}'?:",
            "Evaluate the biomedical concept: '{0}':"
        ],
        'data': [
            ("Carcinomas (Epithelial origin of cancers)", "Malignant tumors derived from epithelial cells constitute over \\(85\\%\\text{ to }90\\%\\) of all human adult cancers (e.g., breast, lung, prostate, colon)", "Reflects the high ongoing mitotic turnover of epithelial stem cell compartments and perpetual exposure to environmental mutagens and carcinogens", "Tumors derived exclusively from bone and cartilage, Benign non-dividing cysts, Infections caused by parasitic worms"),
            ("Primary Ciliary Dyskinesia (Kartagener's Syndrome)", "Autosomal recessive mutation in genes encoding dynein motor arms of cilia (9+2 axoneme), rendering cilia and sperm flagella completely immotile", "Leads to chronic bronchiectasis, recurrent sinusitis, male infertility, and situs inversus (reversal of internal organs)", "Causes rapid overgrowth of hair on skin, Inability of skin to produce sweat, Excessive absorption of water in kidneys"),
            ("Barrett's Esophagus (Metaplasia due to acid reflux)", "Chronic gastroesophageal reflux disease (GERD) causes stratified squamous epithelium of lower esophagus to undergo metaplasia into simple columnar epithelium with goblet cells (intestinal metaplasia)", "Increases risk of esophageal adenocarcinoma by 30- to 40-fold; monitored by routine surveillance endoscopy", "Causes complete narrowing of the trachea, Leads to instant stomach rupture, Completely curable with drinking milk"),
            ("Celiac Disease and Intestinal Villous Atrophy", "Autoimmune reaction triggered by dietary gluten in genetically susceptible individuals (HLA-DQ2/DQ8), destroying intestinal columnar enterocytes and flattening villi", "Causes severe malabsorption of iron, calcium, fats, and vitamins, leading to chronic diarrhea, weight loss, and anemia", "Overgrowth of giant intestinal microvilli, Excessive production of digestive acid in stomach, Bacterial infection of skin epidermis"),
            ("Pap Smear (Papanicolaou Cervical Cytology)", "Exfoliative cytology scraping cells from the cervical squamocolumnar transformation zone to detect dysplastic pre-cancerous nuclear atypia", "Has reduced cervical cancer mortality by over 70% worldwide through early detection of cervical intraepithelial neoplasia (CIN)", "Measures blood glucose levels, Tests for bacterial stomach ulcers, Counts red blood cells in urine"),
            ("Epidermolysis Bullosa (EB / Butterfly Children)", "Severe genetic fragility of the skin caused by mutations in keratin (K5/K14), collagen VII, or laminin-332 anchoring filaments in the basement membrane", "Minor mechanical touch or friction produces devastating widespread blistering, open ulcerations, and skin detachment", "Nutritional deficiency of vitamin D, Autoimmune attack on synovial joints, Viral infection of nerve endings"),
            ("Cholera Toxin mechanism on intestinal epithelium", "Vibrio cholerae toxin permanently ribosylates Gs protein, causing constitutive adenylate cyclase activation and runaway cAMP generation in crypt enterocytes", "Forces massive active secretion of \\(\\text{Cl}^-\\) and water into intestinal lumen, causing lethal 'rice-water' watery diarrhea and rapid hypovolemic shock", "Destroys basement membrane with acid, Paralyzes esophageal swallowing muscles, Inhibits all bile production in liver"),
            ("Clostridium perfringens enterotoxin targeting Tight Junctions", "Bacterial enterotoxin binds specifically to claudin-3 and claudin-4 in epithelial tight junctions, creating pore complexes that permeabilize membranes", "Destroys the epithelial barrier integrity, triggering acute food poisoning and severe abdominal cramps", "Stimulates hair growth on skin, Dissolves bone mineral matrix, Inhibits muscle acetylcholine receptors"),
            ("Basal Cell Carcinoma (BCC) vs Squamous Cell Carcinoma (SCC)", "BCC arises from pluripotential basal cells of epidermis (slow-growing, rarely metastasizes); SCC arises from keratinocytes of stratum spinosum (can metastasize to lymph nodes)", "Most common skin malignancies, primarily induced by chronic ultraviolet (UVB) solar radiation causing p53 DNA mutations", "Arise from deep bone marrow stem cells, Caused by eating contaminated food, Benign viral warts that heal in 3 days"),
            ("Keratin pearls in well-differentiated Squamous Cell Carcinoma", "Histopathological hallmark where malignant squamous cells produce concentric, whorled laminations of eosinophilic keratin within tissue stroma", "Diagnostic indicator of squamous cell differentiation in biopsy specimens", "Deposits of pure calcium phosphate, Clusters of living bacteria inside blood vessels, Glycogen granules inside muscle fibers")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Clinical Pathology of Epithelial Tissues.**\n- Oncology: Carcinomas arise from epithelia (85-90% of all cancers) due to high mitotic turnover and carcinogen exposure.\n- Ciliary defects: Kartagener's syndrome (dynein arm defect \\(\\rightarrow\\) immotile cilia/flagella, bronchiectasis, situs inversus).\n- Metaplasia: Barrett's esophagus (squamous \\(\\rightarrow\\) columnar from GERD acid).\n- Pathogen targets: Cholera toxin (cAMP \\(\\rightarrow\\) \\(\\text{Cl}^-\\) hypersecretion); Pemphigus (desmoglein-3 autoimmunity).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Clinical Consequence:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }


    # Arch 5: Glandular Epithelia: Exocrine vs Endocrine & Secretory Modes
    arch5 = {
        'templates': [
            "What distinct histological classification defines: '{0}'?:",
            "In glandular epithelial histology: '{0}' is characterized by:",
            "Consider glandular secretory mechanisms: '{0}' functions to:",
            "Which statement precisely describes: '{0}'?:",
            "A histologist examines exocrine vs endocrine tissue: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' discharge secretory products into ducts or blood?:",
            "Evaluate the glandular epithelial type: '{0}':",
            "Why is '{0}' categorized under this specific secretory mode?:",
            "What structural property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Merocrine (Eccrine) Secretion", "Secretory products are packaged into membrane-bound vesicles and discharged by exocytosis with zero loss of cellular cytoplasm", "Most common secretory mode; found in salivary glands, eccrine sweat glands, and pancreatic exocrine acini", "The entire cell disintegrates to release secretion, Apical portion of cell pinches off, Lipids are secreted without vesicles"),
            ("Apocrine Secretion", "The apical portion of the secretory cell cytoplasm pinches off along with the secretory vesicles", "Found in mammary glands (secreting milk lipid droplets) and axillary/perineal apocrine sweat glands", "Cells burst completely dying in the process, Secretion is purely by exocytosis with no loss, Glands lack all cytoplasm"),
            ("Holocrine Secretion", "The entire secretory cell dies, disintegrates, and is discharged as the secretory product itself", "Found in Sebaceous glands of the skin producing sebum (oil); continuous replacement from basal stem cells", "No cell loss occurs, Apical cytoplasm pinches off, Found in salivary glands"),
            ("Unicellular Exocrine Gland (Goblet Cell)", "Single isolated secretory cells scattered within an epithelial sheet; synthesizes and secretes protective mucus", "Lines the respiratory and gastrointestinal tracts; sole example of a unicellular exocrine gland in humans", "Multi-layered cluster of cells in pancreas, Endocrine gland lacking ducts, Gland producing adrenaline"),
            ("Multicellular Exocrine Gland Classification", "Classified by duct branching: Simple (unbranched duct) vs Compound (branched duct); and secretory unit shape: Tubular, Acinar (alveolar), or Tubuloacinar", "Pancreas and parotid are compound acinar glands; sweat glands are simple coiled tubular glands", "Classified purely by the color of secretion, Based on presence of red blood cells, Based on bone minerals"),
            ("Serous vs Mucous Secretory Acini", "Serous acini secrete watery protein- and enzyme-rich fluid (e.g., parotid gland, pancreatic acini); Mucous acini secrete thick, viscous, protective mucin glycoproteins (e.g., sublingual gland)", "Serous cells have spherical central nuclei; mucous cells have flattened basal nuclei compressed by apical mucinogen droplets", "Serous cells secrete hydrochloric acid, Mucous cells lack nuclei, Both are endocrine glands"),
            ("Endocrine Glands (Ductless glands)", "Glands that lack ducts; secretory epithelial cords or follicles secrete hormones directly into surrounding interstitial fluid to enter capillaries", "Pituitary, thyroid, adrenal, and parathyroid glands coordinate distant systemic target organs via bloodstream transport", "Glands discharging enzymes onto skin through long tubes, Sweat glands in armpits, Digestive glands in stomach"),
            ("Heterocrine (Mixed / Amphicrine) Gland (e.g., Pancreas)", "Contains both exocrine tissue (pancreatic acini secreting digestive enzymes via pancreatic duct) and endocrine tissue (Islets of Langerhans secreting insulin and glucagon into blood)", "Dual functional identity vital for digestion and systemic glucose homeostasis", "Gland composed of dead cells, Pure endocrine gland like pituitary, Pure exocrine gland like sweat gland"),
            ("Myoepithelial Cells (Basket cells)", "Spindle-shaped, stellate contractile cells of epithelial origin located between secretory cells and the basement membrane of exocrine glands", "Contracts under autonomic or hormonal stimulation (e.g., oxytocin in mammary glands) to expel accumulated secretion into the duct system", "Dead connective tissue fibers, Skeletal muscle fibers, Glial cells of the brain"),
            ("Thyroid Follicular Epithelium (Colloid storage)", "Simple cuboidal epithelium arranged in spherical follicles enclosing a central lumen filled with gelatinous thyroglobulin colloid", "Synthesizes, stores, and iodinates thyroglobulin extracellularly in the follicular lumen before releasing T3 and T4 hormones into capillaries", "Multi-layered keratinized lining, Endocrine gland without any follicles, Gland producing digestive bile")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Glandular Epithelial Classification & Secretory Modes.**\n- Exocrine (ducts) vs Endocrine (ductless \(\rightarrow\) bloodstream).\n- Secretory mechanisms: Merocrine/Eccrine (exocytosis, no cell loss: salivary, pancreas); Apocrine (apical pinch-off: mammary lipid); Holocrine (entire cell disintegrates: sebaceous).\n- Acini types: Serous (watery enzymes, round central nuclei) vs Mucous (viscous mucin, flat basal nuclei).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Functional / Clinical Detail:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 6: Quantitative & Morphometric Epithelial Problems
    arch6 = {
        'templates': [
            "{0}:",
            "Calculate the epithelial tissue cellular metric: {0}:",
            "A quantitative epithelial morphometry calculation: {0}:",
            "Solve the quantitative cytology calculation: {0}:",
            "Compute the following epithelial parameter: {0}:",
            "Analyze the numerical surface-area expansion calculation: {0}:",
            "Determine the correct calculated morphometric value: {0}:",
            "An analytical epithelial cell turnover problem: {0}:",
            "Find the accurate quantity for: {0}:",
            "Quantitative epithelial tissue evaluation: {0}:"
        ],
        'data': [
            ("A cylindrical intestinal enterocyte has apical diameter \(10\text{ }\\mu\text{m}\) (flat area \(\approx 78.5\text{ }\\mu\text{m}^2\)). Its apical membrane bears \(2,000\) microvilli, each \(1.0\text{ }\\mu\text{m}\) long and \(0.1\text{ }\\mu\text{m}\) in diameter. By what factor do microvilli expand the apical absorptive surface area of this enterocyte?", "\(\approx 9.0\text{-fold expansion}\)", "Area per microvillus \(= \pi d h = 3.1416 \times 0.1 \times 1.0 \approx 0.314\text{ }\\mu\text{m}^2\). Total microvilli area \(= 2,000 \times 0.314 \approx 628.3\text{ }\\mu\text{m}^2\). Total apical area \(= 78.5 + 628.3 = 706.8\text{ }\\mu\text{m}^2\). Factor \(= 706.8 / 78.5 \approx 9.0\)", "\(\approx 2.0\text{-fold}\), \(\approx 50\text{-fold}\), \(\approx 200\text{-fold}\)"),
            ("The human small intestine has an anatomical tube surface area of \(\approx 0.5\text{ m}^2\). Plicae circulares increase area 3-fold; villi increase it 10-fold; microvilli increase it 20-fold. What is the total effective absorptive surface area of the human small intestine?", "\(\approx 300\text{ m}^2\) (roughly the area of a tennis court)", "\(\text{Total Area} = 0.5\text{ m}^2 \times 3 \times 10 \times 20 = 300\text{ m}^2\)", "\(30\text{ m}^2\), \(3,000\text{ m}^2\), \(3.0\text{ m}^2\)"),
            ("Human skin sheds approximately \(30,000\text{ to }40,000\) dead cornified keratinocytes per minute. Approximately how many dead skin scales are shed from a human body in 24 hours?", "\(\approx 5.04 \times 10^7\text{ cells per day}\) (\(\approx 50\text{ million}\))", "\(\text{Cells/day} = 35,000\text{ cells/min} \times 60\text{ min} \times 24\text{ hr} = 5.04 \times 10^7\text{ cells}\)", "\(\approx 5.04 \times 10^5\), \(\approx 5.04 \times 10^9\), \(\approx 1.00 \times 10^6\)"),
            ("In human intestinal mucosa, complete epithelial turnover of enterocytes occurs every 4 days (96 hours). If the intestinal lining comprises \(1.0 \times 10^{11}\) epithelial cells, how many new enterocytes are produced by crypt stem cells every hour?", "\(\approx 1.04 \times 10^9\text{ enterocytes/hour}\) (\(\approx 1\text{ billion/hr}\))", "\(\text{Rate} = 1.0 \times 10^{11}\text{ cells} / 96\text{ hours} \approx 1.04 \times 10^9\text{ cells/hour}\)", "\(\approx 1.04 \times 10^7\), \(\approx 1.04 \times 10^{11}\), \(\approx 5.00 \times 10^8\)"),
            ("The respiratory diffusion barrier in human lung alveoli has an average thickness of \(0.5\text{ }\\mu\text{m}\) (\(5.0 \times 10^{-7}\text{ m}\)) and total surface area \(100\text{ m}^2\). According to Fick's Law (\(J = -D A \Delta C / \Delta x\)), if pulmonary fibrosis doubles barrier thickness to \(1.0\text{ }\\mu\text{m}\), by what factor is the rate of oxygen diffusion reduced?", "Reduced to \(1/2\) (by \(50\%\))", "Diffusion rate is inversely proportional to membrane thickness \(\Delta x\); doubling thickness halves the diffusion rate", "Reduced to 1/4, Reduced to 1/10, Diffusion rate remains unchanged"),
            ("A simple cuboidal epithelial cell in a renal collecting duct is a cube of side \(12\text{ }\\mu\text{m}\). What is its volume and total surface area?", "Volume: \(1,728\text{ }\\mu\text{m}^3\); Surface area: \(864\text{ }\\mu\text{m}^2\)", "\(V = s^3 = 12^3 = 1,728\text{ }\\mu\text{m}^3\). \(SA = 6s^2 = 6 \times 144 = 864\text{ }\\mu\text{m}^2\)", "Volume: 1,000 μm^3; SA: 600 μm^2, Volume: 2,400 μm^3; SA: 1,200 μm^2, Volume: 864 μm^3; SA: 1,728 μm^2"),
            ("A human trachea has internal diameter \(2.0\text{ cm}\) (circumference \(\approx 6.28\text{ cm}\)) and length \(10\text{ cm}\). If ciliated epithelial cells average \(10\text{ }\\mu\text{m}\) in diameter (surface area \(100\text{ }\\mu\text{m}^2 = 10^{-6}\text{ cm}^2\)), approximately how many ciliated cells line the tracheal lumen?", "\(\approx 6.28 \times 10^7\text{ ciliated cells}\)", "\(\text{Tracheal area} = \pi D L = 3.1416 \times 2.0 \times 10 = 62.83\text{ cm}^2\). Cells \(= 62.83 / 10^{-6} \approx 6.28 \times 10^7\)", "\(\approx 6.28 \times 10^5\), \(\approx 6.28 \times 10^9\), \(\approx 1.25 \times 10^6\)"),
            ("Cilia in human respiratory epithelium beat at an average frequency of \(12\text{ Hz}\) (12 beats/second). How many forward effective power strokes are executed by a tracheal cilium in 1 hour?", "\(43,200\text{ power strokes}\)", "\(\text{Strokes} = 12\text{ beats/sec} \times 3,600\text{ s/hr} = 43,200\)", "720, 4,320, 86,400"),
            ("The mucociliary escalator moves trapped particulate mucus upwards in the trachea at a steady velocity of \(5\text{ mm/minute}\). How long does it take for a dust particle trapped in the mid-trachea to travel \(60\text{ mm}\) (\(6.0\text{ cm}\)) to the pharynx?", "\(12\text{ minutes}\)", "\(\text{Time} = \text{Distance} / \text{Velocity} = 60\text{ mm} / 5\text{ mm/min} = 12\text{ minutes}\)", "30 minutes, 6 minutes, 60 minutes"),
            ("Transitional epithelium in an empty relaxed urinary bladder has a thickness of \(6\text{ cell layers}\) (\(\approx 80\text{ }\\mu\text{m}\)). When distended with \(500\text{ mL}\) of urine, umbrella cells flatten and the epithelium thins to \(2\text{--}3\text{ cell layers}\) (\(\approx 20\text{ }\\mu\text{m}\)). By what percentage has the epithelial thickness decreased?", "\(75\%\text{ decrease}\)", "\(\text{Decrease} = (80 - 20) / 80 = 60 / 80 = 0.75 = 75\%\)", "50% decrease, 25% decrease, 90% decrease")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Identify given physical and histological values.**\n" + item[0] + "\n\n**Step 2: Apply the governing morphometric/biophysical formula.**\n" + item[2] + ".\n\n**Step 3: Conclude.**\nResult is " + item[1] + "."
        ),
        'diff': 'hard'
    }

    # Arch 7: Histochemical Staining, Microtechnique & Identification of Epithelia
    arch7 = {
        'templates': [
            "Which histological stain, fixative, or microtechnique specifically identifies: '{0}'?:",
            "In diagnostic histopathology: '{0}' is confirmed using:",
            "What laboratory staining reaction visualizes: '{0}'?:",
            "How do histologists differentiate between: '{0}'?:",
            "A medical student examines an H&E stained biopsy slide: '{0}'. What is observed?:",
            "Which histochemical reagent specifically stains: '{0}'?:",
            "In laboratory tissue processing, '{0}' is demonstrated using:",
            "What microscopic appearance confirms: '{0}'?:",
            "Evaluate the diagnostic histology protocol for: '{0}':",
            "Identify the standard histochemical procedure utilized for: '{0}':"
        ],
        'data': [
            ("Periodic Acid-Schiff (PAS) Staining of Basement Membrane", "Periodic acid oxidizes 1,2-glycol groups in basement membrane proteoglycans into aldehydes; Schiff reagent reacts to produce a brilliant magenta / deep pink line", "Gold standard diagnostic stain for evaluating basement membrane thickening (e.g., in diabetic nephropathy) and goblet cell mucins", "Stains cytoplasm bright green, Stains dead wood cherry red, Stains lipid droplets yellow"),
            ("Hematoxylin and Eosin (H&E) staining of epithelia", "Basic hematoxylin stains acidic nucleic acids in nuclei dark blue/purple; Acidic eosin stains basic cytoplasmic proteins and extracellular collagen pink/red", "Standard universal histological stain for light microscopic evaluation of all tissue biopsies", "Stains all tissues black, Stains living cells only with fluorescent blue, Bleaches cell nuclei"),
            ("Alcian Blue staining of acidic mucins", "Basic copper phthalocyanin dye that binds selectively to acidic sulfated and carboxylated glycosaminoglycans and mucins at pH 2.5, staining goblet cells bright turquoise blue", "Differentiates epithelial mucins from neutral connective tissue proteins; combined with PAS to detect intestinal metaplasia", "Stains keratin scales red, Stains cell membranes black, Stains bone mineral blue"),
            ("Papanicolaou (Pap) Staining Method", "Multichromatic staining protocol using Harris hematoxylin, Orange G (keratin), and Eosin Azure (EA50) for exfoliated epithelial cells", "Differentiates metabolic maturity of squamous cells: superficial mature cells stain pink-orange (keratinized); deeper parabasal cells stain green-cyan", "Stains bacterial cell walls, Tests blood hemoglobin, Stains urine crystals"),
            ("Immunohistochemistry for Cytokeratins (CK markers)", "Monoclonal antibodies targeting specific intermediate filament cytokeratins (e.g., CK7, CK20, pan-cytokeratin AE1/AE3)", "Confirms epithelial carcinoma origin in metastatic undifferentiated tumors and pinpoints primary organ site (e.g., CK7+/CK20- in lung/breast vs CK7-/CK20+ in colon)", "Stains muscle actin, Stains nerve myelin, Stains bone mineral"),
            ("Silver impregnation (Grocott / Gomori) for reticular fibers", "Reduces silver nitrate to metallic black silver, delineating the reticular lamina of the epithelial basement membrane", "Visualizes the anchoring connective tissue stroma underlying epithelial sheets", "Stains cilia red, Stains cell nuclei yellow, Stains lipid droplets white"),
            ("Electron Microscopy (TEM) of Tight Junctions (Freeze-fracture)", "Freeze-fracture electron microscopy reveals tight junctions as an anastomosing network of intramembrane protein strands on the P-face with complementary grooves on the E-face", "Resolves sub-nanometer molecular architecture impossible with light microscopy", "Visualizes light photons, Stains chromosomes purple, Measures cellular ATP levels"),
            ("Gram stain on ciliated respiratory smear", "Distinguishes normal ciliated respiratory epithelial cells from invading Gram-positive (purple) or Gram-negative (pink) bacterial pathogens", "Diagnoses bacterial pneumonia and purulent tracheobronchitis", "Tests for viral DNA, Measures ciliary beat frequency, Detects asthma allergens"),
            ("Masson's Trichrome staining of mucosal biopsies", "Stains epithelial cytoplasm red/pink, nuclei dark brown/black, and underlying connective tissue collagen bright blue or green", "Evaluates sub-epithelial collagen deposition and fibrosis (e.g., in collagenous colitis)", "Stains all cells identical gray, Bleaches connective tissue, Stains red blood cells black"),
            ("Mucicarmine staining (Mayer's mucicarmine)", "Aluminum complexed with carmine dye that stains epithelial acid mucins intense deep ruby red", "Diagnostic histological tool to confirm adenocarcinoma and detect capsule of Cryptococcus neoformans fungus", "Stains skin keratin yellow, Stains thyroid colloid blue, Stains bone mineral green")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Histochemical & Diagnostic Stains for Epithelia.**\n- PAS: Magenta line for Basement Membrane & Goblet cell mucins (oxidizes glycols \(\rightarrow\) Schiff reaction).\n- H&E: Hematoxylin (nuclei blue/purple) + Eosin (cytoplasm pink).\n- Alcian Blue: Turquoise for acidic mucins.\n- Pap Stain: Orange G (keratin) + EA50 (maturation grading in cervical screening).\n- Cytokeratins: Intermediate filament IHC markers confirming carcinoma (epithelial) origin.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Laboratory / Diagnostic Significance:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }


    # Arch 8: Intercellular Junctions, Basement Anchors & Apical Adaptations
    arch8 = {
        'templates': [
            "What distinct molecular junction or specialized membrane feature defines: '{0}'?:",
            "In epithelial ultrastructure and junctional integrity: '{0}' is characterized by:",
            "Consider epithelial barrier specializations: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A cell biologist examines epithelial adhesion: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' anchor epithelial cells to the extracellular matrix or adjacent cells?:",
            "Evaluate the junctional protein complex: '{0}':",
            "Why is '{0}' vital for maintaining polarized epithelial barrier function?:",
            "What molecular property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Hemidesmosomes (Basal matrix anchors)", "Specialized cell-matrix junctions that anchor the intermediate keratin filaments of basal epithelial cells to the underlying basement membrane (laminin-332 and collagen IV)", "Utilizes alpha-6 beta-4 integrin heterodimers; failure causes severe junctional epidermolysis bullosa", "Junctions connecting two adjacent cells side-by-side, Open channels passing ions, Tight seals blocking water"),
            ("Bullous Pemphigoid (BP180 / BP230 autoimmunity)", "Autoimmune subepidermal blistering disease where autoantibodies target hemidesmosomal proteins BP180 (collagen XVII) and BP230", "Causes complete detachment of the whole epidermis from the dermis, producing tense, fluid-filled blisters (unlike flaccid blisters of pemphigus)", "Destruction of skin keratin by bacteria, Autoantibodies against bone collagen, Viral destruction of melanocytes"),
            ("Stereocilia (Epididymis and Hair Cells)", "Extremely long, non-motile, branching microvilli supported by internal actin filaments (NOT true 9+2 cilia)", "In the epididymis: absorbs excess testicular fluid; in the inner ear hair cells: acts as mechanosensory transducers for hearing and balance", "Motile 9+2 axoneme sweeping mucus, Thick keratin scales, Hard bone pillars"),
            ("Zonula Adherens (Belt desmosome) and E-Cadherin", "Continuous circumferential belt of transmembrane E-cadherin glycoproteins linking the cortical actin belts of adjacent epithelial cells (\(\text{Ca}^{2+}\)-dependent)", "Loss of E-cadherin expression is the primary driver of Epithelial-Mesenchymal Transition (EMT) and cancer metastasis", "Junction passing electrical action potentials, Impermeable water barrier, Anchors intermediate filaments to bone"),
            ("Claudins and Occludins in Tight Junctions", "Four-transmembrane-domain proteins that polymerize into anastomosing intramembrane strands sealing the paracellular space", "Determines the electrical resistance and selective ion permeability ('pore' vs 'leak' pathways) across epithelial sheets", "Motor proteins powering ciliary movement, Enzymes that digest protein fibers, Structural proteins of the spindle"),
            ("Connexin-26 mutations in Congenital Deafness", "Mutations in GJB2 gene encoding connexin-26 (major gap junction protein in cochlear epithelial cells)", "Impairs potassium recycling in inner ear endolymph, causing the most common form of hereditary non-syndromic congenital sensorineural deafness", "Causes complete blindness, Leads to loss of skin pigmentation, Causes brittle bones"),
            ("Focal Adhesions (Integrin-Actin anchors)", "Dynamic cell-matrix junctions linking transmembrane integrins to intracellular actin microfilaments via talin, vinculin, and paxillin", "Crucial for epithelial cell migration during wound re-epithelialization and embryonic morphogenesis", "Static rivets that never disassemble, Water-impermeable seals, Sites of protein translation"),
            ("Basal infoldings and Mitochondria (Ion-transporting epithelia)", "Extensive invaginations of the basal plasma membrane interleaved with elongated vertical mitochondria", "Provides immense surface area and local ATP for \(\text{Na}^+/\text{K}^+\) ATPase pumps in fluid-transporting epithelia (renal DCT, salivary striated ducts)", "Structures that secrete mucus, Storage vacuoles for lipids, Ciliated projections sweeping fluid"),
            ("Terminal Web in columnar enterocytes", "Dense horizontal filamentous meshwork of actin, spectrin, and myosin directly beneath the apical microvilli", "Provides mechanical scaffolding anchoring the rootlets of microvillar actin cores and stabilizing the apical cell pole", "Meshwork enclosing the cell nucleus, Dense bone ring, Thick layer of dead keratin"),
            ("Transepithelial Electrical Resistance (TEER)", "Electrophysiological measurement of electrical resistance across an intact epithelial monolayer, reflecting the tight junction seal integrity", "Tight epithelia (urinary bladder) display TEER \(> 2,000\text{ }\Omega\cdot\text{cm}^2\); leaky epithelia (renal PCT) display TEER \(< 30\text{ }\Omega\cdot\text{cm}^2\)", "Measures the rate of cellular mitosis, Quantifies the number of cilia, Measures cellular DNA content")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Intercellular Junctions & Basal Specializations.**\n- Hemidesmosomes: \(\alpha_6\beta_4\) integrin anchors keratin to basement membrane (Bullous pemphigoid = anti-BP180/BP230).\n- Stereocilia: Giant actin microvilli, non-motile (epididymis absorption & inner ear mechanoreceptors).\n- E-Cadherin: Zonula adherens (\(\text{Ca}^{2+}\)-dependent, loss triggers EMT metastasis).\n- Connexin-26: Gap junctions in cochlea (mutation \(\rightarrow\) congenital deafness).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Ultrastructural / Clinical Significance:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-3-3.3.1", "Epithelial tissues: Squamous, cuboidal, columnar, ciliated", archs)


# ==========================================
# 3.3.2: Connective tissues: Blood, bone, cartilage, ligaments, tendons, areolar, adipose
# ==========================================
def gen_3_3_2():
    # Arch 1: General Features of Connective Tissue & Areolar Tissue
    arch1 = {
        'templates': [
            "What distinct histological and structural feature defines: '{0}'?:",
            "In animal ground connective tissues: '{0}' is characterized by:",
            "Consider connective tissue architecture: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A histologist examines loose connective tissue: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' bind, package, and cushion internal somatic organs?:",
            "Evaluate the cellular/extracellular feature: '{0}':",
            "Why is '{0}' considered the packaging tissue of the animal body?:",
            "What histological property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Connective Tissue General Definition", "Most abundant, widely distributed animal tissue; composed of widely spaced cells embedded within an abundant extracellular matrix (ECM)", "Originates from embryonic mesoderm; functions to connect, bind, support, package, and protect other tissues and organs", "Composed of tightly packed cells without any matrix, Originates from ectoderm only, Dedicated entirely to transmitting electrical signals"),
            ("Extracellular Matrix (ECM) composition", "Composed of non-cellular Ground Substance (glycosaminoglycans - hyaluronic acid, chondroitin sulfate) and Protein Fibres (collagen, elastin, reticulin)", "Secreted by resident fibroblasts; provides structural scaffolding, biochemical signaling, and compressive resilience", "Consists of pure water with zero proteins, Solid sheet of dead keratin scales, Composed of phospholipid bilayers"),
            ("Areolar Connective Tissue (Packaging tissue)", "Loose connective tissue containing a meshwork of collagen and elastic fibers, embedded in viscous ground substance with fibroblasts, macrophages, and mast cells", "Fills spaces inside organs, attaches skin to underlying muscles (subcutaneous layer), and surrounds blood vessels and nerves", "Rigid rock-hard matrix supporting body weight, Dense regular cord attaching muscle to bone, Fluid tissue circulating without fibers"),
            ("Fibroblasts", "Most abundant resident cells in connective tissue proper: large, flat, branching cells with prominent euchromatic nuclei", "Actively synthesize and secrete all ECM components (tropocollagen, proelastin, fibronectin, and hyaluronic acid ground substance)", "Phagocytic cells that engulf bacteria, Cells that store massive lipid droplets, Contractile cells that generate movement"),
            ("Mast Cells and their secretions", "Bone marrow-derived granulocytes residing near blood vessels; surface IgE receptors trigger rapid degranulation upon allergen exposure", "Releases Histamine (vasodilation and increased capillary permeability), Heparin (natural anticoagulant), and Serotonin (vasoconstrictor)", "Synthesizes collagen fibers, Stores triglycerides, Generates electrical action potentials"),
            ("Tissue Macrophages (Histiocytes)", "Phagocytic cells derived from circulating blood monocytes; rich in lysosomes and phagocytic vacuoles", "Engulfs cellular debris, apoptotic bodies, and invading foreign microorganisms; acts as antigen-presenting cells (APCs)", "Synthesizes bone mineral matrix, Stores calcium crystals, Produces red blood cells"),
            ("Collagen Fibres (White fibres)", "Thick, unbranched, wavy bundles composed of Type I collagen fibrils; possess immense tensile strength with minimal stretchability", "Most abundant protein in the human body (\\(\\approx 25\\text{--}30\\%\\text{ of total protein}\\)); yields gelatin upon prolonged boiling in water", "Thin branching yellow fibers that stretch easily, Highly branched fibers forming delicate nets, Fibers made of actin and myosin"),
            ("Elastic Fibres (Yellow fibres)", "Thin, highly branched, anastomosing fibers composed of elastin protein cores surrounded by fibrillin microfibrils", "Can stretch reversibly up to \\(150\\%\\) of their relaxed length and snap back without plastic deformation; imparts resilience to lungs, arteries, and skin", "Thick unbranched rigid cords, Fibers that dissolve in boiling water into gelatin, Non-stretching fibers found in bone"),
            ("Reticular Fibres (Type III Collagen)", "Delicate, thin, highly branched, argyrophilic (silver-staining) micro-networks of Type III collagen", "Forms the structural scaffolding (stroma) supporting cellular parenchymal organs: spleen, lymph nodes, liver, and bone marrow", "Thick cords attaching muscles to bone, Tough waterproof sheets on skin, Giant fibers providing bone rigidity"),
            ("Scurvy and Vitamin C (Ascorbic acid) dependency", "Prolyl and lysyl hydroxylase enzymes require ascorbic acid (vitamin C) as an essential cofactor to hydroxylate proline/lysine in collagen triple helices", "Deficiency prevents stable collagen cross-linking, causing capillary fragility, gum bleeding, skin hemorrhages, wound dehiscence, and tooth loss", "Nutritional deficiency of calcium, Genetic defect in elastin synthesis, Autoimmune destruction of macrophages")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Connective Tissue Proper & Areolar Tissue.**\n- Derived from embryonic mesoderm; widely spaced cells in abundant Extracellular Matrix (Ground substance + Fibers).\n- Areolar Tissue: Loose packaging tissue under skin and around organs; contains Fibroblasts (make fibers/matrix), Mast cells (histamine, heparin, serotonin), and Macrophages (histiocytes/phagocytosis).\n- Fibers: Collagen (white, unbranched, high tensile strength), Elastic (yellow, branched, elastin/fibrillin, stretchable), Reticular (argyrophilic mesh, lymphoid stroma).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Histological / Clinical Significance:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 2: Adipose Tissue (White vs Brown Fat)
    arch2 = {
        'templates': [
            "What distinct cytological and metabolic feature characterizes: '{0}'?:",
            "In mammalian energy storage and thermogenesis: '{0}' is defined by:",
            "Consider adipose tissue biology: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A biochemist analyzes metabolic lipid stores: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' insulate the body, store energy, or generate non-shivering heat?:",
            "Evaluate the specialized adipocyte feature: '{0}':",
            "Why is '{0}' vital for mammalian thermal and metabolic homeostasis?:",
            "What structural property corresponds to: '{0}'?:"
        ],
        'data': [
            ("White Adipose Tissue (WAT / Unilocular fat)", "Predominant adult fat; each adipocyte contains a single massive lipid droplet occupying \\(> 90\\%\\) of cell volume, flattening the cytoplasm and nucleus against the periphery ('signet-ring appearance')", "Primary long-term energy reservoir (stores triglycerides), thermal insulator under skin (hypodermis), and shock-absorbing mechanical cushion around kidneys and eyeballs", "Contains multiple small droplets and generates heat, Hard mineralized tissue supporting body, Fluid connective tissue carrying gases"),
            ("Brown Adipose Tissue (BAT / Multilocular fat)", "Abundant in newborns, hibernating mammals, and small rodents (retained around neck, scapulae, and kidneys in adult humans); contains multiple small lipid droplets and high mitochondrial density with rich vascularization", "Dedicated to non-shivering thermogenesis, burning fatty acids directly to produce metabolic heat without shivering", "Stores energy without burning it, Forms tough cords attaching muscles, Composed of dead keratinized cells"),
            ("Thermogenin (UCP-1 / Uncoupling Protein-1) in BAT", "Specialized proton transport channel in the inner mitochondrial membrane of brown adipocytes", "Uncouples electron transport chain from ATP synthesis, collapsing the proton-motive force directly as heat to protect neonates from lethal hypothermia", "Synthesizes ATP at 10-fold higher rates, Transports triglycerides out of cells, Degrades mitochondrial DNA"),
            ("Signet-ring appearance of adipocytes", "The huge single lipid droplet pushes the nucleus and thin rim of cytoplasm completely to one side of the cell border, resembling a signet ring in cross-section", "Diagnostic histological hallmark of unilocular white adipocytes", "Appearance of bone osteocytes, Morphology of ciliated epithelia, Appearance of red blood cells"),
            ("Blubber in marine mammals (Whales, Seals, Walruses)", "Massive, continuous subcutaneous hypodermal layer of white adipose tissue up to \\(50\\text{ cm}\\) thick", "Provides unmatched thermal insulation against freezing polar waters and acts as a buoyancy aid and energy reserve", "Thick layer of dead skin scales, Bone armor shielding internal organs, Dense muscle layer for swimming"),
            ("Endocrine function of WAT (Leptin secretion)", "White adipocytes act as a major endocrine organ, secreting the peptide hormone leptin into the bloodstream", "Acts on hypothalamic receptors to inhibit appetite and signal long-term energy satiety; deficiency causes morbid hyperphagic obesity", "Secretes insulin to lower blood glucose, Produces digestive enzymes for intestine, Secretes adrenaline during fight-or-flight"),
            ("Lipolysis in fasting (Hormone-Sensitive Lipase)", "Glucagon and epinephrine stimulate beta-adrenergic receptors, activating hormone-sensitive lipase (HSL) via cAMP", "Hydrolyzes stored intracellular triglycerides into glycerol and free fatty acids released into blood for systemic energy", "Converts glucose into glycogen inside fat cells, Synthesizes new collagen fibers, Transports cholesterol into bile"),
            ("Fat pads as shock absorbers (Retrobulbar and Perirenal fat)", "Dense pads of unilocular adipose tissue cushioning delicate organs (around eyeballs, kidneys, heart epicardium, palms, soles)", "Provides mechanical shock absorption, protecting visceral organs against physical impact and trauma", "Hard calcium cushions, Hollow air cavities, Fluid-filled lymphatic sacs"),
            ("Browning of white fat (Beige / Brite adipocytes)", "Cold exposure or exercise (via irisin hormone) induces trans-differentiation of white adipocytes into uncoupling UCP-1 positive 'beige' adipocytes", "Emerging therapeutic frontier to boost systemic energy expenditure and combat obesity and type 2 diabetes", "Converts fat directly into muscle fibers, Causes fat cells to undergo necrosis, Converts adipose tissue into bone"),
            ("Histological clearing of lipids in routine slides", "Routine histological processing with alcohol and xylene dissolves lipid droplets, leaving adipocytes appearing as empty, polygonal, honeycomb-like rings", "Requires frozen sectioning and staining with Oil Red O or Sudan IV to preserve and visualize neutral lipids", "Preserves lipids as dark black crystals, Converts lipids into cellulose, Stains lipids bright blue with hematoxylin")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Adipose Tissue Biology.**\n- White Adipose Tissue (WAT): Unilocular (single giant lipid droplet), signet-ring nucleus, energy storage (triglycerides), insulation (subcutaneous/blubber), shock absorption, endocrine (Leptin).\n- Brown Adipose Tissue (BAT): Multilocular (multiple lipid droplets), rich vascularity & iron-rich mitochondria, UCP-1 (Thermogenin) uncouples proton gradient for non-shivering thermogenesis (newborns/hibernators).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Metabolic / Physiological Significance:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 3: Dense Connective Tissue (Tendons vs Ligaments)
    arch3 = {
        'templates': [
            "What distinct anatomical and biomechanical distinction defines: '{0}'?:",
            "In musculoskeletal connective tissue: '{0}' is characterized by:",
            "Consider dense regular connective tissue: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "An orthopedic surgeon examines a joint injury: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' transmit muscle contraction forces or stabilize skeletal articulations?:",
            "Evaluate the fibrous connective tissue: '{0}':",
            "Why is '{0}' organized in parallel fiber bundles?:",
            "What structural property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Tendons (Muscle to Bone)", "Dense regular connective tissue composed of closely packed, parallel bundles of tough, non-elastic White Collagen Fibres", "Connects skeletal muscles to bones, transmitting muscular contractile forces to bones to produce joint movement with minimal energy loss", "Connects bone to bone, Composed of stretchable yellow elastic fibers, Loose packaging tissue around organs"),
            ("Ligaments (Bone to Bone)", "Dense regular connective tissue composed of parallel bundles containing abundant Yellow Elastic Fibres interspersed with collagen", "Connects bone to bone across synovial joints, providing high tensile strength combined with elastic flexibility to stabilize joints and prevent dislocation", "Connects skeletal muscles to bones, Composed of pure non-elastic collagen only, Fluid tissue carrying blood cells"),
            ("Fibroblast arrangement in Tendons", "Rows of elongated, flattened fibroblasts (tendon cells / tenocytes) are lined up in single files squeezed between adjacent parallel collagen bundles", "Possess minimal vascularity; healing after rupture or tendonitis is exceptionally slow and prolonged", "Fibroblasts are randomly scattered in all directions, Squeezed inside round stone cells, Cells are dead and hollow like wood fibers"),
            ("Achilles Tendon (Calcaneal tendon)", "Largest, thickest, and strongest tendon in the human body, connecting gastrocnemius and soleus calf muscles to the calcaneus heel bone", "Transmits ground reaction forces up to \\(10\\text{-times body weight}\\) during sprinting, running, and jumping", "Small ligament stabilizing the elbow joint, Muscle fiber inside the heart, Tendon attaching tongue to jaw"),
            ("Dense Regular vs Dense Irregular Connective Tissue", "Dense Regular: collagen bundles are arranged in parallel arrays resisting pull along a single axis (tendons, ligaments, aponeuroses); Dense Irregular: collagen bundles are interwoven in multiple planes resisting tensile stress from all directions (dermis of skin, organ capsules, periosteum)", "Architecture matches the directional vector of mechanical tension experienced by that anatomical site", "Dense regular is found only in the skin dermis, Dense irregular connects muscle to bone, Both lack collagen fibers"),
            ("Sprain vs Strain", "Sprain: stretching or tearing of a Ligament (connecting bone to bone) at a joint (e.g., twisted ankle); Strain: stretching or tearing of a Muscle or Tendon (e.g., pulled hamstring)", "Sprains take far longer to heal than muscle strains due to lower vascularity of ligamentous tissue", "Sprain involves muscle while strain involves bone, Both terms are identical, Sprain is a bone fracture"),
            ("Sharpey's Fibres (Perforating fibres)", "Terminal collagen fibers of tendons and periosteum that penetrate deeply into the outer circumferential lamellae of cortical bone matrix", "Anchors tendons and periosteum with unbreakable biomechanical bonding into the hard mineralized bone", "Fibres connecting skin to hair, Fibers forming the heart valves, Elastic fibers in lung alveoli"),
            ("Aponeuroses (Sheet-like tendons)", "Broad, flat, ribbon-like or sheet-like sheets of dense regular collagenous connective tissue (e.g., epicranial aponeurosis, abdominal aponeuroses)", "Attaches broad flat muscles to the skeleton or to adjacent muscular fascias", "Spherical pads cushioning joints, Fluid sacs preventing friction, Dense bone rings"),
            ("Ligamentum Flavum in Vertebral Column", "Specialized ligament connecting adjacent vertebral laminae, composed predominantly of dense yellow elastic tissue (\\(\\approx 80\\%\\text{ elastin}\\))", "Elastic recoil helps restore upright posture after bending the spine forward and prevents vertebral canal impingement", "Composed of hard bone mineral, Rigid non-elastic collagen cord, Loose packaging tissue"),
            ("Avulsion fracture", "Severe trauma where a tendon or ligament pulls away so forcefully that it tears off a fragment of the bone to which it is attached", "Demonstrates that the tensile strength of dense regular collagen bundles can exceed the shear strength of the bone itself", "Spontaneous rotting of muscle fibers, Infection of the joint cavity by bacteria, Fracture caused by lack of calcium only")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Tendon vs Ligament Histology & Biomechanics.**\n- Tendon: Connects Muscle to Bone; Dense regular White Collagen bundles (non-elastic, high tensile strength, tenocytes in single files).\n- Ligament: Connects Bone to Bone; Dense regular Yellow Elastic fibers + collagen (elastic flexibility, stabilizes joints).\n- Clinical: Sprain = Ligament tear; Strain = Muscle/Tendon tear. Sharpey's fibers anchor tendon into bone matrix.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Biomechanical / Clinical Detail:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Skeletal Tissues: Cartilage (Hyaline, Elastic, Fibrocartilage)
    arch4 = {
        'templates': [
            "What distinct histological and structural feature characterizes: '{0}'?:",
            "In skeletal cartilaginous tissue: '{0}' is recognized by:",
            "Consider cartilage types and architecture: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "An orthopedic pathologist analyzes joint cartilage: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' provide flexible, compressive, or low-friction mechanical support?:",
            "Evaluate the chondral tissue feature: '{0}':",
            "Why is '{0}' avascular with slow regenerative capacity?:",
            "What histological property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Cartilage General Definition", "Solid, semi-rigid, flexible skeletal connective tissue whose cells (chondrocytes) reside in fluid-filled cavities (lacunae) within a firm, gel-like matrix", "Matrix is composed of chondroitin sulfate proteoglycans (aggrecan) reinforced with collagen or elastic fibers", "Hard, rigid tissue impregnated with calcium phosphate crystals, Fluid tissue circulating without cells, Multi-layered epithelial barrier"),
            ("Chondrocytes and Lacunae", "Mature cartilage cells (chondrocytes) derived from chondroblasts, situated singly or in isogenous groups of 2 to 4 inside small fluid spaces termed lacunae", "Synthesize and maintain the surrounding proteoglycan and collagen matrix", "Cells lined up in single files like tenocytes, Dead hollow cells like tracheids, Rapidly dividing bone-resorbing cells"),
            ("Avascularity and Perichondrium", "Mature cartilage strictly lacks blood vessels, lymphatics, and nerves; enveloped by a dense vascular fibrous sheath termed the Perichondrium", "Chondrocytes rely entirely on slow diffusion of oxygen and nutrients across the matrix from perichondrial capillaries; articular cartilage lacks perichondrium and heals poorly", "Penetrated by dense networks of muscular arteries, Surrounded by bone marrow, Receives direct innervation by motor nerves"),
            ("Hyaline Cartilage (Most abundant cartilage)", "Glassy, bluish-white, translucent, homogeneous matrix containing fine, sub-microscopic Type II collagen fibrils (invisible under standard light microscopy)", "Covers articular surfaces of long bones (articular cartilage), forms costal cartilages (ribs to sternum), nose tip, larynx (thyroid/cricoid), trachea/bronchial rings, and embryonic skeleton", "Opaque yellow cartilage full of elastic fibers, Toughest cartilage with thick collagen cords, Hard bone with osteons"),
            ("Elastic Cartilage", "Pliant, highly flexible cartilage containing an abundant network of branching yellow elastic fibers within its matrix", "Provides flexible support and maintains organ shape; located in the external ear pinna, Eustachian tube, and epiglottis", "Glassy blue cartilage in tracheal rings, Toughest cartilage in intervertebral discs, Mineralized bone matrix"),
            ("Fibrocartilage (White fibrous cartilage)", "Toughest, most resilient cartilage; matrix contains dense, thick, parallel bundles of Type I collagen fibers, with chondrocytes aligned in rows between bundles; lacks a perichondrium", "Provides exceptional tensile strength and shock absorption; forms Intervertebral Discs, Pubic Symphysis, and knee Menisci", "Translucent glassy cartilage in nose, Flexible cartilage in ear pinna, Soft lipid storage tissue"),
            ("Articular Cartilage and Synovial Joint Lubriction", "A specialized layer of hyaline cartilage covering the bone ends of synovial joints, lacking a perichondrium to provide an ultra-smooth, low-friction bearing surface", "Friction coefficient (\\(\\\mu \\approx 0.001\\)) is 5 times smoother than ice sliding on ice, lubricated by synovial fluid (hyaluronic acid + lubricin)", "Rough abrasive surface anchoring tendons, Covered by thick periosteum, Mineralized with calcium carbonate"),
            ("Intervertebral Disc architecture", "Consists of an outer tough fibrous ring of fibrocartilage (Annulus Fibrosus) surrounding a gelatinous, water-rich central shock-absorbing core (Nucleus Pulposus)", "Herniation ('slipped disc') occurs when the annulus tears, allowing nucleus pulposus to protrude and compress spinal nerve roots", "Solid ball of hard cortical bone, Hollow cavity filled with air, Pure elastic tissue without collagen"),
            ("Osteoarthritis (Articular cartilage wear)", "Progressive biomechanical breakdown, fibrillation, and enzymatic erosion (MMP-13, aggrecanase) of articular hyaline cartilage over decades of joint loading", "Exposes underlying subchondral bone, causing joint space narrowing, bone spurs (osteophytes), severe pain, and morning stiffness", "Autoimmune destruction of bone marrow, Bacterial infection of muscle tendons, Genetic absence of elastic fibers"),
            ("Chondrogenesis: Appositional vs Interstitial Growth", "Appositional growth: new matrix deposited on the outer surface by chondroblasts in the inner perichondrium; Interstitial growth: internal chondrocytes divide inside lacunae and secrete matrix from within", "Allows rapid 3D embryonic expansion of cartilage precursors before endochondral ossification into bone", "Cartilage grows only by cell death, Grows by absorbing calcium from blood, Cartilage never grows after birth")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Cartilage Classification & Histology.**\n- Solid, semi-rigid, flexible skeletal tissue; Chondrocytes in Lacunae (isogenous groups); Avascular (slow healing via perichondrium diffusion).\n- Hyaline: Glassy translucent matrix, fine Type II collagen (articular ends, costal, nose, trachea, embryonic skeleton).\n- Elastic: Branching yellow elastic fibers (ear pinna, epiglottis, Eustachian tube).\n- Fibrocartilage: Toughest, thick Type I collagen cords, no perichondrium (intervertebral discs, pubic symphysis, knee menisci).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Biomechanical / Pathological Detail:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 5: Skeletal Tissues: Bone (Osteon / Haversian System & Mineralization)
    arch5 = {
        'templates': [
            "What distinct histological and structural feature characterizes: '{0}'?:",
            "In skeletal osteology and bone microanatomy: '{0}' is recognized by:",
            "Consider bone tissue architecture: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A medical student examines compact bone histology: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' impart rigid load-bearing support and calcium homeostasis?:",
            "Evaluate the osteological component: '{0}':",
            "Why is '{0}' organized in concentric Haversian systems?:",
            "What structural property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Bone (Osseous tissue) general definition", "Hard, rigid, highly vascularized skeletal connective tissue impregnated with inorganic calcium salts and reinforced with organic collagen fibers", "Provides rigid structural framework, protects internal organs, anchors skeletal muscles, houses hemopoietic bone marrow, and serves as calcium/phosphate reservoir", "Soft semi-rigid avascular tissue, Fluid tissue circulating without cells, Non-mineralized flexible meshwork"),
            ("Bone Matrix Composition (Organic vs Inorganic)", "Inorganic phase (\\(\\approx 65\\%\\)): crystalline Hydroxyapatite (\\(\\text{Ca}_{10}(\\text{PO}_4)_6(\\text{OH})_2\\)) providing compressive rigidity; Organic phase (\\(\\approx 35\\%\\)): Type I collagen fibers (ossein) and ground substance providing tensile strength and fracture resistance", "Acid demineralization removes minerals leaving soft flexible collagen; burning (calcination) destroys collagen leaving brittle chalk-like mineral", "Composed entirely of calcium carbonate, Pure protein matrix without minerals, Pure lipid crystals"),
            ("Osteon (Haversian System) in Compact Bone", "Fundamental structural and functional unit of mammalian compact (cortical) bone: concentric cylindrical columns aligned parallel to the long axis of the bone", "Consists of a central Haversian canal surrounded by concentric lamellae, osteocytes inside lacunae, and radiating canaliculi", "Spongy meshwork of trabeculae without canals, Solid solid glass without any cells, Hollow dead cylinder like plant xylem"),
            ("Haversian Canal (Central canal)", "Longitudinal central vascular channel running through the core of each osteon", "Contains blood capillaries, venules, lymphatic vessels, and unmyelinated nerve fibers to supply living osteocytes", "Dead empty tube filled with air, Canal through which bone marrow passes, Closed pore lacking blood vessels"),
            ("Volkmann's Canals (Perforating canals)", "Transverse or oblique channels connecting adjacent Haversian canals with each other and with the external periosteum and internal endosteum", "Allows collateral vascular and nerve network distribution throughout the thick compact bone cortex", "Longitudinal canals running parallel to Haversian canals, Pores through which cartilage cells migrate, Hollow tubes storing calcium"),
            ("Osteocytes, Lacunae, and Canaliculi", "Mature bone cells (osteocytes) trapped singly inside fluid-filled spaces (lacunae); delicate cytoplasmic processes extend through microscopic radiating tunnels (canaliculi)", "Canaliculi connect adjacent osteocytes via gap junctions, enabling nutrient, oxygen, and metabolic waste diffusion to and from the central Haversian canal", "Dead enucleated cells lacking cytoplasm, Cells arranged in single files like tenocytes, Chondrocytes dividing inside isogenous nests"),
            ("Osteoblasts vs Osteoclasts", "Osteoblasts: mononucleated, bone-forming cells derived from osteoprogenitor stem cells that synthesize and secrete organic unmineralized matrix (osteoid); Osteoclasts: giant, multinucleated (5-20 nuclei) bone-resorbing cells derived from monocyte-macrophage lineage that dissolve bone matrix using \\(\\text{H}^+\\) and cathepsin K", "Dynamic balance between osteoblast deposition and osteoclast resorption maintains continuous bone remodeling throughout adult life", "Osteoblasts dissolve bone while osteoclasts form bone, Both are derived from red blood cells, Both are dead cells"),
            ("Compact (Cortical) Bone vs Spongy (Cancellous / Trabecular) Bone", "Compact bone forms the dense, hard outer shell of bones organized into Haversian systems; Spongy bone forms the lightweight, porous interior composed of an open lattice of branching bony plates (trabeculae) housing red bone marrow", "Trabeculae align precisely along lines of mechanical compressive and tensile stress vectors (trajectorial architecture)", "Compact bone is porous while spongy bone is solid, Spongy bone lacks all cells, Compact bone is found only in the skull"),
            ("Periosteum and Endosteum", "Periosteum: outer tough double-layered fibrous sheath (fibrous outer layer + osteogenic inner layer containing osteoprogenitor cells and osteoblasts); Endosteum: delicate single-cell osteogenic membrane lining internal marrow cavities and Haversian canals", "Essential for appositional bone growth in diameter, fracture repair, and bone remodeling", "Dead protective bark covering bones, Fluid lining preventing joint friction, Thick cartilage cushion"),
            ("Osteoporosis and Bone Remodeling imbalance", "Systemic skeletal disorder where bone resorption by osteoclasts outpaces bone formation by osteoblasts, leading to thinned trabeculae, high porosity, and fragile susceptibility to pathological fractures (e.g., hip, spine)", "Accelerated in postmenopausal women due to estrogen deficiency (estrogen normally induces osteoclast apoptosis)", "Excessive mineralization making bones rock-hard, Infection of bone marrow by viruses, Genetic defect in muscle fibers")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Bone (Osseous) Histology & Microarchitecture.**\n- Highly vascularized, rigid mineralized tissue: \\(65\\%\\) Hydroxyapatite (compression) + \\(35\\%\\) Type I collagen (tension).\n- Compact Bone: Osteon / Haversian System = Central Haversian canal (blood vessels/nerves) + Concentric lamellae + Osteocytes in Lacunae + Radiating Canaliculi.\n- Perforating Volkmann's canals run transversely; Spongy bone has porous Trabeculae housing red marrow.\n- Cells: Osteoblasts (build bone/osteoid), Osteocytes (maintain bone/lacunae), Osteoclasts (multinucleated, resorb bone).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Osteological / Pathological Significance:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 6: Fluid Connective Tissue: Blood (Plasma, RBCs, WBCs, Platelets)
    arch6 = {
        'templates': [
            "What distinct hematological and physiological feature defines: '{0}'?:",
            "In fluid connective tissue (blood): '{0}' is characterized by:",
            "Consider blood cellular and plasma elements: '{0}' functions to:",
            "Which statement precisely describes the biology of: '{0}'?:",
            "A hematologist evaluates a peripheral blood smear: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' transport gases, defend against pathogens, or maintain hemostasis?:",
            "Evaluate the hematological component: '{0}':",
            "Why is blood classified as a fluid connective tissue?:",
            "What structural/cytological property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Blood as a Fluid Connective Tissue", "A circulating fluid connective tissue consisting of a straw-colored liquid extracellular matrix (Plasma, \\(\\approx 55\\%\\)) and suspended cellular elements (Formed Elements, \\(\\approx 45\\%\\))", "Connects all organ systems through systemic transport of oxygen, nutrients, hormones, metabolic wastes, and heat; originates from embryonic mesoderm", "Tissue composed of dead lignified tubes, Dense solid tissue holding joints together, Epithelial sheet lining the heart"),
            ("Blood Plasma composition", "Aqueous solution (\\(90\\text{--}92\\%\\text{ water}\\)) containing \\(6\\text{--}8\\%\\) plasma proteins (Albumin for colloid osmotic pressure; Globulins for immunity; Fibrinogen for blood clotting), electrolytes (\\(\\text{Na}^+, \\text{Cl}^-, \\text{HCO}_3^-\\)), glucose, and metabolic wastes", "Maintains blood volume, systemic pH (\\(7.35\\text{--}7.45\\)), and colloid osmotic pressure (\\(\\approx 25\\text{ mmHg}\\))", "Pure distilled water without dissolved proteins, 90% lipid emulsion, Liquid containing only dead hemoglobin"),
            ("Erythrocytes (RBCs - Red Blood Cells)", "Biconcave disc-shaped, enucleated cells in mature mammals (\\(7.2\\text{ }\\mu\\text{m}\\) diameter), packed with hemoglobin (\\(\\approx 280\\text{ million molecules/cell}\\))", "Biconcave shape maximizes surface-area-to-volume ratio for gas diffusion; lacks nucleus, mitochondria, and ER to devote 100% volume to \\(\\text{O}_2\\) transport; life span \\(\\approx 120\\text{ days}\\)", "Spherical nucleated cells dividing actively in blood, Spindle-shaped cells forming fibers, Phagocytic cells that engulf bacteria"),
            ("Leukocytes (WBCs - White Blood Cells)", "Nucleated, amoeboid, motile defense cells (count: \\(4,000\\text{ to }11,000\\text{ cells/}\\mu\\text{L}\\)); divided into Granulocytes (Neutrophils, Eosinophils, Basophils) and Agranulocytes (Lymphocytes, Monocytes)", "Defends the host against bacterial, viral, fungal pathogens and foreign antigens; capable of squeezing through capillary walls (diapedesis)", "Enucleated cells transporting oxygen, Small fragments forming blood clots, Cells that synthesize bone mineral"),
            ("Neutrophils (Polymorphonuclear leukocytes / PMNs)", "Most abundant WBC (\\(50\\text{--}70\\%\\)); possesses a characteristic 3 to 5 lobed nucleus and fine neutral-staining granules", "First cellular responders to acute bacterial infection; rapidly phagocytose and destroy bacteria via respiratory burst (ROS) and neutrophil extracellular traps (NETs)", "Cells that secrete histamine during allergy, Cells producing antibodies, Cells that transport carbon dioxide"),
            ("Lymphocytes (B cells, T cells, NK cells)", "Second most abundant WBC (\\(20\\text{--}40\\%\\)); possesses a large, darkly staining spherical nucleus with a thin rim of pale blue cytoplasm", "Key mediators of adaptive immunity: B-cells differentiate into plasma cells secreting antibodies; T-cells direct cell-mediated immunity and cytokine regulation", "Phagocytic cells eating large cellular debris, Cells containing heparin granules, Cells that carry hemoglobin"),
            ("Monocytes and Macrophages", "Largest circulating blood cells (\\(12\\text{--}20\\text{ }\\mu\\text{m}\\)) with a characteristic kidney-shaped or indented nucleus and abundant agranular cytoplasm (\\(3\\text{--}8\\%\\))", "Circulate in blood for 1-3 days before migrating into tissues to differentiate into resident macrophages (histiocytes, Kupffer cells, microglia, alveolar dust cells)", "Small cells producing antibodies, Granular cells destroying parasites, Cells that initiate blood clotting"),
            ("Eosinophils and Basophils", "Eosinophils (bilobed nucleus, coarse red-orange granules): defend against parasitic helminth worms and modulate allergic reactions; Basophils (S-shaped nucleus, coarse dark purple granules): secrete histamine, heparin, and leukotrienes during hypersensitivity", "Represent specialized granulocyte lineages mediating allergic responses and antiparasitic defense", "Cells carrying oxygen in lungs, Cells that dissolve blood clots, Cells forming bone matrix"),
            ("Thrombocytes (Platelets)", "Small, enucleated cytoplasmic fragments (\\(2\\text{--}4\\text{ }\\mu\\text{m}\\)) shed from giant polyploid Megakaryocytes in the bone marrow (count: \\(150,000\\text{ to }450,000/\\\mu\\text{L}\\))", "Adheres to exposed subendothelial collagen at vascular injury sites, aggregating to form a primary platelet plug and activating the coagulation cascade (clotting factors)", "Full-sized nucleated cells producing antibodies, Cells that circulate nutrients, Red cells carrying oxygen"),
            ("Blood Clotting Cascade (Hemostasis)", "Vascular spasm \\(\\rightarrow\\) Platelet plug formation \\(\\rightarrow\\) Coagulation cascade: Prothrombinase converts Prothrombin to active Thrombin (in presence of \\(\\text{Ca}^{2+}\\)); Thrombin cleaves soluble Fibrinogen into an insoluble mesh of Fibrin threads that traps blood cells to form a permanent clot", "Prevents lethal blood loss from injured vessels; failure occurs in Hemophilia (deficiency of factor VIII or IX)", "Blood clots by evaporative drying in air, Clotting is caused by red blood cells exploding, Clotting occurs only inside arteries")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Hematology & Blood Components.**\n- Fluid Connective Tissue: Plasma (\\(55\\%\\): Albumin, Globulins, Fibrinogen) + Formed Elements (\\(45\\%\\)).\n- Erythrocytes (RBCs): Biconcave, enucleated, hemoglobin, 120-day lifespan, \\(\\text{O}_2\\) transport.\n- Leukocytes (WBCs): Neutrophils (bacterial phagocytosis), Lymphocytes (B & T cells, immunity), Monocytes (macrophage precursors), Eosinophils (parasites/allergies), Basophils (histamine/heparin).\n- Platelets (Thrombocytes): Megakaryocyte fragments, primary hemostasis; Clotting: Prothrombin \\(\\rightarrow\\) Thrombin \\(\\rightarrow\\) Fibrinogen \\(\\rightarrow\\) Fibrin mesh.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Hematological / Diagnostic Significance:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 7: Quantitative & Biophysical Problems in Connective Tissue & Hematology
    arch7 = {
        'templates': [
            "{0}:",
            "Calculate the hematological or histological parameter: {0}:",
            "A quantitative hematology / connective tissue problem: {0}:",
            "Solve the quantitative physiology calculation: {0}:",
            "Compute the following physiological metric: {0}:",
            "Analyze the numerical blood count and bone mineral calculation: {0}:",
            "Determine the correct calculated hematological quantity: {0}:",
            "An analytical biomedical calculation: {0}:",
            "Find the accurate quantity for: {0}:",
            "Quantitative connective tissue evaluation: {0}:"
        ],
        'data': [
            ("A human patient has a total blood volume of \\(5.0\\text{ liters}\\) and a hematocrit (packed cell volume - PCV) of \\(45\\%\\). What is the total volume of blood plasma and red blood cell mass in this patient?", "Plasma: \\(2.75\\text{ liters}\\); RBCs: \\(2.25\\text{ liters}\\)", "\\(\\text{RBC volume} = 0.45 \\times 5.0\\text{ L} = 2.25\\text{ L}\\). \\(\\text{Plasma volume} = 5.0 - 2.25 = 2.75\\text{ L}\\) (or \\(0.55 \\times 5.0 = 2.75\\text{ L}\\))", "Plasma: 2.50 L; RBCs: 2.50 L, Plasma: 3.50 L; RBCs: 1.50 L, Plasma: 4.00 L; RBCs: 1.00 L"),
            ("A healthy adult male has a red blood cell count of \\(5.0 \\times 10^6\\text{ cells/}\\mu\\text{L}\\). How many total red blood cells are circulating in his \\(5.0\\text{ liters}\\) of blood (\\(1\\text{ L} = 10^6\\text{ }\\mu\\text{L}\\))?", "\\(2.5 \\times 10^{13}\\text{ red blood cells}\\) (\\(25\\text{ trillion}\\))", "\\(\\text{Total RBCs} = (5.0 \\times 10^6\\text{ cells/}\\mu\\text{L}) \\times (5.0 \\times 10^6\\text{ }\\mu\\text{L}) = 2.5 \\times 10^{13}\\text{ cells}\\)", "\\(2.5 \\times 10^{11}\\), \\(2.5 \\times 10^{15}\\), \\(5.0 \\times 10^{12}\\)"),
            ("Given that each gram of hemoglobin can bind \\(1.34\\text{ mL of }\\text{O}_2\\) at full saturation, how many milliliters of oxygen can be carried in \\(100\\text{ mL}\\) of blood in a person with normal hemoglobin concentration of \\(15.0\\text{ g/dL}\\)?", "\\(20.1\\text{ mL of }\\text{O}_2\\text{ per 100 mL blood}\\)", "\\(\\text{Oxygen capacity} = 15.0\\text{ g/dL} \\times 1.34\\text{ mL/g} = 20.1\\text{ mL/dL}\\) (\\(20.1\\text{ vol}\\%\\))", "15.0 mL, 26.8 mL, 13.4 mL"),
            ("If \\(2.5 \\times 10^{13}\\) red blood cells are circulating in the body and their average lifespan is 120 days, how many new red blood cells must be produced by the red bone marrow every second to maintain a steady state?", "\\(\\approx 2.41 \\times 10^6\\text{ RBCs per second}\\) (\\(\\approx 2.4\\text{ million/s}\\))", "RBCs destroyed per day \\(= 2.5 \\times 10^{13} / 120 \\approx 2.083 \\times 10^{11}\\text{ cells/day}\\). Seconds/day \\(= 86,400\\). Rate/sec \\(= 2.083 \\times 10^{11} / 86,400 \\approx 2.41 \\times 10^6\\text{ cells/sec}\\)", "\\(\\approx 2.41 \\times 10^4\\), \\(\\approx 2.41 \\times 10^8\\), \\(\\approx 1.20 \\times 10^6\\)"),
            ("A dry bone specimen has mass \\(600\\text{ grams}\\). If inorganic mineral hydroxyapatite constitutes \\(65\\%\\) of bone dry weight, what is the mass of the organic collagenous matrix in this bone?", "\\(210\\text{ grams}\\)", "\\(\\text{Organic mass} = 35\\% \\times 600\\text{ g} = 0.35 \\times 600 = 210\\text{ g}\\) (Inorganic \\(= 0.65 \\times 600 = 390\\text{ g}\\))", "390 grams, 150 grams, 300 grams"),
            ("A microscopic cross-section of compact bone of area \\(4.0\\text{ mm}^2\\) reveals 36 complete Haversian systems (osteons). What is the average cross-sectional area of a single osteon?", "\\(0.111\\text{ mm}^2\\) (\\(111,111\\text{ }\\mu\\text{m}^2\\))", "\\(\\text{Area per osteon} = 4.0\\text{ mm}^2 / 36 \\approx 0.111\\text{ mm}^2\\)", "0.222 mm^2, 0.055 mm^2, 0.011 mm^2"),
            ("A differential WBC count on 200 leukocytes reveals 130 neutrophils, 50 lymphocytes, 12 monocytes, 6 eosinophils, and 2 basophils. What is the percentage of neutrophils and lymphocytes?", "Neutrophils: \\(65\\%\\); Lymphocytes: \\(25\\%\\)", "Neutrophils \\(= (130 / 200) \\times 100 = 65\\%\\). Lymphocytes \\(= (50 / 200) \\times 100 = 25\\%\\)", "Neutrophils: 50%; Lymphocytes: 40%, Neutrophils: 70%; Lymphocytes: 20%, Neutrophils: 60%; Lymphocytes: 30%"),
            ("A patient has a platelet count of \\(50,000\\text{ platelets/}\\mu\\text{L}\\) (normal range: \\(150,000\\text{ to }450,000/\\\mu\\text{L}\\)). What clinical term describes this condition, and what is the primary risk?", "Thrombocytopenia; high risk of spontaneous bruising and uncontrolled bleeding", "Thrombocytopenia refers to abnormally low platelet count, leading to prolonged bleeding time and petechiae", "Thrombocytosis; high risk of blood clots, Polycythemia; risk of stroke, Leukopenia; risk of infection"),
            ("A biconcave red blood cell has a surface area of \\(136\\text{ }\\mu\\text{m}^2\\) and volume \\(90\\text{ }\\mu\\text{m}^3\\). What is its Surface-Area-to-Volume (SA:V) ratio?", "\\(1.51\\text{ }\\mu\\text{m}^{-1}\\)", "\\(\\text{SA:V} = 136 / 90 \\approx 1.51\\text{ }\\mu\\text{m}^{-1}\\). (A sphere of the same volume would have SA \\(\\approx 97\\text{ }\\mu\\text{m}^2\\), yielding SA:V \\(\\approx 1.08\\); biconcavity provides a 40% surface area bonus)", "1.08 μm^-1, 2.00 μm^-1, 0.66 μm^-1"),
            ("If a patient's plasma volume is \\(3.0\\text{ liters}\\) and total circulating albumin is \\(120\\text{ grams}\\), what is the plasma albumin concentration in grams per deciliter (\\(\\text{g/dL}\\)) (\\(1\\text{ L} = 10\\text{ dL}\\))?", "\\(4.0\\text{ g/dL}\\) (within normal clinical range \\(3.5\\text{--}5.0\\text{ g/dL}\\))", "\\(\\text{Volume} = 30\\text{ dL}\\). Concentration \\(= 120\\text{ g} / 30\\text{ dL} = 4.0\\text{ g/dL}\\)", "40.0 g/dL, 0.4 g/dL, 2.5 g/dL")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Identify given hematological/histological quantities.**\n" + item[0] + "\n\n**Step 2: Apply the governing physiological formula.**\n" + item[2] + ".\n\n**Step 3: Conclude.**\nResult is " + item[1] + "."
        ),
        'diff': 'hard'
    }

    # Arch 8: Clinical Pathology, Hematological Disorders & Connective Tissue Diseases
    arch8 = {
        'templates': [
            "Which clinical disorder, genetic syndrome, or diagnostic test relates to: '{0}'?:",
            "In clinical medicine and connective tissue pathology: '{0}' is characterized by:",
            "What clinical insight or pathophysiological finding defines: '{0}'?:",
            "How does genetic defect or autoimmune attack disrupt: '{0}'?:",
            "A physician analyzes a clinical case: '{0}'. What is true?:",
            "Which disease mechanism explains: '{0}'?:",
            "What is the medical significance of: '{0}'?:",
            "Why is '{0}' a diagnostic cornerstone in hematology or rheumatology?:",
            "What pathological consequence results from: '{0}'?:",
            "Evaluate the clinical biomedical concept: '{0}':"
        ],
        'data': [
            ("Marfan Syndrome (Fibrillin-1 mutation)", "Autosomal dominant mutation in FBN1 gene encoding fibrillin-1, causing defective elastic fiber assembly in connective tissues", "Manifests with tall thin habitus, arachnodactyly (spider fingers), ectopia lentis (lens dislocation), and life-threatening aortic root aneurysm and dissection", "Nutritional deficiency of vitamin C, Bacterial infection of bone marrow, Genetic defect in red blood cell membranes"),
            ("Osteogenesis Imperfecta (Brittle Bone Disease)", "Mutations in COL1A1 or COL1A2 genes encoding Type I collagen, impairing bone matrix mineralization and tensile strength", "Manifests with severe bone fragility, recurrent fractures from minimal trauma, blue sclerae, and hearing loss", "Deficiency of calcium in diet, Overproduction of cartilage in joints, Destruction of blood platelets"),
            ("Sickle Cell Anemia (HbS point mutation)", "Single base substitution (GAG \\(\\rightarrow\\) GTG) replacing glutamic acid with hydrophobic valine at position 6 of the beta-globin chain", "Under hypoxia, deoxygenated HbS polymerizes into rigid helical fibers that deform RBCs into sickle shapes, causing painful vaso-occlusive crises, hemolysis, and organ infarction", "Mutation in alpha-globin chain, Deletion of entire hemoglobin gene, Autoimmune attack on bone marrow"),
            ("Hemophilia A and B (Coagulation factor deficiencies)", "X-linked recessive bleeding disorders: Hemophilia A (deficiency of Factor VIII); Hemophilia B (deficiency of Factor IX)", "Causes failure of secondary hemostasis, leading to spontaneous deep hemarthroses (joint bleeding), intramuscular hematomas, and prolonged post-surgical bleeding", "Deficiency of platelets, Overproduction of fibrin, Bacterial infection of liver"),
            ("Rheumatoid Arthritis (Autoimmune Synovitis)", "Autoimmune disorder where chronic inflammation of the synovial membrane leads to synovial proliferation (pannus formation)", "Pannus releases collagenases and cytokines that enzymatically erode articular cartilage and underlying bone, causing joint deformity and ankylosis", "Wear-and-tear loss of cartilage without inflammation, Nutritional deficiency of vitamin D, Uric acid crystal deposition in joints"),
            ("Gout (Monosodium urate crystal arthropathy)", "Hyperuricemia leads to precipitation of needle-shaped, negatively birefringent monosodium urate crystals in synovial fluid and joint tissues (especially first MTP joint / podagra)", "Triggers intense acute inflammatory response by neutrophils engulfing crystals, causing excruciating joint pain, redness, and tophi formation", "Calcium phosphate crystals in tendons, Bacterial infection of joint cartilage, Autoimmune attack on red blood cells"),
            ("Leukemia vs Leukopenia", "Leukemia: malignant uncontrolled neoplastic proliferation of abnormal, non-functional white blood cells in bone marrow and blood; Leukopenia: abnormally low white blood cell count (\\(< 4,000/\\\mu\\text{L}\\)), severely compromising host immune defenses", "Diagnosed by bone marrow aspirate and flow cytometry immunophenotyping", "Leukemia is low red blood cell count, Leukopenia is high platelet count, Both terms are identical to anemia"),
            ("Ehlers-Danlos Syndrome (EDS / Rubber man syndrome)", "Heterogeneous group of genetic disorders affecting collagen synthesis and processing (e.g., COL5A1/COL3A1 mutations or lysyl hydroxylase deficiency)", "Characterized by skin hyperextensibility, generalized joint hypermobility, tissue fragility, and high risk of vascular rupture", "Stiffening of joints like stone, Complete absence of all skin, Inability to sweat"),
            ("Erythroblastosis Fetalis (Hemolytic Disease of the Newborn)", "Occurs when an \\(\\text{Rh}^-\\) mother carries an \\(\\text{Rh}^+\\) fetus: maternal anti-Rh (anti-D) IgG antibodies cross the placenta to destroy fetal \\(\\text{Rh}^+\\) erythrocytes", "Causes severe fetal hemolytic anemia, hydrops fetalis, and kernicterus; prevented by administering Rho(D) immune globulin (RhoGAM) to the mother", "ABO incompatibility between father and child, Infection of fetus by bacteria, Deficiency of iron in maternal diet"),
            ("Complete Blood Count (CBC) with Differential", "Routine automated laboratory hematological profile measuring RBC count, Hemoglobin, Hematocrit, MCV, MCH, MCHC, RDW, total WBC count with 5-part differential, and Platelet count", "Cornerstone clinical diagnostic panel detecting anemias, acute/chronic infections, hematologic malignancies, and coagulation risks", "Measures blood pressure, Counts heart beats per minute, Tests liver digestive enzymes")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Clinical Connective Tissue & Hematological Pathology.**\n- Genetic ECM defects: Marfan (Fibrillin-1 \\(\\rightarrow\\) aortic dissection); Osteogenesis Imperfecta (Type I collagen \\(\\rightarrow\\) brittle bones); Ehlers-Danlos (collagen \\(\\rightarrow\\) joint hypermobility).\n- Hematologic: Sickle Cell (Glu6Val on \\(\\beta\\)-globin \\(\\rightarrow\\) vaso-occlusion); Hemophilia A/B (Factor VIII/IX deficiency \\(\\rightarrow\\) joint hemarthroses); Erythroblastosis fetalis (Rh mismatch).\n- Joint diseases: Rheumatoid (autoimmune synovitis/pannus); Gout (monosodium urate crystals).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Clinical / Pathological Significance:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-3-3.3.2", "Connective tissues: Blood, bone, cartilage, ligaments, tendons, areolar, adipose", archs)


# ==========================================
# 3.3.3: Muscular tissue: Striated, smooth, cardiac
# ==========================================
def gen_3_3_3():
    # Arch 1: Striated (Skeletal) Muscle Histology & Sarcomere Architecture
    arch1 = {
        'templates': [
            "What distinct histological and ultrastructural feature characterizes: '{0}'?:",
            "In skeletal muscle histology: '{0}' is recognized by:",
            "Consider striated muscle architecture: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A muscle physiologist examines skeletal muscle contraction: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' generate voluntary skeletal locomotion?:",
            "Evaluate the myofibrillar component: '{0}':",
            "Why is '{0}' called a syncytial, voluntary, striated tissue?:",
            "What structural property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Skeletal (Striated) Muscle general histology", "Long, unbranched, cylindrical muscle fibers arranged in parallel bundles, displaying prominent alternating light and dark transverse striations", "Multinucleated syncytium with peripherally placed oval nuclei directly beneath the sarcolemma; under voluntary somatic nervous control", "Short spindle-shaped unstriated involuntary cells, Branched cells with central nuclei and intercalated discs, Non-contractile connective tissue"),
            ("Sarcomere (Fundamental functional unit of contraction)", "The segment of a myofibril bounded between two consecutive Z-discs (Z-lines) (relaxed length \\(\\approx 2.0\\text{ to }2.5\\text{ }\\mu\\text{m}\\))", "Contains an entire dark A-band and two flanking halves of light I-bands; shortens during muscle contraction as thin filaments slide past thick filaments", "The entire length of an unbranched muscle fiber, The space between two neuromuscular junctions, A cluster of mitochondria inside muscle"),
            ("A-Band (Anisotropic band) vs I-Band (Isotropic band)", "A-band: dark central band of constant length (\\(\\approx 1.5\\text{ }\\mu\\text{m}\\)) containing thick myosin filaments and overlapping thin actin filaments; I-band: light band containing only thin actin filaments anchored to the central Z-disc", "Birefringent under polarized light (Anisotropic = A-band; Isotropic = I-band)", "A-band disappears during contraction while I-band expands, Both bands are identical in protein content, A-band contains only actin"),
            ("H-Zone and M-Line", "H-zone: pale central region of the A-band containing only thick myosin filaments without thin filament overlap; M-line: dark protein line (myomesin) in the center of the H-zone holding thick filaments in alignment", "H-zone narrows and completely disappears during maximal muscle contraction", "H-zone contains only actin filaments, M-line anchors thin filaments, M-line is found inside the nucleus"),
            ("Z-Disc (Z-line / Zwischenscheibe)", "Dense transverse protein disc (\\(\\alpha\\)-actinin) that anchors the barbed (+) ends of thin actin filaments, defining the boundary of each sarcomere", "Z-discs are pulled closer together during contraction, reducing total sarcomere length", "Anchors thick myosin filaments in the center, Transmits electrical signals across the fiber, Membrane surrounding the whole muscle"),
            ("Thick Myosin Filaments (Myosin II)", "Composed of \\(\\approx 300\\) myosin II molecules; each molecule consists of two heavy chains forming a coiled-tail and two globular heads containing actin-binding sites and ATPase catalytic activity", "Myosin heads swivel as cross-bridges to pull thin actin filaments towards the center of the sarcomere during the power stroke", "Composed of actin, troponin, and tropomyosin, Thin filament anchored to Z-disc, Filament that does not hydrolyze ATP"),
            ("Thin Actin Filaments (F-Actin, Tropomyosin, Troponin)", "Two twisted helical strands of filamentous actin (F-actin) associated with two regulatory proteins: Tropomyosin (blocks myosin-binding sites in relaxed state) and Troponin complex (TnT, TnI, TnC)", "Troponin C (TnC) binds \\(\\text{Ca}^{2+}\\), inducing a conformational shift in tropomyosin that unmasks myosin-binding sites on actin", "Thick filament with cross-bridge heads, Composed purely of structural collagen, Filaments that generate heat without moving"),
            ("Sarcoplasmic Reticulum (SR) and Terminal Cisternae", "Specialized smooth endoplasmic reticulum network surrounding each myofibril, forming expanded terminal cisternae that store high concentrations of calcium ions (\\(\\text{Ca}^{2+}\\))", "Rapidly releases \\(\\text{Ca}^{2+}\\) into sarcoplasm via ryanodine receptors (RyR1) upon depolarization, triggering contraction", "Synthesizes glycogen and secretes digestive enzymes, Generates ATP via aerobic respiration, Encloses the nucleus"),
            ("Transverse Tubules (T-Tubules) and Triad", "Deep invaginations of the sarcolemma (plasma membrane) that penetrate perpendicular to the fiber axis at the A-I junction", "Forms a 'Triad' with two flanking SR terminal cisternae; rapidly conducts action potentials from the cell surface deep into the interior of the muscle fiber", "Connects muscle to adjacent bones, Pores that excrete lactic acid, Channels through which red blood cells travel"),
            ("Connective Tissue Sheaths: Epimysium, Perimysium, Endomysium", "Epimysium surrounds the entire muscle belly; Perimysium surrounds bundles of muscle fibers (fascicles); Endomysium surrounds each individual muscle fiber", "Unites muscle fibers mechanically, transmitting the collective tensile pull continuously into the tendon attached to bone", "Sheaths are made of epithelial cells, Enclose individual sarcomeres inside fibers, Found only in the brain")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Skeletal Muscle Histology & Sarcomere Structure.**\n- Multinucleated syncytium, unbranched, peripheral nuclei, voluntary, striated.\n- Sarcomere (Z-disc to Z-disc): A-band (thick myosin + overlap, constant length), I-band (thin actin only), H-zone (myosin only, disappears in contraction), M-line (center).\n- Triad = Central T-tubule + 2 SR terminal cisternae (transmits action potential \\(\\rightarrow\\) \\(\\text{Ca}^{2+}\\) release).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Ultrastructural / Mechanical Detail:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 2: Sliding Filament Theory, Cross-Bridge Cycle & Neuromuscular Junction
    arch2 = {
        'templates': [
            "What molecular event and biochemical step governs: '{0}'?:",
            "In the Sliding Filament Theory (Huxley & Hanson 1954): '{0}' is characterized by:",
            "Consider the cross-bridge cycle: '{0}' functions to:",
            "Which statement precisely describes the sequence of: '{0}'?:",
            "A biophysicist investigates actomyosin mechanics: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' couple ATP hydrolysis to mechanical power strokes?:",
            "Evaluate the neuromuscular synaptic event: '{0}':",
            "Why is '{0}' essential for sustained excitation-contraction coupling?:",
            "What biochemical state corresponds to: '{0}'?:"
        ],
        'data': [
            ("Neuromuscular Junction (Motor End Plate)", "Specialized chemical synapse between the axon terminal of an alpha-motor neuron and the folded sarcolemma of a skeletal muscle fiber", "Action potential triggers \\(\\text{Ca}^{2+}\\)-mediated exocytosis of Acetylcholine (ACh); ACh binds to nicotinic receptors, causing \\(\\text{Na}^+\\) influx and muscle end-plate potential (EPP)", "Electrical synapse with gap junctions, Site where muscle attaches directly to bone, Synapse releasing inhibitory GABA"),
            ("Acetylcholinesterase (AChE) termination", "Enzyme anchored in the synaptic basal lamina that rapidly hydrolyzes acetylcholine into acetate and choline within milliseconds", "Prevents continuous, uncontrolled muscle firing and spastic paralysis; inhibited by organophosphate nerve agents and sarin", "Synthesizes acetylcholine from amino acids, Transports calcium back into SR, Hydrolyzes ATP inside sarcomere"),
            ("Sliding Filament Theory (Huxley & Hanson / A.F. Huxley 1954)", "Muscle contraction occurs by the active sliding of thin actin filaments over thick myosin filaments towards the center of the sarcomere", "During contraction: Sarcomere shortens, I-band narrows, H-zone disappears, while the A-band length remains completely constant", "Muscle shortens because filaments contract like rubber bands, Thick filaments dissolve into fluid, Thin filaments expand in length"),
            ("Cross-bridge Attachment (Myosin binding to Actin)", "In the presence of \\(\\text{Ca}^{2+}\\) (bound to TnC), energized myosin heads (carrying ADP + Pi) bind to newly exposed myosin-binding sites on actin", "Forms the high-affinity actomyosin cross-bridge complex", "Occurs only in the total absence of calcium, Requires immediate uncoupling of ATP, Binds myosin directly to the Z-disc"),
            ("Power Stroke (Force Generation)", "Release of Pi and ADP triggers a conformational rotation of the myosin head around its neck hinge from \\(90^\\circ\\) to \\(45^\\circ\\)", "Pulls the attached thin actin filament \\(\\approx 10\\text{ nm}\\) towards the M-line of the sarcomere, generating mechanical tension", "Pushes the thin filament away from the M-line, Causes immediate relaxation of the fiber, Occurs upon binding a new ATP molecule"),
            ("Cross-bridge Detachment by ATP Binding", "Binding of a new ATP molecule to the nucleotide pocket on the myosin head causes an allosteric conformational shift, drastically reducing affinity for actin", "Cross-bridge detaches cleanly from the actin filament; lack of ATP prevents detachment, causing rigor mortis", "ATP binding causes the power stroke, ATP binding cements myosin permanently to actin, Detachment occurs by calcium efflux"),
            ("ATP Hydrolysis and Myosin Head Re-cocking", "Myosin ATPase hydrolyzes bound ATP into ADP and Pi, which remain bound to the head", "The released free energy re-cocks the myosin head back to its high-energy \\(90^\\circ\\) resting orientation, primed for the next cycle", "Hydrolysis detaches the head from actin, Converts myosin into actin, Releases heat without resetting the head"),
            ("Rigor Mortis after death", "Upon somatic death, cellular respiration stops, depleting ATP; without ATP, myosin cross-bridges cannot detach from actin, locking muscles in a rigid contracted state", "Begins 2-4 hours post-mortem, peaks at 12 hours, and gradually resolves as lysosomal enzymes autolyze myofibrillar proteins", "Caused by sudden massive production of ATP, Immediate flaccid paralysis that never stiffens, Caused by lack of calcium"),
            ("SERCA Pump (Sarco/Endoplasmic Reticulum \\(\\text{Ca}^{2+}\\)-ATPase)", "ATP-driven calcium pump in the SR membrane that actively pumps \\(\\text{Ca}^{2+}\\) from sarcoplasm back into the SR lumen against a steep 10,000-fold concentration gradient", "Reduces cytoplasmic \\([\\text{Ca}^{2+}]\\) below \\(10^{-7}\\text{ M}\\), allowing troponin-tropomyosin to re-block actin sites and induce muscle relaxation", "Releases calcium during action potentials, Pumps calcium out of the cell across sarcolemma, Synthesizes ATP from ADP"),
            ("Motor Unit definition (Sherrington)", "A single alpha-motor neuron and all the individual skeletal muscle fibers that it innervates", "Small motor units (3-10 fibers/neuron e.g., extraocular and hand muscles) provide fine precision control; Large motor units (hundreds to thousands of fibers/neuron e.g., gastrocnemius) provide gross powerful force", "An entire muscle belly and its tendon, The collection of all motor neurons in spinal cord, A single myofibril and its mitochondria")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand the Cross-Bridge Cycle & Sliding Filament Mechanism.**\n- Sliding Filament Theory: Actin slides over myosin towards M-line; Sarcomere shortens, I-band narrows, H-zone disappears, A-band stays CONSTANT.\n- Cross-bridge Cycle: \\(\\text{Ca}^{2+}\\) binds TnC \\(\\rightarrow\\) Tropomyosin shifts \\(\\rightarrow\\) Myosin-ADP-Pi binds Actin \\(\\rightarrow\\) Pi release drives Power Stroke (\\(10\\text{ nm}\\)) \\(\\rightarrow\\) ATP binds causing Detachment \\(\\rightarrow\\) ATP hydrolysis re-cocks head.\n- Rigor mortis: No ATP \\(\\rightarrow\\) cross-bridges cannot detach.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Biophysical Detail:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    # Arch 3: Smooth Muscle Histology, Calmodulin & Involuntary Visceral Control
    arch3 = {
        'templates': [
            "What distinct histological and physiological feature characterizes: '{0}'?:",
            "In involuntary visceral muscle histology: '{0}' is recognized by:",
            "Consider smooth muscle architecture: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A pharmacologist investigates gastrointestinal motility: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' sustain prolonged tonic contraction with minimal ATP expenditure?:",
            "Evaluate the smooth muscle structural feature: '{0}':",
            "Why is '{0}' called unstriated, involuntary, and spindle-shaped?:",
            "What cytological property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Smooth (Visceral) Muscle general histology", "Short, spindle-shaped (fusiform) cells with tapering, pointed ends and a single, centrally located oval nucleus", "Lacks transverse striations (unstriated); innervated by the autonomic nervous system (involuntary); lines hollow visceral organs (stomach, intestines, blood vessels, bronchi, bladder, uterus)", "Long cylindrical multinucleated syncytium, Branched fibers with intercalated discs, Striated voluntary muscle"),
            ("Absence of Sarcomeres and Striations", "Myosin and actin filaments are not arranged in regular, repeating, parallel paracrystalline arrays, hence striations are completely absent under light microscopy", "Actin and myosin criss-cross obliquely throughout the cytoplasm in a loose diamond lattice anchored to dense bodies", "Contains regular A-bands and I-bands like skeletal muscle, Completely lacks actin and myosin, Contains only thick collagen fibers"),
            ("Dense Bodies and Intermediate Filaments", "Dense bodies (composed of \\(\\alpha\\)-actinin) are scattered in the cytoplasm and attached to the inner surface of the sarcolemma, serving as functional equivalents of Z-discs", "Interconnected by intermediate filaments (desmin / vimentin) and actin filaments, transmitting contractile tension to the cell surface", "Enclosed inside the nucleus, Organelles producing ATP, Specialized calcium pumps"),
            ("Calmodulin and Myosin Light Chain Kinase (MLCK)", "Smooth muscle completely lacks Troponin; \\(\\text{Ca}^{2+}\\) binds to Calmodulin, and the \\(\\text{Ca}^{2+}\\text{-Calmodulin}\\) complex activates Myosin Light Chain Kinase (MLCK)", "MLCK phosphorylates the regulatory light chain of myosin, enabling the myosin head to bind actin and initiate cross-bridge cycling", "Troponin C binds calcium to move tropomyosin, Myosin is phosphorylated by troponin T, Actin is directly cleaved by enzymes"),
            ("Myosin Light Chain Phosphatase (MLCP) and Relaxation", "Relaxation occurs when intracellular \\([\\text{Ca}^{2+}]\\) drops and MLCP dephosphorylates the myosin light chain, inactivating the myosin head", "Regulated by cyclic nucleotides (cAMP, cGMP) that activate MLCP to induce vasodilation and bronchodilation (e.g., nitric oxide, nitroglycerin)", "Phosphorylates actin to stop contraction, Destroys all intracellular ATP, Triggers immediate cell division"),
            ("Latch-State Mechanism (Prolonged tonic contraction)", "Dephosphorylated myosin heads remain attached to actin for extended periods before detaching, maintaining high isometric tension with \\(< 1/100\\text{th}\\) the ATP consumption of skeletal muscle", "Allows blood vessels (arterioles) to maintain baseline vasomotor tone and sphincters to stay contracted indefinitely without fatiguing", "Skeletal muscle mechanism producing tetanus, State where muscle is paralyzed permanently, Rapid twitch contraction"),
            ("Single-Unit (Unitary / Visceral) Smooth Muscle", "Sheets of smooth muscle cells interconnected by abundant Gap Junctions, functioning electrically and mechanically as a coordinated single functional syncytium", "Displays spontaneous autorhythmic pacemaker waves; lines the gastrointestinal tract, uterus, ureters, and bladder", "Each muscle cell is stimulated independently by its own nerve, Found in the iris of the eye, Under strict voluntary control"),
            ("Multi-Unit Smooth Muscle", "Individual muscle fibers are insulated from each other with minimal gap junctions; each fiber is innervated independently by an autonomic nerve varicosity", "Allows fine, graded, non-propagating contraction; found in the ciliary body and iris of the eye, piloerector muscles of hair follicles, and large arteries", "Functions as a single electrical syncytium, Found in the stomach wall, Contracts rhythmically without nerves"),
            ("Varicosities and 'En Passant' Synapses", "Autonomic postganglionic axons do not form discrete motor end plates; instead, axons display swellings (varicosities) that release neurotransmitters (norepinephrine, acetylcholine) into wide synaptic clefts", "Diffuses broadly over entire sheets of smooth muscle cells ('synapses en passant')", "Single axon ending forming a motor plate, Electrical synapse via gap junctions only, Completely lacks neurotransmitters"),
            ("Plasticity and Stress-Relaxation (Hollow organ accommodation)", "When stretched (e.g., as the stomach fills with food or bladder fills with urine), smooth muscle initially generates tension, then rapidly relaxes to baseline tension at the new longer length", "Enables hollow storage organs to accommodate massive volume changes without premature, painful increases in internal wall pressure", "Stretching causes smooth muscle to rupture instantly, Causes permanent irreversible contraction, Prevents any volume expansion")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Smooth (Visceral) Muscle Biology.**\n- Spindle-shaped (fusiform), single central nucleus, involuntary (autonomic), unstriated (no sarcomeres/troponin).\n- Thin/thick filaments criss-cross obliquely, anchored to Dense Bodies (\\(\\alpha\\)-actinin).\n- Contraction: \\(\\text{Ca}^{2+}\\) binds Calmodulin \\(\\rightarrow\\) activates MLCK \\(\\rightarrow\\) phosphorylates myosin light chain \\(\\rightarrow\\) cross-bridge cycling. Latch-state maintains tone with minimal ATP.\n- Unitary (gap junctions, coordinated syncytium e.g., GI tract) vs Multi-unit (independent fibers e.g., iris, piloerector).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Physiological / Pharmacological Significance:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Cardiac Muscle Histology, Intercalated Discs & Autorhythmicity
    arch4 = {
        'templates': [
            "What distinct histological and electrophysiological feature characterizes: '{0}'?:",
            "In myocardial histology and cardiac physiology: '{0}' is recognized by:",
            "Consider cardiac muscle architecture: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A cardiologist examines myocardial tissue: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' ensure synchronized, fatigue-free lifelong pumping of the heart?:",
            "Evaluate the cardiac muscular feature: '{0}':",
            "Why is cardiac muscle described as an involuntary, striated, branching syncytium?:",
            "What structural property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Cardiac Muscle (Myocardium) general histology", "Short, branched, cylindrical cardiomyocytes with one or two centrally located oval nuclei and prominent transverse striations", "Joined end-to-end by specialized junctional complexes termed Intercalated Discs; involuntary and highly resistant to fatigue", "Long unbranched multinucleated syncytium, Spindle-shaped unstriated involuntary cells, Non-contractile fibrous tissue"),
            ("Intercalated Discs (Junctional complexes)", "Specialized step-like transverse boundaries joining adjacent cardiomyocytes end-to-end, consisting of three distinct junctional specializations", "Mechanically binds cardiomyocytes and provides low-resistance electrical coupling, allowing the entire myocardium to contract as a functional syncytium", "Simple open holes without membranes, Lignified secondary cell walls, Loose connective tissue sheaths"),
            ("Transverse Component of Intercalated Discs (Fascia Adherens & Desmosomes)", "Fascia adherens anchors terminal actin filaments of the last sarcomere; Maculae adherentes (desmosomes) anchor intermediate filaments", "Provides immense mechanical tensile anchorage, preventing cardiomyocytes from pulling apart during vigorous systolic pumping", "Channels that transmit electrical currents, Waterproof seals preventing all fluid movement, Sites where glycogen is stored"),
            ("Longitudinal Component of Intercalated Discs (Gap Junctions / Nexus)", "Located along the lateral, longitudinal parallel faces of the intercalated disc step, containing abundant connexin-43 channels", "Allows rapid electrical ionic current (\\(\\text{Na}^+, \\text{Ca}^{2+}\\)) to flow directly from cardiomyocyte to cardiomyocyte, synchronizing action potential propagation across the atria and ventricles", "Mechanical rivets preventing cell tearing, Tight barriers blocking ions, Sensory receptors for adrenaline"),
            ("Functional Syncytium (vs Anatomical Syncytium)", "Myocardium is a Functional Syncytium because cells are distinct individual mononucleated cells joined electrically by gap junctions; Skeletal muscle is an Anatomical Syncytium formed by embryonic fusion of myoblasts into a single multinucleated cell", "An action potential generated anywhere in the atrial or ventricular myocardium spreads automatically across all cells, ensuring an all-or-none coordinated beat", "Myocardium consists of a single giant cell with 10,000 nuclei, Cardiac muscle lacks cell boundaries, Skeletal muscle is made of separate cells joined by gap junctions"),
            ("Diad system in Cardiac Muscle (vs Triad in Skeletal)", "T-tubules are located at the Z-discs (larger diameter than in skeletal muscle) and associate with a single terminal cistern of sarcoplasmic reticulum to form a Diad", "Coupled with massive influx of extracellular calcium during the action potential plateau phase (\\(\\text{Ca}^{2+}\\)-induced \\(\\text{Ca}^{2+}\\) release via RyR2)", "Consists of 3 T-tubules and 4 cisternae, Lacks T-tubules completely, Identical to skeletal muscle triads"),
            ("Calcium-Induced Calcium Release (CICR)", "Depolarization opens L-type voltage-gated calcium channels (dihydropyridine receptors - DHPR) in T-tubules; incoming trigger \\(\\text{Ca}^{2+}\\) binds to ryanodine receptors (RyR2) on SR, releasing massive \\(\\text{Ca}^{2+}\\) stores into sarcoplasm", "Cardiac contraction depends strictly on extracellular calcium influx; skeletal muscle does not require extracellular calcium influx for single twitches", "Calcium is pumped directly into mitochondria, Calcium is released without any depolarization, Sarcoplasmic reticulum lacks all calcium"),
            ("Mitochondrial density and Fatigue Resistance in Myocardium", "Mitochondria occupy nearly \\(40\\%\\) of total cardiomyocyte cell volume, densely packed with cristae and rich in myoglobin and oxidative enzymes", "Relies entirely on continuous aerobic oxidative phosphorylation (burns fatty acids, lactate, glucose); completely fatigue-resistant throughout an individual's lifetime", "Relies on anaerobic glycolysis like white muscle, Fatigues after 50 heartbeats, Lacks mitochondria entirely"),
            ("Absolute Refractory Period in Cardiac Muscle (\\(\\approx 250\\text{ ms}\\))", "Prolonged plateau phase of the cardiac action potential (mediated by sustained \\(\\text{Ca}^{2+}\\) influx) keeps the myocardium in an absolute refractory state until mechanical contraction is nearly complete", "Prevents tetanic contractions (tetany/cramping) in the heart, ensuring alternating phases of systolic contraction and diastolic filling essential for pumping blood", "Refractory period lasts only 1 millisecond like nerves, Allows heart to undergo continuous tetanic cramping, Heart contracts without relaxing"),
            ("Autorhythmicity and Cardiac Conduction System (SA Node, AV Node, Purkinje Fibers)", "Specialized modified cardiomyocytes (Sinoatrial node - SA node) display spontaneous diastolic depolarization (funny current \\(I_f\\)), generating intrinsic electrical impulses without external nerve input", "Autonomic nerves (vagus and sympathetic) modulate heart rate (chronotropy), but the heartbeat originates intrinsically within cardiac tissue (myogenic heart)", "Heart requires continuous motor nerve firing from brain to beat, Heartbeat originates in skeletal muscles, SA node is composed of dense bone")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Cardiac Muscle (Myocardium) Biology.**\n- Branched cylindrical cells, 1-2 central nuclei, striated, involuntary, myogenic autorhythmicity (SA node).\n- Intercalated Discs = Transverse Fascia Adherens & Desmosomes (mechanical tensile anchorage) + Longitudinal Gap Junctions (electrical coupling \\(\\rightarrow\\) Functional Syncytium).\n- Diad system at Z-discs; \\(\\text{Ca}^{2+}\\)-Induced \\(\\text{Ca}^{2+}\\) Release (CICR); \\(40\\%\\) volume mitochondria (fatigue-resistant aerobic metabolism).\n- Long absolute refractory period (\\(250\\text{ ms}\\)) prevents fatal tetany.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Electrophysiological / Clinical Significance:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 5: Comparative Matrix: Skeletal vs Smooth vs Cardiac Muscle
    arch5 = {
        'templates': [
            "Which row in the comparative table correctly contrasts: '{0}'?:",
            "In comparing the three muscle tissue types: '{0}' is characterized by:",
            "Consider muscular tissue classification: '{0}' demonstrates that:",
            "Which statement presents a 100% accurate contrast: '{0}'?:",
            "A histological summary matrix features: '{0}'. The accurate entry is:",
            "Compare Skeletal, Smooth, and Cardiac muscles: '{0}' is accurately stated as:",
            "Which comparative muscle fact holds true for: '{0}'?:",
            "Select the correct pairing for: '{0}':",
            "In an analytical examination question: '{0}' is correctly described by:",
            "Evaluate the muscular tissue comparison: '{0}':"
        ],
        'data': [
            ("Cell shape and Branching pattern", "Skeletal: Long cylindrical, unbranched; Smooth: Short spindle-shaped (fusiform), unbranched; Cardiac: Short cylindrical, branched", "Cardiomyocyte branching allows 3D mechanical meshwork formation in ventricular walls", "Skeletal is branched, Smooth is cylindrical, Cardiac is spindle-shaped; All three are unbranched cylinders; Smooth is multinucleated cylinder"),
            ("Nuclear number and location", "Skeletal: Multinucleated syncytium, peripheral nuclei directly beneath sarcolemma; Smooth: Uninucleated, single central oval nucleus; Cardiac: Uninucleated (or binucleated), single central nucleus", "Peripheral nuclear positioning in skeletal muscle avoids interfering with central contracting myofibril filaments", "Skeletal has central nuclei, Smooth has 50 peripheral nuclei, Cardiac has no nuclei"),
            ("Presence of Striations and Sarcomeres", "Skeletal: Present (prominent striations with regular sarcomeres); Smooth: Completely absent (unstriated, no sarcomeres); Cardiac: Present (striated with regular sarcomeres)", "Regular paracrystalline alignment of thick and thin filaments produces light-refracting striations in skeletal and cardiac muscle", "Smooth is striated while cardiac is unstriated, All three are unstriated, Skeletal is the only muscle with actin and myosin"),
            ("Nature of Control (Voluntary vs Involuntary)", "Skeletal: Voluntary (somatic nervous system); Smooth: Involuntary (autonomic nervous system + hormones); Cardiac: Involuntary (myogenic autorhythmicity modulated by autonomic nerves)", "Skeletal muscle requires conscious motor cortex motor unit recruitment", "Skeletal is involuntary while smooth is voluntary, All three are strictly voluntary, Cardiac is under conscious voluntary control"),
            ("Calcium regulatory sensor protein", "Skeletal: Troponin (Troponin C binds \\(\\text{Ca}^{2+}\\)); Smooth: Calmodulin (activates MLCK); Cardiac: Troponin (Troponin C binds \\(\\text{Ca}^{2+}\\))", "Smooth muscle lacks troponin entirely and depends on myosin light chain phosphorylation", "Smooth uses troponin while skeletal uses calmodulin, All three use hemoglobin, Skeletal uses calmodulin only"),
            ("Intercellular connections and Gap Junctions", "Skeletal: Completely absent (each fiber is electrically insulated by endomysium); Smooth: Abundant gap junctions in single-unit smooth muscle; Cardiac: Abundant gap junctions localized in intercalated discs", "Absence of gap junctions in skeletal muscle allows fine graded recruitment of independent motor units", "Skeletal has massive gap junctions linking all fibers, Cardiac lacks gap junctions, Smooth lacks all cell junctions"),
            ("Speed of contraction and Fatigue susceptibility", "Skeletal: Rapid, powerful contraction, susceptible to fatigue (lactic acid accumulation); Smooth: Slow, rhythmic, sustained tonic contraction, highly fatigue-resistant; Cardiac: Intermediate speed, rhythmic, completely fatigue-resistant throughout life", "Matches functional roles: sprinting/lifting (skeletal) vs peristalsis/vascular tone (smooth) vs continuous lifetime pumping (cardiac)", "Skeletal never fatigues while cardiac fatigues in 5 minutes, Smooth is the fastest contracting muscle, All three have identical contraction velocities"),
            ("T-tubule and Sarcoplasmic Reticulum system", "Skeletal: Triads at A-I junctions (2 cisternae + 1 T-tubule); Smooth: Rudimentary SR with surface caveolae (no true T-tubules); Cardiac: Diads at Z-discs (1 cistern + 1 wide T-tubule)", "Reflects the reliance on rapid internal calcium release (skeletal) vs trigger extracellular calcium influx (cardiac/smooth)", "Smooth muscle has giant triads, Cardiac has no T-tubules, Skeletal lacks sarcoplasmic reticulum"),
            ("Capacity for regeneration after injury", "Skeletal: Limited regeneration via resident quiescent satellite cells; Smooth: High regenerative capacity (smooth muscle cells can divide by mitosis); Cardiac: Minimal or virtually zero regeneration (heals by non-contractile fibrous collagen scar formation / fibrosis)", "Myocardial infarction results in permanent functional loss of contractile heart tissue replaced by stiff fibrous scar", "Cardiac regenerates completely within one week, Smooth muscle can never divide, Skeletal muscle has infinite regeneration"),
            ("Typical anatomical locations", "Skeletal: Attached to bones of the skeleton, tongue, pharynx, diaphragm; Smooth: Walls of hollow visceral organs (stomach, intestines, blood vessels, bladder, uterus); Cardiac: Confined exclusively to the myocardium of the heart and root of great vessels", "Matches structural adaptations to organ functions across the vertebrate body", "Skeletal lines internal organs, Smooth is attached to bones, Cardiac is found in lungs and liver")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Definitive Comparative Muscle Histology.**\n- Skeletal: Cylindrical, unbranched, multinucleated syncytium (peripheral), striated, voluntary (somatic), Troponin, Triad, no gap junctions, fatigable.\n- Smooth: Spindle-shaped (fusiform), uninucleate (central), unstriated (dense bodies), involuntary (autonomic), Calmodulin/MLCK, caveolae, gap junctions in unitary, fatigue-resistant (latch state).\n- Cardiac: Cylindrical, branched, 1-2 central nuclei, striated, involuntary (myogenic), Troponin, Diad, Intercalated Discs (gap junctions + desmosomes), fatigue-resistant (aerobic).\n\n**Step 2: Contrast '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Diagnostic / Evolutionary Criterion:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 6: Quantitative & Biomechanical Calculations in Muscle Physiology
    arch6 = {
        'templates': [
            "{0}:",
            "Calculate the muscle physiological or biomechanical parameter: {0}:",
            "A biophysical muscle contraction calculation: {0}:",
            "Quantitative muscle mechanics problem: {0}:",
            "Solve the quantitative muscle calculation: {0}:",
            "Analyze the numerical sarcomere shortening calculation: {0}:",
            "Determine the correct calculated mechanical quantity: {0}:",
            "An analytical muscle energetics problem: {0}:",
            "Find the accurate quantity for: {0}:",
            "Compute the following physiological rate: {0}:"
        ],
        'data': [
            ("A myofibril of resting length \\(50\\text{ mm}\\) (\\(50,000\\text{ }\\mu\\text{m}\\)) consists of sarcomeres of resting length \\(2.5\\text{ }\\mu\\text{m}\\). During a maximal isometric-to-isotonic contraction, each individual sarcomere shortens by \\(20\\%\\) (to \\(2.0\\text{ }\\mu\\text{m}\\)). What is the new total length of the myofibril, and how many sarcomeres are arranged in series?", "Length: \\(40\\text{ mm}\\); 20,000 sarcomeres in series", "\\(\\text{Sarcomeres} = 50,000 / 2.5 = 20,000\\). New sarcomere length \\(= 2.0\\text{ }\\mu\\text{m}\\). New total length \\(= 20,000 \\times 2.0\\text{ }\\mu\\text{m} = 40,000\\text{ }\\mu\\text{m} = 40\\text{ mm}\\)", "Length: 45 mm; 20,000 sarcomeres, Length: 30 mm; 10,000 sarcomeres, Length: 25 mm; 40,000 sarcomeres"),
            ("A single power stroke of a myosin head pulls an actin filament by \\(10\\text{ nm}\\) (\\(1.0 \\times 10^{-8}\\text{ m}\\)) and generates a unitary force of \\(4.0\\text{ pN}\\) (\\(4.0 \\times 10^{-12}\\text{ N}\\)). How much mechanical work is done by this single power stroke (\\(W = F \\times d\\))?", "\\(4.0 \\times 10^{-20}\\text{ Joules}\\)", "\\(W = (4.0 \\times 10^{-12}\\text{ N}) \\times (1.0 \\times 10^{-8}\\text{ m}) = 4.0 \\times 10^{-20}\\text{ J}\\) (\\(40\\text{ zJ}\\))", "\\(4.0 \\times 10^{-18}\\text{ J}\\), \\(4.0 \\times 10^{-22}\\text{ J}\\), \\(1.0 \\times 10^{-20}\\text{ J}\\)"),
            ("A human biceps brachii muscle has a physiological cross-sectional area (PCSA) of \\(30\\text{ cm}^2\\). If the maximum specific isometric tension of human skeletal muscle is \\(25\\text{ N/cm}^2\\), what is the maximum isometric force this muscle can generate?", "\\(750\\text{ Newtons}\\) (equivalent to \\(\\approx 76.5\\text{ kg}\\) hanging load)", "\\(F = \\text{PCSA} \\times \\text{Specific Tension} = 30\\text{ cm}^2 \\times 25\\text{ N/cm}^2 = 750\\text{ N}\\)", "7,500 N, 75 N, 300 N"),
            ("In a heart beating at \\(75\\text{ beats/minute}\\), what is the duration of a single complete cardiac cycle, and if ventricular systole lasts \\(0.3\\text{ seconds}\\), how much time is available for diastolic ventricular filling?", "Cycle: \\(0.8\\text{ seconds}\\); Diastole: \\(0.5\\text{ seconds}\\)", "\\(\\text{Cycle duration} = 60\\text{ s} / 75 = 0.8\\text{ seconds}\\). \\(\\text{Diastolic time} = 0.8 - 0.3 = 0.5\\text{ seconds}\\)", "Cycle: 1.0 s; Diastole: 0.7 s, Cycle: 0.6 s; Diastole: 0.3 s, Cycle: 0.8 s; Diastole: 0.3 s"),
            ("During strenuous sprinting, a skeletal muscle fiber hydrolyzes \\(1.5 \\times 10^{-3}\\text{ moles of ATP}\\) per minute. Given that ATP hydrolysis under physiological conditions yields \\(\\approx 50\\text{ kJ/mole}\\) of free energy, what is the metabolic power consumed by this muscle in Watts (\\(\\text{J/s}\\))?", "\\(1.25\\text{ Watts}\\)", "\\(\\text{Energy/min} = (1.5 \\times 10^{-3}\\text{ mol}) \\times (50,000\\text{ J/mol}) = 75\\text{ J/min}\\). Power \\(= 75\\text{ J} / 60\\text{ s} = 1.25\\text{ J/s} = 1.25\\text{ W}\\)", "12.5 W, 75.0 W, 0.125 W"),
            ("A muscle fiber action potential has a conduction velocity of \\(5\\text{ meters/second}\\). How long does it take an electrical wave to travel along a \\(10\\text{ cm}\\) (\\(0.1\\text{ meter}\\)) long skeletal muscle fiber from its central neuromuscular junction to the tendon end (distance \\(= 5\\text{ cm} = 0.05\\text{ m}\\))?", "\\(10\\text{ milliseconds}\\) (\\(0.01\\text{ s}\\))", "\\(\\text{Time} = \\text{Distance} / \\text{Velocity} = 0.05\\text{ m} / 5\\text{ m/s} = 0.01\\text{ s} = 10\\text{ ms}\\)", "1.0 ms, 50 ms, 20 ms"),
            ("In smooth muscle, the latch-state reduces cross-bridge cycling rate and ATP consumption by \\(98\\%\\) while maintaining \\(100\\%\\) tension. If baseline cycling consumes \\(500\\text{ nmol ATP/min}\\), how much ATP is consumed per minute in the latch-state?", "\\(10\\text{ nmol ATP/min}\\)", "\\(\\text{ATP consumed} = 500 \\times (1 - 0.98) = 500 \\times 0.02 = 10\\text{ nmol/min}\\)", "50 nmol/min, 1 nmol/min, 100 nmol/min"),
            ("A ventricular cardiomyocyte has volume \\(30,000\\text{ }\\mu\\text{m}^3\\). If mitochondria occupy \\(38\\%\\) of the cell volume, what is the total volume of mitochondria in this single cardiac cell?", "\\(11,400\\text{ }\\mu\\text{m}^3\\)", "\\(\\text{Mitochondrial volume} = 0.38 \\times 30,000 = 11,400\\text{ }\\mu\\text{m}^3\\)", "7,600 μm^3, 15,200 μm^3, 3,800 μm^3"),
            ("If a motor unit consists of 1 alpha-motor neuron innervating 150 muscle fibers, how many total motor units are required to control a calf muscle containing 300,000 muscle fibers?", "2,000 motor units", "\\(\\text{Number of motor units} = 300,000 / 150 = 2,000\\)", "200 motor units, 20,000 motor units, 1,500 motor units"),
            ("A resting muscle fiber has intracellular sarcoplasmic \\([\\text{Ca}^{2+}] = 0.05\\text{ }\\mu\\text{M}\\). Upon peak tetanic stimulation, \\([\\text{Ca}^{2+}]\\) rises to \\(10\\text{ }\\mu\\text{M}\\). By what factor has the free calcium concentration increased in the sarcoplasm?", "\\(200\\text{-fold increase}\\)", "\\(\\text{Fold increase} = 10\\text{ }\\mu\\text{M} / 0.05\\text{ }\\mu\\text{M} = 200\\)", "20-fold, 2,000-fold, 50-fold")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Identify given physical and physiological parameters.**\n" + item[0] + "\n\n**Step 2: Apply the governing muscular/biomechanical formula.**\n" + item[2] + ".\n\n**Step 3: Conclude.**\nResult is " + item[1] + "."
        ),
        'diff': 'hard'
    }

    # Arch 7: Neuromuscular Pathology, Toxins & Clinical Muscle Diseases
    arch7 = {
        'templates': [
            "Which clinical disorder, neurotoxin, or pharmacology mechanism relates to: '{0}'?:",
            "In neuromuscular pathology and clinical neurology: '{0}' is characterized by:",
            "What clinical insight or pathophysiological finding defines: '{0}'?:",
            "How does toxin action or genetic defect disrupt: '{0}'?:",
            "A neurologist evaluates a patient with muscle weakness: '{0}'. What is true?:",
            "Which disease mechanism explains: '{0}'?:",
            "What is the medical significance of: '{0}'?:",
            "Why is '{0}' a target in clinical therapeutics or anesthesia?:",
            "What pathological consequence results from: '{0}'?:",
            "Evaluate the neuromuscular disease concept: '{0}':"
        ],
        'data': [
            ("Myasthenia Gravis", "Autoimmune disease where autoantibodies target and destroy nicotinic acetylcholine receptors (AChR) at the post-synaptic motor end plate", "Causes progressive muscle fatiguability and weakness, typically starting in extraocular muscles (ptosis, diplopia) and worsening with exertion; treated with AChE inhibitors (pyridostigmine)", "Bacterial infection destroying muscle fibers, Autoimmune attack on myelin sheath, Defect in calcium release from bone"),
            ("Duchenne Muscular Dystrophy (DMD)", "X-linked recessive frameshift mutation in the dystrophin gene (largest human gene), causing complete absence of dystrophin protein", "Without dystrophin anchoring the actin cytoskeleton to the extracellular matrix, mechanical contraction tears the sarcolemma, causing progressive muscle necrosis, pseudo-hypertrophy, wheelchair dependence by age 12, and early death", "Nutritional deficiency of protein, Autoimmune attack on blood vessels, Excessive growth of bone inside muscle"),
            ("Botulinum Toxin (Botox / Clostridium botulinum)", "Bacterial zinc endopeptidase that selectively cleaves SNARE proteins (SNAP-25) in presynaptic motor terminals, preventing acetylcholine exocytosis", "Causes flaccid paralysis (inability of muscles to contract); used clinically for dystonias, spasticity, and cosmetic reduction of facial wrinkles", "Causes spastic tetanic contraction, Blocks sodium channels in heart, Stimulates excessive acetylcholine release"),
            ("Tetanus Toxin (Tetanospasmin / Clostridium tetani)", "Retrogradely transported to spinal cord inhibitory interneurons (Renshaw cells), cleaving synaptobrevin to block release of inhibitory neurotransmitters (GABA, glycine)", "Removes normal inhibitory feedback, causing uncontrolled continuous motor neuron firing, violent spastic contractions, lockjaw (trismus), and opisthotonos", "Causes complete flaccid limp paralysis, Dissolves bone mineral matrix, Destroys red blood cells in spleen"),
            ("Malignant Hyperthermia (RyR1 receptor defect)", "Autosomal dominant mutation in the ryanodine receptor (RyR1) in SR; volatile anesthetics (halothane) or succinylcholine trigger massive, uncontrolled \\(\\text{Ca}^{2+}\\) release into sarcoplasm", "Causes sustained muscle rigidity, hypermetabolism, extreme lactic acidosis, and lethal hyperthermia (temperature \\(> 42^\\circ\\text{C}\\)); treated immediately with Dantrolene (RyR1 antagonist)", "Caused by sudden drop in body temperature, Infection of lungs by bacteria, Allergy to penicillin antibiotics"),
            ("Curare (d-Tubocurarine) mechanism", "Competitive antagonist of nicotinic acetylcholine receptors at the neuromuscular junction, blocking ACh binding without depolarizing the membrane", "Causes flaccid skeletal muscle paralysis; historically used as arrow poison by indigenous Amazonians and as an adjunct in surgical anesthesia", "Stimulates violent muscle cramps, Destroys heart muscle cells, Increases blood pressure to dangerous levels"),
            ("Organophosphate poisoning (Nerve agents / Insecticides)", "Irreversibly inhibits acetylcholinesterase (AChE), causing massive accumulation of acetylcholine at all cholinergic synapses", "Triggers SLUDGEM toxidrome (Salivation, Lacrimation, Urination, Defecation, GI cramps, Emesis, Muscle fasciculations \\(\\rightarrow\\) flaccid paralysis due to depolarizing block); treated with Atropine and Pralidoxime (2-PAM)", "Causes sudden death by hypoglycemia, Destroys red blood cells, Blocks all nerve action potentials"),
            ("Lambert-Eaton Myasthenic Syndrome (LEMS)", "Autoimmune disorder (often a paraneoplastic syndrome associated with small cell lung cancer) with autoantibodies against presynaptic voltage-gated calcium channels (VGCC)", "Reduces calcium influx into the motor nerve terminal, impairing acetylcholine release; muscle weakness paradoxically IMPROVES with repeated exercise (unlike Myasthenia Gravis)", "Destroys muscle actin filaments, Causes permanent muscle contraction, Destroys acetylcholine receptors"),
            ("Troponin I and Troponin T as Myocardial Infarction Biomarkers", "Following myocardial ischemic necrosis (heart attack), cardiac isoforms of Troponin I (cTnI) and Troponin T (cTnT) leak out of damaged cardiomyocytes into the bloodstream", "Gold standard clinical laboratory diagnostic biomarker for diagnosing acute myocardial infarction (rises in 2-4 hours, peaks at 24 hours, persists for up to 10-14 days)", "Indicates skeletal muscle trauma only, Biomarker for kidney failure, Test for brain stroke"),
            ("Sarcopenia and Aging", "Age-related progressive, involuntary loss of skeletal muscle mass, strength, and fast-twitch glycolytic Type II muscle fibers", "Driven by motor unit denervation, declining testosterone/GH/IGF-1, chronic low-grade inflammation, and satellite cell senescence", "Excessive uncontrolled growth of muscle in elderly, Conversion of muscle into bone, Disease caused by excess protein diet")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Neuromuscular Pathology & Pharmacology.**\n- Myasthenia Gravis: Autoantibodies destroy post-synaptic AChR \\(\\rightarrow\\) fatiguable weakness (worse with use).\n- LEMS: Presynaptic \\(\\text{Ca}^{2+}\\) channel antibodies (improves with use).\n- Toxins: Botulinum (cleaves SNARE \\(\\rightarrow\\) flaccid paralysis); Tetanus (blocks GABA/glycine release in spinal cord \\(\\rightarrow\\) spastic lockjaw); Curare (AChR antagonist); Organophosphates (AChE inhibitor \\(\\rightarrow\\) SLUDGEM).\n- Genetic/Diagnostic: DMD (dystrophin frameshift); Cardiac Troponin I/T (MI biomarker); Malignant hyperthermia (RyR1 defect \\(\\rightarrow\\) Dantrolene).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Clinical / Pathological Detail:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }


    # Arch 8: Muscle Fiber Types: Red (Type I) vs White (Type II), Energetics & Fatigue
    arch8 = {
        'templates': [
            "Which physiological characteristic, metabolic pathway, or muscle fiber type defines: '{0}'?:",
            "In comparative muscle fiber physiology: '{0}' is characterized by:",
            "Consider skeletal muscle fiber diversity: '{0}' functions to:",
            "Which statement precisely describes the biology of: '{0}'?:",
            "A sports physiologist tests athletic muscle performance: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' optimize sustained endurance vs rapid explosive power?:",
            "Evaluate the myofiber specialization: '{0}':",
            "Why is '{0}' categorized under this specific metabolic phenotype?:",
            "What biochemical property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Slow-Twitch (Type I / Red) Muscle Fibers", "Slow contraction velocity, rich in myoglobin and iron (red appearance), high mitochondrial density, dense capillary beds", "Relies on aerobic oxidative phosphorylation; highly resistant to fatigue; dominates in postural antigravity muscles (soleus, erector spinae) and marathon runners", "Fast contracting fibers that fatigue in 10 seconds, Completely devoid of mitochondria, Relies solely on anaerobic glycolysis"),
            ("Fast-Twitch (Type IIx/IIb / White) Muscle Fibers", "Rapid contraction velocity, low myoglobin content (pale/white appearance), low mitochondrial density, high glycogen content and glycolytic enzymes", "Relies on rapid anaerobic glycolysis; generates explosive power but fatigues quickly due to lactic acid and \(\text{H}^+\) accumulation; dominates in sprinters, weightlifters, and extraocular eye muscles", "Slow contracting fibers that never fatigue, Red fibers rich in myoglobin, Postural muscles maintaining standing stance"),
            ("Intermediate (Type IIa / Fast Oxidative-Glycolytic) Fibers", "Fast contraction speed combined with intermediate mitochondrial density and aerobic/glycolytic capacity", "Recruited for middle-distance running, swimming, and sustained athletic power", "Pure white fibers with zero mitochondria, Spindle-shaped cells without striations, Dead muscle fibers"),
            ("Myoglobin in Red Muscle Fibers", "Monomeric heme-iron protein with high oxygen affinity (hyperbolic binding curve); stores oxygen inside sarcoplasm and facilitates \(\text{O}_2\) diffusion from capillaries to mitochondria", "Imparts deep red color to endurance muscles and marine mammal divers (seals, whales)", "Tetrameric protein circulating in blood, Protein that synthesizes lactic acid, Enzyme that hydrolyzes glycogen"),
            ("Creatine Phosphate (Phosphocreatine) Energy Shuttle", "High-energy phosphate reservoir (\(\approx 20\text{ mM}\)) in muscle sarcoplasm; Creatine Kinase (CK) transfers phosphate to ADP, regenerating ATP in \(< 1\text{ millisecond}\)", "Provides the immediate energy buffer sustaining maximal explosive exertion for the first 5 to 10 seconds (e.g., 100m sprint)", "Sustains marathon running for 5 hours, Stores glucose in liver, Dissolves lactic acid"),
            ("Oxygen Debt (Excess Post-Exercise Oxygen Consumption - EPOC)", "Elevated oxygen consumption continuing for hours post-exercise to replenish ATP and creatine phosphate stores, metabolize accumulated lactic acid (Cori cycle in liver), and re-oxygenate myoglobin", "Explains why athletes continue heavy breathing long after stopping vigorous exertion", "Permanent loss of oxygen leading to death, State where no oxygen enters lungs, Caused by lack of hemoglobin"),
            ("Lactic Acid and Muscle Fatigue (Cori Cycle)", "Intense anaerobic glycolysis converts pyruvate to lactic acid via Lactate Dehydrogenase (LDH), regenerating \(\text{NAD}^+\); lactate is shuttled to the liver and converted back into glucose (gluconeogenesis)", "Intracellular \(\text{H}^+\) ion accumulation reduces sarcoplasmic pH, inhibiting phosphofructokinase and competitive binding to troponin C, contributing to acute muscular fatigue", "Lactic acid burns muscle fibers permanently, Lactate is excreted 100% by kidneys in 1 minute, Formed by aerobic Krebs cycle"),
            ("Hypertrophy vs Hyperplasia in Muscle Growth", "Resistance strength training increases muscle size via Hypertrophy (increased myofibrillar diameter, actin/myosin protein synthesis, and satellite cell donation of nuclei); Hyperplasia (increase in cell number) is extremely limited or absent in adult human skeletal muscle", "Explains why bodybuilders develop massive muscle bellies without multiplying muscle fiber counts", "Bodybuilding increases muscle cell count by 10-fold, Hypertrophy refers to muscle death, Muscle grows by accumulating water only"),
            ("Tetanus vs Treppe (Staircase phenomenon)", "Treppe: gradual warm-up increase in twitch force when stimulated at low frequency due to warmed enzymes and residual sarcoplasmic \(\text{Ca}^{2+}\); Tetanus: smooth, sustained maximal contraction produced when stimulus frequency is so high that relaxation between twitches is completely eliminated", "Physiological basis for normal sustained voluntary motor actions", "Tetanus is a flaccid paralysis, Treppe causes permanent muscle tearing, Tetanus is a disease caused only by viruses"),
            ("Rigor Mortis resolution after 24 to 48 hours", "Post-mortem muscular rigidity gradually resolves and muscles become flaccid due to autolytic enzymatic digestion of Z-discs and cross-bridges by endogenous lysosomal cathepsins and calpains", "Marks the post-mortem transition used in forensic medicine to estimate time of somatic death", "Resolved because ATP production resumes, Resolved by drinking water, Rigor mortis never resolves")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Muscle Fiber Types & Energetics.**\n- Red Fibers (Type I): Slow-twitch, myoglobin-rich, high mitochondria/capillaries, aerobic oxidative, fatigue-resistant (postural, marathon).\n- White Fibers (Type IIx/b): Fast-twitch, low myoglobin, high glycogen/glycolytic enzymes, anaerobic, explosive power, rapid fatigue (sprinters).\n- Energy sources: ATP (1-2s) \(\rightarrow\) Creatine Phosphate (5-10s) \(\rightarrow\) Anaerobic Glycolysis (lactic acid, Cori cycle) \(\rightarrow\) Aerobic phosphorylation.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Physiological / Biomechanical Significance:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-3-3.3.3", "Muscular tissue: Striated, smooth, cardiac", archs)


# ==========================================
# 3.3.4: Nervous tissue: Neuron structure (cyton, dendrites, axon, synapse)
# ==========================================
def gen_3_3_4():
    # Arch 1: Neuron Architecture: Cyton (Soma), Dendrites, and Axon
    arch1 = {
        'templates': [
            "What distinct histological and anatomical feature defines: '{0}'?:",
            "In neurohistology: '{0}' is recognized by:",
            "Consider the structural components of a neuron: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A neuroanatomist examines nerve cell architecture: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' receive, integrate, or propagate electrical nerve impulses?:",
            "Evaluate the neuronal component: '{0}':",
            "Why is '{0}' considered a specialized structural adaptation for neural signaling?:",
            "What structural property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Neuron (Nerve Cell) General Definition", "Highly specialized, electrically excitable cells that perceive stimuli, generate action potentials, and transmit signals throughout the nervous system", "Longest cells in the human body (up to \\(1\\text{ meter}\\) in sciatic motor neurons); permanently post-mitotic in adult life (G0 arrest due to absence of centrioles)", "Tightly packed epithelial cells lining skin, Contractile syncytial cells generating force, Dead mineralized cells storing calcium"),
            ("Cyton (Soma / Perikaryon / Cell Body)", "Central metabolic and genetic hub of the neuron containing a large, spherical, euchromatic nucleus, prominent nucleolus, and abundant active organelles", "Synthesizes neurotransmitters, proteins, and structural elements required to maintain extensive axonal and dendritic arborizations", "Non-living empty tube conducting sap, Long unbranched fiber conducting impulses to muscles, Fluid space between two neurons"),
            ("Nissl Granules (Nissl Bodies)", "Dense, basophilic clumps of rough endoplasmic reticulum and free polyribosomes scattered throughout the cyton and proximal dendrites", "Site of intense protein synthesis for neuroreceptors, enzymes, and cytoskeleton; strictly ABSENT from the axon hillock and axon", "Lipid storage droplets, Starch amyloplasts, Calcium carbonate crystal inclusions"),
            ("Dendrites", "Multiple, short, highly branched, tapering protoplasmic processes extending from the cyton, covered with dendritic spines", "Act as the primary receptive antenna of the neuron, conducting graded electrical signals (EPSPs, IPSPs) centripetally towards the cell body", "Single long uniform cylinder transmitting impulses away, Non-conducting structural cords, Myelinated sheath insulating the axon"),
            ("Axon (Axis cylinder / Nerve Fiber)", "Single, long, uniform-diameter cylindrical process arising from the axon hillock, extending up to \\(1\\text{ meter}\\)", "Conducts all-or-none action potentials centrifugally away from the cyton toward target effector cells or subsequent neurons", "Short tapering receptive antenna, Cluster of basophilic rough ER, Fluid cushion protecting the brain"),
            ("Axon Hillock and Initial Segment (Trigger Zone)", "Funnel-shaped, cone-like region of the cyton where the axon originates, completely devoid of Nissl granules and Golgi complexes", "High density of voltage-gated \\(\\text{Na}^+\\) channels (Nav1.6) gives this trigger zone the lowest threshold for action potential initiation", "Site where neurotransmitters are stored in vesicles, Terminal end forming synapses with muscles, The protective outer myelin covering"),
            ("Axoplasm and Axolemma", "Axolemma: the excitable plasma membrane enclosing the axon; Axoplasm: the specialized cytoplasm of the axon containing neurofilaments, microtubules, and mitochondria", "Strictly lacks ribosomes and rough ER, relying completely on axoplasmic transport from the cyton for protein supply", "Axolemma is a dead cell wall, Axoplasm contains giant starch grains, Axolemma is made of suberin"),
            ("Axon Terminals (Telodendria / Terminal Boutons)", "The distal branched endings of an axon terminating in swollen bulbous knobs (synaptic boutons / end feet)", "Contains abundant neurotransmitter-filled synaptic vesicles and mitochondria; forms pre-synaptic elements of chemical synapses", "Receptive dendrite branches, Centrally located cell body, Protective bone casing around nerves"),
            ("Anterograde vs Retrograde Axonal Transport", "Anterograde transport (mediated by Kinesin motors moving towards (+) end): carries synaptic vesicles, enzymes, and mitochondria from soma to axon terminals; Retrograde transport (mediated by Dynein motors moving towards (-) end): returns worn-out organelles, trophic signals (NGF), and neurotropic pathogens (Rabies, Tetanus, Polio) to the soma", "Essential for neuronal survival, spanning up to \\(400\\text{ mm/day}\\) along microtubule tracks", "Anterograde moves by simple diffusion without motors, Retrograde uses myosin on actin filaments, Both are passive processes"),
            ("Centriole absence and lack of cell division in mature neurons", "Mature differentiated neurons lack functional centrosomes/centrioles, permanently preventing them from forming mitotic spindles or undergoing cell division", "Irreversible post-mitotic arrest; severed CNS axons in the brain and spinal cord cannot regenerate by cell division", "Neurons divide rapidly every 24 hours like skin, Lack nuclei entirely, Divide by binary fission like bacteria")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Neuron Cytology & Structural Architecture.**\n- Cyton (Soma): Nucleus, prominent nucleolus, Nissl granules (rough ER + ribosomes; absent in axon hillock and axon), neurofibrils.\n- Dendrites: Short, branched, tapering, receptive (centripetal conduction towards soma).\n- Axon: Single, long, uniform diameter, conductile (centrifugal conduction away from soma), begins at Axon Hillock (trigger zone: lowest threshold, dense \\(\\text{Na}^+\\) channels).\n- Axonal Transport: Anterograde (Kinesin \\(\\rightarrow\\) to terminal), Retrograde (Dynein \\(\\rightarrow\\) to soma; hijacked by Rabies/Tetanus).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Neurocytological Detail:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 2: Myelination, Schwann Cells, Oligodendrocytes & Saltatory Conduction
    arch2 = {
        'templates': [
            "What distinct histological and electrophysiological feature characterizes: '{0}'?:",
            "In peripheral vs central nervous system myelination: '{0}' is recognized by:",
            "Consider nerve impulse conduction mechanics: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A neurophysiologist investigates saltatory conduction: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' accelerate nerve impulse velocity up to 100-fold?:",
            "Evaluate the glial/myelin feature: '{0}':",
            "Why is '{0}' indispensable for rapid vertebrate reflex and cognitive speed?:",
            "What structural property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Myelin Sheath", "A multi-layered, lipid-rich insulating sheath (\\(\\approx 70\\%\\text{ lipid, }30\\%\\text{ protein}\\)) wrapped concentrically around axons", "Acts as an electrical insulator that drastically reduces membrane capacitance and increases transmembrane electrical resistance", "Conducts electricity faster than copper wire, Secretes neurotransmitters, Thick layer of cellulose"),
            ("Schwann Cells (Neurolemmocytes in PNS)", "Glial cells responsible for synthesizing and wrapping the myelin sheath around peripheral nerve fibers in the Peripheral Nervous System (PNS)", "A single Schwann cell myelinates only a SINGLE internode segment of a single axon; outer nucleated cytoplasmic layer forms the Neurilemma (sheath of Schwann)", "Myelinates 50 axons simultaneously in the brain, Found exclusively in the spinal cord, Non-living lipid crystals"),
            ("Oligodendrocytes (Myelination in CNS)", "Glial cells responsible for synthesizing myelin in the Central Nervous System (brain and spinal cord)", "A single oligodendrocyte extends multiple branching processes to myelinate internodal segments of up to \\(30\\text{ to }50\\text{ different axons}\\); strictly lacks a neurilemma", "Found exclusively in peripheral nerves, Encloses only a single axon segment, Capable of forming bone matrix"),
            ("Nodes of Ranvier", "Microscopic periodic unmyelinated gaps (\\(\\approx 1\\text{ }\\mu\\text{m}\\) long) occurring at regular \\(1\\text{ mm}\\) intervals along myelinated axons between adjacent Schwann cells", "Densely packed with voltage-gated sodium channels (\\(\\approx 10,000/\\\mu\\text{m}^2\\)), acting as the exclusive sites for action potential regeneration", "Pores that absorb cerebrospinal fluid, Sites where neurotransmitters are destroyed, Sealed regions impermeable to ions"),
            ("Saltatory Conduction", "The rapid, leaping propagation of the action potential from one Node of Ranvier to the next, jumping over the insulated internodal segments", "Increases nerve conduction velocity up to \\(100\\text{ to }120\\text{ meters/second}\\) (\\(\\approx 430\\text{ km/h}\\)) while saving massive metabolic ATP energy (fewer ions need to be pumped by \\(\\text{Na}^+/\\text{K}^+\\) ATPase)", "Slow continuous conduction creeping smoothly along every micrometer, Wave of contraction of muscle fibers, Transmission of sound vibrations"),
            ("Neurilemma and Peripheral Nerve Regeneration", "The outer nucleated cytoplasmic layer of Schwann cells enclosing the myelin sheath in the PNS", "Forms a continuous regeneration tube (Büngner band) guiding sprouted axon tips to re-innervate target organs after peripheral nerve transection; absent in CNS", "Prevents all nerve regeneration, Found only in the cerebrum, Dead layer of bone cells"),
            ("Continuous vs Saltatory Conduction velocity", "Unmyelinated axons conduct via continuous conduction (\\(0.5\\text{ to }2.0\\text{ m/s}\\)); Myelinated axons conduct via saltatory conduction (up to \\(120\\text{ m/s}\\))", "Myelination enables vertebrates to achieve hyper-fast reflex responses without needing giant-diameter axons like squid", "Unmyelinated axons conduct 100 times faster, Both conduct at identical speeds, Conduction velocity is independent of myelin"),
            ("White Matter vs Gray Matter in CNS", "White Matter consists predominantly of myelinated axons and oligodendrocytes (white appearance due to high lipid myelin); Gray Matter consists predominantly of neuronal cell bodies (somata), dendrites, unmyelinated axons, and synapses", "White matter coordinates long-distance signal routing; Gray matter performs local information processing and integration", "White matter contains no axons, Gray matter is dead tissue, White matter is found only in the skin"),
            ("Internode distance and fiber diameter scaling", "Larger axon diameter and longer internodal distances (up to \\(1.5\\text{ mm}\\)) increase electrical length constant (\\(\\lambda\\)) and accelerate saltatory conduction velocity", "Conduction velocity in myelinated mammalian fibers scales approximately as \\(V \\approx 6 \\times \\text{diameter in }\\mu\\text{m}\\)", "Wider axons conduct slower, Internodal distance has zero effect, Axons with zero nodes conduct fastest"),
            ("Myelin basic protein (MBP) and Proteolipid protein (PLP)", "Major structural transmembrane and peripheral proteins that stabilize and tightly compact the concentric spiral lamellae of the myelin sheath", "Target of autoimmune inflammatory attack in multiple sclerosis", "Enzymes that synthesize acetylcholine, Structural proteins of the spindle apparatus, Ion channels in nodes")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Myelination & Saltatory Conduction.**\n- Myelin Sheath: Multi-layered lipid insulator (reduces capacitance, increases resistance).\n- PNS: Schwann cells (1 cell = 1 internode; Neurilemma permits regeneration).\n- CNS: Oligodendrocytes (1 cell myelinates 30-50 axons; no neurilemma \\(\\rightarrow\\) no regeneration).\n- Nodes of Ranvier: Unmyelinated gaps rich in \\(\\text{Na}^+\\) channels \\(\\rightarrow\\) Saltatory conduction (action potential leaps node-to-node, up to \\(120\\text{ m/s}\\), saving ATP).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Electrophysiological Detail:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 3: Neuroglia (Astrocytes, Microglia, Ependymal, Schwann, Oligodendrocytes)
    arch3 = {
        'templates': [
            "What distinct histological and physiological support role characterizes: '{0}'?:",
            "In central and peripheral neuroglial histology: '{0}' is recognized by:",
            "Consider supporting glial cells: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A neuropathologist examines non-neuronal brain tissue: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' protect, insulate, or metabolically nurture neurons?:",
            "Evaluate the neuroglial cell type: '{0}':",
            "Why do neuroglial cells outnumber neurons in the central nervous system?:",
            "What cytological property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Neuroglia (Glial Cells) General Definition", "Non-excitable supporting cells of the nervous system that do not conduct action potentials, outnumbering neurons by \\(\\approx 5\\text{ to }10\\text{ to }1\\)", "Retain mitotic dividing capacity throughout adult life (giving rise to the vast majority of adult primary brain tumors - gliomas)", "Cells that transmit electrical action potentials to muscles, Dead mineralized bone cells, Red blood cells carrying oxygen in brain"),
            ("Astrocytes (Blood-Brain Barrier & Metabolic Support)", "Star-shaped glial cells with radiating foot processes (perivascular end-feet) that envelop cerebral capillaries and neuronal synapses", "Induces endothelial tight junctions forming the Blood-Brain Barrier (BBB), buffers extracellular \\(\\text{K}^+\\), recycles neurotransmitters (glutamate), and supplies lactate to active neurons", "Phagocytic cells derived from bone marrow, Myelin-forming cells in peripheral nerves, Ciliated cells lining brain ventricles"),
            ("Blood-Brain Barrier (BBB) Architecture", "Formed primarily by continuous brain capillary endothelial cells joined by impermeable tight junctions, resting on a basal lamina and surrounded by astrocyte end-feet", "Strictly shields delicate neural tissue from circulating systemic toxins, fluctuations in amino acids/ions, and peripheral pathogens", "Open fenestrated capillaries allowing free diffusion, Porous membrane letting all proteins enter brain, Formed by bone osteocytes"),
            ("Microglia (Resident Brain Macrophages)", "Small, thorny, dark-staining glial cells derived from embryonic mesoderm (yolk sac hematopoietic progenitors, unlike neuroectodermal glia)", "Act as the primary resident immune defense and phagocytes of the CNS; transform into amoeboid phagocytes upon brain injury or infection to clear debris", "Cells that synthesize myelin, Cells that secrete cerebrospinal fluid, Electrical conductor cells"),
            ("Ependymal Cells (Choroid Plexus & CSF)", "Simple cuboidal to low columnar ciliated epithelial-like cells lining the brain ventricles and the central canal of the spinal cord", "Modified ependymal cells associated with capillary tufts form the Choroid Plexus, which actively secretes Cerebrospinal Fluid (CSF)", "Myelinates peripheral nerve axons, Forms tough protective bone, Generates voluntary motor signals"),
            ("Satellite Cells in PNS Ganglia", "Small, flattened glial cells surrounding and cushioning the cell bodies (somata) of sensory and autonomic neurons in peripheral ganglia", "Provide physical support and regulate the biochemical microenvironment around ganglion cell bodies", "Myelinates long axons in spinal cord, Destroys bacteria like microglia, Transmits pain signals directly"),
            ("Radial Glia in Embryonic Brain Development", "Bipolar elongated glial cells spanning the developing cerebral cortex from ventricular zone to pial surface", "Serve as physical migratory scaffolding along which newborn embryonic neuroblasts travel to build the 6-layered cerebral cortex", "Cells that synthesize skull bone, Cells that produce cerebrospinal fluid in adults, Permanent post-mitotic neurons"),
            ("Gliosis / Glial Scar (Astrogliosis)", "Following CNS trauma or ischemic stroke, reactive astrocytes undergo hypertrophy and hyperplasia, forming an impermeable dense meshwork (glial scar)", "Walls off damaged necrotic brain regions, but physically and chemically (via chondroitin sulfate proteoglycans) prevents axon regeneration in the CNS", "Causes instant regeneration of severed brain tracts, Melts brain tissue into fluid, Reverses stroke damage completely"),
            ("Potassium Spatial Buffering by Astrocytes", "High neuronal firing releases excessive \\(\\text{K}^+\\) into narrow synaptic clefts; astrocytes take up surplus \\(\\text{K}^+\\) via Kir4.1 channels and dissipate it through gap junction networks", "Prevents dangerous extracellular potassium accumulation that would cause unprovoked epileptic neuronal depolarization", "Pumps potassium out into blood, Destroys potassium ions with acid, Converts potassium into sodium"),
            ("Gliomas (Astrocytoma, Glioblastoma)", "Malignant brain tumors originating from the uncontrolled mitotic proliferation of glial cells (most commonly astrocytes)", "Glioblastoma (grade IV astrocytoma) is the most aggressive primary brain tumor in adults, displaying high invasiveness along white matter tracts", "Tumors derived from dead skull bones, Benign infections caused by amoebae, Viral warts on the brain surface")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Neuroglial Diversity & Functions.**\n- Outnumber neurons 5-10:1; retain mitotic ability (source of gliomas).\n- Astrocytes: Star-shaped, perivascular end-feet induce Blood-Brain Barrier (BBB), \\(\\text{K}^+\\) spatial buffering, glutamate recycling, glial scar.\n- Microglia: Mesodermal origin (monocyte-macrophage lineage), resident CNS phagocytes/immune surveillance.\n- Ependymal: Ciliated lining of ventricles, Choroid plexus secretes CSF.\n- Oligodendrocytes (CNS myelin) & Schwann cells (PNS myelin).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Neurophysiological Detail:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Synapse Transmission: Chemical vs Electrical Synapse & Neurotransmitters
    arch4 = {
        'templates': [
            "What distinct molecular and electrophysiological mechanism defines: '{0}'?:",
            "In synaptic neurobiology and neurotransmission: '{0}' is characterized by:",
            "Consider synaptic architecture: '{0}' functions to:",
            "Which statement precisely describes the sequence of: '{0}'?:",
            "A neuropharmacologist investigates synaptic receptors: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' transmit, modulate, or terminate neural information flow?:",
            "Evaluate the synaptic event: '{0}':",
            "Why is '{0}' unidirectional in chemical synapses?:",
            "What biophysical property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Chemical Synapse Architecture", "Presynaptic terminal, Synaptic Cleft (\\(20\\text{--}40\\text{ nm}\\) fluid gap), and Postsynaptic membrane studded with specific neuroreceptors", "Action potential in presynaptic neuron triggers calcium-dependent exocytosis of neurotransmitters, diffusing across the cleft to bind postsynaptic receptors", "Direct cytoplasmic continuity via gap junctions, Solid physical bone connection, Open hole through which whole cells migrate"),
            ("Unidirectional transmission in Chemical Synapses", "Information flows strictly unidirectionally from presynaptic terminal to postsynaptic membrane", "Because neurotransmitter vesicles are localized exclusively in the presynaptic terminal, and specific receptor proteins are situated on the postsynaptic membrane", "Current flows bidirectionally with equal speed, Information jumps randomly backwards, Voltage travels backwards into axon"),
            ("Electrical Synapse (Gap Junction synapse)", "Presynaptic and postsynaptic membranes are separated by a tiny gap (\\(\\approx 3.5\\text{ nm}\\)) and connected directly by hexameric connexon channels", "Permits instantaneous, bidirectional ionic current flow with zero synaptic delay (\\(< 0.1\\text{ ms}\\)); found in cardiac intercalated discs and escape reflex circuits", "Wide gap requiring chemical neurotransmitter diffusion, Synaptic delay of 5 milliseconds, Unidirectional transmission only"),
            ("Synaptic Delay (\\(0.5\\text{ to }1.0\\text{ ms}\\))", "The brief time delay in chemical synapses required for \\(\\text{Ca}^{2+}\\) channel opening, vesicle fusion, neurotransmitter diffusion across the cleft, and postsynaptic receptor activation", "The primary bottleneck slowing reflex arc transmission speed", "Delay of 10 seconds, Time needed for axon to grow new branches, Period when nerve completely dies"),
            ("Voltage-gated Calcium Channels in Presynaptic Bouton", "Arrival of the action potential depolarizes the presynaptic terminal, opening voltage-gated \\(\\text{Ca}^{2+}\\) channels (Cav2.1/2.2)", "Influx of \\(\\text{Ca}^{2+}\\) activates synaptotagmin, triggering SNARE-mediated fusion of synaptic vesicles with the presynaptic active zone", "Pumps calcium out into the synaptic cleft, Releases potassium to stop transmission, Degrades neurotransmitters"),
            ("Excitatory Postsynaptic Potential (EPSP) vs Inhibitory Postsynaptic Potential (IPSP)", "EPSP: depolarizing graded potential caused by net influx of positive ions (\\(\\text{Na}^+, \\text{Ca}^{2+}\\)) bringing membrane closer to threshold; IPSP: hyperpolarizing graded potential caused by influx of \\(\\text{Cl}^-\\) or efflux of \\(\\text{K}^+\\) moving membrane away from threshold", "EPSPs and IPSPs undergo spatial and temporal summation at the axon hillock to determine whether an action potential fires", "EPSP hyperpolarizes while IPSP depolarizes, Both always trigger an immediate all-or-none spike, Both are identical action potentials"),
            ("Major Neurotransmitters: Acetylcholine, Glutamate, GABA, Glycine", "Acetylcholine (ACh): primary excitatory neuromuscular transmitter; Glutamate: primary excitatory neurotransmitter of the CNS; GABA (gamma-aminobutyric acid): primary inhibitory neurotransmitter of the brain; Glycine: primary inhibitory neurotransmitter of the spinal cord", "Balance between excitatory glutamate and inhibitory GABA regulates cortical neural circuits; imbalance causes epilepsy", "Glutamate is the main inhibitory transmitter, GABA is the main muscle contractor, All transmitters are identical peptides"),
            ("Ionotropic vs Metabotropic Receptors", "Ionotropic receptors: ligand-gated ion channels that open directly upon neurotransmitter binding for fast, millisecond responses (e.g., Nicotinic AChR, AMPA, NMDA, \\(\\text{GABA}_A\\)); Metabotropic receptors: G-protein coupled receptors (GPCRs) that activate second-messenger cascades (cAMP, \\(\\text{IP}_3\\)/DAG) for slow, modulatory responses (e.g., Muscarinic AChR, \\(\\text{GABA}_B\\))", "Allows both ultra-fast transmission and long-term neuromodulatory synaptic plasticity (e.g., learning and memory)", "Ionotropic receptors activate second messengers, Metabotropic receptors are open pores without proteins, Both act within 1 microsecond"),
            ("Termination of Synaptic Action: Degradation vs Reuptake", "Enzymatic degradation: enzymes break down transmitters in the cleft (e.g., Acetylcholinesterase hydrolyzes ACh); Reuptake: specialized presynaptic transporters take intact transmitters back into the terminal or astrocytes (e.g., Serotonin transporter SERT, Dopamine transporter DAT)", "Essential to clear the cleft within milliseconds, allowing high-frequency discrete signal transmission", "Transmitters evaporate into the air, Transmitters are permanently bound to receptors, Transmitters freeze inside cleft"),
            ("Selective Serotonin Reuptake Inhibitors (SSRIs - Fluoxetine / Prozac)", "Antidepressant drugs that selectively block the serotonin transporter (SERT) on presynaptic terminals", "Prolongs the active residency time of serotonin in the synaptic cleft, enhancing serotonergic neurotransmission to treat major depressive disorder and anxiety", "Destroys serotonin receptors, Blocks acetylcholine degradation, Stimulates rapid GABA release")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Synaptic Transmission.**\n- Chemical Synapse: Unidirectional, \\(20\\text{--}40\\text{ nm}\\) cleft, synaptic delay (\\(0.5\\text{--}1.0\\text{ ms}\\)). Action potential \\(\\rightarrow\\) \\(\\text{Ca}^{2+}\\) influx \\(\\rightarrow\\) vesicle exocytosis \\(\\rightarrow\\) binds postsynaptic receptors.\n- Electrical Synapse: Gap junctions (connexons), bidirectional, zero delay (\\(< 0.1\\text{ ms}\\)).\n- Graded Potentials: EPSP (depolarizing, \\(\\text{Na}^+\\) influx) vs IPSP (hyperpolarizing, \\(\\text{Cl}^-\\) influx / \\(\\text{K}^+\\) efflux); summed at axon hillock.\n- Transmitters: Glutamate (main CNS excitatory), GABA (main brain inhibitory), Glycine (spinal inhibitory), ACh (neuromuscular).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Neurochemical Detail:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 5: Structural Classification of Neurons (Unipolar, Bipolar, Multipolar, Pseudounipolar)
    arch5 = {
        'templates': [
            "Which anatomical morphology, pole count, and representative location characterizes: '{0}'?:",
            "In structural neuron classification: '{0}' is recognized by:",
            "Consider morphological neuronal diversity: '{0}' exhibits:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A neurohistologist examines sensory and motor pathways: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' adapt structural polarity to its specific sensory or motor role?:",
            "Evaluate the neuronal structural type: '{0}':",
            "Why is '{0}' found in this specific anatomical location?:",
            "What morphological property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Multipolar Neurons", "One long axon and two or more (often hundreds) of branching dendrites arising directly from the cyton", "Most common structural neuron type in the mammalian nervous system; includes all somatic motor neurons and interneurons of the brain and spinal cord (e.g., cerebral pyramidal cells, cerebellar Purkinje cells)", "Single process that divides into two, One axon and one dendrite only, Lacks an axon completely"),
            ("Bipolar Neurons", "Possesses exactly two processes arising from opposite poles of the spindle-shaped cell body: one dendrite and one axon", "Specialized sensory neurons dedicated to special senses: retina of the eye, olfactory epithelium of nasal cavity, and spiral/vestibular ganglia of the inner ear", "Has 50 dendrites on one side, Most common neuron in spinal cord, Found in voluntary skeletal muscles"),
            ("Pseudounipolar (Unipolar in adults) Neurons", "Originates embryonically as bipolar, but processes fuse near the cyton into a single stalk that bifurcates into a peripheral process (functioning as dendrite) and a central process (entering CNS)", "Found characteristically in Dorsal Root Ganglia (DRG) of spinal nerves and sensory ganglia of cranial nerves (V, VII, IX, X); transmits touch, pain, and temperature sensations", "Multipolar neurons with 10 axons, Interneurons of the cerebral cortex, Motor neurons innervating muscles"),
            ("True Unipolar Neurons", "Possesses a single process arising from the cell body that acts as an axon, lacking true dendrites", "Found predominantly during embryonic stages of vertebrates and common in invertebrate nervous systems", "Found in adult human retina, Most abundant neuron in adult brain, Contains 100 branching dendrites"),
            ("Anaxonic Neurons", "Small neurons lacking a distinguishable axon; dendrites and axons cannot be distinguished morphologically", "Do not produce action potentials; convey graded local potentials in the brain, retina (amacrine cells), and adrenal medulla", "Giant motor neurons innervating leg muscles, Neurons with a 1-meter long axon, Dead cells lacking nuclei"),
            ("Pyramidal Cells of Cerebral Cortex", "Distinctive triangular, pyramid-shaped cell body with a prominent apical dendrite ascending towards the pial surface and multiple basal dendrites", "Primary excitatory (glutamatergic) projection neurons of the cerebral cortex; includes giant Betz cells in primary motor cortex (layer V)", "Inhibitory interneurons of spinal cord, Sensory cells in the retina, Small round cells in cerebellum"),
            ("Purkinje Cells of Cerebellar Cortex", "Massive, flask-shaped cell body boasting the most elaborate, fan-like, planar dendritic arborization in the entire nervous system (receives \\(\\approx 200,000\\) synaptic inputs)", "Sole output neurons of the cerebellar cortex, releasing inhibitory GABA to coordinate fine motor timing, balance, and motor learning", "Excitatory motor neurons in muscle, Sensory bipolar cells in nose, Glial cells producing myelin"),
            ("Sensory (Afferent) vs Motor (Efferent) Neurons", "Sensory (Afferent): conducts impulses centripetally from peripheral sensory receptors toward the CNS; Motor (Efferent): conducts impulses centrifugally from the CNS outward to effector organs (muscles, glands)", "Interneurons (association neurons) bridge sensory and motor pathways within the gray matter of the CNS", "Sensory conducts away from brain, Motor conducts towards brain, Both conduct identical signals in reverse"),
            ("Reflex Arc Pathway Sequence", "Sensory Receptor \\(\\rightarrow\\) Sensory (Afferent) Neuron \\(\\rightarrow\\) Integrating Center (Interneuron in spinal cord) \\(\\rightarrow\\) Motor (Efferent) Neuron \\(\\rightarrow\\) Effector Organ (Muscle / Gland)", "Basic functional neuroanatomical circuitry underlying automatic, involuntary reflex responses (e.g., knee-jerk patellar reflex)", "Effector \\(\\rightarrow\\) Motor \\(\\rightarrow\\) Brain \\(\\rightarrow\\) Sensory, Interneuron \\(\\rightarrow\\) Receptor \\(\\rightarrow\\) Effector, Receptor \\(\\rightarrow\\) Brain \\(\\rightarrow\\) Bone"),
            ("Dorsal Root vs Ventral Root of Spinal Cord", "Dorsal root: strictly sensory (carries afferent fibers into the dorsal horn; contains dorsal root ganglion); Ventral root: strictly motor (carries efferent motor axons out from anterior horn motor neurons)", "Bell-Magendie law: established that dorsal roots are sensory and ventral roots are motor", "Dorsal root is motor while ventral is sensory, Both roots carry identical mixed signals, Dorsal root contains muscle fibers")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Structural & Functional Neuron Classification.**\n- Multipolar: 1 axon + multiple dendrites (most common; motor neurons, pyramidal, Purkinje cells).\n- Bipolar: 1 axon + 1 dendrite at opposite poles (special senses: retina, olfactory, inner ear).\n- Pseudounipolar: Single process bifurcates into peripheral & central branches (sensory: dorsal root ganglia / DRG).\n- Reflex Arc: Receptor \\(\\rightarrow\\) Afferent (Sensory) \\(\\rightarrow\\) Interneuron \\(\\rightarrow\\) Efferent (Motor) \\(\\rightarrow\\) Effector.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Morphological / Diagnostic Detail:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 6: Quantitative Neurophysiology: Resting Potential, Nernst, Action Potential
    arch6 = {
        'templates': [
            "{0}:",
            "Calculate the electrophysiological or biophysical parameter: {0}:",
            "A quantitative neurophysiology problem: {0}:",
            "Solve the quantitative action potential calculation: {0}:",
            "Compute the following membrane potential metric: {0}:",
            "Analyze the numerical Nernst and Goldman equation problem: {0}:",
            "Determine the correct calculated electrophysiological value: {0}:",
            "An analytical neurophysics problem: {0}:",
            "Find the accurate quantity for: {0}:",
            "Quantitative neurobiology evaluation: {0}:"
        ],
        'data': [
            ("Calculate the equilibrium potential for potassium (\\(E_K\\)) at body temperature (\\(37^\\circ\\text{C} = 310\\text{ K}\\)) using the Nernst equation (\\(E = \\frac{61.5}{z} \\log_{10} \\frac{[\\text{K}^+]_{out}}{[\\text{K}^+]_{in}}\\)), given \\([\\text{K}^+]_{out} = 4.5\\text{ mM}\\) and \\([\\text{K}^+]_{in} = 150\\text{ mM}\\)", "\\(-93.7\\text{ mV}\\)", "\\(E_K = 61.5 \\times \\log_{10}(4.5 / 150) = 61.5 \\times \\log_{10}(0.03) = 61.5 \\times (-1.5229) \\approx -93.66\\text{ mV} \\approx -93.7\\text{ mV}\\)", "-70.0 mV, +61.5 mV, -140.0 mV"),
            ("Calculate the equilibrium potential for sodium (\\(E_{Na}\\)) at \\(37^\\circ\\text{C}\\) given \\([\\text{Na}^+]_{out} = 145\\text{ mM}\\) and \\([\\text{Na}^+]_{in} = 15\\text{ mM}\\)", "\\(+60.6\\text{ mV}\\)", "\\(E_{Na} = 61.5 \\times \\log_{10}(145 / 15) = 61.5 \\times \\log_{10}(9.667) = 61.5 \\times 0.9853 \\approx +60.6\\text{ mV}\\)", "-60.6 mV, +120.0 mV, 0.0 mV"),
            ("A myelinated motor axon conducts action potentials via saltatory conduction at \\(100\\text{ meters/second}\\). How long does it take an impulse to travel \\(1.2\\text{ meters}\\) from the lumbar spinal cord to a muscle in the foot?", "\\(12\\text{ milliseconds}\\) (\\(0.012\\text{ seconds}\\))", "\\(\\text{Time} = \\text{Distance} / \\text{Velocity} = 1.2\\text{ m} / 100\\text{ m/s} = 0.012\\text{ s} = 12\\text{ ms}\\)", "1.2 ms, 120 ms, 0.12 ms"),
            ("An unmyelinated C-type pain fiber conducts impulses at \\(1.0\\text{ meter/second}\\). How long does it take a dull pain impulse to travel \\(1.2\\text{ meters}\\) from the foot to the spinal cord?", "\\(1.2\\text{ seconds}\\) (100 times slower than myelinated)", "\\(\\text{Time} = 1.2\\text{ m} / 1.0\\text{ m/s} = 1.2\\text{ seconds}\\)", "0.12 s, 12 s, 0.012 s"),
            ("If a neuron fires action potentials at its maximal absolute refractory limit where each action potential plus refractory period lasts \\(2.0\\text{ milliseconds}\\), what is the maximum theoretical firing frequency of this neuron in Hertz (action potentials per second)?", "\\(500\\text{ Hz}\\) (500 spikes/sec)", "\\(\\text{Frequency} = 1 / \\text{Period} = 1 / (2.0 \\times 10^{-3}\\text{ s}) = 500\\text{ Hz}\\)", "250 Hz, 1,000 Hz, 100 Hz"),
            ("At a single Node of Ranvier, \\(1.0 \\times 10^6\\) sodium ions (\\(\\text{Na}^+\\)) enter during an action potential spike. Given the elementary charge \\(e = 1.6 \\times 10^{-19}\\text{ Coulombs}\\), what is the total electrical charge transferred across this node?", "\\(1.6 \\times 10^{-13}\\text{ Coulombs}\\) (\\(0.16\\text{ pC}\\))", "\\(Q = N \\times e = (1.0 \\times 10^6) \\times (1.6 \\times 10^{-19}\\text{ C}) = 1.6 \\times 10^{-13}\\text{ C}\\)", "\\(1.6 \\times 10^{-16}\\text{ C}\\), \\(3.2 \\times 10^{-13}\\text{ C}\\), \\(1.6 \\times 10^{-10}\\text{ C}\\)"),
            ("The \\(\\text{Na}^+/\\text{K}^+\\) ATPase pump moves \\(3\\text{ Na}^+\\) ions out of the cell for every \\(2\\text{ K}^+\\) ions pumped in per ATP molecule hydrolyzed. If a neuron hydrolyzes \\(1.0 \\times 10^7\\text{ ATP molecules}\\), how many net positive charges are pumped out of the cell?", "\\(1.0 \\times 10^7\\text{ net positive charges}\\)", "Net charge per pump cycle \\(= 3 - 2 = +1\\). Total net positive charges \\(= 1.0 \\times 10^7 \\times 1 = 1.0 \\times 10^7\\) (electrogenic pumping)", "\\(2.0 \\times 10^7\\), \\(3.0 \\times 10^7\\), \\(5.0 \\times 10^7\\)"),
            ("A typical chemical synaptic cleft has width \\(x = 20\\text{ nm}\\) (\\(2.0 \\times 10^{-8}\\text{ m}\\)). If the diffusion coefficient of acetylcholine in water is \\(D = 4.0 \\times 10^{-6}\\text{ cm}^2/\\text{s} = 4.0 \\times 10^{-10}\\text{ m}^2/\\text{s}\\), calculate the Einstein diffusion time (\\(t \\approx x^2 / 2D\\)) for ACh to cross the cleft", "\\(0.5\\text{ microseconds}\\) (\\(5.0 \\times 10^{-7}\\text{ s}\\))", "\\(t = (2.0 \\times 10^{-8})^2 / (2 \\times 4.0 \\times 10^{-10}) = (4.0 \\times 10^{-16}) / (8.0 \\times 10^{-10}) = 5.0 \\times 10^{-7}\\text{ s} = 0.5\\text{ }\\mu\\text{s}\\)", "5.0 ms, 50 μs, 0.05 ms"),
            ("A resting neuron has membrane resistance \\(R_m = 100\\text{ M}\\Omega\\) (\\(10^8\\text{ }\\Omega\\)). If an excitatory synaptic current injects \\(I = 0.2\\text{ nA}\\) (\\(2.0 \\times 10^{-10}\\text{ A}\\)), what is the amplitude of the resulting EPSP depolarization (\\(\\Delta V = I \\times R_m\\))?", "\\(+20\\text{ mV}\\)", "\\(\\Delta V = (2.0 \\times 10^{-10}\\text{ A}) \\times (10^8\\text{ }\\Omega) = 0.02\\text{ V} = +20\\text{ mV}\\)", "+2 mV, +50 mV, +200 mV"),
            ("If a neuron resting membrane potential is \\(-70\\text{ mV}\\) and its action potential threshold is \\(-55\\text{ mV}\\), what is the minimum EPSP depolarization required at the axon hillock to trigger an action potential?", "\\(+15\\text{ mV}\\)", "\\(\\Delta V = \\text{Threshold} - \\text{RMP} = -55\\text{ mV} - (-70\\text{ mV}) = +15\\text{ mV}\\)", "+55 mV, +70 mV, -15 mV")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Identify given electrophysiological variables.**\n" + item[0] + "\n\n**Step 2: Apply the governing biophysical equation (Nernst, Ohm's law, cable physics).**\n" + item[2] + ".\n\n**Step 3: Conclude.**\nResult is " + item[1] + "."
        ),
        'diff': 'hard'
    }

    # Arch 7: Neurological Pathology, Demyelinating Diseases & Neurotoxins
    arch7 = {
        'templates': [
            "Which neurological disease, neurotoxin, or clinical disorder relates to: '{0}'?:",
            "In neuropathology and clinical neurology: '{0}' is characterized by:",
            "What clinical insight or diagnostic finding defines: '{0}'?:",
            "How does neurotoxin action or autoimmune attack disrupt: '{0}'?:",
            "A neurologist evaluates a patient with neurological symptoms: '{0}'. What is true?:",
            "Which disease mechanism explains: '{0}'?:",
            "What is the medical significance of: '{0}'?:",
            "Why is '{0}' a diagnostic cornerstone in clinical neurobiology?:",
            "What pathological consequence results from: '{0}'?:",
            "Evaluate the neuropathological concept: '{0}':"
        ],
        'data': [
            ("Multiple Sclerosis (MS)", "Chronic autoimmune demyelinating disease of the Central Nervous System where autoreactive T-cells attack myelin basic protein and oligodendrocytes", "Produces demyelinated sclerotic plaques in brain and optic nerve; causes saltatory conduction failure, optic neuritis, paresthesias, spasticity, and Lhermitte's sign", "Demyelination of peripheral nerves only, Bacterial infection of brain ventricles, Excessive growth of bone inside skull"),
            ("Guillain-Barré Syndrome (GBS)", "Acute post-infectious autoimmune demyelinating polyneuropathy of the Peripheral Nervous System, frequently triggered by Campylobacter jejuni infection", "Molecular mimicry leads to autoantibody attack on Schwann cells and peripheral myelin, causing symmetrical ascending flaccid paralysis (ground to brain) and loss of deep tendon reflexes", "Chronic brain dementia, Degeneration of muscle actin fibers, Spastic lockjaw"),
            ("Tetrodotoxin (TTX / Pufferfish poison)", "Pufferfish neurotoxin that selectively and irreversibly blocks voltage-gated sodium channels (Nav) on the extracellular face of excitable membranes", "Prevents action potential generation and conduction in somatic nerves, causing rapid numbness, respiratory muscle paralysis, and death from asphyxiation", "Blocks potassium channels causing heart attack, Blocks acetylcholine receptors, Destroys myelin sheath"),
            ("Saxitoxin (STX / Red Tide Algae)", "Paralytic shellfish toxin produced by marine dinoflagellates (Alexandrium); acts identically to TTX by potently occluding the pore of voltage-gated \\(\\text{Na}^+\\) channels", "Accumulates in filter-feeding shellfish; consumption causes numbness, ataxia, and fatal respiratory paralysis", "Causes uncontrollable muscle spasms, Dissolves bone mineral matrix, Destroys red blood cells"),
            ("Parkinson's Disease (Substantia Nigra degeneration)", "Progressive neurodegenerative disorder characterized by loss of dopaminergic neurons in the substantia nigra pars compacta and accumulation of alpha-synuclein Lewy bodies", "Causes profound dopamine depletion in the striatum, leading to resting tremor ('pill-rolling'), cogwheel rigidity, bradykinesia (slowness of movement), and festinating gait", "Autoimmune destruction of myelin in spinal cord, Infection of motor neurons by poliovirus, Hyperactivity of acetylcholine receptors"),
            ("Alzheimer's Disease (Amyloid plaques & Tau tangles)", "Most common cause of dementia; characterized by extracellular senile plaques of amyloid-beta (A\\(\\beta_{42}\\)) and intracellular neurofibrillary tangles of hyperphosphorylated tau protein", "Causes widespread loss of cortical cholinergic neurons and progressive cognitive decline, starting with severe episodic anterograde amnesia", "Autoimmune destruction of Schwann cells, Prion disease of the cerebellum, Vascular clot in retina"),
            ("Rabies Virus Retrograde Axonal Transport", "Neurotropic rhabdovirus enters peripheral nerve endings at bite wounds (via nicotinic acetylcholine receptors) and travels retrogradely via dynein motors to the CNS", "Ascends along spinal cord to the brain, causing fatal viral encephalitis, hydrophobia, violent agitation, and Negri body inclusions in hippocampal neurons", "Transmitted through air into lungs, Kills skin cells causing rash, Destroys liver hepatocytes"),
            ("Local Anesthetics (Lidocaine / Bupivacaine / Novocaine)", "Lipophilic tertiary amines that cross the axonal membrane, become protonated, and block voltage-gated \\(\\text{Na}^+\\) channels from the intracellular side", "Reversibly arrests action potential generation and conduction in small unmyelinated pain fibers (C-fibers) and sensory A-delta fibers, producing local anesthesia", "Inhibits neurotransmitter synthesis in nucleus, Destroys myelin permanently, Stimulates continuous muscle contraction"),
            ("Amyotrophic Lateral Sclerosis (ALS / Lou Gehrig's disease)", "Progressive, fatal neurodegenerative disease targeting both Upper Motor Neurons (corticospinal tract) and Lower Motor Neurons (anterior horn cells of spinal cord)", "Causes progressive skeletal muscle atrophy, fasciculations, spasticity, and eventual fatal respiratory failure, while sensory and cognitive functions typically remain intact", "Loss of sensory neurons only, Autoimmune attack on synovial joints, Viral infection of brain ventricles"),
            ("Wallerian Degeneration and Axonal Sprouting", "When a peripheral nerve is severed, the distal axon segment and its myelin undergo fragmentation and macrophage phagocytosis (Wallerian degeneration)", "Schwann cells proliferate to form a regeneration tube (bands of Büngner); the proximal axon stump sprouts growth cones guided by neurotrophins (NGF) at \\(\\approx 1\\text{ to }2\\text{ mm/day}\\)", "The entire neuron instantly dies and disappears, Severed axons re-fuse within 10 minutes, Proximal neuron divides into two cells")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Neuropathology, Neurotoxins & Clinical Conditions.**\n- Demyelinating: Multiple Sclerosis (CNS / Oligodendrocytes / autoimmune plaques); Guillain-Barré (PNS / Schwann cells / ascending paralysis).\n- Channel Toxins: Tetrodotoxin & Saxitoxin (block voltage-gated \\(\\text{Na}^+\\) channels \\(\\rightarrow\\) respiratory paralysis); Lidocaine (local anesthetic \\(\\text{Na}^+\\) blocker).\n- Neurodegenerative: Parkinson's (dopaminergic loss in substantia nigra, Lewy bodies); Alzheimer's (amyloid-\\(\\beta\\) plaques, tau tangles); ALS (upper & lower motor neuron loss).\n- Pathogen: Rabies (retrograde axonal dynein transport to brain).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Clinical / Pathophysiological Detail:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }


    # Arch 8: Neuroplasticity, Reflexes, Autonomic vs Somatic & Clinical Diagnostics
    arch8 = {
        'templates': [
            "Which physiological mechanism, reflex pathway, or neuroanatomical circuit characterizes: '{0}'?:",
            "In systems neurobiology and clinical neurology: '{0}' is recognized by:",
            "Consider neural integration and autonomic regulation: '{0}' functions to:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A neurologist examines sensory-motor integration: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' coordinate involuntary homeostasis or automated reflex responses?:",
            "Evaluate the neurofunctional circuit: '{0}':",
            "Why is '{0}' vital for neural homeostasis and clinical neurological examination?:",
            "What neurophysiological property corresponds to: '{0}'?:"
        ],
        'data': [
            ("Monosynaptic Reflex (e.g., Knee-jerk Patellar Reflex)", "Direct single synapse between sensory afferent neuron (muscle spindle Ia fiber) and motor efferent neuron in spinal cord gray matter, with zero intervening interneurons", "Most rapid reflex arc in the human body (latency \(\approx 20\text{ ms}\)); tested clinically to verify L2-L4 spinal nerve root integrity", "Complex polysynaptic reflex involving cerebral cortex, Reflex requiring 5 minutes to execute, Involuntary smooth muscle reflex"),
            ("Polysynaptic Withdrawal (Flexor) Reflex", "Noxious stimulus (e.g., stepping on a sharp nail) activates nociceptive pain fibers that synapse on multiple excitatory and inhibitory spinal interneurons", "Triggers ipsilateral flexor contraction (pulling foot away) and simultaneous contralateral extensor contraction (crossed-extensor reflex) to maintain standing balance", "Single synapse reflex without interneurons, Voluntary conscious decision in motor cortex, Reflex that pushes foot harder onto the nail"),
            ("Sympathetic vs Parasympathetic Autonomic Nervous System", "Sympathetic (Thoracolumbar outflow): 'Fight-or-Flight' response (dilates pupils, accelerates heart rate, bronchodilation, inhibits digestion; neurotransmitters: ACh at ganglion, Norepinephrine at target); Parasympathetic (Craniosacral outflow): 'Rest-and-Digest' response (constricts pupils, slows heart rate, stimulates digestion and peristalsis; neurotransmitters: ACh at both synapses)", "Dual antagonistic innervation fine-tunes involuntary visceral organ homeostasis", "Sympathetic slows heart rate while parasympathetic accelerates, Both use adrenaline as only transmitter, Sympathetic controls voluntary skeletal muscles"),
            ("Long-Term Potentiation (LTP / Hebbian Plasticity)", "Persistent strengthening of synapses based on recent patterns of high-frequency activity (tetanic stimulation), mediated by NMDA receptor activation and \(\text{Ca}^{2+}\)-dependent AMPA receptor insertion", "Primary cellular and molecular mechanism underlying synaptic plasticity, learning, and long-term memory formation in the hippocampus", "Permanent destruction of synapses in Alzheimer's, Inability of nerves to fire action potentials, Rapid death of neurons after stimulation"),
            ("Electroencephalogram (EEG) Brain Waves", "Records synchronized postsynaptic potentials of millions of cortical pyramidal neurons using scalp surface electrodes", "Displays characteristic frequency bands: Alpha (\(8\text{--}13\text{ Hz}\), relaxed awake with eyes closed), Beta (\(14\text{--}30\text{ Hz}\), active alert mental focus), Theta (\(4\text{--}7\text{ Hz}\), light sleep), and Delta (\(< 4\text{ Hz}\), deep slow-wave sleep)", "Measures single action potentials in a single axon, Records muscular twitches in scalp, Measures blood sugar in brain"),
            ("Lumbar Puncture (Spinal Tap) and CSF Sampling", "Inserting a spinal needle between L3/L4 or L4/L5 vertebrae into the subarachnoid space (below the conus medullaris where spinal cord ends at L1/L2)", "Safely samples Cerebrospinal Fluid (CSF) without risk of spinal cord puncture, diagnosing meningitis, subarachnoid hemorrhage, and multiple sclerosis (oligoclonal bands)", "Injects antibiotics directly into the heart, Takes a bone marrow biopsy from skull, Removes brain tumors without surgery"),
            ("Cerebrospinal Fluid (CSF) circulation pathway", "Formed by Choroid Plexus in lateral ventricles \(\rightarrow\) Foramen of Monro \(\rightarrow\) 3rd ventricle \(\rightarrow\) Cerebral aqueduct of Sylvius \(\rightarrow\) 4th ventricle \(\rightarrow\) Foramina of Luschka/Magendie \(\rightarrow\) Subarachnoid space \(\rightarrow\) Arachnoid granulations into dural venous sinuses", "Cushions brain against trauma (buoyancy reduces effective 1400g brain weight to 50g), maintains intracranial pressure, and removes metabolic wastes", "Circulates through blood vessels like red blood cells, Fluid that fills the stomach, Produced by bone osteocytes"),
            ("Hydrocephalus (Water on the brain)", "Abnormal accumulation of CSF within brain ventricles due to impaired drainage (e.g., aqueductal stenosis) or defective arachnoid granulation reabsorption", "Increases intracranial pressure; in infants before cranial suture fusion, causes dramatic enlargement of head circumference and fontanelle bulging", "Drying of the brain due to lack of water, Shrinking of the skull into small size, Viral infection of ear"),
            ("Babinski Sign (Plantar Reflex)", "Stroking the lateral sole of the foot: normal adult response is downward plantar flexion of all toes; Babinski sign is upward dorsiflexion of the big toe and fanning of other toes", "Normal in infants under 1 year (unmyelinated corticospinal tract); in adults, indicates Upper Motor Neuron (UMN) lesion in corticospinal tract (stroke, MS, trauma)", "Diagnostic sign of broken ankle, Sign of vitamin deficiency, Indicates bone fracture"),
            ("Action Potential refractory periods (Absolute vs Relative)", "Absolute refractory period: voltage-gated \(\text{Na}^+\) channels are inactivated; NO stimulus, however strong, can trigger another action potential; Relative refractory period: \(\text{Na}^+\) channels reset but \(\text{K}^+\) channels remain open (hyperpolarization); an action potential can fire only with a stronger-than-normal suprathreshold stimulus", "Ensures unidirectional forward propagation of action potentials along axons and sets the upper limit on neural firing frequency", "Allows action potentials to collide and reverse, Keeps nerve permanently contracted, Causes complete paralysis")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Systems Neurobiology & Clinical Diagnostics.**\n- Reflexes: Monosynaptic (patellar knee-jerk, no interneuron, 20ms) vs Polysynaptic (withdrawal/crossed-extensor, interneurons).\n- Autonomic: Sympathetic (fight-or-flight, NE at target) vs Parasympathetic (rest-and-digest, ACh at target).\n- Neuroplasticity: LTP (NMDA receptor, \(\text{Ca}^{2+}\) influx, learning/memory).\n- Diagnostics: EEG waves (\(\alpha, \beta, \theta, \delta\)); Lumbar puncture at L3/L4 (samples CSF from subarachnoid space); Babinski sign (UMN lesion).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Clinical / Physiological Detail:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-3-3.3.4", "Nervous tissue: Neuron structure (cyton, dendrites, axon, synapse)", archs)


if __name__ == "__main__":
    q1 = gen_3_3_1()
    q2 = gen_3_3_2()
    q3 = gen_3_3_3()
    q4 = gen_3_3_4()
    print(f"gen_3_3_1: {len(q1)} questions")
    print(f"gen_3_3_2: {len(q2)} questions")
    print(f"gen_3_3_3: {len(q3)} questions")
    print(f"gen_3_3_4: {len(q4)} questions")
    print(f"Total Part 3 questions: {len(q1) + len(q2) + len(q3) + len(q4)}")
