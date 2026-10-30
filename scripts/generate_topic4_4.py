# scripts/generate_topic4_4.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-4-4.4"
CHAPTER_NUM = 4

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: Radicals: Simple vs Composite, Basic vs Acidic
    ("""In chemistry, what is a 'RADICAL'?""",
     ["An uncharged inert noble gas atom",
      "An atom or group of atoms carrying a net positive or negative charge that behaves as a single distinct unit in chemical reactions",
      "A mechanical mixture of two metals",
      "A radio wave emitted by radioactive nuclei"],
     "B", "OSC", "easy",
     "• A radical is an electrically charged atom or group of covalently bonded atoms that reacts as a single cohesive chemical entity.\nCorrect Choice is (B)."),

    ("""What distinguishes a 'SIMPLE RADICAL' from a 'COMPOSITE (POLYATOMIC) RADICAL'?""",
     ["Simple radicals have positive charge, composite have negative charge",
      "A simple radical is formed from a single atom, whereas a composite radical is formed from a group of atoms of different elements carrying a net charge",
      "Simple radicals exist only in solids, composite only in liquids",
      "There is no difference between them"],
     "B", "OSC", "easy",
     "• Simple radicals consist of a single atom (e.g. \\(\\text{Na}^+\\), \\(\\text{Cl}^-\\)), while composite radicals contain multiple atoms (e.g. \\(\\text{SO}_4^{2-}\\), \\(\\text{NH}_4^+\\)).\nCorrect Choice is (B)."),

    ("""Which of the following is an example of a COMPOSITE (POLYATOMIC) radical?""",
     ["Chloride ion (\\(\\text{Cl}^-\\))",
      "Sodium ion (\\(\\text{Na}^+\\))",
      "Sulphate ion (\\(\\text{SO}_4^{2-}\\))",
      "Oxide ion (\\(\\text{O}^{2-}\\))"],
     "C", "OSC", "easy",
     "• Sulphate (\\(\\text{SO}_4^{2-}\\)) consists of one sulphur atom and four oxygen atoms carrying a net \\(-2\\) charge, making it a composite radical.\nCorrect Choice is (C)."),

    ("""Why are positively charged ions (cations) called 'BASIC RADICALS'?""",
     ["Because they taste bitter like bases",
      "Because they are generally derived by the dissociation of bases in aqueous solution (e.g. \\(\\text{Na}^+\\) from \\(\\text{NaOH}\\))",
      "Because they neutralize neutral water",
      "Because they contain basic electrons"],
     "B", "OSC", "easy",
     "• When bases dissociate (e.g. \\(\\text{KOH} \\to \\text{K}^+ + \\text{OH}^-\\)), the cation represents the base-derived component, termed the basic radical.\nCorrect Choice is (B)."),

    ("""Why are negatively charged ions (anions) called 'ACIDIC RADICALS'?""",
     ["Because they turn red litmus blue",
      "Because they are derived by the dissociation of acids in aqueous solution (e.g. \\(\\text{Cl}^-\\) from \\(\\text{HCl}\\), \\(\\text{SO}_4^{2-}\\) from \\(\\text{H}_2\\text{SO}_4\\))",
      "Because they only react with organic acids",
      "Because their pH is always zero"],
     "B", "OSC", "easy",
     "• When acids dissociate in water, they release anions (such as \\(\\text{NO}_3^-\\), \\(\\text{Cl}^-\\)), which are termed acidic radicals.\nCorrect Choice is (B)."),

    ("""Which of the following is a positively charged COMPOSITE radical (basic radical)?""",
     ["Carbonate (\\(\\text{CO}_3^{2-}\\))",
      "Ammonium (\\(\\text{NH}_4^+\\))",
      "Nitrate (\\(\\text{NO}_3^-\\))",
      "Hydroxide (\\(\\text{OH}^-\\))"],
     "B", "OSC", "easy",
     "• Ammonium (\\(\\text{NH}_4^+\\)) is a polyatomic basic radical carrying a net positive charge \\(+1\\).\nCorrect Choice is (B)."),

    ("""What is the charge and valency of the Hydroxide radical (\\(\\text{OH}^-\\))?""",
     ["Charge \\(-1\\), Valency \\(1\\)",
      "Charge \\(-2\\), Valency \\(2\\)",
      "Charge \\(+1\\), Valency \\(1\\)",
      "Charge \\(0\\), Valency \\(0\\)"],
     "A", "OSC", "easy",
     "• Hydroxide is a monovalent acidic radical with a single negative charge: \\(\\text{OH}^-\\), valency 1.\nCorrect Choice is (A)."),

    ("""What is the chemical formula and valency of the Carbonate radical?""",
     ["\\(\\text{CO}_3^-\\), valency 1",
      "\\(\\text{CO}_3^{2-}\\), valency 2",
      "\\(\\text{HCO}_3^{2-}\\), valency 2",
      "\\(\\text{CO}_2^{2-}\\), valency 2"],
     "B", "OSC", "easy",
     "• Carbonate is a divalent acidic radical: \\(\\text{CO}_3^{2-}\\), valency 2.\nCorrect Choice is (B)."),

    ("""What is the formula and valency of the Phosphate radical?""",
     ["\\(\\text{PO}_4^-\\), valency 1",
      "\\(\\text{PO}_3^{2-}\\), valency 2",
      "\\(\\text{PO}_4^{3-}\\), valency 3",
      "\\(\\text{P}^{3-}\\), valency 3"],
     "C", "OSC", "easy",
     "• Phosphate is a trivalent composite acidic radical: \\(\\text{PO}_4^{3-}\\), valency 3.\nCorrect Choice is (C)."),

    ("""Which of the following is a MONOVALENT acidic radical?""",
     ["Sulphate (\\(\\text{SO}_4^{2-}\\))",
      "Nitrate (\\(\\text{NO}_3^-\\))",
      "Carbonate (\\(\\text{CO}_3^{2-}\\))",
      "Oxide (\\(\\text{O}^{2-}\\))"],
     "B", "OSC", "easy",
     "• Nitrate (\\(\\text{NO}_3^-\\)) carries a single negative charge and has valency 1.\nCorrect Choice is (B)."),

    # 11-20: Criss-cross valency method and formula derivation
    ("""In writing the chemical formula of a binary compound using the criss-cross method, which radical is written on the LEFT?""",
     ["Acidic radical (anion)",
      "Basic radical (cation)",
      "Whichever radical has the larger molecular mass",
      "Either can be written arbitrarily on the left"],
     "B", "OSC", "easy",
     "• By IUPAC rules, the basic radical (positively charged cation) is written first on the left, followed by the acidic radical on the right.\nCorrect Choice is (B)."),

    ("""What is the correct chemical formula for Sodium Sulphate?""",
     ["\\(\\text{NaSO}_4\\)", "\\(\\text{Na}_2\\text{SO}_4\\)", "\\(\\text{Na}(\\text{SO}_4)_2\\)", "\\(\\text{Na}_2\\text{S}\\)"],
     "B", "OSC", "easy",
     "• Sodium is monovalent (\\(\\text{Na}^+\\), valency 1) and Sulphate is divalent (\\(\\text{SO}_4^{2-}\\), valency 2). Criss-crossing gives \\(\\text{Na}_2\\text{SO}_4\\).\nCorrect Choice is (B)."),

    ("""What is the correct chemical formula for Calcium Hydroxide (slaked lime)?""",
     ["\\(\\text{CaOH}\\)", "\\(\\text{CaOH}_2\\)", "\\(\\text{Ca(OH)}_2\\)", "\\(\\text{Ca}_2\\text{OH}\\)"],
     "C", "OSC", "easy",
     "• Calcium is divalent (\\(\\text{Ca}^{2+}\\), valency 2) and hydroxide is monovalent (\\(\\text{OH}^-\\), valency 1). Criss-crossing requires parentheses around composite radical: \\(\\text{Ca(OH)}_2\\).\nCorrect Choice is (C)."),

    ("""Why must parentheses (brackets) be used when writing the formula \\(\\text{Ca(OH)}_2\\)?""",
     ["To make the formula look neat",
      "To indicate that the subscript 2 multiplies both the Oxygen and Hydrogen atoms of the polyatomic hydroxide radical, rather than hydrogen alone (as in \\(\\text{CaOH}_2\\))",
      "Because calcium is a metal",
      "Because hydroxide contains hydrogen"],
     "B", "OSC", "medium",
     "• Without brackets, writing \\(\\text{CaOH}_2\\) would incorrectly indicate 1 Ca, 1 O, and 2 H. The brackets \\(\\text{Ca(OH)}_2\\) ensure the entire \\(\\text{OH}\\) group is multiplied by 2.\nCorrect Choice is (B)."),

    ("""What is the correct chemical formula for Aluminium Oxide?""",
     ["\\(\\text{AlO}\\)", "\\(\\text{Al}_2\\text{O}_3\\)", "\\(\\text{Al}_3\\text{O}_2\\)", "\\(\\text{AlO}_2\\)"],
     "B", "OSC", "easy",
     "• Aluminium is trivalent (\\(\\text{Al}^{3+}\\), valency 3) and Oxygen is divalent (\\(\\text{O}^{2-}\\), valency 2). Criss-cross gives \\(\\text{Al}_2\\text{O}_3\\).\nCorrect Choice is (B)."),

    ("""What is the correct chemical formula for Aluminium Sulphate?""",
     ["\\(\\text{AlSO}_4\\)", "\\(\\text{Al}_2\\text{SO}_4\\)", "\\(\\text{Al}_2(\\text{SO}_4)_3\\)", "\\(\\text{Al}_3(\\text{SO}_4)_2\\)"],
     "C", "OSC", "easy",
     "• Aluminium (valency 3) and Sulphate (valency 2) criss-cross to form \\(\\text{Al}_2(\\text{SO}_4)_3\\).\nCorrect Choice is (C)."),

    ("""What is the correct chemical formula for Ammonium Carbonate?""",
     ["\\(\\text{NH}_4\\text{CO}_3\\)",
      "\\((\\text{NH}_4)_2\\text{CO}_3\\)",
      "\\(\\text{NH}_4(\\text{CO}_3)_2\\)",
      "\\((\\text{NH}_4)_3\\text{CO}_3\\)"],
     "B", "OSC", "medium",
     "• Ammonium is \\(\\text{NH}_4^+\\) (valency 1), Carbonate is \\(\\text{CO}_3^{2-}\\) (valency 2). Criss-crossing gives \\((\\text{NH}_4)_2\\text{CO}_3\\).\nCorrect Choice is (B)."),

    ("""When the valencies of the basic and acidic radicals are identical (e.g. \\(\\text{Mg}^{2+}\\) and \\(\\text{O}^{2-}\\)), what simplification rule is applied?""",
     ["The valency numbers are multiplied together",
      "The common factor is divided out to give the simplest whole-number ratio (e.g. \\(2:2\\) simplifies to \\(1:1\\), writing \\(\\text{MgO}\\) rather than \\(\\text{Mg}_2\\text{O}_2\\))",
      "Both radicals are written inside brackets",
      "The compound cannot form"],
     "B", "OSC", "easy",
     "• Formula subscripts represent the lowest whole-number ratio of ions; \\(\\text{Mg}_2\\text{O}_2\\) simplifies to \\(\\text{MgO}\\).\nCorrect Choice is (B)."),

    ("""What is the chemical formula for Calcium Carbonate?""",
     ["\\(\\text{Ca}_2(\\text{CO}_3)_2\\)", "\\(\\text{CaCO}_3\\)", "\\(\\text{Ca}(\\text{CO}_3)_2\\)", "\\(\\text{Ca}_2\\text{CO}_3\\)"],
     "B", "OSC", "easy",
     "• Both Calcium (\\(\\text{Ca}^{2+}\\)) and Carbonate (\\(\\text{CO}_3^{2-}\\)) have valency 2; the \\(2:2\\) ratio simplifies to \\(1:1\\), giving \\(\\text{CaCO}_3\\).\nCorrect Choice is (B)."),

    ("""What is the correct chemical formula for Ferric Chloride (Iron(III) chloride)?""",
     ["\\(\\text{FeCl}\\)", "\\(\\text{FeCl}_2\\)", "\\(\\text{FeCl}_3\\)", "\\(\\text{Fe}_3\\text{Cl}\\)"],
     "C", "OSC", "easy",
     "• Ferric ion has valency 3 (\\(\\text{Fe}^{3+}\\)), and chloride has valency 1 (\\(\\text{Cl}^-\\)). Criss-crossing yields \\(\\text{FeCl}_3\\).\nCorrect Choice is (C)."),

    # 21-30: Formula writing and ionic charges
    ("""What is the chemical formula for Ferrous Chloride (Iron(II) chloride)?""",
     ["\\(\\text{FeCl}\\)", "\\(\\text{FeCl}_2\\)", "\\(\\text{FeCl}_3\\)", "\\(\\text{Fe}_2\\text{Cl}\\)"],
     "B", "OSC", "easy",
     "• Ferrous ion has valency 2 (\\(\\text{Fe}^{2+}\\)); chloride has valency 1. Criss-crossing yields \\(\\text{FeCl}_2\\).\nCorrect Choice is (B)."),

    ("""What is the chemical formula for Magnesium Phosphate?""",
     ["\\(\\text{MgPO}_4\\)", "\\(\\text{Mg}_2(\\text{PO}_4)_3\\)", "\\(\\text{Mg}_3(\\text{PO}_4)_2\\)", "\\(\\text{Mg}_3\\text{PO}_4\\)"],
     "C", "OSC", "medium",
     "• Magnesium is divalent (\\(\\text{Mg}^{2+}\\), valency 2) and Phosphate is trivalent (\\(\\text{PO}_4^{3-}\\), valency 3). Criss-crossing gives \\(\\text{Mg}_3(\\text{PO}_4)_2\\).\nCorrect Choice is (C)."),

    ("""What is the chemical formula for Sodium Bicarbonate (Sodium hydrogen carbonate)?""",
     ["\\(\\text{Na}_2\\text{HCO}_3\\)", "\\(\\text{NaHCO}_3\\)", "\\(\\text{Na}(\\text{HCO}_3)_2\\)", "\\(\\text{NaCO}_3\\)"],
     "B", "OSC", "easy",
     "• Sodium is \\(\\text{Na}^+\\) (valency 1), bicarbonate is \\(\\text{HCO}_3^-\\) (valency 1). The formula is \\(\\text{NaHCO}_3\\).\nCorrect Choice is (B)."),

    ("""What is the chemical formula for Potassium Permanganate?""",
     ["\\(\\text{KMnO}_4\\)", "\\(\\text{K}_2\\text{MnO}_4\\)", "\\(\\text{KMnO}_2\\)", "\\(\\text{K}(\\text{MnO}_4)_2\\)"],
     "A", "OSC", "easy",
     "• Potassium is \\(\\text{K}^+\\) (valency 1), Permanganate is \\(\\text{MnO}_4^-\\) (valency 1). Formula is \\(\\text{KMnO}_4\\).\nCorrect Choice is (A)."),

    ("""Assertion (A): In any stable ionic compound, the total positive charge of the basic radicals strictly equals the total negative charge of the acidic radicals.\nReason (R): Matter is macroscopically electrically neutral, so chemical compounds must carry zero net electrical charge.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "• Electrical neutrality is the physical basis of the criss-cross valency method: \\(\\sum q_+ + \\sum q_- = 0\\).\nCorrect Choice is (A)."),

    ("""Assertion (A): The formula of aluminium hydroxide is written as \\(\\text{Al(OH)}_3\\) and not \\(\\text{AlOH}_3\\).\nReason (R): Brackets are compulsory when more than one polyatomic radical is required to balance charge, ensuring the subscript multiplies all elements within the radical.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "• Both statements are correct, and (R) provides the exact structural convention.\nCorrect Choice is (A)."),

    ("""State True or False: Ammonium ion (\\(\\text{NH}_4^+\\)) is the only common composite basic radical (cation) encountered in introductory chemistry.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Virtually all other common basic radicals are simple metal monoatomic cations; \\(\\text{NH}_4^+\\) is the prominent polyatomic cation.\nCorrect Choice is (A)."),

    ("""State True or False: The formula for cuprous oxide is \\(\\text{CuO}\\) and cupric oxide is \\(\\text{Cu}_2\\text{O}\\).""",
     ["True", "False"],
     "B", "OTF", "medium",
     "• False. Cuprous is \\(\\text{Cu}^+\\) (valency 1), so Cuprous Oxide is \\(\\text{Cu}_2\\text{O}\\). Cupric is \\(\\text{Cu}^{2+}\\) (valency 2), so Cupric Oxide is \\(\\text{CuO}\\).\nCorrect Choice is (B)."),

    ("""What is the chemical formula for Plumbous Nitrate (Lead(II) nitrate)?""",
     ["\\(\\text{PbNO}_3\\)", "\\(\\text{Pb(NO}_3)_2\\)", "\\(\\text{Pb}_2\\text{NO}_3\\)", "\\(\\text{Pb(NO}_2)_2\\)"],
     "B", "OSC", "easy",
     "• Lead(II) has valency 2 (\\(\\text{Pb}^{2+}\\)), nitrate is monovalent (\\(\\text{NO}_3^-\\)). The formula is \\(\\text{Pb(NO}_3)_2\\).\nCorrect Choice is (B)."),

    ("""What is the chemical formula for Barium Sulphate?""",
     ["\\(\\text{BaSO}_4\\)", "\\(\\text{Ba}_2\\text{SO}_4\\)", "\\(\\text{Ba}(\\text{SO}_4)_2\\)", "\\(\\text{BaS}\\)"],
     "A", "OSC", "easy",
     "• Barium is divalent (\\(\\text{Ba}^{2+}\\), valency 2) and Sulphate is divalent (\\(\\text{SO}_4^{2-}\\), valency 2). Simplifying gives \\(\\text{BaSO}_4\\).\nCorrect Choice is (A)."),

    # 31-40: Fill in blanks and formula identification
    ("""Fill in the blank: In an ionic compound, the positively charged radical is called a ________ radical.""",
     ["Acidic", "Basic", "Neutral", "Atmospheric"],
     "B", "OFB", "easy",
     "• Positively charged ions are basic radicals.\nCorrect Choice is (B)."),

    ("""Fill in the blank: The composite radical \\(\\text{SO}_3^{2-}\\) is named ________, whereas \\(\\text{SO}_4^{2-}\\) is named sulphate.""",
     ["Sulphide", "Sulphite", "Bisulphate", "Thiosulphate"],
     "B", "OFB", "easy",
     "• \\(\\text{SO}_3^{2-}\\) is sulphite; \\(\\text{SO}_4^{2-}\\) is sulphate.\nCorrect Choice is (B)."),

    ("""Fill in the blank: The radical \\(\\text{S}^{2-}\\) is named ________.""",
     ["Sulphate", "Sulphite", "Sulphide", "Sulphur"],
     "C", "OFB", "easy",
     "• Monoatomic negative ion \\(\\text{S}^{2-}\\) is sulphide.\nCorrect Choice is (C)."),

    ("""What is the correct chemical formula for Copper(II) Sulphate (blue vitriol)?""",
     ["\\(\\text{CuSO}_4\\)", "\\(\\text{Cu}_2\\text{SO}_4\\)", "\\(\\text{Cu}(\\text{SO}_4)_2\\)", "\\(\\text{CuS}\\)"],
     "A", "OSC", "easy",
     "• Cupric ion is \\(\\text{Cu}^{2+}\\) (valency 2), Sulphate is \\(\\text{SO}_4^{2-}\\) (valency 2). The formula is \\(\\text{CuSO}_4\\).\nCorrect Choice is (A)."),

    ("""What is the chemical formula for Zinc Nitrate?""",
     ["\\(\\text{ZnNO}_3\\)", "\\(\\text{Zn(NO}_3)_2\\)", "\\(\\text{Zn}_2\\text{NO}_3\\)", "\\(\\text{Zn(NO}_2)_2\\)"],
     "B", "OSC", "easy",
     "• Zinc is \\(\\text{Zn}^{2+}\\) (valency 2) and nitrate is \\(\\text{NO}_3^-\\) (valency 1). Criss-cross gives \\(\\text{Zn(NO}_3)_2\\).\nCorrect Choice is (B)."),

    ("""What is the chemical formula for Silver Chloride?""",
     ["\\(\\text{AgCl}\\)", "\\(\\text{AgCl}_2\\)", "\\(\\text{Ag}_2\\text{Cl}\\)", "\\(\\text{AgClO}_3\\)"],
     "A", "OSC", "easy",
     "• Silver is \\(\\text{Ag}^+\\) (valency 1) and chloride is \\(\\text{Cl}^-\\) (valency 1). Formula is \\(\\text{AgCl}\\).\nCorrect Choice is (A)."),

    ("""What is the chemical formula for Potassium Dichromate?""",
     ["\\(\\text{KCrO}_4\\)", "\\(\\text{K}_2\\text{Cr}_2\\text{O}_7\\)", "\\(\\text{KCr}_2\\text{O}_7\\)", "\\(\\text{K}_2\\text{CrO}_4\\)"],
     "B", "OSC", "medium",
     "• Potassium is \\(\\text{K}^+\\) (valency 1), Dichromate is \\(\\text{Cr}_2\\text{O}_7^{2-}\\) (valency 2). Formula is \\(\\text{K}_2\\text{Cr}_2\\text{O}_7\\).\nCorrect Choice is (B)."),

    ("""What is the valency of the element \\(M\\) in the compound \\(M_2\\text{O}_3\\)?""",
     ["1", "2", "3", "6"],
     "C", "OSC", "easy",
     "• In \\(M_2\\text{O}_3\\), the subscript 3 on oxygen comes from the valency of \\(M\\). Hence, \\(M\\) has valency 3.\nCorrect Choice is (C)."),

    ("""If a metal \\(M\\) forms an oxide with formula \\(M\\text{O}\\), what is the formula of its chloride?""",
     ["\\(M\\text{Cl}\\)", "\\(M\\text{Cl}_2\\)", "\\(M_2\\text{Cl}\\)", "\\(M\\text{Cl}_3\\)"],
     "B", "OSC", "medium",
     "• Since oxygen has valency 2, \\(M\\text{O}\\) implies \\(M\\) has valency 2. With monovalent chlorine (\\(\\text{Cl}^-\\)), its chloride is \\(M\\text{Cl}_2\\).\nCorrect Choice is (B)."),

    ("""If a non-metal \\(X\\) has valency 3 and combines with hydrogen (valency 1), what is the formula of its hydride?""",
     ["\\(X\\text{H}\\)", "\\(X\\text{H}_2\\)", "\\(X\\text{H}_3\\) (e.g. \\(\\text{NH}_3, \\text{PH}_3\\))", "\\(X_3\\text{H}\\)"],
     "C", "OSC", "easy",
     "• Criss-crossing valency 3 of \\(X\\) and valency 1 of H gives \\(X\\text{H}_3\\).\nCorrect Choice is (C).")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("""What is the valency of the Sodium ion (\\(\\text{Na}^+\\))?""",
     ["1", "2", "3", "0"],
     "A", "OSC", "easy",
     "• Sodium ion has a single positive charge; valency is 1.\nCorrect Choice is (A)."),

    ("""What is the valency of the Magnesium ion (\\(\\text{Mg}^{2+}\\))?""",
     ["1", "2", "3", "4"],
     "B", "OSC", "easy",
     "• Magnesium has valency 2.\nCorrect Choice is (B)."),

    ("""What is the valency of the Aluminium ion (\\(\\text{Al}^{3+}\\))?""",
     ["1", "2", "3", "4"],
     "C", "OSC", "easy",
     "• Aluminium has valency 3.\nCorrect Choice is (C)."),

    ("""What is the charge on a Nitrate radical (\\(\\text{NO}_3\\))?""",
     ["\\(+1\\)", "\\(-1\\)", "\\(-2\\)", "\\(-3\\)"],
     "B", "OSC", "easy",
     "• Nitrate radical has formula \\(\\text{NO}_3^-\\) with charge \\(-1\\).\nCorrect Choice is (B)."),

    ("""What is the charge on a Sulphate radical (\\(\\text{SO}_4\\))?""",
     ["\\(-1\\)", "\\(-2\\)", "\\(-3\\)", "\\(+2\\)"],
     "B", "OSC", "easy",
     "• Sulphate radical has formula \\(\\text{SO}_4^{2-}\\) with charge \\(-2\\).\nCorrect Choice is (B)."),

    ("""What is the charge on an Ammonium radical (\\(\\text{NH}_4\\))?""",
     ["\\(+1\\)", "\\(+2\\)", "\\(-1\\)", "\\(0\\)"],
     "A", "OSC", "easy",
     "• Ammonium radical has formula \\(\\text{NH}_4^+\\) with charge \\(+1\\).\nCorrect Choice is (A)."),

    ("""What is the formula of Potassium Chloride?""",
     ["\\(\\text{KCl}\\)", "\\(\\text{KCl}_2\\)", "\\(\\text{K}_2\\text{Cl}\\)", "\\(\\text{PCl}\\)"],
     "A", "OSC", "easy",
     "• Both \\(\\text{K}^+\\) and \\(\\text{Cl}^-\\) have valency 1; formula is \\(\\text{KCl}\\).\nCorrect Choice is (A)."),

    ("""What is the formula of Magnesium Chloride?""",
     ["\\(\\text{MgCl}\\)", "\\(\\text{MgCl}_2\\)", "\\(\\text{Mg}_2\\text{Cl}\\)", "\\(\\text{MgCl}_3\\)"],
     "B", "OSC", "easy",
     "• \\(\\text{Mg}\\) (valency 2) and \\(\\text{Cl}\\) (valency 1) give \\(\\text{MgCl}_2\\).\nCorrect Choice is (B)."),

    ("""What is the formula of Calcium Oxide?""",
     ["\\(\\text{CaO}\\)", "\\(\\text{CaO}_2\\)", "\\(\\text{Ca}_2\\text{O}\\)", "\\(\\text{Ca}_2\\text{O}_2\\)"],
     "A", "OSC", "easy",
     "• \\(\\text{Ca}\\) (valency 2) and \\(\\text{O}\\) (valency 2) simplify to \\(\\text{CaO}\\).\nCorrect Choice is (A)."),

    ("""What is the formula of Sodium Hydroxide?""",
     ["\\(\\text{NaOH}\\)", "\\(\\text{Na(OH)}_2\\)", "\\(\\text{Na}_2\\text{OH}\\)", "\\(\\text{SOH}\\)"],
     "A", "OSC", "easy",
     "• Both \\(\\text{Na}^+\\) and \\(\\text{OH}^-\\) are monovalent; formula is \\(\\text{NaOH}\\).\nCorrect Choice is (A)."),

    ("""What is the formula of Zinc Sulphate?""",
     ["\\(\\text{ZnSO}_4\\)", "\\(\\text{Zn}_2\\text{SO}_4\\)", "\\(\\text{Zn}(\\text{SO}_4)_2\\)", "\\(\\text{ZnS}\\)"],
     "A", "OSC", "easy",
     "• \\(\\text{Zn}^{2+}\\) and \\(\\text{SO}_4^{2-}\\) both have valency 2; formula is \\(\\text{ZnSO}_4\\).\nCorrect Choice is (A)."),

    ("""What is the formula of Hydrogen Sulphide gas?""",
     ["\\(\\text{HS}\\)", "\\(\\text{H}_2\\text{S}\\)", "\\(\\text{HS}_2\\)", "\\(\\text{H}_2\\text{SO}_4\\)"],
     "B", "OSC", "easy",
     "• H has valency 1, Sulphide has valency 2; formula is \\(\\text{H}_2\\text{S}\\).\nCorrect Choice is (B)."),

    ("""What is the formula of Carbon Tetrachloride?""",
     ["\\(\\text{CCl}\\)", "\\(\\text{CCl}_2\\)", "\\(\\text{CCl}_3\\)", "\\(\\text{CCl}_4\\)"],
     "D", "OSC", "easy",
     "• Carbon has valency 4, Chlorine has valency 1; formula is \\(\\text{CCl}_4\\).\nCorrect Choice is (D)."),

    ("""Which of the following is an ACIDIC radical?""",
     ["\\(\\text{Na}^+\\)", "\\(\\text{K}^+\\)", "\\(\\text{Cl}^-\\)", "\\(\\text{Ca}^{2+}\\)"],
     "C", "OSC", "easy",
     "• Negative anions derived from acids (like \\(\\text{Cl}^-\\)) are acidic radicals.\nCorrect Choice is (C)."),

    ("""Which of the following is a BASIC radical?""",
     ["\\(\\text{SO}_4^{2-}\\)", "\\(\\text{Mg}^{2+}\\)", "\\(\\text{NO}_3^-\\)", "\\(\\text{CO}_3^{2-}\\)"],
     "B", "OSC", "easy",
     "• Positive metal cations (like \\(\\text{Mg}^{2+}\\)) are basic radicals.\nCorrect Choice is (B)."),

    ("""What is the formula of Ammonium Chloride?""",
     ["\\(\\text{NH}_4\\text{Cl}\\)", "\\(\\text{NH}_3\\text{Cl}\\)", "\\((\\text{NH}_4)_2\\text{Cl}\\)", "\\(\\text{NCl}_3\\)"],
     "A", "OSC", "easy",
     "• \\(\\text{NH}_4^+\\) (valency 1) and \\(\\text{Cl}^-\\) (valency 1) yield \\(\\text{NH}_4\\text{Cl}\\).\nCorrect Choice is (A)."),

    ("""What is the formula of Sodium Nitrate?""",
     ["\\(\\text{NaNO}_3\\)", "\\(\\text{Na}_2\\text{NO}_3\\)", "\\(\\text{Na(NO}_3)_2\\)", "\\(\\text{NaNO}_2\\)"],
     "A", "OSC", "easy",
     "• \\(\\text{Na}^+\\) and \\(\\text{NO}_3^-\\) are both monovalent; formula is \\(\\text{NaNO}_3\\).\nCorrect Choice is (A)."),

    ("""What is the formula of Magnesium Nitrate?""",
     ["\\(\\text{MgNO}_3\\)", "\\(\\text{Mg(NO}_3)_2\\)", "\\(\\text{Mg}_2\\text{NO}_3\\)", "\\(\\text{Mg}_3\\text{N}_2\\)"],
     "B", "OSC", "easy",
     "• \\(\\text{Mg}^{2+}\\) (valency 2) and \\(\\text{NO}_3^-\\) (valency 1) give \\(\\text{Mg(NO}_3)_2\\).\nCorrect Choice is (B)."),

    ("""What is the formula of Potassium Hydroxide?""",
     ["\\(\\text{KOH}\\)", "\\(\\text{K(OH)}_2\\)", "\\(\\text{K}_2\\text{OH}\\)", "\\(\\text{POH}\\)"],
     "A", "OSC", "easy",
     "• \\(\\text{K}^+\\) and \\(\\text{OH}^-\\) are both monovalent; formula is \\(\\text{KOH}\\).\nCorrect Choice is (A)."),

    ("""What is the formula of Iron(II) Sulphate (Ferrous sulphate)?""",
     ["\\(\\text{FeSO}_4\\)", "\\(\\text{Fe}_2\\text{SO}_4\\)", "\\(\\text{Fe}_2(\\text{SO}_4)_3\\)", "\\(\\text{FeS}\\)"],
     "A", "OSC", "easy",
     "• Ferrous is \\(\\text{Fe}^{2+}\\) (valency 2), Sulphate is \\(\\text{SO}_4^{2-}\\) (valency 2). Formula is \\(\\text{FeSO}_4\\).\nCorrect Choice is (A)."),

    ("""What is the formula of Iron(III) Sulphate (Ferric sulphate)?""",
     ["\\(\\text{FeSO}_4\\)", "\\(\\text{Fe}_2(\\text{SO}_4)_3\\)", "\\(\\text{Fe}_3(\\text{SO}_4)_2\\)", "\\(\\text{Fe}_2\\text{SO}_4\\)"],
     "B", "OSC", "easy",
     "• Ferric is \\(\\text{Fe}^{3+}\\) (valency 3), Sulphate is \\(\\text{SO}_4^{2-}\\) (valency 2). Formula is \\(\\text{Fe}_2(\\text{SO}_4)_3\\).\nCorrect Choice is (B)."),

    ("""State True or False: In a neutral molecule, the sum of oxidation numbers / charges of all constituent radicals is zero.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Stable chemical compounds are electrically neutral.\nCorrect Choice is (A)."),

    ("""State True or False: Polyatomic radicals contain only one single type of atom.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. Polyatomic (composite) radicals contain atoms of two or more different elements (e.g. S and O in \\(\\text{SO}_4^{2-}\\)).\nCorrect Choice is (B)."),

    ("""What is the formula of Calcium Phosphate?""",
     ["\\(\\text{CaPO}_4\\)", "\\(\\text{Ca}_2(\\text{PO}_4)_3\\)", "\\(\\text{Ca}_3(\\text{PO}_4)_2\\)", "\\(\\text{Ca}_3\\text{PO}_4\\)"],
     "C", "OSC", "medium",
     "• Calcium is \\(\\text{Ca}^{2+}\\) (valency 2), Phosphate is \\(\\text{PO}_4^{3-}\\) (valency 3). Formula is \\(\\text{Ca}_3(\\text{PO}_4)_2\\).\nCorrect Choice is (C)."),

    ("""What is the formula of Sodium Carbonate?""",
     ["\\(\\text{NaCO}_3\\)", "\\(\\text{Na}_2\\text{CO}_3\\)", "\\(\\text{Na}(\\text{CO}_3)_2\\)", "\\(\\text{Na}_2\\text{C}\\)"],
     "B", "OSC", "easy",
     "• \\(\\text{Na}^+\\) (valency 1) and \\(\\text{CO}_3^{2-}\\) (valency 2) give \\(\\text{Na}_2\\text{CO}_3\\).\nCorrect Choice is (B)."),

    ("""Fill in the blank: The symbol \\(\\text{HCO}_3^-\\) represents the ________ radical.""",
     ["Carbonate", "Bicarbonate (hydrogen carbonate)", "Carbide", "Oxalate"],
     "B", "OFB", "easy",
     "• \\(\\text{HCO}_3^-\\) is bicarbonate or hydrogen carbonate.\nCorrect Choice is (B)."),

    ("""Fill in the blank: When writing chemical formulae, the numbers obtained after cross-multiplying valencies are written as ________.""",
     ["Superscripts", "Subscripts", "Coefficients", "Exponents"],
     "B", "OFB", "easy",
     "• Subscripts indicate atom/radical counts (e.g. \\(\\text{H}_2\\text{O}\\)).\nCorrect Choice is (B)."),

    ("""What is the chemical formula of Lead(II) Oxide?""",
     ["\\(\\text{PbO}\\)", "\\(\\text{PbO}_2\\)", "\\(\\text{Pb}_2\\text{O}\\)", "\\(\\text{Pb}_3\\text{O}_4\\)"],
     "A", "OSC", "easy",
     "• Lead(II) has valency 2, Oxygen has valency 2; formula is \\(\\text{PbO}\\).\nCorrect Choice is (A)."),

    ("""What is the chemical formula of Lead(IV) Oxide (Lead dioxide)?""",
     ["\\(\\text{PbO}\\)", "\\(\\text{PbO}_2\\)", "\\(\\text{Pb}_2\\text{O}_4\\)", "\\(\\text{Pb}_4\\text{O}_2\\)"],
     "B", "OSC", "medium",
     "• Lead(IV) has valency 4, Oxygen has valency 2. Criss-crossing gives \\(\\text{Pb}_2\\text{O}_4\\), which simplifies to \\(\\text{PbO}_2\\).\nCorrect Choice is (B)."),

    ("""What is the formula of Potassium Sulphite?""",
     ["\\(\\text{K}_2\\text{SO}_4\\)", "\\(\\text{K}_2\\text{SO}_3\\)", "\\(\\text{KSO}_3\\)", "\\(\\text{K}_2\\text{S}\\)"],
     "B", "OSC", "easy",
     "• Potassium is \\(\\text{K}^+\\) (valency 1), Sulphite is \\(\\text{SO}_3^{2-}\\) (valency 2). Formula is \\(\\text{K}_2\\text{SO}_3\\).\nCorrect Choice is (B).")
]

# 12 Foundation Mock Questions (501-512) with rich embedded vector SVGs
foundation_data = [
    # 501: Criss-Cross Step-by-Step for Aluminium Oxide
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Criss-Cross Method: Al₂O₃</text>
  <!-- Step 1: Symbols -->
  <text x="35" y="60" fill="#cbd5e1" font-size="10">1. Radicals:</text>
  <text x="120" y="60" fill="#38bdf8" font-size="14" font-weight="bold">Al</text>
  <text x="210" y="60" fill="#ef4444" font-size="14" font-weight="bold">O</text>
  <!-- Step 2: Valencies -->
  <text x="35" y="95" fill="#cbd5e1" font-size="10">2. Valencies:</text>
  <text x="125" y="95" fill="#fde047" font-size="14" font-weight="bold">3</text>
  <text x="215" y="95" fill="#fde047" font-size="14" font-weight="bold">2</text>
  <!-- Criss-cross arrows -->
  <line x1="130" y1="105" x2="215" y2="140" stroke="#34d399" stroke-width="2.5"/>
  <line x1="215" y1="105" x2="130" y2="140" stroke="#34d399" stroke-width="2.5"/>
  <text x="170" y="125" fill="#34d399" font-size="14">✕</text>
  <!-- Step 3: Result -->
  <rect x="70" y="160" width="200" height="40" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="4"/>
  <text x="100" y="185" fill="#38bdf8" font-size="15" font-weight="bold">Formula: Al₂O₃</text>
</svg>
</div>
In the criss-cross formula construction shown above, why does the valency 3 of Aluminium become the subscript for Oxygen, and the valency 2 of Oxygen become the subscript for Aluminium?""",
     ["Because chemical symbols swap positions alphabetically",
      "To ensure equal and opposite electrical charge: \\(2 \\times (+3) = +6\\) and \\(3 \\times (-2) = -6\\), achieving net electrical neutrality (\\(+6 - 6 = 0\\))",
      "Because aluminium is three times heavier than oxygen",
      "Because oxygen atoms push aluminium into the front"],
     "B", "OSC", "hard",
     "• Cross-multiplying the valencies guarantees that total positive charge balances total negative charge: \\(2(+3) + 3(-2) = 0\\), satisfying macroscopic electrical neutrality.\nCorrect Choice is (B)."),

    # 502: Bracket Convention in Calcium Hydroxide Ca(OH)2
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="70" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Bracket Rule for Polyatomic Radicals</text>
  <!-- Correct notation -->
  <rect x="25" y="55" width="135" height="90" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="40" y="80" fill="#34d399" font-size="12" font-weight="bold">✓ Ca(OH)₂</text>
  <text x="35" y="105" fill="#cbd5e1" font-size="9">• 1 Calcium atom (Ca)</text>
  <text x="35" y="120" fill="#cbd5e1" font-size="9">• 2 Oxygen atoms (2×O)</text>
  <text x="35" y="135" fill="#cbd5e1" font-size="9">• 2 Hydrogen atoms (2×H)</text>
  <!-- Incorrect notation -->
  <rect x="180" y="55" width="135" height="90" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="195" y="80" fill="#f87171" font-size="12" font-weight="bold">✗ CaOH₂</text>
  <text x="190" y="105" fill="#cbd5e1" font-size="9">• 1 Calcium atom (Ca)</text>
  <text x="190" y="120" fill="#cbd5e1" font-size="9">• 1 Oxygen atom (1×O)</text>
  <text x="190" y="135" fill="#ef4444" font-size="9">• 2 Hydrogen atoms (WRONG!)</text>
  <text x="40" y="185" fill="#fde047" font-size="10">Parentheses enclose polyatomic groups when subscript &gt; 1</text>
</svg>
</div>
What critical error does the formula \\(\\text{CaOH}_2\\) contain compared to the correct IUPAC notation \\(\\text{Ca(OH)}_2\\)?""",
     ["\\(\\text{CaOH}_2\\) has too many calcium atoms",
      "Without brackets, the subscript 2 applies only to Hydrogen, incorrectly representing 1 Oxygen atom instead of the required 2 complete hydroxide radicals",
      "Calcium cannot form bonds with oxygen",
      "Hydroxide must always be written first on the left"],
     "B", "OSC", "medium",
     "• In chemical nomenclature, a subscript without parentheses modifies only the immediately preceding symbol. Writing \\(\\text{CaOH}_2\\) would mean \\(1\\text{ O}\\) and \\(2\\text{ H}\\), whereas \\(\\text{Ca(OH)}_2\\) correctly doubles both O and H.\nCorrect Choice is (B)."),

    # 503: Simple vs Composite Radical Classification Matrix
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Radical Classification Matrix</text>
  <!-- Simple Radicals -->
  <rect x="25" y="50" width="135" height="110" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="35" y="70" fill="#38bdf8" font-size="11" font-weight="bold">Simple Radicals</text>
  <text x="35" y="88" fill="#94a3b8" font-size="9">(Single element atom)</text>
  <text x="35" y="110" fill="#cbd5e1" font-size="10">Basic: Na⁺, Mg²⁺, Al³⁺</text>
  <text x="35" y="130" fill="#cbd5e1" font-size="10">Acidic: Cl⁻, O²⁻, S²⁻</text>
  <!-- Composite Radicals -->
  <rect x="180" y="50" width="135" height="110" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="190" y="70" fill="#fde047" font-size="11" font-weight="bold">Composite Radicals</text>
  <text x="190" y="88" fill="#94a3b8" font-size="9">(Multiple element group)</text>
  <text x="190" y="110" fill="#cbd5e1" font-size="10">Basic: NH₄⁺ (Ammonium)</text>
  <text x="190" y="130" fill="#cbd5e1" font-size="10">Acidic: SO₄²⁻, NO₃⁻, CO₃²⁻</text>
  <text x="45" y="195" fill="#34d399" font-size="10">Composite radicals behave as a single unyielding unit</text>
</svg>
</div>
According to the classification matrix above, which pair consists of ONE simple basic radical and ONE composite acidic radical?""",
     ["\\(\\text{Na}^+\\) and \\(\\text{Cl}^-\\)",
      "\\(\\text{NH}_4^+\\) and \\(\\text{SO}_4^{2-}\\)",
      "\\(\\text{Mg}^{2+}\\) and \\(\\text{CO}_3^{2-}\\)",
      "\\(\\text{Cl}^-\\) and \\(\\text{O}^{2-}\\)"],
     "C", "OSC", "medium",
     "• \\(\\text{Mg}^{2+}\\) is a simple basic radical (monoatomic cation) and \\(\\text{CO}_3^{2-}\\) is a composite acidic radical (polyatomic anion).\nCorrect Choice is (C)."),

    # 504: Ammonium Sulphate (NH4)2SO4 Formula Building
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Formula Construction: (NH₄)₂SO₄</text>
  <!-- Radicals -->
  <text x="35" y="60" fill="#cbd5e1" font-size="10">Radicals:</text>
  <text x="115" y="60" fill="#38bdf8" font-size="13" font-weight="bold">NH₄⁺</text>
  <text x="215" y="60" fill="#f59e0b" font-size="13" font-weight="bold">SO₄²⁻</text>
  <!-- Valency -->
  <text x="35" y="95" fill="#cbd5e1" font-size="10">Valency:</text>
  <text x="125" y="95" fill="#fde047" font-size="14" font-weight="bold">1</text>
  <text x="225" y="95" fill="#fde047" font-size="14" font-weight="bold">2</text>
  <!-- Criss Cross -->
  <line x1="130" y1="105" x2="225" y2="140" stroke="#34d399" stroke-width="2.5"/>
  <line x1="225" y1="105" x2="130" y2="140" stroke="#34d399" stroke-width="2.5"/>
  <!-- Result -->
  <rect x="55" y="160" width="230" height="40" fill="#1e293b" stroke="#34d399" stroke-width="2" rx="4"/>
  <text x="80" y="185" fill="#34d399" font-size="15" font-weight="bold">Formula: (NH₄)₂SO₄</text>
</svg>
</div>
In the compound Ammonium Sulphate, \\((\\text{NH}_4)_2\\text{SO}_4\\), how many TOTAL atoms of all elements are present in one formula unit?""",
     ["7 atoms", "10 atoms", "15 atoms", "18 atoms"],
     "C", "OSC", "hard",
     "• In \\((\\text{NH}_4)_2\\text{SO}_4\\):\n- Ammonium \\((\\text{NH}_4)_2\\): \\(2 \\times (1\\text{ N} + 4\\text{ H}) = 2 \\times 5 = 10\\text{ atoms}\\)\n- Sulphate \\(\\text{SO}_4\\): \\(1\\text{ S} + 4\\text{ O} = 5\\text{ atoms}\\)\nTotal atoms = \\(10 + 5 = 15\\text{ atoms}\\).\nCorrect Choice is (C)."),

    # 505: Electrical Neutrality in Ionic Lattice (Al2(SO4)3)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Charge Balance in Al₂(SO₄)₃</text>
  <!-- Positive Cation Block -->
  <rect x="30" y="55" width="130" height="75" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="40" y="75" fill="#38bdf8" font-size="11" font-weight="bold">2 × Al³⁺ Cations</text>
  <text x="40" y="95" fill="#cbd5e1" font-size="10">2 × (+3) =</text>
  <text x="105" y="98" fill="#38bdf8" font-size="16" font-weight="bold">+6</text>
  <!-- Negative Anion Block -->
  <rect x="180" y="55" width="130" height="75" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="190" y="75" fill="#f87171" font-size="11" font-weight="bold">3 × SO₄²⁻ Anions</text>
  <text x="190" y="95" fill="#cbd5e1" font-size="10">3 × (-2) =</text>
  <text x="255" y="98" fill="#ef4444" font-size="16" font-weight="bold">-6</text>
  <!-- Neutral Sum -->
  <rect x="30" y="145" width="280" height="35" fill="#334155" stroke="#34d399" rx="3"/>
  <text x="60" y="168" fill="#34d399" font-size="11" font-weight="bold">Net Ionic Charge = (+6) + (-6) = 0 (Neutral)</text>
</svg>
</div>
In the compound Aluminium Sulphate \\(\\text{Al}_2(\\text{SO}_4)_3\\) illustrated above, what is the total positive charge donated by the aluminium ions and total negative charge provided by the sulphate ions?""",
     ["\\(+2\\) and \\(-3\\)",
      "\\(+3\\) and \\(-2\\)",
      "\\(+6\\) and \\(-6\\)",
      "\\(+12\\) and \\(-12\\)"],
     "C", "OSC", "easy",
     "• 2 aluminium ions each carry \\(+3\\) (total \\(+6\\)), and 3 sulphate ions each carry \\(-2\\) (total \\(-6\\)), canceling out to zero.\nCorrect Choice is (C)."),

    # 506: Basic vs Acidic Radical Origin (Neutralization Reaction)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Acid-Base Origin of Salt Radicals</text>
  <!-- Acid -->
  <rect x="25" y="50" width="85" height="50" fill="#1e293b" stroke="#ef4444" rx="3"/>
  <text x="35" y="70" fill="#f87171" font-size="10" font-weight="bold">Acid (HCl)</text>
  <text x="35" y="88" fill="#cbd5e1" font-size="9">Yields Cl⁻</text>
  <text x="118" y="80" fill="#fff" font-size="14">+</text>
  <!-- Base -->
  <rect x="135" y="50" width="85" height="50" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="145" y="70" fill="#38bdf8" font-size="10" font-weight="bold">Base (NaOH)</text>
  <text x="145" y="88" fill="#cbd5e1" font-size="9">Yields Na⁺</text>
  <text x="228" y="80" fill="#38bdf8" font-size="14">→</text>
  <!-- Salt -->
  <rect x="245" y="50" width="75" height="50" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="252" y="70" fill="#34d399" font-size="10" font-weight="bold">Salt (NaCl)</text>
  <text x="252" y="88" fill="#cbd5e1" font-size="9">+ H₂O</text>
  <!-- Summary text -->
  <rect x="25" y="125" width="295" height="70" fill="#334155" rx="4"/>
  <text x="35" y="145" fill="#38bdf8" font-size="10">• Na⁺ comes from the Base → Basic Radical (Cation)</text>
  <text x="35" y="165" fill="#f87171" font-size="10">• Cl⁻ comes from the Acid → Acidic Radical (Anion)</text>
  <text x="35" y="185" fill="#34d399" font-size="10">• Every inorganic salt is an ionic combination of both</text>
</svg>
</div>
In the neutralization reaction \\(\\text{NaOH} + \\text{HCl} \\to \\text{NaCl} + \\text{H}_2\\text{O}\\) shown above, which ion acts as the basic radical and which ion acts as the acidic radical in the salt \\(\\text{NaCl}\\)?""",
     ["\\(\\text{Cl}^-\\) is basic, \\(\\text{Na}^+\\) is acidic",
      "\\(\\text{Na}^+\\) is the basic radical (from base \\(\\text{NaOH}\\)) and \\(\\text{Cl}^-\\) is the acidic radical (from acid \\(\\text{HCl}\\))",
      "Both are acidic radicals",
      "Both are basic radicals"],
     "B", "OSC", "easy",
     "• In any salt, the cation originates from the base (basic radical) and the anion originates from the acid (acidic radical).\nCorrect Choice is (B)."),

    # 507: Simplification of Common Factor (Magnesium Oxide)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Simplification of Common Factors</text>
  <text x="40" y="60" fill="#cbd5e1" font-size="11">Initial cross: Mg (valency 2) and O (valency 2)</text>
  <text x="40" y="85" fill="#ef4444" font-size="13" font-weight="bold">Intermediate Form: Mg₂O₂</text>
  <line x1="40" y1="100" x2="300" y2="100" stroke="#475569" stroke-width="1.5"/>
  <text x="40" y="125" fill="#fde047" font-size="11">Divide subscripts by common divisor (2): 2÷2 = 1</text>
  <rect x="70" y="145" width="200" height="40" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="4"/>
  <text x="105" y="170" fill="#34d399" font-size="15" font-weight="bold">Final Formula: MgO</text>
</svg>
</div>
What is the proper chemical formula for Tin(IV) Oxide (Stannic oxide), formed between \\(\\text{Sn}^{4+}\\) and \\(\\text{O}^{2-}\\)?""",
     ["\\(\\text{Sn}_2\\text{O}_4\\)", "\\(\\text{SnO}_2\\)", "\\(\\text{Sn}_4\\text{O}_2\\)", "\\(\\text{SnO}\\)"],
     "B", "OSC", "medium",
     "• Criss-crossing valency 4 and 2 gives \\(\\text{Sn}_2\\text{O}_4\\). Dividing both subscripts by the common divisor 2 simplifies the formula to \\(\\text{SnO}_2\\).\nCorrect Choice is (B)."),

    # 508: Variable Valency Formula Pair (Cu2O vs CuO)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Copper Oxides Comparison</text>
  <!-- Cuprous Oxide -->
  <rect x="25" y="55" width="135" height="100" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="35" y="80" fill="#f87171" font-size="12" font-weight="bold">Cuprous Oxide</text>
  <text x="35" y="100" fill="#cbd5e1" font-size="10">• Formula: Cu₂O</text>
  <text x="35" y="118" fill="#fde047" font-size="10">• Cu Valency: 1 (Cu⁺)</text>
  <text x="35" y="135" fill="#94a3b8" font-size="9">• Reddish powder</text>
  <!-- Cupric Oxide -->
  <rect x="180" y="55" width="135" height="100" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="190" y="80" fill="#38bdf8" font-size="12" font-weight="bold">Cupric Oxide</text>
  <text x="190" y="100" fill="#cbd5e1" font-size="10">• Formula: CuO</text>
  <text x="190" y="118" fill="#fde047" font-size="10">• Cu Valency: 2 (Cu²⁺)</text>
  <text x="190" y="135" fill="#94a3b8" font-size="9">• Black powder</text>
  <text x="40" y="185" fill="#34d399" font-size="10">Lower valency (-ous) has higher copper-to-oxygen ratio</text>
</svg>
</div>
Which of the following compounds contains copper in the CUPRIC state (valency 2)?""",
     ["\\(\\text{Cu}_2\\text{O}\\)", "\\(\\text{CuCl}\\)", "\\(\\text{CuSO}_4\\)", "\\(\\text{Cu}_2\\text{S}\\)"],
     "C", "OSC", "medium",
     "• In \\(\\text{CuSO}_4\\), Sulphate is \\(\\text{SO}_4^{2-}\\), so Copper must be \\(\\text{Cu}^{2+}\\) (cupric state). In the other choices, copper is monovalent (\\(\\text{Cu}^+\\), cuprous).\nCorrect Choice is (C)."),

    # 509: Phosphate Salts Formula Comparison
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Trivalent Phosphate (PO₄³⁻) Salts</text>
  <!-- Sodium Phosphate -->
  <rect x="25" y="55" width="85" height="70" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="30" y="75" fill="#38bdf8" font-size="10" font-weight="bold">Na⁺ (Val: 1)</text>
  <text x="30" y="100" fill="#fde047" font-size="11" font-weight="bold">Na₃PO₄</text>
  <!-- Calcium Phosphate -->
  <rect x="125" y="55" width="90" height="70" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="130" y="75" fill="#10b981" font-size="10" font-weight="bold">Ca²⁺ (Val: 2)</text>
  <text x="130" y="100" fill="#fde047" font-size="11" font-weight="bold">Ca₃(PO₄)₂</text>
  <!-- Aluminium Phosphate -->
  <rect x="230" y="55" width="85" height="70" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="235" y="75" fill="#f59e0b" font-size="10" font-weight="bold">Al³⁺ (Val: 3)</text>
  <text x="235" y="100" fill="#fde047" font-size="11" font-weight="bold">AlPO₄</text>
  <text x="40" y="165" fill="#cbd5e1" font-size="10">Phosphate valency (3) determines the cation multiplier</text>
</svg>
</div>
What is the correct chemical formula for Aluminium Phosphate formed between \\(\\text{Al}^{3+}\\) and \\(\\text{PO}_4^{3-}\\)?""",
     ["\\(\\text{Al}_3(\\text{PO}_4)_3\\)", "\\(\\text{AlPO}_4\\)", "\\(\\text{Al}_2(\\text{PO}_4)_3\\)", "\\(\\text{Al}_3\\text{PO}_4\\)"],
     "B", "OSC", "easy",
     "• Both \\(\\text{Al}^{3+}\\) and \\(\\text{PO}_4^{3-}\\) have valency 3. The ratio \\(3:3\\) simplifies to \\(1:1\\), yielding \\(\\text{AlPO}_4\\).\nCorrect Choice is (B)."),

    # 510: Bicarbonate vs Carbonate Radicals
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="70" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Carbonate vs Bicarbonate Radical</text>
  <!-- Carbonate -->
  <rect x="25" y="55" width="135" height="85" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="35" y="80" fill="#f87171" font-size="12" font-weight="bold">Carbonate Ion</text>
  <text x="35" y="100" fill="#cbd5e1" font-size="10">• Formula: CO₃²⁻</text>
  <text x="35" y="118" fill="#fde047" font-size="10">• Valency: 2 (Divalent)</text>
  <!-- Bicarbonate -->
  <rect x="180" y="55" width="135" height="85" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="190" y="80" fill="#38bdf8" font-size="12" font-weight="bold">Bicarbonate Ion</text>
  <text x="190" y="100" fill="#cbd5e1" font-size="10">• Formula: HCO₃⁻</text>
  <text x="190" y="118" fill="#fde047" font-size="10">• Valency: 1 (Monovalent)</text>
  <text x="35" y="175" fill="#93c5fd" font-size="10">Adding H⁺ to CO₃²⁻ reduces net charge from -2 to -1</text>
</svg>
</div>
Why does the Bicarbonate radical (\\(\\text{HCO}_3^-\\)) have a valency of 1, whereas the Carbonate radical (\\(\\text{CO}_3^{2-}\\)) has a valency of 2?""",
     ["Because hydrogen has no mass",
      "Because adding one positively charged proton (\\(\\text{H}^+\\)) to a divalent carbonate ion (\\(\\text{CO}_3^{2-}\\)) partially neutralizes its negative charge from \\(-2\\) to \\(-1\\)",
      "Because carbon loses an electron to hydrogen",
      "Because bicarbonate is an organic compound"],
     "B", "OSC", "medium",
     "• \\(\\text{CO}_3^{2-} + \\text{H}^+ \\to \\text{HCO}_3^-\\). The addition of \\(+1\\) charge from the proton reduces the overall charge to \\(-1\\), reducing valency to 1.\nCorrect Choice is (B)."),

    # 511: Cross-Multiplication Grid Practice
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Deducing Unknown Valency from Formula</text>
  <text x="35" y="60" fill="#cbd5e1" font-size="11">Given Compound: X(SO₄)₂</text>
  <!-- Analysis box -->
  <rect x="30" y="75" width="280" height="80" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="40" y="98" fill="#cbd5e1" font-size="10">• Sulphate radical (SO₄) has a known valency of 2</text>
  <text x="40" y="118" fill="#cbd5e1" font-size="10">• Subscript of SO₄ is 2; Subscript of X is 1 (simplified)</text>
  <text x="40" y="138" fill="#fde047" font-size="11" font-weight="bold">• Cross-multiplication reveals: Valency of X = 2 × 2 = 4</text>
  <text x="40" y="185" fill="#34d399" font-size="10">Element X is tetravalent (such as Sn⁴⁺ or Pb⁴⁺)</text>
</svg>
</div>
A newly discovered metal element \\(M\\) forms a sulphate with the chemical formula \\(M(\\text{SO}_4)_2\\). What is the valency of metal \\(M\\)?""",
     ["1", "2", "3", "4"],
     "D", "OSC", "hard",
     "• Sulphate has valency 2 (charge \\(-2\\)). Two sulphate groups provide a total charge of \\(2 \\times (-2) = -4\\). To maintain electrical neutrality, a single atom of \\(M\\) must have valency 4 (charge \\(+4\\)).\nCorrect Choice is (D)."),

    # 512: Complex Radicals Nomenclature Hierarchy
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Radical Suffix Rules: -ide, -ite, -ate</text>
  <!-- -ide -->
  <rect x="25" y="50" width="85" height="100" fill="#1e293b" stroke="#60a5fa" rx="3"/>
  <text x="35" y="72" fill="#93c5fd" font-size="11" font-weight="bold">-ide</text>
  <text x="30" y="95" fill="#cbd5e1" font-size="9">Monoatomic</text>
  <text x="30" y="115" fill="#fde047" font-size="10">S²⁻ (Sulphide)</text>
  <text x="30" y="132" fill="#fde047" font-size="10">Cl⁻ (Chloride)</text>
  <!-- -ite -->
  <rect x="125" y="50" width="90" height="100" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="135" y="72" fill="#fde047" font-size="11" font-weight="bold">-ite</text>
  <text x="130" y="95" fill="#cbd5e1" font-size="9">Fewer Oxygen</text>
  <text x="130" y="115" fill="#fde047" font-size="10">SO₃²⁻ (Sulphite)</text>
  <text x="130" y="132" fill="#fde047" font-size="10">NO₂⁻ (Nitrite)</text>
  <!-- -ate -->
  <rect x="230" y="50" width="85" height="100" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="240" y="72" fill="#86efac" font-size="11" font-weight="bold">-ate</text>
  <text x="235" y="95" fill="#cbd5e1" font-size="9">More Oxygen</text>
  <text x="235" y="115" fill="#fde047" font-size="10">SO₄²⁻ (Sulphate)</text>
  <text x="235" y="132" fill="#fde047" font-size="10">NO₃⁻ (Nitrate)</text>
  <text x="45" y="185" fill="#38bdf8" font-size="10">Universal chemical suffix logic for inorganic oxyanions</text>
</svg>
</div>
Based on the oxyanion nomenclature hierarchy above, which formula corresponds to Potassium Nitrite?""",
     ["\\(\\text{KNO}_3\\)", "\\(\\text{KNO}_2\\)", "\\(\\text{K}_3\\text{N}\\)", "\\(\\text{K}_2\\text{NO}_2\\)"],
     "B", "OSC", "easy",
     "• Nitrite corresponds to the oxyanion with fewer oxygens (\\(\\text{NO}_2^-\\)). Combining with \\(\\text{K}^+\\) yields \\(\\text{KNO}_2\\) (while \\(\\text{KNO}_3\\) is potassium nitrate).\nCorrect Choice is (B).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-4-4.4-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-4-4.4-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-4-4.4-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch4_topic4.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
