# scripts/generate_ch16_topic3.py
# MH-9-SCIT-16-16.3: Mendel's Laws of Inheritance: Monohybrid Cross (3:1 Phenotype, 1:2:1 Genotype)
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-16-16.3"

exam_data = [
    # 1-10: Mendel's Experimental System & Genetics Terminology
    ("Who is universally recognized as the 'Father of Genetics' for discovering the fundamental laws of inheritance?",
     ["Gregor Johann Mendel", "Charles Darwin", "Thomas Hunt Morgan", "Jean-Baptiste Lamarck"],
     "A", "OSC", "easy",
     "Gregor Johann Mendel established the principles of inheritance through systematic breeding experiments on garden pea plants between 1856 and 1863 at the Augustinian Abbey in Brno."),

    ("What is the scientific binomial botanical name of the garden pea plant selected by Mendel for his genetic breeding experiments?",
     ["Pisum sativum", "Lathyrus odoratus", "Phaseolus vulgaris", "Cicer arietinum"],
     "A", "OSC", "easy",
     "Mendel selected the common garden pea, Pisum sativum, because of its annual life cycle, ease of cultivation, bisexual flowers, and clear contrasting traits."),

    ("Why was the garden pea (Pisum sativum) an exceptionally advantageous model organism for Mendel's inheritance experiments?",
     ["It naturally self-pollinates, can be easily cross-pollinated artificially, has a short life cycle, and displays sharply contrasting traits",
      "It grows only once every 50 years",
      "It produces sterile seeds that cannot reproduce",
      "It has over 1,000 chromosomes"],
     "A", "OSC", "easy",
     "Pisum sativum naturally undergoes self-pollination due to cleistogamous flowers, allows simple emasculation and manual hybridization, and yields abundant offspring per generation."),

    ("How many pairs of contrasting morphological characters in pea plants did Mendel study in his hybridization experiments?",
     ["7 pairs of contrasting traits", "4 pairs", "12 pairs", "23 pairs"],
     "A", "OSC", "easy",
     "Mendel methodically analyzed 7 distinct pairs of contrasting traits governing seed shape, seed color, flower color, flower position, pod shape, pod color, and stem height."),

    ("Which of the following represents a DOMINANT trait in Mendel's garden pea experiments?",
     ["Round seed shape", "Wrinkled seed shape", "Green seed color", "Constricted pod shape"],
     "A", "OSC", "easy",
     "Round seed shape (R) is dominant over wrinkled seed shape (r); round seeds result from functional starch branching enzyme (SBEI)."),

    ("In pea plants, which flower position trait is dominant over the other?",
     ["Axial flower position is dominant over terminal flower position",
      "Terminal flower position is dominant over axial",
      "Both flower positions are always codominant",
      "Pea flowers have no fixed positions"],
     "A", "OSC", "medium",
     "Flowers born axially along leaf axils (A) are dominant over flowers clustered exclusively at the terminal apex of the stem (a)."),

    ("In pea plants, green pod color is ________ while yellow pod color is ________.",
     ["dominant ; recessive", "recessive ; dominant", "codominant ; recessive", "incompletely dominant ; neutral"],
     "A", "OSC", "medium",
     "For pod color, green (G) is dominant over yellow (g); note that for seed color, the opposite is true (yellow seed color is dominant over green seed color)."),

    ("What is the observable physical appearance or morphological expression of an organism's genetic makeup called?",
     ["Phenotype", "Genotype", "Karyotype", "Archetype"],
     "A", "OSC", "easy",
     "Phenotype refers to the observable structural, physiological, or biochemical manifestations of an individual resulting from the interaction of its genotype with the environment."),

    ("What is the genetic constitution or specific allelic combination of an individual organism called?",
     ["Genotype", "Phenotype", "Protype", "Serotype"],
     "A", "OSC", "easy",
     "Genotype refers to the internal allelic complement (e.g. TT, Tt, or tt) that underlies an organism's phenotypic traits."),

    ("Alternative forms or variant nucleotide sequences of the same gene that occupy corresponding loci on homologous chromosomes are termed:",
     ["Alleles (Allelomorphs)", "Chromatids", "Centromeres", "Mutagens"],
     "A", "OSC", "easy",
     "Alleles are alternative versions of a gene (such as T for tallness and t for dwarfness) situated at identical genomic coordinates on homologous chromosomes."),

    # 11-20: Monohybrid Cross Ratios & Laws
    ("An organism that possesses two identical alleles for a specific trait (e.g. TT or tt) is described as:",
     ["Homozygous (Pure breeding)", "Heterozygous (Hybrid)", "Hemizygous", "Aneuploid"],
     "A", "OSC", "easy",
     "Homozygotes carry identical maternal and paternal alleles at a given locus (homozygous dominant TT or homozygous recessive tt), breeding true when selfed."),

    ("An individual containing two different alleles for a particular character (e.g. Tt) is described as:",
     ["Heterozygous (Hybrid)", "Homozygous", "Monoploid", "Polyploid"],
     "A", "OSC", "easy",
     "Heterozygotes carry two discordant alleles at a single locus (Tt), with the dominant allele masking the expression of the recessive allele in the phenotype."),

    ("A genetic breeding cross that tracks the inheritance of ONE single pair of contrasting characters is designated a:",
     ["Monohybrid cross", "Dihybrid cross", "Trihybrid cross", "Test cross"],
     "A", "OSC", "easy",
     "A monohybrid cross investigates the transmission pattern of a single genetic trait (such as plant height: tall vs dwarf) across successive filial generations."),

    ("When Mendel crossed a pure true-breeding tall pea plant (TT) with a pure true-breeding dwarf pea plant (tt), what was the phenotype of ALL F1 generation progeny?",
     ["100% Tall pea plants", "50% Tall and 50% Dwarf", "100% Dwarf plants", "100% Intermediate medium-height plants"],
     "A", "OSC", "easy",
     "All F1 offspring inherit a dominant T allele from the tall parent and a recessive t allele from the dwarf parent (genotype Tt), manifesting 100% tall phenotypes."),

    ("Which allele expresses itself in the phenotype of a heterozygous individual (Tt), completely masking the effect of the partner allele?",
     ["Dominant allele (T)", "Recessive allele (t)", "Codominant allele", "Lethal allele"],
     "A", "OSC", "easy",
     "The dominant allele expresses its phenotype in both homozygous (TT) and heterozygous (Tt) states, while the recessive allele is masked unless homozygous (tt)."),

    ("What is the classic PHENOTYPIC ratio obtained in the F2 generation of a Mendelian monohybrid cross when F1 hybrids (Tt) are self-pollinated?",
     ["3 Tall : 1 Dwarf (3:1)", "1 Tall : 2 Medium : 1 Dwarf (1:2:1)", "9 Tall : 3 Dwarf : 3 Medium : 1 Short", "1 Tall : 1 Dwarf (1:1)"],
     "A", "OSC", "easy",
     "Selfing F1 plants (Tt x Tt) yields 3 phenotypically tall plants (1 TT + 2 Tt) for every 1 phenotypically dwarf plant (1 tt), producing a 3:1 phenotypic ratio."),

    ("What is the classic GENOTYPIC ratio obtained in the F2 generation of a Mendelian monohybrid cross?",
     ["1 TT : 2 Tt : 1 tt (1:2:1)", "3 TT : 1 tt (3:1)", "9 TT : 3 Tt : 1 tt", "2 TT : 2 tt"],
     "A", "OSC", "easy",
     "F2 monohybrid genotypes segregate as 1 homozygous dominant (TT, 25%) : 2 heterozygous dominant (Tt, 50%) : 1 homozygous recessive (tt, 25%), or 1:2:1."),

    ("Mendel's First Law, which states that when two contrasting factors/alleles are brought together in an F1 hybrid, only one expresses while the other remains suppressed, is the:",
     ["Law of Dominance", "Law of Segregation", "Law of Independent Assortment", "Law of Linkage"],
     "A", "OSC", "easy",
     "The Law of Dominance states that in a heterozygote, the dominant allele dictates the phenotypic outcome while the recessive allele remains phenotypically latent."),

    ("Mendel's Second Law, which states that during gamete formation, the two alleles of a gene pair segregate cleanly without blending so each gamete receives only one allele, is the:",
     ["Law of Segregation (Purity of Gametes)", "Law of Dominance", "Law of Independent Assortment", "Law of Multiple Alleles"],
     "A", "OSC", "easy",
     "The Law of Segregation dictates that homologous chromosomes separate during anaphase I of meiosis, ensuring gametes are 100% pure for a single allele."),

    ("Who invented the graphical grid or checkerboard method widely used by geneticists to calculate probabilities of all possible offspring genotypes from parental gametes?",
     ["Reginald C. Punnett (Punnett Square)", "Gregor Mendel", "Francis Crick", "Thomas Morgan"],
     "A", "OSC", "medium",
     "English geneticist Reginald Punnett designed the Punnett square in 1905 as a tabular matrix displaying maternal and paternal gametic combinations."),

    # 21-30: Test Cross, Back Cross & Numerical Problems
    ("What type of cross is performed by breeding an individual of unknown or dominant phenotype (such as T_) with a homozygous recessive individual (tt)?",
     ["Test cross", "Reciprocal cross", "Dihybrid cross", "Inbreeding cross"],
     "A", "OSC", "medium",
     "A test cross breeds an organism displaying a dominant phenotype with a homozygous recessive tester to determine whether it is homozygous (TT) or heterozygous (Tt)."),

    ("If an F1 tall pea plant (Tt) is subjected to a test cross with a dwarf pea plant (tt), what is the expected phenotypic and genotypic ratio among the offspring?",
     ["1 Tall : 1 Dwarf (50% Tall, 50% Dwarf)", "3 Tall : 1 Dwarf", "All 100% Tall", "All 100% Dwarf"],
     "A", "OSC", "medium",
     "Crossing heterozygous Tt with homozygous recessive tt yields 50% Tt (tall) and 50% tt (dwarf), producing a characteristic 1:1 test cross ratio."),

    ("If a test cross of a tall pea plant produces 100 offspring and ALL 100 are tall, what was the genotype of the parent plant?",
     ["Homozygous dominant (TT)", "Heterozygous (Tt)", "Homozygous recessive (tt)", "Cannot be determined"],
     "A", "OSC", "easy",
     "A test cross yielding 100% dominant progeny proves that the tested parent contributed exclusively dominant T alleles to every gamete, confirming genotype TT."),

    ("A cross between an F1 hybrid individual and ANY of its parental genotypes (dominant or recessive) is broadly known as a:",
     ["Back cross", "Monohybrid cross", "Test cross only", "Polyhybrid cross"],
     "A", "OSC", "medium",
     "A back cross refers to any mating between an F1 offspring and one of its parents; a test cross is a specific sub-type where the parent is homozygous recessive."),

    ("If 400 pea plants are produced in the F2 generation of a standard monohybrid cross (Tt x Tt), approximately how many plants are expected to be DWARF?",
     ["100 dwarf plants (25%)", "300 dwarf plants", "200 dwarf plants", "50 dwarf plants"],
     "A", "ONE", "easy",
     "The Mendelian F2 monohybrid phenotypic ratio is 3 tall : 1 dwarf (1/4 dwarf). One-quarter of 400 plants $= 400 / 4 = 100$ dwarf plants."),

    ("In an F2 monohybrid population of 600 tall pea plants, how many are statistically expected to be HETEROZYGOUS (Tt)?",
     ["400 plants (2/3 of tall plants)", "200 plants", "300 plants", "600 plants"],
     "A", "ONE", "medium",
     "Among F2 tall plants (1 TT : 2 Tt), two-thirds are heterozygous Tt. Therefore, $600 \\times (2/3) = 400$ plants are heterozygous."),

    ("What percentage of gametes produced by a heterozygous tall pea plant (Tt) will carry the RECESSIVE allele (t)?",
     ["50% of gametes", "25% of gametes", "75% of gametes", "100% of gametes"],
     "A", "ONE", "easy",
     "Meiotic segregation ensures that the two alleles T and t separate into equal halves of gametes: 50% carry T and 50% carry t."),

    ("Why is Mendel's Law of Segregation considered an exception-less, universal law of genetics for all sexually reproducing diploid organisms?",
     ["Homologous chromosomes and their alleles must physically separate during Meiosis I to produce haploid gametes without blending",
      "Because DNA can never mutate",
      "Because all organisms have pea plants in their cells",
      "Because dominance always fails in plants"],
     "A", "OSC", "medium",
     "Unlike the Law of Dominance (which shows incomplete dominance and codominance exceptions), segregation of homologous alleles during meiotic anaphase I is universal."),

    ("In Mirabilis jalapa (4 o'clock plant), crossing pure red flowers (RR) with pure white flowers (rr) produces all PINK flowers (Rr) in F1. This non-Mendelian phenomenon is called:",
     ["Incomplete dominance", "Codominance", "Multiple allelism", "Polygenic inheritance"],
     "A", "OSC", "medium",
     "In incomplete dominance, neither allele is completely dominant; heterozygous individuals display an intermediate blended phenotype (pink), with F2 phenotypic ratio 1:2:1."),

    ("In human ABO blood groups, an individual with genotype IAIB expresses both A and B antigens equally on red blood cells. This phenomenon is called:",
     ["Codominance", "Incomplete dominance", "Pleiotropy", "Epistasis"],
     "A", "OSC", "easy",
     "In codominance, both alleles express their full biological effects independently in heterozygotes without blending or masking each other."),

    # 31-40: Fill in blanks, Numerical, Multi-choice
    ("When an F1 hybrid tall pea plant (Tt) is self-pollinated, the phenotypic ratio observed in the F2 generation is ________.",
     ["3 Tall : 1 Dwarf (3:1)", "1 Tall : 2 Medium : 1 Dwarf", "9 Tall : 7 Dwarf", "1 Tall : 1 Dwarf"],
     "A", "OFB", "easy",
     "Selfing heterozygous F1 hybrids yields a 3:1 phenotypic ratio (75% dominant tall and 25% recessive dwarf)."),

    ("In an F2 monohybrid generation consisting of 800 pea plants, how many plants are statistically expected to have the heterozygous genotype (Tt)?",
     ["400 plants (50%)", "200 plants", "600 plants", "800 plants"],
     "A", "ONE", "easy",
     "The genotypic segregation ratio is 1 TT (25%) : 2 Tt (50%) : 1 tt (25%). Exactly 50% of 800 plants $= 800 \\times 0.50 = 400$ plants."),

    ("State whether True or False: In a monohybrid cross, the F1 generation expresses both dominant and recessive traits in equal numbers.",
     ["False", "True"],
     "A", "OTF", "easy",
     "In the F1 generation of a cross between pure-breeding contrasting parents, 100% of the progeny display strictly the dominant phenotype due to the Law of Dominance."),

    ("Which of the following statements are correct regarding Mendel's monohybrid cross? (Select all that apply)",
     ["The F1 generation is 100% heterozygous tall, and the F2 generation displays a 3:1 phenotypic ratio",
      "The F1 generation is 100% dwarf",
      "The F2 generation contains no dwarf plants whatsoever",
      "Pea plants do not obey laws of probability"],
     "A", "OMC", "easy",
     "Mendel's monohybrid crosses consistently demonstrated uniform F1 dominance followed by clear 3:1 phenotypic segregation in the F2 generation."),

    ("Assertion (A): Recessive traits do not appear in the F1 generation of a cross between pure-breeding contrasting parents.\nReason (R): The dominant allele suppresses the phenotypic expression of the recessive allele in the heterozygous condition.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is not the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "easy",
     "The Law of Dominance explains why heterozygous F1 individuals display only the dominant phenotype while the recessive allele remains phenotypically latent."),

    ("What is the term for a single gene that simultaneously controls or influences multiple, apparently unrelated phenotypic traits in an organism?",
     ["Pleiotropy (Pleiotropic gene)", "Polygenic inheritance", "Multiple allelism", "Codominance"],
     "A", "OSC", "medium",
     "A pleiotropic gene influences multiple phenotypic characteristics; for example, the sickle-cell gene affects both erythrocyte shape and resistance to malaria."),

    ("Which genetic term describes an organism or cell having only ONE single allele for a particular gene, such as X-linked genes in human males (XY)?",
     ["Hemizygous", "Homozygous", "Heterozygous", "Nullizygous"],
     "A", "OSC", "medium",
     "Human males possess only one X chromosome and are therefore hemizygous for all non-pseudoautosomal X-linked loci, expressing recessive X-linked alleles directly."),

    ("If you cross a pure yellow-seeded pea plant (YY) with a pure green-seeded pea plant (yy), what percentage of F2 plants will produce GREEN seeds?",
     ["25% (1/4)", "75% (3/4)", "50% (1/2)", "0%"],
     "A", "ONE", "easy",
     "In the F2 generation, 1/4 (25%) of the progeny inherit the homozygous recessive genotype yy, producing green seeds."),

    ("What phenotypic ratio is obtained in the F2 generation of a monohybrid cross when the two alleles exhibit INCOMPLETE dominance (e.g., Snapdragons)?",
     ["1 : 2 : 1 (1 Red : 2 Pink : 1 White)", "3 : 1", "9 : 3 : 3 : 1", "1 : 1"],
     "A", "OSC", "easy",
     "Incomplete dominance yields three distinct phenotypic classes corresponding exactly to the 1:2:1 genotypic ratio."),

    ("Which statistical hypothesis test did geneticists historically apply to Mendel's experimental data to confirm that observed counts matched theoretical ratios?",
     ["Chi-square (chi^2) goodness-of-fit test", "Student's t-test", "ANOVA test", "Z-test"],
     "A", "OSC", "medium",
     "The chi-square goodness-of-fit test calculates the sum of squared deviations between observed and expected Mendelian numbers to evaluate statistical concordance.")
]

practice_data = [
    # 41-50: Advanced Genetics Scenarios & Calculations
    ("Why did Mendel's results remain unrecognized and unappreciated by the scientific community until their dramatic rediscovery in 1900?",
     ["Mendel applied advanced mathematical and statistical analysis to biology ahead of his time, and contemporary biologists were absorbed by Darwin's theories",
      "Mendel lost all his notes in a fire",
      "Pea plants became extinct in 1865",
      "Mendel never published his paper in any journal"],
     "A", "OSC", "medium",
     "Mendel's rigorous quantitative combinatorial methodology clashed with the purely qualitative descriptive botany of the 1860s until de Vries, Correns, and Tschermak verified it in 1900."),

    ("Which three scientists independently rediscovered and confirmed Mendel's laws of inheritance in the year 1900?",
     ["Hugo de Vries, Carl Correns, and Erich von Tschermak",
      "Watson, Crick, and Franklin",
      "Darwin, Wallace, and Lamarck",
      "Schleiden, Schwann, and Virchow"],
     "A", "OSC", "medium",
     "In 1900, Hugo de Vries (Netherlands), Carl Correns (Germany), and Erich von Tschermak (Austria) independently confirmed Mendelian segregation ratios in separate hybridization studies."),

    ("What is the genotypic ratio among the F2 offspring of a monohybrid cross exhibiting INCOMPLETE dominance (such as flower color in Antirrhinum majus)?",
     ["1 Red : 2 Pink : 1 White (1:2:1)", "3 Red : 1 White (3:1)", "9 Red : 7 White", "1 Red : 1 White"],
     "A", "OSC", "medium",
     "In incomplete dominance, the phenotypic ratio matches the genotypic ratio exactly: 1 homozygous dominant (red) : 2 heterozygotes (pink) : 1 homozygous recessive (white), or 1:2:1."),

    ("If a homozygous black guinea pig (BB) is crossed with a homozygous white guinea pig (bb), what proportion of the F2 generation will be homozygous?",
     ["50% (25% BB and 25% bb)", "100%", "25%", "75%"],
     "A", "ONE", "medium",
     "The F2 genotypic ratio is 1 BB (25%) : 2 Bb (50%) : 1 bb (25%). The total homozygous fraction is $25\\% + 25\\% = 50\\%$."),

    ("If a heterozygous purple-flowered pea plant (Pp) is crossed with a white-flowered pea plant (pp), what percentage of the progeny will have WHITE flowers?",
     ["50% white flowers", "25% white flowers", "75% white flowers", "0% white flowers"],
     "A", "ONE", "easy",
     "This is a standard monohybrid test cross: Pp x pp yields 50% Pp (purple) and 50% pp (white)."),

    ("State whether True or False: A recessive allele can only express its phenotype in an organism when it is in the homozygous state.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Because a dominant allele masks recessive expression in heterozygotes, recessive traits emerge phenotypically only when both homologous loci carry the recessive allele (homozygous recessive)."),

    ("What molecular mechanism explains why wrinkled pea seeds (rr) are wrinkled while round pea seeds (R_) are smooth?",
     ["Wrinkled seeds lack the functional SBEI enzyme, causing accumulation of free sucrose which absorbs water, swells, and subsequently wrinkles upon desiccation",
      "Wrinkled seeds have no cell walls",
      "Wrinkled seeds are infected with bacteria",
      "Smooth seeds are coated in pure animal wax"],
     "A", "OSC", "hard",
     "Loss-of-function mutation in the starch branching enzyme (SBEI) gene leads to high free sucrose and high osmotic water uptake during development; shrinkage during drying leaves the testa wrinkled."),

    ("What is an emasculation step in artificial cross-pollination experiments?",
     ["Surgical removal of anthers from the bisexual flower bud of the designated female parent before pollen matures",
      "Removal of all petals from the plant",
      "Cutting down the plant stem completely",
      "Watering the plant with hot salt water"],
     "A", "OSC", "easy",
     "Emasculation removes the stamens/anthers before dehiscence, preventing self-pollination and ensuring fertilization occurs exclusively with designated donor pollen."),

    ("Why did Mendel cover emasculated flowers with paper or butter-paper bags ('bagging')?",
     ["To prevent unwanted foreign airborne pollen or insect-borne pollen from contaminating the receptive stigma",
      "To protect the flower from rainwater",
      "To keep the flower warm at night",
      "To make the flower grow faster"],
     "A", "OSC", "easy",
     "Bagging protects the emasculated stigma from rogue airborne or insect-carried pollen grains until artificial pollination with selected pollen is performed."),

    ("State whether True or False: In a monohybrid cross between two heterozygous plants (Tt x Tt), the probability that any single offspring will be homozygous tall (TT) is 1/4 (25%).",
     ["True", "False"],
     "A", "OTF", "easy",
     "Punnett square probabilities indicate: $P(TT) = 1/2 \\times 1/2 = 1/4$ (25%), $P(Tt) = 2/4$ (50%), and $P(tt) = 1/4$ (25%).")
]

# Additional 20 practice questions to reach exactly 30 questions
practice_data.extend([
    # 51-60: Further Monohybrid Genetic Calculations
    ("In garden peas, yellow seed color (Y) is dominant over green seed color (y). If an F1 hybrid (Yy) is selfed, what fraction of yellow-seeded F2 plants are TRUE-BREEDING?",
     ["1/3 of yellow-seeded plants", "2/3 of yellow-seeded plants", "1/4 of yellow-seeded plants", "1/2 of yellow-seeded plants"],
     "A", "OSC", "medium",
     "The yellow-seeded F2 plants have genotypes 1 YY : 2 Yy. Out of 3 yellow plants, exactly 1 is homozygous true-breeding (YY), representing 1/3 (33.3%)."),

    ("If two parents with normal skin pigmentation have an albino child (autosomal recessive condition, aa), what are the genotypes of the parents?",
     ["Both parents are heterozygous carriers (Aa x Aa)", "One is AA and one is aa", "Both are homozygous recessive aa", "Both are homozygous dominant AA"],
     "A", "OSC", "easy",
     "An albino child (aa) must receive one recessive allele 'a' from each parent; since both parents appear normal, both must be heterozygous carriers (Aa)."),

    ("What is the probability that a child born to two heterozygous carriers of an autosomal recessive trait will be completely FREE of the disease allele (genotype AA)?",
     ["25% (1/4)", "50% (1/2)", "75% (3/4)", "0%"],
     "A", "ONE", "medium",
     "Cross Aa x Aa yields 1 AA (25%) : 2 Aa (50%) : 1 aa (25%). The chance of inheriting two normal dominant alleles (AA) is exactly 1/4 or 25%."),

    ("Which of the following Mendelian crosses will produce a phenotypic ratio of 1 dominant : 1 recessive?",
     ["Heterozygote x Homozygous recessive (Tt x tt)", "Heterozygote x Heterozygote (Tt x Tt)", "Homozygous dominant x Homozygous recessive (TT x tt)", "Homozygous dominant x Heterozygote (TT x Tt)"],
     "A", "OSC", "easy",
     "A monohybrid test cross (Tt x tt) yields 50% tall (Tt) and 50% dwarf (tt), producing a 1:1 phenotypic outcome."),

    ("Which Mendelian cross produces 100% phenotypic dominant offspring with a genotypic ratio of 1 homozygous dominant : 1 heterozygous dominant?",
     ["Homozygous dominant x Heterozygote (TT x Tt)", "Heterozygote x Heterozygote (Tt x Tt)", "Heterozygote x Homozygous recessive (Tt x tt)", "TT x tt"],
     "A", "OSC", "medium",
     "Crossing TT x Tt produces 50% TT and 50% Tt; all 100% exhibit the dominant tall phenotype, but the genotypic ratio is 1:1."),

    ("State whether True or False: Mendel called genes 'factors' (or elementen) because the physical chemical nature of DNA was unknown in his lifetime.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Mendel deduced the existence of discrete, particulate hereditary units which he named 'factors'; the word 'gene' was later coined by Wilhelm Johannsen in 1909."),

    ("A pure-breeding tall pea plant with terminal flowers (TTaa) is crossed with a pure-breeding dwarf plant with axial flowers (ttAA). What will be the phenotype of F1 plants?",
     ["All Tall with Axial flowers", "All Dwarf with Terminal flowers", "50% Tall and 50% Dwarf", "All Dwarf with Axial flowers"],
     "A", "OSC", "medium",
     "All F1 progeny inherit dominant alleles for both traits (TtAa); since Tall and Axial are dominant, all F1 plants are phenotypically Tall with Axial flowers."),

    ("In guinea pigs, short hair (S) is dominant over long hair (s). If a short-haired guinea pig crossed with a long-haired guinea pig produces 4 short-haired and 5 long-haired offspring, what is the genotype of the short-haired parent?",
     ["Heterozygous (Ss)", "Homozygous dominant (SS)", "Homozygous recessive (ss)", "Cannot be determined"],
     "A", "OSC", "easy",
     "The occurrence of long-haired offspring (ss) requires one recessive allele from each parent; therefore, the short-haired parent must be heterozygous (Ss)."),

    ("How many different types of gametes can be produced by an individual with genotype Tt for a single gene?",
     ["2 types of gametes (T and t)", "1 type", "4 types", "8 types"],
     "A", "ONE", "easy",
     "A monohybrid heterozygote (Tt) produces two distinct gametic types in equal 50:50 proportions: gamete T and gamete t ($2^1 = 2$)."),

    ("State whether True or False: Mendel's monohybrid cross proved that hereditary traits do NOT blend or dilute, but remain distinct particulate units across generations.",
     ["True", "False"],
     "A", "OTF", "easy",
     "The reappearance of the pristine dwarf trait in F2 in full unblended form disproved the prevailing 'blending inheritance' theory of the 19th century.")
])

# 10 more questions to reach 30 questions
practice_data.extend([
    # 61-70: High-Yield Practice Questions
    ("In a cross between two heterozygous tall pea plants (Tt x Tt), what is the probability that an offspring displaying the dominant tall phenotype is HETEROZYGOUS?",
     ["2/3 (approximately 66.7%)", "1/2 (50%)", "1/4 (25%)", "3/4 (75%)"],
     "A", "OSC", "medium",
     "Given that the offspring is tall, the sample space is restricted to {TT, Tt, Tt}. Among these 3 tall genotypes, exactly 2 are heterozygous (Tt), so the conditional probability is 2/3."),

    ("What is the biological definition of a 'pure line' or true-breeding organism in plant genetics?",
     ["A homozygous lineage that consistently produces offspring with identical phenotypic traits over multiple generations of self-pollination",
      "A plant that has been treated with chemical fertilizers",
      "A hybrid plant that produces 10 different flower colors",
      "A plant that reproduces strictly by root budding"],
     "A", "OSC", "medium",
     "True-breeding pure lines are homozygous at the studied loci; repeated self-fertilization maintains stable, uniform parental phenotypes generation after generation."),

    ("What term did Wilhelm Johannsen introduce in 1909 to replace Mendel's term 'factor'?",
     ["Gene", "Chromosome", "Centromere", "Allele"],
     "A", "OSC", "easy",
     "Danish botanist Wilhelm Johannsen coined the terms 'gene', 'genotype', and 'phenotype' in 1909 to formalize Mendelian genetics."),

    ("If a trait is governed by a single gene with two alleles showing complete dominance, how many distinct PHENOTYPIC classes are possible?",
     ["2 phenotypic classes (Dominant and Recessive)", "3 phenotypic classes", "4 phenotypic classes", "1 phenotypic class"],
     "A", "ONE", "easy",
     "With complete dominance, homozygous dominant (TT) and heterozygous (Tt) exhibit the identical dominant phenotype, leaving only 2 observable classes: dominant and recessive."),

    ("State whether True or False: In a test cross, the phenotypic ratio directly mirrors the genotypic ratio of the gametes produced by the tested individual.",
     ["True", "False"],
     "A", "OTF", "medium",
     "Because the homozygous recessive tester contributes only non-masking recessive alleles, the resulting progeny phenotypes directly reveal the gametic frequencies of the tested parent."),

    ("A garden pea plant with genotype tt is crossed with another plant of genotype tt. What percentage of the offspring will be dwarf?",
     ["100% dwarf plants", "50% dwarf", "25% dwarf", "0% dwarf"],
     "A", "ONE", "easy",
     "Both parents contribute exclusively recessive 't' alleles; 100% of the offspring have genotype tt and are dwarf."),

    ("Which pair of contrasting characters in pea plants was used by Mendel in his classic stem height monohybrid cross?",
     ["Tall stem vs Dwarf stem", "Round seed vs Wrinkled seed", "Yellow seed vs Green seed", "Green pod vs Yellow pod"],
     "A", "OSC", "easy",
     "Mendel's primary monohybrid cross analyzed tall vines (approx 6-7 feet tall) versus dwarf vines (approx 0.75-1.5 feet tall)."),

    ("What proportion of the F2 generation in a standard monohybrid cross exhibits the RECESSIVE phenotype?",
     ["1/4 (25%)", "3/4 (75%)", "1/2 (50%)", "2/3 (66.7%)"],
     "A", "OSC", "easy",
     "The recessive phenotype (tt) emerges only in homozygous recessive individuals, accounting for exactly 1 out of 4 F2 offspring (25%)."),

    ("If an F1 plant (Tt) produces 1,000 pollen grains, approximately how many of these pollen grains carry the dominant allele 'T'?",
     ["500 pollen grains", "250 pollen grains", "750 pollen grains", "1,000 pollen grains"],
     "A", "ONE", "easy",
     "Equal meiotic segregation produces 50% T-bearing microspores and 50% t-bearing microspores: $1,000 \\times 0.50 = 500$ pollen grains carry 'T'."),

    ("State whether True or False: Mendel's Law of Segregation occurs physically during Anaphase I of meiosis when homologous chromosomes separate to opposite poles.",
     ["True", "False"],
     "A", "OTF", "easy",
     "During meiotic Anaphase I, homologous chromosomes bearing alternative alleles segregate to opposite spindle poles, physically enacting Mendel's Law of Segregation.")
])

mock_data = [
    # 71: The 7 Pairs of Contrasting Traits in Pisum sativum
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="210" viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="210" rx="8" fill="#090d16"/>
  <!-- Header -->
  <text x="50" y="25" fill="#facc15" font-size="10" font-family="sans-serif" font-weight="bold">Character</text>
  <text x="190" y="25" fill="#4ade80" font-size="10" font-family="sans-serif" font-weight="bold">Dominant Trait</text>
  <text x="310" y="25" fill="#f87171" font-size="10" font-family="sans-serif" font-weight="bold">Recessive Trait</text>
  <line x1="20" y1="32" x2="380" y2="32" stroke="#334155" stroke-width="1"/>
  <!-- Row 1: Seed Shape -->
  <text x="50" y="52" fill="#cbd5e1" font-size="9" font-family="sans-serif">1. Seed Shape</text>
  <text x="190" y="52" fill="#4ade80" font-size="9" font-family="sans-serif">Round (R)</text>
  <text x="310" y="52" fill="#f87171" font-size="9" font-family="sans-serif">Wrinkled (r)</text>
  <!-- Row 2: Seed Color -->
  <text x="50" y="75" fill="#cbd5e1" font-size="9" font-family="sans-serif">2. Seed Color</text>
  <text x="190" y="75" fill="#facc15" font-size="9" font-family="sans-serif">Yellow (Y)</text>
  <text x="310" y="75" fill="#22c55e" font-size="9" font-family="sans-serif">Green (y)</text>
  <!-- Row 3: Pod Color -->
  <text x="50" y="98" fill="#cbd5e1" font-size="9" font-family="sans-serif">3. Pod Color</text>
  <text x="190" y="98" fill="#22c55e" font-size="9" font-family="sans-serif">Green (G)</text>
  <text x="310" y="98" fill="#facc15" font-size="9" font-family="sans-serif">Yellow (g)</text>
  <!-- Row 4: Pod Shape -->
  <text x="50" y="121" fill="#cbd5e1" font-size="9" font-family="sans-serif">4. Pod Shape</text>
  <text x="190" y="121" fill="#4ade80" font-size="9" font-family="sans-serif">Inflated (I)</text>
  <text x="310" y="121" fill="#f87171" font-size="9" font-family="sans-serif">Constricted (i)</text>
  <!-- Row 5: Flower Color -->
  <text x="50" y="144" fill="#cbd5e1" font-size="9" font-family="sans-serif">5. Flower Color</text>
  <text x="190" y="144" fill="#c084fc" font-size="9" font-family="sans-serif">Violet / Purple</text>
  <text x="310" y="144" fill="#ffffff" font-size="9" font-family="sans-serif">White</text>
  <!-- Row 6: Stem Height -->
  <text x="50" y="167" fill="#cbd5e1" font-size="9" font-family="sans-serif">6. Stem Height</text>
  <text x="190" y="167" fill="#38bdf8" font-size="9" font-family="sans-serif">Tall (T)</text>
  <text x="310" y="167" fill="#f87171" font-size="9" font-family="sans-serif">Dwarf (t)</text>
  <!-- Row 7: Flower Pos -->
  <text x="50" y="190" fill="#cbd5e1" font-size="9" font-family="sans-serif">7. Flower Position</text>
  <text x="190" y="190" fill="#38bdf8" font-size="9" font-family="sans-serif">Axial (A)</text>
  <text x="310" y="190" fill="#f87171" font-size="9" font-family="sans-serif">Terminal (a)</text>
</svg>
</div>
Based on Mendel's 7 pairs of contrasting traits tabulated above, what paradoxical relationship exists between the dominant colors of pea seeds and pea pods?""",
     ["Yellow is dominant for seed color while Green is dominant for pod color",
      "Green is dominant for both seeds and pods",
      "Yellow is recessive for both seeds and pods",
      "White is dominant for both seeds and pods"],
     "A", "OSC", "medium",
     "In garden peas, yellow seed color (Y) is dominant over green seed color (y), whereas green pod color (G) is dominant over yellow pod color (g)."),

    # 72: Monohybrid Cross Punnett Square (F2 Checkerboard)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Punnett Grid -->
  <!-- Header row / col -->
  <text x="80" y="60" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle">Gametes</text>
  <text x="140" y="45" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">T</text>
  <text x="210" y="45" fill="#f87171" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">t</text>
  <text x="65" y="90" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">T</text>
  <text x="65" y="145" fill="#f87171" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">t</text>
  <!-- Box 1 (TT) -->
  <rect x="105" y="60" width="70" height="50" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="140" y="85" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">TT</text>
  <text x="140" y="100" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Tall (Pure)</text>
  <!-- Box 2 (Tt) -->
  <rect x="175" y="60" width="70" height="50" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="210" y="85" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">Tt</text>
  <text x="210" y="100" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Tall (Hybrid)</text>
  <!-- Box 3 (Tt) -->
  <rect x="105" y="110" width="70" height="50" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="140" y="135" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">Tt</text>
  <text x="140" y="150" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Tall (Hybrid)</text>
  <!-- Box 4 (tt) -->
  <rect x="175" y="110" width="70" height="50" fill="#1e293b" stroke="#f87171" stroke-width="2"/>
  <text x="210" y="135" fill="#f87171" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">tt</text>
  <text x="210" y="150" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">Dwarf (Pure)</text>
  <!-- Summary Box -->
  <rect x="260" y="45" width="125" height="115" rx="6" fill="#27272a" stroke="#facc15" stroke-width="1"/>
  <text x="322" y="68" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">F2 Outcome:</text>
  <text x="322" y="90" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle">Phenotypic: 3 : 1</text>
  <text x="322" y="105" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">(75% Tall : 25% Dwarf)</text>
  <text x="322" y="130" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle">Genotypic: 1:2:1</text>
  <text x="322" y="145" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">(1 TT : 2 Tt : 1 tt)</text>
</svg>
</div>
In the F2 monohybrid Punnett square above, what proportion of the phenotypically tall pea plants are HETEROZYGOUS carriers of the dwarf allele (genotype Tt)?""""",
     ["2/3 of the tall plants (66.7%)", "1/2 of the tall plants", "1/4 of the tall plants", "100% of the tall plants"],
     "A", "OSC", "medium",
     "Among the three tall F2 boxes (1 TT and 2 Tt), two out of three tall plants carry the heterozygous genotype Tt, representing a fraction of 2/3 (66.7%)."),

    # 73: Monohybrid Test Cross (Tt x tt)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#0f172a"/>
  <!-- Cross header -->
  <rect x="30" y="20" width="340" height="35" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="200" y="42" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">TEST CROSS: F1 Hybrid (Tt) x Homozygous Recessive (tt)</text>
  <!-- Gametes -->
  <text x="90" y="80" fill="#facc15" font-size="10" font-family="sans-serif">F1 Gametes: 50% T  &  50% t</text>
  <text x="90" y="100" fill="#f87171" font-size="10" font-family="sans-serif">Tester Gamete: 100% t</text>
  <!-- Progeny boxes -->
  <rect x="60" y="125" width="130" height="45" rx="5" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="125" y="145" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Tt (50%)</text>
  <text x="125" y="160" fill="#bbf7d0" font-size="9" font-family="sans-serif" text-anchor="middle">Phenotype: Tall</text>
  <rect x="210" y="125" width="130" height="45" rx="5" fill="#7f1d1d" stroke="#f87171" stroke-width="2"/>
  <text x="275" y="145" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">tt (50%)</text>
  <text x="275" y="160" fill="#fca5a5" font-size="9" font-family="sans-serif" text-anchor="middle">Phenotype: Dwarf</text>
  <text x="200" y="190" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Test Cross Ratio = 1 Tall : 1 Dwarf (1:1)</text>
</svg>
</div>
Why does a monohybrid test cross between a heterozygous tall plant (Tt) and a dwarf plant (tt) always produce a 1:1 phenotypic ratio?""""",
     ["The homozygous recessive parent contributes only 't' alleles, so the phenotype of each offspring directly reflects the 50:50 ratio of T and t gametes from the heterozygous parent",
      "Dwarf alleles destroy all dominant alleles",
      "Tall plants refuse to grow next to dwarf plants",
      "The test cross only produces white flowers"],
     "A", "OSC", "easy",
     "Because the homozygous recessive tester parent donates exclusively non-masking recessive alleles (t), the offspring phenotypes directly exhibit the gametic frequency (1 T : 1 t) of the tested hybrid."),

    # 74: Law of Segregation Meiotic Mechanics
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#111827"/>
  <!-- Diploid Heterozygote cell -->
  <circle cx="90" cy="95" r="45" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <rect x="75" y="75" width="8" height="40" rx="2" fill="#38bdf8"/>
  <text x="79" y="70" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">T</text>
  <rect x="95" y="75" width="8" height="40" rx="2" fill="#f87171"/>
  <text x="99" y="70" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">t</text>
  <text x="90" y="130" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Diploid (Tt)</text>
  <!-- Meiotic division arrows -->
  <line x1="145" y1="95" x2="200" y2="65" stroke="#facc15" stroke-width="2"/>
  <line x1="145" y1="95" x2="200" y2="125" stroke="#facc15" stroke-width="2"/>
  <!-- Gamete 1 (T) -->
  <circle cx="240" cy="65" r="24" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <text x="240" y="70" fill="#38bdf8" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">T</text>
  <text x="310" y="70" fill="#4ade80" font-size="9" font-family="sans-serif">50% Gametes (Pure T)</text>
  <!-- Gamete 2 (t) -->
  <circle cx="240" cy="125" r="24" fill="#1e293b" stroke="#f87171" stroke-width="2"/>
  <text x="240" y="130" fill="#f87171" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">t</text>
  <text x="310" y="130" fill="#f87171" font-size="9" font-family="sans-serif">50% Gametes (Pure t)</text>
  <!-- Caption -->
  <text x="200" y="175" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Mendel's Law of Segregation (Purity of Gametes)</text>
</svg>
</div>
What physical cellular event during meiosis guarantees that gametes remain 100% 'pure' for a single allele, as formulated in Mendel's Law of Segregation?""""",
     ["Homologous chromosome pairs disjoin and migrate to opposite spindle poles during Anaphase I of meiosis",
      "Spindle fibers destroy half of the DNA",
      "DNA polymerase converts recessive alleles into dominant alleles",
      "Gametes fuse together before fertilization"],
     "A", "OSC", "medium",
     "During anaphase I of meiosis, homologous chromosomes bearing alleles T and t segregate independently to opposite daughter cells, ensuring each haploid gamete carries only one unblended allele."),

    # 75: Incomplete Dominance in 4 O'Clock Plant (Mirabilis jalapa)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Parents -->
  <circle cx="80" cy="50" r="18" fill="#dc2626"/>
  <text x="80" y="55" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">RR</text>
  <text x="80" y="80" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">Red Parent</text>
  <text x="130" y="55" fill="#ffffff" font-size="14" font-family="sans-serif">X</text>
  <circle cx="180" cy="50" r="18" fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>
  <text x="180" y="55" fill="#000000" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">rr</text>
  <text x="180" y="80" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">White Parent</text>
  <!-- F1 Hybrid (Pink) -->
  <line x1="130" y1="85" x2="130" y2="110" stroke="#facc15" stroke-width="2"/>
  <circle cx="130" cy="135" r="22" fill="#ec4899"/>
  <text x="130" y="139" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Rr</text>
  <text x="130" y="170" fill="#f472b6" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">100% PINK Flowers!</text>
  <!-- Explanation box -->
  <rect x="230" y="35" width="150" height="130" rx="6" fill="#27272a" stroke="#ec4899" stroke-width="2"/>
  <text x="305" y="58" fill="#ec4899" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Incomplete Dominance</text>
  <text x="305" y="80" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Neither allele is fully dominant</text>
  <text x="305" y="105" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle">F2 Ratio = 1:2:1</text>
  <text x="305" y="125" fill="#e2e8f0" font-size="8" font-family="sans-serif" text-anchor="middle">1 Red : 2 Pink : 1 White</text>
  <text x="305" y="145" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">Phenotype = Genotype</text>
</svg>
</div>
Why does a monohybrid cross in Mirabilis jalapa produce an F2 phenotypic ratio of 1:2:1 instead of the classic Mendelian 3:1 ratio?""""",
     ["Incomplete dominance causes heterozygotes (Rr) to display an intermediate blended pink phenotype, so each distinct genotype has its own unique phenotype",
      "Red pigment dissolves all white pigment permanently",
      "Pea plants cannot produce pink flowers",
      "The white allele is lethal in seeds"],
     "A", "OSC", "medium",
     "Because the single functional R allele in heterozygotes synthesizes only half the normal quantity of anthocyanin pigment, heterozygotes appear intermediate pink, making phenotypic and genotypic ratios identical (1:2:1)."),

    # 76: Emasculation and Bagging in Cross-Pollination
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Step 1: Flower bud emasculation -->
  <rect x="25" y="25" width="165" height="140" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="107" y="48" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Step 1: Emasculation</text>
  <circle cx="107" cy="85" r="20" fill="#334155"/>
  <line x1="95" y1="75" x2="120" y2="95" stroke="#ef4444" stroke-width="3"/>
  <text x="107" y="120" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">Anthers surgically snipped</text>
  <text x="107" y="135" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">before pollen release</text>
  <text x="107" y="152" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">Prevents self-pollination</text>
  <!-- Step 2: Bagging -->
  <rect x="210" y="25" width="165" height="140" rx="6" fill="#1e293b" stroke="#eab308" stroke-width="2"/>
  <text x="292" y="48" fill="#eab308" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Step 2: Bagging</text>
  <rect x="267" y="65" width="50" height="40" rx="4" fill="#854d0e"/>
  <text x="292" y="88" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Bag</text>
  <text x="292" y="120" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">Covered with paper bag</text>
  <text x="292" y="135" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Blocks rogue foreign pollen</text>
  <text x="292" y="152" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">Ensures controlled cross</text>
</svg>
</div>
Why were the twin experimental procedures of emasculation and bagging essential to the success of Mendel's hybridization experiments?""""",
     ["They completely prevented unwanted natural self-pollination and foreign airborne pollen contamination, guaranteeing total parentage control",
      "They kept the flowers moist so seeds would not dry out",
      "They accelerated photosynthesis by 500%",
      "They made the flowers glow in the dark"],
     "A", "OSC", "easy",
     "Emasculation eliminates self-pollination in hermaphroditic pea flowers, and bagging shields the receptive stigma from contamination by random insect-borne or atmospheric pollen."),

    # 77: Phenotype vs Genotype Conceptual Difference
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Phenotype Box -->
  <rect x="25" y="25" width="165" height="140" rx="6" fill="#27272a" stroke="#4ade80" stroke-width="2"/>
  <text x="107" y="48" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">PHENOTYPE</text>
  <text x="107" y="70" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">Observable Physical Trait</text>
  <text x="107" y="95" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">"Tall Plant"</text>
  <text x="107" y="120" fill="#e2e8f0" font-size="8" font-family="sans-serif" text-anchor="middle">Visible to the naked eye</text>
  <text x="107" y="138" fill="#e2e8f0" font-size="8" font-family="sans-serif" text-anchor="middle">Both TT and Tt look identical!</text>
  <!-- Genotype Box -->
  <rect x="210" y="25" width="165" height="140" rx="6" fill="#27272a" stroke="#38bdf8" stroke-width="2"/>
  <text x="292" y="48" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">GENOTYPE</text>
  <text x="292" y="70" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">Underlying Genetic Alleles</text>
  <text x="292" y="95" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">TT (Pure) vs Tt (Hybrid)</text>
  <text x="292" y="120" fill="#e2e8f0" font-size="8" font-family="sans-serif" text-anchor="middle">Revealed by Test Cross</text>
  <text x="292" y="138" fill="#e2e8f0" font-size="8" font-family="sans-serif" text-anchor="middle">Molecular DNA composition</text>
</svg>
</div>
Why can two pea plants possess the exact same tall phenotype yet harbor different underlying genotypes?""""",
     ["Because the dominant allele (T) completely masks the presence of the recessive allele (t), making homozygous TT and heterozygous Tt phenotypically indistinguishable",
      "Because genotypes change every time the sun rises",
      "Because tall plants have no genes at all",
      "Because phenotype is determined entirely by soil fertilizer"],
     "A", "OSC", "easy",
     "Complete dominance dictates that a single dominant T allele provides sufficient gibberellin hormone biosynthesis to achieve full tall vine height, rendering TT and Tt phenotypically identical."),

    # 78: Back Cross vs Test Cross Relationship
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <!-- Big Outer Circle: Backcross -->
  <circle cx="200" cy="100" r="80" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="200" y="45" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">BACK CROSS</text>
  <text x="200" y="60" fill="#93c5fd" font-size="8" font-family="sans-serif" text-anchor="middle">(F1 crossed with ANY parent: TT or tt)</text>
  <!-- Inner Circle: Testcross -->
  <circle cx="200" cy="115" r="45" fill="#0f172a" stroke="#facc15" stroke-width="2"/>
  <text x="200" y="105" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">TEST CROSS</text>
  <text x="200" y="120" fill="#fef08a" font-size="8" font-family="sans-serif" text-anchor="middle">(Strictly with tt)</text>
  <text x="200" y="135" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">Reveals genotype!</text>
  <!-- Axiom -->
  <text x="200" y="175" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">"All test crosses are back crosses, but not all back crosses are test crosses"</text>
</svg>
</div>
What fundamental genetic distinction separates a test cross from a standard back cross?""""",
     ["A test cross is strictly a cross with the homozygous recessive parent (tt) to identify genotype, whereas a back cross can involve either the dominant (TT) or recessive (tt) parent",
      "A test cross is done with animals while back crosses are done with plants",
      "A test cross requires radiation while back cross uses sunlight",
      "A back cross produces only sterile plants"],
     "A", "OSC", "medium",
     "A back cross denotes any mating between an F1 progeny and either parental genotype; a test cross is the specific diagnostic subset mated to the homozygous recessive parent."),

    # 79: Monohybrid F2 Genotype Ratio (1:2:1 Pie Chart)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#111827"/>
  <!-- Pie representation / Bars -->
  <rect x="50" y="40" width="70" height="100" rx="4" fill="#2563eb" stroke="#60a5fa" stroke-width="2"/>
  <text x="85" y="85" fill="#ffffff" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">TT</text>
  <text x="85" y="105" fill="#bfdbfe" font-size="10" font-family="sans-serif" text-anchor="middle">25% (1/4)</text>
  <text x="85" y="160" fill="#60a5fa" font-size="9" font-family="sans-serif" text-anchor="middle">Pure Tall</text>

  <rect x="140" y="40" width="130" height="100" rx="4" fill="#0d9488" stroke="#2dd4bf" stroke-width="2"/>
  <text x="205" y="85" fill="#ffffff" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">Tt</text>
  <text x="205" y="105" fill="#ccfbf1" font-size="10" font-family="sans-serif" text-anchor="middle">50% (2/4)</text>
  <text x="205" y="160" fill="#2dd4bf" font-size="9" font-family="sans-serif" text-anchor="middle">Hybrid Tall</text>

  <rect x="290" y="40" width="70" height="100" rx="4" fill="#dc2626" stroke="#f87171" stroke-width="2"/>
  <text x="325" y="85" fill="#ffffff" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">tt</text>
  <text x="325" y="105" fill="#fecaca" font-size="10" font-family="sans-serif" text-anchor="middle">25% (1/4)</text>
  <text x="325" y="160" fill="#f87171" font-size="9" font-family="sans-serif" text-anchor="middle">Pure Dwarf</text>
  <!-- Header -->
  <text x="205" y="25" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Mendelian F2 Genotypic Frequency Breakdown</text>
</svg>
</div>
In an F2 monohybrid population of 1,200 pea plants, what exact numerical distribution corresponds to the 1:2:1 genotypic ratio?""""",
     ["300 TT : 600 Tt : 300 tt", "600 TT : 300 Tt : 300 tt", "400 TT : 400 Tt : 400 tt", "900 TT : 300 tt"],
     "A", "ONE", "easy",
     "Following the 1:2:1 ratio: $1/4 \\times 1,200 = 300$ homozygous TT; $1/2 \\times 1,200 = 600$ heterozygous Tt; and $1/4 \\times 1,200 = 300$ homozygous recessive tt."),

    # 80: Multiple Alleles & Codominance (Human ABO Blood Groups)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Table Header -->
  <text x="70" y="30" fill="#facc15" font-size="10" font-family="sans-serif" font-weight="bold">Genotype</text>
  <text x="180" y="30" fill="#38bdf8" font-size="10" font-family="sans-serif" font-weight="bold">Blood Group</text>
  <text x="300" y="30" fill="#4ade80" font-size="10" font-family="sans-serif" font-weight="bold">RBC Surface Antigens</text>
  <line x1="30" y1="38" x2="370" y2="38" stroke="#334155" stroke-width="1"/>
  <!-- IA IA or IA i -->
  <text x="70" y="60" fill="#cbd5e1" font-size="9" font-family="sans-serif">IA IA  or  IA i</text>
  <text x="180" y="60" fill="#38bdf8" font-size="9" font-family="sans-serif">Type A</text>
  <text x="300" y="60" fill="#cbd5e1" font-size="9" font-family="sans-serif">Antigen A only</text>
  <!-- IB IB or IB i -->
  <text x="70" y="90" fill="#cbd5e1" font-size="9" font-family="sans-serif">IB IB  or  IB i</text>
  <text x="180" y="90" fill="#38bdf8" font-size="9" font-family="sans-serif">Type B</text>
  <text x="300" y="90" fill="#cbd5e1" font-size="9" font-family="sans-serif">Antigen B only</text>
  <!-- IA IB (Codominant) -->
  <rect x="30" y="105" width="340" height="30" rx="4" fill="#831843" stroke="#f43f5e" stroke-width="1"/>
  <text x="70" y="125" fill="#facc15" font-size="10" font-family="sans-serif" font-weight="bold">IA IB</text>
  <text x="180" y="125" fill="#facc15" font-size="10" font-family="sans-serif" font-weight="bold">Type AB</text>
  <text x="300" y="125" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold">Both A and B Antigens (Codominance!)</text>
  <!-- ii -->
  <text x="70" y="160" fill="#cbd5e1" font-size="9" font-family="sans-serif">ii (Recessive)</text>
  <text x="180" y="160" fill="#38bdf8" font-size="9" font-family="sans-serif">Type O</text>
  <text x="300" y="160" fill="#cbd5e1" font-size="9" font-family="sans-serif">Neither antigen</text>
</svg>
</div>
How does human blood group inheritance in genotype IAIB demonstrate the non-Mendelian genetic principle of codominance?""""",
     ["Both alleles IA and IB express their respective surface glycoprotein transferases simultaneously and fully without blending or dominance",
      "Allele IA destroys allele IB inside the bone marrow",
      "Blood cells have no cell membrane in Type AB",
      "Type AB blood contains only pure water"],
     "A", "OSC", "easy",
     "Alleles IA and IB produce distinct functional enzymes (N-acetylgalactosaminyltransferase and galactosyltransferase); in heterozygotes, both antigens appear codominantly on RBC surfaces."),

    # 81: Parental Generation to F1 Generation Cross Schematic
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- P1 Parents -->
  <rect x="50" y="30" width="120" height="40" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="110" y="48" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Pure Tall (TT)</text>
  <text x="110" y="62" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Produces Gametes: T</text>

  <rect x="230" y="30" width="120" height="40" rx="5" fill="#1e293b" stroke="#f87171" stroke-width="2"/>
  <text x="290" y="48" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Pure Dwarf (tt)</text>
  <text x="290" y="62" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Produces Gametes: t</text>
  <!-- Syngamy Lines -->
  <line x1="110" y1="70" x2="170" y2="105" stroke="#facc15" stroke-width="2"/>
  <line x1="290" y1="70" x2="230" y2="105" stroke="#facc15" stroke-width="2"/>
  <!-- F1 Progeny Box -->
  <rect x="100" y="110" width="200" height="55" rx="6" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="200" y="130" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">F1 Generation: Genotype Tt</text>
  <text x="200" y="145" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">100% PHENOTYPICALLY TALL!</text>
  <text x="200" y="158" fill="#bbf7d0" font-size="8" font-family="sans-serif" text-anchor="middle">Recessive dwarf allele 't' completely masked</text>
</svg>
</div>
What core genetic conclusion did Mendel deduce from observing 100% tall plants in the F1 generation from a pure tall x pure dwarf parental cross?""""",
     ["The Law of Dominance: alternative alleles do not blend into intermediate heights, but the dominant trait completely masks the recessive factor in hybrids",
      "Dwarf plants can never reproduce under any conditions",
      "Tallness is caused by the greenhouse effect",
      "The dwarf gene was permanently deleted from the DNA"],
     "A", "OSC", "easy",
     "Mendel demonstrated particulate inheritance and dominance: the recessive dwarf factor remained intact and latent within the F1 hybrids, reappearing unblemished in F2."),

    # 82: F2 Phenotype Segregation Bar Representation
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Tall Bar (75%) -->
  <rect x="70" y="40" width="180" height="90" rx="5" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
  <text x="160" y="80" fill="#ffffff" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">TALL (75%)</text>
  <text x="160" y="100" fill="#bbf7d0" font-size="10" font-family="sans-serif" text-anchor="middle">3 / 4 of Progeny (1 TT + 2 Tt)</text>
  <!-- Dwarf Bar (25%) -->
  <rect x="270" y="40" width="60" height="90" rx="5" fill="#991b1b" stroke="#f87171" stroke-width="2"/>
  <text x="300" y="80" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">DWARF</text>
  <text x="300" y="100" fill="#fca5a5" font-size="9" font-family="sans-serif" text-anchor="middle">25% (1 tt)</text>
  <!-- Ratio -->
  <text x="200" y="160" fill="#facc15" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">F2 Phenotypic Ratio = 3 Tall : 1 Dwarf (3:1)</text>
</svg>
</div>
In Mendel's actual historical monohybrid cross on stem height, he harvested 1,064 F2 pea plants, of which 787 were tall and 277 were dwarf. What exact empirical ratio does this represent?""",
     ["2.84 : 1 (statistically approximating the theoretical 3:1 Mendelian expectation)",
      "Exactly 4 : 1",
      "Exactly 1 : 1",
      "9 : 3"],
     "A", "ONE", "medium",
     "Mendel's raw count of $787 / 277 = 2.84 : 1$, which chi-square statistical analysis confirms is a textbook empirical approximation of the theoretical 3:1 Mendelian ratio.")
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

output_path = os.path.join(os.path.dirname(__file__), "ch16_topic3.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
