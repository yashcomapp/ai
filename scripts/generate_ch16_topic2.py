# scripts/generate_ch16_topic2.py
# MH-9-SCIT-16-16.2: DNA (Deoxyribonucleic Acid) - Watson & Crick Double Helix Model & RNA Types
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-16-16.2"

exam_data = [
    # 1-10: DNA Discovery & Nucleotide Chemistry
    ("What does the chemical acronym 'DNA' stand for?",
     ["Deoxyribonucleic Acid", "Dinitroribonucleic Acid", "Deoxyribose Nitrogen Acid", "Diaminonucleic Acid"],
     "A", "OSC", "easy",
     "DNA stands for Deoxyribonucleic Acid, the primary biological polymer that stores genetic instructions in all cellular life."),

    ("Who proposed the universally accepted Double Helix model of DNA structure in 1953?",
     ["James Watson and Francis Crick", "Gregor Mendel", "Robert Hooke", "Louis Pasteur"],
     "A", "OSC", "easy",
     "James Watson and Francis Crick proposed the double helical architecture of DNA in 1953, utilizing X-ray crystallography data collected by Rosalind Franklin and Maurice Wilkins."),

    ("Whose pioneering X-ray diffraction photograph of DNA fiber (Photo 51) provided critical mathematical proof of the helical structure of DNA?",
     ["Rosalind Franklin", "Marie Curie", "Jane Goodall", "Barbara McClintock"],
     "A", "OSC", "medium",
     "Photo 51, captured by Rosalind Franklin via X-ray crystallographic diffraction at King's College London, revealed the signature cross-pattern of a double helix."),

    ("What are the three chemical sub-components that covalently bond together to form a single DNA nucleotide?",
     ["Deoxyribose pentose sugar, a nitrogenous base, and a phosphate group",
      "Glucose, an amino acid, and a lipid",
      "Ribose sugar, sulfur, and calcium",
      "Starch, glycerol, and nitrogen"],
     "A", "OSC", "easy",
     "Every DNA mononucleotide consists of a 5-carbon 2-deoxyribose sugar esterified to an inorganic phosphate group at C5' and linked to a purine or pyrimidine nitrogenous base at C1'."),

    ("Which two nitrogenous bases belong to the double-ringed chemical class called PURINES?",
     ["Adenine (A) and Guanine (G)", "Cytosine (C) and Thymine (T)", "Uracil (U) and Thymine (T)", "Cytosine (C) and Adenine (A)"],
     "A", "OSC", "easy",
     "Purines possess a fused bicyclic pyrimidine-imidazole ring structure; Adenine (6-aminopurine) and Guanine (2-amino-6-oxypurine) constitute the two DNA purines."),

    ("Which two nitrogenous bases belong to the single-ringed heterocyclic chemical class called PYRIMIDINES in DNA?",
     ["Cytosine (C) and Thymine (T)", "Adenine (A) and Guanine (G)", "Adenine (A) and Thymine (T)", "Guanine (G) and Cytosine (C)"],
     "A", "OSC", "easy",
     "Pyrimidines are six-membered heterocyclic aromatic rings with two nitrogens; Cytosine and Thymine are the pyrimidines present in double-stranded DNA."),

    ("According to Chargaff's complementary base-pairing rules, Adenine always pairs with ________ via ________ hydrogen bonds.",
     ["Thymine (T) ; 2", "Cytosine (C) ; 3", "Guanine (G) ; 2", "Uracil (U) ; 3"],
     "A", "OSC", "easy",
     "Steric and hydrogen-bonding geometries dictate that Adenine pairs strictly with Thymine ($A = T$) via two hydrogen bonds."),

    ("Guanine (G) forms a complementary base pair with Cytosine (C) stabilized by how many hydrogen bonds?",
     ["3 hydrogen bonds", "2 hydrogen bonds", "1 hydrogen bond", "4 hydrogen bonds"],
     "A", "OSC", "easy",
     r"Guanine and Cytosine form three complementary hydrogen bonds ($G \equiv C$), imparting significantly greater thermodynamic stability than A-T base pairs."),

    ("According to Chargaff's rules of base composition in double-stranded DNA, which mathematical relationship is always true?",
     ["Total Purines = Total Pyrimidines (A + G = T + C)", "A = C and G = T", "A + T = G + C always", "Purines > Pyrimidines"],
     "A", "OSC", "easy",
     "Erwin Chargaff demonstrated that double-stranded DNA contains equimolar quantities of complementary bases ($A = T$ and $G = C$), so $(A + G) = (T + C)$."),

    ("If a sample of double-stranded DNA contains 30% Adenine, what percentage of Cytosine is present in this DNA?",
     ["20%", "30%", "40%", "10%"],
     "A", "ONE", "medium",
     "If Adenine = 30%, then complementary Thymine = 30% (total A + T = 60%). The remaining 40% is equally divided between Guanine and Cytosine, so Cytosine = 20%."),

    # 11-20: Double Helix Dimensions & Gene Concept
    ("What is the diameter of the DNA double helix in nanometers (nm) and Angstroms (A)?",
     ["2.0 nm (20 A)", "3.4 nm (34 A)", "0.34 nm (3.4 A)", "10 nm (100 A)"],
     "A", "OSC", "medium",
     "The antiparallel sugar-phosphate backbones wind around a central axis maintaining a constant uniform diameter of 2.0 nm (20 Angstroms)."),

    ("What is the distance spanned by one complete 360-degree helical turn (pitch) of B-DNA?",
     ["3.4 nm (34 A)", "2.0 nm (20 A)", "0.34 nm (3.4 A)", "20 nm (200 A)"],
     "A", "OSC", "medium",
     "One complete helical turn in standard B-DNA advances 3.4 nm (34 Angstroms) along the longitudinal helical axis."),

    ("How many base pairs (bp) are present in each single 360-degree helical turn of standard B-form DNA?",
     ["10 base pairs (10 bp)", "20 base pairs", "5 base pairs", "4 base pairs"],
     "A", "OSC", "easy",
     "Each full 360-degree turn accommodates approximately 10 base pairs, with each successive pair rotated by 36 degrees."),

    ("What is the vertical axial distance between two adjacent, stacked base pairs in a DNA molecule?",
     ["0.34 nm (3.4 A)", "3.4 nm (34 A)", "2.0 nm (20 A)", "1.0 nm (10 A)"],
     "A", "OSC", "medium",
     "Dividing the 3.4 nm helical pitch by 10 base pairs per turn yields an axial rise of 0.34 nm (3.4 Angstroms) between neighboring stacked base pairs."),

    ("What does it mean that the two strands of a DNA double helix run in an 'anti-parallel' direction?",
     ["One strand runs in the 5' -> 3' direction while the complementary strand runs in the 3' -> 5' direction",
      "One strand is made of metal and the other is made of wood",
      "Both strands run in the same 5' -> 3' direction simultaneously",
      "The strands never touch or interact with each other"],
     "A", "OSC", "medium",
     "The phosphodiester backbones are oriented in opposite polarities: the 5'-phosphate terminus of one strand aligns with the 3'-hydroxyl terminus of its partner."),

    ("What chemical bond links the 3'-hydroxyl group of one deoxyribose sugar to the 5'-phosphate group of the adjacent nucleotide along a DNA strand?",
     ["Phosphodiester bond", "Peptide bond", "Glycosidic bond", "Hydrogen bond"],
     "A", "OSC", "medium",
     "Phosphodiester covalent bonds link successive nucleoside pentoses between the C3' and C5' positions, forming the structural backbone."),

    ("What is a functional segment of DNA that contains the specific nucleotide sequence coding for a functional polypeptide protein or RNA called?",
     ["Gene", "Centromere", "Histone", "Telomere"],
     "A", "OSC", "easy",
     "A gene is the fundamental physical and functional unit of heredity, consisting of a discrete transcribed nucleotide sequence."),

    ("Which five-carbon pentose sugar is found exclusively in RNA instead of the deoxyribose found in DNA?",
     ["Ribose sugar (having an -OH group at C2')", "Deoxyribose sugar", "Glucose", "Fructose"],
     "A", "OSC", "easy",
     "RNA nucleotides contain beta-D-ribose with a hydroxyl (-OH) group at the 2' carbon position, whereas deoxyribose has a single hydrogen (-H) atom at C2'."),

    ("Which pyrimidine nitrogenous base is present in RNA molecules in place of Thymine (T)?",
     ["Uracil (U)", "Cytosine (C)", "Guanine (G)", "Adenine (A)"],
     "A", "OSC", "easy",
     "Thymine is 5-methyluracil; in RNA, the unmethylated pyrimidine Uracil (U) pairs complementarily with Adenine ($A = U$)."),

    ("What is the primary architectural difference between DNA and RNA in cellular organisms?",
     ["DNA is typically double-stranded while RNA is predominantly single-stranded",
      "DNA is liquid while RNA is a hard gas",
      "DNA is found only in plants while RNA is found only in animals",
      "DNA has no nitrogen atoms"],
     "A", "OSC", "easy",
     "Cellular genomic DNA exists as an antiparallel double-stranded helix, whereas cellular RNA molecules function as flexible single-stranded polynucleotide chains."),

    # 21-30: RNA Types & Central Dogma
    ("Which type of RNA transcribes the genetic code from chromosomal DNA in the nucleus and carries it to the ribosomes in the cytoplasm?",
     ["Messenger RNA (mRNA)", "Ribosomal RNA (rRNA)", "Transfer RNA (tRNA)", "Small nuclear RNA (snRNA)"],
     "A", "OSC", "easy",
     "mRNA functions as the genetic messenger, carrying complementary ribonucleotide codon triplets copied from genomic DNA to the cytoplasm for translation."),

    ("Which type of RNA is the most abundant in living cells, forming over 80% of total cellular RNA and serving as the structural and catalytic core of ribosomes?",
     ["Ribosomal RNA (rRNA)", "Transfer RNA (tRNA)", "Messenger RNA (mRNA)", "Micro RNA (miRNA)"],
     "A", "OSC", "easy",
     "rRNA forms ribonucleoprotein complexes with ribosomal proteins, providing the peptidyl transferase ribozyme activity that catalyzes peptide bond formation."),

    ("Which small adapter RNA molecule adopts a 2D cloverleaf shape, carrying specific amino acids to the ribosome during protein synthesis?",
     ["Transfer RNA (tRNA)", "Messenger RNA (mRNA)", "Ribosomal RNA (rRNA)", "Heterogeneous nuclear RNA (hnRNA)"],
     "A", "OSC", "easy",
     "tRNA serves as the physical adapter translating mRNA codons into amino acids; it carries an amino acid at its 3'-CCA tail and an anticodon loop at its base."),

    ("What is the triplet sequence of three ribonucleotides on an mRNA molecule that specifies a particular amino acid called?",
     ["Codon", "Anticodon", "Intron", "Exon"],
     "A", "OSC", "easy",
     "A codon is a sequential triplet of three mRNA nucleotide bases (e.g. AUG for Methionine) that dictates one specific amino acid in a polypeptide chain."),

    ("What is the complementary three-nucleotide sequence located on the anticodon loop of a tRNA molecule that base-pairs with an mRNA codon?",
     ["Anticodon", "Codon", "Promoter", "Operon"],
     "A", "OSC", "easy",
     "The tRNA anticodon triplet forms antiparallel Watson-Crick hydrogen bonds with matching mRNA codons, ensuring fidelity of the genetic code."),

    ("What biological term describes the process of synthesizing a complementary single-stranded RNA molecule from a DNA template strand?",
     ["Transcription", "Translation", "Replication", "Transduction"],
     "A", "OSC", "easy",
     "Transcription is the enzymatic synthesis of RNA by RNA polymerase using a template strand of genomic DNA."),

    ("What biological process describes the synthesis of a polypeptide protein chain at the ribosome using the genetic sequence encoded on mRNA?",
     ["Translation", "Transcription", "Replication", "Splicing"],
     "A", "OSC", "easy",
     "Translation decodes mRNA nucleotide sequences into linear sequences of amino acids at the ribosome to construct functional proteins."),

    ("The flow of genetic information from DNA to RNA (via transcription) and from RNA to Protein (via translation) is known as the:",
     ["Central Dogma of Molecular Biology", "Cell Theory", "Law of Segregation", "Theory of Natural Selection"],
     "A", "OSC", "easy",
     "Formulated by Francis Crick in 1958, the Central Dogma establishes the directional flow of genetic information: $\\text{DNA} \\xrightarrow{\\text{transcription}} \\text{RNA} \\xrightarrow{\\text{translation}} \\text{Protein}$."),

    ("Which universal codon serves as the 'START codon' for initiating protein translation and simultaneously codes for the amino acid Methionine?",
     ["AUG", "UAA", "UAG", "UGA"],
     "A", "OSC", "medium",
     "AUG is the universal initiator codon recognized by initiator tRNA loaded with formylmethionine or methionine to set the translational reading frame."),

    ("Which of the following triplet codons function as 'STOP codons' (nonsense codons) that signal termination of protein synthesis?",
     ["UAA, UAG, and UGA", "AUG, GUG, and UUG", "AAA, UUU, and GGG", "CCC, AAA, and TTT"],
     "A", "OSC", "medium",
     "UAA (ochre), UAG (amber), and UGA (opal) lack cognate aminoacyl-tRNAs; they recruit release factors that cleave the completed polypeptide from the ribosome."),

    # 31-40: Fill in blanks, Numerical, Multi-choice
    ("A DNA molecule with 100 complete helical turns contains exactly ________ base pairs.",
     ["1,000 base pairs", "100 base pairs", "2,000 base pairs", "500 base pairs"],
     "A", "ONE", "easy",
     "Standard B-DNA contains 10 base pairs per helical turn; therefore, 100 helical turns contain $100 \\times 10 = 1,000$ base pairs."),

    ("In an RNA molecule, the nitrogenous base that pairs with Adenine is ________ instead of Thymine.",
     ["Uracil", "Guanine", "Cytosine", "Thiamine"],
     "A", "OFB", "easy",
     "Uracil replaces thymine in ribonucleic acid, forming two hydrogen bonds with adenine during RNA transcription and translation."),

    ("If a segment of double-stranded DNA has a total length of 34 nanometers (nm), how many complete helical turns does it contain?",
     ["10 complete turns", "100 complete turns", "1 complete turn", "34 complete turns"],
     "A", "ONE", "medium",
     "Helical pitch is 3.4 nm per complete turn. A 34 nm DNA segment contains $34 / 3.4 = 10$ complete helical turns (100 base pairs)."),

    ("State whether True or False: In a double-stranded DNA molecule, the ratio of (A + T) to (G + C) is strictly equal to 1.0 in all organisms.",
     ["False", "True"],
     "A", "OTF", "medium",
     "While $A = T$ and $G = C$ independently (so $(A+G)/(T+C) = 1.0$), the $(A+T)/(G+C)$ base ratio varies widely among species and is species-specific."),

    ("Which of the following components are found in a molecule of ATP (Adenosine Triphosphate)? (Select all that apply)",
     ["Adenine nitrogenous base, Ribose pentose sugar, and Three phosphate groups",
      "Only Deoxyribose sugar and Guanine",
      "Only Thymine and two sulfates",
      "Lipid bilayer and cholesterol"],
     "A", "OMC", "easy",
     "ATP is an adenine ribonucleotide consisting of an adenine base linked to ribose, bound to a chain of three high-energy phosphate groups."),

    ("Assertion (A): The genetic code is described as 'degenerate' or redundant.\nReason (R): Most amino acids are specified by more than one distinct triplet codon (61 sense codons code for 20 amino acids).",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is not the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "medium",
     "Because $4^3 = 64$ triplet combinations encode only 20 standard amino acids, multiple synonymous codons code for the same amino acid, conferring mutational resilience."),

    ("What type of chemical linkage connects a nitrogenous base to the 1'-carbon of deoxyribose in a nucleoside?",
     ["N-glycosidic bond", "Phosphodiester bond", "Peptide bond", "Hydrogen bond"],
     "A", "OSC", "medium",
     "A beta-N-glycosidic bond connects the N9 of purines or N1 of pyrimidines to the C1' of the pentose sugar ring."),

    ("During DNA replication, which enzyme unwinds the double helix by breaking hydrogen bonds between complementary base pairs?",
     ["DNA Helicase", "DNA Ligase", "DNA Polymerase", "RNA Primase"],
     "A", "OSC", "medium",
     "DNA helicase utilizes ATP hydrolysis energy to disrupt hydrogen bonds between bases, unwinding the double helix ahead of the replication fork."),

    ("Which enzyme joins Okazaki fragments on the lagging strand by catalyzing the formation of phosphodiester bonds?",
     ["DNA Ligase", "DNA Helicase", "RNA Polymerase", "Topoisomerase"],
     "A", "OSC", "medium",
     "DNA ligase seals nicks in the phosphodiester sugar-phosphate backbone by joining 3'-OH and 5'-phosphate ends of adjacent Okazaki fragments."),

    ("State whether True or False: Meselson and Stahl's classic 1958 experiment using heavy isotope 15N proved that DNA replication is semi-conservative.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Meselson and Stahl grew E. coli in 15N and shifted them to 14N, demonstrating that daughter DNA molecules receive one intact parental strand and one newly synthesized strand.")
]

practice_data = [
    # 41-50: Advanced Molecular Genetics & Chargaff Problems
    ("A double-stranded DNA fragment contains 2,000 base pairs (4,000 nucleotides). If there are 600 Guanine bases, how many Thymine bases are present?",
     ["1,400 Thymine bases", "600 Thymine bases", "2,000 Thymine bases", "1,200 Thymine bases"],
     "A", "ONE", "hard",
     "G = 600 means C = 600 (total G + C = 1,200). Out of 4,000 total nucleotides, remaining A + T = 4,000 - 1,200 = 2,800. Since A = T, Thymine = 2,800 / 2 = 1,400."),

    ("Why do G-C rich regions of DNA require higher temperatures to melt and denature into single strands than A-T rich regions?",
     ["G-C base pairs are held together by three hydrogen bonds and stronger base-stacking interactions compared to only two in A-T pairs",
      "G-C pairs are made of pure stone",
      "A-T pairs have no chemical bonds",
      "G-C pairs freeze at room temperature"],
     "A", "OSC", "medium",
     "Three hydrogen bonds per G-C pair and favorable base-stacking enthalpy increase the thermal denaturation melting temperature (Tm) of G-C rich duplexes."),

    ("What is the function of the CCA-3' terminal sequence found on every mature transfer RNA (tRNA) molecule?",
     ["It serves as the amino acid attachment site where a specific amino acid is esterified by aminoacyl-tRNA synthetase",
      "It binds directly to the cell nucleus",
      "It cuts the ribosome into pieces",
      "It produces energy like a battery"],
     "A", "OSC", "medium",
     "The invariant 3'-CCA terminal adenosine provides a 2'- or 3'-hydroxyl group to which cognate amino acids are covalently esterified during tRNA charging."),

    ("What happens during post-transcriptional splicing of eukaryotic primary pre-mRNA transcripts?",
     ["Non-coding intervening sequences (introns) are excised and coding sequences (exons) are spliced together",
      "All nucleotides are converted into glucose",
      "The pre-mRNA is transported back into DNA",
      "Exons are destroyed while introns are saved"],
     "A", "OSC", "medium",
     "Spliceosomes remove non-coding introns from nuclear pre-mRNA and ligate coding exons contiguously to yield translationally competent mature mRNA."),

    ("Which enzyme synthesizes complementary DNA (cDNA) from an RNA template in retroviruses (such as HIV)?",
     ["Reverse Transcriptase", "DNA Polymerase III", "RNA Polymerase II", "Telomerase"],
     "A", "OSC", "medium",
     "Reverse transcriptase is an RNA-dependent DNA polymerase that reverses the standard Central Dogma flow by converting viral RNA into proviral cDNA."),

    ("If a template DNA strand has the sequence 3'-TAC GGC TTA-5', what will be the transcribed mRNA sequence?",
     ["5'-AUG CCG AAU-3'", "5'-ATG CCG AAT-3'", "3'-AUG CCG AAU-5'", "5'-UAC GGC UUA-3'"],
     "A", "OSC", "medium",
     "Transcription follows antiparallel base pairing with RNA replacing T with U: 3'-T-A-C-G-G-C-T-T-A-5' yields complementary 5'-A-U-G-C-C-G-A-A-U-3'."),

    ("State whether True or False: The genetic code is universal, meaning that a codon such as UUU codes for Phenylalanine across virtually all living organisms from bacteria to humans.",
     ["True", "False"],
     "A", "OTF", "easy",
     "With minor mitochondrial exceptions, the triplet genetic code is identical across all kingdoms of life, proving a common evolutionary origin for all living systems."),

    ("What is the term for a point mutation in DNA where a purine base is replaced by another purine (e.g. A to G), or a pyrimidine by another pyrimidine (e.g. C to T)?",
     ["Transition mutation", "Transversion mutation", "Frameshift mutation", "Inversion"],
     "A", "OSC", "hard",
     "Transitions swap like-with-like ring structures (purine to purine or pyrimidine to pyrimidine); transversions interchange purines and pyrimidines."),

    ("Which structural form of DNA is a left-handed double helix with a zigzag phosphodiester backbone and 12 base pairs per turn?",
     ["Z-DNA", "B-DNA", "A-DNA", "C-DNA"],
     "A", "OSC", "hard",
     "Z-DNA is a transient left-handed helical conformation with 12 bp per turn, found in alternating purine-pyrimidine tracts under negative supercoiling."),

    ("What cellular machinery is responsible for proofreading newly added nucleotides and excising mismatched bases during DNA replication?",
     ["3' -> 5' exonuclease proofreading activity of DNA Polymerase",
      "Mitochondria",
      "Ribosomes",
      "Golgi apparatus"],
     "A", "OSC", "hard",
     "DNA polymerases exhibit 3' to 5' exonuclease activity; upon sensing a steric mismatch, the enzyme reverses, hydrolyzes the erroneous base, and resumes elongation.")
]

# Additional 20 practice questions to reach exactly 30 questions
practice_data.extend([
    # 51-60: Further Structural & Functional Concepts
    ("What prevents DNA strands from re-annealing and tangling during replication while single-stranded?",
     ["Single-Stranded Binding Proteins (SSBs)", "Histone H1", "Tubulin fibers", "Actin microfilaments"],
     "A", "OSC", "medium",
     "Single-stranded DNA binding proteins coat the transiently exposed unwound single strands, preventing self-annealing and hairpin degradation."),

    ("How many hydrogen bonds exist between 50 pairs of A-T and 50 pairs of G-C in a 100 bp DNA segment?",
     ["250 hydrogen bonds", "200 hydrogen bonds", "100 hydrogen bonds", "300 hydrogen bonds"],
     "A", "ONE", "hard",
     "Each A-T pair has 2 H-bonds ($50 \\times 2 = 100$). Each G-C pair has 3 H-bonds ($50 \\times 3 = 150$). Total $= 100 + 150 = 250$ hydrogen bonds."),

    ("What is the primary role of microRNAs (miRNAs) in cellular post-transcriptional regulation?",
     ["Binding complementarily to target mRNAs to degrade them or repress their translation",
      "Synthesizing glucose molecules",
      "Constructing cellular cell walls",
      "Pumping calcium into mitochondria"],
     "A", "OSC", "medium",
     "MicroRNAs (miRNAs) guide the RISC complex to imperfectly match 3'-UTRs of mRNAs, fine-tuning gene expression by translational repression or mRNA cleavage."),

    ("Which RNA molecule exhibits catalytic enzymatic activity and earned Thomas Cech and Sidney Altman a Nobel Prize for discovering 'Ribozymes'?",
     ["Catalytic RNA (Ribozyme)", "DNA ligase", "Transfer RNA", "Lipids"],
     "A", "OSC", "medium",
     "Ribozymes are catalytic RNA molecules capable of cleaving RNA phosphodiester bonds and catalyzing peptide bond synthesis in ribosomes."),

    ("State whether True or False: RNA is chemically more labile and prone to alkaline hydrolysis than DNA due to the reactive 2'-OH group on its ribose sugar.",
     ["True", "False"],
     "A", "OTF", "medium",
     "The 2'-hydroxyl group in ribose acts as an internal nucleophile under alkaline conditions, attacking the adjacent phosphodiester bond and cleaving RNA."),

    ("In prokaryotes, transcription and translation can occur simultaneously in the same compartment because:",
     ["Prokaryotes lack a nuclear membrane separating DNA from ribosomes",
      "Bacteria have no chromosomes",
      "Bacteria produce only lipids",
      "Ribosomes live inside bacterial nuclei"],
     "A", "OSC", "easy",
     "Lacking a nuclear envelope, bacterial ribosomes attach directly to nascent mRNA transcripts while RNA polymerase is actively transcribing the downstream DNA."),

    ("What is the chemical nature of the 5'-cap added to eukaryotic pre-mRNAs to protect against exonucleases and assist ribosome binding?",
     ["7-methylguanosine (m7G) linked by a 5'-5' triphosphate bridge",
      "A long tail of 200 thymines",
      "A layer of cholesterol",
      "A cellulose fiber cap"],
     "A", "OSC", "hard",
     "Capping attaches 7-methylguanosine via an atypical 5'-to-5' triphosphate linkage, shielding the mRNA from 5' exonucleolytic decay and initiating translation."),

    ("What is the series of 100 to 250 Adenine nucleotides enzymatically appended to the 3' terminus of eukaryotic mature mRNA called?",
     ["Poly-A tail", "5' cap", "Intron", "TATA box"],
     "A", "OSC", "medium",
     "Polyadenylate polymerase synthesizes a poly-A tail at the cleaved 3' end, promoting nuclear export, translational efficiency, and mRNA stability."),

    ("Which antibiotic halts bacterial protein synthesis by mimicking the 3' end of tyrosyl-tRNA and causing premature chain termination?",
     ["Puromycin", "Penicillin", "Aspirin", "Insulin"],
     "A", "OSC", "hard",
     "Puromycin enters the ribosomal A site, accepts the nascent polypeptide chain via transpeptidation, and prematurely releases the truncated peptidyl-puromycin."),

    ("State whether True or False: DNA in mitochondria and chloroplasts is circular and double-stranded, closely resembling bacterial DNA.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Supporting the endosymbiotic theory, mitochondrial and plastid genomes exist as circular, double-stranded, non-histone-bound DNA molecules reminiscent of alpha-proteobacteria.")
])

# 10 more questions to complete practice_data to 30
practice_data.extend([
    # 61-70: High-Yield Practice Questions
    ("What is the structural role of the major and minor grooves in the DNA double helix?",
     ["They expose distinct chemical groups of base pairs to allow sequence-specific binding of regulatory transcription factors",
      "They allow water to flow through the center like a pipe",
      "They store minerals for tooth growth",
      "They trap air bubbles inside the nucleus"],
     "A", "OSC", "hard",
     "Asymmetrical attachment of base pairs to sugars creates deep major grooves and shallow minor grooves, displaying characteristic hydrogen-donor/acceptor arrays for transcription factors."),

    ("How many total base pairs are contained in the haploid human genome (23 chromosomes)?",
     ["Approximately 3.2 billion base pairs (~3.2 x 10^9 bp)",
      "3.2 million base pairs",
      "32,000 base pairs",
      "100 billion base pairs"],
     "A", "ONE", "medium",
     "The haploid human genome comprises approximately $3.2 \\times 10^9$ base pairs of nuclear DNA distributed across 23 chromosomes."),

    ("If an mRNA codon reads 5'-UAC-3', what is the complementary tRNA anticodon sequence reading 3' to 5'?",
     ["3'-AUG-5'", "3'-UAC-5'", "5'-AUG-3'", "3'-ATG-5'"],
     "A", "OSC", "medium",
     "By antiparallel base pairing, 5'-U-A-C-3' pairs with 3'-A-U-G-5' on the matching tRNA anticodon loop."),

    ("Which enzyme relieves torsional strain and positive supercoiling ahead of the advancing DNA replication fork by nicking and resealing DNA strands?",
     ["Topoisomerase (DNA Gyrase)", "DNA Polymerase I", "DNA Ligase", "Telomerase"],
     "A", "OSC", "medium",
     "Topoisomerases transiently cleave one or both DNA strands, allowing controlled rotation to dissipate supercoiling generated by helicase unwinding."),

    ("State whether True or False: The two strands of DNA double helix are held together strictly by covalent peptide bonds between nitrogen bases.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Strands are held together by non-covalent hydrogen bonds between complementary bases and hydrophobic pi-pi base stacking, allowing reversible strand separation."),

    ("What provides the chemical energy required for DNA polymerase to synthesize new phosphodiester bonds during replication?",
     ["Hydrolysis of high-energy pyrophosphate (PPi) from incoming deoxynucleoside triphosphates (dNTPs)",
      "Direct solar energy from sunlight",
      "Battery currents from the cell membrane",
      "Combustion of oxygen gas"],
     "A", "OSC", "medium",
     "Incoming dNTPs (dATP, dCTP, dGTP, dTTP) provide the high-energy pyrophosphate leaving group; its cleavage into 2 Pi drives thermodynamically irreversible synthesis."),

    ("Which RNA polymerase transcribes the vast majority of protein-coding genes into pre-mRNAs in eukaryotic nuclei?",
     ["RNA Polymerase II", "RNA Polymerase I", "RNA Polymerase III", "DNA Polymerase alpha"],
     "A", "OSC", "hard",
     "Eukaryotic RNA Polymerase II transcribes all protein-coding genes and most snRNAs/miRNAs, regulated by its carboxy-terminal domain (CTD)."),

    ("What does the 'wobble hypothesis' formulated by Francis Crick explain?",
     ["Non-standard, flexible base-pairing at the third (3') codon base position allows 31 tRNAs to recognize all 61 sense codons",
      "Why DNA molecules wobble when heated",
      "How cells balance on liquid surfaces",
      "Why bacteria swim in circles"],
     "A", "OSC", "hard",
     "The wobble hypothesis states that steric constraints are relaxed at the 3' codon / 5' anticodon wobble position, permitting unconventional base pairing (e.g. Inosine with U, C, or A)."),

    ("How long would all the DNA strands from a single human diploid somatic cell be if stretched end-to-end?",
     ["Approximately 2 meters long", "2 millimeters", "2 kilometers", "2 micrometers"],
     "A", "OSC", "easy",
     "A diploid cell contains $6.4 \\times 10^9$ base pairs; with 0.34 nm per base pair, the total linear length equals $6.4 \\times 10^9 \\times 0.34 \\times 10^{-9} \\approx 2.18$ meters."),

    ("Which molecular component recognizes and binds to the promoter sequence (such as the Pribnow box / TATA box) to initiate transcription?",
     ["Sigma factor in bacteria / TBP (TATA-Binding Protein) in eukaryotes",
      "Ribosome large subunit",
      "tRNA anticodon loop",
      "DNA ligase"],
     "A", "OSC", "medium",
     "The sigma factor directs bacterial RNA polymerase holoenzyme to -10 and -35 promoter elements; TBP recruits eukaryotic pre-initiation complexes to the TATA box.")
])

mock_data = [
    # 71: Watson & Crick Double Helix Model Dimensions
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="210" viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="210" rx="8" fill="#090d16"/>
  <!-- Two Strands intertwining -->
  <path d="M 120 20 Q 80 70 120 120 T 120 200" stroke="#38bdf8" stroke-width="4" fill="none"/>
  <path d="M 160 20 Q 200 70 160 120 T 160 200" stroke="#ec4899" stroke-width="4" fill="none"/>
  <!-- Base pair rungs -->
  <line x1="125" y1="35" x2="155" y2="35" stroke="#facc15" stroke-width="3"/>
  <line x1="110" y1="65" x2="170" y2="65" stroke="#4ade80" stroke-width="3"/>
  <line x1="125" y1="95" x2="155" y2="95" stroke="#facc15" stroke-width="3"/>
  <line x1="140" y1="120" x2="140" y2="120" stroke="#4ade80" stroke-width="3"/>
  <line x1="125" y1="145" x2="155" y2="145" stroke="#facc15" stroke-width="3"/>
  <line x1="110" y1="175" x2="170" y2="175" stroke="#4ade80" stroke-width="3"/>
  <!-- Labels -->
  <!-- Diameter -->
  <line x1="85" y1="65" x2="195" y2="65" stroke="#ffffff" stroke-width="1" stroke-dasharray="2"/>
  <text x="210" y="68" fill="#ffffff" font-size="10" font-family="sans-serif" font-weight="bold">Diameter = 2.0 nm (20 A)</text>
  <!-- One Pitch (3.4 nm) -->
  <line x1="60" y1="35" x2="60" y2="145" stroke="#facc15" stroke-width="2"/>
  <text x="50" y="95" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="end" font-weight="bold">1 Turn = 3.4 nm</text>
  <text x="50" y="110" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="end">(10 bp / 34 A)</text>
  <!-- Distance between bp -->
  <text x="210" y="130" fill="#4ade80" font-size="10" font-family="sans-serif" font-weight="bold">Distance between bp:</text>
  <text x="210" y="145" fill="#bbf7d0" font-size="9" font-family="sans-serif">0.34 nm (3.4 A)</text>
  <!-- Antiparallel text -->
  <text x="120" y="15" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle">5'</text>
  <text x="160" y="15" fill="#ec4899" font-size="8" font-family="sans-serif" text-anchor="middle">3'</text>
</svg>
</div>
According to the calibrated Watson-Crick B-DNA double helix model depicted above, what is the axial distance between two adjacent, stacked base pairs along the helical axis?""""",
     ["0.34 nm (3.4 Angstroms)", "3.4 nm (34 Angstroms)", "2.0 nm (20 Angstroms)", "20 nm (200 Angstroms)"],
     "A", "OSC", "easy",
     "One complete 360-degree helical turn spans 3.4 nm and accommodates exactly 10 base pairs; dividing pitch by 10 yields an axial spacing of 0.34 nm (3.4 A) between adjacent base pairs."),

    # 72: Complementary Base Pairing (A=T & G≡C Hydrogen Bonds)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- A = T Box -->
  <rect x="30" y="30" width="160" height="140" rx="6" fill="#27272a" stroke="#38bdf8" stroke-width="2"/>
  <text x="110" y="55" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">Adenine = Thymine</text>
  <circle cx="70" cy="95" r="22" fill="#0284c7"/>
  <text x="70" y="100" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">A</text>
  <!-- 2 H Bonds -->
  <line x1="95" y1="90" x2="125" y2="90" stroke="#facc15" stroke-width="2" stroke-dasharray="3"/>
  <line x1="95" y1="100" x2="125" y2="100" stroke="#facc15" stroke-width="2" stroke-dasharray="3"/>
  <circle cx="150" cy="95" r="22" fill="#ef4444"/>
  <text x="150" y="100" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">T</text>
  <text x="110" y="145" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">2 Hydrogen Bonds</text>
  <!-- G ≡ C Box -->
  <rect x="210" y="30" width="160" height="140" rx="6" fill="#27272a" stroke="#4ade80" stroke-width="2"/>
  <text x="290" y="55" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">Guanine = Cytosine</text>
  <circle cx="250" cy="95" r="22" fill="#15803d"/>
  <text x="250" y="100" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">G</text>
  <!-- 3 H Bonds -->
  <line x1="275" y1="88" x2="305" y2="88" stroke="#facc15" stroke-width="2" stroke-dasharray="3"/>
  <line x1="275" y1="95" x2="305" y2="95" stroke="#facc15" stroke-width="2" stroke-dasharray="3"/>
  <line x1="275" y1="102" x2="305" y2="102" stroke="#facc15" stroke-width="2" stroke-dasharray="3"/>
  <circle cx="330" cy="95" r="22" fill="#a855f7"/>
  <text x="330" y="100" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">C</text>
  <text x="290" y="145" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">3 Hydrogen Bonds</text>
</svg>
</div>
Why does a Guanine-Cytosine (G-C) rich DNA segment exhibit significantly greater thermal stability and a higher melting temperature than an Adenine-Thymine (A-T) rich segment?""""",
     ["G-C pairs are joined by three hydrogen bonds with superior base-stacking enthalpy, compared to only two hydrogen bonds in A-T pairs",
      "G-C pairs are bonded with steel covalent links",
      "A-T pairs have no chemical bonds whatsoever",
      "Guanine freezes at room temperature while Adenine boils"],
     "A", "OSC", "medium",
     "Each G-C base pair contributes three hydrogen bonds ($G \\equiv C$) versus two in an A-T pair ($A = T$), imparting substantially higher free energy of dissociation and higher melting temperature (Tm)."),

    # 73: Nucleotide Monomer Molecular Anatomy
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#0f172a"/>
  <!-- Phosphate Group (Yellow) -->
  <circle cx="80" cy="70" r="22" fill="#ca8a04" stroke="#facc15" stroke-width="2"/>
  <text x="80" y="74" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">PO4 (3-)</text>
  <text x="80" y="105" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">5' Phosphate</text>
  <line x1="102" y1="70" x2="150" y2="100" stroke="#facc15" stroke-width="3"/>
  <!-- Deoxyribose Pentose Sugar (Blue Pentagon) -->
  <polygon points="180,75 220,105 205,145 155,145 140,105" fill="#1e40af" stroke="#38bdf8" stroke-width="2"/>
  <text x="180" y="120" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Deoxyribose</text>
  <text x="180" y="135" fill="#93c5fd" font-size="8" font-family="sans-serif" text-anchor="middle">(2' -H only)</text>
  <line x1="220" y1="105" x2="270" y2="105" stroke="#38bdf8" stroke-width="3"/>
  <!-- Nitrogenous Base (Green) -->
  <rect x="270" y="80" width="85" height="48" rx="6" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
  <text x="312" y="102" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Base (A/G/C/T)</text>
  <text x="312" y="117" fill="#bbf7d0" font-size="8" font-family="sans-serif" text-anchor="middle">Purine / Pyrimidine</text>
  <!-- Phosphodiester note -->
  <text x="200" y="180" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">Nucleotide = Phosphate + Pentose Sugar + Nitrogenous Base</text>
</svg>
</div>
What chemical feature distinguishes the 5-carbon pentose sugar in a DNA nucleotide from that in an RNA nucleotide?""",
     ["DNA contains 2-deoxyribose with a single hydrogen atom (-H) at the 2' carbon, whereas RNA contains ribose with a hydroxyl group (-OH) at C2'",
      "DNA sugar has 10 carbon atoms while RNA has only 3",
      "DNA sugar is glucose while RNA sugar is fructose",
      "DNA contains no oxygen atoms anywhere in its structure"],
     "A", "OSC", "easy",
     "The prefix 'deoxy' denotes the absence of an oxygen atom at position 2' of the furanose ring in DNA; RNA retains a reactive 2'-hydroxyl (-OH) group."),

    # 74: Antiparallel Sugar-Phosphate Strands (5' to 3' vs 3' to 5')
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#111827"/>
  <!-- Strand 1 (5' -> 3') -->
  <rect x="60" y="30" width="40" height="140" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="80" y="22" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">5' End</text>
  <text x="80" y="55" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle">PO4</text>
  <text x="80" y="95" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle">Sugar</text>
  <text x="80" y="135" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle">PO4</text>
  <text x="80" y="185" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">3' -OH</text>
  <!-- Arrow downwards -->
  <line x1="80" y1="145" x2="80" y2="170" stroke="#38bdf8" stroke-width="2"/>
  <!-- Central Base Pairs -->
  <rect x="130" y="60" width="140" height="30" rx="4" fill="#27272a" stroke="#4ade80" stroke-width="1"/>
  <text x="200" y="80" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle">A === T</text>
  <rect x="130" y="110" width="140" height="30" rx="4" fill="#27272a" stroke="#4ade80" stroke-width="1"/>
  <text x="200" y="130" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle">G ==== C</text>
  <!-- Strand 2 (3' -> 5') -->
  <rect x="300" y="30" width="40" height="140" rx="6" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
  <text x="320" y="22" fill="#ec4899" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">3' -OH</text>
  <text x="320" y="55" fill="#ec4899" font-size="9" font-family="sans-serif" text-anchor="middle">Sugar</text>
  <text x="320" y="95" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle">PO4</text>
  <text x="320" y="135" fill="#ec4899" font-size="9" font-family="sans-serif" text-anchor="middle">Sugar</text>
  <text x="320" y="185" fill="#ec4899" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">5' End</text>
</svg>
</div>
What structural characteristic of the DNA double helix is illustrated by the opposing chemical polarities (5'-to-3' and 3'-to-5') of the complementary strands?""",
     ["Antiparallel orientation of the phosphodiester sugar-phosphate backbones",
      "Semi-conservative degradation",
      "Circular bacterial chromosome replication",
      "Unidirectional translation"],
     "A", "OSC", "medium",
     "The complementary polynucleotide chains run in opposite chemical directions (antiparallel); the 5'-phosphate head of one strand faces the 3'-hydroxyl tail of its partner, permitting stable Watson-Crick hydrogen bonding."),

    # 75: tRNA Cloverleaf 2D Architecture
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="210" viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="210" rx="8" fill="#18181b"/>
  <!-- Acceptor Stem -->
  <line x1="200" y1="20" x2="200" y2="60" stroke="#facc15" stroke-width="4"/>
  <text x="200" y="15" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">3' -CCA (Amino Acid Binding Site)</text>
  <!-- D Loop (Left) -->
  <circle cx="130" cy="90" r="24" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="130" y="94" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">D Loop</text>
  <!-- T-Psi-C Loop (Right) -->
  <circle cx="270" cy="90" r="24" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
  <text x="270" y="94" fill="#ec4899" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">T Loop</text>
  <!-- Anticodon Loop (Bottom) -->
  <circle cx="200" cy="150" r="24" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <text x="200" y="154" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Anticodon</text>
  <text x="200" y="190" fill="#bbf7d0" font-size="9" font-family="sans-serif" text-anchor="middle">Pairs with mRNA codon (e.g. UAC -> AUG)</text>
</svg>
</div>
In the standard cloverleaf model of transfer RNA (tRNA) shown above, which domain is responsible for recognizing and base-pairing with the triplet codon on messenger RNA (mRNA)?""",
     ["The anticodon loop at the base of the tRNA molecule",
      "The 3'-CCA amino acid acceptor stem",
      "The D loop exclusively",
      "The variable loop"],
     "A", "OSC", "easy",
     "The anticodon loop carries a unique three-base sequence that forms complementary antiparallel hydrogen bonds with the mRNA codon, translating nucleic acid sequence into specific amino acids."),

    # 76: Central Dogma of Molecular Biology Flow
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- DNA Box -->
  <rect x="25" y="60" width="85" height="50" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="67" y="85" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">DNA</text>
  <text x="67" y="100" fill="#93c5fd" font-size="8" font-family="sans-serif" text-anchor="middle">(Genes / Nucleus)</text>
  <!-- Arrow 1 (Transcription) -->
  <line x1="110" y1="85" x2="160" y2="85" stroke="#facc15" stroke-width="3"/>
  <text x="135" y="75" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Transcription</text>
  <!-- RNA Box -->
  <rect x="160" y="60" width="85" height="50" rx="6" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
  <text x="202" y="85" fill="#ec4899" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">mRNA</text>
  <text x="202" y="100" fill="#f472b6" font-size="8" font-family="sans-serif" text-anchor="middle">(Messenger)</text>
  <!-- Arrow 2 (Translation) -->
  <line x1="245" y1="85" x2="295" y2="85" stroke="#4ade80" stroke-width="3"/>
  <text x="270" y="75" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">Translation</text>
  <!-- Protein Box -->
  <rect x="295" y="60" width="85" height="50" rx="6" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
  <text x="337" y="85" fill="#22c55e" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">PROTEIN</text>
  <text x="337" y="100" fill="#86efac" font-size="8" font-family="sans-serif" text-anchor="middle">(Functional trait)</text>
  <!-- Central Dogma title -->
  <text x="200" y="35" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Francis Crick's Central Dogma (1958)</text>
  <text x="200" y="145" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">Replication: DNA copies itself | Reverse Transcription: RNA -> cDNA</text>
</svg>
</div>
In the Central Dogma workflow depicted above, what cellular process occurs at the ribosome where the linear codon sequence of mRNA is converted into an amino acid sequence?""",
     ["Translation", "Transcription", "Replication", "Splicing"],
     "A", "OSC", "easy",
     "Translation decodes mRNA triplets into polypeptide chains at the ribosome; transcription is the synthesis of mRNA from a DNA template in the nucleus."),

    # 77: The 3 Main RNA Types Comparison (mRNA, rRNA, tRNA)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- mRNA -->
  <rect x="20" y="25" width="110" height="140" rx="6" fill="#27272a" stroke="#38bdf8" stroke-width="2"/>
  <text x="75" y="48" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">mRNA (3-5%)</text>
  <text x="75" y="70" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">Messenger RNA</text>
  <text x="75" y="95" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Linear ribbon</text>
  <text x="75" y="115" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Carries genetic</text>
  <text x="75" y="130" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">message in codons</text>
  <!-- rRNA -->
  <rect x="145" y="25" width="110" height="140" rx="6" fill="#27272a" stroke="#4ade80" stroke-width="2"/>
  <text x="200" y="48" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">rRNA (80%)</text>
  <text x="200" y="70" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">Ribosomal RNA</text>
  <text x="200" y="95" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Forms ribosome</text>
  <text x="200" y="115" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Catalyzes peptide</text>
  <text x="200" y="130" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">bonds (Ribozyme)</text>
  <!-- tRNA -->
  <rect x="270" y="25" width="110" height="140" rx="6" fill="#27272a" stroke="#ec4899" stroke-width="2"/>
  <text x="325" y="48" fill="#ec4899" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">tRNA (15%)</text>
  <text x="325" y="70" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">Transfer RNA</text>
  <text x="325" y="95" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Cloverleaf shape</text>
  <text x="325" y="115" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Transports amino</text>
  <text x="325" y="130" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">acids to ribosome</text>
</svg>
</div>
Which class of cellular RNA constitutes the vast majority (approximately 80%) of total cellular RNA and serves as the structural and enzymatic core of ribosomes?""",
     ["Ribosomal RNA (rRNA)", "Messenger RNA (mRNA)", "Transfer RNA (tRNA)", "Micro RNA (miRNA)"],
     "A", "OSC", "easy",
     "Ribosomal RNA (rRNA) makes up about 80% of total RNA; it combines with proteins to construct ribosomes and acts as the catalytic peptidyl transferase ribozyme."),

    # 78: Semiconservative DNA Replication (Meselson & Stahl Model)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <!-- Parental Double Strand (Both 15N Blue) -->
  <line x1="80" y1="35" x2="80" y2="85" stroke="#38bdf8" stroke-width="4"/>
  <line x1="90" y1="35" x2="90" y2="85" stroke="#38bdf8" stroke-width="4"/>
  <text x="85" y="105" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle">Parent (15N / 15N)</text>
  <!-- Replication Arrow -->
  <line x1="125" y1="60" x2="175" y2="60" stroke="#facc15" stroke-width="3"/>
  <text x="150" y="50" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">1 Generation in 14N</text>
  <!-- Gen 1 Hybrid Strands (One 15N Blue, One 14N Pink) -->
  <line x1="220" y1="35" x2="220" y2="85" stroke="#38bdf8" stroke-width="4"/>
  <line x1="230" y1="35" x2="230" y2="85" stroke="#ec4899" stroke-width="4"/>
  <line x1="260" y1="35" x2="260" y2="85" stroke="#38bdf8" stroke-width="4"/>
  <line x1="270" y1="35" x2="270" y2="85" stroke="#ec4899" stroke-width="4"/>
  <text x="245" y="105" fill="#f472b6" font-size="9" font-family="sans-serif" text-anchor="middle">100% Hybrid (15N / 14N)</text>
  <!-- Explanation box -->
  <rect x="50" y="125" width="300" height="45" rx="6" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="200" y="145" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Semi-Conservative DNA Replication</text>
  <text x="200" y="160" fill="#bbf7d0" font-size="9" font-family="sans-serif" text-anchor="middle">Each daughter molecule receives ONE parental strand and ONE new strand</text>
</svg>
</div>
What fundamental discovery did Matthew Meselson and Franklin Stahl prove through their classic 15N/14N isotope centrifugation experiment?""",
     ["DNA replicates semi-conservatively, where each daughter DNA molecule retains one intact template strand from the parent and one newly synthesized strand",
      "DNA replicates completely conservatively where parents remain untouched",
      "DNA dissolves completely into water during cell division",
      "DNA is synthesized exclusively from amino acids"],
     "A", "OSC", "medium",
     "Meselson and Stahl confirmed Watson and Crick's semiconservative hypothesis: parental duplex strands separate, each acting as a physical template directing the synthesis of a complementary partner."),

    # 79: Purines vs Pyrimidines Chemical Ring Structure
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Purine Box -->
  <rect x="30" y="25" width="160" height="140" rx="6" fill="#27272a" stroke="#38bdf8" stroke-width="2"/>
  <text x="110" y="48" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">PURINES (Double Ring)</text>
  <polygon points="80,75 100,65 120,75 120,105 100,115 80,105" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="120,80 140,88 135,110 120,105" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <text x="110" y="135" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Adenine (A) & Guanine (G)</text>
  <text x="110" y="152" fill="#e2e8f0" font-size="8" font-family="sans-serif" text-anchor="middle">9-membered Bicyclic Ring</text>
  <!-- Pyrimidine Box -->
  <rect x="210" y="25" width="160" height="140" rx="6" fill="#27272a" stroke="#ec4899" stroke-width="2"/>
  <text x="290" y="48" fill="#ec4899" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">PYRIMIDINES (Single Ring)</text>
  <polygon points="270,75 290,65 310,75 310,105 290,115 270,105" fill="#9d174d" stroke="#ec4899" stroke-width="2"/>
  <text x="290" y="135" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Cytosine (C) & Thymine (T)</text>
  <text x="290" y="152" fill="#e2e8f0" font-size="8" font-family="sans-serif" text-anchor="middle">6-membered Monocyclic Ring (U in RNA)</text>
</svg>
</div>
How does pairing a double-ring purine (A or G) strictly with a single-ring pyrimidine (T or C) maintain the constant 2.0 nm (20 A) width of the DNA double helix?""",
     ["Combining a double-ring base with a single-ring base spans a uniform 3-ring distance (1.08 nm between C1' atoms) along the entire helix length",
      "Purines and pyrimidines shrink each other into identical spheres",
      "Two purines together would be too small to reach across the helix",
      "Two pyrimidines together would bulge the helix outward dangerously"],
     "A", "OSC", "hard",
     "A purine-purine pair would exceed the available 2.0 nm diameter, whereas a pyrimidine-pyrimidine pair would be too far apart to hydrogen bond; strict purine-pyrimidine pairing preserves a constant helical width."),

    # 80: Phosphodiester Backbone & 5' to 3' Growth
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#111827"/>
  <!-- Sugar 1 -->
  <rect x="70" y="30" width="80" height="35" rx="5" fill="#1e3a8a" stroke="#38bdf8" stroke-width="2"/>
  <text x="110" y="52" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">Deoxyribose 1</text>
  <!-- Phosphodiester Link -->
  <circle cx="110" cy="85" r="14" fill="#ca8a04" stroke="#facc15" stroke-width="2"/>
  <text x="110" y="89" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">PO4</text>
  <!-- Sugar 2 -->
  <rect x="70" y="115" width="80" height="35" rx="5" fill="#1e3a8a" stroke="#38bdf8" stroke-width="2"/>
  <text x="110" y="137" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">Deoxyribose 2</text>
  <!-- Annotations -->
  <line x1="124" y1="85" x2="200" y2="85" stroke="#facc15" stroke-width="2"/>
  <text x="210" y="80" fill="#facc15" font-size="10" font-family="sans-serif" font-weight="bold">Phosphodiester Bond</text>
  <text x="210" y="95" fill="#cbd5e1" font-size="9" font-family="sans-serif">Links C3'-OH of Sugar 1</text>
  <text x="210" y="110" fill="#cbd5e1" font-size="9" font-family="sans-serif">to C5'-Phosphate of Sugar 2</text>
  <text x="210" y="135" fill="#4ade80" font-size="9" font-family="sans-serif" font-weight="bold">Chain grows strictly 5' -> 3'</text>
</svg>
</div>
Why can DNA Polymerase enzymes synthesize new DNA strands strictly in the 5' -> 3' direction?""",
     ["DNA polymerase requires a free 3'-OH group to attack the incoming alpha-phosphate of a new dNTP substrate",
      "DNA polymerase only has eyes on one side",
      "5' ends of DNA are made of solid rock",
      "The cell has no 3' phosphate molecules"],
     "A", "OSC", "medium",
     "The 3'-hydroxyl group of the terminal deoxyribose performs a nucleophilic attack on the alpha-phosphate of the incoming deoxynucleoside triphosphate, restricting elongation strictly to the 5'-to-3' direction."),

    # 81: Major and Minor Grooves of DNA
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Helix silhouette -->
  <path d="M 80 20 Q 50 60 80 100 T 80 180" stroke="#38bdf8" stroke-width="6" fill="none"/>
  <path d="M 120 20 Q 150 60 120 100 T 120 180" stroke="#38bdf8" stroke-width="6" fill="none"/>
  <!-- Major Groove -->
  <rect x="150" y="45" width="220" height="40" rx="5" fill="#27272a" stroke="#facc15" stroke-width="2"/>
  <text x="260" y="62" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Major Groove (Wide & Deep)</text>
  <text x="260" y="76" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Exposes base edges for transcription factor recognition</text>
  <!-- Minor Groove -->
  <rect x="150" y="105" width="220" height="40" rx="5" fill="#27272a" stroke="#ec4899" stroke-width="2"/>
  <text x="260" y="122" fill="#ec4899" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Minor Groove (Narrow & Shallow)</text>
  <text x="260" y="136" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Formed by smaller angle between glycosidic bonds</text>
</svg>
</div>
What functional biological purpose is served by the major groove of the DNA double helix?""",
     ["It provides a spacious, chemically distinct pocket where sequence-specific transcription factors and DNA-binding proteins read base sequences without unwinding the helix",
      "It allows blood to circulate through chromosomes",
      "It catches waste products from cellular digestion",
      "It stores calcium ions for tooth enamel"],
     "A", "OSC", "hard",
     "The wide major groove exposes rich, distinct patterns of hydrogen-bond donors, acceptors, and methyl groups that enable regulatory proteins (e.g. zinc fingers, leucine zippers) to identify specific gene sequences."),

    # 82: Chargaff's Equimolar Rules Formula
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Equation Box -->
  <rect x="50" y="25" width="300" height="140" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="200" y="52" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">Erwin Chargaff's Rules (1950)</text>
  <text x="200" y="80" fill="#facc15" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">% Adenine = % Thymine  (A = T)</text>
  <text x="200" y="105" fill="#4ade80" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">% Guanine = % Cytosine  (G = C)</text>
  <text x="200" y="130" fill="#ec4899" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Total Purines (A + G) = Total Pyrimidines (T + C)</text>
  <text x="200" y="152" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">Ratio (A + G) / (T + C) = 1.0 in any double-stranded DNA</text>
</svg>
</div>
If a biochemical analysis reveals that a double-stranded bacterial chromosome contains 28% Cytosine, what percentage of Adenine does it contain according to Chargaff's rules?""",
     ["22% Adenine", "28% Adenine", "56% Adenine", "44% Adenine"],
     "A", "ONE", "medium",
     "If Cytosine = 28%, then complementary Guanine = 28% (total G + C = 56%). The remaining fraction is A + T = 100% - 56% = 44%. Since A = T, Adenine = 44% / 2 = 22%.")
]

all_questions = []

# Exam: 40 questions (1-40)
for idx, item in enumerate(exam_data):
    qnum = idx + 1
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "exam", "standard", item[5])
    )

# Practice: 30 questions (41-70)
for idx, item in enumerate(practice_data):
    qnum = idx + 41
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "practice", "standard", item[5])
    )

# Mock: 12 questions (71-82)
for idx, item in enumerate(mock_data):
    qnum = idx + 71
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "mock", "foundation", item[5])
    )

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE}")

output_path = os.path.join(os.path.dirname(__file__), "ch16_topic2.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
