# scripts/generate_ch16_topic5.py
# MH-9-SCIT-16-16.5: Genetic Disorders: Chromosomal (Down, Turner, Klinefelter) & Monogenic (Sickle Cell Anemia, Albinism, Hemophilia)
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-16-16.5"

exam_data = [
    # 1-10: Chromosomal Disorders Basics & Down Syndrome
    ("What are disorders caused by numerical or structural abnormalities in an individual's chromosomes called?",
     ["Chromosomal disorders (Chromosomal aberrations)", "Infectious diseases", "Deficiency diseases", "Degenerative diseases"],
     "A", "OSC", "easy",
     "Chromosomal disorders arise from errors during gametogenesis (such as meiotic non-disjunction) resulting in gain, loss, or rearrangement of chromosomes."),

    ("Which chromosomal disorder is caused by the presence of an extra copy of autosome 21 (Trisomy 21), resulting in 47 total chromosomes?",
     ["Down's syndrome (46 + 1 = 47, Trisomy 21)", "Turner's syndrome", "Klinefelter's syndrome", "Cri-du-chat syndrome"],
     "A", "OSC", "easy",
     "Down's syndrome is an autosomal aneuploidy characterized by 47 chromosomes (45 autosomes + 2 sex chromosomes) due to meiotic non-disjunction of chromosome 21."),

    ("Who first clinically characterized and published the symptoms of Trisomy 21 in the medical literature in 1866?",
     ["John Langdon Down", "Gregor Mendel", "Reginald Punnett", "Charles Darwin"],
     "A", "OSC", "easy",
     "British physician John Langdon Down first formally classified the constellation of symptoms in 1866; its cytogenetic cause (Trisomy 21) was identified by Jerome Lejeune in 1959."),

    ("Which of the following physical characteristics is a hallmark clinical feature of a child with Down's syndrome?",
     ["Short stature, broad flat face, epicanthic eye folds, protruding furrowed tongue, and a single palmar crease (Simian crease)",
      "Unusually tall height (> 7 feet) with sharp facial features",
      "Presence of green skin and wings",
      "Total absence of bones in the arms"],
     "A", "OSC", "easy",
     "Down's syndrome presents with brachycephaly, upward slanting palpebral fissures, a single transverse palmar crease (Simian line), muscular hypotonia, and cognitive disability."),

    ("What is the chromosome complement and total chromosome number of a female diagnosed with Turner's syndrome?",
     ["44 autosomes + XO (45 chromosomes)", "44 autosomes + XXY (47 chromosomes)", "45 autosomes + XX (47 chromosomes)", "44 autosomes + XXX (47 chromosomes)"],
     "A", "OSC", "easy",
     "Turner's syndrome represents monosomy of the X chromosome in phenotypic females, possessing 45 total chromosomes with karyotype 45, X (or 44+XO)."),

    ("Which clinical features characteristically distinguish a female with Turner's syndrome?",
     ["Short stature, webbed neck, low posterior hairline, rudimentary streak ovaries, and sterility",
      "Excessive tall height with multiple ovaries",
      "Beard growth and deep male voice",
      "Production of 10 children simultaneously"],
     "A", "OSC", "medium",
     "Monosomy X (45, X) results in streak gonads failing to produce estrogen, primary amenorrhea, infantile sexual development, webbed neck (pterygium colli), and cubitus valgus."),

    ("What is the chromosome complement and total chromosome count of an individual with Klinefelter's syndrome?",
     ["44 autosomes + XXY (47 chromosomes)", "44 autosomes + XO (45 chromosomes)", "45 autosomes + XY (47 chromosomes)", "44 autosomes + XYY (47 chromosomes)"],
     "A", "OSC", "easy",
     "Klinefelter's syndrome occurs in genetic males carrying an extra X chromosome, yielding 47 chromosomes with karyotype 47, XXY (44 autosomes + XXY)."),

    ("Which clinical manifestation is typical of an adult male with Klinefelter's syndrome?",
     ["Tall eunuchoid stature, gynecomastia (breast enlargement), sparse body hair, small underdeveloped testes (hypogonadism), and azoospermic sterility",
      "Extremely short dwarf height with excessive body hair",
      "Production of millions of fertile sperm daily",
      "Female pelvic bones with pregnancy ability"],
     "A", "OSC", "medium",
     "The extra X chromosome leads to testicular dysgenesis, hyalinized seminiferous tubules, androgen deficiency, female-like breast development (gynecomastia), and infertility."),

    ("What meiotic accident is responsible for the generation of aneuploid gametes carrying extra or missing chromosomes (e.g. 24 or 22 chromosomes instead of 23)?",
     ["Non-disjunction (failure of homologous chromosomes or sister chromatids to separate cleanly during meiosis)",
      "Normal DNA replication",
      "Cell wall formation",
      "Crossing over in pachytene"],
     "A", "OSC", "medium",
     "Meiotic non-disjunction occurs when spindle checkpoints fail, causing both copies of a chromosome pair to migrate to a single daughter gamete while the other receives none."),

    ("How does maternal age correlate with the statistical risk of giving birth to an infant with Down's syndrome?",
     ["The risk increases exponentially in mothers older than 35 years due to prolonged meiotic arrest of primary oocytes",
      "The risk drops to zero in older mothers",
      "Maternal age has zero statistical effect",
      "Only teenage mothers are affected"],
     "A", "OSC", "medium",
     "Primary oocytes remain arrested in prophase I from fetal development until ovulation; maternal aging compromises the cohesin rings, sharply elevating meiotic non-disjunction."),

    # 11-20: Monogenic Disorders: Sickle Cell Anemia & Albinism
    ("Disorders caused by a mutation or defect in a SINGLE structural gene following Mendelian inheritance patterns are classified as:",
     ["Monogenic disorders (Mendelian disorders)", "Chromosomal disorders", "Polygenic disorders", "Mitochondrial disorders"],
     "A", "OSC", "easy",
     "Monogenic disorders stem from a single pathogenic mutation in a specific gene locus and follow classic autosomal dominant, autosomal recessive, or sex-linked inheritance."),

    ("Sickle Cell Anemia is inherited as which type of genetic disorder?",
     ["Autosomal recessive disorder (located on Chromosome 11)",
      "X-linked dominant disorder",
      "Y-linked holandric disorder",
      "Chromosomal trisomy"],
     "A", "OSC", "easy",
     "Sickle cell anemia is an autosomal recessive condition mapped to the HBB gene on chromosome 11p15.5; disease manifests only in homozygous individuals (HbS HbS)."),

    ("What exact single-point molecular mutation in the beta-globin (HBB) gene causes Sickle Cell Anemia?",
     ["A point transversion from GAG to GTG, replacing Glutamic acid with Valine at the 6th position of the beta-globin polypeptide chain",
      "Deletion of the entire hemoglobin gene",
      "Addition of 500 extra amino acids",
      "Replacement of iron by copper in the heme ring"],
     "A", "OSC", "hard",
     "A single nucleotide substitution (A to T in codon 6: GAG to GTG) substitutes polar negatively charged glutamic acid with nonpolar hydrophobic valine in the beta-globin chain."),

    ("Why do red blood cells of a sickle cell patient distort into an abnormal rigid 'sickle' or crescent shape under low oxygen conditions?",
     ["Deoxygenated mutant hemoglobin HbS molecules polymerize into rigid fibrous insoluble crystalline rods that deform the RBC membrane",
      "RBCs are attacked by white blood cells",
      "Oxygen melts the cell membrane",
      "RBCs dry out into solid salt"],
     "A", "OSC", "medium",
     "Hydrophobic valine at position 6 interacts with hydrophobic patches on adjacent deoxygenated HbS molecules, forming fibrous 14-strand polymers that distort the erythrocyte into a sickle."),

    ("What severe physiological complication occurs when rigid, inflexible sickle-shaped RBCs clump together and occlude microscopic capillary blood vessels?",
     ["Vaso-occlusive crisis (causing severe tissue ischemia, excruciating bone pain, and organ infarction)",
      "Immediate doubling of oxygen delivery",
      "Complete whitening of the skin",
      "Instant bone growth"],
     "A", "OSC", "medium",
     "Sickled erythrocytes plug microvascular beds, producing tissue hypoxia, acute painful bone crises, acute chest syndrome, splenic sequestration, and progressive end-organ damage."),

    ("What is an individual who carries one normal beta-globin allele (HbA) and one sickle allele (HbS) designated as?",
     ["Sickle cell trait carrier (HbA HbS ; heterozygous)", "Full sickle cell disease patient", "Normal homozygous non-carrier", "Aneuploid carrier"],
     "A", "OSC", "easy",
     "Heterozygotes (HbA HbS) carry the sickle cell trait; they remain largely asymptomatic under normal physiological conditions and act as genetic carriers."),

    ("What unexpected evolutionary survival advantage is enjoyed by individuals carrying the heterozygous sickle cell trait (HbA HbS) in tropical regions of Africa and India?",
     ["Natural resistance/protection against severe malaria caused by Plasmodium falciparum (Heterozygote advantage)",
      "Immunity to snake bites",
      "Ability to survive without water for months",
      "Immunity to all viral infections"],
     "A", "OSC", "medium",
     "Parasitized HbA HbS erythrocytes sickle prematurely and are cleared by the spleen; the lower intra-erythrocytic oxygen and potassium levels abort Plasmodium falciparum replication."),

    ("Which monogenic autosomal recessive disorder is characterized by a complete absence of the dark pigment melanin in the skin, hair, and iris of the eyes?",
     ["Albinism", "Sickle cell anemia", "Hemophilia", "Night blindness"],
     "A", "OSC", "easy",
     "Albinism is an autosomal recessive metabolic disorder where defective melanin biosynthesis results in hypopigmentation of ocular, cutaneous, and pilar tissues."),

    ("Which biochemical enzyme deficiency prevents melanocytes from converting the amino acid tyrosine into melanin pigment in individuals with classic albinism?",
     ["Tyrosinase enzyme", "Pepsin", "Amylase", "DNA polymerase"],
     "A", "OSC", "medium",
     "Mutations in the TYR gene inactivate copper-containing tyrosinase, the rate-limiting enzyme that catalyzes the hydroxylation of L-tyrosine to DOPA and dopaquinone in the melanin pathway."),

    ("Why do individuals with albinism suffer from extreme photophobia (light sensitivity) and high vulnerability to skin cancer?",
     ["The lack of melanin in the iris allows excessive blinding light into the retina, and the skin lacks melanin to absorb harmful solar ultraviolet (UV) radiation",
      "Their eyes have no corneas",
      "Their skin produces pure acid when warm",
      "They have no blood vessels in their skin"],
     "A", "OSC", "easy",
     "Melanin acts as a natural photoprotective shield against UV radiation and provides optical opacity in the iris; its absence permits uncontrolled UV DNA damage and retinal dazzle."),

    # 21-30: Sex-Linked Disorders: Hemophilia & Color Blindness
    ("Which X-linked recessive bleeding disorder, famously known as the 'Royal Disease', is characterized by a failure of blood to clot normally?",
     ["Hemophilia", "Thalassemia", "Leukemia", "Anemia"],
     "A", "OSC", "easy",
     "Hemophilia is an X-linked recessive coagulopathy where minor cuts or internal trauma produce persistent, life-threatening hemorrhage due to clotting factor deficiency."),

    ("Classical Hemophilia A, which accounts for over 80% of all hemophilia cases, results from an inherited deficiency in which blood clotting factor?",
     ["Factor VIII (Antihemophilic factor)", "Factor IX (Christmas factor)", "Factor I (Fibrinogen)", "Factor II (Prothrombin)"],
     "A", "OSC", "medium",
     "Hemophilia A is caused by pathogenic mutations in the F8 gene on Xq28, which codes for blood coagulation Factor VIII, an essential cofactor in the intrinsic clotting cascade."),

    ("Why are biological males (XY) significantly more frequently affected by X-linked recessive disorders (such as Hemophilia and Red-Green Color Blindness) than females (XX)?",
     ["Males are hemizygous, possessing only ONE X chromosome; a single recessive mutant allele on the X chromosome expresses directly in males without a second allele to mask it",
      "Males have weaker immune systems than females",
      "The Y chromosome destroys all clotting factors",
      "Females cannot inherit X chromosomes from their fathers"],
     "A", "OSC", "easy",
     "Because males carry only one X chromosome, they lack a homologous counterpart; females require two mutant alleles (homozygous) to express an X-linked recessive disease."),

    ("What is the genetic carrier status of a woman whose father had hemophilia (XhY), assuming her mother was completely normal (XHXH)?",
     ["She is an obligate heterozygous carrier (XHXh ; 100% certainty)",
      "She has full hemophilia disease",
      "She is completely free of the hemophilia allele (XHXH)",
      "She cannot produce children"],
     "A", "OSC", "medium",
     "A father contributes his single X chromosome to all his daughters; thus, all daughters of an affected father invariably inherit the mutant Xh chromosome as carriers (XHXh)."),

    ("If a female carrier of hemophilia (XHXh) marries a normal man (XHY), what is the probability that their SON will suffer from hemophilia?",
     ["50% probability among sons (1/2)", "100% of sons", "25% of sons", "0% of sons"],
     "A", "ONE", "medium",
     "Sons receive their Y chromosome from the father; from the carrier mother, a son has a 50% chance of receiving XH (normal) and a 50% chance of receiving Xh (hemophilic)."),

    ("Which X-linked recessive disorder causes an inability to distinguish between red and green hues due to missing or defective cone photopigments in the retina?",
     ["Red-Green Color Blindness (Daltonism)", "Glaucoma", "Myopia", "Cataract"],
     "A", "OSC", "easy",
     "Red-green color blindness results from mutations in the opsin photoreceptor genes on the X chromosome (OPN1LW / OPN1MW), impairing red-green discrimination."),

    ("Which standardized clinical diagnostic eye chart containing multicolored dots forming hidden numbers is used to test for color blindness?",
     ["Ishihara color chart", "Snellen eye chart", "Guthrie test card", "Amsler grid"],
     "A", "OSC", "medium",
     "The Ishihara pseudoisochromatic plate test displays circles of dots randomized in size and hue to selectively screen for red-green color vision deficiencies."),

    ("Which autosomal recessive monogenic disorder causes progressive thick, sticky mucus accumulation in the lungs and pancreas, leading to severe chronic respiratory infections?",
     ["Cystic Fibrosis (CFTR gene mutation on Chromosome 7)", "Sickle cell anemia", "Albinism", "Down syndrome"],
     "A", "OSC", "medium",
     "Cystic fibrosis is caused by loss-of-function mutations in the CFTR chloride channel, impairing fluid secretion and generating viscous mucus plugs in respiratory and digestive tracts."),

    ("Which inborn error of metabolism is caused by an inherited deficiency of phenylalanine hydroxylase (PAH), leading to toxic accumulation of phenylalanine in the brain?",
     ["Phenylketonuria (PKU)", "Albinism", "Gout", "Diabetes mellitus"],
     "A", "OSC", "medium",
     "PKU is an autosomal recessive deficiency of hepatic phenylalanine hydroxylase; unconverted phenylalanine converts to phenylketones, causing severe cognitive impairment unless dietary phenylalanine is restricted."),

    ("What diagnostic prenatal test involves aspirating amniotic fluid around the 15th-18th week of gestation to analyze fetal cells for chromosomal aberrations (karyotyping)?",
     ["Amniocentesis", "Biopsy", "Endoscopy", "Dialysis"],
     "A", "OSC", "easy",
     "Amniocentesis extracts amniotic fluid containing desquamated fetal amniocytes, allowing cell culture and karyotypic analysis to detect trisomies and monogenic defects prenatally.")
]

# Additional 10 questions to make exam_data 40
exam_data.extend([
    # 31-40: Fill in blanks, Numerical, Multi-choice
    ("Down's syndrome is cytogenetically designated as Trisomy ________.",
     ["21", "18", "13", "23"],
     "A", "ONE", "easy",
     "Down's syndrome is caused by an extra copy of chromosome 21 (Trisomy 21)."),

    ("The total number of chromosomes in the somatic cells of an individual with Turner's syndrome is ________ chromosomes.",
     ["45", "46", "47", "44"],
     "A", "ONE", "easy",
     "Females with Turner's syndrome possess 45 chromosomes (44 autosomes + 1 single X chromosome, 45, XO)."),

    ("The total number of chromosomes in the somatic cells of an individual with Klinefelter's syndrome is ________ chromosomes.",
     ["47", "46", "45", "48"],
     "A", "ONE", "easy",
     "Males with Klinefelter's syndrome possess 47 chromosomes (44 autosomes + XXY)."),

    ("In Sickle Cell Anemia, normal adult hemoglobin HbA is replaced by the mutant hemoglobin ________.",
     ["HbS", "HbF", "HbC", "HbM"],
     "A", "OFB", "easy",
     "Sickle hemoglobin is designated HbS; homozygotes (HbS HbS) suffer from sickle cell disease."),

    ("State whether True or False: Sickle cell anemia is transmitted to offspring only when BOTH parents are at least carriers (heterozygous) of the sickle allele.",
     ["True", "False"],
     "A", "OTF", "easy",
     "As an autosomal recessive trait, disease manifestation (HbS HbS) requires the inheritance of one mutant allele from each parent."),

    ("Which of the following conditions are examples of MONOGENIC (single-gene) disorders? (Select all that apply)",
     ["Sickle cell anemia, Albinism, Hemophilia, and Phenylketonuria (PKU)",
      "Only Down's syndrome and Turner's syndrome",
      "Only Klinefelter's syndrome",
      "Tuberculosis and Malaria"],
     "A", "OMC", "easy",
     "Sickle cell anemia, albinism, hemophilia, and PKU are classic monogenic disorders caused by single defective gene loci obeying Mendelian inheritance."),

    ("Assertion (A): Human males cannot be silent heterozygous carriers of X-linked recessive hemophilia.\nReason (R): Males possess only a single X chromosome (hemizygous) and will manifest the disease if that X carries the mutant allele.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is not the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "easy",
     "Because males lack a second X chromosome to mask a recessive allele, any hemophilic allele (Xh) results directly in the hemophilia phenotype."),

    ("Which diagnostic test is universally performed to screen blood samples for sickle hemoglobin using sodium metabisulfite to induce sickling?",
     ["Solubility test (Sickling test)", "Widal test", "Mantoux test", "ELISA test"],
     "A", "OSC", "medium",
     "Sodium metabisulfite reduces oxygen tension in blood droplets, inducing rapid sickling of HbS-containing erythrocytes visible under a light microscope."),

    ("What is the probability that two parents who are BOTH heterozygous carriers of sickle cell trait (HbA HbS) will have a child with full SICKLE CELL DISEASE (HbS HbS)?",
     ["25% (1 / 4)", "50% (1 / 2)", "75% (3 / 4)", "0%"],
     "A", "ONE", "easy",
     "Crossing HbA HbS x HbA HbS follows classic Mendelian monohybrid genetics: 25% HbA HbA, 50% HbA HbS (carrier), and 25% HbS HbS (affected)."),

    ("Disorders such as hypertension, diabetes mellitus, asthma, and cleft palate are not caused by a single gene, but result from the combined effects of multiple genes and environmental factors, known as:",
     ["Polygenic (Multifactorial) disorders", "Monogenic disorders", "Chromosomal disorders", "Mendelian disorders"],
     "A", "OSC", "medium",
     "Polygenic or multifactorial conditions involve additive genetic susceptibility across numerous polygenes interacting with lifestyle and environmental triggers.")
])

practice_data = [
    # 41-50: Clinical Genetics & Diagnostic Problems
    ("Why does an individual with sickle cell trait (HbA HbS) experience sickling symptoms only during extreme unpressurized high-altitude flight or severe physical exertion?",
     ["Under normal atmospheric conditions, 50% normal HbA prevents sickling; only severe hypoxia triggers HbS polymerization",
      "High altitude causes bacterial infection in the blood",
      "The airplane dissolves hemoglobin into water",
      "The sickle gene only activates at night"],
     "A", "OSC", "medium",
     "Heterozygotes possess ~55-60% HbA and ~40-45% HbS; normal HbA inhibits polymer nucleation until extreme arterial oxygen desaturation (<60% SaO2) is encountered."),

    ("What is the biological mechanism of 'Lyonization' (X-chromosome inactivation) that occurs in female mammalian somatic cells?",
     ["One of the two X chromosomes in every female somatic cell is randomly and permanently silenced into a condensed, inactive Barr body",
      "Both X chromosomes are destroyed completely",
      "The X chromosome transforms into a Y chromosome",
      "Females produce only male cells after puberty"],
     "A", "OSC", "hard",
     "Mary Lyon demonstrated dosage compensation in female mammals: XIST non-coding RNA randomly heterochromatinizes one X chromosome into a dense peripheral Barr body."),

    ("How many Barr bodies are observed in a buccal mucosal smear from a male patient diagnosed with Klinefelter's syndrome (47, XXY)?",
     ["1 Barr body (Total X chromosomes - 1 = 2 - 1 = 1)", "0 Barr bodies", "2 Barr bodies", "3 Barr bodies"],
     "A", "ONE", "hard",
     "The rule of Barr body number is $N_X - 1$. A Klinefelter male has two X chromosomes ($2 - 1 = 1$); thus, exactly one inactive condensed Barr body is observed."),

    ("How many Barr bodies are present in the somatic cells of a female with Turner's syndrome (45, XO)?",
     ["0 Barr bodies (1 - 1 = 0)", "1 Barr body", "2 Barr bodies", "45 Barr bodies"],
     "A", "ONE", "hard",
     "A female with Turner's syndrome possesses only one X chromosome ($N_X - 1 = 1 - 1 = 0$); therefore, zero Barr bodies are detected in her nuclei."),

    ("What is the mode of inheritance for Duchenne Muscular Dystrophy (DMD), characterized by rapid skeletal muscle degeneration in young boys?",
     ["X-linked recessive disorder (mutation in the dystrophin gene)",
      "Autosomal dominant disorder",
      "Y-linked disorder",
      "Mitochondrial disorder"],
     "A", "OSC", "medium",
     "DMD is an X-linked recessive myopathy caused by out-of-frame mutations in the massive DMD gene on Xp21, leading to a complete absence of structural dystrophin."),

    ("If a color-blind man (XcY) marries a normal homozygous woman (XCXC), what is the expected color vision status of their children?",
     ["All daughters are normal vision carriers (XCXc) and all sons have normal color vision (XCY)",
      "All sons are color blind",
      "All daughters are color blind",
      "50% of sons and 50% of daughters are color blind"],
     "A", "OSC", "medium",
     "The father donates his mutant Xc exclusively to daughters (making them all carriers) and his Y chromosome to all sons (who receive a normal XC from the mother)."),

    ("If a color-blind woman (XcXc) marries a man with normal vision (XCY), what percentage of their SONS will be color blind?",
     ["100% of sons will be color blind", "50% of sons", "0% of sons", "25% of sons"],
     "A", "ONE", "easy",
     "Every son receives his only X chromosome from the mother; since the mother has genotype XcXc, 100% of sons inherit the mutant allele and are color blind."),

    ("What is the mode of inheritance of Huntington's disease, a progressive neurodegenerative brain disorder caused by expanded CAG trinucleotide repeats?",
     ["Autosomal dominant disorder (located on Chromosome 4)",
      "Autosomal recessive disorder",
      "X-linked recessive disorder",
      "Mitochondrial disorder"],
     "A", "OSC", "hard",
     "Huntington's disease is an autosomal dominant condition with high penetrance; individuals carrying just a single mutant HTT allele develop chorea and dementia in midlife."),

    ("State whether True or False: Marrying a close biological relative (consanguineous marriage) significantly increases the risk of producing children affected by autosomal recessive disorders.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Consanguinity increases the coefficient of inbreeding, dramatically elevating the statistical probability that two carriers will inherit the same rare recessive pathogenic allele from a common ancestor."),

    ("What is the primary role of genetic counseling for prospective parents with a family history of genetic disease?",
     ["To evaluate family pedigrees, estimate mathematical risks of recurrence, and guide informed reproductive and diagnostic decisions",
      "To legally prohibit parents from getting married",
      "To perform gene editing with household chemicals",
      "To guarantee the birth of a boy"],
     "A", "OSC", "easy",
     "Genetic counseling provides medical, psychological, and statistical guidance regarding inherited risks, carrier testing, and prenatal diagnostic options.")
]

# Additional 20 practice questions to reach exactly 30 questions
practice_data.extend([
    # 51-60: Further Genetic Disorder Mechanics
    ("Which autosomal recessive hemoglobin disorder is prevalent in Mediterranean regions and caused by reduced synthesis of either alpha or beta globin chains?",
     ["Thalassemia", "Sickle cell anemia", "Hemophilia", "Pernicious anemia"],
     "A", "OSC", "medium",
     "Thalassemias are quantitative hemoglobinopathies where reduced or absent globin chain synthesis causes microcytic hypochromic anemia and hepatosplenomegaly."),

    ("What is the primary difference between a QUALITATIVE hemoglobinopathy (like Sickle Cell Anemia) and a QUANTITATIVE hemoglobinopathy (like Thalassemia)?",
     ["Sickle cell anemia produces an abnormal structural hemoglobin molecule (HbS), whereas thalassemia produces reduced amounts of normal hemoglobin chains",
      "Sickle cell has no hemoglobin at all",
      "Thalassemia turns blood into water",
      "Sickle cell only affects bones while thalassemia affects teeth"],
     "A", "OSC", "hard",
     "Sickle cell is a structural defect (qualitative mutation in amino acid sequence), whereas thalassemia is a regulatory defect in transcription/translation rate (quantitative deficit)."),

    ("Which chromosomal disorder is characterized by a high-pitched, cat-like infant cry due to a partial deletion of the short arm of chromosome 5 (5p-)?",
     ["Cri-du-chat syndrome (Cat cry syndrome)", "Down syndrome", "Turner syndrome", "Edwards syndrome"],
     "A", "OSC", "medium",
     "Cri-du-chat syndrome results from a terminal or interstitial deletion on chromosome 5p, producing abnormal laryngeal hypoplasia and severe cognitive impairment."),

    ("What is Edwards syndrome, a severe chromosomal condition where infants rarely survive past the first year?",
     ["Trisomy 18 (an extra chromosome 18)", "Trisomy 21", "Trisomy 13", "Monosomy X"],
     "A", "OSC", "hard",
     "Edwards syndrome is Trisomy 18, characterized by microcephaly, clenched fists with overlapping fingers, rocker-bottom feet, and complex congenital heart defects."),

    ("What is Patau syndrome?",
     ["Trisomy 13 (an extra chromosome 13)", "Trisomy 21", "Trisomy 18", "Monosomy 21"],
     "A", "OSC", "hard",
     "Patau syndrome is Trisomy 13, marked by holoprosencephaly, cleft lip and palate, microphthalmia, and polydactyly."),

    ("State whether True or False: Females with two X chromosomes who are heterozygous for hemophilia (XHXh) typically show normal blood clotting because of adequate Factor VIII production by the normal allele.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Because Factor VIII is synthesized in hepatocytes, random X-inactivation in 50% of liver cells provides sufficient circulating Factor VIII (>40-50%) to achieve normal hemostasis."),

    ("If a man with hemophilia (XhY) marries a normal homozygous woman (XHXH), what is the probability that their SON will inherit hemophilia?",
     ["0% (No sons will have hemophilia)", "100%", "50%", "25%"],
     "A", "ONE", "easy",
     "A son receives his Y chromosome from his father and his normal XH from his mother; therefore, 0% of sons will inherit hemophilia from an affected father."),

    ("What is a pedigree chart in human medical genetics?",
     ["A standardized diagrammatic family tree using symbols to track the transmission of a phenotypic trait across multiple ancestral generations",
      "A medical bill from a hospital",
      "A photograph of chromosomes under a microscope",
      "A chart showing daily body temperature"],
     "A", "OSC", "easy",
     "Pedigree charts depict biological relationships using standard symbols (squares for males, circles for females, darkened shapes for affected individuals) to deduce inheritance modes."),

    ("What do open circles and filled squares represent in a standard clinical pedigree chart?",
     ["Open circle: Unaffected female ; Filled square: Affected male",
      "Open circle: Affected male ; Filled square: Normal female",
      "Open circle: Hospital bed ; Filled square: Doctor",
      "Both represent identical twins"],
     "A", "OSC", "easy",
     "In international pedigree nomenclature, circles represent females, squares represent males, and solid filled/shaded symbols signify individuals manifesting the disease phenotype."),

    ("A horizontal line connecting a square and a circle in a pedigree chart indicates:",
     ["A marriage or mating partnership", "A brother-sister sibling relationship", "Parent-child relationship", "Divorce"],
     "A", "OSC", "easy",
     "A single horizontal line bridging a male square and female circle represents a mating or conjugal union; a double horizontal line signifies a consanguineous marriage.")
])

# 10 more questions to complete practice_data to 30
practice_data.extend([
    # 61-70: High-Yield Practice Questions
    ("Which newborn screening blood spot test is universally performed by pricking an infant's heel to detect metabolic disorders like Phenylketonuria (PKU)?",
     ["Guthrie bacterial inhibition assay", "Ishihara test", "Mantoux test", "Widal test"],
     "A", "OSC", "medium",
     "Robert Guthrie designed the dried blood spot assay where infant blood inhibits Bacillus subtilis growth if toxic phenylalanine concentrations are present."),

    ("Why are Y-linked traits (holandric traits) passed down exclusively from fathers to all sons and NEVER to daughters?",
     ["Only biological males possess the Y chromosome and transmit it exclusively to their male offspring",
      "The Y chromosome is destroyed in daughters",
      "Females possess antibodies that destroy Y chromosomes",
      "Y-linked traits can only survive in cold weather"],
     "A", "OSC", "easy",
     "Because the Y chromosome is inherited strictly down the patrilineal line (father to son), holandric genes (such as hypertrichosis of the ear pinna) show 100% male-to-male transmission."),

    ("What is the probability of a child having Sickle Cell Anemia (HbS HbS) if ONE parent has sickle cell trait (HbA HbS) and the OTHER parent is completely normal (HbA HbA)?",
     ["0% (None will have the disease ; 50% will be carriers)", "25%", "50%", "100%"],
     "A", "ONE", "easy",
     "The normal parent donates exclusively normal HbA alleles. Cross HbA HbS x HbA HbA yields 50% HbA HbA and 50% HbA HbS; exactly 0% develop sickle cell disease."),

    ("What genetic term describes a sudden, heritable change in the nucleotide sequence of an organism's genomic DNA?",
     ["Mutation", "Translation", "Transcription", "Mitosis"],
     "A", "OSC", "easy",
     "Mutations are permanent alterations in genomic nucleotide sequences caused by replication errors, UV light, ionizing radiation, or chemical mutagens."),

    ("Which type of mutation occurs when one or two nucleotide base pairs are inserted or deleted from a protein-coding sequence, shifting the downstream triplet reading frame?",
     ["Frameshift mutation", "Silent mutation", "Missense mutation", "Nonsense mutation"],
     "A", "OSC", "medium",
     "Insertions or deletions that are not multiples of three alter the triplet reading frame of mRNA, changing every downstream amino acid and typically introducing a premature STOP codon."),

    ("State whether True or False: Sickle cell anemia causes jaundice because massive destruction of fragile sickled red blood cells releases excess bilirubin into the bloodstream.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Chronic extravascular and intravascular hemolysis breaks down heme into unconjugated bilirubin faster than the liver can conjugate it, producing hemolytic jaundice."),

    ("Which dietary precaution is vital for an infant diagnosed with Phenylketonuria (PKU) to prevent severe irreversible brain damage?",
     ["Strict lifelong adherence to a low-phenylalanine medical diet (avoiding aspartame, dairy, meat, and eggs)",
      "Eating large quantities of red meat daily",
      "Avoiding table salt completely",
      "Drinking only cow's milk"],
     "A", "OSC", "medium",
     "Because PKU patients cannot metabolize phenylalanine into tyrosine, synthetic medical formulas low in phenylalanine prevent neurotoxic buildup during brain maturation."),

    ("Why does taking aspirin (acetylsalicylic acid) pose an extreme life-threatening risk for a patient with hemophilia?",
     ["Aspirin irreversibly inhibits platelet cyclooxygenase (COX-1), blocking platelet aggregation and accelerating fatal hemorrhage",
      "Aspirin causes immediate cardiac arrest in boys",
      "Aspirin destroys red blood cells into dust",
      "Aspirin freezes blood into ice"],
     "A", "OSC", "hard",
     "Aspirin impairs primary platelet plug formation; combining impaired platelet function with a severe coagulation factor deficit precipitates uncontrollable hemorrhage."),

    ("If both parents are heterozygous carriers of the autosomal recessive gene for albinism (Aa x Aa), what is the probability that their first child will be an albino (aa)?",
     ["25% (1 / 4)", "50% (1 / 2)", "75% (3 / 4)", "100%"],
     "A", "ONE", "easy",
     "In an autosomal recessive monohybrid cross between two carriers (Aa x Aa), the chance of producing an affected homozygous recessive offspring (aa) is exactly 1 in 4 (25%)."),

    ("State whether True or False: A person with Klinefelter's syndrome is biologically male, whereas a person with Turner's syndrome is biologically female.",
     ["True", "False"],
     "A", "OTF", "easy",
     "The presence of the Y chromosome (carrying the SRY gene) determines male phenotype in Klinefelter's (47, XXY); its absence results in female phenotype in Turner's (45, XO).")
])

mock_data = [
    # 71: Trisomy 21 (Down Syndrome) Karyotype Breakdown
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="210" viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="210" rx="8" fill="#090d16"/>
  <!-- Normal pairs representation -->
  <text x="50" y="35" fill="#38bdf8" font-size="10" font-family="sans-serif">Pairs 1-20:</text>
  <rect x="120" y="25" width="6" height="15" rx="2" fill="#38bdf8"/>
  <rect x="130" y="25" width="6" height="15" rx="2" fill="#38bdf8"/>
  <text x="150" y="37" fill="#cbd5e1" font-size="9" font-family="sans-serif">Normal Disomic Pairs (2n)</text>
  <!-- Pair 21 TRISOMY highlighted -->
  <rect x="40" y="55" width="320" height="60" rx="6" fill="#831843" stroke="#f43f5e" stroke-width="2"/>
  <text x="60" y="80" fill="#facc15" font-size="12" font-family="sans-serif" font-weight="bold">Chromosome 21:</text>
  <!-- Three chromosomes! -->
  <rect x="180" y="67" width="10" height="35" rx="3" fill="#facc15"/>
  <rect x="195" y="67" width="10" height="35" rx="3" fill="#facc15"/>
  <rect x="210" y="67" width="10" height="35" rx="3" fill="#facc15"/>
  <text x="235" y="90" fill="#ffffff" font-size="11" font-family="sans-serif" font-weight="bold">TRISOMY 21 (3 Copies!)</text>
  <!-- Sex chromosomes -->
  <text x="50" y="140" fill="#38bdf8" font-size="10" font-family="sans-serif">Pair 23 (Sex):</text>
  <text x="130" y="140" fill="#cbd5e1" font-size="9" font-family="sans-serif">XX or XY (Normal)</text>
  <!-- Summary Box -->
  <text x="200" y="175" fill="#facc15" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">Total: 47 Chromosomes (45 Autosomes + 2 Sex Chromosomes)</text>
  <text x="200" y="195" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">Clinical Condition: Down's Syndrome (John Langdon Down, 1866)</text>
</svg>
</div>
In the karyotypic diagnostic scheme shown above, what specific chromosomal abnormality is responsible for Down's syndrome?""",
     ["Trisomy of autosome 21 (presence of three copies of chromosome 21 yielding 47 total chromosomes)",
      "Total absence of the X chromosome",
      "An extra copy of the Y chromosome",
      "Loss of both copies of chromosome 1"],
     "A", "OSC", "easy",
     "Down's syndrome results from non-disjunction during meiosis leading to three complete copies of chromosome 21 (Trisomy 21), giving a total chromosome count of 47 (47, XX,+21 or 47, XY,+21)."),

    # 72: Normal RBC vs Sickle RBC Molecular Pathology
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Normal RBC (HbA) -->
  <rect x="25" y="25" width="165" height="150" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <text x="107" y="48" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Normal RBC (HbA HbA)</text>
  <circle cx="107" cy="85" r="24" fill="#dc2626"/>
  <circle cx="107" cy="85" r="12" fill="#ef4444"/>
  <text x="107" y="125" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">Biconcave, Flexible Disc</text>
  <text x="107" y="145" fill="#bbf7d0" font-size="8" font-family="sans-serif" text-anchor="middle">Flows smoothly through capillaries</text>
  <text x="107" y="160" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">HbA: 6th Amino Acid = Glutamic Acid</text>
  <!-- Sickle RBC (HbS) -->
  <rect x="210" y="25" width="165" height="150" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
  <text x="292" y="48" fill="#ef4444" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Sickle RBC (HbS HbS)</text>
  <path d="M 275 65 Q 315 85 295 110 Q 285 85 275 65 Z" fill="#991b1b" stroke="#f87171" stroke-width="2"/>
  <text x="292" y="125" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">Rigid Crescent / Sickle Shape</text>
  <text x="292" y="145" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">Clumps & blocks micro-vessels</text>
  <text x="292" y="160" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">HbS: 6th Amino Acid = Valine!</text>
</svg>
</div>
What exact molecular substitution in the beta-globin chain causes hemoglobin molecules to polymerize into rigid sickles under deoxygenated conditions?""",
     ["Hydrophobic Valine replaces negatively charged Glutamic acid at position 6 of the beta-globin polypeptide chain",
      "Alanine replaces Glycine at position 1",
      "Iron is replaced by Magnesium in the heme ring",
      "All amino acids are converted into lipids"],
     "A", "OSC", "hard",
     "The point mutation replaces polar glutamic acid with nonpolar valine at codon 6; this creates a hydrophobic protrusion that binds complementary hydrophobic receptor sites on adjacent deoxy-HbS molecules, driving helical polymer fiber formation."),

    # 73: Capillary Occlusion by Sickled Erythrocytes (Vaso-Occlusion)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#0f172a"/>
  <!-- Capillary walls -->
  <line x1="30" y1="60" x2="370" y2="60" stroke="#f43f5e" stroke-width="4"/>
  <line x1="30" y1="130" x2="370" y2="130" stroke="#f43f5e" stroke-width="4"/>
  <text x="50" y="50" fill="#f43f5e" font-size="9" font-family="sans-serif">Capillary Endothelial Wall</text>
  <!-- Blood Flow Direction -->
  <text x="70" y="95" fill="#38bdf8" font-size="9" font-family="sans-serif">Blood Flow -> </text>
  <!-- Sickle Cell Blockage Clump -->
  <path d="M 200 70 Q 225 90 210 115 Z" fill="#b91c1c" stroke="#f87171" stroke-width="2"/>
  <path d="M 215 80 Q 240 100 225 125 Z" fill="#b91c1c" stroke="#f87171" stroke-width="2"/>
  <path d="M 230 70 Q 255 90 240 115 Z" fill="#b91c1c" stroke="#f87171" stroke-width="2"/>
  <!-- Stop Symbol -->
  <circle cx="280" cy="95" r="16" fill="#ef4444"/>
  <line x1="270" y1="85" x2="290" y2="105" stroke="#ffffff" stroke-width="3"/>
  <!-- Annotations -->
  <text x="240" y="155" fill="#facc15" font-size="10" font-family="sans-serif" font-weight="bold">Vaso-Occlusive Crisis (Traffic Jam)</text>
  <text x="240" y="172" fill="#cbd5e1" font-size="9" font-family="sans-serif">Causes intense pain, tissue ischemia & splenic infarction</text>
</svg>
</div>
Why does microvascular vaso-occlusion occur during a sickle cell crisis as shown in the diagram above?""",
     ["Rigid, non-deformable sickle erythrocytes become physically entrapped and logjam within narrow capillaries, completely obstructing downstream tissue blood flow",
      "Blood turns into solid bone inside the arteries",
      "Capillaries shrink to zero diameter due to cold air",
      "Platelets evaporate from the blood"],
     "A", "OSC", "medium",
     "Normal RBCs are pliable and squeeze single-file through narrow 5-7 micrometer capillaries; rigid sickle cells cannot flex, adhesively lodging against endothelial walls and precipitating microvascular occlusion."),

    # 74: Turner's (45, XO) vs Klinefelter's (47, XXY) Comparison
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#111827"/>
  <!-- Turner Syndrome -->
  <rect x="25" y="25" width="165" height="150" rx="6" fill="#1f2937" stroke="#ec4899" stroke-width="2"/>
  <text x="107" y="48" fill="#ec4899" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Turner's Syndrome</text>
  <text x="107" y="70" fill="#facc15" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">44 Autosomes + XO</text>
  <text x="107" y="90" fill="#f472b6" font-size="10" font-family="sans-serif" text-anchor="middle">Total: 45 Chromosomes</text>
  <text x="107" y="115" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- Phenotypically Female</text>
  <text x="107" y="130" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- Short stature, webbed neck</text>
  <text x="107" y="145" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- Rudimentary streak ovaries</text>
  <text x="107" y="160" fill="#f87171" font-size="8" font-family="sans-serif" text-anchor="middle">0 Barr Bodies (Monosomy X)</text>
  <!-- Klinefelter Syndrome -->
  <rect x="210" y="25" width="165" height="150" rx="6" fill="#1f2937" stroke="#38bdf8" stroke-width="2"/>
  <text x="292" y="48" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Klinefelter's Syndrome</text>
  <text x="292" y="70" fill="#facc15" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">44 Autosomes + XXY</text>
  <text x="292" y="90" fill="#93c5fd" font-size="10" font-family="sans-serif" text-anchor="middle">Total: 47 Chromosomes</text>
  <text x="292" y="115" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- Phenotypically Male</text>
  <text x="292" y="130" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- Tall eunuchoid build</text>
  <text x="292" y="145" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- Gynecomastia & small testes</text>
  <text x="292" y="160" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">1 Barr Body (XXY)</text>
</svg>
</div>
What critical cytogenetic difference distinguishes sex chromosome aneuploidy in Turner's syndrome from Klinefelter's syndrome?""",
     ["Turner's is monosomy of the sex chromosomes (45, XO in females), while Klinefelter's is sex chromosomal trisomy (47, XXY in males)",
      "Turner's syndrome occurs only in chimpanzees",
      "Klinefelter's syndrome has 90 chromosomes",
      "Turner's syndrome has two Y chromosomes"],
     "A", "OSC", "easy",
     "Turner's syndrome involves the loss of a second sex chromosome (45, XO monosomy), whereas Klinefelter's syndrome involves an additional X chromosome in males (47, XXY trisomy)."),

    # 75: X-Linked Recessive Inheritance Pedigree (Hemophilia Pattern)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Parents -->
  <rect x="70" y="30" width="26" height="26" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="83" y="20" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle">Father (XHY)</text>
  <line x1="96" y1="43" x2="140" y2="43" stroke="#cbd5e1" stroke-width="2"/>
  <circle cx="155" cy="43" r="14" fill="#831843" stroke="#f43f5e" stroke-width="2"/>
  <text x="155" y="20" fill="#f472b6" font-size="8" font-family="sans-serif" text-anchor="middle">Carrier Mother (XHXh)</text>
  <!-- Descent Line -->
  <line x1="118" y1="43" x2="118" y2="80" stroke="#cbd5e1" stroke-width="2"/>
  <line x1="45" y1="80" x2="350" y2="80" stroke="#cbd5e1" stroke-width="2"/>
  <!-- Children -->
  <!-- Son 1: Normal -->
  <rect x="35" y="100" width="22" height="22" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="46" y="138" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">XHY (Normal)</text>
  <!-- Daughter 1: Normal -->
  <circle cx="130" cy="111" r="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="130" y="138" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">XHXH (Normal)</text>
  <!-- Daughter 2: Carrier -->
  <circle cx="220" cy="111" r="12" fill="#831843" stroke="#f43f5e" stroke-width="2"/>
  <text x="220" y="138" fill="#f472b6" font-size="8" font-family="sans-serif" text-anchor="middle">XHXh (Carrier)</text>
  <!-- Son 2: Affected! -->
  <rect x="300" y="100" width="22" height="22" fill="#b91c1c" stroke="#f87171" stroke-width="2"/>
  <text x="311" y="138" fill="#ef4444" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">XhY (Hemophilic!)</text>
  <text x="200" y="180" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Criss-Cross Inheritance: Mother passes trait to 50% of sons</text>
</svg>
</div>
In the X-linked recessive pedigree illustrated above, why does a carrier mother transmit the active clinical disease specifically to her sons rather than her daughters?""",
     ["Sons receive a single X chromosome from the mother with no second X to compensate, whereas daughters inherit a normal dominant XH from the father",
      "Sons have no blood clotting enzymes at birth",
      "The father's Y chromosome destroys clotting factor VIII",
      "Daughters cannot produce liver cells"],
     "A", "OSC", "medium",
     "Females inherit two X chromosomes; a mutant Xh is masked by the paternal XH. Males inherit only the maternal X; if it carries Xh, the hemizygous male inevitably suffers from hemophilia."),

    # 76: Biochemical Pathway Block in Albinism
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Substrate -->
  <rect x="30" y="55" width="85" height="40" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="72" y="75" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">L-Tyrosine</text>
  <text x="72" y="88" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">(Dietary Amino Acid)</text>
  <!-- Blocked Arrow -->
  <line x1="115" y1="75" x2="195" y2="75" stroke="#ef4444" stroke-width="3"/>
  <circle cx="155" cy="75" r="14" fill="#ef4444"/>
  <line x1="145" y1="65" x2="165" y2="85" stroke="#ffffff" stroke-width="3"/>
  <text x="155" y="45" fill="#f87171" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">NO Tyrosinase!</text>
  <!-- Product -->
  <rect x="195" y="55" width="95" height="40" rx="5" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <text x="242" y="75" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">DOPA / Quinone</text>
  <line x1="290" y1="75" x2="330" y2="75" stroke="#facc15" stroke-width="2"/>
  <!-- End Product -->
  <rect x="330" y="55" width="55" height="40" rx="5" fill="#334155"/>
  <text x="357" y="75" fill="#94a3b8" font-size="9" font-family="sans-serif" text-anchor="middle">Melanin</text>
  <text x="357" y="88" fill="#ef4444" font-size="8" font-family="sans-serif" text-anchor="middle">(ABSENT)</text>
  <!-- Result Box -->
  <rect x="50" y="125" width="300" height="45" rx="6" fill="#831843" stroke="#f43f5e" stroke-width="2"/>
  <text x="200" y="145" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Total Melanin Pigment Deficiency: ALBINISM</text>
  <text x="200" y="160" fill="#fbcfe8" font-size="9" font-family="sans-serif" text-anchor="middle">White skin, white hair, pink eyes, and extreme UV photophobia</text>
</svg>
</div>
According to the metabolic pathway block illustrated above, which defective gene product directly causes the complete failure of melanin synthesis in albinism?""",
     ["Tyrosinase enzyme (inactivating conversion of tyrosine to DOPA and melanin polymer)",
      "Insulin hormone",
      "Hemoglobin protein",
      "Amylase enzyme"],
     "A", "OSC", "medium",
     "Albinism results from loss-of-function mutations in the tyrosinase gene (TYR); without active copper-dependent tyrosinase, melanocytes cannot convert tyrosine into dark melanin pigments."),

    # 77: Heterozygote Advantage: Malaria Resistance Curve
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Box 1: Normal HbA HbA -->
  <rect x="25" y="30" width="105" height="130" rx="5" fill="#27272a" stroke="#ef4444" stroke-width="2"/>
  <text x="77" y="52" fill="#ef4444" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">HbA HbA (Normal)</text>
  <text x="77" y="80" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">No sickle cell disease</text>
  <text x="77" y="110" fill="#f87171" font-size="9" font-family="sans-serif" text-anchor="middle">High Vulnerability</text>
  <text x="77" y="125" fill="#f87171" font-size="8" font-family="sans-serif" text-anchor="middle">to Lethal Malaria!</text>
  <!-- Box 2: Heterozygote HbA HbS (WINNER) -->
  <rect x="145" y="20" width="110" height="150" rx="6" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="200" y="45" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">HbA HbS (Carrier)</text>
  <text x="200" y="70" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">BALANCED</text>
  <text x="200" y="85" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">POLYMORPHISM</text>
  <text x="200" y="110" fill="#bbf7d0" font-size="9" font-family="sans-serif" text-anchor="middle">Protected against</text>
  <text x="200" y="125" fill="#bbf7d0" font-size="9" font-family="sans-serif" text-anchor="middle">Falciparum Malaria!</text>
  <text x="200" y="150" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Highest Survival Rate</text>
  <!-- Box 3: Sickle Disease HbS HbS -->
  <rect x="270" y="30" width="105" height="130" rx="5" fill="#27272a" stroke="#ef4444" stroke-width="2"/>
  <text x="322" y="52" fill="#ef4444" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">HbS HbS (Sickle)</text>
  <text x="322" y="80" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Protected from malaria</text>
  <text x="322" y="110" fill="#f87171" font-size="9" font-family="sans-serif" text-anchor="middle">High Mortality</text>
  <text x="322" y="125" fill="#f87171" font-size="8" font-family="sans-serif" text-anchor="middle">from Sickle Crises</text>
</svg>
</div>
Why has the deleterious sickle cell gene (HbS) persisted at high frequencies in equatorial populations despite its lethal homozygous effects?""",
     ["Heterozygote advantage (balanced polymorphism): HbA HbS carriers gain substantial natural survival protection against severe falciparum malaria",
      "Because the sickle cell gene cures cancer",
      "Because homozygous sickle individuals have more children than anyone else",
      "Because malaria only infects mosquitoes and not humans"],
     "A", "OSC", "medium",
     "In endemic malaria zones, natural selection favors heterozygotes (HbA HbS) who survive lethal malaria crises without suffering the severe mortality of homozygous HbS HbS disease, maintaining balanced polymorphism."),

    # 78: Amniocentesis Prenatal Diagnosis Procedure
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <!-- Uterus outline -->
  <circle cx="120" cy="95" r="55" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
  <circle cx="120" cy="95" r="24" fill="#334155"/>
  <text x="120" y="99" fill="#fbcfe8" font-size="8" font-family="sans-serif" text-anchor="middle">Fetus</text>
  <!-- Needle aspiration -->
  <line x1="220" y1="40" x2="140" y2="80" stroke="#facc15" stroke-width="3"/>
  <circle cx="225" cy="38" r="4" fill="#facc15"/>
  <text x="240" y="35" fill="#facc15" font-size="9" font-family="sans-serif">Amniotic Needle</text>
  <!-- Steps to diagnosis -->
  <rect x="220" y="65" width="155" height="100" rx="5" fill="#18181b" stroke="#38bdf8" stroke-width="1"/>
  <text x="297" y="85" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Amniocentesis Workflow:</text>
  <text x="297" y="105" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">1. Aspirate amniotic fluid (wk 15-18)</text>
  <text x="297" y="120" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">2. Culture fetal amniocytes</text>
  <text x="297" y="135" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">3. Metaphase karyotyping (47, XX,+21?)</text>
  <text x="297" y="150" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">4. Detects chromosomal aneuploidies</text>
</svg>
</div>
What primary diagnostic purpose is served by amniocentesis during the second trimester of pregnancy?""",
     ["Harvesting shed fetal cells from amniotic fluid for karyotyping and biochemical testing to diagnose chromosomal and metabolic disorders prenatally",
      "Changing the baby's eye color",
      "Injecting antibiotics into the baby's bones",
      "Determining the baby's future adult career"],
     "A", "OSC", "easy",
     "Amniocentesis harvests fetal amniocytes; microscopic karyotype analysis confirms or excludes numerical aberrations (e.g. Down's, Edwards) and uncovers single-gene enzymopathies prenatally."),

    # 79: Phenylketonuria (PKU) Metabolic Pathway
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#111827"/>
  <!-- Substrate -->
  <rect x="30" y="40" width="110" height="40" rx="5" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
  <text x="85" y="58" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Phenylalanine</text>
  <text x="85" y="72" fill="#bfdbfe" font-size="8" font-family="sans-serif" text-anchor="middle">(Dietary Protein)</text>
  <!-- Normal pathway vs blocked -->
  <line x1="140" y1="60" x2="230" y2="60" stroke="#ef4444" stroke-width="3"/>
  <circle cx="185" cy="60" r="14" fill="#ef4444"/>
  <line x1="175" y1="50" x2="195" y2="70" stroke="#ffffff" stroke-width="3"/>
  <text x="185" y="35" fill="#f87171" font-size="8" font-family="sans-serif" text-anchor="middle">NO PAH Enzyme!</text>
  <!-- Normal destination -->
  <rect x="230" y="40" width="90" height="40" rx="5" fill="#334155"/>
  <text x="275" y="65" fill="#94a3b8" font-size="9" font-family="sans-serif" text-anchor="middle">Tyrosine (Blocked)</text>
  <!-- Toxic alternative shunt -->
  <line x1="85" y1="80" x2="85" y2="120" stroke="#facc15" stroke-width="3"/>
  <rect x="30" y="120" width="340" height="45" rx="5" fill="#7f1d1d" stroke="#f87171" stroke-width="2"/>
  <text x="200" y="138" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Accumulation of Phenylpyruvic Acid & Phenylketones</text>
  <text x="200" y="155" fill="#fecaca" font-size="9" font-family="sans-serif" text-anchor="middle">Excreted in urine (PKU) & causes severe toxic brain damage</text>
</svg>
</div>
In Phenylketonuria (PKU), why does toxic phenylpyruvic acid accumulate in an infant's brain and body fluids?""",
     ["Deficiency of phenylalanine hydroxylase (PAH) prevents conversion of phenylalanine to tyrosine, shunting it into neurotoxic phenylketones",
      "The child consumes pure industrial acid",
      "The kidneys refuse to excrete urine",
      "The liver is completely missing at birth"],
     "A", "OSC", "medium",
     "Inability to hydroxylate phenylalanine into tyrosine causes excessive phenylalanine to transaminate into phenylpyruvic acid and phenyllactate, causing microcephaly and intellectual disability."),

    # 80: Ishihara Pseudoisochromatic Color Blindness Plate
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Ishihara Plate Circle -->
  <circle cx="100" cy="95" r="60" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
  <!-- Dot pattern simulating 74 -->
  <text x="100" y="112" fill="#ef4444" font-size="44" font-family="sans-serif" text-anchor="middle" font-weight="bold">74</text>
  <!-- Explanation Panel -->
  <rect x="180" y="35" width="200" height="120" rx="6" fill="#27272a" stroke="#38bdf8" stroke-width="1"/>
  <text x="280" y="55" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Ishihara Color Plate Test</text>
  <text x="280" y="75" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle">Normal Trichromat sees: "74"</text>
  <text x="280" y="95" fill="#f87171" font-size="9" font-family="sans-serif" text-anchor="middle">Red-Green Blind sees: "21" or nothing</text>
  <text x="280" y="120" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle">X-Linked Recessive Trait</text>
  <text x="280" y="135" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Males: 8%  |  Females: 0.4%</text>
</svg>
</div>
Why is red-green color blindness twenty times more prevalent in biological males (~8%) than in biological females (~0.4%)?""",
     ["The opsin pigment genes reside on the X chromosome; males have only one X chromosome and express the disorder directly from a single mutant copy",
      "Males have fewer retinal rod cells than females",
      "Females cannot see the color red",
      "Color blindness is transmitted strictly through the Y chromosome"],
     "A", "OSC", "easy",
     "The green (deuteranopia) and red (protanopia) cone opsin genes are situated on the X chromosome (Xq28); males (hemizygous) express the condition with one mutant allele, whereas females require two."),

    # 81: Simian Crease and Down Syndrome Physical Traits
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Normal Hand Palm -->
  <rect x="40" y="30" width="130" height="130" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="105" y="52" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Normal Palm</text>
  <path d="M 60 85 Q 90 95 130 90" stroke="#cbd5e1" stroke-width="2" fill="none"/>
  <path d="M 70 115 Q 110 125 150 110" stroke="#cbd5e1" stroke-width="2" fill="none"/>
  <text x="105" y="145" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Two separate transverse flexion creases</text>
  <!-- Down Syndrome Simian Crease -->
  <rect x="220" y="30" width="130" height="130" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
  <text x="285" y="52" fill="#f43f5e" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Down's Syndrome</text>
  <line x1="240" y1="100" x2="330" y2="100" stroke="#facc15" stroke-width="4"/>
  <text x="285" y="130" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">SIMIAN CREASE</text>
  <text x="285" y="145" fill="#fbcfe8" font-size="8" font-family="sans-serif" text-anchor="middle">Single continuous transverse palmar line</text>
</svg>
</div>
What dermatoglyphic clinical sign on the palm of the hand is famously associated with Trisomy 21 (Down's syndrome)?""",
     ["A single, continuous transverse palmar flexion crease spanning across the entire palm (Simian crease)",
      "Having 8 fingers on each hand",
      "Complete absence of fingernails",
      "Green colored palm skin"],
     "A", "OSC", "easy",
     "A single transverse palmar crease (historically termed a Simian crease) results from abnormal intrauterine hand flexion dynamics associated with fetal hypotonia in Down's syndrome."),

    # 82: Mendelian Monogenic vs Chromosomal Disorders Classification
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Monogenic Column -->
  <rect x="25" y="25" width="165" height="140" rx="6" fill="#27272a" stroke="#4ade80" stroke-width="2"/>
  <text x="107" y="48" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">MONOGENIC DISORDERS</text>
  <text x="107" y="68" fill="#bbf7d0" font-size="9" font-family="sans-serif" text-anchor="middle">(Single Defective Gene Locus)</text>
  <text x="107" y="90" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">- Sickle Cell Anemia (HbS)</text>
  <text x="107" y="108" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">- Albinism (Tyrosinase)</text>
  <text x="107" y="126" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">- Hemophilia A (Factor VIII)</text>
  <text x="107" y="144" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">- Phenylketonuria (PAH)</text>
  <!-- Chromosomal Column -->
  <rect x="210" y="25" width="165" height="140" rx="6" fill="#27272a" stroke="#38bdf8" stroke-width="2"/>
  <text x="292" y="48" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">CHROMOSOMAL DISORDERS</text>
  <text x="292" y="68" fill="#bfdbfe" font-size="9" font-family="sans-serif" text-anchor="middle">(Aneuploidy / Numerical)</text>
  <text x="292" y="90" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">- Down's (47, Trisomy 21)</text>
  <text x="292" y="108" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">- Turner's (45, XO Monosomy)</text>
  <text x="292" y="126" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">- Klinefelter's (47, XXY)</text>
  <text x="292" y="144" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">- Edwards (47, Trisomy 18)</text>
</svg>
</div>
Which fundamental characteristic separates monogenic genetic disorders from chromosomal disorders according to the comparison chart above?""",
     ["Monogenic disorders arise from point mutations in a single specific gene and follow Mendelian ratios, whereas chromosomal disorders involve whole chromosome additions, deletions, or structural rearrangements",
      "Monogenic disorders only occur in plants while chromosomal disorders occur in animals",
      "Chromosomal disorders can be cured with simple aspirin",
      "Monogenic disorders have no DNA involvement"],
     "A", "OSC", "easy",
     "Monogenic conditions follow predictable Mendelian segregation originating from a single defective gene sequence (e.g. point mutation), whereas chromosomal disorders stem from non-disjunction of entire chromosomes.")
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

output_path = os.path.join(os.path.dirname(__file__), "ch16_topic5.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
