import json

def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        "Uncontrolled biological variation",
        "Non-cellular spontaneous crystallization",
        "Artifact of optical distortion"
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
# SUBTOPIC 2.2.1: Phospholipid bilayer with embedded proteins
# Topic Code: CBSE-9-SCIE-2-2.2.1
# ==============================================================================
def gen_2_2_1():
    # Arch 1: Fluid Mosaic Model Formulation (Singer and Nicolson, 1972)
    arch1 = {
        'data': [
            ("Fluid Mosaic Model", "S.J. Singer and Garth L. Nicolson (1972)", "Quasi-fluid phospholipid bilayer with floating embedded proteins ('protein icebergs in a sea of lipids')", "Robert Hooke and Anton van Leeuwenhoek, James Watson and Francis Crick, Matthias Schleiden and Theodor Schwann"),
            ("Physical meaning of 'Mosaic' in the Fluid Mosaic Model", "The mosaic refers to proteins of various shapes and sizes embedded discontinuously within and on the phospholipid bilayer", "Creates an irregular, dynamic pattern like tiles in a mosaic floor", "The cell wall is made of colored stained glass tiles, The nucleus contains mosaic chromosomes, Lipids form hard geometric stone patterns"),
            ("Physical meaning of 'Fluid' in the Fluid Mosaic Model", "Lipids and proteins possess lateral mobility within the plane of the bilayer", "Enables membrane flexibility, endocytosis, cell division, self-repair, and dynamic signaling", "The membrane is composed entirely of pure liquid water, The membrane evaporates into gas at body temperature, The membrane dissolves in blood"),
            ("Earlier 'Sandwich Model' proposed by Hugh Davson and James Danielli (1935)", "Proposed that the phospholipid bilayer is coated on both outer surfaces by continuous sheets of globular proteins", "Superseded because it could not explain hydrophobic transmembrane proteins, membrane fluidity, or selective permeability", "Proposed that membranes are made of pure wood, Stated that animal cells have no lipids, Claimed membranes have no proteins"),
            ("J. David Robertson's 'Unit Membrane' hypothesis (1959)", "Proposed that all biological cellular and organelle membranes share a universal trilaminar (three-layered: protein-lipid-protein) electron microscopic appearance of ~7.5 nm thickness", "Fell short because it assumed static, invariant protein coats rather than dynamic embedded proteins", "Stated that only red blood cells have membranes, Claimed plant cells have no lipid bilayer, Asserted that membranes are made of RNA"),
            ("Thickness of a typical eukaryotic plasma membrane", "Approximately 7 to 10 nanometres (70 to 100 Ångströms)", "Encloses the cytoplasm while remaining flexible and dynamic", "1 to 2 millimetres, 100 micrometres, Exactly 0.1 nanometres"),
            ("Lipid-to-Protein ratio in typical biological membranes", "Approximately 40% lipids and 50-52% proteins by weight, with 8-10% carbohydrates (e.g. human erythrocyte membrane: 52% protein, 40% lipid, 8% carbohydrate)", "Varies depending on membrane function (e.g. mitochondrial inner membrane has ~75% protein for electron transport)", "99% lipid and 1% protein, 100% carbohydrate, 50% nucleic acid and 50% water"),
            ("Why the plasma membrane was not resolved until the invention of the Electron Microscope", "Light microscopes have a resolution limit of ~200 nm, whereas the plasma membrane is only ~7-10 nm thick, far below the diffraction limit of visible light", "Required the ~0.2 nm resolution of transmission electron microscopy to visualize the trilaminar lipid bilayer", "Because 19th-century scientists did not believe in membranes, Because light dissolves membranes instantly, Because membranes only formed in the 20th century"),
            ("Quasi-fluid nature of the lipid matrix", "Allows lateral diffusion of lipids and embedded proteins across the two-dimensional surface of the membrane", "Flip-flop (transverse migration from one leaflet to the other) is extremely rare without flippase enzymes", "The membrane behaves as a rigid brittle glass crystal, Lipids boil and bubble constantly, Proteins are permanently welded to fixed coordinates"),
            ("Why the plasma membrane is termed 'Selectively Permeable' (Semi-permeable)", "It permits the passage of solvent (water) and specific selective solutes while blocking the uncontrolled entry or exit of other substances", "Maintains cellular homeostasis by regulating internal cytoplasmic chemical composition", "It allows all molecules in the universe to pass freely without restriction, It blocks 100% of all matter from ever crossing, It only allows sand and dust to enter")
        ],
        'templates': [
            "In membrane biology: '{0}'. Identify the correct scientific fact or description:",
            "What foundational concept is described by: '{0}'?:",
            "Regarding the structure of the plasma membrane: '{0}' is characterized as:",
            "A student learns about the Fluid Mosaic Model: '{0}'. The accurate biological fact is:",
            "Which statement correctly details the membrane feature: '{0}'?:",
            "Analyze the biological model: '{0}' established that:",
            "What is the structural and historical reality of: '{0}'?:",
            "In modern cytology, '{0}' refers to:",
            "Why is '{0}' significant in understanding cellular boundary dynamics?:",
            "A biology question tests membrane models: '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1: Understand plasma membrane architecture.**\nThe widely accepted **Fluid Mosaic Model** was proposed by Singer and Nicolson in 1972.\n\n**Step 2: Key concept of '{item[0]}':**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 2: Phospholipid Molecular Anatomy and Bilayer Assembly
    arch2 = {
        'data': [
            ("Amphipathic (Amphiphilic) nature of phospholipids", "Possess both a hydrophilic (water-loving) polar head and hydrophobic (water-fearing) non-polar fatty acid tails within the same molecule", "Drives spontaneous self-assembly into stable lipid bilayers in aqueous environments", "Purely water-soluble like sugar, Completely non-polar like mineral wax, Possess four identical electrical charges"),
            ("Chemical composition of the hydrophilic polar head in phospholipids", "Glycerol molecule bound to a negatively charged phosphate group and an organic polar headgroup (e.g. choline, ethanolamine, serine)", "Interacts electrostatically and forms hydrogen bonds with water molecules in cytosol and extracellular fluid", "Two saturated fatty acid chains, Solid cholesterol rings, Pure cellulose polymer"),
            ("Chemical composition of the hydrophobic non-polar tails in phospholipids", "Two long-chain fatty acid hydrocarbon chains (one saturated, one unsaturated with a cis-double bond kink)", "Secluded away from aqueous water in the interior hydrophobic core of the bilayer", "Phosphate and sulfate ions, Amino acids joined by peptide bonds, Monosaccharide glucose rings"),
            ("Spontaneous formation of phospholipid bilayers in water", "Hydrophobic interactions: non-polar hydrocarbon tails cluster together to minimize contact with water, while polar heads face the aqueous surroundings", "Thermodynamically driven by the increase in entropy of surrounding water molecules (hydrophobic effect)", "Covalent bonds cross-link all phospholipid heads together, Magnetic attraction between metallic lipid ions, Atmospheric pressure forces lipids into sheets"),
            ("Role of the cis-double bond kink in unsaturated fatty acid tails", "Prevents tight parallel packing of hydrocarbon chains, keeping the membrane fluid at physiological and low temperatures", "Kinks create space within the hydrophobic core, lowering the membrane phase transition (freezing) temperature", "Straightens the fatty acid into a rigid rod, Glues the two leaflets together permanently, Bonds with extracellular DNA"),
            ("Liposomes and Micelles compared to biological bilayers", "Micelles are single-layered spherical droplets (tails inward); Liposomes are spherical vesicles enclosing an aqueous core bounded by a complete lipid bilayer", "Liposomes are widely used in medicine to encapsulate and deliver hydrophilic and hydrophobic pharmaceutical drugs", "Micelles have two bilayers while liposomes have none, Both are rigid mineral crystals with no lipids, Micelles only form in alcohol while liposomes form in air"),
            ("Leaflet asymmetry in the plasma membrane", "The outer and inner leaflets have distinct phospholipid compositions (e.g. phosphatidylcholine and sphingomyelin on outer leaflet; phosphatidylserine and phosphatidylethanolamine on inner leaflet)", "Negatively charged phosphatidylserine on the inner leaflet maintains membrane potential; its exposure on the outer leaflet triggers apoptosis phagocytosis", "Both leaflets are completely identical in chemical composition, Lipids flip rapidly between leaflets 10,000 times a second without enzymes, Outer leaflet contains no lipids"),
            ("Role of flippases, floppases, and scramblases in membrane asymmetry", "Enzymes that regulate transbilayer movement of phospholipids: flippases move specific lipids to inner leaflet (ATP-dependent); floppases move lipids to outer leaflet (ATP-dependent); scramblases randomly mix lipids (ATP-independent)", "Maintains and dynamically modifies functional lipid asymmetry between bilayer leaflets", "Synthesize glucose from carbon dioxide, Break down starch into maltose, Destroy the plasma membrane during digestion"),
            ("Hydrophobic core barrier against water-soluble molecules", "The central non-polar hydrocarbon core forms a high energetic barrier that repels polar, hydrophilic molecules and charged ions", "Guarantees that essential cytosolic metabolites (glucose, ATP, amino acids, RNA) cannot spontaneously leak out of the cell", "Allows large proteins to freely drift in and out without channels, Attracts heavy metal ions into the cytoplasm, Dissolves cellular DNA"),
            ("Thermal phase transition of the lipid bilayer (Gel to Fluid state)", "At low temperatures, membranes freeze into a rigid, non-functional paracrystalline gel; at physiological temperatures, thermal energy keeps it in a dynamic fluid state", "Organisms adapt by homeoviscous adaptation: incorporating more unsaturated fatty acids with kinks at lower temperatures", "Membranes boil into vapor at 37°C, Phase transition causes the cell wall to evaporate, Freezing causes lipids to transform into carbohydrates")
        ],
        'templates': [
            "In molecular cytology: '{0}'. Identify the correct structural or chemical fact:",
            "What biochemical feature explains: '{0}'?:",
            "Regarding phospholipid structure and membrane dynamics: '{0}' is characterized by:",
            "A biology student analyzes lipid bilayers: '{0}'. The accurate scientific fact is:",
            "Which statement correctly accounts for: '{0}'?:",
            "Analyze the biophysical property: '{0}' demonstrates that:",
            "What is the thermodynamic or structural reason for: '{0}'?:",
            "In membrane biochemistry, '{0}' refers to:",
            "Why is '{0}' critical in maintaining cellular boundary function?:",
            "A question on phospholipid chemistry asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand phospholipid molecular anatomy.**\nPhospholipids are **amphipathic** molecules containing:\n- Polar hydrophilic head (phosphate + glycerol) facing aqueous environments.\n- Non-polar hydrophobic tails (two fatty acid chains) sheltered in the bilayer core.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Membrane Proteins: Integral vs Peripheral and Functions
    arch3 = {
        'data': [
            ("Integral (Intrinsic / Transmembrane) Proteins", "Proteins firmly embedded within the lipid bilayer, spanning completely across both leaflets with hydrophobic amino acid alpha-helices traversing the core", "Can only be extracted by harsh detergents (e.g. SDS, Triton X-100) that disrupt the hydrophobic lipid bilayer", "Loosely attached to the outer surface by weak ionic bonds, Float freely in the blood serum without membrane contact, Made purely of carbohydrates without amino acids"),
            ("Peripheral (Extrinsic) Proteins", "Proteins located on the inner or outer surface of the bilayer, bound to lipid polar heads or integral proteins by weak non-covalent electrostatic interactions and hydrogen bonds", "Easily removed by mild treatments such as altering salt concentration or pH without disrupting the bilayer (e.g. spectrin, ankyrin)", "Permanently embedded across both lipid leaflets, Form the core hydrophobic barrier of the membrane, Contain zero amino acids"),
            ("Channel Proteins (Ion Channels, e.g. \\(\\text{Na}^+\\), \\(\\text{K}^+\\), \\(\\text{Ca}^{2+}\\), \\(\\text{Cl}^-\\))", "Transmembrane proteins with a hydrophilic central pore that allows specific inorganic ions to diffuse rapidly down their electrochemical gradient", "Can be gated (voltage-gated, ligand-gated, or mechanically gated) to open or close in response to cellular stimuli", "Pump ions against their concentration gradient using ATP, Synthesize lipids for the endoplasmic reticulum, Replicate nuclear DNA"),
            ("Carrier Proteins (Transporters / Permeases, e.g. GLUT glucose transporters)", "Transmembrane proteins that bind a specific solute, undergo reversible conformational shape changes, and release the solute on the other side of the membrane", "Can mediate facilitated diffusion (passive) or active transport (coupled to ATP)", "Remain open permanently as rigid non-selective wide holes, Consume oxygen to generate ATP, Digest the plasma membrane"),
            ("Active Transport Pumps (e.g. \\(\\text{Na}^+/\\text{K}^+\\) ATPase Pump)", "Primary active transporter that hydrolyzes 1 molecule of ATP to pump \\(3\\text{ Na}^+\\) out of the cell and \\(2\\text{ K}^+\\) into the cell against their steep concentration gradients", "Maintains resting membrane potential (\\(\\sim -70\\text{ mV}\\)), cell volume/osmotic balance, and drives secondary active transport of glucose and amino acids", "Allows sodium to rush passively into the cell without energy, Pumps water into the vacuole, Synthesizes proteins for secretion"),
            ("Receptor Proteins (e.g. G-Protein Coupled Receptors, Insulin Receptors)", "Transmembrane signaling proteins that bind specific extracellular chemical ligands (hormones, neurotransmitters) on outer surface", "Undergo conformational changes that activate intracellular second messenger signaling cascades (e.g. cAMP, phosphorylation) without ligand entering cell", "Transport the hormone physically into the nucleus, Digest the hormone into energy, Act as structural cellulose bricks"),
            ("Enzymatic Proteins on the plasma membrane", "Catalyze specific biochemical reactions at the inner or outer surface of the membrane (e.g. adenylate cyclase, membrane-bound peptidases)", "Transform substrate molecules right at the cellular interface", "Are inert structural rocks with no catalytic activity, Replicate viral RNA, Float in the atmospheric air"),
            ("Cell Adhesion Molecules (CAMs, e.g. Cadherins, Integrins, Selectins)", "Transmembrane proteins that bind cells to neighboring cells (desmosomes, tight junctions) or attach cells to extracellular matrix collagen/fibronectin", "Maintain tissue mechanical integrity, guide cell migration during development, and anchor the internal actin cytoskeleton", "Digest connective tissue fibers, Transmit electrical power lines between buildings, Form the cell wall in plant leaves"),
            ("Aquaporins (Water Channel Proteins, Peter Agre, 1992 Nobel Prize)", "Specialized tetrameric transmembrane channels containing a narrow 0.28 nm pore that permits rapid bidirectional diffusion of water molecules while completely blocking ions and protons", "Enables high water permeability in renal kidney tubules and plant root cells (up to 3 billion water molecules per second per pore)", "Pumps glucose against concentration gradient, Generates ATP from water flow, Synthesizes phospholipid molecules"),
            ("Spectrin and the Erythrocyte Cytoskeletal Meshwork", "Peripheral protein network on the cytosolic face of red blood cell membranes linked via ankyrin to transmembrane Band 3 proteins", "Confers extraordinary mechanical resilience, elasticity, and flexibility, allowing RBCs to deform through narrow 3-μm capillaries without shearing", "Makes RBCs rigid like glass rods, Dissolves hemoglobin, Acts as a photosynthetic pigment")
        ],
        'templates': [
            "In membrane protein biochemistry: '{0}'. Identify the correct structural or functional fact:",
            "What physiological role or classification is described by: '{0}'?:",
            "Regarding plasma membrane proteins: '{0}' is characterized as:",
            "A biology student analyzes transport mechanisms: '{0}'. The accurate fact is:",
            "Which statement correctly details: '{0}'?:",
            "Analyze the cellular function: '{0}' demonstrates that:",
            "What is the biochemical or physiological reality of: '{0}'?:",
            "In membrane transport, '{0}' refers to:",
            "Why is '{0}' critical in cellular physiology and homeostasis?:",
            "A cytology question examines membrane proteins: '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand membrane protein classifications.**\n- **Integral (Transmembrane):** Span the bilayer, hydrophobic core interactions, extractable only by detergents.\n- **Peripheral:** Surface-bound via non-covalent ionic bonds, easily dissociated.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Functional detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Cholesterol and Glycocalyx: Membrane Modulators and Recognition
    arch4 = {
        'data': [
            ("Role of Cholesterol in animal cell plasma membranes", "Acts as a bidirectional membrane fluidity buffer: prevents excessive fluidity at high temperatures and prevents crystallization/freezing at low temperatures", "Intercalates between phospholipid molecules with its hydroxyl group near polar heads and rigid steroid ring alongside fatty acid tails", "Serves as the primary genetic material of membranes, Dissolves cell walls in plant cells, Replaces ATP as energy currency"),
            ("Why plant cell membranes have little to no cholesterol", "Plant cells regulate membrane fluidity using phytosterols (e.g. sitosterol, stigmasterol) and higher proportions of polyunsaturated fatty acids", "The rigid cellulose cell wall provides external mechanical support, reducing dependence on sterol-mediated structural reinforcement", "Plant cells contain zero lipids of any kind, Plant cells freeze instantly above 50°C, Cholesterol is poisonous to plant chloroplasts"),
            ("Glycocalyx (Cell Coat)", "Carbohydrate-rich peripheral zone on the outer leaflet composed of oligosaccharide chains covalently bound to membrane lipids (glycolipids) and proteins (glycoproteins)", "Forms a protective, lubricated surface layer mediating cell-cell recognition, cellular identity, tissue compatibility, and receptor binding", "A thick layer of dead wood surrounding animal cells, An internal storage vacuole for starch, A layer of pure metallic minerals"),
            ("ABO blood group antigens on human red blood cells", "Oligosaccharide carbohydrate chains covalently linked to sphingolipids and proteins on the erythrocyte plasma membrane surface", "Specific terminal sugars determine blood type: N-acetylgalactosamine (Type A), Galactose (Type B), both (Type AB), neither (Type O)", "Determined by the shape of the red blood cell nucleus, Controlled by the amount of iron in hemoglobin, Determined by the number of flagella"),
            ("Major Histocompatibility Complex (MHC / HLA) glycoproteins", "Cell-surface glycoproteins that display peptide fragments to immune T-cells, enabling the immune system to distinguish 'self' from 'non-self'", "Primary barrier in organ transplant rejection; tissue typing matches MHC compatibility between donor and recipient", "Digest food in the stomach, Form the structural bones of the skeleton, Synthesize insulin hormone in the pancreas"),
            ("Glycolipids: Structure and location", "Lipids with covalently attached carbohydrate groups, located exclusively on the extracellular outer leaflet of the plasma membrane", "Contribute to glycocalyx structure, cell-cell interactions, and membrane stability", "Located inside the cell nucleus, Form the inner lining of mitochondria, Stored as fat in adipose tissue"),
            ("Selectins and cellular homing during inflammation", "Endothelial and leukocyte membrane glycoproteins that bind specific carbohydrate ligands on opposing cells, mediating leukocyte rolling and extravasation", "Directs white blood cells precisely to sites of bacterial infection or tissue injury", "Cause permanent destruction of all blood cells, Prevent white blood cells from ever moving, Form blood clotting fibrin threads"),
            ("Lipid Rafts (Membrane Microdomains)", "Dynamic, specialized microdomains of the plasma membrane enriched in cholesterol, sphingolipids, and specific signaling proteins", "Serve as organizing centers for signal transduction, endocytosis, and viral entry (e.g. HIV, influenza)", "Large physical holes where cytoplasm leaks out, Floating chunks of dead bone, Rigid iron plates bolted to the membrane"),
            ("Why carbohydrates are found EXCLUSIVELY on the extracellular face of the plasma membrane", "Asymmetric orientation established during synthesis: carbohydrate chains are attached inside the lumen of ER and Golgi, which becomes the external cell surface upon vesicle exocytosis", "Reflects the dedicated outward-facing role of oligosaccharides in external recognition, immune signaling, and cellular adhesion", "Because carbohydrates cannot survive inside water, Because enzymes inside cytoplasm eat all carbohydrates, Because sunlight attracts carbohydrates to the exterior"),
            ("Glycocalyx in vascular endothelial cells lining blood vessels", "Forms a delicate, negatively charged, non-thrombogenic endothelial surface layer that prevents inappropriate platelet sticking and leukocyte adhesion", "Disruption of endothelial glycocalyx leads to inflammation, capillary leakage, and atherosclerosis", "Hardens blood vessels into solid stone pipes, Replaces red blood cells, Generates heartbeats directly")
        ],
        'templates': [
            "In membrane biochemistry and immunology: '{0}'. Identify the correct scientific fact:",
            "What physiological function or structure is described by: '{0}'?:",
            "Regarding cholesterol and the glycocalyx: '{0}' is characterized as:",
            "A biology student analyzes cell surface recognition: '{0}'. The accurate fact is:",
            "Which statement correctly details the role of: '{0}'?:",
            "Analyze the biochemical feature: '{0}' demonstrates that:",
            "What is the biological and clinical reality of: '{0}'?:",
            "In cell biology, '{0}' refers to:",
            "Why is '{0}' significant in cellular identity and physiology?:",
            "A cytology question examines membrane surface components: '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand membrane modulators and surface recognition.**\n- **Cholesterol:** Fluidity buffer in animal membranes.\n- **Glycocalyx:** Outer carbohydrate coat (glycoproteins + glycolipids) mediating cell identity (e.g. ABO blood groups, MHC self-recognition).\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Passive vs Active Transport Across the Plasma Membrane
    arch5 = {
        'data': [
            ("Simple Diffusion", "Passive transport of small, non-polar molecules (\\(\\text{O}_2\\), \\(\\text{CO}_2\\), \\(\\text{N}_2\\)) directly across the phospholipid bilayer down their concentration gradient without transport proteins or ATP", "Rate is directly proportional to concentration gradient and membrane lipid solubility; non-saturable", "Requires ATP hydrolysis, Transports large charged proteins against gradients, Mediated by vesicular budding"),
            ("Facilitated Diffusion", "Passive transport of polar or charged solutes (glucose, amino acids, ions) across the membrane down their electrochemical gradient via specific channel or carrier proteins", "Does not require cellular metabolic ATP; exhibits saturation kinetics (\\(V_{\\max}\\)) when all carrier binding sites are occupied", "Pumps molecules from low to high concentration, Uses ATP energy directly, Destroys transport proteins after one use"),
            ("Primary Active Transport", "Direct consumption of metabolic energy (ATP hydrolysis) by a pump protein to transport solutes against their concentration gradient (e.g. \\(\\text{Na}^+/\\text{K}^+\\) ATPase, \\(\\text{Ca}^{2+}\\) ATPase)", "Generates and maintains steep transmembrane electrochemical ion gradients vital for cellular life", "Occurs spontaneously down concentration gradients, Does not use any energy or proteins, Operates only in dead cells"),
            ("Secondary Active Transport (Cotransport / Coupled Transport)", "Transport of a solute against its concentration gradient powered by the downhill movement of another solute (typically \\(\\text{Na}^+\\) or \\(\\text{H}^+\\)) whose electrochemical gradient was previously created by primary active transport", "Includes symport (both solutes move in same direction, e.g. \\(\\text{Na}^+\\)-glucose symporter SGLT1) and antiport (solutes move in opposite directions, e.g. \\(\\text{Na}^+/\\text{Ca}^{2+}\\) exchanger)", "Directly hydrolyzes ATP at the transport site, Is completely passive and identical to simple diffusion, Occurs only in plant vacuoles"),
            ("Endocytosis (Vesicular Bulk Ingestion)", "Active vesicular uptake of macromolecules, fluids, or large particles by invagination and pinching off of the plasma membrane to form an intracellular vesicle", "Requires cellular ATP and dynamic cytoskeletal actin rearrangement (includes phagocytosis, pinocytosis, receptor-mediated endocytosis)", "Passive diffusion of gases through lipid tails, The bursting of the cell membrane, Dissolution of the cell wall by enzymes"),
            ("Exocytosis (Vesicular Bulk Secretion)", "Active fusion of intracellular secretory vesicles with the plasma membrane, releasing their contents into the extracellular space and adding new membrane lipids/proteins", "Mediated by SNARE proteins and triggered by intracellular \\(\\text{Ca}^{2+}\\) elevation (e.g. neurotransmitter release, insulin secretion)", "Passive seepage of ions across pores, The division of the nucleus, Destruction of mitochondria"),
            ("Phagocytosis ('Cell Eating')", "Endocytosis of large solid particles, cellular debris, or intact microorganisms by extending pseudopodia that engulf the prey into a phagosome (e.g. macrophages, Amoeba)", "Phagosome fuses with a lysosome to form a phagolysosome where hydrolytic enzymes digest the contents", "Uptake of dissolved liquid droplets through tiny pits, Diffusion of oxygen gas across membranes, Excretion of pure mineral salt crystals"),
            ("Pinocytosis ('Cell Drinking')", "Non-specific endocytic internalization of extracellular fluid and dissolved solutes via small invaginating micro-vesicles", "Enables continuous surveillance and fluid sampling across capillary endothelia and epithelial cells", "Ingestion of large bacterial cells via pseudopodia, Transport of water through aquaporin channels, Pumping of sodium ions using ATP"),
            ("Receptor-Mediated Endocytosis (Clathrin-dependent endocytosis)", "Selective uptake of specific macromolecules (e.g. LDL cholesterol particles, transferrin/iron, hormones) that bind to cell-surface receptors concentrated in clathrin-coated pits", "Enables high-affinity concentrated uptake of trace ligands from extracellular fluids without internalizing massive fluid volumes", "Non-specific random engulfment of dirt, Diffusion of carbon dioxide, Active pumping of potassium ions"),
            ("Membrane potential (\\(V_m\\)) maintained by active transport", "An electrical voltage difference across the plasma membrane (interior negative, \\(\\sim -70\\text{ mV}\\) in neurons), created primarily by the electrogenic \\(\\text{Na}^+/\\text{K}^+\\) pump and selective \\(\\text{K}^+\\) leak channels", "Provides stored electrochemical potential energy to transmit nerve impulses, drive muscle contraction, and power nutrient uptake", "Means the inside of the cell is charged to +500 Volts like a wall socket, Signifies that the cell has zero electrical charges, Causes the cell to emit visible light sparks")
        ],
        'templates': [
            "In membrane transport physiology: '{0}'. Identify the correct scientific fact:",
            "What transport mechanism or concept is defined as: '{0}'?:",
            "Regarding cellular transport across membranes: '{0}' is characterized by:",
            "A biology student evaluates cellular transport: '{0}'. The accurate principle is:",
            "Which statement correctly differentiates and explains: '{0}'?:",
            "Analyze the membrane transport mechanism: '{0}' demonstrates that:",
            "What is the energetic and molecular reality of: '{0}'?:",
            "In biophysics of transport, '{0}' refers to:",
            "Why is '{0}' critical in cellular metabolism and signaling?:",
            "A cytology question examines transport types: '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Distinguish transport categories.**\n- **Passive Transport:** Down concentration gradient, no ATP required (Simple diffusion, Facilitated diffusion, Osmosis).\n- **Active Transport:** Against concentration gradient, requires ATP (Primary active pumps, Secondary active cotransporters).\n- **Bulk Transport:** Vesicular trafficking requiring ATP (Endocytosis, Exocytosis).\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Relative Permeability of the Lipid Bilayer to Different Classes of Molecules
    arch6 = {
        'data': [
            ("Small Non-Polar Hydrophobic Molecules (\\(\\text{O}_2\\), \\(\\text{CO}_2\\), \\(\\text{N}_2\\), steroid hormones, benzene)", "High permeability; diffuse rapidly and unhindered directly through the phospholipid bilayer without transport proteins", "Soluble in the hydrophobic interior core of the membrane; diffusion rate depends directly on concentration gradient", "Zero permeability; completely blocked by lipid heads, Require ATP-driven primary pumps to cross, Can only cross via endocytosis"),
            ("Small Uncharged Polar Molecules (\\(\\text{H}_2\\text{O}\\), urea, glycerol, ethanol)", "Moderate / Low permeability; can cross slowly across the lipid bilayer via transient thermal defects", "Water crosses slowly by simple diffusion, but specialized aquaporin channels drastically accelerate rapid physiological osmosis", "Cross faster than oxygen gas, Are completely blocked like giant proteins, Permanently dissolve the membrane"),
            ("Large Uncharged Polar Molecules (Glucose, fructose, sucrose, amino acids)", "Virtually impermeable; cannot cross the hydrophobic core by simple diffusion in physiological timeframes", "Require dedicated carrier proteins (e.g. GLUT facilitative transporters) or cotransporters to enter the cell", "Diffuse instantly across the bilayer within 1 microsecond, Dissolve the lipid tails upon contact, Replaced by carbon dioxide"),
            ("Inorganic Ions (\\(\\text{Na}^+\\), \\(\\text{K}^+\\), \\(\\text{Ca}^{2+}\\), \\(\\text{Cl}^-\\), \\(\\text{H}^+\\))", "Extremely low / zero permeability across pure lipid bilayer; completely blocked by the hydrophobic core", "Ions have a large hydration shell of ordered water molecules; stripping this shell to enter the non-polar hydrocarbon core is energetically prohibitive without ion channels", "Diffuse freely like oxygen, Cross faster than pure water, Are made of pure lipids and dissolve the bilayer"),
            ("Large Macromolecules (Proteins, polysaccharides, nucleic acids, DNA/RNA)", "Completely impermeable; zero diffusion across the lipid bilayer", "Must be internalized or secreted via vesicular transport (endocytosis / exocytosis)", "Diffuse directly through individual lipid tails, Float through the membrane like smoke, Pass through without energy"),
            ("Lipid solubility and the Overtons Rule (Charles Overton, 1899)", "The permeability of a non-electrolyte substance across the plasma membrane is directly proportional to its lipid-water partition coefficient (oil/water solubility)", "Substances that dissolve easily in organic lipids penetrate living cell membranes with the highest velocity", "Lipid-soluble substances are completely blocked by cell membranes, Water-soluble substances cross fastest without proteins, Overtons rule applies only to rocks"),
            ("Why synthetic lipid vesicles (liposomes) are impermeable to glucose without transport proteins", "Synthetic bilayers lack transmembrane transport proteins; the large polar hydroxyl groups of glucose cannot traverse the non-polar fatty acid core", "Reconstituting purified GLUT protein into the liposome restores rapid, saturable facilitated glucose transport", "Because glucose evaporates in water, Because liposomes are made of solid iron, Because glucose is a gas"),
            ("Hydration shell of inorganic ions and membrane impermeability", "Ions in water are surrounded by a tightly held cage of polar water dipoles; passing through the hydrophobic core requires vast desolvation energy", "Ion channels provide water-filled pores and carbonyl oxygen coordination rings that mimic hydration shells, allowing rapid ion transit without energy barrier", "Ions have no electrical charge in water, Hydration shells turn ions into solid ice, Water molecules destroy ions"),
            ("Effect of molecular size on simple diffusion rate across lipid bilayers", "Smaller molecules penetrate faster than larger molecules of identical polarity and lipid solubility", "Smaller molecules fit more easily between transient gaps created by flexing hydrocarbon tails in the fluid bilayer", "Molecular size has zero relationship to diffusion rate, Giant proteins diffuse faster than hydrogen gas, Larger molecules dissolve the bilayer faster"),
            ("General order of membrane permeability across pure phospholipid bilayers", "Small non-polar (\\(\\text{O}_2\\), \\(\\text{CO}_2\\)) > Small uncharged polar (\\(\\text{H}_2\\text{O}\\), ethanol) > Large uncharged polar (Glucose) > Ions (\\(\\text{Na}^+\\), \\(\\text{K}^+\\))", "Forms the biophysical foundation explaining why cells require diverse specialized transport proteins to survive", "Ions > Glucose > Water > Oxygen, Proteins > Ions > Water > Carbon dioxide, All molecules cross with identical velocity")
        ],
        'templates': [
            "In membrane biophysics: '{0}'. What is the correct scientific permeability classification?:",
            "How does the plasma membrane selectively treat: '{0}'?:",
            "Regarding the relative permeability of the lipid bilayer: '{0}' is characterized by:",
            "A biology student analyzes membrane barrier properties: '{0}'. The accurate fact is:",
            "Which statement correctly describes the permeability behavior of: '{0}'?:",
            "Analyze the biophysical transport barrier: '{0}' demonstrates that:",
            "What is the molecular reason for the permeability characteristics of: '{0}'?:",
            "In comparative membrane permeability, '{0}' refers to:",
            "Why is '{0}' critical for maintaining the internal cytoplasmic environment?:",
            "A cytology question examines selective permeability: '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand membrane permeability hierarchy.**\nAcross pure lipid bilayers:\n1. Small non-polar molecules (\\(\\text{{O}}_2, \\text{{CO}}_2\\)) \\(\\rightarrow\\) **High permeability**.\n2. Small uncharged polar (\\(\\text{{H}}_2\\text{{O}}\\)) \\(\\rightarrow\\) **Moderate/Low permeability**.\n3. Large polar (glucose) \\(\\rightarrow\\) **Very low / Impermeable**.\n4. Charged ions (\\(\\text{{Na}}^+, \\text{{K}}^+\\)) \\(\\rightarrow\\) **Impermeable**.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Experimental Evidence Supporting the Fluid Mosaic Model
    arch7 = {
        'data': [
            ("Mouse-Human Cell Fusion Experiment (Larry Frye and Michael Edidin, 1970)", "Mouse cells with specific surface antigens were fused with human cells using Sendai virus to form a heterokaryon", "Initially, antigens were segregated on separate halves; within 40 minutes at 37°C, both mouse and human antigens completely intermixed over the entire hybrid cell surface, proving lateral protein mobility", "Proved that proteins are fixed in concrete and never move, Proved that mouse cells eat human cells, Demonstrated that membranes are made of pure DNA"),
            ("Temperature dependence of antigen intermixing in the Frye-Edidin experiment", "Intermixing occurred rapidly at 37°C, but was completely inhibited at temperatures below 15°C", "Lower temperatures cause the lipid bilayer to freeze into a rigid gel phase, immobilizing embedded proteins and proving that fluidity is temperature-dependent", "Low temperatures make antigens explode, High temperatures turn proteins into lipids, Antigens move only in total darkness"),
            ("Freeze-Fracture Electron Microscopy (Branton, 1966)", "Frozen cells are cleaved with a diamond knife along the central hydrophobic plane of the lipid bilayer, splitting it into P-face (protoplasmic) and E-face (extracellular)", "Revealed globular protein particles protruding from the interior hydrophobic faces, conclusively disproving the Davson-Danielli sandwich model", "Proved that membranes contain no proteins, Showed that cells have no internal structure, Demonstrated that lipids are made of ice crystals"),
            ("Fluorescence Recovery After Photobleaching (FRAP)", "Fluorescently labeled membrane proteins or lipids are bleached in a small circular spot using an intense laser beam; recovery of fluorescence in the bleached area is tracked over time", "Unbleached fluorescent molecules laterally diffuse into the bleached region, providing quantitative measurement of membrane diffusion rates and mobile fractions", "The laser permanently destroys the cell nucleus, The bleached spot never recovers because proteins are immobile, Fluorescence is caused by radioactive decay"),
            ("Single Particle Tracking (SPT) in live cell membranes", "Tracking individual gold- or fluorophore-tagged membrane proteins using high-speed video microscopy with nanometre spatial precision", "Revealed that proteins undergo hop diffusion between microscopic compartments created by the underlying actin cytoskeleton 'fences' and transmembrane 'pickets'", "Proved that proteins teleport across cells instantaneously, Showed that proteins move only in straight lines, Demonstrated that lipids do not exist in live cells"),
            ("Differential scanning calorimetry (DSC) of biological membranes", "Measures heat absorption as a membrane transitions from a frozen gel phase to a fluid liquid-crystalline phase", "Determines the melting temperature (\\(T_m\\)) and reveals how cholesterol broadens the phase transition", "Measures the weight of the cell nucleus, Determines the color of cell pigments, Proves that cells boil at 0°C"),
            ("Detergent extraction of membrane proteins", "Non-ionic detergents (e.g. Triton X-100) solubilize integral proteins by replacing membrane lipids with detergent molecules without denaturing the protein", "Proves that integral proteins have hydrophobic transmembrane surfaces that interact directly with lipid tails", "Proves that proteins are attached by water, Dissolves only the cell nucleus while leaving membranes intact, Turns proteins into carbohydrates"),
            ("Atomic Force Microscopy (AFM) of lipid bilayers", "Uses an ultrafine scanning probe tip to image topography of lipid bilayers and measure mechanical membrane stiffness at sub-nanometre resolution", "Directly visualizes elevated lipid raft microdomains, membrane height, and protein conformational changes in physiological buffer", "Destroys the specimen with X-rays, Proves that membranes have no height, Measures nuclear radiation"),
            ("X-ray crystallography of transmembrane proteins", "Reveals that transmembrane segments consist of hydrophobic alpha-helices with non-polar amino acid side chains facing outward toward the lipid core", "First achieved for the photosynthetic reaction center (Deisenhofer, Huber, Michel, 1988 Nobel Prize)", "Showed that membrane proteins have no structure, Proved that membrane proteins are identical to DNA, Demonstrated that proteins are made of cellulose"),
            ("Patch-Clamp electrophysiology (Erwin Neher and Bert Sakmann, 1991 Nobel Prize)", "Seals a microscopic glass micropipette against a tiny patch of plasma membrane to record ion flow through individual single channel proteins (picoamperes)", "Directly demonstrated that ion channels are discrete molecular pore proteins that flicker between open and closed conformations", "Measures blood pressure in the aorta, Proves that current flows without ions, Measures the mass of the cell wall")
        ],
        'templates': [
            "In experimental cell biology: '{0}'. What critical scientific evidence did this provide?:",
            "How did the milestone investigation '{0}' validate the Fluid Mosaic Model?:",
            "Regarding experimental proof of membrane fluidity and structure: '{0}' demonstrated that:",
            "A biology student analyzes biophysical techniques: '{0}'. The accurate finding is:",
            "Which statement correctly explains the experimental methodology and conclusion of: '{0}'?:",
            "Analyze the historical experiment: '{0}' provided conclusive proof that:",
            "What was the revolutionary outcome of: '{0}'?:",
            "In experimental cytology, '{0}' refers to:",
            "Why was '{0}' critical in overthrowing earlier static membrane models?:",
            "A question on biophysical evidence asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1: Understand the experimental validation of the Fluid Mosaic Model.**\n- **Frye-Edidin (1970):** Mouse-human cell fusion proved lateral protein mobility.\n- **Freeze-fracture (1966):** Revealed transmembrane protein particles embedded inside the hydrophobic core.\n- **FRAP:** Quantified lateral diffusion rates.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'hard'
    }

    # Arch 8: Clinical and Applied Aspects of the Plasma Membrane
    arch8 = {
        'data': [
            ("Cystic Fibrosis (CFTR Channelopathy)", "Caused by mutations in the CFTR gene encoding an ABC transporter class-regulated chloride ion channel on epithelial plasma membranes", "Defective chloride transport leads to dehydrated, abnormally thick, viscous mucus in lungs, pancreas, and intestine, causing recurrent infections", "Caused by failure of hemoglobin to bind oxygen, Caused by overproduction of insulin hormone, Caused by a lack of cell walls in lungs"),
            ("Anesthetics and membrane lipid perturbation", "General volatile anesthetics (e.g. isoflurane, propofol) dissolve in hydrophobic lipid bilayers and bind specific transmembrane ion channels (GABA receptors)", "Modulates neuronal membrane fluidity and potentiates inhibitory ion conductance, suppressing central nervous system transmission", "Solidify the membrane into stone, Destroy the cell nucleus instantly, Function by boiling blood plasma"),
            ("Liposomes as targeted drug delivery nanocarriers", "Artificial lipid vesicles enclosing anti-cancer drugs (e.g. Doxil / liposomal doxorubicin) with PEGylated stealth surfaces", "Increases drug circulation time, enhances tumor accumulation via EPR effect, and reduces cardiotoxicity and systemic side effects", "Release toxic drugs exclusively into healthy liver cells, Destroy blood platelets immediately, Are rejected as bacterial cells"),
            ("Bacterial membrane targeting by Polymyxin and Daptomycin antibiotics", "Polymyxin binds bacterial lipid A / LPS and disrupts outer and inner membranes like a detergent, causing cell lysis; Daptomycin inserts into Gram-positive membranes causing rapid depolarization", "Bactericidal by destroying membrane barrier integrity without needing to enter the cytoplasm", "Inhibit DNA replication in the nucleus, Block cell wall synthesis in humans, Neutralize bacterial toxins chemically"),
            ("HIV entry via CD4 receptor and CCR5 coreceptor", "The HIV surface glycoprotein gp120 binds the host T-cell CD4 receptor, triggering conformational change to bind the CCR5 chemokine coreceptor and mediate membrane fusion", "Individuals homozygous for the CCR5-Δ32 deletion mutation lack functional coreceptor and are highly resistant to HIV infection", "HIV enters by chewing through the cell wall, HIV infects only cells that lack plasma membranes, HIV is destroyed by the plasma membrane instantly"),
            ("Cardiac Glycosides (Digoxin and Ouabain) mechanism", "Inhibit the \\(\\text{Na}^+/\\text{K}^+\\) ATPase pump on cardiac myocyte plasma membranes, raising intracellular \\([\\text{Na}^+]\\)", "Reduces \\(\\text{Na}^+/\\text{Ca}^{2+}\\) exchanger activity, elevating sarcoplasmic \\([\\text{Ca}^{2+}]\\) and increasing myocardial contractile force (positive inotropy)", "Accelerate heart rate to 300 bpm, Destroy cardiac muscle cells, Inhibit ATP synthesis in mitochondria"),
            ("Diabetes Mellitus and insulin-stimulated GLUT4 translocation", "Insulin binding to its tyrosine kinase receptor triggers signaling cascades that mobilize GLUT4 glucose transporters from intracellular vesicles to the plasma membrane", "Enables rapid facilitated glucose uptake into skeletal muscle and adipose tissue from the bloodstream", "Insulin breaks down the plasma membrane, Insulin transforms glucose into carbon dioxide gas, GLUT4 transports sodium ions"),
            ("Cholera Toxin mechanism and CFTR activation", "Cholera toxin ADP-ribosylates Gs-alpha subunit, locking adenylate cyclase in an active state and causing massive cAMP elevation", "Hyper-activates CFTR chloride channels on intestinal mucosal membranes, causing massive secretomotor diarrhea and severe dehydration", "Destroys all intestinal cells immediately, Blocks water from entering the intestine, Freezes the plasma membrane into gel"),
            ("Local Anesthetics (Lidocaine, Novocaine) mechanism", "Reversibly block voltage-gated \\(\\text{Na}^+\\) channels from the intracellular face of the neuronal plasma membrane", "Prevents sodium influx, halting action potential generation and propagation along sensory pain nerves", "Destroy pain receptors permanently, Cause systemic paralysis, Inhibit protein translation"),
            ("Familial Hypercholesterolemia (Brown and Goldstein, 1985 Nobel Prize)", "Genetic defect in the LDL receptor on hepatocyte plasma membranes, impairing clathrin-mediated endocytosis of LDL cholesterol particles", "Leads to dangerously elevated blood LDL cholesterol levels, premature atherosclerosis, and early myocardial infarction", "Causes blood cells to burst from water influx, Results in complete loss of cell membranes, Destroys insulin receptors")
        ],
        'templates': [
            "In clinical medicine and pharmacology: '{0}'. Identify the correct scientific mechanism:",
            "What biomedical pathology or mechanism is described by: '{0}'?:",
            "Regarding membrane-related diseases and therapeutics: '{0}' is characterized by:",
            "A medical biology student analyzes channelopathies: '{0}'. The accurate fact is:",
            "Which statement correctly details: '{0}'?:",
            "Analyze the pharmacological mechanism: '{0}' demonstrates that:",
            "What is the cellular and molecular reality of: '{0}'?:",
            "In applied cytology, '{0}' refers to:",
            "Why is '{0}' significant in therapeutic pharmacology and pathology?:",
            "A question on membrane medicine asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand membrane pathology and pharmacology.**\nPlasma membrane proteins and lipids serve as critical drug targets and the focal point of genetic channelopathies.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Clinical detail:**\n{item[2]}."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-2-2.2.1", "Phospholipid bilayer with embedded proteins", archs)


# ==============================================================================
# SUBTOPIC 2.2.2: Diffusion of gases (CO2, O2)
# Topic Code: CBSE-9-SCIE-2-2.2.2
# ==============================================================================
def gen_2_2_2():
    # Arch 1: Basic Principles of Diffusion and Concentration Gradients
    arch1 = {
        'data': [
            ("Definition of Diffusion", "The spontaneous net movement of particles (atoms, ions, or molecules) from a region of higher concentration to a region of lower concentration down a concentration gradient until dynamic equilibrium is reached", "Driven by intrinsic thermal kinetic energy of particles; requires no external metabolic ATP energy", "The active pumping of particles against a concentration gradient using ATP, The movement of water across a semi-permeable membrane exclusively, The boiling of liquid into gas under pressure"),
            ("Concept of 'Dynamic Equilibrium' in diffusion", "A state where particles continue to move in all directions at equal rates such that there is no further net change in concentration across the space", "Molecular movement never stops at equilibrium; net flux is zero (\\(\\text{Rate}_{\\text{forward}} = \\text{Rate}_{\\text{reverse}}\\))", "All molecular motion freezes to absolute zero, All particles settle to the bottom of the container, Particles react chemically and disappear"),
            ("Concentration Gradient", "A gradual difference in the concentration of a substance across a distance or between two regions", "Steeper concentration gradients produce a faster initial rate of diffusion", "A physical barrier preventing particles from moving, A measure of the acidity of a solution, A magnetic field created by ions"),
            ("Why diffusion is classified as a 'Passive Transport' process", "Because it is powered entirely by the random thermal kinetic energy of the diffusing particles and requires zero cellular metabolic energy (no ATP)", "Occurs spontaneously in living and non-living systems alike", "Because it only occurs in dead organisms, Because it requires energy from sunlight directly, Because it is powered by nuclear forces"),
            ("Brownian Motion as physical proof of thermal kinetic energy", "The erratic, continuous, random zig-zag motion of microscopic particles (e.g. pollen grains in water, smoke particles in air) suspended in a fluid", "First described by Robert Brown (1827) and mathematically explained by Albert Einstein (1905) as collisions with invisible thermal fluid molecules", "Proves that pollen grains are alive and swimming, Proves that water contains microscopic electric motors, Demonstrates that gravity does not affect pollen"),
            ("Effect of Temperature on the rate of diffusion", "Higher temperatures increase the average kinetic energy and velocity of particles (\\(\\text{KE} = \\frac{3}{2} k_B T\\)), accelerating the rate of diffusion", "Particles move faster and collide more frequently, dispersing through the medium in less time", "Higher temperatures freeze particles and stop diffusion, Temperature has zero effect on molecular motion, Diffusion only occurs at 0°C"),
            ("Effect of Molecular Mass on diffusion rate (Graham's Law)", "Heavier molecules diffuse more slowly than lighter molecules at the same temperature (\\(\\text{Rate} \\propto 1/\\sqrt{M}\\))", "E.g. lighter ammonia gas (\\(\\text{NH}_3\\), \\(M = 17\\)) diffuses faster through air than heavier hydrogen chloride gas (\\(\\text{HCl}\\), \\(M = 36.5\\))", "Heavier molecules always diffuse faster because gravity pulls them harder, Molecular mass has no influence on diffusion, Gas molecules have no mass"),
            ("Effect of the Medium (State of Matter) on diffusion velocity", "Gases diffuse fastest, liquids diffuse moderately, and solids exhibit negligible/extremely slow diffusion", "Because intermolecular forces are weakest and mean free paths between collisions are longest in gases", "Solids diffuse faster than gases, Liquids cannot undergo diffusion, Gases freeze during diffusion"),
            ("Fick's First Law of Diffusion", "Diffusion flux is directly proportional to concentration gradient difference and membrane surface area, and inversely proportional to diffusion distance / membrane thickness", "\\(J = -D \\frac{dC}{dx}\\); governs all respiratory and cellular gas exchange", "Diffusion occurs only when pressure is zero, Flux is inversely proportional to temperature, Diffusion distance increases rate of exchange"),
            ("Net Movement vs Random Movement in diffusion", "Individual molecules move completely randomly in all directions due to thermal collisions; net directional movement occurs solely because there are more molecules in the high-concentration region to move away", "Diffusion is a statistical probabilistic phenomenon, not a conscious or forced push", "Molecules consciously travel towards empty areas, Molecules are magnetically attracted to low concentration, Molecules push each other away with electric repulsion")
        ],
        'templates': [
            "In physical chemistry and cellular biophysics: '{0}'. What is the correct scientific description?:",
            "What fundamental principle governs: '{0}'?:",
            "Regarding the physical laws of diffusion: '{0}' is characterized as:",
            "A student learns about molecular transport: '{0}'. The accurate physical fact is:",
            "Which statement correctly explains the concept: '{0}'?:",
            "Analyze the diffusion mechanism: '{0}' demonstrates that:",
            "What is the thermodynamic and kinetic reality of: '{0}'?:",
            "In cellular respiration and physics, '{0}' refers to:",
            "Why is '{0}' critical in understanding gaseous dispersion and biological uptake?:",
            "A biology question tests diffusion principles: '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand diffusion physics.**\n- **Diffusion:** Net passive movement of particles down a concentration gradient driven by thermal kinetic energy.\n- **Equilibrium:** Net flux = 0, dynamic continuous motion.\n- **Governed by Fick's Law:** Rate \\(\\propto \\frac{{\\text{{Area}} \\times \\Delta C}}{{\\text{{Distance}}}}\\).\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Cellular Respiration and Internal Gaseous Exchange (O2 and CO2)
    arch2 = {
        'data': [
            ("Why Oxygen (\\(\\text{O}_2\\)) continuously diffuses into living metabolizing cells", "Cellular respiration inside mitochondria constantly consumes \\(\\text{O}_2\\) as the terminal electron acceptor, keeping intracellular \\([\\text{O}_2]\\) lower than extracellular fluid", "The continuous inward concentration gradient drives spontaneous passive diffusion of \\(\\text{O}_2\\) into the cell across the lipid bilayer", "The cell actively pumps oxygen in using ATP pumps, Cells absorb oxygen because oxygen is magnetic, Oxygen is pulled in by gravity"),
            ("Why Carbon Dioxide (\\(\\text{CO}_2\\)) continuously diffuses out of living metabolizing cells", "The Krebs cycle and pyruvate decarboxylation inside mitochondria constantly produce \\(\\text{CO}_2\\) waste, keeping intracellular \\([\\text{CO}_2]\\) higher than extracellular fluid", "The continuous outward concentration gradient drives spontaneous passive diffusion of \\(\\text{CO}_2\\) out of the cell across the lipid bilayer", "The cell consumes carbon dioxide as food, Carbon dioxide is trapped permanently inside the cell, Carbon dioxide is actively pumped in using ATP"),
            ("Overall chemical equation of Aerobic Cellular Respiration", "\\(\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\rightarrow 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{ to } 38\\text{ ATP}\\)", "Glucose is oxidized to carbon dioxide while oxygen is reduced to water, releasing biochemical energy stored as ATP", "\\(6\\text{CO}_2 + 6\\text{H}_2\\text{O} \\rightarrow \\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2\\), \\(\\text{C}_6\\text{H}_{12}\\text{O}_6 \\rightarrow 2\\text{C}_2\\text{H}_5\\text{OH} + 2\\text{CO}_2\\), \\(\\text{O}_2 + \\text{CO}_2 \\rightarrow \\text{ATP}\\)"),
            ("How \\(\\text{O}_2\\) and \\(\\text{CO}_2\\) physically cross the plasma membrane", "Direct simple diffusion across the hydrophobic phospholipid bilayer without requiring any transport proteins or ATP", "Both are small, non-polar, uncharged gas molecules that dissolve readily in the lipid core of the bilayer", "Active transport via \\(\\text{Na}^+/\\text{K}^+\\) ATPase pumps, Facilitated diffusion through aquaporin channels, Endocytosis inside clathrin-coated vesicles"),
            ("Consequences of toxic accumulation of \\(\\text{CO}_2\\) inside a cell", "\\(\\text{CO}_2\\) reacts with water to form carbonic acid (\\(\\text{CO}_2 + \\text{H}_2\\text{O} \\rightleftharpoons \\text{H}_2\\text{CO}_3 \\rightleftharpoons \\text{H}^+ + \\text{HCO}_3^-\\)), drastically lowering cytoplasmic pH (cellular acidosis) and denaturing enzymes", "Continuous diffusion of \\(\\text{CO}_2\\) into the bloodstream is vital to prevent lethal intracellular acidification", "Accumulation of carbon dioxide turns the cell into wood, Cells use excess carbon dioxide to make starch, Carbon dioxide makes the cell freeze"),
            ("Role of Carbonic Anhydrase enzyme in red blood cells", "Catalyzes the rapid interconversion of \\(\\text{CO}_2\\) and \\(\\text{H}_2\\text{O}\\) into bicarbonate ions (\\(\\text{HCO}_3^-\\)) and \\(\\text{H}^+\\) in capillary beds (and reverse in lungs)", "Allows ~70% of metabolic \\(\\text{CO}_2\\) to be transported in blood plasma as soluble bicarbonate without forming gas bubbles", "Synthesizes oxygen from water, Transports glucose to brain, Digests hemoglobin"),
            ("Chloride Shift (Hamburger Phenomenon) during \\(\\text{CO}_2\\) transport", "Anion exchange protein (Band 3) exchanges \\(\\text{HCO}_3^-\\)) out of red blood cells for \\(\\text{Cl}^-\\) into red blood cells in systemic capillaries", "Maintains electrical neutrality across the erythrocyte plasma membrane as bicarbonate diffuses out into plasma", "Exchanges sodium for potassium using ATP, Transports oxygen into plasma, Destroys red blood cells in the spleen"),
            ("Partial pressure gradient driving lung-capillary \\(\\text{O}_2\\) diffusion", "Alveolar \\(p\\text{O}_2\\) is \\(\\sim 104\\text{ mmHg}\\) while deoxygenated pulmonary capillary blood \\(p\\text{O}_2\\) is \\(\\sim 40\\text{ mmHg}\\)", "Steep partial pressure gradient of \\(\\sim 64\\text{ mmHg}\\) drives rapid diffusion of oxygen across the thin alveolar-capillary membrane (0.5 μm) in 0.25 seconds", "Alveolar oxygen pressure is 0 mmHg, Capillary blood has higher oxygen pressure than air, Oxygen moves against pressure gradients"),
            ("Partial pressure gradient driving lung-capillary \\(\\text{CO}_2\\) diffusion", "Deoxygenated blood \\(p\\text{CO}_2\\) is \\(\\sim 45\\text{ mmHg}\\) while alveolar air \\(p\\text{CO}_2\\) is \\(\\sim 40\\text{ mmHg}\\)", "Although the gradient is only \\(\\sim 5\\text{ mmHg}\\), \\(\\text{CO}_2\\) diffuses rapidly because its solubility in water/tissues is ~20 to 24 times higher than \\(\\text{O}_2\\)", "Carbon dioxide has zero solubility in blood, Carbon dioxide gradient is over 500 mmHg, Carbon dioxide cannot cross alveolar walls"),
            ("Why respiratory surfaces must remain perpetually moist", "Gases (\\(\\text{O}_2\\) and \\(\\text{CO}_2\\)) must first dissolve in a thin film of aqueous liquid before they can diffuse across living plasma membranes", "Dry cell membranes become impermeable to gases and cellular tissues desiccate and perish", "Water prevents oxygen from burning the lungs, Moisture freezes gases into liquids, Moist lungs convert oxygen into nitrogen")
        ],
        'templates': [
            "In respiratory physiology and cellular metabolism: '{0}'. Identify the correct scientific fact:",
            "What biochemical or biophysical mechanism explains: '{0}'?:",
            "Regarding cellular gaseous exchange: '{0}' is characterized by:",
            "A biology student analyzes gas transport: '{0}'. The accurate physiological fact is:",
            "Which statement correctly details: '{0}'?:",
            "Analyze the respiratory mechanism: '{0}' demonstrates that:",
            "What is the cellular reality regarding: '{0}'?:",
            "In comparative respiration, '{0}' refers to:",
            "Why is '{0}' vital for cellular survival and metabolic homeostasis?:",
            "A question on cellular respiration asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand cellular gas exchange.**\n- **Oxygen consumption:** Mitochondria consume \\(\\text{{O}}_2\\) \\(\\implies\\) lower internal \\([\\text{{O}}_2]\\) \\(\\implies\\) \\(\\text{{O}}_2\\) diffuses in.\n- **Carbon dioxide production:** Krebs cycle produces \\(\\text{{CO}}_2\\) \\(\\implies\\) higher internal \\([\\text{{CO}}_2]\\) \\(\\implies\\) \\(\\text{{CO}}_2\\) diffuses out.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Gaseous Exchange in Unicellular Organisms vs Multicellular Adaptations
    arch3 = {
        'data': [
            ("Gaseous exchange in Amoeba and Paramecium", "Takes place entirely by simple passive diffusion of \\(\\text{O}_2\\) and \\(\\text{CO}_2\\) across the general body plasma membrane directly with surrounding pond water", "Extremely high surface-area-to-volume ratio and microscopic diffusion distance (<50 μm) allow diffusion to supply 100% of metabolic needs", "Possess microscopic internal lungs and gills, Pump gases using heart and blood vessels, Absorb oxygen through a specialized wooden mouth"),
            ("Why diffusion alone is sufficient for unicellular organisms but completely inadequate for humans", "As organism size increases, volume increases cubically (\\(r^3\\)) while surface area increases only quadratically (\\(r^2\\)), and diffusion distance to internal cells increases to centimetres", "Calculations show that an oxygen molecule would take over 3 years to diffuse from human skin to the heart by simple diffusion alone!", "Humans do not need oxygen, Unicellular organisms consume 1000 times more oxygen than humans, Diffusion stops working in warm-blooded animals"),
            ("Specialized adaptations of respiratory exchange surfaces in multicellular animals (e.g. lungs, gills)", "(1) Extremely large surface area (e.g. human lungs ~70-100 m², size of a tennis court); (2) Extremely thin diffusion barrier (0.2-0.5 μm); (3) Moist epithelial surface; (4) Rich capillary blood supply to maintain steep concentration gradients", "Optimizes all parameters of Fick's Law to maximize gas diffusion velocity", "Thick dry skin covering lungs, Absence of blood capillaries, Low surface area with thick cartilage barriers"),
            ("Respiratory pigment (Hemoglobin) necessity in large animals", "Oxygen has low solubility in aqueous blood plasma (~0.3 mL \\(\\text{O}_2\\)/100 mL plasma); hemoglobin binds \\(\\text{O}_2\\) reversibly, increasing oxygen-carrying capacity of blood by ~70-fold (~20 mL \\(\\text{O}_2\\)/100 mL blood)", "Maintains low free dissolved \\(p\\text{O}_2\\) in blood plasma at alveolar interfaces, preserving steep diffusion gradients", "Hemoglobin turns oxygen into carbon dioxide, Hemoglobin prevents oxygen from entering cells, Hemoglobin is an inert food protein"),
            ("Tracheal respiratory system in terrestrial insects", "A network of branching air-filled chitinous tubes (tracheae and fluid-filled tracheoles) that deliver atmospheric air directly to every individual body cell", "Bypasses the circulatory system completely; insect blood (hemolymph) does not carry hemoglobin or transport oxygen", "Insects breathe using internal gills in their stomach, Insects have large human-like lungs, Insects absorb oxygen exclusively through feet"),
            ("Counter-current exchange mechanism in fish gills", "Water flows over gill secondary lamellae in the opposite direction to blood flow through gill capillaries", "Maintains a continuous concentration gradient for \\(\\text{O}_2\\) diffusion across the entire length of the capillary, achieving ~80-85% oxygen extraction from water", "Water and blood flow in the same direction (concurrent), Extracts only 5% of dissolved oxygen, Freezes the gill filaments to save energy"),
            ("Cutaneous respiration in amphibians (e.g. Earthworm, Frog)", "Gas exchange occurs across thin, vascularized, moist skin continuously kept damp by mucous gland secretions", "Requires a damp terrestrial or aquatic environment; if the skin dries out, gas diffusion halts and the animal suffocates", "Skin is covered in thick dry reptile scales, Respiration occurs only through claws, Glands secrete oil that blocks all gas transfer"),
            ("Spiracles in insects", "Valve-controlled lateral external openings on the insect thorax and abdomen that regulate air entry into the tracheal system", "Can close to minimize respiratory water loss in dry terrestrial environments", "Are digestive mouths that swallow solid food, Sense sound vibrations like ears, Secrete venom during flight"),
            ("Alveoli in mammalian lungs", "Millions of microscopic thin-walled spherical air sacs (~300-500 million in humans) lined by simple squamous type I pneumocytes and enveloped by dense capillary networks", "Provides the vast, thin, moist interface where external gas exchange occurs between air and pulmonary blood", "Store food for winter hibernation, Contract like muscle fibers to pump air out, Produce red blood cells in the chest"),
            ("Surfactant (Dipalmitoylphosphatidylcholine) in alveoli", "Lipoprotein complex secreted by alveolar type II pneumocytes that reduces surface tension of alveolar fluid", "Prevents small alveoli from collapsing (atelectasis) during expiration and reduces the muscular work of lung expansion", "Stiffens alveoli into rigid bone cups, Destroys all oxygen molecules, Clots blood inside the lungs")
        ],
        'templates': [
            "In comparative respiratory biology: '{0}'. Identify the correct scientific fact:",
            "What physiological adaptation explains: '{0}'?:",
            "Regarding respiratory evolution: '{0}' is characterized as:",
            "A biology student compares gas exchange across species: '{0}'. The accurate fact is:",
            "Which statement correctly details the adaptation: '{0}'?:",
            "Analyze the biological gas exchange system: '{0}' demonstrates that:",
            "What is the biophysical reality regarding: '{0}'?:",
            "In respiratory anatomy, '{0}' refers to:",
            "Why is '{0}' critical for sustaining aerobic metabolism in multicellular life?:",
            "A question on comparative gas exchange asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand scaling of gas exchange.**\n- **Unicellular organisms:** High SA/V ratio, short diffusion distance (<50 μm) \\(\\implies\\) simple diffusion across general body surface is sufficient.\n- **Multicellular organisms:** Low SA/V ratio, massive internal diffusion distance \\(\\implies\\) require specialized respiratory surfaces (lungs, gills, tracheae) with huge surface area, thin membranes, and circulatory transport.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Plant Gaseous Exchange: Stomata, Guard Cells, and Lenticels
    arch4 = {
        'data': [
            ("Stomata (singular: Stoma)", "Microscopic elliptical pores found predominantly on the lower epidermis of leaves, bounded by a pair of specialized regulatory guard cells", "Primary pathway for photosynthetic \\(\\text{CO}_2\\) uptake, respiratory \\(\\text{O}_2\\) exchange, and transpirational water loss", "Water-absorbing roots inside soil, Woody bark protective lenticels, Flower petal color patches"),
            ("Guard cells in dicot leaves vs monocot leaves (grasses)", "Kidney- or bean-shaped in dicot leaves; Dumbbell-shaped in monocot leaves (grasses)", "Possess chloroplasts and differentially thickened inner cellulose microfibril walls", "Hexagonal dead cells in dicots, Spherical air bubbles in grasses, Lacking cell walls in all plants"),
            ("Mechanism of Stomatal Opening in daylight", "Active proton extrusion (\\(\\text{H}^+\\)-ATPase) drives \\(\\text{K}^+\\) and malate influx into guard cells \\(\\rightarrow\\) internal solute potential drops \\(\\rightarrow\\) endosmosis of water occurs \\(\\rightarrow\\) guard cells become turgid", "Because the outer cell wall is thin and elastic while the inner wall facing the pore is thick and rigid, turgid guard cells bow outward, opening the stomatal pore", "Guard cells lose all water and shrivel to open, Guard cells divide by mitosis every morning, Stomata are opened by wind blowing on the leaf"),
            ("Mechanism of Stomatal Closing in darkness or drought", "Proton pumping ceases and Abscisic Acid (ABA) stress hormone triggers massive \\(\\text{K}^+\\) and anion efflux \\(\\rightarrow\\) internal water potential rises \\(\\rightarrow\\) exosmosis occurs \\(\\rightarrow\\) guard cells become flaccid", "Flaccid guard cells straighten and their thick inner walls collapse together, sealing the stomatal aperture to prevent desiccation", "Guard cells swell with water until they burst, Stomata are sealed by wax secretions at night, Leaves drop off the tree every evening"),
            ("Radial Micellation of cellulose microfibrils in guard cell walls", "Cellulose microfibrils radiate outward from the dorsal to ventral wall like wheel spokes, preventing radial expansion while allowing longitudinal stretching", "Forces turgid guard cells to bend and curve outward in an arc, creating the central open aperture", "Causes guard cells to shrink when watered, Prevents water from entering the leaf, Glues the stomata shut permanently"),
            ("Gas exchange during Daytime vs Nighttime in plants", "Daytime: Photosynthesis exceeds respiration; net uptake of \\(\\text{CO}_2\\) and net release of \\(\\text{O}_2\\). Nighttime: Photosynthesis stops (no light); net uptake of \\(\\text{O}_2\\) and net release of \\(\\text{CO}_2\\) via cellular respiration", "Respiration occurs continuously 24 hours a day; photosynthesis occurs only in light", "Plants produce oxygen 24 hours a day even in pitch black darkness, Plants do not respire and never consume oxygen, Plants consume nitrogen gas at night"),
            ("Compensation Point in plant gas exchange", "The light intensity (typically at dawn and dusk) where the rate of photosynthesis exactly equals the rate of cellular respiration", "Net gaseous exchange of \\(\\text{CO}_2\\) and \\(\\text{O}_2\\) with the atmosphere is zero (all \\(\\text{CO}_2\\) produced by respiration is consumed by photosynthesis)", "The temperature where the plant freezes, The point where leaves fall off, The moment stomata burst from pressure"),
            ("Lenticels in woody stems and roots", "Permanent lens-shaped openings formed by loosely arranged non-suberized complementary cells in the periderm of woody bark", "Enable continuous passive diffusion of \\(\\text{O}_2\\) and \\(\\text{CO}_2\\) for respiration of living phloem, cambium, and ray cells in woody stems", "Absorb liquid water from rain, Secrete sticky sap to catch birds, Open and close using guard cells"),
            ("Pneumatophores (Respiratory roots) in Mangroves (e.g. Rhizophora, Avicennia)", "Specialized negative geotropic aerial roots that grow vertically upward above waterlogged, oxygen-depleted saline marsh mud", "Covered with numerous lenticels (pneumathodes) allowing atmospheric \\(\\text{O}_2\\) to diffuse into subterranean root aerenchyma tissue", "Roots that consume salt water and turn into wood, Thorns that protect against aquatic predators, Floating leaves that produce seeds"),
            ("Aerenchyma tissue in aquatic hydrophytes (e.g. Hydrilla, Water Lily)", "Specialized parenchymatous tissue with prominent, interconnected continuous air spaces/lacunae", "Provides buoyancy to float plant organs and provides internal gas diffusion conduits transporting \\(\\text{O}_2\\) from leaves down to submerged roots", "Dead sclerenchyma tissue for wood production, Water-absorbing root tissue, Toxic tissue protecting against fish")
        ],
        'templates': [
            "In plant physiology and gaseous exchange: '{0}'. Identify the correct scientific fact:",
            "What physiological mechanism or structure is described by: '{0}'?:",
            "Regarding plant gas exchange adaptations: '{0}' is characterized as:",
            "A biology student analyzes stomatal mechanics: '{0}'. The accurate botanical fact is:",
            "Which statement correctly details: '{0}'?:",
            "Analyze the botanical adaptation: '{0}' demonstrates that:",
            "What is the cellular and biophysical reality of: '{0}'?:",
            "In plant histology and environmental biology, '{0}' refers to:",
            "Why is '{0}' critical for balancing photosynthesis and transpirational water economy?:",
            "A question on plant respiration asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand plant gaseous exchange mechanisms.**\n- **Stomata:** Regulated by guard cell turgidity (\\(\\text{{K}}^+\\) and malate uptake \\(\\implies\\) endosmosis \\(\\implies\\) turgid guard cells bow open).\n- **Daytime:** Net \\(\\text{{CO}}_2\\) in, \\(\\text{{O}}_2\\) out.\n- **Nighttime:** Net \\(\\text{{O}}_2\\) in, \\(\\text{{CO}}_2\\) out.\n- **Lenticels / Pneumatophores:** Woody stem and mangrove root aeration.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Laboratory Demonstration Experiments on Gas Diffusion
    arch5 = {
        'data': [
            ("Demonstrating gas diffusion rate differences using \\(\\text{NH}_3\\) and \\(\\text{HCl}\\) in a glass tube", "Cotton soaked in concentrated ammonia (\\(\\text{NH}_3\\)) at one end and concentrated hydrochloric acid (\\(\\text{HCl}\\)) at the other end of a sealed horizontal glass tube", "A white dense ring of solid ammonium chloride (\\(\\text{NH}_4\\text{Cl}\\)) forms closer to the \\(\\text{HCl}\\) end, proving lighter \\(\\text{NH}_3\\) gas (\\(M=17\\)) diffuses faster than heavier \\(\\text{HCl}\\) gas (\\(M=36.5\\))", "The ring forms exactly at the midpoint, The ring forms inside the ammonia cotton, No reaction occurs because gases cannot travel in tubes"),
            ("Demonstrating respiration in germinating seeds using potassium hydroxide (KOH)", "Germinating seeds placed in a sealed conical flask connected to a bent delivery tube dipping into colored water, with a small test tube of KOH pellets inside the flask", "Seeds absorb \\(\\text{O}_2\\) and release \\(\\text{CO}_2\\); KOH absorbs the \\(\\text{CO}_2\\), creating a partial vacuum that causes colored water to rise up the delivery tube", "Water rises because seeds blow air into the tube, KOH releases oxygen into the flask, Water level drops because seeds drink water through air"),
            ("Testing exhaled air for carbon dioxide using lime water (\\(\\text{Ca(OH)}_2\\))", "Exhaling air through a glass straw into freshly prepared clear lime water turns it milky / turbid due to precipitation of insoluble calcium carbonate (\\(\\text{CaCO}_3\\))", "\\(\\text{Ca(OH)}_2 + \\text{CO}_2 \\rightarrow \\text{CaCO}_3\\downarrow + \\text{H}_2\\text{O}\\); prolonged bubbling turns it clear again as soluble calcium bicarbonate forms", "Lime water turns bright green, Lime water catches fire from oxygen, Lime water boils violently"),
            ("Measuring photosynthetic oxygen evolution using Hydrilla in a funnel setup", "Inverted glass funnel over \\(\\textit{Hydrilla}\\) plants submerged in water with an inverted water-filled test tube over the funnel stem in bright light", "Gas bubbles collect at the top of the test tube and rekindle a glowing wooden splint, proving the evolved gas is oxygen", "Gas collected is explosive hydrogen that pops with flame, Gas turns lime water milky proving it is carbon dioxide, Gas is poisonous chlorine"),
            ("Demonstration of diffusion of potassium permanganate (\\(\\text{KMnO}_4\\)) in water", "Dropping a single purple crystal of \\(\\text{KMnO}_4\\) into a beaker of undisturbed still water", "Purple color slowly spreads throughout the entire liquid over hours without stirring, proving continuous random thermal molecular motion", "Crystal remains completely unchanged at bottom forever, Water turns into solid ice instantly, Purple color vanishes into invisible gas"),
            ("Effect of temperature on \\(\\text{KMnO}_4\\) diffusion in water", "Comparing diffusion rate of \\(\\text{KMnO}_4\\) crystal in a beaker of ice-cold water vs a beaker of hot boiling water", "Purple color disperses dramatically faster in hot water because higher thermal kinetic energy increases molecular collision velocity", "Diffusion occurs faster in ice water because cold water is denser, Temperature has zero effect on color spread, Hot water destroys the purple color"),
            ("Demonstration of diffusion of nitrogen dioxide (\\(\\text{NO}_2\\)) gas vs air", "Inverting a gas jar of dense brown nitrogen dioxide gas over an upright gas jar of colorless air", "Brown \\(\\text{NO}_2\\) gas diffuses downward while colorless air diffuses upward against gravity until both jars have uniform pale brown coloration", "Dense \\(\\text{NO}_2\\) falls like liquid to the bottom and stays separated, Air blocks \\(\\text{NO}_2\\) from entering, Both jars turn black instantly"),
            ("Why boiled, cooled water cannot support aquatic fish respiration", "Boiling drives all dissolved gases (including dissolved \\(\\text{O}_2\\)) out of solution; if not re-aerated, fish suffocate from lack of dissolved oxygen", "Cold water holds more dissolved oxygen than warm water; boiling reduces dissolved oxygen concentration to near zero", "Boiling creates toxic poison in water, Boiled water has no hydrogen atoms, Boiled water is too heavy for fish to swim in"),
            ("Demonstrating that expired air has more \\(\\text{CO}_2\\) than inspired atmospheric air", "Using a two-way T-tube aspirator to bubble inspired room air through Lime Water A and expired air through Lime Water B", "Lime Water B (expired air) turns milky almost immediately, while Lime Water A remains clear for a long time (expired air has ~4% \\(\\text{CO}_2\\) vs ~0.04% in inspired air)", "Both turn milky at the exact same second, Neither turns milky, Atmospheric air has 50% carbon dioxide"),
            ("Using a respirometer to calculate Respiratory Quotient (RQ)", "Apparatus measuring simultaneous \\(\\text{O}_2\\) uptake and \\(\\text{CO}_2\\) output: \\(\\text{RQ} = \\frac{\\text{Volume of } \\text{CO}_2 \\text{ evolved}}{\\text{Volume of } \\text{O}_2 \\text{ consumed}}\\)", "\\(\\text{RQ} = 1.0\\) for carbohydrates (glucose); \\(\\text{RQ} \\approx 0.7\\) for fats/lipids; \\(\\text{RQ} \\approx 0.8\\) for proteins", "RQ is always equal to 100, RQ measures body temperature, RQ measures the volume of blood pumped by the heart")
        ],
        'templates': [
            "In experimental biology and laboratory chemistry: '{0}'. Identify the correct scientific fact:",
            "What observation and scientific conclusion result from: '{0}'?:",
            "Regarding laboratory demonstrations of gas diffusion and respiration: '{0}' proves that:",
            "A student conducts the practical: '{0}'. The accurate experimental observation is:",
            "Which statement correctly explains: '{0}'?:",
            "Analyze the experimental setup: '{0}' demonstrates:",
            "What is the chemical or physiological mechanism underlying: '{0}'?:",
            "In practical school science, '{0}' refers to:",
            "Why is '{0}' significant in confirming empirical principles of gas exchange?:",
            "A laboratory practical question asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1: Understand laboratory gas diffusion experiments.**\n- **\\(\\text{{NH}}_3\\) vs \\(\\text{{HCl}}\\):** White ring of \\(\\text{{NH}}_4\\text{{Cl}}\\) forms closer to \\(\\text{{HCl}}\\), proving lighter gases diffuse faster.\n- **KOH in seed respiration:** Absorbs \\(\\text{{CO}}_2\\), causing water rise.\n- **Lime water test:** \\(\\text{{Ca(OH)}}_2 + \\text{{CO}}_2 \\rightarrow \\text{{CaCO}}_3\\downarrow\\) turns milky.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Mathematical Problems: Diffusion Distance, Time, and Rates
    arch6 = {
        'data': [
            ("Calculate the diffusion time \\(t\\) across a cell membrane of thickness \\(10\\text{ nm}\\) if \\(D = 1.0 \\times 10^{-5}\\text{ cm}^2/\\text{s}\\) using \\(t \\approx x^2 / (2D)\\)", "5.0 * 10^-8 s (50 nanoseconds)", "\\(x = 10\\text{ nm} = 10^{-6}\\text{ cm}\\). \\(t = (10^{-6})^2 / (2 \\times 10^{-5}) = 10^{-12} / (2 \\times 10^{-5}) = 5.0 \\times 10^{-8}\\text{ s}\\)", "5.0 s, 0.05 s, 500 s"),
            ("Calculate the diffusion time for an oxygen molecule to diffuse across a human lung alveolar membrane of thickness \\(0.5\\text{ }\\mu\\text{m}\\) (\\(D = 1.0 \\times 10^{-5}\\text{ cm}^2/\\text{s}\\))", "1.25 * 10^-4 s (125 microseconds)", "\\(x = 0.5\\text{ }\\mu\\text{m} = 5 \\times 10^{-5}\\text{ cm}\\). \\(t = (25 \\times 10^{-10}) / (2 \\times 10^{-5}) = 1.25 \\times 10^{-4}\\text{ s}\\)", "1.25 s, 12.5 s, 0.0125 s"),
            ("Calculate diffusion time across \\(1\\text{ mm}\\) distance in tissue (\\(D = 1.0 \\times 10^{-5}\\text{ cm}^2/\\text{s}\\))", "500 s (8.3 minutes)", "\\(x = 1\\text{ mm} = 0.1\\text{ cm}\\). \\(t = (0.01) / (2 \\times 10^{-5}) = 500\\text{ s}\\)", "5 s, 0.5 s, 50000 s"),
            ("Calculate diffusion time across \\(1\\text{ cm}\\) distance in tissue (\\(D = 1.0 \\times 10^{-5}\\text{ cm}^2/\\text{s}\\))", "50,000 s (~14 hours)", "\\(x = 1\\text{ cm}\\). \\(t = 1 / (2 \\times 10^{-5}) = 50,000\\text{ s} \\approx 13.9\\text{ hours}\\)", "50 s, 500 s, 5 s"),
            ("Calculate diffusion time across \\(1\\text{ metre}\\) distance (human leg length) if organisms relied on diffusion alone (\\(D = 1.0 \\times 10^{-5}\\text{ cm}^2/\\text{s}\\))", "~500,000,000 s (~16 years!)", "\\(x = 100\\text{ cm}\\). \\(t = 10,000 / (2 \\times 10^{-5}) = 5 \\times 10^8\\text{ s} \\approx 15.85\\text{ years}\\)!", "10 minutes, 2 hours, 3 days"),
            ("Relative diffusion rates of ammonia (\\(\\text{NH}_3\\), \\(M = 17\\)) and hydrogen chloride (\\(\\text{HCl}\\), \\(M = 36.5\\)) using Graham's Law \\(\\frac{R_{\\text{NH}_3}}{R_{\\text{HCl}}} = \\sqrt{\\frac{M_{\\text{HCl}}}{M_{\\text{NH}_3}}}\\)", "1.47 times faster", "\\(\\sqrt{36.5 / 17} = \\sqrt{2.147} \\approx 1.465 \\approx 1.47\\)", "2.15 times faster, 0.47 times faster, Exactly 1.0 times"),
            ("Relative diffusion rates of oxygen (\\(\\text{O}_2\\), \\(M = 32\\)) and carbon dioxide (\\(\\text{CO}_2\\), \\(M = 44\\)) in air", "Oxygen diffuses ~1.17 times faster than carbon dioxide in air", "\\(\\sqrt{44 / 32} = \\sqrt{1.375} \\approx 1.173\\)", "Carbon dioxide diffuses 2 times faster, Oxygen diffuses 5 times faster, Both diffuse at identical speeds"),
            ("If the surface area of a respiratory membrane is doubled while maintaining identical thickness and concentration gradient, how does diffusion flux change?", "Doubles (increases by 100%)", "According to Fick's Law, diffusion rate \\(J \\propto \\text{Surface Area}\\)", "Halves, Quadruples, Remains unchanged"),
            ("If the thickness of an alveolar membrane triples due to pulmonary edema / fibrosis, how does the gas diffusion rate change?", "Decreases to one-third (reduced by 66.7%)", "According to Fick's Law, diffusion rate is inversely proportional to membrane thickness (\\(J \\propto 1/\\Delta x\\))", "Triples, Increases 9-fold, Remains completely unchanged"),
            ("If the concentration gradient \\(\\Delta C\\) across a cell membrane increases from 2 mM to 8 mM (4-fold increase), how does initial simple diffusion flux change?", "Increases 4-fold (quadruples)", "For simple passive diffusion, flux is directly proportional to concentration gradient (\\(J \\propto \\Delta C\\))", "Decreases by half, Increases by 16-fold, Remains constant due to saturation")
        ],
        'templates': [
            "Calculate or solve the biophysical diffusion problem: '{0}':",
            "From biophysical diffusion principles: '{0}'. The correct calculated answer is:",
            "A physics/biology calculation asks: '{0}'. Determine the result:",
            "Solve the quantitative transport task: '{0}':",
            "According to Fick's Law and diffusion mathematics: '{0}' yields:",
            "Calculate the numerical outcome for: '{0}':",
            "In quantitative physiological transport: '{0}' equals:",
            "Evaluate the mathematical parameter from: '{0}':",
            "A student calculates diffusion dynamics: '{0}'. The solution is:",
            "Determine the result for the transport calculation: '{0}':"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: State the relevant mathematical relationship.**\n- **Einstein diffusion relation:** \\(t \\approx \\frac{{x^2}}{{2D}}\\).\n- **Fick's Law:** \\(J = -D A \\frac{{\\Delta C}}{{\\Delta x}}\\).\n- **Graham's Law:** \\(\\frac{{R_1}}{{R_2}} = \\sqrt{{\\frac{{M_2}}{{M_1}}}}\\).\n\n**Step 2: Substitute the numerical values.**\n{item[2]}.\n\n**Step 3: Result:** **{item[1]}**."
        ),
        'diff': 'hard'
    }

    # Arch 7: Environmental Factors and Behavioral Regulation of Gas Exchange
    arch7 = {
        'data': [
            ("High Altitude Hypoxia and atmospheric pressure drop", "At high altitude (e.g. 4000 m), atmospheric pressure drops from 760 mmHg to ~460 mmHg; although \\(\\text{O}_2\\) is still 21%, alveolar \\(p\\text{O}_2\\) drops from 104 to ~50 mmHg", "Steepness of the diffusion gradient into pulmonary capillaries drops drastically, causing acute mountain sickness (hypoxemia)", "Oxygen percentage drops to 0%, Carbon dioxide replaces all oxygen, Lungs freeze into ice"),
            ("Acclimatization to high altitude in humans", "Kidneys secrete erythropoietin (EPO) hormone, stimulating red bone marrow to increase red blood cell production (polycythemia) and hemoglobin concentration", "Increases blood oxygen-carrying capacity and capillary density in skeletal muscles to compensate for reduced diffusion gradient", "Lungs shrink to half size, Body stops consuming oxygen, Blood turns into pure water"),
            ("Carbon monoxide (CO) poisoning as a competitive respiratory inhibitor", "CO binds hemoglobin with ~200 to 250 times higher affinity than oxygen, forming stable carboxyhemoglobin (COHb)", "Blocks oxygen binding sites and shifts the oxygen-hemoglobin dissociation curve to the left, preventing oxygen delivery to tissues (asphyxiation)", "CO causes lungs to burst mechanically, CO dissolves all red blood cells, CO turns blood into pure acid"),
            ("Hyperventilation and blood \\(\\text{pH}\\) changes (Respiratory Alkalosis)", "Rapid, deep breathing expels \\(\\text{CO}_2\\) faster than metabolic production, causing arterial \\(p\\text{CO}_2\\) to plummet (hypocapnia)", "Loss of carbonic acid drives blood pH up (>7.45), causing cerebral vasoconstriction, dizziness, and peripheral tetany", "Causes blood pH to drop into severe acidosis, Causes instant death within 2 seconds, Increases oxygen in tissues by 500%"),
            ("Hypoventilation and blood \\(\\text{pH}\\) changes (Respiratory Acidosis)", "Shallow or depressed breathing fails to expel \\(\\text{CO}_2\\), causing arterial \\(p\\text{CO}_2\\) to accumulate (>45 mmHg)", "Dissolves in plasma forming excess carbonic acid, lowering blood pH (<7.35) and suppressing nervous system function", "Causes blood pH to rise above 8.0, Causes body temperature to reach 100°C, Destroys all white blood cells"),
            ("Effect of wind/air movement on plant stomatal gas exchange", "Gentle breezes sweep away the boundary layer of still, humid air adhering to the leaf surface, steepening the diffusion gradient for water vapor and \\(\\text{CO}_2\\)", "Elevates transpiration and photosynthetic gas exchange up to a threshold; high gale winds trigger stress-induced stomatal closure", "Stops all gas movement, Glues stomata shut permanently, Freezes the leaf epidermis"),
            ("Why aquatic organisms expend much more energy on respiration than terrestrial animals", "Water is ~800 times denser and ~50 times more viscous than air, and holds ~30 times less oxygen per litre than atmospheric air (~7 mL/L in water vs 210 mL/L in air)", "Fish must expend ~10-20% of their total metabolic energy driving dense water across gills (compared to ~1-2% for human breathing)", "Water destroys oxygen molecules, Fish do not need oxygen, Water contains zero oxygen"),
            ("Effect of water temperature on dissolved oxygen concentration in aquatic ecosystems", "Warm water holds significantly less dissolved oxygen than cold water (thermal gas solubility relationship)", "Thermal pollution from power plants discharging hot water into rivers causes severe aquatic hypoxia and fish kills", "Hot water holds 10 times more oxygen, Temperature has zero effect on gas solubility, Cold water contains no dissolved oxygen"),
            ("Diving mammals (Whales, Seals) adaptations for prolonged breath-holding", "Possess massive blood volumes, exceptionally high myoglobin concentrations in skeletal muscles, and initiate profound diving reflex (bradycardia and peripheral vasoconstriction)", "Stores vast reserves of oxygen in muscle myoglobin and restricts blood flow exclusively to brain and heart during 60-90 minute deep dives", "Possess internal gills that extract oxygen from water, Breathe through skin like earthworms, Do not consume oxygen during dives"),
            ("Surfacing behavior of aquatic insects (e.g. Diving Beetles / Notonecta)", "Trap an air bubble (physical gill) under their elytra or on specialized hydrophobic abdominal hairs (plastron) before diving", "Oxygen from surrounding water diffuses into the bubble down its concentration gradient as the insect consumes oxygen, extending dive time", "Insects carry scuba tanks manufactured from leaves, Insects decompose water into oxygen using electricity, Insects breathe through their eyes")
        ],
        'templates': [
            "In environmental physiology and respiratory adaptation: '{0}'. Identify the correct scientific fact:",
            "What physiological mechanism explains: '{0}'?:",
            "Regarding environmental influences on gas exchange: '{0}' is characterized as:",
            "A biology student analyzes respiratory stress: '{0}'. The accurate physiological fact is:",
            "Which statement correctly details: '{0}'?:",
            "Analyze the ecological adaptation: '{0}' demonstrates that:",
            "What is the cellular and biophysical reality of: '{0}'?:",
            "In environmental cytology, '{0}' refers to:",
            "Why is '{0}' critical in maintaining organismal gas exchange under extreme conditions?:",
            "A question on gas transport adaptations asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand environmental influences on gas diffusion.**\n- **High altitude:** Lower \\(p\\text{{O}}_2\\) \\(\\implies\\) reduced diffusion gradient \\(\\implies\\) EPO release and polycythemia.\n- **Carbon monoxide:** High affinity for hemoglobin (250x) blocks \\(\\text{{O}}_2\\).\n- **Aquatic respiration:** Water has lower \\([\\text{{O}}_2]\\) and higher viscosity than air.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'hard'
    }

    # Arch 8: Clinical Pathologies of Gas Exchange: Pneumonia, Emphysema, and Asthma
    arch8 = {
        'data': [
            ("Pneumonia pathology affecting gas exchange", "Alveoli become inflamed and fill with inflammatory exudate fluid, pus, and cellular debris", "Severely increases diffusion distance and blocks ventilation, causing acute hypoxemia and respiratory distress", "Causes lungs to turn into bone, Destroys red blood cells in the liver, Blocks food in the esophagus"),
            ("Emphysema (Chronic Obstructive Pulmonary Disease - COPD)", "Enzymatic destruction of alveolar septal walls by elastase (often triggered by cigarette smoke), merging tiny alveoli into large, flaccid air cavities", "Drastically reduces total alveolar surface area for gas diffusion and destroys elastic recoil, trapping air in lungs during exhalation", "Increases lung surface area by 1000%, Causes excessive production of healthy oxygen, Is an acute viral infection that heals in 2 days"),
            ("Pulmonary Fibrosis pathology", "Accumulation of excess fibrous collagen connective tissue in the alveolar-capillary interstitial space (scarring of lung tissue)", "Increases diffusion distance (\\(\\Delta x\\)) and reduces lung compliance, severely retarding the rate of \\(\\text{O}_2\\) diffusion into blood", "Causes lung tissue to dissolve into liquid, Turns lungs into transparent glass, Accelerates oxygen diffusion 100-fold"),
            ("Asthma bronchospasm mechanism", "Spasmodic contraction of bronchial smooth muscle, mucosal edema, and hypersecretion of thick mucus obstructing airway lumens", "Restricts bulk air ventilation into alveoli, reducing alveolar \\(p\\text{O}_2\\) and causing wheezing and dyspnea", "Destroys alveolar walls permanently, Destroys red blood cells, Freezes the trachea into ice"),
            ("Carbon Dioxide Narcosis in severe chronic respiratory failure", "Extreme retention of \\(\\text{CO}_2\\) (hypercapnia) that depresses central nervous system function, leading to confusion, lethargy, coma, and death", "Normal central respiratory drive becomes blunted when arterial \\(p\\text{CO}_2\\) remains chronically elevated", "Causes uncontrollable running, Causes body temperature to reach boiling point, Turns skin bright green"),
            ("Cyanosis as a clinical sign of hypoxemia", "Bluish discoloration of skin, lips, and nail beds caused by abnormally high concentration of deoxygenated hemoglobin (>5 g/dL) in capillary blood", "Indicates severe impairment of alveolar gas diffusion or inadequate systemic blood oxygenation", "Caused by copper poisoning in blood, Indicates excessive oxygen in tissues, Caused by eating blue fruit"),
            ("Pulse Oximetry principle in monitoring arterial oxygenation", "Non-invasive optical sensor measuring differential light absorption of oxygenated hemoglobin (absorbs more infrared at 940 nm) vs deoxygenated hemoglobin (absorbs more red at 660 nm)", "Calculates peripheral arterial oxygen saturation (\\(\\text{SpO}_2\\), normal = 95-100%) in real time", "Measures blood glucose levels, Measures the count of white blood cells, Measures blood alcohol content"),
            ("Supplemental Oxygen Therapy in pulmonary diffusion impairment", "Administering breathing gas with high fraction of inspired oxygen (\\(\\text{FiO}_2 = 40-100\\%\\) compared to 21% in room air)", "Artificially elevates alveolar \\(p\\text{O}_2\\) up to 300-600 mmHg, steepening the diffusion gradient to force oxygen across thickened, damaged alveolar membranes", "Substitutes carbon dioxide for oxygen, Freezes the lungs, Eliminates the need for breathing"),
            ("Mechanical Ventilation in acute respiratory distress syndrome (ARDS)", "Positive pressure ventilation pushing humidified oxygen-rich air into lungs to recruit collapsed alveoli and sustain oxygenation", "Assists or replaces patient's respiratory muscular work while underlying lung inflammation is treated", "Pumps blood directly through veins, Heats the heart, Operates without oxygen"),
            ("Why Carbon Dioxide retention causes respiratory acidosis", "Accumulated \\(\\text{CO}_2\\) shifts the carbonic acid equilibrium rightward: \\(\\text{CO}_2 + \\text{H}_2\\text{O} \\rightleftharpoons \\text{H}_2\\text{CO}_3 \\rightleftharpoons \\text{H}^+ + \\text{HCO}_3^-\\)", "Excess \\(\\text{H}^+\\) ions overwhelm plasma buffers, lowering arterial pH below 7.35 and impairing enzymatic catalysis across the entire body", "Carbon dioxide turns into solid limestone in blood, Carbon dioxide destroys all water molecules, Carbon dioxide neutralizes all acids")
        ],
        'templates': [
            "In clinical pathology and respiratory medicine: '{0}'. Identify the correct scientific fact:",
            "What physiological mechanism or disease process is described by: '{0}'?:",
            "Regarding disorders of gas exchange: '{0}' is characterized by:",
            "A medical biology student analyzes pulmonary pathology: '{0}'. The accurate fact is:",
            "Which statement correctly details the pathology of: '{0}'?:",
            "Analyze the respiratory disorder: '{0}' demonstrates that:",
            "What is the cellular and biophysical consequence of: '{0}'?:",
            "In clinical pathophysiology, '{0}' refers to:",
            "Why is '{0}' critical in medical diagnosis and management of respiratory disease?:",
            "A question on pulmonary pathology asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand clinical respiratory pathology.**\nDiseases disrupt Fick's Law of diffusion:\n- **Emphysema:** Destroys surface area (\\(A\\)).\n- **Pneumonia / Fibrosis:** Increases membrane thickness/distance (\\(\\Delta x\\)).\n- **Asthma:** Impairs ventilation, lowering alveolar \\(p\\text{{O}}_2\\).\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-2-2.2.2", "Diffusion of gases (CO2, O2)", archs)


# ==============================================================================
# SUBTOPIC 2.2.3: Osmosis across semi-permeable membrane: endosmosis, exosmosis, plasmolysis
# Topic Code: CBSE-9-SCIE-2-2.2.3
# ==============================================================================
def gen_2_2_3():
    # Arch 1: Definition of Osmosis, Water Potential, and Semipermeability
    arch1 = {
        'data': [
            ("Definition of Osmosis", "The spontaneous net diffusion of solvent (water) molecules from a region of higher water potential (dilute solution / lower solute concentration) to a region of lower water potential (concentrated solution / higher solute concentration) across a selectively permeable membrane", "Osmosis is a special case of passive diffusion specifically involving water across a semi-permeable membrane", "The active pumping of water using ATP, The movement of solute particles from high to low concentration, The boiling of water inside plant roots"),
            ("Selectively Permeable Membrane in Osmosis", "A membrane that permits the free passage of water solvent molecules while obstructing or restricting the passage of solute particles", "E.g. cell plasma membrane, tonoplast of vacuole, egg membrane, cellophane tubing", "A membrane that allows all solute crystals to pass while blocking water, A sheet of impermeable glass, A membrane that destroys all water molecules"),
            ("Water Potential (\\(\\Psi_w\\)) concept", "The chemical free energy of water molecules per unit volume, measured in pressure units (Pascals / kPa); pure water at standard temperature and pressure has a reference water potential of exactly 0 kPa", "Adding solutes reduces free water concentration, making water potential negative (\\(\\Psi_w = \\Psi_s + \\Psi_p\\)); water always flows spontaneously from higher (less negative) to lower (more negative) \\(\\Psi_w\\)", "Pure water has a water potential of -1000 kPa, Water potential has no units and cannot be measured, Water flows from low to high water potential"),
            ("Solute Potential (\\(\\Psi_s\\) / Osmotic Potential)", "The component of water potential that reflects the presence of dissolved solute molecules; always has a negative value (or zero for pure water)", "As solute concentration increases, \\(\\Psi_s\\) becomes increasingly negative, lowering total water potential", "Always has a positive value above +1000 kPa, Is independent of solute concentration, Replaces gravity in plants"),
            ("Pressure Potential (\\(\\Psi_p\\) / Turgor Potential)", "The hydrostatic pressure exerted on water inside a closed compartment; in turgid plant cells, it represents the outward turgor pressure exerted against the cell wall (positive value)", "Elevates total water potential, counterbalancing negative solute potential", "Always has a negative value in turgid cells, Is zero in all plant cells, Melts the plasma membrane"),
            ("Osmotic Pressure (\\(\\Pi\\)) definition", "The minimum external hydrostatic pressure that must be applied to a solution to completely prevent the inward osmotic flow of pure water across a semi-permeable membrane", "Directly proportional to solute molar concentration and absolute temperature (van 't Hoff equation: \\(\\Pi = iCRT\\))", "The pressure that causes water to boil, The atmospheric pressure of air on water, The pressure created by plant roots growing in soil"),
            ("Reverse Osmosis (RO) principle", "Applying external pressure greater than the osmotic pressure (\\(P > \\Pi\\)) onto the concentrated solution side, forcing pure water molecules backward across the semi-permeable membrane against the natural osmotic gradient", "Widely utilized globally in seawater desalination and municipal drinking water purification systems", "Heating water to 500°C to destroy salt, Using giant magnets to extract salt, Pumping salt into pure water"),
            ("Aquaporins and the velocity of osmosis", "Specialized tetrameric transmembrane protein channels that facilitate exceptionally rapid bidirectional osmotic transit of water molecules across plasma membranes", "Allows water molecules to pass in single file (up to 3 billion molecules per second) while strictly blocking hydronium ions (\\(\\text{H}_3\\text{O}^+\\))", "Pump water actively against water potential using ATP, Synthesize water from oxygen and hydrogen, Filter bacteria from pond water"),
            ("Difference between Osmosis and Simple Diffusion", "Osmosis strictly requires a selectively permeable membrane and involves exclusively solvent (water) movement; Simple diffusion involves any solute/solvent particle and does not require a membrane", "Both are passive transport processes requiring zero cellular metabolic ATP", "Diffusion requires ATP while osmosis is passive, Osmosis occurs only in dead organisms, Diffusion applies only to water"),
            ("Net direction of water flow across an osmotic system", "From a region of higher water potential (lower osmotic pressure, lower solute concentration, more hypotonic) to a region of lower water potential (higher osmotic pressure, higher solute concentration, more hypertonic)", "Continues until water potentials equalize on both sides of the membrane (equilibrium)", "From hypertonic to hypotonic, Always from right to left regardless of concentration, In random circular loops")
        ],
        'templates': [
            "In biophysics and plant physiology: '{0}'. Identify the correct scientific fact:",
            "What fundamental principle governs: '{0}'?:",
            "Regarding the physical laws of osmosis: '{0}' is characterized as:",
            "A biology student analyzes water movement across membranes: '{0}'. The accurate concept is:",
            "Which statement correctly details: '{0}'?:",
            "Analyze the osmotic principle: '{0}' demonstrates that:",
            "What is the thermodynamic and biophysical reality of: '{0}'?:",
            "In cellular transport and osmoregulation, '{0}' refers to:",
            "Why is '{0}' critical for understanding plant water relations and desalination technology?:",
            "A question on osmotic fundamentals asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand osmotic definitions.**\n- **Osmosis:** Net movement of water from higher water potential (dilute) to lower water potential (concentrated) across a selectively permeable membrane.\n- **Water potential (\\(\\Psi_w\\)):** Pure water = 0 kPa; solutes make \\(\\Psi_w\\) negative.\n- **Osmotic pressure (\\(\\Pi\\)):** Pressure needed to halt osmosis.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: The Three Tonicity States: Hypotonic, Hypertonic, and Isotonic
    arch2 = {
        'data': [
            ("Hypotonic Solution", "A solution having a lower solute concentration (higher water potential / more dilute) than the internal fluid of a cell", "Causes net influx of water into the cell by **Endosmosis**", "Higher solute concentration than cell, Equal solute concentration to cell, Pure concentrated acid"),
            ("Hypertonic Solution", "A solution having a higher solute concentration (lower water potential / more concentrated) than the internal fluid of a cell", "Causes net efflux of water out of the cell by **Exosmosis**", "Lower solute concentration than cell, Equal solute concentration to cell, Pure distilled water"),
            ("Isotonic Solution", "A solution having the exact same solute concentration (and water potential) as the internal fluid of a cell", "Water molecules cross the membrane in both directions at equal rates; **net water flux is zero**", "Causes rapid endosmosis, Causes violent cell bursting, Causes immediate plasmolysis"),
            ("Animal cell (e.g. Red Blood Cell) placed in a Hypotonic Solution (pure water)", "Water rushes into the cell by endosmosis; lacking a rigid cell wall, the delicate plasma membrane stretches, swells, and bursts (**Lysis / Hemolysis**)", "Fatal to the animal cell; demonstrates why animals must regulate extracellular osmotic balance strictly", "The cell shrivels into a prickly ball, The cell undergoes plasmolysis, The cell remains completely unchanged"),
            ("Animal cell (e.g. Red Blood Cell) placed in a Hypertonic Solution (concentrated salt/sugar)", "Water leaves the cell by exosmosis; the cell loses volume, shrinks, and forms spiky scalloped edges (**Crenation**)", "Interferes with cellular metabolism and oxygen transport capacity", "The cell swells and bursts, The cell becomes turgid and stiff, The cell divides by mitosis"),
            ("Animal cell placed in an Isotonic Solution (e.g. 0.9% w/v saline / normal saline)", "No net change in cell volume or shape; maintains normal biconcave disc morphology", "Dynamic equilibrium exists where water enters and exits at identical velocities", "The cell explodes immediately, The cell shrivels, The cell forms a thick cellulose wall"),
            ("Plant cell placed in a Hypotonic Solution (pure water)", "Water enters the vacuole by endosmosis; the protoplast swells, pushing against the rigid cell wall, creating high internal **Turgor Pressure** (**Turgid state**)", "The rigid cellulose cell wall exerts equal and opposite **Wall Pressure**, preventing the plant cell from bursting", "The plant cell bursts like a balloon, The plant cell shrivels away from the wall, The plant cell dies instantly"),
            ("Plant cell placed in a Hypertonic Solution (concentrated solution)", "Water exits the vacuole and cytoplasm by exosmosis; the protoplast shrinks and pulls away from the rigid cell wall (**Plasmolysis**)", "The plant cell becomes flaccid; herbaceous plant shoots wilt", "The plant cell becomes excessively turgid, The plant cell bursts, The cell wall dissolves"),
            ("Plant cell placed in an Isotonic Solution", "No net water movement; the protoplast does not exert pressure against the cell wall (**Flaccid state**)", "Plant tissue lacks mechanical stiffness and feels soft and limp", "The cell is fully turgid and crisp, The cell is severely plasmolysed, The cell bursts"),
            ("Normal Saline (0.9% NaCl solution) in medical intravenous infusions", "Isotonic to human red blood cells and blood plasma; safely rehydrates patients without causing hemolysis or crenation of blood cells", "If pure distilled water were infused into a patient's veins, massive intravascular hemolysis would occur, causing fatal kidney failure and death", "Hypertonic solution that shrinks all blood cells to kill bacteria, Pure water that bursts all red blood cells, Concentrated acid that cleans blood vessels")
        ],
        'templates': [
            "In cellular tonicity and osmotic behavior: '{0}'. Identify the correct scientific fact:",
            "What physiological outcome occurs during: '{0}'?:",
            "Regarding cell responses in diverse tonicity environments: '{0}' is characterized as:",
            "A biology student places cells in different media: '{0}'. The accurate observation is:",
            "Which statement correctly accounts for: '{0}'?:",
            "Analyze the osmotic behavior: '{0}' demonstrates that:",
            "What is the cellular and morphological reality of: '{0}'?:",
            "In experimental osmoregulation, '{0}' refers to:",
            "Why is '{0}' critical in medical clinical practice and biological survival?:",
            "A question on tonicity states asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand tonicity states.**\n- **Hypotonic:** Water enters \\(\\implies\\) Endosmosis (Animal cell lyses; Plant cell becomes turgid).\n- **Hypertonic:** Water leaves \\(\\implies\\) Exosmosis (Animal cell crenates; Plant cell plasmolyses).\n- **Isotonic:** Net flux = 0 (Normal animal cell; Flaccid plant cell).\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 3: Plasmolysis and Deplasmolysis in Plant Cells
    arch3 = {
        'data': [
            ("Definition of Plasmolysis", "The shrinkage of the living protoplast (cytoplasm + vacuole + nucleus) away from the rigid cellulose cell wall when a plant cell is placed in a hypertonic solution", "Driven by exosmosis of water from the large central vacuole into the concentrated external medium", "The swelling of a plant cell until it bursts, The division of a plant cell nucleus, The synthesis of starch in chloroplasts"),
            ("Stages of Plasmolysis: Limiting, Incipient, and Full Plasmolysis", "Limiting: cell volume decreases without protoplast detachment; Incipient: protoplast begins to detach at the corners of the cell wall; Full: protoplast completely rounds up in the center", "Incipient plasmolysis is used experimentally to determine the osmotic pressure of plant cell sap (\\(\\text{TP} = 0\\))", "Full plasmolysis occurs in pure water, Incipient plasmolysis causes cell lysis, Limiting plasmolysis destroys the cell wall"),
            ("What occupies the space between the cell wall and the shrunken protoplast in a fully plasmolysed plant cell", "The external hypertonic solution", "Because the cellulose cell wall is fully permeable to water and small dissolved solutes, while the plasma membrane is selectively permeable", "Pure vacuum, Air gas, Cytoplasmic sap that leaked out"),
            ("Definition of Deplasmolysis (Recovery from Plasmolysis)", "The reversal of plasmolysis when a plasmolysed plant cell is returned to a hypotonic medium (e.g. pure water)", "Water re-enters the cell by endosmosis, the vacuole re-expands, and the protoplast pushes back against the cell wall, restoring turgidity", "The complete death and rotting of the plant cell, The detachment of the cell wall from the root, The transformation of plant cells into animal cells"),
            ("Permanent (Irreversible) Plasmolysis", "Occurs when a cell remains plasmolysed in a severely hypertonic or toxic solution for an extended duration, causing irreversible membrane damage and cell death", "Such dead cells cannot undergo deplasmolysis when returned to pure water", "Cells divide into 100 new cells, Cells become immortal, Cells transform into photosynthetic bacteria"),
            ("Why plant leaves wilt during severe drought or high fertilizer application", "Loss of turgor pressure due to water deficit or high soil solute concentration causes cells to become flaccid and plasmolysed", "Herbaceous plant stems and leaves rely on internal hydrostatic turgor pressure for mechanical stiffness; loss of turgor causes wilting", "The plant breaks down its cell walls to eat them, Leaves lose all chlorophyll within 5 seconds, Soil bacteria eat the leaf blades"),
            ("Preservation of food using high sugar or salt concentration (Pickles, Jams, Jellies, Salted Fish)", "Hypertonic sugar/salt solutions cause rapid exosmosis and fatal plasmolysis of contaminating bacteria and fungal spores, preventing microbial growth and spoilage", "Classic historical application of osmotic dehydration in food preservation", "Sugar poisons bacteria chemically, Salt creates high temperature that cooks bacteria, Microbes prefer to eat salt instead of food"),
            ("Salting weeds to kill them (Chemical weed control / Saline burn)", "Applying concentrated salt to weed foliage or soil creates an intensely hypertonic root environment, causing massive exosmosis, severe plasmolysis, and rapid death of weeds", "Known as 'chemical/osmotic burn' in agriculture", "Salt feeds the weeds to grow faster, Salt attracts insects that eat the weeds, Salt freezes the soil into solid ice"),
            ("Observation of Plasmolysis using Tradescantia / Rheo discolor leaf peel mount", "Epidermal peel from the lower purple surface of \\(\\textit{Rheo}\\) leaves placed in concentrated 10-20% sucrose or salt solution", "The purple anthocyanin pigment inside the central vacuole makes the shrinking protoplast vividly visible under a light microscope", "The purple pigment turns bright yellow, The cell walls dissolve within 10 seconds, Cells swim like protozoa"),
            ("Why dead plant cells do NOT exhibit plasmolysis", "Plasmolysis strictly requires a semi-permeable living plasma membrane; in dead cells, the plasma membrane is ruptured/denatured and fully permeable, so no osmotic gradient can be sustained", "Dead cell walls and debris simply soak up liquids like a sponge without cellular shrinkage", "Because dead cells have no cell walls, Because dead cells contain infinite water, Because dead cells repel sugar molecules")
        ],
        'templates': [
            "In plant cellular physiology: '{0}'. Identify the correct scientific fact:",
            "What botanical phenomenon is described by: '{0}'?:",
            "Regarding plasmolysis and deplasmolysis: '{0}' is characterized as:",
            "A student observes plant cells in hypertonic solution: '{0}'. The accurate observation is:",
            "Which statement correctly explains the mechanism of: '{0}'?:",
            "Analyze the cellular response: '{0}' demonstrates that:",
            "What is the biological and practical reality of: '{0}'?:",
            "In experimental plant biology, '{0}' refers to:",
            "Why is '{0}' critical in agricultural practice and food technology?:",
            "A question on plasmolysis asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand plasmolysis and deplasmolysis.**\n- **Plasmolysis:** Hypertonic solution \\(\\implies\\) exosmosis \\(\\implies\\) protoplast shrinks away from the cell wall.\n- **Space between wall and protoplast:** Filled with **external hypertonic solution** (cell wall is freely permeable).\n- **Deplasmolysis:** Hypotonic solution \\(\\implies\\) endosmosis \\(\\implies\\) protoplast re-expands.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Turgor Pressure, Wall Pressure, and Plant Mechanical Rigidity
    arch4 = {
        'data': [
            ("Turgor Pressure (TP)", "The outward hydrostatic pressure exerted by the swelling protoplast (fluid cell sap) against the inner surface of the rigid cell wall", "In fully turgid plant cells, TP can reach 10 to 20 atmospheres (1-2 MPa), providing mechanical firmness to non-woody tissues", "The inward pressure exerted by the cell wall, The atmospheric air pressure in the room, The pressure of sunlight on leaves"),
            ("Wall Pressure (WP)", "The equal and opposite inward mechanical pressure exerted by the rigid, elastic cellulose cell wall against the expanding turgid protoplast", "According to Newton's Third Law of Motion, \\(\\text{Wall Pressure} = \\text{Turgor Pressure}\\) in a fully turgid cell", "The pressure that causes the cell wall to burst, The pressure of sap flowing through xylem vessels, The gravitational pull of the earth on roots"),
            ("Diffusion Pressure Deficit (DPD) / Suction Pressure", "The net capacity or thirst of a plant cell to absorb water; \\(\\text{DPD} = \\text{OP} - \\text{TP}\\) (where OP is Osmotic Pressure and TP is Turgor Pressure)", "In modern water potential terminology: \\(\\Psi_w = -\\text{DPD}\\); water flows from lower DPD to higher DPD", "DPD is always zero in all cells, DPD is the pressure of air inside leaves, DPD is created by cellular respiration"),
            ("DPD and Water Potential in a Fully Turgid Cell", "\\(\\text{TP} = \\text{OP} \\implies \\text{DPD} = \\text{OP} - \\text{TP} = 0\\); Water potential \\(\\Psi_w = 0\\text{ kPa}\\)", "A fully turgid cell has zero net suction capacity; it cannot absorb any further water", "DPD is at its absolute maximum, Water rushes in and bursts the cell, Water potential is -1000 kPa"),
            ("DPD and Water Potential in a Fully Flaccid (Plasmolysed) Cell", "\\(\\text{TP} = 0 \\implies \\text{DPD} = \\text{OP}\\); Water potential is at its most negative value (\\(\\Psi_w = \\Psi_s\\))", "A flaccid cell has maximum water deficit / suction force to absorb water from surrounding hypotonic regions", "DPD is zero, Water flows out of the cell rapidly, Wall pressure is at maximum"),
            ("Role of Turgor Pressure in herbaceous plant support", "Maintains erect posture and stiffness of non-woody stems, leaves, and petals without requiring a bony skeleton or secondary lignified wood", "Loss of turgor causes immediate drooping and wilting of the plant", "Prevents plants from growing tall, Causes plant stems to break easily, Decreases photosynthesis rate to zero"),
            ("Role of Turgor Pressure in plant cell enlargement and growth", "Outward turgor pressure stretches the loosened, auxin-softened primary cell wall, driving cellular elongation during plant growth", "Without turgor pressure, plant cell expansion and organ elongation cannot physically occur", "Turgor pressure stops cells from growing, Cells grow by shrinking their walls, Cells grow only during winter dormancy"),
            ("Role of Turgor Pressure in Stomatal kinetics", "Differential turgor changes in guard cells regulate the opening and closing of stomatal pores for photosynthesis and transpiration", "High turgor opens the pore; low turgor closes the pore", "Turgor pressure permanently glues stomata shut, Stomata are operated by animal muscle fibers, Stomata are controlled by atmospheric wind alone"),
            ("Turgor movements in Mimosa pudica (Touch-me-not / Sensitive plant)", "Touching the leaf triggers an electrical action potential that causes rapid \\(\\text{K}^+\\) and water efflux from parenchymal cells in the lower half of the pulvinus", "Loss of turgor in the lower pulvinus causes the petiole to collapse and leaflets to fold inward within seconds (seismonastic movement)", "The leaf burns off and falls to the ground, The plant dies instantly from fright, The plant undergoes rapid cell division to hide"),
            ("Root penetration into compact soils driven by turgor pressure", "High turgor pressure generated in elongating root tip cells generates mechanical thrust forces (up to 1 MPa / 10 atm) to push through dense soil particles and rock crevices", "Enables roots to crack rocks and anchor deep into subterranean substrates", "Roots dissolve rocks with concentrated boiling acid, Roots pull rocks with muscle fibers, Roots grow only through existing open tunnels")
        ],
        'templates': [
            "In plant water relations and biomechanics: '{0}'. Identify the correct scientific fact:",
            "What physiological parameter or mechanism is described by: '{0}'?:",
            "Regarding turgor pressure and wall pressure: '{0}' is characterized as:",
            "A botany student calculates cell pressure dynamics: '{0}'. The accurate principle is:",
            "Which statement correctly details: '{0}'?:",
            "Analyze the plant biomechanical adaptation: '{0}' demonstrates that:",
            "What is the cellular reality regarding: '{0}'?:",
            "In plant cell physiology, '{0}' refers to:",
            "Why is '{0}' vital for mechanical support and plant organ movements?:",
            "A question on plant turgor mechanics asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand plant pressure relationships.**\n- **Turgor Pressure (TP):** Hydrostatic pressure of protoplast against cell wall.\n- **Wall Pressure (WP):** Equal inward counter-pressure of wall against protoplast.\n- **\\(\\text{{DPD}} = \\text{{OP}} - \\text{{TP}}\\).\n- In a **fully turgid cell:** \\(\\text{{TP}} = \\text{{OP}} \\implies \\text{{DPD}} = 0\\) (cannot absorb more water).\n- In a **flaccid cell:** \\(\\text{{TP}} = 0 \\implies \\text{{DPD}} = \\text{{OP}}\\).\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Classic School Laboratory Osmosis Experiments
    arch5 = {
        'data': [
            ("Potato Osmometer Experiment Setup", "A peeled potato tuber with a flat base and a scooped central cavity filled with concentrated sugar solution, placed in a Petri dish of colored water", "Water level inside the potato cavity rises over several hours, proving endosmosis across living potato parenchyma cells into the hypertonic sugar solution", "Water level inside the potato cavity drops to zero, Colored water turns into solid ice, The potato explodes into fragments"),
            ("Why a boiled potato fails to act as an osmometer", "Boiling denatures membrane proteins and ruptures plasma membranes of potato cells, destroying selective permeability; water level does not rise", "Proves that osmosis strictly requires living, selectively permeable membranes", "Boiling turns the potato into sugar, Boiling makes water evaporate instantly, Boiled potatoes become impermeable to water"),
            ("Raisin (Kishmish) Endosmosis and Exosmosis Experiment", "Dried raisins placed in pure water swell and become turgid (endosmosis); when swollen raisins are transferred to concentrated salt/sugar solution, they shrink and lose weight (exosmosis)", "Demonstrates bidirectional osmotic water transport depending on the external medium's tonicity", "Raisins burst into flames in water, Raisins double in weight in concentrated salt, Raisins undergo mitosis in sugar"),
            ("De-shelled Chicken Egg in Pure Water vs Concentrated Salt Solution", "Egg shell (calcium carbonate) is dissolved away by soaking in dilute \\(\\text{HCl}\\), leaving the inner selectively permeable egg membrane intact; de-shelled egg placed in water swells (endosmosis), while in saturated salt solution it shrinks (exosmosis)", "Classic demonstration of osmosis in animal membrane systems", "The egg cooks into an omelet, The egg shell grows back thicker in salt, The egg membrane bursts within 1 second in salt"),
            ("Dialysis Tubing (Visking Tubing) Osmometer Model", "Cellophane dialysis tubing filled with starch/glucose solution and submerged in a beaker of water containing iodine", "Water enters by endosmosis (causing tubing to swell) and iodine diffuses in (turning starch blue-black), while starch molecules are too large to diffuse out across the pore membrane", "Starch diffuses out into the beaker within 1 second, The tubing dissolves completely in water, Water leaves the tubing causing it to shrivel"),
            ("Rheo discolor leaf peel demonstration of Plasmolysis", "Lower purple epidermis of \\(\\textit{Rheo}\\) placed in 10% NaCl solution on a microscope slide", "The purple anthocyanin-colored vacuole noticeably shrinks away from the rectangular cell wall within 2 to 5 minutes", "The leaf peel turns bright green, The cell walls burst open, Cells begin swimming across the slide"),
            ("Why salt is sprinkled on sliced cucumbers or cabbage when making salads/slaw", "Hypertonic salt causes rapid exosmosis of water from cucumber/cabbage cells, drawing out water and leaving the vegetable crisp and seasoned", "Common everyday culinary application of osmotic dehydration", "Salt causes cucumber cells to swell with water, Salt cooks the cucumber chemically, Salt destroys all vitamins instantly"),
            ("Why touching concentrated salt or sugar solution with bare hands feels dry later", "Exosmosis draws water out from skin epidermal cells into the hypertonic layer, causing temporary localized skin dehydration and tightening", "Reversible upon rinsing with freshwater", "Salt burns through the bones, Sugar turns into fat under the skin, Hands become permanently mummified"),
            ("Measuring percentage water absorption in swollen raisins", "\\(\\text{Percentage Absorption} = \\frac{\\text{Mass of swollen raisins} - \\text{Mass of dry raisins}}{\\text{Mass of dry raisins}} \\times 100\\%\\)", "Standard quantitative class practical in Class 9 CBSE science curriculum", "\\(\\frac{\\text{Dry mass}}{\\text{Wet mass}} \\times 100\\%, \\text{Wet mass} + \\text{Dry mass}, \\text{Dry mass} \\times \\text{Wet mass}\\)"),
            ("Why dried seeds (beans, peas) swell dramatically when soaked in water", "Both Imbibition (adsorption of water by hydrophilic cellulose, pectin, and protein colloids) and Endosmosis occur simultaneously, generating massive swelling pressure", "Imbibition breaks the seed coat (testa) to initiate seed germination", "Seeds swell because they are dividing by mitosis, Seeds absorb water through open mouths, Seeds swell because air enters them")
        ],
        'templates': [
            "In experimental school biology practicals: '{0}'. Identify the correct scientific fact:",
            "What observation and scientific deduction result from: '{0}'?:",
            "Regarding laboratory investigations of osmosis: '{0}' proves that:",
            "A student performs the experiment: '{0}'. The accurate laboratory observation is:",
            "Which statement correctly explains: '{0}'?:",
            "Analyze the practical investigation: '{0}' demonstrates:",
            "What is the biological and physical mechanism underlying: '{0}'?:",
            "In practical cell biology, '{0}' refers to:",
            "Why is '{0}' critical in demonstrating osmotic principles empirically?:",
            "A laboratory practical exam question asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1: Understand laboratory osmosis demonstrations.**\n- **Potato osmometer:** Endosmosis into hypertonic cavity; failed in boiled potato (dead membrane).\n- **Raisins:** Swell in water (endosmosis), shrink in concentrated salt (exosmosis).\n- **De-shelled egg:** \\(\\text{{HCl}}\\) removes \\(\\text{{CaCO}}_3\\) shell; swells in water, shrinks in salt.\n- **Rheo peel:** Purple vacuole shrinks in hypertonic solution.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Mathematical Problems: Osmotic Calculations and Raisin Percentage Absorption
    arch6 = {
        'data': [
            ("Mass of dry raisins = 10.0 g, Mass of swollen raisins after soaking in water = 15.0 g. Calculate percentage water absorption", "50.0%", "\\(\\text{Absorption} = \\frac{15.0 - 10.0}{10.0} \\times 100\\% = \\frac{5.0}{10.0} \\times 100\\% = 50.0\\%\\)", "25.0%, 150.0%, 33.3%"),
            ("Mass of dry raisins = 20.0 g, Mass of swollen raisins = 32.0 g. Calculate percentage water absorption", "60.0%", "\\(\\text{Absorption} = \\frac{32.0 - 20.0}{20.0} \\times 100\\% = \\frac{12.0}{20.0} \\times 100\\% = 60.0\\%\\)", "30.0%, 160.0%, 40.0%"),
            ("Mass of dry raisins = 8.0 g, Mass of swollen raisins = 14.0 g. Calculate percentage water absorption", "75.0%", "\\(\\text{Absorption} = \\frac{14.0 - 8.0}{8.0} \\times 100\\% = \\frac{6.0}{8.0} \\times 100\\% = 75.0\\%\\)", "37.5%, 175.0%, 50.0%"),
            ("Mass of dry raisins = 25.0 g, Mass of swollen raisins = 45.0 g. Calculate percentage water absorption", "80.0%", "\\(\\text{Absorption} = \\frac{45.0 - 25.0}{25.0} \\times 100\\% = \\frac{20.0}{25.0} \\times 100\\% = 80.0\\%\\)", "40.0%, 180.0%, 20.0%"),
            ("Mass of dry raisins = 12.0 g, Mass of swollen raisins = 24.0 g. Calculate percentage water absorption", "100.0%", "\\(\\text{Absorption} = \\frac{24.0 - 12.0}{12.0} \\times 100\\% = \\frac{12.0}{12.0} \\times 100\\% = 100.0\\%\\)", "50.0%, 200.0%, 25.0%"),
            ("Mass of swollen raisins = 25.0 g, Mass after placing in concentrated salt solution = 20.0 g. Calculate percentage mass loss by exosmosis", "20.0%", "\\(\\text{Loss} = \\frac{25.0 - 20.0}{25.0} \\times 100\\% = \\frac{5.0}{25.0} \\times 100\\% = 20.0\\%\\)", "10.0%, 25.0%, 5.0%"),
            ("A plant cell has Osmotic Pressure (OP) = 15 atm and Turgor Pressure (TP) = 10 atm. Calculate its Diffusion Pressure Deficit (DPD)", "5 atm", "\\(\\text{DPD} = \\text{OP} - \\text{TP} = 15 - 10 = 5\\text{ atm}\\)", "25 atm, 1.5 atm, 150 atm"),
            ("A plant cell has Osmotic Pressure (OP) = 12 atm and Turgor Pressure (TP) = 12 atm. Calculate its DPD and describe its physiological state", "0 atm (Fully Turgid cell)", "\\(\\text{DPD} = 12 - 12 = 0\\text{ atm}\\); when DPD = 0, the cell is fully turgid and absorbs no net water", "24 atm (Plasmolysed), 1 atm (Flaccid), 144 atm"),
            ("A plant cell has Solute Potential (\\(\\Psi_s\\)) = -800 kPa and Pressure Potential (\\(\\Psi_p\\)) = +500 kPa. Calculate its total Water Potential (\\(\\Psi_w\\))", "-300 kPa", "\\(\\Psi_w = \\Psi_s + \\Psi_p = -800 + 500 = -300\\text{ kPa}\\)", "-1300 kPa, +300 kPa, +1300 kPa"),
            ("Cell A (\\(\\Psi_w = -400\\text{ kPa}\\)) is in contact with Cell B (\\(\\Psi_w = -700\\text{ kPa}\\)). Determine the direction of net water flow", "From Cell A to Cell B", "Water flows spontaneously from higher (less negative: -400 kPa) to lower (more negative: -700 kPa) water potential", "From Cell B to Cell A, No water flow occurs, Water flows into Cell A from air")
        ],
        'templates': [
            "Calculate or solve the osmotic problem: '{0}':",
            "A laboratory practical question asks: '{0}'. The correct calculated answer is:",
            "Solve the quantitative water relations task: '{0}':",
            "From the experimental data: '{0}'. Determine the numerical outcome:",
            "Calculate the required parameter: '{0}':",
            "In plant water relation calculations: '{0}' yields:",
            "Determine the calculated result for: '{0}':",
            "Evaluate the osmotic parameter from: '{0}':",
            "A student measures osmotic values: '{0}'. The correct answer is:",
            "Solve the physiological measurement problem: '{0}':"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: State the relevant formula.**\n- **Percentage water absorption:** \\(\\frac{{\\text{{Swollen mass}} - \\text{{Dry mass}}}}{{\\text{{Dry mass}}}} \\times 100\\%\\).\n- **\\(\\text{{DPD}} = \\text{{OP}} - \\text{{TP}}\\).\n- **\\(\\Psi_w = \\Psi_s + \\Psi_p\\).\n- **Direction of flow:** From higher (less negative) to lower (more negative) \\(\\Psi_w\\).\n\n**Step 2: Substitute values.**\n{item[2]}.\n\n**Step 3: Result:** **{item[1]}**."
        ),
        'diff': 'medium'
    }

    # Arch 7: Physiological and Ecological Significance of Osmosis in Nature
    arch7 = {
        'data': [
            ("Root water uptake from soil by plant root hairs", "Soil water typically has higher water potential (more dilute) than root hair vacuolar sap, driving spontaneous endosmotic entry of water into root epidermal cells", "Forms the primary mechanism by which terrestrial plants absorb hundreds of litres of water daily", "Plants drink water using muscle contractions, Water is pumped into roots using gasoline, Roots absorb water only when soil is completely dry"),
            ("Halophytes (Salt-tolerant plants, e.g. Mangroves, Salicornia) osmotic adaptation", "Accumulate exceptionally high concentrations of compatible organic solutes (proline, glycine betaine) and inorganic ions in their vacuoles", "Maintains cellular water potential lower than the surrounding hypertonic seawater, enabling water absorption without undergoing plasmolysis", "Absorb salt until they turn into stone, Have no cell membranes, Expel all water into the ocean"),
            ("Osmoregulation in freshwater bony fish (e.g. Trout, Carp)", "Internal body fluids are hypertonic to surrounding freshwater; constantly gain water by endosmosis across gills and lose salts by diffusion", "Adaptation: do NOT drink water, actively absorb salts across gill chloride cells, and excrete large volumes of highly dilute urine", "Drink gallons of water constantly, Excrete concentrated solid salt urine, Have dead skin that blocks all water"),
            ("Osmoregulation in marine bony fish (e.g. Tuna, Cod)", "Internal body fluids are hypotonic to surrounding seawater; constantly lose water by exosmosis across gills", "Adaptation: drink copious seawater, actively secrete excess salts out across gill chloride cells, and excrete small volumes of concentrated urine", "Absorb water through skin, Never excrete urine, Freeze their gills to stop water loss"),
            ("Osmotic burst of bacteria in honey, jam, and dry grains", "High sugar concentration (low water potential) draws water out of bacterial cells by exosmosis, causing severe plasmolysis and inhibiting bacterial proliferation", "Explains why properly prepared honey and jams never spoil at room temperature without synthetic preservatives", "Honey contains high concentrations of bleach, Sugar freezes bacteria into glass, Bacteria cannot touch sweet food"),
            ("Why drinking seawater increases dehydration in humans", "Seawater has a salinity of ~3.5% (osmolarity ~1000 mOsm/L), far higher than human blood (~300 mOsm/L); kidneys can only concentrate urine up to ~1200 mOsm/L", "Excreting the ingested salt requires more water than was consumed, accelerating fatal systemic dehydration", "Seawater turns into solid stone in the stomach, Seawater destroys the heart directly, Salt causes the stomach to burst"),
            ("Guttation in herbaceous plants (e.g. Grasses, Tomato)", "Exudation of liquid water droplets from hydathodes at vein endings along leaf margins in early morning", "Driven by positive **Root Pressure** developed through active ion accumulation and endosmosis in roots when transpiration is zero at night", "Guttation is dew condensing from atmospheric clouds, Guttation is plant sweat caused by fever, Guttation occurs only when roots are dead"),
            ("Opening and closing of insect spiracles compared to plant stomata", "Both represent analogous convergent evolutionary solutions to balance gas exchange against desiccating transpirational water loss in terrestrial environments", "Regulated by environmental humidity and internal hydration status", "Insects have plant stomata on their wings, Plants have insect spiracles in their roots, Both are controlled by bone muscles"),
            ("Why freshwater protozoa (Amoeba) possess a contractile vacuole while marine protozoa lack one", "Freshwater Amoeba is hypertonic to its environment and constantly gains water by endosmosis, requiring a contractile vacuole to bail out excess water; marine protozoa are isotonic to seawater and face no net water influx", "Demonstrates cellular organelle adaptation to environmental osmotic gradients", "Marine protozoa have no cell membrane, Freshwater Amoeba drinks water for food, Contractile vacuoles only exist in plants"),
            ("Osmotic shock in laboratory cell lysis", "Suspending cells in pure distilled water causes massive rapid endosmosis, bursting cell membranes to isolate intracellular proteins, DNA, and organelles for biochemical analysis", "Standard gentle cell disruption technique widely used in molecular biology laboratories", "Boiling cells in oil, Crushing cells with hydraulic hammers, Freezing cells in liquid nitrogen to vaporize DNA")
        ],
        'templates': [
            "In ecological physiology and evolutionary osmoregulation: '{0}'. Identify the correct scientific fact:",
            "What physiological adaptation explains: '{0}'?:",
            "Regarding the natural significance of osmosis: '{0}' is characterized as:",
            "A biology student analyzes environmental water balance: '{0}'. The accurate concept is:",
            "Which statement correctly details: '{0}'?:",
            "Analyze the biological adaptation: '{0}' demonstrates that:",
            "What is the ecological and cellular reality of: '{0}'?:",
            "In comparative osmoregulation, '{0}' refers to:",
            "Why is '{0}' critical for survival in diverse aquatic and terrestrial habitats?:",
            "A question on environmental osmosis asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand ecological osmoregulation.**\n- **Freshwater organisms:** Hypertonic to medium \\(\\implies\\) water influx \\(\\implies\\) contractile vacuoles / dilute urine.\n- **Marine organisms:** Hypotonic to medium \\(\\implies\\) water loss \\(\\implies\\) drink seawater, excrete salt.\n- **Halophytes:** High vacuolar solutes prevent water loss.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'hard'
    }

    # Arch 8: Clinical and Biomedical Applications of Osmotic Principles
    arch8 = {
        'data': [
            ("Intravenous Rehydration Fluids (IV Drip) Tonicity Requirements", "Must be strictly isotonic with human blood plasma (e.g. 0.9% NaCl normal saline, 5% Dextrose in water, Ringer's Lactate)", "Prevents lethal osmotic hemolysis (bursting) or crenation (shriveling) of circulating red blood cells", "Must be pure distilled water, Must be concentrated 20% salt solution to kill viruses, Must be acidic vinegar"),
            ("Treatment of Cerebral Edema using Intravenous Mannitol", "Mannitol is a non-metabolizable, membrane-impermeable sugar alcohol infused into blood; increases plasma osmolarity (hypertonic blood)", "Draws excess fluid out of swollen brain tissue into the vascular compartment by exosmosis, reducing intracranial pressure and saving lives", "Dissolves the skull bone, Cools the brain by evaporating, Destroys all brain cells"),
            ("Osmotic Laxatives (e.g. Milk of Magnesia / Magnesium hydroxide, Polyethylene glycol)", "Poorly absorbed solutes that remain in the intestinal lumen, creating a hypertonic luminal environment that retains water by osmosis", "Softens stool and increases fecal volume, stimulating peristalsis to relieve constipation", "Paralyze the intestinal muscle, Absorb all water from the body causing dehydration, Digest food in the stomach"),
            ("Peritoneal Dialysis in Renal Kidney Failure", "Hypertonic sterile glucose dialysate fluid is infused into the patient's abdominal peritoneal cavity; the vascular peritoneal membrane acts as a natural semi-permeable filter", "Excess metabolic waste (urea, creatinine) and surplus water diffuse and osmose across into the dialysate, which is then drained after several hours", "Pumps blood through an artificial heart, Replaces the kidneys with plastic tubes inside veins, Uses laser beams to destroy urea"),
            ("Hemodialysis and Dialysis Fluid (Dialysate) Composition", "Dialysate is formulated to be isotonic with normal plasma electrolytes, containing physiological bicarbonate, potassium, and glucose, but ZERO urea or creatinine", "Urea and toxins diffuse rapidly out of blood down steep concentration gradients, while essential ions and water volume are balanced without red blood cell lysis", "Dialysate is pure distilled water that bursts all blood cells, Dialysate is concentrated acid that sterilizes blood, Dialysate contains no water"),
            ("Infantile Diarrhea and Oral Rehydration Salts (ORS) formulation", "WHO-formulated isotonic solution containing sodium chloride, glucose, potassium chloride, and trisodium citrate", "Exploits the intestinal \\(\\text{Na}^+\\)-glucose cotransporter (SGLT1): glucose absorption actively pulls \\(\\text{Na}^+\\) across mucosal cells, creating an osmotic gradient that rapidly draws water back into the body", "ORS is a medicine that kills all intestinal bacteria, ORS works by freezing the intestine, ORS stops diarrhea by forming a mechanical plug"),
            ("Gargling with Warm Salt Water for Sore Throat Relief", "Hypertonic warm saline draws fluid out of swollen, edematous pharyngeal mucosal tissues by exosmosis, reducing inflammation and pain", "Simultaneously exerts osmotic stress on bacterial cells on the throat surface, inhibiting microbial activity", "Salt water burns throat tissues to destroy nerves, Salt water permanently changes the voice, Salt water acts as a local anesthetic"),
            ("Eye Drops and Contact Lens Solution Tonicity", "Must be strictly formulated as sterile, buffered, isotonic solutions (~0.9% NaCl equivalent) matching the osmolarity of human tear film (~300 mOsm/L)", "Prevents corneal epithelial swelling (edema) or painful stinging and epithelial dehydration", "Must be hypertonic salt solution to dry the eyes, Formulated with pure alcohol, Must be acidic to clean contact lenses"),
            ("Hyponatremia (Water Intoxication) pathology", "Excessive intake of pure water without electrolyte replacement dilutes extracellular sodium concentration, making blood plasma dangerously hypotonic", "Water rushes into brain neurons by endosmosis, causing cerebral edema, brain herniation, seizures, coma, and death", "Causes brain cells to shrivel into raisins, Causes blood to boil in arteries, Has no physiological effect on humans"),
            ("Osmotic Diuresis in Uncontrolled Diabetes Mellitus (Polyuria)", "Excess blood glucose exceeds the renal threshold (~180 mg/dL) and spills into tubular urine; unreabsorbed glucose acts as an osmotic agent, retaining water in kidney tubules", "Prevents normal water reabsorption in collecting ducts, causing massive, frequent urination (polyuria) and severe thirst (polydipsia)", "Destroys kidney nephrons within 5 minutes, Turns urine into solid sugar crystals, Causes the bladder to burst")
        ],
        'templates': [
            "In clinical medicine and pharmacology: '{0}'. Identify the correct scientific fact:",
            "What physiological mechanism or clinical outcome is described by: '{0}'?:",
            "Regarding biomedical applications of osmosis: '{0}' is characterized by:",
            "A medical student analyzes fluid therapeutics: '{0}'. The accurate physiological fact is:",
            "Which statement correctly details the clinical principle of: '{0}'?:",
            "Analyze the medical application: '{0}' demonstrates that:",
            "What is the cellular and osmotic reality of: '{0}'?:",
            "In clinical pathophysiology, '{0}' refers to:",
            "Why is '{0}' critical in emergency medicine and renal therapeutics?:",
            "A question on biomedical osmosis asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand clinical applications of osmosis.**\n- **IV fluids & ORS:** Must match physiological osmolarity (~300 mOsm/L) to prevent hemolysis.\n- **Mannitol:** Hypertonic infusion draws fluid out of edematous brain.\n- **Dialysis:** Osmotic removal of excess fluid and diffusion of metabolic wastes.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-2-2.2.3", "Osmosis across semi-permeable membrane: endosmosis, exosmosis, plasmolysis", archs)


if __name__ == "__main__":
    q1 = gen_2_2_1()
    q2 = gen_2_2_2()
    q3 = gen_2_2_3()
    print(f"gen_2_2_1: {len(q1)} questions")
    print(f"gen_2_2_2: {len(q2)} questions")
    print(f"gen_2_2_3: {len(q3)} questions")
    print(f"Total Part 2 questions: {len(q1) + len(q2) + len(q3)}")
