# scripts/generate_topic5_3.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-5-5.3"
CHAPTER_NUM = 5

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: Reaction of acids with active metals
    ("""When a dilute mineral acid (such as dilute \\(\\text{HCl}\\) or dilute \\(\\text{H}_2\\text{SO}_4\\)) reacts with an active metal like Zinc, what gas is liberated?""",
     ["Oxygen gas (\\(\\text{O}_2\\))",
      "Hydrogen gas (\\(\\text{H}_2\\))",
      "Carbon dioxide gas (\\(\\text{CO}_2\\))",
      "Nitrogen dioxide gas (\\(\\text{NO}_2\\))"],
     "B", "OSC", "easy",
     "• Active metals displace hydrogen from dilute acids: \\(\\text{Metal} + \\text{Dilute Acid} \\to \\text{Salt} + \\text{H}_2\\uparrow\\).\nCorrect Choice is (B)."),

    ("""What standard laboratory test confirms that an evolved gas is Hydrogen (\\(\\text{H}_2\\))?""",
     ["It turns lime water milky",
      "It extinguishes a flame silently without sound",
      "It burns with a characteristic pale blue flame accompanied by a sharp 'pop' sound when a burning splint is brought near the mouth of the tube",
      "It rekindles a glowing wooden splinter"],
     "C", "OSC", "easy",
     "• Hydrogen forms an explosive mixture with oxygen in air that combusts rapidly with a signature 'pop' sound: \\(2\\text{H}_2 + \\text{O}_2 \\to 2\\text{H}_2\\text{O}\\).\nCorrect Choice is (C)."),

    ("""What is the balanced chemical equation for the reaction between zinc granules and dilute hydrochloric acid?""",
     ["\\(\\text{Zn} + \\text{HCl} \\to \\text{ZnCl} + \\text{H}\\)",
      "\\(\\text{Zn} + 2\\text{HCl} \\to \\text{ZnCl}_2 + \\text{H}_2\\uparrow\\)",
      "\\(\\text{Zn} + 2\\text{HCl} \\to \\text{ZnCl}_2 + \\text{H}_2\\text{O}\\)",
      "\\(2\\text{Zn} + \\text{HCl} \\to \\text{Zn}_2\\text{Cl} + \\text{H}_2\\)"],
     "B", "OSC", "easy",
     "• Zinc is divalent (\\(\\text{Zn}^{2+}\\)) and displaces hydrogen: \\(\\text{Zn} + 2\\text{HCl} \\to \\text{ZnCl}_2 + \\text{H}_2\\uparrow\\).\nCorrect Choice is (B)."),

    ("""Why should sour food substances (such as curd, pickles, vinegar, or citrus juices) NEVER be stored in brass or copper vessels?""",
     ["Sour foods absorb the shiny color of copper",
      "Organic acids present in sour foods react chemically with copper/brass to form toxic, poisonous metallic salts that cause food poisoning",
      "Sour foods cause copper to turn into gold",
      "The vessels dissolve into water within five minutes"],
     "B", "OSC", "easy",
     "• Acids in foods corrode copper and zinc (brass), leaching toxic metallic ions into food causing severe toxicity.\nCorrect Choice is (B)."),

    ("""Which active metal reacts with concentrated Sodium Hydroxide (\\(\\text{NaOH}\\)) solution upon heating to release Hydrogen gas?""",
     ["Copper (\\(\\text{Cu}\\))",
      "Zinc (\\(\\text{Zn}\\))",
      "Silver (\\(\\text{Ag}\\))",
      "Gold (\\(\\text{Au}\\))"],
     "B", "OSC", "medium",
     "• Amphoteric metals like Zinc react with strong alkalis on heating: \\(\\text{Zn} + 2\\text{NaOH} \\to \\text{Na}_2\\text{ZnO}_2\\text{ (Sodium zincate)} + \\text{H}_2\\uparrow\\).\nCorrect Choice is (B)."),

    ("""What is the chemical name and formula of the salt produced when Zinc reacts with hot concentrated \\(\\text{NaOH}\\) solution?""",
     ["Zinc oxide (\\(\\text{ZnO}\\))",
      "Sodium zincate (\\(\\text{Na}_2\\text{ZnO}_2\\))",
      "Zinc hydroxide (\\(\\text{Zn(OH)}_2\\))",
      "Sodium hydride (\\(\\text{NaH}\\))"],
     "B", "OSC", "medium",
     "• The reaction produces sodium zincate: \\(\\text{Na}_2\\text{ZnO}_2\\).\nCorrect Choice is (B)."),

    ("""Which metal does NOT react with dilute hydrochloric acid to liberate hydrogen gas under normal conditions?""",
     ["Magnesium (\\(\\text{Mg}\\))",
      "Iron (\\(\\text{Fe}\\))",
      "Copper (\\(\\text{Cu}\\))",
      "Aluminium (\\(\\text{Al}\\))"],
     "C", "OSC", "medium",
     "• Copper is situated below hydrogen in the metal reactivity series and cannot reduce \\(\\text{H}^+\\) to \\(\\text{H}_2\\).\nCorrect Choice is (C)."),

    ("""Why does dilute Nitric acid (\\(\\text{HNO}_3\\)) usually NOT evolve hydrogen gas when reacting with metals (except \\(\\text{Mg}\\) and \\(\\text{Mn}\\))?""",
     ["Nitric acid contains no hydrogen",
      "Nitric acid is a powerful oxidizing agent that immediately oxidizes the evolved hydrogen gas into water (\\(\\text{H}_2\\text{O}\\)), getting itself reduced to nitrogen oxides (\\(\\text{NO}_2, \\text{NO}\\))",
      "Nitric acid freezes the metal surface",
      "Nitric acid is a weak organic acid"],
     "B", "OSC", "hard",
     "• Because \\(\\text{HNO}_3\\) is a strong oxidizer, the liberated hydrogen is oxidized to \\(\\text{H}_2\\text{O}\\) while nitric acid reduces to \\(\\text{NO}_x\\).\nCorrect Choice is (B)."),

    ("""Which two metals react with very dilute (approx. \\(1\\%\\)) cold nitric acid to liberate Hydrogen gas?""",
     ["Copper and Silver", "Magnesium (\\(\\text{Mg}\\)) and Manganese (\\(\\text{Mn}\\))", "Gold and Platinum", "Lead and Zinc"],
     "B", "OSC", "hard",
     "• Very dilute cold \\(\\text{HNO}_3\\) is such a mild oxidizer that \\(\\text{Mg}\\) and \\(\\text{Mn}\\) successfully displace \\(\\text{H}_2\\) gas.\nCorrect Choice is (B)."),

    ("""When magnesium ribbon reacts with dilute hydrochloric acid, what is observed?""",
     ["The solution turns dark black",
      "Vigorous bubbling and effervescence of hydrogen gas occurs, magnesium dissolves, and the test tube becomes warm (exothermic)",
      "A brown gas is evolved",
      "No reaction takes place"],
     "B", "OSC", "easy",
     "• \\(\\text{Mg} + 2\\text{HCl} \\to \\text{MgCl}_2 + \\text{H}_2\\uparrow\\); vigorous effervescence and exothermic heat release.\nCorrect Choice is (B)."),

    # 11-20: Reaction with metal oxides and non-metal oxides
    ("""What is the general chemical equation for the reaction of a dilute acid with a basic metal oxide?""",
     ["\\(\\text{Metal oxide} + \\text{Acid} \\to \\text{Metal} + \\text{Water}\\)",
      "\\(\\text{Metal oxide} + \\text{Acid} \\to \\text{Salt} + \\text{Water}\\)",
      "\\(\\text{Metal oxide} + \\text{Acid} \\to \\text{Base} + \\text{Hydrogen}\\)",
      "\\(\\text{Metal oxide} + \\text{Acid} \\to \\text{Salt} + \\text{Oxygen}\\)"],
     "B", "OSC", "easy",
     "• Basic metal oxides neutralize acids forming salt and water: \\(\\text{Metal Oxide} + \\text{Acid} \\to \\text{Salt} + \\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    ("""What happens when black Copper(II) Oxide (\\(\\text{CuO}\\)) powder is stirred with warm dilute hydrochloric acid?""",
     ["The powder turns yellow and releases oxygen gas",
      "The black copper oxide dissolves, and the solution turns a characteristic clear bluish-green due to the formation of Copper(II) Chloride (\\(\\text{CuCl}_2\\))",
      "Red copper metal precipitates immediately",
      "No change occurs because copper oxide is inert"],
     "B", "OSC", "medium",
     "• \\(\\text{CuO (black)} + 2\\text{HCl} \\to \\text{CuCl}_2\\text{ (bluish-green solution)} + \\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    ("""Because metal oxides react with acids to form salt and water (analogous to neutralization), metal oxides are classified as:""",
     ["Acidic oxides", "Basic oxides", "Neutral gases", "Amphoteric salts"],
     "B", "OSC", "easy",
     "• Most metal oxides (like \\(\\text{Na}_2\\text{O}, \\text{CaO}, \\text{MgO}, \\text{CuO}\\)) are basic oxides.\nCorrect Choice is (B)."),

    ("""What type of oxides are NON-METAL oxides such as carbon dioxide (\\(\\text{CO}_2\\)) and sulphur dioxide (\\(\\text{SO}_2\\))?""",
     ["Basic oxides", "Acidic oxides", "Neutral salts", "Alkaline ores"],
     "B", "OSC", "easy",
     "• Non-metal oxides dissolve in water to form acids (e.g. \\(\\text{CO}_2 + \\text{H}_2\\text{O} \\to \\text{H}_2\\text{CO}_3\\)) and neutralize bases, making them acidic oxides.\nCorrect Choice is (B)."),

    ("""What is observed when carbon dioxide gas (\\(\\text{CO}_2\\)) is bubbled through a clear solution of lime water (\\(\\text{Ca(OH)}_2\\))?""",
     ["The solution turns deep red",
      "The lime water turns milky due to the formation of an insoluble white precipitate of Calcium Carbonate (\\(\\text{CaCO}_3\\))",
      "A pop sound is heard",
      "The solution boils vigorously"],
     "B", "OSC", "easy",
     "• \\(\\text{Ca(OH)}_2 + \\text{CO}_2 \\to \\text{CaCO}_3\\downarrow\\text{ (milky white)} + \\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    ("""What happens when carbon dioxide gas is passed in EXCESS through the milky lime water solution?""",
     ["The milkiness turns dark black",
      "The milky precipitate dissolves completely and the solution becomes clear again due to the formation of soluble Calcium Bicarbonate (\\(\\text{Ca(HCO}_3)_2\\))",
      "The test tube shatters",
      "Lime water decomposes into metallic calcium"],
     "B", "OSC", "medium",
     "• Excess \\(\\text{CO}_2\\) converts insoluble \\(\\text{CaCO}_3\\) into soluble calcium bicarbonate: \\(\\text{CaCO}_3 + \\text{H}_2\\text{O} + \\text{CO}_2 \\to \\text{Ca(HCO}_3)_2\\text{ (clear solution)}\\).\nCorrect Choice is (B)."),

    ("""What is an 'AMPHOTERIC OXIDE'?""",
     ["An oxide that does not react with any chemical",
      "A metallic oxide that reacts with BOTH acids and strong bases to produce salt and water",
      "An oxide that dissolves only in alcohol",
      "An oxide that explodes in air"],
     "B", "OSC", "easy",
     "• Amphoteric oxides (such as \\(\\text{ZnO}\\) and \\(\\text{Al}_2\\text{O}_3\\)) exhibit both basic and acidic properties.\nCorrect Choice is (B)."),

    ("""Which of the following pairs of oxides are AMPHOTERIC?""",
     ["\\(\\text{Na}_2\\text{O}\\) and \\(\\text{K}_2\\text{O}\\)",
      "\\(\\text{ZnO}\\) (Zinc oxide) and \\(\\text{Al}_2\\text{O}_3\\) (Aluminium oxide)",
      "\\(\\text{CaO}\\) and \\(\\text{MgO}\\)",
      "\\(\\text{CO}_2\\) and \\(\\text{SO}_2\\)"],
     "B", "OSC", "easy",
     "• Both \\(\\text{ZnO}\\) and \\(\\text{Al}_2\\text{O}_3\\) react with acids as well as alkalis, classifying them as amphoteric oxides.\nCorrect Choice is (B)."),

    ("""What salt is formed when Aluminium Oxide (\\(\\text{Al}_2\\text{O}_3\\)) reacts with hot concentrated Sodium Hydroxide (\\(\\text{NaOH}\\))?""",
     ["Aluminium chloride",
      "Sodium aluminate (\\(\\text{NaAlO}_2\\))",
      "Sodium oxide",
      "Aluminium hydroxide"],
     "B", "OSC", "medium",
     "• \\(\\text{Al}_2\\text{O}_3 + 2\\text{NaOH} \\to 2\\text{NaAlO}_2\\text{ (Sodium aluminate)} + \\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    ("""Which of the following non-metal oxides is NEUTRAL (neither acidic nor basic)?""",
     ["Carbon dioxide (\\(\\text{CO}_2\\))",
      "Carbon monoxide (\\(\\text{CO}\\))",
      "Sulphur trioxide (\\(\\text{SO}_3\\))",
      "Nitrogen dioxide (\\(\\text{NO}_2\\))"],
     "B", "OSC", "medium",
     "• Carbon monoxide (\\(\\text{CO}\\)), nitrous oxide (\\(\\text{N}_2\\text{O}\\)), and nitric oxide (\\(\\text{NO}\\)) are neutral oxides.\nCorrect Choice is (B)."),

    # 21-30: Reaction with carbonates, bicarbonates, and neutralization
    ("""What three products are formed when an acid reacts with a metal carbonate or metal bicarbonate?""",
     ["Salt + Hydrogen gas only",
      "Salt + Water + Carbon dioxide gas (\\(\\text{CO}_2\\uparrow\\))",
      "Metal + Oxygen gas + Water",
      "Base + Nitrogen gas + Salt"],
     "B", "OSC", "easy",
     "• \\(\\text{Carbonate/Bicarbonate} + \\text{Acid} \\to \\text{Salt} + \\text{H}_2\\text{O} + \\text{CO}_2\\uparrow\\).\nCorrect Choice is (B)."),

    ("""What is observed when dilute hydrochloric acid is poured over marble chips (\\(\\text{CaCO}_3\\)) or baking soda (\\(\\text{NaHCO}_3\\))?""",
     ["A pale blue precipitate forms",
      "Brisk effervescence occurs with the rapid evolution of a colorless, odorless gas (\\(\\text{CO}_2\\))",
      "A pop sound is produced",
      "The liquid freezes instantly"],
     "B", "OSC", "easy",
     "• Brisk effervescence occurs due to the rapid release of carbon dioxide gas bubbles.\nCorrect Choice is (B)."),

    ("""What is the balanced equation for the reaction of sodium carbonate with dilute hydrochloric acid?""",
     ["\\(\\text{Na}_2\\text{CO}_3 + \\text{HCl} \\to \\text{NaCl} + \\text{H}_2\\text{O} + \\text{CO}_2\\)",
      "\\(\\text{Na}_2\\text{CO}_3 + 2\\text{HCl} \\to 2\\text{NaCl} + \\text{H}_2\\text{O} + \\text{CO}_2\\uparrow\\)",
      "\\(\\text{Na}_2\\text{CO}_3 + 2\\text{HCl} \\to \\text{Na}_2\\text{Cl}_2 + \\text{H}_2\\text{CO}_3\\)",
      "\\(\\text{NaCO}_3 + \\text{HCl} \\to \\text{NaCl} + \\text{CO}_2\\)"],
     "B", "OSC", "easy",
     "• \\(\\text{Na}_2\\text{CO}_3 + 2\\text{HCl} \\to 2\\text{NaCl} + \\text{H}_2\\text{O} + \\text{CO}_2\\uparrow\\).\nCorrect Choice is (B)."),

    ("""What is the fundamental ionic equation that describes the NEUTRALIZATION of an acid by an alkali?""",
     ["\\(\\text{Na}^+ + \\text{Cl}^- \\to \\text{NaCl}\\)",
      "\\(\\text{H}^+(aq) + \\text{OH}^-(aq) \\to \\text{H}_2\\text{O}(l)\\)",
      "\\(2\\text{H}^+ + \\text{O}^{2-} \\to \\text{H}_2\\text{O}\\)",
      "\\(\\text{Acid} + \\text{Metal} \\to \\text{Salt} + \\text{H}_2\\)"],
     "B", "OSC", "easy",
     "• The universal net ionic neutralization equation is \\(\\text{H}^+ + \\text{OH}^- \\to \\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    ("""Is the chemical reaction of neutralization exothermic or endothermic?""",
     ["Exothermic (releases heat energy)",
      "Endothermic (absorbs heat, feels cold)",
      "Neither absorbs nor releases any energy",
      "Varies with atmospheric pressure"],
     "A", "OSC", "easy",
     "• Neutralization is strongly exothermic; the temperature of the reaction mixture rises noticeably.\nCorrect Choice is (A)."),

    ("""What is the standard enthalpy of neutralization for a strong acid with a strong base at \\(25^\\circ\\text{C}\\)?""",
     ["\\(-10.5\\text{ kJ/mol}\\)",
      "\\(-57.1\\text{ kJ/mol}\\) (or \\(-57.3\\text{ kJ/mol}\\))",
      "\\(+57.1\\text{ kJ/mol}\\)",
      "\\(0\\text{ kJ/mol}\\)"],
     "B", "OSC", "medium",
     "• Neutralizing 1 mole of \\(\\text{H}^+\\) by 1 mole of \\(\\text{OH}^-\\) consistently releases \\(57.1\\text{ to } 57.3\\text{ kJ}\\) of thermal energy.\nCorrect Choice is (B)."),

    ("""Why does a fire extinguisher containing sodium bicarbonate solution and a glass vial of sulphuric acid generate foam/gas to smother fires?""",
     ["Because the reaction generates oxygen gas",
      "Mixing the two chemicals instantly produces a large volume of carbon dioxide gas (\\(\\text{CO}_2\\)), which is heavier than air and blankets the fire, cutting off oxygen supply",
      "Because sulphuric acid freezes the flames",
      "Because sodium bicarbonate absorbs heat completely"],
     "B", "OSC", "easy",
     "• \\(2\\text{NaHCO}_3 + \\text{H}_2\\text{SO}_4 \\to \\text{Na}_2\\text{SO}_4 + 2\\text{H}_2\\text{O} + 2\\text{CO}_2\\uparrow\\); \\(\\text{CO}_2\\) displaces atmospheric oxygen, smothering the flame.\nCorrect Choice is (B)."),

    ("""Assertion (A): When eggshells (calcium carbonate) are placed in vinegar (acetic acid), bubbles of gas are evolved.\nReason (R): Acetic acid reacts with the calcium carbonate shell to produce carbon dioxide gas and water.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "• Eggshells are predominantly \\(\\text{CaCO}_3\\); reaction with acid releases effervescent \\(\\text{CO}_2\\).\nCorrect Choice is (A)."),

    ("""Assertion (A): Copper metal dissolves in dilute hydrochloric acid with brisk effervescence of hydrogen gas.\nReason (R): Copper is more electropositive than hydrogen in the activity series.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is false, but (R) is true",
      "Both (A) and (R) are false"],
     "D", "OAR", "medium",
     "• Copper is LESS reactive than hydrogen and lies below it in the activity series; it does not react with dilute \\(\\text{HCl}\\) to evolve \\(\\text{H}_2\\). Both statements are false.\nCorrect Choice is (D)."),

    ("""State True or False: Baking powder contains sodium bicarbonate mixed with a mild edible organic acid such as tartaric acid.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. When heated with moisture during baking, tartaric acid reacts with \\(\\text{NaHCO}_3\\) to generate \\(\\text{CO}_2\\) gas, making cakes light and spongy without bitter aftertaste.\nCorrect Choice is (A)."),

    # 31-40: Fill in blanks and applied reactions
    ("""Fill in the blank: \\(\\text{Acid} + \\text{Active Metal} \\to \\text{Salt} +\\) ________.""",
     ["Oxygen gas", "Hydrogen gas (\\(\\text{H}_2\\))", "Water", "Nitrogen"],
     "B", "OFB", "easy",
     "• Hydrogen gas is evolved.\nCorrect Choice is (B)."),

    ("""Fill in the blank: \\(\\text{Metal Carbonate} + \\text{Acid} \\to \\text{Salt} + \\text{Water} +\\) ________.""",
     ["Hydrogen gas", "Carbon dioxide gas (\\(\\text{CO}_2\\))", "Carbon monoxide", "Methane"],
     "B", "OFB", "easy",
     "• Carbon dioxide gas is produced.\nCorrect Choice is (B)."),

    ("""Fill in the blank: \\(\\text{Basic Metal Oxide} + \\text{Acid} \\to \\text{Salt} +\\) ________.""",
     ["Water (\\(\\text{H}_2\\text{O}\\))", "Hydrogen gas", "Oxygen gas", "Carbon dioxide"],
     "A", "OFB", "easy",
     "• Metal oxide + Acid yields Salt + Water.\nCorrect Choice is (A)."),

    ("""What is the formula of the gas that turns moist acidified potassium dichromate paper from orange to green?""",
     ["\\(\\text{CO}_2\\)", "\\(\\text{SO}_2\\) (Sulphur dioxide)", "\\(\\text{H}_2\\)", "\\(\\text{O}_2\\)"],
     "B", "OSC", "medium",
     "• Sulphur dioxide (\\(\\text{SO}_2\\)) reduces orange dichromate to green chromium sulphate (\\(\\text{Cr}^{3+}\\)).\nCorrect Choice is (B)."),

    ("""Which chemical reaction explains why white wash on walls (slaked lime) develops a shiny, hard white finish after two to three days?""",
     ["Evaporation of all water",
      "Calcium hydroxide in lime slowly absorbs atmospheric carbon dioxide (\\(\\text{CO}_2\\)) to form a thin, shiny layer of hard Calcium Carbonate (\\(\\text{CaCO}_3\\))",
      "Reaction with oxygen to form calcium peroxide",
      "Formation of calcium chloride"],
     "B", "OSC", "easy",
     "• \\(\\text{Ca(OH)}_2 + \\text{CO}_2 \\to \\text{CaCO}_3 + \\text{H}_2\\text{O}\\); white insoluble calcium carbonate gives walls a bright reflective sheen.\nCorrect Choice is (B)."),

    ("""What gas is evolved when concentrated sulphuric acid is added to sodium chloride (\\(\\text{NaCl}\\)) crystals?""",
     ["Chlorine gas (\\(\\text{Cl}_2\\))",
      "Hydrogen chloride gas (\\(\\text{HCl}\\))",
      "Sulphur dioxide gas (\\(\\text{SO}_2\\))",
      "Hydrogen gas (\\(\\text{H}_2\\))"],
     "B", "OSC", "medium",
     "• \\(\\text{NaCl} + \\text{H}_2\\text{SO}_4 \\to \\text{NaHSO}_4 + \\text{HCl}\\uparrow\\) (pungent choking hydrogen chloride fumes).\nCorrect Choice is (B)."),

    ("""How can you distinguish between carbon dioxide (\\(\\text{CO}_2\\)) and sulphur dioxide (\\(\\text{SO}_2\\)) since both turn lime water milky?""",
     ["\\(\\text{SO}_2\\) has a burning sulphur smell and turns acidified potassium dichromate paper green, whereas \\(\\text{CO}_2\\) is odorless and has no effect on dichromate paper",
      "\\(\\text{CO}_2\\) burns with a pop sound",
      "\\(\\text{SO}_2\\) is completely odorless",
      "\\(\\text{CO}_2\\) is a green gas"],
     "A", "OSC", "hard",
     "• \\(\\text{SO}_2\\) has the characteristic smell of burning sulphur and is a reducing agent that turns acidified dichromate paper green, whereas \\(\\text{CO}_2\\) does not.\nCorrect Choice is (A)."),

    ("""What is the salt produced when calcium hydroxide reacts with nitric acid?""",
     ["Calcium sulphate", "Calcium nitrate (\\(\\text{Ca(NO}_3)_2\\))", "Calcium carbonate", "Calcium nitride"],
     "B", "OSC", "easy",
     "• \\(\\text{Ca(OH)}_2 + 2\\text{HNO}_3 \\to \\text{Ca(NO}_3)_2 + 2\\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    ("""What is the salt produced when potassium hydroxide neutralizes sulphuric acid in a \\(2:1\\) molar ratio?""",
     ["Potassium bisulphate", "Potassium sulphate (\\(\\text{K}_2\\text{SO}_4\\))", "Potassium sulphide", "Potassium sulphite"],
     "B", "OSC", "easy",
     "• \\(2\\text{KOH} + \\text{H}_2\\text{SO}_4 \\to \\text{K}_2\\text{SO}_4 + 2\\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    ("""Which gas extinguishes a burning candle without producing any explosion or pop sound?""",
     ["Hydrogen gas (\\(\\text{H}_2\\))",
      "Carbon dioxide gas (\\(\\text{CO}_2\\))",
      "Oxygen gas (\\(\\text{O}_2\\))",
      "Acetylene gas"],
     "B", "OSC", "easy",
     "• Carbon dioxide does not support combustion and immediately smothers a burning candle.\nCorrect Choice is (B).")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("""What gas is released when zinc reacts with dilute hydrochloric acid?""",
     ["Oxygen", "Hydrogen", "Carbon dioxide", "Nitrogen"],
     "B", "OSC", "easy",
     "• Active metals release hydrogen gas.\nCorrect Choice is (B)."),

    ("""What sound does hydrogen gas make when ignited?""",
     ["Hissing sound", "Pop sound", "Whistling sound", "No sound"],
     "B", "OSC", "easy",
     "• Hydrogen burns with a pop sound.\nCorrect Choice is (B)."),

    ("""What gas is released when dilute hydrochloric acid is added to sodium carbonate?""",
     ["Hydrogen", "Carbon dioxide (\\(\\text{CO}_2\\))", "Oxygen", "Ammonia"],
     "B", "OSC", "easy",
     "• Carbonates liberate \\(\\text{CO}_2\\) gas.\nCorrect Choice is (B)."),

    ("""What test proves the presence of carbon dioxide gas?""",
     ["It burns with a pop sound", "It turns lime water milky", "It rekindles a glowing splint", "It turns red litmus blue"],
     "B", "OSC", "easy",
     "• \\(\\text{CO}_2\\) turns lime water milky.\nCorrect Choice is (B)."),

    ("""What is the reaction between an acid and a base called?""",
     ["Precipitation", "Neutralization", "Oxidation", "Electrolysis"],
     "B", "OSC", "easy",
     "• Acid + Base \\(\\to\\) Salt + Water is neutralization.\nCorrect Choice is (B)."),

    ("""What are the products of a neutralization reaction?""",
     ["Salt and Hydrogen", "Salt and Water", "Acid and Gas", "Base and Salt"],
     "B", "OSC", "easy",
     "• Salt and water are formed.\nCorrect Choice is (B)."),

    ("""What type of oxide is Magnesium Oxide (\\(\\text{MgO}\\))?""",
     ["Acidic oxide", "Basic oxide", "Neutral oxide", "Amphoteric oxide"],
     "B", "OSC", "easy",
     "• Metal oxides like \\(\\text{MgO}\\) are basic oxides.\nCorrect Choice is (B)."),

    ("""What type of oxide is Carbon Dioxide (\\(\\text{CO}_2\\))?""",
     ["Acidic oxide", "Basic oxide", "Neutral oxide", "Metallic oxide"],
     "A", "OSC", "easy",
     "• Non-metal oxides like \\(\\text{CO}_2\\) are acidic oxides.\nCorrect Choice is (A)."),

    ("""Which metal oxide is amphoteric?""",
     ["\\(\\text{Na}_2\\text{O}\\)", "\\(\\text{CaO}\\)", "\\(\\text{ZnO}\\) (Zinc oxide)", "\\(\\text{CuO}\\)"],
     "C", "OSC", "easy",
     "• Zinc oxide (\\(\\text{ZnO}\\)) is amphoteric.\nCorrect Choice is (C)."),

    ("""What color is Copper(II) Oxide powder?""",
     ["White", "Black", "Blue", "Red"],
     "B", "OSC", "easy",
     "• \\(\\text{CuO}\\) is black.\nCorrect Choice is (B)."),

    ("""What is the color of copper chloride solution formed when black \\(\\text{CuO}\\) dissolves in \\(\\text{HCl}\\)?""",
     ["Colorless", "Bluish-green", "Deep purple", "Yellow"],
     "B", "OSC", "easy",
     "• Copper(II) chloride solution is bluish-green.\nCorrect Choice is (B)."),

    ("""Which metal does not liberate hydrogen gas with dilute hydrochloric acid?""",
     ["Iron", "Magnesium", "Copper", "Zinc"],
     "C", "OSC", "easy",
     "• Copper is unreactive towards dilute \\(\\text{HCl}\\).\nCorrect Choice is (C)."),

    ("""What is the formula of the precipitate that makes lime water milky?""",
     ["\\(\\text{CaCl}_2\\)", "\\(\\text{CaCO}_3\\) (Calcium carbonate)", "\\(\\text{Ca(OH)}_2\\)", "\\(\\text{CaO}\\)"],
     "B", "OSC", "easy",
     "• Insoluble \\(\\text{CaCO}_3\\) causes the white milkiness.\nCorrect Choice is (B)."),

    ("""What happens when excess \\(\\text{CO}_2\\) is passed through milky lime water?""",
     ["Turns black", "Milkiness disappears (turns clear)", "Turns blue", "Explodes"],
     "B", "OSC", "easy",
     "• Soluble calcium bicarbonate \\(\\text{Ca(HCO}_3)_2\\) is formed, clearing the solution.\nCorrect Choice is (B)."),

    ("""Why does zinc react with both \\(\\text{HCl}\\) and \\(\\text{NaOH}\\) to release hydrogen?""",
     ["Zinc is a radioactive element", "Zinc is an amphoteric metal", "Zinc is a noble gas", "Zinc has no electrons"],
     "B", "OSC", "easy",
     "• Zinc exhibits amphoteric reactivity with both acids and strong bases.\nCorrect Choice is (B)."),

    ("""What salt is formed when sodium hydroxide neutralizes hydrochloric acid?""",
     ["Sodium sulphate", "Sodium chloride (\\(\\text{NaCl}\\))", "Sodium nitrate", "Sodium carbonate"],
     "B", "OSC", "easy",
     "• \\(\\text{NaOH} + \\text{HCl} \\to \\text{NaCl} + \\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    ("""Is heat absorbed or released during acid-base neutralization?""",
     ["Absorbed (endothermic)", "Released (exothermic)", "Neither", "Varies randomly"],
     "B", "OSC", "easy",
     "• Neutralization is always an exothermic reaction.\nCorrect Choice is (B)."),

    ("""What is the net ionic equation of neutralization?""",
     ["\\(\\text{Na}^+ + \\text{Cl}^- \\to \\text{NaCl}\\)",
      "\\(\\text{H}^+ + \\text{OH}^- \\to \\text{H}_2\\text{O}\\)",
      "\\(\\text{Ca}^{2+} + \\text{CO}_3^{2-} \\to \\text{CaCO}_3\\)",
      "\\(\\text{Zn} + 2\\text{H}^+ \\to \\text{Zn}^{2+} + \\text{H}_2\\)"],
     "B", "OSC", "easy",
     "• \\(\\text{H}^+ + \\text{OH}^- \\to \\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    ("""State True or False: Pickles should be stored in aluminium containers.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. Acid in pickles corrodes aluminium, forming toxic salts.\nCorrect Choice is (B)."),

    ("""State True or False: Non-metallic oxides like \\(\\text{SO}_2\\) and \\(\\text{CO}_2\\) are acidic in nature.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Non-metallic oxides dissolve in water to produce acidic solutions.\nCorrect Choice is (A)."),

    ("""What is formed when carbon dioxide reacts with calcium hydroxide?""",
     ["\\(\\text{CaCO}_3 + \\text{H}_2\\text{O}\\)", "\\(\\text{CaCl}_2 + \\text{H}_2\\)", "\\(\\text{CaO} + \\text{O}_2\\)", "\\(\\text{Ca} + \\text{CO}_2\\)"],
     "A", "OSC", "easy",
     "• Neutralization forms \\(\\text{CaCO}_3 + \\text{H}_2\\text{O}\\).\nCorrect Choice is (A)."),

    ("""What gas is evolved when vinegar is mixed with baking soda?""",
     ["Hydrogen", "Carbon dioxide (\\(\\text{CO}_2\\))", "Oxygen", "Chlorine"],
     "B", "OSC", "easy",
     "• Acetic acid + sodium bicarbonate releases \\(\\text{CO}_2\\) gas.\nCorrect Choice is (B)."),

    ("""What is the effect of carbon dioxide gas on a burning splint?""",
     ["Makes it burn brighter", "Extinguishes the flame", "Causes a pop explosion", "Turns the flame green"],
     "B", "OSC", "easy",
     "• Carbon dioxide extinguishes flames.\nCorrect Choice is (B)."),

    ("""What is the reaction product of \\(\\text{MgO} + \\text{H}_2\\text{SO}_4\\)?""",
     ["\\(\\text{MgSO}_4 + \\text{H}_2\\)", "\\(\\text{MgSO}_4 + \\text{H}_2\\text{O}\\)", "\\(\\text{MgS} + \\text{O}_2\\)", "\\(\\text{Mg} + \\text{SO}_2\\)"],
     "B", "OSC", "easy",
     "• Metal oxide + acid forms salt and water: \\(\\text{MgSO}_4 + \\text{H}_2\\text{O}\\).\nCorrect Choice is (B)."),

    ("""Which metal reacts vigorously with cold water to evolve hydrogen gas?""",
     ["Sodium (\\(\\text{Na}\\))", "Copper (\\(\\text{Cu}\\))", "Gold (\\(\\text{Au}\\))", "Iron (\\(\\text{Fe}\\))"],
     "A", "OSC", "easy",
     "• Sodium reacts explosively with cold water: \\(2\\text{Na} + 2\\text{H}_2\\text{O} \\to 2\\text{NaOH} + \\text{H}_2\\uparrow\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: The reaction of \\(\\text{Zn} + 2\\text{NaOH} \\to \\text{Na}_2\\text{ZnO}_2 +\\) ________.""",
     ["\\(\\text{H}_2\\)", "\\(\\text{O}_2\\)", "\\(\\text{H}_2\\text{O}\\)", "\\(\\text{CO}_2\\)"],
     "A", "OFB", "easy",
     "• Hydrogen gas is evolved: \\(\\text{H}_2\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: Limewater turns milky due to the formation of insoluble ________.""",
     ["Calcium sulphate", "Calcium carbonate (\\(\\text{CaCO}_3\\))", "Calcium chloride", "Calcium oxide"],
     "B", "OFB", "easy",
     "• Calcium carbonate precipitate.\nCorrect Choice is (B)."),

    ("""What type of reaction is \\(\\text{HCl} + \\text{NaOH} \\to \\text{NaCl} + \\text{H}_2\\text{O}\\)?""",
     ["Combination reaction", "Neutralization reaction", "Decomposition reaction", "Electrolytic reaction"],
     "B", "OSC", "easy",
     "• Neutralization reaction.\nCorrect Choice is (B)."),

    ("""Which acid is used in lead-acid storage automobile batteries?""",
     ["Hydrochloric acid", "Sulphuric acid (\\(\\text{H}_2\\text{SO}_4\\))", "Nitric acid", "Acetic acid"],
     "B", "OSC", "easy",
     "• Sulphuric acid (battery acid).\nCorrect Choice is (B)."),

    ("""What happens to the temperature of a solution when strong acid and strong base mix?""",
     ["Temperature drops sharply", "Temperature rises (reaction is exothermic)", "Temperature stays identical to 0.001°C", "Freezes into ice"],
     "B", "OSC", "easy",
     "• Neutralization generates heat; temperature rises.\nCorrect Choice is (B).")
]

# 12 Foundation Mock Questions (501-512) with rich embedded vector SVGs
foundation_data = [
    # 501: Hydrogen Gas Pop-Sound Test Delivery Tube Apparatus
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="60" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Hydrogen Gas Generation &amp; Pop-Sound Test</text>
  <!-- Test Tube -->
  <rect x="50" y="70" width="30" height="90" fill="#1e293b" stroke="#94a3b8" rx="4"/>
  <rect x="52" y="120" width="26" height="38" fill="#38bdf8" opacity="0.4"/>
  <!-- Zinc granules -->
  <circle cx="60" cy="150" r="4" fill="#94a3b8"/>
  <circle cx="70" cy="148" r="4" fill="#94a3b8"/>
  <text x="35" y="175" fill="#cbd5e1" font-size="9">Zn + Dilute HCl</text>
  <!-- Delivery Tube -->
  <path d="M 65 70 L 65 50 L 170 50 L 170 140" fill="none" stroke="#60a5fa" stroke-width="2.5"/>
  <!-- Soap solution trough -->
  <rect x="140" y="135" width="60" height="35" fill="#334155" stroke="#94a3b8" rx="2"/>
  <text x="145" y="185" fill="#cbd5e1" font-size="8">Soap Solution</text>
  <!-- Soap bubble rising -->
  <circle cx="210" cy="100" r="14" fill="#38bdf8" opacity="0.3" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="195" y="103" fill="#38bdf8" font-size="8">H₂ Bubble</text>
  <!-- Burning Candle -->
  <line x1="260" y1="90" x2="260" y2="120" stroke="#f59e0b" stroke-width="4"/>
  <polygon points="260,75 255,88 265,88" fill="#ef4444"/>
  <text x="235" y="70" fill="#fde047" font-size="12" font-weight="bold">💥 POP!</text>
  <text x="40" y="210" fill="#34d399" font-size="10">2 H₂ + O₂ ⟶ 2 H₂O (Rapid explosion with pop sound)</text>
</svg>
</div>
In the hydrogen test apparatus shown above, why does the hydrogen gas bubble burst with a distinct 'pop' sound when brought near the burning candle flame?""",
     ["Because soap bubbles contain gunpowder",
      "Because hydrogen gas has a wide flammability range and reacts instantaneously with atmospheric oxygen in an exothermic micro-explosion",
      "Because the candle flame melts the delivery glass tube",
      "Because water vapor expands slowly"],
     "B", "OSC", "medium",
     "• Hydrogen forms an explosive mixture with air. The micro-detonation produces sudden thermal expansion of gases, creating a characteristic acoustic shockwave ('pop' sound).\nCorrect Choice is (B)."),

    # 502: Lime Water Milky Test with CO2 Evolution
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="70" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Testing CO₂ with Lime Water Ca(OH)₂</text>
  <!-- Tube 1: Generator -->
  <rect x="40" y="70" width="30" height="90" fill="#1e293b" stroke="#94a3b8" rx="4"/>
  <text x="15" y="180" fill="#cbd5e1" font-size="9">Na₂CO₃ + HCl</text>
  <text x="45" y="115" fill="#fde047" font-size="8">CO₂ ↗</text>
  <!-- Delivery Tube -->
  <path d="M 55 70 L 55 50 L 215 50 L 215 130" fill="none" stroke="#60a5fa" stroke-width="2.5"/>
  <!-- Tube 2: Lime Water -->
  <rect x="200" y="90" width="30" height="90" fill="#1e293b" stroke="#94a3b8" rx="4"/>
  <rect x="202" y="125" width="26" height="53" fill="#f8fafc" opacity="0.8"/>
  <text x="180" y="195" fill="#86efac" font-size="9" font-weight="bold">Turns Milky White!</text>
  <text x="180" y="208" fill="#cbd5e1" font-size="8">CaCO₃ precipitate</text>
  <!-- Equation -->
  <text x="40" y="222" fill="#38bdf8" font-size="9">Ca(OH)₂ + CO₂ ⟶ CaCO₃↓ (Milky) + H₂O</text>
</svg>
</div>
In the lime water experiment above, what chemical transformation causes the transparent lime water (\\(\\text{Ca(OH)}_2\\)) to turn cloudy and milky white?""",
     ["Lime water boils and produces steam bubbles",
      "Gaseous \\(\\text{CO}_2\\) reacts with dissolved calcium hydroxide to form an insoluble white precipitate of Calcium Carbonate (\\(\\text{CaCO}_3\\))",
      "Calcium chloride crystallizes out",
      "Nitrogen gas forms an emulsion"],
     "B", "OSC", "easy",
     "• Precipitation of insoluble calcium carbonate particles suspended in the liquid scatters light, imparting a distinct milky appearance.\nCorrect Choice is (B)."),

    # 503: Excess CO2 Dissolving Milkiness Mechanism
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Milkiness Disappearance by Excess CO₂</text>
  <!-- Step 1: Initial Precipitation -->
  <rect x="25" y="55" width="135" height="85" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="35" y="75" fill="#fde047" font-size="10" font-weight="bold">Limited CO₂:</text>
  <text x="35" y="95" fill="#cbd5e1" font-size="9">Insoluble CaCO₃ forms</text>
  <text x="35" y="120" fill="#f8fafc" font-size="11" font-weight="bold">MILKY WHITE</text>
  <!-- Arrow -->
  <text x="165" y="105" fill="#38bdf8" font-size="14">→</text>
  <!-- Step 2: Excess CO2 -->
  <rect x="180" y="55" width="135" height="85" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="190" y="75" fill="#34d399" font-size="10" font-weight="bold">Excess CO₂ Passed:</text>
  <text x="190" y="95" fill="#cbd5e1" font-size="9">Forms Ca(HCO₃)₂</text>
  <text x="190" y="120" fill="#38bdf8" font-size="11" font-weight="bold">CLEAR SOLUTION</text>
  <text x="35" y="175" fill="#93c5fd" font-size="10">CaCO₃(s) + H₂O(l) + CO₂(g) ⟶ Ca(HCO₃)₂(aq) [Soluble]</text>
</svg>
</div>
Why does the white milkiness completely disappear and revert to a crystal-clear solution when excess \\(\\text{CO}_2\\) gas is bubbled into the test tube?""",
     ["Because the precipitate is pushed to the bottom of the tube",
      "Because excess \\(\\text{CO}_2\\) converts insoluble calcium carbonate into soluble Calcium Bicarbonate (\\(\\text{Ca(HCO}_3)_2\\))",
      "Because carbon dioxide bleaches white chalk",
      "Because water evaporates completely"],
     "B", "OSC", "medium",
     "• The chemical equilibrium converts insoluble \\(\\text{CaCO}_3\\) into water-soluble calcium hydrogen carbonate (\\(\\text{Ca(HCO}_3)_2\\)), clearing the turbidity.\nCorrect Choice is (B)."),

    # 504: Black CuO Dissolution in Dilute Acid
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Reaction of Copper Oxide with Dilute HCl</text>
  <!-- Beaker before -->
  <rect x="35" y="60" width="115" height="80" fill="#1e293b" stroke="#94a3b8" rx="4"/>
  <text x="45" y="80" fill="#f87171" font-size="10" font-weight="bold">Before Stirring:</text>
  <text x="45" y="100" fill="#cbd5e1" font-size="9">Black CuO powder</text>
  <text x="45" y="118" fill="#cbd5e1" font-size="9">+ Colorless Dil. HCl</text>
  <!-- Arrow -->
  <text x="160" y="105" fill="#38bdf8" font-size="18">→</text>
  <!-- Beaker after -->
  <rect x="190" y="60" width="115" height="80" fill="#1e293b" stroke="#34d399" rx="4"/>
  <rect x="192" y="90" width="111" height="48" fill="#06b6d4" opacity="0.6"/>
  <text x="200" y="80" fill="#34d399" font-size="10" font-weight="bold">After Reaction:</text>
  <text x="200" y="115" fill="#fff" font-size="10" font-weight="bold">Bluish-Green CuCl₂</text>
  <text x="40" y="175" fill="#cbd5e1" font-size="10">CuO (black solid) + 2 HCl ⟶ CuCl₂ (bluish-green) + H₂O</text>
  <text x="40" y="195" fill="#fde047" font-size="9">Confirms basic nature of metallic copper oxide</text>
</svg>
</div>
In the experiment shown above, what is the chemical identity of the bluish-green compound formed when black copper oxide dissolves in dilute hydrochloric acid?""",
     ["Copper metal (\\(\\text{Cu}\\))",
      "Copper(II) Chloride (Cupric chloride, \\(\\text{CuCl}_2\\))",
      "Copper sulphate (\\(\\text{CuSO}_4\\))",
      "Copper hydroxide (\\(\\text{Cu(OH)}_2\\))"],
     "B", "OSC", "easy",
     "• \\(\\text{CuO} + 2\\text{HCl} \\to \\text{CuCl}_2 + \\text{H}_2\\text{O}\\). Dissolved cupric ions hydrated in water impart the distinct bluish-green color.\nCorrect Choice is (B)."),

    # 505: Amphoteric Zinc Oxide Dual Nature
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Dual Amphoteric Character of ZnO</text>
  <!-- Central ZnO -->
  <circle cx="170" cy="115" r="30" fill="#334155" stroke="#f59e0b" stroke-width="2"/>
  <text x="155" y="120" fill="#fde047" font-size="12" font-weight="bold">ZnO</text>
  <!-- Left: Acid Reaction -->
  <rect x="25" y="85" width="105" height="60" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="32" y="105" fill="#38bdf8" font-size="10" font-weight="bold">With Acid (HCl):</text>
  <text x="32" y="122" fill="#cbd5e1" font-size="9">Acts as a BASE</text>
  <text x="32" y="138" fill="#38bdf8" font-size="9">ZnO + 2HCl → ZnCl₂</text>
  <!-- Right: Base Reaction -->
  <rect x="210" y="85" width="105" height="60" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="217" y="105" fill="#34d399" font-size="10" font-weight="bold">With Base (NaOH):</text>
  <text x="217" y="122" fill="#cbd5e1" font-size="9">Acts as an ACID</text>
  <text x="217" y="138" fill="#34d399" font-size="8">ZnO+2NaOH→Na₂ZnO₂</text>
  <text x="45" y="190" fill="#fde047" font-size="10">Amphoteric oxides react with BOTH acids and strong alkalis</text>
</svg>
</div>
How does Zinc Oxide (\\(\\text{ZnO}\\)) behave when treated with strong alkali (\\(\\text{NaOH}\\)) versus strong acid (\\(\\text{HCl}\\))?""",
     ["It explodes with acids but does not react with alkalis",
      "It acts as a basic oxide when reacting with acids to produce \\(\\text{ZnCl}_2\\), and acts as an acidic oxide when reacting with alkalis to form \\(\\text{Na}_2\\text{ZnO}_2\\)",
      "It dissolves only in neutral water",
      "It forms zinc metal in both cases"],
     "B", "OSC", "hard",
     "• Amphoteric oxides display dual chemical behavior: acting as a base against acids and as an acid against strong bases.\nCorrect Choice is (B)."),

    # 506: Neutralization Titration Curve & Equivalence Point
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Neutralization Titration Curve (HCl + NaOH)</text>
  <!-- Coordinate axes -->
  <line x1="50" y1="170" x2="300" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="170" x2="50" y2="40" stroke="#94a3b8" stroke-width="2"/>
  <text x="140" y="190" fill="#cbd5e1" font-size="10">Volume of NaOH added (mL)</text>
  <text x="15" y="105" fill="#cbd5e1" font-size="10" transform="rotate(-90 15,105)">pH</text>
  <!-- Sigmoidal titration curve -->
  <path d="M 50 160 L 150 155 Q 165 155 170 105 Q 175 55 190 55 L 290 50" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Equivalence Point -->
  <circle cx="170" cy="105" r="5" fill="#ef4444"/>
  <text x="180" y="110" fill="#f87171" font-size="10" font-weight="bold">Equivalence Point (pH = 7)</text>
  <text x="50" y="210" fill="#34d399" font-size="10">Sudden vertical pH jump occurs at stoichiometric equivalence</text>
</svg>
</div>
In the titration curve above, what chemical event occurs at the exact inflection point (\\(\\text{pH} = 7.0\\)) where the curve turns vertical?""",
     ["The solution runs out of water",
      "All hydrogen ions from \\(\\text{HCl}\\) are stoichiometrically neutralized by hydroxide ions from \\(\\text{NaOH}\\) (\\(\\text{H}^+ + \\text{OH}^- \\to \\text{H}_2\\text{O}\\)), leaving only neutral \\(\\text{NaCl}\\) salt in solution",
      "The beaker cools to 0°C",
      "Phenolphthalein turns bright yellow"],
     "B", "OSC", "medium",
     "• At the equivalence point, moles of \\(\\text{H}^+\\) equal moles of \\(\\text{OH}^-\\), leaving a neutral salt solution of pH 7.\nCorrect Choice is (B)."),

    # 507: Baking Soda Effervescence with Vinegar
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Baking Soda + Vinegar Reaction</text>
  <!-- Conical Flask -->
  <path d="M 120 70 L 80 160 L 220 160 L 180 70 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <!-- Bubbles of CO2 -->
  <circle cx="140" cy="130" r="5" fill="#fde047"/>
  <circle cx="155" cy="115" r="7" fill="#fde047"/>
  <circle cx="165" cy="95" r="6" fill="#fde047"/>
  <circle cx="150" cy="80" r="8" fill="#fde047"/>
  <text x="175" y="85" fill="#fde047" font-size="11" font-weight="bold">CO₂ Bubbles ↗</text>
  <!-- Labels -->
  <text x="35" y="185" fill="#cbd5e1" font-size="10">NaHCO₃ (solid) + CH₃COOH (vinegar) ⟶ CH₃COONa + H₂O + CO₂↑</text>
</svg>
</div>
When sodium bicarbonate reacts with acetic acid as depicted, what causes the dramatic foaming and effervescence?""",
     ["Rapid production of flammable hydrogen gas",
      "Rapid release of carbon dioxide (\\(\\text{CO}_2\\)) gas escaping the liquid mixture",
      "Dissolution of glass by vinegar",
      "Evaporation of alcohol"],
     "B", "OSC", "easy",
     "• Carbon dioxide gas is rapidly liberated, producing vigorous bubbling and foaming.\nCorrect Choice is (B)."),

    # 508: Action of Acid on Metal Carbonate vs Bicarbonate
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="70" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Carbonate vs Bicarbonate Acid Stoichiometry</text>
  <!-- Reaction 1: Carbonate -->
  <rect x="25" y="55" width="290" height="45" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="35" y="75" fill="#38bdf8" font-size="10" font-weight="bold">Carbonate (Na₂CO₃):</text>
  <text x="35" y="90" fill="#cbd5e1" font-size="10">Na₂CO₃ + 2 HCl ⟶ 2 NaCl + H₂O + CO₂↑ (Requires 2 mol HCl)</text>
  <!-- Reaction 2: Bicarbonate -->
  <rect x="25" y="115" width="290" height="45" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="135" fill="#34d399" font-size="10" font-weight="bold">Bicarbonate (NaHCO₃):</text>
  <text x="35" y="150" fill="#cbd5e1" font-size="10">NaHCO₃ + 1 HCl ⟶ 1 NaCl + H₂O + CO₂↑ (Requires 1 mol HCl)</text>
  <text x="45" y="195" fill="#fde047" font-size="10">Both evolve CO₂, but carbonate requires twice the molar amount of acid</text>
</svg>
</div>
How many moles of dilute hydrochloric acid are required to completely decompose \\(1\\text{ mole}\\) of Sodium Carbonate (\\(\\text{Na}_2\\text{CO}_3\\)) versus \\(1\\text{ mole}\\) of Sodium Bicarbonate (\\(\\text{NaHCO}_3\\))?""",
     ["1 mole for carbonate, 2 moles for bicarbonate",
      "2 moles for carbonate, 1 mole for bicarbonate",
      "2 moles for both",
      "1 mole for both"],
     "B", "OSC", "medium",
     "• Carbonate ion (\\(\\text{CO}_3^{2-}\\)) requires \\(2\\text{ H}^+\\) ions to form \\(\\text{H}_2\\text{CO}_3\\) (which breaks down into \\(\\text{H}_2\\text{O} + \\text{CO}_2\\)), whereas bicarbonate (\\(\\text{HCO}_3^-\\)) already carries one proton and requires only \\(1\\text{ H}^+\\).\nCorrect Choice is (B)."),

    # 509: Fire Extinguisher Internal Chemical Mechanism
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Soda-Acid Fire Extinguisher Anatomy</text>
  <!-- Metallic Cylinder -->
  <rect x="130" y="50" width="70" height="130" fill="#b91c1c" stroke="#ef4444" stroke-width="2" rx="10"/>
  <!-- Glass bottle of acid inside -->
  <rect x="150" y="65" width="30" height="40" fill="#94a3b8" stroke="#cbd5e1"/>
  <text x="153" y="85" fill="#0f172a" font-size="7" font-weight="bold">H₂SO₄</text>
  <!-- Solution around -->
  <text x="138" y="145" fill="#fef08a" font-size="8">NaHCO₃ sol.</text>
  <!-- Knob on top -->
  <circle cx="165" cy="45" r="6" fill="#f59e0b"/>
  <!-- Nozzle spray -->
  <line x1="200" y1="65" x2="250" y2="55" stroke="#38bdf8" stroke-width="3"/>
  <text x="215" y="90" fill="#38bdf8" font-size="10" font-weight="bold">CO₂ + Foam Jets</text>
  <text x="35" y="205" fill="#cbd5e1" font-size="9">Striking knob breaks acid vial → Instant CO₂ pressure forces stream out</text>
</svg>
</div>
How does a soda-acid fire extinguisher extinguish fires when activated?""",
     ["It cools the fire with liquid nitrogen",
      "Striking the plunger breaks the sulphuric acid bottle into the sodium bicarbonate solution, generating huge pressure of \\(\\text{CO}_2\\) gas that propels water and blankets the fire, cutting off oxygen",
      "It absorbs air from the room",
      "It produces chlorine gas to kill the flames"],
     "B", "OSC", "medium",
     "• The acid-carbonate reaction instantly generates pressurized carbon dioxide and water, extinguishing flames by cutting off oxygen and cooling the fuel.\nCorrect Choice is (B)."),

    # 510: White Wash Shiny Finish Chemical Equation
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Chemistry of Wall Whitewashing</text>
  <!-- Step 1: Slaking -->
  <rect x="25" y="55" width="290" height="45" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="35" y="75" fill="#fde047" font-size="10" font-weight="bold">Step 1: Slaking of Quicklime</text>
  <text x="35" y="90" fill="#cbd5e1" font-size="9">CaO (Quicklime) + H₂O ⟶ Ca(OH)₂ (Slaked lime) + Intense Heat</text>
  <!-- Step 2: Carbonation on wall -->
  <rect x="25" y="115" width="290" height="45" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="135" fill="#34d399" font-size="10" font-weight="bold">Step 2: Carbonation on Wall Surface (2–3 days)</text>
  <text x="35" y="150" fill="#cbd5e1" font-size="9">Ca(OH)₂ + CO₂ (air) ⟶ CaCO₃ (Hard, shiny marble layer) + H₂O</text>
  <text x="45" y="195" fill="#38bdf8" font-size="10">Slow carbonation creates a durable, weather-resistant white crust</text>
</svg>
</div>
Why does a freshly whitewashed wall look dull on day one but becomes intensely white and lustrous after 2 to 3 days?""",
     ["Because sunlight whitens calcium atoms directly",
      "Because slaked lime (\\(\\text{Ca(OH)}_2\\)) slowly reacts with atmospheric carbon dioxide (\\(\\text{CO}_2\\)) over several days to form a crystalline, reflective film of Calcium Carbonate (\\(\\text{CaCO}_3\\))",
      "Because paint evaporates",
      "Because dust settles on the wall"],
     "B", "OSC", "easy",
     "• Slow absorption of atmospheric \\(\\text{CO}_2\\) forms a thin, tough coat of calcium carbonate, imparting a shiny white finish.\nCorrect Choice is (B)."),

    # 511: Enthalpy of Neutralization Calorimetry
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="70" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Thermochemistry of Strong Acid-Base Neutralization</text>
  <text x="45" y="60" fill="#38bdf8" font-size="12" font-weight="bold">H⁺(aq) + OH⁻(aq) ⟶ H₂O(l)</text>
  <!-- Calorimeter block -->
  <rect x="35" y="75" width="270" height="75" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="45" y="100" fill="#f87171" font-size="11" font-weight="bold">Heat of Neutralization (ΔH_neut):</text>
  <text x="45" y="120" fill="#fde047" font-size="14" font-family="monospace">-57.1 kJ per mole of H₂O formed</text>
  <text x="45" y="140" fill="#cbd5e1" font-size="9">Identical for ANY strong acid with ANY strong base!</text>
  <text x="45" y="180" fill="#34d399" font-size="10">Because both are 100% dissociated, the actual reaction is always identical</text>
</svg>
</div>
Why is the enthalpy of neutralization for ANY strong acid (\\(\\text{HCl}, \\text{HNO}_3\\)) with ANY strong base (\\(\\text{NaOH}, \\text{KOH}\\)) always virtually constant at \\(-57.1\\text{ kJ/mol}\\)?""",
     ["Because all acids contain chlorine",
      "Because strong acids and bases are completely dissociated in water, so in every case the actual net chemical reaction is identical: \\(\\text{H}^+(aq) + \\text{OH}^-(aq) \\to \\text{H}_2\\text{O}(l)\\)",
      "Because calorimeters are standardized to that number",
      "Because strong acids have no chemical bonds"],
     "B", "OSC", "hard",
     "• Spectator ions (\\(\\text{Na}^+, \\text{Cl}^-, \\text{K}^+, \\text{NO}_3^-\\)) do not participate; the net reaction is universally the formation of 1 mole of water from \\(\\text{H}^+\\) and \\(\\text{OH}^-\\), which consistently liberates \\(57.1\\text{ kJ}\\).\nCorrect Choice is (B)."),

    # 512: Reactivity Series Hydrogen Displacement Criterion
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Activity Series &amp; Hydrogen Displacement</text>
  <!-- Above H -->
  <rect x="35" y="50" width="270" height="60" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="45" y="70" fill="#34d399" font-size="10" font-weight="bold">METALS ABOVE HYDROGEN (K, Na, Ca, Mg, Al, Zn, Fe):</text>
  <text x="45" y="88" fill="#cbd5e1" font-size="9">• More electropositive than H → Displace H₂ gas from dilute acids</text>
  <text x="45" y="102" fill="#34d399" font-size="9">✓ Metal + 2H⁺ ⟶ Metal²⁺ + H₂↑</text>
  <!-- Hydrogen Benchmark -->
  <line x1="35" y1="125" x2="305" y2="125" stroke="#f59e0b" stroke-width="2"/>
  <text x="135" y="130" fill="#fde047" font-size="11" font-weight="bold">[ HYDROGEN ]</text>
  <!-- Below H -->
  <rect x="35" y="145" width="270" height="60" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="45" y="165" fill="#f87171" font-size="10" font-weight="bold">METALS BELOW HYDROGEN (Cu, Ag, Au, Pt):</text>
  <text x="45" y="183" fill="#cbd5e1" font-size="9">• Less electropositive than H → CANNOT displace H₂ from dilute acids</text>
  <text x="45" y="198" fill="#fca5a5" font-size="9">✗ Cu + Dil. HCl ⟶ NO REACTION</text>
</svg>
</div>
Based on the Activity Series criterion shown above, which of the following metals will FAIL to liberate hydrogen gas when treated with dilute sulphuric acid?""",
     ["Iron (\\(\\text{Fe}\\))",
      "Zinc (\\(\\text{Zn}\\))",
      "Silver (\\(\\text{Ag}\\))",
      "Magnesium (\\(\\text{Mg}\\))"],
     "C", "OSC", "medium",
     "• Silver (\\(\\text{Ag}\\)) lies below hydrogen in the reactivity series and has a higher standard reduction potential, making it unable to displace hydrogen gas from dilute non-oxidizing acids.\nCorrect Choice is (C).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-5-5.3-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-5-5.3-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-5-5.3-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch5_topic3.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
