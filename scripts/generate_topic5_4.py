# scripts/generate_topic5_4.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-5-5.4"
CHAPTER_NUM = 5

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: Types of salts and aqueous pH
    ("""What is the pH of an aqueous solution of a salt formed by a STRONG ACID and a STRONG BASE (e.g. \\(\\text{NaCl}, \\text{K}_2\\text{SO}_4\\))?""",
     ["\\(\\text{pH} < 7\\) (Acidic)",
      "\\(\\text{pH} = 7.0\\) (Strictly neutral)",
      "\\(\\text{pH} > 7\\) (Basic)",
      "\\(\\text{pH} = 0\\)"],
     "B", "OSC", "easy",
     "• When strong acid and strong base neutralize, neither ion undergoes significant hydrolysis; the resulting salt solution has a neutral pH of 7.0.\nCorrect Choice is (B)."),

    ("""What is the pH of an aqueous solution of a salt formed from a STRONG ACID and a WEAK BASE (e.g. Ammonium chloride, \\(\\text{NH}_4\\text{Cl}\\))?""",
     ["\\(\\text{pH} < 7\\) (Acidic)",
      "\\(\\text{pH} = 7\\) (Neutral)",
      "\\(\\text{pH} > 7\\) (Basic)",
      "\\(\\text{pH} = 14\\)"],
     "A", "OSC", "easy",
     "• Ammonium chloride hydrolyzes in water: \\(\\text{NH}_4^+ + \\text{H}_2\\text{O} \\rightleftharpoons \\text{NH}_4\\text{OH} + \\text{H}^+\\), generating excess \\(\\text{H}^+\\) ions that make the solution acidic (\\(\\text{pH} < 7\\)).\nCorrect Choice is (A)."),

    ("""What is the pH of an aqueous solution of a salt formed from a WEAK ACID and a STRONG BASE (e.g. Sodium acetate \\(\\text{CH}_3\\text{COONa}\\) or Sodium carbonate \\(\\text{Na}_2\\text{CO}_3\\))?""",
     ["\\(\\text{pH} < 7\\) (Acidic)",
      "\\(\\text{pH} = 7\\) (Neutral)",
      "\\(\\text{pH} > 7\\) (Basic / Alkaline)",
      "\\(\\text{pH} = 1\\)"],
     "C", "OSC", "easy",
     "• Acetate/carbonate ions undergo anion hydrolysis: \\(\\text{CH}_3\\text{COO}^- + \\text{H}_2\\text{O} \\rightleftharpoons \\text{CH}_3\\text{COOH} + \\text{OH}^-\\), generating excess \\(\\text{OH}^-\\) ions (\\(\\text{pH} > 7\\)).\nCorrect Choice is (C)."),

    ("""Which of the following salts dissolves in water to form a distinctly ACIDIC solution (turning blue litmus red)?""",
     ["Sodium chloride (\\(\\text{NaCl}\\))",
      "Potassium nitrate (\\(\\text{KNO}_3\\))",
      "Copper(II) sulphate (\\(\\text{CuSO}_4\\))",
      "Sodium carbonate (\\(\\text{Na}_2\\text{CO}_3\\))"],
     "C", "OSC", "medium",
     "• \\(\\text{CuSO}_4\\) is derived from strong acid \\(\\text{H}_2\\text{SO}_4\\) and weak base \\(\\text{Cu(OH)}_2\\). Cationic hydrolysis yields excess \\(\\text{H}^+\\), making it acidic.\nCorrect Choice is (C)."),

    ("""Which of the following salts dissolves in water to form a BASIC solution (turning red litmus blue)?""",
     ["Sodium carbonate (\\(\\text{Na}_2\\text{CO}_3\\))",
      "Ammonium chloride (\\(\\text{NH}_4\\text{Cl}\\))",
      "Sodium chloride (\\(\\text{NaCl}\\))",
      "Aluminium chloride (\\(\\text{AlCl}_3\\))"],
     "A", "OSC", "easy",
     "• \\(\\text{Na}_2\\text{CO}_3\\) is the salt of a weak acid (\\(\\text{H}_2\\text{CO}_3\\)) and strong base (\\(\\text{NaOH}\\)); its solution is distinctly alkaline.\nCorrect Choice is (A)."),

    ("""What is 'WATER OF CRYSTALLIZATION'?""",
     ["Water added to dilute a solution",
      "The fixed number of water molecules chemically bonded into the geometric crystal structure of a salt in definite stoichiometric proportion",
      "Moisture condensed on the outside of a beaker",
      "Water that has been boiled to 100°C"],
     "B", "OSC", "easy",
     "• Water of crystallization represents a stoichiometric number of water molecules integrated into the salt crystal lattice.\nCorrect Choice is (B)."),

    ("""How many molecules of water of crystallization are present in one formula unit of Copper(II) Sulphate (Blue vitriol, \\(\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}\\))?""",
     ["2", "5", "7", "10"],
     "B", "OSC", "easy",
     "• Blue vitriol contains exactly 5 molecules of water of crystallization: \\(\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    ("""What happens to blue vitriol crystals (\\(\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}\\)) when heated strongly in a dry test tube?""",
     ["They melt into red copper metal",
      "They lose their water of crystallization, turning into a white amorphous anhydrous powder (\\(\\text{CuSO}_4\\)), while droplets of condensed water appear on the cooler upper walls of the test tube",
      "They burn with a green flash",
      "They turn into black charcoal"],
     "B", "OSC", "medium",
     "• Heating removes the 5 water molecules: \\(\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O (blue)} \\xrightarrow{\\Delta} \\text{CuSO}_4\\text{ (white anhydrous)} + 5\\text{H}_2\\text{O}\\uparrow\\).\nCorrect Choice is (B)."),

    ("""What happens when a few drops of liquid water are added to the white anhydrous \\(\\text{CuSO}_4\\) powder obtained after heating?""",
     ["It explodes immediately",
      "The white powder regains its characteristic blue color and crystal form in an exothermic reaction",
      "It turns yellow",
      "It decomposes into copper gas"],
     "B", "OSC", "easy",
     "• Re-hydration restores the blue copper-hydrate complex: \\(\\text{CuSO}_4 + 5\\text{H}_2\\text{O} \\to \\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    ("""How many molecules of water of crystallization are present in Ferrous Sulphate crystals (Green vitriol, \\(\\text{FeSO}_4 \\cdot 7\\text{H}_2\\text{O}\\))?""",
     ["2", "5", "7", "10"],
     "C", "OSC", "easy",
     "• Green vitriol is ferrous sulphate heptahydrate: \\(\\text{FeSO}_4 \\cdot 7\\text{H}_2\\text{O}\\).\nCorrect Choice is (C)."),

    # 11-20: Hydrated salts: Washing soda, Gypsum, POP, Alum
    ("""What is the chemical formula of Washing Soda crystals?""",
     ["\\(\\text{NaHCO}_3\\)",
      "\\(\\text{Na}_2\\text{CO}_3 \\cdot 10\\text{H}_2\\text{O}\\) (Sodium carbonate decahydrate)",
      "\\(\\text{Na}_2\\text{CO}_3 \\cdot \\text{H}_2\\text{O}\\)",
      "\\(\\text{NaOH}\\)"],
     "B", "OSC", "easy",
     "• Washing soda is sodium carbonate decahydrate: \\(\\text{Na}_2\\text{CO}_3 \\cdot 10\\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    ("""What is the phenomenon called when washing soda crystals (\\(\\text{Na}_2\\text{CO}_3 \\cdot 10\\text{H}_2\\text{O}\\)) lose 9 water molecules on exposure to dry air, turning into a white powder?""",
     ["Deliquescence", "Efflorescence", "Sublimation", "Hydrolysis"],
     "B", "OSC", "medium",
     "• Efflorescence is the spontaneous loss of water of crystallization from a hydrated salt exposed to air.\nCorrect Choice is (B)."),

    ("""What is the chemical formula of Gypsum?""",
     ["\\(\\text{CaSO}_4 \\cdot \\frac{1}{2}\\text{H}_2\\text{O}\\)",
      "\\(\\text{CaSO}_4 \\cdot 2\\text{H}_2\\text{O}\\) (Calcium sulphate dihydrate)",
      "\\(\\text{CaCO}_3\\)",
      "\\(\\text{CaO}\\)"],
     "B", "OSC", "easy",
     "• Gypsum is calcium sulphate dihydrate: \\(\\text{CaSO}_4 \\cdot 2\\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    ("""What is the chemical formula of Plaster of Paris (POP)?""",
     ["\\(\\text{CaSO}_4 \\cdot 2\\text{H}_2\\text{O}\\)",
      "\\(\\text{CaSO}_4 \\cdot \\frac{1}{2}\\text{H}_2\\text{O}\\) (Calcium sulphate hemihydrate)",
      "\\(\\text{Ca(OH)}_2\\)",
      "\\(\\text{CaCO}_3\\)"],
     "B", "OSC", "easy",
     "• Plaster of Paris is calcium sulphate hemihydrate: \\(\\text{CaSO}_4 \\cdot \\frac{1}{2}\\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    ("""At what controlled temperature must Gypsum be heated to manufacture Plaster of Paris?""",
     ["\\(100^\\circ\\text{C}\\ (373\\text{ K})\\)",
      "\\(500^\\circ\\text{C}\\ (773\\text{ K})\\)",
      "\\(0^\\circ\\text{C}\\)",
      "\\(1000^\\circ\\text{C}\\)"],
     "A", "OSC", "medium",
     "• Gypsum is carefully heated to \\(100^\\circ\\text{C}\\ (373\\text{ K})\\): \\(\\text{CaSO}_4 \\cdot 2\\text{H}_2\\text{O} \\to \\text{CaSO}_4 \\cdot \\frac{1}{2}\\text{H}_2\\text{O} + 1\\frac{1}{2}\\text{H}_2\\text{O}\\).\nCorrect Choice is (A)."),

    ("""What happens if Gypsum is overheated above \\(100^\\circ\\text{C}\\) (e.g. at \\(200^\\circ\\text{C}\\))?""",
     ["It turns into liquid water",
      "It loses all its water of crystallization completely, forming anhydrous calcium sulphate ('dead burnt plaster') which loses the property of setting with water",
      "It becomes magnetic",
      "It explodes"],
     "B", "OSC", "medium",
     "• Overheating completely dehydrates gypsum into anhydrous \\(\\text{CaSO}_4\\) ('dead burnt plaster'), which no longer sets upon adding water.\nCorrect Choice is (B)."),

    ("""Why does Plaster of Paris set into a hard, rigid solid mass within 10 to 15 minutes of mixing with water?""",
     ["It freezes water into ice",
      "It re-absorbs water to re-form interlocking needle-like crystals of hard Gypsum: \\(\\text{CaSO}_4 \\cdot \\frac{1}{2}\\text{H}_2\\text{O} + 1\\frac{1}{2}\\text{H}_2\\text{O} \\to \\text{CaSO}_4 \\cdot 2\\text{H}_2\\text{O}\\)",
      "It reacts with carbon dioxide to form marble",
      "It evaporates completely"],
     "B", "OSC", "easy",
     "• Hydration recrystallizes POP into a densely felted mesh of gypsum crystals, resulting in setting and slight expansion.\nCorrect Choice is (B)."),

    ("""What is the full chemical formula of Potash Alum (Fitkari)?""",
     ["\\(\\text{K}_2\\text{SO}_4 \\cdot \\text{Al}_2(\\text{SO}_4)_3 \\cdot 24\\text{H}_2\\text{O}\\)",
      "\\(\\text{KAlSO}_4\\)",
      "\\(\\text{K}_2\\text{CO}_3 \\cdot 10\\text{H}_2\\text{O}\\)",
      "\\(\\text{Al}_2(\\text{SO}_4)_3 \\cdot 12\\text{H}_2\\text{O}\\)"],
     "A", "OSC", "medium",
     "• Potash alum is a double salt with 24 molecules of water of crystallization: \\(\\text{K}_2\\text{SO}_4 \\cdot \\text{Al}_2(\\text{SO}_4)_3 \\cdot 24\\text{H}_2\\text{O}\\).\nCorrect Choice is (A)."),

    ("""Why is Potash Alum added to turbid, muddy river water in water purification plants and domestic tanks?""",
     ["It gives water a sweet taste",
      "Trivalent aluminium ions (\\(\\text{Al}^{3+}\\)) neutralize the negative electrostatic charges on suspended clay particles, causing rapid coagulation and settling (sedimentation)",
      "It boils the water cold",
      "It filters water through invisible pores"],
     "B", "OSC", "medium",
     "• Alum acts as a coagulant: \\(\\text{Al}^{3+}\\) ions neutralize colloidal clay charges, causing flocculation and sedimentation.\nCorrect Choice is (B)."),

    ("""What is 'DELIQUESCENCE'?""",
     ["The property of a substance to dissolve upon boiling",
      "The property of certain dry water-soluble substances (like anhydrous \\(\\text{CaCl}_2\\), \\(\\text{NaOH}\\) pellets) to absorb moisture from the atmosphere and dissolve in it to form a liquid solution",
      "Loss of water on heating",
      "A change from solid directly to gas"],
     "B", "OSC", "medium",
     "• Deliquescent substances absorb so much atmospheric water vapor that they dissolve in their own absorbed water.\nCorrect Choice is (B)."),

    # 21-30: Applied properties and salt behavior
    ("""Which of the following salts is commonly used as a desiccant (drying agent) to absorb moisture from damp air?""",
     ["Anhydrous Calcium Chloride (\\(\\text{CaCl}_2\\)) or Silica Gel",
      "Sodium chloride (\\(\\text{NaCl}\\))",
      "Copper sulphate pentahydrate",
      "Sodium carbonate decahydrate"],
     "A", "OSC", "easy",
     "• Anhydrous \\(\\text{CaCl}_2\\) and silica gel are hygroscopic desiccants that avidly capture water vapor.\nCorrect Choice is (A)."),

    ("""What is the formula of Epsom salt?""",
     ["\\(\\text{MgSO}_4 \\cdot 7\\text{H}_2\\text{O}\\) (Magnesium sulphate heptahydrate)",
      "\\(\\text{Na}_2\\text{SO}_4 \\cdot 10\\text{H}_2\\text{O}\\)",
      "\\(\\text{ZnSO}_4 \\cdot 7\\text{H}_2\\text{O}\\)",
      "\\(\\text{CaSO}_4 \\cdot 2\\text{H}_2\\text{O}\\)"],
     "A", "OSC", "medium",
     "• Epsom salt is \\(\\text{MgSO}_4 \\cdot 7\\text{H}_2\\text{O}\\).\nCorrect Choice is (A)."),

    ("""What is the formula of White Vitriol?""",
     ["\\(\\text{ZnSO}_4 \\cdot 7\\text{H}_2\\text{O}\\) (Zinc sulphate heptahydrate)",
      "\\(\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}\\)",
      "\\(\\text{FeSO}_4 \\cdot 7\\text{H}_2\\text{O}\\)",
      "\\(\\text{MgSO}_4 \\cdot 7\\text{H}_2\\text{O}\\)"],
     "A", "OSC", "medium",
     "• White vitriol is zinc sulphate heptahydrate: \\(\\text{ZnSO}_4 \\cdot 7\\text{H}_2\\text{O}\\).\nCorrect Choice is (A)."),

    ("""Assertion (A): An aqueous solution of copper sulphate (\\(\\text{CuSO}_4\\)) turns blue litmus paper red.\nReason (R): Copper sulphate is a salt of a strong acid (\\(\\text{H}_2\\text{SO}_4\\)) and a weak base (\\(\\text{Cu(OH)}_2\\)), which hydrolyzes to create an acidic solution.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "• Cationic hydrolysis of \\(\\text{Cu}^{2+}\\) releases excess \\(\\text{H}^+\\) ions into solution, giving it an acidic character.\nCorrect Choice is (A)."),

    ("""Assertion (A): Common salt (pure \\(\\text{NaCl}\\)) absorbs water vapor and turns wet and sticky during rainy monsoons.\nReason (R): Pure sodium chloride is inherently a deliquescent compound.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "Both (A) and (R) are false"],
     "C", "OAR", "hard",
     "• (A) is true for commercial table salt, but (R) is false: pure \\(\\text{NaCl}\\) is NOT deliquescent. Table salt becomes wet during monsoon due to impurities of magnesium chloride (\\(\\text{MgCl}_2\\)) and calcium chloride (\\(\\text{CaCl}_2\\)), which are strongly deliquescent.\nCorrect Choice is (C)."),

    ("""State True or False: Plaster of Paris slightly expands upon setting, which allows it to reproduce sharp, detailed impressions in decorative casting and orthopedic plaster casts.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. The slight volumetric expansion on hydration ensures that POP fills mould contours with great fidelity.\nCorrect Choice is (A)."),

    ("""State True or False: Anhydrous salts have identical chemical formulas and colors as their hydrated crystalline counterparts.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. Hydrated salts contain water of crystallization which coordinates to metal cations, altering optical color and crystal lattice.\nCorrect Choice is (B)."),

    ("""What is the percentage of water of crystallization in Copper(II) Sulphate pentahydrate (\\(\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}\\))? (Given: \\(\\text{Cu}=63.5\\), \\(\\text{S}=32\\), \\(\\text{O}=16\\), \\(\\text{H}=1\\))""",
     ["\\(18.0\\%\\)", "\\(36.08\\%\\)", "\\(50.0\\%\\)", "\\(64.0\\%\\)"],
     "B", "OSC", "hard",
     "• Formula mass = \\(63.5 + 32 + (4 \\times 16) + (5 \\times 18) = 159.5 + 90 = 249.5\\text{ g/mol}\\).\nPercentage of water = \\(\\frac{90}{249.5} \\times 100 \\approx 36.07\\%\\).\nCorrect Choice is (B)."),

    ("""What is the salt produced by the reaction between Carbonic acid (weak) and Potassium hydroxide (strong)?""",
     ["Potassium carbonate (\\(\\text{K}_2\\text{CO}_3\\)), which forms a basic solution in water",
      "Potassium chloride, which is neutral",
      "Potassium sulphate, which is acidic",
      "Potassium nitrate"],
     "A", "OSC", "easy",
     "• \\(2\\text{KOH} + \\text{H}_2\\text{CO}_3 \\to \\text{K}_2\\text{CO}_3 + 2\\text{H}_2\\text{O}\\); salt of weak acid + strong base is basic in water.\nCorrect Choice is (A)."),

    ("""What is the name and formula of Glauber's salt?""",
     ["Sodium sulphate decahydrate (\\(\\text{Na}_2\\text{SO}_4 \\cdot 10\\text{H}_2\\text{O}\\))",
      "Magnesium sulphate heptahydrate",
      "Calcium sulphate dihydrate",
      "Zinc sulphate heptahydrate"],
     "A", "OSC", "medium",
     "• Glauber's salt is \\(\\text{Na}_2\\text{SO}_4 \\cdot 10\\text{H}_2\\text{O}\\).\nCorrect Choice is (A)."),

    # 31-40: Additional Exam questions to complete 40
    ("""What is the pH of an aqueous solution of baking soda (Sodium bicarbonate, \\(\\text{NaHCO}_3\\))?""",
     ["\\(2.0\\)", "\\(5.0\\)", "\\(7.0\\)", "\\(8.5\\) (Mildly basic)"],
     "D", "OSC", "easy",
     "• Hydrolysis of bicarbonate ion gives a mildly alkaline solution with pH around 8.5.\nCorrect Choice is (D)."),

    ("""What type of salt is Ammonium Acetate (\\(\\text{CH}_3\\text{COONH}_4\\)) formed from weak acid (\\(\\text{CH}_3\\text{COOH}\\)) and weak base (\\(\\text{NH}_4\\text{OH}\\))?""",
     ["Strongly acidic",
      "Nearly neutral (pH ≈ 7.0) because dissociation constants \\(K_a\\) and \\(K_b\\) are almost equal",
      "Strongly alkaline (pH 14)",
      "Insoluble in water"],
     "B", "OSC", "medium",
     "• Because acetic acid and ammonium hydroxide have virtually identical dissociation constants (\\(K_a \\approx K_b\\)), ammonium acetate solution is nearly neutral (pH ~7.0).\nCorrect Choice is (B)."),

    ("""Which of the following is an ACID SALT containing replaceable hydrogen?""",
     ["Sodium chloride (\\(\\text{NaCl}\\))",
      "Sodium bisulphate (\\(\\text{NaHSO}_4\\))",
      "Sodium sulphate (\\(\\text{Na}_2\\text{SO}_4\\))",
      "Potassium chloride (\\(\\text{KCl}\\))"],
     "B", "OSC", "easy",
     "• Acid salts (like \\(\\text{NaHSO}_4, \\text{NaHCO}_3\\)) retain replaceable hydrogen from partial neutralization of polybasic acids.\nCorrect Choice is (B)."),

    ("""Which anhydrous salt is used in test strips to detect traces of moisture by changing color from deep blue to bright pink?""",
     ["Cobalt(II) chloride (\\(\\text{CoCl}_2\\))",
      "Sodium chloride",
      "Potassium iodide",
      "Calcium carbonate"],
     "A", "OSC", "medium",
     "• Anhydrous \\(\\text{CoCl}_2\\) is deep blue; absorbing moisture coordinates water molecules forming pink \\(\\text{CoCl}_2 \\cdot 6\\text{H}_2\\text{O}\\).\nCorrect Choice is (A)."),

    ("""How many total water molecules are present in one formula unit of Potash Alum?""",
     ["10", "12", "18", "24"],
     "D", "OSC", "easy",
     "• Potash alum contains 24 molecules of water of crystallization: \\(\\text{K}_2\\text{SO}_4 \\cdot \\text{Al}_2(\\text{SO}_4)_3 \\cdot 24\\text{H}_2\\text{O}\\).\nCorrect Choice is (D)."),

    ("""Why must Plaster of Paris (POP) be stored strictly in airtight, moisture-proof containers?""",
     ["It evaporates into air",
      "It absorbs atmospheric moisture slowly, hydrating prematurely into hard Gypsum and losing its setting property",
      "It reacts with nitrogen to form toxic gas",
      "It dissolves into thin air"],
     "B", "OSC", "easy",
     "• Moisture slowly converts POP into set gypsum, ruining its setting ability.\nCorrect Choice is (B)."),

    ("""Fill in the blank: Salts of a strong acid and a weak base undergo ________ hydrolysis to yield an acidic solution.""",
     ["Anionic", "Cationic", "Neutral", "Non-polar"],
     "B", "OFB", "medium",
     "• In salts like \\(\\text{NH}_4\\text{Cl}\\), the cation (\\(\\text{NH}_4^+\\)) hydrolyzes to release \\(\\text{H}^+\\) (cationic hydrolysis).\nCorrect Choice is (B)."),

    ("""Fill in the blank: Salts of a weak acid and a strong base undergo ________ hydrolysis to yield a basic solution.""",
     ["Cationic", "Anionic", "Oxidative", "Thermal"],
     "B", "OFB", "medium",
     "• In salts like \\(\\text{CH}_3\\text{COONa}\\), the anion (\\(\\text{CH}_3\\text{COO}^-\\)) hydrolyzes to release \\(\\text{OH}^-\\) (anionic hydrolysis).\nCorrect Choice is (B)."),

    ("""What is the approximate percentage by mass of water of crystallization in Washing Soda (\\(\\text{Na}_2\\text{CO}_3 \\cdot 10\\text{H}_2\\text{O}\\))? (Molar mass = 286 g/mol, 10 H2O = 180 g)""",
     ["\\(18.0\\%\\)", "\\(35.5\\%\\)", "\\(62.9\\%\\)", "\\(80.0\\%\\)"],
     "C", "OSC", "medium",
     "• Percentage = \\(\\frac{180}{286} \\times 100 \\approx 62.93\\%\\).\nCorrect Choice is (C)."),

    ("""What happens when green vitriol crystals (\\(\\text{FeSO}_4 \\cdot 7\\text{H}_2\\text{O}\\)) are heated strongly beyond dehydration?""",
     ["They turn into liquid iron",
      "Anhydrous \\(\\text{FeSO}_4\\) decomposes into reddish-brown solid \\(\\text{Fe}_2\\text{O}_3\\) and suffocating gases of \\(\\text{SO}_2\\) and \\(\\text{SO}_3\\)",
      "They turn into copper sulphate",
      "They evaporate completely with no residue"],
     "B", "OSC", "hard",
     "• Strong heating decomposes anhydrous ferrous sulphate: \\(2\\text{FeSO}_4 \\xrightarrow{\\Delta} \\text{Fe}_2\\text{O}_3\\text{ (brown ferric oxide)} + \\text{SO}_2\\uparrow + \\text{SO}_3\\uparrow\\).\nCorrect Choice is (B).")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("""What is the pH of an aqueous solution of sodium chloride (\\(\\text{NaCl}\\))?""",
     ["\\(3\\)", "\\(7\\) (Neutral)", "\\(11\\)", "\\(14\\)"],
     "B", "OSC", "easy",
     "• \\(\\text{NaCl}\\) is neutral (pH 7).\nCorrect Choice is (B)."),

    ("""What is the pH of a solution of ammonium chloride (\\(\\text{NH}_4\\text{Cl}\\))?""",
     ["Less than 7 (Acidic)", "7 (Neutral)", "Greater than 7 (Basic)", "14"],
     "A", "OSC", "easy",
     "• Salt of strong acid and weak base is acidic (pH < 7).\nCorrect Choice is (A)."),

    ("""What is the pH of a solution of sodium acetate (\\(\\text{CH}_3\\text{COONa}\\))?""",
     ["Less than 7", "7 (Neutral)", "Greater than 7 (Basic)", "0"],
     "C", "OSC", "easy",
     "• Salt of weak acid and strong base is basic (pH > 7).\nCorrect Choice is (C)."),

    ("""What is the color of hydrated copper sulphate crystals?""",
     ["White", "Blue", "Green", "Yellow"],
     "B", "OSC", "easy",
     "• Blue vitriol is blue.\nCorrect Choice is (B)."),

    ("""What is the color of anhydrous copper sulphate powder?""",
     ["White", "Blue", "Pink", "Black"],
     "A", "OSC", "easy",
     "• Anhydrous \\(\\text{CuSO}_4\\) is white.\nCorrect Choice is (A)."),

    ("""How many water molecules are in Blue Vitriol?""",
     ["\\(2\\)", "\\(5\\)", "\\(7\\)", "\\(10\\)"],
     "B", "OSC", "easy",
     "• 5 molecules of water.\nCorrect Choice is (B)."),

    ("""How many water molecules are in Green Vitriol?""",
     ["\\(2\\)", "\\(5\\)", "\\(7\\)", "\\(10\\)"],
     "C", "OSC", "easy",
     "• 7 molecules of water (\\(\\text{FeSO}_4 \\cdot 7\\text{H}_2\\text{O}\\)).\nCorrect Choice is (C)."),

    ("""How many water molecules are in Washing Soda?""",
     ["\\(2\\)", "\\(5\\)", "\\(7\\)", "\\(10\\)"],
     "D", "OSC", "easy",
     "• 10 molecules of water (\\(\\text{Na}_2\\text{CO}_3 \\cdot 10\\text{H}_2\\text{O}\\)).\nCorrect Choice is (D)."),

    ("""How many water molecules are in Gypsum?""",
     ["\\(0.5\\)", "\\(1\\)", "\\(2\\)", "\\(5\\)"],
     "C", "OSC", "easy",
     "• 2 molecules of water (\\(\\text{CaSO}_4 \\cdot 2\\text{H}_2\\text{O}\\)).\nCorrect Choice is (C)."),

    ("""How many water molecules are in Plaster of Paris per formula unit of \\(\\text{CaSO}_4\\)?""",
     ["\\(0.5\\ (1/2)\\)", "\\(1\\)", "\\(2\\)", "\\(5\\)"],
     "A", "OSC", "easy",
     "• 1/2 molecule of water (\\(\\text{CaSO}_4 \\cdot \\frac{1}{2}\\text{H}_2\\text{O}\\)).\nCorrect Choice is (A)."),

    ("""What temperature is required to convert gypsum into Plaster of Paris?""",
     ["\\(50^\\circ\\text{C}\\)", "\\(100^\\circ\\text{C}\\ (373\\text{ K})\\)", "\\(250^\\circ\\text{C}\\)", "\\(1000^\\circ\\text{C}\\)"],
     "B", "OSC", "easy",
     "• Controlled heating at \\(100^\\circ\\text{C}\\).\nCorrect Choice is (B)."),

    ("""What is formed when Plaster of Paris reacts with water?""",
     ["Gypsum (hard mass)", "Slaked lime", "Limestone", "Quicklime"],
     "A", "OSC", "easy",
     "• POP hydrates back into hard Gypsum.\nCorrect Choice is (A)."),

    ("""What medical application uses Plaster of Paris?""",
     ["Setting fractured bones in orthopedic casts", "Eye drops", "Treating stomach ulcers", "Disinfecting cuts"],
     "A", "OSC", "easy",
     "• POP casts immobilize fractured bones.\nCorrect Choice is (A)."),

    ("""What is the loss of water of crystallization to dry air called?""",
     ["Efflorescence", "Deliquescence", "Condensation", "Distillation"],
     "A", "OSC", "easy",
     "• Efflorescence.\nCorrect Choice is (A)."),

    ("""What is the absorption of moisture from air to form a liquid solution called?""",
     ["Efflorescence", "Deliquescence", "Evaporation", "Oxidation"],
     "B", "OSC", "easy",
     "• Deliquescence.\nCorrect Choice is (B)."),

    ("""Which compound is used in blood coagulation after shaving cuts (Fitkari)?""",
     ["Potash Alum", "Baking soda", "Washing soda", "Plaster of Paris"],
     "A", "OSC", "easy",
     "• Alum acts as a styptic agent to coagulate blood.\nCorrect Choice is (A)."),

    ("""What is the color of Ferrous Sulphate crystals (green vitriol)?""",
     ["Pale green", "Bright red", "Dark purple", "Colorless"],
     "A", "OSC", "easy",
     "• \\(\\text{FeSO}_4 \\cdot 7\\text{H}_2\\text{O}\\) crystals are pale green.\nCorrect Choice is (A)."),

    ("""What is the color of anhydrous Ferrous Sulphate after gentle heating?""",
     ["White / Dirty white", "Deep blue", "Bright yellow", "Magenta"],
     "A", "OSC", "easy",
     "• Anhydrous \\(\\text{FeSO}_4\\) is dirty white.\nCorrect Choice is (A)."),

    ("""State True or False: Water of crystallization gives crystalline shape and color to hydrated salts.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. It is integral to the crystal geometry.\nCorrect Choice is (A)."),

    ("""State True or False: Plaster of Paris contracts upon setting.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. POP slightly expands upon setting.\nCorrect Choice is (B)."),

    ("""What is the common name for \\(\\text{Na}_2\\text{CO}_3 \\cdot 10\\text{H}_2\\text{O}\\)?""",
     ["Baking soda", "Washing soda", "Caustic soda", "Bleaching powder"],
     "B", "OSC", "easy",
     "• Washing soda.\nCorrect Choice is (B)."),

    ("""What is the common name for \\(\\text{NaHCO}_3\\)?""",
     ["Washing soda", "Baking soda", "Caustic soda", "Soda ash"],
     "B", "OSC", "easy",
     "• Baking soda.\nCorrect Choice is (B)."),

    ("""What is the common name for \\(\\text{NaOH}\\)?""",
     ["Baking soda", "Caustic soda", "Washing soda", "Lime"],
     "B", "OSC", "easy",
     "• Caustic soda.\nCorrect Choice is (B)."),

    ("""Which salt is used in making statues, moulds, and false ceilings?""",
     ["Plaster of Paris (POP)", "Potash alum", "Common salt", "Blue vitriol"],
     "A", "OSC", "easy",
     "• Plaster of Paris is widely used for casts, moulds, and architecture.\nCorrect Choice is (A)."),

    ("""Fill in the blank: The formula of Blue Vitriol is \\(\\text{CuSO}_4 \\cdot\\) ________ \\(\\text{H}_2\\text{O}\\).""",
     ["\\(2\\)", "\\(5\\)", "\\(7\\)", "\\(10\\)"],
     "B", "OFB", "easy",
     "• 5 water molecules.\nCorrect Choice is (B)."),

    ("""Fill in the blank: Heating Gypsum at \\(373\\text{ K}\\) produces ________.""",
     ["Quicklime", "Plaster of Paris", "Slaked lime", "Calcium carbide"],
     "B", "OFB", "easy",
     "• Plaster of Paris.\nCorrect Choice is (B)."),

    ("""What is the formula of anhydrous sodium carbonate (Soda Ash)?""",
     ["\\(\\text{Na}_2\\text{CO}_3\\)", "\\(\\text{Na}_2\\text{CO}_3 \\cdot 10\\text{H}_2\\text{O}\\)", "\\(\\text{NaHCO}_3\\)", "\\(\\text{NaOH}\\)"],
     "A", "OSC", "easy",
     "• Anhydrous \\(\\text{Na}_2\\text{CO}_3\\) is soda ash.\nCorrect Choice is (A)."),

    ("""What happens to table salt containing magnesium chloride impurity when left in open humid air?""",
     ["It evaporates", "It becomes damp and wet due to deliquescence", "It turns green", "It catches fire"],
     "B", "OSC", "easy",
     "• Deliquescent \\(\\text{MgCl}_2\\) attracts atmospheric moisture.\nCorrect Choice is (B)."),

    ("""What type of salt is Potassium Nitrate (\\(\\text{KNO}_3\\)) in terms of aqueous pH?""",
     ["Acidic", "Neutral (pH 7)", "Basic", "Strongly alkaline"],
     "B", "OSC", "easy",
     "• Salt of strong acid (\\(\\text{HNO}_3\\)) and strong base (\\(\\text{KOH}\\)) is neutral.\nCorrect Choice is (B)."),

    ("""What type of salt is Sodium Sulphide (\\(\\text{Na}_2\\text{S}\\)) in water?""",
     ["Acidic", "Basic (pH > 7)", "Neutral", "Insoluble"],
     "B", "OSC", "easy",
     "• Salt of weak acid (\\(\\text{H}_2\\text{S}\\)) and strong base (\\(\\text{NaOH}\\)) is basic.\nCorrect Choice is (B).")
]

# 12 Foundation Mock Questions (501-512) with rich embedded vector SVGs
foundation_data = [
    # 501: Blue Vitriol Heating Crystal Tube Apparatus
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="70" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Thermal Dehydration of Blue Vitriol</text>
  <!-- Boiling tube tilted -->
  <path d="M 60 140 L 220 70 L 230 90 L 70 160 Z" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
  <!-- Blue crystals at bottom turning white -->
  <polygon points="62,142 90,130 95,145 70,158" fill="#38bdf8"/>
  <text x="35" y="180" fill="#38bdf8" font-size="9" font-weight="bold">CuSO₄·5H₂O</text>
  <text x="35" y="195" fill="#f8fafc" font-size="8">Turns white anhydrous</text>
  <!-- Burner Flame -->
  <polygon points="75,170 70,200 85,200" fill="#ef4444"/>
  <polygon points="75,175 72,195 80,195" fill="#fde047"/>
  <!-- Water droplets condensed on cooler upper walls -->
  <circle cx="170" cy="85" r="2.5" fill="#60a5fa"/>
  <circle cx="185" cy="80" r="3" fill="#60a5fa"/>
  <circle cx="195" cy="75" r="2.5" fill="#60a5fa"/>
  <text x="160" y="60" fill="#60a5fa" font-size="9">Water Droplets</text>
  <text x="45" y="218" fill="#34d399" font-size="10">CuSO₄·5H₂O (Blue) ⟶ CuSO₄ (White) + 5 H₂O↑</text>
</svg>
</div>
In the heating experiment shown above, what two distinct observations confirm the presence of water of crystallization in blue vitriol crystals?""",
     ["The test tube melts and emits green sparks",
      "The blue crystals lose their color, turning into a white powder, while liquid water droplets condense on the cooler upper walls of the tube",
      "Black charcoal forms and a pop sound is heard",
      "The crystals turn into steam without leaving any residue"],
     "B", "OSC", "easy",
     "• Loss of the 5 coordinated water molecules turns blue crystalline \\(\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}\\) into white anhydrous \\(\\text{CuSO}_4\\), with liberated steam condensing on cooler glass.\nCorrect Choice is (B)."),

    # 502: Re-Hydration of Anhydrous Copper Sulphate
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Reversible Re-Hydration of CuSO₄</text>
  <!-- Watch glass with powder -->
  <ellipse cx="110" cy="120" rx="50" ry="16" fill="#334155" stroke="#94a3b8"/>
  <ellipse cx="110" cy="118" rx="35" ry="10" fill="#f8fafc"/>
  <text x="80" y="100" fill="#f8fafc" font-size="9">White Anhydrous CuSO₄</text>
  <!-- Dropper adding water -->
  <rect x="200" y="50" width="10" height="40" fill="#94a3b8"/>
  <polygon points="200,90 205,105 210,90" fill="#38bdf8"/>
  <circle cx="205" cy="115" r="4" fill="#38bdf8"/>
  <text x="215" y="80" fill="#38bdf8" font-size="10">Add H₂O</text>
  <!-- Blue patch spreading -->
  <ellipse cx="120" cy="118" rx="20" ry="8" fill="#38bdf8"/>
  <text x="100" y="150" fill="#38bdf8" font-size="10" font-weight="bold">Turns Blue Instantly!</text>
  <text x="40" y="185" fill="#34d399" font-size="10">CuSO₄ + 5 H₂O ⟶ CuSO₄·5H₂O (Exothermic color restoration)</text>
</svg>
</div>
Why does adding a few drops of water to white anhydrous copper sulphate immediately restore its vibrant blue color?""",
     ["Because water has a natural blue dye",
      "Because water molecules re-enter the crystal coordination sphere around \\(\\text{Cu}^{2+}\\) ions, reconstituting the blue \\([\\text{Cu(H}_2\\text{O})_4]^{2+}\\) chromophore complex",
      "Because copper oxidizes into blue copper hydroxide",
      "Because water causes optical interference"],
     "B", "OSC", "hard",
     "• In anhydrous \\(\\text{CuSO}_4\\), the crystal field splitting is small. Re-hydration coordinates four water molecules directly to \\(\\text{Cu}^{2+}\\), splitting d-orbitals to absorb red light and reflect brilliant blue.\nCorrect Choice is (B)."),

    # 503: Gypsum to Plaster of Paris Dehydration Equation
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Gypsum ⇌ Plaster of Paris Equilibrium</text>
  <!-- Gypsum -->
  <rect x="25" y="55" width="130" height="75" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="35" y="78" fill="#38bdf8" font-size="11" font-weight="bold">Gypsum</text>
  <text x="35" y="98" fill="#cbd5e1" font-size="10">CaSO₄·2H₂O</text>
  <text x="35" y="118" fill="#94a3b8" font-size="9">Hard rock mineral</text>
  <!-- Forward Arrow with 373 K -->
  <text x="160" y="85" fill="#fde047" font-size="11">Δ 373K →</text>
  <text x="160" y="110" fill="#34d399" font-size="11">← +H₂O</text>
  <!-- Plaster of Paris -->
  <rect x="215" y="55" width="105" height="75" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="220" y="78" fill="#34d399" font-size="10" font-weight="bold">Plaster of Paris</text>
  <text x="220" y="98" fill="#cbd5e1" font-size="10">CaSO₄·½H₂O</text>
  <text x="220" y="118" fill="#94a3b8" font-size="8">Sets in 10-15 mins</text>
  <text x="40" y="170" fill="#ef4444" font-size="10">Overheating (&gt; 393 K) ⟶ Dead Burnt Plaster (CaSO₄)</text>
  <text x="40" y="195" fill="#cbd5e1" font-size="9">Dead burnt plaster loses water completely and cannot set</text>
</svg>
</div>
In the Gypsum-POP reaction scheme above, how is half a molecule of water (\\(\\frac{1}{2}\\text{H}_2\\text{O}\\)) physically possible in the chemical formula \\(\\text{CaSO}_4 \\cdot \\frac{1}{2}\\text{H}_2\\text{O}\\)?""",
     ["Individual water molecules are cut in half by heat",
      "Two formula units of \\(\\text{CaSO}_4\\) share a single molecule of water between them in the crystal lattice: \\((2\\text{CaSO}_4) \\cdot \\text{H}_2\\text{O}\\)",
      "It represents hydrogen gas trapped in stone",
      "Half molecule is a typographical error"],
     "B", "OSC", "medium",
     "• Fractional coefficients indicate crystal sharing: one water molecule is coordinated between two \\(\\text{CaSO}_4\\) units (\\(2\\text{CaSO}_4 \\cdot \\text{H}_2\\text{O}\\)).\nCorrect Choice is (B)."),

    # 504: Salt Hydrolysis pH Matrix (4 Salt Classes)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Salt Hydrolysis &amp; Solution pH</text>
  <!-- Class 1: SA + SB -->
  <rect x="25" y="45" width="140" height="55" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="32" y="62" fill="#34d399" font-size="9" font-weight="bold">1. Strong Acid + Strong Base</text>
  <text x="32" y="78" fill="#cbd5e1" font-size="8">NaCl, KNO₃, Na₂SO₄</text>
  <text x="32" y="92" fill="#34d399" font-size="9" font-weight="bold">pH = 7.0 (NEUTRAL)</text>
  <!-- Class 2: SA + WB -->
  <rect x="175" y="45" width="140" height="55" fill="#1e293b" stroke="#ef4444" rx="3"/>
  <text x="182" y="62" fill="#f87171" font-size="9" font-weight="bold">2. Strong Acid + Weak Base</text>
  <text x="182" y="78" fill="#cbd5e1" font-size="8">NH₄Cl, CuSO₄, FeCl₃</text>
  <text x="182" y="92" fill="#f87171" font-size="9" font-weight="bold">pH &lt; 7 (ACIDIC)</text>
  <!-- Class 3: WA + SB -->
  <rect x="25" y="110" width="140" height="55" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="32" y="127" fill="#38bdf8" font-size="9" font-weight="bold">3. Weak Acid + Strong Base</text>
  <text x="32" y="143" fill="#cbd5e1" font-size="8">CH₃COONa, Na₂CO₃</text>
  <text x="32" y="157" fill="#38bdf8" font-size="9" font-weight="bold">pH &gt; 7 (BASIC)</text>
  <!-- Class 4: WA + WB -->
  <rect x="175" y="110" width="140" height="55" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="182" y="127" fill="#fde047" font-size="9" font-weight="bold">4. Weak Acid + Weak Base</text>
  <text x="182" y="143" fill="#cbd5e1" font-size="8">CH₃COONH₄</text>
  <text x="182" y="157" fill="#fde047" font-size="9" font-weight="bold">pH ≈ 7 (Depends on Ka/Kb)</text>
  <text x="45" y="195" fill="#cbd5e1" font-size="9">Hydrolysis of cation yields H⁺; hydrolysis of anion yields OH⁻</text>
</svg>
</div>
According to the salt hydrolysis classification above, what is the nature of an aqueous solution of Ferric Chloride (\\(\\text{FeCl}_3\\)) and why?""",
     ["Neutral; both ions are equal",
      "Acidic (\\(\\text{pH} < 7\\)); it is formed from strong acid \\(\\text{HCl}\\) and weak base \\(\\text{Fe(OH)}_3\\), and the \\(\\text{Fe}^{3+}\\) cation hydrolyzes in water to release excess \\(\\text{H}^+\\) ions",
      "Basic (\\(\\text{pH} > 7\\)); chloride ions produce hydroxide",
      "Non-conductive"],
     "B", "OSC", "medium",
     "• \\(\\text{Fe}^{3+} + 3\\text{H}_2\\text{O} \\rightleftharpoons \\text{Fe(OH)}_3 + 3\\text{H}^+\\). Excess hydrogen ions impart an acidic pH to \\(\\text{FeCl}_3\\) solution.\nCorrect Choice is (B)."),

    # 505: Coagulation Mechanism of Alum in Water Purification
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Coagulation by Potash Alum (Fitkari)</text>
  <!-- Dispersed Muddy Particles -->
  <circle cx="60" cy="80" r="12" fill="#78350f"/>
  <text x="56" y="84" fill="#fff" font-size="9">-</text>
  <circle cx="100" cy="110" r="10" fill="#78350f"/>
  <text x="97" y="114" fill="#fff" font-size="9">-</text>
  <text x="35" y="145" fill="#fca5a5" font-size="9">Negatively charged clay</text>
  <text x="35" y="160" fill="#fca5a5" font-size="9">repels and stays suspended</text>
  <!-- Al3+ Addition -->
  <text x="145" y="105" fill="#fde047" font-size="12" font-weight="bold">+ Al³⁺ →</text>
  <!-- Settled Coagulated Floc -->
  <ellipse cx="240" cy="120" rx="35" ry="20" fill="#451a03" stroke="#a16207" stroke-width="2"/>
  <text x="215" y="123" fill="#fff" font-size="10" font-weight="bold">Heavy Floc</text>
  <text x="205" y="160" fill="#34d399" font-size="9" font-weight="bold">Settles to bottom</text>
  <text x="45" y="195" fill="#38bdf8" font-size="10">Al³⁺ neutralizes clay charges (Hardy-Schulze Rule)</text>
</svg>
</div>
How does Potash Alum (\\(\\text{K}_2\\text{SO}_4 \\cdot \\text{Al}_2(\\text{SO}_4)_3 \\cdot 24\\text{H}_2\\text{O}\\)) clarify muddy turbid water so effectively?""",
     ["It freezes the mud particles into solid ice",
      "Its high-charge trivalent aluminium cations (\\(\\text{Al}^{3+}\\)) neutralize the mutual negative electrostatic repulsion of colloidal mud particles, causing them to aggregate into heavy clumps (flocs) that settle rapidly by gravity",
      "It dissolves the mud into gas",
      "It acts as a magnetic sponge"],
     "B", "OSC", "medium",
     "• Colloidal clay carries negative surface charge preventing settling. Highly charged \\(\\text{Al}^{3+}\\) ions neutralize this charge, inducing coagulation and sedimentation.\nCorrect Choice is (B)."),

    # 506: Efflorescence of Washing Soda
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Efflorescence of Washing Soda</text>
  <!-- Left: Fresh Crystals -->
  <rect x="30" y="55" width="125" height="85" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="40" y="75" fill="#38bdf8" font-size="10" font-weight="bold">Fresh Crystals:</text>
  <text x="40" y="95" fill="#cbd5e1" font-size="9">Na₂CO₃·10H₂O</text>
  <text x="40" y="112" fill="#93c5fd" font-size="9">Transparent crystal</text>
  <text x="40" y="128" fill="#fde047" font-size="8">10 water molecules</text>
  <!-- Arrow with Dry Air -->
  <text x="160" y="95" fill="#fde047" font-size="10">Dry Air →</text>
  <!-- Right: Effloresced Powder -->
  <rect x="185" y="55" width="125" height="85" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="195" y="75" fill="#34d399" font-size="10" font-weight="bold">Effloresced Form:</text>
  <text x="195" y="95" fill="#cbd5e1" font-size="9">Na₂CO₃·H₂O</text>
  <text x="195" y="112" fill="#86efac" font-size="9">White opaque powder</text>
  <text x="195" y="128" fill="#fca5a5" font-size="8">Lost 9 H₂O molecules!</text>
  <text x="40" y="175" fill="#cbd5e1" font-size="10">Vapor pressure of crystal &gt; Atmospheric water vapor pressure</text>
</svg>
</div>
Why do transparent washing soda crystals spontaneously crumble into a white, powdery monohydrate crust when exposed to dry atmospheric air?""",
     ["Bacteria eat 9 of the water molecules",
      "Because the vapor pressure of water of crystallization in the decahydrate crystal exceeds the partial pressure of water vapor in dry ambient air, causing 9 water molecules to evaporate spontaneously (efflorescence)",
      "Because oxygen replaces water in the crystal",
      "Because light breaks all chemical bonds"],
     "B", "OSC", "hard",
     "• When crystal water vapor pressure is higher than ambient humidity, spontaneous efflorescence occurs: \\(\\text{Na}_2\\text{CO}_3 \\cdot 10\\text{H}_2\\text{O} \\to \\text{Na}_2\\text{CO}_3 \\cdot \\text{H}_2\\text{O} + 9\\text{H}_2\\text{O}\\uparrow\\).\nCorrect Choice is (B)."),

    # 507: Deliquescence vs Hygroscopy
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Deliquescence vs Hygroscopy</text>
  <!-- Hygroscopic -->
  <rect x="25" y="55" width="135" height="90" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="35" y="75" fill="#fde047" font-size="11" font-weight="bold">Hygroscopic</text>
  <text x="35" y="95" fill="#cbd5e1" font-size="9">• Absorbs moisture</text>
  <text x="35" y="110" fill="#cbd5e1" font-size="9">• REMAINS SOLID</text>
  <text x="35" y="125" fill="#94a3b8" font-size="8">e.g. Silica gel, Con. H₂SO₄</text>
  <!-- Deliquescent -->
  <rect x="180" y="55" width="135" height="90" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="190" y="75" fill="#38bdf8" font-size="11" font-weight="bold">Deliquescent</text>
  <text x="190" y="95" fill="#cbd5e1" font-size="9">• Absorbs so much moisture</text>
  <text x="190" y="110" fill="#38bdf8" font-size="9">• DISSOLVES INTO LIQUID</text>
  <text x="190" y="125" fill="#94a3b8" font-size="8">e.g. NaOH pellets, CaCl₂</text>
  <text x="40" y="185" fill="#34d399" font-size="10">Deliquescence continues until atmospheric vapor pressure is matched</text>
</svg>
</div>
What distinguishes a DELIQUESCENT substance (like solid \\(\\text{NaOH}\\) or anhydrous \\(\\text{CaCl}_2\\)) from a simply HYGROSCOPIC substance (like silica gel)?""",
     ["Deliquescent substances explode in water",
      "Both absorb moisture, but a deliquescent substance absorbs so much atmospheric moisture that it completely dissolves into its own absorbed water to form a liquid puddle, whereas hygroscopic substances remain solid",
      "Hygroscopic substances only absorb oil",
      "There is no chemical difference"],
     "B", "OSC", "medium",
     "• Both take up water vapor, but deliquescent materials have vapor pressure lower than atmospheric humidity and liquefy completely in their own absorbed water.\nCorrect Choice is (B)."),

    # 508: Setting of POP Microcrystalline Interlocking
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">POP Setting Mechanism (Hydration)</text>
  <!-- Powder slurry -->
  <circle cx="80" cy="110" r="35" fill="#334155" stroke="#94a3b8"/>
  <text x="55" y="105" fill="#cbd5e1" font-size="9">POP Slurry</text>
  <text x="52" y="120" fill="#fde047" font-size="8">CaSO₄·½H₂O</text>
  <!-- Arrow -->
  <text x="125" y="115" fill="#38bdf8" font-size="16">⟶ +H₂O</text>
  <!-- Interlocking needle crystals of gypsum -->
  <rect x="200" y="75" width="80" height="70" fill="#1e293b" stroke="#10b981" rx="4"/>
  <line x1="210" y1="90" x2="260" y2="130" stroke="#34d399" stroke-width="2"/>
  <line x1="220" y1="130" x2="270" y2="90" stroke="#34d399" stroke-width="2"/>
  <line x1="240" y1="80" x2="240" y2="140" stroke="#34d399" stroke-width="2"/>
  <text x="210" y="160" fill="#86efac" font-size="8" font-weight="bold">Interlocked Gypsum</text>
  <text x="35" y="190" fill="#cbd5e1" font-size="10">Crystal growth causes slight volumetric expansion (~1%), ensuring sharp casting</text>
</svg>
</div>
Why does Plaster of Paris slightly EXPAND on setting instead of shrinking?""",
     ["Because bubbles of oxygen are trapped",
      "Because the formation of elongated, needle-shaped interlocking gypsum crystals creates microscopic intercrystalline void spaces that increase overall volume by about 1%",
      "Because water turns into steam during setting",
      "Because calcium atoms double in size"],
     "B", "OSC", "hard",
     "• Growing prismatic gypsum needles push against each other during crystallization, producing a slight volumetric expansion (\\(\\sim 0.5\\text{--}1\\%\\)) that fills moulds flawlessly.\nCorrect Choice is (B)."),

    # 509: Epsom Salt vs White Vitriol Formula Pair
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Isomorphous Heptahydrate Sulphates</text>
  <!-- Epsom Salt -->
  <rect x="25" y="55" width="135" height="85" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="35" y="80" fill="#38bdf8" font-size="11" font-weight="bold">Epsom Salt</text>
  <text x="35" y="100" fill="#cbd5e1" font-size="10">• MgSO₄·7H₂O</text>
  <text x="35" y="118" fill="#fde047" font-size="9">• 7 water molecules</text>
  <text x="35" y="132" fill="#94a3b8" font-size="8">Used in bath salts &amp; laxatives</text>
  <!-- White Vitriol -->
  <rect x="180" y="55" width="135" height="85" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="190" y="80" fill="#34d399" font-size="11" font-weight="bold">White Vitriol</text>
  <text x="190" y="100" fill="#cbd5e1" font-size="10">• ZnSO₄·7H₂O</text>
  <text x="190" y="118" fill="#fde047" font-size="9">• 7 water molecules</text>
  <text x="190" y="132" fill="#94a3b8" font-size="8">Used in eye drops &amp; dyeing</text>
  <text x="40" y="175" fill="#cbd5e1" font-size="10">Both have identical stoichiometry (7 H₂O) and identical crystal symmetry</text>
</svg>
</div>
Which cation pair forms isomorphous heptahydrate sulphate crystals containing exactly 7 molecules of water of crystallization?""",
     ["\\(\\text{Cu}^{2+}\\) and \\(\\text{Ca}^{2+}\\)",
      "\\(\\text{Mg}^{2+}\\) (Epsom salt) and \\(\\text{Zn}^{2+}\\) (White vitriol)",
      "\\(\\text{Na}^+\\) and \\(\\text{K}^+\\)",
      "\\(\\text{Al}^{3+}\\) and \\(\\text{Fe}^{3+}\\)"],
     "B", "OSC", "medium",
     "• Both \\(\\text{MgSO}_4 \\cdot 7\\text{H}_2\\text{O}\\) and \\(\\text{ZnSO}_4 \\cdot 7\\text{H}_2\\text{O}\\) crystallize as isomorphous orthorhombic heptahydrates.\nCorrect Choice is (B)."),

    # 510: Table Salt Dampness in Monsoons
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Table Salt Wetness in Monsoon Season</text>
  <!-- Table salt shaker -->
  <rect x="50" y="60" width="60" height="80" fill="#334155" stroke="#94a3b8" rx="4"/>
  <text x="55" y="100" fill="#fff" font-size="9">NaCl + Impurities</text>
  <!-- Analysis Box -->
  <rect x="135" y="55" width="180" height="95" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="145" y="75" fill="#fde047" font-size="10" font-weight="bold">Chemical Reality:</text>
  <text x="145" y="92" fill="#38bdf8" font-size="9">• Pure NaCl is NOT deliquescent</text>
  <text x="145" y="110" fill="#cbd5e1" font-size="9">• Commercial salt has MgCl₂ &amp; CaCl₂</text>
  <text x="145" y="128" fill="#ef4444" font-size="9">• MgCl₂ &amp; CaCl₂ are highly DELIQUESCENT</text>
  <text x="145" y="142" fill="#ef4444" font-size="9">  and absorb atmospheric humidity</text>
  <text x="40" y="185" fill="#34d399" font-size="10">Purified analytical-grade NaCl stays completely dry even during rain!</text>
</svg>
</div>
Why does commercial table salt turn sticky and wet during the rainy season, whereas chemically pure sodium chloride does not?""",
     ["Pure sodium chloride is waterproof",
      "Commercial salt contains trace impurities of magnesium chloride (\\(\\text{MgCl}_2\\)) and calcium chloride (\\(\\text{CaCl}_2\\)), which are strongly deliquescent and absorb water from humid air",
      "Sodium reacts with air to form water",
      "Chlorine gas liquefies in rain"],
     "B", "OSC", "easy",
     "• Pure \\(\\text{NaCl}\\) is non-deliquescent; dampness in table salt is entirely caused by hygroscopic \\(\\text{MgCl}_2\\) and \\(\\text{CaCl}_2\\) impurities.\nCorrect Choice is (B)."),

    # 511: Alum Double Salt 24 H2O Stoichiometry
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="70" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Anatomy of Potash Alum (Double Salt)</text>
  <text x="35" y="60" fill="#cbd5e1" font-size="11">Formula: K₂SO₄ · Al₂(SO₄)₃ · 24 H₂O</text>
  <!-- 3 Components -->
  <rect x="25" y="75" width="85" height="60" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="30" y="95" fill="#38bdf8" font-size="10" font-weight="bold">Potassium Salt</text>
  <text x="30" y="115" fill="#cbd5e1" font-size="9">K₂SO₄</text>
  <rect x="120" y="75" width="95" height="60" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="125" y="95" fill="#34d399" font-size="10" font-weight="bold">Aluminium Salt</text>
  <text x="125" y="115" fill="#cbd5e1" font-size="9">Al₂(SO₄)₃</text>
  <rect x="225" y="75" width="90" height="60" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="230" y="95" fill="#fde047" font-size="10" font-weight="bold">Water of Cryst.</text>
  <text x="230" y="115" fill="#cbd5e1" font-size="10">24 H₂O</text>
  <text x="35" y="165" fill="#38bdf8" font-size="10">Double salt: Yields K⁺, Al³⁺, and SO₄²⁻ ions in aqueous solution</text>
</svg>
</div>
How many total ions are released when one formula unit of Potash Alum (\\(\\text{K}_2\\text{SO}_4 \\cdot \\text{Al}_2(\\text{SO}_4)_3 \\cdot 24\\text{H}_2\\text{O}\\)) completely dissolves in water?""",
     ["3 ions", "5 ions", "8 ions (\\(2\\text{K}^+ + 2\\text{Al}^{3+} + 4\\text{SO}_4^{2-}\\))", "24 ions"],
     "C", "OSC", "hard",
     "• In solution, it dissociates completely into \\(2\\text{ K}^+ + 2\\text{ Al}^{3+} + 4\\text{ SO}_4^{2-} = 8\\) individual ions.\nCorrect Choice is (C)."),

    # 512: Copper Sulphate Hydrate Crystal Lattice Structure
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">CuSO₄·5H₂O Octahedral Coordination</text>
  <!-- Central Cu2+ -->
  <circle cx="170" cy="115" r="22" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <text x="158" y="120" fill="#fff" font-size="12" font-weight="bold">Cu²⁺</text>
  <!-- 4 Coordinated H2O molecules (Square Planar) -->
  <circle cx="120" cy="115" r="14" fill="#1e293b" stroke="#38bdf8"/>
  <text x="110" y="118" fill="#38bdf8" font-size="8">H₂O</text>
  <circle cx="220" cy="115" r="14" fill="#1e293b" stroke="#38bdf8"/>
  <text x="210" y="118" fill="#38bdf8" font-size="8">H₂O</text>
  <circle cx="170" cy="65" r="14" fill="#1e293b" stroke="#38bdf8"/>
  <text x="160" y="68" fill="#38bdf8" font-size="8">H₂O</text>
  <circle cx="170" cy="165" r="14" fill="#1e293b" stroke="#38bdf8"/>
  <text x="160" y="168" fill="#38bdf8" font-size="8">H₂O</text>
  <!-- 5th H2O hydrogen bonded to Sulphate -->
  <rect x="250" y="150" width="75" height="40" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="255" y="168" fill="#fde047" font-size="8">5th H₂O H-bonded</text>
  <text x="255" y="180" fill="#cbd5e1" font-size="7">to SO₄²⁻ anion</text>
  <text x="40" y="200" fill="#34d399" font-size="9">4 water molecules coordinate to Cu²⁺; 1 is hydrogen-bonded to SO₄²⁻</text>
</svg>
</div>
In the molecular coordination geometry of blue vitriol (\\(\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}\\)) shown above, how are the 5 water molecules structurally distributed in the crystal?""",
     ["All 5 water molecules float freely as ice",
      "Four water molecules are directly coordinate-bonded to the central \\(\\text{Cu}^{2+}\\) cation in a square planar arrangement, while the fifth water molecule is hydrogen-bonded to the sulphate anion (\\(\\text{SO}_4^{2-}\\))",
      "All 5 water molecules are bonded to sulphur",
      "Five water molecules surround each oxygen atom"],
     "B", "OSC", "hard",
     "• Structural formula is \\([\\text{Cu(H}_2\\text{O})_4]\\text{SO}_4 \\cdot \\text{H}_2\\text{O}\\): four coordinate to copper, and the fifth forms hydrogen bonds bridging the sulphate anion.\nCorrect Choice is (B).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-5-5.4-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-5-5.4-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-5-5.4-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch5_topic4.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
