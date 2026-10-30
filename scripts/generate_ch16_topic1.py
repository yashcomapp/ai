# scripts/generate_ch16_topic1.py
# MH-9-SCIT-16-16.1: Inheritance & Chromosome Types (Metacentric, Submetacentric, Acrocentric, Telocentric)
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-16-16.1"

exam_data = [
    # 1-10: Heredity, Variation & Chromosome Structure
    ("What biological term describes the transmission of physical and biological characters from parents to offspring?",
     ["Heredity (Inheritance)", "Evolution", "Mutation", "Regeneration"],
     "A", "OSC", "easy",
     "Heredity is the mechanism of genetic transfer by which ancestral anatomical, physiological, and biochemical traits pass from parents to progeny through gametes."),

    ("What are the subtle differences in morphological and physiological traits observed between individuals of the same species called?",
     ["Variations", "Speciation", "Cloning", "Adaptations"],
     "A", "OSC", "easy",
     "Variations represent the phenotypic differences exhibited by members of the same biological species, arising via sexual recombination and genetic mutation."),

    ("Where are chromosomes strictly situated inside a eukaryotic cell?",
     ["Inside the cell nucleus", "Floating freely in cytoplasm", "Inside the cell wall", "Within ribosomes"],
     "A", "OSC", "easy",
     "Chromosomes are dense nuclear structures composed of organized chromatin fibers located inside the eukaryotic nucleus, carrying genetic information."),

    ("What are the two major biochemical components that constitute the molecular framework of a eukaryotic chromosome?",
     ["DNA (Deoxyribonucleic acid) and basic histone proteins",
      "Cellulose and starch",
      "Hemoglobin and lipids",
      "Phospholipids and calcium"],
     "A", "OSC", "easy",
     "Chromosomes consist of nuclear chromatin, where double-stranded DNA wraps around octamers of basic histone proteins to form repeating nucleosome units."),

    ("What is the primary constriction point on a duplicated chromosome where sister chromatids are held together and spindle fibers attach during cell division?",
     ["Centromere (Primary constriction)", "Telomere", "Chromomere", "Pellicle"],
     "A", "OSC", "easy",
     "The centromere is the specialized constricted chromosomal region harboring the kinetochore protein complex, which coordinates mitotic spindle attachment."),

    ("What are the two identical longitudinal halves of a replicated metaphase chromosome called?",
     ["Sister chromatids", "Centrioles", "Chromomeres", "Chiasmata"],
     "A", "OSC", "easy",
     "During S-phase DNA replication, each chromosome duplicates into two identical sister chromatids attached at a shared centromere until anaphase separation."),

    ("The specialized terminal protective caps situated at the extreme ends of eukaryotic chromosome arms are known as:",
     ["Telomeres", "Centromeres", "Chromocenters", "Satellites"],
     "A", "OSC", "medium",
     "Telomeres are repetitive non-coding hexanucleotide sequences capping chromosome ends, preventing chromosomal degradation and end-to-end fusion."),

    ("On a chromosome with unequal arm lengths, the shorter arm is designated as the ________ arm, while the longer arm is designated as the ________ arm.",
     ["p arm ; q arm", "q arm ; p arm", "alpha arm ; beta arm", "x arm ; y arm"],
     "A", "OSC", "medium",
     "In cytogenetic nomenclature, the short arm is designated 'p' (from the French 'petit'), and the long arm is designated 'q' (the next letter in the alphabet)."),

    ("A chromosome having its centromere located exactly in the middle, dividing it into two equal arms and resembling the letter 'V' during anaphase, is classified as:",
     ["Metacentric", "Submetacentric", "Acrocentric", "Telocentric"],
     "A", "OSC", "easy",
     "Metacentric chromosomes feature a median centromere yielding equal arm lengths (p = q); poleward traction during anaphase pulls them into a characteristic V-shape."),

    ("A chromosome with its centromere located slightly away from the midpoint, forming one slightly shorter arm and one longer arm, appearing like the letter 'L' during anaphase, is:",
     ["Submetacentric", "Metacentric", "Acrocentric", "Telocentric"],
     "A", "OSC", "easy",
     "Submetacentric chromosomes possess a submedian centromere creating unequal arms; movement through viscous cytoplasm gives them an L-shaped appearance at anaphase."),

    # 11-20: Chromosome Types & Ploidy
    ("A chromosome having its centromere located near one end, producing one extremely short arm and one very long arm, appearing like the letter 'J' during anaphase, is called:",
     ["Acrocentric", "Telocentric", "Metacentric", "Submetacentric"],
     "A", "OSC", "easy",
     "Acrocentric chromosomes have a subterminal centromere yielding a miniscule short arm (often bearing a nucleolar satellite) and a long arm, assuming a J-shape during division."),

    ("A chromosome whose centromere is positioned at the absolute terminal tip, possessing only a single visible arm and resembling a rod or letter 'i' at anaphase, is:",
     ["Telocentric", "Metacentric", "Submetacentric", "Acrocentric"],
     "A", "OSC", "easy",
     "Telocentric chromosomes feature a strictly terminal centromere; lacking a second arm, they trail behind the kinetochore like a straight rod or letter 'i'."),

    ("How many total chromosomes (and pairs) are present in the somatic body cells of a normal human being?",
     ["46 chromosomes (23 pairs)", "23 chromosomes (46 pairs)", "48 chromosomes (24 pairs)", "44 chromosomes (22 pairs)"],
     "A", "OSC", "easy",
     "Normal human diploid somatic cells contain 46 chromosomes organized into 23 homologous pairs (22 pairs of autosomes and 1 pair of sex chromosomes)."),

    ("How many pairs of AUTOSOMES (non-sex chromosomes) are present in every human diploid somatic cell?",
     ["22 pairs (44 chromosomes)", "23 pairs (46 chromosomes)", "1 pair (2 chromosomes)", "21 pairs (42 chromosomes)"],
     "A", "OSC", "easy",
     "Human cells possess 22 pairs of somatic autosomes (numbered 1 through 22 in order of descending size) which regulate general body characteristics."),

    ("What are the sex chromosomes (allosomes) present in a normal human biological female and male, respectively?",
     ["Female: XX ; Male: XY", "Female: XY ; Male: XX", "Female: YY ; Male: XX", "Female: XO ; Male: YO"],
     "A", "OSC", "easy",
     "Females are homogametic, having two morphologically similar X chromosomes (XX); males are heterogametic, possessing one X and one smaller Y chromosome (XY)."),

    ("What is the chromosome number found in human haploid gametes (sperm and egg cells)?",
     ["23 chromosomes", "46 chromosomes", "92 chromosomes", "12 chromosomes"],
     "A", "OSC", "easy",
     "Meiotic reduction division halves the diploid number (2n = 46) so that mature gametes contain exactly one haploid set of chromosomes (n = 23)."),

    ("How many chromosomes are present in a somatic body cell of the fruit fly (Drosophila melanogaster)?",
     ["8 chromosomes (4 pairs)", "46 chromosomes", "26 chromosomes", "12 chromosomes"],
     "A", "OSC", "medium",
     "The fruit fly (Drosophila melanogaster) has a compact genome with 2n = 8 chromosomes (3 pairs of autosomes and 1 pair of sex chromosomes)."),

    ("In which phase of eukaryotic cell division are chromosomes most condensed, distinct, and optimal for microscopic karyotyping and counting?",
     ["Metaphase", "Interphase", "Telophase", "G1 phase"],
     "A", "OSC", "medium",
     "At mitotic metaphase, chromatin reaches maximum condensation along the equatorial plate, making individual chromatids and centromeres sharply visible under brightfield microscopy."),

    ("What cytogenetic term describes an organized visual photographic arrangement of a cell's complete chromosome complement paired and ordered by size?",
     ["Karyotype", "Genotype", "Phenotype", "Serotype"],
     "A", "OSC", "medium",
     "A karyotype is a standardized display of homologous chromosome pairs arranged systematically from largest to smallest, used to detect numerical and structural aberrations."),

    ("Which roundworm species holds the distinction of having one of the lowest chromosome numbers in the animal kingdom, with only 2 chromosomes (1 pair) in somatic cells?",
     ["Ascaris megalocephala univalens", "Caenorhabditis elegans", "Taenia solium", "Fasciola hepatica"],
     "A", "OSC", "hard",
     "Ascaris megalocephala univalens possesses 2n = 2 chromosomes in its germline cells, representing the minimum possible diploid count in metazoans."),

    # 21-30: Centromere Positions, Homologous Pairs & Gene Loci
    ("Chromosomes that are identical in size, shape, centromere location, and carry genes for the same traits at identical loci are called:",
     ["Homologous chromosomes", "Non-homologous chromosomes", "Heterochromatin", "Polytene chromosomes"],
     "A", "OSC", "easy",
     "Homologous chromosomes are matching paternal and maternal chromosome pairs that synapse during prophase I of meiosis and share identical gene loci."),

    ("What is the specific physical location or address of a gene along the length of a chromosome called?",
     ["Locus (plural: loci)", "Centromere", "Chiasma", "Allelomorph"],
     "A", "OSC", "medium",
     "A gene locus denotes the fixed linear coordinate of a specific gene on a chromosome; alleles of the same gene occupy homologous loci."),

    ("The rounded knob-like body separated from the main body of an acrocentric chromosome by a secondary constriction is known as a:",
     ["Satellite (SAT body)", "Telomere", "Centrosome", "Kinetochore"],
     "A", "OSC", "medium",
     "SAT chromosomes possess a secondary constriction (nucleolar organizer region) demarcating a distal terminal chromosomal knob called a satellite."),

    ("During mitotic anaphase, if a chromosome is being dragged toward the spindle pole by its centromere and forms an inverted 'V', what type of chromosome is it?",
     ["Metacentric", "Telocentric", "Acrocentric", "Submetacentric"],
     "A", "OSC", "easy",
     "Equal arm lengths on both sides of a median centromere experience symmetrical hydrodynamic drag during anaphase, bending the chromosome into a classic V-shape."),

    ("Which sex chromosome in humans is physically smaller and carries the SRY gene responsible for triggering male embryonic testis development?",
     ["Y chromosome", "X chromosome", "Chromosome 21", "Chromosome 1"],
     "A", "OSC", "easy",
     "The human Y chromosome is roughly one-third the size of the X chromosome and harbors the Sex-determining Region Y (SRY) gene which initiates male gonadogenesis."),

    ("A cell containing TWO complete sets of homologous chromosomes (one maternal, one paternal) is described by the ploidy term:",
     ["Diploid (2n)", "Haploid (n)", "Triploid (3n)", "Aneuploid"],
     "A", "OSC", "easy",
     "Somatic cells with paired homologous chromosomes are diploid (2n), whereas gametes carrying a single set of unpaired chromosomes are haploid (n)."),

    ("State whether True or False: Telocentric chromosomes naturally do NOT occur in normal human somatic karyotypes.",
     ["True", "False"],
     "A", "OTF", "medium",
     "Human karyotypes contain metacentric, submetacentric, and acrocentric chromosomes (groups A through G), but no truly telocentric chromosomes exist naturally in humans."),

    ("How many chromosomes are present in a somatic body cell of a chimpanzee (Pan troglodytes)?",
     ["48 chromosomes (24 pairs)", "46 chromosomes", "42 chromosomes", "52 chromosomes"],
     "A", "OSC", "medium",
     "Chimpanzees possess 2n = 48 chromosomes; ancestral telomeric fusion of two ape acrocentric chromosomes created human chromosome 2, giving humans 46."),

    ("What is the term for the dense, dark-staining, transcriptionally inactive region of chromatin in interphase nuclei?",
     ["Heterochromatin", "Euchromatin", "Nucleoplasm", "Polysome"],
     "A", "OSC", "medium",
     "Heterochromatin remains tightly condensed throughout the cell cycle, repressing gene transcription; transcriptionally active, loosely packed chromatin is euchromatin."),

    ("The proteinaceous disc-like structure assembled on the centromeric DNA that physically captures spindle microtubules is called the:",
     ["Kinetochore", "Centrosome", "Centriole", "Aster"],
     "A", "OSC", "hard",
     "The kinetochore is a trilaminar multiprotein complex assembled directly upon centromeric alpha-satellite DNA, generating poleward force during chromatid segregation."),

    # 31-40: Fill in blanks, Numerical, Multi-choice
    ("The total number of chromosome pairs in the somatic cells of a normal human being is ________ pairs.",
     ["23", "46", "22", "44"],
     "A", "ONE", "easy",
     "Humans have 23 pairs of chromosomes, comprising 22 autosomal pairs and 1 sex chromosome pair."),

    ("A human male sperm cell carries 22 autosomes and either one ________ or one ________ chromosome.",
     ["X ; Y", "X ; X", "Y ; Y", "Z ; W"],
     "A", "OFB", "easy",
     "Spermatogenesis produces two equal populations of sperm: 50% carrying 22+X and 50% carrying 22+Y, determining the biological sex of the fertilized zygote."),

    ("An unfertilized human ovum (egg cell) normally contains ________ autosomes and one X chromosome.",
     ["22", "23", "44", "46"],
     "A", "ONE", "easy",
     "Female oogenesis produces gametes that invariably contain 22 autosomes and exactly one X chromosome (22+X)."),

    ("Which of the following chromosome morphological shapes correspond to their anaphase movement configurations? (Select all that apply)",
     ["Metacentric = V-shape, Submetacentric = L-shape, Acrocentric = J-shape, Telocentric = i-shape (rod)",
      "Only Metacentric = V-shape and Telocentric = round",
      "All chromosomes form straight circles during anaphase",
      "Only Submetacentric = X-shape"],
     "A", "OMC", "easy",
     "Centromere position dictates hydrodynamic bending during poleward migration: median yields V, submedian yields L, subterminal yields J, and terminal yields i (rod)."),

    ("State whether True or False: In humans, the father's sperm determines the biological sex of the unborn child.",
     ["True", "False"],
     "A", "OTF", "easy",
     "The mother always contributes an X chromosome; if a sperm carrying an X fertilizes the egg, the child is female (XX), and if a Y sperm fertilizes it, the child is male (XY)."),

    ("Assertion (A): Gametes must be haploid (n) rather than diploid (2n).\nReason (R): Haploid gametes ensure that syngamy (fertilization) restores the species-specific constant diploid (2n) chromosome number in the offspring.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is not the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "easy",
     "Meiotic halving of chromosome sets prevents the geometric doubling of chromosome number across successive sexual generations, preserving genetic stability."),

    ("What is the ratio of arm lengths (p : q) in a perfectly metacentric chromosome?",
     ["1 : 1 (equal arm lengths)", "1 : 3", "1 : 10", "0 : 1"],
     "A", "OSC", "easy",
     "A metacentric chromosome has its centromere at the geometric center, resulting in an arm ratio of p/q = 1.0."),

    ("Which organism among the following has 78 chromosomes (39 pairs) in its somatic body cells?",
     ["Domestic dog (Canis familiaris)", "Human", "Fruit fly", "Frog"],
     "A", "OSC", "medium",
     "Domestic dogs possess 2n = 78 chromosomes, consisting of 38 pairs of acrocentric autosomes and 1 pair of sex chromosomes."),

    ("Secondary constrictions on certain human acrocentric chromosomes (such as chromosomes 13, 14, 15, 21, and 22) contain genes that transcribe:",
     ["Ribosomal RNA (rRNA) in the nucleolus (Nucleolar Organizer Regions / NOR)",
      "Hemoglobin protein",
      "Insulin exclusively",
      "Keratin for hair"],
     "A", "OSC", "hard",
     "Nucleolar Organizer Regions (NORs) at secondary constrictions house tandem clusters of ribosomal DNA genes that direct rRNA synthesis and assemble the nucleolus."),

    ("What structural change occurs to chromosomes during interphase compared to metaphase?",
     ["During interphase, chromosomes decondense into a diffuse, loose network of chromatin threads for transcription and replication",
      "Chromosomes dissolve completely into pure water",
      "Chromosomes leave the cell and travel through blood",
      "Chromosomes fuse into one giant crystal"],
     "A", "OSC", "medium",
     "Chromatin remains dispersed and uncoiled during interphase to grant RNA polymerase access to genes, condensing into discrete chromosomes only for mitosis.")
]

practice_data = [
    # 41-50: Advanced Cytogenetics & Mechanics
    ("Why do homologous chromosomes pair up exclusively during Prophase I of meiosis but NOT during mitotic prophase?",
     ["Meiotic synapsis allows genetic crossing-over between non-sister chromatids to generate novel allelic combinations",
      "Mitosis has no chromosomes",
      "Meiosis occurs only in plant leaves",
      "Homologous pairing prevents cell division"],
     "A", "OSC", "medium",
     "The synaptonemal complex zips homologous chromosomes together during pachytene of meiosis I, mediating reciprocal DNA exchange (crossing over) to foster diversity."),

    ("If an organism has a diploid chromosome number of 2n = 16, how many chromatids are present in a single somatic cell at mitotic metaphase?",
     ["32 chromatids", "16 chromatids", "64 chromatids", "8 chromatids"],
     "A", "ONE", "medium",
     "Each of the 16 replicated chromosomes consists of 2 sister chromatids during metaphase, yielding 16 x 2 = 32 individual chromatids."),

    ("What is an ideogram in cytogenetics?",
     ["A standardized diagrammatic schematic representation of a chromosome karyotype showing band patterns and arm lengths",
      "A photograph of a single cell membrane",
      "A graph showing blood pressure changes",
      "An electronic machine that measures heartbeat"],
     "A", "OSC", "medium",
     "An ideogram provides a calibrated diagrammatic map illustrating chromosomal G-banding landmarks, centromere locations, and relative arm proportions."),

    ("Which staining technique produces alternating light and dark bands along the length of chromosomes using trypsin digestion and Giemsa dye?",
     ["G-banding (Giemsa banding)", "Gram staining", "Iodine staining", "Methylene blue staining"],
     "A", "OSC", "medium",
     "G-banding is the gold-standard cytogenetic staining technique; AT-rich heterochromatic regions stain darkly, producing distinct reproducible banding patterns."),

    ("In human karyotyping, chromosome pairs are classified into seven groups designated A through G based on size and centromere position. Chromosome 1 belongs to:",
     ["Group A (large metacentric)", "Group G (small acrocentric)", "Group D (medium acrocentric)", "Group E (small submetacentric)"],
     "A", "OSC", "hard",
     "Group A comprises the largest chromosomes (pairs 1, 2, and 3); Chromosome 1 is the largest metacentric chromosome in the human genome."),

    ("State whether True or False: Acrocentric chromosomes 13, 14, 15, 21, and 22 in humans are prone to Robertsonian translocations because of their small p arms.",
     ["True", "False"],
     "A", "OTF", "hard",
     "Robertsonian translocations occur when two acrocentric chromosomes break at their centromeres and their long q arms fuse, creating a single derivative chromosome."),

    ("If a mother has blood type alleles IA and IB, these two distinct alleles occupy:",
     ["The exact same locus on homologous copies of Chromosome 9",
      "Different chromosomes entirely (one on Chromosome 1 and one on Chromosome 2)",
      "The cytoplasm outside the nucleus",
      "Only the Y chromosome"],
     "A", "OSC", "medium",
     "Allelic variants of a gene occupy corresponding loci on maternal and paternal homologous chromosomes; the ABO glycosyltransferase gene resides on 9q34.2."),

    ("What prevents the ends of two different chromosomes from adhering and fusing together inside the nucleus?",
     ["Specialized shelterin protein complexes binding to repetitive telomeric DNA caps",
      "A thick layer of cellulose between chromosomes",
      "High electrostatic repulsion from cell wall ions",
      "Continuous movement of mitochondria"],
     "A", "OSC", "hard",
     "The shelterin multi-protein complex sequesters single-stranded 3' telomeric overhangs into protective T-loops, preventing them from being recognized as double-strand DNA breaks."),

    ("Which organism has 26 chromosomes (13 pairs) in its diploid somatic cells?",
     ["Frog (Rana tigrina)", "Human", "Dog", "Fruit fly"],
     "A", "OSC", "medium",
     "The Indian bullfrog (Hoplobatrachus tigerinus / Rana tigrina) possesses a diploid chromosome complement of 2n = 26."),

    ("How does the chromosome composition of a human mature sperm cell differ from that of a somatic skin cell?",
     ["Sperm: 23 single chromosomes (22 autosomes + 1 sex chromosome); Skin cell: 46 chromosomes in 23 pairs (44 autosomes + 2 sex chromosomes)",
      "Sperm has no chromosomes while skin cell has 100",
      "Sperm has 46 pairs of chromosomes",
      "Sperm cell has only autosomes and no sex chromosomes"],
     "A", "OSC", "easy",
     "Meiotic reduction during spermatogenesis yields haploid gametes with n = 23 chromosomes, whereas mitotically maintained somatic cells remain diploid with 2n = 46.")
]

# Additional 20 practice questions to make practice_data exactly 30 questions
practice_data.extend([
    # 51-60: Further Ploidy & Structure Concepts
    ("What term describes a chromosomal mutation where an individual gains or loses one or more individual chromosomes (e.g., 2n + 1 or 2n - 1)?",
     ["Aneuploidy", "Polyploidy", "Inversion", "Duplication"],
     "A", "OSC", "medium",
     "Aneuploidy involves non-disjunction errors leading to an abnormal chromosome count differing by individual chromosomes rather than whole sets."),

    ("When whole extra sets of chromosomes are added to an organism's genome (e.g., 3n, 4n, 6n), the condition is called:",
     ["Polyploidy", "Aneuploidy", "Trisomy", "Monosomy"],
     "A", "OSC", "medium",
     "Polyploidy involves the presence of multiple complete sets of chromosomes, common in flowering plants (e.g., hexaploid wheat) and agricultural crops."),

    ("Which basic amino acids are abundantly present in histone proteins to confer a positive electrical charge that binds tightly to negatively charged DNA?",
     ["Lysine and Arginine", "Glycine and Alanine", "Valine and Leucine", "Tryptophan and Phenylalanine"],
     "A", "OSC", "hard",
     "Histones are rich in positively charged basic amino acids (lysine and arginine), creating electrostatic bonds with the negatively charged phosphodiester backbone of DNA."),

    ("What is the fundamental repeating unit of chromatin packaging consisting of 147 base pairs of DNA wound around a histone octamer core?",
     ["Nucleosome", "Chromomere", "Centrosome", "Telomere"],
     "A", "OSC", "medium",
     "The nucleosome is the primary packaging unit resembling 'beads-on-a-string', where DNA wraps 1.65 turns around an octamer of H2A, H2B, H3, and H4 histones."),

    ("State whether True or False: The Y chromosome in human males contains significantly fewer protein-coding genes than the X chromosome.",
     ["True", "False"],
     "A", "OTF", "easy",
     "The human X chromosome carries over 900-1400 genes, whereas the diminutive Y chromosome contains only about 50-70 protein-coding genes, predominantly involved in male sex determination and spermatogenesis."),

    ("A chromosome configuration where the centromere is so close to the end that the p-arm appears as small satellite stalks is termed:",
     ["Acrocentric", "Metacentric", "Holocentric", "Dicentric"],
     "A", "OSC", "easy",
     "In acrocentric chromosomes, the centromere is positioned near the terminus, reducing the short arm to a tiny stalk often capped with a satellite knob."),

    ("In which organ in the human male body does meiotic reduction division occur to produce haploid sperm cells?",
     ["Testes (seminiferous tubules)", "Prostate gland", "Epididymis", "Urinary bladder"],
     "A", "OSC", "easy",
     "Spermatogenesis takes place within the seminiferous tubules of the testes, where diploid primary spermatocytes undergo meiosis to generate haploid spermatids."),

    ("What is the function of the centromere during mitotic anaphase?",
     ["It serves as the assembly site for the kinetochore that directs sister chromatids toward opposite spindle poles",
      "It dissolves the spindle fibers completely",
      "It makes copies of cell membranes",
      "It produces ribosomes for protein synthesis"],
     "A", "OSC", "medium",
     "Centromeres recruit inner and outer kinetochore plates that anchor plus-ends of kinetochore microtubules, guiding equitable chromatid segregation."),

    ("Which of the following organisms has a haploid chromosome number of n = 12 (and diploid 2n = 24)?",
     ["Tomato (Solanum lycopersicum) and Rice (Oryza sativa)", "Human", "Dog", "Roundworm"],
     "A", "OSC", "medium",
     "Both rice (Oryza sativa) and tomato plants possess 2n = 24 chromosomes, meaning their haploid gametes possess n = 12 chromosomes."),

    ("State whether True or False: In birds, females are heterogametic (ZW) while males are homogametic (ZZ).",
     ["True", "False"],
     "A", "OTF", "medium",
     "Unlike mammals where males are heterogametic (XY), in birds, butterflies, and some reptiles, the female produces two types of gametes (ZW) and dictates offspring sex."),

    # 61-70: High-Yield Cytogenetics & Variation
    ("What is the evolutionary benefit of chromosomal crossing-over and sexual reproduction over asexual cloning?",
     ["Generating novel genetic combinations that enhance adaptability and survival against changing environmental pressures and pathogens",
      "Ensuring all offspring are 100% identical clones",
      "Preventing cells from dividing",
      "Keeping chromosome numbers strictly at zero"],
     "A", "OSC", "easy",
     "Crossing over shuffles maternal and paternal alleles into novel combinations, providing the raw genetic diversity necessary for natural selection."),

    ("If a tissue sample shows cells having 92 chromatids organized as 46 duplicated chromosomes aligned at the cell equator, what phase of mitosis is underway?",
     ["Metaphase", "Anaphase", "Telophase", "Interphase"],
     "A", "OSC", "medium",
     "At metaphase, all 46 duplicated chromosomes line up along the metaphase plate; each consists of 2 sister chromatids, totaling 92 chromatids."),

    ("Which chromosome in the human genome is the physically largest and carries the highest number of protein-coding genes (over 2,000 genes)?",
     ["Chromosome 1", "Chromosome 21", "X chromosome", "Y chromosome"],
     "A", "OSC", "medium",
     "Human Chromosome 1 is the largest autosome, spanning approximately 249 million base pairs and harboring over 2,000 identified protein-coding genes."),

    ("Which human autosome is the smallest in terms of physical length and base pairs, yet was numbered 21 due to historical staining conventions?",
     ["Chromosome 21 (or 22)", "Chromosome 1", "Chromosome 7", "Chromosome 10"],
     "A", "OSC", "medium",
     "Chromosome 21 is cytogenetically the smallest autosome (~47 million base pairs), whose triplication results in Down syndrome."),

    ("What does the notation '46, XX' signify in standard international cytogenetic nomenclature?",
     ["A normal human biological female having 46 total chromosomes including two X chromosomes",
      "A male with 46 chromosomes",
      "A chimpanzee with 46 chromosomes",
      "A cell with 92 chromosomes"],
     "A", "OSC", "easy",
     "The formula '46, XX' designates a normal human female karyotype: 46 total chromosomes with two homologous sex chromosomes (XX)."),

    ("What does the notation '46, XY' represent in cytogenetics?",
     ["A normal human biological male having 46 total chromosomes including one X and one Y chromosome",
      "A female with 46 chromosomes",
      "A cell lacking sex chromosomes",
      "A bacterial chromosome"],
     "A", "OSC", "easy",
     "In human cytogenetics, '46, XY' denotes a normal human male karyotype containing 22 pairs of autosomes plus one X and one Y sex chromosome."),

    ("A chromosome that possesses TWO centromeres as a result of an abnormal chromosomal fusion event is called a:",
     ["Dicentric chromosome", "Acentric fragment", "Metacentric chromosome", "Ring chromosome"],
     "A", "OSC", "hard",
     "Dicentric chromosomes carry two centromeres; during anaphase, spindle fibers pulling toward opposite poles can form an anaphase bridge and tear the chromosome."),

    ("A broken chromosomal fragment that completely lacks a centromere is called an ________ fragment and is lost during subsequent cell divisions.",
     ["acentric", "holocentric", "telomeric", "isochromosome"],
     "A", "OFB", "medium",
     "Without a centromere/kinetochore, an acentric fragment cannot anchor to mitotic spindle microtubules and fails to migrate, being lost during cytokinesis."),

    ("State whether True or False: Somatic body cells divide by mitosis to maintain the constant diploid (2n) chromosome count, whereas germline cells undergo meiosis.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Mitosis is equational division producing identical 2n daughter somatic cells; meiosis is reductional division producing genetically unique haploid (n) gametes."),

    ("How many pairs of chromosomes are categorized as autosomes in the domestic dog (2n = 78)?",
     ["38 pairs (76 autosomes)", "39 pairs", "1 pair", "23 pairs"],
     "A", "ONE", "medium",
     "In dogs (2n = 78), 76 chromosomes form 38 pairs of autosomes, while the remaining 2 chromosomes form 1 pair of allosomes (XX or XY).")
])

mock_data = [
    # 71: Chromosome Anatomy (Chromatids, Centromere, Telomeres, p & q arms)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="210" viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="210" rx="8" fill="#090d16"/>
  <!-- Sister Chromatid 1 -->
  <path d="M 120 25 Q 110 65 130 95 Q 110 135 120 185" stroke="#38bdf8" stroke-width="8" stroke-linecap="round" fill="none"/>
  <!-- Sister Chromatid 2 -->
  <path d="M 160 25 Q 170 65 150 95 Q 170 135 160 185" stroke="#38bdf8" stroke-width="8" stroke-linecap="round" fill="none"/>
  <!-- Centromere -->
  <circle cx="140" cy="95" r="9" fill="#facc15" stroke="#ffffff" stroke-width="2"/>
  <text x="140" y="99" fill="#000000" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">C</text>
  <!-- Telomeres -->
  <circle cx="120" cy="25" r="6" fill="#ec4899"/>
  <circle cx="160" cy="25" r="6" fill="#ec4899"/>
  <circle cx="120" cy="185" r="6" fill="#ec4899"/>
  <circle cx="160" cy="185" r="6" fill="#ec4899"/>
  <!-- Labels -->
  <line x1="166" y1="25" x2="220" y2="25" stroke="#ec4899" stroke-width="2"/>
  <text x="230" y="29" fill="#ec4899" font-size="10" font-family="sans-serif" font-weight="bold">Telomere (Protective cap)</text>
  <line x1="150" y1="60" x2="220" y2="60" stroke="#38bdf8" stroke-width="2"/>
  <text x="230" y="64" fill="#38bdf8" font-size="10" font-family="sans-serif" font-weight="bold">Short arm (p arm)</text>
  <line x1="150" y1="95" x2="220" y2="95" stroke="#facc15" stroke-width="2"/>
  <text x="230" y="99" fill="#facc15" font-size="10" font-family="sans-serif" font-weight="bold">Centromere (Primary constriction)</text>
  <line x1="150" y1="145" x2="220" y2="145" stroke="#38bdf8" stroke-width="2"/>
  <text x="230" y="149" fill="#38bdf8" font-size="10" font-family="sans-serif" font-weight="bold">Long arm (q arm)</text>
  <line x1="166" y1="185" x2="220" y2="185" stroke="#ec4899" stroke-width="2"/>
  <text x="230" y="189" fill="#ec4899" font-size="10" font-family="sans-serif" font-weight="bold">Sister Chromatids (Duplicated)</text>
</svg>
</div>
In the labeled metaphase chromosome diagram above, what essential function is performed by the primary constriction (centromere)?""""",
     ["It holds the two replicated sister chromatids together and serves as the anchor point for spindle fiber attachment during cell division",
      "It synthesizes hemoglobin for blood cells",
      "It dissolves the nuclear envelope permanently",
      "It stores water for photosynthesis"],
     "A", "OSC", "medium",
     "The centromere maintains sister chromatid cohesion until anaphase and assembles the kinetochore protein complex that anchors spindle microtubules for chromatid segregation."),

    # 72: The 4 Types of Chromosomes (Metacentric, Submetacentric, Acrocentric, Telocentric)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="210" viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="210" rx="8" fill="#18181b"/>
  <!-- Metacentric (V) -->
  <line x1="50" y1="30" x2="50" y2="80" stroke="#38bdf8" stroke-width="5" stroke-linecap="round"/>
  <circle cx="50" cy="80" r="5" fill="#facc15"/>
  <line x1="50" y1="80" x2="50" y2="130" stroke="#38bdf8" stroke-width="5" stroke-linecap="round"/>
  <text x="50" y="155" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Metacentric</text>
  <text x="50" y="170" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle">Equal arms (V)</text>
  <!-- Submetacentric (L) -->
  <line x1="140" y1="45" x2="140" y2="75" stroke="#4ade80" stroke-width="5" stroke-linecap="round"/>
  <circle cx="140" cy="75" r="5" fill="#facc15"/>
  <line x1="140" y1="75" x2="140" y2="135" stroke="#4ade80" stroke-width="5" stroke-linecap="round"/>
  <text x="140" y="155" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Submetacentric</text>
  <text x="140" y="170" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle">Slightly unequal (L)</text>
  <!-- Acrocentric (J) -->
  <line x1="240" y1="65" x2="240" y2="75" stroke="#ec4899" stroke-width="5" stroke-linecap="round"/>
  <circle cx="240" cy="75" r="5" fill="#facc15"/>
  <line x1="240" y1="75" x2="240" y2="140" stroke="#ec4899" stroke-width="5" stroke-linecap="round"/>
  <text x="240" y="155" fill="#ec4899" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Acrocentric</text>
  <text x="240" y="170" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle">Near one end (J)</text>
  <!-- Telocentric (i) -->
  <circle cx="340" cy="70" r="5" fill="#facc15"/>
  <line x1="340" y1="70" x2="340" y2="140" stroke="#a855f7" stroke-width="5" stroke-linecap="round"/>
  <text x="340" y="155" fill="#a855f7" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Telocentric</text>
  <text x="340" y="170" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle">Terminal (i / rod)</text>
</svg>
</div>
Based on the four morphological types of chromosomes categorized by centromere position above, which type appears as a 'J' shape during anaphase due to having one very short arm and one very long arm?""""",
     ["Acrocentric chromosome", "Metacentric chromosome", "Submetacentric chromosome", "Telocentric chromosome"],
     "A", "OSC", "easy",
     "Acrocentric chromosomes feature a subterminal centromere; hydrodynamic drag on the tiny p arm and long q arm bends them into an asymmetrical 'J' shape at anaphase."),

    # 73: Metaphase Anaphase Movement Shapes (V, L, J, i)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#111827"/>
  <!-- Pole -->
  <line x1="30" y1="20" x2="370" y2="20" stroke="#475569" stroke-width="2" stroke-dasharray="4"/>
  <text x="200" y="15" fill="#94a3b8" font-size="9" font-family="sans-serif" text-anchor="middle">Anaphase Spindle Pole Direction (Traction ^)</text>
  <!-- V Shape -->
  <path d="M 40 85 L 65 35 L 90 85" stroke="#38bdf8" stroke-width="4" stroke-linecap="round" fill="none"/>
  <circle cx="65" cy="35" r="4" fill="#facc15"/>
  <text x="65" y="115" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">'V' Shape</text>
  <text x="65" y="130" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">(Metacentric)</text>
  <!-- L Shape -->
  <path d="M 140 60 L 160 35 L 180 95" stroke="#4ade80" stroke-width="4" stroke-linecap="round" fill="none"/>
  <circle cx="160" cy="35" r="4" fill="#facc15"/>
  <text x="160" y="115" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">'L' Shape</text>
  <text x="160" y="130" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">(Submetacentric)</text>
  <!-- J Shape -->
  <path d="M 250 48 L 260 35 L 270 100" stroke="#ec4899" stroke-width="4" stroke-linecap="round" fill="none"/>
  <circle cx="260" cy="35" r="4" fill="#facc15"/>
  <text x="260" y="115" fill="#ec4899" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">'J' Shape</text>
  <text x="260" y="130" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">(Acrocentric)</text>
  <!-- i Shape -->
  <line x1="345" y1="35" x2="345" y2="100" stroke="#a855f7" stroke-width="4" stroke-linecap="round"/>
  <circle cx="345" cy="35" r="4" fill="#facc15"/>
  <text x="345" y="115" fill="#a855f7" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">'i' Shape</text>
  <text x="345" y="130" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">(Telocentric)</text>
</svg>
</div>
Why do chromosomes assume distinct V, L, J, and i shapes specifically during anaphase of cell division?""""",
     ["Centromeres are actively pulled toward the spindle poles while the trailing arms experience resistance from the viscous cytoplasm",
      "Spindle fibers melt the chromosome arms into flexible rubber",
      "The nuclear membrane twists chromosomes into letters of the alphabet",
      "Gravity pulls chromosomes toward the bottom of the cell"],
     "A", "OSC", "medium",
     "Kinetochore microtubules apply traction force directly at the centromere; the trailing chromosome arms encounter cytoplasmic hydrodynamic resistance, flexing into characteristic shapes depending on centromere placement."),

    # 74: Human Karyotype Map (Autosomes 1-22 vs Sex Chromosomes XX / XY)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#0f172a"/>
  <!-- Autosomes Box -->
  <rect x="25" y="25" width="230" height="150" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="140" y="50" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">AUTOSOMES (Pairs 1 to 22)</text>
  <text x="140" y="75" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Exactly 22 homologous pairs (44 total)</text>
  <text x="140" y="95" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Morphologically identical in both sexes</text>
  <text x="140" y="115" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Control somatic and physiological traits</text>
  <text x="140" y="145" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">44 Autosomes in every somatic cell</text>
  <!-- Sex Chromosomes Box -->
  <rect x="270" y="25" width="105" height="150" rx="6" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
  <text x="322" y="50" fill="#ec4899" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">ALLOSOMES</text>
  <text x="322" y="70" fill="#f472b6" font-size="9" font-family="sans-serif" text-anchor="middle">(Pair 23)</text>
  <text x="322" y="95" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Female: XX</text>
  <text x="322" y="125" fill="#60a5fa" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Male: XY</text>
  <text x="322" y="155" fill="#e2e8f0" font-size="8" font-family="sans-serif" text-anchor="middle">Sex Determination</text>
</svg>
</div>
In the human chromosomal classification depicted above, what distinguishes autosomes from allosomes (sex chromosomes)?""""",
     ["Autosomes (pairs 1-22) govern general somatic body characters and are identical in males and females, whereas allosomes (pair 23) determine biological sex",
      "Autosomes have no DNA while allosomes are made of pure protein",
      "Autosomes are found only in blood while sex chromosomes are found in bones",
      "Autosomes disappear after puberty while allosomes remain"],
     "A", "OSC", "easy",
     "Autosomes (the 44 non-sex chromosomes) control somatic traits symmetrically across both sexes; allosomes (the 23rd pair: XX in females, XY in males) govern sexual differentiation."),

    # 75: Nucleosome Chromatin Packaging Architecture
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- DNA double helix thread -->
  <path d="M 30 100 Q 60 70 90 100 T 150 100" stroke="#38bdf8" stroke-width="3" fill="none"/>
  <!-- Histone Core Octamer -->
  <circle cx="190" cy="100" r="32" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
  <text x="190" y="96" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Histone</text>
  <text x="190" y="110" fill="#bbf7d0" font-size="8" font-family="sans-serif" text-anchor="middle">Octamer</text>
  <!-- DNA wrapping around core -->
  <path d="M 160 90 A 32 32 0 1 1 220 110" stroke="#38bdf8" stroke-width="4" fill="none"/>
  <!-- H1 Linker Histone -->
  <rect x="145" y="70" width="14" height="25" rx="3" fill="#eab308" stroke="#fef08a" stroke-width="1"/>
  <text x="152" y="87" fill="#000000" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">H1</text>
  <!-- Exiting DNA -->
  <path d="M 220 110 Q 260 140 300 100 T 370 100" stroke="#38bdf8" stroke-width="3" fill="none"/>
  <!-- Label -->
  <text x="280" y="45" fill="#facc15" font-size="11" font-family="sans-serif" font-weight="bold">Nucleosome Unit (147 bp DNA wrap)</text>
  <text x="280" y="65" fill="#94a3b8" font-size="9" font-family="sans-serif">'Beads-on-a-string' Chromatin Model</text>
</svg>
</div>
How does the nucleosome architecture illustrated above enable 2 meters of human cellular DNA to fit securely inside a microscopic 6-micrometer nucleus?""""",
     ["DNA winds tightly 1.65 times around basic histone protein octamers, packaging into compact chromatin coils and higher-order loops",
      "DNA is melted down into liquid droplets",
      "Excess DNA is discarded into the bloodstream",
      "DNA shrinks because the nucleus has zero air pressure"],
     "A", "OSC", "medium",
     "Positively charged histone octamers (H2A, H2B, H3, H4) neutralize the negative phosphodiester backbone of DNA, wrapping 147 base pairs per bead to achieve a 10,000-fold compaction ratio into mitotic chromosomes."),

    # 76: Sex Determination Mechanism in Humans (XX vs XY Cross)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Parents -->
  <rect x="40" y="20" width="130" height="35" rx="5" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
  <text x="105" y="42" fill="#ec4899" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Mother (44 + XX)</text>
  <rect x="230" y="20" width="130" height="35" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="295" y="42" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Father (44 + XY)</text>
  <!-- Gametes -->
  <circle cx="105" cy="85" r="16" fill="#831843"/>
  <text x="105" y="90" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">X (100%)</text>
  <circle cx="260" cy="85" r="16" fill="#1e3a8a"/>
  <text x="260" y="90" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">X (50%)</text>
  <circle cx="330" cy="85" r="16" fill="#1e3a8a"/>
  <text x="330" y="90" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Y (50%)</text>
  <!-- Offspring Result -->
  <rect x="50" y="135" width="140" height="45" rx="5" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
  <text x="120" y="155" fill="#ec4899" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">X + X -> 44 + XX</text>
  <text x="120" y="170" fill="#f472b6" font-size="9" font-family="sans-serif" text-anchor="middle">50% Female Child</text>
  <rect x="210" y="135" width="140" height="45" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="280" y="155" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">X + Y -> 44 + XY</text>
  <text x="280" y="170" fill="#93c5fd" font-size="9" font-family="sans-serif" text-anchor="middle">50% Male Child</text>
</svg>
</div>
Based on the human sex determination schematic above, why is the statistical probability of having a male or female child exactly 50% (1:1)?""",
     ["The father produces equal proportions (50% X and 50% Y) of sperm, while all maternal eggs carry an X chromosome",
      "The mother alternates between producing X and Y eggs every month",
      "Environmental temperature determines whether the zygote becomes male or female",
      "Dietary intake of calcium determines the sex of the baby"],
     "A", "OSC", "easy",
     "Human males are heterogametic, generating equal numbers of X-bearing and Y-bearing spermatozoa during meiosis; random fusion with monogametic (X-only) ova yields a strict 1:1 sex ratio at fertilization."),

    # 77: Secondary Constriction & Satellite Chromosome
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#111827"/>
  <!-- Main chromosome arm -->
  <rect x="90" y="80" width="140" height="28" rx="6" fill="#2563eb" stroke="#60a5fa" stroke-width="2"/>
  <text x="160" y="98" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Long arm (q arm)</text>
  <!-- Primary Constriction -->
  <circle cx="75" cy="94" r="7" fill="#facc15"/>
  <text x="75" y="70" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle">Centromere</text>
  <!-- Secondary Constriction stalk -->
  <line x1="230" y1="94" x2="270" y2="94" stroke="#ec4899" stroke-width="3"/>
  <text x="250" y="130" fill="#ec4899" font-size="9" font-family="sans-serif" text-anchor="middle">Secondary Constriction (NOR)</text>
  <!-- Satellite Knob -->
  <circle cx="285" cy="94" r="14" fill="#a855f7" stroke="#c084fc" stroke-width="2"/>
  <text x="285" y="98" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">SAT</text>
  <text x="285" y="135" fill="#c084fc" font-size="9" font-family="sans-serif" text-anchor="middle">Satellite knob</text>
</svg>
</div>
What vital cellular role is played by the secondary constriction (NOR) situated before the satellite body in human acrocentric chromosomes?""""",
     ["It harbors nucleolar organizer regions containing ribosomal RNA (rRNA) gene clusters that reconstruct the nucleolus",
      "It produces bile salts for liver digestion",
      "It absorbs glucose directly from the bloodstream",
      "It acts as a battery generating cellular electricity"],
     "A", "OSC", "hard",
     "Secondary constrictions on chromosomes 13, 14, 15, 21, and 22 contain tandem rDNA repeats known as Nucleolar Organizer Regions (NORs) that transcribe pre-rRNA and assemble the nucleolus."),

    # 78: Ploidy Comparison: Diploid vs Haploid
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Diploid Somatic Cell -->
  <rect x="30" y="25" width="160" height="140" rx="6" fill="#27272a" stroke="#38bdf8" stroke-width="2"/>
  <text x="110" y="48" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Diploid Cell (2n)</text>
  <text x="110" y="70" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle">46 Chromosomes (23 Pairs)</text>
  <text x="110" y="95" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Two full sets of chromosomes</text>
  <text x="110" y="115" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- All somatic body cells</text>
  <text x="110" y="135" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle">- Maintained by Mitosis</text>
  <!-- Haploid Gamete -->
  <rect x="210" y="25" width="160" height="140" rx="6" fill="#27272a" stroke="#ec4899" stroke-width="2"/>
  <text x="290" y="48" fill="#ec4899" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Haploid Gamete (n)</text>
  <text x="290" y="70" fill="#f472b6" font-size="10" font-family="sans-serif" text-anchor="middle">23 Chromosomes (Unpaired)</text>
  <text x="290" y="95" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- One single set of chromosomes</text>
  <text x="290" y="115" fill="#e2e8f0" font-size="9" font-family="sans-serif" text-anchor="middle">- Sperm and Ovum only</text>
  <text x="290" y="135" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle">- Produced by Meiosis</text>
</svg>
</div>
Why must gametes (sperm and egg) undergo meiotic reduction division to become haploid (n = 23) rather than remaining diploid (2n = 46)?""""",
     ["Fertilization of two haploid gametes restores the constant species-specific diploid number (2n = 46); without meiosis, chromosome counts would double every generation",
      "Haploid cells are lighter so sperm can swim faster",
      "Diploid sperm would be too heavy to fit through blood vessels",
      "Cells cannot undergo DNA replication if they have 46 chromosomes"],
     "A", "OSC", "easy",
     "Syngamy unites two gametic nuclei; halving parental chromosome complements during meiosis ensures the offspring inherits the exact diploid complement (2n = 46) of Homo sapiens."),

    # 79: Comparison of Chromosome Numbers Across Species
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <!-- Bars -->
  <text x="30" y="40" fill="#e2e8f0" font-size="9" font-family="sans-serif">Roundworm (Ascaris)</text>
  <rect x="150" y="30" width="10" height="14" rx="2" fill="#38bdf8"/>
  <text x="170" y="42" fill="#38bdf8" font-size="9" font-family="sans-serif" font-weight="bold">2 (1 pair)</text>

  <text x="30" y="75" fill="#e2e8f0" font-size="9" font-family="sans-serif">Fruit fly (Drosophila)</text>
  <rect x="150" y="65" width="30" height="14" rx="2" fill="#4ade80"/>
  <text x="190" y="77" fill="#4ade80" font-size="9" font-family="sans-serif" font-weight="bold">8 (4 pairs)</text>

  <text x="30" y="110" fill="#e2e8f0" font-size="9" font-family="sans-serif">Human (Homo sapiens)</text>
  <rect x="150" y="100" width="120" height="14" rx="2" fill="#facc15"/>
  <text x="280" y="112" fill="#facc15" font-size="9" font-family="sans-serif" font-weight="bold">46 (23 pairs)</text>

  <text x="30" y="145" fill="#e2e8f0" font-size="9" font-family="sans-serif">Domestic Dog (Canis)</text>
  <rect x="150" y="135" width="180" height="14" rx="2" fill="#ec4899"/>
  <text x="340" y="147" fill="#ec4899" font-size="9" font-family="sans-serif" font-weight="bold">78 (39 pairs)</text>

  <text x="200" y="178" fill="#94a3b8" font-size="8" font-family="sans-serif" text-anchor="middle">Total diploid chromosome count (2n) in somatic cells</text>
</svg>
</div>
What fundamental evolutionary principle is demonstrated by the wide disparity in chromosome counts between roundworms (2n = 2), humans (2n = 46), and dogs (2n = 78)?""",
     ["Chromosome count does NOT correlate with biological organism complexity or evolutionary status, but reflects historical karyotypic rearrangements and fusions",
      "Animals with more chromosomes are always smarter and more complex than humans",
      "Every animal species originally had exactly 100 chromosomes",
      "Chromosome count changes every year depending on animal age"],
     "A", "OSC", "medium",
     "Organismal complexity depends on gene content, regulatory networks, and proteomic diversity rather than crude chromosome count; a dog (2n = 78) is not more biologically advanced than a human (2n = 46)."),

    # 80: Robertsonian Translocation & Evolution of Human Chromosome 2
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Ancestral Ape Chromosomes (2p and 2q) -->
  <rect x="35" y="30" width="15" height="40" rx="4" fill="#38bdf8"/>
  <text x="42" y="85" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle">2p (Ape)</text>
  <text x="65" y="55" fill="#ffffff" font-size="12" font-family="sans-serif">+</text>
  <rect x="85" y="30" width="15" height="50" rx="4" fill="#38bdf8"/>
  <text x="92" y="95" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle">2q (Ape)</text>
  <text x="70" y="125" fill="#94a3b8" font-size="9" font-family="sans-serif" text-anchor="middle">Chimpanzee (2n = 48)</text>
  <!-- Arrow -->
  <line x1="125" y1="55" x2="190" y2="55" stroke="#facc15" stroke-width="3"/>
  <text x="157" y="45" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Telomeric Fusion</text>
  <!-- Human Chromosome 2 -->
  <rect x="220" y="20" width="18" height="95" rx="5" fill="#ec4899" stroke="#f472b6" stroke-width="2"/>
  <circle cx="229" cy="65" r="4" fill="#facc15"/>
  <text x="260" y="55" fill="#ec4899" font-size="10" font-family="sans-serif" font-weight="bold">Human Chromosome 2</text>
  <text x="260" y="70" fill="#fef08a" font-size="9" font-family="sans-serif">Vestigial centromere &</text>
  <text x="260" y="85" fill="#fef08a" font-size="9" font-family="sans-serif">internal telomere sequence!</text>
  <text x="260" y="115" fill="#4ade80" font-size="10" font-family="sans-serif" font-weight="bold">Human (2n = 46)</text>
</svg>
</div>
What molecular genomic evidence conclusively proves that human chromosome 2 formed from the end-to-end fusion of two ancestral ape chromosomes?""",
     ["Human chromosome 2 contains vestigial telomeric hexamer repeats head-to-head in its interior and an inactivated second centromere",
      "It is the only chromosome made of gold",
      "It contains bird feathers inside its DNA",
      "It has no centromere whatsoever"],
     "A", "OSC", "hard",
     "Cytogenetic and sequencing analyses reveal head-to-head telomeric repeat sequences (TTAGGG) inside band 2q13 and a second cryptic centromere homologous to ape chromosome 2q, proving ancestral chromosome fusion."),

    # 81: Heterochromatin vs Euchromatin Functional State
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#111827"/>
  <!-- Euchromatin Box -->
  <rect x="30" y="25" width="160" height="140" rx="6" fill="#1f2937" stroke="#4ade80" stroke-width="2"/>
  <text x="110" y="48" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Euchromatin</text>
  <text x="110" y="72" fill="#bbf7d0" font-size="9" font-family="sans-serif" text-anchor="middle">- Loosely packed chromatin</text>
  <text x="110" y="92" fill="#bbf7d0" font-size="9" font-family="sans-serif" text-anchor="middle">- Stains lightly with basic dyes</text>
  <text x="110" y="112" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">- Transcriptionally ACTIVE</text>
  <text x="110" y="132" fill="#e2e8f0" font-size="8" font-family="sans-serif" text-anchor="middle">RNA Polymerase has access</text>
  <!-- Heterochromatin Box -->
  <rect x="210" y="25" width="160" height="140" rx="6" fill="#1f2937" stroke="#ef4444" stroke-width="2"/>
  <text x="290" y="48" fill="#ef4444" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Heterochromatin</text>
  <text x="290" y="72" fill="#fca5a5" font-size="9" font-family="sans-serif" text-anchor="middle">- Densely, tightly coiled</text>
  <text x="290" y="92" fill="#fca5a5" font-size="9" font-family="sans-serif" text-anchor="middle">- Stains darkly with basic dyes</text>
  <text x="290" y="112" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">- Transcriptionally INACTIVE</text>
  <text x="290" y="132" fill="#e2e8f0" font-size="8" font-family="sans-serif" text-anchor="middle">Centromeres & Telomeres</text>
</svg>
</div>
Why are genes located in heterochromatic chromosomal regions silenced (inactive) compared to those in euchromatic regions?""",
     ["Dense chromatin coiling physically blocks RNA polymerase and transcription factor complexes from binding promoter DNA",
      "Heterochromatin has no DNA at all",
      "Heterochromatin is destroyed by stomach acid",
      "The nuclear envelope cuts heterochromatin into pieces"],
     "A", "OSC", "medium",
     "Heterochromatin adopts a condensed steric conformation through histone deacetylation and H3K9 methylation, physically preventing transcriptional machinery from accessing DNA."),

    # 82: G-Banding Chromosome Identification
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Chromosome outline -->
  <rect x="70" y="25" width="22" height="140" rx="6" fill="#f1f5f9" stroke="#94a3b8" stroke-width="2"/>
  <!-- Dark G-bands -->
  <rect x="70" y="35" width="22" height="12" fill="#0f172a"/>
  <rect x="70" y="55" width="22" height="8" fill="#0f172a"/>
  <circle cx="81" cy="78" r="6" fill="#facc15"/>
  <rect x="70" y="95" width="22" height="15" fill="#0f172a"/>
  <rect x="70" y="125" width="22" height="20" fill="#0f172a"/>
  <!-- Explanatory text -->
  <line x1="95" y1="41" x2="160" y2="41" stroke="#38bdf8" stroke-width="2"/>
  <text x="170" y="45" fill="#38bdf8" font-size="10" font-family="sans-serif" font-weight="bold">Dark G-Bands (Heterochromatin)</text>
  <text x="170" y="60" fill="#cbd5e1" font-size="9" font-family="sans-serif">- AT-rich DNA base pairs</text>
  <text x="170" y="75" fill="#cbd5e1" font-size="9" font-family="sans-serif">- Condensed late-replicating chromatin</text>
  <line x1="95" y1="110" x2="160" y2="110" stroke="#4ade80" stroke-width="2"/>
  <text x="170" y="114" fill="#4ade80" font-size="10" font-family="sans-serif" font-weight="bold">Light Interbands (Euchromatin)</text>
  <text x="170" y="129" fill="#cbd5e1" font-size="9" font-family="sans-serif">- GC-rich DNA base pairs</text>
  <text x="170" y="144" fill="#cbd5e1" font-size="9" font-family="sans-serif">- Gene-rich transcriptionally active regions</text>
</svg>
</div>
In clinical cytogenetics, how does Giemsa G-banding enable geneticists to identify individual chromosome pairs and chromosomal abnormalities?""",
     ["It produces a unique, reproducible barcode of light and dark horizontal bands characteristic for each homologous chromosome pair",
      "It turns damaged chromosomes into bright red fluid",
      "It changes the length of chromosomes permanently",
      "It melts all autosomes so only sex chromosomes remain"],
     "A", "OSC", "easy",
     "G-banding yields an individualized, high-resolution cross-striation pattern for every chromosome pair, allowing precise cytogenetic identification of deletions, duplications, and translocations.")
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

output_path = os.path.join(os.path.dirname(__file__), "ch16_topic1.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
