# scripts/generate_ch14_topic1.py
# MH-9-SCIT-14-14.1: Important Salts: Common Salt (NaCl), Baking Soda (NaHCO3), Washing Soda (Na2CO3·10H2O)
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-14-14.1"

# 40 Exam Questions
exam_data = [
    # 1-10: Classification of Salts & Water of Crystallization
    ("What is the pH value of an aqueous solution of a neutral salt formed by the reaction of a strong acid and a strong base (such as NaCl)?""",
     ["pH = 7 (strictly neutral)", "pH < 7 (acidic)", "pH > 7 (basic)", "pH = 0"],
     "A", "OSC", "easy",
     "When an equimolar strong acid (HCl) neutralizes a strong base (NaOH), neither conjugate cation nor anion hydrolyzes in water, maintaining a neutral pH of 7."),

    ("What type of salt is formed by the reaction between a strong acid and a weak base (such as ammonium chloride, NH4Cl)?""",
     ["An acidic salt with an aqueous pH less than 7 (pH < 7)",
      "A basic salt with pH > 7",
      "A neutral salt with pH = 7",
      "A neutral salt with pH = 14"],
     "A", "OSC", "easy",
     "In NH4Cl, the ammonium cation (NH4+) undergoes cation hydrolysis with water to produce hydronium ions: NH4+ + H2O <=> NH3 + H3O+, making the aqueous solution acidic (pH < 7)."),

    ("What type of salt is formed by the neutralization of a weak acid with a strong base (such as sodium carbonate, Na2CO3)?""",
     ["A basic salt with an aqueous pH greater than 7 (pH > 7)",
      "An acidic salt with pH < 7",
      "A neutral salt with pH = 7",
      "A neutral salt with pH = 1"],
     "A", "OSC", "easy",
     "Carbonate anions (CO3^2-) undergo anion hydrolysis with water: CO3^2- + H2O <=> HCO3- + OH-, generating excess hydroxide ions and imparting alkaline/basic character (pH > 7)."),

    ("What is 'water of crystallization' in inorganic salts?""",
     ["A fixed, definite number of water molecules chemically bonded in the crystal lattice structure of a crystalline salt",
      "Liquid water poured over dry salt crystals",
      "Moisture absorbed from humid air by hygroscopic salts",
      "Water boiled inside an engine boiler"],
     "A", "OSC", "easy",
     "Water of crystallization comprises stoichiometric water molecules occupying specific coordination sites within the crystalline lattice (e.g. 5 H2O in CuSO4.5H2O)."),

    ("What happens to hydrated copper sulfate crystals (CuSO4.5H2O, blue vitriol) when heated strongly in a dry test tube?""",
     ["They lose their water of crystallization, turning into white anhydrous copper sulfate powder (CuSO4) while water droplets condense on the cooler tube walls",
      "They turn into metallic copper wire",
      "They melt into a yellow liquid",
      "They turn pitch black and catch fire"],
     "A", "OSC", "easy",
     "Heating drives off the 5 coordinated water molecules: CuSO4.5H2O (blue) -> CuSO4 (white anhydrous) + 5H2O. Adding a drop of water immediately restores the vibrant blue color."),

    ("What is the chemical formula and common name of crystalline green vitriol?""",
     ["Ferrous sulfate heptahydrate (FeSO4.7H2O)",
      "Copper sulfate pentahydrate",
      "Magnesium sulfate heptahydrate",
      "Zinc sulfate heptahydrate"],
     "A", "OSC", "easy",
     "Green vitriol is ferrous sulfate heptahydrate (FeSO4.7H2O), containing seven molecules of water of crystallization per formula unit."),

    ("What is the chemical formula of potash alum (fitkari) commonly used for purifying muddy water and aftershave astringent?""",
     ["K2SO4.Al2(SO4)3.24H2O",
      "K2SO4.CuSO4.5H2O",
      "FeSO4.7H2O",
      "Na2CO3.10H2O"],
     "A", "OSC", "medium",
     "Potash alum is a double salt of potassium sulfate and aluminium sulfate dodecahydrate containing 24 molecules of water of crystallization: K2SO4.Al2(SO4)3.24H2O."),

    ("How does dissolved potash alum clarify turbid, muddy river water during municipal water purification?""",
     ["Trivalent Al3+ ions neutralize negative electrostatic charges on colloidal clay particles, causing them to coagulate and settle rapidly to the bottom (coagulation)",
      "Alum dissolves the mud into clear water",
      "Alum boils the water to kill bacteria",
      "Alum turns the clay particles into oxygen gas"],
     "A", "OSC", "medium",
     "Colloidal clay particles carry negative surface charges that repel each other. Multivalent Al3+ ions from alum neutralize these charges, allowing particles to aggregate and precipitate."),

    ("What is the chemical formula of Epsom salt used as a therapeutic bath soak and laxative?""",
     ["Magnesium sulfate heptahydrate (MgSO4.7H2O)",
      "Calcium sulfate dihydrate",
      "Sodium chloride",
      "Sodium carbonate decahydrate"],
     "A", "OSC", "easy",
     "Epsom salt is hydrated magnesium sulfate (MgSO4.7H2O), named after the mineral springs at Epsom in Surrey, England."),

    ("State whether the following statement is True or False: Adding water to white anhydrous copper sulfate powder turns it blue again.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Rehydration re-establishes the copper-water coordination complex [Cu(H2O)4]^2+, immediately restoring the characteristic blue crystalline color."),

    # 11-20: Common Salt (NaCl) & The Chlor-Alkali Process
    ("What are the primary commercial products generated during the industrial 'chlor-alkali' electrolysis of aqueous sodium chloride (brine)?""",
     ["Sodium hydroxide (NaOH) in solution, chlorine gas (Cl2) at the anode, and hydrogen gas (H2) at the cathode",
      "Pure metallic sodium and liquid oxygen",
      "Hydrochloric acid and nitrogen gas",
      "Solid baking soda and carbon dioxide"],
     "A", "OSC", "easy",
     "Electrolysis of concentrated brine drives the chlor-alkali reaction: 2NaCl + 2H2O -> 2NaOH + Cl2 (anode) + H2 (cathode), supplying chlorine, hydrogen, and caustic soda."),

    ("At which electrode is chlorine gas (Cl2) discharged during the electrolysis of brine?""",
     ["At the positive anode (+), where chloride ions (Cl-) undergo oxidation by losing electrons",
      "At the negative cathode (-)",
      "At both electrodes equally",
      "In the middle of the liquid solution only"],
     "A", "OSC", "easy",
     "Anions migrate to the positively charged anode: 2Cl- -> Cl2 + 2e- (oxidation)."),

    ("At which electrode is hydrogen gas (H2) released during the chlor-alkali process?""",
     ["At the negative cathode (-), where hydrogen ions (H+) from water undergo reduction by gaining electrons",
      "At the positive anode (+)",
      "Inside the gas separator valve",
      "Nowhere (hydrogen is not produced)"],
     "A", "OSC", "easy",
     "Cations migrate to the negatively charged cathode: 2H2O + 2e- -> H2 + 2OH- (reduction)."),

    ("Why is common table salt slightly iodized with trace potassium iodate (KIO3) or potassium iodide (KI)?""",
     ["To provide essential dietary iodine required by the thyroid gland to synthesize thyroxine hormone and prevent endemic goiter and cretinism",
      "To prevent table salt from dissolving in water",
      "To make table salt sweet to taste",
      "To color table salt bright yellow"],
     "A", "OSC", "easy",
     "Iodine is a micronutrient required for thyroxine synthesis; mandatory salt iodization prevents thyroid enlargement (goitre) and cognitive impairment."),

    ("Why does ordinary unrefined common salt become sticky, wet, and clumpy during the humid rainy monsoon season?""",
     ["It contains deliquescent mineral impurities of magnesium chloride (MgCl2) and calcium chloride (CaCl2) that absorb moisture from humid air",
      "Pure NaCl attracts water vapor faster than ice",
      "Salt molecules decompose into liquid water",
      "Salt turns into baking soda when wet"],
     "A", "OSC", "medium",
     "Pure NaCl is not deliquescent. However, unrefined sea salt contains traces of MgCl2 and CaCl2, which absorb atmospheric moisture and dissolve in it."),

    # 16-25: Baking Soda (NaHCO3) & Baking Powder
    ("What is the chemical name and chemical formula of commercial 'baking soda'?""",
     ["Sodium hydrogen carbonate (or sodium bicarbonate), NaHCO3",
      "Sodium carbonate decahydrate, Na2CO3.10H2O",
      "Calcium carbonate, CaCO3",
      "Sodium hydroxide, NaOH"],
     "A", "OSC", "easy",
     "Baking soda is pure sodium bicarbonate / sodium hydrogen carbonate (NaHCO3)."),

    ("What chemical reaction takes place when dry baking soda (NaHCO3) is heated during cooking?""",
     ["Thermal decomposition into sodium carbonate, water vapor, and carbon dioxide: 2 NaHCO3 -> Na2CO3 + H2O + CO2 (gas)",
      "It melts into pure metallic sodium",
      "It turns into liquid chlorine gas",
      "It oxidizes to form sodium nitrate"],
     "A", "OSC", "easy",
     "Heat decomposes sodium bicarbonate: 2 NaHCO3 -> Na2CO3 + H2O + CO2, releasing expanding CO2 bubbles that leaven the batter."),

    ("What is the crucial chemical difference between 'baking soda' and 'baking powder'?""",
     ["Baking soda is pure NaHCO3, whereas baking powder is a dry mixture of baking soda (NaHCO3) and a mild edible organic acid (such as tartaric acid)",
      "Baking powder is made of pure flour",
      "Baking soda is acidic while baking powder is neutral",
      "Baking powder contains liquid vinegar"],
     "A", "OSC", "medium",
     "Baking powder contains both a bicarbonate base and dry tartaric acid (or cream of tartar) with starch filler. In moisture, acid neutralizes the basic carbonate, preventing a bitter taste."),

    ("Why does baking a cake with pure baking soda alone leave an unpleasant, bitter soapy taste, whereas baking powder does not?""",
     ["Heating pure baking soda leaves basic sodium carbonate (Na2CO3) in the cake, whereas baking powder contains tartaric acid that neutralizes Na2CO3 into tasteless sodium tartrate",
      "Baking soda contains concentrated soap",
      "Baking powder adds sugar automatically",
      "Baking soda reacts with oven heat to form salt"],
     "A", "OSC", "medium",
     "Thermal breakdown of NaHCO3 generates alkaline Na2CO3, which tastes bitter. The tartaric acid in baking powder neutralizes Na2CO3: Na2CO3 + C4H6O6 -> Na2C4H4O6 (neutral) + H2O + CO2."),

    ("Why is sodium bicarbonate (NaHCO3) used as an active ingredient in clinical antacid tablets (e.g. Eno)?""",
     ["It is a mild, non-corrosive basic salt that safely neutralizes hyper-acidic hydrochloric acid in gastric juice: NaHCO3 + HCl -> NaCl + H2O + CO2",
      "It stops the stomach from digesting food",
      "It kills all bacteria in the intestines with chlorine",
      "It coats the stomach with metallic sodium"],
     "A", "OSC", "easy",
     "Being mildly basic, NaHCO3 neutralizes excess gastric HCl, relieving heartburn and acid indigestion without damaging delicate esophageal mucosa."),

    # 21-30: Washing Soda (Na2CO3.10H2O) & Hard Water Softening
    ("What is the chemical name and formula of commercial 'washing soda'?""",
     ["Sodium carbonate decahydrate, Na2CO3.10H2O",
      "Sodium hydrogen carbonate, NaHCO3",
      "Sodium hydroxide, NaOH",
      "Sodium sulfate decahydrate, Na2SO4.10H2O"],
     "A", "OSC", "easy",
     "Washing soda is sodium carbonate decahydrate (Na2CO3.10H2O), containing ten molecules of water of crystallization."),

    ("What is the phenomenon of 'efflorescence' exhibited by washing soda crystals exposed to dry air?""",
     ["The spontaneous loss of 9 molecules of water of crystallization from Na2CO3.10H2O to form a white monohydrate powder: Na2CO3.10H2O -> Na2CO3.H2O + 9 H2O",
      "The absorption of water vapor until the crystals dissolve",
      "The explosion of crystals in sunlight",
      "The change of washing soda into diamond"],
     "A", "OSC", "medium",
     "When vapor pressure of water of crystallization exceeds ambient atmospheric humidity, decahydrate crystals lose 9 water molecules, crumbling into white monohydrate powder."),

    ("What chemical reaction explains how washing soda permanently softens hard water containing dissolved calcium chloride (CaCl2) or magnesium sulfate (MgSO4)?""",
     ["Carbonate ions precipitate soluble Ca2+ and Mg2+ ions as insoluble calcium carbonate and magnesium carbonate: CaCl2 + Na2CO3 -> CaCO3 (insoluble ppt) + 2 NaCl",
      "Washing soda boils the hard water instantly",
      "Washing soda evaporates the calcium ions into air",
      "Washing soda turns magnesium into gold"],
     "A", "OSC", "easy",
     "Soluble calcium and magnesium hardness ions react with carbonate ions to form insoluble precipitates (CaCO3 and MgCO3), removing hardness from water."),

    ("What industrial products are manufactured using sodium carbonate (washing soda) as a principal raw material?""",
     ["Glass, soap, paper, and caustic soda (NaOH)",
      "Gasoline and motor oil",
      "Computer microprocessors and silicone chips",
      "Antibiotic medicines and vaccines"],
     "A", "OSC", "easy",
     "Sodium carbonate is a cornerstone industrial chemical, fused with silica sand and limestone to make glass and boiled with fats to make soap."),

    ("What is anhydrous sodium carbonate (Na2CO3) with zero water of crystallization commonly called in chemical industry?""",
     ["Soda ash", "Baking soda", "Caustic soda", "Slaked lime"],
     "A", "OSC", "easy",
     "Anhydrous sodium carbonate obtained by heating washing soda is industrially termed soda ash."),

    ("State whether the following statement is True or False: Both baking soda and washing soda are salts of the weak acid carbonic acid (H2CO3) and strong base sodium hydroxide (NaOH).",
     ["True", "False"],
     "A", "OTF", "easy",
     "Both NaHCO3 and Na2CO3 derive from NaOH + H2CO3, yielding alkaline/basic aqueous solutions upon hydrolysis."),

    ("State whether the following statement is True or False: Pure dry sodium chloride is a deliquescent substance that turns into liquid water in dry winter air.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Pure NaCl is non-deliquescent; it only becomes damp if contaminated with magnesium chloride or calcium chloride impurities in humid air."),

    ("State whether the following statement is True or False: Washing soda can be used to remove both temporary hardness and permanent hardness from water.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Washing soda precipitates all multivalent cations (calcium and magnesium bicarbonates, chlorides, and sulfates) as insoluble carbonates, eliminating both forms of hardness."),

    ("State whether the following statement is True or False: Heating washing soda decahydrate above 100 deg C removes all 10 water molecules to yield white anhydrous soda ash.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Heating to 100 deg C expels the remaining single water molecule from Na2CO3.H2O, leaving anhydrous Na2CO3 (soda ash)."),

    ("State whether the following statement is True or False: Baking powder contains an acidic compound to neutralize the basicity of sodium carbonate.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Tartaric acid or monocalcium phosphate neutralizes the alkaline Na2CO3 formed during thermal decomposition, eliminating bitter taste."),

    # 31-40: Synthesis & Quantitative Problems
    ("In the industrial Solvay process, what four basic raw materials react together to produce sodium hydrogen carbonate (baking soda)?""",
     ["Brine (NaCl), water (H2O), ammonia (NH3), and carbon dioxide (CO2)",
      "Sulfuric acid, copper, zinc, and coal",
      "Sodium metal, chlorine gas, oxygen, and hydrogen",
      "Limestone, sand, iron ore, and charcoal"],
     "A", "OSC", "medium",
     "The Solvay reaction mixes brine, ammonia, and CO2 in water: NaCl + H2O + NH3 + CO2 -> NH4Cl + NaHCO3 (precipitates as solid crystals)."),

    ("What mass of carbon dioxide (CO2) is released by heating 168 grams of pure sodium hydrogen carbonate (NaHCO3)? (Molar mass of NaHCO3 = 84 g/mol)",
     ["44 grams (one mole of CO2)", "84 grams", "22 grams", "88 grams"],
     "A", "OSC", "hard",
     "2 NaHCO3 (168 g, 2 moles) -> Na2CO3 (106 g) + H2O (18 g) + CO2 (44 g, 1 mole). Exactly 44 g of CO2 gas is generated."),

    ("What is the percentage by mass of water of crystallization in pure washing soda crystals (Na2CO3.10H2O)? (Na = 23, C = 12, O = 16, H = 1)",
     ["Approximately 62.9% by mass",
      "Approximately 10.0%",
      "Approximately 37.1%",
      "Approximately 50.0%"],
     "A", "OSC", "hard",
     "Molar mass of Na2CO3 = 106. Molar mass of 10 H2O = 180. Total molar mass = 286 g/mol. Mass % of water = (180 / 286) * 100 \approx 62.93%."),

    ("What is the percentage by mass of water of crystallization in blue vitriol (CuSO4.5H2O)? (Cu = 63.5, S = 32, O = 16, H = 1)",
     ["Approximately 36.1% by mass",
      "Approximately 50.0%",
      "Approximately 20.0%",
      "Approximately 63.5%"],
     "A", "OSC", "hard",
     "CuSO4 = 159.5. 5 H2O = 90. Total = 249.5 g/mol. Water % = (90 / 249.5) * 100 \approx 36.07%."),

    ("Why is common salt used as an effective preservative for raw mango pickles, meat, and salted fish?""",
     ["High salt concentrations create hypertonic osmotic pressure that draws water out of bacterial and fungal cells via plasmolysis, dehydrating and killing them",
      "Salt dissolves bacteria chemically into gas",
      "Salt turns food into rock",
      "Salt produces poisonous chlorine inside food"],
     "A", "OSC", "easy",
     "Microorganisms lose intracellular water through exosmosis in high-salinity media, halting metabolic enzymes and microbial proliferation."),

    ("What is the freezing point of water when mixed with common salt (freezing mixture)?""",
     ["Depressed well below 0 deg C (down to -21 deg C)",
      "Elevated to +100 deg C",
      "Remains strictly at 0 deg C",
      "Becomes absolute zero (-273 deg C)"],
     "A", "OSC", "medium",
     "Adding solute particles lowers the chemical potential of liquid water, depressing the eutectic freezing point down to -21.1 deg C in traditional kulfi and ice-cream churns."),

    ("What is the active disinfectant gas generated at the anode during the electrolysis of brine that is used to sterilize municipal swimming pool water?""",
     ["Chlorine gas (Cl2)", "Hydrogen gas", "Oxygen gas", "Carbon dioxide"],
     "A", "OSC", "easy",
     "Anodic chlorine gas dissolves in water to form hypochlorous acid (HOCl), a powerful germicide and oxidizing biocide for water disinfection."),

    ("State whether the following statement is True or False: Sodium bicarbonate solution can be used to treat acidic bee stings.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Bee stings inject acidic formic acid; applying mildly basic baking soda paste neutralizes the acid and relieves inflammatory pain."),

    ("State whether the following statement is True or False: An aqueous solution of baking soda turns red litmus paper blue.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Because NaHCO3 is a basic salt formed from a strong base and weak acid, its aqueous solution hydrolyzes to produce OH- ions, turning red litmus blue."),

    ("Which property of washing soda allows it to remove grease and oil stains from fabric fibers during laundry washing?""",
     ["Alkaline hydrolysis converts insoluble fatty acids into water-soluble sodium soaps (saponification) and emulsifies oils",
      "Washing soda bleaches fabric with chlorine",
      "Washing soda turns oil into water vapor",
      "Washing soda makes fabric magnetic"],
     "A", "OSC", "medium",
     "The mild alkalinity (pH ~11) saponifies free fatty acids into soluble soaps while dispersing and suspending oily particulate dirt.")
]

# 30 Practice Questions
practice_data = [
    ("What gas is evolved when sodium bicarbonate reacts with dilute hydrochloric acid?""",
     ["Carbon dioxide (CO2)", "Hydrogen (H2)", "Chlorine (Cl2)", "Oxygen (O2)"],
     "A", "OSC", "easy",
     "NaHCO3 + HCl -> NaCl + H2O + CO2 (gas)."),

    ("How many molecules of water of crystallization are attached to each formula unit of washing soda?""",
     ["10 molecules (decahydrate, 10 H2O)", "5 molecules", "7 molecules", "2 molecules"],
     "A", "OSC", "easy",
     "Washing soda is sodium carbonate decahydrate (Na2CO3.10H2O)."),

    ("How many molecules of water of crystallization are present in blue vitriol (copper sulfate)?""",
     ["5 molecules (pentahydrate, 5 H2O)", "10 molecules", "7 molecules", "2 molecules"],
     "A", "OSC", "easy",
     "Blue vitriol is copper sulfate pentahydrate (CuSO4.5H2O)."),

    ("How many molecules of water of crystallization are present in green vitriol (ferrous sulfate)?""",
     ["7 molecules (heptahydrate, 7 H2O)", "5 molecules", "10 molecules", "2 molecules"],
     "A", "OSC", "easy",
     "Green vitriol is ferrous sulfate heptahydrate (FeSO4.7H2O)."),

    ("What is the common household name for sodium hydrogen carbonate?""",
     ["Baking soda", "Washing soda", "Caustic soda", "Table salt"],
     "A", "OSC", "easy",
     "Baking soda is sodium hydrogen carbonate (NaHCO3)."),

    ("What is the common commercial name for sodium hydroxide (NaOH)?""",
     ["Caustic soda", "Baking soda", "Washing soda", "Soda ash"],
     "A", "OSC", "easy",
     "Sodium hydroxide is commercially known as caustic soda due to its corrosive nature on organic tissues."),

    ("State whether the following statement is True or False: Common salt (NaCl) is used as a de-icing agent to melt winter snow on highway roads in cold countries.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Spreading salt on icy highways depresses the freezing point of water, melting ice down to -10 deg C."),

    ("State whether the following statement is True or False: Efflorescence causes washing soda crystals to gain mass by absorbing atmospheric water.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Efflorescence is the loss of water of crystallization into dry air, causing crystals to lose mass and crumble into monohydrate powder."),

    ("State whether the following statement is True or False: Baking soda is used in dry chemical fire extinguishers.",
     ["True", "False"],
     "A", "OTF", "easy",
     "NaHCO3 powder smothers flames and decomposes under fire heat to release fire-extinguishing CO2 gas."),

    ("What is the color of anhydrous copper sulfate (CuSO4) powder after all water of crystallization is driven off?""",
     ["White", "Blue", "Green", "Bright red"],
     "A", "OSC", "easy",
     "Anhydrous copper sulfate lacks ligand-field hydration splitting and is completely white."),

    # 11-20
    ("What is the primary commercial source of common salt (NaCl) on Earth?""",
     ["Solar evaporation of seawater in coastal salt pans and underground rock salt mining (halite)",
      "Direct synthesis from sodium metal and chlorine gas in factories",
      "Filtering river water",
      "Digging coal mines"],
     "A", "OSC", "easy",
     "Vast shallow coastal salt pans harness solar heat and wind to crystallize sodium chloride from evaporated ocean brine."),

    ("What happens when an aqueous solution of washing soda is tested with red litmus paper?""",
     ["The red litmus paper turns blue, confirming its basic (alkaline) nature",
      "The litmus paper turns red to yellow",
      "The litmus paper dissolves completely",
      "The litmus paper does not change color at all"],
     "A", "OSC", "easy",
     "Hydrolysis of carbonate anions produces basic hydroxide ions, turning red litmus blue."),

    ("What happens when blue litmus paper is dipped into an aqueous solution of common table salt (NaCl)?""",
     ["The blue litmus paper remains blue with zero color change, confirming neutrality",
      "The blue litmus turns bright red",
      "The litmus turns black",
      "The litmus emits smoke"],
     "A", "OSC", "easy",
     "NaCl is a neutral salt with pH = 7, causing no color change on either red or blue litmus paper."),

    ("State whether the following statement is True or False: Hard water contains dissolved calcium and magnesium hydrogencarbonates, chlorides, or sulfates.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Hardness in water is caused by multivalent metal cations, primarily Ca2+ and Mg2+."),

    ("State whether the following statement is True or False: Permanent hard water can be softened simply by boiling it in an open pot.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Boiling removes only temporary bicarbonate hardness; permanent hardness (chlorides and sulfates of Ca/Mg) requires chemical treatment like washing soda."),

    ("Why does soap fail to lather easily in hard water and instead forms a sticky curd-like scum?""",
     ["Soluble sodium soap molecules react with Ca2+ and Mg2+ ions to precipitate insoluble calcium and magnesium stearates (scum)",
      "Hard water turns soap into oil",
      "Hard water has zero density",
      "Soap evaporates immediately in hard water"],
     "A", "OSC", "easy",
     "2 C17H35COONa (soap) + Ca2+ -> (C17H35COO)2Ca (insoluble scum precipitate) + 2 Na+, wasting soap before lather can form."),

    ("Which property of baking soda makes it ideal for neutralizing battery acid spills in automobile workshops?""",
     ["It is a mild, non-caustic alkaline powder that neutralizes corrosive battery sulfuric acid safely while fizzing CO2: 2NaHCO3 + H2SO4 -> Na2SO4 + 2H2O + 2CO2",
      "It melts battery acid into water",
      "It freezes battery acid solid",
      "It makes battery acid conductive"],
     "A", "OSC", "easy",
     "Baking soda neutralizes hazardous sulfuric acid safely without generating dangerous secondary chemical burns."),

    ("What is the taste of a dilute aqueous solution of washing soda?""",
     ["A bitter, alkaline soapy taste", "A sour acidic taste", "A sweet sugary taste", "Completely salty like sea water"],
     "A", "OSC", "easy",
     "Alkaline basic solutions exhibit a characteristic bitter taste and slippery, soapy texture on skin."),

    ("How does heating baking soda make pakodas or dhokla light, crisp, and fluffy?""",
     ["Bubbles of CO2 gas generated by thermal decomposition expand and become trapped in the frying batter, creating porous air pockets",
      "It cooks the oil into ice",
      "It increases the weight of the dough",
      "It turns water into flour"],
     "A", "OSC", "easy",
     "Thermal release of CO2 bubbles expands inside the batter during frying or steaming, yielding a light, aerated spongy texture."),

    ("State whether the following statement is True or False: Alum crystals are completely insoluble in water.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Potash alum dissolves readily in warm water to release hydrated potassium, aluminium, and sulfate ions."),

    # 21-30
    ("What happens when anhydrous copper sulfate powder is exposed to humid air?""",
     ["It slowly absorbs moisture from the air to re-form blue hydrated copper sulfate crystals (CuSO4.5H2O)",
      "It turns into metallic gold",
      "It burns with a red flame",
      "It explodes violently"],
     "A", "OSC", "easy",
     "Anhydrous CuSO4 is hygroscopic, absorbing water vapor to re-establish the hydrated blue pentahydrate lattice."),

    ("What is the common name for sodium chloride crystals mined from underground mineral deposits?""",
     ["Rock salt (halite)", "Baking salt", "Glauber's salt", "Epsom salt"],
     "A", "OSC", "easy",
     "Geological rock salt deposits formed by dried ancient inland seas are mineralogically called halite."),

    ("Why is rock salt often brown or yellowish-pink in color, unlike pure white refined table salt?""",
     ["It contains natural mineral impurities such as iron oxides and clay trace minerals",
      "It is painted by miners",
      "It has been burned by underground fires",
      "It contains radioactive uranium"],
     "A", "OSC", "easy",
     "Trace iron oxide and clay sediments trapped during prehistoric evaporation impart brownish or pinkish coloration to rock salt."),

    ("State whether the following statement is True or False: Sodium carbonate is used in the manufacture of borax (Na2B4O7.10H2O).",
     ["True", "False"],
     "A", "OTF", "easy",
     "Industrial synthesis of borax reacts sodium carbonate with mineral colemanite or boric acid."),

    ("State whether the following statement is True or False: Sodium bicarbonate is an ionic compound consisting of Na+ cations and HCO3- anions.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Baking soda is an ionic salt comprising sodium cations (Na+) and polyatomic hydrogen carbonate anions (HCO3-)."),

    ("What is the chemical name and formula of 'Glauber's salt'?""",
     ["Sodium sulfate decahydrate (Na2SO4.10H2O)", "Sodium chloride", "Magnesium sulfate", "Copper sulfate"],
     "A", "OSC", "easy",
     "Glauber's salt is sodium sulfate decahydrate (Na2SO4.10H2O), named after the 17th-century chemist Johann Rudolf Glauber."),

    ("Why is washing soda dissolved in water before washing greasy garage overalls?""",
     ["It saponifies greasy fats and breaks grease into small water-dispersible droplets (emulsification)",
      "It dissolves the cotton fabric away",
      "It turns grease into solid stone",
      "It bleaches the grease with chlorine"],
     "A", "OSC", "easy",
     "Alkaline washing soda hydrolyzes fatty grease into water-soluble soap molecules, lifting oily soils from clothing fibers."),

    ("What gas is collected at the cathode in the chlor-alkali process, and what is its clean energy application?""",
     ["Hydrogen gas (H2), utilized as a zero-emission fuel for hydrogen fuel cells and industrial ammonia fertilizer synthesis",
      "Oxygen gas",
      "Chlorine gas",
      "Carbon monoxide"],
     "A", "OSC", "easy",
     "Cathodic hydrogen is a valuable clean fuel and chemical feedstock for Haber-Bosch ammonia production."),

    ("What happens when baking soda is heated above 270 deg C?""",
     ["It decomposes completely into anhydrous sodium carbonate (soda ash), water, and carbon dioxide",
      "It melts into clear liquid glass",
      "It turns into pure carbon diamond",
      "It freezes into dry ice"],
     "A", "OSC", "easy",
     "Above 100-270 deg C, all sodium bicarbonate decomposes into anhydrous Na2CO3, steam, and CO2."),

    ("What is the pH range of a concentrated baking soda (NaHCO3) solution in water?""",
     ["Mildly alkaline (pH approximately 8.3 to 8.5)",
      "Extremely acidic (pH = 1.0)",
      "Extremely alkaline (pH = 14.0)",
      "Neutral (pH = 7.0 strictly)"],
     "A", "OSC", "medium",
     "Because HCO3- is amphiprotic with a small base dissociation constant, its solution is mildly alkaline at pH ~8.3.")
]

# 12 Mock Questions with Vector SVG Diagrams
mock_data = [
    # 71: Chlor-Alkali Electrolytic Cell Diagram
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="200" viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="200" fill="#0f172a" rx="8"/>
  <rect x="40" y="40" width="260" height="120" fill="#1e293b" stroke="#64748b" stroke-width="2" rx="4"/>
  <rect x="45" y="70" width="250" height="85" fill="#0284c7" opacity="0.3"/>
  <!-- Anode (+) -->
  <rect x="80" y="45" width="20" height="90" fill="#ef4444" rx="2"/>
  <text x="70" y="32" fill="#ef4444" font-size="8" font-weight="bold">(+) Anode</text>
  <text x="65" y="150" fill="#fca5a5" font-size="8">2Cl- -> Cl2 + 2e-</text>
  <path d="M 90 45 L 90 20" stroke="#facc15" stroke-width="2"/>
  <text x="65" y="15" fill="#facc15" font-size="8" font-weight="bold">Cl2 Gas \uparrow</text>
  <!-- Cathode (-) -->
  <rect x="240" y="45" width="20" height="90" fill="#22c55e" rx="2"/>
  <text x="230" y="32" fill="#22c55e" font-size="8" font-weight="bold">(-) Cathode</text>
  <text x="210" y="150" fill="#86efac" font-size="8">2H+ + 2e- -> H2</text>
  <path d="M 250 45 L 250 20" stroke="#38bdf8" stroke-width="2"/>
  <text x="235" y="15" fill="#38bdf8" font-size="8" font-weight="bold">H2 Gas \uparrow</text>
  <!-- Porous membrane in middle -->
  <line x1="170" y1="40" x2="170" y2="160" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,3"/>
  <text x="135" y="100" fill="#fde68a" font-size="8">NaOH Solution Formed</text>
  <text x="35" y="180" fill="#4ade80" font-size="9">2 NaCl + 2 H2O --(Electricity)--> 2 NaOH + Cl2 \uparrow + H2 \uparrow</text>
</svg>
</div>
The schematic shows the industrial chlor-alkali process. What valuable alkali solution is harvested from the electrolyte during this electrolytic decomposition of concentrated brine?""",
     ["Sodium hydroxide (caustic soda, NaOH)",
      "Sodium carbonate",
      "Calcium hydroxide",
      "Hydrochloric acid"],
     "A", "easy",
     "As chloride ions oxidize at the anode to form Cl2 gas and hydrogen ions reduce at the cathode to form H2 gas, remaining Na+ and OH- ions combine to produce sodium hydroxide (NaOH)."),

    # 72: Water of Crystallization Heating Experiment
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="50" y="60" width="130" height="30" fill="#334155" stroke="#94a3b8" rx="3"/>
  <!-- Blue crystals turning white -->
  <rect x="55" y="65" width="40" height="20" fill="#0284c7"/>
  <text x="56" y="78" fill="#ffffff" font-size="7">Blue CuSO4.5H2O</text>
  <rect x="95" y="65" width="40" height="20" fill="#f8fafc"/>
  <text x="96" y="78" fill="#0f172a" font-size="7">White Anhydrous</text>
  <!-- Condensed water drops near mouth -->
  <circle cx="160" cy="65" r="3" fill="#38bdf8"/>
  <circle cx="170" cy="70" r="3" fill="#38bdf8"/>
  <text x="165" y="55" fill="#38bdf8" font-size="8">H2O drops</text>
  <!-- Burner flame below -->
  <polygon points="75,95 85,115 95,95" fill="#ef4444"/>
  <text x="75" y="130" fill="#f87171" font-size="8">Heat</text>
  <text x="45" y="160" fill="#facc15" font-size="9">CuSO4.5H2O (Blue) --(Heat)--> CuSO4 (White) + 5 H2O \uparrow</text>
  <text x="45" y="175" fill="#a7f3d0" font-size="8">Adding a drop of water immediately restores the vibrant blue color</text>
</svg>
</div>
What does the thermal dehydration experiment illustrated above prove about crystalline copper sulfate?""",
     ["The blue color is dependent on the presence of chemically bonded water of crystallization in the crystal lattice",
      "Copper sulfate is made of pure ice",
      "Heating copper sulfate destroys the copper atoms",
      "Water of crystallization is trapped as liquid pools inside"],
     "A", "easy",
     "Coordinated water molecules split d-orbitals in Cu2+ to produce blue light absorption; driving off water of crystallization collapses this ligand field, leaving white anhydrous CuSO4."),

    # 73: Solvay Process Flow Diagram
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Reactants Inputs -->
  <rect x="20" y="30" width="80" height="25" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="25" y="46" fill="#38bdf8" font-size="8">Brine (NaCl)</text>
  <rect x="20" y="65" width="80" height="25" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="25" y="81" fill="#38bdf8" font-size="8">Ammonia (NH3)</text>
  <rect x="20" y="100" width="80" height="25" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="25" y="116" fill="#38bdf8" font-size="8">CO2 Gas</text>
  <!-- Mixing Tower -->
  <line x1="105" y1="80" x2="145" y2="80" stroke="#facc15" stroke-width="2"/>
  <polygon points="145,76 155,80 145,84" fill="#facc15"/>
  <rect x="155" y="45" width="70" height="70" fill="#334155" stroke="#94a3b8" rx="4"/>
  <text x="160" y="75" fill="#fde68a" font-size="8" font-weight="bold">Carbonating</text>
  <text x="170" y="90" fill="#fde68a" font-size="8" font-weight="bold">Tower</text>
  <!-- Precipitation of NaHCO3 -->
  <line x1="230" y1="80" x2="265" y2="80" stroke="#facc15" stroke-width="2"/>
  <polygon points="265,76 275,80 265,84" fill="#facc15"/>
  <rect x="275" y="55" width="55" height="50" fill="#1e293b" stroke="#4ade80" rx="3"/>
  <text x="280" y="78" fill="#4ade80" font-size="8" font-weight="bold">NaHCO3</text>
  <text x="280" y="92" fill="#ffffff" font-size="7">Precipitate</text>
  <text x="35" y="150" fill="#facc15" font-size="9">NaCl + H2O + NH3 + CO2 \rightarrow NH4Cl + NaHCO3 \downarrow</text>
  <text x="35" y="170" fill="#a7f3d0" font-size="8">Precipitated sodium bicarbonate is filtered, dried, and packaged as baking soda</text>
</svg>
</div>
Which sparingly soluble compound precipitates out of solution in the carbonating tower of the industrial Solvay process?""",
     ["Sodium hydrogen carbonate (baking soda, NaHCO3)",
      "Sodium chloride",
      "Ammonium chloride",
      "Calcium sulfate"],
     "A", "medium",
     "Because sodium hydrogen carbonate (NaHCO3) has low solubility in cold brine containing ammonium chloride, it crystallizes out as a solid precipitate and is filtered off."),

    # 74: Baking Powder Neutralization Chemistry
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="25" y="40" width="135" height="85" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="35" y="60" fill="#f87171" font-size="8" font-weight="bold">Baking Soda Alone:</text>
  <text x="35" y="80" fill="#cbd5e1" font-size="8">2 NaHCO3 --(Heat)--> Na2CO3</text>
  <text x="35" y="98" fill="#facc15" font-size="8">Leaves basic Na2CO3 in cake</text>
  <text x="35" y="115" fill="#ef4444" font-size="8" font-weight="bold">Result: Bitter, soapy taste!</text>
  <rect x="180" y="40" width="135" height="85" fill="#1e293b" stroke="#22c55e" rx="4"/>
  <text x="190" y="60" fill="#4ade80" font-size="8" font-weight="bold">Baking Powder Solution:</text>
  <text x="190" y="80" fill="#cbd5e1" font-size="8">NaHCO3 + H+ (Tartaric Acid)</text>
  <text x="190" y="98" fill="#cbd5e1" font-size="8">\rightarrow Na-tartrate + CO2 \uparrow</text>
  <text x="190" y="115" fill="#22c55e" font-size="8" font-weight="bold">Result: Fluffy, sweet cake!</text>
  <text x="45" y="150" fill="#fde68a" font-size="9">Why Baking Powder Contains Tartaric Acid</text>
  <text x="45" y="170" fill="#38bdf8" font-size="8">Tartaric acid neutralizes alkaline Na2CO3, eliminating bitterness completely</text>
</svg>
</div>
Why is tartaric acid incorporated into commercial baking powder alongside sodium bicarbonate?""",
     ["It neutralizes basic sodium carbonate (Na2CO3) produced by heating, preventing a bitter soapy taste while boosting CO2 generation",
      "It makes the cake dough heavy",
      "It prevents bread from rising",
      "It acts as a sweet icing glaze"],
     "A", "medium",
     "Thermal decomposition of NaHCO3 leaves alkaline Na2CO3, which tastes bitter. Edible tartaric acid neutralizes Na2CO3 into neutral sodium tartrate, ensuring a pleasant taste and soft texture."),

    # 75: Efflorescence of Washing Soda Decahydrate
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="30" y="45" width="110" height="70" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
  <text x="35" y="65" fill="#38bdf8" font-size="9" font-weight="bold">Fresh Crystals</text>
  <text x="35" y="85" fill="#cbd5e1" font-size="8">Na2CO3.10H2O</text>
  <text x="35" y="100" fill="#cbd5e1" font-size="8">Transparent Glassy</text>
  <line x1="145" y1="80" x2="200" y2="80" stroke="#facc15" stroke-width="2.5"/>
  <polygon points="200,76 210,80 200,84" fill="#facc15"/>
  <text x="148" y="70" fill="#facc15" font-size="8">Dry Air Exposure</text>
  <rect x="210" y="45" width="105" height="70" fill="#1e293b" stroke="#facc15" stroke-width="1.5" rx="4"/>
  <text x="215" y="65" fill="#facc15" font-size="9" font-weight="bold">Effloresced</text>
  <text x="215" y="85" fill="#cbd5e1" font-size="8">Na2CO3.H2O</text>
  <text x="215" y="100" fill="#ffffff" font-size="8">White Opaque Powder</text>
  <text x="45" y="145" fill="#4ade80" font-size="9">Efflorescence: Na2CO3.10H2O \rightarrow Na2CO3.H2O + 9 H2O \uparrow</text>
  <text x="45" y="165" fill="#cbd5e1" font-size="8">Loss of 9 molecules of water of crystallization when exposed to dry atmosphere</text>
</svg>
</div>
What physical phenomenon causes clear, glassy washing soda crystals to turn into a white opaque powder when left open in dry air?""",
     ["Efflorescence: the crystals spontaneously lose 9 molecules of water of crystallization to dry air, forming a monohydrate powder",
      "Deliquescence: the crystals absorb moisture until they dissolve",
      "Sublimation directly into gas",
      "Combustion with atmospheric oxygen"],
     "A", "easy",
     "Efflorescence occurs when the vapor pressure of water of crystallization exceeds ambient humidity, driving out 9 water molecules: Na2CO3.10H2O -> Na2CO3.H2O + 9H2O."),

    # 76: Permanent Hard Water Softening Reaction
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="25" y="40" width="105" height="70" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="35" y="60" fill="#f87171" font-size="9" font-weight="bold">Hard Water</text>
  <text x="35" y="80" fill="#cbd5e1" font-size="8">Dissolved Ca2+, Mg2+</text>
  <text x="35" y="95" fill="#fde68a" font-size="8">(CaCl2, MgSO4)</text>
  <line x1="135" y1="75" x2="195" y2="75" stroke="#facc15" stroke-width="2.5"/>
  <polygon points="195,71 205,75 195,79" fill="#facc15"/>
  <text x="140" y="65" fill="#facc15" font-size="8">+ Na2CO3</text>
  <rect x="205" y="40" width="110" height="70" fill="#1e293b" stroke="#22c55e" rx="4"/>
  <text x="215" y="60" fill="#4ade80" font-size="9" font-weight="bold">Softened Water</text>
  <text x="215" y="80" fill="#ffffff" font-size="8">CaCO3 \downarrow + MgCO3 \downarrow</text>
  <text x="215" y="95" fill="#86efac" font-size="8">Insoluble precipitate</text>
  <text x="35" y="145" fill="#38bdf8" font-size="9">CaCl2 (aq) + Na2CO3 (aq) \rightarrow CaCO3 \downarrow (s) + 2 NaCl (aq)</text>
  <text x="35" y="165" fill="#cbd5e1" font-size="8">Precipitating hardness ions allows soap to lather instantly without scum</text>
</svg>
</div>
How does adding washing soda (sodium carbonate) remove permanent hardness from water?""",
     ["Carbonate ions precipitate dissolved calcium and magnesium ions as insoluble carbonates (CaCO3 and MgCO3), which settle out",
      "Washing soda evaporates the calcium atoms",
      "Washing soda turns calcium into sodium",
      "Washing soda freezes the magnesium ions"],
     "A", "easy",
     "Carbonate ions (CO3^2-) react with divalent Ca2+ and Mg2+ hardness ions to form insoluble carbonate precipitates, eliminating hardness."),

    # 77: Antacid Neutralization of Stomach Acid
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <path d="M 80 40 C 40 60 40 120 80 140 C 130 150 160 120 150 80 C 160 50 120 30 80 40 Z" fill="#7f1d1d" opacity="0.4" stroke="#ef4444" stroke-width="2"/>
  <text x="65" y="65" fill="#fca5a5" font-size="8">Stomach</text>
  <text x="60" y="95" fill="#f87171" font-size="9" font-weight="bold">Excess HCl (pH ~ 1.5)</text>
  <line x1="160" y1="90" x2="210" y2="90" stroke="#facc15" stroke-width="2"/>
  <polygon points="210,86 220,90 210,94" fill="#facc15"/>
  <text x="165" y="80" fill="#facc15" font-size="8">+ NaHCO3</text>
  <rect x="220" y="55" width="105" height="70" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="225" y="75" fill="#38bdf8" font-size="8" font-weight="bold">Neutralized:</text>
  <text x="225" y="90" fill="#cbd5e1" font-size="8">NaCl + H2O</text>
  <text x="225" y="105" fill="#4ade80" font-size="8">+ CO2 \uparrow (burp)</text>
  <text x="225" y="118" fill="#4ade80" font-size="8">pH normalized</text>
  <text x="45" y="165" fill="#facc15" font-size="9">NaHCO3 (s) + HCl (aq) \rightarrow NaCl (aq) + H2O (l) + CO2 (g)</text>
</svg>
</div>
What chemical neutralization reaction takes place when a patient drinks an antacid solution containing sodium bicarbonate (baking soda)?""",
     ["NaHCO3 safely neutralizes hyper-acidic stomach hydrochloric acid to form sodium chloride, water, and carbon dioxide gas",
      "NaHCO3 freezes the stomach lining",
      "NaHCO3 stops blood flow to the digestive tract",
      "NaHCO3 oxidizes stomach acid into sulfuric acid"],
     "A", "easy",
     "Sodium bicarbonate is a mild alkaline salt that neutralizes excess gastric HCl: NaHCO3 + HCl -> NaCl + H2O + CO2, quickly restoring comfortable gastric pH."),

    # 78: Deliquescence of Sea Salt Impurities
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="25" y="35" width="135" height="110" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="35" y="55" fill="#38bdf8" font-size="9" font-weight="bold">Pure NaCl</text>
  <text x="35" y="75" fill="#cbd5e1" font-size="8">- Non-deliquescent</text>
  <text x="35" y="90" fill="#cbd5e1" font-size="8">- Stays dry & powdery</text>
  <text x="35" y="105" fill="#cbd5e1" font-size="8">- Does not absorb H2O</text>
  <text x="35" y="130" fill="#4ade80" font-size="8">Dry crystalline salt</text>
  <rect x="180" y="35" width="135" height="110" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="190" y="55" fill="#fbbf24" font-size="9" font-weight="bold">Unrefined Table Salt</text>
  <text x="190" y="75" fill="#cbd5e1" font-size="8">- Contains MgCl2, CaCl2</text>
  <text x="190" y="90" fill="#cbd5e1" font-size="8">- Highly deliquescent</text>
  <text x="190" y="105" fill="#f87171" font-size="8">- Absorbs monsoon moisture</text>
  <text x="190" y="130" fill="#f87171" font-size="8">Turns damp & clumpy</text>
  <text x="45" y="170" fill="#fde68a" font-size="9">Deliquescent impurities MgCl2 and CaCl2 cause monsoon dampness</text>
</svg>
</div>
Why does common unrefined table salt turn damp and clumpy during humid rainy weather?""",
     ["It contains traces of deliquescent magnesium chloride (MgCl2) and calcium chloride (CaCl2) impurities that absorb water vapor from humid air",
      "Pure sodium chloride turns into liquid water in rain",
      "Salt molecules decompose into liquid hydrogen",
      "Air turns into liquid salt"],
     "A", "medium",
     "While 100% pure NaCl is non-deliquescent, unrefined sea salt retains trace MgCl2 and CaCl2 impurities, which absorb atmospheric humidity and dissolve in it."),

    # 79: Double Salt Crystal Lattice of Alum
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <polygon points="170,30 240,100 170,170 100,100" fill="#0284c7" opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
  <line x1="100" y1="100" x2="240" y2="100" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="170" y1="30" x2="170" y2="170" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="110" y="95" fill="#fde68a" font-size="9" font-weight="bold">Potash Alum Octahedron</text>
  <text x="50" y="20" fill="#38bdf8" font-size="10" font-weight="bold">K2SO4 . Al2(SO4)3 . 24 H2O</text>
  <text x="45" y="180" fill="#4ade80" font-size="9">Octahedral crystal habit containing exactly 24 water of crystallization molecules</text>
</svg>
</div>
How many molecules of water of crystallization are chemically bound inside the crystal lattice of one formula unit of potash alum (fitkari)?""",
     ["24 molecules of water (24 H2O)",
      "10 molecules of water",
      "5 molecules of water",
      "12 molecules of water"],
     "A", "easy",
     "Potash alum is a double sulfate dodecahydrate with formula K2SO4.Al2(SO4)3.24H2O, containing 24 molecules of water of crystallization."),

    # 80: Freezing Mixture Temperature Depression
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="180" viewBox="0 0 340 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="180" fill="#0f172a" rx="8"/>
  <rect x="50" y="40" width="100" height="110" fill="#334155" stroke="#94a3b8" rx="4"/>
  <text x="60" y="60" fill="#38bdf8" font-size="9" font-weight="bold">Pure Ice</text>
  <text x="60" y="80" fill="#cbd5e1" font-size="8">Melting Point:</text>
  <text x="60" y="100" fill="#38bdf8" font-size="12" font-weight="bold">0^{\circ}C</text>
  <rect x="190" y="40" width="115" height="110" fill="#1e293b" stroke="#facc15" rx="4"/>
  <text x="195" y="60" fill="#facc15" font-size="9" font-weight="bold">Ice + Salt (Freezing Mix)</text>
  <text x="195" y="80" fill="#cbd5e1" font-size="8">Depressed Freezing Point:</text>
  <text x="195" y="105" fill="#ef4444" font-size="12" font-weight="bold">-21.1^{\circ}C</text>
  <text x="45" y="165" fill="#fde68a" font-size="9">Eutectic freezing point depression freezes traditional kulfi and ice creams</text>
</svg>
</div>
Why is common salt (NaCl) blended with crushed ice in traditional hand-cranked ice cream churns?""",
     ["It depresses the freezing point of water well below 0 deg C (down to -21 deg C), creating a freezing mixture that rapidly freezes ice cream cream",
      "It makes the ice cream taste salty",
      "It prevents the wooden churn from catching fire",
      "It melts all the ice into steam"],
     "A", "medium",
     "Dissolving salt in ice depresses the chemical freezing point to the eutectic temperature of -21.1 deg C, providing cryogenic chilling to freeze dessert creams."),

    # 81: Soap Saponification with Caustic Soda
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="25" y="45" width="100" height="70" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="35" y="65" fill="#fbbf24" font-size="9" font-weight="bold">Fat / Oil</text>
  <text x="35" y="80" fill="#cbd5e1" font-size="8">(Glyceryl ester)</text>
  <text x="35" y="98" fill="#facc15" font-size="8">+ Conc. NaOH</text>
  <line x1="130" y1="80" x2="190" y2="80" stroke="#facc15" stroke-width="2"/>
  <polygon points="190,76 200,80 190,84" fill="#facc15"/>
  <text x="140" y="70" fill="#facc15" font-size="8">Boil / Heat</text>
  <rect x="200" y="45" width="115" height="70" fill="#1e293b" stroke="#4ade80" rx="4"/>
  <text x="210" y="65" fill="#4ade80" font-size="9" font-weight="bold">Soap + Glycerol</text>
  <text x="210" y="85" fill="#cbd5e1" font-size="8">Soap precipitates</text>
  <text x="210" y="100" fill="#38bdf8" font-size="8">when NaCl added</text>
  <text x="45" y="145" fill="#facc15" font-size="9">Saponification: Fat + 3 NaOH \rightarrow Glycerol + 3 Soap (R-COONa)</text>
  <text x="45" y="165" fill="#cbd5e1" font-size="8">Common salt (NaCl) is added to precipitate ('salt out') solid soap from the lye</text>
</svg>
</div>
What role does common salt (NaCl) play during the final stage of commercial soap manufacturing?""",
     ["It precipitates (salts out) the solid soap from solution by drastically lowering its solubility through the common-ion effect",
      "It adds perfume to the soap",
      "It bleaches the soap into clear water",
      "It turns soap into shampoo"],
     "A", "medium",
     "Adding solid NaCl increases Na+ concentration, driving sodium soap past its solubility limit so it precipitates ('salting out') and floats to the top of the lye vat."),

    # 82: Acidic vs Basic Salt Litmus Test
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="25" y="35" width="85" height="110" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="35" y="55" fill="#38bdf8" font-size="9" font-weight="bold">NaCl (aq)</text>
  <text x="35" y="75" fill="#cbd5e1" font-size="8">Strong + Strong</text>
  <text x="35" y="95" fill="#4ade80" font-size="9" font-weight="bold">pH = 7</text>
  <text x="35" y="125" fill="#94a3b8" font-size="8">Neutral Litmus</text>
  <rect x="127" y="35" width="85" height="110" fill="#1e293b" stroke="#ef4444" rx="3"/>
  <text x="135" y="55" fill="#f87171" font-size="9" font-weight="bold">NH4Cl (aq)</text>
  <text x="135" y="75" fill="#cbd5e1" font-size="8">Strong + Weak</text>
  <text x="135" y="95" fill="#ef4444" font-size="9" font-weight="bold">pH < 7</text>
  <text x="135" y="125" fill="#f87171" font-size="8">Turns Litmus Red</text>
  <rect x="230" y="35" width="85" height="110" fill="#1e293b" stroke="#22c55e" rx="3"/>
  <text x="238" y="55" fill="#4ade80" font-size="9" font-weight="bold">Na2CO3 (aq)</text>
  <text x="238" y="75" fill="#cbd5e1" font-size="8">Weak + Strong</text>
  <text x="238" y="95" fill="#4ade80" font-size="9" font-weight="bold">pH > 7</text>
  <text x="238" y="125" fill="#38bdf8" font-size="8">Turns Litmus Blue</text>
  <text x="45" y="170" fill="#fde68a" font-size="9">Salt Hydrolysis Governs the Acidic, Neutral, or Basic Nature of Salts</text>
</svg>
</div>
What type of litmus color change occurs when red litmus paper is dipped into an aqueous solution of washing soda (Na2CO3)?""",
     ["The red litmus paper turns blue, confirming its basic (alkaline) nature due to anion hydrolysis",
      "The litmus paper turns red to yellow",
      "The litmus paper turns black",
      "No color change occurs"],
     "A", "easy",
     "Na2CO3 is formed from strong base NaOH and weak acid H2CO3. Carbonate ions hydrolyze in water to produce hydroxide ions (OH-), turning red litmus blue.")
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

    out_file = "scripts/ch14_topic1.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {TOPIC_CODE} -> {out_file}")

if __name__ == "__main__":
    generate()
