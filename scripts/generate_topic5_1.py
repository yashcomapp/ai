# scripts/generate_topic5_1.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-5-5.1"
CHAPTER_NUM = 5

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: Arrhenius definition of acids and bases
    ("""Who proposed the classical theory of electrolytic dissociation of acids and bases in 1884?""",
     ["Antoine Lavoisier", "Svante Arrhenius", "Søren Sørensen", "Robert Boyle"],
     "B", "OSC", "easy",
     "• Swedish chemist Svante Arrhenius proposed that acids and bases dissociate into ions in aqueous solution.\nCorrect Choice is (B)."),

    ("""According to Arrhenius theory, an 'ACID' is defined as a substance which on dissolving in water:""",
     ["Produces hydroxide ions (\\(\\text{OH}^-\\)) as the only anions",
      "Dissociates to produce hydrogen ions (\\(\\text{H}^+\\)) as the only cations",
      "Releases oxygen gas bubbles",
      "Turns phenolphthalein deep pink"],
     "B", "OSC", "easy",
     "• Arrhenius defined an acid as a hydrogen-containing compound that yields \\(\\text{H}^+\\) ions in water.\nCorrect Choice is (B)."),

    ("""Why do free hydrogen ions (\\(\\text{H}^+\\)) not exist as bare protons in aqueous solution?""",
     ["Because they evaporate into the atmosphere",
      "Because a bare proton (\\(\\text{H}^+\\)) has an extremely high charge density and instantly bonds with a water molecule to form a stable hydronium ion (\\(\\text{H}_3\\text{O}^+\\))",
      "Because water repels positive charges",
      "Because hydrogen turns into helium in water"],
     "B", "OSC", "medium",
     "• A bare proton is minuscule (\\(\\sim 10^{-15}\\text{ m}\\)) and immediately hydrates: \\(\\text{H}^+ + \\text{H}_2\\text{O} \\to \\text{H}_3\\text{O}^+\\) (hydronium ion).\nCorrect Choice is (B)."),

    ("""According to Arrhenius theory, a 'BASE' is defined as a substance which on dissolving in water:""",
     ["Produces hydrogen ions (\\(\\text{H}^+\\)) as the only cations",
      "Dissociates to produce hydroxide ions (\\(\\text{OH}^-\\)) as the only anions",
      "Absorbs nitrogen from the atmosphere",
      "Turns blue litmus red"],
     "B", "OSC", "easy",
     "• An Arrhenius base dissociates in aqueous solution yielding \\(\\text{OH}^-\\) (hydroxide) as the sole negative ion.\nCorrect Choice is (B)."),

    ("""What is an 'ALKALI' in chemical terminology?""",
     ["Any insoluble metallic oxide",
      "A base that is readily soluble in water (such as \\(\\text{NaOH}\\) or \\(\\text{KOH}\\))",
      "An acid with a bitter taste",
      "A dry salt crystal"],
     "B", "OSC", "easy",
     "• Water-soluble bases are termed alkalis. All alkalis are bases, but not all bases are water-soluble alkalis.\nCorrect Choice is (B)."),

    ("""Which of the following substances is a water-soluble alkali?""",
     ["Copper(II) hydroxide (\\(\\text{Cu(OH)}_2\\))",
      "Ferric hydroxide (\\(\\text{Fe(OH)}_3\\))",
      "Potassium hydroxide (\\(\\text{KOH}\\))",
      "Aluminium hydroxide (\\(\\text{Al(OH)}_3\\))"],
     "C", "OSC", "easy",
     "• \\(\\text{KOH}\\) dissolves completely in water, forming a caustic alkali solution. Transition metal hydroxides like \\(\\text{Cu(OH)}_2\\) are insoluble bases.\nCorrect Choice is (C)."),

    ("""What defines a 'STRONG ACID'?""",
     ["An acid with a very strong smell",
      "An acid that dissociates almost completely in aqueous solution, converting nearly all its molecules into \\(\\text{H}^+\\) (or \\(\\text{H}_3\\text{O}^+\\)) ions",
      "An acid stored in glass bottles",
      "An acid that does not react with zinc"],
     "B", "OSC", "easy",
     "• Strong acids (e.g. \\(\\text{HCl}\\), \\(\\text{HNO}_3\\), \\(\\text{H}_2\\text{SO}_4\\)) have a degree of dissociation \\(\\alpha \\approx 1\\) (nearly 100% ionized).\nCorrect Choice is (B)."),

    ("""Which of the following is a WEAK acid?""",
     ["Hydrochloric acid (\\(\\text{HCl}\\))",
      "Nitric acid (\\(\\text{HNO}_3\\))",
      "Acetic acid (Ethanoic acid, \\(\\text{CH}_3\\text{COOH}\\))",
      "Sulphuric acid (\\(\\text{H}_2\\text{SO}_4\\))"],
     "C", "OSC", "easy",
     "• Acetic acid dissociates only partially in water (typically \\(< 5\\%\\)), leaving mostly undissociated molecules in equilibrium with ions.\nCorrect Choice is (C)."),

    ("""What defines a 'STRONG BASE'?""",
     ["A base that dissociates almost completely in water into metal cations and hydroxide ions (\\(\\text{OH}^-\\))",
      "A base that cannot dissolve in water",
      "A base with high density",
      "A base that turns phenolphthalein colorless"],
     "A", "OSC", "easy",
     "• Strong bases (like \\(\\text{NaOH}\\), \\(\\text{KOH}\\)) ionize almost completely in water.\nCorrect Choice is (A)."),

    ("""Which of the following is a WEAK base?""",
     ["Sodium hydroxide (\\(\\text{NaOH}\\))",
      "Potassium hydroxide (\\(\\text{KOH}\\))",
      "Ammonium hydroxide (\\(\\text{NH}_4\\text{OH}\\))",
      "Barium hydroxide (\\(\\text{Ba(OH)}_2\\))"],
     "C", "OSC", "easy",
     "• Ammonium hydroxide (\\(\\text{NH}_4\\text{OH}\\)) ionizes only slightly in water, behaving as a weak base.\nCorrect Choice is (C)."),

    # 11-20: Basicity of acids, Acidity of bases
    ("""What is meant by the 'BASICITY OF AN ACID'?""",
     ["The number of hydroxide ions the acid can absorb",
      "The number of replaceable hydrogen ions (\\(\\text{H}^+\\)) produced by one molecule of the acid on complete dissociation in water",
      "The boiling point of the acid",
      "The mass of the acid in kilograms"],
     "B", "OSC", "easy",
     "• Basicity is the number of ionizable \\(\\text{H}^+\\) ions generated per acid molecule.\nCorrect Choice is (B)."),

    ("""Which of the following is a MONOBASIC acid?""",
     ["Sulphuric acid (\\(\\text{H}_2\\text{SO}_4\\))",
      "Carbonic acid (\\(\\text{H}_2\\text{CO}_3\\))",
      "Hydrochloric acid (\\(\\text{HCl}\\))",
      "Phosphoric acid (\\(\\text{H}_3\\text{PO}_4\\))"],
     "C", "OSC", "easy",
     "• \\(\\text{HCl}\\) dissociates to give exactly one \\(\\text{H}^+\\) ion per molecule, making it monobasic.\nCorrect Choice is (C)."),

    ("""Why is Acetic acid (\\(\\text{CH}_3\\text{COOH}\\)) classified as MONOBASIC, even though its molecule contains four hydrogen atoms?""",
     ["Three hydrogen atoms evaporate upon dissolution",
      "Only the single hydrogen atom attached to the carboxyl group (\\(-\\text{COOH}\\)) is ionizable; the three hydrogens bonded to methyl carbon cannot dissociate as \\(\\text{H}^+\\)",
      "Because acetic acid is an inorganic acid",
      "Because its molecular weight is under 100"],
     "B", "OSC", "medium",
     "• In \\(\\text{CH}_3\\text{COOH}\\), only the polar \\(\\text{O-H}\\) bond ionizes: \\(\\text{CH}_3\\text{COOH} \\rightleftharpoons \\text{CH}_3\\text{COO}^- + \\text{H}^+\\).\nCorrect Choice is (B)."),

    ("""Which of the following is a DIBASIC acid?""",
     ["Nitric acid (\\(\\text{HNO}_3\\))",
      "Sulphuric acid (\\(\\text{H}_2\\text{SO}_4\\))",
      "Hydrochloric acid (\\(\\text{HCl}\\))",
      "Acetic acid (\\(\\text{CH}_3\\text{COOH}\\))"],
     "B", "OSC", "easy",
     "• \\(\\text{H}_2\\text{SO}_4\\) yields two \\(\\text{H}^+\\) ions per molecule upon complete dissociation.\nCorrect Choice is (B)."),

    ("""Which of the following is a TRIBASIC acid?""",
     ["Sulphuric acid (\\(\\text{H}_2\\text{SO}_4\\))",
      "Phosphoric acid (\\(\\text{H}_3\\text{PO}_4\\))",
      "Carbonic acid (\\(\\text{H}_2\\text{CO}_3\\))",
      "Nitric acid (\\(\\text{HNO}_3\\))"],
     "B", "OSC", "easy",
     "• Phosphoric acid (\\(\\text{H}_3\\text{PO}_4\\)) can dissociate in three stages, providing 3 ionizable \\(\\text{H}^+\\) ions per molecule.\nCorrect Choice is (B)."),

    ("""What is meant by the 'ACIDITY OF A BASE'?""",
     ["The mass of acid required to burn the base",
      "The number of replaceable hydroxide ions (\\(\\text{OH}^-\\)) produced by one molecule of the base on complete dissociation in water",
      "The sour taste of the base",
      "The boiling point of the base"],
     "B", "OSC", "easy",
     "• Acidity of a base is the number of ionizable \\(\\text{OH}^-\\) ions provided per molecule.\nCorrect Choice is (B)."),

    ("""Which of the following is a DIACIDIC base?""",
     ["Sodium hydroxide (\\(\\text{NaOH}\\))",
      "Calcium hydroxide (\\(\\text{Ca(OH)}_2\\))",
      "Aluminium hydroxide (\\(\\text{Al(OH)}_3\\))",
      "Potassium hydroxide (\\(\\text{KOH}\\))"],
     "B", "OSC", "easy",
     "• \\(\\text{Ca(OH)}_2\\) yields two \\(\\text{OH}^-\\) ions per molecule, making it a diacidic base.\nCorrect Choice is (B)."),

    ("""Which of the following is a TRIACIDIC base?""",
     ["Magnesium hydroxide (\\(\\text{Mg(OH)}_2\\))",
      "Aluminium hydroxide (\\(\\text{Al(OH)}_3\\))",
      "Sodium hydroxide (\\(\\text{NaOH}\\))",
      "Barium hydroxide (\\(\\text{Ba(OH)}_2\\))"],
     "B", "OSC", "easy",
     "• \\(\\text{Al(OH)}_3\\) dissociates to yield three \\(\\text{OH}^-\\) ions per formula unit, making it triacidic.\nCorrect Choice is (B)."),

    ("""What is the crucial scientific difference between the 'CONCENTRATION' of an acid and the 'STRENGTH' of an acid?""",
     ["There is no difference; they mean the exact same thing",
      "Concentration refers to the amount of acid solute dissolved in a unit volume of water, whereas strength refers to the intrinsic degree of dissociation of acid molecules into ions",
      "Strength refers to the volume of acid, while concentration refers to temperature",
      "Concentration applies only to bases"],
     "B", "OSC", "medium",
     "• A dilute solution of \\(\\text{HCl}\\) is still a strong acid (because it is 100% dissociated), while pure glacial acetic acid is a concentrated weak acid (because it ionizes poorly).\nCorrect Choice is (B)."),

    ("""What happens to an aqueous solution of dry hydrogen chloride gas (\\(\\text{HCl}\\))?""",
     ["It remains as uncharged neutral molecules in water",
      "It completely ionizes into hydronium ions (\\(\\text{H}_3\\text{O}^+\\)) and chloride ions (\\(\\text{Cl}^-\\)), conducting electricity vigorously",
      "It freezes immediately",
      "It forms chlorine gas bubbles"],
     "B", "OSC", "easy",
     "• \\(\\text{HCl} + \\text{H}_2\\text{O} \\to \\text{H}_3\\text{O}^+ + \\text{Cl}^-\\); complete ionization makes hydrochloric acid a strong electrolyte.\nCorrect Choice is (B)."),

    # 21-30: Electrical conductivity, degree of dissociation
    ("""Why does pure, dry liquid hydrogen chloride (or glacial acetic acid) NOT conduct electricity, whereas its aqueous solution conducts electricity efficiently?""",
     ["Water provides extra electrons to the molecules",
      "Pure liquid \\(\\text{HCl}\\) exists as covalent molecules without free ions; water acts as an ionizing solvent that breaks covalent bonds into mobile cations and anions",
      "Dry acid molecules are frozen",
      "Electricity travels only through pure metals"],
     "B", "OSC", "medium",
     "• Conduction requires mobile ions. Covalent \\(\\text{HCl}\\) ionizes only when dissolved in a polar solvent like water.\nCorrect Choice is (B)."),

    ("""Why does an aqueous solution of glucose (\\(\\text{C}_6\\text{H}_{12}\\text{O}_6\\)) or alcohol (\\(\\text{C}_2\\text{H}_5\\text{OH}\\)) NOT conduct electricity or show acidic properties, despite containing hydrogen atoms?""",
     ["Because their hydrogen atoms do not dissociate as free \\(\\text{H}^+\\) ions in water",
      "Because glucose molecules destroy electric current",
      "Because alcohol absorbs all ions from water",
      "Because glucose is too heavy to conduct"],
     "A", "OSC", "easy",
     "• Only ionizable hydrogen forming \\(\\text{H}^+\\) yields acidic character and electrical conductivity. Glucose and ethanol dissolve as intact neutral molecules.\nCorrect Choice is (A)."),

    ("""Assertion (A): All alkalis are bases, but all bases are not alkalis.\nReason (R): Alkalis are specifically defined as those bases which are readily soluble in water; insoluble metal hydroxides like \\(\\text{Fe(OH)}_3\\) are bases but not alkalis.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "• Alkalis are a subset of bases comprising the water-soluble ones.\nCorrect Choice is (A)."),

    ("""Assertion (A): A \\(0.001\\text{ M}\\) aqueous solution of hydrochloric acid (\\(\\text{HCl}\\)) is a dilute acid, but still classified as a strong acid.\nReason (R): Acid strength depends on the degree of dissociation (which is nearly 100% for \\(\\text{HCl}\\)), independent of the amount of water used to dilute it.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "medium",
     "• Dilution affects concentration (moles per litre), not the intrinsic percentage ionization (strength).\nCorrect Choice is (A)."),

    ("""State True or False: Dry blue litmus paper turns red when exposed to dry \\(\\text{HCl}\\) gas.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. Acidic color change requires \\(\\text{H}^+\\) ions, which can only form in the presence of moisture. Dry \\(\\text{HCl}\\) has no effect on dry litmus.\nCorrect Choice is (B)."),

    ("""State True or False: Carbonic acid (\\(\\text{H}_2\\text{CO}_3\\)) present in carbonated soda drinks is a dibasic weak acid.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. \\(\\text{H}_2\\text{CO}_3\\) is dibasic (2 ionizable H) and partially dissociates, making it a weak acid safe for human consumption.\nCorrect Choice is (A)."),

    ("""What is the degree of dissociation (\\(\\alpha\\)) of a completely ionized strong acid?""",
     ["\\(\\alpha = 0\\)", "\\(\\alpha \\approx 1\\) (or \\(100\\%\\))", "\\(\\alpha = 0.5\\)", "\\(\\alpha = 10\\)"],
     "B", "OSC", "easy",
     "• Degree of dissociation \\(\\alpha = \\frac{\\text{dissociated molecules}}{\\text{total molecules}} \\approx 1\\) for strong electrolytes.\nCorrect Choice is (B)."),

    ("""Which of the following acids dissociates in TWO successive stages in water?""",
     ["Nitric acid (\\(\\text{HNO}_3\\))",
      "Sulphuric acid (\\(\\text{H}_2\\text{SO}_4\\))",
      "Hydrochloric acid (\\(\\text{HCl}\\))",
      "Hydrobromic acid (\\(\\text{HBr}\\))"],
     "B", "OSC", "easy",
     "• \\(\\text{H}_2\\text{SO}_4\\) dissociates in two steps: first to \\(\\text{H}^+ + \\text{HSO}_4^-\\), then \\(\\text{HSO}_4^- \\rightleftharpoons \\text{H}^+ + \\text{SO}_4^{2-}\\).\nCorrect Choice is (B)."),

    ("""Which ion is universally responsible for all acidic chemical properties in aqueous solution?""",
     ["Chloride ion (\\(\\text{Cl}^-\\))",
      "Hydronium ion (\\(\\text{H}_3\\text{O}^+\\) / \\(\\text{H}^+\\))",
      "Hydroxide ion (\\(\\text{OH}^-\\))",
      "Sodium ion (\\(\\text{Na}^+\\))"],
     "B", "OSC", "easy",
     "• Hydrogen/hydronium ions (\\(\\text{H}_3\\text{O}^+\\)) produce all acidic reactions (litmus red, reaction with metals to produce \\(\\text{H}_2\\)).\nCorrect Choice is (B)."),

    ("""Which ion is universally responsible for basic properties and alkaline feel in aqueous solution?""",
     ["Hydrogen ion (\\(\\text{H}^+\\))",
      "Hydroxide ion (\\(\\text{OH}^-\\))",
      "Sulphate ion (\\(\\text{SO}_4^{2-}\\))",
      "Carbonate ion (\\(\\text{CO}_3^{2-}\\))"],
     "B", "OSC", "easy",
     "• Hydroxide ions (\\(\\text{OH}^-\\)) impart bitter taste, slippery soapy touch, and turn red litmus blue.\nCorrect Choice is (B)."),

    # 31-40: Fill in blanks and classifications
    ("""Fill in the blank: A hydrogen ion combines with a water molecule by forming a coordinate covalent bond to produce a ________ ion.""",
     ["Hydroxide", "Hydronium (\\(\\text{H}_3\\text{O}^+\\))", "Ammonium", "Carbonate"],
     "B", "OFB", "easy",
     "• \\(\\text{H}^+ + \\text{H}_2\\text{O} \\to \\text{H}_3\\text{O}^+\\) (hydronium ion).\nCorrect Choice is (B)."),

    ("""Fill in the blank: Bases that dissolve in water are specifically called ________.""",
     ["Acids", "Alkalis", "Salts", "Alloys"],
     "B", "OFB", "easy",
     "• Water-soluble bases are alkalis.\nCorrect Choice is (B)."),

    ("""Fill in the blank: The basicity of Nitric acid (\\(\\text{HNO}_3\\)) is ________.""",
     ["1 (Monobasic)", "2 (Dibasic)", "3 (Tribasic)", "4"],
     "A", "OFB", "easy",
     "• \\(\\text{HNO}_3\\) is monobasic (basicity = 1).\nCorrect Choice is (A)."),

    ("""What is the acidity of Magnesium Hydroxide (\\(\\text{Mg(OH)}_2\\), milk of magnesia)?""",
     ["1", "2 (Diacidic)", "3", "0"],
     "B", "OSC", "easy",
     "• \\(\\text{Mg(OH)}_2\\) yields two \\(\\text{OH}^-\\) ions per formula unit; its acidity is 2.\nCorrect Choice is (B)."),

    ("""Which organic acid is found in sour milk and yogurt?""",
     ["Citric acid", "Lactic acid", "Tartaric acid", "Oxalic acid"],
     "B", "OSC", "easy",
     "• Lactic acid is the natural organic weak acid present in curd and sour milk.\nCorrect Choice is (B)."),

    ("""Which organic acid is present in lemons and oranges?""",
     ["Acetic acid", "Citric acid", "Formic acid", "Tartaric acid"],
     "B", "OSC", "easy",
     "• Citrus fruits contain citric acid.\nCorrect Choice is (B)."),

    ("""Which acid is injected into the skin by an ant sting or nettle leaf hair, causing a burning pain?""",
     ["Hydrochloric acid", "Methanoic acid (Formic acid, \\(\\text{HCOOH}\\))", "Sulphuric acid", "Carbonic acid"],
     "B", "OSC", "easy",
     "• Ant stings deliver formic acid (methanoic acid).\nCorrect Choice is (B)."),

    ("""Which household mild basic substance can be applied to neutralize an acidic ant sting?""",
     ["Dilute sulphuric acid", "Baking soda (Sodium bicarbonate, \\(\\text{NaHCO}_3\\))", "Vinegar", "Lemon juice"],
     "B", "OSC", "easy",
     "• Baking soda is a mild base that neutralizes acidic formic acid, relieving pain.\nCorrect Choice is (B)."),

    ("""What is the chemical formula of Hydronium ion?""",
     ["\\(\\text{H}_2\\text{O}^+\\)", "\\(\\text{H}_3\\text{O}^+\\)", "\\(\\text{HO}^-\\)", "\\(\\text{H}_4\\text{O}^{2+}\\)"],
     "B", "OSC", "easy",
     "• Hydronium is \\(\\text{H}_3\\text{O}^+\\).\nCorrect Choice is (B)."),

    ("""Why is concentrated Sulphuric acid known as the 'King of Chemicals'?""",
     ["It is expensive and shiny",
      "It is used extensively in manufacturing fertilizers, synthetic fibers, paints, explosives, batteries, and across almost all chemical industries",
      "It dissolves gold at room temperature",
      "It was invented by royal kings"],
     "B", "OSC", "easy",
     "• Sulphuric acid's colossal industrial usage in producing fertilizers, chemicals, and plastics earned it the title 'King of Chemicals'.\nCorrect Choice is (B).")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("""What ion is released by an Arrhenius acid in water?""",
     ["\\(\\text{OH}^-\\)", "\\(\\text{H}^+\\) (or \\(\\text{H}_3\\text{O}^+\\))", "\\(\\text{Cl}^-\\)", "\\(\\text{Na}^+\\)"],
     "B", "OSC", "easy",
     "• Acids yield \\(\\text{H}^+\\) in water.\nCorrect Choice is (B)."),

    ("""What ion is released by an Arrhenius base in water?""",
     ["\\(\\text{H}^+\\)", "\\(\\text{OH}^-\\) (Hydroxide)", "\\(\\text{O}^{2-}\\)", "\\(\\text{H}_3\\text{O}^+\\)"],
     "B", "OSC", "easy",
     "• Bases yield \\(\\text{OH}^-\\) in water.\nCorrect Choice is (B)."),

    ("""Which of the following is a strong mineral acid?""",
     ["Acetic acid", "Carbonic acid", "Hydrochloric acid (\\(\\text{HCl}\\))", "Tartaric acid"],
     "C", "OSC", "easy",
     "• \\(\\text{HCl}\\) is a strong mineral acid.\nCorrect Choice is (C)."),

    ("""Which of the following is a strong alkali?""",
     ["\\(\\text{NH}_4\\text{OH}\\)", "\\(\\text{NaOH}\\) (Sodium hydroxide)", "\\(\\text{Al(OH)}_3\\)", "\\(\\text{Fe(OH)}_3\\)"],
     "B", "OSC", "easy",
     "• \\(\\text{NaOH}\\) is a strong water-soluble alkali.\nCorrect Choice is (B)."),

    ("""What is the basicity of Sulphuric Acid (\\(\\text{H}_2\\text{SO}_4\\))?""",
     ["1", "2 (Dibasic)", "3", "4"],
     "B", "OSC", "easy",
     "• Basicity is 2.\nCorrect Choice is (B)."),

    ("""What is the basicity of Phosphoric Acid (\\(\\text{H}_3\\text{PO}_4\\))?""",
     ["1", "2", "3 (Tribasic)", "4"],
     "C", "OSC", "easy",
     "• Basicity is 3.\nCorrect Choice is (C)."),

    ("""What is the acidity of Sodium Hydroxide (\\(\\text{NaOH}\\))?""",
     ["1 (Monoacidic)", "2", "3", "0"],
     "A", "OSC", "easy",
     "• Acidity is 1.\nCorrect Choice is (A)."),

    ("""What is the acidity of Aluminium Hydroxide (\\(\\text{Al(OH)}_3\\))?""",
     ["1", "2", "3 (Triacidic)", "4"],
     "C", "OSC", "easy",
     "• Acidity is 3.\nCorrect Choice is (C)."),

    ("""Are all alkalis bases?""",
     ["Yes, alkalis are water-soluble bases", "No, alkalis are acids", "Only at high pressure", "Never"],
     "A", "OSC", "easy",
     "• All alkalis are water-soluble bases.\nCorrect Choice is (A)."),

    ("""Are all bases alkalis?""",
     ["Yes", "No, only water-soluble bases are alkalis; insoluble bases are not alkalis", "Only when heated", "Yes, in vacuum"],
     "B", "OSC", "easy",
     "• Insoluble bases (like \\(\\text{Cu(OH)}_2\\)) are not alkalis.\nCorrect Choice is (B)."),

    ("""Which acid is found in vinegar?""",
     ["Citric acid", "Acetic acid (\\(\\text{CH}_3\\text{COOH}\\))", "Formic acid", "Lactic acid"],
     "B", "OSC", "easy",
     "• Vinegar is a \\(5\\text{--}8\\%\\) aqueous solution of acetic acid.\nCorrect Choice is (B)."),

    ("""Which acid is present in tamarind?""",
     ["Tartaric acid", "Oxalic acid", "Ascorbic acid", "Acetic acid"],
     "A", "OSC", "easy",
     "• Tamarind contains tartaric acid.\nCorrect Choice is (A)."),

    ("""Which acid is present in tomatoes?""",
     ["Oxalic acid", "Lactic acid", "Hydrochloric acid", "Sulphuric acid"],
     "A", "OSC", "easy",
     "• Tomatoes contain oxalic acid and citric acid.\nCorrect Choice is (A)."),

    ("""Which acid is produced in human stomach to assist digestion?""",
     ["Sulphuric acid", "Hydrochloric acid (\\(\\text{HCl}\\))", "Nitric acid", "Acetic acid"],
     "B", "OSC", "easy",
     "• Gastric juice contains \\(\\text{HCl}\\) (pH around 1.5 to 2.5) to activate pepsin.\nCorrect Choice is (B)."),

    ("""What medication is taken to neutralize excess stomach acidity (acid reflux)?""",
     ["Antibiotic", "Antacid (such as milk of magnesia or sodium bicarbonate)", "Analgesic", "Antiseptic"],
     "B", "OSC", "easy",
     "• Antacids are mild bases that neutralize stomach \\(\\text{HCl}\\).\nCorrect Choice is (B)."),

    ("""What color does moist blue litmus paper turn when dipped in an acid?""",
     ["Remains blue", "Turns red", "Turns yellow", "Turns colorless"],
     "B", "OSC", "easy",
     "• Acids turn blue litmus red.\nCorrect Choice is (B)."),

    ("""What color does moist red litmus paper turn when dipped in a base (alkali)?""",
     ["Remains red", "Turns blue", "Turns green", "Turns black"],
     "B", "OSC", "easy",
     "• Bases turn red litmus blue.\nCorrect Choice is (B)."),

    ("""What is the color of phenolphthalein indicator in an acidic solution?""",
     ["Pink", "Colorless", "Blue", "Yellow"],
     "B", "OSC", "easy",
     "• Phenolphthalein remains colorless in acidic or neutral solutions.\nCorrect Choice is (B)."),

    ("""What is the color of phenolphthalein indicator in a basic (alkaline) solution?""",
     ["Deep Pink (Magenta)", "Colorless", "Green", "Orange"],
     "A", "OSC", "easy",
     "• Phenolphthalein turns bright pink in basic solutions.\nCorrect Choice is (A)."),

    ("""What is the color of methyl orange indicator in an acidic solution?""",
     ["Yellow", "Red / Pink", "Blue", "Colorless"],
     "B", "OSC", "easy",
     "• Methyl orange turns red/pink in acidic solution.\nCorrect Choice is (B)."),

    ("""What is the color of methyl orange indicator in a basic solution?""",
     ["Yellow", "Red", "Blue", "Purple"],
     "A", "OSC", "easy",
     "• Methyl orange turns yellow in basic solution.\nCorrect Choice is (A)."),

    ("""State True or False: Distilled water conducts electricity strongly because it is an acid.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. Pure distilled water is neutral with virtually no free ions and is a poor electrical conductor.\nCorrect Choice is (B)."),

    ("""State True or False: Adding a small amount of dilute sulphuric acid to water makes it conduct electricity efficiently.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Acid provides mobile \\(\\text{H}_3\\text{O}^+\\) and \\(\\text{SO}_4^{2-}\\) ions that conduct current.\nCorrect Choice is (A)."),

    ("""What is the basicity of Carbonic Acid (\\(\\text{H}_2\\text{CO}_3\\))?""",
     ["1", "2 (Dibasic)", "3", "4"],
     "B", "OSC", "easy",
     "• \\(\\text{H}_2\\text{CO}_3\\) is dibasic.\nCorrect Choice is (B)."),

    ("""Which of the following is an insoluble base?""",
     ["\\(\\text{NaOH}\\)", "\\(\\text{KOH}\\)", "\\(\\text{Cu(OH)}_2\\)", "\\(\\text{Ba(OH)}_2\\)"],
     "C", "OSC", "easy",
     "• Copper(II) hydroxide is an insoluble pale blue precipitate.\nCorrect Choice is (C)."),

    ("""Fill in the blank: The process of adding water to an acid to reduce its concentration is called ________.""",
     ["Neutralization", "Dilution", "Distillation", "Sublimation"],
     "B", "OFB", "easy",
     "• Dilution reduces solute concentration per unit volume.\nCorrect Choice is (B)."),

    ("""Why should concentrated acid ALWAYS be added slowly to water with constant stirring, and NEVER water to concentrated acid?""",
     ["Water will decompose into gases",
      "Adding water to concentrated acid generates intense localized heat that can boil the water instantly, causing hazardous acid to splash onto face and hands, or shatter the glass beaker",
      "Because water is heavier than acid",
      "To change the color of the acid"],
     "B", "OSC", "medium",
     "• Dissolution of concentrated acid in water is strongly exothermic. Adding water causes instantaneous boiling and acid eruption.\nCorrect Choice is (B)."),

    ("""What type of bond forms between \\(\\text{H}^+\\) and \\(\\text{H}_2\\text{O}\\) to create a hydronium ion (\\(\\text{H}_3\\text{O}^+\\))?""",
     ["Ionic bond", "Coordinate covalent (dative) bond", "Metallic bond", "Van der Waals bond"],
     "B", "OSC", "medium",
     "• The lone pair of electrons on the oxygen atom in water is shared with the bare proton \\(\\text{H}^+\\) via a coordinate covalent bond.\nCorrect Choice is (B)."),

    ("""What is the formula for the hydronium ion?""",
     ["\\(\\text{H}_3\\text{O}^+\\)", "\\(\\text{H}_2\\text{O}^+\\)", "\\(\\text{OH}^-\\)", "\\(\\text{HO}_2^-\\修"],
     "A", "OSC", "easy",
     "• Hydronium ion is \\(\\text{H}_3\\text{O}^+\\).\nCorrect Choice is (A)."),

    ("""Which base is used as 'Milk of Magnesia' to relieve acidity in the human stomach?""",
     ["Sodium hydroxide", "Magnesium hydroxide (\\(\\text{Mg(OH)}_2\\))", "Calcium oxide", "Ammonium hydroxide"],
     "B", "OSC", "easy",
     "• Magnesium hydroxide \\(\\text{Mg(OH)}_2\\) is milk of magnesia.\nCorrect Choice is (B).")
]

# 12 Foundation Mock Questions (501-512) with rich embedded vector SVGs
foundation_data = [
    # 501: Hydronium Ion (H3O+) Formation
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Hydronium Ion (H₃O⁺) Formation</text>
  <!-- Water Molecule -->
  <circle cx="90" cy="115" r="30" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="82" y="112" fill="#38bdf8" font-size="14" font-weight="bold">O</text>
  <text x="75" y="130" fill="#93c5fd" font-size="9">Lone Pair : :</text>
  <!-- Bare Proton -->
  <circle cx="170" cy="80" r="14" fill="#ef4444" stroke="#f87171" stroke-width="2"/>
  <text x="162" y="85" fill="#fff" font-size="12" font-weight="bold">H⁺</text>
  <!-- Arrow -->
  <path d="M 115 105 Q 140 100 155 85" fill="none" stroke="#fde047" stroke-width="2.5" stroke-dasharray="3 3"/>
  <text x="140" y="135" fill="#fde047" font-size="14">→</text>
  <!-- Hydronium Result -->
  <circle cx="250" cy="115" r="38" fill="#1e293b" stroke="#10b981" stroke-width="2.5"/>
  <text x="232" y="112" fill="#10b981" font-size="14" font-weight="bold">H₃O⁺</text>
  <text x="215" y="132" fill="#86efac" font-size="9">Hydronium Ion</text>
  <text x="45" y="195" fill="#cbd5e1" font-size="10">Coordinate covalent bond formed by oxygen lone pair donating to H⁺</text>
</svg>
</div>
In the molecular reaction above, why does a bare hydrogen ion (\\(\\text{H}^+\\)) never remain unbonded in aqueous solution, immediately forming a hydronium ion (\\(\\text{H}_3\\text{O}^+\\))?""",
     ["Because hydrogen turns into an electron",
      "Because a bare proton has an extraordinarily small radius (\\(\\sim 10^{-15}\\text{ m}\\)) and colossal positive charge density, which strongly attracts and binds to the lone electron pair of a polar water molecule",
      "Because water molecules are acidic by nature",
      "Because hydrogen ions are repelled by air"],
     "B", "OSC", "hard",
     "• A bare proton \\(\\text{H}^+\\) is a naked atomic nucleus with infinite electric field gradient at atomic distances; it instantly coordinates with water's oxygen lone pair to form \\(\\text{H}_3\\text{O}^+\\).\nCorrect Choice is (B)."),

    # 502: Strong vs Weak Acid Dissociation Comparison
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Strong Acid (HCl) vs Weak Acid (CH₃COOH)</text>
  <!-- Left: Strong Acid -->
  <rect x="25" y="55" width="135" height="100" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="75" fill="#34d399" font-size="11" font-weight="bold">Strong Acid (HCl)</text>
  <text x="35" y="95" fill="#cbd5e1" font-size="9">• 100% Dissociation (α ≈ 1)</text>
  <text x="35" y="112" fill="#fde047" font-size="10">All HCl → H⁺ + Cl⁻</text>
  <text x="35" y="135" fill="#38bdf8" font-size="9">Dense free mobile ions</text>
  <!-- Right: Weak Acid -->
  <rect x="180" y="55" width="135" height="100" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="190" y="75" fill="#fde047" font-size="11" font-weight="bold">Weak Acid (CH₃COOH)</text>
  <text x="190" y="95" fill="#cbd5e1" font-size="9">• Partial Ionization (α &lt; 5%)</text>
  <text x="190" y="112" fill="#cbd5e1" font-size="9">CH₃COOH ⇌ H⁺ + CH₃COO⁻</text>
  <text x="190" y="135" fill="#ef4444" font-size="9">Mostly intact molecules</text>
  <text x="40" y="185" fill="#93c5fd" font-size="10">Bulb glows brightly in HCl; glows dimly in CH₃COOH</text>
</svg>
</div>
In an electrical conductivity test using a light bulb, why does a \\(0.1\\text{ M}\\) solution of \\(\\text{HCl}\\) cause the bulb to glow brightly while a \\(0.1\\text{ M}\\) solution of \\(\\text{CH}_3\\text{COOH}\\) causes only a faint glow?""",
     ["Because \\(\\text{HCl}\\) has more heavy atoms",
      "Because \\(\\text{HCl}\\) is a strong acid that dissociates completely into a high concentration of mobile ions, whereas \\(\\text{CH}_3\\text{COOH}\\) is a weak acid that ionizes only slightly (low ion concentration)",
      "Because acetic acid consumes electricity",
      "Because hydrochloric acid is flammable"],
     "B", "OSC", "medium",
     "• Electrical current through an electrolyte depends on ion concentration. Full ionization in \\(\\text{HCl}\\) yields abundant charge carriers (bright glow); partial ionization in acetic acid yields few ions (dim glow).\nCorrect Choice is (B)."),

    # 503: Basicity Ladder (Mono, Di, Tri)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="90" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Acid Basicity Hierarchy</text>
  <!-- Monobasic -->
  <rect x="25" y="55" width="85" height="90" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="32" y="75" fill="#38bdf8" font-size="10" font-weight="bold">Monobasic (1)</text>
  <text x="32" y="95" fill="#cbd5e1" font-size="9">Yields 1 H⁺</text>
  <text x="32" y="115" fill="#fde047" font-size="10">HCl, HNO₃</text>
  <text x="32" y="132" fill="#fde047" font-size="10">CH₃COOH</text>
  <!-- Dibasic -->
  <rect x="125" y="55" width="90" height="90" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="135" y="75" fill="#34d399" font-size="10" font-weight="bold">Dibasic (2)</text>
  <text x="135" y="95" fill="#cbd5e1" font-size="9">Yields 2 H⁺</text>
  <text x="135" y="115" fill="#fde047" font-size="10">H₂SO₄</text>
  <text x="135" y="132" fill="#fde047" font-size="10">H₂CO₃</text>
  <!-- Tribasic -->
  <rect x="230" y="55" width="85" height="90" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="240" y="75" fill="#fde047" font-size="10" font-weight="bold">Tribasic (3)</text>
  <text x="240" y="95" fill="#cbd5e1" font-size="9">Yields 3 H⁺</text>
  <text x="240" y="115" fill="#fde047" font-size="10">H₃PO₄</text>
  <text x="240" y="132" fill="#94a3b8" font-size="8">Phosphoric</text>
  <text x="40" y="185" fill="#cbd5e1" font-size="10">Basicity = number of ionizable H⁺ ions per acid molecule</text>
</svg>
</div>
How many moles of \\(\\text{NaOH}\\) are required to completely neutralize \\(1\\text{ mole}\\) of Phosphoric Acid (\\(\\text{H}_3\\text{PO}_4\\))?""",
     ["\\(1\\text{ mole}\\)", "\\(2\\text{ moles}\\)", "\\(3\\text{ moles}\\)", "\\(6\\text{ moles}\\)"],
     "C", "OSC", "medium",
     "• Because \\(\\text{H}_3\\text{PO}_4\\) is a tribasic acid, each molecule releases three \\(\\text{H}^+\\) ions: \\(\\text{H}_3\\text{PO}_4 + 3\\text{NaOH} \\to \\text{Na}_3\\text{PO}_4 + 3\\text{H}_2\\text{O}\\). Thus, 3 moles of \\(\\text{NaOH}\\) are needed.\nCorrect Choice is (C)."),

    # 504: Alkali vs Base Venn Diagram
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Bases vs Alkalis: Venn Relation</text>
  <!-- Outer Ellipse: BASES -->
  <ellipse cx="170" cy="115" rx="130" ry="65" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="55" y="85" fill="#38bdf8" font-size="12" font-weight="bold">ALL BASES</text>
  <text x="50" y="105" fill="#cbd5e1" font-size="9">Insoluble Bases:</text>
  <text x="50" y="122" fill="#cbd5e1" font-size="9">• Cu(OH)₂ (Blue)</text>
  <text x="50" y="138" fill="#cbd5e1" font-size="9">• Fe(OH)₃ (Brown)</text>
  <text x="50" y="154" fill="#cbd5e1" font-size="9">• Al(OH)₃ (White)</text>
  <!-- Inner Ellipse: ALKALIS -->
  <ellipse cx="230" cy="115" rx="60" ry="45" fill="#334155" stroke="#10b981" stroke-width="2.5"/>
  <text x="200" y="95" fill="#34d399" font-size="11" font-weight="bold">ALKALIS</text>
  <text x="185" y="115" fill="#fde047" font-size="9">Water Soluble:</text>
  <text x="185" y="130" fill="#cbd5e1" font-size="9">• NaOH, KOH</text>
  <text x="185" y="145" fill="#cbd5e1" font-size="9">• NH₄OH</text>
  <text x="45" y="200" fill="#34d399" font-size="10">"All alkalis are bases, but all bases are not alkalis"</text>
</svg>
</div>
Which scientific statement accurately expresses the chemical relationship depicted in the Venn diagram above?""",
     ["All bases dissolve completely in water",
      "All alkalis are bases because they contain basic hydroxide groups, but insoluble bases (like \\(\\text{Cu(OH)}_2\\)) cannot be classified as alkalis",
      "Alkalis contain no hydroxide ions",
      "Insoluble bases turn blue litmus red"],
     "B", "OSC", "easy",
     "• Alkalis represent the water-soluble subset of bases. Insoluble metal hydroxides remain bases but are not alkalis.\nCorrect Choice is (B)."),

    # 505: Electrical Conductivity Circuit Apparatus
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Electrolyte Conductivity Test Circuit</text>
  <!-- Beaker with solution -->
  <path d="M 100 80 L 100 170 A 10 10 0 0 0 110 180 L 230 180 A 10 10 0 0 0 240 170 L 240 80" fill="none" stroke="#94a3b8" stroke-width="2"/>
  <rect x="102" y="115" width="136" height="62" fill="#38bdf8" opacity="0.3"/>
  <!-- Two Carbon/Iron Rods (Electrodes) -->
  <rect x="130" y="90" width="14" height="80" fill="#475569" stroke="#64748b"/>
  <rect x="195" y="90" width="14" height="80" fill="#475569" stroke="#64748b"/>
  <!-- Battery and Bulb -->
  <line x1="137" y1="90" x2="137" y2="50" stroke="#fde047" stroke-width="2"/>
  <line x1="137" y1="50" x2="160" y2="50" stroke="#fde047" stroke-width="2"/>
  <circle cx="170" cy="50" r="10" fill="#fef08a"/>
  <text x="166" y="54" fill="#0f172a" font-size="10" font-weight="bold">💡</text>
  <line x1="180" y1="50" x2="202" y2="50" stroke="#fde047" stroke-width="2"/>
  <line x1="202" y1="50" x2="202" y2="90" stroke="#fde047" stroke-width="2"/>
  <text x="120" y="205" fill="#34d399" font-size="10">Dilute HCl solution completes circuit via mobile H₃O⁺ and Cl⁻ ions</text>
</svg>
</div>
When the beaker in the conductivity apparatus is filled with a solution of glucose (\\(\\text{C}_6\\text{H}_{12}\\text{O}_6\\)) in pure water, the bulb fails to glow. Why?""",
     ["Glucose coats the electrodes with insulating plastic",
      "Glucose dissolves as neutral covalent molecules without dissociating into mobile ions, leaving the circuit electrically open",
      "Glucose absorbs electric voltage into caloric energy",
      "The bulb burned out"],
     "B", "OSC", "medium",
     "• Electrical conduction through a liquid requires mobile ions. Covalent molecules like glucose and urea do not ionize in water and cannot conduct current.\nCorrect Choice is (B)."),

    # 506: Dilution Exothermic Reaction Rule
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Acid Dilution Safety Protocol</text>
  <!-- Correct Protocol -->
  <rect x="25" y="55" width="135" height="100" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="75" fill="#34d399" font-size="11" font-weight="bold">✓ SAFE METHOD</text>
  <text x="35" y="95" fill="#cbd5e1" font-size="9">• Acid slowly into Water</text>
  <text x="35" y="112" fill="#cbd5e1" font-size="9">• Constant stirring</text>
  <text x="35" y="130" fill="#fde047" font-size="9">• Large water volume</text>
  <text x="35" y="145" fill="#fde047" font-size="9">  absorbs heat safely</text>
  <!-- Dangerous Protocol -->
  <rect x="180" y="55" width="135" height="100" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="190" y="75" fill="#f87171" font-size="11" font-weight="bold">✗ DEADLY ERROR</text>
  <text x="190" y="95" fill="#cbd5e1" font-size="9">• Water into Con. Acid</text>
  <text x="190" y="112" fill="#ef4444" font-size="9">• Instant steam explosion!</text>
  <text x="190" y="130" fill="#fca5a5" font-size="9">• Acid splashes on face</text>
  <text x="190" y="145" fill="#fca5a5" font-size="9">• Beaker shatters</text>
  <text x="45" y="185" fill="#fde047" font-size="10" font-weight="bold">Always add ACID to WATER, never water to acid!</text>
</svg>
</div>
What severe physical phenomenon occurs if someone recklessly pours water directly into a beaker of concentrated sulphuric acid?""",
     ["The acid solidifies into ice",
      "The hydration of sulphuric acid is violently exothermic; localized heat instantly vaporizes the small droplets of water into steam bubbles that erupt, splashing caustic acid into the eyes and face",
      "The acid turns into harmless carbon dioxide",
      "The beaker becomes magnetically charged"],
     "B", "OSC", "medium",
     "• The large enthalpy of hydration causes water to flash boil instantaneously, spraying boiling concentrated acid outward with explosive force.\nCorrect Choice is (B)."),

    # 507: Dry HCl vs Moist HCl Litmus Test
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Dry HCl Gas vs Litmus Paper</text>
  <!-- Dry Litmus Paper -->
  <rect x="35" y="55" width="125" height="85" fill="#1e293b" stroke="#60a5fa" rx="4"/>
  <text x="45" y="78" fill="#60a5fa" font-size="10" font-weight="bold">Dry Blue Litmus</text>
  <text x="45" y="98" fill="#cbd5e1" font-size="9">+ Dry HCl Gas</text>
  <text x="45" y="125" fill="#93c5fd" font-size="11" font-weight="bold">NO COLOR CHANGE</text>
  <!-- Moist Litmus Paper -->
  <rect x="180" y="55" width="125" height="85" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="190" y="78" fill="#f87171" font-size="10" font-weight="bold">Moist Blue Litmus</text>
  <text x="190" y="98" fill="#cbd5e1" font-size="9">+ HCl Gas dissolves</text>
  <text x="190" y="125" fill="#ef4444" font-size="11" font-weight="bold">TURNS BRIGHT RED!</text>
  <text x="45" y="175" fill="#34d399" font-size="10">Ionization into H⁺ ions strictly requires presence of water</text>
</svg>
</div>
Why does dry hydrogen chloride gas fail to turn dry blue litmus paper red, but immediately turns moist blue litmus paper red?""",
     ["Because dry paper is immune to acids",
      "Because \\(\\text{HCl}\\) is a covalent gas that only ionizes into acidic \\(\\text{H}^+\\) (or \\(\\text{H}_3\\text{O}^+\\)) ions when dissolved in water",
      "Because water contains red dye",
      "Because chlorine gas bleaches dry paper"],
     "B", "OSC", "easy",
     "• Acidic properties are manifested solely by \\(\\text{H}^+\\) ions. In the absence of moisture, \\(\\text{HCl}\\) remains an unionized covalent molecule.\nCorrect Choice is (B)."),

    # 508: Dissociation Degree (Alpha) Mathematical Spectrum
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Degree of Dissociation Scale (α)</text>
  <!-- Horizontal Spectrum Bar -->
  <rect x="40" y="70" width="260" height="30" fill="#334155" rx="3"/>
  <rect x="40" y="70" width="30" height="30" fill="#ef4444" rx="2"/>
  <text x="42" y="90" fill="#fff" font-size="9">α=0</text>
  <rect x="250" y="70" width="50" height="30" fill="#10b981" rx="2"/>
  <text x="255" y="90" fill="#fff" font-size="9">α ≈ 1</text>
  <!-- Labels -->
  <text x="35" y="125" fill="#ef4444" font-size="10">Non-electrolyte</text>
  <text x="35" y="140" fill="#cbd5e1" font-size="8">(Pure water, sugar)</text>
  <text x="120" y="125" fill="#fde047" font-size="10">Weak Acid (α &lt; 0.05)</text>
  <text x="120" y="140" fill="#cbd5e1" font-size="8">(Acetic, Carbonic)</text>
  <text x="220" y="125" fill="#34d399" font-size="10">Strong Acid (α ≈ 1)</text>
  <text x="220" y="140" fill="#cbd5e1" font-size="8">(HCl, HNO₃, H₂SO₄)</text>
  <text x="45" y="180" fill="#38bdf8" font-size="10">α = (Molecules dissociated) / (Total molecules dissolved)</text>
</svg>
</div>
If out of \\(1000\\) molecules of an acid dissolved in water, only \\(12\\) molecules dissociate into ions at equilibrium, what is its degree of dissociation (\\(\\alpha\\)) and classification?""",
     ["\\(\\alpha = 1.2\\), Strong acid",
      "\\(\\alpha = 0.012\\ (1.2\\%)\\), Weak acid",
      "\\(\\alpha = 12\\), Concentrated acid",
      "\\(\\alpha = 0\\), Non-electrolyte"],
     "B", "OSC", "medium",
     "• \\(\\alpha = \\frac{12}{1000} = 0.012 = 1.2\\%\\). Since \\(\\alpha \\ll 1\\), it is a weak acid.\nCorrect Choice is (B)."),

    # 509: Multistage Dissociation of H2SO4
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="70" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Two-Stage Ionization of H₂SO₄</text>
  <!-- Stage 1 -->
  <rect x="30" y="50" width="280" height="45" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="40" y="70" fill="#34d399" font-size="10" font-weight="bold">Stage 1 (Complete, 100%):</text>
  <text x="40" y="86" fill="#cbd5e1" font-size="10">H₂SO₄ ⟶ H⁺ + HSO₄⁻ (Bisulphate ion)</text>
  <!-- Stage 2 -->
  <rect x="30" y="105" width="280" height="45" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="40" y="125" fill="#fde047" font-size="10" font-weight="bold">Stage 2 (Partial Equilibrium):</text>
  <text x="40" y="141" fill="#cbd5e1" font-size="10">HSO₄⁻ ⇌ H⁺ + SO₄²⁻ (Sulphate ion)</text>
  <text x="40" y="180" fill="#38bdf8" font-size="10">Overall complete dissociation yields 2 H⁺ per molecule</text>
</svg>
</div>
What are the two distinct acid radicals (anions) produced during the stepwise ionization of Sulphuric Acid in water?""",
     ["Sulphide (\\(\\text{S}^{2-}\\)) and Sulphite (\\(\\text{SO}_3^{2-}\\))",
      "Bisulphate (Hydrogen sulphate, \\(\\text{HSO}_4^-\\)) and Sulphate (\\(\\text{SO}_4^{2-}\\))",
      "Thiosulphate and Persulphate",
      "Oxide and Hydroxide"],
     "B", "OSC", "easy",
     "• In stage 1, loss of one proton forms bisulphate (\\(\\text{HSO}_4^-\\)); in stage 2, loss of the second proton forms sulphate (\\(\\text{SO}_4^{2-}\\)).\nCorrect Choice is (B)."),

    # 510: Concentrated Weak Acid vs Dilute Strong Acid
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Concentration vs Strength Paradox</text>
  <!-- Case A: Glacial Acetic Acid -->
  <rect x="25" y="55" width="135" height="100" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="35" y="75" fill="#fde047" font-size="10" font-weight="bold">Glacial Acetic Acid</text>
  <text x="35" y="95" fill="#cbd5e1" font-size="9">• 100% pure CH₃COOH</text>
  <text x="35" y="110" fill="#cbd5e1" font-size="9">• Highly CONCENTRATED</text>
  <text x="35" y="130" fill="#ef4444" font-size="10" font-weight="bold">Yet a WEAK acid!</text>
  <!-- Case B: 0.001M HCl -->
  <rect x="180" y="55" width="135" height="100" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="190" y="75" fill="#34d399" font-size="10" font-weight="bold">0.001 M HCl Solution</text>
  <text x="190" y="95" fill="#cbd5e1" font-size="9">• 99.99% water</text>
  <text x="190" y="110" fill="#cbd5e1" font-size="9">• Highly DILUTE</text>
  <text x="190" y="130" fill="#34d399" font-size="10" font-weight="bold">Yet a STRONG acid!</text>
  <text x="40" y="185" fill="#38bdf8" font-size="10">Strength = % ionization | Concentration = solute/volume</text>
</svg>
</div>
Why is pure glacial acetic acid (\\(100\\%\\ \\text{CH}_3\\text{COOH}\\)) still classified scientifically as a WEAK acid?""",
     ["Because it contains no carbon",
      "Because 'weak' refers strictly to the percentage of molecules that dissociate into ions (which is very low for acetic acid), regardless of how concentrated it is",
      "Because it tastes sweet",
      "Because it does not dissolve in water"],
     "B", "OSC", "medium",
     "• Strength is solely defined by degree of dissociation (\\(\\alpha\\)). Acetic acid ionizes poorly even at 100% concentration, remaining an intrinsically weak acid.\nCorrect Choice is (B)."),

    # 511: Organic Acids in Natural Sources Infographic
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Natural Organic Acids in Food</text>
  <!-- Grid of 4 foods -->
  <rect x="25" y="50" width="135" height="45" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="35" y="68" fill="#38bdf8" font-size="10" font-weight="bold">Curd / Yogurt:</text>
  <text x="35" y="85" fill="#cbd5e1" font-size="9">Lactic Acid</text>
  <rect x="180" y="50" width="135" height="45" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="190" y="68" fill="#fde047" font-size="10" font-weight="bold">Citrus Fruits:</text>
  <text x="190" y="85" fill="#cbd5e1" font-size="9">Citric Acid</text>
  <rect x="25" y="105" width="135" height="45" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="35" y="123" fill="#34d399" font-size="10" font-weight="bold">Tamarind / Grapes:</text>
  <text x="35" y="140" fill="#cbd5e1" font-size="9">Tartaric Acid</text>
  <rect x="180" y="105" width="135" height="45" fill="#1e293b" stroke="#ef4444" rx="3"/>
  <text x="190" y="123" fill="#f87171" font-size="10" font-weight="bold">Ant / Nettle Sting:</text>
  <text x="190" y="140" fill="#cbd5e1" font-size="9">Formic Acid (Methanoic)</text>
  <text x="45" y="185" fill="#93c5fd" font-size="10">All natural organic food acids are non-toxic WEAK acids</text>
</svg>
</div>
Why are organic acids present in foods (such as citric acid in lemons or lactic acid in curd) safe for human consumption, whereas mineral acids like concentrated sulphuric acid are highly corrosive and dangerous?""",
     ["Organic acids contain vitamins that kill acid ions",
      "Organic acids are weak acids that dissociate only slightly, releasing very low concentrations of \\(\\text{H}^+\\) ions that do not destroy living human tissues",
      "Mineral acids have negative temperature",
      "Food acids are neutralized by saliva completely before touching the tongue"],
     "B", "OSC", "easy",
     "• Organic acids have very low ionization constants; their low hydrogen ion concentration imparts pleasant sourness without chemically dehydrating or oxidizing organic tissues.\nCorrect Choice is (B)."),

    # 512: Antacid Neutralization Mechanism in Stomach
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Antacid Neutralization Reaction</text>
  <!-- Stomach with excess acid -->
  <rect x="30" y="55" width="125" height="70" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="40" y="75" fill="#f87171" font-size="10" font-weight="bold">Hyperacidity:</text>
  <text x="40" y="95" fill="#cbd5e1" font-size="9">Excess stomach HCl</text>
  <text x="40" y="110" fill="#ef4444" font-size="9">Causes burning &amp; ulcer</text>
  <!-- Plus sign -->
  <text x="162" y="95" fill="#fff" font-size="14">+</text>
  <!-- Antacid Dose -->
  <rect x="185" y="55" width="125" height="70" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="195" y="75" fill="#34d399" font-size="10" font-weight="bold">Antacid Base:</text>
  <text x="195" y="95" fill="#cbd5e1" font-size="9">Mg(OH)₂ / NaHCO₃</text>
  <text x="195" y="110" fill="#34d399" font-size="9">Mild, non-corrosive</text>
  <!-- Neutralization equation -->
  <rect x="30" y="140" width="280" height="40" fill="#334155" stroke="#38bdf8" rx="3"/>
  <text x="45" y="165" fill="#38bdf8" font-size="11" font-weight="bold">Mg(OH)₂ + 2 HCl ⟶ MgCl₂ + 2 H₂O (Neutralization)</text>
</svg>
</div>
Why is Sodium Hydroxide (\\(\\text{NaOH}\\)) NEVER prescribed as an antacid for stomach acidity, even though it can neutralize \\(\\text{HCl}\\)?""",
     ["Because \\(\\text{NaOH}\\) is too expensive",
      "Because \\(\\text{NaOH}\\) is a caustic, highly corrosive strong alkali that would severely burn and destroy the mouth, esophagus, and stomach lining; only mild, non-caustic bases like \\(\\text{Mg(OH)}_2\\) are safe",
      "Because \\(\\text{NaOH}\\) produces acid when swallowed",
      "Because \\(\\text{NaOH}\\) is a gas"],
     "B", "OSC", "easy",
     "• \\(\\text{NaOH}\\) is dangerously caustic (lye) and dissolves animal tissue. Antacids must be mild, sparingly soluble bases like \\(\\text{Mg(OH)}_2\\) or \\(\\text{Al(OH)}_3\\).\nCorrect Choice is (B).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-5-5.1-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-5-5.1-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-5-5.1-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch5_topic1.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
