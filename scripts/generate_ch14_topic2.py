# scripts/generate_ch14_topic2.py
# MH-9-SCIT-14-14.2: Bleaching Powder (CaOCl2) & Plaster of Paris (CaSO4·1/2H2O)
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-14-14.2"

exam_data = [
    # 1-10: Bleaching Powder: Preparation & Formula
    ("What is the chemical name and molecular formula of bleaching powder?""",
     ["Calcium hypochlorite / Calcium oxychloride (CaOCl2)",
      "Calcium chloride dihydrate (CaCl2.2H2O)",
      "Calcium carbonate (CaCO3)",
      "Calcium hydroxide (Ca(OH)2)"],
     "A", "OSC", "easy",
     "Bleaching powder is chemically known as calcium oxychloride or calcium hypochlorite, with the molecular formula CaOCl2."),

    ("How is bleaching powder manufactured industrially?""",
     ["By passing chlorine gas (Cl2) over dry slaked lime (Ca(OH)2) at 40 degrees Celsius",
      "By reacting calcium metal with concentrated hydrochloric acid",
      "By heating limestone (CaCO3) in a lime kiln",
      "By dissolving quicklime in liquid ammonia"],
     "A", "OSC", "easy",
     "Bleaching powder is produced by passing dry chlorine gas over slaked lime: Ca(OH)2 + Cl2 -> CaOCl2 + H2O."),

    ("Why does bleaching powder always smell distinctly of chlorine even when stored in a container?""",
     ["It slowly reacts with carbon dioxide (CO2) from atmospheric moisture to liberate chlorine gas",
      "It is mixed with pure liquid chlorine",
      "Chlorine gas is trapped inside the crystal without any chemical bond",
      "It decomposes only when exposed to strong sunlight"],
     "A", "OSC", "easy",
     "Bleaching powder slowly reacts with atmospheric carbon dioxide: CaOCl2 + CO2 -> CaCO3 + Cl2, releasing chlorine gas."),

    ("What gas is evolved when bleaching powder reacts with dilute sulfuric acid (H2SO4) or dilute hydrochloric acid (HCl)?""",
     ["Chlorine gas (Cl2)", "Hydrogen gas (H2)", "Carbon dioxide gas (CO2)", "Oxygen gas (O2)"],
     "A", "OSC", "easy",
     "Dilute mineral acids react with bleaching powder to liberate chlorine gas: CaOCl2 + H2SO4 -> CaSO4 + H2O + Cl2."),

    ("What is meant by the 'available chlorine' of a sample of bleaching powder?""",
     ["The percentage by mass of chlorine liberated when treated with excess dilute acid",
      "The total amount of calcium present in the sample",
      "The mass of water vapor absorbed from the atmosphere",
      "The percentage of unreacted slaked lime remaining"],
     "A", "OSC", "medium",
     "Available chlorine indicates the bleaching and sterilizing power of the powder, measured as the percentage of chlorine liberated on reaction with acid."),

    ("Why does chlorine gas liberated from bleaching powder act as an effective bleaching and sterilizing agent?""",
     ["It oxidizes colored organic substances to colorless compounds through nascent oxygen produced in the presence of moisture",
      "It dissolves the cotton fabric fibers completely",
      "It freezes water molecules to trap bacteria",
      "It converts colored dyes into radioactive isotopes"],
     "A", "OSC", "medium",
     "Chlorine reacts with water to form unstable hypochlorous acid (HOCl), which decomposes releasing nascent oxygen [O] that bleaches colored matter by oxidation."),

    ("Which of the following is a major industrial use of bleaching powder?""",
     ["Bleaching wood pulp in paper factories and linen in textile mills",
      "Manufacturing automobile tires",
      "Fueling rockets and jet engines",
      "Extracting aluminium metal from bauxite"],
     "A", "OSC", "easy",
     "Bleaching powder is widely used for bleaching wood pulp in the paper industry and cotton/linen in textile manufacturing."),

    ("Why is bleaching powder routinely added to drinking water supplies and swimming pools?""",
     ["To act as a powerful disinfectant and germicide that kills pathogenic microorganisms",
      "To increase the sweetness of tap water",
      "To soften hard water by removing calcium ions",
      "To impart a bright yellow color to water"],
     "A", "OSC", "easy",
     "The nascent oxygen and hypochlorite ions released by bleaching powder destroy bacteria, viruses, and microbial pathogens, sterilizing drinking water."),

    ("What happens when bleaching powder is left exposed to open humid air for a prolonged period?""",
     ["It undergoes slow carbonation, loses its chlorine content, and turns into useless calcium carbonate",
      "It catches fire spontaneously",
      "It transforms into pure solid calcium metal",
      "It turns into liquid baking soda"],
     "A", "OSC", "medium",
     "Continuous exposure to humid air causes CaOCl2 to react with atmospheric CO2, gradually liberating all available chlorine and leaving behind inert CaCO3."),

    ("State whether the following statement is True or False: Bleaching powder is completely soluble in cold water without leaving any residue.",
     ["True", "False"],
     "B", "OTF", "easy",
     "Bleaching powder is only partially soluble in water; unreacted calcium hydroxide (slaked lime) remains behind as an insoluble white suspension."),

    # 11-20: Plaster of Paris: Formula, Preparation & History
    ("What is the chemical formula of Plaster of Paris (POP)?""",
     ["CaSO4.1/2H2O (Calcium sulfate hemihydrate)",
      "CaSO4.2H2O (Calcium sulfate dihydrate)",
      "CaSO4 (Anhydrous calcium sulfate)",
      "CaCO3.1/2H2O"],
     "A", "OSC", "easy",
     "Plaster of Paris is calcium sulfate hemihydrate, CaSO4.1/2H2O, containing half a molecule of water of crystallization per CaSO4 formula unit."),

    ("From which naturally occurring mineral is Plaster of Paris manufactured?""",
     ["Gypsum (CaSO4.2H2O)", "Limestone (CaCO3)", "Dolomite (CaCO3.MgCO3)", "Fluorite (CaF2)"],
     "A", "OSC", "easy",
     "Plaster of Paris is manufactured by carefully heating mineral gypsum (calcium sulfate dihydrate, CaSO4.2H2O)."),

    ("At what temperature must gypsum be heated to produce Plaster of Paris without destroying its setting property?""",
     ["100 degrees Celsius (373 K)",
      "500 degrees Celsius (773 K)",
      "25 degrees Celsius (298 K)",
      "1000 degrees Celsius (1273 K)"],
     "A", "OSC", "easy",
     "Gypsum is heated at a controlled temperature of 100 degrees Celsius (373 K): CaSO4.2H2O -> CaSO4.1/2H2O + 1.5H2O."),

    ("Why is calcium sulfate hemihydrate commonly known as 'Plaster of Paris'?""",
     ["It was historically prepared in large quantities by burning rich gypsum deposits found in Montmartre, Paris",
      "It was first synthesized by French king Louis XIV",
      "It can only be manufactured inside laboratories in France",
      "It smells like perfumes made in Paris"],
     "A", "OSC", "easy",
     "It earned the name Plaster of Paris because large deposits of high-grade gypsum were first quarried at Montmartre in Paris to produce this building plaster."),

    ("What product is formed if gypsum is overheated above 200 degrees Celsius (473 K)?""",
     ["Dead burnt plaster (anhydrous CaSO4) which completely loses the property of setting with water",
      "Plaster of Paris with faster setting time",
      "Slaked lime and sulfur trioxide gas",
      "Pure calcium metal and sulfuric acid"],
     "A", "OSC", "medium",
     "Overheating gypsum above 200 degrees Celsius expels all water of crystallization, yielding dead burnt plaster (anhydrous CaSO4) which will not set upon adding water."),

    ("What remarkable physical transformation occurs when Plaster of Paris is mixed with water?""",
     ["It forms a moldable plastic paste that hydrates back into gypsum and hardens into a rigid solid mass within 10 to 15 minutes",
      "It dissolves into a clear liquid that never solidifies",
      "It explodes violently with the evolution of carbon dioxide",
      "It turns into liquid sulfuric acid"],
     "A", "OSC", "easy",
     "When mixed with water, POP reabsorbs water: CaSO4.1/2H2O + 1.5H2O -> CaSO4.2H2O (gypsum), crystallizing into an interlocking network of needle-shaped crystals."),

    ("Why does Plaster of Paris expand slightly upon setting, making it uniquely ideal for cast reproduction?""",
     ["The newly formed interlocking needle-like crystals of gypsum have a slightly larger molar volume than the original paste",
      "Air bubbles are permanently trapped inside the plaster",
      "The water boils and creates steam pressure",
      "Chemical decomposition produces nitrogen gas bubbles"],
     "A", "OSC", "medium",
     "During crystallization into gypsum, the interlocking crystal lattice expands slightly (approx 0.5%), filling fine mold details with great fidelity."),

    ("Which medical application relies heavily on Plaster of Paris bandages?""",
     ["Immobilizing fractured bones in orthopedic casts while they heal",
      "Disinfecting open surgical wounds",
      "Treating internal stomach ulcers",
      "Lowering high blood pressure in heart patients"],
     "A", "OSC", "easy",
     "POP bandages provide a rigid, custom-molded cast that immobilizes broken bones, keeping fragments aligned while bone tissue regenerates."),

    ("Which of the following is an architectural and artistic application of Plaster of Paris?""",
     ["Making decorative ceiling cornices, ornamental false ceilings, and sculpted idols/statues",
      "Manufacturing bulletproof glass windows",
      "Paving high-speed highway roads",
      "Constructing structural bridge pillars"],
     "A", "OSC", "easy",
     "Because POP can be poured into molds and replicates intricate patterns upon expanding slightly, it is used for decorative cornices, statues, and idols."),

    ("Why are environmental regulatory authorities increasingly urging the public to use clay (shadu mati) instead of POP idols for festival celebrations?""",
     ["POP is sparingly soluble in water, settles on riverbeds, and leaches toxic heavy metals from decorative paints, causing severe aquatic pollution",
      "POP dissolves instantly and turns river water acidic",
      "POP attracts sharks and harmful reptiles into rivers",
      "POP evaporates into the atmosphere and destroys the ozone layer"],
     "A", "OSC", "medium",
     "Gypsum from POP does not easily dissolve in water; immersed idols remain intact for months, silting riverbeds and smothering benthic aquatic life."),

    # 21-30: Alum, Water of Crystallization & Chemical Reactions
    ("What is the chemical formula of potash alum (fitkari)?""",
     ["K2SO4.Al2(SO4)3.24H2O", "FeSO4.7H2O", "CuSO4.5H2O", "Na2CO3.10H2O"],
     "A", "OSC", "easy",
     "Potash alum is a double sulfate hydrate of potassium and aluminium: K2SO4.Al2(SO4)3.24H2O."),

    ("Why is potash alum called a 'double salt' rather than a complex compound?""",
     ["It completely dissociates into simple constituent ions (K+, Al3+, SO4^2-) in aqueous solution and gives positive qualitative tests for each ion",
      "It contains two different types of water molecules",
      "It can only exist as two separate crystals in a container",
      "It has twice the density of common salt"],
     "A", "OSC", "medium",
     "Double salts dissociate completely into their individual constituent ions in solution: K2SO4.Al2(SO4)3.24H2O -> 2K+ + 2Al3+ + 4SO4^2- + 24H2O."),

    ("How does alum stop bleeding from minor shaving cuts and barber nicks?""",
     ["Al3+ ions coagulate and precipitate blood proteins (albumin), forming an immediate physical clot (astringent effect)",
      "Alum chemically burns and cauterizes the skin",
      "Alum numbs local sensory nerves to halt blood flow",
      "Alum oxidizes red blood cells into white cells"],
     "A", "OSC", "easy",
     "Alum acts as a styptic/astringent: positive Al3+ ions neutralize the negative charges on colloidal blood proteins, causing them to clot rapidly."),

    ("What is the role of gypsum (CaSO4.2H2O) when added in small amounts (2-3%) during cement manufacturing?""",
     ["It retards the initial setting time of cement, preventing it from flash-hardening too quickly so it can be mixed and applied",
      "It accelerates cement setting to less than 1 second",
      "It turns grey cement into white cement",
      "It reduces the total weight of the concrete slab"],
     "A", "OSC", "medium",
     "Gypsum slows down the hydration rate of tricalcium aluminate in clinker, preventing instant flash setting and allowing workers time to pour and finish concrete."),

    ("What happens to bleaching powder when treated with dilute carbon dioxide in water?""",
     ["It slowly precipitates calcium carbonate and releases chlorine: CaOCl2 + CO2 -> CaCO3 + Cl2",
      "It explodes violently",
      "It forms calcium bicarbonate solution with zero gas release",
      "It turns into liquid hydrochloric acid"],
     "A", "OSC", "medium",
     "Carbon dioxide displaces chlorine from calcium oxychloride, producing insoluble calcium carbonate and gaseous chlorine."),

    ("Assertion (A): Bleaching powder should always be stored in airtight containers kept in a cool, dry place.\nReason (R): In the presence of atmospheric carbon dioxide and moisture, it gradually decomposes and loses its available chlorine.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "medium",
     "Exposure to humid air and CO2 causes slow degradation into CaCO3 and Cl2 gas, degrading the available chlorine over time."),

    ("Assertion (A): The temperature during the manufacturing of Plaster of Paris from gypsum must not exceed 100 degrees Celsius (373 K).\nReason (R): Heating gypsum above 373 K removes all water of crystallization, yielding dead burnt plaster which has no setting properties.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "medium",
     "Controlled calcination at 373 K retains exactly 0.5 H2O per CaSO4. Higher temperatures drive off all water to form inert dead burnt plaster."),

    ("Which of the following salts contain water of crystallization in their formula unit?""",
     ["Copper sulfate pentahydrate, Potash alum, and Gypsum",
      "Dry sodium chloride, Potassium nitrate, and Ammonium chloride",
      "Calcium oxide, Sodium hydroxide, and Zinc chloride",
      "Magnesium oxide, Iron filings, and Carbon powder"],
     "A", "OSC", "easy",
     "CuSO4.5H2O (5 H2O), K2SO4.Al2(SO4)3.24H2O (24 H2O), and CaSO4.2H2O (2 H2O) all possess stoichiometric water of crystallization."),

    ("What is the molar ratio of water molecules to calcium sulfate formula units in Plaster of Paris versus Gypsum?""",
     ["Plaster of Paris has 1:2 (0.5 H2O per CaSO4) while Gypsum has 2:1 (2 H2O per CaSO4)",
      "Plaster of Paris has 2:1 while Gypsum has 1:2",
      "Both have 1:1 molar ratio",
      "Both have zero water molecules"],
     "A", "OSC", "medium",
     "In POP, two CaSO4 units share one molecule of water (2CaSO4.H2O or CaSO4.1/2H2O). In gypsum, each CaSO4 unit holds two water molecules (CaSO4.2H2O)."),

    ("State whether the following statement is True or False: Bleaching powder can act as both a disinfectant and an oxidizing agent.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Because it readily releases chlorine and nascent oxygen, bleaching powder is both a potent chemical oxidizer and a bactericidal disinfectant."),

    # 31-40: Fill in blanks, Numerical & Multi-choice
    ("Bleaching powder is chemically designated as ________.",
     ["calcium oxychloride", "sodium hypochlorite", "calcium hydroxide", "calcium chlorate"],
     "A", "OFB", "easy",
     "Bleaching powder is calcium oxychloride (CaOCl2)."),

    ("Gypsum on controlled heating at 373 K loses ________ molecules of water of crystallization per formula unit to form POP.",
     ["1.5 (one and a half)", "2.0 (two)", "0.5 (half)", "3.0 (three)"],
     "A", "OFB", "easy",
     "CaSO4.2H2O loses 1.5 molecules of water: CaSO4.2H2O -> CaSO4.1/2H2O + 1.5H2O."),

    ("The number of water molecules associated with each formula unit of potash alum is ________.",
     ["24", "10", "7", "5"],
     "A", "OFB", "easy",
     "Potash alum crystal contains 24 water molecules: K2SO4.Al2(SO4)3.24H2O."),

    ("How many grams of water are released when 1 mole of gypsum (172 g) is completely dehydrated into dead burnt plaster (136 g)?""",
     ["36 g", "18 g", "54 g", "72 g"],
     "A", "ONE", "medium",
     "One mole of CaSO4.2H2O contains 2 moles of water. Mass of 2 moles H2O = 2 * 18 g = 36 g."),

    ("A 100 g sample of gypsum is heated to 373 K to prepare Plaster of Paris. What theoretical percentage of mass is lost as steam? (Molar mass of gypsum = 172 g/mol, molar mass of 1.5 H2O = 27 g/mol)",
     ["15.7%", "25.0%", "31.4%", "50.0%"],
     "A", "ONE", "hard",
     "Theoretical mass loss = (27 / 172) * 100% = 15.698% \approx 15.7%."),

    ("Which of the following compounds undergo hydration reactions that lead to hardening or setting?""",
     ["Plaster of Paris and Portland cement",
      "Table salt and sugar",
      "Baking soda and vinegar",
      "Ammonium chloride and iodine"],
     "A", "OMC", "easy",
     "Both Plaster of Paris (rehydrating to gypsum) and Portland cement set and harden through exothermic hydration reactions."),

    ("Which of the following chemical reagents can liberate chlorine gas when treated with bleaching powder?""",
     ["Dilute hydrochloric acid (HCl) and dilute sulfuric acid (H2SO4)",
      "Sodium hydroxide solution and lime water",
      "Liquid ammonia and paraffin wax",
      "Pure distilled water and ethanol"],
     "A", "OMC", "medium",
     "Dilute mineral acids like HCl and H2SO4 immediately displace chlorine gas from bleaching powder."),

    ("Which substances among the following contain calcium as their primary metal cation?""",
     ["Bleaching powder, Plaster of Paris, and Gypsum",
      "Potash alum, Epsom salt, and Blue vitriol",
      "Washing soda, Baking soda, and Caustic soda",
      "Ammonium chloride, Sal ammoniac, and Urea"],
     "A", "OMC", "easy",
     "Bleaching powder (CaOCl2), POP (CaSO4.1/2H2O), and Gypsum (CaSO4.2H2O) all contain calcium (Ca2+) cations."),

    ("What is the oxidation state of the hypochlorite chlorine atom in bleaching powder (CaOCl2)?""",
     ["+1 in the hypochlorite ion (OCl-) and -1 in the chloride ion (Cl-)",
      "0 in both chlorine atoms",
      "+2 in both chlorine atoms",
      "-2 in both chlorine atoms"],
     "A", "OSC", "hard",
     "Bleaching powder is a mixed salt: Ca(OCl)Cl, where one chlorine has oxidation state -1 (chloride) and the other has +1 (hypochlorite)."),

    ("Why is bleaching powder used in the textile industry primarily for vegetable fibers like cotton and linen, but NOT for wool or natural silk?""",
     ["Chlorine and nascent oxygen attack and dissolve animal protein fibers (keratin/fibroin), degrading the fabric",
      "Wool is already completely white",
      "Bleaching powder turns silk into cotton",
      "Silk reacts with calcium to form an explosive compound"],
     "A", "OSC", "medium",
     "Animal fibers like wool and silk are proteins. Strong oxidizers like bleaching powder hydrolyze and damage protein amide bonds, so milder bleaching agents like H2O2 or SO2 are preferred.")
]

practice_data = [
    # 41-50: Practice on Bleaching Powder
    ("What is the balanced chemical equation for the production of bleaching powder from dry slaked lime?""",
     ["Ca(OH)2 + Cl2 -> CaOCl2 + H2O",
      "CaO + Cl2 -> CaOCl2",
      "CaCO3 + 2HCl -> CaCl2 + H2O + CO2",
      "Ca + Cl2 -> CaCl2"],
     "A", "OSC", "easy",
     "Chlorine gas reacting with solid slaked lime at moderate temperatures yields calcium oxychloride and water."),

    ("What is observed when a piece of colored litmus paper or flower petal is dipped into an aqueous suspension of bleaching powder?""",
     ["It gets permanently decolored / bleached to white",
      "It turns bright metallic green",
      "It becomes twice as intensely colored",
      "It dissolves into liquid carbon"],
     "A", "OSC", "easy",
     "The nascent oxygen [O] liberated oxidizes the organic chromophores of the dye, converting colored compounds into colorless derivatives."),

    ("Why must bleaching powder be dissolved in cold water rather than boiling hot water when preparing a sanitizing solution?""",
     ["Hot water accelerates thermal decomposition into calcium chloride and calcium chlorate, destroying bleaching capacity: 6CaOCl2 -> 5CaCl2 + Ca(ClO3)2",
      "Hot water causes bleaching powder to freeze instantly",
      "Cold water is more expensive than hot water",
      "Hot water neutralizes the calcium ions into nitrogen"],
     "A", "OSC", "medium",
     "At elevated temperatures, hypochlorite disproportionates into chlorate and chloride: 3OCl- -> ClO3- + 2Cl-, destroying active chlorine."),

    ("What white insoluble residue is left behind when bleaching powder is stirred with excess water?""",
     ["Unreacted calcium hydroxide (slaked lime, Ca(OH)2)",
      "Pure silver chloride",
      "Sodium bicarbonate crystals",
      "Silicon dioxide sand"],
     "A", "OSC", "medium",
     "Commercial bleaching powder contains 20-30% unreacted slaked lime (Ca(OH)2) from the manufacturing process, which forms a milky suspension."),

    ("How does bleaching powder act as a chloroform-producing reagent in organic synthesis?""",
     ["It reacts with ethanol or acetone through oxidation, chlorination, and alkaline cleavage (haloform reaction)",
      "It directly condenses with carbon dioxide",
      "It releases methane gas under pressure",
      "It reduces methanol into petroleum"],
     "A", "OSC", "hard",
     "In the laboratory haloform synthesis, bleaching powder oxidizes and chlorinates ethanol or acetone into trichloro derivatives, followed by cleavage to chloroform (CHCl3)."),

    ("State whether the following statement is True or False: Plaster of Paris can be regenerated back into gypsum repeatedly by adding water.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Adding water to POP converts it back into gypsum; however, once set into a hard solid, it cannot be re-molded unless calcinated again at 373 K."),

    ("Which property of Plaster of Paris makes it invaluable for dental impressions?""",
     ["It sets quickly with high dimensional accuracy and negligible shrinkage",
      "It tastes like sugar",
      "It remains flexible forever inside the mouth",
      "It glows in the dark"],
     "A", "OSC", "easy",
     "Dental plasters capture microscopic tooth contours precisely because the hemihydrate slurry expands slightly on crystallization without shrinking."),

    ("What is the effect of adding common salt (NaCl) in small amounts to Plaster of Paris slurry?""",
     ["It acts as an accelerator, speeding up the setting time of the plaster",
      "It completely prevents the plaster from setting forever",
      "It causes the plaster to explode",
      "It turns the plaster liquid blue"],
     "A", "OSC", "medium",
     "Electrolytes like sodium chloride increase the solubility and dissolution rate of calcium sulfate hemihydrate, accelerating gypsum crystallization."),

    ("What is the effect of adding borax, glue, or citric acid to Plaster of Paris paste?""",
     ["They act as retarders, slowing down the setting time to provide more working time for sculpting",
      "They cause the plaster to catch fire",
      "They evaporate all the water instantly",
      "They convert the plaster into quicklime"],
     "A", "OSC", "medium",
     "Colloidal retarders like glue or organic acids adsorb onto developing crystal nuclei, slowing crystal growth and extending working time."),

    ("Why should Plaster of Paris be stored in waterproof and moisture-proof bags?""",
     ["Even slight atmospheric moisture causes it to slowly hydrate into gypsum, ruining its setting power before use",
      "Water dissolves the plastic bag",
      "Moisture turns POP into poisonous chlorine gas",
      "Air makes the powder too heavy to lift"],
     "A", "OSC", "easy",
     "If exposed to humid air, POP absorbs water and slowly hydrates into gypsum, forming hard clumps and rendering the powder useless."),

    # 51-60: Gypsum, Alum & Setting Characteristics
    ("What is the chemical difference between Gypsum and Plaster of Paris?""",
     ["Gypsum has 2 molecules of water of crystallization per formula unit, while Plaster of Paris has 0.5 molecule",
      "Gypsum has zero water molecules, while POP has 10",
      "Gypsum contains sodium, while POP contains calcium",
      "Gypsum is a liquid, while POP is a gas"],
     "A", "OSC", "easy",
     "Gypsum is calcium sulfate dihydrate (CaSO4.2H2O); Plaster of Paris is calcium sulfate hemihydrate (CaSO4.1/2H2O)."),

    ("How is 'dead burnt plaster' produced?""",
     ["By heating gypsum strongly above 200 degrees Celsius (473 K) until all water of crystallization is driven off",
      "By freezing POP below zero degrees Celsius",
      "By dissolving gypsum in concentrated sulfuric acid",
      "By exposing gypsum to ultraviolet rays"],
     "A", "OSC", "medium",
     "At temperatures exceeding 473 K, all water of crystallization is lost, yielding anhydrous calcium sulfate (CaSO4), also called dead burnt plaster."),

    ("Why is dead burnt plaster called 'dead'?""",
     ["Because it does not set or harden when mixed with water",
      "Because it is lethal to touch",
      "Because it emits toxic radioactive rays",
      "Because it can never be heated again"],
     "A", "OSC", "easy",
     "It is called dead because it has lost its hydraulic setting affinity; adding water does not rehydrate it into gypsum under normal conditions."),

    ("What type of chemical reaction is the setting of Plaster of Paris?""",
     ["An exothermic hydration reaction that releases heat",
      "An endothermic decomposition reaction that absorbs cold",
      "A photochemical displacement reaction",
      "A nuclear fusion reaction"],
     "A", "OSC", "medium",
     "Setting of POP is an exothermic hydration reaction; the cast noticeably warms up during the 10-15 minute hardening period."),

    ("Why does an orthopedic plaster cast feel warm to the touch during the first 15 minutes of application?""",
     ["The hydration of calcium sulfate hemihydrate into gypsum releases latent heat of crystallization (exothermic reaction)",
      "Hot water is used to soak the bandages",
      "The patient's body temperature boils the plaster",
      "Friction between bandages generates heat"],
     "A", "OSC", "medium",
     "The hydration enthalpy released as needle-like gypsum crystals form elevates the temperature of the cast temporarily."),

    ("What is the molecular formula of potash alum when written in standard double-salt notation?""",
     ["K2SO4.Al2(SO4)3.24H2O",
      "KAlSO4.12H2O",
      "K2Al2(SO4)4.10H2O",
      "KAlO2.6H2O"],
     "A", "OSC", "easy",
     "Potash alum is formulated as K2SO4.Al2(SO4)3.24H2O, which can also be represented by its empirical formula KAl(SO4)2.12H2O."),

    ("What test can be performed to confirm the presence of sulfate ions (SO4^2-) in an aqueous solution of potash alum or gypsum?""",
     ["Adding barium chloride (BaCl2) solution produces a dense white precipitate of barium sulfate (BaSO4) insoluble in dilute HCl",
      "Adding silver nitrate produces a bright red gas",
      "Adding sodium hydroxide produces blue flames",
      "Adding vinegar turns the solution into milk"],
     "A", "OSC", "medium",
     "Barium chloride reacts with sulfate ions to form an insoluble white precipitate: Ba2+ + SO4^2- -> BaSO4(s)."),

    ("Assertion (A): Bleaching powder does not dissolve completely in water.\nReason (R): It contains unreacted slaked lime (calcium hydroxide) which has low aqueous solubility.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "medium",
     "Because slaked lime is only sparingly soluble (approx 1.7 g/L), the unreacted portion remains as a milky colloidal suspension in water."),

    ("Assertion (A): Gypsum is added to Portland cement clinker during grinding.\nReason (R): Without gypsum, cement undergoes flash setting within minutes of adding water, making placement impossible.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "medium",
     "Gypsum forms ettringite crystals on the surface of tricalcium aluminate particles, retarding rapid hydration and controlling setting rate."),

    ("State whether the following statement is True or False: Potash alum exhibits acidic character in aqueous solution.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Aluminium ions undergo hydrolysis: Al3+ + 3H2O <=> Al(OH)3 + 3H+, generating excess hydronium ions and lowering the solution pH below 7.")
]

# Add remaining practice questions to make exactly 30 (61-70)
practice_data.extend([
    ("What gas is released when bleaching powder reacts with excess dilute hydrochloric acid?""",
     ["Chlorine (Cl2)", "Hydrogen (H2)", "Oxygen (O2)", "Nitrogen (N2)"],
     "A", "OSC", "easy",
     "CaOCl2 + 2HCl -> CaCl2 + H2O + Cl2."),

    ("Which salt among the following is extensively used for fireproofing materials and fireproof wallboards?""",
     ["Gypsum (drywall / sheetrock)", "Sodium chloride", "Potassium nitrate", "Ammonium chloride"],
     "A", "OSC", "medium",
     "Gypsum boards contain 21% chemically bound water by weight. When exposed to fire, this water vaporizes, absorbing heat and delaying temperature rise."),

    ("How many water molecules are present in one formula unit of gypsum?""",
     ["2", "1/2", "5", "7"],
     "A", "OSC", "easy",
     "Gypsum is CaSO4.2H2O, containing 2 water molecules per formula unit."),

    ("What happens when anhydrous copper sulfate powder is exposed to moist air?""",
     ["It absorbs moisture and turns blue", "It turns black", "It turns green", "It burns"],
     "A", "OSC", "easy",
     "Anhydrous white CuSO4 hydrates into blue CuSO4.5H2O."),

    ("Which property of bleaching powder makes it suitable for purifying drinking water in municipal tanks?""",
     ["Germicidal and sterilizing action due to nascent oxygen and hypochlorite",
      "Pleasant sweet taste",
      "Ability to dissolve all mud instantly",
      "Increases electrical conductivity"],
     "A", "OSC", "easy",
     "Nascent oxygen released oxidizes and destroys bacteria and bacterial cell walls."),

    ("State whether True or False: Plaster of Paris expands slightly upon setting.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Plaster of Paris expands by approx 0.5% during crystallization, ensuring crisp mold reproduction."),

    ("Which double salt is used as a mordant in dyeing cloth to fix colors to textile fibers?""",
     ["Potash alum", "Common salt", "Baking soda", "Washing soda"],
     "A", "OSC", "medium",
     "Alum precipitates gelatinous Al(OH)3 on fibers, binding the organic dye molecules permanently."),

    ("Plaster of Paris is chemically represented as CaSO4.________ H2O.",
     ["1/2", "2", "5", "10"],
     "A", "OFB", "easy",
     "POP is calcium sulfate hemihydrate: CaSO4.1/2H2O."),

    ("How many grams of water are present in 1 mole of potash alum (K2SO4.Al2(SO4)3.24H2O)?""",
     ["432 g", "24 g", "216 g", "180 g"],
     "A", "ONE", "medium",
     "24 moles of water * 18 g/mol = 432 g."),

    ("Which pair of compounds are chemical hydrates of calcium sulfate?""",
     ["Gypsum and Plaster of Paris", "Slaked lime and Quicklime", "Baking soda and Washing soda", "Epsom salt and Glauber's salt"],
     "A", "OSC", "easy",
     "Both gypsum (CaSO4.2H2O) and Plaster of Paris (CaSO4.1/2H2O) are hydrates of calcium sulfate.")
])

# 12 Mock/Foundation Questions with Vector SVGs (71-82)
mock_data = [
    # 71: Manufacturing of Bleaching Powder apparatus
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#1e293b"/>
  <rect x="50" y="50" width="300" height="70" rx="6" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <line x1="80" y1="30" x2="80" y2="50" stroke="#38bdf8" stroke-width="4" marker-end="url(#arrow)"/>
  <text x="80" y="24" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">Dry Slaked Lime Ca(OH)2</text>
  <line x1="30" y1="85" x2="50" y2="85" stroke="#4ade80" stroke-width="4"/>
  <text x="25" y="80" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="end" font-weight="bold">Cl2 Gas (inlet)</text>
  <circle cx="120" cy="85" r="4" fill="#fde047"/>
  <circle cx="160" cy="85" r="4" fill="#fde047"/>
  <circle cx="200" cy="85" r="4" fill="#fde047"/>
  <circle cx="240" cy="85" r="4" fill="#fde047"/>
  <circle cx="280" cy="85" r="4" fill="#fde047"/>
  <line x1="320" y1="120" x2="320" y2="155" stroke="#fde047" stroke-width="4"/>
  <text x="320" y="175" fill="#fde047" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">Bleaching Powder (CaOCl2)</text>
</svg>
</div>
The schematic shows the industrial chlorination tower for producing bleaching powder. What is the role of maintaining the reaction temperature strictly below 40 degrees Celsius?""",
     ["To prevent the formation of unwanted calcium chlorate (Ca(ClO3)2) and ensure maximum available chlorine",
      "To prevent chlorine gas from condensing into a solid block",
      "To stop slaked lime from melting into liquid calcium",
      "To accelerate explosive decomposition into oxygen gas"],
     "A", "OSC", "hard",
     "At temperatures above 40 degrees Celsius, chlorine reacts with slaked lime to form calcium chlorate (Ca(ClO3)2) rather than bleaching powder, severely reducing available chlorine."),

    # 72: Bleaching mechanism by nascent oxygen
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="180" rx="8" fill="#0f172a"/>
  <rect x="30" y="60" width="90" height="45" rx="6" fill="#ef4444" stroke="#f87171" stroke-width="2"/>
  <text x="75" y="87" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Colored Dye</text>
  <path d="M 125 82 L 185 82" stroke="#38bdf8" stroke-width="3" fill="none"/>
  <polygon points="190,82 180,77 180,87" fill="#38bdf8"/>
  <text x="155" y="72" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">+ [O]</text>
  <rect x="195" y="60" width="160" height="45" rx="6" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="275" y="87" fill="#e2e8f0" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Colorless Oxidized Matter</text>
  <text x="200" y="145" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle">Nascent oxygen [O] oxidizes dye chromophores</text>
</svg>
</div>
The diagram illustrates the bleaching mechanism of bleaching powder in moisture. Which chemical reaction generates the reactive nascent oxygen [O]?""",
     ["Cl2 + H2O -> HCl + HOCl; HOCl -> HCl + [O]",
      "CaOCl2 -> Ca + O2 + Cl2",
      "2H2O -> 2H2 + O2",
      "CO2 + H2O -> H2CO3"],
     "A", "OSC", "medium",
     "Chlorine dissolves in water to form hypochlorous acid (HOCl), which is unstable and breaks down into hydrochloric acid and highly reactive nascent oxygen [O]."),

    # 73: Dehydration curve of Gypsum to POP
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <line x1="60" y1="160" x2="350" y2="160" stroke="#71717a" stroke-width="2"/>
  <line x1="60" y1="160" x2="60" y2="30" stroke="#71717a" stroke-width="2"/>
  <text x="350" y="180" fill="#a1a1aa" font-size="11" font-family="sans-serif" text-anchor="end">Temperature (K)</text>
  <text x="45" y="30" fill="#a1a1aa" font-size="11" font-family="sans-serif" text-anchor="end">Water of Cryst.</text>
  <circle cx="100" cy="60" r="5" fill="#38bdf8"/>
  <text x="100" y="50" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">2 H2O (Gypsum)</text>
  <line x1="100" y1="60" x2="200" y2="110" stroke="#facc15" stroke-width="2" stroke-dasharray="4"/>
  <circle cx="200" cy="110" r="5" fill="#facc15"/>
  <text x="200" y="100" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle">373 K: 0.5 H2O (POP)</text>
  <line x1="200" y1="110" x2="310" y2="160" stroke="#ef4444" stroke-width="2" stroke-dasharray="4"/>
  <circle cx="310" cy="160" r="5" fill="#ef4444"/>
  <text x="310" y="150" fill="#ef4444" font-size="10" font-family="sans-serif" text-anchor="middle">> 473 K: 0 H2O (Dead burnt)</text>
</svg>
</div>
Based on the temperature-dependent dehydration chart above, what state of matter is obtained if calcination is conducted at 480 K?""",
     ["Anhydrous calcium sulfate (CaSO4, dead burnt plaster) with zero water of crystallization",
      "Plaster of Paris with 1.5 water molecules",
      "Liquid gypsum solution",
      "Metallic calcium powder"],
     "A", "OSC", "hard",
     "Heating gypsum above 473 K drives off all water of crystallization, yielding completely anhydrous CaSO4 (dead burnt plaster)."),

    # 74: Setting and expansion of POP in casting
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="180" rx="8" fill="#0f172a"/>
  <rect x="50" y="40" width="120" height="90" rx="4" fill="#334155" stroke="#64748b" stroke-width="2"/>
  <text x="110" y="75" fill="#e2e8f0" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Hemihydrate Slurry</text>
  <text x="110" y="95" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">(Fluid, fills cavity)</text>
  <path d="M 185 85 L 225 85" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="230,85 220,80 220,90" fill="#38bdf8"/>
  <rect x="240" y="38" width="124" height="94" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="302" y="75" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Set Gypsum Matrix</text>
  <text x="302" y="95" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle">(0.5% expansion, sharp edges)</text>
</svg>
</div>
The diagram shows why Plaster of Paris is preferred for intricate sculpture casting over other cements. What structural phenomenon causes the volume expansion upon setting?""",
     ["Growth of interlocking needle-shaped monoclinic gypsum crystals leaving micro-porosity",
      "Formation of high pressure hydrogen gas bubbles",
      "Dissolution of calcium into air",
      "Sublimation of water molecules into steam"],
     "A", "OSC", "hard",
     "Hydration converts hemihydrate into an interlocking network of acicular (needle-like) gypsum crystals, increasing the apparent specific volume by ~0.5%."),

    # 75: Orthopedic Cast Mechanism
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#1e293b"/>
  <rect x="70" y="70" width="260" height="40" rx="8" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
  <text x="200" y="95" fill="#f8fafc" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">Fractured Bone (Immobilized)</text>
  <rect x="50" y="50" width="300" height="80" rx="12" fill="none" stroke="#38bdf8" stroke-width="4" stroke-dasharray="6,4"/>
  <text x="200" y="40" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Rigid P.O.P. Cast (Exothermic Setting)</text>
  <text x="200" y="160" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle">Heat released: \DeltaH_hydration < 0</text>
</svg>
</div>
When an orthopedic surgeon immerses a POP gauze roll in water before applying it to a fractured limb, why must cold or lukewarm water be used rather than hot water?""",
     ["Hot water accelerates setting excessively, generating high exothermic heat that could scald or burn patient skin",
      "Hot water dissolves all the gauze fibers completely",
      "Hot water turns POP into calcium oxide (quicklime)",
      "Hot water stops the bone from mending"],
     "A", "OSC", "hard",
     "The hydration reaction is strongly exothermic; hot water causes rapid setting and can push the temperature of a thick cast past 45-50 degrees Celsius, risking thermal burns to skin."),

    # 76: Double salt dissociation (Potash Alum)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="180" rx="8" fill="#0f172a"/>
  <rect x="30" y="65" width="130" height="50" rx="6" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="95" y="90" fill="#f8fafc" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">K2SO4.Al2(SO4)3</text>
  <text x="95" y="105" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">(Potash Alum solid)</text>
  <path d="M 170 90 L 210 90" stroke="#4ade80" stroke-width="3"/>
  <polygon points="215,90 205,85 205,95" fill="#4ade80"/>
  <text x="190" y="80" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle">+ H2O</text>
  <rect x="225" y="45" width="145" height="90" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="297" y="70" fill="#fde047" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">2 K+ (aq)</text>
  <text x="297" y="92" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">2 Al3+ (aq)</text>
  <text x="297" y="115" fill="#f87171" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">4 SO4^2- (aq)</text>
</svg>
</div>
The diagram shows the complete ionic dissociation of potash alum in aqueous solution. Why does this behavior classify potash alum as a double salt rather than a coordination complex?""",
     ["It completely dissociates into its simple individual ions and gives characteristic qualitative tests for K+, Al3+, and SO4^2-",
      "It only dissociates into liquid potassium metal",
      "It forms covalent bonds that never break in water",
      "It precipitates as metallic aluminium instantly"],
     "A", "OSC", "medium",
     "Double salts dissociate completely into their individual constituent ions in aqueous solution, retaining no complex coordination structure."),

    # 77: Coagulation of muddy water by Alum
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <circle cx="80" cy="95" r="30" fill="#78350f" stroke="#d97706" stroke-width="2"/>
  <text x="80" y="92" fill="#fef3c7" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Colloidal Clay</text>
  <text x="80" y="106" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle">(- - - charge)</text>
  <path d="M 125 95 L 175 95" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="180,95 170,90 170,100" fill="#38bdf8"/>
  <text x="150" y="85" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">+ Al3+</text>
  <rect x="195" y="55" width="170" height="80" rx="6" fill="#27272a" stroke="#4ade80" stroke-width="2"/>
  <text x="280" y="85" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Neutralized Floc</text>
  <text x="280" y="105" fill="#a1a1aa" font-size="10" font-family="sans-serif" text-anchor="middle">Aggregates & settles down</text>
</svg>
</div>
According to the Hardy-Schulze rule illustrated above, why is the trivalent Al3+ ion from potash alum far more potent at coagulating negative clay colloids than divalent Ca2+ or univalent Na+?""",
     ["Coagulation power increases exponentially with the valence of the coagulating counter-ion (Al3+ >> Ca2+ > Na+)",
      "Al3+ ions are magnetic and pull clay particles together",
      "Al3+ turns clay into gaseous oxygen",
      "Na+ ions destroy water molecules"],
     "A", "OSC", "hard",
     "Under the Hardy-Schulze rule, the coagulating power of an electrolyte is proportional to the sixth power of the ion's valency; trivalent Al3+ is several hundred times more effective than monovalent Na+."),

    # 78: Reaction of Bleaching powder with atmospheric CO2
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="180" rx="8" fill="#0f172a"/>
  <rect x="40" y="60" width="100" height="50" rx="6" fill="#334155" stroke="#fde047" stroke-width="2"/>
  <text x="90" y="85" fill="#fde047" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">CaOCl2 (solid)</text>
  <text x="90" y="100" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">+ CO2 (air)</text>
  <path d="M 155 85 L 205 85" stroke="#94a3b8" stroke-width="3"/>
  <polygon points="210,85 200,80 200,90" fill="#94a3b8"/>
  <rect x="220" y="45" width="150" height="80" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <text x="295" y="75" fill="#e2e8f0" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">CaCO3 (solid)</text>
  <text x="295" y="98" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">+ Cl2 (gas escaped)</text>
</svg>
</div>
A sealed bag of bleaching powder stored in a warehouse was found to have turned into an inert chalky powder after 3 years. What test would quickly reveal that it has lost its active chlorine?""",
     ["Adding dilute HCl produces no greenish-yellow chlorine gas and no bleaching effect on litmus",
      "Testing with a magnet to see if it attracts iron",
      "Measuring its electrical conductivity in solid dry state",
      "Weighing if its mass decreased to zero"],
     "A", "OSC", "medium",
     "Fresh bleaching powder effervesces chlorine when treated with dilute acid. Once fully carbonated into CaCO3, treating it with dilute acid liberates CO2 instead of Cl2, losing all bleaching capability."),

    # 79: Comparison of POP vs Gypsum Crystal Structures
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="180" rx="8" fill="#18181b"/>
  <rect x="40" y="45" width="140" height="90" rx="6" fill="#27272a" stroke="#38bdf8" stroke-width="2"/>
  <text x="110" y="75" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">Plaster of Paris</text>
  <text x="110" y="95" fill="#e2e8f0" font-size="11" font-family="sans-serif" text-anchor="middle">2 CaSO4 : 1 H2O</text>
  <text x="110" y="115" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">(Hemihydrate)</text>
  <rect x="220" y="45" width="140" height="90" rx="6" fill="#27272a" stroke="#4ade80" stroke-width="2"/>
  <text x="290" y="75" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">Gypsum</text>
  <text x="290" y="95" fill="#e2e8f0" font-size="11" font-family="sans-serif" text-anchor="middle">1 CaSO4 : 2 H2O</text>
  <text x="290" y="115" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">(Dihydrate)</text>
</svg>
</div>
How many moles of liquid water must be added to 1 mole of solid Plaster of Paris (CaSO4.1/2H2O) to completely convert it into 1 mole of gypsum?""",
     ["1.5 moles (27 grams of water)",
      "0.5 moles (9 grams of water)",
      "2.0 moles (36 grams of water)",
      "3.0 moles (54 grams of water)"],
     "A", "OSC", "medium",
     "Stoichiometrically: CaSO4.0.5H2O + 1.5H2O -> CaSO4.2H2O. Exactly 1.5 moles of water are required per mole of POP."),

    # 80: Retardation of cement setting by Gypsum
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="180" rx="8" fill="#0f172a"/>
  <rect x="40" y="55" width="130" height="70" rx="6" fill="#334155" stroke="#f87171" stroke-width="2"/>
  <text x="105" y="80" fill="#f87171" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Without Gypsum</text>
  <text x="105" y="102" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Flash sets in 3-5 min!</text>
  <rect x="230" y="55" width="130" height="70" rx="6" fill="#334155" stroke="#4ade80" stroke-width="2"/>
  <text x="295" y="80" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">With 2-3% Gypsum</text>
  <text x="295" y="102" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Initial set > 45 min</text>
</svg>
</div>
Why is controlling the initial setting time of cement with gypsum indispensable on modern construction sites?""",
     ["It gives masons sufficient time for mixing, transporting, pouring, and finishing concrete before it solidifies",
      "It prevents concrete from ever hardening",
      "It makes concrete completely float on water",
      "It eliminates the need for steel reinforcement"],
     "A", "OSC", "easy",
     "Flash setting would freeze concrete in the transit mixer or chute. Gypsum ensures a minimum initial setting time of 30-45 minutes for workable placement."),

    # 81: Identification of Bleaching Powder vs Calcium Carbonate
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <rect x="50" y="50" width="120" height="85" rx="6" fill="#27272a" stroke="#38bdf8" stroke-width="2"/>
  <text x="110" y="75" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Test Tube A: CaOCl2</text>
  <text x="110" y="95" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">+ Dilute HCl</text>
  <text x="110" y="115" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle">-> Cl2 (yellow-green)</text>
  <rect x="230" y="50" width="120" height="85" rx="6" fill="#27272a" stroke="#facc15" stroke-width="2"/>
  <text x="290" y="75" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Test Tube B: CaCO3</text>
  <text x="290" y="95" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">+ Dilute HCl</text>
  <text x="290" y="115" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">-> CO2 (colorless)</text>
</svg>
</div>
Which confirmatory test definitively differentiates the gas evolved from Tube A from that of Tube B?""",
     ["Gas from Tube A bleaches moist colored litmus paper, while gas from Tube B turns lime water milky without bleaching",
      "Gas from Tube A explodes with a pop sound",
      "Gas from Tube B burns with a lilac flame",
      "Both gases have identical smell and color"],
     "A", "OSC", "medium",
     "Chlorine from bleaching powder decolors moist litmus paper via oxidation; CO2 from carbonate turns lime water milky due to CaCO3 precipitation."),

    # 82: Water of Crystallization Loss in Vitriols
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <circle cx="80" cy="95" r="35" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2"/>
  <text x="80" y="90" fill="#bfdbfe" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">CuSO4.5H2O</text>
  <text x="80" y="105" fill="#93c5fd" font-size="10" font-family="sans-serif" text-anchor="middle">(Blue Vitriol)</text>
  <path d="M 130 95 L 180 95" stroke="#facc15" stroke-width="3"/>
  <polygon points="185,95 175,90 175,100" fill="#facc15"/>
  <text x="157" y="85" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">\Delta heat</text>
  <circle cx="235" cy="95" r="35" fill="#334155" stroke="#cbd5e1" stroke-width="2"/>
  <text x="235" y="90" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">CuSO4</text>
  <text x="235" y="105" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">(White powder)</text>
  <text x="330" y="95" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">+ 5 H2O (g)</text>
</svg>
</div>
When blue vitriol crystals are heated in a dry boiling tube, water droplets collect at the upper cool mouth and the salt loses its color. Why is this considered a reversible chemical change?""",
     ["Adding a few drops of liquid water immediately restores the pentahydrate coordination complex and the blue crystalline appearance",
      "The white powder spontaneously turns into gold",
      "The water cannot be reabsorbed once lost",
      "Heating permanently breaks the copper-sulfate ionic bond"],
     "A", "OSC", "easy",
     "Rehydration of anhydrous CuSO4 is an exothermic reversible coordination reaction that reconstitutes the blue copper-aqua complex [Cu(H2O)4]SO4.H2O.")
]

# Generate questions
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

output_path = os.path.join(os.path.dirname(__file__), "ch14_topic2.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
