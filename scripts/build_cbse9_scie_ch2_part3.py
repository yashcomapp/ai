import json
import re

def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        "Uncontrolled metabolic collapse",
        "Non-chromosomal ribonucleic inclusion",
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
                "chapterNumber": 2,
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
# 2.3.1: Nuclear envelope, nucleolus, chromatin and DNA genes
# ==========================================
def gen_2_3_1():
    # Arch 1: Structure and roles of Nuclear Envelope and Nuclear Pores
    arch1 = {
        'templates': [
            "What is the structural composition and functional role of: '{0}'?:",
            "In eukaryotic cytology, what defines: '{0}'?:",
            "Consider the nuclear membrane architecture: '{0}' is characterized by:",
            "Which statement precisely describes the significance of: '{0}'?:",
            "Identify the accurate cytological fact regarding: '{0}':",
            "In the mammalian nucleus, '{0}' functions primarily to:",
            "A cell biologist investigates nuclear transport: '{0}'. What is true?:",
            "Evaluate the structural feature: '{0}'. Its key functional attribute is:",
            "How does the eukaryotic nucleus utilize '{0}' to regulate cellular activity?:",
            "What critical function distinguishes '{0}' during gene expression and transport?:"
        ],
        'data': [
            ("Nuclear envelope double membrane", "Two concentric lipid bilayer membranes separated by a perinuclear space of \\(10\\text{ to }50\\text{ nm}\\)", "The outer membrane is continuous with the rough endoplasmic reticulum and studded with ribosomes", "A single continuous lipid monolayer with no lumen, A triple-layered protein shell without lipids, A semi-solid carbohydrate wall"),
            ("Nuclear pores (Nuclear Pore Complexes)", "Aqueous channels that selectively regulate bidirectional macromolecular transport between nucleoplasm and cytoplasm", "Allows passive diffusion of small water-soluble molecules and active signal-mediated transport of proteins (importins/exportins) and RNAs", "Impermeable barriers preventing all molecular exit, Holes formed by spontaneous lipid rupture, Permanent open gaps devoid of protein regulation"),
            ("Perinuclear space", "A fluid-filled lumen of \\(10\\text{ to }50\\text{ nm}\\) separating inner and outer nuclear membranes", "Continuous with the lumen of the rough endoplasmic reticulum", "A \\(500\\text{ nm}\\) vacuum gap between membranes, Intranuclear zone holding dense chromatin, Cytoplasmic space separating mitochondria"),
            ("Nuclear lamina", "Dense fibrous protein meshwork underlying the inner nuclear membrane composed of lamins", "Provides mechanical support to the nuclear envelope and anchors chromatin fibers", "A lipid bilayer lining the nucleolus, A carbohydrate coat on the outer membrane, A microtubule spindle array inside mitochondria"),
            ("Outer nuclear membrane ribosomes", "Site of translation for cytoplasmic and secretable proteins continuous with the RER", "Engaged in active protein synthesis facing the cytoplasmic side", "Site of ribosomal RNA assembly, Enzymes that degrade chromatin, Storage vesicles for calcium ions"),
            ("Nuclear transport signals (NLS)", "Specific peptide sequences that target proteins synthesized in cytoplasm for import through nuclear pores", "Recognized by importin receptors to mediate active translocation", "Carbohydrate tags for lysosomal delivery, Signal peptides targeting proteins into chloroplasts, Stop codons on mRNA strands"),
            ("Nucleoplasm (nuclear sap)", "Viscous, colloidal ground substance enclosed by nuclear envelope containing chromatin and nucleolus", "Provides aqueous medium rich in nucleotides, enzymes (DNA/RNA polymerases), and mineral ions for transcription and replication", "Lipid emulsion devoid of enzymes, Pure water reservoir maintaining turgidity, Dense crystalline matrix preventing enzyme diffusion"),
            ("Outer membrane continuity with RER", "Direct physical connection between outer nuclear membrane and the cisternae of rough ER", "Allows shared luminal environment and direct vesicle trafficking between nucleus and endomembrane system", "Separated by rigid peptidoglycan layer, Connected only during telophase of mitosis, Artifact caused by chemical fixation"),
            ("Nuclear envelope breakdown in open mitosis", "Phosphorylation of nuclear lamins leading to reversible envelope disassembly during prophase", "Allows the mitotic spindle to capture condensed metaphase chromosomes", "Irreversible apoptosis destroying genetic material, Permanent fusion with plasma membrane, Enzymatic digestion into free fatty acids"),
            ("Nuclear envelope reformation in telophase", "Dephosphorylation of lamins and vesicle fusion around separated daughter chromosome sets", "Re-establishes nuclear compartmentalization and distinct nucleoplasm", "Synthesis of an entirely new membrane from peroxisomes, Endocytosis of extracellular vesicles, Direct cleavage of mitochondrial outer membrane")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Nuclear Envelope Organization.**\n- The nuclear envelope is a double-membrane barrier enclosing the eukaryotic genome.\n- Consists of outer membrane (continuous with RER), perinuclear space (\\(10\\text{{--}}50\\text{{ nm}}\\)), inner membrane, and nuclear pore complexes (NPCs).\n\n**Step 2: Analyze '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Functional Significance:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 2: Nucleolus structure, ribosome biogenesis, and rRNA synthesis
    arch2 = {
        'templates': [
            "What is the exact function and structural nature of: '{0}'?:",
            "In cytogenetics and cell biology, '{0}' is recognized as:",
            "Consider the nucleolar sub-compartments: '{0}' is characterized by:",
            "Which statement accurately explains the biology of: '{0}'?:",
            "A student observes a eukaryotic nucleus under electron microscopy: '{0}'. What is correct?:",
            "Identify the primary role and biochemical process associated with: '{0}':",
            "Why is '{0}' indispensable for protein synthesis and cellular metabolism?:",
            "What happens with respect to: '{0}' during cell division?:",
            "Which description best characterizes: '{0}'?:",
            "Evaluate the cytological statement regarding: '{0}':"
        ],
        'data': [
            ("Nucleolus (plural: nucleoli)", "A non-membrane bound dense nuclear sub-domain dedicated to rRNA transcription and ribosome subunit assembly", "First observed by Felice Fontana (1781); dynamic structure formed around Nucleolar Organizer Regions (NORs)", "A membrane-enclosed vesicle storing ATP, A DNA-free protein crystal, The site of lipid synthesis in the nucleus"),
            ("Nucleolar Organizer Regions (NORs)", "Chromosomal chromosomal loops containing tandem arrays of ribosomal RNA (rRNA) genes", "In humans, located on the short arms of acrocentric chromosomes 13, 14, 15, 21, and 22", "Centromeric heterochromatin devoid of genes, Telomeric caps preventing degradation, Non-transcribed mitochondrial circular plasmids"),
            ("Fibrillar center (FC) of nucleolus", "Pale-staining nucleolar zone containing inactive or low-level transcribing rRNA genes and RNA polymerase I", "Acts as the storage pool for transcriptionally competent rDNA units", "Dense site of mature ribosome export, The site of lipid vesicle storage, Membrane border of the nucleolus"),
            ("Dense fibrillar component (DFC)", "Region rich in nascent pre-rRNA transcripts actively processed by snoRNPs and fibrillarin", "Site of early cleavage, methylation, and pseudouridylation of 45S pre-rRNA", "Site of translation of tubulin proteins, Lipid storage compartment, Outer nuclear membrane boundary"),
            ("Granular component (GC)", "Periphery of nucleolus containing assembling ribosomal subunits (preribosomal particles)", "Site of late assembly where processed rRNAs associate with imported ribosomal proteins", "Zone containing fully translated active enzymes, Site of spindle fiber anchorage, Heterochromatin perimeter"),
            ("Ribosomal subunit export", "Small (40S) and large (60S) pre-ribosomal subunits are exported separately via nuclear pores to the cytoplasm", "Prevents premature translation of cytoplasmic mRNAs within the nucleoplasm", "Subunits assemble into 80S inside nucleus before export, Entire ribosomes diffuse freely through lipid bilayer, Subunits pass via gap junctions"),
            ("Disappearance and reformation of nucleolus", "Disassembles during prophase as transcription ceases and reforms in telophase at NOR sites", "Correlates with chromosome condensation and cessation of ribosomal RNA gene transcription", "Permanently expelled into cytoplasm, Engulfed and digested by lysosomes, Merged with centrioles during metaphase"),
            ("Multiple nucleoli in active cells", "Highly active protein-synthesizing cells (e.g., plasma cells, oocytes, cancer cells) contain enlarged or multiple nucleoli", "Reflects tremendous demand for new ribosomes to support rapid polypeptide synthesis", "Indicates imminent cell death or necrosis, Signifies viral genome integration, Diagnostic of bacterial infection"),
            ("RNA Polymerase I function", "Transcribes the major ribosomal precursor transcript (45S pre-rRNA) within the nucleolus", "Exclusively localized within nucleoli to transcribe 18S, 5.8S, and 28S rRNAs", "Transcribes all protein-coding mRNAs, Synthesizes transfer RNAs (tRNAs), Replicates mitochondrial circular DNA"),
            ("Small nucleolar RNAs (snoRNAs)", "Non-coding guide RNAs that direct site-specific base methylation and pseudouridylation of pre-rRNA", "Form snoRNPs essential for proper folding and maturation of ribosomal RNAs", "Messenger RNAs encoding histone proteins, Primers for nuclear DNA replication, MicroRNAs that degrade oncogenes")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Nucleolus Function & Organization.**\n- The nucleolus is a prominent, non-membrane bound nuclear factory.\n- Responsible for transcription of rRNA, processing of pre-rRNA, and assembly of ribosomal subunits.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Mechanistic Details:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Chromatin, Histones, Nucleosomes, and Chromosome Packaging
    arch3 = {
        'templates': [
            "What defines the hierarchical packaging structure of: '{0}'?:",
            "In molecular genetics and chromatin biology, '{0}' refers to:",
            "How does the eukaryotic cell organize: '{0}'?:",
            "Which statement accurately explains the structural organization of: '{0}'?:",
            "Consider the nucleosomal architecture: '{0}' is characterized by:",
            "What is the functional difference or property of: '{0}'?:",
            "A cytogeneticist examines chromosome compaction: '{0}'. The correct fact is:",
            "Evaluate the biochemical composition of: '{0}':",
            "Why is '{0}' vital for regulating gene transcription and replication?:",
            "Which description best summarizes: '{0}'?:"
        ],
        'data': [
            ("Chromatin", "Complex of genomic DNA (\\(\\approx 35\\%\\)), basic histone proteins (\\(\\approx 35\\%\\)), non-histone proteins, and RNA", "Term coined by Walther Flemming (1879) due to its strong affinity for basic biological stains (e.g., acetocarmine)", "Pure double-stranded DNA without proteins, Dense lipid-protein emulsion, Structural fibrous protein of the spindle"),
            ("Euchromatin", "Lightly stained, loosely condensed, transcriptionally active chromatin accessible to RNA polymerase", "Replicates early in S-phase and contains majority of actively expressed genes", "Darkly stained permanently silenced centromeric DNA, Non-functional junk RNA fibers, Telomeric protein caps"),
            ("Heterochromatin", "Darkly stained, densely packed, transcriptionally inactive chromatin inaccessible to transcription factors", "Replicates late in S-phase; divided into constitutive (always silent) and facultative heterochromatin", "Loosely packed gene-rich active euchromatin, Free uncoiled naked DNA plasmid, Translating polyribosome chains"),
            ("Nucleosome core particle", "An octamer of core histone proteins wrapped by \\(146\\text{ to }147\\text{ bp}\\) of DNA in \\(1.65\\) superhelical turns", "Fundamental repeating unit of chromatin packaging (11 nm 'beads-on-a-string' fiber)", "A tetramer of non-histone enzymes binding 50 bp, A hexamer of DNA polymerases, A single histone H1 monomer with 500 bp DNA"),
            ("Histone octamer composition", "Consists of two copies each of core histones H2A, H2B, H3, and H4", "Forms a positively charged protein spool due to high content of basic lysine and arginine residues", "One copy each of H1, H2, H3, H4, Two copies each of H1 and H2 only, Acidic protein complex rich in glutamate and aspartate"),
            ("Histone H1 (linker histone)", "Binds to the linker DNA at entry/exit sites of the nucleosome to seal the coil and promote 30 nm fiber folding", "Facilitates higher-order compaction from 11 nm fiber to 30 nm solenoid/zigzag structure", "Core component inside the nucleosome octamer, Enzyme that cuts DNA during replication, RNA-binding transcription factor"),
            ("Linker DNA", "Stretch of free DNA (\\(20\\text{ to }80\\text{ bp}\\)) connecting adjacent nucleosome core particles", "Associated with histone H1 and susceptible to micrococcal nuclease digestion", "Tightly bound 146 bp inside histone core, Circular DNA found in plasmids, Non-coding mitochondrial DNA loop"),
            ("Chromosome condensation during M-phase", "Chromatin fibers condense \\(\\approx 10,000\\text{-fold}\\) into visible rod-shaped chromosomes using condensins and topoisomerases", "Ensures error-free segregation of sister chromatids without entangling during anaphase", "DNA is uncoiled completely into single strands, Nucleosomes dissociate permanently into lysosomes, Chromatin is hydrolyzed into free nucleotides"),
            ("Facultative heterochromatin (e.g., Barr body)", "Chromatin regions that can alternate between condensed inactive and euchromatic active states", "In mammalian females, one X chromosome is randomly inactivated into a condensed Barr body", "Permanently silenced repetitive centromeric satellite DNA, Active rRNA genes in the nucleolus, Non-functional mitochondrial plasmid DNA"),
            ("Constitutive heterochromatin", "Permanently condensed, highly repetitive DNA sequences located predominantly at centromeres and telomeres", "Remains genetically silent across all developmental stages and cell types", "Transcriptionally hyperactive protein-coding genes, Loosely packed euchromatic regulatory promoters, Mobile ribosomal subunit arrays")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Chromatin Packaging & Organization.**\n- Eukaryotic DNA (\\(\\approx 2\\text{{ meters}}\\) in a human cell) must be compacted into a \\(\\approx 6\\text{{ }}\\mu\\text{{m}}\\) nucleus.\n- Packaging hierarchy: Naked DNA (2 nm) \\(\\rightarrow\\) Nucleosomes (11 nm 'beads-on-a-string') \\(\\rightarrow\\) Solenoid (30 nm) \\(\\rightarrow\\) Loops & Scaffolding (300 nm) \\(\\rightarrow\\) Metaphase Chromosome (1400 nm).\n\n**Step 2: Analyze '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Structural/Functional Details:**\n{item[2]}."
        ),
        'diff': 'hard'
    }

    # Arch 4: DNA, Genes, Chromosomes, and Molecular Genetics Concepts
    arch4 = {
        'templates': [
            "What is the functional definition and relationship of: '{0}'?:",
            "In Mendelian and molecular genetics, what is: '{0}'?:",
            "Consider genetic material organization: '{0}' is defined as:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "How does modern cell biology define: '{0}'?:",
            "A biology student analyzes chromosome architecture: '{0}'. What is true?:",
            "Identify the accurate molecular property of: '{0}':",
            "What distinguishes '{0}' in eukaryotic cellular inheritance?:",
            "Which description correctly specifies: '{0}'?:",
            "Evaluate the cytogenetic concept: '{0}':"
        ],
        'data': [
            ("Gene", "A functional segment of DNA that contains the nucleotide sequence encoding a functional protein or RNA molecule", "Functional unit of inheritance occupying a specific physical locus on a chromosome", "An entire intact chromosome, A free-floating nucleotide in the cytoplasm, A carbohydrate tag on the cell membrane"),
            ("DNA (Deoxyribonucleic Acid)", "Double-helical polymer of deoxyribonucleotides carrying the genetic blueprint of the organism", "Composed of two antiparallel polynucleotide chains held by hydrogen bonds between complementary base pairs (A=T, G≡C)", "Single-stranded polyamino acid chain, Phospholipid bilayer storing chemical energy, Protein polymer synthesized in nucleolus"),
            ("Chromosome", "Deeply staining rod-like nucleoprotein structure formed by extreme compaction of chromatin during cell division", "Humans possess 46 chromosomes (23 pairs: 22 pairs of autosomes and 1 pair of allosomes/sex chromosomes)", "A small spherical vesicle storing digestive enzymes, A cytoplasmic microfilament bundle, An extranuclear circular plasmid"),
            ("Sister chromatids", "Two identical copies of a replicated chromosome joined together at a single common centromere", "Formed during S-phase DNA replication and separated into individual chromosomes during anaphase", "Non-homologous chromosomes from different parents, Unrelated chromatin strands from different cells, Fragments of broken nuclear membrane"),
            ("Centromere (Primary constriction)", "Specialized constricted region of chromosome holding sister chromatids and assembling kinetochores", "Essential for spindle microtubule attachment and proper chromosome movement during cell division", "The terminal end of chromosome preventing end-joining, The active transcription site encoding rRNA, The protein complex that unwinds DNA double helix"),
            ("Kinetochore", "Trilaminar protein disc assembled on centromeric DNA that binds spindle fiber microtubules", "Generates and monitors pulling forces required to segregate sister chromatids during anaphase", "Enzyme complex that replicates telomeres, Membrane pore regulating nuclear import, Organelle producing ATP"),
            ("Telomeres", "Specialized repetitive nucleoprotein structures capping the ends of linear eukaryotic chromosomes", "Protect chromosome ends from degradation, fusion, and inappropriate DNA damage responses", "Sites where spindle fibers attach during metaphase, Genes encoding core ribosomal RNAs, Internal constrictions separating arms"),
            ("Ploidy (Haploid vs Diploid)", "Haploid (n) has one complete set of chromosomes (gametes); Diploid (2n) has two sets (somatic cells)", "In humans, haploid gametes have \\(n = 23\\) and diploid somatic cells have \\(2n = 46\\)", "Haploid has 4 sets while diploid has 1 set, Ploidy refers to the number of nucleoli per cell, Diploid refers only to bacterial nucleoids"),
            ("Karyotype", "The complete visual profile and organized display of metaphase chromosomes arranged by size, centromere position, and banding pattern", "Used clinically to diagnose chromosomal numerical abnormalities (e.g., Down syndrome 47,+21) and structural defects", "Total protein content of a cell, Microscopic snapshot of cellular organelles, DNA sequencing chromatogram"),
            ("Autosomes vs Sex chromosomes (Allosomes)", "Autosomes are chromosomes non-related to sex determination (22 pairs in humans); Allosomes determine biological sex (XX/XY)", "Autosomes govern general morphological and physiological somatic traits", "Autosomes are found only in bacteria, Allosomes are non-coding mitochondrial loops, Autosomes lack histone proteins")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Genetic Terminology & Concepts.**\n- DNA \\(\\rightarrow\\) Functional segments are Genes.\n- Chromatin \\(\\rightarrow\\) Highly condensed into Chromosomes during M-phase.\n- Somatic cells are diploid (\\(2n = 46\\)), gametes are haploid (\\(n = 23\\)).\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Details & Context:**\n{item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 5: Numerical & Quantitative Problems on Chromosomes, DNA Length, and Cell Ploidy
    arch5 = {
        'templates': [
            "{0}:",
            "Calculate the genomic parameter: {0}:",
            "A cytogenetics laboratory problem: {0}:",
            "Quantitative cytology question: {0}:",
            "Solve the genetics calculation: {0}:",
            "Analyze the numerical chromosome problem: {0}:",
            "Determine the correct numeric result: {0}:",
            "An analytical cytology calculation: {0}:",
            "Find the accurate quantity for: {0}:",
            "Compute the following cellular metric: {0}:"
        ],
        'data': [
            ("A human somatic cell contains \\(6.6 \\times 10^9\\text{ bp}\\) of DNA in diploid state. Given distance between adjacent base pairs is \\(0.34\\text{ nm}\\), what is the total length of DNA in one cell?", "\\(2.24\\text{ meters}\\)", "\\(\\text{Length} = 6.6 \\times 10^9 \\times 0.34 \\times 10^{-9}\\text{ m} = 2.244\\text{ m} \\approx 2.24\\text{ m}\\)", "\\(0.22\\text{ m}, 22.4\\text{ m}, 2.24\\text{ mm}\\)"),
            ("If a diploid organism has \\(2n = 16\\) chromosomes, how many chromatids are present in a single cell during mitotic metaphase?", "32 chromatids", "Each of the 16 chromosomes has replicated in S-phase, possessing 2 sister chromatids: \\(16 \\times 2 = 32\\)", "16 chromatids, 64 chromatids, 8 chromatids"),
            ("In an organism with \\(2n = 24\\) chromosomes, how many chromosomes and chromatids are present in anaphase of mitosis?", "48 chromosomes and 48 single-stranded chromatids", "During anaphase, centromeres split; sister chromatids separate and are now individual daughter chromosomes: \\(24 \\times 2 = 48\\)", "24 chromosomes and 48 chromatids, 12 chromosomes and 24 chromatids, 24 chromosomes and 24 chromatids"),
            ("How many nucleosomes are formed by a stretch of double-stranded DNA comprising \\(40,000\\text{ bp}\\), assuming standard \\(200\\text{ bp}\\) of DNA per nucleosome (core + linker)?", "200 nucleosomes", "\\(\\text{Number of nucleosomes} = 40,000 / 200 = 200\\)", "400 nucleosomes, 100 nucleosomes, 2,000 nucleosomes"),
            ("How many histone protein molecules are required to assemble 50 complete nucleosome units (including linker histone H1)?", "450 histone molecules", "Each nucleosome has an octamer (8 core histones) + 1 linker histone H1 = 9 histones. For 50 nucleosomes: \\(50 \\times 9 = 450\\)", "400 histone molecules, 500 histone molecules, 350 histone molecules"),
            ("A haploid gamete of an angiosperm plant contains \\(n = 12\\) chromosomes and \\(2.5\\text{ pg}\\) of DNA. What will be the chromosome number and DNA content of a root tip cell in G2 phase?", "24 chromosomes and 10.0 pg DNA", "Root tip is diploid somatic (\\(2n = 24\\)). G1 has \\(2 \\times 2.5 = 5.0\\text{ pg}\\). In G2 after S-phase replication, DNA doubles to \\(10.0\\text{ pg}\\), while chromosome number remains 24", "24 chromosomes and 5.0 pg DNA, 48 chromosomes and 10.0 pg DNA, 12 chromosomes and 5.0 pg DNA"),
            ("If a segment of B-DNA has 30 complete helical turns, how many base pairs and what is its length (pitch \\(= 3.4\\text{ nm}\\), 10 bp/turn)?", "300 bp and 102 nm", "Base pairs \\(= 30 \\times 10 = 300\\text{ bp}\\). Length \\(= 30 \\times 3.4\\text{ nm} = 102\\text{ nm}\\)", "300 bp and 34 nm, 600 bp and 204 nm, 150 bp and 51 nm"),
            ("How many DNA molecules (double helices) are present in a human somatic cell at G1 phase versus metaphase of mitosis?", "46 in G1 and 92 in metaphase", "In G1, 46 unreplicated chromosomes = 46 DNA molecules. In metaphase, 46 duplicated chromosomes with 2 sister chromatids each = 92 DNA molecules", "46 in G1 and 46 in metaphase, 23 in G1 and 46 in metaphase, 92 in G1 and 184 in metaphase"),
            ("How many hydrogen bonds are present in a \\(100\\text{ bp}\\) DNA duplex containing 40 Adenine bases?", "260 hydrogen bonds", "A = 40 implies T = 40 (\\(40 \\times 2 = 80\\text{ H-bonds}\\)). G + C = \\(200 - 80 = 120\\text{ bases}\\), so G = 60, C = 60 (\\(60 \\times 3 = 180\\text{ H-bonds}\\)). Total \\(= 80 + 180 = 260\\)", "240 hydrogen bonds, 300 hydrogen bonds, 200 hydrogen bonds"),
            ("If a double-stranded DNA sample has \\(28\\%\\) Cytosine, what is the expected percentage of Adenine according to Chargaff's rules?", "\\(22\\%\\)", "C = \\(28\\%\\) \\(\\implies\\) G = \\(28\\%\\). G + C = \\(56\\%\\). A + T = \\(100 - 56 = 44\\%\\). Since A = T, \\(A = 44 / 2 = 22\\%\\)", "\\(28\\%\\), \\(32\\%\\), \\(44\\%\\)")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Identify given biological quantities.**\n{item[0]}\n\n**Step 2: Apply the governing formula/principle.**\n{item[2]}.\n\n**Step 3: Conclude.**\nResult is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Experimental Techniques in Nuclear & Chromatin Biology
    arch6 = {
        'templates': [
            "Which staining or microscopy protocol is correctly matched with: '{0}'?:",
            "In laboratory cytological investigation: '{0}' is identified using:",
            "What experimental methodology is employed to analyze: '{0}'?:",
            "How did researchers experimentally demonstrate: '{0}'?:",
            "A student performs a laboratory smear of onion root tip cells: '{0}'. What is observed?:",
            "Which biochemical test or stain demonstrates: '{0}'?:",
            "In cell biology research, '{0}' is visualized or analyzed by:",
            "What laboratory observation confirms: '{0}'?:",
            "Evaluate the scientific protocol used for: '{0}':",
            "Identify the standard histological stain utilized for: '{0}':"
        ],
        'data': [
            ("Acetocarmine / Feulgen staining of chromatin", "Basic nuclear dyes that selectively bind to negatively charged phosphate backbones of DNA, rendering chromosomes magenta/pink", "Feulgen reaction is specific for deoxyribose sugar of DNA via Schiff reagent", "Acidic dye binding exclusively to basic lipids, Fluorophore binding only to ribosomal RNA, Silver salt precipitating cell wall cellulose"),
            ("Methylene blue staining of human cheek cells", "Stains the nucleus deep blue while cytoplasm stains light blue", "Due to high density of acidic nucleic acids in the nucleus binding cationic dye molecules", "Stains only the dead lipid bilayer, Reacts with starch granules, Completely decolorizes nucleic acids"),
            ("Hammerling's Acetabularia grafting experiments", "Proved that the nucleus contains genetic instructions and controls cellular morphology and regeneration", "Grafted stalk and rhizoid (containing nucleus) of A. mediterranea and A. crenulata; cap shape was determined by the rhizoid's nucleus", "Proved that chloroplasts can synthesize proteins independently, Demonstrated that cell wall determines cell shape, Showed cytoplasm alone controls heredity"),
            ("Gurdon's nuclear transplantation experiments (1958)", "Proved nuclear totipotency by transplanting a somatic intestinal cell nucleus into an enucleated Xenopus egg to develop a normal tadpole", "Demonstrated that differentiated somatic nuclei retain the complete, intact genome", "Showed that genes are discarded during differentiation, Proved that mitochondrial DNA controls embryogenesis, Proved that proteins carry genetic code"),
            ("Differential centrifugation for nuclear isolation", "Pelleted at lowest centrifugal force (\\(\\approx 600\\text{ to }1,000 \\times g\\) for 10 min) because nuclei are the largest, densest cellular organelles", "Separates unbroken nuclei cleanly from mitochondria, lysosomes, and microsomes", "Requires \\(100,000 \\times g\\) ultracentrifugation for 4 hours, Pelleted along with free ribosomes, Floats on top due to low buoyant density"),
            ("Fluorescence in situ hybridization (FISH)", "Uses fluorescently labeled single-stranded DNA probes to locate specific gene sequences on intact metaphase chromosomes", "Used clinically to detect microdeletions, gene amplifications (e.g., HER2), and chromosomal translocations", "Measures cellular ATP production, Stains endoplasmic reticulum membranes, Quantifies protein secretion rates"),
            ("Micrococcal nuclease (MNase) digestion", "Digests naked linker DNA between nucleosomes, yielding ladder fragments in multiples of \\(\\approx 200\\text{ bp}\\)", "Conclusive experimental proof of the repeating 'beads-on-a-string' nucleosome model", "Cleaves core histones without cutting DNA, Randomly hydrolyzes RNA only, Degrades nuclear envelope lipids"),
            ("Autoradiography with tritiated thymidine (3H-thymidine)", "Taylor, Woods, and Hughes used 3H-thymidine in Vicia faba root tips to prove semiconservative replication of chromosomes", "Selectively incorporated into replicating DNA during S-phase, exposing photographic emulsion", "Incorporates into synthesized proteins, Stains cell wall pectin, Labels newly synthesized rRNA in nucleolus"),
            ("Transmission Electron Microscopy (TEM) of nuclear pore", "Reveals an 8-fold rotational symmetry (octagonal ring) spanning both nuclear membranes with a central plug/transporter", "Resolves fine structural details at sub-nanometer resolution impossible with light microscopy", "Shows pore is an open unregulated hole, Shows nuclear envelope is a single continuous protein sheet, Visualizes individual ATP molecules"),
            ("DAPI (4',6-diamidino-2-phenylindole) staining", "Fluorescent stain that binds strongly to A-T rich regions in DNA, emitting bright blue fluorescence under UV excitation", "Standard cytological tool for nuclear visualization and cell cycle DNA content profiling via flow cytometry", "Binds specifically to plasma membrane cholesterol, Emits green light when binding glycogen, Red dye for acidic lysosomes")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Cytological & Molecular Techniques.**\n- Staining and visualization of nuclear components depend on nucleic acid chemistry (negative phosphate charges, basic dye affinity).\n- Historic experiments (Hammerling, Gurdon) established the nucleus as the seat of cellular control.\n\n**Step 2: Analyze '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Laboratory Significance:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Cell Cycle & Nuclear Dynamics (Mitosis vs Interphase Nucleus)
    arch7 = {
        'templates': [
            "What nuclear change characterizes: '{0}'?:",
            "In the context of the cell cycle: '{0}' is marked by:",
            "During eukaryotic cell division, how does the nucleus undergo: '{0}'?:",
            "Which description precisely captures: '{0}'?:",
            "What cytological event occurs during: '{0}'?:",
            "A student observes a dividing cell: '{0}'. What is taking place?:",
            "Identify the essential event occurring during: '{0}':",
            "Why is '{0}' critical for equal distribution of hereditary material?:",
            "What structural transformation defines: '{0}'?:",
            "Evaluate the cell cycle phase: '{0}':"
        ],
        'data': [
            ("Interphase nucleus (G1, S, G2 phases)", "High metabolic and transcriptional activity; chromatin is decondensed; gene transcription and DNA replication take place", "Nucleus is bounded by an intact envelope with visible nucleoli and active nucleocytoplasmic transport", "Chromosomes are maximally condensed and non-transcribing, Nuclear membrane is completely absent, Cell has stopped all protein synthesis"),
            ("S-phase (Synthesis phase)", "Accurate duplication of nuclear genomic DNA and replication of centrioles in the cytoplasm", "DNA content doubles from 2C to 4C, while chromosome number remains constant (2n)", "Chromosome number doubles from 2n to 4n, Nuclear envelope breaks down, Ribosomes are degraded"),
            ("Prophase nuclear events", "Chromatin condenses into visible distinct chromosomes; nucleolus gradually disappears; nuclear envelope breaks down at late prophase", "Facilitated by phosphorylation of nuclear lamins and condensin activation", "DNA replicates into four copies, Daughter nuclei reform around chromosomes, Cytokinesis occurs"),
            ("Metaphase alignment", "Chromosomes reach maximum condensation and align individually at the equatorial metaphase plate", "Kinetochores of sister chromatids attach to opposite spindle poles via kinetochore microtubules", "Nuclear envelope reforms around each chromosome, Chromatin decondenses into euchromatin, Nucleolus synthesizes ribosomes rapidly"),
            ("Anaphase sister chromatid disjunction", "Synchronous splitting of centromeres and poleward migration of sister chromatids (now daughter chromosomes)", "Ensures that both future daughter cells receive an exact identical copy of the genome", "Chromatin replicates again, Nuclear membrane reforms before movement, Homologous chromosomes pair up as bivalents"),
            ("Telophase nuclear reformation", "Daughter chromosomes decondense back into chromatin; nuclear envelopes reassemble around each daughter set; nucleoli reappear", "Marks the completion of karyokinesis before cytokinesis divides the cytoplasm", "Spindle fibers contract to pull chromosomes out of cell, Cell wall completely dissolves, Chromosomes condense further"),
            ("Karyokinesis vs Cytokinesis", "Karyokinesis is division of the nucleus; Cytokinesis is the subsequent division of cytoplasm into two daughter cells", "In plant cells, cytokinesis occurs by cell plate formation; in animal cells, by cleavage furrowing", "Karyokinesis occurs in cytoplasm while cytokinesis occurs inside nucleus, Both terms refer to DNA replication, Karyokinesis is destruction of nucleus during apoptosis"),
            ("Syncytium / Coenocyte formation", "Occurs when multiple nuclear divisions (karyokinesis) proceed without cytokinesis (e.g., liquid endosperm of coconut)", "Results in a multinucleated cell containing thousands of free nuclei in shared cytoplasm", "Single cell with zero nuclei, Complete failure of DNA replication, Formed by fusion of lysosomal vesicles"),
            ("G0 phase (Quiescent stage)", "Metabolically active state where cells exit the cell cycle without dividing (e.g., mature neurons and cardiac myocytes)", "Cells perform specialized somatic functions but divide only upon specific injury or growth factor stimulation", "Permanent necrotic state leading to cell lysis, State where DNA replicates continuously, Phase of rapid mitotic proliferation"),
            ("G1/S Checkpoint (Restriction point)", "Critical regulatory transition where the cell commits irreversibly to DNA replication and division upon checking DNA integrity", "Regulated by cyclin D-CDK4/6 and retinoblastoma (Rb) protein phosphorylation", "Phase where spindle fibers are disassembled, Time when chromosomes are sorted into gametes, Point of nuclear envelope degradation")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Nuclear Dynamics Across the Cell Cycle.**\n- Interphase: Chromatin is dispersed, active transcription & replication (S-phase).\n- M-Phase: Karyokinesis (Prophase \\(\\rightarrow\\) Metaphase \\(\\rightarrow\\) Anaphase \\(\\rightarrow\\) Telophase) divides the duplicated genome.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Biological Significance:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 8: Clinical & Pathophysiological Aspects of the Nucleus
    arch8 = {
        'templates': [
            "Which biomedical condition or diagnostic feature relates to: '{0}'?:",
            "In clinical pathology and medicine: '{0}' is characterized by:",
            "What clinical insight is provided by: '{0}'?:",
            "How does medicine utilize: '{0}' as a diagnostic biomarker?:",
            "A physician analyzes a patient biopsy: '{0}'. The accurate finding is:",
            "Which disease mechanism explains: '{0}'?:",
            "What is the medical significance of: '{0}'?:",
            "Why is '{0}' important in oncology and clinical genetics?:",
            "What pathophysiological defect causes: '{0}'?:",
            "Evaluate the biomedical statement regarding: '{0}':"
        ],
        'data': [
            ("Laminopathies (e.g., Hutchinson-Gilford Progeria Syndrome)", "Caused by mutations in LMNA gene encoding lamin A, leading to abnormal progerin protein, nuclear envelope blebbing, and premature aging", "Patients exhibit rapid clinical aging, alopecia, cardiovascular disease, and severe atherosclerosis in childhood", "Nutritional deficiency of vitamin C, Bacterial infection of nuclear pores, Excess ribosome accumulation in cytoplasm"),
            ("Aneuploidy (e.g., Trisomy 21 / Down syndrome)", "Presence of an abnormal number of chromosomes due to non-disjunction of homologous chromosomes or sister chromatids during meiosis", "Human karyotype exhibits 47 chromosomes (47, XX, +21 or 47, XY, +21) with characteristic intellectual and physical features", "Complete absence of nucleus in somatic cells, Duplication of all 46 chromosomes into 92, Deletion of entire X chromosome in all males"),
            ("Anaplasia and high Nuclear-to-Cytoplasmic (N:C) ratio in cancer", "Malignant cancer cells display enlarged, hyperchromatic, irregularly contoured nuclei with a high N:C ratio (approaching 1:1 vs normal 1:4 to 1:6)", "Hallmark of malignancy used in histopathological grading and Pap smear cervical cancer screening", "Shrinkage of nucleus into tiny pyknotic bead, Total loss of DNA from tumor cells, Complete disappearance of nucleoli in cancer"),
            ("Systemic Lupus Erythematosus (SLE) and Antinuclear Antibodies (ANA)", "Autoimmune disorder where autoantibodies target nuclear constituents (double-stranded DNA, histones, Sm ribonucleoproteins)", "Detected by indirect immunofluorescence giving distinctive nuclear rim, speckled, or homogeneous staining patterns", "Viral infection degrading the cell wall, Genetic defect preventing ribosome export, Toxin inhibiting mitochondrial ATP synthesis"),
            ("Barr body examination in sex chromosome anomalies", "Used to detect Turner syndrome (45, X0; 0 Barr bodies) and Klinefelter syndrome (47, XXY; 1 Barr body)", "Number of Barr bodies \\(= \\text{Total X chromosomes} - 1\\)", "Detects sickle cell anemia mutations, Counts the number of autosomes, Measures glucose levels in blood"),
            ("Nucleoside analogue drugs (e.g., AZT, Remdesivir)", "Antiviral drugs that terminate viral nucleic acid chain elongation by lacking a 3'-OH group required for phosphodiester bond formation", "Inhibit reverse transcriptase or viral RNA-dependent RNA polymerase to block replication", "Disassemble nuclear pore complexes, Neutralize histone positive charges, Dissolve plasma membrane bilayer"),
            ("Radiation-induced double-strand DNA breaks (DSBs)", "Ionizing radiation creates lethal breaks in DNA backbone, triggering phosphorylation of histone variant H2AX (\\(\\gamma\\text{-H2AX}\\))", "Failure of non-homologous end joining (NHEJ) or homologous recombination causes chromosomal aberrations or cell death", "Causes spontaneous synthesis of new chromosomes, Reverses aging by shortening telomeres, Stimulates excessive cell wall production"),
            ("Karyolysis, Pyknosis, and Karyorrhexis in cell death", "Pyknosis (nuclear shrinkage), Karyorrhexis (nuclear fragmentation), and Karyolysis (enzymatic dissolution of chromatin) characterize necrosis", "Irreversible nuclear morphological changes signaling definitive somatic cell death", "Active stages of normal mitotic division, Stages of ribosome biogenesis in nucleolus, Reversible steps of endocytosis"),
            ("Epigenetic histone modifications in gene expression", "Histone acetylation (HATs) neutralizes positive lysine charges, opening chromatin for active transcription; HDACs reverse it", "Aberrant histone deacetylation is implicated in cancer; HDAC inhibitors act as promising antineoplastic drugs", "Permanent mutation of the DNA sequence, Physical destruction of the nuclear envelope, Irreversible denaturation of DNA polymers"),
            ("Telomerase reactivation in human cancers", "Telomerase ribonucleoprotein extends telomeric repeat sequences (TTAGGG) to confer cellular immortality in \\(\\approx 90\\%\\) of cancers", "Enables cancer cells to bypass the Hayflick limit of cellular senescence and divide indefinitely", "Degrades cellular RNA to induce apoptosis, Transcribes mitochondrial tRNA genes, Synthesizes new nuclear envelopes")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Nuclear Pathology & Clinical Genetics.**\n- Genetic, structural (lamins), or numerical abnormalities in the nucleus produce profound human diseases (progeria, trisomy, cancer).\n- Histopathological examination of nuclear morphology (N:C ratio, hyperchromasia) is standard oncology practice.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Clinical Implication:**\n{item[2]}."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-2-2.3.1", "Nuclear envelope, nucleolus, chromatin and DNA genes", archs)


# ==========================================
# 2.3.2: Prokaryotic vs Eukaryotic cell comparison
# ==========================================
def gen_2_3_2():
    # Arch 1: Nucleoid vs True Nucleus Comparison
    arch1 = {
        'templates': [
            "In comparing prokaryotic and eukaryotic genetic organization: '{0}' is defined by:",
            "What distinguishes prokaryotes from eukaryotes regarding: '{0}'?:",
            "Consider the nuclear organization: '{0}' is characterized by:",
            "Which statement accurately contrasts: '{0}'?:",
            "A microbiology student examines cell types: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' fundamentally differ between prokaryotes and eukaryotes?:",
            "Evaluate the genomic structural feature: '{0}':",
            "Why is '{0}' a defining taxonomic criteria in cytology?:",
            "What is the structural nature of: '{0}'?:"
        ],
        'data': [
            ("Prokaryotic nucleoid", "An irregularly shaped, non-membrane enclosed region containing a single circular double-stranded DNA molecule", "Lacks a nuclear envelope, nucleolus, and nucleoplasm; DNA is in direct contact with the cytoplasm", "A double-membrane enclosed nucleus with multiple linear chromosomes, An organelle surrounded by a peptidoglycan wall, A dense lipid vesicle storing RNA"),
            ("Eukaryotic true nucleus", "A distinct organelle bounded by a double-layered nuclear envelope with pores, containing linear chromatin and nucleolus", "Isolates transcription in nucleoplasm from translation in cytoplasm, enabling complex pre-mRNA processing", "A naked circular plasmid floating free in cytoplasm, A single-layered non-porous lipid sac, A transient structure present only during M-phase"),
            ("Prokaryotic DNA packaging proteins", "Packaged by small basic nucleoid-associated proteins (NAPs e.g., HU, IHF, H-NS) and supercoiling, lacking true histones", "Organized into looped domains maintained by RNA and non-histone proteins without nucleosome octamers", "Packaged into 146 bp nucleosome octamers with histone H1, Wrapped around spherical lipid droplets, Naked without any associated proteins"),
            ("Eukaryotic DNA packaging with histones", "Genomic DNA is packaged into regular repeating nucleosome octamers (H2A, H2B, H3, H4) and compacted into chromatin fibers", "Enables epigenetic gene regulation through histone post-translational modifications (acetylation, methylation)", "Compacted purely by magnesium ions without proteins, Attached directly to outer plasma membrane, Maintained as open circular relaxed plasmids"),
            ("Presence of introns and pre-mRNA processing", "Eukaryotic protein-coding genes contain non-coding introns requiring 5' capping, splicing, and 3' polyadenylation", "Coupled with spatial separation of transcription (nucleus) and translation (cytoplasm)", "Prokaryotes contain massive introns in all operons, Eukaryotes lack introns entirely, Prokaryotes require spliceosome complexes in cytoplasm"),
            ("Coupled transcription and translation in prokaryotes", "Translation begins on the nascent mRNA strand before transcription is even completed, because there is no nuclear membrane barrier", "Enables rapid physiological responses and feedback control (e.g., attenuation in the trp operon)", "Requires transport of mRNA into mitochondria, Occurs only after cell division finishes, Inhibited completely by ribosomes"),
            ("Extrachromosomal plasmids in prokaryotes", "Small, circular, self-replicating double-stranded DNA molecules carrying non-essential accessory genes (e.g., antibiotic resistance)", "Can be horizontally transferred between bacteria via conjugation (F-plasmids, R-plasmids)", "Essential chromosomes encoding all housekeeping genes, Linear protein filaments functioning as flagella, Lipid storage droplets in the periplasm"),
            ("Number and morphology of chromosomes", "Prokaryotes typically possess a single circular chromosome; Eukaryotes possess multiple linear chromosomes", "Bacteria are functionally haploid (1 copy of circular chromosome), whereas eukaryotes are typically diploid (2n)", "Prokaryotes have hundreds of linear chromosomes, Eukaryotes possess only one circular plasmid, Both possess identical pairs of linear autosomes"),
            ("Genomic size and non-coding DNA proportion", "Eukaryotes have large genomes (\\(10^7\\text{ to }10^{11}\\text{ bp}\\)) with high non-coding repetitive DNA; Prokaryotes have compact genomes (\\(10^6\\text{ to }10^7\\text{ bp}\\)) with \\(> 85\\%\\) coding regions", "Reflects evolutionary gene density and complex regulatory architectures in multicellular eukaryotes", "Bacteria have 99% non-coding satellite DNA, Eukaryotes have zero non-coding introns or spacers, Both have identical genome lengths of 1 million bp"),
            ("Origin of replication (oriC)", "Bacterial circular chromosomes typically have a single origin of replication (oriC); Eukaryotic linear chromosomes have thousands of origins", "Multiple origins ensure complete eukaryotic genome replication within the brief window of S-phase", "Bacteria possess thousands of origins per chromosome, Eukaryotes have only one single origin at the centromere, Neither utilizes specific replication origin sites")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Genomic Architecture Differences.**\n- Prokaryotes: Nucleoid (no membrane), single circular DNA, no histones, no introns, coupled transcription-translation.\n- Eukaryotes: True nucleus (double membrane + pores), multiple linear chromosomes, histones (nucleosomes), introns + splicing.\n\n**Step 2: Contrast '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Cytological Significance:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 2: Ribosomes (70S vs 80S) and Protein Synthesis Machinery
    arch2 = {
        'templates': [
            "What is the structural and biochemical difference in: '{0}'?:",
            "In comparing prokaryotic and eukaryotic protein synthesis: '{0}' is characterized by:",
            "Consider ribosomal sedimentation coefficients: '{0}' consists of:",
            "Which statement precisely describes: '{0}'?:",
            "A pharmacology student analyzes antibiotic targets: '{0}'. What is true?:",
            "Identify the accurate fact regarding ribosomal architecture: '{0}':",
            "How does '{0}' affect cellular translation?:",
            "What biochemical feature defines: '{0}'?:",
            "Why is '{0}' critical for selective antibacterial drug toxicity?:",
            "Evaluate the comparative feature: '{0}':"
        ],
        'data': [
            ("Prokaryotic 70S ribosome", "Composed of a small 30S subunit (16S rRNA + 21 proteins) and a large 50S subunit (23S rRNA + 5S rRNA + 31 proteins)", "Sedimentation coefficient 70 Svedberg units; sensitive to chloramphenicol, tetracycline, and streptomycin", "Composed of 40S and 60S subunits totaling 80S, Bounded by double lipid membrane, Synthesizes DNA polymers instead of proteins"),
            ("Eukaryotic cytosolic 80S ribosome", "Composed of a small 40S subunit (18S rRNA + 33 proteins) and a large 60S subunit (28S + 5.8S + 5S rRNA + 49 proteins)", "Sedimentation coefficient 80S; sensitive to cycloheximide but resistant to chloramphenicol and streptomycin", "Composed of 30S and 50S subunits totaling 70S, Found freely inside the nucleoid, Assembled in the Golgi cisternae"),
            ("Mitochondrial and chloroplast ribosomes (70S)", "Semiautonomous eukaryotic organelles contain 70S ribosomes structurally homologous to bacterial ribosomes", "Strong evolutionary evidence supporting the Endosymbiotic Theory of organelle origin", "Contain 80S ribosomes identical to cytosolic ribosomes, Contain 100S ribosomes bounded by peptidoglycan, Lack ribosomal RNA entirely"),
            ("Svedberg unit (S)", "Unit of sedimentation velocity in an ultracentrifuge field (\\(1\\text{ S} = 10^{-13}\\text{ seconds}\\)), reflecting size, mass, and shape", "Values are non-additive because sedimentation depends on hydrodynamic drag as well as mass (50S + 30S = 70S)", "Direct arithmetic sum of individual molecular weights, Unit of electrical conductivity of cytoplasm, Measure of DNA base pair length"),
            ("16S rRNA vs 18S rRNA", "16S rRNA is present in prokaryotic 30S subunit (binds Shine-Dalgarno sequence); 18S rRNA is in eukaryotic 40S subunit", "16S rRNA gene sequences are the gold standard molecular chronometer for bacterial phylogenetic classification", "16S rRNA is a eukaryotic histone protein, 18S rRNA is found only in viruses, Both rRNAs are translated into metabolic enzymes"),
            ("Shine-Dalgarno sequence vs Kozak consensus", "Prokaryotic mRNAs possess a purine-rich Shine-Dalgarno sequence (AGGAGG) upstream of AUG; Eukaryotic mRNAs utilize Kozak consensus and 5' cap", "Shine-Dalgarno pairs with complementary 3' end of 16S rRNA to position the start codon at the P site", "Prokaryotes scan from 5' methylguanosine cap, Eukaryotes lack start codons, Both require poly-A tails for ribosome binding"),
            ("Initiator amino acid (fMet vs Met)", "Prokaryotes use N-formylmethionine (fMet-tRNA) to initiate translation; Eukaryotes use unformylated methionine (Met-tRNA)", "Bacterial fMet peptides are recognized by mammalian immune cells as pathogen-associated molecular patterns (PAMPs)", "Prokaryotes use valine to initiate translation, Eukaryotes use formylmethionine, Neither uses methionine as start codon"),
            ("Mechanism of Streptomycin action", "Binds specifically to bacterial 30S ribosomal subunit (16S rRNA), causing mRNA misreading and inhibiting initiation", "Exhibits selective toxicity against bacteria without harming host eukaryotic cytosolic 80S ribosomes", "Inhibits eukaryotic RNA polymerase II, Hydrolyzes phospholipid bilayer of mitochondria, Degrades eukaryotic nuclear DNA"),
            ("Mechanism of Chloramphenicol action", "Binds to 50S bacterial ribosomal subunit and inhibits peptidyl transferase enzyme (transpeptidation)", "Prevents peptide bond formation between incoming aminoacyl-tRNA and growing polypeptide chain", "Binds to 40S subunit blocking mRNA binding, Destroys peptidoglycan crosslinks, Inactivates bacterial DNA gyrase"),
            ("Mechanism of Cycloheximide action", "Selectively blocks eukaryotic cytosolic 80S ribosome peptidyl transferase and translocation; inactive against bacterial 70S", "Widely used in research to distinguish nuclear-encoded eukaryotic translation from organellar/prokaryotic translation", "Kills bacteria by rupturing cell walls, Selectively destroys mitochondrial plasmids, Prevents bacterial binary fission")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Ribosomal Differences (70S vs 80S).**\n- Prokaryotes: 70S (50S + 30S), 16S/23S/5S rRNAs, fMet, Shine-Dalgarno, inhibited by chloramphenicol/streptomycin.\n- Eukaryotes: 80S (60S + 40S), 18S/28S/5.8S/5S rRNAs, Met, 5' Cap & Kozak, inhibited by cycloheximide.\n\n**Step 2: Contrast '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Pharmacological / Biological Importance:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Membrane-Bound Organelles and Cytoskeleton
    arch3 = {
        'templates': [
            "In comparing cellular compartmentalization: '{0}' is characterized by:",
            "What distinguishes prokaryotes and eukaryotes regarding: '{0}'?:",
            "Consider intracellular organelle distribution: '{0}' exhibits:",
            "Which statement accurately explains: '{0}'?:",
            "A cell biologist analyzes internal cell architecture: '{0}'. What is true?:",
            "Identify the accurate cytological fact regarding: '{0}':",
            "How does '{0}' define eukaryotic compartmentalization?:",
            "Evaluate the presence or absence of: '{0}':",
            "Why is '{0}' exclusively found in eukaryotic organisms?:",
            "What structural organization corresponds to: '{0}'?:"
        ],
        'data': [
            ("Membrane-bound organelles (ER, Golgi, Mitochondria, Lysosomes)", "Completely absent in prokaryotes; Highly developed and compartmentalized in eukaryotes", "Enables specialized microenvironments with dedicated pH, enzyme sets, and substrate concentrations in eukaryotes", "Present in identical numbers in both prokaryotes and eukaryotes, Present in bacteria but absent in plant cells, Bounded by peptidoglycan walls in eukaryotes"),
            ("Endoplasmic Reticulum (RER & SER)", "Absent in prokaryotes; Eukaryotes possess extensive network of tubules and cisternae for protein folding and lipid synthesis", "Prokaryotes perform protein synthesis on free cytoplasmic ribosomes and secrete via plasma membrane translocons", "Prokaryotes possess RER but lack SER, Eukaryotes lack internal membranes entirely, RER is responsible for ATP synthesis in bacteria"),
            ("Golgi apparatus (Dictyosomes)", "Absent in prokaryotes; Eukaryotes possess polarized stacks of flattened cisternae for protein modification, sorting, and packaging", "Modifies proteins via glycosylation and tags them for lysosomes, plasma membrane, or extracellular secretion", "Present in bacteria as spherical vesicles, Site of cellular respiration in prokaryotes, Responsible for DNA replication in plants"),
            ("Mitochondria vs Mesosomes", "Eukaryotes possess double-membraned mitochondria for aerobic respiration; Bacteria carry respiratory electron transport chains on plasma membrane (or mesosomal invaginations)", "Mesosomes were once thought to be distinct organelles, now recognized largely as artifacts of chemical fixation", "Bacteria possess mitochondria with 80S ribosomes, Eukaryotes lack mitochondria and use plasma membrane, Both use chloroplasts for ATP synthesis"),
            ("Plastids (Chloroplasts, Chromoplasts, Leucoplasts)", "Absent in prokaryotes; photosynthetic bacteria (cyanobacteria) possess unstacked thylakoid membranes floating freely in cytoplasm", "Plant and algal eukaryotes possess double-membraned chloroplasts with organized grana and stroma", "Present in all prokaryotes, Eukaryotes lack plastids entirely, Cyanobacteria have triple-membraned chloroplasts with 80S ribosomes"),
            ("Lysosomes and Peroxisomes", "Absent in prokaryotes; Eukaryotes possess single-membrane lysosomes (acid hydrolases at pH 4.5–5.0) and peroxisomes (catalase)", "In bacteria, periplasmic space between plasma membrane and peptidoglycan performs analogous degradation functions", "Bacteria possess giant lysosomes containing DNA polymerases, Lysosomes synthesize glycogen in plant cells, Peroxisomes are found only in viruses"),
            ("Cytoskeleton (Microfilaments, Microtubules, Intermediate filaments)", "Eukaryotes possess an elaborate cytoskeleton composed of actin, tubulin, and intermediate filaments", "Responsible for cell shape, intracellular organelle transport, amoeboid motility, and mitotic spindle assembly", "Prokaryotes possess identical tubulin spindles, Eukaryotic cytoplasm is a static liquid devoid of fibers, Cytoskeleton is made of peptidoglycan polymers"),
            ("Bacterial cytoskeletal homologues (FtsZ, MreB, Crescentin)", "Bacteria possess structural homologues of eukaryotic proteins: FtsZ (tubulin homolog), MreB (actin homolog), and Crescentin (intermediate filament homolog)", "FtsZ forms the contractile Z-ring during bacterial binary fission; MreB maintains rod shape in bacilli", "Bacteria possess true 9+2 tubulin microtubules, FtsZ is a lipid enzyme that degrades DNA, Eukaryotes lack actin and tubulin genes"),
            ("Vacuoles and Tonoplast", "Plant eukaryotes have a prominent central vacuole bounded by a tonoplast maintaining turgor pressure; Prokaryotes lack true vacuoles (some have gas vacuoles)", "Gas vacuoles in aquatic photosynthetic bacteria are non-membrane proteinaceous shells permeable to gases, not water", "Bacteria possess massive sap vacuoles taking up 90% cell volume, Tonoplast is a peptidoglycan layer, Animal cells have a giant central tonoplast"),
            ("Centrioles and Centrosomes", "Absent in prokaryotes and higher gymnosperms/angiosperms; Present in animal and lower plant eukaryotic cells", "Organize spindle apparatus during animal mitosis and serve as basal bodies for cilia and flagella", "Essential for bacterial binary fission, Found inside the bacterial nucleoid, Made of circular DNA plasmids")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Organelle & Cytoskeletal Differences.**\n- Prokaryotes lack membrane-bound organelles (no ER, Golgi, mitochondria, plastids, lysosomes) and true eukaryotic cytoskeleton.\n- Cellular respiration occurs on bacterial plasma membrane; photosynthesis in cyanobacteria occurs on free thylakoids.\n\n**Step 2: Contrast '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Functional / Evolutionary Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Cell Wall, Flagella, and Surface Appendages
    arch4 = {
        'templates': [
            "How do prokaryotes and eukaryotes differ in: '{0}'?:",
            "What is the biochemical composition and structural difference of: '{0}'?:",
            "In comparative cytology, '{0}' is defined by:",
            "Which statement precisely describes the distinction in: '{0}'?:",
            "A microbiologist investigates cell envelopes: '{0}'. What is true?:",
            "Identify the accurate fact regarding surface appendages: '{0}':",
            "How does '{0}' function differently between cell types?:",
            "What biochemical feature characterizes: '{0}'?:",
            "Why is '{0}' fundamentally distinct in bacteria compared to eukaryotes?:",
            "Evaluate the comparative feature: '{0}':"
        ],
        'data': [
            ("Bacterial cell wall vs Plant cell wall", "Bacterial wall is composed of peptidoglycan (murein); Plant wall is composed of cellulose, hemicellulose, and pectin", "Peptidoglycan consists of alternating NAG and NAM glycan chains cross-linked by short tetrapeptide bridges", "Bacterial wall is pure cellulose, Plant wall is made of chitin and peptidoglycan, Animal cells possess a thick murein wall"),
            ("Fungal cell wall vs Bacterial wall", "Fungal wall is composed of chitin (polymer of N-acetylglucosamine - NAG) and beta-glucans; Bacterial wall contains peptidoglycan with NAM", "Fungal walls lack muramic acid (NAM) and D-amino acids found uniquely in bacterial peptidoglycan", "Fungi possess peptidoglycan walls sensitive to penicillin, Bacteria possess chitin walls, Both walls are made of cholesterol"),
            ("Archaeal cell wall (Pseudomurein / S-layer)", "Archaea lack true peptidoglycan; possess pseudomurein (NAG + N-acetyltalosaminuronic acid with \\(\\beta(1\\rightarrow 3)\\) linkages) or protein S-layers", "Insensitive to lysozyme and penicillin, allowing archaea to inhabit extreme environments (extremophiles)", "Archaea possess cellulose identical to plants, Archaea lack cell walls entirely, Archaea have lipid bilayer cell walls"),
            ("Bacterial flagellum vs Eukaryotic flagellum", "Bacterial flagellum is made of flagellin protein and rotates like a propeller (driven by proton motive force); Eukaryotic flagellum is made of tubulin (9+2 axoneme) and bends like a whip (driven by dynein ATP)", "Bacterial flagella lack an enclosing membrane; Eukaryotic flagella and cilia are enveloped by the plasma membrane", "Bacterial flagella contain 9+2 microtubules, Eukaryotic flagella rotate by rotary motor, Both are driven by sodium symport"),
            ("Basal body and motor of bacterial flagellum", "Consists of rotor, stator, and protein rings (L, P, MS, C rings in Gram-negative bacteria) embedded in cell envelope", "Driven directly by electrochemical proton gradient (\\(\\text{H}^+\\) or \\(\\text{Na}^+\\) influx) without ATP hydrolysis", "Driven by myosin-actin sliding filaments, Powered by direct glucose phosphorylation, Anchored to the nuclear envelope"),
            ("Eukaryotic cilia and flagella (9+2 Axoneme)", "Composed of 9 peripheral doublet microtubules surrounding 2 central singlet microtubules with inner and outer dynein arms", "Anchored in cytoplasm by a basal body (kinetosome) displaying a 9+0 triplet microtubule arrangement", "Composed of single rotating flagellin filaments, Powered by proton motive force across cell wall, Lacks membrane covering"),
            ("Pili and Fimbriae in bacteria", "Proteinaceous surface appendages made of pilin; Fimbriae mediate surface adhesion, whereas sex pili mediate bacterial conjugation", "Completely absent in eukaryotic cells; critical virulence factors for mucosal colonization (e.g., Neisseria gonorrhoeae)", "Used for swimming motility like cilia, Responsible for DNA replication in cytoplasm, Storage granules for carbohydrates"),
            ("Bacterial capsule / Glycocalyx", "Viscous gelatinous layer composed of polysaccharides (or polypeptides in B. anthracis) external to the cell wall", "Protects pathogenic bacteria from phagocytosis by host white blood cells and prevents desiccation", "Rigid crystalline shell made of silica, Site of electron transport chain, Membrane bilayer containing transport channels"),
            ("Gram-positive vs Gram-negative cell wall", "Gram-positive has thick multilayered peptidoglycan (\\(20\\text{--}80\\text{ nm}\\)) with teichoic acids; Gram-negative has thin peptidoglycan (\\(2\\text{--}7\\text{ nm}\\)) and outer membrane containing LPS", "Gram-negative outer membrane contains endotoxin (lipopolysaccharide - LPS) and porin proteins", "Gram-positive has outer lipid membrane with LPS, Gram-negative lacks peptidoglycan, Both stain pink with Gram stain"),
            ("Mycoplasma (Wall-less bacteria)", "Smallest free-living prokaryotes (\\(\\approx 0.1\\text{ to }0.3\\text{ }\\mu\\text{m}\\)) completely lacking a peptidoglycan cell wall; membrane stabilized by sterols", "Naturally resistant to penicillin and beta-lactam antibiotics that target cell wall synthesis; pleomorphic in shape", "Obligate eukaryotic parasites with chitin walls, Gram-positive spore-forming bacilli, Photosynthetic cyanobacteria with silica shells")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Cell Envelope & Surface Appendages.**\n- Bacteria: Peptidoglycan wall (NAG + NAM), rotatory flagellin motor (proton motive force), pili/fimbriae, capsule.\n- Plants/Fungi: Cellulose or Chitin wall, eukaryotic 9+2 axoneme flagella (whip-like, dynein ATP-driven), no pili.\n\n**Step 2: Contrast '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Structural/Clinical Details:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Reproduction, Cell Division, and Evolutionary Endosymbiosis
    arch5 = {
        'templates': [
            "In comparing cellular reproduction and evolution: '{0}' is characterized by:",
            "What distinguishes prokaryotic and eukaryotic reproduction regarding: '{0}'?:",
            "Consider the evolutionary transition: '{0}' demonstrates that:",
            "Which statement precisely describes: '{0}'?:",
            "An evolutionary biologist investigates cellular lineages: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does '{0}' differ fundamentally between bacteria and eukaryotes?:",
            "Evaluate the evidence supporting: '{0}':",
            "Why is '{0}' critical to the modern understanding of cell biology?:",
            "What mechanistic principle explains: '{0}'?:"
        ],
        'data': [
            ("Binary fission in bacteria vs Mitosis in eukaryotes", "Bacteria divide by binary fission (direct DNA replication, attachment to plasma membrane, and FtsZ ring constriction) without spindle apparatus; Eukaryotes divide by mitosis involving chromosome condensation and microtubule spindles", "Bacterial binary fission is rapid (e.g., E. coli divides every 20 min) and does not involve nuclear envelope breakdown", "Bacteria undergo meiosis with crossing over, Eukaryotes divide by budding without DNA replication, Mitosis occurs inside the bacterial nucleoid"),
            ("Absence of true sexual reproduction (meiosis) in prokaryotes", "Prokaryotes lack gamete formation, syngamy, and meiosis; Genetic recombination occurs via horizontal gene transfer (transformation, transduction, conjugation)", "Meiosis with homologous recombination and independent assortment is a unique eukaryotic evolutionary innovation", "Bacteria reproduce sexually via haploid sperm and eggs, Eukaryotes lack sexual reproduction entirely, Bacteria undergo meiotic reduction division"),
            ("Bacterial Conjugation (F-plasmid transfer)", "Unidirectional transfer of plasmid DNA from donor (\\(\\text{F}^+\\)) to recipient (\\(\\text{F}^-\\)) through a specialized conjugation pilus (sex pilus)", "Discovered by Lederberg and Tatum (1946); can transfer antibiotic resistance genes across species", "Uptake of naked foreign DNA from the environment, Viral transfer of bacterial genes by bacteriophage, Division of a bacterial cell into four spores"),
            ("Bacterial Transformation (Griffith 1928, Avery 1944)", "Uptake and incorporation of free naked exogenous DNA fragments from the surrounding extracellular medium into a competent bacterial cell", "Pivotal historical experiment proving DNA (not protein) is the transforming genetic principle", "Transfer of viral capsids between host cells, Injection of bacterial DNA by a plasmid pilus, Spontaneous generation of new bacterial chromosomes"),
            ("Bacterial Transduction (Zinder and Lederberg 1952)", "Transfer of bacterial genetic material from one bacterium to another mediated by a bacteriophage (bacterial virus)", "Can be generalized (random bacterial DNA fragments packaged) or specialized (specific adjacent genes packaged)", "Direct cell-to-cell contact via sex pilus, Passive diffusion through aquaporin channels, Endocytosis of bacterial plasmids by amoebae"),
            ("Endosymbiotic Theory (Lynn Margulis 1967)", "Mitochondria and chloroplasts originated as free-living aerobic prokaryotes (alphaproteobacteria and cyanobacteria) engulfed by ancestral host cells", "Supported by circular DNA, 70S ribosomes, binary fission, and double membrane envelope", "Mitochondria evolved by spontaneous self-assembly of nuclear membranes, Chloroplasts originated from viral infection of lysosomes, Organelles evolved by de novo synthesis of proteins"),
            ("Evidence for mitochondrial endosymbiosis", "Possess their own circular double-stranded DNA, 70S ribosomes, transcribe their own RNA, and replicate independently by binary fission", "Inner mitochondrial membrane contains cardiolipin and electron transport complexes homologous to bacterial plasma membranes", "Mitochondria contain 80S ribosomes and linear chromosomes, Bounded by thick peptidoglycan cell walls, Lack all nucleic acids and rely entirely on cytoplasm"),
            ("Evidence for chloroplast endosymbiosis", "Contain circular DNA, 70S ribosomes, photosynthetic thylakoid membranes, and pigments homologous to modern cyanobacteria", "Sequencing of chloroplast 16S rRNA proves direct phylogenetic lineage from oxygenic photosynthetic cyanobacteria", "Chloroplasts originated from green fungal spores, Synthesize their own cellulose cell wall, Replicate by assembling tubulin spindle fibers"),
            ("Primary vs Secondary Endosymbiosis", "Primary endosymbiosis involves engulfment of a bacterium by a eukaryote (yielding 2 membranes); Secondary endosymbiosis involves engulfment of a eukaryotic alga by another eukaryote (yielding 3 or 4 membranes e.g., euglenoids, diatoms)", "Explains the complex multi-membrane envelopes of brown algae, diatoms, and dinoflagellates", "Primary endosymbiosis occurred only in animals, Secondary endosymbiosis created bacterial plasmids, Both yield single-membraned organelles"),
            ("Hydrogenosome and Mitosome evolution", "Anaerobic eukaryotic parasites (e.g., Trichomonas, Giardia) possess degenerate, modified mitochondria that generate ATP by substrate-level phosphorylation or assemble Fe-S clusters", "Proves that all extant eukaryotes derived from a common ancestor that already possessed endosymbiotic mitochondria", "Proves that anaerobic eukaryotes evolved completely independently from bacteria, Relics of ancient chloroplasts in animal cells, Organelles synthesized de novo by the Golgi apparatus")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Reproduction & Evolutionary Endosymbiosis.**\n- Prokaryotes divide by binary fission (FtsZ ring, no spindle, no nuclear breakdown); exchange genes via HGT (transformation, conjugation, transduction).\n- Eukaryotes divide by mitosis/meiosis; originated by serial endosymbiosis (Margulis: mitochondria from \\(\\alpha\\)-proteobacteria, plastids from cyanobacteria).\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Evolutionary Proof:**\n{item[2]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Comprehensive Comparative Table / Diagnostic Match
    arch6 = {
        'templates': [
            "Which row in the table correctly compares prokaryotes and eukaryotes regarding: '{0}'?:",
            "In a comparative diagnostic test: '{0}' correctly matches:",
            "Identify the correct pairwise comparison: '{0}':",
            "Which statement presents a 100% accurate contrast: '{0}'?:",
            "A cytological summary table features: '{0}'. The accurate entry is:",
            "Compare prokaryotes and eukaryotes: '{0}' is accurately stated as:",
            "Which comparative fact holds true for: '{0}'?:",
            "Select the correct pairing for: '{0}':",
            "In an analytical examination question: '{0}' is correctly described by:",
            "Evaluate the comparative cytological criteria: '{0}':"
        ],
        'data': [
            ("Cell size", "Prokaryotes: \\(0.1\\text{ to }5.0\\text{ }\\mu\\text{m}\\); Eukaryotes: \\(10\\text{ to }100\\text{ }\\mu\\text{m}\\)", "Prokaryotes are generally 10 to 100 times smaller in linear dimension, with a much larger surface-area-to-volume ratio", "Prokaryotes: 100 to 500 μm; Eukaryotes: 0.1 to 1.0 μm, Both have identical average diameter of 50 μm, Prokaryotes are always visible to naked eye"),
            ("Compartmentalization", "Prokaryotes: Absent (single cytoplasmic compartment); Eukaryotes: Extensive internal compartmentalization by membrane-bound organelles", "Enables eukaryotes to maintain distinct metabolic microenvironments (e.g., lysosomal acid hydrolases separated from cytoplasm)", "Prokaryotes possess extensive nuclear compartments, Eukaryotes lack all internal membranes, Both have identical organelle numbers"),
            ("Genetic material", "Prokaryotes: Single circular DNA in nucleoid, no true histones; Eukaryotes: Multiple linear chromosomes in nucleus, packaged with histones", "Eukaryotic DNA has telomeres, centromeres, and nucleosomal packaging (H2A, H2B, H3, H4, H1)", "Prokaryotes have multiple linear chromosomes, Eukaryotes have a single circular naked plasmid, Both contain 46 linear chromosomes"),
            ("Site of cellular respiration", "Prokaryotes: Plasma membrane (mesosomal infoldings); Eukaryotes: Mitochondria (inner membrane cristae and matrix)", "Prokaryotes pump protons across plasma membrane to generate ATP; Eukaryotes pump across inner mitochondrial membrane", "Prokaryotes respire in Golgi cisternae, Eukaryotes respire across outer plasma membrane only, Neither utilizes proton gradients"),
            ("Cytoplasmic streaming (cyclosis)", "Prokaryotes: Absent; Eukaryotes: Present (active actin-myosin driven circulation of cytosol and organelles)", "Particularly prominent in large plant cells (e.g., Elodea, Chara) to facilitate nutrient and organelle distribution", "Prokaryotes display vigorous cyclosis, Eukaryotes lack cytoplasmic movement, Cyclosis is driven by bacterial flagellin"),
            ("Ribosomes", "Prokaryotes: 70S (30S + 50S) throughout cytoplasm; Eukaryotes: 80S (40S + 60S) in cytosol/RER, and 70S inside mitochondria and plastids", "Differential antibiotic sensitivity (e.g., chloramphenicol inhibits 70S, cycloheximide inhibits 80S)", "Prokaryotes have 80S only, Eukaryotes have 70S in cytosol and 80S in mitochondria, Both have identical 100S ribosomes"),
            ("Cell wall chemistry", "Prokaryotes: Peptidoglycan (bacteria) or Pseudomurein (archaea); Eukaryotes: Cellulose/pectin (plants), Chitin (fungi), Absent (animals)", "Peptidoglycan contains characteristic D-amino acids (D-alanine, D-glutamic acid) cross-linking glycan chains", "Prokaryotes have cellulose walls, Eukaryotes have peptidoglycan walls, Fungi possess peptidoglycan cell walls"),
            ("Mode of cell division", "Prokaryotes: Binary fission (no mitotic spindle, mediated by FtsZ ring); Eukaryotes: Mitosis and Meiosis (microtubule spindle apparatus)", "Binary fission does not involve nuclear envelope breakdown or chromosome condensation into karyotypes", "Prokaryotes divide by meiosis, Eukaryotes divide by budding without chromosomes, Both form microtubule spindles"),
            ("Transcription and translation", "Prokaryotes: Coupled simultaneously in cytoplasm; Eukaryotes: Spatially and temporally separated (transcription in nucleus, translation in cytoplasm)", "Separation allows extensive post-transcriptional RNA processing (splicing, capping, polyadenylation) in eukaryotes", "Prokaryotes transcribe in nucleus, Eukaryotes couple transcription and translation simultaneously, Neither requires RNA polymerase"),
            ("Endocytosis and Exocytosis (vesicular transport)", "Prokaryotes: Absent (cannot perform phagocytosis or pinocytosis); Eukaryotes: Present (receptor-mediated endocytosis, phagocytosis, exocytosis)", "Eukaryotes utilize dynamic actin cytoskeleton and vesicle fusion machinery (SNARE proteins, clathrin)", "Prokaryotes actively engulf large eukaryotic cells by phagocytosis, Eukaryotes lack exocytosis, Both lack vesicle transport")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Definitive Comparative Cytology.**\n- Prokaryotes (Bacteria, Archaea) vs Eukaryotes (Protists, Fungi, Plants, Animals).\n- Core differences span size, genome architecture, organelles, ribosomes, cell walls, and division.\n\n**Step 2: Contrast '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Details & Invariant:**\n{item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 7: Quantitative and Physical Comparisons (SA:V ratio, Diffusion Limits, Scaling)
    arch7 = {
        'templates': [
            "{0}:",
            "Calculate the physical cytology parameter: {0}:",
            "A biophysical cell scaling problem: {0}:",
            "Quantitative comparison between cell types: {0}:",
            "Solve the quantitative cytology problem: {0}:",
            "Analyze the numerical surface-area-to-volume calculation: {0}:",
            "Determine the correct numeric ratio or value: {0}:",
            "An analytical scaling calculation: {0}:",
            "Find the correct physical outcome: {0}:",
            "Compute the cellular parameter: {0}:"
        ],
        'data': [
            ("Consider a spherical bacterium of radius \\(r_1 = 1\\text{ }\\mu\\text{m}\\) and a spherical eukaryotic cell of radius \\(r_2 = 10\\text{ }\\mu\\text{m}\\). What is the ratio of their Surface-Area-to-Volume ratios (\\(\\text{SA:V}_1 / \\text{SA:V}_2\\))?", "10", "\\(\\text{SA:V} = (4\\pi r^2) / (\\frac{4}{3}\\pi r^3) = 3/r\\). For bacterium: \\(3/1 = 3\\text{ }\\mu\\text{m}^{-1}\\). For eukaryote: \\(3/10 = 0.3\\text{ }\\mu\\text{m}^{-1}\\). Ratio \\(= 3 / 0.3 = 10\\)", "1, 100, 0.1"),
            ("A cylindrical bacterium has diameter \\(1\\text{ }\\mu\\text{m}\\) and length \\(2\\text{ }\\mu\\text{m}\\). A eukaryotic amoeba has volume \\(8,000\\text{ }\\mu\\text{m}^3\\). How many such bacteria can fit into the volume of this single eukaryotic cell?", "\\(\\approx 5,093\\text{ bacteria}\\)", "Bacterial volume \\(= \\pi r^2 h = \\pi (0.5)^2 (2) = 0.5\\pi \\approx 1.57\\text{ }\\mu\\text{m}^3\\). Ratio \\(= 8,000 / 1.57 \\approx 5,093\\)", "\\(\\approx 500\\text{ bacteria}\\), \\(\\approx 50,000\\text{ bacteria}\\), \\(\\approx 509\\text{ bacteria}\\)"),
            ("Diffusion time \\(t\\) scales with the square of distance (\\(t \\approx x^2 / 2D\\)). If a small metabolite diffuses \\(1\\text{ }\\mu\\text{m}\\) in a bacterium in \\(0.5\\text{ ms}\\), how long will it take to diffuse across a large \\(100\\text{ }\\mu\\text{m}\\) eukaryotic egg cell by passive diffusion alone?", "\\(5.0\\text{ seconds}\\) (10,000-fold longer)", "\\(t_2 / t_1 = (x_2 / x_1)^2 = (100 / 1)^2 = 10,000\\). Time \\(= 0.5\\text{ ms} \\times 10,000 = 5,000\\text{ ms} = 5.0\\text{ s}\\). Demonstrates why large eukaryotes require active transport and cyclosis", "0.05 s, 50 s, 0.5 s"),
            ("An E. coli genome consists of \\(4.6 \\times 10^6\\text{ bp}\\). Given that DNA polymerase III replicates at \\(1,000\\text{ bp/sec}\\) bidirectionally from a single origin, calculate the minimum theoretical time required to replicate the genome", "\\(2,300\\text{ seconds}\\) (\\(\\approx 38.3\\text{ minutes}\\))", "Two replication forks proceed bidirectionally: total replication rate \\(= 2,000\\text{ bp/s}\\). Time \\(= 4.6 \\times 10^6 / 2,000 = 2,300\\text{ s} \\approx 38.3\\text{ min}\\)", "4,600 s (76.6 min), 1,150 s (19.2 min), 230 s (3.8 min)"),
            ("A human diploid genome contains \\(6.0 \\times 10^9\\text{ bp}\\). If eukaryotic DNA replication forks travel at \\(50\\text{ bp/sec}\\) bidirectionally, how many replication origins must fire simultaneously to replicate the genome in 5 hours (\\(18,000\\text{ seconds}\\))?", "\\(\\approx 3,333\\text{ origins}\\)", "Total DNA synthesized per origin in 5 h \\(= 2 \\text{ forks} \\times 50\\text{ bp/s} \\times 18,000\\text{ s} = 1.8 \\times 10^6\\text{ bp}\\). Number of origins \\(= 6.0 \\times 10^9 / 1.8 \\times 10^6 \\approx 3,333\\)", "\\(\\approx 333\\text{ origins}\\), \\(\\approx 33,333\\text{ origins}\\), \\(\\approx 100,000\\text{ origins}\\)"),
            ("If a bacterial cell has \\(70\\%\\) water and \\(15\\%\\) protein by weight, and a total mass of \\(1.0 \\times 10^{-12}\\text{ g}\\) (1 picogram), what is the approximate number of protein molecules in the bacterium assuming an average protein molecular weight of \\(40,000\\text{ Da}\\)?", "\\(\\approx 2.26 \\times 10^6\\text{ protein molecules}\\)", "Protein mass \\(= 0.15 \\times 10^{-12}\\text{ g} = 1.5 \\times 10^{-13}\\text{ g}\\). Moles of protein \\(= 1.5 \\times 10^{-13} / 40,000 = 3.75 \\times 10^{-18}\\text{ mol}\\). Molecules \\(= 3.75 \\times 10^{-18} \\times 6.022 \\times 10^{23} \\approx 2.26 \\times 10^6\\)", "\\(\\approx 2.26 \\times 10^4\\), \\(\\approx 2.26 \\times 10^8\\), \\(\\approx 2.26 \\times 10^5\\)"),
            ("What is the linear compaction ratio of an E. coli chromosome (length \\(1.6\\text{ mm} = 1,600\\text{ }\\mu\\text{m}\\)) packed inside a bacterial cell of length \\(2.0\\text{ }\\mu\\text{m}\\)?", "\\(800\\text{-fold}\\)", "\\(\\text{Compaction ratio} = 1,600\\text{ }\\mu\\text{m} / 2.0\\text{ }\\mu\\text{m} = 800\\)", "80-fold, 8,000-fold, 8-fold"),
            ("If an uncompacted human diploid DNA molecule is \\(2.0\\text{ meters}\\) long packed inside a nucleus of diameter \\(6\\text{ }\\mu\\text{m}\\), what is the linear compaction ratio?", "\\(\\approx 333,333\\text{-fold}\\)", "\\(\\text{Compaction ratio} = 2.0\\text{ m} / (6 \\times 10^{-6}\\text{ m}) \\approx 3.33 \\times 10^5\\)", "\\(\\approx 33,333\\text{-fold}\\), \\(\\approx 3,333\\text{-fold}\\), \\(\\approx 3,333,333\\text{-fold}\\)"),
            ("What is the volume ratio of a human egg cell (diameter \\(100\\text{ }\\mu\\text{m}\\)) compared to a sperm cell (head diameter \\(3\\text{ }\\mu\\text{m} \\times 5\\text{ }\\mu\\text{m}\\), volume \\(\\approx 20\\text{ }\\mu\\text{m}^3\\))?", "\\(\\approx 26,180\\text{-fold}\\)", "Egg volume \\(= \\frac{4}{3}\\pi (50)^3 = 523,598\\text{ }\\mu\\text{m}^3\\). Ratio \\(= 523,598 / 20 \\approx 26,180\\)", "\\(\\approx 2,618\\text{-fold}\\), \\(\\approx 261,800\\text{-fold}\\), \\(\\approx 260\\text{-fold}\\)"),
            ("In an actively growing bacterial culture undergoing binary fission every 30 minutes, how many bacterial cells will be produced from a single bacterium after 5 hours?", "1,024 cells (\\(2^{10}\\))", "Number of generations \\(n = 5\\text{ hours} / 0.5\\text{ hours} = 10\\). Total cells \\(= 2^{10} = 1,024\\)", "512 cells, 2,048 cells, 100 cells")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Physical & Quantitative Constraints.**\n{item[0]}\n\n**Step 2: Apply the Biophysical / Mathematical Formulation.**\n{item[2]}.\n\n**Step 3: Conclude.**\nResult is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 8: Clinical and Biotechnological Implications of Prokaryote vs Eukaryote Differences
    arch8 = {
        'templates': [
            "Which clinical or biotechnological application exploits: '{0}'?:",
            "In pharmacology and antimicrobial therapy: '{0}' is targeted because:",
            "What clinical rationale explains: '{0}'?:",
            "How does biotechnology utilize: '{0}'?:",
            "A medical student examines antibiotic mechanisms: '{0}'. What is true?:",
            "Which biomedical property of '{0}' provides selective antimicrobial action?:",
            "What is the therapeutic significance of: '{0}'?:",
            "Why is '{0}' non-toxic to human eukaryotic host cells?:",
            "What pharmacological principle governs: '{0}'?:",
            "Evaluate the biomedical statement regarding: '{0}':"
        ],
        'data': [
            ("Beta-lactam antibiotics (Penicillin, Ampicillin, Cephalosporin)", "Inhibit bacterial transpeptidase enzymes (PBPs) preventing peptidoglycan cell wall cross-linking, causing osmotic lysis", "Human eukaryotic cells lack peptidoglycan walls entirely, conferring high therapeutic safety index", "Inhibit human mitochondrial ATP synthase, Block eukaryotic nuclear importins, Hydrolyze eukaryotic plasma membrane lipids"),
            ("Fluoroquinolones (Ciprofloxacin, Levofloxacin)", "Selectively inhibit bacterial DNA gyrase (topoisomerase II) and topoisomerase IV, preventing DNA supercoiling and replication", "Bacterial DNA gyrase differs structurally from eukaryotic topoisomerases", "Inhibit human RNA polymerase II, Inhibit eukaryotic histone acetyltransferases, Degrade bacterial 80S ribosomes"),
            ("Macrolides and Aminoglycosides (Erythromycin, Gentamicin)", "Bind selectively to bacterial 70S ribosomes (50S and 30S subunits respectively), halting bacterial translation", "Eukaryotic cytosolic 80S ribosomes are unaffected at therapeutic concentrations", "Degrade host nuclear membranes, Inhibit host cell wall synthesis, Block human microtubule assembly"),
            ("Recombinant protein expression in bacteria (e.g., Human Insulin in E. coli)", "Genetically engineered bacteria lack machinery to splice introns, requiring cDNA (complementary DNA from mature mRNA) for expression", "Bacteria also lack post-translational glycosylation pathways, requiring eukaryotic expression systems (yeast or CHO cells) for complex glycoproteins", "Bacteria reject all eukaryotic genes as foreign, Bacteria translate introns directly into functional proteins, Eukaryotic mRNAs can be inserted directly without cDNA"),
            ("Endotoxin (Lipopolysaccharide - LPS) and Septic Shock", "Gram-negative outer membrane LPS lipid A binds to host TLR4/CD14 receptors on macrophages, triggering massive release of TNF-alpha and IL-1", "Induces systemic vasodilation, capillary leak, disseminated intravascular coagulation (DIC), and septic shock", "Destroys host cell walls, Causes immediate cellular hyperpolarization, Inhibits bacterial binary fission"),
            ("CRISPR-Cas9 adaptive immune system", "Originally evolved as an RNA-guided prokaryotic adaptive immune system against invading bacteriophages and plasmids", "Adapted in biotechnology as a revolutionary tool for targeted eukaryotic genome editing", "Bacterial mechanism for protein degradation in lysosomes, Eukaryotic system for repairing telomeres, Viral mechanism for synthesizing RNA"),
            ("Bacterial polycistronic mRNA vs Eukaryotic monocistronic mRNA", "Prokaryotic operons produce single polycistronic mRNAs encoding multiple distinct enzymes; Eukaryotic mRNAs encode single polypeptides", "Allows bacteria to coordinate expression of entire metabolic pathways (e.g., lac operon: lacZ, lacY, lacA)", "Eukaryotic mRNAs encode entire chromosomes, Bacteria require separate mRNAs for every subunit, Both produce identical tricistronic mRNAs"),
            ("Mitochondrial toxicity of certain antibiotics", "Prolonged high-dose use of chloramphenicol, linezolid, or aminoglycosides can inhibit mitochondrial 70S ribosomes, causing ototoxicity or bone marrow suppression", "Direct consequence of the endosymbiotic prokaryotic ancestry of mitochondria", "Due to antibiotic binding to nuclear DNA, Caused by destruction of eukaryotic plasma membrane, Result of bacterial cell wall accumulation"),
            ("Polymyxins (Colistin) mechanism of action", "Disrupts outer membrane of Gram-negative bacteria by binding to lipid A and displacing divalent cations (\\(\\text{Ca}^{2+}, \\text{Mg}^{2+}\\))", "Acts like a detergent to permeabilize bacterial membranes; last-resort drug for multidrug-resistant pathogens", "Blocks 80S ribosome elongation, Destroys bacterial nucleolus, Inhibits eukaryotic dynein motors"),
            ("Gram-stain differential mechanism (Crystal Violet & Iodine)", "Gram-positive retain crystal violet-iodine complex after alcohol wash due to thick dehydrated peptidoglycan; Gram-negative decolorize and counterstain pink with safranin", "Alcohol dissolves lipid outer membrane and leaches dye from thin peptidoglycan layer of Gram-negative cells", "Gram-negative cells lack a cell wall, Gram-positive cells have lipid outer membranes that trap safranin, Gram-stain binds exclusively to bacterial DNA")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Clinical & Pharmacological Exploitation.**\n- Selective toxicity targets structures unique to bacteria (peptidoglycan wall, 70S ribosomes, DNA gyrase, LPS).\n- Human host cells lack these structures, minimizing adverse drug effects.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Biomedical Consequence:**\n{item[2]}."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-2-2.3.2", "Prokaryotic vs Eukaryotic cell comparison", archs)


# ==========================================
# 2.3.3: Endoplasmic Reticulum, Golgi apparatus, Lysosomes, Mitochondria, Plastids, Vacuoles
# ==========================================
def gen_2_3_3():
    # Arch 1: Endoplasmic Reticulum (RER vs SER structure and functions)
    arch1 = {
        'templates': [
            "What is the distinct structure and physiological function of: '{0}'?:",
            "In eukaryotic cytology: '{0}' is characterized by:",
            "Consider the endoplasmic reticulum architecture: '{0}' plays a vital role in:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A cell biologist investigates intracellular membranes: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does the cell utilize '{0}' to maintain metabolic homeostasis?:",
            "Evaluate the biochemical activity associated with: '{0}':",
            "Why is '{0}' abundant in specialized secretory or detoxification tissues?:",
            "What functional feature distinguishes: '{0}'?:"
        ],
        'data': [
            ("Rough Endoplasmic Reticulum (RER)", "Flattened, interconnected sac-like cisternae studded with ribosomes on its outer cytoplasmic surface", "Engaged in synthesis, co-translational translocation, and initial folding/glycosylation of secretable and membrane proteins", "Smooth tubular network synthesizing steroid lipids, Free-floating vesicles storing glycogen, Double-membraned organelle synthesizing ATP"),
            ("Smooth Endoplasmic Reticulum (SER)", "Tubular branching membrane network devoid of ribosomes", "Major site for synthesis of lipids (phospholipids, cholesterol), steroid hormones, and detoxification of drugs and poisons", "Flattened cisternae synthesizing ribosomal RNAs, Site of protein translation and secretion, Digestive organelle containing acid hydrolases"),
            ("Sarcoplasmic Reticulum in muscle fibers", "Specialized smooth endoplasmic reticulum that stores and rapidly releases calcium ions (\\(\\text{Ca}^{2+}\\)) to trigger muscle contraction", "Pumps \\(\\text{Ca}^{2+}\\) back into lumen via SERCA pumps to induce muscle relaxation", "Synthesizes actin and myosin filaments, Generates ATP via oxidative phosphorylation, Forms the outer sarcolemma barrier"),
            ("Hepatic SER and Cytochrome P450 detoxification", "Liver smooth ER is richly endowed with cytochrome P450 monooxygenases that convert hydrophobic drugs and toxins into water-soluble excretable forms", "Undergoes dramatic proliferation upon chronic exposure to lipophilic compounds (e.g., phenobarbital, alcohol)", "Degrades proteins into free amino acids, Synthesizes digestive enzymes for the stomach, Stores bile acids in crystalline form"),
            ("Chaperones and protein quality control in RER (BiP / Calnexin)", "Molecular chaperones that assist proper folding of nascent polypeptide chains and retain misfolded proteins", "Misfolded proteins undergo ER-associated degradation (ERAD) via retrotranslocation to cytoplasmic proteasomes", "Directly secrete misfolded proteins into blood, Inactivate viral capsids by phosphorylation, Synthesize phospholipid bilayers"),
            ("Co-translational translocation (Signal Peptide & SRP)", "Hydrophobic N-terminal signal peptides are recognized by Signal Recognition Particle (SRP), docking ribosome at the RER translocon (Sec61)", "Directs polypeptide elongation directly into the lumen of the RER", "Targets proteins to the nucleolus, Transports mRNAs directly into mitochondria, Transports ribosomes to the plasma membrane"),
            ("Initial N-linked Glycosylation in RER", "En bloc transfer of a preformed 14-sugar oligosaccharide (\\(\\text{Glc}_3\\text{Man}_9\\text{GlcNAc}_2\\)) from dolichol phosphate to asparagine (Asn-X-Ser/Thr)", "Crucial for protein folding, stability, and recognition in the secretory pathway", "Addition of glucose to lipid fatty acid tails, Phosphorylation of nuclear lamins, Attachment of sialic acid in the nucleoplasm"),
            ("Continuity of ER with Nuclear Envelope", "The outer nuclear membrane is directly continuous with the cisternae of the rough endoplasmic reticulum", "Shares a continuous luminal space, facilitating shared lipid and protein membrane synthesis", "Connected only via open gap junctions, Formed by fusion of mitochondrial outer membranes, Artifact of chemical fixation"),
            ("Unfolded Protein Response (UPR)", "Cellular stress response triggered by accumulation of unfolded/misfolded proteins in ER lumen", "Upregulates chaperone expression, reduces general translation, and triggers apoptosis if ER stress is prolonged", "Triggers immediate rapid binary fission, Increases glycogen synthesis in cytoplasm, Causes permanent loss of nuclear envelope"),
            ("Transitional ER (tER)", "Specialized ribosome-free regions of RER where COPII-coated transport vesicles bud off carrying cargo to the cis-Golgi", "Marks the initial exit gateway of the secretory pathway", "Site where lysosomes fuse with endosomes, Region where ribosomes assemble 60S subunits, Site where mitochondria attach to ER")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Endoplasmic Reticulum Structure & Roles.**\n- RER: Studded with ribosomes, cisternae, protein synthesis (secretory, lysosomal, membrane), folding, N-glycosylation.\n- SER: Tubular, no ribosomes, lipid & steroid synthesis, drug detoxification (P450 in liver), \\(\\text{{Ca}}^{{2+}}\\) storage (sarcoplasmic reticulum).\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Mechanistic Details:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 2: Golgi Apparatus (Polarity, Protein Processing, and Vesicle Trafficking)
    arch2 = {
        'templates': [
            "What is the structural organization and function of: '{0}'?:",
            "In eukaryotic protein sorting and processing: '{0}' is characterized by:",
            "Consider the Golgi apparatus: '{0}' plays a pivotal role in:",
            "Which statement precisely describes the function of: '{0}'?:",
            "A cell biologist traces protein secretion: '{0}'. What is true?:",
            "Identify the accurate fact regarding the Golgi complex: '{0}':",
            "How does the Golgi apparatus utilize '{0}' to direct intracellular traffic?:",
            "Evaluate the biochemical modification occurring at: '{0}':",
            "Why is '{0}' vital for cellular secretion and lysosome biogenesis?:",
            "What architectural feature defines: '{0}'?:"
        ],
        'data': [
            ("Golgi apparatus (Golgi complex / Dictyosome)", "A stack of curved, membrane-bound flattened cisternae (\\(4\\text{ to }8\\text{ cisternae}\\)) discovered by Camillo Golgi (1898) using silver nitrate staining", "Acts as the central sorting, packaging, and dispatching factory of the eukaryotic endomembrane system", "A network of branching tubules synthesizing steroid hormones, A double-membraned organelle generating ATP, A non-membrane bound RNA granule"),
            ("Cis-Golgi network (CGN / Entry face)", "Convex cisternae facing the rough ER and nuclear envelope that receive cargo vesicles from transitional ER", "Vesicles fuse with CGN; proteins and lipids begin post-translational processing", "Concave cisternae budding secretory granules to plasma membrane, Site where acid hydrolases are degraded, Bounded by double lipid bilayer with nuclear pores"),
            ("Trans-Golgi network (TGN / Exit face)", "Concave cisternae facing the plasma membrane that sort and package proteins into distinct transport vesicles", "Dispatches vesicles targeted to lysosomes, secretory granules (regulated exocytosis), or plasma membrane (constitutive exocytosis)", "Entry face receiving COPII vesicles from RER, Non-membrane protein shell in cytoplasm, Storage site for glycogen granules"),
            ("Medial Golgi cisternae", "Central cisternae where oligosaccharide chains undergo sequential enzymatic remodeling (removal of mannose, addition of GlcNAc, galactose, sialic acid)", "Contains specific glycosyltransferases organized in strict polarity from cis to trans", "Site where fatty acids undergo beta-oxidation, Site of ribosomal RNA synthesis, Storage reservoir for calcium ions"),
            ("Mannose-6-Phosphate (M6P) tagging", "Specific phosphorylation of mannose residues on lysosomal enzymes occurring in the cis-Golgi", "M6P receptors in the TGN package these acid hydrolases into clathrin-coated vesicles destined for lysosomes", "Targets proteins to mitochondrial matrix, Signal targeting proteins into the nucleolus, Tag that causes rapid proteasomal degradation"),
            ("COPI vs COPII coated vesicles", "COPII mediates anterograde transport from RER to cis-Golgi; COPI mediates retrograde transport from Golgi back to ER (retrieval pathway)", "COPI retrieves ER-resident proteins carrying KDEL or KKXX retention signals", "COPI transports proteins into nucleus, COPII transports ribosomes out of cell, Both coat peroxisomal vesicles only"),
            ("Clathrin-coated vesicles", "Triskelion-structured protein cages that mediate receptor-mediated endocytosis at plasma membrane and vesicle transport from TGN to endosomes/lysosomes", "Disassembled by Hsp70 chaperones after vesicle budding to allow membrane fusion", "Enclose photosynthetic thylakoid membranes, Form the contractile ring during cytokinesis, Synthesize phospholipid bilayers"),
            ("Plant Dictyosomes and Cell Wall synthesis", "In plant cells, separate individual Golgi stacks (dictyosomes) synthesize non-cellulosic cell wall polysaccharides (pectins, hemicelluloses)", "Direct vesicle fusion during telophase forms the phragmoplast and cell plate", "Synthesize crystalline cellulose microfibrils directly, Degrade plant cell walls during turgor changes, Inactive during plant cell division"),
            ("Acroblast / Acrosome formation in spermiogenesis", "The Golgi apparatus of developing spermatids transforms into the acrosome, a cap-like lysosomal vesicle over the sperm nucleus", "Contains hyaluronidase and acrosin to digest the egg's zona pellucida during fertilization", "Transforms into the sperm flagellum, Forms the midpiece mitochondria, Disappears completely during sperm maturation"),
            ("Constitutive vs Regulated Exocytosis", "Constitutive exocytosis is continuous and unregulated (supplying plasma membrane lipids and extracellular matrix); Regulated exocytosis requires a specific extracellular trigger (e.g., \\(\\text{Ca}^{2+}\\) influx releasing insulin or neurotransmitters)", "Regulated secretory vesicles are stored at the cell periphery until stimulation", "Constitutive exocytosis occurs only in bacteria, Regulated exocytosis lacks vesicle fusion, Both release acid hydrolases into cytoplasm")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Golgi Complex Organization & Trafficking.**\n- Discovered by Camillo Golgi (1898); polarity: Cis face (receiving from ER) \\(\\rightarrow\\) Medial cisternae (glycosylation/remodeling) \\(\\rightarrow\\) Trans face (sorting & dispatch).\n- M6P tag directs lysosomal enzymes; COPII anterograde, COPI retrograde.\n\n**Step 2: Analyze '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Physiological Details:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Lysosomes, Peroxisomes, and Intracellular Digestion
    arch3 = {
        'templates': [
            "What is the biochemical property and physiological role of: '{0}'?:",
            "In cellular catabolism and pathology: '{0}' is characterized by:",
            "Consider lysosomal biology: '{0}' is defined as:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A pathology resident examines cellular degradation: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does the cell utilize '{0}' to dispose of waste or defend against pathogens?:",
            "Evaluate the clinical or biological impact of: '{0}':",
            "Why is '{0}' termed the 'suicide bag' or digestive hub of the cell?:",
            "What biochemical feature characterizes: '{0}'?:"
        ],
        'data': [
            ("Lysosomes (Suicide bags)", "Single-membrane bound spherical vesicles containing \\(\\approx 50\\) different acid hydrolases active at acidic pH (\\(4.5\\text{--}5.0\\))", "Discovered by Christian de Duve (1955); digest extracellular materials (heterophagy) and worn-out organelles (autophagy)", "Double-membraned organelles producing ATP, Non-membrane bound protein factories synthesizing RNA, Alkaline vesicles storing starch"),
            ("Vacuolar \\(\\text{H}^+\\)-ATPase (V-ATPase) proton pump", "Electrogenic proton pump in the lysosomal membrane that hydrolyzes ATP to pump \\(\\text{H}^+\\) into the lumen, maintaining pH \\(\\approx 4.5\\text{--}5.0\\)", "Safeguards the cell: if a lysosome ruptures, acid hydrolases are largely inactive at the neutral pH (\\(\\approx 7.2\\)) of cytosol", "Synthesizes ATP by pumping protons out of lysosomes, Pumps sodium ions to keep lumen alkaline, Replicates lysosomal circular DNA"),
            ("Primary lysosome vs Secondary lysosome (Phagolysosome)", "Primary lysosomes are newly budded vesicles containing inactive enzymes; Secondary lysosomes are formed by fusion with phagosomes/endosomes where active digestion occurs", "Secondary lysosomes contain active substrate degradation products", "Primary lysosomes contain living bacteria, Secondary lysosomes lack enzymes entirely, Primary lysosomes are found only in plant cell walls"),
            ("Autophagy and Autophagosomes", "Process where a double-membraned crescent (phagophore) engulfs damaged organelles (e.g., old mitochondria) and fuses with lysosomes for recycling", "Yoshinori Ohsumi won the 2016 Nobel Prize for elucidating autophagy genes (ATG); crucial for starvation survival and clearing aggregates", "Spontaneous explosive lysis destroying the whole tissue, Uptake of extracellular fluid by pinocytosis, Synthesis of new organelles from amino acids"),
            ("Autolysis in programmed cell death", "Massive synchronous rupture of all lysosomes in a dying or damaged cell, releasing acid hydrolases that digest the entire cell", "Occurs during developmental tissue remodeling (e.g., resorption of tadpole tail during amphibian metamorphosis)", "Normal physiological process occurring during every S-phase, Bacterial invasion mechanism, Mitotic division of chromosomes"),
            ("Tay-Sachs disease (Lysosomal Storage Disease)", "Autosomal recessive deficiency of beta-hexosaminidase A, leading to toxic accumulation of GM2 gangliosides in neuronal lysosomes", "Causes progressive neurodegeneration, developmental regression, blindness, cherry-red macular spot, and early childhood death", "Excessive accumulation of glycogen in liver mitochondria, Inability to synthesize insulin in RER, Failure of peroxisomal catalase"),
            ("Gaucher disease and Niemann-Pick disease", "Gaucher: deficiency of glucocerebrosidase accumulating glucosylceramide; Niemann-Pick: deficiency of sphingomyelinase accumulating sphingomyelin", "Lead to massive hepatosplenomegaly, bone crises, and progressive neurological impairment", "Deficiencies in mitochondrial ATP synthase, Complete absence of Golgi apparatus, Hyperactivity of ribosomes in cytoplasm"),
            ("Residual bodies (Telolysosomes / Lipofuscin)", "Lysosomes containing undigested debris that remain in the cytoplasm; in long-lived post-mitotic cells (neurons, cardiac myocytes), accumulates as lipofuscin ('age pigment')", "Indicates cumulative oxidative stress and cellular aging over decades", "Vesicles secreting collagen into bone matrix, Precursor vesicles forming new centrioles, Storage granules for active digestive enzymes"),
            ("Peroxisomes (Microbodies) and Catalase", "Single-membraned organelles containing oxidases producing toxic hydrogen peroxide (\\(\\text{H}_2\\text{O}_2\\)) and catalase which decomposes it: \\(2\\text{H}_2\\text{O}_2 \\rightarrow 2\\text{H}_2\\text{O} + \\text{O}_2\\)", "Perform beta-oxidation of very long-chain fatty acids (VLCFAs, \\(> \\text{C}_{22}\\)) and plasmalogen phospholipid synthesis", "Synthesize major ribosomal subunits, Generate ATP by oxidative phosphorylation, Digest foreign bacteria via acid hydrolases"),
            ("Zellweger syndrome", "Lethal congenital disorder caused by mutations in PEX genes required for peroxisomal protein import, resulting in 'empty' non-functional peroxisomes", "Causes severe neurological impairment, craniofacial dysmorphism, hepatomegaly, and accumulation of VLCFAs in blood", "Nutritional deficiency of catalase, Autoimmune attack destroying lysosomes, Failure of nuclear envelope reassembly")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Lysosome & Peroxisome Biology.**\n- Lysosomes: Discovered by Christian de Duve; single membrane, V-ATPase maintains pH \\(4.5\\text{{--}}5.0\\), acid hydrolases (heterophagy, autophagy, autolysis).\n- Peroxisomes: Catalase decomposes \\(\\text{{H}}_2\\text{{O}}_2\\); \\(\\beta\\)-oxidation of VLCFAs. Zellweger syndrome: PEX defect.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Pathophysiology & Details:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Mitochondria (Double Membrane, Cristae, Matrix, and Bioenergetics)
    arch4 = {
        'templates': [
            "What is the structural feature and biochemical role of: '{0}'?:",
            "In mitochondrial biology and cellular respiration: '{0}' is characterized by:",
            "Consider the mitochondrial architecture: '{0}' is essential for:",
            "Which statement precisely describes: '{0}'?:",
            "A biochemistry student examines oxidative phosphorylation: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does the mitochondrion utilize '{0}' to generate cellular energy?:",
            "Evaluate the biochemical activity occurring in: '{0}':",
            "Why is '{0}' termed the 'powerhouse of the cell'?:",
            "What structural component corresponds to: '{0}'?:"
        ],
        'data': [
            ("Mitochondrion (Powerhouse of the cell)", "Double-membraned semiautonomous organelle that generates the vast majority of cellular ATP via oxidative phosphorylation", "First observed by Kolliker (1857), termed 'bioblasts' by Altmann (1890), and named 'mitochondria' by Carl Benda (1898)", "Single-membraned vesicle storing starch, Organelle synthesizing digestive enzymes, Non-membrane bound nucleoprotein complex"),
            ("Mitochondrial outer membrane and Porins", "Smooth outer membrane containing large transmembrane channel proteins (porins) permeable to molecules up to \\(\\approx 5,000\\text{ Da}\\)", "Allows free diffusion of ions, metabolites (ADP, ATP, pyruvate), and small cofactors into the intermembrane space", "Impermeable to all ions requiring active sodium pumps, Lined with electron transport chain complexes, Continuous with the nuclear lamina"),
            ("Intermembrane space and Cytochrome c", "Aqueous compartment between outer and inner membranes into which protons (\\(\\text{H}^+\\)) are pumped by complexes I, III, and IV", "Reservoir for cytochrome c; its leakage into cytosol triggers the intrinsic apoptosis pathway via apoptosome assembly", "Site where Krebs cycle occurs, Fluid containing 80S ribosomes, Alkaline compartment of pH 9.0"),
            ("Mitochondrial inner membrane and Cristae", "Extensively folded into finger-like or shelf-like cristae to dramatically increase surface area for ATP synthase and electron transport complexes", "Cardiolipin-rich membrane that is strictly impermeable to ions, maintaining the proton-motive force", "Smooth permeable membrane containing porins, Site of fatty acid synthesis, Bounded by peptidoglycan"),
            ("Mitochondrial Matrix", "Dense aqueous gel-like core containing Krebs cycle enzymes, pyruvate dehydrogenase, 70S ribosomes, and circular mtDNA", "Site of beta-oxidation of fatty acids and substrate-level phosphorylation (succinyl-CoA synthetase)", "Acidic chamber of pH 4.0 containing digestive hydrolases, Pure water devoid of proteins, Site of light-dependent photosynthetic reactions"),
            ("Mitochondrial DNA (mtDNA)", "Small, double-stranded, circular DNA molecule replicating independently of nuclear DNA by binary fission", "In humans, encodes 13 essential polypeptide subunits of respiratory complexes, 22 tRNAs, and 2 rRNAs (maternally inherited)", "Linear double-stranded chromosome packaged with histones, Single-stranded viral RNA molecule, Plasmid encoding antibiotic resistance only"),
            ("F0-F1 ATP Synthase (Complex V)", "Mushroom-shaped rotary motor on inner membrane: \\(\\text{F}_0\\) stalk channels protons across membrane; \\(\\text{F}_1\\) catalytic head synthesizes ATP from ADP + Pi", "Driven by proton-motive force (\\(\\Delta p = \\Delta\\psi + \Delta\\text{pH}\\)) according to Peter Mitchell's Chemiosmotic Hypothesis", "Pumps electrons into the matrix using ATP hydrolysis, Transports pyruvic acid out of mitochondria, Degrades ATP into AMP during starvation"),
            ("Maternal inheritance of mitochondria", "In human fertilization, sperm mitochondria located in the midpiece are flagged with ubiquitin and degraded in the fertilized oocyte", "All human mtDNA is inherited exclusively from the biological mother, used in matrilineal genealogical tracing", "mtDNA is inherited exclusively from the father, Inherited equally 50% from mother and 50% from father, Formed de novo from maternal egg ribosomes"),
            ("Mitochondrial myopathies (e.g., MERRF, MELAS)", "Disorders caused by point mutations in mitochondrial tRNA or subunit genes, predominantly affecting high-energy tissues (brain, skeletal/cardiac muscle)", "Manifest with muscle weakness, exercise intolerance, lactic acidosis, strokes, and ragged-red muscle fibers on biopsy", "Curable with oral penicillin, Caused by lack of dietary vitamins, Diseases of the endoplasmic reticulum"),
            ("Mitochondria-driven intrinsic apoptosis", "Pro-apoptotic proteins (Bax/Bak) oligomerize in outer membrane, releasing cytochrome c into cytosol to bind Apaf-1 and activate caspase-9", "Executes programmed cell death without provoking inflammatory tissue damage", "Triggers immediate cell swelling and necrotic rupture, Causes rapid replication of mitochondrial DNA, Stimulates massive ATP overproduction")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Mitochondrial Organization & Energetics.**\n- Double membrane: Outer (porins), Intermembrane space (\\(\\text{{H}}^+\\) reservoir, cytochrome c), Inner (cristae, cardiolipin, ETC complexes I-IV, \\(\\text{{F}}_0\\text{{-F}}_1\\) ATP synthase).\n- Matrix: Krebs cycle, \\(\\beta\\)-oxidation, circular mtDNA, 70S ribosomes (maternal inheritance).\n\n**Step 2: Analyze '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Bioenergetic / Clinical Details:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Plastids (Chloroplasts, Chromoplasts, Leucoplasts)
    arch5 = {
        'templates': [
            "What is the classification, structure, or function of: '{0}'?:",
            "In plant cell biology: '{0}' is characterized by:",
            "Consider plastid biology: '{0}' is distinguished by:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A botanist investigates plant pigments and storage: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How do plant cells utilize '{0}' for photosynthesis or metabolic storage?:",
            "Evaluate the biochemical feature of: '{0}':",
            "Why is '{0}' vital for plant physiology and autotrophic nutrition?:",
            "What structural component corresponds to: '{0}'?:"
        ],
        'data': [
            ("Chloroplast (Kitchen of the cell)", "Double-membraned semiautonomous photosynthetic organelle found in green plant cells and algae", "Contains light-capturing chlorophyll pigments and enzymes to convert solar energy, \\(\\text{CO}_2\\), and \\(\\text{H}_2\\text{O}\\) into glucose", "Single-membraned vesicle storing starch, Non-membrane bound protein granule, Animal organelle producing melanin pigments"),
            ("Thylakoids and Grana", "Flattened disc-like membranous sacs (thylakoids) stacked like piles of coins into grana (singular: granum)", "Thylakoid membranes contain Photosystems I and II, electron transport chains, and ATP synthase for light reactions", "Site of the dark reactions and Calvin cycle, Compartments where starch is synthesized, Outer membrane extensions of the chloroplast"),
            ("Stroma of chloroplast", "Homogeneous, proteinaceous fluid matrix surrounding grana, analogous to the mitochondrial matrix", "Contains circular cpDNA, 70S ribosomes, and soluble Calvin cycle enzymes (e.g., RuBisCO)", "Acidic fluid containing digestive hydrolases, Site where light reactions split water, Bounded by cellulose cell wall"),
            ("Stroma lamellae (Fret membranes)", "Unstacked membranous tubules connecting adjacent grana across the stroma", "Contain predominantly Photosystem I (PS I) and mediate cyclic photophosphorylation", "Sites of Photosystem II water-splitting reactions, Channels for exporting whole chloroplasts, Non-membrane cytoskeletal fibers"),
            ("Chromoplasts", "Non-photosynthetic colored plastids containing fat-soluble carotenoid pigments (carotene, xanthophylls)", "Impart vibrant yellow, orange, and red colors to petals, flowers, and ripe fruits (e.g., lycopene in tomatoes) to attract pollinators and seed dispersers", "Store colorless starches in underground tubers, Photosynthesize actively in deep ocean waters, Contain pure water and anthocyanins"),
            ("Leucoplasts (Amyloplasts, Elaioplasts, Aleuroplasts)", "Colorless plastids specialized for nutrient storage: Amyloplasts store starch; Elaioplasts (lipoplasts) store fats/oils; Aleuroplasts store proteins", "Abundant in non-photosynthetic storage tissues (tubers, seeds, roots)", "Impart bright red colors to flower petals, Contain photosynthetic grana, Digest cellular waste like lysosomes"),
            ("Interconversion of plastids", "Plastids can interconvert depending on developmental cues and environmental light (e.g., chloroplasts turn into chromoplasts during tomato ripening; leucoplasts turn green in light-exposed potatoes)", "All plastid types differentiate from undifferentiated proplastids found in meristematic tissues", "Plastids are rigid permanent structures that never alter their pigment content, Chloroplasts convert directly into mitochondria, Chromoplasts turn into lysosomes"),
            ("Chloroplast DNA (cpDNA)", "Circular double-stranded DNA molecule present in multiple copies per chloroplast, encoding \\(\\approx 120\\) genes", "Encodes large subunit of RuBisCO, ribosomal RNAs, tRNAs, and key photosystem reaction center polypeptides", "Linear chromosome bound with histone H1, Encodes all plant enzymes without needing nuclear genome, Single-stranded RNA molecule"),
            ("RuBisCO (Ribulose-1,5-bisphosphate carboxylase/oxygenase)", "Most abundant enzyme on Earth, located in chloroplast stroma, catalyzing initial \\(\\text{CO}_2\\) fixation in the Calvin cycle", "Composed of 8 large subunits (encoded by cpDNA) and 8 small subunits (encoded by nuclear DNA)", "Enzyme in thylakoid membrane that splits water, Mitochondrial enzyme in Krebs cycle, Lysosomal hydrolase"),
            ("Anthocyanin pigments vs Carotenoid pigments", "Anthocyanins are water-soluble flavonoid pigments dissolved in the central vacuole sap (imparting purple/blue/red); Carotenoids are lipid-soluble pigments localized in plastid membranes", "Vacuolar anthocyanin color shifts with cellular pH (red in acid, blue in base); plastid carotenoids do not", "Anthocyanins are synthesized in mitochondria, Carotenoids dissolve in nucleoplasm, Both are stored in chloroplast stroma")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Plastid Classification & Structure.**\n- Plastids: Proplastids \\(\\rightarrow\\) Chloroplasts (chlorophyll, grana/stroma, photosynthesis), Chromoplasts (carotenoids/xanthophylls, color in fruits/flowers), Leucoplasts (colorless storage: Amyloplasts=starch, Elaioplasts=oils, Aleuroplasts=protein).\n- Thylakoids (light reactions), Stroma (Calvin cycle, RuBisCO, 70S ribosomes, circular cpDNA).\n\n**Step 2: Analyze '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Physiological Details:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Vacuoles (Central Vacuole, Tonoplast, Contractile and Food Vacuoles)
    arch6 = {
        'templates': [
            "What is the structural feature and physiological role of: '{0}'?:",
            "In plant and protistan cell biology: '{0}' is characterized by:",
            "Consider vacuolar biology: '{0}' is essential for:",
            "Which statement precisely describes the nature of: '{0}'?:",
            "A student examines a mature plant cell under microscopy: '{0}'. What is true?:",
            "Identify the accurate fact regarding: '{0}':",
            "How does the cell utilize '{0}' to maintain turgidity or osmotic equilibrium?:",
            "Evaluate the biochemical feature of: '{0}':",
            "Why is '{0}' vital for freshwater protozoan survival?:",
            "What functional feature distinguishes: '{0}'?:"
        ],
        'data': [
            ("Central sap vacuole in plant cells", "Large membrane-bound fluid-filled compartment occupying up to \\(90\\%\\) of a mature plant cell's volume", "Contains cell sap (water, mineral salts, sugars, organic acids, toxic excretory waste products, and water-soluble anthocyanin pigments)", "Small temporary vesicle storing digestive enzymes, Double-membraned organelle generating ATP, A non-membrane bound lipid crystal"),
            ("Tonoplast (Vacuolar membrane)", "Semi-permeable single membrane enclosing the plant central vacuole", "Contains active transport proton pumps and antiporters (e.g., \\(\\text{Na}^+/\\text{H}^+\\) antiporter) that concentrate solutes against steep concentration gradients into the vacuole", "Impermeable double lipid bilayer continuous with nuclear envelope, Peptidoglycan cell wall boundary, Free-floating protein coat in cytoplasm"),
            ("Turgor pressure and plant mechanical support", "High osmotic concentration of solutes in the vacuole draws water in by endosmosis, pressing cytoplasm against rigid cell wall (turgor pressure)", "Maintains mechanical rigidity in herbaceous stems and leaves, preventing wilting; loss of turgor causes plasmolysis", "Pushes cell wall inward causing cell collapse, Neutralizes all intracellular solutes, Prevents photosynthesis"),
            ("Contractile vacuole in Amoeba / Paramecium", "Specialized osmoregulatory organelle in freshwater protists that collects excess water entering by osmosis and expels it periodically via exocytosis", "Prevents hypotonic lysis of wall-less freshwater organisms; cycle involves diastolic filling and systolic emptying", "Digests engulfed bacterial food particles, Synthesizes cellulose cell wall, Generates ATP via oxidative phosphorylation"),
            ("Food vacuole in Amoeba (Phagosome)", "Formed when Amoeba engulfs food particles (e.g., algae, bacteria) by pseudopodial phagocytosis; fuses with lysosomes for digestion", "Nutrients are absorbed into cytoplasm, and undigested waste is egested by exocytosis", "Permanent central vacuole maintaining turgor pressure, Organelle carrying out photosynthesis, Storage vesicle for calcium ions"),
            ("Gas vacuoles in aquatic prokaryotes", "Non-membrane bound aggregates of hollow cylindrical protein sub-units (gas vesicles) impermeable to water but freely permeable to atmospheric gases", "Provide buoyancy to photosynthetic bacteria (cyanobacteria, purple/green sulfur bacteria) to position them in optimal light zones", "Membrane-bound organelles containing cell sap, True plant vacuoles storing starch, Toxic waste storage vesicles"),
            ("Vacuolar role in waste storage and secondary metabolites", "Plants lack specialized excretory organs; toxic metabolic wastes (calcium oxalate crystals, tannins, resins, alkaloids like nicotine/caffeine) are sequestered safely inside the central vacuole", "Prevents toxic metabolites from inhibiting metabolic enzymes in the cytoplasm", "Wastes are immediately pumped out into soil, Wastes are converted into ATP, Central vacuole exports wastes into phloem"),
            ("Anthocyanin pigments in vacuolar sap", "Water-soluble flavonoid pigments stored in the central vacuole imparting blue, purple, magenta, or red colors to petals and fruits (e.g., beetroot, red cabbage)", "Color changes with vacuolar pH: acidic pH yields bright red, while alkaline pH shifts to blue-green", "Lipid-soluble pigments located in chloroplast grana, Synthesized exclusively in mitochondria, Bound permanently to the cell wall"),
            ("Lytic vacuoles in fungi and plants", "Functionally equivalent to animal lysosomes, containing acid hydrolases (proteases, nucleases, glycosidases) to degrade macromolecules", "Participate in vegetative cellular remodeling, senescence, and defense against fungal pathogens", "Synthesize glycogen from sucrose, Replicate circular DNA molecules, Pump water out like contractile vacuoles"),
            ("Plasmolysis and the Central Vacuole", "When a plant cell is placed in a hypertonic solution, water leaves the central vacuole by exosmosis, causing the protoplast to shrink away from the rigid cell wall", "The space between cell wall and shrunken protoplast is filled with external hypertonic solution", "Causes the cell wall to burst violently, The central vacuole swells to fill 100% of cell, Plasmolysis occurs in pure distilled water")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Vacuolar Structure & Roles.**\n- Plants: Central sap vacuole (up to 90% volume), Tonoplast (active transport, turgor pressure), stores cell sap, waste, anthocyanins.\n- Protists: Contractile vacuole (osmoregulation in freshwater), Food vacuole (phagocytosis/digestion).\n- Bacteria: Gas vacuoles (proteinaceous gas vesicles, buoyancy).\n\n**Step 2: Analyze '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Functional / Physiological Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Quantitative and Bioenergetic Organelle Calculations
    arch7 = {
        'templates': [
            "{0}:",
            "Calculate the organelle cellular metric: {0}:",
            "A quantitative cell biology problem: {0}:",
            "Solve the bioenergetic organelle calculation: {0}:",
            "Compute the following physiological quantity: {0}:",
            "Analyze the numerical organelle question: {0}:",
            "Determine the correct calculated parameter: {0}:",
            "An analytical bioenergetics problem: {0}:",
            "Find the accurate quantity for: {0}:",
            "Quantitative cytology evaluation: {0}:"
        ],
        'data': [
            ("If a single mitochondrion consumes \\(1.0 \\times 10^{-15}\\text{ moles of }\\text{O}_2\\) per minute and synthesizes \\(5.0\\text{ ATP molecules}\\) per \\(\\text{O}_2\\) molecule, how many ATP molecules are produced by a liver cell containing 2,000 mitochondria in 1 hour?", "\\(\\approx 3.61 \\times 10^{14}\\text{ ATP molecules}\\)", "Moles \\(\\text{O}_2\\) in 1 hr \\(= 10^{-15} \\times 60 \\times 2,000 = 1.2 \\times 10^{-10}\\text{ mol}\\). Molecules \\(\\text{O}_2 = 1.2 \\times 10^{-10} \\times 6.022 \\times 10^{23} \\approx 7.23 \\times 10^{13}\\). ATP \\(= 7.23 \\times 10^{13} \\times 5 = 3.61 \\times 10^{14}\\)", "\\(\\approx 3.61 \\times 10^{12}\\), \\(\\approx 7.23 \\times 10^{14}\\), \\(\\approx 1.80 \\times 10^{13}\\)"),
            ("A plant cell has volume \\(64,000\\text{ }\\mu\\text{m}^3\\). If its central vacuole occupies \\(85\\%\\) of the cell volume, what is the volume of the central vacuole and the remaining cytoplasm?", "Vacuole: \\(54,400\\text{ }\\mu\\text{m}^3\\); Cytoplasm: \\(9,600\\text{ }\\mu\\text{m}^3\\)", "Vacuole volume \\(= 0.85 \\times 64,000 = 54,400\\text{ }\\mu\\text{m}^3\\). Cytoplasm volume \\(= 64,000 - 54,400 = 9,600\\text{ }\\mu\\text{m}^3\\)", "Vacuole: 50,000 μm^3; Cytoplasm: 14,000 μm^3, Vacuole: 60,000 μm^3; Cytoplasm: 4,000 μm^3, Vacuole: 45,000 μm^3; Cytoplasm: 19,000 μm^3"),
            ("If a spherical lysosome has diameter \\(0.5\\text{ }\\mu\\text{m}\\) (radius \\(r = 0.25\\text{ }\\mu\\text{m}\\)), what is its volume in liters (\\(1\\text{ }\\mu\\text{m}^3 = 10^{-15}\\text{ liters}\\))?", "\\(6.54 \\times 10^{-17}\\text{ liters}\\)", "\\(V = \\frac{4}{3}\\pi r^3 = \\frac{4}{3}\\pi (0.25)^3 \\approx 0.0654\\text{ }\\mu\\text{m}^3\\). In liters: \\(0.0654 \\times 10^{-15} = 6.54 \\times 10^{-17}\\text{ L}\\)", "\\(6.54 \\times 10^{-15}\\text{ L}\\), \\(6.54 \\times 10^{-18}\\text{ L}\\), \\(1.31 \\times 10^{-16}\\text{ L}\\)"),
            ("At pH 5.0, \\([\\text{H}^+] = 10^{-5}\\text{ M}\\). In a lysosome of volume \\(6.54 \\times 10^{-17}\\text{ liters}\\), how many free hydronium ions (\\(\\text{H}^+\\)) are present at any given instant?", "\\(\\approx 394\\text{ free }\\text{H}^+\\text{ ions}\\)", "Moles \\(\\text{H}^+ = 10^{-5}\\text{ mol/L} \\times 6.54 \\times 10^{-17}\\text{ L} = 6.54 \\times 10^{-22}\\text{ mol}\\). Ions \\(= 6.54 \\times 10^{-22} \\times 6.022 \\times 10^{23} \\approx 394\\)", "\\(\\approx 3,940\\), \\(\\approx 39\\), \\(\\approx 39,400\\)"),
            ("A chloroplast has 50 grana, each containing 20 stacked thylakoid discs. If each thylakoid disc has a membrane surface area of \\(0.8\\text{ }\\mu\\text{m}^2\\), what is the total photosynthetic thylakoid membrane area in this chloroplast?", "\\(800\\text{ }\\mu\\text{m}^2\\)", "Total thylakoid discs \\(= 50 \\times 20 = 1,000\\). Total membrane area \\(= 1,000 \\times 0.8\\text{ }\\mu\\text{m}^2 = 800\\text{ }\\mu\\text{m}^2\\)", "80 μm^2, 8,000 μm^2, 400 μm^2"),
            ("If a pancreatic acinar cell synthesizes \\(5.0 \\times 10^6\\) digestive enzyme molecules per minute, each averaging \\(400\\text{ amino acids}\\), and translation proceeds at \\(5\\text{ amino acids/sec/ribosome}\\), how many active ribosomes must be engaged on the RER?", "\\(6.67 \\times 10^6\\text{ ribosomes}\\)", "Total amino acids/min \\(= 5 \\times 10^6 \\times 400 = 2.0 \\times 10^9\\). Amino acids/sec \\(= 2.0 \\times 10^9 / 60 = 3.33 \\times 10^7\\). Ribosomes required \\(= 3.33 \\times 10^7 / 5 \\approx 6.67 \\times 10^6\\)", "\\(1.33 \\times 10^6\\), \\(3.33 \\times 10^6\\), \\(1.00 \\times 10^7\\)"),
            ("A contractile vacuole in Paramecium fills and empties every 15 seconds. If each discharge expels \\(40\\text{ }\\mu\\text{m}^3\\) of fluid, how much fluid is expelled per hour?", "\\(9,600\\text{ }\\mu\\text{m}^3\\text{ per hour}\\)", "Discharges per minute \\(= 60 / 15 = 4\\). Discharges per hour \\(= 4 \\times 60 = 240\\). Volume per hour \\(= 240 \\times 40 = 9,600\\text{ }\\mu\\text{m}^3\\)", "4,800 μm^3, 19,200 μm^3, 2,400 μm^3"),
            ("The proton-motive force (\\(\\Delta p\\)) across the inner mitochondrial membrane is \\(\\Delta p = \\Delta\\psi - 59\\Delta\\text{pH}\\text{ mV}\\). If the membrane potential \\(\\Delta\\psi = -160\\text{ mV}\\) and the pH inside matrix is 8.0 while intermembrane space is 7.0 (\\(\\Delta\\text{pH} = 1.0\\)), what is \\(\\Delta p\\)?", "\\(-219\\text{ mV}\\)", "\\(\\Delta p = -160\\text{ mV} - (59 \\times 1.0)\\text{ mV} = -160 - 59 = -219\\text{ mV}\\)", "-160 mV, -101 mV, -260 mV"),
            ("Human mitochondrial DNA encodes 13 proteins, 22 tRNAs, and 2 rRNAs (total 37 genes). What is the total number of gene products directly synthesized from the mitochondrial genome?", "37 gene products", "Total functional products \\(= 13 \\text{ polypeptides} + 22 \\text{ tRNAs} + 2 \\text{ rRNAs} = 37\\)", "13 products, 22 products, 46 products"),
            ("If a plant cell has 40 chloroplasts, and each chloroplast contains \\(1.5 \\times 10^6\\) molecules of RuBisCO, how many RuBisCO molecules are present in this single cell?", "\\(6.0 \\times 10^7\\text{ RuBisCO molecules}\\)", "\\(\\text{Total RuBisCO} = 40 \\times 1.5 \\times 10^6 = 6.0 \\times 10^7\\)", "\\(6.0 \\times 10^6\\), \\(6.0 \\times 10^8\\), \\(1.5 \\times 10^7\\)")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Identify given physical/biological quantities.**\n{item[0]}\n\n**Step 2: Apply the governing formula/rate.**\n{item[2]}.\n\n**Step 3: Conclude.**\nResult is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 8: Endomembrane System Coordination and Clinical Disorders
    arch8 = {
        'templates': [
            "Which integrated physiological pathway or disease mechanism explains: '{0}'?:",
            "In clinical cell biology and medicine: '{0}' is characterized by:",
            "What clinical insight is derived from: '{0}'?:",
            "How does the endomembrane system coordinate: '{0}'?:",
            "A medical student examines intracellular transport pathology: '{0}'. What is true?:",
            "Which disease or therapeutic mechanism relates to: '{0}'?:",
            "What is the medical significance of: '{0}'?:",
            "Why is '{0}' considered a coordinated endomembrane network?:",
            "What pathophysiological consequence results from: '{0}'?:",
            "Evaluate the biomedical concept: '{0}':"
        ],
        'data': [
            ("Endomembrane System Definition", "A coordinated system of intracellular membranes (Nuclear envelope, ER, Golgi apparatus, Lysosomes, and Vacuoles) whose functions are coordinated via vesicle transport", "Mitochondria, chloroplasts, and peroxisomes are NOT part of the endomembrane system because their functions and evolutionary origins are independent", "Includes mitochondria and chloroplasts as central sorting hubs, Excludes lysosomes and Golgi apparatus, Defined only in prokaryotic cells"),
            ("Secretory Pathway Trajectory (Pulse-Chase: Palade 1974 Nobel)", "RER (synthesis/signal cleavage) \\(\\rightarrow\\) COPII vesicles \\(\\rightarrow\\) Cis-Golgi \\(\\rightarrow\\) Medial \\(\\rightarrow\\) Trans-Golgi \\(\\rightarrow\\) Secretory vesicles \\(\\rightarrow\\) Exocytosis at plasma membrane", "Elucidated by George Palade using autoradiography with 3H-leucine in pancreatic exocrine cells", "Golgi \\(\\rightarrow\\) RER \\(\\rightarrow\\) Nucleus \\(\\rightarrow\\) Mitochondria \\(\\rightarrow\\) Secretion, Ribosomes \\(\\rightarrow\\) Lysosomes \\(\\rightarrow\\) Vacuoles \\(\\rightarrow\\) Plasma membrane, Plasma membrane \\(\\rightarrow\\) Golgi \\(\\rightarrow\\) RER \\(\\rightarrow\\) Nucleolus"),
            ("I-Cell Disease (Inclusion-cell disease / Mucolipidosis II)", "Severe autosomal recessive deficiency of GlcNAc phosphotransferase in the cis-Golgi, failing to phosphorylate mannose (no M6P tag)", "Lysosomal enzymes are misrouted and secreted into extracellular fluid; lysosomes accumulate undigested inclusion bodies, causing fatal skeletal/developmental failure", "Overproduction of acid hydrolases inside mitochondria, Defect in peroxisome catalase synthesis, Failure of RER protein folding leading to progeria"),
            ("Botulinum and Tetanus toxins targeting SNARE proteins", "Bacterial neurotoxins are zinc endopeptidases that cleave specific SNARE proteins (synaptobrevin, syntaxin, SNAP-25) at the presynaptic membrane", "Blocks synaptic vesicle exocytosis; Botulinum causes flaccid paralysis (blocks acetylcholine), Tetanus causes spastic paralysis (blocks GABA/glycine)", "Inhibit mitochondrial ATP synthase, Dissolve the nuclear envelope of motor neurons, Inactivate ribosomal 80S subunits"),
            ("Cystic Fibrosis (CFTR delta-F508 mutation)", "Deletion of phenylalanine 508 causes CFTR chloride channel misfolding; trapped in RER by chaperones and degraded by the proteasome", "Absence of CFTR at apical epithelial membrane leads to thick, dehydrated mucus in lungs, pancreas, and GI tract", "Overproduction of active chloride channels at plasma membrane, Massive accumulation of CFTR in lysosomes, Complete absence of RER in epithelial cells"),
            ("Brefeldin A mechanism of action", "Fungal antiviral metabolite that inhibits Arf1-GEF, blocking COPI vesicle coat assembly and causing disassembly and collapse of the Golgi into the ER", "Widely used tool in cell biology to arrest the secretory pathway and study vesicle dynamics", "Stimulates hyper-secretion of insulin, Destroys mitochondrial cristae, Inactivates lysosomal hydrolases permanently"),
            ("Chaperone-Mediated Autophagy (CMA) and Parkinson's Disease", "Lysosomal uptake of soluble proteins containing a KFERQ-like motif via LAMP-2A receptor and Hsc70 chaperone", "Impaired CMA clearance of mutant alpha-synuclein leads to toxic Lewy body aggregate accumulation in dopaminergic neurons", "Massive apoptosis caused by cytochrome c leakage, Failure of mitochondrial binary fission, Destruction of the Golgi complex by proteasomes"),
            ("Adrenoleukodystrophy (ALD / Lorenzo's Oil)", "X-linked disorder caused by mutations in ABCD1 peroxisomal transporter, impairing transport and beta-oxidation of VLCFAs in peroxisomes", "Leads to toxic accumulation of VLCFAs in brain white matter and adrenal cortex, causing rapid demyelination and adrenal failure", "Deficiency of mitochondrial Krebs cycle enzymes, Inability of lysosomes to digest glycogen, Overproduction of melanin in skin"),
            ("Mitochondrial ROS production and Aging Theory", "Electron leak from respiratory complexes I and III reduces \\(\\text{O}_2\\) prematurely to superoxide (\\(\\text{O}_2^{\\bullet-}\\)), generating reactive oxygen species (ROS)", "Cumulative oxidative damage to mtDNA, inner membrane lipids, and respiratory enzymes is a primary driver of senescence and degenerative diseases", "ROS are harmless molecules that enhance DNA replication, Leakage occurs only across the nuclear envelope, Aging is caused purely by cell wall thickening"),
            ("SNARE hypothesis (v-SNARE and t-SNARE pairing)", "Vesicle fusion is mediated by complementary pairing of vesicular v-SNAREs (e.g., synaptobrevin) with target membrane t-SNAREs (e.g., syntaxin, SNAP-25) forming a 4-helix bundle", "Overcomes electrostatic repulsion between lipid bilayers, driving spontaneous membrane fusion", "Requires destruction of lipid bilayer by lysosomes, Mediated by tubulin microtubules without proteins, Driven purely by water osmosis")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            f"**Step 1: Understand Endomembrane System Coordination & Pathology.**\n- Endomembrane system: Nuclear envelope, ER, Golgi, Lysosomes, Vacuoles.\n- Secretory pathway: RER \\(\\rightarrow\\) COPII \\(\\rightarrow\\) Golgi \\(\\rightarrow\\) Vesicles \\(\\rightarrow\\) Plasma membrane.\n- Pathologies: I-cell disease (M6P deficiency), Botulinum/Tetanus (SNARE cleavage), CFTR \\(\\Delta\\text{{F}}508\\) (ERAD degradation).\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Clinical / Molecular Impact:**\n{item[2]}."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-2-2.3.3", "Endoplasmic Reticulum, Golgi apparatus, Lysosomes, Mitochondria, Plastids, Vacuoles", archs)


if __name__ == "__main__":
    q1 = gen_2_3_1()
    q2 = gen_2_3_2()
    q3 = gen_2_3_3()
    print(f"gen_2_3_1: {len(q1)} questions")
    print(f"gen_2_3_2: {len(q2)} questions")
    print(f"gen_2_3_3: {len(q3)} questions")
    print(f"Total Part 3 questions: {len(q1) + len(q2) + len(q3)}")
