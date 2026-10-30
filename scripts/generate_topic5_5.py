# scripts/generate_topic5_5.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-5-5.5"
CHAPTER_NUM = 5

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: Electrolysis basics and electrode conventions
    ("""What is 'ELECTROLYSIS' in chemistry?""",
     ["Melting an ice cube with electricity",
      "The chemical decomposition of an electrolyte in molten or aqueous state caused by the passage of direct electric current (DC)",
      "Generating electricity from chemical batteries",
      "Heating a gas inside a tube"],
     "B", "OSC", "easy",
     "• Electrolysis is the non-spontaneous chemical breakdown of an ionic substance driven by direct electrical current.\nCorrect Choice is (B)."),

    ("""In an electrolytic cell, the ANODE is connected to which terminal of the DC battery, and what electrical charge does it carry?""",
     ["Negative terminal, negatively charged",
      "Positive terminal of battery, positively charged (+ve)",
      "Neutral terminal",
      "Ground terminal"],
     "B", "OSC", "easy",
     "• In an electrolytic cell, the anode is connected to the positive terminal of the power supply and carries a positive charge.\nCorrect Choice is (B)."),

    ("""In an electrolytic cell, the CATHODE is connected to which terminal of the battery, and what electrical charge does it carry?""",
     ["Positive terminal",
      "Negative terminal of battery, negatively charged (-ve)",
      "Zero potential",
      "Both positive and negative alternately"],
     "B", "OSC", "easy",
     "• The cathode is connected to the negative terminal of the DC power supply and carries a negative charge.\nCorrect Choice is (B)."),

    ("""What fundamental chemical reaction ALWAYS takes place at the CATHODE during electrolysis?""",
     ["Oxidation (loss of electrons)",
      "Reduction (gain of electrons: cations gain electrons)",
      "Combustion",
      "Sublimation"],
     "B", "OSC", "easy",
     "• Reduction (gain of electrons) always takes place at the cathode ('Red Cat': Reduction at Cathode).\nCorrect Choice is (B)."),

    ("""What fundamental chemical reaction ALWAYS occurs at the ANODE during electrolysis?""",
     ["Oxidation (loss of electrons: anions or electrode atoms donate electrons)",
      "Reduction (gain of electrons)",
      "Neutralization",
      "Precipitation"],
     "A", "OSC", "easy",
     "• Oxidation (loss of electrons) always takes place at the anode ('An Ox': Anode is Oxidation).\nCorrect Choice is (A)."),

    ("""Why does pure, distilled water NOT undergo electrolysis when an electric current is passed through it?""",
     ["Water absorbs the current and converts it into light",
      "Pure water is an extremely weak electrolyte with an extraordinarily low degree of auto-ionization (\\([\\text{H}^+] = [\\text{OH}^-] = 10^{-7}\\text{ M}\\)), having virtually no free mobile ions to conduct current",
      "Water dissolves the battery",
      "Water contains too many metal ions"],
     "B", "OSC", "medium",
     "• Pure water contains only 1 ion pair per 550 million molecules, making it a very poor electrical conductor without added ions.\nCorrect Choice is (B)."),

    ("""Why are a few drops of dilute Sulphuric Acid (\\(\\text{H}_2\\text{SO}_4\\)) added to water before attempting its electrolysis?""",
     ["To change the color of water to blue",
      "To provide abundant mobile \\(\\text{H}_3\\text{O}^+\\) and \\(\\text{SO}_4^{2-}\\) ions that make water conductive (acidulated water)",
      "To make the water boil faster",
      "To prevent hydrogen from exploding"],
     "B", "OSC", "easy",
     "• Dilute \\(\\text{H}_2\\text{SO}_4\\) acts as a catalyst electrolyte, fully ionizing to enable rapid electrical conduction.\nCorrect Choice is (B)."),

    ("""During the electrolysis of acidulated water, what gas is collected at the CATHODE (-ve electrode)?""",
     ["Oxygen gas (\\(\\text{O}_2\\))",
      "Hydrogen gas (\\(\\text{H}_2\\))",
      "Sulphur dioxide gas (\\(\\text{SO}_2\\))",
      "Chlorine gas (\\(\\text{Cl}_2\\))"],
     "B", "OSC", "easy",
     "• Positively charged \\(\\text{H}^+\\) cations migrate to the negative cathode, gaining electrons to form \\(\\text{H}_2\\) gas.\nCorrect Choice is (B)."),

    ("""During the electrolysis of acidulated water, what gas is collected at the ANODE (+ve electrode)?""",
     ["Hydrogen gas (\\(\\text{H}_2\\))",
      "Oxygen gas (\\(\\text{O}_2\\))",
      "Nitrogen gas (\\(\\text{N}_2\\))",
      "Sulphur trioxide (\\(\\text{SO}_3\\))"],
     "B", "OSC", "easy",
     "• Hydroxide ions / water molecules are oxidized at the positive anode to liberate oxygen gas (\\(\\text{O}_2\\)).\nCorrect Choice is (B)."),

    ("""What is the stoichiometric ratio of the volumes of Hydrogen gas to Oxygen gas collected during the electrolysis of water in a Hofmann voltameter?""",
     ["\\(1 : 1\\)",
      "\\(2 : 1\\) (Volume of \\(\\text{H}_2\\) is double that of \\(\\text{O}_2\\))",
      "\\(1 : 2\\)",
      "\\(8 : 1\\)"],
     "B", "OSC", "easy",
     "• By water stoichiometry \\(2\\text{H}_2\\text{O} \\to 2\\text{H}_2\\uparrow + \\text{O}_2\\uparrow\\), the volume of hydrogen produced at the cathode is exactly twice the volume of oxygen at the anode.\nCorrect Choice is (B)."),

    # 11-20: Electrolysis of Copper Sulphate solution
    ("""When aqueous copper sulphate (\\(\\text{CuSO}_4\\)) is electrolyzed using INERT carbon (graphite) or platinum electrodes, what is deposited at the cathode?""",
     ["Hydrogen gas",
      "Reddish-brown metallic Copper (\\(\\text{Cu}\\))",
      "Oxygen gas",
      "Sulphur powder"],
     "B", "OSC", "easy",
     "• Copper cations have a higher reduction potential than \\(\\text{H}^+\\) and discharge preferentially at the cathode: \\(\\text{Cu}^{2+} + 2e^- \\to \\text{Cu}(s)\\).\nCorrect Choice is (B)."),

    ("""What gas is evolved at the anode when copper sulphate solution is electrolyzed using INERT electrodes?""",
     ["Hydrogen gas (\\(\\text{H}_2\\))",
      "Oxygen gas (\\(\\text{O}_2\\))",
      "Sulphur dioxide (\\(\\text{SO}_2\\))",
      "Copper vapor"],
     "B", "OSC", "medium",
     "• Hydroxide ions from water discharge preferentially over sulphate ions at an inert anode: \\(4\\text{OH}^- \\to 2\\text{H}_2\\text{O} + \\text{O}_2\\uparrow + 4e^-\\).\nCorrect Choice is (B)."),

    ("""What happens to the blue color of copper sulphate solution when electrolyzed for a prolonged period with INERT graphite electrodes?""",
     ["The blue color intensifies",
      "The blue color gradually fades and eventually turns colorless as \\(\\text{Cu}^{2+}\\) ions are progressively removed from solution",
      "The solution turns blood red",
      "The color remains completely unchanged"],
     "B", "OSC", "medium",
     "• Blue color is due to hydrated \\(\\text{Cu}^{2+}\\) ions. As \\(\\text{Cu}^{2+}\\) is continuously plated out onto the cathode while \\(\\text{H}^+\\) and \\(\\text{SO}_4^{2-}\\) remain, the solution fades into colorless \\(\\text{H}_2\\text{SO}_4\\).\nCorrect Choice is (B)."),

    ("""When copper sulphate solution is electrolyzed using COPPER ELECTRODES (active electrodes), what occurs at the copper ANODE?""",
     ["Oxygen gas is evolved",
      "Metallic copper atoms from the anode oxidize and dissolve into solution as cupric ions (\\(\\text{Cu} \\to \\text{Cu}^{2+} + 2e^-\\)), causing the anode to lose mass",
      "Copper chloride precipitates",
      "The anode thickens with gold"],
     "B", "OSC", "medium",
     "• When active copper anodes are used, copper metal oxidizes preferentially over \\(\\text{OH}^-\\) ions, dissolving into solution: \\(\\text{Cu} \\to \\text{Cu}^{2+} + 2e^-\\).\nCorrect Choice is (B)."),

    ("""When copper sulphate is electrolyzed with COPPER ELECTRODES, what happens to the intensity of the blue color of the electrolyte?""",
     ["It fades completely within 5 minutes",
      "The blue color intensity remains completely constant because the rate of \\(\\text{Cu}^{2+}\\) deposition at the cathode strictly equals the rate of \\(\\text{Cu}^{2+}\\) dissolution from the anode",
      "It turns black",
      "It turns neon green"],
     "B", "OSC", "medium",
     "• The net concentration of \\(\\text{Cu}^{2+}\\) ions in the electrolyte remains invariant, preserving the deep blue coloration.\nCorrect Choice is (B)."),

    ("""In the industrial electrorefining of blister copper, which electrode is made of the IMPURE copper block?""",
     ["The Cathode", "The Anode", "Both electrodes", "Neither electrode"],
     "B", "OSC", "easy",
     "• Impure blister copper is cast as the ANODE (+ve), where copper oxidizes and dissolves into the electrolyte.\nCorrect Choice is (B)."),

    ("""In industrial copper refining, what constitutes the CATHODE on which pure copper deposits?""",
     ["A thick block of wood",
      "A thin strip/sheet of highly pure (99.99%) copper metal",
      "A lead plate",
      "An iron rod"],
     "B", "OSC", "easy",
     "• A thin sheet of pure copper serves as the cathode, growing thicker as pure copper ions discharge onto it.\nCorrect Choice is (B)."),

    ("""What happens to precious noble metal impurities (like Silver and Gold) present in the blister copper anode during electrorefining?""",
     ["They dissolve and plate onto the cathode",
      "They do not oxidize at the anode potential and settle unreacted beneath the anode as valuable 'anode mud' (anode sludge)",
      "They evaporate into air",
      "They neutralize the acid"],
     "B", "OSC", "hard",
     "• Silver and gold have lower oxidation potentials than copper; they fall to the tank floor as 'anode mud' and are recovered economically.\nCorrect Choice is (B)."),

    ("""What is 'ELECTROPLATING'?""",
     ["Melting metals using an electric arc",
      "The electrolytic process of depositing a thin, uniform protective or decorative layer of a superior metal (e.g. silver, gold, chromium) onto the surface of a base metal object",
      "Welding metal sheets together",
      "Painting iron with oil paint"],
     "B", "OSC", "easy",
     "• Electroplating uses electrolysis to coat a base metal with a corrosion-resistant or decorative noble metal.\nCorrect Choice is (B)."),

    ("""In an electroplating cell, the article/object to be coated (e.g. an iron spoon to be silver-plated) must ALWAYS be connected as the:""",
     ["Anode (+ve)", "Cathode (-ve)", "Ground wire", "Neutral switch"],
     "B", "OSC", "easy",
     "• The object to be plated must be the CATHODE (-ve) so that positive metal cations (\\(\\text{Ag}^+\\)) migrate towards it and deposit as a solid metal film.\nCorrect Choice is (B)."),

    # 21-30: Electroplating principles and half-reactions
    ("""In silver plating of a copper spoon, what metal must be used as the ANODE, and what solution is used as the electrolyte?""",
     ["Anode: Pure Silver plate; Electrolyte: Sodium argento-cyanide / Silver nitrate solution",
      "Anode: Iron rod; Electrolyte: Copper sulphate",
      "Anode: Carbon rod; Electrolyte: Distilled water",
      "Anode: Lead plate; Electrolyte: Sulphuric acid"],
     "A", "OSC", "medium",
     "• The anode must be pure silver to replenish \\(\\text{Ag}^+\\) ions in the electrolyte (sodium dicyanoargentate or silver salt).\nCorrect Choice is (A)."),

    ("""Why is alternating current (AC) NEVER used for electroplating or electrolysis?""",
     ["AC current is too low in voltage",
      "AC reverses its electrical polarity 50 times per second (in a 50 Hz supply), causing metal to deposit in one half-cycle and dissolve back in the next half-cycle, resulting in zero net plating",
      "AC cannot flow through water",
      "AC produces sparks in liquids"],
     "B", "OSC", "medium",
     "• Constant unidirectional DC is essential. Reversing AC polarity alternately plates and un-plates the electrode, preventing continuous deposition.\nCorrect Choice is (B)."),

    ("""What is the half-reaction occurring at the cathode during water electrolysis?""",
     ["\\(2\\text{H}^+ + 2e^- \\to \\text{H}_2\\uparrow\\) (Reduction)",
      "\\(4\\text{OH}^- \\to 2\\text{H}_2\\text{O} + \\text{O}_2 + 4e^-\\)",
      "\\(\\text{H}_2 \\to 2\\text{H}^+ + 2e^-\\)",
      "\\(\\text{O}_2 + 4e^- \\to 2\\text{O}^{2-}\\)"],
     "A", "OSC", "easy",
     "• At the cathode, hydrogen ions gain electrons (reduction): \\(2\\text{H}^+ + 2e^- \\to \\text{H}_2\\uparrow\\).\nCorrect Choice is (A)."),

    ("""What is the half-reaction occurring at the anode during the electrolysis of acidulated water?""",
     ["\\(2\\text{H}^+ + 2e^- \\to \\text{H}_2\\)",
      "\\(4\\text{OH}^-(aq) \\to 2\\text{H}_2\\text{O}(l) + \\text{O}_2(g)\\uparrow + 4e^-\\) (Oxidation)",
      "\\(\\text{SO}_4^{2-} \\to \\text{SO}_2 + \\text{O}_2\\)",
      "\\(\\text{H}_2\\text{O} + e^- \\to \\text{OH}^-\\text{ only}\\)"],
     "B", "OSC", "medium",
     "• Hydroxide ions discharge at the anode, losing electrons: \\(4\\text{OH}^- \\to 2\\text{H}_2\\text{O} + \\text{O}_2\\uparrow + 4e^-\\).\nCorrect Choice is (B)."),

    ("""Assertion (A): During the electrolysis of water, the volume of hydrogen gas collected is exactly double the volume of oxygen gas.\nReason (R): Every water molecule (\\(\\text{H}_2\\text{O}\\)) contains two hydrogen atoms bonded to one oxygen atom in a 2:1 atomic and molar ratio.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "• Chemical decomposition \\(2\\text{H}_2\\text{O} \\to 2\\text{H}_2 + \\text{O}_2\\) produces 2 moles of \\(\\text{H}_2\\) gas for every 1 mole of \\(\\text{O}_2\\) gas, yielding a \\(2:1\\) volume ratio by Avogadro's law.\nCorrect Choice is (A)."),

    ("""Assertion (A): In the electrorefining of copper, the cathode grows thicker while the anode shrinks.\nReason (R): Copper atoms from the impure anode oxidize into \\(\\text{Cu}^{2+}\\) ions, while \\(\\text{Cu}^{2+}\\) ions from the solution reduce onto the cathode as pure copper.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "• Anode loses mass via oxidation; cathode gains equal mass via reduction.\nCorrect Choice is (A)."),

    ("""State True or False: Cations carry positive electrical charge and migrate towards the cathode during electrolysis.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Cations (+ve) are attracted to the negative cathode (-ve).\nCorrect Choice is (A)."),

    ("""State True or False: Anions carry negative electrical charge and migrate towards the anode during electrolysis.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Anions (-ve) migrate towards the positive anode (+ve).\nCorrect Choice is (A)."),

    ("""Why is chromium electroplated onto bicycle handlebars, car bumpers, and bathroom fixtures?""",
     ["Chromium is cheaper than plastic",
      "Chromium produces a brilliant decorative mirror-like shine, resists atmospheric corrosion, and provides high scratch resistance",
      "Chromium is magnetic",
      "Chromium dissolves in rain"],
     "B", "OSC", "easy",
     "• Chromium electroplating provides decorative shine, corrosion resistance, and high hardness.\nCorrect Choice is (B)."),

    ("""Which of the following compounds is a NON-ELECTROLYTE that does not conduct electricity in molten or aqueous state?""",
     ["Sodium chloride (\\(\\text{NaCl}\\))",
      "Copper sulphate (\\(\\text{CuSO}_4\\))",
      "Cane Sugar (Sucrose, \\(\\text{C}_{12}\\text{H}_{22}\\text{O}_{11}\\))",
      "Sulphuric acid (\\(\\text{H}_2\\text{SO}_4\\))"],
     "C", "OSC", "easy",
     "• Sugar is a covalent compound that does not dissociate into ions, remaining a non-electrolyte.\nCorrect Choice is (C)."),

    # 31-40: Fill in blanks and applied calculations
    ("""Fill in the blank: The electrode connected to the positive terminal of the DC battery is called the ________.""",
     ["Cathode", "Anode", "Diode", "Triode"],
     "B", "OFB", "easy",
     "• Positive electrode is the anode.\nCorrect Choice is (B)."),

    ("""Fill in the blank: During water electrolysis, \\(20\\text{ mL}\\) of Hydrogen gas is collected at the cathode; the volume of Oxygen collected at the anode will be ________ \\(\\text{mL}\\).""",
     ["\\(5\\)", "\\(10\\)", "\\(20\\)", "\\(40\\)"],
     "B", "OFB", "easy",
     "• Volume ratio \\(\\text{H}_2 : \\text{O}_2 = 2 : 1\\). Therefore, \\(\\text{O}_2\\) volume = \\(\\frac{20}{2} = 10\\text{ mL}\\).\nCorrect Choice is (B)."),

    ("""Fill in the blank: The loss of electrons is called ________, while the gain of electrons is called reduction.""",
     ["Hydration", "Oxidation", "Precipitation", "Neutralization"],
     "B", "OFB", "easy",
     "• Oxidation is loss of electrons (OIL RIG).\nCorrect Choice is (B)."),

    ("""What is the apparatus specifically designed for measuring gas volumes during the electrolysis of water called?""",
     ["Hofmann Voltameter", "Calorimeter", "Spectrophotometer", "Barometer"],
     "A", "OSC", "easy",
     "• The Hofmann voltameter consists of three joined vertical glass cylinders with platinum electrodes for water electrolysis.\nCorrect Choice is (A)."),

    ("""If \\(50\\text{ cm}^3\\) of oxygen gas is produced at the anode during water electrolysis, what volume of hydrogen gas was simultaneously collected at the cathode?""",
     ["\\(25\\text{ cm}^3\\)", "\\(50\\text{ cm}^3\\)", "\\(100\\text{ cm}^3\\)", "\\(200\\text{ cm}^3\\)"],
     "C", "OSC", "easy",
     "• \\(V(\\text{H}_2) = 2 \\times V(\\text{O}_2) = 2 \\times 50 = 100\\text{ cm}^3\\).\nCorrect Choice is (C)."),

    ("""What happens to an iron key when it is electroplated with copper?""",
     ["The iron key becomes lighter",
      "Copper ions from the solution gain electrons at the iron key (cathode) and form a reddish-brown metallic copper coating over the key",
      "The key melts",
      "The key emits chlorine fumes"],
     "B", "OSC", "easy",
     "• \\(\\text{Cu}^{2+} + 2e^- \\to \\text{Cu}\\); metallic copper plates onto the negative cathode (the key).\nCorrect Choice is (B)."),

    ("""Why must the surface of a metal article be thoroughly cleaned with acid and emery paper before electroplating?""",
     ["To change its electrical resistance",
      "To remove grease, dirt, and oxide coatings so that the electroplated metal layer adheres firmly and uniformly without peeling off",
      "To make the metal lighter in weight",
      "To make it radioactive"],
     "B", "OSC", "medium",
     "• Clean metallic contact is crucial; grease or oxides prevent atomic adhesion, causing plated layers to blister or peel.\nCorrect Choice is (B)."),

    ("""What ions are present in an aqueous solution of Copper Sulphate (\\(\\text{CuSO}_4\\))?""",
     ["\\(\\text{Cu}^{2+}\\) and \\(\\text{SO}_4^{2-}\\) from salt, plus \\(\\text{H}^+\\) and \\(\\text{OH}^-\\) from water auto-ionization",
      "\\(\\text{Cu}^+\\) and \\(\\text{S}^{2-}\\) only",
      "\\(\\text{H}_2\\) and \\(\\text{O}_2\\) molecules only",
      "Metallic copper atoms"],
     "A", "OSC", "easy",
     "• Four ionic species are present: \\(\\text{Cu}^{2+}, \\text{SO}_4^{2-}, \\text{H}^+, \\text{OH}^-\\).\nCorrect Choice is (A)."),

    ("""Which metal is extracted commercially on a large scale by the electrolysis of molten bauxite ore dissolved in cryolite (Hall-Héroult process)?""",
     ["Iron", "Aluminium (\\(\\text{Al}\\))", "Copper", "Zinc"],
     "B", "OSC", "easy",
     "• Aluminium is produced globally by molten electrolytic reduction of alumina.\nCorrect Choice is (B)."),

    ("""What term is used for the insoluble residue containing silver, gold, and platinum collected at the bottom of a copper electrorefining cell?""",
     ["Cathode sludge", "Anode mud (anode slime)", "Fly ash", "Slag"],
     "B", "OSC", "easy",
     "• Anode mud contains unreactive precious metals dropped during copper refining.\nCorrect Choice is (B).")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("""What is the positive electrode in an electrolytic cell called?""",
     ["Cathode", "Anode", "Electrolyte", "Separator"],
     "B", "OSC", "easy",
     "• Positive electrode is the anode.\nCorrect Choice is (B)."),

    ("""What is the negative electrode in an electrolytic cell called?""",
     ["Anode", "Cathode", "Filament", "Collector"],
     "B", "OSC", "easy",
     "• Negative electrode is the cathode.\nCorrect Choice is (B)."),

    ("""Which process occurs at the cathode?""",
     ["Oxidation", "Reduction", "Neutralization", "Combustion"],
     "B", "OSC", "easy",
     "• Reduction (gain of electrons) takes place at cathode.\nCorrect Choice is (B)."),

    ("""Which process occurs at the anode?""",
     ["Oxidation", "Reduction", "Precipitation", "Hydration"],
     "A", "OSC", "easy",
     "• Oxidation (loss of electrons) occurs at anode.\nCorrect Choice is (A)."),

    ("""What gas is collected at the cathode in water electrolysis?""",
     ["Oxygen", "Hydrogen", "Chlorine", "Nitrogen"],
     "B", "OSC", "easy",
     "• Hydrogen gas is liberated at the cathode.\nCorrect Choice is (B)."),

    ("""What gas is collected at the anode in water electrolysis?""",
     ["Hydrogen", "Oxygen", "Carbon dioxide", "Helium"],
     "B", "OSC", "easy",
     "• Oxygen gas is liberated at the anode.\nCorrect Choice is (B)."),

    ("""What is the volume ratio of \\(\\text{H}_2\\) to \\(\\text{O}_2\\) in water electrolysis?""",
     ["\\(1 : 1\\)", "\\(2 : 1\\)", "\\(1 : 2\\)", "\\(3 : 1\\)"],
     "B", "OSC", "easy",
     "• Ratio is 2 : 1.\nCorrect Choice is (B)."),

    ("""Why is dilute acid added to water for electrolysis?""",
     ["To make it safe to touch", "To make it an electrical conductor", "To evaporate water", "To neutralize bases"],
     "B", "OSC", "easy",
     "• Pure water does not conduct; acid provides ions.\nCorrect Choice is (B)."),

    ("""In copper electrorefining, the pure copper is deposited at the:""",
     ["Anode", "Cathode", "Anode mud", "Liquid surface"],
     "B", "OSC", "easy",
     "• Pure copper deposits at the cathode.\nCorrect Choice is (B)."),

    ("""In copper electrorefining, the impure blister copper is connected as:""",
     ["Anode", "Cathode", "Neutral rod", "Battery casing"],
     "A", "OSC", "easy",
     "• Impure copper is the anode.\nCorrect Choice is (A)."),

    ("""What happens to the impure anode in copper electrorefining?""",
     ["It gains mass", "It dissolves and shrinks in size", "It catches fire", "It turns green"],
     "B", "OSC", "easy",
     "• Copper atoms oxidize into solution, shrinking the anode.\nCorrect Choice is (B)."),

    ("""What is anode mud?""",
     ["Melted glass", "Insoluble impurities of noble metals (Ag, Au) beneath the anode", "Rust on the tank", "Plastic residue"],
     "B", "OSC", "easy",
     "• Insoluble noble metals form anode mud.\nCorrect Choice is (B)."),

    ("""In electroplating, the article to be plated is made the:""",
     ["Anode", "Cathode", "Electrolyte", "Heater"],
     "B", "OSC", "easy",
     "• The object must be the cathode.\nCorrect Choice is (B)."),

    ("""In silver plating, what is used as the anode?""",
     ["A piece of pure silver", "A carbon rod", "An iron plate", "A copper wire"],
     "A", "OSC", "easy",
     "• Pure silver is the anode.\nCorrect Choice is (A)."),

    ("""Why is DC used for electrolysis rather than AC?""",
     ["AC reverses direction rapidly, undoing deposition", "AC has zero voltage", "AC is too cheap", "DC is flammable"],
     "A", "OSC", "easy",
     "• DC provides constant unidirectional ion migration.\nCorrect Choice is (A)."),

    ("""What type of current is supplied by a chemical battery?""",
     ["Alternating Current (AC)", "Direct Current (DC)", "Three-phase current", "Static current"],
     "B", "OSC", "easy",
     "• Batteries provide DC.\nCorrect Choice is (B)."),

    ("""What is the colour of copper metal deposited on the cathode?""",
     ["Bright yellow", "Reddish-brown", "Deep black", "White"],
     "B", "OSC", "easy",
     "• Metallic copper is reddish-brown.\nCorrect Choice is (B)."),

    ("""Which ion discharges at the cathode during electrolysis of \\(\\text{CuSO}_4\\)?""",
     ["\\(\\text{SO}_4^{2-}\\)", "\\(\\text{Cu}^{2+}\\)", "\\(\\text{OH}^-\\)", "\\(\\text{O}^{2-}\\)"],
     "B", "OSC", "easy",
     "• \\(\\text{Cu}^{2+}\\) discharges at the cathode.\nCorrect Choice is (B)."),

    ("""State True or False: Oxidation occurs at the anode.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True (Anode = Oxidation).\nCorrect Choice is (A)."),

    ("""State True or False: Reduction occurs at the cathode.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True (Cathode = Reduction).\nCorrect Choice is (A)."),

    ("""What happens to an electrolyte during electrolysis?""",
     ["It gets boiled into steam", "It undergoes chemical decomposition into simpler substances", "It freezes", "It disappears"],
     "B", "OSC", "easy",
     "• Chemical decomposition occurs.\nCorrect Choice is (B)."),

    ("""Which metal is commonly plated on iron to prevent rusting?""",
     ["Chromium or Zinc", "Lead", "Mercury", "Sodium"],
     "A", "OSC", "easy",
     "• Zinc (galvanizing) and chromium protect iron.\nCorrect Choice is (A)."),

    ("""What is electroplating iron with zinc called?""",
     ["Galvanizing", "Anodizing", "Smelting", "Annealing"],
     "A", "OSC", "easy",
     "• Coating zinc on iron is galvanizing.\nCorrect Choice is (A)."),

    ("""If \\(30\\text{ mL}\\) of hydrogen is collected, how much oxygen is formed in water electrolysis?""",
     ["\\(15\\text{ mL}\\)", "\\(30\\text{ mL}\\)", "\\(60\\text{ mL}\\)", "\\(10\\text{ mL}\\)"],
     "A", "OSC", "easy",
     "• Oxygen volume is half of hydrogen: \\(30 / 2 = 15\\text{ mL}\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: Cations are attracted to the ________ during electrolysis.""",
     ["Anode", "Cathode", "Switch", "Battery cover"],
     "B", "OFB", "easy",
     "• Cations migrate to the cathode.\nCorrect Choice is (B)."),

    ("""Fill in the blank: Anions are attracted to the ________ during electrolysis.""",
     ["Cathode", "Anode", "Wire", "Bulb"],
     "B", "OFB", "easy",
     "• Anions migrate to the anode.\nCorrect Choice is (B)."),

    ("""What gas rekindles a glowing splint in water electrolysis?""",
     ["Hydrogen", "Oxygen", "Nitrogen", "Carbon dioxide"],
     "B", "OSC", "easy",
     "• Oxygen supports combustion and rekindles a glowing splint.\nCorrect Choice is (B)."),

    ("""What is an electrolyte?""",
     ["A solid insulator", "A substance that conducts electricity when dissolved in water or melted and decomposes chemically", "A type of wire", "A magnetic metal"],
     "B", "OSC", "easy",
     "• An electrolyte is an ionic conductor in liquid state.\nCorrect Choice is (B)."),

    ("""Which of the following is a strong electrolyte?""",
     ["Pure water", "Aqueous sodium chloride (\\(\\text{NaCl}\\))", "Sugar solution", "Alcohol"],
     "B", "OSC", "easy",
     "• \\(\\text{NaCl}\\) is fully dissociated into ions.\nCorrect Choice is (B)."),

    ("""What happens to cathode mass during electroplating?""",
     ["Decreases", "Increases as metal deposits on it", "Remains zero", "Becomes negative"],
     "B", "OSC", "easy",
     "• Cathode gains mass from depositing metal.\nCorrect Choice is (B).")
]

# 12 Foundation Mock Questions (501-512) with rich embedded vector SVGs
foundation_data = [
    # 501: Hofmann Voltameter 2:1 Gas Ratio Diagram
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Hofmann Voltameter (Water Electrolysis)</text>
  <!-- Left Tube: Cathode (H2) -->
  <rect x="70" y="50" width="30" height="130" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <rect x="71" y="51" width="28" height="60" fill="#38bdf8" opacity="0.3"/>
  <text x="73" y="80" fill="#38bdf8" font-size="9" font-weight="bold">2 Vol H₂</text>
  <text x="65" y="195" fill="#38bdf8" font-size="9" font-weight="bold">Cathode (-)</text>
  <!-- Right Tube: Anode (O2) -->
  <rect x="230" y="50" width="30" height="130" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
  <rect x="231" y="51" width="28" height="30" fill="#ef4444" opacity="0.3"/>
  <text x="233" y="70" fill="#f87171" font-size="9" font-weight="bold">1 Vol O₂</text>
  <text x="225" y="195" fill="#f87171" font-size="9" font-weight="bold">Anode (+)</text>
  <!-- Central Funnel Tube -->
  <rect x="150" y="40" width="30" height="140" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
  <polygon points="140,40 190,40 180,60 150,60" fill="#334155"/>
  <text x="142" y="32" fill="#cbd5e1" font-size="8">Acidulated H₂O</text>
  <!-- Horizontal connecting bridge -->
  <rect x="100" y="150" width="130" height="15" fill="#1e293b" stroke="#94a3b8"/>
  <text x="45" y="218" fill="#34d399" font-size="10">Stoichiometric Volume Ratio H₂ : O₂ = 2 : 1 (Proves H₂O)</text>
</svg>
</div>
In the Hofmann voltameter apparatus shown above, why is the height of gas collected in the left limb (cathode) exactly double the height of gas collected in the right limb (anode)?""",
     ["Because hydrogen expands twice as much as oxygen in glass",
      "Because every two molecules of water decompose into two molecules of hydrogen gas and one molecule of oxygen gas (\\(2\\text{H}_2\\text{O} \\to 2\\text{H}_2 + \\text{O}_2\\)), which occupy volumes in a strict \\(2:1\\) ratio by Avogadro's law",
      "Because oxygen dissolves completely in acid",
      "Because the left tube has a wider diameter"],
     "B", "OSC", "easy",
     "• Water stoichiometry produces 2 moles of \\(\\text{H}_2\\) per 1 mole of \\(\\text{O}_2\\). By Avogadro's law, equal moles of gases occupy equal volumes, resulting in a strict \\(2:1\\) volume ratio.\nCorrect Choice is (B)."),

    # 502: Copper Electrorefining Cell Anatomy
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Industrial Copper Electrorefining</text>
  <!-- Electrolytic Tank -->
  <rect x="40" y="55" width="260" height="120" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <rect x="42" y="80" width="256" height="92" fill="#0284c7" opacity="0.3"/>
  <text x="120" y="100" fill="#93c5fd" font-size="9">CuSO₄ + Dil. H₂SO₄</text>
  <!-- Anode (Impure Blister Copper) -->
  <rect x="75" y="65" width="22" height="90" fill="#78350f" stroke="#b45309" stroke-width="2"/>
  <text x="65" y="170" fill="#f59e0b" font-size="9" font-weight="bold">Anode (+)</text>
  <text x="50" y="182" fill="#cbd5e1" font-size="8">Impure Blister Cu</text>
  <!-- Cathode (Pure Copper) -->
  <rect x="235" y="65" width="12" height="90" fill="#ea580c" stroke="#f97316" stroke-width="2"/>
  <text x="225" y="170" fill="#10b981" font-size="9" font-weight="bold">Cathode (-)</text>
  <text x="215" y="182" fill="#cbd5e1" font-size="8">Pure Cu (99.99%)</text>
  <!-- Anode Mud -->
  <ellipse cx="85" cy="172" rx="16" ry="5" fill="#fde047"/>
  <text x="55" y="200" fill="#fde047" font-size="8">Anode Mud (Ag, Au)</text>
  <text x="40" y="218" fill="#34d399" font-size="9">Cu (Anode) ⟶ Cu²⁺ + 2e⁻ | Cu²⁺ + 2e⁻ ⟶ Cu (Cathode)</text>
</svg>
</div>
In the copper refining cell illustrated above, why does the concentration of copper sulphate in the electrolyte remain unchanged throughout the entire refining process?""",
     ["Because copper ions cannot leave the solution",
      "Because the rate at which copper atoms dissolve from the impure anode as \\(\\text{Cu}^{2+}\\) ions strictly equals the rate at which \\(\\text{Cu}^{2+}\\) ions deposit as pure copper on the cathode",
      "Because water turns into copper",
      "Because the battery pumps fresh copper sulphate into the tank"],
     "B", "OSC", "medium",
     "• Rate of oxidation (\\(\\text{Cu} \\to \\text{Cu}^{2+}\\)) at anode equals rate of reduction (\\(\\text{Cu}^{2+} \\to \\text{Cu}\\)) at cathode; net \\([\\text{Cu}^{2+}]\\) remains constant.\nCorrect Choice is (B)."),

    # 503: Electroplating of Spoon Setup
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Electroplating a Spoon with Silver</text>
  <!-- Tank -->
  <rect x="40" y="55" width="260" height="120" fill="#1e293b" stroke="#94a3b8" rx="4"/>
  <rect x="42" y="80" width="256" height="92" fill="#38bdf8" opacity="0.2"/>
  <!-- Pure Silver Anode -->
  <rect x="75" y="65" width="20" height="85" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
  <text x="65" y="170" fill="#f59e0b" font-size="9" font-weight="bold">Anode (+)</text>
  <text x="60" y="182" fill="#cbd5e1" font-size="8">Pure Silver Plate</text>
  <!-- Spoon as Cathode -->
  <path d="M 240 65 L 240 125 Q 240 150 225 150 Q 210 150 210 125 Z" fill="#94a3b8" stroke="#cbd5e1"/>
  <text x="210" y="170" fill="#10b981" font-size="9" font-weight="bold">Cathode (-)</text>
  <text x="210" y="182" fill="#cbd5e1" font-size="8">Metal Spoon</text>
  <!-- Battery and circuit on top -->
  <line x1="85" y1="65" x2="85" y2="45" stroke="#ef4444" stroke-width="2"/>
  <line x1="85" y1="45" x2="150" y2="45" stroke="#ef4444" stroke-width="2"/>
  <line x1="180" y1="45" x2="230" y2="45" stroke="#3b82f6" stroke-width="2"/>
  <line x1="230" y1="45" x2="230" y2="65" stroke="#3b82f6" stroke-width="2"/>
  <rect x="150" y="38" width="30" height="14" fill="#334155" stroke="#f59e0b"/>
  <text x="156" y="49" fill="#fde047" font-size="9">DC</text>
  <text x="40" y="210" fill="#34d399" font-size="9">Ag⁺ ions in solution migrate to spoon (-ve) and deposit as shiny silver film</text>
</svg>
</div>
In the silver plating experiment shown above, what critical error would occur if an inexperienced student reversed the battery connections, making the spoon the ANODE and the silver plate the CATHODE?""",
     ["The spoon would be plated with double thickness",
      "The metallic spoon would corrode and dissolve into the electrolyte, while silver would plate wastefully onto the silver plate",
      "The battery would explode",
      "The solution would freeze solid"],
     "B", "OSC", "medium",
     "• At the anode, metal oxidizes and dissolves. If the spoon were the anode, it would be corroded away into ions rather than coated.\nCorrect Choice is (B)."),

    # 504: Cation vs Anion Migration Direction Vectors
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Ion Migration Vectors in Electric Field</text>
  <!-- Positive Anode Electrode -->
  <rect x="40" y="55" width="20" height="110" fill="#b91c1c" stroke="#ef4444" stroke-width="2"/>
  <text x="32" y="185" fill="#f87171" font-size="10" font-weight="bold">ANODE (+)</text>
  <!-- Negative Cathode Electrode -->
  <rect x="280" y="55" width="20" height="110" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2"/>
  <text x="265" y="185" fill="#60a5fa" font-size="10" font-weight="bold">CATHODE (-)</text>
  <!-- Anions migrating left to Anode -->
  <circle cx="120" cy="85" r="10" fill="#ef4444"/>
  <text x="114" y="89" fill="#fff" font-size="10" font-weight="bold">-</text>
  <line x1="110" y1="85" x2="70" y2="85" stroke="#ef4444" stroke-width="2.5"/>
  <polygon points="65,85 75,80 75,90" fill="#ef4444"/>
  <text x="80" y="105" fill="#fca5a5" font-size="9">Anions (-ve) ⟶ Anode</text>
  <!-- Cations migrating right to Cathode -->
  <circle cx="200" cy="135" r="10" fill="#3b82f6"/>
  <text x="195" y="139" fill="#fff" font-size="10" font-weight="bold">+</text>
  <line x1="210" y1="135" x2="250" y2="135" stroke="#3b82f6" stroke-width="2.5"/>
  <polygon points="255,135 245,130 245,140" fill="#3b82f6"/>
  <text x="175" y="155" fill="#93c5fd" font-size="9">Cations (+ve) ⟶ Cathode</text>
</svg>
</div>
Which mnemonic correctly associates ions with their respective target electrodes in an electrolytic cell?""",
     ["Anions go to Cathode, Cations go to Anode",
      "ANIONS (negatively charged) migrate to the ANODE (+ve), while CATIONS (positively charged) migrate to the CATHODE (-ve)",
      "All ions move to the cathode simultaneously",
      "Ions do not move in an electric field"],
     "B", "OSC", "easy",
     "• Opposite charges attract: negative Anions seek the positive Anode; positive Cations seek the negative Cathode.\nCorrect Choice is (B)."),

    # 505: Inert vs Active Electrodes Comparison in CuSO4
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Inert vs Active Electrodes in CuSO₄ Electrolysis</text>
  <!-- Setup A: Inert Platinum/Graphite -->
  <rect x="25" y="55" width="135" height="100" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="35" y="75" fill="#fde047" font-size="10" font-weight="bold">A. Inert Electrodes (Pt/C):</text>
  <text x="35" y="95" fill="#cbd5e1" font-size="8">• Cathode: Cu²⁺ + 2e⁻ → Cu</text>
  <text x="35" y="110" fill="#cbd5e1" font-size="8">• Anode: 4OH⁻ → 2H₂O+O₂↑+4e⁻</text>
  <text x="35" y="130" fill="#ef4444" font-size="9" font-weight="bold">Blue color FADES away!</text>
  <!-- Setup B: Active Copper Electrodes -->
  <rect x="180" y="55" width="135" height="100" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="190" y="75" fill="#34d399" font-size="10" font-weight="bold">B. Active Electrodes (Cu):</text>
  <text x="190" y="95" fill="#cbd5e1" font-size="8">• Cathode: Cu²⁺ + 2e⁻ → Cu</text>
  <text x="190" y="110" fill="#cbd5e1" font-size="8">• Anode: Cu → Cu²⁺ + 2e⁻</text>
  <text x="190" y="130" fill="#38bdf8" font-size="9" font-weight="bold">Blue color STAYS constant!</text>
  <text x="40" y="185" fill="#cbd5e1" font-size="10">Active anode dissolves to replenish consumed cations</text>
</svg>
</div>
Comparing setups A and B above, why does the electrolyte color fade in setup A but remain deep blue in setup B?""",
     ["Inert electrodes absorb blue pigment from the water",
      "In setup A, \\(\\text{Cu}^{2+}\\) ions are removed onto the cathode without replenishment, fading the blue color; in setup B, the copper anode dissolves to replace every \\(\\text{Cu}^{2+}\\) ion plated onto the cathode",
      "Setup B produces green paint",
      "Setup A runs out of electricity"],
     "B", "OSC", "hard",
     "• Inert anodes evolve oxygen gas rather than dissolving copper, permanently consuming \\(\\text{Cu}^{2+}\\) ions from solution. Active copper anodes replenish \\(\\text{Cu}^{2+}\\) continuously.\nCorrect Choice is (B)."),

    # 506: Preferential Discharge Order (Electrochemical Series)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Selective Discharge of Cations</text>
  <!-- Vertical ladder -->
  <rect x="40" y="55" width="120" height="120" fill="#1e293b" stroke="#94a3b8" rx="3"/>
  <text x="50" y="75" fill="#ef4444" font-size="10">K⁺, Na⁺, Ca²⁺, Mg²⁺</text>
  <text x="50" y="95" fill="#f59e0b" font-size="10">Al³⁺, Zn²⁺, Fe²⁺</text>
  <text x="50" y="120" fill="#fde047" font-size="11" font-weight="bold">H⁺ (Hydrogen)</text>
  <text x="50" y="145" fill="#10b981" font-size="11" font-weight="bold">Cu²⁺ (Copper)</text>
  <text x="50" y="165" fill="#38bdf8" font-size="10">Ag⁺ (Silver)</text>
  <!-- Downward arrow -->
  <line x1="180" y1="65" x2="180" y2="165" stroke="#34d399" stroke-width="3"/>
  <polygon points="180,170 175,160 185,160" fill="#34d399"/>
  <text x="195" y="105" fill="#34d399" font-size="10" font-weight="bold">Ease of Discharge</text>
  <text x="195" y="120" fill="#34d399" font-size="10" font-weight="bold">INCREASES (↓)</text>
  <text x="195" y="140" fill="#cbd5e1" font-size="8">Lower in series discharges</text>
  <text x="195" y="152" fill="#cbd5e1" font-size="8">preferentially at cathode</text>
</svg>
</div>
When an aqueous solution containing BOTH \\(\\text{Na}^+\\) and \\(\\text{Cu}^{2+}\\) ions is electrolyzed, which ion will discharge first at the cathode and why?""",
     ["\\(\\text{Na}^+\\) discharges first because it is lighter",
      "\\(\\text{Cu}^{2+}\\) discharges first because it lies lower in the electrochemical series and has a much higher standard reduction potential, accepting electrons more readily than \\(\\text{Na}^+\\)",
      "Both discharge simultaneously as a brass alloy",
      "Neither discharges; water freezes"],
     "B", "OSC", "hard",
     "• Ions lower in the electrochemical series have higher reduction potentials and discharge preferentially at the cathode. Hence \\(\\text{Cu}^{2+}\\) discharges as metallic copper rather than \\(\\text{Na}^+\\).\nCorrect Choice is (B)."),

    # 507: Water Electrolysis Gas Verification Tests
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Identification of Water Electrolysis Gases</text>
  <!-- Cathode Gas: Hydrogen -->
  <rect x="25" y="55" width="135" height="90" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="35" y="75" fill="#38bdf8" font-size="11" font-weight="bold">Cathode Gas (H₂):</text>
  <text x="35" y="95" fill="#cbd5e1" font-size="9">• Burning splinter brought near</text>
  <text x="35" y="112" fill="#fde047" font-size="11" font-weight="bold">Burns with 'POP' sound!</text>
  <text x="35" y="130" fill="#cbd5e1" font-size="8">Combustible gas</text>
  <!-- Anode Gas: Oxygen -->
  <rect x="180" y="55" width="135" height="90" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="190" y="75" fill="#f87171" font-size="11" font-weight="bold">Anode Gas (O₂):</text>
  <text x="190" y="95" fill="#cbd5e1" font-size="9">• Glowing splinter inserted</text>
  <text x="190" y="112" fill="#ef4444" font-size="11" font-weight="bold">REKINDLES INTO FLAME!</text>
  <text x="190" y="130" fill="#cbd5e1" font-size="8">Supporter of combustion</text>
  <text x="40" y="180" fill="#34d399" font-size="10">H₂ is combustible; O₂ supports combustion</text>
</svg>
</div>
How can a student unambiguously verify the identity of the two gases collected in the inverted test tubes of a water electrolysis cell?""",
     ["By tasting both gases",
      "Bringing a burning splinter to the cathode gas causes it to burn with a pop sound (confirming \\(\\text{H}_2\\)), while inserting a glowing splinter into the anode gas causes it to burst into bright flame (confirming \\(\\text{O}_2\\))",
      "By shining laser light through the tubes",
      "By smelling the odors"],
     "B", "OSC", "easy",
     "• Hydrogen combusts with a signature pop sound; oxygen reignites a glowing wooden splinter, unambiguously identifying each gas.\nCorrect Choice is (B)."),

    # 508: Faraday's First Law Conceptual Basis
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Charge vs Mass Deposited (m ∝ Q)</text>
  <!-- Formula Box -->
  <rect x="35" y="55" width="270" height="45" fill="#334155" stroke="#38bdf8" rx="4"/>
  <text x="50" y="82" fill="#38bdf8" font-size="14" font-weight="bold">m = Z · Q = Z · I · t</text>
  <!-- Explanations -->
  <text x="40" y="125" fill="#cbd5e1" font-size="10">• m = Mass of substance liberated at electrode</text>
  <text x="40" y="145" fill="#cbd5e1" font-size="10">• Q = Total electric charge passed (Current I × Time t)</text>
  <text x="40" y="165" fill="#fde047" font-size="10">• Z = Electrochemical Equivalent of the substance</text>
  <text x="40" y="195" fill="#34d399" font-size="10">Doubling the current or plating duration strictly doubles the deposited metal</text>
</svg>
</div>
According to Faraday's First Law of Electrolysis (\\(m = Z \\cdot I \\cdot t\\)), if an electroplating workshop doubles the electric current from \\(2\\text{ A}\\) to \\(4\\text{ A}\\) while plating for the exact same duration, what happens to the mass of silver deposited on the cathode?""",
     ["The mass remains unchanged",
      "The mass of silver deposited is exactly doubled",
      "The mass quadruples",
      "Zero silver is deposited"],
     "B", "OSC", "medium",
     "• Mass is directly proportional to charge: \\(m \\propto Q = I \\cdot t\\). Doubling the current \\(I\\) at constant time \\(t\\) doubles the deposited mass.\nCorrect Choice is (B)."),

    # 509: Anode Mud Refining Economics
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="70" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Composition of Copper Anode Mud</text>
  <!-- Anode Mud Particles -->
  <rect x="35" y="55" width="270" height="90" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="45" y="78" fill="#fde047" font-size="11" font-weight="bold">Recovered Precious By-Products:</text>
  <text x="45" y="100" fill="#cbd5e1" font-size="10">• Gold (Au) &amp; Silver (Ag)</text>
  <text x="45" y="118" fill="#cbd5e1" font-size="10">• Platinum (Pt) &amp; Palladium (Pd)</text>
  <text x="45" y="135" fill="#cbd5e1" font-size="10">• Selenium (Se) &amp; Tellurium (Te)</text>
  <text x="40" y="175" fill="#34d399" font-size="10">The value of gold and silver extracted from anode mud often</text>
  <text x="40" y="195" fill="#34d399" font-size="10">covers the entire electrical operating cost of the refinery!</text>
</svg>
</div>
Why is the 'anode mud' collected at the bottom of copper refining tanks economically significant to metallurgical corporations?""",
     ["It is used to make cement",
      "It contains concentrated deposits of noble precious metals (Gold, Silver, Platinum) that were present as impurities in the raw copper ore and did not dissolve into the electrolyte",
      "It is converted into chemical fertilizer",
      "It is a radioactive fuel for nuclear reactors"],
     "B", "OSC", "easy",
     "• Unreactive precious metals (Au, Ag, Pt) do not oxidize at the cell potential and settle out, providing lucrative precious metal yields.\nCorrect Choice is (B)."),

    # 510: Electroplating Industrial Thickness Quality Criteria
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Quality Factors in Electroplating</text>
  <!-- Factor 1 -->
  <rect x="30" y="55" width="80" height="75" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="35" y="75" fill="#38bdf8" font-size="9" font-weight="bold">1. Current</text>
  <text x="35" y="95" fill="#cbd5e1" font-size="8">Low, steady DC</text>
  <text x="35" y="110" fill="#cbd5e1" font-size="8">prevents rough</text>
  <text x="35" y="122" fill="#cbd5e1" font-size="8">nodular growth</text>
  <!-- Factor 2 -->
  <rect x="130" y="55" width="80" height="75" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="135" y="75" fill="#34d399" font-size="9" font-weight="bold">2. Cleaning</text>
  <text x="135" y="95" fill="#cbd5e1" font-size="8">Degreased surface</text>
  <text x="135" y="110" fill="#cbd5e1" font-size="8">ensures atomic</text>
  <text x="135" y="122" fill="#cbd5e1" font-size="8">adhesion</text>
  <!-- Factor 3 -->
  <rect x="230" y="55" width="80" height="75" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="235" y="75" fill="#fde047" font-size="9" font-weight="bold">3. Complex Ions</text>
  <text x="235" y="95" fill="#cbd5e1" font-size="8">Cyanide complexes</text>
  <text x="235" y="110" fill="#cbd5e1" font-size="8">release ions</text>
  <text x="235" y="122" fill="#cbd5e1" font-size="8">slowly &amp; evenly</text>
  <text x="35" y="175" fill="#38bdf8" font-size="10">Produces dense, mirror-bright, peel-resistant coatings</text>
</svg>
</div>
Why are complex cyanide salts (such as sodium dicyanoargentate, \\(\\text{Na[Ag(CN)}_2]\\)) preferred over simple silver nitrate (\\(\\text{AgNO}_3\\)) for commercial silver electroplating?""",
     ["Because silver nitrate is explosive",
      "Because simple silver nitrate dissociates completely, causing rapid, uneven, coarse crystal deposition that flakes off easily; complex cyanide dissociates slowly, providing a low, steady \\([\\text{Ag}^+]\\) that yields an ultra-smooth, adherent, mirror-like finish",
      "Because cyanide is sweet-tasting",
      "Because silver nitrate conducts zero current"],
     "B", "OSC", "hard",
     "• Rapid reduction from simple \\(\\text{AgNO}_3\\) produces brittle, loose powdery crystals. Low free \\(\\text{Ag}^+\\) maintained by complex equilibrium ensures fine-grained, cohesive plating.\nCorrect Choice is (B)."),

    # 511: Electronic vs Electrolytic Conduction Comparison
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Metallic vs Electrolytic Conduction</text>
  <!-- Metallic Conduction -->
  <rect x="25" y="55" width="135" height="90" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="35" y="75" fill="#38bdf8" font-size="10" font-weight="bold">Metallic Conduction:</text>
  <text x="35" y="95" fill="#cbd5e1" font-size="8">• Carried by FREE ELECTRONS</text>
  <text x="35" y="110" fill="#cbd5e1" font-size="8">• No chemical change in wire</text>
  <text x="35" y="125" fill="#cbd5e1" font-size="8">• Resistance increases with T</text>
  <!-- Electrolytic Conduction -->
  <rect x="180" y="55" width="135" height="90" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="190" y="75" fill="#34d399" font-size="10" font-weight="bold">Electrolytic Conduction:</text>
  <text x="190" y="95" fill="#cbd5e1" font-size="8">• Carried by MOBILE IONS</text>
  <text x="190" y="110" fill="#cbd5e1" font-size="8">• Involves chemical decomposition</text>
  <text x="190" y="125" fill="#cbd5e1" font-size="8">• Resistance decreases with T</text>
  <text x="40" y="180" fill="#fde047" font-size="10">Matter is physically transported in electrolytes; not in metals</text>
</svg>
</div>
What fundamental distinction exists between electrical conduction through a solid copper wire and conduction through an aqueous copper sulphate electrolyte?""",
     ["Copper wires conduct only AC, while electrolytes conduct DC",
      "In a copper wire, current is carried strictly by free electrons with zero transfer of matter or chemical change; in an electrolyte, current is carried by mobile ions and results in physical transport of matter and chemical decomposition",
      "Electrolytes have zero electrical resistance",
      "Copper wire loses mass when conducting current"],
     "B", "OSC", "medium",
     "• Metallic conduction involves electron drift through a stationary positive lattice without material change. Electrolytic conduction physically transports ions to electrodes where redox reactions occur.\nCorrect Choice is (B)."),

    # 512: Overall Electrolysis Energy Balance
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Electrolysis as Energy Conversion</text>
  <text x="35" y="60" fill="#cbd5e1" font-size="11">Electrical Energy In ⟶ Chemical Potential Energy Out</text>
  <!-- Reaction block -->
  <rect x="30" y="75" width="280" height="75" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="45" y="100" fill="#34d399" font-size="12" font-weight="bold">2 H₂O(l) + Electrical Energy ⟶ 2 H₂(g) + O₂(g)</text>
  <text x="45" y="125" fill="#fde047" font-size="10">ΔH = +285.8 kJ per mole of H₂ produced (Endothermic)</text>
  <text x="45" y="140" fill="#cbd5e1" font-size="9">Stored chemical potential can be recovered in Fuel Cells!</text>
  <text x="40" y="185" fill="#38bdf8" font-size="10">Green Hydrogen produced via water electrolysis is the clean fuel of the future</text>
</svg>
</div>
From a thermodynamic perspective, what kind of energy conversion takes place during water electrolysis?""",
     ["Chemical energy is converted into kinetic energy",
      "Electrical energy supplied from the DC source is converted and stored as chemical bond potential energy in high-energy gaseous hydrogen and oxygen molecules (\\(\\Delta H > 0\\))",
      "Thermal energy is destroyed",
      "Nuclear energy is released"],
     "B", "OSC", "medium",
     "• Electrolysis is an endothermic, non-spontaneous process that converts electrical work into chemical potential energy stored in fuel molecules like \\(\\text{H}_2\\).\nCorrect Choice is (B).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-5-5.5-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-5-5.5-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-5-5.5-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch5_topic5.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
