# scripts/generate_topic4_1.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-4-4.1"
CHAPTER_NUM = 4

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: Law of Conservation of Mass
    ("""Who formulated the 'Law of Conservation of Mass' in 1774?""",
     ["John Dalton", "Antoine Lavoisier", "Joseph Proust", "Ernest Rutherford"],
     "B", "OSC", "easy",
     "• Antoine Lavoisier formulated the Law of Conservation of Mass and is known as the Father of Modern Chemistry.\nCorrect Choice is (B)."),

    ("""What does the Law of Conservation of Mass state regarding a chemical reaction?""",
     ["Energy is created whenever chemical bonds are formed",
      "In a chemical reaction, the total mass of the reactants equals the total mass of the products formed",
      "Volume of gas reactants always equals volume of gas products",
      "Mass of products is always slightly less than reactants due to heat release"],
     "B", "OSC", "easy",
     "• In any closed chemical reaction, matter is neither created nor destroyed; total mass of reactants equals total mass of products.\nCorrect Choice is (B)."),

    ("""In a closed flask, \\(5.3\\text{ g}\\) of sodium carbonate reacts completely with \\(6.0\\text{ g}\\) of ethanoic acid. If \\(2.2\\text{ g}\\) of carbon dioxide gas and \\(0.9\\text{ g}\\) of water are produced, what is the mass of sodium ethanoate formed?""",
     ["\\(8.2\\text{ g}\\)", "\\(11.3\\text{ g}\\)", "\\(3.1\\text{ g}\\)", "\\(9.1\\text{ g}\\)"],
     "A", "OSC", "medium",
     "• Total mass of reactants = \\(5.3 + 6.0 = 11.3\\text{ g}\\).\nTotal mass of products = \\(m + 2.2 + 0.9 = m + 3.1\\text{ g}\\).\nBy Law of Conservation of Mass: \\(m + 3.1 = 11.3 \\implies m = 11.3 - 3.1 = 8.2\\text{ g}\\).\nCorrect Choice is (A)."),

    ("""When \\(100\\text{ g}\\) of calcium carbonate (\\(\\text{CaCO}_3\\)) is heated strongly in a closed vessel, it decomposes into \\(56\\text{ g}\\) of calcium oxide (\\(\\text{CaO}\\)) and carbon dioxide gas (\\(\\text{CO}_2\\)). What is the mass of \\(\\text{CO}_2\\) released?""",
     ["\\(40\\text{ g}\\)", "\\(44\\text{ g}\\)", "\\(56\\text{ g}\\)", "\\(100\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• Mass of \\(\\text{CO}_2 = 100 - 56 = 44\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""Which scientist is universally acknowledged as the 'Father of Modern Chemistry' for establishing quantitative measurement and chemical nomenclature?""",
     ["Antoine Laurent Lavoisier", "Jöns Jacob Berzelius", "Dmitri Mendeleev", "Robert Boyle"],
     "A", "OSC", "easy",
     "• Antoine Lavoisier revolutionized chemistry by introducing quantitative precision and establishing the Law of Conservation of Mass.\nCorrect Choice is (A)."),

    ("""Why must a chemical experiment verifying the Law of Conservation of Mass involving a gas-evolving reaction be performed in a tightly CLOSED flask?""",
     ["To prevent air temperature from rising",
      "To prevent evolved gases from escaping into the atmosphere, which would cause an apparent loss of mass on the weighing balance",
      "To accelerate the rate of chemical reaction",
      "To keep light away from the reactants"],
     "B", "OSC", "medium",
     "• If gaseous products escape into the surroundings, the final recorded mass will be less than the initial mass, appearing to violate mass conservation.\nCorrect Choice is (B)."),

    ("""In an experiment, \\(10.0\\text{ g}\\) of barium chloride solution is mixed with \\(10.0\\text{ g}\\) of sodium sulphate solution in a sealed conical flask. A white precipitate of barium sulphate forms. What is the total mass of the flask and contents after reaction?""",
     ["Less than initial mass because a solid formed",
      "Exactly equal to the initial mass before reaction",
      "Greater than initial mass because precipitate is heavy",
      "Zero"],
     "B", "OSC", "easy",
     "• By the Law of Conservation of Mass, the mass of the closed system remains strictly identical before and after precipitation.\nCorrect Choice is (B)."),

    ("""A piece of magnesium ribbon of mass \\(2.4\\text{ g}\\) burns completely in open air to form \\(4.0\\text{ g}\\) of white magnesium oxide powder. How much oxygen from the air combined with the magnesium?""",
     ["\\(0.8\\text{ g}\\)", "\\(1.6\\text{ g}\\)", "\\(2.4\\text{ g}\\)", "\\(6.4\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• Mass of oxygen consumed = Mass of \\(\\text{MgO}\\) - Mass of \\(\\text{Mg} = 4.0 - 2.4 = 1.6\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""Which law of chemical combination was experimentally verified using Landolt's H-shaped tube?""",
     ["Law of Multiple Proportions", "Law of Conservation of Mass", "Law of Gaseous Volumes", "Avogadro's Law"],
     "B", "OSC", "medium",
     "• Landolt used sealed H-shaped glass tubes containing separate solutions to confirm with extreme precision that no change in mass occurs upon mixing.\nCorrect Choice is (B)."),

    ("""When \\(12\\text{ g}\\) of carbon burns completely in \\(32\\text{ g}\\) of oxygen, how many grams of carbon dioxide gas are formed?""",
     ["\\(20\\text{ g}\\)", "\\(32\\text{ g}\\)", "\\(44\\text{ g}\\)", "\\(56\\text{ g}\\)"],
     "C", "OSC", "easy",
     "• Total mass = \\(12 + 32 = 44\\text{ g}\\) of \\(\\text{CO}_2\\).\nCorrect Choice is (C)."),

    # 11-20: Law of Constant Proportion (Proust)
    ("""Who stated the 'Law of Constant Proportion' (also known as the Law of Definite Proportions) in 1799?""",
     ["Antoine Lavoisier", "Joseph Louis Proust", "John Dalton", "Amedeo Avogadro"],
     "B", "OSC", "easy",
     "• French chemist Joseph Louis Proust stated the Law of Constant Proportion in 1799.\nCorrect Choice is (B)."),

    ("""What is the formal statement of the Law of Constant Proportion?""",
     ["Elements always combine in equal volumes at STP",
      "The proportion by weight of the constituent elements in any pure chemical compound is always fixed and independent of its source or method of preparation",
      "The total mass of reactants equals total mass of products",
      "Atoms of the same element have different masses"],
     "B", "OSC", "easy",
     "• The Law of Constant Proportion states that a given chemical compound always contains its component elements in fixed ratio by mass.\nCorrect Choice is (B)."),

    ("""In pure water (\\(\\text{H}_2\\text{O}\\)), what is the fixed ratio by mass of Hydrogen to Oxygen?""",
     ["\\(1 : 2\\)", "\\(1 : 8\\)", "\\(1 : 16\\)", "\\(2 : 1\\)"],
     "B", "OSC", "easy",
     "• In \\(\\text{H}_2\\text{O}\\), mass of H = \\(2 \\times 1 = 2\\text{ u}\\), mass of O = \\(16\\text{ u}\\). Mass ratio \\(\\text{H} : \\text{O} = 2 : 16 = 1 : 8\\).\nCorrect Choice is (B)."),

    ("""If \\(9\\text{ g}\\) of pure water is decomposed completely by electrolysis, what masses of hydrogen and oxygen gases are obtained?""",
     ["\\(1\\text{ g}\\) of hydrogen and \\(8\\text{ g}\\) of oxygen",
      "\\(2\\text{ g}\\) of hydrogen and \\(7\\text{ g}\\) of oxygen",
      "\\(4.5\\text{ g}\\) of hydrogen and \\(4.5\\text{ g}\\) of oxygen",
      "\\(3\\text{ g}\\) of hydrogen and \\(6\\text{ g}\\) of oxygen"],
     "A", "OSC", "easy",
     "• By the constant ratio of \\(1 : 8\\), \\(9\\text{ g}\\) of water decomposes into \\(1\\text{ g}\\) of \\(\\text{H}_2\\) and \\(8\\text{ g}\\) of \\(\\text{O}_2\\).\nCorrect Choice is (A)."),

    ("""What mass of oxygen gas is required to react completely with \\(4\\text{ g}\\) of hydrogen gas to produce water?""",
     ["\\(8\\text{ g}\\)", "\\(16\\text{ g}\\)", "\\(32\\text{ g}\\)", "\\(64\\text{ g}\\)"],
     "C", "OSC", "medium",
     "• Ratio of \\(\\text{H} : \\text{O} = 1 : 8\\). For \\(4\\text{ g}\\) of hydrogen, mass of oxygen needed = \\(4 \\times 8 = 32\\text{ g}\\).\nCorrect Choice is (C)."),

    ("""If \\(3\\text{ g}\\) of hydrogen gas is mixed with \\(30\\text{ g}\\) of oxygen gas and ignited, how much water will be formed, and which reactant remains in excess?""",
     ["\\(33\\text{ g}\\) of water, no excess",
      "\\(27\\text{ g}\\) of water, with \\(6\\text{ g}\\) of oxygen remaining unreacted",
      "\\(24\\text{ g}\\) of water, with \\(1\\text{ g}\\) of hydrogen remaining",
      "\\(30\\text{ g}\\) of water, with \\(3\\text{ g}\\) of oxygen remaining"],
     "B", "OSC", "hard",
     "• Hydrogen and oxygen combine in \\(1:8\\) mass ratio. \\(3\\text{ g}\\) of \\(\\text{H}_2\\) requires \\(3 \\times 8 = 24\\text{ g}\\) of \\(\\text{O}_2\\).\nWater produced = \\(3 + 24 = 27\\text{ g}\\).\nExcess oxygen left = \\(30 - 24 = 6\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""What is the fixed proportion by mass of Carbon to Oxygen in pure carbon dioxide (\\(\\text{CO}_2\\))?""",
     ["\\(1 : 2\\)", "\\(3 : 8\\)", "\\(3 : 4\\)", "\\(12 : 16\\)"],
     "B", "OSC", "easy",
     "• In \\(\\text{CO}_2\\), mass of C = \\(12\\text{ u}\\), mass of O = \\(2 \\times 16 = 32\\text{ u}\\). Ratio \\(\\text{C} : \\text{O} = 12 : 32 = 3 : 8\\).\nCorrect Choice is (B)."),

    ("""In ammonia gas (\\(\\text{NH}_3\\)), what is the constant ratio by mass of Nitrogen to Hydrogen?""",
     ["\\(1 : 3\\)", "\\(14 : 3\\)", "\\(7 : 3\\)", "\\(14 : 1\\)"],
     "B", "OSC", "easy",
     "• Atomic mass of N = \\(14\\text{ u}\\), H = \\(1\\text{ u}\\). For \\(\\text{NH}_3\\), mass ratio \\(\\text{N} : \\text{H} = 14 : (3 \\times 1) = 14 : 3\\).\nCorrect Choice is (B)."),

    ("""In hydrogen peroxide (\\(\\text{H}_2\\text{O}_2\\)), what is the proportion by mass of Hydrogen to Oxygen?""",
     ["\\(1 : 8\\)", "\\(1 : 16\\)", "\\(2 : 16\\)", "\\(1 : 32\\)"],
     "B", "OSC", "medium",
     "• In \\(\\text{H}_2\\text{O}_2\\), mass of H = \\(2 \\times 1 = 2\\text{ u}\\), mass of O = \\(2 \\times 16 = 32\\text{ u}\\). Ratio \\(\\text{H} : \\text{O} = 2 : 32 = 1 : 16\\).\nCorrect Choice is (B)."),

    ("""Whether water is obtained from tap water, river, rainwater, or synthesized in a laboratory, the percentage of hydrogen by mass is always approximately:""",
     ["\\(50\\%\\)", "\\(11.11\\%\\)", "\\(88.89\\%\\)", "\\(2.0\\%\\)"],
     "B", "OSC", "medium",
     "• Percentage of H = \\(\\frac{2}{18} \\times 100 = 11.11\\%\\); percentage of O = \\(\\frac{16}{18} \\times 100 = 88.89\\%\\).\nCorrect Choice is (B)."),

    # 21-30: Dalton's Atomic Theory & Proust experiments
    ("""Which atomic theory provided the first successful theoretical and physical explanation for both the Law of Conservation of Mass and the Law of Constant Proportion?""",
     ["Thomson's Plum Pudding Model",
      "Dalton's Atomic Theory (1808)",
      "Bohr's Quantum Model",
      "Rutherford's Nuclear Model"],
     "B", "OSC", "easy",
     "• John Dalton's postulates (indivisible atoms that combine in simple whole-number ratios) provided the scientific rationale for both laws.\nCorrect Choice is (B)."),

    ("""Which postulate of Dalton's atomic theory directly explains the Law of Conservation of Mass?""",
     ["Atoms of different elements have different masses",
      "Atoms are indivisible particles that can neither be created nor destroyed in a chemical reaction",
      "Atoms combine in whole number ratios to form compounds",
      "All atoms of a given element are identical in chemical properties"],
     "B", "OSC", "easy",
     "• Because atoms cannot be created or destroyed, the total number and kinds of atoms before and after a reaction remain identical, conserving mass.\nCorrect Choice is (B)."),

    ("""Which postulate of Dalton's atomic theory directly explains the Law of Constant Proportion?""",
     ["Atoms of the same element have the same mass",
      "The relative number and kinds of atoms are constant in a given compound",
      "Atoms of an element are spherical",
      "Matter is composed of small particles called atoms"],
     "B", "OSC", "easy",
     "• A given compound always consists of fixed proportions of atoms of specific elements, ensuring a constant mass ratio.\nCorrect Choice is (B)."),

    ("""Proust analyzed two samples of copper carbonate (cupric carbonate) — one naturally occurring malachite and the other synthesized in the laboratory. What did he discover?""",
     ["The natural sample had double the copper content of the synthetic sample",
      "Both samples had identical percentages by weight of copper, carbon, and oxygen",
      "The synthetic sample contained no oxygen",
      "The natural sample contained no carbon"],
     "B", "OSC", "medium",
     "• Both natural and synthetic copper carbonate yielded identical proportions: \\(51.35\\%\\) copper, \\(9.74\\%\\) carbon, and \\(38.91\\%\\) oxygen by weight.\nCorrect Choice is (B)."),

    ("""Assertion (A): When \\(10\\text{ g}\\) of calcium carbonate is heated strongly in an open crucible, the remaining residue weighs only \\(5.6\\text{ g}\\), apparently losing \\(4.4\\text{ g}\\).\nReason (R): The Law of Conservation of Mass is violated in open systems.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "C", "OAR", "medium",
     "• (A) is true because \\(4.4\\text{ g}\\) of \\(\\text{CO}_2\\) gas escapes into the room. (R) is false: the Law of Conservation of Mass is universal and never violated; the apparent loss is simply the mass of escaping gaseous product.\nCorrect Choice is (C)."),

    ("""Assertion (A): Pure carbon dioxide prepared by burning coal in air or by reacting marble chips with dilute hydrochloric acid has a fixed carbon to oxygen mass ratio of \\(3 : 8\\).\nReason (R): According to Proust's Law of Constant Proportion, a chemical compound always contains elements combined in a fixed ratio by weight regardless of origin.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "• Both statements are correct, and (R) is the exact governing scientific law.\nCorrect Choice is (A)."),

    ("""Assertion (A): In water (\\(\\text{H}_2\\text{O}\\)), the mass ratio of \\(\\text{H} : \\text{O}\\) is \\(1 : 8\\), whereas in hydrogen peroxide (\\(\\text{H}_2\\text{O}_2\\)), the mass ratio is \\(1 : 16\\).\nReason (R): Different chemical compounds formed from the same elements have their own specific, characteristic constant proportions by mass.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "• Each distinct compound has a unique fixed ratio of its constituent elements.\nCorrect Choice is (A)."),

    ("""State True or False: In any chemical reaction, the total volume of gaseous reactants must always strictly equal the total volume of gaseous products.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. While MASS is strictly conserved, volume and mole counts frequently change during reactions (e.g. \\(2\\text{H}_2 + \\text{O}_2 \\to 2\\text{H}_2\\text{O}\\): 3 volumes of gas form 2 volumes of steam).\nCorrect Choice is (B)."),

    ("""State True or False: The Law of Constant Proportion is valid for all pure chemical compounds, but is NOT applicable to variable mixtures such as air, saltwater, or brass alloy.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Mixtures have variable compositions, whereas chemical compounds possess fixed atomic proportions.\nCorrect Choice is (A)."),

    ("""When \\(12\\text{ g}\\) of carbon is burned in \\(16\\text{ g}\\) of oxygen in a limited air supply, carbon monoxide (\\(\\text{CO}\\)) is formed. What is the fixed mass ratio of Carbon to Oxygen in carbon monoxide?""",
     ["\\(3 : 8\\)", "\\(3 : 4\\)", "\\(1 : 1\\)", "\\(12 : 32\\)"],
     "B", "OSC", "medium",
     "• In \\(\\text{CO}\\), mass of C = \\(12\\text{ u}\\), mass of O = \\(16\\text{ u}\\). Ratio \\(\\text{C} : \\text{O} = 12 : 16 = 3 : 4\\).\nCorrect Choice is (B)."),

    # 31-40: Fill in the blanks & Numerical problems
    ("""Fill in the blank: In a chemical reaction, mass can neither be ________ nor destroyed.""",
     ["Transformed", "Created", "Measured", "Combined"],
     "B", "OFB", "easy",
     "• Mass can neither be created nor destroyed in a chemical reaction.\nCorrect Choice is (B)."),

    ("""Fill in the blank: The proportion by mass of constituent elements in any chemical compound is always ________.""",
     ["Variable", "Constant (fixed)", "Proportional to temperature", "Dependent on atmospheric pressure"],
     "B", "OFB", "easy",
     "• The proportion by mass is constant (fixed).\nCorrect Choice is (B)."),

    ("""Fill in the blank: In methane gas (\\(\\text{CH}_4\\)), the fixed ratio by mass of Carbon to Hydrogen is ________.""",
     ["\\(1 : 4\\)", "\\(3 : 1\\)", "\\(12 : 1\\)", "\\(4 : 1\\)"],
     "B", "OFB", "medium",
     "• Mass of C = \\(12\\text{ u}\\), mass of 4H = \\(4 \\times 1 = 4\\text{ u}\\). Ratio \\(\\text{C} : \\text{H} = 12 : 4 = 3 : 1\\).\nCorrect Choice is (B)."),

    ("""A student heats \\(24.5\\text{ g}\\) of potassium chlorate (\\(\\text{KClO}_3\\)). It decomposes completely into \\(14.9\\text{ g}\\) of potassium chloride residue and oxygen gas. What mass of oxygen gas was produced?""",
     ["\\(8.0\\text{ g}\\)", "\\(9.6\\text{ g}\\)", "\\(10.0\\text{ g}\\)", "\\(12.2\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• Mass of oxygen = \\(24.5 - 14.9 = 9.6\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""How many grams of carbon dioxide gas are produced when \\(6\\text{ g}\\) of pure carbon burns completely with sufficient oxygen?""",
     ["\\(11\\text{ g}\\)", "\\(22\\text{ g}\\)", "\\(44\\text{ g}\\)", "\\(88\\text{ g}\\)"],
     "B", "OSC", "medium",
     "• In \\(\\text{CO}_2\\), ratio \\(\\text{C} : \\text{O} = 3 : 8\\), and total \\(\\text{CO}_2\\) per \\(3\\text{ g}\\) of C is \\(11\\text{ g}\\).\nFor \\(6\\text{ g}\\) of carbon (\\(2 \\times 3\\text{ g}\\)), mass of \\(\\text{CO}_2 = 2 \\times 11 = 22\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""If \\(20\\text{ g}\\) of calcium combines with \\(8\\text{ g}\\) of oxygen to form calcium oxide (\\(\\text{CaO}\\)), what is the constant proportion by mass of \\(\\text{Ca} : \\text{O}\\)?""",
     ["\\(2 : 1\\)", "\\(5 : 2\\)", "\\(10 : 3\\)", "\\(4 : 1\\)"],
     "B", "OSC", "medium",
     "• Mass ratio \\(\\text{Ca} : \\text{O} = 20 : 8 = 5 : 2\\).\nCorrect Choice is (B)."),

    ("""How much calcium oxide (\\(\\text{CaO}\\)) is formed when \\(10\\text{ g}\\) of calcium reacts completely with \\(4\\text{ g}\\) of oxygen?""",
     ["\\(10\\text{ g}\\)", "\\(14\\text{ g}\\)", "\\(20\\text{ g}\\)", "\\(28\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• By the Law of Conservation of Mass: Mass of product = \\(10 + 4 = 14\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""In an experiment, \\(1.5\\text{ g}\\) of hydrocarbon fuel completely combusts in \\(4.8\\text{ g}\\) of oxygen to form \\(4.4\\text{ g}\\) of \\(\\text{CO}_2\\) and water vapor. What is the mass of water vapor produced?""",
     ["\\(1.9\\text{ g}\\)", "\\(2.7\\text{ g}\\)", "\\(3.3\\text{ g}\\)", "\\(0.9\\text{ g}\\)"],
     "A", "OSC", "medium",
     "• Total reactants = \\(1.5 + 4.8 = 6.3\\text{ g}\\).\nTotal products = \\(4.4 + m_{\\text{water}} = 6.3\\text{ g} \\implies m_{\\text{water}} = 6.3 - 4.4 = 1.9\\text{ g}\\).\nCorrect Choice is (A)."),

    ("""Which fundamental scientific concept distinguishes a chemical compound from a mechanical mixture?""",
     ["Compounds have variable constituent ratios",
      "Compounds have fixed chemical composition by mass and distinct chemical properties different from their constituent elements",
      "Mixtures can never be separated by physical methods",
      "Compounds retain the individual properties of their elements unchanged"],
     "B", "OSC", "easy",
     "• Compounds have fixed composition by mass (Proust's Law) and novel chemical identities.\nCorrect Choice is (B)."),

    ("""What happens when \\(1\\text{ g}\\) of hydrogen is reacted with \\(10\\text{ g}\\) of oxygen?""",
     ["\\(11\\text{ g}\\) of water is formed",
      "\\(9\\text{ g}\\) of water is formed, and \\(2\\text{ g}\\) of oxygen remains unreacted",
      "\\(10\\text{ g}\\) of water is formed, and \\(1\\text{ g}\\) of oxygen remains",
      "No reaction takes place"],
     "B", "OSC", "medium",
     "• Hydrogen and oxygen combine strictly in \\(1 : 8\\) ratio. \\(1\\text{ g}\\) of hydrogen consumes \\(8\\text{ g}\\) of oxygen, producing \\(9\\text{ g}\\) of water. \\(10 - 8 = 2\\text{ g}\\) of oxygen remains unreacted.\nCorrect Choice is (B).")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("""What is the constant mass ratio of Hydrogen to Oxygen in water?""",
     ["\\(1 : 2\\)", "\\(1 : 8\\)", "\\(2 : 16\\)", "\\(1 : 16\\)"],
     "B", "OSC", "easy",
     "• \\(\\text{H}_2\\text{O}\\) mass ratio = \\(2 : 16 = 1 : 8\\).\nCorrect Choice is (B)."),

    ("""What is the constant mass ratio of Carbon to Oxygen in carbon dioxide?""",
     ["\\(1 : 2\\)", "\\(3 : 8\\)", "\\(12 : 16\\)", "\\(3 : 4\\)"],
     "B", "OSC", "easy",
     "• In \\(\\text{CO}_2\\), ratio = \\(12 : 32 = 3 : 8\\).\nCorrect Choice is (B)."),

    ("""According to Lavoisier, during any chemical reaction:""",
     ["Mass is created from nothing",
      "Total mass of reactants equals total mass of products",
      "Mass of gases cannot be measured",
      "Liquid mass always decreases"],
     "B", "OSC", "easy",
     "• Law of Conservation of Mass: mass of reactants equals mass of products.\nCorrect Choice is (B)."),

    ("""Who gave the Law of Constant Proportion in 1799?""",
     ["Proust", "Lavoisier", "Dalton", "Bohr"],
     "A", "OSC", "easy",
     "• Joseph Louis Proust formulated the Law of Constant Proportion.\nCorrect Choice is (A)."),

    ("""When \\(3\\text{ g}\\) of carbon burns in \\(8\\text{ g}\\) of oxygen, what mass of \\(\\text{CO}_2\\) is formed?""",
     ["\\(5\\text{ g}\\)", "\\(8\\text{ g}\\)", "\\(11\\text{ g}\\)", "\\(24\\text{ g}\\)"],
     "C", "OSC", "easy",
     "• \\(3 + 8 = 11\\text{ g}\\) of \\(\\text{CO}_2\\).\nCorrect Choice is (C)."),

    ("""If \\(18\\text{ g}\\) of water is decomposed by electric current, how many grams of oxygen are liberated?""",
     ["\\(2\\text{ g}\\)", "\\(8\\text{ g}\\)", "\\(16\\text{ g}\\)", "\\(18\\text{ g}\\)"],
     "C", "OSC", "easy",
     "• In \\(18\\text{ g}\\) of water, \\(2\\text{ g}\\) is hydrogen and \\(16\\text{ g}\\) is oxygen (\\(1:8\\) ratio).\nCorrect Choice is (C)."),

    ("""What mass of hydrogen is liberated from \\(18\\text{ g}\\) of decomposed water?""",
     ["\\(1\\text{ g}\\)", "\\(2\\text{ g}\\)", "\\(4\\text{ g}\\)", "\\(8\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• Mass of hydrogen = \\(\\frac{1}{9} \\times 18 = 2\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""In sulfur dioxide (\\(\\text{SO}_2\\)), what is the fixed mass ratio of Sulfur (atomic mass \\(32\\)) to Oxygen (atomic mass \\(16\\))?""",
     ["\\(1 : 1\\)", "\\(1 : 2\\)", "\\(2 : 1\\)", "\\(32 : 16\\)"],
     "A", "OSC", "medium",
     "• Mass of S = \\(32\\text{ u}\\), mass of \\(\\text{O}_2 = 2 \\times 16 = 32\\text{ u}\\). Ratio \\(\\text{S} : \\text{O} = 32 : 32 = 1 : 1\\).\nCorrect Choice is (A)."),

    ("""In sulfur trioxide (\\(\\text{SO}_3\\)), what is the constant mass ratio of Sulfur to Oxygen?""",
     ["\\(1 : 1\\)", "\\(2 : 3\\)", "\\(3 : 2\\)", "\\(1 : 3\\)"],
     "B", "OSC", "medium",
     "• Mass of S = \\(32\\text{ u}\\), mass of \\(3\\text{O} = 3 \\times 16 = 48\\text{ u}\\). Ratio \\(\\text{S} : \\text{O} = 32 : 48 = 2 : 3\\).\nCorrect Choice is (B)."),

    ("""When \\(4\\text{ g}\\) of hydrogen reacts with \\(40\\text{ g}\\) of oxygen, how much water is formed?""",
     ["\\(44\\text{ g}\\)", "\\(36\\text{ g}\\)", "\\(32\\text{ g}\\)", "\\(40\\text{ g}\\)"],
     "B", "OSC", "medium",
     "• \\(4\\text{ g}\\) of \\(\\text{H}_2\\) requires \\(4 \\times 8 = 32\\text{ g}\\) of \\(\\text{O}_2\\). Water formed = \\(4 + 32 = 36\\text{ g}\\). \\(8\\text{ g}\\) of oxygen is left in excess.\nCorrect Choice is (B)."),

    ("""What mass of oxygen remains unreacted when \\(4\\text{ g}\\) of hydrogen reacts with \\(40\\text{ g}\\) of oxygen?""",
     ["\\(0\\text{ g}\\)", "\\(4\\text{ g}\\)", "\\(8\\text{ g}\\)", "\\(12\\text{ g}\\)"],
     "C", "OSC", "medium",
     "• Unreacted oxygen = \\(40 - 32 = 8\\text{ g}\\).\nCorrect Choice is (C)."),

    ("""When calcium oxide (\\(\\text{CaO}\\)) reacts with water, slaked lime (\\(\\text{Ca(OH)}_2\\)) is formed. If \\(56\\text{ g}\\) of \\(\\text{CaO}\\) reacts with \\(18\\text{ g}\\) of water, what is the mass of \\(\\text{Ca(OH)}_2\\) formed?""",
     ["\\(56\\text{ g}\\)", "\\(74\\text{ g}\\)", "\\(80\\text{ g}\\)", "\\(38\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• Mass of product = \\(56 + 18 = 74\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""Which law allows chemists to balance chemical equations?""",
     ["Law of Conservation of Mass", "Law of Gravitation", "Boyle's Law", "Hooke's Law"],
     "A", "OSC", "easy",
     "• Chemical equations are balanced so that the number of atoms of each element on both sides is equal, satisfying the Law of Conservation of Mass.\nCorrect Choice is (A)."),

    ("""In a closed vessel, \\(6.3\\text{ g}\\) of \\(\\text{NaHCO}_3\\) is added to \\(15.0\\text{ g}\\) of ethanoic acid solution. The residue left weighs \\(18.0\\text{ g}\\). What is the mass of \\(\\text{CO}_2\\) gas released?""",
     ["\\(3.3\\text{ g}\\)", "\\(2.2\\text{ g}\\)", "\\(4.4\\text{ g}\\)", "\\(1.1\\text{ g}\\)"],
     "A", "OSC", "medium",
     "• Total reactants = \\(6.3 + 15.0 = 21.3\\text{ g}\\).\nMass of \\(\\text{CO}_2 = 21.3 - 18.0 = 3.3\\text{ g}\\).\nCorrect Choice is (A)."),

    ("""What is the percentage by mass of oxygen in pure carbon dioxide (\\(\\text{CO}_2\\))?""",
     ["\\(27.27\\%\\)", "\\(50.0\\%\\)", "\\(72.73\\%\\)", "\\(88.89\\%\\)"],
     "C", "OSC", "medium",
     "• Molecular mass of \\(\\text{CO}_2 = 12 + 32 = 44\\text{ u}\\).\nPercentage of oxygen = \\(\\frac{32}{44} \\times 100 \\approx 72.73\\%\\).\nCorrect Choice is (C)."),

    ("""What is the percentage by mass of carbon in pure carbon dioxide (\\(\\text{CO}_2\\))?""",
     ["\\(27.27\\%\\)", "\\(33.33\\%\\)", "\\(50.0\\%\\)", "\\(72.73\\%\\)"],
     "A", "OSC", "medium",
     "• Percentage of carbon = \\(\\frac{12}{44} \\times 100 \\approx 27.27\\%\\).\nCorrect Choice is (A)."),

    ("""A chemical compound formed from hydrogen and carbon contains \\(75\\%\\) carbon and \\(25\\%\\) hydrogen by mass. What is the mass ratio of \\(\\text{C} : \\text{H}\\)?""",
     ["\\(1 : 3\\)", "\\(3 : 1\\)", "\\(4 : 1\\)", "\\(1 : 4\\)"],
     "B", "OSC", "easy",
     "• Ratio \\(\\text{C} : \\text{H} = 75 : 25 = 3 : 1\\) (corresponds to methane, \\(\\text{CH}_4\\)).\nCorrect Choice is (B)."),

    ("""Why does a log of wood appear to lose mass after being burned completely in an open campfire?""",
     ["Mass is destroyed by heat",
      "Gaseous combustion products (\\(\\text{CO}_2\\), water vapor, and smoke) disperse into the atmosphere; if captured, total mass would equal the original wood and oxygen combined",
      "Wood contains negative mass",
      "Carbon atoms evaporate without mass"],
     "B", "OSC", "easy",
     "• Burning converts wood and atmospheric oxygen into gaseous \\(\\text{CO}_2\\) and \\(\\text{H}_2\\text{O}\\) vapor, which escape into the air.\nCorrect Choice is (B)."),

    ("""When iron rusts in moist air, does the iron nail gain mass, lose mass, or stay the same?""",
     ["Loses mass",
      "Gains mass because it chemically combines with oxygen and water from the air to form hydrated iron oxide",
      "Stays exactly the same",
      "Mass drops to zero"],
     "B", "OSC", "medium",
     "• Rusted iron incorporates oxygen and water molecules from the air, increasing its measured mass.\nCorrect Choice is (B)."),

    ("""In an experiment, \\(2.16\\text{ g}\\) of copper metal on heating with nitric acid and subsequent ignition yields \\(2.70\\text{ g}\\) of copper oxide. What is the percentage of copper in the oxide?""",
     ["\\(20\\%\\)", "\\(50\\%\\)", "\\(80\\%\\)", "\\(90\\%\\)"],
     "C", "OSC", "medium",
     "• Percentage of copper = \\(\\frac{2.16}{2.70} \\times 100 = 80\\%\\).\nCorrect Choice is (C)."),

    ("""In a second experiment, \\(1.15\\text{ g}\\) of copper oxide on reduction by hydrogen yielded \\(0.92\\text{ g}\\) of copper. What is the percentage of copper in this sample?""",
     ["\\(60\\%\\)", "\\(75\\%\\)", "\\(80\\%\\)", "\\(85\\%\\)"],
     "C", "OSC", "medium",
     "• Percentage of copper = \\(\\frac{0.92}{1.15} \\times 100 = 80\\%\\). Since both samples have \\(80\\%\\) copper, this confirms the Law of Constant Proportion.\nCorrect Choice is (C)."),

    ("""State True or False: The Law of Conservation of Mass applies to all physical changes (such as melting ice) as well as chemical reactions.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Melting ice produces the exact same mass of liquid water in a closed container.\nCorrect Choice is (A)."),

    ("""State True or False: Synthetic vitamin C synthesized in a laboratory has a different chemical composition and mass ratio than natural vitamin C extracted from oranges.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. By the Law of Constant Proportion, ascorbic acid (\\(\\text{C}_6\\text{H}_8\\text{O}_6\\)) has identical atomic mass ratios regardless of origin.\nCorrect Choice is (B)."),

    ("""How many grams of oxygen are needed to react with \\(12\\text{ g}\\) of magnesium to form magnesium oxide (\\(\\text{MgO}\\))? (Given atomic masses: \\(\\text{Mg}=24\\), \\(\\text{O}=16\\))""",
     ["\\(4\\text{ g}\\)", "\\(8\\text{ g}\\)", "\\(16\\text{ g}\\)", "\\(24\\text{ g}\\)"],
     "B", "OSC", "medium",
     "• Ratio \\(\\text{Mg} : \\text{O} = 24 : 16 = 3 : 2\\).\nFor \\(12\\text{ g}\\) of \\(\\text{Mg}\\), oxygen needed = \\(\\frac{12 \\times 2}{3} = 8\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""What total mass of magnesium oxide (\\(\\text{MgO}\\)) is formed when \\(12\\text{ g}\\) of magnesium reacts completely with \\(8\\text{ g}\\) of oxygen?""",
     ["\\(16\\text{ g}\\)", "\\(20\\text{ g}\\)", "\\(24\\text{ g}\\)", "\\(28\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• Total mass = \\(12 + 8 = 20\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""Fill in the blank: The Law of Constant Proportion is also known as the Law of ________ Proportion.""",
     ["Definite", "Multiple", "Reciprocal", "Variable"],
     "A", "OFB", "easy",
     "• The Law of Constant Proportion is also termed the Law of Definite Proportions.\nCorrect Choice is (A)."),

    ("""Fill in the blank: French chemist Antoine Lavoisier showed that air is a mixture consisting mainly of nitrogen and ________.""",
     ["Hydrogen", "Oxygen", "Helium", "Chlorine"],
     "B", "OFB", "easy",
     "• Lavoisier identified oxygen and showed combustion consumes oxygen from air.\nCorrect Choice is (B)."),

    ("""What is the mass ratio of Magnesium to Oxygen in magnesium oxide (\\(\\text{MgO}\\))?""",
     ["\\(1 : 1\\)", "\\(3 : 2\\)", "\\(2 : 3\\)", "\\(4 : 3\\)"],
     "B", "OSC", "easy",
     "• In \\(\\text{MgO}\\), \\(\\text{Mg}=24\\text{ u}\\), \\(\\text{O}=16\\text{ u}\\). Ratio = \\(24 : 16 = 3 : 2\\).\nCorrect Choice is (B)."),

    ("""Which law states that the mass of a system remains strictly constant regardless of physical or chemical changes taking place inside a closed boundary?""",
     ["Law of Conservation of Mass", "Law of Gravitation", "Law of Inertia", "Charles's Law"],
     "A", "OSC", "easy",
     "• Law of Conservation of Mass.\nCorrect Choice is (A)."),

    ("""When \\(10\\text{ g}\\) of lead nitrate reacts with \\(10\\text{ g}\\) of potassium iodide in a closed flask, \\(20\\text{ g}\\) of products are obtained. This confirms the:""",
     ["Law of Multiple Proportions", "Law of Conservation of Mass", "Law of Gaseous Volumes", "Periodic Law"],
     "B", "OSC", "easy",
     "• Reactants \\(10 + 10 = 20\\text{ g}\\) equal products \\(20\\text{ g}\\), confirming conservation of mass.\nCorrect Choice is (B).")
]

# 12 Foundation Mock Questions (501-512) with rich embedded vector SVGs
foundation_data = [
    # 501: Conical Flask Experiment (Conservation of Mass)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="50" y="25" fill="#38bdf8" font-size="13" font-weight="bold">Verification of Law of Conservation of Mass</text>
  <!-- Balance Platform -->
  <rect x="30" y="165" width="280" height="15" fill="#334155" rx="3"/>
  <!-- Left Flask (Before mixing) -->
  <path d="M 60 165 L 75 110 L 80 85 L 90 85 L 95 110 L 110 165 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <rect x="80" y="80" width="10" height="6" fill="#f59e0b"/>
  <text x="55" y="195" fill="#94a3b8" font-size="10">Before Mixing</text>
  <text x="50" y="212" fill="#34d399" font-size="11" font-weight="bold">Mass: 154.30 g</text>
  <!-- Inverted Arrow -->
  <text x="160" y="125" fill="#38bdf8" font-size="18">→</text>
  <!-- Right Flask (After precipitation) -->
  <path d="M 210 165 L 225 110 L 230 85 L 240 85 L 245 110 L 260 165 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <rect x="230" y="80" width="10" height="6" fill="#f59e0b"/>
  <circle cx="235" cy="155" r="8" fill="#e2e8f0"/>
  <text x="205" y="195" fill="#94a3b8" font-size="10">After Mixing (Precipitate)</text>
  <text x="200" y="212" fill="#34d399" font-size="11" font-weight="bold">Mass: 154.30 g</text>
</svg>
</div>
In the conical flask experiment above, a small test tube containing barium chloride solution inside a corked flask of sodium sulphate is tipped over. A white precipitate forms, but the digital balance reading remains exactly \\(154.30\\text{ g}\\). Which scientific law does this outcome directly prove?""",
     ["Law of Constant Proportion",
      "Law of Conservation of Mass (Total mass of reactants equals total mass of products in a closed system)",
      "Law of Gaseous Volumes",
      "Law of Multiple Proportions"],
     "B", "OSC", "medium",
     "• Because the system is sealed, no matter enters or escapes. The digital balance reading of \\(154.30\\text{ g}\\) before and after precipitation proves the Law of Conservation of Mass.\nCorrect Choice is (B)."),

    # 502: Water Decomposition (1:8 Mass Ratio)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="80" y="25" fill="#38bdf8" font-size="13" font-weight="bold">Constant Mass Ratio in Water (H₂O)</text>
  <!-- Pie Chart or Bar representation -->
  <rect x="50" y="55" width="240" height="35" fill="#334155" rx="4"/>
  <!-- 1 part H -->
  <rect x="50" y="55" width="26.6" height="35" fill="#38bdf8" rx="2"/>
  <text x="52" y="77" fill="#0f172a" font-size="10" font-weight="bold">1g H</text>
  <!-- 8 parts O -->
  <rect x="76.6" y="55" width="213.4" height="35" fill="#ef4444" rx="2"/>
  <text x="160" y="77" fill="#fff" font-size="12" font-weight="bold">8g Oxygen (88.89%)</text>
  <!-- Formula -->
  <text x="65" y="125" fill="#cbd5e1" font-size="11">Total Mass of Water = 1g + 8g = 9g</text>
  <text x="65" y="150" fill="#fde047" font-size="11" font-weight="bold">Mass Ratio of Hydrogen : Oxygen = 1 : 8</text>
  <text x="65" y="180" fill="#94a3b8" font-size="10">True for rain, tap water, ocean, and laboratory synthesis</text>
</svg>
</div>
According to the mass distribution diagram of water (\\(\\text{H}_2\\text{O}\\)) shown above, if \\(72\\text{ g}\\) of pure water is completely decomposed into its constituent elements by electrolysis, what masses of hydrogen and oxygen gases will be collected?""",
     ["\\(9\\text{ g}\\) of hydrogen and \\(63\\text{ g}\\) of oxygen",
      "\\(8\\text{ g}\\) of hydrogen and \\(64\\text{ g}\\) of oxygen",
      "\\(4\\text{ g}\\) of hydrogen and \\(68\\text{ g}\\) of oxygen",
      "\\(36\\text{ g}\\) of hydrogen and \\(36\\text{ g}\\) of oxygen"],
     "B", "OSC", "hard",
     "• Mass of \\(\\text{H} = \\frac{1}{9} \\times 72 = 8\\text{ g}\\).\nMass of \\(\\text{O} = \\frac{8}{9} \\times 72 = 64\\text{ g}\\).\nRatio is \\(8 : 64 = 1 : 8\\).\nCorrect Choice is (B)."),

    # 503: Carbon Dioxide Formation (3:8 Mass Ratio)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="80" y="25" fill="#38bdf8" font-size="13" font-weight="bold">Carbon Dioxide (CO₂) Mass Composition</text>
  <!-- Carbon Box -->
  <rect x="40" y="60" width="70" height="50" fill="#475569" stroke="#94a3b8" rx="4"/>
  <text x="50" y="85" fill="#f8fafc" font-size="11" font-weight="bold">Carbon</text>
  <text x="55" y="100" fill="#fde047" font-size="10">3 parts</text>
  <!-- Plus sign -->
  <text x="125" y="90" fill="#cbd5e1" font-size="16" font-weight="bold">+</text>
  <!-- Oxygen Box -->
  <rect x="150" y="60" width="130" height="50" fill="#b91c1c" stroke="#ef4444" rx="4"/>
  <text x="180" y="85" fill="#f8fafc" font-size="11" font-weight="bold">Oxygen</text>
  <text x="185" y="100" fill="#fde047" font-size="10">8 parts</text>
  <!-- Result -->
  <text x="60" y="150" fill="#34d399" font-size="12" font-weight="bold">Carbon Dioxide (CO₂) = 11 parts by mass</text>
  <text x="60" y="180" fill="#cbd5e1" font-size="10">Burning 12g Carbon requires 32g Oxygen → 44g CO₂</text>
</svg>
</div>
Based on the mass composition diagram for carbon dioxide (\\(\\text{CO}_2\\)), if \\(9\\text{ g}\\) of carbon is burned in a combustion chamber containing \\(50\\text{ g}\\) of oxygen, how much \\(\\text{CO}_2\\) is produced and what mass of oxygen remains unreacted?""",
     ["\\(59\\text{ g}\\) of \\(\\text{CO}_2\\) with \\(0\\text{ g}\\) oxygen remaining",
      "\\(33\\text{ g}\\) of \\(\\text{CO}_2\\) with \\(26\\text{ g}\\) oxygen remaining unreacted",
      "\\(44\\text{ g}\\) of \\(\\text{CO}_2\\) with \\(15\\text{ g}\\) oxygen remaining unreacted",
      "\\(22\\text{ g}\\) of \\(\\text{CO}_2\\) with \\(37\\text{ g}\\) oxygen remaining unreacted"],
     "B", "OSC", "hard",
     "• Carbon combines with oxygen in \\(3 : 8\\) mass ratio. \\(9\\text{ g}\\) of carbon requires \\(9 \\times \\frac{8}{3} = 24\\text{ g}\\) of oxygen.\nMass of \\(\\text{CO}_2\\) formed = \\(9 + 24 = 33\\text{ g}\\).\nOxygen left unreacted = \\(50 - 24 = 26\\text{ g}\\).\nCorrect Choice is (B)."),

    # 504: Landolt's Tube Verification
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Landolt's Sealed H-Tube Experiment</text>
  <!-- H-Tube -->
  <path d="M 90 50 L 90 140 A 15 15 0 0 0 120 140 L 120 100 L 170 100 L 170 140 A 15 15 0 0 0 200 140 L 200 50" fill="none" stroke="#60a5fa" stroke-width="4"/>
  <!-- Solutions in both limbs -->
  <rect x="92" y="115" width="26" height="35" fill="#f59e0b" opacity="0.8"/>
  <text x="45" y="130" fill="#fde047" font-size="9">AgNO₃ sol.</text>
  <rect x="172" y="115" width="26" height="35" fill="#38bdf8" opacity="0.8"/>
  <text x="205" y="130" fill="#93c5fd" font-size="9">NaCl sol.</text>
  <!-- Seals -->
  <line x1="85" y1="50" x2="125" y2="50" stroke="#ef4444" stroke-width="3"/>
  <line x1="165" y1="50" x2="205" y2="50" stroke="#ef4444" stroke-width="3"/>
  <text x="135" y="45" fill="#ef4444" font-size="8">Hermetic Seals</text>
  <!-- Note -->
  <text x="40" y="180" fill="#cbd5e1" font-size="10">When inverted, white AgCl precipitate forms instantly.</text>
  <text x="40" y="200" fill="#34d399" font-size="10" font-weight="bold">Pre-mix mass = Post-mix mass (Error &lt; 0.0001%)</text>
</svg>
</div>
In Landolt's precision verification of the Law of Conservation of Mass shown above, solutions of silver nitrate (\\(\\text{AgNO}_3\\)) and sodium chloride (\\(\\text{NaCl}\\)) in sealed limbs of an H-tube are inverted to precipitate silver chloride (\\(\\text{AgCl}\\)). Why did Landolt use an H-shaped glass tube hermetically sealed at the top?""",
     ["To allow atmospheric oxygen to enter slowly during the reaction",
      "To prevent any escape of moisture vapor or gases and prevent absorption of atmospheric moisture, maintaining a strictly closed thermodynamic system",
      "To measure electrical resistance across both limbs",
      "To separate positive and negative magnetic poles"],
     "B", "OSC", "hard",
     "• Hermetic glass sealing ensures a completely closed physical system where no mass (including volatile moisture) can leave or enter, enabling ultra-precise mass verification.\nCorrect Choice is (B)."),

    # 505: Open Crucible vs Closed Flask Comparison
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="60" y="25" fill="#38bdf8" font-size="13" font-weight="bold">Thermal Decomposition of CaCO₃</text>
  <!-- Open System -->
  <rect x="30" y="55" width="125" height="100" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="40" y="75" fill="#f87171" font-size="10" font-weight="bold">A. Open Crucible</text>
  <text x="40" y="95" fill="#cbd5e1" font-size="9">100g CaCO₃ heated</text>
  <text x="40" y="115" fill="#ef4444" font-size="9">CO₂ gas escapes ↗</text>
  <text x="40" y="140" fill="#fca5a5" font-size="10" font-weight="bold">Residue = 56g CaO</text>
  <!-- Closed System -->
  <rect x="185" y="55" width="125" height="100" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="195" y="75" fill="#34d399" font-size="10" font-weight="bold">B. Sealed Retort</text>
  <text x="195" y="95" fill="#cbd5e1" font-size="9">100g CaCO₃ heated</text>
  <text x="195" y="115" fill="#10b981" font-size="9">CO₂ trapped inside</text>
  <text x="195" y="140" fill="#86efac" font-size="10" font-weight="bold">Total Mass = 100g</text>
  <text x="40" y="185" fill="#93c5fd" font-size="10">Apparent mass loss in A is strictly due to escaping gas</text>
</svg>
</div>
Comparing setups A and B in the decomposition diagram, why does the open crucible show an apparent loss of \\(44\\text{ g}\\) while the sealed retort maintains a constant mass of \\(100\\text{ g}\\)?""",
     ["Because heat destroys matter in open air",
      "Because 44g of carbon dioxide gas escaped into the atmosphere in setup A, whereas setup B conserved all products inside the closed boundary",
      "Because calcium oxide evaporates rapidly in closed systems",
      "Because the balance in setup A is inaccurate"],
     "B", "OSC", "medium",
     "• In the open container, \\(44\\text{ g}\\) of gaseous \\(\\text{CO}_2\\) escapes into the room. When all products are contained in a closed system, total mass is conserved at \\(100\\text{ g}\\).\nCorrect Choice is (B)."),

    # 506: Ammonia (NH3) 14:3 Mass Ratio
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="25" fill="#38bdf8" font-size="13" font-weight="bold">Ammonia (NH₃) Mass Composition</text>
  <!-- Bar Representation -->
  <rect x="40" y="60" width="260" height="40" fill="#334155" rx="4"/>
  <!-- Nitrogen 14/17 -->
  <rect x="40" y="60" width="214" height="40" fill="#6366f1" rx="2"/>
  <text x="90" y="85" fill="#fff" font-size="11" font-weight="bold">Nitrogen: 14 parts (82.35%)</text>
  <!-- Hydrogen 3/17 -->
  <rect x="254" y="60" width="46" height="40" fill="#38bdf8" rx="2"/>
  <text x="260" y="85" fill="#0f172a" font-size="10" font-weight="bold">3p H</text>
  <!-- Text -->
  <text x="45" y="130" fill="#cbd5e1" font-size="11">Total Mass of Ammonia = 14 + 3 = 17 units</text>
  <text x="45" y="155" fill="#fde047" font-size="11" font-weight="bold">Mass Ratio N : H = 14 : 3</text>
  <text x="45" y="185" fill="#94a3b8" font-size="10">28g Nitrogen reacts with 6g Hydrogen → 34g Ammonia</text>
</svg>
</div>
In the synthesis of ammonia (\\(\\text{NH}_3\\)) by Haber's process shown above, if \\(42\\text{ g}\\) of nitrogen gas is reacted with \\(15\\text{ g}\\) of hydrogen gas, what mass of ammonia gas is formed?""",
     ["\\(57\\text{ g}\\)", "\\(51\\text{ g}\\)", "\\(34\\text{ g}\\)", "\\(45\\text{ g}\\)"],
     "B", "OSC", "hard",
     "• Nitrogen and hydrogen combine in \\(14 : 3\\) mass ratio.\n\\(42\\text{ g}\\) of \\(\\text{N}_2\\) requires \\(42 \\times \\frac{3}{14} = 9\\text{ g}\\) of \\(\\text{H}_2\\).\nMass of ammonia formed = \\(42 + 9 = 51\\text{ g}\\).\n(Excess hydrogen = \\(15 - 9 = 6\\text{ g}\\)).\nCorrect Choice is (B)."),

    # 507: Proust's Copper Carbonate Analysis
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="25" fill="#38bdf8" font-size="13" font-weight="bold">Proust's Cupric Carbonate Discovery</text>
  <!-- Table Header -->
  <text x="30" y="58" fill="#94a3b8" font-size="10" font-weight="bold">Sample Source</text>
  <text x="135" y="58" fill="#38bdf8" font-size="10" font-weight="bold">% Copper</text>
  <text x="205" y="58" fill="#38bdf8" font-size="10" font-weight="bold">% Carbon</text>
  <text x="270" y="58" fill="#38bdf8" font-size="10" font-weight="bold">% Oxygen</text>
  <!-- Natural Sample -->
  <text x="30" y="85" fill="#10b981" font-size="10">Natural (Malachite)</text>
  <text x="140" y="85" fill="#cbd5e1" font-size="10">51.35%</text>
  <text x="210" y="85" fill="#cbd5e1" font-size="10">9.74%</text>
  <text x="275" y="85" fill="#cbd5e1" font-size="10">38.91%</text>
  <!-- Synthetic Sample -->
  <text x="30" y="115" fill="#f59e0b" font-size="10">Synthetic (Lab)</text>
  <text x="140" y="115" fill="#cbd5e1" font-size="10">51.35%</text>
  <text x="210" y="115" fill="#cbd5e1" font-size="10">9.74%</text>
  <text x="275" y="115" fill="#cbd5e1" font-size="10">38.91%</text>
  <line x1="30" y1="130" x2="315" y2="130" stroke="#475569" stroke-width="1"/>
  <text x="35" y="160" fill="#fde047" font-size="11" font-weight="bold">Elemental percentages are IDENTICAL</text>
  <text x="35" y="185" fill="#93c5fd" font-size="10">Definite proportions regardless of natural or artificial origin</text>
</svg>
</div>
What monumental conclusion did Joseph Louis Proust deduce from the analytical data shown in the table above?""",
     ["That natural minerals contain special vital force absent in laboratory chemicals",
      "That a pure chemical compound always contains elements in fixed, definite proportions by weight, regardless of whether it was mined from nature or synthesized in a laboratory",
      "That laboratory chemicals are always impure",
      "That copper carbonate has no definite formula"],
     "B", "OSC", "medium",
     "• The identical percentage compositions of natural and synthetic copper carbonate demonstrated that chemical compounds have invariable elemental weight ratios.\nCorrect Choice is (B)."),

    # 508: Dalton's Postulates Linking Both Laws
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Dalton's Theoretical Bridge</text>
  <!-- Law 1 Box -->
  <rect x="25" y="50" width="135" height="70" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="70" fill="#34d399" font-size="10" font-weight="bold">Conservation of Mass</text>
  <text x="35" y="90" fill="#cbd5e1" font-size="8">Atoms cannot be created</text>
  <text x="35" y="105" fill="#cbd5e1" font-size="8">or destroyed in reactions</text>
  <!-- Law 2 Box -->
  <rect x="180" y="50" width="135" height="70" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="190" y="70" fill="#fde047" font-size="10" font-weight="bold">Constant Proportion</text>
  <text x="190" y="90" fill="#cbd5e1" font-size="8">Atoms combine in fixed</text>
  <text x="190" y="105" fill="#cbd5e1" font-size="8">whole-number ratios</text>
  <!-- Unifying Core -->
  <rect x="70" y="145" width="200" height="45" fill="#334155" stroke="#38bdf8" stroke-width="2" rx="4"/>
  <text x="95" y="172" fill="#38bdf8" font-size="12" font-weight="bold">Dalton's Atomic Theory (1808)</text>
</svg>
</div>
How did Dalton's atomic theory conceptually harmonize the empirical laws of Lavoisier and Proust?""",
     ["By proposing that atoms change into light during reactions",
      "By proposing that chemical reactions merely rearrange indivisible, indestructible atoms possessing fixed element-specific masses into fixed numerical combinations",
      "By claiming that atoms do not have any mass",
      "By stating that mass can be converted to electrical charge at will"],
     "B", "OSC", "hard",
     "• Dalton explained that atoms are indestructible (explaining mass conservation) and combine in fixed integer ratios of unchanging atomic weights (explaining constant proportion).\nCorrect Choice is (B)."),

    # 509: Combustion of Methane (Mass Balance Equation)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="25" fill="#38bdf8" font-size="13" font-weight="bold">Mass Balance: Methane Combustion</text>
  <text x="35" y="65" fill="#cbd5e1" font-size="12" font-family="monospace">CH₄  +  2 O₂  ⟶  CO₂  +  2 H₂O</text>
  <!-- Reactants Mass -->
  <rect x="30" y="85" width="125" height="45" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="40" y="105" fill="#93c5fd" font-size="10">Reactants:</text>
  <text x="40" y="120" fill="#38bdf8" font-size="11" font-weight="bold">16g + 64g = 80g</text>
  <!-- Equals -->
  <text x="165" y="112" fill="#cbd5e1" font-size="16" font-weight="bold">=</text>
  <!-- Products Mass -->
  <rect x="185" y="85" width="125" height="45" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="195" y="105" fill="#86efac" font-size="10">Products:</text>
  <text x="195" y="120" fill="#10b981" font-size="11" font-weight="bold">44g + 36g = 80g</text>
  <text x="50" y="165" fill="#fde047" font-size="11" font-weight="bold">Total Reactant Mass (80g) = Total Product Mass (80g)</text>
</svg>
</div>
In the combustion reaction \\(\\text{CH}_4 + 2\\text{O}_2 \\to \\text{CO}_2 + 2\\text{H}_2\\text{O}\\) shown above, if \\(32\\text{ g}\\) of methane is burned completely with excess oxygen, what total combined mass of products (carbon dioxide + water vapor) will be formed?""",
     ["\\(80\\text{ g}\\)", "\\(128\\text{ g}\\)", "\\(160\\text{ g}\\)", "\\(64\\text{ g}\\)"],
     "C", "OSC", "hard",
     "• In the stoichiometric reaction, \\(16\\text{ g}\\) of \\(\\text{CH}_4\\) reacts with \\(64\\text{ g}\\) of \\(\\text{O}_2\\) to form \\(80\\text{ g}\\) of total products.\nFor \\(32\\text{ g}\\) of \\(\\text{CH}_4\\) (double quantity), total product mass = \\(2 \\times 80 = 160\\text{ g}\\) (comprising \\(88\\text{ g}\\) \\(\\text{CO}_2\\) + \\(72\\text{ g}\\) \\(\\text{H}_2\\text{O}\\)).\nCorrect Choice is (C)."),

    # 510: Hydrogen Peroxide vs Water (Multiple Proportions Foundation)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="70" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Water vs Hydrogen Peroxide Ratios</text>
  <!-- Water H2O -->
  <rect x="35" y="50" width="270" height="45" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="45" y="70" fill="#38bdf8" font-size="11" font-weight="bold">Water (H₂O):</text>
  <text x="45" y="85" fill="#cbd5e1" font-size="10">2g Hydrogen combines with 16g Oxygen → Ratio 1 : 8</text>
  <!-- Hydrogen Peroxide H2O2 -->
  <rect x="35" y="110" width="270" height="45" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="45" y="130" fill="#f59e0b" font-size="11" font-weight="bold">Hydrogen Peroxide (H₂O₂):</text>
  <text x="45" y="145" fill="#cbd5e1" font-size="10">2g Hydrogen combines with 32g Oxygen → Ratio 1 : 16</text>
  <text x="45" y="185" fill="#fde047" font-size="10">Oxygen masses combining with fixed 1g H bear simple ratio 8 : 16 = 1 : 2</text>
</svg>
</div>
Comparing water and hydrogen peroxide in the schematic above, for a fixed mass of \\(1\\text{ g}\\) of hydrogen, what is the ratio of masses of oxygen that combine to form water versus hydrogen peroxide?""",
     ["\\(1 : 1\\)", "\\(1 : 2\\)", "\\(1 : 8\\)", "\\(2 : 3\\)"],
     "B", "OSC", "medium",
     "• In \\(\\text{H}_2\\text{O}\\), \\(1\\text{ g}\\) of H combines with \\(8\\text{ g}\\) of O. In \\(\\text{H}_2\\text{O}_2\\), \\(1\\text{ g}\\) of H combines with \\(16\\text{ g}\\) of O. The ratio of oxygen masses is \\(8 : 16 = 1 : 2\\).\nCorrect Choice is (B)."),

    # 511: Landolt Experiment Precision Data Analysis
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="25" fill="#38bdf8" font-size="13" font-weight="bold">Landolt's Analytical Balance Record</text>
  <!-- Table representation -->
  <rect x="30" y="45" width="280" height="110" fill="#1e293b" stroke="#475569" rx="4"/>
  <text x="40" y="70" fill="#94a3b8" font-size="10">Initial System Mass (m₁):</text>
  <text x="210" y="70" fill="#38bdf8" font-size="10" font-family="monospace">243.6812 g</text>
  <text x="40" y="95" fill="#94a3b8" font-size="10">Final Mass after Reaction (m₂):</text>
  <text x="210" y="95" fill="#38bdf8" font-size="10" font-family="monospace">243.6811 g</text>
  <text x="40" y="120" fill="#fde047" font-size="10">Difference (Δm):</text>
  <text x="210" y="120" fill="#10b981" font-size="10" font-family="monospace">-0.0001 g (&lt; 0.00005%)</text>
  <text x="40" y="145" fill="#93c5fd" font-size="9">Difference is within experimental balance measurement error</text>
  <text x="40" y="185" fill="#34d399" font-size="10" font-weight="bold">Conclusion: Mass remains invariant during chemical change</text>
</svg>
</div>
The recorded balance data shows a minuscule mass variation of \\(0.0001\\text{ g}\\) (less than \\(0.00005\\%\\)) across a vigorous precipitation reaction. How do modern scientists interpret this result?""",
     ["Chemical energy was created from mass",
      "Mass is strictly conserved; the minute \\(0.0001\\text{ g}\\) difference is within the limits of experimental measurement error of the analytical balance",
      "One hundredth of a gram of silver evaporated through glass",
      "Gravity changed during the experiment"],
     "B", "OSC", "medium",
     "• In chemical reactions, mass conservation holds true to extraordinary precision; fractional differences at the limit of sensitivity reflect balance tolerance rather than loss of matter.\nCorrect Choice is (B)."),

    # 512: Law of Definite Proportions in Glucose
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="70" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Mass Breakdown of Glucose (C₆H₁₂O₆)</text>
  <!-- Carbon bar -->
  <rect x="40" y="55" width="260" height="30" fill="#334155" rx="3"/>
  <rect x="40" y="55" width="104" height="30" fill="#475569" rx="2"/>
  <text x="50" y="75" fill="#fff" font-size="10" font-weight="bold">Carbon: 72u (40.0%)</text>
  <!-- Hydrogen bar -->
  <rect x="144" y="55" width="17" height="30" fill="#38bdf8" rx="2"/>
  <text x="146" y="75" fill="#0f172a" font-size="9" font-weight="bold">H</text>
  <!-- Oxygen bar -->
  <rect x="161" y="55" width="139" height="30" fill="#ef4444" rx="2"/>
  <text x="195" y="75" fill="#fff" font-size="10" font-weight="bold">Oxygen: 96u (53.3%)</text>
  <text x="45" y="115" fill="#cbd5e1" font-size="10">Molar Mass = (6×12) + (12×1) + (6×16) = 180 g/mol</text>
  <text x="45" y="140" fill="#fde047" font-size="11" font-weight="bold">Mass Ratio C : H : O = 72 : 12 : 96 = 6 : 1 : 8</text>
  <text x="45" y="170" fill="#93c5fd" font-size="9">In 180g of glucose, there are strictly 72g C, 12g H, and 96g O</text>
</svg>
</div>
According to the mass breakdown of glucose (\\(\\text{C}_6\\text{H}_{12}\\text{O}_6\\)) shown above, what is the simplified constant mass ratio of Carbon to Hydrogen to Oxygen in pure glucose?""",
     ["\\(1 : 2 : 1\\)", "\\(6 : 1 : 8\\)", "\\(12 : 1 : 16\\)", "\\(3 : 1 : 4\\)"],
     "B", "OSC", "hard",
     "• Mass of C = \\(72\\text{ u}\\), H = \\(12\\text{ u}\\), O = \\(96\\text{ u}\\). Dividing each by 12 gives the simplified constant mass ratio \\(6 : 1 : 8\\).\nCorrect Choice is (B).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-4-4.1-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-4-4.1-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-4-4.1-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch4_topic1.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
