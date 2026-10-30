# scripts/generate_ch16_topic4.py
# MH-9-SCIT-16-16.4: Mendel Dihybrid Cross (9:3:3:1 Ratio) & Law of Independent Assortment
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-16-16.4"

exam_data = [
    # 1-10: Dihybrid Cross Basics & F1 Generation
    ("What is a genetic breeding cross that simultaneously tracks the inheritance of TWO pairs of contrasting characters called?",
     ["Dihybrid cross", "Monohybrid cross", "Trihybrid cross", "Test cross"],
     "A", "OSC", "easy",
     "A dihybrid cross analyzes the simultaneous transmission and assortment of two independent pairs of contrasting alleles (e.g. seed shape and seed color)."),

    ("In Mendel's classic dihybrid cross, which two pairs of contrasting seed characters were hybridized?",
     ["Seed shape (Round vs Wrinkled) and Seed color (Yellow vs Green)",
      "Stem height (Tall vs Dwarf) and Flower color (Violet vs White)",
      "Pod color (Green vs Yellow) and Pod shape (Inflated vs Constricted)",
      "Root length and Leaf size"],
     "A", "OSC", "easy",
     "Mendel crossed a true-breeding plant having round yellow seeds with a true-breeding plant having wrinkled green seeds to discover the Law of Independent Assortment."),

    ("What are the genotypes of the pure-breeding parental plants (P1) in Mendel's classic dihybrid seed cross?",
     ["RRYY (Round Yellow) and rryy (Wrinkled Green)",
      "RrYy and RrYy",
      "RRyy and rrYY",
      "RRYy and rrYy"],
     "A", "OSC", "easy",
     "The homozygous dominant parent possesses genotype RRYY (producing RY gametes), and the homozygous recessive parent possesses rryy (producing ry gametes)."),

    ("What were the uniform genotype and phenotype observed in ALL F1 generation progeny from the RRYY x rryy parental cross?",
     ["Genotype RrYy ; Phenotype 100% Round Yellow seeds",
      "Genotype RRYY ; Phenotype 100% Wrinkled Green seeds",
      "Genotype Rryy ; Phenotype 50% Round Green",
      "Genotype rryy ; Phenotype 100% Yellow"],
     "A", "OSC", "easy",
     "All F1 offspring inherit dominant R and Y alleles alongside recessive r and y alleles, yielding dihybrid genotype RrYy with 100% Round Yellow phenotypes."),

    ("How many distinct types of gametes are produced by an F1 dihybrid pea plant with genotype RrYy?",
     ["4 types of gametes (RY, Ry, rY, ry in equal 25% proportions)",
      "2 types of gametes",
      "16 types of gametes",
      "8 types of gametes"],
     "A", "OSC", "easy",
     "By independent assortment, the two allele pairs segregate independently, producing four gametic classes ($2^2 = 4$): RY (25%), Ry (25%), rY (25%), and ry (25%)."),

    ("When the 4 types of male gametes fertilize the 4 types of female gametes in an F1 self-cross (RrYy x RrYy), how many total boxes/combinations exist in the F2 Punnett square?",
     ["16 combinations (4 x 4 = 16)", "4 combinations", "8 combinations", "64 combinations"],
     "A", "OSC", "easy",
     "Combining 4 distinct pollen genotypes with 4 distinct ovule genotypes generates a $4 \\times 4$ checkerboard containing 16 zygotic combinations."),

    ("What is the classic PHENOTYPIC ratio obtained in the F2 generation of a Mendelian dihybrid cross?",
     ["9 Round Yellow : 3 Round Green : 3 Wrinkled Yellow : 1 Wrinkled Green (9:3:3:1)",
      "9:7",
      "1:2:1:2:4:2:1:2:1",
      "1:1:1:1"],
     "A", "OSC", "easy",
     "The 16 F2 combinations segregate into 4 distinct phenotypic categories in the iconic 9:3:3:1 ratio."),

    ("In the F2 generation of Mendel's dihybrid cross, which two phenotypic classes represent the original PARENTAL combinations?",
     ["Round Yellow and Wrinkled Green (total 10/16)",
      "Round Green and Wrinkled Yellow",
      "Only Round Yellow",
      "Only Wrinkled Green"],
     "A", "OSC", "medium",
     "The parental phenotypes are Round Yellow (9/16) and Wrinkled Green (1/16), accounting for $10/16$ (62.5%) of the total F2 progeny."),

    ("Which two phenotypic classes in the F2 dihybrid generation represent entirely novel RECOMBINANT (non-parental) trait combinations?",
     ["Round Green (3/16) and Wrinkled Yellow (3/16)",
      "Round Yellow (9/16) and Wrinkled Green (1/16)",
      "Only Round Green",
      "Only Wrinkled Yellow"],
     "A", "OSC", "medium",
     "Recombinants shuffle contrasting parental traits into novel combinations: Round Green ($3/16$) and Wrinkled Yellow ($3/16$), totaling $6/16$ (37.5%)."),

    ("Mendel's Third Law, which states that alleles of two or more different genes assort independently of one another during gamete formation, is the:",
     ["Law of Independent Assortment", "Law of Segregation", "Law of Dominance", "Law of Gene Linkage"],
     "A", "OSC", "easy",
     "The Law of Independent Assortment establishes that maternal and paternal non-homologous chromosomes align independently at the metaphase I plate during meiosis."),

    # 11-20: Ratios, Genotypes & Probability
    ("How many distinct GENOTYPES are produced in the F2 generation of a Mendelian dihybrid cross (RrYy x RrYy)?",
     ["9 distinct genotypes", "16 genotypes", "4 genotypes", "6 genotypes"],
     "A", "OSC", "medium",
     "The 16 F2 offspring partition into 9 unique genotypes ($3^2 = 9$): RRYY, RRYy, RRyy, RrYY, RrYy, Rryy, rrYY, rrYy, and rryy."),

    ("What is the detailed genotypic ratio of the 9 genotypes in the F2 dihybrid generation?",
     ["1 : 2 : 1 : 2 : 4 : 2 : 1 : 2 : 1", "9 : 3 : 3 : 1", "3 : 1 : 3 : 1", "1 : 1 : 1 : 1"],
     "A", "OSC", "medium",
     "Expanding $(1:2:1) \\times (1:2:1)$ yields the 9-term genotypic ratio: 1 RRYY : 2 RRYy : 1 RRyy : 2 RrYY : 4 RrYy : 2 Rryy : 1 rrYY : 2 rrYy : 1 rryy."),

    ("What proportion of the total F2 dihybrid progeny is completely HOMOZYGOUS for both dominant alleles (genotype RRYY)?",
     ["1 / 16 (6.25%)", "4 / 16 (25%)", "9 / 16 (56.25%)", "2 / 16 (12.5%)"],
     "A", "ONE", "easy",
     "Genotype RRYY arises strictly when an RY sperm fertilizes an RY egg: $1/4 \\times 1/4 = 1/16$ (6.25%)."),

    ("What proportion of the total F2 dihybrid progeny has the completely HETEROZYGOUS genotype (RrYy), identical to the F1 hybrid?",
     ["4 / 16 (25%)", "1 / 16 (6.25%)", "2 / 16 (12.5%)", "8 / 16 (50%)"],
     "A", "ONE", "easy",
     "The double heterozygote RrYy occupies four diagonal boxes in the Punnett square, representing $4/16$ or 1/4 (25%)."),

    ("What proportion of the total F2 dihybrid progeny is completely homozygous recessive for both traits (genotype rryy)?",
     ["1 / 16 (6.25%)", "3 / 16 (18.75%)", "4 / 16 (25%)", "2 / 16 (12.5%)"],
     "A", "ONE", "easy",
     "Double homozygous recessive rryy occurs in only one out of 16 boxes ($1/4 \\times 1/4 = 1/16$), manifesting the double-recessive wrinkled green phenotype."),

    ("If an F1 dihybrid plant (RrYy) is crossed with a double homozygous recessive tester plant (rryy), this cross is a:",
     ["Dihybrid test cross", "Dihybrid back cross only", "Reciprocal cross", "Trihybrid cross"],
     "A", "OSC", "easy",
     "A dihybrid test cross mates a double heterozygote (RrYy) with a double homozygous recessive (rryy) to test the independent assortment of alleles."),

    ("What is the expected phenotypic and genotypic ratio among the offspring of a DIHYBRID TEST CROSS (RrYy x rryy)?",
     ["1 Round Yellow : 1 Round Green : 1 Wrinkled Yellow : 1 Wrinkled Green (1:1:1:1)",
      "9:3:3:1",
      "3:1",
      "1:2:1"],
     "A", "OSC", "easy",
     "Because the tester contributes only ry gametes, the 4 gametes from RrYy produce four equal phenotypic classes in a 1:1:1:1 ratio."),

    ("If 1,600 pea seeds are harvested in the F2 generation of a standard dihybrid cross, approximately how many seeds are expected to be WRINKLED GREEN?",
     ["100 seeds (1/16 of 1,600)", "300 seeds", "900 seeds", "400 seeds"],
     "A", "ONE", "easy",
     "Wrinkled green seeds account for $1/16$ of the progeny. Therefore, $1,600 \\times (1/16) = 100$ seeds."),

    ("In an F2 dihybrid population of 1,600 pea seeds, how many seeds are statistically expected to be ROUND GREEN?",
     ["300 seeds (3/16 of 1,600)", "100 seeds", "900 seeds", "600 seeds"],
     "A", "ONE", "easy",
     "Round green seeds represent a recombinant phenotype with frequency $3/16$. Therefore, $1,600 \\times (3/16) = 300$ seeds."),

    ("In an F2 dihybrid population of 1,600 pea seeds, how many seeds are statistically expected to be ROUND YELLOW?",
     ["900 seeds (9/16 of 1,600)", "300 seeds", "100 seeds", "1,200 seeds"],
     "A", "ONE", "easy",
     "Round yellow seeds represent the dominant parental phenotype with frequency $9/16$. Therefore, $1,600 \\times (9/16) = 900$ seeds."),

    # 21-30: Linkage, Exceptions & Advanced Assortment
    ("What major genetic phenomenon represents an EXCEPTION to Mendel's Law of Independent Assortment?",
     ["Gene Linkage (genes located physically close together on the same chromosome)",
      "Dominance",
      "Independent segregation",
      "Mutation"],
     "A", "OSC", "easy",
     "Genes residing in close proximity on the same chromosome do not assort independently because they tend to be inherited together as a linked unit during meiosis."),

    ("Who discovered the chromosomal basis of gene linkage and genetic recombination using the fruit fly (Drosophila melanogaster)?",
     ["Thomas Hunt Morgan", "Gregor Mendel", "James Watson", "Francis Crick"],
     "A", "OSC", "medium",
     "Thomas Hunt Morgan provided definitive cytological evidence for gene linkage and crossing-over in Drosophila, winning the 1933 Nobel Prize in Physiology or Medicine."),

    ("Why did Mendel NOT observe gene linkage in his 7 pea traits, even though garden peas have only 7 pairs of chromosomes?",
     ["The genes for the 7 characters Mendel chose are located on separate chromosomes or are situated far enough apart on the same chromosome to assort independently",
      "Pea plants have no chromosomes",
      "Pea plant chromosomes never undergo meiosis",
      "Mendel discarded all linked plants"],
     "A", "OSC", "medium",
     "Mendel's 7 characters reside on chromosomes 1, 4, 5, and 7; traits on the same chromosome (like chromosome 4) are separated by large physical distances (>50 cM), assorting independently."),

    ("In a cross between two individuals with genotypes AaBb x aabb, the offspring appear in the ratio 45% AB, 45% ab, 5% Ab, and 5% aB. This result indicates:",
     ["Genes A and B are linked on the same chromosome with 10% crossing-over frequency",
      "Genes A and B obey standard independent assortment",
      "Genes A and B are lethal",
      "Both genes are located on the Y chromosome"],
     "A", "OSC", "hard",
     "Parental combinations (AB and ab) comprise 90% while recombinants (Ab and aB) comprise only 10%, deviating from the 1:1:1:1 test cross ratio and confirming linkage."),

    ("How many different types of gametes can be produced by an individual heterozygous for THREE independently assorting genes (genotype AaBbCc)?",
     ["8 types of gametes (2^3 = 8)", "6 types", "4 types", "16 types"],
     "A", "ONE", "medium",
     "The number of unique gametic types produced by a polyhybrid is given by $2^n$, where $n$ is the number of heterozygous gene pairs. For a trihybrid: $2^3 = 8$ gametes."),

    ("If you self-pollinate a trihybrid plant (AaBbCc x AaBbCc), how many total boxes will be present in the resulting Punnett square?",
     ["64 boxes (8 x 8 = 64)", "16 boxes", "32 boxes", "128 boxes"],
     "A", "ONE", "medium",
     "Since both parents produce 8 types of gametes, combining them yields an $8 \\times 8 = 64$ box Punnett square."),

    ("State whether True or False: Mendel's Law of Independent Assortment applies strictly to genes that are situated on different non-homologous chromosomes.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Independent assortment requires genes to reside on different chromosomes or be separated by recombinant crossing-over distances greater than 50 map units."),

    ("What is the probability of obtaining an offspring with genotype AABB from a cross between AaBb x AaBb?",
     ["1 / 16", "1 / 4", "1 / 8", "9 / 16"],
     "A", "OSC", "easy",
     "Using the product rule of independent probabilities: $P(AA) = 1/4$ and $P(BB) = 1/4$. Therefore, $P(AABB) = 1/4 \\times 1/4 = 1/16$."),

    ("In a dihybrid cross between RrYy x RrYy, what is the probability that an offspring will display at least ONE dominant trait?",
     ["15 / 16", "9 / 16", "1 / 16", "3 / 16"],
     "A", "OSC", "medium",
     "The only phenotypic class lacking any dominant trait is double-recessive wrinkled green (1/16). Thus, $1 - 1/16 = 15/16$ (93.75%) exhibit at least one dominant trait."),

    ("What mathematical rule states that the probability of two independent events occurring together is the product of their individual probabilities?",
     ["Multiplication rule (Product rule of probability)", "Addition rule", "Law of segregation", "Binomial theorem"],
     "A", "OSC", "medium",
     "The product rule states that for independent events A and B, the joint probability is $P(A \\cap B) = P(A) \\times P(B)$, underlying Mendelian dihybrid ratios.")
]

# 10 more questions to make exam_data exactly 40
exam_data.extend([
    # 31-40: Fill in blanks, Numerical, Multi-choice
    ("The classic Mendelian dihybrid phenotypic ratio in the F2 generation is 9 : 3 : 3 : ________.",
     ["1", "3", "2", "4"],
     "A", "ONE", "easy",
     "The canonical dihybrid phenotypic ratio is 9 dominant-dominant : 3 dominant-recessive : 3 recessive-dominant : 1 double-recessive."),

    ("In a dihybrid cross (RrYy x RrYy), the total number of RECOMBINANT (non-parental) offspring out of 16 is ________.",
     ["6 (3 Round Green + 3 Wrinkled Yellow)", "10", "1", "9"],
     "A", "ONE", "easy",
     "Recombinant phenotypes comprise Round Green (3/16) and Wrinkled Yellow (3/16), summing to exactly $3 + 3 = 6$ out of 16 progeny."),

    ("A dihybrid test cross between an individual of genotype RrYy and a tester of genotype rryy yields a phenotypic ratio of ________.",
     ["1 : 1 : 1 : 1", "9 : 3 : 3 : 1", "3 : 1", "1 : 2 : 1"],
     "A", "OFB", "easy",
     "The dihybrid test cross produces four phenotypically distinct classes in equal 1:1:1:1 proportions."),

    ("State whether True or False: Mendel's Law of Independent Assortment holds true for two genes situated immediately adjacent to each other on the same chromosome.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Tightly linked adjacent genes co-segregate together during meiosis without independent assortment unless crossing-over physically intervenes."),

    ("Which of the following genotype combinations represent TRUE-BREEDING homozygous individuals in an F2 dihybrid cross? (Select all that apply)",
     ["RRYY, RRyy, rrYY, and rryy",
      "Only RrYy",
      "Only RrYY and RRYy",
      "All F2 plants are true-breeding"],
     "A", "OMC", "easy",
     "True-breeding organisms must be homozygous at both loci; the four homozygous dihybrid genotypes are RRYY, RRyy, rrYY, and rryy."),

    ("Assertion (A): The F2 dihybrid phenotypic ratio 9:3:3:1 is a mathematical expansion of two independent 3:1 monohybrid ratios.\nReason (R): The two gene pairs controlling seed shape and seed color assort independently during gamete formation.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is not the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "easy",
     "Multiplying two independent monohybrid ratios $(3:1) \\times (3:1) = 9:3:3:1$ demonstrates that the two gene pairs segregate independently."),

    ("How many different PHENOTYPIC classes are observed in the F2 generation of a trihybrid cross (AaBbCc x AaBbCc) assuming complete dominance?",
     ["8 phenotypic classes (2^3 = 8)", "27 phenotypic classes", "64 phenotypic classes", "16 phenotypic classes"],
     "A", "ONE", "medium",
     "With complete dominance, each gene pair yields 2 phenotypic classes; for 3 independently assorting pairs, the total number of phenotypic classes is $2^3 = 8$."),

    ("How many different GENOTYPIC classes are produced in the F2 generation of a trihybrid cross?",
     ["27 genotypic classes (3^3 = 27)", "64 genotypic classes", "8 genotypic classes", "9 genotypic classes"],
     "A", "ONE", "medium",
     "Each monohybrid gene pair yields 3 genotypes (1:2:1); for 3 independently assorting pairs, the total number of genotypic classes is $3^3 = 27$."),

    ("What is the physical chromosomal basis of Mendel's Law of Independent Assortment?",
     ["Random independent alignment and orientation of non-homologous chromosome bivalents at the equatorial plate during Metaphase I of meiosis",
      "Centromere division during mitotic anaphase",
      "Replication of DNA in S phase",
      "Dissolution of the cell wall during cytokinesis"],
     "A", "OSC", "hard",
     "The random 50:50 orientation of paternal versus maternal kinetochores across non-homologous bivalents on the metaphase I plate physically enacts independent assortment."),

    ("What is the frequency of the double heterozygous genotype RrYy among the F2 progeny of a dihybrid cross?",
     ["4 / 16 (25%)", "1 / 16 (6.25%)", "2 / 16 (12.5%)", "9 / 16 (56.25%)"],
     "A", "OSC", "easy",
     "The double heterozygous genotype RrYy occurs in four diagonal cells of the 16-cell Punnett square, representing $4/16$ or 25%.")
])

practice_data = [
    # 41-50: Dihybrid Calculations & Advanced Pedigree Crosses
    ("A plant with genotype RrYy is self-pollinated. What fraction of the F2 offspring will have ROUND seeds regardless of seed color?",
     ["3 / 4 (75% or 12/16)", "9 / 16", "1 / 4", "1 / 2"],
     "A", "OSC", "easy",
     "Looking at seed shape independently, Rr x Rr yields $3/4$ round seeds (1 RRYY + 2 RRYy + 1 RRyy + 2 RrYY + 4 RrYy + 2 Rryy = 12/16 = 3/4)."),

    ("A plant with genotype RrYy is self-pollinated. What fraction of the F2 offspring will have GREEN seeds regardless of seed shape?",
     ["1 / 4 (25% or 4/16)", "3 / 16", "1 / 16", "9 / 16"],
     "A", "OSC", "easy",
     "Looking at seed color independently, Yy x Yy yields $1/4$ green seeds (3/16 Round Green + 1/16 Wrinkled Green = 4/16 = 1/4)."),

    ("In a cross between AaBb x Aabb, what proportion of the progeny is expected to be homozygous recessive for BOTH genes (aabb)?",
     ["1 / 8 (12.5%)", "1 / 16 (6.25%)", "1 / 4 (25%)", "1 / 2 (50%)"],
     "A", "ONE", "medium",
     "From Aa x Aa, $P(aa) = 1/4$. From Bb x bb, $P(bb) = 1/2$. By the product rule, $P(aabb) = 1/4 \\times 1/2 = 1/8$."),

    ("In fruit flies (Drosophila), gray body (B) is dominant over black body (b), and long wings (V) are dominant over vestigial wings (v). In a dihybrid test cross (BbVv x bbvv), 1,000 flies were counted: 410 gray long, 410 black vestigial, 90 gray vestigial, and 90 black long. What is the recombination frequency?",
     ["18% (180 / 1000 x 100)", "9%", "50%", "25%"],
     "A", "ONE", "hard",
     "Recombinant flies are gray vestigial (90) and black long (90), totaling $90 + 90 = 180$. Recombination frequency $= (180 / 1,000) \\times 100 = 18\\%$ (18 map units or centimorgans)."),

    ("What does a recombination frequency of exactly 50% between two genes indicate in genetic mapping?",
     ["The two genes are assorting independently (located either on separate chromosomes or very far apart on the same chromosome)",
      "The genes are tightly linked right next to each other",
      "Both genes are completely deleted",
      "The organism is triploid"],
     "A", "OSC", "hard",
     "A 50% recombination frequency represents the upper limit of crossing over, matching the expected 1:1:1:1 test cross ratio of unlinked genes."),

    ("If you self-fertilize a pea plant with genotype RrYY, what phenotypic ratio will you observe among its offspring?",
     ["3 Round Yellow : 1 Wrinkled Yellow", "9 Round Yellow : 3 Wrinkled Green", "1 Round Yellow : 1 Wrinkled Yellow", "All Round Yellow"],
     "A", "OSC", "medium",
     "Since the plant is homozygous YY, all offspring inherit Y and will be Yellow. The Rr alleles segregate as 3 Round : 1 Wrinkled, yielding 3 Round Yellow : 1 Wrinkled Yellow."),

    ("If a pea plant with genotype RRYy is crossed with a plant of genotype rrYy, what proportion of the offspring will have WRINKLED seeds?",
     ["0% (No wrinkled seeds)", "25%", "50%", "75%"],
     "A", "ONE", "easy",
     "Cross RR x rr yields 100% Rr (all round seeds). Therefore, 0% of the offspring will have wrinkled seeds."),

    ("State whether True or False: In a dihybrid cross where both parents are heterozygous (AaBb x AaBb), the probability that an offspring will have the genotype AaBb is 1/4 (25%).",
     ["True", "False"],
     "A", "OTF", "easy",
     "$P(Aa) = 1/2$ and $P(Bb) = 1/2$. Product $= 1/2 \\times 1/2 = 1/4$ or 4/16 (25%)."),

    ("What is the map distance unit used in genetic linkage mapping, named in honor of Thomas Hunt Morgan?",
     ["Centimorgan (cM)", "Nanometer", "Angstrom", "Base pair"],
     "A", "OSC", "medium",
     "One centimorgan (cM) or map unit (m.u.) represents a 1% frequency of meiotic recombination between two linked gene loci."),

    ("Who constructed the very first genetic linkage map of a chromosome in 1913 while working as an undergraduate student in Morgan's laboratory?",
     ["Alfred Sturtevant", "Gregor Mendel", "Francis Crick", "Reginald Punnett"],
     "A", "OSC", "hard",
     "Alfred H. Sturtevant realized that recombination frequencies are proportional to the physical distance between genes along a chromosome, constructing the first genetic map in 1913.")
]

# Additional 20 practice questions to reach exactly 30 questions
practice_data.extend([
    # 51-60: Further Dihybrid Concepts
    ("In a dihybrid cross (RrYy x RrYy), what fraction of the total progeny will be TRUE-BREEDING for both traits?",
     ["4 / 16 (1/4 or 25%)", "1 / 16", "9 / 16", "2 / 16"],
     "A", "OSC", "medium",
     "The four homozygous true-breeding genotypes (RRYY, RRyy, rrYY, rryy) each occur with frequency $1/16$, summing to $4/16$ or $25\\%$."),

    ("How many different types of gametes can an individual with genotype AABbCc produce?",
     ["4 types of gametes (2^2 = 4)", "8 types", "2 types", "16 types"],
     "A", "ONE", "medium",
     "Gene A is homozygous (1 type: A), while genes B and C are heterozygous (2 types each). Total gametic types $= 1 \\times 2 \\times 2 = 4$."),

    ("What is the probability of obtaining an offspring with the dominant phenotype for BOTH traits from a test cross (RrYy x rryy)?",
     ["1 / 4 (25%)", "9 / 16", "1 / 2", "1 / 16"],
     "A", "ONE", "easy",
     "A test cross produces 4 phenotypes in 1:1:1:1 proportions: Round Yellow is $1/4$ or 25%."),

    ("State whether True or False: Two genes located on different non-homologous chromosomes will ALWAYS assort independently.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Genes on separate chromosomes segregate with 100% independence due to random bivalent alignment at Metaphase I of meiosis."),

    ("If an organism of genotype AaBb is test-crossed and produces offspring in the ratio 1 AaBb : 1 Aabb : 1 aaBb : 1 aabb, what does this prove?",
     ["Genes A and B are located on different chromosomes and assort independently",
      "Genes A and B are tightly linked",
      "Gene A is lethal",
      "Gene B has mutated"],
     "A", "OSC", "medium",
     "An equal 1:1:1:1 test cross ratio is the empirical signature proving that the two genes assort independently during meiosis."),

    ("In tomatoes, red fruit (R) is dominant over yellow fruit (r), and tall vine (T) is dominant over dwarf vine (t). If a dihybrid plant (RrTt) is selfed, what fraction of offspring will be DWARF with RED fruit?",
     ["3 / 16", "9 / 16", "1 / 16", "1 / 4"],
     "A", "OSC", "easy",
     "Following the 9:3:3:1 ratio: Red Tall is 9/16, Red Dwarf is 3/16, Yellow Tall is 3/16, and Yellow Dwarf is 1/16."),

    ("What is the phenotypic ratio of offspring from a cross between AaBb x AABB?",
     ["100% displaying both dominant traits", "9:3:3:1", "1:1:1:1", "3:1"],
     "A", "OSC", "easy",
     "Since the second parent contributes dominant alleles A and B to every gamete, all 100% of the progeny inherit at least one dominant A and one dominant B."),

    ("Which mathematical formula predicts the number of distinct genotypes in the F2 generation of a polyhybrid cross involving 'n' heterozygous gene pairs?",
     ["3^n genotypes", "2^n genotypes", "4^n genotypes", "n^2 genotypes"],
     "A", "OSC", "medium",
     "Each heterozygous gene pair generates 3 genotypes (1:2:1); for $n$ independently assorting gene pairs, the total number of genotypes is $3^n$ (e.g. $3^2 = 9$ for a dihybrid)."),

    ("Which mathematical formula predicts the number of distinct PHENOTYPIC classes in the F2 generation of a polyhybrid cross assuming complete dominance?",
     ["2^n phenotypes", "3^n phenotypes", "4^n phenotypes", "n^3 phenotypes"],
     "A", "OSC", "medium",
     "With complete dominance, each gene pair produces 2 phenotypic classes; for $n$ gene pairs, the total number of phenotypes is $2^n$ (e.g. $2^2 = 4$ for a dihybrid)."),

    ("State whether True or False: Crossing over between homologous chromosomes occurs during Pachytene of Prophase I in meiosis.",
     ["True", "False"],
     "A", "OTF", "medium",
     "Recombination nodules mediate reciprocal genetic exchange (crossing over) between non-sister chromatids during the pachytene stage of meiotic prophase I.")
])

# 10 more questions to complete practice_data to 30
practice_data.extend([
    # 61-70: High-Yield Practice Questions
    ("In a dihybrid cross between RrYy x RrYy, how many distinct genotypes code for the ROUND YELLOW phenotype?",
     ["4 distinct genotypes (RRYY, RRYy, RrYY, RrYy)", "1 genotype", "9 genotypes", "2 genotypes"],
     "A", "ONE", "medium",
     "Any genotype containing at least one R and one Y manifests the Round Yellow phenotype: RRYY (1), RRYy (2), RrYY (2), and RrYy (4), totaling 4 genotypes (9/16)."),

    ("How many genotypes code for the WRINKLED GREEN phenotype in an F2 dihybrid cross?",
     ["Exactly 1 genotype (rryy)", "2 genotypes", "3 genotypes", "4 genotypes"],
     "A", "ONE", "easy",
     "The double-recessive phenotype requires complete homozygosity at both loci; only genotype rryy expresses wrinkled green seeds."),

    ("How many genotypes code for the ROUND GREEN phenotype in an F2 dihybrid cross?",
     ["2 genotypes (RRyy and Rryy)", "1 genotype", "3 genotypes", "4 genotypes"],
     "A", "ONE", "medium",
     "Round green requires at least one dominant R and homozygous recessive yy: RRyy (1/16) and Rryy (2/16), summing to 3/16 across 2 genotypes."),

    ("How many genotypes code for the WRINKLED YELLOW phenotype in an F2 dihybrid cross?",
     ["2 genotypes (rrYY and rrYy)", "1 genotype", "3 genotypes", "4 genotypes"],
     "A", "ONE", "medium",
     "Wrinkled yellow requires homozygous recessive rr and at least one dominant Y: rrYY (1/16) and rrYy (2/16), summing to 3/16 across 2 genotypes."),

    ("If two genes assort independently, what is the probability that an F2 individual will be homozygous at both loci?",
     ["4 / 16 (1/4 or 25%)", "1 / 16", "2 / 16", "9 / 16"],
     "A", "OSC", "medium",
     "The double-homozygous genotypes are RRYY, RRyy, rrYY, and rryy ($1/16$ each), summing to $4/16$ or $25\\%$."),

    ("What is the ratio of parental phenotypes to recombinant phenotypes in the F2 generation of a Mendelian dihybrid cross?",
     ["10 Parental : 6 Recombinant (or 5 : 3)", "9 : 7", "1 : 1", "12 : 4"],
     "A", "OSC", "medium",
     "Parental phenotypes are Round Yellow (9) + Wrinkled Green (1) = 10. Recombinants are Round Green (3) + Wrinkled Yellow (3) = 6. Ratio $= 10 : 6$ or $5 : 3$."),

    ("State whether True or False: Mendel's experiments on dihybrid inheritance provided the first quantitative proof of genetic recombination in living organisms.",
     ["True", "False"],
     "A", "OTF", "easy",
     "The generation of novel recombinant phenotypes (Round Green and Wrinkled Yellow) demonstrated that individual traits separate and recombine freely in progeny."),

    ("If an F1 dihybrid plant (RrYy) is selfed and yields 3,200 seeds, how many seeds are statistically expected to be RECOMBINANT?",
     ["1,200 seeds (6/16 of 3,200)", "600 seeds", "1,800 seeds", "200 seeds"],
     "A", "ONE", "easy",
     "Recombinant seeds comprise $6/16$ of the total progeny. Therefore, $3,200 \\times (6/16) = 1,200$ seeds."),

    ("Which term describes the physical cross-shaped connections formed between non-sister chromatids where crossing over occurs during diplotene of meiosis?",
     ["Chiasmata (singular: chiasma)", "Centromeres", "Kinetochores", "Telomeres"],
     "A", "OSC", "medium",
     "Chiasmata are the cytological manifestations of crossing-over, visible as X-shaped points of contact where non-sister chromatids undergo reciprocal breakage and reunion."),

    ("State whether True or False: The physical distance between two genes on a chromosome is directly proportional to their probability of recombination.",
     ["True", "False"],
     "A", "OTF", "easy",
     "The greater the physical distance separating two gene loci on a chromosome, the greater the statistical likelihood that a crossing-over event will occur between them.")
])

mock_data = [
    # 71: Dihybrid 16-Box Punnett Square Architecture
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="210" viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="210" rx="8" fill="#090d16"/>
  <!-- Punnett Grid 4x4 -->
  <!-- Gamete Headers -->
  <text x="70" y="30" fill="#facc15" font-size="9" font-family="sans-serif">RY</text>
  <text x="120" y="30" fill="#facc15" font-size="9" font-family="sans-serif">Ry</text>
  <text x="170" y="30" fill="#facc15" font-size="9" font-family="sans-serif">rY</text>
  <text x="220" y="30" fill="#facc15" font-size="9" font-family="sans-serif">ry</text>
  <text x="35" y="60" fill="#facc15" font-size="9" font-family="sans-serif">RY</text>
  <text x="35" y="95" fill="#facc15" font-size="9" font-family="sans-serif">Ry</text>
  <text x="35" y="130" fill="#facc15" font-size="9" font-family="sans-serif">rY</text>
  <text x="35" y="165" fill="#facc15" font-size="9" font-family="sans-serif">ry</text>
  <!-- 4x4 Blocks Summary Representation -->
  <rect x="55" y="40" width="190" height="135" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="150" y="90" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">16 Zygotic Boxes</text>
  <text x="150" y="110" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle">4 Gamete Types x 4 Gamete Types</text>
  <text x="150" y="130" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">9 Unique Genotypes Generated</text>
  <!-- Right Outcome Panel -->
  <rect x="260" y="35" width="125" height="145" rx="6" fill="#18181b" stroke="#facc15" stroke-width="1"/>
  <text x="322" y="55" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">F2 Phenotypic Ratio:</text>
  <text x="322" y="78" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle">9 Round Yellow</text>
  <text x="322" y="98" fill="#22c55e" font-size="9" font-family="sans-serif" text-anchor="middle">3 Round Green</text>
  <text x="322" y="118" fill="#eab308" font-size="9" font-family="sans-serif" text-anchor="middle">3 Wrinkled Yellow</text>
  <text x="322" y="138" fill="#ef4444" font-size="9" font-family="sans-serif" text-anchor="middle">1 Wrinkled Green</text>
  <text x="322" y="162" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">9 : 3 : 3 : 1</text>
</svg>
</div>
In the standard 16-box F2 dihybrid Punnett square above, how many boxes represent offspring displaying at least ONE dominant trait?""",
     ["15 boxes (15/16 or 93.75%)", "9 boxes", "16 boxes", "12 boxes"],
     "A", "OSC", "easy",
     "Out of 16 boxes, only the single double-recessive homozygous box (rryy) lacks a dominant trait; the remaining $16 - 1 = 15$ boxes ($9 + 3 + 3 = 15$) display at least one dominant trait."),

    # 72: Parental vs Recombinant Phenotypes in Dihybrid Cross
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Parental Box (10/16) -->
  <rect x="25" y="30" width="165" height="140" rx="6" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="107" y="55" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">PARENTAL PHENOTYPES</text>
  <text x="107" y="80" fill="#ffffff" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">10 / 16 (62.5%)</text>
  <text x="107" y="105" fill="#bbf7d0" font-size="9" font-family="sans-serif" text-anchor="middle">Round Yellow (9/16)</text>
  <text x="107" y="125" fill="#bbf7d0" font-size="9" font-family="sans-serif" text-anchor="middle">Wrinkled Green (1/16)</text>
  <text x="107" y="152" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle">Original P1 Combinations</text>
  <!-- Recombinant Box (6/16) -->
  <rect x="210" y="30" width="165" height="140" rx="6" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
  <text x="292" y="55" fill="#f59e0b" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">RECOMBINANT PHENOTYPES</text>
  <text x="292" y="80" fill="#ffffff" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">6 / 16 (37.5%)</text>
  <text x="292" y="105" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle">Round Green (3/16)</text>
  <text x="292" y="125" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle">Wrinkled Yellow (3/16)</text>
  <text x="292" y="152" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle">Novel Recombined Traits!</text>
</svg>
</div>
What evolutionary significance is highlighted by the appearance of 6/16 recombinant phenotypes in Mendel's dihybrid cross?""",
     ["Independent assortment generates new trait combinations not present in either original parent, driving phenotypic variation in nature",
      "Recombinant seeds are poisonous and cannot germinate",
      "Recombinant plants prove that genes mutate constantly",
      "It proves that pea plants can turn into animals"],
     "A", "OSC", "medium",
     "Recombinant phenotypes (Round Green and Wrinkled Yellow) demonstrated that individual traits behave as autonomous units that shuffle freely, fueling genetic diversity for natural selection."),

    # 73: Dihybrid Test Cross Matrix (RrYy x rryy)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#0f172a"/>
  <!-- Dihybrid Test Cross Header -->
  <rect x="30" y="20" width="340" height="30" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="200" y="40" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">DIHYBRID TEST CROSS: RrYy x rryy</text>
  <!-- 4 Outcome Boxes -->
  <rect x="25" y="70" width="75" height="85" rx="5" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="62" y="95" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">RrYy</text>
  <text x="62" y="115" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Round Yellow</text>
  <text x="62" y="140" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">25% (1)</text>

  <rect x="115" y="70" width="75" height="85" rx="5" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
  <text x="152" y="95" fill="#60a5fa" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Rryy</text>
  <text x="152" y="115" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Round Green</text>
  <text x="152" y="140" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">25% (1)</text>

  <rect x="205" y="70" width="75" height="85" rx="5" fill="#854d0e" stroke="#facc15" stroke-width="2"/>
  <text x="242" y="95" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">rrYy</text>
  <text x="242" y="115" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Wrinkled Yellow</text>
  <text x="242" y="140" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">25% (1)</text>

  <rect x="295" y="70" width="75" height="85" rx="5" fill="#7f1d1d" stroke="#f87171" stroke-width="2"/>
  <text x="332" y="95" fill="#f87171" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">rryy</text>
  <text x="332" y="115" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Wrinkled Green</text>
  <text x="332" y="140" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">25% (1)</text>
  <!-- Summary -->
  <text x="200" y="180" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Test Cross Phenotypic Ratio = 1 : 1 : 1 : 1</text>
</svg>
</div>
Why does a dihybrid test cross result in an exact 1:1:1:1 phenotypic ratio only if the two genes are unlinked?""",
     ["Because unlinked genes produce four types of gametes (RY, Ry, rY, ry) in strictly equal 25% frequencies, and the tester provides only recessive ry alleles",
      "Because the tester parent destroys all dominant alleles",
      "Because test cross seeds never grow tall vines",
      "Because peas only have 4 chromosomes"],
     "A", "OSC", "easy",
     "The double homozygous recessive parent contributes solely non-masking recessive ry gametes; thus, the progeny phenotypes directly map the 1:1:1:1 gametic output of the heterozygous parent."),

    # 74: Meiotic Basis of Independent Assortment (Metaphase I Alignment)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#111827"/>
  <!-- Possibility 1 -->
  <rect x="25" y="25" width="165" height="150" rx="6" fill="#1f2937" stroke="#38bdf8" stroke-width="2"/>
  <text x="107" y="48" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Arrangement 1 (50%)</text>
  <rect x="80" y="65" width="12" height="35" rx="3" fill="#38bdf8"/>
  <text x="86" y="85" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">R</text>
  <rect x="120" y="65" width="12" height="35" rx="3" fill="#facc15"/>
  <text x="126" y="85" fill="#000000" font-size="9" font-family="sans-serif" text-anchor="middle">Y</text>
  <line x1="50" y1="115" x2="165" y2="115" stroke="#475569" stroke-width="1"/>
  <text x="107" y="140" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle">Yields Gametes:</text>
  <text x="107" y="160" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">RY and ry</text>
  <!-- Possibility 2 -->
  <rect x="210" y="25" width="165" height="150" rx="6" fill="#1f2937" stroke="#ec4899" stroke-width="2"/>
  <text x="292" y="48" fill="#ec4899" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Arrangement 2 (50%)</text>
  <rect x="265" y="65" width="12" height="35" rx="3" fill="#38bdf8"/>
  <text x="271" y="85" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">R</text>
  <rect x="305" y="65" width="12" height="35" rx="3" fill="#22c55e"/>
  <text x="311" y="85" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">y</text>
  <line x1="235" y1="115" x2="350" y2="115" stroke="#475569" stroke-width="1"/>
  <text x="292" y="140" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle">Yields Gametes:</text>
  <text x="292" y="160" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Ry and rY</text>
</svg>
</div>
What physical mechanism during Metaphase I of meiosis generates the four types of gametes (RY, Ry, rY, ry) in strictly equal proportions?""",
     ["Random and independent alignment of maternal versus paternal homologous chromosome pairs across the metaphase equatorial plate",
      "DNA replication occurring 4 times in a row",
      "Spindle fibers tearing chromosomes into small pieces",
      "Mutations caused by ultraviolet radiation"],
     "A", "OSC", "hard",
     "The orientation of one bivalent (e.g. chromosome carrying R/r) on the equatorial spindle is completely independent of other bivalents (e.g. chromosome carrying Y/y), yielding equal 50:50 chances for each alignment."),

    # 75: Exception to Independent Assortment: Gene Linkage
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Unlinked Genes Box -->
  <rect x="25" y="25" width="165" height="140" rx="6" fill="#27272a" stroke="#38bdf8" stroke-width="2"/>
  <text x="107" y="48" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">UNLINKED GENES</text>
  <line x1="80" y1="65" x2="80" y2="105" stroke="#38bdf8" stroke-width="4"/>
  <text x="80" y="88" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">A</text>
  <line x1="130" y1="65" x2="130" y2="105" stroke="#facc15" stroke-width="4"/>
  <text x="130" y="88" fill="#000000" font-size="9" font-family="sans-serif" text-anchor="middle">B</text>
  <text x="107" y="130" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">On separate chromosomes</text>
  <text x="107" y="150" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Assort Independently (9:3:3:1)</text>
  <!-- Linked Genes Box -->
  <rect x="210" y="25" width="165" height="140" rx="6" fill="#27272a" stroke="#ef4444" stroke-width="2"/>
  <text x="292" y="48" fill="#ef4444" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">LINKED GENES</text>
  <line x1="292" y1="65" x2="292" y2="115" stroke="#ec4899" stroke-width="5"/>
  <text x="315" y="80" fill="#38bdf8" font-size="9" font-family="sans-serif">A</text>
  <text x="315" y="105" fill="#facc15" font-size="9" font-family="sans-serif">B</text>
  <text x="292" y="135" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">On SAME chromosome!</text>
  <text x="292" y="152" fill="#ef4444" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Violates Independent Assortment!</text>
</svg>
</div>
Why do two genes situated adjacent to each other on the same physical chromosome violate Mendel's Law of Independent Assortment?""",
     ["They physically travel together on the same DNA molecule during cell division unless separated by meiotic crossing-over",
      "They destroy the mitotic spindle",
      "They change into RNA nucleotides",
      "They can only express in female organisms"],
     "A", "OSC", "easy",
     "Linked genes reside on the same contiguous double-stranded DNA thread and segregate together into the same gamete as a physical linkage group unless separated by a crossover event."),

    # 76: Multiplication Rule of Independent Events
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Math Box -->
  <rect x="35" y="25" width="330" height="140" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="200" y="50" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">The Product Rule of Probability</text>
  <text x="200" y="80" fill="#facc15" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">(3 Round : 1 Wrinkled) x (3 Yellow : 1 Green)</text>
  <line x1="60" y1="95" x2="340" y2="95" stroke="#475569" stroke-width="1"/>
  <!-- Multiplied Terms -->
  <text x="80" y="120" fill="#4ade80" font-size="10" font-family="sans-serif">3/4 x 3/4 = 9/16 Round Yellow</text>
  <text x="80" y="145" fill="#facc15" font-size="10" font-family="sans-serif">3/4 x 1/4 = 3/16 Round Green</text>
  <text x="230" y="120" fill="#facc15" font-size="10" font-family="sans-serif">1/4 x 3/4 = 3/16 Wrinkled Yellow</text>
  <text x="230" y="145" fill="#ef4444" font-size="10" font-family="sans-serif">1/4 x 1/4 = 1/16 Wrinkled Green</text>
</svg>
</div>
How does the Product Rule of probability mathematically derive the 9:3:3:1 dihybrid ratio from two independent monohybrid crosses?""",
     ["By multiplying the two independent 3:1 phenotypic monohybrid segregation ratios: (3/4 + 1/4) x (3/4 + 1/4) = 9/16 + 3/16 + 3/16 + 1/16",
      "By adding the chromosome counts together",
      "By subtracting recessive alleles from dominant alleles",
      "By dividing seed weight by root length"],
     "A", "OSC", "medium",
     "Because seed shape and seed color segregate independently, the probability of any dual phenotype is the algebraic product of their individual monohybrid probabilities: $(3:1) \\times (3:1) = 9:3:3:1$."),

    # 77: The 9 Distinct Genotypes in F2 Generation
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Table Header -->
  <text x="60" y="30" fill="#facc15" font-size="10" font-family="sans-serif" font-weight="bold">Genotype</text>
  <text x="170" y="30" fill="#38bdf8" font-size="10" font-family="sans-serif" font-weight="bold">Proportion</text>
  <text x="290" y="30" fill="#4ade80" font-size="10" font-family="sans-serif" font-weight="bold">Resulting Phenotype</text>
  <line x1="30" y1="38" x2="370" y2="38" stroke="#334155" stroke-width="1"/>
  <!-- Rows -->
  <text x="60" y="60" fill="#cbd5e1" font-size="9" font-family="sans-serif">RRYY, RRYy, RrYY, RrYy</text>
  <text x="170" y="60" fill="#38bdf8" font-size="9" font-family="sans-serif">1 + 2 + 2 + 4 = 9/16</text>
  <text x="290" y="60" fill="#4ade80" font-size="9" font-family="sans-serif">Round Yellow (9)</text>

  <text x="60" y="90" fill="#cbd5e1" font-size="9" font-family="sans-serif">RRyy, Rryy</text>
  <text x="170" y="90" fill="#38bdf8" font-size="9" font-family="sans-serif">1 + 2 = 3/16</text>
  <text x="290" y="90" fill="#22c55e" font-size="9" font-family="sans-serif">Round Green (3)</text>

  <text x="60" y="120" fill="#cbd5e1" font-size="9" font-family="sans-serif">rrYY, rrYy</text>
  <text x="170" y="120" fill="#38bdf8" font-size="9" font-family="sans-serif">1 + 2 = 3/16</text>
  <text x="290" y="120" fill="#facc15" font-size="9" font-family="sans-serif">Wrinkled Yellow (3)</text>

  <text x="60" y="150" fill="#cbd5e1" font-size="9" font-family="sans-serif">rryy</text>
  <text x="170" y="150" fill="#38bdf8" font-size="9" font-family="sans-serif">1/16</text>
  <text x="290" y="150" fill="#ef4444" font-size="9" font-family="sans-serif">Wrinkled Green (1)</text>

  <text x="200" y="175" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle">Total: 9 Unique Genotypes in 1:2:1:2:4:2:1:2:1 Ratio</text>
</svg>
</div>
Which single genotype is the most frequent among all 16 F2 combinations, occurring in 4 out of 16 boxes (25%)?""",
     ["RrYy (Heterozygous at both gene loci)", "RRYY", "rryy", "Rryy"],
     "A", "OSC", "easy",
     "The double heterozygous genotype RrYy occurs four times ($4/16 = 25\\%$) because it can be formed by four distinct gametic unions (RY+ry, Ry+rY, rY+Ry, ry+RY)."),

    # 78: Thomas Hunt Morgan's Drosophila Linkage Experiment
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#111827"/>
  <!-- Morgan's Fly cross -->
  <rect x="30" y="25" width="340" height="40" rx="5" fill="#1f2937" stroke="#ec4899" stroke-width="2"/>
  <text x="200" y="45" fill="#ec4899" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Morgan's Fruit Fly Cross: Yellow Body & White Eyes (X-linked)</text>
  <text x="200" y="58" fill="#f472b6" font-size="8" font-family="sans-serif" text-anchor="middle">Observed 98.7% Parental Types vs only 1.3% Recombinants!</text>
  <!-- Bar Representation -->
  <rect x="50" y="85" width="260" height="35" rx="4" fill="#15803d"/>
  <text x="180" y="107" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Parental Types (98.7%)</text>
  <rect x="310" y="85" width="40" height="35" rx="4" fill="#dc2626"/>
  <text x="330" y="107" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">1.3% Rec</text>
  <!-- Takeaway -->
  <rect x="50" y="130" width="300" height="45" rx="5" fill="#1e293b" stroke="#facc15" stroke-width="1"/>
  <text x="200" y="148" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Discovery of Physical Gene Linkage</text>
  <text x="200" y="163" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Genes situated very close on the X chromosome rarely cross over</text>
</svg>
</div>
What historical discovery did Thomas Hunt Morgan deduce from the extreme disparity (98.7% parental vs 1.3% recombinant) in his yellow-white Drosophila cross?""",
     ["The yellow body and white eye genes are tightly linked on the X chromosome and co-segregate with very low recombination frequency",
      "Pea plants turn into fruit flies",
      "Mendel fabricated all his data",
      "Fruit flies have no X chromosome"],
     "A", "OSC", "medium",
     "Morgan proved that genes located closely on the same physical chromosome (linkage) do not assort independently, providing conclusive physical proof of the Chromosome Theory of Heredity."),

    # 79: P1 to F1 Dihybrid Parental Cross Diagram
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Parent 1 -->
  <circle cx="90" cy="50" r="22" fill="#eab308" stroke="#fef08a" stroke-width="2"/>
  <text x="90" y="55" fill="#000000" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">RRYY</text>
  <text x="90" y="85" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle">Round Yellow (P1)</text>
  <text x="145" y="55" fill="#ffffff" font-size="14" font-family="sans-serif">X</text>
  <!-- Parent 2 -->
  <circle cx="200" cy="50" r="22" fill="#15803d" stroke="#4ade80" stroke-width="2" stroke-dasharray="3"/>
  <text x="200" y="55" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">rryy</text>
  <text x="200" y="85" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle">Wrinkled Green (P1)</text>
  <!-- Arrow -->
  <line x1="145" y1="95" x2="145" y2="120" stroke="#facc15" stroke-width="2"/>
  <!-- F1 Progeny -->
  <rect x="70" y="125" width="150" height="45" rx="5" fill="#14532d" stroke="#facc15" stroke-width="2"/>
  <text x="145" y="145" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">F1: Genotype RrYy</text>
  <text x="145" y="160" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle">100% Round Yellow Seeds!</text>
  <!-- Gamete text box -->
  <rect x="250" y="40" width="120" height="120" rx="5" fill="#27272a" stroke="#38bdf8" stroke-width="1"/>
  <text x="310" y="65" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">F1 Gametes:</text>
  <text x="310" y="85" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">25% RY</text>
  <text x="310" y="105" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">25% Ry</text>
  <text x="310" y="125" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">25% rY</text>
  <text x="310" y="145" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">25% ry</text>
</svg>
</div>
What essential genetic fact is revealed by the observation that 100% of F1 plants produce Round Yellow seeds despite inheriting recessive 'r' and 'y' alleles?""",
     ["Both the round allele (R) and yellow allele (Y) exhibit complete dominance over their respective recessive alleles",
      "Recessive alleles were permanently destroyed during pollination",
      "Yellow seeds have no DNA",
      "Green color is caused by cold weather"],
     "A", "OSC", "easy",
     "The F1 generation confirms the Law of Dominance for multiple traits simultaneously: both dominant alleles (R and Y) independently mask their recessive counterparts (r and y)."),

    # 80: Polygenic / Trihybrid Calculation Tree
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Formula Summary -->
  <text x="200" y="30" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Mendelian Polyhybrid Mathematical Formulas (for 'n' pairs)</text>
  <!-- Row 1: Types of Gametes -->
  <rect x="40" y="45" width="320" height="35" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
  <text x="60" y="67" fill="#38bdf8" font-size="10" font-family="sans-serif" font-weight="bold">Types of Gametes produced by F1:</text>
  <text x="330" y="67" fill="#facc15" font-size="12" font-family="sans-serif" text-anchor="end" font-weight="bold">2^n</text>
  <!-- Row 2: Phenotypes in F2 -->
  <rect x="40" y="88" width="320" height="35" rx="4" fill="#1e293b" stroke="#4ade80" stroke-width="1"/>
  <text x="60" y="110" fill="#4ade80" font-size="10" font-family="sans-serif" font-weight="bold">Number of F2 Phenotypes (complete dominance):</text>
  <text x="330" y="110" fill="#facc15" font-size="12" font-family="sans-serif" text-anchor="end" font-weight="bold">2^n</text>
  <!-- Row 3: Genotypes in F2 -->
  <rect x="40" y="131" width="320" height="35" rx="4" fill="#1e293b" stroke="#ec4899" stroke-width="1"/>
  <text x="60" y="153" fill="#ec4899" font-size="10" font-family="sans-serif" font-weight="bold">Number of F2 Genotypes:</text>
  <text x="330" y="153" fill="#facc15" font-size="12" font-family="sans-serif" text-anchor="end" font-weight="bold">3^n</text>
</svg>
</div>
Using the general Mendelian polyhybrid formulas summarized above, how many distinct genotypes will be produced in the F2 generation of a tetrahybrid cross involving 4 independent heterozygous gene pairs (n = 4)?""",
     ["81 genotypes (3^4 = 81)", "16 genotypes", "256 genotypes", "64 genotypes"],
     "A", "ONE", "medium",
     "For a tetrahybrid cross ($n = 4$), the number of distinct F2 genotypes equals $3^n = 3^4 = 81$ genotypes."),

    # 81: Dihybrid Phenotype Segregation Proportions
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Bars for 9:3:3:1 -->
  <rect x="40" y="35" width="160" height="25" rx="3" fill="#15803d"/>
  <text x="50" y="52" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold">Round Yellow (9/16 = 56.25%)</text>
  <text x="180" y="52" fill="#fef08a" font-size="9" font-family="sans-serif" font-weight="bold">9</text>

  <rect x="40" y="70" width="70" height="25" rx="3" fill="#0284c7"/>
  <text x="50" y="87" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold">Round Green (3/16 = 18.75%)</text>
  <text x="90" y="87" fill="#fef08a" font-size="9" font-family="sans-serif" font-weight="bold">3</text>

  <rect x="40" y="105" width="70" height="25" rx="3" fill="#d97706"/>
  <text x="50" y="122" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold">Wrinkled Yellow (3/16 = 18.75%)</text>
  <text x="90" y="122" fill="#fef08a" font-size="9" font-family="sans-serif" font-weight="bold">3</text>

  <rect x="40" y="140" width="30" height="25" rx="3" fill="#b91c1c"/>
  <text x="50" y="157" fill="#ffffff" font-size="8" font-family="sans-serif" font-weight="bold">Wrinkled Green (1/16 = 6.25%)</text>
  <text x="55" y="157" fill="#fef08a" font-size="9" font-family="sans-serif" font-weight="bold">1</text>

  <!-- Side label -->
  <text x="300" y="90" fill="#facc15" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">Total: 16 Units</text>
  <text x="300" y="110" fill="#cbd5e1" font-size="10" font-family="sans-serif" text-anchor="middle">Ratio 9 : 3 : 3 : 1</text>
</svg>
</div>
In an agricultural field trial of 8,000 F2 pea plants resulting from a dihybrid cross, how many plants are expected to bear WRINKLED YELLOW seeds?""",
     ["1,500 plants (3/16 of 8,000)", "4,500 plants", "500 plants", "3,000 plants"],
     "A", "ONE", "easy",
     "Wrinkled yellow seeds represent $3/16$ of the total progeny. Therefore, $8,000 \\times (3/16) = 1,500$ plants."),

    # 82: Chiasma Formation during Meiotic Crossing-Over
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Chromatids crossing -->
  <line x1="80" y1="40" x2="160" y2="150" stroke="#38bdf8" stroke-width="5" stroke-linecap="round"/>
  <line x1="160" y1="40" x2="80" y2="150" stroke="#ec4899" stroke-width="5" stroke-linecap="round"/>
  <!-- Chiasma intersection -->
  <circle cx="120" cy="95" r="8" fill="#facc15"/>
  <text x="120" y="99" fill="#000000" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">X</text>
  <!-- Label -->
  <line x1="128" y1="95" x2="210" y2="95" stroke="#facc15" stroke-width="2"/>
  <text x="220" y="88" fill="#facc15" font-size="11" font-family="sans-serif" font-weight="bold">Chiasma (Crossing-Over Point)</text>
  <text x="220" y="105" fill="#cbd5e1" font-size="9" font-family="sans-serif">- Non-sister chromatids break and exchange segments</text>
  <text x="220" y="122" fill="#4ade80" font-size="9" font-family="sans-serif">- Generates genetic recombinants</text>
  <text x="220" y="140" fill="#94a3b8" font-size="8" font-family="sans-serif">Occurs during Pachytene of Meiosis I</text>
</svg>
</div>
What cytological event is occurring at the 'chiasma' intersection indicated in the diagram above?""",
     ["Physical breakage and reciprocal reciprocal exchange of DNA segments between non-sister chromatids of homologous chromosomes (crossing over)",
      "Destruction of the cell membrane",
      "Fusion of two sperm cells",
      "Formation of a new cell wall"],
     "A", "OSC", "easy",
     "A chiasma is the physical crossover site where non-sister chromatids of homologous bivalents break and re-ligate, exchanging genetic alleles during meiotic prophase I.")
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

output_path = os.path.join(os.path.dirname(__file__), "ch16_topic4.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
