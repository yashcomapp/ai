import re

with open('scripts/build_cbse9_scie_ch3_part3.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect where gen_3_3_1 ends:
# Line 232: archs = [arch1, arch2, arch3, arch4, arch1, arch2, arch3, arch4]
# We will define arch5, arch6, arch7, arch8 for gen_3_3_1!

archs_3_3_1_new = """
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
            "**Step 1: Understand Glandular Epithelial Classification & Secretory Modes.**\\n- Exocrine (ducts) vs Endocrine (ductless \\(\\rightarrow\\) bloodstream).\\n- Secretory mechanisms: Merocrine/Eccrine (exocytosis, no cell loss: salivary, pancreas); Apocrine (apical pinch-off: mammary lipid); Holocrine (entire cell disintegrates: sebaceous).\\n- Acini types: Serous (watery enzymes, round central nuclei) vs Mucous (viscous mucin, flat basal nuclei).\\n\\n**Step 2: Evaluate '" + item[0] + "'.**\\n" + item[1] + ".\\n\\n**Step 3: Functional / Clinical Detail:**\\n" + item[2] + "."
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
            ("A cylindrical intestinal enterocyte has apical diameter \\(10\\text{ }\mu\\text{m}\\) (flat area \\(\\approx 78.5\\text{ }\mu\\text{m}^2\\)). Its apical membrane bears \\(2,000\\) microvilli, each \\(1.0\\text{ }\mu\\text{m}\\) long and \\(0.1\\text{ }\mu\\text{m}\\) in diameter. By what factor do microvilli expand the apical absorptive surface area of this enterocyte?", "\\(\\approx 9.0\\text{-fold expansion}\\)", "Area per microvillus \\(= \\pi d h = 3.1416 \\times 0.1 \\times 1.0 \\approx 0.314\\text{ }\mu\\text{m}^2\\). Total microvilli area \\(= 2,000 \\times 0.314 \\approx 628.3\\text{ }\mu\\text{m}^2\\). Total apical area \\(= 78.5 + 628.3 = 706.8\\text{ }\mu\\text{m}^2\\). Factor \\(= 706.8 / 78.5 \\approx 9.0\\)", "\\(\\approx 2.0\\text{-fold}\\), \\(\\approx 50\\text{-fold}\\), \\(\\approx 200\\text{-fold}\\)"),
            ("The human small intestine has an anatomical tube surface area of \\(\\approx 0.5\\text{ m}^2\\). Plicae circulares increase area 3-fold; villi increase it 10-fold; microvilli increase it 20-fold. What is the total effective absorptive surface area of the human small intestine?", "\\(\\approx 300\\text{ m}^2\\) (roughly the area of a tennis court)", "\\(\\text{Total Area} = 0.5\\text{ m}^2 \\times 3 \\times 10 \\times 20 = 300\\text{ m}^2\\)", "\\(30\\text{ m}^2\\), \\(3,000\\text{ m}^2\\), \\(3.0\\text{ m}^2\\)"),
            ("Human skin sheds approximately \\(30,000\\text{ to }40,000\\) dead cornified keratinocytes per minute. Approximately how many dead skin scales are shed from a human body in 24 hours?", "\\(\\approx 5.04 \\times 10^7\\text{ cells per day}\\) (\\(\\approx 50\\text{ million}\\))", "\\(\\text{Cells/day} = 35,000\\text{ cells/min} \\times 60\\text{ min} \\times 24\\text{ hr} = 5.04 \\times 10^7\\text{ cells}\\)", "\\(\\approx 5.04 \\times 10^5\\), \\(\\approx 5.04 \\times 10^9\\), \\(\\approx 1.00 \\times 10^6\\)"),
            ("In human intestinal mucosa, complete epithelial turnover of enterocytes occurs every 4 days (96 hours). If the intestinal lining comprises \\(1.0 \\times 10^{11}\\) epithelial cells, how many new enterocytes are produced by crypt stem cells every hour?", "\\(\\approx 1.04 \\times 10^9\\text{ enterocytes/hour}\\) (\\(\\approx 1\\text{ billion/hr}\\))", "\\(\\text{Rate} = 1.0 \\times 10^{11}\\text{ cells} / 96\\text{ hours} \\approx 1.04 \\times 10^9\\text{ cells/hour}\\)", "\\(\\approx 1.04 \\times 10^7\\), \\(\\approx 1.04 \\times 10^{11}\\), \\(\\approx 5.00 \\times 10^8\\)"),
            ("The respiratory diffusion barrier in human lung alveoli has an average thickness of \\(0.5\\text{ }\mu\\text{m}\\) (\\(5.0 \\times 10^{-7}\\text{ m}\\)) and total surface area \\(100\\text{ m}^2\\). According to Fick's Law (\\(J = -D A \\Delta C / \\Delta x\\)), if pulmonary fibrosis doubles barrier thickness to \\(1.0\\text{ }\mu\\text{m}\\), by what factor is the rate of oxygen diffusion reduced?", "Reduced to \\(1/2\\) (by \\(50\\%\\))", "Diffusion rate is inversely proportional to membrane thickness \\(\\Delta x\\); doubling thickness halves the diffusion rate", "Reduced to 1/4, Reduced to 1/10, Diffusion rate remains unchanged"),
            ("A simple cuboidal epithelial cell in a renal collecting duct is a cube of side \\(12\\text{ }\mu\\text{m}\\). What is its volume and total surface area?", "Volume: \\(1,728\\text{ }\mu\\text{m}^3\\); Surface area: \\(864\\text{ }\mu\\text{m}^2\\)", "\\(V = s^3 = 12^3 = 1,728\\text{ }\mu\\text{m}^3\\). \\(SA = 6s^2 = 6 \\times 144 = 864\\text{ }\mu\\text{m}^2\\)", "Volume: 1,000 μm^3; SA: 600 μm^2, Volume: 2,400 μm^3; SA: 1,200 μm^2, Volume: 864 μm^3; SA: 1,728 μm^2"),
            ("A human trachea has internal diameter \\(2.0\\text{ cm}\\) (circumference \\(\\approx 6.28\\text{ cm}\\)) and length \\(10\\text{ cm}\\). If ciliated epithelial cells average \\(10\\text{ }\mu\\text{m}\\) in diameter (surface area \\(100\\text{ }\mu\\text{m}^2 = 10^{-6}\\text{ cm}^2\\)), approximately how many ciliated cells line the tracheal lumen?", "\\(\\approx 6.28 \\times 10^7\\text{ ciliated cells}\\)", "\\(\\text{Tracheal area} = \\pi D L = 3.1416 \\times 2.0 \\times 10 = 62.83\\text{ cm}^2\\). Cells \\(= 62.83 / 10^{-6} \\approx 6.28 \\times 10^7\\)", "\\(\\approx 6.28 \\times 10^5\\), \\(\\approx 6.28 \\times 10^9\\), \\(\\approx 1.25 \\times 10^6\\)"),
            ("Cilia in human respiratory epithelium beat at an average frequency of \\(12\\text{ Hz}\\) (12 beats/second). How many forward effective power strokes are executed by a tracheal cilium in 1 hour?", "\\(43,200\\text{ power strokes}\\)", "\\(\\text{Strokes} = 12\\text{ beats/sec} \\times 3,600\\text{ s/hr} = 43,200\\)", "720, 4,320, 86,400"),
            ("The mucociliary escalator moves trapped particulate mucus upwards in the trachea at a steady velocity of \\(5\\text{ mm/minute}\\). How long does it take for a dust particle trapped in the mid-trachea to travel \\(60\\text{ mm}\\) (\\(6.0\\text{ cm}\\)) to the pharynx?", "\\(12\\text{ minutes}\\)", "\\(\\text{Time} = \\text{Distance} / \\text{Velocity} = 60\\text{ mm} / 5\\text{ mm/min} = 12\\text{ minutes}\\)", "30 minutes, 6 minutes, 60 minutes"),
            ("Transitional epithelium in an empty relaxed urinary bladder has a thickness of \\(6\\text{ cell layers}\\) (\\(\\approx 80\\text{ }\mu\\text{m}\\)). When distended with \\(500\\text{ mL}\\) of urine, umbrella cells flatten and the epithelium thins to \\(2\\text{--}3\\text{ cell layers}\\) (\\(\\approx 20\\text{ }\mu\\text{m}\\)). By what percentage has the epithelial thickness decreased?", "\\(75\\%\\text{ decrease}\\)", "\\(\\text{Decrease} = (80 - 20) / 80 = 60 / 80 = 0.75 = 75\\%\\)", "50% decrease, 25% decrease, 90% decrease")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Identify given physical and histological values.**\\n" + item[0] + "\\n\\n**Step 2: Apply the governing morphometric/biophysical formula.**\\n" + item[2] + ".\\n\\n**Step 3: Conclude.**\\nResult is " + item[1] + "."
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
            "**Step 1: Understand Histochemical & Diagnostic Stains for Epithelia.**\\n- PAS: Magenta line for Basement Membrane & Goblet cell mucins (oxidizes glycols \\(\\rightarrow\\) Schiff reaction).\\n- H&E: Hematoxylin (nuclei blue/purple) + Eosin (cytoplasm pink).\\n- Alcian Blue: Turquoise for acidic mucins.\\n- Pap Stain: Orange G (keratin) + EA50 (maturation grading in cervical screening).\\n- Cytokeratins: Intermediate filament IHC markers confirming carcinoma (epithelial) origin.\\n\\n**Step 2: Evaluate '" + item[0] + "'.**\\n" + item[1] + ".\\n\\n**Step 3: Laboratory / Diagnostic Significance:**\\n" + item[2] + "."
        ),
        'diff': 'medium'
    }
"""

# Replace the archs list in gen_3_3_1
text = text.replace(
    "    archs = [arch1, arch2, arch3, arch4, arch1, arch2, arch3, arch4]\n    return generate_vault_questions(\"CBSE-9-SCIE-3-3.3.1\", \"Epithelial tissues: Squamous, cuboidal, columnar, ciliated\", archs)",
    archs_3_3_1_new + "\n    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]\n    return generate_vault_questions(\"CBSE-9-SCIE-3-3.3.1\", \"Epithelial tissues: Squamous, cuboidal, columnar, ciliated\", archs)"
)

# In gen_3_3_3, add arch8 before archs = ...
arch8_3_3_3 = """
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
            ("Fast-Twitch (Type IIx/IIb / White) Muscle Fibers", "Rapid contraction velocity, low myoglobin content (pale/white appearance), low mitochondrial density, high glycogen content and glycolytic enzymes", "Relies on rapid anaerobic glycolysis; generates explosive power but fatigues quickly due to lactic acid and \\(\\text{H}^+\\) accumulation; dominates in sprinters, weightlifters, and extraocular eye muscles", "Slow contracting fibers that never fatigue, Red fibers rich in myoglobin, Postural muscles maintaining standing stance"),
            ("Intermediate (Type IIa / Fast Oxidative-Glycolytic) Fibers", "Fast contraction speed combined with intermediate mitochondrial density and aerobic/glycolytic capacity", "Recruited for middle-distance running, swimming, and sustained athletic power", "Pure white fibers with zero mitochondria, Spindle-shaped cells without striations, Dead muscle fibers"),
            ("Myoglobin in Red Muscle Fibers", "Monomeric heme-iron protein with high oxygen affinity (hyperbolic binding curve); stores oxygen inside sarcoplasm and facilitates \\(\\text{O}_2\\) diffusion from capillaries to mitochondria", "Imparts deep red color to endurance muscles and marine mammal divers (seals, whales)", "Tetrameric protein circulating in blood, Protein that synthesizes lactic acid, Enzyme that hydrolyzes glycogen"),
            ("Creatine Phosphate (Phosphocreatine) Energy Shuttle", "High-energy phosphate reservoir (\\(\\approx 20\\text{ mM}\\)) in muscle sarcoplasm; Creatine Kinase (CK) transfers phosphate to ADP, regenerating ATP in \\(< 1\\text{ millisecond}\\)", "Provides the immediate energy buffer sustaining maximal explosive exertion for the first 5 to 10 seconds (e.g., 100m sprint)", "Sustains marathon running for 5 hours, Stores glucose in liver, Dissolves lactic acid"),
            ("Oxygen Debt (Excess Post-Exercise Oxygen Consumption - EPOC)", "Elevated oxygen consumption continuing for hours post-exercise to replenish ATP and creatine phosphate stores, metabolize accumulated lactic acid (Cori cycle in liver), and re-oxygenate myoglobin", "Explains why athletes continue heavy breathing long after stopping vigorous exertion", "Permanent loss of oxygen leading to death, State where no oxygen enters lungs, Caused by lack of hemoglobin"),
            ("Lactic Acid and Muscle Fatigue (Cori Cycle)", "Intense anaerobic glycolysis converts pyruvate to lactic acid via Lactate Dehydrogenase (LDH), regenerating \\(\\text{NAD}^+\\); lactate is shuttled to the liver and converted back into glucose (gluconeogenesis)", "Intracellular \\(\\text{H}^+\\) ion accumulation reduces sarcoplasmic pH, inhibiting phosphofructokinase and competitive binding to troponin C, contributing to acute muscular fatigue", "Lactic acid burns muscle fibers permanently, Lactate is excreted 100% by kidneys in 1 minute, Formed by aerobic Krebs cycle"),
            ("Hypertrophy vs Hyperplasia in Muscle Growth", "Resistance strength training increases muscle size via Hypertrophy (increased myofibrillar diameter, actin/myosin protein synthesis, and satellite cell donation of nuclei); Hyperplasia (increase in cell number) is extremely limited or absent in adult human skeletal muscle", "Explains why bodybuilders develop massive muscle bellies without multiplying muscle fiber counts", "Bodybuilding increases muscle cell count by 10-fold, Hypertrophy refers to muscle death, Muscle grows by accumulating water only"),
            ("Tetanus vs Treppe (Staircase phenomenon)", "Treppe: gradual warm-up increase in twitch force when stimulated at low frequency due to warmed enzymes and residual sarcoplasmic \\(\\text{Ca}^{2+}\\); Tetanus: smooth, sustained maximal contraction produced when stimulus frequency is so high that relaxation between twitches is completely eliminated", "Physiological basis for normal sustained voluntary motor actions", "Tetanus is a flaccid paralysis, Treppe causes permanent muscle tearing, Tetanus is a disease caused only by viruses"),
            ("Rigor Mortis resolution after 24 to 48 hours", "Post-mortem muscular rigidity gradually resolves and muscles become flaccid due to autolytic enzymatic digestion of Z-discs and cross-bridges by endogenous lysosomal cathepsins and calpains", "Marks the post-mortem transition used in forensic medicine to estimate time of somatic death", "Resolved because ATP production resumes, Resolved by drinking water, Rigor mortis never resolves")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Muscle Fiber Types & Energetics.**\\n- Red Fibers (Type I): Slow-twitch, myoglobin-rich, high mitochondria/capillaries, aerobic oxidative, fatigue-resistant (postural, marathon).\\n- White Fibers (Type IIx/b): Fast-twitch, low myoglobin, high glycogen/glycolytic enzymes, anaerobic, explosive power, rapid fatigue (sprinters).\\n- Energy sources: ATP (1-2s) \\(\\rightarrow\\) Creatine Phosphate (5-10s) \\(\\rightarrow\\) Anaerobic Glycolysis (lactic acid, Cori cycle) \\(\\rightarrow\\) Aerobic phosphorylation.\\n\\n**Step 2: Evaluate '" + item[0] + "'.**\\n" + item[1] + ".\\n\\n**Step 3: Physiological / Biomechanical Significance:**\\n" + item[2] + "."
        ),
        'diff': 'hard'
    }
"""

text = text.replace(
    "    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]\n    return generate_vault_questions(\"CBSE-9-SCIE-3-3.3.3\", \"Muscular tissue: Striated, smooth, cardiac\", archs)",
    arch8_3_3_3 + "\n    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]\n    return generate_vault_questions(\"CBSE-9-SCIE-3-3.3.3\", \"Muscular tissue: Striated, smooth, cardiac\", archs)"
)

# In gen_3_3_4, add arch8 before archs = ...
arch8_3_3_4 = """
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
            ("Monosynaptic Reflex (e.g., Knee-jerk Patellar Reflex)", "Direct single synapse between sensory afferent neuron (muscle spindle Ia fiber) and motor efferent neuron in spinal cord gray matter, with zero intervening interneurons", "Most rapid reflex arc in the human body (latency \\(\\approx 20\\text{ ms}\\)); tested clinically to verify L2-L4 spinal nerve root integrity", "Complex polysynaptic reflex involving cerebral cortex, Reflex requiring 5 minutes to execute, Involuntary smooth muscle reflex"),
            ("Polysynaptic Withdrawal (Flexor) Reflex", "Noxious stimulus (e.g., stepping on a sharp nail) activates nociceptive pain fibers that synapse on multiple excitatory and inhibitory spinal interneurons", "Triggers ipsilateral flexor contraction (pulling foot away) and simultaneous contralateral extensor contraction (crossed-extensor reflex) to maintain standing balance", "Single synapse reflex without interneurons, Voluntary conscious decision in motor cortex, Reflex that pushes foot harder onto the nail"),
            ("Sympathetic vs Parasympathetic Autonomic Nervous System", "Sympathetic (Thoracolumbar outflow): 'Fight-or-Flight' response (dilates pupils, accelerates heart rate, bronchodilation, inhibits digestion; neurotransmitters: ACh at ganglion, Norepinephrine at target); Parasympathetic (Craniosacral outflow): 'Rest-and-Digest' response (constricts pupils, slows heart rate, stimulates digestion and peristalsis; neurotransmitters: ACh at both synapses)", "Dual antagonistic innervation fine-tunes involuntary visceral organ homeostasis", "Sympathetic slows heart rate while parasympathetic accelerates, Both use adrenaline as only transmitter, Sympathetic controls voluntary skeletal muscles"),
            ("Long-Term Potentiation (LTP / Hebbian Plasticity)", "Persistent strengthening of synapses based on recent patterns of high-frequency activity (tetanic stimulation), mediated by NMDA receptor activation and \\(\\text{Ca}^{2+}\\)-dependent AMPA receptor insertion", "Primary cellular and molecular mechanism underlying synaptic plasticity, learning, and long-term memory formation in the hippocampus", "Permanent destruction of synapses in Alzheimer's, Inability of nerves to fire action potentials, Rapid death of neurons after stimulation"),
            ("Electroencephalogram (EEG) Brain Waves", "Records synchronized postsynaptic potentials of millions of cortical pyramidal neurons using scalp surface electrodes", "Displays characteristic frequency bands: Alpha (\\(8\\text{--}13\\text{ Hz}\\), relaxed awake with eyes closed), Beta (\\(14\\text{--}30\\text{ Hz}\\), active alert mental focus), Theta (\\(4\\text{--}7\\text{ Hz}\\), light sleep), and Delta (\\(< 4\\text{ Hz}\\), deep slow-wave sleep)", "Measures single action potentials in a single axon, Records muscular twitches in scalp, Measures blood sugar in brain"),
            ("Lumbar Puncture (Spinal Tap) and CSF Sampling", "Inserting a spinal needle between L3/L4 or L4/L5 vertebrae into the subarachnoid space (below the conus medullaris where spinal cord ends at L1/L2)", "Safely samples Cerebrospinal Fluid (CSF) without risk of spinal cord puncture, diagnosing meningitis, subarachnoid hemorrhage, and multiple sclerosis (oligoclonal bands)", "Injects antibiotics directly into the heart, Takes a bone marrow biopsy from skull, Removes brain tumors without surgery"),
            ("Cerebrospinal Fluid (CSF) circulation pathway", "Formed by Choroid Plexus in lateral ventricles \\(\\rightarrow\\) Foramen of Monro \\(\\rightarrow\\) 3rd ventricle \\(\\rightarrow\\) Cerebral aqueduct of Sylvius \\(\\rightarrow\\) 4th ventricle \\(\\rightarrow\\) Foramina of Luschka/Magendie \\(\\rightarrow\\) Subarachnoid space \\(\\rightarrow\\) Arachnoid granulations into dural venous sinuses", "Cushions brain against trauma (buoyancy reduces effective 1400g brain weight to 50g), maintains intracranial pressure, and removes metabolic wastes", "Circulates through blood vessels like red blood cells, Fluid that fills the stomach, Produced by bone osteocytes"),
            ("Hydrocephalus (Water on the brain)", "Abnormal accumulation of CSF within brain ventricles due to impaired drainage (e.g., aqueductal stenosis) or defective arachnoid granulation reabsorption", "Increases intracranial pressure; in infants before cranial suture fusion, causes dramatic enlargement of head circumference and fontanelle bulging", "Drying of the brain due to lack of water, Shrinking of the skull into small size, Viral infection of ear"),
            ("Babinski Sign (Plantar Reflex)", "Stroking the lateral sole of the foot: normal adult response is downward plantar flexion of all toes; Babinski sign is upward dorsiflexion of the big toe and fanning of other toes", "Normal in infants under 1 year (unmyelinated corticospinal tract); in adults, indicates Upper Motor Neuron (UMN) lesion in corticospinal tract (stroke, MS, trauma)", "Diagnostic sign of broken ankle, Sign of vitamin deficiency, Indicates bone fracture"),
            ("Action Potential refractory periods (Absolute vs Relative)", "Absolute refractory period: voltage-gated \\(\\text{Na}^+\\) channels are inactivated; NO stimulus, however strong, can trigger another action potential; Relative refractory period: \\(\\text{Na}^+\\) channels reset but \\(\\text{K}^+\\) channels remain open (hyperpolarization); an action potential can fire only with a stronger-than-normal suprathreshold stimulus", "Ensures unidirectional forward propagation of action potentials along axons and sets the upper limit on neural firing frequency", "Allows action potentials to collide and reverse, Keeps nerve permanently contracted, Causes complete paralysis")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Systems Neurobiology & Clinical Diagnostics.**\\n- Reflexes: Monosynaptic (patellar knee-jerk, no interneuron, 20ms) vs Polysynaptic (withdrawal/crossed-extensor, interneurons).\\n- Autonomic: Sympathetic (fight-or-flight, NE at target) vs Parasympathetic (rest-and-digest, ACh at target).\\n- Neuroplasticity: LTP (NMDA receptor, \\(\\text{Ca}^{2+}\\) influx, learning/memory).\\n- Diagnostics: EEG waves (\\(\\alpha, \\beta, \\theta, \\delta\\)); Lumbar puncture at L3/L4 (samples CSF from subarachnoid space); Babinski sign (UMN lesion).\\n\\n**Step 2: Evaluate '" + item[0] + "'.**\\n" + item[1] + ".\\n\\n**Step 3: Clinical / Physiological Detail:**\\n" + item[2] + "."
        ),
        'diff': 'hard'
    }
"""

text = text.replace(
    "    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]\n    return generate_vault_questions(\"CBSE-9-SCIE-3-3.3.4\", \"Nervous tissue: Neuron structure (cyton, dendrites, axon, synapse)\", archs)",
    arch8_3_3_4 + "\n    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]\n    return generate_vault_questions(\"CBSE-9-SCIE-3-3.3.4\", \"Nervous tissue: Neuron structure (cyton, dendrites, axon, synapse)\", archs)"
)

# Clean up escape sequences
text = text.replace(r'\mu', r'\\mu')
text = text.replace(r'\\\\mu', r'\\mu')
text = text.replace(r'\Omega', r'\\Omega')
text = text.replace(r'\\\\Omega', r'\\Omega')

with open('scripts/build_cbse9_scie_ch3_part3.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated build_cbse9_scie_ch3_part3.py successfully!")
