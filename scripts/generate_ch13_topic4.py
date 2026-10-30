# scripts/generate_ch13_topic4.py
# MH-9-SCIT-13-13.4: Hydrocarbons: Saturated (Alkanes) vs Unsaturated (Alkenes & Alkynes)
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-13-13.4"

# 40 Exam Questions
exam_data = [
    # 1-10: Hydrocarbon Classification & Saturated Alkanes
    ("What defines a 'hydrocarbon' in organic chemistry?",
     ["An organic compound composed exclusively of carbon and hydrogen atoms",
      "A compound of carbon, hydrogen, and oxygen only",
      "A solution of carbon dissolved in liquid water",
      "A salt of carbonic acid and hydrogen gas"],
     "A", "OSC", "easy",
     "Hydrocarbons are the foundational parent compounds of organic chemistry, containing only carbon and hydrogen (e.g. CH4, C2H6, C2H4, C2H2)."),

    ("What distinguishes a 'saturated hydrocarbon' from an 'unsaturated hydrocarbon'?",
     ["In saturated hydrocarbons, all carbon atoms are bonded together exclusively by single covalent bonds, whereas unsaturated hydrocarbons contain at least one double or triple bond",
      "Saturated hydrocarbons contain water molecules in their crystal lattice",
      "Unsaturated hydrocarbons cannot burn in air",
      "Saturated hydrocarbons are always liquids at room temperature"],
     "A", "OSC", "easy",
     "Saturated hydrocarbons (alkanes) contain maximum possible hydrogen atoms linked solely by C-C single bonds; unsaturated hydrocarbons possess multiple C=C or C#C bonds with fewer hydrogens."),

    ("What is the general homologous molecular formula for acyclic saturated hydrocarbons (alkanes)?",
     ["C_n H_{2n+2}  (where n = 1, 2, 3, ...)",
      "C_n H_{2n}",
      "C_n H_{2n-2}",
      "C_n H_n"],
     "A", "OSC", "easy",
     "Alkanes follow the general formula C_n H_{2n+2}. For instance, methane (n=1) is CH4, ethane (n=2) is C2H6, propane (n=3) is C3H8, and butane (n=4) is C4H10."),

    ("What were saturated hydrocarbons (alkanes) historically termed due to their low chemical reactivity at room temperature?",
     ["Paraffins (from Latin parum affinis, meaning 'little affinity')",
      "Olefins",
      "Acetylenes",
      "Aromatics"],
     "A", "OSC", "easy",
     "Because single C-C and C-H sigma bonds are strong and non-polar, alkanes resist attack by ordinary acids, bases, and oxidizing agents at room temperature, earning the name paraffins."),

    ("What type of flame is typically produced when saturated hydrocarbons burn in an adequate supply of air?",
     ["A clean, non-sooty blue flame with complete combustion",
      "A dense, smoky yellow flame with heavy black soot",
      "A bright green sparkling flame",
      "A flame that emits zero heat"],
     "A", "OSC", "easy",
     "Alkanes have a relatively high hydrogen-to-carbon ratio, allowing complete combustion to CO2 and H2O in excess air with a clear, non-sooty blue flame."),

    ("What is the general homologous molecular formula for acyclic alkenes containing one double bond?",
     ["C_n H_{2n}  (where n >= 2)",
      "C_n H_{2n+2}",
      "C_n H_{2n-2}",
      "C_n H_{2n+1}"],
     "A", "OSC", "easy",
     "Alkenes contain one C=C double bond, reducing hydrogen by two compared to alkanes to give the general formula C_n H_{2n} (e.g. ethene C2H4, propene C3H6)."),

    ("What is the IUPAC name and common commercial name of the simplest alkene with molecular formula C2H4?",
     ["IUPAC: Ethene, Common: Ethylene",
      "IUPAC: Ethane, Common: Acetylene",
      "IUPAC: Ethyne, Common: Propylene",
      "IUPAC: Methane, Common: Marsh gas"],
     "A", "OSC", "easy",
     "C2H4 is officially named ethene in IUPAC nomenclature and commonly known as ethylene in industry."),

    ("What is the general homologous molecular formula for acyclic alkynes containing one carbon-carbon triple bond?",
     ["C_n H_{2n-2}  (where n >= 2)",
      "C_n H_{2n}",
      "C_n H_{2n+2}",
      "C_n H_{n+2}"],
     "A", "OSC", "easy",
     "Alkynes contain a C#C triple bond, possessing four fewer hydrogens than corresponding alkanes: C_n H_{2n-2} (e.g. ethyne C2H2, propyne C3H4)."),

    ("What is the IUPAC name and common commercial name of the simplest alkyne with molecular formula C2H2?",
     ["IUPAC: Ethyne, Common: Acetylene",
      "IUPAC: Ethene, Common: Ethylene",
      "IUPAC: Ethane, Common: Marsh gas",
      "IUPAC: Propane, Common: LPG"],
     "A", "OSC", "easy",
     "C2H2 is officially named ethyne (IUPAC) and commonly called acetylene, famously used in high-temperature oxy-acetylene welding torches."),

    ("Why do unsaturated hydrocarbons (alkenes and alkynes) burn with a luminous, sooty yellow flame in ordinary air?",
     ["They have a higher carbon-to-hydrogen ratio, causing incomplete combustion in atmospheric air that leaves glowing incandescent unburned carbon soot particles",
      "They contain sulfur impurities naturally",
      "They react with atmospheric nitrogen",
      "They absorb oxygen without burning"],
     "A", "OSC", "medium",
     "Higher carbon proportions require greater volumes of oxygen per mole for complete oxidation. In normal air, incomplete combustion produces fine carbon soot that glows yellow in the flame."),

    # 11-20: Unsaturation Tests & Chemical Reactions
    ("Which chemical diagnostic test can readily distinguish an unsaturated hydrocarbon (ethene) from a saturated hydrocarbon (ethane)?",
     ["Bromine water test: ethene decolourises reddish-brown bromine water, whereas ethane does not",
      "Blue litmus paper test: ethene turns litmus blue to red",
      "Lime water test: ethane turns lime water milky without burning",
      "Starch iodine test: ethene turns blue-black"],
     "A", "OSC", "easy",
     "Unsaturated alkenes rapidly add bromine across the double bond (forming colorless 1,2-dibromoethane), discharging the reddish-brown bromine color; saturated alkanes show no reaction in the dark."),

    ("What is the chemical reaction called when reddish-brown bromine adds across the double bond of ethene?",
     ["Addition reaction: C2H4 + Br2 -> CH2Br-CH2Br (1,2-dibromoethane)",
      "Substitution reaction",
      "Displacement reaction",
      "Decomposition reaction"],
     "A", "OSC", "easy",
     "Addition reactions are characteristic of unsaturated hydrocarbons, where the weak pi-bond breaks to incorporate the two bromine atoms into a single saturated product."),

    ("What chemical change occurs when ethene is bubbled through cold, alkaline potassium permanganate (KMnO4) solution (Baeyer's reagent)?",
     ["The bright purple permanganate solution is decolourised and forms a brown precipitate of manganese dioxide (MnO2)",
      "The solution turns bright yellow",
      "The solution freezes into solid ice",
      "The solution releases chlorine gas"],
     "A", "OSC", "medium",
     "Baeyer's reagent oxidizes the double bond into a diol (ethylene glycol), reducing purple MnO4- ions to brown MnO2 precipitate, confirming unsaturation."),

    ("What type of chemical reaction occurs when methane reacts with chlorine gas in the presence of diffused sunlight?",
     ["Substitution reaction: CH4 + Cl2 -> CH3Cl + HCl",
      "Addition reaction",
      "Polymerization reaction",
      "Precipitation reaction"],
     "A", "OSC", "easy",
     "Because methane has no multiple bonds to break, a chlorine radical displaces and substitutes for a hydrogen atom, yielding chloromethane and hydrogen chloride."),

    ("What industrial chemical process converts liquid vegetable oils into solid vegetable ghee (vanaspati)?",
     ["Catalytic hydrogenation: bubbling hydrogen gas through unsaturated vegetable oil at 60 deg C in the presence of a finely divided nickel (Ni) catalyst",
      "Oxidation with concentrated sulfuric acid",
      "Electrolysis of the oil with carbon electrodes",
      "Boiling the oil with table salt"],
     "A", "OSC", "easy",
     "Hydrogenation adds hydrogen atoms across the C=C double bonds in polyunsaturated vegetable oils, converting them into saturated solid fats (vanaspati ghee)."),

    ("Why is consuming natural liquid vegetable oils containing unsaturated fatty acids considered healthier for the human heart than solid saturated fats?",
     ["Unsaturated fatty acids maintain healthy blood cholesterol profiles (higher HDL), whereas excessive saturated fats increase LDL cholesterol and arterial plaque risk",
      "Unsaturated oils contain pure vitamin C",
      "Saturated fats dissolve human blood vessels",
      "Unsaturated oils are made of water"],
     "A", "OSC", "easy",
     "Polyunsaturated and monounsaturated fatty acids with cis-double bonds do not elevate atherogenic LDL cholesterol, reducing cardiovascular disease risk."),

    ("What chemical product is formed when ethene (C2H4) undergoes catalytic hydrogenation with hydrogen gas in the presence of nickel (Ni) or platinum (Pt)?",
     ["Ethane (C2H6)", "Methane (CH4)", "Acetylene (C2H2)", "Ethanol (C2H5OH)"],
     "A", "OSC", "easy",
     "C2H4 + H2 --(Ni catalyst)--> C2H6. Addition of hydrogen across the double bond converts unsaturated ethene into saturated ethane."),

    ("What gas is mixed with ethyne (acetylene) in welding torches to produce temperatures over 3000 deg C capable of cutting steel?",
     ["Pure oxygen gas (oxy-acetylene flame)",
      "Pure nitrogen gas",
      "Carbon dioxide gas",
      "Helium gas"],
     "A", "OSC", "easy",
     "Burning ethyne in pure oxygen yields an intensely hot oxy-acetylene flame (>3300 deg C) that melts steel instantaneously for welding and demolition cutting."),

    ("Which plant hormone gas is commercially used by fruit traders to artificially ripen green bananas, mangoes, and tomatoes?",
     ["Ethene (ethylene, C2H4)", "Methane (CH4)", "Propane (C3H8)", "Carbon monoxide (CO)"],
     "A", "OSC", "easy",
     "Ethylene is a natural plant hormone triggering fruit maturation, softening, and chlorophyll breakdown; controlled exposure ripens harvested fruit uniformly."),

    ("What synthetic plastic polymer is manufactured by the high-pressure polymerization of thousands of ethene (ethylene) monomers?",
     ["Polyethylene (polythene)", "Polyvinyl chloride (PVC)", "Polystyrene", "Nylon-6,6"],
     "A", "OSC", "easy",
     "Under heat and catalyst pressure, ethene double bonds break to link thousands of monomers into long saturated polyethylene chains: n(C2H4) -> (-CH2-CH2-)_n."),

    # 21-30: True/False & Molecular Structures
    ("State whether the following statement is True or False: Saturated hydrocarbons undergo addition reactions with bromine water.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Saturated hydrocarbons have only single bonds and cannot undergo addition reactions; they react only via substitution under strong light."),

    ("State whether the following statement is True or False: Ethyne (acetylene) has a linear molecular geometry with H-C-C bond angles of 180 degrees.",
     ["True", "False"],
     "A", "OTF", "easy",
     "The carbon atoms in ethyne are sp-hybridized, forming a collinear cylindrical triple bond with 180 deg bond angles (H-C#C-H)."),

    ("State whether the following statement is True or False: Ethene (ethylene) has a planar molecular geometry with bond angles of approximately 120 degrees.",
     ["True", "False"],
     "A", "OTF", "easy",
     "The carbon atoms in ethene are sp2-hybridized, creating a flat planar geometry with bond angles of roughly 120 degrees."),

    ("State whether the following statement is True or False: Alkanes are generally soluble in water.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Alkanes are non-polar hydrophobic molecules that do not form hydrogen bonds with water, dissolving only in non-polar organic solvents."),

    ("State whether the following statement is True or False: The addition of hydrogen to unsaturated oils in the presence of nickel is an example of an addition reaction.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Hydrogen molecules add across the carbon-carbon double bonds, making it a classic industrial addition reaction."),

    ("State whether the following statement is True or False: Methane (CH4) can decolourise purple potassium permanganate solution.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Being a saturated alkane, methane does not react with or decolourise cold alkaline KMnO4 solution."),

    ("State whether the following statement is True or False: Alkynes are more reactive towards electrophilic addition reactions than alkanes.",
     ["True", "False"],
     "A", "OTF", "easy",
     "The exposed, electron-rich pi-electrons in double and triple bonds make unsaturated hydrocarbons far more chemically reactive than alkanes."),

    ("What is the molecular formula of propane, the third member of the alkane homologous series?",
     ["C3H8", "C3H6", "C3H4", "C4H10"],
     "A", "OSC", "easy",
     "Using C_n H_{2n+2} with n=3: C3 H_{2(3)+2} = C3H8."),

    ("What is the molecular formula of propene, the second member of the alkene homologous series?",
     ["C3H6", "C3H8", "C3H4", "C2H4"],
     "A", "OSC", "easy",
     "Using C_n H_{2n} with n=3: C3 H_{2(3)} = C3H6."),

    ("What is the molecular formula of propyne, the second member of the alkyne homologous series?",
     ["C3H4", "C3H6", "C3H8", "C2H2"],
     "A", "OSC", "easy",
     "Using C_n H_{2n-2} with n=3: C3 H_{2(3)-2} = C3H4."),

    ("What type of bond exists between carbon atoms in an alkyne molecule?",
     ["One sigma bond and two pi bonds (triple bond)",
      "Three sigma bonds",
      "One ionic bond and two covalent bonds",
      "Three pi bonds with zero sigma bonds"],
     "A", "OSC", "medium",
     "A carbon-carbon triple bond consists of one strong axial sigma bond and two mutually perpendicular lateral pi bonds."),

    ("Which property of alkenes explains why they are also commercially known as 'olefins'?",
     ["They react with halogens (like chlorine) to form oily liquid products (from Latin oleum facere, 'oil-making')",
      "They are extracted from olive oil trees",
      "They float on water like petroleum oil",
      "They are viscous like engine oil"],
     "A", "OSC", "easy",
     "Early chemists observed that ethene reacted with chlorine gas to form an oily liquid (Dutch liquid, 1,2-dichloroethane), hence naming alkenes 'olefins'."),

    ("What is the general molecular formula of a cycloalkane containing one ring (e.g. cyclopropane, cyclohexane)?",
     ["C_n H_{2n} (isomeric with alkenes)",
      "C_n H_{2n+2}",
      "C_n H_{2n-2}",
      "C_n H_n"],
     "A", "OSC", "medium",
     "Closing a carbon chain into a cyclic ring eliminates two terminal hydrogen atoms, giving cycloalkanes the general formula C_n H_{2n}."),

    ("What is the molecular formula and structure of cyclohexane?",
     ["C6H12, a closed saturated hexagonal ring of 6 CH2 methylene groups",
      "C6H6, an aromatic planar ring with alternating double bonds",
      "C6H14, an open-chain straight alkane",
      "C6H10, a cyclic alkyne"],
     "A", "OSC", "easy",
     "Cyclohexane (C6H12) is a saturated 6-carbon cyclic alkane with each carbon bonded to two neighbouring carbons and two hydrogens."),

    ("How does the carbon-carbon bond length compare across single (ethane), double (ethene), and triple (ethyne) bonds?",
     ["C-C (154 pm) > C=C (134 pm) > C#C (120 pm)",
      "C#C (154 pm) > C=C (134 pm) > C-C (120 pm)",
      "All three bond lengths are strictly identical (142 pm)",
      "C=C is longer than both single and triple bonds"],
     "A", "OSC", "medium",
     "Greater bond order draws the carbon nuclei closer together due to higher electron density between them, shortening bond length."),

    ("Which alkane is commonly used as a laboratory solvent for extracting non-polar organic compounds?",
     ["Hexane (C6H14)", "Methane", "Propane", "Carbonic acid"],
     "A", "OSC", "easy",
     "Hexane is a volatile, non-polar liquid alkane that efficiently dissolves vegetable oils, fats, and non-polar organic solutes."),

    ("What is the primary industrial source of commercial hydrocarbons worldwide?",
     ["Petroleum (crude oil) and natural gas deposits",
      "Atmospheric air distillation",
      "Seawater evaporation",
      "Limestone quarrying"],
     "A", "OSC", "easy",
     "Crude oil and natural gas are vast underground hydrocarbon reservoirs refined through fractional distillation into fuels and petrochemical feedstocks."),

    ("State whether the following statement is True or False: Saturated alkanes decolourise alkaline potassium permanganate (Baeyer's reagent).",
     ["False", "True"],
     "A", "OTF", "easy",
     "Saturated alkanes lack accessible pi-electrons and do not react with cold alkaline KMnO4, maintaining the purple color."),

    ("What is the IUPAC name for the hydrocarbon with structural formula CH3-CH2-CH=CH2?",
     ["1-butene (or but-1-ene)", "2-butene", "Butane", "1-butyne"],
     "A", "OSC", "easy",
     "A 4-carbon chain containing a double bond starting at carbon-1 is named 1-butene (but-1-ene)."),

    ("What is the IUPAC name for the hydrocarbon with structural formula CH3-C#C-CH3?",
     ["2-butyne (or but-2-yne)", "1-butyne", "2-butene", "Butane"],
     "A", "OSC", "easy",
     "A 4-carbon chain containing a triple bond situated symmetrically between carbon-2 and carbon-3 is named 2-butyne (but-2-yne).")
]

# 30 Practice Questions
practice_data = [
    ("How many single covalent bonds are present in an ethane (C2H6) molecule?",
     ["7 bonds (1 C-C bond and 6 C-H bonds)", "6 bonds", "8 bonds", "4 bonds"],
     "A", "OSC", "easy",
     "Ethane contains 1 central carbon-carbon single bond and 6 peripheral carbon-hydrogen single bonds, totaling 7 covalent bonds."),

    ("How many shared pairs of electrons form the double bond in an ethene (C2H4) molecule?",
     ["2 shared pairs (four electrons in total)", "1 shared pair", "3 shared pairs", "4 shared pairs"],
     "A", "OSC", "easy",
     "A double covalent bond consists of 2 shared electron pairs (one sigma bond and one pi bond)."),

    ("How many shared pairs of electrons form the triple bond in an ethyne (C2H2) molecule?",
     ["3 shared pairs (six electrons in total)", "2 shared pairs", "1 shared pair", "4 shared pairs"],
     "A", "OSC", "easy",
     "A triple covalent bond consists of 3 shared electron pairs (one sigma bond and two pi bonds)."),

    ("Which catalyst is commonly used in the industrial hydrogenation of vegetable oils into vanaspati ghee?",
     ["Finely divided nickel (Ni)", "Iron oxide", "Zinc granules", "Copper wire"],
     "A", "OSC", "easy",
     "Finely divided nickel serves as the heterogeneous catalyst facilitating H2 adsorption and bond addition at 60 deg C."),

    ("State whether the following statement is True or False: Cooking oils containing unsaturated fatty acids remain liquid at room temperature.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Cis-double bonds introduce kinks in hydrocarbon tails that prevent tight crystalline packing, keeping unsaturated oils liquid at room temperature."),

    ("State whether the following statement is True or False: Saturated fats like butter and vanaspati ghee are typically solids or semi-solids at room temperature.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Straight saturated hydrocarbon chains pack tightly together, increasing van der Waals interactions and raising melting points into solids."),

    ("What color change occurs when an unsaturated alkene gas is bubbled into reddish-brown bromine water?",
     ["The reddish-brown color completely disappears, turning into a clear colorless solution",
      "The solution turns deep purple",
      "The solution turns bright green",
      "The solution solidifies into black powder"],
     "A", "OSC", "easy",
     "Bromine adds across the double bond to form a colorless vicinal dibromide, discharging the characteristic reddish-brown color."),

    ("What is the product when chlorine gas completely substitutes all hydrogen atoms in methane?",
     ["Carbon tetrachloride (CCl4) and hydrogen chloride (HCl)",
      "Chloroform (CHCl3) only",
      "Dichloromethane only",
      "Chloromethane only"],
     "A", "OSC", "medium",
     "Progressive photochemical substitution: CH4 -> CH3Cl -> CH2Cl2 -> CHCl3 -> CCl4 (carbon tetrachloride)."),

    ("What is the primary commercial use of acetylene gas in construction and shipbreaking?",
     ["High-temperature oxy-acetylene metal cutting and welding",
      "Fuel for jet aeroplanes",
      "Refrigerant in kitchen refrigerators",
      "Fire extinguisher propellant"],
     "A", "OSC", "easy",
     "Oxy-acetylene combustion produces temperatures exceeding 3300 deg C, melting high-strength steel effortlessly."),

    ("Which property makes ethene (ethylene) indispensable in the modern plastics industry?",
     ["Its ability to undergo addition polymerization to produce polyethylene plastics",
      "Its ability to dissolve metals",
      "Its magnetic attraction to glass",
      "Its high electrical conductivity"],
     "A", "OSC", "easy",
     "Polymerization of ethylene monomers produces millions of tons of film, piping, and container polyethylene plastic annually."),

    # 11-20
    ("What is the IUPAC name of the alkane with molecular formula C5H12?",
     ["Pentane", "Hexane", "Butane", "Propane"],
     "A", "OSC", "easy",
     "A 5-carbon alkane is named pentane (root 'pent-' + suffix '-ane')."),

    ("What is the IUPAC name of the alkane with molecular formula C6H14?",
     ["Hexane", "Heptane", "Octane", "Pentane"],
     "A", "OSC", "easy",
     "A 6-carbon alkane is named hexane (root 'hex-' + suffix '-ane')."),

    ("How many structural isomers exist for pentane (C5H12)?",
     ["Three isomers (n-pentane, isopentane, and neopentane)",
      "Two isomers",
      "Five isomers",
      "Four isomers"],
     "A", "OSC", "medium",
     "C5H12 forms 3 structural isomers: n-pentane (straight), isopentane/2-methylbutane (branched), and neopentane/2,2-dimethylpropane (cross-branched)."),

    ("State whether the following statement is True or False: Saturated hydrocarbons are generally more reactive than unsaturated hydrocarbons.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Unsaturated hydrocarbons are significantly more reactive due to reactive, accessible pi-electrons in double and triple bonds."),

    ("State whether the following statement is True or False: The bond angle in methane (CH4) is 90 degrees.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Methane has a tetrahedral geometry with bond angles of 109.5 degrees, not 90 degrees."),

    ("State whether the following statement is True or False: Ethylene gas is produced naturally by ripening fruits.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Ethylene is an endogenous phytohormone synthesized naturally by fruits like apples and bananas to stimulate ripening."),

    ("What type of hybridization is present in the carbon atoms of an ethene (C2H4) molecule?",
     ["sp2 hybridization (trigonal planar)", "sp3 hybridization", "sp hybridization", "dsp3 hybridization"],
     "A", "OSC", "medium",
     "Each carbon in ethene hybridizes one s and two p orbitals into three planar sp2 hybrid orbitals oriented at 120 degrees."),

    ("What type of hybridization is present in the carbon atoms of an ethyne (C2H2) molecule?",
     ["sp hybridization (linear)", "sp3 hybridization", "sp2 hybridization", "d2sp3 hybridization"],
     "A", "OSC", "medium",
     "Each carbon in ethyne hybridizes one s and one p orbital into two linear sp hybrid orbitals oriented at 180 degrees."),

    ("Which alkane is the main constituent (over 90%) of compressed natural gas (CNG) and piped natural gas (PNG)?",
     ["Methane (CH4)", "Propane (C3H8)", "Butane (C4H10)", "Ethane (C2H6)"],
     "A", "OSC", "easy",
     "Natural gas consists predominantly of methane (~90-95%), providing a clean-burning gaseous motor and domestic fuel."),

    ("Which two alkanes are liquefied under moderate pressure to formulate commercial Liquefied Petroleum Gas (LPG) cylinders?",
     ["Propane (C3H8) and Butane (C4H10)", "Methane and ethene", "Ethane and ethyne", "Pentane and hexane"],
     "A", "OSC", "easy",
     "Domestic LPG cylinders contain a pressurized mixture primarily of butane and propane with odorant ethanethiol."),

    # 21-30
    ("What strong-smelling chemical is added to odorless domestic LPG cylinders to enable immediate detection of gas leaks?",
     ["Ethyl mercaptan (ethanethiol, C2H5SH)", "Ammonia water", "Sulfur dioxide", "Chlorine"],
     "A", "OSC", "easy",
     "Because pure propane and butane are odorless, pungent ethanethiol is added as a safety odorant so even tiny leaks are smelled immediately."),

    ("State whether the following statement is True or False: All hydrocarbons are insoluble in water and float on water because their density is less than 1 g/cm^3.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Hydrocarbons are non-polar (densities ~0.6-0.8 g/cm^3) and do not dissolve in polar water, floating as an immiscible layer on top."),

    ("State whether the following statement is True or False: An alkyne with 4 carbon atoms has the molecular formula C4H8.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Using C_n H_{2n-2} with n=4: C4 H_{2(4)-2} = C4H6 (C4H8 is an alkene)."),

    ("What is the total number of single covalent bonds in a propane (C3H8) molecule?",
     ["10 single covalent bonds (2 C-C bonds and 8 C-H bonds)", "8 bonds", "11 bonds", "9 bonds"],
     "A", "OSC", "easy",
     "Propane contains 2 carbon-carbon single bonds and 8 carbon-hydrogen single bonds, totaling 2 + 8 = 10 covalent bonds."),

    ("What is the total number of covalent bonds in a cyclobutane (C4H8) ring molecule?",
     ["12 covalent bonds (4 C-C ring bonds and 8 C-H bonds)", "8 bonds", "10 bonds", "14 bonds"],
     "A", "OSC", "medium",
     "Cyclobutane has a closed square ring of 4 C-C single bonds plus 8 peripheral C-H bonds, totaling 12 covalent bonds."),

    ("What chemical product is formed when ethene reacts with steam in the presence of phosphoric acid catalyst at high pressure?",
     ["Ethanol (ethyl alcohol, C2H5OH)", "Methanol", "Ethanoic acid", "Diethyl ether"],
     "A", "OSC", "medium",
     "Hydration of ethene: C2H4 + H2O -> C2H5OH, adding H and OH across the double bond to manufacture industrial ethanol."),

    ("Why does an oil spill on the ocean surface spread rapidly into a thin film rather than dissolving?",
     ["Hydrocarbons in petroleum are non-polar and hydrophobic, possessing lower density than seawater and low surface tension",
      "Oil reacts with seawater to form solid rock",
      "Oil boils at ocean temperatures",
      "Seawater freezes petroleum into ice"],
     "A", "OSC", "easy",
     "Non-polar petroleum hydrocarbons do not mix with polar water; having a density ~0.85 g/cm^3, oil spreads across the surface as an environmental slick."),

    ("What type of bond is broken when an alkene undergoes an addition reaction?",
     ["The weaker pi (pi) bond of the double bond breaks, while the stronger sigma (sigma) bond remains intact",
      "All bonds in the molecule shatter completely",
      "Only C-H bonds break",
      "The nucleus splits"],
     "A", "OSC", "medium",
     "A double bond consists of one strong sigma bond and one weaker pi bond. In addition reactions, the exposed pi-bond breaks to form two new single sigma bonds."),

    ("What is the molecular geometry around the central carbon atoms in an ethene (C2H4) molecule?",
     ["Trigonal planar with bond angles of approximately 120 degrees",
      "Regular tetrahedral with 109.5 degrees",
      "Linear with 180 degrees",
      "Square planar with 90 degrees"],
     "A", "OSC", "easy",
     "Sp2 hybridization dictates trigonal planar electron geometry with ~120 deg bond angles."),

    ("What is the ratio of carbon to hydrogen atoms in an ethyne (acetylene, C2H2) molecule?",
     ["1 to 1 (empirical formula CH)", "1 to 2", "1 to 4", "2 to 3"],
     "A", "OSC", "easy",
     "C2H2 has two carbon atoms and two hydrogen atoms, giving a 1:1 atomic ratio.")
]

# 12 Mock Questions with Vector SVG Diagrams
mock_data = [
    # 71: Saturated vs Unsaturated Structural Distinction
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="200" viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="200" fill="#0f172a" rx="8"/>
  <!-- Box 1: Saturated (Ethane) -->
  <rect x="20" y="30" width="140" height="130" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
  <text x="30" y="50" fill="#38bdf8" font-size="10" font-weight="bold">Saturated (Alkane)</text>
  <text x="30" y="70" fill="#cbd5e1" font-size="8">Ethane: C2H6</text>
  <text x="50" y="105" fill="#facc15" font-size="11" font-weight="bold">H3C — CH3</text>
  <text x="30" y="130" fill="#94a3b8" font-size="8">- Single C-C sigma bond</text>
  <text x="30" y="145" fill="#4ade80" font-size="8">- Clean blue flame</text>
  <!-- Box 2: Unsaturated (Ethene & Ethyne) -->
  <rect x="180" y="30" width="140" height="130" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5" rx="4"/>
  <text x="190" y="50" fill="#fda4af" font-size="10" font-weight="bold">Unsaturated</text>
  <text x="190" y="70" fill="#cbd5e1" font-size="8">Ethene: C2H4 | Ethyne: C2H2</text>
  <text x="210" y="98" fill="#facc15" font-size="11" font-weight="bold">H2C = CH2</text>
  <text x="215" y="118" fill="#facc15" font-size="11" font-weight="bold">HC # CH</text>
  <text x="190" y="140" fill="#94a3b8" font-size="8">- Double/triple pi-bonds</text>
  <text x="190" y="152" fill="#ef4444" font-size="8">- Sooty yellow flame</text>
  <text x="35" y="180" fill="#fde68a" font-size="9">Fundamental Classification: Saturated vs Unsaturated Hydrocarbons</text>
</svg>
</div>
What structural characteristic fundamentally defines an unsaturated hydrocarbon compared to a saturated hydrocarbon?""",
     ["The presence of at least one carbon-carbon double bond (C=C) or triple bond (C#C)""",
     "The presence of oxygen atoms""",
     "Having more hydrogen atoms than carbon atoms""",
     "Being solid at room temperature"],
     "A", "easy""",
     "Saturated hydrocarbons have exclusively single C-C bonds with maximum hydrogen saturation; unsaturated hydrocarbons contain multiple bonds (double or triple) with reactive pi-electrons."),

    # 72: Bromine Water Decolourization Test
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Tube 1: Saturated (Ethane + Br2) -->
  <rect x="45" y="45" width="40" height="95" fill="#b45309" opacity="0.8" stroke="#f59e0b" stroke-width="1.5" rx="3"/>
  <text x="35" y="35" fill="#f59e0b" font-size="8" font-weight="bold">Ethane (C2H6)</text>
  <text x="30" y="155" fill="#cbd5e1" font-size="8">Remains Reddish-Brown</text>
  <text x="35" y="170" fill="#f87171" font-size="8">No Reaction (Dark)</text>
  <!-- Tube 2: Unsaturated (Ethene + Br2) -->
  <rect x="215" y="45" width="40" height="95" fill="#38bdf8" opacity="0.15" stroke="#38bdf8" stroke-width="1.5" rx="3"/>
  <text x="205" y="35" fill="#38bdf8" font-size="8" font-weight="bold">Ethene (C2H4)</text>
  <text x="195" y="155" fill="#38bdf8" font-size="8" font-weight="bold">Colour Discharged!</text>
  <text x="190" y="170" fill="#4ade80" font-size="8">Colorless 1,2-dibromoethane</text>
  <!-- Addition equation in middle -->
  <text x="100" y="80" fill="#facc15" font-size="9" font-weight="bold">+ Br2 water</text>
  <line x1="105" y1="90" x2="195" y2="90" stroke="#facc15" stroke-width="2"/>
  <polygon points="195,86 205,90 195,94" fill="#facc15"/>
  <text x="95" y="110" fill="#a7f3d0" font-size="8">Addition across C=C</text>
</svg>
</div>
The diagram shows the bromine water unsaturation test. Why does ethene rapidly discharge the reddish-brown color of bromine water while ethane produces no color change?""",
     ["Ethene undergoes an addition reaction across its C=C double bond to form colorless 1,2-dibromoethane, while saturated ethane cannot add bromine""",
     "Ethane absorbs bromine without changing color""",
     "Ethene turns bromine into pure water""",
     "Bromine evaporates instantly in ethene gas"],
     "A", "medium""",
     "The reactive pi-bond in ethene opens to add two bromine atoms: H2C=CH2 + Br2 -> CH2Br-CH2Br (colorless), completely decolourising the reddish-brown test solution."),

    # 73: Catalytic Hydrogenation of Vegetable Oil to Ghee
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Reactant: Liquid Vegetable Oil -->
  <rect x="20" y="45" width="100" height="65" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" rx="4"/>
  <text x="25" y="65" fill="#fde68a" font-size="8" font-weight="bold">Vegetable Oil (Liquid)</text>
  <text x="25" y="82" fill="#cbd5e1" font-size="8">Unsaturated (C=C)</text>
  <text x="25" y="98" fill="#4ade80" font-size="7">Healthy cis-bonds</text>
  <!-- Hydrogenation conditions arrow -->
  <line x1="125" y1="78" x2="210" y2="78" stroke="#facc15" stroke-width="2.5"/>
  <polygon points="210,74 220,78 210,82" fill="#facc15"/>
  <text x="135" y="62" fill="#38bdf8" font-size="8" font-weight="bold">+ H2 Gas (60^{\circ}C)</text>
  <text x="140" y="95" fill="#fde68a" font-size="8">Ni Catalyst</text>
  <!-- Product: Solid Vanaspati Ghee -->
  <rect x="225" y="45" width="100" height="65" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
  <text x="230" y="65" fill="#38bdf8" font-size="8" font-weight="bold">Vanaspati Ghee (Solid)</text>
  <text x="230" y="82" fill="#cbd5e1" font-size="8">Saturated (C-C)</text>
  <text x="230" y="98" fill="#f87171" font-size="7">High melting point</text>
  <!-- Reaction summary equation -->
  <text x="35" y="150" fill="#facc15" font-size="9">R-CH=CH-R' + H2 --(Ni, 60^{\circ}C)--> R-CH2-CH2-R'</text>
  <text x="35" y="175" fill="#a7f3d0" font-size="8">Addition of hydrogen saturates double bonds, converting liquid oil into solid fat</text>
</svg>
</div>
What chemical transformation occurs during the industrial manufacture of vanaspati ghee from vegetable oil?""",
     ["Catalytic addition of hydrogen across carbon-carbon double bonds converts unsaturated liquid oil into saturated solid fat""",
     "Oxidation of vegetable oil with ozone gas""",
     "Dehydration of oil to remove water molecules""",
     "Thermal cracking of oil into methane"],
     "A", "easy""",
     "Hydrogen gas bubbled through liquid oil at 60 deg C with a nickel catalyst saturates C=C double bonds into C-C single bonds, packing hydrocarbon chains into solid fat."),

    # 74: Oxy-Acetylene Welding Torch
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Torch body -->
  <rect x="40" y="70" width="100" height="25" fill="#475569" rx="3"/>
  <!-- Two gas inlet tubes -->
  <line x1="15" y1="75" x2="40" y2="75" stroke="#ef4444" stroke-width="3"/>
  <text x="5" y="68" fill="#ef4444" font-size="8">Acetylene (C2H2)</text>
  <line x1="15" y1="90" x2="40" y2="90" stroke="#38bdf8" stroke-width="3"/>
  <text x="15" y="105" fill="#38bdf8" font-size="8">Oxygen (O2)</text>
  <!-- Torch nozzle -->
  <polygon points="140,75 170,82 140,90" fill="#94a3b8"/>
  <!-- Super hot flame cone (>3300 deg C) -->
  <polygon points="170,82 220,72 250,82 220,92" fill="#facc15"/>
  <polygon points="170,82 200,77 215,82 200,87" fill="#67e8f9"/>
  <text x="185" y="60" fill="#67e8f9" font-size="9" font-weight="bold">Inner Cone: >3300^{\circ}C</text>
  <!-- Steel plate being welded -->
  <rect x="255" y="60" width="15" height="50" fill="#94a3b8"/>
  <rect x="270" y="60" width="15" height="50" fill="#94a3b8"/>
  <circle cx="262" cy="85" r="5" fill="#ef4444"/>
  <text x="245" y="125" fill="#fde68a" font-size="8">Molten Steel Weld</text>
  <text x="35" y="160" fill="#facc15" font-size="9">2 C2H2 (g) + 5 O2 (g) \rightarrow 4 CO2 (g) + 2 H2O (g) + Heat (Huge \Delta H)</text>
  <text x="35" y="175" fill="#cbd5e1" font-size="8">Acetylene burns in pure oxygen with extreme calorific intensity to weld metals</text>
</svg>
</div>
Why is ethyne (acetylene) standardly chosen over methane or ethane for industrial metal welding and cutting torches?""",
     ["Combustion of ethyne in pure oxygen generates temperatures exceeding 3300 deg C, hot enough to melt structural steel instantaneously""",
     "Acetylene flame is cold and does not burn skin""",
     "Acetylene makes metals magnetic""",
     "Acetylene produces zero light"],
     "A", "medium""",
     "The high enthalpy of the carbon-carbon triple bond releases immense energy upon combustion in pure oxygen, generating a flame temperature over 3300 deg C."),

    # 75: Methane Substitution Reaction Series
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Title -->
  <text x="45" y="25" fill="#38bdf8" font-size="10" font-weight="bold">Stepwise Photochemical Chlorination of Methane</text>
  <!-- Step 1 -->
  <rect x="20" y="40" width="295" height="25" fill="#1e293b" rx="3"/>
  <text x="25" y="56" fill="#fde68a" font-size="8">CH4 + Cl2 --(h\nu)--> CH3Cl (Chloromethane) + HCl</text>
  <!-- Step 2 -->
  <rect x="20" y="70" width="295" height="25" fill="#1e293b" rx="3"/>
  <text x="25" y="86" fill="#fde68a" font-size="8">CH3Cl + Cl2 --(h\nu)--> CH2Cl2 (Dichloromethane) + HCl</text>
  <!-- Step 3 -->
  <rect x="20" y="100" width="295" height="25" fill="#1e293b" rx="3"/>
  <text x="25" y="116" fill="#fde68a" font-size="8">CH2Cl2 + Cl2 --(h\nu)--> CHCl3 (Chloroform) + HCl</text>
  <!-- Step 4 -->
  <rect x="20" y="130" width="295" height="25" fill="#1e293b" rx="3"/>
  <text x="25" y="146" fill="#4ade80" font-size="8" font-weight="bold">CHCl3 + Cl2 --(h\nu)--> CCl4 (Carbon Tetrachloride) + HCl</text>
  <text x="35" y="175" fill="#38bdf8" font-size="8">Each step replaces one H atom with one Cl atom (Substitution Reaction)</text>
</svg>
</div>
What type of chemical reaction is represented by the chlorination of methane in diffused sunlight?""",
     ["Substitution reaction: chlorine radicals progressively displace hydrogen atoms from the saturated alkane""",
     "Addition reaction across double bonds""",
     "Combustion reaction producing CO2""",
     "Neutralization reaction forming salts"],
     "A", "easy""",
     "Because saturated methane has no multiple bonds, chlorine atoms substitute for hydrogens one by one, forming chloromethane, dichloromethane, chloroform, and carbon tetrachloride."),

    # 76: Molecular Geometry Comparison: Sp3, Sp2, Sp
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Column 1: Ethane (sp3) -->
  <rect x="20" y="30" width="95" height="120" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="30" y="50" fill="#38bdf8" font-size="9" font-weight="bold">Ethane (C2H6)</text>
  <text x="30" y="70" fill="#cbd5e1" font-size="8">- sp3 Hybrid</text>
  <text x="30" y="85" fill="#cbd5e1" font-size="8">- Tetrahedral</text>
  <text x="30" y="100" fill="#facc15" font-size="8">- 109.5^{\circ} angle</text>
  <text x="30" y="120" fill="#4ade80" font-size="8">Single C-C</text>
  <!-- Column 2: Ethene (sp2) -->
  <rect x="122" y="30" width="95" height="120" fill="#1e293b" stroke="#4ade80" rx="3"/>
  <text x="130" y="50" fill="#4ade80" font-size="9" font-weight="bold">Ethene (C2H4)</text>
  <text x="130" y="70" fill="#cbd5e1" font-size="8">- sp2 Hybrid</text>
  <text x="130" y="85" fill="#cbd5e1" font-size="8">- Trigonal Planar</text>
  <text x="130" y="100" fill="#facc15" font-size="8">- 120^{\circ} angle</text>
  <text x="130" y="120" fill="#4ade80" font-size="8">Double C=C</text>
  <!-- Column 3: Ethyne (sp) -->
  <rect x="225" y="30" width="95" height="120" fill="#1e293b" stroke="#f43f5e" rx="3"/>
  <text x="235" y="50" fill="#fda4af" font-size="9" font-weight="bold">Ethyne (C2H2)</text>
  <text x="235" y="70" fill="#cbd5e1" font-size="8">- sp Hybrid</text>
  <text x="235" y="85" fill="#cbd5e1" font-size="8">- Linear shape</text>
  <text x="235" y="100" fill="#facc15" font-size="8">- 180^{\circ} angle</text>
  <text x="235" y="120" fill="#4ade80" font-size="8">Triple C#C</text>
  <text x="35" y="170" fill="#fde68a" font-size="9">Bond Order Influences Hybridization, Geometry, and Bond Angle</text>
</svg>
</div>
What molecular geometry and bond angle characterize an ethyne (acetylene, C2H2) molecule?""",
     ["Linear geometry with bond angles of 180 degrees""",
     "Tetrahedral geometry with bond angles of 109.5 degrees""",
     "Trigonal planar geometry with bond angles of 120 degrees""",
     "Square planar geometry with bond angles of 90 degrees"],
     "A", "medium""",
     "The carbon atoms in ethyne are sp-hybridized, arranging the sigma bonds at maximum separation of 180 degrees in a collinear linear geometry (H-C#C-H)."),

    # 77: Polyethylene Polymerization Mechanism
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Multiple Ethene monomers -->
  <rect x="30" y="45" width="80" height="40" fill="#1e293b" stroke="#4ade80" rx="3"/>
  <text x="35" y="68" fill="#4ade80" font-size="10" font-weight="bold">n (CH2=CH2)</text>
  <text x="35" y="100" fill="#94a3b8" font-size="8">Ethene Monomer</text>
  <!-- Polymerization arrow with catalyst -->
  <line x1="120" y1="65" x2="190" y2="65" stroke="#facc15" stroke-width="2.5"/>
  <polygon points="190,61 200,65 190,69" fill="#facc15"/>
  <text x="130" y="55" fill="#facc15" font-size="8">High Pressure</text>
  <text x="135" y="80" fill="#facc15" font-size="8">Catalyst</text>
  <!-- Polyethylene polymer chain -->
  <rect x="210" y="45" width="100" height="40" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="215" y="68" fill="#38bdf8" font-size="10" font-weight="bold">[-CH2-CH2-]_n</text>
  <text x="215" y="100" fill="#94a3b8" font-size="8">Polyethylene (Polythene)</text>
  <!-- Applications below -->
  <text x="45" y="145" fill="#fde68a" font-size="9">Addition Polymerization of Ethene</text>
  <text x="45" y="165" fill="#cbd5e1" font-size="8">Double bonds open up to link thousands of units into plastic bags, bottles, and pipes</text>
</svg>
</div>
What happens to the double bonds of ethene molecules during the industrial manufacture of polyethylene plastic?""",
     ["The pi-bonds open up and link with adjacent ethene molecules to form long, saturated continuous polymer chains""",
     "The double bonds turn into triple bonds""",
     "The carbon atoms disintegrate into gas""",
     "The molecules dissolve in water"],
     "A", "easy""",
     "Under catalytic pressure, the double bond in each monomer opens to form single covalent bonds with adjacent units, producing high-molecular-weight polyethylene."),

    # 78: Fruit Ripening Ethylene Action
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="180" viewBox="0 0 340 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="180" fill="#0f172a" rx="8"/>
  <!-- Green unripe banana -->
  <path d="M 50 110 Q 75 55 120 75 Q 85 85 50 110 Z" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
  <text x="40" y="135" fill="#4ade80" font-size="8">Unripe (Hard/Sour)</text>
  <!-- Ethylene gas vapor arrow -->
  <line x1="125" y1="85" x2="195" y2="85" stroke="#facc15" stroke-width="2"/>
  <polygon points="195,81 205,85 195,89" fill="#facc15"/>
  <text x="135" y="75" fill="#facc15" font-size="9" font-weight="bold">+ C2H4 Gas</text>
  <text x="130" y="105" fill="#fde68a" font-size="8">(Plant Hormone)</text>
  <!-- Yellow ripe banana -->
  <path d="M 215 110 Q 240 55 285 75 Q 250 85 215 110 Z" fill="#facc15" stroke="#eab308" stroke-width="2"/>
  <text x="210" y="135" fill="#fde68a" font-size="8">Ripe (Soft/Sweet)</text>
  <text x="45" y="25" fill="#38bdf8" font-size="10" font-weight="bold">Ethylene (C2H4): Gaseous Phytohormone for Fruit Ripening</text>
  <text x="45" y="165" fill="#cbd5e1" font-size="8">Triggers starch conversion to sugars, softening of pectin, and color change</text>
</svg>
</div>
Which gaseous hydrocarbon acts as a natural plant hormone to trigger the ripening and sweetening of harvested fruits?""",
     ["Ethene (ethylene, C2H4)", "Methane (CH4)", "Ethane (C2H6)", "Acetylene (C2H2)"],
     "A", "easy""",
     "Ethylene is a natural botanical gaseous hormone regulating senescence and fruit ripening, breaking down acids and starches into sugars."),

    # 79: Comparison of Melting Points of Saturated vs Unsaturated Fats
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Saturated Fat straight chains -->
  <rect x="25" y="30" width="135" height="110" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5" rx="4"/>
  <text x="35" y="50" fill="#fda4af" font-size="9" font-weight="bold">Saturated Fat (Butter)</text>
  <line x1="35" y1="70" x2="140" y2="70" stroke="#f43f5e" stroke-width="2"/>
  <line x1="35" y1="85" x2="140" y2="85" stroke="#f43f5e" stroke-width="2"/>
  <text x="35" y="105" fill="#cbd5e1" font-size="8">Straight chains pack tightly</text>
  <text x="35" y="125" fill="#f87171" font-size="8" font-weight="bold">Solid at room temp</text>
  <!-- Unsaturated Oil kinked chains -->
  <rect x="180" y="30" width="135" height="110" fill="#1e293b" stroke="#4ade80" stroke-width="1.5" rx="4"/>
  <text x="190" y="50" fill="#4ade80" font-size="9" font-weight="bold">Unsaturated (Veg Oil)</text>
  <!-- Kinked chain path -->
  <path d="M 190 70 L 230 70 L 250 85 L 290 85" stroke="#4ade80" stroke-width="2" fill="none"/>
  <path d="M 190 90 L 220 90 L 240 105 L 280 105" stroke="#4ade80" stroke-width="2" fill="none"/>
  <text x="190" y="125" fill="#34d399" font-size="8" font-weight="bold">Liquid at room temp</text>
  <text x="45" y="165" fill="#facc15" font-size="9">Cis double bonds create structural kinks that prevent close packing</text>
</svg>
</div>
Why are unsaturated vegetable oils liquid at room temperature whereas saturated animal fats (like butter) are solid?""",
     ["Cis-double bonds in unsaturated oils create kinks in fatty acid chains that prevent tight molecular packing, lowering their melting points""",
     "Unsaturated oils are made of liquid nitrogen""",
     "Saturated fats contain metallic iron""",
     "Vegetable oils contain boiling water"],
     "A", "medium""",
     "Rigid cis C=C kinks disrupt close parallel alignment of hydrocarbon chains, weakening intermolecular van der Waals forces and lowering the melting point below room temperature."),

    # 80: Natural Gas vs LPG Hydrocarbon Composition
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="180" viewBox="0 0 340 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="180" fill="#0f172a" rx="8"/>
  <!-- Box 1: CNG / PNG -->
  <rect x="25" y="30" width="135" height="110" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
  <text x="35" y="50" fill="#38bdf8" font-size="10" font-weight="bold">CNG / Natural Gas</text>
  <text x="35" y="75" fill="#fde68a" font-size="9" font-weight="bold">>90% Methane (CH4)</text>
  <text x="35" y="95" fill="#cbd5e1" font-size="8">- Lightest gas (C1)</text>
  <text x="35" y="110" fill="#cbd5e1" font-size="8">- High auto-ignition temp</text>
  <text x="35" y="125" fill="#4ade80" font-size="8">- Very clean burning</text>
  <!-- Box 2: LPG -->
  <rect x="180" y="30" width="135" height="110" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" rx="4"/>
  <text x="190" y="50" fill="#fbbf24" font-size="10" font-weight="bold">LPG (Cylinder)</text>
  <text x="190" y="75" fill="#fde68a" font-size="9" font-weight="bold">Propane + Butane</text>
  <text x="190" y="95" fill="#cbd5e1" font-size="8">- C3H8 + C4H10</text>
  <text x="190" y="110" fill="#cbd5e1" font-size="8">- Liquefies under pressure</text>
  <text x="190" y="125" fill="#ef4444" font-size="8">- + Ethanethiol odorant</text>
  <text x="45" y="165" fill="#facc15" font-size="9">Two Dominant Commercial Hydrocarbon Fuel Supplies</text>
</svg>
</div>
What are the primary hydrocarbon chemical constituents of domestic LPG cylinders versus CNG vehicle fuel?""",
     ["LPG consists mainly of propane (C3H8) and butane (C4H10), whereas CNG consists predominantly of methane (CH4)""",
     "LPG is pure hydrogen and CNG is pure carbon dioxide""",
     "LPG is acetylene and CNG is ethylene""",
     "LPG is solid coal and CNG is liquid petroleum"],
     "A", "easy""",
     "LPG consists of easily liquefied C3 and C4 alkanes (propane/butane), while CNG is compressed natural gas composed of over 90% C1 methane."),

    # 81: Baeyer's Alkaline KMnO4 Oxidation Test
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Tube 1: Alkaline KMnO4 initial purple -->
  <rect x="50" y="45" width="40" height="90" fill="#86198f" opacity="0.8" stroke="#c026d3" stroke-width="1.5" rx="3"/>
  <text x="40" y="35" fill="#e879f9" font-size="8">Purple KMnO4</text>
  <!-- Arrow with ethene gas -->
  <line x1="110" y1="90" x2="190" y2="90" stroke="#facc15" stroke-width="2.5"/>
  <polygon points="190,86 200,90 190,94" fill="#facc15"/>
  <text x="115" y="75" fill="#facc15" font-size="9" font-weight="bold">+ Ethene (C2H4)</text>
  <!-- Tube 2: Decolourized with brown MnO2 precipitate -->
  <rect x="220" y="45" width="40" height="90" fill="#38bdf8" opacity="0.15" stroke="#38bdf8" stroke-width="1.5" rx="3"/>
  <circle cx="240" cy="120" r="8" fill="#78350f"/>
  <text x="210" y="35" fill="#38bdf8" font-size="8" font-weight="bold">Decolourized</text>
  <text x="210" y="150" fill="#d97706" font-size="7">Brown MnO2 ppt</text>
  <text x="35" y="170" fill="#fde68a" font-size="9">Baeyer's Test: 3 C2H4 + 2 KMnO4 + 4 H2O \rightarrow 3 C2H4(OH)2 + 2 MnO2 \downarrow</text>
</svg>
</div>
What visible change occurs during Baeyer's test when an unsaturated alkene reacts with alkaline potassium permanganate solution?""",
     ["The intense purple color of KMnO4 disappears and a brown precipitate of manganese dioxide (MnO2) forms""",
     "The solution turns bright orange""",
     "The liquid turns into solid black coal""",
     "The solution starts bubbling pure oxygen"],
     "A", "medium""",
     "Alkaline KMnO4 oxidizes the alkene double bond into a diol (glycol), reducing purple permanganate ions to brown insoluble manganese dioxide (MnO2)."),

    # 82: Alkanes Insoluble in Water (Hydrophobic Layer)
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Beaker containing two liquid layers -->
  <rect x="100" y="40" width="140" height="110" fill="#1e293b" stroke="#94a3b8" stroke-width="2" rx="4"/>
  <!-- Top Layer: Liquid Alkane (Hexane/Oil) -->
  <rect x="100" y="55" width="140" height="40" fill="#facc15" opacity="0.4"/>
  <text x="110" y="78" fill="#fde68a" font-size="9" font-weight="bold">Liquid Alkane (Hexane / Oil)</text>
  <text x="110" y="90" fill="#fde68a" font-size="8">Density ~0.66 g/cm^3 (Floats)</text>
  <!-- Meniscus line -->
  <line x1="100" y1="95" x2="240" y2="95" stroke="#38bdf8" stroke-width="2"/>
  <!-- Bottom Layer: Water -->
  <rect x="100" y="95" width="140" height="55" fill="#0284c7" opacity="0.3"/>
  <text x="120" y="125" fill="#38bdf8" font-size="9" font-weight="bold">Water (H2O)</text>
  <text x="120" y="140" fill="#38bdf8" font-size="8">Density = 1.0 g/cm^3</text>
  <text x="45" y="25" fill="#facc15" font-size="10" font-weight="bold">Like Dissolves Like: Immiscibility of Non-Polar Hydrocarbons</text>
  <text x="45" y="175" fill="#cbd5e1" font-size="8">Non-polar C-H bonds cannot form hydrogen bonds with polar water molecules</text>
</svg>
</div>
Why are liquid hydrocarbons like hexane and kerosene completely immiscible with water and float on top as a separate layer?""",
     ["Hydrocarbons are non-polar hydrophobic molecules that cannot form hydrogen bonds with polar water, and having densities less than 1.0 g/cm^3, they float on top""",
     "Hydrocarbons are denser than water and sink to the bottom""",
     "Hydrocarbons boil instantly when touching water""",
     "Hydrocarbons turn water into acidic vinegar"],
     "A", "easy""",
     "The 'like dissolves like' rule applies: non-polar hydrocarbons cannot disrupt hydrogen bonding in polar water, remaining immiscible and floating due to lower density (~0.7 g/cm^3).")
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

    out_file = "scripts/ch13_topic4.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {TOPIC_CODE} -> {out_file}")

if __name__ == "__main__":
    generate()
