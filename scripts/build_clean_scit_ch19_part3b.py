# scripts/build_clean_scit_ch19_part3b.py
# Clean generator for MH-9-SCIT Chapter 19 Topic 19.3 (Subtopics 19.3.3 and 19.3.4)
# 2 subtopics x 80 = 160 Qs
# Strictly compliant with Rule 2T: 40 Exam, 20 Practice, 20 Foundation per subtopic.

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_scit import build_q, generate_subtopic

CH_NUM = 19
CH_NAME = "Class 7 Science Foundation Core"

def gen_19_3_3():
    tc = "MH-9-SCIT-19-19.3.3"
    tname = "Acids, bases and neutralisation in daily life"
    archs = [
        # Arch 0: Acids: Natural vs Mineral & Properties
        {
            'data': [
                ("chemical substances that have a sour taste, turn blue litmus paper red, and liberate hydrogen ions (\\(H^+\\)) in aqueous solution", "Acids", "Bases", "Neutral salts", "Hydrocarbons"),
                ("the organic acid naturally present in citrus fruits such as lemons, oranges, and limes", "Citric acid", "Lactic acid", "Acetic acid", "Formic acid"),
                ("the organic acid present in fermented vinegar used as a food preservative and culinary flavoring", "Acetic acid (Ethanoic acid, \\(CH_3COOH\\))", "Citric acid", "Oxalic acid", "Malic acid"),
                ("the organic acid present in sour milk and fresh curd produced by bacterial fermentation of lactose", "Lactic acid", "Tartaric acid", "Butyric acid", "Ascorbic acid"),
                ("the natural organic acid found in ripe apples", "Malic acid", "Citric acid", "Tartaric acid", "Formic acid"),
                ("the organic acid present in tamarind, unripened grapes, and baking powder", "Tartaric acid", "Acetic acid", "Oxalic acid", "Lactic acid"),
                ("the organic acid present in spinach and tomatoes, whose accumulation with calcium can form kidney stones", "Oxalic acid", "Formic acid", "Lactic acid", "Citric acid"),
                ("the stinging acid injected into human skin by an ant or honeybee sting causing sharp pain and burning itching", "Formic acid (Methanoic acid, \\(HCOOH\\))", "Acetic acid", "Lactic acid", "Sulphuric acid"),
                ("strong mineral acids synthesized from inorganic minerals in industrial chemical laboratories", "Sulphuric acid (\\(H_2SO_4\\)), Hydrochloric acid (\\(HCl\\)), and Nitric acid (\\(HNO_3\\))", "Citric acid, Acetic acid, and Lactic acid", "Tartaric acid and Formic acid", "Carbonic acid only"),
                ("the chemical substance referred to in industrial chemistry as the 'King of Chemicals' due to its ubiquitous manufacturing use", "Sulphuric acid (\\(H_2SO_4\\))", "Hydrochloric acid", "Sodium hydroxide", "Nitric acid")
            ],
            'tmpls': [
                "Which category of chemical compounds is defined as: {0}?",
                "Which natural organic acid corresponds to: {0}?",
                "Which culinary organic acid is identified as: {0}?",
                "Which dairy fermentation acid represents: {0}?",
                "Which fruit organic acid matches: {0}?",
                "Which botanical acid corresponds to: {0}?",
                "Which dietary organic acid is described by: {0}?",
                "Which insect chemical venom represents: {0}?",
                "Which inorganic industrial suite constitutes: {0}?",
                "Which supreme industrial chemical is celebrated as: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Acid Chemistry Context**\\nThe statement details {item[0]}.\\n**Step 2: Natural vs Mineral Acids**\\nOrganic acids are weak natural metabolites (citric, acetic, lactic, tartaric, formic); mineral acids (\\(HCl, H_2SO_4, HNO_3\\)) are strong synthesized electrolytes.\\n**Step 3: Verification**\\nThe correct chemical answer is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Bases & Alkalis: Definition & Everyday Examples
        {
            'data': [
                ("chemical substances that have a bitter taste, slippery or soapy feel to touch, and turn red litmus paper blue", "Bases", "Acids", "Neutral salts", "Halogens"),
                ("water-soluble bases that dissolve completely in aqueous medium to produce hydroxide ions (\\(OH^-\\))", "Alkalis (e.g., \\(NaOH, KOH, Ca(OH)_2\\))", "Insoluble oxides", "Acid salts", "Mineral acids"),
                ("the fundamental chemical relationship between bases and alkalis", "All alkalis are bases, but not all bases are alkalis (insoluble bases like \\(Cu(OH)_2\\) are not alkalis)", "All bases are alkalis", "Alkalis and bases are mutually exclusive", "Alkalis are acidic bases"),
                ("the strong alkali known as caustic soda used extensively in manufacturing soaps, detergents, paper, and textiles", "Sodium hydroxide (\\(NaOH\\))", "Calcium hydroxide", "Magnesium hydroxide", "Ammonium hydroxide"),
                ("the strong alkali known as caustic potash used in manufacturing soft liquid soaps, shaving creams, and alkaline batteries", "Potassium hydroxide (\\(KOH\\))", "Sodium hydroxide", "Calcium oxide", "Copper hydroxide"),
                ("the base known as slaked lime used in whitewashing walls, neutralizing acidic soils, and water treatment", "Calcium hydroxide (\\(Ca(OH)_2\\))", "Calcium oxide", "Calcium carbonate", "Sodium carbonate"),
                ("the base known as Milk of Magnesia used therapeutically as a gentle antacid to relieve stomach acidity and indigestion", "Magnesium hydroxide (\\(Mg(OH)_2\\))", "Magnesium oxide", "Sodium hydroxide", "Potassium hydroxide"),
                ("the household cleaning alkali present in commercial window cleaning liquids and glass cleaners", "Ammonium hydroxide (\\(NH_4OH\\))", "Hydrochloric acid", "Sodium chloride", "Calcium chloride"),
                ("the white powder known as baking soda used in baking and as a household antacid", "Sodium hydrogen carbonate (Sodium bicarbonate, \\(NaHCO_3\\))", "Sodium carbonate", "Sodium hydroxide", "Calcium hydroxide"),
                ("the chemical substance known as washing soda used for removing permanent hardness of water and domestic laundry cleaning", "Sodium carbonate decahydrate (\\(Na_2CO_3\\cdot 10H_2O\\))", "Sodium bicarbonate", "Sodium hydroxide", "Potassium carbonate")
            ],
            'tmpls': [
                "Which category of chemical compounds is defined as: {0}?",
                "Which aqueous chemical classification corresponds to: {0}?",
                "What foundational chemical principle describes: {0}?",
                "Which industrial alkali is identified as: {0}?",
                "Which industrial potash alkali corresponds to: {0}?",
                "Which calcium base is characterized by: {0}?",
                "Which pharmaceutical antacid base represents: {0}?",
                "Which household cleaning reagent is identified as: {0}?",
                "Which domestic leavening compound corresponds to: {0}?",
                "Which laundry cleaning decahydrate is defined by: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Base / Alkali Chemistry Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Hydroxide Ionization and Everyday Compounds**\\nBases yield \\(OH^-\\); soluble bases are alkalis. Common examples include caustic soda (\\(NaOH\\)), slaked lime (\\(Ca(OH)_2\\)), and milk of magnesia (\\(Mg(OH)_2\\)).\\n**Step 3: Verification**\\nThe matching chemical entity is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 2: Chemical Indicators: Litmus, Turmeric, China Rose & Synthetics
        {
            'data': [
                ("substances that exhibit distinctly different colors in acidic, basic, and neutral solutions, used to test the nature of substances", "Acid-base indicators", "Catalysts", "Emulsifiers", "Electrolytes"),
                ("the most commonly used natural acid-base indicator extracted from lichens, available as solution or paper strips", "Litmus (neutral color is mauve/purple)", "Turmeric", "Phenolphthalein", "Methyl orange"),
                ("the color change shown by red and blue litmus paper when exposed to an acidic solution", "Blue litmus turns red; red litmus remains red", "Red litmus turns blue; blue remains blue", "Both turn yellow", "Both turn completely colorless"),
                ("the color change shown by red and blue litmus paper when exposed to a basic (alkaline) solution", "Red litmus turns blue; blue litmus remains blue", "Blue litmus turns red", "Both turn bright green", "Both remain unchanged"),
                ("the color change shown by natural turmeric paper indicator when exposed to a basic substance like soap or detergent", "Turns from bright yellow to deep reddish-brown", "Turns from yellow to blue", "Turns from yellow to pink", "Remains yellow"),
                ("why a bright yellow curry turmeric stain on a white shirt turns reddish-brown when washed with domestic laundry soap", "Soap is alkaline/basic in nature, which chemically reacts with turmeric turning it reddish-brown", "Soap contains red synthetic dye", "Turmeric dissolves into grease", "Water oxidizes turmeric to acid"),
                ("the color changes produced by China rose (Gudhul flower) petal extract in acidic and basic solutions", "Turns dark pink (magenta) in acidic solution, and turns bright green in basic solution", "Turns red in acid and blue in base", "Turns yellow in acid and pink in base", "Turns colorless in acid and black in base"),
                ("the color behavior of synthetic indicator phenolphthalein in acidic, neutral, and basic media", "Completely colorless in acidic and neutral solutions; turns deep bright pink (magenta) in basic solution", "Pink in acid and colorless in base", "Yellow in acid and red in base", "Blue in acid and red in base"),
                ("the color behavior of synthetic indicator methyl orange in acidic and basic media", "Turns red/pink in acidic solution, and turns bright yellow in basic solution", "Yellow in acid and red in base", "Colorless in acid and pink in base", "Blue in acid and green in base"),
                ("indicators whose characteristic odor (smell) changes or vanishes in acidic or basic solutions (e.g., onion extract, vanilla essence, clove oil)", "Olfactory indicators", "Universal indicators", "Visual pH indicators", "Radiometric indicators")
            ],
            'tmpls': [
                "Which diagnostic chemical diagnostic group is defined as: {0}?",
                "Which classic lichen-derived indicator corresponds to: {0}?",
                "What diagnostic litmus color shift occurs in: {0}?",
                "What diagnostic litmus response indicates: {0}?",
                "What chromatic reaction occurs when: {0}?",
                "What chemical pH indicator reaction explains why: {0}?",
                "What chromatic transitions characterize: {0}?",
                "What specific color transitions define: {0}?",
                "What diagnostic chromatic behavior characterizes: {0}?",
                "Which olfactory diagnostic category is defined as: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Indicator Chemistry Context**\\nThe statement details {item[0]}.\\n**Step 2: Chromatic Transitions across pH Ranges**\\nLitmus: red in acid, blue in base; Turmeric: red-brown in base; China rose: magenta in acid, green in base; Phenolphthalein: pink in base, colorless in acid.\\n**Step 3: Verification**\\nThe matching chemical response is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Neutralization Reaction & Thermochemistry
        {
            'data': [
                ("the chemical reaction between an acid and a base that produces a salt and water with the evolution of thermal heat", "Neutralization reaction (\\(\\text{Acid} + \\text{Base} \\rightarrow \\text{Salt} + \\text{Water} + \\text{Heat}\\))", "Decomposition reaction", "Electrolytic synthesis", "Photochemical halogenation"),
                ("the balanced chemical equation for the classic neutralization reaction between hydrochloric acid and sodium hydroxide", "\\(HCl + NaOH \\rightarrow NaCl + H_2O + \\text{Heat}\\)", "\\(2HCl + NaOH \\rightarrow NaCl_2 + H_2O\\)", "\\(HCl + Na_2O \\rightarrow 2NaCl + H_2O\\)", "\\(HCl + Na(OH)_2 \\rightarrow NaCl + 2H_2O\\)"),
                ("why the temperature of the reaction mixture always rises during an acid-base neutralization reaction in a test tube", "Neutralization is an exothermic reaction that liberates heat energy (standard enthalpy of neutralization \\(\\approx -57.1\\text{ kJ/mol}\\))", "Neutralization absorbs heat from the room", "Water boiling point increases", "The test tube friction generates heat"),
                ("the net ionic equation representing the fundamental chemical reaction of all strong acid-strong base neutralizations", "\\(H^+ (aq) + OH^- (aq) \\rightarrow H_2O (l) + 57.1\\text{ kJ}\\)", "\\(Na^+ + Cl^- \\rightarrow NaCl\\)", "\\(H^+ + Cl^- \\rightarrow HCl\\)", "\\(2H_2 + O_2 \\rightarrow 2H_2O\\)"),
                ("the chemical product formed alongside water in any acid-base neutralization reaction", "Salt (an ionic compound consisting of metallic cation from base and non-metallic anion from acid)", "Sugar", "Pure element", "Alkali metal"),
                ("the nature of the aqueous salt solution formed when a strong acid (e.g., \\(HCl\\)) reacts with a strong base (e.g., \\(NaOH\\))", "Neutral salt solution (pH = 7, e.g., \\(NaCl\\))", "Acidic salt solution (pH < 7)", "Basic salt solution (pH > 7)", "Insoluble oxide precipitate"),
                ("the nature of the aqueous salt solution formed when a strong acid (e.g., \\(HCl\\)) reacts with a weak base (e.g., \\(NH_4OH\\))", "Acidic salt solution (pH < 7, e.g., \\(NH_4Cl\\))", "Neutral salt solution", "Strongly basic solution", "Insoluble double salt"),
                ("the nature of the aqueous salt solution formed when a weak acid (e.g., \\(CH_3COOH\\)) reacts with a strong base (e.g., \\(NaOH\\))", "Basic salt solution (pH > 7, e.g., \\(CH_3COONa\\))", "Acidic salt solution", "Neutral salt solution", "Covalent non-electrolyte"),
                ("the continuous quantitative laboratory technique of adding a standardized acid slowly from a burette to a known volume of base until complete neutralization is reached", "Acid-base titration", "Fractional crystallization", "Electrolytic refining", "Simple decantation"),
                ("the point during an acid-base titration where chemically equivalent amounts of acid and base have reacted completely, signaled by an indicator color change", "Equivalence point (or End point)", "Boiling point", "Freezing point", "Triple point")
            ],
            'tmpls': [
                "Which foundational chemical reaction is defined as: {0}?",
                "Which balanced stoichiometric neutralization equation represents: {0}?",
                "What thermodynamic physical reason explains why: {0}?",
                "Which fundamental net ionic equation describes: {0}?",
                "What ionic chemical product is defined by: {0}?",
                "What aqueous pH characteristic defines: {0}?",
                "What solution pH property characterizes: {0}?",
                "What salt solution property results when: {0}?",
                "Which quantitative analytical laboratory method corresponds to: {0}?",
                "Which stoichiometric titration milestone is defined as: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Neutralization Context**\\nThe query highlights {item[0]}.\\n**Step 2: Reaction Enthalpy and Salt Hydrolysis**\\n\\(H^+ + OH^- \\rightarrow H_2O\\) releases \\(\\sim 57.1\\text{{ kJ/mol}}\\). Strong acid + strong base gives neutral salt; strong acid + weak base yields acidic salt; weak acid + strong base yields basic salt.\\n**Step 3: Verification**\\nThe matching chemical concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Neutralization in Daily Life: Antacids, Stings, Soil & Industrial Waste
        {
            'data': [
                ("the therapeutic treatment for acute gastric acidity and heartburn caused by excessive secretion of hydrochloric acid (\\(HCl\\)) in the human stomach", "Administering an antacid containing a mild base like Milk of Magnesia (\\(Mg(OH)_2\\)) or sodium bicarbonate (\\(NaHCO_3\\)) to neutralize excess acid", "Drinking concentrated lemon juice", "Taking strong sulphuric acid", "Eating spicy fried food"),
                ("the therapeutic home treatment applied to skin to relieve the painful acidic burn of an ant sting or honeybee sting", "Rubbing moist baking soda (\\(NaHCO_3\\)) or calamine lotion containing zinc carbonate (\\(ZnCO_3\\)) to neutralize formic acid", "Applying concentrated vinegar", "Rubbing lemon juice", "Washing with dilute hydrochloric acid"),
                ("the home treatment recommended to soothe the burning alkaline sting of a wasp (which injects an alkaline fluid)", "Applying a mild acid such as vinegar (acetic acid) or diluted lemon juice to neutralize the alkali", "Rubbing caustic soda", "Applying baking soda paste", "Rubbing slaked lime"),
                ("the agricultural practice applied when farming soil becomes excessively acidic due to excessive chemical fertilizer use", "Treating the soil with quicklime (calcium oxide, \\(CaO\\)) or slaked lime (calcium hydroxide, \\(Ca(OH)_2\\)) to neutralize acidity", "Adding more ammonium sulphate", "Flooding the field with dilute acid", "Covering the field with plastic sheets"),
                ("the agricultural practice applied when farming soil becomes overly alkaline/basic (pH > 8.5)", "Adding organic decaying manure/compost, which releases organic acids during decomposition that neutralize soil basicity", "Adding quicklime", "Adding sodium hydroxide", "Adding slaked lime"),
                ("why industrial factory effluents containing acidic chemical wastes must be chemically treated before discharging into natural rivers and lakes", "Acidic effluents would severely alter water pH and kill fish and aquatic organisms; they are neutralized by adding slaked lime (\\(Ca(OH)_2\\))", "To make river water turn blue", "To speed up river water flow", "To convert industrial effluents into drinking milk"),
                ("why commercial toothpaste is deliberately formulated with mild basic/alkaline compounds", "To neutralize the organic acids produced by oral bacteria fermenting trapped food particles, preventing tooth enamel decay", "To make toothpaste foam only", "To bleach the tongue white", "To dissolve the jawbone"),
                ("the formation of acid rain is primarily caused by atmospheric industrial emissions of which acidic anhydride gases", "Sulphur dioxide (\\(SO_2\\)) and Nitrogen dioxide (\\(NO_2\\)), forming sulphuric acid and nitric acid", "Carbon monoxide and hydrogen", "Pure nitrogen and oxygen", "Methane and helium"),
                ("the visible yellowing and marble erosion ('marble cancer') observed on historical monuments like the Taj Mahal in Agra is caused by", "Acid rain reacting with marble calcium carbonate: \\(CaCO_3 + H_2SO_4 \\rightarrow CaSO_4 + H_2O + CO_2\\)", "Dust storms physically grinding marble", "Direct sunlight bleaching marble", "Algal photosynthesis"),
                ("the chemical formula representing the principal chemical compound present in calamine soothing lotion used for ant stings", "Zinc carbonate (\\(ZnCO_3\\))", "Zinc chloride (\\(ZnCl_2\\))", "Zinc sulphate (\\(ZnSO_4\\))", "Zinc oxide exclusively")
            ],
            'tmpls': [
                "Which medical therapeutic neutralization protocol treats: {0}?",
                "Which dermatological home remedy neutralizes: {0}?",
                "Which alkaline sting neutralization treatment applies to: {0}?",
                "Which agronomic remediation technique corrects: {0}?",
                "Which soil conditioning treatment remediates: {0}?",
                "What environmental ecological protection rationale mandates: {0}?",
                "What dental prophylactic chemical rationale explains why: {0}?",
                "Which atmospheric chemical pollutants trigger: {0}?",
                "Which architectural acid-corrosion reaction explains: {0}?",
                "Which chemical active ingredient corresponds to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Real-World Neutralization Context**\\nThe statement details {item[0]}.\\n**Step 2: Practical Application Principles**\\nAcidity is neutralized with mild bases (antacids, baking soda, lime); alkalinity is neutralized with mild acids (vinegar, compost organic acids).\\n**Step 3: Verification**\\nThe matching concept is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 5: pH Scale Basics & Universal Indicators
        {
            'data': [
                ("the numerical logarithmic scale ranging from 0 to 14 introduced by Danish biochemist S.P.L. Sørensen in 1909 to measure hydrogen ion concentration", "pH scale", "Mohs hardness scale", "Richter magnitude scale", "Kelvin scale"),
                ("on the standard pH scale at \\(25^\\circ\\text{C}\\), a completely neutral solution (such as pure distilled water) has a pH value of", "Exactly 7.0 (where \\([H^+] = [OH^-] = 10^{-7}\\text{ M}\\))", "0.0", "14.0", "1.0"),
                ("on the pH scale, solutions having pH values strictly less than 7 (pH < 7) are classified as", "Acidic solutions (lower pH indicates higher acidity and stronger \\([H^+]\\))", "Basic solutions", "Neutral solutions", "Alkaline buffers"),
                ("on the pH scale, solutions having pH values strictly greater than 7 (pH > 7) are classified as", "Basic (alkaline) solutions (higher pH indicates stronger alkalinity)", "Acidic solutions", "Neutral solutions", "Pure solvents"),
                ("between two acidic solutions A with pH = 2 and B with pH = 5, which solution is significantly more acidic and by what factor of hydrogen ion concentration?", "Solution A is 1000 times (\\(10^3\\)) more acidic than Solution B", "Solution B is 3 times more acidic", "Both are equally acidic", "Solution A is 3 times more acidic"),
                ("the typical physiological pH range of healthy human blood strictly maintained by physiological bicarbonate buffers", "Between 7.35 and 7.45 (slightly alkaline)", "Between 5.5 and 6.0 (acidic)", "Between 8.5 and 9.0 (strongly basic)", "Exactly 7.00 always"),
                ("the normal pH of gastric juice in the human stomach required for pepsin activation", "Between 1.5 and 2.5 (strongly acidic due to concentrated \\(HCl\\))", "Between 7.0 and 8.0", "Between 11.0 and 12.0", "Between 5.0 and 6.0"),
                ("a mixture of several different organic chemical dyes that produces a smooth spectrum of colors over the entire pH range from 0 to 14", "Universal indicator (available as solution or paper strips with calibrated color chart)", "Litmus paper", "Phenolphthalein", "Methyl orange"),
                ("the color displayed by a universal indicator paper strip when dipped into a strongly acidic solution of pH 1", "Dark red / crimson", "Deep purple / violet", "Bright green", "Golden yellow"),
                ("the color displayed by a universal indicator paper strip when dipped into a strongly alkaline solution of pH 13 to 14", "Deep purple / dark violet", "Crimson red", "Pale green", "Bright yellow")
            ],
            'tmpls': [
                "Which logarithmic chemical measurement scale is defined as: {0}?",
                "What is the precise baseline value for: {0}?",
                "Which chemical acidity classification corresponds to: {0}?",
                "Which chemical alkalinity classification corresponds to: {0}?",
                "Compare the hydrogen ion concentration disparity between: {0}?",
                "What is the strict homeostatic physiological range for: {0}?",
                "What is the resting biochemical pH value for: {0}?",
                "Which broad-spectrum chemical indicator is defined as: {0}?",
                "What chromatic diagnostic color indicates: {0}?",
                "What extreme alkaline diagnostic color represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: pH Scale Context**\\nThe question targets {item[0]}.\\n**Step 2: Logarithmic Acidity Analysis**\\n\\(\\text{{pH}} = -\\log_{{10}}[H^+]\\). pH < 7 is acidic, 7 is neutral, pH > 7 is basic. Each unit shift represents a 10-fold change in \\([H^+]\\).\\n**Step 3: Verification**\\nThe correct physical-chemical answer is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Common Salts, Formulae & Industrial Uses
        {
            'data': [
                ("the chemical name and formula of common table salt used in daily cooking and food preservation", "Sodium chloride (\\(NaCl\\))", "Sodium bicarbonate (\\(NaHCO_3\\))", "Sodium carbonate (\\(Na_2CO_3\\))", "Potassium chloride (\\(KCl\\))"),
                ("the salt known as Plaster of Paris (POP) used for setting fractured bones and making decorative casts and statues", "Calcium sulphate hemihydrate (\\(CaSO_4\\cdot \\frac{1}{2}H_2O\\))", "Calcium sulphate dihydrate (Gypsum)", "Calcium carbonate", "Magnesium sulphate"),
                ("the chemical equation representing the setting of Plaster of Paris (POP) into hard gypsum upon mixing with water", "\\(CaSO_4\\cdot \\frac{1}{2}H_2O + 1\\frac{1}{2}H_2O \\rightarrow CaSO_4\\cdot 2H_2O \\text{ (Gypsum)}\\)", "\\(CaSO_4 + 2H_2O \\rightarrow Ca(OH)_2 + H_2SO_4\\)", "\\(CaCO_3 + H_2O \\rightarrow Ca(OH)_2 + CO_2\\)", "\\(CaO + H_2O \\rightarrow Ca(OH)_2\\)"),
                ("the chemical substance known as bleaching powder used for disinfecting drinking water and industrial bleaching of textiles", "Calcium oxychloride (\\(CaOCl_2\\))", "Calcium chloride (\\(CaCl_2\\))", "Sodium hypochlorite (\\(NaClO\\))", "Potassium chlorate (\\(KClO_3\\))"),
                ("the chemical reaction by which bleaching powder is manufactured industrially", "Action of chlorine gas on dry slaked lime: \\(Ca(OH)_2 + Cl_2 \\rightarrow CaOCl_2 + H_2O\\)", "Reaction of quicklime with hydrochloric acid", "Electrolysis of brine solution", "Heating limestone strongly"),
                ("the constituent chemicals present in commercial baking powder that cause cakes to rise light and fluffy upon heating", "A mixture of baking soda (\\(NaHCO_3\\)) and an edible mild organic acid like tartaric acid (along with starch)", "Pure sodium hydroxide", "Pure calcium carbonate", "Washing soda and vinegar"),
                ("why tartaric acid is essentially blended with baking soda in baking powder", "To react with and neutralize the bitter-tasting sodium carbonate (\\(Na_2CO_3\\)) produced when baking soda decomposes by heat", "To make the cake taste sour", "To prevent the cake from drying", "To add yellow color"),
                ("the chemical gas evolved when baking powder reacts with water and heat, creating thousands of tiny bubbles that make bread spongy", "Carbon dioxide (\\(CO_2\\))", "Oxygen (\\(O_2\\))", "Hydrogen (\\(H_2\\))", "Nitrogen (\\(N_2\\))"),
                ("the chemical compound known as Epsom salt used as a therapeutic bath salt and saline laxative", "Magnesium sulphate heptahydrate (\\(MgSO_4\\cdot 7H_2O\\))", "Copper sulphate pentahydrate", "Sodium sulphate decahydrate", "Calcium sulphate dihydrate"),
                ("the chemical compound known as green vitriol used in making iron inks and agricultural iron sprays", "Ferrous sulphate heptahydrate (\\(FeSO_4\\cdot 7H_2O\\))", "Copper sulphate pentahydrate", "Zinc sulphate heptahydrate", "Potassium permanganate")
            ],
            'tmpls': [
                "Which common culinary salt is identified as: {0}?",
                "Which medical orthopedic setting compound corresponds to: {0}?",
                "Which balanced hydration equation represents: {0}?",
                "Which municipal disinfectant chemical is defined as: {0}?",
                "Which industrial chemical synthesis reaction produces: {0}?",
                "Which culinary leavening mixture corresponds to: {0}?",
                "What chemical neutralization purpose explains why: {0}?",
                "Which leavening gas creates sponge texture in: {0}?",
                "Which therapeutic heptahydrate salt matches: {0}?",
                "Which traditional green vitriol compound represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Salt Chemistry Context**\\nThe statement details {item[0]}.\\n**Step 2: Hydration and Chemical Formulations**\\nSalts form via neutralization; water of crystallization determines structural forms: POP (\\(CaSO_4\\cdot \\frac{{1}}{{2}}H_2O\\)), Gypsum (\\(CaSO_4\\cdot 2H_2O\\)), Bleaching powder (\\(CaOCl_2\\)).\\n**Step 3: Verification**\\nThe matching chemical compound is {item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 7: Quantitative Problems in Neutralization & Stoichiometry
        {
            'data': [
                ("Calculate the mass of sodium hydroxide (\\(NaOH\\), molar mass \\(40\\text{ g/mol}\\)) required to completely neutralize \\(36.5\\text{ g}\\) (\\(1\\text{ mole}\\)) of hydrochloric acid (\\(HCl\\)).", "\\(40.0\\text{ g}\\)", "\\(20.0\\text{ g}\\)", "\\(80.0\\text{ g}\\)", "\\(58.5\\text{ g}\\)"),
                ("How many grams of common salt (\\(NaCl\\), molar mass \\(58.5\\text{ g/mol}\\)) are produced when \\(36.5\\text{ g}\\) of \\(HCl\\) reacts completely with \\(40.0\\text{ g}\\) of \\(NaOH\\)?", "\\(58.5\\text{ g}\\)", "\\(76.5\\text{ g}\\)", "\\(98.5\\text{ g}\\)", "\\(18.0\\text{ g}\\)"),
                ("In a neutralization reaction, \\(98\\text{ g}\\) of sulphuric acid (\\(H_2SO_4\\), molar mass \\(98\\text{ g/mol}\\)) reacts with sodium hydroxide according to \\(H_2SO_4 + 2NaOH \\rightarrow Na_2SO_4 + 2H_2O\\). What mass of \\(NaOH\\) is required for complete neutralization?", "\\(80.0\\text{ g } (2 \\times 40\\text{ g})\\)", "\\(40.0\\text{ g}\\)", "\\(98.0\\text{ g}\\)", "\\(142.0\\text{ g}\\)"),
                ("What mass of calcium oxide (\\(CaO\\), molar mass \\(56\\text{ g/mol}\\)) is needed to neutralize \\(73\\text{ g}\\) (\\(2\\text{ moles}\\)) of hydrochloric acid (\\(HCl\\)) via \\(CaO + 2HCl \\rightarrow CaCl_2 + H_2O\\)?", "\\(56.0\\text{ g}\\)", "\\(28.0\\text{ g}\\)", "\\(112.0\\text{ g}\\)", "\\(73.0\\text{ g}\\)"),
                ("If a strong acid and strong base react to produce \\(2\\text{ moles}\\) of water, calculate the total heat energy released (taking enthalpy of neutralization as \\(57.1\\text{ kJ/mole}\\)).", "\\(114.2\\text{ kJ}\\)", "\\(57.1\\text{ kJ}\\)", "\\(28.55\\text{ kJ}\\)", "\\(228.4\\text{ kJ}\\)"),
                ("If \\(50\\text{ mL}\\) of \\(0.1\\text{ M } HCl\\) neutralizes \\(25\\text{ mL}\\) of \\(NaOH\\) solution, calculate the molar concentration of the \\(NaOH\\) solution (\\(M_1V_1 = M_2V_2\\)).", "\\(0.2\\text{ M}\\)", "\\(0.1\\text{ M}\\)", "\\(0.05\\text{ M}\\)", "\\(0.4\\text{ M}\\)"),
                ("Calculate the formula unit mass of sodium hydrogen carbonate (baking soda, \\(NaHCO_3\\)) taking \\(Na = 23\\text{ u}\\), \\(H = 1\\text{ u}\\), \\(C = 12\\text{ u}\\), \\(O = 16\\text{ u}\\).", "\\(84\\text{ u } (23 + 1 + 12 + 48 = 84\\text{ u})\\)", "\\(68\\text{ u}\\)", "\\(106\\text{ u}\\)", "\\(92\\text{ u}\\)"),
                ("Calculate the formula unit mass of washing soda (anhydrous sodium carbonate, \\(Na_2CO_3\\)) taking \\(Na = 23\\text{ u}\\), \\(C = 12\\text{ u}\\), \\(O = 16\\text{ u}\\).", "\\(106\\text{ u } (2 \\times 23 + 12 + 48 = 106\\text{ u})\\)", "\\(84\\text{ u}\\)", "\\(120\\text{ u}\\)", "\\(96\\text{ u}\\)"),
                ("Calculate the formula unit mass of washing soda crystals (\\(Na_2CO_3\\cdot 10H_2O\\)) taking \\(Na_2CO_3 = 106\\text{ u}\\) and \\(H_2O = 18\\text{ u}\\).", "\\(286\\text{ u } (106 + 10 \\times 18 = 286\\text{ u})\\)", "\\(180\\text{ u}\\)", "\\(206\\text{ u}\\)", "\\(310\\text{ u}\\)"),
                ("Calculate the percentage by mass of water of crystallization in washing soda crystals (\\(Na_2CO_3\\cdot 10H_2O\\), formula mass \\(286\\text{ u}\\)).", "\\(62.94\\% \\text{ (approx } 63\\%\\))", "\\(37.06\\%\\)", "\\(50.0\\%\\)", "\\(75.5\\%\\)")
            ],
            'tmpls': [
                "Calculate stoichiometric base reactant mass: {0}",
                "Determine neutral salt product mass: {0}",
                "Compute diprotic acid neutralization mass: {0}",
                "Calculate quicklime neutralization requirement: {0}",
                "Evaluate total exothermic neutralization enthalpy: {0}",
                "Determine unknown alkaline molarity: {0}",
                "Compute baking soda formula mass: {0}",
                "Calculate anhydrous sodium carbonate formula mass: {0}",
                "Compute decahydrate crystal formula mass: {0}",
                "Calculate decahydrate water percentage: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract molar masses, stoichiometric coefficients, molarities, or heat values from the problem.\\n**Step 2: Arithmetic Evaluation**\\nApply molar stoichiometry (\\(n = \\frac{{m}}{{M}}\\)), titration relation (\\(M_1V_1 = M_2V_2\\)), or \\(\\Delta H = n \\times 57.1\\text{{ kJ}}\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def gen_19_3_4():
    tc = "MH-9-SCIT-19-19.3.4"
    tname = "Natural resources: air, water, soil properties & conservation"
    archs = [
        # Arch 0: Atmosphere Layers & Air Composition
        {
            'data': [
                ("the lowest layer of the Earth's atmosphere extending up to ~13 km where almost all weather phenomena (clouds, rain, wind) occur", "Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"),
                ("the atmospheric layer extending from 13 km to 50 km containing the vital ozone layer (\\(O_3\\)) that absorbs harmful solar ultraviolet rays", "Stratosphere", "Troposphere", "Exosphere", "Ionosphere"),
                ("the coldest layer of the atmosphere where incoming meteors burn up upon entry, extending from 50 km to 80 km", "Mesosphere", "Stratosphere", "Thermosphere", "Troposphere"),
                ("the percentage composition by volume of dry atmospheric air for nitrogen (\\(N_2\\)) and oxygen (\\(O_2\\))", "Nitrogen: ~78.08%; Oxygen: ~20.95%", "Nitrogen: 50%; Oxygen: 50%", "Nitrogen: 21%; Oxygen: 78%", "Nitrogen: 90%; Oxygen: 10%"),
                ("the noble gas that constitutes the third most abundant gas in the Earth's dry atmosphere at approximately 0.93% by volume", "Argon (\\(Ar\\))", "Carbon dioxide", "Helium", "Neon"),
                ("the present concentration of carbon dioxide (\\(CO_2\\)) in atmospheric air", "Approximately 0.04% (around 420 parts per million, ppm)", "0.4%", "4.0%", "0.001%"),
                ("the noble gas used to fill electric filament lamps to prevent tungsten evaporation and extend bulb life", "Argon (\\(Ar\\))", "Helium", "Hydrogen", "Oxygen"),
                ("the non-flammable noble gas with very low density used for filling meteorological weather balloons and airships", "Helium (\\(He\\))", "Hydrogen (highly flammable)", "Nitrogen", "Methane"),
                ("the noble gas used in decorative advertising glow signs producing a characteristic brilliant reddish-orange glow", "Neon (\\(Ne\\))", "Argon", "Krypton", "Xenon"),
                ("the international ecological treaty signed in 1987 to phase out chlorofluorocarbons (CFCs) and protect the stratospheric ozone layer", "Montreal Protocol (World Ozone Day is observed on September 16)", "Kyoto Protocol", "Paris Agreement", "Ramsar Convention")
            ],
            'tmpls': [
                "Which atmospheric layer is characterized as: {0}?",
                "Which protective atmospheric stratum corresponds to: {0}?",
                "Which coldest atmospheric layer is defined by: {0}?",
                "What is the precise volumetric fraction for: {0}?",
                "Which third most abundant atmospheric gas represents: {0}?",
                "What is the current atmospheric fraction of: {0}?",
                "Which inert lighting gas corresponds to: {0}?",
                "Which safe buoyant gas represents: {0}?",
                "Which luminous commercial discharge gas is defined by: {0}?",
                "Which landmark international ozone agreement corresponds to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Atmospheric Science Context**\\nThe statement details {item[0]}.\\n**Step 2: Atmospheric Structure and Composition**\\nAtmosphere contains 78% \\(N_2\\), 21% \\(O_2\\), 0.93% \\(Ar\\), and 0.04% \\(CO_2\\); Stratosphere shields via \\(O_3\\); Troposphere hosts weather.\\n**Step 3: Verification**\\nThe matching concept is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Air Pollution, Greenhouse Effect & Acid Rain
        {
            'data': [
                ("the phenomenon where atmospheric greenhouse gases (\\(CO_2, CH_4, N_2O, H_2O\\) vapor) trap outgoing infrared radiation warming Earth's surface", "Greenhouse effect", "Ozone depletion", "Thermal inversion", "Photochemical smog"),
                ("the primary greenhouse gas whose concentration has risen by over 50% since the industrial revolution due to fossil fuel combustion and deforestation", "Carbon dioxide (\\(CO_2\\))", "Oxygen", "Nitrogen", "Argon"),
                ("the potent greenhouse gas released from paddy rice fields, cattle digestion (enteric fermentation), and decomposing garbage landfills", "Methane (\\(CH_4\\))", "Carbon monoxide", "Sulphur dioxide", "Nitrogen dioxide"),
                ("the toxic, colorless, odorless gas produced by the incomplete combustion of fossil fuels that binds irreversibly to hemoglobin forming carboxyhemoglobin", "Carbon monoxide (\\(CO\\))", "Carbon dioxide", "Sulphur dioxide", "Nitrogen oxide"),
                ("the atmospheric pollution phenomenon formed by the interaction of sunlight with automobile nitrogen oxides and volatile hydrocarbons", "Photochemical smog", "Acid rain", "Greenhouse effect", "Stratospheric ozone"),
                ("the industrial gases responsible for acid rain that react with atmospheric water vapor to form sulphuric acid and nitric acid", "Sulphur dioxide (\\(SO_2\\)) and Nitrogen oxides (\\(NO_x\\))", "Carbon dioxide and oxygen", "Methane and ammonia", "Hydrogen and helium"),
                ("the harmful ecological impacts of acid rain on terrestrial and aquatic ecosystems", "Acidifies freshwater lakes killing aquatic fish, leaches toxic aluminum from soils, and damages forest tree canopies", "Increases crop yields", "Purifies groundwater", "Expands polar glaciers"),
                ("the synthetic chemical compounds previously used in refrigerators, air conditioners, and aerosol sprays that catalyze ozone depletion", "Chlorofluorocarbons (CFCs / Freons)", "Hydrocarbons", "Noble gases", "Carbonates"),
                ("the chemical radical released when CFCs are broken down by solar UV rays in the stratosphere that catalytic destroys thousands of ozone molecules", "Chlorine free radical (\\(Cl^\\bullet\\))", "Fluorine ion", "Carbon atom", "Nitrate radical"),
                ("the particulate air quality metric measuring airborne inhalable toxic dust and soot particles with diameters \\(\\le 2.5\\text{ micrometres}\\)", "PM 2.5 (Fine particulate matter)", "PM 100", "AQI index alone", "UV index")
            ],
            'tmpls': [
                "Which thermal radiation phenomenon is defined as: {0}?",
                "Which principal anthropogenic greenhouse gas corresponds to: {0}?",
                "Which agricultural greenhouse gas represents: {0}?",
                "Which deadly asphyxiating combustion byproduct is defined as: {0}?",
                "Which urban solar-driven air pollution represents: {0}?",
                "Which industrial precursor gases trigger: {0}?",
                "What extensive environmental damage is caused by: {0}?",
                "Which commercial refrigerant chemicals correspond to: {0}?",
                "Which catalytic stratospheric radical is responsible for: {0}?",
                "Which microscopic particulate metric corresponds to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Environmental Atmospheric Pollution Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Anthropogenic Pollutant Chemistry**\\nGreenhouse gases (\\(CO_2, CH_4\\)) trap heat; \\(SO_2/NO_x\\) produce acid rain; CFCs release \\(Cl^\\bullet\\) destroying stratospheric \\(O_3\\).\\n**Step 3: Verification**\\nThe correct environmental science answer is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Water Properties, Distribution & Anomalous Expansion
        {
            'data': [
                ("the percentage distribution of the Earth's total water between saline oceans and total freshwater", "Saline ocean water: ~97%; Total freshwater: ~3% (with 2.7% locked in glaciers/polar ice and only ~0.3% liquid fresh water)", "Oceans: 50%; Freshwater: 50%", "Oceans: 80%; Freshwater: 20%", "Oceans: 99.9%; Freshwater: 0.1%"),
                ("the physical property that allows liquid water to dissolve a wider variety of ionic and polar substances than any other known liquid", "Universal solvent (due to high dielectric constant and strong dipole polarity)", "High viscosity", "Low surface tension", "Zero latent heat"),
                ("the temperature at which liquid water achieves its maximum density (\\(1.000\\text{ g/cm}^3\\)) under normal atmospheric pressure", "\\(4^\\circ\\text{C}\\)", "\\(0^\\circ\\text{C}\\)", "\\(100^\\circ\\text{C}\\)", "\\(-4^\\circ\\text{C}\\)"),
                ("the physical behavior where water expands upon cooling between \\(4^\\circ\\text{C}\\) and \\(0^\\circ\\text{C}\\), causing solid ice to be less dense than liquid water", "Anomalous expansion of water", "Thermal contraction", "Sublimation", "Capillary depression"),
                ("why solid ice floats on liquid water instead of sinking to the bottom", "Ice has an open, cage-like hexagonal crystal lattice with large empty spaces held by hydrogen bonds, making its density lower (\\(0.917\\text{ g/cm}^3\\)) than water", "Ice contains trapped air bubbles only", "Ice repels gravity", "Water exerts negative pressure"),
                ("the high quantity of heat required to raise the temperature of water (\\(4184\\text{ J/kg}\\cdot^\\circ\\text{C}\\)) which moderates coastal climates", "Specific heat capacity of water", "Latent heat of fusion", "Surface tension", "Thermal conductivity"),
                ("the property of liquid water caused by cohesive intermolecular hydrogen bonding that enables insects like water striders to walk on water surfaces", "Surface tension", "Viscosity", "Buoyancy", "Capillarity"),
                ("the upward movement of water through narrow soil pores and xylem plant conduits against gravity", "Capillary action (driven by cohesion and adhesion)", "Transpirational cooling", "Gravitational drainage", "Hydraulic pumping"),
                ("the disease caused by drinking microbial contaminated water containing Vibrio cholerae bacteria", "Cholera (acute waterborne bacterial infection)", "Malaria (vector-borne)", "Dengue", "Scurvy"),
                ("the international standard guideline for human access to safe potable drinking water", "Free from pathogenic microorganisms, toxic heavy metals (arsenic, lead), and possessing balanced dissolved minerals", "Pure distilled water with zero minerals", "Water containing chlorine above 10%", "Boiled sea water")
            ],
            'tmpls': [
                "What is the global hydrological distribution for: {0}?",
                "Which chemical solvent property characterizes: {0}?",
                "At what precise temperature point does: {0}?",
                "Which thermodynamic anomaly is defined as: {0}?",
                "What hydrogen-bonded crystal lattice physics explains why: {0}?",
                "Which thermal buffering property corresponds to: {0}?",
                "Which cohesive intermolecular fluid property enables: {0}?",
                "Which hydrodynamic transport mechanism represents: {0}?",
                "Which waterborne bacterial gastrointestinal pathology matches: {0}?",
                "What public health biochemical criteria define: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Water Resource Context**\\nThe statement details {item[0]}.\\n**Step 2: Molecular and Physical Properties**\\nPolarity makes water universal solvent; anomalous density peak at \\(4^\\circ\\text{{C}}\\) allows ice to float, preserving aquatic habitats.\\n**Step 3: Verification**\\nThe matching scientific answer is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 3: Water Conservation & Rainwater Harvesting
        {
            'data': [
                ("the technique of collecting and storing rainwater from rooftops and surface catchments for direct use or groundwater recharge", "Rainwater harvesting (RWH)", "Desalination", "Drip irrigation", "Hydroelectric generation"),
                ("the specialized agricultural irrigation method where water is delivered drop by drop directly to the root zone of plants, minimizing evaporation loss", "Drip irrigation (Micro-irrigation)", "Flood irrigation", "Sprinkler irrigation", "Furrow irrigation"),
                ("the traditional community water harvesting structures constructed across seasonal streams in Rajasthan and Maharashtra to impound monsoon runoff and recharge wells", "Johads, check dams, and bandharas", "Canals only", "Hydro dams", "Tube wells"),
                ("the environmental 3R (or 5R) conservation principle for sustainable resource management", "Reduce, Reuse, Recycle (and Refuse, Recover)", "Remove, Replace, Relocate", "Refine, React, Rebuild", "Resell, Rebuy, Return"),
                ("the underground permeable geological rock formation or sediment layer that holds and yields groundwater to wells and springs", "Aquifer", "Bedrock", "Magma chamber", "Clay horizon"),
                ("the upper natural boundary of the underground saturated groundwater zone", "Water table", "Artesian level", "Soil profile", "Humus layer"),
                ("the physical process by which surface rainwater slowly seeps downward through soil layers to replenish groundwater reserves", "Infiltration (Percolation)", "Transpiration", "Condensation", "Sublimation"),
                ("the advanced industrial membrane filtration process that forces sea water under high pressure across a semi-permeable membrane to produce fresh drinking water", "Reverse Osmosis (RO desalination)", "Simple filtration", "Electrolysis", "Crystallization"),
                ("the domestic practice of recycling gently used household wastewater from washbasins, showers, and laundry for garden irrigation and toilet flushing", "Greywater recycling", "Blackwater disposal", "Sewage dumping", "Potable distillation"),
                ("the primary cause of rapid depletion of underground water tables in agricultural regions across India", "Over-extraction of groundwater by deep submersible tube-wells for water-intensive cash crops (e.g., sugarcane, paddy)", "Decreased rainfall alone", "Urbanization only", "Solar evaporation")
            ],
            'tmpls': [
                "Which sustainable water management technique is defined as: {0}?",
                "Which water-efficient agronomic technique corresponds to: {0}?",
                "Which traditional Indian rainwater conservation structures represent: {0}?",
                "Which environmental sustainability framework represents: {0}?",
                "Which geological groundwater reservoir is defined as: {0}?",
                "Which hydrological groundwater boundary represents: {0}?",
                "Which groundwater recharge seepage process corresponds to: {0}?",
                "Which industrial membrane desalination technology represents: {0}?",
                "Which wastewater reclamation conservation practice represents: {0}?",
                "What agronomic overdraft mechanism explains: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Water Conservation Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Hydrogeology and Conservation Technologies**\\nGroundwater management relies on rainwater harvesting, percolation recharge, aquifer replenishment, and drip irrigation to balance extraction rates.\\n**Step 3: Verification**\\nThe correct conservation concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Soil Profile & Horizons (O, A, B, C, R)
        {
            'data': [
                ("the dark-colored, porous organic matter in soil formed by the microbial decomposition of dead plant and animal residues that enriches soil fertility", "Humus", "Clay", "Silt", "Bedrock"),
                ("the vertical section through the soil showing all its successive developmental layers (horizons) from surface to unweathered bedrock", "Soil profile", "Geological strata", "Topographical contour", "Sedimentary column"),
                ("the uppermost mineral soil horizon (A-horizon) rich in organic humus, soft, porous, and sheltering earthworms, roots, and microbes", "Topsoil (A-horizon)", "Subsoil (B-horizon)", "Substratum (C-horizon)", "Bedrock (R-horizon)"),
                ("the soil horizon situated beneath the topsoil (B-horizon) that contains harder, compact mineral matter with less humus but rich in accumulated iron oxides and clay", "Subsoil (B-horizon)", "Topsoil (A-horizon)", "Organic litter (O-horizon)", "Bedrock (R-horizon)"),
                ("the soil horizon (C-horizon) consisting of partially weathered, cracked, and fissured parent rock fragments", "Substratum (C-horizon / Parent rock fragments)", "Topsoil", "Subsoil", "Organic humus"),
                ("the solid, unweathered, impermeable rock layer lying at the very base of the soil profile that cannot be dug easily with a spade", "Bedrock (R-horizon / Parent rock)", "Subsoil", "Topsoil", "Eluvial layer"),
                ("the soil type containing a well-balanced mixture of sand, silt, clay, and rich humus, universally regarded as the best soil for growing crops", "Loamy soil (Loam)", "Pure sandy soil", "Heavy clayey soil", "Gravel soil"),
                ("the soil type characterized by large mineral particles with large air spaces between them, possessing high water drainage but poor water retention", "Sandy soil", "Clayey soil", "Loamy soil", "Peat soil"),
                ("the soil type characterized by microscopic tightly packed particles with tiny pore spaces, possessing high water-holding capacity but poor aeration", "Clayey soil", "Sandy soil", "Loamy soil", "Gravelly soil"),
                ("the beneficial annelid worm termed the 'friend of the farmer' that aerates the soil by burrowing and converts organic waste into rich vermicompost", "Earthworm (Pheretima posthuma)", "Roundworm", "Tapeworm", "Centipede")
            ],
            'tmpls': [
                "Which vital organic soil constituent is defined as: {0}?",
                "Which comprehensive vertical pedological view corresponds to: {0}?",
                "Which fertile upper soil stratum represents: {0}?",
                "Which dense intermediate mineral stratum corresponds to: {0}?",
                "Which fragmented rock horizon is characterized by: {0}?",
                "Which basal impenetrable lithic layer represents: {0}?",
                "Which agronomic soil textural class is recognized as: {0}?",
                "Which coarse-grained soil texture matches: {0}?",
                "Which fine-textured, water-retaining soil type represents: {0}?",
                "Which beneficial soil annelid organism is celebrated as: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Pedology and Soil Profile Context**\\nThe statement details {item[0]}.\\n**Step 2: Soil Horizons and Textural Classification**\\nSoil horizons: O (humus), A (topsoil), B (subsoil), C (weathered rock), R (bedrock). Loamy soil balances sand, silt, and clay for optimal plant aeration and water retention.\\n**Step 3: Verification**\\nThe matching pedological answer is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 5: Soil Weathering, Erosion & Conservation Methods
        {
            'data': [
                ("the natural breakdown of massive bedrocks into fine soil particles through physical, chemical, and biological forces over thousands of years", "Weathering of rocks", "Soil erosion", "Sedimentation", "Soil leaching"),
                ("the removal and transportation of fertile topsoil from the land surface by running water, wind, or human activities", "Soil erosion", "Soil weathering", "Humification", "Bioremediation"),
                ("the agricultural practice of planting broad belts of trees and tall shrubs along farmland boundaries to break the speed of strong winds and prevent wind erosion", "Shelter belts (Windbreaks)", "Terrace farming", "Contour ploughing", "Crop rotation"),
                ("the agricultural practice of cutting flat steps or terraces into steep mountain hillsides to slow water runoff and prevent erosion", "Terrace farming", "Shelter belts", "Strip cropping", "Overgrazing"),
                ("the farming technique of ploughing parallel along the natural contour lines of a sloping hill rather than up and down the slope", "Contour ploughing", "Terrace farming", "Clear-cutting", "Monoculture"),
                ("the practice of growing different types of crops sequentially on the same agricultural plot across seasons to maintain soil nitrogen and fertility", "Crop rotation (e.g., alternating cereals with leguminous pulses)", "Monocropping", "Deforestation", "Slash and burn agriculture"),
                ("the single most effective long-term method for preventing widespread soil erosion on barren lands", "Afforestation (planting large numbers of trees whose roots bind the soil firmly)", "Building concrete roads", "Deep tilling with tractors", "Removing all grass cover"),
                ("how uncontrolled overgrazing by domestic cattle and goats accelerates severe soil erosion", "Animals eat away grass and vegetative ground cover, and their hooves pulverize the soil structure, exposing loose topsoil to wind and rain", "Animals compact soil making it impermeable", "Animals add too much organic manure", "Animals lower the air temperature"),
                ("the catastrophic formation of deep gullies and ravines (badland topography) caused by unchecked running rainwater carving into barren clay soils", "Gully erosion (as seen in the Chambal ravines)", "Sheet erosion", "Wind erosion", "Glacial drift"),
                ("the gradual removal of a thin, uniform surface layer of topsoil across a large expanse of land by rainfall runoff without visible channels", "Sheet erosion", "Gully erosion", "Rill erosion", "Wind abrasion")
            ],
            'tmpls': [
                "Which natural pedogenic process is defined as: {0}?",
                "Which destructive land degradation process corresponds to: {0}?",
                "Which agricultural wind-barrier conservation method represents: {0}?",
                "Which hillside agricultural conservation technique corresponds to: {0}?",
                "Which slope-following tillage practice matches: {0}?",
                "Which agronomic crop-sequencing strategy represents: {0}?",
                "Which foundational vegetative conservation intervention represents: {0}?",
                "What livestock management impact explains how: {0}?",
                "Which severe hydraulic land degradation phenomenon represents: {0}?",
                "Which subtle broad-scale hydraulic erosion type is defined as: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Soil Erosion and Conservation Context**\\nThe query highlights {item[0]}.\\n**Step 2: Mechanics of Soil Conservation**\\nRoots bind topsoil preventing erosion; hillside terracing, contour ploughing, shelterbelts, and afforestation counteract sheet and gully erosion.\\n**Step 3: Verification**\\nThe matching agronomic concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Soil Physical Properties: Moisture, Percolation Rate & Absorption
        {
            'data': [
                ("the physical rate at which liquid water passes downward through a given soil sample, expressed in millilitres per minute (\\(\\text{mL/min}\\))", "Percolation rate of water in soil", "Moisture retention capacity", "Bulk density", "Soil porosity fraction"),
                ("the mathematical formula used to calculate the percolation rate of water through soil", "\\(\\text{Percolation rate (mL/min)} = \\frac{\\text{Amount of water (mL)}}{\\text{Percolation time (min)}}\\)", "\\(\\text{Percolation rate} = \\text{Amount of water} \\times \\text{Time}\\)", "\\(\\text{Percolation rate} = \\frac{\\text{Percolation time}}{\\text{Water amount}}\\)", "\\(\\text{Percolation rate} = \\text{Mass of soil} \\times \\text{Time}\\)"),
                ("among sandy soil, clayey soil, and loamy soil, which soil exhibits the highest (fastest) percolation rate of water?", "Sandy soil (large particles leave large interconnected pore spaces allowing rapid drainage)", "Clayey soil", "Loamy soil", "Peaty soil"),
                ("among sandy soil, clayey soil, and loamy soil, which soil exhibits the lowest (slowest) percolation rate of water?", "Clayey soil (extremely fine particles leave tiny micropores that hold water tenaciously)", "Sandy soil", "Loamy soil", "Gravelly soil"),
                ("the water content trapped within microscopic soil capillary pores and absorbed on soil particle surfaces available to plant roots", "Soil moisture", "Gravitational drainage water", "Water table", "Percolation surplus"),
                ("the simple laboratory method to detect the presence of moisture in a dry-looking soil sample", "Heating the soil gently in a test tube; evaporated water vapor condenses as visible droplets on the cooler upper inner walls of the tube", "Adding hydrochloric acid", "Testing with blue litmus paper", "Passing electric current through soil"),
                ("why the air directly above agricultural farmland appears shimmering and shimmering on a hot sunny afternoon", "Vaporizing soil moisture rises into the hot air above, creating warm air layers of differing refractive index that refract sunlight unevenly", "Soil particles emit radioactive heat", "Earth's magnetic field bends light", "Plants emit visible carbon dioxide"),
                ("which soil property is calculated by \\(\\frac{\\text{Mass of water absorbed}}{\\text{Mass of soil sample}} \\times 100\\%\\)?", "Percentage of water absorbed by soil", "Percolation rate in mL/min", "Soil organic fraction", "Clay content fraction"),
                ("which soil type absorbs and holds the highest percentage of water by mass?", "Clayey soil (large total microscopic surface area retains maximum water)", "Sandy soil", "Gravel soil", "Coarse silt"),
                ("the ideal soil pH range required for optimum growth and nutrient absorption of most agricultural crops", "Between 6.0 and 7.5 (slightly acidic to neutral)", "Between 2.0 and 3.5 (highly acidic)", "Between 9.5 and 11.0 (highly alkaline)", "Below 4.5 always")
            ],
            'tmpls': [
                "Which pedological hydraulic metric is defined as: {0}?",
                "Which standard mathematical formula calculates: {0}?",
                "Which soil textural class displays: {0}?",
                "Which fine soil textural class exhibits: {0}?",
                "Which plant-available water compartment corresponds to: {0}?",
                "Which school laboratory procedure demonstrates: {0}?",
                "What optical atmospheric refraction phenomenon explains why: {0}?",
                "Which soil agronomic absorption metric is defined by: {0}?",
                "Which soil texture maximizes: {0}?",
                "What is the optimal pedological pH window for: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Soil Physics Context**\\nThe statement details {item[0]}.\\n**Step 2: Percolation and Moisture Mechanics**\\n\\(\\text{{Rate}} = \\frac{{\\text{{Volume (mL)}}}}{{\\text{{Time (min)}}}}\\). Sandy soil has high percolation rate; clayey soil has low percolation rate and high water retention capacity.\\n**Step 3: Verification**\\nThe matching physical concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Quantitative Problems in Soil Percolation & Water Harvesting
        {
            'data': [
                ("In an experiment, \\(200\\text{ mL}\\) of water takes \\(40\\text{ minutes}\\) to percolate completely through a soil sample. Calculate the percolation rate of the soil in \\(\\text{mL/min}\\).", "\\(5.0\\text{ mL/min } (\\frac{200}{40} = 5.0\\text{ mL/min})\\)", "\\(8.0\\text{ mL/min}\\)", "\\(4.0\\text{ mL/min}\\)", "\\(10.0\\text{ mL/min}\\)"),
                ("In a soil testing experiment, \\(300\\text{ mL}\\) of water percolates through a sandy soil sample in \\(15\\text{ minutes}\\). Calculate the percolation rate.", "\\(20.0\\text{ mL/min } (\\frac{300}{15} = 20.0\\text{ mL/min})\\)", "\\(15.0\\text{ mL/min}\\)", "\\(25.0\\text{ mL/min}\\)", "\\(10.0\\text{ mL/min}\\)"),
                ("In a clayey soil sample, \\(100\\text{ mL}\\) of water takes \\(50\\text{ minutes}\\) to percolate completely. Calculate the percolation rate.", "\\(2.0\\text{ mL/min } (\\frac{100}{50} = 2.0\\text{ mL/min})\\)", "\\(4.0\\text{ mL/min}\\)", "\\(1.0\\text{ mL/min}\\)", "\\(5.0\\text{ mL/min}\\)"),
                ("A \\(50\\text{ g}\\) sample of dry soil is used in a funnel experiment. If \\(100\\text{ mL}\\) of water is poured and \\(70\\text{ mL}\\) drips through into the measuring cylinder below, how much water was absorbed by the soil?", "\\(30\\text{ mL } (100\\text{ mL} - 70\\text{ mL} = 30\\text{ mL})\\)", "\\(70\\text{ mL}\\)", "\\(50\\text{ mL}\\)", "\\(20\\text{ mL}\\)"),
                ("For the \\(50\\text{ g}\\) soil sample above that absorbed \\(30\\text{ mL } (30\\text{ g})\\) of water, calculate the percentage of water absorbed by the soil.", "\\(60.0\\% \\text{ (} \\frac{30}{50} \\times 100\\% = 60\\%\\text{)}\\)", "\\(30.0\\%\\)", "\\(40.0\\%\\)", "\\(70.0\\%\\)"),
                ("A \\(100\\text{ g}\\) soil sample is heated strongly in an oven until completely dry. If the mass of soil decreases from \\(100\\text{ g}\\) to \\(84\\text{ g}\\), calculate the moisture percentage of the original soil sample.", "\\(16.0\\% \\text{ (} \\frac{100 - 84}{100} \\times 100\\% = 16\\%\\text{)}\\)", "\\(84.0\\%\\)", "\\(14.0\\%\\)", "\\(20.0\\%\\)"),
                ("A building has a flat rooftop catchment area of \\(100\\text{ m}^2\\). During a storm, \\(50\\text{ mm } (0.05\\text{ m})\\) of rainfall occurs. Assuming \\(80\\%\\) harvesting efficiency, calculate the total volume of water collected in litres.", "\\(4000\\text{ litres } (100 \\times 0.05 \\times 0.8 \\times 1000\\text{ L})\\)", "\\(5000\\text{ litres}\\)", "\\(2500\\text{ litres}\\)", "\\(8000\\text{ litres}\\)"),
                ("A family uses \\(500\\text{ litres}\\) of water per day. If a domestic rainwater tank stores \\(30,000\\text{ litres}\\), for how many days can this harvested water supply the family?", "\\(60\\text{ days } (\\frac{30000}{500} = 60\\text{ days})\\)", "\\(50\\text{ days}\\)", "\\(90\\text{ days}\\)", "\\(30\\text{ days}\\)"),
                ("If a leaky household tap drips at a rate of \\(1\\text{ drop per second}\\) and \\(20\\text{ drops} = 1\\text{ mL}\\), calculate how much water is wasted in \\(24\\text{ hours } (86,400\\text{ seconds})\\).", "\\(4.32\\text{ litres } (4320\\text{ mL})\\)", "\\(8.64\\text{ litres}\\)", "\\(2.16\\text{ litres}\\)", "\\(1.00\\text{ litre}\\)"),
                ("A farm uses drip irrigation delivering \\(2\\text{ litres/hour}\\) per plant instead of flood irrigation using \\(10\\text{ litres/hour}\\) per plant. Calculate the percentage of water conserved.", "\\(80.0\\% \\text{ (} \\frac{10 - 2}{10} \\times 100\\% = 80\\%\\text{)}\\)", "\\(50.0\\%\\)", "\\(20.0\\%\\)", "\\(90.0\\%\\)")
            ],
            'tmpls': [
                "Calculate soil percolation rate: {0}",
                "Evaluate sandy soil percolation velocity: {0}",
                "Determine clayey soil drainage velocity: {0}",
                "Compute retained water volume in soil: {0}",
                "Calculate percentage of water absorption: {0}",
                "Determine soil gravimetric moisture percentage: {0}",
                "Calculate harvested rainwater catchment volume: {0}",
                "Determine household storage sustainability duration: {0}",
                "Compute daily leakage water wastage: {0}",
                "Evaluate drip irrigation water conservation efficiency: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract water volume, percolation time, catchment area, rainfall depth, or masses from the problem.\\n**Step 2: Arithmetic Evaluation**\\nCompute \\(\\text{{Percolation Rate}} = \\frac{{V}}{{t}}\\) or \\(\\text{{Volume}} = \\text{{Area}} \\times \\text{{Depth}} \\times \\text{{Efficiency}}\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)
