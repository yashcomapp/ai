arch8_code = """
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
            ("Zonula Adherens (Belt desmosome) and E-Cadherin", "Continuous circumferential belt of transmembrane E-cadherin glycoproteins linking the cortical actin belts of adjacent epithelial cells (\\(\\text{Ca}^{2+}\\)-dependent)", "Loss of E-cadherin expression is the primary driver of Epithelial-Mesenchymal Transition (EMT) and cancer metastasis", "Junction passing electrical action potentials, Impermeable water barrier, Anchors intermediate filaments to bone"),
            ("Claudins and Occludins in Tight Junctions", "Four-transmembrane-domain proteins that polymerize into anastomosing intramembrane strands sealing the paracellular space", "Determines the electrical resistance and selective ion permeability ('pore' vs 'leak' pathways) across epithelial sheets", "Motor proteins powering ciliary movement, Enzymes that digest protein fibers, Structural proteins of the spindle"),
            ("Connexin-26 mutations in Congenital Deafness", "Mutations in GJB2 gene encoding connexin-26 (major gap junction protein in cochlear epithelial cells)", "Impairs potassium recycling in inner ear endolymph, causing the most common form of hereditary non-syndromic congenital sensorineural deafness", "Causes complete blindness, Leads to loss of skin pigmentation, Causes brittle bones"),
            ("Focal Adhesions (Integrin-Actin anchors)", "Dynamic cell-matrix junctions linking transmembrane integrins to intracellular actin microfilaments via talin, vinculin, and paxillin", "Crucial for epithelial cell migration during wound re-epithelialization and embryonic morphogenesis", "Static rivets that never disassemble, Water-impermeable seals, Sites of protein translation"),
            ("Basal infoldings and Mitochondria (Ion-transporting epithelia)", "Extensive invaginations of the basal plasma membrane interleaved with elongated vertical mitochondria", "Provides immense surface area and local ATP for \\(\\text{Na}^+/\\text{K}^+\\) ATPase pumps in fluid-transporting epithelia (renal DCT, salivary striated ducts)", "Structures that secrete mucus, Storage vacuoles for lipids, Ciliated projections sweeping fluid"),
            ("Terminal Web in columnar enterocytes", "Dense horizontal filamentous meshwork of actin, spectrin, and myosin directly beneath the apical microvilli", "Provides mechanical scaffolding anchoring the rootlets of microvillar actin cores and stabilizing the apical cell pole", "Meshwork enclosing the cell nucleus, Dense bone ring, Thick layer of dead keratin"),
            ("Transepithelial Electrical Resistance (TEER)", "Electrophysiological measurement of electrical resistance across an intact epithelial monolayer, reflecting the tight junction seal integrity", "Tight epithelia (urinary bladder) display TEER \\(> 2,000\\text{ }\Omega\\cdot\\text{cm}^2\\); leaky epithelia (renal PCT) display TEER \\(< 30\\text{ }\Omega\\cdot\\text{cm}^2\\)", "Measures the rate of cellular mitosis, Quantifies the number of cilia, Measures cellular DNA content")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Intercellular Junctions & Basal Specializations.**\\n- Hemidesmosomes: \\(\\alpha_6\\beta_4\\) integrin anchors keratin to basement membrane (Bullous pemphigoid = anti-BP180/BP230).\\n- Stereocilia: Giant actin microvilli, non-motile (epididymis absorption & inner ear mechanoreceptors).\\n- E-Cadherin: Zonula adherens (\\(\\text{Ca}^{2+}\\)-dependent, loss triggers EMT metastasis).\\n- Connexin-26: Gap junctions in cochlea (mutation \\(\\rightarrow\\) congenital deafness).\\n\\n**Step 2: Evaluate '" + item[0] + "'.**\\n" + item[1] + ".\\n\\n**Step 3: Ultrastructural / Clinical Significance:**\\n" + item[2] + "."
        ),
        'diff': 'hard'
    }
"""

with open('scripts/build_cbse9_scie_ch3_part3.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Insert arch8_code right before line archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8] in gen_3_3_1
target = "    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]\n    return generate_vault_questions(\"CBSE-9-SCIE-3-3.3.1\", \"Epithelial tissues: Squamous, cuboidal, columnar, ciliated\", archs)"
replacement = arch8_code + "\n" + target

text = text.replace(target, replacement)

with open('scripts/build_cbse9_scie_ch3_part3.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Inserted arch8 into gen_3_3_1 successfully!")
