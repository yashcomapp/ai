# scripts/generate_topic4_3.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-4-4.3"
CHAPTER_NUM = 4

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: Mole concept definition and Avogadro number
    ("""What is the fundamental SI unit for the amount of substance?""",
     ["Kilogram (\\(\\text{kg}\\))", "Mole (\\(\\text{mol}\\))", "Candela (\\(\\text{cd}\\))", "Ampere (\\(\\text{A}\\))"],
     "B", "OSC", "easy",
     "• In the International System of Units (SI), the mole (symbol: mol) is the unit of amount of substance.\nCorrect Choice is (B)."),

    ("""What is the universally accepted value of Avogadro's constant (\\(N_A\\))?""",
     ["\\(6.022 \\times 10^{20}\\text{ mol}^{-1}\\)",
      "\\(6.022 \\times 10^{23}\\text{ mol}^{-1}\\)",
      "\\(1.6605 \\times 10^{-24}\\text{ mol}^{-1}\\)",
      "\\(9.109 \\times 10^{28}\\text{ mol}^{-1}\\)"],
     "B", "OSC", "easy",
     "• Avogadro's constant \\(N_A = 6.022 \\times 10^{23}\\text{ entities per mole}\\).\nCorrect Choice is (B)."),

    ("""One mole of any chemical substance contains exactly how many elementary entities (atoms, molecules, or ions)?""",
     ["\\(1000\\)", "\\(10^6\\)", "\\(6.022 \\times 10^{23}\\)", "\\(1.66 \\times 10^{-19}\\)"],
     "C", "OSC", "easy",
     "• By definition, 1 mole contains Avogadro's number of particles: \\(6.022 \\times 10^{23}\\).\nCorrect Choice is (C)."),

    ("""The mole was originally defined as the number of atoms present in exactly:""",
     ["\\(1\\text{ g}\\) of Hydrogen-1",
      "\\(12\\text{ g}\\) of Carbon-12 (\\(^{12}\\text{C}\\))",
      "\\(16\\text{ g}\\) of Oxygen-16",
      "\\(23\\text{ g}\\) of Sodium"],
     "B", "OSC", "easy",
     "• One mole corresponds to the number of atoms in exactly \\(12\\text{ g}\\) (or \\(0.012\\text{ kg}\\)) of pure Carbon-12.\nCorrect Choice is (B)."),

    ("""What is the mass in grams of \\(1\\text{ mole}\\) of pure water (\\(\\text{H}_2\\text{O}\\))?""",
     ["\\(9\\text{ g}\\)", "\\(18\\text{ g}\\)", "\\(20\\text{ g}\\)", "\\(36\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• Molar mass of \\(\\text{H}_2\\text{O} = (2 \\times 1) + 16 = 18\\text{ g/mol}\\).\nCorrect Choice is (B)."),

    ("""What is the mass of \\(1\\text{ mole}\\) of carbon dioxide (\\(\\text{CO}_2\\))?""",
     ["\\(28\\text{ g}\\)", "\\(32\\text{ g}\\)", "\\(44\\text{ g}\\)", "\\(56\\text{ g}\\)"],
     "C", "OSC", "easy",
     "• Molar mass of \\(\\text{CO}_2 = 12 + (2 \\times 16) = 44\\text{ g/mol}\\).\nCorrect Choice is (C)."),

    ("""What is the mathematical formula used to calculate the number of moles (\\(n\\)) from a given mass (\\(m\\))?""",
     ["\\(n = m \\times M\\)",
      "\\(n = \\frac{m}{M}\\) (where \\(M\\) is the molar mass)",
      "\\(n = \\frac{M}{m}\\)",
      "\\(n = m + M\\)"],
     "B", "OSC", "easy",
     "• Number of moles \\(n = \\frac{\\text{mass in grams } (m)}{\\text{molar mass } (M)}\\).\nCorrect Choice is (B)."),

    ("""How many moles are present in \\(52\\text{ g}\\) of Helium gas (\\(\\text{He}\\), atomic mass \\(4\\text{ u}\\))?""",
     ["\\(4\\text{ moles}\\)", "\\(13\\text{ moles}\\)", "\\(26\\text{ moles}\\)", "\\(52\\text{ moles}\\)"],
     "B", "OSC", "easy",
     "• Number of moles \\(n = \\frac{52}{4} = 13\\text{ moles}\\).\nCorrect Choice is (B)."),

    ("""What is the mass in grams of \\(0.5\\text{ moles}\\) of Nitrogen gas (\\(\\text{N}_2\\))? (Given atomic mass \\(\\text{N} = 14\\text{ u}\\))""",
     ["\\(7\\text{ g}\\)", "\\(14\\text{ g}\\)", "\\(28\\text{ g}\\)", "\\(56\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• Molar mass of \\(\\text{N}_2 = 2 \\times 14 = 28\\text{ g/mol}\\).\nMass \\(m = n \\times M = 0.5 \\times 28 = 14\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""How many molecules are present in \\(36\\text{ g}\\) of pure water (\\(\\text{H}_2\\text{O}\\))?""",
     ["\\(6.022 \\times 10^{23}\\)",
      "\\(1.2044 \\times 10^{24}\\) (which is \\(2 \\times N_A\\))",
      "\\(3.011 \\times 10^{23}\\)",
      "\\(18 \\times 10^{23}\\)"],
     "B", "OSC", "medium",
     "• Number of moles \\(n = \\frac{36}{18} = 2\\text{ moles}\\).\nTotal molecules \\(N = 2 \\times 6.022 \\times 10^{23} = 1.2044 \\times 10^{24}\\).\nCorrect Choice is (B)."),

    # 11-20: Molar volume at STP, particle counts
    ("""What volume is occupied by \\(1\\text{ mole}\\) of any ideal gas at Standard Temperature and Pressure (STP: \\(0^\\circ\\text{C}, 1\\text{ atm}\\))?""",
     ["\\(1.0\\text{ litre}\\)", "\\(11.2\\text{ litres}\\)", "\\(22.4\\text{ litres} (\\text{dm}^3)\\)", "\\(44.8\\text{ litres}\\)"],
     "C", "OSC", "easy",
     "• At STP, 1 mole of any ideal gas occupies a standard molar volume of \\(22.4\\text{ L}\\) (or \\(22.4\\text{ dm}^3\\)).\nCorrect Choice is (C)."),

    ("""What volume at STP is occupied by \\(44\\text{ g}\\) of Carbon Dioxide gas (\\(\\text{CO}_2\\))?""",
     ["\\(11.2\\text{ L}\\)", "\\(22.4\\text{ L}\\)", "\\(44.8\\text{ L}\\)", "\\(88.0\\text{ L}\\)"],
     "B", "OSC", "easy",
     "• \\(44\\text{ g}\\) of \\(\\text{CO}_2\\) is exactly \\(1\\text{ mole}\\), which occupies \\(22.4\\text{ L}\\) at STP.\nCorrect Choice is (B)."),

    ("""What volume at STP is occupied by \\(0.5\\text{ moles}\\) of Oxygen gas (\\(\\text{O}_2\\))?""",
     ["\\(5.6\\text{ L}\\)", "\\(11.2\\text{ L}\\)", "\\(22.4\\text{ L}\\)", "\\(44.8\\text{ L}\\)"],
     "B", "OSC", "easy",
     "• Volume = \\(0.5 \\times 22.4 = 11.2\\text{ litres}\\).\nCorrect Choice is (B)."),

    ("""How many total ATOMS are present in \\(1\\text{ mole}\\) of water molecules (\\(\\text{H}_2\\text{O}\\))?""",
     ["\\(6.022 \\times 10^{23}\\text{ atoms}\\)",
      "\\(1.2044 \\times 10^{24}\\text{ atoms}\\)",
      "\\(1.8066 \\times 10^{24}\\text{ atoms} (3 \\times N_A)\\)",
      "\\(3.613 \\times 10^{24}\\text{ atoms}\\)"],
     "C", "OSC", "medium",
     "• Each \\(\\text{H}_2\\text{O}\\) molecule contains 3 atoms (2 H + 1 O). Total atoms = \\(3 \\times 6.022 \\times 10^{23} = 1.8066 \\times 10^{24}\\).\nCorrect Choice is (C)."),

    ("""How many moles of Oxygen atoms are present in \\(1\\text{ mole}\\) of Sulphuric Acid (\\(\\text{H}_2\\text{SO}_4\\))?""",
     ["\\(1\\text{ mole}\\)", "\\(2\\text{ moles}\\)", "\\(4\\text{ moles}\\)", "\\(7\\text{ moles}\\)"],
     "C", "OSC", "easy",
     "• The chemical formula \\(\\text{H}_2\\text{SO}_4\\) shows that 1 formula unit contains 4 oxygen atoms; hence 1 mole contains 4 moles of O atoms.\nCorrect Choice is (C)."),

    ("""What is the mass of \\(3.011 \\times 10^{23}\\) atoms of Carbon?""",
     ["\\(3\\text{ g}\\)", "\\(6\\text{ g}\\)", "\\(12\\text{ g}\\)", "\\(24\\text{ g}\\)"],
     "B", "OSC", "medium",
     "• Number of moles \\(n = \\frac{3.011 \\times 10^{23}}{6.022 \\times 10^{23}} = 0.5\\text{ moles}\\).\nMass \\(m = 0.5 \\times 12 = 6\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""How many moles are present in \\(100\\text{ g}\\) of Calcium Carbonate (\\(\\text{CaCO}_3\\))? (Molar mass = \\(100\\text{ g/mol}\\))""",
     ["\\(0.1\\text{ mole}\\)", "\\(1\\text{ mole}\\)", "\\(10\\text{ moles}\\)", "\\(100\\text{ moles}\\)"],
     "B", "OSC", "easy",
     "• \\(n = \\frac{100}{100} = 1\\text{ mole}\\).\nCorrect Choice is (B)."),

    ("""Which of the following samples contains the GREATEST number of molecules?""",
     ["\\(1\\text{ g}\\) of \\(\\text{H}_2\\) (molar mass \\(2\\text{ g/mol}\\))",
      "\\(1\\text{ g}\\) of \\(\\text{O}_2\\) (molar mass \\(32\\text{ g/mol}\\))",
      "\\(1\\text{ g}\\) of \\(\\text{N}_2\\) (molar mass \\(28\\text{ g/mol}\\))",
      "\\(1\\text{ g}\\) of \\(\\text{CH}_4\\) (molar mass \\(16\\text{ g/mol}\\))"],
     "A", "OSC", "hard",
     "• Number of molecules is proportional to moles \\(n = m/M\\). For \\(1\\text{ g}\\), smaller molar mass gives more moles: \\(n(\\text{H}_2) = \\frac{1}{2} = 0.5\\text{ mol}\\), which is greater than all others.\nCorrect Choice is (A)."),

    ("""How many moles are present in \\(12.044 \\times 10^{23}\\) atoms of Iron?""",
     ["\\(1\\text{ mole}\\)", "\\(2\\text{ moles}\\)", "\\(3\\text{ moles}\\)", "\\(4\\text{ moles}\\)"],
     "B", "OSC", "easy",
     "• \\(n = \\frac{12.044 \\times 10^{23}}{6.022 \\times 10^{23}} = 2\\text{ moles}\\).\nCorrect Choice is (B)."),

    ("""What is the mass in grams of a single molecule of water (\\(\\text{H}_2\\text{O}\\))?""",
     ["\\(18\\text{ g}\\)",
      "\\(2.99 \\times 10^{-23}\\text{ g}\\)",
      "\\(1.66 \\times 10^{-24}\\text{ g}\\)",
      "\\(6.022 \\times 10^{-23}\\text{ g}\\)"],
     "B", "OSC", "medium",
     "• Mass of 1 molecule = \\(\\frac{\\text{Molar mass}}{N_A} = \\frac{18\\text{ g}}{6.022 \\times 10^{23}} \\approx 2.989 \\times 10^{-23}\\text{ g}\\).\nCorrect Choice is (B)."),

    # 21-30: Stoichiometry and mole relationships
    ("""In the chemical reaction \\(2\\text{H}_2 + \\text{O}_2 \\to 2\\text{H}_2\\text{O}\\), how many moles of water are produced from \\(4\\text{ moles}\\) of hydrogen gas reacting with excess oxygen?""",
     ["\\(2\\text{ moles}\\)", "\\(4\\text{ moles}\\)", "\\(6\\text{ moles}\\)", "\\(8\\text{ moles}\\)"],
     "B", "OSC", "easy",
     "• By reaction stoichiometry, 2 moles of \\(\\text{H}_2\\) produce 2 moles of \\(\\text{H}_2\\text{O}\\) (\\(1:1\\) mole ratio). Therefore, 4 moles of \\(\\text{H}_2\\) yield 4 moles of \\(\\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    ("""What is the mass of \\(0.2\\text{ moles}\\) of Glucose (\\(\\text{C}_6\\text{H}_{12}\\text{O}_6\\), molar mass \\(180\\text{ g/mol}\\))?""",
     ["\\(18\\text{ g}\\)", "\\(36\\text{ g}\\)", "\\(72\\text{ g}\\)", "\\(90\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• Mass = \\(0.2 \\times 180 = 36\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""Assertion (A): One mole of \\(\\text{O}_2\\) gas and one mole of \\(\\text{CO}_2\\) gas occupy the exact same volume at STP (\\(22.4\\text{ L}\\)).\nReason (R): According to Avogadro's hypothesis, equal volumes of all gases under identical temperature and pressure contain equal numbers of molecules.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "• Both statements are correct, and Avogadro's Law explains why 1 mole of any gas occupies \\(22.4\\text{ L}\\) at STP.\nCorrect Choice is (A)."),

    ("""Assertion (A): One mole of Hydrogen gas (\\(\\text{H}_2\\)) weighs \\(2\\text{ g}\\), whereas one mole of Oxygen gas (\\(\\text{O}_2\\)) weighs \\(32\\text{ g}\\).\nReason (R): An oxygen molecule contains more protons and neutrons than a hydrogen molecule, giving it a higher molecular mass while both contain \\(6.022 \\times 10^{23}\\) molecules.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "• A mole is a fixed particle count (\\(N_A\\)); mass varies proportionally with molecular mass.\nCorrect Choice is (A)."),

    ("""State True or False: One mole of Sodium Chloride (\\(\\text{NaCl}\\)) contains \\(6.022 \\times 10^{23}\\) Sodium ions (\\(\\text{Na}^+\\)) and \\(6.022 \\times 10^{23}\\) Chloride ions (\\(\\text{Cl}^-\\)).""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. 1 mole of NaCl formula units dissociates into 1 mole of \\(\\text{Na}^+\\) ions and 1 mole of \\(\\text{Cl}^-\\) ions.\nCorrect Choice is (A)."),

    ("""State True or False: 1 mole of liquid water occupies 22.4 litres at room temperature.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. The \\(22.4\\text{ L}\\) molar volume applies strictly to GASES at STP. One mole of liquid water has mass \\(18\\text{ g}\\) and occupies only about \\(18\\text{ mL}\\) (\\(0.018\\text{ L}\\)).\nCorrect Choice is (B)."),

    ("""How many moles are present in \\(90\\text{ g}\\) of pure water?""",
     ["\\(2.5\\text{ moles}\\)", "\\(5.0\\text{ moles}\\)", "\\(10.0\\text{ moles}\\)", "\\(18.0\\text{ moles}\\)"],
     "B", "OSC", "easy",
     "• \\(n = \\frac{90}{18} = 5\\text{ moles}\\).\nCorrect Choice is (B)."),

    ("""What is the mass of \\(2.5\\text{ moles}\\) of Calcium Oxide (\\(\\text{CaO}\\), molar mass \\(56\\text{ g/mol}\\))?""",
     ["\\(112\\text{ g}\\)", "\\(140\\text{ g}\\)", "\\(168\\text{ g}\\)", "\\(224\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• Mass = \\(2.5 \\times 56 = 140\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""How many moles of gas molecules are present in \\(5.6\\text{ litres}\\) of Nitrogen gas at STP?""",
     ["\\(0.25\\text{ moles}\\)", "\\(0.5\\text{ moles}\\)", "\\(1.0\\text{ mole}\\)", "\\(2.0\\text{ moles}\\)"],
     "A", "OSC", "medium",
     "• Moles \\(n = \\frac{V}{22.4} = \\frac{5.6}{22.4} = 0.25\\text{ moles}\\).\nCorrect Choice is (A)."),

    ("""How many moles of atoms are contained in \\(16\\text{ g}\\) of Ozone gas (\\(\\text{O}_3\\))?""",
     ["\\(0.33\\text{ moles}\\)", "\\(0.5\\text{ moles}\\)", "\\(1.0\\text{ mole}\\)", "\\(3.0\\text{ moles}\\)"],
     "C", "OSC", "hard",
     "• Mass of oxygen atoms is \\(16\\text{ g}\\). Since atomic mass of O is \\(16\\text{ g/mol}\\), \\(n(\\text{O atoms}) = \\frac{16}{16} = 1.0\\text{ mole}\\) (or \\(\\frac{16}{48} = \\frac{1}{3}\\text{ mol}\\) \\(\\text{O}_3 \\times 3 = 1\\text{ mol}\\) atoms).\nCorrect Choice is (C)."),

    # 31-40: Fill in blanks and applied calculations
    ("""Fill in the blank: The number \\(6.022 \\times 10^{23}\\) is named the ________ Constant in honor of an Italian scientist.""",
     ["Dalton", "Avogadro", "Lavoisier", "Rutherford"],
     "B", "OFB", "easy",
     "• Avogadro's constant \\(N_A\\).\nCorrect Choice is (B)."),

    ("""Fill in the blank: The mass of one mole of a substance expressed in grams is called its ________ mass.""",
     ["Atomic", "Molar", "Isotopic", "Equivalent"],
     "B", "OFB", "easy",
     "• Molar mass (in g/mol).\nCorrect Choice is (B)."),

    ("""Fill in the blank: At STP, \\(11.2\\text{ litres}\\) of any gas contains ________ moles of molecules.""",
     ["\\(0.25\\)", "\\(0.5\\)", "\\(1.0\\)", "\\(2.0\\)"],
     "B", "OFB", "easy",
     "• \\(\\frac{11.2}{22.4} = 0.5\\text{ moles}\\).\nCorrect Choice is (B)."),

    ("""What is the mass of \\(0.1\\text{ moles}\\) of Sodium Carbonate (\\(\\text{Na}_2\\text{CO}_3\\))? (Molar mass = \\(106\\text{ g/mol}\\))""",
     ["\\(5.3\\text{ g}\\)", "\\(10.6\\text{ g}\\)", "\\(21.2\\text{ g}\\)", "\\(106\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• Mass = \\(0.1 \\times 106 = 10.6\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""How many moles of hydrogen atoms are present in \\(3\\text{ moles}\\) of methane (\\(\\text{CH}_4\\))?""",
     ["\\(3\\text{ moles}\\)", "\\(4\\text{ moles}\\)", "\\(12\\text{ moles}\\)", "\\(16\\text{ moles}\\)"],
     "C", "OSC", "easy",
     "• In 1 mole of \\(\\text{CH}_4\\) there are 4 moles of H atoms. In 3 moles, \\(3 \\times 4 = 12\\text{ moles}\\) of H atoms.\nCorrect Choice is (C)."),

    ("""What is the volume occupied by \\(14\\text{ g}\\) of Carbon Monoxide gas (\\(\\text{CO}\\)) at STP? (Molar mass = \\(28\\text{ g/mol}\\))""",
     ["\\(5.6\\text{ L}\\)", "\\(11.2\\text{ L}\\)", "\\(22.4\\text{ L}\\)", "\\(44.8\\text{ L}\\)"],
     "B", "OSC", "medium",
     "• Moles \\(n = \\frac{14}{28} = 0.5\\text{ mol}\\). Volume at STP = \\(0.5 \\times 22.4 = 11.2\\text{ L}\\).\nCorrect Choice is (B)."),

    ("""A flask contains \\(8\\text{ g}\\) of methane (\\(\\text{CH}_4\\)) and \\(22\\text{ g}\\) of carbon dioxide (\\(\\text{CO}_2\\)). What is the total number of moles of gas present?""",
     ["\\(0.5\\text{ moles}\\)", "\\(1.0\\text{ mole}\\)", "\\(1.5\\text{ moles}\\)", "\\(2.0\\text{ moles}\\)"],
     "B", "OSC", "hard",
     "• Moles of \\(\\text{CH}_4 = \\frac{8}{16} = 0.5\\text{ mol}\\).\nMoles of \\(\\text{CO}_2 = \\frac{22}{44} = 0.5\\text{ mol}\\).\nTotal moles = \\(0.5 + 0.5 = 1.0\\text{ mole}\\).\nCorrect Choice is (B)."),

    ("""Which sample has the least mass in grams?""",
     ["\\(1\\text{ mole of }\\text{H}_2\\text{O}\\)",
      "\\(1\\text{ mole of }\\text{N}_2\\)",
      "\\(1\\text{ mole of }\\text{He}\\)",
      "\\(1\\text{ mole of }\\text{O}_2\\)"],
     "C", "OSC", "easy",
     "• Molar masses: \\(\\text{H}_2\\text{O}=18\\text{ g}\\), \\(\\text{N}_2=28\\text{ g}\\), \\(\\text{He}=4\\text{ g}\\), \\(\\text{O}_2=32\\text{ g}\\). Helium has the least mass.\nCorrect Choice is (C)."),

    ("""How many total electrons are present in \\(1\\text{ mole}\\) of Hydrogen atoms?""",
     ["\\(1\\)", "\\(6.022 \\times 10^{23}\\)", "\\(1.2044 \\times 10^{24}\\)", "\\(1837\\)"],
     "B", "OSC", "easy",
     "• Each H atom has 1 electron, so 1 mole of H atoms contains \\(1 \\times 6.022 \\times 10^{23} = 6.022 \\times 10^{23}\\) electrons.\nCorrect Choice is (B)."),

    ("""How many moles are in \\(3.4\\text{ g}\\) of Ammonia (\\(\\text{NH}_3\\))? (Molar mass = \\(17\\text{ g/mol}\\))""",
     ["\\(0.1\\text{ mole}\\)", "\\(0.2\\text{ mole}\\)", "\\(0.5\\text{ mole}\\)", "\\(2.0\\text{ moles}\\)"],
     "B", "OSC", "easy",
     "• \\(n = \\frac{3.4}{17} = 0.2\\text{ mole}\\).\nCorrect Choice is (B).")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("""What is the value of Avogadro number?""",
     ["\\(6.022 \\times 10^{23}\\)", "\\(6.022 \\times 10^{20}\\)", "\\(3.011 \\times 10^{23}\\)", "\\(1.66 \\times 10^{-27}\\)"],
     "A", "OSC", "easy",
     "• \\(N_A = 6.022 \\times 10^{23}\\).\nCorrect Choice is (A)."),

    ("""What is the mass of \\(1\\text{ mole}\\) of oxygen atoms (\\(\\text{O}\\))?""",
     ["\\(8\\text{ g}\\)", "\\(16\\text{ g}\\)", "\\(32\\text{ g}\\)", "\\(64\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• Mass of 1 mole of O atoms is \\(16\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""What is the mass of \\(1\\text{ mole}\\) of oxygen gas molecules (\\(\\text{O}_2\\))?""",
     ["\\(16\\text{ g}\\)", "\\(32\\text{ g}\\)", "\\(64\\text{ g}\\)", "\\(8\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• Mass of 1 mole of \\(\\text{O}_2\\) is \\(32\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""How many moles are in \\(64\\text{ g}\\) of Oxygen gas (\\(\\text{O}_2\\))?""",
     ["\\(1\\text{ mole}\\)", "\\(2\\text{ moles}\\)", "\\(4\\text{ moles}\\)", "\\(8\\text{ moles}\\)"],
     "B", "OSC", "easy",
     "• \\(n = \\frac{64}{32} = 2\\text{ moles}\\).\nCorrect Choice is (B)."),

    ("""How many molecules are in \\(2\\text{ moles}\\) of any substance?""",
     ["\\(6.022 \\times 10^{23}\\)", "\\(1.2044 \\times 10^{24}\\)", "\\(3.011 \\times 10^{23}\\)", "\\(2.4088 \\times 10^{24}\\)"],
     "B", "OSC", "easy",
     "• \\(2 \\times 6.022 \\times 10^{23} = 1.2044 \\times 10^{24}\\).\nCorrect Choice is (B)."),

    ("""What volume at STP is occupied by \\(2\\text{ moles}\\) of gas?""",
     ["\\(11.2\\text{ L}\\)", "\\(22.4\\text{ L}\\)", "\\(44.8\\text{ L}\\)", "\\(89.6\\text{ L}\\)"],
     "C", "OSC", "easy",
     "• \\(2 \\times 22.4 = 44.8\\text{ L}\\).\nCorrect Choice is (C)."),

    ("""What is the mass of \\(0.5\\text{ moles}\\) of water?""",
     ["\\(9\\text{ g}\\)", "\\(18\\text{ g}\\)", "\\(36\\text{ g}\\)", "\\(4.5\\text{ g}\\)"],
     "A", "OSC", "easy",
     "• \\(0.5 \\times 18 = 9\\text{ g}\\).\nCorrect Choice is (A)."),

    ("""How many moles are in \\(40\\text{ g}\\) of Sodium Hydroxide (\\(\\text{NaOH}\\))? (Molar mass = \\(40\\text{ g/mol}\\))""",
     ["\\(0.5\\text{ mole}\\)", "\\(1\\text{ mole}\\)", "\\(2\\text{ moles}\\)", "\\(40\\text{ moles}\\)"],
     "B", "OSC", "easy",
     "• \\(n = \\frac{40}{40} = 1\\text{ mole}\\).\nCorrect Choice is (B)."),

    ("""How many moles are in \\(80\\text{ g}\\) of \\(\\text{NaOH}\\)?""",
     ["\\(1\\text{ mole}\\)", "\\(2\\text{ moles}\\)", "\\(4\\text{ moles}\\)", "\\(8\\text{ moles}\\)"],
     "B", "OSC", "easy",
     "• \\(n = \\frac{80}{40} = 2\\text{ moles}\\).\nCorrect Choice is (B)."),

    ("""What is the molar mass of Sodium Chloride (\\(\\text{NaCl}\\))?""",
     ["\\(35.5\\text{ g/mol}\\)", "\\(58.5\\text{ g/mol}\\)", "\\(46.0\\text{ g/mol}\\)", "\\(71.0\\text{ g/mol}\\)"],
     "B", "OSC", "easy",
     "• \\(23 + 35.5 = 58.5\\text{ g/mol}\\).\nCorrect Choice is (B)."),

    ("""How many atoms are in \\(1\\text{ mole}\\) of Argon gas (\\(\\text{Ar}\\))?""",
     ["\\(3.011 \\times 10^{23}\\)", "\\(6.022 \\times 10^{23}\\)", "\\(1.2044 \\times 10^{24}\\)", "\\(40\\)"],
     "B", "OSC", "easy",
     "• Argon is monoatomic; 1 mole has \\(6.022 \\times 10^{23}\\) atoms.\nCorrect Choice is (B)."),

    ("""What is the mass of \\(1\\text{ mole}\\) of Nitrogen atoms (\\(\\text{N}\\))?""",
     ["\\(7\\text{ g}\\)", "\\(14\\text{ g}\\)", "\\(28\\text{ g}\\)", "\\(1\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• Mass of 1 mole of N atoms is \\(14\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""What is the mass of \\(1\\text{ mole}\\) of Nitrogen gas (\\(\\text{N}_2\\))?""",
     ["\\(14\\text{ g}\\)", "\\(28\\text{ g}\\)", "\\(56\\text{ g}\\)", "\\(7\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• Mass of 1 mole of \\(\\text{N}_2 = 2 \\times 14 = 28\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""How many moles are present in \\(5.6\\text{ g}\\) of Iron (\\(\\text{Fe}\\), atomic mass \\(56\\text{ u}\\))?""",
     ["\\(0.01\\text{ mole}\\)", "\\(0.1\\text{ mole}\\)", "\\(1\\text{ mole}\\)", "\\(10\\text{ moles}\\)"],
     "B", "OSC", "easy",
     "• \\(n = \\frac{5.6}{56} = 0.1\\text{ mole}\\).\nCorrect Choice is (B)."),

    ("""How many moles of atoms are in \\(44\\text{ g}\\) of \\(\\text{CO}_2\\)?""",
     ["\\(1\\text{ mole}\\)", "\\(2\\text{ moles}\\)", "\\(3\\text{ moles}\\)", "\\(44\\text{ moles}\\)"],
     "C", "OSC", "medium",
     "• \\(44\\text{ g}\\) is 1 mole of \\(\\text{CO}_2\\) molecules. Each molecule has 3 atoms (1 C + 2 O), so there are 3 moles of atoms.\nCorrect Choice is (C)."),

    ("""What is the mass of \\(0.1\\text{ moles}\\) of Sulphuric Acid (\\(\\text{H}_2\\text{SO}_4\\))?""",
     ["\\(4.9\\text{ g}\\)", "\\(9.8\\text{ g}\\)", "\\(98\\text{ g}\\)", "\\(19.6\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• Mass = \\(0.1 \\times 98 = 9.8\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""How many moles of gas are present in \\(1.12\\text{ litres}\\) at STP?""",
     ["\\(0.05\\text{ moles}\\)", "\\(0.1\\text{ mole}\\)", "\\(0.5\\text{ mole}\\)", "\\(1\\text{ mole}\\)"],
     "A", "OSC", "medium",
     "• \\(n = \\frac{1.12}{22.4} = 0.05\\text{ moles}\\).\nCorrect Choice is (A)."),

    ("""What is the mass of \\(3.011 \\times 10^{23}\\) molecules of Oxygen (\\(\\text{O}_2\\))?""",
     ["\\(8\\text{ g}\\)", "\\(16\\text{ g}\\)", "\\(32\\text{ g}\\)", "\\(64\\text{ g}\\)"],
     "B", "OSC", "medium",
     "• \\(n = 0.5\\text{ mole}\\). Mass = \\(0.5 \\times 32 = 16\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""State True or False: 1 mole of any element always has the exact same mass in grams as 1 mole of any other element.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. 1 mole contains the same NUMBER of particles, but different elements have different atomic masses.\nCorrect Choice is (B)."),

    ("""State True or False: The number of particles in one mole is constant regardless of temperature or pressure.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Avogadro's constant is a fundamental counting number.\nCorrect Choice is (A)."),

    ("""How many moles of Carbon are in \\(24\\text{ g}\\) of Carbon?""",
     ["\\(1\\text{ mole}\\)", "\\(2\\text{ moles}\\)", "\\(3\\text{ moles}\\)", "\\(12\\text{ moles}\\)"],
     "B", "OSC", "easy",
     "• \\(n = \\frac{24}{12} = 2\\text{ moles}\\).\nCorrect Choice is (B)."),

    ("""What is the mass of \\(10\\text{ moles}\\) of water?""",
     ["\\(18\\text{ g}\\)", "\\(90\\text{ g}\\)", "\\(180\\text{ g}\\)", "\\(360\\text{ g}\\)"],
     "C", "OSC", "easy",
     "• Mass = \\(10 \\times 18 = 180\\text{ g}\\).\nCorrect Choice is (C)."),

    ("""How many molecules are in \\(0.1\\text{ moles}\\) of sugar?""",
     ["\\(6.022 \\times 10^{22}\\)", "\\(6.022 \\times 10^{23}\\)", "\\(6.022 \\times 10^{24}\\)", "\\(3.011 \\times 10^{22}\\)"],
     "A", "OSC", "easy",
     "• \\(0.1 \\times 6.022 \\times 10^{23} = 6.022 \\times 10^{22}\\).\nCorrect Choice is (A)."),

    ("""What volume at STP is occupied by \\(0.1\\text{ moles}\\) of gas?""",
     ["\\(0.224\\text{ L}\\)", "\\(2.24\\text{ L}\\)", "\\(22.4\\text{ L}\\)", "\\(11.2\\text{ L}\\)"],
     "B", "OSC", "easy",
     "• \\(0.1 \\times 22.4 = 2.24\\text{ L}\\).\nCorrect Choice is (B)."),

    ("""Fill in the blank: One mole of Hydrogen gas (\\(\\text{H}_2\\)) contains ________ moles of Hydrogen atoms.""",
     ["\\(1\\)", "\\(2\\)", "\\(3\\)", "\\(4\\)"],
     "B", "OFB", "easy",
     "• Each molecule has 2 atoms; 1 mole of \\(\\text{H}_2\\) contains 2 moles of H atoms.\nCorrect Choice is (B)."),

    ("""Fill in the blank: The formula for calculating number of particles is \\(N = n \\times\\) ________.""",
     ["\\(M\\)", "\\(N_A\\)", "\\(V\\)", "\\(m\\)"],
     "B", "OFB", "easy",
     "• \\(N = n \\times N_A\\).\nCorrect Choice is (B)."),

    ("""What is the mass in grams of \\(2\\text{ moles}\\) of Magnesium (\\(\\text{Mg}\\), atomic mass \\(24\\text{ u}\\))?""",
     ["\\(12\\text{ g}\\)", "\\(24\\text{ g}\\)", "\\(48\\text{ g}\\)", "\\(96\\text{ g}\\)"],
     "C", "OSC", "easy",
     "• Mass = \\(2 \\times 24 = 48\\text{ g}\\).\nCorrect Choice is (C)."),

    ("""How many moles are in \\(69\\text{ g}\\) of Sodium (\\(\\text{Na}=23\\text{ u}\\))?""",
     ["\\(1\\text{ mole}\\)", "\\(2\\text{ moles}\\)", "\\(3\\text{ moles}\\)", "\\(4\\text{ moles}\\)"],
     "C", "OSC", "easy",
     "• \\(n = \\frac{69}{23} = 3\\text{ moles}\\).\nCorrect Choice is (C)."),

    ("""What is the mass of \\(1\\text{ mole}\\) of Calcium (\\(\\text{Ca}=40\\text{ u}\\))?""",
     ["\\(20\\text{ g}\\)", "\\(40\\text{ g}\\)", "\\(80\\text{ g}\\)", "\\(100\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• Mass of 1 mole of Ca is \\(40\\text{ g}\\).\nCorrect Choice is (B)."),

    ("""How many moles are present in \\(4.4\\text{ g}\\) of \\(\\text{CO}_2\\)?""",
     ["\\(0.01\\text{ mole}\\)", "\\(0.1\\text{ mole}\\)", "\\(1.0\\text{ mole}\\)", "\\(10\\text{ moles}\\)"],
     "B", "OSC", "easy",
     "• \\(n = \\frac{4.4}{44} = 0.1\\text{ mole}\\).\nCorrect Choice is (B).")
]

# 12 Foundation Mock Questions (501-512) with rich embedded vector SVGs
foundation_data = [
    # 501: Mole Conversion Triangle (Mass, Moles, Particles)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">The Central Mole Triangle</text>
  <!-- Central Moles Circle -->
  <circle cx="170" cy="115" r="32" fill="#334155" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="145" y="112" fill="#38bdf8" font-size="12" font-weight="bold">MOLES</text>
  <text x="155" y="128" fill="#cbd5e1" font-size="10">(n)</text>
  <!-- Left Box: Mass (g) -->
  <rect x="20" y="90" width="80" height="50" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="35" y="112" fill="#fde047" font-size="10" font-weight="bold">Mass (m)</text>
  <text x="35" y="128" fill="#cbd5e1" font-size="9">in grams</text>
  <!-- Right Box: Particles (N) -->
  <rect x="240" y="90" width="80" height="50" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="250" y="112" fill="#34d399" font-size="10" font-weight="bold">Particles (N)</text>
  <text x="245" y="128" fill="#cbd5e1" font-size="8">atoms/molecules</text>
  <!-- Arrows -->
  <text x="105" y="105" fill="#f59e0b" font-size="10">÷ M →</text>
  <text x="105" y="130" fill="#f59e0b" font-size="10">← × M</text>
  <text x="205" y="105" fill="#10b981" font-size="10">→ × N_A</text>
  <text x="205" y="130" fill="#10b981" font-size="10">← ÷ N_A</text>
  <text x="45" y="195" fill="#93c5fd" font-size="10">Bridge between microscopic entities and laboratory scale</text>
</svg>
</div>
Using the Mole Triangle conversion framework shown above, how many molecules are present in \\(9.0\\text{ g}\\) of pure water (\\(\\text{H}_2\\text{O}\\), \\(M = 18\\text{ g/mol}\\))?""",
     ["\\(6.022 \\times 10^{23}\\)",
      "\\(3.011 \\times 10^{23}\\) (which is \\(0.5 \\times N_A\\))",
      "\\(1.505 \\times 10^{23}\\)",
      "\\(1.2044 \\times 10^{24}\\)"],
     "B", "OSC", "medium",
     "• Step 1: \\(n = \\frac{m}{M} = \\frac{9.0}{18} = 0.5\\text{ mol}\\).\nStep 2: \\(N = n \\times N_A = 0.5 \\times 6.022 \\times 10^{23} = 3.011 \\times 10^{23}\\) molecules.\nCorrect Choice is (B)."),

    # 502: Molar Volume at STP Cube (22.4 L)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Standard Molar Volume (STP)</text>
  <!-- Cube representing 22.4 L -->
  <polygon points="120,80 180,50 240,80 180,110" fill="#334155" stroke="#38bdf8" stroke-width="1.5"/>
  <polygon points="120,80 180,110 180,170 120,140" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <polygon points="180,110 240,80 240,140 180,170" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="155" y="125" fill="#fde047" font-size="13" font-weight="bold">22.4 L</text>
  <text x="145" y="145" fill="#cbd5e1" font-size="9">(28.2 cm side)</text>
  <!-- Facts -->
  <text x="35" y="195" fill="#34d399" font-size="10">1 mole of ANY ideal gas at 0°C &amp; 1 atm occupies 22.4 L</text>
</svg>
</div>
In the molar volume diagram above, what mass of Methane gas (\\(\\text{CH}_4\\), molar mass \\(16\\text{ g/mol}\\)) will completely fill this \\(22.4\\text{ L}\\) container at STP?""",
     ["\\(8\\text{ g}\\)", "\\(16\\text{ g}\\)", "\\(22.4\\text{ g}\\)", "\\(32\\text{ g}\\)"],
     "B", "OSC", "easy",
     "• At STP, \\(22.4\\text{ L}\\) contains exactly \\(1\\text{ mole}\\) of gas. The mass of 1 mole of \\(\\text{CH}_4\\) is \\(16\\text{ g}\\).\nCorrect Choice is (B)."),

    # 503: Avogadro Counting Analogy
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Counting Units in Daily Life vs Chemistry</text>
  <!-- 1 Dozen -->
  <rect x="30" y="55" width="130" height="60" fill="#1e293b" stroke="#94a3b8" rx="3"/>
  <text x="40" y="80" fill="#cbd5e1" font-size="11" font-weight="bold">1 Dozen</text>
  <text x="40" y="100" fill="#fde047" font-size="11">= 12 items</text>
  <!-- 1 Gross -->
  <rect x="180" y="55" width="130" height="60" fill="#1e293b" stroke="#94a3b8" rx="3"/>
  <text x="190" y="80" fill="#cbd5e1" font-size="11" font-weight="bold">1 Gross</text>
  <text x="190" y="100" fill="#fde047" font-size="11">= 144 items (12 doz)</text>
  <!-- 1 Mole -->
  <rect x="30" y="130" width="280" height="55" fill="#334155" stroke="#38bdf8" stroke-width="2" rx="4"/>
  <text x="45" y="155" fill="#38bdf8" font-size="12" font-weight="bold">1 MOLE</text>
  <text x="100" y="155" fill="#34d399" font-size="12" font-weight="bold">= 6.022 × 10²³ particles</text>
  <text x="45" y="175" fill="#cbd5e1" font-size="10">The universal chemist's counting packet for microscopic entities</text>
</svg>
</div>
How does the concept of a 'mole' conceptually compare to common counting terms like 'a dozen' or 'a gross'?""",
     ["A mole is a measure of weight only, not a count",
      "Just as 1 dozen signifies exactly 12 items and 1 gross signifies 144 items, 1 mole signifies a fixed count of \\(6.022 \\times 10^{23}\\) elementary entities",
      "A mole changes its number depending on room temperature",
      "A mole has no connection to particle counting"],
     "B", "OSC", "easy",
     "• A mole is a fundamental counting unit representing a fixed number (\\(6.022 \\times 10^{23}\\)) of entities, exactly analogous to a dozen (12) or gross (144).\nCorrect Choice is (B)."),

    # 504: Water Mole Physical Scale (18 mL)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Physical Reality of 1 Mole of Water</text>
  <!-- Measuring Cylinder -->
  <rect x="70" y="55" width="40" height="120" fill="#1e293b" stroke="#94a3b8" rx="3"/>
  <!-- Liquid level 18 mL -->
  <rect x="71" y="145" width="38" height="30" fill="#38bdf8" opacity="0.8"/>
  <line x1="65" y1="145" x2="115" y2="145" stroke="#f59e0b" stroke-width="2"/>
  <text x="120" y="150" fill="#fde047" font-size="11" font-weight="bold">18 mL (~1.2 tablespoons)</text>
  <!-- Properties box -->
  <rect x="145" y="65" width="170" height="70" fill="#334155" stroke="#38bdf8" rx="3"/>
  <text x="155" y="85" fill="#38bdf8" font-size="10" font-weight="bold">1 Mole of H₂O contains:</text>
  <text x="155" y="102" fill="#cbd5e1" font-size="9">• Mass = 18.0 grams</text>
  <text x="155" y="118" fill="#34d399" font-size="9">• 6.022 × 10²³ H₂O molecules</text>
  <text x="45" y="195" fill="#cbd5e1" font-size="10">In a single small sip of water, you swallow &gt; 10²³ molecules!</text>
</svg>
</div>
In the measuring cylinder shown, a tiny volume of only \\(18\\text{ mL}\\) of liquid water represents \\(1\\text{ mole}\\). How many individual hydrogen atoms are contained in this single sip of water?""",
     ["\\(6.022 \\times 10^{23}\\)",
      "\\(1.2044 \\times 10^{24}\\) (\\(2 \\times N_A\\))",
      "\\(1.8066 \\times 10^{24}\\)",
      "\\(18\\)"],
     "B", "OSC", "medium",
     "• In 1 mole of \\(\\text{H}_2\\text{O}\\), there are \\(6.022 \\times 10^{23}\\) molecules. Each molecule has 2 hydrogen atoms, giving \\(2 \\times 6.022 \\times 10^{23} = 1.2044 \\times 10^{24}\\) hydrogen atoms.\nCorrect Choice is (B)."),

    # 505: Carbon-12 Balance Definition
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">12 Grams of Carbon-12 = 1 Mole</text>
  <!-- Digital Balance -->
  <rect x="70" y="100" width="200" height="60" fill="#334155" stroke="#94a3b8" rx="4"/>
  <rect x="110" y="125" width="120" height="28" fill="#0f172a" rx="2"/>
  <text x="135" y="145" fill="#34d399" font-size="16" font-family="monospace">12.000 g</text>
  <!-- Graphite sample on pan -->
  <ellipse cx="170" cy="98" rx="35" ry="10" fill="#475569" stroke="#64748b"/>
  <text x="135" y="85" fill="#fde047" font-size="10" font-weight="bold">Pure ¹²C Graphite</text>
  <text x="45" y="185" fill="#cbd5e1" font-size="10">Exactly 6.022 × 10²³ carbon atoms are balanced on this plate</text>
</svg>
</div>
If the digital balance reading of pure Carbon-12 graphite is \\(12.000\\text{ g}\\) as illustrated, how many carbon atoms are present on the pan?""",
     ["\\(12\\text{ atoms}\\)",
      "\\(1\\text{ atom}\\)",
      "\\(6.022 \\times 10^{23}\\text{ atoms}\\)",
      "\\(1.9926 \\times 10^{-23}\\text{ atoms}\\)"],
     "C", "OSC", "easy",
     "• By the SI definition of the mole, \\(12\\text{ g}\\) of Carbon-12 contains exactly \\(1\\text{ mole} = 6.022 \\times 10^{23}\\) atoms.\nCorrect Choice is (C)."),

    # 506: Mole to Volume Gas Comparison (H2 vs O2 vs CO2 at STP)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="70" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Molar Comparison at STP (22.4 L each)</text>
  <!-- Balloon 1: H2 -->
  <circle cx="70" cy="90" r="30" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="58" y="88" fill="#38bdf8" font-size="10" font-weight="bold">H₂ Gas</text>
  <text x="55" y="102" fill="#cbd5e1" font-size="9">Mass = 2g</text>
  <text x="50" y="135" fill="#fde047" font-size="9">1 mol = 22.4L</text>
  <!-- Balloon 2: O2 -->
  <circle cx="170" cy="90" r="30" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
  <text x="158" y="88" fill="#ef4444" font-size="10" font-weight="bold">O₂ Gas</text>
  <text x="152" y="102" fill="#cbd5e1" font-size="9">Mass = 32g</text>
  <text x="150" y="135" fill="#fde047" font-size="9">1 mol = 22.4L</text>
  <!-- Balloon 3: CO2 -->
  <circle cx="270" cy="90" r="30" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  <text x="255" y="88" fill="#10b981" font-size="10" font-weight="bold">CO₂ Gas</text>
  <text x="252" y="102" fill="#cbd5e1" font-size="9">Mass = 44g</text>
  <text x="250" y="135" fill="#fde047" font-size="9">1 mol = 22.4L</text>
  <text x="45" y="185" fill="#93c5fd" font-size="10">All 3 have IDENTICAL volumes (22.4L) and particles (6.022×10²³)</text>
</svg>
</div>
In the three gas balloons at STP shown above, why do all three have the exact same volume (\\(22.4\\text{ L}\\)) and particle count (\\(6.022 \\times 10^{23}\\)) despite having vastly different masses (\\(2\\text{ g}\\), \\(32\\text{ g}\\), and \\(44\\text{ g}\\))?""",
     ["Because heavy gases compress more",
      "Because Avogadro's Law establishes that equal volumes of all gases under identical conditions contain equal numbers of particles, and gas volume is determined by intermolecular spacing rather than individual molecular mass",
      "Because oxygen turns into hydrogen at 0°C",
      "Because balloons cannot expand past 22.4 litres"],
     "B", "OSC", "hard",
     "• In ideal gases, the size/mass of individual molecules is negligible compared to the vast empty distance between them; hence 1 mole of any gas occupies \\(22.4\\text{ L}\\) at STP.\nCorrect Choice is (B)."),

    # 507: Helium vs Argon Mole Mass Comparison
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Helium (He) vs Argon (Ar) Moles</text>
  <!-- Balance Seesaw -->
  <line x1="60" y1="130" x2="280" y2="130" stroke="#94a3b8" stroke-width="3"/>
  <polygon points="170,130 160,165 180,165" fill="#64748b"/>
  <!-- Left: 1 mol He -->
  <circle cx="80" cy="115" r="14" fill="#38bdf8"/>
  <text x="50" y="90" fill="#38bdf8" font-size="10" font-weight="bold">1 mol He (4 g)</text>
  <text x="45" y="150" fill="#cbd5e1" font-size="9">6.022 × 10²³ atoms</text>
  <!-- Right: 1 mol Ar -->
  <circle cx="260" cy="115" r="14" fill="#f59e0b"/>
  <text x="230" y="90" fill="#fde047" font-size="10" font-weight="bold">1 mol Ar (40 g)</text>
  <text x="225" y="150" fill="#cbd5e1" font-size="9">6.022 × 10²³ atoms</text>
  <text x="55" y="185" fill="#34d399" font-size="10">Argon is 10× heavier per mole, but particle count is identical</text>
</svg>
</div>
Comparing 1 mole of Helium (\\(4\\text{ g}\\)) and 1 mole of Argon (\\(40\\text{ g}\\)), what is the ratio of the number of atoms in Helium to the number of atoms in Argon?""",
     ["\\(1 : 10\\)", "\\(10 : 1\\)", "\\(1 : 1\\)", "\\(1 : 4\\)"],
     "C", "OSC", "medium",
     "• Both samples contain exactly 1 mole, so both contain \\(N_A = 6.022 \\times 10^{23}\\) atoms. The ratio of atom counts is strictly \\(1 : 1\\).\nCorrect Choice is (C)."),

    # 508: Atom Counting Breakdown in Carbon Dioxide (CO2)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Atom Partition in 1 Mole of CO₂</text>
  <!-- Formula -->
  <text x="120" y="60" fill="#fde047" font-size="16" font-weight="bold">1 Mole CO₂ (44 g)</text>
  <!-- Branching -->
  <rect x="35" y="80" width="125" height="60" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="45" y="105" fill="#38bdf8" font-size="11" font-weight="bold">Carbon Atoms:</text>
  <text x="45" y="125" fill="#cbd5e1" font-size="10">1 mol C = 6.022 × 10²³</text>
  <rect x="180" y="80" width="125" height="60" fill="#1e293b" stroke="#ef4444" rx="3"/>
  <text x="190" y="105" fill="#f87171" font-size="11" font-weight="bold">Oxygen Atoms:</text>
  <text x="190" y="125" fill="#cbd5e1" font-size="10">2 mol O = 1.204 × 10²⁴</text>
  <rect x="35" y="155" width="270" height="35" fill="#334155" stroke="#34d399" rx="3"/>
  <text x="50" y="177" fill="#34d399" font-size="11" font-weight="bold">Total Atoms = 1 + 2 = 3 moles = 1.8066 × 10²⁴</text>
</svg>
</div>
In \\(88\\text{ g}\\) of Carbon Dioxide gas (\\(\\text{CO}_2\\), molar mass \\(44\\text{ g/mol}\\)), what is the total number of oxygen atoms present?""",
     ["\\(6.022 \\times 10^{23}\\)",
      "\\(1.2044 \\times 10^{24}\\)",
      "\\(2.4088 \\times 10^{24}\\) (which is \\(4 \\times N_A\\))",
      "\\(3.613 \\times 10^{24}\\)"],
     "C", "OSC", "hard",
     "• Number of moles of \\(\\text{CO}_2 = \\frac{88}{44} = 2\\text{ moles}\\).\nEach mole of \\(\\text{CO}_2\\) contains 2 moles of O atoms, so 2 moles contains \\(2 \\times 2 = 4\\text{ moles}\\) of O atoms.\nTotal oxygen atoms = \\(4 \\times 6.022 \\times 10^{23} = 2.4088 \\times 10^{24}\\).\nCorrect Choice is (C)."),

    # 509: Glucose Molar Mass and Mole Fractions
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">1 Mole of Glucose (C₆H₁₂O₆ = 180 g)</text>
  <!-- Breakdown -->
  <rect x="30" y="55" width="85" height="70" fill="#1e293b" stroke="#94a3b8" rx="3"/>
  <text x="40" y="75" fill="#cbd5e1" font-size="10" font-weight="bold">6 mol Carbon</text>
  <text x="40" y="95" fill="#fde047" font-size="10">6 × 12 = 72g</text>
  <text x="40" y="112" fill="#94a3b8" font-size="8">3.613 × 10²⁴ atoms</text>
  <rect x="125" y="55" width="90" height="70" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="130" y="75" fill="#38bdf8" font-size="10" font-weight="bold">12 mol Hydrogen</text>
  <text x="130" y="95" fill="#fde047" font-size="10">12 × 1 = 12g</text>
  <text x="130" y="112" fill="#94a3b8" font-size="8">7.226 × 10²⁴ atoms</text>
  <rect x="225" y="55" width="85" height="70" fill="#1e293b" stroke="#ef4444" rx="3"/>
  <text x="235" y="75" fill="#f87171" font-size="10" font-weight="bold">6 mol Oxygen</text>
  <text x="235" y="95" fill="#fde047" font-size="10">6 × 16 = 96g</text>
  <text x="235" y="112" fill="#94a3b8" font-size="8">3.613 × 10²⁴ atoms</text>
  <text x="50" y="175" fill="#34d399" font-size="11" font-weight="bold">Total atoms in 1 mol Glucose = 6 + 12 + 6 = 24 moles</text>
</svg>
</div>
How many total atoms of all elements combined are contained in \\(0.5\\text{ moles}\\) of glucose (\\(\\text{C}_6\\text{H}_{12}\\text{O}_6\\))?""",
     ["\\(12\\text{ atoms}\\)",
      "\\(6.022 \\times 10^{23}\\text{ atoms}\\)",
      "\\(7.2264 \\times 10^{24}\\text{ atoms} (12 \\times N_A)\\)",
      "\\(1.445 \\times 10^{25}\\text{ atoms}\\)"],
     "C", "OSC", "hard",
     "• 1 molecule of glucose contains \\(6 + 12 + 6 = 24\\) atoms.\nIn \\(0.5\\text{ moles}\\), there are \\(0.5 \\times 24 = 12\\text{ moles}\\) of atoms.\nTotal atoms = \\(12 \\times 6.022 \\times 10^{23} = 7.2264 \\times 10^{24}\\).\nCorrect Choice is (C)."),

    # 510: Avogadro's Hypothesis Gas Equal Volume Experiment
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Avogadro's Law Verification (Equal V)</text>
  <!-- Flask 1: 1L H2 -->
  <rect x="40" y="55" width="70" height="85" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="50" y="80" fill="#38bdf8" font-size="11" font-weight="bold">1 Litre H₂</text>
  <text x="50" y="100" fill="#cbd5e1" font-size="9">P = 1 atm</text>
  <text x="50" y="115" fill="#cbd5e1" font-size="9">T = 273 K</text>
  <text x="50" y="130" fill="#fde047" font-size="10">N molecules</text>
  <!-- Flask 2: 1L Cl2 -->
  <rect x="135" y="55" width="70" height="85" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="145" y="80" fill="#10b981" font-size="11" font-weight="bold">1 Litre Cl₂</text>
  <text x="145" y="100" fill="#cbd5e1" font-size="9">P = 1 atm</text>
  <text x="145" y="115" fill="#cbd5e1" font-size="9">T = 273 K</text>
  <text x="145" y="130" fill="#fde047" font-size="10">N molecules</text>
  <!-- Flask 3: 1L NH3 -->
  <rect x="230" y="55" width="70" height="85" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="240" y="80" fill="#f59e0b" font-size="11" font-weight="bold">1 Litre NH₃</text>
  <text x="240" y="100" fill="#cbd5e1" font-size="9">P = 1 atm</text>
  <text x="240" y="115" fill="#cbd5e1" font-size="9">T = 273 K</text>
  <text x="240" y="130" fill="#fde047" font-size="10">N molecules</text>
  <text x="50" y="175" fill="#34d399" font-size="11" font-weight="bold">At same T &amp; P: Equal Volume = Equal Molecules</text>
</svg>
</div>
According to Avogadro's hypothesis illustrated above, if \\(1\\text{ litre}\\) of \\(\\text{H}_2\\) contains \\(N\\) molecules at STP, how many molecules are contained in \\(3\\text{ litres}\\) of \\(\\text{NH}_3\\) gas at the exact same temperature and pressure?""",
     ["\\(N\\) molecules", "\\(2N\\) molecules", "\\(3N\\) molecules", "\\(9N\\) molecules"],
     "C", "OSC", "medium",
     "• By Avogadro's Law, volume is directly proportional to the number of molecules (\\(V \\propto n\\)). If \\(1\\text{ L}\\) has \\(N\\) molecules, \\(3\\text{ L}\\) contains \\(3N\\) molecules.\nCorrect Choice is (C)."),

    # 511: Stoichiometric Mole Ratio in Ammonia Synthesis
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Mole Stoichiometry: N₂ + 3 H₂ ⟶ 2 NH₃</text>
  <!-- N2 -->
  <rect x="30" y="55" width="60" height="50" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="40" y="75" fill="#38bdf8" font-size="10" font-weight="bold">1 mol N₂</text>
  <text x="40" y="95" fill="#cbd5e1" font-size="9">28 g (22.4L)</text>
  <text x="98" y="85" fill="#fff" font-size="16">+</text>
  <!-- 3H2 -->
  <rect x="115" y="55" width="65" height="50" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="122" y="75" fill="#fde047" font-size="10" font-weight="bold">3 mol H₂</text>
  <text x="122" y="95" fill="#cbd5e1" font-size="9">6 g (67.2L)</text>
  <text x="190" y="85" fill="#38bdf8" font-size="16">→</text>
  <!-- 2NH3 -->
  <rect x="215" y="55" width="95" height="50" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="225" y="75" fill="#34d399" font-size="10" font-weight="bold">2 mol NH₃</text>
  <text x="225" y="95" fill="#cbd5e1" font-size="9">34 g (44.8L)</text>
  <!-- Summary -->
  <text x="40" y="145" fill="#fde047" font-size="10">Mole Ratio: 1 : 3 : 2</text>
  <text x="40" y="165" fill="#cbd5e1" font-size="10">Total Reactant Mass = 28 + 6 = 34g = Product Mass 34g</text>
</svg>
</div>
In Haber's ammonia reaction shown above, how many moles of hydrogen gas (\\(\\text{H}_2\\)) are required to produce \\(10\\text{ moles}\\) of ammonia gas (\\(\\text{NH}_3\\))?""",
     ["\\(5\\text{ moles}\\)", "\\(10\\text{ moles}\\)", "\\(15\\text{ moles}\\)", "\\(30\\text{ moles}\\)"],
     "C", "OSC", "medium",
     "• From the equation, 2 moles of \\(\\text{NH}_3\\) require 3 moles of \\(\\text{H}_2\\).\nFor 10 moles of \\(\\text{NH}_3\\), hydrogen needed = \\(10 \\times \\frac{3}{2} = 15\\text{ moles}\\).\nCorrect Choice is (C)."),

    # 512: Mass Spectrometry Isotopic Molar Average
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="70" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Avogadro Packets of Isotopes (Mg)</text>
  <!-- 3 Isotopes of Mg -->
  <rect x="30" y="55" width="80" height="75" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="40" y="75" fill="#38bdf8" font-size="10" font-weight="bold">²⁴Mg (79%)</text>
  <text x="40" y="95" fill="#cbd5e1" font-size="9">Mass = 24u</text>
  <text x="40" y="115" fill="#94a3b8" font-size="8">12p, 12n</text>
  <rect x="130" y="55" width="80" height="75" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="140" y="75" fill="#fde047" font-size="10" font-weight="bold">²⁵Mg (10%)</text>
  <text x="140" y="95" fill="#cbd5e1" font-size="9">Mass = 25u</text>
  <text x="140" y="115" fill="#94a3b8" font-size="8">12p, 13n</text>
  <rect x="230" y="55" width="80" height="75" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="240" y="75" fill="#34d399" font-size="10" font-weight="bold">²⁶Mg (11%)</text>
  <text x="240" y="95" fill="#cbd5e1" font-size="9">Mass = 26u</text>
  <text x="240" y="115" fill="#94a3b8" font-size="8">12p, 14n</text>
  <rect x="30" y="150" width="280" height="35" fill="#334155" stroke="#38bdf8" rx="3"/>
  <text x="45" y="172" fill="#38bdf8" font-size="11" font-weight="bold">Average Molar Mass of Mg = 24.31 g/mol</text>
</svg>
</div>
Why does a laboratory sample of 1 mole of naturally occurring Magnesium weigh \\(24.31\\text{ g}\\) instead of an integer like \\(24.0\\text{ g}\\)?""",
     ["Because individual magnesium atoms change weight every second",
      "Because natural magnesium contains a weighted mixture of three stable isotopes (\\(^{24}\\text{Mg}\\), \\(^{25}\\text{Mg}\\), \\(^{26}\\text{Mg}\\)), and \\(1\\text{ mole}\\) contains Avogadro's number of these mixed isotopic atoms in natural proportion",
      "Because electrons contribute \\(0.31\\text{ g}\\) of mass",
      "Because magnesium oxidizes inside the balance"],
     "B", "OSC", "medium",
     "• 1 mole of any naturally occurring element consists of \\(N_A\\) atoms distributed according to their natural isotopic abundances, resulting in a weighted average molar mass (\\(24.31\\text{ g/mol}\\)).\nCorrect Choice is (B).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-4-4.3-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-4-4.3-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-4-4.3-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch4_topic3.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
