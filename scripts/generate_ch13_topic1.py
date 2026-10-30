# scripts/generate_ch13_topic1.py
# MH-9-SCIT-13-13.1: Occurrence, Properties & Tetravalency of Carbon
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-13-13.1"

# 40 Exam Questions
exam_data = [
    # 1-10: Atomic Structure, Valency & Covalent Bonding
    ("What is the atomic number (Z) and standard electronic configuration of a neutral carbon atom?",
     ["Atomic number 6, electronic configuration (2, 4)",
      "Atomic number 12, electronic configuration (2, 8, 2)",
      "Atomic number 8, electronic configuration (2, 6)",
      "Atomic number 4, electronic configuration (2, 2)"],
     "A", "OSC", "easy",
     "Carbon has an atomic number of 6, meaning it possesses 6 protons and 6 electrons arranged as 2 electrons in the inner K-shell and 4 electrons in the valence L-shell (2, 4)."),

    ("Why does a carbon atom achieve octet stability by sharing electrons rather than forming ionic C4+ cations?",
     ["Removing four valence electrons requires an extraordinarily high amount of cumulative ionization energy that is energetically impossible under chemical conditions",
      "Carbon atoms are too heavy to lose electrons",
      "Carbon lacks protons in its nucleus",
      "Ionic bonds cannot exist in nature"],
     "A", "OSC", "medium",
     "The successive removal of four electrons requires enormous energy input against increasing nuclear charge, making the formation of a C4+ cation energetically unfeasible."),

    ("Why does a carbon atom not achieve octet stability by gaining four electrons to form C4- anions?",
     ["A tiny carbon nucleus with only 6 positive protons cannot stably hold onto 10 total electrons due to intense inter-electronic repulsion",
      "Gaining electrons causes carbon to explode",
      "Electrons cannot enter the L-shell",
      "Carbon atoms have zero electron affinity"],
     "A", "OSC", "medium",
     "A nucleus containing only 6 protons lacks sufficient positive electrostatic charge to hold 10 negatively charged electrons stably; extreme electrostatic repulsion destabilizes C4-."),

    ("How many covalent bonds does a carbon atom standardly form in stable organic molecules?",
     ["Four covalent bonds (tetravalency)",
      "Two covalent bonds",
      "Six covalent bonds",
      "One covalent bond"],
     "A", "OSC", "easy",
     "With 4 valence electrons, carbon shares one electron each with four other atoms (or forms double/triple bonds) to complete its stable octet of 8 electrons, exhibiting tetravalency."),

    ("What is the unique property of carbon atoms that allows them to link with other carbon atoms to form vast chains and rings?",
     ["Catenation", "Allotropy", "Electronegativity", "Radioactivity"],
     "A", "OSC", "easy",
     "Catenation is the remarkable ability of carbon atoms to form strong, stable covalent bonds with one another, generating endless straight chains, branched frameworks, and closed cyclic rings."),

    ("What is the approximate percentage of carbon dioxide present by volume in Earth's clean atmosphere?",
     ["Approximately 0.03% to 0.04%",
      "Approximately 21%",
      "Approximately 78%",
      "Approximately 5%"],
     "A", "OSC", "easy",
     "Carbon dioxide constitutes roughly 0.03% to 0.04% of Earth's atmosphere by volume, serving as the essential carbon reservoir for plant photosynthesis."),

    ("In which of the following natural forms does carbon occur in an uncombined, free elemental state?",
     ["Diamond and graphite",
      "Limestone and marble",
      "Petroleum and diesel",
      "Carbon dioxide gas"],
     "A", "OSC", "easy",
     "Diamond, graphite, and fullerenes represent pure elemental allotropes where carbon exists in a native, uncombined free state."),

    ("In which combined mineral form is carbon predominantly found in Earth's crustal rocks?",
     ["Carbonates such as limestone, chalk, and marble (calcium carbonate, CaCO3)",
      "Pure silicon dioxide",
      "Sodium chloride crystals",
      "Iron oxide rust"],
     "A", "OSC", "easy",
     "In the lithosphere, vast quantities of combined carbon reside in sedimentary carbonate minerals such as calcite, limestone, and dolomite (CaCO3 and MgCO3)."),

    ("What happens when an organic compound containing carbon is burned in an excess supply of air?",
     ["It oxidizes to form carbon dioxide (CO2) gas and water vapor, releasing heat energy",
      "It turns into pure solid diamond",
      "It forms hydrogen gas and ozone",
      "It produces liquid nitrogen"],
     "A", "OSC", "easy",
     "Combustion of carbon-containing organic compounds in oxygen produces carbon dioxide gas (CO2) along with water vapor and thermal energy."),

    ("Which simple chemical test confirms the presence of carbon dioxide gas evolved from burning an organic sample?",
     ["Passing the gas through clear lime water turns it milky due to the formation of insoluble calcium carbonate precipitate",
      "The gas turns blue litmus red instantly without color change",
      "The gas burns with a popping sound",
      "The gas relights a glowing wooden splint"],
     "A", "OSC", "easy",
     "When CO2 bubbles through lime water (aqueous calcium hydroxide, Ca(OH)2), it forms a white suspension of insoluble calcium carbonate (CaCO3), turning the solution milky."),

    # 11-20: Covalent Bonding & Molecular Geometry
    ("What is the geometric arrangement of the four single covalent bonds around a carbon atom in methane (CH4)?",
     ["A regular three-dimensional tetrahedron with bond angles of approximately 109.5 degrees",
      "A flat square plane with bond angles of 90 degrees",
      "A straight linear line with bond angles of 180 degrees",
      "A flat equilateral triangle with bond angles of 120 degrees"],
     "A", "OSC", "medium",
     "To minimize mutual repulsion between the four electron pairs (VSEPR theory), the bonds point toward the vertices of a regular tetrahedron with 109.5 deg bond angles."),

    ("What type of covalent bond exists between the two carbon atoms in an ethane (C2H6) molecule?",
     ["A single covalent bond (sharing one pair of electrons)",
      "A double covalent bond",
      "A triple covalent bond",
      "An ionic electrovalent bond"],
     "A", "OSC", "easy",
     "In ethane (H3C-CH3), the two carbon atoms share a single pair of electrons, forming a stable single covalent bond (C-C)."),

    ("What type of covalent bond links the two carbon atoms in an ethene (ethylene, C2H4) molecule?",
     ["A double covalent bond (sharing two pairs of electrons)",
      "A single covalent bond",
      "A triple covalent bond",
      "A hydrogen bond"],
     "A", "OSC", "easy",
     "In ethene (H2C=CH2), the two carbon atoms share two electron pairs, forming a double covalent bond comprising one sigma bond and one pi bond."),

    ("What type of covalent bond connects the two carbon atoms in an ethyne (acetylene, C2H2) molecule?",
     ["A triple covalent bond (sharing three pairs of electrons)",
      "A single covalent bond",
      "A double covalent bond",
      "A metallic bond"],
     "A", "OSC", "easy",
     "In ethyne (HC#CH), the two carbon atoms share three electron pairs, establishing a strong, linear triple covalent bond."),

    ("Why are carbon-carbon covalent bonds exceptionally strong and chemically stable compared to silicon-silicon bonds?",
     ["Carbon has a very small atomic radius, allowing its positive nucleus to hold the shared electron pairs firmly and closely",
      "Carbon has more neutrons than silicon",
      "Carbon is a noble gas",
      "Carbon atoms are magnetic"],
     "A", "OSC", "medium",
     "Because carbon belongs to period 2 with only two electron shells, its small atomic size allows tight nuclear overlap with shared bonding pairs, conferring high C-C bond energy (~348 kJ/mol)."),

    ("What is the phenomenon called when two or more organic compounds possess the identical molecular formula but distinct structural formulas?",
     ["Structural isomerism", "Allotropy", "Homologous series", "Polymerization"],
     "A", "OSC", "easy",
     "Isomerism describes compounds sharing the same molecular formula (same atom counts) whose different spatial arrangements yield distinct physical and chemical characteristics."),

    ("Which two structural isomers exist for the alkane butane with molecular formula C4H10?",
     ["n-butane (straight 4-carbon chain) and isobutane / 2-methylpropane (branched chain)",
      "Cyclobutane and methylcyclopropane",
      "1-butene and 2-butene",
      "Propane and methane"],
     "A", "OSC", "medium",
     "Butane (C4H10) can assemble as a continuous 4-carbon chain (n-butane, boiling point -0.5 deg C) or as a branched 3-carbon chain with a methyl branch (isobutane, boiling point -11.7 deg C)."),

    ("Which major class of biomolecules essential for living cells contains carbon as its primary structural element?",
     ["Carbohydrates, proteins, lipids, and nucleic acids (DNA/RNA)",
      "Pure table salt crystals",
      "Liquid water molecules only",
      "Atmospheric argon gas"],
     "A", "OSC", "easy",
     "All fundamental cellular macromolecules (sugars, amino acid polymers, fatty acids, and genetic material) are constructed on carbon backbones."),

    ("When wood or sugar is heated strongly in a dry test tube in the complete absence of air, what solid residue remains behind?",
     ["A black porous residue of carbon (charcoal)",
      "A white powder of calcium oxide",
      "A pool of metallic mercury",
      "A transparent glass bead"],
     "A", "OSC", "easy",
     "Destructive thermal decomposition drives off volatile hydrogen and oxygen as water vapor and gases, leaving elemental black carbon behind as char."),

    ("Why is carbon classified as a non-metal in the periodic table?",
     ["It forms acidic oxides (CO2), does not form simple cations in water, lacks metallic luster, and exhibits poor thermal conductivity in typical forms",
      "It has 12 valence electrons",
      "It reacts violently with cold water to release hydrogen",
      "It is located in Group 1"],
     "A", "OSC", "easy",
     "Carbon resides in Group 14 (Period 2) of the periodic table; its high electronegativity and ionization energy classify it chemically as a p-block non-metal."),

    # 21-30: True/False & Conceptual Assertions
    ("State whether the following statement is True or False: Carbon forms both open-chain (aliphatic) and closed-ring (cyclic) compounds.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Through catenation, carbon readily forms unbranched chains, branched networks, and closed cyclic rings (such as cyclohexane and benzene)."),

    ("State whether the following statement is True or False: Carbon can easily form ionic compounds by losing all 4 of its valence electrons to chlorine atoms.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Carbon shares electrons with chlorine to form covalent carbon tetrachloride (CCl4); it never forms C4+ ionic salts."),

    ("State whether the following statement is True or False: All living organisms are made up of carbon-based organic compounds.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Life on Earth is fundamentally carbon-based; carbon compounds account for virtually all biochemical structures and metabolic enzymes."),

    ("State whether the following statement is True or False: The valency of carbon in carbon monoxide (CO) is four.",
     ["False", "True"],
     "A", "OTF", "easy",
     "In carbon monoxide, carbon forms two covalent bonds and one coordinate bond with oxygen, formally acting with a valency of 2."),

    ("State whether the following statement is True or False: Carbon dioxide is a neutral oxide that does not react with water.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Carbon dioxide is an acidic oxide; it dissolves in water to form carbonic acid (H2CO3) and turns blue litmus red."),

    ("State whether the following statement is True or False: The mass number of the most abundant stable isotope of carbon is 12.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Carbon-12 (containing 6 protons and 6 neutrons) accounts for roughly 98.9% of natural carbon on Earth."),

    ("Which radioactive isotope of carbon with mass number 14 is utilized in archaeology to determine the age of ancient biological fossils?",
     ["Carbon-14 (14C)", "Carbon-12 (12C)", "Carbon-13 (13C)", "Carbon-16 (16C)"],
     "A", "OSC", "easy",
     "Radiocarbon dating measures the decay of radioactive Carbon-14 (half-life of 5,730 years) to date organic remnants up to 50,000 years old."),

    ("What is the nature of the chemical bonds formed within a carbon tetrachloride (CCl4) molecule?",
     ["Four single polar covalent bonds sharing four pairs of electrons symmetrically",
      "One ionic bond and three metallic bonds",
      "Four double bonds",
      "One quadruple covalent bond"],
     "A", "OSC", "medium",
     "Carbon shares one electron pair with each of four chlorine atoms, forming four equivalent single covalent bonds in a tetrahedral geometry."),

    ("Why does pure solid carbon tetrachloride (CCl4) not conduct electricity in liquid form?",
     ["It is a covalent molecular compound with no free ions or delocalized electrons to carry an electric charge",
      "It is an ionic salt with frozen ions",
      "It absorbs all electricity as heat",
      "It contains metallic cations"],
     "A", "OSC", "medium",
     "Covalent substances consist of neutral molecules and lack charged charge carriers (ions or mobile electrons), behaving as electrical insulators."),

    ("What happens to lime water when an excess of carbon dioxide gas is bubbled through it for a prolonged period?",
     ["The milky solution turns clear and colorless again because insoluble CaCO3 converts into soluble calcium bicarbonate (Ca(HCO3)2)",
      "The milkiness turns bright red",
      "The solution solidifies into stone",
      "The solution boils vigorously"],
     "A", "OSC", "medium",
     "Excess CO2 reacts with the CaCO3 precipitate to form water-soluble calcium hydrogen carbonate: CaCO3 + H2O + CO2 -> Ca(HCO3)2, restoring transparency."),

    # 31-40: Quantitative, Synthesis & Reasoning
    ("How many total shared pairs of electrons (covalent bonds) are present in one molecule of carbon dioxide (O=C=O)?",
     ["Four shared electron pairs (two double covalent bonds)",
      "Two shared electron pairs",
      "Six shared electron pairs",
      "Eight shared electron pairs"],
     "A", "OSC", "medium",
     "In CO2, carbon forms a double covalent bond with each of two oxygen atoms (O=C=O), sharing a total of 4 electron pairs (8 shared electrons)."),

    ("How many single covalent bonds are present in a single molecule of methane (CH4)?",
     ["Four single covalent C-H bonds",
      "Two bonds",
      "One bond",
      "Eight bonds"],
     "A", "OSC", "easy",
     "The central carbon atom forms four individual single covalent bonds with four hydrogen atoms (C-H)."),

    ("What is the total number of covalent bonds present in an ethane (C2H6) molecule?",
     ["Seven covalent bonds (one C-C bond and six C-H bonds)",
      "Six covalent bonds",
      "Eight covalent bonds",
      "Four covalent bonds"],
     "A", "OSC", "medium",
     "Ethane possesses 1 central C-C single bond plus 6 peripheral C-H single bonds, totaling 1 + 6 = 7 covalent bonds."),

    ("What is the total number of covalent bonds in an ethene (C2H4) molecule?",
     ["Six covalent bonds (one C=C double bond and four C-H single bonds)",
      "Five covalent bonds",
      "Four covalent bonds",
      "Seven covalent bonds"],
     "A", "OSC", "medium",
     "Ethene contains 1 double bond (counting as 2 bonds) between the carbons plus 4 C-H single bonds, giving 2 + 4 = 6 covalent bonds."),

    ("What is the total number of covalent bonds in an ethyne (acetylene, C2H2) molecule?",
     ["Five covalent bonds (one C#C triple bond and two C-H single bonds)",
      "Three covalent bonds",
      "Four covalent bonds",
      "Six covalent bonds"],
     "A", "OSC", "medium",
     "Ethyne contains 1 triple bond (3 bonds) between carbons plus 2 C-H single bonds, giving 3 + 2 = 5 covalent bonds."),

    ("Why can carbon form millions of different chemical compounds, far more than all other elements combined?",
     ["Due to the combination of its tetravalency, strong catenation ability, formation of multiple bonds, and structural isomerism",
      "Because carbon is the heaviest known element",
      "Because carbon reacts violently with all noble gases",
      "Because carbon atoms spontaneously multiply"],
     "A", "OSC", "easy",
     "The multifaceted versatility of carbon arises from catenation, tetravalent branching, single/double/triple bond formation, and isomeric diversity."),

    ("Which of the following fuels is NOT derived from fossilized ancient organic carbon deposits?",
     ["Nuclear uranium fuel rods", "Coal", "Petroleum (crude oil)", "Natural gas (methane)"],
     "A", "OSC", "easy",
     "Uranium is a radioactive heavy metal mined from mineral ores; coal, oil, and gas are fossilized carbon fuels from ancient biomass."),

    ("What is the molecular formula of the simplest saturated hydrocarbon (alkane)?",
     ["CH4 (Methane)", "C2H6 (Ethane)", "C2H4 (Ethene)", "C3H8 (Propane)"],
     "A", "OSC", "easy",
     "Methane (CH4) consists of a single carbon atom covalently bonded to four hydrogen atoms, representing the simplest alkane."),

    ("State whether the following statement is True or False: Graphite and diamond have completely identical chemical properties when burned in oxygen.",
     ["True", "False"],
     "A", "OTF", "medium",
     "Both allotropes are pure elemental carbon; when burned in pure oxygen, both yield solely carbon dioxide gas with zero ash residue."),

    ("What mass of carbon dioxide (CO2) is produced by the complete combustion of 12 grams of pure carbon in excess oxygen? (Atomic masses: C = 12, O = 16)",
     ["44 grams", "28 grams", "32 grams", "12 grams"],
     "A", "OSC", "medium",
     "C + O2 -> CO2. One mole of carbon (12 g) combines with one mole of O2 (32 g) to produce exactly one mole of CO2 (12 + 32 = 44 g).")
]

# 30 Practice Questions
practice_data = [
    ("What is the valency of carbon in methane (CH4)?",
     ["4 (tetravalent)", "2", "1", "3"],
     "A", "OSC", "easy",
     "Carbon shares 4 electron pairs to achieve an octet, exhibiting a valency of 4."),

    ("Which shell is the outermost (valence) shell of a carbon atom?",
     ["L-shell", "K-shell", "M-shell", "N-shell"],
     "A", "OSC", "easy",
     "With electronic configuration (2, 4), the K-shell holds 2 electrons and the outer L-shell holds 4 valence electrons."),

    ("How many electrons are required by a carbon atom to complete its octet in the L-shell?",
     ["4 electrons", "2 electrons", "6 electrons", "8 electrons"],
     "A", "OSC", "easy",
     "The L-shell can hold a maximum of 8 electrons; with 4 present, carbon requires 4 additional shared electrons for an octet."),

    ("Which of the following substances contains carbon in its chemical composition?",
     ["Sugar (sucrose, C12H22O11)", "Pure water (H2O)", "Sodium chloride table salt (NaCl)", "Copper sulphate crystals (CuSO4)"],
     "A", "OSC", "easy",
     "Sucrose is a carbohydrate disaccharide containing 12 carbon atoms per molecule."),

    ("State whether the following statement is True or False: Diamonds are composed entirely of pure carbon atoms.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Diamond is a crystalline allotrope of 100% elemental carbon arranged in a tetrahedral lattice."),

    ("State whether the following statement is True or False: Carbon dioxide turns dry blue litmus paper red without any moisture.",
     ["False", "True"],
     "A", "OTF", "easy",
     "CO2 requires moisture to form carbonic acid (H2CO3) that dissociates hydrogen ions to change litmus color; dry CO2 cannot affect dry litmus."),

    ("State whether the following statement is True or False: Carbon can form triple covalent bonds with nitrogen in cyanide groups (-C#N).",
     ["True", "False"],
     "A", "OTF", "easy",
     "Carbon shares three pairs of electrons with nitrogen to form stable nitrile and cyanide triple bonds."),

    ("What gas is released when dilute hydrochloric acid is poured onto marble chips (CaCO3)?",
     ["Carbon dioxide (CO2)", "Hydrogen gas (H2)", "Oxygen gas (O2)", "Chlorine gas (Cl2)"],
     "A", "OSC", "easy",
     "CaCO3 + 2HCl -> CaCl2 + H2O + CO2. Effervescence of carbon dioxide gas is produced."),

    ("What is the chemical name of lime water?",
     ["Calcium hydroxide solution, Ca(OH)2", "Calcium carbonate, CaCO3", "Calcium oxide, CaO", "Calcium chloride, CaCl2"],
     "A", "OSC", "easy",
     "Lime water is a clear dilute aqueous solution of calcium hydroxide (slaked lime)."),

    ("Why does baking bread or cake puff up with airy sponge holes when baked in an oven?",
     ["Carbon dioxide gas produced by baking powder or yeast expands under heat and escapes, leaving porous cavities",
      "Oxygen gas condenses inside the dough",
      "Nitrogen gas dissolves into the flour",
      "Water turns into solid ice"],
     "A", "OSC", "easy",
     "Thermal decomposition of sodium bicarbonate (baking soda) releases expanding bubbles of CO2 that create a light, porous spongy texture."),

    # 11-20
    ("What type of bond is formed when atoms share pairs of electrons?",
     ["Covalent bond", "Ionic bond", "Metallic bond", "Hydrogen bond"],
     "A", "OSC", "easy",
     "Covalent bonds arise from the mutual sharing of valence electron pairs between atoms."),

    ("How many pairs of electrons are shared between carbon and oxygen in a formaldehyde (H2C=O) molecule?",
     ["Two pairs (forming a double bond C=O)", "One pair", "Three pairs", "Four pairs"],
     "A", "OSC", "medium",
     "Carbon forms a double covalent bond with the carbonyl oxygen atom, sharing two electron pairs."),

    ("What is the general molecular formula for open-chain saturated hydrocarbons (alkanes)?",
     ["C_n H_{2n+2}", "C_n H_{2n}", "C_n H_{2n-2}", "C_n H_n"],
     "A", "OSC", "easy",
     "Acyclic alkanes follow the general homologous formula C_n H_{2n+2} (e.g. CH4, C2H6, C3H8)."),

    ("What is the general molecular formula for open-chain alkenes containing one double bond?",
     ["C_n H_{2n}", "C_n H_{2n+2}", "C_n H_{2n-2}", "C_n H_{2n-4} "],
     "A", "OSC", "easy",
     "Alkenes containing one C=C double bond follow the general formula C_n H_{2n} (e.g. C2H4, C3H6)."),

    ("What is the general molecular formula for open-chain alkynes containing one triple bond?",
     ["C_n H_{2n-2}", "C_n H_{2n}", "C_n H_{2n+2}", "C_n H_n"],
     "A", "OSC", "easy",
     "Alkynes containing one C#C triple bond follow the homologous formula C_n H_{2n-2} (e.g. C2H2, C3H4)."),

    ("State whether the following statement is True or False: Graphite conducts electricity because it contains delocalized, mobile electrons.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Each carbon in graphite is bonded to only three other carbons, leaving one unhybridized valence electron free to migrate across hexagonal graphene layers."),

    ("State whether the following statement is True or False: Carbon is found in stars like the Sun where nuclear fusion creates it from helium nuclei.",
     ["True", "False"],
     "A", "OTF", "medium",
     "The triple-alpha process in red giant stars fuses three helium-4 nuclei (alpha particles) to synthesize carbon-12."),

    ("What is the percentage by mass of carbon in a pure methane (CH4) molecule? (C = 12, H = 1)",
     ["75%", "50%", "25%", "80%"],
     "A", "OSC", "easy",
     "Molecular mass of CH4 = 12 + 4(1) = 16. Carbon mass percentage = (12 / 16) * 100 = 75%."),

    ("What is the percentage by mass of carbon in carbon dioxide (CO2)? (C = 12, O = 16)",
     ["27.27%", "50.0%", "72.73%", "33.33%"],
     "A", "OSC", "medium",
     "Molar mass of CO2 = 12 + 2(16) = 44 g/mol. Carbon percentage = (12 / 44) * 100 = 27.27%."),

    ("Which property of carbon allows it to form branched polymers such as starch and cellulose?",
     ["Catenation and tetravalent cross-linking",
      "High boiling point",
      "Magnetic susceptibility",
      "Radioactive decay"],
     "A", "OSC", "easy",
     "Tetravalent catenation allows carbon to form continuous backbone networks with side-chain branches."),

    # 21-30
    ("What is the term for compounds containing only carbon and hydrogen atoms?",
     ["Hydrocarbons", "Carbohydrates", "Halocarbons", "Carbonates"],
     "A", "OSC", "easy",
     "Compounds composed exclusively of carbon and hydrogen are termed hydrocarbons."),

    ("Which organic compound is commonly called 'marsh gas' because it bubbles up from decaying vegetation in swamps?",
     ["Methane (CH4)", "Carbon monoxide (CO)", "Ethylene (C2H4)", "Acetylene (C2H2)"],
     "A", "OSC", "easy",
     "Anaerobic bacterial digestion of plant cellulose in marshy bogs produces methane, colloquially named marsh gas."),

    ("State whether the following statement is True or False: All organic compounds must contain carbon.",
     ["True", "False"],
     "A", "OTF", "easy",
     "By definition, organic chemistry is the chemistry of carbon compounds (excluding simple oxides and carbonates)."),

    ("State whether the following statement is True or False: Carbon dioxide is a supporter of normal candle combustion.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Carbon dioxide does not support ordinary combustion; it smothers flames by displacing atmospheric oxygen."),

    ("Why does heating sugar in a dry test tube produce droplets of water on the cooler upper walls?",
     ["Sugar (C12H22O11) contains hydrogen and oxygen in a 2:1 ratio, which condense out as water vapor during thermal decomposition",
      "Sugar attracts water from the air outside the glass",
      "The test tube melts into liquid",
      "The flame leaks water through the glass"],
     "A", "OSC", "easy",
     "Carbohydrates undergo destructive dehydration upon heating, releasing constitutional hydrogen and oxygen as steam while leaving carbon behind."),

    ("How many electrons does carbon share with each hydrogen atom in a methane molecule?",
     ["One electron (forming a pair of two shared electrons)", "Two electrons", "Four electrons", "Zero electrons"],
     "A", "OSC", "easy",
     "Carbon contributes 1 electron and hydrogen contributes 1 electron to form each shared single covalent bond pair."),

    ("What is the physical state of methane and ethane at room temperature and normal atmospheric pressure?",
     ["Colorless, odorless gases", "Viscous oily liquids", "Hard crystalline solids", "Metallic powders"],
     "A", "OSC", "easy",
     "Lower alkanes (C1 to C4: methane, ethane, propane, butane) exist as gases due to weak intermolecular van der Waals forces."),

    ("What is the physical state of pentane (C5H12) through hexadecane (C16H34) at room temperature?",
     ["Liquids (such as gasoline, kerosene, diesel)",
      "Gases",
      "Hard brittle solids",
      "Plasma"],
     "A", "OSC", "easy",
     "Intermediate alkanes with 5 to 16 carbon atoms possess sufficient van der Waals attraction to exist as volatile liquids."),

    ("What is the physical state of alkanes with more than 17 carbon atoms (such as paraffin wax)?",
     ["Waxy solids", "Gases", "Thin vapors", "Plasmas"],
     "A", "OSC", "easy",
     "High molecular weight alkanes (>C17) have extensive surface contact, forming malleable waxy solids."),

    ("What happens when carbon monoxide (CO) gas is inhaled by humans?",
     ["It binds irreversibly to blood hemoglobin with over 200 times greater affinity than oxygen, causing fatal tissue asphyxiation",
      "It turns blood into clear water",
      "It improves athletic endurance",
      "It strengthens bone marrow"],
     "A", "OSC", "medium",
     "Carbon monoxide binds tightly to iron in hemoglobin to form carboxyhemoglobin, blocking oxygen transport and causing rapid cellular suffocation.")
]

# 12 Mock Questions with Vector SVG Diagrams
mock_data = [
    # 71: Carbon Atom Shell Structure & Tetravalency
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="200" viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="200" fill="#0f172a" rx="8"/>
  <!-- Nucleus -->
  <circle cx="170" cy="100" r="22" fill="#ef4444" stroke="#f87171" stroke-width="2"/>
  <text x="156" y="96" fill="#ffffff" font-size="9" font-weight="bold">6p + 6n</text>
  <text x="154" y="110" fill="#fde68a" font-size="8">Carbon-12</text>
  <!-- K-Shell (n=1) -->
  <circle cx="170" cy="100" r="45" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <circle cx="170" cy="55" r="5" fill="#38bdf8"/>
  <circle cx="170" cy="145" r="5" fill="#38bdf8"/>
  <text x="220" y="60" fill="#38bdf8" font-size="8">K Shell: 2 e-</text>
  <!-- L-Shell (n=2, Valence) -->
  <circle cx="170" cy="100" r="80" fill="none" stroke="#facc15" stroke-width="1.8"/>
  <circle cx="90" cy="100" r="6" fill="#facc15"/>
  <circle cx="250" cy="100" r="6" fill="#facc15"/>
  <circle cx="170" cy="20" r="6" fill="#facc15"/>
  <circle cx="170" cy="180" r="6" fill="#facc15"/>
  <text x="235" y="175" fill="#facc15" font-size="9" font-weight="bold">L Shell: 4 Valence e-</text>
  <text x="25" y="25" fill="#4ade80" font-size="9">Carbon Atomic Structure (Z = 6): Configuration (2, 4)</text>
</svg>
</div>
The diagram shows the Bohr atomic model of a neutral carbon-12 atom. Based on its 4 valence electrons in the outer L-shell, what fundamental chemical valency does carbon exhibit in forming stable organic molecules?""",
     ["Tetravalency (valency of 4 by sharing four electron pairs)""",
     "Monovalency (valency of 1)""",
     "Divalency (valency of 2)""",
     "Hexavalency (valency of 6)"],
     "A", "easy""",
     "With 4 valence electrons in its L-shell, carbon requires 4 more electrons to achieve the stable neon octet (8 electrons). It achieves this by forming 4 covalent bonds (tetravalency)."),

    # 72: Methane Tetrahedral Geometry
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Central Carbon Atom -->
  <circle cx="170" cy="100" r="18" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="165" y="105" fill="#f8fafc" font-size="12" font-weight="bold">C</text>
  <!-- 4 Hydrogen Atoms in Tetrahedron -->
  <!-- H top -->
  <line x1="170" y1="82" x2="170" y2="35" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="170" cy="30" r="12" fill="#0284c7"/>
  <text x="166" y="34" fill="#ffffff" font-size="10" font-weight="bold">H</text>
  <!-- H bottom-left -->
  <line x1="155" y1="110" x2="105" y2="155" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="95" cy="160" r="12" fill="#0284c7"/>
  <text x="91" y="164" fill="#ffffff" font-size="10" font-weight="bold">H</text>
  <!-- H bottom-right wedge -->
  <polygon points="175,112 235,160 220,165" fill="#38bdf8"/>
  <circle cx="235" cy="160" r="12" fill="#0284c7"/>
  <text x="231" y="164" fill="#ffffff" font-size="10" font-weight="bold">H</text>
  <!-- H dashed behind -->
  <line x1="178" y1="95" x2="225" y2="80" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="3,3"/>
  <circle cx="235" cy="78" r="12" fill="#0284c7"/>
  <text x="231" y="82" fill="#ffffff" font-size="10" font-weight="bold">H</text>
  <!-- Bond angle arc -->
  <path d="M 170 55 Q 185 70 195 90" stroke="#facc15" stroke-width="1.5" fill="none"/>
  <text x="195" y="70" fill="#facc15" font-size="10" font-weight="bold">109.5^{\circ}</text>
  <text x="60" y="180" fill="#fde68a" font-size="9">Tetrahedral Spatial Geometry of Methane (CH4)</text>
</svg>
</div>
The 3D spatial geometry of a methane (CH4) molecule is illustrated above. What is the precise H-C-H bond angle between the covalent bonds in this regular tetrahedral arrangement?""",
     ["109.5 degrees (or 109^{\circ}28')""",
     "90 degrees""",
     "120 degrees""",
     "180 degrees"],
     "A", "medium""",
     "Mutual electrostatic repulsion between the four equivalent electron bonding pairs forces them into a regular 3D tetrahedral geometry with characteristic bond angles of 109.5 degrees."),

    # 73: Catenation Chain Types (Straight, Branched, Cyclic)
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Straight Chain (Butane) -->
  <rect x="20" y="25" width="295" height="40" fill="#1e293b" rx="4"/>
  <text x="30" y="48" fill="#38bdf8" font-size="10" font-weight="bold">Straight:  C — C — C — C</text>
  <text x="210" y="48" fill="#94a3b8" font-size="9">(n-Butane)</text>
  <!-- Branched Chain (Isobutane) -->
  <rect x="20" y="75" width="140" height="95" fill="#1e293b" rx="4"/>
  <text x="30" y="98" fill="#4ade80" font-size="9" font-weight="bold">Branched Chain:</text>
  <text x="45" y="125" fill="#4ade80" font-size="10">C — C — C</text>
  <line x1="72" y1="128" x2="72" y2="148" stroke="#4ade80" stroke-width="2"/>
  <text x="68" y="160" fill="#4ade80" font-size="10">C</text>
  <!-- Cyclic Ring (Cyclohexane) -->
  <rect x="175" y="75" width="140" height="95" fill="#1e293b" rx="4"/>
  <text x="185" y="95" fill="#facc15" font-size="9" font-weight="bold">Closed Ring (Cyclic):</text>
  <polygon points="245,105 270,120 270,145 245,160 220,145 220,120" fill="none" stroke="#facc15" stroke-width="2"/>
  <text x="220" y="175" fill="#facc15" font-size="8">Cyclohexane (C6H12)</text>
</svg>
</div>
The diagram contrasts straight, branched, and cyclic carbon skeletons. Which unique chemical capability of carbon atoms enables the construction of such endless structural varieties?""",
     ["Catenation: the ability of carbon atoms to form strong covalent bonds with one another""",
     "High density of carbon""",
     "Ability of carbon to act as a noble gas""",
     "Magnetic attraction between carbon nuclei"],
     "A", "easy""",
     "Catenation refers to the self-linking property of carbon atoms through robust C-C covalent bonds, generating straight chains, branched isomers, and closed rings."),

    # 74: Lime Water Carbon Dioxide Test
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Test Tube 1: Clear lime water -->
  <rect x="40" y="40" width="35" height="95" fill="#0284c7" opacity="0.3" stroke="#38bdf8" stroke-width="1.5" rx="3"/>
  <text x="30" y="30" fill="#38bdf8" font-size="8">Initial: Clear</text>
  <text x="25" y="150" fill="#94a3b8" font-size="8">Ca(OH)2 solution</text>
  <!-- Delivery tube bubbling CO2 -->
  <path d="M 120 50 L 150 50 L 150 120" stroke="#facc15" stroke-width="2" fill="none"/>
  <polygon points="147,120 153,120 150,126" fill="#facc15"/>
  <text x="110" y="40" fill="#facc15" font-size="9" font-weight="bold">+ CO2 Gas</text>
  <!-- Test Tube 2: Milky Suspension -->
  <rect x="180" y="40" width="35" height="95" fill="#f8fafc" opacity="0.85" stroke="#cbd5e1" stroke-width="1.5" rx="3"/>
  <text x="175" y="30" fill="#ffffff" font-size="8" font-weight="bold">Turns Milky</text>
  <text x="160" y="150" fill="#ffffff" font-size="8">CaCO3 precipitate</text>
  <!-- Equation -->
  <text x="45" y="175" fill="#4ade80" font-size="9">Ca(OH)2 (aq) + CO2 (g) \rightarrow CaCO3 \downarrow (milky) + H2O (l)</text>
</svg>
</div>
The chemical experiment illustrated above serves as the confirmatory diagnostic test for carbon dioxide gas. Why does clear lime water turn milky when CO2 gas is bubbled through it?""",
     ["Insoluble white calcium carbonate (CaCO3) precipitate forms as a colloidal suspension""",
     "Calcium hydroxide dissolves into clear water""",
     "Carbon dioxide condenses into dry ice flakes""",
     "The water boils away leaving salt"],
     "A", "easy""",
     "Aqueous calcium hydroxide reacts with carbon dioxide to precipitate insoluble calcium carbonate: Ca(OH)2 + CO2 -> CaCO3 (solid white suspension) + H2O."),

    # 75: Excess CO2 Turning Solution Clear Again
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Milky test tube -->
  <rect x="50" y="45" width="40" height="90" fill="#f8fafc" opacity="0.8" stroke="#cbd5e1" stroke-width="1.5" rx="4"/>
  <text x="45" y="35" fill="#f8fafc" font-size="8">Milky (CaCO3)</text>
  <!-- Arrow with Excess CO2 -->
  <line x1="110" y1="90" x2="200" y2="90" stroke="#facc15" stroke-width="2.5"/>
  <polygon points="200,85 210,90 200,95" fill="#facc15"/>
  <text x="115" y="75" fill="#facc15" font-size="9" font-weight="bold">+ Excess CO2 + H2O</text>
  <!-- Clear test tube -->
  <rect x="230" y="45" width="40" height="90" fill="#38bdf8" opacity="0.25" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
  <text x="215" y="35" fill="#38bdf8" font-size="8" font-weight="bold">Clear Solution Again</text>
  <!-- Chemical Equation -->
  <text x="25" y="160" fill="#67e8f9" font-size="9">CaCO3 (s) + H2O (l) + CO2 (g) \rightarrow Ca(HCO3)2 (aq)</text>
  <text x="45" y="180" fill="#a7f3d0" font-size="9">Calcium hydrogen carbonate is completely water-soluble</text>
</svg>
</div>
What causes the white milkiness in lime water to disappear completely when carbon dioxide gas is passed continuously in excess (shown above)?""",
     ["Insoluble CaCO3 reacts with excess CO2 and water to form soluble calcium hydrogen carbonate [Ca(HCO3)2]""",
     "The milkiness evaporates into the room""",
     "Calcium carbonate transforms into metallic calcium""",
     "Carbon dioxide bleaches the white color away"],
     "A", "medium""",
     "Excess CO2 converts insoluble calcium carbonate into soluble calcium hydrogen carbonate: CaCO3 + H2O + CO2 -> Ca(HCO3)2 (aqueous), restoring complete clarity."),

    # 76: Covalent Bond Formation in Single, Double, Triple Bonds
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Single Bond: Ethane -->
  <rect x="20" y="25" width="300" height="40" fill="#1e293b" rx="4"/>
  <text x="30" y="48" fill="#38bdf8" font-size="9" font-weight="bold">Single Bond (Ethane):  H3C — CH3  (1 shared pair, length = 154 pm)</text>
  <!-- Double Bond: Ethene -->
  <rect x="20" y="75" width="300" height="40" fill="#1e293b" rx="4"/>
  <text x="30" y="98" fill="#4ade80" font-size="9" font-weight="bold">Double Bond (Ethene):  H2C = CH2  (2 shared pairs, length = 134 pm)</text>
  <!-- Triple Bond: Ethyne -->
  <rect x="20" y="125" width="300" height="40" fill="#1e293b" rx="4"/>
  <text x="30" y="148" fill="#facc15" font-size="9" font-weight="bold">Triple Bond (Ethyne):  HC # CH  (3 shared pairs, length = 120 pm)</text>
  <text x="40" y="180" fill="#fde68a" font-size="9">Higher bond order \rightarrow Greater bond strength, shorter bond length</text>
</svg>
</div>
The chart summarizes single, double, and triple carbon-carbon covalent bonds. What general relationship exists between the number of shared electron pairs (bond order) and bond length/strength?""",
     ["As bond order increases from single to triple, bond length decreases and bond strength increases significantly""",
     "Triple bonds are the weakest and longest bonds""",
     "Bond order has zero influence on bond strength""",
     "Single bonds have the highest bond dissociation energy"],
     "A", "medium""",
     "Sharing multiple electron pairs increases attractive nuclear-electron electrostatic forces, drawing the carbon nuclei closer (from 154 pm in C-C to 120 pm in C#C) and increasing bond strength."),

    # 77: Butane Structural Isomers (n-Butane vs Isobutane)
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Isomer 1: n-Butane -->
  <rect x="20" y="30" width="140" height="110" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
  <text x="30" y="50" fill="#38bdf8" font-size="10" font-weight="bold">n-Butane</text>
  <text x="30" y="75" fill="#e2e8f0" font-size="9">CH3-CH2-CH2-CH3</text>
  <text x="30" y="105" fill="#94a3b8" font-size="8">Straight Chain</text>
  <text x="30" y="125" fill="#facc15" font-size="8">B.P. = -0.5^{\circ}C</text>
  <!-- Isomer 2: Isobutane -->
  <rect x="180" y="30" width="140" height="110" fill="#1e293b" stroke="#4ade80" stroke-width="1.5" rx="4"/>
  <text x="190" y="50" fill="#4ade80" font-size="10" font-weight="bold">Isobutane (2-methylpropane)</text>
  <text x="190" y="75" fill="#e2e8f0" font-size="9">CH3-CH(CH3)-CH3</text>
  <text x="190" y="105" fill="#94a3b8" font-size="8">Branched Chain</text>
  <text x="190" y="125" fill="#facc15" font-size="8">B.P. = -11.7^{\circ}C</text>
  <text x="45" y="165" fill="#fde68a" font-size="9">Same Molecular Formula: C4H10 (Different Structures)</text>
  <text x="45" y="180" fill="#cbd5e1" font-size="8">Branching reduces surface area, lowering boiling point</text>
</svg>
</div>
Both n-butane and isobutane share the identical chemical formula \\(\\text{C}_4\\text{H}_{10}\\), yet isobutane boils at a noticeably lower temperature (\\(-11.7^{\\circ}\\text{C}\\) vs \\(-0.5^{\\circ}\\text{C}\\)). Why?""",
     ["Branching gives isobutane a more compact spherical shape with smaller surface area, weakening intermolecular van der Waals forces""",
     "Isobutane has fewer hydrogen atoms than n-butane""",
     "Isobutane is an ionic compound""",
     "n-butane contains double bonds"],
     "A", "medium""",
     "Branched molecules occupy a more spherical volume with reduced contact area, weakening temporary dipole-dipole (van der Waals) attractions and lowering boiling point."),

    # 78: Radiocarbon Dating Mechanism
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Atmosphere cycle -->
  <rect x="30" y="30" width="130" height="55" fill="#0369a1" opacity="0.4" stroke="#38bdf8" rx="4"/>
  <text x="40" y="50" fill="#38bdf8" font-size="9" font-weight="bold">Cosmic Rays in Air</text>
  <text x="40" y="70" fill="#cbd5e1" font-size="8">14N + n \rightarrow 14C + 1p</text>
  <!-- Living Organism -->
  <rect x="180" y="30" width="130" height="55" fill="#065f46" opacity="0.4" stroke="#34d399" rx="4"/>
  <text x="190" y="50" fill="#34d399" font-size="9" font-weight="bold">Living Biomass</text>
  <text x="190" y="70" fill="#cbd5e1" font-size="8">Constant 14C / 12C ratio</text>
  <!-- Fossil decay after death -->
  <rect x="30" y="105" width="280" height="55" fill="#78350f" opacity="0.4" stroke="#f59e0b" rx="4"/>
  <text x="40" y="125" fill="#fde68a" font-size="9" font-weight="bold">After Death (Fossil Wood / Bone):</text>
  <text x="40" y="145" fill="#ffffff" font-size="9">14C decays into 14N with half-life T_{1/2} = 5,730 years</text>
  <text x="45" y="180" fill="#facc15" font-size="9">Radiocarbon dating measures remaining 14C to date fossils</text>
</svg>
</div>
How does the radioactive isotope Carbon-14 (14C) enable archaeologists to determine the age of ancient wooden artifacts and bones?""",
     ["Upon death, intake of 14C halts and existing 14C decays at a known steady half-life (5,730 years); measuring the remaining ratio reveals elapsed time""",
     "14C turns into pure diamond after 1,000 years""",
     "14C glows in the dark with diminishing brightness""",
     "Ancient wood absorbs 14C from surrounding soil rocks"],
     "A", "medium""",
     "Living organisms maintain a steady 14C/12C ratio through metabolic exchange. At death, 14C intake stops and 14C beta-decays with a half-life of 5,730 years, allowing precise radiometric age calculation."),

    # 79: Comparison of Carbon vs Silicon Catenation
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Carbon-Carbon Bond Box -->
  <rect x="30" y="30" width="130" height="110" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
  <text x="40" y="50" fill="#38bdf8" font-size="10" font-weight="bold">C — C Bonding</text>
  <text x="40" y="75" fill="#cbd5e1" font-size="8">- Small atomic radius</text>
  <text x="40" y="90" fill="#cbd5e1" font-size="8">- Bond Energy: 348 kJ/mol</text>
  <text x="40" y="105" fill="#4ade80" font-size="8">- Highly stable chains</text>
  <text x="40" y="125" fill="#4ade80" font-size="9" font-weight="bold">Infinite Catenation</text>
  <!-- Silicon-Silicon Bond Box -->
  <rect x="180" y="30" width="130" height="110" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5" rx="4"/>
  <text x="190" y="50" fill="#fda4af" font-size="10" font-weight="bold">Si — Si Bonding</text>
  <text x="190" y="75" fill="#cbd5e1" font-size="8">- Larger atomic radius</text>
  <text x="190" y="90" fill="#cbd5e1" font-size="8">- Bond Energy: 222 kJ/mol</text>
  <text x="190" y="105" fill="#f87171" font-size="8">- Weak, reactive bonds</text>
  <text x="190" y="125" fill="#f87171" font-size="9" font-weight="bold">Chains unstable (>7 Si)</text>
  <text x="35" y="165" fill="#facc15" font-size="9">Small size of carbon enables strong overlap of shared pairs</text>
</svg>
</div>
Silicon belongs to the same Group 14 as carbon with 4 valence electrons, yet silicon can only form chains of up to 7-8 atoms while carbon forms chains of millions. What explains this dramatic difference?""",
     ["Carbon has a much smaller atomic radius, enabling tight nuclear attraction and high C-C bond energy (348 kJ/mol vs 222 kJ/mol for Si-Si)""",
     "Silicon atoms possess zero electrons in their valence shell""",
     "Silicon cannot form covalent bonds""",
     "Carbon atoms are magnetically attracted to each other"],
     "A", "hard""",
     "Carbon's small atomic radius (Period 2) enables strong orbital overlap and robust C-C bond strength (348 kJ/mol), whereas Silicon's larger radius (Period 3) weakens Si-Si bonds (222 kJ/mol), rendering long silane chains unstable in air."),

    # 80: Destructive Distillation of Organic Matter
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Boiling tube with sugar / wood -->
  <rect x="50" y="60" width="130" height="30" fill="#334155" stroke="#94a3b8" rx="3"/>
  <text x="55" y="80" fill="#facc15" font-size="9">Organic sample (sugar/wood)</text>
  <!-- Bunsen burner flame below -->
  <polygon points="105,95 115,115 125,95" fill="#ef4444"/>
  <text x="95" y="130" fill="#f87171" font-size="8">Strong Heat</text>
  <!-- Condensed water droplets -->
  <circle cx="160" cy="65" r="3" fill="#38bdf8"/>
  <circle cx="170" cy="68" r="3" fill="#38bdf8"/>
  <text x="175" y="55" fill="#38bdf8" font-size="8">Water droplets</text>
  <!-- Carbon black residue -->
  <rect x="55" y="65" width="40" height="20" fill="#020617"/>
  <text x="35" y="160" fill="#ffffff" font-size="9" font-weight="bold">Residual Black Mass = Elemental Carbon (Charcoal)</text>
  <text x="35" y="175" fill="#cbd5e1" font-size="8">Decomposition confirms presence of constituent carbon</text>
</svg>
</div>
When white cane sugar is heated strongly in a dry test tube, water droplets condense near the tube mouth and a voluminous black spongy residue forms at the bottom. What chemical conclusion does this establish?""",
     ["Sugar is an organic compound of carbon, hydrogen, and oxygen; heat dehydrates it to leave elemental black carbon""",
     "Sugar is a compound of nitrogen and sulphur""",
     "Sugar has absorbed black smoke from the burner""",
     "The glass test tube has melted into black charcoal"],
     "A", "easy""",
     "Thermal decomposition of carbohydrate sugar (C12H22O11) releases water of constitution (11 H2O) as steam, leaving behind a black solid residue of elemental carbon."),

    # 81: Global Carbon Cycle Reservoir
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Atmosphere Box -->
  <rect x="110" y="20" width="120" height="35" fill="#0369a1" opacity="0.4" stroke="#38bdf8" rx="3"/>
  <text x="125" y="42" fill="#38bdf8" font-size="9" font-weight="bold">Atmosphere (CO2)</text>
  <!-- Photosynthesis down arrow -->
  <line x1="140" y1="58" x2="80" y2="95" stroke="#4ade80" stroke-width="2"/>
  <text x="65" y="75" fill="#4ade80" font-size="8">Photosynthesis</text>
  <!-- Respiration up arrow -->
  <line x1="90" y1="95" x2="150" y2="58" stroke="#f43f5e" stroke-width="2"/>
  <text x="135" y="85" fill="#f43f5e" font-size="8">Respiration</text>
  <!-- Biosphere Box -->
  <rect x="30" y="100" width="120" height="40" fill="#065f46" opacity="0.4" stroke="#34d399" rx="3"/>
  <text x="40" y="125" fill="#34d399" font-size="9" font-weight="bold">Living Biomass</text>
  <!-- Lithosphere / Fossil Fuels -->
  <rect x="190" y="100" width="120" height="40" fill="#78350f" opacity="0.4" stroke="#f59e0b" rx="3"/>
  <text x="195" y="125" fill="#fde68a" font-size="9" font-weight="bold">Fossil Fuels & Rocks</text>
  <!-- Combustion arrow -->
  <line x1="250" y1="98" x2="210" y2="58" stroke="#ef4444" stroke-width="2"/>
  <text x="240" y="75" fill="#ef4444" font-size="8">Combustion</text>
  <text x="45" y="175" fill="#facc15" font-size="9">Continuous cycling of carbon between abiotic and biotic reservoirs</text>
</svg>
</div>
The chart depicts the global biogeochemical carbon cycle. Which natural process continuously removes carbon dioxide from the atmosphere to incorporate carbon into organic glucose molecules?""",
     ["Photosynthesis by green plants, algae, and cyanobacteria""",
     "Cellular respiration by animals""",
     "Combustion of coal and petroleum""",
     "Volcanic outgassing from mantle rocks"],
     "A", "easy""",
     "Photosynthesis absorbs atmospheric CO2 and water, utilizing solar photon energy to synthesize glucose (C6H12O6) and release oxygen: 6 CO2 + 6 H2O -> C6H12O6 + 6 O2."),

    # 82: Covalent Molecular vs Ionic Lattice Properties
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Covalent Carbon Compound Box (CH4, CCl4) -->
  <rect x="25" y="30" width="135" height="120" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
  <text x="35" y="50" fill="#38bdf8" font-size="9" font-weight="bold">Covalent (Carbon)</text>
  <text x="35" y="70" fill="#cbd5e1" font-size="8">- Shared electron pairs</text>
  <text x="35" y="85" fill="#cbd5e1" font-size="8">- Weak intermolecular forces</text>
  <text x="35" y="100" fill="#cbd5e1" font-size="8">- Low melting/boiling points</text>
  <text x="35" y="115" fill="#cbd5e1" font-size="8">- Non-conductors (no ions)</text>
  <text x="35" y="135" fill="#4ade80" font-size="8">e.g. CH4, C2H6, CCl4</text>
  <!-- Ionic Compound Box (NaCl) -->
  <rect x="180" y="30" width="135" height="120" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" rx="4"/>
  <text x="190" y="50" fill="#fbbf24" font-size="9" font-weight="bold">Ionic (e.g. NaCl)</text>
  <text x="190" y="70" fill="#cbd5e1" font-size="8">- Transferred electrons</text>
  <text x="190" y="85" fill="#cbd5e1" font-size="8">- Strong crystal lattice</text>
  <text x="190" y="100" fill="#cbd5e1" font-size="8">- High melting/boiling points</text>
  <text x="190" y="115" fill="#cbd5e1" font-size="8">- Conducts in molten/aqueous</text>
  <text x="190" y="135" fill="#facc15" font-size="8">e.g. NaCl, CaO, MgCl2</text>
  <text x="45" y="175" fill="#38bdf8" font-size="9">Covalent nature explains organic compounds' lower melting points</text>
</svg>
</div>
Why do carbon-based covalent compounds generally possess much lower melting and boiling points than ionic salts such as sodium chloride?""",
     ["Covalent molecules are held together by weak intermolecular van der Waals forces that require little thermal energy to overcome, unlike strong ionic crystal lattices""",
     "Carbon compounds contain no protons""",
     "Ionic bonds are made of light""",
     "Carbon compounds are always gaseous at all temperatures"],
     "A", "medium""",
     "While intramolecular covalent bonds within a molecule are strong, intermolecular forces between adjacent neutral covalent molecules are weak, resulting in low melting and boiling points.")
]

def generate():
    all_qs = []
    
    # 40 Exam
    for i, item in enumerate(exam_data, start=1):
        qcode = f"{TOPIC_CODE}-{item[3]}-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
            {"text": "True", "isCorrect": (item[2] == "A")},
            {"text": "False", "isCorrect": (item[2] == "B")}
        ]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "exam", "standard", item[5]))

    # 30 Practice
    for i, item in enumerate(practice_data, start=41):
        qcode = f"{TOPIC_CODE}-{item[3]}-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
            {"text": "True", "isCorrect": (item[2] == "A")},
            {"text": "False", "isCorrect": (item[2] == "B")}
        ]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "practice", "standard", item[5]))

    # 12 Mock
    for i, item in enumerate(mock_data, start=71):
        qcode = f"{TOPIC_CODE}-OSC-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], "OSC", item[3], "mock", "foundation", item[4]))

    out_file = "scripts/ch13_topic1.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {TOPIC_CODE} -> {out_file}")

if __name__ == "__main__":
    generate()
